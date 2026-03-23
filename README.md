# CEI Literature Vault

A curated collection of academic papers and research literature for the **Center of Ethical Intelligence (CEI)**, focused on **Values Alignment for AI**.

## Purpose

This repository serves as a centralized knowledge base for AI ethics and safety research, supporting CEI's mission to advance values-aligned artificial intelligence. The literature covers critical topics including:

- **AI Safety & Alignment** — Research on ensuring AI systems behave according to human values
- **Bias & Fairness in ML** — Detection and mitigation of bias in language models and AI systems
- **Hate Speech Detection** — Benchmarks and methods for identifying harmful content
- **LLM Evaluation** — Frameworks for assessing hallucination, reliability, and ethical behavior
- **Responsible AI Development** — Best practices for building trustworthy AI systems
## Project Status (Feb 2, 2026)

- **Papers**: 657 in `papers/` (100% YAML valid)
- **PDFs**: 652/657 (99.2%) - stored externally (configured via `.vault-config.json`)
- **PDF Extracts**: 662 searchable Markdown files in `PDF Extracts/`
- **Author Profiles**: 2,946 profiles, 408 first authors enriched (99%)
- **AI Labs**: 14 labs documented (OpenAI, Anthropic, DeepMind, Meta, Mistral, Qwen, DeepSeek, 01.AI, Zhipu, Baidu, Tencent, xAI, NVIDIA, Microsoft)
- **AI Labs Papers**: 350+ research papers, 70+ model cards, 500+ files (100% coverage)
- **Metadata Enrichment**: ~150 ethics papers enriched with `key_contribution` and `significance`
- **Data Nature**: All papers classified as Benchmarks, Evaluations, or Datasets with metrics
- **YAML Validation**: 657/657 papers validated (100%)

## AI-Assisted Research Environment

This vault is configured for use with multiple AI coding assistants:

| Tool | Model(s) | Purpose |
|------|----------|---------|
| **Claude Code** | Claude (Anthropic) | Code analysis, literature exploration, and research assistance |
| **Antigravity** | Gemini (Google) | Additional AI-powered research and development workflows |

Both Claude and Gemini models can be used to:
- Navigate and search the literature database
- Extract insights from paper metadata and abstracts
- Generate summaries and identify research connections
- Assist with data processing scripts

## Repository Structure

```
CEI-Literature-Vault/              # Repository root
├── .agent/                        # Google Antigravity skills
├── .claude/                       # Claude Code commands and skills
├── .obsidian/                     # Obsidian vault configuration
├── .venv/                         # Python virtual environment
└── CEI-Lit-WS/                    # Main workspace (GitHub tracked)
    ├── .vault-config.json         # External paths configuration (gitignored)
    ├── README.md                  # This file
    ├── CLAUDE.md                  # Claude Code instructions
    ├── LLM_CONTEXT.md             # Classification logic details
    ├── YAML_SAFEGUARDS.md         # YAML frontmatter rules
    ├── Base Source from Zotero.md # Primary CSV export (read-only)
    ├── docs/                      # All documentation
    ├── logs/                      # Log files and JSON reports
    ├── PYTHON/                    # Python utility scripts
    │   └── vault_config.py        # Centralized path configuration
    ├── STATISTICS/                # Generated statistics reports
    ├── papers/                    # Individual paper files (657 papers)
    ├── PDF Extracts/              # Extracted PDF text (662 Markdown files)
    ├── Authors/                   # Author profiles (2,946 profiles)
    ├── AI Labs/                   # 14 AI Labs: 350+ papers, 500+ files
    ├── paper_analyses/            # Paper analysis outputs
    └── RECYCLE-BIN/               # Deleted files go here

External (configurable via .vault-config.json):
└── /path/to/Lit-WS-PDFs/                 # PDF files (user-configured location)
```

## Setup (New Clone)

1. Clone this repository
2. Copy `.vault-config.json.example` to `.vault-config.json`
3. Edit `pdf_path` in `.vault-config.json` to point to your PDF storage location
4. Create and activate Python virtual environment:
   ```bash
   python3 -m venv ../.venv
   ../.venv/bin/pip install -r requirements.txt
   ```
5. Verify setup:
   ```bash
   ../.venv/bin/python -c "from PYTHON.vault_config import PDFS_DIR; print(f'PDFs: {PDFS_DIR}')"
   ```

## Classification & Scripts

We have implemented an automated classification system to enrich paper metadata. See [LLM_CONTEXT.md](LLM_CONTEXT.md) for detailed logic.

### Metadata Sourcing
New fields have been added to paper YAML headers:
- `ethics_overall`: Classification of paper's relevance to ethics
- `virtue_ethics`, `deontological_ethics`, `utilitarian_ethics`: Specific framework detection
- `ethics_perspective`: Category for general ethics papers (e.g., "AI Safety", "Bias")
- `research_topic`: Topic for non-ethics papers (e.g., "Machine Learning", "NLP")
- `national_ethnic_cultural`: Specific nation, ethnicity, or cultural focus (e.g., "Chinese", "African/Ubuntu")
- `religious_values`: Religious focus (e.g., "Islam", "Christianity")
- `moral_psychology`: Moral psychological theories (e.g., "Moral Foundations Theory")
- `newtags`: Aggregated list of all relevant tags (e.g., `#VirtueEthics`, `#Christianity`)
- `is_benchmark`: Whether the paper introduces/uses a benchmark (Yes/No/N/A/Unknown)
- `is_eval`: Whether the paper provides evaluation/assessment methods (Yes/No/N/A/Unknown)
- `is_dataset`: Whether the paper introduces/describes a dataset (Yes/No/N/A/Unknown)
- `data_description`: Technical description of the data nature
- `data_metrics`: Quantitative metrics (e.g., "817 questions", "100 languages")
- `key_contribution`: (Ethics papers) Summary of specific technical/theoretical contribution
- `significance`: (Ethics papers) Importance for AI alignment/safety context
- `pdf_extract`: (Optional) Relative path to extracted PDF text: `PDF Extracts/YYYY-Author-Title.md`

### Utility Scripts (Located in `PYTHON/` directory)
See [PYTHON/README.md](PYTHON/README.md) for detailed documentation on all scripts.

**Classification Scripts:**
- `PYTHON/classify_ethics.py`: Base ethics classification
- `PYTHON/classify_ethics_perspective.py`: Detailed ethics categorization
- `PYTHON/classify_non_ethics_topics.py`: Research topic classification
- `PYTHON/classify_cultural_religious.py`: Cultural and religious value classification
- `PYTHON/classify_moral_psych.py`: Moral psychology classification
- `PYTHON/classify_data_nature.py`: Benchmark/evaluation/dataset classification with metrics extraction
- `PYTHON/generate_newtags.py`: Aggregate tag generation (supersedes `add_newtags.py`)

**Report Generation Scripts:**
- `PYTHON/generate_stats.py`: Generates `paper-statistics-1.md` report
- `PYTHON/generate_report_v2.py`: Generates detailed statistics report `paper-statistics-2.md`
- `PYTHON/generate_data_report.py`: Generates benchmark/eval/dataset report `data-nature-statistics.md`
- `PYTHON/generate_paper_statistics_3.py`: Generates comprehensive data nature report `paper-statistics-3.md`

**PDF & Data Processing:**
- `PYTHON/prepare_analyses.py`: Prepares extracted text and metadata for content analysis

**Maintenance Utilities:**
- `PYTHON/check_publication_status.py`: Checks Semantic Scholar for published versions of preprints
- `PYTHON/resolve_unknowns.py`: Fixes specific "Unknown" authors/years using hardcoded mappings
- `PYTHON/rename_papers.py`: Standardizes filenames to `YYYY-Author-ShortTitle.md`
- `PYTHON/convert_csv_to_md.py`: Imports papers from Zotero CSV export
- `PYTHON/update_urls.py`: Updates URLs in paper metadata
- `PYTHON/fetch_abstracts.py`: Fetches abstracts from arXiv
- And 10+ additional utility scripts

## Data Source

The primary data file (`Base.md`) is a CSV export from **Zotero** containing:
- Bibliographic metadata (authors, titles, publication dates, DOIs)
- Abstracts and keywords
- Citation information
- Links to PDF attachments

> **Note:** The CSV data in `Base.md` is managed externally via Zotero. Avoid direct edits to maintain synchronization.

## Getting Started

### For Obsidian Users
Open the `CEI-Lit-WS/` folder as an Obsidian vault to browse papers, view connections, and take research notes.

### For AI-Assisted Research
- **Claude Code:** Reference `CLAUDE.md` for Claude-specific guidance
- **Antigravity (Gemini):** The vault is compatible with Gemini workflows for research exploration

### PDF Configuration
PDFs are stored externally to keep the repository lightweight. Configure your PDF location in `.vault-config.json`:
```json
{
  "pdf_path": "/path/to/your/PDFs",
  "zotero_path": "~/Zotero/storage"
}
```

## About CEI

The **Center of Ethical Intelligence** is dedicated to advancing the development of AI systems that are aligned with human values, promoting safety, fairness, and accountability in artificial intelligence research and deployment.

---

*Last updated: February 2026*
