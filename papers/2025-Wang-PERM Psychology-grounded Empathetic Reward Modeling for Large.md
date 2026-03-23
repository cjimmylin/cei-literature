---



































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0099
type: preprint
short_title: "PERM: Psychology-grounded Empathetic Reward Modeling for Large Language Models"
year: 2025
first_author: "[[Chengbing Wang]]"
last_author: "[[Fuli Feng]]"
authors: "Chengbing Wang; Wuqiang Zheng; Yang Zhang; Fengbin Zhu; Junyi Cheng; Yi Xie; Wenjie Wang; Fuli Feng"
url: "https://arxiv.org/abs/2601.10532"
external_pdf: "https://arxiv.org/pdf/2601.10532.pdf"
pdf_extract: "PDF Extracts/2025/2025-Wang-PERM Psychology-grounded Empathetic Reward Modeling for Large.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Wang-PERM Psychology-grounded Empathetic Reward Modeling for Large.pdf]]"
publication: "arXiv preprint"
CONF-CC: "Preprint"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
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
abstract: "Large Language Models (LLMs) are increasingly deployed in human-centric applications, yet they often fail to provide substantive emotional support. While Reinforcement Learning (RL) has been utilized to enhance empathy of LLMs, existing reward models typically evaluate empathy from a single perspective, overlooking the inherently bidirectional interaction nature of empathy between the supporter and seeker as defined by Empathy Cycle theory."
LLM_assessed: "GPT-4o, Qwen, RoBERTa"
DATA_URL: "https://github.com/ZhengWwwq/PERM"
CONFERENCE: "Preprint"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 5
contractarian_ethics: 0
care_ethics: 95
research_topic: "Machine Learning"
is_benchmark: No
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark text corpus for conversational ai"
data_metrics: "Not specified"
---
# PERM: Psychology-grounded Empathetic Reward Modeling for Large Language Models

## Authors

[[Chengbing Wang]], [[Wuqiang Zheng]], [[Yang Zhang]], [[Fengbin Zhu]], [[Junyi Cheng]], [[Yi Xie]], [[Wenjie Wang]], [[Fuli Feng]]

## Metadata

**Authors:** Chengbing Wang; Wuqiang Zheng; Yang Zhang; Fengbin Zhu; Junyi Cheng; Yi Xie; Wenjie Wang; Fuli Feng

**Year:** 2025

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2601.10532
- **Code/Data:** https://github.com/ZhengWwwq/PERM](https://github.com/ZhengWwwq/PERM

## Abstract

Large Language Models (LLMs) are increasingly deployed in human-centric applications, yet they often fail to provide substantive emotional support. While Reinforcement Learning (RL) has been utilized to enhance empathy of LLMs, existing reward models typically evaluate empathy from a single perspective, overlooking the inherently bidirectional interaction nature of empathy between the supporter and seeker as defined by Empathy Cycle theory. To address this limitation, we propose Psychology-grounded Empathetic Reward Modeling (PERM). PERM operationalizes empathy evaluation through a bidirectional decomposition: 1) Supporter perspective, assessing internal resonation and communicative expression; 2) Seeker perspective, evaluating emotional reception. Additionally, it incorporates a bystander perspective to monitor overall interaction quality. Extensive experiments on a widely-used emotional intelligence benchmark and an industrial daily conversation dataset demonstrate that PERM outperforms state-ofthe-art baselines by over 10%. Furthermore, a blinded user study reveals a 70% preference for our approach, highlighting its efficacy in generating more empathetic responses1.

## Dataset Information

Training data built on EmpatheticDialogues, augmented with GPT-4o scenario expansions and user personas; evaluated on EQ-Bench3

## Data Description

A psychology-grounded empathetic reward modeling dataset built upon EmpatheticDialogues, expanded with GPT-4o-generated responses. The dataset supports training reward models for empathy evaluation in LLMs using a bidirectional decomposition framework.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 15
**Implementation Readiness:** HIGH

## Tags

