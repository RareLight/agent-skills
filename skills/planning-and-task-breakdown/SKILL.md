---
name: planning-and-task-breakdown
description: Breaks work into ordered tasks. Use when you have a spec or clear requirements and need to break work into implementable tasks. Use when a task feels too large to start, when you need to estimate scope, or when parallel work is possible.
---

# Planning and Task Breakdown

## Core Workflow
1. **Scoping**: Run in read-only mode first. Scan requirements, map component relationships, and identify risks. Do not implement code.
2. **Graph Dependencies**: Map the system bottom-up (Database → API Contracts → Business Logic → UI client → Layouts). Build foundations first.
3. **Slicing**: Slice tasks vertically (e.g. CRUD for Create → Read → Update) so each task results in a runnable, testable increment.
4. **Task Structure**: Define each task with a Title, Description, Acceptance Criteria, Verification Commands, and touched files.
5. **Checkpoints**: Order by risk and establish mandatory checkpoints (tests passing, clean builds, user review) every 2-3 tasks.

## Sizing Rules
- **Task Sizes**: Target Small (1-2 files) or Medium (3-5 files) tasks. 
- **Decompose**: Split tasks if they take >2 hours, touch distinct subsystems (e.g., auth and payments), or require more than 3 bullet points of acceptance criteria.

## Parallelization Boundaries
- **Independent**: Feature slices and unit tests can run in parallel.
- **Sequential**: DB migrations and shared core state changes must run sequentially.
- **Contract-First**: Define interfaces/types first to coordinate parallel streams.

## Verification Checklist
- [ ] Dependency hierarchy is mapped and foundation steps are scheduled first.
- [ ] Every task has specific, testable acceptance criteria.
- [ ] Every task includes a runnable verification command.
- [ ] No task spans more than 5 files.
- [ ] Checkpoints are scheduled between phases.
- [ ] Human has reviewed and approved the plan document.
