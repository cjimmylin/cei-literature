---




























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0462
type: conferencePaper
short_title: "DeTox: A Comprehensive Dataset for German Offensive Language and Conversation Analysis"
year: 2022
first_author: "[[Christoph Demus]]"
last_author: "[[Udo Kruschwitz]]"
authors: Christoph Demus; Jonas Pitz; Mina Schussler; Dirk Labudde; Udo Kruschwitz
url: "https://aclanthology.org/2022.woah-1.14/"
external_pdf: "https://aclanthology.org/2022.woah-1.14.pdf"
publication: "ACL Anthology"
CONF-CC: "N/A"
pdf_extract: "PDF Extracts/2022/2022-Demus-DeTox A Comprehensive Dataset for German Offensive Language and.md"
local_pdf: "[[PDFs/2022/2022-Demus-DeTox A Comprehensive Dataset for German Offensive Language and.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "German"
cultures_nationalities_list: "German"
languages_list: "German"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: BERT
DATA_URL: "https://github.com/hdaSprachtechnologie/detox"
tags: 
abstract: "In this work, we present a publicly available offensive language dataset (DeTox-dataset) containing 10,278 annotated German social media comments collected in the first half of 2021. With twelve different annotation categories annotated by six annotators, it is far more comprehensive than other datasets, and goes beyond just hate speech detection. The labels aim in particular also at toxicity, criminal relevance and discrimination types of comments."
CONFERENCE: "ACL 2022"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Toxicity & Hate Speech"
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Dataset for toxicity detection"
data_metrics: "Not specified"
---
# DeTox: A Comprehensive Dataset for German Offensive Language and Conversation Analysis

## Authors

[[Christoph Demus]], [[Jonas Pitz]], [[Mina Schussler]], [[Dirk Labudde]], [[Udo Kruschwitz]]

## Metadata

**Authors:** Christoph Demus, Jonas Pitz, Mina Schussler, Dirk Labudde, Udo Kruschwitz

**Year:** 2022

**Type:** conferencePaper

**Venue:** ACL Anthology

**Languages:** German

**Benchmark:** DeTox

## Links

- **URL:** https://aclanthology.org/2022.woah-1.14/
- **Code/Data:** https://github.com/hdaSprachtechnologie/detox

## Abstract

A publicly available dataset of 10,278 German social media comments with 12 annotation categories covering toxicity, criminal relevance, and discrimination types. About half the comments come from coherent conversations, enabling conversation-level analysis of offensive language contagion.

## Summary

This paper presents DeTox, a comprehensive German offensive language dataset containing 10,278 annotated social media comments collected in early 2021 with twelve annotation categories covering hate speech, toxicity, sentiment, criminal relevance (under German law), threat, and various discrimination types (age, gender, ethnicity, religion, sexual orientation). Uniquely, approximately half of the comments come from coherent conversation threads, enabling context-aware analysis and research on the contagion of offensive language in conversations. The dataset was evaluated using BERT-based models and supports fine-grained classification beyond binary hate speech detection, developed to assist the Hessen state government's hate comment reporting center.

## Data Description

DeTox dataset of 10,278 annotated German social media comments with 12 annotation categories covering toxicity, criminal relevance, discrimination types, and conversation-level analysis.


## Detailed Summary

This paper presents DeTox, a comprehensive German offensive language dataset containing 10,278 annotated social media comments collected in the first half of 2021. What distinguishes DeTox from other German hate speech datasets is its breadth of annotation: twelve different categories are annotated by six annotators, covering hate speech, toxicity, sentiment, criminal relevance (under German law), threat level, and discrimination types (age, gender, ethnicity, religion, sexual orientation). This goes well beyond the binary hate speech classification that characterizes most existing datasets. The dataset was developed to support the Hessen state government's hate comment reporting center (hessengegenhetze.de), providing a concrete application for fine-grained offensive language classification.

A particularly innovative feature is that approximately half of the comments come from coherent conversation threads, enabling context-aware analysis and research on the contagion of offensive language within online discussions. This conversational structure allows researchers to study how toxic language spreads through conversation dynamics, a dimension not captured by datasets of isolated comments. The paper provides baseline results using BERT-based models and compares DeTox to existing German datasets including GermEval 2018/2019 (15,567 Twitter posts), HASOC 2019 (4,669 posts), and GermEval 2021 (4,188 Facebook comments), noting that DeTox's twelve annotation categories offer significantly broader research and application possibilities.

## Paper Outline

1. Introduction - Motivation and three main contributions
2. Related Work - German hate speech datasets overview
3. Dataset - Collection methodology, annotation schema, corpus statistics
4. Annotation - 12 categories, inter-annotator agreement, quality control
5. Experiments - BERT-based baseline classification
6. Discussion - Results and comparison to existing datasets
7. Conclusion

## Methods Summary

Data collection targets German social media comments from platforms including Facebook and Twitter, with approximately half collected as coherent conversation threads. Six trained annotators label each comment across twelve categories using detailed annotation guidelines. Categories include binary hate speech, toxicity level, sentiment, criminal relevance under German law, threat presence, and discrimination targeting (by age, gender, ethnicity, religion, sexual orientation). Inter-annotator agreement is measured across all categories. Baseline experiments use fine-tuned German BERT models for multi-label classification, with separate classifiers for each annotation dimension and macro-averaged F1 as the primary evaluation metric.

## Results Summary

DeTox provides 10,278 annotated German social media comments with twelve annotation dimensions, making it one of the most comprehensively annotated German hate speech datasets. Approximately 10.85% of posts are classified as abusive, comparable to rates found in other German datasets. BERT-based baseline models achieve varying performance across the twelve annotation categories, with hate speech and toxicity detection being more tractable than fine-grained discrimination type classification. The inclusion of conversation context enables preliminary analysis of how offensive language propagates through discussion threads, revealing patterns of escalation and de-escalation in online conversations.

## Conclusions

The twelve-category annotation schema opens broad research opportunities beyond basic hate speech detection, including analysis of conversation dynamics, criminal relevance assessment, and discrimination type classification. Future work includes expanding the dataset, developing context-aware models that leverage conversation structure, and investigating the relationship between different annotation dimensions (e.g., correlation between toxicity and criminal relevance). The practical application for the Hessen state government demonstrates the real-world utility of fine-grained offensive language classification.

## Artifact Contributions

- **DeTox Dataset**: 10,278 German social media comments with 12 annotation categories (https://github.com/hdaSprachtechnologie/detox)

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** Comprehensive German offensive language dataset with 12 fine-grained annotation categories including toxicity and discrimination.

## Tags

