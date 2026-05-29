---
name: spec-driven-development
description: Creates specs before coding. Use when starting a new project, feature, or significant change and no specification exists yet. Use when requirements are unclear, ambiguous, or only exist as a vague idea.
---

# Spec-Driven Development

## Objective & Posture
- **Shared Source of Truth**: Establish a structured, version-controlled specification defining what is being built, why, and how we verify completion before writing functional code.
- **Assumption Exposure**: State all technical and architectural assumptions (stack, browsers, database) before drafting the spec. Never fill in gaps silently.

## The 4-Phase Gated Workflow
```
SPECIFY (Human Approval) ──→ PLAN (Human Approval) ──→ TASKS (Human Approval) ──→ IMPLEMENT
```
*Do not proceed to the next phase until the current phase is fully reviewed and approved.*

### Phase 1: Specify
Write a spec document saved to the repository covering:
- **Objective**: Use cases, target audience, and reframed testable success criteria.
- **Commands**: Explicit build, test, lint, and typecheck commands.
- **Project Structure**: Folder structure and colocated test locations.
- **Code Style**: Practical code snippet illustrating pattern design.
- **Testing**: Framework, coverage, and test tier mapping.
- **Boundaries**: Strictly outline Always, Ask First, and Never rules.

### Phase 2: Plan
Map dependencies, identify implementation sequence (foundations first), evaluate technical risks, and define checkpoints.

### Phase 3: Tasks
Decompose into Small/Medium vertical slices containing acceptance criteria, verification commands, and file targets.

### Phase 4: Implement
Execute task-by-task using `incremental-implementation` and `test-driven-development`.

## Verification Checklist
- [ ] Specification document covers all six core areas.
- [ ] Success criteria are translated into specific, measurable thresholds (e.g., LCP < 2.5s).
- [ ] Human reviewed and approved the spec file.
- [ ] Spec is committed to version control prior to implementation.
