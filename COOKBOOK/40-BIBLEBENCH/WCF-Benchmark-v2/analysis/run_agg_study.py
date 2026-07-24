"""
Session-14 Phase-3 aggregation study.

Reads the calibration results JSON for the given iteration and writes the
aggregation study JSON + MD for the SAME iteration — env-parameterized so an i3
run does NOT overwrite the i2 outputs (dated-file immutability).

Env:
  WCF_AGG_IN_TAG   input results tag  (default: 20260724-session14-calibration-i2)
  WCF_AGG_OUT_TAG  output study tag   (default: 20260724-session14-aggregation-study)

Examples:
  # i2 (default, historical):
  python run_agg_study.py
  # i3:
  WCF_AGG_IN_TAG=20260724-session14-calibration-i3 \
  WCF_AGG_OUT_TAG=20260724-session14-aggregation-study-i3 python run_agg_study.py
"""

import json
import os
import statistics
from pathlib import Path
from collections import defaultdict

ANALYSIS_DIR = Path(__file__).resolve().parent

_IN_TAG  = os.environ.get("WCF_AGG_IN_TAG", "20260724-session14-calibration-i2")
_OUT_TAG = os.environ.get("WCF_AGG_OUT_TAG", "20260724-session14-aggregation-study")

RESULTS_FILE = ANALYSIS_DIR / f"{_IN_TAG}-results.json"
SAMPLE_FILE  = ANALYSIS_DIR / "20260724-session14-calibration-sample.json"
OUT_JSON     = ANALYSIS_DIR / f"{_OUT_TAG}.json"
OUT_MD       = ANALYSIS_DIR / f"{_OUT_TAG}.md"

JUDGES = ["gemini-2.5-flash", "deepseek-chat", "mistral-small-2603"]
JUDGE_SHORT = {"gemini-2.5-flash": "gemini", "deepseek-chat": "deepseek", "mistral-small-2603": "mistral"}

# ── load data ──────────────────────────────────────────────────────────────────
with open(RESULTS_FILE) as f:
    raw = json.load(f)

with open(SAMPLE_FILE) as f:
    sample_raw = json.load(f)

# Build role lookup
role_map = {item["id"]: item["role"] for item in sample_raw["items"]}

# ── build per-item×SUT table ───────────────────────────────────────────────────
# key: (item_id, sut) → {scores: {judge: score}, flagged: {judge: bool}, role, mold}
cells = {}
for rec in raw["records"]:
    key = (rec["id"], rec["sut"])
    scores = {}
    flagged = {}
    for j in JUDGES:
        jdata = rec["judges"][j]
        scores[j] = float(jdata["score"])
        flagged[j] = jdata["quote_check"]["flagged"]
    cells[key] = {
        "id": rec["id"],
        "sut": rec["sut"],
        "role": rec.get("role", role_map.get(rec["id"], "unknown")),
        "mold": rec.get("mold", ""),
        "scores": scores,
        "flagged": flagged,
    }

# ── aggregation functions ──────────────────────────────────────────────────────

def agg_A(scores, flagged):
    """Median of 3."""
    return statistics.median(scores[j] for j in JUDGES), None

def agg_B(scores, flagged):
    """Min of 3, note which judge supplied it."""
    vals = {j: scores[j] for j in JUDGES}
    min_val = min(vals.values())
    suppliers = [j for j, v in vals.items() if v == min_val]
    return min_val, suppliers

def agg_C(scores, flagged):
    """Median over non-flagged judges; fallback to median-of-3 if all flagged."""
    clean = [j for j in JUDGES if not flagged[j]]
    if not clean:
        val = statistics.median(scores[j] for j in JUDGES)
        return val, True  # True = fallback
    return statistics.median(scores[j] for j in clean), False

def agg_D(scores, flagged):
    """Min over non-flagged judges; fallback to median-of-3 if none clean."""
    clean = [j for j in JUDGES if not flagged[j]]
    if not clean:
        val = statistics.median(scores[j] for j in JUDGES)
        return val, True, None  # fallback
    min_val = min(scores[j] for j in clean)
    suppliers = [j for j in clean if scores[j] == min_val]
    return min_val, False, suppliers

# ── compute panel scores ───────────────────────────────────────────────────────
panel = {}
fallback_C = 0
fallback_D = 0

for key, cell in cells.items():
    s = cell["scores"]
    f = cell["flagged"]

    vA, _ = agg_A(s, f)
    vB, suppB = agg_B(s, f)
    vC, fb_C  = agg_C(s, f)
    vD, fb_D, suppD = agg_D(s, f)

    if fb_C:
        fallback_C += 1
    if fb_D:
        fallback_D += 1

    panel[key] = {
        "id": cell["id"],
        "sut": cell["sut"],
        "role": cell["role"],
        "mold": cell["mold"],
        "scores": s,
        "flagged": f,
        "A_median3": vA,
        "B_min3": vB,
        "B_min3_supplier": suppB,
        "C_median_nofab": vC,
        "C_fallback": fb_C,
        "D_groundeddissent": vD,
        "D_fallback": fb_D,
        "D_supplier": suppD,
    }

print(f"Total cells processed: {len(panel)}")
print(f"Fallback count C: {fallback_C}, D: {fallback_D}")

# ── Section 1: Controls (qwen side only) ──────────────────────────────────────
CONTROLS = ["LIB-N-006", "PROOF-N-009", "MEND-N-002", "MEND-N-009", "PROOF-N-005", "WHOLE-N-004"]
EXPECTED = {
    "LIB-N-006": "~83 (positive control)",
    "PROOF-N-009": "~83–91 (positive control)",
    "MEND-N-002": "100 (negative control)",
    "MEND-N-009": "100 (negative control)",
    "PROOF-N-005": "100 (negative control)",
    "WHOLE-N-004": "100 (negative control)",
}

controls_table = []
for item_id in CONTROLS:
    key = (item_id, "qwen")
    if key not in panel:
        print(f"WARNING: missing cell {key}")
        continue
    cell = panel[key]
    row = {
        "id": item_id,
        "role": cell["role"],
        "expected": EXPECTED[item_id],
        "raw_scores": {JUDGE_SHORT[j]: cell["scores"][j] for j in JUDGES},
        "flagged": {JUDGE_SHORT[j]: cell["flagged"][j] for j in JUDGES},
        "A_median3": cell["A_median3"],
        "B_min3": cell["B_min3"],
        "B_supplier": [JUDGE_SHORT[j] for j in cell["B_min3_supplier"]],
        "C_median_nofab": cell["C_median_nofab"],
        "C_fallback": cell["C_fallback"],
        "D_groundeddissent": cell["D_groundeddissent"],
        "D_fallback": cell["D_fallback"],
        "D_supplier": [JUDGE_SHORT[j] for j in cell["D_supplier"]] if cell["D_supplier"] else None,
    }
    controls_table.append(row)

# ── Section 2: Tied-100 sample (20 items) — qwen vs haiku gap per rule ────────
TIED100_IDS = [item["id"] for item in sample_raw["items"] if item["role"] == "tied100_sample"]
assert len(TIED100_IDS) == 20, f"Expected 20 tied100_sample, got {len(TIED100_IDS)}"

RULES = ["A_median3", "B_min3", "C_median_nofab", "D_groundeddissent"]

gap_study = {}
for rule in RULES:
    movers = []
    for item_id in TIED100_IDS:
        kq = (item_id, "qwen")
        kh = (item_id, "haiku")
        if kq not in panel or kh not in panel:
            print(f"WARNING: missing cell for {item_id}")
            continue
        vq = panel[kq][rule]
        vh = panel[kh][rule]
        gap = abs(vq - vh)
        if gap > 0:
            movers.append({"id": item_id, "qwen": vq, "haiku": vh, "gap": gap})
    movers.sort(key=lambda x: -x["gap"])
    gaps = [m["gap"] for m in movers]
    gap_study[rule] = {
        "n_movers": len(movers),
        "movers": movers,
        "median_gap_among_movers": statistics.median(gaps) if gaps else 0,
        "max_gap": max(gaps) if gaps else 0,
    }

# ── Section 3: Gate-relevant: all 26 items, nonzero |qwen−haiku| per rule ─────
ALL_IDS = [item["id"] for item in sample_raw["items"]]
gate_summary = {}
for rule in RULES:
    count = 0
    for item_id in ALL_IDS:
        kq = (item_id, "qwen")
        kh = (item_id, "haiku")
        if kq not in panel or kh not in panel:
            continue
        if abs(panel[kq][rule] - panel[kh][rule]) > 0:
            count += 1
    gate_summary[rule] = count

# ── Section 4: Instability exposure (B and D) ─────────────────────────────────
# Per-item: which judge supplied the min; count of cells where min differs from median >25 pts

def instability_study(rule_key, supplier_key, fallback_key):
    judge_tally = defaultdict(int)   # counts across all item×SUT cells
    large_dissent_cells = []          # cells where |min - median| > 25
    per_mover_detail = []

    for key, cell in panel.items():
        item_id, sut = key
        if cell[fallback_key]:
            # fallback: min = median, supplier undefined
            continue
        suppliers = cell[supplier_key]
        if suppliers is None:
            continue
        val = cell[rule_key]
        med = cell["A_median3"]  # always median-of-3 as baseline
        for j in suppliers:
            judge_tally[JUDGE_SHORT[j]] += 1
        if abs(val - med) > 25:
            large_dissent_cells.append({
                "id": item_id,
                "sut": sut,
                "min_val": val,
                "median_val": med,
                "diff": abs(val - med),
                "supplier": [JUDGE_SHORT[j] for j in suppliers],
            })

    # For movers (tied100 + nonzero gap)
    for item_id in TIED100_IDS:
        kq = (item_id, "qwen")
        kh = (item_id, "haiku")
        for k in [kq, kh]:
            if k not in panel:
                continue
            cell = panel[k]
            if cell[fallback_key]:
                continue
            suppliers = cell[supplier_key]
            if suppliers is None:
                continue
            per_mover_detail.append({
                "id": item_id,
                "sut": k[1],
                "val": cell[rule_key],
                "supplier": [JUDGE_SHORT[j] for j in suppliers],
            })

    return {
        "judge_min_tally": dict(judge_tally),
        "n_large_dissent_cells": len(large_dissent_cells),
        "large_dissent_cells": large_dissent_cells,
    }

instab_B = instability_study("B_min3", "B_min3_supplier", "C_fallback")  # B has no fallback key — use dummy
# B never has fallback; redefine:
def instability_B():
    judge_tally = defaultdict(int)
    large_dissent_cells = []
    for key, cell in panel.items():
        item_id, sut = key
        suppliers = cell["B_min3_supplier"]
        val = cell["B_min3"]
        med = cell["A_median3"]
        for j in suppliers:
            judge_tally[JUDGE_SHORT[j]] += 1
        if abs(val - med) > 25:
            large_dissent_cells.append({
                "id": item_id,
                "sut": sut,
                "min_val": val,
                "median_val": med,
                "diff": abs(val - med),
                "supplier": [JUDGE_SHORT[j] for j in suppliers],
            })
    return {
        "judge_min_tally": dict(judge_tally),
        "n_large_dissent_cells": len(large_dissent_cells),
        "large_dissent_cells": large_dissent_cells,
    }

def instability_D():
    judge_tally = defaultdict(int)
    large_dissent_cells = []
    for key, cell in panel.items():
        item_id, sut = key
        if cell["D_fallback"]:
            continue
        suppliers = cell["D_supplier"]
        if suppliers is None:
            continue
        val = cell["D_groundeddissent"]
        med = cell["A_median3"]
        for j in suppliers:
            judge_tally[JUDGE_SHORT[j]] += 1
        if abs(val - med) > 25:
            large_dissent_cells.append({
                "id": item_id,
                "sut": sut,
                "min_val": val,
                "median_val": med,
                "diff": abs(val - med),
                "supplier": [JUDGE_SHORT[j] for j in suppliers],
            })
    return {
        "judge_min_tally": dict(judge_tally),
        "n_large_dissent_cells": len(large_dissent_cells),
        "large_dissent_cells": large_dissent_cells,
    }

instab_B = instability_B()
instab_D = instability_D()

# ── Assemble output JSON ───────────────────────────────────────────────────────
out = {
    "generated": "2026-07-24",
    "study": "s14 Phase-3 aggregation study",
    "source": str(RESULTS_FILE.name),
    "n_cells": len(panel),
    "judges": JUDGES,
    "fallback_counts": {"C_median_nofab": fallback_C, "D_groundeddissent": fallback_D},
    "section1_controls_qwen": controls_table,
    "section2_tied100_gap_study": gap_study,
    "section3_gate_summary_all26": gate_summary,
    "section4_instability": {
        "B_min3": instab_B,
        "D_groundeddissent": instab_D,
    },
    "panel_cells": [
        {
            "id": cell["id"],
            "sut": cell["sut"],
            "role": cell["role"],
            "mold": cell["mold"],
            "raw_scores": {JUDGE_SHORT[j]: cell["scores"][j] for j in JUDGES},
            "flagged": {JUDGE_SHORT[j]: cell["flagged"][j] for j in JUDGES},
            "A_median3": cell["A_median3"],
            "B_min3": cell["B_min3"],
            "B_min3_supplier": [JUDGE_SHORT[j] for j in cell["B_min3_supplier"]],
            "C_median_nofab": cell["C_median_nofab"],
            "C_fallback": cell["C_fallback"],
            "D_groundeddissent": cell["D_groundeddissent"],
            "D_fallback": cell["D_fallback"],
            "D_supplier": [JUDGE_SHORT[j] for j in cell["D_supplier"]] if cell["D_supplier"] else None,
        }
        for cell in panel.values()
    ],
}

with open(OUT_JSON, "w") as f:
    json.dump(out, f, indent=2)
print(f"Wrote {OUT_JSON}")

# ── Markdown report ────────────────────────────────────────────────────────────
def fmt(v):
    if v == int(v):
        return str(int(v))
    return f"{v:.1f}"

lines = []
lines.append("# Session-14 Phase-3 Aggregation Study")
lines.append("")
lines.append(f"Generated: 2026-07-24  |  Source: `{RESULTS_FILE.name}`  |  n_cells: {len(panel)}")
lines.append("")
lines.append("**Four rules:**")
lines.append("- **A** median-of-3 (status quo)")
lines.append("- **B** min-of-3")
lines.append("- **C** median over non-fabrication-flagged judges (fallback to median-of-3 if all flagged)")
lines.append("- **D** grounded-dissent min: min over non-flagged judges if >=1 clean; else fallback to median-of-3")
lines.append("")
lines.append(f"**Fallback counts:** C = {fallback_C} cells, D = {fallback_D} cells (out of {len(panel)} total cells)")
lines.append("")

# Section 1
lines.append("---")
lines.append("")
lines.append("## Section 1 — Controls (qwen side)")
lines.append("")
lines.append("Judges short: gemini = gemini-2.5-flash, deepseek = deepseek-chat, mistral = mistral-small-2603")
lines.append("")
lines.append("| Item | Role | Expected | gemini | deepseek | mistral | Fab-flagged | A median-3 | B min-3 (supplier) | C med-nofab (fb) | D grnd-diss (fb, supplier) |")
lines.append("|------|------|----------|--------|----------|---------|------------|------------|-------------------|-----------------|--------------------------|")
for row in controls_table:
    rs = row["raw_scores"]
    fl = row["flagged"]
    fab_str = "+".join(k for k, v in fl.items() if v) or "none"
    suppB_str = "+".join(row["B_supplier"])
    fb_C = "FALLBACK" if row["C_fallback"] else ""
    suppD_str = "+".join(row["D_supplier"]) if row["D_supplier"] else "n/a"
    fb_D = "FALLBACK" if row["D_fallback"] else ""
    lines.append(
        f"| {row['id']} | {row['role']} | {row['expected']} "
        f"| {fmt(rs['gemini'])} | {fmt(rs['deepseek'])} | {fmt(rs['mistral'])} "
        f"| {fab_str} "
        f"| {fmt(row['A_median3'])} "
        f"| {fmt(row['B_min3'])} ({suppB_str}) "
        f"| {fmt(row['C_median_nofab'])} {fb_C} "
        f"| {fmt(row['D_groundeddissent'])} {fb_D} ({suppD_str}) |"
    )
lines.append("")

# Section 2
lines.append("---")
lines.append("")
lines.append("## Section 2 — Tied-100 Sample (20 items): |qwen - haiku| gap per rule")
lines.append("")
lines.append("| Rule | n_movers / 20 | Median gap (movers) | Max gap |")
lines.append("|------|--------------|--------------------|---------| ")
for rule in RULES:
    gs = gap_study[rule]
    med_g = fmt(gs["median_gap_among_movers"]) if gs["n_movers"] > 0 else "—"
    max_g = fmt(gs["max_gap"]) if gs["n_movers"] > 0 else "—"
    lines.append(f"| {rule} | {gs['n_movers']} | {med_g} | {max_g} |")
lines.append("")

# Mover lists per rule
for rule in RULES:
    gs = gap_study[rule]
    if gs["n_movers"] == 0:
        lines.append(f"**{rule}:** no movers.")
        lines.append("")
        continue
    lines.append(f"**{rule} movers** ({gs['n_movers']}):")
    lines.append("")
    lines.append("| Item | qwen | haiku | gap |")
    lines.append("|------|------|-------|-----|")
    for m in gs["movers"]:
        lines.append(f"| {m['id']} | {fmt(m['qwen'])} | {fmt(m['haiku'])} | {fmt(m['gap'])} |")
    lines.append("")

# Section 3
lines.append("---")
lines.append("")
lines.append("## Section 3 — Gate-Relevant Summary (all 26 items)")
lines.append("")
lines.append("Count of items where |qwen_score - haiku_score| > 0 under each rule.")
lines.append("")
lines.append("| Rule | Items with nonzero gap (of 26) |")
lines.append("|------|-------------------------------|")
for rule in RULES:
    lines.append(f"| {rule} | {gate_summary[rule]} |")
lines.append("")

# Section 4
lines.append("---")
lines.append("")
lines.append("## Section 4 — Instability Exposure (Rules B and D)")
lines.append("")
lines.append("### 4a. Rule B (min-of-3): judge min-supplier tally across all cells")
lines.append("")
lines.append("| Judge | Times supplied min (of 52 cells) |")
lines.append("|-------|----------------------------------|")
for j, cnt in sorted(instab_B["judge_min_tally"].items(), key=lambda x: -x[1]):
    lines.append(f"| {j} | {cnt} |")
lines.append("")
lines.append(f"**Large-dissent cells (|min - median| > 25 pts): {instab_B['n_large_dissent_cells']}**")
lines.append("")
if instab_B["large_dissent_cells"]:
    lines.append("| Item | SUT | min | median | diff | supplier |")
    lines.append("|------|-----|-----|--------|------|----------|")
    for c in sorted(instab_B["large_dissent_cells"], key=lambda x: -x["diff"]):
        lines.append(f"| {c['id']} | {c['sut']} | {fmt(c['min_val'])} | {fmt(c['median_val'])} | {fmt(c['diff'])} | {'+'.join(c['supplier'])} |")
    lines.append("")

lines.append("### 4b. Rule D (grounded-dissent min): judge min-supplier tally")
lines.append("")
lines.append(f"(Cells excluded from tally due to D-fallback: {fallback_D})")
lines.append("")
lines.append("| Judge | Times supplied min (non-fallback cells) |")
lines.append("|-------|----------------------------------------|")
for j, cnt in sorted(instab_D["judge_min_tally"].items(), key=lambda x: -x[1]):
    lines.append(f"| {j} | {cnt} |")
lines.append("")
lines.append(f"**Large-dissent cells (|min - median| > 25 pts): {instab_D['n_large_dissent_cells']}**")
lines.append("")
if instab_D["large_dissent_cells"]:
    lines.append("| Item | SUT | min | median | diff | supplier |")
    lines.append("|------|-----|-----|--------|------|----------|")
    for c in sorted(instab_D["large_dissent_cells"], key=lambda x: -x["diff"]):
        lines.append(f"| {c['id']} | {c['sut']} | {fmt(c['min_val'])} | {fmt(c['median_val'])} | {fmt(c['diff'])} | {'+'.join(c['supplier'])} |")
    lines.append("")

lines.append("---")
lines.append("")
lines.append("## Full Panel Cell Scores")
lines.append("")
lines.append("All 52 item×SUT cells.")
lines.append("")
lines.append("| Item | SUT | Role | gemini | deepseek | mistral | Fab | A | B | C | D |")
lines.append("|------|-----|------|--------|----------|---------|-----|---|---|---|---|")
for cell in sorted(panel.values(), key=lambda c: (c["id"], c["sut"])):
    rs = cell["scores"]
    fl = cell["flagged"]
    fab_str = "+".join(JUDGE_SHORT[j] for j in JUDGES if fl[j]) or "—"
    fb_c_str = "*" if cell["C_fallback"] else ""
    fb_d_str = "*" if cell["D_fallback"] else ""
    lines.append(
        f"| {cell['id']} | {cell['sut']} | {cell['role']} "
        f"| {fmt(rs[JUDGES[0]])} | {fmt(rs[JUDGES[1]])} | {fmt(rs[JUDGES[2]])} "
        f"| {fab_str} "
        f"| {fmt(cell['A_median3'])} "
        f"| {fmt(cell['B_min3'])} "
        f"| {fmt(cell['C_median_nofab'])}{fb_c_str} "
        f"| {fmt(cell['D_groundeddissent'])}{fb_d_str} |"
    )
lines.append("")
lines.append("\\* = fallback to median-of-3 (all judges fabrication-flagged on that cell)")

md_text = "\n".join(lines)
with open(OUT_MD, "w") as f:
    f.write(md_text)
print(f"Wrote {OUT_MD}")

# ── Print key numbers to stdout for verification ───────────────────────────────
print("\n=== CONTROLS TABLE (qwen) ===")
for row in controls_table:
    print(f"  {row['id']:15s} A={fmt(row['A_median3']):4s} B={fmt(row['B_min3']):4s} C={fmt(row['C_median_nofab']):4s} D={fmt(row['D_groundeddissent']):4s}  fab={'+'.join(k for k,v in row['flagged'].items() if v) or 'none'}")

print("\n=== TIED-100 MOVER COUNTS ===")
for rule in RULES:
    gs = gap_study[rule]
    print(f"  {rule}: {gs['n_movers']}/20 movers  med_gap={fmt(gs['median_gap_among_movers']) if gs['n_movers']>0 else '—'}  max={fmt(gs['max_gap']) if gs['n_movers']>0 else '—'}")

print("\n=== GATE SUMMARY (all 26) ===")
for rule in RULES:
    print(f"  {rule}: {gate_summary[rule]}/26 items with nonzero |qwen-haiku|")

print("\n=== INSTABILITY B: judge tally ===")
for j, cnt in sorted(instab_B["judge_min_tally"].items(), key=lambda x: -x[1]):
    print(f"  {j}: {cnt}")
print(f"  Large-dissent cells (>25pt): {instab_B['n_large_dissent_cells']}")

print("\n=== INSTABILITY D: judge tally ===")
for j, cnt in sorted(instab_D["judge_min_tally"].items(), key=lambda x: -x[1]):
    print(f"  {j}: {cnt}")
print(f"  Large-dissent cells (>25pt): {instab_D['n_large_dissent_cells']}")
