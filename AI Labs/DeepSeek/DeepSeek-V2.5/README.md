# DeepSeek-V2.5

## Overview
Optimized version of DeepSeek-V2 with improved multilingual performance and significantly enhanced tool-calling capabilities. Achieves better results on AlpacaEval 2.0, ArenaHard, MT-Bench, HumanEval, and LiveCodeBench compared to V2.

## Technical Specifications
- **Release Year:** 2024
- **Version:** 2.5
- **Parameters:** 236B total
- **Architecture:** MoE (Mixture-of-Experts)
- **Hardware Requirements:** 80GB x 8 GPUs (BF16 inference)
- **License:** MIT (code) + DeepSeek Model Agreement (supports commercial use)

## Benchmarks

| Metric | DeepSeek-V2-0628 | DeepSeek-Coder-V2 | DeepSeek-V2.5 |
|--------|------------------|-------------------|---------------|
| AlpacaEval 2.0 | 46.6 | 44.5 | **50.5** |
| ArenaHard | 68.3 | 66.3 | **76.2** |
| MT-Bench | 8.85 | 8.91 | **9.02** |
| HumanEval Python | 84.5 | 87.2 | **89.0** |
| LiveCodeBench | 36.6 | 39.7 | **41.8** |

## Papers

No dedicated technical paper. See [DeepSeek-V2](../DeepSeek-V2/README.md) for the foundational architecture paper (arXiv: 2405.04434).

## Documentation & Links

### Official Resources
| Resource | Link |
|----------|------|
| Official Website | [deepseek.com](https://www.deepseek.com/) |
| Blog Post | [DeepSeek-V2.5 Announcement](https://deepseek.com/blog/deepseek-v2-5/) |
| Chat Interface | [chat.deepseek.com](https://chat.deepseek.com/) |
| API Platform | [platform.deepseek.com](https://platform.deepseek.com/) |

### GitHub
| Repository | Link |
|------------|------|
| DeepSeek-V2 | [github.com/deepseek-ai/DeepSeek-V2](https://github.com/deepseek-ai/DeepSeek-V2) |

### HuggingFace Models
| Model | Link |
|-------|------|
| DeepSeek-V2.5 | [HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-V2.5) |

### Research Paper (V2 Architecture)
| Resource | Link |
|----------|------|
| arXiv | [arxiv.org/abs/2405.04434](https://arxiv.org/abs/2405.04434) |
| PDF | [arXiv PDF](https://arxiv.org/pdf/2405.04434) |

### Community
| Platform | Link |
|----------|------|
| Discord | [DeepSeek Discord](https://discord.gg/Tc7c45Zzu5) |
| Twitter/X | [@deepseek_ai](https://twitter.com/deepseek_ai) |
| Contact | service@deepseek.com |
