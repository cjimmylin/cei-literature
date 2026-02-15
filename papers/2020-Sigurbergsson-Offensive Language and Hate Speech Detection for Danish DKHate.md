---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0490
type: conferencePaper
short_title: "Offensive Language and Hate Speech Detection for Danish (DKHate)"
year: 2025
first_author: "[[Gudbjartur Ingi Sigurbergsson]]"
last_author: "[[Leon Derczynski]]"
authors: "Gudbjartur Ingi Sigurbergsson, Leon Derczynski"
url: "https://aclanthology.org/2020.lrec-1.430/"
external_pdf: "https://arxiv.org/pdf/1908.04531.pdf"
publication: "ACL Anthology / LREC 2020"
pdf_extract: "PDF Extracts/2020/2020-Sigurbergsson-Offensive Language and Hate Speech Detection for Danish DKHate.md"
local_pdf: "[[PDFs/2020/2020-Sigurbergsson-Offensive Language and Hate Speech Detection for Danish DKHate.pdf]]"
DATE_ADDED: 20260213
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
languages_list: Danish
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Annotated dataset for hate speech detection"
data_metrics: "Not specified"
LLM_assessed: BERT
DATA_URL: "https://github.com/guscode/dkhate"
tags: 
abstract: "The presence of offensive language on social media platforms and the implications this poses is becoming a major concern in modern society. Given the enormous amount of content created every day, automatic methods are required to detect and deal with this type of content. Until now, most of the research has focused on solving the problem for the English language, while the problem is multilingual. We construct a Danish dataset containing user-generated comments from Reddit and Facebook."
ethics_perspective: "Toxicity & Hate Speech"
---
# Offensive Language and Hate Speech Detection for Danish (DKHate)

## Authors

[[Gudbjartur Ingi Sigurbergsson, Leon Derczynski]]

## Metadata

**Authors:** Gudbjartur Ingi Sigurbergsson, Leon Derczynski

**Year:** 2020

**Type:** conferencePaper

**Venue:** ACL Anthology / LREC 2020

**Languages:** Danish

**Benchmark:** DKHate

## Links

- **arXiv:** https://arxiv.org/abs/1908.04531
- **URL:** https://aclanthology.org/2020.lrec-1.430/
- **Code/Data:** https://huggingface.co/datasets/DDSC/dkhate

## Abstract

First Danish hate speech/offensive language dataset with 3,600 annotated comments from various social media platforms following the OLID annotation scheme. Provides train/test splits for benchmarking.

## Summary

This paper introduces DKHate, the first Danish dataset for offensive language and hate speech detection, containing 3,600 user-generated comments from Reddit and Facebook annotated using the OLID three-level hierarchical framework (offensive vs. non-offensive, targeted vs. untargeted, and target type). The authors develop four automatic classification systems designed to work for both English and Danish, with the best Danish system achieving macro F1 scores of 0.70 for offensive language detection, 0.73 for targeting detection, and 0.63 for target type classification. The dataset addresses the multilingual gap in offensive language research and captures characteristics of hate speech and cyberbullying.

## Data Description

DKHate dataset for offensive language and hate speech detection in Danish, containing annotated comments from Reddit and Facebook. Evaluates Danish BERT models and multilingual models on binary offensive language classification.


## Detailed Summary

This paper introduces DKHate, the first Danish dataset for offensive language and hate speech detection, containing 3,600 user-generated comments from Reddit and Facebook. The dataset is annotated following the three-level hierarchical OLID annotation scheme: Sub-task A classifies posts as offensive (OFF) or not offensive (NOT); Sub-task B determines whether offensive posts are targeted (TIN) or untargeted (UNT); and Sub-task C identifies the target type as individual (IND), group (GRP), or other (OTH). The paper provides extensive background on hate speech regulation, noting that hate speech is prohibited by law in Denmark (targeting groups based on nationality, ethnicity, religion, or sexual orientation) and across the European Union, while being protected under the First Amendment in the United States.

The authors develop four automatic classification systems designed to work for both English (using the OLID dataset) and Danish (using DKHate): Logistic Regression with character and word n-grams, BiLSTM with fastText embeddings, CNN with fastText embeddings, and BERT-based models. For Danish, the best system achieves macro F1 scores of 0.70 for offensive language identification (Sub-task A), 0.73 for targeting detection (Sub-task B), and 0.63 for target type classification (Sub-task C). The paper also analyzes error patterns, identifying linguistic features that prove challenging for automatic detection, such as implicit hate speech without explicit profanity.

## Paper Outline

1. Introduction - Motivation for Danish offensive language detection
2. Background - Definitions of cyberbullying, hate speech, and contradicting definitions
3. Dataset - Classification structure (three sub-tasks), collection and annotation
4. Methods - Four classification systems for English and Danish
5. Results - Performance comparison across models and sub-tasks
6. Error Analysis - Patterns difficult to detect
7. Conclusion

## Methods Summary

Four classification systems are developed and evaluated on both English (OLID) and Danish (DKHate) data: (1) Logistic Regression with character n-grams (2-5) and word n-grams (1-3) using TF-IDF weighting; (2) BiLSTM with 2 layers, 512 hidden units, and pre-trained fastText word embeddings; (3) CNN with multiple filter sizes and fastText embeddings; (4) BERT-based transformer models using multilingual BERT. Data collection involves keyword-based and topic-based sampling from Danish Reddit and Facebook, with annotation by trained annotators following the OLID hierarchical schema. Cohen's Kappa inter-annotator agreement is measured on a subset of doubly-annotated instances.

## Results Summary

For Danish, the best Sub-task A performance (offensive language identification) achieves macro F1 of 0.70. Sub-task B (targeting detection) achieves the highest macro F1 of 0.73, while Sub-task C (target type classification) reaches 0.63 macro F1. For English comparison, the best systems achieve 0.74 (A), 0.62 (B), and 0.56 (C) macro F1 scores, showing that Danish models perform comparably despite less training data. BERT-based models and logistic regression with n-gram features show competitive performance, with the optimal approach varying by sub-task. Error analysis reveals that implicit hate speech (without explicit profanity) and context-dependent offensive language are the most challenging patterns for all models.

## Conclusions

The paper identifies the lack of consensus in hate speech definitions and annotation schemas as a key challenge for cross-dataset comparison. Future work includes expanding the dataset with more diverse sources, developing Danish-specific language models, and exploring the three-level hierarchical classification in an end-to-end pipeline. The authors note that the dataset's relatively small size limits the performance of data-hungry deep learning approaches.

## Artifact Contributions

- **DKHate Dataset**: First Danish offensive language and hate speech dataset with hierarchical OLID annotations (https://github.com/guscode/dkhate)

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** Foundational Danish offensive language/hate speech detection dataset.

## Tags

