# DeepSeek AI - Model Overview

## Lab Overview

DeepSeek AI is a Chinese artificial intelligence research lab founded in 2023 that has rapidly emerged as a leading developer of open-source large language models. The lab is known for its innovative approaches to model architecture, particularly its development of the Mixture-of-Experts (MoE) framework and Multi-head Latent Attention (MLA), which enable training strong models at economical costs while maintaining efficient inference. DeepSeek has consistently released cutting-edge models that rival or exceed closed-source alternatives from major AI labs while maintaining open-source accessibility.

Key research themes:
- **Efficient Architecture**: MoE with fine-grained expert segmentation, MLA for KV cache compression
- **Scalable Training**: FP8 mixed precision, DualPipe parallelism, auxiliary-loss-free load balancing
- **Reasoning Enhancement**: Group Relative Policy Optimization (GRPO), reinforcement learning from scratch
- **Domain Specialization**: Dedicated models for code, mathematics, theorem proving, and vision-language tasks

---

## Model Timeline

| Date | Model | Parameters | Key Innovation |
|------|-------|-----------|----------------|
| Jan 2024 | DeepSeek LLM | 7B, 67B | Scaling laws research, 2T token training |
| Jan 2024 | DeepSeek-Coder | 1.3B-33B | Repository-level code training, 87 languages |
| Jan 2024 | DeepSeekMoE | 2B, 16B, 145B | Fine-grained expert segmentation, shared expert isolation |
| Feb 2024 | DeepSeekMath | 7B | 120B math tokens, GRPO algorithm |
| Mar 2024 | DeepSeek-VL | 1.3B, 7B | Hybrid vision encoder, 1024x1024 resolution |
| May 2024 | DeepSeek-Prover | 7B | Synthetic theorem proving data, Lean 4 |
| May 2024 | DeepSeek-V2 | 236B (21B active) | MLA + DeepSeekMoE, 128K context |
| Aug 2024 | DeepSeek-Prover-V1.5 | 7B | RLPAF, Monte-Carlo tree search |
| Dec 2024 | DeepSeek-VL2 | 1.0B-4.5B active | Dynamic tiling, MoE vision-language |
| Dec 2024 | DeepSeek-V3 | 671B (37B active) | Auxiliary-loss-free balancing, multi-token prediction |
| Jan 2025 | DeepSeek-R1 | 671B (37B active) | Pure RL reasoning, emergent chain-of-thought |

---

## Summary Table

| Model | Total Params | Active Params | Architecture | Context | Training Data | Key Benchmarks |
|-------|-------------|---------------|--------------|---------|---------------|----------------|
| DeepSeek LLM | 7B, 67B | Dense | Transformer | 4K | 2T tokens | Surpasses LLaMA2-70B |
| DeepSeek-Coder | 1.3B-33B | Dense | Transformer + FIM | 16K | 2T tokens (87 languages) | Beats GPT-3.5 Turbo |
| DeepSeekMoE | 16B | 2.8B | Fine-grained MoE | 4K | 2T tokens | Matches LLaMA2-7B at 40% compute |
| DeepSeekMath | 7B | Dense | Transformer | 4K | 120B math tokens | 51.7% on MATH |
| DeepSeek-VL | 7B | Dense | Hybrid vision encoder | - | Multi-source VL | SOTA on VL benchmarks |
| DeepSeek-Prover | 7B | Dense | Transformer | - | 8M synthetic proofs | 52% on miniF2F |
| DeepSeek-V2 | 236B | 21B | MLA + DeepSeekMoE | 128K | 8.1T tokens | Top open-source MoE |
| DeepSeek-Prover-V1.5 | 7B | Dense | Transformer + MCTS | - | Enhanced proofs | 63.5% on miniF2F |
| DeepSeek-VL2 | 3B-27B | 1.0B-4.5B | MoE + Dynamic Tiling | - | Enhanced VL data | SOTA VL with visual grounding |
| DeepSeek-V3 | 671B | 37B | MLA + DeepSeekMoE | 128K | 14.8T tokens | Rivals GPT-4o, Claude-3.5 |
| DeepSeek-R1 | 671B | 37B | MLA + DeepSeekMoE | 128K | RL training | 79.8% on AIME 2024 |

---

## Detailed Model Descriptions

### DeepSeek LLM (V1)

**Paper**: DeepSeek LLM: Scaling Open-Source Language Models with Longtermism
**arXiv**: 2401.02954
**Released**: January 2024

DeepSeek LLM represents the foundational model series, available in 7B and 67B parameter configurations. The project focused on establishing scaling laws for open-source models and demonstrated that with proper hyperparameter tuning, smaller models can achieve competitive performance.

**Key Features**:
- Trained on 2 trillion tokens of curated data (primarily English and Chinese)
- Multi-step learning rate scheduler (enables continual training)
- Grouped-Query Attention (GQA) in 67B model for efficient inference
- Architecture follows LLaMA with modifications for pipeline partitioning

**Performance**:
- DeepSeek 67B surpasses LLaMA-2 70B across benchmarks
- Superior performance in code, mathematics, and reasoning
- DeepSeek 67B Chat outperforms GPT-3.5 in open-ended evaluations

**Source PDF**: [[DeepSeek_LLM_arxiv_2401.02954.pdf]]

---

### DeepSeek-V2

**Paper**: DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model
**arXiv**: 2405.04434
**Released**: May 2024

DeepSeek-V2 introduced two breakthrough architectural innovations: Multi-head Latent Attention (MLA) and the DeepSeekMoE framework. This combination enables both economical training and efficient inference.

**Architecture**:
- **Total Parameters**: 236B
- **Activated Parameters**: 21B per token
- **Context Length**: 128K tokens
- **Multi-head Latent Attention (MLA)**: Compresses KV cache into latent vectors, reducing cache by 93.3%
- **DeepSeekMoE**: Fine-grained expert segmentation with shared expert isolation

**Key Innovations**:
- Low-rank key-value joint compression for efficient inference
- Device-limited routing for balanced computation across GPUs
- 42.5% reduction in training costs vs. DeepSeek 67B
- 5.76x improvement in maximum generation throughput

**Performance**:
- Top-tier performance among open-source models with only 21B activated parameters
- DeepSeek-V2 Chat achieves 38.9 win rate on AlpacaEval 2.0
- Outperforms all open-source models on AlignBench (Chinese)

**Source PDF**: [[DeepSeek-V2_arxiv_2405.04434.pdf]]

---

### DeepSeek-V3

**Paper**: DeepSeek-V3 Technical Report
**arXiv**: 2412.19437
**Released**: December 2024

DeepSeek-V3 represents a massive scale-up of the DeepSeek architecture, achieving performance comparable to leading closed-source models at a fraction of the training cost.

**Architecture**:
- **Total Parameters**: 671B
- **Activated Parameters**: 37B per token
- **Context Length**: 128K tokens
- **Training Data**: 14.8T tokens

**Key Innovations**:
- **Auxiliary-loss-free load balancing**: Minimizes performance degradation from load balancing
- **Multi-token prediction (MTP)**: Enhances performance and enables speculative decoding
- **FP8 mixed precision training**: First validation at extremely large scale
- **DualPipe algorithm**: Efficient pipeline parallelism with near-zero communication overhead

**Training Efficiency**:
- Only 2.788M H800 GPU hours for full training (~$5.576M)
- No irrecoverable loss spikes or rollbacks during training
- 180K GPU hours per trillion tokens

**Performance**:
- 88.5 on MMLU, 75.9 on MMLU-Pro, 59.1 on GPQA
- 90.2% on MATH-500 (outperforms o1-preview)
- Rivals GPT-4o and Claude-3.5-Sonnet

**Source PDF**: [[DeepSeek-V3_arxiv_2412.19437.pdf]]

---

### DeepSeek-R1

**Paper**: DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
**arXiv**: 2501.12948
**Released**: January 2025

DeepSeek-R1 demonstrates that reasoning capabilities can emerge through pure reinforcement learning without supervised fine-tuning on human-annotated reasoning traces.

**Architecture**:
- Built on DeepSeek-V3-Base
- Uses Group Relative Policy Optimization (GRPO)
- **DeepSeek-R1-Zero**: Trained with RL only (no SFT)
- **DeepSeek-R1**: Multi-stage pipeline with rejection sampling, RL, and SFT

**Key Innovations**:
- **Pure RL reasoning**: Develops advanced reasoning patterns autonomously
- **Emergent behaviors**: Self-reflection, verification, dynamic strategy adaptation
- **"Aha moment"**: Model spontaneously develops reflective reasoning (e.g., "Wait, let me reconsider...")
- **Rule-based rewards**: Accuracy + format rewards without neural reward models

**Performance**:
- 79.8% on AIME 2024 (vs. 15.6% initial)
- 97.3% on MATH-500
- 96.3 percentile on Codeforces
- 49.2% on SWE-Bench Verified

**Distilled Models**: Available in 1.5B, 7B, 8B, 14B, 32B, and 70B sizes

**Source PDF**: [[DeepSeek-R1_arxiv_2501.12948.pdf]]

---

### DeepSeek-Coder

**Paper**: DeepSeek-Coder: When the Large Language Model Meets Programming
**arXiv**: 2401.14196
**Released**: January 2024

DeepSeek-Coder is a family of open-source code models trained from scratch on 2 trillion tokens, supporting 87 programming languages.

**Model Sizes**: 1.3B, 6.7B, 7B, 33B (Base and Instruct versions)

**Key Features**:
- **Repository-level training**: First to incorporate project-level dependencies during pre-training
- **Fill-in-the-Middle (FIM)**: Enhanced code completion capabilities
- **16K context length**: Handles complex, extensive coding tasks
- **87 programming languages**: Comprehensive language coverage

**Data Composition**:
- 87% source code
- 10% English code-related natural language
- 3% Chinese natural language

**Performance**:
- DeepSeek-Coder-Base 33B: SOTA among open-source code models
- DeepSeek-Coder-Instruct 33B: Surpasses GPT-3.5 Turbo
- 7B model competitive with CodeLlama-33B

**Source PDF**: [[DeepSeek-Coder_arxiv_2401.14196.pdf]]

---

### DeepSeekMath

**Paper**: DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models
**arXiv**: 2402.03300
**Released**: February 2024

DeepSeekMath 7B achieves near-GPT-4 level mathematical reasoning through careful data curation and the introduction of GRPO.

**Architecture**:
- **Parameters**: 7B
- **Base Model**: DeepSeek-Coder-Base-v1.5 7B
- **Training Data**: 120B math-related tokens from Common Crawl

**Key Innovations**:
- **DeepSeekMath Corpus**: 120B tokens (7x Minerva, 9x OpenWebMath)
- **Group Relative Policy Optimization (GRPO)**: Efficient RL algorithm without critic model
- **Code-before-math training**: Improves mathematical reasoning capabilities

**Performance**:
- 51.7% on MATH benchmark (competition-level)
- 88.2% on GSM8K after RL
- Approaches Gemini-Ultra and GPT-4 performance
- Self-consistency over 64 samples: 60.9% on MATH

**Key Finding**: Code training prior to math training improves reasoning abilities

**Source PDF**: [[DeepSeekMath_arxiv_2402.03300.pdf]]

---

### DeepSeek-Prover

**Paper**: DeepSeek-Prover: Advancing Theorem Proving in LLMs through Large-Scale Synthetic Data
**arXiv**: 2405.14333
**Released**: May 2024

DeepSeek-Prover generates large-scale synthetic theorem proving data to train models for formal mathematics in Lean 4.

**Architecture**:
- **Base Model**: DeepSeekMath-Base 7B
- **Training Data**: 8 million synthetic formal statements with proofs

**Key Innovations**:
- **Autoformalization pipeline**: Converts informal math problems to formal Lean 4 statements
- **Quality filtering**: Model scoring + hypothesis rejection
- **Parallel proving**: Proves both statements and their negations concurrently
- **Iterative enhancement**: Progressive refinement of synthetic data quality

**Performance**:
- 46.3% pass@64 on miniF2F test (whole-proof generation)
- 52% cumulative accuracy on miniF2F
- Surpasses GPT-4 (23.0%) and tree search RL methods (41.0%)
- Solved 5/148 problems on FIMO benchmark (GPT-4: 0)

**Source PDF**: [[DeepSeek-Prover_arxiv_2405.14333.pdf]]

---

### DeepSeek-Prover-V1.5

**Paper**: DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search
**arXiv**: 2408.08152
**Released**: August 2024

DeepSeek-Prover-V1.5 enhances theorem proving through RLPAF and a novel Monte-Carlo tree search algorithm.

**Key Innovations**:
- **RLPAF**: Reinforcement Learning from Proof Assistant Feedback
- **RMaxTS**: Monte-Carlo tree search with intrinsic-reward-driven exploration
- **Truncate-and-resume mechanism**: Integrates proof-step and whole-proof generation
- **Chain-of-thought comments**: Natural language reasoning aligned with Lean 4 code

**Performance**:
- **miniF2F-test**: 63.5% (new SOTA, +10.2% over V1)
- **ProofNet-test**: 25.3% (new SOTA)
- Single-pass: 60.2% on miniF2F-test

**Source PDF**: [[DeepSeek-Prover-V1.5_arxiv_2408.08152.pdf]]

---

### DeepSeek-VL

**Paper**: DeepSeek-VL: Towards Real-World Vision-Language Understanding
**arXiv**: 2403.05525
**Released**: March 2024

DeepSeek-VL is an open-source Vision-Language Model designed for real-world applications.

**Model Sizes**: 1.3B, 7B

**Architecture**:
- **Hybrid vision encoder**: Combines text-aligned (384x384) and high-resolution (1024x1024) encoders
- **576 tokens per image**: Balanced visual representation and token economy
- **Maintains LLM capabilities**: 70%+ language data during pretraining

**Key Features**:
- **Real-world data**: Web screenshots, PDFs, OCR, charts, knowledge-based content
- **Use case taxonomy**: Instruction tuning based on real user scenarios
- **Modality warm-up**: Gradual incorporation of vision-language data

**Capabilities**:
- Document/chart understanding
- OCR and formula recognition
- Scientific literature analysis
- Embodied intelligence scenarios

**Source PDF**: [[DeepSeek-VL_arxiv_2403.05525.pdf]]

---

### DeepSeek-VL2

**Paper**: DeepSeek-VL2: Mixture-of-Experts Vision-Language Models for Advanced Multimodal Understanding
**arXiv**: 2412.10302
**Released**: December 2024

DeepSeek-VL2 combines MoE architecture with dynamic high-resolution vision encoding.

**Model Variants**:
| Variant | Activated Params | Total Params | LLM Base |
|---------|-----------------|--------------|----------|
| Tiny | 1.0B | 3B | DeepSeekMoE 3B |
| Small | 2.8B | 16B | DeepSeekMoE 16B |
| Full | 4.5B | 27B | DeepSeekMoE 27B |

**Architecture**:
- **Dynamic tiling**: Processes high-resolution images with varying aspect ratios
- **DeepSeekMoE LLM**: With Multi-head Latent Attention (MLA)
- **SigLIP-SO400M-384**: Vision encoder with up to 9 tiles

**New Capabilities**:
- Visual grounding with bounding boxes
- GUI perception
- Enhanced OCR and document understanding
- In-context visual grounding

**Source PDF**: [[DeepSeek-VL2_arxiv_2412.10302.pdf]]

---

### DeepSeekMoE

**Paper**: DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models
**arXiv**: 2401.06066
**Released**: January 2024

DeepSeekMoE introduces architectural innovations for achieving ultimate expert specialization in MoE models.

**Model Sizes**: 2B, 16B, 145B

**Key Innovations**:

1. **Fine-Grained Expert Segmentation**:
   - Splits experts into smaller, more specialized units
   - Increases combinatorial flexibility (120 combinations -> 4.4 billion)
   - Enables more precise knowledge acquisition

2. **Shared Expert Isolation**:
   - Dedicated experts for common knowledge
   - Reduces redundancy among routed experts
   - Improves parameter efficiency

**Performance**:
- DeepSeekMoE 2B matches GShard 2.9B (1.5x parameters)
- DeepSeekMoE 16B achieves LLaMA2-7B performance at 40% compute
- DeepSeekMoE 145B comparable to DeepSeek 67B at 28.5% compute

**Load Balancing**:
- Expert-level balance loss
- Device-level balance loss for distributed training

**Source PDF**: [[DeepSeek-MoE_arxiv_2401.06066.pdf]]

---

## Source PDFs

All technical reports are available in:
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/PDFs/AI Labs/DeepSeek/Papers/`

Extracted text versions:
- `/Users/jimmy.lin/Documents/CEI-Literature-Vault/PDF Extracts/AI Labs/`

---

## References

1. DeepSeek LLM - arxiv:2401.02954
2. DeepSeek-Coder - arxiv:2401.14196
3. DeepSeekMoE - arxiv:2401.06066
4. DeepSeekMath - arxiv:2402.03300
5. DeepSeek-VL - arxiv:2403.05525
6. DeepSeek-Prover - arxiv:2405.14333
7. DeepSeek-V2 - arxiv:2405.04434
8. DeepSeek-Prover-V1.5 - arxiv:2408.08152
9. DeepSeek-VL2 - arxiv:2412.10302
10. DeepSeek-V3 - arxiv:2412.19437
11. DeepSeek-R1 - arxiv:2501.12948
