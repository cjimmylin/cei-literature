---




































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 8F4KS6NP
type: document
short_title: KoSBI
year: 2023
first_author: "[[Hwaran Lee]]"
last_author: "[[Ha, Jung-woo]]"
authors: "Lee, Hwaran; Hong, Seokhee; Park, Joonsuk; Kim, Takyoung; Kim, Gunhee; Ha, Jung-woo"
url: "https://aclanthology.org/2023.acl-industry.21/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/QM5QX7X7/2023 - KoSBI A Dataset for Mitigating Social Bias Risks Towards Safer Large Language Model Applications.pdf"
national_ethnic_cultural: "Korean"
cultures_nationalities_list: "Korean"
languages_list: "Korean"
religious_values: "Judaism"
rv_islam: 0
rv_christianity: 0
rv_buddhism: 0
rv_judaism: 50
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
religious_values_list: "Judaism"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: "Korean, Bias & Fairness"
key_contribution: "Created KoSBI, a Korean social bias dataset (34k samples, 72 groups), finding that localized data reduces bias by ~16% in Korean LLMs."
significance: "Validates the 'localization hypothesis': you cannot just translate English safety data; you need native datasets to capture the specific biases (e.g., ageism, regionalism) relevant to a specific culture."
tags: 
abstract: "Large language models (LLMs) learn not only natural text generation abilities but also social biases against different demographic groups from real-world data. This poses a critical risk when deploying LLM-based applications. Existing research and resources are not readily applicable in South Korea due to the differences in language and culture, both of which significantly affect the biases and targeted demographic groups."
pdf: "http://arxiv.org/pdf/2305.17701"
pdf_extract: "PDF Extracts/2023/2023-Lee-KoSBI.md"
local_pdf: "[[PDFs/2023/2023-Lee-KoSBI.pdf]]"
CONF-CC: "N/A"
DATE_ADDED: 20260208
LLM_assessed: "GPT-3"
DATA_URL: "https://github.com/naver-ai/korean-safety-benchmarks"
CONFERENCE: "ACL 2023"
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
is_benchmark: "No"
is_eval: Yes
is_dataset: "Yes"
data_description: "Dataset"
data_metrics: "15 categories"
ethics_perspective: "Bias & Fairness"
---
# KoSBI: A Dataset for Mitigating Social Bias Risks Towards Safer Large Language Model Applications

## Authors

[[Hwaran Lee|Lee, Hwaran]], [[Seokhee Hong|Hong, Seokhee]], [[Joonsuk Park|Park, Joonsuk]], [[Takyoung Kim|Kim, Takyoung]], [[Gunhee Kim|Kim, Gunhee]], [[Ha, Jung-woo]]

## Links

- **ACL Anthology:** https://aclanthology.org/2023.acl-industry.21/

## Abstract

Large language models (LLMs) not only learn natural text generation abilities but also social biases against different demographic groups from real-world data. This poses a critical risk when deploying LLM-based applications. Existing research and resources are not readily applicable in South Korea due to the differences in language and culture, both of which significantly affect the biases and targeted demographic groups. This limitation requires localized social bias datasets to ensure the safe and effective deployment of LLMs. To this end, we present KosBi, a new social bias dataset of 34k pairs of contexts and sentences in Korean covering 72 demographic groups in 15 categories. We find that through filtering-based moderation, social biases in generated content can be reduced by 16.47%p on average for HyperClova (30B and 82B), and GPT-3.

## Data Description

KOSBI: 34K pairs of contexts and sentences covering 72 demographic groups in 15 categories for Korean social bias detection, with safe/unsafe labels.


## Notes

