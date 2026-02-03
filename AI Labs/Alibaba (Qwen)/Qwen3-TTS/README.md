# Qwen3-TTS

## Overview
Qwen3-TTS is an open-source series of text-to-speech models developed by the Qwen team at Alibaba Cloud. It supports stable, expressive, and streaming speech generation, free-form voice design, and vivid voice cloning.

## Technical Specifications
- **Release Year:** 2026
- **Version:** 3.0
- **Parameters:** 0.6B, 1.7B
- **Language Support:** 10 languages
- **Training Data:** Over 5 million hours of speech data
- **Architecture:** Dual-track LM architecture with two speech tokenizers

## Key Capabilities
- **Voice Cloning:** State-of-the-art 3-second voice cloning
- **Description-Based Control:** Create entirely novel voices from text descriptions
- **Fine-Grained Manipulation:** Precise control over output speech characteristics
- **Real-Time Synthesis:** Streaming speech generation for low-latency applications
- **Multilingual:** Supports 10 languages

## Documentation & Links

### Official Resources
- **Technical Report:** [arXiv:2601.15621](https://arxiv.org/abs/2601.15621)
- **Blog Post:** [Qwen3-TTS Announcement](https://qwen.ai/blog)

### GitHub Repositories
- **Main Repository:** [github.com/QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS)

### HuggingFace Models
| Model | HuggingFace Link |
|-------|------------------|
| Qwen3-TTS-12Hz-1.7B-Base | [huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base) |
| Qwen3-TTS-12Hz-1.7B-CustomVoice | [huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice) |
| Qwen3-TTS-12Hz-0.6B-Base | [huggingface.co/Qwen/Qwen3-TTS-12Hz-0.6B-Base](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-0.6B-Base) |

### Demo & API
- **Qwen Chat:** [chat.qwenlm.ai](https://chat.qwenlm.ai/)
- **Alibaba Cloud API:** [DashScope](https://dashscope.aliyun.com/)

## Papers

| Paper | arXiv ID | Local PDF |
|-------|----------|-----------|
| Qwen3-TTS Technical Report | [2601.15621](https://arxiv.org/abs/2601.15621) | [Qwen3-TTS_Technical_Report_2601.15621.pdf](Qwen3-TTS_Technical_Report_2601.15621.pdf) |

## License
Both tokenizers and models are released under Apache 2.0 license.
