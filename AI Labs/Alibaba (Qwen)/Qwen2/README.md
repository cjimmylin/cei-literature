# Qwen2

## Overview
Updated open-weights series with better multilingual performance, instruction following, and expanded 32k context support.

## Technical Specifications
- **Release Year:** 2024
- **Version:** 2.0
- **Parameters:** 0.5B, 1.5B, 7B, 57B-A14B (MoE), 72B
- **Context Window:** 32K tokens (128K for 7B/72B Instruct)
- **Architecture:** Transformer with GQA, SwiGLU, RoPE, RMSNorm
- **Languages:** 29 languages supported

## Documentation & Links

### Official Resources
- **Blog Post:** [Qwen2: Official Announcement](https://qwenlm.github.io/blog/qwen2/)
- **Research Paper:** [arXiv:2407.10671](https://arxiv.org/abs/2407.10671)

### GitHub Repositories
- **Main Repository:** [github.com/QwenLM/Qwen2](https://github.com/QwenLM/Qwen2)
- **Documentation:** [github.com/QwenLM/Qwen2/blob/main/README.md](https://github.com/QwenLM/Qwen2/blob/main/README.md)
- **Cookbook/Examples:** [github.com/QwenLM/Qwen2/tree/main/examples](https://github.com/QwenLM/Qwen2/tree/main/examples)

### HuggingFace Models
| Model | HuggingFace Link |
|-------|------------------|
| Qwen2-0.5B | [huggingface.co/Qwen/Qwen2-0.5B](https://huggingface.co/Qwen/Qwen2-0.5B) |
| Qwen2-0.5B-Instruct | [huggingface.co/Qwen/Qwen2-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2-0.5B-Instruct) |
| Qwen2-1.5B | [huggingface.co/Qwen/Qwen2-1.5B](https://huggingface.co/Qwen/Qwen2-1.5B) |
| Qwen2-1.5B-Instruct | [huggingface.co/Qwen/Qwen2-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2-1.5B-Instruct) |
| Qwen2-7B | [huggingface.co/Qwen/Qwen2-7B](https://huggingface.co/Qwen/Qwen2-7B) |
| Qwen2-7B-Instruct | [huggingface.co/Qwen/Qwen2-7B-Instruct](https://huggingface.co/Qwen/Qwen2-7B-Instruct) |
| Qwen2-57B-A14B | [huggingface.co/Qwen/Qwen2-57B-A14B](https://huggingface.co/Qwen/Qwen2-57B-A14B) |
| Qwen2-57B-A14B-Instruct | [huggingface.co/Qwen/Qwen2-57B-A14B-Instruct](https://huggingface.co/Qwen/Qwen2-57B-A14B-Instruct) |
| Qwen2-72B | [huggingface.co/Qwen/Qwen2-72B](https://huggingface.co/Qwen/Qwen2-72B) |
| Qwen2-72B-Instruct | [huggingface.co/Qwen/Qwen2-72B-Instruct](https://huggingface.co/Qwen/Qwen2-72B-Instruct) |

### ModelScope (China)
- **Qwen2-72B:** [modelscope.cn/models/qwen/Qwen2-72B](https://modelscope.cn/models/qwen/Qwen2-72B)
- **Qwen2-72B-Instruct:** [modelscope.cn/models/qwen/Qwen2-72B-Instruct](https://modelscope.cn/models/qwen/Qwen2-72B-Instruct)

### Demo & API
- **Demo (HuggingFace Spaces):** [huggingface.co/spaces/Qwen/Qwen2-72B-Instruct](https://huggingface.co/spaces/Qwen/Qwen2-72B-Instruct)
- **Alibaba Cloud API:** [DashScope - Qwen2](https://dashscope.aliyun.com/)
- **Together AI:** [api.together.xyz](https://api.together.xyz/) (Qwen2 models available)

### Benchmarks & Evaluations
- MMLU, GPQA, MATH, GSM8K, HumanEval, MBPP, IFEval
- Multilingual benchmarks across 29 languages
- See [arXiv paper](https://arxiv.org/abs/2407.10671) for detailed benchmark comparisons

## Papers

| Paper | arXiv ID | Local PDF |
|-------|----------|-----------|
| Qwen2 Technical Report | [2407.10671](https://arxiv.org/abs/2407.10671) | [Qwen2_Technical_Report_2407.10671.pdf](Qwen2_Technical_Report_2407.10671.pdf) |
