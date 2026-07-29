# Skill Anatomy

This document describes the structure and format of agent-skills skill files. Use this as a guide when contributing new skills or understanding existing ones.

## File Location

Every skill lives in its own directory under `skills/`:

```
skills/
  skill-name/
    SKILL.md           # Required: The skill definition
    scripts/           # Optional: Runnable helpers used by the skill workflow
    supporting-file.md # Optional: Reference material loaded on demand
```

`SKILL.md` is the only required file. Add `scripts/` only when the skill actually ships runnable helpers, and omit the directory entirely for markdown-only skills.

## SKILL.md Format

### Frontmatter (Required)

```yaml
---
name: skill-name-with-hyphens
description: Guides agents through [task/workflow]. Use when [specific trigger conditions].
applies_when: A concise condition that activates the skill.
skip_when: A concise condition that makes the skill unnecessary.
risk: low | medium | high
requires: [capability-or-context]
fallback: Safe action when a required capability is unavailable.
outputs: [artifact-or-evidence]
---
```

**Rules:**
- `name`: Lowercase, hyphen-separated. Must match the directory name.
- `description`: Start with what the skill does in third person, then include one or more clear "Use when" trigger conditions. Include both *what* and *when*. Maximum 1024 characters.
- Routing fields make skill selection possible without loading the body. Keep them concise and capability-based; do not name a specific harness or absolute installation path.

**Why this matters:** Agents discover skills by reading descriptions. The description is injected into the system prompt, so it must tell the agent both what the skill provides and when to activate it. Do not summarize the workflow — if the description contains process steps, the agent may follow the summary instead of reading the full skill.

### Streamlined High-Density Pattern (Recommended)

To optimize context window usage and prevent token bloat, all skill files should be written in a high-density, action-oriented format. Avoid tutorial prose, large code examples, ASCII diagrams, and redundant tables.

```markdown
# Skill Title

## Core Workflow / Process
Numbered step-by-step instructions or phases of the workflow. Keep descriptions brief, imperative, and focused strictly on the procedural actions required.

## Implementation / Architectural Rules
A dense bulleted list of constraints, boundaries, and best practices. Combine what to avoid and mental checks into direct, clear, imperative rules (e.g., "Do not X; always Y").

## Verification Checklist
A concise, checkable exit-criteria list of testable conditions (e.g., tests pass, linter is clean). Every checkbox should be verifiable with evidence (test output, build result, screenshot, etc.).
```

## Section Purposes

### Core Process
The heart of the skill. This is the step-by-step workflow the agent follows. Must be specific and actionable — not vague advice.

**Good:** "Run `npm test` and verify all tests pass"
**Bad:** "Make sure the tests work"

### Implementation Rules
The constraints and boundaries governing execution. These consolidate rules of thumb, design system policies, and behavioral guardrails into direct imperative statements. They prevent the agent from rationalizing its way out of following the process.

### Verification
The exit criteria. A checklist the agent uses to confirm the skill's process is complete.

## Supporting Files

Create supporting files only when:
- Reference material exceeds 100 lines (keep the main SKILL.md focused)
- Code tools or scripts are needed
- Checklists are long enough to justify separate files

Keep patterns and principles inline when under 50 lines.

If a skill does not need runnable helpers, do not create an empty `scripts/` directory just to mirror other skills. Empty directories add noise without changing how the skill works.

## Writing Principles

1. **Process over knowledge.** Skills are workflows, not reference docs. Steps, not facts.
2. **Specific over general.** "Run `npm test`" beats "verify the tests".
3. **Evidence over assumption.** Every verification checkbox requires proof.
4. **Token-conscious.** Every section must justify its inclusion. If removing it wouldn't change agent behavior, remove it.
5. **Progressive disclosure.** Main SKILL.md is the entry point. Supporting files are loaded only when needed.
6. **High Density.** Prefer bulleted imperative instructions over narrative explanations, ASCII diagrams, or tutorial blocks.

## Naming Conventions

- Skill directories: `lowercase-hyphen-separated`
- Skill files: `SKILL.md` (always uppercase)
- Supporting files: `lowercase-hyphen-separated.md`
- References: stored in `references/` at the project root, not inside skill directories

## Cross-Skill References

Reference other skills by name:

```markdown
Follow the `test-driven-development` skill for writing tests.
If the build breaks, use the `debugging-and-error-recovery` skill.
```

Don't duplicate content between skills — reference and link instead.

## Required vs Recommended

Required:

- A `skills/<skill-name>/SKILL.md` file
- Valid YAML frontmatter with `name` and `description`
- A description that includes both what the skill does and when to use it
- `applies_when`, `skip_when`, `risk`, `requires`, `fallback`, and `outputs` metadata

Recommended:

- The streamlined, high-density section flow shown above
- Supporting files only when they keep the main `SKILL.md` focused
