---
name: using-agent-skills
description: Selects the smallest applicable engineering workflow. Use when starting a task, switching task type, or deciding whether a specialized skill is warranted.
applies_when: A task needs workflow selection or a relevant skill may improve safety, evidence, or quality.
skip_when: A higher-priority repository router already selects workflows.
risk: low
requires: [repository-instructions]
fallback: Apply the portable core and the maintenance fast path.
outputs: [selected-skills, verification-plan]
related_skills: []
---

# Using Agent Skills

## Route by conditions

1. Read repository instructions and classify the request: maintenance, behavior change, public or irreversible change, incident, review, release, or discovery.
2. Select only skills whose `applies_when` condition holds. Do not load a full lifecycle by default.
3. For a localized, reversible task with clear acceptance criteria, use the maintenance fast path in `docs/routing-model.md`.
4. Add discovery or specification for material ambiguity; planning for broad dependency or migration work; and domain skills for their explicit risk signals.
5. Select verification proportionate to the change. If a capability is unavailable, apply the skill fallback and state the gap.

## Decision guide

| Condition | Skill |
|---|---|
| Intent or outcome is materially unclear | `interview-me` or `idea-refine` |
| Significant, public, or irreversible change | `spec-driven-development` |
| Multi-component dependency or migration work | `planning-and-task-breakdown` |
| Implementation or behavior change | `incremental-implementation`, `test-driven-development` as appropriate |
| Browser, API, resilience, security, or performance risk | corresponding domain skill |
| Failure or unexpected behavior | `debugging-and-error-recovery` |
| Review, release, migration, CI, or documentation work | corresponding lifecycle skill |

## Verification checklist

- [ ] Selected skills match observed task conditions.
- [ ] Unneeded workflows were skipped with a reason when that is not obvious.
- [ ] Required capabilities and fallbacks are identified.
- [ ] The final handoff includes evidence and material verification gaps.
