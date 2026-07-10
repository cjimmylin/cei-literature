# Statistical Deepening Report

**Date:** 20260404
**Papers:** 2329

## 1. Mann-Whitney U: High-WEIRD vs Non-WEIRD

| Framework | High-WEIRD Mean | Non-WEIRD Mean | Cohen's d | p-value | Sig (BH-FDR) |
|-----------|----------------|---------------|-----------|---------|-------------|
| virtue_ethics | 4.47 | 0.0 | +0.254 | 0.0238 | No |
| deontological_ethics | 4.67 | 0.5 | +0.258 | 0.2781 | No |
| utilitarian_ethics | 6.3 | 1.2 | +0.278 | 0.1126 | No |
| care_ethics | 1.09 | 0.0 | +0.129 | 0.1450 | No |
| contractarian_ethics | 0.85 | 0.0 | +0.132 | 0.2019 | No |
| nw_confucian | 1.6 | 0.0 | +0.176 | 0.0994 | No |
| nw_ubuntu | 0.88 | 0.0 | +0.117 | 0.2941 | No |
| nw_islamic_ethics | 0.44 | 0.6 | -0.026 | 0.2424 | No |
| nw_buddhist | 0.91 | 0.0 | +0.130 | 0.1662 | No |
| nw_dharmic | 0.61 | 0.0 | +0.095 | 0.3322 | No |
| nw_indigenous_relational | 2.03 | 0.1 | +0.158 | 0.5582 | No |
| nw_buen_vivir | 0.28 | 0.0 | +0.068 | 0.6035 | No |

## 2. Kruskal-Wallis: Global North vs South vs Ambiguous

| Framework | North Mean | South Mean | Ambiguous Mean | η² | p-value | Sig |
|-----------|-----------|-----------|---------------|-----|---------|-----|
| virtue_ethics | 4.43 | 0.41 | 1.24 | 0.0135 | 0.0000 | Yes |
| deontological_ethics | 4.5 | 0.56 | 2.49 | 0.0056 | 0.0009 | Yes |
| utilitarian_ethics | 6.01 | 0.74 | 3.08 | 0.0196 | 0.0000 | Yes |
| care_ethics | 0.99 | 0.41 | 0.75 | 0.0000 | 0.3677 | No |
| contractarian_ethics | 0.77 | 0.16 | 0.48 | 0.0019 | 0.0489 | No |
| nw_confucian | 1.57 | 1.0 | 3.19 | 0.0040 | 0.0047 | Yes |
| nw_ubuntu | 0.79 | 1.49 | 0.63 | 0.0008 | 0.1627 | No |
| nw_islamic_ethics | 0.46 | 1.32 | 1.05 | 0.0060 | 0.0006 | Yes |
| nw_buddhist | 0.91 | 1.14 | 0.29 | 0.0014 | 0.0779 | No |
| nw_dharmic | 0.62 | 0.95 | 0.31 | 0.0000 | 0.6209 | No |
| nw_indigenous_relational | 1.82 | 2.5 | 0.61 | 0.0058 | 0.0007 | Yes |
| nw_buen_vivir | 0.25 | 0.34 | 0.0 | 0.0002 | 0.2954 | No |

## 3. Chi-Square: Region × Framework Detection

- χ² = 397.67, df = 99, p = 0.0
- Cramér's V = 0.3028 (medium effect)


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
| nw_confucian | 1.51 | [0.9, 2.13] |
| nw_ubuntu | 0.69 | [0.28, 1.24] |
| nw_buddhist | 0.79 | [0.39, 1.3] |
| nw_dharmic | 0.52 | [0.17, 0.95] |
| nw_indigenous_relational | 1.61 | [0.92, 2.39] |

### Western Europe (n=457)

| Framework | Mean | 95% CI |
|-----------|------|--------|
| virtue_ethics | 5.83 | [3.96, 7.89] |
| deontological_ethics | 5.05 | [3.57, 6.65] |
| utilitarian_ethics | 6.63 | [4.89, 8.4] |
| care_ethics | 0.91 | [0.32, 1.64] |
| contractarian_ethics | 0.53 | [0.16, 0.97] |
| nw_confucian | 1.64 | [0.89, 2.56] |
| nw_ubuntu | 1.12 | [0.39, 1.91] |
| nw_islamic_ethics | 0.83 | [0.18, 1.66] |
| nw_buddhist | 1.03 | [0.48, 1.78] |
| nw_indigenous_relational | 1.5 | [0.59, 2.58] |

### East Asia (n=271)

| Framework | Mean | 95% CI |
|-----------|------|--------|
| virtue_ethics | 2.4 | [1.16, 4.04] |
| deontological_ethics | 3.91 | [2.51, 5.66] |
| utilitarian_ethics | 4.19 | [2.79, 5.79] |
| care_ethics | 0.98 | [0.2, 2.14] |
| contractarian_ethics | 0.65 | [0.15, 1.29] |
| nw_confucian | 3.45 | [1.97, 5.17] |
| nw_dharmic | 0.76 | [0.22, 1.49] |
| nw_indigenous_relational | 0.55 | [0.0, 1.48] |

### MENA (n=114)

| Framework | Mean | 95% CI |
|-----------|------|--------|
| utilitarian_ethics | 1.18 | [0.66, 1.75] |
| nw_confucian | 1.1 | [0.0, 2.5] |
| nw_islamic_ethics | 3.42 | [0.79, 6.67] |

### South Asia (n=104)

| Framework | Mean | 95% CI |
|-----------|------|--------|
| deontological_ethics | 1.15 | [0.34, 2.4] |
| utilitarian_ethics | 1.25 | [0.34, 2.74] |
| care_ethics | 1.06 | [0.0, 3.03] |
| nw_confucian | 1.54 | [0.24, 3.08] |
| nw_buddhist | 0.87 | [0.24, 1.59] |
| nw_dharmic | 1.39 | [0.05, 3.17] |

### Southeast Asia (n=115)

| Framework | Mean | 95% CI |
|-----------|------|--------|
| utilitarian_ethics | 1.17 | [0.35, 2.48] |
| nw_confucian | 1.13 | [0.13, 2.57] |
| nw_ubuntu | 1.0 | [0.0, 2.57] |
| nw_islamic_ethics | 2.65 | [0.65, 5.26] |
| nw_buddhist | 1.78 | [0.22, 3.65] |
| nw_indigenous_relational | 1.04 | [0.04, 2.39] |

### Latin America & Caribbean (n=141)

| Framework | Mean | 95% CI |
|-----------|------|--------|
| virtue_ethics | 1.06 | [0.0, 2.73] |
| nw_confucian | 1.03 | [0.0, 2.45] |
| nw_islamic_ethics | 1.21 | [0.21, 2.63] |
| nw_buddhist | 0.74 | [0.21, 1.49] |
| nw_dharmic | 1.45 | [0.35, 2.98] |
| nw_indigenous_relational | 5.96 | [3.16, 9.4] |

### Eastern Europe & Central Asia (n=59)

| Framework | Mean | 95% CI |
|-----------|------|--------|
| virtue_ethics | 1.36 | [0.0, 3.81] |
| deontological_ethics | 1.69 | [0.25, 3.73] |
| utilitarian_ethics | 2.03 | [0.08, 5.59] |
| nw_confucian | 2.71 | [0.59, 5.51] |
| nw_islamic_ethics | 1.69 | [0.0, 4.24] |

### Oceania (n=46)

| Framework | Mean | 95% CI |
|-----------|------|--------|
| virtue_ethics | 3.59 | [0.0, 9.79] |
| deontological_ethics | 1.52 | [0.11, 3.81] |
| utilitarian_ethics | 1.85 | [0.11, 5.0] |
| care_ethics | 2.5 | [0.0, 7.07] |
| nw_confucian | 1.3 | [0.0, 3.91] |
| nw_ubuntu | 1.09 | [0.0, 3.26] |
| nw_buddhist | 2.5 | [0.11, 5.76] |
| nw_dharmic | 4.57 | [0.0, 11.09] |
| nw_indigenous_relational | 12.72 | [5.22, 22.07] |

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
