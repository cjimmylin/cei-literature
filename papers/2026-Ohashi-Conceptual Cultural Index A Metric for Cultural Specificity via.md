---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: CULT0063
type: preprint
short_title: "Conceptual Cultural Index: A Metric for Cultural Specificity via Relative Generality"
year: 2026
first_author: "[[Takumi Ohashi]]"
last_author: "[[Hitoshi Iyatomi Takumi Ohashi]]"
authors: Takumi Ohashi, Hitoshi Iyatomi
url: "https://arxiv.org/abs/2602.09444"
external_pdf: "https://arxiv.org/pdf/2602.09444.pdf"
publication: arXiv
local_pdf: "[[PDFs/2026-Ohashi-Conceptual Cultural Index A Metric for Cultural Specificity via.pdf]]"
pdf_extract: "PDF Extracts/2026/2026-Ohashi-Conceptual Cultural Index A Metric for Cultural Specificity via.md"
DATE_ADDED: 20260215
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "Multicultural/Cross-cultural"
cultures_nationalities_list: "Cross-cultural, Japanese, Multiple cultures (methodology paper)"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation approach"
data_metrics: "Not specified"
LLM_assessed: "Qwen2.5-7B, Llama-3.1-8B, Llama-3.1-Swallow-8B, llm-jp-3.1-13b, gpt-oss-20b"
DATA_URL: "https://github.com/IyatomiLab/CCI"
tags: 
abstract: "Large language models (LLMs) are increasingly deployed in multicultural settings; however, systematic evaluation of cultural specificity at the sentence level remains underexplored. We propose the Conceptual Cultural Index (CCI), which estimates cultural specificity at the sentence level. CCI is defined as the difference between the generality estimate within the target culture and the average generality estimate across other cultures."
research_topic: "AI Safety & Alignment"
---
# Conceptual Cultural Index: A Metric for Cultural Specificity via Relative Generality

## Authors

[[Hitoshi Iyatomi Takumi Ohashi]]

## Metadata

**Authors:** Takumi Ohashi, Hitoshi Iyatomi

**Year:** 2026

**Type:** preprint

**Venue:** arXiv

**Cultures:** Cross-cultural, Japanese, Multiple cultures (methodology paper)

**Benchmark:** CCI

## Links

- **arXiv:** https://arxiv.org/abs/2602.09444

## Abstract

Sentence-level metric for quantifying cultural specificity. Validated on 400 sentences (200 culture-specific, 200 general). Outperforms direct LLM scoring by 10+ AUC points. Applied to assign culture-specificity scores to existing benchmarks, enabling culture-aware error analysis of model performance.

## Data Description

This paper proposes the Conceptual Cultural Index (CCI), a sentence-level metric for quantifying cultural specificity using LLM-based generality estimation across multiple cultures. CCI is validated using Japanese cultural and general sentences, demonstrating clearer separability than direct LLM scoring. The metric is applied to benchmark stratification on JCommonsenseQA and JCommonsenseMorality, showing that model performance varies with cultural specificity levels.


## Notes

**Source:** Culture/Nationality Benchmark Search (20260215), Agent Agent_09, Agent_29
**Relevance:** Methodology paper providing cultural specificity metrics applicable to Indonesian/Malay cultural benchmarks for more nuanced evaluation.

## Tags

