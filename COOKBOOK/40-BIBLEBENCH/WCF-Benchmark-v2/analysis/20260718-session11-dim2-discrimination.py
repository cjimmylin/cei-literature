"""
Dimension 2 item assessment: per-item discrimination / difficulty / dead-ceiling evidence.
Consolidates pilot triage, gate-run per-item data, and s8 J4/J5 rows into a single ledger.

Outputs:
  analysis/20260718-session11-ledger-dim2.json
  analysis/20260718-session11-dim2-summary.json
"""
import json
import csv
import statistics
from pathlib import Path
from collections import defaultdict, Counter

ROOT = Path(__file__).parent.parent

# ---------------------------------------------------------------------------
# 1. Load the 287-item bank
# ---------------------------------------------------------------------------
def load_bank():
    items = {}
    for fname in ["data/wcf_main.jsonl", "data/wcf_episodes.jsonl"]:
        for line in (ROOT / fname).open():
            r = json.loads(line)
            item_id = r["id"]
            pfx = item_id.split("-")[0]
            # AGG and CONT share aggravate-family; NARROW = episodes mold
            is_core_N = "-N-" in item_id
            items[item_id] = {
                "mold": pfx,
                "is_core_N": is_core_N,
            }
    return items

# ---------------------------------------------------------------------------
# 2. Pilot triage (221 items)
# ---------------------------------------------------------------------------
def load_pilot():
    pilot = {}
    with open(ROOT / "analysis/20260716-session5-item-triage.csv") as f:
        for r in csv.DictReader(f):
            sid = r["sample_id"]
            spread = float(r["cross_sut_spread"]) if r["cross_sut_spread"] else None
            itr = float(r["item_total_r_exploratory"]) if r["item_total_r_exploratory"] else None
            pilot[sid] = {
                "pilot_triage_class": r["triage_class"],
                "pilot_cross_sut_spread": spread,
                "pilot_item_total_r": itr,
            }
    return pilot

# ---------------------------------------------------------------------------
# 3. Gate results (s6 and s7 per_item dicts)
# ---------------------------------------------------------------------------
def load_gate(path, run_label):
    data = json.loads((ROOT / path).read_text())
    out = {}
    for item_id, vals in data.get("per_item", {}).items():
        out[item_id] = {
            "gate_run": run_label,
            "gate_gap_qwen_haiku": vals.get("gap_qwen_haiku"),
            "gate_per_sut": {k: v for k, v in vals.items() if k != "gap_qwen_haiku"},
        }
    return out

# ---------------------------------------------------------------------------
# 4. s8 J4/J5 rows — parse sample_key -> item|SUT|epoch|stratum
# ---------------------------------------------------------------------------
def load_s8():
    """
    Combines J4 and J5 rows. Skips rows where parse_fail==True or grade is None
    (channel_error rows with grade=None appear in the raw files due to claude -p
    subprocess failures; these carry no numeric signal and must be excluded).

    s8_n_rows = count of rows with usable (non-None) grades.
    per-SUT means are averaged across both judges + all epochs for a given
    item-SUT pair. cross-SUT spread = max(per_sut_mean) - min(per_sut_mean).
    """
    per_item_sut_grades = defaultdict(lambda: defaultdict(list))
    n_rows_per_item = Counter()

    for fname in [
        "analysis/20260717-session8-j4-raw.jsonl",
        "analysis/20260717-session8-j5-raw.jsonl",
    ]:
        for line in (ROOT / fname).open():
            r = json.loads(line)
            # Skip explicit parse failures
            if r.get("parse_fail"):
                continue
            grade = r.get("grade")
            # Skip channel_error rows where grade is None
            if grade is None:
                continue
            parts = r["sample_key"].split("|")
            item_id = parts[0]
            sut = parts[1]
            per_item_sut_grades[item_id][sut].append(grade)
            n_rows_per_item[item_id] += 1

    # Aggregate: per-SUT mean across all epochs + judges
    s8 = {}
    for item_id, sut_grades in per_item_sut_grades.items():
        per_sut_mean = {}
        for sut, grades in sut_grades.items():
            if grades:
                per_sut_mean[sut] = round(statistics.mean(grades), 2)
        means = list(per_sut_mean.values())
        spread = round(max(means) - min(means), 2) if len(means) >= 2 else None
        s8[item_id] = {
            "s8_n_rows": n_rows_per_item[item_id],
            "s8_per_sut_mean": per_sut_mean,
            "s8_cross_sut_spread": spread,
        }
    return s8

# ---------------------------------------------------------------------------
# 5. Cohort labeling
# ---------------------------------------------------------------------------
def load_cohorts():
    """
    s6_cohort: the 52 items in data/session6_new_items.json (run through gate6)
    s7_cohort: the 42 items in data/session7_new_items.json (run through gate7)
    v1_layer:  287 - 94 = 193 items from the original pilot bank not added in s6/s7
    Method: explicit new-item lists from session6_new_items.json +
            session7_new_items.json; remainder = v1 layer.
    """
    s6_ids = {r["id"] for r in json.loads((ROOT / "data/session6_new_items.json").read_text())}
    s7_ids = {r["id"] for r in json.loads((ROOT / "data/session7_new_items.json").read_text())}
    return s6_ids, s7_ids

# ---------------------------------------------------------------------------
# 6. discrimination_verdict logic
# ---------------------------------------------------------------------------
def compute_verdict(entry):
    """
    Priority order: DEAD-CEILING > DISCRIMINATING > WEAK > NO-EVIDENCE

    DEAD-CEILING:
      - pilot_triage_class == "DEAD-CEILING", OR
      - all observed SUT means >= 95 AND s8_cross_sut_spread < 5

    DISCRIMINATING:
      - pilot_triage_class == "CORE-DISCRIMINATING", OR
      - gate_gap_qwen_haiku is not None and != 0, OR
      - s8_cross_sut_spread >= 15

    WEAK: otherwise-with-evidence (at least one era present, not NO-EVIDENCE)

    NO-EVIDENCE: evidence_era == ["none"]
    """
    eras = entry["evidence_era"]
    if not eras or eras == ["none"]:
        return "NO-EVIDENCE"

    # DEAD-CEILING checks
    is_dc = False
    if entry.get("pilot_triage_class") == "DEAD-CEILING":
        is_dc = True
    if not is_dc and entry.get("s8_per_sut_mean"):
        means = list(entry["s8_per_sut_mean"].values())
        spread = entry.get("s8_cross_sut_spread")
        if means and all(m >= 95 for m in means) and spread is not None and spread < 5:
            is_dc = True
    if is_dc:
        return "DEAD-CEILING"

    # DISCRIMINATING checks
    is_disc = False
    if entry.get("pilot_triage_class") == "CORE-DISCRIMINATING":
        is_disc = True
    gate_gap = entry.get("gate_gap_qwen_haiku")
    if gate_gap is not None and gate_gap != 0:
        is_disc = True
    s8_spread = entry.get("s8_cross_sut_spread")
    if s8_spread is not None and s8_spread >= 15:
        is_disc = True
    if is_disc:
        return "DISCRIMINATING"

    return "WEAK"

# ---------------------------------------------------------------------------
# 7. Conflicting evidence: pilot DEAD-CEILING but s8 spread >= 15
# ---------------------------------------------------------------------------
def is_conflicting(entry):
    if entry.get("pilot_triage_class") == "DEAD-CEILING":
        s8_spread = entry.get("s8_cross_sut_spread")
        if s8_spread is not None and s8_spread >= 15:
            return True
    return False

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    bank = load_bank()
    pilot = load_pilot()
    gate6 = load_gate("analysis/20260716-session6-gate-results.json", "s6")
    gate7 = load_gate("analysis/20260716-session7-gate-results.json", "s7")
    s8 = load_s8()
    s6_ids, s7_ids = load_cohorts()

    ledger = {}

    for item_id, base in bank.items():
        entry = dict(base)

        # --- pilot ---
        p = pilot.get(item_id, {})
        entry["pilot_triage_class"] = p.get("pilot_triage_class")
        entry["pilot_cross_sut_spread"] = p.get("pilot_cross_sut_spread")
        entry["pilot_item_total_r"] = p.get("pilot_item_total_r")

        # --- gate ---
        # An item appears in gate6 OR gate7 (they are disjoint new-item sets)
        g = gate6.get(item_id) or gate7.get(item_id)
        entry["gate_run"] = g["gate_run"] if g else None
        entry["gate_gap_qwen_haiku"] = g["gate_gap_qwen_haiku"] if g else None

        # --- s8 ---
        s = s8.get(item_id, {})
        entry["s8_n_rows"] = s.get("s8_n_rows", 0)
        entry["s8_per_sut_mean"] = s.get("s8_per_sut_mean", {})
        entry["s8_cross_sut_spread"] = s.get("s8_cross_sut_spread")

        # --- evidence eras ---
        eras = []
        if item_id in pilot:
            eras.append("pilot")
        if item_id in gate6:
            eras.append("gate6")
        if item_id in gate7:
            eras.append("gate7")
        if item_id in s8:
            eras.append("s8")
        entry["evidence_era"] = eras if eras else ["none"]

        # --- verdict ---
        entry["discrimination_verdict"] = compute_verdict(entry)

        ledger[item_id] = entry

    # -----------------------------------------------------------------------
    # Write ledger
    # -----------------------------------------------------------------------
    ledger_path = ROOT / "analysis/20260718-session11-ledger-dim2.json"
    ledger_path.write_text(json.dumps(ledger, indent=2))
    print(f"Ledger written: {ledger_path} ({ledger_path.stat().st_size} bytes, {len(ledger)} entries)")

    # -----------------------------------------------------------------------
    # Summary
    # -----------------------------------------------------------------------
    all_entries = list(ledger.values())
    all_item_ids = list(ledger.keys())

    verdict_overall = Counter(e["discrimination_verdict"] for e in all_entries)

    # By mold
    verdict_by_mold = defaultdict(Counter)
    for item_id, e in ledger.items():
        verdict_by_mold[e["mold"]][e["discrimination_verdict"]] += 1

    # By cohort
    # Cohort method: explicit session new-item files (session6_new_items.json,
    # session7_new_items.json); v1-layer = all remaining 287-94 items.
    cohort_label = {}
    for iid in all_item_ids:
        if iid in s6_ids:
            cohort_label[iid] = "s6-new"
        elif iid in s7_ids:
            cohort_label[iid] = "s7-new"
        else:
            cohort_label[iid] = "v1-layer"

    verdict_by_cohort = defaultdict(Counter)
    for iid, e in ledger.items():
        verdict_by_cohort[cohort_label[iid]][e["discrimination_verdict"]] += 1

    # By is_core_N
    verdict_by_core_N = defaultdict(Counter)
    for e in all_entries:
        verdict_by_core_N[e["is_core_N"]][e["discrimination_verdict"]] += 1

    # v1-layer dead-ceiling %
    v1_items = [iid for iid, lbl in cohort_label.items() if lbl == "v1-layer"]
    v1_dc = sum(1 for iid in v1_items if ledger[iid]["discrimination_verdict"] == "DEAD-CEILING")
    v1_dc_pct = round(v1_dc / len(v1_items) * 100, 1) if v1_items else None

    # Conflicting evidence items
    conflicting = [iid for iid, e in ledger.items() if is_conflicting(e)]
    conflicting_examples = conflicting[:3]

    # Parsing notes
    parsing_notes = [
        "s8 J4/J5 raw files contain 218 rows with grade=None (channel_error: "
        "'claude -p exited 1'); these are excluded from per-item means. "
        "s8_n_rows counts only rows with a numeric grade.",
    ]

    summary = {
        "_caveats": [
            "Scores are panel-median rubric conformity (ranks, not absolute capability values).",
            "Pilot and v2.4 (gate6/gate7/s8) are different bank versions and separate instruments. "
            "Evidence is era-tagged; pilot and v2.4 metrics are never averaged across eras.",
            "Single-judge s8 J4 (Opus-4.8) and J5 (GPT-5.5) rows are stability signals only; "
            "per-SUT means in s8_per_sut_mean are means across both judges and all epochs for "
            "a given item-SUT pair.",
            "Cohort labels use explicit new-item lists from data/session6_new_items.json and "
            "data/session7_new_items.json; v1-layer = all remaining 287-94=193 items "
            "(original pilot bank items not added in s6/s7 waves).",
        ],
        "_parsing_notes": parsing_notes,
        "total_items": len(ledger),
        "verdict_overall": dict(verdict_overall),
        "verdict_by_mold": {
            mold: dict(cnts) for mold, cnts in sorted(verdict_by_mold.items())
        },
        "verdict_by_cohort": {
            cohort: dict(cnts) for cohort, cnts in sorted(verdict_by_cohort.items())
        },
        "verdict_by_is_core_N": {
            str(k): dict(v) for k, v in sorted(verdict_by_core_N.items())
        },
        "v1_layer_count": len(v1_items),
        "v1_layer_dead_ceiling_count": v1_dc,
        "v1_layer_dead_ceiling_pct": v1_dc_pct,
        "known_pilot_dead_ceiling_pct": 53.8,
        "note_v1_dc_pct": (
            "v1_layer_dead_ceiling_pct counts items with verdict==DEAD-CEILING in the v1 layer. "
            "The known 53.8% figure (119/221) comes from the session5 pilot triage CSV; "
            "the v1-layer here is 193 items (pilot minus 28 pilot items that also appear in "
            "s6/s7 new-item lists, if any — check cohort counts). "
            "s8-era DEAD-CEILING condition (all-SUT means>=95 and spread<5) may add items "
            "beyond those flagged in pilot triage."
        ),
        "conflicting_evidence_count": len(conflicting),
        "conflicting_evidence_definition": (
            "pilot_triage_class == DEAD-CEILING but s8_cross_sut_spread >= 15 "
            "(item was ceiling-flat in pilot era but shows cross-SUT spread >=15 in v2.4 s8 runs)"
        ),
        "conflicting_evidence_examples": conflicting_examples,
        "cohort_method": (
            "s6-new: 52 items from data/session6_new_items.json (gate6 run); "
            "s7-new: 42 items from data/session7_new_items.json (gate7 run); "
            "v1-layer: 287 - 94 = 193 items not in s6 or s7 new-item lists."
        ),
    }

    summary_path = ROOT / "analysis/20260718-session11-dim2-summary.json"
    summary_path.write_text(json.dumps(summary, indent=2))
    print(f"Summary written: {summary_path} ({summary_path.stat().st_size} bytes)")

    # -----------------------------------------------------------------------
    # Screen report
    # -----------------------------------------------------------------------
    print("\n=== DIM-2 DISCRIMINATION LEDGER — SCREEN REPORT ===")
    print(f"Total items: {len(ledger)}")
    print(f"\nVerdict counts (all 287 items):")
    for v, c in sorted(verdict_overall.items(), key=lambda x: -x[1]):
        print(f"  {v:<20} {c:>4}  ({c/len(ledger)*100:.1f}%)")
    print(f"\nv1-layer ({len(v1_items)} items): DEAD-CEILING = {v1_dc} ({v1_dc_pct}%)")
    print(f"  (Known pilot-era figure: 53.8% [119/221 pilot items])")
    print(f"\nConflicting evidence items: {len(conflicting)}")
    if conflicting_examples:
        print(f"  Examples: {', '.join(conflicting_examples)}")
    print("\nVerdict by cohort:")
    for cohort, cnts in sorted(verdict_by_cohort.items()):
        row = "  " + cohort + " (n=" + str(sum(cnts.values())) + "): " + " | ".join(
            f"{k}={v}" for k, v in sorted(cnts.items()))
        print(row)
    print("\nVerdict by mold:")
    for mold, cnts in sorted(verdict_by_mold.items()):
        row = "  " + mold + ": " + " | ".join(f"{k}={v}" for k, v in sorted(cnts.items()))
        print(row)
    print("\nVerdict by is_core_N:")
    for is_n, cnts in sorted(verdict_by_core_N.items()):
        label = "core-N" if is_n else "non-N"
        row = f"  {label}: " + " | ".join(f"{k}={v}" for k, v in sorted(cnts.items()))
        print(row)
    print("\nParsing notes:")
    for note in parsing_notes:
        print(f"  - {note}")


if __name__ == "__main__":
    main()
