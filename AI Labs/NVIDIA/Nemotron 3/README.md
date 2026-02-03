# Nemotron 3

## Overview
Hybrid Mamba-Transformer Mixture-of-Experts (MoE) models designed for next-generation agentic AI applications, featuring up to 1M token context windows and best-in-class throughput.

## Model Family
- **Nemotron 3 Nano** (30B parameters): Efficient model for agentic reasoning
- **Nemotron 3 Super**: Mid-tier model
- **Nemotron 3 Ultra**: Largest model (rated most intelligent open-source model as of April 2025)

## Technical Specifications
- **Release Year:** 2025
- **Architecture:** Hybrid Mamba-Transformer MoE (23 Mamba-2 and MoE layers + 6 Attention layers)
- **Version:** Nano/Super/Ultra
- **Parameters:** 30B - 500B
- **Context Length:** Up to 1 million tokens
- **Training Data:** 25T tokens (Nano), cutoff date June 25, 2025

## Research Papers

### 1. NVIDIA Nemotron 3: Efficient and Open Intelligence (December 2025)
**File:** Nemotron-3-Efficient-Open-Intelligence.pdf
**arXiv:** 2512.20856
- Introduces the complete Nemotron 3 family (Nano, Super, Ultra)
- Details the hybrid MoE architecture
- Demonstrates strong agentic, reasoning, and conversational capabilities

### 2. Nemotron 3 Nano Technical Report (December 2025)
**File:** Nemotron-3-Nano-Technical-Report.pdf
**Source:** NVIDIA Research
- Focused technical report on the 30B Nano variant
- First effort to scale up reinforcement learning in post-training using multi-environment RL
- Details training on all environments simultaneously

### 3. Nemotron 3 Nano arXiv Paper (December 2025)
**File:** Nemotron-3-Nano-arXiv.pdf
**arXiv:** 2512.20848
- Academic publication on Nemotron 3 Nano
- Open, efficient mixture-of-experts hybrid Mamba-Transformer model for agentic reasoning

### 4. Nemotron 3 White Paper (December 2025)
**File:** Nemotron-3-White-Paper.pdf
**Source:** NVIDIA Research
- Comprehensive white paper covering the entire Nemotron 3 platform
- Training methodology, architecture details, and benchmark results

### 5. Nemotron 3: Hybrid Mamba-Transformer MoE (Earlier 2025)
**File:** Nemotron_3_Hybrid_Mamba_Transformer_MoE.pdf
- Initial research on hybrid architecture approach

## Model Card
**File:** Nemotron-3-Nano-Model-Card.md
- Official model card for Nemotron 3 Nano 30B-A3B
- API access, deployment options, and licensing information

## Documentation & Links

### Official Resources
- [Official Announcement](https://nvidianews.nvidia.com/news/nvidia-debuts-nemotron-3-family-of-open-models) - NVIDIA News
- [Research Page](https://research.nvidia.com/labs/nemotron/Nemotron-3/) - NVIDIA Research
- [Model Card](https://build.nvidia.com/nvidia/nemotron-3-nano-30b-a3b/modelcard) - Official model card
- [Technical Blog](https://developer.nvidia.com/blog/inside-nvidia-nemotron-3-techniques-tools-and-data-that-make-it-efficient-and-accurate/) - Technical deep dive

### Model Weights
- [HuggingFace: Nemotron-3-Nano-30B-A3B-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16) - BF16 variant
- [HuggingFace: Nemotron-3-Nano-30B-A3B-Base-BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-Base-BF16) - Base model
- [HuggingFace: NVIDIA](https://huggingface.co/nvidia) - All NVIDIA models

### NGC Catalog
- [NGC Catalog](https://catalog.ngc.nvidia.com/) - NVIDIA model registry

### Documentation
- [NeMo Documentation](https://docs.nvidia.com/nemo-framework/user-guide/latest/) - Framework user guide
