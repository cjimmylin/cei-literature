---





































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: F5F25757
type: conferencePaper
short_title: "GermEval 2019 Task 2"
year: 2019
first_author: "[[Sven Kreutz]]"
last_author: "[[Hendrik Klawitter]]"
authors: "Sven Kreutz; Hendrik Klawitter"
url: "https://germevalmp2023.github.io/data/"
pdf_extract: "PDF Extracts/2019/2019-Kreutz-GermEval 2019 Task 2.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2019/2019-Kreutz-GermEval 2019 Task 2.pdf]]"
national_ethnic_cultural: "German"
cultures_nationalities_list: "German"
languages_list: "German"
religious_values: "N/A"
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
newtags: "German, Toxicity & Hate Speech"
key_contribution: "A shared task dataset for identifying offensive language in *German*."
significance: "Benchmark resource for German hate speech detection."
tags: 
abstract: "This paper presents an overview of the second edition of the GermEval Shared Task on the Identification of Offensive Language, dealing with the classification of German tweets from Twitter. Two subtasks were continued from the first edition, namely a coarse-grained binary classification task and a fine-grained multi-class classification task. As a novel subtask, the classification of offensive tweets as explicit or implicit was introduced. The shared task had 13 participating groups submitting runs across the three subtasks."
CONF-CC: "N/A"
DATE_ADDED: 20260129
LLM_assessed: NA
DATA_URL: "NA"
CONFERENCE: "Other Conference"
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "N/A"
data_metrics: "Not specified"
ethics_perspective: "Toxicity & Hate Speech"
---
# GermEval 2019 Task 2: Offensive Language Identification (Data Page)

## Metadata

**Authors:** Kreutz, Sven; Klawitter, Hendrik

**Year:** 2019

**Type:** conferencePaper

## Links

- **URL:** https://germevalmp2023.github.io/data/

## Abstract

This paper presents an overview of the second edition of the GermEval Shared Task on the Identification of Offensive Language, dealing with the classification of German tweets from Twitter. Two subtasks were continued from the first edition, namely a coarse-grained binary classification task and a fine-grained multi-class classification task. As a novel subtask, the classification of offensive tweets as explicit or implicit was introduced. The shared task had 13 participating groups submitting runs across the three subtasks.

## Authors

[[Sven Kreutz]], [[Hendrik Klawitter]]

## Detailed Summary

This paper presents the second edition of the GermEval Shared Task on the Identification of Offensive Language in German tweets. The task continues two subtasks from the first edition - a coarse-grained binary classification (OFFENSE vs OTHER) and a fine-grained multi-class classification (ABUSE, INSULT, PROFANITY, OTHER) - while introducing a novel third subtask distinguishing between explicit and implicit offensive language. Implicit offensive content, which requires contextual inference and includes figurative language like irony, sarcasm, or wordplay, represents a particularly challenging aspect of hate speech detection.

The shared task attracted 13 participating groups who submitted 28 runs for both the coarse-grained and fine-grained tasks, and 17 runs for the implicit-explicit classification. The dataset comprises German tweets manually annotated with moderate inter-annotator agreement (kappa = 0.59). BERT-based systems, particularly those pre-trained on German tweets, achieved the best results across all subtasks, with the UPB team achieving top F-scores of 76.95 for coarse-grained and 53.59 for fine-grained classification. Traditional classifiers like SVMs remained competitive within 1% of top neural systems.

The paper highlights that offensive language detection remains "far from solved," with the implicit class proving especially challenging (best F-score of only 53.93 for implicit detection). The distinction between ABUSE (degradation based on group membership or dehumanization) and INSULT (intent to offend with negative qualities) requires nuanced understanding that current systems struggle to achieve. The shared task provides a valuable resource for advancing German hate speech detection research and demonstrates the importance of distinguishing explicit from implicit forms of offensive content.

## Paper Outline

1. Introduction - Background on shared task and its importance
2. Task Description
   - Subtask 1: Coarse-grained Binary Classification (OFFENSE vs OTHER)
   - Subtask 2: Fine-grained 4-way Classification (ABUSE, INSULT, PROFANITY, OTHER)
   - Subtask 3: Implicit vs. Explicit Classification
3. Dataset
   - Data collection from Twitter
   - Annotation process and guidelines
   - Inter-annotator agreement analysis
4. Participating Systems Overview
5. Results
   - Coarse-grained task results
   - Fine-grained task results
   - Implicit/Explicit task results
6. Analysis and Discussion
7. Conclusion

## Methods Summary

The shared task methodology includes: (1) Data collection: 7,025 new German tweets manually annotated for 2019, combined with 2018 data for approximately 12,000 total tweets; (2) Annotation scheme with three classification levels - binary (OFFENSE/OTHER), fine-grained (ABUSE/INSULT/PROFANITY/OTHER), and implicit/explicit distinction; (3) Category definitions: PROFANITY for non-targeting profane language, INSULT for targeted offense ascribing negative qualities, ABUSE for degradation based on group membership or dehumanization; (4) Train/test split of 3,994/3,031 tweets for evaluation; (5) Multiple annotators with measured inter-annotator agreement (kappa = 0.59); (6) Evaluation using F-score metrics across participating systems.

## Results Summary

Key results across the 13 participating teams: (1) Coarse-grained task: Best F-score of 76.95 achieved by UPB team using BERT models; (2) Fine-grained task: Best F-score of 53.59 by UPB team, showing significant drop in difficulty; (3) Implicit/Explicit task: Best F-score of 73.11 by hpiDEDIS team overall, but best F-score for IMPLICIT class specifically was 53.93; (4) BERT-based systems (especially German tweet pre-trained) consistently outperformed other approaches; (5) Traditional SVM classifiers remained competitive, within 1% of top neural systems in some cases; (6) The ABUSE category proved hardest to distinguish from INSULT in fine-grained classification; (7) Inter-annotator agreement of kappa = 0.59 indicates moderate agreement, reflecting inherent ambiguity in offensive language classification.

## Conclusions

The shared task demonstrates that offensive language detection in German, particularly implicit forms, remains a challenging open problem. BERT-based models show promise but do not fully solve the task, with best coarse-grained F-scores below 80% and implicit detection below 54%. The paper establishes that: (1) Pre-training on domain-specific data (German tweets) improves performance; (2) Fine-grained distinctions between abuse types are more difficult than binary classification; (3) Implicit offensive content requiring pragmatic inference is substantially harder to detect than explicit content; (4) The problem requires continued research and improved datasets. The shared task provides benchmarks and resources for the research community to advance German hate speech detection.

## Artifact Contributions

- GermEval 2019 Task 2 dataset: ~12,000 annotated German tweets
- 2019 training set: 3,994 tweets
- 2019 test set: 3,031 tweets
- Annotation guidelines for three-level classification
- Benchmark results from 13 participating systems
- Novel implicit vs. explicit classification subtask and annotations

## Data Description

GermEval 2019 Task 2 dataset of ~12,000 German tweets annotated for offensive language across three subtasks: coarse-grained binary, fine-grained 4-class, and implicit vs. explicit classification.


## Notes

