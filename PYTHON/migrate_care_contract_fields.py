#!/usr/bin/env python3
"""
Migration: Add care_ethics: 0 and contractarian_ethics: 0 to all papers.
Follows same pattern as rv_* migration — uses safe_yaml_set_int for existing fields,
appends for new fields. Places new fields after utilitarian_ethics.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent / ".agent" / "lib"))

from config import PAPERS_DIR

NEW_FIELDS = ['care_ethics', 'contractarian_ethics']
INSERT_AFTER = 'utilitarian_ethics'


def migrate_paper(filepath):
    """Add care_ethics and contractarian_ethics fields if missing."""
    content = filepath.read_text(encoding='utf-8')
    if not content.startswith('---'):
        return False

    end = content.find('\n---', 3)
    if end == -1:
        return False

    fm = content[3:end]
    rest = content[end:]
    changed = False

    for field in NEW_FIELDS:
        # Check if field already exists
        if re.search(rf'^{re.escape(field)}:', fm, re.MULTILINE):
            continue

        # Insert after utilitarian_ethics line
        pattern = rf'^({re.escape(INSERT_AFTER)}:.*$)'
        replacement = rf'\1\n{field}: 0'
        new_fm, count = re.subn(pattern, replacement, fm, count=1, flags=re.MULTILINE)
        if count > 0:
            fm = new_fm
            changed = True
        else:
            # Fallback: append at end
            fm = fm.rstrip() + f'\n{field}: 0'
            changed = True

    if changed:
        filepath.write_text(f'---{fm}{rest}', encoding='utf-8')

    return changed


def main():
    papers = sorted(PAPERS_DIR.glob('*.md'))
    print(f"Migrating {len(papers)} papers...")

    migrated = 0
    skipped = 0
    errors = 0

    for f in papers:
        try:
            if migrate_paper(f):
                migrated += 1
            else:
                skipped += 1
        except Exception as e:
            errors += 1
            print(f"  Error: {f.name}: {e}")

    print(f"\nDone. Migrated: {migrated}, Already had fields: {skipped}, Errors: {errors}")


if __name__ == '__main__':
    main()
