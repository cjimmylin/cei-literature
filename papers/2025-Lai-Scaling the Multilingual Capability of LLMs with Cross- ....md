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
local_pdf: "[[PDFs/2025/2025-Lai-Scaling the Multilingual Capability of LLMs with Cross- ....pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "Chinese"
cultures_nationalities_list: "N/A"
languages_list: "Chinese, English, Multilingual"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: "Alpaca, BLOOM, BLOOM 251, BLOOM 35, BLOOM 48, BLOOM 83, ChatGPT, Llama, LLaMA 23.26, LLaMA 32, LLaMA 38.10, LLaMA 45.65, LLaMA 5.38, LLaMA 50.00, LLaMA 6.26, LLaMA 7.09, LLaMA 76.6, Llama-2, T5-LM, bloom-7b1"
DATA_URL: "https://github.com/boschresearch/ACL24-MLLM"
tags: 
abstract: "To democratize large language models (LLMs) to most natural languages, it is imperative to make these models capable of understanding and generating texts in many languages, in particular low-resource ones. While recent multilingual LLMs demonstrate remarkable performance in such capabilities, these LLMs still support a limited number of human languages due to the lack of training data for low-resource languages."
CONFERENCE: "ACL 2025"
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "Yes"
utilitarian_ethics: "No"
research_topic: "Machine Translation"
is_benchmark: "Yes"
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

Backfill summary: Models assessed include Alpaca, BLOOM, BLOOM 251, BLOOM 35, BLOOM 48, BLOOM 83, ChatGPT, Llama, LLaMA 23.26, LLaMA 32, LLaMA 38.10, LLaMA 45.65, LLaMA 5.38, LLaMA 50.00, LLaMA 6.26, LLaMA 7.09, LLaMA 76.6, Llama-2, T5-LM, bloom-7b1. Verified dataset/resource link: https://github.com/boschresearch/ACL24-MLLM.

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent D1
**Relevance:** Relevant to Chinese, Multilingual, English

## Tags

