#!/usr/bin/env python
"""Stream B agreement stats + verdict (EXPLORATORY / NON-QUOTABLE).

Reads the grade matrix written by regrade_graders.py and emits:
  - per-grader means (overall + per SUT + episodes-only)
  - pairwise mean absolute difference (gemini-deepseek, gemini-mistral, deepseek-mistral)
  - Spearman rho for each pair
  - count of samples with >=30-point spread across the 3 graders
  - haiku-vs-4o-mini gap under each grader (sign + magnitude)
  - episode 100-ceiling survival for haiku under each grader
  - single-grader stability verdict

Usage: ./.venv-v2/bin/python analysis/analyze_grader_bound.py [matrix.json]
Writes: analysis/<date>-streamB-agreement-stats.json
"""
from __future__ import annotations

import glob
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

V2_ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = V2_ROOT / "analysis"
GRADERS = ["gemini", "deepseek", "mistral"]
HAIKU = "openrouter/anthropic/claude-haiku-4.5"
MINI = "openrouter/openai/gpt-4o-mini"


def spearman(xs, ys):
    """Spearman rho with average ranks; pairs must be complete."""
    pairs = [(x, y) for x, y in zip(xs, ys) if x is not None and y is not None]
    n = len(pairs)
    if n < 3:
        return None
    def rank(vals):
        order = sorted(range(len(vals)), key=lambda i: vals[i])
        r = [0.0] * len(vals)
        i = 0
        while i < len(vals):
            j = i
            while j + 1 < len(vals) and vals[order[j + 1]] == vals[order[i]]:
                j += 1
            avg = (i + j) / 2 + 1
            for k in range(i, j + 1):
                r[order[k]] = avg
            i = j + 1
        return r
    rx = rank([p[0] for p in pairs])
    ry = rank([p[1] for p in pairs])
    mx = sum(rx) / n
    my = sum(ry) / n
    cov = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    vx = sum((a - mx) ** 2 for a in rx) ** 0.5
    vy = sum((b - my) ** 2 for b in ry) ** 0.5
    if vx == 0 or vy == 0:
        return None
    return round(cov / (vx * vy), 4)


def mean(vals):
    vals = [v for v in vals if v is not None]
    return round(sum(vals) / len(vals), 2) if vals else None


def mad(xs, ys):
    pairs = [(x, y) for x, y in zip(xs, ys) if x is not None and y is not None]
    if not pairs:
        return None, 0
    return round(sum(abs(a - b) for a, b in pairs) / len(pairs), 2), len(pairs)


def main():
    if len(sys.argv) > 1:
        mpath = Path(sys.argv[1])
    else:
        cands = sorted(glob.glob(str(OUT_DIR / "*-streamB-grade-matrix.json")))
        mpath = Path(cands[-1])
    data = json.load(open(mpath))
    rows = data["matrix"]

    def subset(pred):
        return [r for r in rows if pred(r)]

    def grader_means(rs):
        return {g: mean([r[g] for r in rs]) for g in GRADERS}

    result = {
        "_meta": {
            "generated": datetime.now(timezone.utc).isoformat(),
            "banner": "EXPLORATORY / NON-QUOTABLE",
            "source_matrix": mpath.name,
            "n_rows": len(rows),
        },
        "coverage": {
            "n_total": len(rows),
            "unparseable": {g: sum(1 for r in rows if r[g] is None) for g in GRADERS},
        },
    }

    # per-grader means: overall, per SUT, episodes-only per SUT
    result["means"] = {
        "overall": grader_means(rows),
        "gpt-4o-mini": grader_means(subset(lambda r: r["sut"] == MINI)),
        "haiku-4.5": grader_means(subset(lambda r: r["sut"] == HAIKU)),
        "episodes_gpt-4o-mini": grader_means(
            subset(lambda r: r["sut"] == MINI and r["task"] == "wcf_episodes")),
        "episodes_haiku-4.5": grader_means(
            subset(lambda r: r["sut"] == HAIKU and r["task"] == "wcf_episodes")),
    }

    # pairwise agreement (overall + per SUT)
    def pair_stats(rs):
        out = {}
        for a, b in [("gemini", "deepseek"), ("gemini", "mistral"), ("deepseek", "mistral")]:
            m, n = mad([r[a] for r in rs], [r[b] for r in rs])
            rho = spearman([r[a] for r in rs], [r[b] for r in rs])
            out[f"{a}-{b}"] = {"mad": m, "spearman": rho, "n": n}
        return out

    result["agreement"] = {
        "overall": pair_stats(rows),
        "gpt-4o-mini": pair_stats(subset(lambda r: r["sut"] == MINI)),
        "haiku-4.5": pair_stats(subset(lambda r: r["sut"] == HAIKU)),
    }

    # >=30-point spread across the 3 graders
    def spread(r):
        vals = [r[g] for g in GRADERS if r[g] is not None]
        return (max(vals) - min(vals)) if len(vals) == 3 else None

    spread_rows = []
    for r in rows:
        sp = spread(r)
        if sp is not None and sp >= 30:
            spread_rows.append({
                "sample_id": r["sample_id"], "sut": r["sut"].split("/")[-1],
                "design": r["design"], "kind": r["kind"],
                "gemini": r["gemini"], "deepseek": r["deepseek"], "mistral": r["mistral"],
                "spread": sp,
            })
    result["spread_ge30"] = {
        "count": len(spread_rows),
        "of_complete": sum(1 for r in rows if spread(r) is not None),
        "samples": sorted(spread_rows, key=lambda x: -x["spread"]),
    }

    # haiku - mini gap under each grader
    gap = {}
    for g in GRADERS:
        h = mean([r[g] for r in rows if r["sut"] == HAIKU])
        m = mean([r[g] for r in rows if r["sut"] == MINI])
        gap[g] = {"haiku": h, "mini": m, "gap": round(h - m, 2) if h is not None and m is not None else None}
    result["haiku_minus_mini_gap"] = gap
    signs = {v["gap"] > 0 for v in gap.values() if v["gap"] is not None}
    result["gap_survives"] = (signs == {True})  # haiku > mini under ALL graders

    # episode ceiling: haiku episodes scored exactly 100, per grader
    hep = subset(lambda r: r["sut"] == HAIKU and r["task"] == "wcf_episodes")
    result["haiku_episode_ceiling"] = {
        g: {
            "n": len(hep),
            "at_100": sum(1 for r in hep if r[g] == 100),
            "mean": mean([r[g] for r in hep]),
        } for g in GRADERS
    }

    # VERDICT
    mads = [result["agreement"]["overall"][k]["mad"] for k in result["agreement"]["overall"]]
    mads = [m for m in mads if m is not None]
    max_mad = max(mads) if mads else None
    rank_flip = not result["gap_survives"]
    unstable = (max_mad is not None and max_mad > 10) or rank_flip
    result["verdict"] = {
        "max_pairwise_mad": max_mad,
        "rank_flip": rank_flip,
        "single_grader_unstable": unstable,
        "recommendation": (
            "ADOPT majority-vote scorer (model=[gemini,deepseek,mistral])"
            if unstable else
            "RECORD grader-effect bound; KEEP single gemini grader"
        ),
    }

    stamp = datetime.now(timezone.utc).strftime("%Y%m%d")
    out = OUT_DIR / f"{stamp}-streamB-agreement-stats.json"
    json.dump(result, open(out, "w"), indent=2)
    print(json.dumps(result, indent=2))
    print(f"\nWrote {out}")


if __name__ == "__main__":
    main()
