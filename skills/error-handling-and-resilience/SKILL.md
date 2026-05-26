---
name: error-handling-and-resilience
description: Designs resilient error handling for production systems. Use when implementing error boundaries, retry logic, circuit breakers, graceful degradation, or dead letter queues. Use when building any service that must tolerate failures without cascading.
---

# Error Handling and Resilience

## Overview

Production systems fail. Networks partition, services restart, databases time out, queues overflow. Resilience is the discipline of designing systems that degrade gracefully under failure rather than collapsing catastrophically. This skill covers the patterns that keep a system alive when things break — and make failures observable, recoverable, and bounded in blast radius.

## When to Use

- Building any service that calls external systems (APIs, databases, caches, queues)
- Implementing retry logic for transient failures
- Designing error boundaries between components or services
- Adding circuit breakers to prevent cascading failures
- Planning graceful degradation paths (what happens when a dependency is down)
- Building idempotent operations (safe to retry without duplication)
- Designing dead letter queues or poison message handling

**When NOT to use:**

- Pure in-process logic with no external I/O
- One-off scripts where failure means "stop and fix"
- Trivial CRUD with no concurrency or external dependencies
- Prototypes where resilience requirements are explicitly waived

## Core Principles

### 1. Fail Fast, Fail Safe

A system should detect failures quickly and react before the failure propagates:

```
FAIL FAST:
  → Timeout early (don't hang indefinitely)
  → Validate at boundaries (catch bad input before it enters the system)
  → Health-check dependencies at startup (fail on boot, not mid-request)

FAIL SAFE:
  → Default to denying access if auth is unreachable (not granting)
  → Return cached/stale data rather than crashing
  → Close connections, release locks on error paths
```

### 2. Blast Radius Isolation

Failures in one component must not cascade to unrelated components:

```python
# BAD: Uncaught failure in one task kills the entire batch
def process_all(tasks: list[Task]) -> list[Result]:
    results = []
    for task in tasks:
        results.append(dangerous_operation(task))  # One exception kills everything
    return results

# GOOD: Isolate failures per task, log context, continue
def process_all(tasks: list[Task]) -> list[Result]:
    results: list[Result] = []
    for task in tasks:
        try:
            results.append(dangerous_operation(task))
        except Exception as exc:
            logger.exception("Task %s failed", task.id, exc_info=exc)
            results.append(Result.error(task.id, str(exc)))
    return results
```

## Patterns

### Retry with Backoff

Transient failures (network blips, brief service restarts) resolve on retry. But naive retry makes things worse under load (thundering herd).

```python
import time
import random

def retry_with_backoff(
    func,
    max_retries: int = 3,
    base_delay: float = 1.0,
    max_delay: float = 60.0,
    jitter: bool = True,
):
    """Retry with exponential backoff and optional jitter."""
    for attempt in range(max_retries + 1):
        try:
            return func()
        except TransientError as exc:
            if attempt == max_retries:
                raise
            delay = min(base_delay * (2 ** attempt), max_delay)
            if jitter:
                delay = delay * (0.5 + random.random())  # +/- 50% jitter
            logger.warning("Attempt %d/%d failed, retrying in %.1fs: %s",
                           attempt + 1, max_retries + 1, delay, exc)
            time.sleep(delay)
```

**When to retry:**
- HTTP 429 (rate limit), 503 (unavailable), 504 (gateway timeout)
- Database deadlocks or serialization failures
- Temporary DNS or connection failures

**When NOT to retry:**
- HTTP 400 (bad request), 401 (unauthorized), 403 (forbidden), 404 (not found)
- Validation errors (retrying the same bad input produces the same error)
- Side-effecting operations that aren't idempotent

### Circuit Breaker

When a downstream service is failing repeatedly, stop calling it entirely. Give it time to recover. This prevents a slow dependency from exhausting your own thread pool/connection pool.

```
Circuit breaker states:
  CLOSED ──→ failures exceed threshold ──→ OPEN
    ▲                                         │
    │                                   timeout expires
    │                                         │
    └──── failures below threshold ──── HALF-OPEN
```

```python
from dataclasses import dataclass, field
import time
from enum import Enum, auto

class CircuitState(Enum):
    CLOSED = auto()
    OPEN = auto()
    HALF_OPEN = auto()

@dataclass
class CircuitBreaker:
    failure_threshold: int = 5
    recovery_timeout: float = 30.0
    failure_count: int = 0
    last_failure_time: float = 0.0
    state: CircuitState = CircuitState.CLOSED

    def call(self, func):
        if self.state == CircuitState.OPEN:
            if time.time() - self.last_failure_time >= self.recovery_timeout:
                self.state = CircuitState.HALF_OPEN
            else:
                raise CircuitBreakerOpenError()

        try:
            result = func()
            if self.state == CircuitState.HALF_OPEN:
                self.state = CircuitState.CLOSED
                self.failure_count = 0
            return result
        except Exception:
            self.failure_count += 1
            self.last_failure_time = time.time()
            if self.failure_count >= self.failure_threshold:
                self.state = CircuitState.OPEN
            raise
```

### Graceful Degradation

When a dependency is unavailable, serve a degraded experience rather than failing entirely:

```python
async def get_user_dashboard(user_id: str) -> Dashboard:
    profile: UserProfile
    recommendations: list[Recommendation] = []
    notifications: list[Notification] = []

    profile = await get_profile(user_id)  # Required — fail if unavailable

    try:
        recommendations = await get_recommendations(user_id)
    except RecommendationServiceError:
        logger.warning("Recommendations unavailable, serving dashboard without them")
        recommendations = []

    try:
        notifications = await get_notifications(user_id)
    except NotificationServiceError:
        logger.warning("Notifications unavailable, serving dashboard without them")
        notifications = []

    return Dashboard(profile=profile, recommendations=recommendations,
                     notifications=notifications)
```

**Degradation decision flow:**
```
Dependency fails
    │
    ├── Core to the feature? → Fail the request (user must know)
    ├── Enhancement only?    → Degrade gracefully (stale data, empty list, default)
    └── Cached version exists? → Serve stale data with a freshness indicator
```

### Idempotency

Operations that can be safely retried without producing duplicate side effects:

```python
import uuid

async def process_payment(order_id: str, amount: int) -> PaymentResult:
    idempotency_key = f"payment:{order_id}"

    existing = await db.payments.find_one({"idempotency_key": idempotency_key})
    if existing:
        return existing  # Already processed — return the same result

    result = await payment_gateway.charge(order_id, amount)
    await db.payments.insert_one({
        "order_id": order_id,
        "amount": amount,
        "status": result.status,
        "idempotency_key": idempotency_key,
    })
    return result
```

**Idempotency strategies:**
- **Natural key:** Operation already has a unique identifier (e.g., `order_id + action`)
- **Idempotency key:** Require caller to provide a unique key per operation
- **State check:** Before acting, check if the operation was already performed
- **Upsert/put semantics:** `INSERT ... ON CONFLICT DO NOTHING`, `PUT` instead of `POST`

### Dead Letter Queue

Messages that repeatedly fail processing should be moved aside so they don't block the queue:

```python
async def process_with_dlq(message: Message, max_attempts: int = 3) -> None:
    attempt = message.headers.get("retry_count", 0)

    try:
        await process_message(message)
    except Exception as exc:
        if attempt >= max_attempts:
            logger.error("Message %s failed after %d attempts, routing to DLQ",
                         message.id, max_attempts, exc_info=exc)
            await dlq.publish(message, error=str(exc), attempts=attempt)
        else:
            message.headers["retry_count"] = attempt + 1
            delay = 2 ** attempt  # Exponential backoff on the queue
            await queue.publish(message, delay=delay)
            raise  # Let the queue handler NACK this delivery
```

### Timeout Patterns

Every external call must have a timeout. Unbounded waits exhaust thread pools and cascade failure:

```python
import asyncio

async def fetch_with_timeout(url: str, timeout: float = 30.0) -> bytes:
    try:
        async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=timeout)
        ) as session:
            async with session.get(url) as response:
                return await response.read()
    except asyncio.TimeoutError:
        raise ExternalServiceTimeoutError(
            f"{url} timed out after {timeout}s"
        )

# Database queries need timeouts too
async def query_with_statement_timeout(db, query: str, timeout_ms: int = 5000):
    await db.execute(f"SET statement_timeout = {timeout_ms}")
    return await db.execute(query)
```

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| "The external service is reliable, we don't need retries" | Every service fails eventually. The question is when, not if. Design for it. |
| "I'll add error handling later" | Error handling retrofitted onto existing code is scatter-shot and inconsistent. The error model is part of the interface. |
| "A try/catch at the top level is enough" | Catching at the top level loses context. You can't retry, degrade, or recover without knowing what failed and why. |
| "Retrying is easy, just loop and try again" | Naive retry without backoff creates thundering herd problems and DDoS-es your own dependencies. |
| "Circuit breakers are over-engineering for our scale" | A slow dependency that ties up 10 connections can kill a service at any scale. The breaker pattern is about connection pool protection, not request volume. |
| "We'll just let it crash and restart" | Crash-restart works for stateless services but loses in-flight work, corrupts partial state, and creates restart storms. |
| "If an error can't happen, don't handle it" | "Can't happen" errors are the ones that take down production at 3 AM. Handle them defensively. |

## Red Flags

- External calls without timeouts (database queries, HTTP requests, RPC calls)
- Retry logic without exponential backoff or jitter
- Retry on non-idempotent operations without deduplication
- Catching `Exception` at the top level and logging without recovery
- Error messages that don't include enough context to diagnose (no ID, no input)
- Service that crashes entirely because one optional dependency is down
- Queue consumer that stops processing because one message is poison
- Silent error swallowing (`except: pass`)
- Different error handling patterns in every module (no shared retry/breaker/timeout utilities)

## Verification

After implementing resilience patterns:

- [ ] Every external call has a timeout configured
- [ ] Retry logic includes exponential backoff with jitter
- [ ] Retryable operations are idempotent or use idempotency keys
- [ ] Circuit breakers protect against known slow/unreliable dependencies
- [ ] Non-critical dependencies degrade gracefully rather than crashing the service
- [ ] Poison messages route to a dead letter queue rather than blocking the queue
- [ ] Error messages include diagnostic context (what failed, with what input, after how many attempts)
- [ ] Resilience patterns are shared through the codebase (not re-implemented per module)
- [ ] Unit tests exercise each error path (timeout, retry exhaustion, circuit open)

