---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0226
type: conferencePaper
short_title: "Unintended Impacts of LLM Alignment on Global Representation"
year: 2024
first_author: "[[Michael J. Ryan]]"
last_author: "[[Diyi Yang]]"
authors: "Michael J. Ryan, William Held, Diyi Yang"
doi: 10.18653/v1/2024.acl-long.853
url: "https://doi.org/10.18653/v1/2024.acl-long.853"
external_pdf: "https://aclanthology.org/2024.acl-long.853.pdf"
pdf_extract: "PDF Extracts/2024/2024-Ryan-Unintended Impacts of LLM Alignment on Global Representation.md"
local_pdf: "[[PDFs/2024/2024-Ryan-Unintended Impacts of LLM Alignment on Global Representation.pdf]]"
publication: "ACL 2024"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "Before being deployed for user-facing applications, developers align Large Language Models (LLMs) to user preferences through a variety of procedures, such as Reinforcement Learning From Human Feedback (RLHF) and Direct Preference Optimization (DPO). Current evaluations of these procedures focus on benchmarks of instruction following, reasoning, and truthfulness. However, human preferences are not universal, and aligning to specific preference sets may have unintended effects."
LLM_assessed: "Llama-2, Mistral"
DATA_URL: "https://github.com/SALT-NLP/unintended-impacts-of-alignment"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Multilingual benchmark"
data_metrics: "Not specified"
---
# Unintended Impacts of LLM Alignment on Global Representation

## Authors

[[Michael J. Ryan]], [[William Held]], [[Diyi Yang]]

## Metadata

**Authors:** Michael J. Ryan, William Held, Diyi Yang

**Year:** 2024

**Type:** conferencePaper

**Venue:** ACL 2024

**DOI:** [10.18653/v1/2024.acl-long.853](https://doi.org/10.18653/v1/2024.acl-long.853)

## Links

- **DOI:** https://doi.org/10.18653/v1/2024.acl-long.853

## Abstract

Before being deployed for user-facing applications, developers align Large Language Models (LLMs) to user preferences through a variety of procedures, such as Reinforcement Learning From Human Feedback (RLHF) and Direct Preference Optimization (DPO). Current evaluations of these procedures focus on benchmarks of instruction following, reasoning, and truthfulness. However, human preferences are not universal, and aligning to specific preference sets may have unintended effects. We explore how alignment impacts performance along three axes of global representation: English dialects, multilingualism, and opinions from and about countries worldwide. Our results show that current alignment procedures create disparities between English dialects and global opinions. We find alignment improves capabilities in several languages. We conclude by discussing design decisions that led to these unintended impacts and recommendations for more equitable preference tuning. We make our code and data publicly available on Github1.

## Dataset Information

Size: Multi-axis evaluation across dialects, languages, global opinions

## Data Description

This paper evaluates 9 distinct LLMs from two model families (Llama 2 7B and Mistral v0.1 7B) across different alignment stages on three axes of global representation: English dialects, multilingualism, and global opinions. The study includes a new dataset of 554 opinionated questions about countries from r/AskReddit and uses existing benchmarks including MD3 for dialect evaluation and TyDiQA for multilingual question answering.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 2
**Implementation Readiness:** MEDIUM

## Tags

