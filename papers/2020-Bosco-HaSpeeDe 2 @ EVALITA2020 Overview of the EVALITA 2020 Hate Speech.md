---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0508
type: conferencePaper
short_title: "HaSpeeDe 2 @ EVALITA2020: Overview of the EVALITA 2020 Hate Speech Detection Task"
year: 2020
first_author: "[[Manuela Sanguinetti]]"
last_author: "[[Russo, Irene]]"
authors: "Manuela Sanguinetti; Comandini, Gloria; Nuovo, Elisa Di; Frenda, Simona; Stranisci, M.; Cristina Bosco; Caselli, Tommaso; Viviana Patti; Russo, Irene"
authors_incomplete: false
url: "https://www.researchgate.net/publication/346997652_HaSpeeDe_2_EVALITA2020_Overview_of_the_EVALITA_2020_Hate_Speech_Detection_Task"
external_pdf: "https://books.openedition.org/aaccademia/pdf/6732"
publication: "EVALITA 2020"
CONF-CC: "EVALITA 2020"
pdf_extract: "PDF Extracts/2020/2020-Bosco-HaSpeeDe 2 @ EVALITA2020 Overview of the EVALITA 2020 Hate Speech.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2020/2020-Bosco-HaSpeeDe 2 @ EVALITA2020 Overview of the EVALITA 2020 Hate Speech.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: Italian
cultures_nationalities_list: Italian
languages_list: Italian
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
newtags: 
LLM_assessed: NA
DATA_URL: "https://github.com/msang/haspeede/tree/master/2020"
tags: 
abstract: "Welcome to EVALITA 2020! EVALITA is the evaluation campaign of Natural Language Processing and Speech Tools for Italian. EVALITA is an initiative of the Italian Association for Computational Linguistics (AILC, http://www.ai-lc.it) and it is endorsed by the Italian Association for Artificial Intelligence (AIxIA, http://www.aixia.it) and the Italian Association for Speech Sciences (AISV, http://www.aisv.it)."
CONFERENCE: "Other Conference"
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
author_country: FR
author_region: "Western Europe"
author_global_north_south: "Global North"
weird_score: 75
is_benchmark: No
is_eval: No
is_dataset: No
data_description: N/A
data_metrics: "Not specified"
---
# HaSpeeDe 2 @ EVALITA2020: Overview of the EVALITA 2020 Hate Speech Detection Task

## Authors

[[Sanguinetti, M]], [[Comandini, Gloria]], [[Nuovo, Elisa Di]], [[Frenda, Simona]], [[Stranisci, M]], [[Bosco, C]], [[Tommaso Caselli|Caselli, Tommaso]], [[Patti, V]], [[Russo, Irene]]

## Metadata

**Authors:** Sanguinetti, M.; Comandini, Gloria; Nuovo, Elisa Di; Frenda, Simona; Stranisci, M.; Bosco, C.; Caselli, Tommaso; Patti, V.; Russo, Irene

**Year:** 2020

**Type:** conferencePaper

**Venue:** EVALITA 2020

**Languages:** Italian

**Benchmark:** HaSpeeDe 2

## Links

- **URL:** https://www.researchgate.net/publication/346997652_HaSpeeDe_2_EVALITA2020_Overview_of_the_EVALITA_2020_Hate_Speech_Detection_Task
- **Code/Data:** https://github.com/msang/haspeede/tree/master/2020

## Abstract

Second edition shared task on detection of hateful content in Italian Twitter messages. Composed of main task (hate speech detection) and pilot tasks (stereotype detection, nominal utterance detection). 14 teams participated; best macro F1 of 0.8088.

## Summary

This paper presents HaSpeeDe 2, the second edition of the EVALITA shared task on hate speech detection in Italian Twitter messages and news headlines. The task includes a main hate speech detection track and two pilot tasks for stereotype detection and nominal utterance detection, with 14 participating teams employing various approaches including BERT-based models. The best-performing system achieved a macro F1 score of 0.8088, and the shared task provides cross-domain evaluation between Twitter and news domains to assess model robustness.

## Data Description

HaSpeeDe 2 dataset: 8,012 Italian tweets and 500 news headlines annotated for hate speech, stereotypes, and nominal utterances targeting immigrants, Muslims, and Roma.


## Detailed Summary

This paper presents HaSpeeDe 2, the second edition of the shared task on hate speech detection within the EVALITA 2020 evaluation campaign for Italian NLP. The task is part of the broader EVALITA proceedings (523 pages) covering multiple tracks including hate speech detection, automatic misogyny identification, stance detection, and other NLP tasks for the Italian language. HaSpeeDe 2 includes a main hate speech detection task on Italian Twitter messages and news headlines, along with pilot tasks for stereotype detection and nominal utterance detection. The shared task attracted 14 participating teams who employed various approaches, predominantly BERT-based transformer models including AlBERTo and XLM-RoBERTa.

The task provides cross-domain evaluation between Twitter and news headline domains to assess model robustness and generalization. The best-performing system achieved a macro F1 score of 0.8088. The proceedings also include detailed system descriptions from participating teams, covering approaches ranging from fine-tuned pre-trained language models to convolutional neural networks and ensemble methods. The shared task contributes to the growing body of Italian-language hate speech detection research and provides benchmark datasets and evaluation standards for the Italian NLP community.

## Paper Outline

1. EVALITA 2020 Overview - Seventh evaluation campaign for Italian NLP
2. Track: Affect, Hate, and Stance - AMI, HaSpeeDe 2, SardiStance tasks
3. HaSpeeDe 2 - Main hate speech detection task and pilot tasks
4. System Descriptions - 14 participating teams and their approaches
5. Additional Tracks - Other EVALITA 2020 evaluation tasks

## Methods Summary

The shared task follows a standard evaluation campaign format with provided training and test data for Italian hate speech detection. Participating teams employed diverse approaches including fine-tuned BERT-based models (AlBERTo, XLM-RoBERTa), convolutional neural networks, ensemble methods combining transformer architectures with transfer learning, and traditional classifiers enhanced with linguistic features. Cross-domain evaluation between Twitter and news headline datasets tests model generalization across text genres. The annotation scheme captures both hate speech presence and stereotype detection.

## Results Summary

The best-performing system achieved a macro F1 score of 0.8088 on the main hate speech detection task. Fourteen teams participated in the shared task, with transformer-based approaches (particularly BERT-based models) dominating the top results. The cross-domain evaluation revealed challenges in transferring hate speech detection capabilities between Twitter and news headline domains, highlighting the importance of domain-robust approaches. The stereotype detection pilot task provided initial baselines for this relatively unexplored dimension of Italian hate speech analysis.

## Conclusions

The shared task represents the continued maturation of Italian hate speech detection research, building on the first HaSpeeDe edition. The inclusion of cross-domain evaluation and pilot tasks for stereotype detection extends the scope beyond binary hate speech classification. Future editions are expected to incorporate additional annotation dimensions and larger, more diverse datasets for Italian hate speech evaluation.

## Artifact Contributions

- **HaSpeeDe 2 Dataset**: Italian hate speech detection dataset from Twitter and news headlines (https://github.com/msang/haspeede/tree/master/2020)

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B8
**Relevance:** Major Italian hate speech evaluation campaign with stereotype detection pilot task. Includes cross-domain evaluation (Twitter and news headlines).

## Tags

