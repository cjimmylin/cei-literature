---



































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0071
type: conferencePaper
short_title: "LLMEval-Med (Medical Safety & Ethics Component)"
year: 2025
first_author: "[[Zhang, Ming]]"
last_author: "[[Huang, Xuanjing]]"
authors: "Zhang, Ming; Shen, Yujiong; Li, Zelin; Sha, Huayu; Hu, Binze; Wang, Yuhui; Huang, Chenhao; Liu, Shichun; Tong, Jingqi; Jiang, Changhao; Chai, Mingxu; Xi, Zhiheng; Dou, Shihan; Gui, Tao; Zhang, Qi; Huang, Xuanjing"
authors_incomplete: false
url: "https://arxiv.org/abs/2506.04078"
external_pdf: "https://arxiv.org/pdf/2506.04078.pdf"
pdf_extract: "PDF Extracts/2025/2025-Zhang-LLMEval-Med Medical Safety & Ethics Component.md"
local_pdf: "[[PDFs/2025/2025-Zhang-LLMEval-Med Medical Safety & Ethics Component.pdf]]"
publication: "EMNLP 2025"
CONF-CC: "EMNLP 2025"
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
abstract: "Evaluating large language models (LLMs) in medicine is crucial because medical applications require high accuracy with little room for error. Current medical benchmarks have three main types: medical exam-based, comprehensive medical, and specialized assessments. However, these benchmarks have limitations in question design (mostly multiple-choice), data sources (often not derived from real clinical scenarios), and evaluation methods (poor assessment of complex reasoning)."
LLM_assessed: "Baichuan, DeepSeek, GPT-4, Llama-3, Mistral, Qwen, o1"
DATA_URL: "https://github.com/llmeval/LLMEval-Med"
CONFERENCE: "EMNLP 2025"
ethics_overall: 35
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark text corpus"
data_metrics: "2,996 questions"
---
# LLMEval-Med (Medical Safety & Ethics Component)

## Authors

[[Zhang, Ming]], [[Shen, Yujiong]], [[Li, Zelin]], [[Sha, Huayu]], [[Hu, Binze]], [[Wang, Yuhui]], [[Huang, Chenhao]], [[Liu, Shichun]], [[Tong, Jingqi]], [[Jiang, Changhao]], [[Chai, Mingxu]], [[Xi, Zhiheng]], [[Dou, Shihan]], [[Gui, Tao]], [[Zhang, Qi]], [[Huang, Xuanjing]]

## Metadata

**Authors:** Zhang, Ming; Shen, Yujiong; Li, Zelin; Sha, Huayu; Hu, Binze; Wang, Yuhui; Huang, Chenhao; Liu, Shichun; Tong, Jingqi; Jiang, Changhao; Chai, Mingxu; Xi, Zhiheng; Dou, Shihan; Gui, Tao; Zhang, Qi; Huang, Xuanjing

**Year:** 2025

**Type:** conferencePaper

**Venue:** EMNLP 2025

## Links

- **arXiv:** https://arxiv.org/abs/2506.04078
- **Code/Data:** https://github.com/llmeval/LLMEval-Med](https://github.com/llmeval/LLMEval-Med

## Abstract

Evaluating large language models (LLMs) in medicine is crucial because medical applications require high accuracy with little room for error. Current medical benchmarks have three main types: medical exam-based, comprehensive medical, and specialized assessments. However, these benchmarks have limitations in question design (mostly multiple-choice), data sources (often not derived from real clinical scenarios), and evaluation methods (poor assessment of complex reasoning). To address these issues, we present LLMEval-Medicine, a new benchmark covering five core medical areas, including 2,996 questions created from real-world electronic health records and expert-designed clinical scenarios. We also design an automated evaluation pipeline, incorporating expert-developed checklists into our LLM-as-Judge framework. Furthermore, our methodology validates machine scoring through human-machine agreement analysis, dynamically refining checklists and prompts based on expert feedback to ensure reliability. We evaluate 13 LLMs across three categories (specialized medical models, open-source models, and closed-source models) on LLMEvalMed, providing valuable insights for the safe and effective deployment of LLMs in medical domains. The dataset is released in https: //github.com/llmeval/LLMEval-Med.

## Dataset Information

2,996 questions total across 5 dimensions (Medical Knowledge, Language Understanding, Reasoning, Text Generation, Safety & Ethics)

## Data Description

LLMEval-Medicine: 2,996 questions derived from real-world clinical electronic health records covering 5 medical dimensions (knowledge, language understanding, reasoning, text generation, safety ethics) with expert-validated reference answers and evaluation checklists.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 14
**Implementation Readiness:** HIGH

## Tags

