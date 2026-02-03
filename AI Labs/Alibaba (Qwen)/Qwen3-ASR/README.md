# Qwen3-ASR

## Overview
Qwen3-ASR is an open-source series of automatic speech recognition models developed by the Qwen team at Alibaba Cloud. It supports stable multilingual speech/music/song recognition, language detection, and timestamp prediction.

## Technical Specifications
- **Release Year:** 2026
- **Version:** 3.0
- **Parameters:** 0.6B, 1.7B
- **Language Support:** 52 languages and dialects
- **Foundation Model:** Based on Qwen3-Omni

## Key Capabilities
- **Multilingual ASR:** 52 languages and dialects
- **Language Identification:** Automatic language detection
- **Timestamp Prediction:** Precise alignment of text and speech
- **SOTA Performance:**
  - Qwen3-ASR-1.7B achieves SOTA among open-source ASR models
  - Competitive with strongest proprietary APIs
- **Low Latency:**
  - Qwen3-ASR-0.6B: 92ms average TTFT (Time To First Token)
  - Can transcribe 2000 seconds of speech in 1 second at concurrency of 128

## Additional Models
- **Qwen3-ForcedAligner-0.6B:** LLM-based non-autoregressive timestamp predictor for text-speech alignment in 11 languages. Outperforms three strongest force alignment models.

## Documentation & Links

### Official Resources
- **Technical Report:** [arXiv:2601.21337](https://arxiv.org/abs/2601.21337)
- **Blog Post:** [Qwen3-ASR Announcement](https://qwen.ai/blog?id=41e4c0f6175f9b004a03a07e42343eaaf48329e7)

### GitHub Repositories
- **Main Repository:** [github.com/QwenLM/Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR)

### HuggingFace Models
| Model | HuggingFace Link |
|-------|------------------|
| Qwen3-ASR-1.7B | [huggingface.co/Qwen/Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) |
| Qwen3-ASR-0.6B | [huggingface.co/Qwen/Qwen3-ASR-0.6B](https://huggingface.co/Qwen/Qwen3-ASR-0.6B) |
| Qwen3-ForcedAligner-0.6B | [huggingface.co/Qwen/Qwen3-ForcedAligner-0.6B](https://huggingface.co/Qwen/Qwen3-ForcedAligner-0.6B) |

### Demo & API
- **Qwen Chat:** [chat.qwenlm.ai](https://chat.qwenlm.ai/)
- **Alibaba Cloud API:** [DashScope](https://dashscope.aliyun.com/)

## Papers

| Paper | arXiv ID | Local PDF |
|-------|----------|-----------|
| Qwen3-ASR Technical Report | [2601.21337](https://arxiv.org/abs/2601.21337) | [Qwen3-ASR_Technical_Report_2601.21337.pdf](Qwen3-ASR_Technical_Report_2601.21337.pdf) |

## License
Released under Apache 2.0 license.
