# AI Labs PDF Extraction Status

**Last Updated:** 2026-01-31
**Coverage:** 99.3% (270/272 PDFs)

## Summary

All AI Labs PDFs have been processed for text extraction. Extracts are stored in centralized location with standardized naming.

### Statistics
- **Total PDFs:** 272
- **Valid Extracts:** 270 (99.3%)
- **Placeholder Files:** 3 (0.7%)
- **New Extracts Created:** 23 (on 2026-01-31)

### Extract Location
```
/Users/jimmy.lin/Documents/CEI-Literature-Vault/PDF Extracts/AI Labs/
```

### Naming Convention
```
{Lab-Name}-{Filename}.md
```

Example: `OpenAI-gpt-5-system-card.md`

## Coverage by Lab

| Lab | PDFs | Status |
|-----|------|--------|
| OpenAI | 75+ | ✓ Complete |
| Zhipu AI | 50+ | ✓ Complete |
| Google DeepMind | 40+ | ✓ Complete |
| Anthropic | 25+ | ✓ Complete (3 placeholders) |
| Meta AI | 25+ | ✓ Complete |
| DeepSeek | 20+ | ✓ Complete |
| Alibaba (Qwen) | 20+ | ✓ Complete |
| Tencent | 15+ | ✓ Complete |
| Baidu | 12+ | ✓ Complete |
| Microsoft Research | 10+ | ✓ Complete |
| NVIDIA | 10+ | ✓ Complete |
| Mistral AI | 5+ | ✓ Complete |
| 01.AI | 3 | ✓ Complete |

## Missing PDFs (Placeholder Files)

The following files are ASCII text placeholders, not actual PDFs:

1. `AI Labs/Anthropic/Papers/Claude_Character_2024.pdf` (15 bytes)
2. `AI Labs/Anthropic/Papers/Core_Views_on_AI_Safety.pdf` (66 bytes)
3. `AI Labs/Anthropic/Papers/Scaling_Monosemanticity_Features_in_Claude_3_Sonnet_2024.pdf` (243 bytes)

**Action:** Need to download actual PDFs from Anthropic's website/publications.

## Recent Updates (2026-01-31)

### New Extracts Created
23 new extracts for recently added OpenAI papers:

**GPT-5 Series (9):**
- gpt-5-arxiv-2601.03267
- gpt-5-system-card (multiple versions)
- gpt-5.1-codex-max-card
- gpt-5.1-codex-max-model-card
- gpt-5.2-system-card (December 2025)

**GPT-4.5 (2):**
- gpt-4.5-system-card-february-2025
- gpt-4-5-system-card

**o3 (2):**
- competitive-programming-large-reasoning-models
- o3-and-o4-mini-system-card

**o1 (2):**
- deliberative-alignment-arxiv-2412.16720
- o1-system-card-arxiv-2412.16720

**GPT-4 (4):**
- gpt-4-technical-report-arxiv
- gpt-4v-vision-system-card
- gpt-4v-system-card
- gpt-4-technical-report-arxiv-2303.08774

**DALL-E (2):**
- dall-e-3-style-transfer-arxiv-2412.05325
- dall-e-3-arabic-script-arxiv-2502.20459

**New Products (2):**
- operator-system-card-january-2025 (ChatGPT-Agent)
- deep-research-system-card-february-2025

## Extraction Process

To extract new PDFs, use:
```bash
.venv/bin/python PYTHON/extract_ai_labs_pdfs.py
```

This script:
- Scans all PDFs in `AI Labs/` directory
- Extracts text to markdown with YAML frontmatter
- Saves to `PDF Extracts/AI Labs/` with lab prefix
- Skips already-extracted files

## Quality Metrics

Extract files contain:
- **YAML frontmatter:** company, model, page count, timestamp
- **Full text content:** Formatted as markdown
- **Typical size:** 1,000-4,000 lines per extract

## Verification

Last verified: 2026-01-31 using 10 parallel agents
- Processed all 272 PDFs
- Created 23 new extracts
- Verified 247 existing extracts
- Identified 3 placeholder files

See detailed log: `logs/session_2026-01-31_ai_labs_pdf_extraction.md`
