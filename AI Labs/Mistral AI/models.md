# Mistral AI Models

| Release Year | Model Name | Version | Description | Description URL | Link to Paper | Link to Model Card |
|--------------|------------|---------|-------------|-----------------|---------------|-------------------|
| 2023 | [[Mistral 7B/README.md|Mistral 7B]] | 0.1 | 7.3B parameter model outperforming Llama 2 13B. Apache 2.0. | [Blog](https://mistral.ai/news/announcing-mistral-7b/) | [arXiv](https://arxiv.org/abs/2310.06825) | [HuggingFace](https://huggingface.co/mistralai/Mistral-7B-v0.1) |
| 2023 | [[Mixtral 8x7B/README.md|Mixtral 8x7B]] | 0.1 | Sparse Mixture of Experts model, state-of-the-art open weights. | [Blog](https://mistral.ai/news/mixtral-of-experts/) | [arXiv](https://arxiv.org/abs/2401.04088) | [HuggingFace](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1) |
| 2024 | [[Mistral Large/README.md|Mistral Large]] | 1.0 | Closed-weight flagship model for high-complexity reasoning. | [Blog](https://mistral.ai/news/mistral-large/) | - | - |
| 2024 | [[Mixtral 8x22B/README.md|Mixtral 8x22B]] | 0.1 | Larger MoE model with 141B total parameters, 39B active. | [Blog](https://mistral.ai/news/mixtral-8x22b/) | - | [HuggingFace](https://huggingface.co/mistralai/Mixtral-8x22B-v0.1) |
| 2024 | [[Codestral/README.md|Codestral]] | 22B | Open-weight generative model tailored for code-centric tasks. | [Blog](https://mistral.ai/news/codestral/) | - | [HuggingFace](https://huggingface.co/mistralai/Codestral-22B-v0.1) |
| 2024 | [[Mistral NeMo/README.md|Mistral NeMo]] | 12B | Small model designed for high performance and efficiency, co-developed with NVIDIA. | [Blog](https://mistral.ai/news/mistral-nemo/) | - | [HuggingFace](https://huggingface.co/mistralai/Mistral-Nemo-Base-2407) |
| 2024 | [[Mistral Large 2/README.md|Mistral Large 2]] | 24.07 | Frontier-class model with 123B parameters, rivaling GPT-4o. | [Blog](https://mistral.ai/news/mistral-large-2407/) | - | [HuggingFace](https://huggingface.co/mistralai/Mistral-Large-Instruct-2407) |
| 2024 | [[Mathstral/README.md|Mathstral]] | 7B | Specialized model for STEM subjects and mathematical reasoning. | [Blog](https://mistral.ai/news/mathstral) | - | [HuggingFace](https://huggingface.co/mistralai/mathstral-7B-v0.1) |
| 2024 | [[Pixtral 12B/README.md|Pixtral 12B]] | 24.09 | Mistral's first multimodal model for vision and text. | [Blog](https://mistral.ai/news/pixtral-12b/) | [arXiv](https://arxiv.org/abs/2410.07073) | [HuggingFace](https://huggingface.co/mistralai/Pixtral-12B-2409) |
| 2025 | [[Mistral Small/README.md|Mistral Small]] | 3.x | Updated compact model family (24B) for diverse generative tasks. | [Blog](https://mistral.ai/news/mistral-small-3/) | - | [HuggingFace](https://huggingface.co/mistralai/Mistral-Small-Instruct-2409) |
| 2025 | [[Mistral Medium/README.md|Mistral Medium]] | 3.x | Balanced enterprise model with multimodal and 128k context support. | [Blog](https://mistral.ai/news/mistral-medium-3/) | - | - |
| 2025 | [[Magistral/README.md|Magistral]] | Small: 24B, Medium: TBD | First reasoning model with transparent multi-step logic and RL pipeline. | [Blog](https://mistral.ai/news/magistral) | [arXiv](https://arxiv.org/abs/2506.10910) | [HuggingFace](https://huggingface.co/mistralai/Magistral-Small-2506) |
| 2026 | [[Ministral 3B/README.md|Ministral 3B]] | 3B | Parameter-efficient model family (3B/8B/14B) with image understanding. | - | [arXiv](https://arxiv.org/abs/2601.08584) | [HuggingFace](https://huggingface.co/collections/mistralai/ministral) |

---

## Documentation & Resources

### Official Platforms
| Platform | URL | Description |
|----------|-----|-------------|
| **La Plateforme** | [console.mistral.ai](https://console.mistral.ai/) | API access and management console |
| **Le Chat** | [chat.mistral.ai](https://chat.mistral.ai/) | Interactive playground for all models |
| **Documentation** | [docs.mistral.ai](https://docs.mistral.ai/) | Official documentation hub |
| **API Reference** | [docs.mistral.ai/api](https://docs.mistral.ai/api/) | API endpoints and specifications |
| **News & Blog** | [mistral.ai/news](https://mistral.ai/news/) | Official announcements and releases |

### GitHub Repositories
| Repository | URL | Description |
|------------|-----|-------------|
| **mistral-inference** | [github.com/mistralai/mistral-inference](https://github.com/mistralai/mistral-inference) | Official inference library |
| **mistral-common** | [github.com/mistralai/mistral-common](https://github.com/mistralai/mistral-common) | Common utilities and tokenizers |
| **mistral-finetune** | [github.com/mistralai/mistral-finetune](https://github.com/mistralai/mistral-finetune) | Fine-tuning toolkit |
| **client-python** | [github.com/mistralai/client-python](https://github.com/mistralai/client-python) | Python API client |
| **client-js** | [github.com/mistralai/client-js](https://github.com/mistralai/client-js) | JavaScript API client |

### HuggingFace
| Resource | URL |
|----------|-----|
| **Organization** | [huggingface.co/mistralai](https://huggingface.co/mistralai) |
| **All Models (65+)** | [huggingface.co/mistralai/models](https://huggingface.co/models?author=mistralai) |

### Capability Guides
| Guide | URL |
|-------|-----|
| Code Generation | [docs.mistral.ai/capabilities/code_generation](https://docs.mistral.ai/capabilities/code_generation/) |
| Vision | [docs.mistral.ai/capabilities/vision](https://docs.mistral.ai/capabilities/vision/) |
| Function Calling | [docs.mistral.ai/capabilities/function_calling](https://docs.mistral.ai/capabilities/function_calling/) |
| JSON Mode | [docs.mistral.ai/capabilities/json_mode](https://docs.mistral.ai/capabilities/json_mode/) |
| Embeddings | [docs.mistral.ai/capabilities/embeddings](https://docs.mistral.ai/capabilities/embeddings/) |

### Third-Party Integrations
| Integration | URL | Description |
|-------------|-----|-------------|
| vLLM | [github.com/vllm-project/vllm](https://github.com/vllm-project/vllm) | High-throughput inference engine |
| NVIDIA NeMo | [github.com/NVIDIA/NeMo](https://github.com/NVIDIA/NeMo) | NVIDIA's AI framework |
| LangChain | [python.langchain.com](https://python.langchain.com/) | LLM application framework |
| LlamaIndex | [llamaindex.ai](https://www.llamaindex.ai/) | Data framework for LLM apps |
