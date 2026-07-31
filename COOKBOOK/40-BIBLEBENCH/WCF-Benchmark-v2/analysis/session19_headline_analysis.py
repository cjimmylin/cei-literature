"""Session-19 first QUOTABLE analysis (boot prompt s19 section 3).

Computes, from the strict-v2 dual-judge full-run panel
(analysis/20260731-session18-perjudge.csv, 5,175 rows = 5 SUTs x 345 items x
3 epochs):

  1. Per-SUT panel means + per-judge (opus, Sol) sensitivity columns.
  2. Paired-epoch significance between every SUT pair, reusing the s7 MDD80
     method verbatim (analysis/compute_session7_epochs_stats.py): per-item
     epoch-averaged scores first, then a paired difference with
     mdd80 = 2.80 * se(diffs) (two-sided alpha=.05, power=.80 normal-approx).
  3. Per-mold (item-family prefix) breakdown per SUT.
  4. Frontier-core (146-item index, analysis/20260724-session13-frontier-core-index.json)
     vs full-bank breakdown per SUT.
  5. 3-epoch consistency: per-SUT mean absolute deviation of each epoch's
     score from that item's 3-epoch mean, to make explicit how noisy any
     single epoch would have been in isolation (WALKWORTHY lesson: don't
     quote single-epoch verdicts).

Output: analysis/20260731-session19-headline-analysis.json
"""

from __future__ import annotations

import csv
import json
import math
from collections import defaultdict
from pathlib import Path
from statistics import mean, stdev

WCF_ROOT = Path(__file__).resolve().parent.parent
PERJUDGE = WCF_ROOT / "analysis" / "20260731-session18-perjudge.csv"
FRONTIER_CORE = WCF_ROOT / "analysis" / "20260724-session13-frontier-core-index.json"
OUT = WCF_ROOT / "analysis" / "20260731-session19-headline-analysis.json"

SUTS = ["gpt-4o-mini", "gpt-5-mini", "haiku", "minimax-m3", "qwen"]


def mold(item_id: str) -> str:
    return item_id.split("-")[0]


def load_rows():
    rows = []
    with PERJUDGE.open() as f:
        for r in csv.DictReader(f):
            r["opus"] = int(r["opus"])
            r["sol"] = int(r["sol"])
            r["panel_mean"] = float(r["panel_mean"])
            r["gap"] = int(r["gap"])
            r["epoch"] = int(r["epoch"])
            rows.append(r)
    return rows


def per_sut_summary(rows, sut_filter=None):
    subset = [r for r in rows if sut_filter is None or r["sut"] in sut_filter]
    out = {}
    for sut in SUTS:
        cells = [r for r in subset if r["sut"] == sut]
        if not cells:
            continue
        out[sut] = {
            "n": len(cells),
            "panel_mean": round(mean(r["panel_mean"] for r in cells), 2),
            "opus_mean": round(mean(r["opus"] for r in cells), 2),
            "sol_mean": round(mean(r["sol"] for r in cells), 2),
            "opus_minus_sol_mean": round(mean(r["opus"] - r["sol"] for r in cells), 2),
            "opus_sol_stdev": round(stdev(r["panel_mean"] for r in cells), 2) if len(cells) > 1 else None,
        }
    return out


def item_epoch_means(rows, sut):
    """item_id -> mean panel_mean across its 3 epochs, for one SUT."""
    by_item = defaultdict(list)
    for r in rows:
        if r["sut"] == sut:
            by_item[r["item"]].append(r["panel_mean"])
    return {item_id: mean(vals) for item_id, vals in by_item.items()}


def paired_epoch_significance(rows):
    """s7 MDD80 method, reused verbatim: per-item epoch-averaged scores first,
    then paired difference per SUT pair over the common item set."""
    item_means = {sut: item_epoch_means(rows, sut) for sut in SUTS}
    pairs = {}
    for i, a in enumerate(SUTS):
        for b in SUTS[i + 1:]:
            common = sorted(set(item_means[a]) & set(item_means[b]))
            diffs = [item_means[a][x] - item_means[b][x] for x in common]
            se = stdev(diffs) / math.sqrt(len(diffs))
            mdd80 = 2.80 * se
            pairs[f"{a}-vs-{b}"] = {
                "n": len(common),
                "gap": round(mean(diffs), 2),
                "se_diff": round(se, 4),
                "mdd80": round(mdd80, 2),
                "significant_at_mdd80": abs(mean(diffs)) >= mdd80,
            }
    return pairs


def per_mold_breakdown(rows):
    molds = sorted({mold(r["item"]) for r in rows})
    out = {}
    for m in molds:
        cells = [r for r in rows if mold(r["item"]) == m]
        by_sut = {}
        for sut in SUTS:
            sc = [r["panel_mean"] for r in cells if r["sut"] == sut]
            if sc:
                by_sut[sut] = round(mean(sc), 2)
        out[m] = {"n_cells": len(cells), "n_items": len({r["item"] for r in cells}),
                   "panel_mean_by_sut": by_sut}
    return out


def frontier_core_breakdown(rows):
    fc_ids = set(json.loads(FRONTIER_CORE.read_text())["item_ids"])
    fc_rows = [r for r in rows if r["item"] in fc_ids]
    non_fc_rows = [r for r in rows if r["item"] not in fc_ids]
    return {
        "frontier_core_n_items": len(fc_ids),
        "frontier_core": per_sut_summary(fc_rows),
        "non_frontier_core": per_sut_summary(non_fc_rows),
    }


def epoch_consistency(rows):
    """Per-SUT mean absolute deviation of each epoch score from the item's
    3-epoch mean -- how noisy a single epoch would be in isolation."""
    out = {}
    for sut in SUTS:
        item_means = item_epoch_means(rows, sut)
        cells = [r for r in rows if r["sut"] == sut]
        abs_devs = [abs(r["panel_mean"] - item_means[r["item"]]) for r in cells]
        # also: how often does the single worst epoch differ from the 3-epoch mean by >= 15 pts
        big_dev_rate = sum(1 for d in abs_devs if d >= 15) / len(abs_devs)
        out[sut] = {
            "n_epoch_observations": len(cells),
            "mean_abs_deviation_from_3ep_mean": round(mean(abs_devs), 2),
            "pct_single_epoch_obs_off_by_15pt_or_more": round(big_dev_rate * 100, 1),
        }
    return out


def main() -> None:
    rows = load_rows()
    assert len(rows) == 5175, f"expected 5175 rows, got {len(rows)}"

    result = {
        "n_total_cells": len(rows),
        "per_sut_panel_and_judge_sensitivity": per_sut_summary(rows),
        "paired_epoch_significance_s7_mdd80_method": paired_epoch_significance(rows),
        "per_mold_breakdown": per_mold_breakdown(rows),
        "frontier_core_breakdown": frontier_core_breakdown(rows),
        "epoch_consistency": epoch_consistency(rows),
    }
    OUT.write_text(json.dumps(result, indent=2))
    print(json.dumps({
        "per_sut_panel_and_judge_sensitivity": result["per_sut_panel_and_judge_sensitivity"],
        "frontier_core_breakdown": {
            "frontier_core_n_items": result["frontier_core_breakdown"]["frontier_core_n_items"],
            "frontier_core": result["frontier_core_breakdown"]["frontier_core"],
            "non_frontier_core": result["frontier_core_breakdown"]["non_frontier_core"],
        },
    }, indent=2))
    print(f"\nfull output written to {OUT}")


if __name__ == "__main__":
    main()
