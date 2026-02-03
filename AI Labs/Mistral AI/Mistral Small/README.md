# Mistral Small

## Overview
Updated compact model family (24B) optimized for low-latency generative tasks and cost-effective deployment. Designed for enterprise applications requiring a balance of performance and efficiency.

## Technical Specifications
- **Release Year:** 2025
- **Version:** 3.x
- **Parameters:** 22-24B
- **Context Window:** 32k tokens
- **Vocabulary Size:** 32,768
- **License:** MRL (Mistral Research License)
- **Features:** Function calling support

## Documentation & Links

### Official Resources
| Resource | Link |
|----------|------|
| Blog Announcement (v3) | [Mistral Small 3](https://mistral.ai/news/mistral-small-3/) |
| Documentation | [docs.mistral.ai](https://docs.mistral.ai/) |
| Model Overview | [docs.mistral.ai/getting-started/models](https://docs.mistral.ai/getting-started/models/) |

### HuggingFace Models
| Model | Link |
|-------|------|
| Instruct v2409 | [mistralai/Mistral-Small-Instruct-2409](https://huggingface.co/mistralai/Mistral-Small-Instruct-2409) |
| Base v2409 | [mistralai/Mistral-Small-Base-2409](https://huggingface.co/mistralai/Mistral-Small-Base-2409) |

### GitHub Repositories
| Repository | Description |
|------------|-------------|
| [mistralai/mistral-inference](https://github.com/mistralai/mistral-inference) | Official inference library |
| [mistralai/client-python](https://github.com/mistralai/client-python) | Python API client |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | Optimized inference engine |

### API & Playground
| Service | Link |
|---------|------|
| La Plateforme API | [console.mistral.ai](https://console.mistral.ai/) |
| Le Chat Playground | [chat.mistral.ai](https://chat.mistral.ai/) |
| API Documentation | [docs.mistral.ai/api](https://docs.mistral.ai/api/) |

## Dependencies
- vLLM >= v0.6.1.post1
- mistral_common >= 1.4.1
- Hugging Face transformers
