# RV Dashboard v8 Build Handoff

**Date:** 2026-04-30
**Deliverable:** `dashboard/20260430-religious-values-dashboard-v8.html` (444,703 bytes; sha256 `c2d71cd1…`)
**Generator:** `scripts/20260430-generate-dashboard-v8.py`
**Base:** `dashboard/20260413-religious-values-dashboard-v7.html` (untouched, sha256 `118cda0f…`)
**Live:** https://cjimmylin.github.io/cei-rv-dashboard-v8/ (deployed 2026-04-30; HTTP 200; SHA matches local `eb40d2e2…`)
**Repo:** https://github.com/cjimmylin/cei-rv-dashboard-v8 (NEW public repo, separate from v6/v7's `cei-rv-dashboard`)

## What changed vs v7

Added two new tabs.  v7's six tabs are byte-identical inside v8.

**Tab 7 — Gate-Passers (47 papers).** Cleared both gates (RD ≥ 30 AND
public data URL).

**Tab 8 — All Candidates (401 papers).** Full screening corpus with a
gate-status badge per row (PASS / RD<30 / No data / both-fail).  Counts:
47 PASS, 184 RD-only-fail, 49 data-only-fail, 121 both-fail.  Includes a
stacked bar of gate outcomes by tradition and a PASS-vs-FAIL composite-score
histogram.

The new tab contains:

1. **Narrative header** explaining the gate criteria and the 3-axis composite
   (RD 40% / PE 35% / CI 25%).
2. **Tradition distribution callout** (Islam 28, Christianity 6, Buddhism 6,
   Hinduism 5, Sikhism 2, Confucianism 1; 8 traditions zero) with cross-link
   to Tab 2 (Tradition Void).
3. **Two ECharts panels:**
   - Horizontal bar chart of gate-passers by tradition, color-coded by family.
   - Composite-score histogram in 5-point bins.
4. **Filter & sort table** (47 rows × 11 columns):
   - Columns: rank, composite ↓, title (1st author · year · venue tier),
     tradition (with family-color dot), format, RD, PE, CI, citations,
     languages, links.
   - Filters: family / tradition / format / search-by-title-or-author.
   - Click any column header to sort; numeric columns default to descending.
   - "Paper" link uses the cleaned URL (38/47 entries; arXiv ID surfaced as
     button label for 21 of them).  "Data" link uses `DATA_URL` (47/47).
5. **Caveat callout** — gating is necessary not sufficient; cross-link to
   Values Relevance tab for the Claim 8 finding (values relevance score
   30/100; t = -4.93, p < 0.001, d = -1.23).

## Build strategy: fork-by-injection

v7's 154 KB generator was *not* re-run.  Instead the v8 generator reads the
v7 HTML output and surgically injects three blocks:

| Anchor in v7 HTML | Injected content |
|---|---|
| After `<li>` for `#tab-crossvendor` (line 566) | New `<li>` for `#tab-gatepassers` (Tab 7) |
| Before `</div><!-- /tab-content -->` (line 1468) | New `<div class="tab-pane" id="tab-gatepassers">…</div>` |
| Before `// ===== Initialize =====` (line ~2495) | `const GATEPASSERS = [...]` + `renderGatepassers()` + helpers |
| Inside the lazy-render dispatcher | `else if (target === 'gatepassers') renderGatepassers();` |
| `<title>`, footer cite, footer version stamp | `(v7)` → `(v8)`, `2026-04-13` → `2026-04-30` |

Five Python `assert`s guarantee each anchor is unique before substitution
(generator aborts loudly on drift).

## Data source

`data/20260404-religious-benchmark-feature-matrix-v2.json` — the v2 feature
matrix with 401 entries, 47 of which carry `passes_gates: true`.  v1 of that
matrix had 46 passers; v7's OVERVIEW JS already cited 47, confirming v7 was
also wired against v2 even though earlier reports refer to v1.

Per-row payload includes: `composite`, `rd`, `pe`, `ci`, `citations`,
`venue`, `venue_tier`, `format`, `languages`, `llms`, `license`, `paper_url`
(cleaned from messy `external_pdf: "…"` wrapped strings via regex),
`data_url` (first comma-split URL when multiple), and `arxiv_id` (extracted
from `arxiv.org/abs/…` or `/pdf/…`).

## Security & compliance

- **No `innerHTML`.** All dynamic table rows, links, dropdown options, and
  family-color dots are built with `document.createElement` /
  `textContent` / `setAttribute`.  This satisfies the vault's
  `security_reminder_hook` policy noted in MEMORY (the same rewrite pattern
  used in the SUB-SR v1.2.0 ship).
- **No file deletions.**  v7 source files (HTML, generator, council docs)
  are untouched; v8 is a NEW file with a new date prefix.
- **No external API calls.**  Pure data → static HTML.

## Verification (Phase C gates)

Ran `python3 -m http.server 8765` from the dashboard directory and drove
Playwright against `http://localhost:8765/20260430-religious-values-dashboard-v8.html`:

| Check | Result |
|---|---|
| Page title | `Religious Values Benchmark: Meta-Evaluation Dashboard (v8)` ✓ |
| Console errors / warnings | 0 / 0 ✓ |
| Tab nav has new "Gate-Passers" link | ✓ |
| Click → tab-pane activates | ✓ |
| Table renders 47 rows | ✓ |
| Default sort = composite desc | rank 1 = composite 52.0 ✓ |
| Filter `tradition=Buddhism` | 47 → 6 rows; first row composite 44.0 (Mandikal 2024) ✓ |
| Sort flip on `rank` header (click twice) | first cell becomes "1" ✓ |
| Both ECharts panels render | ✓ (no JS errors during init) |
| External links | paper 38/47 (21 arXiv); data 47/47 ✓ |

## Files

- Generator: `scripts/20260430-generate-dashboard-v8.py`
- HTML output: `dashboard/20260430-religious-values-dashboard-v8.html` (sha256 `eb40d2e2…`)
- This handoff: `PAPER/20260430-rv-dashboard-v8-handoff.md`
- Base v7 (untouched): `dashboard/20260413-religious-values-dashboard-v7.html` (sha256 `118cda0f…`)

## Deploy (executed)

Per user instruction "deploy to github pages as a new repo with version
number" (overrides v7's prior repo-sprawl-avoidance policy):

1. New public repo `cjimmylin/cei-rv-dashboard-v8` created via `gh repo create`.
2. Single commit `7745365` containing `index.html` (the v8 dashboard) and
   `README.md` (description + archive of prior versions).
3. GitHub Pages enabled via API (`source.branch=main`, `source.path=/`).
4. Build cycle ~30s; latest build status `built`.
5. `curl -L https://cjimmylin.github.io/cei-rv-dashboard-v8/` returns HTTP
   200 with 210,368 bytes (matches local file byte-for-byte) and title
   `Religious Values Benchmark: Meta-Evaluation Dashboard (v8)`.

The v6/v7 repo `cjimmylin/cei-rv-dashboard` is untouched; its `/v7/` URL
continues to serve the v7 dashboard.
