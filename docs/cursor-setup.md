# Using agent-skills with Cursor

## Setup

> [!NOTE]
> Synchronizing rules to workspace folders (like `.cursor/rules/`) is **optional** and primarily used to customize rules on a per-project basis. The automated [install](../install) script handles installing and implementing your skills and default prompts globally for supported IDEs/CLIs (defined in `config.yaml`).

### Option 1: Automated Sync (Recommended)

You can use the automated [install](../install) script in this repository to automatically configure and sync rules into your project's `.cursor/rules/` folder as flat `.md` files.

1. Ensure your [config.yaml](../config.yaml) contains `./.cursor/rules/` in the `targets` list:
   ```yaml
   targets:
     - "./.cursor/rules/"
   ```
2. Run the installer:
   ```bash
   python3 ./install
   ```

The script will automatically copy the `SKILL.md` file of each skill to `.cursor/rules/<skill-name>.md` to conform to Cursor's flat rules requirement.

### Option 2: Manual Configuration

If you prefer to configure your workspace manually, configure these three parts:

1. **Global Prompt**: Paste the contents of `GLOBAL-PROMPT.md` into Cursor's global settings under **Cursor Settings > Features > Rules for AI**.
2. **Project AGENTS.md**: Copy the template `AGENTS.md` file from this repository to your project's root folder (`./AGENTS.md`) to define project-specific conventions.
3. **Skills**: Create a `.cursor/rules/` directory and copy the `SKILL.md` file of the skills you need directly to `.cursor/rules/<skill-name>.md` (e.g. `cp skills/test-driven-development/SKILL.md .cursor/rules/test-driven-development.md`). Alternatively, you can concatenate essential skill rules inside a `.cursorrules` file in your project root.

## Recommended Configuration

### Essential Skills (Always Load)

Add these to `.cursor/rules/`:

1. `test-driven-development.md` — TDD workflow and Prove-It pattern
2. `code-review-and-quality.md` — Five-axis review
3. `incremental-implementation.md` — Build in small verifiable slices

### Phase-Specific Skills (Load on Demand)

For phase-specific work, create additional rule files as needed:

- `spec-development.md` -> `spec-driven-development/SKILL.md`
- `frontend-ui.md` -> `frontend-ui-engineering/SKILL.md`
- `security.md` -> `security-and-hardening/SKILL.md`
- `performance.md` -> `performance-optimization/SKILL.md`

Add these to `.cursor/rules/` when working on relevant tasks, then remove when done to manage context limits.

## Usage Tips

1. **Don't load all skills at once** - Cursor has context limits. Load 2-3 essential skills as rules and add phase-specific skills as needed.
2. **Reference skills explicitly** - Tell Cursor "Follow the test-driven-development rules for this change" to ensure it reads the loaded rules.
3. **Use agents for review** - Copy `~/.config/agent-skills/agents/code-reviewer.md` content and tell Cursor to "review this diff using this code review framework."
4. **Load references on demand** - When working on performance, add `performance.md` to `.cursor/rules/` or paste the checklist content directly.
