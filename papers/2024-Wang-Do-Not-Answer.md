---




Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: TNHI8F8M
type: document
short_title: Do-Not-Answer
year: 2025
first_author: "[[Yuxia Wang]]"
last_author: "[[Baldwin, Timothy]]"
authors: "[[Wang, Yuxia]]; [[Li, Haonan]]; [[Han, Xudong]]; [[Nakov, Preslav]]; [[Baldwin, Timothy]]"
url: "https://aclanthology.org/2024.findings-eacl.61/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/VZA7CY4P/2024 - Do-Not-Answer A Dataset for Evaluating Safeguards in LLMs.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "AI Safety & Alignment"
key_contribution: "Released Do-Not-Answer, an open-source dataset of 'dangerous capabilities' instructions for evaluating safeguards in LLMs."
significance: "Provides a public resource for safety evaluation, allowing open-source developers to test refusal mechanisms against harmful queries, democratizing red-teaming resources."
tags: 
abstract: "With the rapid evolution of large language models (LLMs), new and hard-to-predict harmful capabilities are emerging. This requires developers to identify potential risks through the evaluation of “dangerous capabilities” in order to responsibly deploy LLMs. Here we aim to facilitate this process. In particular, we collect an open-source dataset to evaluate the safeguards in LLMs, to facilitate the deployment of safer open-source LLMs at a low cost."
DATE_ADDED: 20260208
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation approach dataset"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, ChatGPT, Claude, Vicuna, Llama-2, BERT"
DATA_URL: "https://github.com/Libr-AI/do-not-answer"
pdf_extract: "PDF Extracts/2024/2024-Wang-Do-Not-Answer.md"
local_pdf: [[PDFs/2024/2024-Wang-Do-Not-Answer.pdf]]
---
# Do-Not-Answer: A Dataset for Evaluating Safeguards in LLMs

## Authors

[[Yuxia Wang|Wang, Yuxia]], [[Haonan Li|Li, Haonan]], [[Xudong Han|Han, Xudong]], [[Preslav Nakov|Nakov, Preslav]], [[Timothy Baldwin|Baldwin, Timothy]]

## Links

- **ACL Anthology:** https://aclanthology.org/2024.findings-eacl.61/

## Abstract

With the rapid evolution of large language models (LLMs), new and hard-to-predict harmful capabilities are emerging. This requires developers to identify potential risks through the evaluation of “dangerous capabilities” in order to responsibly deploy LLMs. Here we aim to facilitate this process. In particular, we collect an open-source dataset to evaluate the safeguards in LLMs, to facilitate the deployment of safer open-source LLMs at a low cost. Our dataset is curated and filtered to consist only of instructions that responsible language models should not follow. We assess the responses of six popular LLMs to these instructions, and we find that simple BERT-style classifiers can achieve results that are comparable to GPT-4 on automatic safety evaluation. Our data and code are available at https://github.com/Libr-AI/do-not-answer

## Data Description

Do-Not-Answer is an open-source dataset for evaluating safeguards in LLMs, consisting of 939 risky prompts curated and filtered to include only instructions that responsible language models should not follow. The dataset covers a three-level hierarchical risk taxonomy with 5 top-level risk areas, 12 harm types, and 61 specific risk types. It includes 5,634 responses from six LLMs with manual harmfulness annotations and six-category response pattern labels.


## Notes

