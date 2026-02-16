---






Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: UPAVQJBQ
type: document
short_title: "'I'm sorry to hear that'"
year: 2022
first_author: "[[Minda Hu]]"
last_author: "[[King, Irwin]]"
authors: "[[Hu, Minda]]; [[Li, Muzhi]]; [[Wang, Yasheng]]; [[King, Irwin]]"
url: "https://aclanthology.org/2022.emnlp-main.291/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/FG497RSQ/2022 - 'I'm sorry to hear that' Finding New Biases in Language Models with a Holistic Descriptor Dataset.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "Existing pre-training methods for extractive Question Answering (QA) generate cloze-like queries different from natural questions in syntax structure, which could overfit pre-trained models to simple keyword matching. In order to address this problem, we propose a novel Momentum Contrastive pRe-training fOr queStion anSwering (MCROSS) method for extractive QA. Specifically, MCROSS introduces a momentum contrastive learning framework to align the answer probability between cloze-like and natural query-passage sample pairs. Hence, the pre-trained models can better transfer the knowledge learned in cloze-like samples to answering natural questions. Experimental results on three benchmarking QA datasets show that our method achieves noticeable improvement compared with all baselines in both supervised and zero-shot scenarios."
DATE_ADDED: 20260208
LLM_assessed: BERT
DATA_URL: "https://github.com/allenai/bi-att-flow"
pdf_extract: "PDF Extracts/2022/2022-Hu-'I'm sorry to hear that'.md"
local_pdf: "[[PDFs/2022/2022-Hu-“I’m sorry to hear that”.pdf]]"
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Question Answering"
is_benchmark: "Yes"
is_eval: "No"
is_dataset: "Yes"
data_description: "Benchmark dataset for question answering"
data_metrics: "Not specified"
---
# “I’m sorry to hear that”: Finding New Biases in Language Models with a Holistic Descriptor Dataset

## Authors

[[Minda Hu|Hu, Minda]], [[Muzhi Li|Li, Muzhi]], [[Yasheng Wang|Wang, Yasheng]], [[Irwin King|King, Irwin]]

## Links

- **ACL Anthology:** https://aclanthology.org/2022.emnlp-main.291/

## Abstract

Existing pre-training methods for extractive Question Answering (QA) generate cloze-like queries different from natural questions in syntax structure, which could overfit pre-trained models to simple keyword matching. In order to address this problem, we propose a novel Momentum Contrastive pRe-training fOr queStion anSwering (MCROSS) method for extractive QA. Specifically, MCROSS introduces a momentum contrastive learning framework to align the answer probability between cloze-like and natural query-passage sample pairs. Hence, the pre-trained models can better transfer the knowledge learned in cloze-like samples to answering natural questions. Experimental results on three benchmarking QA datasets show that our method achieves noticeable improvement compared with all baselines in both supervised and zero-shot scenarios.

## Data Description

The paper proposes MCROSS (Momentum Contrastive Pre-training for Question Answering), which uses a dual BERT-base encoder architecture with momentum contrastive learning. It is evaluated on three QA benchmarks: SQuAD v1.1 (in-domain), NewsQA, and TriviaQA (out-of-domain). T5 is used only as a question generator for data augmentation, not as the evaluated QA model.


## Notes

