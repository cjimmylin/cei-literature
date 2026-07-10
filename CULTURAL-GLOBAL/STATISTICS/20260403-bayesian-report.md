# Bayesian Analysis of Non-Western Framework Detection

**Date:** 20260403
**Papers:** 2046

Addresses Council recommendation R6: Bayesian credible intervals for small-n frameworks (Buddhist n=11, Dharmic n=9, Buen Vivir n=6).

## 1. Detection Rate Posteriors by Region

Beta-binomial model with uniform Beta(1,1) prior. Detection threshold: score >= 50.

### nw_confucian

| Region | n | Detected | Post. Mean | 95% HDI | P(rate>5%) |
|--------|---|----------|-----------|---------|-----------|
| North America | 809 | 21 | 0.027 | [0.017, 0.039] | 0.000 |
| Western Europe | 421 | 15 | 0.038 | [0.022, 0.058] | 0.101 |
| East Asia | 260 | 25 | 0.099 | [0.066, 0.138] | 0.999 |
| MENA | 113 | 2 | 0.026 | [0.005, 0.062] | 0.072 |
| South Asia | 103 | 3 | 0.038 | [0.011, 0.082] | 0.231 |
| Southeast Asia | 102 | 2 | 0.029 | [0.006, 0.068] | 0.106 |
| Latin America & Caribbean | 90 | 1 | 0.022 | [0.003, 0.060] | 0.054 |
| Eastern Europe & Central Asia | 59 | 4 | 0.082 | [0.028, 0.162] | 0.820 |
| Oceania | 38 | 1 | 0.050 | [0.006, 0.135] | 0.413 |
| Sub-Saharan Africa | 22 | 0 | 0.042 | [0.001, 0.148] | 0.307 |

### nw_ubuntu

| Region | n | Detected | Post. Mean | 95% HDI | P(rate>5%) |
|--------|---|----------|-----------|---------|-----------|
| North America | 809 | 8 | 0.011 | [0.005, 0.019] | 0.000 |
| Western Europe | 421 | 6 | 0.017 | [0.007, 0.031] | 0.000 |
| East Asia | 260 | 1 | 0.008 | [0.001, 0.021] | 0.000 |
| MENA | 113 | 0 | 0.009 | [0.000, 0.032] | 0.003 |
| South Asia | 103 | 0 | 0.009 | [0.000, 0.035] | 0.005 |
| Southeast Asia | 102 | 0 | 0.010 | [0.000, 0.035] | 0.005 |
| Latin America & Caribbean | 90 | 0 | 0.011 | [0.000, 0.040] | 0.009 |
| Eastern Europe & Central Asia | 59 | 0 | 0.016 | [0.000, 0.060] | 0.046 |
| Oceania | 38 | 1 | 0.050 | [0.006, 0.135] | 0.413 |
| Sub-Saharan Africa | 22 | 6 | 0.292 | [0.132, 0.484] | 1.000 |

### nw_islamic_jurisprudence

| Region | n | Detected | Post. Mean | 95% HDI | P(rate>5%) |
|--------|---|----------|-----------|---------|-----------|
| North America | 809 | 4 | 0.006 | [0.002, 0.013] | 0.000 |
| Western Europe | 421 | 3 | 0.009 | [0.003, 0.021] | 0.000 |
| East Asia | 260 | 0 | 0.004 | [0.000, 0.014] | 0.000 |
| MENA | 113 | 6 | 0.061 | [0.025, 0.111] | 0.656 |
| South Asia | 103 | 0 | 0.009 | [0.000, 0.035] | 0.005 |
| Southeast Asia | 102 | 1 | 0.019 | [0.002, 0.053] | 0.033 |
| Latin America & Caribbean | 90 | 1 | 0.022 | [0.003, 0.060] | 0.054 |
| Eastern Europe & Central Asia | 59 | 2 | 0.049 | [0.010, 0.115] | 0.417 |
| Oceania | 38 | 0 | 0.025 | [0.001, 0.090] | 0.135 |
| Sub-Saharan Africa | 22 | 0 | 0.042 | [0.001, 0.148] | 0.307 |

### nw_buddhist

| Region | n | Detected | Post. Mean | 95% HDI | P(rate>5%) |
|--------|---|----------|-----------|---------|-----------|
| North America | 809 | 5 | 0.007 | [0.003, 0.014] | 0.000 |
| Western Europe | 421 | 2 | 0.007 | [0.002, 0.017] | 0.000 |
| East Asia | 260 | 1 | 0.008 | [0.001, 0.021] | 0.000 |
| MENA | 113 | 0 | 0.009 | [0.000, 0.032] | 0.003 |
| South Asia | 103 | 0 | 0.009 | [0.000, 0.035] | 0.005 |
| Southeast Asia | 102 | 1 | 0.019 | [0.002, 0.053] | 0.033 |
| Latin America & Caribbean | 90 | 0 | 0.011 | [0.000, 0.040] | 0.009 |
| Eastern Europe & Central Asia | 59 | 0 | 0.016 | [0.000, 0.060] | 0.046 |
| Oceania | 38 | 1 | 0.050 | [0.006, 0.135] | 0.413 |
| Sub-Saharan Africa | 22 | 1 | 0.083 | [0.011, 0.220] | 0.679 |

### nw_dharmic

| Region | n | Detected | Post. Mean | 95% HDI | P(rate>5%) |
|--------|---|----------|-----------|---------|-----------|
| North America | 809 | 3 | 0.005 | [0.001, 0.011] | 0.000 |
| Western Europe | 421 | 0 | 0.002 | [0.000, 0.009] | 0.000 |
| East Asia | 260 | 1 | 0.008 | [0.001, 0.021] | 0.000 |
| MENA | 113 | 0 | 0.009 | [0.000, 0.032] | 0.003 |
| South Asia | 103 | 3 | 0.038 | [0.011, 0.082] | 0.231 |
| Southeast Asia | 102 | 0 | 0.010 | [0.000, 0.035] | 0.005 |
| Latin America & Caribbean | 90 | 0 | 0.011 | [0.000, 0.040] | 0.009 |
| Eastern Europe & Central Asia | 59 | 0 | 0.016 | [0.000, 0.060] | 0.046 |
| Oceania | 38 | 2 | 0.075 | [0.016, 0.173] | 0.691 |
| Sub-Saharan Africa | 22 | 0 | 0.042 | [0.001, 0.148] | 0.307 |

### nw_indigenous_relational

| Region | n | Detected | Post. Mean | 95% HDI | P(rate>5%) |
|--------|---|----------|-----------|---------|-----------|
| North America | 809 | 16 | 0.021 | [0.012, 0.032] | 0.000 |
| Western Europe | 421 | 7 | 0.019 | [0.008, 0.034] | 0.000 |
| East Asia | 260 | 2 | 0.011 | [0.002, 0.027] | 0.000 |
| MENA | 113 | 0 | 0.009 | [0.000, 0.032] | 0.003 |
| South Asia | 103 | 0 | 0.009 | [0.000, 0.035] | 0.005 |
| Southeast Asia | 102 | 2 | 0.029 | [0.006, 0.068] | 0.106 |
| Latin America & Caribbean | 90 | 8 | 0.098 | [0.046, 0.166] | 0.962 |
| Eastern Europe & Central Asia | 59 | 0 | 0.016 | [0.000, 0.060] | 0.046 |
| Oceania | 38 | 6 | 0.175 | [0.075, 0.305] | 0.997 |
| Sub-Saharan Africa | 22 | 1 | 0.083 | [0.011, 0.220] | 0.679 |

### nw_buen_vivir

| Region | n | Detected | Post. Mean | 95% HDI | P(rate>5%) |
|--------|---|----------|-----------|---------|-----------|
| North America | 809 | 4 | 0.006 | [0.002, 0.013] | 0.000 |
| Western Europe | 421 | 1 | 0.005 | [0.001, 0.013] | 0.000 |
| East Asia | 260 | 0 | 0.004 | [0.000, 0.014] | 0.000 |
| MENA | 113 | 0 | 0.009 | [0.000, 0.032] | 0.003 |
| South Asia | 103 | 0 | 0.009 | [0.000, 0.035] | 0.005 |
| Southeast Asia | 102 | 0 | 0.010 | [0.000, 0.035] | 0.005 |
| Latin America & Caribbean | 90 | 0 | 0.011 | [0.000, 0.040] | 0.009 |
| Eastern Europe & Central Asia | 59 | 0 | 0.016 | [0.000, 0.060] | 0.046 |
| Oceania | 38 | 0 | 0.025 | [0.001, 0.090] | 0.135 |
| Sub-Saharan Africa | 22 | 1 | 0.083 | [0.011, 0.220] | 0.679 |

### dharmic_family

| Region | n | Detected | Post. Mean | 95% HDI | P(rate>5%) |
|--------|---|----------|-----------|---------|-----------|
| North America | 809 | 8 | 0.011 | [0.005, 0.019] | 0.000 |
| Western Europe | 421 | 2 | 0.007 | [0.002, 0.017] | 0.000 |
| East Asia | 260 | 2 | 0.011 | [0.002, 0.027] | 0.000 |
| MENA | 113 | 0 | 0.009 | [0.000, 0.032] | 0.003 |
| South Asia | 103 | 3 | 0.038 | [0.011, 0.082] | 0.231 |
| Southeast Asia | 102 | 1 | 0.019 | [0.002, 0.053] | 0.033 |
| Latin America & Caribbean | 90 | 0 | 0.011 | [0.000, 0.040] | 0.009 |
| Eastern Europe & Central Asia | 59 | 0 | 0.016 | [0.000, 0.060] | 0.046 |
| Oceania | 38 | 3 | 0.100 | [0.029, 0.209] | 0.871 |
| Sub-Saharan Africa | 22 | 1 | 0.083 | [0.011, 0.220] | 0.679 |

## 2. Score Posteriors by Region

Normal-Inverse-Gamma conjugate model (prior: mu0=25, kappa0=1, alpha0=2, beta0=100). Only papers with score > 0.

### nw_confucian

| Region | n>0 | Sample Mean | Post. Mean mu | 95% CI |
|--------|-----|------------|--------------|--------|
| North America | 41 | 34.51 | 34.29 | [26.01, 42.56] |
| Western Europe | 23 | 38.7 | 38.13 | [27.65, 48.6] |
| East Asia | 35 | 45.0 | 44.44 | [35.36, 53.53] |
| MENA | 3 | 48.33 | 42.5 | [31.33, 53.67] |
| South Asia | 8 | 22.5 | 22.78 | [9.76, 35.8] |
| Southeast Asia | 6 | 21.67 | 22.14 | [8.32, 35.96] |
| Latin America & Caribbean | 1 | 55.0 | 40.0 | [19.28, 60.72] |
| Eastern Europe & Central Asia | 6 | 36.67 | 35.0 | [21.68, 48.32] |
| Oceania | 3 | 21.67 | 22.5 | [5.63, 39.37] |
| Sub-Saharan Africa | 1 | 5.0 | 15.0 | [0, 31.26] |

### nw_ubuntu

| Region | n>0 | Sample Mean | Post. Mean mu | 95% CI |
|--------|-----|------------|--------------|--------|
| North America | 11 | 53.64 | 51.25 | [33.52, 68.98] |
| Western Europe | 12 | 36.67 | 35.77 | [18.07, 53.46] |
| East Asia | 1 | 100.0 | 62.5 | [17.88, 107.12] |
| Oceania | 1 | 50.0 | 37.5 | [19.1, 55.9] |
| Sub-Saharan Africa | 6 | 90.0 | 80.71 | [61.75, 99.68] |

### nw_islamic_jurisprudence

| Region | n>0 | Sample Mean | Post. Mean mu | 95% CI |
|--------|-----|------------|--------------|--------|
| North America | 5 | 52.0 | 47.5 | [25.98, 69.02] |
| Western Europe | 3 | 100.0 | 81.25 | [51.54, 110.96] |
| MENA | 8 | 53.75 | 50.56 | [29.78, 71.33] |
| South Asia | 1 | 5.0 | 15.0 | [0, 31.26] |
| Southeast Asia | 2 | 57.5 | 46.67 | [7.91, 85.43] |
| Latin America & Caribbean | 1 | 50.0 | 37.5 | [19.1, 55.9] |
| Eastern Europe & Central Asia | 2 | 50.0 | 41.67 | [27.34, 55.99] |

### nw_buddhist

| Region | n>0 | Sample Mean | Post. Mean mu | 95% CI |
|--------|-----|------------|--------------|--------|
| North America | 30 | 21.17 | 21.29 | [11.16, 31.42] |
| Western Europe | 8 | 31.25 | 30.56 | [14.49, 46.62] |
| East Asia | 10 | 17.0 | 17.73 | [9.59, 25.87] |
| MENA | 1 | 5.0 | 15.0 | [0, 31.26] |
| South Asia | 7 | 12.86 | 14.38 | [9.02, 19.73] |
| Southeast Asia | 6 | 15.0 | 16.43 | [1.16, 31.69] |
| Latin America & Caribbean | 2 | 20.0 | 21.67 | [6.78, 36.56] |
| Eastern Europe & Central Asia | 2 | 10.0 | 15.0 | [4.21, 25.79] |
| Oceania | 4 | 20.0 | 21.0 | [7.02, 34.98] |
| Sub-Saharan Africa | 1 | 50.0 | 37.5 | [19.1, 55.9] |

### nw_dharmic

| Region | n>0 | Sample Mean | Post. Mean mu | 95% CI |
|--------|-----|------------|--------------|--------|
| North America | 11 | 33.64 | 32.92 | [12.4, 53.43] |
| Western Europe | 3 | 11.67 | 15.0 | [5.52, 24.48] |
| East Asia | 2 | 27.5 | 26.67 | [6.55, 46.78] |
| South Asia | 4 | 46.25 | 42.0 | [20.65, 63.35] |
| Southeast Asia | 1 | 25.0 | 25.0 | [13.5, 36.5] |
| Oceania | 3 | 70.0 | 58.75 | [21.05, 96.45] |

### nw_indigenous_relational

| Region | n>0 | Sample Mean | Post. Mean mu | 95% CI |
|--------|-----|------------|--------------|--------|
| North America | 20 | 65.5 | 63.57 | [50.44, 76.7] |
| Western Europe | 13 | 53.08 | 51.07 | [31.41, 70.73] |
| East Asia | 2 | 75.0 | 58.33 | [26.14, 90.53] |
| Southeast Asia | 4 | 30.0 | 29.0 | [11.63, 46.37] |
| Latin America & Caribbean | 15 | 44.67 | 43.44 | [29.06, 57.81] |
| Eastern Europe & Central Asia | 1 | 5.0 | 15.0 | [0, 31.26] |
| Oceania | 8 | 62.5 | 58.33 | [35.66, 81.01] |
| Sub-Saharan Africa | 2 | 30.0 | 28.33 | [9.94, 46.72] |

### nw_buen_vivir

| Region | n>0 | Sample Mean | Post. Mean mu | 95% CI |
|--------|-----|------------|--------------|--------|
| North America | 4 | 50.0 | 45.0 | [35.35, 54.65] |
| Western Europe | 1 | 90.0 | 57.5 | [18.41, 96.59] |
| Sub-Saharan Africa | 1 | 50.0 | 37.5 | [19.1, 55.9] |

### dharmic_family

| Region | n>0 | Sample Mean | Post. Mean mu | 95% CI |
|--------|-----|------------|--------------|--------|
| North America | 34 | 28.24 | 28.14 | [16.9, 39.39] |
| Western Europe | 11 | 25.91 | 25.83 | [12.74, 38.93] |
| East Asia | 12 | 18.75 | 19.23 | [10.67, 27.79] |
| MENA | 1 | 5.0 | 15.0 | [0, 31.26] |
| South Asia | 11 | 25.0 | 25.0 | [12.59, 37.41] |
| Southeast Asia | 6 | 15.0 | 16.43 | [1.16, 31.69] |
| Latin America & Caribbean | 2 | 20.0 | 21.67 | [6.78, 36.56] |
| Eastern Europe & Central Asia | 2 | 10.0 | 15.0 | [4.21, 25.79] |
| Oceania | 5 | 54.0 | 49.17 | [19.85, 78.49] |
| Sub-Saharan Africa | 1 | 50.0 | 37.5 | [19.1, 55.9] |

## 3. WEIRD Comparison

Bayesian comparison of detection rates: High-WEIRD (score >= 70) vs Non-WEIRD (score < 30). P(High > Non) computed via 50,000 Monte Carlo draws from Beta posteriors.

| Framework | HW Rate | NW Rate | P(HW > NW) | Interpretation |
|-----------|---------|---------|-----------|---------------|
| nw_confucian | 0.030 (36/1221) | 0.019 (0/50) | 0.786 | Inconclusive |
| nw_ubuntu | 0.013 (15/1221) | 0.019 (0/50) | 0.486 | Inconclusive |
| nw_islamic_jurisprudence | 0.006 (7/1221) | 0.038 (1/50) | 0.049 | Strong evidence Non-WEIRD > WEIRD |
| nw_buddhist | 0.007 (8/1221) | 0.019 (0/50) | 0.310 | Inconclusive |
| nw_dharmic | 0.005 (5/1221) | 0.019 (0/50) | 0.217 | Inconclusive |
| nw_indigenous_relational | 0.025 (29/1221) | 0.019 (0/50) | 0.713 | Inconclusive |
| nw_buen_vivir | 0.005 (5/1221) | 0.019 (0/50) | 0.217 | Inconclusive |
| dharmic_family | 0.011 (13/1221) | 0.019 (0/50) | 0.440 | Inconclusive |

## 4. Dharmic Family Aggregation

dharmic_family = max(nw_buddhist, nw_dharmic) per paper. This aggregation addresses the small-n concern by combining conceptually related traditions.

- **Overall detection:** 20/2017 papers (1.0%)
- **Buddhist alone:** 11 detections
- **Dharmic alone:** 9 detections
- **Family combined:** 20 detections (gain: +9)

**Widest 95% HDIs (most uncertain):**

- Sub-Saharan Africa (n=22): HDI width = 0.209
- Oceania (n=38): HDI width = 0.180
- South Asia (n=103): HDI width = 0.071
- Eastern Europe & Central Asia (n=59): HDI width = 0.059
- Southeast Asia (n=102): HDI width = 0.051

## 5. Interpretation

### Key Findings

**Frameworks with widest credible intervals (most uncertain estimates):**

- nw_ubuntu in Sub-Saharan Africa (n=22): 95% HDI width = 0.352
- nw_indigenous_relational in Oceania (n=38): 95% HDI width = 0.230
- nw_buddhist in Sub-Saharan Africa (n=22): 95% HDI width = 0.209
- nw_indigenous_relational in Sub-Saharan Africa (n=22): 95% HDI width = 0.209
- nw_buen_vivir in Sub-Saharan Africa (n=22): 95% HDI width = 0.209
- dharmic_family in Sub-Saharan Africa (n=22): 95% HDI width = 0.209
- dharmic_family in Oceania (n=38): 95% HDI width = 0.180
- nw_dharmic in Oceania (n=38): 95% HDI width = 0.157
- nw_confucian in Sub-Saharan Africa (n=22): 95% HDI width = 0.147
- nw_islamic_jurisprudence in Sub-Saharan Africa (n=22): 95% HDI width = 0.147

**WEIRD comparison summary:**

- nw_confucian: Inconclusive (P=0.786)
- nw_ubuntu: Inconclusive (P=0.486)
- nw_islamic_jurisprudence: Strong evidence Non-WEIRD > WEIRD (P=0.049)
- nw_buddhist: Inconclusive (P=0.310)
- nw_dharmic: Inconclusive (P=0.217)
- nw_indigenous_relational: Inconclusive (P=0.713)
- nw_buen_vivir: Inconclusive (P=0.217)
- dharmic_family: Inconclusive (P=0.440)

### Caveats

1. **Small samples dominate uncertainty:** Buen Vivir (n=6 globally), Dharmic (n=9), and Buddhist (n=11) have HDI widths spanning 10-40 percentage points, making point estimates unreliable.
2. **Beta(1,1) prior is non-informative:** With n < 10, the prior contributes meaningfully to the posterior. Results should be interpreted as 'what the data suggest given no prior knowledge.'
3. **NIG model assumes normality:** Score distributions are likely bimodal (zero-inflated), so NIG posteriors should be treated as approximate.
4. **WEIRD comparison limited by Non-WEIRD sample:** Only 50 papers have weird_score < 30, creating asymmetric uncertainty.
