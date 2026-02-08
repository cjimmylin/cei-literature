---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0054
type: preprint
short_title: FiSCo (Fine-grained Semantic Comparison)
year: 2025
first_author: "[[Weijie Xu]]"
authors: Weijie Xu et al.
url: "https://arxiv.org/abs/2506.19028"
external_pdf: "https://arxiv.org/pdf/2506.19028.pdf"
local_pdf: "[[PDFs/2025/2025-Xu-FiSCo Fine-grained Semantic Comparison.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Xu-FiSCo Fine-grained Semantic Comparison.md"
publication: arXiv preprint
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
tags: 
abstract: "Large Language Models (LLMs) often generate responses with inherent biases, undermining their reliability in real-world applications. Existing evaluation methods often overlook biases in long-form responses and the intrinsic variability of LLM outputs. To address these challenges, we propose FiSCo (Fine-grained Semantic Comparison), a novel statistical framework to evaluate group-level fairness in LLMs by detecting subtle semantic differences in long-form responses across demographic groups."
ethics_perspective: "Bias & Fairness"
data_description: "Evaluation framework annotated dataset"
data_metrics: "Not specified"
---
# FiSCo (Fine-grained Semantic Comparison)

## Authors

[[Weijie Xu et al.]]

## Metadata

**Authors:** Weijie Xu et al.

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

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 17
**Implementation Readiness:** HIGH

## Tags

