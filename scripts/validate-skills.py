#!/usr/bin/env python3
"""Validate the portable skill schema and declared relationships."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_SCALARS = {"name", "description", "applies_when", "skip_when", "risk", "fallback"}
REQUIRED_LISTS = {"requires", "outputs", "related_skills"}
VALID_RISKS = {"low", "medium", "high"}
NAME = re.compile(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*\Z")
KEY_VALUE = re.compile(r"([a-z_]+):[ \t]+(.+)\Z")
LIST = re.compile(r"\[([^]]*)\]\Z")
FORBIDDEN_PORTABLE = re.compile(
    r"~/(?:\.config|\.gemini)|chrome-devtools|\b(?:OpenCode|Gemini|Codex)\b|\bMCP\b",
    re.IGNORECASE,
)


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", text, re.DOTALL)
    if not match:
        raise ValueError("missing YAML frontmatter")
    values: dict[str, str] = {}
    for number, line in enumerate(match.group(1).splitlines(), start=2):
        parsed = KEY_VALUE.fullmatch(line)
        if not parsed:
            raise ValueError(f"invalid frontmatter line {number}: {line!r}")
        key, value = parsed.groups()
        if key in values:
            raise ValueError(f"duplicate frontmatter key {key!r}")
        values[key] = value
    return values


def parse_list(value: str, field: str) -> list[str]:
    match = LIST.fullmatch(value)
    if not match:
        raise ValueError(f"{field} must use inline list syntax")
    items = [] if not match.group(1).strip() else [item.strip() for item in match.group(1).split(",")]
    if any(not item or not NAME.fullmatch(item) for item in items):
        raise ValueError(f"{field} contains an invalid identifier")
    return items


def validate_skill(path: Path, known_names: set[str], display_root: Path) -> list[str]:
    errors: list[str] = []
    label = path.relative_to(display_root)
    try:
        text = path.read_text(encoding="utf-8")
        data = parse_frontmatter(text)
    except (OSError, UnicodeError, ValueError) as error:
        return [f"{label}: {error}"]

    missing = (REQUIRED_SCALARS | REQUIRED_LISTS) - data.keys()
    if missing:
        errors.append(f"{label}: missing metadata: {', '.join(sorted(missing))}")
    unknown = data.keys() - (REQUIRED_SCALARS | REQUIRED_LISTS)
    if unknown:
        errors.append(f"{label}: unknown metadata: {', '.join(sorted(unknown))}")
    if data.get("name") != path.parent.name or not NAME.fullmatch(data.get("name", "")):
        errors.append(f"{label}: name must match its kebab-case directory")
    for field in REQUIRED_SCALARS - {"name", "risk"}:
        if not data.get(field, "").strip():
            errors.append(f"{label}: {field} must be non-empty")
    if data.get("risk") not in VALID_RISKS:
        errors.append(f"{label}: risk must be one of {', '.join(sorted(VALID_RISKS))}")
    for field in REQUIRED_LISTS:
        try:
            items = parse_list(data.get(field, ""), field)
        except ValueError as error:
            errors.append(f"{label}: {error}")
            continue
        if field != "related_skills" and not items:
            errors.append(f"{label}: {field} must not be empty")
        if field == "related_skills":
            unknown_skills = sorted(set(items) - known_names)
            if unknown_skills:
                errors.append(f"{label}: unknown related skills: {', '.join(unknown_skills)}")
    if FORBIDDEN_PORTABLE.search(text):
        errors.append(f"{label}: portable skill contains a harness-specific token")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skills-dir", type=Path, default=ROOT / "skills")
    args = parser.parse_args()
    skills_dir = args.skills_dir.resolve()
    skill_files = sorted(skills_dir.glob("*/SKILL.md")) if skills_dir.is_dir() else []
    if not skill_files:
        print(f"Skill validation failed:\n- no skills found in {skills_dir}", file=sys.stderr)
        return 1
    known_names = {path.parent.name for path in skill_files}
    errors = [error for path in skill_files for error in validate_skill(path, known_names, skills_dir.parent)]
    if errors:
        print("Skill validation failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"Validated {len(skill_files)} portable skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
