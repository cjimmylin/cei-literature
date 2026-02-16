---






Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0254
type: preprint
short_title: "CLASH: Evaluating Language Models on Judging High-Stakes Dilemmas from Multiple Perspectives"
year: 2025
first_author: "[[Lee, Ayoung]]"
last_author: "[[Wang, Lu]]"
authors: "[[Lee, Ayoung]]; [[Kwon, Ryan Sungmo]]; [[Railton, Peter]]; [[Wang, Lu]]"
authors_incomplete: false
url: "https://arxiv.org/abs/2504.10823"
external_pdf: "https://arxiv.org/pdf/2504.10823.pdf"
pdf_extract: "PDF Extracts/2025/2025-Lee-CLASH Evaluating Language Models on Judging High-Stakes Dilemmas from.md"
local_pdf: "[[PDFs/2025/2025-Lee-CLASH Evaluating Language Models on Judging High-Stakes Dilemmas from.pdf]]"
publication: arXiv
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "Navigating dilemmas involving conflicting values is challenging even for humans in high-stakes domains, let alone for AI, yet prior work has been limited to everyday scenarios. To close this gap, we introduce CLASH (Character perspectivebased LLM Assessments in Situations with High-stakes), a meticulously curated dataset consisting of 345 high-impact dilemmas along with 3,795 individual perspectives of diverse values."
LLM_assessed: "GPT-4o, GPT-4o mini, GPT-5, Claude, Llama-3, Qwen, Mistral, DeepSeek"
DATA_URL: "https://huggingface.co/datasets/launch/CLASH"
normative_ethics_benchmark: Borderline
ethics_overall: "Yes"
virtue_ethics: "Yes"
deontological_ethics: "No"
utilitarian_ethics: "No"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for ai safety dataset"
data_metrics: "Not specified"
---
# CLASH: Evaluating Language Models on Judging High-Stakes Dilemmas from Multiple Perspectives

## Authors

[[Lee, Ayoung]], [[Kwon, Ryan Sungmo]], [[Railton, Peter]], [[Lu Wang|Wang, Lu]]

## Metadata

**Authors:** Lee, Ayoung; Kwon, Ryan Sungmo; Railton, Peter; Wang, Lu

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2504.10823

## Abstract

Navigating dilemmas involving conflicting values is challenging even for humans in high-stakes domains, let alone for AI, yet prior work has been limited to everyday scenarios. To close this gap, we introduce CLASH (Character perspectivebased LLM Assessments in Situations with High-stakes), a meticulously curated dataset consisting of 345 high-impact dilemmas along with 3,795 individual perspectives of diverse values. CLASH enables the study of critical yet underexplored aspects of value-based decision-making processes, including understanding of decision ambivalence and psychological discomfort as well as capturing the temporal shifts of values in the perspectives of characters. By benchmarking 14 non-thinking and thinking models, we uncover several key findings. (1) Even strong proprietary models, such as GPT-5 and Claude-4-Sonnet, struggle with ambivalent decisions, achieving only 24.06 and 51.01 accuracy. (2) Although LLMs reasonably predict psychological discomfort, they do not adequately comprehend perspectives involving value shifts. (3) Cognitive behaviors that are effective in the math-solving and game strategy domains do not transfer to value reasoning. Instead, new failure patterns emerge, including early commitment and overcommitment. (4) The steerability of LLMs towards a given value is significantly correlated with their value preferences. (5) Finally, LLMs exhibit greater steerability when reasoning from a third-party perspective, although certain values (e.g., safety) benefit uniquely from first-person framing.

## Dataset Information

345 high-impact dilemmas with 3,795 diverse value perspectives across 14 models

## Data Description

CLASH (Character perspective-based LLM Assessments in Situations with High-stakes) is a curated dataset of 345 high-impact human-written dilemmas with 3,795 individual perspectives representing diverse values. It evaluates LLMs on ambivalence understanding, psychological discomfort, and value shift reasoning. Fourteen non-thinking and thinking models were benchmarked, including GPT-5, Claude-4-Sonnet, Deepseek-3.1, and Qwen3-32B. The dataset includes static and dynamic character description categories to test nuanced value-based decision-making.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** HIGH

## Tags

