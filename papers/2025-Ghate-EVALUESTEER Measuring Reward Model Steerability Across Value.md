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
authors: "Ghate, Kshitish; Liu, Andy; Jain, Devansh; Sorensen, Taylor; Kasirzadeh, Atoosa; Caliskan, Aylin; Diab, Mona T.; Sap, Maarten"
authors_incomplete: false
url: "https://arxiv.org/abs/2510.06370"
external_pdf: "https://arxiv.org/pdf/2510.06370.pdf"
pdf_extract: "PDF Extracts/2025/2025-Ghate-EVALUESTEER Measuring Reward Model Steerability Across Value.md"
local_pdf: "[[PDFs/2025/2025-Ghate-EVALUESTEER Measuring Reward Model Steerability Across Value.pdf]]"
publication: arXiv
CONF-CC: "Preprint"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "Multiple Religions"
rv_islam: 0
rv_christianity: 50
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 50
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: "Christianity, Jainism"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "As large language models (LLMs) are deployed globally, creating pluralistic systems that can accommodate the diverse preferences and values of users worldwide becomes essential. We introduce EVALUESTEER, a benchmark to measure LLMs’ and reward models’ (RMs) steerability towards users’ value and stylistic preference profiles grounded in psychology and human-LLM interaction literature. To address the gap in existing datasets that do not support controlled evaluations of RM steering, we..."
LLM_assessed: "Gemini, Llama-3, Qwen-2"
DATA_URL: "https://github.com/kshitishghate/EVALUESTEER-benchmark"
CONFERENCE: "Preprint"
ethics_overall: 45
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Moral Reasoning & Psychology"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark dataset"
data_metrics: "Not specified"
---
# EVALUESTEER: Measuring Reward Model Steerability Across Value Dimensions

## Authors

[[Ghate, Kshitish]], [[Liu, Andy]], [[Devansh Jain|Jain, Devansh]], [[Taylor Sorensen|Sorensen, Taylor]], [[Atoosa Kasirzadeh|Kasirzadeh, Atoosa]], [[Caliskan, Aylin]], [[Diab, Mona T]], [[Maarten Sap|Sap, Maarten]]

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

EVALUESTEER benchmark with 165,888 synthetically generated preference pairs systematically varying 4 value dimensions and 4 style dimensions, grounded in World Values Survey data.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** HIGH

## Tags

