---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0848
type: preprint
short_title: "CodeMixBench: Evaluating Large Language Models on Code Generation with Code-Mixed Prompts"
year: 2025
first_author: "[[Yilun Yang]]"
last_author: "[[Yilun Yang]]"
authors: "Yilun Yang"
url: "https://arxiv.org/html/2505.05063v1"
external_pdf: "https://arxiv.org/pdf/2505.05063.pdf"
publication: arXiv
CONF-CC: Preprint
pdf_extract: "PDF Extracts/2025/2025-Yang-CodeMixBench Evaluating Large Language Models on Code Generation with.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Yang-CodeMixBench Evaluating Large Language Models on Code Generation with.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: Multicultural/Cross-cultural
cultures_nationalities_list: Multicultural/Cross-cultural
languages_list: "Code-switching, Multilingual"
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
LLM_assessed: "CodeLlama, DeepSeek, Gemma, LLaMA, Llama-3, Phi-3, Qwen, StarCoder"
DATA_URL: NA
tags: 
abstract: "Large Language Models (LLMs) have achieved remarkable success in code generation tasks, powering various applications like code completion, debugging, and programming assistance. However, existing benchmarks such as HumanEval, MBPP, and BigCodeBench primarily evaluate LLMs on English-only prompts, overlooking the real-world scenario where multilingual developers often use codemixed language while interacting with LLMs."
CONFERENCE: Preprint
ethics_overall: No
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "AI Safety & Alignment"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: IN
author_region: "South Asia"
author_global_north_south: "Global South"
weird_score: 36
is_benchmark: Yes
is_eval: Yes
is_dataset: No
data_description: "Multilingual benchmark"
data_metrics: "Not specified"
---
# CodeMixBench: Evaluating Large Language Models on Code Generation with Code-Mixed Prompts

## Authors

[[Yilun Yang]]

## Metadata

**Authors:** Yilun Yang

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** Code-switching, English, Hindi

**Benchmark:** CodeMixBench

## Links

- **arXiv:** https://arxiv.org/abs/2505.05063

## Abstract


Large Language Models (LLMs) have achieved remarkable success in code generation tasks, powering various applications like code completion, debugging, and programming assistance. However, existing benchmarks such as HumanEval, MBPP, and BigCodeBench primarily evaluate LLMs on English-only prompts, overlooking the real-world scenario where multilingual developers often use codemixed language while interacting with LLMs. To address this gap, we introduce CodeMixBench, a novel benchmark designed to evaluate the robustness of LLMs on code generation from code-mixed prompts. Built upon BigCodeBench, CodeMixBench introduces controlled code-mixing (CMD) into the natural language parts of prompts across three language pairs: Hinglish (Hindi-English), Spanish-English, and Chinese Pinyin-English. We comprehensively evaluate a diverse set of open-source code generation models ranging from 1.5B to 15B parameters. Our results show that code-mixed prompts consistently degrade Pass@1 performance compared to their English-only counterparts, with performance drops increasing under higher CMD levels for smaller models. CodeMixBench provides a realistic evaluation framework for studying multilingual code generation and highlights new challenges and directions for building robust code generation models that generalize well across diverse linguistic settings.

## Data Description

CodeMixBench (code generation): 6,840 code-mixed prompts derived from BigCodeBench across 3 language mixes (Hinglish, Spanish-English, Chinese Pinyin-English) at 2 code-mixing degree levels (CMD 0.6 and 0.9), covering 1,140 unique programming tasks for evaluating code generation robustness to multilingual prompts.


## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent D3
**Relevance:** CodeMixBench benchmark for Hindi, Code-switching, English

## Tags

