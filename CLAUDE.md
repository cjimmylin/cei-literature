# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## ⛔ CRITICAL: NO FILE DELETIONS

**NEVER use `rm`, `unlink`, or any delete command. EVER.**

To remove files, ALWAYS move them to `RECYCLE-BIN/`:
```bash
mv unwanted-file.pdf RECYCLE-BIN/
mv unwanted-directory/ RECYCLE-BIN/
```

This rule exists because accidental deletion destroyed 422 PDF files. **NO EXCEPTIONS.**

---

## Quick Reference

| Item | Value |
|------|-------|
| **Type** | Obsidian vault - CEI research literature database |
| **Papers** | 657 in `papers/` (100% YAML valid) |
| **PDFs** | External location (configured in `.vault-config.json`) |
| **Extracts** | 662 searchable `.md` files in `PDF Extracts/` |
| **Authors** | 2,946 profiles, 408 first authors enriched (99%) |
| **AI Labs** | 14 labs, 350+ papers, 500+ files, 100% coverage - [Master Report](AI%20Labs/MASTER_COMPLETION_REPORT.md) |
| **Zotero** | `~/Zotero/storage` as read-only reference (3,500+ PDFs) |
| **Python** | `../.venv/` with PyMuPDF - run: `../.venv/bin/python PYTHON/script.py` |
| **Status** | Production-ready, actively maintained |

**Recent Updates (Feb 2, 2026)**: New directory structure - PDFs now stored externally (configured via `.vault-config.json`). Main workspace is `CEI-Lit-WS/` (GitHub tracked). See `.vault-config.json.example` for setup.

## Essential Rules

### 1. YAML Safety (CRITICAL)
**Always use `PYTHON/yaml_frontmatter_utils.py`** for any YAML modifications:
```python
from PYTHON.yaml_frontmatter_utils import write_paper, validate_frontmatter
is_valid, issues = validate_frontmatter(frontmatter)
if not is_valid: raise ValueError(f"YAML invalid: {issues}")
write_paper(filepath, frontmatter, body, validate=True)
```
- Never use regex/string manipulation on frontmatter
- Never create orphaned list items (lists need parent keys)
- `newtags` is a string, not a YAML list

### 2. Data Source
- `Base Source from Zotero.md` = Zotero CSV export (read-only, managed externally)
- Papers in `papers/` have enriched YAML frontmatter

### 3. Validation Check
```bash
../.venv/bin/python PYTHON/validate_all_papers.py       # Basic YAML
../.venv/bin/python PYTHON/validate_papers_enhanced.py  # Extended checks
../.venv/bin/python PYTHON/detect_content_mismatches.py # Content validation
```

### 4. No Deletions (See top of file)
Rule documented above. **Use `mv` to RECYCLE-BIN/, NEVER `rm`.**

## Directory Structure

```
CEI-Lit-WS/                    # This workspace (GitHub tracked)
├── .vault-config.json         # External path configuration (gitignored)
├── papers/                    # 657 paper metadata files (YAML + body)
├── PDF Extracts/              # 662 searchable markdown extracts
├── Authors/                   # 2,946 author profiles
├── AI Labs/                   # 14 AI labs: 350+ papers, 500+ files
├── PYTHON/                    # Classification & utility scripts
│   └── vault_config.py        # Centralized path configuration
├── STATISTICS/                # Generated reports
├── docs/                      # All documentation
├── logs/                      # Log files and JSON reports
└── RECYCLE-BIN/               # Deleted files go here (NEVER use rm)

External (configured via .vault-config.json):
└── /path/to/PDFs/             # 652 PDF files (user-configured)
```

## Setup (New Clone)

1. Copy `.vault-config.json.example` to `.vault-config.json`
2. Edit `pdf_path` to point to your PDFs location
3. Verify: `../.venv/bin/python -c "from PYTHON.vault_config import PDFS_DIR; print(PDFS_DIR)"`

## Progressive Documentation

Read these **only when needed** for specific tasks:

| Task | Read |
|------|------|
| **All documentation** | [docs/INDEX.md](docs/INDEX.md) - Complete index |
| PDF recovery & download | [docs/PDF_RECOVERY_GUIDE.md](docs/PDF_RECOVERY_GUIDE.md) |
| Author enrichment (parallel agents) | [docs/PARALLEL_AGENT_BEST_PRACTICES.md](docs/PARALLEL_AGENT_BEST_PRACTICES.md) |
| Running classification/scripts | [docs/SCRIPTS.md](docs/SCRIPTS.md) |
| Common workflows (import, enrich, etc.) | [docs/WORKFLOWS.md](docs/WORKFLOWS.md) |
| Slash commands & skills reference | [docs/COMMANDS.md](docs/COMMANDS.md) |
| YAML issues or writing scripts | [YAML_SAFEGUARDS.md](YAML_SAFEGUARDS.md) |
| Code quality checks & standards | [docs/QC_SYSTEM.md](docs/QC_SYSTEM.md) |
| Known issues & prevention | [docs/KNOWN_ISSUES.md](docs/KNOWN_ISSUES.md) |
| Classification logic details | [LLM_CONTEXT.md](LLM_CONTEXT.md) |
| Session history & past fixes | [docs/SESSION_HISTORY.md](docs/SESSION_HISTORY.md) |
| Maintaining this doc structure | [docs/CONTEXT_OPTIMIZATION.md](docs/CONTEXT_OPTIMIZATION.md) |
| AI Labs (all labs complete) | [AI Labs/MASTER_COMPLETION_REPORT.md](AI%20Labs/MASTER_COMPLETION_REPORT.md) - 14 labs, 350+ papers |
| AI Labs session summary | [AI Labs/SESSION_SUMMARY_2026-01-31.md](AI%20Labs/SESSION_SUMMARY_2026-01-31.md) - Learnings & patterns |

## Key Metadata Fields

Papers have these enriched fields (beyond Zotero data):
- `ethics_overall`, `ethics_perspective`, `research_topic`
- `national_ethnic_cultural`, `religious_values`, `moral_psychology`
- `is_benchmark`, `is_eval`, `is_dataset`, `data_description`
- `pdf_extract` (path to searchable extract)
- `newtags` (aggregated classification tags)

## Slash Commands (Quick List)

| Category | Commands |
|----------|----------|
| **PDF** | `/download-pdf` (auto: download→extract→summarize), `/extract-pdf-text`, `/summarize-paper` |
| **Research** | `/research-paper`, `/fetch-abstracts`, `/list-papers` |
| **Classification** | `/classify-papers`, `/generate-reports`, `/enrich-paper` |
| **Vault** | `/vault-stats`, `/identify-targets`, `/import-papers` |
| **Authors** | `/fix-authors` |
| **QA** | `/qc-code`, `/audit-papers` |

See [docs/COMMANDS.md](docs/COMMANDS.md) for full details.

## Maintenance Rules

**Keep this file under 100 lines.** New docs → `docs/`, scripts → `PYTHON/`, logs → `logs/`. See [docs/CONTEXT_OPTIMIZATION.md](docs/CONTEXT_OPTIMIZATION.md).
