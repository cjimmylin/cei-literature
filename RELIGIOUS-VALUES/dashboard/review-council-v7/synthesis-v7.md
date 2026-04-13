# Dashboard v7 — Critic Synthesis & Resolution Document

**Date:** 2026-04-13
**Input:** critique-plain-reader.md (9 CRITICAL, 15 MAJOR, 6 MINOR), critique-overclaim.md (2 CRITICAL, 9 MAJOR, 6 MINOR), critique-contract-drift.md (5 CRITICAL, 8 MAJOR, 6 MINOR)
**Output:** Binding resolutions for v7 generator implementation

---

## Resolution Methodology

Three critic reports were cross-referenced. Where critics flagged the same issue under different criteria, a single resolution addresses all. Resolutions are numbered R-01 through R-28 and grouped by severity.

---

## CRITICAL Resolutions

### R-01: Data key mismatches — use JSON keys, not contract keys
**Source:** Contract-drift CRITICAL-01, CRITICAL-02
**Issue:** Contract doc says `rubric_v_min`/`rubric_v_max` but JSON uses `mean_rubric_knowledge`, `mean_rubric_reasoning`, `mean_rubric_values`, etc.
**Resolution:** The canonical data source is `claims_canonical.json`. The generator MUST use the actual JSON keys: `mean_rubric_knowledge`, `mean_rubric_reasoning`, `mean_rubric_values`. The contract doc is informational only; JSON wins.

### R-02: bias_score_range is an array, not a string
**Source:** Contract-drift CRITICAL-03
**Issue:** JSON has `[0.5667, 1.0]`, contract says `"0.567-1.0"`.
**Resolution:** Generator indexes with `[0]`/`[1]`. No `.split('-')`. The array form is canonical.

### R-03: Keep v6 DOM tab order — add reading path badges instead
**Source:** Contract-drift CRITICAL-07/CRITICAL-11, Plain-reader 5.1
**Issue:** UX plan and narrative plan propose different tab reorders; both conflict with the frozen skeleton.
**Resolution:** Keep v6 DOM order as source of truth: Overview | Sensitivity | Tradition Void | Values Relevance | Claims | Simulated Scorer Study. Do NOT reorder tabs. Instead, add small numbered circle badges ("Suggested Reading Path") on each tab label indicating the recommended reading order: 1-Overview, 2-Tradition Void, 3-Ranking, 4-Sensitivity, 5-Claims, 6-Simulated Scorer.

### R-04: C4 null p_value handling
**Source:** Contract-drift MAJOR-17, Overclaim Criterion 2
**Issue:** C4's primary test is logistic regression with `"p_value": null`. Computing `-log10(null)` produces NaN.
**Resolution:** For the p-value strip chart, use `-log10(p_value)` only when p_value is not null. C4 gets a diamond marker at y=1.0 (a neutral position) with tooltip: "Not applicable -- logistic regression reports pseudo R-squared = 0.068 instead of a claim-level p-value."

### R-05: Replace ALL "A3" with "values relevance score (0-100)"
**Source:** Plain-reader 2.4 (CRITICAL)
**Issue:** "A3" is an internal axis identifier unexplained to general readers.
**Resolution:** Every rendered instance of "A3" in chart labels, annotations, claim cards, and alt text becomes "values relevance score (0-100)" or "values relevance" (short form). Chart axis labels read "Values Relevance Score (0 = factual recall only, 100 = full values reasoning)."

### R-06: Add C8 hero stat card to Tab 1 Overview
**Source:** Plain-reader 3.1/3.2 (CRITICAL), Overclaim Criterion 3
**Issue:** C8 (values relevance failure) is buried in Tab 5; first-time readers who stop at Tab 1 never see it.
**Resolution:** Add a prominent stat card to Tab 1's first viewport: "Mean values relevance: 30/100 -- most benchmarks do not test religious values (d=-1.23, p<0.001). Assessed on the top-16 tier-eligible benchmarks. Values relevance scoring was performed by Claude Opus (see Caveat 2: Scorer Bias)." This is not an ECharts chart; it is a `.card-stat` HTML element with green accent.

### R-07: Add hero subtitle — "meta-evaluation" framing
**Source:** Plain-reader 1.9b (CRITICAL)
**Issue:** Readers may think this is a benchmark-creation paper rather than a meta-evaluation.
**Resolution:** Add subtitle under page title: "A study of whether religious-values benchmarks actually measure what they claim." This appears as a persistent subtitle in the header.

### R-08: Add visible glossary panel on Tab 5
**Source:** Plain-reader 4.1 (CRITICAL)
**Issue:** Tab 5 can have 9+ unexplained abbreviations simultaneously.
**Resolution:** Add an expandable `<details>` glossary panel on Tab 5 (Claims) defining: K = Knowledge, R = Reasoning, V = Values; T1 = 65-item construct validity battery; T2 = 30-item Arabic MCQ on Islamic inheritance law (fara'id); CI = Confidence Interval (the range within which we are 95% confident the true value falls); pp = percentage points; WEIRD = Western, Educated, Industrialized, Rich, Democratic. The glossary is expanded by default on first visit.

### R-09: Resolve not_significant color — blue, not grey
**Source:** Plain-reader 5.3 (CRITICAL), Plan-statistics.md Section 2
**Issue:** Statistics plan says blue (#0072B2); dataviz plan says grey (#8b949e).
**Resolution:** Blue wins. Use #0072B2 (light theme) / #58A6FF (dark theme) for `not_significant` verdicts. Grey is reserved for "missing data" or "not applicable." The three verdict colors are:
- Supported: #009E73 (Okabe-Ito green)
- Revised: #E69F00 (Okabe-Ito amber)
- Not significant: #0072B2 light / #58A6FF dark (Okabe-Ito blue)

### R-10: "CI" disambiguation
**Source:** Plain-reader 4.2 (MAJOR)
**Issue:** "CI" means both Confidence Interval and Citation Impact in the same dashboard.
**Resolution:** Use "CI" exclusively for Confidence Interval. Rename the scoring axis from "Citation Impact (CI)" to "citation impact" (spelled out, never abbreviated). The composite formula becomes: "Composite = 0.50 x RD + 0.35 x PE + 0.15 x citation impact."

### R-11: Static claims index table on Tab 5
**Source:** Plain-reader 2.1 (CRITICAL)
**Issue:** Claim titles are tooltip-only in the p-value strip chart.
**Resolution:** Add a static HTML table above the p-value strip chart on Tab 5 with columns: Claim # | Title | Verdict. All 8 claims visible without hover. C8 appears first in the table.

### R-12: K/R/V legend requirement
**Source:** Plain-reader 1.1 (CRITICAL)
**Issue:** K/R/V labels appear as bare single letters on charts without a visible legend.
**Resolution:** Every chart whose axis or legend uses K, R, or V as standalone letters MUST display a visible on-chart legend: "K = Knowledge, R = Reasoning, V = Values." This is implemented as a `graphic` text element in ECharts, not tooltip-only.

---

## MAJOR Resolutions

### R-13: C8 must show CAV-2 (scorer bias) badge
**Source:** Overclaim Criterion 3 and 4
**Issue:** C8 convergence box and forest plot lack scorer bias caveat.
**Resolution:** The C8 forest plot (N1) and the three-way convergence callout both carry a CAV-2 badge: "Values relevance scoring was performed by Claude Opus (same-vendor as the Claude trial models -- see Caveat 2). The large effect size (d=-1.23) and three-test convergence mitigate but do not eliminate this concern."

### R-14: Tab 6 opening line must start with simulation disclosure
**Source:** Overclaim Criterion 5 (CRITICAL)
**Issue:** Tab 6 Background opens with "9 AI models from 3 vendor families" without simulation qualifier.
**Resolution:** Tab 6 Background opens with: "This tab presents results from a simulated scorer study. Only the Anthropic Claude family used real API calls; OpenAI and Gemini conditions were simulated by Claude models roleplaying those vendor behaviors." This precedes any discussion of findings.

### R-15: C4 and C6 hedging language
**Source:** Overclaim Criterion 2 (MAJOR)
**Issue:** Narrative plan states C4 mechanism affirmatively and C6 reversal as confirmed, contradicting statistics plan.
**Resolution:** C4 annotation includes: "...though neither individual predictor reaches statistical significance (p > 0.09), and the finding is classified as revised, not confirmed." C6 annotation includes: "...though this direction reversal does not reach the conventional significance threshold (p = 0.09) and should be treated as a strong trend rather than a confirmed effect."

### R-16: Alt text uses "Claude-roleplaying-X-scorer" labels
**Source:** Overclaim Criterion 1 (MINOR)
**Issue:** Alt text has bare "GPT-Codex" and "OpenAI"/"Gemini" without roleplay framing.
**Resolution:** All pre-computed alt text uses format: "(Simulated by Claude) GPT-Codex: 100%" and "Simulated (Claude-roleplaying): Compressed Accuracy (OpenAI-scorer condition)." No bare vendor names in any `aria-label`.

### R-17: Caveat card IDs match skeleton
**Source:** Contract-drift MAJOR-08
**Issue:** Transparency plan says `id="cav-1"` but skeleton uses `id="caveat-cav1"`.
**Resolution:** Use `id="caveat-cav1"`, `id="caveat-cav2"`, `id="caveat-cav3"` matching the skeleton. All anchor links target these IDs.

### R-18: Single canonical vendor color palette
**Source:** Contract-drift MAJOR-14
**Issue:** Three different vendor color palettes across three plans.
**Resolution:** Use the vendor-framing plan's palette as canonical:
- Claude-as-Claude: #5b8ff9 (blue)
- Sim: OpenAI-scorer: #61d9aa (teal)
- Sim: Gemini-scorer: #f6bd16 (amber)
These replace the v6 VENDOR_COLORS in the generator.

### R-19: Skip link targets
**Source:** Contract-drift MAJOR-09
**Issue:** Skip link targets `#main-content` which does not exist.
**Resolution:** Skip link targets `#mainTabs` (already exists in skeleton). Add `<a href="#mainTabs" class="sr-only skip-link">Skip to main content</a>` as the first element in `<body>`.

### R-20: T1 and T2 glossing
**Source:** Plain-reader 1.2, 1.3 (MAJOR)
**Issue:** T1 unglossed in most plans; fara'id missing from chart titles.
**Resolution:** T1 is glossed on first use as "T1 (65-item construct validity battery: Knowledge, Reasoning, Values, and Bias items)." T2 chart title reads: "T2 (fara'id -- Islamic Inheritance Law) Arabic MCQ Accuracy." fara'id uses ASCII straight apostrophe.

### R-21: WEIRD glossing
**Source:** Plain-reader 1.8 (MAJOR)
**Issue:** WEIRD used without expansion in claims tab.
**Resolution:** First use of WEIRD in any claim card or annotation text expands to "WEIRD (Western, Educated, Industrialized, Rich, Democratic)."

### R-22: Bonferroni glossing on strip chart
**Source:** Plain-reader 1.7 (MAJOR)
**Issue:** Bonferroni threshold line appears without explanation.
**Resolution:** The p-value strip chart includes visible annotation: "Dashed line: p < 0.05 (conventional threshold). Dotted line: p < 0.006 (Bonferroni correction for testing 8 claims simultaneously -- reduces false-alarm risk)."

### R-23: "AI systems" generalization bounded
**Source:** Overclaim Criterion 6 (MAJOR)
**Issue:** Narrative arc says "AI systems show fundamentally different behavioral modes" -- overgeneralization.
**Resolution:** Replace with: "Model configurations in this study show three distinct behavioral modes -- though only Claude family results derive from real API calls; OpenAI and Gemini patterns are Claude-simulated and require replication."

### R-24: n=16 scope for C8
**Source:** Overclaim Criterion 6 (MAJOR)
**Issue:** C8 values relevance failure applies to 16 benchmarks, not all 47 gate-passers.
**Resolution:** All C8 references include: "assessed on the top-16 tier-eligible benchmarks." The hero stat card and forest plot annotation both carry this qualifier.

### R-25: Void-grid tradition names as visible text
**Source:** Plain-reader 5.5 (MAJOR)
**Issue:** Tradition names may be tooltip-only in void grid.
**Resolution:** The eight VOID tradition names (Judaism, Jainism, Taoism, Shinto, Ubuntu Philosophy, Indigenous Spirituality, Baha'i, Zoroastrianism) appear as visible text labels, not tooltip-only.

### R-26: Mobile caveat accordion starts expanded
**Source:** Plain-reader 6.3 (MAJOR)
**Issue:** Mobile caveat ribbon starts collapsed, hiding critical disclosure.
**Resolution:** Caveat ribbon starts expanded on first load regardless of viewport. Collapsed state persists via localStorage only after user explicitly collapses it.

---

## MINOR Resolutions

### R-27: "pp" spelled out
**Source:** Plain-reader 1.10
**Resolution:** Replace "pp" with "percentage-point" in all chart titles and annotations. "93.3 percentage-point span."

### R-28: ASCII straight apostrophes
**Source:** Plain-reader 5.4
**Resolution:** All apostrophes in fara'id, shari'a, and similar terms use straight ASCII apostrophe (U+0027). Generator enforces this in all string constants.

---

## Implementation Priority

**Blocking (must be in generator before first run):**
1. R-01, R-02 (data key fixes -- generator will crash without these)
2. R-04 (C4 null p-value -- generator will produce NaN without this)
3. R-03 (tab order preserved)
4. R-09 (verdict colors)
5. R-18 (vendor colors)

**Required for cold-reader gate (must be in output HTML):**
6. R-05 (A3 -> values relevance)
7. R-06 (C8 hero card)
8. R-07 (meta-evaluation subtitle)
9. R-08 (glossary panel)
10. R-11 (claims index table)
11. R-12 (K/R/V legend)
12. R-14 (Tab 6 simulation disclosure)

**Required for overclaim compliance:**
13. R-13 (CAV-2 on C8)
14. R-15 (C4/C6 hedging)
15. R-16 (alt text labels)
16. R-23 (bounded generalization)
17. R-24 (n=16 scope)

**Polish:**
18. All remaining MAJOR and MINOR resolutions

---

*Synthesis authored: 2026-04-13. All resolutions are binding for the v7 generator implementation.*
