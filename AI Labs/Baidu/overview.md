# Baidu AI Research - ERNIE Model Family Overview

## Lab Overview

Baidu is a leading Chinese technology company that has made significant contributions to AI research, particularly in natural language processing. Baidu's AI research team has developed the **ERNIE** (Enhanced Representation through kNowledge IntEgration) family of pre-trained language models, which represent a pioneering approach to integrating knowledge into language representation learning.

The ERNIE series is distinguished by its focus on:
- **Knowledge-enhanced pre-training**: Incorporating linguistic and world knowledge beyond simple word co-occurrence
- **Multi-task learning frameworks**: Enabling models to learn from diverse pre-training tasks
- **Chinese NLP excellence**: Achieving state-of-the-art results on numerous Chinese language tasks
- **Unified understanding and generation**: Supporting both NLU and NLG tasks in a single framework

All ERNIE models are implemented on Baidu's PaddlePaddle deep learning framework.

---

## Timeline of ERNIE Models

| Date | Model | Parameters | Key Innovation |
|------|-------|------------|----------------|
| April 2019 | ERNIE 1.0 | ~110M (BERT-base size) | Knowledge masking strategies (entity-level, phrase-level) |
| July 2019 | ERNIE 2.0 | Base: ~110M, Large: ~340M | Continual pre-training framework with multi-task learning |
| July 2021 | ERNIE 3.0 | 10 billion | Unified NLU/NLG framework with knowledge graph integration |
| December 2021 | ERNIE 3.0 Titan | 260 billion | Credible and controllable generation, largest Chinese dense model |

---

## Summary Table of All Models

| Model | Parameters | Architecture | Training Data | Key Capabilities | Notable Benchmarks |
|-------|------------|--------------|---------------|------------------|-------------------|
| **ERNIE 1.0** | ~110M | 12-layer Transformer | Chinese Wikipedia, Baidu Baike, News, Tieba (173M sentences) | Entity/phrase masking, dialogue language modeling | SOTA on 5 Chinese NLP tasks |
| **ERNIE 2.0** | Base: ~110M, Large: ~340M | 12/24-layer Transformer | Encyclopedia, BookCorpus, News, Dialog, IR data | Continual multi-task pre-training, 7 pre-training tasks | GLUE score 80.6 (base), 83.6 (large); SOTA on 16 tasks |
| **ERNIE 3.0** | 10 billion | 48-layer Transformer-XL (universal) + 12-layer task-specific | 4TB corpus (11 categories) + knowledge graph | Unified NLU/NLG, knowledge-text prediction | SOTA on 54 Chinese tasks; SuperGLUE #1 (90.6%) |
| **ERNIE 3.0 Titan** | 260 billion | 48-layer Transformer-XL + task-specific modules | 4TB corpus + adversarial/controllable datasets | Credible/controllable generation, online distillation | SOTA on 68 NLP datasets |

---

## Detailed Model Sections

### ERNIE 1.0 (April 2019)

**Full Title**: ERNIE: Enhanced Representation through Knowledge Integration

**Key Innovation**: Knowledge Masking Strategies

ERNIE 1.0 introduced a novel approach to language representation pre-training by masking semantic units (entities and phrases) rather than individual tokens, allowing the model to learn richer semantic knowledge.

**Architecture**:
- 12 encoder layers (same as BERT-base)
- 768 hidden units
- 12 attention heads
- Vocabulary: 17,964 unicode characters

**Pre-training Tasks**:
1. **Basic-Level Masking**: Random masking of basic language units (characters for Chinese)
2. **Phrase-Level Masking**: Masking entire phrases as conceptual units
3. **Entity-Level Masking**: Masking named entities (persons, locations, organizations)
4. **Dialogue Language Model (DLM)**: Learning from query-response dialogue structures

**Training Data**:
- Chinese Wikipedia: 21M sentences
- Baidu Baike: 51M sentences
- Baidu News: 47M sentences
- Baidu Tieba: 54M sentences

**Key Results** (vs BERT):
| Task | BERT | ERNIE 1.0 | Improvement |
|------|------|-----------|-------------|
| XNLI | 77.2 | 78.4 | +1.2 |
| LCQMC | 87.0 | 87.4 | +0.4 |
| MSRA-NER | 92.6 | 93.8 | +1.2 |
| ChnSentiCorp | 94.3 | 95.4 | +1.1 |

**Source PDF**: [[AI Labs/Baidu/ERNIE 1.0/ERNIE_1.0_Enhanced_Representation_through_Knowledge_Integration.pdf]]

---

### ERNIE 2.0 (July 2019)

**Full Title**: ERNIE 2.0: A Continual Pre-Training Framework for Language Understanding

**Key Innovation**: Continual Multi-Task Pre-Training

ERNIE 2.0 introduced a framework for incrementally building and training on multiple pre-training tasks without forgetting previously learned knowledge.

**Architecture**:
- Base: 12 layers, 12 heads, 768 hidden units
- Large: 24 layers, 16 heads, 1024 hidden units
- Task embedding added to input representation

**Pre-training Tasks** (7 tasks across 3 categories):

*Word-aware Tasks*:
1. **Knowledge Masking**: Entity and phrase masking (from ERNIE 1.0)
2. **Capitalization Prediction**: Predict whether words are capitalized
3. **Token-Document Relation**: Predict if tokens appear elsewhere in the document

*Structure-aware Tasks*:
4. **Sentence Reordering**: Reorganize permuted paragraph segments (k-class classification)
5. **Sentence Distance**: 3-class classification (adjacent, same document, different documents)

*Semantic-aware Tasks*:
6. **Discourse Relation**: Predict semantic/rhetorical relations between sentences
7. **IR Relevance**: Predict query-title relevance (3-class: strong, weak, irrelevant)

**Training**:
- 48 NVIDIA V100 GPUs (base), 64 V100 GPUs (large)
- Adam optimizer with batch size 393,216 tokens

**Key Results**:
| Task | BERT | XLNet | ERNIE 2.0 |
|------|------|-------|-----------|
| GLUE Score (Large) | 80.5 | - | 83.6 |
| CoLA | 60.5 | 63.6 | 63.5 |
| SST-2 | 94.9 | 95.6 | 95.6 |
| QNLI | 92.7 | 93.9 | 94.6 |

**Source PDF**: [[AI Labs/Baidu/ERNIE 2.0/ERNIE_2.0_Continual_Pre-training_Framework.pdf]]

---

### ERNIE 3.0 (July 2021)

**Full Title**: ERNIE 3.0: Large-scale Knowledge Enhanced Pre-training for Language Understanding and Generation

**Key Innovation**: Unified NLU/NLG Framework with Knowledge Graph Integration

ERNIE 3.0 introduced a "Continual Multi-Paradigms Unified Pre-training Framework" that handles both understanding and generation tasks through shared and task-specific representation modules.

**Architecture**:
- **Universal Representation Module**: 48-layer Transformer-XL, 4096 hidden units, 64 heads
- **Task-specific Modules**: 12-layer Transformer-XL, 768 hidden units, 12 heads
  - NLU-specific: Bi-directional modeling
  - NLG-specific: Uni-directional modeling
- **Total Parameters**: 10 billion
- **Activation**: GeLU
- **Max Sequence Length**: 512 (context), 128 (memory for generation)

**Pre-training Tasks**:

*Word-aware*:
- Knowledge Masked Language Modeling
- Document Language Modeling (with Enhanced Recurrence Memory)

*Structure-aware*:
- Sentence Reordering
- Sentence Distance

*Knowledge-aware*:
- **Universal Knowledge-Text Prediction (UKTP)**: Novel task combining triples from knowledge graphs with encyclopedia sentences

**Training Data** (4TB, largest Chinese pre-training corpus at the time):
- ERNIE 2.0 corpus (17.8B tokens)
- Baidu Search/Web (357.1B tokens)
- QA data (33.9B tokens)
- Domain-specific (Medical, Law, Finance)
- Knowledge Graph (50M+ facts)

**Training**:
- 384 NVIDIA V100 GPUs
- 375 billion tokens total
- Progressive learning for efficiency

**Key Results**:
- **SuperGLUE**: 90.6% (1st place, July 2021) - surpassing human performance (89.8%)
- State-of-the-art on **54 Chinese NLP tasks**

| Task Category | Notable Improvements |
|---------------|---------------------|
| Sentiment Analysis | +11% on SE-ABSA16_PHNS |
| Winograd Schema | +25.7% on WSC2020 |
| Reading Comprehension | +34% on CMRC2019 PAC |

**Source PDF**: [[AI Labs/Baidu/ERNIE 3.0/ERNIE_3.0_Large-scale_Knowledge_Enhanced_Pre-training.pdf]]

---

### ERNIE 3.0 Titan (December 2021)

**Full Title**: ERNIE 3.0 Titan: Exploring Larger-scale Knowledge Enhanced Pre-training for Language Understanding and Generation

**Key Innovation**: Credible and Controllable Generation + Online Distillation

ERNIE 3.0 Titan scaled up the ERNIE 3.0 framework to 260 billion parameters, making it the largest Chinese dense pre-trained model. It introduced novel techniques for generating credible and controllable text.

**Architecture**:
- **Universal Representation Module**: 48 layers, 12288 hidden units, 192 heads
- **Feed-forward inner dimension**: 196,608 (16x hidden size)
- **Task-specific Modules**: 12 layers, 768 hidden units, 12 heads
- **Total Parameters**: 260 billion

**Novel Pre-training Tasks**:

1. **Self-supervised Adversarial Loss**:
   - Binary classification: distinguish original text from ERNIE-generated text
   - Enables credibility ranking of generated outputs
   - Dataset: 2M positive examples + 2M generated negative examples

2. **Controllable Language Modeling Loss**:
   - Conditions generation on multiple attributes:
     - **Genre**: General, Web, QA, Knowledge, Finance, Law, Medical, Novel, etc.
     - **Topic**: 26 categories (sports, technology, culture, etc.)
     - **Keywords**: Extracted key information
     - **Sentiment**: Positive, negative, neutral
     - **Length**: Token count control

**Online Distillation Framework**:
- **On-the-Fly Distillation (OFD)**: Teacher trains itself while teaching students
- **Auxiliary Layer Distillation (ALD)**: Extra layer for complete gradient flow
- **Teacher Assistants**: Bridge large capacity gaps between teacher and students
- Enables simultaneous training of multiple student models

**Distributed Training**:
- 4D hybrid parallelism: Data, Pipeline, Tensor Model, and Group Sharded
- Trained on both NVIDIA V100 GPUs and Ascend 910 NPUs
- Resource-aware partition for heterogeneous clusters
- 91.7% weak scalability with thousands of NPU cards

**Key Results**:
- State-of-the-art on **68 NLP datasets**
- Improvements over ERNIE 3.0 across all task categories

| Task | ERNIE 3.0 | ERNIE 3.0 Titan |
|------|-----------|-----------------|
| NLPCC2014-SC | 86.00 | 86.32 |
| SE-ABSA16_PHNS | 93.95 | 94.14 |
| LCQMC | 90.38 | 90.55 |
| DuReader (EM/F1) | 67.69/79.66 | 68.92/80.74 |

**Source PDF**: [[AI Labs/Baidu/ERNIE 3.0 Titan/ERNIE_3.0_Titan_Exploring_Larger-scale_Knowledge_Enhanced_Pre-training.pdf]]

---

## Key Themes Across the ERNIE Family

1. **Knowledge Integration**: From entity/phrase masking (1.0) to knowledge graph integration (3.0/Titan)
2. **Continual Learning**: Building new capabilities without forgetting previous knowledge
3. **Multi-Task Pre-training**: Diverse tasks for comprehensive language understanding
4. **Unified Frameworks**: Single models supporting both understanding and generation
5. **Scalability**: Progressive scaling from BERT-size to 260B parameters
6. **Practical Deployment**: Distillation frameworks for real-world applications

## References

- GitHub: https://github.com/PaddlePaddle/ERNIE
- arXiv: 1904.09223 (ERNIE 1.0), 1907.12412 (ERNIE 2.0), 2107.02137 (ERNIE 3.0), 2112.12731 (ERNIE 3.0 Titan)
