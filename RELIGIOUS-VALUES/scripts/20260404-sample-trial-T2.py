#!/usr/bin/env python3
"""Sample 30 stratified items from Islamic Inheritance test set and save as JSON.

Produces TWO output files:
  - *-gold.json   — with gold labels (for scoring only, NEVER show to models)
  - *-admin.json  — without gold labels (safe to include in model prompts)
"""
from __future__ import annotations

import csv
import json
import random
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
DATA_FILE = BASE / "data" / "20260404-Task1_MCQ_Test_gold_labels.csv"
OUT_GOLD = BASE / "trials" / "20260404-trial-T2-sample-30-gold.json"
OUT_ADMIN = BASE / "trials" / "20260404-trial-T2-sample-30-admin.json"
# Legacy path kept for backward compat with scoring scripts
OUT_LEGACY = BASE / "trials" / "20260404-trial-T2-sample-30.json"


def main() -> None:
    items: list[dict] = []
    with open(DATA_FILE, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            items.append(row)

    print(f"Loaded {len(items)} items")

    beginner = [i for i in items if i.get("level", "").strip().lower() == "beginner"]
    advanced = [i for i in items if i.get("level", "").strip().lower() == "advanced"]
    print(f"  Beginner: {len(beginner)}, Advanced: {len(advanced)}")

    random.seed(42)
    b_sample = random.sample(beginner, 15)
    a_sample = random.sample(advanced, 15)
    sample = b_sample + a_sample

    gold_output = []
    admin_output = []
    for idx, item in enumerate(sample, 1):
        base_entry = {
            "index": idx,
            "item_id": item.get("id_question", f"item_{idx}"),
            "level": item.get("level", "").strip(),
            "question": item.get("question", "").strip(),
            "options": {
                "A": item.get("option1", "").strip(),
                "B": item.get("option2", "").strip(),
                "C": item.get("option3", "").strip(),
                "D": item.get("option4", "").strip(),
                "E": item.get("option5", "").strip(),
                "F": item.get("option6", "").strip(),
            },
        }
        # Gold version: includes answer key (for scoring only)
        gold_entry = {**base_entry, "gold": item.get("label", "").strip().upper()}
        gold_output.append(gold_entry)
        # Admin version: NO gold label (safe for model administration)
        admin_output.append(base_entry)

    OUT_GOLD.parent.mkdir(parents=True, exist_ok=True)

    with open(OUT_GOLD, "w", encoding="utf-8") as f:
        json.dump(gold_output, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(gold_output)} items (WITH gold) to {OUT_GOLD}")

    with open(OUT_ADMIN, "w", encoding="utf-8") as f:
        json.dump(admin_output, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(admin_output)} items (NO gold — for model admin) to {OUT_ADMIN}")

    # Legacy file (with gold) for backward compat with existing scoring scripts
    with open(OUT_LEGACY, "w", encoding="utf-8") as f:
        json.dump(gold_output, f, indent=2, ensure_ascii=False)
    print(f"Saved legacy copy to {OUT_LEGACY}")

    # Print items for manual evaluation
    for entry in gold_output:
        print(f"\n{'='*60}")
        print(f"ITEM {entry['index']} | {entry['level']} | ID: {entry['item_id']} | Gold: {entry['gold']}")
        print(f"Q: {entry['question'][:200]}...")
        for letter, text in entry["options"].items():
            print(f"  {letter}) {text[:150]}")


if __name__ == "__main__":
    main()
