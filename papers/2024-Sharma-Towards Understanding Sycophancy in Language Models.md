---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0224
type: conferencePaper
short_title: "Towards Understanding Sycophancy in Language Models"
year: 2024
first_author: "[[Sharma, Mrinank]]"
last_author: "[[Perez, Ethan]]"
authors: "Sharma, Mrinank; Tong, Meg; Korbak, Tomasz; Duvenaud, David; Askell, Amanda; Samuel R. Bowman; Cheng, Newton; Durmus, Esin; Hatfield-Dodds, Zac; Scott R. Johnston; Kravec, Shauna; Maxwell, Timothy; McCandlish, Sam; Ndousse, Kamal; Rausch, Oliver; Schiefer, Nicholas; Yan, Da; Zhang, Miranda; Perez, Ethan"
authors_incomplete: false
url: "https://arxiv.org/abs/2310.13548"
external_pdf: "https://arxiv.org/pdf/2310.13548.pdf"
pdf_extract: "PDF Extracts/2024/2024-Sharma-Towards Understanding Sycophancy in Language Models.md"
local_pdf: "[[Lit-WS-PDFs/2024/2024-Sharma-Towards Understanding Sycophancy in Language Models.pdf]]"
publication: "ICLR 2024"
CONF-CC: "ICLR 2024"
DATE_ADDED: 20260207
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: English
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
newtags: 
tags: 
abstract: "Human feedback is commonly utilized to finetune AI assistants. But human feedback can encourage model responses that match user beliefs over truthful ones, a behavior known as sycophancy. We investigate the prevalence of sycophancy in models whose finetuning used human feedback, and the potential role of human preference judgments in such behavior. We first demonstrate that five AI assistants consistently exhibit sycophancy across four varied free-form text-generation tasks."
LLM_assessed: "Claude, GPT-3.5, GPT-4, Llama-2"
DATA_URL: "https://github.com/meg-tong/sycophancy-eval"
CONFERENCE: "ICLR 2024"
eleutherai: incorporated
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "Truthfulness & Factuality"
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
is_eval: No
is_dataset: No
data_description: N/A
data_metrics: "Not specified"
---
# Towards Understanding Sycophancy in Language Models

## Authors

[[Sharma, Mrinank]], [[Tong, Meg]], [[Tomasz Korbak|Korbak, Tomasz]], [[Duvenaud, David]], [[Askell, Amanda]], [[Bowman, Samuel R]], [[Cheng, Newton]], [[Durmus, Esin]], [[Hatfield-Dodds, Zac]], [[Johnston, Scott R]], [[Shauna Kravec|Kravec, Shauna]], [[Maxwell, Timothy]], [[McCandlish, Sam]], [[Kamal Ndousse|Ndousse, Kamal]], [[Rausch, Oliver]], [[Schiefer, Nicholas]], [[Yan, Da]], [[Zhang, Miranda]], [[Ethan Perez|Perez, Ethan]]

## Metadata

**Authors:** Sharma, Mrinank; Tong, Meg; Korbak, Tomasz; Duvenaud, David; Askell, Amanda; Bowman, Samuel R.; Cheng, Newton; Durmus, Esin; Hatfield-Dodds, Zac; Johnston, Scott R.; Kravec, Shauna; Maxwell, Timothy; McCandlish, Sam; Ndousse, Kamal; Rausch, Oliver; Schiefer, Nicholas; Yan, Da; Zhang, Miranda; Perez, Ethan

**Year:** 2024

**Type:** conferencePaper

**Venue:** ICLR 2024

## Links

- **arXiv:** https://arxiv.org/abs/2310.13548
- **Code/Data:** https://github.com/meg-tong/sycophancy-eval

## Abstract

Human feedback is commonly utilized to finetune AI assistants. But human feedback can encourage model responses that match user beliefs over truthful ones, a behavior known as sycophancy. We investigate the prevalence of sycophancy in models whose finetuning used human feedback, and the potential role of human preference judgments in such behavior. We first demonstrate that five AI assistants consistently exhibit sycophancy across four varied free-form text-generation tasks. To understand if human preferences drive this broadly observed behavior, we analyze existing human preference data. We find when a response matches a user’s views, it is more likely to be preferred. Moreover, both humans and preference models (PMs) prefer convincingly-written sycophantic responses over correct ones a non-negligible fraction of the time. Optimizing model outputs against PMs also sometimes sacrifices truthfulness in favor of sycophancy. Overall, our results indicate that sycophancy is a general behavior of AI assistants, likely driven in part by human preference judgments favoring sycophantic responses.

## Dataset Information

Three evaluation tasks in JSONL format:

## Data Description

SycophancyEval: a set of evaluation datasets and code for measuring sycophancy across four free-form text generation tasks (feedback on math, arguments, poetry; answering QA under challenge), released alongside this paper.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 17
**Implementation Readiness:** HIGH

## Tags

