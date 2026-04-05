---






































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0534
type: conferencePaper
short_title: "Offensive Language Identification in Greek"
year: 2020
first_author: "[[Zeses Pitenis]]"
last_author: "[[Tharindu Ranasinghe]]"
authors: Zeses Pitenis; Marcos Zampieri; Tharindu Ranasinghe
url: "https://aclanthology.org/2020.lrec-1.629/"
external_pdf: "https://arxiv.org/pdf/2003.07459.pdf"
publication: "ACL Anthology / LREC 2020"
CONF-CC: "LREC 2020"
pdf_extract: "PDF Extracts/2020/2020-Pitenis-Offensive Language Identification in Greek.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2020/2020-Pitenis-Offensive Language Identification in Greek.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "Greek"
religious_values: "N/A"
rv_islam: 5
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
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: 
LLM_assessed: "BERT"
DATA_URL: NA
tags: 
abstract: "As offensive language has become a rising issue for online communities and social media platforms, researchers have been investigating ways of coping with abusive content and developing systems to detect its different types: cyberbullying, hate speech, aggression, etc. With a few notable exceptions, most research on this topic so far has dealt with English. This is mostly due to the availability of language resources for English."
CONFERENCE: "ACL 2020"
ethics_overall: 100
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
author_country: "CA"
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 84
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation approach annotated dataset"
data_metrics: "Not specified"
---
# Offensive Language Identification in Greek

## Authors

[[Zeses Pitenis]], [[Marcos Zampieri]], [[Tharindu Ranasinghe]]

## Metadata

**Authors:** Zeses Pitenis, Marcos Zampieri, Tharindu Ranasinghe

**Year:** 2020

**Type:** conferencePaper

**Venue:** ACL Anthology / LREC 2020

**Languages:** Greek

**Benchmark:** OGTD

## Links

- **arXiv:** https://arxiv.org/abs/2003.07459
- **URL:** https://aclanthology.org/2020.lrec-1.629/
- **Code/Data:** https://github.com/intelligence-csd-auth-gr/Ethos-Hate-Speech-Dataset

## Abstract

Presents the first Greek annotated dataset for offensive language identification: the Offensive Greek Tweet Dataset (OGTD), containing 4,779 manually annotated Twitter posts. Evaluates several computational models from traditional ML to BERT and DistilBERT transformers.

## Summary

This paper presents the Offensive Greek Tweet Dataset (OGTD), the first manually annotated dataset for offensive language identification in Greek, containing 4,779 Twitter posts collected using keyword-based queries and trending hashtags during the 2019 Greek elections and television programs. The dataset follows the OLID annotation framework for binary offensive/non-offensive classification. The authors evaluate multiple computational models including traditional machine learning approaches, LSTMs with attention, and BERT-based transformers, with the best system achieving 0.89 F1 score, establishing baseline performance for Greek offensive language detection.

## Data Description

OGTD (Offensive Greek Tweet Dataset): 4,779 manually annotated Greek Twitter posts for offensive language identification, later expanded to 10,287 in v2.0.


## Detailed Summary

This paper presents the Offensive Greek Tweet Dataset (OGTD), the first manually annotated dataset for offensive language identification in Greek, containing 4,779 Twitter posts annotated as offensive or not offensive. The dataset was constructed using keyword-based queries targeting common Greek slurs and offensive terms, as well as trending hashtags during the 2019 Greek elections and popular television programs. The annotation follows the OLID (Offensive Language Identification Dataset) framework for binary offensive/non-offensive classification, with posts collected and annotated by a team of volunteers to ensure high-quality labels.

The authors evaluate several computational models on OGTD, progressing from traditional machine learning approaches to deep learning architectures. Models tested include Naive Bayes, SVM, and Logistic Regression with bag-of-words and TF-IDF features, as well as LSTMs and GRU networks with attention mechanisms using pre-trained fastText Greek word embeddings. Transformer-based models including BERT and DistilBERT (using multilingual versions) are also evaluated. The best results are achieved by the LSTM/GRU with attention model, reaching 0.89 F1 score. The paper addresses a significant gap in non-English offensive language detection resources, as prior work had been limited to a handful of languages with few resources available for Greek.

## Paper Outline

1. Introduction - Motivation and overview of OGTD
2. Related Work - Offensive language and hate speech detection, non-English datasets
3. Dataset - OGTD collection methodology, annotation, and statistics
4. Experiments - Models evaluated and experimental setup
5. Results - Performance comparison across models
6. Conclusion - Summary and future work

## Methods Summary

Data collection uses the Twitter Search API with keyword queries targeting Greek offensive terms and trending hashtags from politically and socially charged events (2019 Greek elections, television shows). Annotation follows a binary scheme (offensive/not offensive) inspired by OLID. Models evaluated include: (1) traditional classifiers (Naive Bayes, SVM, Logistic Regression) with BoW/TF-IDF features; (2) LSTM and GRU networks with attention mechanisms using 300-dimensional pre-trained fastText Greek word embeddings; (3) transformer models including multilingual BERT and DistilBERT fine-tuned on the Greek data.

## Results Summary

The LSTM/GRU with attention model achieves the best F1 score of 0.89, outperforming both traditional machine learning baselines and transformer-based approaches on this dataset. Traditional classifiers achieve reasonable but lower performance, with SVM being the best among them. Multilingual BERT and DistilBERT show competitive but not superior performance compared to the attention-based recurrent models, likely due to the limited Greek-specific vocabulary in multilingual models. The dataset shows approximately balanced class distribution between offensive and non-offensive posts, which contributes to the reliability of the evaluation results.

## Conclusions

The authors note that OGTD is a first step toward Greek offensive language detection and can be extended with more fine-grained annotations following the full OLID hierarchy (targeted vs. untargeted, target type). Future work includes expanding the dataset size, adding sub-categories for different types of offensive language, and developing Greek-specific language models that may improve transformer-based detection.

## Artifact Contributions

No publicly released artifacts identified.

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B9
**Relevance:** Foundational Greek offensive language/hate speech detection dataset. First annotated resource for Greek offensive language identification. Directly relevant to toxicity and safety evaluation in Greek.

## Tags

