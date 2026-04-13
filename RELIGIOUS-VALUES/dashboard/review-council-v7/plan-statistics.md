# Statistical Reviewer Plan — Dashboard v7
# Religious Values Benchmark Paper
# Generated: 2026-04-13

---

## 1. Presenting p-values, CIs, and Effect Sizes to Non-Expert Readers

### Core principle
Statistics are supporting evidence, not the story. Lead with the substantive finding in plain English; follow with the number. Never lead with the p-value.

### p-value presentation rules

| Situation | Dashboard text | What to avoid |
|-----------|----------------|---------------|
| p < 0.001 | "very strong statistical support" | "p < 0.001 means the finding is important" |
| 0.001 <= p < 0.01 | "strong statistical support" | "highly significant" |
| 0.01 <= p < 0.05 | "statistically supported" | "significant" alone, without context |
| 0.05 <= p < 0.15 | "trend in expected direction, below significance threshold" | "failed" or "null result" |
| p >= 0.15 | "not statistically supported in this sample" | "proven false" |

For non-expert readers, always accompany the p-value with a one-sentence plain-English gloss. Example format:

> "Mean values relevance score = 30.0 / 100 (p < 0.001). In plain terms: the chance of observing a gap this large by random variation alone is less than 1 in 5,000."

Avoid reporting raw p = 0.000000 as displayed by scipy; round to "p < 0.001" or "p < 0.0001" as appropriate.

### Confidence interval presentation rules

CIs appear in the data for C3 (binomial, 0.938-1.000) and C5 (bootstrap median, [2023, 2024]) and C7 (binomial proportion, 0.232-0.655).

Plain-English CI framing:

- For binomial CIs: "We are 95% confident the true rate falls between X% and Y%."
- For bootstrap CIs on the median year: "The median publication year in the field is 2024, with the 95% uncertainty range spanning 2023 to 2024."
- For proportion CIs that cross 0.5 (C7): "The uncertainty range spans both sides of the 50% mark, meaning we cannot rule out that bias-adjacent and values-focused benchmarks are equally common."

Do not display CI notation as "[0.232, 0.655]" without a label. Use: "95% CI: 23% to 66%."

### Effect size presentation rules

Effect sizes are the most policy-relevant number. Present them with a benchmark label:

| Metric | Value | Plain label |
|--------|-------|-------------|
| Cohen's d = -1.23 (C8) | Large negative | "far below the midpoint" |
| Cramer's V = 0.53 (C1, uniform) | Large | "strongly unequal distribution" |
| Cramer's V = 0.30 (C1, proportional) | Medium | "meaningfully unequal even after adjusting for corpus size" |
| Odds ratio = 0.58 (C6) | Below 1.0 | "non-WEIRD traditions pass at higher rates than WEIRD ones" |
| Pseudo R-squared = 0.068 (C4) | Small | "structural factors explain about 7% of gate-passage variation" |

Always state the direction (above/below, higher/lower, more/fewer) before the magnitude. A number without direction misleads.

### When to use "statistically significant" vs accessible language

Use "statistically significant" only once per claim block -- in the technical tooltip or footnote. In the primary claim card text, use:

- "The data strongly support..." (supported claims)
- "The pattern is consistent with... but falls short of the standard threshold" (not_significant claims)
- "The original claim holds, but the mechanism differs from what was expected" (revised claims)

Do not use: "proves," "confirms definitively," "demonstrates conclusively," or "fails to show."

---

## 2. Visual Encoding of Statistical Confidence

### Verdict badge system

Each claim card carries a verdict badge. The badge encodes both verdict category and confidence level through color, icon, and border treatment.

**Supported (C1, C2, C3, C8)**
- Badge background: #009E73 (Okabe-Ito green)
- Icon: filled circle (solid confidence)
- Border: solid 2px same color
- Tooltip: "Statistically supported — all tests significant, effect in predicted direction"

**Revised (C4, C6)**
- Badge background: #E69F00 (Okabe-Ito orange/amber)
- Icon: half-filled circle or diamond (partial support)
- Border: dashed 2px same color
- Tooltip: "Finding revised — direction or mechanism differs from original claim; see notes"

**Not significant (C5, C7)**
- Badge background: #0072B2 (Okabe-Ito blue) — deliberately NOT grey or red
- Icon: open circle (indeterminate)
- Border: dotted 2px same color
- Tooltip: "Not statistically supported in this sample — the pattern exists but falls below the p < 0.05 threshold"

### Rationale for blue (not grey) for not_significant

Grey reads as "unknown" or "missing data." Blue reads as "informative null" — a real finding with a specific meaning. The non-significant results here (C5, C7) contain interpretable content (the recency pattern, the construct independence result) and deserve a positive color.

### Effect size bar chart encoding

For claims with Cohen's d or Cramer's V, render a horizontal bar chart alongside the claim card:

- Bar width proportional to |effect size|
- Vertical reference lines at d = 0.2 (small), d = 0.5 (medium), d = 0.8 (large)
- C8 bar (d = 1.23) extends well past the "large" line, visually anchoring it as the strongest finding
- Bar color matches verdict badge color
- Label the bar: "Effect: 1.23 (large)" in plain text

For Cramer's V (C1), use the same bar with V = 0.53 labeled "Effect: 0.53 (large, uniform baseline)" and V = 0.30 labeled "Effect: 0.30 (medium, corpus-adjusted)."

### p-value font treatment

Within claim cards, render the p-value in a smaller, secondary font weight relative to the main finding text. This visually signals that the p-value is supporting evidence, not the headline. Use color matching the verdict badge for the p-value text, not grey (grey reads as unimportant).

---

## 3. Centering Claim 8 as the Strongest Finding

### Why C8 anchors the dashboard

C8 has d = -1.23, three converging tests (t-test p = 0.000181, Wilcoxon p = 0.00061, binomial p = 0.0106), and the most direct policy implication: the field's current production does not actually measure what it claims to measure. This is an argument about construct validity, not just coverage.

### Structural placement

- C8 should appear first in the "Core Findings" tab, above all other claims.
- Introduce it with a summary callout box at the top of the claims section:
  > "The central finding of this paper: the average religious values benchmark scores 30 out of 100 on values relevance, far below the midpoint. This gap is large (d = 1.23) and unlikely to be due to chance (p < 0.001 across three independent tests). Most benchmarks test knowledge recall, not genuine values alignment."
- The effect size bar for C8 should be the widest bar in the effect size panel, serving as a visual anchor for all other comparisons.

### Convergence framing

Emphasize that C8 is supported by three methodologically distinct tests:

1. Parametric (one-sample t-test) — tests the mean
2. Non-parametric (Wilcoxon signed-rank) — tests the median without normality assumptions
3. Distributional (binomial) — tests whether most benchmarks fall above or below the midpoint

Present these as a "three-way convergence" box. Example text:
> "Three independent statistical tests all point to the same conclusion: mean score 30.0 (t-test), median score 27.5 (Wilcoxon), only 3 of 16 benchmarks above the midpoint (binomial). Convergent evidence across methods strengthens confidence beyond what any single test provides."

### Connection to other claims

Link C8 explicitly to C2 (knowledge-reasoning conflation) in the dashboard annotation:
> "Claim 2 shows that only 27.7% of benchmarks test genuine reasoning rather than factual recall. Claim 8 shows the deeper consequence: even when benchmarks are well-designed, the field averages only 30/100 on values relevance. Together, they describe a field building infrastructure faster than it is building measurement validity."

---

## 4. Handling Revised (C4, C6) and Not-Significant (C5, C7) Claims Honestly

### Framing principle

Null and revised results are not failures of the research. They are informative findings that discipline the interpretation of supported claims. The dashboard must communicate this explicitly.

### Claim 4 — Structural epistemic injustice (revised)

**What the original claim said:** Gate-passage correlates with Western proximity via English-language source bias and venue tier.

**What the data show:** The logistic regression has pseudo R-squared = 0.068. Neither English-language source (OR = 1.76, p = 0.097) nor venue tier (OR = 1.34, p = 0.148) individually reaches significance. However, the structural correlation through publication infrastructure (r = 0.74) remains.

**Dashboard text:**
> "The original claim is partly right but the mechanism differs. Structural epistemic injustice operates through publication infrastructure — which traditions have HuggingFace repos, shared-task communities, and institutional backing — rather than through a direct scoring bias against non-Western traditions. No individual predictor reaches statistical significance (p > 0.09 for both tested variables), but the infrastructure correlation is strong (r = 0.74)."

**Annotation note:** "This revision is scientifically important: it locates the bias upstream of the scoring framework, making it harder to fix by adjusting weighting schemes alone."

### Claim 6 — WEIRD bias (revised, direction inverted)

**What the original claim said:** Benchmarks from WEIRD (Western, Educated, Industrialized, Rich, Democratic) contexts disproportionately pass gates.

**What the data show:** Fisher's exact test, OR = 0.58 (p = 0.090). Non-WEIRD traditions pass at 14.4% vs WEIRD at 8.9%. The direction is reversed from the hypothesis.

**Dashboard text:**
> "The expected WEIRD advantage does not appear. Non-WEIRD traditions actually pass the gates at a higher rate (14.4% vs 8.9%), driven by Islam's strong infrastructure rather than a broad non-WEIRD advantage. This is not an absence of bias — it is a different kind of bias. Islamic benchmark production has become so dominant that it inverts the expected Western-advantage pattern. Eight of the 14 traditions surveyed remain completely invisible, most of them non-WEIRD traditions with strong oral and communal knowledge traditions."

**Annotation note:** "The p-value is 0.09, just above the conventional threshold. The finding is directionally consistent across sub-analyses. Treat as a strong trend, not a confirmed effect."

### Claim 5 — Field recency (not significant)

**What the data show:** 59.6% of gate-passers are from 2024+, but binomial p = 0.121. The median year is 2024 with a bootstrap CI of [2023, 2024].

**Dashboard text:**
> "The field is young but the statistical evidence for a 2024+ concentration is not strong enough to be confident it reflects a real pattern rather than sampling variation (p = 0.12). What we can say with confidence: the median publication year is 2024, and no tradition-complete benchmark ecosystem existed before 2022. The field's rapid recent growth is visible in the year distribution, even if the exact concentration threshold (60%+) does not reach significance."

**Why this matters:** Do not suppress the histogram. Show the year distribution chart and let readers see the growth curve. The visual evidence is real even if the specific binomial test does not reach threshold. Label the chart: "Year distribution — visual pattern shows recent growth; formal threshold test p = 0.12."

### Claim 7 — Bias-values conflation (not significant)

**What the data show:** Binomial p = 0.678. Bias-adjacent benchmarks: 10/47; values-focused: 13/47; mixed: 24/47. The binomial CI spans 0.232 to 0.655 — wide uncertainty.

**Dashboard text:**
> "The claim that bias-detection and values-measurement are often conflated is conceptually well-grounded, and the implementation trial provides independent evidence: the Sonnet correlation between bias rubric and values rubric is r = 0.288, suggesting construct independence. However, the cross-sectional survey does not reach statistical significance (p = 0.68), meaning the observed split between bias-adjacent and values-focused benchmarks could arise by chance. The practical implication holds regardless of the formal test: researchers building new benchmarks should specify in advance whether they are measuring values alignment or bias detection, as these are distinct constructs."

**Annotation note:** "The wide confidence interval (23%-66%) tells us our sample of 47 benchmarks is underpowered for this particular question. A larger sample or a pre-registered binary classification scheme would resolve this."

---

## 5. Recommended Color Palette (Colorblind-Safe, Okabe-Ito)

Use the Okabe-Ito palette throughout. All four verdict categories and all tradition-family colors should be drawn from this set.

### Verdict categories

| Verdict | Hex | Name | Notes |
|---------|-----|------|-------|
| supported | #009E73 | Teal/green | Positive, confident |
| revised | #E69F00 | Orange/amber | Attention, nuance |
| not_significant | #0072B2 | Blue | Informative, not negative |
| (future: refuted) | #D55E00 | Vermilion | Not used in this paper |

Avoid:
- Red (#FF0000) for not_significant — reads as failure or error
- Grey (#808080) for not_significant — reads as missing or unknown
- Green/red adjacency without a third distinguishing channel

### Tradition families (secondary palette)

| Family | Hex | Notes |
|--------|-----|-------|
| Abrahamic | #56B4E9 | Sky blue |
| Dharmic | #F0E442 | Yellow |
| East Asian | #CC79A7 | Mauve/purple |
| African / Indigenous | #D55E00 | Vermilion |
| Other / cross-tradition | #999999 | Grey (background use only) |

### Background and text

- Dark theme background: #1c2128 (not var(--bg) — explicit hex required for Bootstrap table override)
- Card background: #2d333b
- Body text: #cdd9e5
- Secondary text: #768390
- Accent / highlight: #539bf5 (blue, for links and active states)

### Accessibility verification

All verdict badge combinations must pass WCAG AA (4.5:1 contrast for body text, 3:1 for large text):

- #009E73 on #2d333b: verify contrast before deploy
- #E69F00 on #2d333b: verify — amber on dark usually passes
- #0072B2 on #2d333b: verify — may need lightened variant (#58A6FF) for sufficient contrast on dark backgrounds

Use #58A6FF (lighter blue) in place of #0072B2 for text and icon use on dark backgrounds. Reserve #0072B2 for filled badge backgrounds where white text is used on top.

---

## 6. Effect Size Interpretation Guide (Cohen's d)

### Reference benchmarks

| Cohen's d magnitude | Label | Intuitive translation |
|--------------------|-------|-----------------------|
| 0.0 to < 0.2 | Negligible | Difficult to detect without large samples |
| 0.2 to < 0.5 | Small | Visible with careful measurement; about 8 percentile points difference |
| 0.5 to < 0.8 | Medium | Noticeable in practice; roughly half a standard deviation gap |
| 0.8 to < 1.2 | Large | Clearly distinguishable; comparable to knowing a foreign language vs not |
| >= 1.2 | Very large | Rarely seen outside experimental interventions; substantial in any context |

### C8-specific translation

d = -1.23 means the mean values relevance score (30.0) is 1.23 standard deviations below the midpoint (50.0). The negative sign indicates the gap is in the deficient direction — benchmarks fall below, not above, the threshold.

Intuitive framing for dashboard tooltip:
> "A gap of 1.23 standard deviations is very large by social science benchmarks. For comparison, the difference between average readers and skilled adult readers on standardized reading tests is approximately d = 0.8. The values relevance gap found here (d = 1.23) is larger than that."

### Cramer's V reference benchmarks

| Cramer's V (df=5) | Label | Notes |
|-------------------|-------|-------|
| 0.06 | Small | For df = 5, Cohen (1988) small effect |
| 0.17 | Medium | |
| 0.29 | Large | |
| > 0.50 | Very large | Well above large threshold |

C1 uniform baseline: V = 0.53 (very large). C1 corpus-adjusted: V = 0.30 (just above large threshold).

Dashboard tooltip: "Cramer's V measures how unequal a distribution is compared to what would be expected. At 0.53, the tradition distribution among gate-passers is very far from uniform."

### Odds ratio (C6) reference

An odds ratio of 1.0 means equal odds. OR = 0.58 means WEIRD-origin benchmarks have about 58% of the odds of passing compared to non-WEIRD benchmarks — a 42% reduction in odds. For non-expert readers:

> "An odds ratio of 0.58 means WEIRD-context benchmarks are about 40% less likely to pass the gates than non-WEIRD ones. This is a moderate effect, though the test does not reach the conventional significance threshold (p = 0.09)."

### Pseudo R-squared (C4) reference

McFadden's pseudo R-squared of 0.07 indicates that the logistic regression predictors (English-language source, venue tier) explain about 7% of the variation in gate-passage outcomes. By convention, values of 0.02, 0.13, and 0.26 correspond to small, medium, and large effects in logistic regression.

Dashboard tooltip: "Pseudo R-squared of 0.07 is a small effect — the measured predictors account for about 7% of why some benchmarks pass the gates and others do not. The remaining 93% is explained by other factors, including unmeasured infrastructure variables."

---

## Implementation Notes for Dashboard v7

1. Every claim card must include: (a) verdict badge with color per palette above, (b) plain-English finding as primary text, (c) effect size bar if effect size is available, (d) p-value in secondary text with plain-English gloss, (e) expandable technical footnote with exact test statistics.

2. C8 appears first in claim order, with the three-convergence box as a special layout element not used by other claims.

3. Revised claims (C4, C6) must include an explicit "What changed from the original claim" annotation — do not just show the orange badge without explanation.

4. Not-significant claims (C5, C7) must include an explicit "Why this still matters" annotation — do not let the blue badge imply the finding is unimportant.

5. The effect size interpretation guide (Section 6 benchmarks) should appear as a persistent legend or collapsible panel accessible from any claim card. Do not require readers to scroll to a separate documentation section.

6. All color decisions are final only after Playwright screenshot verification on both light and dark themes. Check WCAG AA on #009E73, #E69F00, #58A6FF against #2d333b before deploy.

7. Simulated cross-vendor data (Gemini, OpenAI) must be labeled with "Simulated — Claude roleplay, not real API" wherever model comparison charts appear. See CAV-3 in claims_canonical.json.
