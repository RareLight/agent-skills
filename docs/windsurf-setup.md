# Using agent-skills with Windsurf

## Setup

> [!NOTE]
> Synchronizing rules to workspace folders (like `.windsurfrules`) is **optional** and primarily used to customize rules on a per-project basis. The automated [install](../install) script handles installing and implementing your skills and default prompts globally for supported IDEs/CLIs (defined in `config.yaml`).

### Option 1: Automated Sync (Recommended)

You can use the automated [install](../install) script in this repository to automatically configure and sync default prompts into your project's `.windsurfrules` file.

1. Ensure your [config.yaml](../config.yaml) contains `./.windsurfrules` under the `prompts.targets` section:
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

### Option 2: Manual Configuration

If you prefer to configure your workspace manually, configure these three parts:

1. **Global Prompt**: Open Windsurf → Settings → AI → Global Rules and paste the contents of `GLOBAL-PROMPT.md`.
2. **Project AGENTS.md**: Copy the template `AGENTS.md` file from this repository to your project's root folder (`./AGENTS.md`) to define project-specific conventions.
3. **Skills**: Create a `.windsurfrules` file in your project root and copy the contents of the essential skills you want directly into it (e.g. `cat skills/test-driven-development/SKILL.md > .windsurfrules`).

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
