---
name: spec-driven-development
description: Defines testable requirements for significant changes. Use when a change is public, cross-cutting, irreversible, high-risk, or materially ambiguous.
applies_when: Requirements or compatibility decisions need a durable shared record.
skip_when: A localized change has clear acceptance criteria and no material risk signal.
risk: high
requires: [writable-workspace]
fallback: Record concise acceptance criteria and assumptions in the task handoff.
outputs: [specification, acceptance-criteria, risk-decisions]
related_skills: []
---

# Spec-Driven Development

1. Classify the change and state why a durable specification is needed.
2. Record objective, users, success criteria, constraints, compatibility/security/privacy implications, alternatives, and verification strategy.
3. Use a lightweight specification for bounded changes; create a versioned document for public, multi-team, irreversible, or architectural changes.
4. Seek approval when project policy requires it or before committing to material external or irreversible decisions.
5. Hand implementation to planning only when dependencies or scope warrant it.

## Verification checklist

- [ ] Success criteria are measurable for the task's risk.
- [ ] Material assumptions, authority boundaries, and rollback/compatibility needs are explicit.
- [ ] The chosen document depth matches the change.
