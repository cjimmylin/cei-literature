# Qwen3

## Overview
Next-generation family with "Thinking" mode and native support for over 100 languages.

## Technical Specifications
- **Release Year:** 2025
- **Version:** 3.0
- **Parameters:** 0.6B, 1.7B, 4B, 8B, 14B, 32B, 30B-A3B (MoE), 235B-A22B (MoE)
- **Context Window:** 32K tokens (extendable to 128K with YaRN)
- **Architecture:** Transformer with GQA, SwiGLU, RoPE, RMSNorm, QK-Norm
- **Languages:** 119 languages and dialects supported
- **Key Innovation:** Hybrid thinking mode (seamless switching between thinking/non-thinking)

## Documentation & Links

### Official Resources
- **Blog Post:** [Qwen3: Official Announcement](https://qwenlm.github.io/blog/qwen3/)
- **Research Paper:** [arXiv:2505.09388](https://arxiv.org/abs/2505.09388)

### GitHub Repositories
- **Main Repository:** [github.com/QwenLM/Qwen3](https://github.com/QwenLM/Qwen3)
- **Documentation:** [github.com/QwenLM/Qwen3/blob/main/README.md](https://github.com/QwenLM/Qwen3/blob/main/README.md)

### HuggingFace Models
| Model | HuggingFace Link |
|-------|------------------|
| Qwen3-0.6B | [huggingface.co/Qwen/Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) |
| Qwen3-1.7B | [huggingface.co/Qwen/Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B) |
| Qwen3-4B | [huggingface.co/Qwen/Qwen3-4B](https://huggingface.co/Qwen/Qwen3-4B) |
| Qwen3-8B | [huggingface.co/Qwen/Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B) |
| Qwen3-14B | [huggingface.co/Qwen/Qwen3-14B](https://huggingface.co/Qwen/Qwen3-14B) |
| Qwen3-32B | [huggingface.co/Qwen/Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) |
| Qwen3-30B-A3B | [huggingface.co/Qwen/Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B) |
| Qwen3-235B-A22B | [huggingface.co/Qwen/Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B) |

### ModelScope (China)
- **Qwen3-32B:** [modelscope.cn/models/qwen/Qwen3-32B](https://modelscope.cn/models/qwen/Qwen3-32B)
- **Qwen3-235B-A22B:** [modelscope.cn/models/qwen/Qwen3-235B-A22B](https://modelscope.cn/models/qwen/Qwen3-235B-A22B)
- **Collection:** [modelscope.cn/organization/qwen](https://modelscope.cn/organization/qwen)

### Demo & API
- **Qwen Chat:** [chat.qwenlm.ai](https://chat.qwenlm.ai/)
- **Demo (HuggingFace Spaces):** [huggingface.co/spaces/Qwen/Qwen3-Demo](https://huggingface.co/spaces/Qwen/Qwen3-Demo)
- **Alibaba Cloud API:** [DashScope - Qwen3](https://dashscope.aliyun.com/)
- **Together AI:** [api.together.xyz](https://api.together.xyz/) (Qwen3 models available)
- **Fireworks AI:** [fireworks.ai](https://fireworks.ai/) (Qwen3 models available)

### Benchmarks & Evaluations
- General: MMLU, MMLU-Pro, GPQA-Diamond, ARC-C, LiveBench
- Reasoning: AIME 2024/2025, MATH-500, OlympiadBench
- Coding: LiveCodeBench, HumanEval+, MBPP+
- Multilingual: MMMLU (119 languages)
- Agentic: BFCL, Tau-Bench
- See [Technical Report](https://arxiv.org/abs/2505.09388) for comprehensive benchmark comparisons

### Thinking Mode
Qwen3 supports a unique hybrid thinking mode:
- **Thinking Mode:** Deep reasoning with extended chain-of-thought (use `/think` or `enable_thinking=True`)
- **Non-Thinking Mode:** Fast, direct responses (use `/no_think` or `enable_thinking=False`)
- Seamless switching between modes within conversation

## Papers

| Paper | arXiv ID | Local PDF |
|-------|----------|-----------|
| Qwen3 Technical Report | [2505.09388](https://arxiv.org/abs/2505.09388) | [Qwen3_Technical_Report_2505.09388.pdf](Qwen3_Technical_Report_2505.09388.pdf) |
