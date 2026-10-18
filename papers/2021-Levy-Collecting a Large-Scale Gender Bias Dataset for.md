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
newtags: "Bias & Fairness"
key_contribution: "Collected a large-scale (108k) dataset of *real-world* (not synthetic) gender bias examples for Coreference Resolution and Machine Translation."
significance: "Demonstrates that synthetic bias benchmarks (like WinoBias) underestimate the problem; models fail even harder on messy, real-world stereotypes (e.g., 'male dancers')."
tags: 
pdf_extract: "PDF Extracts/2021/2021-Levy-Collecting a Large-Scale Gender Bias Dataset for.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2021/2021-Levy-Collecting a Large-Scale Gender Bias Dataset for.pdf]]"
abstract: "Recent works have found evidence of gender bias in models of machine translation and coreference resolution using mostly synthetic diagnostic datasets. While these quantify bias in a controlled experiment, they often do so on a small scale and consist mostly of artiﬁcial, out-of-distribution sentences. In this work, we ﬁnd grammatical patterns indicating stereotypical and non-stereotypical gender-role assignments (e.g."
CONF-CC: N/A
DATE_ADDED: 20260208
LLM_assessed: BERT
DATA_URL: "https://github.com/SLAB-NLP/BUG"
CONFERENCE: "EMNLP 2021"
ethics_overall: 65
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Bias & Fairness"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: IL
author_region: MENA
author_global_north_south: "Global North"
weird_score: 57
is_benchmark: No
is_eval: Yes
is_dataset: Yes
data_description: "Evaluation approach text corpus"
data_metrics: "Not specified"
---
# Collecting a Large-Scale Gender Bias Dataset for Coreference Resolution and Machine Translation

## Authors

[[Shahar Levy|Levy, Shahar]], [[Koren Lazar|Lazar, Koren]], [[Gabriel Stanovsky|Stanovsky, Gabriel]]

## Links

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2021/2021-Levy-Collecting a Large-Scale Gender Bias Dataset for.pdf|Open PDF]]

- **ACL Anthology:** https://aclanthology.org/2021.findings-emnlp.211/

## Abstract

Recent works have found evidence of gender bias in models of machine translation and coreference resolution using mostly synthetic diagnostic datasets. While these quantify bias in a controlled experiment, they often do so on a small scale and consist mostly of artificial, out-of-distribution sentences. In this work, we find grammatical patterns indicating stereotypical and non-stereotypical gender-role assignments (e.g., female nurses versus male dancers) in corpora from three domains, resulting in a first large-scale gender bias dataset of 108K diverse real-world English sentences. We manually verify the quality of our corpus and use it to evaluate gender bias in various coreference resolution and machine translation models. We find that all tested models tend to over-rely on gender stereotypes when presented with natural inputs, which may be especially harmful when deployed in commercial systems. Finally, we show that our dataset lends itself to finetuning a coreference resolution model, finding it mitigates bias on a held out set. Our dataset and models are publicly available at github.com/SLAB-NLP/BUG. We hope they will spur future research into gender bias evaluation mitigation techniques in realistic settings.

## Data Description

BUG: 108K diverse real-world English sentences for large-scale gender bias evaluation in coreference resolution and machine translation, with stereotypical/anti-stereotypical labels.


## Notes

