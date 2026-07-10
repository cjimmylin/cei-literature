# Cross-Cultural AI Values Alignment — Session 2 Handoff

**Date:** 2026-04-03
**Session:** Priorities execution + background literature assembly
**Project:** `CEI-Lit-WS/CULTURAL-GLOBAL/`
**GitHub Pages:** https://cjimmylin.github.io/cei-cultural-global/
**Dashboard repo:** https://github.com/cjimmylin/cei-cultural-global
**Previous handoff:** `METHODS/20260403-session-handoff.md` (Session 1: initial build)

---

## What Was Done This Session

Executed all 5 priorities and 6 known issues from the Session 1 handoff, then assembled comprehensive background literature. Work was done via parallel agent swarms across 8 phases.

---

## Phase 0: Fixed 6 Known Issues

| Issue | Fix | Result |
|-------|-----|--------|
| 24 validation errors | `PYTHON/fix_yaml_quote_errors.py` — fixed `paper_summary` quote mismatches | 2,315/2,315 valid |
| Buddhist undercounting (11 papers) | Added 16 strong + 7 medium Pali canon keywords to `nonwestern_scoring.py` | 11 → 26 detections |
| Western default inflation (544 papers) | `enrich_cultural_classification.py` — split "Western" into "Western (inferred)" vs explicit | 544 relabeled |
| Literature search gaps | `targeted_gap_search.py` — Pacific Island + Buddhist API searches | 57 new candidates (55 new) |
| Small non-WEIRD sample | Addressed by paper ingest (Phase 2) + Bayesian analysis (Phase 1E) | n=50 → expanded |
| Missing correspondence analysis | Built in Phase 4 | Complete |

---

## Phase 1: Council Deliberation #2 — Framework Validation

### Scripts Created
| Script | Purpose |
|--------|---------|
| `generate_audit_materials.py` | 7 per-framework audit packets with keyword hits, FP candidates |
| `select_gold_standard.py` | Stratified sampling for precision/recall validation |
| `rename_islamic_field.py` | Batch rename nw_islamic_jurisprudence → nw_islamic_ethics |
| `stats_bayesian.py` | Beta-binomial + Normal-Inverse-Gamma posteriors for small-n |
| `select_case_studies.py` | 5 qualitative case study candidates per R11 |

### Key Outcomes
- **Field rename:** `nw_islamic_jurisprudence` → `nw_islamic_ethics` across 2,315 papers + 8 scripts
- **Islamic keyword expansion:** +8 strong (akhlaq, ihsan, fitrah, taqwa, wasatiyyah, adab, amanah, khilafah) + 4 medium → 17→30 detections
- **Harmony FP filter added:** `harmony(?=.*(?:eu|regulation|act|gdpr|framework|policy|compliance))` to CONFUCIAN_FP (R2.2)
- **Bayesian analysis:** Beta-binomial posteriors for all frameworks × 10 regions. Sub-Saharan Africa Ubuntu: posterior mean 29.2%, 95% HDI [13.2%, 48.4%]
- **Within-region variance:** 11/13 frameworks have within-SD > between-range — important caveat for paper
- **Case studies:** 5 slots × 3 candidates each, including rv/nw divergence (Jigsaw: rv_islam=100, nw_islamic=0)
- **Gold standard:** 170 detected + 350 non-detected sample for precision/recall validation
- **Deliberation document:** `COUNCIL/20260403-deliberation-02-framework-validation.md` — 12 recommendations, 4 disagreements, 2 minority reports

---

## Phase 2: Ingested 216 New Papers

| Step | Script | Result |
|------|--------|--------|
| Import stubs | `import_from_search_results.py` | 216 papers created (169 main + 55 gap - 8 dedup) |
| Resolve authors | `resolve_unknown_authors.py` | 81/128 resolved (63.3% via CrossRef/OpenAlex/S2) |
| Author key prefix | CGSR0001–CGSR0216 | Cultural-Global Search Results |

**Vault total:** 2,046 → **2,315 papers**

---

## Phase 3: Re-Scored Full Corpus

### Updated Headline Numbers

| Metric | Before (2,046) | After (2,315) | Change |
|--------|---------------|---------------|--------|
| Mean WEIRD | 64.5 | **63.4** | -1.1 |
| High-WEIRD % | 59.7% | **56.0%** | -3.7% |
| NW papers (any ≥50) | 166 (8.1%) | **223 (9.6%)** | +57 |
| Confucian | 74 | 86 | +12 |
| Ubuntu | 22 | 26 | +4 |
| Islamic Ethics | 30 | 30 | +0 |
| Buddhist | 17 | 26 | **+9** |
| Dharmic | 9 | 19 | **+10** |
| Indigenous | 45 | 53 | +8 |
| Buen Vivir | 6 | 9 | +3 |
| Global South % | 15.9% | **16.7%** | +0.8% |

### Pipeline Re-Run
```
enrich_author_geography → score_nonwestern_frameworks --write-yaml →
score_weird → enrich_cultural_classification → write_all_cultural_fields →
analyze_regional_clusters → stats_clustering → stats_tests →
generate_cultural_dashboard
```

---

## Phase 4: Correspondence Analysis

- **Script:** `correspondence_analysis.py` — manual SVD on 10×12 region×framework contingency table
- **Results:** Dim1 33.2% + Dim2 23.2% = 56.4% explained variance
- **Spatial validation:** East Asia↔Confucian (closest pair), Sub-Saharan Africa↔Ubuntu, MENA↔Islamic, Western frameworks cluster at origin
- **Output:** `DATA/20260403-correspondence-analysis.json`, `PAPER/figures/correspondence-biplot.png`

---

## Phase 5: Dashboard Enhanced to 14 Tabs

| Tab | New? | Content |
|-----|------|---------|
| Overview | | KPIs + summary |
| Regional | | Profiles + radar |
| **Dendrogram** | **NEW** | ECharts tree (Ward's linkage, LR layout) |
| **CA Biplot** | **NEW** | ECharts scatter (regions circles + frameworks triangles) |
| WEIRD | | Tier distribution |
| North/South | | N/S comparison |
| East/West | | E/W axis |
| Frameworks | | 12 frameworks × 10 regions heatmap |
| Religious | | 14 traditions × 10 regions |
| Positionality | | Who studies whom |
| Temporal | | 2019→2026 trends |
| Gap Analysis | | Coverage gaps |
| Landscape | | Paper distribution |
| Methods | | Methodology transparency |

**data.js:** 174.4KB (16 constants), well under 300KB split threshold.

---

## Phase 6: Paper Polished for AIES/FAccT

| Task | Before | After |
|------|--------|-------|
| Abstract | 392 words | **228 words** (under 250 limit) |
| Figures | 3 (dendrogram, silhouette, heatmap) | **8** (+ CA biplot, WEIRD bars/histogram/radar, NW bars) |
| Figure numbering | Collision (two Figure 2s) | Sequential 1-8 |
| Image references | None | `![Figure N: Caption](figures/...)` in all sections |
| References | 33 | **62** (Hofstede, Schwartz, Constitutional AI, PRISMA, etc.) |
| Reflexivity | None | **New Section 8.6** (~200 words) |

**Figure generation script:** `generate_paper_figures.py` produces 5 print-quality figures from JSON data.

---

## BACKGROUND Literature Assembly

### Summary

| Metric | Count |
|--------|-------|
| Papers catalogued | **130** across 13 topic folders |
| PDFs downloaded | **44** (33.8%) |
| Text extracts | **44** in `EXTRACT/` (881 pages of markdown) |
| Originals | **44** in `ORIG/` (git-ignored) |
| Council members | 14 (7 tradition + 7 cross-cutting) |
| Deliberation | 1 document, 55 paper recommendations |

### Folder Distribution

| # | Folder | Papers | Extracts |
|---|--------|--------|----------|
| 01 | WEIRD / Cross-Cultural Psychology | 14 | 5 |
| 02 | AI Ethics Landscape | 16 | 6 |
| 03 | Values Alignment | 10 | 5 |
| 04 | Confucian Ethics & AI | 13 | 3 |
| 05 | Ubuntu Philosophy & AI | 10 | 2 |
| 06 | Islamic Ethics & AI | 11 | 3 |
| 07 | Buddhist Ethics & AI | 8 | 2 |
| 08 | Dharmic Ethics & AI | 7 | 2 |
| 09 | Indigenous Relational & AI | 8 | 2 |
| 10 | Buen Vivir & AI | 6 | 1 |
| 11 | Decolonial AI & Power | 11 | 4 |
| 12 | Methodology References | 9 | 3 |
| 13 | Cross-Cultural AI Fairness | 7 | 1 |

### File Organization (CRITICAL)
- **`EXTRACT/`** — Use for ALL analysis. Markdown text extracts, git-tracked.
- **`ORIG/`** — Original PDFs. Git-ignored. Reference only.
- **`Documents/`** — Empty (originals moved to ORIG after extraction). Git-ignored.

### Scripts
| Script | Purpose |
|--------|---------|
| `build_background_registry.py` | Parse references.md → seed registry + YAML stubs |
| `search_background_papers.py` | Semantic Scholar + OpenAlex per-folder queries |
| `download_background_pdfs.py` | 13-strategy waterfall |
| `advanced_download.py` | 27-strategy waterfall (adds 14 advanced strategies) |
| `enrich_paper_identifiers.py` | DOI enrichment via CrossRef/OpenAlex |
| `extract_background_pdfs.py` | PyMuPDF text extraction → markdown |

---

## Files Inventory (This Session)

### New Scripts (18)
| Script | Location | Phase |
|--------|----------|-------|
| `fix_yaml_quote_errors.py` | `PYTHON/` | 0A |
| `targeted_gap_search.py` | `SCRIPTS/` | 0D |
| `generate_audit_materials.py` | `SCRIPTS/` | 1A |
| `select_gold_standard.py` | `SCRIPTS/` | 1B |
| `rename_islamic_field.py` | `SCRIPTS/` | 1C |
| `stats_bayesian.py` | `SCRIPTS/` | 1E |
| `select_case_studies.py` | `SCRIPTS/` | 1F |
| `import_from_search_results.py` | `SCRIPTS/` | 2A |
| `resolve_unknown_authors.py` | `SCRIPTS/` | 2B |
| `correspondence_analysis.py` | `SCRIPTS/` | 4 |
| `generate_paper_figures.py` | `SCRIPTS/` | 6 |
| `build_background_registry.py` | `BACKGROUND/scripts/` | BG |
| `search_background_papers.py` | `BACKGROUND/scripts/` | BG |
| `download_background_pdfs.py` | `BACKGROUND/scripts/` | BG |
| `advanced_download.py` | `BACKGROUND/scripts/` | BG |
| `enrich_paper_identifiers.py` | `BACKGROUND/scripts/` | BG |
| `extract_background_pdfs.py` | `BACKGROUND/scripts/` | BG |
| `cultural_pdf_finder.py` | `SCRIPTS/` | 2C |

### New Data Files
| File | Size | Content |
|------|------|---------|
| `20260403-bayesian-estimates.json` | ~50KB | Posteriors for all frameworks × regions |
| `20260403-correspondence-analysis.json` | 6.4KB | SVD coordinates, explained variance |
| `20260403-author-resolutions.json` | ~30KB | API-resolved author names |
| `20260403-targeted-gap-search-results.json` | ~15KB | 57 Pacific Island + Buddhist papers |
| `BACKGROUND-registry.json` | ~80KB | 130 background paper entries |

### New Council Documents
| File | Content |
|------|---------|
| `COUNCIL/20260403-deliberation-02-framework-validation.md` | 12 recommendations, 4 disputes, 2 minority reports |
| `COUNCIL/20260403-audit-nw_*.md` (7 files) | Per-framework keyword audit packets |
| `COUNCIL/20260403-gold-standard-sample.json` | Stratified validation sample |
| `COUNCIL/20260403-gold-standard-labeling-sheet.md` | Reviewer labeling template |
| `COUNCIL/20260403-case-study-candidates.md` | 5 case study slots × 3 candidates |
| `BACKGROUND/council/20260403-council-composition.md` | 14-member background search council |
| `BACKGROUND/council/20260403-deliberation-01-literature-coverage.md` | Per-folder gap review |

---

## What Needs Doing Next

### Priority 1: Push Dashboard to GitHub Pages
- Push updated `DASHBOARD/` files (14 tabs, new data.js) to `cjimmylin/cei-cultural-global`

### Priority 2: Complete Gold Standard Validation
- Council tradition specialists label the gold standard sample (170 detected + 350 non-detected)
- Compute precision/recall/F1 per framework
- Update paper's methodology section with validation metrics

### Priority 3: PDF Acquisition for Remaining 86 Background Papers
- 30 are books (need library/purchase)
- 56 are paywalled journal articles (need institutional access)
- Consider: Google Scholar cached copies, author personal pages, institutional repositories

### Priority 4: Finish Paper for Submission
- LaTeX conversion (pandoc 3.9 available, need ACM acmart.cls template)
- Create references.bib from 10-references.md
- Finalize figure placement in LaTeX
- Submit to AIES 2027 or FAccT 2027

### Priority 5: Background-Informed Literature Review Expansion
- Use the 44 EXTRACT files to deepen Section 02 (Background) with more specific citations
- Address council-identified gaps (Central Asian indigenous, East Asian Buddhist, etc.)

---

## Reproducibility

### Full Re-Run Pipeline (10 steps)
```bash
cd CEI-Lit-WS

# 1. Score NW frameworks
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/score_nonwestern_frameworks.py

# 2. Author geography
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/enrich_author_geography.py

# 3. WEIRD scoring
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/score_weird.py

# 4. Cultural classification
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/enrich_cultural_classification.py

# 5. Cross-cultural analysis
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/analyze_regional_clusters.py

# 6. Clustering
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/stats_clustering.py

# 7. Statistical tests
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/stats_tests.py

# 8. Correspondence analysis
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/correspondence_analysis.py

# 9. Bayesian analysis
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/stats_bayesian.py

# 10. Regenerate dashboard
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/generate_cultural_dashboard.py

# Write to YAML + validate
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/score_nonwestern_frameworks.py --write-yaml
../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/write_all_cultural_fields.py
../.venv/bin/python PYTHON/validate_all_papers.py
```

**Dependencies:** numpy, scipy, scikit-learn, matplotlib, pandas, seaborn, fitz (PyMuPDF)

---

*Filed: 2026-04-03 | Session 2 | CULTURAL-GLOBAL/METHODS/*
