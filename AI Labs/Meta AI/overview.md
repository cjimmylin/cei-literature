# Meta AI: Llama Model Family Overview

## Lab Overview

Meta AI (formerly Facebook AI Research/FAIR) is a leading AI research lab within Meta Platforms, Inc. headquartered in Menlo Park, California. Meta AI has distinguished itself as one of the most significant champions of open-source AI, releasing the Llama series of large language models that have democratized access to state-of-the-art AI capabilities.

### Open-Source Philosophy

Meta AI's approach to AI development emphasizes "Open Innovation" - the belief that releasing model weights openly leads to:

- **Faster innovation** through community contributions and experimentation
- **Better safety** via collective red-teaming and vulnerability discovery
- **Democratized access** enabling researchers and organizations without massive compute budgets
- **Transparency** in AI development methodologies

This philosophy stands in contrast to labs like OpenAI and Anthropic, which have shifted toward closed-source models.

---

## Timeline of Llama Models

| Date | Model | Key Milestone |
|------|-------|---------------|
| **February 2023** | LLaMA 1 | First release; 7B-65B parameters; research-only license |
| **July 2023** | Llama 2 | Commercial license; 7B-70B parameters; 2T training tokens |
| **August 2023** | Code Llama | Code-specialized variant; infilling capabilities |
| **April 2024** | Llama 3 | 8B and 70B parameters; improved tokenizer |
| **July 2024** | Llama 3.1 | Flagship 405B model; 128K context; tool use |
| **September 2024** | Llama 3.2 | Multimodal (vision) and edge models (1B, 3B) |
| **December 2024** | Llama 3.3 | 70B with 405B-class performance |
| **2025** | Llama 4 | MoE architecture; 10M context; native multimodality |

---

## Summary Table: All Models

| Model | Parameters | Training Tokens | Context Length | Architecture | Key Features |
|-------|------------|-----------------|----------------|--------------|--------------|
| LLaMA 1 (7B) | 6.7B | 1.0T | 2K | Dense Transformer | Research-only |
| LLaMA 1 (13B) | 13.0B | 1.0T | 2K | Dense Transformer | Outperforms GPT-3 (175B) |
| LLaMA 1 (33B) | 32.5B | 1.4T | 2K | Dense Transformer | - |
| LLaMA 1 (65B) | 65.2B | 1.4T | 2K | Dense Transformer | Competitive with PaLM-540B |
| Llama 2 (7B) | 7B | 2.0T | 4K | Dense Transformer | Commercial license |
| Llama 2 (13B) | 13B | 2.0T | 4K | Dense Transformer | Commercial license |
| Llama 2 (70B) | 70B | 2.0T | 4K | Dense + GQA | Grouped-Query Attention |
| Code Llama (7B-70B) | 7B-70B | 500B-1T (code) | 16K (100K extrapolated) | Dense + FIM | Infilling, Python specialist |
| Llama 3 (8B) | 8B | 15T+ | 8K | Dense + GQA | 128K vocabulary |
| Llama 3 (70B) | 70B | 15T+ | 8K | Dense + GQA | 128K vocabulary |
| Llama 3.1 (405B) | 405B | 15.6T | 128K | Dense + GQA | Flagship model, tool use |
| Llama 3.2 Vision | 11B, 90B | - | - | Multimodal | Image understanding |
| Llama 3.2 Edge | 1B, 3B | - | - | Dense | Mobile-optimized |
| Llama 3.3 (70B) | 70B | - | - | Dense + GQA | 405B-class performance |
| Llama 4 | 17B-400B+ | - | 10M | MoE | Native multimodality |

---

## Detailed Model Descriptions

### LLaMA 1 (February 2023)

**Paper:** "LLaMA: Open and Efficient Foundation Language Models" (arXiv:2302.13971)

**Overview:**
LLaMA (Large Language Model Meta AI) was the foundational release that established Meta AI's open-source LLM strategy. The key insight was that smaller models trained on more data can match or exceed the performance of larger models trained on less data.

**Architecture:**
- Standard Transformer with key improvements:
  - **Pre-normalization** using RMSNorm (inspired by GPT-3)
  - **SwiGLU activation function** (from PaLM) replacing ReLU
  - **Rotary Position Embeddings (RoPE)** instead of absolute positional embeddings
- Byte-pair encoding (BPE) tokenizer via SentencePiece

**Training Data:**
| Source | Proportion | Description |
|--------|------------|-------------|
| CommonCrawl | 67% | Filtered web crawl (2017-2020) |
| C4 | 15% | Colossal Clean Crawled Corpus |
| GitHub | 4.5% | Apache/BSD/MIT licensed code |
| Wikipedia | 4.5% | 20 languages |
| Books | 4.5% | Gutenberg + Books3 |
| ArXiv | 2.5% | Scientific papers |
| StackExchange | 2% | Q&A content |

**Key Results:**
- LLaMA-13B outperforms GPT-3 (175B) on most benchmarks despite being 10x smaller
- LLaMA-65B is competitive with Chinchilla-70B and PaLM-540B
- Trained on publicly available data only (open-source compatible)

**Source PDF:** [AI Labs/Meta AI/LLaMA/LLaMA_2302.13971.pdf](LLaMA/LLaMA_2302.13971.pdf)

---

### Llama 2 (July 2023)

**Paper:** "Llama 2: Open Foundation and Fine-Tuned Chat Models" (arXiv:2307.09288)

**Overview:**
Llama 2 represented a major leap forward with commercial licensing, doubled training data, and the introduction of chat-optimized variants (Llama 2-Chat) using RLHF.

**Key Improvements over LLaMA 1:**
- **40% more training data** (2T tokens vs 1.4T)
- **Doubled context length** (4,096 tokens vs 2,048)
- **Grouped-Query Attention (GQA)** for 34B and 70B models
- **Commercial license** enabling commercial deployment
- **RLHF fine-tuning** for Llama 2-Chat variants

**Architecture:**
| Model | Params | Context | GQA | Training Tokens |
|-------|--------|---------|-----|-----------------|
| Llama 2 7B | 7B | 4K | No | 2.0T |
| Llama 2 13B | 13B | 4K | No | 2.0T |
| Llama 2 34B | 34B | 4K | Yes | 2.0T |
| Llama 2 70B | 70B | 4K | Yes | 2.0T |

**Training Process:**
1. **Pretraining** on publicly available data
2. **Supervised Fine-Tuning (SFT)** on instruction data
3. **RLHF** using:
   - Rejection Sampling
   - Proximal Policy Optimization (PPO)

**Safety Features:**
- Extensive red-teaming
- Safety-specific data annotation
- Iterative safety evaluations
- Helpfulness vs safety balance optimization

**Source PDF:** [AI Labs/Meta AI/Llama 2/Llama_2_2307.09288.pdf](Llama%202/Llama_2_2307.09288.pdf)

---

### Code Llama (August 2023)

**Paper:** "Code Llama: Open Foundation Models for Code" (arXiv:2308.12950)

**Overview:**
Code Llama is a family of code-specialized LLMs derived from Llama 2, providing state-of-the-art performance among open models for code generation, with unique infilling capabilities and extended context support.

**Model Variants:**

| Variant | Sizes | Infilling | Description |
|---------|-------|-----------|-------------|
| Code Llama | 7B, 13B, 34B, 70B | 7B, 13B, 70B | Foundation code model |
| Code Llama - Python | 7B, 13B, 34B, 70B | No | Python-specialized |
| Code Llama - Instruct | 7B, 13B, 34B, 70B | 7B, 13B, 70B | Instruction-following |

**Training Pipeline:**
1. **Code Training** from Llama 2 foundation (500B tokens, 1T for 70B)
2. **Infilling Training** using causal masking (PSM/SPM formats)
3. **Long Context Fine-Tuning (LCFT)** - extends to 16K tokens (100K extrapolation)
4. **Python Specialization** (additional 100B tokens for Python variants)
5. **Instruction Fine-Tuning** (~5B tokens)

**Key Capabilities:**
- **Infilling:** Fill in missing code given surrounding context
- **Long Context:** Up to 100K tokens for repository-level reasoning
- **Multilingual:** Python, C++, Java, PHP, C#, TypeScript, Bash

**Benchmark Performance (pass@1):**
| Model | HumanEval | MBPP |
|-------|-----------|------|
| Code Llama 7B | 33.5% | 41.4% |
| Code Llama 34B | 48.8% | 55.0% |
| Code Llama 70B | 53.0% | 62.4% |
| Code Llama - Instruct 70B | 67.8% | 62.2% |
| Code Llama - Python 70B | 57.3% | 65.6% |

**Key Finding:** Code Llama - Python 7B outperforms Llama 2 70B on code benchmarks, demonstrating the value of specialization.

**Source PDF:** [AI Labs/Meta AI/Code Llama/Code_Llama_2308.12950.pdf](Code%20Llama/Code_Llama_2308.12950.pdf)

---

### Llama 3 and 3.1 (April-July 2024)

**Paper:** "The Llama 3 Herd of Models" (arXiv:2407.21783)

**Overview:**
Llama 3 represents a generational leap with the flagship 405B parameter model matching GPT-4 class performance. The "herd" includes models from 8B to 405B parameters with native support for multilinguality, coding, reasoning, and tool use.

**Model Family:**

| Model | Finetuned | Multilingual | Long Context | Tool Use | Release |
|-------|-----------|--------------|--------------|----------|---------|
| Llama 3 8B | No | Limited | No | No | April 2024 |
| Llama 3 8B Instruct | Yes | Limited | No | No | April 2024 |
| Llama 3 70B | No | Limited | No | No | April 2024 |
| Llama 3 70B Instruct | Yes | Limited | No | No | April 2024 |
| Llama 3.1 8B | No | Yes | Yes (128K) | No | July 2024 |
| Llama 3.1 8B Instruct | Yes | Yes | Yes (128K) | Yes | July 2024 |
| Llama 3.1 70B | No | Yes | Yes (128K) | No | July 2024 |
| Llama 3.1 70B Instruct | Yes | Yes | Yes (128K) | Yes | July 2024 |
| Llama 3.1 405B | No | Yes | Yes (128K) | No | July 2024 |
| Llama 3.1 405B Instruct | Yes | Yes | Yes (128K) | Yes | July 2024 |

**Architecture Specifications:**

| Parameter | 8B | 70B | 405B |
|-----------|-----|------|------|
| Layers | 32 | 80 | 126 |
| Model Dimension | 4,096 | 8,192 | 16,384 |
| FFN Dimension | 14,336 | 28,672 | 53,248 |
| Attention Heads | 32 | 64 | 128 |
| Key/Value Heads | 8 | 8 | 8 |
| Vocabulary Size | 128,000 | 128,000 | 128,000 |
| RoPE Base | 500,000 | 500,000 | 500,000 |

**Key Innovations:**
- **Massive Scale:** 405B model trained on 15.6T tokens using 3.8 x 10^25 FLOPs
- **New Tokenizer:** 128K vocabulary (100K from tiktoken + 28K multilingual)
- **Improved Compression:** 3.94 characters per token (vs 3.17 for Llama 2)
- **Grouped-Query Attention:** 8 KV heads for efficient inference
- **Extended Context:** 128K tokens via continued pre-training

**Training Data Mix:**
- 50% general knowledge
- 25% mathematical and reasoning
- 17% code
- 8% multilingual

**Post-Training:**
- Supervised Fine-Tuning (SFT)
- Rejection Sampling (RS)
- Direct Preference Optimization (DPO)

**Benchmark Performance (Instruct models):**

| Benchmark | Llama 3 8B | Llama 3 70B | Llama 3.1 405B | GPT-4 | GPT-4o |
|-----------|------------|-------------|----------------|-------|--------|
| MMLU (5-shot) | 69.4 | 83.6 | 87.3 | 85.1 | 89.1 |
| HumanEval | 72.6 | 80.5 | 89.0 | 86.6 | 90.2 |
| GSM8K (8-shot) | 84.5 | 95.1 | 96.8 | 94.2 | 96.1 |
| MATH (0-shot) | 51.9 | 68.0 | 73.8 | 64.5 | 76.6 |

**Multimodal Extensions (Under Development):**
- Image encoder pre-training
- Video adapter training
- Speech adapter training

**Source PDF:** [AI Labs/Meta AI/Llama 3/Llama_3_2407.21783.pdf](Llama%203/Llama_3_2407.21783.pdf)

---

## Key Architectural Features Across Generations

### Common Elements

All Llama models share core architectural choices:

1. **Pre-normalization (RMSNorm):** Normalize inputs to each transformer sub-layer
2. **SwiGLU Activation:** Superior to ReLU for language modeling
3. **Rotary Position Embeddings (RoPE):** Better generalization to sequence lengths
4. **BPE Tokenization:** Via SentencePiece (Llama 1-2) or tiktoken-based (Llama 3+)

### Evolution of Key Features

| Feature | LLaMA 1 | Llama 2 | Code Llama | Llama 3/3.1 |
|---------|---------|---------|------------|-------------|
| Context Length | 2K | 4K | 16K (100K) | 8K (128K) |
| GQA | No | 34B+ | Inherited | All sizes |
| Vocabulary | 32K | 32K | 32K | 128K |
| RoPE Base | 10,000 | 10,000 | 1,000,000 | 500,000 |
| Training Tokens | 1.0-1.4T | 2.0T | 500B-1T | 15T+ |
| Infilling | No | No | Yes (select) | No |
| Tool Use | No | No | No | Yes (3.1) |

---

## Links to Source PDFs

| Paper | arXiv ID | Local PDF |
|-------|----------|-----------|
| LLaMA: Open and Efficient Foundation Language Models | 2302.13971 | [LLaMA/LLaMA_2302.13971.pdf](LLaMA/LLaMA_2302.13971.pdf) |
| Llama 2: Open Foundation and Fine-Tuned Chat Models | 2307.09288 | [Llama 2/Llama_2_2307.09288.pdf](Llama%202/Llama_2_2307.09288.pdf) |
| Code Llama: Open Foundation Models for Code | 2308.12950 | [Code Llama/Code_Llama_2308.12950.pdf](Code%20Llama/Code_Llama_2308.12950.pdf) |
| The Llama 3 Herd of Models | 2407.21783 | [Llama 3/Llama_3_2407.21783.pdf](Llama%203/Llama_3_2407.21783.pdf) |

---

## Additional Resources

- **Official Website:** [ai.meta.com/llama](https://ai.meta.com/llama/)
- **Documentation:** [llama.meta.com/docs](https://www.llama.com/docs/overview)
- **GitHub (Llama 3+):** [github.com/meta-llama/llama-models](https://github.com/meta-llama/llama-models)
- **GitHub (Legacy):** [github.com/facebookresearch/llama](https://github.com/facebookresearch/llama)
- **HuggingFace:** [huggingface.co/meta-llama](https://huggingface.co/meta-llama)

See also: [[models|Meta AI Models]] | [[README|Meta AI Overview]]
