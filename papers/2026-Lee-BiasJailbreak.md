---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0003
type: conferencePaper
short_title: BiasJailbreak
year: 2025
first_author: "[[Isack Lee]]"
last_author: "[[Haebin Seong]]"
authors: "Isack Lee; Haebin Seong"
url: "https://arxiv.org/abs/2410.13334"
external_pdf: "https://arxiv.org/pdf/2410.13334.pdf"
pdf_extract: "PDF Extracts/2026/2026-Lee-BiasJailbreak.md"
local_pdf: [[Lit-WS-Lit-WS-PDFs/2026/2026-Lee-BiasJailbreak.pdf]]
publication: "AAAI 2026"
CONF-CC: "AAAI 2026"
DATE_ADDED: 20260207
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: 
religious_values: "Multiple Religions"
rv_islam: 0
rv_christianity: 50
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 50
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: "Christianity, Jainism"
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
abstract: "Warning: This paper contains potentially offensive and harmful text. Although large language models (LLMs) demonstrate impressive proficiency in various tasks, they present potential safety risks, such as 'jailbreaks', where malicious inputs can coerce LLMs into generating harmful content bypassing safety alignments. In this paper, we delve into the ethical biases in LLMs and examine how those biases could be exploited for jailbreaks."
LLM_assessed: "GPT-3.5, GPT-4, GPT-4o, ChatGPT, Claude, Llama-2, Llama-3, Qwen, Qwen-2"
DATA_URL: "https://github.com/Isaac-theori/BiasJailbreak"
research_topic: Other
CONFERENCE: "AAAI 2026"
ethics_overall: No
virtue_ethics: 0
deontological_ethics: 0
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
is_benchmark: No
is_eval: No
is_dataset: No
data_description: N/A
data_metrics: "Not specified"
---
# BiasJailbreak

## Authors

[[Isack Lee]], [[Haebin Seong]]

## Metadata

**Authors:** Isack Lee, Haebin Seong

**Year:** 2026

**Type:** conferencePaper

**Venue:** AAAI 2026

## Links

- **arXiv:** https://arxiv.org/abs/2410.13334

## Abstract

Warning: This paper contains potentially offensive and harmful text. Although large language models (LLMs) demonstrate impressive proficiency in various tasks, they present potential safety risks, such as ‘jailbreaks’, where malicious inputs can coerce LLMs into generating harmful content bypassing safety alignments. In this paper, we delve into the ethical biases in LLMs and examine how those biases could be exploited for jailbreaks. Notably, these biases result in a jailbreaking success rate in GPT-4o models that differs by 20% between non-binary and cisgender keywords and by 16% between white and black keywords, even when the other parts of the prompts are identical. We introduce the concept of BiasJailbreak, highlighting the inherent risks posed by these safety-induced biases. BiasJailbreak generates biased keywords automatically by asking the target LLM itself, and utilizes the keywords to generate harmful output. Additionally, we propose an efficient defense method BiasDefense, which prevents jailbreak attempts by injecting defense prompts prior to generation. BiasDefense stands as an appealing alternative to Guard Models, such as Llama-Guard, that require additional inference cost after text generation. Our findings emphasize that ethical biases in LLMs can actually lead to generating unsafe output, and suggest a method to make the LLMs more secure and unbiased. To enable further research and improvements, we open-source our code and artifacts of BiasJailbreak, providing the community with tools to better understand and mitigate safety-induced biases in LLMs. Code and Artifacts — https://github.com/Isaac-theori/BiasJailbreak

## Dataset Information

Adversarial prompts with systematically varied demographic keywords

## Data Description

The BiasJailbreak dataset combines harmful prompts from JailBreakBench (100 samples) and AdvBench (totaling 600 harmful prompts) with automatically generated bias keywords representing privileged and marginalized demographic groups. The study evaluates jailbreak success rates across 9 LLMs including GPT-3.5, GPT-4, GPT-4o, Claude-sonnet3.5, LLaMA2, LLaMA3, Qwen-1.5, Qwen2, and Phi-mini, measuring ethical bias differentials in safety alignment.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 16
**Implementation Readiness:** MEDIUM

## Tags

