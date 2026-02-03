# OpenAI Model Overview

## Lab Introduction

OpenAI is an artificial intelligence research laboratory founded in December 2015. The organization has been at the forefront of developing large language models, multimodal AI systems, and generative AI technologies. OpenAI's research has significantly shaped the field of AI, introducing influential architectures like the GPT (Generative Pre-trained Transformer) series, pioneering techniques such as Reinforcement Learning from Human Feedback (RLHF), and creating widely-used systems like ChatGPT, DALL-E, and Whisper.

OpenAI's approach emphasizes scaling neural networks, learning from diverse internet data, and aligning AI systems with human values through techniques like InstructGPT's human feedback methodology.

---

## Timeline of Major Models

| Year | Model | Category | Key Milestone |
|------|-------|----------|---------------|
| 2018 | GPT-1 | Language | First demonstration of generative pre-training for NLU |
| 2019 | GPT-2 | Language | Zero-shot task transfer, 1.5B parameters |
| 2020 | GPT-3 | Language | 175B parameters, few-shot learning |
| 2020 | Image GPT | Vision | Generative pre-training for images |
| 2020 | Jukebox | Audio | Music generation in raw audio domain |
| 2020 | Scaling Laws | Research | Power-law relationships in model scaling |
| 2020 | RLHF Summarization | Alignment | Learning to summarize from human feedback |
| 2021 | DALL-E | Image Generation | Text-to-image via autoregressive transformer |
| 2021 | CLIP | Vision-Language | Contrastive language-image pre-training |
| 2021 | Codex | Code | GPT fine-tuned on code, powers GitHub Copilot |
| 2021 | GLIDE | Image Generation | Text-guided diffusion models |
| 2021 | WebGPT | Language | Browser-assisted question answering |
| 2022 | InstructGPT | Alignment | RLHF for instruction following |
| 2022 | DALL-E 2 | Image Generation | CLIP latents with diffusion decoder |
| 2022 | Whisper | Speech | Robust multilingual speech recognition |
| 2022 | Point-E | 3D | Text-to-3D point cloud generation |
| 2023 | GPT-4 | Language | Multimodal capabilities, improved reasoning |
| 2023 | GPT-4V | Vision-Language | GPT-4 with vision understanding |
| 2023 | DALL-E 3 | Image Generation | Improved prompt following via recaptioning |
| 2024 | GPT-4o | Multimodal | Omni model: text, audio, image, video |
| 2024 | o1 | Reasoning | Chain-of-thought reasoning via reinforcement learning |

---

## Summary Table of All Models

| Model | Release | Parameters | Architecture | Key Capability |
|-------|---------|------------|--------------|----------------|
| GPT-1 | Jun 2018 | 117M | 12-layer Transformer decoder | Pre-training + fine-tuning paradigm |
| GPT-2 | Feb 2019 | 1.5B | 48-layer Transformer decoder | Zero-shot multitask learning |
| GPT-3 | Jun 2020 | 175B | 96-layer Transformer decoder | Few-shot learning, in-context learning |
| Image GPT | Jun 2020 | 6.8B | GPT-2 architecture on pixels | Image generation and representation |
| Jukebox | Apr 2020 | 5B | VQ-VAE + Sparse Transformer | Music with singing in raw audio |
| DALL-E | Jan 2021 | 12B | dVAE + Transformer | Text-to-image generation |
| CLIP | Feb 2021 | 400M | Dual encoder (ViT + Transformer) | Zero-shot image classification |
| Codex | Jul 2021 | 12B | GPT fine-tuned on code | Code generation from docstrings |
| GLIDE | Dec 2021 | 3.5B | Diffusion model + text encoder | Photorealistic text-to-image |
| WebGPT | Dec 2021 | 175B | GPT-3 + browser environment | Web-assisted question answering |
| InstructGPT | Mar 2022 | 1.3B-175B | GPT-3 + RLHF | Instruction following |
| DALL-E 2 | Apr 2022 | 3.5B | CLIP + diffusion decoder | Image variations and editing |
| Whisper | Dec 2022 | 1.5B | Encoder-decoder Transformer | Multilingual speech recognition |
| Point-E | Dec 2022 | 1B | GLIDE + point cloud diffusion | Text-to-3D point clouds |
| GPT-4 | Mar 2023 | N/A | Transformer (details undisclosed) | Multimodal, human-level reasoning |
| GPT-4V | Sep 2023 | N/A | GPT-4 + vision encoder | Image understanding |
| DALL-E 3 | Oct 2023 | N/A | Diffusion with synthetic captions | Improved prompt following |
| GPT-4o | Aug 2024 | N/A | End-to-end omni model | Native multimodal (text/audio/image/video) |
| o1 | Dec 2024 | N/A | RL-trained reasoning model | Chain-of-thought deliberative alignment |

---

## Detailed Model Families

### GPT Series (Language Models)

#### GPT-1 (2018)
**Paper:** "Improving Language Understanding by Generative Pre-Training"

- **Architecture:** 12-layer Transformer decoder, 768-dimensional states, 12 attention heads
- **Training:** Pre-trained on BooksCorpus (~7,000 books) using language modeling objective
- **Innovation:** Demonstrated that generative pre-training followed by discriminative fine-tuning achieves state-of-the-art on diverse NLP tasks
- **Results:** Improved state-of-the-art on 9 of 12 NLP benchmarks including commonsense reasoning (+8.9%), question answering (+5.7%), and textual entailment (+1.5%)

**Source:** [[OpenAI-gpt-1-improving-language-understanding.pdf]]

#### GPT-2 (2019)
**Paper:** "Language Models are Unsupervised Multitask Learners"

- **Architecture:** 48-layer Transformer decoder, 1.5 billion parameters
- **Training:** WebText dataset (8M documents, 40GB text) from Reddit links with 3+ karma
- **Innovation:** Zero-shot task performance without explicit fine-tuning; demonstrated language models as general-purpose task learners
- **Key Insight:** Sufficient scale and diverse training enables zero-shot transfer to multiple tasks

**Source:** [[OpenAI-gpt-2-language-models-unsupervised-multitask-learners.pdf]]

#### GPT-3 (2020)
**Paper:** "Language Models are Few-Shot Learners"

- **Architecture:** 96-layer Transformer decoder, 175 billion parameters
- **Training:** 300B tokens from Common Crawl, WebText2, Books, Wikipedia
- **Innovation:** In-context learning - models can perform tasks from a few examples in the prompt
- **Capabilities:** Few-shot learning approaches or exceeds fine-tuned models on many benchmarks
- **Significance:** Demonstrated emergent abilities at scale, spawned era of prompt engineering

**Source:** [[OpenAI-gpt-3-language-models-few-shot-learners.pdf]]

#### GPT-4 (2023)
**Paper:** "GPT-4 Technical Report"

- **Architecture:** Details not disclosed; multimodal (text and image inputs)
- **Training:** Completed in 2022, used RLHF for alignment
- **Capabilities:** Human-level performance on professional exams (bar exam: 90th percentile), advanced reasoning, multimodal understanding
- **Safety:** Extensive red teaming, expert evaluation for dangerous capabilities

**Source:** [[OpenAI-gpt-4-technical-report.pdf]], [[OpenAI-gpt-4-system-card.pdf]]

#### GPT-4V (2023)
**Paper:** "GPT-4V(ision) System Card"

- **Architecture:** GPT-4 with vision input capability
- **Release:** September 25, 2023
- **Capabilities:** Analyze images, answer questions about visual content, describe scenes
- **Applications:** Be My Eyes accessibility tool for visually impaired users
- **Safety Mitigations:** Refusals for person identification, sensitive trait attribution, ungrounded inferences

**Source:** [[OpenAI-gpt-4v-system-card.pdf]]

#### GPT-4o (2024)
**Paper:** "GPT-4o System Card"

- **Architecture:** Autoregressive omni model, end-to-end trained across text, vision, and audio
- **Release:** August 8, 2024
- **Capabilities:**
  - Accepts any combination of text, audio, image, video inputs
  - Generates text, audio, and image outputs
  - Audio response time: 232-320ms (human-like)
  - 50% cheaper than GPT-4 Turbo
- **Notable Features:** Native multimodal processing (not separate models chained together)

**Source:** [[OpenAI-gpt-4o-system-card.pdf]]

---

### o1 Series (Reasoning Models)

#### o1 (2024)
**Paper:** "OpenAI o1 System Card"

- **Architecture:** Large-scale reinforcement learning for chain-of-thought reasoning
- **Release:** December 5, 2024
- **Innovation:** Deliberative alignment - models explicitly reason through safety specifications before answering
- **Capabilities:**
  - Extended thinking before responding
  - State-of-the-art jailbreak resistance
  - Improved factual accuracy (lower hallucination rates)
  - Better adherence to content policies
- **Variants:** o1 (full), o1-mini (faster, coding-focused), o1-preview (earlier version)

**Source:** [[OpenAI-o1-system-card.pdf]], [[OpenAI-o1-preview-system-card.pdf]]

---

### DALL-E Series (Image Generation)

#### DALL-E (2021)
**Paper:** "Zero-Shot Text-to-Image Generation"

- **Architecture:** 12 billion parameter autoregressive Transformer
- **Training:** 250 million image-text pairs from the internet
- **Method:** Two-stage: discrete VAE compresses images to 32x32 grid of tokens, then Transformer models text and image tokens as single stream
- **Capabilities:** Zero-shot text-to-image generation, image-to-image translation, concept composition

**Source:** [[OpenAI-dall-e-creating-images-from-text.pdf]]

#### DALL-E 2 / unCLIP (2022)
**Paper:** "Hierarchical Text-Conditional Image Generation with CLIP Latents"

- **Architecture:** Two-stage model: prior (generates CLIP image embedding from text) + decoder (diffusion model generates image from embedding)
- **Resolution:** Up to 1024x1024 pixels
- **Innovation:**
  - Leverages CLIP's joint embedding space
  - Enables image variations, interpolations, and text-guided editing
  - Language-guided image manipulation in zero-shot fashion
- **Capabilities:** Greater diversity than DALL-E while maintaining photorealism

**Source:** [[OpenAI-dall-e-2-hierarchical-text-conditional.pdf]]

#### DALL-E 3 (2023)
**Paper:** "Improving Image Generation with Better Captions"

- **Architecture:** Diffusion model trained on synthetically recaptioned data
- **Innovation:** Addresses prompt following by training a custom image captioner to generate highly descriptive captions for the training dataset
- **Key Insight:** Poor prompt following stems from noisy/inaccurate captions in training data, not model architecture
- **Improvements:** Substantially better prompt following, coherence, and aesthetics compared to competitors

**Source:** [[OpenAI-dall-e-3-improving-image-generation.pdf]]

---

### Vision-Language Models

#### CLIP (2021)
**Paper:** "Learning Transferable Visual Models From Natural Language Supervision"

- **Architecture:** Dual encoder - image encoder (ViT or ResNet) + text encoder (Transformer)
- **Training:** 400 million (image, text) pairs from the internet via contrastive learning
- **Innovation:**
  - Predicts which caption goes with which image
  - Zero-shot transfer to downstream tasks using natural language
- **Capabilities:**
  - Matches ResNet-50 accuracy on ImageNet zero-shot
  - Robust to distribution shift
  - Foundation for DALL-E 2 and many other systems

**Source:** [[OpenAI-clip-learning-transferable-visual-models.pdf]]

---

### Audio Models

#### Whisper (2022)
**Paper:** "Robust Speech Recognition via Large-Scale Weak Supervision"

- **Architecture:** Encoder-decoder Transformer
- **Training:** 680,000 hours of weakly supervised audio from the internet
  - 117,000 hours covering 96 languages
  - 125,000 hours of X-to-English translation data
- **Innovation:** Simple scaling of weakly supervised pre-training; no need for fine-tuning
- **Capabilities:**
  - Multilingual speech recognition (97 languages)
  - Speech translation
  - Voice activity detection
  - Approaches human-level accuracy and robustness

**Source:** [[OpenAI-whisper-robust-speech-recognition.pdf]]

#### Jukebox (2020)
**Paper:** "Jukebox: A Generative Model for Music"

- **Architecture:** Hierarchical VQ-VAE + autoregressive Sparse Transformer
- **Training:** 1.2 million songs (600,000 in English)
- **Capabilities:**
  - Generates music with singing in raw audio domain
  - Coherent songs spanning multiple minutes
  - Condition on artist, genre, and lyrics
  - Captures melody, rhythm, composition, and vocal styles

**Source:** [[OpenAI-jukebox-music-generation.pdf]]

---

### Code Models

#### Codex (2021)
**Paper:** "Evaluating Large Language Models Trained on Code"

- **Architecture:** GPT language model fine-tuned on publicly available code from GitHub
- **Parameters:** Up to 12 billion
- **Benchmark:** HumanEval - 164 programming problems with unit tests
- **Results:**
  - Codex-12B: 28.8% pass@1 (GPT-3: 0%)
  - Codex-S: 37.7% pass@1
  - With 100 samples: 77.5% pass@k
- **Application:** Powers GitHub Copilot
- **Innovation:** Introduced functional correctness evaluation via unit tests

**Source:** [[OpenAI-codex-evaluating-large-language-models-on-code.pdf]]

---

### 3D Generation

#### Point-E (2022)
**Paper:** "Point-E: A System for Generating 3D Point Clouds from Complex Prompts"

- **Architecture:** GLIDE (text-to-image) + point cloud diffusion stack
- **Speed:** Generates 3D models in 1-2 minutes on single GPU (vs. hours for alternatives)
- **Method:** First generates synthetic view from text, then conditions 3D point cloud on that image
- **Trade-off:** Faster but lower quality than optimization-based methods

**Source:** [[OpenAI-point-e-3d-point-clouds.pdf]]

---

### Research Models

#### Image GPT (2020)
**Paper:** "Generative Pretraining from Pixels"

- **Architecture:** GPT-2 style Transformer applied to image pixels
- **Innovation:** Demonstrates generative pre-training works for images without 2D spatial inductive biases
- **Results:**
  - 96.3% accuracy on CIFAR-10 with linear probe
  - 99.0% with full fine-tuning
  - 72.0% on ImageNet linear probe

**Source:** [[OpenAI-image-gpt-generative-pretraining.pdf]]

---

### Alignment Techniques

#### InstructGPT (2022)
**Paper:** "Training language models to follow instructions with human feedback"

- **Method:** Reinforcement Learning from Human Feedback (RLHF)
  1. Supervised fine-tuning on human demonstrations
  2. Train reward model on human preferences
  3. Optimize policy via PPO against reward model
- **Key Finding:** 1.3B InstructGPT preferred to 175B GPT-3 despite 100x fewer parameters
- **Improvements:** Better truthfulness, reduced toxicity, follows instructions more reliably

**Source:** [[OpenAI-instructgpt-training-language-models-to-follow-instructions.pdf]]

#### Learning to Summarize from Human Feedback (2020)
**Paper:** "Learning to summarize from human feedback"

- **Innovation:** First large-scale demonstration of RLHF for NLP
- **Method:** Train reward model on human comparisons, then optimize with PPO
- **Results:** Models trained with human feedback preferred to human reference summaries
- **Significance:** Foundation for InstructGPT and ChatGPT alignment

**Source:** [[OpenAI-learning-to-summarize-rlhf.pdf]]

#### WebGPT (2021)
**Paper:** "WebGPT: Browser-assisted question-answering with human feedback"

- **Architecture:** GPT-3 fine-tuned to use a text-based web browser
- **Method:** Behavior cloning + rejection sampling against reward model
- **Results:**
  - Preferred 56% of time to human demonstrators
  - Preferred 69% of time to highest-voted Reddit answers
- **Innovation:** End-to-end improvement of retrieval and synthesis with human feedback

**Source:** [[OpenAI-webgpt-browser-assisted-question-answering.pdf]]

---

### GLIDE (2021)
**Paper:** "GLIDE: Towards Photorealistic Image Generation and Editing with Text-Guided Diffusion Models"

- **Architecture:** 3.5 billion parameter text-conditional diffusion model
- **Innovation:** Compares CLIP guidance vs. classifier-free guidance for text-to-image
- **Finding:** Classifier-free guidance produces better photorealism and caption similarity
- **Capabilities:**
  - Photorealistic text-to-image generation
  - Image inpainting for text-driven editing
- **Results:** Preferred to DALL-E 87% for photorealism, 69% for caption similarity

**Source:** [[OpenAI-glide-text-guided-diffusion.pdf]]

---

### Foundational Research

#### Scaling Laws for Neural Language Models (2020)
**Paper:** "Scaling Laws for Neural Language Models"

- **Key Findings:**
  - Performance scales as power-law with model size, dataset size, and compute
  - Trends span 7+ orders of magnitude
  - Architecture details (width, depth) have minimal effects
  - Larger models are more sample-efficient
- **Practical Impact:** Optimal compute allocation involves training very large models on relatively modest data, stopping before convergence

**Source:** [[OpenAI-scaling-laws-for-neural-language-models.pdf]]

---

## Related Papers (Not OpenAI-authored but in collection)

The following papers are by other organizations but relevant to understanding the AI landscape:

- **Constitutional AI** (Anthropic): Self-improvement for harmlessness via AI feedback
- **Direct Preference Optimization (DPO)** (Stanford): Simpler alternative to RLHF
- **Sparks of AGI** (Microsoft Research): Early experiments analyzing GPT-4 capabilities

---

## Source PDFs

All papers referenced in this overview are available in the vault's PDF collection:

- GPT Series: `AI Labs/OpenAI/GPT-1/`, `AI Labs/OpenAI/GPT-4o/`, `AI Labs/OpenAI/o1/`
- DALL-E Series: `AI Labs/OpenAI/DALL-E/`
- Whisper: `AI Labs/OpenAI/Whisper/`
- InstructGPT: `AI Labs/OpenAI/InstructGPT/`
- Other Papers: `AI Labs/OpenAI/Papers/`

---

*Last updated: January 2026*
