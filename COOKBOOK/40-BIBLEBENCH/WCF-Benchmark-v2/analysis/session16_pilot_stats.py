#!/usr/bin/env python3
"""Session-16 B2: aggregate the pilot panel verdicts (3 SUTs x 146 frontier-core
items x 2 frozen judges, single-packet mode).

Reads /tmp/wcf-s16-pilot/{opus,sol}/<ITEM>__<sut>.md, parses the strict
last-match GRADE contract, and writes:
  - analysis/20260725-session16-pilot-panel.json  (per-cell table + summaries)
  - logs/20260724-session16-pilot/wcf-s16-pilot-{opus,sol}-grades.csv

ALL NUMBERS EXPLORATORY / NON-QUOTABLE (pilot; paper numbers come only from the
authorized full run). Pure stdlib, $0.
"""

from __future__ import annotations

import json
import re
import statistics
from pathlib import Path

WCF_ROOT = Path(__file__).resolve().parent.parent
PILOT = Path("/tmp/wcf-s16-pilot")
OUT_JSON = WCF_ROOT / "analysis" / "20260725-session16-pilot-panel.json"
LOG_DIR = WCF_ROOT / "logs" / "20260724-session16-pilot"
GRADE_RE = re.compile(r"GRADE:\s*(\d+)")
SUTS = ("gpt-4o-mini", "gpt-5-mini", "minimax-m3")


def parse(path: Path):
    if not path.exists():
        return None
    m = GRADE_RE.findall(path.read_text())
    return int(m[-1]) if m else None


def main() -> None:
    items = sorted({p.name.split("__")[0] for p in (PILOT / "packets").glob("*.md")})
    cells = {}
    missing = []
    for iid in items:
        for sut in SUTS:
            rec = {}
            for judge in ("opus", "sol"):
                g = parse(PILOT / judge / f"{iid}__{sut}.md")
                rec[judge] = g
                if g is None:
                    missing.append(f"{judge}/{iid}__{sut}")
            if rec["opus"] is not None and rec["sol"] is not None:
                rec["panel"] = (rec["opus"] + rec["sol"]) / 2
            cells[f"{iid}__{sut}"] = rec

    # summaries (exploratory)
    def sut_summary(sut):
        vals = [c["panel"] for k, c in cells.items()
                if k.endswith(f"__{sut}") and "panel" in c]
        by_judge = {j: [c[j] for k, c in cells.items()
                        if k.endswith(f"__{sut}") and c[j] is not None]
                    for j in ("opus", "sol")}
        molds = {}
        for k, c in cells.items():
            if not k.endswith(f"__{sut}") or "panel" not in c:
                continue
            mold = k.split("-N-")[0]
            molds.setdefault(mold, []).append(c["panel"])
        return {
            "n": len(vals),
            "panel_mean": round(statistics.mean(vals), 1) if vals else None,
            "panel_median": round(statistics.median(vals), 1) if vals else None,
            "judge_means": {j: round(statistics.mean(v), 1) if v else None
                            for j, v in by_judge.items()},
            "per_mold_panel_mean": {m: round(statistics.mean(v), 1)
                                    for m, v in sorted(molds.items())},
            "floor_cells_le15": sum(1 for v in vals if v <= 15),
            "ceiling_cells_ge95": sum(1 for v in vals if v >= 95),
        }

    # pairwise nonzero-gap counts (the gate-style discrimination statistic)
    def gaps(a, b):
        nz = at5 = n = 0
        for iid in items:
            ca, cb = cells.get(f"{iid}__{a}"), cells.get(f"{iid}__{b}")
            if not ca or not cb or "panel" not in ca or "panel" not in cb:
                continue
            n += 1
            d = abs(ca["panel"] - cb["panel"])
            nz += d > 0
            at5 += d >= 5
        return {"n": n, "nonzero": nz, "ge5": at5}

    out = {
        "name": "WCF-Bench-v2 session-16 pilot panel table (EXPLORATORY / NON-QUOTABLE)",
        "date": "2026-07-25",
        "design": "3 new SUTs x 146 frontier-core x 1 epoch; frozen instrument (strict-v2, opus+Sol mean-of-2, single-packet mode)",
        "missing_or_unparsed": missing,
        "per_sut": {s: sut_summary(s) for s in SUTS},
        "pairwise_gaps": {
            "minimax-m3_vs_gpt-5-mini": gaps("minimax-m3", "gpt-5-mini"),
            "minimax-m3_vs_gpt-4o-mini": gaps("minimax-m3", "gpt-4o-mini"),
            "gpt-5-mini_vs_gpt-4o-mini": gaps("gpt-5-mini", "gpt-4o-mini"),
        },
        "cells": cells,
    }
    OUT_JSON.write_text(json.dumps(out, indent=1))
    for judge in ("opus", "sol"):
        rows = [f"{k},{c[judge]}" for k, c in sorted(cells.items())
                if c[judge] is not None]
        (LOG_DIR / f"wcf-s16-pilot-{judge}-grades.csv").write_text(
            "\n".join(rows) + "\n")
    print(f"wrote {OUT_JSON.name}; missing/unparsed: {len(missing)}")
    print(json.dumps({k: v for k, v in out.items() if k in ("per_sut", "pairwise_gaps")}, indent=1))


if __name__ == "__main__":
    main()
