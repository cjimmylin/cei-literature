#!/usr/bin/env python3
"""Session-16 A3: aggregate the 120-verdict judge-stability repeat study.

Reads the 20-cell x 3-repeat x 2-judge verdict files from /tmp/wcf-s16-a3/
(opus/ = fresh Agent contexts, sol/ = fresh codex exec processes), parses the
strict last-match GRADE contract, and computes per-judge and panel-mean
test-retest statistics:

  - full repeat matrix (cell x judge x repeat)
  - per-cell repeat SD (population SD over k=3) and max spread
  - per-judge summaries: median/mean SD, worst cell, % zero-spread cells
  - ICC(2,1) (two-way random effects, absolute agreement, single measurement)
    treating repeats as exchangeable "raters" over the 20 cells — the
    LLM-only test-retest number per the vault no-human-raters directive
  - panel-mean series (mean of the two judges within repeat index)

Writes analysis/20260724-session16-judge-stability.json (the paper's
instrument-reliability deliverable). Pure stdlib; no API calls.
"""

from __future__ import annotations

import json
import re
import statistics
from pathlib import Path

WCF_ROOT = Path(__file__).resolve().parent.parent
A3 = Path("/tmp/wcf-s16-a3")
META = Path("/tmp/wcf-s16-a3-meta/MANIFEST.json")
OUT = WCF_ROOT / "analysis" / "20260724-session16-judge-stability.json"
GRADE_RE = re.compile(r"GRADE:\s*(\d+)")
REPEATS = 3


def parse_grade(path: Path):
    if not path.exists():
        return None
    m = GRADE_RE.findall(path.read_text())
    return int(m[-1]) if m else None


def icc_2_1(rows):
    """ICC(2,1): rows = list of [k measurements]; two-way random, absolute."""
    n = len(rows)
    k = len(rows[0])
    grand = sum(sum(r) for r in rows) / (n * k)
    row_means = [sum(r) / k for r in rows]
    col_means = [sum(r[j] for r in rows) / n for j in range(k)]
    ss_rows = k * sum((m - grand) ** 2 for m in row_means)
    ss_cols = n * sum((m - grand) ** 2 for m in col_means)
    ss_tot = sum((x - grand) ** 2 for r in rows for x in r)
    ss_err = ss_tot - ss_rows - ss_cols
    msr = ss_rows / (n - 1)
    msc = ss_cols / (k - 1)
    mse = ss_err / ((n - 1) * (k - 1))
    denom = msr + (k - 1) * mse + k * (msc - mse) / n
    return (msr - mse) / denom if denom else float("nan")


def main() -> None:
    manifest = json.loads(META.read_text())
    matrix = []
    missing = []
    for m in manifest:
        cell = m["cell"]
        row = {"cell": cell, "item": m["item"], "sut": m["sut"],
               "source": m["source"], "panel_s15_reference": m["panel_s15"]}
        for judge in ("opus", "sol"):
            grades = []
            for r in range(1, REPEATS + 1):
                g = parse_grade(A3 / judge / f"{cell}-r{r}.md")
                if g is None:
                    missing.append(f"{judge}/{cell}-r{r}")
                grades.append(g)
            row[judge] = grades
            if all(g is not None for g in grades):
                row[f"{judge}_sd"] = round(statistics.pstdev(grades), 2)
                row[f"{judge}_spread"] = max(grades) - min(grades)
        if all(g is not None for g in row["opus"] + row["sol"]):
            row["panel_mean"] = [round((row["opus"][r] + row["sol"][r]) / 2, 1)
                                 for r in range(REPEATS)]
            row["panel_sd"] = round(statistics.pstdev(row["panel_mean"]), 2)
            row["panel_spread"] = round(max(row["panel_mean"]) - min(row["panel_mean"]), 1)
        matrix.append(row)

    summary = {}
    for series, key in (("opus", "opus"), ("sol", "sol"), ("panel_mean", "panel")):
        rows = [r[series] for r in matrix if series in r and all(
            g is not None for g in r.get(series, [None]))]
        sds = [r[f"{key}_sd"] for r in matrix if f"{key}_sd" in r]
        spreads = [r[f"{key}_spread"] for r in matrix if f"{key}_spread" in r]
        worst = max((r for r in matrix if f"{key}_spread" in r),
                    key=lambda r: r[f"{key}_spread"])
        summary[key] = {
            "n_cells": len(rows),
            "icc_2_1_repeats_as_raters": round(icc_2_1(rows), 4),
            "median_repeat_sd": round(statistics.median(sds), 2),
            "mean_repeat_sd": round(statistics.mean(sds), 2),
            "max_spread": max(spreads),
            "worst_cell": {"cell": worst["cell"], "item": worst["item"],
                           "sut": worst["sut"], "values": worst[series]},
            "pct_zero_spread_cells": round(
                100 * sum(1 for s in spreads if s == 0) / len(spreads), 1),
        }

    out = {
        "name": "WCF-Bench-v2 session-16 judge-stability repeat study (A3)",
        "date": "2026-07-24",
        "design": ("20 stratified cells (14 truth-bench + 6 non-bench from the "
                   "s13 gate logs) x 3 repeats x 2 judges = 120 verdicts; "
                   "frozen instrument (strict-v2 template, opus Agent fresh "
                   "context per verdict, gpt-5.6-sol codex exec high effort "
                   "fresh process per verdict); identical packet bytes per "
                   "repeat; $0 API"),
        "parse_failures": missing,
        "summary": summary,
        "note": ("LLM-only test-retest per vault no-human-raters directive. "
                 "panel_s15_reference values are the s15 gate-arm panel means "
                 "recorded for stratification ONLY — the s15 gate arm judged in "
                 "SUT-pure batches of 8, so s15-vs-A3 level differences "
                 "confound repeat noise with the batched-vs-single-packet mode "
                 "effect; do not read them as the same measurement."),
        "matrix": matrix,
    }
    OUT.write_text(json.dumps(out, indent=1))
    print(f"wrote {OUT.name}")
    print(json.dumps(summary, indent=1))
    if missing:
        print(f"MISSING: {missing}")


if __name__ == "__main__":
    main()
