"""
Dimension 5 — Per-Item Judge Reliability/Agreement
Session 11, 2026-07-18

Inputs
------
analysis/20260716-session5-item-matrix.json   pilot panel-3 scores per (item x SUT) row
analysis/20260716-session5-kin-matrix.json    5-grader scores per (item x SUT) row (678 rows)
analysis/20260716-session5-g-partition.json   92 high-spread rows with disagreement categories
analysis/20260717-session8-j4-raw.jsonl       779 rows, J4=claude-opus-4-8 grades
analysis/20260717-session8-j5-raw.jsonl       562 rows, J5=gpt-5.5 grades

Outputs
-------
analysis/20260718-session11-ledger-dim5.json    per-item ledger
analysis/20260718-session11-dim5-summary.json   summary stats + top-15 worst items
"""

import json
import math
import statistics
from collections import defaultdict
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).parent  # analysis/ directory

# ---------------------------------------------------------------------------
# Helper: mold from item_id prefix
# ---------------------------------------------------------------------------
def item_to_mold(item_id: str) -> str:
    prefix = item_id.split("-")[0]
    mold_map = {"COMP": "complicit", "STED": "steadfast", "CONT": "contested"}
    return mold_map.get(prefix, "v1-kind")


# ---------------------------------------------------------------------------
# Source 1: pilot panel spread  (item-matrix.json  →  "pilot" array)
# pilot rows have sample_id = item_id (not item|SUT), sut field separate
# panel_values: list of 3 scores (may include None if panel_n_valid < 3)
# Metric: per (item, SUT) row: spread = max - min over valid values
#         aggregate to per-item: mean of per-row spreads
# ---------------------------------------------------------------------------
def load_pilot(path: Path):
    with open(path) as f:
        data = json.load(f)
    rows = data["pilot"]

    item_spreads: dict[str, list[float]] = defaultdict(list)
    for row in rows:
        item_id = row["sample_id"]
        vals = [v for v in row["panel_values"] if v is not None]
        if len(vals) >= 2:
            spread = max(vals) - min(vals)
            item_spreads[item_id].append(spread)
        # rows with only 1 valid value contribute no spread info — skip

    result = {}
    for item_id, spreads in item_spreads.items():
        result[item_id] = {
            "pilot_mean_panel_spread": round(statistics.mean(spreads), 4),
            "pilot_n_rows": len(spreads),
        }
    return result


# ---------------------------------------------------------------------------
# Source 2: kin-matrix 5-grader disagreement
# graders: gemini, deepseek, mistral_small, nova, command_r
# Per row: mean absolute pairwise disagreement over C(5,2)=10 pairs
# Aggregate to per-item mean; also identify worst grader (highest mean deviation
# from row-mean, summed over item's rows)
# ---------------------------------------------------------------------------
KIN_GRADERS = ["gemini", "deepseek", "mistral_small", "nova", "command_r"]


def load_kin(path: Path):
    with open(path) as f:
        data = json.load(f)
    rows = data["matrix"]

    item_mapd: dict[str, list[float]] = defaultdict(list)       # per-row mean abs pairwise diff
    grader_dev: dict[str, dict[str, float]] = defaultdict(lambda: defaultdict(float))
    grader_cnt: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))

    for row in rows:
        item_id = row["sample_id"]
        vals = {g: row[g] for g in KIN_GRADERS if row.get(g) is not None}
        grader_list = list(vals.keys())
        if len(grader_list) < 2:
            continue

        # Mean abs pairwise disagreement for this row
        pairs = list(combinations(grader_list, 2))
        diffs = [abs(vals[a] - vals[b]) for a, b in pairs]
        mapd = statistics.mean(diffs)
        item_mapd[item_id].append(mapd)

        # Deviation of each grader from row mean (for worst-grader identification)
        row_mean = statistics.mean(vals.values())
        for g in grader_list:
            grader_dev[item_id][g] += abs(vals[g] - row_mean)
            grader_cnt[item_id][g] += 1

    result = {}
    for item_id, mapds in item_mapd.items():
        # Worst grader: highest mean absolute deviation from row mean across item's rows
        devs = {g: grader_dev[item_id][g] / grader_cnt[item_id][g]
                for g in grader_dev[item_id] if grader_cnt[item_id][g] > 0}
        worst_grader = max(devs, key=lambda g: devs[g]) if devs else None
        result[item_id] = {
            "kin_mean_pairwise_disagreement": round(statistics.mean(mapds), 4),
            "kin_n_rows": len(mapds),
            "kin_worst_grader": worst_grader,
        }
    return result


# ---------------------------------------------------------------------------
# Source 3: g-partition categories — keyed by (item_id, sut)
# We want the category at item level: if multiple (item, SUT) pairs have
# categories, take the most frequent; ties broken by precedence order
# from the rules field: A > B > C > D > F > G
# ---------------------------------------------------------------------------
CAT_PRECEDENCE = ["A-gemini-zero", "B-counterfactual", "C-contested",
                  "D-anchor", "F-lone-harsh", "F-lone-lenient", "G-diffuse"]

def load_gpartition(path: Path):
    with open(path) as f:
        data = json.load(f)
    rows = data["rows"]
    # rules precedence string: "A>B>C>D>F>G"

    item_cats: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        item_id = row["sample_id"]
        cat = row.get("cat", "")
        if cat:
            item_cats[item_id].append(cat)

    result = {}
    for item_id, cats in item_cats.items():
        # Most frequent; ties broken by precedence (earlier in list = higher priority)
        freq = defaultdict(int)
        for c in cats:
            freq[c] += 1
        max_freq = max(freq.values())
        candidates = [c for c, n in freq.items() if n == max_freq]
        # Sort candidates by precedence index (lower = higher priority)
        def prec_idx(c):
            for i, pc in enumerate(CAT_PRECEDENCE):
                if c == pc or c.startswith(pc[:2]):
                    return i
            return 99
        chosen = sorted(candidates, key=prec_idx)[0]
        result[item_id] = {"gpartition_category": chosen}
    return result


# ---------------------------------------------------------------------------
# Source 4: J4 x J5 cross-vendor agreement
# Twin rows: same sample_key in both J4 and J5 (no parse_fail)
# sample_key = item|SUT|epoch|stratum  →  item = split('|')[0]
# Per twin row: |J4 grade - J5 grade|
# Aggregate to per-item mean cross-vendor delta
# ---------------------------------------------------------------------------
def load_j4_j5(j4_path: Path, j5_path: Path):
    def read_jsonl(p):
        with open(p) as f:
            return [json.loads(line) for line in f if line.strip()]

    j4_rows = read_jsonl(j4_path)
    j5_rows = read_jsonl(j5_path)

    # Index J4 by sample_key (exclude parse_fail; none expected but defensive)
    j4_index: dict[str, float] = {}
    for row in j4_rows:
        if not row.get("parse_fail", False):
            j4_index[row["sample_key"]] = row["grade"]

    # For each J5 row that also has a J4 match, compute |delta|
    item_deltas: dict[str, list[float]] = defaultdict(list)
    for row in j5_rows:
        if row.get("parse_fail", False):
            continue
        sk = row["sample_key"]
        if sk in j4_index:
            delta = abs(j4_index[sk] - row["grade"])
            item_id = sk.split("|")[0]
            item_deltas[item_id].append(delta)

    result = {}
    for item_id, deltas in item_deltas.items():
        result[item_id] = {
            "s8_mean_abs_j4_j5_delta": round(statistics.mean(deltas), 4),
            "s8_n_twin_rows": len(deltas),
        }
    return result


# ---------------------------------------------------------------------------
# Flags
# ---------------------------------------------------------------------------
def compute_flag(pilot_spread, kin_mapd, s8_delta):
    has_data = any(v is not None for v in [pilot_spread, kin_mapd, s8_delta])
    if not has_data:
        return "NO-DATA"
    low = False
    if pilot_spread is not None and pilot_spread >= 30:
        low = True
    if kin_mapd is not None and kin_mapd >= 20:
        low = True
    if s8_delta is not None and s8_delta >= 20:
        low = True
    return "LOW-AGREEMENT" if low else "OK"


# ---------------------------------------------------------------------------
# Normalize disagreement scores for ranking (0–100 scale assumed)
# pilot_spread max possible = 100; kin_mapd max possible = 100; s8_delta max = 100
# normalized = value / 100 ; then take max across available sources
# ---------------------------------------------------------------------------
def worst_normalized(pilot_spread, kin_mapd, s8_delta):
    vals = []
    if pilot_spread is not None:
        vals.append(pilot_spread / 100.0)
    if kin_mapd is not None:
        vals.append(kin_mapd / 100.0)
    if s8_delta is not None:
        vals.append(s8_delta / 100.0)
    return max(vals) if vals else 0.0


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    base = ROOT

    print("Loading pilot panel data...")
    pilot_data = load_pilot(base / "20260716-session5-item-matrix.json")
    print(f"  {len(pilot_data)} items from pilot")

    print("Loading kin-matrix data...")
    kin_data = load_kin(base / "20260716-session5-kin-matrix.json")
    print(f"  {len(kin_data)} items from kin-matrix")

    print("Loading g-partition categories...")
    gpart_data = load_gpartition(base / "20260716-session5-g-partition.json")
    print(f"  {len(gpart_data)} items from g-partition")

    print("Loading J4 / J5 twin rows...")
    s8_data = load_j4_j5(
        base / "20260717-session8-j4-raw.jsonl",
        base / "20260717-session8-j5-raw.jsonl",
    )
    print(f"  {len(s8_data)} items from J4×J5 twins")

    # Build union of all item ids
    all_items: set[str] = set()
    all_items.update(pilot_data)
    all_items.update(kin_data)
    all_items.update(gpart_data)
    all_items.update(s8_data)
    print(f"Union of items: {len(all_items)}")

    # Build ledger
    ledger: dict[str, dict] = {}
    for item_id in sorted(all_items):
        p = pilot_data.get(item_id, {})
        k = kin_data.get(item_id, {})
        g = gpart_data.get(item_id, {})
        s = s8_data.get(item_id, {})

        pilot_spread = p.get("pilot_mean_panel_spread")
        kin_mapd = k.get("kin_mean_pairwise_disagreement")
        s8_delta = s.get("s8_mean_abs_j4_j5_delta")

        n_sources = sum([
            bool(p), bool(k), bool(g), bool(s)
        ])

        if n_sources == 0:
            ledger[item_id] = {"n_sources": 0}
        else:
            ledger[item_id] = {
                # pilot
                "pilot_mean_panel_spread": pilot_spread,
                "pilot_n_rows": p.get("pilot_n_rows"),
                # kin
                "kin_mean_pairwise_disagreement": kin_mapd,
                "kin_n_rows": k.get("kin_n_rows"),
                "kin_worst_grader": k.get("kin_worst_grader"),
                # g-partition
                "gpartition_category": g.get("gpartition_category"),
                # s8 cross-vendor
                "s8_mean_abs_j4_j5_delta": s8_delta,
                "s8_n_twin_rows": s.get("s8_n_twin_rows"),
                # flag
                "reliability_flag": compute_flag(pilot_spread, kin_mapd, s8_delta),
            }

    ledger_path = base / "20260718-session11-ledger-dim5.json"
    with open(ledger_path, "w") as f:
        json.dump(ledger, f, indent=2)
    print(f"Ledger written: {ledger_path}")

    # ---------------------------------------------------------------------------
    # Summary
    # ---------------------------------------------------------------------------

    # Flag counts overall
    flag_counts_overall = {"LOW-AGREEMENT": 0, "OK": 0, "NO-DATA": 0}
    for entry in ledger.values():
        flag = entry.get("reliability_flag", "NO-DATA")
        if "n_sources" in entry and entry.get("n_sources") == 0:
            flag = "NO-DATA"
        flag_counts_overall[flag] = flag_counts_overall.get(flag, 0) + 1

    # Flag counts by mold (id prefix mapped to mold label)
    flag_by_mold: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for item_id, entry in ledger.items():
        mold = item_to_mold(item_id)
        flag = entry.get("reliability_flag", "NO-DATA")
        if "n_sources" in entry and entry.get("n_sources") == 0:
            flag = "NO-DATA"
        flag_by_mold[mold][flag] += 1

    # Flag counts for -N- core items (item_id contains '-N-')
    flag_n_core: dict[str, int] = defaultdict(int)
    for item_id, entry in ledger.items():
        if "-N-" not in item_id:
            continue
        flag = entry.get("reliability_flag", "NO-DATA")
        if "n_sources" in entry and entry.get("n_sources") == 0:
            flag = "NO-DATA"
        flag_n_core[flag] += 1

    # Top 15 worst items by max normalized disagreement (descending)
    scored_items = []
    for item_id, entry in ledger.items():
        if "n_sources" in entry and entry.get("n_sources") == 0:
            continue
        pilot_spread = entry.get("pilot_mean_panel_spread")
        kin_mapd = entry.get("kin_mean_pairwise_disagreement")
        s8_delta = entry.get("s8_mean_abs_j4_j5_delta")
        score = worst_normalized(pilot_spread, kin_mapd, s8_delta)
        scored_items.append((item_id, score, entry.get("reliability_flag", "OK")))

    scored_items.sort(key=lambda x: x[1], reverse=True)
    top_15 = [
        {
            "rank": i + 1,
            "item_id": item_id,
            "mold": item_to_mold(item_id),
            "max_normalized_disagreement": round(score, 4),
            "reliability_flag": flag,
            "pilot_mean_panel_spread": ledger[item_id].get("pilot_mean_panel_spread"),
            "kin_mean_pairwise_disagreement": ledger[item_id].get("kin_mean_pairwise_disagreement"),
            "s8_mean_abs_j4_j5_delta": ledger[item_id].get("s8_mean_abs_j4_j5_delta"),
            "gpartition_category": ledger[item_id].get("gpartition_category"),
        }
        for i, (item_id, score, flag) in enumerate(scored_items[:15])
    ]

    # Steadfast-weakness check at item level
    # Compare mean max-normalized-disagreement by mold
    mold_scores: dict[str, list[float]] = defaultdict(list)
    for item_id, score, flag in scored_items:
        mold = item_to_mold(item_id)
        mold_scores[mold].append(score)

    mold_mean_disagreement = {
        mold: round(statistics.mean(scores), 4)
        for mold, scores in mold_scores.items()
        if scores
    }

    # Is steadfast worst vs contested?
    sted_mean = mold_mean_disagreement.get("steadfast")
    cont_mean = mold_mean_disagreement.get("contested")
    comp_mean = mold_mean_disagreement.get("complicit")
    v1_mean = mold_mean_disagreement.get("v1-kind")

    steadfast_weakness_check = {
        "mold_mean_max_normalized_disagreement": mold_mean_disagreement,
        "expected_ranking_from_slice_icc": "steadfast < contested (lower ICC = higher disagreement)",
        "steadfast_mean": sted_mean,
        "contested_mean": cont_mean,
        "complicit_mean": comp_mean,
        "v1_kind_mean": v1_mean,
        "steadfast_worse_than_contested_at_item_level": (
            sted_mean is not None and cont_mean is not None and sted_mean > cont_mean
        ),
        "note": (
            "Slice ICC ordering was steadfast(0.557) < contested(0.612) < overall(0.798). "
            "Item-level disagreement should reproduce this if the same instruments are consistent."
        ),
    }

    # LOW-AGREEMENT rate by mold (for consistency check)
    low_rate_by_mold = {}
    for mold, counts in flag_by_mold.items():
        total = sum(counts.values())
        low = counts.get("LOW-AGREEMENT", 0)
        low_rate_by_mold[mold] = {
            "n_items": total,
            "n_low_agreement": low,
            "pct_low_agreement": round(100 * low / total, 1) if total else None,
        }

    summary = {
        "_meta": {
            "script": "20260718-session11-dim5-reliability.py",
            "date": "2026-07-18",
            "n_items_in_ledger": len(ledger),
        },
        "flag_counts_overall": flag_counts_overall,
        "flag_counts_by_mold": {mold: dict(counts) for mold, counts in flag_by_mold.items()},
        "low_agreement_rate_by_mold": low_rate_by_mold,
        "flag_counts_n_core_items": dict(flag_n_core),
        "n_n_core_items": sum(flag_n_core.values()),
        "steadfast_weakness_check": steadfast_weakness_check,
        "top_15_worst_items": top_15,
        "_caveats": (
            "Disagreement magnitudes are era-specific: pilot panel (3 mixed LLM judges, session-5 bank) "
            "vs kin-matrix (5 graders, session-5 bank) vs s8 twin pairs (J4=claude-opus-4-8 and "
            "J5=gpt-5.5 on session-8 bank). Flags may compose across sources but raw magnitudes "
            "must not be averaged across eras. Single-judge J4×J5 deltas are stability-only signals, "
            "not full panel ICC. Items with only one source populated are less reliable flag candidates."
        ),
    }

    summary_path = base / "20260718-session11-dim5-summary.json"
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Summary written: {summary_path}")

    # Quick console report
    print()
    print("=== QUICK REPORT ===")
    print(f"Total items in ledger: {len(ledger)}")
    print(f"Flag counts (overall): {flag_counts_overall}")
    print()
    print("Flag counts by mold:")
    for mold, counts in sorted(flag_by_mold.items()):
        print(f"  {mold}: {dict(counts)}")
    print()
    print(f"-N- core items: {dict(flag_n_core)}")
    print()
    print("Mold mean max-normalized disagreement:")
    for mold, mean_d in sorted(mold_mean_disagreement.items(), key=lambda x: x[1], reverse=True):
        print(f"  {mold}: {mean_d:.4f}")
    print()
    print("Steadfast < contested reproduced:", steadfast_weakness_check["steadfast_worse_than_contested_at_item_level"])
    print()
    print("Top 5 worst items:")
    for entry in top_15[:5]:
        print(f"  #{entry['rank']} {entry['item_id']} ({entry['mold']}) "
              f"max_norm={entry['max_normalized_disagreement']:.3f} "
              f"flag={entry['reliability_flag']} "
              f"gcat={entry['gpartition_category']}")


if __name__ == "__main__":
    import os
    os.chdir(Path(__file__).parent)
    main()
