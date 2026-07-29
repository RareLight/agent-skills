#!/usr/bin/env python3
"""Ensure tracked Copilot artifacts exactly match their canonical sources."""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def files(root: Path) -> dict[Path, str]:
    if not root.is_dir():
        return {}
    return {
        path.relative_to(root): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in root.rglob("*")
        if path.is_file()
    }


source_skills = files(ROOT / "skills")
generated_skills = files(ROOT / ".github" / "skills")
errors = []
for path in sorted(source_skills.keys() | generated_skills.keys()):
    if source_skills.get(path) != generated_skills.get(path):
        errors.append(f".github/skills/{path} differs from skills/{path}")
source_prompt = ROOT / "GLOBAL-PROMPT.md"
generated_prompt = ROOT / ".github" / "copilot-instructions.md"
if not generated_prompt.is_file() or source_prompt.read_bytes() != generated_prompt.read_bytes():
    errors.append(".github/copilot-instructions.md differs from GLOBAL-PROMPT.md")

if errors:
    print("Generated artifact validation failed:", file=sys.stderr)
    print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
    raise SystemExit(1)
print(f"Validated {len(source_skills)} generated skill files and the Copilot prompt.")
