# Microsoft Research - AI Models Overview

## Lab Overview

Microsoft Research (MSR) is the research division of Microsoft Corporation, founded in 1991. MSR has been at the forefront of large language model research, pioneering both massive-scale models (like Megatron-Turing NLG with 530B parameters) and highly efficient small language models (the Phi series). Their research philosophy emphasizes:

- **Data Quality over Scale**: Demonstrating that carefully curated training data can enable smaller models to match larger ones
- **Efficient Deployment**: Creating models small enough to run locally on phones while maintaining competitive performance
- **Reasoning Capabilities**: Teaching smaller models sophisticated reasoning strategies rather than simple imitation
- **Responsible AI**: Incorporating safety alignment, red-teaming, and ethical guidelines across all models

## Timeline of Models

| Year | Model | Parameters | Key Achievement |
|------|-------|------------|-----------------|
| 2020 | Turing-NLG | 17B | One of the earliest massive-scale language models |
| 2022 | Megatron-Turing NLG | 530B | Largest monolithic transformer model (collaboration with NVIDIA) |
| 2023 | Phi-1 | 1.3B | "Textbooks Are All You Need" - breakthrough code generation |
| 2023 | Phi-1.5 | 1.3B | Common sense reasoning comparable to 5x larger models |
| 2023 | WizardLM | Various | Evol-Instruct: progressively complex instruction following |
| 2023 | WizardCoder | Various | Code generation surpassing Claude and Bard |
| 2023 | WizardMath | 70B | Mathematical reasoning outperforming GPT-3.5-Turbo |
| 2023 | Orca | 13B | Progressive learning from explanation traces |
| 2023 | Orca 2 | 7B, 13B | Cautious reasoning - teaching models to select strategies |
| 2023 | Phi-2 | 2.7B | Data quality focus - surpassing 7B+ models |
| 2024 | Phi-3 | 3.8B-14B | Phone-deployable model rivaling GPT-3.5 |
| 2024 | Phi-3.5 | 3.8B-42B | MoE variant, Vision capabilities, 128K context |
| 2024-25 | Phi-4 | 3.8B-14B | Advanced reasoning, multimodal, o3-mini-guided training |

## Summary Table of All Models

| Model | Size | Architecture | Context | Key Feature | Release |
|-------|------|--------------|---------|-------------|---------|
| **Megatron-Turing NLG** | 530B | Transformer decoder | 2K | 3D parallelism training | Feb 2022 |
| **Orca** | 13B | LLaMA-based | 4K | Explanation tuning | Jun 2023 |
| **Orca 2** | 7B, 13B | LLaMA-2-based | 4K | Cautious reasoning | Nov 2023 |
| **Phi-3-mini** | 3.8B | Transformer decoder | 4K/128K | Phone deployment | Apr 2024 |
| **Phi-3-small** | 7B | Transformer decoder | 8K | Blocksparse attention | Apr 2024 |
| **Phi-3-medium** | 14B | Transformer decoder | 4K | Data optimal regime | Apr 2024 |
| **Phi-3.5-mini** | 3.8B | Transformer decoder | 128K | Enhanced multilingual | Aug 2024 |
| **Phi-3.5-MoE** | 16x3.8B (6.6B active) | MoE | 128K | Mixture-of-Experts | Aug 2024 |
| **Phi-3.5-Vision** | 4.2B | CLIP + Phi-3.5-mini | - | Multi-image reasoning | Aug 2024 |

---

## Phi-3 Series

### Overview
The Phi-3 family represents Microsoft's groundbreaking work on small language models that achieve performance comparable to much larger models through high-quality data curation and synthetic data generation.

### Key Innovation: Data Optimal Regime
Unlike traditional scaling laws that assume fixed data sources, Phi-3 demonstrates that:
- Heavily filtered web data combined with LLM-generated synthetic data enables dramatic efficiency gains
- A 3.8B parameter model can match Mixtral 8x7B (45B parameters) and GPT-3.5
- Quality of training data matters more than quantity for smaller models

### Model Variants

#### Phi-3-mini (3.8B)
- **Architecture**: Transformer decoder, similar to Llama-2
- **Training**: 3.3T tokens on filtered web + synthetic data
- **Context**: 4K default, 128K via LongRope
- **Tokenizer**: 32,064 vocabulary (Llama-2 compatible)
- **Key Result**: 69% MMLU, 8.38 MT-bench
- **Deployment**: Runs on iPhone 14 (4-bit quantized, ~1.8GB, 12+ tokens/sec)

#### Phi-3-small (7B)
- **Architecture**: 32 heads, 32 layers, hidden size 4096
- **Training**: 4.8T tokens with 10% additional multilingual data
- **Key Features**:
  - tiktoken tokenizer (100,352 vocabulary)
  - Grouped-query attention (4 queries per key)
  - Novel blocksparse attention for efficient long context
  - GEGLU activation
  - Maximal Update Parametrization (muP)
- **Key Result**: 75% MMLU, 8.7 MT-bench

#### Phi-3-medium (14B)
- **Architecture**: 40 heads, 40 layers, embedding dimension 5120
- **Training**: 4.8T tokens
- **Key Result**: 78% MMLU, 8.9 MT-bench

#### Phi-3.5-MoE (16x3.8B)
- **Architecture**: Mixture-of-Experts with 16 expert networks
- **Active Parameters**: 6.6B (top-2 routing per token)
- **Total Parameters**: 42B
- **Key Features**:
  - SparseMixer training approach
  - 128K context window
  - Superior multilingual performance
- **Key Result**: On par with Gemini-1.5-Flash and GPT-4o-mini

#### Phi-3.5-Vision (4.2B)
- **Architecture**: CLIP ViT-L/14 encoder + Phi-3.5-mini decoder
- **Capabilities**:
  - Single and multi-image understanding
  - Chart/table/diagram comprehension
  - Video summarization (16 frames)
  - High-resolution support (up to 1344x1344)
- **Training**: 0.5T vision+text tokens, 33B multimodal SFT tokens

### Benchmark Performance

| Benchmark | Phi-3-mini | Phi-3-small | Phi-3-medium | GPT-3.5 |
|-----------|------------|-------------|--------------|---------|
| MMLU (5-shot) | 68.8 | 75.7 | 78.0 | 71.4 |
| GSM-8K (8-shot, CoT) | 82.5 | 89.6 | 91.0 | 78.1 |
| HumanEval (0-shot) | 58.5 | 61.0 | 62.2 | 62.2 |
| BigBench-Hard (3-shot) | 71.7 | 79.1 | 81.4 | 68.3 |
| MT-bench | 8.38 | 8.70 | 8.91 | 8.35 |

### Training Methodology
1. **Phase 1**: General knowledge and language understanding from web sources
2. **Phase 2**: Logical reasoning and niche skills from heavily filtered web + synthetic data
3. **Post-training**: SFT on curated data + DPO for safety and robustness

### Source PDF
- [[Phi-3/Phi-3_Technical_Report.pdf|Phi-3 Technical Report]]

---

## Orca Series

### Overview
The Orca models pioneer "explanation tuning" - learning from rich signals including step-by-step thought processes and detailed explanations from GPT-4, rather than simple imitation of outputs.

### Orca (Original)

#### Key Innovation: Explanation Tuning
- Augments query-response pairs with detailed reasoning traces from GPT-4
- Uses system instructions to elicit explanations (e.g., "think step-by-step", "explain like I'm five")
- 5M ChatGPT responses + 1M GPT-4 responses for training

#### Architecture
- **Base Model**: LLaMA-13B
- **Training Data**: 5M samples from ChatGPT, 1M from GPT-4
- **Data Source**: FLAN-v2 collection (diverse task mixture)

#### Key Results
- Surpasses Vicuna-13B by 100% on BigBench Hard
- 42% improvement over Vicuna on AGIEval
- Reaches parity with ChatGPT on BBH benchmark
- Competitive on SAT, LSAT, GRE, GMAT exams (zero-shot)

### Orca 2

#### Key Innovation: Cautious Reasoning
Orca 2 teaches models to **select** the most effective reasoning strategy rather than always using the same approach:

- **Step-by-step**: Sequential reasoning for complex problems
- **Recall then generate**: Retrieve relevant information first
- **Recall-reason-generate**: Multi-stage reasoning
- **Direct answer**: When appropriate for simpler tasks
- **Explain-then-answer**: Provide rationale before conclusion

#### Prompt Erasure Technique
- Teacher model receives task-specific system instructions to demonstrate optimal strategies
- Student model sees only the task and resulting behavior (not the prompts)
- Forces the model to learn **when** to use each strategy, not just follow instructions

#### Architecture
- **Base Models**: LLaMA-2 7B and 13B
- **Training Data**: ~817K new instances + FLAN + Orca 1 data
- **Progressive Learning**:
  1. FLAN-v2 (1 epoch)
  2. 5M ChatGPT data (3 epochs)
  3. 1M GPT-4 + 817K Orca 2 data (4 epochs)

#### Key Results
| Benchmark | Orca-2-7B | Orca-2-13B | LLaMA-2-Chat-70B | WizardLM-70B |
|-----------|-----------|------------|------------------|--------------|
| AGIEval | - | Higher | Comparable | Higher |
| BBH | - | Higher | Comparable | Higher |
| MMLU | - | Higher | Comparable | Higher |
| GSM8K | - | Higher | Comparable | Higher |

*Orca 2 models (7B and 13B) match or exceed models 5-10x larger*

#### Evaluation
- 15 diverse benchmarks (~100 tasks, 36K+ unique prompts)
- Covers: language understanding, common sense reasoning, multi-step reasoning, math, reading comprehension, summarization, truthfulness, safety

### Source PDFs
- [[Orca/Orca_Progressive_Learning_from_Complex_Explanation_Traces.pdf|Orca: Progressive Learning from Complex Explanation Traces]]
- [[Orca/Orca_2_Teaching_Small_Language_Models_How_to_Reason.pdf|Orca 2: Teaching Small Language Models How to Reason]]

---

## Megatron-Turing NLG (Collaboration with NVIDIA)

### Overview
Megatron-Turing NLG 530B (MT-NLG) was the largest monolithic transformer language model at the time of release, developed through collaboration between Microsoft DeepSpeed and NVIDIA Megatron-LM teams.

### Key Specifications
- **Parameters**: 530 billion (3x larger than GPT-3)
- **Architecture**: Transformer decoder (monolithic, not mixture-of-experts)
- **Training Infrastructure**: 560 DGX A100 nodes on NVIDIA Selene
- **Memory Requirements**: 10+ terabytes for weights, gradients, and optimizer states

### 3D Parallelism Innovation
The key technical contribution was combining three parallelism strategies:

1. **Tensor Parallelism** (Megatron): Partitions individual layers across GPUs
   - 8-way within each DGX node (using NVLink)
   - Reduces memory proportionally

2. **Pipeline Parallelism** (DeepSpeed): Divides model into pipeline stages
   - 35-way across nodes
   - Uses 1F1B schedule to bound activations in flight
   - Lowest communication overhead

3. **Data Parallelism**: Scales to arbitrary GPU counts
   - Gradient aggregation across replicas
   - ZeRO optimizations for memory efficiency

### Topology-Aware Mapping
- Tensor parallel groups placed within nodes (highest bandwidth)
- Data parallel workers on nearby nodes when possible
- Pipeline stages can span nodes (lowest communication volume)

### Training Details
- **Hardware**: 4480 NVIDIA A100 80GB GPUs
- **Training Precision**: bfloat16 mixed precision
- **Batch Size**: 1920 with gradient accumulation
- **Performance**: 113-126 teraFLOP/s per GPU
- **Efficiency**: 81-90% parallel efficiency with 4-8x micro-batches vs pipeline stages

### Capabilities
- State-of-the-art zero-shot, one-shot, and few-shot learning
- Free-form generation of coherent long-form text
- Real-world knowledge responses
- Basic mathematical operations

### Source PDF
- [[Megatron-Turing NLG/Megatron-Turing_NLG_530B.pdf|Using DeepSpeed and Megatron to Train Megatron-Turing NLG 530B]]

---

## Key Research Themes

### 1. Data Quality > Model Size
Microsoft Research consistently demonstrates that training data quality can compensate for model size:
- Phi series: 3.8B model matches 45B Mixtral
- "Textbooks Are All You Need" philosophy
- Synthetic data generation from LLMs

### 2. Teaching Reasoning, Not Imitation
- Orca series focuses on learning the reasoning **process**, not just outputs
- Explanation tuning provides visibility into teacher's thinking
- Cautious reasoning teaches strategy selection

### 3. Efficient Deployment
- Phi-3-mini: Phone-deployable at 1.8GB (4-bit quantized)
- Focus on real-world usability, not just benchmark scores

### 4. Responsible AI
- Safety alignment through SFT and DPO
- Red-teaming across harm categories
- Transparency about limitations and weaknesses

---

## WizardLM Family

### Overview
The WizardLM family uses the innovative "Evol-Instruct" methodology to progressively rewrite instructions into increasingly complex forms, enabling smaller models to excel at following complex instructions and specialized tasks.

### Key Innovation: Evol-Instruct
- Progressively rewrites initial instructions step-by-step into more complex instructions
- Mixes all generated instruction data to fine-tune base models (LLaMA)
- Creates three specialized variants: WizardLM (general), WizardCoder (code), WizardMath (math)

### Models
- **WizardLM**: Base instruction-following model, preferred over ChatGPT in human evaluations on complex tasks
- **WizardCoder**: Code generation specialist, surpasses Anthropic's Claude and Google's Bard
- **WizardMath**: Mathematical reasoning expert, outperforms GPT-3.5-Turbo, Claude 2, and Gemini Pro

### Source PDFs
- [[WizardLM/WizardLM_Empowering_Complex_Instructions.pdf|WizardLM: Empowering Complex Instructions]]
- [[WizardLM/WizardCoder_Evol-Instruct.pdf|WizardCoder: Evol-Instruct]]
- [[WizardLM/WizardMath_Reinforced_Evol-Instruct.pdf|WizardMath: Reinforced Evol-Instruct]]

**Note**: In 2025, the WizardLM team left Microsoft to join Tencent's Hunyuan organization.

---

## Phi-1 and Phi-1.5

### Phi-1: The Beginning
- **Parameters**: 1.3B
- **Key Innovation**: "Textbooks Are All You Need" - high-quality curated and synthetic data
- **Training**: 4 days on 8 A100 GPUs
- **Performance**: 50.6% HumanEval, 55.5% MBPP
- **Paradigm**: Demonstrated that data quality can compensate for model size

### Phi-1.5: Common Sense Reasoning
- **Parameters**: 1.3B
- **Focus**: Common sense reasoning and language understanding
- **Achievement**: Performance comparable to models 5x larger
- **Capabilities**: Grade-school mathematics, basic coding, natural language tasks

### Source PDFs
- [[Phi-1/Textbooks_Are_All_You_Need.pdf|Textbooks Are All You Need (Phi-1)]]
- [[Phi-1.5/Textbooks_Are_All_You_Need_II.pdf|Textbooks Are All You Need II (Phi-1.5)]]

---

## Phi-2

### Overview
Phi-2 continues the data quality focus with a 2.7B parameter model that surpasses Mistral 7B and Llama-2 13B on various benchmarks.

### Key Specifications
- **Parameters**: 2.7B
- **Training**: 1.4T tokens from synthetic and web datasets
- **Context**: 2048 tokens
- **Achievement**: Matches or outperforms Google Gemini Nano 2

### Note
Unlike other Phi models, Phi-2 does not have a standalone arXiv technical report. Information is available through the Microsoft Research blog post and the Phi-3 technical report.

---

## Phi-4 Series

### Overview
The latest generation of Phi models featuring a 14B parameter flagship model and specialized variants for reasoning, multimodal understanding, and compact deployment.

### Models

#### Phi-4 (14B)
- **Training Focus**: Data quality centrally focused recipe
- **Performance**: State-of-the-art for its size on reasoning benchmarks
- **Coding**: Strong performance on LiveCodeBench and Codeforces

#### Phi-4-mini (3.8B)
- **Architecture**: Compact model with multimodal capabilities via Mixture-of-LoRAs
- **Capabilities**: Text, image, and audio processing
- **Deployment**: Lightweight multimodal foundation model

#### Phi-4-reasoning (14B)
- **Training**: Supervised fine-tuning on "teachable" prompts generated by o3-mini
- **Innovation**: Guided by reasoning demonstrations from o3-mini
- **Focus**: Advanced reasoning capabilities

#### Phi-4-multimodal
- **Modalities**: Text, image, and audio inputs
- **Architecture**: Lightweight open multimodal foundation model

### Source PDFs
- [[Phi-4/Phi-4_Technical_Report.pdf|Phi-4 Technical Report]]
- [[Phi-4/Phi-4-Mini_Technical_Report.pdf|Phi-4-Mini Technical Report]]
- [[Phi-4/Phi-4-Reasoning_Technical_Report.pdf|Phi-4-Reasoning Technical Report]]
- [[Phi-4/Phi-4-Multimodal_Technical_Report.pdf|Phi-4-Multimodal Technical Report]]

---

## Links to Source PDFs

| Paper | Model | Link |
|-------|-------|------|
| Textbooks Are All You Need | Phi-1 | [[Phi-1/Textbooks_Are_All_You_Need.pdf]] |
| Textbooks Are All You Need II | Phi-1.5 | [[Phi-1.5/Textbooks_Are_All_You_Need_II.pdf]] |
| Phi-3 Technical Report | Phi-3, Phi-3.5 | [[Phi-3/Phi-3_Technical_Report.pdf]] |
| Phi-3 Safety Post-Training | Phi-3.5 | [[Phi-3.5/Phi-3_Safety_Post-Training.pdf]] |
| Phi-4 Technical Report | Phi-4 | [[Phi-4/Phi-4_Technical_Report.pdf]] |
| Phi-4-Mini Technical Report | Phi-4-mini | [[Phi-4/Phi-4-Mini_Technical_Report.pdf]] |
| Phi-4-Reasoning Technical Report | Phi-4-reasoning | [[Phi-4/Phi-4-Reasoning_Technical_Report.pdf]] |
| Phi-4-Multimodal Technical Report | Phi-4-multimodal | [[Phi-4/Phi-4-Multimodal_Technical_Report.pdf]] |
| WizardLM | WizardLM | [[WizardLM/WizardLM_Empowering_Complex_Instructions.pdf]] |
| WizardCoder | WizardCoder | [[WizardLM/WizardCoder_Evol-Instruct.pdf]] |
| WizardMath | WizardMath | [[WizardLM/WizardMath_Reinforced_Evol-Instruct.pdf]] |
| Orca: Progressive Learning | Orca | [[Orca/Orca_Progressive_Learning_from_Complex_Explanation_Traces.pdf]] |
| Orca 2: Teaching Reasoning | Orca 2 | [[Orca/Orca_2_Teaching_Small_Language_Models_How_to_Reason.pdf]] |
| Megatron-Turing NLG 530B | MT-NLG | [[Megatron-Turing NLG/Megatron-Turing_NLG_530B.pdf]] |
