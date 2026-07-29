#!/usr/bin/env python3
"""Validate portable skill metadata and prevent harness-specific leakage."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
REQUIRED = {"name", "description", "applies_when", "skip_when", "risk", "requires", "fallback", "outputs"}
FORBIDDEN_PORTABLE = ("~/.config", "chrome-devtools", "OpenCode", "Gemini", "Codex", " MCP")


def frontmatter(text: str) -> dict[str, str] | None:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return None
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip()
    return values


def main() -> int:
    errors: list[str] = []
    skill_files = sorted(SKILLS.glob("*/SKILL.md"))
    known_names = {path.parent.name for path in skill_files}

    for path in skill_files:
        text = path.read_text(encoding="utf-8")
        data = frontmatter(text)
        if data is None:
            errors.append(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
            continue
        missing = REQUIRED - data.keys()
        if missing:
            errors.append(f"{path.relative_to(ROOT)}: missing metadata: {', '.join(sorted(missing))}")
        if data.get("name") != path.parent.name:
            errors.append(f"{path.relative_to(ROOT)}: name does not match directory")
        for token in FORBIDDEN_PORTABLE:
            if token in text:
                errors.append(f"{path.relative_to(ROOT)}: portable skill contains harness token {token!r}")
        for reference in re.findall(r"`([a-z][a-z0-9-]+)`", text):
            if reference.endswith("-development") or reference in known_names:
                if reference not in known_names:
                    errors.append(f"{path.relative_to(ROOT)}: unknown skill reference {reference!r}")

    if errors:
        print("Skill validation failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"Validated {len(skill_files)} portable skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
