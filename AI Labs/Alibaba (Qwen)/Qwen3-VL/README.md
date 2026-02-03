# Qwen3-VL

## Overview
Qwen3-VL is the most capable vision-language model in the Qwen series to date, achieving superior performance across a broad range of multimodal benchmarks. It natively supports interleaved contexts of up to 256K tokens, seamlessly integrating text, images, and video.

## Technical Specifications
- **Release Year:** 2025
- **Version:** 3.0
- **Parameters:** 2B, 4B, 8B, 32B, 30B-A3B (MoE), 235B-A22B (MoE)
- **Architecture:** Dense and Mixture-of-Experts variants
- **Context Window:** 256K tokens (native support for text, images, and video)

## Key Capabilities
- **Pure-Text Understanding:** Surpasses comparable text-only backbones in several cases
- **Long-Context Comprehension:** Native 256K-token window for both text and interleaved multimodal inputs
- **Advanced Multimodal Reasoning:** Leading performance on single-image, multi-image, and video tasks
- **Benchmarks:** SOTA on MMMU, MathVista, MathVision

## Documentation & Links

### Official Resources
- **Technical Report:** [arXiv:2511.21631](https://arxiv.org/abs/2511.21631)
- **Blog Post:** [Qwen3-VL Announcement](https://qwen.ai/blog)

### GitHub Repositories
- **Main Repository:** [github.com/QwenLM/Qwen3-VL](https://github.com/QwenLM/Qwen3-VL)

### HuggingFace Models
| Model | HuggingFace Link |
|-------|------------------|
| Qwen3-VL-2B | [huggingface.co/Qwen/Qwen3-VL-2B](https://huggingface.co/Qwen/Qwen3-VL-2B) |
| Qwen3-VL-4B | [huggingface.co/Qwen/Qwen3-VL-4B](https://huggingface.co/Qwen/Qwen3-VL-4B) |
| Qwen3-VL-8B | [huggingface.co/Qwen/Qwen3-VL-8B](https://huggingface.co/Qwen/Qwen3-VL-8B) |
| Qwen3-VL-32B | [huggingface.co/Qwen/Qwen3-VL-32B](https://huggingface.co/Qwen/Qwen3-VL-32B) |

### Demo & API
- **Qwen Chat:** [chat.qwenlm.ai](https://chat.qwenlm.ai/)
- **Alibaba Cloud API:** [DashScope](https://dashscope.aliyun.com/)

## Papers

| Paper | arXiv ID | Local PDF |
|-------|----------|-----------|
| Qwen3-VL Technical Report | [2511.21631](https://arxiv.org/abs/2511.21631) | [Qwen3-VL_Technical_Report_2511.21631.pdf](Qwen3-VL_Technical_Report_2511.21631.pdf) |

## Related Models
- **Qwen3-VL-Embedding:** [arXiv:2601.04720](https://arxiv.org/abs/2601.04720) - Multimodal retrieval and ranking framework
