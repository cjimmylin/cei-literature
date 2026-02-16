---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: L2DU2UQX
type: conferencePaper
short_title: "Amharic Hate Speech Dataset"
year: 2025
first_author: "[[Abinet Ayele]]"
last_author: "[[Chris Biemann]]"
authors: "Abinet Ayele; Seid Muhie Yimam; Yaregal Assabie Belay; Moges Asfaw; Chris Biemann"
url: "https://aclanthology.org/2023.ranlp-1.6/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/UZ25W9FY/Ayele et al. - 2023 - Amharic Hate Speech Dataset.pdf"
national_ethnic_cultural: "African/Ubuntu"
cultures_nationalities_list: "Ethiopian"
languages_list: "Amharic"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "African/Ubuntu, Toxicity & Hate Speech"
key_contribution: "Created the first large-scale annotated hate speech dataset (15k tweets) for Amharic and benchmarked baseline models (AmFLAIR)."
significance: "Addresses the critical lack of safety resources for Amharic (Ethiopia), enabling the development of content moderation tools for a low-resource language with significant online conflict."
tags: 
abstract: "In this paper, we present a study of efficient data selection and annotation strategies for Amharic hate speech. We also build various classification models and investigate the challenges of hate speech data selection, annotation, and classification for the Amharic language. From a total of over 18 million tweets in our Twitter corpus, 15.1k tweets are annotated by two independent native speakers, and a Cohen’s kappa score of 0.48 is achieved."
DATE_ADDED: 20260208
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Toxicity & Hate Speech"
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Annotated dataset for hate speech detection"
data_metrics: "15.1k tweets"
LLM_assessed: RoBERTa
DATA_URL: "https://github.com/uhh-lt/AmharicHateSpeech"
pdf_extract: "PDF Extracts/2023/2023-Ayele-Amharic Hate Speech Dataset.md"
local_pdf: "[[PDFs/2023/2023-Ayele-Amharic Hate Speech Dataset.pdf]]"
---
# Amharic Hate Speech Dataset

## Metadata

**Authors:** Ayele, Abinet; Yimam, Seid Muhie; Belay, Yaregal Assabie; Asfaw, Moges; Biemann, Chris

**Year:** 2023

**Publication:** Proceedings of the International Conference on Recent Advances in Natural Language Processing (RANLP 2023)

**Type:** conferencePaper

## Links

- **ACL Anthology:** https://aclanthology.org/2023.ranlp-1.6/

## Abstract

In this paper, we present a study of efficient data selection and annotation strategies for Amharic hate speech. We also build various classification models and investigate the challenges of hate speech data selection, annotation, and classification for the Amharic language. From a total of over 18 million tweets in our Twitter corpus, 15.1k tweets are annotated by two independent native speakers, and a Cohen’s kappa score of 0.48 is achieved. A third annotator, a curator, is also employed to decide on the final gold labels. We employ both classical machine learning and deep learning approaches, which include fine-tuning AmFLAIR and AmRoBERTa contextual embedding models. Among all the models, AmFLAIR achieves the best performance with an F1-score of 72%. We publicly release the annotation guidelines, keywords/lexicon entries, datasets, models, and associated scripts with a permissive license.

## Authors

[[Abinet Ayele]], [[Seid Muhie Yimam]], [[Yaregal Assabie Belay]], [[Moges Asfaw]], [[Chris Biemann]]

## Data Description

The dataset consists of 15,100 Amharic tweets annotated for hate speech classification with four labels (hate, offensive, normal, unsure) by two independent native speakers plus a curator adjudicator, achieving a Cohen's kappa of 0.48. The tweets were sampled from a corpus of over 18 million Amharic tweets collected since 2014 via the Twitter API, with 3.8 million tweets from October 2020 to November 2021 filtered using hate and offensive lexicon entries and near-duplicate removal via Jaccard similarity.


## Notes

