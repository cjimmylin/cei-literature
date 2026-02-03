# Qwen2.5-1M

## Overview
Specialized long-context variants of the Qwen2.5 series, supporting natively up to 1 million tokens.

## Technical Specifications
- **Release Year:** 2025
- **Version:** 2.51
- **Parameters:** 7B, 14B (1M context variants)
- **Context Window:** 1,000,000 tokens (native)
- **Architecture:** Based on Qwen2.5 with optimized attention for extreme long context
- **Key Innovation:** Dual-chunk attention, sparse attention patterns for efficient 1M token processing

## Documentation & Links

### Official Resources
- **Blog Post:** [Qwen2.5-1M: Official Announcement](https://qwenlm.github.io/blog/qwen2.5-1m/)
- **Technical Report:** [arXiv:2501.15383](https://arxiv.org/abs/2501.15383)

### GitHub Repositories
- **Main Repository:** [github.com/QwenLM/Qwen2.5](https://github.com/QwenLM/Qwen2.5) (1M variants included)
- **Documentation:** [github.com/QwenLM/Qwen2.5/blob/main/README.md](https://github.com/QwenLM/Qwen2.5/blob/main/README.md)

### HuggingFace Models
| Model | HuggingFace Link |
|-------|------------------|
| Qwen2.5-7B-Instruct-1M | [huggingface.co/Qwen/Qwen2.5-7B-Instruct-1M](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-1M) |
| Qwen2.5-14B-Instruct-1M | [huggingface.co/Qwen/Qwen2.5-14B-Instruct-1M](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct-1M) |

### ModelScope (China)
- **Qwen2.5-7B-Instruct-1M:** [modelscope.cn/models/qwen/Qwen2.5-7B-Instruct-1M](https://modelscope.cn/models/qwen/Qwen2.5-7B-Instruct-1M)
- **Qwen2.5-14B-Instruct-1M:** [modelscope.cn/models/qwen/Qwen2.5-14B-Instruct-1M](https://modelscope.cn/models/qwen/Qwen2.5-14B-Instruct-1M)

### Demo & API
- **Qwen Chat:** [chat.qwenlm.ai](https://chat.qwenlm.ai/)
- **Alibaba Cloud API:** [DashScope](https://dashscope.aliyun.com/)

### Benchmarks & Evaluations
- Long Context: RULER (up to 1M tokens), Needle-in-Haystack, LongBench
- Passkey Retrieval: Near-perfect accuracy at 1M token context
- Multi-document QA: Evaluated on extremely long document collections
- See [Technical Report](https://arxiv.org/abs/2501.15383) for detailed long-context benchmark results

## Papers

| Paper | arXiv ID | Local PDF |
|-------|----------|-----------|
| Qwen2.5-1M Technical Report | [2501.15383](https://arxiv.org/abs/2501.15383) | [Qwen2.5-1M_Technical_Report_2501.15383.pdf](Qwen2.5-1M_Technical_Report_2501.15383.pdf) |
