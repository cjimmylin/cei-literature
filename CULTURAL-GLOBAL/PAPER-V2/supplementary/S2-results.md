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

### Gemini (all 5 models, Tier 3: Template-Derived)
- All metrics identical: MFQ 3.75, RLHF 277, response length 389.9
- Treated as single observation for all analyses
