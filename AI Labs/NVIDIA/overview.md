# NVIDIA AI Research Overview

## Lab Overview

NVIDIA is a leading technology company that has become central to the AI revolution through both hardware (GPUs) and software contributions. NVIDIA's AI research division focuses on large-scale language models, multimodal AI, and efficient training methodologies. The company has pioneered techniques for training multi-billion parameter models through innovations in parallelism strategies and numerical precision training.

Key research areas include:
- **Large-Scale Language Models**: Megatron-LM, Megatron-Turing NLG, Nemotron series
- **Multimodal AI**: NVLM for vision-language models
- **Training Infrastructure**: DeepSpeed integration, 3D parallelism, NVFP4 training
- **Efficient Architectures**: Hybrid Mamba-Transformer, Mixture-of-Experts (MoE)
- **Document Understanding**: Nemotron-Parse for OCR and document parsing

---

## Timeline of Models

| Year | Model | Parameters | Key Milestone |
|------|-------|------------|---------------|
| 2019 | Megatron-LM | 8.3B | First efficient intra-layer model parallelism for transformers |
| 2022 | Megatron-Turing NLG | 530B | Largest monolithic transformer language model at the time (joint with Microsoft) |
| 2024 | Nemotron-4 340B | 340B | Open-access model with 98%+ synthetic data alignment |
| 2024 | NVLM 1.0 | 72B | Frontier-class multimodal LLM with improved text-only performance |
| 2025 | Nemotron-Parse 1.1 | 885M | Lightweight document parsing and OCR model |
| 2025 | Nemotron 3 | 30B (3B active) | Hybrid Mamba-Transformer MoE with 1M token context |

---

## Summary of All Models

| Model | Parameters | Architecture | Key Capabilities | Release Date |
|-------|------------|--------------|------------------|--------------|
| Megatron-LM | 8.3B (GPT-2), 3.9B (BERT) | Transformer | Model parallelism, SOTA on WikiText103/LAMBADA/RACE | Sept 2019 |
| Megatron-Turing NLG | 530B | Transformer (decoder-only) | 3D parallelism, zero/few-shot learning | Jan 2022 |
| Nemotron-4 340B | 340B (96 layers) | Transformer with GQA | Synthetic data generation, fits on single DGX H100 | June 2024 |
| NVLM 1.0 | 72B | Decoder-only / Cross-attention / Hybrid | Vision-language, OCR, multimodal reasoning | Sept 2024 |
| Nemotron-Parse 1.1 | 885M (256M decoder) | Encoder-Decoder | Document OCR, table extraction, multilingual | Nov 2025 |
| Nemotron 3 Nano | 30B (3B active) | Hybrid Mamba-Transformer MoE | 1M context, 3.3x throughput vs transformers | Dec 2025 |

---

## Detailed Model Information

### Megatron-LM (2019)

**Paper**: "Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism"

**Overview**: Megatron-LM introduced an efficient intra-layer model parallel approach that enables training transformer models with billions of parameters using native PyTorch without custom compilers.

**Key Specifications**:
- **Parameters**: Up to 8.3B (GPT-2 style), 3.9B (BERT style)
- **Training**: 512 NVIDIA V100 GPUs with 8-way model parallelism
- **Performance**: 15.1 PetaFLOPs sustained, 76% scaling efficiency
- **Architecture**: Standard transformer with layer normalization rearrangement for BERT

**Notable Features**:
- Simple intra-layer model parallelism requiring only a few communication operations
- Orthogonal and complementary to pipeline model parallelism
- Critical insight: Careful placement of layer normalization is essential for scaling BERT models

**Benchmark Results**:
- WikiText103: 10.81 perplexity (SOTA at the time)
- LAMBADA: 66.51% accuracy (SOTA at the time)
- RACE: 90.9% accuracy (SOTA at the time)

**Source PDF**: [Megatron-LM_Training_Multi-Billion_Parameter_Language_Models.pdf](../../Lit-WS-PDFs/AI%20Labs/NVIDIA/Megatron-LM/Megatron-LM_Training_Multi-Billion_Parameter_Language_Models.pdf)

---

### Megatron-Turing NLG 530B (2022)

**Paper**: "Using DeepSpeed and Megatron to Train Megatron-Turing NLG 530B"

**Overview**: A joint effort between NVIDIA and Microsoft, MT-NLG was the largest monolithic transformer language model at its release with 530 billion parameters, representing 3x more parameters than GPT-3.

**Key Specifications**:
- **Parameters**: 530 billion
- **Architecture**: 105 layers, hidden dimension 20480, 128 attention heads
- **Sequence Length**: 2048 tokens
- **Training Data**: 339 billion tokens from 15 datasets
- **Training Infrastructure**: 560 DGX A100 nodes (4,480 GPUs)

**Notable Features**:
- **3D Parallelism**: Combines tensor parallelism (8-way), pipeline parallelism (35-way), and data parallelism
- **Topology-Aware Mapping**: Optimizes communication by prioritizing high-bandwidth connections
- **Careful Data Curation**: Fuzzy deduplication, quality filtering with fastText classifier

**Training Details**:
- Memory requirement: ~10 terabytes for model states
- Performance: 113-126 TeraFLOPs per GPU
- Batch size: 1920 (with gradient accumulation)

**Source PDF**: [Megatron-Turing_NLG_530B.pdf](../../Lit-WS-PDFs/AI%20Labs/NVIDIA/Megatron-Turing%20NLG/Megatron-Turing_NLG_530B.pdf)

---

### Nemotron-4 340B (2024)

**Paper**: "Nemotron-4 340B Technical Report"

**Overview**: The Nemotron-4 340B family includes Base, Instruct, and Reward models released under the NVIDIA Open Model License. Notable for using over 98% synthetically generated data in the alignment process.

**Key Specifications**:
- **Parameters**: 340B (331.6B non-embedding, 9.4B embedding)
- **Architecture**: 96 transformer layers, hidden dimension 18432, 96 attention heads, 8 KV heads (GQA)
- **Context Length**: 4096 tokens
- **Vocabulary**: 256,000 tokens
- **Training**: 9 trillion tokens (8T pretraining + 1T continued)

**Model Family**:
1. **Nemotron-4-340B-Base**: Competitive with Llama-3 70B, Mixtral 8x22B on reasoning tasks
2. **Nemotron-4-340B-Instruct**: Superior instruction following and chat capabilities
3. **Nemotron-4-340B-Reward**: Top accuracy on RewardBench (92.0% overall)

**Notable Features**:
- **Synthetic Data Generation Pipeline**: Comprehensive pipeline for prompts, responses, quality filtering
- **Continued Training**: Final 1T tokens with shifted data distribution for improved quality
- **Designed for Single DGX H100**: Fits on 8 GPUs when deployed in FP8 precision

**Training Infrastructure**:
- 768 DGX H100 nodes (6,144 GPUs)
- 8-way tensor parallelism, 12-way pipeline parallelism
- MFU: ~41-42%

**Source PDF**: [Nemotron-4_340B_Technical_Report.pdf](../../Lit-WS-PDFs/AI%20Labs/NVIDIA/Nemotron-4/Nemotron-4_340B_Technical_Report.pdf)

---

### NVLM 1.0 (2024)

**Paper**: "NVLM: Open Frontier-Class Multimodal LLMs"

**Overview**: NVLM 1.0 is a family of frontier-class multimodal LLMs that achieve state-of-the-art results on vision-language tasks while improving text-only performance over the backbone LLM.

**Key Specifications**:
- **Parameters**: 72B (NVLM-D-72B)
- **Architecture Variants**:
  - **NVLM-D**: Decoder-only (like LLaVA)
  - **NVLM-X**: Cross-attention-based (like Flamingo)
  - **NVLM-H**: Novel hybrid architecture

**Notable Features**:
- **1-D Tile-Tagging**: Novel design for dynamic high-resolution images, boosting OCR and reasoning
- **Production-Grade Multimodality**: Maintains/improves text-only performance during multimodal training
- **+4.3 points improvement** on text-only math and coding benchmarks after multimodal training

**Capabilities**:
- Chart and table understanding
- OCR and document comprehension
- Multimodal math reasoning
- Code generation from visual inputs
- Meme and humor understanding

**Benchmark Performance** (NVLM-D-72B):
- MMMU: 59.7%
- MathVista: 65.2%
- OCRBench: 853
- AI2D: 94.2%
- DocVQA: 92.6%

**Source PDF**: [NVLM_1.0_Multimodal_Model.pdf](../../Lit-WS-PDFs/AI%20Labs/NVIDIA/NVLM%201.0/NVLM_1.0_Multimodal_Model.pdf)

---

### Nemotron-Parse 1.1 (2025)

**Paper**: "NVIDIA Nemotron-Parse 1.1"

**Overview**: A lightweight document parsing and OCR model that extracts formatted text, bounding boxes, and semantic classes from documents while preserving reading order.

**Key Specifications**:
- **Parameters**: 885M total (657M vision encoder, 256M decoder)
- **Architecture**: Encoder-decoder transformer
  - Vision Encoder: RADIO (ViT-H/16)
  - Decoder: mBART-style (10 layers, tied weights)
- **Vision Tokens**: 3200 (standard) / 833 (TC variant)

**Model Variants**:
1. **Nemotron-Parse 1.1**: Full capability model
2. **Nemotron-Parse 1.1-TC**: Token-compressed variant with 20% speed improvement

**Notable Features**:
- **Multi-token Prediction**: Predicts multiple tokens simultaneously for faster inference
- **No Positional Embeddings in Decoder**: Better generalization to different document lengths
- **Multilingual Support**: English, German, French, Italian, Spanish, Chinese, Japanese

**Capabilities**:
- Markdown/LaTeX text extraction
- Complex table parsing
- Mathematical formula recognition
- Bounding box prediction with semantic classes
- Reading order preservation

**Performance**:
- OCR F1: 0.978 (English)
- Table Extraction (TEDS): 86.2%
- Inference: ~4-5 pages/second on H100

**Source PDF**: [Nemotron-Parse_Document_Parsing.pdf](../../Lit-WS-PDFs/AI%20Labs/NVIDIA/Nemotron-Parse/Nemotron-Parse_Document_Parsing.pdf)

---

### Nemotron 3 (2025)

**Paper**: "NVIDIA Nemotron 3: Efficient and Open Intelligence"

**Overview**: The Nemotron 3 family (Nano, Super, Ultra) uses a hybrid Mamba-Transformer MoE architecture for best-in-class throughput with context lengths up to 1M tokens.

**Key Specifications** (Nemotron 3 Nano):
- **Parameters**: 30B total, 3B active (MoE)
- **Architecture**: Hybrid Mamba-2 + Transformer + MoE
- **Context Length**: Up to 1M tokens
- **Training**: Multi-environment reinforcement learning

**Model Family**:
1. **Nemotron 3 Nano**: Cost-efficient, 30B total / 3B active
2. **Nemotron 3 Super**: Optimized for collaborative agents (coming soon)
3. **Nemotron 3 Ultra**: State-of-the-art accuracy and reasoning (coming soon)

**Notable Innovations**:

1. **Hybrid Mamba-Transformer MoE**:
   - Predominantly Mamba-2 + MoE layers with few attention layers
   - 3.3x higher throughput than comparable Transformer MoEs
   - Fixed memory during generation (no growing KV cache for Mamba layers)

2. **LatentMoE**:
   - Projects tokens to smaller latent dimension for routing
   - Reduces memory bandwidth and communication by ~4x
   - Increases expert diversity without sacrificing inference speed

3. **Multi-Token Prediction (MTP)**:
   - ~97% acceptance rate on first two predicted tokens
   - Enables efficient speculative decoding
   - ~2.4% average accuracy improvement across benchmarks

4. **NVFP4 Training**:
   - Native FP4 GEMMs for 3x higher throughput on GB300
   - <1% relative loss difference from BF16

5. **Reasoning Budget Control**:
   - Granular control over inference-time thinking token budget
   - Accuracy-efficiency trade-off at inference time

**Benchmark Performance** (Nano):
- Arena-Hard-v2: 67.7%
- AIME25: 89.1%
- IFBench: 99.2%
- SWE-Bench: 47.7%
- RULER @ 1M: 68.2%

**Source PDF**: [Nemotron_3_Hybrid_Mamba_Transformer_MoE.pdf](../../Lit-WS-PDFs/AI%20Labs/NVIDIA/Nemotron%203/Nemotron_3_Hybrid_Mamba_Transformer_MoE.pdf)

---

## Key Technologies and Innovations

### Model Parallelism
- **Tensor Parallelism**: Intra-layer partitioning across GPUs
- **Pipeline Parallelism**: Inter-layer partitioning with micro-batching
- **3D Parallelism**: Combination of tensor, pipeline, and data parallelism

### Training Efficiency
- **NVFP4**: Native FP4 training for 3x speedup on modern hardware
- **Mixed Precision**: BF16/FP16 training with selective high-precision layers
- **Activation Checkpointing**: Memory-efficient gradient computation

### Architecture Innovations
- **Hybrid Mamba-Transformer**: Combines benefits of state-space models and attention
- **LatentMoE**: Efficient expert routing in smaller latent space
- **GQA (Grouped Query Attention)**: Reduced KV heads for efficiency

### Data and Alignment
- **Synthetic Data Generation**: Over 98% synthetic data for alignment
- **HelpSteer**: Multi-attribute regression reward model
- **Multi-environment RL**: Diverse training environments for robust capabilities

---

## Open Source Resources

- **Megatron-LM**: https://github.com/NVIDIA/Megatron-LM
- **NeMo**: https://github.com/NVIDIA/NeMo
- **NeMo-RL**: https://github.com/NVIDIA-NeMo/RL
- **NeMo-Gym**: https://github.com/NVIDIA-NeMo/Gym
- **HuggingFace Models**: https://huggingface.co/nvidia

---

## References

All source PDFs are available in the vault at:
- `Lit-WS-PDFs/AI Labs/NVIDIA/Megatron-LM/`
- `Lit-WS-PDFs/AI Labs/NVIDIA/Megatron-Turing NLG/`
- `Lit-WS-PDFs/AI Labs/NVIDIA/Nemotron-4/`
- `Lit-WS-PDFs/AI Labs/NVIDIA/NVLM 1.0/`
- `Lit-WS-PDFs/AI Labs/NVIDIA/Nemotron-Parse/`
- `Lit-WS-PDFs/AI Labs/NVIDIA/Nemotron 3/`
