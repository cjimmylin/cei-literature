#!/usr/bin/env python3
"""
Snapshot current ethics scores for all papers before audit changes.
Output: STATISTICS/20260313-normative-pre-audit-snapshot.json
"""

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent / ".agent" / "lib"))

from config import PAPERS_DIR, STATISTICS_DIR

FIELDS = ['ethics_overall', 'virtue_ethics', 'deontological_ethics', 'utilitarian_ethics']


def get_score(frontmatter, field):
    """Extract integer score from frontmatter text."""
    m = re.search(rf'^{re.escape(field)}:\s*"?([^"\n]*)"?', frontmatter, re.MULTILINE)
    if not m:
        return None
    val = m.group(1).strip()
    try:
        return int(val)
    except ValueError:
        if val.lower() == 'yes':
            return 80
        return 0


def main():
    snapshot = {}
    for f in sorted(PAPERS_DIR.glob('*.md')):
        try:
            content = f.read_text(encoding='utf-8')
            if not content.startswith('---'):
                continue
            end = content.find('---', 3)
            if end == -1:
                continue
            fm = content[3:end]
            scores = {}
            for field in FIELDS:
                scores[field] = get_score(fm, field)
            snapshot[f.name] = scores
        except Exception as e:
            print(f"Error reading {f.name}: {e}")

    out_path = STATISTICS_DIR / "20260313-normative-pre-audit-snapshot.json"
    with open(out_path, 'w', encoding='utf-8') as fh:
        json.dump(snapshot, fh, indent=2)
    print(f"Snapshot saved: {out_path}")
    print(f"Papers: {len(snapshot)}")


if __name__ == '__main__':
    main()
