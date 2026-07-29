#!/bin/bash
# Smoke-test installation in an isolated temporary directory.

set -euo pipefail

root_dir="$(cd "$(dirname "$0")/.." && pwd)"
tmp_dir="$(mktemp -d)"
trap 'rm -rf "$tmp_dir"' EXIT

python3 "$root_dir/install" \
  --resources-target "$tmp_dir/resources" \
  --targets "$tmp_dir/skills" \
  --prompt-targets "$tmp_dir/AGENTS.md"

test -f "$tmp_dir/skills/using-agent-skills/SKILL.md"
test -f "$tmp_dir/resources/adapters/generic.md"
test ! -e "$tmp_dir/resources/hooks"
cmp -s "$root_dir/GLOBAL-PROMPT.md" "$tmp_dir/AGENTS.md"

echo "isolated installer smoke test OK"
