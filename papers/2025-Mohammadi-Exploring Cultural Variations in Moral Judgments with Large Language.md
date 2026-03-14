---





































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0051
type: preprint
short_title: "Exploring Cultural Variations in Moral Judgments with Large Language Models"
year: 2025
first_author: "[[Hadi Mohammadi]]"
last_author: "[[A & Bagheri]]"
authors: "Hadi Mohammadi; A & Bagheri"
url: "https://arxiv.org/abs/2506.12433"
external_pdf: "https://arxiv.org/pdf/2506.12433.pdf"
pdf_extract: "PDF Extracts/2025/2025-Mohammadi-Exploring Cultural Variations in Moral Judgments with Large Language.md"
local_pdf: "[[PDFs/2025/2025-Mohammadi-Exploring Cultural Variations in Moral Judgments with Large Language.pdf]]"
publication: arXiv
CONF-CC: "Preprint"
DATE_ADDED: 20260207
national_ethnic_cultural: "Multicultural/Cross-cultural"
cultures_nationalities_list: "Multicultural/Cross-cultural"
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
mp_schwartz: 50
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "Value Pluralism / Schwartz"
newtags: 
tags: 
abstract: "Large Language Models (LLMs) have shown strong performance across many tasks, but their ability to capture culturally diverse moral values remains unclear. In this paper, we examine whether LLMs mirror variations in moral attitudes reported by the World Values Survey (WVS) and the Pew Research Center’s Global Attitudes Survey (PEW). We compare smaller monolingual and multilingual models (GPT-2, OPT, BLOOMZ, and Qwen) with recent instruction-tuned models (GPT-4o, GPT-4o-mini, Gemma-2-9b-it, and..."
LLM_assessed: "BLOOM, Falcon, GPT-2, GPT-3.5, GPT-4o, GPT-4o mini, Gemma-2, Llama-2, Llama-3, Qwen"
DATA_URL: "https://github.com/mohammadi-hadi/cultural-moral-judgments-llms"
CONFERENCE: "Preprint"
ethics_overall: 50
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 5
is_benchmark: "No"
is_eval: Yes
is_dataset: No
data_description: "Dataset"
data_metrics: "Not specified"
ethics_perspective: "Social & Cultural Values"
---
# Exploring Cultural Variations in Moral Judgments with Large Language Models

## Authors

[[Hadi Mohammadi]], [[A & Bagheri]]

## Metadata

**Authors:** Mohammadi, H., & Bagheri, A

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2506.12433
- **Code/Data:** https://github.com/mohammadi-hadi/cultural-moral-judgments-llms

## Abstract

Large Language Models (LLMs) have shown strong performance across many tasks, but their ability to capture culturally diverse moral values remains unclear. In this paper, we examine whether LLMs mirror variations in moral attitudes reported by the World Values Survey (WVS) and the Pew Research Center’s Global Attitudes Survey (PEW). We compare smaller monolingual and multilingual models (GPT-2, OPT, BLOOMZ, and Qwen) with recent instruction-tuned models (GPT-4o, GPT-4o-mini, Gemma-2-9b-it, and Llama-3.3-70B-Instruct). Using log-probabilitybased moral justifiability scores, we correlate each model’s outputs with survey data covering a broad set of ethical topics. Our results show that many earlier or smaller models often produce near-zero or negative correlations with human judgments. In contrast, advanced instruction-tuned models achieve substantially higher positive correlations, suggesting they better reflect real-world moral attitudes. We provide a detailed regional analysis revealing that models align better with Western, Educated, Industrialized, Rich, and Democratic (W.E.I.R.D.) nations than with other regions. While scaling model size and using instruction tuning improves alignment with crosscultural moral norms, challenges remain for certain topics and regions. We discuss these findings in relation to bias analysis, training data diversity, information retrieval implications, and strategies for improving the cultural sensitivity of LLMs.

## Dataset Information

Format: Structured probing prompts with contrasting moral statements; log-probability scoring

## Data Description

This study evaluates 20 models across 9 families on their ability to capture culturally diverse moral values using the World Values Survey (55 countries, 19 topics) and PEW Global Attitudes Survey (39 countries, 8 topics). Models range from smaller monolingual (GPT-2, OPT) and multilingual (BLOOMZ, Qwen) to instruction-tuned systems (GPT-4o, Gemma-2-9B-IT, Llama-3.3-70B, Falcon-40B-Instruct), using log-probability-based moral justifiability scores correlated with survey data.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 12-13
**Implementation Readiness:** HIGH

## Tags

