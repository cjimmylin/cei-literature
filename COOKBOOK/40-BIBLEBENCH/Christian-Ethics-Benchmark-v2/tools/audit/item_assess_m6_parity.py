"""
item_assess_m6_parity.py  --  M6 public vs holdout parity audit
================================================================
Run from vault root:
  WALKWORTHY_ALLOW_HOLDOUT=1 python tools/audit/item_assess_m6_parity.py

Outputs:
  $LOG/m6-parity.json   -- machine-readable aggregates + rates
  $LOG/m6-parity.md     -- human-readable parity report

SAFETY:
  - ZERO holdout item IDs or holdout item text in outputs
  - Aggregates and rates only
  - Read-only outside tools/audit/ and $LOG
  - Does NOT use Python built-in named exec
"""

from __future__ import annotations
import json
import os
import statistics
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

CANARY = "WALKWORTHY-CANARY-7f3e2026"

# ---------------------------------------------------------------------------
# Environment gate
# ---------------------------------------------------------------------------
if os.environ.get("WALKWORTHY_ALLOW_HOLDOUT") != "1":
    sys.exit("ERROR: set WALKWORTHY_ALLOW_HOLDOUT=1 to run this script.")

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
V2 = SCRIPT_DIR.parent.parent  # Christian-Ethics-Benchmark-v2

DATASETS = V2 / "datasets"
LOG = V2 / "logs" / "item-assessment-20260718"

DESIGNS = [f"design{n:02d}" for n in range(1, 11)]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def pct(n: int, total: int) -> float:
    return round(100.0 * n / total, 2) if total else 0.0


def summary_stats(vals: list) -> dict:
    if not vals:
        return {"n": 0, "mean": None, "median": None, "p99": None, "max": None}
    s = sorted(vals)
    n = len(s)
    p99_idx = max(0, int(0.99 * n) - 1)
    return {
        "n": n,
        "mean": round(statistics.mean(s), 6),
        "median": round(statistics.median(s), 6),
        "p99": round(s[p99_idx], 6),
        "max": round(max(s), 6),
    }


def rate_dict(counter: Counter, total: int) -> dict:
    return {k: {"n": v, "pct": pct(v, total)} for k, v in sorted(counter.items())}


# ---------------------------------------------------------------------------
# 1. Load all JSONL records (both surfaces)
# ---------------------------------------------------------------------------

def load_surface_jsonl(surface: str) -> dict:
    """Returns {design_name: [row_dict, ...]} for all 10 designs."""
    per_design: dict[str, list] = {}
    for d in DESIGNS:
        path = DATASETS / surface / f"{d}.jsonl"
        rows = []
        with path.open() as fh:
            for line in fh:
                line = line.strip()
                if line:
                    rows.append(json.loads(line))
        per_design[d] = rows
    return per_design


pub_data = load_surface_jsonl("public")
hld_data = load_surface_jsonl("holdout")


# ---------------------------------------------------------------------------
# 2. Load auxiliary files
# ---------------------------------------------------------------------------

def load_json_file(path: Path) -> dict | list:
    with path.open() as fh:
        return json.load(fh)


m1_pub = load_json_file(LOG / "m1-defects-public.json")
m1_hld = load_json_file(LOG / "m1-defects-holdout.json")

m2_pub = load_json_file(LOG / "m2-anchors-public.json")
m2_hld = load_json_file(LOG / "m2-anchors-holdout.json")

m4_pub = load_json_file(LOG / "m4-redundancy-public.json")
m4_hld = load_json_file(LOG / "m4-redundancy-holdout.json")
m4_cross_raw = load_json_file(LOG / "m4-redundancy-cross.json")


def load_ledger(path: Path) -> list[dict]:
    rows = []
    with path.open() as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            if "item_id" in rec:   # skip header row
                rows.append(rec)
    return rows


ledger_pub = load_ledger(LOG / "merged-ledger-public.jsonl")
ledger_hld = load_ledger(LOG / "merged-ledger-holdout.jsonl")


# ---------------------------------------------------------------------------
# 3. Build M1 defect lookup
# ---------------------------------------------------------------------------

def build_m1_lookup(m1_data: dict) -> dict[str, set]:
    """Returns {two-digit design num: set_of_item_ids_with_defects}."""
    by_design: dict[str, set] = defaultdict(set)
    for rec in m1_data.get("defects", []):
        design_full = rec.get("design", "")   # e.g. "07-seventyseven"
        dnum = design_full.split("-")[0]      # "07"
        by_design[dnum].add(rec["item_id"])
    return dict(by_design)


m1_pub_lookup = build_m1_lookup(m1_pub)
m1_hld_lookup = build_m1_lookup(m1_hld)


# ---------------------------------------------------------------------------
# 4. Char length: sum of all input message content chars + target chars
# ---------------------------------------------------------------------------

def char_len(row: dict) -> int:
    total = 0
    for msg in row.get("input", []):
        content = msg.get("content", "")
        total += len(content) if isinstance(content, str) else len(str(content))
    target = row.get("target", "")
    total += len(target) if isinstance(target, str) else len(str(target))
    return total


# ---------------------------------------------------------------------------
# 5. M1 defect rate helper
# ---------------------------------------------------------------------------

def m1_defect_code_rates(m1_data: dict, all_rows: list[dict]) -> dict:
    """Defect rates per unique item."""
    defects = m1_data.get("defects", [])
    unique_items = set(r["metadata"]["item_id"] for r in all_rows)
    n_items = len(unique_items)

    code_items: dict[str, set] = defaultdict(set)
    for d in defects:
        for code in d.get("defect_codes", []):
            code_items[code].add(d["item_id"])

    contamination_codes = {c for c in code_items if "CONTAM" in c or "TOKEN" in c}
    budget_zero_codes   = {c for c in code_items if "BUDGET" in c or "ZERO"  in c}
    keyed_empty_codes   = {c for c in code_items if "KEYED"  in c or "EMPTY" in c}

    def pct_set(codes_set):
        affected = set()
        for c in codes_set:
            affected |= code_items.get(c, set())
        return {"n_items": len(affected), "pct": pct(len(affected), n_items)}

    all_defected = {d["item_id"] for d in defects}
    return {
        "n_unique_items": n_items,
        "n_items_any_defect": len(all_defected & unique_items),
        "pct_items_any_defect": pct(len(all_defected & unique_items), n_items),
        "keyed_empty": pct_set(keyed_empty_codes),
        "budget_zero": pct_set(budget_zero_codes),
        "contamination": pct_set(contamination_codes),
        "all_codes_present": sorted({c for d in defects for c in d.get("defect_codes", [])}),
    }


# ---------------------------------------------------------------------------
# 6. M2 anchor stats
# ---------------------------------------------------------------------------

def m2_stats(m2_data: dict) -> dict:
    records = m2_data.get("records", [])
    n_total = len(records)
    item_counts: Counter = Counter(r["item_id"] for r in records)
    n_items = len(item_counts)
    mean_anchors = statistics.mean(item_counts.values()) if item_counts else 0.0

    resolve_counts = Counter(r["resolve_status"] for r in records)
    loc_counts = Counter(r["loc_status"] for r in records)

    return {
        "total_anchor_instances": n_total,
        "n_unique_items_with_anchors": n_items,
        "mean_anchors_per_item": round(mean_anchors, 3),
        "resolve_status_rates": rate_dict(resolve_counts, n_total),
        "loc_status_rates": rate_dict(loc_counts, n_total),
    }


# ---------------------------------------------------------------------------
# 7. M4 per-design stats
# ---------------------------------------------------------------------------

def m4_stats_by_design(m4_data: dict) -> dict[str, dict]:
    result = {}
    for des in m4_data.get("designs", []):
        d_name = des.get("design", "")
        stats = des.get("stats", {})
        result[d_name] = {
            "n_items": des.get("n_items"),
            "n_pairs": stats.get("n_pairs"),
            "mean_sim": round(stats.get("mean", 0), 6),
            "p99_sim":  round(stats.get("p99",  0), 6),
            "max_sim":  round(stats.get("max",  0), 6),
        }
    return result


def pooled_m4_summary(m4_by_design: dict) -> dict:
    means = [v["mean_sim"] for v in m4_by_design.values() if v.get("mean_sim") is not None]
    p99s  = [v["p99_sim"]  for v in m4_by_design.values() if v.get("p99_sim")  is not None]
    maxes = [v["max_sim"]  for v in m4_by_design.values() if v.get("max_sim")  is not None]
    return {
        "across_designs_mean_of_means": round(statistics.mean(means), 6) if means else None,
        "across_designs_mean_of_p99s":  round(statistics.mean(p99s),  6) if p99s  else None,
        "across_designs_max_of_maxes":  round(max(maxes),              6) if maxes else None,
        "per_design": m4_by_design,
    }


def m4_cross_summary(m4_cross: dict) -> dict:
    designs_data = m4_cross.get("designs", [])
    if not designs_data:
        return {"note": "cross-design M4 not available or empty"}
    result = {}
    for des in designs_data:
        dname = des.get("design", "unknown")
        stats = des.get("stats", {})
        result[dname] = {
            "n_cross_pairs": stats.get("n_pairs"),
            "mean_cross_sim": round(stats.get("mean", 0), 6),
            "p99_cross_sim":  round(stats.get("p99",  0), 6),
            "max_cross_sim":  round(stats.get("max",  0), 6),
        }
    return result


# ---------------------------------------------------------------------------
# 8. IVR dimension analysis
# ---------------------------------------------------------------------------

IVR_DIMS = ["kv", "af", "cl", "gr", "pi", "bi"]


def ivr_stats(ledger_rows: list[dict]) -> dict:
    n = len(ledger_rows)
    if n == 0:
        return {"n_ledger_items": 0}

    dim_stats = {}
    for dim in IVR_DIMS:
        a_vals: Counter = Counter()
        b_vals: Counter = Counter()
        agree_vals: Counter = Counter()
        for row in ledger_rows:
            av = row.get("A", {}).get(dim)
            bv = row.get("B", {}).get(dim)
            if av is not None:
                a_vals[str(av)] += 1
            if bv is not None:
                b_vals[str(bv)] += 1
            if av is not None and bv is not None and av == bv:
                agree_vals[str(av)] += 1

        total_agree = sum(agree_vals.values())
        dim_stats[dim] = {
            "rater_A": rate_dict(a_vals, n),
            "rater_B": rate_dict(b_vals, n),
            "both_agree_n": total_agree,
            "both_agree_rate": pct(total_agree, n),
            "agree_breakdown": rate_dict(agree_vals, total_agree) if total_agree else {},
        }

    sev_a   = Counter(str(row.get("A", {}).get("derived_severity", "")) for row in ledger_rows)
    sev_b   = Counter(str(row.get("B", {}).get("derived_severity", "")) for row in ledger_rows)
    csev    = Counter(str(row.get("consensus_severity", ""))             for row in ledger_rows)
    n_disp  = sum(1 for row in ledger_rows if row.get("disputed", False))

    sev_labels = ["clean", "minor", "major", "blocker", "disputed"]

    def sev_dist(cnt: Counter) -> dict:
        total = sum(cnt.values())
        return {k: {"n": cnt.get(k, 0), "pct": pct(cnt.get(k, 0), total)}
                for k in sev_labels if cnt.get(k, 0) > 0}

    return {
        "n_ledger_items": n,
        "dimensions": dim_stats,
        "derived_severity_raterA": sev_dist(sev_a),
        "derived_severity_raterB": sev_dist(sev_b),
        "consensus_severity": sev_dist(csev),
        "n_disputed": n_disp,
        "pct_disputed": pct(n_disp, n),
    }


# ---------------------------------------------------------------------------
# 9. Per-surface metrics for a set of rows + ledger
# ---------------------------------------------------------------------------

def surface_metrics(rows: list[dict], ledger_rows: list[dict],
                    m1_lookup: dict, dnum: str) -> dict:
    n_admin = len(rows)
    unique_item_ids = {r["metadata"]["item_id"] for r in rows}
    n_items = len(unique_item_ids)

    n_runnable = sum(1 for r in rows if r["metadata"].get("runnable", False))

    char_lens = [char_len(r) for r in rows]

    seen: set[str] = set()
    area_ctr: Counter = Counter()
    stratum_c = 0
    tier_ctr: Counter = Counter()
    diff_ctr: Counter = Counter()
    for r in rows:
        iid = r["metadata"]["item_id"]
        if iid in seen:
            continue
        seen.add(iid)
        area_ctr[r["metadata"].get("area", "")] += 1
        if r["metadata"].get("stratum") == "c":
            stratum_c += 1
        tier_ctr[r["metadata"].get("tier", "")] += 1
        diff_ctr[r["metadata"].get("difficulty", "")] += 1

    defected_items = m1_lookup.get(dnum, set()) & unique_item_ids
    n_defected = len(defected_items)

    return {
        "n_items": n_items,
        "n_admin_lines": n_admin,
        "n_runnable": n_runnable,
        "runnable_rate_pct": pct(n_runnable, n_admin),
        "char_length": summary_stats(char_lens),
        "area_distribution": rate_dict(area_ctr, n_items),
        "stratum_c_n": stratum_c,
        "stratum_c_pct": pct(stratum_c, n_items),
        "tier_distribution": rate_dict(tier_ctr, n_items),
        "difficulty_distribution": rate_dict(diff_ctr, n_items),
        "m1_n_items_any_defect": n_defected,
        "m1_defect_rate_pct": pct(n_defected, n_items),
        "ivr": ivr_stats(ledger_rows),
    }


# ---------------------------------------------------------------------------
# 10. Per-design blocks
# ---------------------------------------------------------------------------

def compute_design_block(dname: str) -> dict:
    dnum = dname.replace("design", "")
    pub_rows = pub_data[dname]
    hld_rows = hld_data[dname]

    pub_ledger_d = [r for r in ledger_pub if r.get("design") == f"d{dnum}"]
    hld_ledger_d = [r for r in ledger_hld if r.get("design") == f"d{dnum}"]

    pub_m = surface_metrics(pub_rows, pub_ledger_d, m1_pub_lookup, dnum)
    hld_m = surface_metrics(hld_rows, hld_ledger_d, m1_hld_lookup, dnum)

    deltas: dict[str, float] = {}
    for key in ["runnable_rate_pct", "stratum_c_pct", "m1_defect_rate_pct"]:
        pv = pub_m.get(key)
        hv = hld_m.get(key)
        if pv is not None and hv is not None:
            deltas[key] = round(hv - pv, 2)

    pub_cm = pub_m["char_length"].get("mean") or 0
    hld_cm = hld_m["char_length"].get("mean") or 0
    deltas["char_length_mean"] = round(hld_cm - pub_cm, 1)

    pub_hard = pub_m.get("difficulty_distribution", {}).get("hard", {}).get("pct", 0)
    hld_hard = hld_m.get("difficulty_distribution", {}).get("hard", {}).get("pct", 0)
    deltas["difficulty_hard_pct"] = round(hld_hard - pub_hard, 2)

    # Verdict: 5 pp threshold for rate/pct metrics;
    # char_length flagged only if abs relative diff > 20% of public mean.
    PCT_KEYS = {"runnable_rate_pct", "stratum_c_pct", "m1_defect_rate_pct",
                "difficulty_hard_pct"}
    big: dict = {}
    for k, v in deltas.items():
        if k in PCT_KEYS and abs(v) >= 5.0:
            big[k] = v
        elif k == "char_length_mean":
            pub_mean = pub_m["char_length"].get("mean") or 1
            if pub_mean and abs(v / pub_mean) >= 0.20:
                big[k] = v
    verdict = "comparable"
    if big:
        verdict = "non-comparable: " + "; ".join(
            f"{k} delta{v:+.1f}" for k, v in sorted(big.items())
        )

    return {
        "design": dname,
        "public": pub_m,
        "holdout": hld_m,
        "deltas_holdout_minus_public": deltas,
        "parity_verdict": verdict,
    }


print("Computing per-design blocks...", flush=True)
per_design_blocks = []
for dname in DESIGNS:
    block = compute_design_block(dname)
    per_design_blocks.append(block)
    print(f"  {dname}: {block['parity_verdict'][:70]}", flush=True)


# ---------------------------------------------------------------------------
# 11. Pooled metrics
# ---------------------------------------------------------------------------

def flatten_rows(per_design_dict: dict) -> list[dict]:
    out = []
    for d in DESIGNS:
        out.extend(per_design_dict[d])
    return out


pub_flat = flatten_rows(pub_data)
hld_flat = flatten_rows(hld_data)


def pooled_surface_metrics(rows: list[dict], ledger: list[dict],
                            m1_data: dict, m2_data: dict) -> dict:
    n_admin = len(rows)
    unique_items = {r["metadata"]["item_id"] for r in rows}
    n_items = len(unique_items)
    n_runnable = sum(1 for r in rows if r["metadata"].get("runnable", False))

    char_lens = [char_len(r) for r in rows]

    seen: set[str] = set()
    area_ctr: Counter = Counter()
    stratum_c = 0
    tier_ctr: Counter = Counter()
    diff_ctr: Counter = Counter()
    for r in rows:
        iid = r["metadata"]["item_id"]
        if iid in seen:
            continue
        seen.add(iid)
        area_ctr[r["metadata"].get("area", "")] += 1
        if r["metadata"].get("stratum") == "c":
            stratum_c += 1
        tier_ctr[r["metadata"].get("tier", "")] += 1
        diff_ctr[r["metadata"].get("difficulty", "")] += 1

    return {
        "n_items": n_items,
        "n_admin_lines": n_admin,
        "n_runnable": n_runnable,
        "runnable_rate_pct": pct(n_runnable, n_admin),
        "char_length": summary_stats(char_lens),
        "area_distribution": rate_dict(area_ctr, n_items),
        "stratum_c_n": stratum_c,
        "stratum_c_pct": pct(stratum_c, n_items),
        "tier_distribution": rate_dict(tier_ctr, n_items),
        "difficulty_distribution": rate_dict(diff_ctr, n_items),
        "m1_defect_rates": m1_defect_code_rates(m1_data, rows),
        "m2": m2_stats(m2_data),
        "ivr": ivr_stats(ledger),
    }


print("Computing pooled metrics...", flush=True)
pooled_pub = pooled_surface_metrics(pub_flat, ledger_pub, m1_pub, m2_pub)
pooled_hld = pooled_surface_metrics(hld_flat, ledger_hld, m1_hld, m2_hld)


# ---------------------------------------------------------------------------
# 12. Pooled deltas
# ---------------------------------------------------------------------------

def pooled_deltas(pub: dict, hld: dict) -> dict:
    deltas: dict[str, float] = {}

    for key in ["n_items", "n_admin_lines", "runnable_rate_pct",
                "stratum_c_pct", "stratum_c_n"]:
        pv = pub.get(key)
        hv = hld.get(key)
        if pv is not None and hv is not None:
            deltas[key] = round(hv - pv, 3)

    pc = pub.get("char_length", {}).get("mean") or 0
    hc = hld.get("char_length", {}).get("mean") or 0
    deltas["char_length_mean"] = round(hc - pc, 1)
    deltas["char_length_median"] = round(
        (hld.get("char_length", {}).get("median") or 0) -
        (pub.get("char_length", {}).get("median") or 0), 1)

    pub_hard = pub.get("difficulty_distribution", {}).get("hard", {}).get("pct", 0)
    hld_hard = hld.get("difficulty_distribution", {}).get("hard", {}).get("pct", 0)
    deltas["difficulty_hard_pct"] = round(hld_hard - pub_hard, 2)

    pub_def = pub.get("m1_defect_rates", {}).get("pct_items_any_defect", 0)
    hld_def = hld.get("m1_defect_rates", {}).get("pct_items_any_defect", 0)
    deltas["m1_defect_rate_pct"] = round(hld_def - pub_def, 2)

    pub_anc = pub.get("m2", {}).get("mean_anchors_per_item", 0)
    hld_anc = hld.get("m2", {}).get("mean_anchors_per_item", 0)
    deltas["m2_mean_anchors_per_item"] = round(hld_anc - pub_anc, 3)

    pub_clean = pub.get("ivr", {}).get("consensus_severity", {}).get("clean", {}).get("pct", 0)
    hld_clean = hld.get("ivr", {}).get("consensus_severity", {}).get("clean", {}).get("pct", 0)
    deltas["ivr_consensus_clean_pct"] = round(hld_clean - pub_clean, 2)

    pub_disp = pub.get("ivr", {}).get("pct_disputed", 0)
    hld_disp = hld.get("ivr", {}).get("pct_disputed", 0)
    deltas["ivr_pct_disputed"] = round(hld_disp - pub_disp, 2)

    return deltas


p_deltas = pooled_deltas(pooled_pub, pooled_hld)

non_comparable = [b["design"] for b in per_design_blocks
                  if not b["parity_verdict"].startswith("comparable")]


# ---------------------------------------------------------------------------
# 13. Assemble JSON output
# ---------------------------------------------------------------------------

m4_pub_by_design = m4_stats_by_design(m4_pub)
m4_hld_by_design = m4_stats_by_design(m4_hld)

output_json = {
    "canary": CANARY,
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "script": "tools/audit/item_assess_m6_parity.py",
    "safety_note": "ZERO holdout item IDs or holdout item text. Aggregates and rates only.",
    "pooled": {
        "public": pooled_pub,
        "holdout": pooled_hld,
        "deltas_holdout_minus_public": p_deltas,
    },
    "pooled_m4": {
        "public": pooled_m4_summary(m4_pub_by_design),
        "holdout": pooled_m4_summary(m4_hld_by_design),
        "cross_surface": m4_cross_summary(m4_cross_raw),
    },
    "per_design": per_design_blocks,
    "non_comparable_designs": non_comparable,
}


# ---------------------------------------------------------------------------
# 14. Assemble Markdown output
# ---------------------------------------------------------------------------

def fmt_pct(v) -> str:
    if v is None:
        return "--"
    return f"{v:.1f}%"


def fmt_n(v) -> str:
    if v is None:
        return "--"
    return str(int(v))


def fmt_f(v, decimals=3) -> str:
    if v is None:
        return "--"
    return f"{v:.{decimals}f}"


def delta_str(v) -> str:
    if v is None:
        return "--"
    sign = "+" if v >= 0 else ""
    return f"{sign}{v:.2f}"


now_str = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

md_lines = [
    "# M6 Public vs Holdout Parity Report",
    "",
    f"**Generated:** {now_str}  ",
    "**Script:** `tools/audit/item_assess_m6_parity.py`  ",
    f"**Canary:** `{CANARY}`  ",
    "",
    "> SAFETY: This report contains ZERO holdout item IDs and ZERO holdout item text.",
    "> All figures are aggregates and rates only.",
    "",
    "---",
    "",
    "## 1. Pooled Overview",
    "",
    "| Metric | Public | Holdout | Delta (hld-pub) |",
    "|--------|--------|---------|----------------|",
]

pm = pooled_pub
hm = pooled_hld

md_lines += [
    f"| n_items (unique) | {pm['n_items']} | {hm['n_items']} | {delta_str(p_deltas.get('n_items'))} |",
    f"| n_admin_lines | {pm['n_admin_lines']} | {hm['n_admin_lines']} | {delta_str(p_deltas.get('n_admin_lines'))} |",
    f"| runnable_rate | {fmt_pct(pm['runnable_rate_pct'])} | {fmt_pct(hm['runnable_rate_pct'])} | {delta_str(p_deltas.get('runnable_rate_pct'))} |",
    f"| char_len mean | {fmt_f(pm['char_length'].get('mean'),1)} | {fmt_f(hm['char_length'].get('mean'),1)} | {delta_str(p_deltas.get('char_length_mean'))} |",
    f"| char_len median | {fmt_f(pm['char_length'].get('median'),1)} | {fmt_f(hm['char_length'].get('median'),1)} | {delta_str(p_deltas.get('char_length_median'))} |",
    f"| stratum_c % | {fmt_pct(pm['stratum_c_pct'])} | {fmt_pct(hm['stratum_c_pct'])} | {delta_str(p_deltas.get('stratum_c_pct'))} |",
    f"| difficulty hard % | {fmt_pct(pm.get('difficulty_distribution',{}).get('hard',{}).get('pct'))} | {fmt_pct(hm.get('difficulty_distribution',{}).get('hard',{}).get('pct'))} | {delta_str(p_deltas.get('difficulty_hard_pct'))} |",
    f"| M1 defect rate | {fmt_pct(pm['m1_defect_rates']['pct_items_any_defect'])} | {fmt_pct(hm['m1_defect_rates']['pct_items_any_defect'])} | {delta_str(p_deltas.get('m1_defect_rate_pct'))} |",
    f"| M2 mean anchors/item | {fmt_f(pm['m2']['mean_anchors_per_item'])} | {fmt_f(hm['m2']['mean_anchors_per_item'])} | {delta_str(p_deltas.get('m2_mean_anchors_per_item'))} |",
    f"| IVR consensus clean % | {fmt_pct(pm.get('ivr',{}).get('consensus_severity',{}).get('clean',{}).get('pct'))} | {fmt_pct(hm.get('ivr',{}).get('consensus_severity',{}).get('clean',{}).get('pct'))} | {delta_str(p_deltas.get('ivr_consensus_clean_pct'))} |",
    f"| IVR disputed % | {fmt_pct(pm.get('ivr',{}).get('pct_disputed'))} | {fmt_pct(hm.get('ivr',{}).get('pct_disputed'))} | {delta_str(p_deltas.get('ivr_pct_disputed'))} |",
]

md_lines += [
    "",
    "---",
    "",
    "## 2. M2 Anchor Status Rates (pooled)",
    "",
    "### Resolve status",
    "",
    "| Status | Public n | Public % | Holdout n | Holdout % |",
    "|--------|----------|----------|-----------|-----------|",
]

pub_res = pm["m2"]["resolve_status_rates"]
hld_res = hm["m2"]["resolve_status_rates"]
for k in sorted(set(list(pub_res.keys()) + list(hld_res.keys()))):
    pv = pub_res.get(k, {})
    hv = hld_res.get(k, {})
    md_lines.append(
        f"| {k} | {pv.get('n','--')} | {fmt_pct(pv.get('pct'))} | {hv.get('n','--')} | {fmt_pct(hv.get('pct'))} |"
    )

md_lines += [
    "",
    "### Loc status",
    "",
    "| Status | Public n | Public % | Holdout n | Holdout % |",
    "|--------|----------|----------|-----------|-----------|",
]
pub_loc = pm["m2"]["loc_status_rates"]
hld_loc = hm["m2"]["loc_status_rates"]
for k in sorted(set(list(pub_loc.keys()) + list(hld_loc.keys()))):
    pv = pub_loc.get(k, {})
    hv = hld_loc.get(k, {})
    md_lines.append(
        f"| {k} | {pv.get('n','--')} | {fmt_pct(pv.get('pct'))} | {hv.get('n','--')} | {fmt_pct(hv.get('pct'))} |"
    )

md_lines += [
    "",
    "---",
    "",
    "## 3. M4 Within-Design Similarity (per design)",
    "",
    "| Design | Pub mean | Pub p99 | Pub max | Hld mean | Hld p99 | Hld max |",
    "|--------|----------|---------|---------|----------|---------|---------|",
]

for dname in DESIGNS:
    pv = m4_pub_by_design.get(dname, {})
    hv = m4_hld_by_design.get(dname, {})
    md_lines.append(
        f"| {dname} | {fmt_f(pv.get('mean_sim'),4)} | {fmt_f(pv.get('p99_sim'),4)} | {fmt_f(pv.get('max_sim'),4)} "
        f"| {fmt_f(hv.get('mean_sim'),4)} | {fmt_f(hv.get('p99_sim'),4)} | {fmt_f(hv.get('max_sim'),4)} |"
    )

md_lines += [
    "",
    "---",
    "",
    "## 4. IVR Dimension Summary (pooled)",
    "",
]

for dim in IVR_DIMS:
    pub_dim = pm.get("ivr", {}).get("dimensions", {}).get(dim, {})
    hld_dim = hm.get("ivr", {}).get("dimensions", {}).get(dim, {})

    md_lines.append(f"### {dim.upper()}")
    md_lines.append("")
    md_lines.append("| Category | Pub A% | Pub B% | Pub agree% | Hld A% | Hld B% | Hld agree% |")
    md_lines.append("|----------|--------|--------|------------|--------|--------|------------|")

    pub_a  = pub_dim.get("rater_A", {})
    pub_b  = pub_dim.get("rater_B", {})
    pub_ag = pub_dim.get("agree_breakdown", {})
    hld_a  = hld_dim.get("rater_A", {})
    hld_b  = hld_dim.get("rater_B", {})
    hld_ag = hld_dim.get("agree_breakdown", {})

    pub_n = pm.get("ivr", {}).get("n_ledger_items", 1) or 1
    hld_n = hm.get("ivr", {}).get("n_ledger_items", 1) or 1

    all_cats = sorted({c for c in list(pub_a.keys()) + list(hld_a.keys()) if c})
    for cat in all_cats:
        pA    = pub_a.get(cat, {}).get("pct", 0)
        pB    = pub_b.get(cat, {}).get("pct", 0)
        pAg_n = pub_ag.get(cat, {}).get("n", 0)
        pAg   = pct(pAg_n, pub_n)
        hA    = hld_a.get(cat, {}).get("pct", 0)
        hB    = hld_b.get(cat, {}).get("pct", 0)
        hAg_n = hld_ag.get(cat, {}).get("n", 0)
        hAg   = pct(hAg_n, hld_n)
        md_lines.append(
            f"| {cat} | {fmt_pct(pA)} | {fmt_pct(pB)} | {fmt_pct(pAg)} "
            f"| {fmt_pct(hA)} | {fmt_pct(hB)} | {fmt_pct(hAg)} |"
        )

    pub_agree_rate = pub_dim.get("both_agree_rate", 0)
    hld_agree_rate = hld_dim.get("both_agree_rate", 0)
    md_lines.append(
        f"| **inter-rater agree (any cat)** | -- | -- | {fmt_pct(pub_agree_rate)} "
        f"| -- | -- | {fmt_pct(hld_agree_rate)} |"
    )
    md_lines.append("")

md_lines += [
    "### Derived Severity (consensus)",
    "",
    "| Level | Public n | Public % | Holdout n | Holdout % |",
    "|-------|----------|----------|-----------|-----------|",
]

pub_csev = pm.get("ivr", {}).get("consensus_severity", {})
hld_csev = hm.get("ivr", {}).get("consensus_severity", {})
for lv in ["clean", "minor", "major", "blocker", "disputed"]:
    pv = pub_csev.get(lv, {})
    hv = hld_csev.get(lv, {})
    if pv or hv:
        md_lines.append(
            f"| {lv} | {pv.get('n','--')} | {fmt_pct(pv.get('pct'))} | {hv.get('n','--')} | {fmt_pct(hv.get('pct'))} |"
        )

md_lines += [
    "",
    "---",
    "",
    "## 5. Per-Design Parity Grid",
    "",
    "| Design | Pub items | Hld items | Pub run% | Hld run% | Pub char_mean | Hld char_mean "
    "| Pub M1_def% | Hld M1_def% | Pub strat_c% | Hld strat_c% | Pub hard% | Hld hard% | Verdict |",
    "|--------|-----------|-----------|----------|----------|---------------|---------------"
    "|------------|------------|--------------|--------------|-----------|-----------|---------|",
]

for block in per_design_blocks:
    pb = block["public"]
    hb = block["holdout"]
    md_lines.append(
        f"| {block['design']} "
        f"| {pb['n_items']} | {hb['n_items']} "
        f"| {fmt_pct(pb['runnable_rate_pct'])} | {fmt_pct(hb['runnable_rate_pct'])} "
        f"| {fmt_f(pb['char_length'].get('mean'),0)} | {fmt_f(hb['char_length'].get('mean'),0)} "
        f"| {fmt_pct(pb['m1_defect_rate_pct'])} | {fmt_pct(hb['m1_defect_rate_pct'])} "
        f"| {fmt_pct(pb['stratum_c_pct'])} | {fmt_pct(hb['stratum_c_pct'])} "
        f"| {fmt_pct(pb.get('difficulty_distribution',{}).get('hard',{}).get('pct'))} "
        f"| {fmt_pct(hb.get('difficulty_distribution',{}).get('hard',{}).get('pct'))} "
        f"| {block['parity_verdict'][:60]} |"
    )

md_lines += [
    "",
    "---",
    "",
    "## 6. Non-Comparable Designs",
    "",
]
if non_comparable:
    for d in non_comparable:
        blk = next(b for b in per_design_blocks if b["design"] == d)
        md_lines.append(f"- **{d}**: {blk['parity_verdict']}")
else:
    md_lines.append(
        "All designs: **comparable** (no key metric delta >= 5.0 pp on key metrics)."
    )

md_lines += [
    "",
    "---",
    "",
    "## 7. M1 Defect Details (pooled)",
    "",
    "| Code class | Public n items | Public % | Holdout n items | Holdout % |",
    "|------------|----------------|----------|-----------------|-----------|",
]

for code in ["keyed_empty", "budget_zero", "contamination"]:
    pv = pm["m1_defect_rates"].get(code, {})
    hv = hm["m1_defect_rates"].get(code, {})
    md_lines.append(
        f"| {code} | {pv.get('n_items','--')} | {fmt_pct(pv.get('pct'))} "
        f"| {hv.get('n_items','--')} | {fmt_pct(hv.get('pct'))} |"
    )

pub_codes = ", ".join(pm["m1_defect_rates"].get("all_codes_present", []))
hld_codes = ", ".join(hm["m1_defect_rates"].get("all_codes_present", []))
md_lines += [
    "",
    f"Public defect codes present: `{pub_codes}`  ",
    f"Holdout defect codes present: `{hld_codes}`",
    "",
    "---",
    "",
    f"*End of M6 parity report -- canary: {CANARY}*",
]

md_content = "\n".join(md_lines)


# ---------------------------------------------------------------------------
# 15. Write outputs
# ---------------------------------------------------------------------------

out_json = LOG / "m6-parity.json"
out_md   = LOG / "m6-parity.md"

with out_json.open("w") as fh:
    json.dump(output_json, fh, indent=2)

with out_md.open("w") as fh:
    fh.write(md_content)

print(f"\nOutputs written:")
print(f"  {out_json}")
print(f"  {out_md}")


# ---------------------------------------------------------------------------
# 16. Print pooled parity headline
# ---------------------------------------------------------------------------
print("\n=== POOLED PARITY HEADLINE ===")
print(f"Public:  {pooled_pub['n_items']} unique items / {pooled_pub['n_admin_lines']} admin lines")
print(f"Holdout: {pooled_hld['n_items']} unique items / {pooled_hld['n_admin_lines']} admin lines")
print()
print("Top deltas (holdout minus public, sorted by abs magnitude):")
sorted_deltas = sorted(p_deltas.items(), key=lambda kv: abs(kv[1] or 0), reverse=True)
for k, v in sorted_deltas[:8]:
    sign = "+" if v >= 0 else ""
    print(f"  {k:45s} {sign}{v:.3f}")
print()
if non_comparable:
    print(f"Non-comparable designs: {non_comparable}")
else:
    print("All 10 designs: comparable (no key metric delta >= 5.0 pp).")
