#!/usr/bin/env python3
"""
WCF-Benchmark-v2 session-5 Phase-1 item triage (EXPLORATORY / NON-QUOTABLE).

Input : analysis/20260716-session5-item-matrix.json (pilot block only for triage;
        s3_sweep used ONLY for a flagged supplementary appendix, never pooled).
Outputs:
  analysis/20260716-session5-item-triage.csv
  analysis/20260716-session5-item-triage-summary.json
  analysis/20260716-session5-panel-health.json
  (report written separately)

$0 logs-only. No API calls. Re-runnable.

Panel grader order (from panel_order_note):
  panel_g1 = gemini-2.5-flash
  panel_g2 = deepseek-chat
  panel_g3 = mistral-small-2603
n_valid=2 rows: the failed grader's panel_value is null; position preserved.
"""
import json
import csv
import os
from collections import defaultdict, Counter

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INP = os.path.join(BASE, "analysis", "20260716-session5-item-matrix.json")
OUT_CSV = os.path.join(BASE, "analysis", "20260716-session5-item-triage.csv")
OUT_SUM = os.path.join(BASE, "analysis", "20260716-session5-item-triage-summary.json")
OUT_PANEL = os.path.join(BASE, "analysis", "20260716-session5-panel-health.json")

TIER1 = ["qwen3.7-plus", "haiku-4.5", "kimi-k2"]
TIER2 = ["llama-4-maverick", "gpt-4o-mini"]
ALL_SUTS = TIER1 + TIER2
GRADERS = ["gemini-2.5-flash", "deepseek-chat", "mistral-small-2603"]  # g1,g2,g3


def mean(xs):
    xs = [x for x in xs if x is not None]
    return sum(xs) / len(xs) if xs else None


def spread(xs):
    xs = [x for x in xs if x is not None]
    return (max(xs) - min(xs)) if xs else None


def pearson(x, y):
    n = len(x)
    if n < 2:
        return None
    mx, my = sum(x) / n, sum(y) / n
    num = sum((a - mx) * (b - my) for a, b in zip(x, y))
    dx = sum((a - mx) ** 2 for a in x) ** 0.5
    dy = sum((b - my) ** 2 for b in y) ** 0.5
    if dx == 0 or dy == 0:
        return None
    return num / (dx * dy)


def load():
    d = json.load(open(INP))
    return d["pilot"], d.get("s3_sweep", []), d


def build_items(pilot):
    """Group rows by sample_id -> dict of per-SUT record."""
    items = defaultdict(dict)
    meta = {}
    for r in pilot:
        sid = r["sample_id"]
        items[sid][r["sut"]] = r
        if sid not in meta:
            meta[sid] = {
                "kind": r["kind"],
                "design": r["design"],
                "track": r["track"],
                "tier": r["tier"],
                "contested": r["contested"],
                "episode": r["episode"],
                "task": r["task"],
                "commandments": r["commandments"],
            }
    return items, meta


def triage():
    pilot, s3, raw = load()
    items, meta = build_items(pilot)
    assert len(items) == 221, f"expected 221 items, got {len(items)}"

    # SUT grand means (across all 221 items) for item-total r
    sut_scores = defaultdict(list)
    for sid in items:
        for sut in ALL_SUTS:
            sut_scores[sut].append(items[sid][sut]["score"])
    sut_grand_mean = {sut: mean(sut_scores[sut]) for sut in ALL_SUTS}
    grand_mean_vec = [sut_grand_mean[s] for s in ALL_SUTS]

    rows = []
    for sid in sorted(items):
        recs = items[sid]
        m = meta[sid]
        medians = {sut: recs[sut]["score"] for sut in ALL_SUTS}
        t1_med = [medians[s] for s in TIER1]
        t2_med = [medians[s] for s in TIER2]
        all_med = [medians[s] for s in ALL_SUTS]

        cross_sut_spread = spread(all_med)
        within_t1_spread = spread(t1_med)
        tier_gap = mean(t1_med) - mean(t2_med)

        # per-SUT panel spread (max-min of that SUT's valid panel values)
        per_sut_panel_spread = {}
        for sut in ALL_SUTS:
            pv = recs[sut]["panel_values"]
            per_sut_panel_spread[sut] = spread(pv)  # ignores None
        mean_panel_spread = mean(list(per_sut_panel_spread.values()))
        n_sut_spread_ge30 = sum(1 for v in per_sut_panel_spread.values()
                                if v is not None and v >= 30)

        # item-total r (exploratory, n=5): item's 5 scores vs SUT grand means
        item_vec = [medians[s] for s in ALL_SUTS]
        item_total_r = pearson(item_vec, grand_mean_vec)

        # --- CLASSIFICATION (exact rules, in order) ---
        if all(v == 100 for v in t1_med):
            cls = "DEAD-CEILING"
        elif (mean_panel_spread is not None
              and mean_panel_spread >= max(15, cross_sut_spread)) \
                or n_sut_spread_ge30 >= 2:
            cls = "NOISY"
        elif within_t1_spread is not None and within_t1_spread >= 10:
            cls = "CORE-DISCRIMINATING"
        else:
            cls = "TIER-BREAK-ONLY"

        flat = (cls == "TIER-BREAK-ONLY" and tier_gap < 15)

        rows.append({
            "sample_id": sid,
            "kind": m["kind"],
            "design": m["design"],
            "track": m["track"],
            "tier": m["tier"],
            "contested": m["contested"],
            "episode": m["episode"],
            "main_or_episode": "episode" if m["episode"] else "main",
            "score_qwen": medians["qwen3.7-plus"],
            "score_haiku": medians["haiku-4.5"],
            "score_kimi": medians["kimi-k2"],
            "score_llama": medians["llama-4-maverick"],
            "score_gpt4omini": medians["gpt-4o-mini"],
            "cross_sut_spread": round(cross_sut_spread, 3),
            "within_tier1_spread": round(within_t1_spread, 3),
            "tier_gap": round(tier_gap, 3),
            "mean_panel_spread": round(mean_panel_spread, 3) if mean_panel_spread is not None else "",
            "n_sut_panel_spread_ge30": n_sut_spread_ge30,
            "item_total_r_exploratory": round(item_total_r, 4) if item_total_r is not None else "",
            "triage_class": cls,
            "flat_no_discrim": flat,
        })

    # write CSV
    cols = list(rows[0].keys())
    with open(OUT_CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow(r)

    return rows, items, meta, sut_grand_mean


def summarize(rows):
    def crosstab(keyfn):
        c = defaultdict(lambda: defaultdict(int))
        for r in rows:
            c[r["triage_class"]][keyfn(r)] += 1
        return {k: dict(v) for k, v in c.items()}

    summary = {
        "note": "EXPLORATORY / NON-QUOTABLE. Session-5 Phase-1 triage of 221 pilot items.",
        "n_items": len(rows),
        "class_counts": dict(Counter(r["triage_class"] for r in rows)),
        "class_by_kind": crosstab(lambda r: r["kind"]),
        "class_by_design": crosstab(lambda r: r["design"]),
        "class_by_main_or_episode": crosstab(lambda r: r["main_or_episode"]),
        "flat_no_discrim_count": sum(1 for r in rows if r["flat_no_discrim"]),
        "dead_ceiling_by_kind": dict(Counter(
            r["kind"] for r in rows if r["triage_class"] == "DEAD-CEILING")),
        "core_discriminating_ids": [
            {"sample_id": r["sample_id"], "kind": r["kind"], "design": r["design"],
             "main_or_episode": r["main_or_episode"],
             "within_tier1_spread": r["within_tier1_spread"],
             "cross_sut_spread": r["cross_sut_spread"],
             "tier_gap": r["tier_gap"],
             "mean_panel_spread": r["mean_panel_spread"]}
            for r in rows if r["triage_class"] == "CORE-DISCRIMINATING"
        ],
    }
    json.dump(summary, open(OUT_SUM, "w"), indent=2)
    return summary


def anatomy(rows):
    """Deliverable 2: discrimination anatomy."""
    core = [r for r in rows if r["triage_class"] == "CORE-DISCRIMINATING"]
    n_core = len(core)
    core_ep = sum(1 for r in core if r["main_or_episode"] == "episode")
    ep_bank_share = 22 / 221

    def by(keyfn, subset=None):
        subset = subset or rows
        g = defaultdict(list)
        for r in subset:
            g[keyfn(r)].append(r)
        return {
            k: {
                "n": len(v),
                "mean_within_tier1_spread": round(mean([x["within_tier1_spread"] for x in v]), 3),
                "mean_tier_gap": round(mean([x["tier_gap"] for x in v]), 3),
            } for k, v in sorted(g.items())
        }

    # designs carrying discrimination: core share within each design
    design_core = defaultdict(lambda: {"total": 0, "core": 0})
    for r in rows:
        design_core[r["design"]]["total"] += 1
        if r["triage_class"] == "CORE-DISCRIMINATING":
            design_core[r["design"]]["core"] += 1
    design_core = {
        d: {**v, "core_share": round(v["core"] / v["total"], 4)}
        for d, v in sorted(design_core.items(),
                           key=lambda kv: -kv[1]["core"] / kv[1]["total"])
    }

    return {
        "core_count": n_core,
        "core_episode_count": core_ep,
        "core_episode_share_of_core": round(core_ep / n_core, 4) if n_core else None,
        "episode_share_of_bank": round(ep_bank_share, 4),
        "episode_enrichment_factor": (round((core_ep / n_core) / ep_bank_share, 3)
                                      if n_core and core_ep else 0.0),
        "by_kind": by(lambda r: r["kind"]),
        "by_main_or_episode": by(lambda r: r["main_or_episode"]),
        "designs_discrimination": design_core,
    }


def panel_health(pilot):
    """Deliverable 3: panel health from metadata only."""
    # per-grader delta from panel median, overall/by kind/by SUT
    deltas = {g: [] for g in GRADERS}
    deltas_by_kind = {g: defaultdict(list) for g in GRADERS}
    deltas_by_sut = {g: defaultdict(list) for g in GRADERS}
    lone_outlier = {g: 0 for g in GRADERS}
    lone_denom = 0  # rows where all 3 graders present (eligible for lone-outlier test)
    nvalid_lt3 = []

    for r in pilot:
        pv = r["panel_values"]
        med = r["score"]
        kind = r["kind"]
        sut = r["sut"]
        if r["panel_n_valid"] < 3:
            nvalid_lt3.append({"sut": sut, "sample_id": r["sample_id"],
                               "panel_values": pv,
                               "missing_grader": GRADERS[pv.index(None)]})
        for i, g in enumerate(GRADERS):
            v = pv[i]
            if v is None:
                continue
            deltas[g].append(v - med)
            deltas_by_kind[g][kind].append(v - med)
            deltas_by_sut[g][sut].append(v - med)

        # lone-outlier: needs all 3 present
        if all(x is not None for x in pv):
            lone_denom += 1
            for i in range(3):
                others = [pv[j] for j in range(3) if j != i]
                if abs(others[0] - others[1]) <= 15 and \
                        all(abs(pv[i] - o) >= 30 for o in others):
                    lone_outlier[GRADERS[i]] += 1

    def fmt(dmap):
        return {k: round(mean(v), 3) for k, v in dmap.items() if v}

    result = {
        "per_grader_mean_delta_overall": {g: round(mean(deltas[g]), 3) for g in GRADERS},
        "per_grader_mean_delta_by_kind": {g: fmt(deltas_by_kind[g]) for g in GRADERS},
        "per_grader_mean_delta_by_sut": {g: fmt(deltas_by_sut[g]) for g in GRADERS},
        "lone_outlier_counts": lone_outlier,
        "lone_outlier_denominator_all3present": lone_denom,
        "lone_outlier_rates": {g: round(lone_outlier[g] / lone_denom, 4)
                               for g in GRADERS},
        "n_valid_lt3_count": len(nvalid_lt3),
        "n_valid_lt3_rows": nvalid_lt3,
        "gemini_mean_delta_patched_bank": round(mean(deltas["gemini-2.5-flash"]), 3),
        "gemini_session3_old_bank_reference": -8.6,
    }
    json.dump(result, open(OUT_PANEL, "w"), indent=2)
    return result


def s3_supplementary(s3):
    """s3_sweep supplementary appendix ONLY. NEVER pooled with pilot."""
    # s3 has no panel/score column in the same schema? check fields
    if not s3:
        return {"note": "no s3_sweep rows"}
    # s3 rows: config_era flag; single-grader old bank
    suts = Counter(r["sut"] for r in s3)
    kinds = Counter(r["kind"] for r in s3)
    items = set(r["sample_id"] for r in s3)
    has_score = "score" in s3[0]
    return {
        "config_break_flag": "s3-single-grader-old-bank — 204+22 item bank, 4 SUTs, "
                             "single grader. DIFFERENT CONFIG ERA. Never pooled with pilot.",
        "n_rows": len(s3),
        "n_unique_items": len(items),
        "suts": dict(suts),
        "kinds": dict(kinds),
        "has_score_field": has_score,
    }


def main():
    pilot, s3, raw = load()
    rows, items, meta, grand = triage()
    summary = summarize(rows)
    anat = anatomy(rows)
    ph = panel_health(pilot)
    s3supp = s3_supplementary(s3)

    # attach anatomy + s3 supp into summary json for the report to read
    summary["discrimination_anatomy"] = anat
    summary["s3_sweep_supplementary"] = s3supp
    summary["sut_grand_means"] = {k: round(v, 3) for k, v in grand.items()}
    json.dump(summary, open(OUT_SUM, "w"), indent=2)

    print("=== CLASS COUNTS ===")
    for k, v in summary["class_counts"].items():
        print(f"  {k}: {v}")
    print("core:", anat["core_count"], "core-episodes:", anat["core_episode_count"],
          "enrichment:", anat["episode_enrichment_factor"])
    print("gemini mean delta (patched):", ph["gemini_mean_delta_patched_bank"])
    print("n_valid<3:", ph["n_valid_lt3_count"])
    print("lone-outlier:", ph["lone_outlier_counts"], "/", ph["lone_outlier_denominator_all3present"])
    print("wrote:", OUT_CSV, OUT_SUM, OUT_PANEL)


if __name__ == "__main__":
    main()
