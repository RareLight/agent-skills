# Using agent-skills with Cursor

## Setup

### Option 1: Automated Sync (Recommended)

You can use the automated [install](file:///Users/anna/Documents/Coding/agent-skills/install) script in this repository to automatically configure and sync rules into your project's `.cursor/rules/` folder as flat `.md` files.

1. Ensure your [config.yaml](file:///Users/anna/Documents/Coding/agent-skills/config.yaml) contains `./.cursor/rules/` in the `targets` list:
   ```yaml
   targets:
     - "./.cursor/rules/"
   ```
2. Run the installer:
   ```bash
   python3 ./install
   ```

The script will automatically copy the `SKILL.md` file of each skill to `.cursor/rules/<skill-name>.md` to conform to Cursor's flat rules requirement.

### Option 2: Manual Copying (Rules Directory)

Cursor supports a `.cursor/rules/` directory for project-specific rules:

```bash
# Create the rules directory
mkdir -p .cursor/rules

# Copy skills you want as rules
cp /path/to/agent-skills/skills/test-driven-development/SKILL.md .cursor/rules/test-driven-development.md
cp /path/to/agent-skills/skills/code-review-and-quality/SKILL.md .cursor/rules/code-review-and-quality.md
cp /path/to/agent-skills/skills/incremental-implementation/SKILL.md .cursor/rules/incremental-implementation.md
```

Rules in this directory are automatically loaded into Cursor's context.

### Option 3: .cursorrules File

Create a `.cursorrules` file in your project root with the essential skills inlined:

```bash
# Generate a combined rules file
cat /path/to/agent-skills/skills/test-driven-development/SKILL.md > .cursorrules
echo "\n---\n" >> .cursorrules
cat /path/to/agent-skills/skills/code-review-and-quality/SKILL.md >> .cursorrules
```

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
