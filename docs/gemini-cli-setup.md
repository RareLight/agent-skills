# Using agent-skills with Gemini CLI and Google Antigravity

## Setup

Gemini CLI and Google Antigravity share the same underlying configuration paths (`~/.gemini/`) and default prompt files (`~/.gemini/GEMINI.md`).

### Option 1: Install as Skills (Recommended)

Gemini CLI and Google Antigravity have a native skills system that auto-discovers `SKILL.md` files in `.gemini/skills/` or `.agents/skills/` directories. Each skill activates on demand when it matches your task.

**Install from the repo:**

```bash
gemini skills install https://github.com/RareLight/agent-skills.git --path skills
```

**Or install from a local clone:**

```bash
git clone https://github.com/RareLight/agent-skills.git
gemini skills install ./agent-skills/skills/
```

**Install for a specific workspace only:**

```bash
gemini skills install ./agent-skills/skills/ --scope workspace
```

**Or sync automatically using the install script:**

You can use the included [install](../install) script to sync skills directly to your global Gemini/Antigravity and OpenCode config directories:

```bash
python3 ./install
```

Skills installed at workspace scope go into `.gemini/skills/` (or `.agents/skills/`). User-level skills go into `~/.gemini/skills/` (which both Gemini CLI and Google Antigravity read).

Once installed, verify with:

```
/skills list
```

Gemini CLI and Google Antigravity inject skill names and descriptions into the prompt automatically. When they recognize a matching task, they ask permission to activate the skill before loading its full instructions.

### Option 2: Manual Configuration

If you prefer to configure your workspace manually, configure these three parts:

1. **Global Prompt**: Place a copy of `GLOBAL-PROMPT.md` at `~/.gemini/GEMINI.md` to establish global default rules.
2. **Project AGENTS.md**: Copy the template `AGENTS.md` file from this repository to your project's root folder (`./AGENTS.md`) to define project-specific conventions.
3. **Skills**: Manually copy the `skills/` folder to `~/.gemini/skills/` (for user scope) or `.gemini/skills/` (for workspace scope). Alternatively, you can copy essential skills directly to your project's `GEMINI.md` file for persistent context (e.g. `cat skills/incremental-implementation/SKILL.md > GEMINI.md`).

Use `/memory show` to verify loaded context, and `/memory reload` to refresh after changes.

> **Skills vs GEMINI.md:** Skills are on-demand expertise that activate only when relevant, keeping your context window clean. GEMINI.md provides persistent context loaded for every prompt. Use skills for phase-specific workflows and GEMINI.md for always-on project conventions.

## Recommended Configuration

### Always-On (GEMINI.md)

Add these as persistent context for every session:

- `incremental-implementation` — Build in small verifiable slices
- `code-review-and-quality` — Five-axis review

### On-Demand (Skills)

Install these as skills so they activate only when relevant:

- `test-driven-development` — Activates when implementing logic or fixing bugs
- `spec-driven-development` — Activates when starting a new project or feature
- `frontend-ui-engineering` — Activates when building UI
- `security-and-hardening` — Activates during security reviews
- `performance-optimization` — Activates during performance work

## Advanced Configuration

### MCP Integration

Many skills in this pack leverage [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) tools to interact with the environment. For example:

- `browser-testing-with-devtools` uses the `chrome-devtools` MCP extension.
- `performance-optimization` can benefit from performance-related MCP tools.

To enable these, ensure you have the relevant MCP extensions installed in your Gemini CLI / Google Antigravity configuration (`~/.gemini/config.json`).

### Session Hooks

Gemini CLI and Google Antigravity support session lifecycle hooks. You can use these to automatically inject context or run validation scripts at the start of a session.

To replicate the `agent-skills` experience from other tools, you can configure a `SessionStart` hook that reminds you of the available skills or loads a meta-skill.

### Explicit Context Loading

You can explicitly load any skill into your current session by referencing it with the `@` symbol in your prompt:

```markdown
Use the @skills/test-driven-development/SKILL.md skill to implement this fix.
```

This is useful when you want to ensure a specific workflow is followed without waiting for auto-discovery.

## Slash Commands

The repo ships 7 slash commands under `.gemini/commands/` that map to the development lifecycle. Gemini CLI and Google Antigravity auto-discover them when you run from the project root.

| Command | What it does |
|---------|--------------|
| `/spec` | Write a structured spec before writing code |
| `/planning` | Break work into small, verifiable tasks |
| `/build` | Implement the next task incrementally |
| `/test` | Run TDD workflow — red, green, refactor |
| `/review` | Five-axis code review |
| `/code-simplify` | Reduce complexity without changing behavior |
| `/ship` | Pre-launch checklist via parallel persona fan-out |

Each command invokes the corresponding skill automatically — no manual skill loading required.

> **Note:** Use `/planning` instead of `/plan` — `/plan` conflicts with an internal command name in Gemini CLI / Google Antigravity.

## Usage Tips

1. **Prefer skills over GEMINI.md** — Skills activate on demand and keep your context window focused. Only put skills in GEMINI.md if you want them always loaded.
2. **Skill descriptions matter** — Each SKILL.md has a `description` field in its frontmatter that tells agents when to activate it. The descriptions in this repo are optimized for auto-discovery across all supported tools by clearly stating both *what* the skill does and *when* it should be triggered.
3. **Use agents for review** — Copy `~/.config/agent-skills/agents/code-reviewer.md` content when requesting structured code reviews.
4. **Combine with references** — Reference checklists from `~/.config/agent-skills/references/` when working on specific quality areas like testing or performance.
