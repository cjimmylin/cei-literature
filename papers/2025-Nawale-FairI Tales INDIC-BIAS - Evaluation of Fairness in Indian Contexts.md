---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0052
type: conferencePaper
short_title: "FairI Tales / INDIC-BIAS -- Evaluation of Fairness in Indian Contexts"
year: 2025
first_author: "[[Janki Atul Nawale]]"
last_author: "[[Mitesh M. Khapra]]"
authors: "Janki Atul Nawale; Mohammed Safi Ur Rahman Khan; Janani D; Mansi Gupta; Danish Pruthi; Mitesh M. Khapra"
doi: 10.1007/s44443-025-00137-9
url: "https://arxiv.org/abs/2506.23111"
external_pdf: "https://arxiv.org/pdf/2506.23111.pdf"
pdf_extract: "PDF Extracts/2025/2025-Nawale-FairI Tales INDIC-BIAS - Evaluation of Fairness in Indian Contexts.md"
local_pdf: "[[PDFs/2025/2025-Nawale-FairI Tales INDIC-BIAS - Evaluation of Fairness in Indian Contexts.pdf]]"
publication: "ACL 2025"
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "Indian"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
tags: 
abstract: "Warning: This paper includes content that may be considered offensive or upsetting. Existing studies on fairness are largely Westernfocused, making them inadequate for culturally diverse countries such as India. To address this gap, we introduce INDIC-BIAS, a comprehensive India-centric benchmark designed to evaluate fairness of LLMs across 85 identity groups encompassing diverse castes, religions, regions, and tribes."
ethics_perspective: "Bias & Fairness"
data_description: "Benchmark for bias and fairness"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, Llama-3, Gemma, Mistral, Mixtral, Gemini"
DATA_URL: "https://github.com/AI4Bharat/indic-bias"
---
# FairI Tales / INDIC-BIAS -- Evaluation of Fairness in Indian Contexts

## Authors

[[Janki Atul Nawale]], [[Mohammed Safi Ur Rahman Khan]], [[Janani D]], [[Mansi Gupta]], [[Danish Pruthi]], [[Mitesh M. Khapra]]

## Metadata

**Authors:** Janki Atul Nawale; Mohammed Safi Ur Rahman Khan; Janani D; Mansi Gupta; Danish Pruthi; Mitesh M. Khapra

**Year:** 2025

**Type:** conferencePaper

**Venue:** ACL 2025

**DOI:** [10.1007/s44443-025-00137-9](https://doi.org/10.1007/s44443-025-00137-9)

## Links

- **arXiv:** https://arxiv.org/abs/2506.23111
- **DOI:** https://doi.org/10.1007/s44443-025-00137-9
- **Code/Data:** https://github.com/AI4Bharat/indic-bias; https://huggingface.co/datasets/ai4bharat/Indic-Bias; https://huggingface.co/blog/Omartificial-Intelligence-Space/ilmaam-overview

## Abstract

Warning: This paper includes content that may be considered offensive or upsetting. Existing studies on fairness are largely Westernfocused, making them inadequate for culturally diverse countries such as India. To address this gap, we introduce INDIC-BIAS, a comprehensive India-centric benchmark designed to evaluate fairness of LLMs across 85 identity groups encompassing diverse castes, religions, regions, and tribes. We first consult domain experts to curate over 1,800 socio-cultural topics spanning behaviors and situations, where biases and stereotypes are likely to emerge. Grounded in these topics, we generate and manually validate 20,000 real-world scenario templates to probe LLMs for fairness. We structure these templates into three evaluation tasks: plausibility, judgment, and generation. Our evaluation of 14 popular LLMs on these tasks reveals strong negative biases against marginalized identities, with models frequently reinforcing common stereotypes. Additionally, we find that models struggle to mitigate bias even when explicitly asked to rationalize their decision. Our evaluation provides evidence of both allocative and representational harms that current LLMs could cause towards Indian identities, calling for a more cautious usage in practical applications. We release INDIC-BIAS as an open-source benchmark to advance research on benchmarking and mitigating biases and steoretypes in the Indian context.

## Dataset Information

20,000 manually validated real-world scenario templates

## Data Description

INDIC-BIAS is an India-centric fairness benchmark comprising 20,000 manually validated real-world scenario templates across 85 identity groups spanning caste, religion, region, and tribe categories. The benchmark evaluates LLMs through three tasks (plausibility, judgment, and generation) using over 1,800 expert-curated socio-cultural topics. Fourteen LLMs were evaluated including Llama-3 (1B-70B), Gemma (2B-27B), Mistral (7B, 8x7B MoE), GPT-4O, GPT-4O-mini, Gemini-1.5-Pro, and Gemini-1.5-Flash.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 9-11
**Implementation Readiness:** HIGH

## Tags

