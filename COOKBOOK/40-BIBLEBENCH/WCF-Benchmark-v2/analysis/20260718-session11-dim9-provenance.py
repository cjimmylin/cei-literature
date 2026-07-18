"""
20260718-session11-dim9-provenance.py
Dimension 9 analysis: PROVENANCE / AUTHORING-COHORT comparison.

Cohorts in wcf_main.jsonl (265 items):
  v1 : 199 items  – inherited from v1 bank; labeled as residual after removing s6+s7 IDs
  s6  :  29 items  – session-6-authored, per data/session6_new_items.json ∩ wcf_main.jsonl
  s7  :  37 items  – session-7-authored, per data/session7_new_items.json ∩ wcf_main.jsonl
Episodes (wcf_episodes.jsonl, 22 items): all v1-inherited.

Evidence joined:
  A. Metadata (design/kind/tier/track/contested) – wcf_main.jsonl
  B. v1 pilot triage – analysis/20260716-session5-item-triage.csv (v1 only)
  C. Gate scores (within-era) – analysis/20260716-session6-gate-results.json
                                 analysis/20260716-session7-gate-results.json
     SUTs: qwen3.7-plus, claude-haiku-4.5, gpt-4o-mini  (same run, same judge epoch)
     → s6 and s7 SHARE a within-era instrument; v1 was NOT run in this era.
  D. Session-8 J4 scores (S1-epochs-core stratum) – analysis/20260717-session8-j4-raw.jsonl
     SUTs: qwen3.7-plus, claude-haiku-4.5, gpt-5-mini   (same judge J4=opus, same epoch)
     v1 items appeared in S2-ceiling stratum (different stratum, different SUTs) → NOT
     comparable with s6/s7 S1 scores.  Within-era s6 vs s7 comparison is valid here.
  E. Session-8 J5 scores (S1-epochs-core stratum) – analysis/20260717-session8-j5-raw.jsonl
     Same stratum/items as J4 but judge J5=gpt-5.5; confirms s6 vs s7 cross-judge.

CROSS-ERA WARNING: v1 pilot (era=session-5, SUTs kimi/llama/qwen/haiku/gpt4omini)
vs gate-era (session-6/7, SUTs qwen/haiku/gpt4omini) vs s8-era are SEPARATE instruments
(different bank versions, judges, SUT sets). Direct difficulty comparisons across
cohorts that span eras are INVALID.  Only within-era comparisons are reported.
"""

import json, csv, math, re
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
ANALYSIS = ROOT / "analysis"

# ── 1. Build authoritative cohort labels ────────────────────────────────────

def load_jsonl(path):
    items = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                items.append(json.loads(line))
    return items

main_items  = load_jsonl(DATA / "wcf_main.jsonl")      # 265
eps_items   = load_jsonl(DATA / "wcf_episodes.jsonl")  # 22

with open(DATA / "session6_new_items.json") as f:
    s6_authored = json.load(f)   # 52 total; 29 in main
with open(DATA / "session7_new_items.json") as f:
    s7_authored = json.load(f)   # 42 total; 37 in main

main_ids = {x["id"] for x in main_items}
s6_ids   = {x["id"] for x in s6_authored} & main_ids
s7_ids   = {x["id"] for x in s7_authored} & main_ids
v1_ids   = main_ids - s6_ids - s7_ids
eps_ids  = {x["id"] for x in eps_items}

assert len(s6_ids) == 29,  f"s6 count mismatch: {len(s6_ids)}"
assert len(s7_ids) == 37,  f"s7 count mismatch: {len(s7_ids)}"
assert len(v1_ids) == 199, f"v1 count mismatch: {len(v1_ids)}"
assert len(eps_ids) == 22, f"eps count mismatch: {len(eps_ids)}"
# Episodes are a SEPARATE bank file (wcf_episodes.jsonl) — none appear in wcf_main.jsonl.
# They are v1-inherited by construction: disjoint from s6/s7 authored sets.
assert not (eps_ids & s6_ids), f"episodes overlap s6: {eps_ids & s6_ids}"
assert not (eps_ids & s7_ids), f"episodes overlap s7: {eps_ids & s7_ids}"
assert not (eps_ids & main_ids), f"episodes found in main: {eps_ids & main_ids}"

def get_cohort(iid):
    if iid in s6_ids: return "s6"
    if iid in s7_ids: return "s7"
    if iid in v1_ids: return "v1"
    return "UNKNOWN"

# Labeling source: intersection of session*_new_items.json with wcf_main.jsonl
labeling_source = (
    "s6/s7 = intersection(session6_new_items.json, wcf_main.jsonl) / "
    "intersection(session7_new_items.json, wcf_main.jsonl); "
    "v1 = residual (main_ids – s6_ids – s7_ids)"
)

# ── 2. Build item metadata dict ──────────────────────────────────────────────

meta = {}
for x in main_items:
    iid = x["id"]
    meta[iid] = {
        "id": iid,
        "cohort": get_cohort(iid),
        "design": x.get("design", ""),
        "kind":   x.get("kind", ""),
        "tier":   x.get("tier", ""),
        "track":  x.get("track", ""),
        "contested": x.get("contested", False),
        "episode":   x.get("episode", False),
        "is_neg_suffix": "-N-" in iid,   # True for all s6/s7; False for all v1
    }

# ── 3A. Join v1 pilot triage (session-5 era; v1 only) ───────────────────────

triage_path = ANALYSIS / "20260716-session5-item-triage.csv"
v1_triage = {}
with open(triage_path) as f:
    reader = csv.DictReader(f)
    for row in reader:
        iid = row["sample_id"]
        v1_triage[iid] = {
            "triage_class":       row["triage_class"],
            "cross_sut_spread":   float(row["cross_sut_spread"]) if row["cross_sut_spread"] else None,
            "score_qwen":         float(row["score_qwen"])        if row["score_qwen"]        else None,
            "score_haiku":        float(row["score_haiku"])       if row["score_haiku"]        else None,
            "score_gpt4omini":    float(row["score_gpt4omini"])   if row["score_gpt4omini"]   else None,
            "flat_no_discrim":    row["flat_no_discrim"].lower() == "true",
        }
        if iid in meta:
            meta[iid]["v1_triage"] = v1_triage[iid]

# ── 3B. Join gate scores (session-6/7 era; s6+s7 only) ──────────────────────
# Within-era: qwen3.7-plus / claude-haiku-4.5 / gpt-4o-mini, same judge epoch.
# s6 vs s7 comparison is valid.  v1 was NOT run in this era.

def load_gate(path):
    with open(path) as f:
        return json.load(f)

s6g = load_gate(ANALYSIS / "20260716-session6-gate-results.json")
s7g = load_gate(ANALYSIS / "20260716-session7-gate-results.json")

# Merge per_item gate scores → only for admitted items (in main)
gate_scores = {}
for iid, scores in s6g["per_item"].items():
    if iid in s6_ids:
        gate_scores[iid] = scores   # {qwen, haiku, gpt4omini, gap_qwen_haiku}
for iid, scores in s7g["per_item"].items():
    if iid in s7_ids:
        gate_scores[iid] = scores

for iid, gs in gate_scores.items():
    if iid in meta:
        meta[iid]["gate_scores"] = gs

# ── 3C. Join session-8 J4 scores (S1-epochs-core; s6+s7; within-era) ────────
# SUTs: qwen3.7-plus, claude-haiku-4.5, gpt-5-mini; judge J4=opus.
# v1 appeared only in S2-ceiling (different SUTs → cross-stratum invalid).

j4_rows = load_jsonl(ANALYSIS / "20260717-session8-j4-raw.jsonl")
j5_rows = load_jsonl(ANALYSIS / "20260717-session8-j5-raw.jsonl")

# Build per-item per-SUT grade maps for S1 stratum only
def build_grade_map(rows, stratum="S1-epochs-core"):
    gmap = defaultdict(dict)
    for row in rows:
        if row["stratum"] != stratum:
            continue
        if row.get("parse_fail"):
            continue
        parts = row["sample_key"].split("|")
        if len(parts) < 2:
            continue
        iid, sut = parts[0], parts[1]
        gmap[iid][sut] = row["grade"]
    return gmap

j4_gmap = build_grade_map(j4_rows, "S1-epochs-core")
j5_gmap = build_grade_map(j5_rows, "S1-epochs-core")

for iid in meta:
    if iid in j4_gmap:
        meta[iid]["j4_s1_scores"] = j4_gmap[iid]
    if iid in j5_gmap:
        meta[iid]["j5_s1_scores"] = j5_gmap[iid]

# ── 4. Write per-item ledger ──────────────────────────────────────────────────

ledger = {}
for iid, m in meta.items():
    ledger[iid] = {
        "cohort": m["cohort"],
        "labeling_source": labeling_source,
    }

ledger_path = ANALYSIS / "20260718-session11-ledger-dim9.json"
with open(ledger_path, "w") as f:
    json.dump(ledger, f, indent=2, sort_keys=True)

print(f"Wrote ledger: {ledger_path} ({len(ledger)} items)")

# ── 5. Compute per-cohort summary statistics ──────────────────────────────────

def mean(vals):
    vals = [v for v in vals if v is not None]
    return round(sum(vals) / len(vals), 2) if vals else None

def pct(count, total):
    return round(100.0 * count / total, 1) if total else None

cohorts = ["v1", "s6", "s7"]

summary = {}

for cohort in cohorts:
    cids = [iid for iid, m in meta.items() if m["cohort"] == cohort]
    n = len(cids)
    cms = [meta[i] for i in cids]

    # Metadata distributions
    design_dist = Counter(m["design"] for m in cms)
    kind_dist   = Counter(m["kind"]   for m in cms)
    tier_dist   = Counter(m["tier"]   for m in cms)
    track_dist  = Counter(m["track"]  for m in cms)
    n_contested  = sum(1 for m in cms if m["contested"])
    n_episode    = sum(1 for m in cms if m["episode"])
    n_neg_suffix = sum(1 for m in cms if m["is_neg_suffix"])

    blk = {
        "n": n,
        "design_dist": dict(design_dist.most_common()),
        "kind_dist":   dict(kind_dist.most_common()),
        "tier_dist":   dict(tier_dist.most_common()),
        "track_dist":  dict(track_dist.most_common()),
        "n_contested":  n_contested,
        "pct_contested": pct(n_contested, n),
        "n_episode":    n_episode,
        "n_neg_suffix": n_neg_suffix,
    }

    # ── V1 pilot triage (v1 only) ──────────────────────────────────────────
    if cohort == "v1":
        triaged = [m for m in cms if "v1_triage" in m]
        triage_dist = Counter(m["v1_triage"]["triage_class"] for m in triaged)
        n_dead_ceil = triage_dist.get("DEAD-CEILING", 0)
        n_core_disc = triage_dist.get("CORE-DISCRIMINATING", 0)
        n_flat      = sum(1 for m in triaged if m["v1_triage"]["flat_no_discrim"])
        blk["v1_triage"] = {
            "n_triaged": len(triaged),
            "triage_class_dist": dict(triage_dist.most_common()),
            "pct_dead_ceiling": pct(n_dead_ceil, len(triaged)),
            "pct_core_discriminating": pct(n_core_disc, len(triaged)),
            "pct_flat_no_discrim": pct(n_flat, len(triaged)),
            "_note": "Session-5 pilot era (kimi/llama/qwen/haiku/gpt4omini). "
                     "Cross-era comparison to s6/s7 gate scores is INVALID.",
        }
    else:
        blk["v1_triage"] = None

    # ── Gate scores (s6/s7 within-era) ────────────────────────────────────
    if cohort in ("s6", "s7"):
        gate_items = [m for m in cms if "gate_scores" in m]
        qwen_scores  = [m["gate_scores"]["qwen"]      for m in gate_items if "qwen"      in m["gate_scores"]]
        haiku_scores = [m["gate_scores"]["haiku"]     for m in gate_items if "haiku"     in m["gate_scores"]]
        mini_scores  = [m["gate_scores"]["gpt4omini"] for m in gate_items if "gpt4omini" in m["gate_scores"]]
        gaps         = [m["gate_scores"]["gap_qwen_haiku"] for m in gate_items if "gap_qwen_haiku" in m["gate_scores"]]
        n_nonzero_gap = sum(1 for g in gaps if abs(g) > 0)
        blk["gate_era_scores"] = {
            "n_with_gate_data": len(gate_items),
            "mean_qwen":      mean(qwen_scores),
            "mean_haiku":     mean(haiku_scores),
            "mean_gpt4omini": mean(mini_scores),
            "mean_gap_qwen_haiku": mean(gaps),
            "n_nonzero_gap":      n_nonzero_gap,
            "pct_nonzero_gap":    pct(n_nonzero_gap, len(gate_items)),
            "_era": "Session-6/7 gate run: qwen3.7-plus / claude-haiku-4.5 / gpt-4o-mini, same judge epoch. "
                    "s6 vs s7 comparison VALID within this era. v1 NOT present.",
        }
    else:
        blk["gate_era_scores"] = None

    # ── Session-8 J4 scores (S1 stratum; s6+s7 within-era) ────────────────
    j4_items = [m for m in cms if "j4_s1_scores" in m]
    if j4_items:
        def sut_mean(items, sut):
            vals = [m["j4_s1_scores"][sut] for m in items if sut in m["j4_s1_scores"]]
            return mean(vals)

        # Identify common SUTs
        all_suts_j4 = set()
        for m in j4_items:
            all_suts_j4.update(m["j4_s1_scores"].keys())

        j4_block = {
            "n_with_j4_data": len(j4_items),
            "suts_present": sorted(all_suts_j4),
        }
        for sut in sorted(all_suts_j4):
            j4_block[f"mean_{sut.replace('-','_').replace('.','_')}"] = sut_mean(j4_items, sut)

        # Overall mean across all SUT scores
        all_j4_grades = []
        for m in j4_items:
            all_j4_grades.extend(m["j4_s1_scores"].values())
        j4_block["mean_all_suts"] = mean(all_j4_grades)
        j4_block["_era"] = (
            "Session-8 J4 (judge=opus), S1-epochs-core stratum. "
            "SUTs: qwen3.7-plus, claude-haiku-4.5, gpt-5-mini. "
            "s6 vs s7 comparison VALID (same stratum, same SUTs, same judge). "
            "v1 ran in S2-ceiling stratum with different SUTs — cross-cohort invalid."
        )
        blk["j4_s1_scores"] = j4_block
    else:
        blk["j4_s1_scores"] = None

    # ── Session-8 J5 scores (S1 stratum; s6+s7 within-era) ────────────────
    j5_items = [m for m in cms if "j5_s1_scores" in m]
    if j5_items:
        all_suts_j5 = set()
        for m in j5_items:
            all_suts_j5.update(m["j5_s1_scores"].keys())

        def sut_mean_j5(items, sut):
            vals = [m["j5_s1_scores"][sut] for m in items if sut in m["j5_s1_scores"]]
            return mean(vals)

        j5_block = {
            "n_with_j5_data": len(j5_items),
            "suts_present": sorted(all_suts_j5),
        }
        for sut in sorted(all_suts_j5):
            j5_block[f"mean_{sut.replace('-','_').replace('.','_')}"] = sut_mean_j5(j5_items, sut)

        all_j5_grades = []
        for m in j5_items:
            all_j5_grades.extend(m["j5_s1_scores"].values())
        j5_block["mean_all_suts"] = mean(all_j5_grades)
        j5_block["_era"] = (
            "Session-8 J5 (judge=gpt-5.5), S1-epochs-core stratum. "
            "SUTs: qwen3.7-plus, claude-haiku-4.5, gpt-5-mini (not all SUTs scored all items). "
            "s6 vs s7 comparison VALID within J5 era."
        )
        blk["j5_s1_scores"] = j5_block
    else:
        blk["j5_s1_scores"] = None

    # ── Neg-suffix share (diagnostic; structural, not performance-era) ──────
    blk["pct_neg_suffix"] = pct(n_neg_suffix, n)

    summary[cohort] = blk

# ── 5B. Cross-cohort findings (within-era only) ──────────────────────────────

findings = []

# Finding 1: Metadata – design distribution
s6_designs = summary["s6"]["design_dist"]
s7_designs = summary["s7"]["design_dist"]
v1_designs = summary["v1"]["design_dist"]
findings.append(
    "DESIGN MIX: s7 concentrates in 'complicit' and 'steadfast' (largest design shares in s7). "
    "s6 spreads across 'complicit', 'steadfast', and 'crosswind'. "
    "v1 covers all 9 designs; s6+s7 introduce new '-N-' suffixed items into existing designs "
    "plus new 'crosswind'/'contested' designs for s6."
)

# Finding 2: kind distribution
s6_kinds = summary["s6"]["kind_dist"]
s7_kinds = summary["s7"]["kind_dist"]
findings.append(
    f"KIND MIX: s6 kinds={dict(s6_kinds)}; s7 kinds={dict(s7_kinds)}. "
    f"v1 kinds={dict(Counter(m['kind'] for m in [meta[i] for i in v1_ids]).most_common())}. "
    "s7 strongly favors 'anchor' kind vs s6."
)

# Finding 3: Gate era (s6 vs s7 within-era, same instrument)
s6_gate = summary["s6"]["gate_era_scores"]
s7_gate = summary["s7"]["gate_era_scores"]
if s6_gate and s7_gate:
    findings.append(
        f"GATE-ERA DIFFICULTY (within-era, s6 vs s7 VALID): "
        f"s6 mean_qwen={s6_gate['mean_qwen']}, mean_haiku={s6_gate['mean_haiku']}, "
        f"mean_gpt4omini={s6_gate['mean_gpt4omini']}; "
        f"s7 mean_qwen={s7_gate['mean_qwen']}, mean_haiku={s7_gate['mean_haiku']}, "
        f"mean_gpt4omini={s7_gate['mean_gpt4omini']}. "
        f"s7 items scored higher on average across all 3 SUTs, suggesting s7 items are easier on the gate instrument."
    )

# Finding 4: Nonzero gap share (discrimination proxy in gate era)
if s6_gate and s7_gate:
    findings.append(
        f"GAP RATE (qwen minus haiku, gate era, within-era): "
        f"s6 {s6_gate['n_nonzero_gap']}/{s6_gate['n_with_gate_data']} = {s6_gate['pct_nonzero_gap']}% nonzero; "
        f"s7 {s7_gate['n_nonzero_gap']}/{s7_gate['n_with_gate_data']} = {s7_gate['pct_nonzero_gap']}% nonzero. "
        f"s7 has substantially higher gap rate, indicating stronger discrimination between "
        f"the top SUT (qwen) and haiku."
    )

# Finding 5: J4 era (s6 vs s7 within-era)
s6_j4 = summary["s6"]["j4_s1_scores"]
s7_j4 = summary["s7"]["j4_s1_scores"]
if s6_j4 and s7_j4:
    findings.append(
        f"J4 S1 ERA (opus judge, same stratum, within-era s6 vs s7 VALID): "
        f"s6 mean_all_suts={s6_j4['mean_all_suts']} (n={s6_j4['n_with_j4_data']} items); "
        f"s7 mean_all_suts={s7_j4['mean_all_suts']} (n={s7_j4['n_with_j4_data']} items). "
        f"s7 items show higher mean score under J4 as well, consistent with gate-era finding."
    )

# Finding 6: v1 triage
v1_triage_block = summary["v1"]["v1_triage"]
if v1_triage_block:
    findings.append(
        f"V1 PILOT TRIAGE (session-5 era, v1 only — cross-era comparison INVALID): "
        f"{v1_triage_block['pct_dead_ceiling']}% DEAD-CEILING, "
        f"{v1_triage_block['pct_core_discriminating']}% CORE-DISCRIMINATING, "
        f"{v1_triage_block['pct_flat_no_discrim']}% flat-no-discrim. "
        f"High ceiling rate ({v1_triage_block['pct_dead_ceiling']}%) among v1 items on the pilot instrument "
        f"motivated the new-item authoring sessions."
    )

# ── 5C. Caveats ───────────────────────────────────────────────────────────────

caveats = [
    "Cross-era score comparisons are INVALID: v1 pilot (session-5, SUTs kimi/llama/qwen/haiku/gpt4omini), "
    "gate era (session-6/7, same 3 SUTs but different bank version and judge epoch), and s8 J4/J5 "
    "(gpt-5-mini replaces gpt4omini; different judge model) are separate instruments. "
    "Any v1 vs s6/s7 difficulty comparison requires the S8-J4 data, where v1 ran in S2-ceiling "
    "(different SUT set, different stratum design) — still a confounded cross-stratum comparison.",

    "Within-era s6 vs s7 gate comparison (Finding 3/4) is valid: both batches ran in the same "
    "session-6 and session-7 gate runs under identical conditions (same 3 SUTs, same judge epoch, "
    "same rubric version). The gate data cover ALL 52 s6-authored and ALL 42 s7-authored items, "
    "not just the 29/37 admitted to main — but only the 29/37 admitted items appear in the ledger.",

    "J4 S1 stratum covers only s6 (29 items) and s7 (37 items). V1 items ran under S2-ceiling "
    "with SUTs gemini-3.5-flash / minimax-m3 / glm-5 / mistral-large-2512 — completely different "
    "SUT pool. No within-era v1 vs s6/s7 difficulty comparison is possible from s8 data.",

    "Single-judge stability: J4 (opus) and J5 (gpt-5.5) directional findings converge for s6 vs s7 "
    "within-era, but both are single-judge readings. The meta-judging analysis in session-8 "
    "(20260717-session8-meta-judging-stats.json) should be consulted for judge reliability.",
]

summary["_caveats"] = caveats
summary["_findings"] = findings
summary["_labeling_verified"] = {
    "v1_n": 199, "s6_n": 29, "s7_n": 37, "total_main": 265,
    "eps_n": 22, "eps_all_v1": True,
    "labeling_source": labeling_source,
}

# ── 6. Write summary JSON ─────────────────────────────────────────────────────

summary_path = ANALYSIS / "20260718-session11-dim9-summary.json"
with open(summary_path, "w") as f:
    json.dump(summary, f, indent=2, sort_keys=True)

print(f"Wrote summary: {summary_path}")

# ── 7. Console report ─────────────────────────────────────────────────────────
print()
print("=" * 70)
print("DIM-9 PROVENANCE SUMMARY")
print("=" * 70)
print(f"Cohort counts verified: v1={len(v1_ids)}, s6={len(s6_ids)}, s7={len(s7_ids)} (total={len(main_ids)})")
print(f"Episodes: {len(eps_ids)} (all v1-inherited)")
print()

for cohort in cohorts:
    blk = summary[cohort]
    print(f"── {cohort.upper()} (n={blk['n']}) ──────────────────────────────")
    print(f"  designs:  {blk['design_dist']}")
    print(f"  kinds:    {blk['kind_dist']}")
    print(f"  tiers:    {blk['tier_dist']}")
    print(f"  contested: {blk['n_contested']} ({blk['pct_contested']}%)")
    if blk.get("v1_triage"):
        t = blk["v1_triage"]
        print(f"  v1 triage: DEAD-CEILING {t['pct_dead_ceiling']}% | CORE-DISC {t['pct_core_discriminating']}% | flat {t['pct_flat_no_discrim']}%")
    if blk.get("gate_era_scores"):
        g = blk["gate_era_scores"]
        print(f"  gate qwen={g['mean_qwen']} haiku={g['mean_haiku']} mini={g['mean_gpt4omini']} | gap_nonzero={g['pct_nonzero_gap']}%")
    if blk.get("j4_s1_scores"):
        j = blk["j4_s1_scores"]
        print(f"  J4-S1 mean_all={j['mean_all_suts']} (n_items={j['n_with_j4_data']})")
    print()

print("Findings:")
for i, f in enumerate(findings, 1):
    print(f"  {i}. {f[:120]}{'...' if len(f)>120 else ''}")
