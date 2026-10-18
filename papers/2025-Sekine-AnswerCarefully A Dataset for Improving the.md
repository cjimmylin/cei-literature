---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0328
type: preprint
short_title: "AnswerCarefully A Dataset for Improving the"
year: 2025
first_author: "[[Hisami Suzuki]]"
last_author: "[[Satoshi Sekine]]"
authors: "Hisami Suzuki; Satoru Katsumata; Takashi Kodama; Tetsuro Takahashi; Kouta Nakayama; Satoshi Sekine"
authors_incomplete: false
url: "https://arxiv.org/abs/2506.02372"
external_pdf: "https://arxiv.org/pdf/2506.02372.pdf"
pdf_extract: "PDF Extracts/2025/2025-Sekine-AnswerCarefully A Dataset for Improving the.md"
local_pdf: "[[Lit-WS-PDFs/2025/2025-Sekine-AnswerCarefully A Dataset for Improving the.pdf]]"
publication: "arXiv preprint (NII LLM-jp project)"
CONF-CC: Preprint
DATE_ADDED: 20260213
national_ethnic_cultural: Japanese
cultures_nationalities_list: Japanese
languages_list: Japanese
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
abstract: "In this paper we present AnswerCarefully, a dataset for promoting the safety and appropriateness of Japanese LLM outputs. The dataset consists of 1,800 pairs of questions and reference answers, where the questions require special attention in answering. It covers a wide range of risk categories established in prior Englishlanguage datasets, but the data samples are original in that they are manually created to reflect the socio-cultural context of LLM usage in Japan."
LLM_assessed: "GPT-3.5, GPT-4, Claude-3, Llama-3, Qwen-2, Gemma-2"
DATA_URL: "https://huggingface.co/datasets/llm-jp/AnswerCarefully"
CONFERENCE: Preprint
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 5
contractarian_ethics: 0
care_ethics: 0
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: JP
author_region: "East Asia"
author_global_north_south: "Global North"
weird_score: 65
is_benchmark: Yes
is_eval: No
is_dataset: Yes
data_description: "Benchmark for ai safety dataset"
data_metrics: "Not specified"
---
# AnswerCarefully: A Dataset for Improving the Safety of Japanese LLM Output

## Authors

[[Hisami Suzuki]], [[Satoru Katsumata]], [[Takashi Kodama]], [[Tetsuro Takahashi]], [[Kouta Nakayama]], [[Satoshi Sekine]]

## Metadata

**Authors:** Hisami Suzuki, Satoru Katsumata, Takashi Kodama, Tetsuro Takahashi, Kouta Nakayama, Satoshi Sekine

**Year:** 2025

**Type:** preprint

**Venue:** arXiv preprint (NII LLM-jp project)

## Links

- **arXiv:** https://arxiv.org/abs/2506.02372
- **Code/Data:** https://huggingface.co/datasets/llm-jp/AnswerCarefully

## Abstract

AnswerCarefully is a safety dataset created by Japan's National Institute of Informatics (NII) LLM-jp project, consisting of 1,800 manually created question-answer pairs where questions require special attention. Unlike translations of English safety datasets, this is originally created to reflect the socio-cultural context of LLM usage in Japan, including culturally-specific safety risks. Fine-tuning on this data improved safety without reducing utility. While not explicitly a religious values benchmark, it captures Japanese cultural sensitivities that are deeply informed by Shinto/Buddhist/Confucian social norms.

## Dataset Information

1,800 question-answer pairs


## Data Description

AnswerCarefully (AC) is a 1,800-pair Japanese safety dataset of questions requiring careful handling, covering broad risk categories derived from Do-Not-Answer, with reference answers for instruction tuning. It serves both as a fine-tuning corpus for safety alignment and as a benchmark for evaluating 12 Japanese LLMs.


## Notes

**Source:** Religious & Language Search (2026-02-13), R6
**Implementation Readiness:** HIGH

## Tags
