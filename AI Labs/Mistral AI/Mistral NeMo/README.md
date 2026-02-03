# Mistral NeMo

## Overview
12B parameter model designed for high performance and efficiency, co-developed with NVIDIA. Designed to fit on a single consumer GPU. Drop-in replacement for Mistral 7B with improved capabilities.

## Technical Specifications
- **Release Year:** 2024
- **Parameters:** 12B
- **Layers:** 40
- **Context Window:** 128k tokens
- **Vocabulary Size:** ~128k (2^17)
- **Activation Function:** SwiGLU
- **Attention:** GQA (Grouped Query Attention)
- **License:** Apache 2.0
- **Multilingual:** 9 languages supported

## Documentation & Links

### Official Resources
| Resource | Link |
|----------|------|
| Blog Announcement | [Mistral NeMo](https://mistral.ai/news/mistral-nemo/) |
| Documentation | [docs.mistral.ai](https://docs.mistral.ai/) |

### HuggingFace Models
| Model | Link |
|-------|------|
| Base Model | [mistralai/Mistral-Nemo-Base-2407](https://huggingface.co/mistralai/Mistral-Nemo-Base-2407) |
| Instruct Model | [mistralai/Mistral-Nemo-Instruct-2407](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407) |
| NVIDIA Version | [nvidia/Mistral-NeMo-12B-Base](https://huggingface.co/nvidia/Mistral-NeMo-12B-Base) |

### GitHub Repositories
| Repository | Description |
|------------|-------------|
| [mistralai/mistral-inference](https://github.com/mistralai/mistral-inference) | Official inference library |
| [mistralai/mistral-common](https://github.com/mistralai/mistral-common) | Common utilities and tokenizers |
| [NVIDIA/NeMo](https://github.com/NVIDIA/NeMo) | NVIDIA NeMo framework |

### API & Playground
| Service | Link |
|---------|------|
| La Plateforme API | [console.mistral.ai](https://console.mistral.ai/) |
| Le Chat Playground | [chat.mistral.ai](https://chat.mistral.ai/) |
| API Documentation | [docs.mistral.ai/api](https://docs.mistral.ai/api/) |

## Notes
- Recommended temperature: 0.3 (lower than previous Mistral models)
- Co-developed with NVIDIA for optimal performance
