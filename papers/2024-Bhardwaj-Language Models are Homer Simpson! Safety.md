---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: GBMWIP8Q
type: document
short_title: "Language Models are Homer Simpson! Safety"
year: 2025
first_author: "[[Rishabh Bhardwaj]]"
authors: "[[Bhardwaj, Rishabh]]; [[Do, Duc Anh]]; [[Poria, Soujanya]]"
url: "https://aclanthology.org/2024.acl-long.762/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/B6BW5928/2024 - Language Models are Homer Simpson! Safety Re-Alignment of Fine-tuned Language Models through Task Ar.pdf"
national_ethnic_cultural: "Chinese, Indian"
religious_values: N/A
moral_psychology: N/A
newtags: "Chinese, Indian, AI Safety & Alignment"
key_contribution: "Proposed RESTA (Restoring Safety through Task Arithmetic), a method to realign fine-tuned models by simply adding a 'safety vector' to their weights."
significance: "Demonstrates an efficient, scalable way to 'fix' safety after it has been compromised by downstream fine-tuning, likening the process to 'Homer Simpson' (clumsy but fixable) and offering a parameter-efficient alternative to full retraining."
tags: 
abstract: "We propose RESTA to perform LLM realignment towards safety, which gets compromised due to downstream task fine-tuning. RESTA stands for REstoring Safety through Task Arithmetic. At its core, it involves a simple arithmetic addition of a safety vector to the weights of the compromised model. We demonstrate the effectiveness of RESTA in both parameter-efficient and full fine-tuning, covering a wide range of downstream tasks, including instruction following in Chinese, English, and Hindi, as well as problem-solving capabilities in Code and Math. We also showcase the generalizability of RESTA on three existing safety evaluation benchmarks and a multilingual benchmark dataset proposed as a part of this work, consisting of 550 harmful questions covering 11 categories, each with 5 sub-categories of harm. Overall, RESTA decreases the harmfulness of the compromised model from 18.6% to 5.1% and from 9.2% to 1.5% in parameter-efficient and full fine-tuning, respectively, while maintaining most of the model’s performance on the task. We release the source codes at: https://github.com/declare-lab/resta."
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "AI Safety & Alignment"
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Multilingual benchmark for ai safety dataset"
data_metrics: "11 categories"
pdf_extract: "PDF Extracts/2024/2024-Bhardwaj-Language Models are Homer Simpson! Safety.md"
local_pdf: "[[PDFs/2024/2024-Bhardwaj-Language Models are Homer Simpson! Safety.pdf]]"
---
# Language Models are Homer Simpson! Safety Re-Alignment of Fine-tuned Language Models through Task Arithmetic

## Authors

[[Rishabh Bhardwaj]], [[Duc Anh Do]], [[Soujanya Poria]]
## Metadata

**Year:** 2024

**Type:** document

## Links

- **ACL Anthology:** https://aclanthology.org/2024.acl-long.762/

## Abstract

We propose RESTA to perform LLM realignment towards safety, which gets compromised due to downstream task fine-tuning. RESTA stands for REstoring Safety through Task Arithmetic. At its core, it involves a simple arithmetic addition of a safety vector to the weights of the compromised model. We demonstrate the effectiveness of RESTA in both parameter-efficient and full fine-tuning, covering a wide range of downstream tasks, including instruction following in Chinese, English, and Hindi, as well as problem-solving capabilities in Code and Math. We also showcase the generalizability of RESTA on three existing safety evaluation benchmarks and a multilingual benchmark dataset proposed as a part of this work, consisting of 550 harmful questions covering 11 categories, each with 5 sub-categories of harm. Overall, RESTA decreases the harmfulness of the compromised model from 18.6% to 5.1% and from 9.2% to 1.5% in parameter-efficient and full fine-tuning, respectively, while maintaining most of the model’s performance on the task. We release the source codes at: https://github.com/declare-lab/resta.

## Notes

