---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0116
type: conferencePaper
short_title: "SORRY-Bench -- Systematically Evaluating LLM Safety Refusal"
year: 2025
first_author: "[[Xie, Tinghao]]"
last_author: "[[Mittal, Prateek]]"
authors: "Xie, Tinghao; Qi, Xiangyu; Zeng, Yi; Huang, Yangsibo; Sehwag, Udari Madhushani; Huang, Kaixuan; He, Luxi; Wei, Boyi; Li, Dacheng; Sheng, Ying; Jia, Ruoxi; Li, Bo; Li, Kai; Chen, Danqi; Henderson, Peter; Mittal, Prateek"
authors_incomplete: false
url: "https://arxiv.org/abs/2406.14598"
external_pdf: "https://arxiv.org/pdf/2406.14598.pdf"
pdf_extract: "PDF Extracts/2025/2025-Xie-SORRY-Bench - Systematically Evaluating LLM Safety Refusal.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Xie-SORRY-Bench - Systematically Evaluating LLM Safety Refusal.pdf]]"
publication: "ICLR 2025"
CONF-CC: "ICLR 2025"
DATE_ADDED: 20260207
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: Multilingual
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
abstract: "Evaluating aligned large language models’ (LLMs) ability to recognize and reject unsafe user requests is crucial for safe, policy-compliant deployments. Existing evaluation efforts, however, face three limitations that we address with SORRYBench, our proposed benchmark. First, existing methods often use coarse-grained taxonomies of unsafe topics, and are over-representing some fine-grained topics. For example, among the ten existing datasets that we evaluated, tests for refusals of self-harm..."
LLM_assessed: "GPT-3.5, GPT-4o, Claude-2, Gemini, Gemma, Llama-2, Llama-3, Mistral, Qwen, Vicuna, BERT"
DATA_URL: "https://sorry-bench.github.io"
CONFERENCE: "ICLR 2025"
ethics_overall: No
virtue_ethics: 0
deontological_ethics: 10
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "AI Safety & Alignment"
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
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark for ai safety dataset"
data_metrics: "Not specified"
---
# SORRY-Bench -- Systematically Evaluating LLM Safety Refusal

## Authors

[[Xie, Tinghao]], [[Qi, Xiangyu]], [[Yi Zeng|Zeng, Yi]], [[Huang, Yangsibo]], [[Udari Madhushani Sehwag|Sehwag, Udari Madhushani]], [[Huang, Kaixuan]], [[He, Luxi]], [[Wei, Boyi]], [[Li, Dacheng]], [[Sheng, Ying]], [[Ruoxi Jia|Jia, Ruoxi]], [[Bo Li|Li, Bo]], [[Li, Kai]], [[Danqi Chen|Chen, Danqi]], [[Peter Henderson|Henderson, Peter]], [[Prateek Mittal|Mittal, Prateek]]

## Metadata

**Authors:** Xie, Tinghao; Qi, Xiangyu; Zeng, Yi; Huang, Yangsibo; Sehwag, Udari Madhushani; Huang, Kaixuan; He, Luxi; Wei, Boyi; Li, Dacheng; Sheng, Ying; Jia, Ruoxi; Li, Bo; Li, Kai; Chen, Danqi; Henderson, Peter; Mittal, Prateek

**Year:** 2025

**Type:** conferencePaper

**Venue:** ICLR 2025

## Links

- **arXiv:** https://arxiv.org/abs/2406.14598
- **Code/Data:** https://github.com/SORRY-Bench/sorry-bench

## Abstract

Evaluating aligned large language models’ (LLMs) ability to recognize and reject unsafe user requests is crucial for safe, policy-compliant deployments. Existing evaluation efforts, however, face three limitations that we address with SORRYBench, our proposed benchmark. First, existing methods often use coarse-grained taxonomies of unsafe topics, and are over-representing some fine-grained topics. For example, among the ten existing datasets that we evaluated, tests for refusals of self-harm instructions are over 3x less represented than tests for fraudulent activities. SORRY-Bench improves on this by using a fine-grained taxonomy of 44 potentially unsafe topics, and 440 class-balanced unsafe instructions, compiled through humanin-the-loop methods. Second, linguistic characteristics and formatting of prompts are often overlooked, like different languages, dialects, and more – which are only implicitly considered in many evaluations. We supplement SORRY-Bench with 20 diverse linguistic augmentations to systematically examine these effects. Third, existing evaluations rely on large LLMs (e.g., GPT-4) for evaluation, which can be computationally expensive. We investigate design choices for creating a fast, accurate automated safety evaluator. By collecting 7K+ human annotations and conducting a meta-evaluation of diverse LLM-as-a-judge designs, we show that fine-tuned 7B LLMs can achieve accuracy comparable to GPT-4 scale LLMs, with lower computational cost. Putting these together, we evaluate over 50 proprietary and open-weight LLMs on SORRY-Bench, analyzing their distinctive safety refusal behaviors. We hope our effort provides a building block for systematic evaluations of LLMs’ safety refusal capabilities, in a balanced, granular, and efficient manner.

## Dataset Information

440 class-balanced unsafe instructions (base set)

## Data Description

SORRY-Bench: A class-balanced LLM safety refusal evaluation dataset of 440 unsafe instructions across 44 fine-grained risk categories, augmented with 8,800 additional linguistically mutated variants (20 mutations × 440 base instructions), plus 7,040 human safety judgment annotations for evaluator training and meta-evaluation.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 4, Agent 16
**Implementation Readiness:** HIGH

## Tags

