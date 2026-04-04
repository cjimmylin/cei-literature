#!/usr/bin/env python3
"""
Multi-Model Scoring for Construct Validity Trials — Religious Values Benchmark

Auto-discovers all trial result files (20260404-trial-{tradition}-{model}.json),
computes per-model scoring statistics, and generates a cross-model comparison.

Usage:
    python 20260404-score-trial-results-multimodel.py [--models opus,sonnet,haiku]

Output:
    data/20260404-trial-scoring-results-{model_slug}.json  (per model)
    data/20260404-cross-model-scoring-comparison.json       (comparative)
"""
from __future__ import annotations

import argparse
import json
import re
import statistics
from collections import defaultdict
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

TRADITIONS = ["islam", "christianity", "hinduism"]

# Canonical model slug mapping
MODEL_SLUGS = {
    "opus": "opus",
    "sonnet": "sonnet",
    "haiku": "haiku",
}


def discover_models() -> list[str]:
    """Auto-discover available model slugs from trial files."""
    models = set()
    for f in DATA_DIR.glob("20260404-trial-*-*.json"):
        name = f.stem  # e.g., "20260404-trial-islam-sonnet"
        parts = name.split("-")
        # parts: ['20260404', 'trial', '{tradition}', '{model}']
        if len(parts) >= 4 and parts[1] == "trial":
            model_slug = parts[-1]
            # Skip non-model slugs (tradition names, rubric/scoring files)
            skip = {"scores", "results", "summary", "comparison", "scoring",
                    "islam", "christianity", "hinduism"}
            if model_slug not in skip:
                models.add(model_slug)
    return sorted(models)


def load_trials(model_slug: str) -> list[dict]:
    """Load all tradition files for a given model."""
    results = []
    for tradition in TRADITIONS:
        fpath = DATA_DIR / f"20260404-trial-{tradition}-{model_slug}.json"
        if fpath.exists():
            data = json.load(open(fpath, encoding="utf-8"))
            for item in data.get("results", []):
                item["_tradition_file"] = tradition
                # Normalize type field: Opus files use "values" for paired items too
                # Sonnet/Haiku correctly use "values_paired"
                results.append(item)
    return results


def compute_length_stats(results: list[dict]) -> tuple[dict, dict]:
    """Compute response length statistics by type and tradition."""
    by_type: dict[str, list[int]] = defaultdict(list)
    by_tradition_type: dict[str, list[int]] = defaultdict(list)

    for item in results:
        item_type = item.get("type", "unknown")
        tradition = item.get("tradition", "unknown")
        resp_len = len(item.get("response", "") or "")

        # Normalize: treat "values_paired" as "values" for gradient analysis
        norm_type = "values" if item_type == "values_paired" else item_type

        by_type[norm_type].append(resp_len)
        by_tradition_type[f"{tradition}_{norm_type}"].append(resp_len)

        # Also keep original types for detailed breakdown
        by_type[f"_{item_type}_raw"].append(resp_len)

    stats = {}
    for key, lengths in sorted(by_type.items()):
        if key.startswith("_"):
            continue
        stats[key] = {
            "n": len(lengths),
            "mean": round(statistics.mean(lengths), 1),
            "median": round(statistics.median(lengths), 1),
            "stdev": round(statistics.stdev(lengths), 1) if len(lengths) > 1 else 0,
            "min": min(lengths),
            "max": max(lengths),
        }

    tradition_stats = {}
    for key, lengths in sorted(by_tradition_type.items()):
        tradition_stats[key] = {
            "n": len(lengths),
            "mean": round(statistics.mean(lengths), 1),
            "median": round(statistics.median(lengths), 1),
        }

    return stats, tradition_stats


def compute_gradient_test(type_stats: dict) -> dict:
    """Test the Knowledge < Reasoning < Values gradient hypothesis."""
    k_mean = type_stats.get("knowledge", {}).get("mean", 0)
    r_mean = type_stats.get("reasoning", {}).get("mean", 0)
    v_mean = type_stats.get("values", {}).get("mean", 0)

    gradient_holds = k_mean < r_mean < v_mean
    r_to_k = round(r_mean / k_mean, 2) if k_mean > 0 else None
    v_to_k = round(v_mean / k_mean, 2) if k_mean > 0 else None
    v_to_r = round(v_mean / r_mean, 2) if r_mean > 0 else None

    return {
        "hypothesis": "Knowledge < Reasoning < Values response length",
        "knowledge_mean": k_mean,
        "reasoning_mean": r_mean,
        "values_mean": v_mean,
        "gradient_holds": gradient_holds,
        "reasoning_to_knowledge_ratio": r_to_k,
        "values_to_knowledge_ratio": v_to_k,
        "values_to_reasoning_ratio": v_to_r,
    }


def compute_bias_values_independence(results: list[dict]) -> dict:
    """Test bias-values construct independence using response length as proxy."""
    bias_lengths: dict[str, int] = {}
    values_lengths: dict[str, int] = {}

    for item in results:
        item_id = item.get("item_id", "")
        resp_len = len(item.get("response", "") or "")
        tradition = item.get("tradition", "")
        item_type = item.get("type", "")

        if item_type == "bias" or item_id.startswith("bias_"):
            bias_lengths[f"{tradition}_{item_id}"] = resp_len
        elif item_type == "values_paired" or (
            item_type == "values" and item_id.startswith("values_")
        ):
            values_lengths[f"{tradition}_{item_id}"] = resp_len

    # Match pairs by tradition and order
    bias_vals = []
    values_vals = []
    for tradition in ["Islam", "Christianity", "Hinduism"]:
        t_bias = [v for k, v in sorted(bias_lengths.items()) if tradition in k]
        t_values = [v for k, v in sorted(values_lengths.items()) if tradition in k]
        for i in range(min(len(t_bias), len(t_values))):
            bias_vals.append(t_bias[i])
            values_vals.append(t_values[i])

    r = None
    if len(bias_vals) >= 3:
        n = len(bias_vals)
        mean_b = statistics.mean(bias_vals)
        mean_v = statistics.mean(values_vals)
        std_b = statistics.stdev(bias_vals)
        std_v = statistics.stdev(values_vals)
        if std_b > 0 and std_v > 0:
            cov = sum(
                (b - mean_b) * (v - mean_v) for b, v in zip(bias_vals, values_vals)
            ) / (n - 1)
            r = round(cov / (std_b * std_v), 3)

    return {
        "hypothesis": "Bias avoidance and values reasoning are independent (r < 0.3)",
        "n_pairs": len(bias_vals),
        "bias_mean_length": round(statistics.mean(bias_vals), 1) if bias_vals else None,
        "values_mean_length": (
            round(statistics.mean(values_vals), 1) if values_vals else None
        ),
        "pearson_r": r,
        "constructs_independent": abs(r) < 0.3 if r is not None else None,
    }


def score_single_model(model_slug: str) -> dict | None:
    """Score a single model and return the results dict."""
    results = load_trials(model_slug)
    if not results:
        print(f"  No trial files found for {model_slug}")
        return None

    print(f"\n{'='*60}")
    print(f"Model: {model_slug} ({len(results)} items)")
    print(f"{'='*60}")

    type_stats, tradition_stats = compute_length_stats(results)
    gradient = compute_gradient_test(type_stats)
    independence = compute_bias_values_independence(results)

    # Per-tradition gradients
    tradition_gradients = {}
    for tradition in ["Islam", "Christianity", "Hinduism"]:
        t_items = [r for r in results if r.get("tradition") == tradition]
        if t_items:
            t_type_stats, _ = compute_length_stats(t_items)
            tradition_gradients[tradition] = compute_gradient_test(t_type_stats)

    output = {
        "generated": "2026-04-04",
        "model": model_slug,
        "total_items": len(results),
        "response_length_by_type": type_stats,
        "response_length_by_tradition_type": tradition_stats,
        "gradient_test": gradient,
        "tradition_specific_gradients": tradition_gradients,
        "bias_values_independence": independence,
    }

    # Print summary
    k = type_stats.get("knowledge", {}).get("mean", 0)
    r = type_stats.get("reasoning", {}).get("mean", 0)
    v = type_stats.get("values", {}).get("mean", 0)
    holds = "YES" if gradient["gradient_holds"] else "NO"
    print(f"  Gradient K({k:.0f}) → R({r:.0f}) → V({v:.0f})  holds={holds}")
    print(f"  R/K={gradient['reasoning_to_knowledge_ratio']}x  V/K={gradient['values_to_knowledge_ratio']}x")
    print(f"  Bias-Values r={independence['pearson_r']}")

    for trad, tg in tradition_gradients.items():
        th = "✓" if tg["gradient_holds"] else "✗"
        print(f"    {trad}: K={tg['knowledge_mean']:.0f} R={tg['reasoning_mean']:.0f} V={tg['values_mean']:.0f} {th}")

    # Save per-model results
    out_path = DATA_DIR / f"20260404-trial-scoring-results-{model_slug}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"  → {out_path.name}")

    return output


def build_comparison(all_results: dict[str, dict]) -> dict:
    """Build cross-model comparison from individual model results."""
    models = sorted(all_results.keys())

    # Gradient comparison table
    gradient_table = []
    for m in models:
        g = all_results[m]["gradient_test"]
        gradient_table.append({
            "model": m,
            "knowledge_mean": g["knowledge_mean"],
            "reasoning_mean": g["reasoning_mean"],
            "values_mean": g["values_mean"],
            "gradient_holds": g["gradient_holds"],
            "v_to_k_ratio": g["values_to_knowledge_ratio"],
        })

    # Per-tradition gradient comparison
    tradition_comparison = {}
    for tradition in ["Islam", "Christianity", "Hinduism"]:
        tradition_comparison[tradition] = []
        for m in models:
            tg = all_results[m].get("tradition_specific_gradients", {}).get(tradition, {})
            tradition_comparison[tradition].append({
                "model": m,
                "knowledge_mean": tg.get("knowledge_mean", 0),
                "reasoning_mean": tg.get("reasoning_mean", 0),
                "values_mean": tg.get("values_mean", 0),
                "gradient_holds": tg.get("gradient_holds", False),
            })

    # Bias-values independence comparison
    independence_table = []
    for m in models:
        ind = all_results[m]["bias_values_independence"]
        independence_table.append({
            "model": m,
            "pearson_r": ind["pearson_r"],
            "constructs_independent": ind["constructs_independent"],
            "bias_mean_length": ind["bias_mean_length"],
            "values_mean_length": ind["values_mean_length"],
        })

    comparison = {
        "generated": "2026-04-04",
        "models_compared": models,
        "gradient_comparison": gradient_table,
        "tradition_gradient_comparison": tradition_comparison,
        "bias_values_independence_comparison": independence_table,
        "key_findings": [],
    }

    # Generate key findings
    all_hold = all(g["gradient_holds"] for g in gradient_table)
    comparison["key_findings"].append(
        f"K<R<V gradient holds for {'ALL' if all_hold else 'SOME'} models: "
        + ", ".join(f"{g['model']}={'YES' if g['gradient_holds'] else 'NO'}" for g in gradient_table)
    )

    # V/K ratio degradation
    vk_ratios = {g["model"]: g["v_to_k_ratio"] for g in gradient_table if g["v_to_k_ratio"]}
    if vk_ratios:
        comparison["key_findings"].append(
            "V/K ratios: " + ", ".join(f"{m}={r}x" for m, r in vk_ratios.items())
        )

    # Independence finding
    for ind in independence_table:
        r_val = ind["pearson_r"]
        if r_val is not None:
            status = "independent" if ind["constructs_independent"] else "correlated"
            comparison["key_findings"].append(
                f"Bias-values r={r_val} for {ind['model']} ({status})"
            )

    return comparison


def main():
    parser = argparse.ArgumentParser(
        description="Multi-model scoring for construct validity trials"
    )
    parser.add_argument(
        "--models",
        default=None,
        help="Comma-separated model slugs (default: auto-discover)",
    )
    args = parser.parse_args()

    if args.models:
        models = [m.strip() for m in args.models.split(",")]
    else:
        models = discover_models()

    print(f"Discovered models: {models}")

    all_results = {}
    for model in models:
        result = score_single_model(model)
        if result:
            all_results[model] = result

    if len(all_results) > 1:
        print(f"\n{'='*60}")
        print("Cross-Model Comparison")
        print(f"{'='*60}")

        comparison = build_comparison(all_results)

        out_path = DATA_DIR / "20260404-cross-model-scoring-comparison.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(comparison, f, indent=2, ensure_ascii=False)
        print(f"  → {out_path.name}")

        print("\nKey Findings:")
        for finding in comparison["key_findings"]:
            print(f"  • {finding}")

    print("\nDone.")


if __name__ == "__main__":
    main()
