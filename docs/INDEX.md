# Documentation Index

Quick reference to all vault documentation.

## Quick Start
- [CLAUDE.md](../CLAUDE.md) - Main instructions for Claude Code (read this first!)
- [README.md](../README.md) - Project overview and vault structure
- [WORKFLOWS.md](WORKFLOWS.md) - Common workflows and how-to guides
- `.vault-config.json` - PDF path configuration (see `.vault-config.json.example`)

## Directory Structure (Feb 2026)
- **Workspace:** `CEI-Lit-WS/` - Main GitHub-tracked workspace
- **PDFs:** External location configured via `.vault-config.json`
- **Library:** `.agent/lib/` - Centralized utility modules (Phase 5-6)
- **Operating System:** `_OPERATING-SYSTEM/` - 4-layer memory architecture (LifeOS)
  - `Standards/` - 8 procedural knowledge standards
  - `Learnings/` - Session-to-session knowledge
  - `Maintenance/` - Automated health reports

## Core Documentation

### For Researchers
- [LLM_CONTEXT.md](../LLM_CONTEXT.md) - Classification logic and metadata details
- [YAML_SAFEGUARDS.md](../YAML_SAFEGUARDS.md) - YAML frontmatter rules and safety

### For Developers
- [SCRIPTS.md](SCRIPTS.md) - Reference for all Python scripts
- [COMMANDS.md](COMMANDS.md) - Slash commands and skills
- [QC_SYSTEM.md](QC_SYSTEM.md) - Code quality checking system

### LifeOS Architecture (NEW - Phase 1-8)
- [_OPERATING-SYSTEM/README.md](../_OPERATING-SYSTEM/README.md) - 4-layer memory system overview
- [_OPERATING-SYSTEM/Standards/](../_OPERATING-SYSTEM/Standards/) - 8 procedural knowledge standards
- [OPERATING_SYSTEM_MIGRATION.md](OPERATING_SYSTEM_MIGRATION.md) - Complete migration guide
- `.agent/lib/` - Centralized library with 72% test coverage
- `.claude/skills/quarterly-maintenance/` - Automated health checks

## Session History & Reports

### Recent Sessions (2026)
- [SESSION_HISTORY.md](SESSION_HISTORY.md) - Historical log of all sessions
- **Session 18 (Jan 25)**: AI Labs PDF Extraction & Organization
  - [SESSION_2026_01_25_AI_LABS_EXTRACTS.md](SESSION_2026_01_25_AI_LABS_EXTRACTS.md) - Detailed report
  - Extracted 111 PDFs, created 14 lab overviews, reorganized extracts to model folders
- **Session 15 (Jan 25)**: AI Labs Paper Download
  - Downloaded 140 PDFs (~880 MB) for 14 AI labs (OpenAI, Anthropic, DeepMind, etc.)
- **Session 14 (Jan 25)**: Virtue Ethics Paper Discovery
  - [SESSION_2026-01-25_Virtue_Ethics_Papers.md](SESSION_2026-01-25_Virtue_Ethics_Papers.md) - Detailed report
  - Added 28+ papers on virtue ethics for AI alignment (Confucian, Aristotelian, narrative)
- **Session 13 (Jan 25)**: Deontological/Kantian Ethics Paper Discovery
  - [SESSION_2026-01-25_Deontological_Ethics_Papers.md](SESSION_2026-01-25_Deontological_Ethics_Papers.md) - Detailed report
  - Added 14 papers on deontological ethics for AI alignment
- **Session 12 (Jan 25)**: Consequentialist Ethics Paper Discovery
  - [RESEARCH_PAPER_DISCOVERY_LEARNINGS.md](RESEARCH_PAPER_DISCOVERY_LEARNINGS.md) - Workflow learnings
  - Added 11 papers on utilitarian/consequentialist ethics for AI alignment
- **Session 11 (Jan 25)**: First Author Enrichment
  - [SESSION_2026_01_25_AUTHOR_ENRICHMENT.md](SESSION_2026_01_25_AUTHOR_ENRICHMENT.md) - Detailed report
  - [PARALLEL_AGENT_BEST_PRACTICES.md](PARALLEL_AGENT_BEST_PRACTICES.md) - Reusable methodology
- **Session 10 (Jan 24)**: PDF Recovery
  - Recovered 474 PDFs via multi-source downloads

### Completion Reports
- [20260125-AUTHOR_ENRICHMENT_REPORT.md](../logs/20260125-AUTHOR_ENRICHMENT_REPORT.md) - 408 authors enriched
- [20260125-METADATA_CORRECTIONS_2026_01_25.md](../logs/20260125-METADATA_CORRECTIONS_2026_01_25.md) - Papers fixed
- [20260125-SESSION_2026_01_25_SUMMARY.md](../logs/20260125-SESSION_2026_01_25_SUMMARY.md) - Session summary

## Specialized Guides

### Author Management
- [AUTHOR_DATA_MANAGEMENT.md](AUTHOR_DATA_MANAGEMENT.md) - Author name fixes
- [PARALLEL_AGENT_BEST_PRACTICES.md](PARALLEL_AGENT_BEST_PRACTICES.md) - Mass enrichment guide
- [Authors/TEMPLATE.md](../Authors/TEMPLATE.md) - Author profile template

### PDF Management
- [PDF_RECOVERY_GUIDE.md](PDF_RECOVERY_GUIDE.md) - Recovering deleted/missing PDFs
- [PDF_DOWNLOAD_SOURCES.md](PDF_DOWNLOAD_SOURCES.md) - PDF source reference (success rates, URL patterns)
- [MISSING_PDFS.md](MISSING_PDFS.md) - **43 papers missing PDFs** (tracking document for future recovery)
- **Extraction**: Use `/extract-pdf-text` or `PYTHON/extract_pdf_text.py`
- **Summarization**: Use `/summarize-paper` or `/summarize-all-papers`

### AI Labs Management
- [SESSION_2026_01_25_AI_LABS_EXTRACTS.md](SESSION_2026_01_25_AI_LABS_EXTRACTS.md) - Extraction session notes
- [SCRIPTS.md](SCRIPTS.md#ai-labs-management) - AI Labs scripts reference
- **Download papers**: Use `/download-lab-papers` skill
- **Extract PDFs**: `python3 PYTHON/extract_ai_labs_pdfs.py`
- **Move extracts**: `python3 PYTHON/move_ai_lab_extracts.py`
- **Generate overviews**: Ask Claude to create overview.md for each lab

### Data Quality
- [KNOWN_ISSUES.md](KNOWN_ISSUES.md) - Known issues and prevention
- [ENRICHMENT_REPORT.md](ENRICHMENT_REPORT.md) - Ethics paper enrichment details
- **Validation**: `python3 PYTHON/validate_all_papers.py`

## Archive & Historical Context
- [CONTEXT_OPTIMIZATION.md](CONTEXT_OPTIMIZATION.md) - Documentation strategy
- [SESSION_HANDOVER.md](SESSION_HANDOVER.md) - Previous handover notes
- [GEMINI.md](GEMINI.md) - Google Antigravity instructions

## Latest Updates (Jan 2026)

| Date | Update | Documentation |
|------|--------|---------------|
| Jan 25 | **Session 17**: 12 deontological/deontic logic papers | SESSION_HISTORY.md #Session17 |
| Jan 25 | **Session 16**: 24 virtue ethics papers (batch import) | SESSION_HISTORY.md #Session16 |
| Jan 25 | PDF download sources reference created | PDF_DOWNLOAD_SOURCES.md |
| Jan 25 | Batch paper import workflow documented | WORKFLOWS.md, SCRIPTS.md |
| Jan 25 | AI Labs: 111 PDFs extracted, 14 overviews created | SESSION_2026_01_25_AI_LABS_EXTRACTS.md |
| Jan 25 | AI Labs: 140 papers downloaded (~880 MB) | SESSION_HISTORY.md #Session15 |
| Jan 25 | 28+ virtue ethics papers added | SESSION_2026-01-25_Virtue_Ethics_Papers.md |
| Jan 25 | 14 deontological ethics papers added | SESSION_2026-01-25_Deontological_Ethics_Papers.md |
| Jan 25 | 11 consequentialist ethics papers added | RESEARCH_PAPER_DISCOVERY_LEARNINGS.md |
| Jan 25 | 408 first authors enriched (99%) | SESSION_2026_01_25_* |
| Jan 24 | 474 PDFs recovered (82.3%) | SESSION_HISTORY.md #Session10 |

## Vault Statistics (Current)

- **Papers**: 672 (100% YAML valid)
- **PDFs**: 547/672 (81.4%)
- **PDF Extracts**: 546 searchable .md files
- **Authors**: 2,894 total, 408 first authors enriched
- **Classification**: All papers classified with metadata
- **Normative Ethics Coverage**:
  - Virtue ethics: ~55+ papers (including phronesis, Aristotelian)
  - Deontological ethics: ~125+ papers (including deontic logic, Kantian)
  - Utilitarian ethics: ~110+ papers

## How to Find Things

### Looking for...
- **How to do X**: Check [WORKFLOWS.md](WORKFLOWS.md)
- **What does script Y do**: Check [SCRIPTS.md](SCRIPTS.md)
- **Slash command reference**: Check [COMMANDS.md](COMMANDS.md)
- **Past session details**: Check [SESSION_HISTORY.md](SESSION_HISTORY.md)
- **Best practices**: Check relevant guide (see below)

### Best Practices by Topic
- **Paper discovery**: RESEARCH_PAPER_DISCOVERY_LEARNINGS.md
- **Author enrichment**: PARALLEL_AGENT_BEST_PRACTICES.md
- **PDF recovery**: PDF_RECOVERY_GUIDE.md
- **YAML editing**: YAML_SAFEGUARDS.md
- **Code quality**: QC_SYSTEM.md
- **Author names**: AUTHOR_DATA_MANAGEMENT.md

## Quick Commands

```bash
# Health check
python3 PYTHON/validate_all_papers.py

# Generate reports
/generate-reports all

# Check vault stats
/vault-stats

# Extract PDF text
/extract-pdf-text

# Enrich paper
/enrich-paper <name>

# Code quality check
/qc-code
```

---

*This index is maintained to help navigate the comprehensive documentation. For project instructions, start with [CLAUDE.md](../CLAUDE.md).*
