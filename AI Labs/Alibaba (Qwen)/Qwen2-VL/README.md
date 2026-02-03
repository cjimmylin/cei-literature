# Qwen2-VL

## Overview
Second generation vision-language models with massive improvements in resolution, document analysis, and native video understanding.

## Technical Specifications
- **Release Year:** 2024
- **Version:** 2.1
- **Parameters:** 2B, 7B, 72B
- **Architecture:** Naive Dynamic Resolution + Multimodal Rotary Position Embedding (M-RoPE)
- **Capabilities:** Any-resolution image/video understanding, multilingual OCR, video comprehension up to 20+ minutes
- **Input Types:** Images, videos, text (interleaved)

## Documentation & Links

### Official Resources
- **Blog Post:** [Qwen2-VL: Official Announcement](https://qwenlm.github.io/blog/qwen2-vl/)
- **Research Paper:** [arXiv:2410.00520](https://arxiv.org/abs/2410.00520)

### GitHub Repositories
- **Main Repository:** [github.com/QwenLM/Qwen2-VL](https://github.com/QwenLM/Qwen2-VL)
- **Documentation:** [github.com/QwenLM/Qwen2-VL/blob/main/README.md](https://github.com/QwenLM/Qwen2-VL/blob/main/README.md)
- **Cookbooks:** [github.com/QwenLM/Qwen2-VL/tree/main/cookbooks](https://github.com/QwenLM/Qwen2-VL/tree/main/cookbooks)

### HuggingFace Models
| Model | HuggingFace Link |
|-------|------------------|
| Qwen2-VL-2B | [huggingface.co/Qwen/Qwen2-VL-2B](https://huggingface.co/Qwen/Qwen2-VL-2B) |
| Qwen2-VL-2B-Instruct | [huggingface.co/Qwen/Qwen2-VL-2B-Instruct](https://huggingface.co/Qwen/Qwen2-VL-2B-Instruct) |
| Qwen2-VL-7B | [huggingface.co/Qwen/Qwen2-VL-7B](https://huggingface.co/Qwen/Qwen2-VL-7B) |
| Qwen2-VL-7B-Instruct | [huggingface.co/Qwen/Qwen2-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct) |
| Qwen2-VL-72B-Instruct | [huggingface.co/Qwen/Qwen2-VL-72B-Instruct](https://huggingface.co/Qwen/Qwen2-VL-72B-Instruct) |
| Qwen2-VL-72B-Instruct-AWQ | [huggingface.co/Qwen/Qwen2-VL-72B-Instruct-AWQ](https://huggingface.co/Qwen/Qwen2-VL-72B-Instruct-AWQ) |
| Qwen2-VL-72B-Instruct-GPTQ-Int4 | [huggingface.co/Qwen/Qwen2-VL-72B-Instruct-GPTQ-Int4](https://huggingface.co/Qwen/Qwen2-VL-72B-Instruct-GPTQ-Int4) |

### ModelScope (China)
- **Qwen2-VL-7B-Instruct:** [modelscope.cn/models/qwen/Qwen2-VL-7B-Instruct](https://modelscope.cn/models/qwen/Qwen2-VL-7B-Instruct)
- **Qwen2-VL-72B-Instruct:** [modelscope.cn/models/qwen/Qwen2-VL-72B-Instruct](https://modelscope.cn/models/qwen/Qwen2-VL-72B-Instruct)

### Demo & API
- **Demo (HuggingFace Spaces):** [huggingface.co/spaces/Qwen/Qwen2-VL](https://huggingface.co/spaces/Qwen/Qwen2-VL)
- **Alibaba Cloud API:** [DashScope Multimodal Service](https://dashscope.aliyun.com/)

### Benchmarks & Evaluations
- Vision-Language: DocVQA, ChartQA, InfoVQA, TextVQA, OCRBench
- Video Understanding: Video-MME, MVBench
- General VQA: MMMU, MathVista, RealWorldQA
- See [arXiv paper](https://arxiv.org/abs/2410.00520) for comprehensive benchmark results

## Papers

| Paper | arXiv ID | Local PDF |
|-------|----------|-----------|
| Qwen2-VL: Enhancing Vision-Language Model's Perception | [2410.00520](https://arxiv.org/abs/2410.00520) | [Qwen2-VL_2410.00520.pdf](Qwen2-VL_2410.00520.pdf) |
