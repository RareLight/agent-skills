---
name: git-workflow-and-versioning
description: Structures git workflow practices. Use when making any code change. Use when committing, branching, resolving conflicts, or when you need to organize work across multiple parallel streams.
---

# Git Workflow and Versioning

## Workflow & History Rules
- **Trunk-Based Development**: Keep `main` always deployable. Deliver work in short-lived feature branches (`feature/` or `fix/`) merged within 1-3 days.
- **Commit Early & Atomically**: Commit each thin, vertical slice as soon as it lints, builds, and passes tests. Never package unrelated features, refactors, or styling into a single commit.
- **Descriptive, Why-Focused Messages**: Format messages as `<type>: <short imperative description>` (e.g., `feat: validate registration email`). Use the commit body to explain *why* the change was implemented.
- **Refactoring Partitioning**: Submit refactoring commits independently of functional additions to make PRs cleanly reviewable.

## Branch & Worktree Strategy
- **Isolation**: Use `git worktree add` to run parallel agent tasks across isolated directories without branch-switching friction.
- **Clean Sweeps**: Delete branches immediately upon merge. Use feature flags rather than branching to hide partial implementations.

## Pre-Commit Hygiene
Run these steps before every commit:
1. `git diff --staged` - Review the precise changes.
2. Secret Scan - Scan stages for passwords, private keys, API keys, or tokens.
3. Quality checks - Verify that the project builds, lints, and passes tests.

## Verification Checklist
- [ ] Every commit represents exactly one logical change.
- [ ] Commit types follow standard conventions (`feat`, `fix`, `refactor`, `test`, `docs`).
- [ ] Target branch builds with zero compile or linter errors.
- [ ] All tests pass on the staged changeset.
- [ ] `.gitignore` accurately blocks `.env`, dependencies, build folders, and platform caches.
