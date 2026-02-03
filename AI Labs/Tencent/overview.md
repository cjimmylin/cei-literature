# Tencent AI Lab Overview

## Lab Introduction

Tencent is one of China's leading technology companies, with significant investments in artificial intelligence research through its Tencent Hunyuan team. The Hunyuan foundation model family represents Tencent's flagship AI initiative, encompassing large language models, video generation, 3D asset creation, and multimodal capabilities. Tencent has notably committed to open-sourcing several of its most powerful models, aiming to bridge the gap between closed-source and open-source AI communities.

Tencent's AI research spans multiple domains:
- **Large Language Models**: Hunyuan-Large (MoE architecture)
- **Video Generation**: HunyuanVideo (text-to-video, image-to-video)
- **3D Asset Generation**: Hunyuan3D (image-to-3D, text-to-3D)
- **Image Generation**: Hunyuan Image
- **Audio Generation**: Video-to-audio models

The Hunyuan models power Tencent's AI chatbot Yuanbao (yuanbao.tencent.com) and are integrated across thousands of Tencent's applications, serving billions of users.

---

## Model Timeline

| Year | Model | Key Milestone |
|------|-------|---------------|
| 2023 | Hunyuan 1.0 | Initial proprietary foundation model |
| Feb 2024 | Hunyuan MoE | Trillion-parameter flagship LLM adopted for Yuanbao |
| Nov 2024 | Hunyuan-Large | Open-source 389B MoE model (52B active) |
| Dec 2024 | HunyuanVideo | Open-source 13B video generation model |
| Jan 2025 | Hunyuan3D 2.0 | High-resolution textured 3D generation |
| Jun 2025 | Hunyuan3D 2.5 | 10B parameter shape generation with PBR textures |
| 2025 | Hunyuan 2.0 | 406B MoE with 256k context |
| 2025 | Hunyuan Video 1.5 | Lightweight 8.3B for consumer GPUs |
| 2025 | Hunyuan Image 3.0 | 80B MoE image generation |

---

## Model Summary Table

| Model | Type | Parameters | Key Features | Open Source |
|-------|------|------------|--------------|-------------|
| **Hunyuan-Large** | LLM (MoE) | 389B total / 52B active | 256K context, 7T training tokens, Chinese+English | Yes |
| **HunyuanVideo** | Video Generation | 13B | Text-to-video, image-to-video, avatar animation | Yes |
| **Hunyuan3D 2.5** | 3D Generation | Up to 10B | Shape + PBR texture generation | Yes |

---

## Detailed Model Profiles

### Hunyuan-Large

**Release**: November 2024
**Paper**: [arXiv:2411.02265](https://arxiv.org/abs/2411.02265)
**Code**: [github.com/Tencent/Tencent-Hunyuan-Large](https://github.com/Tencent/Tencent-Hunyuan-Large)
**Models**: [huggingface.co/tencent/Tencent-Hunyuan-Large](https://huggingface.co/tencent/Tencent-Hunyuan-Large)

#### Overview
Hunyuan-Large is the largest open-source Transformer-based Mixture of Experts (MoE) model, featuring 389 billion total parameters with 52 billion activated parameters per token. It supports context lengths up to 256K tokens and demonstrates performance comparable to or exceeding LLama3.1-405B while using significantly fewer active parameters.

#### Architecture
- **Model Structure**: Transformer with MoE, 64 layers, 80 attention heads
- **Expert Configuration**: 1 shared expert + 16 specialized experts (1 activated per token)
- **Attention**: Grouped-Query Attention (GQA) + Cross-Layer Attention (CLA) for 95% KV cache reduction
- **Position Encoding**: Rotary Position Embedding (RoPE)
- **Activation**: SwiGLU
- **Vocabulary**: 128K tokens (100K tiktoken + 28K Chinese enhancement)

#### Key Innovations
1. **High-Quality Synthetic Data**: 1.5T tokens of synthetic data out of 7T total training tokens
2. **Recycle Routing**: Novel strategy to reassign tokens from overloaded experts rather than dropping them
3. **Expert-Specific Learning Rates**: Different learning rates for shared vs specialized experts
4. **KV Cache Compression**: GQA+CLA combination saves 95% memory vs standard attention

#### Training
- **Pre-training**: 7T tokens with annealing phase in final 5%
- **Long-Context**: Progressive training 32K to 256K with RoPE base frequency scaled to 1 billion
- **Post-training**: SFT on 1M+ samples, followed by DPO for human preference alignment

#### Performance Highlights
| Benchmark | Hunyuan-Large | LLama3.1-405B |
|-----------|---------------|---------------|
| MMLU | 88.4 | 85.2 |
| GSM8K | 92.8 | 89.0 |
| MATH | 69.8 | 53.8 |
| HumanEval | 71.4 | 61.0 |
| CMMLU (Chinese) | 90.2 | - |

**Source PDF**: [[Hunyuan-Large/Hunyuan-Large_Open_MoE_Model.pdf]]

---

### HunyuanVideo

**Release**: December 2024
**Paper**: [arXiv:2412.03603](https://arxiv.org/abs/2412.03603)
**Code**: [github.com/Tencent/HunyuanVideo](https://github.com/Tencent/HunyuanVideo)

#### Overview
HunyuanVideo is an open-source video foundation model with 13 billion parameters, designed to bridge the gap between closed-source and open-source video generation capabilities. It achieves performance comparable to or superior to leading closed-source models like Runway Gen-3 and Luma 1.6.

#### Architecture
- **Backbone**: Diffusion Transformer (DiT) with dual-stream to single-stream design
- **Parameters**: 13B (largest open-source video model)
- **3D VAE**: Causal 3D VAE with 4x temporal and 8x spatial compression
- **Text Encoder**: Multimodal LLM (MLLM) with bidirectional token refiner + CLIP
- **Position Encoding**: 3D Rotary Position Embedding (RoPE) for time, height, width
- **Training**: Flow Matching framework

#### Key Features
1. **Multi-Resolution Generation**: Supports various aspect ratios and durations
2. **Text Alignment**: Strong prompt following with complex multi-subject scenes
3. **High Motion Dynamics**: Excels in generating dynamic, high-motion videos
4. **Concept Generalization**: Can combine concepts not seen in training data
5. **Camera Control**: 14 distinct camera movement types

#### Data Pipeline
- Hierarchical filtering from 256p to 720p with progressive quality thresholds
- Structured JSON captioning with dense descriptions, style, shot type, lighting, atmosphere
- ~1M manually curated samples for fine-tuning

#### Training Strategy
1. **Image Pre-training**: 256px then mix-scale (256px + 512px)
2. **Progressive Video Training**: Low-res short to high-res long video
3. **Video-Image Joint Training**: Addresses high-quality video data scarcity

#### Performance (Human Evaluation, 1,533 prompts, 60 evaluators)
| Model | Text Alignment | Motion Quality | Visual Quality | Overall Rank |
|-------|----------------|----------------|----------------|--------------|
| HunyuanVideo | 61.8% | 66.5% | 95.7% | 1 |
| GEN-3 alpha | 47.7% | 54.7% | 97.5% | 4 |
| Luma 1.6 | 57.6% | 44.2% | 94.1% | 5 |

#### Applications
- **Image-to-Video (I2V)**: Token replacement with semantic image injection
- **Video-to-Audio (V2A)**: Foley sound and music generation
- **Avatar Animation**: Audio-driven, pose-driven, expression-driven, and hybrid control
- **Portrait Animation**: Upper-body talking avatar generation

**Source PDF**: [[HunyuanVideo/HunyuanVideo_Large_Video_Generation_Model.pdf]]

---

### Hunyuan3D 2.5

**Release**: June 2025
**Paper**: [arXiv:2506.16504](https://arxiv.org/abs/2506.16504)
**Code**: [github.com/Tencent/Hunyuan3D-2](https://github.com/Tencent/Hunyuan3D-2)
**Demo**: [3d.hunyuan.tencent.com](https://3d.hunyuan.tencent.com)

#### Overview
Hunyuan3D 2.5 is a suite of 3D diffusion models for generating high-fidelity, detailed textured 3D assets. It follows a two-stage pipeline (shape generation, then texture generation) with substantial improvements over Hunyuan3D 2.0 in both shape detail and PBR material quality.

#### Architecture
**Stage 1 - Shape Generation (LATTICE)**
- New shape foundation model trained on large-scale high-quality datasets
- Largest model reaches 10B parameters
- Generates sharp, detailed shapes with clean, smooth surfaces
- Supports single image or 4 multi-view images as input
- Uses guidance and step distillation for efficient inference

**Stage 2 - Texture Generation (Paint-PBR)**
- Extended from Hunyuan3D 2.0 Paint model
- Multi-view architecture with 3D-aware RoPE
- Generates PBR materials: albedo, roughness, metallic maps
- Dual-channel attention for spatial alignment across material channels
- Dual-phase resolution enhancement (512x512 to 768x768)

#### Key Innovations
1. **Extreme Detail**: Near handcrafted quality (correct finger count, intricate patterns)
2. **Smooth Surfaces with Sharp Edges**: Balance previously difficult to achieve
3. **PBR Material Generation**: Proper disentanglement of material and illumination
4. **Multi-Channel Alignment**: Shared attention masks across albedo and metallic-roughness

#### Technical Details
- **Input**: Reference image + normal map + CCM (coordinate map)
- **Material Channels**: Learnable embeddings for albedo, MR (metallic-roughness)
- **Training**: Two-phase with zoom-in strategy for detail capture
- **Inference**: Up to 768x768 multi-view resolution with UniPC sampler

#### Performance
**Shape Generation (Numerical)**
| Model | ULIP-T | Uni3D-T | Uni3D-I |
|-------|--------|---------|---------|
| Hunyuan3D 2.5 | 0.0785 | 0.2542 | 0.3151 |
| Hunyuan3D 2.0 | 0.0771 | 0.2519 | 0.3151 |
| Trellis | 0.0769 | 0.2496 | 0.3116 |

**Texture Generation**
| Metric | Ours | Best Competitor |
|--------|------|-----------------|
| CLIP-FID | 23.97 | 26.86 |
| FID | 165.8 | 176.9 |
| CLIP-I | 0.9281 | 0.8871 |

**User Study (Image-to-3D)**
- 72% win rate vs Commercial Model 1 (9x higher)
- Outperforms all tested commercial models

**Source PDF**: [[Hunyuan 3D/Hunyuan3D_2.5_3D_Asset_Generation.pdf]]

---

## Resources

### Official Links
| Resource | URL |
|----------|-----|
| Tencent GitHub | [github.com/Tencent](https://github.com/Tencent) |
| HuggingFace | [huggingface.co/Tencent](https://huggingface.co/Tencent) |
| Hunyuan API | [cloud.tencent.com/document/product/1729](https://cloud.tencent.com/document/product/1729) |
| Hunyuan Demo | [hunyuan.tencent.com](https://hunyuan.tencent.com/) |
| Hunyuan3D Demo | [3d.hunyuan.tencent.com](https://3d.hunyuan.tencent.com) |

### Source PDFs
- [[Hunyuan-Large/Hunyuan-Large_Open_MoE_Model.pdf|Hunyuan-Large Technical Report]]
- [[HunyuanVideo/HunyuanVideo_Large_Video_Generation_Model.pdf|HunyuanVideo Technical Report]]
- [[Hunyuan 3D/Hunyuan3D_2.5_3D_Asset_Generation.pdf|Hunyuan3D 2.5 Technical Report]]

---

*Last updated: January 2026*
