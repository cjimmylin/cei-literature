---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0483
type: preprint
short_title: "Towards Fairness Assessment of Dutch Hate Speech Detection"
year: 2025
first_author: "[[Julie Bauer]]"
last_author: "[[Adriana Iamnitchi]]"
authors: "Julie Bauer; Rishabh Kaushal; Thales Bertaglia; Adriana Iamnitchi"
url: "https://arxiv.org/abs/2506.12502"
external_pdf: "https://arxiv.org/pdf/2506.12502.pdf"
publication: arXiv
CONF-CC: Preprint
pdf_extract: "PDF Extracts/2025/2025-Bauer-Towards Fairness Assessment of Dutch Hate Speech Detection.md"
local_pdf: "[[Lit-WS-PDFs/2025/2025-Bauer-Towards Fairness Assessment of Dutch Hate Speech Detection.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: Dutch
cultures_nationalities_list: Dutch
languages_list: Dutch
religious_values: Sikhism
rv_islam: 5
rv_christianity: 0
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 50
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 0
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: Sikhism
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
LLM_assessed: "BERT, GPT-2"
DATA_URL: "https://github.com/Juulba/Dutch-counterfactual-fairness"
tags: 
abstract: "Numerous studies have proposed computational methods to detect hate speech online, yet most focus on the English language and emphasize model development. In this study, we evaluate the counterfactual fairness of hate speech detection models in the Dutch language, specifically examining the performance and fairness of transformer-based models. We make the following key contributions. First, we curate a list of Dutch Social Group Terms that reflect social context."
authors_incomplete: false
CONFERENCE: Preprint
ethics_overall: 100
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
author_country: CA
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 84
is_benchmark: No
is_eval: Yes
is_dataset: No
data_description: "Evaluation approach"
data_metrics: "Not specified"
---
# Towards Fairness Assessment of Dutch Hate Speech Detection

## Authors

[[Julie Bauer]], [[Rishabh Kaushal]], [[Thales Bertaglia]], [[Adriana Iamnitchi]]

## Metadata

**Authors:** Julie Bauer, Rishabh Kaushal, Thales Bertaglia, Adriana Iamnitchi

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** Dutch

## Links

- **arXiv:** https://arxiv.org/abs/2506.12502

## Abstract

Evaluates counterfactual fairness of hate speech detection models in Dutch. Creates Dutch Social Group Terms list, generates counterfactual data using LLMs, and evaluates transformer models on fairness metrics (Counterfactual Token Fairness, equality of odds, demographic parity).

## Summary

This paper evaluates the counterfactual fairness of hate speech detection models in Dutch by developing a methodology that curates Dutch Social Group Terms reflecting social context, generates counterfactual data using LLMs, and measures fairness using Counterfactual Token Fairness (CTF), equality of odds, and demographic parity metrics. The study focuses specifically on transformer-based models (BERT, RoBERTa) and represents the first fairness assessment specifically tailored for Dutch hate speech detection. The counterfactual evaluation approach systematically tests whether models change predictions based solely on protected attributes rather than actual hate speech content.

## Data Description

Dutch Social Group Terms (SGT) list of 85 terms, plus counterfactual datasets generated via LLMdef (15,175 posts), LLMlist (21,562 posts), SLL (49,104 posts), and MGS (20,393 posts) methods; also includes Dutch counterfactual evaluation dataset of 2,890 template-based sentences.


## Detailed Summary

This paper presents the first comprehensive fairness assessment of hate speech detection models for the Dutch language, focusing on counterfactual fairness -- the principle that a model's decision should remain consistent if sensitive attributes (nationality, ethnicity, sexuality, religion) are changed while keeping all other content identical. The study makes four key contributions: (1) curation of a list of Dutch Social Group Terms reflecting social context, (2) generation of counterfactual data for Dutch using LLMs and established strategies including Manual Group Substitution (MGS) and Sentence Log-Likelihood (SLL), (3) fine-tuning of BERTje-based transformer models with counterfactual data, and (4) fairness evaluation using Counterfactual Token Fairness (CTF) and group fairness metrics (equality of odds, demographic parity). The qualitative evaluation highlights specific challenges in generating realistic counterfactual sentences that conform to Dutch grammar and contextual coherence. Results show that models fine-tuned with counterfactual data perform better in both hate speech detection accuracy and fairness metrics.

## Paper Outline

1. Introduction - Motivation for counterfactual fairness in Dutch hate speech detection
2. Related Work - Hate speech detection in Dutch; fairness and counterfactual evaluation methods
3. Methodology - Dutch Social Group Terms curation; counterfactual generation methods
4. Counterfactual Data Generation - LLM-based (LLMlist, LLMdef) and traditional (MGS, SLL) approaches
5. Model Fine-tuning - BERTje fine-tuning with counterfactual data
6. Evaluation - Performance metrics and fairness assessment
7. Results and Discussion
8. Conclusion

## Methods Summary

The methodology involves four main components. First, Dutch Social Group Terms are curated to reflect the Dutch social context across sensitive attributes. Second, four counterfactual data generation methods are compared: LLMlist (LLM with group term list), LLMdef (LLM with definitions), SLL (Sentence Log-Likelihood), and MGS (Manual Group Substitution). Third, BERTje models are fine-tuned with the generated counterfactual data. Fourth, models are evaluated on both detection performance and fairness using CTF metrics and group fairness measures (equality of odds, demographic parity). Template-based Dutch counterfactual test data is used for final fairness evaluation.

## Results Summary

Models fine-tuned with counterfactual data demonstrate improvements in hate speech detection performance, average counterfactual fairness, and group fairness metrics. The qualitative evaluation reveals challenges specific to Dutch counterfactual generation, including Dutch grammar rules and contextual coherence issues that make literal group substitution problematic. The study provides practical insights for improving both model performance and fairness in Dutch-language hate speech detection systems.

## Conclusions

The paper bridges a significant gap in counterfactual fairness research for non-English languages by providing the first systematic assessment for Dutch. The findings demonstrate that counterfactual data augmentation can improve both detection performance and fairness simultaneously, while highlighting the need for language-specific adaptations of fairness evaluation methods.

## Artifact Contributions

- **Resource:** Curated list of Dutch Social Group Terms for counterfactual fairness evaluation
- **Methodology:** Comparative framework for counterfactual data generation in Dutch (4 methods)
- **Evaluation Framework:** Fairness assessment pipeline using CTF, equality of odds, and demographic parity for Dutch hate speech detection

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** First fairness assessment specifically for Dutch hate speech detection using counterfactual evaluation methods.

## Tags

