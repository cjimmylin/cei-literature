---





































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0782
type: conferencePaper
short_title: "Scaling the Multilingual Capability of LLMs with Cross- ..."
year: 2025
first_author: "[[Lai, Wen]]"
last_author: "[[Fraser, Alexander]]"
authors: "Lai, Wen; Mesgar, Mohsen; Fraser, Alexander"
authors_incomplete: false
url: "https://aclanthology.org/2024.findings-acl.488.pdf"
external_pdf: "https://arxiv.org/pdf/2406.01771v1.pdf"
publication: "ACL Anthology"
CONF-CC: "N/A"
pdf_extract: "PDF Extracts/2025/2025-Lai-Scaling the Multilingual Capability of LLMs with Cross- ....md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Lai-Scaling the Multilingual Capability of LLMs with Cross- ....pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "Multilingual"
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
LLM_assessed: "BLOOM, LLaMA, Llama-2"
DATA_URL: "https://github.com/boschresearch/ACL24-MLLM"
tags: 
abstract: "To democratize large language models (LLMs) to most natural languages, it is imperative to make these models capable of understanding and generating texts in many languages, in particular low-resource ones. While recent multilingual LLMs demonstrate remarkable performance in such capabilities, these LLMs still support a limited number of human languages due to the lack of training data for low-resource languages."
CONFERENCE: "ACL 2025"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "Machine Translation"
is_benchmark: No
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Multilingual benchmark dataset"
data_metrics: "100 languages; 30 languages"
---
# Scaling the Multilingual Capability of LLMs with Cross- ...

## Authors

[[Lai, Wen]], [[Mesgar, Mohsen]], [[Fraser, Alexander]]

## Metadata

**Authors:** Wen Lai; Mohsen Mesgar; Alexander Fraser

**Year:** 2025

**Type:** conferencePaper

**Venue:** ACL Anthology

**Languages:** Chinese, English, Multilingual

## Links

- **URL:** https://aclanthology.org/2024.findings-acl.488.pdf

## Abstract


To democratize large language models (LLMs) to most natural languages, it is imperative to make these models capable of understanding and generating texts in many languages, in particular low-resource ones. While recent multilingual LLMs demonstrate remarkable performance in such capabilities, these LLMs still support a limited number of human languages due to the lack of training data for low-resource languages. Moreover, these LLMs are not yet aligned with human preference for downstream tasks, which is crucial for the success of LLMs in English. In this paper, we introduce xLLaMA-100 and xBLOOM-100 (collectively xLLMs-100), which scale the multilingual capabilities of LLaMA and BLOOM to 100 languages. To do so, we construct two datasets: a multilingual instruction dataset including 100 languages, which represents the largest language coverage to date, and a crosslingual human feedback dataset encompassing 30 languages. We perform multilingual instruction tuning on the constructed instruction data and further align the LLMs with human feedback using the DPO algorithm on our crosslingual human feedback dataset. We evaluate the multilingual understanding and generating capabilities of xLLMs-100 on five multilingual benchmarks. Experimental results show that xLLMs-100 consistently outperforms its peers across the benchmarks by considerable margins, defining a new state-of-the-art multilingual LLM that supports 100 languages1.

## Data Description

Two novel datasets released: a multilingual instruction-following dataset covering 100 languages (translated from Alpaca) and a cross-lingual human feedback dataset covering 30 languages, used to train xLLaMA-100 and xBLOOM-100.


## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent D1
**Relevance:** Relevant to Chinese, Multilingual, English

## Tags

