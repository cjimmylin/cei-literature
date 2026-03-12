---



























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0133
type: conferencePaper
short_title: "TrolleyBench -- Evaluating Emergent Moral Reasoning and Consistency in LLMs"
year: 2025
first_author: "[[Andrew Zhu]]"
last_author: "[[Andrew Zhu]]"
authors: "Andrew Zhu"
publication: "NeurIPS 2025"
CONF-CC: "NeurIPS 2025"
external_pdf: "https://openreview.net/pdf?id=27j9XJQV5O"
pdf_extract: "PDF Extracts/2025/2025-Zhu-TrolleyBench - Evaluating Emergent Moral Reasoning and Consistency in.md"
local_pdf: "[[PDFs/2025/2025-Zhu-TrolleyBench - Evaluating Emergent Moral Reasoning and Consistency in.pdf]]"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "Cognitive Developmental, Trolley / Dilemmas (Psych)"
newtags: 
tags: 
abstract: "Large language models demonstrate remarkable generalization across tasks, yet 1 their reliability in complex domains like moral reasoning remains uncertain. We 2 introduce the first open-source benchmark explicitly designed to evaluate ethical 3 consistency, providing a structured diagnostic of how models handle dilemmas with 4 clarifying and contradictory follow-ups. Our framework yields quantifiable yes/no 5 responses and introduces two novel metrics: the Ethical Consistency Index (ECI) 6 and..."
LLM_assessed: "DeepSeek, Mistral, Gemini, GPT-4"
DATA_URL: "https://anonymous.4open.science/r/TrolleyBench-FD46/README.md"
normative_ethics_benchmark: Borderline
CONFERENCE: "NeurIPS 2025"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark for moral/ethical reasoning"
data_metrics: "Not specified"
---
# TrolleyBench -- Evaluating Emergent Moral Reasoning and Consistency in LLMs

## Authors

[[Andrew Zhu]]

## Metadata

**Authors:** [Authors]

**Year:** 2025

**Type:** conferencePaper

**Venue:** NeurIPS 2025

## Links


## Abstract

Large language models demonstrate remarkable generalization across tasks, yet 1 their reliability in complex domains like moral reasoning remains uncertain. We 2 introduce the first open-source benchmark explicitly designed to evaluate ethical 3 consistency, providing a structured diagnostic of how models handle dilemmas with 4 clarifying and contradictory follow-ups. Our framework yields quantifiable yes/no 5 responses and introduces two novel metrics: the Ethical Consistency Index (ECI) 6 and an entropy-based Inconsistency Score, capturing both contradictions and re7 sponse variability. Applying the benchmark to state-of-the-art models—Deepseek8 R1, Mistral Small-32B, Gemini-2.5, and GPT-4.1-mini—we compare model perfor9 mance against human baselines. Results show models achieve middling levels of 10 ethical consistency, lacking what is required of it. These findings highlight ethical 11 stance as a steerable but fragile trait, raising concerns for high-stakes deployment. 12 By situating moral reasoning within evaluation, we underscore the need for holis13 tic benchmarks that capture emergent behaviors, and we release our benchmark 14 to foster community progress toward more reliable and aligned LLMs (https: 15 //anonymous.4open.science/r/TrolleyBench-FD46/README.md).

## Dataset Information

Trolley-problem-style moral dilemma scenarios

## Data Description

TrolleyBench is an open-source benchmark for evaluating ethical consistency in LLMs, comprising carefully constructed moral dilemmas adapted from psychological studies including trolley problem variants and real-world scenarios. The benchmark uses yes/no response formats and introduces two metrics: the Ethical Consistency Index (ECI) and an entropy-based Inconsistency Score. Four state-of-the-art models (Deepseek-R1, Mistral Small 32B, Gemini-2.5, GPT-4.1-mini) are evaluated against human baselines collected via surveys.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 4, Agent 6
**Implementation Readiness:** HIGH

## Tags

