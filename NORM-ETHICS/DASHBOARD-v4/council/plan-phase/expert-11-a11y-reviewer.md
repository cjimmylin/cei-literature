# Expert 11 — Accessibility Reviewer

**Perspective:** Accessibility and progressive disclosure  
**Scope:** Dashboard v4 usability heuristics (5 explicit questions)  
**Date:** 2026-04-13

---

## (a) Can a reader answer "what does ND mean?" within 60 seconds of landing on the guide tab?

**Verdict: Likely YES in v4, but only if the guide tab delivers on its promise.**

In v2, the answer is buried. The Overview tab's `.tab-explainer` block mentions "Normative Depth (ND)" in passing on line 93 of `index.html`, embedded inside a dense paragraph that also introduces PE and CI. A reader must parse 80+ words of surrounding context to extract the definition. There is no glossary, no anchor link, no tooltip.

The v4 CONTRACT specifies Tab 0 (`tab-guide`, "How to Read This Dashboard") as a framework explainer with a glossary. If the glossary defines ND as a standalone entry with a one-sentence definition and the colored badge used elsewhere (the blue `axis-nd` badge from CSS), a reader can find it within 60 seconds via Ctrl+F or visual scan. However, the contract does not mandate alphabetical ordering or a dedicated `<dl>` element for the glossary. **Recommendation:** The guide tab implementation should include a visually distinct glossary section using a `<dl>` (definition list) with `id="glossary"` and anchor links from the nav. Each term (ND, PE, CI, gate, composite) should be a `<dt>` with the colored axis badge inline. This makes both visual scanning and Ctrl+F reliable.

**Risk if not implemented:** Readers will land on the guide tab, see the preliminary banner (which is mandated as the FIRST element), then a wall of prose, and still not find "ND" quickly.

## (b) Can they navigate from landing tab to a specific framework's results in under 3 clicks?

**Verdict: YES — 2 clicks is achievable, but the path is not obvious.**

Click 1: Tab 4 ("Tradition Coverage") from the nav bar. Click 2: Visual scan of the bar chart to find the target framework. That is 2 clicks (tab click + no further click needed to see results). Alternatively, Tab 2 ("All Papers") with a filter-by-tradition dropdown would also be 2 clicks.

The problem is discoverability. The tab labels "Tradition Coverage" and "All Papers" are domain jargon. A reader looking for "what does the dashboard say about care ethics?" might not know to click "Tradition Coverage." The v2 nav bar has 10 tabs (v4 will have 11) in a horizontally scrolling strip at 0.8rem font size. On mobile, rightmost tabs (Cross-Model, Gaps, Cross-Vendor) require horizontal scrolling to even see.

**Recommendation:** Add brief tooltip text (`title` attribute) on each tab link, e.g., `title="How benchmarks cover 5 ethical traditions"` for Tradition Coverage. Also consider a "jump to" dropdown in the guide tab that maps common questions to specific tabs.

## (c) Does the tab order make logical sense for progressive disclosure?

**Verdict: MOSTLY YES, with one structural concern.**

The v4 order is: Guide (0) -> Overview (1) -> All Papers (2) -> Feature Matrix (3) -> Tradition Coverage (4) -> Composite Scoring (5) -> Trials (6) -> Data Availability (7) -> Cross-Model (8) -> Gaps (9) -> Cross-Vendor (10).

This follows a reasonable pattern: orientation -> summary -> data -> analysis -> replication -> gaps. The Guide tab as Tab 0 is the correct addition for v4. The progression from Overview (high-level claims) to All Papers (browse the data) to analytical tabs (Features, Traditions, Composite) to empirical validation (Trials, Cross-Model) to gaps is sound.

**Structural concern:** Tabs 8 (Cross-Model) and 10 (Cross-Vendor) are separated by Tab 9 (Gaps). A reader moving through replication evidence would expect Cross-Model and Cross-Vendor to be adjacent. Gaps is a "what's missing" tab that conceptually belongs after the analytical tabs (4-5) or at the very end. Suggested reorder: move Gaps to Tab 10 (or Tab 7, after Data Availability, since gaps are a data-availability story) and keep Cross-Model (8) and Cross-Vendor (9) adjacent.

However, given that cross-vendor data is flagged as preliminary/simulated, placing it last (Tab 10) creates a natural "proceed with caution" boundary. This is actually a defensible accessibility choice — the most uncertain data comes last. Keep the current order but add a visual separator (e.g., a subtle divider or color shift in the tab bar) between Tab 8 and Tabs 9-10.

## (d) Are the Background/Method/Interpretation blocks (80-150 words each) the right length?

**Verdict: 80-150 words is appropriate for Background and Interpretation; Method may need 150-200 for some tabs.**

The contract mandates 80-150 words for each of three blocks. At 0.88rem font size (the `.tab-explainer` size in CSS), 150 words renders to roughly 6-8 lines on desktop, which is scannable without scrolling. This is a good length for Background (context-setting) and Interpretation (what to notice).

However, Method blocks for complex tabs (Feature Matrix, Composite Scoring) may need to explain the scoring formula, the 26-feature codebook, and the weighting rationale. The v2 Overview explainer already runs to ~180 words for a combined block. Splitting into three 80-word blocks would lose coherence for methodologically dense tabs.

**Recommendation:** Keep 80-150 for Background and Interpretation. Allow Method blocks up to 200 words for tabs 3 (Feature Matrix) and 5 (Composite Scoring), where the scoring formula itself consumes 30-40 words. For simpler tabs (Data Availability, Gaps), Method can be as short as 50 words. Add a collapsible "show more" affordance if any block exceeds 150 words, so the default view stays compact.

## (e) Is the font size readable on mobile?

**Verdict: BORDERLINE — several elements fall below WCAG minimum recommendations.**

Key font sizes from `style.css`:

| Element | Size | Mobile Override | Assessment |
|---------|------|----------------|------------|
| Body text | inherits Bootstrap (~1rem/16px) | None | OK |
| Tab explainer | 0.88rem (14.1px) | None | Marginal |
| Tab labels | 0.8rem (12.8px) | None | **Too small** |
| Table cells | 0.8rem (12.8px) | None | **Too small** |
| Table headers | 0.7rem (11.2px) | None | **Too small** |
| Metric labels | 0.75rem (12px) | None | **Too small** |
| Expert analysis | 0.85rem (13.6px) | None | Marginal |
| Severity badges | 0.65rem (10.4px) | None | **Too small** |
| Footnotes | 0.78rem (12.5px) | None | **Too small** |

The `@media (max-width: 768px)` block only adjusts padding and metric-value font size. It does not increase any of the small text sizes. WCAG 2.1 SC 1.4.4 requires text to be resizable to 200% without loss of content, but the practical recommendation for mobile is a minimum of 14px (0.875rem) for body text and 12px (0.75rem) absolute minimum for labels.

**Table headers at 0.7rem (11.2px) and severity badges at 0.65rem (10.4px) are below the 12px floor.** On a typical mobile viewport (375px), these are nearly illegible without pinch-zoom.

**Recommendation:** Add mobile-specific overrides in the `@media (max-width: 768px)` block:
- `.nav-tabs .nav-link`: bump to 0.85rem
- `table.papers-table th`: bump to 0.75rem
- `table.papers-table td`: bump to 0.85rem
- `.severity-badge`, `.gate-badge`, `.version-badge`: bump to 0.72rem
- `.tab-explainer`, `.expert-analysis`: bump to 0.92rem
- `.footnote`: bump to 0.82rem

Also add `touch-action: manipulation` on interactive elements to eliminate the 300ms tap delay on older mobile browsers.

---

## Summary of Recommendations (Priority Order)

1. **P0 — Mobile font sizes:** Add `@media (max-width: 768px)` overrides for all sub-14px text. Several elements are below the 12px accessibility floor.
2. **P0 — Guide tab glossary:** Implement as a `<dl>` with `id="glossary"`, colored axis badges, and anchor link from nav. This is the single highest-impact accessibility addition.
3. **P1 — Tab tooltips:** Add `title` attributes to all nav links explaining each tab's content in plain language.
4. **P1 — Method block flexibility:** Allow up to 200 words for Feature Matrix and Composite Scoring method blocks; add collapsible overflow.
5. **P2 — Tab order refinement:** Consider moving Gaps adjacent to Data Availability, or add a visual separator before the cross-vendor cluster.
6. **P2 — Skip navigation:** The v2 skip link targets `#mainTabContent`. Verify the v4 guide tab content is within this target, or add a second skip link for `#tab-guide`.
