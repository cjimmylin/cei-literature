# Yi-VL

## Overview
Multimodal vision-language extension of the Yi family, capable of image captioning and visual question answering. Yi-VL-34B is the first open-source 34B vision-language model worldwide and ranks #1 among all open-source models on MMMU and CMMMU benchmarks.

## Technical Specifications
- **Release Year:** 2024
- **Release Date:** January 23, 2024
- **Model Variants:** 34B and 6B
- **Architecture:** LLaVA-based (ViT + Projection + LLM)
- **Vision Encoder:** CLIP ViT-H/14
- **Input Resolution:** 448×448
- **Bilingual Support:** English and Chinese
- **License:** Apache 2.0

## Documentation

**Comprehensive Technical Documentation:** [Yi-VL_Documentation.md](Yi-VL_Documentation.md)
- Complete architecture details
- Three-stage training methodology
- Training datasets and resources
- Benchmark results
- Usage examples
- Known limitations

## Papers

| Paper | arXiv ID | Date | Local PDF |
|-------|----------|------|-----------|
| Yi: Open Foundation Models by 01.AI | [2403.04652](https://arxiv.org/abs/2403.04652) | 2024-03-07 | [PDF](../Papers/Yi_Technical_Report_2403.04652.pdf) |

Note: Yi-VL is documented in the main Yi Technical Report. No separate publication exists.

## Links
- [Official Blog](https://01.ai/blog/yi-vl)
- [Research Paper](https://arxiv.org/abs/2403.04652)
- [Model Card](https://huggingface.co/01-ai/Yi-VL-34B)

## Documentation & Links

### GitHub
- [01-ai/Yi](https://github.com/01-ai/Yi) - Main repository (includes Yi-VL)

### HuggingFace Models
| Variant | Model Link |
|---------|------------|
| 34B | [Yi-VL-34B](https://huggingface.co/01-ai/Yi-VL-34B) |
| 6B | [Yi-VL-6B](https://huggingface.co/01-ai/Yi-VL-6B) |

### Benchmarks & Demos
- Evaluated on VQAv2, GQA, TextVQA, and other vision-language benchmarks
- See [Yi Technical Report](https://arxiv.org/abs/2403.04652) Section 5 for multimodal evaluation
