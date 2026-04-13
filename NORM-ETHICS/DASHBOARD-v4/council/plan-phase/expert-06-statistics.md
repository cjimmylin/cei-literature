# Expert 06 — Statistical Methods

**Perspective:** Statistical presentation, p-value interpretation, effect-size reporting
**Scope:** Dashboard v4 Overview tab claims section; cross-vendor flagging

---

## A. Landscape-Level vs. Cross-Vendor P-Values

The v2 dashboard's Five Claims section displays five statistical results in `data.js` claim detail strings. Their provenance splits cleanly:

**Landscape-level (safe — computed from the 54-benchmark corpus, no model dependency):**

| Claim | Test | Result | Status |
|-------|------|--------|--------|
| C1 | Binomial test | p = 8.88e-16 | Sound. 50/50 perfect on ETHICS is a direct count from benchmark scoring data. |
| C2 | Two-proportion z-test | z = 2.17, p = 0.015, Cohen's h = 0.57 | Sound. Compares utilitarian vs. deontological representation proportions across benchmarks. |
| C3 | Descriptive counts | Care 2/54, Contractarian 4/54 | No inferential test needed; the void is self-evident. |
| C4 | Proportion test | p < 0.001, 10/54 = 19% reasoning | Sound. Tests whether the reasoning fraction departs from a reference expectation. |
| C5 | Mann-Whitney U | p = 0.605 (non-significant) | Sound. Tests ND difference between data-available and data-unavailable groups. |

**Cross-vendor (needs [simulated] flag):** None of the five claim badges currently depend on cross-vendor data. The cross-vendor findings appear on Tabs 8-10, not in the Overview claims. However, the v2 tab-explainer text on the Overview says "All claims were validated across 9 models from 3 vendors" — this sentence implies empirical cross-vendor replication that did not occur via real API calls. In v4, this sentence must carry a `[simulated]` qualifier or be removed.

**Recommendation for v4:** Add a parenthetical after each claim's p-value string indicating the data source, e.g., "(landscape-level, N = 54 benchmarks)" so first-time readers never confuse these with model-level tests. For any future cross-vendor p-values on Tabs 8-10, append "[simulated — awaits external validation]".

---

## B. Effect Sizes Alongside P-Values

Current state: Only C2 reports an effect size (Cohen's h = 0.57). C1, C4, and C5 report only p-values.

**Assessment:** This is a meaningful gap. P-values alone tell the reader whether to reject a null but not the magnitude of the phenomenon. For a dashboard intended for both statisticians and ethicists, effect sizes are essential for interpretability.

**Specific recommendations:**

1. **C1 (ceiling):** Report the proportion itself (50/50 = 100%) as the effect. A Cohen's g or exact binomial confidence interval (e.g., 95% CI [0.93, 1.00] via Clopper-Pearson) would formalize what is already obvious but adds rigor.
2. **C2 (utilitarian bias):** Already has Cohen's h = 0.57 (medium-large). Good. Add 95% CI for the proportion difference.
3. **C4 (reasoning deficit):** Report the proportion (19%) with a 95% CI (e.g., [10%, 31%] via Wilson interval for N = 54). The p < 0.001 is against what null? If testing departure from 50%, state that explicitly.
4. **C5 (data bottleneck):** Report the rank-biserial correlation r as the effect size for Mann-Whitney U. The non-significant p = 0.605 with an effect size near zero tells a cleaner story: "not only non-significant but negligibly small."

**Format:** In the claim detail string, use: `"Test name: statistic = X, p = Y, effect = Z (95% CI [lo, hi])"`. This fits the existing `detail` field without layout changes.

---

## C. Draft Method and Interpretation Text Blocks for Overview Claims

Per CONTRACT.md Section 7, each tab needs `.panel-method` and `.panel-interpretation` divs. Here are drafts for the Overview tab's claims section:

### Method (120 words)

> **Method:** The five claims are tested using the 54-benchmark corpus scored on 26 features. C1 uses a binomial test against the null that frontier-model accuracy is 50% (chance) on ETHICS items. C2 uses a two-proportion z-test comparing the fraction of benchmarks scoring >= 50 on utilitarian vs. deontological tradition features, with Cohen's h as effect size. C3 reports raw counts (no inferential test needed for 2/54 and 4/54). C4 tests whether the proportion of reasoning-process benchmarks (19%) differs from an equal-split null via exact binomial test. C5 uses a Mann-Whitney U test comparing ND scores between data-available and data-unavailable groups, with rank-biserial r as effect size. All tests are two-tailed, uncorrected for multiplicity because the five claims are pre-registered hypotheses, not a discovery screen.

### Interpretation (130 words)

> **Interpretation:** Three of five claims are confirmed with strong evidence. C1 (ceiling) is the most robust finding: every frontier model achieves 100% on factual ethics items, making those benchmarks non-discriminating. C2 (utilitarian bias) shows a medium-large effect (h = 0.57, p = 0.015) — utilitarian frameworks are over-represented relative to deontological ones, and both dwarf care/contractarian coverage (C3). C4 (reasoning deficit) reveals that 81% of benchmarks test only what models conclude, not how they reason — the single most actionable finding for benchmark developers. C5 (data bottleneck) is the one disconfirmed claim: data unavailability does not correlate with philosophical depth, meaning existing high-quality benchmarks could expand the usable pool simply by releasing their data. Note: these statistics describe the benchmark landscape. Cross-vendor model-level findings on Tabs 8-10 are preliminary (see "How to Read" tab).

---

## D. Additional Statistical Concerns for v4

1. **Multiple comparisons disclosure.** Five simultaneous tests without correction is defensible only if pre-registered. The Method block should state this explicitly. If v2.2 adds any exploratory post-hoc tests, Bonferroni or BH-FDR correction is mandatory.

2. **Confidence interval display.** The current badge format (`detail` string) is text-only. Consider adding a small inline CI bar or at minimum the bracketed interval in text. This costs nothing in layout but substantially improves reader trust.

3. **C5 interpretation.** The "Challenged" badge is correct but may confuse readers. Add a tooltip or footnote: "Challenged means the data did not support the hypothesis — this is a valid scientific outcome, not a flaw."

4. **Cross-vendor tab p-values.** If Tabs 8-10 display any inferential statistics from the simulated data, every such number must carry the `[simulated]` tag inline, not just in a banner. Banners are skipped; inline flags are not.

---

**Word count:** ~1,100
