"""Reconstruct critique-01's 92-row high-spread taxonomy with explicit rules.

The session-4 critique-01 classified the 92 grader-spread>=30 rows into
mutually exclusive categories A-G but did not enumerate the ids. This script
recomputes the partition with explicit precedence rules so the category-G
(diffuse 3-way disagreement) set is reproducible for the session-5 Fable
re-read. Counts may differ slightly from the critique's (its exact rules were
not persisted); deltas are reported, and near-G categories (E) are kept as
re-read candidates rather than dropped.

Input:  analysis/20260716-streamB-grade-matrix.json (s2 responses, old bank)
Output: analysis/20260716-session5-g-partition.json
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
matrix = json.load(open(HERE / "20260716-streamB-grade-matrix.json"))["matrix"]

CV02_ITEMS = {
    # quarantined in session 4
    "MEND-A-003", "MEND-A-010", "MEND-A-W305", "DUTY-C6-002", "DUTY-C7-009",
    # control-twin criterion carriers (2 stripped + 1 related)
    "PROOF-C1-W306", "PROOF-C10-W205", "DUTY-C2-007",
}

GRADERS = ["gemini", "deepseek", "mistral"]
LONE_OUTLIER_GAP = 30   # outlier >=30 from BOTH others
AGREE_TOL = 15          # the other two within 15 of each other

def classify(row):
    vals = [row[g] for g in GRADERS]
    spread = max(vals) - min(vals)
    if spread < 30:
        return None
    # A: gemini-zero vs others >=30
    if row["gemini"] == 0 and min(row["deepseek"], row["mistral"]) >= 30:
        return "A-gemini-zero"
    # B: counterfactual / control-twin (CV-02)
    if row["sample_id"] in CV02_ITEMS:
        return "B-counterfactual"
    # C: contested / decline grading
    if row.get("contested"):
        return "C-contested"
    # D: anchor clause-verification
    if row.get("kind") == "anchor":
        return "D-anchor"
    # F: lone outlier (harsh or lenient)
    for i, g in enumerate(GRADERS):
        others = [vals[j] for j in range(3) if j != i]
        if abs(others[0] - others[1]) <= AGREE_TOL:
            om = sum(others) / 2
            if vals[i] <= om - LONE_OUTLIER_GAP:
                return "F-lone-harsh"
            if vals[i] >= om + LONE_OUTLIER_GAP:
                return "F-lone-lenient"
    # G: diffuse 3-way disagreement (E double-barreled folds in; 3 known E rows
    # were not id-enumerated in the critique -> kept as re-read candidates)
    return "G-diffuse"

out = {"rules": {"spread_min": 30, "lone_outlier_gap": LONE_OUTLIER_GAP,
                 "agree_tol": AGREE_TOL, "precedence": "A>B>C>D>F>G",
                 "cv02_items": sorted(CV02_ITEMS)},
       "categories": {}, "rows": []}

for row in matrix:
    cat = classify(row)
    if cat is None:
        continue
    vals = {g: row[g] for g in GRADERS}
    rec = {"sample_id": row["sample_id"], "sut": row["sut"].split("/")[-1],
           "kind": row["kind"], "design": row["design"], "cat": cat, **vals,
           "spread": max(vals.values()) - min(vals.values())}
    out["rows"].append(rec)
    out["categories"].setdefault(cat, []).append(rec["sample_id"] + "|" + rec["sut"])

out["counts"] = {c: len(v) for c, v in sorted(out["categories"].items())}
out["n_high_spread"] = len(out["rows"])
g_items = sorted({r["sample_id"] for r in out["rows"] if r["cat"] == "G-diffuse"})
out["g_unique_items"] = g_items

dest = HERE / "20260716-session5-g-partition.json"
dest.write_text(json.dumps(out, indent=1))
print("total high-spread rows:", out["n_high_spread"], "(critique said 92)")
print("counts:", out["counts"])
print("(critique: A=6 B=15 C=8 D=11 E=3 F=19+7 G=23)")
print("unique G items:", len(g_items))
for r in sorted([r for r in out["rows"] if r["cat"] == "G-diffuse"],
                key=lambda r: -r["spread"]):
    print(f"  {r['sample_id']:20s} {r['sut']:12s} {r['kind']:9s} "
          f"g={r['gemini']:3d} d={r['deepseek']:3d} m={r['mistral']:3d} spread={r['spread']}")
