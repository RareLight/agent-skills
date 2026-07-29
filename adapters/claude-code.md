# Claude Code Adapter

The hook scripts in `hooks/` are optional Claude-specific integrations. They are not part of the generic install path because they use Claude hook payloads and `CLAUDE_*` environment variables.

For a plugin installation, `hooks/hooks.json` locates the meta-skill relative to `CLAUDE_PLUGIN_ROOT`. For a central installation, set `AGENT_SKILLS_META_SKILL` to the absolute path of `using-agent-skills/SKILL.md` before enabling `session-start.sh`.

Use `python3 ./install --include-hooks` only when this adapter has been configured. Run `bash hooks/session-start-test.sh` after changing the hook or its path configuration.
