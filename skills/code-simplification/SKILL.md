---
name: code-simplification
description: Simplifies code for clarity. Use when refactoring code for clarity without changing behavior. Use when code works but is harder to read, maintain, or extend than it should be. Use when reviewing code that has accumulated unnecessary complexity.
---

# Code Simplification

## Core Simplification Principles
- **Preserve Behavior Exactly**: Never modify actual inputs, outputs, exceptions, or side-effect ordering when refactoring.
- **Readability over Cleverness**: Explicit, clear logic is superior to highly compact, clever tricks (e.g. avoid complex nested ternary chains).
- **Match Conventions**: Ensure refactored code aligns perfectly with existing project patterns and styling.
- **Refactoring Scope**: Simplify code incrementally and test after every change. Limit simplification strictly to the scope of what is already changing.

## Refactoring Targets
- **Nesting & Length**: Replace deep nested branches (3+ levels) with early returns or guard clauses. Break up massive functions (50+ lines).
- **Ternaries & Flags**: Replace dense ternary chains with readable switch statements or lookup mapping configurations.
- **Redundancies**: Remove dead code, redundant type casting, unused packages, and wrapper abstractions that add zero functional value.
- **Speculative Abstractions**: Eliminate speculative code, unused parameter flags, and complex design patterns built for future "what-if" requirements.
- **Protected Blocks**: The `simplify-ignore` hook (`hooks/SIMPLIFY-IGNORE.md`) prevents the model from simplifying annotated code blocks — use for performance-critical or intentionally-unrolled sections.

## Verification Checklist
- [ ] Refactored code preserves the exact input-output behavior.
- [ ] All existing and new tests pass cleanly.
- [ ] Refactoring commits are submitted independently of feature logic.
- [ ] Simplified code follows the defined formatting, naming, and style conventions of the project.
