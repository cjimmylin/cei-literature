---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0230
type: conferencePaper
short_title: WalledEval
year: 2024
first_author: "[[Gupta, Prannaya]]"
last_author: "[[Poria, Soujanya]]"
authors: "[[Gupta, Prannaya]]; [[Yau, Le Qi]]; [[Low, Hao Han]]; [[Lee, I-Shiang]]; [[Lim, Hugo Maximus]]; [[Teoh, Yu Xin]]; [[Koh, Jia Hng]]; [[Liew, Dar Win]]; [[Bhardwaj, Rishabh]]; [[Bhardwaj, Rajat]]; [[Poria, Soujanya]]"
authors_incomplete: false
url: "https://arxiv.org/abs/2408.03837"
external_pdf: "https://arxiv.org/pdf/2408.03837.pdf"
pdf_extract: "PDF Extracts/0000/2024-Gupta-WalledEval.md"
local_pdf: "[[PDFs/2024/2024-Gupta-WalledEval.pdf]]"
publication: "EMNLP 2024"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "Multilingual"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "WALLEDEVAL is a comprehensive AI safety testing toolkit designed to evaluate large language models (LLMs). It accommodates a diverse range of models, including both open-weight and API-based ones, and features over 35 safety benchmarks covering areas such as multilingual safety, exaggerated safety, and prompt injections. The framework supports both LLM and judge benchmarking and incorporates custom mutators to test safety against various text-style mutations, such as future tense and..."
LLM_assessed: "Llama-2, Llama-3, Mistral, Mixtral, Qwen, Gemma, Phi, GPT-4, Claude, Gemini"
DATA_URL: "https://github.com/walledai/walledeval"
research_topic: "Other"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Multilingual benchmark for ai safety text corpus"
data_metrics: "Not specified"
---
# WalledEval

## Authors

[[Gupta, Prannaya]], [[Yunjia Qi|Yau, Le Qi]], [[Low, Hao Han]], [[Lee, I-Shiang]], [[Lim, Hugo Maximus]], [[Teoh, Yu Xin]], [[Koh, Jia Hng]], [[Liew, Dar Win]], [[Rishabh Bhardwaj|Bhardwaj, Rishabh]], [[Bhardwaj, Rajat]], [[Soujanya Poria|Poria, Soujanya]]

## Metadata

**Authors:** Gupta, Prannaya; Yau, Le Qi; Low, Hao Han; Lee, I-Shiang; Lim, Hugo Maximus; Teoh, Yu Xin; Koh, Jia Hng; Liew, Dar Win; Bhardwaj, Rishabh; Bhardwaj, Rajat; Poria, Soujanya

**Year:** 2024

**Type:** conferencePaper

**Venue:** EMNLP 2024

## Links

- **arXiv:** https://arxiv.org/abs/2408.03837
- **Code/Data:** https://github.com/walledai/walledeval

## Abstract

WALLEDEVAL is a comprehensive AI safety testing toolkit designed to evaluate large language models (LLMs). It accommodates a diverse range of models, including both open-weight and API-based ones, and features over 35 safety benchmarks covering areas such as multilingual safety, exaggerated safety, and prompt injections. The framework supports both LLM and judge benchmarking and incorporates custom mutators to test safety against various text-style mutations, such as future tense and paraphrasing. Additionally, WALLEDEVAL introduces WALLEDGUARD, a new, small, and performant content moderation tool, and two datasets: SGXSTEST and HIXSTEST, which serve as benchmarks for assessing the exaggerated safety of LLMs and judges in cultural contexts. We make WALLEDEVAL publicly available at https: //github.com/walledai/walledeval.

## Dataset Information

Size: 35+ safety benchmarks integrated

## Data Description

WalledEval is a comprehensive AI safety evaluation toolkit hosting over 35 safety benchmarks covering harmful behavior, refusal behavior, multilingual safety, exaggerated safety, and prompt injections. The framework evaluates a wide range of open-weight and closed-weight LLMs on datasets including HarmBench, AdvBench, CatQA, XSTest, and the newly introduced SGXSTest and HIXSTest cultural safety benchmarks. It also introduces WalledGuard, a 494M-parameter content moderation model.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 2, Agent 16
**Implementation Readiness:** HIGH

## Tags

