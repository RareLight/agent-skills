---
name: code-simplification
description: Reduces unnecessary complexity while preserving intended behavior. Use for a scoped refactor or when complexity obstructs safe maintenance.
applies_when: Complexity has a demonstrated maintenance, correctness, or performance cost.
skip_when: The current complexity is intentional, documented, or outside the requested scope.
risk: medium
requires: [tests-optional]
fallback: Propose simplifications without editing behavior-sensitive code.
outputs: [simplified-change, behavior-evidence]
related_skills: []
---

# Code Simplification

1. Identify the behavior and constraints that must remain stable.
2. Simplify locally by removing duplication, dead paths, accidental indirection, or confusing control flow.
3. Preserve interfaces and side-effect semantics unless the task explicitly changes them.
4. Verify with relevant tests or characterize behavior before and after when tests are unavailable.

## Verification checklist

- [ ] The simplification has a clear maintenance benefit.
- [ ] Intended behavior and contracts remain intact.
