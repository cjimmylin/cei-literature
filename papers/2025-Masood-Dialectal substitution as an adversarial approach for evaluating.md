---




Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0727
type: journalArticle
short_title: "Dialectal substitution as an adversarial approach for evaluating Arabic NLP robustness"
year: 2025
first_author: "[[Adnan Masood]]"
last_author: "[[Ph Adnan Masood]]"
authors: "Adnan Masood, Ph"
url: "https://www.nature.com/articles/s41598-026-36252-4"
external_pdf: "https://www.nature.com/articles/s41598-026-36252-4_reference.pdf"
publication: Nature
pdf_extract: "PDF Extracts/2025/2025-Masood-Dialectal substitution as an adversarial approach for evaluating.md"
local_pdf: "[[PDFs/2025/2025-Masood-Dialectal substitution as an adversarial approach for evaluating.pdf]]"
DATE_ADDED: 20260213
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "Arabic"
cultures_nationalities_list: "Arabic"
languages_list: "Arabic, English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation methodology text corpus"
data_metrics: "Not specified"
LLM_assessed: "BERT, Qwen3, RoBERTa, XLNet"
DATA_URL: "https://github.com/elnagara/HARD-Arabic-Dataset"
tags: 
abstract: "Recent advances in deep neural networks (DNNs) have led to significant enhancements in Arabic natural language processing (NLP). However, their robustness remains insufficiently explored, particularly in adversarial settings. Most existing Arabic NLP systems are predominantly trained on Modern Standard Arabic (MSA), whereas real-world Arabic text frequently incorporates dialectal forms that diverge lexically and morphologically."
research_topic: "AI Safety & Alignment"
---
# Dialectal substitution as an adversarial approach for evaluating Arabic NLP robustness

## Authors

[[Ph Adnan Masood]]

## Metadata

**Authors:** Adnan Masood, Ph

**Year:** 2025

**Type:** journalArticle

**Venue:** Nature

**Languages:** Arabic, English

## Links

- **URL:** https://www.nature.com/articles/s41598-026-36252-4

## Abstract


Recent advances in deep neural networks (DNNs) have led to significant enhancements in Arabic natural language processing (NLP). However, their robustness remains insufficiently explored, particularly in adversarial settings. Most existing Arabic NLP systems are predominantly trained on Modern Standard Arabic (MSA), whereas real-world Arabic text frequently incorporates dialectal forms that diverge lexically and morphologically. To evaluate the impact of this distributional mismatch between training data and deployment conditions, this paper introduces dialectal substitution as a black-box token-level adversarial method against DNN-based MSA classification systems. Our approach identifies the most influential token in an input sequence via a scoring function and replaces it with a dialectally equivalent form using a fine-tuned Arabic dialectizer. The proposed attack demonstrates how dialectal substitutions can diminish the classification accuracy of the models, exposing vulnerabilities in DNN-based models trained on MSA corpora. We reveal a significant gap in current Arabic NLP systems, which fail to resist the diglossia nature of the Arabic language. We encourage researchers to pursue more robust and generalizable models that consider all forms of Arabic dialects.

## Data Description

Backfill summary: Models assessed include BERT, Qwen3, RoBERTa, XLNet. Verified dataset/resource link: https://github.com/elnagara/HARD-Arabic-Dataset.

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent C2, D3
**Relevance:** Relevant to Arabic

## Tags

