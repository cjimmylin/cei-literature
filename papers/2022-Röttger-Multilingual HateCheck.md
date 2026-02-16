---






Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 9RSV3LVL
type: journalArticle
short_title: "Multilingual HateCheck"
year: 2022
first_author: "[[Paul Röttger]]"
last_author: "[[Bertie Vidgen]]"
authors: "Paul Röttger; Haitham Seelawi; Debora Nozza; Zeerak Talat; Bertie Vidgen"
url: "https://arxiv.org/abs/2206.09917"
external_pdf: "https://arxiv.org/pdf/2206.09917.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "Cross-cultural"
languages_list: "Arabic, Chinese, Dutch, English, French, German, Hindi, Italian, Polish, Portuguese, Spanish"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: Utilitarianism
key_contribution: "Expanded HateCheck to 10 languages, providing functional tests for multilingual hate speech detection"
significance: "Crucial for global AI safety, revealing that multilingual models often fail to transfer specific safety functionalities across languages"
tags: 
osint_source: "Recovered via GITHUB"
pdf_extract: "PDF Extracts/2022/2022-Röttger-Multilingual HateCheck.md"
abstract: "Hate speech detection models are typically evaluated on held-out test sets. However, this risks painting an incomplete and potentially misleading picture of model performance because of increasingly well-documented systematic gaps and biases in hate speech datasets. To enable more targeted diagnostic insights, recent research has thus introduced functional tests for hate speech detection models. However, these tests currently only exist for English-language content, which means that they cannot..."
paper_summary: "Abstract: Hate speech detection models are typically evaluated on held-out test sets. However, this risks painting an incomplete and potentially misleading picture of model performance be- cause of increasingly | Overview: MULTILINGUAL HATECHECK: Functional Tests for Multilingual Hate Speech Detection Models Paul Röttger1,2, Haitham Seelawi1, Debora Nozza1,3, Zeerak Talat1,4, and Bertie Vidgen1 1Rewire 2University of Ox | Conclusions: MHC reveals clear functional weaknesses in the XTC model across all ten languages. First, XTC is overly sensitive to key words and phrases. XTC does h"
local_pdf: "[[PDFs/2022/2022-Röttger-Multilingual HateCheck.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: "XLM-T"
DATA_URL: "https://github.com/rewire-online/multilingual-hatecheck"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "Yes"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation approach dataset for hate speech detection"
data_metrics: "Not specified"
---
# Multilingual HateCheck: Functional Tests for Hate Speech Detection Models in 16 Languages

## Metadata

**Authors:** Röttger, Paul; Seelawi, Haitham; Nozza, Debora; Talat, Zeerak; Vidgen, Bertie

**Year:** 2022

**Publication:** arXiv preprint

**Type:** journalArticle

## Links

- **Local PDF:** [[PDFs/2022/2022-Röttger-Multilingual HateCheck.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2206.09917

## Abstract

Hate speech detection models are typically evaluated on held-out test sets. However, this risks painting an incomplete and potentially misleading picture of model performance because of increasingly well-documented systematic gaps and biases in hate speech datasets. To enable more targeted diagnostic insights, recent research has thus introduced functional tests for hate speech detection models. However, these tests currently only exist for English-language content, which means that they cannot support the development of more effective models in other languages spoken by billions across the world. To help address this issue, we introduce Multilingual HateCheck (MHC), a suite of functional tests for multilingual hate speech detection models. MHC covers 34 functionalities across ten languages, which is more languages than any other hate speech dataset. To illustrate MHC's utility, we train and test a high-performing multilingual hate speech detection model, and reveal critical model weaknesses for monolingual and cross-lingual applications.

## Authors

[[Paul Röttger]], [[Haitham Seelawi]], [[Debora Nozza]], [[Zeerak Talat]], [[Bertie Vidgen]]

## Data Description

The paper introduces Multilingual HateCheck (MHC), a suite of functional tests for multilingual hate speech detection models covering 34 functionalities across 10 languages (Arabic, Dutch, French, German, Hindi, Italian, Mandarin, Polish, Portuguese, Spanish) with 36,582 hand-crafted test cases. An XLM-T model fine-tuned on Spanish, Italian, and Portuguese hate speech datasets is evaluated, along with Google's Perspective API for comparison.


## Notes


## Citation Info

70 citations (Semantic Scholar/arXiv) [2025-08-27] _eprint: 2206.09917
