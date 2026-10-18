---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0138
type: conferencePaper
short_title: "Value Portrait"
year: 2025
first_author: "[[Jongwook Han]]"
last_author: "[[Yohan Jo]]"
authors: "Jongwook Han; Dongmin Choi; Woojung Song; Eun-Ju Lee; Yohan Jo"
url: "https://arxiv.org/abs/2505.01015"
external_pdf: "https://arxiv.org/pdf/2505.01015.pdf"
pdf_extract: "PDF Extracts/2025/2025-Han-Value Portrait.md"
local_pdf: "[[Lit-WS-PDFs/2025/2025-Han-Value Portrait.pdf]]"
publication: "ACL 2025"
CONF-CC: "ACL 2025"
DATE_ADDED: 20260207
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: 
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
mp_schwartz: 50
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "Value Pluralism / Schwartz"
newtags: 
tags: 
abstract: "The importance of benchmarks for assessing the values of language models has been pronounced due to the growing need of more authentic, human-aligned responses. However, existing benchmarks rely on human or machine annotations that are vulnerable to value-related biases. Furthermore, the tested scenarios often diverge from real-world contexts in which models are commonly used to generate text and express values."
LLM_assessed: "Claude, Gemma, Gemma-2, GPT-4, GPT-4o, Llama-3, Mistral, Qwen, o1"
DATA_URL: "https://github.com/holi-lab/ValuePortrait"
CONFERENCE: "ACL 2025"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 5
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
author_country: CA
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 86
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark for bias and fairness dataset"
data_metrics: "Not specified"
---
# Value Portrait

## Authors

[[Jongwook Han]], [[Dongmin Choi]], [[Woojung Song]], [[Eun-Ju Lee]], [[Yohan Jo]]

## Metadata

**Authors:** Jongwook Han, Dongmin Choi, Woojung Song, Eun-Ju Lee, Yohan Jo

**Year:** 2025

**Type:** conferencePaper

**Venue:** ACL 2025

## Links

- **arXiv:** https://arxiv.org/abs/2505.01015

## Abstract

The importance of benchmarks for assessing the values of language models has been pronounced due to the growing need of more authentic, human-aligned responses. However, existing benchmarks rely on human or machine annotations that are vulnerable to value-related biases. Furthermore, the tested scenarios often diverge from real-world contexts in which models are commonly used to generate text and express values. To address these issues, we propose the Value Portrait benchmark, a reliable framework for evaluating LLMs’ value orientations with two key characteristics. First, the benchmark consists of items that capture real-life user-LLM interactions, enhancing the relevance of assessment results to real-world LLM usage. Second, each item is rated by human subjects based on its similarity to their own thoughts, and correlations between these ratings and the subjects’ actual value scores are derived. This psychometrically validated approach ensures that items strongly correlated with specific values serve as reliable items for assessing those values. Through evaluating 44 LLMs with our benchmark, we find that these models prioritize Benevolence, Security, and Self-Direction values while placing less emphasis on Tradition, Power, and Achievement values. Also, our analysis reveals biases in how LLMs perceive various demographic groups, deviating from real human data.

## Dataset Information

Psychometrically validated items with human-subject correlation data; evaluates 10 Schwartz value dimensions

## Data Description

Value Portrait is a psychometrically validated benchmark of 520 unique query-response pairs from real human-LLM interactions (ShareGPT, LMSYS, Reddit, Dear Abby), each annotated on 15 psychological dimensions (10 Schwartz values + 5 Big Five traits) by human participants via correlation analysis, used to evaluate 44 LLMs.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 19, Agent 1
**Implementation Readiness:** HIGH

## Tags

