---



































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0056
type: conferencePaper
short_title: "From Surveys to Narratives: Rethinking Cultural Value Adaptation in LLMs"
year: 2025
first_author: "[[Muhammad Farid Adilazuarda]]"
last_author: "[[Alham Fikri Aji]]"
authors: "Muhammad Farid Adilazuarda; Chen Cecilia Liu; Iryna Gurevych; Alham Fikri Aji"
url: "https://arxiv.org/abs/2505.16408"
external_pdf: "https://arxiv.org/pdf/2505.16408.pdf"
pdf_extract: "PDF Extracts/2025/2025-Adilazuarda-From Surveys to Narratives Rethinking Cultural Value Adaptation in.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Adilazuarda-From Surveys to Narratives Rethinking Cultural Value Adaptation in.pdf]]"
publication: "EMNLP 2025"
CONF-CC: "EMNLP 2025"
DATE_ADDED: 20260207
national_ethnic_cultural: "Multicultural/Cross-cultural"
cultures_nationalities_list: "Multicultural/Cross-cultural"
languages_list: "Arabic, Bengali, Chinese, English, German, Greek, Korean, Portuguese, Spanish, Turkish"
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
abstract: "Adapting cultural values in Large Language Models (LLMs) presents significant challenges, particularly due to biases and limited training data. Prior work primarily aligns LLMs with different cultural values using World Values Survey (WVS) data. However, it remains unclear whether this approach effectively captures cultural nuances or produces distinct cultural representations for various downstream tasks."
LLM_assessed: "Llama-3, Gemma-2, Qwen-2"
DATA_URL: "https://github.com/faridlazuarda/from-surveys-to-narratives"
CONFERENCE: "EMNLP 2025"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Social & Cultural Values"
is_benchmark: "No"
is_eval: Yes
is_dataset: No
data_description: "Dataset"
data_metrics: "Not specified"
---
# From Surveys to Narratives: Rethinking Cultural Value Adaptation in LLMs

## Authors

[[Muhammad Farid Adilazuarda]], [[Chen Cecilia Liu]], [[Iryna Gurevych]], [[Alham Fikri Aji]]

## Metadata

**Authors:** Muhammad Farid Adilazuarda; Chen Cecilia Liu; Iryna Gurevych; Alham Fikri Aji

**Year:** 2025

**Type:** conferencePaper

**Venue:** EMNLP 2025

## Links

- **arXiv:** https://arxiv.org/abs/2505.16408

## Abstract

Adapting cultural values in Large Language Models (LLMs) presents significant challenges, particularly due to biases and limited training data. Prior work primarily aligns LLMs with different cultural values using World Values Survey (WVS) data. However, it remains unclear whether this approach effectively captures cultural nuances or produces distinct cultural representations for various downstream tasks. In this paper, we systematically investigate WVS-based training for cultural value adaptation and find that relying solely on survey data can homogenize cultural norms and interfere with factual knowledge. To investigate these issues, we augment WVS with encyclopedic and scenario-based cultural narratives from Wikipedia and NormAd. While these narratives may have variable effects on downstream tasks, they consistently improve cultural distinctiveness than survey data alone. Our work highlights the inherent complexity of aligning cultural values with the goal of guiding task-specific behavior. We release our code at https://github.com/faridlazuarda/ from-surveys-to-narratives.

## Dataset Information

See report

## Data Description

The paper investigates cultural value adaptation in LLMs using World Values Survey data augmented with Wikipedia and NormAd narratives. Three model families are tested via LoRA fine-tuning across 10 linguistic-cultural settings: Llama-3.1-8B (base and instruction-tuned), Gemma-2-9B-IT, and Qwen-2.5-7B-IT, evaluating offensiveness classification performance and factual knowledge retention on MMLU.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 7-8
**Implementation Readiness:** HIGH

## Tags

