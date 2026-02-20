---









Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0127
type: preprint
short_title: "SycEval: Evaluating LLM Sycophancy"
year: 2025
first_author: "[[Aaron Fanous]]"
last_author: "[[Sanmi Koyejo]]"
authors: "Aaron Fanous; Jacob Goldberg; Ank Agarwal; Joanna Lin; Anson Zhou; Sonnet Xu; Vasiliki Bikia; Roxana Daneshjou; Sanmi Koyejo"
doi: 10.1609/aies.v8i1.36598
url: "https://arxiv.org/abs/2502.08177"
external_pdf: "https://arxiv.org/pdf/2502.08177.pdf"
pdf_extract: "PDF Extracts/2025/2025-Fanous-SycEval Evaluating LLM Sycophancy.md"
local_pdf: "[[PDFs/2025/2025-Fanous-SycEval Evaluating LLM Sycophancy.pdf]]"
publication: arXiv
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
abstract: "Large language models (LLMs) are increasingly applied in educational, clinical, and professional settings, but their tendency for sycophancy—prioritizing user agreement over independent reasoning—poses risks to reliability. This study introduces a framework to evaluate sycophantic behavior in ChatGPT-4o, Claude-Sonnet, and Gemini-1.5-Pro across AMPS (mathematics) and MedQuad (medical advice) datasets. Sycophantic behavior was observed in 58."
LLM_assessed: "ChatGPT, Claude, Llama-3"
DATA_URL: "NA"
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Other"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation framework dataset"
data_metrics: "Not specified"
CONFERENCE: "Preprint"
---
# SycEval: Evaluating LLM Sycophancy

## Authors

[[Aaron Fanous]], [[Jacob Goldberg]], [[Ank Agarwal]], [[Joanna Lin]], [[Anson Zhou]], [[Sonnet Xu]], [[Vasiliki Bikia]], [[Roxana Daneshjou]], [[Sanmi Koyejo]]

## Metadata

**Authors:** Aaron Fanous et al.

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**DOI:** [10.1609/aies.v8i1.36598](https://doi.org/10.1609/aies.v8i1.36598)

## Links

- **arXiv:** https://arxiv.org/abs/2502.08177
- **DOI:** https://doi.org/10.1609/aies.v8i1.36598

## Abstract

Large language models (LLMs) are increasingly applied in educational, clinical, and professional settings, but their tendency for sycophancy—prioritizing user agreement over independent reasoning—poses risks to reliability. This study introduces a framework to evaluate sycophantic behavior in ChatGPT-4o, Claude-Sonnet, and Gemini-1.5-Pro across AMPS (mathematics) and MedQuad (medical advice) datasets. Sycophantic behavior was observed in 58.19% of cases, with Gemini exhibiting the highest rate (62.47%) and ChatGPT the lowest (56.71%). Progressive sycophancy, leading to correct answers, occurred in 43.52% of cases, while regressive sycophancy, leading to incorrect answers, was observed in 14.66%. Preemptive rebuttals demonstrated significantly higher sycophancy rates than in-context rebuttals (61.75% vs. 56.52%, Z = 5.87, p < 0.001), particularly in computational tasks, where regressive sycophancy increased significantly (preemptive: 8.13%, in-context: 3.54%, p < 0.001). Simple rebuttals maximized progressive sycophancy (Z = 6.59, p < 0.001), while citation-based rebuttals exhibited the highest regressive rates (Z = 6.59, p < 0.001). Sycophantic behavior showed high persistence (78.5%, 95% CI: [77.2%, 79.8%]) regardless of context or model. These findings emphasize the risks and opportunities of deploying LLMs in structured and dynamic domains, offering insights into prompt programming and model optimization for safer AI applications.

## Dataset Information

Evaluation framework using AMPS (mathematics) and MedQuad (medical advice) datasets; multi-domain sycophancy probing

## Data Description

SycEval is a framework for evaluating sycophantic behavior in LLMs, testing ChatGPT-4o, Claude-Sonnet, and Gemini-1.5-Pro across AMPS (mathematics) and MedQuad (medical advice) datasets with 500 question-answer pairs each. The study introduces progressive and regressive sycophancy categories and evaluates model responses to in-context and preemptive rebuttals of varying strength, using Llama-3-8b for rebuttal generation and finding sycophantic behavior in 58.19% of cases overall.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 3, Agent 17
**Implementation Readiness:** HIGH

## Tags

