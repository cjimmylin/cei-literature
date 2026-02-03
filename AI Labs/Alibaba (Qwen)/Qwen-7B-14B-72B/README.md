# Qwen-7B/14B/72B

## Overview
Foundational dense models of the Tongyi Qianwen series, providing a strong baseline for general-purpose language tasks.

## Technical Specifications
- **Release Year:** 2023
- **Version:** 1.0
- **Parameters:** 7B, 14B, 72B
- **Architecture:** Decoder-only Transformer with RoPE, SwiGLU, RMSNorm, attention QKV bias
- **Context Window:** 8K tokens (extendable via NTK-aware interpolation)
- **Vocabulary:** 151,936 tokens (optimized for Chinese/English)

## Documentation & Links

### Official Resources
- **Blog Post:** [Introducing Qwen-72B and Qwen-1.8B](https://alibabacloud.com/blog/introducing-qwen-72b-and-qwen-1.8b-open-source-llms_600262)
- **Research Paper:** [arXiv:2309.16609](https://arxiv.org/abs/2309.16609)

### GitHub Repositories
- **Main Repository:** [github.com/QwenLM/Qwen](https://github.com/QwenLM/Qwen)
- **Documentation:** [github.com/QwenLM/Qwen/blob/main/README.md](https://github.com/QwenLM/Qwen/blob/main/README.md)

### HuggingFace Models
| Model | HuggingFace Link |
|-------|------------------|
| Qwen-7B | [huggingface.co/Qwen/Qwen-7B](https://huggingface.co/Qwen/Qwen-7B) |
| Qwen-7B-Chat | [huggingface.co/Qwen/Qwen-7B-Chat](https://huggingface.co/Qwen/Qwen-7B-Chat) |
| Qwen-14B | [huggingface.co/Qwen/Qwen-14B](https://huggingface.co/Qwen/Qwen-14B) |
| Qwen-14B-Chat | [huggingface.co/Qwen/Qwen-14B-Chat](https://huggingface.co/Qwen/Qwen-14B-Chat) |
| Qwen-72B | [huggingface.co/Qwen/Qwen-72B](https://huggingface.co/Qwen/Qwen-72B) |
| Qwen-72B-Chat | [huggingface.co/Qwen/Qwen-72B-Chat](https://huggingface.co/Qwen/Qwen-72B-Chat) |

### ModelScope (China)
- **Qwen-72B:** [modelscope.cn/models/qwen/Qwen-72B](https://modelscope.cn/models/qwen/Qwen-72B)
- **Qwen-72B-Chat:** [modelscope.cn/models/qwen/Qwen-72B-Chat](https://modelscope.cn/models/qwen/Qwen-72B-Chat)

### Demo & API
- **Demo (HuggingFace Spaces):** [huggingface.co/spaces/Qwen/Qwen-72B-Chat-Demo](https://huggingface.co/spaces/Qwen/Qwen-72B-Chat-Demo)
- **Alibaba Cloud API:** [DashScope Model Service](https://dashscope.aliyun.com/)

### Benchmarks & Evaluations
- MMLU, C-Eval, GSM8K, MATH, HumanEval, MBPP benchmarks included in technical report
- See [arXiv paper](https://arxiv.org/abs/2309.16609) Section 4 for detailed results

## Papers

| Paper | arXiv ID | Local PDF |
|-------|----------|-----------|
| Qwen Technical Report | [2309.16609](https://arxiv.org/abs/2309.16609) | [Qwen_Technical_Report_2309.16609.pdf](Qwen_Technical_Report_2309.16609.pdf) |
