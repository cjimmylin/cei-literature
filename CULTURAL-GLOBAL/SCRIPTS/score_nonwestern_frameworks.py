#!/usr/bin/env python3
"""
Score all papers on 7 non-Western normative ethical frameworks.

Reads each paper's title, abstract, and PDF extract, computes scores
using nonwestern_scoring.py, and writes results to a JSON sidecar file.
Optionally writes scores to paper YAML frontmatter.

Usage:
    python score_nonwestern_frameworks.py [--dry-run] [--write-yaml] [START END]

    --dry-run     Compute scores but don't write any files
    --write-yaml  Write nw_* fields into paper YAML frontmatter
    START END     Process papers START..END (1-indexed, inclusive) for parallel batches

Output:
    DATA/20260403-nw-scores.json          — Full score results
    STATISTICS/20260403-nw-score-report.md — Summary report
"""
from __future__ import annotations

import functools
import json
import os
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

print = functools.partial(print, flush=True)

# ── Path setup ───────────────────────────────────────────────────────
_SCRIPT_DIR = Path(__file__).parent
_CEI_LIT_WS = _SCRIPT_DIR.parent.parent
sys.path.insert(0, str(_CEI_LIT_WS / "PYTHON"))
sys.path.insert(0, str(_CEI_LIT_WS / ".agent" / "lib"))
sys.path.insert(0, str(_SCRIPT_DIR))

from nonwestern_scoring import (
    NW_FIELDS_LIST,
    compute_all_nw_scores,
    get_nw_pinned_score,
    score_paper_nw,
)
from ethics_scoring import load_extract
from config import PAPERS_DIR


def set_or_add_yaml_int(content: str, key: str, value: int) -> str:
    """Set an existing YAML field or append it before the closing '---'.

    Safe pattern per CLAUDE.md rule #2: uses re.subn with count=1.
    If field doesn't exist, inserts before the closing --- delimiter.
    """
    pattern = rf'^{re.escape(key)}:.*$'
    replacement = f'{key}: {int(value)}'
    new_content, count = re.subn(pattern, replacement, content, count=1, flags=re.MULTILINE)
    if count > 0:
        return new_content

    # Field doesn't exist yet — insert before closing ---
    # Find the second '---' (closing delimiter)
    first_end = content.find('---', 0)
    if first_end == -1:
        return content
    second_end = content.find('---', first_end + 3)
    if second_end == -1:
        return content

    # Insert field before the closing ---
    before = content[:second_end].rstrip('\n')
    after = content[second_end:]
    return f"{before}\n{replacement}\n{after}"

# ── Output paths ─────────────────────────────────────────────────────
TODAY = date.today().strftime("%Y%m%d")
DATA_DIR = _SCRIPT_DIR.parent / "DATA"
STATS_DIR = _SCRIPT_DIR.parent / "STATISTICS"
SCORES_PATH = DATA_DIR / f"{TODAY}-nw-scores.json"
REPORT_PATH = STATS_DIR / f"{TODAY}-nw-score-report.md"


def main():
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    write_yaml = "--write-yaml" in args
    args = [a for a in args if not a.startswith("--")]

    # Collect all paper files sorted
    papers = sorted(PAPERS_DIR.glob("*.md"))
    total = len(papers)

    # Optional range for parallel batching
    start_idx = 0
    end_idx = total
    if len(args) >= 2:
        start_idx = int(args[0]) - 1
        end_idx = int(args[1])
    papers = papers[start_idx:end_idx]

    print(f"Scoring {len(papers)} papers on {len(NW_FIELDS_LIST)} non-Western frameworks...")
    if dry_run:
        print("  (DRY RUN — no files will be written)")

    results = []
    field_counts = Counter()  # field → count of papers with score >= 50
    field_totals = Counter()  # field → sum of all scores
    errors = []

    for i, paper_path in enumerate(papers, 1):
        if i % 100 == 0:
            print(f"  Progress: {i}/{len(papers)}")

        try:
            scores = score_paper_nw(paper_path)
        except Exception as e:
            errors.append({"file": paper_path.name, "error": str(e)})
            continue

        entry = {"filename": paper_path.name, "scores": scores}

        # Count detections
        detected = []
        for field in NW_FIELDS_LIST:
            score = scores[field]
            field_totals[field] += score
            if score >= 50:
                field_counts[field] += 1
                detected.append(field)

        entry["detected"] = detected
        results.append(entry)

        # Write to YAML if requested
        if write_yaml and not dry_run:
            content = paper_path.read_text(encoding="utf-8", errors="replace")
            original = content
            for field in NW_FIELDS_LIST:
                content = set_or_add_yaml_int(content, field, scores[field])
            if content != original:
                paper_path.write_text(content, encoding="utf-8")

    # ── Save JSON results ────────────────────────────────────────────
    if not dry_run:
        output_data = {
            "date": TODAY,
            "total_papers": len(results),
            "errors": len(errors),
            "field_counts_gte50": dict(field_counts.most_common()),
            "field_mean_scores": {
                f: round(field_totals[f] / max(len(results), 1), 2)
                for f in NW_FIELDS_LIST
            },
            "papers": results,
        }

        # PID-scoped temp file for safety
        tmp_path = SCORES_PATH.with_suffix(f".tmp.{os.getpid()}.json")
        tmp_path.write_text(json.dumps(output_data, indent=2))
        os.replace(str(tmp_path), str(SCORES_PATH))
        print(f"\nSaved scores to {SCORES_PATH}")

    # ── Print summary ────────────────────────────────────────────────
    print(f"\n{'='*60}")
    print(f"NON-WESTERN FRAMEWORK SCORING RESULTS")
    print(f"{'='*60}")
    print(f"Papers scored: {len(results)}")
    print(f"Errors: {len(errors)}")
    print(f"\nDetections (score >= 50):")
    for field in NW_FIELDS_LIST:
        count = field_counts.get(field, 0)
        mean = field_totals[field] / max(len(results), 1)
        print(f"  {field}: {count} papers ({count/max(len(results),1)*100:.1f}%), mean={mean:.1f}")

    # Papers with any detection
    any_detected = sum(1 for r in results if r["detected"])
    multi_detected = sum(1 for r in results if len(r["detected"]) >= 2)
    print(f"\nPapers with any nw framework >= 50: {any_detected} ({any_detected/max(len(results),1)*100:.1f}%)")
    print(f"Papers with 2+ nw frameworks >= 50: {multi_detected}")

    # ── Save report ──────────────────────────────────────────────────
    if not dry_run:
        report = [
            f"# Non-Western Normative Framework Scoring Report",
            f"",
            f"**Date:** {TODAY}",
            f"**Papers scored:** {len(results)}",
            f"**Errors:** {len(errors)}",
            f"",
            f"## Detection Summary (score >= 50)",
            f"",
            f"| Framework | Papers | % | Mean Score |",
            f"|-----------|--------|---|------------|",
        ]
        for field in NW_FIELDS_LIST:
            count = field_counts.get(field, 0)
            mean = field_totals[field] / max(len(results), 1)
            pct = count / max(len(results), 1) * 100
            report.append(f"| {field} | {count} | {pct:.1f}% | {mean:.1f} |")

        report.extend([
            f"",
            f"**Any framework detected:** {any_detected} ({any_detected/max(len(results),1)*100:.1f}%)",
            f"**Multi-framework papers (2+):** {multi_detected}",
            f"",
            f"## Top Scoring Papers",
            f"",
        ])

        # Top 20 papers by max score
        top_papers = sorted(results, key=lambda r: max(r["scores"].values()), reverse=True)[:20]
        for r in top_papers:
            max_field = max(r["scores"], key=r["scores"].get)
            max_score = r["scores"][max_field]
            detected = ", ".join(r["detected"]) if r["detected"] else "none"
            report.append(f"- **{r['filename']}**: {max_field}={max_score} (detected: {detected})")

        if errors:
            report.extend([f"", f"## Errors", f""])
            for e in errors:
                report.append(f"- {e['file']}: {e['error']}")

        REPORT_PATH.write_text("\n".join(report))
        print(f"Saved report to {REPORT_PATH}")

    if errors:
        print(f"\nErrors:")
        for e in errors[:10]:
            print(f"  {e['file']}: {e['error']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
