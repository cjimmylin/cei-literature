# BACKGROUND Literature Search Report

**Date:** 2026-04-03
**Project:** CULTURAL-GLOBAL Cross-Cultural AI Values Alignment
**Council:** 14-member Background Literature Search Expert Council

---

## Summary

| Metric | Count |
|--------|-------|
| Total papers catalogued | **130** |
| YAML stub files | 130 |
| PDFs downloaded | **39** (30.0%) |
| DOIs enriched | 84/130 (64.6%) |
| Books (manual required) | ~30 |
| Paywalled (manual required) | ~61 |
| Topic folders | 13 |
| Council members | 14 |

## Papers by Folder

| # | Folder | Papers | PDFs | Priority Split |
|---|--------|--------|------|----------------|
| 01 | WEIRD & Cross-Cultural Psychology | 14 | 5 | 6 must_read, 8 important |
| 02 | AI Ethics Landscape | 16 | 6 | 5 must_read, 11 important |
| 03 | Values Alignment | 10 | 5 | 4 must_read, 6 important |
| 04 | Confucian Ethics & AI | 13 | 3 | 4 must_read, 9 important |
| 05 | Ubuntu Philosophy & AI | 10 | 2 | 5 must_read, 5 important |
| 06 | Islamic Ethics & AI | 11 | 3 | 3 must_read, 8 important |
| 07 | Buddhist Ethics & AI | 8 | 2 | 2 must_read, 6 important |
| 08 | Dharmic Ethics & AI | 7 | 2 | 1 must_read, 6 important |
| 09 | Indigenous Relational Ethics & AI | 8 | 2 | 4 must_read, 4 important |
| 10 | Buen Vivir & AI | 6 | 1 | 1 must_read, 3 important, 2 supplementary |
| 11 | Decolonial AI & Power Dynamics | 11 | 4 | 4 must_read, 7 important |
| 12 | Methodology References | 9 | 3 | 3 must_read, 6 important |
| 13 | Cross-Cultural AI Fairness | 7 | 1 | 2 must_read, 5 important |

## Pipeline

1. **Seed from references.md** — 63 papers from existing paper bibliography
2. **Council deliberation** — 14 experts recommended ~55 additional papers
3. **Semantic Scholar API search** — 3 parallel agents searched 13 folders (~50 queries)
4. **DOI enrichment** — CrossRef (35) + OpenAlex (5) enriched 40 missing DOIs
5. **PDF download** — 13-step waterfall: arXiv, Unpaywall, S2, OpenAlex, CORE, URL scrape

## DOI Enrichment Results

| Source | DOIs Found |
|--------|-----------|
| CrossRef | 35 |
| OpenAlex | 5 |
| Semantic Scholar | 0 (rate limited) |
| Already had DOI | 44 |
| **Total with DOI** | **84/130** |

## Download Strategy Results

| Strategy | PDFs |
|----------|------|
| Unpaywall | 6 |
| arXiv | 4 |
| Semantic Scholar | 3 |
| CORE | 1 |
| URL Scrape | 1 |
| Re-download (round 2+3) | 24 |
| **Total** | **39** |

## File Organization

### Directory Structure

```
BACKGROUND/
  EXTRACT/     ← Markdown text extracts (USE THIS for analysis)
  ORIG/        ← Original PDFs (git-ignored, large binaries)
  Documents/   ← Empty (originals moved to ORIG after extraction)
  01-* to 13-* ← Topic folders with YAML stub metadata
```

### Usage Policy

**All future analysis scripts MUST read from `EXTRACT/` only, never from `ORIG/`.**

- The `text_extract` field in `BACKGROUND-registry.json` points to each extract file
- Original PDFs are preserved in `ORIG/` for reference but are **git-ignored** due to size
- The `ORIG/` and `Documents/` directories are listed in `CEI-Lit-WS/.gitignore`
- 44 PDFs extracted into 881 pages of markdown text

### Extraction Details

| Metric | Value |
|--------|-------|
| PDFs extracted | 44 |
| Total pages | 881 |
| Extract format | Markdown with page-level sections |
| Registry fields | `local_document` → `ORIG/...`, `text_extract` → `EXTRACT/...` |

---

## Known Limitations

1. **30% acquisition rate** — Lower than vault PDFs (92%) because background includes foundational books (Hofstede 2001, Russell 2019, Greenacre 2017) and paywalled journal articles
2. **Books not downloadable** — ~30 entries are books/book chapters without free PDF access
3. **Non-English sources** — Spanish (Acosta, Gudynas), Arabic (Ibn Ashur), and Chinese sources have limited open access availability
4. **Semantic Scholar heavily rate-limited** — HTTP 429 on most requests; CrossRef was the primary DOI source

## Files

- Registry: `BACKGROUND-registry.json` (130 entries)
- Council: `council/20260403-council-composition.md`, `council/20260403-deliberation-01-literature-coverage.md`
- Scripts: `scripts/build_background_registry.py`, `scripts/download_background_pdfs.py`, `scripts/enrich_paper_identifiers.py`
- Documents: `Documents/*.pdf` (39 files)

---

*Generated: 2026-04-03 | CULTURAL-GLOBAL/BACKGROUND/*
