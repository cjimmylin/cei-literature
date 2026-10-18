---
key: HELM0003
type: conferencePaper
short_title: "Nuanced Metrics for Measuring Unintended Bias"
year: 2019
first_author: "[[Daniel Borkan]]"
last_author: "[[Lucy Vasserman]]"
authors: "Daniel Borkan; Lucas Dixon; Jeffrey Sorensen; Nithum Thain; Lucy Vasserman"
doi: 10.1145/3308560.3317593
url: "https://doi.org/10.1145/3308560.3317593"
external_pdf: "https://arxiv.org/pdf/1903.04561.pdf"
publication: "WWW 2019"
CONF-CC: "WWW 2019"
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: English
religious_values: N/A
rv_islam: 5
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
newtags: "bias metrics, fairness evaluation, unintended bias, text classification, demographic bias, AUC, toxicity detection, identity groups, threshold-agnostic, evaluation dataset"
key_contribution: "Introduces a suite of five threshold-agnostic AUC-based metrics for measuring unintended demographic bias in text classifiers, paired with a large crowd-sourced dataset of online comments annotated for identity references."
significance: "Provides the field with robust, threshold-independent tools for auditing ML models for identity-based bias, directly enabling reproducible fairness evaluation in toxicity detection systems."
tags: []
pdf_extract: "PDF Extracts/2019/2019-Borkan-Nuanced Metrics for Measuring Unintended Bias.md"
abstract: "Unintended bias in Machine Learning can manifest as systemic differences in performance for different demographic groups, potentially compounding existing challenges to fairness in society at large. In this paper, we introduce a suite of threshold-agnostic metrics that provide a nuanced view of this unintended bias, by considering the various ways that a classifier's score distribution can vary across designated groups. We also introduce a large new test set of online comments with crowd-sourced annotations for identity references. We use this to show how our metrics can be used to find new and potentially subtle unintended bias in existing public models."
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2019/2019-Borkan-Nuanced Metrics for Measuring Unintended Bias.pdf]]"
DATE_ADDED: 20260312
helm: incorporated
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 5
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
is_benchmark: Unknown
is_eval: Unknown
is_dataset: Unknown
data_description: Unknown
data_metrics: Unknown
---



## Data Description

A large test set of online comments with crowd-sourced identity annotations for measuring unintended demographic bias in text classifiers, paired with a suite of threshold-agnostic bias metrics.
