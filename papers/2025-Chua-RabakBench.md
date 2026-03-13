---






























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: SU2CF2FW
type: conferencePaper
short_title: RabakBench
year: 2025
first_author: "[[Gabriel Chua]]"
last_author: "[[Roy Ka-Wei Lee]]"
authors: "Gabriel Chua; Leanne Tan; Ziyu Ge; Roy Ka-Wei Lee"
doi: 10.48550/arXiv.2507.05980
url: "http://arxiv.org/abs/2507.05980"
external_pdf: "http://arxiv.org/pdf/2507.05980.pdf"
publication: arXiv.org
CONF-CC: "Preprint"
national_ethnic_cultural: "Singaporean, Chinese"
cultures_nationalities_list: "Singaporean, Chinese"
languages_list: "Chinese, English, Malay, Singlish, Tamil"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Chinese, Singaporean, AI Safety & Alignment"
key_contribution: "Developed RabakBench, a localized multilingual safety benchmark for Singapore (Singlish, Chinese, Malay, Tamil), and a scalable pipeline for building safety datasets in low-resource environments."
significance: "Reveals significant failures in popular safety guardrails when applied to localized multilingual contexts, paving the way for cultrually-aware and representative AI safety evaluations."
tags: 
pdf_extract: "PDF Extracts/2025/2025-Chua-RabakBench.md"
abstract: "Large language models (LLMs) and their safety classifiers often perform poorly on low-resource languages due to limited training data and evaluation benchmarks. This paper introduces RABAKBENCH 2, a new multilingual safety benchmark localized to Singapore’s unique linguistic context, covering Singlish, Chinese, Malay, and Tamil. RABAKBENCH is constructed through a scalable three-stage pipeline: (i) Generate - adversarial example generation by augmenting real Singlish web content with LLM-driven..."
paper_summary: "Abstract: Large language models (LLMs) and their safety classifiers often perform poorly on low-resource languages due to limited training data and evaluation benchmarks. This paper introduces RABAKBENCH 2, a n | Overview: RabakBench: Scaling Human Annotations to Construct Localized Multilingual Safety Benchmarks for Low-Resource Languages Gabriel Chua1 ∗ Leanne Tan1 ∗ Ziyu Ge2 ∗ Roy Ka-Wei Lee1, 2 1GovTech, Singapore 2 | Methodology: for extending safety datasets to additional languages through carefully guided translation. Unlike prior approaches relying on direct translation, our | Key Findings: Models and Evaluation Metrics. We benchmarked 11 content safety models against RABAKBENCH, including 5 commercial services (AWS Bedrock Guardrails [47 | Conclusions: This paper introduced RABAKBENCH, a novel benchmark and scalable pipeline using LLMs to evaluate safety in low-resource languages, specifically within"
local_pdf: "[[PDFs/2025/2025-Chua-RabakBench.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: "Claude-3 Haiku, DeepSeek, GPT-4o, Gemini, Llama-3, Mistral, o3-mini"
DATA_URL: "https://huggingface.co/datasets/govtech/RabakBench"
CONFERENCE: "Other Conference"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Multilingual benchmark for ai safety dataset for toxicity detection"
data_metrics: "Not specified"
---
# RabakBench: Scaling Human Annotations to Construct Localized Multilingual Safety Benchmarks for Low-Resource Languages

## Metadata

**Authors:** Chua, Gabriel; Tan, Leanne; Ge, Ziyu; Lee, Roy Ka-Wei

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2507.05980](https://doi.org/10.48550/arXiv.2507.05980)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2025/2025-Chua-RabakBench.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2507.05980
- **DOI:** https://doi.org/10.48550/arXiv.2507.05980

## Abstract

Large language models (LLMs) and their safety classifiers often perform poorly on low-resource languages due to limited training data and evaluation benchmarks. This paper introduces RABAKBENCH 2, a new multilingual safety benchmark localized to Singapore’s unique linguistic context, covering Singlish, Chinese, Malay, and Tamil. RABAKBENCH is constructed through a scalable three-stage pipeline: (i) Generate - adversarial example generation by augmenting real Singlish web content with LLM-driven red teaming; (ii) Label – semi-automated multi-label safety annotation using majority-voted LLM labelers aligned with human judgments; and (iii) Translate – high-fidelity translation preserving linguistic nuance and toxicity across languages. The final dataset comprises over 5,000 safety-labeled examples across four languages and six fine-grained safety categories with severity levels. Evaluations of 11 popular open-source and closed-source guardrail classifiers reveal significant performance degradation. RABAKBENCH not only enables robust safety evaluation in Southeast Asian multilingual settings but also offers a reproducible framework for building localized safety datasets in low-resource environments. The benchmark dataset 3, including the human-verified translations, and evaluation code 4 are publicly available.

## Authors

[[Gabriel Chua]], [[Leanne Tan]], [[Ziyu Ge]], [[Roy Ka-Wei Lee]]

## Data Description

RABAKBENCH 2: a multilingual safety benchmark covering Singlish, Chinese, Malay, and Tamil with over 5,000 safety-labeled examples across six fine-grained harm categories with severity levels, localized to Singapore's linguistic context.


## Notes


## Tags

#Computer-Science---Machine-Learning #Computer-Science---Computation-and-Language

## Citation Info

0 citations (Semantic Scholar/DOI) [2025-08-27] 24 citations (Semantic Scholar/arXiv) [2025-08-27]
