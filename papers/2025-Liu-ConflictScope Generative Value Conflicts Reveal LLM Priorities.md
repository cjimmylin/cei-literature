---




Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0035
type: preprint
short_title: "ConflictScope: Generative Value Conflicts Reveal LLM Priorities"
year: 2025
first_author: "[[Andy Liu]]"
last_author: "[[Max Kleiman-Weiner]]"
authors: Andy Liu; Kshitish Ghate; Mona Diab; Daniel Fried; Atoosa Kasirzadeh; Max Kleiman-Weiner
url: "https://arxiv.org/abs/2509.25369"
external_pdf: "https://arxiv.org/pdf/2509.25369.pdf"
local_pdf: "[[PDFs/2025/2025-Liu-ConflictScope Generative Value Conflicts Reveal LLM Priorities.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Liu-ConflictScope Generative Value Conflicts Reveal LLM Priorities.md"
publication: arXiv preprint
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
tags: 
abstract: "Past work seeks to align large language model (LLM)-based assistants with a target set of values, but such assistants are frequently forced to make tradeoffs between values when deployed. In response to the scarcity of value conflict in existing alignment datasets, we introduce CONFLICTSCOPE, an automatic pipeline to evaluate how LLMs prioritize different values. Given a user-defined value set, CONFLICTSCOPE automatically generates scenarios in which a language model faces a conflict between..."
ethics_perspective: "AI Safety & Alignment"
data_description: "Evaluation approach dataset"
data_metrics: "Not specified"
LLM_assessed: "GPT-4o, Claude, Llama-3, Qwen, Gemma"
DATA_URL: "https://github.com/andyjliu/conflictscope"
normative_ethics_benchmark: Borderline
---
# ConflictScope: Generative Value Conflicts Reveal LLM Priorities

## Authors

[[Andy Liu]], [[Kshitish Ghate]], [[Mona Diab]], [[Daniel Fried]], [[Atoosa Kasirzadeh]], [[Max Kleiman-Weiner]]

## Metadata

**Authors:** Andy Liu; Kshitish Ghate; Mona Diab; Daniel Fried; Atoosa Kasirzadeh; Max Kleiman-Weiner

**Year:** 2025

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2509.25369

## Abstract

Past work seeks to align large language model (LLM)-based assistants with a target set of values, but such assistants are frequently forced to make tradeoffs between values when deployed. In response to the scarcity of value conflict in existing alignment datasets, we introduce CONFLICTSCOPE, an automatic pipeline to evaluate how LLMs prioritize different values. Given a user-defined value set, CONFLICTSCOPE automatically generates scenarios in which a language model faces a conflict between two values sampled from the set. It then prompts target models with an LLM-written “user prompt” and evaluates their free-text responses to elicit a ranking over values in the value set. Comparing results between multiple-choice and open-ended evaluations, we find that models shift away from supporting protective values, such as harmlessness, and toward supporting personal values, such as user autonomy, in more open-ended value conflict settings. However, including detailed value orderings in models’ system prompts improves alignment with a target ranking by 14%, showing that system prompting can achieve moderate success at aligning LLM behavior under value conflict. Our work demonstrates the importance of evaluating value prioritization in models and provides a foundation for future work in this area.

## Dataset Information

Automated pipeline generating value-conflict dilemmas from user-defined value sets; systematic pairwise comparison of values; MCQ and open-ended formats

## Data Description

CONFLICTSCOPE is an automated pipeline for generating value conflict scenarios that evaluate how LLMs prioritize different values. The dataset contains approximately 2,900 filtered scenarios across three value sets (HHH, Personal-Protective, and ModelSpec), each presenting a conflict between two sampled values. The pipeline evaluates 14 target models through both multiple-choice and open-ended evaluation settings, using Bradley-Terry preference models to elicit value rankings.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 15, Agent 1
**Implementation Readiness:** MEDIUM

## Tags

