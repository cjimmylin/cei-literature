---




Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: P3AITYPK
type: conferencePaper
short_title: HateCheck
year: 2025
first_author: "[[Paul Röttger]]"
last_author: "[[Janet Pierrehumbert]]"
authors: "Paul Röttger; Bertie Vidgen; Dong Nguyen; Zeerak Waseem; Helen Margetts; Janet Pierrehumbert"
doi: 10.18653/v1/2021.acl-long.4
url: "https://aclanthology.org/2021.acl-long.4/"
external_pdf: "https://aclanthology.org/2021.acl-long.4.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: Utilitarianism
key_contribution: "Introduces HateCheck, a suite of functional tests for hate speech detection models, moving beyond simple F1/accuracy metrics"
significance: "Enables targeted diagnosis of model weaknesses (e.g., reclaiming slurs, counter-speech), a precursor to nuanced consequentialist evaluation of harm"
tags: 
pdf_extract: "PDF Extracts/2021/2021-Röttger-HateCheck.md"
local_pdf: [[PDFs/2021/2021-Röttger-HateCheck.pdf]]
abstract: "Detecting online hate is a difﬁcult task that even state-of-the-art models struggle with. Typically, hate speech detection models are evaluated by measuring their performance on held-out test data using metrics such as accuracy and F1 score. However, this approach makes it difﬁcult to identify speciﬁc model weak points. It also risks overestimating generalisable model performance due to increasingly well-evidenced systematic gaps and biases in hate speech datasets."
DATE_ADDED: 20260208
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "Yes"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation approach dataset for hate speech detection"
data_metrics: "Not specified"
LLM_assessed: BERT
DATA_URL: "https://github.com/paul-rottger/hatecheck-data"
---
# HateCheck: Functional Tests for Hate Speech Detection Models

## Metadata

**Authors:** Röttger, Paul; Vidgen, Bertie; Nguyen, Dong; Waseem, Zeerak; Margetts, Helen; Pierrehumbert, Janet

**Year:** 2021

**Publication:** Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)

**Type:** conferencePaper

**DOI:** [10.18653/v1/2021.acl-long.4](https://doi.org/10.18653/v1/2021.acl-long.4)

**Pages:** 41-58

**Publisher:** Association for Computational Linguistics

## Links

- **Local PDF:** [[PDFs/2021/2021-Röttger-HateCheck.pdf|Open PDF]]

- **ACL Anthology:** https://aclanthology.org/2021.acl-long.4
- **DOI:** https://doi.org/10.18653/v1/2021.acl-long.4

## Abstract

Detecting online hate is a difficult task that even state-of-the-art models struggle with. Typically, hate speech detection models are evaluated by measuring their performance on held-out test data using metrics such as accuracy and F1 score. However, this approach makes it difficult to identify specific model weak points. It also risks overestimating generalisable model performance due to increasingly well-evidenced systematic gaps and biases in hate speech datasets. To enable more targeted diagnostic insights, we introduce HateCheck, a suite of functional tests for hate speech detection models. We specify 29 model functionalities motivated by a review of previous research and a series of interviews with civil society stakeholders. We craft test cases for each functionality and validate their quality through a structured annotation process. To illustrate HateCheck’s utility, we test near-state-of-the-art transformer models as well as two popular commercial models, revealing critical model weaknesses.

## Authors

[[Paul Röttger]], [[Bertie Vidgen]], [[Dong Nguyen]], [[Zeerak Waseem]], [[Helen Margetts]], [[Janet Pierrehumbert]]

## Data Description

HateCheck is a suite of 3,728 functional test cases for hate speech detection models, covering 29 model functionalities grouped into 11 classes. The test cases include distinct expressions of hate and contrastive non-hateful content across seven protected groups (women, trans people, gay people, black people, disabled people, Muslims, immigrants). Two fine-tuned BERT-base models (trained on Davidson et al. and Founta et al. datasets) and two commercial models (Google Jigsaw's Perspective and Two Hat's SiftNinja) were evaluated on the test suite.


## Notes


## Citation Info

288 citations (Semantic Scholar/DOI) [2025-08-27] 288 citations (Semantic Scholar/DOI) [2025-08-23] 51 citations (Crossref/DOI) [2025-08-23]
