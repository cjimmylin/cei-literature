---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: VHXG9AIH
type: conferencePaper
short_title: HeQ
year: 2025
first_author: "[[Amir Cohen]]"
last_author: "[[Reut Tsarfaty]]"
authors: "Amir Cohen; Hilla Merhav-Fine; Yoav Goldberg; Reut Tsarfaty"
doi: 10.18653/v1/2023.findings-emnlp.915
url: "https://aclanthology.org/2023.findings-emnlp.915/"
external_pdf: "https://aclanthology.org/2023.findings-emnlp.915.pdf"
national_ethnic_cultural: "Hebrew/Israeli"
cultures_nationalities_list: "Israeli"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: Hebrew/Israeli
tags: 
pdf_extract: "PDF Extracts/2023/2023-Cohen-HeQ.md"
local_pdf: [[PDFs/2023/2023-Cohen-HeQ.pdf]]
abstract: "Current benchmarks for Hebrew Natural Language Processing (NLP) focus mainly on morpho-syntactic tasks, neglecting the semantic dimension of language understanding. To bridge this gap, we set out to deliver a Hebrew Machine Reading Comprehension (MRC) dataset, where MRC is to be realized as extractive Question Answering. The morphologically-rich nature of Hebrew poses a challenge to this endeavor: the indeterminacy and non-transparency of span boundaries in morphologically complex forms lead to..."
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Question Answering"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark dataset for question answering"
data_metrics: "Not specified"
LLM_assessed: BERT
DATA_URL: "https://github.com/NNLP-IL/Hebrew-Question-Answering-Dataset"
publication: ACL Anthology (EMNLP 2023 Findings)
DATE_ADDED: 20260213
---
# HeQ: a Large and Diverse Hebrew Reading Comprehension Benchmark

## Metadata

**Authors:** Cohen, Amir; Merhav-Fine, Hilla; Goldberg, Yoav; Tsarfaty, Reut

**Year:** 2023

**Publication:** Findings of the Association for Computational Linguistics: EMNLP 2023

**Type:** conferencePaper

**DOI:** [10.18653/v1/2023.findings-emnlp.915](https://doi.org/10.18653/v1/2023.findings-emnlp.915)

**Pages:** 13693-13705

**Publisher:** Association for Computational Linguistics

## Links

- **Local PDF:** [[PDFs/2023/2023-Cohen-HeQ.pdf|Open PDF]]

- **ACL Anthology:** https://aclanthology.org/2023.findings-emnlp.915
- **DOI:** https://doi.org/10.18653/v1/2023.findings-emnlp.915

## Abstract

Current benchmarks for Hebrew Natural Language Processing (NLP) focus mainly on morpho-syntactic tasks, neglecting the semantic dimension of language understanding. To bridge this gap, we set out to deliver a Hebrew Machine Reading Comprehension (MRC) dataset, where MRC is to be realized as extractive Question Answering. The morphologically-rich nature of Hebrew poses a challenge to this endeavor: the indeterminacy and non-transparency of span boundaries in morphologically complex forms lead to annotation inconsistencies, disagreements, and flaws of standard evaluation metrics. To remedy this, we devise a novel set of guidelines, a controlled crowdsourcing protocol, and revised evaluation metrics, that are suitable for the morphologically rich nature of the language. Our resulting benchmark, HeQ (Hebrew QA), features 30,147 diverse question-answer pairs derived from both Hebrew Wikipedia articles and Israeli tech news. Our empirical investigation reveals that standard evaluation metrics such as F1 Scores and Exact Match (EM) are not appropriate for Hebrew (and other MRLs), and we propose a relevant enhancement. In addition, our experiments show low correlation between models’ performance on morpho-syntactic tasks and on MRC, which suggests that models that are designed for the former might underperform on semantic-heavy tasks. The development and exploration of HeQ illustrate some of the challenges MRLs pose in natural language understanding (NLU), fostering progression towards more and better NLU models for Hebrew and other MRLs.

## Authors

[[Amir Cohen]], [[Hilla Merhav-Fine]], [[Yoav Goldberg]], [[Reut Tsarfaty]]

## Data Description

HeQ (Hebrew QA) is a Hebrew machine reading comprehension benchmark containing 30,147 question-answer pairs derived from Hebrew Wikipedia articles and Israeli tech news (GeekTime). The dataset is split into train (90%), development (5%), and test (5%) sets, with annotations produced by native Hebrew speakers through a controlled crowdsourcing protocol with quality-tiered evaluation (rejected, verified, good, gold).


## Notes


## Citation Info

3 citations (Semantic Scholar/DOI) [2025-08-27] 10 citations (Semantic Scholar/DOI) [2025-08-23] 1 citations (Crossref/DOI) [2025-08-23]
