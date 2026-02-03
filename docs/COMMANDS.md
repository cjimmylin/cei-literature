# Slash Commands & Skills Reference

## Slash Commands (`.claude/commands/`)

### PDF & Summarization

| Command | Description |
|---------|-------------|
| `/extract-pdf-text` | Extract text from PDFs, update metadata, **auto-generate summaries** |
| `/summarize-paper <name>` | Generate structured summary for a single paper |
| `/summarize-all-papers` | Batch process all papers needing summaries |
| `/list-papers [filter]` | Show paper status (filter: `missing-extract`, `missing-summary`, `complete`) |

### Research & Acquisition

| Command | Description |
|---------|-------------|
| `/research-paper <query>` | Search for papers by title, author, topic, or DOI |
| `/download-pdf <name or URL>` | **Full pipeline**: download PDF → extract text → generate summaries (automatic) |
| `/download-lab-papers <lab>` | Download all papers/docs for an AI lab's models |
| `/fetch-abstracts [name or all]` | Fetch missing abstracts from arXiv/Semantic Scholar |
| `/check-publication [name or all]` | Check if preprints have been published |

### Classification & Metadata

| Command | Description |
|---------|-------------|
| `/classify-papers [stage]` | Run classification pipeline (all, ethics, cultural, data, etc.) |
| `/generate-reports [type]` | Generate statistics reports (all, stats, cultural, data) |
| `/enrich-paper <name>` | Add key_contribution/significance to ethics papers |

### Vault Management

| Command | Description |
|---------|-------------|
| `/vault-stats` | Quick overview of vault statistics |
| `/identify-targets [type]` | Find papers needing attention (enrichment, abstracts, pdfs) |
| `/import-papers` | Import papers from Zotero CSV export |
| `/check-duplicates` | **Run after import** - Detect and handle duplicate papers |
| `/rename-papers` | Standardize filenames to YYYY-Author-Title convention |
| `/complete-learning` | Consolidate and document session learnings in core docs |
| `/audit-papers [--fix]` | Comprehensive audit of all papers for data quality issues |

### Quality Assurance

| Command | Description |
|---------|-------------|
| `/qc-code [--verbose]` | Run automated code quality checks on scripts and skills |

### Author Management

| Command | Description |
|---------|-------------|
| `/fix-authors` | Fix incomplete author names using arXiv API and manual mappings |

## Skills (`.claude/skills/`)

Skills are detailed instructions Claude follows for specific tasks.

### Author Management
- `fix-authors.md` - Fix incomplete author names using arXiv API, CSV data, and manual mappings

### PDF Processing
- `extract-pdf-text.md` - PDF text extraction + auto-summarization (saves `.md` to `PDF Extracts/`, generates summary sections)
- `summarize-paper.md` - Individual paper summarization (regenerate if needed)
- `batch-summarize.md` - Batch summarization workflow
- `list-papers.md` - Paper status reporting (shows extract status)

### Research & Acquisition
- `research-paper.md` - Search for papers across academic databases
- `download-pdf.md` - **Full pipeline**: download PDF → extract text → generate summaries (all automatic)
- `download-lab-papers.md` - Download all papers/docs for an AI lab (OpenAI, DeepMind, etc.)
- `fetch-abstract.md` - Fetch abstracts from arXiv/Semantic Scholar
- `check-publication-status.md` - Check preprint publication status
- `complete-learning.md` - Consolidate session learnings

### Classification & Metadata
- `classify-papers.md` - Run the 7-stage classification pipeline
- `generate-reports.md` - Generate all 4 statistics reports
- `enrich-ethics-paper.md` - Add key_contribution/significance fields

### Vault Management
- `vault-stats.md` - Generate quick vault statistics overview
- `identify-targets.md` - Find papers needing various types of attention
- `import-papers.md` - Import from Zotero CSV export
- `check-duplicates.md` - **Run after import** - Detect duplicate papers by DOI/title matching
- `rename-papers.md` - Standardize paper filenames
- `audit-papers.md` - Comprehensive paper audit and cleanup workflow

### Quality Assurance
- `qc-code.md` - Automated code quality checks for Python scripts and skills

## Supported Academic Databases

The research and fetching skills support:
- **arXiv** - Preprints (API for abstracts)
- **Semantic Scholar** - Publication status, citation data, open access PDFs
- **ACL Anthology** - NLP/CL papers
- **OpenReview** - Conference submissions with reviews
- **DBLP** - Computer science bibliography
- **DOI resolution** - Universal paper lookup
