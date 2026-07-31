#!/usr/bin/env python3
"""Bank-composition stats for the session-20 paper draft.

Recomputes every composition figure cited in the paper's "Benchmark
Composition & Taxonomy" section directly from the frozen v2.5 bank, so
none of those numbers rests on hand-counting. Read-only: no judging, no
scoring, no mutation of any file.
"""
import json
import re
import collections
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BANK = ROOT / "data" / "wcf_main.jsonl"
FRONTIER_CORE = ROOT / "analysis" / "20260724-session13-frontier-core-index.json"
OUT = ROOT / "analysis" / "20260731-session20-composition-stats.json"


def family_of(item_id):
    return re.match(r"^([A-Z]+)-", item_id).group(1)


def main():
    items = {}
    with open(BANK) as f:
        for line in f:
            d = json.loads(line)
            items[d["id"]] = d

    n_total = len(items)
    track = collections.Counter(d.get("track") for d in items.values())
    kind = collections.Counter(d.get("kind") for d in items.values())
    tier = collections.Counter(d.get("tier") for d in items.values())
    authored = sum(1 for d in items.values() if d.get("authored"))
    v1_derived = n_total - authored
    gate_count = sum(1 for d in items.values() if "GATE:" in (d.get("key") or ""))
    no_deliverable = sum(
        1
        for d in items.values()
        if "no-deliverable" in (d.get("key") or "").lower()
        or "no deliverable" in (d.get("key") or "").lower()
    )
    axis_manner = sum(
        1
        for d in items.values()
        if any(c.get("axis") == "manner" for c in d.get("rubric", []))
    )
    recall_hybrid = sum(1 for d in items.values() if d.get("recall_hybrid"))

    criteria_counts = [len(d.get("rubric", [])) for d in items.values()]
    points_totals = [sum(c["points"] for c in d.get("rubric", [])) for d in items.values()]

    by_family = collections.defaultdict(
        lambda: {"n": 0, "track_A": 0, "track_B": 0, "kind": collections.Counter(), "v1": 0, "authored": 0}
    )
    for iid, d in items.items():
        fam = by_family[family_of(iid)]
        fam["n"] += 1
        fam["track_A" if d.get("track") == "A" else "track_B"] += 1
        fam["kind"][d.get("kind")] += 1
        if d.get("authored"):
            fam["authored"] += 1
        else:
            fam["v1"] += 1

    frontier = json.load(open(FRONTIER_CORE))
    frontier_ids = frontier["item_ids"]
    frontier_by_family = collections.Counter(family_of(i) for i in frontier_ids)

    result = {
        "n_total": n_total,
        "track": dict(track),
        "kind": dict(kind),
        "tier": dict(tier),
        "authored": authored,
        "v1_derived": v1_derived,
        "gate_clause_count": gate_count,
        "no_deliverable_count": no_deliverable,
        "axis_manner_count": axis_manner,
        "recall_hybrid_count": recall_hybrid,
        "criteria_per_item_range": [min(criteria_counts), max(criteria_counts)],
        "points_per_item_range": [min(points_totals), max(points_totals)],
        "by_family": {
            k: {
                "n": v["n"],
                "track_A": v["track_A"],
                "track_B": v["track_B"],
                "kind": dict(v["kind"]),
                "v1_derived": v["v1"],
                "authored": v["authored"],
            }
            for k, v in sorted(by_family.items())
        },
        "frontier_core_n": len(frontier_ids),
        "frontier_core_by_family": dict(sorted(frontier_by_family.items())),
    }

    with open(OUT, "w") as f:
        json.dump(result, f, indent=2)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
