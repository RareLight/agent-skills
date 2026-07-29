---
name: error-handling-and-resilience
description: Designs failure handling for dependencies and workflows with meaningful availability or consistency requirements. Use for external calls, queues, retries, degradation, or error boundaries.
applies_when: A change introduces or modifies failure behavior across an unreliable boundary.
skip_when: The code has no relevant external dependency or failure-mode change.
risk: high
requires: [architecture-context]
fallback: Document the failure mode, safe default, and unavailable resilience mechanism.
outputs: [failure-policy, verification-evidence]
related_skills: []
---

# Error Handling and Resilience

1. Identify failure modes, idempotency, consistency needs, user impact, and safe default.
2. Set bounded timeouts and isolate failures where appropriate.
3. Use retries only for transient, safe-to-retry operations; add backoff/jitter, circuit breaking, caching, queues, or degradation only when justified by the dependency and service objective.
4. Test critical timeout, retry, and recovery paths at a proportionate boundary.

## Verification checklist

- [ ] Failure behavior and safe defaults are explicit.
- [ ] Retries and fallback mechanisms are appropriate to operation semantics.
- [ ] Critical failure paths have evidence.
