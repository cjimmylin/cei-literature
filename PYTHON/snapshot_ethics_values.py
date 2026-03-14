#!/usr/bin/env python3
"""
Pre/Post Migration Snapshot Tool for Ethics Fields

Captures the current state of ethics_overall, virtue_ethics,
deontological_ethics, and utilitarian_ethics for every paper in the vault.
Run before and after migration to enable diff comparison.

Usage:
    python snapshot_ethics_values.py --label pre-migration
    python snapshot_ethics_values.py --label post-migration
"""

import argparse
import json
import sys
from collections import Counter
from datetime import date
from pathlib import Path

# ── Path setup ───────────────────────────────────────────────────────
sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent / ".agent" / "lib"))

from config import PAPERS_DIR, STATISTICS_DIR
from yaml_utils import extract_frontmatter, parse_frontmatter

ETHICS_FIELDS = ["ethics_overall", "virtue_ethics", "deontological_ethics", "utilitarian_ethics"]


def snapshot_paper(filepath):
    """Read ethics fields from a single paper. Returns dict of raw values."""
    content = filepath.read_text(encoding="utf-8")
    fm_text, _ = extract_frontmatter(content)
    fields = parse_frontmatter(fm_text)

    return {f: fields.get(f, "") for f in ETHICS_FIELDS}


def categorize_value(val):
    """Categorize a raw value for summary counting."""
    if val is None or val == "":
        return "empty"
    s = str(val).strip().strip('"').strip("'")
    if s.lower() == "yes":
        return "Yes"
    if s.lower() == "no":
        return "No"
    if s.lower() in ("unknown", "n/a"):
        return "Unknown"
    # Check if it's a numeric score
    try:
        int(s)
        return "scores"
    except ValueError:
        pass
    try:
        int(float(s))
        return "scores"
    except ValueError:
        pass
    return "other"


def build_summary(papers_data):
    """Build summary counts for each ethics field."""
    summary = {}
    for field in ETHICS_FIELDS:
        counter = Counter()
        for fname, vals in papers_data.items():
            cat = categorize_value(vals.get(field, ""))
            counter[cat] += 1
        summary[field] = dict(counter)
    return summary


def main():
    parser = argparse.ArgumentParser(description="Snapshot ethics field values for all papers")
    parser.add_argument("--label", required=True, help="Label for this snapshot (e.g., pre-migration)")
    args = parser.parse_args()

    today = date.today().isoformat()
    papers_data = {}
    errors = []

    paper_files = sorted(PAPERS_DIR.glob("*.md"))
    print(f"Scanning {len(paper_files)} papers in {PAPERS_DIR} ...")

    for pf in paper_files:
        try:
            papers_data[pf.name] = snapshot_paper(pf)
        except Exception as e:
            errors.append({"file": pf.name, "error": str(e)})
            print(f"  WARNING: {pf.name}: {e}")

    summary = build_summary(papers_data)

    result = {
        "label": args.label,
        "date": today,
        "total_papers": len(papers_data),
        "papers": papers_data,
        "summary": summary,
    }

    if errors:
        result["errors"] = errors

    outpath = STATISTICS_DIR / f"{today.replace('-', '')}-ethics-snapshot-{args.label}.json"
    STATISTICS_DIR.mkdir(parents=True, exist_ok=True)
    with open(outpath, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"\nSnapshot saved: {outpath}")
    print(f"Total papers: {len(papers_data)}")
    if errors:
        print(f"Errors: {len(errors)}")
    print("\nSummary:")
    for field in ETHICS_FIELDS:
        print(f"  {field}: {summary[field]}")


if __name__ == "__main__":
    main()
