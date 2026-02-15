---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: E5P5N9ZX
type: document
short_title: MARB
year: 2025
first_author: "[[Tom Södahl Bladsjö]]"
last_author: "[[Muñoz Sánchez, Ricardo]]"
authors: "[[Södahl Bladsjö, Tom]]; [[Muñoz Sánchez, Ricardo]]"
url: "https://aclanthology.org/2025.gebnlp-1.5/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/95P47V4W/2025 - MARB A Dataset for Studying the Social Dimensions of Reporting Bias in Language Models.pdf"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Bias & Fairness"
key_contribution: "Presented MARB, a dataset for studying 'reporting bias'—the tendency to over-report deviating attributes—as a lens for analyzing social biases (gender, etc.) in LMs."
significance: "Demonstrates that bias in LMs manifests not just as stereotypes but as 'reporting bias' (mentioning race/gender only when it's non-normative), offering a new diagnostic tool for subtle social exclusions."
tags: 
abstract: "Reporting bias is the tendency for speakers to omit unnecessary or obvious information while mentioning things they consider relevant or surprising. In descriptions of people, reporting bias can manifest as a tendency to over report on attributes that deviate from the norm. While social bias in language models has garnered a lot of attention in recent years, a majority of the existing work equates “bias” with “stereotypes”."
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation approach dataset"
data_metrics: "Not specified"
LLM_assessed: "BERT, RoBERTa, ALBERT, Mistral, Llama, Gemma"
DATA_URL: "https://github.com/TomBladsjo/MARB"
pdf_extract: "PDF Extracts/2025/2025-Södahl Bladsjö-MARB.md"
local_pdf: "[[PDFs/2025/2025-Södahl Bladsjö-MARB.pdf]]"
---
# MARB: A Dataset for Studying the Social Dimensions of Reporting Bias in Language Models

## Authors

[[Tom Södahl Bladsjö|Södahl Bladsjö, Tom]], [[Ricardo Muñoz Sánchez|Muñoz Sánchez, Ricardo]]

## Links

- **ACL Anthology:** https://aclanthology.org/2025.gebnlp-1.5/

## Abstract

Reporting bias is the tendency for speakers to omit unnecessary or obvious information while mentioning things they consider relevant or surprising. In descriptions of people, reporting bias can manifest as a tendency to over report on attributes that deviate from the norm. While social bias in language models has garnered a lot of attention in recent years, a majority of the existing work equates “bias” with “stereotypes”. We suggest reporting bias as an alternative lens through which to study how social attitudes manifest in language models. We present the MARB dataset, a diagnostic dataset for studying the interaction between social bias and reporting bias in language models. We use MARB to evaluate the off-the-shelf behavior of both masked and autoregressive language models and find signs of reporting bias with regards to marginalized identities, mirroring that which can be found in human text. This effect is particularly pronounced when taking gender into account, demonstrating the importance of considering intersectionality when studying social phenomena like biases.

## Data Description

The MARB (Marked Attribute and Reporting Bias) dataset is a diagnostic dataset for studying the interaction between social bias and reporting bias in language models. It consists of 28.5K sequence templates based on naturally occurring English text, populated with attribute descriptors across three categories: Race, Queerness, and Disability. Each template is paired with marked and unmarked versions to measure how language models handle socially marked attributes related to marginalized identities.


## Notes

