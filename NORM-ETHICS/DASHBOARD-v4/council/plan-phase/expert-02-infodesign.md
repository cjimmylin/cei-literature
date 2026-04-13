# Expert 02 — Information Design Analysis

**Perspective:** Information design (Tufte/Munzner tradition)
**Scope:** Chart/caption/interpretation triads, visual hierarchy, Tab 0 content, preliminary banner

---

## (a) Chart-to-Text Ratio by Tab

The v2 dashboard has a persistent text-heaviness problem. Every tab follows a pattern of ~300-word explainer block, then chart(s), then a 200-400 word expert analysis block. On several tabs, the text-to-chart pixel ratio exceeds 1:1, which inverts the purpose of a dashboard.

**Tab-by-tab assessment:**

- **Tab 1 (Overview):** Acceptable. KPI cards and donut chart are above the fold; the 5 Claims block is compact. The expert analysis (~250 words) sits below the charts. The tradition frequency bar at the bottom is easy to miss after the long expert block.
- **Tab 2 (All Papers):** The explainer + expert analysis together exceed 500 words before and after a single table. The table itself is well-designed (sparkbars, tradition dots, gate badges). Ratio: roughly 60% text, 40% data. Invert this.
- **Tab 3 (Feature Matrix):** The heatmap is the star, but it is sandwiched between a 250-word explainer above and a 450-word expert analysis below, plus a full feature reference table with its own 350-word expert block. Total text mass on this tab approaches 1,000 words for two visual elements.
- **Tab 5 (Composite Scoring):** The scoring equation box and rationale box are effective — they are structured content, not paragraph prose. But the 400-word council expert analysis between the formula and the scatter plots breaks the visual flow. A reader looking at the equation wants to see its effect (the scatter plot) immediately.
- **Tab 6 (Trials):** Reasonable ratio. Two charts side-by-side, a detail table, one expert block. The detail table carries most of the information load.
- **Tabs 8-10 (Cross-Model, Gaps, Cross-Vendor):** Each has 4-6 chart containers plus 300-500 words of expert analysis. These are the best-balanced tabs in v2.

**Recommendation for v4:** Collapse the three-part explainer (Background/Method/Interpretation per CONTRACT.md section 7) into a single collapsible `<details>` element, defaulting to closed. Show only the Interpretation block by default — it is the only one a returning user needs. First-time users can expand. This alone would halve the visible text mass on every tab.

## (b) Visual Hierarchy

The v2 hierarchy is: header > tab bar > explainer text > charts > expert analysis. This is backwards for a dashboard. The correct hierarchy is: header > tab bar > charts > captions > supporting text.

**Specific problems:**

1. **Explainer blocks appear above charts.** The `.tab-explainer` with its blue left border visually outweighs the chart below it — higher contrast, more vertical space, positioned first in DOM order. The eye reads the explainer before seeing any data. Tufte's principle: show the data first, explain second.

2. **Expert analysis blocks compete with charts.** The purple left-border `.expert-analysis` panels are nearly the same visual weight as `.chart-container` panels. Both have colored left borders, similar padding, similar font size. A reader scanning the page cannot instantly distinguish "this is data" from "this is commentary."

3. **KPI cards lack hierarchy within the overview.** All six cards have equal visual weight (same size, same padding, same font). The two most important numbers — 54 benchmarks and 24 pass rate — should be visually dominant over secondary metrics.

4. **Figure numbering resets per tab** (via CSS counter). This is correct for tab navigation but creates ambiguity in print mode where all tabs render sequentially. Tab 4's "Fig. 1" and Tab 5's "Fig. 1" collide.

**Recommendation for v4:** Move explainer text below charts or into a collapsible panel. Reduce expert analysis font size to 0.78rem (currently 0.85rem) and mute the border to 1px instead of 3px. Add a visual "data zone" with slightly elevated background to chart areas so the eye goes there first.

## (c) Tab 0 — "How to Read This Dashboard"

Per the contract, Tab 0 is new in v4 and must contain the preliminary banner, a framework explainer, and a glossary. Based on information design principles, the content should be ordered by declining urgency and increasing reference-character:

**Recommended structure and order:**

1. **Preliminary data banner** (the yellow `.preliminary-banner` per CONTRACT.md section 8) — first element, non-dismissible, ~80 words. This is the most time-sensitive content on the entire dashboard.

2. **One-paragraph orientation** (~60 words): What is NormEval, what are the 54 benchmarks, what is the ND/PE/CI framework. No more than three sentences. Link to the paper.

3. **Visual framework diagram** (static image or simple ECharts sankey/flow): Show ND/PE/CI flowing into Composite, with the two gates as filters. This replaces 200+ words of prose. A single diagram communicates the scoring system faster than any text block.

4. **Reading path suggestion** (~40 words): "Start with Overview (Tab 1) for the five claims. Use All Papers (Tab 2) to explore individual benchmarks. Tabs 3-7 provide supporting evidence. Tabs 8-10 cover cross-model replication."

5. **Glossary** (definition list, ~15 terms): ND, PE, CI, gate, composite, tradition, ceiling effect, discriminative power, IH, CBR, knowledge item, judgment item, refusal rate. Use `<dl>/<dt>/<dd>` markup. Keep each definition under 20 words.

6. **Color legend**: The three axis colors (blue=ND, green=PE, orange=CI) plus the five tradition colors. Show as a compact swatch strip, not a paragraph.

**What to exclude from Tab 0:** Do not repeat the full scoring formula (that belongs on Tab 5). Do not include expert analysis panels — Tab 0 is infrastructure, not argumentation. Do not put a table of contents; the tab bar already serves that function.

## (d) Preliminary Banner Prominence

The CONTRACT.md specifies a yellow `.preliminary-banner` with `role="alert"`. The current specification is appropriate in content but needs calibration on two axes:

**Visual prominence — currently adequate.** A yellow background on a dark-theme dashboard creates strong contrast. The bold warning icon and "Important Notice" heading establish urgency. The two paragraphs (~100 words) are short enough to read in 15 seconds.

**Alarm fatigue risk — moderate.** Two concerns:

1. The banner appears on Tab 0 (full version) AND Tab 10 (compact version). This is correct — the cross-vendor tab is where the simulated data actually appears. However, if a user who read Tab 0 then navigates to Tab 10, the second banner feels redundant. Solution: make the Tab 10 compact version a single sentence with a link back to Tab 0 for details: "Cross-vendor results are preliminary — details on the Guide tab."

2. The banner uses persistent yellow, which is appropriate for "preliminary" status. Do NOT use red — that would signal "error/danger" when the actual status is "valid-but-provisional." Do NOT use a dismissible banner — the information remains true for the entire session.

**One addition:** Add a small `[simulated]` inline tag (subtle, not a banner) next to every chart title on Tabs 8-10 that renders simulated cross-vendor data. This follows Tufte's "smallest effective difference" principle — the main banner establishes the context once, and the inline tags maintain awareness without repeating the full disclosure.

---

## Summary of Priority Recommendations

| Priority | Issue | Fix |
|----------|-------|-----|
| P0 | Explainer text appears above charts | Move below or collapse by default |
| P0 | Tab 0 content ordering | Banner > orientation > diagram > reading path > glossary > color legend |
| P1 | Expert analysis competes visually with charts | Reduce font, mute border, or collapse |
| P1 | Cross-vendor `[simulated]` inline tags | Add to chart titles on Tabs 8-10 |
| P2 | Tab 10 compact banner is too long | Reduce to one sentence with link |
| P2 | Figure numbering collides in print | Prefix with tab number: "Tab 4, Fig. 1" |
| P2 | KPI cards lack internal hierarchy | Make top 2 cards visually dominant |
