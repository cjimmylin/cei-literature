---








Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0184
type: preprint
short_title: "Indian-BhED -- A Dataset for Measuring India-Centric Biases in LLMs"
year: 2024
first_author: "[[Khyati Khandelwal]]"
last_author: "[[Scott A. Hale]]"
authors: "Khyati Khandelwal; Manuel Tonneau; Andrew M. Bean; Hannah Rose Kirk; Scott A. Hale"
doi: 10.1145/3677525.3678666
url: "https://arxiv.org/abs/2309.08573"
external_pdf: "https://arxiv.org/pdf/2309.08573.pdf"
pdf_extract: "PDF Extracts/2024/2024-Khandelwal-Indian-BhED - A Dataset for Measuring India-Centric Biases in LLMs.md"
local_pdf: "[[PDFs/2024/2024-Khandelwal-Indian-BhED - A Dataset for Measuring India-Centric Biases in LLMs.pdf]]"
publication: arXiv
CONF-CC: "Preprint"
DATE_ADDED: 20260207
national_ethnic_cultural: "Indian"
cultures_nationalities_list: "Indian"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "Large Language Models (LLMs), now used daily by millions, can encode societal biases, exposing their users to representational harms. A large body of scholarship on LLM bias exists but it predominantly adopts a Western-centric frame and attends comparatively less to bias levels and potential harms in the Global South. In this paper, we quantify stereotypical bias in popular LLMs according to an Indian-centric frame through Indian-BhED, a first of its kind dataset, containing stereotypical and anti-stereotypical examples in the context of caste and religious stereotypes in India. We find that the majority of LLMs tested have a strong propensity to output stereotypes in the Indian context, especially when compared to axes of bias traditionally studied in the Western context, such as gender and race. Notably, we find that GPT-2, GPT-2 Large, and GPT 3.5 have a particularly high propensity for preferring stereotypical outputs as a percent of all sentences for the axes of caste (63-79%) and religion (69-72%). We finally investigate potential causes for such harmful behaviour in LLMs, and posit intervention techniques to reduce both stereotypical and anti-stereotypical biases. The findings of this work highlight the need for including more diverse voices when researching fairness in AI and evaluating LLMs."
LLM_assessed: "BERT, RoBERTa, GPT-2, GPT-3.5, Falcon, Mistral, Llama-2"
DATA_URL: "https://github.com/khyatikhandelwal/Indian-LLMs-Bias"
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Machine Learning"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation approach dataset"
data_metrics: "Not specified"
CONFERENCE: "Preprint"
---
# Indian-BhED -- A Dataset for Measuring India-Centric Biases in LLMs

## Authors

[[Khyati Khandelwal]], [[Manuel Tonneau]], [[Andrew M. Bean]], [[Hannah Rose Kirk]], [[Scott A. Hale]]

## Metadata

**Authors:** Khandelwal, V. & Tonneau, M. et al

**Year:** 2024

**Type:** preprint

**Venue:** arXiv

**DOI:** [10.1145/3677525.3678666](https://doi.org/10.1145/3677525.3678666)

## Links

- **arXiv:** https://arxiv.org/abs/2309.08573
- **DOI:** https://doi.org/10.1145/3677525.3678666

## Abstract

*(To be fetched)*

## Dataset Information

Stereotypical and anti-stereotypical sentence pairs

## Data Description

The paper introduces Indian-BhED, a novel dataset of 229 English-language sentence pairs containing stereotypical and anti-stereotypical examples covering caste-based discrimination and religious biases in the Indian context. It is paired with a filtered subset of CrowS-Pairs (386 racial bias and 159 gender bias sentences) for cross-cultural comparison. Ten LLMs (both encoder and decoder-based) are evaluated for stereotypical bias using All Unmasked Likelihood and Conditional Log-Likelihood metrics.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 9-11
**Implementation Readiness:** MEDIUM

## Tags

