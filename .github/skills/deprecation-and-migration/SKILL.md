---
name: deprecation-and-migration
description: Safely retires or evolves active systems and contracts. Use when removing APIs, dependencies, features, data formats, or user-facing behavior.
applies_when: Active consumers, stored data, or compatibility are affected.
skip_when: The target is demonstrably unused and has no compatibility or retention obligations.
risk: high
requires: [usage-evidence]
fallback: Propose a migration plan and state missing consumer or traffic evidence.
outputs: [migration-plan, compatibility-notes, retirement-evidence]
related_skills: []
---

# Deprecation and Migration

1. Identify consumers, data retention obligations, compatibility windows, and ownership.
2. Choose removal, adapter, staged migration, or coexistence based on evidence and cost.
3. Provide a documented alternative and migration path for active consumers unless explicit authority permits a breaking retirement.
4. Monitor adoption where possible, then remove obsolete code, tests, dependencies, and documentation when exit criteria are met.

## Verification checklist

- [ ] Consumer and data impact are evidenced or explicitly unknown.
- [ ] Compatibility, rollback, and retirement criteria are documented.
