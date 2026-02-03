# DeepSeek-R1

## Overview
Reasoning model trained with large-scale Reinforcement Learning (RL) without initial supervised fine-tuning, showing competitive performance with OpenAI's o1 across major math, code, and reasoning benchmarks.

## Technical Specifications
- **Release Year:** 2025
- **Version:** 1.0
- **Parameters:** 671B total, 37B active per token
- **Context Window:** 128K tokens
- **Architecture:** MoE (Mixture-of-Experts)
- **Training:** Large-scale RL without initial SFT
- **License:** MIT (supports commercial use)

## Model Variants

### Full Models
| Model | Parameters (Total/Active) | Context |
|-------|---------------------------|---------|
| DeepSeek-R1-Zero | 671B / 37B | 128K |
| DeepSeek-R1 | 671B / 37B | 128K |

### Distilled Models
| Model | Base | Parameters |
|-------|------|------------|
| DeepSeek-R1-Distill-Qwen-1.5B | Qwen | 1.5B |
| DeepSeek-R1-Distill-Qwen-7B | Qwen | 7B |
| DeepSeek-R1-Distill-Qwen-14B | Qwen | 14B |
| DeepSeek-R1-Distill-Qwen-32B | Qwen | 32B |
| DeepSeek-R1-Distill-Llama-8B | Llama | 8B |
| DeepSeek-R1-Distill-Llama-70B | Llama | 70B |

## Papers

| Paper | arXiv ID | Local PDF |
|-------|----------|-----------|
| DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning | 2501.12948 | [PDF](DeepSeek-R1_arxiv_2501.12948.pdf) |

## Documentation & Links

### Official Resources
| Resource | Link |
|----------|------|
| Official Website | [deepseek.com](https://www.deepseek.com/) |
| Blog Post | [DeepSeek-R1 Announcement](https://deepseek.com/blog/deepseek-r1/) |
| Chat Interface | [chat.deepseek.com](https://chat.deepseek.com/) |
| API Platform | [platform.deepseek.com](https://platform.deepseek.com/) |

### GitHub
| Repository | Link |
|------------|------|
| DeepSeek-R1 | [github.com/deepseek-ai/DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) |

### HuggingFace Models
| Model | Link |
|-------|------|
| DeepSeek-R1 | [HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-R1) |
| DeepSeek-R1-Zero | [HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-R1-Zero) |
| DeepSeek-R1-Distill-Qwen-32B | [HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B) |
| DeepSeek-R1-Distill-Qwen-14B | [HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B) |
| DeepSeek-R1-Distill-Qwen-7B | [HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B) |
| DeepSeek-R1-Distill-Qwen-1.5B | [HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B) |
| DeepSeek-R1-Distill-Llama-70B | [HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-70B) |
| DeepSeek-R1-Distill-Llama-8B | [HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-8B) |

### Research Paper
| Resource | Link |
|----------|------|
| arXiv | [arxiv.org/abs/2501.12948](https://arxiv.org/abs/2501.12948) |
| PDF | [arXiv PDF](https://arxiv.org/pdf/2501.12948) |

### Usage Recommendations
- **Temperature:** 0.5-0.7 (0.6 recommended)
- **System Prompts:** Avoid; use user prompt only
- **Math Problems:** Include "put your final answer within \boxed{}"
- **Force Reasoning:** Enforce response starting with `<think>\n`

### Community
| Platform | Link |
|----------|------|
| Discord | [DeepSeek Discord](https://discord.gg/Tc7c45Zzu5) |
| Twitter/X | [@deepseek_ai](https://twitter.com/deepseek_ai) |
| Contact | service@deepseek.com |
