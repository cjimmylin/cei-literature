#!/usr/bin/env python3
"""
Re-validate gold standard P/R/F1 using the IMPROVED nonwestern_scoring.py.

Reads per-framework gold standard label files (20260404-gs-nw_*.json),
re-scores each labeled paper with the current scorer, and computes
updated Precision / Recall / F1 per framework.

Outputs:
    COUNCIL/20260404-gold-standard-results-v2.json   — updated metrics
    stdout — comparison table: old v1 vs new v2 metrics

Usage:
    cd CEI-Lit-WS && ../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/revalidate_gold_standard.py
"""
from __future__ import annotations

import functools
import json
import sys
from pathlib import Path

print = functools.partial(print, flush=True)

# ── Path setup ───────────────────────────────────────────────────────
_SCRIPT_DIR = Path(__file__).parent
_CEI_LIT_WS = _SCRIPT_DIR.parent.parent
sys.path.insert(0, str(_CEI_LIT_WS / "PYTHON"))
sys.path.insert(0, str(_CEI_LIT_WS / ".agent" / "lib"))
sys.path.insert(0, str(_SCRIPT_DIR))

from nonwestern_scoring import score_paper_nw
from config import PAPERS_DIR

# ── Paths ────────────────────────────────────────────────────────────
COUNCIL_DIR = _SCRIPT_DIR.parent / "COUNCIL"

# Gold standard label files — map framework field → filename
GS_FILES = {
    "nw_confucian": COUNCIL_DIR / "20260404-gs-nw_confucian.json",
    "nw_ubuntu": COUNCIL_DIR / "20260404-gs-nw_ubuntu.json",
    "nw_islamic_ethics": COUNCIL_DIR / "20260404-gs-nw_islamic.json",
    "nw_buddhist": COUNCIL_DIR / "20260404-gs-nw_buddhist.json",
    "nw_dharmic": COUNCIL_DIR / "20260404-gs-nw_dharmic.json",
    "nw_indigenous_relational": COUNCIL_DIR / "20260404-gs-nw_indigenous.json",
    "nw_buen_vivir": COUNCIL_DIR / "20260404-gs-nw_buen_vivir.json",
}

OLD_RESULTS_PATH = COUNCIL_DIR / "20260404-gold-standard-results.json"
NEW_RESULTS_PATH = COUNCIL_DIR / "20260404-gold-standard-results-v2.json"

# Display names for pretty printing
DISPLAY_NAMES = {
    "nw_confucian": "Confucian Role Ethics",
    "nw_ubuntu": "Ubuntu Communalism",
    "nw_islamic_ethics": "Islamic Ethics (Maqasid)",
    "nw_buddhist": "Buddhist Ethics",
    "nw_dharmic": "Dharmic Ethics",
    "nw_indigenous_relational": "Indigenous Relational",
    "nw_buen_vivir": "Buen Vivir (Sumak Kawsay)",
}


def main() -> int:
    # Load old results for comparison
    old_results = {}
    if OLD_RESULTS_PATH.exists():
        with open(OLD_RESULTS_PATH, "r", encoding="utf-8") as f:
            old_data = json.load(f)
        old_results = old_data.get("frameworks", {})

    # ── Per-framework scoring ────────────────────────────────────────
    new_frameworks = {}
    total_tp = 0
    total_fp = 0
    total_fn = 0
    total_tn = 0
    errors = []

    for field, gs_path in GS_FILES.items():
        if not gs_path.exists():
            print(f"WARNING: Gold standard file not found: {gs_path.name}")
            continue

        with open(gs_path, "r", encoding="utf-8") as f:
            gs_data = json.load(f)

        framework_field = gs_data.get("framework", field)
        detected_labels = gs_data.get("detected_labels", [])
        non_detected_labels = gs_data.get("non_detected_labels", [])

        tp = 0
        fp = 0
        fn = 0
        tn = 0
        details = []  # track individual paper results

        # Process detected_labels (papers that scored >= 50 in the OLD scorer)
        for entry in detected_labels:
            filename = entry["filename"]
            label = entry.get("label", "").upper()
            old_score = entry.get("score", 0)

            paper_path = PAPERS_DIR / filename
            if not paper_path.exists():
                errors.append(f"{field}: paper not found: {filename}")
                continue

            try:
                scores = score_paper_nw(paper_path)
                new_score = scores.get(framework_field, 0)
            except Exception as e:
                errors.append(f"{field}: error scoring {filename}: {e}")
                continue

            detected = new_score >= 50

            if detected and label == "Y":
                tp += 1
                category = "TP"
            elif detected and label == "N":
                fp += 1
                category = "FP"
            elif not detected and label == "Y":
                fn += 1
                category = "FN"
            else:  # not detected and label == "N"
                tn += 1
                category = "TN"

            details.append({
                "filename": filename,
                "old_score": old_score,
                "new_score": new_score,
                "label": label,
                "category": category,
            })

        # Process non_detected_labels (papers that scored < 50 in the OLD scorer)
        for entry in non_detected_labels:
            filename = entry["filename"]
            label = entry.get("label", "").upper()
            old_score = entry.get("score", 0)

            paper_path = PAPERS_DIR / filename
            if not paper_path.exists():
                errors.append(f"{field}: paper not found: {filename}")
                continue

            try:
                scores = score_paper_nw(paper_path)
                new_score = scores.get(framework_field, 0)
            except Exception as e:
                errors.append(f"{field}: error scoring {filename}: {e}")
                continue

            detected = new_score >= 50

            if detected and label == "Y":
                tp += 1
                category = "TP"
            elif detected and label == "N":
                fp += 1
                category = "FP"
            elif not detected and label == "Y":
                fn += 1
                category = "FN"
            else:
                tn += 1
                category = "TN"

            details.append({
                "filename": filename,
                "old_score": old_score,
                "new_score": new_score,
                "label": label,
                "category": category,
            })

        # Compute metrics
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0

        new_frameworks[field] = {
            "display_name": DISPLAY_NAMES.get(field, field),
            "precision": round(precision, 3),
            "recall": round(recall, 3),
            "f1": round(f1, 3),
            "true_positives": tp,
            "false_positives": fp,
            "false_negatives": fn,
            "true_negatives": tn,
            "detected_total": len(detected_labels),
            "non_detected_total": len(non_detected_labels),
            "details": details,
        }

        total_tp += tp
        total_fp += fp
        total_fn += fn
        total_tn += tn

    # ── Aggregate ────────────────────────────────────────────────────
    n_fw = len(new_frameworks)
    mean_p = sum(fw["precision"] for fw in new_frameworks.values()) / max(n_fw, 1)
    mean_r = sum(fw["recall"] for fw in new_frameworks.values()) / max(n_fw, 1)
    mean_f1 = sum(fw["f1"] for fw in new_frameworks.values()) / max(n_fw, 1)

    # ── Save results ─────────────────────────────────────────────────
    output = {
        "date": "20260404",
        "version": "v2",
        "description": "Gold standard re-validation with improved scorer (21 new FP patterns, graduated strong-match floor)",
        "total_papers_reviewed": sum(
            fw["detected_total"] + fw["non_detected_total"]
            for fw in new_frameworks.values()
        ),
        "frameworks": {
            field: {k: v for k, v in fw.items() if k != "details"}
            for field, fw in new_frameworks.items()
        },
        "aggregate": {
            "mean_precision": round(mean_p, 3),
            "mean_recall": round(mean_r, 3),
            "mean_f1": round(mean_f1, 3),
            "total_true_positives": total_tp,
            "total_false_positives": total_fp,
            "total_false_negatives": total_fn,
            "total_true_negatives": total_tn,
        },
        "errors": errors,
        "score_changes": {
            field: [d for d in fw["details"] if d["old_score"] != d["new_score"]]
            for field, fw in new_frameworks.items()
        },
    }

    NEW_RESULTS_PATH.write_text(json.dumps(output, indent=2, ensure_ascii=False))
    print(f"Saved results to {NEW_RESULTS_PATH}\n")

    # ── Print comparison table ───────────────────────────────────────
    print("=" * 90)
    print("GOLD STANDARD VALIDATION: v1 (old) vs v2 (improved scorer)")
    print("=" * 90)
    print()
    print(f"{'Framework':<28} {'P(v1)':>6} {'P(v2)':>6} {'R(v1)':>6} {'R(v2)':>6} {'F1(v1)':>7} {'F1(v2)':>7} {'TP':>4} {'FP':>4} {'FN':>4} {'TN':>4}")
    print("-" * 90)

    for field in GS_FILES:
        if field not in new_frameworks:
            continue
        fw = new_frameworks[field]
        old_fw = old_results.get(field, {})
        old_p = old_fw.get("precision", 0)
        old_r = old_fw.get("recall_estimate", old_fw.get("recall", 0))
        old_f1 = old_fw.get("f1", 0)

        name = DISPLAY_NAMES.get(field, field)[:27]
        print(
            f"{name:<28} {old_p:>6.3f} {fw['precision']:>6.3f} "
            f"{old_r:>6.3f} {fw['recall']:>6.3f} "
            f"{old_f1:>7.3f} {fw['f1']:>7.3f} "
            f"{fw['true_positives']:>4} {fw['false_positives']:>4} "
            f"{fw['false_negatives']:>4} {fw['true_negatives']:>4}"
        )

    print("-" * 90)

    old_agg = old_results and old_data.get("aggregate", {})
    old_mp = old_agg.get("mean_precision", 0) if old_agg else 0
    old_mr = old_agg.get("mean_recall", 0) if old_agg else 0
    old_mf = old_agg.get("mean_f1", 0) if old_agg else 0

    print(
        f"{'MEAN':<28} {old_mp:>6.3f} {mean_p:>6.3f} "
        f"{old_mr:>6.3f} {mean_r:>6.3f} "
        f"{old_mf:>7.3f} {mean_f1:>7.3f} "
        f"{total_tp:>4} {total_fp:>4} {total_fn:>4} {total_tn:>4}"
    )
    print()

    # ── Print score changes ──────────────────────────────────────────
    any_changes = False
    for field in GS_FILES:
        if field not in new_frameworks:
            continue
        changes = [d for d in new_frameworks[field]["details"] if d["old_score"] != d["new_score"]]
        if changes:
            if not any_changes:
                print("SCORE CHANGES (papers where new score differs from old):")
                print("-" * 90)
                any_changes = True
            print(f"\n  {DISPLAY_NAMES.get(field, field)}:")
            for c in changes:
                arrow = "v" if c["new_score"] < c["old_score"] else "^"
                cat_change = f"[{c['category']}]"
                print(
                    f"    {arrow} {c['old_score']:>3} -> {c['new_score']:>3}  "
                    f"label={c['label']} {cat_change:<5} {c['filename']}"
                )

    if not any_changes:
        print("No score changes detected.")

    if errors:
        print(f"\nERRORS ({len(errors)}):")
        for e in errors[:20]:
            print(f"  - {e}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
