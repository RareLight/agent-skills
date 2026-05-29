# Using agent-skills with GitHub Copilot

## Setup

> [!NOTE]
> Synchronizing rules to workspace folders (like `.github/skills/` or `.github/copilot-instructions.md`) is **optional** and primarily used to customize skills on a per-project basis. The automated [install](../install) script handles installing and implementing your skills and default prompts globally for supported IDEs/CLIs (defined in `config.yaml`).

### Option 1: Automated Sync (Recommended)

You can use the automated [install](../install) script in this repository to automatically configure and sync both the skills folder and the custom instructions file for GitHub Copilot.

1. Ensure your [config.yaml](../config.yaml) contains the Copilot targets under `targets` and `prompts.targets`:
   ```yaml
   targets:
     - "./.github/skills/"
   prompts:
     targets:
       - "./.github/copilot-instructions.md"
   ```
2. Run the installer:
   ```bash
   python3 ./install
   ```

The script will automatically copy all skills to `./.github/skills/` and write the global prompt instructions (including precedence rules) to `./.github/copilot-instructions.md`.

### Option 2: Manual Configuration

If you prefer to configure your workspace manually, configure these three parts:

1. **Global Prompt**: In VS Code, go to **Settings → GitHub Copilot → Custom Instructions** and paste the contents of `GLOBAL-PROMPT.md` (or save it directly as `.github/copilot-instructions.md` in your project root to set project-level instructions).
2. **Project AGENTS.md**: Copy the template `AGENTS.md` file from this repository to your project's root folder (`./AGENTS.md`) to define project-specific conventions.
3. **Skills**: Create a `.github/skills/` directory in your workspace and copy individual skills (e.g. `skills/test-driven-development/SKILL.md` to `.github/skills/test-driven-development/SKILL.md`). For specialized agent personas (`*.agent.md`), create a `.github/agents/` directory and copy agent files:
   ```bash
   mkdir -p .github/agents
   cp ~/.config/agent-skills/agents/code-reviewer.md .github/agents/code-reviewer.agent.md
   cp ~/.config/agent-skills/agents/test-engineer.md .github/agents/test-engineer.agent.md
   cp ~/.config/agent-skills/agents/security-auditor.md .github/agents/security-auditor.agent.md
   ```

## Recommended Configuration

### .github/copilot-instructions.md

GitHub Copilot supports project-level instructions via `.github/copilot-instructions.md`.

```markdown
# Project Coding Standards

## Testing
- Write tests before code (TDD)
- For bugs: write a failing test first, then fix (Prove-It pattern)
- Test hierarchy: unit > integration > e2e (use the lowest level that captures the behavior)
- Run `npm test` after every change

## Code Quality
- Review across five axes: correctness, readability, architecture, security, performance
- Every PR must pass: lint, type check, tests, build
- No secrets in code or version control

## Implementation
- Build in small, verifiable increments
- Each increment: implement → test → verify → commit
- Never mix formatting changes with behavior changes

## Boundaries
- Always: Run tests before commits, validate user input
- Ask first: Database schema changes, new dependencies
- Never: Commit secrets, remove failing tests, skip verification
```

### Specialized Agents

Use the agents for targeted review workflows in Copilot Chat.

## Usage Tips

1. **Keep instructions concise** — Copilot instructions work best when focused. Summarize the key rules rather than including full skill files.
2. **Use agents for review** — The code-reviewer, test-engineer, and security-auditor agents are designed for Copilot's agent model.
3. **Reference in chat** — When working on a specific phase, paste the relevant skill content into Copilot Chat for context.
4. **Combine with PR reviews** — Set up Copilot to review PRs using the code-reviewer agent persona.
