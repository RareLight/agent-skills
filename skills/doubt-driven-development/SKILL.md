---
name: doubt-driven-development
description: Performs an adversarial check of high-impact engineering assumptions. Use for unfamiliar, concurrent, irreversible, security-sensitive, or high-blast-radius decisions.
applies_when: The cost of an unnoticed assumption exceeds the cost of an independent review.
skip_when: The decision is conventional, reversible, and already well covered by tests or local contracts.
risk: high
requires: [independent-reviewer-optional]
fallback: Perform a structured self-review against the relevant contract and risk list.
outputs: [claim, review-findings, disposition]
---

# Doubt-Driven Development

1. State the claim, contract, evidence, and blast radius.
2. Obtain an independent review when a suitable reviewer or model is available; provide the artifact and contract, not persuasive reasoning.
3. Classify findings as contract issue, actionable defect, accepted trade-off, or noise.
4. Stop after the review no longer produces material findings; do not require a fixed number of cycles or vendor-specific escalation.

## Verification checklist

- [ ] The decision and risk are explicit.
- [ ] Findings were checked against the artifact rather than accepted blindly.
- [ ] Remaining trade-offs are documented.
