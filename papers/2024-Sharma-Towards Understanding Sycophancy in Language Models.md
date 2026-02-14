---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0224
type: conferencePaper
short_title: "Towards Understanding Sycophancy in Language Models"
year: 2025
first_author: "[[Sharma, Mrinank]]"
last_author: "[[Perez, Ethan]]"
authors: "[[Sharma, Mrinank]]; [[Tong, Meg]]; [[Korbak, Tomasz]]; [[Duvenaud, David]]; [[Askell, Amanda]]; [[Bowman, Samuel R.]]; [[Cheng, Newton]]; [[Durmus, Esin]]; [[Hatfield-Dodds, Zac]]; [[Johnston, Scott R.]]; [[Kravec, Shauna]]; [[Maxwell, Timothy]]; [[McCandlish, Sam]]; [[Ndousse, Kamal]]; [[Rausch, Oliver]]; [[Schiefer, Nicholas]]; [[Yan, Da]]; [[Zhang, Miranda]]; [[Perez, Ethan]]"
authors_incomplete: false
url: "https://arxiv.org/abs/2310.13548"
external_pdf: "https://arxiv.org/pdf/2310.13548.pdf"
pdf_extract: "PDF Extracts/2024/2024-Sharma-Towards Understanding Sycophancy in Language Models.md"
local_pdf: "[[PDFs/2024/2024-Sharma-Towards Understanding Sycophancy in Language Models.pdf]]"
publication: "ICLR 2024"
DATE_ADDED: 20260207
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
national_ethnic_cultural: N/A
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: 
is_benchmark: No
is_eval: No
is_dataset: No
tags: 
abstract: "Human feedback is commonly utilized to finetune AI assistants. But human feedback can encourage model responses that match user beliefs over truthful ones, a behavior known as sycophancy. We investigate the prevalence of sycophancy in models whose finetuning used human feedback, and the potential role of human preference judgments in such behavior. We first demonstrate that five AI assistants consistently exhibit sycophancy across four varied free-form text-generation tasks."
research_topic: "Truthfulness & Factuality"
data_description: N/A
data_metrics: "Not specified"
LLM_assessed: "Claude, GPT-3.5, GPT-4, Llama-2"
DATA_URL: "https://github.com/meg-tong/sycophancy-eval"
---
# Towards Understanding Sycophancy in Language Models

## Authors

[[Sharma, Mrinank]], [[Tong, Meg]], [[Korbak, Tomasz]], [[Duvenaud, David]], [[Askell, Amanda]], [[Bowman, Samuel R.]], [[Cheng, Newton]], [[Durmus, Esin]], [[Hatfield-Dodds, Zac]], [[Johnston, Scott R.]], [[Kravec, Shauna]], [[Maxwell, Timothy]], [[McCandlish, Sam]], [[Ndousse, Kamal]], [[Rausch, Oliver]], [[Schiefer, Nicholas]], [[Yan, Da]], [[Zhang, Miranda]], [[Perez, Ethan]]

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

The study uses SycophancyEval, a set of evaluation datasets measuring sycophancy across four free-form text-generation tasks: feedback sycophancy (across math, arguments, poetry), answer sycophancy (TruthfulQA, TriviaQA), challenge sycophancy (MMLU, MATH, AQuA, TruthfulQA, TriviaQA), and mimicry sycophancy (15 famous poems with incorrect attributions). Additionally, the study analyzes 15K pairs from Anthropic's hh-rlhf helpfulness dataset using GPT-4-generated interpretable features.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 17
**Implementation Readiness:** HIGH

## Tags

