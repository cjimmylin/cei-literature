# Session Summary: AI Labs Paper Download (January 25, 2025)

## Overview

Comprehensive download of technical papers, system cards, model cards, and documentation for all major AI labs. Created `/download-lab-papers` skill for future use.

## Accomplishments

### 1. Created New Skill
- **File:** `.claude/skills/download-lab-papers.md`
- **Command:** `.claude/commands/download-lab-papers.md`
- **Usage:** `/download-lab-papers <lab-name>`

### 2. Downloaded Papers (140 PDFs, ~880 MB)

| Lab | PDFs | Size | Key Papers |
|-----|------|------|------------|
| Google DeepMind | 26 | 192 MB | Gemini 1.0/1.5, Gopher, Chinchilla, Flamingo, Gato, PaLM |
| Zhipu AI | 20 | 163 MB | GLM-130B, ChatGLM, CogVLM, CogVideo |
| OpenAI | 26 | 160 MB | GPT-1/2/3/4, DALL-E 1/2/3, Whisper, o1, CLIP |
| Anthropic | 12 | 97 MB | Constitutional AI, RLHF, Claude system cards |
| Tencent | 3 | 78 MB | Hunyuan-Large, HunyuanVideo |
| Meta AI | 9 | 59 MB | LLaMA, Llama 2/3/3.1, Code Llama |
| Mistral AI | 6 | 37 MB | Mistral 7B, Mixtral 8x7B, Pixtral |
| DeepSeek | 11 | 33 MB | DeepSeek LLM, V2, V3, R1, Math, VL, Prover |
| Alibaba (Qwen) | 12 | 25 MB | Qwen, Qwen2, Qwen2.5, Qwen-VL |
| NVIDIA | 6 | 20 MB | Megatron-LM, Nemotron-4, NVLM |
| Microsoft | 4 | 7.5 MB | Phi-3, Orca 1/2 |
| 01.AI | 1 | 5.6 MB | Yi Technical Report |
| Baidu | 4 | 2.9 MB | ERNIE 1.0/2.0/3.0/Titan |
| xAI | 0 | - | No papers published |

### 3. Added Documentation Links

Each model README now includes:
- Blog posts and announcements
- GitHub repository links
- HuggingFace model pages
- API documentation links
- Benchmark tables
- Technical specifications

### 4. Updated Files

- `AI Labs/README.md` - Added statistics and structure
- `AI Labs/<Lab>/models.md` - Added paper links, documentation columns
- `AI Labs/<Lab>/<Model>/README.md` - Added Documentation & Links sections
- `AI Labs/<Lab>/Papers/README.md` - Created paper indices
- `.claude/skills/download-lab-papers.md` - Enhanced with learnings
- `docs/COMMANDS.md` - Added `/download-lab-papers` command

## Key Learnings

### Paper Availability Patterns

1. **Excellent arxiv coverage:** DeepSeek, Alibaba (Qwen), Meta AI, Google DeepMind
2. **Good arxiv coverage:** Anthropic, OpenAI, Zhipu AI
3. **Partial coverage:** Mistral AI (many closed models)
4. **Single paper:** 01.AI (Yi Technical Report covers all)
5. **No papers:** xAI (all Grok models)

### Models Without Technical Papers

- **xAI:** All Grok models (only GitHub README for Grok-1)
- **Mistral:** Mistral Large, Large 2, Codestral, NeMo, Small, Medium
- **OpenAI:** GPT-3.5, GPT-4 Turbo, o3, o3-mini, Sora
- **Google:** Gemini 2.0+, Veo, AlphaCode 3 (too new)

### Common arxiv IDs

```
# Anthropic
Constitutional AI: 2212.08073
RLHF Training: 2204.05862

# OpenAI
GPT-3: 2005.14165
GPT-4: 2303.08774
Whisper: 2212.04356

# Google DeepMind
Gemini 1.5: 2403.05530
Gopher: 2112.11446
Chinchilla: 2203.15556

# Meta AI
LLaMA: 2302.13971
Llama 2: 2307.09288
Llama 3: 2407.21783

# DeepSeek
DeepSeek-V2: 2405.04434
DeepSeek-V3: 2412.19437
DeepSeek-R1: 2501.12948

# Qwen
Qwen: 2309.16609
Qwen2: 2407.10671
Qwen2.5: 2412.15115
```

### Documentation URL Patterns

| Lab | System Cards | Blog | GitHub | HuggingFace |
|-----|--------------|------|--------|-------------|
| Anthropic | assets.anthropic.com | anthropic.com/news | - | - |
| OpenAI | cdn.openai.com | openai.com/blog | github.com/openai | - |
| DeepMind | - | deepmind.google | github.com/google-deepmind | huggingface.co/google |
| Meta AI | GitHub | ai.meta.com/blog | github.com/meta-llama | huggingface.co/meta-llama |
| Mistral | - | mistral.ai/news | github.com/mistralai | huggingface.co/mistralai |
| DeepSeek | - | deepseek.com | github.com/deepseek-ai | huggingface.co/deepseek-ai |
| Qwen | - | qwenlm.github.io | github.com/QwenLM | huggingface.co/Qwen |

## Directory Structure

```
AI Labs/
├── README.md                    # Overview with statistics
├── TEMPLATE.md                  # Template for new labs
├── Anthropic/
│   ├── README.md
│   ├── models.md               # Enhanced with doc links
│   ├── Papers/                 # Foundational papers
│   │   ├── README.md
│   │   └── *.pdf
│   ├── Claude/
│   │   └── README.md           # With Documentation & Links
│   ├── Claude 2/
│   ├── Claude 3/
│   ├── Claude 3.5 Sonnet/
│   ├── Claude 3.5 Haiku/
│   ├── Claude 3.7 Sonnet/      # NEW
│   ├── Claude 4/
│   ├── Claude 4.5 Sonnet/      # NEW
│   ├── Claude 4.5 Opus/        # NEW
│   └── Claude 4.5 Haiku/       # NEW
├── OpenAI/
│   ├── models.md
│   ├── Papers/
│   ├── GPT-1/ through GPT-4o/
│   ├── o1/, o3/
│   ├── DALL·E/, Whisper/, Sora/
│   └── ...
├── [Other labs with similar structure]
```

## Future Improvements

1. **Automated updates:** Script to check for new papers periodically
2. **Paper extracts:** Run `/extract-pdf-text` on downloaded papers
3. **Cross-references:** Link papers to related vault papers
4. **Benchmark tracking:** Track model performance over time

## Commands Reference

```bash
# Download papers for a specific lab
/download-lab-papers OpenAI
/download-lab-papers "Google DeepMind"
/download-lab-papers Anthropic

# Check PDF counts
find "AI Labs" -name "*.pdf" | wc -l

# Check total size
du -sh "AI Labs"
```
