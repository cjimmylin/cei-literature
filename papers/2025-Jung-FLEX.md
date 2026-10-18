---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: TW3M3CQN
type: document
short_title: FLEX
year: 2025
first_author: "[[Dahyun Jung]]"
last_author: "[[Lim, Heuiseok]]"
authors: "Jung, Dahyun; Lee, Seungyoon; Moon, Hyeonseok; Park, Chanjun; Lim, Heuiseok"
url: "https://aclanthology.org/2025.findings-naacl.199/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/M5J3WHBS/2025 - FLEX A Benchmark for Evaluating Robustness of Fairness in Large Language Models.pdf"
national_ethnic_cultural: Korean
cultures_nationalities_list: Korean
languages_list: Korean
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
newtags: "Bias & Fairness"
key_contribution: "Introduced FLEX, a fairness benchmark designed to test LLM robustness under 'extreme scenarios' (adversarial prompts that attempt to induce bias)."
significance: "Demonstrates that existing benchmarks underestimate fairness risks because they don't account for adversarial conditions where prompts actively try to trigger discriminatory outputs."
tags: 
abstract: "Recent advancements in Large Language Models (LLMs) have significantly enhanced interactions between users and models. These advancements concurrently underscore the need for rigorous safety evaluations due to the manifestation of social biases, which can lead to harmful societal impacts. Despite these concerns, existing benchmarks may overlook the intrinsic weaknesses of LLMs, which can generate biased responses even with simple adversarial instructions."
CONF-CC: N/A
DATE_ADDED: 20260208
LLM_assessed: "GPT-3.5, GPT-4o, Gemma, Llama-2, Llama-3, Mistral"
DATA_URL: "https://github.com/ekgus9/FLEX"
pdf_extract: "PDF Extracts/2025/2025-Jung-FLEX.md"
local_pdf: "[[Lit-WS-PDFs/2025/2025-Jung-FLEX.pdf]]"
CONFERENCE: "NAACL 2025"
ethics_overall: 15
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Bias & Fairness"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: KR
author_region: "East Asia"
author_global_north_south: "Global North"
weird_score: 63
is_benchmark: Yes
is_eval: Yes
is_dataset: No
data_description: "Benchmark for ai safety"
data_metrics: "Not specified"
---
# FLEX: A Benchmark for Evaluating Robustness of Fairness in Large Language Models

## Authors

[[Dahyun Jung|Jung, Dahyun]], [[Seungyoon Lee|Lee, Seungyoon]], [[Hyeonseok Moon|Moon, Hyeonseok]], [[Chanjun Park|Park, Chanjun]], [[Heuiseok Lim|Lim, Heuiseok]]

## Links

- **ACL Anthology:** https://aclanthology.org/2025.findings-naacl.199/

## Abstract

Recent advancements in Large Language Models (LLMs) have significantly enhanced interactions between users and models. These advancements concurrently underscore the need for rigorous safety evaluations due to the manifestation of social biases, which can lead to harmful societal impacts. Despite these concerns, existing benchmarks may overlook the intrinsic weaknesses of LLMs, which can generate biased responses even with simple adversarial instructions. To address this critical gap, we introduce a new benchmark, Fairness Benchmark in LLM under Extreme Scenarios (FLEX), designed to test whether LLMs can sustain fairness even when exposed to prompts constructed to induce bias. To thoroughly evaluate the robustness of LLMs, we integrate prompts that amplify potential biases into the fairness assessment. Comparative experiments between FLEX and existing benchmarks demonstrate that traditional evaluations may underestimate the inherent risks in models. This highlights the need for more stringent LLM evaluation benchmarks to guarantee safety and fairness.

## Data Description

FLEX (Fairness Benchmark in LLM under Extreme Scenarios): adversarial fairness benchmark constructed from BBQ, CrowS-Pairs, and StereoSet by injecting persona injection, competing objectives, and text attack prompts to induce bias in LLMs.


## Notes

