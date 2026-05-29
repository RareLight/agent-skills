# Using agent-skills with Windsurf

## Setup

### Option 1: Automated Sync (Recommended)

You can use the automated [install](file:///Users/anna/Documents/Coding/agent-skills/install) script in this repository to automatically configure and sync default prompts into your project's `.windsurfrules` file.

1. Ensure your [config.yaml](file:///Users/anna/Documents/Coding/agent-skills/config.yaml) contains `./.windsurfrules` under the `prompts.targets` section:
   ```yaml
   prompts:
     targets:
       - "./.windsurfrules"
   ```
2. Run the installer:
   ```bash
   python3 ./install
   ```

The script will automatically copy the `GLOBAL-PROMPT.md` rules containing the meta-skill precedence rules and global workflows to `./.windsurfrules`.

### Option 2: Manual Project Rules

Windsurf uses `.windsurfrules` for project-specific agent instructions:

```bash
# Create a combined rules file from your most important skills
cat /path/to/agent-skills/skills/test-driven-development/SKILL.md > .windsurfrules
echo "\n---\n" >> .windsurfrules
cat /path/to/agent-skills/skills/incremental-implementation/SKILL.md >> .windsurfrules
echo "\n---\n" >> .windsurfrules
cat /path/to/agent-skills/skills/code-review-and-quality/SKILL.md >> .windsurfrules
```

### Global Rules

For skills you want across all projects, add them to Windsurf's global rules:

1. Open Windsurf → Settings → AI → Global Rules
2. Paste the content of your most-used skills

## Recommended Configuration

Keep `.windsurfrules` focused on 2-3 essential skills to stay within context limits:

```
# .windsurfrules
# Essential agent-skills for this project

[Paste test-driven-development SKILL.md]

---

[Paste incremental-implementation SKILL.md]

---

[Paste code-review-and-quality SKILL.md]
```

## Usage Tips

1. **Be selective** — Windsurf's context is limited. Choose skills that address your biggest quality gaps.
2. **Reference in conversation** — Paste additional skill content into the chat when working on specific phases (e.g., paste `security-and-hardening` when building auth).
3. **Use references as checklists** — Paste `~/.config/agent-skills/references/security-checklist.md` and ask Windsurf to verify each item.
