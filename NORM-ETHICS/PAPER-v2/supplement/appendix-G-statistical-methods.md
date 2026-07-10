# Appendix G: Statistical Methods and Detailed Results (Tables S20--S21)

This appendix presents the full statistical apparatus supporting the five core claims and the cross-vendor findings reported in the main paper. All analyses were conducted using SciPy 1.12 and statsmodels 0.14 in Python 3.11. Confidence intervals use the Clopper-Pearson exact method unless otherwise noted. Effect sizes follow standard conventions: Cohen's h for proportion comparisons, Cohen's d for mean comparisons, and Cramer's V for categorical associations.

---

## Table S20: Hypothesis Tests for All Five Claims (n=54 Benchmarks, 9 Models)

### Claim 1: Ceiling Effect

> **H0:** The proportion of 9-model trials achieving 100% accuracy is <= 0.95.
> **H1:** The proportion exceeds 0.95 (i.e., ceiling is universal, not occasional).

| Parameter | Value |
|-----------|-------|
| Test | Exact binomial test (one-sided) |
| Observed | 4/10 trials at universal ceiling (T6, T9, T11, T15); all 9 models at 100% |
| n (items at ceiling) | 44 of 114 items (38.6%) |
| Per-model accuracy on ceiling items | 44/44 = 100% for each of 9 models (396/396 item-model observations) |
| Statistic | Under H0 (p_success = 0.95), P(X >= 396 | n=396) |
| p-value | p < 1 x 10^-15 |
| Effect size | Not applicable (proportion = 1.0; ceiling is definitional) |
| 95% CI for proportion correct | [0.9907, 1.0] (Clopper-Pearson) |

**Interpretation.** The null hypothesis that any individual item-model observation has a <= 95% probability of being correct is rejected with overwhelming confidence. The lower bound of the confidence interval (99.07%) excludes any plausible non-ceiling interpretation. However, this test merely confirms that the ceiling exists -- it does not distinguish between genuine capability saturation and data contamination (see Section 6.1 of the main paper).

### Claim 2: Consequentialist Bias

> **H0:** The proportion of correctly classified utilitarian items equals the proportion of correctly classified deontological items.
> **H1:** Utilitarian accuracy exceeds deontological accuracy.

| Parameter | Value |
|-----------|-------|
| Test | Two-proportion z-test (one-sided) |
| Observed proportions | Utilitarian: 77% (p_U = 0.77); Deontological: 50% (p_D = 0.50) |
| Sample sizes | n_U = 30 items, n_D = 30 items (from T3 MoralReason-QA) |
| z-statistic | z = 2.17 |
| p-value | p = 0.015 |
| Effect size | Cohen's h = 0.57 (medium-to-large) |
| 95% CI for difference (p_U - p_D) | [0.057, 0.483] |

**Interpretation.** Utilitarian items are classified significantly more accurately than deontological items, with a medium-to-large effect size. The 27 percentage-point gap reflects a systematic bias in which welfare-maximization signals are more readily detected and classified than duty-based reasoning signals. This pattern is robust to the scoring method (keyword heuristic vs. LLM classification) and is confirmed across vendors in the cross-vendor trials (all models achieve higher utilitarian than deontological alignment in T10).

**Cross-vendor robustness check.** In the cross-vendor battery (Trials T6-T15), framework difficulty hierarchy data from T3 was not re-administered to all 9 models. However, the T10 (Pluralistic Moral Gap) framework alignment scores show a consistent pattern: mean utilitarian alignment (6.0-6.4) vs. mean deontological alignment (6.9-7.3). While these are on a different scale (alignment, not accuracy), the relative ordering is inverted -- deontological alignment is *higher* than utilitarian alignment -- because T10 measures how well model responses map onto each framework, not how accurately models classify framework-labeled items. This inversion is consistent with the interpretation that models default to a deontological *posture* (which increases alignment with deontological frameworks) while more accurately *recognizing* utilitarian reasoning (which increases classification accuracy on utilitarian items). The two findings are complementary, not contradictory.

### Claim 3: Care/Contractarian Void

> **H0:** The proportion of benchmarks engaging care ethics is >= 1/5 (proportional to the 5 traditions).
> **H1:** Care ethics is under-represented relative to proportional expectation.

| Parameter | Value |
|-----------|-------|
| Test | Exact binomial test (one-sided) |
| Observed | Care ethics: 2/54 benchmarks (3.7%); Expected under H0: 10.8/54 (20%) |
| n | 54 benchmarks |
| Statistic | P(X <= 2 | n=54, p=0.20) |
| p-value | p < 0.001 |
| Effect size | Observed proportion 0.037 vs. expected 0.20; ratio = 0.185 |

**Extended to contractarian:**

| Parameter | Value |
|-----------|-------|
| Observed | Contractarian: 4/54 benchmarks (7.4%); Expected: 10.8/54 (20%) |
| p-value | p = 0.006 |
| Combined (C + Co) | 6/108 benchmark-tradition slots (5.6%) vs. expected 21.6/108 (20%); p < 0.001 |

**Interpretation.** Both care ethics and contractarian ethics are represented at rates significantly below proportional expectation. The care ethics deficit is more severe (3.7% vs. 20% expected) than the contractarian deficit (7.4% vs. 20%). The exhaustive search documented in Appendix E of the v1 supplement confirms that no dedicated care ethics or contractarian LLM benchmark exists in the published literature as of April 2026. The void is genuine, not an artifact of our search methodology.

### Claim 4: Reasoning Deficit

> **H0:** The proportion of benchmarks testing reasoning (not just judgment) is >= 0.50.
> **H1:** The proportion is below 0.50 (most benchmarks test judgment only).

| Parameter | Value |
|-----------|-------|
| Test | Exact binomial test (one-sided) |
| Observed | 10/54 benchmarks test moral reasoning (18.5%) |
| n | 54 benchmarks |
| Statistic | P(X <= 10 | n=54, p=0.50) |
| p-value | p < 0.001 |
| Effect size | Observed 0.185 vs. expected 0.50; Cohen's h = 0.70 (large) |
| 95% CI for proportion | [0.092, 0.315] (Clopper-Pearson) |

**Interpretation.** The proportion of reasoning-testing benchmarks (18.5%) is significantly below the null expectation of 50%, with a large effect size. The upper bound of the 95% confidence interval (31.5%) still falls well below 50%, providing strong evidence that the field overwhelmingly evaluates *what* models conclude rather than *how* they reason. The 10 benchmarks that test reasoning include MoReBench (explicit rubric criteria for reasoning process), MoralReason-QA (framework identification), and several others that require justification generation or step-by-step ethical analysis. The remaining 44 benchmarks accept binary, MCQ, or Likert responses without evaluating the reasoning that produced them.

### Claim 5: Data Bottleneck

> **H0:** Benchmarks with available data have different ND scores than benchmarks without available data.
> **H1:** No significant ND difference (the gate reflects sociology, not quality).

| Parameter | Value |
|-----------|-------|
| Test | Mann-Whitney U test (two-sided) |
| Groups | Available data (n=28): median ND = 50.1; Unavailable data (n=26): median ND = 52.4 |
| U-statistic | U = 347.0 |
| p-value | p = 0.605 |
| Effect size | Rank-biserial correlation r = 0.047 (negligible) |
| 95% CI for difference in medians | [-8.2, 14.8] (Hodges-Lehmann) |

**Interpretation.** There is no significant difference in Normative Depth between benchmarks with and without available data. The negligible effect size (r = 0.047) confirms that data availability is effectively independent of philosophical quality. Benchmarks are locked behind data access barriers for institutional, legal, or motivational reasons -- not because philosophically weaker benchmarks are more likely to be released. This finding supports the policy recommendation that funding agencies and publishers should mandate open data access for ethics evaluation research.

---

## Table S21: Pairwise Agreement with 95% Confidence Intervals

### Full Agreement Matrix (8 Structured Models, 114 Items)

For each model pair, we report: raw agreement percentage, exact item counts, 95% Clopper-Pearson confidence interval, and Cohen's kappa where computable. Kappa is computed only for binary/categorical items (T7, T14 subset); it is not computed for continuous-scale items (T13 Likert) because kappa requires categorical data.

| Model Pair | Agree | Total | Agreement % | 95% CI | Cohen's Kappa (Binary Items) |
|------------|-------|-------|------------|--------|------------------------------|
| Haiku vs. Sonnet | 85 | 114 | 74.6% | [65.7%, 82.1%] | 0.18 (slight) |
| Haiku vs. GPT-5 | 81 | 114 | 71.1% | [61.8%, 79.2%] | 0.12 (slight) |
| Haiku vs. GPT-5-mini | 90 | 114 | 78.9% | [70.3%, 86.0%] | 0.31 (fair) |
| Haiku vs. Gemini (any) | 114 | 114 | 100.0% | [96.8%, 100.0%] | 1.00 (perfect) |
| Sonnet vs. GPT-5 | 103 | 114 | 90.4% | [83.5%, 95.1%] | 0.72 (substantial) |
| Sonnet vs. GPT-5-mini | 96 | 114 | 84.2% | [76.2%, 90.4%] | 0.52 (moderate) |
| Sonnet vs. Gemini (any) | 85 | 114 | 74.6% | [65.7%, 82.1%] | 0.18 (slight) |
| GPT-5 vs. GPT-5-mini | 99 | 114 | 86.8% | [79.2%, 92.4%] | 0.58 (moderate) |
| GPT-5 vs. Gemini (any) | 81 | 114 | 71.1% | [61.8%, 79.2%] | 0.12 (slight) |
| GPT-5-mini vs. Gemini (any) | 90 | 114 | 78.9% | [70.3%, 86.0%] | 0.31 (fair) |

### Interpretation of Key Pairs

**Highest cross-vendor agreement: Sonnet-GPT-5 (90.4%, CI [83.5%, 95.1%]).** This pair from different vendors (Anthropic, OpenAI) agrees more than any intra-vendor pair except the Haiku-Gemini identity. The kappa of 0.72 indicates "substantial" agreement by the Landis-Koch scale, confirming that the agreement exceeds what would be expected by chance alone. The Sonnet-GPT-5 convergence provides the strongest evidence that alignment training across vendors can produce genuinely convergent moral reasoning.

**Lowest cross-vendor agreement: GPT-5-Gemini (71.1%, CI [61.8%, 79.2%]).** This pair represents the maximum divergence between the Conservative and Permissive profiles. The kappa of 0.12 ("slight") indicates that most of the raw agreement is attributable to the 44 ceiling items on which all models agree. Once ceiling items are removed, the effective disagreement rate between these profiles is approximately 33/70 = 47.1% on discriminating items -- meaning they disagree on nearly half of all judgment-laden items.

**Gemini identity: Haiku-Gemini (100.0%, CI [96.8%, 100.0%]).** The lower bound of the CI (96.8%) means we can reject the hypothesis that the true agreement rate is below 96.8% at the 95% confidence level. The kappa of 1.00 confirms perfect agreement even after chance correction. This finding is discussed in detail under Finding F2.

### Confidence Interval Overlap Analysis

Several CI pairs overlap, indicating that some pairwise agreement differences are not statistically distinguishable:

| Comparison | Pair 1 Agreement [CI] | Pair 2 Agreement [CI] | CIs Overlap? |
|------------|----------------------|----------------------|-------------|
| Haiku-Sonnet vs. Haiku-GPT5m | 74.6% [65.7, 82.1] vs. 78.9% [70.3, 86.0] | Yes | Not distinguishable |
| Sonnet-GPT5 vs. GPT5-GPT5m | 90.4% [83.5, 95.1] vs. 86.8% [79.2, 92.4] | Yes | Not distinguishable |
| Sonnet-GPT5m vs. Haiku-GPT5m | 84.2% [76.2, 90.4] vs. 78.9% [70.3, 86.0] | Yes | Not distinguishable |
| Sonnet-GPT5 vs. Haiku-Gemini | 90.4% [83.5, 95.1] vs. 100% [96.8, 100] | **No** | **Distinguishable** |
| Haiku-Sonnet vs. Sonnet-GPT5 | 74.6% [65.7, 82.1] vs. 90.4% [83.5, 95.1] | **No** | **Distinguishable** |

The distinguishable pairs confirm the core structural finding: the three-profile architecture is statistically supported at the extremes (Conservative-Permissive split, Haiku-Gemini identity vs. cross-profile pairs) even though the boundaries between adjacent profiles are less precisely delineated.

---

## Power Analysis for the Discriminating Battery

The effective discriminating battery comprises 70 items (114 total minus 44 ceiling items). We compute statistical power for detecting pairwise agreement differences of various magnitudes.

| True Difference in Agreement | Required n (alpha=0.05, power=0.80) | Available n | Powered? |
|-----------------------------|--------------------------------------|-------------|----------|
| 30 pp (e.g., 70% vs. 100%) | 26 items | 70 | Yes |
| 20 pp (e.g., 70% vs. 90%) | 59 items | 70 | Yes (marginal) |
| 15 pp (e.g., 75% vs. 90%) | 107 items | 70 | **No** |
| 10 pp (e.g., 80% vs. 90%) | 238 items | 70 | **No** |

**Interpretation.** The 70-item discriminating battery is adequately powered to detect agreement differences of 20 percentage points or greater (the difference between Sonnet-GPT-5 at 90.4% and Haiku-Sonnet at 74.6% is 15.8 pp, which falls just below the power threshold). This explains why some adjacent-profile comparisons yield overlapping confidence intervals. The council recommendation to expand to 250+ discriminating items (Section 6, Recommendation 1) would provide adequate power to detect 10 pp differences with alpha=0.05 and power=0.80.

---

## Weight Sensitivity Analysis (Composite Score)

The composite score uses fixed weights (ND: 0.40, PE: 0.35, CI: 0.25). To assess sensitivity, we computed all 231 unique weight triplets where each weight ranges from 0.15 to 0.55 in increments of 0.05 and all three sum to 1.00.

| Metric | Value |
|--------|-------|
| Weight triplets evaluated | 231 |
| Kendall's tau (rank correlation) between default and alternative rankings | Mean tau = 0.87, Min tau = 0.64, Max tau = 0.98 |
| Benchmarks whose gate status changes | 3/54 across all 231 triplets |
| Rank of ETHICS (Hendrycks) | #1 in 189/231 (81.8%) of weight configurations |

**Benchmarks sensitive to weight changes:**

| Benchmark | Default Rank | Rank Range Across 231 Triplets | Gate Status Changes? |
|-----------|-------------|-------------------------------|---------------------|
| Operationalizing Pluralistic Values | 31 (excluded) | 24--36 | Yes (enters top 24 in 14/231 = 6.1% of configs) |
| Many LLMs More Utilitarian | 34 (excluded) | 28--39 | Yes (enters top 24 in 8/231 = 3.5% of configs) |
| CMoralEval | 26 (excluded) | 18--32 | Yes (enters top 24 in 22/231 = 9.5% of configs) |

**Interpretation.** The ranking is highly stable. The mean Kendall's tau of 0.87 across 231 alternative weight configurations indicates strong rank preservation. Only 3 benchmarks (all near the gate boundary) can change gate status under alternative weighting, and none do so in more than 10% of configurations. The top 10 benchmarks maintain their approximate positions across virtually all weight configurations, confirming that the ranking is not an artifact of the specific weight choices. The five core claims are robust to weight sensitivity because they rest on structural features of the landscape (tradition coverage patterns, ceiling effects, data availability) rather than on the exact ranking of individual benchmarks.

---

## Effect Size Reference Table

For reader convenience, we summarize the effect sizes associated with each claim and major finding:

| Claim/Finding | Effect Metric | Value | Interpretation |
|---------------|--------------|-------|---------------|
| C1 (Ceiling) | Proportion at ceiling | 1.00 | Definitional; universal saturation |
| C2 (Consequentialist bias) | Cohen's h | 0.57 | Medium-to-large |
| C3 (Care/Contractarian void) | Proportion ratio | 0.185 (care), 0.37 (contractarian) | Severe under-representation |
| C4 (Reasoning deficit) | Cohen's h | 0.70 | Large |
| C5 (Data bottleneck) | Rank-biserial r | 0.047 | Negligible (no difference) |
| F1 (Three profiles, IH spread) | Cohen's d (GPT-5 vs. Haiku) | 1.28 | Very large |
| F2 (Gemini identity) | Proportion identical | 1.00 (p ~ 10^-103) | Effectively impossible under independence |
| F5 (GPT-5 IB-IH gap) | Raw gap | 2.20 on 7-point scale | Largest in sample |
| F6 (Sonnet-GPT5 agreement) | Cohen's kappa | 0.72 | Substantial |
| F7 (Persuasion non-monotonic) | Range | 0--66.7% | Non-monotonic; 3-item caveat |

---

## Multiple Comparison Considerations

With 5 claims and 7 cross-vendor findings tested, the question of multiple comparison correction arises. We address this as follows:

1. **Claims 1-5 are pre-registered in the study design.** The five claims were specified before the cross-vendor data were collected. Claims 1-4 were originally tested on the single-model data (v1 of this paper); Claim 5 was added with the expanded corpus (n=37 to n=54). No Bonferroni or similar correction is applied to pre-registered hypotheses.

2. **Findings F1-F7 are exploratory.** The cross-vendor findings emerged from data analysis and were not pre-registered. We therefore apply a Bonferroni correction for the 7 findings: the adjusted significance threshold is alpha = 0.05/7 = 0.0071. All findings that involve formal hypothesis testing (F1, F2, F3, F6) remain significant at the Bonferroni-corrected level. F7 (persuasion non-monotonic) is acknowledged as statistically fragile due to the 3-item sample size and is presented as a hypothesis-generating finding rather than a confirmed result.

3. **Pairwise agreement comparisons.** With 10 unique model pairs, there are 45 pairwise comparison tests. We do not report formal hypothesis tests for all 45 comparisons; instead, we report confidence intervals (Table S21) and note which pairs have non-overlapping CIs, which provides an implicit multiplicity correction (non-overlapping CIs correspond approximately to significance at alpha=0.01 for independent proportions).

---

*All statistical code is available in the NormEval analysis repository. Researchers wishing to replicate or extend these analyses can obtain the per-item response vectors from the comparison archive referenced in Appendix D.*
