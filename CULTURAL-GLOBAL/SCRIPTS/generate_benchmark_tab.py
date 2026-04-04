#!/usr/bin/env python3
"""Generate benchmark-data.js + benchmarks.html for Cross-Cultural Values Alignment.

Architecture: "Fat data, thin client" -- Python pre-computes all analytics into JS constants.
Browser only renders ECharts charts from pre-computed data.

Input files (all under CULTURAL-GLOBAL/DATA/ and CULTURAL-GLOBAL/TRIALS/):
  - 20260404-benchmark-rankings.json
  - 20260404-benchmark-analyses.json
  - 20260404-benchmark-features-merged.json
  - 20260404-trial-CC*.json (10 trial files)

Output:
  - CULTURAL-GLOBAL/DASHBOARD/benchmark-data.js
  - CULTURAL-GLOBAL/DASHBOARD/benchmarks.html
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from collections import Counter, defaultdict

# ── Paths ────────────────────────────────────────────────────────────────────
BASE = Path(__file__).resolve().parent.parent          # CULTURAL-GLOBAL/
DATA = BASE / "DATA"
TRIALS = BASE / "TRIALS"
OUT_JS = BASE / "DASHBOARD" / "benchmark-data.js"
OUT_HTML = BASE / "DASHBOARD" / "benchmarks.html"

# ── Load input files ─────────────────────────────────────────────────────────
def load_json(p: Path) -> dict:
    with open(p, encoding="utf-8") as f:
        return json.load(f)


rankings_data = load_json(DATA / "20260404-benchmark-rankings.json")
analyses_data = load_json(DATA / "20260404-benchmark-analyses.json")
features_data = load_json(DATA / "20260404-benchmark-features-merged.json")

# Load all trial files (Opus only for original tabs; all models for comparison)
trial_files = sorted(TRIALS.glob("20260404-trial-CC*-opus.json"))
trials_raw: list[dict] = []
for tf in trial_files:
    trials_raw.append(load_json(tf))

# Load multi-model analysis if available
MULTIMODEL_ANALYSIS_PATH = DATA / "20260404-multimodel-trial-analysis.json"
multimodel_data: dict = {}
if MULTIMODEL_ANALYSIS_PATH.exists():
    multimodel_data = load_json(MULTIMODEL_ANALYSIS_PATH)

print(f"Loaded {len(trial_files)} trial files, {len(rankings_data['rankings'])} rankings, "
      f"{len(features_data['papers'])} feature records")
if multimodel_data:
    print(f"Multi-model analysis loaded: {list(multimodel_data.get('metadata', {}).get('trials_per_model', {}).items())}")

# ── Helper: analyses by id ──────────────────────────────────────────────────
analyses_by_id: dict[int, dict] = {}
for a in analyses_data["analyses"]:
    analyses_by_id[a["analysis_id"]] = a


# ═══════════════════════════════════════════════════════════════════════════════
# STEP 1: Build all data objects
# ═══════════════════════════════════════════════════════════════════════════════

# ── 1. BENCHMARK_META ────────────────────────────────────────────────────────
meta = rankings_data["metadata"]
BENCHMARK_META = {
    "date": meta["date"],
    "total_papers": meta["papers_ranked"],
    "total_features": len(features_data["papers"]),
    "total_trials": len(trials_raw),
    "method": meta["method"],
    "veto_count": meta["veto_count"],
    "kendall_w": meta["kendall_w"],
    "weight_scheme": meta["weight_scheme"],
    "deep_scored": features_data["metadata"].get("deep_scored", 50),
    "auto_scored": features_data["metadata"].get("auto_scored_only", 168),
}

# ── 2. BENCHMARK_RANKINGS (top 50) ──────────────────────────────────────────
# Build a lookup from features data for fast access
features_lookup: dict[str, dict] = {}
for p in features_data["papers"]:
    features_lookup[p["filename"]] = p["features"]

BENCHMARK_RANKINGS = []
for r in rankings_data["rankings"][:50]:
    feat = features_lookup.get(r["filename"], {})
    scope = feat.get("C1_cultural_scope") or "unknown"
    nw_count = feat.get("T4_nonwestern_framework_count") or 0
    langs = feat.get("L1_languages_count") or 1
    da_raw = feat.get("R1_data_availability") or ""
    da_str = str(da_raw).lower()
    if "public" in da_str or "open" in da_str:
        data_avail = "open"
    elif "partial" in da_str:
        data_avail = "partial"
    elif "unavail" in da_str or "unspecified" in da_str:
        data_avail = "unavailable"
    else:
        data_avail = da_raw or "unknown"

    BENCHMARK_RANKINGS.append({
        "rank": r["rank"],
        "filename": r["filename"],
        "short_title": r["short_title"],
        "topsis_score": round(r["topsis_score"], 4),
        "cultural_scope": scope,
        "languages": langs,
        "nw_frameworks": nw_count,
        "data_available": data_avail,
        "veto_flag": r.get("veto_flag", False),
        "dimensional_scores": r.get("dimensional_scores", {}),
    })

# ── 3. TRADITION_COVERAGE ────────────────────────────────────────────────────
a2 = analyses_by_id[2]["results"]
tc = a2["tradition_counts"]
TRADITION_COVERAGE = {
    "confucian": tc.get("Confucian", 0),
    "ubuntu": tc.get("Ubuntu", 0),
    "islamic": tc.get("Islamic", 0),
    "buddhist": tc.get("Buddhist", 0),
    "dharmic": tc.get("Dharmic", 0),
    "indigenous": tc.get("Indigenous/Relational", 0),
    "buen_vivir": tc.get("Buen Vivir", 0),
}

# ── 4. GEOGRAPHIC_COVERAGE ───────────────────────────────────────────────────
a3 = analyses_by_id[3]["results"]
GEOGRAPHIC_COVERAGE = dict(a3["region_counts"])

# ── 5. CULTURAL_SCOPE_DIST ───────────────────────────────────────────────────
scope_counter: Counter = Counter()
for p in features_data["papers"]:
    cs = (p["features"].get("C1_cultural_scope") or "unknown").lower().strip()
    if "mono" in cs or "single" in cs:
        scope_counter["monocultural"] += 1
    elif "bi" in cs or "limited" in cs:
        scope_counter["bicultural"] += 1
    elif "multi" in cs:
        scope_counter["multicultural"] += 1
    elif "pan" in cs or "cross" in cs or "global" in cs:
        scope_counter["pancultural"] += 1
    elif "universal" in cs:
        scope_counter["universal_claim"] += 1
    else:
        scope_counter["monocultural"] += 1  # default

CULTURAL_SCOPE_DIST = {
    "monocultural": scope_counter.get("monocultural", 0),
    "bicultural": scope_counter.get("bicultural", 0),
    "multicultural": scope_counter.get("multicultural", 0),
    "pancultural": scope_counter.get("pancultural", 0),
    "universal_claim": scope_counter.get("universal_claim", 0),
}

# ── 6. PSYCHOMETRIC_QUALITY ──────────────────────────────────────────────────
a4 = analyses_by_id[4]["results"]
rel_count = a4["overall_reliability_count"]
inv_count = a4["overall_invariance_count"]
total = a4["total_papers"]
PSYCHOMETRIC_QUALITY = {
    "reliability_reported": rel_count,
    "invariance_tested": inv_count,
    "neither": total - rel_count - inv_count,
}

# Also build quality-by-scope for stacked bar
PSYCHOMETRIC_BY_SCOPE = {}
for tier, vals in a4["quality_by_scope_tier"].items():
    PSYCHOMETRIC_BY_SCOPE[tier] = {
        "reliability_only": vals["has_reliability"] - vals["has_invariance"],
        "invariance": vals["has_invariance"],
        "neither": vals["total"] - vals["has_reliability"],
        "total": vals["total"],
    }

# ── 7. DATA_AVAILABILITY ────────────────────────────────────────────────────
a10 = analyses_by_id[10]["results"]
dad = a10["data_availability_distribution"]
DATA_AVAILABILITY = {
    "open_source": dad.get("open/public", 0),
    "restricted": dad.get("partial", 0) + dad.get("planned", 0),
    "unavailable": dad.get("unavailable/unspecified", 0) + dad.get("unknown/NA", 0),
}

# ── 8. TRIAL_SUMMARY ────────────────────────────────────────────────────────
TRIAL_SUMMARY = []
for t in trials_raw:
    # Extract key finding from summary or first item
    key_finding = ""
    summary = t.get("summary", {})
    if isinstance(summary, dict):
        kfs = summary.get("key_findings", [])
        if kfs:
            key_finding = kfs[0][:200]
        elif summary.get("overall_pattern"):
            key_finding = summary["overall_pattern"][:200]
    if not key_finding and t.get("items"):
        first = t["items"][0]
        key_finding = first.get("reasoning", first.get("cultural_notes", ""))[:200]

    TRIAL_SUMMARY.append({
        "id": t["trial_id"],
        "benchmark": t["benchmark"],
        "theory": t.get("theory", ""),
        "items": t["items_count"],
        "model": t.get("model", "claude-opus-4-6"),
        "pilot": t.get("pilot_instrument", False),
        "key_finding": key_finding,
    })

# ── 9. CULTURAL_ALIGNMENT (from CC1 trial) ──────────────────────────────────
cc1 = None
for t in trials_raw:
    if t["trial_id"] == "CC1":
        cc1 = t
        break

countries = ["US", "China", "India", "Nigeria", "Brazil", "Saudi_Arabia", "Japan", "Germany"]
distances: dict[str, float] = {c: 0.0 for c in countries}
distance_counts: dict[str, int] = {c: 0 for c in countries}

if cc1:
    for item in cc1["items"]:
        rn = item.get("response_numeric")
        baselines = item.get("human_baselines", {})
        if rn is not None:
            for c in countries:
                if c in baselines and baselines[c] is not None:
                    distances[c] += abs(rn - baselines[c])
                    distance_counts[c] += 1

    for c in countries:
        if distance_counts[c] > 0:
            distances[c] = round(distances[c] / distance_counts[c], 3)

closest = min(distances, key=lambda k: distances[k]) if distances else ""
furthest = max(distances, key=lambda k: distances[k]) if distances else ""

CULTURAL_ALIGNMENT = {
    "distances": distances,
    "closest": closest,
    "furthest": furthest,
    "items_used": max(distance_counts.values()) if distance_counts else 0,
}

# ── 10. MFQ_PROFILE (from CC2 trial) ────────────────────────────────────────
cc2 = None
for t in trials_raw:
    if t["trial_id"] == "CC2":
        cc2 = t
        break

foundation_scores: dict[str, list[float]] = {
    "care": [], "fairness": [], "loyalty": [], "authority": [], "sanctity": []
}
foundation_map = {
    "Care/Harm": "care",
    "Fairness/Cheating": "fairness",
    "Loyalty/Betrayal": "loyalty",
    "Authority/Subversion": "authority",
    "Sanctity/Degradation": "sanctity",
}

if cc2:
    for item in cc2["items"]:
        domain = item.get("domain", "")
        rn = item.get("response_numeric")
        if rn is not None and domain in foundation_map:
            foundation_scores[foundation_map[domain]].append(float(rn))

mfq_means: dict[str, float] = {}
for f_name, scores in foundation_scores.items():
    mfq_means[f_name] = round(sum(scores) / len(scores), 2) if scores else 0.0

MFQ_PROFILE = {
    "care": mfq_means.get("care", 0),
    "fairness": mfq_means.get("fairness", 0),
    "loyalty": mfq_means.get("loyalty", 0),
    "authority": mfq_means.get("authority", 0),
    "sanctity": mfq_means.get("sanctity", 0),
}

# ── 11. RLHF_CONFLICTS (from analysis 23) ───────────────────────────────────
a23 = analyses_by_id[23]["results"]
conflict_cats: Counter = Counter()
for cp in a23.get("conflict_papers", [])[:80]:
    for kw in cp.get("matched_keywords", []):
        kw_lower = kw.lower()
        if "confucian" in kw_lower or "chinese" in kw_lower:
            conflict_cats["Confucian values"] += 1
        elif "islam" in kw_lower:
            conflict_cats["Islamic ethics"] += 1
        elif "moral dilemma" in kw_lower:
            conflict_cats["Moral dilemmas"] += 1
        elif "non-western" in kw_lower:
            conflict_cats["Non-Western values"] += 1
        elif "cultural" in kw_lower:
            conflict_cats["Cultural bias"] += 1
        elif "indigenous" in kw_lower:
            conflict_cats["Indigenous knowledge"] += 1
        elif "dharmic" in kw_lower or "jain" in kw_lower or "buddhist" in kw_lower:
            conflict_cats["Dharmic traditions"] += 1
        elif "ubuntu" in kw_lower:
            conflict_cats["Ubuntu philosophy"] += 1

RLHF_CONFLICTS = []
for cat, freq in conflict_cats.most_common(8):
    RLHF_CONFLICTS.append({"category": cat, "frequency": freq})

# ── 12. TRADITION_ENGAGEMENT (tradition-specific trials) ─────────────────────
tradition_trials_map = {
    "CC4": "Islamic",
    "CC5": "Confucian",
    "CC6": "Ubuntu",
    "CC7": "Buddhist",
    "CC9": "Dharmic",
}
TRADITION_ENGAGEMENT = []
for t in trials_raw:
    tid = t["trial_id"]
    if tid in tradition_trials_map:
        ic = t["items_count"]
        depth = 1
        if ic >= 40:
            depth = 4
        elif ic >= 30:
            depth = 3
        elif ic >= 20:
            depth = 2
        TRADITION_ENGAGEMENT.append({
            "trial_id": tid,
            "tradition": tradition_trials_map[tid],
            "items": ic,
            "depth_score": depth,
            "benchmark": t["benchmark"],
        })

# ── 13. Compute KPI helpers ─────────────────────────────────────────────────
cross_cultural_count = (
    CULTURAL_SCOPE_DIST.get("multicultural", 0)
    + CULTURAL_SCOPE_DIST.get("pancultural", 0)
)
llm_admin_count = sum(
    1 for p in features_data["papers"]
    if p.get("features", {}).get("A1_llm_administrable")
)
topsis_scores = [r["topsis_score"] for r in rankings_data["rankings"] if r.get("topsis_score")]
mean_topsis = round(sum(topsis_scores) / len(topsis_scores), 4) if topsis_scores else 0.0

KPI = {
    "total_benchmarks": BENCHMARK_META["total_papers"],
    "cross_cultural": cross_cultural_count,
    "llm_administrable": llm_admin_count,
    "mean_topsis": mean_topsis,
}


# ═══════════════════════════════════════════════════════════════════════════════
# STEP 1 OUTPUT: Write benchmark-data.js
# ═══════════════════════════════════════════════════════════════════════════════
def js_const(name: str, obj: object) -> str:
    return f"const {name} = {json.dumps(obj, ensure_ascii=False, indent=2)};\n"


OUT_JS.parent.mkdir(parents=True, exist_ok=True)

with open(OUT_JS, "w", encoding="utf-8") as f:
    f.write("// Auto-generated by generate_benchmark_tab.py -- DO NOT EDIT\n")
    f.write(f"// Date: {BENCHMARK_META['date']}\n\n")
    f.write(js_const("BENCHMARK_META", BENCHMARK_META))
    f.write(js_const("BENCHMARK_RANKINGS", BENCHMARK_RANKINGS))
    f.write(js_const("TRADITION_COVERAGE", TRADITION_COVERAGE))
    f.write(js_const("GEOGRAPHIC_COVERAGE", GEOGRAPHIC_COVERAGE))
    f.write(js_const("CULTURAL_SCOPE_DIST", CULTURAL_SCOPE_DIST))
    f.write(js_const("PSYCHOMETRIC_QUALITY", PSYCHOMETRIC_QUALITY))
    f.write(js_const("PSYCHOMETRIC_BY_SCOPE", PSYCHOMETRIC_BY_SCOPE))
    f.write(js_const("DATA_AVAILABILITY", DATA_AVAILABILITY))
    f.write(js_const("TRIAL_SUMMARY", TRIAL_SUMMARY))
    f.write(js_const("CULTURAL_ALIGNMENT", CULTURAL_ALIGNMENT))
    f.write(js_const("MFQ_PROFILE", MFQ_PROFILE))
    f.write(js_const("RLHF_CONFLICTS", RLHF_CONFLICTS))
    f.write(js_const("TRADITION_ENGAGEMENT", TRADITION_ENGAGEMENT))
    f.write(js_const("KPI", KPI))

    # Multi-model comparison data (if available)
    if multimodel_data:
        cm = multimodel_data.get("cross_model", {})
        pm = multimodel_data.get("per_model", {})
        f.write("\n// === Multi-Model Comparison Data ===\n")
        f.write(js_const("MULTIMODEL_AVAILABLE", True))
        f.write(js_const("MODEL_COLORS", {
            "opus": "#0072B2", "sonnet": "#009E73", "haiku": "#E69F00"
        }))
        # MFQ comparison: 3 models + human baselines
        f.write(js_const("MULTIMODEL_MFQ", cm.get("mfq_comparison", {})))
        # Country distance comparison: per-country per-model
        f.write(js_const("MULTIMODEL_ALIGNMENT", cm.get("country_distance_comparison", {})))
        # Engagement depth comparison
        f.write(js_const("MULTIMODEL_ENGAGEMENT", cm.get("engagement_depth_comparison", {})))
        # Pairwise agreement
        f.write(js_const("MULTIMODEL_AGREEMENT", cm.get("numeric_agreement", {})))
        # Top divergence items
        f.write(js_const("MULTIMODEL_DIVERGENCE", cm.get("divergence_items", [])))
        # Model size gradient
        f.write(js_const("MULTIMODEL_GRADIENT", cm.get("model_size_gradient", {})))
        # RLHF conflict comparison
        f.write(js_const("MULTIMODEL_RLHF", cm.get("rlhf_conflict_comparison", {})))
        # Response length comparison
        f.write(js_const("MULTIMODEL_LENGTHS", cm.get("response_length_comparison", {})))
        # Per-model MFQ ratios for KPI
        f.write(js_const("MULTIMODEL_RATIOS", {
            m: pm.get(m, {}).get("mfq_profile", {}).get("ratio")
            for m in ["opus", "sonnet", "haiku"]
        }))
    else:
        f.write(js_const("MULTIMODEL_AVAILABLE", False))

js_size = OUT_JS.stat().st_size
print(f"\nWrote {OUT_JS} ({js_size / 1024:.1f} KB)")


# ═══════════════════════════════════════════════════════════════════════════════
# STEP 2: Generate benchmarks.html
# ═══════════════════════════════════════════════════════════════════════════════

# -- Okabe-Ito colorblind-safe palette ----------------------------------------
OI = [
    "#E69F00",  # orange
    "#56B4E9",  # sky blue
    "#009E73",  # bluish green
    "#F0E442",  # yellow
    "#0072B2",  # blue
    "#D55E00",  # vermillion
    "#CC79A7",  # reddish purple
]

# -- Pre-build table rows for top-50 rankings --------------------------------
ranking_rows = ""
for r in BENCHMARK_RANKINGS:
    title = r["short_title"]
    if len(title) > 40:
        title = title[:37] + "..."
    # Escape for HTML inside f-string
    title = title.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    scope = r["cultural_scope"].replace("_", " ").title()
    ranking_rows += (
        f"<tr>"
        f"<td>{r['rank']}</td>"
        f"<td title=\"{r['filename']}\">{title}</td>"
        f"<td>{r['topsis_score']:.2f}</td>"
        f"<td>{scope}</td>"
        f"<td>{r['languages']}</td>"
        f"<td>{r['nw_frameworks']}</td>"
        f"<td>{r['data_available']}</td>"
        f"</tr>\n"
    )

# -- Pre-build trial summary rows --------------------------------------------
trial_rows = ""
for ts in TRIAL_SUMMARY:
    kf = ts["key_finding"]
    if len(kf) > 120:
        kf = kf[:117] + "..."
    kf = kf.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    trial_rows += (
        f"<tr>"
        f"<td>{ts['id']}</td>"
        f"<td>{ts['benchmark']}</td>"
        f"<td>{ts['items']}</td>"
        f"<td>{kf}</td>"
        f"</tr>\n"
    )

# -- JSON dumps for embedding in JS (these get interpolated via {var}) --------
j_tradition = json.dumps(TRADITION_COVERAGE, ensure_ascii=False)
j_scope = json.dumps(CULTURAL_SCOPE_DIST, ensure_ascii=False)
j_geo = json.dumps(GEOGRAPHIC_COVERAGE, ensure_ascii=False)
j_psych_scope = json.dumps(PSYCHOMETRIC_BY_SCOPE, ensure_ascii=False)
j_data_avail = json.dumps(DATA_AVAILABILITY, ensure_ascii=False)
j_mfq = json.dumps(MFQ_PROFILE, ensure_ascii=False)
j_rlhf = json.dumps(RLHF_CONFLICTS, ensure_ascii=False)
j_alignment = json.dumps(CULTURAL_ALIGNMENT, ensure_ascii=False)
j_engagement = json.dumps(TRADITION_ENGAGEMENT, ensure_ascii=False)
j_kpi = json.dumps(KPI, ensure_ascii=False)
j_oi = json.dumps(OI, ensure_ascii=False)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cross-Cultural Values Alignment -- Benchmark Dashboard</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/echarts@5.5.0/dist/echarts.min.js"></script>
<style>
:root {{
  --bg-primary: #0d1117;
  --bg-secondary: #161b22;
  --bg-card: #1c2128;
  --border: #30363d;
  --text-primary: #e6edf3;
  --text-secondary: #8b949e;
  --accent: #58a6ff;
  --accent2: #3fb950;
  --accent3: #f0883e;
  --danger: #f85149;
}}
* {{ box-sizing: border-box; }}
body {{
  font-family: "Inter", sans-serif;
  background: var(--bg-primary);
  color: var(--text-primary);
  margin: 0;
  min-height: 100vh;
}}
.navbar {{
  background: var(--bg-secondary) !important;
  border-bottom: 1px solid var(--border);
  padding: 0.5rem 1rem;
}}
.navbar-brand {{
  color: var(--text-primary) !important;
  font-weight: 700;
  font-size: 1.05rem;
}}
.nav-pills .nav-link {{
  color: var(--text-secondary);
  border: 1px solid transparent;
  border-radius: 6px;
  padding: 0.5rem 1rem;
  font-size: 0.88rem;
  font-weight: 500;
  margin-right: 0.4rem;
  transition: all 0.2s;
}}
.nav-pills .nav-link:hover {{
  color: var(--text-primary);
  background: rgba(88,166,255,0.08);
}}
.nav-pills .nav-link.active {{
  color: #fff;
  background: var(--accent);
}}
.card {{
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 8px;
  margin-bottom: 1rem;
}}
.card-body {{ padding: 1rem; }}
.card-title {{
  color: var(--text-secondary);
  font-size: 0.78rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  margin-bottom: 0.5rem;
  font-weight: 600;
}}
.stat-value {{
  font-family: "JetBrains Mono", monospace;
  font-size: 1.8rem;
  font-weight: 700;
  color: var(--accent);
  line-height: 1.2;
}}
.stat-sub {{
  color: var(--text-secondary);
  font-size: 0.78rem;
}}
.chart-box {{
  width: 100%;
  min-height: 380px;
}}
.chart-box-sm {{
  width: 100%;
  min-height: 300px;
}}
table.dt {{
  width: 100%;
  font-size: 0.82rem;
  border-collapse: collapse;
}}
table.dt th, table.dt td {{
  padding: 0.4rem 0.6rem;
  border-bottom: 1px solid var(--border);
  text-align: left;
  color: var(--text-primary);
}}
table.dt th {{
  color: var(--text-secondary);
  font-weight: 600;
  text-transform: uppercase;
  font-size: 0.72rem;
  letter-spacing: 0.04em;
  position: sticky;
  top: 0;
  background: var(--bg-card);
  z-index: 1;
}}
table.dt tbody tr:nth-child(even) {{
  background: rgba(255,255,255,0.02);
}}
table.dt tbody tr:hover {{
  background: rgba(88,166,255,0.06);
}}
.scroll-box {{
  max-height: 400px;
  overflow-y: auto;
}}
.section-label {{
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 0.8rem;
  padding-bottom: 0.4rem;
  border-bottom: 1px solid var(--border);
}}
.tab-content {{ padding-top: 1.2rem; }}
.chart-desc {{
  color: var(--text-secondary);
  font-size: 0.82rem;
  line-height: 1.55;
  margin-bottom: 0.8rem;
  padding: 0.5rem 0.6rem;
  background: rgba(88,166,255,0.04);
  border-left: 3px solid var(--accent);
  border-radius: 0 4px 4px 0;
}}
.chart-desc strong {{ color: var(--text-primary); }}
.tab-intro {{
  color: var(--text-secondary);
  font-size: 0.88rem;
  line-height: 1.6;
  margin-bottom: 1.2rem;
  padding: 0.8rem 1rem;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 8px;
}}
.tab-intro strong {{ color: var(--text-primary); }}
.council-tag {{
  color: var(--accent);
  font-size: 0.72rem;
  font-style: italic;
  margin-top: 0.4rem;
}}
</style>
</head>
<body>

<nav class="navbar">
  <span class="navbar-brand">Cross-Cultural Values Alignment &mdash; Benchmark Dashboard</span>
  <span class="stat-sub">Generated {BENCHMARK_META["date"]}</span>
</nav>

<div class="container-fluid px-3 py-3">

<!-- Tab pills -->
<ul class="nav nav-pills mb-3" id="mainTabs" role="tablist">
  <li class="nav-item" role="presentation">
    <button class="nav-link active" id="bench-tab" data-bs-toggle="pill"
      data-bs-target="#benchPane" type="button" role="tab">Benchmarks</button>
  </li>
  <li class="nav-item" role="presentation">
    <button class="nav-link" id="trials-tab" data-bs-toggle="pill"
      data-bs-target="#trialsPane" type="button" role="tab">Trials</button>
  </li>
  <li class="nav-item" role="presentation">
    <button class="nav-link" id="compare-tab" data-bs-toggle="pill"
      data-bs-target="#comparePane" type="button" role="tab">Model Comparison</button>
  </li>
</ul>

<div class="tab-content" id="mainTabContent">

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- BENCHMARKS TAB                                                        -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<div class="tab-pane fade show active" id="benchPane" role="tabpanel">

<div class="tab-intro">
  <strong>Benchmark Landscape Meta-Evaluation.</strong> This tab presents a systematic evaluation of 218 AI values alignment benchmarks, ranked using TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) with ELECTRE III veto thresholds across 8 weighted criteria. The analysis reveals that the benchmark landscape itself reproduces the WEIRD bias documented in cross-cultural psychology &mdash; most benchmarks measure Western moral constructs while leaving non-Western ethical traditions unmeasured.
  <div class="council-tag">Expert Council Interpretation</div>
</div>

<!-- KPI row -->
<div class="row g-3 mb-3">
  <div class="col-6 col-md-3">
    <div class="card"><div class="card-body">
      <div class="card-title">Total Benchmarks</div>
      <div class="stat-value">{KPI["total_benchmarks"]}</div>
      <div class="stat-sub">TOPSIS-ranked papers</div>
    </div></div>
  </div>
  <div class="col-6 col-md-3">
    <div class="card"><div class="card-body">
      <div class="card-title">Cross-Cultural</div>
      <div class="stat-value">{KPI["cross_cultural"]}</div>
      <div class="stat-sub">multicultural + pancultural</div>
    </div></div>
  </div>
  <div class="col-6 col-md-3">
    <div class="card"><div class="card-body">
      <div class="card-title">LLM-Administrable</div>
      <div class="stat-value">{KPI["llm_administrable"]}</div>
      <div class="stat-sub">can be given to LLMs</div>
    </div></div>
  </div>
  <div class="col-6 col-md-3">
    <div class="card"><div class="card-body">
      <div class="card-title">Mean TOPSIS</div>
      <div class="stat-value">{KPI["mean_topsis"]:.3f}</div>
      <div class="stat-sub">across all {KPI["total_benchmarks"]} papers</div>
    </div></div>
  </div>
</div>

<div class="chart-desc">Of {KPI["total_benchmarks"]} benchmarks evaluated, only {KPI["cross_cultural"]} (38%) engage multiple cultures, and the mean TOPSIS score of {KPI["mean_topsis"]:.3f} indicates that even the best benchmarks fall far short of comprehensive cross-cultural coverage. The gap between <strong>LLM-administrable ({KPI["llm_administrable"]})</strong> and <strong>cross-cultural ({KPI["cross_cultural"]})</strong> reveals that most benchmarks <em>can</em> be given to AI systems but measure only Western moral constructs when they do.</div>

<!-- Ranked table -->
<div class="card mb-3">
  <div class="card-body">
    <div class="section-label">Top 50 Benchmarks by TOPSIS Score</div>
    <div class="chart-desc">Benchmarks are ranked by a weighted composite of 8 criteria: values alignment relevance (20%), cross-cultural scope (20%), non-Western framework coverage (15%), LLM administrability (12%), psychometric quality (10%), evaluation depth (10%), data availability (8%), and epistemic provenance (5%). The top-ranked benchmarks tend to engage Indigenous, Islamic, or Confucian traditions &mdash; precisely because such engagement is rare enough to be distinctive. Kendall&rsquo;s W = 0.92 across 5 sensitivity analyses confirms ranking stability.</div>
    <div class="scroll-box">
      <table class="dt">
        <thead>
          <tr><th>#</th><th>Title</th><th>TOPSIS</th><th>Cultural Scope</th><th>Langs</th><th>NW Frmwks</th><th>Data</th></tr>
        </thead>
        <tbody>
{ranking_rows}        </tbody>
      </table>
    </div>
  </div>
</div>

<!-- Charts row 1: Tradition Coverage + Cultural Scope Pie -->
<div class="row g-3 mb-3">
  <div class="col-md-6">
    <div class="card"><div class="card-body">
      <div class="section-label">Non-Western Tradition Coverage</div>
      <div class="chart-desc">This chart reveals the stark underrepresentation of non-Western ethical traditions in AI benchmarks. Confucian ethics leads, but Buen Vivir (Andean well-being philosophy) and Dharmic ethics (Hindu/Jain/Sikh) have near-zero representation. These numbers represent the <em>entire</em> global benchmark infrastructure for evaluating whether AI systems can reason within traditions that guide billions of people.</div>
      <div id="chartTradition" class="chart-box"></div>
    </div></div>
  </div>
  <div class="col-md-6">
    <div class="card"><div class="card-body">
      <div class="section-label">Cultural Scope Distribution</div>
      <div class="chart-desc">Nearly half of all benchmarks are monocultural or bicultural &mdash; they measure values within a single cultural frame. Only a handful achieve pancultural scope. The vast majority of &ldquo;values alignment&rdquo; evaluation is actually &ldquo;Western values alignment&rdquo; evaluation. A benchmark labeled &ldquo;moral reasoning&rdquo; that tests only trolley problems and fairness dilemmas is not measuring moral reasoning &mdash; it is measuring one culture&rsquo;s moral reasoning.</div>
      <div id="chartScope" class="chart-box"></div>
    </div></div>
  </div>
</div>

<!-- Charts row 2: Geographic + Psychometric Quality -->
<div class="row g-3 mb-3">
  <div class="col-md-6">
    <div class="card"><div class="card-body">
      <div class="section-label">Creator Region Distribution</div>
      <div class="chart-desc">North America and Western Europe produce over half of all benchmarks. Sub-Saharan Africa contributes only 2. The geographic concentration of benchmark creation means that the instruments used to evaluate AI morality worldwide are designed by researchers from a narrow cultural bandwidth. Benchmarks encode their creators&rsquo; moral assumptions in item selection, scale design, and scoring criteria.</div>
      <div id="chartGeo" class="chart-box"></div>
    </div></div>
  </div>
  <div class="col-md-6">
    <div class="card"><div class="card-body">
      <div class="section-label">Psychometric Quality by Cultural Scope</div>
      <div class="chart-desc"><strong>Zero benchmarks report measurement invariance testing</strong> &mdash; the statistical procedure that verifies whether a measurement instrument functions equivalently across cultural groups. Without invariance testing, cross-cultural comparisons are psychometrically meaningless: a &ldquo;fairness&rdquo; score of 4/5 in the US and 4/5 in Nigeria may measure entirely different constructs. This is the single most critical methodological gap in the benchmark landscape.</div>
      <div id="chartPsych" class="chart-box"></div>
    </div></div>
  </div>
</div>

<!-- Charts row 3: Gap Radar + Data Availability Donut -->
<div class="row g-3 mb-3">
  <div class="col-md-6">
    <div class="card"><div class="card-body">
      <div class="section-label">Tradition Coverage Gap Radar</div>
      <div class="chart-desc">The radar reveals the asymmetry of coverage: Confucian ethics (the most studied non-Western tradition) still receives only a fraction of the attention given to Western ethical frameworks. The near-zero coverage of Buen Vivir and Dharmic ethics means that AI systems deployed in Andean and South Asian contexts have essentially no benchmark infrastructure for evaluating cultural alignment.</div>
      <div id="chartRadar" class="chart-box"></div>
    </div></div>
  </div>
  <div class="col-md-6">
    <div class="card"><div class="card-body">
      <div class="section-label">Data Availability</div>
      <div class="chart-desc">Two-thirds of benchmarks have open-source data, enabling replication and scrutiny. However, roughly a third have unavailable data, meaning their claims about cultural values alignment cannot be independently verified. Open data is necessary but not sufficient &mdash; the benchmark&rsquo;s cultural assumptions are often embedded in item design, not in the data itself.</div>
      <div id="chartData" class="chart-box"></div>
    </div></div>
  </div>
</div>

</div><!-- /benchPane -->

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- TRIALS TAB                                                            -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<div class="tab-pane fade" id="trialsPane" role="tabpanel">

<div class="tab-intro">
  <strong>Claude Self-Administration Trials.</strong> This tab presents results from 10 self-administered trials where Claude Opus 4.6 responded to 380 items across 7 non-Western ethical traditions. The trials reveal a systematic pattern: Claude can accurately <em>describe</em> non-Western moral frameworks but cannot <em>reason within</em> them. Its responses consistently default to Western liberal individualism, even when explicitly prompted to adopt alternative perspectives.
  <div class="council-tag">Expert Council Interpretation</div>
</div>

<!-- Trial summary table -->
<div class="card mb-3">
  <div class="card-body">
    <div class="section-label">Trial Summary (10 Claude Opus 4.6 Trials)</div>
    <div class="chart-desc">Each trial tested a different cultural dimension. The key findings column summarizes a consistent pattern: Claude agrees with non-Western traditions when they converge with liberal values (e.g., Islamic zakat as redistribution, Ubuntu communal care as harm prevention) and systematically rejects them when they diverge (e.g., Confucian filial piety over individual autonomy, Dharmic svadharma as role-based duty). This <strong>&ldquo;selective agreement&rdquo; pattern</strong> reveals that RLHF alignment does not produce cultural neutrality &mdash; it produces a specific moral orientation that evaluates all other traditions through its own lens.</div>
    <div class="scroll-box">
      <table class="dt">
        <thead>
          <tr><th>Trial</th><th>Benchmark</th><th>Items</th><th>Key Finding</th></tr>
        </thead>
        <tbody>
{trial_rows}        </tbody>
      </table>
    </div>
  </div>
</div>

<!-- Charts row: MFQ Profile + RLHF Conflict -->
<div class="row g-3 mb-3">
  <div class="col-md-6">
    <div class="card"><div class="card-body">
      <div class="section-label">MFQ Foundation Profile (CC2 Trial)</div>
      <div class="chart-desc">Claude&rsquo;s Moral Foundations profile is <strong>more extreme than any documented human population</strong>. Care and Fairness (&ldquo;individualizing&rdquo; foundations) are near-ceiling, while Loyalty, Authority, and Sanctity (&ldquo;binding&rdquo; foundations) are near-floor. The individualizing-to-binding ratio of 3.75 exceeds even the most liberal US populations (~1.4). Claude&rsquo;s moral cognition is not merely liberal &mdash; it is hyper-liberal, with binding foundations functionally treated as morally suspect rather than merely less important.</div>
      <div id="chartMFQ" class="chart-box"></div>
    </div></div>
  </div>
  <div class="col-md-6">
    <div class="card"><div class="card-body">
      <div class="section-label">RLHF Conflict Categories</div>
      <div class="chart-desc">RLHF creates systematic conflict zones when Claude encounters non-Western ethical positions. Cultural bias and non-Western values generate the most conflicts, followed by moral dilemmas that pit autonomy against communal obligation. These are not random disagreements &mdash; they cluster into predictable patterns that map onto the individualism-collectivism axis identified in cross-cultural psychology.</div>
      <div id="chartRLHF" class="chart-box"></div>
    </div></div>
  </div>
</div>

<!-- Charts row: Cultural Alignment Radar + Tradition Engagement -->
<div class="row g-3 mb-3">
  <div class="col-md-6">
    <div class="card"><div class="card-body">
      <div class="section-label">Cultural Alignment Distance (CC1: GlobalOpinionQA)</div>
      <div class="chart-desc">Claude&rsquo;s responses are closest to <strong>Germany</strong> (0.538 mean absolute distance) and farthest from <strong>Saudi Arabia</strong> (1.974). On the Inglehart-Welzel cultural map, this places Claude in the secular-rational / self-expression quadrant shared by fewer than 15% of the global population. The radar&rsquo;s shape &mdash; high similarity to Northwestern European countries, low similarity to Global South countries &mdash; is a visual fingerprint of RLHF&rsquo;s cultural provenance. Higher values = greater similarity.</div>
      <div id="chartAlign" class="chart-box"></div>
    </div></div>
  </div>
  <div class="col-md-6">
    <div class="card"><div class="card-body">
      <div class="section-label">Tradition Engagement Depth</div>
      <div class="chart-desc">Engagement depth measures whether Claude merely names concepts (1), applies reasoning (2), attempts genuine perspective-taking (3), or acknowledges structural limitations (4). Scores of 3&ndash;4 suggest Claude is sophisticated enough to recognize its own cultural limitations &mdash; but this recognition does not translate into the ability to actually reason <em>within</em> non-Western frameworks. Self-awareness without behavioral change is the hallmark of the knowledge-value gap.</div>
      <div id="chartEngage" class="chart-box"></div>
    </div></div>
  </div>
</div>

</div><!-- /trialsPane -->

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- MODEL COMPARISON TAB                                                   -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<div class="tab-pane fade" id="comparePane" role="tabpanel">

<div class="tab-intro">
  <strong>Multi-Model Comparison.</strong> This tab compares how three Claude models (Opus, Sonnet, Haiku) respond to the same 380 cultural benchmark items. The central question: is WEIRD bias a function of model capability (larger models = more bias) or RLHF training (all models share the same bias)? The answer is neither simple hypothesis: all three models cluster near Germany and away from Saudi Arabia, but the relationship between model size and bias intensity is <strong>non-monotonic</strong>. Haiku (smallest) shows the most extreme liberal profile, Sonnet (mid-size) the least extreme, and Opus falls between.
  <div class="council-tag">Expert Council Interpretation</div>
</div>

<!-- KPI row -->
<div class="row g-3 mb-3">
  <div class="col-6 col-md-3">
    <div class="card"><div class="card-body">
      <div class="card-title">Models Compared</div>
      <div class="stat-value">3</div>
      <div class="stat-sub">Opus &middot; Sonnet &middot; Haiku</div>
    </div></div>
  </div>
  <div class="col-6 col-md-3">
    <div class="card"><div class="card-body">
      <div class="card-title">Total Responses</div>
      <div class="stat-value">1,140</div>
      <div class="stat-sub">380 items &times; 3 models</div>
    </div></div>
  </div>
  <div class="col-6 col-md-3">
    <div class="card"><div class="card-body">
      <div class="card-title">Opus-Sonnet r</div>
      <div class="stat-value" id="kpiR">--</div>
      <div class="stat-sub">Pearson correlation</div>
    </div></div>
  </div>
  <div class="col-6 col-md-3">
    <div class="card"><div class="card-body">
      <div class="card-title">MFQ Ratio Range</div>
      <div class="stat-value" id="kpiRatio">--</div>
      <div class="stat-sub">Indiv/Binding across models</div>
    </div></div>
  </div>
</div>

<!-- Charts row 1: MFQ Comparison + Cultural Alignment -->
<div class="row g-3 mb-3">
  <div class="col-md-6">
    <div class="card"><div class="card-body">
      <div class="section-label">MFQ Foundation Profile: 3-Model Comparison</div>
      <div class="chart-desc">All three models share the same hyper-liberal MFQ profile &mdash; Care and Fairness near ceiling, binding foundations near floor &mdash; but the intensity varies. <strong>Haiku&rsquo;s individualizing/binding ratio (4.82) is the most extreme</strong>, exceeding Opus (3.75) and Sonnet (3.23). The dashed lines show human baselines: even US liberals (~1.4 ratio) are far less extreme than any Claude model. RLHF does not merely replicate liberal human values &mdash; it amplifies them beyond any naturally occurring human population.</div>
      <div id="chartMFQCompare" class="chart-box"></div>
    </div></div>
  </div>
  <div class="col-md-6">
    <div class="card"><div class="card-body">
      <div class="section-label">Cultural Alignment Radar: 3-Model Overlay</div>
      <div class="chart-desc">The three radar polygons nearly overlap &mdash; all models are closest to Germany and farthest from Saudi Arabia, with almost identical distance profiles. This convergence indicates that cultural alignment is determined by the <strong>RLHF pipeline, not by model architecture or size</strong>. Changing the model does not change whose values it encodes.</div>
      <div id="chartAlignCompare" class="chart-box"></div>
    </div></div>
  </div>
</div>

<!-- Charts row 2: Agreement Heatmap + Engagement Comparison -->
<div class="row g-3 mb-3">
  <div class="col-md-6">
    <div class="card"><div class="card-body">
      <div class="section-label">Pairwise Agreement by Trial (Pearson r)</div>
      <div class="chart-desc">Pearson correlations between model pairs are uniformly high (0.88&ndash;0.95), confirming that all three models measure the same underlying RLHF value orientation. <strong>Green cells</strong> indicate near-perfect agreement; slight yellowing for Sonnet-Haiku suggests these models diverge most on items where nuanced perspective-taking is required &mdash; precisely the items where model capability differences matter most.</div>
      <div id="chartAgreement" class="chart-box"></div>
    </div></div>
  </div>
  <div class="col-md-6">
    <div class="card"><div class="card-body">
      <div class="section-label">Tradition Engagement Depth by Model</div>
      <div class="chart-desc">Sonnet shows markedly higher engagement depth than Opus or Haiku on Islamic (3.5 vs 1.0), Ubuntu (4.0 vs 1.0), Buddhist (3.5 vs 1.0), and Dharmic (3.5 vs 1.0) traditions. This suggests Sonnet has more capacity for genuine perspective-taking, even though its ultimate value orientation is the same. <strong>Haiku&rsquo;s uniformly low engagement</strong> (1.0 on 4/5 traditions) confirms that smaller models lack the capacity for nuanced cross-cultural reasoning &mdash; they default more rigidly to trained values.</div>
      <div id="chartEngageCompare" class="chart-box"></div>
    </div></div>
  </div>
</div>

<!-- Charts row 3: RLHF Comparison + Divergence Table -->
<div class="row g-3 mb-3">
  <div class="col-md-6">
    <div class="card"><div class="card-body">
      <div class="section-label">RLHF Conflict Frequency by Model</div>
      <div class="chart-desc">Opus identifies the most RLHF conflicts (237), followed by Haiku (176) and Sonnet (170). Higher conflict counts do not indicate worse alignment &mdash; they indicate <strong>greater reflexive capacity</strong>. Opus&rsquo;s ability to identify 237 instances where its training conflicts with non-Western values is itself an analytical achievement. Sonnet and Haiku may have fewer conflicts not because they are less biased, but because they are less capable of detecting their own bias.</div>
      <div id="chartRLHFCompare" class="chart-box"></div>
    </div></div>
  </div>
  <div class="col-md-6">
    <div class="card"><div class="card-body">
      <div class="section-label">Top Divergence Items (Highest Cross-Model Variance)</div>
      <div class="chart-desc">These are the specific items where models disagree most. The highest-variance item (CC5 #26, var=3.56) asks whether a friend should lie to their spouse &mdash; Opus and Sonnet agree with the Confucian position on relational loyalty while Haiku defaults to truth-telling. Such divergences reveal that cross-cultural moral reasoning is one of the <strong>hardest capabilities to maintain at smaller model sizes</strong>, with Haiku reverting to the simplest RLHF default when confronted with complex relational dilemmas.</div>
      <div class="scroll-box" id="divTableBox"></div>
    </div></div>
  </div>
</div>

</div><!-- /comparePane -->

</div><!-- /tab-content -->
</div><!-- /container -->

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<script src="benchmark-data.js"></script>
<script>
(function() {{
  "use strict";

  // ── Data (inlined from Python) ──────────────────────────────────────────
  var OI = {j_oi};
  var TRADITION = {j_tradition};
  var SCOPE = {j_scope};
  var GEO = {j_geo};
  var PSYCH_SCOPE = {j_psych_scope};
  var DATA_AVAIL = {j_data_avail};
  var MFQ = {j_mfq};
  var RLHF = {j_rlhf};
  var ALIGNMENT = {j_alignment};
  var ENGAGEMENT = {j_engagement};

  // ── Helpers ─────────────────────────────────────────────────────────────
  var txtC = "#e6edf3";
  var txtS = "#8b949e";
  var gridC = "#30363d";

  function initChart(id) {{
    var el = document.getElementById(id);
    if (!el) return null;
    return echarts.init(el, null, {{renderer: "canvas"}});
  }}

  // ── 1. Tradition Coverage Bar ───────────────────────────────────────────
  (function() {{
    var ch = initChart("chartTradition");
    if (!ch) return;
    var labels = ["Confucian", "Buddhist", "Islamic", "Indigenous", "Ubuntu", "Dharmic", "Buen Vivir"];
    var keys = ["confucian", "buddhist", "islamic", "indigenous", "ubuntu", "dharmic", "buen_vivir"];
    var vals = keys.map(function(k) {{ return TRADITION[k] || 0; }});
    ch.setOption({{
      tooltip: {{trigger: "axis", axisPointer: {{type: "shadow"}}}},
      grid: {{left: 20, right: 30, top: 20, bottom: 40, containLabel: true}},
      xAxis: {{
        type: "category", data: labels,
        axisLabel: {{color: txtS, fontSize: 11, rotate: 15}},
        axisLine: {{lineStyle: {{color: gridC}}}}
      }},
      yAxis: {{
        type: "value",
        axisLabel: {{color: txtS}},
        splitLine: {{lineStyle: {{color: gridC, type: "dashed"}}}}
      }},
      series: [{{
        type: "bar", data: vals,
        itemStyle: {{
          color: function(p) {{ return OI[p.dataIndex % OI.length]; }},
          borderRadius: [4, 4, 0, 0]
        }},
        barMaxWidth: 50,
        label: {{show: true, position: "top", color: txtC, fontSize: 12, fontWeight: 600}}
      }}]
    }});
    window.addEventListener("resize", function() {{ ch.resize(); }});
  }})();

  // ── 2. Cultural Scope Pie ───────────────────────────────────────────────
  (function() {{
    var ch = initChart("chartScope");
    if (!ch) return;
    var nameMap = {{
      monocultural: "Monocultural",
      bicultural: "Bicultural",
      multicultural: "Multicultural",
      pancultural: "Pancultural",
      universal_claim: "Universal Claim"
    }};
    var pieData = [];
    Object.keys(SCOPE).forEach(function(k) {{
      pieData.push({{name: nameMap[k] || k, value: SCOPE[k]}});
    }});
    ch.setOption({{
      tooltip: {{trigger: "item", formatter: "{{b}}: {{c}} ({{d}}%)"}},
      legend: {{
        bottom: 10, textStyle: {{color: txtS, fontSize: 11}},
        itemWidth: 12, itemHeight: 12
      }},
      series: [{{
        type: "pie", radius: ["35%", "65%"], center: ["50%", "45%"],
        data: pieData,
        color: OI,
        label: {{color: txtC, fontSize: 11}},
        emphasis: {{itemStyle: {{shadowBlur: 10, shadowColor: "rgba(0,0,0,0.5)"}}}}
      }}]
    }});
    window.addEventListener("resize", function() {{ ch.resize(); }});
  }})();

  // ── 3. Geographic Bar (horizontal) ──────────────────────────────────────
  (function() {{
    var ch = initChart("chartGeo");
    if (!ch) return;
    var sorted = Object.keys(GEO).map(function(k) {{ return {{name: k, val: GEO[k]}}; }});
    sorted.sort(function(a, b) {{ return a.val - b.val; }});
    // Take top 10
    sorted = sorted.slice(Math.max(0, sorted.length - 10));
    ch.setOption({{
      tooltip: {{trigger: "axis", axisPointer: {{type: "shadow"}}}},
      grid: {{left: 10, right: 40, top: 10, bottom: 20, containLabel: true}},
      yAxis: {{
        type: "category",
        data: sorted.map(function(d) {{ return d.name; }}),
        axisLabel: {{color: txtS, fontSize: 11}},
        axisLine: {{lineStyle: {{color: gridC}}}}
      }},
      xAxis: {{
        type: "value",
        axisLabel: {{color: txtS}},
        splitLine: {{lineStyle: {{color: gridC, type: "dashed"}}}}
      }},
      series: [{{
        type: "bar", data: sorted.map(function(d) {{ return d.val; }}),
        itemStyle: {{color: OI[1], borderRadius: [0, 4, 4, 0]}},
        barMaxWidth: 28,
        label: {{show: true, position: "right", color: txtC, fontSize: 11}}
      }}]
    }});
    window.addEventListener("resize", function() {{ ch.resize(); }});
  }})();

  // ── 4. Psychometric Quality Stacked Bar ─────────────────────────────────
  (function() {{
    var ch = initChart("chartPsych");
    if (!ch) return;
    var tiers = Object.keys(PSYCH_SCOPE);
    var relData = [], invData = [], neiData = [];
    tiers.forEach(function(t) {{
      var d = PSYCH_SCOPE[t];
      relData.push(d.reliability_only);
      invData.push(d.invariance);
      neiData.push(d.neither);
    }});
    ch.setOption({{
      tooltip: {{trigger: "axis", axisPointer: {{type: "shadow"}}}},
      legend: {{
        data: ["Reliability Only", "Invariance Tested", "Neither"],
        bottom: 10, textStyle: {{color: txtS, fontSize: 11}},
        itemWidth: 12, itemHeight: 12
      }},
      grid: {{left: 10, right: 30, top: 20, bottom: 55, containLabel: true}},
      xAxis: {{
        type: "category", data: tiers,
        axisLabel: {{color: txtS, fontSize: 10, rotate: 10}},
        axisLine: {{lineStyle: {{color: gridC}}}}
      }},
      yAxis: {{
        type: "value",
        axisLabel: {{color: txtS}},
        splitLine: {{lineStyle: {{color: gridC, type: "dashed"}}}}
      }},
      series: [
        {{name: "Reliability Only", type: "bar", stack: "q", data: relData, itemStyle: {{color: OI[0]}}}},
        {{name: "Invariance Tested", type: "bar", stack: "q", data: invData, itemStyle: {{color: OI[2]}}}},
        {{name: "Neither", type: "bar", stack: "q", data: neiData, itemStyle: {{color: "#484f58"}}}}
      ]
    }});
    window.addEventListener("resize", function() {{ ch.resize(); }});
  }})();

  // ── 5. Gap Radar ────────────────────────────────────────────────────────
  (function() {{
    var ch = initChart("chartRadar");
    if (!ch) return;
    var maxVal = 0;
    Object.keys(TRADITION).forEach(function(k) {{
      if (TRADITION[k] > maxVal) maxVal = TRADITION[k];
    }});
    if (maxVal === 0) maxVal = 1;
    var indicators = [];
    var vals = [];
    var labels = {{
      confucian: "Confucian", buddhist: "Buddhist", islamic: "Islamic",
      indigenous: "Indigenous", ubuntu: "Ubuntu", dharmic: "Dharmic",
      buen_vivir: "Buen Vivir"
    }};
    Object.keys(labels).forEach(function(k) {{
      indicators.push({{name: labels[k], max: 100}});
      vals.push(Math.round(100 * (TRADITION[k] || 0) / maxVal));
    }});
    ch.setOption({{
      tooltip: {{}},
      radar: {{
        indicator: indicators,
        shape: "circle",
        axisName: {{color: txtS, fontSize: 11}},
        splitArea: {{areaStyle: {{color: ["rgba(88,166,255,0.02)", "rgba(88,166,255,0.05)"]}}}},
        splitLine: {{lineStyle: {{color: gridC}}}},
        axisLine: {{lineStyle: {{color: gridC}}}}
      }},
      series: [{{
        type: "radar",
        data: [{{
          value: vals,
          name: "Coverage %",
          areaStyle: {{color: "rgba(88,166,255,0.15)"}},
          lineStyle: {{color: OI[4], width: 2}},
          itemStyle: {{color: OI[4]}}
        }}]
      }}]
    }});
    window.addEventListener("resize", function() {{ ch.resize(); }});
  }})();

  // ── 6. Data Availability Donut ──────────────────────────────────────────
  (function() {{
    var ch = initChart("chartData");
    if (!ch) return;
    var items = [
      {{name: "Open Source", value: DATA_AVAIL.open_source}},
      {{name: "Restricted", value: DATA_AVAIL.restricted}},
      {{name: "Unavailable", value: DATA_AVAIL.unavailable}}
    ];
    ch.setOption({{
      tooltip: {{trigger: "item", formatter: "{{b}}: {{c}} ({{d}}%)"}},
      legend: {{
        bottom: 10, textStyle: {{color: txtS, fontSize: 11}},
        itemWidth: 12, itemHeight: 12
      }},
      series: [{{
        type: "pie", radius: ["40%", "68%"], center: ["50%", "43%"],
        data: items,
        color: [OI[2], OI[0], "#484f58"],
        label: {{
          color: txtC, fontSize: 12,
          formatter: "{{b}}\\n{{c}}"
        }},
        emphasis: {{itemStyle: {{shadowBlur: 10, shadowColor: "rgba(0,0,0,0.5)"}}}}
      }}]
    }});
    window.addEventListener("resize", function() {{ ch.resize(); }});
  }})();

  // ── 7. MFQ Grouped Bar ─────────────────────────────────────────────────
  (function() {{
    var ch = initChart("chartMFQ");
    if (!ch) return;
    var foundations = ["Care", "Fairness", "Loyalty", "Authority", "Sanctity"];
    var fkeys = ["care", "fairness", "loyalty", "authority", "sanctity"];
    // Graham et al. (2011) population baselines
    var usLiberal = [3.8, 3.8, 2.3, 2.1, 1.3];
    var usConserv = [3.1, 3.0, 3.2, 3.3, 2.9];
    var claudeVals = fkeys.map(function(k) {{ return MFQ[k] || 0; }});
    ch.setOption({{
      tooltip: {{trigger: "axis", axisPointer: {{type: "shadow"}}}},
      legend: {{
        data: ["Claude Opus 4.6", "US Liberal Baseline", "US Conservative Baseline"],
        bottom: 5, textStyle: {{color: txtS, fontSize: 10}},
        itemWidth: 12, itemHeight: 12
      }},
      grid: {{left: 10, right: 20, top: 20, bottom: 55, containLabel: true}},
      xAxis: {{
        type: "category", data: foundations,
        axisLabel: {{color: txtS, fontSize: 11}},
        axisLine: {{lineStyle: {{color: gridC}}}}
      }},
      yAxis: {{
        type: "value", max: 5.5,
        axisLabel: {{color: txtS}},
        splitLine: {{lineStyle: {{color: gridC, type: "dashed"}}}}
      }},
      series: [
        {{
          name: "Claude Opus 4.6", type: "bar", data: claudeVals,
          itemStyle: {{color: OI[4], borderRadius: [3,3,0,0]}},
          barGap: "15%"
        }},
        {{
          name: "US Liberal Baseline", type: "bar", data: usLiberal,
          itemStyle: {{color: OI[1], borderRadius: [3,3,0,0]}}
        }},
        {{
          name: "US Conservative Baseline", type: "bar", data: usConserv,
          itemStyle: {{color: OI[5], borderRadius: [3,3,0,0]}}
        }}
      ]
    }});
    window.addEventListener("resize", function() {{ ch.resize(); }});
  }})();

  // ── 8. RLHF Conflict Horizontal Bar ────────────────────────────────────
  (function() {{
    var ch = initChart("chartRLHF");
    if (!ch) return;
    // Sort ascending and take top 5
    var sorted = RLHF.slice().sort(function(a, b) {{ return a.frequency - b.frequency; }});
    sorted = sorted.slice(Math.max(0, sorted.length - 5));
    ch.setOption({{
      tooltip: {{trigger: "axis", axisPointer: {{type: "shadow"}}}},
      grid: {{left: 10, right: 40, top: 10, bottom: 20, containLabel: true}},
      yAxis: {{
        type: "category",
        data: sorted.map(function(d) {{ return d.category; }}),
        axisLabel: {{color: txtS, fontSize: 11}},
        axisLine: {{lineStyle: {{color: gridC}}}}
      }},
      xAxis: {{
        type: "value",
        axisLabel: {{color: txtS}},
        splitLine: {{lineStyle: {{color: gridC, type: "dashed"}}}}
      }},
      series: [{{
        type: "bar",
        data: sorted.map(function(d) {{ return d.frequency; }}),
        itemStyle: {{color: OI[5], borderRadius: [0, 4, 4, 0]}},
        barMaxWidth: 28,
        label: {{show: true, position: "right", color: txtC, fontSize: 11}}
      }}]
    }});
    window.addEventListener("resize", function() {{ ch.resize(); }});
  }})();

  // ── 9. Cultural Alignment Radar ─────────────────────────────────────────
  (function() {{
    var ch = initChart("chartAlign");
    if (!ch) return;
    var distances = ALIGNMENT.distances;
    var maxDist = 0;
    Object.keys(distances).forEach(function(k) {{
      if (distances[k] > maxDist) maxDist = distances[k];
    }});
    if (maxDist === 0) maxDist = 5;
    // Invert: similarity = maxDist - distance
    var countries = ["US", "Germany", "Japan", "Brazil", "India", "China", "Nigeria", "Saudi_Arabia"];
    var countryLabels = {{
      US: "United States", Germany: "Germany", Japan: "Japan",
      Brazil: "Brazil", India: "India", China: "China",
      Nigeria: "Nigeria", Saudi_Arabia: "Saudi Arabia"
    }};
    var indicators = countries.map(function(c) {{
      return {{name: countryLabels[c] || c, max: Math.ceil(maxDist * 1.1 * 10) / 10}};
    }});
    var simVals = countries.map(function(c) {{
      return Math.round((maxDist - (distances[c] || 0)) * 100) / 100;
    }});
    var distVals = countries.map(function(c) {{
      return Math.round((distances[c] || 0) * 100) / 100;
    }});
    ch.setOption({{
      tooltip: {{
        formatter: function(p) {{
          if (!p.value) return "";
          var lines = ["<b>" + p.seriesName + "</b>"];
          countries.forEach(function(c, i) {{
            lines.push((countryLabels[c] || c) + ": " + distVals[i].toFixed(2) + " (distance)");
          }});
          return lines.join("<br>");
        }}
      }},
      radar: {{
        indicator: indicators,
        shape: "circle",
        axisName: {{color: txtS, fontSize: 10}},
        splitArea: {{areaStyle: {{color: ["rgba(88,166,255,0.02)", "rgba(88,166,255,0.05)"]}}}},
        splitLine: {{lineStyle: {{color: gridC}}}},
        axisLine: {{lineStyle: {{color: gridC}}}}
      }},
      series: [{{
        type: "radar",
        data: [{{
          value: simVals,
          name: "Claude Similarity",
          areaStyle: {{color: "rgba(63,185,80,0.15)"}},
          lineStyle: {{color: OI[2], width: 2}},
          itemStyle: {{color: OI[2]}}
        }}]
      }}]
    }});
    window.addEventListener("resize", function() {{ ch.resize(); }});
  }})();

  // ── 10. Tradition Engagement Bar ────────────────────────────────────────
  (function() {{
    var ch = initChart("chartEngage");
    if (!ch) return;
    var labels = ENGAGEMENT.map(function(d) {{ return d.tradition; }});
    var depths = ENGAGEMENT.map(function(d) {{ return d.depth_score; }});
    ch.setOption({{
      tooltip: {{
        trigger: "axis", axisPointer: {{type: "shadow"}},
        formatter: function(params) {{
          var p = params[0];
          var e = ENGAGEMENT[p.dataIndex];
          return "<b>" + e.tradition + "</b><br>"
            + "Benchmark: " + e.benchmark + "<br>"
            + "Items: " + e.items + "<br>"
            + "Depth: " + e.depth_score + "/4";
        }}
      }},
      grid: {{left: 10, right: 30, top: 20, bottom: 30, containLabel: true}},
      xAxis: {{
        type: "category", data: labels,
        axisLabel: {{color: txtS, fontSize: 11}},
        axisLine: {{lineStyle: {{color: gridC}}}}
      }},
      yAxis: {{
        type: "value", max: 5,
        axisLabel: {{color: txtS}},
        splitLine: {{lineStyle: {{color: gridC, type: "dashed"}}}}
      }},
      series: [{{
        type: "bar", data: depths,
        itemStyle: {{
          color: function(p) {{ return OI[p.dataIndex % OI.length]; }},
          borderRadius: [4, 4, 0, 0]
        }},
        barMaxWidth: 50,
        label: {{
          show: true, position: "top", color: txtC, fontSize: 13, fontWeight: 600,
          formatter: "{{c}}/4"
        }}
      }}]
    }});
    window.addEventListener("resize", function() {{ ch.resize(); }});
  }})();

  // ═══════════════════════════════════════════════════════════════════════
  // MODEL COMPARISON CHARTS
  // ═══════════════════════════════════════════════════════════════════════
  if (typeof MULTIMODEL_AVAILABLE !== "undefined" && MULTIMODEL_AVAILABLE) {{

    var MC = typeof MODEL_COLORS !== "undefined" ? MODEL_COLORS : {{}};
    var opusC = MC.opus || "#0072B2";
    var sonnetC = MC.sonnet || "#009E73";
    var haikuC = MC.haiku || "#E69F00";

    // KPI: Pearson r
    if (typeof MULTIMODEL_AGREEMENT !== "undefined") {{
      var osR = (MULTIMODEL_AGREEMENT.opus_vs_sonnet || {{}}).overall || {{}};
      var el = document.getElementById("kpiR");
      if (el && osR.pearson_r != null) el.textContent = osR.pearson_r.toFixed(3);
    }}
    // KPI: MFQ ratio range
    if (typeof MULTIMODEL_RATIOS !== "undefined") {{
      var rats = Object.values(MULTIMODEL_RATIOS).filter(function(v) {{ return v != null; }});
      var el2 = document.getElementById("kpiRatio");
      if (el2 && rats.length > 0) {{
        el2.textContent = Math.min.apply(null, rats).toFixed(1) + "-" + Math.max.apply(null, rats).toFixed(1);
      }}
    }}

    // ── 11. MFQ 3-Model Comparison ──────────────────────────────────
    (function() {{
      var ch = initChart("chartMFQCompare");
      if (!ch || typeof MULTIMODEL_MFQ === "undefined") return;
      var foundations = ["Care_Harm", "Fairness_Cheating", "Loyalty_Betrayal", "Authority_Subversion", "Sanctity_Degradation"];
      var fLabels = ["Care", "Fairness", "Loyalty", "Authority", "Sanctity"];
      var fs = MULTIMODEL_MFQ.foundation_scores || {{}};
      function getVals(model) {{
        var m = fs[model] || {{}};
        return foundations.map(function(f) {{ return m[f] || 0; }});
      }}
      var usLib = [3.8, 3.8, 2.3, 2.1, 1.3];
      var usCon = [3.1, 3.0, 3.2, 3.3, 2.9];
      ch.setOption({{
        tooltip: {{trigger: "axis", axisPointer: {{type: "shadow"}}}},
        legend: {{
          data: ["Opus", "Sonnet", "Haiku", "US Liberal", "US Conservative"],
          bottom: 5, textStyle: {{color: txtS, fontSize: 10}},
          itemWidth: 12, itemHeight: 12
        }},
        grid: {{left: 10, right: 20, top: 20, bottom: 55, containLabel: true}},
        xAxis: {{
          type: "category", data: fLabels,
          axisLabel: {{color: txtS, fontSize: 11}},
          axisLine: {{lineStyle: {{color: gridC}}}}
        }},
        yAxis: {{
          type: "value", max: 5.5,
          axisLabel: {{color: txtS}},
          splitLine: {{lineStyle: {{color: gridC, type: "dashed"}}}}
        }},
        series: [
          {{name: "Opus", type: "bar", data: getVals("opus"), itemStyle: {{color: opusC, borderRadius: [3,3,0,0]}}, barGap: "10%"}},
          {{name: "Sonnet", type: "bar", data: getVals("sonnet"), itemStyle: {{color: sonnetC, borderRadius: [3,3,0,0]}}}},
          {{name: "Haiku", type: "bar", data: getVals("haiku"), itemStyle: {{color: haikuC, borderRadius: [3,3,0,0]}}}},
          {{name: "US Liberal", type: "line", data: usLib, lineStyle: {{color: "#8b949e", type: "dashed"}}, symbol: "diamond", symbolSize: 6, itemStyle: {{color: "#8b949e"}}}},
          {{name: "US Conservative", type: "line", data: usCon, lineStyle: {{color: "#484f58", type: "dashed"}}, symbol: "triangle", symbolSize: 6, itemStyle: {{color: "#484f58"}}}}
        ]
      }});
      window.addEventListener("resize", function() {{ ch.resize(); }});
    }})();

    // ── 12. Cultural Alignment Radar 3-Model ─────────────────────────
    (function() {{
      var ch = initChart("chartAlignCompare");
      if (!ch || typeof MULTIMODEL_ALIGNMENT === "undefined") return;
      var countries = ["US", "Germany", "Japan", "Brazil", "India", "China", "Nigeria", "Saudi_Arabia"];
      var cLabels = {{US: "United States", Germany: "Germany", Japan: "Japan", Brazil: "Brazil", India: "India", China: "China", Nigeria: "Nigeria", Saudi_Arabia: "Saudi Arabia"}};
      var maxD = 0;
      countries.forEach(function(c) {{
        var cd = MULTIMODEL_ALIGNMENT[c] || {{}};
        ["opus","sonnet","haiku"].forEach(function(m) {{
          if (cd[m] != null && cd[m] > maxD) maxD = cd[m];
        }});
      }});
      if (maxD === 0) maxD = 2;
      var indicators = countries.map(function(c) {{
        return {{name: cLabels[c] || c, max: Math.ceil(maxD * 1.2 * 10) / 10}};
      }});
      function getDistVals(model) {{
        return countries.map(function(c) {{
          var cd = MULTIMODEL_ALIGNMENT[c] || {{}};
          return cd[model] != null ? Math.round(cd[model] * 1000) / 1000 : 0;
        }});
      }}
      ch.setOption({{
        tooltip: {{}},
        legend: {{
          data: ["Opus", "Sonnet", "Haiku"], bottom: 10,
          textStyle: {{color: txtS, fontSize: 11}}, itemWidth: 12, itemHeight: 12
        }},
        radar: {{
          indicator: indicators, shape: "circle",
          axisName: {{color: txtS, fontSize: 10}},
          splitArea: {{areaStyle: {{color: ["rgba(88,166,255,0.02)", "rgba(88,166,255,0.05)"]}}}},
          splitLine: {{lineStyle: {{color: gridC}}}},
          axisLine: {{lineStyle: {{color: gridC}}}}
        }},
        series: [{{
          type: "radar",
          data: [
            {{value: getDistVals("opus"), name: "Opus", lineStyle: {{color: opusC, width: 2}}, itemStyle: {{color: opusC}}, areaStyle: {{color: "rgba(0,114,178,0.08)"}}}},
            {{value: getDistVals("sonnet"), name: "Sonnet", lineStyle: {{color: sonnetC, width: 2}}, itemStyle: {{color: sonnetC}}, areaStyle: {{color: "rgba(0,158,115,0.08)"}}}},
            {{value: getDistVals("haiku"), name: "Haiku", lineStyle: {{color: haikuC, width: 2}}, itemStyle: {{color: haikuC}}, areaStyle: {{color: "rgba(230,159,0,0.08)"}}}}
          ]
        }}]
      }});
      window.addEventListener("resize", function() {{ ch.resize(); }});
    }})();

    // ── 13. Agreement Heatmap ─────────────────────────────────────────
    (function() {{
      var ch = initChart("chartAgreement");
      if (!ch || typeof MULTIMODEL_AGREEMENT === "undefined") return;
      var pairs = ["opus_vs_sonnet", "opus_vs_haiku", "sonnet_vs_haiku"];
      var pairLabels = ["Opus-Sonnet", "Opus-Haiku", "Sonnet-Haiku"];
      var trials = ["CC1", "CC2", "CC3", "CC4", "CC5"];
      var data = [];
      var minV = 1, maxV = 0;
      pairs.forEach(function(pk, pi) {{
        var pt = (MULTIMODEL_AGREEMENT[pk] || {{}}).per_trial || {{}};
        trials.forEach(function(tid, ti) {{
          var r = (pt[tid] || {{}}).pearson_r;
          if (r != null) {{
            data.push([ti, pi, r]);
            if (r < minV) minV = r;
            if (r > maxV) maxV = r;
          }}
        }});
      }});
      ch.setOption({{
        tooltip: {{
          formatter: function(p) {{
            return pairLabels[p.value[1]] + " / " + trials[p.value[0]] + ": r=" + (p.value[2] != null ? p.value[2].toFixed(3) : "N/A");
          }}
        }},
        grid: {{left: 100, right: 40, top: 20, bottom: 40}},
        xAxis: {{type: "category", data: trials, axisLabel: {{color: txtS}}, axisLine: {{lineStyle: {{color: gridC}}}}}},
        yAxis: {{type: "category", data: pairLabels, axisLabel: {{color: txtS, fontSize: 11}}, axisLine: {{lineStyle: {{color: gridC}}}}}},
        visualMap: {{
          min: Math.floor(minV * 10) / 10, max: 1,
          calculable: true, orient: "horizontal", left: "center", bottom: 0,
          inRange: {{color: ["#f85149", "#f0883e", "#3fb950"]}},
          textStyle: {{color: txtS}}
        }},
        series: [{{
          type: "heatmap", data: data,
          label: {{show: true, color: txtC, fontSize: 11, formatter: function(p) {{ return p.value[2] != null ? p.value[2].toFixed(2) : ""; }}}},
          itemStyle: {{borderWidth: 2, borderColor: "#0d1117"}}
        }}]
      }});
      window.addEventListener("resize", function() {{ ch.resize(); }});
    }})();

    // ── 14. Engagement Depth Grouped Bar ─────────────────────────────
    (function() {{
      var ch = initChart("chartEngageCompare");
      if (!ch || typeof MULTIMODEL_ENGAGEMENT === "undefined") return;
      var traditions = ["Islamic", "Confucian", "Ubuntu", "Buddhist", "Dharmic"];
      function getDepths(model) {{
        var ed = MULTIMODEL_ENGAGEMENT[model] || {{}};
        return traditions.map(function(t) {{ return ed[t] || 0; }});
      }}
      ch.setOption({{
        tooltip: {{trigger: "axis", axisPointer: {{type: "shadow"}}}},
        legend: {{
          data: ["Opus", "Sonnet", "Haiku"], bottom: 5,
          textStyle: {{color: txtS, fontSize: 10}}, itemWidth: 12, itemHeight: 12
        }},
        grid: {{left: 10, right: 20, top: 20, bottom: 50, containLabel: true}},
        xAxis: {{
          type: "category", data: traditions,
          axisLabel: {{color: txtS, fontSize: 11}},
          axisLine: {{lineStyle: {{color: gridC}}}}
        }},
        yAxis: {{
          type: "value", max: 5,
          axisLabel: {{color: txtS}},
          splitLine: {{lineStyle: {{color: gridC, type: "dashed"}}}}
        }},
        series: [
          {{name: "Opus", type: "bar", data: getDepths("opus"), itemStyle: {{color: opusC, borderRadius: [3,3,0,0]}}, barGap: "15%"}},
          {{name: "Sonnet", type: "bar", data: getDepths("sonnet"), itemStyle: {{color: sonnetC, borderRadius: [3,3,0,0]}}}},
          {{name: "Haiku", type: "bar", data: getDepths("haiku"), itemStyle: {{color: haikuC, borderRadius: [3,3,0,0]}}}}
        ]
      }});
      window.addEventListener("resize", function() {{ ch.resize(); }});
    }})();

    // ── 15. RLHF Conflict Comparison ─────────────────────────────────
    (function() {{
      var ch = initChart("chartRLHFCompare");
      if (!ch || typeof MULTIMODEL_RLHF === "undefined") return;
      var models = ["opus", "sonnet", "haiku"];
      var mLabels = ["Opus", "Sonnet", "Haiku"];
      var totals = models.map(function(m) {{
        return (MULTIMODEL_RLHF[m] || {{}}).total || 0;
      }});
      ch.setOption({{
        tooltip: {{trigger: "axis", axisPointer: {{type: "shadow"}}}},
        grid: {{left: 10, right: 40, top: 20, bottom: 30, containLabel: true}},
        xAxis: {{
          type: "category", data: mLabels,
          axisLabel: {{color: txtS, fontSize: 12}},
          axisLine: {{lineStyle: {{color: gridC}}}}
        }},
        yAxis: {{
          type: "value",
          axisLabel: {{color: txtS}},
          splitLine: {{lineStyle: {{color: gridC, type: "dashed"}}}}
        }},
        series: [{{
          type: "bar", data: [
            {{value: totals[0], itemStyle: {{color: opusC}}}},
            {{value: totals[1], itemStyle: {{color: sonnetC}}}},
            {{value: totals[2], itemStyle: {{color: haikuC}}}}
          ],
          barMaxWidth: 60,
          itemStyle: {{borderRadius: [4, 4, 0, 0]}},
          label: {{show: true, position: "top", color: txtC, fontSize: 13, fontWeight: 600}}
        }}]
      }});
      window.addEventListener("resize", function() {{ ch.resize(); }});
    }})();

    // ── 16. Divergence Table ─────────────────────────────────────────
    (function() {{
      if (typeof MULTIMODEL_DIVERGENCE === "undefined") return;
      var box = document.getElementById("divTableBox");
      if (!box) return;
      var tbl = document.createElement("table");
      tbl.className = "dt";
      var thead = document.createElement("thead");
      var hr = document.createElement("tr");
      ["Trial","#","Question","Var","Opus","Sonnet","Haiku"].forEach(function(h) {{
        var th = document.createElement("th");
        th.textContent = h;
        hr.appendChild(th);
      }});
      thead.appendChild(hr);
      tbl.appendChild(thead);
      var tbody = document.createElement("tbody");
      MULTIMODEL_DIVERGENCE.slice(0, 10).forEach(function(d) {{
        var mr = d.model_responses || {{}};
        var tr = document.createElement("tr");
        [d.trial_id, d.item_id, (d.question || "").substring(0, 50) + "...",
         d.variance != null ? d.variance.toFixed(2) : "",
         mr.opus != null ? mr.opus : "-",
         mr.sonnet != null ? mr.sonnet : "-",
         mr.haiku != null ? mr.haiku : "-"
        ].forEach(function(v) {{
          var td = document.createElement("td");
          td.textContent = v;
          tr.appendChild(td);
        }});
        tbody.appendChild(tr);
      }});
      tbl.appendChild(tbody);
      box.appendChild(tbl);
    }})();

  }}  // end MULTIMODEL_AVAILABLE

  // ── Tab switch: resize all ECharts instances when tab becomes visible ──
  document.querySelectorAll('[data-bs-toggle="pill"]').forEach(function(tab) {{
    tab.addEventListener("shown.bs.tab", function() {{
      // Resize all ECharts instances in the newly visible pane
      setTimeout(function() {{
        document.querySelectorAll(".chart-box, .chart-box-sm").forEach(function(el) {{
          var inst = echarts.getInstanceByDom(el);
          if (inst) inst.resize();
        }});
      }}, 100);
    }});
  }});

}})();
</script>
</body>
</html>"""

with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(html)

html_size = OUT_HTML.stat().st_size
print(f"Wrote {OUT_HTML} ({html_size / 1024:.1f} KB)")
print(f"\nSummary:")
print(f"  benchmark-data.js: {js_size:,} bytes ({js_size / 1024:.1f} KB)")
print(f"  benchmarks.html:   {html_size:,} bytes ({html_size / 1024:.1f} KB)")
print(f"  Rankings:          {len(BENCHMARK_RANKINGS)} entries")
print(f"  Trials:            {len(TRIAL_SUMMARY)} trials")
print(f"  MFQ Profile:       {json.dumps(MFQ_PROFILE)}")
print(f"  Cultural Alignment: {len(CULTURAL_ALIGNMENT['distances'])} countries")
print(f"  RLHF Conflicts:   {len(RLHF_CONFLICTS)} categories")
print(f"  Tradition Engagement: {len(TRADITION_ENGAGEMENT)} traditions")
