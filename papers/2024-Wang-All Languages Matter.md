---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: KF3PX7GE
type: document
short_title: "All Languages Matter"
year: 2024
first_author: "[[Wenxuan Wang]]"
last_author: "[[Lyu, Michael]]"
authors: "Wang, Wenxuan; Tu, Zhaopeng; Chen, Chang; Yuan, Youliang; Huang, Jen-tse; Jiao, Wenxiang; Lyu, Michael"
url: "https://aclanthology.org/2024.findings-acl.349/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/SFH74GNU/2024 - All Languages Matter On the Multilingual Safety of Large Language Models.pdf"
national_ethnic_cultural: Multicultural/Cross-cultural
cultures_nationalities_list: Multicultural/Cross-cultural
languages_list: Multilingual
religious_values: Christianity
rv_islam: 0
rv_christianity: 50
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
religious_values_list: Christianity
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
key_contribution: "Built XSafety, a multilingual safety benchmark (10 languages, 14 issues), finding LLMs are much less safe in non-English languages."
significance: "Highlights the 'multilingual safety gap', showing that safety alignment often fails to transfer zero-shot to other languages, necessitating native safety data."
tags: 
abstract: "Ensuring safety is fundamental when developing and deploying large language models (LLMs). However, previous safety benchmarks only concern the safety in one language, e.g., the majority language in the pretraining data, such as English. In this work, we build the first multilingual safety benchmark for LLMs, XSAFETY, in response to the global deployment of LLMs in practice. XSAFETY covers 14 commonly used safety issues across ten languages spanning several language families."
CONF-CC: N/A
DATE_ADDED: 20260208
LLM_assessed: "ChatGPT, LLaMA, Llama-2, BLOOM, PaLM-2, Vicuna"
DATA_URL: "https://github.com/Jarviswang94/Multilingual_safety_benchmark"
pdf_extract: "PDF Extracts/2024/2024-Wang-All Languages Matter.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2024/2024-Wang-All Languages Matter.pdf]]"
CONFERENCE: "ACL 2024"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 5
utilitarian_ethics: 0
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
author_country: HK
author_region: "East Asia"
author_global_north_south: Ambiguous
weird_score: 53
is_benchmark: Yes
is_eval: No
is_dataset: No
data_description: "Multilingual benchmark for ai safety"
data_metrics: "10 languages"
---
# All Languages Matter: On the Multilingual Safety of Large Language Models

## Authors

[[Wenxuan Wang|Wang, Wenxuan]], [[Zhaopeng Tu|Tu, Zhaopeng]], [[Chang Chen|Chen, Chang]], [[Youliang Yuan|Yuan, Youliang]], [[Jen-tse Huang|Huang, Jen-tse]], [[Wenxiang Jiao|Jiao, Wenxiang]], [[Michael Lyu|Lyu, Michael]]

## Links

- **ACL Anthology:** https://aclanthology.org/2024.findings-acl.349/

## Abstract

Safety lies at the core of developing and deploying large language models (LLMs). However, previous safety benchmarks only concern the safety in one language, e.g. the majority language in the pretraining data such as English. In this work, we build the first multilingual safety benchmark for LLMs, XSafety, in response to the global deployment of LLMs in practice. XSafety covers 14 kinds of commonly used safety issues across 10 languages that span several language families. We utilize XSafety to empirically study the multilingual safety for 4 widely-used LLMs, including both close-API and open-source models. Experimental results show that all LLMs produce significantly more unsafe responses for non-English queries than English ones, indicating the necessity of developing safety alignment for non-English languages. In addition, we propose a simple and effective prompting method to improve the multilingual safety of ChatGPT by enhancing cross-lingual generalization of safety alignment. Our prompting method can significantly reduce the ratio of unsafe responses by 42% for non-English queries. We will release all the data and results to facilitate future research on LLMs’ safety.

## Data Description

XSafety: multilingual safety benchmark covering 14 safety issue types across 10 languages, used to evaluate four LLMs including ChatGPT, PaLM-2, LLaMA-2-Chat, and Vicuna.


## Notes

