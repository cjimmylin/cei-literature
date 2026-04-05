---








































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0257
type: conferencePaper
short_title: "MORABLES: A Benchmark for Assessing Abstract Moral Reasoning in LLMs with Fables"
year: 2025
first_author: "[[Marcuzzo, Matteo]]"
last_author: "[[Pilehvar, Mohammad Taher]]"
authors: "Marcuzzo, Matteo; Zangari, Alessandro; Albarelli, Andrea; Camacho-Collados, Jose; Pilehvar, Mohammad Taher"
authors_incomplete: false
url: "https://arxiv.org/abs/2509.12371"
external_pdf: "https://arxiv.org/pdf/2509.12371.pdf"
pdf_extract: "PDF Extracts/2025/2025-Marcuzzo-MORABLES A Benchmark for Assessing Abstract Moral Reasoning in LLMs.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Marcuzzo-MORABLES A Benchmark for Assessing Abstract Moral Reasoning in LLMs.pdf]]"
publication: EMNLP
CONF-CC: "EMNLP 2025"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
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
abstract: "As LLMs excel on standard reading comprehension benchmarks, attention is shifting toward evaluating their capacity for complex abstract reasoning and inference. Literaturebased benchmarks, with their rich narrative and moral depth, provide a compelling framework for evaluating such deeper comprehension skills. Here, we present MORABLES, a humanverified benchmark built from fables and short stories drawn from historical literature."
LLM_assessed: "Claude, DeepSeek, GPT-4o, Gemini, Llama-3, Mistral, Mixtral, Qwen, o3"
DATA_URL: "https://huggingface.co/datasets/cardiffnlp/Morables"
CONFERENCE: "EMNLP 2025"
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 15
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Moral Reasoning & Psychology"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: "US"
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark for moral/ethical reasoning"
data_metrics: "Not specified"
---
# MORABLES: A Benchmark for Assessing Abstract Moral Reasoning in LLMs with Fables

## Authors

[[Marcuzzo, Matteo]], [[Zangari, Alessandro]], [[Albarelli, Andrea]], [[Camacho-Collados, Jose]], [[Pilehvar, Mohammad Taher]]

## Metadata

**Authors:** Marcuzzo, Matteo; Zangari, Alessandro; Albarelli, Andrea; Camacho-Collados, Jose; Pilehvar, Mohammad Taher

**Year:** 2025

**Type:** conferencePaper

**Venue:** EMNLP

## Links

- **arXiv:** https://arxiv.org/abs/2509.12371

## Abstract

As LLMs excel on standard reading comprehension benchmarks, attention is shifting toward evaluating their capacity for complex abstract reasoning and inference. Literaturebased benchmarks, with their rich narrative and moral depth, provide a compelling framework for evaluating such deeper comprehension skills. Here, we present MORABLES, a humanverified benchmark built from fables and short stories drawn from historical literature. The main task is structured as multiple-choice questions targeting moral inference, with carefully crafted distractors that challenge models to go beyond shallow, extractive question answering. To further stress-test model robustness, we introduce adversarial variants designed to surface LLM vulnerabilities and shortcuts due to issues such as data contamination. Our findings show that, while larger models outperform smaller ones, they remain susceptible to adversarial manipulation and often rely on superficial patterns rather than true moral reasoning. This brittleness results in significant self-contradiction, with the best models refuting their own answers in roughly 20% of cases depending on the framing of the moral choice. Interestingly, reasoning-enhanced models fail to bridge this gap, suggesting that scale – not reasoning ability – is the primary driver of performance.

## Dataset Information

Literature-based benchmark using fables for abstract moral reasoning, includes adversarial variants

## Data Description

MORABLES is a human-verified benchmark of 709 fables and short stories drawn from Western historical literature (Aesop, La Fontaine), structured as 5-choice MCQA moral inference tasks with adversarial variants (character swaps, trait injection, tautology injection). Publicly released on HuggingFace.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** HIGH

## Tags

