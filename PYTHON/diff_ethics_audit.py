#!/usr/bin/env python3
"""
Compare post-audit ethics scores against pre-audit snapshot.
Output: STATISTICS/20260313-normative-audit-v2-diff.json
"""

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent / ".agent" / "lib"))

from config import PAPERS_DIR, STATISTICS_DIR

OLD_FIELDS = ['ethics_overall', 'virtue_ethics', 'deontological_ethics', 'utilitarian_ethics']
NEW_FIELDS = ['care_ethics', 'contractarian_ethics']
ALL_FIELDS = OLD_FIELDS + NEW_FIELDS


def get_score(frontmatter, field):
    m = re.search(rf'^{re.escape(field)}:\s*"?([^"\n]*)"?', frontmatter, re.MULTILINE)
    if not m:
        return 0
    val = m.group(1).strip()
    try:
        return int(val)
    except ValueError:
        return 80 if val.lower() == 'yes' else 0


def main():
    # Load snapshot
    snap_path = STATISTICS_DIR / "20260313-normative-pre-audit-snapshot.json"
    with open(snap_path) as f:
        snapshot = json.load(f)

    # Read current scores
    changed_papers = []
    new_above_50 = []
    new_below_50 = []
    large_changes = []
    care_detected = []
    contract_detected = []

    for fpath in sorted(PAPERS_DIR.glob('*.md')):
        try:
            content = fpath.read_text(encoding='utf-8')
            if not content.startswith('---'):
                continue
            end = content.find('---', 3)
            if end == -1:
                continue
            fm = content[3:end]

            current = {f: get_score(fm, f) for f in ALL_FIELDS}
            old = snapshot.get(fpath.name, {})

            # Check for changes in old fields
            for field in OLD_FIELDS:
                old_val = old.get(field)
                new_val = current[field]
                if old_val is None:
                    continue
                if old_val != new_val:
                    delta = new_val - old_val
                    changed_papers.append({
                        'filename': fpath.name,
                        'field': field,
                        'old': old_val,
                        'new': new_val,
                        'delta': delta,
                    })
                    if abs(delta) > 20:
                        large_changes.append({
                            'filename': fpath.name,
                            'field': field,
                            'old': old_val,
                            'new': new_val,
                            'delta': delta,
                        })
                    # Classification change
                    if old_val >= 50 and new_val < 50:
                        new_below_50.append({
                            'filename': fpath.name,
                            'field': field,
                            'old': old_val,
                            'new': new_val,
                        })
                    elif old_val < 50 and new_val >= 50:
                        new_above_50.append({
                            'filename': fpath.name,
                            'field': field,
                            'old': old_val,
                            'new': new_val,
                        })

            # New fields
            if current.get('care_ethics', 0) >= 50:
                care_detected.append({'filename': fpath.name, 'score': current['care_ethics']})
            if current.get('contractarian_ethics', 0) >= 50:
                contract_detected.append({'filename': fpath.name, 'score': current['contractarian_ethics']})

        except Exception as e:
            print(f"Error: {fpath.name}: {e}")

    report = {
        'summary': {
            'total_field_changes': len(changed_papers),
            'papers_with_changes': len(set(c['filename'] for c in changed_papers)),
            'newly_above_50': len(new_above_50),
            'newly_below_50': len(new_below_50),
            'large_changes_gt20': len(large_changes),
            'care_ethics_detected': len(care_detected),
            'contractarian_ethics_detected': len(contract_detected),
        },
        'newly_above_50': sorted(new_above_50, key=lambda x: x['filename']),
        'newly_below_50': sorted(new_below_50, key=lambda x: x['filename']),
        'large_changes': sorted(large_changes, key=lambda x: -abs(x['delta'])),
        'care_ethics_detected': sorted(care_detected, key=lambda x: -x['score']),
        'contractarian_ethics_detected': sorted(contract_detected, key=lambda x: -x['score']),
    }

    out_path = STATISTICS_DIR / "20260313-normative-audit-v2-diff.json"
    with open(out_path, 'w', encoding='utf-8') as fh:
        json.dump(report, fh, indent=2)

    # Print summary
    s = report['summary']
    print(f"Diff report saved: {out_path}")
    print(f"\nSummary:")
    print(f"  Total field-level changes:  {s['total_field_changes']}")
    print(f"  Papers affected:            {s['papers_with_changes']}")
    print(f"  Newly above 50:             {s['newly_above_50']}")
    print(f"  Newly below 50:             {s['newly_below_50']}")
    print(f"  Large changes (>20 pts):    {s['large_changes_gt20']}")
    print(f"  Care ethics detected:       {s['care_ethics_detected']}")
    print(f"  Contractarian detected:     {s['contractarian_ethics_detected']}")

    if new_above_50:
        print(f"\nNewly above 50 (top 10):")
        for item in new_above_50[:10]:
            print(f"  {item['field']:25} {item['old']:3} → {item['new']:3}  {item['filename']}")

    if new_below_50:
        print(f"\nNewly below 50 (top 10):")
        for item in new_below_50[:10]:
            print(f"  {item['field']:25} {item['old']:3} → {item['new']:3}  {item['filename']}")

    if large_changes:
        print(f"\nLargest changes (top 10):")
        for item in large_changes[:10]:
            print(f"  {item['field']:25} {item['old']:3} → {item['new']:3} ({item['delta']:+d})  {item['filename']}")


if __name__ == '__main__':
    main()
