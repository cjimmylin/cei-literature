# Statistical Deepening Report

**Date:** 20260403
**Papers:** 2315

## 1. Mann-Whitney U: High-WEIRD vs Non-WEIRD

| Framework | High-WEIRD Mean | Non-WEIRD Mean | Cohen's d | p-value | Sig (BH-FDR) |
|-----------|----------------|---------------|-----------|---------|-------------|
| virtue_ethics | 4.47 | 0.0 | +0.254 | 0.0238 | No |
| deontological_ethics | 4.67 | 0.5 | +0.258 | 0.2781 | No |
| utilitarian_ethics | 6.3 | 1.2 | +0.278 | 0.1126 | No |
| care_ethics | 1.09 | 0.0 | +0.129 | 0.1450 | No |
| contractarian_ethics | 0.85 | 0.0 | +0.132 | 0.2019 | No |
| nw_confucian | 2.0 | 0.0 | +0.192 | 0.0894 | No |
| nw_ubuntu | 0.92 | 0.0 | +0.120 | 0.2941 | No |
| nw_islamic_ethics | 0.49 | 1.0 | -0.078 | 0.2945 | No |
| nw_buddhist | 0.96 | 0.0 | +0.134 | 0.1617 | No |
| nw_dharmic | 0.62 | 0.0 | +0.096 | 0.3322 | No |
| nw_indigenous_relational | 2.15 | 0.1 | +0.163 | 0.5126 | No |
| nw_buen_vivir | 0.28 | 0.0 | +0.068 | 0.6035 | No |

## 2. Kruskal-Wallis: Global North vs South vs Ambiguous

| Framework | North Mean | South Mean | Ambiguous Mean | η² | p-value | Sig |
|-----------|-----------|-----------|---------------|-----|---------|-----|
| virtue_ethics | 4.43 | 0.41 | 1.24 | 0.0135 | 0.0000 | Yes |
| deontological_ethics | 4.5 | 0.56 | 2.49 | 0.0056 | 0.0009 | Yes |
| utilitarian_ethics | 6.01 | 0.74 | 3.08 | 0.0196 | 0.0000 | Yes |
| care_ethics | 0.99 | 0.41 | 0.75 | 0.0000 | 0.3677 | No |
| contractarian_ethics | 0.77 | 0.16 | 0.48 | 0.0019 | 0.0489 | No |
| nw_confucian | 2.0 | 1.1 | 5.13 | 0.0114 | 0.0000 | Yes |
| nw_ubuntu | 0.83 | 1.49 | 0.63 | 0.0008 | 0.1625 | No |
| nw_islamic_ethics | 0.51 | 1.61 | 1.11 | 0.0063 | 0.0004 | Yes |
| nw_buddhist | 1.0 | 1.19 | 0.37 | 0.0007 | 0.1689 | No |
| nw_dharmic | 0.63 | 1.08 | 0.31 | 0.0000 | 0.6191 | No |
| nw_indigenous_relational | 1.93 | 2.51 | 0.67 | 0.0047 | 0.0023 | Yes |
| nw_buen_vivir | 0.25 | 0.39 | 0.0 | 0.0002 | 0.2951 | No |

## 3. Chi-Square: Region × Framework Detection

- χ² = 418.18, df = 99, p = 0.0
- Cramér's V = 0.2923 (small effect)


## 4. Bootstrap Confidence Intervals

95% CIs for regional mean framework scores (1000 iterations).

### North America (n=840)

| Framework | Mean | 95% CI |
|-----------|------|--------|
| virtue_ethics | 3.83 | [2.79, 4.99] |
| deontological_ethics | 4.51 | [3.43, 5.55] |
| utilitarian_ethics | 6.16 | [5.01, 7.41] |
| care_ethics | 1.05 | [0.52, 1.72] |
| contractarian_ethics | 1.03 | [0.56, 1.57] |
| nw_confucian | 1.89 | [1.18, 2.59] |
| nw_ubuntu | 0.76 | [0.32, 1.33] |
| nw_buddhist | 0.86 | [0.43, 1.39] |
| nw_dharmic | 0.52 | [0.17, 0.95] |
| nw_indigenous_relational | 1.67 | [0.96, 2.46] |

### Western Europe (n=457)

| Framework | Mean | 95% CI |
|-----------|------|--------|
| virtue_ethics | 5.83 | [3.96, 7.89] |
| deontological_ethics | 5.05 | [3.57, 6.65] |
| utilitarian_ethics | 6.63 | [4.89, 8.4] |
| care_ethics | 0.91 | [0.32, 1.64] |
| contractarian_ethics | 0.53 | [0.16, 0.97] |
| nw_confucian | 2.17 | [1.29, 3.22] |
| nw_ubuntu | 1.12 | [0.39, 1.91] |
| nw_islamic_ethics | 0.83 | [0.18, 1.66] |
| nw_buddhist | 1.07 | [0.5, 1.87] |
| nw_indigenous_relational | 1.66 | [0.73, 2.78] |

### East Asia (n=271)

| Framework | Mean | 95% CI |
|-----------|------|--------|
| virtue_ethics | 2.4 | [1.16, 4.04] |
| deontological_ethics | 3.91 | [2.51, 5.66] |
| utilitarian_ethics | 4.19 | [2.79, 5.79] |
| care_ethics | 0.98 | [0.2, 2.14] |
| contractarian_ethics | 0.65 | [0.15, 1.29] |
| nw_confucian | 5.83 | [3.82, 8.15] |
| nw_buddhist | 0.74 | [0.22, 1.44] |
| nw_dharmic | 0.76 | [0.22, 1.49] |
| nw_indigenous_relational | 0.59 | [0.0, 1.51] |

### MENA (n=114)

| Framework | Mean | 95% CI |
|-----------|------|--------|
| utilitarian_ethics | 1.18 | [0.66, 1.75] |
| nw_confucian | 1.27 | [0.0, 2.94] |
| nw_islamic_ethics | 3.77 | [0.96, 7.32] |

### South Asia (n=104)

| Framework | Mean | 95% CI |
|-----------|------|--------|
| deontological_ethics | 1.15 | [0.34, 2.4] |
| utilitarian_ethics | 1.25 | [0.34, 2.74] |
| care_ethics | 1.06 | [0.0, 3.03] |
| nw_confucian | 1.73 | [0.24, 3.51] |
| nw_islamic_ethics | 0.53 | [0.0, 1.54] |
| nw_buddhist | 0.87 | [0.24, 1.59] |
| nw_dharmic | 1.78 | [0.05, 4.13] |

### Southeast Asia (n=115)

| Framework | Mean | 95% CI |
|-----------|------|--------|
| utilitarian_ethics | 1.17 | [0.35, 2.48] |
| nw_confucian | 1.13 | [0.13, 2.57] |
| nw_ubuntu | 1.0 | [0.0, 2.57] |
| nw_islamic_ethics | 2.65 | [0.65, 5.26] |
| nw_buddhist | 1.78 | [0.22, 3.65] |
| nw_indigenous_relational | 1.13 | [0.09, 2.52] |

### Latin America & Caribbean (n=141)

| Framework | Mean | 95% CI |
|-----------|------|--------|
| virtue_ethics | 1.06 | [0.0, 2.73] |
| nw_confucian | 1.17 | [0.0, 2.7] |
| nw_islamic_ethics | 1.49 | [0.35, 3.12] |
| nw_buddhist | 0.89 | [0.21, 1.84] |
| nw_dharmic | 1.45 | [0.35, 2.98] |
| nw_indigenous_relational | 5.99 | [3.16, 9.4] |

### Eastern Europe & Central Asia (n=59)

| Framework | Mean | 95% CI |
|-----------|------|--------|
| virtue_ethics | 1.36 | [0.0, 3.81] |
| deontological_ethics | 1.69 | [0.25, 3.73] |
| utilitarian_ethics | 2.03 | [0.08, 5.59] |
| nw_confucian | 3.73 | [0.85, 7.29] |
| nw_islamic_ethics | 1.69 | [0.0, 4.24] |

### Oceania (n=46)

| Framework | Mean | 95% CI |
|-----------|------|--------|
| virtue_ethics | 3.59 | [0.0, 9.79] |
| deontological_ethics | 1.52 | [0.11, 3.81] |
| utilitarian_ethics | 1.85 | [0.11, 5.0] |
| care_ethics | 2.5 | [0.0, 7.07] |
| nw_confucian | 1.41 | [0.0, 4.02] |
| nw_ubuntu | 1.09 | [0.0, 3.26] |
| nw_buddhist | 2.5 | [0.11, 5.76] |
| nw_dharmic | 4.57 | [0.0, 11.09] |
| nw_indigenous_relational | 13.59 | [5.97, 23.37] |

### Sub-Saharan Africa (n=22)

| Framework | Mean | 95% CI |
|-----------|------|--------|
| deontological_ethics | 1.14 | [0.0, 2.5] |
| utilitarian_ethics | 1.59 | [0.23, 3.64] |
| care_ethics | 0.68 | [0.0, 1.82] |
| nw_ubuntu | 24.55 | [9.09, 42.73] |
| nw_buddhist | 2.27 | [0.0, 6.82] |
| nw_indigenous_relational | 2.73 | [0.0, 8.18] |
| nw_buen_vivir | 2.27 | [0.0, 6.82] |
