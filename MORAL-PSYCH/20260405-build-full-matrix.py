"""
Build full 292-candidate feature matrix by merging:
1. Auto-scores (A1, B2, C3, C5) from 20260405-auto-scores.json
2. Qualitative scores (A2-A6, B1, B3, B4, B6, B7, B10, C1, C2) from opus batch files
3. Compute PD, PE, CI, COMPOSITE for all candidates
4. Apply Jenks natural breaks for 4-tier assignment

Output: MORAL-PSYCH/20260405-full-292-feature-matrix.json
        MORAL-PSYCH/ANALYSIS/20260405-tier-assignment.json
"""
from __future__ import annotations
import json, math
from pathlib import Path

ROOT = Path(".")

# ──────────────────────────────────────────────────────────────────────────────
# 1. Load auto-scores
# ──────────────────────────────────────────────────────────────────────────────
auto_data = json.loads(Path("MORAL-PSYCH/ASSESSMENT/20260405-auto-scores.json").read_text())
auto_by_file = {e["file"]: e["auto_scores"] for e in auto_data["entries"]}

# ──────────────────────────────────────────────────────────────────────────────
# 2. Load qualitative scores from all opus batches
# ──────────────────────────────────────────────────────────────────────────────
qual_by_file: dict[str, dict] = {}
for i in range(1, 6):
    p = Path(f"MORAL-PSYCH/ASSESSMENT/20260405-opus-batch-0{i}.json")
    if not p.exists():
        print(f"WARNING: {p} not found — batch {i} not yet complete")
        continue
    data = json.loads(p.read_text())
    entries = data.get("assessments", data) if isinstance(data, dict) else data
    if isinstance(data, list):
        entries = data
    for e in entries:
        qual_by_file[e["file"]] = e.get("scores", {})

print(f"Loaded qualitative scores for {len(qual_by_file)} candidates")

# ──────────────────────────────────────────────────────────────────────────────
# 3. Merge scores and compute composites
# ──────────────────────────────────────────────────────────────────────────────
roster = json.loads(Path("MORAL-PSYCH/20260405-full-292-candidate-roster.json").read_text())

def safe_score(scores: dict, key: str) -> float:
    entry = scores.get(key, {})
    if isinstance(entry, dict):
        s = entry.get("score")
        return float(s) if s is not None else 0.0
    return float(entry) if entry is not None else 0.0

def compute_composites(all_scores: dict) -> dict:
    # PD = A2(0.25) + A6(0.20) + A1(0.15) + A5(0.15) + A3(0.15) + A4(0.10)
    PD = (safe_score(all_scores, "A2") * 0.25 +
          safe_score(all_scores, "A6") * 0.20 +
          safe_score(all_scores, "A1") * 0.15 +
          safe_score(all_scores, "A5") * 0.15 +
          safe_score(all_scores, "A3") * 0.15 +
          safe_score(all_scores, "A4") * 0.10)
    # PE = B3(0.20) + B2(0.15) + B6(0.15) + B7(0.15) + B1(0.10) + B4(0.10) + B10(0.15)
    PE = (safe_score(all_scores, "B3") * 0.20 +
          safe_score(all_scores, "B2") * 0.15 +
          safe_score(all_scores, "B6") * 0.15 +
          safe_score(all_scores, "B7") * 0.15 +
          safe_score(all_scores, "B1") * 0.10 +
          safe_score(all_scores, "B4") * 0.10 +
          safe_score(all_scores, "B10") * 0.15)
    # CI = C1(0.30) + C2(0.30) + C3(0.25) + C5(0.15)
    CI = (safe_score(all_scores, "C1") * 0.30 +
          safe_score(all_scores, "C2") * 0.30 +
          safe_score(all_scores, "C3") * 0.25 +
          safe_score(all_scores, "C5") * 0.15)
    COMPOSITE = PD * 0.50 + PE * 0.30 + CI * 0.20
    return {"PD": round(PD, 2), "PE": round(PE, 2), "CI": round(CI, 2), "COMPOSITE": round(COMPOSITE, 2)}

matrix = []
missing_qual = 0
for c in roster["candidates"]:
    f = c["file"]
    auto = auto_by_file.get(f, {})
    qual = qual_by_file.get(f, {})

    if not qual:
        missing_qual += 1

    # Merge: qualitative takes precedence over auto for overlapping features
    all_scores = dict(auto)
    all_scores.update(qual)

    composites = compute_composites(all_scores)

    matrix.append({
        "file": f,
        "short_title": c["short_title"],
        "year": c.get("year"),
        "info_tier": c.get("info_tier"),
        "theories": c.get("theories", []),
        "source": c.get("source"),
        "publication": c.get("publication", ""),
        "scores": all_scores,
        "composites": composites,
        "tier": None  # assigned in Phase 4
    })

print(f"Built matrix: {len(matrix)} candidates")
print(f"Missing qualitative scores: {missing_qual}")

# Sort by composite descending
matrix.sort(key=lambda x: x["composites"]["COMPOSITE"], reverse=True)

# ──────────────────────────────────────────────────────────────────────────────
# 4. Jenks natural breaks for 4 tiers
# ──────────────────────────────────────────────────────────────────────────────
def jenks_breaks(values: list[float], n_classes: int) -> list[float]:
    """Fisher-Jenks natural breaks optimization."""
    values = sorted(values)
    n = len(values)
    # Lower triangular matrix of sum of squared deviations
    mat1 = [[0.0] * (n + 1) for _ in range(n_classes + 1)]
    mat2 = [[0.0] * (n + 1) for _ in range(n_classes + 1)]

    for i in range(1, n_classes + 1):
        mat1[i][1] = 1.0
        mat2[i][1] = 0.0
        for j in range(2, n + 1):
            mat2[i][j] = float("inf")

    v = 0.0
    for l in range(2, n + 1):
        s1 = s2 = 0.0
        w = 0.0
        for m in range(1, l + 1):
            i3 = l - m + 1
            val = float(values[i3 - 1])
            s2 += val * val
            s1 += val
            w += 1
            v = s2 - (s1 * s1) / w
            i4 = i3 - 1
            if i4 != 0:
                for j in range(2, n_classes + 1):
                    if mat2[j][l] >= (v + mat2[j - 1][i4]):
                        mat1[j][l] = i3
                        mat2[j][l] = v + mat2[j - 1][i4]
        mat1[1][l] = 1
        mat2[1][l] = v

    k = n
    klass_bounds = []
    for j in range(n_classes, 1, -1):
        idx = int(mat1[j][k] - 1)
        klass_bounds.append(values[idx])
        k = int(mat1[j][k] - 1)

    return list(reversed(klass_bounds))

composites = [e["composites"]["COMPOSITE"] for e in matrix]
breaks = jenks_breaks(composites, 4)
print(f"\nJenks breaks (4 classes): {[round(b,1) for b in breaks]}")

# Assign tiers
def assign_tier(score: float, breaks: list[float]) -> str:
    if score >= breaks[2]: return "top"
    if score >= breaks[1]: return "high"
    if score >= breaks[0]: return "med"
    return "low"

for e in matrix:
    e["tier"] = assign_tier(e["composites"]["COMPOSITE"], breaks)

# Tier counts
from collections import Counter
tier_counts = Counter(e["tier"] for e in matrix)
print(f"Tier distribution: {dict(tier_counts)}")

# Theory × tier crosstab
theory_tier: dict[str, dict] = {}
for e in matrix:
    theories = e.get("theories") or ["unknown"]
    for t in theories[:1]:  # primary theory only
        if t not in theory_tier:
            theory_tier[t] = {"top": 0, "high": 0, "med": 0, "low": 0}
        theory_tier[t][e["tier"]] += 1

print("\nTheory × Tier crosstab (primary theory):")
print(f"{'Theory':<15} {'Top':>5} {'High':>5} {'Med':>5} {'Low':>5} {'Total':>6}")
for t in sorted(theory_tier, key=lambda x: sum(theory_tier[x].values()), reverse=True):
    d = theory_tier[t]
    total = sum(d.values())
    print(f"{t:<15} {d['top']:>5} {d['high']:>5} {d['med']:>5} {d['low']:>5} {total:>6}")

# Top/High composite stats
for tier in ["top", "high", "med", "low"]:
    scores = [e["composites"]["COMPOSITE"] for e in matrix if e["tier"] == tier]
    if scores:
        print(f"\n{tier.upper()} tier: n={len(scores)}, "
              f"mean={sum(scores)/len(scores):.1f}, "
              f"min={min(scores):.1f}, max={max(scores):.1f}")

# Save full matrix
Path("MORAL-PSYCH/20260405-full-292-feature-matrix.json").write_text(
    json.dumps({"summary": {"total": len(matrix), "jenks_breaks": [round(b,2) for b in breaks],
                            "tier_counts": dict(tier_counts)},
                "matrix": matrix}, indent=2))

# Save tier assignment
tier_data = {
    "jenks_breaks": [round(b, 2) for b in breaks],
    "tier_counts": dict(tier_counts),
    "theory_tier_crosstab": theory_tier,
    "ranked": [{"rank": i+1, "file": e["file"], "short_title": e["short_title"],
                "year": e["year"], "theories": e["theories"],
                "COMPOSITE": e["composites"]["COMPOSITE"],
                "PD": e["composites"]["PD"], "PE": e["composites"]["PE"],
                "CI": e["composites"]["CI"], "tier": e["tier"]}
               for i, e in enumerate(matrix)]
}
Path("MORAL-PSYCH/ANALYSIS/20260405-tier-assignment.json").write_text(json.dumps(tier_data, indent=2))
print("\nOutput files written.")
