#!/usr/bin/env python3
"""
Add normative_ethics_benchmark field to papers classified in v2 deep-read.

Reads decisions from logs/normative_v2_decisions.json
and safely appends the field to paper YAML frontmatter.

YAML Safety: Uses direct string append — NOT add_field() which uses
the destructive parse/rebuild round-trip that destroys list fields.

Usage:
    python add_normative_v2_field.py                  # dry run (default)
    python add_normative_v2_field.py --apply          # actually write
    python add_normative_v2_field.py --apply --force  # overwrite existing
"""

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / ".agent" / "lib"))
from yaml_utils import extract_frontmatter, write_paper, validate_frontmatter
from config import PAPERS_DIR, LOGS_DIR


def add_normative_field(dry_run=True, force=False):
    decisions_path = LOGS_DIR / "normative_v2_decisions.json"
    if not decisions_path.exists():
        print("ERROR: Decisions file not found: {}".format(decisions_path))
        sys.exit(1)

    with open(decisions_path, "r", encoding="utf-8") as f:
        decisions = json.load(f)

    mode = "DRY RUN" if dry_run else "APPLYING"
    print("=== {} ===".format(mode))
    print("Decisions file: {}".format(decisions_path))
    print("Papers to tag: {}".format(len(decisions)))
    print()

    success = 0
    skipped = 0
    errors = 0

    for entry in decisions:
        filename = entry["filename"]
        decision = entry["decision"]  # "Yes" or "Borderline"

        paper_path = PAPERS_DIR / filename
        if not paper_path.exists():
            print("  SKIP (not found): {}".format(filename))
            skipped += 1
            continue

        content = paper_path.read_text(encoding="utf-8")

        # Check if field already exists
        if "normative_ethics_benchmark:" in content:
            if not force:
                print("  SKIP (already tagged): {}".format(filename))
                skipped += 1
                continue

        try:
            fm, body = extract_frontmatter(content)
        except ValueError as e:
            print("  ERROR (bad YAML): {} — {}".format(filename, e))
            errors += 1
            continue

        # Safe append: add field at end of frontmatter string
        # Do NOT use add_field() — it destroys list fields
        field_line = "normative_ethics_benchmark: {}".format(decision)

        if "normative_ethics_benchmark:" in fm:
            # Replace existing value (only if --force)
            fm_new, count = re.subn(
                r'^normative_ethics_benchmark:.*$',
                field_line,
                fm,
                count=1,
                flags=re.MULTILINE
            )
            if count == 0:
                print("  ERROR (replace failed): {}".format(filename))
                errors += 1
                continue
            fm = fm_new
        else:
            # Append new field at end
            fm = fm.rstrip() + "\n" + field_line

        # Validate before writing
        is_valid, issues = validate_frontmatter(fm)
        if not is_valid:
            print("  ERROR (validation): {} — {}".format(filename, issues))
            errors += 1
            continue

        if dry_run:
            print("  WOULD TAG: {} → {}".format(filename, decision))
        else:
            write_paper(paper_path, fm, body, validate=True)
            print("  TAGGED: {} → {}".format(filename, decision))

        success += 1

    print()
    print("=== SUMMARY ===")
    print("  Tagged: {}".format(success))
    print("  Skipped: {}".format(skipped))
    print("  Errors: {}".format(errors))

    if dry_run:
        print("\nThis was a DRY RUN. Use --apply to write changes.")


if __name__ == "__main__":
    apply = "--apply" in sys.argv
    force = "--force" in sys.argv
    add_normative_field(dry_run=not apply, force=force)
