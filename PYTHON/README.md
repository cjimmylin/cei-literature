# Python Scripts Directory

This directory contains all utility scripts for the CEI Literature Vault. All scripts are Python 3 and should be run from the workspace directory (`CEI-Lit-WS/`) using `../.venv/bin/python PYTHON/<script_name>.py`.

## Configuration

All scripts use `vault_config.py` for centralized path configuration:

```python
from vault_config import PAPERS_DIR, PDFS_DIR, PDF_EXTRACTS_DIR, WORKSPACE_ROOT
```

PDF location is configured in `.vault-config.json`:
```json
{
  "pdf_path": "/path/to/your/PDFs",
  "zotero_path": "~/Zotero/storage"
}
```

## Quick Reference

### Classification Pipeline (Run in Order)
```bash
../.venv/bin/python PYTHON/classify_ethics.py
../.venv/bin/python PYTHON/classify_ethics_perspective.py
../.venv/bin/python PYTHON/classify_non_ethics_topics.py
../.venv/bin/python PYTHON/classify_cultural_religious.py
../.venv/bin/python PYTHON/classify_moral_psych.py
../.venv/bin/python PYTHON/generate_newtags.py
../.venv/bin/python PYTHON/classify_data_nature.py
```

### Report Generation
```bash
../.venv/bin/python PYTHON/generate_stats.py              # paper-statistics-1.md
../.venv/bin/python PYTHON/generate_report_v2.py          # paper-statistics-2.md
../.venv/bin/python PYTHON/generate_data_report.py        # data-nature-statistics.md
../.venv/bin/python PYTHON/generate_paper_statistics_3.py # paper-statistics-3.md
```

### Vault Management
```bash
../.venv/bin/python PYTHON/identify_targets.py     # Find papers needing work
../.venv/bin/python PYTHON/convert_csv_to_md.py    # Import from Zotero CSV
../.venv/bin/python PYTHON/rename_papers.py        # Standardize filenames
```

### Data Acquisition
```bash
../.venv/bin/python PYTHON/fetch_abstracts.py           # Fetch from arXiv
../.venv/bin/python PYTHON/check_publication_status.py  # Check via Semantic Scholar
../.venv/bin/python PYTHON/download_batch_8.py          # Download PDFs
```

## ⚠️ YAML Utilities Library

**All scripts that modify paper metadata MUST use `yaml_frontmatter_utils.py`**

### Purpose
Provides safe, validated functions for reading and writing YAML frontmatter. Prevents YAML corruption (orphaned list items, missing newlines, etc.).

### Key Functions
```python
from PYTHON.yaml_frontmatter_utils import (
    extract_frontmatter,        # Read YAML safely
    validate_frontmatter,       # Check for issues
    write_paper,                # Write with validation
    add_field,                  # Add/update a field
    add_tags,                   # Add tags as proper YAML list
)

# Safe read
frontmatter, body = extract_frontmatter(content)

# Validate before writing
is_valid, issues = validate_frontmatter(frontmatter)
if not is_valid:
    raise ValueError(f"YAML issues: {issues}")

# Safe write
write_paper(filepath, frontmatter, body, validate=True)
```

### Common Issues Fixed
- ✓ Orphaned list items (indented `-` without parent key)
- ✓ Missing newlines in YAML closing markers
- ✓ Hash prefixes in tags (`#TagName` → `TagName`)
- ✓ Incomplete key-value pairs
- ✓ Malformed closing markers

**See [YAML_SAFEGUARDS.md](../YAML_SAFEGUARDS.md) for complete documentation.**

## Script Categories

### Classification Scripts (7)

These scripts analyze papers and add metadata tags based on content analysis.

- **`classify_ethics.py`** - Base ethics classification
  - Detects virtue ethics, deontological, utilitarian frameworks
  - Sets `ethics_overall` (Yes/No)
  - Sets `virtue_ethics`, `deontological_ethics`, `utilitarian_ethics` (Yes/No)

- **`classify_ethics_perspective.py`** - Detailed ethics categorization
  - Applies ONLY to papers with `ethics_overall: "Yes"`
  - Categorizes into perspectives: "AI Safety & Alignment", "Bias & Fairness", "Toxicity & Hate Speech", etc.
  - Sets `ethics_perspective` field

- **`classify_non_ethics_topics.py`** - Research topic classification
  - Applies ONLY to papers with `ethics_overall: "No"`
  - Identifies topics: "Machine Learning", "NLP", "Computer Vision", "Benchmarks & Datasets", etc.
  - Sets `research_topic` field

- **`classify_cultural_religious.py`** - Cultural and religious value classification
  - Detects national/ethnic/cultural focus (Chinese, African/Ubuntu, American, etc.)
  - Detects religious focus (Islam, Christianity, Buddhism, Judaism, Hinduism, etc.)
  - Sets `national_ethnic_cultural` and `religious_values` fields

- **`classify_moral_psych.py`** - Moral psychology classification
  - Identifies moral psychology theories: Moral Foundations Theory, Dual Process Theory, etc.
  - Sets `moral_psychology` field

- **`classify_data_nature.py`** - Benchmark/Evaluation/Dataset classification
  - Detects whether paper is a benchmark (Yes/No/N/A/Unknown)
  - Detects whether paper is an evaluation (Yes/No/N/A/Unknown)
  - Detects whether paper is a dataset (Yes/No/N/A/Unknown)
  - Extracts quantitative metrics: question counts, language counts, dataset sizes, etc.
  - Sets `is_benchmark`, `is_eval`, `is_dataset`, `data_description`, `data_metrics`

- **`generate_newtags.py`** - Aggregate tag generation
  - Combines all classification results into unified `newtags` field
  - Generates hashtag format: #VirtueEthics, #Deontology, #Christianity, etc.
  - Supersedes `add_newtags.py`

### Report Generation Scripts (4)

These generate markdown reports summarizing paper classifications.

- **`generate_stats.py`** - Generates `paper-statistics-1.md`
  - Overall statistics and framework distributions
  - Lists papers by ethical framework

- **`generate_report_v2.py`** - Generates `paper-statistics-2.md`
  - Cultural and religious value statistics
  - Moral psychology theory distributions
  - Detailed categorization reports

- **`generate_data_report.py`** - Generates `data-nature-statistics.md`
  - 1,604-line detailed report on benchmarks, evaluations, datasets
  - Includes quantitative metrics and descriptions

- **`generate_paper_statistics_3.py`** - Generates `paper-statistics-3.md`
  - 3,391-line comprehensive report
  - Multi-category breakdowns
  - All papers with extracted metrics

### Data Import & Maintenance (5)

Scripts for importing new papers and maintaining metadata.

- **`convert_csv_to_md.py`** - Import from Zotero CSV
  - Reads Zotero export (Base.md)
  - Creates individual `.md` files in `papers/` directory
  - Generates YAML frontmatter with metadata
  - Output: One file per paper with structure and frontmatter

- **`rename_papers.py`** - Standardize filenames
  - Renames papers to format: `YYYY-Author-ShortTitle.md`
  - Handles missing years gracefully
  - Updates internal links if needed

- **`regenerate_papers.py`** - Regenerate paper files
  - Rebuilds paper markdown files from metadata
  - Useful after bulk metadata updates

- **`update_urls.py`** - Update URLs in metadata
  - Updates DOI, arXiv, and other URL fields
  - Normalizes URL formats
  - Adds missing URLs where discoverable

- **`resolve_unknowns.py`** - Fix unknown authors/years
  - Hardcoded mappings for previously problematic papers
  - Cross-references with arXiv, DOI, URLs
  - Renames files after fixing metadata

### Author Management (4)

Scripts for managing the Authors/ directory.

- **`populate_authors.py`** - Populate Authors/ from paper metadata
  - Creates author files from all papers
  - Generates initial wikilinks to papers
  - Initializes author directory structure

- **`update_authors.py`** - Update author metadata
  - Creates/updates author files in `Authors/` directory
  - Adds affiliations and research interests
  - Generates wikilinks to papers

- **`ensure_authors_from_base.py`** - Ensure all authors in Base.md
  - Checks that all papers have proper author entries
  - Creates missing author files
  - Validates author names

- **`enrich_acl_papers.py`** - Enrich ACL papers with venue info
  - Adds ACL-specific metadata
  - Updates publication venues
  - Corrects years for papers published in ACL

### PDF & Text Processing (2+)

Scripts for working with PDF files.

- **`process_pdfs.py`** - Extract text from PDFs
  - Uses PyMuPDF (fitz) for text extraction
  - Outputs to `PDF Extracts/` directory (legacy - see agent skills for current)
  - Preserves page markers for reference
  - Handles large documents (40k-180k characters)

- **`prepare_analyses.py`** - Prepare extracted text for analysis
  - Combines extracted PDF text with metadata
  - Creates JSON objects with text + paper info
  - Organizes for content analysis pipeline

**Note (Jan 2026):** PDF text extraction has been migrated to Agent Skills format:
- **Location:** `.agent/skills/extract_pdf_text/scripts/extract.py`
- **Output Format:** Markdown (.md) files in `PDF Extracts/YYYY-Author-Title.md` (not plain text)
- **Migration Tool:** `.agent/skills/extract_pdf_text/scripts/migrate_txt_to_md.py` (converts legacy .txt to .md)
- **Benefits:** Full Obsidian integration, searchable, metadata support, proper frontmatter
- See [PDF_EXTRACTION_UPGRADE.md](../docs/PDF_EXTRACTION_UPGRADE.md) and [MIGRATION_GUIDE.md](../.agent/skills/extract_pdf_text/MIGRATION_GUIDE.md)

### Preprint & Abstract Management (4)

Scripts for fetching external data.

- **`fetch_abstracts.py`** - Fetch abstracts from arXiv
  - Queries arXiv API for abstracts
  - Updates `abstract` field in paper metadata
  - Rate-limited: 0.3 second delays
  - Handles arXiv ID parsing from URLs

- **`fetch_remaining_abstracts.py`** - Fallback for missing abstracts
  - Second-pass attempt to fetch abstracts
  - Uses title-based searching
  - Handles edge cases and errors

- **`check_publication_status.py`** - Check preprint publication
  - Queries Semantic Scholar API
  - Updates paper type from "preprint" to "conferencePaper"
  - Adds publication venue and corrects year
  - Renames files if year changed
  - Rate-limited: 4 second delays per request

- **`update_published_preprints.py`** - Update published preprint info
  - Variant of publication status checker
  - Focuses on already-identified preprints
  - Updates metadata when publication is confirmed

### Utility Scripts (3)

Miscellaneous utility scripts.

- **`download_batch_8.py`** - Download PDFs in batch
  - Downloads papers from URLs
  - Places PDFs in `Lit-WS-PDFs/` directory
  - Updates metadata links
  - Batch processing of multiple papers

- **`add_newtags.py`** - Legacy tag generation
  - **Deprecated**: Use `generate_newtags.py` instead
  - Kept for compatibility
  - Generates `newtags` field from classifications

- **`identify_targets.py`** - Find papers needing work
  - Lists papers missing PDFs, abstracts, summaries
  - Identifies ethics papers needing enrichment
  - Supports filtering by type
  - Output: Markdown list with paper names

## Dependencies

All scripts require Python 3.9+

### Core Dependencies
```bash
pip install pymupdf requests
```

### Optional Dependencies
- For arXiv API: Built into `requests`
- For Semantic Scholar API: Built into `requests`
- No external package needed for PyMuPDF

### Virtual Environment (if using .venv)
```bash
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate     # On Windows
```

## Common Workflows

### Adding New Papers
```bash
# 1. Export from Zotero to Base.md
# 2. Import to vault
../.venv/bin/python PYTHON/convert_csv_to_md.py

# 3. Standardize filenames
../.venv/bin/python PYTHON/rename_papers.py

# 4. Run full classification
../.venv/bin/python PYTHON/classify_ethics.py
../.venv/bin/python PYTHON/classify_ethics_perspective.py
../.venv/bin/python PYTHON/classify_non_ethics_topics.py
../.venv/bin/python PYTHON/classify_cultural_religious.py
../.venv/bin/python PYTHON/classify_moral_psych.py
../.venv/bin/python PYTHON/classify_data_nature.py
../.venv/bin/python PYTHON/generate_newtags.py

# 5. Fetch missing abstracts
../.venv/bin/python PYTHON/fetch_abstracts.py

# 6. Generate reports
../.venv/bin/python PYTHON/generate_stats.py
../.venv/bin/python PYTHON/generate_report_v2.py
../.venv/bin/python PYTHON/generate_data_report.py
../.venv/bin/python PYTHON/generate_paper_statistics_3.py
```

### Processing PDFs
```bash
# 1. Place PDFs in Lit-WS-PDFs/ directory
# 2. Extract text
python3 .agent/skills/extract_pdf_text/scripts/extract.py

# 3. Generate summaries (manual process)
# See .agent/workflows/summarize_papers.md
```

### Weekly Maintenance
```bash
# Check vault status
python3 .agent/skills/vault_management/scripts/stats.py

# Update publication status for preprints
../.venv/bin/python PYTHON/check_publication_status.py

# Fetch missing abstracts
../.venv/bin/python PYTHON/fetch_abstracts.py

# Regenerate reports
../.venv/bin/python PYTHON/generate_stats.py
../.venv/bin/python PYTHON/generate_report_v2.py
../.venv/bin/python PYTHON/generate_data_report.py
../.venv/bin/python PYTHON/generate_paper_statistics_3.py

# Identify work items
python3 .agent/skills/vault_management/scripts/identify.py
```

## Running Scripts

Always run scripts from the `CEI-Lit-WS/` workspace directory:

```bash
# Correct (from CEI-Lit-WS/)
../.venv/bin/python PYTHON/classify_ethics.py

# Incorrect
cd PYTHON && python3 classify_ethics.py
```

Scripts use `vault_config.py` to locate:
- `papers/` directory (in workspace)
- `Lit-WS-PDFs/` directory (external, from `.vault-config.json`)
- `PDF Extracts/` directory (in workspace)
- `Authors/` and `AI Labs/` directories (in workspace)

## Error Handling

If a script fails:
1. Check the error message for missing imports
2. Ensure Python 3.9+ is installed
3. Verify all paper files are in `papers/` directory
4. Check that `Base.md` exists
5. For API calls, check rate limiting (arXiv: 0.3s, Semantic Scholar: 4s)

## Rate Limiting

- **arXiv API** (`fetch_abstracts.py`): 0.3 second delay between requests
- **Semantic Scholar API** (`check_publication_status.py`): 4 second delay between requests
- These delays prevent API blocking and are built into the scripts

## Testing

For testing or preview mode:
- `classify_ethics.py`, etc. have `--dry-run` flags
- Reports can be generated to test what changes would be made
- Use `identify_targets.py` to preview papers that would be affected

---

Last updated: February 2026
See `LLM_CONTEXT.md` Section 14 for full documentation.
