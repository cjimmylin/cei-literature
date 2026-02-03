# Google DeepMind Model Overview

## Lab Overview

Google DeepMind was formed in April 2023 through the merger of Google Brain and DeepMind. The combined organization has produced some of the most influential AI systems, including the Gemini multimodal models, the PaLM language model family, and pioneering work in efficient scaling (Chinchilla), multimodal learning (Flamingo), and generalist agents (Gato). Their research spans language understanding, code generation, mathematical reasoning, medical AI, and image generation.

---

## Model Summary Table

| Model | Year | Type | Parameters | Key Features |
|-------|------|------|------------|--------------|
| Gopher | 2021 | Language | 280B | Large-scale autoregressive LM with strong few-shot performance |
| Chinchilla | 2022 | Language | 70B | Compute-optimal training; outperforms larger models with more data |
| PaLM | 2022 | Language | 540B | Pathways-trained; breakthrough reasoning and code capabilities |
| Flamingo | 2022 | Multimodal | 80B | Visual language model with few-shot image/video understanding |
| Gato | 2022 | Generalist | 1.2B | Single agent for 600+ tasks across text, images, robotics, games |
| AlphaCode | 2022 | Code | 41B | Competitive programming; ranked in top 54% of participants |
| Minerva | 2022 | Math | 540B | PaLM fine-tuned for quantitative reasoning and STEM |
| Imagen | 2022 | Image Gen | -- | Text-to-image diffusion model with unprecedented photorealism |
| PaLM 2 | 2023 | Language | -- | Improved multilingual, reasoning, and coding; powers Bard/Gemini |
| Med-PaLM 2 | 2023 | Medical | -- | Expert-level medical QA; first to pass USMLE-style benchmarks |
| Gemini 1.0 | 2023 | Multimodal | Ultra/Pro/Nano | Native multimodal; SOTA on 30+ benchmarks; reasoning focus |
| Gemma | 2024 | Language | 2B/7B | Open-weights models based on Gemini architecture |
| Gemini 1.5 | 2024 | Multimodal | Pro/Flash | 1M+ token context; Mixture-of-Experts; near-perfect recall |
| AlphaCode 2 | 2024 | Code | -- | Gemini-powered; 87th percentile on competitive programming |
| Gemma 2 | 2024 | Language | 2B/9B/27B | Knowledge distillation; competitive with models 2-3x larger |

---

## Model Families

### Gemini

#### Gemini 1.0 (December 2023)
Native multimodal model trained jointly on text, images, audio, and video. Available in Ultra (most capable), Pro (balanced), and Nano (on-device) sizes. Achieved state-of-the-art results on 30+ benchmarks, including MMLU (90.0% 5-shot) and multimodal reasoning tasks.

**Source:** [Gemini_1.0_Technical_Report.pdf](Papers/Gemini_1.0_Technical_Report.pdf)

#### Gemini 1.5 (February 2024)
Mixture-of-Experts architecture enabling up to 1 million token context (later expanded to 10M in research). Demonstrates near-perfect retrieval across extremely long documents and "in-context learning" of new languages from grammar books alone.

**Sources:** [Gemini_1.5_Technical_Report.pdf](Papers/Gemini_1.5_Technical_Report.pdf) | [Gemini_1.5_arxiv_2403.05530.pdf](Gemini%201.5/Gemini_1.5_arxiv_2403.05530.pdf)

#### Gemini Safety
Comprehensive safety evaluation framework covering dangerous content, representational harms, and adversarial attacks. Includes responsible deployment guidelines.

**Source:** [Gemini_Safety_arxiv_2403.04312.pdf](Papers/Gemini_Safety_arxiv_2403.04312.pdf)

---

### Gemma

#### Gemma (February 2024)
Open-weights models at 2B and 7B parameters built from the same research as Gemini. Designed for responsible AI development with open access while maintaining strong performance relative to size.

**Source:** [Gemma_Technical_Report.pdf](Papers/Gemma_Technical_Report.pdf)

#### Gemma 2 (August 2024)
Second-generation open models at 2B, 9B, and 27B parameters. Uses knowledge distillation and architectural improvements to achieve performance competitive with models 2-3x larger, including Llama 3 70B on several benchmarks.

**Source:** [Gemma2_Technical_Report_2408.00118.pdf](Papers/Gemma2_Technical_Report_2408.00118.pdf)

---

### PaLM

#### PaLM (April 2022)
540B parameter model trained on Google's Pathways infrastructure across 6144 TPU v4 chips. Demonstrated breakthrough performance in reasoning, code generation, and few-shot learning. First model to show emergent "chain-of-thought" capabilities at scale.

**Source:** [PaLM_arxiv_2204.02311.pdf](Papers/PaLM_arxiv_2204.02311.pdf)

#### PaLM 2 (May 2023)
Successor with improved multilingual understanding (100+ languages), enhanced reasoning, and better coding abilities. Uses compute-optimal training informed by Chinchilla scaling laws. Powers Google Bard and many Workspace features.

**Source:** [PaLM2_arxiv_2305.10403.pdf](Papers/PaLM2_arxiv_2305.10403.pdf)

---

### Gopher (December 2021)
280B parameter autoregressive language model that established new benchmarks for large-scale language understanding. Includes comprehensive analysis of model behavior, bias, and toxicity. Demonstrated strong few-shot performance across 152 diverse tasks.

**Source:** [Gopher_2112.11446.pdf](Papers/Gopher_2112.11446.pdf)

---

### Chinchilla (March 2022)
70B parameter model that challenged the "bigger is better" paradigm by demonstrating compute-optimal training. Showed that training on more data with smaller models outperforms larger undertrained models. Established the influential "Chinchilla scaling laws" used throughout the industry.

**Source:** [Chinchilla_2203.15556.pdf](Papers/Chinchilla_2203.15556.pdf)

---

### Flamingo (April 2022)
80B parameter visual language model pioneering few-shot multimodal learning. Can handle arbitrarily interleaved images/videos and text, enabling rapid adaptation to new vision-language tasks with just a few examples. Set new SOTA on 16 multimodal benchmarks.

**Source:** [Flamingo_2204.14198.pdf](Papers/Flamingo_2204.14198.pdf)

---

### Gato (May 2022)
1.2B parameter generalist agent trained on 600+ distinct tasks spanning Atari games, robotics control, image captioning, and dialogue. Demonstrates that a single network with single weights can perform diverse tasks across different modalities and embodiments.

**Source:** [Gato_2205.06175.pdf](Papers/Gato_2205.06175.pdf)

---

### AlphaCode (February 2022)
41B parameter system for competitive programming. Generates millions of candidate solutions, then filters and clusters them. Ranked in the top 54% of participants in Codeforces competitions, marking the first AI system to achieve human-competitive results.

**Source:** [AlphaCode_arxiv_2203.07814.pdf](Papers/AlphaCode_arxiv_2203.07814.pdf)

#### AlphaCode 2 (January 2024)
Built on Gemini Pro, achieves 87th percentile performance on Codeforces. Uses improved search and filtering with Gemini's enhanced reasoning capabilities for more efficient solution generation.

**Source:** [AlphaCode2_arxiv_2401.14196.pdf](Papers/AlphaCode2_arxiv_2401.14196.pdf)

---

### Minerva (June 2022)
PaLM 540B fine-tuned on 118GB of scientific and mathematical data. Achieves SOTA on MATH (50.3%) and MMLU-STEM benchmarks. Demonstrates strong quantitative reasoning including symbolic manipulation and LaTeX generation.

**Source:** [Minerva_arxiv_2206.14858.pdf](Papers/Minerva_arxiv_2206.14858.pdf)

---

### Imagen (May 2022)
Text-to-image diffusion model achieving unprecedented photorealism (record 7.27 FID on COCO). Uses a large frozen T5-XXL text encoder with cascaded diffusion models. Introduced DrawBench benchmark for systematic text-to-image evaluation.

**Source:** [Imagen_arxiv_2205.11487.pdf](Papers/Imagen_arxiv_2205.11487.pdf)

---

### Med-PaLM (2022-2023)
Medical domain adaptation of PaLM models. Med-PaLM 2 achieves expert-level performance on medical licensing exams and clinical QA tasks, becoming the first AI system to pass USMLE-style benchmarks. Includes comprehensive safety evaluation for medical applications.

**Source:** [Med-PaLM2_2305.09617.pdf](Papers/Med-PaLM2_2305.09617.pdf)

---

## File Index

All papers are located in the `Papers/` subdirectory:

| File | Model |
|------|-------|
| [AlphaCode_arxiv_2203.07814.pdf](Papers/AlphaCode_arxiv_2203.07814.pdf) | AlphaCode |
| [AlphaCode2_arxiv_2401.14196.pdf](Papers/AlphaCode2_arxiv_2401.14196.pdf) | AlphaCode 2 |
| [Chinchilla_2203.15556.pdf](Papers/Chinchilla_2203.15556.pdf) | Chinchilla |
| [Flamingo_2204.14198.pdf](Papers/Flamingo_2204.14198.pdf) | Flamingo |
| [Gato_2205.06175.pdf](Papers/Gato_2205.06175.pdf) | Gato |
| [Gemini_1.0_Technical_Report.pdf](Papers/Gemini_1.0_Technical_Report.pdf) | Gemini 1.0 |
| [Gemini_1.5_Technical_Report.pdf](Papers/Gemini_1.5_Technical_Report.pdf) | Gemini 1.5 |
| [Gemini_Safety_arxiv_2403.04312.pdf](Papers/Gemini_Safety_arxiv_2403.04312.pdf) | Gemini Safety |
| [Gemma_Technical_Report.pdf](Papers/Gemma_Technical_Report.pdf) | Gemma |
| [Gemma2_Technical_Report_2408.00118.pdf](Papers/Gemma2_Technical_Report_2408.00118.pdf) | Gemma 2 |
| [Gopher_2112.11446.pdf](Papers/Gopher_2112.11446.pdf) | Gopher |
| [Imagen_arxiv_2205.11487.pdf](Papers/Imagen_arxiv_2205.11487.pdf) | Imagen |
| [Med-PaLM2_2305.09617.pdf](Papers/Med-PaLM2_2305.09617.pdf) | Med-PaLM 2 |
| [Minerva_arxiv_2206.14858.pdf](Papers/Minerva_arxiv_2206.14858.pdf) | Minerva |
| [PaLM_arxiv_2204.02311.pdf](Papers/PaLM_arxiv_2204.02311.pdf) | PaLM |
| [PaLM2_arxiv_2305.10403.pdf](Papers/PaLM2_arxiv_2305.10403.pdf) | PaLM 2 |
