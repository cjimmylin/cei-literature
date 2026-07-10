#!/usr/bin/env python3
"""Score MFQ-30 trial results and compare against human baselines."""
from __future__ import annotations

import json
import sys
from pathlib import Path

FOUNDATIONS = ["care", "fairness", "loyalty", "authority", "purity"]

# Human baselines from moralfoundations.org (US liberal/conservative means)
# Source: Graham, Haidt, & Nosek (2009), Table 2
HUMAN_BASELINES = {
    "us_liberal": {"care": 3.77, "fairness": 3.93, "loyalty": 2.15, "authority": 2.29, "purity": 1.47},
    "us_conservative": {"care": 3.30, "fairness": 3.10, "loyalty": 3.14, "authority": 3.38, "purity": 2.89},
    "us_overall": {"care": 3.54, "fairness": 3.52, "loyalty": 2.65, "authority": 2.84, "purity": 2.18},
}

# Abdulhai et al. (2024) LLM baselines (Table 1, approximate means from 50 administrations)
LLM_BASELINES = {
    "gpt4_default": {"care": 4.13, "fairness": 4.20, "loyalty": 2.53, "authority": 2.70, "purity": 1.80},
    "claude2_default": {"care": 3.90, "fairness": 4.10, "loyalty": 2.30, "authority": 2.50, "purity": 1.40},
}


def score_trial(trial_path: str) -> dict:
    with open(trial_path) as f:
        trial = json.load(f)

    # Collect responses by foundation
    by_foundation: dict[str, list[int]] = {f: [] for f in FOUNDATIONS}
    by_foundation["filler"] = []

    for part_key in ("part1_relevance", "part2_judgments"):
        items = trial[part_key]["items"]
        for item_id, item in items.items():
            foundation = item["foundation"]
            if foundation in by_foundation:
                by_foundation[foundation].append(item["response"])

    # Compute means
    scores = {}
    for f in FOUNDATIONS:
        vals = by_foundation[f]
        scores[f] = round(sum(vals) / len(vals), 2) if vals else 0

    # Individualizing vs binding
    ind = round((scores["care"] + scores["fairness"]) / 2, 2)
    bind = round((scores["loyalty"] + scores["authority"] + scores["purity"]) / 3, 2)

    print(f"\n{'='*60}")
    print(f"MFQ-30 Scoring: {trial.get('model', 'unknown')}")
    print(f"{'='*60}")
    print(f"\nFoundation Scores (0-5 scale):")
    print(f"{'Foundation':<15} {'Score':>6}  {'US Liberal':>10}  {'US Conserv':>10}  {'US Overall':>10}")
    print(f"{'-'*55}")
    for f in FOUNDATIONS:
        print(f"  {f.capitalize():<13} {scores[f]:>6.2f}  "
              f"{HUMAN_BASELINES['us_liberal'][f]:>10.2f}  "
              f"{HUMAN_BASELINES['us_conservative'][f]:>10.2f}  "
              f"{HUMAN_BASELINES['us_overall'][f]:>10.2f}")

    print(f"\nAggregate:")
    print(f"  Individualizing (Care+Fairness)/2:  {ind:.2f}")
    print(f"  Binding (Loy+Auth+Pur)/3:           {bind:.2f}")
    print(f"  Ind/Bind ratio:                     {ind/bind:.2f}" if bind > 0 else "  Ind/Bind ratio: inf")

    print(f"\nComparison with LLM baselines (Abdulhai et al. 2024):")
    for model_name, baseline in LLM_BASELINES.items():
        diffs = {f: round(scores[f] - baseline[f], 2) for f in FOUNDATIONS}
        print(f"  vs {model_name}: {diffs}")

    return {"scores": scores, "individualizing": ind, "binding": bind}


if __name__ == "__main__":
    trial_file = sys.argv[1] if len(sys.argv) > 1 else str(
        Path(__file__).parent / "20260404-trial-MP2-mfq30-opus.json"
    )
    score_trial(trial_file)
