# Session Handoff: Religious Values Alignment Benchmark Survey

**Date:** 2026-04-03
**Project:** Religious Values Benchmark Pipeline
**Location:** `CEI-Lit-WS/RELIGIOUS-VALUES/`
**Status:** Phase 1–8 complete. Top 15 selected. 53 external papers ingested. Dashboard live.

---

## 1. What Was Accomplished

Built a complete, reusable pipeline for identifying, characterizing, scoring, and ranking religious values alignment benchmarks from the CEI Literature Vault and external sources.

### Pipeline Summary

| Phase | Description | Output |
|-------|-------------|--------|
| **0** | Expert council definition (7 members) | Embedded in council report |
| **1** | Vault scan — 2,099 papers → 401 religious benchmark candidates | `data/20260403-religious-benchmark-candidates.json` |
| **2** | External search — Semantic Scholar + arXiv + HuggingFace across 14 traditions | `data/20260403-external-search-results.json` |
| **2b** | Ingest — 53 new papers into vault (EXSR0623–EXSR0675) | `data/20260403-ingest-report.json` |
| **3** | Feature matrix — 3-axis scoring (RD 40%, PE 35%, CI 25%) for all 401 entries | `data/20260403-religious-benchmark-feature-matrix.json` |
| **4** | Format taxonomy — 12 format codes (MCQ, MRC, BIN, SCN, OPN, PSY, MTN, RAG, TXT, MUL, SHT, MIX) | `data/20260403-format-taxonomy.json` |
| **5** | Top 15 selection with diversity constraints | `data/20260403-religious-values-top15.json` |
| **6** | Eval-of-evals methodology — 7 meta-evaluation criteria | `reports/20260403-eval-of-evals-methodology.md` |
| **7** | Dashboard — 5-tab ECharts + Bootstrap HTML | `dashboard/20260403-religious-values-benchmark-dashboard.html` |
| **8** | Trial template infrastructure | `scripts/trial_religious_benchmark.py` |

---

## 2. Key Numbers

| Metric | Value |
|--------|-------|
| Vault papers scanned | 2,099 |
| Religious benchmark candidates (theological + values) | 401 |
| Demographic-only (excluded) | 29 |
| Scored in feature matrix | 401 |
| Pass all gates (RD ≥ 30 AND data available) | 46 |
| **Top 15 selected** | **15** |
| External search results | 70 |
| External papers ingested | 53 |
| External papers filtered (false positives) | 16 |
| Tradition gaps (zero gate-passing benchmarks) | 8 of 14 |

---

## 3. Top 15 Selection

Scored on 3 axes: **Religious/Theological Depth (40%)**, **Practical Ease (35%)**, **Citation Impact (25%)**.
Diversity constraints: ≥4 Abrahamic, ≥3 Dharmic, ≥1 East Asian, ≥1 African/Indigenous (gap).

| # | COMP | Tradition | Family | Format | Year | Title | Data URL |
|---|------|-----------|--------|--------|------|-------|----------|
| 1 | **50.8** | Islam | Abrahamic | RAG | 2025 | ELQV: Quran Verse Emotion Detection | `github.com/Arwaalmrzoqi/ELQV` |
| 2 | **48.2** | Islam | Abrahamic | MCQ | 2025 | Islamic Inheritance Law (1000 MCQ) | `github.com/bouchekif/inheritance_evaluation` |
| 3 | **47.9** | Christianity | Abrahamic | SCN | 2025 | UAlign: Ukrainian LLM Alignment | `huggingface.co/.../UAlign` |
| 4 | **46.7** | Islam | Abrahamic | SHT | 2025 | QIAS 2025 Shared Task: Islamic Inheritance | `gitlab.com/islamgpt1/qias_shared_task_2025` |
| 5 | **46.6** | Islam | Abrahamic | MCQ | 2025 | Break the Checkbox (multi-religion MCQ) | `github.com/ariba-k/...` |
| 6 | **44.7** | Hinduism | **Dharmic** | TXT | 2022 | Bhagavad Gita Sentiment Analysis | `github.com/sydney-machine-learning/...` |
| 7 | **44.7** | Islam | Abrahamic | MIX | 2025 | Sometimes the Model doth Preach | `github.com/HariShankar08/LLMOpinions` |
| 8 | **44.3** | Islam | Abrahamic | SCN | 2025 | PapersPlease | `github.com/yeonsuuuu28/papers-please` |
| 9 | **44.2** | Christianity | Abrahamic | MIX | 2025 | Gospel Coalition AI Christian Benchmark | `thegospelcoalition.org/ai-christian-benchmark/` |
| 10 | **43.1** | Islam | Abrahamic | MIX | 2022 | Religious Hate Speech Taxonomy | `github.com/dhfbk/religious-hate-speech` |
| 11 | **43.1** | Islam | Abrahamic | MIX | 2023 | AceGPT Arabic LLM | `github.com/FreedomIntelligence/AceGPT` |
| 12 | **43.1** | Islam | Abrahamic | MIX | 2023 | Domain-Specific Islamic LLM | `github.com/shabazpatel/domain-specific-llm` |
| 13 | **41.2** | Buddhism | **Dharmic** | MIX | 2025 | BuddhismEval Bilingual Benchmark | `huggingface.co/.../BuddhismEval` |
| 14 | **40.4** | Sikhism | **Dharmic** | MIX | 2010 | GurbaniDB (Sikh Scripture Database) | `github.com/sikher/gurbanidb` |
| 15 | **34.4** | Confucianism | **East Asian** | SCN | 2024 | Confucian Analects AI Ethics | `github.com/famous-coder/openai-case-study` |

### Diversity Achieved

| Family | Target | Achieved | Traditions |
|--------|--------|----------|------------|
| Abrahamic | ≥ 4 | **9** | Islam (7), Christianity (2) |
| Dharmic | ≥ 3 | **3** | Hinduism (1), Buddhism (1), Sikhism (1) |
| East Asian | ≥ 1 | **1** | Confucianism (1) |
| African/Indigenous | ≥ 1 | **0** | **GAP — no gate-passing benchmarks exist** |

---

## 4. Tradition Coverage (All 14 Traditions)

| Tradition | Total Candidates | Gate Passers | In Top 15 | Status |
|-----------|-----------------|-------------|-----------|--------|
| Islam | 113 | 28 | 7 | Strong |
| Christianity | 117 | 6 | 2 | Moderate |
| Hinduism | 25 | 5 | 1 | Covered |
| Buddhism | 14 | 4 | 1 | Covered |
| Confucianism | 14 | 1 | 1 | Minimal |
| Sikhism | 6 | 2 | 1 | Minimal |
| Judaism | 9 | 0 | 0 | **CRITICAL GAP** |
| Jainism | 47 | 0 | 0 | **CRITICAL GAP** (mostly FP from "ahimsa") |
| Taoism | 2 | 0 | 0 | **CRITICAL GAP** |
| Shinto | 2 | 0 | 0 | **CRITICAL GAP** |
| Ubuntu Philosophy | 4 | 0 | 0 | **CRITICAL GAP** |
| Indigenous Spirituality | 16 | 0 | 0 | **CRITICAL GAP** |
| Baha'i | 0 | 0 | 0 | **CRITICAL GAP** (zero papers) |
| Zoroastrianism | 2 | 0 | 0 | **CRITICAL GAP** |

---

## 5. Scoring Architecture

### 3-Axis Composite: `COMPOSITE = RD × 0.40 + PE × 0.35 + CI × 0.25`

#### Axis RD: Religious/Theological Depth (40%)
| Sub-field | Weight | Scale | Calibration |
|-----------|--------|-------|-------------|
| R1_traditions | 15% | Count of traditions tested | 5+ traditions = 100 |
| R2_depth | 25% | 1–5 ordinal | 5 = fiqh/exegesis, 3 = theology, 1 = demographic mention |
| R3_scriptural | 15% | 0–5 | 5 = primary text reference (Quran, Bible, Vedas) |
| R4_denominational | 10% | 0–3 | Sunni/Shia, Catholic/Protestant distinctions |
| R5_pluralism | 15% | 0–5 | Multi-tradition coverage |
| R6_grounding | 20% | 0–5 | Expert theologian validation |

#### Axis PE: Practical Ease (35%)
P1_format, P2_dataset_size, P3_data_availability, P3_url, P4_code_availability, P5_license, P7_implementability (0–10 composite), P8_scorer_type, P9_model_compat, P10_language

#### Axis CI: Citation Impact (25%)
C1_citation_count, C2_citations_per_year, C3_venue + tier, C4_downstream_adoption, C5_leaderboard, C6_community

### Hard Gates
1. RD ≥ 30
2. Data must be accessible (not "NA" or "Not available")

---

## 6. External Search & Ingest

### Search Coverage (72 queries across 5 tradition families)
- **Sources:** Semantic Scholar (56 results), arXiv (14 results)
- **HuggingFace Datasets:** queried but API rate limits yielded 0 during this session
- **Dedup:** 1 duplicate found against 2,043 vault titles
- **Quality filter:** 16 false positives removed (physics experiments, medical studies, unrelated benchmarks)

### Ingested Papers by Tradition (53 total, EXSR0623–EXSR0675)

| Tradition | Count | Notable Papers |
|-----------|-------|----------------|
| Hinduism | 18 | Bhagavad Gita as Framework for Sattvic AI, Arjuna's Dilemma, Sanskrit OCR Benchmark, Sentiment Analysis of Spiritual Teachings |
| Judaism | 9 | Ancient Hebrew Text Segmentation, Hebrew NLP Models, GPT-3 Religious Translation, AraQA Religious QA |
| Christianity | 7 | Homoousios as Christology Benchmark, Puritan Theology, African Church Syncretism |
| Indigenous | 7 | Spanish-Mazatec Parallel Corpus, Culturally Adapted Word Similarity, Indigenous Connectedness Framework |
| Islam | 5 | Al-Bayan Quran QA System, HAQA/QUQA Hadith QA, Quran Ontology Classification |
| Multi-religion | 5 | Sacred or Synthetic (LLM Reliability), Spiritual-LLM (Gita-Inspired), Cultural Values Benchmarking |
| Confucianism | 1 | **CValues** (Chinese moral values — high priority for enrichment) |
| Ubuntu | 1 | **AfriStereo** (African stereotyping evaluation — high priority for enrichment) |

### Papers Needing DATA_URL Enrichment (Priority)
These papers have high potential to fill gaps but need manual `DATA_URL` population:

1. `2023-Unknown-CValues Measuring Values Chinese Large Language.md` — CValues is likely on HuggingFace/GitHub
2. `2025-Beux-AfriStereo Culturally Grounded Dataset Evaluating Stereotypical.md` — likely on GitHub
3. `2026-Adhikari-Bhagavad Gita as Framework Sattvic AI.md` — Hindu ethics framework
4. `2022-Unknown-Benchmark Dataset PostOCR text correction Sanskrit.md` — Sanskrit NLP dataset
5. `2025-Nayan-Automatic Extraction Summarization Ethical Dilemmas from.md` — Hindu ethical dilemmas

---

## 7. File Manifest

### Data Files (`RELIGIOUS-VALUES/data/`)

| File | Size | Description |
|------|------|-------------|
| `20260403-religious-benchmark-candidates.json` | 991 KB | 401 candidates from vault scan (Phase 1) |
| `20260403-external-search-results.json` | 89 KB | 70 external discoveries (Phase 2) |
| `20260403-ingest-report.json` | 17 KB | Ingest log: 53 ingested, 16 filtered, 1 dupe |
| `20260403-religious-benchmark-feature-matrix.json` | 1.1 MB | Full 3-axis scoring for 401 entries (Phase 3) |
| `20260403-format-taxonomy.json` | 1.6 KB | 12 format codes with descriptions |
| `20260403-religious-values-top15.json` | 44 KB | Final Top 15 with all metadata |

### Reports (`RELIGIOUS-VALUES/reports/`)

| File | Description |
|------|-------------|
| `20260403-religious-values-top15-selection.md` | Main report: ranked list + detailed profiles for all 15 |
| `20260403-expert-council-deliberation.md` | 7-expert council assessment of each Top 15 entry |
| `20260403-gap-analysis.md` | 14-tradition coverage, 8 critical gaps identified |
| `20260403-eval-of-evals-methodology.md` | 7 meta-evaluation criteria + implementation trial protocol |
| `20260403-religious-values-benchmark-handoff.md` | This document |

### Scripts (`RELIGIOUS-VALUES/scripts/`)

| Script | Phase | Purpose |
|--------|-------|---------|
| `identify_religious_benchmarks.py` | 1 | Vault scan — finds papers at intersection of benchmark + religious values |
| `search_external_religious_benchmarks.py` | 2 | External API search (S2, arXiv, HuggingFace) across 14 traditions |
| `ingest_external_discoveries.py` | 2b | Quality-filtered ingest of external results into vault paper stubs |
| `build_religious_feature_matrix.py` | 3 | Constructs 3-axis RD/PE/CI scoring matrix |
| `score_religious_benchmarks.py` | 5 | Diversity-aware Top 15 selection algorithm |
| `generate_religious_dashboard.py` | 7 | Fat-data/thin-client HTML dashboard generator |
| `trial_religious_benchmark.py` | 8 | Implementation trial template generator |

### Background Literature (`RELIGIOUS-VALUES/BACKGROUND/`)

| Folder | Contents | Description |
|--------|----------|-------------|
| `EXTRACT/` | 89 markdown files | **Primary working folder** — text extracts from background PDFs. Use these for all analysis. |
| `ORIG/` | 89 PDF files | Original PDFs. **Gitignored** — not tracked in repo. Do not use directly for analysis. |
| `Documents/` | Empty (staging) | Staging area for downloads. Emptied after extraction. Gitignored. |
| `01-*` through `12-*` | 125 paper stubs | YAML-frontmatter metadata for each background paper (tracked in git). |
| `council/` | 2 files | Expert council composition + deliberation. |
| `scripts/` | 7 scripts | Search, write, download, advanced download, enrich, extract, registry. |
| `data/` | 2 JSON files | Search results and curated paper list. |
| `BACKGROUND-registry.json` | Registry | Full metadata for all 124 unique papers. |
| `20260403-literature-search-report.md` | Report | Summary tables by priority, folder, type, year, venue. |

### Dashboard (`RELIGIOUS-VALUES/dashboard/`)

| File | Size | Description |
|------|------|-------------|
| `20260403-religious-values-benchmark-dashboard.html` | 51 KB | 5-tab dashboard: Overview, Feature Matrix, Top 15, Tradition Coverage, Eval-of-Evals |

### Trials (`RELIGIOUS-VALUES/trials/`)

| File | Description |
|------|-------------|
| `20260403-trial-RV-T1-assessing-large-language-model.md` | Template for Islamic Inheritance Law MCQ trial (unfilled) |

---

## 8. Pipeline Re-Run Instructions

To re-run the full pipeline after making changes (e.g., enriching DATA_URLs, adding papers):

```bash
cd CEI-Lit-WS

# 1. Vault scan (finds new candidates)
../.venv/bin/python RELIGIOUS-VALUES/scripts/identify_religious_benchmarks.py

# 2. Feature matrix (re-scores all candidates)
../.venv/bin/python RELIGIOUS-VALUES/scripts/build_religious_feature_matrix.py

# 3. Top 15 selection (applies diversity constraints)
../.venv/bin/python RELIGIOUS-VALUES/scripts/score_religious_benchmarks.py

# 4. Dashboard (regenerates HTML with latest data)
../.venv/bin/python RELIGIOUS-VALUES/scripts/generate_religious_dashboard.py

# View dashboard:
cd RELIGIOUS-VALUES/dashboard && python3 -m http.server 8765
# Open http://localhost:8765/20260403-religious-values-benchmark-dashboard.html
```

To run a new external search (e.g., with modified queries):
```bash
../.venv/bin/python RELIGIOUS-VALUES/scripts/search_external_religious_benchmarks.py
# Then ingest results:
../.venv/bin/python RELIGIOUS-VALUES/scripts/ingest_external_discoveries.py --dry-run  # preview
../.venv/bin/python RELIGIOUS-VALUES/scripts/ingest_external_discoveries.py             # actual
# Then re-run pipeline steps 1–4 above
```

To generate an implementation trial template:
```bash
../.venv/bin/python RELIGIOUS-VALUES/scripts/trial_religious_benchmark.py                    # list available
../.venv/bin/python RELIGIOUS-VALUES/scripts/trial_religious_benchmark.py --benchmark 2      # by rank
../.venv/bin/python RELIGIOUS-VALUES/scripts/trial_religious_benchmark.py --benchmark "Quran" # by title
```

---

## 9. Known Issues & Limitations

### Scoring Heuristics
- **R2_depth and R6_grounding are keyword-heuristic**, not expert-judged. Papers with theological keywords in their abstract score higher regardless of actual depth. Manual review recommended for Top 15.
- **FaithBench** (Christian theology, 300+ test cases, GPQA-style) scores only 42.0 because its website data availability scores lower than GitHub/HuggingFace. A manual PE adjustment is warranted.
- **Gospel Coalition** similarly penalized — the data is on their website, not a standard platform.

### Tradition Coverage
- **Jainism FP problem:** 47 candidates but 0 gate-passers — most are false positives from "ahimsa" in general ethics papers, not actual Jain benchmarks. Known vault issue (documented in MEMORY.md).
- **African/Indigenous gap is structural:** These traditions have less digitized textual corpora. Benchmark construction (not just search) is needed.
- **Judaism gap despite 9 candidates:** Papers are Hebrew NLP or historical texts, not values alignment benchmarks. The tradition needs a purpose-built theological benchmark.

### External Search
- **HuggingFace Datasets API** returned 0 results during this session (likely rate limiting or search format mismatch). Manual HuggingFace search recommended for: `religion`, `theology`, `quran`, `bible`, `dharma`, `confucian`.
- **Google Scholar and PapersWithCode** not queried (no API in current pipeline). Would yield additional results.
- **Abstracts truncated to 500 chars** from S2 — insufficient for keyword scoring. Tradition assigned from search query metadata instead.

### Data Freshness
- Citation counts are from the search moment (2026-04-03) and will become stale. Re-run external search periodically.
- New papers appear weekly in this rapidly growing field (73% of candidates are from 2024–2026).

---

## 10. Recommended Next Steps

### Immediate (This Week)
1. **Enrich DATA_URLs** for the 5 priority ingested papers (CValues, AfriStereo, Bhagavad Gita, Sanskrit OCR, Hindu Ethical Dilemmas). This will unlock new gate-passers and potentially change the Top 15.
2. **Manual RD review** of Top 15 — adjust R2_depth and R6_grounding scores based on actual paper reading, not keyword heuristics. FaithBench and Gospel Coalition likely deserve score boosts.
3. **Run 2–3 implementation trials** starting with:
   - **#2 Islamic Inheritance Law** (1000 MCQ, GitHub, highest implementability)
   - **#4 QIAS 2025 Shared Task** (established competition infrastructure)
   - **#13 BuddhismEval** (bilingual, fills Dharmic diversity slot)

### Short-Term (This Month)
4. **Search HuggingFace manually** for religious datasets — `huggingface.co/datasets?search=religion`, `quran`, `bible`, `dharma`, `values`, `theology`.
5. **Enrich all 53 ingested papers** with PDF downloads, abstracts, and DATA_URLs via the standard vault enrichment pipeline (`/enrich-paper`).
6. **Run the full classification pipeline** on new papers (stages 1–7) to populate ethics scores, moral psychology, and non-Western worldview fields.
7. **Re-run pipeline** after enrichment to produce updated Top 15 with more Dharmic/East Asian/Indigenous representation.

### Medium-Term (Next Quarter)
8. **Commission new benchmarks** for gap traditions — partner with:
   - Jewish studies departments (Talmudic reasoning benchmark)
   - Buddhist studies (Pali/Sanskrit ethical reasoning)
   - African philosophy departments (Ubuntu values benchmark)
   - Indigenous knowledge holders (with appropriate cultural protocols)
9. **Publish eval-of-evals findings** — the 7-criteria meta-evaluation framework is publishable as a position paper.
10. **Deploy dashboard** to GitHub Pages for the project's public-facing research outputs.

---

## 11. Expert Council Reference

| # | Role | Primary Axis | Key Question |
|---|------|-------------|-------------|
| 1 | Theology/Religious Studies Scholar | RD (R2, R3, R6) | Does this test real theological content? |
| 2 | AI Evaluation Researcher | PE (P1, P7) | Can this run in lm-eval/Inspect/HELM? |
| 3 | Cross-Cultural Psychologist | RD (R5), PE (P10) | Are scenarios culturally native or Western-translated? |
| 4 | NLP/ML Benchmarking Expert | PE (P2, P3, P9) | How hard to implement with open+closed LLMs? |
| 5 | Comparative Religion Specialist | Diversity constraints | Does selection avoid privileging Abrahamic? |
| 6 | Psychometrician | RD (R6), CI (D4) | Is this measuring what it claims? |
| 7 | Data Scientist/Bibliometrician | CI (C1–C6) | What is scholarly impact and community uptake? |

---

## 12. Key Findings

1. **The field is brand new.** 73% of religious values benchmark candidates are from 2024–2026. This is an emerging area with enormous growth.

2. **Islam dominates** due to the Quranic QA shared task ecosystem and Arabic NLP community investment. Islamic benchmarks have the best data availability and harness compatibility.

3. **8 of 14 traditions have zero viable benchmarks.** This is the single most important finding — the religious values benchmark ecosystem is profoundly incomplete and Abrahamic-biased.

4. **Most benchmarks test knowledge, not reasoning.** They ask "what does tradition X say about Y?" rather than "apply principle X to novel dilemma Y." The distinction between factual recall and theological reasoning is critical for values alignment.

5. **Data availability is the bottleneck.** Many papers describe interesting benchmarks but don't publish their data. The gate requiring public data eliminates 77% of candidates (401 → 46 gate-passers).

6. **Format diversity is good.** The Top 15 includes MCQ, MRC, SCN, SHT, RAG, TXT, and MIX formats — enabling evaluation across different cognitive demands.

7. **The 3-axis scoring model adapts well.** The normative ethics template (ND/PE/CI) transferred cleanly to religious values (RD/PE/CI) with the RD axis redesigned for theological grounding rather than philosophical framework depth.
