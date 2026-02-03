# Qwen2.5-Omni

## Overview
End-to-end multimodal model for perceiving text, images, audio, and video while generating text and natural speech responses in streaming manner.

## Technical Specifications
- **Release Year:** 2025
- **Version:** 2.5
- **Parameters:** 7B
- **Architecture:** Thinker-Talker architecture with TMRoPE (Time-aligned Multimodal RoPE)
- **Input Types:** Text, images, audio, video
- **Output Types:** Text, natural speech (streaming)
- **Key Innovation:** Block-wise multimodal processing, sliding-window DiT for streaming audio

## Documentation & Links

### Official Resources
- **Blog Post:** [Qwen2.5-Omni: Official Announcement](https://qwenlm.github.io/blog/qwen2.5-omni/)
- **Technical Report:** [arXiv:2503.20215](https://arxiv.org/abs/2503.20215)

### GitHub Repositories
- **Main Repository:** [github.com/QwenLM/Qwen2.5-Omni](https://github.com/QwenLM/Qwen2.5-Omni)

### HuggingFace Models
| Model | HuggingFace Link |
|-------|------------------|
| Qwen2.5-Omni-7B | [huggingface.co/Qwen/Qwen2.5-Omni-7B](https://huggingface.co/Qwen/Qwen2.5-Omni-7B) |

### Demo & API
- **Qwen Chat:** [chat.qwenlm.ai](https://chat.qwenlm.ai/)
- **Alibaba Cloud API:** [DashScope](https://dashscope.aliyun.com/)

### Key Features
- **Thinker-Talker Architecture:** Separate modules for text generation and speech synthesis
- **TMRoPE:** Time-aligned Multimodal Rotary Position Embedding
- **Streaming Output:** Real-time text and speech generation
- **End-to-End:** Single model for multimodal understanding and generation

### Benchmarks
- Omni-Bench: SOTA on multimodal benchmarks
- Speech instruction following comparable to text input performance (MMLU, GSM8K)
- Streaming speech generation with high robustness and naturalness

## Papers

| Paper | arXiv ID | Local PDF |
|-------|----------|-----------|
| Qwen2.5-Omni Technical Report | [2503.20215](https://arxiv.org/abs/2503.20215) | [Qwen2.5-Omni_Technical_Report_2503.20215.pdf](Qwen2.5-Omni_Technical_Report_2503.20215.pdf) |
