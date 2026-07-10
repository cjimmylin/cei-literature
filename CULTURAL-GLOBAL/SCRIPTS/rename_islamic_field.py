#!/usr/bin/env python3
"""
Batch rename nw_islamic_jurisprudence → nw_islamic_ethics in paper YAML frontmatter.

Uses safe regex pattern (no parse/rebuild round-trip).

Usage:
    python rename_islamic_field.py --dry-run   # preview changes
    python rename_islamic_field.py              # apply changes
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

PAPERS_DIR = Path(__file__).parent.parent.parent / "papers"


def rename_field(dry_run: bool = False) -> int:
    """Rename nw_islamic_jurisprudence → nw_islamic_ethics across all paper files."""
    modified = 0
    errors = []

    for md_file in sorted(PAPERS_DIR.iterdir()):
        if not md_file.suffix == ".md":
            continue

        try:
            content = md_file.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            errors.append((md_file.name, str(e)))
            continue

        new_content, count = re.subn(
            r"^nw_islamic_jurisprudence:(.*)$",
            r"nw_islamic_ethics:\1",
            content,
            count=1,
            flags=re.MULTILINE,
        )

        if count > 0:
            modified += 1
            if dry_run:
                print(f"  [DRY-RUN] Would rename in: {md_file.name}")
            else:
                md_file.write_text(new_content, encoding="utf-8")
                print(f"  Renamed in: {md_file.name}")

    print(f"\n{'[DRY-RUN] ' if dry_run else ''}Total files modified: {modified}")
    if errors:
        print(f"Errors: {len(errors)}")
        for name, err in errors:
            print(f"  {name}: {err}")

    return modified


if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv
    rename_field(dry_run=dry_run)
