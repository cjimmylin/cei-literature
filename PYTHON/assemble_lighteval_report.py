#!/usr/bin/env python3
"""
assemble_lighteval_report.py — Merge 8 score chunks and generate summary report.

Agent 9: Loads all score JSONs, merges, and produces:
  - logs/20260312-lighteval-scores-merged.json
  - STATISTICS/20260312-lighteval-implementability-report.md
"""

import functools
import json
import os
import re
from collections import Counter, defaultdict
from pathlib import Path

print = functools.partial(print, flush=True)

# ── Paths ────────────────────────────────────────────────────────────────────
BASE = Path(__file__).resolve().parent.parent  # CEI-Lit-WS/
LOGS = BASE / "logs"
STATS = BASE / "STATISTICS"

MERGED_JSON = LOGS / "20260312-lighteval-scores-merged.json"
REPORT_PATH = STATS / "20260312-lighteval-implementability-report.md"

TODAY = "2026-03-12"
NUM_AGENTS = 8


def load_chunks():
    """Load and merge all 8 agent score files."""
    all_results = []
    for i in range(1, NUM_AGENTS + 1):
        path = LOGS / f"20260312-lighteval-scores-{i}.json"
        if not path.exists():
            print(f"WARNING: Missing {path.name}")
            continue
        with open(path) as f:
            chunk = json.load(f)
        results = chunk["results"]
        print(f"  Loaded {path.name}: {len(results)} papers")
        all_results.extend(results)

    # Sort by score descending, then filename
    all_results.sort(key=lambda r: (-r["total_score"], r["filename"]))
    return all_results


def generate_report(results):
    """Generate the summary markdown report."""
    total = len(results)

    # Tier counts
    tier_counts = Counter(r["tier"] for r in results)
    tier_order = ["Ready", "Possible", "Barriers", "Not Implementable"]

    # Task type distribution
    task_counts = Counter(r["lighteval_task_type"] for r in results)

    # Score distribution
    score_buckets = Counter()
    for r in results:
        bucket = int(r["total_score"])
        score_buckets[bucket] = score_buckets.get(bucket, 0) + 1

    # Year distribution for top tiers
    year_dist = defaultdict(lambda: Counter())
    for r in results:
        year = re.match(r"^(\d{4})-", r["filename"])
        yr = year.group(1) if year else "????"
        year_dist[r["tier"]][yr] += 1

    # Missing dimension stats
    missing_counts = Counter()
    for r in results:
        for m in r["whats_missing"]:
            missing_counts[m] += 1

    # Average score
    avg = sum(r["total_score"] for r in results) / total if total else 0

    # ── Build report ─────────────────────────────────────────────────────
    lines = [
        f"# lighteval Implementability Report",
        f"",
        f"**Generated:** {TODAY}  ",
        f"**Papers scored:** {total}  ",
        f"**Average score:** {avg:.2f}/10.0  ",
        f"**Scoring model:** 9-dimension weighted (HF presence = 2.0×)",
        f"",
        f"## Executive Summary",
        f"",
        f"| Tier | Score Range | Count | % |",
        f"|------|------------|-------|---|",
    ]
    for tier in tier_order:
        count = tier_counts.get(tier, 0)
        pct = count / total * 100 if total else 0
        ranges = {"Ready": "8.0-10.0", "Possible": "5.0-7.9",
                  "Barriers": "2.0-4.9", "Not Implementable": "0.0-1.9"}
        lines.append(f"| {tier} | {ranges.get(tier, '')} | {count} | {pct:.1f}% |")
    lines.append(f"| **Total** | | **{total}** | |")
    lines.append("")

    # Score distribution histogram
    lines.append("## Score Distribution")
    lines.append("")
    lines.append("| Score | Count | Bar |")
    lines.append("|-------|-------|-----|")
    for s in range(10, -1, -1):
        count = score_buckets.get(s, 0)
        bar = "█" * (count // 5) if count > 0 else ""
        lines.append(f"| {s}.0–{s}.9 | {count} | {bar} |")
    lines.append("")

    # Task type distribution
    lines.append("## lighteval Task Types")
    lines.append("")
    lines.append("| Type | Count | % |")
    lines.append("|------|-------|---|")
    for ttype, count in task_counts.most_common():
        pct = count / total * 100
        lines.append(f"| `{ttype}` | {count} | {pct:.1f}% |")
    lines.append("")

    # Most common missing dimensions
    lines.append("## Most Common Missing Dimensions")
    lines.append("")
    lines.append("| Dimension | Papers Missing | % |")
    lines.append("|-----------|---------------|---|")
    for dim, count in missing_counts.most_common():
        pct = count / total * 100
        lines.append(f"| {dim} | {count} | {pct:.1f}% |")
    lines.append("")

    # Top 30 most implementable
    lines.append("## Top 30 Most Implementable Papers")
    lines.append("")
    lines.append("| # | Paper | Score | Tier | Task Type | Missing |")
    lines.append("|---|-------|-------|------|-----------|---------|")
    for i, r in enumerate(results[:30], 1):
        fn = r["filename"].replace(".md", "")
        missing = len(r["whats_missing"])
        lines.append(
            f"| {i} | {fn} | **{r['total_score']}** | {r['tier']} | "
            f"`{r['lighteval_task_type']}` | {missing} |"
        )
    lines.append("")

    # By-category: year × tier
    lines.append("## Year × Tier Breakdown")
    lines.append("")
    all_years = sorted(set(yr for tc in year_dist.values() for yr in tc))
    header = "| Year | " + " | ".join(tier_order) + " | Total |"
    sep = "|------|" + "|".join(["---"] * len(tier_order)) + "|-------|"
    lines.append(header)
    lines.append(sep)
    for yr in all_years:
        row_total = sum(year_dist[t].get(yr, 0) for t in tier_order)
        cells = " | ".join(str(year_dist[t].get(yr, 0)) for t in tier_order)
        lines.append(f"| {yr} | {cells} | {row_total} |")
    lines.append("")

    # Comparison with lm-eval-harness scores
    lines.append("## Comparison: lighteval vs lm-eval-harness Tiers")
    lines.append("")
    cross = defaultdict(Counter)
    for r in results:
        cross[r.get("lm_eval_tier", "?")][r["tier"]] += 1
    lm_tiers = sorted(cross.keys())
    header = "| lm-eval Tier | " + " | ".join(tier_order) + " |"
    sep = "|-------------|" + "|".join(["---"] * len(tier_order)) + "|"
    lines.append(header)
    lines.append(sep)
    for lt in lm_tiers:
        cells = " | ".join(str(cross[lt].get(t, 0)) for t in tier_order)
        lines.append(f"| {lt} | {cells} |")
    lines.append("")

    lines.append("---")
    lines.append(f"*Generated by `assemble_lighteval_report.py` on {TODAY}*")
    lines.append("")

    return "\n".join(lines)


def main():
    print("Loading score chunks...")
    results = load_chunks()
    print(f"Merged: {len(results)} papers")

    # Write merged JSON
    tmp = MERGED_JSON.with_suffix(f".tmp.{os.getpid()}.json")
    with open(tmp, "w") as f:
        json.dump({
            "generated": TODAY,
            "total": len(results),
            "results": results,
        }, f, indent=2)
    os.replace(str(tmp), str(MERGED_JSON))
    print(f"Wrote {MERGED_JSON.name}")

    # Generate and write report
    report = generate_report(results)
    with open(REPORT_PATH, "w") as f:
        f.write(report)
    print(f"Wrote {REPORT_PATH.name}")

    # Summary
    tier_counts = Counter(r["tier"] for r in results)
    print(f"\nTier summary:")
    for tier in ["Ready", "Possible", "Barriers", "Not Implementable"]:
        print(f"  {tier}: {tier_counts.get(tier, 0)}")


if __name__ == "__main__":
    main()
