#!/usr/bin/env python3
"""
generate_openai_evals_report.py — Generate markdown reports from scored JSON.

Reads the intermediate JSON from scan_openai_evals_implementability.py and
produces two reports:
  1. Summary report (STATISTICS/20260312-openai-evals-implementability-report.md)
  2. Per-paper detailed report (STATISTICS/20260312-openai-evals-paper-reports.md)

Usage:
    cd CEI-Lit-WS && ../.venv/bin/python PYTHON/generate_openai_evals_report.py
"""

import functools
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

print = functools.partial(print, flush=True)

# ── Paths ────────────────────────────────────────────────────────────────────
_script_dir = Path(__file__).resolve().parent
if str(_script_dir) not in sys.path:
    sys.path.insert(0, str(_script_dir))

from vault_config import STATISTICS_DIR, LOGS_DIR

INPUT_JSON = LOGS_DIR / "20260312-openai-evals-implementability-data.json"
SUMMARY_REPORT = STATISTICS_DIR / "20260312-openai-evals-implementability-report.md"
PAPER_REPORT = STATISTICS_DIR / "20260312-openai-evals-paper-reports.md"

TODAY = "2026-03-12"

# Also try to load lm-eval and lighteval data for cross-reference
LM_EVAL_JSON = LOGS_DIR / "20260312-lm-eval-implementability-data.json"
LIGHTEVAL_JSON = LOGS_DIR / "20260312-lighteval-scores-merged.json"


def load_data():
    """Load the scored JSON."""
    if not INPUT_JSON.exists():
        print(f"[ERROR] Input JSON not found: {INPUT_JSON}")
        sys.exit(1)
    data = json.loads(INPUT_JSON.read_text(encoding="utf-8"))
    return data["results"]


def load_cross_reference():
    """Load lm-eval and lighteval data for cross-referencing."""
    cross = {}

    if LM_EVAL_JSON.exists():
        try:
            lm_raw = json.loads(LM_EVAL_JSON.read_text(encoding="utf-8"))
            # lm-eval JSON may be {papers: [...]} or a flat list
            lm_data = lm_raw.get("papers", lm_raw) if isinstance(lm_raw, dict) else lm_raw
            for entry in lm_data:
                cross.setdefault(entry["filename"], {})["lm_eval_score"] = entry.get("score", 0)
                cross[entry["filename"]]["lm_eval_tier"] = entry.get("tier", "")
        except Exception as e:
            print(f"[WARN] Could not load lm-eval data: {e}")

    if LIGHTEVAL_JSON.exists():
        try:
            le_data = json.loads(LIGHTEVAL_JSON.read_text(encoding="utf-8"))
            for entry in le_data.get("results", []):
                cross.setdefault(entry["filename"], {})["lighteval_score"] = entry.get("total_score", 0)
                cross[entry["filename"]]["lighteval_tier"] = entry.get("tier", "")
        except Exception as e:
            print(f"[WARN] Could not load lighteval data: {e}")

    return cross


def generate_summary_report(results, cross_ref):
    """Generate the summary markdown report."""
    total = len(results)
    tier_counts = Counter(r["tier"] for r in results)
    template_counts = Counter(r["oai_eval_template"] for r in results)
    tier_order = ["Ready", "Possible", "Barriers", "Not Implementable"]

    # Score distribution
    score_buckets = Counter()
    for r in results:
        bucket = int(r["total_score"])
        score_buckets[bucket] = score_buckets.get(bucket, 0) + 1

    # Year distribution
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

    avg = sum(r["total_score"] for r in results) / total if total else 0

    # Count papers with all three flags
    triple_flag = sum(1 for r in results
                      if r.get("is_benchmark") and r.get("is_eval") and r.get("is_dataset"))

    lines = [
        f"# OpenAI Evals Implementability Report",
        f"",
        f"**Generated:** {TODAY}  ",
        f"**Papers scored:** {total}  ",
        f"**Average score:** {avg:.2f}/10.0  ",
        f"**Scoring model:** 9-dimension weighted (JSONL-convertible + template mapping = 1.5x each)  ",
        f"**Framework:** [OpenAI Evals](https://github.com/openai/evals) — JSONL data + YAML registry configs",
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
    lines.append(f"Papers with all three flags (benchmark+eval+dataset): {triple_flag}")
    lines.append("")

    # ── Section 1: Ready tier ─────────────────────────────────────────────
    ready = [r for r in results if r["tier"] == "Ready"]
    lines.append("## 1. Ready (score >= 8.0)")
    lines.append("")
    if ready:
        lines.append(f"{len(ready)} papers can be implemented now with minimal effort.")
        lines.append("")
        lines.append("| # | Paper | Score | Template | Data URL | Signals |")
        lines.append("|---|-------|-------|----------|----------|---------|")
        for i, r in enumerate(ready, 1):
            fn = r["filename"].replace(".md", "")
            sigs = ", ".join(r.get("signals", [])[:4])
            data_url = r.get("data_url", "")[:50]
            lines.append(
                f"| {i} | {fn} | **{r['total_score']}** | "
                f"`{r['oai_eval_template']}` | {data_url} | {sigs} |"
            )
    else:
        lines.append("No papers in this tier.")
    lines.append("")

    # ── Section 2: Possible tier ──────────────────────────────────────────
    possible = [r for r in results if r["tier"] == "Possible"]
    lines.append("## 2. Possible (5.0-8.0)")
    lines.append("")
    if possible:
        lines.append(f"{len(possible)} papers are feasible with some data preparation.")
        lines.append("")
        lines.append("| # | Paper | Score | Template | Missing Dimensions |")
        lines.append("|---|-------|-------|----------|--------------------|")
        for i, r in enumerate(possible[:50], 1):
            fn = r["filename"].replace(".md", "")
            missing = ", ".join(r["whats_missing"][:3])
            lines.append(
                f"| {i} | {fn} | {r['total_score']} | "
                f"`{r['oai_eval_template']}` | {missing} |"
            )
        if len(possible) > 50:
            lines.append(f"| | *... and {len(possible) - 50} more* | | | |")
    else:
        lines.append("No papers in this tier.")
    lines.append("")

    # ── Section 3: Barriers tier ──────────────────────────────────────────
    barriers = [r for r in results if r["tier"] == "Barriers"]
    lines.append("## 3. Barriers (2.0-5.0)")
    lines.append("")
    lines.append(f"{len(barriers)} papers have significant gaps to fill.")
    lines.append("")

    # ── Section 4: Not Implementable ──────────────────────────────────────
    not_impl = [r for r in results if r["tier"] == "Not Implementable"]
    lines.append("## 4. Not Implementable (< 2.0)")
    lines.append("")
    lines.append(f"{len(not_impl)} papers are theoretical or lack any benchmark/dataset.")
    lines.append("")

    # ── Section 5: Template Distribution ──────────────────────────────────
    lines.append("## 5. Template Distribution")
    lines.append("")
    lines.append("OpenAI Evals template types mapped to papers:")
    lines.append("")
    lines.append("| Template | Count | % | Description |")
    lines.append("|----------|-------|---|-------------|")
    template_desc = {
        "Match": "Exact string match (MCQ, classification)",
        "FuzzyMatch": "Approximate match (QA with minor variations)",
        "Includes": "Substring inclusion check",
        "ModelBasedClassify": "LLM-graded with rubric (ethics, open-ended)",
        "JsonMatch": "Structured JSON output matching",
        "unknown": "No clear task structure identified",
    }
    for template, count in template_counts.most_common():
        pct = count / total * 100
        desc = template_desc.get(template, "")
        lines.append(f"| `{template}` | {count} | {pct:.1f}% | {desc} |")
    lines.append("")

    # Template by tier
    lines.append("### Template x Tier")
    lines.append("")
    all_templates = sorted(template_counts.keys())
    header = "| Template | " + " | ".join(tier_order) + " |"
    sep = "|----------|" + "|".join(["---"] * len(tier_order)) + "|"
    lines.append(header)
    lines.append(sep)
    template_tier = defaultdict(Counter)
    for r in results:
        template_tier[r["oai_eval_template"]][r["tier"]] += 1
    for tmpl in all_templates:
        cells = " | ".join(str(template_tier[tmpl].get(t, 0)) for t in tier_order)
        lines.append(f"| `{tmpl}` | {cells} |")
    lines.append("")

    # ── Score distribution histogram ──────────────────────────────────────
    lines.append("## Score Distribution")
    lines.append("")
    lines.append("| Score | Count | Bar |")
    lines.append("|-------|-------|-----|")
    for s in range(10, -1, -1):
        count = score_buckets.get(s, 0)
        bar = "#" * (count // 5) if count > 0 else ""
        lines.append(f"| {s}.0-{s}.9 | {count} | {bar} |")
    lines.append("")

    # ── Most common missing dimensions ────────────────────────────────────
    lines.append("## Most Common Missing Dimensions")
    lines.append("")
    lines.append("| Dimension | Papers Missing | % |")
    lines.append("|-----------|---------------|---|")
    for dim, count in missing_counts.most_common():
        pct = count / total * 100
        lines.append(f"| {dim} | {count} | {pct:.1f}% |")
    lines.append("")

    # ── Top 30 most implementable ─────────────────────────────────────────
    lines.append("## Top 30 Most Implementable Papers")
    lines.append("")
    lines.append("| # | Paper | Score | Tier | Template | Missing |")
    lines.append("|---|-------|-------|------|----------|---------|")
    for i, r in enumerate(results[:30], 1):
        fn = r["filename"].replace(".md", "")
        missing = len(r["whats_missing"])
        lines.append(
            f"| {i} | {fn} | **{r['total_score']}** | {r['tier']} | "
            f"`{r['oai_eval_template']}` | {missing} |"
        )
    lines.append("")

    # ── Year x Tier breakdown ─────────────────────────────────────────────
    lines.append("## Year x Tier Breakdown")
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

    # ── Cross-Reference section ───────────────────────────────────────────
    if cross_ref:
        lines.append("## Cross-Reference: OpenAI Evals vs lm-eval / lighteval")
        lines.append("")

        # lm-eval cross-reference
        lm_cross = defaultdict(Counter)
        le_cross = defaultdict(Counter)
        for r in results:
            cr = cross_ref.get(r["filename"], {})
            lm_tier = cr.get("lm_eval_tier", "?")
            le_tier = cr.get("lighteval_tier", "?")
            lm_cross[lm_tier][r["tier"]] += 1
            le_cross[le_tier][r["tier"]] += 1

        if any(t != "?" for t in lm_cross.keys()):
            lines.append("### vs lm-eval-harness")
            lines.append("")
            lm_tiers = sorted(lm_cross.keys())
            header = "| lm-eval Tier | " + " | ".join(tier_order) + " |"
            sep = "|-------------|" + "|".join(["---"] * len(tier_order)) + "|"
            lines.append(header)
            lines.append(sep)
            for lt in lm_tiers:
                cells = " | ".join(str(lm_cross[lt].get(t, 0)) for t in tier_order)
                lines.append(f"| {lt} | {cells} |")
            lines.append("")

        if any(t != "?" for t in le_cross.keys()):
            lines.append("### vs lighteval")
            lines.append("")
            le_tiers = sorted(le_cross.keys())
            header = "| lighteval Tier | " + " | ".join(tier_order) + " |"
            sep = "|---------------|" + "|".join(["---"] * len(tier_order)) + "|"
            lines.append(header)
            lines.append(sep)
            for lt in le_tiers:
                cells = " | ".join(str(le_cross[lt].get(t, 0)) for t in tier_order)
                lines.append(f"| {lt} | {cells} |")
            lines.append("")

    lines.append("---")
    lines.append(f"*Generated by `generate_openai_evals_report.py` on {TODAY}*")
    lines.append("")

    return "\n".join(lines)


def generate_paper_report(results, cross_ref):
    """Generate the per-paper detailed report."""
    from openai_evals_scoring import (
        format_paper_detail, format_paper_summary_line,
        TOTAL_WEIGHT,
    )

    lines = [
        f"# OpenAI Evals — Per-Paper Implementability Reports",
        f"",
        f"**Generated:** {TODAY}  ",
        f"**Papers scored:** {len(results)}  ",
        f"**Detailed reports for:** papers scoring >= 5.0 (Ready + Possible tiers)",
        f"",
        f"---",
        f"",
    ]

    # Detailed reports for Ready + Possible (>= 5.0)
    detailed = [r for r in results if r["total_score"] >= 5.0]
    appendix = [r for r in results if r["total_score"] < 5.0]

    lines.append(f"## Detailed Reports ({len(detailed)} papers)")
    lines.append("")

    for r in detailed:
        # Reconstruct paper dict for format_paper_detail
        paper = {
            "filename": r["filename"],
            "signals": r.get("signals", []),
            "survey_data": r.get("survey_data"),
            "impl_details": r.get("impl_details", {}),
            "meta": {"DATA_URL": r.get("data_url", "")},
        }
        detail = format_paper_detail(r, paper)

        # Add cross-reference line if available
        cr = cross_ref.get(r["filename"], {})
        if cr:
            xref_parts = []
            if "lm_eval_score" in cr:
                xref_parts.append(f"lm-eval: {cr['lm_eval_score']} ({cr.get('lm_eval_tier', '?')})")
            if "lighteval_score" in cr:
                xref_parts.append(f"lighteval: {cr['lighteval_score']} ({cr.get('lighteval_tier', '?')})")
            if xref_parts:
                detail = detail.replace("---\n\n", f"**Cross-ref:** {' | '.join(xref_parts)}\n\n---\n\n")

        lines.append(detail)

    # Appendix: summary lines for papers < 5.0
    lines.append(f"## Appendix: Papers Below 5.0 ({len(appendix)} papers)")
    lines.append("")
    lines.append("| Paper | Score | Tier | Template | Status |")
    lines.append("|-------|-------|------|----------|--------|")
    for r in appendix:
        lines.append(format_paper_summary_line(r))
    lines.append("")

    lines.append("---")
    lines.append(f"*Generated by `generate_openai_evals_report.py` on {TODAY}*")
    lines.append("")

    return "\n".join(lines)


def main():
    print("Loading scored data...")
    results = load_data()
    print(f"  Loaded {len(results)} papers")

    print("Loading cross-reference data...")
    cross_ref = load_cross_reference()
    print(f"  Cross-ref entries: {len(cross_ref)}")

    print("Generating summary report...")
    summary = generate_summary_report(results, cross_ref)
    SUMMARY_REPORT.write_text(summary, encoding="utf-8")
    print(f"  Wrote {SUMMARY_REPORT.name}")

    print("Generating per-paper report...")
    paper_report = generate_paper_report(results, cross_ref)
    PAPER_REPORT.write_text(paper_report, encoding="utf-8")
    print(f"  Wrote {PAPER_REPORT.name}")

    # Quick summary
    from collections import Counter
    tier_counts = Counter(r["tier"] for r in results)
    template_counts = Counter(r["oai_eval_template"] for r in results)
    print()
    print("Tier summary:")
    for tier in ["Ready", "Possible", "Barriers", "Not Implementable"]:
        print(f"  {tier}: {tier_counts.get(tier, 0)}")
    print()
    print("Top template types:")
    for tmpl, count in template_counts.most_common(5):
        print(f"  {tmpl}: {count}")
    print()
    print("Done.")


if __name__ == "__main__":
    main()
