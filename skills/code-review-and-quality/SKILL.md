---
name: code-review-and-quality
description: Reviews a scoped change for correctness, maintainability, security, performance, and verification evidence. Use before merge or when a user requests a code review.
applies_when: A diff, change, or implementation needs an independent quality assessment.
skip_when: No code or configuration change is in scope.
risk: medium
requires: [repository-read]
fallback: Review available artifacts and state what could not be inspected or executed.
outputs: [findings, verdict, verification-gaps]
related_skills: []
---

# Code Review and Quality

1. Read the task, relevant contract, diff, and tests before judging implementation.
2. Assess correctness, readability, architecture, security, performance, and change-specific compatibility risks.
3. Report only evidence-backed findings with severity, location, impact, and an actionable recommendation.
4. Separate blocking defects from optional improvements; “no findings” is a valid result.
5. Do not impose arbitrary change-size, commit-style, or cleanup requirements absent project policy.

## Verification checklist

- [ ] Findings are scoped to the reviewed change and supported by evidence.
- [ ] Verification evidence and gaps are reported.
- [ ] Approval is withheld only for material unresolved risk.
