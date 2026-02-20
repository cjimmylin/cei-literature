---








Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0207
type: conferencePaper
short_title: "OpenEval -- Benchmarking Chinese LLMs across Capability, Alignment, and Safety"
year: 2024
first_author: "[[C. Li]]"
last_author: "[[Deyi Xiong]]"
authors: "Chuang Liu; Linhao Yu; Jiaxuan Li; Renren Jin; Yufei Huang; Ling Shi; Junhui Zhang; Xinmeng Ji; Tingting Cui; Tao Liu; Jinwang Song; Hongying Zan; Sun Li; Deyi Xiong"
url: "https://arxiv.org/abs/2403.12316"
external_pdf: "https://arxiv.org/pdf/2403.12316.pdf"
pdf_extract: "PDF Extracts/2024/2024-Li-OpenEval - Benchmarking Chinese LLMs across Capability Alignment and.md"
local_pdf: "[[PDFs/2024/2024-Li-OpenEval - Benchmarking Chinese LLMs across Capability Alignment and.pdf]]"
publication: "ACL 2024"
CONF-CC: "ACL 2024"
DATE_ADDED: 20260207
national_ethnic_cultural: "Chinese"
cultures_nationalities_list: "Chinese"
languages_list: "Chinese"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "Value Pluralism / Schwartz"
newtags: 
tags: 
abstract: "The rapid development of Chinese large language models (LLMs) poses big challenges for efficient LLM evaluation. While current initiatives have introduced new benchmarks or evaluation platforms for assessing Chinese LLMs, many of these focus primarily on capabilities, usually overlooking potential alignment and safety issues. To address this gap, we introduce OpenEval, an evaluation testbed that benchmarks Chinese LLMs across capability, alignment and safety."
LLM_assessed: "Baichuan2, ChatGPT, GPT-3, GPT-3.5, GPT-4, InternLM, InternLM Team, InternLM-Chat, Qwen, Qwen Qwen, Qwen Table, Qwen technical, Qwen-72B, Qwen-7B, Yi 16, Yi-34B, alpaca, Llama"
DATA_URL: "https://github.com/01-ai/Yi"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for ai safety dataset"
data_metrics: "7 datasets; 6 datasets"
CONFERENCE: "ACL 2024"
---
# OpenEval -- Benchmarking Chinese LLMs across Capability, Alignment, and Safety

## Authors

[[Chuang Liu]], [[Linhao Yu]], [[Jiaxuan Li]], [[Renren Jin]], [[Yufei Huang]], [[Ling Shi]], [[Junhui Zhang]], [[Xinmeng Ji]], [[Tingting Cui]], [[Tao Liu]], [[Jinwang Song]], [[Hongying Zan]], [[Sun Li]], [[Deyi Xiong]]

## Metadata

**Authors:** Li, C. et al

**Year:** 2024

**Type:** conferencePaper

**Venue:** ACL 2024

## Links

- **arXiv:** https://arxiv.org/abs/2403.12316

## Abstract

The rapid development of Chinese large language models (LLMs) poses big challenges for efficient LLM evaluation. While current initiatives have introduced new benchmarks or evaluation platforms for assessing Chinese LLMs, many of these focus primarily on capabilities, usually overlooking potential alignment and safety issues. To address this gap, we introduce OpenEval, an evaluation testbed that benchmarks Chinese LLMs across capability, alignment and safety. For capability assessment, we include 12 benchmark datasets to evaluate Chinese LLMs from 4 sub-dimensions: NLP tasks, disciplinary knowledge, commonsense reasoning and mathematical reasoning. For alignment assessment, OpenEval contains 7 datasets that examines the bias, offensiveness and illegalness in the outputs yielded by Chinese LLMs. To evaluate safety, especially anticipated risks (e.g., power-seeking, self-awareness) of advanced LLMs, we include 6 datasets. In addition to these benchmarks, we have implemented a phased public evaluation and benchmark update strategy to ensure that OpenEval is in line with the development of Chinese LLMs or even able to provide cutting-edge benchmark datasets to guide the development of Chinese LLMs. In our first public evaluation, we have tested a range of Chinese LLMs, spanning from 7B to 72B parameters, including both open-source and proprietary models. Evaluation results indicate that while Chinese LLMs have shown impressive performance in certain tasks, more attention should be directed towards broader aspects such as commonsense reasoning, alignment, and safety.

## Dataset Information

35 benchmark datasets total

## Data Description

OpenEval is a comprehensive evaluation platform for Chinese LLMs encompassing 25 benchmark datasets organized into 53 tasks across capability, alignment, and safety dimensions. The benchmark contains approximately 300K questions covering NLP tasks, disciplinary knowledge, commonsense reasoning, mathematical reasoning, bias, offensiveness, illegality, and advanced AI safety risks. The platform evaluated 14 Chinese LLMs (9 open-source ranging from 6B to 72B parameters, plus 5 proprietary models) under zero-shot settings.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 9-11
**Implementation Readiness:** HIGH

## Tags

