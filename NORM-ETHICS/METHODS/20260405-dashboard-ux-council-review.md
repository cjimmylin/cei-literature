# NormEval Dashboard UX Council Review

**Date:** 2026-04-05
**Dashboard:** https://cjimmylin.github.io/cei-normeval-dashboard/
**Version reviewed:** Post-Session 10 (commit `3d066c0`, 10 tabs, 9-model / 3-vendor replication)

---

## Council Composition (12 Experts)

| # | Perspective | Focus Area |
|---|-----------|------------|
| 1 | Information Design | Data visualization hierarchy, chart selection, visual encoding |
| 2 | Academic Publishing UX | Scholarly dashboard conventions, figure/table formatting |
| 3 | Web Accessibility (WCAG) | Screen reader support, contrast ratios, keyboard navigation |
| 4 | Data Journalism | Narrative structure, progressive disclosure, annotation strategy |
| 5 | Dark-Mode UI Design | Color palette coherence, readability, luminance contrast |
| 6 | Typography & Readability | Font choices, line length, density, scanning patterns |
| 7 | ECharts/Charting Libraries | Technical chart rendering, interactivity, tooltip UX |
| 8 | Mobile Responsiveness | Touch targets, viewport adaptation, tab navigation on small screens |
| 9 | Cognitive Load (UX Psychology) | Working memory limits, chunking, information overload |
| 10 | Scientific Communication | Clarity of claims, statistical presentation, caveat visibility |
| 11 | Color Vision Deficiency | Palette accessibility for protanopia/deuteranopia, redundant encoding |
| 12 | Print & Export | PDF rendering, print stylesheet, offline readability |

---

## Overall Assessment

**Verdict: Strong academic dashboard with sophisticated content, but several UX friction points reduce accessibility and scanability.**

The dashboard successfully implements the "fat data, thin client" architecture with clean ECharts rendering, a coherent dark-mode palette, and expert analysis blocks that add genuine interpretive value. The 10-tab structure covers the full analytical pipeline from benchmark inventory through cross-vendor replication. However, the council identifies **28 specific issues** across 6 categories, ranging from critical accessibility gaps to minor polish items.

**Scores (0-10):**

| Dimension | Score | Notes |
|-----------|-------|-------|
| Content depth | 9.5 | Exceptional — expert blocks, expandable findings, living peer review |
| Visual design | 7.5 | Cohesive dark theme, but some charts underuse available space |
| Typography | 6.5 | Good font choices (Inter/JetBrains Mono), but density issues |
| Accessibility | 4.0 | No ARIA roles, no keyboard nav, poor contrast in some areas |
| Mobile UX | 3.5 | Tab bar overflows, charts don't resize, tables unusable |
| Narrative flow | 8.0 | Tab-explainer pattern is effective; cross-tab references work |

---

## Category 1: Layout & Information Architecture

### Issue 1.1 — Tab bar overflow on narrow viewports (Critical)
**Current:** 10 tab labels in a single horizontal row with `overflow-x: auto`. On viewports below ~1100px, the rightmost tabs (Gaps, Cross-Vendor) are hidden behind a scrollbar that is nearly invisible on dark backgrounds.
**Impact:** Users on laptops or tablets may never discover Tabs 9-10 — the most novel content.
**Recommendation:** Add scroll indicators (gradient fade + arrow buttons) at the edges of the tab bar, or group tabs into two tiers: "Analysis" (Tabs 1-7) and "Replication" (Tabs 8-10) with a visual separator. Consider a dropdown/hamburger for mobile.

### Issue 1.2 — Inconsistent column layouts across tabs
**Current:** Some tabs use `col-lg-6` (50/50 split), others use `col-lg-5`/`col-lg-7`, and the Trials tab uses `col-lg-8`/`col-lg-4`. The Feature Matrix tab is full-width.
**Impact:** Low — this is functional, but the varying layouts create a sense of visual inconsistency.
**Recommendation:** Standardize on 2-3 layout patterns and document them as design tokens. Not urgent.

### Issue 1.3 — No breadcrumb or tab-position indicator
**Current:** The active tab is highlighted with a blue underline, but there is no "Tab 3 of 10" or progress indicator.
**Impact:** On a 10-tab dashboard, users lose spatial orientation. "Am I near the beginning or the end?"
**Recommendation:** Add a subtle "3/10" indicator in the tab bar, or a thin progress bar below the tabs showing position within the tab sequence.

### Issue 1.4 — Expert analysis blocks are visually indistinguishable from tab-explainers
**Current:** Both use the same `.tab-explainer` class with only a different `border-left` color. The expert blocks add a magnifying glass emoji and bold "Expert Analysis" heading, but at a glance they blend together.
**Impact:** Users may skip expert analysis thinking it's a continuation of the tab introduction.
**Recommendation:** Give expert blocks a distinct visual treatment: slightly different background tint (`#1a1d30` instead of `#161822`), or a top-border accent, or an "Expert Analysis" pill/chip that floats in the top-right corner.

---

## Category 2: Typography & Readability

### Issue 2.1 — Tab-explainer text density is overwhelming (High)
**Current:** Tab explainer blocks contain 3 paragraphs of dense text (What/How/Key) at 0.85rem, often exceeding 100 words per paragraph. Line length reaches 120+ characters on wide screens.
**Impact:** Users skip the explainer entirely. Eye-tracking research shows optimal line length is 50-75 characters.
**Recommendation:** (a) Add `max-width: 80ch` to `.tab-explainer` or use a 2-column text layout for wide screens. (b) Break the 3-section pattern into collapsible `<details>` elements — show only "What this tab shows" by default, let users expand "How to read it" and "Key conclusion" on demand. (c) Use slightly larger font (0.88rem) with 1.7 line-height for improved readability.

### Issue 2.2 — Expert block line length exceeds readability threshold
**Current:** Expert analysis blocks run full-width within their column (col-lg-6 or col-lg-12). On a 1440px viewport, this means 90+ characters per line.
**Impact:** Reading fatigue. Academic readers expect 65-75 character lines.
**Recommendation:** Add `max-width: 72ch` to expert block text content, or use `padding: 0.75rem 1.5rem` to narrow the text column.

### Issue 2.3 — Footnote text is too small
**Current:** Footnotes (*, dagger, double-dagger) use `font-size: 0.72rem` — approximately 11.5px at default browser settings.
**Impact:** Borderline legibility on non-Retina displays. WCAG recommends minimum 12px for body text.
**Recommendation:** Increase to `0.78rem` (12.5px) and ensure contrast ratio exceeds 4.5:1 against `--bg-card`.

### Issue 2.4 — Chart titles lack consistent hierarchy
**Current:** Chart titles use `h3` at 0.95rem. Sub-descriptions use `p` at 0.75rem with `--text-muted`. The gap between these two levels is large.
**Impact:** The sub-descriptions are easy to miss, yet they contain critical information (e.g., "T14 PNAS: % of 13 moral dilemmas...").
**Recommendation:** Use 0.8rem for sub-descriptions (up from 0.75rem) and change color from `--text-muted` to `--text-secondary` for better visibility.

---

## Category 3: Color & Visual Encoding

### Issue 3.1 — Color vision deficiency accessibility (Critical)
**Current:** The red-green encoding in the Knowledge vs Judgment chart (`#4ecb71` green for knowledge, `#ef5b5b` red for judgment) is indistinguishable for the ~8% of males with red-green color blindness.
**Impact:** A significant portion of the academic audience cannot interpret the most important construct-level chart.
**Recommendation:** Replace red with orange (`#f0983e`, already in the palette) or use hatching/pattern fills as a redundant channel. Alternatively, use blue (#5b8def) for knowledge and orange for judgment — both are safe for all common color vision deficiencies.

### Issue 3.2 — Feature heatmap uses a single-hue blue scale
**Current:** The feature matrix heatmap (Tab 3) uses varying intensities of blue. Low and medium values are hard to distinguish.
**Impact:** The heatmap is the most data-dense visualization in the dashboard but offers poor discriminability at the low end.
**Recommendation:** Use a diverging palette (e.g., blue-white-orange) if the data has a meaningful midpoint, or a sequential palette with higher contrast (e.g., viridis or inferno, which are perceptually uniform and CVD-safe).

### Issue 3.3 — Provider colors inconsistently applied
**Current:** Anthropic = purple (#a78bfa), OpenAI = green (#4ecb71), Google = blue (#5b8def). But green is also used for "pass" badges, and blue is the ND (Normative Depth) color. This creates semantic collisions.
**Impact:** On Tab 10, the green GPT-5 bars could be misread as "pass/good" when they represent the most conservative profile.
**Recommendation:** Shift OpenAI to a warmer green or teal (#2dd4bf) that doesn't overlap with the pass-green (#16a34a). Or use shape encoding (bar patterns, marker symbols) as a redundant channel.

### Issue 3.4 — Heatmap agreement scale starts at 70%
**Current:** The Cross-Vendor heatmap `visualMap` ranges from 70 to 100. Values below 70 (if any exist) would be invisible.
**Impact:** The 71.1% minimum pair (Haiku-GPT-5) renders as deep red, which accurately conveys "low agreement" — but the compressed scale exaggerates differences. An 80% agreement looks orange when it would be green on a 0-100 scale.
**Recommendation:** This is a defensible design choice (the full 0-100 range would make everything look green), but add a note in the chart description: "Scale: 70-100% (compressed to highlight divergence)."

---

## Category 4: Interactivity & Navigation

### Issue 4.1 — No cross-tab linking (High)
**Current:** The text frequently references other tabs ("see Tab 10", "see Tabs 8-10") but these are plain text, not clickable links.
**Impact:** Users must manually click through the tab bar to find the referenced tab. This is especially painful on mobile where tabs overflow.
**Recommendation:** Make tab references into clickable links that activate the target tab: `<a href="#" onclick="activateTab('tab-crossvendor')">Tab 10</a>`. This is a high-impact, low-effort improvement.

### Issue 4.2 — Tables lack in-page search/filter (Moderate)
**Current:** Tab 2 (All Papers) has a search bar and filters. But the per-trial tables on Tabs 8 and 10 have no search or filtering capability, despite containing 8-10 columns of data.
**Impact:** Users cannot quickly find a specific benchmark or model in these tables.
**Recommendation:** Add a minimal filter row or highlight-on-type search for the per-trial tables.

### Issue 4.3 — Charts lack ECharts toolbox
**Current:** No charts have the ECharts built-in toolbox (save as image, data view, zoom, restore).
**Impact:** Researchers frequently need to export individual charts for presentations or papers. Currently they must screenshot.
**Recommendation:** Add `toolbox: { feature: { saveAsImage: {}, dataView: { readOnly: true } } }` to `baseTheme()`. This is a one-line change in `charts.js` that enables PNG export and raw data view on every chart.

### Issue 4.4 — Expandable findings have no visual affordance when collapsed
**Current:** The chevron (`triangle-right`) on finding cards is 0.7rem and colored `--text-muted`. On dark backgrounds, it's barely visible.
**Impact:** Users may not realize the findings are expandable. The click target (entire card) is generous, but discoverability is poor.
**Recommendation:** (a) Add a "Click to expand" hint on the first card only (dismiss after first click). (b) Make the chevron slightly larger (0.85rem) and colored `--text-secondary`. (c) Add a subtle hover effect (background shift) on the cards.

### Issue 4.5 — No "expand all / collapse all" for findings
**Current:** Each finding must be expanded individually. Users who want to read all 7 must click 7 times.
**Recommendation:** Add a small "Expand All / Collapse All" toggle link above the findings list.

---

## Category 5: Content & Scientific Communication

### Issue 5.1 — Tab-explainer "Key conclusion" buries the lede (High)
**Current:** Each tab explainer follows a rigid What/How/Key three-section pattern. The most important insight ("Key conclusion") is always at the bottom, after two paragraphs of methodological context.
**Impact:** Inverted pyramid — the most newsworthy content is last. Busy readers who scan only the first few lines get methodology, not findings.
**Recommendation:** Lead with the conclusion: "**Key finding:** [one sentence]. **What this shows:** [context]. **How to read it:** [instructions]." This follows data journalism conventions where the headline finding comes first.

### Issue 5.2 — Expert analysis blocks lack structural consistency
**Current:** Some blocks use "What to observe / Interpretation / Conclusion" structure (Tabs 8-10). Others use freeform paragraphs with bold topic headings (Tabs 1-7). The early tabs appear to predate the structured format.
**Recommendation:** Harmonize all expert blocks to use the "What to observe / Interpretation / Conclusion" three-part structure, or at minimum ensure each block has a bold concluding sentence.

### Issue 5.3 — Council vote tallies remain in Tab 10 expert blocks
**Current:** Several expert blocks reference "Council vote: 11/12 robust" or "8/12 favor shared infrastructure hypothesis" from the original simulated council.
**Impact:** After removing simulated names, the vote tallies reference a process that is no longer attributed to named individuals, making them feel ungrounded.
**Recommendation:** Reframe votes as confidence levels: "High confidence (near-unanimous)" instead of "11/12" or "Broad consensus" instead of "8/12". Alternatively, remove specific vote counts entirely and use qualitative descriptors.

### Issue 5.4 — Peer review concerns lack cross-references
**Current:** The updated peer review concern cards have resolution text, but don't link to the specific tabs or data that resolved them.
**Recommendation:** Add tab references: "Resolved: see Tab 8 (Cross-Model) and Tab 10 (Cross-Vendor)" as clickable links in the resolution text.

### Issue 5.5 — No figure/table numbering
**Current:** Charts are labeled by title only ("Pairwise Agreement Heatmap", "IH Scaling"). There are no figure numbers.
**Impact:** Academic readers expect numbered figures for citation: "As shown in Figure 7..." Neither the dashboard nor a future paper can easily reference specific charts.
**Recommendation:** Add auto-incrementing figure numbers using CSS counters: `body { counter-reset: figure; } .chart-container h3::before { counter-increment: figure; content: "Fig. " counter(figure) ": "; }`. This is pure CSS — no JS changes needed.

---

## Category 6: Accessibility & Performance

### Issue 6.1 — No ARIA landmarks or roles (Critical)
**Current:** The dashboard uses semantic HTML (`<header>`, `<ul>`, `<table>`) but has no ARIA roles, labels, or live regions.
**Impact:** Screen readers cannot navigate the tab structure or announce chart descriptions. The dashboard is effectively inaccessible to visually impaired users.
**Recommendation:** Add `role="tablist"` to the nav, `role="tab"` and `aria-selected` to tab links, `role="tabpanel"` to content panes, and `aria-label` to chart containers with text descriptions of the chart contents.

### Issue 6.2 — No skip-to-content link
**Current:** Keyboard users must tab through all 10 tab links before reaching content.
**Recommendation:** Add a visually-hidden "Skip to content" link as the first focusable element.

### Issue 6.3 — Contrast ratio violations
**Current:** `--text-muted` (#6b6f89) on `--bg-card` (#1c1f2e) yields a contrast ratio of approximately 3.2:1, below the WCAG AA requirement of 4.5:1.
**Impact:** Chart sub-descriptions, footnotes, and status text are below accessibility thresholds.
**Recommendation:** Lighten `--text-muted` to `#8a8ea8` (contrast ratio ~4.7:1) or darken the card background.

### Issue 6.4 — No print stylesheet
**Current:** Printing the dashboard yields a dark-background page with invisible text on most printers.
**Impact:** Researchers who want to print a tab for annotation or filing get an unusable output.
**Recommendation:** Add a `@media print` stylesheet that: inverts to light background, hides the tab bar (shows only active tab), removes chart hover effects, and sets `break-inside: avoid` on chart containers.

### Issue 6.5 — External font dependency
**Current:** Google Fonts (Inter, JetBrains Mono) loaded via CDN. If the CDN is down or blocked (common in Chinese academic networks), the dashboard falls back to system sans-serif.
**Impact:** Layout may shift if fallback fonts have different metrics.
**Recommendation:** Self-host the fonts or add explicit `font-display: swap` with well-matched fallback stacks: `font-family: 'Inter', 'SF Pro Text', -apple-system, 'Segoe UI', sans-serif`.

### Issue 6.6 — No loading state for lazy-rendered tabs
**Current:** Tabs use lazy rendering (charts only initialize when tab becomes visible). During the 50ms + ECharts init delay, the chart container shows as an empty dark box.
**Impact:** Users clicking a new tab see a blank area for ~200-500ms before charts appear.
**Recommendation:** Add a minimal loading indicator (CSS spinner or "Loading charts..." text) in each chart container that is replaced when the chart initializes.

---

## Priority Matrix

| Priority | Issues | Impact | Effort |
|----------|--------|--------|--------|
| **P0 — Do First** | 4.1 (cross-tab links), 5.5 (figure numbering), 4.3 (ECharts toolbox) | High | Low |
| **P1 — High Impact** | 2.1 (text density), 3.1 (CVD colors), 1.1 (tab overflow), 5.1 (lede burial) | High | Medium |
| **P2 — Accessibility** | 6.1 (ARIA), 6.3 (contrast), 6.2 (skip link), 6.4 (print stylesheet) | Critical for compliance | Medium |
| **P3 — Polish** | 1.4 (expert block distinction), 2.2 (line length), 4.4 (chevron visibility), 4.5 (expand all) | Medium | Low |
| **P4 — Low Priority** | 1.2 (layout consistency), 1.3 (tab indicator), 2.3 (footnote size), 3.2 (heatmap palette), 3.3 (provider colors), 3.4 (scale note), 4.2 (table filters), 5.2 (block consistency), 5.3 (vote tallies), 5.4 (peer review links), 6.5 (fonts), 6.6 (loading state) | Low-Medium | Varies |

---

## Quick Wins (Implementable in < 30 minutes total)

1. **Cross-tab links** (Issue 4.1): Add `onclick` handlers to tab references in HTML
2. **CSS figure numbering** (Issue 5.5): 2 lines of CSS using counters
3. **ECharts toolbox** (Issue 4.3): Add to `baseTheme()` in charts.js
4. **Contrast fix** (Issue 6.3): Change one CSS variable value
5. **Heatmap scale note** (Issue 3.4): Add one sentence to chart description
6. **Chevron visibility** (Issue 4.4): Increase size and change color in app.js

---

## Commendations

The council also identified several design strengths worth preserving:

1. **Tab-explainer pattern** — The What/How/Key three-section introduction on every tab is an excellent onboarding mechanism. No tab leaves the reader without context.
2. **Expert analysis blocks** — The colored left-border + discipline attribution is an effective way to add interpretive depth without overwhelming the charts.
3. **Expandable findings** — The progressive disclosure pattern on Tab 10 perfectly balances scanability (subtitles) with depth (detail paragraphs).
4. **Peer review concerns as living audit trail** — The color-coded status badges with resolution text transform a static list into an accountability mechanism.
5. **Dark theme execution** — The palette is cohesive and the gradient header + blue accent create a professional feel appropriate for an academic dashboard.
6. **Fat-data architecture** — Pre-computing all analytics in Python and shipping as JS constants eliminates client-side computation, ensures reproducibility, and makes the dashboard trivially deployable on GitHub Pages.

---

*Reviewed: 2026-04-05 | 12-perspective interdisciplinary council*
*Dashboard: NormEval v10, 10 tabs, 54 benchmarks, 9-model / 3-vendor replication*
