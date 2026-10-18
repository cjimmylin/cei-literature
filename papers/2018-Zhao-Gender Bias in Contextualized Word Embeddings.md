---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 559CYS5K
type: journalArticle
short_title: "Gender Bias in Contextualized Word Embeddings"
year: 2018
first_author: "[[Jieyu Zhao]]"
last_author: "[[Kai-Wei Chang]]"
authors: "Jieyu Zhao; Yichao Zhou; Zeyu Li; Wei Wang; Kai-Wei Chang"
url: "https://arxiv.org/abs/1809.01496"
external_pdf: "https://arxiv.org/pdf/1809.01496.pdf"
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
key_contribution: "Proposed a training procedure for gender-neutral word embeddings (GN-GloVe) that isolates gender information to specific dimensions while neutralizing it in others."
significance: "Addressed foundational gender stereotyping in word embeddings (a precursor to LLMs), demonstrating that it's possible to reduce bias without systematically degrading model utility."
tags: 
pdf_extract: "PDF Extracts/2018/2018-Zhao-Gender Bias in Contextualized Word Embeddings.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2018/2018-Zhao-Gender Bias in Contextualized Word Embeddings.pdf]]"
abstract: "Word embedding models have become a fundamental component in a wide range of Natural Language Processing (NLP) applications. However, embeddings trained on human-generated corpora have been demonstrated to inherit strong gender stereotypes that reﬂect social constructs. To address this concern, in this paper, we propose a novel training procedure for learning gender-neutral word embeddings. Our approach aims to preserve gender information in certain dimensions of word vectors while compelling..."
paper_summary: "Abstract: Word embedding models have become a fun- damental component in a wide range of Natural Language Processing (NLP) appli- cations. However, embeddings trained on human-generated corpora have been demon- | Overview: Learning Gender-Neutral Word Embeddings Jieyu Zhao Yichao Zhou Zeyu Li Wei Wang Kai-Wei Chang University of California, Los Angeles {jyzhao, yz, zyli, weiwang, kwchang}@cs.ucla.edu Abstract Word embed | Methodology: In this paper, we take GloVe (Pennington et al., 2014) as the base embedding model and gender as the protected attribute. It is worth noting that our  | Conclusions: In this paper, we introduced an algorithm for train- ing gender-neutral word embedding. Our method is general and can be applied in any language as lo"
CONF-CC: N/A
DATE_ADDED: 20260208
LLM_assessed: NA
DATA_URL: "https://github.com/uclanlp/gn_glove"
doi: 10.18653/v1/D18-1521
CONFERENCE: Journal
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
author_country: US
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: No
is_eval: No
is_dataset: Yes
data_description: "Text corpus"
data_metrics: "Not specified"
---
# Gender Bias in Contextualized Word Embeddings (SemBias)

## Metadata

**Authors:** Zhao, Jieyu; Zhou, Yichao; Li, Zeyu; Wang, Wei; Chang, Kai-Wei

**Year:** 2018

**Publication:** arXiv preprint

**Type:** journalArticle

## Links

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2018/2018-Zhao-Gender Bias in Contextualized Word Embeddings.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/1809.01496

## Abstract

Word embedding models have become a fundamental component in a wide range of Natural Language Processing (NLP) applications. However, embeddings trained on human-generated corpora have been demonstrated to inherit strong gender stereotypes that reflect social constructs. To address this concern, in this paper, we propose a novel training procedure for learning gender-neutral word embeddings. Our approach aims to preserve gender information in certain dimensions of word vectors while compelling other dimensions to be free of gender influence. Based on the proposed method, we generate a Gender-Neutral variant of GloVe (GN-GloVe). Quantitative and qualitative experiments demonstrate that GN-GloVe successfully isolates gender information without sacrificing the functionality of the embedding model.

## Authors

[[Jieyu Zhao]], [[Yichao Zhou]], [[Zeyu Li]], [[Wei Wang]], [[Kai-Wei Chang]]

## Data Description

GN-GloVe: Gender-Neutral GloVe word embeddings trained on Wikipedia, plus SemBias analogy evaluation dataset (440 instances) for measuring gender stereotype vs. definitional word pairs.


## Notes


## Citation Info

419 citations (Semantic Scholar/arXiv) [2025-08-27]
