# Pixtral 12B

## Overview
Mistral's first multimodal model, capable of processing both image and text inputs with high efficiency. Natively multimodal with interleaved image and text data, supporting variable image sizes.

## Technical Specifications
- **Release Year:** 2024
- **Version:** 24.09
- **Parameters:** 12B Multimodal Decoder + 400M Vision Encoder
- **Context Window:** 128k tokens
- **License:** Apache 2.0
- **Format:** Safetensors

## Documentation & Links

### Official Resources
| Resource | Link |
|----------|------|
| Blog Announcement | [Pixtral 12B](https://mistral.ai/news/pixtral-12b/) |
| Research Paper | [arXiv:2410.07073](https://arxiv.org/abs/2410.07073) |
| Documentation | [docs.mistral.ai](https://docs.mistral.ai/) |
| Vision Capabilities | [docs.mistral.ai/capabilities/vision](https://docs.mistral.ai/capabilities/vision/) |

### HuggingFace Models
| Model | Link |
|-------|------|
| Instruct Model | [mistralai/Pixtral-12B-2409](https://huggingface.co/mistralai/Pixtral-12B-2409) |
| Base Model | [mistralai/Pixtral-12B-Base-2409](https://huggingface.co/mistralai/Pixtral-12B-Base-2409) |

### GitHub Repositories
| Repository | Description |
|------------|-------------|
| [mistralai/mistral-inference](https://github.com/mistralai/mistral-inference) | Official inference library |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | Optimized inference (recommended) |
| [Pixtral vLLM Example](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference_pixtral.py) | Usage examples |

### API & Playground
| Service | Link |
|---------|------|
| La Plateforme API | [console.mistral.ai](https://console.mistral.ai/) |
| Le Chat Playground | [chat.mistral.ai](https://chat.mistral.ai/) |
| API Documentation | [docs.mistral.ai/api](https://docs.mistral.ai/api/) |

## Papers

| Title | Authors | Date | arXiv | PDF |
|-------|---------|------|-------|-----|
| Pixtral 12B | Garg et al. | Oct 2024 | [2410.07073](https://arxiv.org/abs/2410.07073) | [Pixtral_12B_arxiv_2410.07073.pdf](Pixtral_12B_arxiv_2410.07073.pdf) |

## Installation
```bash
pip install --upgrade vllm mistral_common>=1.4.4
```
