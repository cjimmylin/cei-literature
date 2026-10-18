---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0842
type: preprint
short_title: "Divide-and-Conquer Attack: Harnessing the Power of LLM to Bypass Safety Filters of Text-to-Image Models"
year: 2023
first_author: "[[Deng, Yimo]]"
last_author: "[[Chen, Huangxun]]"
authors: "Deng, Yimo; Chen, Huangxun"
authors_incomplete: false
url: "https://arxiv.org/html/2312.07130v3"
external_pdf: "https://arxiv.org/pdf/2312.07130.pdf"
publication: arXiv
CONF-CC: Preprint
pdf_extract: "PDF Extracts/2023/2023-Deng-Divide-and-Conquer Attack Harnessing the Power of LLM to Bypass.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2023/2023-Deng-Divide-and-Conquer Attack Harnessing the Power of LLM to Bypass.pdf]]"
DATE_ADDED: 20260213
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
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
newtags: 
LLM_assessed: "GPT-4, GPT-3.5, Qwen"
DATA_URL: "https://github.com/researchcode003/DACA"
tags: 
abstract: "To prevent Text-to-Image (T2I) models from generating unethical images, people deploy safety filters to block inappropriate drawing prompts. Previous works have employed token replacement to search adversarial prompts that attempt to bypass these filters, but they has become ineffective as nonsensical tokens fail semantic logic checks. In this paper, we approach adversarial prompts from a different perspective."
CONFERENCE: Preprint
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
author_country: HK
author_region: "East Asia"
author_global_north_south: Ambiguous
weird_score: 53
is_benchmark: No
is_eval: No
is_dataset: Yes
data_description: Dataset
data_metrics: "Not specified"
---
# Divide-and-Conquer Attack: Harnessing the Power of LLM to Bypass Safety Filters of Text-to-Image Models

## Authors

[[Deng, Yimo]], [[Chen, Huangxun]]

## Metadata

**Authors:** Yimo Deng; Huangxun Chen

**Year:** 2023

**Type:** preprint

**Venue:** arXiv

**Languages:** Arabic, English, Multilingual

**Benchmark:** Divide-and-Conquer

## Links

- **arXiv:** https://arxiv.org/abs/2312.07130

## Abstract


To prevent Text-to-Image (T2I) models from generating unethical images, people deploy safety filters to block inappropriate drawing prompts. Previous works have employed token replacement to search adversarial prompts that attempt to bypass these filters, but they has become ineffective as nonsensical tokens fail semantic logic checks. In this paper, we approach adversarial prompts from a different perspective. We demonstrate that rephrasing a drawing intent into multiple benign descriptions of individual visual components can obtain an effective adversarial prompt. We propose a LLM-piloted multi-agent method named DACA to automatically complete intended rephrasing. Our method successfully bypasses the safety filters of DALL·E 3 and Midjourney to generate the intended images, achieving success rates of up to 76.7% and 64% in the one-time attack, and 98% and 84% in the re-use attack, respectively. We open-source our code and dataset on GitHub1. 1https://github.com/researchcode003/DACA

## Data Description

VBCDE dataset of 100 sensitive prompts across 5 categories (Violence, Bloody, Copyright, Discrimination, Erotic) for evaluating adversarial attacks against T2I model safety filters.


## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent D3
**Relevance:** Divide-and-Conquer benchmark for Arabic, Multilingual, English; ethics/values focus

## Tags

