---




Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: TFWHHICP
type: conferencePaper
short_title: TruthfulQA
year: 2025
first_author: "[[Stephanie Lin]]"
last_author: "[[Owain Evans]]"
authors: "Stephanie Lin; Jacob Hilton; Owain Evans"
doi: 10.18653/v1/2022.acl-long.229
url: "https://aclanthology.org/2022.acl-long.229/"
external_pdf: "https://aclanthology.org/2022.acl-long.229.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
pdf_extract: "PDF Extracts/2022/2022-Lin-TruthfulQA.md"
local_pdf: [[PDFs/2022/2022-Lin-TruthfulQA.pdf]]
abstract: "We propose a benchmark to measure whether a language model is truthful in generating answers to questions. The benchmark comprises 817 questions that span 38 categories, including health, law, finance and politics. We crafted questions that some humans would answer falsely due to a false belief or misconception. To perform well, models must avoid generating false answers learned from imitating human texts. We tested GPT-3, GPT-Neo/J, GPT-2 and a T5-based model."
DATE_ADDED: 20260208
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Truthfulness & Factuality"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark"
data_metrics: "817 questions; 38 categories"
LLM_assessed: "GPT-3, GPT-2, T5, InstructGPT"
DATA_URL: "https://github.com/sylinrl/TruthfulQA"
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

- **Local PDF:** [[PDFs/2022/2022-Lin-TruthfulQA.pdf|Open PDF]]

- **ACL Anthology:** https://aclanthology.org/2022.acl-long.229
- **DOI:** https://doi.org/10.18653/v1/2022.acl-long.229

## Abstract

We propose a benchmark to measure whether a language model is truthful in generating answers to questions. The benchmark comprises 817 questions that span 38 categories, including health, law, finance and politics. We crafted questions that some humans would answer falsely due to a false belief or misconception. To perform well, models must avoid generating false answers learned from imitating human texts. We tested GPT-3, GPT-Neo/J, GPT-2 and a T5-based model. The best model was truthful on 58% of questions, while human performance was 94%. Models generated many false answers that mimic popular misconceptions and have the potential to deceive humans. The largest models were generally the least truthful. This contrasts with other NLP tasks, where performance improves with model size. However, this result is expected if false answers are learned from the training distribution. We suggest that scaling up models alone is less promising for improving truthfulness than fine-tuning using training objectives other than imitation of text from the web.

## Authors

[[Stephanie Lin]], [[Jacob Hilton]], [[Owain Evans]]

## Data Description

TruthfulQA is a benchmark comprising 817 questions spanning 38 categories (health, law, finance, politics, etc.) designed to elicit imitative falsehoods from language models. The questions are adversarially constructed so that some humans would answer them falsely due to misconceptions. The benchmark includes both a generation task and a multiple-choice task, with reference true and false answers for each question, and was tested on GPT-3, GPT-2, GPT-Neo/J, and UnifiedQA (T5-based) models across multiple sizes.


## Notes


## Citation Info

2114 citations (Semantic Scholar/DOI) [2025-08-27] 2092 citations (Semantic Scholar/DOI) [2025-08-23] 219 citations (Crossref/DOI) [2025-08-23]
