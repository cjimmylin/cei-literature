---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0004
type: preprint
short_title: BiasLab (Multilingual Dual-Framing Framework)
year: 2026
first_author: "[[William Guey]]"
last_author: "[[William Guey]]"
authors: William Guey et al.
authors_incomplete: true
url: "https://arxiv.org/abs/2601.06861"
external_pdf: "https://arxiv.org/pdf/2601.06861.pdf"
local_pdf: "[[PDFs/2026/2026-Guey-BiasLab Multilingual Dual-Framing Framework.pdf]]"
pdf_extract: "PDF Extracts/2026/2026-Guey-BiasLab Multilingual Dual-Framing Framework.md"
publication: arXiv preprint
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "Yes"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
tags: 
abstract: "Large Language Models (LLMs) are increasingly deployed in high-stakes contexts where their outputs influence real-world decisions. However, evaluating bias in LLM outputs remains methodologically challenging due to sensitivity to prompt wording, limited multilingual coverage, and the lack of standardized metrics that enable reliable comparison across models. In this paper, we introduce BiasLab, an open-source model-agnostic evaluation framework for quantifying output-level (extrinsic) bias..."
data_description: "Multilingual benchmark for bias and fairness dataset"
data_metrics: "Not specified"
LLM_assessed: "NA"
DATA_URL: "https://github.com/williamguey/LLMbiaslab"
---
# BiasLab (Multilingual Dual-Framing Framework)

## Authors

[[William Guey]]

## Metadata

**Authors:** William Guey et al.

**Year:** 2026

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2601.06861

## Abstract

Large Language Models (LLMs) are increasingly deployed in high-stakes contexts where their outputs influence real-world decisions. However, evaluating bias in LLM outputs remains methodologically challenging due to sensitivity to prompt wording, limited multilingual coverage, and the lack of standardized metrics that enable reliable comparison across models. In this paper, we introduce BiasLab, an open-source model-agnostic evaluation framework for quantifying output-level (extrinsic) bias through a multilingual, robustness-oriented experimental design. BiasLab constructs mirrored probe pairs under a strict dual-framing scheme: an affirmative assertion favoring Target A and a reverse assertion obtained by deterministic target substitution favoring Target B, while preserving identical linguistic structure. To reduce dependence on prompt templates, BiasLab additionally performs repeated evaluation under randomized instructional wrappers and enforces a fixed-choice Likert response format to maximize comparability across models and languages. Responses are normalized into agreement labels using an LLM-based judge, aligned for polarity consistency across framings, and aggregated into quantitative bias indicators with descriptive statistics including effect sizes and neutrality rates. The framework supports evaluation across diverse bias axes, including demographic, cultural, political, and geopolitical topics, and provides reproducible artifacts such as structured reports and comparative visualizations. BiasLab contributes a standardized methodology for cross-lingual and framing-sensitive bias measurement that complements intrinsic and dataset-based audits, enabling researchers and institutions to benchmark bias robustness and make better-informed deployment decisions.

## Dataset Information

Mirrored probe pairs under strict dual-framing scheme; randomized instructional wrappers; fixed-choice Likert response format; multilingual

## Data Description

BiasLab is an open-source, model-agnostic evaluation framework for measuring output-level bias in LLMs through multilingual, dual-framing probe pairs. The framework generates mirrored assertions under affirmative and reverse framing with randomized instructional wrappers, enforces fixed-choice Likert responses, and uses LLM-based judge normalization to produce quantitative bias indicators across languages and models. No specific LLM evaluation results are reported in this paper.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 17
**Implementation Readiness:** HIGH

## Tags

