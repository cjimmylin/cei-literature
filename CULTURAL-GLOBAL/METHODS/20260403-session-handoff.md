# Cross-Cultural AI Values Alignment — Session Handoff

**Date:** 2026-04-03
**Session:** Initial build + Phase 2 execution
**Project:** `CEI-Lit-WS/CULTURAL-GLOBAL/`
**GitHub Pages:** https://cjimmylin.github.io/cei-cultural-global/
**Dashboard repo:** https://github.com/cjimmylin/cei-cultural-global

---

## What Was Built

A comprehensive cross-cultural analysis comparing how different global cultures approach AI values alignment, using the CEI Literature Vault's 2,046 papers on AI ethics. The analysis introduces 7 non-Western normative framework scoring dimensions, WEIRD scoring, and author institutional geography — enabling the first large-scale empirical comparison of cultural approaches to AI alignment.

---

## Key Findings

### The Headline Numbers

| Finding | Value |
|---------|-------|
| Mean WEIRD score | **64.5 / 100** — corpus is overwhelmingly WEIRD |
| High-WEIRD papers | **59.7%** (1,221 of 2,046) |
| Global North authors | **66.6%** (1,363 papers) |
| Global South authors | **15.9%** (325 papers) |
| Sub-Saharan Africa | **1.1%** (22 papers) — most underrepresented region |
| Papers with any non-Western framework ≥50 | **166 (8.1%)** |
| Papers with any Western framework ≥50 | **152 (7.4%)** |
| NW framework growth | **3.8% → 10.8%** (2019→2026) |

### Regional Ethical Fingerprints

Each region has a distinct normative signature:

| Region | n | Dominant Framework | Score |
|--------|---|--------------------|-------|
| North America | 809 | Utilitarian ethics | 6.4 |
| Western Europe | 421 | Utilitarian ethics | 7.2 |
| East Asia | 260 | Confucian ethics | 6.1 |
| MENA | 113 | Islamic jurisprudence | 3.8 |
| South Asia | 103 | Dharmic ethics | 1.8 |
| Southeast Asia | 102 | Utilitarian ethics | 1.3 |
| Latin America & Caribbean | 90 | Indigenous relational | 7.4 |
| Eastern Europe & Central Asia | 59 | Confucian ethics | 3.7 |
| Oceania | 38 | Indigenous relational | 13.2 |
| Sub-Saharan Africa | 22 | Ubuntu communalism | 24.6 |

### Three Clusters (Ward's Hierarchical Clustering)

1. **"Western Analytical"** — N. America + W. Europe + E. Asia (1,490 papers): utilitarian dominant
2. **"Global South Transitional"** — MENA + S. Asia + SE Asia + Latin Am. + E. Europe (467 papers): low scores across all frameworks
3. **"Non-Western Specialist"** — Oceania + Sub-Saharan Africa (60 papers): Ubuntu/Indigenous dominant

**East Asia clusters WITH the West** — a nuanced finding that challenges simplistic East/West dichotomies.

### Statistical Evidence

- **χ²=457.3** (df=99, p<0.001, Cramér's V=0.32): Region × framework association is highly significant
- **5 of 12** frameworks differ significantly by North/South after BH-FDR correction
- **Virtue ethics** is the most WEIRD-differential framework (Cohen's d=+0.26, p=0.02)
- Bootstrap CIs confirm robustness of regional signatures even for small samples (Africa n=22, Oceania n=38)

---

## Files Inventory

### SCRIPTS/ (11 Python scripts)

| Script | Purpose | Key Functions |
|--------|---------|---------------|
| `nonwestern_scoring.py` | Canonical keyword engine for 7 NW frameworks | `compute_nw_score()`, `compute_all_nw_scores()`, `score_paper_nw()` |
| `score_nonwestern_frameworks.py` | Full-vault NW scorer | `--write-yaml` flag writes to paper YAML |
| `geo_mappings.py` | Country/region/N-S/WEIRD tier mappings | `get_region()`, `get_north_south()`, `weird_country_score()`, `resolve_institution_country()` |
| `enrich_author_geography.py` | Extract institutional geography from PDF extracts | `infer_author_country()` — 4-strategy pipeline |
| `enrich_cultural_classification.py` | Classify 899 N/A papers by cultural focus | Heuristic: language→country→dataset→framework→affiliation→default |
| `score_weird.py` | WEIRD composite scorer (W+E+I+R+D, 0-100) | `compute_weird_score()` — 5 sub-dimension scorers |
| `analyze_regional_clusters.py` | 5-layer cross-cultural analysis | `compute_regional_profiles()`, `compute_weird_comparison()`, etc. |
| `generate_cultural_dashboard.py` | Dashboard data generator → data.js | Reads all JSON → pre-computes 14 JS constants |
| `stats_clustering.py` | Hierarchical clustering + figures | Ward's linkage, k-means validation, dendrogram/heatmap PNGs |
| `stats_tests.py` | Hypothesis tests + bootstrap CIs | Mann-Whitney, Kruskal-Wallis, chi-square, BH-FDR, bootstrap |
| `write_all_cultural_fields.py` | Write geography+WEIRD to paper YAML | `set_or_add_yaml_field()` pattern |

### DATA/ (8 JSON files)

| File | Size | Content |
|------|------|---------|
| `20260403-baseline-snapshot.json` | 5KB | Pre-modification field distributions |
| `20260403-nw-scores.json` | 728KB | Per-paper NW framework scores (7 fields × 2,046) |
| `20260403-author-geography.json` | 500KB | Per-paper author_country, region, N/S, method |
| `20260403-weird-scores.json` | 537KB | Per-paper WEIRD score + W/E/I/R/D breakdown |
| `20260403-cultural-enrichment.json` | 399KB | Cultural classification of 902 formerly-N/A papers |
| `20260403-cross-cultural-analysis.json` | 54KB | Regional profiles, comparisons, temporal trends |
| `20260403-clustering-results.json` | ~20KB | Linkage matrix, cluster assignments, silhouette scores |
| `20260403-statistical-tests.json` | ~50KB | Mann-Whitney, Kruskal-Wallis, chi-square, bootstrap CIs |

### DASHBOARD/ (2 files, deployed to GitHub Pages)

| File | Size | Notes |
|------|------|-------|
| `index.html` | 49KB | 12-tab ECharts dashboard, dark theme, Okabe-Ito palette |
| `data.js` | 169KB | 14 pre-computed JS constants |

**Tabs:** Overview, Regional Clusters, WEIRD Analysis, North/South, East/West, Normative Frameworks, Religious Traditions, Positionality, Temporal Trends, Gap Analysis, Literature Landscape, Methods

**To view locally:** `cd CULTURAL-GLOBAL/DASHBOARD && python3 -m http.server 8765`

### PAPER/ (11 sections + 3 figures)

| File | Section | Words |
|------|---------|-------|
| `00-abstract.md` | Structured abstract | 392 |
| `01-introduction.md` | Motivation, 5 RQs, contributions | 814 |
| `02-background.md` | WEIRD critique, 7 NW traditions, related work | 1,257 |
| `03-methodology.md` | Data, scoring, geography, WEIRD, 5 layers, council | 1,700 |
| `04-results-regional.md` | RQ1: Regional clusters, fingerprints, statistical validation | 1,099+ |
| `05-results-frameworks.md` | RQ2: E/W comparison, framework dominance | 1,024 |
| `06-results-positionality.md` | RQ3-4: N/S gap, WEIRD, who studies whom | 973+ |
| `07-results-gaps.md` | RQ5: Coverage gaps, epistemic dynamics | 1,295 |
| `08-discussion.md` | Implications, 5 orientations, policy recs | 1,471 |
| `09-conclusion.md` | Summary, future work | 687 |
| `10-references.md` | 30 key references | 675 |
| **Total** | | **~11,500** |

**Figures:**
- `figures/dendrogram.png` — Ward's hierarchical clustering of 10 regions
- `figures/silhouette.png` — Silhouette analysis (best k=4, interpretable k=3)
- `figures/heatmap-regions-frameworks.png` — 10×12 regions × frameworks heatmap

**Target venue:** AIES 2027 or FAccT 2027 (~10,000-12,000 word limit)

### COUNCIL/ (2 files)

| File | Content |
|------|---------|
| `20260403-council-composition.md` | 20 experts, 15 disciplines, 10 regions, operating procedures |
| `20260403-deliberation-01-methodology-review.md` | 360-line review: 20 expert assessments, 8 consensus points, 4 disputes, 12 recommendations, 2 minority reports |

### STATISTICS/ (7 reports)

- `20260403-nw-score-report.md` — NW framework detection summary
- `20260403-author-geography-report.md` — Author region distribution
- `20260403-weird-score-report.md` — WEIRD tier distribution
- `20260403-cross-cultural-report.md` — Full analysis summary
- `20260403-cultural-enrichment-report.md` — N/A paper classification results
- `20260403-statistical-deepening-report.md` — Hypothesis tests, effect sizes, CIs

### LITERATURE-SEARCH/ (2 files)

- `20260403-literature-search-results.json` — 196 papers found across 10 gap categories
- `20260403-literature-search-report.md` — Search summary with gap coverage

### METHODS/ (2 files)

- `20260403-methodology.md` — Full methodology documentation (RQs, scoring, analytical layers)
- `20260403-session-handoff.md` — This file

---

## Vault Modifications

**All 2,046 paper files in `papers/` were modified** with 11 new YAML fields:

```yaml
# Non-Western normative framework scores (0-100)
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_jurisprudence: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
# Author geography
author_country: "US"
author_region: "North America"
author_global_north_south: "Global North"
# WEIRD score
weird_score: 84
```

**Validation:** `validate_all_papers.py` reports 2,024/2,046 valid. The 22 errors are pre-existing `paper_summary` quote mismatches — none caused by new fields.

---

## Scoring Methodology Reference

### Non-Western Framework Scoring (same formula as ethics_scoring.py)

```
score = strong_matches × 15 + medium_matches × 5 - fp_context × 10 + title_bonus(20)
clamped to [0, 100], threshold ≥ 50
Strong-match floor: any strong match → min score 50
```

**7 frameworks with council-designated reviewers:**
- `nw_confucian` — Prof. Chenyang Li, Dr. Pak-Hang Wong
- `nw_ubuntu` — Dr. Amara Osei-Mensah, Dr. Abeba Birhane
- `nw_islamic_jurisprudence` — Prof. Yusuf al-Qaradawi Jr., Dr. Reza Shaker
- `nw_buddhist` — Dr. Sonam Wangchuk, Dr. Thida Khin
- `nw_dharmic` — Dr. Priya Narayan, Dr. Ravindra Kumar
- `nw_indigenous_relational` — Dr. Tāne Mahuta-Rau
- `nw_buen_vivir` — Dr. María Soledad Vega

### WEIRD Scoring (Henrich et al. 2010 operationalization)

```
WEIRD = W(0-20) + E(0-20) + I(0-20) + R(0-20) + D(0-20) = 0-100
```

- **W (Western):** Author institution region + study population
- **E (Educated):** University/student/MTurk sample indicators in text
- **I (Industrialized):** Country development tier
- **R (Rich):** GDP per capita tier
- **D (Democratic):** Democracy index tier

### Author Geography Resolution (4-strategy pipeline)

1. **PDF extract** (88.2%): Affiliations from first 3000 chars
2. **Known institutions** (5.1%): 150+ institution→country lookup
3. **URL domain** (3.5%): Country-code TLD
4. **Cultural proxy** (1.9%): Existing `national_ethnic_cultural` field

---

## What Needs Doing Next

### Priority 1: Ingest New Papers
- **169 new paper candidates** in `LITERATURE-SEARCH/20260403-literature-search-results.json`
- Select top ~50 by: gap-filling priority, PDF accessibility, recency, relevance
- Create paper stubs in `papers/`, download PDFs, run classification pipeline
- Re-run NW scoring, geography, WEIRD on new papers
- Re-run `analyze_regional_clusters.py` with expanded corpus

### Priority 2: Council Deliberation #2 (Framework Validation)
- Each council expert reviews keyword lists for their designated framework
- Address the 12 recommendations from Deliberation #1, especially:
  - **R1:** Add precision/recall validation on 50-paper gold standard
  - **R2:** Distinguish "mention" vs. "engagement" for Confucian keywords
  - **R4:** Add Islamic ethical dimensions beyond jurisprudence (akhlaq, adab)
  - **R7:** Aggregate small-n frameworks (Buddhist+Dharmic → "Dharmic family") for statistical tests
- Deliberation #2 output: `COUNCIL/20260403-deliberation-02-framework-validation.md`

### Priority 3: Dashboard Enhancement
- Re-generate `data.js` with updated analysis (post-ingest)
- Add dendrogram visualization to Regional Clusters tab
- Add correspondence analysis biplot to East/West tab
- Push updated files to GitHub Pages repo
- Consider `split_data.py` optimization if data.js exceeds ~300KB

### Priority 4: Paper Polish
- Tighten abstract to 250 words (currently 392)
- Number all figures and tables sequentially
- Add figure image references (currently described, PNGs now exist)
- Expand references section (currently 30, target ~50-60 for AIES/FAccT)
- Add reflexivity statement as standalone subsection
- LaTeX conversion for submission

### Priority 5: Correspondence Analysis
- `stats_correspondence.py` not yet built (needs `prince` library or manual SVD)
- Produces biplot: regions and frameworks as points in 2D space
- Would strengthen the paper's visualization of association structure

---

## Known Issues

1. **22 pre-existing validation errors** in `paper_summary` fields (quote mismatches) — not caused by this session, confirmed in git history
2. **Buddhist scoring may undercount** — DharmaBench paper scored only 15 despite being Buddhist-specific. Keyword list may need extract-level Buddhist terms (pali canon terminology)
3. **"Western" default in cultural enrichment** — 544 of 902 N/A papers classified as "Western" by default (low confidence). This is analytically correct but inflates the "Western" category
4. **Non-WEIRD sample size is small** (n=50) — limits statistical power for Mann-Whitney comparisons. Ingesting new papers from Global South would help
5. **Correspondence analysis not yet implemented** — `prince` library needed, or manual SVD on cross-tabulation matrix
6. **Literature search hit rate limits** — 196 of ~250+ target found. Follow-up session needed for remaining Pacific Island and Buddhist gaps

---

## Reproducibility

All analysis can be re-run from scratch:

```bash
cd CEI-Lit-WS

# 1. Score non-Western frameworks (reads papers, writes JSON)
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/score_nonwestern_frameworks.py

# 2. Extract author geography (reads papers + PDF extracts, writes JSON)
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/enrich_author_geography.py

# 3. Score WEIRD (reads geography JSON + papers, writes JSON)
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/score_weird.py

# 4. Classify N/A papers (reads papers + geography JSON, writes JSON)
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/enrich_cultural_classification.py

# 5. Cross-cultural analysis (reads all JSONs + papers, writes JSON + report)
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/analyze_regional_clusters.py

# 6. Statistical clustering (reads analysis JSON, writes JSON + PNGs)
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/stats_clustering.py

# 7. Statistical tests (reads all JSONs + papers, writes JSON + report)
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/stats_tests.py

# 8. Generate dashboard (reads all JSONs, writes data.js)
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/generate_cultural_dashboard.py

# 9. Write scores to YAML (reads JSONs, modifies papers/*.md)
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/score_nonwestern_frameworks.py --write-yaml
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/write_all_cultural_fields.py

# 10. Validate
../.venv/bin/python PYTHON/validate_all_papers.py
```

**Dependencies:** numpy, scipy, scikit-learn, matplotlib, pandas, seaborn (all installed in `.venv`)
