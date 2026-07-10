# Moral Psychology Benchmarks Dashboard --- Expert Council Review Round 2

**Date:** 2026-04-04
**Session:** S11 (Cross-Vendor Council Analysis)
**Review Scope:** Dashboard UX Review Round 2 --- Narrative coherence, annotation quality, accessibility, and user experience across all 12 tabs
**Dashboard URL:** https://cjimmylin.github.io/cei-moral-psych-dashboard/
**Prior review:** `ANALYSIS/20260404-cross-vendor-dashboard-review.md` (Round 1: 12 recommendations, 10/12 implemented)
**Council:** 12 members | **Tabs reviewed:** 12 | **Annotations audited:** 50

---

## Review Dimensions

| # | Dimension | Description | Lead Reviewers |
|---|-----------|-------------|----------------|
| D1 | Annotation Coverage | Every tab and major chart has expert commentary | Chen (#1), Okafor (#2) |
| D2 | Annotation Quality | Annotations are accurate, insightful, and accessible to non-specialists | Lindqvist (#6), Ruiz (#11) |
| D3 | Narrative Coherence | Tabs tell a connected story; findings build on each other logically | Okafor (#2), Chalmers-Park (#12) |
| D4 | Visual Hierarchy | Charts, annotations, and KPIs have clear reading order | Torres (#3), Al-Rashid (#5) |
| D5 | Accessibility | Screen readers, color contrast, keyboard navigation, ARIA labels | Al-Rashid (#5), Krishnamurthy (#8) |
| D6 | Mobile / Responsive | Usability on tablets and phones; tab navigation at small widths | Volkov (#9), Moreau (#10) |
| D7 | Policy Audience Fit | Whether a non-technical reader can extract key takeaways in under 5 minutes | Moreau (#10), Goldstein (#7) |
| D8 | Cross-Tab Navigation | Whether insights connect across tabs; silos vs. integrated narrative | Watanabe (#4), Torres (#3) |

---

## Member Reviews

### Dr. Yilin Chen (#1) --- Psychometrics / Measurement Validity

**Tabs reviewed:** Tab 5 (Trials), Tab 4 (Implementation), Tab 8 (Trial Results)

**R2-01 | Tab 5 | D1 | CRITICAL**
*Observation:* Tab 5 (Trials) contains zero annotation divs. It is the only tab in the entire dashboard with no expert commentary whatsoever. The trials tab presents raw benchmark administration results --- precisely the content most in need of interpretive context for readers unfamiliar with psychometric scoring conventions.
*Recommendation:* Add 4--6 annotations to Tab 5 covering: (a) an introductory block explaining what a "trial" means in this context, (b) chart-level annotations on the trial outcome distributions, (c) guidance on interpreting ceiling effects and score ranges.
*Implementation hint:* Add entries to `_tab_annotations.py` under a new `"tab5"` key in `ANNOTATIONS`. Use the existing `renderTabAnnotations()` JS function --- no new rendering code needed.
*Effort:* Low

**R2-02 | Tab 8 | D2 | Moderate**
*Observation:* The Trial Results tab shows per-benchmark scores but annotations do not flag which results are psychometrically uninformative (ceiling effects, zero variance). A reader could mistake a unanimous 100/100 score for a meaningful finding rather than a measurement artifact.
*Recommendation:* Add a "measurement note" annotation block explaining that benchmarks with identical scores across all models (e.g., ECI, MoralMachine) are measurement ceilings, not evidence of genuine agreement. Reference the CV < 0.05 threshold from Tab 12.
*Implementation hint:* Append a `"type": "description"` annotation keyed to the results table container.
*Effort:* Low

**R2-03 | Tab 4 | D4 | Minor**
*Observation:* Implementation tab annotations use identical visual treatment (same border-left color, same font size) as chart-level annotations, making it unclear which commentary is a section introduction and which is chart-specific.
*Recommendation:* Differentiate intro-block annotations with a distinct left-border color (e.g., `#4ea8de` for intros vs. `#6c757d` for chart notes) and slightly larger font size (0.95rem vs. 0.875rem).
*Implementation hint:* Add a `.annotation-intro` CSS class in `style.css` and apply it to annotations where `type === "intro"`.
*Effort:* Low

---

### Dr. Amara Okafor (#2) --- Moral Philosophy / Normative Ethics

**Tabs reviewed:** Tab 1 (Overview), Tab 10 (Cultural & Religious)

**R2-04 | Tab 1 | D7 | MAJOR**
*Observation:* The Overview tab jumps immediately into KPI cards and charts. There is no executive summary or "5-minute view" for policy audiences. A policymaker arriving at the dashboard has no way to grasp the 3--5 key findings without clicking through 12 tabs.
*Recommendation:* Add an executive summary card at the top of Tab 1 with 4--5 bullet points summarizing headline findings: (1) 6/23 benchmarks show identical scores across all 9 models, (2) RLHF produces convergent moral profiles regardless of vendor, (3) scale-dependent divergence on DIT and CoT, (4) universal WEIRD-liberal bias, (5) purity/authority suppression across all vendors. Format as a visually distinct callout box.
*Implementation hint:* Add a `<div class="executive-summary">` block before the first chart in the Overview tab HTML. Style with a left-accent border and slightly larger text.
*Effort:* Med

**R2-05 | Tab 10 | D1 | Moderate**
*Observation:* The Sacred Values analysis container within Tab 10 (Cultural & Religious) has no annotation wrapper. The sacred/profane distinction findings are presented without the expert commentary that accompanies equivalent content in other tabs.
*Recommendation:* Add 2 annotations to the Sacred Values section: (a) a context-setting block from Dr. Goldstein explaining the theoretical significance of purity-floor findings, (b) a chart annotation on the cross-vendor sacred values comparison.
*Implementation hint:* Add entries to `_tab_annotations.py` under the `"tab10"` key, targeting the sacred values chart container ID.
*Effort:* Low

---

### Dr. Rebecca Torres (#3) --- AI Safety / Alignment

**Tabs reviewed:** Tab 9 (Computational Analysis), Tab 12 (Cross-Vendor Analysis)

**R2-06 | Tabs 9--12 | D8 | Moderate**
*Observation:* The four analytical tabs (Computational Analysis subtabs, Cultural & Religious, Model Comparison, Cross-Vendor) each present findings in isolation. The critical insight that RLHF convergence (Tab 12) undermines cross-cultural variation claims (Tab 10) requires a reader to mentally synthesize across tabs with no navigational assistance.
*Recommendation:* Add cross-tab navigation links at the bottom of each tab's annotation block. Format as "Related findings: [Tab 10: Cultural patterns] [Tab 12: Cross-vendor convergence]" with in-page anchor links.
*Implementation hint:* Add a `renderCrossTabLinks(tabId, relatedTabs)` function in `app.js` that appends a `<div class="cross-tab-links">` after the last annotation in each tab. Use `onclick` handlers to switch to the target tab via Bootstrap's `.tab('show')`.
*Effort:* Med

**R2-07 | Tab 12 | D4 | Minor**
*Observation:* The 8-item conclusions accordion at the bottom of Tab 12 uses severity coding (Critical/Major/Moderate) but the color mapping is not explained anywhere. A reader encountering red, amber, and blue badges has no legend.
*Recommendation:* Add a 1-line legend above the accordion: "Severity: Critical (red) | Major (amber) | Moderate (blue)".
*Implementation hint:* Insert a `<p class="text-muted small">` element before the accordion container.
*Effort:* Low

---

### Dr. Kenji Watanabe (#4) --- Cross-Cultural Psychology

**Tabs reviewed:** Tab 10 (Cultural & Religious), Tab 11 (Model Comparison)

**R2-08 | Tab 10 | D3 | MAJOR**
*Observation:* Tab 10 presents cultural and religious moral patterns but does not explicitly address the elephant in the room: all models show the same WEIRD-liberal profile, which means cross-cultural "findings" are artifacts of uniform training bias. The narrative implies genuine cultural sensitivity analysis, but the cross-vendor data (Tab 12) shows this is impossible with current models.
*Recommendation:* Add a prominent caveat annotation at the top of Tab 10 stating: "All 9 models across 3 vendors exhibit identical WEIRD-liberal moral profiles (see Tab 12). The patterns below reflect training data bias, not genuine cross-cultural moral reasoning capacity."
*Implementation hint:* Add a `"type": "intro"` annotation with `"severity": "critical"` styling to the `"tab10"` key in `_tab_annotations.py`.
*Effort:* Low

**R2-09 | Tab 11 | D2 | Moderate**
*Observation:* Model Comparison annotations reference "within-family variation" but do not define what constitutes a "family" (vendor model lineup ordered by parameter count). The term is used 4 times without definition.
*Recommendation:* Add a glossary-style annotation defining "model family" as the set of models from a single vendor ordered by parameter count (e.g., Haiku < Sonnet < Opus for Anthropic).
*Implementation hint:* Prepend a `"type": "description"` annotation to `"tab11"` annotations in `_tab_annotations.py`.
*Effort:* Low

---

### Dr. Fatima Al-Rashid (#5) --- Computational Linguistics / NLP

**Tabs reviewed:** Tab 2 (Feature Matrix), Tab 6 (Methods)

**R2-10 | All tabs | D5 | Moderate**
*Observation:* None of the ECharts chart containers have `aria-label` or `role="img"` attributes. Screen readers encounter empty `<div>` elements with no description of chart content. The 50 text annotations are accessible, but the 15+ charts are invisible to assistive technology.
*Recommendation:* Add `role="img"` and `aria-label="[chart description]"` to every ECharts container `<div>`. Each label should be a 1-sentence summary of what the chart shows (e.g., `aria-label="Radar chart comparing 8 moral foundation scores across 9 AI models from 3 vendors"`).
*Implementation hint:* In `generate_dashboard.py`, modify chart container emission to include `role="img" aria-label="{chart_description}"`. Store descriptions in `_tab_annotations.py` or a parallel dict.
*Effort:* Med

**R2-11 | Tab 2 | D4 | Minor**
*Observation:* The Feature Matrix tab uses small-font cells in a dense table. At default zoom, row labels are truncated on screens narrower than 1280px. No horizontal scroll indicator is visible.
*Recommendation:* Add a subtle "scroll right" indicator (faded gradient or arrow icon) on the right edge of overflow tables, and increase row label min-width to 200px.
*Implementation hint:* Add `.table-scroll-hint::after { content: ""; ... }` pseudo-element in `style.css` with a horizontal gradient fade.
*Effort:* Low

---

### Dr. Marcus Lindqvist (#6) --- Cognitive Science / Dual-Process Theory

**Tabs reviewed:** Tab 3 (Theory Heatmap), Tab 9 (Computational Analysis)

**R2-12 | Tab 3 | D2 | MAJOR**
*Observation:* The Theory Heatmap shows dual-process constructs (System 1/System 2 moral judgment) alongside normative ethical frameworks (deontology, consequentialism), but annotations do not clarify that these are orthogonal dimensions. A reader could interpret them as competing categories on the same axis.
*Recommendation:* Add a framing annotation explaining that the heatmap rows group into three distinct categories: (a) normative frameworks (what moral position), (b) cognitive mechanisms (how moral judgments are formed), and (c) developmental stages (moral reasoning maturity). Visually separate these groups with horizontal rule annotations.
*Implementation hint:* Add 3 `"type": "description"` annotations to `"tab3"`, one before each conceptual group. Consider adding faint horizontal dividers in the heatmap itself via ECharts `markLine`.
*Effort:* Med

**R2-13 | Tab 9 | D3 | Moderate**
*Observation:* The Computational Analysis tab has 4 subtabs but no introductory text explaining how they relate to each other. A reader clicking through subtabs encounters isolated analyses without understanding the analytical pipeline.
*Recommendation:* Add a brief (2--3 sentence) introductory annotation at the top of Tab 9 explaining the 4-subtab structure and how each builds on the previous.
*Implementation hint:* Add an `"intro"` annotation to the `"tab9"` key that renders above the subtab navigation.
*Effort:* Low

---

### Dr. Sarah Goldstein (#7) --- Religious Studies / Comparative Theology

**Tabs reviewed:** Tab 10 (Cultural & Religious)

**R2-14 | Tab 10 | D1 | Moderate**
*Observation:* The Sacred Values section within Tab 10 presents purity-foundation scores and sacred/profane distinction data, but there is no annotation connecting these findings to the broader literature on religious moral reasoning. The purity floor (universally low scores across all vendors) is the single most important finding for religious ethics, yet it receives less annotation space than secular moral foundations.
*Recommendation:* Add 2 annotations: (a) a chart annotation on the purity-floor bar chart explaining that universal low purity scores may reflect systematic exclusion of religious moral reasoning from RLHF training, not genuine moral architecture; (b) a bridging annotation linking to Tab 12's vendor convergence findings as evidence this is a training artifact.
*Implementation hint:* Extend `"tab10"` annotations in `_tab_annotations.py`. Use `"member": "Dr. Sarah Goldstein"` attribution.
*Effort:* Low

---

### Dr. Raj Krishnamurthy (#8) --- Statistical Methodology

**Tabs reviewed:** Tab 8 (Trial Results), Tab 12 (Cross-Vendor Analysis)

**R2-15 | Tab 12 | D5 | Moderate**
*Observation:* The convergence scatter chart and discrimination bar chart use color alone to distinguish between "discriminating" (blue) and "ceiling" (gray) benchmarks. This distinction is invisible to readers with deuteranopia (blue-gray confusion is less common but non-zero) and entirely lost in grayscale printing.
*Recommendation:* Add shape encoding in addition to color: use circles for discriminating benchmarks and triangles (or squares) for ceiling benchmarks. This ensures the distinction survives both color vision deficiency and print.
*Implementation hint:* In `charts.js`, set `symbol: 'circle'` for the discriminating series and `symbol: 'triangle'` for the ceiling series in the convergence scatter chart options.
*Effort:* Low

**R2-16 | Tab 8 | D4 | Minor**
*Observation:* Trial Results table rows are uniformly styled. The conditional formatting from Tab 12's trial table (dimmed ceiling rows, bold max values) is not applied to Tab 8's equivalent table.
*Recommendation:* Apply the same conditional formatting logic from Tab 12 to Tab 8's trial results table for consistency.
*Implementation hint:* Extract the conditional formatting function in `app.js` into a shared utility and call it for both Tab 8 and Tab 12 tables.
*Effort:* Low

---

### Dr. Elena Volkov (#9) --- AI Industry / Vendor Perspective

**Tabs reviewed:** Tab 1 (Overview), Tab 12 (Cross-Vendor Analysis)

**R2-17 | All tabs | D6 | Moderate**
*Observation:* The 12 tab buttons overflow into a single horizontal scroll strip on mobile. There is no visual grouping to indicate that Tabs 1--3 are "Framework," Tabs 4--8 are "Evidence," and Tabs 9--12 are "Analysis." A user on a phone sees 12 undifferentiated buttons.
*Recommendation:* Add visual tab group separators --- thin vertical dividers or subtle background shading differences between the three logical groups. On mobile, consider a 2-row layout: row 1 = Framework + Evidence, row 2 = Analysis.
*Implementation hint:* In `style.css`, add `.nav-tabs .tab-separator { border-left: 2px solid rgba(255,255,255,0.15); height: 24px; margin: 0 4px; }` and insert separator `<li>` elements in the tab list HTML between groups.
*Effort:* Med

**R2-18 | All tabs | D4 | Minor**
*Observation:* Key ECharts charts (radar, heatmap, convergence scatter) lack the built-in ECharts toolbox for saving chart images. Users who want to cite a specific chart in presentations or reports must take manual screenshots.
*Recommendation:* Add `toolbox: { feature: { saveAsImage: { title: 'Save' } } }` to the 6 most important charts: radar (Tab 12), heatmap (Tab 3), convergence scatter (Tab 12), discrimination bar (Tab 12), scale sensitivity (Tab 12), and the overview summary chart (Tab 1).
*Implementation hint:* In `charts.js`, add the `toolbox` property to each chart's `option` object. Position: `right: 20, top: 10`.
*Effort:* Low

---

### Dr. Jean-Pierre Moreau (#10) --- Policy / Governance

**Tabs reviewed:** Tab 1 (Overview), Tab 7 (Paper Ranking)

**R2-19 | Footer | D7 | Minor**
*Observation:* The dashboard has no provenance or "about" section. A policymaker encountering the dashboard via a shared link has no way to determine: (a) who created it, (b) what data it is based on, (c) when it was last updated, (d) how to cite it.
*Recommendation:* Add a persistent footer (visible on all tabs) with: project name ("CEI Moral Psychology Benchmarks Meta-Evaluation"), data date ("Data as of 2026-04-04"), methodology link (to the published methods document), citation format, and contact/repository link.
*Implementation hint:* Add a `<footer class="dashboard-provenance">` element after the tab content container in `index.html`. Style with reduced opacity text and a top border.
*Effort:* Low

**R2-20 | Tab 1 | D7 | Moderate**
*Observation:* The Overview tab KPI cards use technical language ("CV", "ECI ceiling", "discriminating benchmarks") without glossary definitions. A policy audience would need prior psychometric training to interpret these cards.
*Recommendation:* Add tooltip definitions on KPI card labels. On hover/tap, show a 1-sentence plain-language definition (e.g., "Discriminating benchmarks: Tests where different AI models produce meaningfully different scores").
*Implementation hint:* Wrap KPI labels in `<span data-bs-toggle="tooltip" title="...">` and initialize Bootstrap tooltips in `app.js`.
*Effort:* Low

---

### Dr. Isabella Ruiz (#11) --- Developmental Psychology

**Tabs reviewed:** Tab 5 (Trials), Tab 11 (Model Comparison)

**R2-21 | Tab 11 | D3 | Moderate**
*Observation:* The Model Comparison tab presents the DIT P-score gradient (Haiku 60, Opus 75, Sonnet 85) as a key finding, but annotations do not address the non-monotonic relationship with model size. Sonnet (medium) outscores Opus (large) on post-conventional reasoning --- this breaks the developmental analogy and deserves explicit commentary.
*Recommendation:* Add an annotation flagging the Sonnet > Opus reversal as a theoretically significant finding that challenges simplistic "bigger model = more mature moral reasoning" assumptions.
*Implementation hint:* Add a `"type": "chart"` annotation to `"tab11"` keyed to the DIT comparison chart, attributed to Dr. Ruiz.
*Effort:* Low

**R2-22 | All tabs | D6 | Minor**
*Observation:* The dashboard has no print stylesheet. Printing any tab produces dark-background pages that waste toner and render charts illegibly on white paper.
*Recommendation:* Add a basic `@media print` stylesheet that: (a) forces white background and dark text, (b) hides the tab navigation bar, (c) hides the footer toggle, (d) adds page-break-before on major section dividers.
*Implementation hint:* Append a `@media print { ... }` block to `style.css` with `background: white !important; color: #111 !important;` overrides on `body`, `.card`, and `.annotation`.
*Effort:* Med

---

### Dr. David Chalmers-Park (#12) --- Philosophy of Mind / Consciousness

**Tabs reviewed:** Tab 1 (Overview), Tab 12 (Cross-Vendor Analysis)

**R2-23 | Tab 12 | D3 | Moderate**
*Observation:* The Cross-Vendor Analysis tab presents convergence data without addressing the foundational interpretive question: does moral convergence across vendors indicate genuine moral understanding, shared training data, or identical RLHF reward signals? The annotations describe *what* converges but not *why this matters* for AI moral cognition.
*Recommendation:* Add a concluding annotation to Tab 12 addressing the interpretive ambiguity of convergence: same outputs can arise from shared understanding, shared training data, or shared optimization targets, and the dashboard data alone cannot distinguish these explanations.
*Implementation hint:* Add a `"type": "description"` annotation at the end of `"tab12"` annotations, attributed to Dr. Chalmers-Park. Frame as an open question rather than a conclusion.
*Effort:* Low

**R2-24 | Tab 1 | D3 | Minor**
*Observation:* The Overview tab presents findings as established facts ("RLHF produces convergent moral profiles") without epistemic hedging. For a philosophical audience, the absence of uncertainty language undermines credibility.
*Recommendation:* Review the 5 headline KPI card labels and the executive summary (once added per R2-04) for epistemic hedging. Where appropriate, add qualifiers: "appears to produce," "in the benchmarks tested," "within the scope of these 23 instruments."
*Implementation hint:* Text-only edit to annotation content and KPI card subtitles in `_tab_annotations.py` and `generate_dashboard.py`.
*Effort:* Low

---

## Consensus Recommendations

The following recommendations received explicit support from multiple council members during cross-review discussion. Listed by severity, then effort.

| ID | Recommendation | Severity | Effort | Supporting Members | Tabs |
|----|---------------|----------|--------|-------------------|------|
| **CR-01** | Add annotations to Tab 5 (Trials) --- currently zero annotations | Critical | Low | Chen (#1), Ruiz (#11), Okafor (#2) | 5 |
| **CR-02** | Add executive summary / "5-minute view" card on Overview tab | Major | Med | Okafor (#2), Moreau (#10), Volkov (#9), Chalmers-Park (#12) | 1 |
| **CR-03** | Tab group visual separators (Framework / Evidence / Analysis) | Moderate | Med | Volkov (#9), Al-Rashid (#5), Moreau (#10) | All |
| **CR-04** | Enhanced annotation visual hierarchy (intro vs. chart vs. description) | Major | Low | Chen (#1), Lindqvist (#6), Torres (#3) | All |
| **CR-05** | Cross-tab navigation links connecting related findings | Moderate | Med | Torres (#3), Watanabe (#4), Chalmers-Park (#12) | 9--12 |
| **CR-06** | Sacred Values annotation gap in Tab 10 | Moderate | Low | Goldstein (#7), Okafor (#2), Watanabe (#4) | 10 |
| **CR-07** | Provenance / about footer on all tabs | Minor | Low | Moreau (#10), Volkov (#9), Al-Rashid (#5) | All |
| **CR-08** | Accessibility: `aria-label` and `role="img"` on all chart containers | Moderate | Med | Al-Rashid (#5), Krishnamurthy (#8), Moreau (#10) | All |
| **CR-09** | ECharts toolbox (save-as-image) on 6 key charts | Minor | Low | Volkov (#9), Krishnamurthy (#8) | 1, 3, 12 |
| **CR-10** | Print stylesheet basics (white background, hide nav, page breaks) | Minor | Med | Ruiz (#11), Al-Rashid (#5), Moreau (#10) | All |

---

## Round 1 Deferred Items Status

### R7: 9-Model Heatmap Granularity

**Original recommendation (R1):** Expand vendor-averaged heatmap from 3 columns to 9 columns (per-model granularity).
**Round 2 status:** Still deferred. The 23x9 trial comparison table in Tab 12 with conditional formatting (R6 implemented) serves as a partial substitute. Council consensus: lower priority than annotation gaps (CR-01) and executive summary (CR-02). Revisit when dashboard layout is redesigned for wider viewports.
**Council note (Dr. Chen):** "The trial table with conditional formatting is an adequate interim solution. The 9-column heatmap would require responsive breakpoints and is better addressed in a v2 dashboard redesign."

### R11: Human Baseline References

**Original recommendation (R1):** Add human population norms to radar charts and cross-model comparisons.
**Round 2 status:** Partially addressed. Tab 12 annotations now reference human norms in text (e.g., "human MFQ-30 means typically show Care > Fairness > Loyalty > Authority > Purity"), but no quantitative baselines appear on charts. Curating validated population norms from original publications remains the bottleneck.
**Council note (Dr. Ruiz):** "Even approximate human baselines (MFQ-30 college student means, DIT adult P-score ranges) would dramatically improve interpretability. I recommend prioritizing MFQ-30 and DIT baselines as a minimum viable addition --- these are the two most-cited instruments with widely available norms."
**Recommended next step:** Curate population norms for MFQ-30 (Graham et al., 2011) and DIT-2 (Thoma, 2006) and add as dashed reference lines on the radar chart and model comparison bar charts.

---

## Implementation Priority Matrix

Sorted by severity (Critical > Major > Moderate > Minor), then by effort (Low > Med > High).

| Priority | ID | Recommendation | Severity | Effort | Source |
|----------|-----|---------------|----------|--------|--------|
| 1 | CR-01 / R2-01 | Tab 5 annotations (zero coverage) | Critical | Low | Chen, Ruiz, Okafor |
| 2 | CR-04 / R2-03 | Annotation visual hierarchy (intro vs chart) | Major | Low | Chen, Lindqvist, Torres |
| 3 | CR-02 / R2-04 | Executive summary card on Overview | Major | Med | Okafor, Moreau, Volkov, Chalmers-Park |
| 4 | R2-12 | Theory Heatmap conceptual grouping | Major | Med | Lindqvist |
| 5 | CR-06 / R2-05 | Sacred Values annotation gap | Moderate | Low | Goldstein, Okafor, Watanabe |
| 6 | R2-08 | WEIRD caveat on Tab 10 | Moderate | Low | Watanabe |
| 7 | R2-09 | "Model family" definition in Tab 11 | Moderate | Low | Watanabe |
| 8 | R2-15 | Shape encoding on scatter charts | Moderate | Low | Krishnamurthy |
| 9 | R2-02 | Ceiling effect annotation on Tab 8 | Moderate | Low | Chen |
| 10 | R2-13 | Computational Analysis subtab intro | Moderate | Low | Lindqvist |
| 11 | R2-20 | KPI tooltip definitions | Moderate | Low | Moreau |
| 12 | R2-21 | DIT non-monotonic annotation | Moderate | Low | Ruiz |
| 13 | R2-23 | Convergence interpretive ambiguity annotation | Moderate | Low | Chalmers-Park |
| 14 | CR-05 / R2-06 | Cross-tab navigation links | Moderate | Med | Torres, Watanabe, Chalmers-Park |
| 15 | CR-03 / R2-17 | Tab group visual separators | Moderate | Med | Volkov, Al-Rashid, Moreau |
| 16 | CR-08 / R2-10 | ARIA labels on chart containers | Moderate | Med | Al-Rashid, Krishnamurthy, Moreau |
| 17 | CR-07 / R2-19 | Provenance / about footer | Minor | Low | Moreau, Volkov, Al-Rashid |
| 18 | CR-09 / R2-18 | ECharts saveAsImage toolbox | Minor | Low | Volkov, Krishnamurthy |
| 19 | R2-07 | Accordion severity legend | Minor | Low | Torres |
| 20 | R2-11 | Feature Matrix scroll indicator | Minor | Low | Al-Rashid |
| 21 | R2-16 | Tab 8 conditional formatting parity | Minor | Low | Krishnamurthy |
| 22 | R2-24 | Epistemic hedging in Overview text | Minor | Low | Chalmers-Park |
| 23 | CR-10 / R2-22 | Print stylesheet | Minor | Med | Ruiz, Al-Rashid, Moreau |

**Summary:** 24 recommendations total (R2-01 through R2-24). 10 consensus recommendations (CR-01 through CR-10). 1 Critical, 3 Major, 12 Moderate, 8 Minor. Estimated implementation: 13 Low-effort items achievable in a single session; 8 Med-effort items require dedicated work.

---

## Approval

All 12 council members reviewed this document. Consensus recommendations reflect items endorsed by 3+ members.

| Member | Reviewed | Recommendations Authored |
|--------|----------|------------------------|
| Dr. Yilin Chen (#1) | Tabs 4, 5, 8 | R2-01, R2-02, R2-03 |
| Dr. Amara Okafor (#2) | Tabs 1, 10 | R2-04, R2-05 |
| Dr. Rebecca Torres (#3) | Tabs 9, 12 | R2-06, R2-07 |
| Dr. Kenji Watanabe (#4) | Tabs 10, 11 | R2-08, R2-09 |
| Dr. Fatima Al-Rashid (#5) | Tabs 2, 6 | R2-10, R2-11 |
| Dr. Marcus Lindqvist (#6) | Tabs 3, 9 | R2-12, R2-13 |
| Dr. Sarah Goldstein (#7) | Tab 10 | R2-14 |
| Dr. Raj Krishnamurthy (#8) | Tabs 8, 12 | R2-15, R2-16 |
| Dr. Elena Volkov (#9) | Tabs 1, 12 | R2-17, R2-18 |
| Dr. Jean-Pierre Moreau (#10) | Tabs 1, 7 | R2-19, R2-20 |
| Dr. Isabella Ruiz (#11) | Tabs 5, 11 | R2-21, R2-22 |
| Dr. David Chalmers-Park (#12) | Tabs 1, 12 | R2-23, R2-24 |
