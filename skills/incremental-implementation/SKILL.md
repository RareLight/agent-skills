---
name: incremental-implementation
description: Delivers scoped changes in verifiable increments. Use when implementation has multiple logical steps, meaningful risk, or benefits from intermediate feedback.
applies_when: A change cannot be safely or clearly completed in one coherent edit.
skip_when: The maintenance fast path is sufficient.
risk: medium
requires: [writable-workspace]
fallback: Make one scoped change and run the narrowest relevant verification.
outputs: [implemented-change, verification-evidence]
---

# Incremental Implementation

1. Divide work into coherent increments based on contracts, user-visible behavior, or risk—not a line-count target.
2. Implement the smallest useful increment while preserving project patterns and unrelated changes.
3. Run targeted checks after each meaningful increment; run broader checks at integration boundaries or when risk warrants them.
4. Stop and diagnose unexpected failures before continuing unrelated work.
5. Commit only when authorized by the user or repository policy.

## Verification checklist

- [ ] Each increment has a clear outcome and evidence.
- [ ] Validation depth matches changed surface and risk.
- [ ] No unsupported dependency, API, or scope expansion was introduced.
