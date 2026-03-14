---








































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: J78A4GWD
type: conferencePaper
short_title: ToxiGen
year: 2022
first_author: "[[Thomas Hartvigsen]]"
last_author: "[[Ece Kamar]]"
authors: "Thomas Hartvigsen; Saadia Gabriel; Hamid Palangi; Maarten Sap; Dipankar Ray; Ece Kamar"
doi: 10.18653/v1/2022.acl-long.234
url: "https://aclanthology.org/2022.acl-long.234/"
external_pdf: "https://aclanthology.org/2022.acl-long.234.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
rv_islam: 20
rv_christianity: 0
rv_buddhism: 0
rv_judaism: 15
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
newtags: "Toxicity & Hate Speech"
key_contribution: "Created ToxiGen, a large-scale (274k) machine-generated dataset of toxic and benign statements about 13 minority groups, using adversarial prompting."
significance: "Addresses the scarcity of implicit toxicity data by using LMs to generate subtle hate speech, showing that finetuning on this synthetic data significantly improves detection of human-written implicit hate."
tags: 
abstract: "Toxic language detection systems often falsely ﬂag text that contains minority group mentions as toxic, as those groups are often the targets of online hate. Such over-reliance on spurious correlations also causes systems to struggle with detecting implicitly toxic language. To help mitigate these issues, we create TOXIGEN, a new large-scale and machinegenerated dataset of 274k toxic and benign statements about 13 minority groups."
pdf_extract: "PDF Extracts/2022/2022-Hartvigsen-ToxiGen.md"
local_pdf: "[[PDFs/2022/2022-Hartvigsen-ToxiGen.pdf]]"
CONF-CC: "ACL 2022"
DATE_ADDED: 20260208
LLM_assessed: "GPT-3, HateBERT, RoBERTa"
DATA_URL: "https://github.com/microsoft/ToxiGen"
CONFERENCE: "ACL 2022"
eleutherai: incorporated
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
is_benchmark: Yes
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation framework dataset for hate speech detection"
data_metrics: "Not specified"
ethics_perspective: "Toxicity & Hate Speech"
---
# ToxiGen: A Large-Scale Machine-Generated Dataset for Adversarial and Implicit Hate Speech Detection

## Metadata

**Authors:** Hartvigsen, Thomas; Gabriel, Saadia; Palangi, Hamid; Sap, Maarten; Ray, Dipankar; Kamar, Ece

**Year:** 2022

**Publication:** Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)

**Type:** conferencePaper

**DOI:** [10.18653/v1/2022.acl-long.234](https://doi.org/10.18653/v1/2022.acl-long.234)

**Pages:** 3309-3326

**Publisher:** Association for Computational Linguistics

## Links

- **ACL Anthology:** https://aclanthology.org/2022.acl-long.234
- **DOI:** https://doi.org/10.18653/v1/2022.acl-long.234

## Abstract

Toxic language detection systems often falsely flag text that contains minority group mentions as toxic, as those groups are often the targets of online hate. Such over-reliance on spurious correlations also causes systems to struggle with detecting implicitly toxic language. To help mitigate these issues, we create ToxiGen, a new large-scale and machine-generated dataset of 274k toxic and benign statements about 13 minority groups. We develop a demonstration-based prompting framework and an adversarial classifier-in-the-loop decoding method to generate subtly toxic and benign text with a massive pretrained language model. Controlling machine generation in this way allows ToxiGen to cover implicitly toxic text at a larger scale, and about more demographic groups, than previous resources of human-written text. We conduct a human evaluation on a challenging subset of ToxiGen and find that annotators struggle to distinguish machine-generated text from human-written language. We also find that 94.5% of toxic examples are labeled as hate speech by human annotators. Using three publicly-available datasets, we show that finetuning a toxicity classifier on our data improves its performance on human-written data substantially. We also demonstrate that ToxiGen can be used to fight machine-generated toxicity as finetuning improves the classifier significantly on our evaluation subset.

## Authors

[[Thomas Hartvigsen]], [[Saadia Gabriel]], [[Hamid Palangi]], [[Maarten Sap]], [[Dipankar Ray]], [[Ece Kamar]]

## Data Description

274k machine-generated toxic and benign statements about 13 minority groups for hate speech detection


## Notes


## Citation Info

94 citations (Crossref/DOI) [2025-08-23]
