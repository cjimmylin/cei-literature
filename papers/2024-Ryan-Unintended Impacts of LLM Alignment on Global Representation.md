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
authors: "Michael J. Ryan; William Held; Diyi Yang"
doi: 10.18653/v1/2024.acl-long.853
url: "https://doi.org/10.18653/v1/2024.acl-long.853"
external_pdf: "https://aclanthology.org/2024.acl-long.853.pdf"
pdf_extract: "PDF Extracts/2024/2024-Ryan-Unintended Impacts of LLM Alignment on Global Representation.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2024/2024-Ryan-Unintended Impacts of LLM Alignment on Global Representation.pdf]]"
publication: "ACL 2024"
CONF-CC: "ACL 2024"
DATE_ADDED: 20260207
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: English
religious_values: N/A
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
religious_values_list: N/A
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
newtags: 
tags: 
abstract: "Before being deployed for user-facing applications, developers align Large Language Models (LLMs) to user preferences through a variety of procedures, such as Reinforcement Learning From Human Feedback (RLHF) and Direct Preference Optimization (DPO). Current evaluations of these procedures focus on benchmarks of instruction following, reasoning, and truthfulness. However, human preferences are not universal, and aligning to specific preference sets may have unintended effects."
LLM_assessed: "Llama-2, Mistral, Zephyr"
DATA_URL: "https://github.com/SALT-NLP/unintended-impacts-of-alignment"
CONFERENCE: "ACL 2024"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "AI Safety & Alignment"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: GE
author_region: "Eastern Europe & Central Asia"
author_global_north_south: Ambiguous
weird_score: 38
is_benchmark: Yes
is_eval: Yes
is_dataset: No
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

Releases a new dataset of 554 opinionated questions about countries sourced from r/AskReddit, used to evaluate how LLM alignment affects global opinion representation.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 2
**Implementation Readiness:** MEDIUM

## Tags

