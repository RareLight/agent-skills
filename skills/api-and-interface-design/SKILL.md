---
name: api-and-interface-design
description: Designs explicit, evolvable public and cross-module contracts. Use when creating or changing APIs, schemas, public types, or module boundaries.
applies_when: Consumers outside the immediate implementation depend on the contract.
skip_when: The interface is private, bounded, and unchanged.
risk: high
requires: [repository-read]
fallback: Document the contract and compatibility assumptions in the change handoff.
outputs: [contract, compatibility-notes, validation-plan]
related_skills: []
---

# API and Interface Design

1. Identify consumers, ownership, compatibility needs, and intentional observable behavior.
2. Define input, output, error, and evolution semantics before implementation when the interface is public or shared.
3. Validate untrusted boundary data; keep internal modules on established contracts.
4. Apply pagination, versioning, idempotency, and structured errors when scale, consumer needs, and project conventions warrant them.
5. Prefer additive, backward-compatible evolution unless a documented migration is approved.

## Verification checklist

- [ ] Consumers and compatibility impact are understood.
- [ ] Boundary validation and error semantics match the contract.
- [ ] Public or breaking changes include migration evidence.
