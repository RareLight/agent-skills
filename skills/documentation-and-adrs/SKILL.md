---
name: documentation-and-adrs
description: Records durable decisions and user-facing operational knowledge. Use when a decision, public contract, setup path, or trade-off will matter to future maintainers.
applies_when: Documentation reduces meaningful future ambiguity.
skip_when: The change is self-evident and does not alter a durable contract or decision.
risk: low
requires: [writable-workspace]
fallback: Include rationale and links in the final handoff.
outputs: [documentation-or-adr]
related_skills: []
---

# Documentation and ADRs

1. Document why, constraints, alternatives, and consequences—not line-by-line code narration.
2. Create an ADR for decisions that are expensive to reverse when the repository uses ADRs; supersede rather than silently rewrite accepted historical decisions.
3. Update setup, command, API, and operational documentation when the change makes existing guidance inaccurate.
4. Keep TODOs only when they track intentionally deferred work with an owner or issue reference.

## Verification checklist

- [ ] Documentation matches the implemented behavior.
- [ ] Durable decisions include rationale and consequences.
