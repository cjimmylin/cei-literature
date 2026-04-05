---







































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: CCQX696K
type: conferencePaper
short_title: "MedAI at SemEval-2021 Task 5"
year: 2021
first_author: "[[Zhen Wang]]"
last_author: "[[Junfei Liu]]"
authors: "Zhen Wang; Hongjie Fan; Junfei Liu"
doi: 10.18653/v1/2021.semeval-1.30
url: "https://aclanthology.org/2021.semeval-1.30/"
external_pdf: "https://aclanthology.org/2021.semeval-1.30.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
rv_islam: 0
rv_christianity: 5
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
newtags: "Toxicity & Hate Speech"
key_contribution: "A system submission for detecting 'Toxic Spans' (specific words making a text toxic) using a start-to-end tagging framework."
significance: "Moves beyond binary classification (Toxic/Not Toxic) to 'explainable toxicity' by highlighting *why* a text is toxic, which is crucial for moderation feedback."
tags: 
abstract: "This paper describes the system submitted to SemEval 2021 Task 5: Toxic Spans Detection. The task concerns evaluating systems that detect the spans that make a text toxic when detecting such spans are possible. To address the possibly multi-span detection problem, we develop a start-to-end tagging framework on the top of RoBERTa based language model. Besides, we design a custom loss function which take distance into account. In comparison to other participating teams, our system has achieved 69."
pdf_extract: "PDF Extracts/2021/2021-Wang-MedAI at SemEval-2021 Task 5.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2021/2021-Wang-MedAI at SemEval-2021 Task 5.pdf]]"
CONF-CC: "SemEval 2021"
DATE_ADDED: 20260208
LLM_assessed: "BERT, RoBERTa"
DATA_URL: "NA"
CONFERENCE: "Other Conference"
ethics_overall: 90
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Toxicity & Hate Speech"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: "TH"
author_region: "Southeast Asia"
author_global_north_south: "Global South"
weird_score: 36
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation framework"
data_metrics: "Not specified"
---
# MedAI at SemEval-2021 Task 5: Start-to-end Tagging Framework for Toxic Spans Detection

## Metadata

**Authors:** Wang, Zhen; Fan, Hongjie; Liu, Junfei

**Year:** 2021

**Publication:** Proceedings of the 15th International Workshop on Semantic Evaluation (SemEval-2021)

**Type:** conferencePaper

**DOI:** [10.18653/v1/2021.semeval-1.30](https://doi.org/10.18653/v1/2021.semeval-1.30)

**Pages:** 258-262

**Publisher:** Association for Computational Linguistics

## Links

- **ACL Anthology:** https://aclanthology.org/2021.semeval-1.30
- **DOI:** https://doi.org/10.18653/v1/2021.semeval-1.30

## Abstract

This paper describes the system submitted to SemEval 2021 Task 5: Toxic Spans Detection. The task concerns evaluating systems that detect the spans that make a text toxic when detecting such spans are possible. To address the possibly multi-span detection problem, we develop a start-to-end tagging framework on top of RoBERTa based language model. Besides, we design a custom loss function that takes distance into account. In comparison to other participating teams, our system has achieved 69.03% F1 score, which is slightly lower (-1.8 and -1.73) than the top 1(70.83%) and top 2 (70.77%), respectively.

## Authors

[[Zhen Wang]], [[Hongjie Fan]], [[Junfei Liu]]

## Data Description

The paper uses the SemEval-2021 Task 5 Toxic Spans Detection dataset, which contains 7,939 training examples and 2,000 test examples of text posts annotated with character-level spans indicating toxic content. The system employs a start-to-end tagging framework built on top of RoBERTa-based pretrained language models (DistilRoBERTa-base, RoBERTa-base-squad2, twitter-RoBERTa-base-sentiment) with a custom distance loss function, achieving 69.03% F1 score.


## Notes


## Citation Info

61 citations (Semantic Scholar/DOI) [2025-08-27] 2 citations (Semantic Scholar/DOI) [2025-08-23] 2 citations (Crossref/DOI) [2025-08-23]
