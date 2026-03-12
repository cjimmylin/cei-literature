---



























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0054
type: preprint
short_title: "FiSCo (Fine-grained Semantic Comparison)"
year: 2025
first_author: "[[Xu, Weijie]]"
last_author: "[[Reddy, Chandan K.]]"
authors: "Xu, Weijie; Wang, Yiwen; Xue, Chi; Hu, Xiangkun; Fang, Xi; Dong, Guimin; Reddy, Chandan K."
authors_incomplete: false
url: "https://arxiv.org/abs/2506.19028"
external_pdf: "https://arxiv.org/pdf/2506.19028.pdf"
pdf_extract: "PDF Extracts/2025/2025-Xu-FiSCo Fine-grained Semantic Comparison.md"
local_pdf: "[[PDFs/2025/2025-Xu-FiSCo Fine-grained Semantic Comparison.pdf]]"
publication: "arXiv preprint"
CONF-CC: "Preprint"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "Large Language Models (LLMs) often generate responses with inherent biases, undermining their reliability in real-world applications. Existing evaluation methods often overlook biases in long-form responses and the intrinsic variability of LLM outputs. To address these challenges, we propose FiSCo (Fine-grained Semantic Comparison), a novel statistical framework to evaluate group-level fairness in LLMs by detecting subtle semantic differences in long-form responses across demographic groups."
LLM_assessed: "Llama-3, Mixtral, DeepSeek, GPT-4o, Claude, Qwen"
DATA_URL: "https://github.com/HuXiangkun/FiSCo"
CONFERENCE: "Preprint"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation framework annotated dataset"
data_metrics: "Not specified"
---
# FiSCo (Fine-grained Semantic Comparison)

## Authors

[[Xu, Weijie]], [[Wang, Yiwen]], [[Xue, Chi]], [[Hu, Xiangkun]], [[Fang, Xi]], [[Dong, Guimin]], [[Reddy, Chandan K]]

## Metadata

**Authors:** Xu, Weijie; Wang, Yiwen; Xue, Chi; Hu, Xiangkun; Fang, Xi; Dong, Guimin; Reddy, Chandan K.

**Year:** 2025

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2506.19028
- **Code/Data:** https://github.com/HuXiangkun/FiSCo

## Abstract

Large Language Models (LLMs) often generate responses with inherent biases, undermining their reliability in real-world applications. Existing evaluation methods often overlook biases in long-form responses and the intrinsic variability of LLM outputs. To address these challenges, we propose FiSCo (Fine-grained Semantic Comparison), a novel statistical framework to evaluate group-level fairness in LLMs by detecting subtle semantic differences in long-form responses across demographic groups. Unlike prior work focusing on sentiment or token-level comparisons, FiSCo goes beyond surface-level analysis by operating at the claim level, leveraging entailment checks to assess the consistency of meaning across responses. We decompose model outputs into semantically distinct claims and apply statistical hypothesis testing to compare inter- and intra-group similarities, enabling robust detection of subtle biases. We formalize a new group counterfactual fairness definition and validate FiSCo on both synthetic and human-annotated datasets spanning gender, race, and age. Experiments show that FiSCo more reliably identifies nuanced biases while reducing the impact of stochastic LLM variability, outperforming various evaluation metrics. Dataset: FiSCo Huggingface Datasets Repository Code: https://github.com/HuXiangkun/FiSCo

## Dataset Information

Pipeline-based evaluation framework; decomposes LLM outputs into semantic claims; applies statistical hypothesis testing (Welch's t-test); validated on synthetic and human-annotated datasets

## Data Description

FiSCo provides a benchmark dataset of 150,000 evaluated pairs designed for long-form fairness evaluation of LLMs, spanning major demographic dimensions (gender, race, and age). The dataset includes human-annotated response comparisons across realistic prompt templates with advice and insight generation formats covering 70 real-world scenarios. Multiple state-of-the-art LLMs were evaluated including Llama 3 70B Instruct, Mixtral 8x7B Instruct, DeepSeek V3.1, GPT OSS 120B, Claude4 Sonnet, and Qwen3 235B.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 17
**Implementation Readiness:** HIGH

## Tags

