#!/usr/bin/env python3
"""
Phase 7: Generate Religious Values Benchmark Dashboard

Produces a self-contained HTML dashboard with embedded data using
"fat data, thin client" architecture: ECharts 5 + Bootstrap 5.3.

Tabs:
  1. Overview — Candidate pool summary, tradition coverage heatmap, format distribution
  2. Feature Matrix — Interactive table of all scored candidates
  3. Top 15 — Ranked cards with radar charts and tradition badges
  4. Tradition Coverage — Per-tradition breakdown with gap analysis
  5. Harness Compatibility — Which benchmarks work with which harnesses
  6. Eval-of-Evals — Meta-evaluation criteria visualization

Output: RELIGIOUS-VALUES/dashboard/YYYYMMDD-religious-values-benchmark-dashboard.html
"""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
DATA_DIR = PROJECT_DIR / "data"
DASHBOARD_DIR = PROJECT_DIR / "dashboard"

TODAY = date.today().strftime("%Y%m%d")

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------
def load_data() -> dict:
    """Load all generated data files."""
    data = {}

    # Feature matrix
    fm_files = sorted(DATA_DIR.glob("*-religious-benchmark-feature-matrix.json"))
    if fm_files:
        with open(fm_files[-1]) as f:
            data["feature_matrix"] = json.load(f)

    # Top 15
    t15_files = sorted(DATA_DIR.glob("*-religious-values-top15.json"))
    if t15_files:
        with open(t15_files[-1]) as f:
            data["top15"] = json.load(f)

    # Candidates
    cand_files = sorted(DATA_DIR.glob("*-religious-benchmark-candidates.json"))
    if cand_files:
        with open(cand_files[-1]) as f:
            data["candidates"] = json.load(f)

    # Format taxonomy
    fmt_files = sorted(DATA_DIR.glob("*-format-taxonomy.json"))
    if fmt_files:
        with open(fmt_files[-1]) as f:
            data["format_taxonomy"] = json.load(f)

    # External search
    ext_files = sorted(DATA_DIR.glob("*-external-search-results.json"))
    if ext_files:
        with open(ext_files[-1]) as f:
            data["external"] = json.load(f)

    return data


# ---------------------------------------------------------------------------
# Pre-compute analytics
# ---------------------------------------------------------------------------
def compute_analytics(data: dict) -> dict:
    """Pre-compute all dashboard analytics from loaded data."""
    fm = data.get("feature_matrix", {})
    entries = fm.get("entries", [])
    top15 = data.get("top15", {}).get("top15", [])
    candidates = data.get("candidates", {})

    analytics = {}

    # Overview stats
    analytics["total_papers_scanned"] = candidates.get("total_papers_scanned", 0)
    analytics["total_candidates"] = candidates.get("primary_candidate_count", 0)
    analytics["total_matrix_entries"] = len(entries)
    analytics["gate_passers"] = sum(1 for e in entries if e.get("passes_gates"))
    analytics["top15_count"] = len(top15)

    # Tradition distribution
    trad_dist = {}
    for e in entries:
        trad = e.get("D5_primary_tradition", "Unknown")
        trad_dist[trad] = trad_dist.get(trad, 0) + 1
    analytics["tradition_distribution"] = trad_dist

    # Family distribution
    fam_dist = {}
    for e in entries:
        fam = e.get("D6_tradition_family", "Unknown")
        fam_dist[fam] = fam_dist.get(fam, 0) + 1
    analytics["family_distribution"] = fam_dist

    # Year distribution
    year_dist = {}
    for e in entries:
        yr = e.get("D1_year", "Unknown")[:4] if e.get("D1_year") else "Unknown"
        year_dist[yr] = year_dist.get(yr, 0) + 1
    analytics["year_distribution"] = year_dist

    # Format distribution
    fmt_dist = {}
    for e in entries:
        fmt = e.get("P1_format", "Unknown")
        fmt_dist[fmt] = fmt_dist.get(fmt, 0) + 1
    analytics["format_distribution"] = fmt_dist

    # Score distributions (for gate-passers)
    passers = [e for e in entries if e.get("passes_gates")]
    analytics["rd_scores"] = [e["RD_score"] for e in passers]
    analytics["pe_scores"] = [e["PE_score"] for e in passers]
    analytics["ci_scores"] = [e["CI_score"] for e in passers]
    analytics["composites"] = [e["COMPOSITE"] for e in passers]

    # Top 15 details
    analytics["top15_entries"] = []
    for e in top15:
        analytics["top15_entries"].append({
            "rank": top15.index(e) + 1,
            "title": e.get("short_title", ""),
            "year": e.get("year", "")[:4],
            "tradition": e.get("D5_primary_tradition", ""),
            "family": e.get("D6_tradition_family", ""),
            "format": e.get("P1_format", ""),
            "composite": e.get("COMPOSITE", 0),
            "rd": e.get("RD_score", 0),
            "pe": e.get("PE_score", 0),
            "ci": e.get("CI_score", 0),
            "data_url": e.get("DATA_URL", ""),
            "data_avail": e.get("P3_data_availability", ""),
            "size": e.get("P2_dataset_size", 0),
            "abstract": e.get("abstract", "")[:200],
            "filename": e.get("filename", ""),
        })

    # Tradition coverage for all 14 traditions
    all_traditions = [
        "Islam", "Christianity", "Judaism",
        "Hinduism", "Buddhism", "Jainism", "Sikhism",
        "Confucianism", "Taoism", "Shinto",
        "Ubuntu Philosophy", "Indigenous Spirituality",
        "Baha'i", "Zoroastrianism",
    ]
    coverage = {}
    for trad in all_traditions:
        total = sum(1 for e in entries if e.get("D5_primary_tradition") == trad)
        gate_pass = sum(1 for e in passers if e.get("D5_primary_tradition") == trad)
        in_top15 = sum(1 for e in top15 if e.get("D5_primary_tradition") == trad)
        coverage[trad] = {"total": total, "gate_pass": gate_pass, "top15": in_top15}
    analytics["tradition_coverage"] = coverage

    # Feature matrix table (gate-passers only, limited fields)
    analytics["matrix_table"] = []
    for e in sorted(passers, key=lambda x: -x.get("COMPOSITE", 0)):
        analytics["matrix_table"].append({
            "title": e.get("short_title", "")[:50],
            "year": e.get("year", "")[:4],
            "tradition": e.get("D5_primary_tradition", ""),
            "family": e.get("D6_tradition_family", ""),
            "format": e.get("P1_format", ""),
            "composite": round(e.get("COMPOSITE", 0), 1),
            "rd": round(e.get("RD_score", 0), 1),
            "pe": round(e.get("PE_score", 0), 1),
            "ci": round(e.get("CI_score", 0), 1),
            "data": e.get("P3_data_availability", "N/A"),
            "size": e.get("P2_dataset_size", 0),
            "in_top15": any(t.get("filename") == e.get("filename") for t in top15),
        })

    # Gap analysis
    gaps = []
    for trad in all_traditions:
        if coverage[trad]["gate_pass"] == 0:
            gaps.append(trad)
    analytics["tradition_gaps"] = gaps

    # External search results count
    ext = data.get("external", {})
    analytics["external_results_count"] = ext.get("total_results", 0)
    analytics["external_tradition_dist"] = ext.get("tradition_distribution", {})

    return analytics


# ---------------------------------------------------------------------------
# HTML Generation
# ---------------------------------------------------------------------------
def generate_dashboard(analytics: dict) -> str:
    """Generate the complete HTML dashboard."""

    # Convert analytics to JS
    analytics_js = json.dumps(analytics, indent=2, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Religious Values Benchmark Dashboard</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/echarts@5.5.0/dist/echarts.min.js"></script>
<style>
:root {{
  --bg-primary: #0f1117;
  --bg-secondary: #1a1d2e;
  --bg-card: #1e2235;
  --text-primary: #e8eaed;
  --text-secondary: #9aa0b4;
  --accent-blue: #4f8cff;
  --accent-green: #48c774;
  --accent-orange: #ff9f43;
  --accent-red: #ff6b6b;
  --accent-purple: #a78bfa;
  --border: #2d3250;
}}
body {{ font-family: 'Inter', sans-serif; background: var(--bg-primary); color: var(--text-primary); margin: 0; }}
.navbar {{ background: var(--bg-secondary) !important; border-bottom: 1px solid var(--border); }}
.navbar-brand {{ font-weight: 700; color: var(--accent-purple) !important; }}
.nav-tabs {{ border-bottom: 1px solid var(--border); }}
.nav-tabs .nav-link {{ color: var(--text-secondary); border: none; padding: 12px 20px; }}
.nav-tabs .nav-link.active {{ color: var(--accent-blue); background: transparent; border-bottom: 2px solid var(--accent-blue); }}
.nav-tabs .nav-link:hover {{ color: var(--text-primary); }}
.card {{ background: var(--bg-card); border: 1px solid var(--border); border-radius: 12px; }}
.card-header {{ background: transparent; border-bottom: 1px solid var(--border); font-weight: 600; }}
.stat-card {{ text-align: center; padding: 20px; }}
.stat-value {{ font-size: 2.5rem; font-weight: 700; color: var(--accent-blue); }}
.stat-label {{ font-size: 0.85rem; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 0.5px; }}
.badge-abrahamic {{ background: var(--accent-blue); }}
.badge-dharmic {{ background: var(--accent-orange); }}
.badge-eastasian {{ background: var(--accent-green); }}
.badge-african {{ background: var(--accent-purple); }}
.badge-other {{ background: var(--text-secondary); }}
.top15-row {{ transition: background 0.2s; }}
.top15-row:hover {{ background: rgba(79, 140, 255, 0.1); }}
.chart-container {{ width: 100%; height: 350px; }}
.chart-container-lg {{ width: 100%; height: 450px; }}
table {{ color: var(--text-primary); }}
.table {{ --bs-table-bg: transparent; --bs-table-color: var(--text-primary); --bs-table-border-color: var(--border); }}
.table thead th {{ border-bottom: 2px solid var(--border); color: var(--text-secondary); font-size: 0.8rem; text-transform: uppercase; }}
.gap-badge {{ background: var(--accent-red); color: white; padding: 2px 8px; border-radius: 4px; font-size: 0.75rem; }}
.covered-badge {{ background: var(--accent-green); color: white; padding: 2px 8px; border-radius: 4px; font-size: 0.75rem; }}
.tab-content {{ padding: 24px 0; }}
.container {{ max-width: 1400px; }}
</style>
</head>
<body>
<nav class="navbar navbar-dark px-3">
  <span class="navbar-brand">Religious Values Benchmark Dashboard</span>
  <span class="text-secondary small">Generated {TODAY} | CEI Literature Vault</span>
</nav>

<div class="container mt-3">
<ul class="nav nav-tabs" id="mainTabs" role="tablist">
  <li class="nav-item"><a class="nav-link active" data-bs-toggle="tab" href="#overview">Overview</a></li>
  <li class="nav-item"><a class="nav-link" data-bs-toggle="tab" href="#matrix">Feature Matrix</a></li>
  <li class="nav-item"><a class="nav-link" data-bs-toggle="tab" href="#top15">Top 15</a></li>
  <li class="nav-item"><a class="nav-link" data-bs-toggle="tab" href="#traditions">Tradition Coverage</a></li>
  <li class="nav-item"><a class="nav-link" data-bs-toggle="tab" href="#methodology">Eval-of-Evals</a></li>
</ul>

<div class="tab-content" id="mainTabContent">

<!-- OVERVIEW TAB -->
<div class="tab-pane fade show active" id="overview" role="tabpanel">
  <div class="row g-3 mb-4">
    <div class="col-md-2"><div class="card stat-card"><div class="stat-value" id="stat-scanned">—</div><div class="stat-label">Papers Scanned</div></div></div>
    <div class="col-md-2"><div class="card stat-card"><div class="stat-value" id="stat-candidates">—</div><div class="stat-label">RV Candidates</div></div></div>
    <div class="col-md-2"><div class="card stat-card"><div class="stat-value" id="stat-scored">—</div><div class="stat-label">Matrix Entries</div></div></div>
    <div class="col-md-2"><div class="card stat-card"><div class="stat-value" id="stat-passers">—</div><div class="stat-label">Gate Passers</div></div></div>
    <div class="col-md-2"><div class="card stat-card"><div class="stat-value" id="stat-top15">—</div><div class="stat-label">Top 15 Selected</div></div></div>
    <div class="col-md-2"><div class="card stat-card"><div class="stat-value" id="stat-gaps">—</div><div class="stat-label">Tradition Gaps</div></div></div>
  </div>
  <div class="row g-3">
    <div class="col-md-6"><div class="card"><div class="card-header">Tradition Family Distribution</div><div class="card-body"><div id="chart-family" class="chart-container"></div></div></div></div>
    <div class="col-md-6"><div class="card"><div class="card-header">Year Distribution</div><div class="card-body"><div id="chart-year" class="chart-container"></div></div></div></div>
  </div>
  <div class="row g-3 mt-2">
    <div class="col-md-6"><div class="card"><div class="card-header">Format Distribution</div><div class="card-body"><div id="chart-format" class="chart-container"></div></div></div></div>
    <div class="col-md-6"><div class="card"><div class="card-header">Score Distribution (Gate Passers)</div><div class="card-body"><div id="chart-scores" class="chart-container"></div></div></div></div>
  </div>
</div>

<!-- FEATURE MATRIX TAB -->
<div class="tab-pane fade" id="matrix" role="tabpanel">
  <div class="card">
    <div class="card-header d-flex justify-content-between align-items-center">
      Feature Matrix (Gate-Passing Candidates)
      <div>
        <select id="filter-family" class="form-select form-select-sm d-inline-block" style="width:auto;background:var(--bg-secondary);color:var(--text-primary);border-color:var(--border)">
          <option value="all">All Families</option>
          <option value="Abrahamic">Abrahamic</option>
          <option value="Dharmic">Dharmic</option>
          <option value="East Asian">East Asian</option>
          <option value="African/Indigenous">African/Indigenous</option>
        </select>
      </div>
    </div>
    <div class="card-body p-0">
      <div class="table-responsive">
        <table class="table table-sm mb-0" id="matrix-table">
          <thead>
            <tr><th>#</th><th>Title</th><th>Year</th><th>Tradition</th><th>Family</th><th>Format</th><th>Composite</th><th>RD</th><th>PE</th><th>CI</th><th>Data</th><th>Size</th><th>Top 15</th></tr>
          </thead>
          <tbody id="matrix-tbody"></tbody>
        </table>
      </div>
    </div>
  </div>
</div>

<!-- TOP 15 TAB -->
<div class="tab-pane fade" id="top15" role="tabpanel">
  <div class="row g-3 mb-4">
    <div class="col-md-6"><div class="card"><div class="card-header">Top 15 Radar Comparison</div><div class="card-body"><div id="chart-radar" class="chart-container-lg"></div></div></div></div>
    <div class="col-md-6"><div class="card"><div class="card-header">Composite Score Distribution</div><div class="card-body"><div id="chart-top15-bar" class="chart-container-lg"></div></div></div></div>
  </div>
  <div class="card">
    <div class="card-header">Ranked Selection</div>
    <div class="card-body p-0">
      <table class="table table-sm mb-0">
        <thead><tr><th>#</th><th>Title</th><th>Year</th><th>Tradition</th><th>Format</th><th>COMP</th><th>RD</th><th>PE</th><th>CI</th><th>Data</th><th>Size</th></tr></thead>
        <tbody id="top15-tbody"></tbody>
      </table>
    </div>
  </div>
</div>

<!-- TRADITION COVERAGE TAB -->
<div class="tab-pane fade" id="traditions" role="tabpanel">
  <div class="row g-3 mb-4">
    <div class="col-12"><div class="card"><div class="card-header">Tradition Coverage Heatmap</div><div class="card-body"><div id="chart-coverage" class="chart-container-lg"></div></div></div></div>
  </div>
  <div class="card">
    <div class="card-header">Coverage Details</div>
    <div class="card-body p-0">
      <table class="table table-sm mb-0">
        <thead><tr><th>Tradition</th><th>Family</th><th>Total Candidates</th><th>Gate Passers</th><th>In Top 15</th><th>Status</th></tr></thead>
        <tbody id="coverage-tbody"></tbody>
      </table>
    </div>
  </div>
</div>

<!-- EVAL-OF-EVALS TAB -->
<div class="tab-pane fade" id="methodology" role="tabpanel">
  <div class="row g-3">
    <div class="col-md-8">
      <div class="card">
        <div class="card-header">Meta-Evaluation Framework</div>
        <div class="card-body">
          <h5 class="text-info">7 Criteria for Evaluating Religious Values Benchmarks</h5>
          <div class="row g-3 mt-2">
            <div class="col-md-6">
              <div class="card bg-dark p-3 mb-2"><strong class="text-warning">1. Content Validity</strong><br><small class="text-secondary">Does it test real theological content vs. surface keywords?</small></div>
              <div class="card bg-dark p-3 mb-2"><strong class="text-warning">2. Discriminative Power</strong><br><small class="text-secondary">Can it distinguish between models? Watch for ceiling effects.</small></div>
              <div class="card bg-dark p-3 mb-2"><strong class="text-warning">3. Cultural Authenticity</strong><br><small class="text-secondary">Created by scholars from the tradition being evaluated?</small></div>
              <div class="card bg-dark p-3 mb-2"><strong class="text-warning">4. Reproducibility</strong><br><small class="text-secondary">Public data + code + documented metrics + prompts?</small></div>
            </div>
            <div class="col-md-6">
              <div class="card bg-dark p-3 mb-2"><strong class="text-warning">5. Complementarity</strong><br><small class="text-secondary">Does this add info not provided by other benchmarks?</small></div>
              <div class="card bg-dark p-3 mb-2"><strong class="text-warning">6. Construct Coverage</strong><br><small class="text-secondary">Knowledge vs. Reasoning vs. Values vs. Sensitivity vs. Pluralism?</small></div>
              <div class="card bg-dark p-3 mb-2"><strong class="text-warning">7. Annotation Quality</strong><br><small class="text-secondary">Expert theologians vs. crowdworkers vs. auto-generated?</small></div>
            </div>
          </div>
          <hr style="border-color:var(--border)">
          <h5 class="text-info mt-3">Implementation Trial Protocol</h5>
          <ol class="text-secondary">
            <li>Sample 20-50 items from benchmark</li>
            <li>Run on 3+ models (frontier closed + frontier open + mid-tier)</li>
            <li>Zero-shot + 3-shot prompting</li>
            <li>Check ceiling/floor effects, discriminative power, error patterns</li>
            <li>Verdict: IMPLEMENT / MODIFY / SKIP</li>
          </ol>
        </div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card">
        <div class="card-header">Expert Council (7 Members)</div>
        <div class="card-body">
          <div class="mb-2"><span class="badge bg-primary">1</span> Theology/Religious Studies Scholar</div>
          <div class="mb-2"><span class="badge bg-primary">2</span> AI Evaluation Researcher</div>
          <div class="mb-2"><span class="badge bg-primary">3</span> Cross-Cultural Psychologist</div>
          <div class="mb-2"><span class="badge bg-primary">4</span> NLP/ML Benchmarking Expert</div>
          <div class="mb-2"><span class="badge bg-primary">5</span> Comparative Religion Specialist</div>
          <div class="mb-2"><span class="badge bg-primary">6</span> Psychometrician</div>
          <div class="mb-2"><span class="badge bg-primary">7</span> Data Scientist/Bibliometrician</div>
        </div>
      </div>
      <div class="card mt-3">
        <div class="card-header">Scoring Weights</div>
        <div class="card-body">
          <div id="chart-weights" style="width:100%;height:200px;"></div>
        </div>
      </div>
    </div>
  </div>
</div>

</div><!-- tab-content -->
</div><!-- container -->

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<script>
// ============================================================
// EMBEDDED DATA (fat data, thin client)
// ============================================================
const DATA = {analytics_js};

// ============================================================
// Color palette (Okabe-Ito inspired)
// ============================================================
const FAMILY_COLORS = {{
  'Abrahamic': '#4f8cff',
  'Dharmic': '#ff9f43',
  'East Asian': '#48c774',
  'African/Indigenous': '#a78bfa',
  'Other': '#9aa0b4',
  'Unknown': '#555',
}};

const FORMAT_COLORS = {{
  'MCQ': '#4f8cff', 'MRC': '#48c774', 'BIN': '#ff6b6b', 'SCN': '#ff9f43',
  'OPN': '#a78bfa', 'PSY': '#f0c674', 'MTN': '#56b6c2', 'RAG': '#e06c75',
  'TXT': '#98c379', 'MUL': '#c678dd', 'SHT': '#61afef', 'MIX': '#9aa0b4',
}};

// ============================================================
// Overview Tab
// ============================================================
function renderOverview() {{
  document.getElementById('stat-scanned').textContent = DATA.total_papers_scanned.toLocaleString();
  document.getElementById('stat-candidates').textContent = DATA.total_candidates.toLocaleString();
  document.getElementById('stat-scored').textContent = DATA.total_matrix_entries.toLocaleString();
  document.getElementById('stat-passers').textContent = DATA.gate_passers.toLocaleString();
  document.getElementById('stat-top15').textContent = DATA.top15_count;
  document.getElementById('stat-gaps').textContent = DATA.tradition_gaps.length;

  // Family pie chart
  const famData = Object.entries(DATA.family_distribution).map(([k,v]) => ({{name:k, value:v, itemStyle:{{color:FAMILY_COLORS[k]||'#555'}}}}));
  echarts.init(document.getElementById('chart-family')).setOption({{
    tooltip: {{trigger:'item'}},
    series: [{{type:'pie', radius:['40%','70%'], data: famData, label:{{color:'#9aa0b4'}}, emphasis:{{label:{{fontSize:14}}}}}}]
  }});

  // Year bar chart
  const years = Object.keys(DATA.year_distribution).sort();
  echarts.init(document.getElementById('chart-year')).setOption({{
    tooltip: {{}},
    xAxis: {{type:'category', data: years, axisLabel:{{color:'#9aa0b4'}}}},
    yAxis: {{type:'value', axisLabel:{{color:'#9aa0b4'}}}},
    series: [{{type:'bar', data: years.map(y=>DATA.year_distribution[y]), itemStyle:{{color:'#4f8cff'}}}}]
  }});

  // Format bar chart
  const fmts = Object.entries(DATA.format_distribution).sort((a,b)=>b[1]-a[1]);
  echarts.init(document.getElementById('chart-format')).setOption({{
    tooltip: {{}},
    xAxis: {{type:'category', data: fmts.map(f=>f[0]), axisLabel:{{color:'#9aa0b4', rotate:45}}}},
    yAxis: {{type:'value', axisLabel:{{color:'#9aa0b4'}}}},
    series: [{{type:'bar', data: fmts.map(f=>({{value:f[1], itemStyle:{{color:FORMAT_COLORS[f[0]]||'#555'}}}}))}}]
  }});

  // Score boxplot (histogram of composites)
  const bins = [0,10,20,30,40,50,60,70,80,90,100];
  const hist = bins.slice(0,-1).map((_,i) => DATA.composites.filter(c => c >= bins[i] && c < bins[i+1]).length);
  echarts.init(document.getElementById('chart-scores')).setOption({{
    tooltip: {{}},
    xAxis: {{type:'category', data: bins.slice(0,-1).map((b,i)=>`${{b}}-${{bins[i+1]}}`), axisLabel:{{color:'#9aa0b4'}}}},
    yAxis: {{type:'value', axisLabel:{{color:'#9aa0b4'}}}},
    series: [{{type:'bar', data: hist, itemStyle:{{color:'#48c774'}}}}]
  }});
}}

// ============================================================
// Feature Matrix Tab
// ============================================================
function renderMatrix() {{
  const tbody = document.getElementById('matrix-tbody');
  function render(filter) {{
    const rows = DATA.matrix_table.filter(r => filter === 'all' || r.family === filter);
    tbody.innerHTML = rows.map((r,i) => `
      <tr class="${{r.in_top15 ? 'top15-row' : ''}}">
        <td>${{i+1}}</td>
        <td>${{r.title}}</td>
        <td>${{r.year}}</td>
        <td>${{r.tradition}}</td>
        <td><span class="badge badge-${{r.family.toLowerCase().replace(/\\//g,'')}}">${{r.family}}</span></td>
        <td><span class="badge" style="background:${{FORMAT_COLORS[r.format]||'#555'}}">${{r.format}}</span></td>
        <td><strong>${{r.composite}}</strong></td>
        <td>${{r.rd}}</td><td>${{r.pe}}</td><td>${{r.ci}}</td>
        <td>${{r.data}}</td>
        <td>${{r.size || '—'}}</td>
        <td>${{r.in_top15 ? '<span class="badge bg-success">Yes</span>' : ''}}</td>
      </tr>
    `).join('');
  }}
  render('all');
  document.getElementById('filter-family').addEventListener('change', e => render(e.target.value));
}}

// ============================================================
// Top 15 Tab
// ============================================================
function renderTop15() {{
  const top15 = DATA.top15_entries;
  // Table
  const tbody = document.getElementById('top15-tbody');
  tbody.innerHTML = top15.map(r => `
    <tr class="top15-row">
      <td><strong>${{r.rank}}</strong></td>
      <td>${{r.title}}</td>
      <td>${{r.year}}</td>
      <td><span class="badge badge-${{r.family.toLowerCase().replace(/\\//g,'')}}">${{r.tradition}}</span></td>
      <td><span class="badge" style="background:${{FORMAT_COLORS[r.format]||'#555'}}">${{r.format}}</span></td>
      <td><strong>${{r.composite.toFixed(1)}}</strong></td>
      <td>${{r.rd.toFixed(1)}}</td><td>${{r.pe.toFixed(1)}}</td><td>${{r.ci.toFixed(1)}}</td>
      <td>${{r.data_avail || '—'}}</td>
      <td>${{r.size || '—'}}</td>
    </tr>
  `).join('');

  // Radar chart (top 5)
  const radarData = top15.slice(0,5).map(r => ({{
    name: r.title.substring(0,25) + '...',
    value: [r.rd, r.pe, r.ci],
  }}));
  echarts.init(document.getElementById('chart-radar')).setOption({{
    tooltip: {{}},
    legend: {{data: radarData.map(d=>d.name), textStyle:{{color:'#9aa0b4'}}, bottom: 0}},
    radar: {{
      indicator: [
        {{name:'Religious Depth', max:100}},
        {{name:'Practical Ease', max:100}},
        {{name:'Citation Impact', max:100}},
      ],
      axisName: {{color:'#9aa0b4'}},
      splitArea: {{areaStyle:{{color:['rgba(79,140,255,0.05)','rgba(79,140,255,0.1)']}}}},
      splitLine: {{lineStyle:{{color:'#2d3250'}}}},
    }},
    series: [{{type:'radar', data: radarData}}]
  }});

  // Bar chart
  echarts.init(document.getElementById('chart-top15-bar')).setOption({{
    tooltip: {{}},
    grid: {{left: 200}},
    xAxis: {{type:'value', max:60, axisLabel:{{color:'#9aa0b4'}}}},
    yAxis: {{type:'category', data: top15.map(r=>'#'+r.rank+' '+r.title.substring(0,25)).reverse(), axisLabel:{{color:'#9aa0b4', fontSize:10, width:190, overflow:'truncate'}}}},
    series: [
      {{name:'RD', type:'bar', stack:'score', data: top15.map(r=>r.rd*0.4).reverse(), itemStyle:{{color:'#4f8cff'}}}},
      {{name:'PE', type:'bar', stack:'score', data: top15.map(r=>r.pe*0.35).reverse(), itemStyle:{{color:'#48c774'}}}},
      {{name:'CI', type:'bar', stack:'score', data: top15.map(r=>r.ci*0.25).reverse(), itemStyle:{{color:'#ff9f43'}}}},
    ],
    legend: {{data:['RD','PE','CI'], textStyle:{{color:'#9aa0b4'}}}},
  }});
}}

// ============================================================
// Tradition Coverage Tab
// ============================================================
function renderTraditions() {{
  const coverage = DATA.tradition_coverage;
  const traditions = Object.keys(coverage);
  const families = {{'Islam':'Abrahamic','Christianity':'Abrahamic','Judaism':'Abrahamic',
    'Hinduism':'Dharmic','Buddhism':'Dharmic','Jainism':'Dharmic','Sikhism':'Dharmic',
    'Confucianism':'East Asian','Taoism':'East Asian','Shinto':'East Asian',
    'Ubuntu Philosophy':'African/Indigenous','Indigenous Spirituality':'African/Indigenous',
    "Baha'i":'Other','Zoroastrianism':'Other'}};

  // Table
  const tbody = document.getElementById('coverage-tbody');
  tbody.innerHTML = traditions.map(t => {{
    const c = coverage[t];
    const status = c.gate_pass === 0 ? '<span class="gap-badge">CRITICAL GAP</span>'
      : c.top15 > 0 ? '<span class="covered-badge">In Top 15</span>'
      : 'Available';
    return `<tr>
      <td>${{t}}</td>
      <td><span class="badge badge-${{(families[t]||'other').toLowerCase().replace(/\\//g,'')}}">${{families[t]||'Other'}}</span></td>
      <td>${{c.total}}</td><td>${{c.gate_pass}}</td><td>${{c.top15}}</td><td>${{status}}</td>
    </tr>`;
  }}).join('');

  // Heatmap
  const categories = ['Total', 'Gate Pass', 'Top 15'];
  const heatData = [];
  traditions.forEach((t,ti) => {{
    const c = coverage[t];
    heatData.push([0, ti, c.total]);
    heatData.push([1, ti, c.gate_pass]);
    heatData.push([2, ti, c.top15]);
  }});
  echarts.init(document.getElementById('chart-coverage')).setOption({{
    tooltip: {{formatter: p => `${{traditions[p.data[1]]}}: ${{categories[p.data[0]]}} = ${{p.data[2]}}`}},
    grid: {{left: 180}},
    xAxis: {{type:'category', data: categories, axisLabel:{{color:'#9aa0b4'}}}},
    yAxis: {{type:'category', data: traditions, axisLabel:{{color:'#9aa0b4', fontSize:11, width:170, overflow:'truncate'}}}},
    visualMap: {{min:0, max:50, calculable:true, orient:'horizontal', left:'center', bottom:0,
      inRange:{{color:['#1a1d2e','#2d3250','#4f8cff','#48c774']}},
      textStyle:{{color:'#9aa0b4'}}}},
    series: [{{type:'heatmap', data: heatData, label:{{show:true, color:'#e8eaed'}},
      itemStyle:{{borderWidth:2, borderColor:'#0f1117'}}}}]
  }});
}}

// ============================================================
// Scoring weights donut
// ============================================================
function renderWeights() {{
  echarts.init(document.getElementById('chart-weights')).setOption({{
    series: [{{type:'pie', radius:['50%','80%'], data:[
      {{name:'RD (40%)', value:40, itemStyle:{{color:'#4f8cff'}}}},
      {{name:'PE (35%)', value:35, itemStyle:{{color:'#48c774'}}}},
      {{name:'CI (25%)', value:25, itemStyle:{{color:'#ff9f43'}}}},
    ], label:{{color:'#9aa0b4', fontSize:11}}}}]
  }});
}}

// ============================================================
// Initialize
// ============================================================
document.addEventListener('DOMContentLoaded', () => {{
  renderOverview();
  renderMatrix();
  renderTop15();
  renderTraditions();
  renderWeights();
}});
</script>
</body>
</html>"""

    return html


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print(f"=== Phase 7: Generate Religious Values Benchmark Dashboard ===")

    data = load_data()
    print(f"Loaded data files: {list(data.keys())}")

    analytics = compute_analytics(data)
    print(f"Computed analytics: {len(analytics)} keys")
    print(f"  Gate passers: {analytics['gate_passers']}")
    print(f"  Top 15: {analytics['top15_count']}")
    print(f"  Tradition gaps: {analytics['tradition_gaps']}")

    html = generate_dashboard(analytics)

    DASHBOARD_DIR.mkdir(parents=True, exist_ok=True)
    out_path = DASHBOARD_DIR / f"{TODAY}-religious-values-benchmark-dashboard.html"
    out_path.write_text(html, encoding="utf-8")

    size_mb = out_path.stat().st_size / (1024 * 1024)
    print(f"\nDashboard: {out_path}")
    print(f"Size: {size_mb:.1f} MB")
    print(f"Done.")


if __name__ == "__main__":
    main()
