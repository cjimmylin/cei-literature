"""Session-19 mandatory judge-gap triage (boot prompt s19 section 2).

Selects a stratified sample from the 314 |opus-Sol gap| >= 30 cells (out of
5,175) in the strict-v2 full-run panel, stratified across SUT x mold (item
family prefix, e.g. AGG/COMP/CONT/...) so no single SUT or mold dominates the
audited set. Proportional allocation (largest-remainder method) targeting
TARGET_N total, minimum 1 per nonzero stratum, capped at stratum population.
Within-stratum selection is a seeded uniform sample (no replacement) over the
whole |gap|>=30 population in that stratum -- not biased toward the most
extreme gaps, since the analysis population of interest already IS the
|gap|>=30 set.

Deterministic and reproducible: seed documented below, re-running this script
reproduces the identical sample.

Output: SELECTION.json under /tmp/wcf-s19-triage-meta/ (selection metadata,
including existing opus/Sol/panel/gap scores -- kept OUT of the audit packets
per anti-leakage discipline). Packet building is a separate script
(session19_judge_gap_triage_packets.py) that reads this file.
"""

from __future__ import annotations

import csv
import json
import random
from collections import defaultdict
from pathlib import Path

WCF_ROOT = Path(__file__).resolve().parent.parent
PERJUDGE = WCF_ROOT / "analysis" / "20260731-session18-perjudge.csv"
META_DIR = Path("/tmp/wcf-s19-triage-meta")
GAP_THRESHOLD = 30
TARGET_N = 90
SEED = 19


def mold(item_id: str) -> str:
    return item_id.split("-")[0]


def main() -> None:
    META_DIR.mkdir(parents=True, exist_ok=True)
    rows = []
    with PERJUDGE.open() as f:
        for row in csv.DictReader(f):
            row["gap"] = int(row["gap"])
            rows.append(row)

    big = [r for r in rows if abs(r["gap"]) >= GAP_THRESHOLD]

    strata = defaultdict(list)
    for r in big:
        strata[(r["sut"], mold(r["item"]))].append(r)

    total_pop = len(big)
    frac = TARGET_N / total_pop

    # largest-remainder allocation, minimum 1 per stratum, capped at population
    alloc = {}
    remainders = []
    for key, members in strata.items():
        p = len(members)
        raw = p * frac
        base = max(1, int(raw))
        base = min(base, p)
        alloc[key] = base
        remainders.append((raw - int(raw), key, p))

    current_total = sum(alloc.values())
    remainders.sort(key=lambda t: -t[0])
    i = 0
    while current_total < TARGET_N and i < len(remainders):
        _, key, p = remainders[i]
        if alloc[key] < p:
            alloc[key] += 1
            current_total += 1
        i += 1
        if i >= len(remainders):
            i = 0
            if all(alloc[k] >= len(v) for k, v in strata.items()):
                break  # exhausted whole population

    rng = random.Random(SEED)
    picks = []
    for key, members in strata.items():
        n = alloc[key]
        chosen = rng.sample(members, n)
        for r in chosen:
            picks.append({
                "item": r["item"],
                "sut": r["sut"],
                "epoch": r["epoch"],
                "mold": key[1],
                "opus": int(r["opus"]),
                "sol": int(r["sol"]),
                "panel_mean": float(r["panel_mean"]),
                "gap": r["gap"],
            })

    picks.sort(key=lambda p: (p["sut"], p["mold"], p["item"], p["epoch"]))

    summary = {
        "gap_threshold": GAP_THRESHOLD,
        "total_population": total_pop,
        "target_n": TARGET_N,
        "actual_n": len(picks),
        "seed": SEED,
        "n_strata": len(strata),
        "allocation": {f"{k[0]}__{k[1]}": {"population": len(strata[k]), "sampled": alloc[k]}
                       for k in sorted(strata)},
    }
    out = {"summary": summary, "picks": picks}
    (META_DIR / "SELECTION.json").write_text(json.dumps(out, indent=2))
    print(json.dumps(summary, indent=2))
    print(f"\nwrote {len(picks)} picks to {META_DIR / 'SELECTION.json'}")


if __name__ == "__main__":
    main()
