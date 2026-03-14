"""
generate_eval_dashboard.py
Combines three eval-framework HTML reports into a single 4-tab dashboard.
Run from: CEI-Lit-WS/
Output:   DASHBOARDS/20260313-eval-framework-dashboard.html
"""

import html
from pathlib import Path

BASE = Path(__file__).parent.parent          # CEI-Lit-WS/
STATS = BASE / "STATISTICS"
DASHBOARDS = BASE / "DASHBOARDS"

SOURCE_FILES = {
    "tab1": STATS / "20260313-eval-already-included-table.html",
    "tab2": STATS / "20260313-implementability-cross-framework-table.html",
    "tab3": STATS / "20260313-implementability-cross-framework-table-v2.html",
}

OUTPUT = DASHBOARDS / "20260313-eval-framework-dashboard.html"

# ---------------------------------------------------------------------------
# Overview tab — static HTML
# ---------------------------------------------------------------------------

OVERVIEW_HTML = """\
<div class="overview">
  <h2>CEI Eval Framework Dashboard</h2>
  <p class="subtitle">
    Coverage analysis of 2,043 CEI vault papers across 5 major AI evaluation frameworks.
    Use the tabs above to explore which papers are already implemented, and which are
    ready or possible candidates for each framework.
  </p>

  <div class="summary-box">
    <h3>Cross-Framework Summary</h3>
    <table class="summary-table">
      <thead>
        <tr>
          <th>Framework</th>
          <th>In Framework</th>
          <th>Ready</th>
          <th>Possible</th>
          <th>Notes</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="fw-badge lm">lm-eval</span></td>
          <td>78</td><td>176</td><td>409</td>
          <td>EleutherAI · 200+ benchmarks</td>
        </tr>
        <tr>
          <td><span class="fw-badge inspect">Inspect</span></td>
          <td>38</td><td>23</td><td>29</td>
          <td>UK AISI · model_graded_qa unique</td>
        </tr>
        <tr>
          <td><span class="fw-badge lighteval">LightEval</span></td>
          <td>—</td><td>99</td><td>771</td>
          <td>HuggingFace · no In-Framework tier</td>
        </tr>
        <tr>
          <td><span class="fw-badge helm">HELM</span></td>
          <td>19</td><td>—</td><td>—</td>
          <td>Stanford CRFM · holistic scenarios</td>
        </tr>
        <tr>
          <td><span class="fw-badge oaievals">OpenAI Evals</span></td>
          <td>—</td><td>783</td><td>872</td>
          <td>All 2,043 papers scored</td>
        </tr>
      </tbody>
    </table>
    <p class="note">107 papers appear in ≥1 framework (TABLE 1).</p>
  </div>

  <div class="framework-cards">

    <div class="card">
      <div class="card-header">
        <span class="fw-badge lm">lm-eval</span>
        <span class="org">EleutherAI · lm-evaluation-harness</span>
      </div>
      <p>
        The community-standard open-source harness with 200+ benchmarks.
        Supports multiple-choice, log-likelihood, and <code>generate_until</code> tasks.
        Widely adopted for reproducing published results and CI/CD eval pipelines.
      </p>
      <div class="stats-row">
        <span class="stat in-fw">78 In Framework</span>
        <span class="stat ready">176 Ready</span>
        <span class="stat possible">409 Possible</span>
      </div>
      <p class="best-for"><strong>Best for:</strong> Reproducing published benchmark results; automated eval pipelines.</p>
    </div>

    <div class="card">
      <div class="card-header">
        <span class="fw-badge inspect">Inspect</span>
        <span class="org">UK AI Safety Institute · inspect_ai</span>
      </div>
      <p>
        Purpose-built for safety and alignment evaluations. Its unique
        <code>model_graded_qa()</code> scorer enables rubric-based and scenario
        evaluations that lm-eval cannot handle. Task types: <code>choice()</code>,
        <code>match()</code>, <code>model_graded_qa()</code>, <code>model_graded_fact()</code>.
      </p>
      <div class="stats-row">
        <span class="stat in-fw">38 In Framework</span>
        <span class="stat ready">23 Ready</span>
        <span class="stat possible">29 Possible (model-graded unique)</span>
      </div>
      <p class="best-for"><strong>Best for:</strong> Safety/alignment evals requiring LLM-as-judge.</p>
    </div>

    <div class="card">
      <div class="card-header">
        <span class="fw-badge lighteval">LightEval</span>
        <span class="org">HuggingFace · lighteval</span>
      </div>
      <p>
        Lightweight, HuggingFace-native harness with the easiest HF dataset integration.
        Task types mirror lm-eval: multichoice, generate_until, loglikelihood.
        No "In Framework" tier is tracked (all scored as Ready/Possible).
      </p>
      <div class="stats-row">
        <span class="stat ready">99 Ready</span>
        <span class="stat possible">771 Possible</span>
      </div>
      <p class="best-for"><strong>Best for:</strong> Teams in the HF ecosystem; fast iteration on new models.</p>
    </div>

    <div class="card">
      <div class="card-header">
        <span class="fw-badge helm">HELM</span>
        <span class="org">Stanford CRFM · helm</span>
      </div>
      <p>
        Holistic Evaluation of Language Models uses a scenario abstraction layer
        providing the broadest metric coverage of any framework. Papers tagged
        <code>helm: "incorporated"</code> in the vault.
      </p>
      <div class="stats-row">
        <span class="stat in-fw">19 In Framework</span>
      </div>
      <p class="best-for"><strong>Best for:</strong> Comprehensive multi-metric evaluation with scenario reuse.</p>
    </div>

    <div class="card">
      <div class="card-header">
        <span class="fw-badge oaievals">OpenAI Evals</span>
        <span class="org">OpenAI · evals</span>
      </div>
      <p>
        JSONL registry format with templates: Match, ModelBasedClassify, FreeForm.
        All 2,043 vault papers have been scored against this framework — the highest
        Ready + Possible counts of any framework.
      </p>
      <div class="stats-row">
        <span class="stat ready">783 Ready</span>
        <span class="stat possible">872 Possible</span>
      </div>
      <p class="best-for"><strong>Best for:</strong> Structured community contributions; judge-based free-form evals.</p>
    </div>

  </div>

  <div class="tab-guide">
    <h3>Tab Guide</h3>
    <dl>
      <dt>TABLE 1 — Already Included</dt>
      <dd>107 papers that are already implemented in ≥1 framework. Filterable by framework, tier, and paper metadata.</dd>
      <dt>TABLE 2 — Implementability</dt>
      <dd>All 2,043 vault papers scored across all 5 frameworks with tier badges (In Framework / Ready / Possible / Unlikely). Sortable and filterable.</dd>
      <dt>TABLE 2 + Ethics</dt>
      <dd>Same as TABLE 2 with an additional normative ethics column and ethics-type filter row, enabling cross-referencing of implementability with ethics classification.</dd>
    </dl>
  </div>
</div>
"""

# ---------------------------------------------------------------------------
# CSS for the overview tab
# ---------------------------------------------------------------------------

OVERVIEW_CSS = """\
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Segoe UI', system-ui, sans-serif; background: #0f0f1a; color: #c8d0e8; }

/* ── Header ── */
#header {
  background: #1a1a2e;
  padding: 16px 24px 10px;
  border-bottom: 1px solid #2a2a4a;
}
#header h1 { font-size: 1.35rem; color: #a0b4e0; letter-spacing: .03em; }
#header p  { font-size: .82rem; color: #6a7490; margin-top: 2px; }

/* ── Tab bar ── */
#tabbar {
  position: sticky; top: 0; z-index: 100;
  background: #1a1a2e;
  display: flex; gap: 0;
  border-bottom: 2px solid #2a2a4a;
  padding: 0 16px;
}
.tab-btn {
  padding: 10px 20px;
  background: none; border: none; cursor: pointer;
  color: #6a7490; font-size: .88rem; font-family: inherit;
  border-bottom: 3px solid transparent;
  margin-bottom: -2px;
  transition: color .15s, border-color .15s;
  white-space: nowrap;
}
.tab-btn:hover  { color: #a0b4e0; }
.tab-btn.active { color: #a0b4e0; border-bottom-color: #a0b4e0; }

/* ── Content area ── */
#content-area { height: calc(100vh - 90px); position: relative; }
.tab-panel { display: none; height: 100%; }
.tab-panel.active { display: block; }
.tab-panel iframe {
  width: 100%; height: 100%; border: none;
  background: #0f0f1a;
}

/* ── Overview panel (scrollable div) ── */
#panel-overview { overflow-y: auto; padding: 28px 32px 48px; }

.overview h2 { font-size: 1.5rem; color: #a0b4e0; margin-bottom: 6px; }
.overview .subtitle { color: #8892aa; margin-bottom: 28px; max-width: 780px; line-height: 1.6; }

/* Summary box */
.summary-box { background: #1a1a2e; border: 1px solid #2a2a4a; border-radius: 8px;
  padding: 20px 24px; margin-bottom: 32px; }
.summary-box h3 { color: #7888b8; font-size: .95rem; text-transform: uppercase;
  letter-spacing: .08em; margin-bottom: 14px; }
.summary-table { width: 100%; border-collapse: collapse; font-size: .9rem; }
.summary-table th { text-align: left; color: #5a6480; font-weight: 600;
  padding: 6px 12px; border-bottom: 1px solid #2a2a4a; }
.summary-table td { padding: 8px 12px; border-bottom: 1px solid #1e1e32; }
.summary-table tr:last-child td { border-bottom: none; }
.note { font-size: .8rem; color: #5a6480; margin-top: 10px; }

/* Framework cards */
.framework-cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 18px; margin-bottom: 36px; }
.card { background: #1a1a2e; border: 1px solid #2a2a4a; border-radius: 8px; padding: 18px 20px; }
.card-header { display: flex; align-items: center; gap: 10px; margin-bottom: 10px; }
.org { font-size: .78rem; color: #5a6480; }
.card p { font-size: .875rem; color: #8892aa; line-height: 1.6; margin-bottom: 10px; }
.card code { background: #12122a; padding: 1px 5px; border-radius: 3px;
  font-size: .82rem; color: #a0b4e0; }
.stats-row { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 10px; }
.stat { font-size: .78rem; padding: 3px 9px; border-radius: 12px; font-weight: 600; }
.stat.in-fw   { background: #1a3a5e; color: #7ab4e8; }
.stat.ready   { background: #1a3a2e; color: #7ae8b4; }
.stat.possible{ background: #2a2a1a; color: #d8c870; }
.best-for { font-size: .82rem; color: #6a7490; }

/* Framework badges */
.fw-badge { display: inline-block; font-size: .75rem; font-weight: 700;
  padding: 2px 8px; border-radius: 4px; letter-spacing: .04em; }
.fw-badge.lm        { background: #1a2a5e; color: #7ab4ff; }
.fw-badge.inspect   { background: #3a1a5e; color: #c87aff; }
.fw-badge.lighteval { background: #1a3a5e; color: #7ae0ff; }
.fw-badge.helm      { background: #2a1a3e; color: #ff9aef; }
.fw-badge.oaievals  { background: #1a3a2a; color: #7affc8; }

/* Tab guide */
.tab-guide { background: #1a1a2e; border: 1px solid #2a2a4a; border-radius: 8px;
  padding: 20px 24px; }
.tab-guide h3 { color: #7888b8; font-size: .95rem; text-transform: uppercase;
  letter-spacing: .08em; margin-bottom: 14px; }
.tab-guide dl { display: grid; grid-template-columns: auto 1fr; gap: 6px 18px;
  font-size: .875rem; }
.tab-guide dt { color: #a0b4e0; font-weight: 600; white-space: nowrap; align-self: start; }
.tab-guide dd { color: #8892aa; line-height: 1.5; }
"""

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def read_and_encode(path: Path) -> str:
    """Read HTML file and HTML-escape it for use as an srcdoc attribute value."""
    text = path.read_text(encoding="utf-8")
    return html.escape(text, quote=True)


def build_dashboard() -> str:
    print("Reading source files…")
    tab1_srcdoc = read_and_encode(SOURCE_FILES["tab1"])
    print(f"  TABLE 1:         {len(tab1_srcdoc):,} chars")
    tab2_srcdoc = read_and_encode(SOURCE_FILES["tab2"])
    print(f"  TABLE 2:         {len(tab2_srcdoc):,} chars")
    tab3_srcdoc = read_and_encode(SOURCE_FILES["tab3"])
    print(f"  TABLE 2+Ethics:  {len(tab3_srcdoc):,} chars")

    dashboard = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CEI Eval Framework Dashboard</title>
<style>
{OVERVIEW_CSS}
</style>
</head>
<body>

<div id="header">
  <h1>CEI Eval Framework Dashboard</h1>
  <p>AI evaluation framework coverage · 2,043 vault papers · 5 frameworks</p>
</div>

<div id="tabbar">
  <button class="tab-btn active" onclick="switchTab('overview')">Overview</button>
  <button class="tab-btn" onclick="switchTab('tab1')">TABLE 1 — Already Included</button>
  <button class="tab-btn" onclick="switchTab('tab2')">TABLE 2 — Implementability</button>
  <button class="tab-btn" onclick="switchTab('tab3')">TABLE 2 + Ethics</button>
</div>

<div id="content-area">

  <div id="panel-overview" class="tab-panel active">
    {OVERVIEW_HTML}
  </div>

  <div id="panel-tab1" class="tab-panel">
    <iframe srcdoc="{tab1_srcdoc}" title="TABLE 1 — Already Included"></iframe>
  </div>

  <div id="panel-tab2" class="tab-panel">
    <iframe srcdoc="{tab2_srcdoc}" title="TABLE 2 — Implementability"></iframe>
  </div>

  <div id="panel-tab3" class="tab-panel">
    <iframe srcdoc="{tab3_srcdoc}" title="TABLE 2 + Ethics"></iframe>
  </div>

</div>

<script>
function switchTab(name) {{
  // Deactivate all panels and buttons
  document.querySelectorAll('.tab-panel').forEach(function(p) {{
    p.classList.remove('active');
  }});
  document.querySelectorAll('.tab-btn').forEach(function(b) {{
    b.classList.remove('active');
  }});

  // Activate selected
  var panelId = name === 'overview' ? 'panel-overview' : 'panel-' + name;
  var panel = document.getElementById(panelId);
  if (panel) panel.classList.add('active');

  // Activate the clicked button
  var buttons = document.querySelectorAll('.tab-btn');
  var tabIndex = {{'overview': 0, 'tab1': 1, 'tab2': 2, 'tab3': 3}};
  var idx = tabIndex[name];
  if (buttons[idx]) buttons[idx].classList.add('active');
}}
</script>

</body>
</html>
"""
    return dashboard


def main():
    dashboard_html = build_dashboard()
    OUTPUT.write_text(dashboard_html, encoding="utf-8")
    size_kb = OUTPUT.stat().st_size / 1024
    print(f"\nGenerated {OUTPUT.relative_to(BASE.parent)} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    main()
