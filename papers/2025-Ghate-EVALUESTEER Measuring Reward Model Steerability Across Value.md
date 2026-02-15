---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0274
type: preprint
short_title: "EVALUESTEER: Measuring Reward Model Steerability Across Value Dimensions"
year: 2025
first_author: "[[Ghate, Kshitish]]"
last_author: "[[Sap, Maarten]]"
authors: "[[Ghate, Kshitish]]; [[Liu, Andy]]; [[Jain, Devansh]]; [[Sorensen, Taylor]]; [[Kasirzadeh, Atoosa]]; [[Caliskan, Aylin]]; [[Diab, Mona T.]]; [[Sap, Maarten]]"
authors_incomplete: false
url: "https://arxiv.org/abs/2510.06370"
external_pdf: "https://arxiv.org/pdf/2510.06370.pdf"
pdf_extract: "PDF Extracts/2025/2025-Ghate-EVALUESTEER Measuring Reward Model Steerability Across Value.md"
local_pdf: "[[PDFs/2025/2025-Ghate-EVALUESTEER Measuring Reward Model Steerability Across Value.pdf]]"
publication: arXiv
DATE_ADDED: 20260207
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
national_ethnic_cultural: N/A
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: 
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
tags: 
abstract: "As large language models (LLMs) are deployed globally, creating pluralistic systems that can accommodate the diverse preferences and values of users worldwide becomes essential. We introduce EVALUESTEER, a benchmark to measure LLMs' and reward models' (RMs) steerability towards users' value and stylistic preference profiles grounded in psychology and human-LLM interaction literature. To address the gap in existing datasets that do not support controlled evaluations of RM steering, we..."
ethics_perspective: "Moral Reasoning & Psychology"
data_description: "Benchmark dataset"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, Gemini, Llama-3, Qwen"
DATA_URL: "https://github.com/kshitishghate/EVALUESTEER-benchmark"
---
# EVALUESTEER: Measuring Reward Model Steerability Across Value Dimensions

## Authors

[[Ghate, Kshitish]], [[Liu, Andy]], [[Jain, Devansh]], [[Sorensen, Taylor]], [[Kasirzadeh, Atoosa]], [[Caliskan, Aylin]], [[Diab, Mona T.]], [[Sap, Maarten]]

## Metadata

**Authors:** Ghate, Kshitish; Liu, Andy; Jain, Devansh; Sorensen, Taylor; Kasirzadeh, Atoosa; Caliskan, Aylin; Diab, Mona T.; Sap, Maarten

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2510.06370

## Abstract

As large language models (LLMs) are deployed globally, creating pluralistic systems that can accommodate the diverse preferences and values of users worldwide becomes essential. We introduce EVALUESTEER, a benchmark to measure LLMs’ and reward models’ (RMs) steerability towards users’ value and stylistic preference profiles grounded in psychology and human-LLM interaction literature. To address the gap in existing datasets that do not support controlled evaluations of RM steering, we synthetically generated 165,888 preference pairs – systematically varying pairs along 4 value dimensions (traditional, secular-rational, survival, and self-expression) and 4 style dimensions (verbosity, readability, confidence, and warmth). We use EVALUESTEER to evaluate whether, given a user profile and a pair of candidate value-laden and style-laden responses, LLMs and RMs are able to select the output that aligns with the user’s preferences. We evaluate six open-source and proprietary LLMs and RMs under eleven systematic prompting conditions and six preference comparison scenarios. Notably, our results show that, when given the user’s full profile of values and stylistic preferences, the best models achieve <75% accuracy at choosing the correct response, in contrast to >99% accuracy when only relevant style and value preferences are provided. EVALUESTEER thus highlights the limitations of current RMs at identifying and adapting to relevant user profile information, and provides a challenging testbed for developing RMs that can be steered towards diverse human values and preferences.

## Dataset Information

165,888 synthetic preference pairs testing alignment across value dimensions (traditional, secular-rational, survival, self-expression)

## Data Description

EVALUESTEER is a benchmark for measuring LLM and reward model steerability toward user values and stylistic preferences. It consists of 165,888 synthetically generated preference pairs varying along 4 value dimensions (traditional, secular-rational, survival, self-expression) and 4 style dimensions (verbosity, readability, confidence, warmth), grounded in the World Values Survey. Six open-source and proprietary LLMs and reward models were evaluated under 11 prompting conditions, including GPT-4.1-Mini, Gemini-2.5-Flash, Llama-3.1-8B, and Qwen-2.5-7B.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** HIGH

## Tags

