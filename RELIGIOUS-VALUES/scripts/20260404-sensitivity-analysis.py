#!/usr/bin/env python3
"""
Sensitivity Analysis for the 3-Axis Religious Benchmark Scoring Framework.

Tests the robustness of the corrected RD/PE/CI composite scoring:
  1. Weight sensitivity sweep (all RD/PE/CI combos summing to 100%)
  2. Gate threshold sensitivity (RD gate from 15 to 50)
  3. Bootstrap confidence intervals (Dirichlet-weighted, 10,000 iterations)
  4. Feature leave-one-out (max rank displacement per feature)

Input:  data/20260404-religious-benchmark-feature-matrix-v2.json
Output: data/20260404-sensitivity-analysis.json
"""
from __future__ import annotations

import json
import sys
import functools
from collections import defaultdict
from datetime import date
from itertools import product
from pathlib import Path

import numpy as np
from scipy.stats import kendalltau

print = functools.partial(print, flush=True)

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
DATA_DIR = PROJECT_DIR / "data"

TODAY = date.today().strftime("%Y%m%d")
INPUT_FILE = DATA_DIR / "20260404-religious-benchmark-feature-matrix-v2.json"
OUTPUT_FILE = DATA_DIR / "20260404-sensitivity-analysis.json"

BASELINE_WEIGHTS = {"w_rd": 0.40, "w_pe": 0.35, "w_ci": 0.25}
BASELINE_RD_GATE = 30
TOP_K = 15

# --- Sub-feature weights used inside each axis (from build_religious_feature_matrix.py) ---

# RD sub-feature weights and max values
RD_SUBFEATURES = {
    "R1_count":          {"weight": 0.15, "normalize": lambda v: min(100, v * 20)},
    "R2_depth":          {"weight": 0.25, "normalize": lambda v: (v / 5) * 100},
    "R3_scriptural":     {"weight": 0.15, "normalize": lambda v: (v / 5) * 100},
    "R4_denominational": {"weight": 0.10, "normalize": lambda v: (v / 3) * 100},
    "R5_pluralism":      {"weight": 0.15, "normalize": lambda v: (v / 5) * 100},
    "R6_grounding":      {"weight": 0.20, "normalize": lambda v: (v / 5) * 100},
}

# PE sub-feature weights and normalization
PE_P3_MAP = {
    "GitHub": 90, "HuggingFace": 85, "GitLab": 80,
    "Kaggle": 75, "Archive": 70, "Website": 50,
    "Not available": 0,
}
PE_P9_MAP = {"Both": 90, "Open-only": 60, "Closed-only": 40, "Unknown": 30}
PE_P5_MAP = {
    "Open Source": 90, "Likely Open Source": 70, "CC": 90,
    "Restricted": 30, "Unspecified": 50,
}
PE_P4_MAP = {"Available": 80, "Unknown": 40}

def pe_p10_norm(lang_str: str) -> float:
    lang = (lang_str or "").lower()
    if "multilingual" in lang:
        return 90
    if "english" in lang and "," in lang:
        return 80
    if "english" in lang:
        return 70
    if "arabic" in lang:
        return 50
    if lang:
        return 40
    return 30

PE_SUBFEATURES = {
    "P7_implementability": {"weight": 0.30, "normalize": lambda e: e["P7_implementability"] * 10},
    "P3_data_availability": {"weight": 0.25, "normalize": lambda e: PE_P3_MAP.get(e["P3_data_availability"], 50)},
    "P9_model_compat":      {"weight": 0.15, "normalize": lambda e: PE_P9_MAP.get(e["P9_model_compat"], 30)},
    "P10_language":         {"weight": 0.10, "normalize": lambda e: pe_p10_norm(e.get("P10_language", ""))},
    "P5_license":           {"weight": 0.10, "normalize": lambda e: PE_P5_MAP.get(e["P5_license"], 50)},
    "P4_code_availability": {"weight": 0.10, "normalize": lambda e: PE_P4_MAP.get(e["P4_code_availability"], 40)},
}

# CI sub-feature weights and normalization
CI_TIER_MAP = {"Tier 1 (top conf)": 100, "Tier 2 (good conf/journal)": 60, "Tier 3 (other)": 30}

CI_SUBFEATURES = {
    "C1_citation_count":    {"weight": 0.35, "normalize": lambda e: min(100, e["C1_citation_count"] * 2)},
    "C2_citations_per_year":{"weight": 0.30, "normalize": lambda e: min(100, e["C2_citations_per_year"] * 10)},
    "C3_venue_tier":        {"weight": 0.25, "normalize": lambda e: CI_TIER_MAP.get(e["C3_venue_tier"], 30)},
    "C6_community":         {"weight": 0.10, "normalize": lambda e: 10 if e.get("C6_community") else 0},
}


# ---------------------------------------------------------------------------
# Recomputation helpers
# ---------------------------------------------------------------------------

def recompute_rd(entry: dict, exclude_feature: str | None = None) -> float:
    """Recompute RD_score from sub-features, optionally excluding one."""
    total_weight = 0.0
    total_score = 0.0
    for feat, spec in RD_SUBFEATURES.items():
        if feat == exclude_feature:
            continue
        val = entry[feat]
        norm = spec["normalize"](val)
        total_weight += spec["weight"]
        total_score += norm * spec["weight"]
    if total_weight == 0:
        return 0.0
    return round(total_score / total_weight * 1.0, 1)  # renormalize


def recompute_pe(entry: dict, exclude_feature: str | None = None) -> float:
    """Recompute PE_score from sub-features, optionally excluding one."""
    total_weight = 0.0
    total_score = 0.0
    for feat, spec in PE_SUBFEATURES.items():
        if feat == exclude_feature:
            continue
        norm = spec["normalize"](entry)
        total_weight += spec["weight"]
        total_score += norm * spec["weight"]
    if total_weight == 0:
        return 0.0
    return round(total_score / total_weight * 1.0, 1)


def recompute_ci(entry: dict, exclude_feature: str | None = None) -> float:
    """Recompute CI_score from sub-features, optionally excluding one."""
    total_weight = 0.0
    total_score = 0.0
    for feat, spec in CI_SUBFEATURES.items():
        if feat == exclude_feature:
            continue
        norm = spec["normalize"](entry)
        total_weight += spec["weight"]
        total_score += norm * spec["weight"]
    if total_weight == 0:
        return 0.0
    return round(total_score / total_weight * 1.0, 1)


def composite_score(rd: float, pe: float, ci: float,
                    w_rd: float, w_pe: float, w_ci: float) -> float:
    return rd * w_rd + pe * w_pe + ci * w_ci


def rank_entries(entries: list[dict], w_rd: float, w_pe: float, w_ci: float) -> list[int]:
    """Return entry ids ranked by composite score (descending)."""
    scored = []
    for e in entries:
        c = composite_score(e["RD_score"], e["PE_score"], e["CI_score"], w_rd, w_pe, w_ci)
        scored.append((c, e["id"]))
    scored.sort(key=lambda x: (-x[0], x[1]))
    return [s[1] for s in scored]


def kendall_tau_safe(r1: list[int], r2: list[int]) -> float:
    """Compute Kendall's tau between two rankings (lists of IDs in rank order)."""
    # Build rank maps
    if len(r1) != len(r2) or set(r1) != set(r2):
        common = sorted(set(r1) & set(r2))
        if len(common) < 3:
            return 0.0
        rank1 = {v: i for i, v in enumerate(r1) if v in common}
        rank2 = {v: i for i, v in enumerate(r2) if v in common}
        ids = sorted(common)
    else:
        rank1 = {v: i for i, v in enumerate(r1)}
        rank2 = {v: i for i, v in enumerate(r2)}
        ids = sorted(set(r1))

    vals1 = [rank1[i] for i in ids]
    vals2 = [rank2[i] for i in ids]
    tau, _ = kendalltau(vals1, vals2)
    if np.isnan(tau):
        return 0.0
    return float(tau)


# ---------------------------------------------------------------------------
# Analysis 1: Weight Sensitivity Sweep
# ---------------------------------------------------------------------------

def weight_sensitivity_sweep(gate_passers: list[dict]) -> dict:
    print("\n=== Analysis 1: Weight Sensitivity Sweep ===")

    # Baseline ranking
    baseline_rank = rank_entries(gate_passers, **BASELINE_WEIGHTS)
    baseline_top15 = set(baseline_rank[:TOP_K])

    # Generate all weight combinations
    combos = []
    for rd_pct in range(20, 61, 5):
        for pe_pct in range(15, 56, 5):
            ci_pct = 100 - rd_pct - pe_pct
            if 5 <= ci_pct <= 45:
                combos.append((rd_pct / 100, pe_pct / 100, ci_pct / 100))

    print(f"  Testing {len(combos)} weight combinations")

    # Track: for each benchmark, how many times in top 15
    top15_counts = defaultdict(int)
    rank_ranges = defaultdict(lambda: [999, 0])  # [min_rank, max_rank]
    tau_values = []

    for w_rd, w_pe, w_ci in combos:
        ranked = rank_entries(gate_passers, w_rd, w_pe, w_ci)
        top15_set = set(ranked[:TOP_K])

        for eid in top15_set:
            top15_counts[eid] += 1

        # Track rank range for all gate-passers
        for rank_idx, eid in enumerate(ranked):
            current_rank = rank_idx + 1
            if current_rank < rank_ranges[eid][0]:
                rank_ranges[eid][0] = current_rank
            if current_rank > rank_ranges[eid][1]:
                rank_ranges[eid][1] = current_rank

        tau = kendall_tau_safe(ranked, baseline_rank)
        tau_values.append(tau)

    n_combos = len(combos)
    id_to_title = {e["id"]: e["short_title"] for e in gate_passers}

    benchmark_robustness = []
    for e in gate_passers:
        eid = e["id"]
        pct = top15_counts.get(eid, 0) / n_combos
        rng = rank_ranges.get(eid, [0, 0])
        if pct >= 0.80:
            cat = "robust"
        elif pct >= 0.30:
            cat = "moderate"
        elif pct > 0:
            cat = "fragile"
        else:
            cat = "never_top15"
        benchmark_robustness.append({
            "id": eid,
            "short_title": id_to_title[eid],
            "pct_in_top15": round(pct, 4),
            "rank_range": rng,
            "category": cat,
        })

    benchmark_robustness.sort(key=lambda x: -x["pct_in_top15"])

    tau_arr = np.array(tau_values)
    tau_dist = {
        "mean": round(float(tau_arr.mean()), 4),
        "std": round(float(tau_arr.std()), 4),
        "min": round(float(tau_arr.min()), 4),
        "max": round(float(tau_arr.max()), 4),
        "median": round(float(np.median(tau_arr)), 4),
    }

    robust = [b for b in benchmark_robustness if b["category"] == "robust"]
    fragile = [b for b in benchmark_robustness if b["category"] == "fragile"]
    print(f"  Robust (>80% in Top 15): {len(robust)}")
    print(f"  Fragile (<30% in Top 15): {len(fragile)}")
    print(f"  Kendall tau: mean={tau_dist['mean']}, range=[{tau_dist['min']}, {tau_dist['max']}]")

    return {
        "combinations_tested": n_combos,
        "baseline_weights": BASELINE_WEIGHTS,
        "benchmark_robustness": benchmark_robustness,
        "kendall_tau_distribution": tau_dist,
    }


# ---------------------------------------------------------------------------
# Analysis 2: Gate Threshold Sensitivity
# ---------------------------------------------------------------------------

def gate_threshold_sensitivity(all_entries: list[dict]) -> dict:
    print("\n=== Analysis 2: Gate Threshold Sensitivity ===")

    # 8 void traditions at baseline gate=30
    VOID_TRADITIONS_AT_30 = {
        "Judaism", "Jainism", "Shinto", "Taoism",
        "Ubuntu Philosophy", "Indigenous Spirituality",
        "Baha'i", "Zoroastrianism",
    }

    thresholds = list(range(15, 51, 5))
    results = []

    for thresh in thresholds:
        # Recompute gate-passers: RD >= thresh AND data available
        passers = [
            e for e in all_entries
            if e["RD_score"] >= thresh and e.get("P3_data_availability", "Not available") != "Not available"
        ]

        traditions_repr = set()
        for e in passers:
            traditions_repr.add(e["D5_primary_tradition"])

        # Which of the 8 void traditions now have representation?
        void_gained = sorted(VOID_TRADITIONS_AT_30 & traditions_repr)

        # Tradition-level detail
        trad_counts = defaultdict(int)
        for e in passers:
            trad_counts[e["D5_primary_tradition"]] += 1

        results.append({
            "threshold": thresh,
            "gate_passers": len(passers),
            "traditions_represented": len(traditions_repr),
            "void_traditions_gained": void_gained,
            "tradition_detail": dict(sorted(trad_counts.items())),
        })

        void_str = ", ".join(void_gained) if void_gained else "none"
        print(f"  RD >= {thresh:2d}: {len(passers):3d} passers, "
              f"{len(traditions_repr):2d} traditions, void gained: {void_str}")

    return {
        "thresholds_tested": thresholds,
        "results": results,
    }


# ---------------------------------------------------------------------------
# Analysis 3: Bootstrap Confidence Intervals
# ---------------------------------------------------------------------------

def bootstrap_confidence_intervals(gate_passers: list[dict], n_iter: int = 10000,
                                   alpha: float = 20.0) -> dict:
    print(f"\n=== Analysis 3: Bootstrap CIs (n={n_iter}, alpha={alpha}) ===")

    rng = np.random.default_rng(seed=42)

    # Pre-extract axis scores
    ids = [e["id"] for e in gate_passers]
    rd_arr = np.array([e["RD_score"] for e in gate_passers])
    pe_arr = np.array([e["PE_score"] for e in gate_passers])
    ci_arr = np.array([e["CI_score"] for e in gate_passers])
    n = len(gate_passers)

    # Dirichlet centered on baseline weights with concentration alpha
    alpha_vec = np.array([
        BASELINE_WEIGHTS["w_rd"] * alpha,
        BASELINE_WEIGHTS["w_pe"] * alpha,
        BASELINE_WEIGHTS["w_ci"] * alpha,
    ])

    # Sample all weights at once: (n_iter, 3)
    weights_samples = rng.dirichlet(alpha_vec, size=n_iter)

    # Compute composite scores: (n_iter, n_entries)
    composites = (
        np.outer(weights_samples[:, 0], rd_arr) +
        np.outer(weights_samples[:, 1], pe_arr) +
        np.outer(weights_samples[:, 2], ci_arr)
    )

    # Compute ranks for each iteration: (n_iter, n_entries)
    # argsort descending -> rank
    ranks = np.zeros_like(composites, dtype=int)
    for i in range(n_iter):
        order = np.argsort(-composites[i])
        ranks[i, order] = np.arange(1, n + 1)

    # Statistics per benchmark
    id_to_title = {e["id"]: e["short_title"] for e in gate_passers}
    benchmark_cis = []

    for j in range(n):
        comp_j = composites[:, j]
        rank_j = ranks[:, j]

        ci_lower = float(np.percentile(comp_j, 2.5))
        ci_upper = float(np.percentile(comp_j, 97.5))
        comp_mean = float(comp_j.mean())
        prob_top15 = float((rank_j <= TOP_K).sum() / n_iter)

        rank_lower = int(np.percentile(rank_j, 2.5))
        rank_upper = int(np.percentile(rank_j, 97.5))
        rank_mean = float(rank_j.mean())

        benchmark_cis.append({
            "id": ids[j],
            "short_title": id_to_title[ids[j]],
            "composite_mean": round(comp_mean, 2),
            "composite_ci_lower": round(ci_lower, 2),
            "composite_ci_upper": round(ci_upper, 2),
            "composite_ci_width": round(ci_upper - ci_lower, 2),
            "rank_mean": round(rank_mean, 1),
            "rank_ci_lower": rank_lower,
            "rank_ci_upper": rank_upper,
            "prob_in_top15": round(prob_top15, 4),
        })

    benchmark_cis.sort(key=lambda x: -x["prob_in_top15"])

    # Summary: how many have prob_top15 > 0.95, > 0.50, etc
    certain = sum(1 for b in benchmark_cis if b["prob_in_top15"] >= 0.95)
    likely = sum(1 for b in benchmark_cis if 0.50 <= b["prob_in_top15"] < 0.95)
    contested = sum(1 for b in benchmark_cis if 0.05 < b["prob_in_top15"] < 0.50)
    never = sum(1 for b in benchmark_cis if b["prob_in_top15"] <= 0.05)

    # Average CI width
    avg_ci_width = np.mean([b["composite_ci_width"] for b in benchmark_cis])
    median_ci_width = np.median([b["composite_ci_width"] for b in benchmark_cis])

    # Weight sample statistics
    w_stats = {
        "RD_mean": round(float(weights_samples[:, 0].mean()), 4),
        "RD_std": round(float(weights_samples[:, 0].std()), 4),
        "PE_mean": round(float(weights_samples[:, 1].mean()), 4),
        "PE_std": round(float(weights_samples[:, 1].std()), 4),
        "CI_mean": round(float(weights_samples[:, 2].mean()), 4),
        "CI_std": round(float(weights_samples[:, 2].std()), 4),
    }

    print(f"  Certain (p>=0.95 in Top 15): {certain}")
    print(f"  Likely (0.50<=p<0.95): {likely}")
    print(f"  Contested (0.05<p<0.50): {contested}")
    print(f"  Never (p<=0.05): {never}")
    print(f"  Average CI width: {avg_ci_width:.2f} pts, median: {median_ci_width:.2f} pts")

    return {
        "n_iterations": n_iter,
        "concentration_alpha": alpha,
        "weight_sample_stats": w_stats,
        "summary": {
            "certain_top15": certain,
            "likely_top15": likely,
            "contested_top15": contested,
            "never_top15": never,
            "avg_composite_ci_width": round(float(avg_ci_width), 2),
            "median_composite_ci_width": round(float(median_ci_width), 2),
        },
        "benchmark_cis": benchmark_cis,
    }


# ---------------------------------------------------------------------------
# Analysis 4: Feature Leave-One-Out
# ---------------------------------------------------------------------------

def feature_leave_one_out(gate_passers: list[dict]) -> dict:
    print("\n=== Analysis 4: Feature Leave-One-Out ===")

    # Baseline ranking
    baseline_rank = rank_entries(gate_passers, **BASELINE_WEIGHTS)
    baseline_rank_map = {eid: rank + 1 for rank, eid in enumerate(baseline_rank)}

    # All features to test
    all_features = (
        list(RD_SUBFEATURES.keys()) +
        list(PE_SUBFEATURES.keys()) +
        list(CI_SUBFEATURES.keys())
    )

    results = []

    for feature in all_features:
        # Determine which axis this feature belongs to
        if feature in RD_SUBFEATURES:
            axis = "RD"
        elif feature in PE_SUBFEATURES:
            axis = "PE"
        else:
            axis = "CI"

        # Recompute axis scores with feature removed
        modified_entries = []
        for e in gate_passers:
            new_rd = recompute_rd(e, exclude_feature=feature if axis == "RD" else None)
            new_pe = recompute_pe(e, exclude_feature=feature if axis == "PE" else None)
            new_ci = recompute_ci(e, exclude_feature=feature if axis == "CI" else None)
            modified_entries.append({
                "id": e["id"],
                "RD_score": new_rd,
                "PE_score": new_pe,
                "CI_score": new_ci,
            })

        # Rank with baseline weights
        scored = []
        for me in modified_entries:
            c = composite_score(me["RD_score"], me["PE_score"], me["CI_score"],
                                BASELINE_WEIGHTS["w_rd"], BASELINE_WEIGHTS["w_pe"], BASELINE_WEIGHTS["w_ci"])
            scored.append((c, me["id"]))
        scored.sort(key=lambda x: (-x[0], x[1]))
        new_rank_map = {eid: rank + 1 for rank, (_, eid) in enumerate(scored)}
        new_rank_list = [s[1] for s in scored]
        new_top15 = set(new_rank_list[:TOP_K])
        baseline_top15 = set(baseline_rank[:TOP_K])

        # Max rank displacement
        max_disp = 0
        displacements = {}
        for eid in baseline_rank_map:
            old_r = baseline_rank_map[eid]
            new_r = new_rank_map.get(eid, len(gate_passers))
            disp = abs(new_r - old_r)
            if disp > max_disp:
                max_disp = disp
            if disp > 0:
                displacements[eid] = {"old_rank": old_r, "new_rank": new_r, "displacement": disp}

        tau = kendall_tau_safe(new_rank_list, baseline_rank)
        top15_changes = len(new_top15 ^ baseline_top15) // 2  # entries swapped in/out

        results.append({
            "feature_removed": feature,
            "axis": axis,
            "max_rank_displacement": max_disp,
            "kendall_tau": round(tau, 4),
            "top15_changes": top15_changes,
            "entries_displaced": len(displacements),
            "top_displacements": sorted(
                [{"id": k, **v} for k, v in displacements.items()],
                key=lambda x: -x["displacement"]
            )[:5],
        })

        print(f"  Remove {feature:25s}: max_disp={max_disp:2d}, tau={tau:.4f}, "
              f"top15_changes={top15_changes}")

    # Identify most influential
    results.sort(key=lambda x: -x["max_rank_displacement"])
    most_influential = results[0]["feature_removed"] if results else ""

    # Also sort by lowest tau (most disruptive)
    by_tau = sorted(results, key=lambda x: x["kendall_tau"])
    most_disruptive_tau = by_tau[0]["feature_removed"] if by_tau else ""

    return {
        "features_tested": all_features,
        "results": sorted(results, key=lambda x: -x["max_rank_displacement"]),
        "most_influential_by_displacement": most_influential,
        "most_influential_by_tau": most_disruptive_tau,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("SENSITIVITY ANALYSIS: Religious Benchmark 3-Axis Scoring Framework")
    print("=" * 70)

    if not INPUT_FILE.exists():
        print(f"ERROR: Input not found: {INPUT_FILE}")
        sys.exit(1)

    with open(INPUT_FILE) as f:
        data = json.load(f)

    all_entries = data["entries"]
    gate_passers = [e for e in all_entries if e.get("passes_gates")]
    gate_passers.sort(key=lambda x: -x["COMPOSITE"])

    print(f"Input: {INPUT_FILE.name}")
    print(f"Total entries: {len(all_entries)}")
    print(f"Gate passers (RD >= {BASELINE_RD_GATE}): {len(gate_passers)}")
    print(f"Composite spread: {gate_passers[-1]['COMPOSITE']:.1f} - {gate_passers[0]['COMPOSITE']:.1f} "
          f"= {gate_passers[0]['COMPOSITE'] - gate_passers[-1]['COMPOSITE']:.1f} pts")

    # Run all four analyses
    weight_results = weight_sensitivity_sweep(gate_passers)
    gate_results = gate_threshold_sensitivity(all_entries)
    bootstrap_results = bootstrap_confidence_intervals(gate_passers, n_iter=10000, alpha=20.0)
    loo_results = feature_leave_one_out(gate_passers)

    # Assemble output
    output = {
        "generated": TODAY,
        "input_matrix": "20260404-religious-benchmark-feature-matrix-v2.json",
        "baseline": {
            "weights": BASELINE_WEIGHTS,
            "rd_gate": BASELINE_RD_GATE,
            "gate_passers": len(gate_passers),
            "composite_spread": round(gate_passers[0]["COMPOSITE"] - gate_passers[-1]["COMPOSITE"], 1),
        },
        "weight_sensitivity": weight_results,
        "gate_threshold": gate_results,
        "bootstrap": bootstrap_results,
        "feature_loo": loo_results,
    }

    # Write output
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nOutput written to: {OUTPUT_FILE}")

    # -----------------------------------------------------------------------
    # Summary
    # -----------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    # Weight sweep summary
    robust = [b for b in weight_results["benchmark_robustness"] if b["category"] == "robust"]
    fragile = [b for b in weight_results["benchmark_robustness"] if b["category"] == "fragile"]
    print(f"\n1. WEIGHT SENSITIVITY ({weight_results['combinations_tested']} combos)")
    print(f"   Robust (>80% in Top 15): {len(robust)}")
    for b in robust[:10]:
        print(f"     id={b['id']:3d} ({b['pct_in_top15']*100:5.1f}%) ranks {b['rank_range']} | {b['short_title'][:50]}")
    print(f"   Fragile (<30%): {len(fragile)}")
    for b in fragile[:5]:
        print(f"     id={b['id']:3d} ({b['pct_in_top15']*100:5.1f}%) ranks {b['rank_range']} | {b['short_title'][:50]}")

    # Gate summary
    print(f"\n2. GATE THRESHOLD")
    for r in gate_results["results"]:
        marker = " <-- BASELINE" if r["threshold"] == 30 else ""
        void_str = ", ".join(r["void_traditions_gained"]) if r["void_traditions_gained"] else "none"
        print(f"   RD >= {r['threshold']:2d}: {r['gate_passers']:3d} passers, "
              f"void gained: {void_str}{marker}")

    # Bootstrap summary
    print(f"\n3. BOOTSTRAP (n={bootstrap_results['n_iterations']})")
    print(f"   Certain (p>=0.95): {bootstrap_results['summary']['certain_top15']}")
    print(f"   Likely (0.50<=p<0.95): {bootstrap_results['summary']['likely_top15']}")
    print(f"   Contested (0.05<p<0.50): {bootstrap_results['summary']['contested_top15']}")
    print(f"   Avg CI width: {bootstrap_results['summary']['avg_composite_ci_width']:.2f} pts")
    print(f"   Top 5 by prob_top15:")
    for b in bootstrap_results["benchmark_cis"][:5]:
        print(f"     id={b['id']:3d} p={b['prob_in_top15']:.3f} CI=[{b['composite_ci_lower']:.1f}, {b['composite_ci_upper']:.1f}] | {b['short_title'][:50]}")

    # LOO summary
    print(f"\n4. FEATURE LEAVE-ONE-OUT")
    print(f"   Most influential (displacement): {loo_results['most_influential_by_displacement']}")
    print(f"   Most influential (tau):          {loo_results['most_influential_by_tau']}")
    for r in loo_results["results"][:5]:
        print(f"     {r['feature_removed']:25s}: max_disp={r['max_rank_displacement']:2d}, tau={r['kendall_tau']:.4f}")

    # Overall verdict
    print(f"\n{'=' * 70}")
    print("VERDICT: Are rankings stable or noise?")
    print(f"{'=' * 70}")
    spread = gate_passers[0]["COMPOSITE"] - gate_passers[-1]["COMPOSITE"]
    avg_ci = bootstrap_results["summary"]["avg_composite_ci_width"]
    certain_n = bootstrap_results["summary"]["certain_top15"]
    contested_n = bootstrap_results["summary"]["contested_top15"]
    tau_mean = weight_results["kendall_tau_distribution"]["mean"]
    robust_n = len(robust)

    print(f"  Composite spread: {spread:.1f} pts")
    print(f"  Average bootstrap CI width: {avg_ci:.2f} pts")
    print(f"  CI/spread ratio: {avg_ci/spread*100:.1f}%")
    if avg_ci / spread > 0.5:
        print(f"  --> CIs cover >50% of total spread => RANKINGS ARE LARGELY NOISE")
    elif avg_ci / spread > 0.3:
        print(f"  --> CIs cover 30-50% of spread => TOP TIER STABLE, MIDDLE RANKINGS NOISY")
    else:
        print(f"  --> CIs cover <30% of spread => RANKINGS GENERALLY MEANINGFUL")

    print(f"  Certain Top-15 members: {certain_n} / {len(gate_passers)}")
    print(f"  Contested slots: {contested_n}")
    print(f"  Mean Kendall tau across weight combos: {tau_mean:.3f}")
    if tau_mean > 0.85:
        print(f"  --> High tau => ranking order is robust to weight perturbation")
    elif tau_mean > 0.65:
        print(f"  --> Moderate tau => overall order somewhat stable, boundary rankings shift")
    else:
        print(f"  --> Low tau => rankings are sensitive to weight choices")

    print(f"  Robust benchmarks: {robust_n} (in Top 15 across >80% of weight combos)")


if __name__ == "__main__":
    main()
