---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: AHSMVJAF
type: journalArticle
short_title: "Toward Gender-Inclusive Coreference Resolution"
year: 2025
first_author: "[[Yang Trista Cao]]"
last_author: "[[Hal Daumé III]]"
authors: "Yang Trista Cao; Hal Daumé III"
doi: 10.1162/coli_a_00415
url: "https://direct.mit.edu/coli/article/47/3/615/102824/Toward-Gender-Inclusive-Coreference-Resolution-An"
external_pdf: "https://arxiv.org/pdf/1910.13913v4.pdf"
national_ethnic_cultural: N/A
religious_values: N/A
moral_psychology: N/A
newtags: "Bias & Fairness"
key_contribution: "Analyzed the entire ML lifecycle for gender bias in coreference resolution, proposing metrics for 'inclusive' resolution (handling neo-pronouns)."
significance: "Moves beyond binary gender bias to 'inclusivity', addressing the erasure of non-binary identities in coreference systems."
tags: 
abstract: "AbstractCurrently, deep learning models have been widely adopted and achieved promising results on various application domains. Despite their intriguing performance, most deep learning models function as black boxes, lacking explicit reasoning capabilities and explanations, which are usually essential for complex problems. Take joint inference in information extraction as an example. This task requires the identification of multiple structured knowledge from texts, which is inter-correlated, including entities, events, and the relationships between them. Various deep neural networks have been proposed to jointly perform entity extraction and relation prediction, which only propagate information implicitly via representation learning. However, they fail to encode the intensive correlations between entity types and relations to enforce their coexistence. On the other hand, some approaches adopt rules to explicitly constrain certain relational facts, although the separation of rules with representation learning usually restrains the approaches with error propagation. Moreover, the predefined rules are inflexible and might result in negative effects when data is noisy. To address these limitations, we propose a variational deep logic network that incorporates both representation learning and relational reasoning via the variational EM algorithm. The model consists of a deep neural network to learn high-level features with implicit interactions via the self-attention mechanism and a relational logic network to explicitly exploit target interactions. These two components are trained interactively to bring the best of both worlds. We conduct extensive experiments ranging from fine-grained sentiment terms extraction, end-to-end relation prediction, to end-to-end event extraction to demonstrate the effectiveness of our proposed method."
local_pdf: "[[PDFs/2021/2021-Cao-Toward Gender-Inclusive Coreference Resolution.pdf]]"
pdf_extract: "PDF Extracts/2021/2021-Cao-Toward Gender-Inclusive Coreference Resolution.md"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "Bias & Fairness"
is_benchmark: No
is_eval: No
is_dataset: No
data_description: N/A
data_metrics: "Not specified"
LLM_assessed: "NA"
DATA_URL: "https://github.com/TristaCao/into_inclusivecoref"
---
# Toward Gender-Inclusive Coreference Resolution: An Analysis of Gender and Bias Throughout the Machine Learning Lifecycle

## Metadata

**Authors:** Cao, Yang Trista; Daumé III, Hal

**Year:** 2021

**Publication:** Computational Linguistics

**Type:** journalArticle

**DOI:** [10.1162/coli_a_00415](https://doi.org/10.1162/coli_a_00415)

**Pages:** 615–661

**Volume/Issue:** Vol. 47, Issue 3

## Links

- **URL:** https://direct.mit.edu/coli/article/47/3/615/102824/Toward-Gender-Inclusive-Coreference-Resolution-An
- **DOI:** https://doi.org/10.1162/coli_a_00415

## Abstract

AbstractCurrently, deep learning models have been widely adopted and achieved promising results on various application domains. Despite their intriguing performance, most deep learning models function as black boxes, lacking explicit reasoning capabilities and explanations, which are usually essential for complex problems. Take joint inference in information extraction as an example. This task requires the identification of multiple structured knowledge from texts, which is inter-correlated, including entities, events, and the relationships between them. Various deep neural networks have been proposed to jointly perform entity extraction and relation prediction, which only propagate information implicitly via representation learning. However, they fail to encode the intensive correlations between entity types and relations to enforce their coexistence. On the other hand, some approaches adopt rules to explicitly constrain certain relational facts, although the separation of rules with representation learning usually restrains the approaches with error propagation. Moreover, the predefined rules are inflexible and might result in negative effects when data is noisy. To address these limitations, we propose a variational deep logic network that incorporates both representation learning and relational reasoning via the variational EM algorithm. The model consists of a deep neural network to learn high-level features with implicit interactions via the self-attention mechanism and a relational logic network to explicitly exploit target interactions. These two components are trained interactively to bring the best of both worlds. We conduct extensive experiments ranging from fine-grained sentiment terms extraction, end-to-end relation prediction, to end-to-end event extraction to demonstrate the effectiveness of our proposed method.

## Authors

[[Yang Trista Cao]], [[Hal Daumé III]]

## Data Description

The paper introduces two new datasets: MAP (Maybe Ambiguous Pronoun), a coreference dataset similar to GAP but without binary gender constraints used for counterfactual ablation studies, and GICoref (Gender Inclusive Coreference), a fully annotated coreference resolution dataset written by and about trans people. Five existing coreference resolution systems (AI2, HuggingFace, Stanford deterministic, statistical, and neural) are evaluated on these datasets to measure gender bias in annotations and model specifications.


## Notes


## Citation Info

7 citations (Semantic Scholar/DOI) [2025-08-27]
