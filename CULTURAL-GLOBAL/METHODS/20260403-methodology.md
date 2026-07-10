# Cross-Cultural AI Values Alignment: Methodology

**Date:** 2026-04-03
**Project:** CULTURAL-GLOBAL
**Target venues:** AIES 2027 / FAccT 2027

---

## 1. Research Questions

1. **RQ1 (Regional Clusters):** Do distinct regional clusters of AI values alignment approaches emerge from the literature, and how do they map onto WEIRD/non-WEIRD, Global North/South, and East/West frameworks?
2. **RQ2 (Normative Frameworks):** Which normative ethical frameworks (Western and non-Western) are most associated with which regional/cultural contexts?
3. **RQ3 (Author Geography):** To what extent does author institutional geography predict the normative framework orientation of AI ethics research?
4. **RQ4 (Positionality):** What is the positionality distribution of cross-cultural AI ethics research — who studies whom?
5. **RQ5 (Coverage Gaps):** What are the critical gaps in the global coverage of AI values alignment research, and what do they reveal about epistemic power dynamics?

## 2. Data Sources

### 2.1 Primary Corpus
CEI Literature Vault (CEI-Lit-WS/): 2,046 academic papers on AI ethics published 2010-2026.

**Corpus composition:**
- 730 papers with ethics_overall ≥ 50 (core ethics-relevant subset)
- 1,316 papers below ethics threshold (NLP, benchmarks, datasets with ethical dimensions)
- Year distribution: 2025 (943), 2024 (562), 2023 (207), earlier years (334)
- Publication venues: arXiv (62%), ACL Anthology (39%), Springer, ACM, IEEE, Nature, MDPI

### 2.2 Extended Corpus (Phase 3)
Comprehensive literature search across 12+ databases targeting 200+ new papers from underrepresented regions.

## 3. Metadata Schema

### 3.1 Existing Fields (per paper)
- **5 Western normative ethics scores** (0-100): virtue_ethics, deontological_ethics, utilitarian_ethics, care_ethics, contractarian_ethics
- **14 religious tradition scores** (0-100): rv_islam through rv_indigenous
- **8 moral psychology dimensions** (0-100): mp_mft through mp_identity
- **Cultural classification**: national_ethnic_cultural (24 categories)
- **Ethics overall score** (0-100)

### 3.2 New Fields Added (this analysis)
- **7 non-Western normative framework scores** (0-100): nw_confucian, nw_ubuntu, nw_islamic_jurisprudence, nw_buddhist, nw_dharmic, nw_indigenous_relational, nw_buen_vivir
- **Author geography**: author_country (ISO 3166-1), author_region (10 macro-regions), author_global_north_south
- **WEIRD score** (0-100): Composite of Western (20) + Educated (20) + Industrialized (20) + Rich (20) + Democratic (20)
- **Study population region**, **positionality**, **cultural_comparison_type** (Phase 2B)

## 4. Scoring Methodology

### 4.1 Non-Western Framework Scoring
Same formula as established vault pipeline (ethics_scoring.py):
```
score = strong_matches × 15 + medium_matches × 5 - fp_context × 10 + title_bonus(20)
clamped to [0, 100], threshold ≥ 50
```

Keyword lists designed by council experts (each framework has a designated reviewer). Strong-match floor: any strong match guarantees minimum score of 50.

### 4.2 WEIRD Scoring
Operationalizes Henrich, Heine & Norenzayan (2010):
- **W (Western)**: Author institution region + study population geography (0-20)
- **E (Educated)**: Presence of university/student sample indicators in text (0-20)
- **I (Industrialized)**: Author country's industrial development tier (0-20)
- **R (Rich)**: GDP per capita tier of author country (0-20)
- **D (Democratic)**: Democracy level of author country (0-20)

### 4.3 Author Geography Resolution
Four-strategy pipeline:
1. **PDF extract** (88.2%): Parse institutional affiliations from first 3000 chars of extract
2. **Known institutions** (5.1%): Match against 150+ institution→country lookup table
3. **URL domain** (3.5%): Country-code TLD from paper URL
4. **Cultural proxy** (1.9%): Existing national_ethnic_cultural field as fallback

## 5. Analytical Methods

### 5.1 Layer 1: Regional Clustering
- Feature vector per region: mean scores across all 34 dimensions (5 Western + 7 non-Western + 14 religious + 8 moral psych)
- Hierarchical clustering (Ward's method) on regional profile vectors
- Validated with k-means + silhouette analysis
- Outputs: dendrogram, cluster profiles, heatmap

### 5.2 Layer 2: WEIRD Analysis
- Partition papers by WEIRD tier (4 levels)
- Compare framework score distributions: Mann-Whitney U with Bonferroni correction
- Effect sizes: Cohen's d for each framework dimension
- Visualization: parallel box plots

### 5.3 Layer 3: Global North/South
- Aggregate by author_global_north_south (3 categories)
- Kruskal-Wallis test for multi-group comparison
- Post-hoc Dunn's test with BH-FDR correction
- Framework dominance profiles per hemisphere

### 5.4 Layer 4: East/West Correspondence Analysis
- Define East (East Asia + South Asia + SE Asia) vs. West (W. Europe + N. America + Oceania)
- Correspondence analysis on region × framework cross-tabulation
- Biplot visualization of association structure
- PCA on full 34-dimension feature matrix

### 5.5 Layer 5: Positionality Analysis
- Cross-tabulate author_region × study_population_region
- Compute positionality ratios: endogenous/exogenous/collaborative
- Sankey diagram of knowledge flow
- Chi-square test for independence of author origin and study subject

## 6. Statistical Rigor

- All comparisons corrected for multiple testing (Bonferroni or BH-FDR)
- Effect sizes reported alongside p-values (Cohen's d, Cramér's V, η²)
- Bootstrap confidence intervals (1000 iterations) for key estimates
- Small-cell sensitivity analysis (Buddhist n=11, Dharmic n=9, Buen Vivir n=6)
- Aggregation strategy for sparse cells: group into "Dharmic family" or "Other non-Western"

## 7. Expert Council

20-member panel spanning 15 disciplines and 10 world regions. See `COUNCIL/20260403-council-composition.md`.

Council workflow: methodology review → data audit → framework validation → findings review → final review.

## 8. Validation & Limitations

### 8.1 Validation
- Inter-rater reliability on 50-paper manual coding sample
- Cohen's kappa for categorical, ICC for continuous
- Sensitivity analysis: results stability under alternative WEIRD operationalizations

### 8.2 Known Limitations
- Vault is English-language biased (~78% English)
- Author geography inferred, not self-reported
- Keyword-based scoring cannot capture nuanced philosophical engagement
- Cultural categories are analytical constructs, not bounded entities
- Within-region variation may exceed between-region variation
- The analysis itself is conducted from a Western institutional position

## 9. Anti-Essentialization Protocol

Following council recommendation:
1. Report confidence intervals, not just point estimates
2. Characterize findings as "tendencies in the literature" not "cultural beliefs"
3. Acknowledge within-culture heterogeneity throughout
4. Include reflexivity statement in paper
5. Regional specialists reviewed all characterizations of their traditions
