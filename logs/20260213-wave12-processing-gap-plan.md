# Plan: Close Processing Gaps for Wave 1-2 Papers

## Context

Waves 1-5 of the language/religious search imported 1,044 papers (all `DATE_ADDED: 20260213`). The search agents all completed successfully — no papers were lost. However, post-import processing has gaps:

| Wave | Papers | PDFs | Extracts | Abstracts | Classified |
|------|--------|------|----------|-----------|------------|
| Wave 1 (R+A1-A5) | 322 | ~80% | ~80% | ~97% | 100% |
| Wave 2-3 (A6-B5) | 345 | ~76% | ~76% | ~100% | 100% |
| Wave 4-5 (B6-D3) | 377 | ~50% | ~50% | ~59% | 100% |

**Note:** Since all waves share `DATE_ADDED: 20260213`, the `--date` filter will process all waves together. This is beneficial — wave 4-5 has even larger gaps that will also be closed.

## Plan

### Step 1: Dry-run audit to get exact queue sizes

```bash
cd /Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS
../.venv/bin/python PYTHON/batch_download_pdfs.py 1 9999 --dry-run --date 20260213
../.venv/bin/python PYTHON/batch_extract_pdfs.py 1 9999 --dry-run --date 20260213
../.venv/bin/python PYTHON/batch_abstract_and_classify.py 1 9999 --dry-run --date 20260213
```

This tells us exactly how many papers need each processing step.

### Step 2: PDF download (Tier 1 — direct URLs)

Run `batch_download_pdfs.py` in parallel batches (5 agents), then mop-up.

**Scripts:** `PYTHON/batch_download_pdfs.py` (downloads from `external_pdf` URLs, skips papers with existing `local_pdf`)

```bash
# Split queue into 5 parallel batches (adjust END based on dry-run count)
../.venv/bin/python PYTHON/batch_download_pdfs.py 1 N --date 20260213 > logs/20260213-wave12_pdf_01.log 2>&1 &
../.venv/bin/python PYTHON/batch_download_pdfs.py N+1 2N --date 20260213 > logs/20260213-wave12_pdf_02.log 2>&1 &
../.venv/bin/python PYTHON/batch_download_pdfs.py 2N+1 3N --date 20260213 > logs/20260213-wave12_pdf_03.log 2>&1 &
../.venv/bin/python PYTHON/batch_download_pdfs.py 3N+1 4N --date 20260213 > logs/20260213-wave12_pdf_04.log 2>&1 &
../.venv/bin/python PYTHON/batch_download_pdfs.py 4N+1 TOTAL --date 20260213 > logs/20260213-wave12_pdf_05.log 2>&1 &

# Monitor progress
watch 'wc -l logs/20260213-wave12_pdf_*.log && grep SUMMARY logs/20260213-wave12_pdf_*.log'

# Sequential mop-up pass (catches ~5-7% stragglers from stdout buffering)
../.venv/bin/python PYTHON/batch_download_pdfs.py 1 9999 --date 20260213 > logs/20260213-wave12_pdf_mopup.log 2>&1
```

### Step 3: PDF download (Tier 2 — comprehensive finder)

Run `comprehensive_pdf_finder.py` on remaining papers without PDFs. Uses 13-strategy waterfall (Unpaywall, arXiv, Semantic Scholar, OpenAlex, etc.).

**Script:** `PYTHON/comprehensive_pdf_finder.py`

```bash
# Up to 3 parallel agents (Semantic Scholar rate limits are aggressive — 10s+ delay needed)
../.venv/bin/python PYTHON/comprehensive_pdf_finder.py 1 N --date 20260213 > logs/20260213-wave12_comprehensive_01.log 2>&1 &
../.venv/bin/python PYTHON/comprehensive_pdf_finder.py N+1 2N --date 20260213 > logs/20260213-wave12_comprehensive_02.log 2>&1 &
../.venv/bin/python PYTHON/comprehensive_pdf_finder.py 2N+1 TOTAL --date 20260213 > logs/20260213-wave12_comprehensive_03.log 2>&1 &

# Mop-up
../.venv/bin/python PYTHON/comprehensive_pdf_finder.py 1 9999 --date 20260213 > logs/20260213-wave12_comprehensive_mopup.log 2>&1
```

### Step 4: Extract text from newly downloaded PDFs

Run `batch_extract_pdfs.py` in parallel batches.

**Script:** `PYTHON/batch_extract_pdfs.py` (PyMuPDF extraction, writes to `PDF Extracts/YYYY/`, skips existing extracts)

```bash
# 5 parallel batches (adjust ranges based on dry-run count)
../.venv/bin/python PYTHON/batch_extract_pdfs.py 1 N --date 20260213 > logs/20260213-wave12_extract_01.log 2>&1 &
../.venv/bin/python PYTHON/batch_extract_pdfs.py N+1 2N --date 20260213 > logs/20260213-wave12_extract_02.log 2>&1 &
../.venv/bin/python PYTHON/batch_extract_pdfs.py 2N+1 3N --date 20260213 > logs/20260213-wave12_extract_03.log 2>&1 &
../.venv/bin/python PYTHON/batch_extract_pdfs.py 3N+1 4N --date 20260213 > logs/20260213-wave12_extract_04.log 2>&1 &
../.venv/bin/python PYTHON/batch_extract_pdfs.py 4N+1 TOTAL --date 20260213 > logs/20260213-wave12_extract_05.log 2>&1 &

# Monitor
watch 'wc -l logs/20260213-wave12_extract_*.log && grep SUMMARY logs/20260213-wave12_extract_*.log'

# Sequential mop-up
../.venv/bin/python PYTHON/batch_extract_pdfs.py 1 9999 --date 20260213 > logs/20260213-wave12_extract_mopup.log 2>&1
```

### Step 5: Fetch abstracts + re-classify

Run `batch_abstract_and_classify.py` to extract abstracts from PDF extracts and fill any missing classifications.

**Script:** `PYTHON/batch_abstract_and_classify.py` (extracts abstracts from PDF extract text, runs 7-stage classification)

```bash
# 5 parallel batches
../.venv/bin/python PYTHON/batch_abstract_and_classify.py 1 N --date 20260213 > logs/20260213-wave12_abstract_01.log 2>&1 &
../.venv/bin/python PYTHON/batch_abstract_and_classify.py N+1 2N --date 20260213 > logs/20260213-wave12_abstract_02.log 2>&1 &
../.venv/bin/python PYTHON/batch_abstract_and_classify.py 2N+1 3N --date 20260213 > logs/20260213-wave12_abstract_03.log 2>&1 &
../.venv/bin/python PYTHON/batch_abstract_and_classify.py 3N+1 4N --date 20260213 > logs/20260213-wave12_abstract_04.log 2>&1 &
../.venv/bin/python PYTHON/batch_abstract_and_classify.py 4N+1 TOTAL --date 20260213 > logs/20260213-wave12_abstract_05.log 2>&1 &

# Monitor
watch 'wc -l logs/20260213-wave12_abstract_*.log && grep SUMMARY logs/20260213-wave12_abstract_*.log'

# Sequential mop-up
../.venv/bin/python PYTHON/batch_abstract_and_classify.py 1 9999 --date 20260213 > logs/20260213-wave12_abstract_mopup.log 2>&1
```

### Step 6: Validate

```bash
../.venv/bin/python PYTHON/validate_all_papers.py
```

### Step 7: Generate final gap report

Quick script to count remaining gaps and list papers still missing PDFs (likely paywalled/institutional access only).

## Critical Files

- `PYTHON/batch_download_pdfs.py` — Tier 1 PDF download, 3-strategy YAML update waterfall
- `PYTHON/comprehensive_pdf_finder.py` — Tier 2, 13-strategy waterfall
- `PYTHON/batch_extract_pdfs.py` — PyMuPDF extraction, year-subdir aware
- `PYTHON/batch_abstract_and_classify.py` — Abstract extraction + 7-stage classification
- `PYTHON/validate_all_papers.py` — Final validation

## Key Constraints

- **ArXiv:** 3s delay between requests, max 5 parallel agents, `%PDF-` header verification, HTTP 429 backoff
- **Semantic Scholar:** 10s+ delay needed, gets 429 after ~4 rapid requests
- **Parallel batches:** Always run sequential mop-up pass after (catches ~5-7% stragglers)
- **YAML safety:** Scripts use REPLACE-first 3-strategy waterfall (zero duplicate YAML fields)
- **NEVER use `rm`** — always `mv` to `RECYCLE-BIN/`

## Verification

1. Dry-run counts before each step to track progress
2. `grep SUMMARY logs/20260213-wave12_*.log` to check batch results
3. `validate_all_papers.py` passes with 0 errors
4. Final gap report shows improved coverage percentages
