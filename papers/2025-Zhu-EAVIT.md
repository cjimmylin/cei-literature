---








Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 7557TPRJ
type: conferencePaper
short_title: EAVIT
year: 2025
first_author: "[[Wenhao Zhu]]"
last_author: "[[Xin Zhang]]"
authors: "Wenhao Zhu; Yuhang Xie; Guojie Song; Xin Zhang"
doi: 10.48550/arXiv.2505.12792
tags: "Computer Science - Computation and Language"
url: "http://arxiv.org/abs/2505.12792"
external_pdf: "http://arxiv.org/pdf/2505.12792.pdf"
publication: "International Joint Conference on Artificial Intelligence"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Moral Reasoning & Psychology"
key_contribution: "Proposed EAVIT, a hybrid value identification system where a small local model acts as a 'Detector' to triage and compress inputs for a large 'Verifier' model (GPT-4), saving 83% of tokens."
significance: "Solves the cost/scalability bottleneck of using SOTA LLMs for large-scale social science analysis (like value auditing), making it feasible to process massive datasets accurately."
pdf_extract: "PDF Extracts/2025/2025-Zhu-EAVIT.md"
abstract: "The rapid evolution of large language models (LLMs) has revolutionized various fields, including the identification and discovery of human values within text data. While traditional NLP models, such as BERT, have been employed for this task, their ability to represent textual data is significantly outperformed by emerging LLMs like GPTs. However, the performance of online LLMs often degrades when handling long contexts required for value identification, which also incurs substantial..."
paper_summary: "Abstract: The rapid evolution of large language models (LLMs) has revolutionized various fields, includ- ing the identification and discovery of human val- ues within text data. While traditional NLP mod- els,  | Overview: arXiv:2505.12792v1 [cs.CL] 19 May 2025 EAVIT: Efficient and Accurate Human Value Identification from Text data via LLMs Wenhao Zhu1 , Yuhang Xie1 , Guojie Song∗1 and Xin Zhang1 1National Key Laborator | Methodology: effectively reduces the number of values requiring explicit definition in the input context, thereby shortening the over- all context length. To enabl | Key Findings: Output Stage | Conclusions: This paper investigates the potential of LLMs for identify- ing human values from text data. Despite challenges, LLMs have demonstrated superior capab"
local_pdf: "[[PDFs/2025/2025-Zhu-EAVIT.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: "GPT-4, Llama-2, BERT"
DATA_URL: "NA"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation framework dataset"
data_metrics: "2000 word"
CONFERENCE: "IJCAI 2025"
---
# EAVIT: Efficient and Accurate Human Value Identification from Text data via LLMs

## Metadata

**Authors:** Zhu, Wenhao; Xie, Yuhang; Song, Guojie; Zhang, Xin

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2505.12792](https://doi.org/10.48550/arXiv.2505.12792)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2025/2025-Zhu-EAVIT.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2505.12792
- **DOI:** https://doi.org/10.48550/arXiv.2505.12792

## Abstract

This paper proposes **EAVIT** (Efficient and Accurate Value Identification via LLMs), a framework for extracting human values from text. To solve the problem that "Online" LLMs (like GPT-4) are accurate but expensive/slow, and "Local" models (like BERT) are fast but dumb, EAVIT uses a **Hybrid Architecture**. A small local "Value Detector" makes a preliminary guess and generates a **Concise Prompt** for the large online model. This reduces token usage by **6x** while maintaining or exceeding SOTA accuracy.

### Detailed Summary
Value Identification (e.g., "Does this text express 'Self-Direction'?") is nuanced and requires long context window analysis. Sending entire datasets to GPT-4 is cost-prohibitive. EAVIT trains a small model (the Detector) to act as a "triage nurse." It reads the text, identifies potential values, and then constructs a very short, targeted query for the "Doctor" (GPT-4) to confirm.
Steps:
1.  **Value Detector**: A small LLaVA/Llama model fine-tuned to predict probability scores for Schwartz values.
2.  **Prompt Compression**: Using the detector's output to select only the most relevant text segments or value hypotheses.
3.  **Online Verification**: The large model gives the final verdict.

### Paper Outline
1.  **Introduction**: The cost/accuracy trade-off in VAI (Value alignment identification).
2.  **EAVIT Framework**:
    *   Detector: Architecture and Training (Explanation-based).
    *   Compressor: Sampling strategies (Top-K value prompting).
3.  **Experiments**: Comparing EAVIT against BERT, pure GPT-4, and other baselines on standard value datasets.
4.  **Results**: High accuracy, massive token savings.

### Methods Summary
*   **Explanation-Based Training**: The local model isn't just trained to predict labels; it's trained to generate *explanations* (CoT), which improves its internal representation.
*   **Token Reduction**: Instead of "Read this 2000 word story and find values," the prompt becomes "Does this story exhibit 'Benevolence'? [Short Excerpt]."

### Results Summary
1.  **Efficiency**: Reduces input tokens by ~83% (1/6th).
2.  **Accuracy**: Outperforms BERT-based classifiers by a wide margin and matches/exceeds full-context GPT-4 (likely because the focused prompt reduces noise).

### Conclusions
Hybrid "Small-Big" model systems are the practical path forward for large-scale AI alignment audits. We don't need GPT-4 for everything; we just need it for the final check.

### Artifact Contributions
*   **EAVIT Framework**: Code for the hybrid detector-verifier pipeline.
*   **Value Detector Weights**: Fine-tuned small model checkpoints.

## Authors

[[Wenhao Zhu]], [[Yuhang Xie]], [[Guojie Song]], [[Xin Zhang]]

## Data Description

EAVIT uses the Touché23-ValueEval dataset (approximately 9,000 human-annotated samples) and Webis-ArgValues-22 (5,000 samples) as primary datasets for human value identification from text data based on Schwartz's Theory of Basic Values. The framework generates approximately 8,000 additional training instances via GPT-4o-mini to address data scarcity and class imbalance. The task involves multi-label classification of 54 values across 20 value categories derived from social network argument data.


## Notes


## Tags

#Computer-Science---Computation-and-Language

## Citation Info

123 citations (Semantic Scholar/DOI) [2025-08-27] 0 citations (Semantic Scholar/arXiv) [2025-08-27] 0 citations (Semantic Scholar/DOI) [2025-08-23]
