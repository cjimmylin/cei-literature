# Plan: Close Wave 3 (B1-B5) Processing Gaps

## Context

The user asked to check Wave 3 (agents B1-B5: Korean, Spanish, Slavic, Vietnamese) for gaps due to interruption. **Investigation found NO agent-level interruption** — all 5 agents completed successfully with full JSON output (212 papers across 53-69 search queries each). All 212 papers are already in the vault.

However, there are significant **processing/enrichment gaps** in the Wave 2-3 batch (LSRC papers, keys 1-345). These 306 papers were imported but many lack PDFs, abstracts, and proper author names:

| Gap | Count | % |
|-----|-------|---|
| Missing PDFs | 72/306 | 24% |
| Missing extracts | 72/306 | 24% |
| Missing abstracts | 131/306 | 43% |
| Placeholder authors | 69/306 | 23% |
| Ethics classification | 0/306 | 0% (complete) |
| LLM assessment | 0/306 | 0% (complete) |

---

## Recommended Approach: 4-Step Enrichment Pipeline

### Step 1: Fetch Missing Abstracts (131 papers)

Use existing `batch_abstract_and_classify.py` or a targeted abstract-fetch script to retrieve abstracts for 131 papers via:
- Semantic Scholar API (by DOI or title)
- CrossRef API (by DOI)
- arXiv API (by arXiv ID)
- Scrape from paper URL as fallback

**Script:** `PYTHON/batch_abstract_and_classify.py` (reuse existing, target LSRC key range)
**YAML update:** Safe regex insertion after `abstract:` field (no round-trip rebuild)
**Parallelism:** 5 background processes with START/END ranges

### Step 2: Download Missing PDFs (72 papers)

Use existing `comprehensive_pdf_finder.py` (13-strategy waterfall) targeting the 72 papers without `local_pdf`.

**Script:** `PYTHON/comprehensive_pdf_finder.py` (existing)
**Expected yield:** ~50-60% (35-43 papers) — many are regional/paywalled journals (Korean, Hebrew, CLARIN repositories)
**Rate limits:** arXiv 3s, Semantic Scholar 10s, standard backoff
**Output:** PDFs to `Lit-WS-PDFs/YYYY/`, update `local_pdf` YAML field

### Step 3: Extract PDF Text (for newly downloaded PDFs)

**Script:** `PYTHON/batch_extract_pdfs.py` (existing)
**Output:** Extracts to `PDF Extracts/YYYY/`, update `pdf_extract` YAML field

### Step 4: Resolve Placeholder Authors (69 papers)

Use existing `discover_unknown_authors.py` + `apply_author_fixes.py` pipeline:
1. Query arXiv API (primary), Semantic Scholar (secondary) for real author names
2. Validate first-author match before applying
3. Rename paper files, PDFs, extracts; update YAML

**Scripts:** `PYTHON/discover_unknown_authors.py`, `PYTHON/apply_author_fixes.py`
**Expected yield:** ~70-80% resolvable via API

---

## Critical Files

| File | Purpose |
|------|---------|
| `PYTHON/batch_abstract_and_classify.py` | Abstract fetching + classification |
| `PYTHON/comprehensive_pdf_finder.py` | PDF download (13-strategy waterfall) |
| `PYTHON/batch_extract_pdfs.py` | PDF text extraction |
| `PYTHON/discover_unknown_authors.py` | Author resolution via API |
| `PYTHON/apply_author_fixes.py` | Apply author fixes (rename + YAML) |
| `.agent/lib/yaml_utils.py` | YAML validation |
| `PYTHON/validate_all_papers.py` | Full vault validation |

---

## Execution Order

1. **Abstracts first** — fastest, highest coverage, unblocks nothing
2. **PDFs second** — slower due to rate limits, unblocks extracts
3. **Extracts third** — depends on step 2 completing
4. **Authors fourth** — independent but benefits from having abstracts for validation

Steps 1 and 4 can run in parallel. Steps 2-3 must be sequential.

---

## Verification

1. Run `../.venv/bin/python PYTHON/validate_all_papers.py` — must show 0 errors
2. Recount gaps: should show improvement in PDF/abstract/author coverage
3. Spot-check 5-10 papers for data accuracy
