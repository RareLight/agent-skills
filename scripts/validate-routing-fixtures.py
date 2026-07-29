#!/usr/bin/env python3
"""Check that documented routing fixtures reference installed skills."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
known = {path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")}
fixture = (ROOT / "docs" / "routing-fixtures.md").read_text(encoding="utf-8")
references = set(re.findall(r"`([a-z][a-z0-9-]+)`", fixture))
missing = sorted(references - known)
if missing:
    print(f"Unknown fixture skill references: {', '.join(missing)}", file=sys.stderr)
    raise SystemExit(1)
print(f"Validated {len(references)} fixture skill references.")
