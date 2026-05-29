# OpenCode Setup

This guide explains how to use Agent Skills with OpenCode's agent-driven workflow — automatic skill selection, lifecycle-driven workflows, and strict process enforcement.

## Overview

OpenCode uses a skill-driven architecture:

- A strong system prompt (`AGENTS.md`)
- The built-in `skill` tool
- Consistent skill discovery from the `skills/` directory

This creates an **agent-driven workflow** where skills are selected and executed automatically based on intent, without requiring manual commands.

---

## Installation

### Option 1: Automated Sync (Recommended)

You can use the automated [install](../install) script in this repository to automatically configure and sync all skills globally to your OpenCode configuration directory (`~/.config/opencode/skills/`) and write the default prompt to `~/.config/opencode/AGENTS.md`.

1. Ensure your [config.yaml](../config.yaml) contains the OpenCode targets under `targets` and `prompts.targets`:
   ```yaml
   targets:
     - "~/.config/opencode/skills/"
   prompts:
     targets:
       - "~/.config/opencode/AGENTS.md"
   ```
2. Run the installer:
   ```bash
   python3 ./install
   ```

### Option 2: Workspace Integration (Optional / Manual)

If you only want skills active for a single project workspace or want to customize project-specific skills, manually configure these three parts:

1. **Global Prompt**: Place a copy of `GLOBAL-PROMPT.md` at `~/.config/opencode/AGENTS.md` to establish global default rules.
2. **Project AGENTS.md**: Copy the template `AGENTS.md` file from this repository to your project's root folder (`./AGENTS.md`) to define project-specific conventions.
3. **Skills**: Copy the `./skills/` directory from this repository directly into your project's root folder (`./skills/`) to make all workflow skills available locally.

---

## How It Works

### 1. Skill Discovery

All skills live in:

```
skills/<skill-name>/SKILL.md
```

OpenCode agents are instructed (via `AGENTS.md`) to:

- Detect when a skill applies
- Invoke the `skill` tool
- Follow the skill exactly

### 2. Automatic Skill Invocation

The agent evaluates every request and maps it to the appropriate skill.

Examples:

- "build a feature" → `incremental-implementation` + `test-driven-development`
- "design a system" → `spec-driven-development`
- "fix a bug" → `debugging-and-error-recovery`
- "review this code" → `code-review-and-quality`

The user does **not** need to explicitly request skills.

### 3. Lifecycle Mapping

The development lifecycle is encoded implicitly:

- DEFINE → `spec-driven-development`
- PLAN → `planning-and-task-breakdown`
- BUILD → `incremental-implementation` + `test-driven-development`
- VERIFY → `debugging-and-error-recovery`
- REVIEW → `code-review-and-quality`
- SHIP → `shipping-and-launch`

---

## Usage Examples

### Feature Development

User:
```
Add authentication to this app
```

Agent behavior:
- Detects feature work
- Invokes `spec-driven-development`
- Produces a spec before writing code
- Moves to planning and implementation skills

### Bug Fix

User:
```
This endpoint is returning 500 errors
```

Agent behavior:
- Invokes `debugging-and-error-recovery`
- Reproduces → localizes → fixes → adds guards

### Code Review

User:
```
Review this PR
```

Agent behavior:
- Invokes `code-review-and-quality`
- Applies structured review (correctness, design, readability, etc.)

---

## Agent Expectations (Critical)

For OpenCode to work correctly, the agent must follow these rules:

- Always check if a skill applies before acting
- If a skill applies, it MUST be used
- Never skip required workflows (spec, plan, test, etc.)
- Do not jump directly to implementation

These rules are enforced via `AGENTS.md`.

---

## Recommended Workflow

Just use natural language:

- "Design a feature"
- "Plan this change"
- "Implement this"
- "Fix this bug"
- "Review this"

The agent will automatically select and execute the correct skills.

---

## Summary

OpenCode integration works by combining:

- Structured skills (this repo)
- Strong agent rules (`AGENTS.md`)
- Automatic skill invocation via reasoning

This results in a **fully agent-driven, production-grade engineering workflow** without requiring plugins or manual commands.
