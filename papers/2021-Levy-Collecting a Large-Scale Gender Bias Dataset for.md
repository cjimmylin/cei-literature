---



























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 9HCC2BT4
type: document
short_title: "Collecting a Large-Scale Gender Bias Dataset for"
year: 2021
first_author: "[[Shahar Levy]]"
last_author: "[[Stanovsky, Gabriel]]"
authors: "Levy, Shahar; Lazar, Koren; Stanovsky, Gabriel"
url: "https://aclanthology.org/2021.findings-emnlp.211/"
external_pdf: "https://aclanthology.org/2021.findings-emnlp.211.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Bias & Fairness"
key_contribution: "Collected a large-scale (108k) dataset of *real-world* (not synthetic) gender bias examples for Coreference Resolution and Machine Translation."
significance: "Demonstrates that synthetic bias benchmarks (like WinoBias) underestimate the problem; models fail even harder on messy, real-world stereotypes (e.g., 'male dancers')."
tags: 
pdf_extract: "PDF Extracts/2021/2021-Levy-Collecting a Large-Scale Gender Bias Dataset for.md"
local_pdf: "[[PDFs/2021/2021-Levy-Collecting a Large-Scale Gender Bias Dataset for.pdf]]"
abstract: "Recent works have found evidence of gender bias in models of machine translation and coreference resolution using mostly synthetic diagnostic datasets. While these quantify bias in a controlled experiment, they often do so on a small scale and consist mostly of artiﬁcial, out-of-distribution sentences. In this work, we ﬁnd grammatical patterns indicating stereotypical and non-stereotypical gender-role assignments (e.g."
CONF-CC: "N/A"
DATE_ADDED: 20260208
LLM_assessed: BERT
DATA_URL: "https://github.com/SLAB-NLP/BUG"
CONFERENCE: "EMNLP 2021"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation approach text corpus"
data_metrics: "Not specified"
---
# Collecting a Large-Scale Gender Bias Dataset for Coreference Resolution and Machine Translation

## Authors

[[Shahar Levy|Levy, Shahar]], [[Koren Lazar|Lazar, Koren]], [[Gabriel Stanovsky|Stanovsky, Gabriel]]

## Links

- **Local PDF:** [[PDFs/2021/2021-Levy-Collecting a Large-Scale Gender Bias Dataset for.pdf|Open PDF]]

- **ACL Anthology:** https://aclanthology.org/2021.findings-emnlp.211/

## Abstract

Recent works have found evidence of gender bias in models of machine translation and coreference resolution using mostly synthetic diagnostic datasets. While these quantify bias in a controlled experiment, they often do so on a small scale and consist mostly of artificial, out-of-distribution sentences. In this work, we find grammatical patterns indicating stereotypical and non-stereotypical gender-role assignments (e.g., female nurses versus male dancers) in corpora from three domains, resulting in a first large-scale gender bias dataset of 108K diverse real-world English sentences. We manually verify the quality of our corpus and use it to evaluate gender bias in various coreference resolution and machine translation models. We find that all tested models tend to over-rely on gender stereotypes when presented with natural inputs, which may be especially harmful when deployed in commercial systems. Finally, we show that our dataset lends itself to finetuning a coreference resolution model, finding it mitigates bias on a held out set. Our dataset and models are publicly available at github.com/SLAB-NLP/BUG. We hope they will spur future research into gender bias evaluation mitigation techniques in realistic settings.

## Data Description

BUG is a large-scale gender bias dataset containing 108,419 diverse real-world English sentences semi-automatically collected from Wikipedia, PubMed, and COVID-19 research corpora using 14 lexical-syntactic patterns. Each sentence contains a human entity identified by profession and a gendered pronoun, marked as stereotypical, anti-stereotypical, or neutral with respect to gender-role assignments for evaluating bias in coreference resolution and machine translation.


## Notes

