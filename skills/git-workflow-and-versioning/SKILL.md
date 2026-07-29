---
name: git-workflow-and-versioning
description: Organizes repository history and collaboration safely. Use when branching, committing, resolving conflicts, or preparing a reviewable change.
applies_when: Version-control operations are requested or required by repository policy.
skip_when: The user has not authorized VCS changes and the project does not require them.
risk: medium
requires: [git]
fallback: Report the recommended VCS steps without performing them.
outputs: [vcs-status, commit-or-branch-plan]
---

# Git Workflow and Versioning

1. Inspect repository status and project branch policy before VCS changes.
2. Keep changes reviewable and logically coherent; use branches, worktrees, and commits according to project policy.
3. Review staged content, scan for secrets, and run proportionate checks before an authorized commit.
4. Never force-push protected history or bypass required verification without explicit authorization.

## Verification checklist

- [ ] VCS actions were authorized and consistent with repository policy.
- [ ] Staged changes and applicable checks were reviewed.
