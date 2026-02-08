# GEMINI.md

This file provides guidance to Google Gemini models when working with code in this repository.

## Overview

This is an Obsidian vault containing a literature database for CEI research. The primary data file is `Base.md`, which is a CSV export from Zotero containing academic references. The enriched data lives in the `papers/` directory as Markdown files with YAML frontmatter. Author information is consolidated in the `Authors/` directory. Lab-specific information is maintained in the `AI Labs/` directory.

## Source of Truth

**`LLM_CONTEXT.md`** is the primary source of truth for all classification logic, script execution orders, authorship structures, and system learnings. **ALWAYS** refer to `LLM_CONTEXT.md` before making changes to the classification pipeline or CRM structure.

## Classification Pipeline

The following scripts enrich metadata. Execute them in this order:

1. `classify_ethics.py` - Base ethics classification (Yes/No, Frameworks)
2. `classify_ethics_perspective.py` - Refines "Ethics Yes" papers
3. `classify_non_ethics_topics.py` - Refines "Ethics No" papers
4. `classify_cultural_religious.py` - Cultural/Religious values
5. `classify_moral_psych.py` - Moral Psychology
6. `generate_newtags.py` - Aggregates tags
7. `classify_data_nature.py` - Identifies Benchmarks/Evals/Datasets

## Reporting

- `generate_stats.py` -> `20260119-paper-statistics-1.md`
- `generate_report_v2.py` -> `20260119-paper-statistics-2.md`
- `generate_data_report.py` -> `20260119-data-nature-statistics.md`
- `generate_paper_statistics_3.py` -> `20260119-paper-statistics-3.md`

## Authors CRM

- **Location**: `Authors/`
- **Purpose**: Centralized researcher database.
- **Key Files**: `Authors/README.md`, `Authors/TEMPLATE.md`.
- **Relationship**: Linked to `papers/` via wikilinks.

## AI Labs Repository

- **Location**: `AI Labs/`
- **Purpose**: Centralized database for AI labs and their models.
- **Key Files**: `AI Labs/README.md`, `AI Labs/TEMPLATE.md`.
- **Relationship**: Links to models and papers via wikilinks.

## Agent Skills (Google Antigravity)

- **Location**: `.agent/skills/`
- **Consolidate Memory**: (`consolidate_memory/SKILL.md`) Protocol for ending sessions and updating documentation.
- **Enrich Authors**: (`.agent/workflows/enrich_author_profile.md`) Workflow for Author CRM.
- **Download PDFs**: (`.agent/skills/download_pdf/SKILL.md`) Automated downloading of papers from ArXiv/ACL.
- **Extract PDF Text**: (`.agent/skills/extract_pdf_text/SKILL.md`) Extract text from PDFs for analysis.
- **Summarize Paper**: (`.agent/skills/summarize_paper/SKILL.md`) Generate structured summaries from extracted text.

## Metadata Fields

Enriched fields include:
- **Ethics:** `ethics_overall`, `virtue_ethics`, `deontological_ethics`, `utilitarian_ethics`
- **Descriptions:** `key_contribution`, `significance`
- **Topics:** `ethics_perspective`, `research_topic`
- **Values:** `national_ethnic_cultural`, `religious_values`, `moral_psychology`
- **Data Nature:** `is_benchmark`, `is_eval`, `is_dataset`, `data_description`, `data_metrics`
- **Tags:** `newtags`

## Critical Learnings

1. **File Naming (Papers):** All files must follow `YYYY-FirstAuthorLettersOnly-ShortTitle.md` format.
2. **File Naming (Authors):** All files must follow `FullName.md` format (e.g., `Ruben E. Laukkonen.md`).
3. **Links:** Use Obsidian Wikilinks `[[Filename|Title]]`. Do NOT use standard markdown links with `%20`.
4. **Missing Metadata:** If `year` or `author` is missing, verify online (ArXiv/Semantic Scholar) and update before processing stats.
5. **Author Enrichment:** Focus on full names. Consolidate name variants (e.g., `Name M. LastName` vs `Name LastName`) into a single profile.
6. **Maintenance:** Use `check_publication_status.py` to check for published versions of preprints.
7. **PDF Verification:** When downloading PDFs (especially via ArXiv ID), verify that the downloaded content matches the expected paper title. Mismatches can occur if IDs are transposed or if metadata is outdated.
8. **Malformatted YAML:** Automated tools must ensure YAML frontmatter is properly formatted (e.g., ensuring a newline before the closing `---`). Malformed YAML breaks Obsidian parsing.
9. **Script Location (PYTHON/):** Scripts have been moved to the `PYTHON/` directory. When running them or writing new ones, ensure relative paths (like `papers_dir`) are updated to handle the subdirectory location (e.g., `Path(__file__).parent.parent / 'papers'`).
10. **PDF Text Extraction (Jan 2026):** Always save extracts as **Markdown files (.md)** not plain text (.txt). Plain text files are invisible in Obsidian's file explorer and defeat full-text search. Extract files are saved to `PDF Extracts/YYYY-Author-Title.md` with YAML frontmatter containing metadata (source PDF, page count, extraction timestamp). See [PDF_EXTRACTION_UPGRADE.md](PDF_EXTRACTION_UPGRADE.md) and [MIGRATION_GUIDE.md](../.agent/skills/extract_pdf_text/MIGRATION_GUIDE.md).
