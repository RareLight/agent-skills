#!/usr/bin/env python3
"""Regenerate tracked Copilot artifacts from canonical sources."""

from __future__ import annotations

import os
import shutil
import tempfile
import uuid
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def replace_tree(source: Path, destination: Path) -> None:
    staging = Path(tempfile.mkdtemp(prefix=".agent-skills-stage-", dir=destination.parent)) / destination.name
    backup = destination.with_name(f"{destination.name}.agent-skills-backup-{uuid.uuid4().hex}")
    shutil.copytree(source, staging)
    if destination.exists():
        os.replace(destination, backup)
    try:
        os.replace(staging, destination)
    except Exception:
        if backup.exists() and not destination.exists():
            os.replace(backup, destination)
        raise
    finally:
        shutil.rmtree(staging.parent, ignore_errors=True)
    if backup.exists():
        shutil.rmtree(backup)


def replace_file(source: Path, destination: Path) -> None:
    fd, staged_name = tempfile.mkstemp(prefix=".agent-skills-stage-", dir=destination.parent)
    os.close(fd)
    staged = Path(staged_name)
    backup = destination.with_name(f"{destination.name}.agent-skills-backup-{uuid.uuid4().hex}")
    shutil.copy2(source, staged)
    if destination.exists():
        os.replace(destination, backup)
    try:
        os.replace(staged, destination)
    except Exception:
        if backup.exists() and not destination.exists():
            os.replace(backup, destination)
        raise
    finally:
        staged.unlink(missing_ok=True)
    if backup.exists():
        backup.unlink()


github = ROOT / ".github"
replace_tree(ROOT / "skills", github / "skills")
replace_file(ROOT / "GLOBAL-PROMPT.md", github / "copilot-instructions.md")
print("Synchronized tracked Copilot artifacts.")
