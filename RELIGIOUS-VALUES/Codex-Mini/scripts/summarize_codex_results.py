#!/usr/bin/env python3
from __future__ import annotations

import json
import statistics
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
RESULTS = BASE / "results"
TRADITIONS = ["islam", "christianity", "hinduism"]
MODEL = "gpt-codex-mini"


def load_trials() -> list[dict]:
    items = []
    for tradition in TRADITIONS:
        path = RESULTS / f"20260404-trial-{tradition}-{MODEL}.json"
        data = json.load(open(path, encoding="utf-8"))
        items.extend(data["results"])
    return items


def compute_length_stats(results: list[dict]) -> tuple[dict, dict]:
    by_type: dict[str, list[int]] = defaultdict(list)
    by_tradition_type: dict[str, list[int]] = defaultdict(list)
    for item in results:
        item_type = item["type"]
        norm_type = "values" if item_type == "values_paired" else item_type
        tradition = item["tradition"]
        resp_len = len(item.get("response", "") or "")
        by_type[norm_type].append(resp_len)
        by_tradition_type[f"{tradition}_{norm_type}"].append(resp_len)

    stats = {}
    for key, lengths in sorted(by_type.items()):
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


def gradient(type_stats: dict) -> dict:
    k = type_stats.get("knowledge", {}).get("mean", 0)
    r = type_stats.get("reasoning", {}).get("mean", 0)
    v = type_stats.get("values", {}).get("mean", 0)
    return {
        "hypothesis": "Knowledge < Reasoning < Values response length",
        "knowledge_mean": k,
        "reasoning_mean": r,
        "values_mean": v,
        "gradient_holds": k < r < v,
        "reasoning_to_knowledge_ratio": round(r / k, 2) if k else None,
        "values_to_knowledge_ratio": round(v / k, 2) if k else None,
        "values_to_reasoning_ratio": round(v / r, 2) if r else None,
    }


def bias_values_independence(results: list[dict]) -> dict:
    bias_vals = []
    values_vals = []
    grouped: dict[str, dict[str, list[int]]] = defaultdict(lambda: {"bias": [], "values": []})
    for item in results:
        tradition = item["tradition"]
        value = len(item.get("response", "") or "")
        if item["type"] == "bias":
            grouped[tradition]["bias"].append(value)
        elif item["type"] in {"values", "values_paired"}:
            if item["item_id"].startswith("values_") or item["type"] == "values_paired":
                grouped[tradition]["values"].append(value)
    for tradition in ["Islam", "Christianity", "Hinduism"]:
        for bias_len, values_len in zip(grouped[tradition]["bias"], grouped[tradition]["values"]):
            bias_vals.append(bias_len)
            values_vals.append(values_len)

    r = None
    if len(bias_vals) >= 3:
        std_b = statistics.stdev(bias_vals)
        std_v = statistics.stdev(values_vals)
        if std_b > 0 and std_v > 0:
            mean_b = statistics.mean(bias_vals)
            mean_v = statistics.mean(values_vals)
            cov = sum((b - mean_b) * (v - mean_v) for b, v in zip(bias_vals, values_vals)) / (len(bias_vals) - 1)
            r = round(cov / (std_b * std_v), 3)
    return {
        "hypothesis": "Bias avoidance and values reasoning are independent (r < 0.3)",
        "n_pairs": len(bias_vals),
        "bias_mean_length": round(statistics.mean(bias_vals), 1) if bias_vals else None,
        "values_mean_length": round(statistics.mean(values_vals), 1) if values_vals else None,
        "pearson_r": r,
        "constructs_independent": abs(r) < 0.3 if r is not None else None,
    }


def summarize_rubric() -> tuple[dict, list[dict]]:
    type_scores: dict[str, list[float]] = defaultdict(list)
    tradition_type_scores: dict[str, list[float]] = defaultdict(list)
    all_scores = []
    for tradition in TRADITIONS:
        path = RESULTS / f"20260404-trial-rubric-scores-{tradition}-{MODEL}.json"
        data = json.load(open(path, encoding="utf-8"))
        for score in data["scores"]:
            entry = {
                "item_id": score["item_id"],
                "tradition": data["tradition"],
                "type": score["type"],
                "raw_score": score["score"],
                "max_score": score["max_score"],
                "normalized": round(score["score"] / score["max_score"], 4) if score["max_score"] else None,
                "justification": score["justification"],
            }
            all_scores.append(entry)
            type_scores[score["type"]].append(entry["normalized"])
            tradition_type_scores[f"{data['tradition']}_{score['type']}"].append(entry["normalized"])

    type_summary = {
        key: {
            "n": len(vals),
            "mean_normalized": round(statistics.mean(vals), 4),
            "median_normalized": round(statistics.median(vals), 4),
        }
        for key, vals in sorted(type_scores.items())
    }
    tradition_type_summary = {
        key: {
            "n": len(vals),
            "mean_normalized": round(statistics.mean(vals), 4),
        }
        for key, vals in sorted(tradition_type_scores.items())
    }
    return {
        "generated": "2026-04-04",
        "model": MODEL,
        "scorer": "codex-gpt-mini",
        "total_items_scored": len(all_scores),
        "scoring_method": "Agent rubric scoring under Codex-Mini/ without SDK/API",
        "caveat": "Rubric scores are model-judged and should be treated as provisional.",
        "type_summary": type_summary,
        "tradition_type_summary": tradition_type_summary,
        "gradient_test": {
            "knowledge_mean_normalized": type_summary.get("knowledge", {}).get("mean_normalized"),
            "reasoning_mean_normalized": type_summary.get("reasoning", {}).get("mean_normalized"),
            "values_mean_normalized": type_summary.get("values", {}).get("mean_normalized"),
        },
        "bias_values_independence": {
            "bias_mean_normalized": type_summary.get("bias", {}).get("mean_normalized"),
            "values_paired_mean_normalized": type_summary.get("values_paired", {}).get("mean_normalized"),
        },
        "all_scores": all_scores,
    }, all_scores


def main() -> int:
    results = load_trials()
    type_stats, tradition_stats = compute_length_stats(results)
    scoring = {
        "generated": "2026-04-04",
        "model": MODEL,
        "total_items": len(results),
        "response_length_by_type": type_stats,
        "response_length_by_tradition_type": tradition_stats,
        "gradient_test": gradient(type_stats),
        "bias_values_independence": bias_values_independence(results),
    }
    with open(RESULTS / f"20260404-trial-scoring-results-{MODEL}.json", "w", encoding="utf-8") as f:
        json.dump(scoring, f, indent=2, ensure_ascii=False)

    rubric_summary, all_scores = summarize_rubric()
    with open(RESULTS / f"20260404-trial-rubric-summary-{MODEL}.json", "w", encoding="utf-8") as f:
        json.dump(rubric_summary, f, indent=2, ensure_ascii=False)

    t2 = json.load(open(RESULTS / f"20260404-t2-results-{MODEL}.json", encoding="utf-8"))
    comparison = {
        "generated": "2026-04-04",
        "title": "Codex GPT mini benchmark replication bundle",
        "model": MODEL,
        "total_items_per_model": len(results),
        "gradient_comparison": scoring["gradient_test"],
        "bias_values_independence": scoring["bias_values_independence"],
        "rubric_comparison": rubric_summary["type_summary"],
        "t2_arabic_mcq": t2["summary"],
        "all_scores_count": len(all_scores),
    }
    with open(RESULTS / "20260404-codex-gpt-mini-comparison.json", "w", encoding="utf-8") as f:
        json.dump(comparison, f, indent=2, ensure_ascii=False)

    print("Wrote Codex scoring summaries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
