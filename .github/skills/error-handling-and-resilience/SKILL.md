---
name: error-handling-and-resilience
description: Designs resilient error handling for production systems. Use when implementing error boundaries, retry logic, circuit breakers, graceful degradation, or dead letter queues. Use when building any service that must tolerate failures without cascading.
---

# Error Handling and Resilience

## Architectural Rules
- **Fail Fast, Fail Safe**: Enforce connection timeouts on all external network and database calls. Default to safe states (deny access, fallback cache) if services are unreachable.
- **Blast Radius Isolation**: Never let transient errors inside a single task crash an entire batch runner or the host thread pool. Keep loops guarded with try-catch blocks.
- **Timeout Restrictions**: Avoid unbounded wait loops. Configure clear maximum query execution timeouts.

## Resilience Patterns
- **Retry with Jittered Backoff**: Apply exponential backoff with randomized jitter on transient faults (HTTP 429/503/504, DB locks). Never retry 400/401/403/404 errors or non-idempotent mutations.
- **Circuit Breaker**: Track failure thresholds for dependent endpoints. Open the circuit to block requests immediately, allowing failing systems time to recover before switching to half-open.
- **Graceful Degradation**: If an optional downstream API fails, serve cached stale data or default empty states rather than throwing user-visible crashes.
- **Idempotency keys**: Ensure critical mutations (e.g. payment transactions) require unique idempotency keys or perform state validation before executing.
- **Dead Letter Queue (DLQ)**: Route persistently failing queue messages to a DLQ after exhausted attempts to prevent head-of-line blocking.

## Verification Checklist
- [ ] Every external integration and database client has a configured timeout.
- [ ] All retry loops enforce exponential backoff and randomized jitter.
- [ ] Critical state-changing endpoints support idempotent retries.
- [ ] Non-essential components degrade to fallback mock/cache states.
- [ ] Unit/Integration tests actively mock and verify timeout and error paths.
