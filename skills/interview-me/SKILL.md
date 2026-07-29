---
name: interview-me
description: Clarifies materially underspecified product or engineering requests. Use when a safe assumption would materially change the outcome or the user explicitly requests an interview.
applies_when: Material intent, success criteria, or constraints are unknown.
skip_when: The request is conventional, reversible, and sufficiently scoped to proceed with stated assumptions.
risk: medium
requires: [interactive-user]
fallback: State assumptions, choose a reversible implementation, and identify the decision that needs confirmation.
outputs: [confirmed-intent, assumptions]
---

# Interview Me

1. State the decision that is blocked and the best current assumption.
2. Ask the smallest useful set of questions; ask one at a time only when each answer changes the next question.
3. Summarize outcome, user, success criteria, constraints, and out-of-scope items.
4. Obtain confirmation only for material decisions. Do not require a file or explicit approval for routine work.

## Verification checklist

- [ ] Questions were necessary to resolve a material decision.
- [ ] Assumptions and confirmed constraints are recorded in the handoff or applicable spec.
