---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 6EJBF544
type: document
short_title: "Unlearn Dataset Bias in Natural Language"
year: 2019
first_author: "[[He He]]"
last_author: "[[Wang, Haohan]]"
authors: "He, He; Zha, Sheng; Wang, Haohan"
url: "https://aclanthology.org/D19-6115/"
external_pdf: "https://aclanthology.org/D19-6115.pdf"
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
key_contribution: "Proposed DRiFt (Debiased Residual Fitting), a learning algorithm that removes known dataset biases (superficial cues) by fitting the residual of a 'biased' model."
significance: "Addresses the 'Clever Hans' effect in NLP, ensuring models learn robust semantic features rather than just memorizing spurious correlations (e.g., negation = contradiction) in training data."
tags: 
abstract: "Statistical natural language inference (NLI) models are susceptible to learning dataset bias: superﬁcial cues that happen to associate with the label on a particular dataset, but are not useful in general, e.g., negation words indicate contradiction. As exposed by several recent challenge datasets, these models perform poorly when such association is absent, e.g., predicting that “I love dogs.” contradicts “I don’t love cats.”."
pdf_extract: "PDF Extracts/2019/2019-He-Unlearn Dataset Bias in Natural Language.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2019/2019-He-Unlearn Dataset Bias in Natural Language.pdf]]"
CONF-CC: N/A
DATE_ADDED: 20260208
LLM_assessed: BERT
DATA_URL: NA
CONFERENCE: "Other Conference"
ethics_overall: 20
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
author_country: HK
author_region: "East Asia"
author_global_north_south: Ambiguous
weird_score: 53
is_benchmark: Yes
is_eval: No
is_dataset: Yes
data_description: "Benchmark for bias and fairness dataset"
data_metrics: "Not specified"
---
# Unlearn Dataset Bias in Natural Language Inference by Fitting the Residual

## Authors

[[He He|He, He]], [[Sheng Zha|Zha, Sheng]], [[Haohan Wang|Wang, Haohan]]

## Links

- **ACL Anthology:** https://aclanthology.org/D19-6115/

## Abstract

Statistical natural language inference (NLI) models are susceptible to learning dataset bias: superficial cues that happen to associate with the label on a particular dataset, but are not useful in general, e.g., negation words indicate contradiction. As exposed by several recent challenge datasets, these models perform poorly when such association is absent, e.g., predicting that “I love dogs.” contradicts “I don’t love cats.”. Our goal is to design learning algorithms that guard against known dataset bias. We formalize the concept of dataset bias under the framework of distribution shift and present a simple debiasing algorithm based on residual fitting, which we call DRiFt. We first learn a biased model that only uses features that are known to relate to dataset bias. Then, we train a debiased model that fits to the residual of the biased model, focusing on examples that cannot be predicted well by biased features only. We use DRiFt to train three high-performing NLI models on two benchmark datasets, SNLI and MNLI. Our debiased models achieve significant gains over baseline models on two challenge test sets, while maintaining reasonable performance on the original test sets.

## Data Description

The paper uses two benchmark NLI datasets, SNLI (549,367 training pairs) and MNLI (392,702 training pairs), along with the HANS challenge dataset and STRESS test sets, to evaluate the DRiFt debiasing algorithm for natural language inference models susceptible to dataset bias from crowdsourcing artifacts.


## Notes

