---



























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0031
type: conferencePaper
short_title: "CARE -- Multilingual Human Preference Learning for Cultural Awareness"
year: 2025
first_author: "[[Guo, Geyang]]"
last_author: "[[Xu, Wei]]"
authors: "Guo, Geyang; Naous, Tarek; Wakaki, Hiromi; Nishimura, Yukiko; Mitsufuji, Yuki; Ritter, Alan; Xu, Wei"
authors_incomplete: false
url: "https://arxiv.org/abs/2504.05154"
external_pdf: "https://arxiv.org/pdf/2504.05154.pdf"
pdf_extract: "PDF Extracts/2025/2025-Guo-CARE - Multilingual Human Preference Learning for Cultural Awareness.md"
local_pdf: "[[PDFs/2025/2025-Guo-CARE - Multilingual Human Preference Learning for Cultural Awareness.pdf]]"
publication: "EMNLP 2025"
CONF-CC: "EMNLP 2025"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "Multilingual"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "Language Models (LMs) are typically tuned with human preferences to produce helpful responses, but the impact of preference tuning on the ability to handle culturally diverse queries remains understudied. In this paper, we systematically analyze how native human cultural preferences can be incorporated into the preference learning process to train more culturally aware LMs. We introduce CARE, a multilingual resource containing 3,490 culturally specific questions and 31."
LLM_assessed: "GPT-4, Llama-3, Qwen, Gemma, Mistral"
DATA_URL: "https://github.com/Guochry/CARE"
CONFERENCE: "EMNLP 2025"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Social & Cultural Values"
is_benchmark: "No"
is_eval: "No"
is_dataset: "No"
data_description: "N/A"
data_metrics: "Not specified"
---
# CARE -- Multilingual Human Preference Learning for Cultural Awareness

## Authors

[[Guo, Geyang]], [[Naous, Tarek]], [[Wakaki, Hiromi]], [[Nishimura, Yukiko]], [[Mitsufuji, Yuki]], [[Ritter, Alan]], [[Wei Xu|Xu, Wei]]

## Metadata

**Authors:** Guo, Geyang; Naous, Tarek; Wakaki, Hiromi; Nishimura, Yukiko; Mitsufuji, Yuki; Ritter, Alan; Xu, Wei

**Year:** 2025

**Type:** conferencePaper

**Venue:** EMNLP 2025

## Links

- **arXiv:** https://arxiv.org/abs/2504.05154

## Abstract

Language Models (LMs) are typically tuned with human preferences to produce helpful responses, but the impact of preference tuning on the ability to handle culturally diverse queries remains understudied. In this paper, we systematically analyze how native human cultural preferences can be incorporated into the preference learning process to train more culturally aware LMs. We introduce CARE, a multilingual resource containing 3,490 culturally specific questions and 31.7k responses with human judgments. We demonstrate how a modest amount of high-quality native preferences improves cultural awareness across various LMs, outperforming larger generic preference data. Our analyses reveal that models with stronger initial cultural performance benefit more from alignment, leading to gaps among models developed in different regions with varying access to culturally relevant data. CARE is publicly available at https://github.com/Guochry/ CARE.

## Dataset Information

Size: 3,490 culturally specific questions + 31,700 LLM/human-written responses with human preference judgments

## Data Description

CARE is a multilingual human preference dataset containing 3,490 culturally specific questions and 31,700 responses with human judgments across Chinese, Arabic, and Japanese cultures. Nine LLMs were tested including Llama-3.3-70B, Llama-3.1-8B, Qwen-2.5-72B, Qwen-2.5-7B, Gemma-2-27B, Gemma-2-9B, Mistral-Large, Mistral-7B, and GPT-4o, evaluated on five cultural dimensions (entities, opinion, social norms, commonsense, literacy) using preference optimization methods like DPO, KTO, and SimPO.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 12-13
**Implementation Readiness:** HIGH

## Tags

