#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
COMPARISON = Path(__file__).resolve().parent.parent
GOLD = BASE / "trials" / "20260404-trial-T2-sample-30-gold.json"
GEMINI_MODELS = [
    "gemini-2.5-flash-lite",
    "gemini-2.5-flash",
    "gemini-2.5-pro",
    "gemini-3.1-pro",
]


def main() -> int:
    gold = {item["item_id"]: item for item in json.load(open(GOLD, encoding="utf-8"))}
    for model in GEMINI_MODELS:
        src = BASE / model / f"20260404-t2-results-{model}.json"
        out_dir = COMPARISON / "derived" / model
        out_dir.mkdir(parents=True, exist_ok=True)
        data = json.load(open(src, encoding="utf-8"))
        beginner_total = 0
        beginner_correct = 0
        advanced_total = 0
        advanced_correct = 0
        for item in data["results"]:
            g = gold[item["item_id"]]
            item["gold"] = g["gold"]
            item["correct"] = item.get("answer") == g["gold"]
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
        out = out_dir / f"20260404-t2-results-{model}.json"
        json.dump(data, open(out, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
        print(f"{model}: {total_correct}/{total_items}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
