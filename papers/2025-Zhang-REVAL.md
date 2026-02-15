---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: G8626BE5
type: conferencePaper
short_title: REVAL
year: 2025
first_author: "[[Jie Zhang]]"
last_author: "[[Xilin Chen]]"
authors: "Jie Zhang; Zheng Yuan; Zhongqi Wang; Bei Yan; Sibo Wang; Xiangkui Cao; Zonghui Guo; Shiguang Shan; Xilin Chen"
doi: 10.48550/arXiv.2503.16566
tags: "Computer Science - Computer Vision and Pattern Recognition"
url: "http://arxiv.org/abs/2503.16566"
external_pdf: "http://arxiv.org/pdf/2503.16566.pdf"
publication: arXiv.org
ethics_perspective: "AI Safety & Alignment"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "AI Safety & Alignment"
key_contribution: "Introduced REVAL, a large-scale benchmark (144k samples) for evaluating Large Vision-Language Models (LVLMs) on reliability (hallucination) and values (safety, ethics, privacy)."
significance: "Exposes the 'multimodal safety gap', showing that LVLMs are highly vulnerable to 'visual jailbreaks' (e.g., text instructions inside images) that purely text-based models would reject."
pdf_extract: "PDF Extracts/2025/2025-Zhang-REVAL.md"
abstract: "The rapid evolution of Large Vision-Language Models (LVLMs) has highlighted the necessity for comprehensive evaluation frameworks that assess these models across diverse dimensions. While existing benchmarks focus on specific aspects such as perceptual abilities, cognitive capabilities, and safety against adversarial attacks, they often lack the breadth and depth required to provide a holistic understanding of LVLMs’ strengths and limitations."
paper_summary: "Abstract: The rapid evolution of Large Vision-Language Models (LVLMs) has highlighted the necessity for comprehensive evaluation frameworks that assess these models across diverse dimensions. While existing ben | Overview: REVAL: A Comprehension Evaluation on Reliability and Values of Large Vision-Language Models Jie Zhang1,2†, Zheng Yuan1,2†, Zhongqi Wang1,2, Bei Yan1,2, Sibo Wang1,2, Xiangkui Cao1,2, Zonghui Guo1, Shi | Key Findings: aspects, question types and statistics. The number following the ✓indicates the number of fine-grained categories specifically considered when evaluat | Conclusions: Discussion on the difference with MultiTrust. In recent years, comprehen- sive multi-dimensional evaluations of Large Vision-Language Models (LVLMs) h"
local_pdf: [[PDFs/2025/2025-Zhang-REVAL.pdf]]
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark for moral/ethical reasoning"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, Gemini, OPT, Vicuna, Llama-2, Flan-T5, Qwen, Phi"
DATA_URL: "https://github.com/InternLM/InternLM-techreport"
---
# REVAL: A Comprehension Evaluation on Reliability and Values of Large Vision-Language Models

## Metadata

**Authors:** Zhang, Jie; Yuan, Zheng; Wang, Zhongqi; Yan, Bei; Wang, Sibo; Cao, Xiangkui; Guo, Zonghui; Shan, Shiguang; Chen, Xilin

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2503.16566](https://doi.org/10.48550/arXiv.2503.16566)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2025/2025-Zhang-REVAL.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2503.16566
- **DOI:** https://doi.org/10.48550/arXiv.2503.16566

## Abstract

This paper presents **REVAL**, a comprehensive benchmark for evaluating the **REliability** and **VALues** of Large Vision-Language Models (LVLMs). Addressing the gap in holistic evaluation, REVAL covers 144k samples across two main pillars:
1.  **Reliability**: Truthfulness (Hallucination) and Robustness (Adversarial attacks, image corruption).
2.  **Values**: Ethics (Bias, Moral understanding), Safety (Toxicity, Jailbreaks), and Privacy.
Testing 26 models (including GPT-4o and Gemini 1.5), the authors find that while models are getting better at perception, they are surprisingly vulnerable to **Visual Jailbreaks** and privacy leaks.

### Detailed Summary
REVAL is a massive stress-test suite. It goes beyond simple "accuracy" to test **Safety Alignment** in the visual modality.
Key findings:
*   **Visual Jailbreaks**: Images containing text instructions (Typographic Attacks) can easily bypass safety filters that would stop a text-only prompt.
*   **Privacy**: Models often eagerly identify PII (Personally Identifiable Information) from images (e.g., reading a credit card number or face recognition) despite safety guidelines.
*   **Ethical Reasoning**: While text reasoning is strong, *visual* ethical reasoning (identifying unsafe situations in a photo) lags behind.

### Paper Outline
1.  **Introduction**: The need for a "GLUE-style" safety benchmark for Vision-Language.
2.  **REVAL Benchmark Construction**:
    *   **Reliability**: Hallucination (POPE), Robustness (ImageNet-C).
    *   **Values**: Ethics (Ethical Lens), Safety (SafeBench), Privacy (PrivBench).
3.  **Experiments**: Evaluating 26 LVLMs (Open: LLaVA, Yi-VL; Closed: GPT-4o, Gemini).
4.  **Results**: Detailed breakdown by category.
5.  **Conclusion**: Visual safety is the new frontier for alignment.

### Methods Summary
*   **Dataset Aggregation**: Combining diverse sources (e.g., ObjectNet for robustness, locally curated safety/jailbreak images).
*   **Evaluation Metrics**: Accuracy (for factual tasks), Attack Success Rate (ASR, for jailbreaks/robustness).
*   **Diverse Models**: Benchmarking the SOTA across different architectures (MoE, Dense) and sizes.

### Results Summary
1.  **The Safety-Utility Tradeoff**: Robust models (high accuracy) were not necessarily safer. GPT-4o scored high on both, but many open models sacrificed safety for performance.
2.  **Adversarial Vulnerability**: Almost all models failed significantly against "pixel perturbation" attacks and "typographic" attacks (writing "I hate you" on a sign in the image).
3.  **Privacy Gap**: Most models failed to redact sensitive info in images unless explicitly instructed, posing a risk for real-world deployment (e.g., smart glasses).

### Conclusions
Current LVLMs are powerful but fragile. REVAL provides the standard for "Red Teaming" multimodal systems before deployment.

### Artifact Contributions
*   **REVAL Benchmark**: 144K VQA samples for Reliability and Values.
*   **Leaderboard**: Comparative safety rankings of 26 LVLMs.

## Authors

[[Jie Zhang]], [[Zheng Yuan]], [[Zhongqi Wang]], [[Bei Yan]], [[Sibo Wang]], [[Xiangkui Cao]], [[Zonghui Guo]], [[Shiguang Shan]], [[Xilin Chen]]

## Data Description

REVAL is a comprehensive benchmark for evaluating the reliability and values of large vision-language models, encompassing over 144,000 image-text Visual Question Answering (VQA) samples. The benchmark is structured into two primary sections: Reliability (truthfulness and robustness) and Values (ethics, safety, and privacy), covering 11 evaluation aspects including perception, hallucination, adversarial attacks, typographic attacks, image corruption, bias, morality, toxicity, jailbreak, privacy awareness, and privacy leakage. A total of 26 models were evaluated across true-or-false, multiple-choice, and free-form question types.


## Notes


## Tags

#Computer-Science---Computer-Vision-and-Pattern-Recognition

## Citation Info

2 citations (Semantic Scholar/DOI) [2025-08-27] 0 citations (Semantic Scholar/DOI) [2025-08-23]
