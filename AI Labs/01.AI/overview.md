# 01.AI Overview

## Lab Overview

01.AI is a Chinese artificial intelligence startup founded by **Kai-Fu Lee**, the renowned AI scientist, venture capitalist, and former president of Google China. Headquartered in Beijing, China, the company focuses on building frontier-class foundation models that are optimized for both English and Chinese languages.

The company's core philosophy centers on data quality over quantity, believing that thoroughly engineered high-quality data combined with classical transformer architectures can achieve advanced capabilities without significant architectural modifications. This approach has enabled 01.AI to develop models that match or exceed GPT-3.5 performance while remaining deployable on consumer-grade hardware.

**Key Resources:**
- Code: https://github.com/01-ai/Yi
- Models: https://huggingface.co/01-ai
- Official Website: https://01.ai

---

## Yi Model Family Summary

The Yi model family represents 01.AI's primary contribution to open-source AI. The family includes language models, vision-language models, long-context models, and code-specialized variants. All models share the core design philosophy of prioritizing data quality and efficient architecture.

| Model Variant | Parameters | Key Capability | Release |
|---------------|------------|----------------|---------|
| Yi-6B/34B | 6B, 34B | Bilingual foundation models | Nov 2023 |
| Yi-9B | 9B | Depth-upscaled enhanced model | 2024 |
| Yi-Chat | 6B, 34B | Instruction-following chat models | Nov 2023 |
| Yi-200K | 6B, 34B | Extended 200K context window | 2024 |
| Yi-VL | 6B, 34B | Vision-language multimodal | 2024 |
| Yi-1.5 | 6B, 9B, 34B | Improved reasoning and coding | 2024 |
| Yi-Coder | 1.5B, 9B | Code-specialized models | Sept 2024 |
| Yi-Lightning | - | Flagship frontier model (MoE) | Dec 2024 |

---

## Detailed Model Information

### Yi-6B and Yi-34B (Base Models)

**Release:** November 2023
**Architecture:** Decoder-only Transformer with modifications

The Yi base models are pretrained language models trained on 3.1 trillion tokens of high-quality English and Chinese corpora. The 34B model was specifically designed to balance performance with deployability on consumer-grade hardware like RTX 4090 GPUs (24GB VRAM).

#### Architecture Details

| Parameter | Yi-6B | Yi-34B |
|-----------|-------|--------|
| Hidden Size | 4096 | 7168 |
| Query Heads | 32 | 56 |
| KV Heads | 4 | 8 |
| Layers | 32 | 60 |
| Pretrain Seq. Length | 4096 | 4096 |
| Max Learning Rate | 3e-4 | 1.5e-4 |

**Key Architectural Features:**
- **Grouped-Query Attention (GQA):** Applied to both 6B and 34B models for reduced memory and computation costs
- **SwiGLU Activation:** Post-attention layer with reduced activation size (8/3h instead of 4h)
- **Rotary Position Embedding (RoPE):** With adjusted base frequency for long-context support
- **Vocabulary Size:** 64,000 tokens using byte-pair encoding (BPE)

#### Pretraining Data

The pretraining corpus consists of 3.1 trillion high-quality tokens in English and Chinese, processed through a sophisticated multi-stage pipeline:

1. **Language Identification:** CCNet pipeline for language detection and perplexity scoring
2. **Heuristic Filtering:** URL/domain blocklists, document length, special symbol ratios, repetition detection
3. **Learned Filters:** Perplexity scorer, quality scorer, safety scorer, document coherence scorer
4. **Cluster-based Filtering:** Unsupervised semantic clustering for quality assessment
5. **Deduplication:** Document-level MinHash and sub-document exact-match deduplication

#### Benchmark Performance

| Benchmark | Yi-6B | Yi-34B | GPT-3.5 |
|-----------|-------|--------|---------|
| MMLU | 63.2 | 76.3 | 69.1 |
| C-Eval | 72.0 | 81.4 | 52.5 |
| CMMLU | 75.5 | 83.7 | 55.5 |
| GSM8K | 32.5 | 67.2 | 57.1 |
| HumanEval (pass@1) | 15.9 | 23.2 | 48.1 |
| MBPP (pass@1) | 26.3 | 41.0 | 61.4 |

---

### Yi-Chat (Instruction-Tuned Models)

**Finetuning Philosophy:** Quality over quantity

Yi-Chat models are finetuned from the base models using a carefully curated dataset of **less than 10,000** instruction-response pairs. This approach follows the LIMA methodology, where each training instance is manually examined and polished by machine learning engineers over multiple iterations.

**Finetuning Techniques:**
- **Data Format:** ChatML-style format for clear differentiation between system, user, and assistant roles
- **Compound Instructions:** Progressively evolved complexity inspired by WizardLM
- **Chain-of-Thought:** "Step-Back" pattern for abstract reasoning before detailed answers
- **Hallucination Reduction:** Careful verification that knowledge is within model capability
- **Repetition Reduction:** Manual rewriting of repetitive turns in training data

**Training Hyperparameters:**
- Optimizer: AdamW (beta1=0.9, beta2=0.999, epsilon=1e-8)
- Sequence Length: 4096
- Batch Size: 64
- Training Steps: 300
- Learning Rate: 1e-5 (constant)
- NEFTune Noise: 45 (Yi-34B-Chat), 5 (Yi-6B-Chat)

**Human Evaluation Results (December 2023):**

| Model | AlpacaEval | LMSys Chatbot Arena | SuperClue |
|-------|------------|---------------------|-----------|
| GPT-4-Turbo | 97.7 | 1243 | 89.79 |
| Yi-34B-Chat | 94.08 | 1110 | 71.87 |
| LLaMA2-Chat-70B | 92.66 | 1077 | - |
| GPT-3.5-Turbo | 89.37 | 1117 | 59.39 |

---

### Yi-200K (Long Context Models)

Yi-200K extends the context window from 4K to 200K tokens through lightweight continual pretraining and finetuning.

**Training Approach:**
- **Continual Pretraining:** ~5B tokens with length-upsampled data (mostly from books)
- **Synthetic Data:** Multi-document QA pairs with recitation-before-answer format
- **Architecture:** Full attention (no sparse or linear attention modifications)
- **Implementation:** Sequence parallelism and distributed attention

**Key Insight:** The capability to model longer dependencies than the pretrained length is viewed as an intrinsic capability of the base model that post-training simply "unlocks."

**Needle-in-a-Haystack Performance:** Near-perfect retrieval across the full 200K context window.

**MMLU Retention:** Extending to 200K context causes minimal degradation:
- Yi-34B 4K: 76.32 average
- Yi-34B 200K: 75.56 average (only -0.76)

---

### Yi-VL (Vision-Language Models)

Yi-VL integrates vision understanding into the Yi language models, inspired by LLaVA architecture.

**Architecture Components:**
1. **Vision Transformer (ViT):** Initialized from CLIP ViT-H/14
2. **Projection Module:** Two-layer MLP with layer normalizations
3. **Language Model:** Yi-Chat models (6B or 34B)

**Three-Stage Training Process:**

| Stage | Resolution | Data | Trainable Components |
|-------|------------|------|---------------------|
| 1 | 224x224 | 100M pairs from LAION-400M | ViT + Projection |
| 2 | 448x448 | 20M pairs + 4.8M diverse sources | ViT + Projection |
| 3 | 448x448 | ~1M pairs (GQA, VizWiz, etc.) | Full model |

**MMMU Benchmark Performance (at release):**

| Model | Overall | Art | Business | Science | Health | Society | Engineering |
|-------|---------|-----|----------|---------|--------|---------|-------------|
| GPT-4V | 55.7 | 65.3 | 64.3 | 48.4 | 63.5 | 76.3 | 41.7 |
| Yi-VL-34B | 41.6 | 56.1 | 33.3 | 32.9 | 45.9 | 66.5 | 36.0 |
| Yi-VL-6B | 37.8 | 53.4 | 30.3 | 30.0 | 39.3 | 58.5 | 34.1 |

---

### Yi-9B (Depth-Upscaled Model)

Yi-9B demonstrates the effectiveness of depth upscaling for improving model performance without training from scratch.

**Method:**
- Starting point: Yi-6B (32 layers)
- Upscaling: Duplicate middle layers 12-28 to create 48-layer model
- Result: Yi-9B (9 billion parameters)
- Continual training: ~800B tokens

**Layer Selection Insight:** Layers to replicate are chosen based on cosine similarity between layer inputs and outputs. High similarity (approaching 1.0) between duplicated layer inputs/outputs ensures minimal output disruption.

**Performance Comparison:**

| Benchmark | Yi-6B | Yi-9B Init | Yi-9B (trained) |
|-----------|-------|------------|-----------------|
| MMLU | 63.2 | 63.0 | 68.4 |
| GSM8K | 32.5 | 31.3 | 52.3 |
| MATH | 4.6 | 4.1 | 15.9 |
| HumanEval | 15.9 | 12.8 | 39.0 |
| MBPP | 26.3 | 25.8 | 54.4 |

The dramatic improvements in math and code after continual training demonstrate the effectiveness of depth upscaling combined with targeted data.

---

### Yi-Coder (Code-Specialized Models)

**Release:** September 5, 2024
**Model Variants:** Yi-Coder-1.5B, Yi-Coder-9B (Base and Chat)

Yi-Coder represents a specialized code generation series delivering state-of-the-art coding performance with fewer than 10 billion parameters.

**Key Features:**
- **52 Programming Languages:** Comprehensive support across major programming paradigms
- **128K Context Window:** Extended context for large codebase understanding
- **State-of-the-Art Performance:** Yi-Coder-9B-Chat achieves 23% pass rate on LiveCodeBench, the only model under 10B parameters to exceed 20%

**Benchmark Results:**
- **LiveCodeBench:** 23% (outperforms DeepSeekCoder-33B-Ins at 22.3%)
- **Multi-lingual HumanEval (9B):** 49.6% average across languages
- **Math Programming:** 70.3% average across GSM8k, MATH, TabMWP, MAWPS
- **CodeEditorBench:** 78.57% win rate across debug, translation, and refactoring

**Documentation:** [Yi-Coder/Yi-Coder_Documentation.md](Yi-Coder/Yi-Coder_Documentation.md)

---

### Yi-Lightning (Flagship Frontier Model)

**Release:** December 2024
**Technical Report:** arXiv:2412.01253

Yi-Lightning is 01.AI's flagship frontier model featuring an enhanced Mixture-of-Experts (MoE) architecture designed to compete with GPT-4o and Claude 3.5 Sonnet.

**Architecture Highlights:**
- **Enhanced MoE Design:** Advanced expert segmentation and routing mechanisms
- **Optimized KV-Caching:** Improved memory efficiency for inference
- **Expanded Vocabulary:** 100,352 tokens (increased from 64K for better multilingual support)
- **RAISE Safety Framework:** Four-component Responsible AI Safety Engine

**Training Methodology:**
1. **Pre-training:** Multilingual corpus (web documents, books, academic papers, codebases, Q&A pairs) through early 2024
2. **Supervised Fine-Tuning (SFT):** Multi-stage training with synthetic data construction
3. **RLHF:** Reinforcement learning with optimized reward modeling

**Chatbot Arena Performance:**
- **Overall Ranking:** 6th place
- **Specialized Categories (2nd-4th place):**
  - Chinese language tasks
  - Math and reasoning
  - Coding challenges
  - Hard prompts

**Availability:** Commercial API only (https://platform.lingyiwanwu.com) - not available as open-weights

**Technical Report:** [Papers/Yi-Lightning_Technical_Report_2412.01253.pdf](Papers/Yi-Lightning_Technical_Report_2412.01253.pdf)

---

## Infrastructure and Safety

### Training Infrastructure

01.AI developed full-stack infrastructure for pretraining, finetuning, and serving:

- **Multi-Cloud Scheduling:** Elastic task scheduling across clusters with automatic scaling
- **Failure Recovery:** Automated inspection, prediction, and recovery for hardware/software errors
- **Memory Optimization:** ZeRO-1, tensor parallelism, pipeline parallelism, flash attention
- **Finetuning Framework:** Hierarchical scheduling supporting heterogeneous backends (Megatron + DeepSpeed)
- **Inference:** 4-bit model quantization, 8-bit KV cache quantization, PagedAttention, dynamic batching

### Responsible AI Safety Engine (RAISE)

**Safety in Pretraining:**
- Filters based on heuristic rules, keyword matching, and learned classifiers
- Removal of personal identifiers and private data
- Reduction of sexual, violent, and extremist content

**Safety in Alignment:**
- Comprehensive taxonomy covering: environmental issues, superstition, religious sensitivities, discrimination, substance abuse, violence, illegal activities, hate speech, ethical violations, privacy breaches, self-harm, sexually explicit content, mental health issues, and cybersecurity threats
- Attack simulation prompts for improved resilience

---

## Key Takeaways

1. **Data Quality Emphasis:** Training on 3.1T high-quality tokens outperforms larger but lower-quality datasets
2. **Post-Chinchilla Optimal:** Overtraining (more tokens than compute-optimal) improves inference efficiency
3. **Quantization-Friendly:** 4-bit and 8-bit quantization with near-zero performance degradation enables consumer deployment
4. **Small-Scale Finetuning:** Less than 10K carefully curated examples can match performance of million-scale instruction datasets
5. **Depth Upscaling:** Cost-effective method for improving model performance through layer duplication and continual training

---

## Source Documents

| Document | Type | Location |
|----------|------|----------|
| Yi-Lightning Technical Report (arXiv:2412.01253) | Research Paper | [PDF](Papers/Yi-Lightning_Technical_Report_2412.01253.pdf) / [Extract](Papers/Yi-Lightning_Technical_Report_2412.01253.md) |
| Yi Technical Report (arXiv:2403.04652) | Research Paper | [PDF](Papers/Yi_Technical_Report_2403.04652.pdf) / [Extract](Papers/Yi_Technical_Report_2403.04652.md) |
| Yi-Coder Documentation | Technical Documentation | [Yi-Coder/Yi-Coder_Documentation.md](Yi-Coder/Yi-Coder_Documentation.md) |
| Yi-VL Documentation | Technical Documentation | [Yi-VL/Yi-VL_Documentation.md](Yi-VL/Yi-VL_Documentation.md) |

**Citations:**
```bibtex
@article{yi2024lightning,
  title={Yi-Lightning Technical Report},
  author={01.AI},
  journal={arXiv preprint arXiv:2412.01253},
  year={2024}
}

@article{yi2024,
  title={Yi: Open Foundation Models by 01.AI},
  author={01.AI},
  journal={arXiv preprint arXiv:2403.04652},
  year={2024}
}
```
