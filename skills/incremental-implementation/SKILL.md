---
name: incremental-implementation
description: Delivers changes incrementally. Use when implementing any feature or change that touches more than one file. Use when you're about to write a large amount of code at once, or when a task feels too big to land in one step.
---

# Incremental Implementation

## Core Workflow
1. **Slicing**: Divide the task into thin, compilable vertical slices that trace end-to-end through the stack (e.g., DB → API → UI) rather than horizontal layers.
2. **Implement**: Write code for the smallest complete, compilable piece of functionality. Keep modifications to ~100 lines before verifying.
3. **Verify**: Run build checks, typecheck, linter, and tests. Immediately fix any broken checks before moving forward.
4. **Commit**: Save progress with a clear, atomic commit.
5. **Iterate**: Build the next slice on top of the working foundation.

## Slicing Strategies
- **Vertical Slices (Preferred)**: Deliver functional slices (e.g., Create Task → List Tasks → Edit Task) end-to-end.
- **Contract-First**: Define interfaces/types first to unblock parallel frontend/backend streams.
- **Risk-First**: Solve high-risk, high-complexity dependencies first (e.g., WebSocket stability, critical algorithms).

## Implementation Rules
- **Simplicity First (Rule 0)**: Implement the naive, obviously-correct solution. Avoid building abstractions before the third distinct use case.
- **Scope Discipline (Rule 0.5)**: Touch only what the task requires. Never clean up adjacent code, refactor imports in untouched files, or add hypothetical out-of-scope features.
- **Compilable Checks**: The codebase must compile, build, and pass existing tests after every slice.
- **Safe Defaults**: Default to safe, opt-in, non-breaking configurations (e.g., disabled feature flags, private-by-default fields).
- **Rollback Friendly**: Keep additive and subtractive changes separate. Ensure migrations have clean rollbacks.

## Verification Checklist
- [ ] Each increment represents one logical, self-contained change.
- [ ] No uncommitted changes remain.
- [ ] Build succeeds with zero linter, compiler, or type warnings.
- [ ] Full test suite passes.
- [ ] Run build or check commands only on file modifications; avoid repeated identical runs.
