---









Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0204
type: preprint
short_title: "Norm Inconsistency in LLM Decision-Making"
year: 2024
first_author: "[[Shomik Jain]]"
last_author: "[[Ashia Wilson]]"
authors: "Shomik Jain; D Calacci; Ashia Wilson"
doi: 10.1609/aies.v7i1.31665
url: "https://arxiv.org/abs/2405.14812"
external_pdf: "https://arxiv.org/pdf/2405.14812.pdf"
pdf_extract: "PDF Extracts/2024/2024-Jain-Norm Inconsistency in LLM Decision-Making.md"
local_pdf: "[[PDFs/2024/2024-Jain-Norm Inconsistency in LLM Decision-Making.pdf]]"
publication: arXiv
CONF-CC: "Preprint"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "We investigate the phenomenon of norm inconsistency: where LLMs apply different norms in similar situations. Specifically, we focus on the high-risk application of deciding whether to call the police in Amazon Ring home surveillance videos. We evaluate the decisions of three state-of-theart LLMs – GPT-4, Gemini 1.0, and Claude 3 Sonnet – in relation to the activities portrayed in the videos, the subjects’ skin-tone and gender, and the characteristics of the neighborhoods where the videos were..."
LLM_assessed: "GPT-4, Claude"
DATA_URL: "NA"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation approach"
data_metrics: "Not specified"
CONFERENCE: "Preprint"
---
# Norm Inconsistency in LLM Decision-Making

## Authors

[[Shomik Jain]], [[D Calacci]], [[Ashia Wilson]]

## Metadata

**Authors:** Shomik Jain; D Calacci; Ashia Wilson

**Year:** 2024

**Type:** preprint

**Venue:** arXiv

**DOI:** [10.1609/aies.v7i1.31665](https://doi.org/10.1609/aies.v7i1.31665)

## Links

- **arXiv:** https://arxiv.org/abs/2405.14812
- **DOI:** https://doi.org/10.1609/aies.v7i1.31665

## Abstract

We investigate the phenomenon of norm inconsistency: where LLMs apply different norms in similar situations. Specifically, we focus on the high-risk application of deciding whether to call the police in Amazon Ring home surveillance videos. We evaluate the decisions of three state-of-theart LLMs – GPT-4, Gemini 1.0, and Claude 3 Sonnet – in relation to the activities portrayed in the videos, the subjects’ skin-tone and gender, and the characteristics of the neighborhoods where the videos were recorded. Our analysis reveals significant norm inconsistencies: (1) a discordance between the recommendation to call the police and the actual presence of criminal activity, and (2) biases influenced by the racial demographics of the neighborhoods. These results highlight the arbitrariness of model decisions in the surveillance context and the limitations of current bias detection and mitigation strategies in normative decision-making.

## Dataset Information

Thousands of Amazon Ring home surveillance video descriptions; annotated for criminal activity, subject skin-tone, gender, and neighborhood demographics

## Data Description

This paper evaluates norm inconsistency in LLM decision-making using 928 Amazon Ring home surveillance videos from the Calacci, Shen, and Pentland (2022) dataset. Videos are annotated for activity type (6 categories including theft, break-in, entryway interactions), subject skin-tone, gender, and setting, with neighborhood demographic data from Census tract ACS 5-year estimates. Each video is evaluated with crime and police prompts across three iterations per model.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 3
**Implementation Readiness:** MEDIUM

## Tags

