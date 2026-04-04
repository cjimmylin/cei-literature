"""Generate a self-contained HTML dashboard for the Religious Values Benchmark paper.

Architecture: "fat data, thin client" -- Python pre-computes ALL analytics and
embeds them as JS constants. The browser does zero computation.

IMPORTANT: Since HTML is emitted via Python f-strings, ALL JavaScript curly
braces are DOUBLED ({{ }}).  Data constants use json.dumps (single braces).
"""
from __future__ import annotations

import json
import math
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE = Path(__file__).resolve().parent.parent   # RELIGIOUS-VALUES/
DATA = BASE / "data"
OUT  = BASE / "dashboard" / "20260404-religious-values-dashboard-v2.html"
OUT.parent.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Load all data files
# ---------------------------------------------------------------------------
sensitivity   = json.loads((DATA / "20260404-sensitivity-analysis.json").read_text())
correlation   = json.loads((DATA / "20260404-correlation-matrix.json").read_text())
claims_data   = json.loads((DATA / "20260404-claim-robustness-tests.json").read_text())
void_factors  = json.loads((DATA / "20260404-void-factor-taxonomy.json").read_text())
batch1        = json.loads((DATA / "20260404-claude-assessment-batch1.json").read_text())
batch2        = json.loads((DATA / "20260404-claude-assessment-batch2.json").read_text())
feature_mat   = json.loads((DATA / "20260404-religious-benchmark-feature-matrix-v2.json").read_text())

# ---------------------------------------------------------------------------
# Pre-compute analytics
# ---------------------------------------------------------------------------

# -- Overview stats --
total_candidates = feature_mat["total_entries"]
gate_passers = feature_mat["gate_passing"]
gp_entries = [e for e in feature_mat["entries"] if e.get("passes_gates")]

# Tradition counts among gate-passers
tradition_counts: dict[str, int] = {}
family_counts: dict[str, int] = {}
for e in gp_entries:
    trad = e.get("D5_primary_tradition", "Unknown")
    fam  = e.get("D6_tradition_family", "Other")
    tradition_counts[trad] = tradition_counts.get(trad, 0) + 1
    family_counts[fam] = family_counts.get(fam, 0) + 1

n_traditions = len(void_factors["traditions"])
n_void = sum(1 for t in void_factors["traditions"] if not t["has_benchmarks"])

# -- Bootstrap CI data for chart --
boot_cis = sorted(sensitivity["bootstrap"]["benchmark_cis"],
                  key=lambda x: x["composite_mean"], reverse=True)
boot_labels = [c["short_title"][:45] for c in boot_cis]
boot_means  = [c["composite_mean"] for c in boot_cis]
boot_lowers = [c["composite_ci_lower"] for c in boot_cis]
boot_uppers = [c["composite_ci_upper"] for c in boot_cis]

# Tradition family for each gate-passer (for coloring)
id_to_family = {e["id"]: e.get("D6_tradition_family", "Other") for e in gp_entries}
boot_families = [id_to_family.get(c["id"], "Other") for c in boot_cis]

# Top-15 cutoff
top15_cutoff = boot_means[14] if len(boot_means) >= 15 else 0

# -- Weight sensitivity heatmap --
ws = sensitivity["weight_sensitivity"]
benchmark_robustness = ws["benchmark_robustness"]
rob_labels = [b["short_title"][:40] for b in benchmark_robustness[:20]]
rob_pct_top15 = [b["pct_in_top15"] * 100 for b in benchmark_robustness[:20]]
rob_rank_range = [b["rank_range"] for b in benchmark_robustness[:20]]

# -- Gate threshold --
gt_results = sensitivity["gate_threshold"]["results"]
gt_thresholds = [r["threshold"] for r in gt_results]
gt_passers = [r["gate_passers"] for r in gt_results]
gt_traditions = [r["traditions_represented"] for r in gt_results]
gt_void_gained = {r["threshold"]: r.get("void_traditions_gained", []) for r in gt_results}

# -- Void factor radar data --
void_traditions = void_factors["traditions"]
exemplar_names = ["Islam", "Judaism", "Indigenous Spirituality"]
factor_keys = ["digital_corpus", "nlp_community", "formalizability",
               "data_sovereignty", "institutional_support", "publication_infrastructure"]
factor_labels = ["Digital Corpus", "NLP Community", "Formalizability",
                 "Data Sovereignty", "Institutional Support", "Publication Infra."]

radar_data: dict[str, list[int]] = {}
for name in exemplar_names:
    for t in void_traditions:
        if t["tradition"] == name:
            radar_data[name] = [t[f] for f in factor_keys]
            break

# Structural scores table
struct_table = []
for t in sorted(void_traditions, key=lambda x: x["benchmark_readiness_index"], reverse=True):
    struct_table.append({
        "tradition": t["tradition"],
        "family": t["family"],
        "has_bm": t["has_benchmarks"],
        "gp_count": t["gate_passers_count"],
        "readiness": t["benchmark_readiness_index"],
        "total": t["total_structural_score"],
        "digital": t["digital_corpus"],
        "nlp": t["nlp_community"],
        "formal": t["formalizability"],
    })

# Readiness bar chart
readiness_labels = [t["tradition"] for t in struct_table]
readiness_vals   = [t["readiness"] for t in struct_table]
readiness_colors = ["#54A24B" if t["has_bm"] else "#E45756" for t in struct_table]

# -- A3 Values Relevance --
a3_scores: list[int] = []
a3_benchmarks: list[dict] = []
for a in batch1["assessments"]:
    v = a.get("features", {}).get("A3_values_relevance")
    if v is not None:
        a3_scores.append(v)
        a3_benchmarks.append({"name": a["short_title"][:45], "score": v,
                              "tradition": a.get("primary_tradition", "?")})
for a in batch2["assessments"]:
    v = a.get("features", {}).get("A3_values_alignment_relevance")
    if v is not None:
        a3_scores.append(v)
        a3_benchmarks.append({"name": a["short_title"][:45], "score": v,
                              "tradition": a.get("primary_tradition", "?")})

a3_mean = sum(a3_scores) / len(a3_scores) if a3_scores else 0
a3_benchmarks_sorted = sorted(a3_benchmarks, key=lambda x: x["score"], reverse=True)

# A1 construct breakdown
a1_counts: dict[str, int] = {}
for a in batch1["assessments"]:
    c = a.get("features", {}).get("A1_primary_construct", "unknown")
    a1_counts[c] = a1_counts.get(c, 0) + 1
for a in batch2["assessments"]:
    c = a.get("features", {}).get("A1_primary_construct", "unknown")
    a1_counts[c] = a1_counts.get(c, 0) + 1

# -- Claim robustness --
claim_chart: list[dict] = []
for c in claims_data["claims"]:
    num = c["claim_number"]
    text = c["claim_text"]
    if "tests" in c and isinstance(c["tests"], list):
        pv = c["tests"][0].get("p_value", 1.0)
    elif "p_value" in c:
        pv = c["p_value"]
    else:
        pv = 1.0
    if pv == 0.0:
        pv = 1e-15
    claim_chart.append({
        "claim": f"C{num}",
        "text": text,
        "p_value": pv,
        "neg_log_p": -math.log10(pv),
        "significant": pv < 0.05,
        "marginal": 0.05 <= pv < 0.10,
        "interpretation": c.get("interpretation", ""),
    })

# -- Correlation heatmap data --
corr_features = correlation["spearman_correlations"]["features"]
corr_matrix   = correlation["spearman_correlations"]["matrix"]

# ---------------------------------------------------------------------------
# Embed data as JSON
# ---------------------------------------------------------------------------
js_data = f"""
// === Pre-computed data constants ===
const OVERVIEW = {json.dumps({
    "total_candidates": total_candidates,
    "gate_passers": gate_passers,
    "n_traditions": n_traditions,
    "n_void": n_void,
    "tradition_counts": tradition_counts,
    "family_counts": family_counts,
})};

const BOOT_CI = {json.dumps({
    "labels": boot_labels,
    "means": boot_means,
    "lowers": boot_lowers,
    "uppers": boot_uppers,
    "families": boot_families,
    "top15_cutoff": top15_cutoff,
})};

const WEIGHT_SENSITIVITY = {json.dumps({
    "labels": rob_labels,
    "pct_top15": rob_pct_top15,
    "rank_range": rob_rank_range,
})};

const GATE_THRESHOLD = {json.dumps({
    "thresholds": gt_thresholds,
    "passers": gt_passers,
    "traditions": gt_traditions,
    "void_gained": gt_void_gained,
})};

const RADAR = {json.dumps({
    "factors": factor_labels,
    "series": radar_data,
})};

const STRUCT_TABLE = {json.dumps(struct_table)};

const READINESS = {json.dumps({
    "labels": readiness_labels,
    "values": readiness_vals,
    "colors": readiness_colors,
})};

const A3_DATA = {json.dumps({
    "scores": a3_scores,
    "mean": round(a3_mean, 1),
    "benchmarks": a3_benchmarks_sorted,
})};

const A1_COUNTS = {json.dumps(a1_counts)};

const CLAIMS = {json.dumps(claim_chart)};

const CORR = {json.dumps({
    "features": corr_features,
    "matrix": corr_matrix,
})};
"""

# ---------------------------------------------------------------------------
# HTML template
# ---------------------------------------------------------------------------
FAMILY_COLOR_JS = """{
    "Abrahamic": "#4C78A8",
    "Dharmic": "#54A24B",
    "East Asian": "#E45756",
    "African/Indigenous": "#9D9D9D",
    "Other": "#9D9D9D"
}"""

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Religious Values Benchmark Meta-Evaluation Dashboard</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/echarts@5.5.0/dist/echarts.min.js"></script>
<style>
:root {{
    --bg-primary: #0d1117;
    --bg-secondary: #161b22;
    --bg-card: #1c2128;
    --text-primary: #e6edf3;
    --text-secondary: #8b949e;
    --accent-blue: #4C78A8;
    --accent-green: #54A24B;
    --accent-red: #E45756;
    --accent-orange: #F58518;
    --border: #30363d;
}}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
    font-family: 'Inter', sans-serif;
    background: var(--bg-primary);
    color: var(--text-primary);
    min-height: 100vh;
}}
.header {{
    background: var(--bg-secondary);
    border-bottom: 1px solid var(--border);
    padding: 16px 24px;
}}
.header h1 {{
    font-size: 1.4rem;
    font-weight: 700;
    margin: 0;
}}
.header .subtitle {{
    font-size: 0.85rem;
    color: var(--text-secondary);
    margin-top: 2px;
}}
.nav-tabs {{
    border-bottom: 1px solid var(--border);
    background: var(--bg-secondary);
    padding: 0 24px;
}}
.nav-tabs .nav-link {{
    color: var(--text-secondary);
    border: none;
    padding: 10px 18px;
    font-size: 0.9rem;
    font-weight: 500;
    border-bottom: 2px solid transparent;
    transition: all 0.2s;
}}
.nav-tabs .nav-link:hover {{
    color: var(--text-primary);
    border-bottom-color: var(--accent-blue);
}}
.nav-tabs .nav-link.active {{
    color: var(--accent-blue);
    background: transparent;
    border-bottom: 2px solid var(--accent-blue);
}}
.tab-content {{
    padding: 20px 24px;
}}
.card-stat {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 20px;
    text-align: center;
}}
.card-stat .number {{
    font-size: 2.2rem;
    font-weight: 700;
    color: var(--accent-blue);
}}
.card-stat .label {{
    font-size: 0.85rem;
    color: var(--text-secondary);
    margin-top: 4px;
}}
.chart-container {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 16px;
    margin-bottom: 20px;
}}
.chart-title {{
    font-size: 1rem;
    font-weight: 600;
    margin-bottom: 12px;
    color: var(--text-primary);
}}
table.dark-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 0.85rem;
}}
table.dark-table th {{
    background: var(--bg-secondary);
    color: var(--text-secondary);
    padding: 8px 10px;
    text-align: left;
    font-weight: 600;
    border-bottom: 1px solid var(--border);
}}
table.dark-table td {{
    padding: 7px 10px;
    border-bottom: 1px solid var(--border);
    color: var(--text-primary);
}}
table.dark-table tr:hover td {{
    background: rgba(76, 120, 168, 0.08);
}}
.badge-void {{
    background: var(--accent-red);
    color: white;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: 600;
}}
.badge-active {{
    background: var(--accent-green);
    color: white;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: 600;
}}
.claim-card {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 14px 16px;
    margin-bottom: 10px;
}}
.claim-card .claim-num {{
    font-weight: 700;
    color: var(--accent-blue);
}}
.claim-card .claim-text {{
    color: var(--text-primary);
    font-size: 0.9rem;
}}
.claim-card .claim-pval {{
    font-size: 0.8rem;
    margin-top: 4px;
}}
.claim-card .claim-interp {{
    font-size: 0.8rem;
    color: var(--text-secondary);
    margin-top: 6px;
}}
</style>
</head>
<body>

<div class="header">
    <h1>Religious Values Benchmark Meta-Evaluation</h1>
    <div class="subtitle">What Do Religious AI Benchmarks Actually Measure?  |  Dashboard v2  |  2026-04-04</div>
</div>

<ul class="nav nav-tabs" id="mainTabs" role="tablist">
    <li class="nav-item"><a class="nav-link active" data-bs-toggle="tab" href="#tab-overview">Overview</a></li>
    <li class="nav-item"><a class="nav-link" data-bs-toggle="tab" href="#tab-sensitivity">Sensitivity</a></li>
    <li class="nav-item"><a class="nav-link" data-bs-toggle="tab" href="#tab-void">Tradition Void</a></li>
    <li class="nav-item"><a class="nav-link" data-bs-toggle="tab" href="#tab-values">Values Relevance</a></li>
    <li class="nav-item"><a class="nav-link" data-bs-toggle="tab" href="#tab-claims">Claim Evidence</a></li>
</ul>

<div class="tab-content">

<!-- ============ TAB 1: OVERVIEW ============ -->
<div class="tab-pane fade show active" id="tab-overview">
    <div class="row g-3 mb-4">
        <div class="col-md-3">
            <div class="card-stat">
                <div class="number">{total_candidates}</div>
                <div class="label">Total Candidates Screened</div>
            </div>
        </div>
        <div class="col-md-3">
            <div class="card-stat">
                <div class="number" style="color:var(--accent-green)">{gate_passers}</div>
                <div class="label">Gate-Passers (RD &ge; 30)</div>
            </div>
        </div>
        <div class="col-md-3">
            <div class="card-stat">
                <div class="number">{n_traditions}</div>
                <div class="label">Religious Traditions Analyzed</div>
            </div>
        </div>
        <div class="col-md-3">
            <div class="card-stat">
                <div class="number" style="color:var(--accent-red)">{n_void}</div>
                <div class="label">Void Traditions (0 Gate-Passers)</div>
            </div>
        </div>
    </div>
    <div class="row g-3">
        <div class="col-md-6">
            <div class="chart-container">
                <div class="chart-title">Gate-Passers by Tradition</div>
                <div id="chart-tradition-bar" style="height:350px"></div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="chart-container">
                <div class="chart-title">Gate-Passers by Tradition Family</div>
                <div id="chart-family-pie" style="height:350px"></div>
            </div>
        </div>
    </div>
</div>

<!-- ============ TAB 2: SENSITIVITY ============ -->
<div class="tab-pane fade" id="tab-sensitivity">
    <div class="row g-3 mb-4">
        <div class="col-12">
            <div class="chart-container">
                <div class="chart-title">Bootstrap 95% CI for Composite Scores (n=10,000)</div>
                <div id="chart-boot-ci" style="height:900px"></div>
            </div>
        </div>
    </div>
    <div class="row g-3 mb-4">
        <div class="col-md-6">
            <div class="chart-container">
                <div class="chart-title">Weight Sensitivity: Top-15 Stability (%)</div>
                <div id="chart-weight-sens" style="height:450px"></div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="chart-container">
                <div class="chart-title">Gate Threshold vs Coverage</div>
                <div id="chart-gate-threshold" style="height:450px"></div>
            </div>
        </div>
    </div>
</div>

<!-- ============ TAB 3: TRADITION VOID ============ -->
<div class="tab-pane fade" id="tab-void">
    <div class="row g-3 mb-4">
        <div class="col-md-6">
            <div class="chart-container">
                <div class="chart-title">Void Factor Profiles: Three Tradition Archetypes</div>
                <div id="chart-radar" style="height:450px"></div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="chart-container">
                <div class="chart-title">Benchmark Readiness Index by Tradition</div>
                <div id="chart-readiness" style="height:450px"></div>
            </div>
        </div>
    </div>
    <div class="chart-container">
        <div class="chart-title">Structural Scores by Tradition</div>
        <table class="dark-table">
            <thead>
                <tr>
                    <th>Tradition</th><th>Family</th><th>Status</th><th>Gate-Passers</th>
                    <th>Digital</th><th>NLP</th><th>Formalizability</th>
                    <th>Readiness</th><th>Total</th>
                </tr>
            </thead>
            <tbody id="struct-table-body"></tbody>
        </table>
    </div>
</div>

<!-- ============ TAB 4: VALUES RELEVANCE ============ -->
<div class="tab-pane fade" id="tab-values">
    <div class="row g-3 mb-4">
        <div class="col-md-6">
            <div class="chart-container">
                <div class="chart-title">A3 Values Alignment Relevance Distribution</div>
                <div id="chart-a3-hist" style="height:380px"></div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="chart-container">
                <div class="chart-title">Construct Type Breakdown (A1)</div>
                <div id="chart-a1-pie" style="height:380px"></div>
            </div>
        </div>
    </div>
    <div class="row g-3">
        <div class="col-md-6">
            <div class="chart-container">
                <div class="chart-title">Top A3 Benchmarks (Values-Aligned)</div>
                <table class="dark-table">
                    <thead><tr><th>Benchmark</th><th>Tradition</th><th>A3 Score</th></tr></thead>
                    <tbody id="a3-top-table"></tbody>
                </table>
            </div>
        </div>
        <div class="col-md-6">
            <div class="chart-container">
                <div class="chart-title">Bottom A3 Benchmarks (Knowledge-Oriented)</div>
                <table class="dark-table">
                    <thead><tr><th>Benchmark</th><th>Tradition</th><th>A3 Score</th></tr></thead>
                    <tbody id="a3-bottom-table"></tbody>
                </table>
            </div>
        </div>
    </div>
</div>

<!-- ============ TAB 5: CLAIM EVIDENCE ============ -->
<div class="tab-pane fade" id="tab-claims">
    <div class="row g-3 mb-4">
        <div class="col-12">
            <div class="chart-container">
                <div class="chart-title">Statistical Support for Paper Claims</div>
                <div id="chart-claims" style="height:350px"></div>
            </div>
        </div>
    </div>
    <div id="claim-cards"></div>
</div>

</div><!-- /tab-content -->

<script>
{js_data}

const FAMILY_COLORS = {FAMILY_COLOR_JS};

function familyColor(f) {{
    return FAMILY_COLORS[f] || "#9D9D9D";
}}

// ===== TAB 1: Overview Charts =====
function renderOverview() {{
    // Tradition bar
    var trads = Object.entries(OVERVIEW.tradition_counts).sort((a,b) => b[1]-a[1]);
    var tradChart = echarts.init(document.getElementById('chart-tradition-bar'));
    tradChart.setOption({{
        tooltip: {{ trigger: 'axis' }},
        xAxis: {{ type: 'category', data: trads.map(t=>t[0]), axisLabel: {{ rotate: 30, color: '#8b949e' }}, axisLine: {{ lineStyle: {{ color: '#30363d' }} }} }},
        yAxis: {{ type: 'value', axisLabel: {{ color: '#8b949e' }}, splitLine: {{ lineStyle: {{ color: '#21262d' }} }} }},
        series: [{{ type: 'bar', data: trads.map(t => ({{ value: t[1], itemStyle: {{ color: '#4C78A8' }} }})), barMaxWidth: 40 }}],
        grid: {{ left: 50, right: 20, bottom: 60, top: 20 }},
        backgroundColor: 'transparent'
    }});

    // Family pie
    var fams = Object.entries(OVERVIEW.family_counts).map(f => ({{ name: f[0], value: f[1] }}));
    var famChart = echarts.init(document.getElementById('chart-family-pie'));
    famChart.setOption({{
        tooltip: {{ trigger: 'item', formatter: '{{b}}: {{c}} ({{d}}%)' }},
        series: [{{
            type: 'pie', radius: ['35%','65%'],
            data: fams.map(f => ({{ ...f, itemStyle: {{ color: familyColor(f.name) }} }})),
            label: {{ color: '#e6edf3', fontSize: 12 }},
            emphasis: {{ itemStyle: {{ shadowBlur: 10 }} }}
        }}],
        backgroundColor: 'transparent'
    }});
}}

// ===== TAB 2: Sensitivity Charts =====
function renderSensitivity() {{
    // Bootstrap CI forest plot (horizontal)
    var bc = echarts.init(document.getElementById('chart-boot-ci'));
    var n = BOOT_CI.labels.length;
    var errData = [];
    for (var i = 0; i < n; i++) {{
        errData.push([BOOT_CI.lowers[i], n - 1 - i]);
        errData.push([BOOT_CI.uppers[i], n - 1 - i]);
    }}
    bc.setOption({{
        tooltip: {{
            trigger: 'axis',
            axisPointer: {{ type: 'shadow' }},
            formatter: function(p) {{
                var idx = n - 1 - p[0].dataIndex;
                return BOOT_CI.labels[idx] + '<br>Mean: ' + BOOT_CI.means[idx].toFixed(1) +
                    '<br>95% CI: [' + BOOT_CI.lowers[idx].toFixed(1) + ', ' + BOOT_CI.uppers[idx].toFixed(1) + ']';
            }}
        }},
        xAxis: {{
            type: 'value',
            name: 'Composite Score',
            nameLocation: 'middle',
            nameGap: 30,
            axisLabel: {{ color: '#8b949e' }},
            splitLine: {{ lineStyle: {{ color: '#21262d' }} }}
        }},
        yAxis: {{
            type: 'category',
            data: BOOT_CI.labels.slice().reverse(),
            axisLabel: {{ color: '#8b949e', fontSize: 9 }},
            axisLine: {{ lineStyle: {{ color: '#30363d' }} }}
        }},
        series: [
            {{
                type: 'bar',
                data: BOOT_CI.means.slice().reverse().map(function(v, i) {{
                    var origIdx = n - 1 - i;
                    return {{ value: v, itemStyle: {{ color: familyColor(BOOT_CI.families[origIdx]) }} }};
                }}),
                barMaxWidth: 14
            }},
            {{
                type: 'custom',
                renderItem: function(params, api) {{
                    var catIdx = api.value(1);
                    var origIdx = n - 1 - catIdx;
                    var lo = api.coord([BOOT_CI.lowers[origIdx], catIdx]);
                    var hi = api.coord([BOOT_CI.uppers[origIdx], catIdx]);
                    var halfH = 4;
                    return {{
                        type: 'group',
                        children: [
                            {{ type: 'line', shape: {{ x1: lo[0], y1: lo[1], x2: hi[0], y2: hi[1] }}, style: {{ stroke: '#aaa', lineWidth: 1.2 }} }},
                            {{ type: 'line', shape: {{ x1: lo[0], y1: lo[1]-halfH, x2: lo[0], y2: lo[1]+halfH }}, style: {{ stroke: '#aaa', lineWidth: 1.2 }} }},
                            {{ type: 'line', shape: {{ x1: hi[0], y1: hi[1]-halfH, x2: hi[0], y2: hi[1]+halfH }}, style: {{ stroke: '#aaa', lineWidth: 1.2 }} }}
                        ]
                    }};
                }},
                encode: {{ x: 0, y: 1 }},
                data: (function() {{
                    var d = [];
                    for (var i = 0; i < n; i++) {{
                        d.push([BOOT_CI.means[i], n - 1 - i]);
                    }}
                    return d;
                }})(),
                z: 10
            }}
        ],
        markLine: {{ data: [{{ xAxis: BOOT_CI.top15_cutoff }}] }},
        grid: {{ left: 260, right: 30, top: 10, bottom: 40 }},
        backgroundColor: 'transparent'
    }});

    // Top-15 cutoff line
    bc.setOption({{
        series: [{{
            markLine: {{
                silent: true,
                lineStyle: {{ color: '#E45756', type: 'dashed', width: 1.5 }},
                label: {{ formatter: 'Top-15 cutoff', color: '#E45756', fontSize: 10 }},
                data: [{{ xAxis: BOOT_CI.top15_cutoff }}]
            }}
        }}]
    }});

    // Weight sensitivity bar
    var ws = echarts.init(document.getElementById('chart-weight-sens'));
    ws.setOption({{
        tooltip: {{ trigger: 'axis' }},
        xAxis: {{ type: 'value', max: 100, name: '% in Top-15', axisLabel: {{ color: '#8b949e' }}, splitLine: {{ lineStyle: {{ color: '#21262d' }} }} }},
        yAxis: {{ type: 'category', data: WEIGHT_SENSITIVITY.labels.slice().reverse(), axisLabel: {{ color: '#8b949e', fontSize: 9 }}, axisLine: {{ lineStyle: {{ color: '#30363d' }} }} }},
        series: [{{
            type: 'bar', data: WEIGHT_SENSITIVITY.pct_top15.slice().reverse().map(function(v) {{
                var color = v >= 90 ? '#54A24B' : v >= 50 ? '#F58518' : '#E45756';
                return {{ value: v, itemStyle: {{ color: color }} }};
            }}),
            barMaxWidth: 16
        }}],
        grid: {{ left: 240, right: 30, top: 10, bottom: 30 }},
        backgroundColor: 'transparent'
    }});

    // Gate threshold
    var gt = echarts.init(document.getElementById('chart-gate-threshold'));
    gt.setOption({{
        tooltip: {{ trigger: 'axis' }},
        legend: {{ data: ['Gate-Passers', 'Traditions'], textStyle: {{ color: '#8b949e' }}, top: 0 }},
        xAxis: {{ type: 'category', data: GATE_THRESHOLD.thresholds, name: 'RD Threshold', nameLocation: 'middle', nameGap: 30, axisLabel: {{ color: '#8b949e' }}, axisLine: {{ lineStyle: {{ color: '#30363d' }} }} }},
        yAxis: [
            {{ type: 'value', name: 'Gate-Passers', axisLabel: {{ color: '#4C78A8' }}, splitLine: {{ lineStyle: {{ color: '#21262d' }} }} }},
            {{ type: 'value', name: 'Traditions', axisLabel: {{ color: '#E45756' }}, splitLine: {{ show: false }} }}
        ],
        series: [
            {{ name: 'Gate-Passers', type: 'line', data: GATE_THRESHOLD.passers, itemStyle: {{ color: '#4C78A8' }}, lineStyle: {{ width: 2 }}, symbol: 'circle', symbolSize: 8 }},
            {{ name: 'Traditions', type: 'line', yAxisIndex: 1, data: GATE_THRESHOLD.traditions, itemStyle: {{ color: '#E45756' }}, lineStyle: {{ width: 2, type: 'dashed' }}, symbol: 'rect', symbolSize: 8 }}
        ],
        grid: {{ left: 60, right: 60, top: 40, bottom: 40 }},
        backgroundColor: 'transparent'
    }});
    // Add threshold markers
    gt.setOption({{
        series: [{{
            markLine: {{
                silent: true,
                lineStyle: {{ color: '#54A24B', type: 'dotted', width: 2 }},
                label: {{ formatter: 'Current (30)', color: '#54A24B', fontSize: 10 }},
                data: [{{ xAxis: '30' }}]
            }}
        }}, {{
            markLine: {{
                silent: true,
                lineStyle: {{ color: '#F58518', type: 'dotted', width: 2 }},
                label: {{ formatter: 'NormEval (40)', color: '#F58518', fontSize: 10 }},
                data: [{{ xAxis: '40' }}]
            }}
        }}]
    }});
}}

// ===== TAB 3: Tradition Void =====
function renderVoid() {{
    // Radar
    var radarChart = echarts.init(document.getElementById('chart-radar'));
    var indicators = RADAR.factors.map(function(f) {{ return {{ name: f, max: 5 }}; }});
    var radarColors = {{ "Islam": "#4C78A8", "Judaism": "#E45756", "Indigenous Spirituality": "#54A24B" }};
    var seriesData = Object.entries(RADAR.series).map(function(entry) {{
        return {{ value: entry[1], name: entry[0], lineStyle: {{ width: 2 }}, areaStyle: {{ opacity: 0.15 }}, itemStyle: {{ color: radarColors[entry[0]] || '#9D9D9D' }} }};
    }});
    radarChart.setOption({{
        tooltip: {{}},
        legend: {{ data: Object.keys(RADAR.series), textStyle: {{ color: '#8b949e' }}, bottom: 0 }},
        radar: {{ indicator: indicators, shape: 'polygon', axisName: {{ color: '#8b949e', fontSize: 11 }}, splitArea: {{ areaStyle: {{ color: ['#161b22','#1c2128','#161b22','#1c2128','#161b22'] }} }}, splitLine: {{ lineStyle: {{ color: '#30363d' }} }}, axisLine: {{ lineStyle: {{ color: '#30363d' }} }} }},
        series: [{{ type: 'radar', data: seriesData }}],
        backgroundColor: 'transparent'
    }});

    // Readiness bar
    var rb = echarts.init(document.getElementById('chart-readiness'));
    rb.setOption({{
        tooltip: {{ trigger: 'axis' }},
        xAxis: {{ type: 'category', data: READINESS.labels, axisLabel: {{ rotate: 35, color: '#8b949e', fontSize: 9 }}, axisLine: {{ lineStyle: {{ color: '#30363d' }} }} }},
        yAxis: {{ type: 'value', name: 'Readiness Index', max: 15, axisLabel: {{ color: '#8b949e' }}, splitLine: {{ lineStyle: {{ color: '#21262d' }} }} }},
        series: [{{
            type: 'bar',
            data: READINESS.values.map(function(v, i) {{
                return {{ value: v, itemStyle: {{ color: READINESS.colors[i] }} }};
            }}),
            barMaxWidth: 30
        }}],
        grid: {{ left: 50, right: 20, bottom: 80, top: 30 }},
        backgroundColor: 'transparent'
    }});

    // Structural table
    var tbody = document.getElementById('struct-table-body');
    STRUCT_TABLE.forEach(function(t) {{
        var statusBadge = t.has_bm ? '<span class="badge-active">Active</span>' : '<span class="badge-void">Void</span>';
        tbody.innerHTML += '<tr>' +
            '<td>' + t.tradition + '</td>' +
            '<td>' + t.family + '</td>' +
            '<td>' + statusBadge + '</td>' +
            '<td>' + t.gp_count + '</td>' +
            '<td>' + t.digital + '</td>' +
            '<td>' + t.nlp + '</td>' +
            '<td>' + t.formal + '</td>' +
            '<td><strong>' + t.readiness + '</strong></td>' +
            '<td>' + t.total + '</td>' +
            '</tr>';
    }});
}}

// ===== TAB 4: Values Relevance =====
function renderValues() {{
    // A3 histogram
    var a3hist = echarts.init(document.getElementById('chart-a3-hist'));
    // Bin the scores into 10-wide bins
    var bins = [0,10,20,30,40,50,60,70,80,90,100];
    var counts = new Array(bins.length - 1).fill(0);
    A3_DATA.scores.forEach(function(s) {{
        var idx = Math.min(Math.floor(s / 10), counts.length - 1);
        counts[idx]++;
    }});
    var binLabels = [];
    for (var i = 0; i < bins.length - 1; i++) {{
        binLabels.push(bins[i] + '-' + (bins[i+1]-1));
    }}
    a3hist.setOption({{
        tooltip: {{ trigger: 'axis' }},
        xAxis: {{ type: 'category', data: binLabels, name: 'A3 Score Range', nameLocation: 'middle', nameGap: 30, axisLabel: {{ color: '#8b949e' }}, axisLine: {{ lineStyle: {{ color: '#30363d' }} }} }},
        yAxis: {{ type: 'value', name: 'Count', axisLabel: {{ color: '#8b949e' }}, splitLine: {{ lineStyle: {{ color: '#21262d' }} }} }},
        series: [{{
            type: 'bar', data: counts.map(function(v) {{ return {{ value: v, itemStyle: {{ color: '#4C78A8' }} }}; }}), barMaxWidth: 35
        }}],
        grid: {{ left: 50, right: 20, bottom: 50, top: 20 }},
        backgroundColor: 'transparent'
    }});
    // Add mean line and threshold lines
    a3hist.setOption({{
        series: [{{
            markLine: {{
                silent: true,
                data: [
                    {{ xAxis: 4, lineStyle: {{ color: '#E45756', type: 'dashed' }}, label: {{ formatter: 'Minimal (50)', color: '#E45756' }} }},
                    {{ xAxis: 7, lineStyle: {{ color: '#54A24B', type: 'dashed' }}, label: {{ formatter: 'Strong (75)', color: '#54A24B' }} }}
                ]
            }},
            markPoint: {{
                data: [{{ coord: [Math.floor(A3_DATA.mean / 10), 0], value: 'Mean=' + A3_DATA.mean, symbolSize: 0, label: {{ show: true, color: '#F58518', fontSize: 11, position: 'top', offset: [0, -30] }} }}]
            }}
        }}]
    }});

    // A1 pie
    var a1pie = echarts.init(document.getElementById('chart-a1-pie'));
    var a1data = Object.entries(A1_COUNTS).map(function(e) {{ return {{ name: e[0], value: e[1] }}; }});
    a1pie.setOption({{
        tooltip: {{ trigger: 'item', formatter: '{{b}}: {{c}} ({{d}}%)' }},
        series: [{{
            type: 'pie', radius: ['30%','60%'],
            data: a1data,
            label: {{ color: '#e6edf3', fontSize: 10, formatter: '{{b}}\\n{{d}}%' }},
            emphasis: {{ itemStyle: {{ shadowBlur: 10 }} }}
        }}],
        backgroundColor: 'transparent'
    }});

    // Top A3 table
    var topTbody = document.getElementById('a3-top-table');
    A3_DATA.benchmarks.slice(0, 10).forEach(function(b) {{
        topTbody.innerHTML += '<tr><td>' + b.name + '</td><td>' + b.tradition + '</td><td><strong>' + b.score + '</strong></td></tr>';
    }});

    // Bottom A3 table
    var botTbody = document.getElementById('a3-bottom-table');
    A3_DATA.benchmarks.slice(-10).reverse().forEach(function(b) {{
        botTbody.innerHTML += '<tr><td>' + b.name + '</td><td>' + b.tradition + '</td><td>' + b.score + '</td></tr>';
    }});
}}

// ===== TAB 5: Claim Evidence =====
function renderClaims() {{
    // Chart
    var cc = echarts.init(document.getElementById('chart-claims'));
    var claimLabels = CLAIMS.map(function(c) {{ return c.claim + ': ' + c.text.substring(0, 50); }});
    var claimVals = CLAIMS.map(function(c) {{
        var color = c.significant ? '#54A24B' : c.marginal ? '#F58518' : '#E45756';
        return {{ value: c.neg_log_p, itemStyle: {{ color: color }} }};
    }});
    cc.setOption({{
        tooltip: {{
            trigger: 'axis',
            formatter: function(p) {{
                var c = CLAIMS[CLAIMS.length - 1 - p[0].dataIndex];
                var pstr = c.p_value < 0.001 ? 'p < 0.001' : 'p = ' + c.p_value.toFixed(4);
                return c.claim + ': ' + c.text.substring(0,60) + '<br>' + pstr;
            }}
        }},
        xAxis: {{ type: 'value', name: '-log10(p)', nameLocation: 'middle', nameGap: 30, axisLabel: {{ color: '#8b949e' }}, splitLine: {{ lineStyle: {{ color: '#21262d' }} }} }},
        yAxis: {{ type: 'category', data: claimLabels.slice().reverse(), axisLabel: {{ color: '#8b949e', fontSize: 9 }}, axisLine: {{ lineStyle: {{ color: '#30363d' }} }} }},
        series: [{{
            type: 'bar', data: claimVals.slice().reverse(), barMaxWidth: 24,
            markLine: {{
                silent: true,
                lineStyle: {{ color: '#aaa', type: 'dashed', width: 1.2 }},
                label: {{ formatter: 'p = 0.05', color: '#aaa', fontSize: 10 }},
                data: [{{ xAxis: 1.301 }}]
            }}
        }}],
        grid: {{ left: 300, right: 30, top: 10, bottom: 40 }},
        backgroundColor: 'transparent'
    }});

    // Claim cards
    var cardsDiv = document.getElementById('claim-cards');
    CLAIMS.forEach(function(c) {{
        var color = c.significant ? '#54A24B' : c.marginal ? '#F58518' : '#E45756';
        var status = c.significant ? 'SUPPORTED' : c.marginal ? 'MARGINAL' : 'NOT SUPPORTED';
        var pstr = c.p_value < 0.001 ? 'p < 0.001' : 'p = ' + c.p_value.toFixed(4);
        cardsDiv.innerHTML += '<div class="claim-card">' +
            '<span class="claim-num">' + c.claim + '</span> ' +
            '<span class="claim-text">' + c.text + '</span>' +
            '<div class="claim-pval" style="color:' + color + '"><strong>' + status + '</strong> (' + pstr + ')</div>' +
            '<div class="claim-interp">' + c.interpretation + '</div>' +
            '</div>';
    }});
}}

// ===== Initialize =====
document.addEventListener('DOMContentLoaded', function() {{
    renderOverview();

    // Lazy-render tabs on first show
    var rendered = {{ overview: true }};
    document.querySelectorAll('#mainTabs .nav-link').forEach(function(tab) {{
        tab.addEventListener('shown.bs.tab', function(e) {{
            var target = e.target.getAttribute('href').replace('#tab-', '');
            if (!rendered[target]) {{
                rendered[target] = true;
                if (target === 'sensitivity') renderSensitivity();
                else if (target === 'void') renderVoid();
                else if (target === 'values') renderValues();
                else if (target === 'claims') renderClaims();
            }}
            // Resize charts on tab show (ECharts needs this)
            setTimeout(function() {{
                document.querySelectorAll('.tab-pane.active [id^="chart-"]').forEach(function(el) {{
                    var chart = echarts.getInstanceByDom(el);
                    if (chart) chart.resize();
                }});
            }}, 100);
        }});
    }});

    // Window resize
    window.addEventListener('resize', function() {{
        document.querySelectorAll('[id^="chart-"]').forEach(function(el) {{
            var chart = echarts.getInstanceByDom(el);
            if (chart) chart.resize();
        }});
    }});
}});
</script>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

OUT.write_text(html)
print(f"Dashboard written to {OUT}")
print(f"File size: {OUT.stat().st_size:,} bytes")
