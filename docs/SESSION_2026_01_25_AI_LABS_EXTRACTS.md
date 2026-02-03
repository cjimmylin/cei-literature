# Session: AI Labs PDF Extraction & Organization

**Date:** January 25, 2026
**Focus:** PDF text extraction for AI Labs, overview generation, and file reorganization

## Summary

This session focused on making AI Labs documentation searchable and well-organized:

1. **Extracted text from 111 unique AI Labs PDFs** into searchable markdown files
2. **Created overview.md files for all 14 AI labs** using parallel agents
3. **Reorganized extracts** from generic folder to model-specific folders

## Tasks Completed

### 1. PDF Text Extraction (111 files)

Created `PYTHON/extract_ai_labs_pdfs.py` to extract text from all PDFs in the AI Labs folder.

**Key features:**
- Handles duplicate PDFs (same file in multiple locations)
- Prefers model-specific folders over Papers/ folders for duplicates
- Creates markdown extracts with YAML frontmatter
- Extracts company and model info from folder path

**Statistics:**
| Company | Extracts |
|---------|----------|
| OpenAI | 24 |
| Google DeepMind | 16 |
| Zhipu AI | 13 |
| Anthropic | 10 |
| DeepSeek | 11 |
| Alibaba (Qwen) | 7 |
| NVIDIA | 6 |
| Meta AI | 5 |
| Baidu | 4 |
| Microsoft Research | 3 |
| Mistral AI | 3 |
| Tencent | 3 |
| 01.AI | 1 |

### 2. Lab Overview Generation (14 files)

Created comprehensive `overview.md` files for each AI lab using **parallel agents** (14 agents simultaneously).

**Each overview includes:**
- Lab introduction/history
- Model summary table (name, year, type, parameters, features)
- Detailed sections for each model family
- Links to source PDFs

**Labs with overviews:**
- 01.AI, Alibaba (Qwen), Anthropic, Baidu, DeepSeek
- Google DeepMind, Meta AI, Microsoft Research, Mistral AI
- NVIDIA, OpenAI, Tencent, xAI, Zhipu AI

### 3. Extract Reorganization

Created `PYTHON/move_ai_lab_extracts.py` to move extracts from generic folder to model folders.

**Before:** `PDF Extracts/AI Labs/Company-filename.md`
**After:** `AI Labs/Company/Model/filename.md`

The script:
- Reads `source_pdf` field from extract YAML frontmatter
- Determines destination folder from original PDF location
- Moves extract to same folder as source PDF
- Removes company prefix from filename

## New Scripts Created

### `PYTHON/extract_ai_labs_pdfs.py`

```bash
# Extract text from all AI Labs PDFs
python3 PYTHON/extract_ai_labs_pdfs.py
```

**Features:**
- Finds all unique PDFs in `AI Labs/` (handles duplicates)
- Creates markdown extracts with YAML frontmatter
- Saves to `PDF Extracts/AI Labs/` (original location)
- Includes company, model, page count in metadata

**Extract format:**
```yaml
---
title: "Model Name"
source_pdf: "AI Labs/Company/Model/filename.pdf"
company: "Company"
pages: 120
extracted_at: "2026-01-25T04:43:43.635840"
type: "ai_lab_paper"
---

# Model Name

**Company/Lab:** Company
**Model:** Model Name
**Source PDF:** path/to/file.pdf
**Total Pages:** 120

---

## Content

```
[Full extracted text with page markers]
```

### `PYTHON/move_ai_lab_extracts.py`

```bash
# Move extracts to model folders
python3 PYTHON/move_ai_lab_extracts.py
```

**Features:**
- Reads source_pdf from YAML frontmatter
- Moves extracts to same folder as source PDF
- Removes company prefix from filename
- Reports moved/skipped/errors

## Key Learnings

### Parallel Agent Usage

- Spawned **14 agents simultaneously** for overview generation
- Each agent reads extracts, analyzes content, writes overview
- Two agents (Google DeepMind, Zhipu AI) hit context limits due to document volume
- Solution: Re-run with simpler prompts focusing on key facts

### PDF Extract Organization

- **Colocate extracts with source PDFs** for easier navigation
- Extract YAML frontmatter should include `source_pdf` for traceability
- Company name in extract filename aids sorting but should be removed when moving

### AI Labs Folder Structure

Standard structure for each lab:
```
AI Labs/
└── Company/
    ├── overview.md           # Lab summary
    ├── models.md            # Model list
    ├── Papers/              # Research papers
    │   ├── paper.pdf
    │   └── paper.md         # Extract
    └── Model Name/          # Model-specific folder
        ├── README.md        # Model details
        ├── model_card.pdf
        └── model_card.md    # Extract
```

## Files Modified/Created

### New Files
- `PYTHON/extract_ai_labs_pdfs.py` - AI Labs PDF extraction script
- `PYTHON/move_ai_lab_extracts.py` - Extract relocation script
- `AI Labs/*/overview.md` - 14 overview files

### Files Moved
- 111 extract files from `PDF Extracts/AI Labs/` to `AI Labs/*/`

## Usage for Future Sessions

### Adding New AI Lab Papers

1. Download PDFs to `AI Labs/Company/Model/` folder
2. Run extraction: `python3 PYTHON/extract_ai_labs_pdfs.py`
3. Move extracts: `python3 PYTHON/move_ai_lab_extracts.py`
4. Update overview: Ask Claude to regenerate `AI Labs/Company/overview.md`

### Regenerating Overviews

For a single lab:
```
Create an overview.md for [Lab Name] summarizing all models based on the PDF extracts in AI Labs/[Lab Name]/
```

For all labs (parallel):
```
Create overview.md files for each AI lab using parallel agents
```

## Related Documentation

- [SESSION_HISTORY.md](SESSION_HISTORY.md) - Session 15: AI Labs paper download
- [download-lab-papers.md](../.claude/skills/download-lab-papers.md) - Paper download skill
- [SCRIPTS.md](SCRIPTS.md) - All Python scripts reference
