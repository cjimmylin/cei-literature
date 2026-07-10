#!/usr/bin/env python3
import json
from pathlib import Path

DATA_DIR = Path("CEI-Lit-WS/RELIGIOUS-VALUES/data")
TRIALS_DIR = Path("CEI-Lit-WS/RELIGIOUS-VALUES/trials")

def strip_gold(input_file, output_file, list_key=None):
    with open(input_file, encoding="utf-8") as f:
        data = json.load(f)
    
    if list_key:
        items = data[list_key]
    else:
        items = data

    admin_items = []
    for item in items:
        # Define allowed fields for administration
        # For construct-validity items
        allowed = ["id", "tradition", "type", "question", "options", "index", "item_id", "level"]
        admin_item = {k: v for k, v in item.items() if k in allowed}
        admin_items.append(admin_item)
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(admin_items, f, indent=2, ensure_ascii=False)
    print(f"Created {output_file} ({len(admin_items)} items)")

def strip_bias_values(input_file, output_file):
    with open(input_file, encoding="utf-8") as f:
        data = json.load(f)
    
    admin_items = []
    for pair in data["pairs"]:
        # Bias item
        bi = pair["bias_item"]
        admin_items.append({
            "id": bi["id"],
            "pair_id": pair["pair_id"],
            "tradition": pair["tradition"],
            "type": "bias",
            "question": bi["question"]
        })
        # Values item
        vi = pair["values_item"]
        admin_items.append({
            "id": vi["id"],
            "pair_id": pair["pair_id"],
            "tradition": pair["tradition"],
            "type": "values",
            "question": vi["question"]
        })
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(admin_items, f, indent=2, ensure_ascii=False)
    print(f"Created {output_file} ({len(admin_items)} items)")

if __name__ == "__main__":
    # 1. Construct Validity Items (45 items)
    strip_gold(
        DATA_DIR / "20260404-construct-validity-items.json",
        TRIALS_DIR / "20260404-construct-validity-items-admin.json",
        list_key="items"
    )
    
    # 2. Bias-Values Items (20 items)
    strip_bias_values(
        DATA_DIR / "20260404-bias-values-items.json",
        TRIALS_DIR / "20260404-bias-values-items-admin.json"
    )
