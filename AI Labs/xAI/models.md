# xAI Models

> **Note:** xAI has not published official technical papers for their Grok models. See [[Papers/DOCUMENTATION_STATUS|Documentation Status]] for details.

| Release Year | Model Name | Version | Description | Description URL | Link to Paper | Link to Model Card |
|--------------|------------|---------|-------------|-----------------|---------------|-------------------|
| 2023 | [[Grok-1/README.md|Grok-1]] | 1.0 | 314B parameter MoE model, open-sourced with a focus on real-time knowledge. | [Blog](https://x.ai/blog/grok-os) | [GitHub](https://github.com/xai-org/grok-1) | [HuggingFace](https://huggingface.co/xai-org/grok-1) |
| 2024 | [[Grok-1.5/README.md|Grok-1.5]] | 1.5 | Improved reasoning and 128k context window. | [Blog](https://x.ai/blog/grok-1.5) | - | - |
| 2024 | [[Grok-1.5V/README.md|Grok-1.5V]] | Preview | xAI's first multimodal model capable of processing vision data. | [Blog](https://x.ai/blog/grok-1.5v) | - | - |
| 2024 | [[Grok-2/README.md|Grok-2]] | 2.0 | State-of-the-art reasoning and introduction of image generation on X. | [Blog](https://x.ai/blog/grok-2) | - | - |
| 2025 | [[Grok-3/README.md|Grok-3]] | 3.0 | Trained on 10x more compute, features DeepSearch and "Think" mode. | [Blog](https://x.ai/blog/grok-3) | - | [Model Card](https://x.ai/model-card/grok-3) |
| 2025 | [[Grok-4/README.md|Grok-4]] | 4.0 | Advanced agentic capabilities with 256k context and SuperGrok Heavy tier. | [Blog](https://x.ai/blog/grok-4) | - | - |
| 2025 | [[Grok 4.1 Fast/README.md|Grok 4.1 Fast]] | 4.1 | Optimized reasoning model with 2M context window and top-tier tool calling. | [Blog](https://x.ai/blog/grok-4-1-fast) | - | - |
| 2025 | [[Grok Code Fast/README.md|Grok Code Fast]] | 1.0 | Specialized fast reasoning model for agentic coding applications. | [Blog](https://x.ai/blog/grok-code-fast) | - | [Model Card](https://x.ai/model-card/grok-code-fast-1) |

## Technical Documentation

The only model with publicly available architecture details is Grok-1:

| Specification | Value |
|--------------|-------|
| Parameters | 314B |
| Architecture | Mixture of 8 Experts (MoE) |
| Experts per Token | 2 |
| Layers | 64 |
| Attention Heads | 48 queries, 8 keys/values |
| Embedding Size | 6,144 |
| Tokenizer | SentencePiece (131,072 tokens) |
| Context Length | 8,192 tokens |
| License | Apache 2.0 |

## Documentation Links

### Official Resources
| Resource | Link |
|----------|------|
| Official Website | [x.ai](https://x.ai) |
| Blog | [x.ai/blog](https://x.ai/blog) |
| API Documentation | [docs.x.ai](https://docs.x.ai) |
| API Console | [console.x.ai](https://console.x.ai) |
| X/Twitter | [@xai](https://x.com/xai) |

### GitHub & HuggingFace
| Resource | Link |
|----------|------|
| GitHub Organization | [github.com/xai-org](https://github.com/xai-org) |
| Grok-1 Repository | [github.com/xai-org/grok-1](https://github.com/xai-org/grok-1) |
| HuggingFace Organization | [huggingface.co/xai-org](https://huggingface.co/xai-org) |
| Grok-1 Model | [huggingface.co/xai-org/grok-1](https://huggingface.co/xai-org/grok-1) |
| Grok-2 Model | [huggingface.co/xai-org/grok-2](https://huggingface.co/xai-org/grok-2) |
| RealWorldQA Dataset | [huggingface.co/datasets/xai-org/RealworldQA](https://huggingface.co/datasets/xai-org/RealworldQA) |

### Model Cards
| Model | Model Card |
|-------|------------|
| Grok-3 | [x.ai/model-card/grok-3](https://x.ai/model-card/grok-3) |
| Grok Code Fast | [x.ai/model-card/grok-code-fast-1](https://x.ai/model-card/grok-code-fast-1) |

### Blog Announcements
| Model | Blog Post |
|-------|-----------|
| Grok-1 Open Source | [x.ai/blog/grok-os](https://x.ai/blog/grok-os) |
| Grok-1.5 | [x.ai/blog/grok-1.5](https://x.ai/blog/grok-1.5) |
| Grok-1.5V | [x.ai/blog/grok-1.5v](https://x.ai/blog/grok-1.5v) |
| Grok-2 | [x.ai/blog/grok-2](https://x.ai/blog/grok-2) |
| Grok-3 | [x.ai/blog/grok-3](https://x.ai/blog/grok-3) |
