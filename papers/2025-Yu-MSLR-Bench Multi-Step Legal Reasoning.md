---



































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0082
type: conferencePaper
short_title: "MSLR-Bench (Multi-Step Legal Reasoning)"
year: 2025
first_author: "[[Wenhan Yu]]"
last_author: "[[Lei Sha]]"
authors: Wenhan Yu; Xinbo Lin; Lanxin Ni; Jinhua Cheng; Lei Sha
url: "https://arxiv.org/abs/2511.07979"
external_pdf: "https://arxiv.org/pdf/2511.07979.pdf"
pdf_extract: "PDF Extracts/2025/2025-Yu-MSLR-Bench Multi-Step Legal Reasoning.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Yu-MSLR-Bench Multi-Step Legal Reasoning.pdf]]"
publication: "AAAI 2026"
CONF-CC: "AAAI 2026"
DATE_ADDED: 20260207
national_ethnic_cultural: "Chinese"
cultures_nationalities_list: "Chinese"
languages_list: "Chinese"
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
abstract: "As large language models (LLMs) exhibit advanced reasoning capabilities in different specialized domains, their application to legal reasoning tasks is actively being explored. The pursuit of justice in legal contexts demands not only correct outcomes but also reasoned elaboration, which necessitates deriving conclusions through logically justified and transparent argumentation. Current legal benchmarks, despite being cited as reasoning-focused, suffer from three critical limitations:..."
LLM_assessed: "DeepSeek, GPT-4, GPT-4o, Llama-3, Qwen"
DATA_URL: "https://github.com/yuwenhan07/MSLR-Bench"
CONFERENCE: "AAAI 2026"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Hallucination & Truthfulness"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark dataset"
data_metrics: "Not specified"
---
# MSLR-Bench (Multi-Step Legal Reasoning)

## Authors

[[Wenhan Yu]], [[Xinbo Lin]], [[Lanxin Ni]], [[Jinhua Cheng]], [[Lei Sha]]

## Metadata

**Authors:** Wenhan Yu, Xinbo Lin, Lanxin Ni, Jinhua Cheng, and Lei Sha

**Year:** 2025

**Type:** conferencePaper

**Venue:** AAAI 2026

## Links

- **arXiv:** https://arxiv.org/abs/2511.07979
- **Code/Data:** https://github.com/yuwenhan07/MSLR-Bench](https://github.com/yuwenhan07/MSLR-Bench

## Abstract

As large language models (LLMs) exhibit advanced reasoning capabilities in different specialized domains, their application to legal reasoning tasks is actively being explored. The pursuit of justice in legal contexts demands not only correct outcomes but also reasoned elaboration, which necessitates deriving conclusions through logically justified and transparent argumentation. Current legal benchmarks, despite being cited as reasoning-focused, suffer from three critical limitations: conflation of factual recall with genuine inference, fragmentation of holistic reasoning processes, and neglect of reasoning process quality. To bridge these gaps, we construct MSLR, the first Chinese multi-step legal reasoning dataset centered on legal decision-making. To align with real-world legal reasoning trajectories, MSLR employs the IRAC framework (Issue-Rule-Application-Conclusion) to capture expert reasoning traces from official legal decisions. In parallel, we design a scalable Human-LLM collaborative annotation pipeline that efficiently generates fine-grained step-level annotations while establishing a reusable methodological framework for multi-step reasoning datasets. Evaluation of a range of LLMs on MSLR reveals only modest performance, highlighting substantial challenges in adapting to complex legal reasoning. Further experiments show that Self-Initiated CoT prompts—created autonomously by the models—consistently improve reasoning coherence and output quality, outperforming Human-Designed CoT prompts, which often yield ambiguous results. This work contributes to the broader discourse on LLM reasoning and CoT strategies, offering practical insights and resources for future research. The dataset and code are publicly available at https://github.com/yuwenhan07/MSLR-Bench and https://law.sjtu.edu.cn/flszyjzx/index.html.

## Dataset Information

~1,400 cases with 60,000 step-level annotations

## Data Description

MSLR: the first Chinese multi-step legal reasoning dataset centered on insider trading cases, with 1,389 legal documents annotated using the IRAC framework with 60K step-level labels.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 14
**Implementation Readiness:** HIGH

## Tags

