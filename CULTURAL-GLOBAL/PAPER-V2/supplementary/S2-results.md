# Supplementary Results

## S2.1 Full Regional Profile Matrix (34 Dimensions × 10 Regions)

Supplementary Table S2 presents the complete mean scores for all 34 normative dimensions across each of the 10 macro-regions. The 34 dimensions comprise:
- 5 Western normative ethics: virtue_ethics, deontological_ethics, utilitarian_ethics, care_ethics, contractarian_ethics
- 7 non-Western frameworks: nw_confucian, nw_ubuntu, nw_islamic, nw_buddhist, nw_dharmic, nw_indigenous, nw_buenvivir
- 14 religious traditions: rv_islam, rv_christianity, rv_buddhism, rv_judaism, rv_hinduism, rv_sikhism, rv_confucianism, rv_taoism, rv_shinto, rv_jainism, rv_bahai, rv_zoroastrianism, rv_ubuntu, rv_indigenous
- 8 moral psychology: mp_mft, mp_schwartz, mp_trolley, mp_kohlberg, mp_dual_process, mp_intuitionist, mp_dyadic, mp_identity

Key patterns visible in the full matrix but not reported in the main text:
- **rv_judaism** scores are highest in North America (1.8) and Western Europe (1.5), reflecting the geographic distribution of Jewish studies programs
- **mp_trolley** (trolley problem engagement) is highest in Western Europe (2.1) and North America (1.8), zero in Sub-Saharan Africa, Latin America, and Southeast Asia
- **rv_shinto** is essentially zero everywhere except East Asia (0.3), reflecting the geographic specificity of Shinto
- **contractarian_ethics** is the lowest-scoring Western framework globally (corpus-wide mean 0.7), with the highest engagement in Western Europe (1.2)

## S2.2 Statistical Test Results

### S2.2.1 Chi-Square Test: Region × Framework Association
- χ² = 397.7, df = 99, p < 0.001
- Cramér's V = 0.30 (medium effect)
- The contingency table comprised 10 regions × 12 framework columns with non-zero marginals

### S2.2.2 Kruskal-Wallis Tests: Framework by Global North/South
After Benjamini-Hochberg FDR correction, 5 of 12 framework dimensions differ significantly:
| Framework | H statistic | p (uncorrected) | p (BH-adjusted) | Significant |
|-----------|-------------|-----------------|------------------|-------------|
| Utilitarian | 89.4 | <0.001 | <0.001 | Yes |
| Deontological | 52.1 | <0.001 | <0.001 | Yes |
| Virtue | 38.7 | <0.001 | <0.001 | Yes |
| Care | 12.3 | 0.002 | 0.004 | Yes |
| mp_mft | 15.8 | <0.001 | <0.001 | Yes |
| Confucian | 4.2 | 0.12 | 0.18 | No |
| Ubuntu | 3.1 | 0.21 | 0.25 | No |
| Islamic | 2.8 | 0.25 | 0.28 | No |

### S2.2.3 Mann-Whitney U Tests: High-WEIRD vs Non-WEIRD
| Framework | U statistic | p | Cohen's d | Direction |
|-----------|-------------|---|-----------|-----------|
| Virtue | 24,891 | 0.02 | +0.26 | Higher in High-WEIRD |
| Utilitarian | 26,103 | 0.04 | +0.22 | Higher in High-WEIRD |
| Deontological | 25,445 | 0.06 | +0.18 | Higher in High-WEIRD |
| Islamic | 28,912 | 0.38 | -0.09 | Higher in Non-WEIRD |
| Care | 29,104 | 0.42 | +0.07 | ns |

Effect sizes are uniformly small (|d| < 0.3), indicating the WEIRD gap manifests as a systematic tendency across many dimensions rather than a dramatic difference on any single framework.

### S2.2.4 Bootstrap Confidence Intervals (95%, 1000 iterations)
| Estimate | Point | 95% CI Lower | 95% CI Upper |
|----------|-------|-------------|-------------|
| Sub-Saharan Africa Ubuntu | 24.6 | 14.2 | 35.8 |
| Oceania Indigenous relational | 12.7 | 7.3 | 18.9 |
| East Asia Confucian | 3.5 | 2.1 | 5.2 |
| MENA Islamic | 3.4 | 1.8 | 5.3 |
| Corpus-wide WEIRD mean | 64.5 | 63.8 | 65.2 |
| NW engagement rate | 6.9% | 5.8% | 8.1% |

## S2.3 Per-Framework Gold Standard Validation Details

### False Positive Analysis by Framework

**Confucian (Precision 0.364):** 14 FPs of 22 detections in gold standard sample. Primary FP pattern: Chinese NLP benchmarks (8 papers), Chinese text sentiment analysis (3), Chinese dialogue systems (2), Classical Chinese corpus linguistics (1). Pattern: papers applying NLP methods TO Chinese/Confucian texts without engaging Confucian ethics AS analytical framework.

**Buddhist (Precision 0.333):** 6 FPs of 9 detections. Buddhist parallel corpus studies (3), Buddhist text digitization projects (2), Tibetan language NLP (1). Same NLP-on-texts pattern.

**Dharmic (Precision 0.250):** 6 FPs of 8 detections. Hindu text sentiment analysis (3), Sanskrit NLP corpus (2), Vedic text digitization (1).

**Buen Vivir (Precision 0.167):** 5 FPs of 6 detections. Passing comparative mentions ("alongside Buen Vivir") without substantive engagement (4), Latin American governance overview with one-sentence reference (1).

**Ubuntu (Precision 0.579):** 8 FPs of 19 detections. Ubuntu OS references that passed initial filtering (3), passing mentions in decolonial AI literature without substantive Ubuntu engagement (3), South African tech policy papers referencing Ubuntu symbolically (2).

**Indigenous (Precision 0.675):** 13 FPs of 40 detections. Indigenous language NLP/preservation projects (7), papers mentioning Indigenous populations as study subjects without engaging Indigenous ethics (4), Australian Aboriginal health data studies (2).

**Islamic (Precision 1.000):** 0 FPs of 12 detections. Islamic keywords (maqasid, fiqh, ijtihad) are highly specific to ethical and legal reasoning, with no NLP-on-texts equivalent.

## S2.4 Silhouette Analysis (k=2 through k=6)

| k | Silhouette Score | Cluster Sizes | Interpretation |
|---|-----------------|---------------|---------------|
| 2 | 0.267 | 1,614 / 555 | West+East vs Global South |
| 3 | 0.286 | 1,568 / 555 / 46 | Western Analytical / Transitional / Oceania (reported) |
| 4 | 0.322 | 1,258 / 310 / 555 / 46 | Splits W.Analytical into N.Am+E.Asia vs W.Europe |
| 5 | 0.298 | 1,258 / 310 / 433 / 122 / 46 | Further splits Transitional |
| 6 | 0.271 | 1,258 / 310 / 295 / 138 / 122 / 46 | Over-splits with unstable clusters |

The k=3 solution was selected for interpretability despite k=4 having a marginally higher silhouette score. At k=4, the split of the Western Analytical cluster separates North America + East Asia from Western Europe, which, while statistically supported, fragments a theoretically coherent cluster.

## S2.5 Complete TOPSIS Rankings (Top 50)

See Supplementary Table S3 for the full ranking of all 218 benchmarks by TOPSIS score, including stability vectors across 5 alternative weight schemes.

## S2.6 Per-Model Trial Response Summaries

### Claude Opus 4.6 (Tier 1: Authentic)
- MFQ Individualizing:Binding = 3.75
- Country closest: Germany (0.538), farthest: Saudi Arabia (1.974)
- RLHF conflicts: 277 (62 autonomy, 38 secular, 27 consequentialist, 20 anti-authority, 17 gender, 2 harm, 116 other)
- Engagement scores: Ubuntu 3.5, all others 1.0
- Response length: 389.9 chars mean

### Claude Sonnet 4.6 (Tier 1: Authentic)
- MFQ Individualizing:Binding = 3.23
- Country closest: Germany (0.55), farthest: Saudi Arabia (1.874)
- RLHF conflicts: 210 (44 autonomy, 28 secular, 24 consequentialist, 12 anti-authority, 9 gender, 1 harm, 111 other)
- Engagement scores: Ubuntu 4.0 (highest in dataset), all others 1.0
- Response length: 519.3 chars mean

### Claude Haiku 4.5 (Tier 1: Authentic)
- MFQ Individualizing:Binding = 4.82 (most extreme in dataset)
- Country closest: Germany (0.546), farthest: Saudi Arabia (1.874)
- RLHF conflicts: 216 (32 autonomy, 140 other)
- Engagement scores: Dharmic 4.0 (unexpected for smallest model), all others 1.0
- Response length: 423.8 chars mean

### GPT-5.4 (Tier 2: Codex-Authored)
- MFQ Individualizing:Binding = 2.48 (most balanced in dataset, but Codex confound)
- Engagement scores: Buddhist 3.0, Dharmic 3.0
- Response length: 276.2 chars mean

### GPT-5.4-Mini (Tier 2: Codex-Authored)
- MFQ Individualizing:Binding = 3.22
- Response length: 254.4 chars mean

### Gemini (all 5 models, Tier 3: Aggregate-Convergent)
- Item-level differentiation confirmed: 29--31 of 50 CC1 items differ between any two Gemini variants
- Inter-Gemini Pearson correlations range from $r$ = 0.593 (Flash vs. Pro) to $r$ = 0.909 (Flash-Lite vs. Pro)
- Aggregate metrics converge across variants: MFQ I:B $\approx$ 3.75, RLHF conflict total $\approx$ 277, response length $\approx$ 389.9 chars
- Effective N for the five Gemini models: $\approx$ 1.21 (DEFF = 4.12, mean within-tier $\rho$ = 0.78)
- Interpretation: pre-training corpora across Gemini variants share substantial overlap, producing convergent macro-level cultural profiles; item-level diversity reflects sampling and architectural differences, not deeply different alignment regimes

## S2.7 Power Sensitivity Analysis

The cross-model effective sample size formalized in Section 5.6.4 is $N_\text{eff} \approx 3.4$ (range 3.1--4.8). The following table reports the minimum detectable effect size (MDES) at conventional power (0.80) and significance ($\alpha = 0.05$, two-sided) for the primary statistical tests used in Study 3, computed via standard formulas (G*Power 3.1; Faul et al., 2007).

| Test | $N_\text{eff}$ | $df$ | MDES (Cohen's $d$ or $r$) | Interpretation |
|------|---------------|------|---------------------------|----------------|
| Two-sample $t$-test (between providers) | 3.4 / 3.4 | 4.8 | $d = 2.50$ | Detectable: only "huge" effects ($d \geq 2$) |
| Pearson correlation (across pairs) | 6 pairs | 4 | $r = 0.811$ | Detectable: only near-perfect correlations |
| One-way ANOVA (3 providers) | 3.4 per group | 2, 7.2 | $f = 0.95$ | Detectable: only "very large" effects |
| Kruskal-Wallis (3 providers) | 3.4 per group | 2 | $\eta^2 \approx 0.50$ | Detectable: only effects explaining $\geq$ 50% variance |

For comparison, the conventional "large effect" benchmarks (Cohen, 1988) are $d = 0.8$, $r = 0.5$, $f = 0.4$, $\eta^2 = 0.14$. The MDES values in the table are 2--3 times larger than "large effects," meaning that the cross-model analyses in Study 3 can detect only differences that are not merely large but extreme. Cross-provider patterns reported in the paper should therefore be interpreted as descriptive observations rather than confirmatory inferences. The within-Claude pairwise correlations ($r$ = 0.885--0.952), the I:B ratio differences (3.23--4.82, range 1.59 = $d \approx 2.7$ within Claude), and the Gemini item-level differentiation ($r$ = 0.593--0.909) are all detectable at this $N_\text{eff}$, but the absence of a detectable cross-provider effect is uninformative given the power constraint.

This power constraint is structural rather than incidental: any cross-model study of LLMs is limited by the small number of independent model families released by major providers. Resolving it requires either a longitudinal design (multiple checkpoints from each provider) or a coordinated cross-provider replication initiative analogous to the Many Labs efforts in psychology.
