# Alibaba Qwen Models Overview

## Lab Overview

The **Qwen Team** (Qianwen, meaning "thousands of prompts" in Chinese) is Alibaba Group's large language model research division. Since 2023, the team has developed a comprehensive series of foundation models spanning language understanding, vision-language multimodality, specialized coding/math capabilities, and long-context processing. Qwen models are notable for their strong multilingual support (up to 119 languages in Qwen3), competitive performance against proprietary models, and open-weight releases under Apache 2.0 licensing.

The Qwen series has evolved rapidly from initial 7B-72B dense models to sophisticated mixture-of-experts (MoE) architectures with up to 235B parameters. Key innovations include:
- Progressive context length extension (4K to 1M tokens)
- Unified thinking/non-thinking modes for reasoning tasks
- Strong-to-weak distillation for efficient smaller models
- Multimodal capabilities for vision, audio, and document understanding

---

## Timeline of Qwen Models

| Date | Model | Key Milestone |
|------|-------|---------------|
| Aug 2023 | Qwen-VL | First vision-language model |
| Sep 2023 | Qwen (1.0) | Initial 7B/14B/72B dense LLMs |
| Jul 2024 | Qwen2 | 7T token training, 30+ language support, MoE architecture |
| Oct 2024 | Qwen2-VL | Enhanced vision-language with video understanding |
| Dec 2024 | Qwen2.5 | 18T tokens, 0.5B-72B sizes, improved math/coding |
| Jan 2025 | Qwen2.5-1M | 1 million token context length |
| May 2025 | Qwen3 | 36T tokens, 119 languages, thinking mode, MoE flagship |

---

## Summary Table of All Models

| Model | Release | Parameters | Architecture | Context Length | Key Features |
|-------|---------|------------|--------------|----------------|--------------|
| **Qwen (1.0)** | Sep 2023 | 1.8B, 7B, 14B | Dense | 2K (8K extended) | Foundation LLMs, RoPE, SwiGLU |
| **Qwen-VL** | Aug 2023 | 9.6B total | Dense + ViT | 2K | Vision-language, grounding, OCR |
| **Qwen2** | Jul 2024 | 0.5B-72B, 57B-A14B MoE | Dense + MoE | 32K (128K) | GQA, 7T tokens, 30+ languages |
| **Qwen2-VL** | Oct 2024 | 2B-72B | Dense + ViT | Variable | Video understanding, dynamic resolution |
| **Qwen2.5** | Dec 2024 | 0.5B-72B | Dense | 32K-128K | 18T tokens, 8K generation |
| **Qwen2.5-1M** | Jan 2025 | 7B, 14B | Dense | 1M tokens | Long-context, sparse attention |
| **Qwen3** | May 2025 | 0.6B-235B-A22B | Dense + MoE | 32K-128K | 36T tokens, thinking mode, 119 languages |

---

## Detailed Model Sections

### Qwen (1.0)

**Release Date:** September 2023
**Paper:** [arXiv:2309.16609](https://arxiv.org/abs/2309.16609)

The inaugural Qwen series introduced comprehensive language models with strong base capabilities:

**Model Sizes:**
| Parameters | Hidden Size | Heads | Layers | Training Tokens |
|------------|-------------|-------|--------|-----------------|
| 1.8B | 2048 | 16 | 24 | 2.2T |
| 7B | 4096 | 32 | 32 | 2.4T |
| 14B | 5120 | 40 | 40 | 3.0T |

**Architecture Highlights:**
- Modified Transformer with RoPE positional embeddings
- SwiGLU activation function (8/3 FFN ratio)
- RMSNorm with pre-normalization
- Untied input/output embeddings
- FP32 precision for inverse frequency matrix in RoPE

**Training:**
- Up to 3 trillion tokens of diverse multilingual data
- Byte-pair encoding tokenizer (~152K vocabulary)
- Flash Attention for efficiency
- AdamW optimizer with cosine learning rate schedule

**Specialized Variants:**
- **Qwen-Chat:** Instruction-tuned with SFT and RLHF
- **Code-Qwen:** Specialized for code generation
- **Math-Qwen-Chat:** Optimized for mathematical reasoning

**Source PDF:** [[../PDF Extracts/AI Labs/Alibaba (Qwen)-Qwen_Technical_Report_2309.16609.md|Qwen Technical Report]]

---

### Qwen2

**Release Date:** July 2024
**Paper:** [arXiv:2407.10671](https://arxiv.org/abs/2407.10671)

Qwen2 introduced significant improvements in scale, multilinguality, and architecture:

**Model Configurations:**
| Model | Hidden Size | Layers | Q Heads | KV Heads | Training Tokens |
|-------|-------------|--------|---------|----------|-----------------|
| Qwen2-0.5B | 896 | 24 | 14 | 2 | 12T |
| Qwen2-1.5B | 1,536 | 28 | 12 | 2 | 7T |
| Qwen2-7B | 3,584 | 28 | 28 | 4 | 7T |
| Qwen2-72B | 8,192 | 80 | 64 | 8 | 7T |
| Qwen2-57B-A14B (MoE) | 3,584 | 28 | 28 | 4 | 4.5T |

**Key Innovations:**
- **Grouped Query Attention (GQA):** Reduced KV cache usage for better throughput
- **Dual Chunk Attention (DCA) + YARN:** Extended context to 128K tokens
- **Fine-grained MoE experts:** 64 routed + 8 shared experts in MoE variant
- **7+ trillion training tokens:** Expanded from 3T in Qwen1

**Performance Highlights:**
- Qwen2-72B: 84.2 MMLU, 37.9 GPQA, 64.6 HumanEval, 89.5 GSM8K
- Qwen2-72B-Instruct: 9.1 MT-Bench, 48.1 Arena-Hard
- Support for ~30 languages including European, Asian, and Arabic languages

**Post-Training:**
- Collaborative data annotation with automatic ontology extraction
- Rejection sampling for math/code with execution feedback
- Direct Preference Optimization (DPO) for alignment

**Source PDF:** [[../PDF Extracts/AI Labs/Alibaba (Qwen)-Qwen2_Technical_Report_2407.10671.md|Qwen2 Technical Report]]

---

### Qwen2.5

**Release Date:** December 2024
**Paper:** [arXiv:2412.15115](https://arxiv.org/abs/2412.15115)

Qwen2.5 represents a major leap with 18 trillion training tokens and enhanced capabilities:

**Model Sizes and Configurations:**
| Model | Layers | Q/KV Heads | Context Length | Generation Length | License |
|-------|--------|------------|----------------|-------------------|---------|
| Qwen2.5-0.5B | 24 | 14/2 | 32K | 8K | Apache 2.0 |
| Qwen2.5-1.5B | 28 | 12/2 | 32K | 8K | Apache 2.0 |
| Qwen2.5-3B | 36 | 16/2 | 32K | 8K | Qwen Research |
| Qwen2.5-7B | 28 | 28/4 | 128K | 8K | Apache 2.0 |
| Qwen2.5-14B | 48 | 40/8 | 128K | 8K | Apache 2.0 |
| Qwen2.5-32B | 64 | 40/8 | 128K | 8K | Apache 2.0 |
| Qwen2.5-72B | 80 | 64/8 | 128K | 8K | Qwen |

**Training Data Improvements:**
- **Scale:** 18 trillion tokens (vs 7T in Qwen2)
- **Better filtering:** Qwen2-Instruct models as quality filters
- **Specialized data:** Integration of Qwen2.5-Math and Qwen2.5-Coder training data
- **Synthetic data:** High-quality generation using Qwen2-72B-Instruct
- **Balanced mixture:** Down-sampling overrepresented domains (e-commerce, social media)

**Post-Training Advances:**
- **Two-stage RL:** Offline RL (DPO for reasoning/factuality) + Online RL (GRPO for helpfulness)
- **1M+ SFT examples:** Covering long-sequence generation, math, coding, instruction-following
- **Long-sequence generation:** Up to 8,192 output tokens

**Key Improvements Over Qwen2:**
- Better structured data understanding (tables, JSON)
- Improved instruction following with code-based validation
- Cross-lingual transfer for low-resource languages
- Robust system instruction handling

**Proprietary Models:**
- **Qwen2.5-Turbo:** MoE model competitive with GPT-4o-mini
- **Qwen2.5-Plus:** MoE model competitive with GPT-4o

**Source PDF:** [[../PDF Extracts/AI Labs/Alibaba (Qwen)-Qwen2.5_Technical_Report_2412.15115.md|Qwen2.5 Technical Report]]

---

### Qwen3

**Release Date:** May 2025
**Paper:** [arXiv:2505.09388](https://arxiv.org/abs/2505.09388)

The latest flagship series with thinking capabilities and massive multilingual support:

**Dense Model Configurations:**
| Model | Layers | Q/KV Heads | Context Length |
|-------|--------|------------|----------------|
| Qwen3-0.6B | 28 | 16/8 | 32K |
| Qwen3-1.7B | 28 | 16/8 | 32K |
| Qwen3-4B | 36 | 32/8 | 128K |
| Qwen3-8B | 36 | 32/8 | 128K |
| Qwen3-14B | 40 | 40/8 | 128K |
| Qwen3-32B | 64 | 64/8 | 128K |

**MoE Model Configurations:**
| Model | Layers | Q/KV Heads | Total/Activated Experts | Context Length |
|-------|--------|------------|------------------------|----------------|
| Qwen3-30B-A3B | 48 | 32/4 | 128/8 | 128K |
| Qwen3-235B-A22B | 94 | 64/4 | 128/8 | 128K |

**Key Innovations:**

1. **Unified Thinking Mode:**
   - Combines reasoning (thinking) and rapid response (non-thinking) in one model
   - Dynamic mode switching based on user queries
   - Thinking budget mechanism for adaptive computational resources

2. **Architecture Updates:**
   - Removed QKV-bias (used in Qwen2)
   - Added QK-Norm for stable training
   - Global-batch load balancing loss for expert specialization

3. **Training:**
   - **36 trillion tokens** across 119 languages and dialects
   - Three-stage pre-training: General (30T) -> Reasoning (5T) -> Long Context
   - PDF text extraction using Qwen2.5-VL
   - Strong-to-weak distillation for smaller models

4. **Multilingual Expansion:**
   - 119 languages (vs 29 in Qwen2.5)
   - Enhanced cross-lingual understanding and generation

**Flagship Performance (Qwen3-235B-A22B):**
- AIME'24: 85.7
- AIME'25: 81.5
- LiveCodeBench v5: 70.7
- CodeForces: 2,056
- BFCL v3: 70.8

**Source PDF:** [[../PDF Extracts/AI Labs/Alibaba (Qwen)-Qwen3_Technical_Report_2505.09388.md|Qwen3 Technical Report]]

---

### Qwen-VL

**Release Date:** August 2023
**Paper:** [arXiv:2308.12966](https://arxiv.org/abs/2308.12966)

The first vision-language model in the Qwen family:

**Architecture:**
| Component | Parameters | Description |
|-----------|------------|-------------|
| Visual Encoder | 1.9B | ViT-bigG initialized from OpenCLIP |
| VL Adapter | 0.08B | Single-layer cross-attention, 256 queries |
| LLM (Qwen-7B) | 7.7B | Language model backbone |
| **Total** | **9.6B** | |

**Key Features:**
- **Visual Receptor:** ViT with position-aware adapter
- **Input Resolution:** 224x224 (pre-training) -> 448x448 (multi-task)
- **Bounding Box I/O:** Normalized coordinates for grounding tasks
- **Multi-image Support:** Interleaved image-text conversations

**Training Pipeline:**
1. **Stage 1 (Pre-training):** 1.4B image-text pairs from web data
2. **Stage 2 (Multi-task):** VQA, grounding, OCR, captioning tasks
3. **Stage 3 (SFT):** 350K instruction-following samples

**Capabilities:**
- Image captioning and visual question answering
- Text reading (OCR) and document understanding
- Visual grounding and object localization
- Multilingual support (English, Chinese)

**Source PDF:** [[../PDF Extracts/AI Labs/Alibaba (Qwen)-Qwen-VL_2308.12966.md|Qwen-VL Technical Report]]

---

### Qwen2-VL

**Release Date:** October 2024
**Paper:** [arXiv:2410.00520](https://arxiv.org/abs/2410.00520)

Second generation vision-language model with significant improvements:

**Model Sizes:**
- Qwen2-VL-2B
- Qwen2-VL-7B
- Qwen2-VL-72B

**Key Improvements Over Qwen-VL:**
- Dynamic resolution support (not fixed to 448x448)
- Video understanding capabilities
- Enhanced document and chart analysis
- Improved multilingual visual understanding

**Note:** The PDF extract for this paper appears to have content issues. Refer to the [official blog post](https://qwenlm.github.io/blog/qwen2-vl/) and [arXiv paper](https://arxiv.org/abs/2410.00520) for complete details.

---

### Qwen2.5-1M

**Release Date:** January 2025
**Paper:** [arXiv:2501.15383](https://arxiv.org/abs/2501.15383)

Specialized long-context variants supporting up to 1 million tokens:

**Model Configurations:**
| Model | Layers | Q/KV Heads | Context/Generation Length | License |
|-------|--------|------------|--------------------------|---------|
| Qwen2.5-7B-Instruct-1M | 28 | 28/4 | 1M / 8K | Apache 2.0 |
| Qwen2.5-14B-Instruct-1M | 48 | 40/8 | 1M / 8K | Apache 2.0 |

**Long-Context Training Techniques:**

1. **Synthetic Data for Long-Range Dependencies:**
   - Fill-in-the-Middle (FIM) tasks
   - Keyword/position-based retrieval
   - Paragraph reordering

2. **Progressive Pre-training:**
   - 5 stages: 4K -> 32K -> 64K -> 128K -> 256K
   - RoPE base frequency scaling: 10K -> 1M -> 5M -> 10M

3. **Two-Stage SFT:**
   - Stage 1: Short instructions (up to 32K)
   - Stage 2: Mixed short + long (up to 262K)

**Inference Optimizations:**

1. **Dual Chunk Attention (DCA):**
   - Remaps relative positions to avoid untrained large distances
   - Enables 4x+ context length extrapolation without training

2. **Sparse Attention (MInference-based):**
   - "Vertical-Slash" pattern for critical token selection
   - 3-7x prefill speedup at 1M context

3. **Engine Optimizations:**
   - Kernel optimization for sparse attention
   - Dynamic Chunked Pipeline Parallelism (DCPP)
   - Totally Asynchronous Generator (TAG) scheduling

**Performance:**
- Qwen2.5-14B-Instruct-1M: 92.2 on RULER at 128K, outperforms GPT-4o-mini
- Passkey retrieval: Perfect accuracy up to 1M tokens (14B model)
- Short-context tasks: Maintains parity with 128K versions

**Source PDF:** [[../PDF Extracts/AI Labs/Alibaba (Qwen)-Qwen2.5-1M_Technical_Report_2501.15383.md|Qwen2.5-1M Technical Report]]

---

## Links to Source PDFs

| Model | PDF Extract |
|-------|-------------|
| Qwen (1.0) | [[../PDF Extracts/AI Labs/Alibaba (Qwen)-Qwen_Technical_Report_2309.16609.md]] |
| Qwen-VL | [[../PDF Extracts/AI Labs/Alibaba (Qwen)-Qwen-VL_2308.12966.md]] |
| Qwen2 | [[../PDF Extracts/AI Labs/Alibaba (Qwen)-Qwen2_Technical_Report_2407.10671.md]] |
| Qwen2-VL | [[../PDF Extracts/AI Labs/Alibaba (Qwen)-Qwen2-VL_2410.00520.md]] |
| Qwen2.5 | [[../PDF Extracts/AI Labs/Alibaba (Qwen)-Qwen2.5_Technical_Report_2412.15115.md]] |
| Qwen2.5-1M | [[../PDF Extracts/AI Labs/Alibaba (Qwen)-Qwen2.5-1M_Technical_Report_2501.15383.md]] |
| Qwen3 | [[../PDF Extracts/AI Labs/Alibaba (Qwen)-Qwen3_Technical_Report_2505.09388.md]] |

---

## External Resources

- **GitHub:** [github.com/QwenLM](https://github.com/QwenLM)
- **HuggingFace:** [huggingface.co/Qwen](https://huggingface.co/Qwen)
- **ModelScope:** [modelscope.cn/organization/qwen](https://modelscope.cn/organization/qwen)
- **Blog:** [qwenlm.github.io](https://qwenlm.github.io/)
