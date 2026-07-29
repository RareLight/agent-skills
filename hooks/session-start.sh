#!/bin/bash
# Claude Code session-start hook. Use from a plugin layout or set
# AGENT_SKILLS_META_SKILL to the installed using-agent-skills/SKILL.md path.

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
META_SKILL="${AGENT_SKILLS_META_SKILL:-$(dirname "$SCRIPT_DIR")/skills/using-agent-skills/SKILL.md}"

if ! command -v jq >/dev/null 2>&1; then
  echo '{"priority": "INFO", "message": "agent-skills: jq is required for the optional Claude session-start hook. Skills remain available individually."}'
  exit 0
fi

if [ -f "$META_SKILL" ]; then
  CONTENT=$(cat "$META_SKILL")
  # Use jq to properly escape and construct valid JSON
  jq -cn \
    --arg message "agent-skills loaded. Select the smallest applicable workflow using skill metadata and the routing model.

$CONTENT" \
    '{priority: "IMPORTANT", message: $message}'
else
  echo '{"priority": "INFO", "message": "agent-skills: meta-skill not found. Set AGENT_SKILLS_META_SKILL or install from a plugin layout."}'
fi
