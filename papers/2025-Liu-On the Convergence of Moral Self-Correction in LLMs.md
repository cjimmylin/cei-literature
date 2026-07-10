---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0097
type: conferencePaper
short_title: "On the Convergence of Moral Self-Correction in LLMs"
year: 2025
first_author: "[[Liu, Guangliang]]"
last_author: "[[Johnson, Kristen Marie]]"
authors: "Liu, Guangliang; Mao, Haitao; Cao, Bochuan; Xue, Zhiyu; Zhang, Xitong; Wang, Rongrong; Johnson, Kristen Marie"
authors_incomplete: false
url: "https://arxiv.org/abs/2510.07290"
external_pdf: "https://arxiv.org/pdf/2510.07290.pdf"
pdf_extract: "PDF Extracts/2025/2025-Liu-On the Convergence of Moral Self-Correction in LLMs.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Liu-On the Convergence of Moral Self-Correction in LLMs.pdf]]"
publication: "AACL-IJCNLP 2025"
CONF-CC: "AACL 2025"
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
abstract: "Large Language Models (LLMs) are able to improve their responses when instructed to do so, a capability known as self-correction. When instructions provide only a general and abstract goal without specific details about potential issues in the response, LLMs must rely on their internal knowledge to improve response quality, a process referred to as intrinsic selfcorrection. The empirical success of intrinsic self-correction is evident in various applications, but how and why it is effective..."
LLM_assessed: "GPT-4, Mistral"
DATA_URL: NA
CONFERENCE: "Other Conference"
ethics_overall: No
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Toxicity & Hate Speech"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: US
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: No
is_eval: No
is_dataset: No
data_description: N/A
data_metrics: "Not specified"
---
# On the Convergence of Moral Self-Correction in LLMs

## Authors

[[Guangliang Liu|Liu, Guangliang]], [[Mao, Haitao]], [[Cao, Bochuan]], [[Xue, Zhiyu]], [[Xitong Zhang|Zhang, Xitong]], [[Wang, Rongrong]], [[Kristen Marie Johnson|Johnson, Kristen Marie]]

## Metadata

**Authors:** Liu, Guangliang; Mao, Haitao; Cao, Bochuan; Xue, Zhiyu; Zhang, Xitong; Wang, Rongrong; Johnson, Kristen Marie

**Year:** 2025

**Type:** conferencePaper

**Venue:** AACL-IJCNLP 2025

## Links

- **arXiv:** https://arxiv.org/abs/2510.07290

## Abstract

Large Language Models (LLMs) are able to improve their responses when instructed to do so, a capability known as self-correction. When instructions provide only a general and abstract goal without specific details about potential issues in the response, LLMs must rely on their internal knowledge to improve response quality, a process referred to as intrinsic selfcorrection. The empirical success of intrinsic self-correction is evident in various applications, but how and why it is effective remains unknown. Focusing on moral self-correction in LLMs, we reveal a key characteristic of intrinsic self-correction: performance convergence through multi-round interactions; and provide a mechanistic analysis of this convergence behavior. Based on our experimental results and analysis, we uncover the underlying mechanism of convergence: consistently injected selfcorrection instructions activate moral concepts that reduce model uncertainty, leading to converged performance as the activated moral concepts stabilize over successive rounds. This paper demonstrates the strong potential of moral self-correction by showing that it exhibits a desirable property of converged performance. Warning: examples in this paper contain offensive languages

## Dataset Information

Multi-choice QA and language generation tasks; uses semantic uncertainty as uncertainty estimator

## Data Description

This paper uses the BBQ benchmark (social bias mitigation) and RealToxicityPrompts (text detoxification) to study moral self-correction convergence in LLMs. The primary model tested is Zephyr-7B (fine-tuned on Mistral-7B-v0.1), with GPT-4 used as backbone for vision-language tasks. Experiments involve multi-round self-correction across six tasks including social bias mitigation, jailbreak defense, VQA, text detoxification, commonsense generation, and visual grounding.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 19
**Implementation Readiness:** MEDIUM

## Tags

