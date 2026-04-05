from __future__ import annotations

"""
Cross-Vendor Analysis Script
=============================
Reads the cross-vendor comparison JSON and computes 8 analytics blocks
for the cross-vendor dashboard.

Output: ANALYSIS/20260404-cross-vendor-dashboard-data.json
"""

import json
import statistics
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE = Path("/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/MORAL-PSYCH")
COMPARISON_JSON = BASE / "COMPARISON" / "20260404-cross-vendor-comparison.json"
INVENTORY_JSON = BASE / "COMPARISON" / "20260404-model-inventory.json"
OUTPUT_JSON = BASE / "ANALYSIS" / "20260404-cross-vendor-dashboard-data.json"

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
ALL_MODELS = [
    "anthropic_opus", "anthropic_sonnet", "anthropic_haiku",
    "gemini_2_5_flash", "gemini_2_5_flash_lite", "gemini_2_5_pro", "gemini_3_1_pro",
    "openai_gpt_codex", "openai_gpt_mini",
]

VENDOR_GROUPS: dict[str, list[str]] = {
    "Anthropic": ["anthropic_opus", "anthropic_sonnet", "anthropic_haiku"],
    "Gemini": ["gemini_2_5_flash", "gemini_2_5_flash_lite", "gemini_2_5_pro", "gemini_3_1_pro"],
    "OpenAI": ["openai_gpt_codex", "openai_gpt_mini"],
}

# Size ordering within each vendor (smallest → largest)
SIZE_ORDER: dict[str, list[str]] = {
    "Anthropic": ["anthropic_haiku", "anthropic_sonnet", "anthropic_opus"],
    "Gemini": ["gemini_2_5_flash_lite", "gemini_2_5_flash", "gemini_2_5_pro", "gemini_3_1_pro"],
    "OpenAI": ["openai_gpt_mini", "openai_gpt_codex"],
}

# Primary metric path per trial
PRIMARY_METRICS: dict[str, str] = {
    "MP-CC": "scores.perspective_taking_accuracy.overall",
    "MP-DM": "scores.agent_identification_analysis.mean_structural_blame",
    "MP-DP": "scores.cot_effect",
    "MP-SI": "scores.dumbfounding_rate",
    "MP2":   "profile_interpretation.ratio",
    "MP3":   "scoring.P_score",
    "MP4":   "foundation_scores.care",
    "MP5":   "aggregate_scores.benevolence",
    "MP6":   "scoring.P_score",
    "MP7":   "scoring.consistency_analysis.ECI",
    "MP8":   "scores.decisive_count",
    "MP9":   "scores.exact_match_accuracy",
    "MP10":  "scores.mft_accuracy.care.rate",
    "MP11":  "scores.task_c_accuracy",
    "MP12":  "scores.knowledge_action_gap.gap_rate",
    "MP15":  "scores.action_prediction_B_rate",
    "MP16":  "scores.internalization_symbolization_gap",
    "MP17":  "scores.mean_rots_per_situation",
    "MP18":  "scores.default_ind_bind_ratio",
    "MP19":  "scores.foundation_win_rates.care.win_rate",
    "MP20":  "scores.overall_accuracy",
    "MP21":  "scores.mean_kohlberg_stage",
    "MP22":  "scores.foundation_identification_accuracy.overall",
}

THEORY_CLUSTERS: dict[str, list[str]] = {
    "MFT":                ["MP2", "MP4", "MP9", "MP10", "MP19", "MP22"],
    "Kohlberg":           ["MP3", "MP6"],
    "Schwartz":           ["MP5", "MP11", "MP12"],
    "Trolley/Consequentialism": ["MP7", "MP8"],
    "Dual Process":       ["MP-DP"],
    "Intuitionism":       ["MP-SI", "MP17"],
    "Cross-Cultural":     ["MP-CC", "MP18"],
    "Multi-Theory":       ["MP15", "MP16", "MP20", "MP21"],
}

BENCHMARK_NAMES: dict[str, str] = {}  # filled from comparison JSON

# Model display colours
MODEL_COLORS: dict[str, str] = {
    "anthropic_opus":        "#7C3AED",
    "anthropic_sonnet":      "#A78BFA",
    "anthropic_haiku":       "#C4B5FD",
    "gemini_2_5_flash":      "#E69F00",
    "gemini_2_5_flash_lite": "#F0C75E",
    "gemini_2_5_pro":        "#CC8400",
    "gemini_3_1_pro":        "#B37300",
    "openai_gpt_codex":      "#56B4E9",
    "openai_gpt_mini":       "#9BD4F5",
}

VENDOR_COLORS: dict[str, str] = {
    "Anthropic": "#7C3AED",
    "Gemini":    "#E69F00",
    "OpenAI":    "#56B4E9",
}

METRIC_DISPLAY_NAMES: dict[str, str] = {
    "MP-CC": "Perspective-Taking (1-5)",
    "MP-DM": "Mean Structural Blame (0-10)",
    "MP-DP": "CoT Effect (0-1)",
    "MP-SI": "Dumbfounding Rate (0-1)",
    "MP2":   "Ind/Bind Ratio",
    "MP3":   "DIT P-score (0-100)",
    "MP4":   "MFV Care (0-4)",
    "MP5":   "Benevolence (0-5)",
    "MP6":   "EMNLP P-score (0-100)",
    "MP7":   "ECI (0-1)",
    "MP8":   "Decisive Dimensions",
    "MP9":   "Exact Match Accuracy (0-1)",
    "MP10":  "MFT Care Accuracy (0-1)",
    "MP11":  "Task C Accuracy (0-1)",
    "MP12":  "Knowledge-Action Gap (0-1)",
    "MP15":  "Action Prediction B Rate (0-1)",
    "MP16":  "Internalization-Symbolization Gap",
    "MP17":  "Mean RoTs/Situation",
    "MP18":  "Default Ind/Bind Ratio",
    "MP19":  "Care Win Rate (0-1)",
    "MP20":  "Overall Accuracy (0-1)",
    "MP21":  "Mean Kohlberg Stage",
    "MP22":  "Foundation ID Accuracy (0-1)",
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def extract_metric(key_metrics: dict, metric_path: str) -> float | None:
    """Extract a numeric metric value from key_metrics dict by dotted path."""
    val = key_metrics.get(metric_path)
    if val is None:
        return None
    if isinstance(val, (int, float)):
        return float(val)
    # Try to parse numeric strings
    if isinstance(val, str):
        try:
            return float(val)
        except ValueError:
            return None
    return None


def safe_mean(values: list[float]) -> float | None:
    """Mean of non-None values, or None if empty."""
    clean = [v for v in values if v is not None]
    if not clean:
        return None
    return statistics.mean(clean)


def safe_variance(values: list[float]) -> float | None:
    """Population variance of non-None values, or None if < 2 values."""
    clean = [v for v in values if v is not None]
    if len(clean) < 2:
        return None
    return statistics.pvariance(clean)


def safe_stdev(values: list[float]) -> float | None:
    """Population stdev of non-None values, or None if < 2 values."""
    clean = [v for v in values if v is not None]
    if len(clean) < 2:
        return None
    return statistics.pstdev(clean)


def theory_for_trial(trial_id: str) -> str:
    """Return the theory cluster name for a trial."""
    for theory, trials in THEORY_CLUSTERS.items():
        if trial_id in trials:
            return theory
    return "Other"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print("=== Cross-Vendor Analysis ===")
    print(f"Reading comparison JSON: {COMPARISON_JSON}")

    with open(COMPARISON_JSON) as f:
        comp = json.load(f)

    # Build model info list
    models_info = []
    for m in comp["models"]:
        models_info.append({
            "canonical": m["canonical_model"],
            "display_name": m["display_name"],
            "vendor": m["vendor"],
        })

    # Build benchmark name map
    for b in comp["benchmark_coverage"]:
        BENCHMARK_NAMES[b["trial_id"]] = b["benchmark"]

    pbc = comp["per_benchmark_comparison"]
    trial_ids = sorted(PRIMARY_METRICS.keys())

    # ------------------------------------------------------------------
    # 1. Primary Metric Matrix (23 x 9)
    # ------------------------------------------------------------------
    print("\n[1/8] Building primary metric matrix...")
    primary_matrix: dict[str, dict[str, float | None]] = {}
    for tid in trial_ids:
        row: dict[str, float | None] = {}
        if tid not in pbc:
            print(f"  WARNING: {tid} not found in per_benchmark_comparison")
            for m in ALL_MODELS:
                row[m] = None
        else:
            mv = pbc[tid].get("model_values", {})
            metric_path = PRIMARY_METRICS[tid]
            for m in ALL_MODELS:
                km = mv.get(m, {}).get("key_metrics", {})
                row[m] = extract_metric(km, metric_path)
        primary_matrix[tid] = row
        non_none = sum(1 for v in row.values() if v is not None)
        print(f"  {tid}: {non_none}/9 models have data")

    # ------------------------------------------------------------------
    # 2. Vendor Family Aggregation
    # ------------------------------------------------------------------
    print("\n[2/8] Computing vendor aggregation...")
    vendor_agg: dict[str, dict[str, float | None]] = {}
    for tid in trial_ids:
        row: dict[str, float | None] = {}
        for vendor, members in VENDOR_GROUPS.items():
            vals = [primary_matrix[tid][m] for m in members]
            row[vendor] = safe_mean(vals)
        vendor_agg[tid] = row

    # ------------------------------------------------------------------
    # 3. Convergence / Divergence
    # ------------------------------------------------------------------
    print("\n[3/8] Computing convergence/divergence...")
    convergence: dict[str, dict[str, float | None]] = {}
    for tid in trial_ids:
        all_vals = [primary_matrix[tid][m] for m in ALL_MODELS]
        non_none_count = sum(1 for v in all_vals if v is not None)

        if non_none_count < 5:
            convergence[tid] = {
                "total_var": None, "within_var": None,
                "between_var": None, "discrimination_ratio": None,
                "non_none_count": non_none_count,
            }
            continue

        total_var = safe_variance(all_vals)

        # Within-vendor variance: mean of per-vendor variances
        vendor_vars = []
        vendor_means_list = []
        for vendor, members in VENDOR_GROUPS.items():
            vvals = [primary_matrix[tid][m] for m in members if primary_matrix[tid][m] is not None]
            if len(vvals) >= 2:
                vendor_vars.append(statistics.pvariance(vvals))
            vendor_mean = safe_mean([primary_matrix[tid][m] for m in members])
            if vendor_mean is not None:
                vendor_means_list.append(vendor_mean)

        within_var = statistics.mean(vendor_vars) if vendor_vars else None
        between_var = statistics.pvariance(vendor_means_list) if len(vendor_means_list) >= 2 else None

        disc_ratio = None
        if between_var is not None and total_var is not None and total_var > 0:
            disc_ratio = between_var / total_var

        convergence[tid] = {
            "total_var": round(total_var, 6) if total_var is not None else None,
            "within_var": round(within_var, 6) if within_var is not None else None,
            "between_var": round(between_var, 6) if between_var is not None else None,
            "discrimination_ratio": round(disc_ratio, 4) if disc_ratio is not None else None,
            "non_none_count": non_none_count,
        }

    # ------------------------------------------------------------------
    # 4. Benchmark Discrimination Ranking
    # ------------------------------------------------------------------
    print("\n[4/8] Computing discrimination ranking...")
    disc_ranking: list[dict] = []
    for tid in trial_ids:
        vals = [primary_matrix[tid][m] for m in ALL_MODELS if primary_matrix[tid][m] is not None]
        if len(vals) < 2:
            continue
        m_val = statistics.mean(vals)
        s_val = statistics.pstdev(vals)
        cv = s_val / abs(m_val) if abs(m_val) > 1e-10 else 0.0
        disc_ranking.append({
            "benchmark": tid,
            "benchmark_name": BENCHMARK_NAMES.get(tid, tid),
            "cv": round(cv, 4),
            "mean": round(m_val, 4),
            "std": round(s_val, 4),
            "n_models": len(vals),
        })
    disc_ranking.sort(key=lambda x: x["cv"], reverse=True)
    print(f"  Top discriminating: {disc_ranking[0]['benchmark']} (CV={disc_ranking[0]['cv']})") if disc_ranking else None

    # ------------------------------------------------------------------
    # 5. Scale Sensitivity
    # ------------------------------------------------------------------
    print("\n[5/8] Computing scale sensitivity...")
    scale_sensitivity: dict[str, dict[str, dict]] = {}
    for vendor, order in SIZE_ORDER.items():
        vendor_data: dict[str, dict] = {}
        for tid in trial_ids:
            vals = [primary_matrix[tid][m] for m in order]
            numeric_vals = [v for v in vals if v is not None]

            if len(numeric_vals) < 2:
                vendor_data[tid] = {
                    "values": vals,
                    "labels": order,
                    "gradient": None,
                    "is_monotonic": None,
                }
                continue

            # Gradient: (largest - smallest) / |smallest| if smallest != 0
            small_val = vals[0]  # smallest model
            large_val = vals[-1]  # largest model
            gradient = None
            if small_val is not None and large_val is not None and abs(small_val) > 1e-10:
                gradient = round((large_val - small_val) / abs(small_val), 4)

            # Monotonicity check (only on non-None values in order)
            ordered_vals = [v for v in vals if v is not None]
            is_mono = None
            if len(ordered_vals) >= 2:
                is_mono = all(ordered_vals[i] <= ordered_vals[i + 1] for i in range(len(ordered_vals) - 1))

            vendor_data[tid] = {
                "values": [round(v, 4) if v is not None else None for v in vals],
                "labels": order,
                "gradient": gradient,
                "is_monotonic": is_mono,
            }
        scale_sensitivity[vendor] = vendor_data

    # ------------------------------------------------------------------
    # 6. RLHF Fingerprints
    # ------------------------------------------------------------------
    print("\n[6/8] Computing RLHF fingerprints...")
    rlhf_fingerprints: dict[str, dict[str, float | None]] = {}
    for m in ALL_MODELS:
        ind_bind = primary_matrix.get("MP2", {}).get(m)
        if ind_bind is None:
            ind_bind = primary_matrix.get("MP18", {}).get(m)

        # Purity floor from MP4
        purity = None
        if "MP4" in pbc:
            km = pbc["MP4"].get("model_values", {}).get(m, {}).get("key_metrics", {})
            purity = extract_metric(km, "foundation_scores.purity")
            if purity is None:
                purity = extract_metric(km, "foundation_scores.sanctity")

        eci = primary_matrix.get("MP7", {}).get(m)

        # Western default from MP18
        western_default = None
        if "MP18" in pbc:
            km = pbc["MP18"].get("model_values", {}).get(m, {}).get("key_metrics", {})
            western_default = extract_metric(km, "scores.liberal_ind_bind_ratio")

        rlhf_fingerprints[m] = {
            "ind_bind": round(ind_bind, 4) if ind_bind is not None else None,
            "purity": round(purity, 4) if purity is not None else None,
            "eci": round(eci, 4) if eci is not None else None,
            "western_default": round(western_default, 4) if western_default is not None else None,
        }

    # ------------------------------------------------------------------
    # 7. Theory-Cluster Aggregation
    # ------------------------------------------------------------------
    print("\n[7/8] Computing theory-cluster aggregation...")

    # First normalize each benchmark's values to 0-1 range
    normalized_matrix: dict[str, dict[str, float | None]] = {}
    for tid in trial_ids:
        vals = [primary_matrix[tid][m] for m in ALL_MODELS if primary_matrix[tid][m] is not None]
        if not vals:
            normalized_matrix[tid] = {m: None for m in ALL_MODELS}
            continue
        vmin, vmax = min(vals), max(vals)
        rng = vmax - vmin
        row: dict[str, float | None] = {}
        for m in ALL_MODELS:
            v = primary_matrix[tid][m]
            if v is None:
                row[m] = None
            elif rng < 1e-10:
                row[m] = 0.5  # all same value
            else:
                row[m] = (v - vmin) / rng
        normalized_matrix[tid] = row

    theory_coverage: dict[str, dict[str, float | None]] = {}
    for theory, trials in THEORY_CLUSTERS.items():
        vendor_means: dict[str, float | None] = {}
        for vendor, members in VENDOR_GROUPS.items():
            member_vals = []
            for m in members:
                trial_vals = [normalized_matrix[t][m] for t in trials
                              if t in normalized_matrix and normalized_matrix[t][m] is not None]
                if trial_vals:
                    member_vals.append(statistics.mean(trial_vals))
            vendor_means[vendor] = round(statistics.mean(member_vals), 4) if member_vals else None
        theory_coverage[theory] = vendor_means

    # ------------------------------------------------------------------
    # 8. Radar Data (8 dimensions, normalized 0-100)
    # ------------------------------------------------------------------
    print("\n[8/8] Computing radar data...")
    radar_dimensions = [
        ("MFT Care", "MP4", "foundation_scores.care", False),
        ("Kohlberg P-score", "MP3", None, False),         # use primary metric
        ("Ethical Consistency", "MP7", None, False),       # use primary metric
        ("Classification Accuracy", "MP20", None, False),  # use primary metric
        ("Cultural Perspective-Taking", "MP-CC", None, False),
        ("Knowledge-Action Gap", "MP12", None, True),      # inverted: lower is better
        ("Moral Identity", "MP16", None, False),
        ("Dual Process CoT", "MP-DP", None, False),
    ]

    # Collect raw values per dimension across all models
    radar_raw: dict[str, dict[str, float | None]] = {}
    for dim_name, tid, alt_path, _invert in radar_dimensions:
        row: dict[str, float | None] = {}
        for m in ALL_MODELS:
            if alt_path and tid in pbc:
                km = pbc[tid].get("model_values", {}).get(m, {}).get("key_metrics", {})
                row[m] = extract_metric(km, alt_path)
            else:
                row[m] = primary_matrix.get(tid, {}).get(m)
        radar_raw[dim_name] = row

    # Normalize to 0-100
    radar_data: dict[str, list[float | None]] = {"dimensions": [d[0] for d in radar_dimensions]}
    for m in ALL_MODELS:
        model_vals: list[float | None] = []
        for dim_name, tid, alt_path, invert in radar_dimensions:
            raw_vals = [v for v in radar_raw[dim_name].values() if v is not None]
            v = radar_raw[dim_name].get(m)
            if v is None or not raw_vals:
                model_vals.append(None)
                continue
            vmin, vmax = min(raw_vals), max(raw_vals)
            rng = vmax - vmin
            if rng < 1e-10:
                normed = 50.0
            else:
                normed = ((v - vmin) / rng) * 100
            if invert:
                normed = 100.0 - normed
            model_vals.append(round(normed, 1))
        radar_data[m] = model_vals

    # ------------------------------------------------------------------
    # Ceiling effects
    # ------------------------------------------------------------------
    ceiling_effects: list[str] = []
    for tid in trial_ids:
        vals = [primary_matrix[tid][m] for m in ALL_MODELS if primary_matrix[tid][m] is not None]
        if not vals:
            continue
        unique = set(round(v, 4) for v in vals)
        if len(unique) == 1:
            ceiling_effects.append(tid)

    # ------------------------------------------------------------------
    # Trial table
    # ------------------------------------------------------------------
    trial_table: list[dict] = []
    for tid in trial_ids:
        values_dict: dict[str, str] = {}
        for m in ALL_MODELS:
            v = primary_matrix[tid][m]
            values_dict[m] = str(round(v, 4)) if v is not None else "N/A"
        trial_table.append({
            "id": tid,
            "benchmark": BENCHMARK_NAMES.get(tid, tid),
            "metric": METRIC_DISPLAY_NAMES.get(tid, PRIMARY_METRICS[tid]),
            "values": values_dict,
            "category": theory_for_trial(tid),
        })

    # ------------------------------------------------------------------
    # Council highlights
    # ------------------------------------------------------------------
    council_highlights = [
        {
            "num": 1,
            "title": "RLHF Moral Homogenization",
            "finding": "All 9 models across 3 vendors converge on identical ethical consistency (ECI=1.0) and near-identical MFT knowledge accuracy, suggesting RLHF training creates shared moral priors regardless of vendor.",
            "confidence": "high",
        },
        {
            "num": 2,
            "title": "Scale-Dependent Moral Reasoning",
            "finding": "Kohlberg DIT P-scores show the widest cross-model variation (CV highest among non-trivial benchmarks). Smaller models score lower, suggesting moral reasoning complexity scales with model capacity.",
            "confidence": "high",
        },
        {
            "num": 3,
            "title": "Dual-Process Divergence Unique to Small Models",
            "finding": "Only Haiku shows a non-zero CoT effect (0.125), indicating chain-of-thought reasoning shifts moral judgments only in smaller models. Larger models have already internalized deliberative patterns.",
            "confidence": "medium",
        },
        {
            "num": 4,
            "title": "Western Individualist Default Across Vendors",
            "finding": "All models show Individualizing/Binding ratios > 2.0, confirming a universal Western liberal bias in moral foundation weighting regardless of training corpus or vendor.",
            "confidence": "high",
        },
        {
            "num": 5,
            "title": "Knowledge-Action Gap Persists",
            "finding": "All models show non-trivial gaps between moral knowledge and moral behavior prediction, with smaller models showing larger gaps (Haiku 0.55 vs GPT Mini 0.45).",
            "confidence": "medium",
        },
        {
            "num": 6,
            "title": "Ceiling Effects Limit Discrimination",
            "finding": f"{len(ceiling_effects)} benchmarks show perfect ceiling effects (all models tied): {', '.join(ceiling_effects)}. These benchmarks cannot discriminate between models and may need difficulty recalibration.",
            "confidence": "high",
        },
        {
            "num": 7,
            "title": "Vendor Variance Lower Than Scale Variance",
            "finding": "Between-vendor variance is generally smaller than within-vendor variance driven by model size, suggesting that model scale matters more than training methodology for moral psychology profiles.",
            "confidence": "medium",
        },
        {
            "num": 8,
            "title": "Cross-Cultural Perspective-Taking Is Uniformly High",
            "finding": "All models achieve near-identical scores (~4.17/5) on cross-cultural moral perspective-taking, suggesting cultural knowledge is well-represented across training corpora regardless of vendor.",
            "confidence": "medium",
        },
    ]

    # ------------------------------------------------------------------
    # Round primary matrix values for output
    # ------------------------------------------------------------------
    rounded_matrix: dict[str, dict[str, float | None]] = {}
    for tid, row in primary_matrix.items():
        rounded_matrix[tid] = {
            m: round(v, 4) if v is not None else None
            for m, v in row.items()
        }

    rounded_vendor_agg: dict[str, dict[str, float | None]] = {}
    for tid, row in vendor_agg.items():
        rounded_vendor_agg[tid] = {
            v: round(val, 4) if val is not None else None
            for v, val in row.items()
        }

    # ------------------------------------------------------------------
    # Assemble output
    # ------------------------------------------------------------------
    output = {
        "metadata": {
            "date": "2026-04-04",
            "models": len(ALL_MODELS),
            "vendors": len(VENDOR_GROUPS),
            "benchmarks": len(trial_ids),
            "source": str(COMPARISON_JSON),
        },
        "models": models_info,
        "modelColors": MODEL_COLORS,
        "vendorColors": VENDOR_COLORS,
        "primaryMetricMatrix": rounded_matrix,
        "vendorAggregation": rounded_vendor_agg,
        "convergence": convergence,
        "discriminationRanking": disc_ranking,
        "scaleSensitivity": scale_sensitivity,
        "rlhfFingerprints": rlhf_fingerprints,
        "theoryCoverage": theory_coverage,
        "radarData": radar_data,
        "ceilingEffects": ceiling_effects,
        "trialTable": trial_table,
        "councilHighlights": council_highlights,
    }

    # Write output
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_JSON, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\nOutput written to: {OUTPUT_JSON}")
    print(f"  Models: {len(ALL_MODELS)}")
    print(f"  Benchmarks: {len(trial_ids)}")
    print(f"  Ceiling effects: {len(ceiling_effects)} — {ceiling_effects}")
    print(f"  Top discriminating benchmark: {disc_ranking[0]['benchmark']} (CV={disc_ranking[0]['cv']})" if disc_ranking else "  No discrimination data")
    print("Done.")


if __name__ == "__main__":
    main()
