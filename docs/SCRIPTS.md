# Scripts Reference

All scripts are in the `PYTHON/` directory.

## Python Environment Setup

**IMPORTANT**: Use the virtual environment for all scripts (required for PDF extraction).

### Initial Setup (One-Time)
```bash
# Create virtual environment and install dependencies
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

### Running Scripts
```bash
# Option 1: Direct path (recommended)
.venv/bin/python PYTHON/script_name.py

# Option 2: Activate environment first
source .venv/bin/activate
python PYTHON/script_name.py
deactivate  # when done
```

### Key Dependencies
- **PyMuPDF** (`fitz`): Required for `/extract-pdf-text` and PDF processing
- **PyYAML**: Required for YAML frontmatter operations
- **requests**: Required for PDF downloading and API calls

---

## Classification Pipeline (Run in Order)

```bash
# 1. Base ethics classification
python3 PYTHON/classify_ethics.py

# 2. Refine "Ethics Yes" papers
python3 PYTHON/classify_ethics_perspective.py

# 3. Refine "Ethics No" papers
python3 PYTHON/classify_non_ethics_topics.py

# 4. Cultural/religious values
python3 PYTHON/classify_cultural_religious.py

# 5. Moral psychology
python3 PYTHON/classify_moral_psych.py

# 6. Aggregate tags
python3 PYTHON/generate_newtags.py

# 7. Benchmark/eval/dataset (can run independently)
python3 PYTHON/classify_data_nature.py
```

## Report Generation

```bash
python3 PYTHON/generate_stats.py              # → STATISTICS/20260119-paper-statistics-1.md
python3 PYTHON/generate_report_v2.py          # → STATISTICS/20260119-paper-statistics-2.md
python3 PYTHON/generate_data_report.py        # → STATISTICS/20260119-data-nature-statistics.md
python3 PYTHON/generate_paper_statistics_3.py # → STATISTICS/20260119-paper-statistics-3.md
```

## PDF Extraction

**Requires PyMuPDF**: Ensure `.venv` is set up (see Python Environment Setup above).

```bash
# Extract all unprocessed PDFs
.venv/bin/python .agent/skills/extract_pdf_text/scripts/extract.py

# Extract specific PDF
.venv/bin/python .agent/skills/extract_pdf_text/scripts/extract.py "2024-Author-Title"

# Preview changes
.venv/bin/python .agent/skills/extract_pdf_text/scripts/extract.py --dry-run

# Verbose output
.venv/bin/python .agent/skills/extract_pdf_text/scripts/extract.py --verbose
```

## Data Acquisition

```bash
# Fetch abstracts from arXiv
python3 PYTHON/fetch_abstracts.py

# Multi-source abstract fetch (OpenAlex, CrossRef, arXiv, body)
python3 PYTHON/fetch_missing_abstracts.py

# Check publication status via Semantic Scholar
python3 PYTHON/check_publication_status.py
```

## Vault Management

```bash
# Import from Zotero CSV
python3 PYTHON/convert_csv_to_md.py

# Standardize filenames
python3 PYTHON/rename_papers.py

# Find papers needing enrichment
python3 PYTHON/identify_targets.py

# Sync body Authors with frontmatter
python3 PYTHON/fix_body_authors.py
python3 PYTHON/fix_body_authors.py --dry-run  # Preview
```

## Author Management

```bash
# Fix incomplete author names (arXiv API + CSV data)
python3 PYTHON/complete_author_data_fix.py

# Add wikilinks to paper bodies
python3 PYTHON/update_author_wikilinks.py

# Recombine split names
python3 PYTHON/fix_author_names_comprehensive.py

# Manual edge case fixes
python3 PYTHON/fix_remaining_authors.py
```

## Validation

```bash
# Validate all paper YAML
python3 PYTHON/validate_all_papers.py

# Validate single file
python3 PYTHON/yaml_frontmatter_utils.py papers/2016-Amodei-Concrete.md

# Pre-commit hook validation
python3 PYTHON/validate_yaml_hook.py
python3 PYTHON/validate_yaml_hook.py --staged-only
```

## Code Quality

```bash
# Run comprehensive QC/QA checks
python3 PYTHON/code_quality_check.py

# Verbose output
python3 PYTHON/code_quality_check.py --verbose

# Output to specific file
python3 PYTHON/code_quality_check.py -o logs/qc_report.md
```

**Checks performed:**
- **Critical**: Hardcoded paths, outdated format references
- **High**: Bare except clauses, YAML utility compliance
- **Medium**: Missing docstrings, duplicate functionality, excessive print statements
- **Low**: Unused imports

**Known Exclusions** (false positives):
- `generate_report_v2.py` - Only writes to STATISTICS/, not papers
- `fix_yaml_tags.py` - Fixes malformed YAML that can't use standard utilities
- `identify_benchmarks.py` - Only writes to STATISTICS/, doesn't modify papers

**Session 9 Results**:
- Initial: 150+ issues detected
- Fixed: 128 issues (all Critical, High, and Low)
- Remaining: 22 Medium (informational only)

**Major Fixes Applied**:
- 8 bare except clauses → specific exception types
- 111 unused imports removed
- 28 files converted from print() to logging
- 3 YAML safety exclusions added

## Paper Audit & Cleanup

Comprehensive scripts for finding and fixing data quality issues.

```bash
# Run full audit (generates STATISTICS/20260124-comprehensive-audit-report.md)
python3 PYTHON/comprehensive_audit.py

# Initial cleanup - fixes common issues
python3 PYTHON/comprehensive_cleanup.py --dry-run  # Preview
python3 PYTHON/comprehensive_cleanup.py            # Apply

# Enhanced cleanup - phase 2 fixes
python3 PYTHON/enhanced_cleanup.py --dry-run
python3 PYTHON/enhanced_cleanup.py

# Smart citation deduplication
python3 PYTHON/smart_citation_cleanup.py --dry-run
python3 PYTHON/smart_citation_cleanup.py

# Fix specific truncated abstracts
python3 PYTHON/fix_truncated_abstracts.py
```

### What Each Cleanup Script Fixes

| Script | Fixes |
|--------|-------|
| `comprehensive_cleanup.py` | Duplicate citations, local_pdf format, type normalization, ethics consistency, abstract placeholders |
| `enhanced_cleanup.py` | N/A local_pdf values, broken author wikilinks |
| `smart_citation_cleanup.py` | Redundant citation entries (keeps highest count per source/date) |
| `fix_truncated_abstracts.py` | Specific papers with content warnings instead of abstracts |

### Full Audit Workflow

```bash
# 1. Run audit
python3 PYTHON/comprehensive_audit.py

# 2. Review report
cat STATISTICS/20260124-comprehensive-audit-report.md

# 3. Apply cleanups
python3 PYTHON/comprehensive_cleanup.py
python3 PYTHON/enhanced_cleanup.py
python3 PYTHON/smart_citation_cleanup.py

# 4. Validate
python3 PYTHON/validate_all_papers.py

# 5. Re-audit to verify
python3 PYTHON/comprehensive_audit.py
```

## Script Classification Logic

| Script | Field(s) Set |
|--------|--------------|
| `classify_ethics.py` | `ethics_overall`, `virtue_ethics`, `deontological_ethics`, `utilitarian_ethics` |
| `classify_ethics_perspective.py` | `ethics_perspective` |
| `classify_non_ethics_topics.py` | `research_topic` |
| `classify_cultural_religious.py` | `national_ethnic_cultural`, `religious_values` |
| `classify_moral_psych.py` | `moral_psychology` |
| `classify_data_nature.py` | `is_benchmark`, `is_eval`, `is_dataset`, `data_description`, `data_metrics` |
| `generate_newtags.py` | `newtags` |


---

## PDF Downloading & Recovery

Scripts for downloading and recovering PDFs from multiple sources.

### Enhanced PDF Downloader

**Script**: `PYTHON/pdf_downloader_enhanced.py`

Multi-source PDF downloader with intelligent fallback and progress tracking.

```bash
# Download all missing PDFs
python3 PYTHON/pdf_downloader_enhanced.py

# Resume from checkpoint (if interrupted)
python3 PYTHON/pdf_downloader_enhanced.py --resume

# Limit to first 100 papers
python3 PYTHON/pdf_downloader_enhanced.py --limit 100
```

**Features**:
- Multi-source fallback (arXiv → ACL → OpenReview → DOI → URLs)
- Automatic DOI discovery from URLs
- Smart retry with exponential backoff
- Progress checkpointing every 10 papers
- Comprehensive logging
- Rate limiting (0.5s between downloads)

**Download Priority**:
1. arXiv (95% success) - `10.48550/arXiv.*` DOIs
2. ACL Anthology (90% success) - NLP/CL papers
3. OpenReview (85% success) - ML conferences
4. DOI resolution (40% success) - Generic DOI lookup
5. External PDF URL (60% success) - Direct links
6. Main URL (30% success) - Landing pages

**Checkpoint File**: `logs/download_checkpoint.json`

**Session 10 Results** (2026-01-24 recovery):
- Recovered: 474 PDFs from 0 (82.3%)
- Sources: arXiv (200+), ACL (60+), OpenReview (20+), Others (190+)
- Time: ~2 hours automated

### DOI Discovery

**Script**: `PYTHON/doi_discovery.py`

Discovers missing DOIs using CrossRef, Semantic Scholar, and URL parsing.

```bash
# Find all missing DOIs
python3 PYTHON/doi_discovery.py

# Check first 50 papers
python3 PYTHON/doi_discovery.py --limit 50
```

**Discovery Methods**:
1. **CrossRef API** - Title-based fuzzy matching
2. **Semantic Scholar API** - Title + author validation
3. **URL Pattern Extraction**:
   - arXiv: `arxiv.org/abs/{id}` → `10.48550/arXiv.{id}`
   - OSF: `osf.io/{id}` → `10.31219/osf.io/{id}`
   - SSRN: `ssrn.com/abstract={id}` → `10.2139/ssrn.{id}`
   - PubMed: API lookup for DOI
4. **DOI Extraction from URLs** - Regex pattern matching

**Output**: `logs/discovered_dois.json`

**Session 10 Results**:
- Found: 7 new DOIs (from 48 papers without DOIs)
- Methods: CrossRef (5), Semantic Scholar (1), URL parsing (1)
- Successfully downloaded: 2 PDFs using new DOIs

**Rate Limiting**: 0.5s between API requests

### Legacy Download Scripts

These older scripts are superseded by the enhanced downloader but retained for reference:

**Script**: `PYTHON/batch_pdf_downloader.py` (Legacy)
- Basic batch downloader with resume capability
- Use enhanced downloader instead

**Script**: `PYTHON/smart_pdf_downloader.py` (Legacy)
- URL discovery and download
- Missing multi-source fallback

**Script**: `PYTHON/download_missing_pdfs.py` (Legacy)
- Simple download from external_pdf field
- No fallback or retry logic

### Manual Download Guide

For papers that require manual intervention (typically 15-20%):

**Reference Files Generated**:
- `logs/20260124-SEARCH_GUIDE.md` - Complete guide with DOIs and search queries
- `logs/20260124-papers_to_search.csv` - CSV for batch processing
- `logs/20260124-papers_to_find_UPDATED.json` - Machine-readable data

**Manual Sources** (when automated fails):
- **Sci-Hub**: For papers with DOI (paste DOI directly)
- **Anna's Archive**: Search by DOI or title
- **LibGen**: For books and some journals
- **Google Scholar**: Sometimes links to free PDFs
- **ResearchGate/Academia.edu**: Author uploads

**Critical**: Save PDFs with exact filename from `papers/` directory:
```bash
# Example: papers/2024-Smith-Paper Title.md
# Save as: PDFs/2024-Smith-Paper Title.pdf
```

### Verification Commands

```bash
# Count PDFs
ls PDFs/*.pdf | wc -l

# Find 0-byte files
find PDFs -name "*.pdf" -size 0

# Verify PDF format
file PDFs/*.pdf | grep -v "PDF document"

# Coverage report
python3 << EOF
from pathlib import Path
papers = len(list(Path('papers').glob('*.md')))
pdfs = len(list(Path('PDFs').glob('*.pdf')))
extracts = len(list(Path('PDF Extracts').glob('*.md')))
print(f"Papers: {papers}")
print(f"PDFs: {pdfs} ({100*pdfs/papers:.1f}%)")
print(f"Extracts: {extracts} ({100*extracts/papers:.1f}%)")
EOF
```

### Related Documentation

- [docs/PDF_RECOVERY_GUIDE.md](PDF_RECOVERY_GUIDE.md) - Complete recovery procedures
- [docs/WORKFLOWS.md](WORKFLOWS.md) - PDF download workflows
- [docs/KNOWN_ISSUES.md](KNOWN_ISSUES.md) - Common download problems

---

## AI Labs Management

Scripts for managing the AI Labs folder (PDFs, extracts, overviews for AI company documentation).

### PDF Extraction for AI Labs

**Script**: `PYTHON/extract_ai_labs_pdfs.py`

Extracts text from all PDFs in the `AI Labs/` folder into searchable markdown files.

```bash
# Extract text from all AI Labs PDFs
python3 PYTHON/extract_ai_labs_pdfs.py
```

**Features**:
- Finds all unique PDFs in `AI Labs/` (handles duplicates in Papers/ folders)
- Creates markdown extracts with YAML frontmatter
- Includes company, model, page count, extraction timestamp
- Saves to `PDF Extracts/AI Labs/Company-filename.md`

**Extract YAML Format**:
```yaml
---
title: "Model Name"
source_pdf: "AI Labs/Company/Model/filename.pdf"
company: "Company"
pages: 120
extracted_at: "2026-01-25T04:43:43.635840"
type: "ai_lab_paper"
---
```

**Session Statistics (Jan 2026)**:
- 111 unique PDFs extracted
- 140 total PDFs (29 duplicates handled)
- 14 AI labs covered

### Move Extracts to Model Folders

**Script**: `PYTHON/move_ai_lab_extracts.py`

Moves extracts from generic folder to model-specific folders alongside source PDFs.

```bash
# Move extracts to model folders
python3 PYTHON/move_ai_lab_extracts.py
```

**Before**: `PDF Extracts/AI Labs/Company-filename.md`
**After**: `AI Labs/Company/Model/filename.md`

**Features**:
- Reads `source_pdf` field from YAML frontmatter to determine destination
- Removes company prefix from filename when moving
- Reports moved/skipped/errors

### Generate Lab Overviews

For generating overview.md files for AI labs, use Claude directly:

```
# Single lab
Create an overview.md for [Lab Name] summarizing all models based on the PDF extracts

# All labs (parallel agents)
Create overview.md files for each AI lab using parallel agents
```

**Overview structure**:
- Lab introduction
- Model summary table (name, year, type, parameters, features)
- Detailed sections for each model family
- Links to source PDFs

### AI Labs Workflow

```bash
# 1. Download papers (use /download-lab-papers skill)

# 2. Extract text from all PDFs
python3 PYTHON/extract_ai_labs_pdfs.py

# 3. Move extracts to model folders
python3 PYTHON/move_ai_lab_extracts.py

# 4. Generate overviews (via Claude)
```

### Related Documentation

- [SESSION_2026_01_25_AI_LABS_EXTRACTS.md](SESSION_2026_01_25_AI_LABS_EXTRACTS.md) - Detailed session notes
- [.claude/skills/download-lab-papers.md](../.claude/skills/download-lab-papers.md) - Paper download skill

---

## Batch Paper Import

Scripts for importing multiple papers from research into the vault.

### Create Virtue Ethics Papers (Template)

**Script**: `PYTHON/create_virtue_ethics_papers.py`

Batch creates paper profiles from a predefined list of paper metadata.

```bash
# Run to create all defined papers
python3 PYTHON/create_virtue_ethics_papers.py
```

**Features**:
- Defines papers as Python dicts with all metadata fields
- Generates standardized filenames (YYYY-Author-ShortTitle.md)
- Creates proper YAML frontmatter using `yaml_frontmatter_utils.py`
- Validates YAML before writing
- Skips existing papers (no overwrites)

**Use as template**: Copy and modify PAPERS list for new topics.

**Paper Definition Format**:
```python
{
    "year": 2024,
    "first_author": "Author Name",
    "short_title": "Paper Title",
    "authors": "Author1; Author2; Author3",
    "url": "https://source-url",
    "external_pdf": "https://pdf-url",  # optional
    "doi": "10.xxxx/xxxxx",  # optional
    "publication": "Journal or Conference",
    "type": "journalArticle",  # journalArticle, conferencePaper, preprint, report
    "abstract": "Full abstract text...",
    "ethics_overall": "Yes",
    "virtue_ethics": "Yes",  # or deontological_ethics, utilitarian_ethics
    "research_topic": "Category Name",
}
```

### Download Virtue Ethics PDFs (Template)

**Script**: `PYTHON/download_virtue_ethics_pdfs.py`

Downloads PDFs for a targeted list of papers with URL pattern conversion.

```bash
# Download PDFs for all defined papers
python3 PYTHON/download_virtue_ethics_pdfs.py
```

**Features**:
- URL pattern conversion (arXiv, ACL, OpenReview, DOI)
- Semantic Scholar API fallback (rate-limited)
- Updates paper metadata with local_pdf field
- Skips papers that already have local PDFs

**URL Conversion Patterns**:
```python
# arXiv
'arxiv.org/abs/XXXX' → 'arxiv.org/pdf/XXXX.pdf'

# ACL Anthology
'aclanthology.org/ID' → 'aclanthology.org/ID.pdf'

# OpenReview
'openreview.net/forum?id=X' → 'openreview.net/pdf?id=X'
```

**Semantic Scholar Rate Limits**:
- Hard limit at ~10-15 requests
- Returns HTTP 429 (Too Many Requests)
- Requires 4+ second delays between requests

### Update Virtue Ethics Metadata

**Script**: `PYTHON/update_virtue_ethics_metadata.py`

Updates paper profiles with local_pdf and pdf_extract paths after downloads.

```bash
python3 PYTHON/update_virtue_ethics_metadata.py
```

### Batch Import Workflow

```bash
# 1. Create papers (modify PAPERS list first)
python3 PYTHON/create_virtue_ethics_papers.py

# 2. Download PDFs
python3 PYTHON/download_virtue_ethics_pdfs.py

# 3. Manual curl for paywalled sources
curl -L -o "PDFs/YYYY-Author-Title.pdf" "https://arxiv.org/pdf/XXXX.pdf"

# 4. Extract text
PYTHONPATH="$PWD" python3 .agent/skills/extract_pdf_text/scripts/extract.py --verbose

# 5. Update metadata
python3 PYTHON/update_virtue_ethics_metadata.py
```

### PDF Source Success Rates (Learned from Session 16)

| Source | Pattern | Success Rate | Notes |
|--------|---------|--------------|-------|
| arXiv | `arxiv.org/abs/` → `/pdf/` | 95% | Best source, always try first |
| ACL Anthology | `aclanthology.org/ID` → `.pdf` | 90% | NLP/CL papers |
| OpenReview | `openreview.net/forum?` → `/pdf?` | 85% | ML conferences |
| Nature Scientific Reports | Direct `.pdf` append | 80% | Often OA |
| Springer OA | `link.springer.com/content/pdf/DOI.pdf` | 70% | Only for OA articles |
| PhilArchive | Direct PDF links | 85% | Philosophy papers |
| Semantic Scholar API | openAccessPdf field | 60% | Rate limited (4s delays) |
| SAGE Journals | Institutional access required | 20% | Usually paywalled |
| ScienceDirect | Institutional access required | 30% | Usually paywalled |
| Academia.edu | Login required | 10% | Rarely works |
| ResearchGate | Login required | 15% | Rarely works |

### Related Documentation

- [docs/WORKFLOWS.md](WORKFLOWS.md) - Batch import workflow
- [docs/SESSION_HISTORY.md](SESSION_HISTORY.md) - Session 16 details
