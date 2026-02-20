---








Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0218
type: conferencePaper
short_title: "Social (Measuring Social Norms of LLMs)"
year: 2024
first_author: "[[Ye Yuan]]"
last_author: "[[Chenguang Wang]]"
authors: "Ye Yuan, Kexin Tang, Jianhao Shen, Ming Zhang, Chenguang Wang"
url: "https://arxiv.org/abs/2404.02491"
external_pdf: "https://arxiv.org/pdf/2404.02491.pdf"
pdf_extract: "PDF Extracts/2024/2024-Yuan-Social Measuring Social Norms of LLMs.md"
local_pdf: "[[PDFs/2024/2024-Yuan-Social Measuring Social Norms of LLMs.pdf]]"
publication: "ACL 2024"
CONF-CC: "ACL 2024"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "We present a new challenge to examine whether large language models understand social norms. In contrast to existing datasets, our dataset requires a fundamental understanding of social norms to solve. Our dataset features the largest set of social norm skills, consisting of 402 skills and 12, 383 questions covering a wide set of social norms ranging from opinions and arguments to culture and laws. We design our dataset according to the K-12 curriculum."
LLM_assessed: "GPT-3.5, Llama-2, T5"
DATA_URL: "https://huggingface.co/datasets/socialnormdataset/social"
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Machine Learning"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark dataset"
data_metrics: "383 questions"
CONFERENCE: "ACL 2024"
---
# Social (Measuring Social Norms of LLMs)

## Authors

[[Ye Yuan]], [[Kexin Tang]], [[Jocelyn Shen|Jianhao Shen]], [[Ming Zhang]], [[Chenguang Wang]]

## Metadata

**Authors:** Ye Yuan, Kexin Tang, Jianhao Shen, Ming Zhang, Chenguang Wang

**Year:** 2024

**Type:** conferencePaper

**Venue:** ACL 2024

## Links

- **arXiv:** https://arxiv.org/abs/2404.02491
- **Code/Data:** https://github.com/socialnormdataset/socialagent; https://huggingface.co/datasets/socialnormdataset/social

## Abstract

We present a new challenge to examine whether large language models understand social norms. In contrast to existing datasets, our dataset requires a fundamental understanding of social norms to solve. Our dataset features the largest set of social norm skills, consisting of 402 skills and 12, 383 questions covering a wide set of social norms ranging from opinions and arguments to culture and laws. We design our dataset according to the K-12 curriculum. This enables the direct comparison of the social understanding of large language models to humans, more specifically, elementary students. While prior work generates nearly random accuracy on our benchmark, recent large language models such as GPT3.5-Turbo and LLaMA2-Chat are able to improve the performance significantly, only slightly below human performance. We then propose a multi-agent framework based on large language models to improve the models’ ability to understand social norms. This method further improves large language models to be on par with humans. Given the increasing adoption of large language models in real-world applications, our finding is particularly important and presents a unique direction for future improvements.

## Dataset Information

12,383 questions covering 402 social norm skills; multiple-choice format aligned with K-12 educational standards

## Data Description

The Social benchmark is a large-scale dataset for examining LLMs' understanding of fundamental social norms, consisting of 12,383 multi-choice questions across 402 skills spanning social studies and language arts, designed following the K-12 curriculum. Models tested include GPT3.5-Turbo, LLaMA2-Chat (70B, 13B, 7B variants), and UnifiedQA (T5-based), with a proposed multi-agent framework called SocialAgent that improves LLM performance to be on par with elementary student benchmarks.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 17
**Implementation Readiness:** HIGH

## Tags

