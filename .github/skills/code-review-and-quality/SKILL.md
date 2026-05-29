---
name: code-review-and-quality
description: Conducts multi-axis code review. Use before merging any change. Use when reviewing code written by yourself, another agent, or a human. Use when you need to assess code quality across multiple dimensions before it enters the main branch.
---

# Code Review and Quality

## The Five-Axis Review
Review every change prior to merge across five distinct axes:
1. **Correctness**: Adheres strictly to specifications, gracefully manages error paths, and includes comprehensive testing.
2. **Readability**: Simple, straightforward control flows without nested ternary chains, using descriptive, convention-aligned naming.
3. **Architecture**: Fits codebase patterns, maintains clean module boundaries, has zero circular imports, and avoids premature abstractions.
4. **Security**: Inputs are validated at boundaries, secrets are barred from commits and logging, and external payload sources are handled as untrusted.
5. **Performance**: Avoids database N+1 queries, applies missing indexes, paginates list collections, and avoids blocking synchronous calls.

## Sizing & Commits
- **Small Batches**: Target ~100 line changes. Keep PRs tightly focused on a single logical concern. Split refactoring steps from feature work into separate PRs.
- **Descriptive Commits**: The first line must use short, imperative verbs ("Fix task sorting"). The commit body must state *what* changed and *why*.
- **Dead Code Hygiene**: Identify and propose removal of unreachable functions, unused exports, and orphan imports.

## Review Communication
- **Severity Labels**: Tag comments explicitly with: `Critical` (blocks merge), `Important` (address or defer with reason), `Nit` (minor style/optional), or `FYI` (informational).
- **Data-Driven Feedback**: Ground design and performance critiques in facts, standards, or profiling data rather than personal style preferences.
- **Don't Soft-Pedal**: Clearly call out production-breaking logic or security bugs without sycophancy or softening concerns.

## Verification Checklist
- [ ] All flagged `Critical` issues are resolved.
- [ ] Regression tests are included with all bug fixes.
- [ ] Code builds, lints, and passes tests cleanly.
- [ ] Dead code has been cleaned up.
