---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0536
type: preprint
short_title: "ETHOS: an Online Hate Speech Detection Dataset"
year: 2025
first_author: "[[Ioannis Mollas]]"
last_author: "[[Grigorios Tsoumakas]]"
authors: "Ioannis Mollas, Zoe Chrysopoulou, Stamatis Karlos, Grigorios Tsoumakas"
doi: 10.1007/s40747-021-00608-2
url: "https://arxiv.org/abs/2006.08328"
external_pdf: "https://arxiv.org/pdf/2006.08328.pdf"
publication: "arXiv / Complex & Intelligent Systems"
pdf_extract: "PDF Extracts/2020/2020-Mollas-ETHOS an Online Hate Speech Detection Dataset.md"
local_pdf: "[[PDFs/2020/2020-Mollas-ETHOS an Online Hate Speech Detection Dataset.pdf]]"
DATE_ADDED: 20260213
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "American"
languages_list: English
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Text corpus for hate speech detection"
data_metrics: "Not specified"
LLM_assessed: BERT
DATA_URL: "https://github.com/intelligence-csd-auth-gr/Ethos-Hate-Speech-Dataset"
tags: 
abstract: "Online hate speech is a recent problem in our society that is rising at a steady pace by leveraging the vulnerabilities of the corresponding regimes that characterise most social media platforms. This phenomenon is primarily fostered by offensive comments, either during user interaction or in the form of a posted multimedia context. Nowadays, giant corporations own platforms where millions of users log in every day, and protection from exposure to similar phenomena appears to be necessary in..."
ethics_perspective: "Toxicity & Hate Speech"
---
# ETHOS: an Online Hate Speech Detection Dataset

## Authors

[[Ioannis Mollas, Zoe Chrysopoulou, Stamatis Karlos, Grigorios Tsoumakas]]

## Metadata

**Authors:** Ioannis Mollas, Zoe Chrysopoulou, Stamatis Karlos, Grigorios Tsoumakas

**Year:** 2020

**Type:** preprint

**Venue:** arXiv / Complex & Intelligent Systems

**DOI:** [10.1007/s40747-021-00608-2](https://doi.org/10.1007/s40747-021-00608-2)

**Languages:** English

**Benchmark:** ETHOS

## Links

- **arXiv:** https://arxiv.org/abs/2006.08328
- **DOI:** https://doi.org/10.1007/s40747-021-00608-2
- **Code/Data:** https://huggingface.co/datasets/iamollas/ethos

## Abstract

A textual dataset with binary and multi-label variants for hate speech detection, based on YouTube and Reddit comments. Contains 998 comments with labels about hate speech presence or absence. By Greek researchers at Aristotle University of Thessaloniki.

## Summary

This paper presents ETHOS, an online hate speech detection dataset containing approximately 998 YouTube and Reddit comments with both binary (hate speech or not) and multi-label annotations validated using the Figure-Eight crowdsourcing platform. The multi-label annotations include violence, directed/undirected hate, and target groups (race, religion, gender, sexual orientation, national origin, disability). The authors employ an active sampling procedure to balance the dataset across various aspects and evaluate performance using BERT and traditional machine learning classifiers, demonstrating that careful dataset design during the sampling stage improves model performance despite limited dataset size.

## Data Description

ETHOS dataset for online hate speech detection in English with binary and multi-label annotations. Contains Reddit and YouTube comments annotated for violence, directed/undirected hate, and target groups. Evaluated with BERT and traditional ML classifiers.


## Detailed Summary

This paper presents ETHOS (onlinE haTe speecH detectiOn dataSet), a hate speech detection dataset with two variants: binary and multi-label, constructed from YouTube and Reddit comments and validated using the Figure-Eight (now Appen) crowdsourcing platform. The dataset contains approximately 998 annotated comments in English. The binary variant classifies comments as hate speech or not, while the multi-label variant annotates eight dimensions: violence, directed vs. undirected hate, and target categories including gender, race, national origin, disability, religion, and sexual orientation. A key contribution is the active sampling annotation protocol designed to ensure balanced representation across hate speech categories while maintaining dataset informativeness, addressing common problems of class imbalance and redundancy in existing hate speech datasets.

The authors benchmark ETHOS using a range of approaches spanning traditional machine learning (Random Forest, Gradient Boosting, Logistic Regression, Naive Bayes), neural networks with and without word embeddings (fastText, GloVe), and BERT-based transformer models. Despite the dataset's limited size, its careful design during the active sampling stage yields competitive classification results. The multi-label formulation is argued to be more practical than binary classification, as it provides human reviewers with richer information about the nature and targets of hateful content, enabling more informed moderation decisions. The dataset and annotation protocol are publicly available to foster research in hate speech detection.

## Paper Outline

1. Introduction - Hate speech problem and motivation for multi-label approach
2. Related Datasets - Survey of existing hate speech datasets
3. Annotation Protocol - Active sampling procedure for balanced dataset creation
4. Experiments - Binary and multi-label classification using ML and DL models
5. Cross-dataset Evaluation - Generalization tests on external datasets
6. Discussion and Conclusion - Dataset assets and future directions

## Methods Summary

The annotation protocol uses an active sampling procedure starting from seed data (Hatebusters dataset from social media), iteratively selecting informative instances for crowdsourced annotation to ensure class balance. Binary and multi-label experiments are conducted using: (1) traditional ML algorithms including Random Forest, Gradient Boosting, Logistic Regression, and Naive Bayes with TF-IDF features; (2) neural networks including BiLSTM and CNN with fastText and GloVe embeddings; and (3) BERT-based transformers. The multi-label task uses binary relevance decomposition. Cross-dataset evaluation tests generalization to Davidson et al. (2017) and the multilingual MLMA dataset.

## Results Summary

BERT-based models achieve the best binary classification performance on ETHOS. In multi-label classification, the most challenging categories to detect are those with fewer training examples and more subtle linguistic markers. The active sampling protocol produces a more balanced dataset compared to random sampling approaches, resulting in improved detection of underrepresented hate speech categories. Cross-dataset experiments demonstrate reasonable generalization, though performance degrades when transferring between datasets with different annotation schemas and data sources, highlighting the ongoing challenge of building robust hate speech detectors.

## Conclusions

The authors emphasize that the active sampling approach, while producing a smaller dataset, ensures higher quality and balance than larger but randomly sampled alternatives. The multi-label perspective provides more actionable insights for content moderation than binary classification. Future work includes extending the annotation protocol to other domains, incorporating multimedia content analysis, and developing more sophisticated active learning strategies for hate speech detection.

## Artifact Contributions

- **ETHOS Dataset**: Binary and multi-label hate speech dataset from YouTube and Reddit comments (https://github.com/intelligence-csd-auth-gr/Ethos-Hate-Speech-Dataset)

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B9
**Relevance:** While in English, developed by Greek researchers. Multi-label hate speech detection covering gender, race, national origin, disability, religion, and sexual orientation. Foundational dataset for hate speech benchmarking.

## Tags

