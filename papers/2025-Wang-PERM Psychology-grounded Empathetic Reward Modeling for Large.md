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
local_pdf: "[[PDFs/2025/2025-Wang-PERM Psychology-grounded Empathetic Reward Modeling for Large.pdf]]"
publication: "arXiv preprint"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "Large Language Models (LLMs) are increasingly deployed in human-centric applications, yet they often fail to provide substantive emotional support. While Reinforcement Learning (RL) has been utilized to enhance empathy of LLMs, existing reward models typically evaluate empathy from a single perspective, overlooking the inherently bidirectional interaction nature of empathy between the supporter and seeker as defined by Empathy Cycle theory."
LLM_assessed: "GPT-4o, Qwen"
DATA_URL: "https://github.com/ZhengWwwq/PERM"
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Machine Learning"
is_benchmark: "Yes"
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

This paper uses the EmpatheticDialogues dataset augmented with GPT-4o-generated scenario descriptions and user personas for training, comprising 3,000 samples. Evaluation is conducted on EQ-Bench3, a comprehensive emotional intelligence benchmark, as well as a daily conversation benchmark and a user study. The PERM reward modeling framework is applied to fine-tune Qwen2.5-7B-Instruct via GRPO reinforcement learning, using GPT-4o-mini as the judge LLM for multi-perspective empathy scoring.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 15
**Implementation Readiness:** HIGH

## Tags

