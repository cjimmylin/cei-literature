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
last_author: "[[Amy X. Zhang]]"
authors: Quan Ze Chen; Kevin Feng; Chan Young Park; Amy X. Zhang
publication: "ACL 2025"
CONF-CC: "ACL 2025"
external_pdf: "https://arxiv.org/pdf/2411.10912.pdf"
pdf_extract: "PDF Extracts/2025/2025-Chen-SPICA Scenarios for Pluralistic In-Context Alignment.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Chen-SPICA Scenarios for Pluralistic In-Context Alignment.pdf]]"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
rv_islam: 0
rv_christianity: 0
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 0
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: "N/A"
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
abstract: "When different groups’ values differ, one approach to model alignment is to steer models at inference time towards each group’s preferences. However, techniques like in-context learning only consider similarity when drawing few-shot examples and not cross-group differences in values. We propose SPICA, a framework that accounts for group-level differences during in-context example retrieval. SPICA introduces three designs: scenario banks, groupinformed retrieval metrics, and in-context alignment..."
LLM_assessed: "GPT-4o, Llama-3"
DATA_URL: "https://github.com/Social-Futures-Lab/SPICA-code"
CONFERENCE: "ACL 2025"
ethics_overall: 45
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 5
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation framework"
data_metrics: "Not specified"
---
# SPICA (Scenarios for Pluralistic In-Context Alignment)

## Authors

[[Quan Ze Chen]], [[Kevin Feng]], [[Chan Young Park]], [[Amy X. Zhang]]

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

Code and scenario bank data for pluralistic in-context alignment experiments across four demographic groups.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 2
**Implementation Readiness:** MEDIUM

## Tags

