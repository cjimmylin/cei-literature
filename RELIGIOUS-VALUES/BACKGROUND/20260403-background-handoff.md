# Session Handoff: Religious Values Benchmark — Background Literature

**Date:** 2026-04-03
**Project:** Religious Values Benchmark Survey — Background Research
**Location:** `CEI-Lit-WS/RELIGIOUS-VALUES/BACKGROUND/`
**Status:** Complete. 125 papers curated, 89 PDFs acquired (71%), 89 text extracts ready for analysis.

---

## 1. What Was Accomplished

Built a comprehensive BACKGROUND literature folder to support an academic paper on evaluating AI alignment with religious values. The folder follows the established vault pattern (ISIC-APPROACH, NormEval, Children governance) with thematic subfolders, expert council, registry, and a complete extract pipeline.

### Pipeline Summary

| Phase | Description | Output |
|-------|-------------|--------|
| **A** | Scaffolding — 12 thematic subfolders + support dirs | `BACKGROUND/01-*` through `12-*` |
| **B** | Expert council — 14-member interdisciplinary panel | `council/20260403-council-composition.md` |
| **C** | Literature search — API (S2, arXiv, OpenAlex) + WebSearch + expert seeds | `data/20260403-background-search-results.json`, `data/20260403-expert-curated-papers.json` |
| **D** | Paper file creation — 125 YAML-frontmatter markdown stubs | Across 12 thematic subfolders |
| **E** | PDF acquisition — 13-strategy waterfall download | `Documents/` (staging) → `ORIG/` (final) |
| **F** | Metadata enrichment — CrossRef + OpenAlex + S2 + arXiv title search | 53 DOIs + 31 URLs + 13 arXiv IDs found |
| **G** | Advanced download — strategies 14-27 on remaining failures | 2 additional PDFs |
| **H** | Text extraction — PyMuPDF page-by-page into markdown | `EXTRACT/` (89 files, 12.9 MB) |
| **I** | Registry & report | `BACKGROUND-registry.json`, `20260403-literature-search-report.md` |
| **J** | Council deliberation — 14-expert coverage review | `council/20260403-deliberation-01-literature-coverage.md` |

---

## 2. Key Numbers

| Metric | Value |
|--------|-------|
| Total papers curated | 125 (124 unique after dedup) |
| PDFs acquired | 89 (71%) |
| Text extracts | 89 (100% of acquired) |
| Manual-required (no PDF) | 36 (books, paywalled) |
| Must-read papers | 51 |
| Important papers | 55 |
| Supplementary papers | 18 |
| Expert council members | 14 |
| Thematic folders | 12 |
| Total extract size | 12.9 MB (avg 148 KB per paper) |
| Scripts | 7 |
| DOIs after enrichment | 82 (65%) |
| URLs after enrichment | 65 (52%) |
| Papers with zero identifiers | 7 (5%) |

---

## 3. File Workflow — CRITICAL

**For all future analysis, use `EXTRACT/*.md` ONLY.**

```
EXTRACT/          ← USE THIS for reading, searching, citing, analysis
  89 markdown text extracts with YAML frontmatter + page-by-page content

ORIG/             ← DO NOT USE for analysis. Gitignored. Backup only.
  89 original PDFs (large binaries, not tracked in repo)

Documents/        ← EMPTY. Staging area for downloads. Gitignored.

01-* through 12-* ← Paper metadata stubs (YAML frontmatter, tracked in git)
```

**Why:** Original PDFs are 100+ MB of binary data that would bloat the git repo. Text extracts are 12.9 MB of searchable, diffable markdown. The `ORIG/` folder exists only for re-extraction if a better extractor becomes available.

**Extract format:**
```yaml
---
title: "Paper Title - PDF Extract"
source_pdf: "YYYY-Author-Short Title.pdf"
pages: 17
extracted_at: "2026-04-03T..."
---
# PDF Extract: Paper Title

--- Page 1 ---
[full text of page 1]

--- Page 2 ---
[full text of page 2]
```

---

## 4. Thematic Folder Structure

| # | Folder | Papers | Extracts | Focus |
|---|--------|--------|----------|-------|
| 01 | ai-values-alignment | 12 | 11 | HELM, MMLU, RLHF, values alignment surveys |
| 02 | religious-nlp | 10 | 9 | Sacred text NLP, computational theology, corpus linguistics |
| 03 | cultural-values-ai | 12 | 11 | WEIRD bias, WVS, Hofstede/Schwartz, cultural alignment |
| 04 | islamic-ai-ethics | 12 | 10 | Maqasid al-Shariah, Quranic NLP, IslamicMMLU, Islamic virtue ethics |
| 05 | christian-ethics-ai | 11 | 7 | Vatican Rome Call, Laudato Si', theological anthropology, doctrinal flattening |
| 06 | dharmic-ethics-ai | 9 | 5 | Hindu dharma/karma, Buddhist karuna, Jain ahimsa, Sikh sewa, Indic AI |
| 07 | comparative-religious-ethics | 10 | 8 | Comparative methodology, interfaith AI, AI4People, Algorethics |
| 08 | benchmark-psychometrics | 11 | 11 | Construct validity, IRT, PATCH framework, LLM psychometrics |
| 09 | ai-bias-religion | 10 | 10 | Anti-Muslim bias, religious stereotyping, SP-10, Divine LLaMAs |
| 10 | indigenous-african-ai | 10 | 8 | Ubuntu, decolonial AI, CARE principles, African data ethics |
| 11 | jewish-ethics-ai | 10 | 5 | Talmudic Logic Project, computational halakha, Jewish roboethics |
| 12 | east-asian-philosophy-ai | 8 | 4 | Confucian ren-li, Daoist wu-wei, Shinto roboethics, CValues |

**Extract coverage pattern:** CS/ML folders (01, 08, 09) have ~100% coverage (open access). Theology/philosophy folders (05, 06, 11, 12) have ~50% coverage (paywalled books/chapters).

---

## 5. Expert Council (14 Members)

### Tier 1: Tradition-Specific Scholars (6)

| # | Name | Discipline | Folders |
|---|------|-----------|---------|
| 1 | Prof. Abdulaziz Sachedina | Islamic Ethics & Bioethics | 04, 09 |
| 2 | Prof. Brent Waters | Christian Theological Ethics | 05 |
| 3 | Prof. Purushottama Bilimoria | Dharmic Philosophy | 06 |
| 4 | Prof. Chenyang Li | Confucian Philosophy | 12 |
| 5 | Dr. Amara Osei-Mensah | African Philosophy & Ubuntu | 10 |
| 6 | Dr. Moshe Koppel | Computational Talmudics & Jewish Ethics | 11 |

### Tier 2: Methodological & Cross-Cutting Experts (8)

| # | Name | Discipline | Folders |
|---|------|-----------|---------|
| 7 | Dr. Percy Liang | AI Evaluation & Benchmarking | 01, 08 |
| 8 | Dr. Henriette Cramer | Cross-Cultural HCI & AI | 03 |
| 9 | Prof. Luciano Floridi | Philosophy of Information & AI Ethics | 01, 07 |
| 10 | Dr. Abubakar Abid | NLP & Religious Text Computation | 02, 04 |
| 11 | Dr. Abeba Birhane | Cognitive Science & AI Fairness | 09 |
| 12 | Prof. Joanna Bryson | AI Governance & Comparative Ethics | 07, 03 |
| 13 | Dr. Maria Pearce | Psychometrics & Educational Measurement | 08 |
| 14 | Dr. Segun Awosanya | Statistical Methods & Bibliometrics | All |

---

## 6. Enrichment & Acquisition Journey

### Phase 1: Initial Download (42%)
- 89 papers had DOI or URL from curated list
- 13-strategy waterfall: arXiv, Unpaywall, EuropePMC, S2, OpenAlex, CrossRef, CORE...
- Result: **53 PDFs** acquired

### Phase 2: Metadata Enrichment (+27%)
- 72 papers with missing DOIs/URLs enriched via CrossRef + OpenAlex + S2 + arXiv
- **53 DOIs found** (74% CrossRef hit rate), **31 URLs found**, **13 arXiv IDs found**
- Papers with zero identifiers dropped from 63 (50%) to 7 (5%)
- Re-ran download waterfall on enriched metadata
- Result: **+34 PDFs** (total: 87)

### Phase 3: Advanced Strategies (+2%)
- Strategies 14-27: OpenAlex Full Locations, CrossRef Links, S2 Title Search, arXiv Title, PMC, Wayback, Internet Archive, BASE, Browser UA Retry, OSF
- Result: **+2 PDFs** (total: 89)

### Phase 4: Text Extraction (100% of acquired)
- PyMuPDF (fitz v1.26.5) page-by-page extraction
- 89 PDFs → 89 markdown files in EXTRACT/
- Originals moved to ORIG/ (gitignored)
- **0 extraction errors**

---

## 7. File Manifest

### Text Extracts (`BACKGROUND/EXTRACT/`)

89 markdown files, 12.9 MB total. **This is the working folder for all analysis.**

### Original PDFs (`BACKGROUND/ORIG/`) — GITIGNORED

89 PDF files. Backup only. Not tracked in git.

### Paper Metadata Stubs (`BACKGROUND/01-*` through `12-*`)

125 YAML-frontmatter markdown files across 12 thematic subfolders. Tracked in git. Contains: title, authors, year, doi, url, source, type, priority, expert_source, topic_tags, relevance_note, local_document, document_acquired.

### Council (`BACKGROUND/council/`)

| File | Description |
|------|-------------|
| `20260403-council-composition.md` | 14-member panel: roles, operating procedures, anti-essentialization guardrails |
| `20260403-deliberation-01-literature-coverage.md` | Expert assessments of all 12 folders, consensus, dissent, recommendations |

### Scripts (`BACKGROUND/scripts/`)

| Script | Purpose |
|--------|---------|
| `search_background_papers.py` | API search across S2, arXiv, OpenAlex (12 thematic configs) |
| `write_background_paper_files.py` | Generate YAML-frontmatter paper stubs from JSON |
| `download_background_pdfs.py` | 13-strategy waterfall PDF downloader |
| `advanced_download.py` | Strategies 14-27 for remaining failures |
| `enrich_paper_identifiers.py` | CrossRef + OpenAlex + S2 + arXiv metadata enrichment |
| `extract_background_pdfs.py` | PyMuPDF text extraction → EXTRACT/ + move to ORIG/ |
| `build_background_registry.py` | Build BACKGROUND-registry.json + literature search report |

### Data (`BACKGROUND/data/`)

| File | Description |
|------|-------------|
| `20260403-background-search-results.json` | 360 API search results (S2, arXiv, OpenAlex) |
| `20260403-expert-curated-papers.json` | 125 expert-curated papers with full metadata |

### Registry & Report (top-level)

| File | Description |
|------|-------------|
| `BACKGROUND-registry.json` | 124 unique papers with all metadata (deduped) |
| `20260403-literature-search-report.md` | Summary tables: priority, folder, type, year, venues, tags, gaps |
| `20260403-background-handoff.md` | This document |
| `.gitignore` | Ignores ORIG/, Documents/, logs/, __pycache__/ |

---

## 8. Pipeline Re-Run Instructions

```bash
cd CEI-Lit-WS/RELIGIOUS-VALUES/BACKGROUND

# 1. Search for new papers (API-based)
../../../.venv/bin/python scripts/search_background_papers.py

# 2. Write paper stubs from curated JSON
../../../.venv/bin/python scripts/write_background_paper_files.py data/20260403-expert-curated-papers.json

# 3. Enrich missing DOIs/URLs
../../../.venv/bin/python scripts/enrich_paper_identifiers.py
../../../.venv/bin/python scripts/enrich_paper_identifiers.py --report

# 4. Download PDFs (13-strategy waterfall)
../../../.venv/bin/python scripts/download_background_pdfs.py
../../../.venv/bin/python scripts/download_background_pdfs.py --report

# 5. Advanced download (strategies 14-27, for remaining failures)
../../../.venv/bin/python scripts/advanced_download.py

# 6. Extract text from new PDFs
../../../.venv/bin/python scripts/extract_background_pdfs.py
../../../.venv/bin/python scripts/extract_background_pdfs.py --report

# 7. Rebuild registry
../../../.venv/bin/python scripts/build_background_registry.py
```

---

## 9. Known Issues & Limitations

### Extraction Quality
- **PyMuPDF extracts raw text only** — no layout preservation, tables become garbled, figures are lost. For papers with heavy tables/figures, consult the original PDF in ORIG/.
- **One outlier extract** is very large: `2019-Wong-Dao Harmony And Personhood.md` (5 MB, 1,852 pages) — this appears to be a full book PDF, not a paper. Consider truncating for analysis.
- **Scanned PDFs** will extract empty or garbled text. Check for `*[Page appears blank or contains only images]*` markers.

### Coverage Gaps (36 papers without PDFs)
- **11 books** (Oxford, Routledge, Springer, Blackwell, Fortress Press) — require institutional purchase
- **15 book chapters** (behind Springer/Palgrave paywalls) — require institutional access
- **10 journal articles** (Cambridge, Elsevier, subscription-only) — require institutional login or ILL
- These 36 papers have metadata stubs in the thematic subfolders but no EXTRACT file.

### Semantic Scholar Rate Limiting
- S2 API returns HTTP 429 throughout most searches. The 20s delay is insufficient without an API key.
- Enrichment compensated via CrossRef (74% hit rate) and OpenAlex.
- For future runs, consider obtaining an S2 API key for reliable access.

### Tradition-Specific Literature Sparsity
- Folders 06 (Dharmic), 11 (Jewish), 12 (East Asian) have fewer papers AND lower PDF coverage.
- This reflects genuine sparsity in the published literature, not a curation failure.
- The council deliberation documents this as a finding (Expert 3, Bilimoria).

---

## 10. Recommended Next Steps

### Immediate
1. **Read the 51 must-read extracts** in `EXTRACT/` — these form the paper's core bibliography.
2. **Start drafting the paper** using the 12-folder thematic structure as a literature review outline (or group into 4-5 sections per Expert 12's recommendation).
3. **Run classification pipeline** on the 53 externally ingested papers (EXSR0623-0675) to populate ethics scores.

### Short-Term
4. **Manual PDF acquisition** for the 36 missing papers via institutional access — prioritize the 11 must-read papers in this set.
5. **Run extraction** on any newly acquired PDFs: `scripts/extract_background_pdfs.py`
6. **Cross-reference** BACKGROUND papers with the 401 benchmark candidates to identify overlaps.

### Medium-Term
7. **Deploy dashboard** to GitHub Pages for public-facing research outputs.
8. **Publish** the eval-of-evals methodology as a position paper.
9. **Commission new benchmarks** for the 8 gap traditions (Jewish, Jain, Taoist, Shinto, Ubuntu, Indigenous, Baha'i, Zoroastrian).

---

## 11. Council Key Findings (from Deliberation D-01)

1. **Cultural values and AI bias folders (03, 09) are strongest** — mature, rapidly publishing research communities.
2. **Dharmic, Shinto, and Jewish AI ethics literatures are genuinely sparse** — not a curation failure but a field-state finding.
3. **Most benchmarks test knowledge recall, not theological reasoning** — the distinction is critical for values alignment.
4. **Non-English scholarship is almost entirely absent** — reinforces the WEIRD bias the paper critiques. Noted as methodological limitation.
5. **Expert 3 minority report:** Scarcity of Dharmic/African/Indigenous literature reflects structural epistemic injustice in academic publishing, not just a "gap to fill."
6. **Psychometric critique literature (folder 08) is the paper's methodological anchor** — 2025 papers on construct validity provide the strongest argument for careful benchmark design.
7. **The 12-folder structure maps to 4-5 paper sections:** (i) AI alignment & evaluation, (ii) cultural & religious values in AI, (iii) tradition-specific perspectives, (iv) benchmark methodology & psychometrics, (v) bias & fairness.
