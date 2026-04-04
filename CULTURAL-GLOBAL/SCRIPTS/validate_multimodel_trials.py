#!/usr/bin/env python3
"""
Validate multi-model trial JSON files for the Cross-Cultural benchmark study.

Checks:
  1. JSON parsability
  2. items_count matches len(items)
  3. Required fields present per trial type
  4. Numeric responses in valid range
  5. Qualitative items have response_numeric = null
  6. Item IDs match 1:1 with Opus baseline
  7. Model field is correct
  8. Domain-specific fields present

Output: CULTURAL-GLOBAL/DATA/20260404-multimodel-validation-report.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
TRIALS_DIR = BASE / "TRIALS"
DATA_DIR = BASE / "DATA"
OUTPUT = DATA_DIR / "20260404-multimodel-validation-report.json"

MODELS = ["opus", "sonnet", "haiku"]
TRIAL_IDS = [f"CC{i}" for i in range(1, 11)]

# Trial metadata
TRIAL_META = {
    "CC1":  {"items": 50, "numeric": True,  "scale_max": 5, "scale_min": 1,
             "extra_fields": ["human_baselines"]},
    "CC2":  {"items": 50, "numeric": True,  "scale_max": 5, "scale_min": 0,
             "extra_fields": ["subtype"]},
    "CC3":  {"items": 40, "numeric": True,  "scale_max": 5, "scale_min": 1,
             "extra_fields": ["cultural_lens"]},
    "CC4":  {"items": 40, "numeric": True,  "scale_max": 5, "scale_min": 1,
             "extra_fields": ["maqsad", "rlhf_conflict"]},
    "CC5":  {"items": 30, "numeric": True,  "scale_max": 5, "scale_min": 1,
             "extra_fields": ["wu_lun", "confucian_concept",
                              "western_framing", "confucian_framing"]},
    "CC6":  {"items": 30, "numeric": False, "extra_fields": [
             "tradition_perspective", "rlhf_tension"]},
    "CC7":  {"items": 30, "numeric": False, "extra_fields": [
             "tradition_perspective", "rlhf_tension"]},
    "CC8":  {"items": 40, "numeric": False, "extra_fields": [
             "knowledge_vs_expression_gap"]},
    "CC9":  {"items": 30, "numeric": False, "extra_fields": [
             "tradition_perspective", "rlhf_tension"]},
    "CC10": {"items": 40, "numeric": False, "extra_fields": [
             "perspectives", "my_response", "rlhf_pulls_toward"]},
}

REQUIRED_ITEM_FIELDS = ["id", "question", "domain", "response"]


def find_trial_file(trial_id: str, model: str) -> Path | None:
    """Find trial file by trial_id and model suffix."""
    for fn in TRIALS_DIR.glob(f"20260404-trial-{trial_id}-*-{model}.json"):
        return fn
    return None


def validate_trial(trial_id: str, model: str) -> dict:
    """Validate a single trial file. Returns dict of errors and warnings."""
    result = {
        "trial_id": trial_id,
        "model": model,
        "file": None,
        "status": "PASS",
        "errors": [],
        "warnings": [],
        "item_count": 0,
    }

    path = find_trial_file(trial_id, model)
    if path is None:
        result["status"] = "MISSING"
        result["errors"].append(f"File not found: 20260404-trial-{trial_id}-*-{model}.json")
        return result
    result["file"] = str(path.name)

    # 1. JSON parsability
    try:
        with open(path) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        result["status"] = "FAIL"
        result["errors"].append(f"Invalid JSON: {e}")
        return result

    meta = TRIAL_META.get(trial_id, {})
    expected_count = meta.get("items", 0)
    items = data.get("items", [])
    result["item_count"] = len(items)

    # 2. items_count matches
    declared = data.get("items_count", 0)
    if declared != len(items):
        result["errors"].append(
            f"items_count={declared} but len(items)={len(items)}")

    if len(items) != expected_count:
        result["errors"].append(
            f"Expected {expected_count} items, got {len(items)}")

    # 3. Model field
    model_field = data.get("model", "")
    if model not in model_field.lower():
        result["warnings"].append(
            f"model field '{model_field}' doesn't contain '{model}'")

    # 4. Required fields + numeric validation
    is_numeric = meta.get("numeric", False)
    scale_min = meta.get("scale_min", 1)
    scale_max = meta.get("scale_max", 5)

    for item in items:
        item_id = item.get("id", "?")

        # Required fields
        for field in REQUIRED_ITEM_FIELDS:
            if field not in item or not item[field]:
                if field == "response" and item.get("my_response"):
                    continue  # CC10 uses my_response instead
                result["errors"].append(
                    f"Item {item_id}: missing required field '{field}'")

        # Numeric validation
        if is_numeric:
            val = item.get("response_numeric")
            if val is None:
                result["errors"].append(
                    f"Item {item_id}: response_numeric is null (expected numeric)")
            elif not isinstance(val, (int, float)):
                result["errors"].append(
                    f"Item {item_id}: response_numeric is {type(val).__name__}, not number")
            elif val < scale_min or val > scale_max:
                result["errors"].append(
                    f"Item {item_id}: response_numeric={val} outside [{scale_min},{scale_max}]")
        else:
            val = item.get("response_numeric")
            if val is not None:
                result["warnings"].append(
                    f"Item {item_id}: qualitative item has response_numeric={val}")

        # Extra fields (only for non-Opus models, check response fields)
        if model != "opus":
            for field in meta.get("extra_fields", []):
                # Read-only fields from Opus (human_baselines, subtype, maqsad,
                # wu_lun, confucian_concept, culturally_correct_answer) are
                # not required in response
                if field in ("human_baselines", "subtype", "maqsad",
                             "wu_lun", "confucian_concept",
                             "culturally_correct_answer"):
                    continue
                if field not in item:
                    result["warnings"].append(
                        f"Item {item_id}: missing extra field '{field}'")
                elif field == "perspectives" and isinstance(item.get(field), dict):
                    expected_keys = {"western_liberal", "islamic", "confucian",
                                     "ubuntu", "indigenous"}
                    actual_keys = set(item[field].keys())
                    missing = expected_keys - actual_keys
                    if missing:
                        result["errors"].append(
                            f"Item {item_id}: perspectives missing keys: {missing}")

    # 5. Item ID matching with Opus baseline
    if model != "opus":
        opus_path = find_trial_file(trial_id, "opus")
        if opus_path:
            with open(opus_path) as f:
                opus_data = json.load(f)
            opus_ids = {item.get("id") for item in opus_data.get("items", [])}
            trial_ids_set = {item.get("id") for item in items}
            missing_ids = opus_ids - trial_ids_set
            extra_ids = trial_ids_set - opus_ids
            if missing_ids:
                result["errors"].append(
                    f"Missing item IDs vs Opus: {sorted(missing_ids)}")
            if extra_ids:
                result["warnings"].append(
                    f"Extra item IDs not in Opus: {sorted(extra_ids)}")

    # Status
    if result["errors"]:
        result["status"] = "FAIL"
    elif result["warnings"]:
        result["status"] = "WARN"

    return result


def main():
    print("Validating multi-model trial files...\n")
    results = []
    pass_count = 0
    warn_count = 0
    fail_count = 0
    missing_count = 0

    for model in MODELS:
        for tid in TRIAL_IDS:
            r = validate_trial(tid, model)
            results.append(r)
            status = r["status"]
            if status == "PASS":
                pass_count += 1
            elif status == "WARN":
                warn_count += 1
            elif status == "FAIL":
                fail_count += 1
            elif status == "MISSING":
                missing_count += 1

            icon = {"PASS": "✓", "WARN": "⚠", "FAIL": "✗", "MISSING": "○"}[status]
            print(f"  {icon} {model:7s} {tid:5s} | items={r['item_count']:3d} | "
                  f"{status}")
            for e in r["errors"][:3]:
                print(f"      ERROR: {e}")
            for w in r["warnings"][:2]:
                print(f"      WARN:  {w}")

    print(f"\n=== Summary ===")
    print(f"  PASS: {pass_count}  WARN: {warn_count}  "
          f"FAIL: {fail_count}  MISSING: {missing_count}")

    report = {
        "date": "2026-04-04",
        "script": "validate_multimodel_trials.py",
        "summary": {
            "total": len(results),
            "pass": pass_count,
            "warn": warn_count,
            "fail": fail_count,
            "missing": missing_count,
        },
        "results": results,
    }

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\nReport written to {OUTPUT}")

    # Exit code: non-zero if any failures
    sys.exit(1 if fail_count > 0 else 0)


if __name__ == "__main__":
    main()
