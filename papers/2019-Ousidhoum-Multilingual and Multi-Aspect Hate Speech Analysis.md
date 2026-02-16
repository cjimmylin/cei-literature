---





Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0456
type: preprint
short_title: "Multilingual and Multi-Aspect Hate Speech Analysis"
year: 2019
first_author: "[[Ousidhoum, Nedjma]]"
last_author: "[[Yeung, Dit-Yan]]"
authors: "[[Ousidhoum, Nedjma]]; [[Lin, Zizheng]]; [[Zhang, Hongming]]; [[Song, Yangqiu]]; [[Yeung, Dit-Yan]]"
authors_incomplete: false
url: "https://arxiv.org/abs/1908.11049"
external_pdf: "https://arxiv.org/pdf/1908.11049.pdf"
publication: arXiv
pdf_extract: "PDF Extracts/2019/2019-Ousidhoum-Multilingual and Multi-Aspect Hate Speech Analysis.md"
local_pdf: "[[PDFs/2019/2019-Ousidhoum-Multilingual and Multi-Aspect Hate Speech Analysis.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "Arabic, French"
cultures_nationalities_list: "Arabic, French, English"
languages_list: "Arabic, English, French"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: BiLSTM
DATA_URL: "https://github.com/HKUST-KnowComp/MLMA_hate_speech"
tags: 
abstract: "Current research on hate speech analysis is typically oriented towards monolingual and single classiﬁcation tasks. In this paper, we present a new multilingual multi-aspect hate speech analysis dataset and use it to test the current state-of-the-art multilingual multitask learning approaches. We evaluate our dataset in various classiﬁcation settings, then we discuss how to leverage our annotations in order to improve hate speech detection and classiﬁcation in general."
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Toxicity & Hate Speech"
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Dataset for hate speech detection"
data_metrics: "Not specified"
---
# Multilingual and Multi-Aspect Hate Speech Analysis

## Authors

[[Nedjma Ousidhoum|Ousidhoum, Nedjma]], [[Lin, Zizheng]], [[Zhang, Hongming]], [[Song, Yangqiu]], [[Yeung, Dit-Yan]]

## Metadata

**Authors:** Nedjma Ousidhoum; Zizheng Lin; Hongming Zhang; Yangqiu Song; Dit-Yan Yeung

**Year:** 2019

**Type:** preprint

**Venue:** arXiv

**Languages:** Arabic, English, French

## Links

- **arXiv:** https://arxiv.org/abs/1908.11049

## Abstract

Trilingual hate speech dataset comprising English, French, and Arabic tweets encompassing various targets and hostility types. Early work on multilingual hate speech analysis including French.

## Summary

This paper presents a multilingual multi-aspect hate speech dataset containing approximately 13,000 tweets in English, French, and Arabic with five annotation dimensions: directness, hostility type, target attribute, target group, and annotator sentiment. The authors evaluate BiLSTM models with Babylon multilingual embeddings using Sluice networks for multi-task learning across languages and annotation aspects. The work demonstrates that multilingual multitask learning can improve hate speech detection and classification, with the dataset and code publicly released to advance research in multilingual hate speech analysis.

## Data Description

Multilingual hate speech dataset comprising 13,000 tweets in English, French, and Arabic with five annotation aspects: directness, hostility type, target attribute, target group, and annotator sentiment. Tests BiLSTM models with Babylon multilingual embeddings using Sluice networks for multi-task learning.


## Detailed Summary

This paper presents a multilingual multi-aspect hate speech analysis dataset comprising approximately 13,000 tweets in English (5,647), French (4,014), and Arabic (3,353), annotated across five dimensions: directness (direct/indirect), hostility type (abusive, hateful, offensive, disrespectful, fearful, normal), target attribute (origin, gender, sexual orientation, religion, disability, other), target group (16 categories including women, immigrants, refugees, and various ethnic/religious groups), and annotator sentiment (disgust, shock, anger, sadness, fear, confusion, indifference). The dataset was annotated via Amazon Mechanical Turk with five annotators per tweet, using majority voting and multilabel annotations for the most subjective tasks. The authors highlight cultural and linguistic differences in hate speech across languages, noting for instance that French tweets contain more anti-African content related to immigration debates, while Arabic tweets show more hateful comments toward women.

The authors evaluate the dataset using bidirectional LSTM models with Babylon multilingual word embeddings and Sluice networks for multitask learning, comparing single-task single-language (STSL), single-task multilingual (STML), multitask single-language (MTSL), and multitask multilingual (MTML) settings. Results show that STSL models perform best on the binary directness classification task, while multilingual and multitask approaches improve performance on tasks with many labels and limited per-label training data, such as target group classification. The MTML setting achieves the best average macro-F1 of 0.31 on the hostility type task. Pairwise task training reveals that target attributes can improve hostility type classification, and the work provides the first trilingual hate speech dataset examining annotator reactions to hateful content.

## Paper Outline

1. Introduction - Motivation for multilingual multi-aspect hate speech analysis
2. Related Work - Existing hate speech datasets, non-English resources, multitask learning
3. Dataset - Data collection methodology, linguistic challenges, annotation process
4. Experiments - Models (LR, BiLSTM, Sluice networks), results across classification settings
5. Conclusion - Summary of contributions and future directions

## Methods Summary

The authors use Logistic Regression (LR) with bag-of-words features as a traditional baseline, and bidirectional LSTM (BiLSTM) models with Babylon multilingual word embeddings for deep learning approaches. For multitask learning, they employ Sluice networks that learn parameter sharing weights jointly with the model, using a 1-layer BiLSTM partitioned into shared and private subspaces with orthogonal regularization. The hidden layer dimension is 200, with SGD optimization and DyNet for computation. Cross-lingual alignment uses Babylon embeddings. Experiments use an 8:1:1 train/dev/test split, with the dev set used for threshold tuning in multilabel tasks.

## Results Summary

STSL models consistently outperform other settings on directness classification (average macro-F1 0.86), as this binary task does not benefit from multilingual or multitask approaches. For hostility type, the MTML setting achieves the best average macro-F1 (0.31), while MTSL outperforms STSL on most tasks. Target group classification benefits most from multilingual training due to the regularity of group identification words across languages. Pairwise task training reveals that target attributes improve hostility type classification by 0.01-0.05 F1 points. All deep learning models outperform BOW-based logistic regression in most multilabel settings. Inter-annotator agreement (Krippendorff alpha) ranges from 0.153 (English) to 0.244 (French), reflecting the inherent subjectivity of hate speech annotation.

## Conclusions

The authors note that better-tuned multilingual and multitask models would be expected to outperform their current settings. Future work includes transfer learning, multimodal information integration, label transformation techniques, and leveraging the comparable corpora across languages to investigate how additional unlabeled data can boost classification. The low inter-annotator agreement highlights the continued challenge of annotator subjectivity in hate speech labeling.

## Artifact Contributions

- **MLMA Hate Speech Dataset**: Trilingual hate speech dataset of ~13,000 tweets in English, French, and Arabic with five-aspect annotations (https://github.com/HKUST-KnowComp/MLMA_hate_speech)

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** Early trilingual hate speech dataset including French tweets with target and hostility type annotations.

## Tags

