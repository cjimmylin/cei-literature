#!/usr/bin/env python3
"""
Rubric Scorer for Construct Validity Trials — Religious Values Benchmark

Scores model responses using rubrics from the items files.
Designed to be run by a Claude agent that evaluates responses and writes scores.

This script provides the scaffolding (loading items, matching rubrics, output format).
The actual scoring is done by the agent reading responses and applying rubrics.

Usage (for generating scoring templates):
    python 20260404-rubric-scorer.py --respondent sonnet --tradition islam --format template
    python 20260404-rubric-scorer.py --respondent haiku --tradition christianity --format template

The template output shows each item's question, rubric, and response to be scored.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

MAX_SCORES = {
    "knowledge": 1.0,
    "reasoning": 3,
    "values": 5,
    "bias": 3,
    "values_paired": 5,
}


def load_items() -> dict[str, dict]:
    """Load all items indexed by item_id."""
    items = {}

    # Construct validity items
    cv_path = DATA_DIR / "20260404-construct-validity-items.json"
    cv_data = json.load(open(cv_path, encoding="utf-8"))
    for item in cv_data["items"]:
        items[item["id"]] = item

    # Bias-values items
    bv_path = DATA_DIR / "20260404-bias-values-items.json"
    bv_data = json.load(open(bv_path, encoding="utf-8"))
    for pair in bv_data["pairs"]:
        bi = pair["bias_item"]
        items[bi["id"]] = {**bi, "tradition": pair["tradition"], "type": "bias"}
        vi = pair["values_item"]
        items[vi["id"]] = {**vi, "tradition": pair["tradition"], "type": "values_paired"}

    return items


def load_responses(model_slug: str, tradition: str) -> list[dict]:
    """Load trial responses for a model/tradition."""
    fpath = DATA_DIR / f"20260404-trial-{tradition}-{model_slug}.json"
    if not fpath.exists():
        raise FileNotFoundError(f"No trial file: {fpath}")
    data = json.load(open(fpath, encoding="utf-8"))
    return data.get("results", [])


def generate_scoring_template(model_slug: str, tradition: str) -> None:
    """Print a scoring template for an agent to evaluate."""
    items = load_items()
    responses = load_responses(model_slug, tradition)

    print(f"# Rubric Scoring Template: {model_slug} / {tradition.title()}")
    print(f"# {len(responses)} items to score\n")

    for resp in responses:
        item_id = resp["item_id"]
        item = items.get(item_id, {})
        item_type = resp.get("type", item.get("type", "unknown"))
        # Normalize type for max_score lookup
        max_score = MAX_SCORES.get(item_type, MAX_SCORES.get("values", 5))

        print(f"## Item: {item_id} (type: {item_type}, max_score: {max_score})")
        print(f"**Question:** {resp.get('question', item.get('question', 'N/A'))}")
        print(f"**Rubric:** {item.get('scoring_rubric', 'N/A')}")
        print(f"**Response:** {resp.get('response', 'N/A')[:500]}...")
        print(f"**Score:** ___")
        print(f"**Justification:** ___")
        print()


def main():
    parser = argparse.ArgumentParser(description="Rubric scorer for trial responses")
    parser.add_argument("--respondent", required=True, help="Model slug (sonnet/haiku)")
    parser.add_argument("--tradition", required=True, help="Tradition (islam/christianity/hinduism)")
    parser.add_argument("--format", default="template", choices=["template", "json"])
    args = parser.parse_args()

    if args.format == "template":
        generate_scoring_template(args.respondent, args.tradition)
    elif args.format == "json":
        # Output the items + responses as JSON for agent consumption
        items = load_items()
        responses = load_responses(args.respondent, args.tradition)
        output = []
        for resp in responses:
            item_id = resp["item_id"]
            item = items.get(item_id, {})
            item_type = resp.get("type", item.get("type", "unknown"))
            max_score = MAX_SCORES.get(item_type, MAX_SCORES.get("values", 5))
            output.append({
                "item_id": item_id,
                "type": item_type,
                "max_score": max_score,
                "question": resp.get("question", item.get("question", "")),
                "scoring_rubric": item.get("scoring_rubric", ""),
                "response": resp.get("response", ""),
            })
        print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
