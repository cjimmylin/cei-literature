# DeepSeek Janus

## Overview
Janus is DeepSeek's series of unified multimodal models that excel at both visual understanding and image generation. The key innovation is decoupling visual encoding into separate pathways while maintaining a single unified transformer architecture.

## Model Versions

### Janus (October 2024)
- **arXiv:** 2410.13848
- **Release Date:** October 2024
- **Key Features:**
  - Decoupled visual encoding for understanding vs. generation
  - Single unified transformer architecture
  - Superior performance on both tasks vs. previous unified models
- **Model Sizes:** 1.3B parameters

### JanusFlow (November 2024)
- **arXiv:** 2411.07975
- **Release Date:** November 13, 2024
- **Key Features:**
  - Harmonizes autoregressive LLMs with rectified flow
  - Native rectified flow training within LLM framework
  - No complex architectural modifications needed
- **Performance:**
  - Understanding: 74.9 MMBench, 70.5 SeedBench, 60.3 GQA
  - Generation: 9.51 MJHQ FID-30k, 0.63 GenEval
- **Model Sizes:** 1.3B parameters (based on DeepSeek-LLM)

### Janus-Pro (January 2025)
- **arXiv:** 2501.17811
- **Release Date:** January 27, 2025
- **Key Features:**
  - Optimized training strategy
  - Expanded training data
  - Scaled to larger model sizes
  - Enhanced multimodal understanding and generation
- **Model Sizes:** 1B, 7B parameters

## Research Papers

All papers are available in this directory:
- `Janus_arxiv_2410.13848.pdf` - Original Janus paper
- `JanusFlow_arxiv_2411.07975.pdf` - JanusFlow with rectified flow
- `Janus-Pro_arxiv_2501.17811.pdf` - Latest scaled-up version

## Key Innovations

1. **Decoupled Visual Encoding:** Separate encoders for understanding and generation tasks, eliminating the conflict between these roles
2. **Rectified Flow Integration:** JanusFlow seamlessly integrates state-of-the-art generative modeling within the LLM framework
3. **Unified Architecture:** Single transformer processes both modalities without task-specific architectural changes
4. **Scalability:** Janus-Pro demonstrates the approach scales effectively to larger models

## Links

- **GitHub:** [github.com/deepseek-ai/Janus](https://github.com/deepseek-ai/Janus)
- **Hugging Face:** [deepseek-ai Janus models](https://huggingface.co/deepseek-ai)
- **License:** MIT License (code), DeepSeek Model License (models)
