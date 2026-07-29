---
name: planning-and-task-breakdown
description: Creates an ordered, verifiable plan for work with meaningful dependencies or parallelism. Use when scope spans components, migrations, risks, or independent work streams.
applies_when: Execution order, ownership, or verification is not obvious.
skip_when: A localized task can be safely completed as one coherent change.
risk: medium
requires: [repository-read]
fallback: State a brief inline sequence and verification plan.
outputs: [ordered-tasks, dependency-notes, verification-plan]
---

# Planning and Task Breakdown

1. Inspect the relevant system and identify contracts, dependencies, risks, and authority boundaries.
2. Order work by dependency and risk; use vertical slices where they improve feedback.
3. Describe each task with outcome, affected area, acceptance criteria, verification, and ownership when delegated.
4. Parallelize only independent work; isolate concurrent writers.
5. Add checkpoints for migrations, public contracts, external effects, and other high-risk decisions.

## Verification checklist

- [ ] Dependencies and ordering are explicit where they matter.
- [ ] Each task has proportionate acceptance evidence.
- [ ] Task size is justified by cohesion and risk, not arbitrary file or time limits.
