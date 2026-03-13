---































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0112
type: preprint
short_title: "RoleConflictBench: A Benchmark of Role Conflict Scenarios for Evaluating LLMs' Contextual Sensitivity"
year: 2025
first_author: "[[Jisu Shin]]"
last_author: "[[Alice Oh]]"
authors: "Jisu Shin; Hoyun Song; Juhyun Oh; Changgeon Ko; Eunsu Kim; Chani Jung; Alice Oh"
url: "https://arxiv.org/abs/2509.25897"
external_pdf: "https://arxiv.org/pdf/2509.25897.pdf"
pdf_extract: "PDF Extracts/2025/2025-Shin-RoleConflictBench A Benchmark of Role Conflict Scenarios for.md"
local_pdf: "[[PDFs/2025/2025-Shin-RoleConflictBench A Benchmark of Role Conflict Scenarios for.pdf]]"
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
abstract: "Humans often encounter role conflicts—social dilemmas where the expectations of multiple roles clash and cannot be simultaneously fulfilled. As large language models (LLMs) become increasingly influential in human decision-making, understanding how they behave in complex social situations is essential. While previous research has evaluated LLMs’ social abilities in contexts with predefined correct answers, role conflicts represent inherently ambiguous social dilemmas that require contextual..."
LLM_assessed: "GPT-4, Gemini, Qwen"
DATA_URL: "https://github.com/ddindidu/RoleConflictBench"
CONFERENCE: "Preprint"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for bias and fairness dataset"
data_metrics: "Not specified"
---
# RoleConflictBench: A Benchmark of Role Conflict Scenarios for Evaluating LLMs' Contextual Sensitivity

## Authors

[[Jisu Shin]], [[Hoyun Song]], [[Juhyun Oh]], [[Changgeon Ko]], [[Eunsu Kim]], [[Chani Jung]], [[Alice Oh]]

## Metadata

**Authors:** Jisu Shin; Hoyun Song; Juhyun Oh; Changgeon Ko; Eunsu Kim; Chani Jung; Alice Oh

**Year:** 2025

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2509.25897

## Abstract

Humans often encounter role conflicts—social dilemmas where the expectations of multiple roles clash and cannot be simultaneously fulfilled. As large language models (LLMs) become increasingly influential in human decision-making, understanding how they behave in complex social situations is essential. While previous research has evaluated LLMs’ social abilities in contexts with predefined correct answers, role conflicts represent inherently ambiguous social dilemmas that require contextual sensitivity: the ability to recognize and appropriately weigh situational cues that can fundamentally alter decision priorities. To address this gap, we introduce ROLECONFLICTBENCH, a novel benchmark designed to evaluate LLMs’ contextual sensitivity in complex social dilemmas. Our benchmark employs a three-stage pipeline to generate over 13K realistic role conflict scenarios across 65 roles, systematically varying their associated expectations (i.e., their responsibilities and obligations) and situational urgency levels. By analyzing model choices across 10 different LLMs, we find that while LLMs show some capacity to respond to these contextual cues, this sensitivity is insufficient. Instead, their decisions are predominantly governed by a powerful, inherent bias related to social roles rather than situational information. Our analysis quantifies these biases, revealing a dominant preference for roles within the Family and Occupation domains, as well as a clear prioritization of male roles and Abrahamic religions across most evaluatee models. Code & Dataset: https://github.com/ddindidu/RoleConflictBench

## Dataset Information

13K+ realistic role conflict scenarios across 65 roles; three-stage generation pipeline; systematically varying social expectations and urgency levels

## Data Description

RoleConflictBench is a dataset of 13,914 role conflict stories across 65 social roles, generated via a three-stage pipeline varying expectation and situational urgency levels. It is designed to evaluate LLMs' contextual sensitivity in ambiguous social dilemmas.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 15, Agent 1
**Implementation Readiness:** MEDIUM

## Tags

