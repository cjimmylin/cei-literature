---






































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0178
type: conferencePaper
short_title: "GenMO (Gender-bias in Morality Opinions)"
year: 2024
first_author: "[[Divij Bajaj]]"
last_author: "[[Ruihong Huang]]"
authors: Divij Bajaj; Yuanyuan Lei; Jonathan Tong; Ruihong Huang
doi: 10.18653/v1/2024.findings-emnlp.928
url: "https://doi.org/10.18653/v1/2024.findings-emnlp.928"
external_pdf: "https://aclanthology.org/2024.findings-emnlp.928.pdf"
pdf_extract: "PDF Extracts/2024/2024-Bajaj-GenMO Gender-bias in Morality Opinions.md"
local_pdf: "[[PDFs/2024/2024-Bajaj-GenMO Gender-bias in Morality Opinions.pdf]]"
publication: "EMNLP 2024"
CONF-CC: "EMNLP 2024"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
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
mp_mft: 50
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "Moral Foundations Theory"
newtags: 
tags: 
abstract: "Large Language Models (LLMs) have shown remarkable capabilities in a multitude of Natural Language Processing (NLP) tasks. However, these models are still not immune to limitations such as social biases, especially gender bias. This work investigates whether current closed and open-source LLMs possess gender bias, especially when asked to give moral opinions. To evaluate these models, we curate and introduce a new dataset GenMO (Genderbias in Morality Opinions) comprising parallel short stories..."
LLM_assessed: "GPT-3.5, GPT-4, Llama-3, Mistral, Claude-3 Sonnet, Claude-3 Opus"
DATA_URL: "https://github.com/divij30bajaj/GenMO"
CONFERENCE: "EMNLP 2024"
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation approach dataset"
data_metrics: "Not specified"
ethics_perspective: "Bias & Fairness"
---
# GenMO (Gender-bias in Morality Opinions)

## Authors

[[Divij Bajaj]], [[Yuanyuan Lei]], [[Jonathan Tong]], [[Ruihong Huang]]

## Metadata

**Authors:** Divij Bajaj, Yuanyuan Lei, Jonathan Tong, Ruihong Huang

**Year:** 2024

**Type:** conferencePaper

**Venue:** EMNLP 2024

**DOI:** [10.18653/v1/2024.findings-emnlp.928](https://doi.org/10.18653/v1/2024.findings-emnlp.928)

## Links

- **DOI:** https://doi.org/10.18653/v1/2024.findings-emnlp.928

## Abstract

Large Language Models (LLMs) have shown remarkable capabilities in a multitude of Natural Language Processing (NLP) tasks. However, these models are still not immune to limitations such as social biases, especially gender bias. This work investigates whether current closed and open-source LLMs possess gender bias, especially when asked to give moral opinions. To evaluate these models, we curate and introduce a new dataset GenMO (Genderbias in Morality Opinions) comprising parallel short stories featuring male and female characters respectively. Specifically, we test models from the GPT family (GPT-3.5-turbo, GPT-3.5turbo-instruct, GPT-4-turbo), Llama 3 and 3.1 families (8B/70B), Mistral-7B and Claude 3 families (Sonnet and Opus). Surprisingly, despite employing safety checks, all productionstandard models we tested display significant gender bias with GPT-3.5-turbo giving biased opinions in 24% of the samples. Additionally, all models consistently favour female characters, with GPT showing bias in 68-85% of cases and Llama 3 in around 81-85% instances. Additionally, our study investigates the impact of model parameters on gender bias and explores real-world situations where LLMs reveal biases in moral decision-making.

## Dataset Information

Size: Parallel short stories (exact count in full paper)

## Data Description

GenMO is a dataset of 908 parallel short story pairs featuring male and female protagonists, drawn from Moral Stories, ETHICS, and Social Chemistry 101 datasets, designed to evaluate gender bias in LLM moral judgments.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 2
**Implementation Readiness:** HIGH

## Tags

