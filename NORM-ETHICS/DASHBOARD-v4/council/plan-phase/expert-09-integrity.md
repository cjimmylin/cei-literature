# Expert 09 — Research Integrity Review

**Perspective:** Research integrity, transparent reporting, responsible data visualization  
**Scope:** Preliminary-data disclosure adequacy in Dashboard v4  
**Date:** 2026-04-13

---

## (a) CONTRACT Section 8 Banner Wording: Honest Enough?

The banner text in CONTRACT.md Section 8 is substantively honest. It names the exact models affected, identifies the methodology ("in-context elicitation by a Codex sub-agent"), distinguishes this from direct API calls, and explicitly states the results do not constitute empirical evaluation. The closing sentence — "Claude's elicited model of cross-vendor variation, not direct measurements" — is a clear, non-euphemistic framing that a reviewer or reader can act on.

**Two concerns remain:**

1. **The word "appropriate" is a judgment call the authors should not make for the reader.** The phrase "This methodology is appropriate for exploratory hypothesis generation" pre-empts the reader's assessment. Replace with a neutral description: "This methodology generates exploratory hypotheses that require external replication." The reader can decide appropriateness.

2. **"An external replication using non-Anthropic APIs is in progress" implies imminent resolution.** If the timeline is uncertain, this creates a promissory note that may not be honored before the dashboard circulates. Recommend changing to: "External replication using non-Anthropic APIs is planned but not yet complete." This is more accurate and less likely to be read as a credibility guarantee.

**Verdict:** The banner is substantially adequate. With the two wording fixes above, it meets the standard expected by journals such as Nature Human Behaviour or PNAS for preliminary/simulated data disclosure.

---

## (b) Does the Cross-Vendor Tab Need Its Own Banner?

**Yes — emphatically.** The current v2 Cross-Vendor tab (tab 10) has zero disclosure of the simulated provenance. A user who navigates directly to tab 10 via a shared URL anchor, a paper citation, or the tab bar will encounter:

- KPI cards stating specific numeric values (e.g., "90.4% agreement," "IH=2.93," "kappa=0.72") with no qualification
- Expert analysis panels attributing behavior to GPT-5 and Gemini as though empirically measured
- A footnote (line 708) that mentions "Codex agent wrapper" for GPT-5/GPT-5-mini but frames it as a minor methodological note about "additional conservatism," not as a fundamental provenance disclosure

The CONTRACT already anticipates this: Section 8 says "Also repeated (compact version) at the top of #tab-crossvendor." This plan is correct and must be enforced. A reader who lands on tab 10 without visiting tab 0 must encounter the disclosure before any chart renders visually.

**Placement recommendation:** The compact banner should be the FIRST child element inside `#tab-crossvendor`, before the `.tab-explainer` div. It should use the same `.preliminary-banner` class (yellow background, role="alert") for visual consistency with the landing tab.

---

## (c) Unqualified Factual Claims in v2

The v2 Cross-Vendor tab contains multiple instances where simulated data is presented as established fact:

1. **Tab 1 (Overview), line 40:** "Cross-vendor replication (9 models, 3 providers) confirms these findings are not artifacts of a single model" — the word "confirms" asserts empirical validation that did not occur.

2. **Tab 1 (Overview), line 42:** "All claims were validated across 9 models from 3 vendors" — same issue; "validated" implies real API testing.

3. **Tab 8 (Cross-Model), line 620:** "The within-family scaling pattern is not Claude-specific. GPT-5 (IH=2.93) and Gemini models (IH=4.47) fall into the same Conservative/Permissive gradient, confirming that alignment intensity — not vendor origin — determines ethical posture." This is the most problematic sentence in the dashboard. It uses "confirming" to assert a cross-vendor empirical finding based entirely on simulated data.

4. **Tab 10, line 698:** "Training philosophy matters more than model family for ethical judgment" — stated as the "Key conclusion" without any caveat that the non-Anthropic data is simulated.

5. **Tab 10, line 736 (Expert Analysis):** Calculates the probability of Gemini identity at "10^-103" and discusses "falsifying the independent-inference hypothesis" — this is a statistical claim about real Google infrastructure derived from simulated data.

6. **Tab 10, line 738:** Cohen's kappa values (0.72, 0.18) reported as though computed from empirical item-level data.

7. **Tab 10, line 784 (Expert Analysis):** "When a hospital selects an AI vendor, they are implicitly selecting a moral profile" — policy recommendation derived from simulated data without disclosure.

**Recommendation for v4:** Every cross-vendor numeric value, finding label (F1-F7), and expert analysis panel on tabs 1, 8, and 10 must carry an inline `[simulated]` tag or be wrapped in a clearly styled container indicating preliminary status. The seven findings list should have a header: "Findings below are based on in-context elicitation, not direct API testing."

---

## (d) Proposed Cross-Vendor Tab Banner (2 sentences)

> **Preliminary Data Notice.** All non-Anthropic results on this tab (GPT-5, GPT-5-mini, Gemini 2.5 Flash, Gemini 2.5 Flash-Lite, Gemini 2.5 Pro, Gemini 3.1 Pro) were generated through in-context elicitation by a Claude sub-agent, not through direct API calls to OpenAI or Google. These findings represent exploratory hypotheses about cross-vendor variation and require independent replication before being cited as empirical measurements.

This is 63 words. It omits the methodology explanation (available on tab 0 for interested readers) and focuses on the two facts a tab-10 visitor must know: (1) the data source is simulated, and (2) the results are not citable as empirical evidence.

---

## Summary of Recommended Actions

| Priority | Action | Location |
|----------|--------|----------|
| P0 | Add compact `.preliminary-banner` as first child of `#tab-crossvendor` | Tab 10 |
| P0 | Replace "confirms" / "validated" with "suggests" / "explored" in tabs 1, 8, 10 | Tabs 1, 8, 10 |
| P0 | Remove "appropriate for exploratory hypothesis generation" judgment from landing banner | Tab 0 (Section 8) |
| P1 | Add `[simulated]` inline tags to all cross-vendor KPI cards and expert analysis panels | Tab 10 |
| P1 | Change "in progress" to "planned but not yet complete" in landing banner | Tab 0 (Section 8) |
| P2 | Add `[simulated]` to the cross-vendor reference in Tab 8 expert analysis (line 620) | Tab 8 |
| P2 | Add `[simulated]` to Overview tab claims referencing cross-vendor validation | Tab 1 |

All P0 items are blockers for responsible deployment of v4.
