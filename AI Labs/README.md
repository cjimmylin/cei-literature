# AI Labs Repository

This directory serves as a centralized hub for information regarding various AI Labs, their flagship models, and their research directions, particularly focusing on alignment and ethics.

## Statistics (January 2026)

| Metric | Count |
|--------|-------|
| **Total Labs** | 14 |
| **Total PDFs** | 278 |
| **Total Size** | ~1.5 GB |
| **Model READMEs** | 147 |

## Directory Structure

Each major AI lab has its own subfolder containing:
- `README.md` - Lab overview
- `models.md` - Table of all models with documentation links
- `Papers/` - Foundational research papers (PDFs)
- `<Model Name>/` - Model-specific documentation and papers

### US-based Labs
| Lab | PDFs | Notable Models |
|-----|------|----------------|
| [[OpenAI]] | 42 | GPT-4/4o/5, o1/o3, DALL-E, Whisper, Sora |
| [[Anthropic]] | 33 | Claude 3/3.5/3.7/4/4.5 |
| [[Google DeepMind]] | 36 | Gemini, Gemma, Gopher, Flamingo |
| [[Meta AI]] | 15 | Llama 2/3/3.1/3.2/4, Llama Guard |
| [[Microsoft Research]] | 10 | Phi-3/4, Orca |
| [[NVIDIA]] | 10 | Megatron, Nemotron, NVLM |
| [[xAI]] | 0 | Grok (no papers published) |

### European Labs
| Lab | PDFs | Notable Models |
|-----|------|----------------|
| [[Mistral AI]] | 7 | Mistral 7B, Mixtral 8x7B, Ministral |

### Chinese Labs
| Lab | PDFs | Notable Models |
|-----|------|----------------|
| [[DeepSeek]] | 13 | DeepSeek-V2/V3, R1, Coder |
| [[Alibaba (Qwen)]] | 18 | Qwen, Qwen2, Qwen2.5, Qwen-Audio |
| [[Zhipu AI]] | 62 | GLM-130B/4, ChatGLM, CogVLM |
| [[01.AI]] | 2 | Yi Technical Report |
| [[Tencent]] | 17 | Hunyuan, HunyuanVideo |
| [[Baidu]] | 13 | ERNIE 1.0-4.5, ERNIE-ViLG |

## Documentation Coverage

Each model README includes:
- **Papers** - Technical reports, system cards (local PDFs)
- **Blog Posts** - Official announcements
- **GitHub** - Repositories, model weights
- **HuggingFace** - Model cards and downloads
- **API Docs** - Platform documentation
- **Benchmarks** - Performance comparisons

## Contributing

When adding a new lab:
1. Create a subfolder with the lab's full name
2. Copy `TEMPLATE.md` to `[Lab Name]/README.md`
3. Create `models.md` with model table
4. Run `/download-lab-papers <lab>` to populate papers
5. Update this `README.md`

## Reference Template
For a consistent structure across all lab documentation, please refer to the [[TEMPLATE.md|AI Lab Template]].

## Related Commands

- `/download-lab-papers <lab>` - Download all papers for a lab
- See `.claude/skills/download-lab-papers.md` for detailed instructions
