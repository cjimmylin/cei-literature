---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: TFWHHICP
type: conferencePaper
short_title: TruthfulQA
year: 2022
first_author: "[[Stephanie Lin]]"
last_author: "[[Owain Evans]]"
authors: "Stephanie Lin; Jacob Hilton; Owain Evans"
doi: 10.18653/v1/2022.acl-long.229
url: "https://aclanthology.org/2022.acl-long.229/"
external_pdf: "https://aclanthology.org/2022.acl-long.229.pdf"
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: English
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
pdf_extract: "PDF Extracts/2022/2022-Lin-TruthfulQA.md"
local_pdf: "[[Lit-WS-PDFs/2022/2022-Lin-TruthfulQA.pdf]]"
abstract: "We propose a benchmark to measure whether a language model is truthful in generating answers to questions. The benchmark comprises 817 questions that span 38 categories, including health, law, finance and politics. We crafted questions that some humans would answer falsely due to a false belief or misconception. To perform well, models must avoid generating false answers learned from imitating human texts. We tested GPT-3, GPT-Neo/J, GPT-2 and a T5-based model."
CONF-CC: "ACL 2022"
DATE_ADDED: 20260208
LLM_assessed: "GPT-2, GPT-3, GPT-J, GPT-Neo, UnifiedQA"
DATA_URL: "https://github.com/sylinrl/TruthfulQA"
CONFERENCE: "ACL 2022"
eleutherai: incorporated
helm: incorporated
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "Truthfulness & Factuality"
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
is_dataset: No
data_description: Benchmark
data_metrics: "817 questions; 38 categories"
---
# TruthfulQA: Measuring How Models Mimic Human Falsehoods

## Metadata

**Authors:** Lin, Stephanie; Hilton, Jacob; Evans, Owain

**Year:** 2022

**Publication:** Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)

**Type:** conferencePaper

**DOI:** [10.18653/v1/2022.acl-long.229](https://doi.org/10.18653/v1/2022.acl-long.229)

**Pages:** 3214-3252

**Publisher:** Association for Computational Linguistics

## Links

- **Local PDF:** [[Lit-WS-PDFs/2022/2022-Lin-TruthfulQA.pdf|Open PDF]]

- **ACL Anthology:** https://aclanthology.org/2022.acl-long.229
- **DOI:** https://doi.org/10.18653/v1/2022.acl-long.229

## Abstract

We propose a benchmark to measure whether a language model is truthful in generating answers to questions. The benchmark comprises 817 questions that span 38 categories, including health, law, finance and politics. We crafted questions that some humans would answer falsely due to a false belief or misconception. To perform well, models must avoid generating false answers learned from imitating human texts. We tested GPT-3, GPT-Neo/J, GPT-2 and a T5-based model. The best model was truthful on 58% of questions, while human performance was 94%. Models generated many false answers that mimic popular misconceptions and have the potential to deceive humans. The largest models were generally the least truthful. This contrasts with other NLP tasks, where performance improves with model size. However, this result is expected if false answers are learned from the training distribution. We suggest that scaling up models alone is less promising for improving truthfulness than fine-tuning using training objectives other than imitation of text from the web.

## Authors

[[Stephanie Lin]], [[Jacob Hilton]], [[Owain Evans]]

## Data Description

Benchmark of 817 questions across 38 categories measuring LM truthfulness


## Notes


## Citation Info

2114 citations (Semantic Scholar/DOI) [2025-08-27] 2092 citations (Semantic Scholar/DOI) [2025-08-23] 219 citations (Crossref/DOI) [2025-08-23]
