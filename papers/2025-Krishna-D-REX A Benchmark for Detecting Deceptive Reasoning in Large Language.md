---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0037
type: conferencePaper
short_title: "D-REX: A Benchmark for Detecting Deceptive Reasoning in Large Language Models"
year: 2025
first_author: "[[Satyapriya Krishna]]"
last_author: "[[Spyros Matsoukas]]"
authors: "Satyapriya Krishna; Andy Zou; Rahul Gupta; Eliot Krzysztof Jones; Nick Winter; Dan Hendrycks; J. Zico Kolter; Matt Fredrikson; Spyros Matsoukas"
url: "https://arxiv.org/abs/2509.17938"
external_pdf: "https://arxiv.org/pdf/2509.17938.pdf"
pdf_extract: "PDF Extracts/2025/2025-Krishna-D-REX A Benchmark for Detecting Deceptive Reasoning in Large Language.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Krishna-D-REX A Benchmark for Detecting Deceptive Reasoning in Large Language.pdf]]"
publication: "ACL 2025"
CONF-CC: "ACL 2025"
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
abstract: "The safety and alignment of Large Language Models (LLMs) are critical for their responsible deployment. Current evaluation methods predominantly focus on identifying and preventing overtly harmful outputs. However, they often fail to address a more insidious failure mode: models that produce benign-appearing outputs while operating on malicious or deceptive internal reasoning. This vulnerability, often triggered by sophisticated system prompt injections, allows models to bypass conventional..."
LLM_assessed: "Claude, DeepSeek, Gemini, Grok, Qwen"
DATA_URL: NA
CONFERENCE: "ACL 2025"
ethics_overall: No
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 5
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
# D-REX: A Benchmark for Detecting Deceptive Reasoning in Large Language Models

## Authors

[[Satyapriya Krishna]], [[Andy Zou]], [[Rahul Gupta]], [[Eliot Krzysztof Jones]], [[Nick Winter]], [[Dan Hendrycks]], [[J. Zico Kolter]], [[Matt Fredrikson]], [[Spyros Matsoukas]]

## Metadata

**Authors:** Satyapriya Krishna; Andy Zou; Rahul Gupta; Eliot Krzysztof Jones; Nick Winter; Dan Hendrycks; J. Zico Kolter; Matt Fredrikson; Spyros Matsoukas

**Year:** 2025

**Type:** conferencePaper

**Venue:** ACL 2025

## Links

- **arXiv:** https://arxiv.org/abs/2509.17938

## Abstract

The safety and alignment of Large Language Models (LLMs) are critical for their responsible deployment. Current evaluation methods predominantly focus on identifying and preventing overtly harmful outputs. However, they often fail to address a more insidious failure mode: models that produce benign-appearing outputs while operating on malicious or deceptive internal reasoning. This vulnerability, often triggered by sophisticated system prompt injections, allows models to bypass conventional safety filters, posing a significant, underexplored risk. To address this gap, we introduce the Deceptive Reasoning Exposure Suite (D-REX), a novel dataset designed to evaluate the discrepancy between a model’s internal reasoning process and its final output. D-REX was constructed through a competitive red-teaming exercise where participants crafted adversarial system prompts to induce such deceptive behaviors. Each sample in D-REX contains the adversarial system prompt, an end-user’s test query, the model’s seemingly innocuous response, and, crucially, the model’s internal chain-of-thought, which reveals the underlying malicious intent. Our benchmark facilitates a new, essential evaluation task: the detection of deceptive alignment. We demonstrate that D-REX presents a significant challenge for existing models and safety mechanisms, highlighting the urgent need for new techniques that scrutinize the internal processes of LLMs, not just their final outputs.

## Dataset Information

Red-teaming exercise-generated dataset; each sample contains: adversarial system prompt, user query, seemingly innocuous response, and internal chain-of-thought revealing malicious intent

## Data Description

D-REX (Deceptive Reasoning Exposure Suite) is a private benchmark of 8,162 adversarial examples collected via competitive red-teaming, each containing an adversarial system prompt, benign user query, internal chain-of-thought revealing malicious intent, and a seemingly innocuous final response. The benchmark is maintained as a private test set with a controlled submission portal to prevent contamination.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 18
**Implementation Readiness:** MEDIUM

## Tags

