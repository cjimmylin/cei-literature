# DeepSeek-V3

## Overview
671B parameter MoE model with world-class reasoning and coding performance. Features Multi-head Latent Attention (MLA) and DeepSeekMoE architecture. Trained on 14.8 trillion tokens using 2.788M H800 GPU hours.

## Technical Specifications
- **Release Year:** 2024
- **Version:** 3.0
- **Parameters:** 671B total, 37B active per token (685B on HuggingFace including 14B Multi-Token Prediction module)
- **Context Window:** 128K tokens
- **Architecture:** MoE with MLA (Multi-head Latent Attention)
- **Training Cost:** 2.788M H800 GPU hours
- **Pre-training Tokens:** 14.8 trillion
- **License:** MIT (code) + DeepSeek Model Agreement (supports commercial use)

## Papers

| Paper | arXiv ID | Local PDF |
|-------|----------|-----------|
| DeepSeek-V3 Technical Report | 2412.19437 | [PDF](DeepSeek-V3_arxiv_2412.19437.pdf) |

## Documentation & Links

### Official Resources
| Resource | Link |
|----------|------|
| Official Website | [deepseek.com](https://www.deepseek.com/) |
| Blog Post | [DeepSeek-V3 Announcement](https://deepseek.com/blog/deepseek-v3/) |
| Chat Interface | [chat.deepseek.com](https://chat.deepseek.com/) |
| API Platform | [platform.deepseek.com](https://platform.deepseek.com/) |

### GitHub
| Repository | Link |
|------------|------|
| DeepSeek-V3 | [github.com/deepseek-ai/DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) |

### HuggingFace Models
| Model | Parameters | Link |
|-------|------------|------|
| DeepSeek-V3 | 671B (37B active) | [HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-V3) |
| DeepSeek-V3-Base | 671B (37B active) | [HuggingFace](https://huggingface.co/deepseek-ai/DeepSeek-V3-Base) |

### Research Paper
| Resource | Link |
|----------|------|
| arXiv | [arxiv.org/abs/2412.19437](https://arxiv.org/abs/2412.19437) |
| PDF | [arXiv PDF](https://arxiv.org/pdf/2412.19437) |

### Local Deployment Frameworks
| Framework | Features | Link |
|-----------|----------|------|
| SGLang | FP8 & BF16, NVIDIA & AMD GPUs | [SGLang Benchmark](https://github.com/sgl-project/sglang/tree/main/benchmark/deepseek_v3) |
| LMDeploy | FP8 & BF16 inference | [LMDeploy Guide](https://github.com/InternLM/lmdeploy/issues/2960) |
| vLLM | FP8 & BF16, tensor/pipeline parallelism | [vLLM](https://github.com/vllm-project/vllm) |
| TensorRT-LLM | BF16 & INT4/8 quantization | [TensorRT-LLM DeepSeek](https://github.com/NVIDIA/TensorRT-LLM/tree/deepseek/examples/deepseek_v3) |

### Community
| Platform | Link |
|----------|------|
| Discord | [DeepSeek Discord](https://discord.gg/Tc7c45Zzu5) |
| Twitter/X | [@deepseek_ai](https://twitter.com/deepseek_ai) |
| Contact | service@deepseek.com |
