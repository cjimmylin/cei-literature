# CogView: Text-to-Image Generation Models

## Overview

CogView is Zhipu AI's family of text-to-image generation models, developed jointly with Tsinghua University. The series represents pioneering work in Chinese text-to-image generation and has evolved to incorporate relay diffusion techniques for high-quality, efficient image generation.

## Model Versions

### CogView (2021)
- **Parameters**: 4 billion
- **Architecture**: Transformer-based text-to-image generation
- **Key Innovation**: First large-scale open Chinese text-to-image model
- **Technical Features**:
  - Techniques for stable training of ultra-high resolution generation
  - Bidirectional attention for text-image alignment
  - Progressive generation approach
- **Paper**: [CogView_2105.13290.pdf](CogView_2105.13290.pdf)
- **arXiv**: https://arxiv.org/abs/2105.13290

### CogView2 (2022)
- **Architecture**: Hierarchical transformer with cross-modal attention
- **Key Innovation**: Improved efficiency and quality over CogView
- **Technical Features**:
  - Enhanced text-image alignment
  - Better Chinese character generation
  - Faster inference speed
- **Paper**: [CogView2_2204.14217.pdf](CogView2_2204.14217.pdf)
- **arXiv**: https://arxiv.org/abs/2204.14217

### CogView3 (2024)
- **Architecture**: Cascaded diffusion framework (relay diffusion)
- **Key Innovation**: First model implementing relay diffusion for text-to-image generation
- **Conference**: ECCV 2024
- **Technical Features**:
  - Three-stage generation: 512x512 → 1024x1024 → 2048x2048
  - Significantly reduced training and inference costs
  - 77.0% win rate vs SDXL in human evaluation
  - Progressive distillation enabling 10x faster inference than SDXL
- **Paper**: [CogView3_2403.05121.pdf](CogView3_2403.05121.pdf)
- **arXiv**: https://arxiv.org/abs/2403.05121
- **Release**: March 8, 2024

### CogView3-Plus (2024)
- **Architecture**: Diffusion Transformer (DiT) based
- **Key Innovation**: Enhanced DiT framework with zero-SNR diffusion noise scheduling
- **Technical Features**:
  - Text-image joint attention mechanism
  - 3B parameter variant for efficient deployment
  - Open-sourced on October 14, 2024
- **Repository**: https://github.com/THUDM/CogView3

### CogView4 (2025)
- **Key Innovation**: First open-source text-to-image model capable of generating Chinese characters
- **Technical Features**:
  - Bilingual GLM-4 encoder
  - Bilingual text-image training for Chinese and English prompts
  - State-of-the-art (SOTA) on DPG-Bench among open-source models
- **License**: Apache 2.0
- **Repository**: https://github.com/THUDM/CogView4
- **Release**: March 4, 2025

## Research Impact

The CogView series has been instrumental in advancing:
- Chinese text-to-image generation capabilities
- Relay diffusion techniques for efficient high-resolution generation
- Open-source alternatives to proprietary text-to-image models
- Bilingual (Chinese-English) prompt understanding

## Resources

- **Official Website**: https://chatglm.cn
- **GitHub**: https://github.com/THUDM/CogView3, https://github.com/THUDM/CogView4
- **HuggingFace**: https://huggingface.co/THUDM
- **API Platform**: https://open.bigmodel.cn

## Related Models

- **RelayDiffusion**: Core technique used in CogView3 ([Papers/RelayDiffusion_2309.03350.pdf](../Papers/RelayDiffusion_2309.03350.pdf))
- **Inf-DiT**: Infinite resolution diffusion transformer ([Papers/Inf-DiT_2405.04312.pdf](../Papers/Inf-DiT_2405.04312.pdf))
- **ImageReward**: Image quality evaluation ([Papers/ImageReward_2304.05977.pdf](../Papers/ImageReward_2304.05977.pdf))
- **VisionReward**: Vision model evaluation ([Papers/VisionReward_2412.21059.pdf](../Papers/VisionReward_2412.21059.pdf))
