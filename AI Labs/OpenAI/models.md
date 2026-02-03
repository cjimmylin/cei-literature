# OpenAI Models

| Release Year | Model Name | Version | Description | Blog | Paper | Model Card | API Docs | Local PDF |
|--------------|------------|---------|-------------|------|-------|------------|----------|-----------|
| 2018 | [[GPT-1/README.md\|GPT-1]] | 1.0 | Improving Language Understanding by Generative Pre-Training. First iteration of the GPT series. | [Blog](https://openai.com/blog/language-unsupervised/) | [Paper](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf) | - | - | [PDF](GPT-1/gpt-1-improving-language-understanding.pdf) |
| 2019 | [[GPT-2/README.md\|GPT-2]] | 1.0 | Language Models are Unsupervised Multitask Learners. Introduced the 1.5B parameter model. | [Blog](https://openai.com/blog/better-language-models/) | [Paper](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) | [GitHub](https://github.com/openai/gpt-2/blob/master/model_card.md) | - | [PDF](GPT-2/gpt-2-language-models-unsupervised-multitask-learners.pdf) |
| 2020 | [[GPT-3/README.md\|GPT-3]] | 1.0 | Language Models are Few-Shot Learners. 175B parameters, foundational for modern LLMs. | [Blog](https://openai.com/blog/openai-api/) | [arXiv](https://arxiv.org/abs/2005.14165) | [GitHub](https://github.com/openai/gpt-3/blob/master/model-card.md) | [Docs](https://platform.openai.com/docs/models/gpt-base) | [PDF](GPT-3/gpt-3-language-models-few-shot-learners.pdf) |
| 2021 | [[DALL-E/README.md\|DALL-E]] | 1.0-3.0 | Creating Images from Text. Zero-shot text-to-image generation. | [Blog](https://openai.com/blog/dall-e/) | [arXiv](https://arxiv.org/abs/2102.12092) | [System Card](https://openai.com/index/dall-e-3-system-card/) | [Docs](https://platform.openai.com/docs/guides/images) | [PDF](DALL-E/dall-e-creating-images-from-text.pdf) |
| 2022 | [[GPT-3.5/README.md\|GPT-3.5]] | Turbo | Optimized for chat and dialog. Powers the initial version of ChatGPT. | [Blog](https://openai.com/blog/chatgpt/) | - | [Fine-tuning](https://openai.com/index/gpt-3-5-turbo-fine-tuning-and-api-updates/) | [Docs](https://platform.openai.com/docs/models/gpt-3-5-turbo) | - |
| 2022 | [[InstructGPT/README.md\|InstructGPT]] | - | Training language models to follow instructions with human feedback (RLHF). | [Blog](https://openai.com/blog/instruction-following/) | [arXiv](https://arxiv.org/abs/2203.02155) | - | - | [PDF](InstructGPT/instructgpt-training-language-models-to-follow-instructions.pdf) |
| 2022 | [[Whisper/README.md\|Whisper]] | 1.0 | Robust Speech Recognition via Large-Scale Weak Supervision. | [Blog](https://openai.com/blog/whisper/) | [arXiv](https://arxiv.org/abs/2212.04356) | [GitHub](https://github.com/openai/whisper/blob/main/model-card.md) | [Docs](https://platform.openai.com/docs/guides/speech-to-text) | [PDF](Whisper/whisper-robust-speech-recognition.pdf) |
| 2023 | [[GPT-4/README.md\|GPT-4]] | 1.0 | Large-scale multimodal model with improved reasoning and reliability. | [Blog](https://openai.com/blog/gpt-4/) | [Paper](https://cdn.openai.com/papers/gpt-4.pdf) | [System Card](https://cdn.openai.com/papers/gpt-4-system-card.pdf) | [Docs](https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo) | [PDF](GPT-4/gpt-4-technical-report.pdf) |
| 2023 | [[GPT-4 Turbo/README.md\|GPT-4 Turbo]] | 2023-11-06 | Updated model with 128k context and knowledge cutoff in April 2023. | [Blog](https://openai.com/blog/new-models-and-developer-products-announced-at-devday/) | - | - | [Docs](https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo) | - |
| 2024 | [[Sora/README.md\|Sora]] | Preview | Text-to-video generation model capable of generating highly realistic scenes. | [Blog](https://openai.com/sora/) | [Report](https://openai.com/index/video-generation-models-as-world-simulators/) | - | - | - |
| 2024 | [[GPT-4o/README.md\|GPT-4o]] | 1.0 | Omnimodel supporting real-time text, audio, and vision interactions. | [Blog](https://openai.com/index/hello-gpt-4o/) | - | [System Card](https://openai.com/index/gpt-4o-system-card/) | [Docs](https://platform.openai.com/docs/models/gpt-4o) | [PDF](GPT-4o/gpt-4o-system-card.pdf) |
| 2024 | [[o1/README.md\|o1]] | Preview | New reasoning models trained with reinforcement learning for complex tasks. | [Blog](https://openai.com/index/learning-to-reason-with-llms/) | - | [System Card](https://openai.com/index/openai-o1-system-card/) | [Docs](https://platform.openai.com/docs/models/o1) | [PDF](o1/o1-system-card.pdf) |
| 2025 | [[o3/README.md\|o3]] | - | Frontier reasoning model with world-class performance in math and coding. | [Blog](https://openai.com/index/deliberative-alignment/) | - | [System Card](https://openai.com/index/openai-o3-system-card/) | [Docs](https://platform.openai.com/docs/models/o3) | - |
| 2025 | [[o3-mini/README.md\|o3-mini]] | - | Cost-efficient model for advanced reasoning and low-latency applications. | [Blog](https://openai.com/index/openai-o3-mini/) | - | - | [Docs](https://platform.openai.com/docs/models/o3-mini) | - |

## Foundational Papers

See [Papers/README.md](Papers/README.md) for additional foundational research papers including:
- Scaling Laws for Neural Language Models
- CLIP (Contrastive Language-Image Pre-training)
- Codex (Code generation)
- GLIDE (Image generation)
- Jukebox (Music generation)
- Point-E (3D generation)
- WebGPT (Browser-assisted QA)
- Constitutional AI
- Direct Preference Optimization (DPO)
- GPT-4V System Card
