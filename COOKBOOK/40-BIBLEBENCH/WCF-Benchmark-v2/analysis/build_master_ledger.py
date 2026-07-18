"""
Build session-11 master per-item ledger for WCF Benchmark v2.4 (287 items).
Outputs:
  analysis/20260718-session11-master-ledger.json
  analysis/20260718-session11-master-ledger.csv
  analysis/20260718-session11-master-summary.json
"""
import json
import csv
import math
import os
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent.parent
ANALYSIS = ROOT / "analysis"
DATA = ROOT / "data"
QUAL_DIR = ANALYSIS / "20260718-session11-qual"
OUT_DATE = "20260718"

# ─── helpers ──────────────────────────────────────────────────────────────────

def load_jsonl(path):
    items = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                items.append(json.loads(line))
    return items

def load_json(path):
    with open(path) as f:
        return json.load(f)

# ─── 1. Load authoritative bank ───────────────────────────────────────────────
main_items = {item["id"]: item for item in load_jsonl(DATA / "wcf_main.jsonl")}
ep_items   = {item["id"]: item for item in load_jsonl(DATA / "wcf_episodes.jsonl")}
bank       = {**main_items, **ep_items}   # 287 items
bank_ids   = set(bank.keys())
assert len(bank_ids) == 287, f"Expected 287 bank ids, got {len(bank_ids)}"

# ─── 2. Load dimension ledgers ────────────────────────────────────────────────
dim2  = load_json(ANALYSIS / "20260718-session11-ledger-dim2.json")
dim5  = load_json(ANALYSIS / "20260718-session11-ledger-dim5.json")
dim7  = load_json(ANALYSIS / "20260718-session11-ledger-dim7.json")
dim8  = load_json(ANALYSIS / "20260718-session11-ledger-dim8.json")
dim9  = load_json(ANALYSIS / "20260718-session11-ledger-dim9.json")
dim10 = load_json(ANALYSIS / "20260718-session11-ledger-dim10.json")

# Collect all orphan ids from all dim ledgers
all_evidence_ids = (set(dim2) | set(dim5) | set(dim7) | set(dim8) |
                    set(dim9) | set(dim10))
orphan_ids = sorted(all_evidence_ids - bank_ids)

# ─── 3. Load qual ratings ─────────────────────────────────────────────────────
def load_qual_rater(rater_name):
    """Load all batches for one rater, returning {id: {cv, rq, tf, edit_rec, batch}}."""
    items = {}
    for b in range(1, 8):
        path = QUAL_DIR / f"{rater_name}-batch{b}.json"
        d = load_json(path)
        for k, v in d.items():
            if not isinstance(v, dict):
                continue
            # Skip meta-like entries (have 'rater' key or 'ids' key but not cv)
            if "construct_validity" not in v:
                continue
            items[k] = {
                "cv":      v["construct_validity"],
                "rq":      v["rubric_quality"],
                "tf":      v["trap_fidelity"],
                "edit_rec": v.get("edit_recommendation"),
                "batch":   b,
            }
    return items

raterA = load_qual_rater("raterA")
raterB = load_qual_rater("raterB")
dual_rated_ids = sorted(set(raterA) & set(raterB))
assert len(dual_rated_ids) == 78, f"Expected 78 dual-rated ids, got {len(dual_rated_ids)}"

# ─── 4. Build per-item rows ───────────────────────────────────────────────────

def get_mold(item_id):
    """Derive mold from id prefix (up to first '-' that precedes C/N/A/W pattern)."""
    # Prefer from dim2 or dim7 which already have mold
    if item_id in dim2:
        return dim2[item_id].get("mold")
    if item_id in dim7:
        return dim7[item_id].get("mold")
    # Fallback: first segment before any digit/commandment pattern
    parts = item_id.split("-")
    return parts[0]

def get_cohort(item_id):
    if item_id in ep_items:
        return "v1"  # episodes per spec
    if item_id in dim9:
        return dim9[item_id]["cohort"]
    return None

def get_is_core_N(item_id):
    if item_id in dim2:
        return dim2[item_id].get("is_core_N")
    # Derive: core-N items have '-N-' in id
    return "-N-" in item_id

def build_dim2_row(item_id):
    if item_id not in dim2:
        return {"discrimination_verdict": None, "evidence_era": None}
    d = dim2[item_id]
    return {
        "discrimination_verdict": d.get("discrimination_verdict"),
        "evidence_era": d.get("evidence_era"),
    }

def build_dim5_row(item_id):
    if item_id not in dim5:
        return {"reliability_flag": None, "key_disagreement_numbers": None}
    d = dim5[item_id]
    # Collect the key disagreement numbers
    nums = {}
    if d.get("pilot_mean_panel_spread") is not None:
        nums["pilot_mean_panel_spread"] = d["pilot_mean_panel_spread"]
    if d.get("kin_mean_pairwise_disagreement") is not None:
        nums["kin_mean_pairwise_disagreement"] = d["kin_mean_pairwise_disagreement"]
    if d.get("s8_mean_abs_j4_j5_delta") is not None:
        nums["s8_mean_abs_j4_j5_delta"] = d["s8_mean_abs_j4_j5_delta"]
    return {
        "reliability_flag": d.get("reliability_flag"),
        "key_disagreement_numbers": nums if nums else None,
    }

def build_dim7_row(item_id):
    if item_id not in dim7:
        return {"redundancy_flag": None, "nearest_neighbor_id": None, "max_stem_sim": None}
    d = dim7[item_id]
    return {
        "redundancy_flag": d.get("redundancy_flag"),
        "nearest_neighbor_id": d.get("nearest_neighbor_id"),
        "max_stem_sim": d.get("max_stem_sim"),
    }

def build_dim8_row(item_id):
    if item_id not in dim8:
        return {"contamination_risk": None}
    d = dim8[item_id]
    return {"contamination_risk": d.get("contamination_risk")}

def build_dim10_row(item_id):
    if item_id not in dim10:
        return {"hygiene_flags": None}
    d = dim10[item_id]
    return {"hygiene_flags": d.get("hygiene_flags", [])}

def build_qual_row(item_id):
    if item_id not in dual_rated_ids:
        return None
    ra = raterA[item_id]
    rb = raterB[item_id]
    recs = []
    if ra["edit_rec"] is not None:
        recs.append(ra["edit_rec"])
    if rb["edit_rec"] is not None:
        recs.append(rb["edit_rec"])
    return {
        "raterA": {"cv": ra["cv"], "rq": ra["rq"], "tf": ra["tf"]},
        "raterB": {"cv": rb["cv"], "rq": rb["rq"], "tf": rb["tf"]},
        "cv_agree": ra["cv"] == rb["cv"],
        "rq_agree": ra["rq"] == rb["rq"],
        "tf_agree": ra["tf"] == rb["tf"],
        "edit_recommendations": recs,
    }

# Build master rows
items_dict = {}
for item_id in sorted(bank_ids):
    bk = bank[item_id]
    row = {
        "id":        item_id,
        "mold":      get_mold(item_id),
        "cohort":    get_cohort(item_id),
        "is_core_N": get_is_core_N(item_id),
        "track":     bk.get("track"),
        "tier":      bk.get("tier"),
        "kind":      bk.get("kind"),
        "contested": bk.get("contested"),
        "dim2":      build_dim2_row(item_id),
        "dim5":      build_dim5_row(item_id),
        "dim7":      build_dim7_row(item_id),
        "dim8":      build_dim8_row(item_id),
        "dim10":     build_dim10_row(item_id),
        "qual":      build_qual_row(item_id),
    }
    items_dict[item_id] = row

assert len(items_dict) == 287

# ─── 5. IRR computation ───────────────────────────────────────────────────────
# Scale ordering for weighted kappa
CV_ORDER = {"STRONG": 2, "ADEQUATE": 1, "WEAK": 0}
RQ_ORDER = {"STRONG": 2, "ADEQUATE": 1, "WEAK": 0}
TF_ORDER = {"CLEAR-TRAP": 2, "PARTIAL-TRAP": 1, "NO-TRAP": 0}

def linear_weighted_kappa(ratings_a, ratings_b, order_map):
    """Compute linear-weighted kappa from two parallel lists of labels."""
    cats = sorted(order_map, key=lambda c: order_map[c])
    n_cats = len(cats)
    n = len(ratings_a)
    if n == 0:
        return None
    # Build O (observed) matrix
    O = [[0] * n_cats for _ in range(n_cats)]
    for a, b in zip(ratings_a, ratings_b):
        if a not in order_map or b not in order_map:
            continue
        i = order_map[a]
        j = order_map[b]
        O[i][j] += 1
    total = sum(O[i][j] for i in range(n_cats) for j in range(n_cats))
    if total == 0:
        return None
    # Marginals
    row_sum = [sum(O[i][j] for j in range(n_cats)) for i in range(n_cats)]
    col_sum = [sum(O[i][j] for i in range(n_cats)) for j in range(n_cats)]
    # Weights: w_ij = 1 - |i-j|/(n_cats-1)
    W = [[0.0] * n_cats for _ in range(n_cats)]
    for i in range(n_cats):
        for j in range(n_cats):
            W[i][j] = 1.0 - abs(i - j) / (n_cats - 1) if n_cats > 1 else 1.0
    Po = sum(W[i][j] * O[i][j] / total for i in range(n_cats) for j in range(n_cats))
    Pe = sum(W[i][j] * (row_sum[i] / total) * (col_sum[j] / total)
             for i in range(n_cats) for j in range(n_cats))
    if Pe == 1.0:
        return 1.0
    return (Po - Pe) / (1.0 - Pe)

def exact_agreement_pct(a_list, b_list):
    if not a_list:
        return None
    return sum(a == b for a, b in zip(a_list, b_list)) / len(a_list)

def compute_irr(id_subset):
    cv_a, cv_b = [], []
    rq_a, rq_b = [], []
    tf_a, tf_b = [], []
    for id_ in id_subset:
        if id_ in raterA and id_ in raterB:
            cv_a.append(raterA[id_]["cv"]); cv_b.append(raterB[id_]["cv"])
            rq_a.append(raterA[id_]["rq"]); rq_b.append(raterB[id_]["rq"])
            tf_a.append(raterA[id_]["tf"]); tf_b.append(raterB[id_]["tf"])
    n = len(cv_a)
    return {
        "n": n,
        "cv": {
            "exact_agree_pct": round(exact_agreement_pct(cv_a, cv_b) * 100, 1) if n else None,
            "linear_weighted_kappa": round(linear_weighted_kappa(cv_a, cv_b, CV_ORDER), 4) if n else None,
        },
        "rq": {
            "exact_agree_pct": round(exact_agreement_pct(rq_a, rq_b) * 100, 1) if n else None,
            "linear_weighted_kappa": round(linear_weighted_kappa(rq_a, rq_b, RQ_ORDER), 4) if n else None,
        },
        "tf": {
            "exact_agree_pct": round(exact_agreement_pct(tf_a, tf_b) * 100, 1) if n else None,
            "linear_weighted_kappa": round(linear_weighted_kappa(tf_a, tf_b, TF_ORDER), 4) if n else None,
        },
    }

# Batch membership for dual-rated items
def batch_of(item_id):
    if item_id in raterA:
        return raterA[item_id]["batch"]
    return None

batch1_ids = [id_ for id_ in dual_rated_ids if batch_of(id_) == 1]
batch3_ids = [id_ for id_ in dual_rated_ids if batch_of(id_) == 3]
rest_ids   = [id_ for id_ in dual_rated_ids if batch_of(id_) not in (1, 3)]

irr_overall = compute_irr(dual_rated_ids)
irr_batch1  = compute_irr(batch1_ids)
irr_batch3  = compute_irr(batch3_ids)
irr_rest    = compute_irr(rest_ids)

irr_stats = {
    "overall":   irr_overall,
    "batch1":    irr_batch1,
    "batch3":    irr_batch3,
    "batches_2_4_5_6_7": irr_rest,
}

# ─── 6. Negative-flag counting and top-20 most-flagged ───────────────────────
NEGATIVE_DIM2  = {"DEAD-CEILING", "LOW-DISCRIMINATION"}   # treat DEAD-CEILING or any non-OK
NEGATIVE_DIM5  = {"LOW-AGREEMENT"}
NEGATIVE_DIM7  = {"NEAR-DUP", "HIGH-SIM"}
NEGATIVE_DIM8  = {"HIGH", "MEDIUM"}
NEGATIVE_QUAL_CV = {"WEAK"}
NEGATIVE_QUAL_TF = {"NO-TRAP"}

def count_negative_flags(row):
    flags = []
    # dim2
    dv = row["dim2"]["discrimination_verdict"]
    if dv and dv not in ("OK", "ADEQUATE", None) and dv.upper() in ("DEAD-CEILING", "LOW-DISCRIMINATION"):
        flags.append(f"dim2:{dv}")
    elif dv and dv.upper() == "DEAD-CEILING":
        flags.append(f"dim2:{dv}")
    # More general: flag anything that is not OK/ADEQUATE/PASS/STRONG
    # Use the verdict directly
    if dv in ("DEAD-CEILING", "LOW-DISCRIMINATION"):
        pass  # already handled (may double but we deduplicate)
    # dim5
    rf = row["dim5"]["reliability_flag"]
    if rf == "LOW-AGREEMENT":
        flags.append(f"dim5:{rf}")
    # dim7
    rdf = row["dim7"]["redundancy_flag"]
    if rdf in NEGATIVE_DIM7:
        flags.append(f"dim7:{rdf}")
    # dim8
    cr = row["dim8"]["contamination_risk"]
    if cr in NEGATIVE_DIM8:
        flags.append(f"dim8:{cr}")
    # dim10
    hf = row["dim10"]["hygiene_flags"]
    if hf:
        for f_ in hf:
            flags.append(f"dim10:{f_}")
    # qual
    q = row["qual"]
    if q is not None:
        if q["raterA"]["cv"] == "WEAK":
            flags.append("qual:raterA-cv-WEAK")
        if q["raterB"]["cv"] == "WEAK":
            flags.append("qual:raterB-cv-WEAK")
        if q["raterA"]["tf"] == "NO-TRAP":
            flags.append("qual:raterA-tf-NO-TRAP")
        if q["raterB"]["tf"] == "NO-TRAP":
            flags.append("qual:raterB-tf-NO-TRAP")
    # Deduplicate
    seen = set()
    unique_flags = []
    for f_ in flags:
        if f_ not in seen:
            seen.add(f_)
            unique_flags.append(f_)
    return unique_flags

# Recompute with proper deduplication
def get_flags(row):
    flags = []
    dv = row["dim2"]["discrimination_verdict"]
    if dv in ("DEAD-CEILING", "LOW-DISCRIMINATION"):
        flags.append(f"dim2:{dv}")
    rf = row["dim5"]["reliability_flag"]
    if rf == "LOW-AGREEMENT":
        flags.append(f"dim5:{rf}")
    rdf = row["dim7"]["redundancy_flag"]
    if rdf in NEGATIVE_DIM7:
        flags.append(f"dim7:{rdf}")
    cr = row["dim8"]["contamination_risk"]
    if cr in NEGATIVE_DIM8:
        flags.append(f"dim8:{cr}")
    hf = row["dim10"]["hygiene_flags"]
    if hf:
        for f_ in hf:
            flags.append(f"dim10:{f_}")
    q = row["qual"]
    if q is not None:
        if q["raterA"]["cv"] == "WEAK":
            flags.append("qual:raterA-cv-WEAK")
        if q["raterB"]["cv"] == "WEAK":
            flags.append("qual:raterB-cv-WEAK")
        if q["raterA"]["tf"] == "NO-TRAP":
            flags.append("qual:raterA-tf-NO-TRAP")
        if q["raterB"]["tf"] == "NO-TRAP":
            flags.append("qual:raterB-tf-NO-TRAP")
    return flags

flag_counts = {}
for id_, row in items_dict.items():
    flag_counts[id_] = get_flags(row)

items_with_any_neg = sum(1 for flags in flag_counts.values() if flags)
ranked = sorted(flag_counts.items(), key=lambda x: -len(x[1]))
top_20 = [
    {"id": id_, "n_flags": len(flags), "flags": flags}
    for id_, flags in ranked[:20]
]

# ─── 7. Cross-tabs and distributions ─────────────────────────────────────────

def dist(values):
    d = {}
    for v in values:
        if v is None:
            v = "null"
        d[str(v)] = d.get(str(v), 0) + 1
    return d

# Per-dim flag distributions
d2_verdicts   = [row["dim2"]["discrimination_verdict"] for row in items_dict.values()]
d5_flags      = [row["dim5"]["reliability_flag"] for row in items_dict.values()]
d7_flags      = [row["dim7"]["redundancy_flag"] for row in items_dict.values()]
d8_risks      = [row["dim8"]["contamination_risk"] for row in items_dict.values()]
d10_n_flags   = [len(row["dim10"]["hygiene_flags"] or []) for row in items_dict.values()]

# Cross-tabs
def crosstab(rows, key_a, key_b):
    """Simple 2-way cross-tab returning dict-of-dict."""
    ct = {}
    for row in rows:
        a = key_a(row)
        b = key_b(row)
        if a is None: a = "null"
        if b is None: b = "null"
        a, b = str(a), str(b)
        if a not in ct:
            ct[a] = {}
        ct[a][b] = ct[a].get(b, 0) + 1
    return ct

rows = list(items_dict.values())
ct_d2_d5 = crosstab(rows,
    lambda r: r["dim2"]["discrimination_verdict"],
    lambda r: r["dim5"]["reliability_flag"])
ct_cont_mold = crosstab(rows,
    lambda r: r["dim8"]["contamination_risk"],
    lambda r: r["mold"])

# Qual verdict x mold (only for dual-rated items)
qual_rows = [row for row in rows if row["qual"] is not None]
ct_qual_cv_mold = crosstab(qual_rows,
    lambda r: r["qual"]["raterA"]["cv"],  # use raterA as representative
    lambda r: r["mold"])

# ─── 8. Assemble summary ─────────────────────────────────────────────────────
summary = {
    "_meta": {
        "date": str(date.today()),
        "bank_version": "v2.4",
        "bank_ids_count": 287,
        "orphan_count": len(orphan_ids),
        "orphan_ids": orphan_ids,
        "dual_rated_items": len(dual_rated_ids),
        "template_audit_file": "20260718-session11-qual/template-audit.json",
        "template_audit_note": "Machinery-level audit — not included in per-item ledger",
    },
    "dim2_discrimination": {
        "verdict_distribution": dist(d2_verdicts),
    },
    "dim5_reliability": {
        "flag_distribution": dist(d5_flags),
        "orphan_ids_in_dim5_not_in_bank": orphan_ids,
    },
    "dim7_redundancy": {
        "flag_distribution": dist(d7_flags),
    },
    "dim8_contamination": {
        "risk_distribution": dist(d8_risks),
    },
    "dim10_hygiene": {
        "n_items_with_0_flags": sum(1 for n in d10_n_flags if n == 0),
        "n_items_with_1plus_flags": sum(1 for n in d10_n_flags if n >= 1),
        "n_items_with_2plus_flags": sum(1 for n in d10_n_flags if n >= 2),
    },
    "crosstabs": {
        "discrimination_x_reliability": ct_d2_d5,
        "contamination_x_mold": ct_cont_mold,
        "qual_cv_raterA_x_mold": ct_qual_cv_mold,
    },
    "irr_stats": irr_stats,
    "negative_flag_summary": {
        "items_with_any_negative_flag": items_with_any_neg,
        "pct_of_287": round(items_with_any_neg / 287 * 100, 1),
    },
    "top_20_most_flagged": top_20,
}

# ─── 9. Assemble master ledger JSON ──────────────────────────────────────────
master = {
    "items": items_dict,
    "orphans": orphan_ids,
    "_meta": {
        "date": str(date.today()),
        "bank_version": "v2.4",
        "source_files": {
            "bank_main": "data/wcf_main.jsonl",
            "bank_episodes": "data/wcf_episodes.jsonl",
            "dim2": "analysis/20260718-session11-ledger-dim2.json",
            "dim5": "analysis/20260718-session11-ledger-dim5.json",
            "dim7": "analysis/20260718-session11-ledger-dim7.json",
            "dim8": "analysis/20260718-session11-ledger-dim8.json",
            "dim9": "analysis/20260718-session11-ledger-dim9.json",
            "dim10": "analysis/20260718-session11-ledger-dim10.json",
            "qual_dir": "analysis/20260718-session11-qual/",
            "template_audit": "analysis/20260718-session11-qual/template-audit.json",
        },
        "items_count": 287,
        "orphan_count": len(orphan_ids),
    },
}

# ─── 10. Write JSON ledger ────────────────────────────────────────────────────
ledger_json_path = ANALYSIS / "20260718-session11-master-ledger.json"
with open(ledger_json_path, "w") as f:
    json.dump(master, f, indent=2)
print(f"Wrote: {ledger_json_path}  ({ledger_json_path.stat().st_size:,} bytes)")

# ─── 11. Write CSV ledger ─────────────────────────────────────────────────────
csv_path = ANALYSIS / "20260718-session11-master-ledger.csv"
CSV_FIELDS = [
    "id", "mold", "cohort", "is_core_N", "track", "tier", "kind", "contested",
    # dim2
    "dim2_discrimination_verdict", "dim2_evidence_era",
    # dim5
    "dim5_reliability_flag", "dim5_pilot_mean_panel_spread", "dim5_kin_mean_pairwise_disagreement", "dim5_s8_mean_abs_j4_j5_delta",
    # dim7
    "dim7_redundancy_flag", "dim7_nearest_neighbor_id", "dim7_max_stem_sim",
    # dim8
    "dim8_contamination_risk",
    # dim10
    "dim10_hygiene_flags",
    # qual
    "qual_raterA_cv", "qual_raterA_rq", "qual_raterA_tf",
    "qual_raterB_cv", "qual_raterB_rq", "qual_raterB_tf",
    "qual_cv_agree", "qual_rq_agree", "qual_tf_agree",
    "qual_edit_recommendations",
]

def row_to_csv(row):
    d2 = row["dim2"]
    d5 = row["dim5"]
    d7 = row["dim7"]
    d8 = row["dim8"]
    d10 = row["dim10"]
    q = row["qual"]
    kn = d5["key_disagreement_numbers"] or {}

    def fmt(v):
        if v is None:
            return ""
        if isinstance(v, list):
            return ";".join(str(x) for x in v)
        if isinstance(v, bool):
            return str(v).lower()
        return str(v)

    return {
        "id":                              row["id"],
        "mold":                            fmt(row["mold"]),
        "cohort":                          fmt(row["cohort"]),
        "is_core_N":                       fmt(row["is_core_N"]),
        "track":                           fmt(row["track"]),
        "tier":                            fmt(row["tier"]),
        "kind":                            fmt(row["kind"]),
        "contested":                       fmt(row["contested"]),
        "dim2_discrimination_verdict":     fmt(d2["discrimination_verdict"]),
        "dim2_evidence_era":               fmt(d2["evidence_era"]),
        "dim5_reliability_flag":           fmt(d5["reliability_flag"]),
        "dim5_pilot_mean_panel_spread":    fmt(kn.get("pilot_mean_panel_spread")),
        "dim5_kin_mean_pairwise_disagreement": fmt(kn.get("kin_mean_pairwise_disagreement")),
        "dim5_s8_mean_abs_j4_j5_delta":   fmt(kn.get("s8_mean_abs_j4_j5_delta")),
        "dim7_redundancy_flag":            fmt(d7["redundancy_flag"]),
        "dim7_nearest_neighbor_id":        fmt(d7["nearest_neighbor_id"]),
        "dim7_max_stem_sim":               fmt(d7["max_stem_sim"]),
        "dim8_contamination_risk":         fmt(d8["contamination_risk"]),
        "dim10_hygiene_flags":             fmt(d10["hygiene_flags"]),
        "qual_raterA_cv":                  fmt(q["raterA"]["cv"]) if q else "",
        "qual_raterA_rq":                  fmt(q["raterA"]["rq"]) if q else "",
        "qual_raterA_tf":                  fmt(q["raterA"]["tf"]) if q else "",
        "qual_raterB_cv":                  fmt(q["raterB"]["cv"]) if q else "",
        "qual_raterB_rq":                  fmt(q["raterB"]["rq"]) if q else "",
        "qual_raterB_tf":                  fmt(q["raterB"]["tf"]) if q else "",
        "qual_cv_agree":                   fmt(q["cv_agree"]) if q else "",
        "qual_rq_agree":                   fmt(q["rq_agree"]) if q else "",
        "qual_tf_agree":                   fmt(q["tf_agree"]) if q else "",
        "qual_edit_recommendations":       fmt(q["edit_recommendations"]) if q else "",
    }

with open(csv_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
    writer.writeheader()
    for id_ in sorted(items_dict.keys()):
        writer.writerow(row_to_csv(items_dict[id_]))

csv_row_count = sum(1 for _ in open(csv_path)) - 1  # subtract header
print(f"Wrote: {csv_path}  ({csv_path.stat().st_size:,} bytes, {csv_row_count} data rows)")

# ─── 12. Write summary JSON ───────────────────────────────────────────────────
summary_path = ANALYSIS / "20260718-session11-master-summary.json"
with open(summary_path, "w") as f:
    json.dump(summary, f, indent=2)
print(f"Wrote: {summary_path}  ({summary_path.stat().st_size:,} bytes)")

# ─── 13. Print verification report ───────────────────────────────────────────
print()
print("=" * 70)
print("VERIFICATION REPORT")
print("=" * 70)
print(f"Bank ids: {len(bank_ids)} (expected 287) — {'OK' if len(bank_ids)==287 else 'FAIL'}")
print(f"Ledger rows: {len(items_dict)} — {'OK' if len(items_dict)==287 else 'FAIL'}")
print(f"CSV data rows: {csv_row_count} — {'OK' if csv_row_count==287 else 'FAIL'}")
print(f"Orphan ids: {len(orphan_ids)}")
print(f"  {orphan_ids}")
print()
print("IRR — Overall (n=78):")
for dim in ["cv", "rq", "tf"]:
    s = irr_overall[dim]
    print(f"  {dim.upper()}: exact={s['exact_agree_pct']}%  κw={s['linear_weighted_kappa']}")
print()
print("IRR — Batch 1 (n=%d):" % irr_batch1["n"])
for dim in ["cv", "rq", "tf"]:
    s = irr_batch1[dim]
    print(f"  {dim.upper()}: exact={s['exact_agree_pct']}%  κw={s['linear_weighted_kappa']}")
print()
print("IRR — Batch 3 (n=%d):" % irr_batch3["n"])
for dim in ["cv", "rq", "tf"]:
    s = irr_batch3[dim]
    print(f"  {dim.upper()}: exact={s['exact_agree_pct']}%  κw={s['linear_weighted_kappa']}")
print()
print("IRR — Batches 2,4,5,6,7 (n=%d):" % irr_rest["n"])
for dim in ["cv", "rq", "tf"]:
    s = irr_rest[dim]
    print(f"  {dim.upper()}: exact={s['exact_agree_pct']}%  κw={s['linear_weighted_kappa']}")
print()
print(f"Items with >= 1 negative flag: {items_with_any_neg} / 287 ({summary['negative_flag_summary']['pct_of_287']}%)")
print()
print("TOP-10 MOST-FLAGGED:")
for entry in top_20[:10]:
    print(f"  {entry['id']:25s}  n={entry['n_flags']}  {entry['flags']}")
print()
print("STED-N-003 vs STED-N-022:")
s003 = dim7.get("STED-N-003", {})
s022 = dim7.get("STED-N-022", {})
print(f"  STED-N-003: max_stem_sim={s003.get('max_stem_sim')}  nearest={s003.get('nearest_neighbor_id')}  flag={s003.get('redundancy_flag')}")
print(f"  STED-N-022: max_stem_sim={s022.get('max_stem_sim')}  nearest={s022.get('nearest_neighbor_id')}  flag={s022.get('redundancy_flag')}")
print(f"  Verdict: mutual nearest-neighbors, sim={s003.get('max_stem_sim')} — both flagged '{s003.get('redundancy_flag')}'")
