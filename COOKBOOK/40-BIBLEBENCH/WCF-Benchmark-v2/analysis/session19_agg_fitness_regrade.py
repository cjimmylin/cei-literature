"""Session-19 standing regrade: does 'fit-now' rise from 84 after the s14
gold_order char-split fix (wcf_tasks.py:96)?

Background: 5 AGG items carry gold_order as the STRING sentinel "declines total
order" (no total order exists among the ranked options). Before the s14 fix
(commit 5a449a4a9, 2026-07-24), render_standard() did `" < ".join(record["gold_order"])`
unconditionally -- str.join() on a *string* iterates its characters, so these 5
items were judged against a nonsense char-split "GOLD ORDER" line, not an error.
The s11 item-assessment master ledger (dim2 discrimination x dim5 reliability)
classified all 5 as WEAK / LOW-AGREEMENT off pilot-era data carrying that bug
(pilot_mean_panel_spread 27-46.8, evidence_era=['pilot']) -- none counted toward
the 84/287 "fit" (DISCRIMINATING and OK) count.

The s14 fix landed BEFORE the session-17 Scenario-A full run was rendered, so
the 5,175-response full run already scored these 5 items correctly. This script
re-applies the s11 dim2/dim5 classification RULES (thresholds only, not the
original multi-source pilot/kin/s8 formula -- see CAVEATS) to the new full-run
data to answer the standing question directly.

CAVEATS (why this is an analog, not a literal re-run of dim2/dim5):
  - dim2's original s8_cross_sut_spread used s8-era logs; here cross_sut_spread
    is computed from this session's 5-SUT x 3-epoch panel means (richer, but a
    different era/roster).
  - dim5's original pilot_mean_panel_spread averaged max-min spread over a
    3-5-grader panel per row; here the panel is 2 judges (opus, Sol), so the
    per-row spread degenerates to |opus - sol| directly. Same >=30 threshold
    applied for comparability, disclosed as a proxy metric.
  - pilot_triage_class / kin_mapd / s8_delta (other dim2/dim5 inputs) are not
    recomputed -- only the two threshold rules that are answerable from this
    session's panel data are re-applied.

Output: analysis/20260731-session19-agg-fitness-regrade.json
"""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

WCF_ROOT = Path(__file__).resolve().parent.parent
PERJUDGE = WCF_ROOT / "analysis" / "20260731-session18-perjudge.csv"
LEDGER = WCF_ROOT / "analysis" / "20260718-session11-master-ledger.json"
OUT = WCF_ROOT / "analysis" / "20260731-session19-agg-fitness-regrade.json"

TARGET_ITEMS = [
    "AGG-C3-003", "AGG-C4-W202", "AGG-C7-007", "AGG-C5-W304", "AGG-C8-W305",
]
DISCRIMINATING_SPREAD_THRESHOLD = 15.0  # dim2 s8_cross_sut_spread >= 15
LOW_AGREEMENT_SPREAD_THRESHOLD = 30.0   # dim5 pilot_mean_panel_spread >= 30


def main() -> None:
    rows_by_item = defaultdict(list)
    with PERJUDGE.open() as f:
        for row in csv.DictReader(f):
            if row["item"] in TARGET_ITEMS:
                rows_by_item[row["item"]].append(row)

    ledger = json.loads(LEDGER.read_text())["items"]
    fit_now_baseline = 84  # s11 master ledger crosstab: discrimination_x_reliability.DISCRIMINATING/OK

    results = {}
    n_now_fit = 0
    n_previously_fit = 0
    for item in TARGET_ITEMS:
        rows = rows_by_item[item]
        assert len(rows) == 15, f"{item}: expected 15 rows (5 SUT x 3 epoch), got {len(rows)}"

        by_sut = defaultdict(list)
        abs_gaps = []
        for r in rows:
            by_sut[r["sut"]].append(float(r["panel_mean"]))
            abs_gaps.append(abs(int(r["gap"])))
        sut_means = {sut: round(sum(v) / len(v), 2) for sut, v in by_sut.items()}
        cross_sut_spread = round(max(sut_means.values()) - min(sut_means.values()), 2)
        mean_judge_spread = round(sum(abs_gaps) / len(abs_gaps), 2)
        max_judge_spread = max(abs_gaps)

        discriminating = cross_sut_spread >= DISCRIMINATING_SPREAD_THRESHOLD
        ok_agreement = mean_judge_spread < LOW_AGREEMENT_SPREAD_THRESHOLD
        fit_now = discriminating and ok_agreement

        old = ledger.get(item, {})
        old_dim2 = old.get("dim2", {}).get("discrimination_verdict")
        old_dim5 = old.get("dim5", {}).get("reliability_flag")
        old_fit = (old_dim2 == "DISCRIMINATING") and (old_dim5 == "OK")
        n_previously_fit += int(old_fit)
        n_now_fit += int(fit_now)

        results[item] = {
            "s11_pre_fix": {
                "discrimination_verdict": old_dim2,
                "reliability_flag": old_dim5,
                "pilot_mean_panel_spread": old.get("dim5", {}).get(
                    "key_disagreement_numbers", {}
                ).get("pilot_mean_panel_spread"),
                "fit": old_fit,
            },
            "s19_post_fix_fullrun": {
                "cross_sut_spread": cross_sut_spread,
                "sut_means": sut_means,
                "discrimination_verdict": "DISCRIMINATING" if discriminating else "WEAK",
                "mean_abs_opus_sol_gap": mean_judge_spread,
                "max_abs_opus_sol_gap": max_judge_spread,
                "reliability_flag": "OK" if ok_agreement else "LOW-AGREEMENT",
                "fit": fit_now,
            },
        }

    delta = n_now_fit - n_previously_fit
    summary = {
        "question": "does fit-now rise from 84 after the s14 gold_order char-split fix?",
        "fit_now_baseline_s11": fit_now_baseline,
        "n_target_items": len(TARGET_ITEMS),
        "n_of_5_previously_fit_s11": n_previously_fit,
        "n_of_5_fit_post_fix_s19": n_now_fit,
        "delta": delta,
        "fit_now_regraded_estimate": fit_now_baseline + delta,
        "answer": (
            f"YES -- fit-now rises from {fit_now_baseline} to an estimated "
            f"{fit_now_baseline + delta} ({n_now_fit}/5 of the string-sentinel AGG "
            "items now classify DISCRIMINATING+OK under the fixed renderer, vs "
            f"{n_previously_fit}/5 before)"
            if delta > 0 else
            f"NO CHANGE -- fit-now remains {fit_now_baseline} "
            f"({n_now_fit}/5 fit post-fix vs {n_previously_fit}/5 before)"
        ),
        "caveats": [
            "This is a threshold-rule analog applied to new-era 5-SUT x 3-epoch full-run "
            "data, not a literal re-run of dim2/dim5's original multi-source (pilot+kin+s8) "
            "formula -- see module docstring.",
            "2-judge (opus, Sol) per-row spread substitutes for the original 3-5-grader "
            "panel spread at the same >=30 threshold.",
            "The wider 84/287 ledger (282 other items) was NOT recomputed -- only the 5 "
            "items whose classification was directly attributable to the char-split bug.",
        ],
    }

    OUT.write_text(json.dumps({"summary": summary, "items": results}, indent=2))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
