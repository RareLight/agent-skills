# Project instructions

Applies to this repository. These instructions override the IDE-global defaults found in `~/.config/opencode/AGENTS.md` / `~/.gemini/GEMINI.md` when they conflict.

> [!IMPORTANT]
> **Instructions for Future AI Coding Agents**:
> This file is a living document and a starting point for project development.
> - **Update, Don't Overwrite**: When initializing or discovering project details (e.g., via `/init` or context exploration), append/integrate your discoveries into this file. **NEVER** overwrite, replace, or delete existing contents.
> - **Evolve Project Context**: Update the project structure, stack descriptions, conventions, commands, and boundaries as the codebase evolves, but always preserve the core skill rules, workflows, and overrides.

## Project

A collection of production-grade engineering skills for AI coding agents.

## Project Structure

```
skills/       → Core skills (SKILL.md per directory)
agents/       → Reusable agent personas
hooks/        → Session lifecycle hooks
references/   → Supplementary checklists
docs/         → Skill anatomy and setup guides
```

## Skills by Phase

- **Define:** interview-me, idea-refine, spec-driven-development
- **Plan:** planning-and-task-breakdown
- **Build:** incremental-implementation, test-driven-development, context-engineering, source-driven-development, doubt-driven-development, frontend-ui-engineering, api-and-interface-design
- **Verify:** browser-testing-with-devtools, debugging-and-error-recovery
- **Review:** code-review-and-quality, code-simplification, security-and-hardening, performance-optimization
- **Ship:** git-workflow-and-versioning, ci-cd-and-automation, deprecation-and-migration, documentation-and-adrs, shipping-and-launch

## Conventions

- Every skill lives in `skills/<name>/SKILL.md` with YAML frontmatter (`name`, `description`)
- Description: what the skill does (third person) + "Use when" trigger conditions
- Skills follow the streamlined high-density pattern in `docs/skill-anatomy.md`
- References stored in `references/`, not inside skill directories
- Supporting files created only when content exceeds 100 lines
- All skills must be language-agnostic, logically consistent, and optimized for minimal context usage

## Commands

- Validate: Verify all SKILL.md files have valid YAML frontmatter with name and description

## Boundaries

- Always: Follow the streamlined high-density skill-anatomy format
- Never: Add skills that are vague advice instead of actionable processes
- Never: Duplicate content between skills — reference other skills by name instead
