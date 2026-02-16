---






Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: SRKAQM3X
type: journalArticle
year: 2025
short_title: "Overview of GermEval Task 2, 2019 Shared Task on"
first_author: "[[Julia Maria Struß]]"
last_author: "[[Manfred Klenner]]"
authors: "Julia Maria Struß; Melanie Siegel; Josef Ruppenhofer; Michael Wiegand; Manfred Klenner"
external_pdf: "file:///Users/jimmylin/Zotero/storage/ITICC3WW/Struß et al. - Overview of GermEval Task 2, 2019 Shared Task on the Identiﬁcation of Offensive Language.pdf"
national_ethnic_cultural: "German"
cultures_nationalities_list: "German"
languages_list: "German"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "German, Toxicity & Hate Speech"
key_contribution: "Shared task on offensive language identification in German tweets, introducing implicit vs explicit offense classification."
significance: "A standard reference for German toxicity detection, highlighting the difficulty of detecting 'implicit' offense (sarcasm, dogwhistles) compared to explicit slurs."
tags: 
abstract: "We present the second edition of the GermEval Shared Task on the Identiﬁcation of Offensive Language. This shared task deals with the classiﬁcation of German tweets from Twitter. Two subtasks were continued from the ﬁrst edition, namely a coarse-grained binary classiﬁcation task and a ﬁne-grained multi-class classiﬁcation task. As a novel subtask, we introduce the classiﬁcation of offensive tweets as explicit or implicit."
DATE_ADDED: 20260208
LLM_assessed: BERT
DATA_URL: "NA"
pdf_extract: "PDF Extracts/2019/2019-Struß-Overview of GermEval Task 2, 2019 Shared Task on.md"
local_pdf: "[[PDFs/2019/2019-Struß-Overview of GermEval Task 2, 2019 Shared Task on.pdf]]"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Toxicity & Hate Speech"
is_benchmark: "No"
is_eval: "No"
is_dataset: "No"
data_description: "N/A"
data_metrics: "Not specified"
---
# Overview of GermEval Task 2, 2019 Shared Task on the Identiﬁcation of Offensive Language

## Metadata

**Authors:** Struß, Julia Maria; Siegel, Melanie; Ruppenhofer, Josef; Wiegand, Michael; Klenner, Manfred

**Type:** journalArticle

## Links

- **Semantic Scholar:** https://www.semanticscholar.org/paper/f8e9851f175d9f8b87201118906b39f5491041b1

## Abstract

We present the second edition of the GermEval Shared Task on the Identiﬁcation of Offensive Language. This shared task deals with the classiﬁcation of German tweets from Twitter. Two subtasks were continued from the ﬁrst edition, namely a coarse-grained binary classiﬁcation task and a ﬁne-grained multi-class classiﬁcation task. As a novel subtask, we introduce the classiﬁcation of offensive tweets as explicit or implicit.

## Authors

[[Julia Maria Struß]], [[Melanie Siegel]], [[Josef Ruppenhofer]], [[Michael Wiegand]], [[Manfred Klenner]]

## Detailed Summary

This paper presents the second edition of the GermEval Shared Task on the Identification of Offensive Language, focusing on the classification of German tweets from Twitter. The shared task continued two subtasks from the 2018 edition and introduced a novel third subtask. Subtask 1 required binary classification of tweets as OFFENSE or OTHER. Subtask 2 involved fine-grained classification into four categories: PROFANITY (profane words without intent to insult), INSULT (clear intent to offend someone), ABUSE (degradation based on group membership or dehumanization), and OTHER. The new Subtask 3 introduced classification of offensive content as either EXPLICIT or IMPLICIT, addressing a significant challenge in offensive language detection.

The distinction between explicit and implicit offensive language is particularly valuable for the field. Implicit offensive language requires inference to understand the hate, condemnation, or degradation directed at a target, rather than stating aversion directly. This includes the use of sarcasm, irony, wordplay, or inappropriate casual language when addressing serious topics. The paper provides illustrative examples: suggesting someone's "swing was too close to the wall as a child" (implying stupidity through hypothetical consequences), or calling something "very honourable" when the context makes clear the opposite is meant (sarcasm). This classification challenge is important because implicit offensive content is harder to detect automatically and may evade simple keyword-based filters.

The shared task attracted 13 participating groups who submitted 28 runs each for Subtasks 1 and 2, and 17 runs for Subtask 3. The data collection strategy focused on sampling from user timelines rather than keyword-based sampling to ensure vocabulary diversity and include non-offensive tweets. The 2019 data deliberately expanded beyond right-wing content by incorporating left-wing sources and antisemitism-focused accounts. Careful debiasing was performed to prevent classifiers from learning spurious correlations between topics and offensiveness labels.

## Paper Outline

1. Introduction - Establishes the need for offensive language detection in social media
2. Related Work - Reviews prior shared tasks and German-language datasets
3. Task Description - Details all three classification subtasks
4. Data Set - Describes data collection, annotation, and quality control procedures
5. Systems and Results - Summarizes participating systems and their performance
6. Conclusions - Discusses outcomes and future directions

## Methods Summary

Data was collected from Twitter user timelines rather than keyword sampling to ensure diversity. The dataset includes tweets from extreme left-wing and right-wing sources, plus antisemitism-focused accounts. Annotation followed detailed guidelines distinguishing profanity, insult, and abuse. Debiasing involved adding non-offensive tweets containing politically relevant terms. For Subtask 3, tweets labeled as abuse or insult from GermEval 2018 were further annotated as explicit or implicit. Evaluation used macro-averaged precision, recall, and F-score rather than accuracy due to class imbalance.

## Results Summary

The shared task received strong participation with 13 teams. For Subtask 1 (binary), the best systems achieved macro F1 scores in the competitive range. Subtask 2 (4-way) proved more challenging given the fine-grained distinctions required. Subtask 3 (implicit/explicit) was newly introduced and showed that detecting implicit offense remains significantly more difficult than explicit offense. Most successful systems employed transformer-based architectures and transfer learning approaches.

## Conclusions

The GermEval 2019 shared task advanced research on German offensive language detection by expanding the dataset, improving topic diversity, and introducing the novel implicit vs. explicit classification task. The results demonstrate that while explicit offensive content detection has improved, implicit offense remains a significant challenge requiring more sophisticated understanding of context, sarcasm, and cultural references.

## Artifact Contributions

- GermEval 2019 dataset: German tweets annotated for offensive language (coarse and fine-grained)
- Implicit vs. explicit offense annotations
- Evaluation tool publicly available via shared task website: https://projects.fzai.h-da.de/iggsa/

## Data Description

The GermEval 2019 Shared Task dataset contains approximately 12,000 German tweets annotated for offensive language identification across three subtasks: coarse-grained binary classification (OFFENSE vs OTHER), fine-grained 4-way classification (ABUSE, INSULT, PROFANITY, OTHER), and implicit vs explicit offensive language classification. The 2019 data includes 7,025 newly collected tweets with 3,994 for training and 3,031 for testing, sampled from user timelines across different political orientations to reduce topic bias.


## Notes

