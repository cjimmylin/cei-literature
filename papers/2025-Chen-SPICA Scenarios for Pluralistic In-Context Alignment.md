---








Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0118
type: conferencePaper
short_title: "SPICA (Scenarios for Pluralistic In-Context Alignment)"
year: 2025
first_author: "[[Quan Ze Chen]]"
last_author: "[[Amy X. Zhang Chan Young Park]]"
authors: "Quan Ze Chen, Kevin Feng, Chan Young Park, Amy X. Zhang"
publication: "ACL 2025"
external_pdf: "https://arxiv.org/pdf/2411.10912.pdf"
pdf_extract: "PDF Extracts/2025/2025-Chen-SPICA Scenarios for Pluralistic In-Context Alignment.md"
local_pdf: "[[PDFs/2025/2025-Chen-SPICA Scenarios for Pluralistic In-Context Alignment.pdf]]"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "When different groups’ values differ, one approach to model alignment is to steer models at inference time towards each group’s preferences. However, techniques like in-context learning only consider similarity when drawing few-shot examples and not cross-group differences in values. We propose SPICA, a framework that accounts for group-level differences during in-context example retrieval. SPICA introduces three designs: scenario banks, groupinformed retrieval metrics, and in-context alignment..."
LLM_assessed: "GPT-4o, Llama3"
DATA_URL: "https://github.com/Social-Futures-Lab/SPICA-code"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation framework"
data_metrics: "Not specified"
---
# SPICA (Scenarios for Pluralistic In-Context Alignment)

## Authors

[[Kevin Feng Quan Ze Chen]], [[Amy X. Zhang Chan Young Park]]

## Metadata

**Authors:** Quan Ze Chen, Kevin Feng, Chan Young Park, Amy X. Zhang

**Year:** 2025

**Type:** conferencePaper

**Venue:** ACL 2025

## Links


## Abstract

When different groups’ values differ, one approach to model alignment is to steer models at inference time towards each group’s preferences. However, techniques like in-context learning only consider similarity when drawing few-shot examples and not cross-group differences in values. We propose SPICA, a framework that accounts for group-level differences during in-context example retrieval. SPICA introduces three designs: scenario banks, groupinformed retrieval metrics, and in-context alignment prompts. From an evaluation of SPICA on an alignment task collecting inputs from four demographic groups (n = 544), our metrics retrieve in-context examples that more closely match observed preferences, with the best prompt configuration using multiple contrastive responses to demonstrate examples. In an endto-end evaluation (n = 120), we observe that SPICA is higher rated than similarity-based retrieval, with groups seeing up to a +0.16 point improvement on a 5 point scale. Additionally, gains from SPICA were more uniform, with all groups benefiting from alignment rather than only some. Finally, we find that while a groupagnostic approach can align to aggregated values, it is not most suited for divergent groups.

## Dataset Information

Size: Evaluation with n=544 participants (4 demographic groups) + n=120 end-to-end

## Data Description

SPICA introduces a framework for pluralistic in-context alignment that uses scenario banks, group-informed retrieval metrics, and ICL prompt setups to steer LLM outputs toward different demographic groups' values and norms. The evaluation involves an alignment task with four demographic groups (n=544 for retrieval evaluation, n=120 for end-to-end), but the extract does not specify which base LLM models were tested.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 2
**Implementation Readiness:** MEDIUM

## Tags

