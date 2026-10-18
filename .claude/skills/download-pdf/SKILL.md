---
name: download-pdf
description: Download a PDF for a paper using 13-strategy waterfall, extract text, and update YAML metadata.
argument-hint: <paper-name-or-DOI-or-URL>
disable-model-invocation: true
---

# Download PDF

**Purpose:** Download a PDF for a paper, extract its text, and update YAML metadata — the full acquisition-to-extraction pipeline for a single paper.

**When to use:** When you need to obtain a PDF for a paper that has `local_pdf: "N/A"` or no `local_pdf` field. Also used after importing new papers that lack PDFs.

**Trigger:** `/download-pdf <paper-name-or-DOI-or-URL>`

## Input

The user's input is: `$ARGUMENTS`

This can be a paper name (e.g., `2024-Smith-Ethics`), a DOI, or a direct PDF URL.

---

## Overview

```
Step 1: Identify Paper & Check Status
  ├─ Find paper file in papers/
  ├─ Check local_pdf field (skip if already populated with valid link)
  └─ Extract metadata: DOI, URL, title, publication venue

Step 2: Classify & Run Acquisition Waterfall
  ├─ Category A (has DOI): unpaywall → europepmc → semantic_scholar → crossref → ...
  ├─ Category B (conference): acl_anthology → openreview → neurips_direct → ...
  └─ Category C (minimal): arxiv_title → semantic_scholar → openalex → europepmc → ...

Step 3: Download & Validate
  ├─ curl -sS -L with browser-like User-Agent
  ├─ Verify %PDF- magic bytes
  └─ Check file size > 1KB

Step 4: Store PDF in Year Directory
  └─ Move to Lit-WS-PDFs/YYYY/<paper-stem>.pdf

Step 5: Update YAML Metadata (safe regex — NEVER parse/rebuild)
  ├─ Set local_pdf: "[[Lit-WS-PDFs/YYYY/<filename>.pdf]]"
  └─ Set external_pdf: "<source-url>"

Step 6: Create PDF Extract
  ├─ Extract text via PyMuPDF (fitz)
  └─ Save to PDF Extracts/YYYY/<paper-stem>.md

Step 7: Update Extract Link & Validate
  ├─ Set pdf_extract: "PDF Extracts/YYYY/<paper-stem>.md"
  └─ Run validate_all_papers.py to confirm
```

---

## Acquisition Strategies (13-Strategy Waterfall)

The script `PYTHON/comprehensive_pdf_finder.py` implements these in priority order per category:

### Category A — Has DOI
1. `direct_download` — Use `external_pdf` URL if already set
2. `unpaywall` — Official OA lookup via DOI
3. `europepmc` — EuropePMC REST API → OA PDF or PMCID → ptpmcrender
4. `semantic_scholar` — Title/DOI search → openAccessPdf
5. `crossref` — DOI metadata → PDF content links
6. `arxiv_title` — arXiv title search for preprint versions
7. `openalex` — Title search → all OA locations (incl. preprints)
8. `doi_scrape` — Follow DOI → scrape publisher page for PDF link
9. `manual_urls` — Generate Google Scholar / ResearchGate search URLs

### Category B — Known Conference
1. `direct_download`
2. `acl_anthology` — ACL venues: construct PDF from DOI `10.18653/v1/...`
3. `openreview` — NeurIPS/ICML/ICLR papers via OpenReview API
4. `neurips_direct` — URL pattern: `-Abstract-Conference.html` → `-Paper-Conference.pdf`
5. `arxiv_title` → `semantic_scholar` → `dblp` → `openalex` → `europepmc`
6. `manual_urls`

### Category C — Minimal Metadata
1. `direct_download` → `arxiv_title` → `semantic_scholar` → `openalex` → `europepmc`
2. `core` → `philarchive` → `dblp` → `manual_urls`

---

## Key Patterns for Manual Downloads

When automated strategies fail, these patterns are useful:

| Source | Pattern |
|--------|---------|
| MDPI | `mdpi-res.com/d_attachment/{journal}/{vol}/{article}/...` or append `/pdf` to article URL |
| NeurIPS | Replace `-Abstract-Conference.html` → `-Paper-Conference.pdf` in proceedings URL |
| AAAI OJS | `ojs.aaai.org/index.php/.../article/download/{id}/{galley}/{file}` (3-part URL) |
| EuropePMC | `europepmc.org/backend/ptpmcrender.fcgi?accid=PMC{id}&blobtype=pdf` |
| ACL Anthology | `aclanthology.org/{paper-id}.pdf` (derive from DOI) |
| Research Square | Check OpenAlex `locations` for preprint PDF URLs |

---

## Step-by-Step Execution

### 1. Identify the Paper

```bash
# By name (partial match)
ls papers/ | grep -i "keyword"

# By DOI
grep -rl "doi: \"10.xxxx" papers/
```

### 2. Check Current Status

```python
# Read YAML frontmatter
local_pdf = field("local_pdf")   # Should be "N/A" or empty
doi = field("doi")
url = field("url")
```

If `local_pdf` already contains a `[[Lit-WS-PDFs/...]]` wikilink and the file exists, skip download.

### 3. Download via curl

```bash
# Standard download with browser UA
curl -sS -L \
  -o "Lit-WS-PDFs/2024/2024-Author-Title.pdf" \
  -w "%{http_code}" \
  --max-time 60 \
  --connect-timeout 15 \
  -H "User-Agent: CEI-Literature-Vault/2.0 (Academic Research)" \
  "https://example.com/paper.pdf"

# Verify %PDF- magic bytes
head -c 5 "Lit-WS-PDFs/2024/2024-Author-Title.pdf"
# Expected: %PDF-
```

### 4. Update YAML (Safe Regex)

**CRITICAL: NEVER use `parse_frontmatter()` → `rebuild_frontmatter()` round-trip.**

```python
# Safe pattern for updating a single field:
import re
content = paper_path.read_text(encoding="utf-8")
new_line = 'local_pdf: "[[Lit-WS-PDFs/2024/2024-Author-Title.pdf]]"'

content = re.sub(
    r'^local_pdf:.*$',
    new_line,
    content,
    count=1,
    flags=re.MULTILINE,
)
paper_path.write_text(content, encoding="utf-8")
```

### 5. Create PDF Extract

```python
import fitz  # PyMuPDF
from datetime import datetime

doc = fitz.open(pdf_path)
pages_text = []
for i in range(len(doc)):
    pages_text.append(f"Page {i+1}:\n{doc[i].get_text()}\n")

# Year-based extract path
extract_path = Path(f"PDF Extracts/{year}/{paper_stem}.md")
extract_path.parent.mkdir(parents=True, exist_ok=True)

frontmatter = f'''---
source_pdf: "[[Lit-WS-PDFs/{year}/{pdf_filename}]]"
extracted_date: "{datetime.now().strftime('%Y-%m-%d')}"
pages: {len(doc)}
extractor: "PyMuPDF"
---

'''
extract_path.write_text(frontmatter + "\n".join(pages_text))
```

### 6. Validate

```bash
../.venv/bin/python PYTHON/validate_all_papers.py
# Expected: All papers pass validation
```

---

## Rate Limiting

| Source | Delay |
|--------|-------|
| arXiv | 3.0s |
| Semantic Scholar | 4.0s (very aggressive rate limiting) |
| Unpaywall | 1.0s |
| EuropePMC | 1.0s |
| OpenAlex | 0.1s (10 req/s allowed) |
| CrossRef | 0.02s (50 req/s allowed) |
| Others | 1.0s default |

---

## Error Handling

| Error | Action |
|-------|--------|
| HTTP 429 (rate limited) | Back off exponentially: 10s, 20s, 30s |
| Not a PDF (HTML error page) | Delete file, try next strategy |
| File too small (<1KB) | Delete file, try next strategy |
| All strategies exhausted | Log manual search URLs, report to user |
| YAML update failed | Report warning, do not corrupt paper file |

---

## Related Scripts

| Script | Purpose |
|--------|---------|
| `PYTHON/comprehensive_pdf_finder.py` | 13-strategy waterfall (batch mode) |
| `PYTHON/advanced_pdf_finder.py` | Targeted strategies for hard-to-find papers |
| `PYTHON/batch_download_pdfs.py` | arXiv-focused batch downloader |
| `PYTHON/batch_extract_pdfs.py` | Batch PDF text extraction |

---

## Related Standards

- **YAML Safety:** `_OPERATING-SYSTEM/Standards/yaml-standards.md`
- **File Safety:** `_OPERATING-SYSTEM/Standards/file-safety.md` (NEVER use `rm`)
- **API Integration:** `_OPERATING-SYSTEM/Standards/api-integration.md`

---

**Version:** 1.1
**Updated:** 2026-02-16
