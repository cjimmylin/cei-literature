#!/usr/bin/env python3
"""Build a 25-feature Quick Assessment subset from the 157-feature moral psychology
benchmark evaluation framework.

Selection method:
  1. For each feature, compute variance across 54 benchmarks (high = discriminating)
  2. Compute non-null rate (features with many nulls are less useful)
  3. Discriminative power = variance * non_null_rate
  4. Allocate 25 features proportionally across 7 tiers
  5. Within each tier, pick the N features with highest discriminative power

Outputs:
  - 20260404-quick-assessment-25.json  (structured, machine-readable)
  - 20260404-quick-assessment-25.md    (human-readable document)

Usage:
  cd CEI-Lit-WS && ../.venv/bin/python MORAL-PSYCH/scripts/build_quick_assessment.py
"""
from __future__ import annotations

import json
import math
import statistics
import sys
from collections import defaultdict
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
MORAL_PSYCH_DIR = SCRIPT_DIR.parent
MATRIX_PATH = MORAL_PSYCH_DIR / "20260404-extended-feature-matrix-v3.json"
FRAMEWORK_PATH = MORAL_PSYCH_DIR / "COUNCIL" / "20260404-feature-framework-v2.md"
OUT_JSON = MORAL_PSYCH_DIR / "20260404-quick-assessment-25.json"
OUT_MD = MORAL_PSYCH_DIR / "20260404-quick-assessment-25.md"

# Composite keys to skip in original_scores
COMPOSITE_KEYS = {"PD", "PE", "CI"}

# Tier allocation (proportional to actual feature counts, summing to 25)
# Actual tier sizes: A=6, B=6, C=4, D=24, E=44, F=44, G=29 = 157
TIER_ALLOCATION = {"A": 2, "B": 2, "C": 1, "D": 4, "E": 6, "F": 6, "G": 4}


# ---------------------------------------------------------------------------
# Feature name / rubric lookup from the framework markdown
# ---------------------------------------------------------------------------
def parse_feature_names(framework_path: Path) -> dict[str, dict[str, str]]:
    """Parse feature ID -> {name, description} from the framework markdown."""
    import re

    text = framework_path.read_text(encoding="utf-8")
    features: dict[str, dict[str, str]] = {}

    # Built-in rubrics for Tier A/B/C features (2-column tables without descriptions)
    builtin_rubrics: dict[str, str] = {
        "A1": "Depth of psychological construct operationalization: surface behavioral measures (low) vs. deep cognitive/affective processes (high).",
        "A2": "Breadth of moral foundation coverage (e.g., MFT's 5-6 foundations, Schwartz's values). How many distinct moral dimensions does the benchmark measure?",
        "A3": "Complexity of moral dilemmas presented: simple binary choices (low) vs. multi-factor tradeoffs with competing values (high).",
        "A4": "Richness of response format: forced-choice binary (low) vs. free-text justification with Likert scales (high).",
        "A5": "Degree of cultural grounding in benchmark design: WEIRD-only assumptions (low) vs. cross-cultural development with local validation (high).",
        "A6": "Internal theoretical coherence: ad-hoc item collection (low) vs. systematic derivation from a coherent theoretical framework (high).",
        "B1": "Number of items in the benchmark. Higher scores for moderate counts (20-60 items); very low (<10) or very high (>500) score lower.",
        "B2": "Time required to administer the benchmark to one model. Lower time scores higher: <15 min (high) vs. >2 hours (low).",
        "B3": "Degree of scoring automation: manual expert coding (low) vs. fully automated deterministic scoring (high).",
        "B4": "Clarity and interpretability of benchmark output: raw numbers (low) vs. structured profiles with norms (high).",
        "B5": "Simplicity and clarity of administration instructions for LLM benchmarking.",
        "B6": "Effort required to adapt the benchmark for new LLMs or new model families.",
        "B7": "Platform/infrastructure requirements: custom hardware (low) vs. standard API calls (high).",
        "B8": "Open access availability: proprietary/paywalled (low) vs. fully open with permissive license (high).",
        "B9": "Completeness of benchmark documentation: minimal README (low) vs. full datasheet + model card equivalent (high).",
        "B10": "Community adoption: unused (low) vs. widely used in published LLM evaluations with active community (high).",
        "C1": "Total citation count of the benchmark paper (log-scaled).",
        "C2": "Recent citation velocity: citations in the last 2 years as a proportion of total.",
        "C3": "Contribution to the lead author's h-index; proxy for the paper's standing in the field.",
        "C4": "Breadth of citing disciplines: CS-only (low) vs. psychology + philosophy + CS + policy (high).",
        "C5": "How often other benchmark papers cite this benchmark as a foundation or comparison point.",
    }

    # Parse 2-column table rows: | A1 | Construct depth |
    two_col_pattern = re.compile(
        r"^\|\s*([A-G]\d+)\s*\|\s*([^|]+?)\s*\|\s*$", re.MULTILINE
    )
    for m in two_col_pattern.finditer(text):
        fid = m.group(1)
        name = m.group(2).strip()
        desc = builtin_rubrics.get(fid, "See full framework for details.")
        features[fid] = {"name": name, "description": desc}

    # Parse 5-column table rows: | D1 | Name | Member | Scale | Description... |
    # Use [^|\n]+ to prevent cross-line matching
    five_col_pattern = re.compile(
        r"^\|\s*([A-G]\d+)\s*\|\s*([^|\n]+?)\s*\|[^|\n]+\|[^|\n]+\|\s*(.+?)\s*\|",
        re.MULTILINE,
    )
    for m in five_col_pattern.finditer(text):
        fid = m.group(1)
        name = m.group(2).strip()
        desc = m.group(3).strip()
        features[fid] = {"name": name, "description": desc}

    return features


# ---------------------------------------------------------------------------
# Extract scores
# ---------------------------------------------------------------------------
def extract_all_scores(matrix: list[dict]) -> dict[str, list[float | None]]:
    """Return {feature_id: [score_or_None for each benchmark]}."""
    scores: dict[str, list[float | None]] = defaultdict(list)

    for entry in matrix:
        # original_scores: flat int/float values
        seen_orig: set[str] = set()
        for k, v in entry.get("original_scores", {}).items():
            if k in COMPOSITE_KEYS:
                continue
            seen_orig.add(k)
            scores[k].append(v)

        # new_scores: nested dicts with 'score' key
        for k, v in entry.get("new_scores", {}).items():
            if isinstance(v, dict):
                scores[k].append(v.get("score"))
            else:
                scores[k].append(v)

    return dict(scores)


# ---------------------------------------------------------------------------
# Compute discriminative power
# ---------------------------------------------------------------------------
def compute_discriminative_power(
    all_scores: dict[str, list[float | None]],
) -> list[dict]:
    """For each feature, compute variance, non-null rate, discriminative power."""
    results = []
    n_benchmarks = max(len(v) for v in all_scores.values())

    for fid, raw in sorted(all_scores.items()):
        valid = [x for x in raw if x is not None]
        n_valid = len(valid)
        non_null_rate = n_valid / n_benchmarks if n_benchmarks > 0 else 0.0

        if n_valid >= 2:
            var = statistics.variance(valid)
        else:
            var = 0.0

        disc_power = var * non_null_rate

        tier = fid[0]
        results.append(
            {
                "id": fid,
                "tier": tier,
                "variance": round(var, 2),
                "non_null_rate": round(non_null_rate, 4),
                "discriminative_power": round(disc_power, 2),
                "n_valid": n_valid,
                "mean": round(statistics.mean(valid), 1) if valid else None,
            }
        )

    return results


# ---------------------------------------------------------------------------
# Select top-N per tier
# ---------------------------------------------------------------------------
def select_features(
    power_data: list[dict], allocation: dict[str, int]
) -> list[dict]:
    """Pick the N highest-discriminative-power features per tier."""
    by_tier: dict[str, list[dict]] = defaultdict(list)
    for item in power_data:
        by_tier[item["tier"]].append(item)

    selected = []
    for tier in sorted(allocation):
        n = allocation[tier]
        candidates = sorted(
            by_tier.get(tier, []),
            key=lambda x: x["discriminative_power"],
            reverse=True,
        )
        selected.extend(candidates[:n])

    # Sort selected by tier letter then numeric ID
    selected.sort(key=lambda x: (x["tier"], int(x["id"][1:])))
    return selected


# ---------------------------------------------------------------------------
# Compute benchmark quick composites
# ---------------------------------------------------------------------------
def compute_benchmark_scores(
    matrix: list[dict],
    selected_ids: set[str],
    all_scores: dict[str, list[float | None]],
) -> list[dict]:
    """For each benchmark, compute quick composite (mean of 25 selected features)."""
    results = []

    for i, entry in enumerate(matrix):
        # Collect the 25 feature scores for this benchmark
        feature_vals: dict[str, float | None] = {}

        # From original_scores
        for k, v in entry.get("original_scores", {}).items():
            if k in selected_ids:
                feature_vals[k] = v

        # From new_scores
        for k, v in entry.get("new_scores", {}).items():
            if k in selected_ids:
                if isinstance(v, dict):
                    feature_vals[k] = v.get("score")
                else:
                    feature_vals[k] = v

        valid_scores = [v for v in feature_vals.values() if v is not None]
        quick_composite = (
            round(statistics.mean(valid_scores), 2) if valid_scores else None
        )

        results.append(
            {
                "benchmark": entry.get("short_title", entry.get("file", "")),
                "file": entry.get("file", ""),
                "rank": entry.get("rank"),
                "quick_composite": quick_composite,
                "full_composite": entry.get("composite"),
                "scores": {k: feature_vals.get(k) for k in sorted(selected_ids)},
            }
        )

    return results


# ---------------------------------------------------------------------------
# Correlation
# ---------------------------------------------------------------------------
def pearson_r(xs: list[float], ys: list[float]) -> float:
    """Compute Pearson correlation coefficient."""
    n = len(xs)
    if n < 3:
        return 0.0
    mx = statistics.mean(xs)
    my = statistics.mean(ys)
    sx = math.sqrt(sum((x - mx) ** 2 for x in xs) / (n - 1))
    sy = math.sqrt(sum((y - my) ** 2 for y in ys) / (n - 1))
    if sx == 0 or sy == 0:
        return 0.0
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / (n - 1)
    return cov / (sx * sy)


def rank_correlation(xs: list[float], ys: list[float]) -> float:
    """Compute Spearman rank correlation."""

    def ranks(vals: list[float]) -> list[float]:
        sorted_vals = sorted(enumerate(vals), key=lambda t: t[1])
        rank_list = [0.0] * len(vals)
        i = 0
        while i < len(sorted_vals):
            j = i
            while j < len(sorted_vals) and sorted_vals[j][1] == sorted_vals[i][1]:
                j += 1
            avg_rank = (i + j + 1) / 2  # 1-based average
            for k in range(i, j):
                rank_list[sorted_vals[k][0]] = avg_rank
            i = j
        return rank_list

    rx = ranks(xs)
    ry = ranks(ys)
    return pearson_r(rx, ry)


# ---------------------------------------------------------------------------
# Generate markdown output
# ---------------------------------------------------------------------------
def generate_markdown(
    selected: list[dict],
    benchmark_scores: list[dict],
    correlation: float,
    spearman: float,
    r_squared: float,
    feature_names: dict[str, dict[str, str]],
    actual_tier_sizes: dict[str, int],
) -> str:
    """Generate the human-readable markdown document."""
    lines = []
    lines.append("# Quick Assessment: 25-Feature Subset for Moral Psychology Benchmarks")
    lines.append("")
    lines.append("## Overview")
    lines.append("")
    lines.append(
        "This document defines a practical 25-feature subset of the full 157-feature "
        "moral psychology benchmark evaluation framework. The Quick Assessment is designed "
        "to take approximately 60 minutes per benchmark (vs 5+ hours for the full framework), "
        "while preserving strong correlation with the comprehensive evaluation."
    )
    lines.append("")
    lines.append("**Selection method:** Variance-based discriminative power across 54 benchmarks")
    lines.append(f"**Correlation with full assessment:** Pearson r = {correlation:.3f} (r-squared = {r_squared:.1f}%)")
    lines.append(f"**Rank preservation:** Spearman rho = {spearman:.3f}")
    lines.append(f"**Estimated scoring time:** ~2.5 min/feature x 25 = ~60 minutes total")
    lines.append("")

    # Tier allocation table
    lines.append("## Tier Allocation")
    lines.append("")
    lines.append("| Tier | Name | Selected | Total | Selection Rate |")
    lines.append("|------|------|----------|-------|----------------|")
    tier_names = {
        "A": "Psychological Depth",
        "B": "Practical Ease",
        "C": "Citation Impact",
        "D": "Psychometric Rigor",
        "E": "LLM-Specific Validity",
        "F": "Cultural & Philosophical Breadth",
        "G": "Theory Fidelity & Provenance",
    }
    for t in "ABCDEFG":
        n_sel = sum(1 for s in selected if s["tier"] == t)
        n_tot = actual_tier_sizes.get(t, 0)
        rate = f"{n_sel / n_tot * 100:.0f}%" if n_tot > 0 else "N/A"
        lines.append(f"| {t} | {tier_names[t]} | {n_sel} | {n_tot} | {rate} |")
    lines.append(f"| **Total** | | **25** | **{sum(actual_tier_sizes.values())}** | **{25 / sum(actual_tier_sizes.values()) * 100:.0f}%** |")
    lines.append("")

    # Selected features table
    lines.append("## Selected Features")
    lines.append("")
    lines.append("| # | ID | Tier | Name | Disc. Power | Variance | Non-Null Rate |")
    lines.append("|---|-----|------|------|-------------|----------|---------------|")
    for i, feat in enumerate(selected, 1):
        fname = feature_names.get(feat["id"], {}).get("name", feat["id"])
        lines.append(
            f"| {i} | {feat['id']} | {feat['tier']} | {fname} | "
            f"{feat['discriminative_power']:.1f} | {feat['variance']:.1f} | "
            f"{feat['non_null_rate']:.2f} |"
        )
    lines.append("")

    # Scoring rubrics
    lines.append("## Scoring Rubrics")
    lines.append("")
    lines.append("Each feature is scored on a 0-100 scale. Below are brief rubrics for the 25 selected features.")
    lines.append("")
    for feat in selected:
        fid = feat["id"]
        info = feature_names.get(fid, {})
        fname = info.get("name", fid)
        desc = info.get("description", "See full framework for details.")
        lines.append(f"### {fid}: {fname}")
        lines.append("")
        lines.append(f"**Tier:** {feat['tier']} ({tier_names[feat['tier']]})")
        lines.append(f"**Discriminative power:** {feat['discriminative_power']:.1f}")
        lines.append("")
        lines.append(f"{desc}")
        lines.append("")
        lines.append("| Score Range | Interpretation |")
        lines.append("|-------------|----------------|")
        lines.append("| 0-25 | Absent or minimal |")
        lines.append("| 26-50 | Partial or emerging |")
        lines.append("| 51-75 | Substantial |")
        lines.append("| 76-100 | Comprehensive or exemplary |")
        lines.append("")

    # How to compute composite
    lines.append("## Computing the Quick Assessment Composite")
    lines.append("")
    lines.append("1. Score each of the 25 features on the 0-100 scale using the rubrics above")
    lines.append("2. Compute the arithmetic mean of all 25 scores")
    lines.append("3. The result is the Quick Assessment composite (0-100 scale)")
    lines.append("")
    lines.append("**Formula:** `Quick_Composite = mean(F1, F2, ..., F25)`")
    lines.append("")
    lines.append("All features are equally weighted. If a feature cannot be scored (e.g., data unavailable), "
                 "exclude it and compute the mean of the remaining features.")
    lines.append("")

    # Comparison with full assessment
    lines.append("## Comparison with Full 157-Feature Assessment")
    lines.append("")
    lines.append(f"- **Pearson r:** {correlation:.3f}")
    lines.append(f"- **R-squared:** {r_squared:.1f}% of variance explained")
    lines.append(f"- **Spearman rho:** {spearman:.3f} (rank preservation)")
    lines.append("")
    lines.append("### Benchmark Rankings Comparison")
    lines.append("")
    lines.append("| Rank (Quick) | Benchmark | Quick Composite | Full Composite | Rank (Full) |")
    lines.append("|-------------|-----------|-----------------|----------------|-------------|")

    # Sort by quick composite descending
    scored = [b for b in benchmark_scores if b["quick_composite"] is not None and b["full_composite"] is not None]
    by_quick = sorted(scored, key=lambda x: x["quick_composite"], reverse=True)
    by_full = sorted(scored, key=lambda x: x["full_composite"], reverse=True)

    full_rank_map = {b["benchmark"]: i + 1 for i, b in enumerate(by_full)}
    for qi, b in enumerate(by_quick, 1):
        fr = full_rank_map.get(b["benchmark"], "?")
        lines.append(
            f"| {qi} | {b['benchmark']} | {b['quick_composite']:.1f} | "
            f"{b['full_composite']:.1f} | {fr} |"
        )
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("*Generated 2026-04-04 by `build_quick_assessment.py` from 54-benchmark feature matrix.*")
    lines.append("*Source: `20260404-extended-feature-matrix-v3.json` | Framework: `20260404-feature-framework-v2.md`*")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    print("=" * 70)
    print("Quick Assessment 25-Feature Subset Builder")
    print("=" * 70)

    # Load data
    print(f"\nLoading feature matrix: {MATRIX_PATH}")
    with open(MATRIX_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    matrix = data["matrix"]
    print(f"  Loaded {len(matrix)} benchmarks")

    # Load feature names from framework
    print(f"Loading feature framework: {FRAMEWORK_PATH}")
    feature_names = parse_feature_names(FRAMEWORK_PATH)
    print(f"  Parsed {len(feature_names)} feature definitions")

    # Extract all scores
    all_scores = extract_all_scores(matrix)
    print(f"  {len(all_scores)} features with score data")

    # Compute actual tier sizes
    actual_tier_sizes: dict[str, int] = defaultdict(int)
    for fid in all_scores:
        actual_tier_sizes[fid[0]] += 1
    print(f"  Tier sizes: {dict(sorted(actual_tier_sizes.items()))}")

    # Compute discriminative power
    print("\nComputing discriminative power...")
    power_data = compute_discriminative_power(all_scores)

    # Print top-5 per tier for diagnostics
    by_tier: dict[str, list[dict]] = defaultdict(list)
    for item in power_data:
        by_tier[item["tier"]].append(item)

    for tier in sorted(by_tier):
        ranked = sorted(
            by_tier[tier], key=lambda x: x["discriminative_power"], reverse=True
        )
        n_alloc = TIER_ALLOCATION.get(tier, 0)
        print(f"\n  Tier {tier} (selecting {n_alloc} of {len(ranked)}):")
        for item in ranked[:max(5, n_alloc)]:
            fname = feature_names.get(item["id"], {}).get("name", "?")
            marker = " *" if ranked.index(item) < n_alloc else ""
            print(
                f"    {item['id']:5s} {fname:45s} "
                f"disc={item['discriminative_power']:8.1f} "
                f"var={item['variance']:8.1f} "
                f"nn={item['non_null_rate']:.2f}{marker}"
            )

    # Select 25 features
    selected = select_features(power_data, TIER_ALLOCATION)
    selected_ids = {s["id"] for s in selected}
    print(f"\nSelected {len(selected)} features: {sorted(selected_ids)}")

    # Compute benchmark scores
    print("\nComputing benchmark quick composites...")
    benchmark_scores = compute_benchmark_scores(matrix, selected_ids, all_scores)

    # Compute correlations
    quick_vals = [
        b["quick_composite"]
        for b in benchmark_scores
        if b["quick_composite"] is not None and b["full_composite"] is not None
    ]
    full_vals = [
        b["full_composite"]
        for b in benchmark_scores
        if b["quick_composite"] is not None and b["full_composite"] is not None
    ]

    corr = pearson_r(quick_vals, full_vals)
    spearman = rank_correlation(quick_vals, full_vals)
    r_squared = corr ** 2 * 100

    print(f"\n  Pearson r:    {corr:.4f}")
    print(f"  R-squared:   {r_squared:.1f}%")
    print(f"  Spearman rho: {spearman:.4f}")

    # Prepare rubrics for JSON
    feature_list = []
    for feat in selected:
        fid = feat["id"]
        info = feature_names.get(fid, {})
        feature_list.append(
            {
                "id": fid,
                "name": info.get("name", fid),
                "tier": feat["tier"],
                "discriminative_power": feat["discriminative_power"],
                "variance": feat["variance"],
                "non_null_rate": feat["non_null_rate"],
                "mean_score": feat["mean"],
                "scoring_rubric": info.get(
                    "description", "See full framework for details."
                ),
            }
        )

    # Build JSON output
    output = {
        "version": "1.0",
        "date": "2026-04-04",
        "total_features": len(selected),
        "total_features_in_framework": len(all_scores),
        "selection_method": f"variance-based discriminative power across {len(matrix)} benchmarks",
        "tier_allocation": TIER_ALLOCATION,
        "actual_tier_sizes": dict(sorted(actual_tier_sizes.items())),
        "features": feature_list,
        "benchmark_scores": benchmark_scores,
        "correlation_with_full": round(corr, 4),
        "spearman_rank_correlation": round(spearman, 4),
        "variance_explained_pct": round(r_squared, 1),
        "estimated_scoring_time_minutes": 60,
    }

    # Write JSON
    print(f"\nWriting JSON: {OUT_JSON}")
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"  Written ({OUT_JSON.stat().st_size:,} bytes)")

    # Write markdown
    print(f"Writing markdown: {OUT_MD}")
    md_text = generate_markdown(
        selected,
        benchmark_scores,
        corr,
        spearman,
        r_squared,
        feature_names,
        dict(sorted(actual_tier_sizes.items())),
    )
    OUT_MD.write_text(md_text, encoding="utf-8")
    print(f"  Written ({OUT_MD.stat().st_size:,} bytes)")

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"  Features selected:  25 / {len(all_scores)}")
    print(f"  Benchmarks scored:  {len(benchmark_scores)}")
    print(f"  Pearson r:          {corr:.4f}")
    print(f"  R-squared:          {r_squared:.1f}%")
    print(f"  Spearman rho:       {spearman:.4f}")
    print(f"  Scoring time est:   ~60 minutes per benchmark")
    print(f"  Output JSON:        {OUT_JSON}")
    print(f"  Output MD:          {OUT_MD}")
    print("=" * 70)


if __name__ == "__main__":
    main()
