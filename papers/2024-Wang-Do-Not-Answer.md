---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: TNHI8F8M
type: document
short_title: Do-Not-Answer
year: 2024
first_author: "[[Yuxia Wang]]"
last_author: "[[Baldwin, Timothy]]"
authors: "Wang, Yuxia; Li, Haonan; Han, Xudong; Nakov, Preslav; Baldwin, Timothy"
url: "https://aclanthology.org/2024.findings-eacl.61/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/VZA7CY4P/2024 - Do-Not-Answer A Dataset for Evaluating Safeguards in LLMs.pdf"
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
newtags: "AI Safety & Alignment"
key_contribution: "Released Do-Not-Answer, an open-source dataset of 'dangerous capabilities' instructions for evaluating safeguards in LLMs."
significance: "Provides a public resource for safety evaluation, allowing open-source developers to test refusal mechanisms against harmful queries, democratizing red-teaming resources."
tags: 
abstract: "With the rapid evolution of large language models (LLMs), new and hard-to-predict harmful capabilities are emerging. This requires developers to identify potential risks through the evaluation of “dangerous capabilities” in order to responsibly deploy LLMs. Here we aim to facilitate this process. In particular, we collect an open-source dataset to evaluate the safeguards in LLMs, to facilitate the deployment of safer open-source LLMs at a low cost."
CONF-CC: N/A
DATE_ADDED: 20260208
LLM_assessed: "GPT-4, ChatGPT, Claude, Vicuna, Llama-2, ChatGLM"
DATA_URL: "https://github.com/Libr-AI/do-not-answer"
pdf_extract: "PDF Extracts/2024/2024-Wang-Do-Not-Answer.md"
local_pdf: "[[Lit-WS-PDFs/2024/2024-Wang-Do-Not-Answer.pdf]]"
CONFERENCE: "EACL 2024"
ethics_overall: 30
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 5
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "AI Safety & Alignment"
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
is_benchmark: No
is_eval: Yes
is_dataset: Yes
data_description: "Evaluation approach dataset"
data_metrics: "Not specified"
---
# Do-Not-Answer: A Dataset for Evaluating Safeguards in LLMs

## Authors

[[Yuxia Wang|Wang, Yuxia]], [[Haonan Li|Li, Haonan]], [[Xudong Han|Han, Xudong]], [[Preslav Nakov|Nakov, Preslav]], [[Timothy Baldwin|Baldwin, Timothy]]

## Links

- **ACL Anthology:** https://aclanthology.org/2024.findings-eacl.61/

## Abstract

With the rapid evolution of large language models (LLMs), new and hard-to-predict harmful capabilities are emerging. This requires developers to identify potential risks through the evaluation of “dangerous capabilities” in order to responsibly deploy LLMs. Here we aim to facilitate this process. In particular, we collect an open-source dataset to evaluate the safeguards in LLMs, to facilitate the deployment of safer open-source LLMs at a low cost. Our dataset is curated and filtered to consist only of instructions that responsible language models should not follow. We assess the responses of six popular LLMs to these instructions, and we find that simple BERT-style classifiers can achieve results that are comparable to GPT-4 on automatic safety evaluation. Our data and code are available at https://github.com/Libr-AI/do-not-answer

## Data Description

Do-Not-Answer: an open-source dataset of instructions that responsible LLMs should refuse to follow, used to evaluate safeguards in six LLMs. Also includes a BERT-style automatic safety classifier.


## Notes

