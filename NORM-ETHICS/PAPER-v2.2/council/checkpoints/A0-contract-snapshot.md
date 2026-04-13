# Dashboard v4 — Implementation Contract

**Purpose:** Pin all shared conventions BEFORE parallel agent dispatch.
**Date:** 2026-04-13 | **Version:** v4 (NormEval v2.2-preliminary)
**Rationale:** Per `feedback_parallel_agent_dashboard_contract.md`, parallel dashboard agents diverge on class names, script loading, and toggle types when not pinned upfront.

---

## 1. Architecture: Fat Data, Thin Client

- Python generator (`generate_dashboard_v4.py`) pre-computes ALL analytics → emits `data.js` as JS constants
- Browser does ZERO computation — JS only renders ECharts charts from pre-computed data
- No runtime API calls, no server-side code

## 2. Script Load Order (classic `<script>`, NOT ES modules)

```html
<script src="data.js"></script>
<script src="data_cross_vendor.js"></script>
<script src="charts.js"></script>
<script src="app.js"></script>
```

No `type="module"`, no dynamic imports. All constants attach to `window` scope implicitly via `const` at top-level in classic scripts. Access via `typeof DATA !== 'undefined'` checks (NOT `window.DATA`).

## 3. CSS Class Names (canonical — do not rename)

| Class | Purpose |
|-------|---------|
| `.tab-explainer` | Container for Background/Method/Interpretation text blocks below tab header |
| `.panel-background` | Background text block (what this metric measures and why it matters) |
| `.panel-method` | Method text block (how the data was collected and scored) |
| `.panel-interpretation` | Interpretation text block (what the chart shows and what it means) |
| `.chart-container` | ECharts chart wrapper (has `min-height: 400px`) |
| `.echarts-box-sm` | Small chart variant (300px) |
| `.echarts-box-lg` | Large chart variant (600px) |
| `.kpi-card` | Key Performance Indicator card in overview |
| `.preliminary-banner` | Yellow warning banner for simulated-data disclosure |
| `.expert-analysis` | Expert perspective panel with left border accent |
| `.skip-link` | Accessibility skip-to-content link |

## 4. Tab Structure (11 tabs)

| Tab # | ID | Label | New in v4? |
|-------|----|-------|-----------|
| 0 | `tab-guide` | How to Read This Dashboard | **YES** |
| 1 | `tab-overview` | Overview | No (was tab 1 in v2) |
| 2 | `tab-papers` | All Papers | No |
| 3 | `tab-features` | Feature Matrix | No |
| 4 | `tab-traditions` | Tradition Coverage | No |
| 5 | `tab-composite` | Composite Scoring | No |
| 6 | `tab-trials` | Trials | No |
| 7 | `tab-data` | Data Availability | No |
| 8 | `tab-crossmodel` | Cross-Model | No |
| 9 | `tab-gaps` | Gaps | No |
| 10 | `tab-crossvendor` | Cross-Vendor | No |

## 5. Theme Toggle

- CSS custom properties on `<html data-theme="dark|light">`
- Default: **dark** (no `data-theme` attribute = dark via CSS `:root` defaults)
- Never set `data-theme="light"` on initial load — CSS `:root` dark theme loads first, JS handles persistence
- localStorage key: `normeval-theme`
- On load: read `localStorage.getItem('normeval-theme')`. If value is exactly `"light"`, set `data-theme="light"`. Otherwise (null, `"dark"`, `"undefined"`, anything else): use dark (remove `data-theme` attr or set to `"dark"`)
- ECharts re-render on toggle via version counter pattern (see memory `20260405h-echarts-theme-version-counter.md`)

## 6. CDN Dependencies

| Library | Version | Source | SRI Required |
|---------|---------|--------|-------------|
| Bootstrap CSS | 5.3.3 | jsDelivr | YES — verify hash in browser per `feedback_bootstrap_sri_hash_mismatch.md` |
| ECharts | 5.4.3 | jsDelivr | YES |
| Google Fonts (Inter) | latest | fonts.googleapis.com | No (Google Fonts doesn't support SRI) |

## 7. Background / Method / Interpretation Text Blocks

Every chart panel MUST have three sibling `<div>` blocks inside `.tab-explainer`:

```html
<div class="tab-explainer">
  <div class="panel-background">
    <strong>Background:</strong> [80-150 words — what this metric measures and why it matters for normative ethics evaluation. No jargon or define all terms inline.]
  </div>
  <div class="panel-method">
    <strong>Method:</strong> [80-150 words — how the data was collected, scored, and visualized. Reference the 54-benchmark corpus, 26 features, specific scoring formula if relevant.]
  </div>
  <div class="panel-interpretation">
    <strong>Interpretation:</strong> [80-150 words — what the chart shows, what the key takeaways are, and what a first-time reader should notice first.]
  </div>
</div>
```

## 8. Preliminary Data Banner (Landing Tab)

```html
<div class="preliminary-banner" role="alert">
  <strong>⚠ Important Notice — Preliminary Cross-Vendor Data</strong>
  <p>The non-Anthropic results in this dashboard (GPT-5, GPT-5-mini, Gemini 2.5 Flash, Gemini 2.5 Flash-Lite, Gemini 2.5 Pro, Gemini 3.1 Pro) were generated through <em>in-context elicitation</em> by a Codex sub-agent rather than through direct API calls to OpenAI or Google endpoints. This methodology is appropriate for exploratory hypothesis generation but does not constitute empirical evaluation of those models. An external replication using non-Anthropic APIs is in progress.</p>
  <p>All cross-vendor findings should be interpreted as <em>Claude's elicited model of cross-vendor variation</em>, not as direct measurements of OpenAI or Google products.</p>
</div>
```

**Placement:** FIRST element inside `#tab-guide`, above all other content. Also repeated (compact version) at the top of `#tab-crossvendor`.

## 9. Deploy Allowlist

Files that go into `DASHBOARD-v4/deploy/` for GitHub Pages:
- `index.html`
- `data.js`
- `data_cross_vendor.js`
- `charts.js`
- `app.js`
- `style.css`
- `fonts/` directory
- `LICENSE`
- `NOTICE`
- `README.md`

**NEVER deploy:** `council/`, `CONTRACT.md`, `generate_dashboard_v4.py`, `*.log`, `screenshots/`, `test_*.py`, `*.md` (except README.md)

## 10. Immutability

- v1, v2, v3 dashboards are frozen. Do not merge v4 changes into their repos.
- Public repos `cjimmylin/cei-normeval-dashboard{,-v2,-v3}` are never modified.
- DASHBOARD-v2/ source directory is frozen per CLAUDE.md Rule 3.

## 11. Footer

```html
<footer>
  <p>NormEval v2.2-preliminary | Generated 2026-04-13 | 
     Code: <a href="https://github.com/cjimmylin/cei-literature">MIT</a> | 
     Data: <a href="https://creativecommons.org/licenses/by/4.0/">CC-BY-4.0</a> |
     <a href="CITATION.cff">Cite this work</a></p>
  <p class="text-muted">Cross-vendor results are preliminary — see "How to Read This Dashboard" tab.</p>
</footer>
```
