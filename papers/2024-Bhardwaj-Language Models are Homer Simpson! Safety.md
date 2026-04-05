---




































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: GBMWIP8Q
type: document
short_title: "Language Models are Homer Simpson! Safety"
year: 2024
first_author: "[[Rishabh Bhardwaj]]"
last_author: "[[Poria, Soujanya]]"
authors: "Bhardwaj, Rishabh; Do, Duc Anh; Poria, Soujanya"
url: "https://aclanthology.org/2024.acl-long.762/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/B6BW5928/2024 - Language Models are Homer Simpson! Safety Re-Alignment of Fine-tuned Language Models through Task Ar.pdf"
national_ethnic_cultural: "Multicultural/Cross-cultural"
cultures_nationalities_list: "Multicultural/Cross-cultural"
languages_list: "Chinese, English, Hindi, Vietnamese"
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
newtags: "Chinese, Indian, AI Safety & Alignment"
key_contribution: "Proposed RESTA (Restoring Safety through Task Arithmetic), a method to realign fine-tuned models by simply adding a 'safety vector' to their weights."
significance: "Demonstrates an efficient, scalable way to 'fix' safety after it has been compromised by downstream fine-tuning, likening the process to 'Homer Simpson' (clumsy but fixable) and offering a parameter-efficient alternative to full retraining."
tags: 
abstract: "Aligned language models face a significant limitation as their fine-tuning often results in compromised safety. To tackle this, we propose a simple method RESTA that performs LLM safety realignment. RESTA stands for REstoring Safety through Task Arithmetic. At its core, it involves a simple arithmetic addition of a safety vector to the weights of the compromised model. We demonstrate the effectiveness of RESTA in both parameter-efficient and full fine-tuning, covering a wide range of downstream..."
CONF-CC: "N/A"
DATE_ADDED: 20260208
LLM_assessed: Llama-2
DATA_URL: "https://github.com/declare-lab/resta"
pdf_extract: "PDF Extracts/2024/2024-Bhardwaj-Language Models are Homer Simpson! Safety.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2024/2024-Bhardwaj-Language Models are Homer Simpson! Safety.pdf]]"
CONFERENCE: "ACL 2024"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
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
author_country: "SG"
author_region: "Southeast Asia"
author_global_north_south: "Ambiguous"
weird_score: 57
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Multilingual benchmark for ai safety dataset"
data_metrics: "11 categories"
---
# Language Models are Homer Simpson! Safety Re-Alignment of Fine-tuned Language Models through Task Arithmetic

## Authors

[[Rishabh Bhardwaj|Bhardwaj, Rishabh]], [[Duc Anh Do|Do, Duc Anh]], [[Soujanya Poria|Poria, Soujanya]]

## Links

- **ACL Anthology:** https://aclanthology.org/2024.acl-long.762/

## Abstract

We propose RESTA to perform LLM realignment towards safety, which gets compromised due to downstream task fine-tuning. RESTA stands for REstoring Safety through Task Arithmetic. At its core, it involves a simple arithmetic addition of a safety vector to the weights of the compromised model. We demonstrate the effectiveness of RESTA in both parameter-efficient and full fine-tuning, covering a wide range of downstream tasks, including instruction following in Chinese, English, and Hindi, as well as problem-solving capabilities in Code and Math. We also showcase the generalizability of RESTA on three existing safety evaluation benchmarks and a multilingual benchmark dataset proposed as a part of this work, consisting of 550 harmful questions covering 11 categories, each with 5 sub-categories of harm. Overall, RESTA decreases the harmfulness of the compromised model from 18.6% to 5.1% and from 9.2% to 1.5% in parameter-efficient and full fine-tuning, respectively, while maintaining most of the model’s performance on the task. We release the source codes at: https://github.com/declare-lab/resta.

## Data Description

Introduces CATQA, a multilingual safety evaluation benchmark of 550 harmful questions across 11 categories in English, Chinese, and Vietnamese, used to evaluate the RESTA safety realignment method on Llama-2.


## Notes

