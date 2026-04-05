---







































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: BI8SMNT6
type: document
short_title: "Measuring Desired Group Discrimination in LLMs"
year: 2025
first_author: "[[Angelina Wang]]"
last_author: "[[Koyejo, Sanmi]]"
authors: "Wang, Angelina; Phan, Michelle; Daniel E. Ho; Koyejo, Sanmi"
url: "https://aclanthology.org/2025.acl-long.341/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/42WJ28G6/2025 - Measuring Desired Group Discrimination in LLMs (DiffAware Benchmark Suite).pdf"
national_ethnic_cultural: "American"
cultures_nationalities_list: "American"
languages_list: "English"
religious_values: "N/A"
rv_islam: 10
rv_christianity: 10
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
newtags: "American, Islam, Bias & Fairness"
key_contribution: "Presented a benchmark suite (DiffAware) to measure 'desired group discrimination'—contexts where treating groups differently is appropriate (e.g., medical or legal distinctions)."
significance: "Critiques the standard 'color-blind' fairness approach, showing that bias mitigation strategies can backfire by preventing models from making necessary, context-aware distinctions between groups."
tags: 
abstract: "Algorithmic fairness has conventionally adopted the mathematically convenient perspective of racial color-blindness (i.e., difference unaware treatment). However, we contend that in a range of important settings, group difference awareness matters. For example, differentiating between groups may be necessary in legal contexts (e.g., the U.S. compulsory draft applies to men but not women) and harm assessments (e.g."
CONF-CC: "N/A"
DATE_ADDED: 20260208
LLM_assessed: "Llama-3, Mistral, Gemma-2, GPT-4o, Claude-3"
DATA_URL: "NA"
pdf_extract: "PDF Extracts/2025/2025-Wang-Measuring Desired Group Discrimination in LLMs.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Wang-Measuring Desired Group Discrimination in LLMs.pdf]]"
CONFERENCE: "ACL 2025"
ethics_overall: 95
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Bias & Fairness"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: "CN"
author_region: "East Asia"
author_global_north_south: "Ambiguous"
weird_score: 36
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark for bias and fairness"
data_metrics: "16k questions"
---
# Measuring Desired Group Discrimination in LLMs (DiffAware Benchmark Suite)

## Authors

[[Angelina Wang|Wang, Angelina]], [[Michelle Phan|Phan, Michelle]], [[Ho, Daniel E]], [[Sanmi Koyejo|Koyejo, Sanmi]]

## Links

- **ACL Anthology:** https://aclanthology.org/2025.acl-long.341/

## Abstract

Algorithmic fairness has conventionally adopted the mathematically convenient perspective of racial color-blindness (i.e., difference unaware treatment). However, we contend that in a range of important settings, group difference awareness matters. For example, differentiating between groups may be necessary in legal contexts (e.g., the U.S. compulsory draft applies to men but not women) and harm assessments (e.g., referring to girls as “terrorists” may be less harmful than referring to Muslim people as such). Thus, in contrast to most fairness work, we study fairness through the perspective of treating people differently — when it is contextually appropriate to. We first introduce an important distinction between descriptive (fact-based), normative (value-based), and correlation (association-based) benchmarks. This distinction is significant because each category requires separate interpretation and mitigation tailored to its specific characteristics. Then, we present a benchmark suite composed of eight different scenarios for a total of 16k questions that enables us to assess difference awareness. Finally, we show results across ten models that demonstrate difference awareness is a distinct dimension to fairness where existing bias mitigation strategies may backfire.

## Data Description

A benchmark suite of eight benchmarks (16,000 questions total) spanning descriptive and normative fairness evaluations, designed to measure 'difference awareness' in LLMs across social groups. Dataset was anonymized and submitted separately at time of publication.


## Notes

