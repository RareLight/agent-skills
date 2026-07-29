#!/usr/bin/env python3
"""Validate machine-readable routing fixtures against the routing manifest."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
known_skills = {path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")}
manifest = json.loads((ROOT / "routing-manifest.json").read_text(encoding="utf-8"))
fixtures = json.loads((ROOT / "fixtures" / "routing.json").read_text(encoding="utf-8"))
errors: list[str] = []
seen_ids: set[str] = set()

for fixture in fixtures:
    label = fixture.get("id", "<missing id>")
    if not isinstance(label, str) or not label or label in seen_ids:
        errors.append(f"fixture has missing or duplicate id: {label!r}")
        continue
    seen_ids.add(label)
    task_type = fixture.get("task_type")
    if task_type not in manifest:
        errors.append(f"{label}: unknown task_type {task_type!r}")
        continue
    expected = fixture.get("expected_skills")
    evidence = fixture.get("minimum_evidence")
    if not isinstance(expected, list) or not all(isinstance(item, str) for item in expected):
        errors.append(f"{label}: expected_skills must be a list of skill names")
        continue
    if not isinstance(evidence, str) or not evidence.strip():
        errors.append(f"{label}: minimum_evidence must be non-empty")
    unknown = sorted(set(expected) - known_skills)
    if unknown:
        errors.append(f"{label}: unknown skills: {', '.join(unknown)}")
    required = set(manifest[task_type]["required_skills"])
    allowed = required | set(manifest[task_type]["allowed_skills"])
    missing = sorted(required - set(expected))
    disallowed = sorted(set(expected) - allowed)
    if missing:
        errors.append(f"{label}: missing required skills: {', '.join(missing)}")
    if disallowed:
        errors.append(f"{label}: disallowed skills: {', '.join(disallowed)}")

if not fixtures:
    errors.append("no routing fixtures found")
if errors:
    print("Routing fixture validation failed:", file=sys.stderr)
    print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
    raise SystemExit(1)
print(f"Validated {len(fixtures)} routing fixtures across {len(manifest)} task types.")
