# Methods: Cross-Cultural Values Alignment Benchmark Meta-Evaluation

**Date:** 2026-04-04
**Project:** `CEI-Lit-WS/CULTURAL-GLOBAL/`

## Data and Materials

### Source Corpus
The benchmark analysis drew from the CEI Literature Vault containing 2,329 AI ethics papers (2010--2026), each annotated with YAML frontmatter including `is_benchmark`, `is_eval`, `is_dataset` flags, non-Western framework scores (7 `nw_*` fields, 0--100 scale), ethics scores, moral psychology flags, and religious values scores. Papers were stored as Markdown files with structured frontmatter in `papers/`.

### PDF Extracts
For 188 of the top 200 candidates, PDF extracts (first 15,000 characters) were available in `PDF Extracts/YYYY/` directories, providing abstracts, methodology descriptions, and dataset specifications.

### External Search
Supplementary papers were identified via Semantic Scholar API (10s+ inter-request delay), arXiv API, and web search across 25 distinct queries targeting 5 benchmark groups: cross-cultural LLM benchmarks, moral judgment benchmarks, cross-cultural psychology instruments adapted for AI, tradition-specific instruments, and pluralistic alignment evaluations.

## Procedure

### Phase 1: Feature Taxonomy Design
A 12-member expert council (6 tradition specialists covering Confucian, Ubuntu, Islamic, Buddhist/Dharmic, Indigenous, and Buen Vivir ethics; 6 methodological specialists covering psychometrics, LLM evaluation, critical information studies, pluralistic alignment, comparative ethics, and statistical methods) designed a 107-feature taxonomy spanning 13 dimensions: Instrument Format (8 features), Cultural Scope (8), Language Coverage (6), Population & Sampling (8), Theoretical Grounding (10), Psychometric Properties (11), Evaluation Depth (13), LLM Administrability (10), Data & Reproducibility (6), Values Alignment (10), Cross-Cultural Validity (7), Gap & Impact (4), and Epistemic Power & Provenance (6).

### Phase 2: Vault Scan and External Search
All 2,329 papers were scanned for benchmark/eval/dataset flags and cross-referenced with non-Western framework scores. A relevance score (0--100) was computed using weighted combination of field flags (is_benchmark: +20, is_eval: +15, is_dataset: +10), non-Western framework engagement (any nw_* >= 20: +15, cap +30), ethics relevance (ethics_overall >= 50: +10), and keyword matches in title/abstract/extract (+3 each, cap +30). 1,574 candidates scored >= 20; 114 scored >= 60.

External search yielded 48 papers; 15 were not already in the vault. One additional paper (Elmahjub 2023, on Islamic AI ethics pluralism) was ingested during the follow-up session.

### Phase 3: Feature Scoring
Two-tier scoring was applied. **Automated scoring** (200 papers, relevance >= 40): regex-based extraction of format type, item count, language count, primary theory, data availability, LLM evaluation history, and 18 additional features from YAML frontmatter and PDF extract text. Average 14.6 features extracted per paper. **Deep scoring** (top 50 papers, two batches of 25): Claude Opus 4.6 read each paper's full PDF extract and scored 34 features per paper with reasoning and confidence ratings.

### Phase 4: Composite Ranking
Rankings were computed using TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) with the following weight scheme: values alignment relevance (0.20), cross-cultural scope (0.20), non-Western framework coverage (0.15), LLM administrability (0.12), psychometric quality (0.10), evaluation depth (0.10), data availability (0.08), epistemic provenance (0.05). Categorical features were converted to ordinal scales (e.g., cultural_scope: monocultural=1, pancultural=5). ELECTRE III veto thresholds were applied: papers with monocultural scope, zero non-Western frameworks, and no Global South representation were flagged. Sensitivity analysis was performed under 5 weight perturbation schemes (+-20% per dimension), yielding Kendall's W = 0.92 concordance.

### Phase 5: Claude Self-Administration Trials
Ten trials (380 total items) were self-administered by Claude Opus 4.6:
- CC1: GlobalOpinionQA (50 items, WVS/Pew themes, 8-country baselines)
- CC2: MFQ Cross-Cultural (50 items, standard MFQ-30 + 20 culturally-reframed)
- CC3: NormAd Cultural Norms (40 scenarios across 4 norm domains)
- CC4: IslamTrust (40 items across 5 Maqasid al-Shariah)
- CC5: Confucian Relational Dilemmas (30 dilemmas across wu lun)
- CC6: Ubuntu Communal Ethics (30 scenarios)
- CC7: Buddhist Ethics (30 scenarios)
- CC8: CulturalBench Commonsense (40 items, 5 world regions)
- CC9: Dharmic Ethics (30 scenarios)
- CC10: Value Conflict Cross-Cultural (40 dilemmas with multi-tradition perspectives)

For CC1, cultural alignment distances were computed as mean absolute differences between Claude's numeric responses and published human baselines per country. For CC2, Moral Foundations scores were computed per foundation domain and compared to published US liberal, US conservative, and non-WEIRD baselines. RLHF conflict zones were identified by aggregating all self-reported tension fields across trials and categorizing into themes.

### Phase 6: Computational Analyses
Twenty-five analyses were performed on the scored benchmark corpus: landscape clustering (Gower's distance, hierarchical), tradition coverage matrix, geographic coverage, psychometric quality gradient, temporal trends, language coverage, LLM evaluation landscape, epistemic power analysis, theory-practice gap, data availability audit, response format analysis, stakeholder complexity, value conflict handling, ecological/intergenerational scope, benchmark redundancy, validation chain analysis, construct mapping, annotation patterns, provenance network, cross-cultural effectiveness index, tradition-internal diversity, modality analysis, RLHF conflict potential, cultural alignment distance preparation, and gap prioritization.

### Phase 7: Dashboard and Deployment
A self-contained HTML dashboard was generated using Python f-string templating with pre-computed JavaScript data constants (ECharts 5 + Bootstrap 5.3, dark theme). Two tabs: Benchmarks (8 visualizations including ranked table, tradition coverage, cultural scope distribution, geographic distribution, psychometric quality, gap radar, data availability) and Trials (5 visualizations including MFQ profile, RLHF conflicts, cultural alignment radar, tradition engagement). Deployed to GitHub Pages via `cei-cultural-global` public repository. Playwright-verified on both localhost and deployed URL.

## Computational Environment

- Python 3.9 (`.venv/bin/python`)
- Key libraries: json, re, os, pathlib (standard library only for most scripts); scipy (clustering, distance); numpy (matrix operations)
- ECharts 5.5.0 (CDN), Bootstrap 5.3.3 (CDN), Google Fonts Inter
- Playwright MCP for dashboard verification
- GitHub Pages for deployment (static files, no server-side computation)

## Limitations and Decisions

1. **Automated feature extraction coverage:** Only 24 of 107 features could be auto-extracted from YAML frontmatter and PDF extract text. The remaining 83 features require manual or LLM-assisted scoring, which was performed only for the top 50 papers.

2. **Self-administration validity:** Claude's trial responses represent one model's alignment profile at one point in time. The knowledge-about/value-expression gap identified (accurate cultural knowledge paired with Western-default value expression) is a property of this model's RLHF training, not a universal LLM characteristic.

3. **English-language bias:** Both the vault corpus and external search were predominantly English-language. Benchmarks published in Arabic, Mandarin, Malay, or other non-English languages are systematically underrepresented.

4. **TOPSIS weight sensitivity:** While Kendall's W = 0.92 indicates strong rank stability, the weight scheme reflects council priorities and is not uniquely determined. Different stakeholders might reasonably assign different weights, particularly regarding the trade-off between psychometric rigor and cultural breadth.

5. **Tradition-specific pilot instruments (CC4-CC9):** These were designed and administered within a single session without external validation. They serve as prototypes requiring peer review, community consultation (particularly for Indigenous and Ubuntu instruments per CARE Principles), and human baseline collection before use in published research.
