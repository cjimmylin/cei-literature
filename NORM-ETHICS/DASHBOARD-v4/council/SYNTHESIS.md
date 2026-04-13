# Dashboard v4 Council Synthesis

**Date:** 2026-04-13 | **Phase B** | **12 expert plans reviewed**

---

## Converged Findings

### Universal agreement (8+ of 12 experts)
1. **Abstract/"validates" language** on tabs 1, 8, 10 must be replaced. "Confirms," "validated," "confirms" → "suggests," "explored," "indicates."
2. **Tab 0 glossary is essential** — 20 terms identified (Expert 1), `<dl>` format with colored badges (Expert 11).
3. **Cross-Vendor tab needs its own banner** — users arrive via direct links and bypass Tab 0.
4. **Inline `[simulated]` tags** on chart titles for tabs 8-10 (Experts 2, 5, 6, 9, 10).

### Strong agreement (5-7 experts)
5. **Theme toggle must be built from scratch** — v2 has zero infrastructure, ~30 hardcoded hex values.
6. **CSS contrast failures** — `--text-muted` (3.6:1) and `--text-secondary` (4.3:1 marginal) both fail AA.
7. **Mobile font floor** — 6 element classes below 12px.
8. **B/M/I blocks should collapse** — `<details>` with Interpretation visible by default (Expert 2).
9. **Provenance badges** on trial data: `[Empirical]` for T1-T5, `[Simulated]` for T6-T15 (Expert 5).

---

## Tab 0 Content Order (locked)

Per Experts 2, 3, 4, 10, 11 — ordered by declining urgency:

1. **Preliminary data banner** (CONTRACT §8, with Expert 9 wording fixes: remove "appropriate," change "in progress" → "planned but not yet complete")
2. **One-paragraph orientation** (~60 words: what is NormEval, 54 benchmarks, 3 axes)
3. **"Why show simulated data?" rationale** (~100 words: Anthropic data is empirical, non-Anthropic are falsifiable hypotheses, replication planned) — per Expert 10 Q1
4. **Framework explainer** (Expert 3's 300-word draft: ND, PE, CI, dual gates, composite formula, weight rationale with 94% stability mention)
5. **Five Ethical Traditions glossary** (Expert 4's 260-word draft with Western qualifier)
6. **Reading path** (~40 words: "Start with Overview → All Papers → Tabs 3-7 → Tabs 8-10 for cross-vendor")
7. **Technical glossary** (20 terms from Expert 1, as `<dl>` with colored badges per Expert 11)
8. **Color legend** (axis colors + tradition colors as swatch strip)

---

## Per-Tab Edit List

### Tab 1 (Overview)
- **REMOVE** "All claims were validated across 9 models from 3 vendors" or add `[includes simulated data]`
- **REMOVE** "Cross-vendor replication...confirms these findings" → "Cross-vendor analysis suggests..."
- Add B/M/I blocks (use Expert 6 drafts for claims Method/Interpretation)
- Add `(landscape-level, N=54)` parenthetical to each claim p-value
- Collapse Expert Analysis block by default

### Tab 2 (All Papers)
- Add B/M/I blocks; Method: add composite formula one-liner (Expert 1)
- Expand "A6" column header to "Philosophical Grounding"

### Tab 3 (Feature Matrix)
- Add B/M/I blocks; Method: "Each cell is 0-5 rating normalized to 0-100" (Expert 1)
- Allow Method up to 200 words (Expert 11)

### Tab 4 (Tradition Coverage)
- Add B/M/I blocks (use Expert 1's draft for all 3)
- Add tradition color legend inline (Expert 4: missing `.tradition-dot.active-care`)

### Tab 5 (Composite Scoring)
- Add formal B/M/I wrappers around existing equation/rationale boxes
- Allow Method up to 200 words

### Tab 6 (Trials)
- Add B/M/I blocks (use Expert 5's draft)
- **Add provenance badge column**: "Empirical" for T1-T5, "Simulated [preliminary]" for T6-T15
- **Add amber callout** at tab top (Expert 5): T1-T5 direct API vs. T6-T15 elicitation
- Define "discriminative power" inline

### Tab 7 (Data Availability)
- Add B/M/I blocks (minimal; Expert 1: add host/license verification note)

### Tab 8 (Cross-Model)
- Add B/M/I blocks (use Expert 5's draft)
- **Flag** line 620 "confirming" → "suggesting" + `[simulated]` tag
- State 70/52 item concentration in Method block
- Note single-administration IH point estimates with no test-retest

### Tab 9 (Gaps)
- Add B/M/I blocks; define "vault mining" (Expert 1)
- Expand Tronto framework reference

### Tab 10 (Cross-Vendor)
- **FIRST CHILD: compact preliminary banner** (Expert 9's 63-word draft)
- Add B/M/I blocks (use Expert 1's draft)
- **Replace ALL cross-vendor "Key conclusion" and "confirms" language** (Expert 9: 7 specific instances identified)
- `[simulated]` inline tag on every chart title and KPI value
- Add header above F1-F7 findings: "Findings below are based on in-context elicitation, not direct API testing"
- Remove "10^-103" Gemini statistical inference or add callout that this is an elicitation artifact

---

## CSS Changes (locked)

1. `--text-muted`: `#8a8ea8` → `#9ea2bc` (~4.6:1)
2. `--text-secondary`: `#9498b3` → `#a8acc4` (~5.2:1)
3. Add `[data-theme="light"]` CSS variable block (all `--bg-*`, `--text-*`, `--border-*` overrides)
4. Add `:focus-visible` with 2px solid outline on all interactive elements
5. Add `.preliminary-banner` styles (yellow bg, dark text, role="alert")
6. Add `@media (prefers-reduced-motion: reduce)` block
7. Add `@media (max-width: 480px)` breakpoint
8. Floor all text at 0.75rem minimum
9. Add `.tradition-dot.active-care` color class
10. Add `.simulated-tag` inline indicator style
11. Add `.provenance-badge` styles (green for empirical, amber for simulated)

---

## JS Changes (locked)

1. **Theme toggle**: `getThemeColors()` helper reading CSS computed styles
2. **Dispose/re-init cycle** on toggle: iterate chartInstances, dispose all, reset `rendered` flags, re-render active tab
3. **Version counter pattern** for lazy re-render on inactive tabs
4. **localStorage try/catch** wrappers for get and set
5. **Validate `data-theme`** on load: exactly `"dark"` or `"light"`, else default dark
6. **Remove all `window.DATA_*` references** — use bare names or `typeof` checks
7. **Add ECharts `aria.enabled = true`** in chart options
8. **Add `aria-label` summaries** to chart wrapper divs
9. **Add `aria-selected`/`aria-controls`** to tab links
10. **Add `aria-sort`** to sortable table headers

---

## Deferred to Future Sessions

- **Anthropic-only default toggle** (Expert 10 Q3) — high impact but high complexity; would require refactoring all chart rendering to support dual data modes. Noted for v5.
- **Calibration/validity subsection** (Expert 10 Q4) — no ground-truth data exists yet. Adding "we have no calibration data" is honest but adds no information. Deferred until real comparison data lands.
- **Hidden data tables for screen readers** (Expert 7 V16) — important but massive effort (one table per chart × 11 tabs). ECharts `aria.enabled` is the partial fix for now.
- **Print mode figure numbering** (Expert 2) — prefix with tab number. Low priority.

---

## Execution Approach

Given the scale of changes (~30 CSS fixes, ~30 JS changes, Tab 0 new content, B/M/I blocks on 10 tabs, simulated flags throughout), the execution strategy is:

1. **Copy v2 → v4** (`cp -r DASHBOARD-v2/* DASHBOARD-v4/`)
2. **Edit style.css** — CSS variable fixes, light theme, new classes
3. **Edit app.js** — theme toggle, localStorage, ARIA attributes
4. **Edit charts.js** — `getThemeColors()` helper, replace hardcoded hex
5. **Edit index.html** — Tab 0 insertion, B/M/I blocks on all tabs, banner on Tab 10, [simulated] tags, language fixes
6. **Create NOTICE** — third-party attributions
7. **Populate deploy/** — allowlisted files only
8. **Playwright verification**

All edits happen in the main session per plan (no sub-agent dispatch for execution).
