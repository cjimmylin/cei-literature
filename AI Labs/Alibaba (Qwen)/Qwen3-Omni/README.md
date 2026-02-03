# Qwen3-Omni

## Overview
Qwen3-Omni is a natively end-to-end, omni-modal LLM developed by the Qwen team at Alibaba Cloud, capable of understanding text, audio, images, and video, as well as generating speech in real time. It is the first multimodal model that maintains state-of-the-art performance across all modalities without degradation.

## Technical Specifications
- **Release Year:** 2025
- **Version:** 3.0
- **Parameters:** 30B-A3B (Mixture-of-Experts)
- **Architecture:** Thinker-Talker MoE architecture
- **Language Support:**
  - Text: 119 languages
  - Speech Understanding: 19 languages
  - Speech Generation: 10 languages
- **Latency:** 234ms theoretical end-to-end first-packet latency (cold-start)

## Key Capabilities
- **Unified Multimodal Architecture:** Single model for text, image, audio, and video understanding and generation
- **Real-Time Speech:** Natural speech generation with streaming output
- **SOTA Performance:** Open-source SOTA on 32 out of 36 audio and audio-visual benchmarks
- **Competitive with Closed Models:** Outperforms Gemini-2.5-Pro, Seed-ASR, and GPT-4o-Transcribe on 22 benchmarks

## Documentation & Links

### Official Resources
- **Technical Report:** [arXiv:2509.17765](https://arxiv.org/abs/2509.17765)
- **Blog Post:** [Qwen3-Omni Announcement](https://qwen.ai/blog)

### GitHub Repositories
- **Main Repository:** [github.com/QwenLM/Qwen3-Omni](https://github.com/QwenLM/Qwen3-Omni)

### HuggingFace Models
| Model | HuggingFace Link |
|-------|------------------|
| Qwen3-Omni-30B-A3B | [huggingface.co/Qwen/Qwen3-Omni-30B-A3B](https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B) |
| Qwen3-Omni-30B-A3B-Thinking | [huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Thinking](https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Thinking) |
| Qwen3-Omni-30B-A3B-Captioner | [huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Captioner](https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Captioner) |

### Demo & API
- **Qwen Chat:** [chat.qwenlm.ai](https://chat.qwenlm.ai/)
- **Alibaba Cloud API:** [DashScope](https://dashscope.aliyun.com/)

## Papers

| Paper | arXiv ID | Local PDF |
|-------|----------|-----------|
| Qwen3-Omni Technical Report | [2509.17765](https://arxiv.org/abs/2509.17765) | [Qwen3-Omni_Technical_Report_2509.17765.pdf](Qwen3-Omni_Technical_Report_2509.17765.pdf) |

## License
Released under Apache 2.0 license.
