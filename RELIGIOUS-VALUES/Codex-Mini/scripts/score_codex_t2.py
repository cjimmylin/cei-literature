#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
RESULTS = BASE / "results"
GOLD_FILE = BASE / "trials" / "20260404-trial-T2-sample-30-gold.json"
INPUT_FILE = RESULTS / "20260404-t2-results-gpt-codex-mini.json"


def main() -> int:
    gold_items = json.load(open(GOLD_FILE, encoding="utf-8"))
    gold_by_id = {item["item_id"]: item for item in gold_items}
    data = json.load(open(INPUT_FILE, encoding="utf-8"))

    beginner_total = 0
    beginner_correct = 0
    advanced_total = 0
    advanced_correct = 0

    for item in data["results"]:
        gold = gold_by_id[item["item_id"]]
        item["gold"] = gold["gold"]
        item["correct"] = item.get("answer") == gold["gold"]
        level = item.get("level", "").lower()
        if level == "beginner":
            beginner_total += 1
            beginner_correct += int(item["correct"])
        elif level == "advanced":
            advanced_total += 1
            advanced_correct += int(item["correct"])

    total_items = len(data["results"])
    total_correct = sum(1 for item in data["results"] if item["correct"])
    data["summary"] = {
        "total_correct": total_correct,
        "total_items": total_items,
        "accuracy": round(total_correct / total_items, 4) if total_items else 0.0,
        "beginner_correct": beginner_correct,
        "beginner_total": beginner_total,
        "advanced_correct": advanced_correct,
        "advanced_total": advanced_total,
    }

    with open(INPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Scored {INPUT_FILE.name}: {total_correct}/{total_items}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
