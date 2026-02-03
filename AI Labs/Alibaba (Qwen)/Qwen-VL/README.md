# Qwen-VL

## Overview
Large-scale vision-language models capable of image understanding, document analysis, and visual conversation.

## Technical Specifications
- **Release Year:** 2023
- **Version:** 1.0
- **Architecture:** Vision Transformer (ViT-G) + Qwen-7B LLM with cross-attention adapter
- **Image Resolution:** 448x448 (with position-aware vision-language adapter)
- **Capabilities:** Image captioning, VQA, OCR, document understanding, grounding

## Documentation & Links

### Official Resources
- **Blog Post:** [Alibaba's Open Source Vision-Language Models](https://alibabacloud.com/blog/alibabas-open-source-vision-language-models_600244)
- **Research Paper:** [arXiv:2308.12966](https://arxiv.org/abs/2308.12966)

### GitHub Repositories
- **Main Repository:** [github.com/QwenLM/Qwen-VL](https://github.com/QwenLM/Qwen-VL)
- **Documentation:** [github.com/QwenLM/Qwen-VL/blob/master/README.md](https://github.com/QwenLM/Qwen-VL/blob/master/README.md)
- **Evaluation Code:** [github.com/QwenLM/Qwen-VL/tree/master/eval_mm](https://github.com/QwenLM/Qwen-VL/tree/master/eval_mm)

### HuggingFace Models
| Model | HuggingFace Link |
|-------|------------------|
| Qwen-VL | [huggingface.co/Qwen/Qwen-VL](https://huggingface.co/Qwen/Qwen-VL) |
| Qwen-VL-Chat | [huggingface.co/Qwen/Qwen-VL-Chat](https://huggingface.co/Qwen/Qwen-VL-Chat) |
| Qwen-VL-Chat-Int4 | [huggingface.co/Qwen/Qwen-VL-Chat-Int4](https://huggingface.co/Qwen/Qwen-VL-Chat-Int4) |

### ModelScope (China)
- **Qwen-VL:** [modelscope.cn/models/qwen/Qwen-VL](https://modelscope.cn/models/qwen/Qwen-VL)
- **Qwen-VL-Chat:** [modelscope.cn/models/qwen/Qwen-VL-Chat](https://modelscope.cn/models/qwen/Qwen-VL-Chat)

### Demo & API
- **Demo (HuggingFace Spaces):** [huggingface.co/spaces/Qwen/Qwen-VL-Chat-Demo](https://huggingface.co/spaces/Qwen/Qwen-VL-Chat-Demo)
- **ModelScope Demo:** [modelscope.cn/studios/qwen/Qwen-VL-Chat-Demo](https://modelscope.cn/studios/qwen/Qwen-VL-Chat-Demo)
- **Alibaba Cloud API:** [DashScope Multimodal Service](https://dashscope.aliyun.com/)

### Benchmarks & Evaluations
- Benchmarks: VQAv2, GQA, TextVQA, DocVQA, ChartQA, OCRVQA, RefCOCO
- State-of-the-art performance on Chinese VL benchmarks
- See [arXiv paper](https://arxiv.org/abs/2308.12966) for detailed benchmark results

## Papers

| Paper | arXiv ID | Local PDF |
|-------|----------|-----------|
| Qwen-VL: A Versatile Vision-Language Model | [2308.12966](https://arxiv.org/abs/2308.12966) | [Qwen-VL_2308.12966.pdf](Qwen-VL_2308.12966.pdf) |
