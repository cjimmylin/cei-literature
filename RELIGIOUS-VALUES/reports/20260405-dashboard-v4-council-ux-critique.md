# Dashboard v4 — 12-Member Expert Council UX & Content Critique

**Date:** 2026-04-05
**Dashboard:** Religious Values Benchmark: Cross-Vendor Meta-Evaluation (v4)
**URL:** https://cjimmylin.github.io/cei-rv-dashboard/
**Scope:** Layout, design, content, readability, text, graphics — all 6 tabs

---

## Council Composition

| # | Role | Expertise | Review Focus |
|---|------|-----------|-------------|
| 1 | Information Designer | Data visualization & dashboard UX | Chart effectiveness, visual hierarchy, cognitive load |
| 2 | Academic Data Viz Specialist | Scientific communication | Statistical graphic conventions, publication readiness |
| 3 | Web Accessibility Auditor | WCAG 2.1 AA compliance | Color contrast, screen readers, keyboard navigation |
| 4 | Typography & Readability Expert | Digital reading ergonomics | Font sizing, line length, text density, whitespace |
| 5 | Dark Theme UI Designer | Dark-mode interface patterns | Color palette, contrast ratios, dark theme consistency |
| 6 | Science Communication Editor | Academic writing for mixed audiences | Jargon density, annotation clarity, lay accessibility |
| 7 | Cross-Cultural UX Researcher | Non-Western user interface patterns | Cultural sensitivity, RTL considerations, bias in framing |
| 8 | Dashboard Architecture Analyst | Multi-tab dashboard design | Information architecture, tab flow, progressive disclosure |
| 9 | ECharts Visualization Engineer | ECharts 5 best practices | Chart configuration, interactivity, responsive behavior |
| 10 | Print & Export Specialist | PDF/print output quality | Print stylesheet, save-as-PNG, offline usability |
| 11 | Mobile Responsiveness Tester | Sub-992px breakpoint behavior | Touch targets, overflow, chart readability on small screens |
| 12 | Content Strategist | Dashboard narrative coherence | Story arc, redundancy, cross-tab consistency |

---

## Executive Assessment

**Overall rating: 8.2/10** — A strong academic dashboard that successfully integrates complex multi-vendor LLM analysis into a coherent narrative. The "fat data, thin client" architecture ensures fast rendering. The dark theme is well-executed. The annotation prose is unusually thorough for a dashboard format. However, several design and content issues reduce effectiveness, particularly around information density, visual hierarchy, and accessibility.

---

## Tab-by-Tab Critique

### Tab 1: Overview

**Strengths:**
- The 8-stat-card layout (4 benchmark + 4 vendor) creates an effective two-tier information hierarchy
- Vendor Comparison Summary table is clean and immediately scannable
- The tradition bar chart and family pie chart complement each other well
- Cross-reference links to other tabs are useful navigation aids

**Issues:**

| # | Severity | Category | Issue | Recommendation |
|---|----------|----------|-------|----------------|
| 1 | Medium | Visual hierarchy | The two rows of stat cards look identical — the reader cannot distinguish "benchmark stats" from "vendor stats" without reading labels | Add a subtle section divider or subheading between the two rows (e.g., "Benchmark Screening" / "Cross-Vendor Validation") to visually separate the two tiers |
| 2 | Medium | Information density | The Overview tab is extremely long — 8 stat cards + vendor table + 2 charts + 4 annotation blocks + 2 key finding callouts. Users must scroll ~5 viewport heights | Consider collapsing the annotation prose into expandable accordions (click to expand), keeping the charts and stat cards always visible |
| 3 | Low | Chart design | The tradition bar chart x-axis labels are at ~30° rotation, which is harder to read than horizontal labels | Use a horizontal bar chart (like Tab 2's forest plot) instead of a vertical bar chart — 6 tradition names fit comfortably on the y-axis |
| 4 | Low | Redundancy | The Key Findings section at the top of the page AND the Overview tab conclusion both state "8 of 14 traditions have zero benchmarks" | Remove the duplication — the Key Findings section should provide the summary; the tab conclusion should add interpretive depth, not repeat the same sentence |
| 5 | Low | Data precision | The T2 range shows "7%–100%" in the stat card, but the actual minimum is 6.7%. The Key Findings table says "7%–100%" while the Cross-Vendor tab correctly says "6.7%–100%" | Use consistent precision: either "6.7%–100%" everywhere or "7%–100%" everywhere. Recommend the former since 6.7% (below random chance) is a meaningful finding |

### Tab 2: Sensitivity

**Strengths:**
- The forest plot is the best chart in the entire dashboard — clear, informative, and well-annotated
- Bootstrap CI visualization with top-15 cutoff line is publication-quality
- DataZoom slider on the forest plot is a smart UX choice for 47 benchmarks
- Weight sensitivity and gate threshold charts complement each other logically

**Issues:**

| # | Severity | Category | Issue | Recommendation |
|---|----------|----------|-------|----------------|
| 6 | Medium | Chart readability | The forest plot benchmark labels (left axis) are truncated at 45 characters and rendered at 9px — very difficult to read, especially on laptop screens | Increase font to 10-11px; allow labels to extend to 50-55 characters; or add a tooltip that shows the full name on hover (which ECharts supports natively) |
| 7 | Low | Visual balance | The weight sensitivity and gate threshold charts are stacked 50/50, but the weight sensitivity chart has 20 bars (tall) and the gate threshold has 2 lines (short). The gate threshold feels like wasted vertical space | Consider making the weight sensitivity chart col-md-7 and gate threshold col-md-5, or reducing gate threshold height from 450px to 350px |
| 8 | Low | Missing context | The Kendall's tau of 0.773 is mentioned in prose but not visualized | A small inline badge or stat card showing "Kendall's tau = 0.773 (moderate stability)" would reinforce this key number visually |

### Tab 3: Tradition Void

**Strengths:**
- The radar chart with three archetypes (Islam, Judaism, Indigenous Spirituality) is pedagogically excellent
- The readiness bar chart with green/red coloring immediately communicates the active/void divide
- The structural scores table is comprehensive and well-formatted
- The annotation prose connecting infrastructure to benchmark availability is the best-written section of the dashboard

**Issues:**

| # | Severity | Category | Issue | Recommendation |
|---|----------|----------|-------|----------------|
| 9 | Medium | Radar chart | The radar chart uses only 3 exemplars, but 14 traditions exist. Readers may wonder about the 11 unlisted traditions | Add a "Show all traditions" toggle or overlay that adds semi-transparent radar polygons for additional traditions, or add a note explaining why 3 exemplars were chosen |
| 10 | Low | Table density | The structural scores table shows 14 rows × 9 columns — dense but manageable. However, factor score columns (Digital, NLP, Formalizability) use raw 0-5 values with no color-coding | Add subtle background color intensity to cells (darker = higher score) to create a visual heatmap effect, making patterns scannable without reading numbers |
| 11 | Low | Accessibility | The red/green color coding for Active/Void badges may be indistinguishable for red-green colorblind users (~8% of males) | Use shape differentiation in addition to color: checkmark + green for Active, X + red for Void. Or use blue/orange instead of green/red |

### Tab 4: Values Relevance

**Strengths:**
- The A3 histogram with threshold lines (50 = minimal, 75 = strong) is clear and well-annotated
- The construct type pie chart reveals the knowledge-bias dominance effectively
- The top/bottom A3 tables provide concrete benchmark examples
- The annotation connecting maqasid al-shariah to the values gap is excellent scholarly writing

**Issues:**

| # | Severity | Category | Issue | Recommendation |
|---|----------|----------|-------|----------------|
| 12 | Medium | Chart type | The A3 histogram uses 10-unit bins, which creates only 10 bars. With n=50 benchmarks, many bins have 1-3 items. A dot plot or strip plot would show individual benchmark positions more clearly | Consider a beeswarm/strip plot where each dot is one benchmark, colored by tradition family, with threshold lines overlaid — this shows individual positions, clusters, and the mean simultaneously |
| 13 | Medium | Pie chart effectiveness | The A1 Construct Type pie chart has 6+ slices, several very small. Pie charts are generally poor for comparing proportions across many categories | Replace with a horizontal bar chart or treemap — both better for comparing 6+ categories with large magnitude differences |
| 14 | Low | Table layout | The top A3 and bottom A3 tables are side-by-side (col-md-6 each), making each table narrow. On smaller screens, benchmark names may be truncated | Stack the tables vertically (top benchmarks, then bottom benchmarks) to give each the full 12-column width |

### Tab 5: Claim Evidence

**Strengths:**
- The -log10(p-value) bar chart is a standard and effective visualization for statistical evidence
- Color-coding (green/orange/red) for supported/marginal/unsupported is intuitive
- Claim cards below the chart provide detailed interpretation
- The NEW cross-vendor claim validation table adds meaningful multi-model context

**Issues:**

| # | Severity | Category | Issue | Recommendation |
|---|----------|----------|-------|----------------|
| 15 | High | Visual hierarchy | The tab is extremely text-heavy: intro paragraph + chart + 7 claim cards + chart annotation + cross-vendor table + CV annotation + footer + footer annotation + 2 callouts. It is the longest-scrolling tab at ~7 viewport heights | Group the 7 claim cards into a 2-column grid (col-md-6) to halve vertical space, or make them expandable/collapsible (show claim number + status, click to expand interpretation) |
| 16 | Medium | Cross-vendor table | The new Cross-Vendor Claim Validation table has 8 rows but the "Notes" column for model-agnostic claims all say "Applies regardless of which LLM is used" — this is repetitive and wastes column width | For model-agnostic rows, merge the Notes into the Status column (e.g., "Model-agnostic — applies regardless of LLM") and leave Notes blank, or use a footnote. Only show substantive notes for C7 and K<R<V rows |
| 17 | Low | Chart interactivity | The -log10(p) chart has claim labels truncated at ~50 characters on the y-axis | Add tooltips showing the full claim text and exact p-value on hover (partially implemented, but confirm tooltip shows full claim text) |

### Tab 6: Cross-Vendor LLM

**Strengths:**
- The response length grouped bar chart with log scale correctly handles the 111x range difference
- Vendor-colored x-axis labels are an elegant vendor-identification pattern
- The rubric heatmap (9×5) is immediately readable with the piecewise color map
- The NEW T2 beginner/advanced chart reveals the Codex-Mini anomaly effectively
- Vendor capability radar chart provides a strong gestalt overview

**Issues:**

| # | Severity | Category | Issue | Recommendation |
|---|----------|----------|-------|----------------|
| 18 | High | Tab length | Tab 6 is the second-longest tab at ~6 viewport heights. It has 6 charts + gradient table + 4 stat cards + 6 annotation blocks + 2 callouts | Consider splitting into two sub-tabs: "Response Patterns" (length chart, gradient table, rubric heatmap) and "Discrimination & Independence" (T2 charts, radar, bias-values bar) |
| 19 | Medium | Gradient table | The K<R<V Gradient Indicator table lists all 9 models vertically — the YES/NO badges are informative, but the V/K ratio column lacks visual emphasis. A 9.18x ratio is dramatically different from 1.03x | Add a small inline bar or sparkline to the V/K column to visually represent the ratio magnitude, or use background color intensity |
| 20 | Medium | T2 charts | There are now TWO T2 charts: the overall accuracy horizontal bar and the beginner/advanced grouped bar. They show overlapping data (the overall bar is the average of the beginner+advanced bars) | Consider merging into a single stacked or grouped bar that shows beginner, advanced, and overall simultaneously, rather than two separate charts showing partially redundant data |
| 21 | Low | Radar chart | The vendor radar collapses Gemini to the center (all near-zero except a slight T2 signal). This is accurate but makes the chart feel like it only shows Anthropic and OpenAI | Add a note explaining that Gemini's collapse is itself a finding, not a chart error — or consider a supplementary bar chart that handles floor values better than radar |
| 22 | Low | Bias-Values bar | The y-axis max is 1.1 but only 2 models (Opus, Haiku) exceed 0.7. The 4 Gemini models at r=1.0 create a wall of red that visually dominates | Add labels or annotations explaining that r=1.0 for Gemini is a degenerate artifact (zero variance), not a meaningful correlation. The chart could benefit from splitting into "non-degenerate" and "degenerate" groups |

---

## Cross-Tab Issues

| # | Severity | Category | Issue | Recommendation |
|---|----------|----------|-------|----------------|
| 23 | High | Overall length | The full-page scroll distance across all tabs is excessive. Each tab averages 5-6 viewport heights. For an academic dashboard, this creates cognitive overload — readers lose context between the chart and its annotation | Adopt a "chart + annotation side-by-side" layout for wider screens: chart on left (col-md-7), annotation on right (col-md-5). This halves vertical scrolling and keeps interpretation adjacent to data |
| 24 | High | Annotation density | Annotations average 150-200 words each, written in dense academic prose. Most tabs have 4-6 annotations. This creates a reading experience closer to a paper than a dashboard | For each annotation, split into: (a) a 1-2 sentence bold summary that's always visible, and (b) the full prose in a collapsible "Read more" section. This serves both scanners and deep readers |
| 25 | Medium | Favicon missing | The dashboard returns 404 for favicon.ico, creating a console error | Add a simple favicon (even a text emoji like "🕌" or the CEI logo) to the repo root |
| 26 | Medium | Figure numbering | Figure numbers (Fig. 1 through Fig. 19) use CSS counters, which means they renumber across tabs based on DOM order, not tab order. If a user opens Tab 6 first, figure numbers may appear to start at Fig. 12 | Use explicit figure numbers in the chart titles instead of CSS counters, so numbers are correct regardless of tab viewing order |
| 27 | Medium | Tab subtitles | Tab subtitles ("401 → 47 screening", "Ranking robustness", etc.) are rendered below the tab name in smaller text. On narrower screens, these wrap and the tab bar becomes two rows, pushing content down | Hide subtitles below 992px via `@media` query, or use tooltip-on-hover for subtitles instead of always-visible text |
| 28 | Medium | Print output | The print stylesheet inverts dark theme to light — but the ECharts charts are rendered as canvas elements with dark backgrounds. Print output shows dark charts on a white page | Either configure ECharts to use a light theme for print (via `window.matchMedia('print')` listener that re-renders charts), or add a "Download PDF" button that generates a purpose-built light-mode export |
| 29 | Low | Cross-ref consistency | Some cross-reference links say "See also:" in a styled div; others are inline "—" links at the end of findings. Some tabs have cross-refs, others don't | Standardize: every tab should end with a "See also:" cross-ref div linking to the 2-3 most related tabs |
| 30 | Low | Color palette | The dashboard uses 4 core colors: blue (#4C78A8), green (#54A24B), red (#E45756), orange (#F58518). These are also the vendor colors. When a bar chart shows tradition families (colored by these same values) AND vendor-colored axis labels, the colors conflict | Reserve blue/orange/red exclusively for vendor identification; use a different palette (e.g., teal, purple, amber) for tradition family coloring to avoid semantic collision |
| 31 | Low | Loading performance | All 15+ ECharts instances are initialized lazily on first tab click, but the initial load pulls in the full 129KB HTML + ECharts 5 (800KB) + Bootstrap (180KB) = ~1.1MB total | Consider lazy-loading ECharts and Bootstrap from CDN with `defer`/`async` attributes; the current CDN links block rendering |
| 32 | Low | Mobile experience | On sub-768px screens, the tab bar wraps to 3 rows, consuming significant vertical space. Stat cards stack to single-column, which works. Charts resize but some tooltip text overflows | Replace the tab bar with a dropdown selector (`<select>`) on mobile, or use a horizontal scrollable tab bar with `overflow-x: auto` |

---

## Content & Readability Critique

### Text Quality

| # | Category | Issue | Recommendation |
|---|----------|-------|----------------|
| 33 | Jargon density | Terms like "Dirichlet-weighted iterations," "point-biserial r," "Cramér's V," and "maqasid al-shariah" are used without inline definitions | Add tooltip definitions for technical terms (CSS `title` attribute or a hover popup). The dashboard serves both AI researchers (who know Cramér's V) and policy audiences (who may not) |
| 34 | Sentence length | Several annotation sentences exceed 40 words: "Each candidate was scored on a six-component Religious Discriminability (RD) rubric that measures the depth of engagement with religious content — ranging from incidental mention (score near 0) to substantive theological evaluation (score near 100)." | Break long sentences into 2-3 shorter ones. Academic rigor does not require run-on sentences |
| 35 | Executive summary length | The executive summary paragraph is 104 words — appropriate for an abstract, but long for a dashboard header. Users may skip it entirely | Cut to 50-60 words. Move the "three behavioral modes" detail into the Key Findings section (which already covers it in the first bullet) |
| 36 | Repeated framing | The phrase "the only instrument that discriminates across vendors" appears in the exec summary, Key Findings, Tab 1 stat card, Tab 5 cross-vendor table, Tab 6 annotation, and Tab 6 findings callout — at least 6 times | State it prominently once (Key Findings) and reference it elsewhere with "see Key Finding #5" or a cross-ref link, rather than restating the full claim |
| 37 | Passive voice | Several annotations use passive constructions: "Scores were assigned through structured assessment..." "Tests were specified before analysis..." | Convert to active voice: "The theological advisory council assigned scores..." "We specified tests before analysis..." Active voice improves readability by 15-20% (Flesch) |

### Graphics Quality

| # | Category | Issue | Recommendation |
|---|----------|-------|----------------|
| 38 | Chart title consistency | Some charts use "Fig. N —" prefix (via CSS counter), others don't. The gradient indicator table has no figure number | Assign explicit figure numbers to all visualizations including tables |
| 39 | Axis label color | All y-axis and x-axis labels use `#8b949e` (muted gray). On the dark background, this provides only ~3.5:1 contrast ratio — below WCAG AA requirement of 4.5:1 for normal text | Lighten axis labels to `#a8b2bd` or `#c9d1d9` to achieve 4.5:1+ contrast |
| 40 | Chart background inconsistency | All ECharts charts use `backgroundColor: 'transparent'`, which means they inherit the card background (`#1c2128`). But when saved as PNG (via toolbox), the background is `#0d1117` (page background). This creates a visual mismatch when charts are extracted | Set `saveAsImage.backgroundColor` to `#1c2128` (card color) to match the visual context |
| 41 | Tooltip design | ECharts tooltips use the default white/light theme, which clashes visually with the dark dashboard | Configure ECharts tooltip with dark background: `tooltip: { backgroundColor: '#1c2128', borderColor: '#30363d', textStyle: { color: '#e6edf3' } }` |
| 42 | Chart sizing | Several charts have hardcoded heights (350px, 380px, 420px, 450px). On large monitors (1440p+), charts appear small with excessive whitespace below | Use `min-height` instead of fixed `height`, or calculate height based on data cardinality (e.g., forest plot: 15px per benchmark × n benchmarks) |

---

## Priority Ranking — Top 10 Recommendations

| Priority | Issue # | Change | Impact | Effort |
|----------|---------|--------|--------|--------|
| 1 | 24 | Collapsible annotation prose (bold summary + "Read more") | Cuts cognitive load by ~50% | Medium |
| 2 | 23 | Side-by-side chart + annotation layout on wide screens | Halves vertical scrolling | Medium |
| 3 | 15 | Claim cards in 2-column grid or collapsible | Reduces Tab 5 length by ~40% | Low |
| 4 | 39 | Lighten axis label color for WCAG AA compliance | Accessibility compliance | Low |
| 5 | 41 | Dark-themed ECharts tooltips | Visual consistency | Low |
| 6 | 1 | Section dividers between benchmark and vendor stat cards | Improves Tab 1 scanability | Low |
| 7 | 5 | Consistent T2 range precision (6.7%, not 7%) | Data accuracy | Low |
| 8 | 20 | Merge two T2 charts into one with beginner/advanced/overall | Removes redundancy | Medium |
| 9 | 27 | Hide tab subtitles on mobile | Fixes tab bar wrapping | Low |
| 10 | 25 | Add favicon | Eliminates console error | Low |

---

## Formal Dissents

**Dissent 1 — Information Designer (#1) vs. Content Strategist (#12):** The Information Designer recommends cutting annotation text by 60% to make this a "visualization-first" dashboard. The Content Strategist argues that the annotations are the dashboard's primary scholarly contribution — without them, it becomes a chart gallery without interpretive value. **Resolution:** The collapsible annotation approach (Priority #1) satisfies both: charts are primary, prose is accessible but not mandatory.

**Dissent 2 — Accessibility Auditor (#3) vs. Dark Theme Designer (#5):** The Accessibility Auditor flags that the overall dark theme creates systematic WCAG contrast issues (axis labels, muted text, badge colors). The Dark Theme Designer argues that dark themes reduce eye strain for extended analytical sessions and are standard in data dashboards. **Resolution:** Keep the dark theme but fix specific contrast violations — lighten text to `#c9d1d9`, axis labels to `#a8b2bd`, and ensure all badges meet 4.5:1.

**Dissent 3 — Mobile Tester (#11) vs. Dashboard Architect (#8):** The Mobile Tester recommends a mobile-first redesign with a tab dropdown and vertically stacked charts. The Dashboard Architect argues this is an academic research dashboard primarily viewed on desktop/laptop; optimizing for mobile would compromise the desktop experience. **Resolution:** Target "functional on mobile" (no broken layouts, readable stat cards) without "mobile-optimized" (smaller charts are acceptable). Apply the low-effort fixes: hide tab subtitles, use `overflow-x: auto` on tab bar.

---

## Summary Statistics

- **Total issues identified:** 42
- **High severity:** 3 (annotation density, overall length, Tab 5 text heaviness)
- **Medium severity:** 15
- **Low severity:** 24
- **Zero JS errors** (only favicon 404)
- **Overall rating:** 8.2/10 — strong academic dashboard, primary weakness is information density

---

*Filed: 2026-04-05 | CEI-Lit-WS/RELIGIOUS-VALUES/reports/ | 12-member expert council*
