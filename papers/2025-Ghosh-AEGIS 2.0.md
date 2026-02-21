---









Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0016
type: conferencePaper
short_title: "AEGIS 2.0"
year: 2025
first_author: "[[Ghosh, Shaona]]"
last_author: "[[Parisien, Christopher]]"
authors: "Ghosh, Shaona; Varshney, Prasoon; Sreedhar, Makesh Narsimhan; Padmakumar, Aishwarya; Rebedea, Traian; Varghese, Jibin Rajan; Parisien, Christopher"
authors_incomplete: false
url: "https://arxiv.org/abs/2501.09004"
external_pdf: "https://arxiv.org/pdf/2501.09004.pdf"
pdf_extract: "PDF Extracts/2025/2025-Ghosh-AEGIS 2.0.md"
local_pdf: "[[PDFs/2025/2025-Ghosh-AEGIS 2.0.pdf]]"
publication: "ACL 2025"
CONF-CC: "ACL 2025"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "As Large Language Models (LLMs) and generative AI become increasingly widespread, concerns about content safety have grown in parallel. Currently, there is a clear lack of highquality, human-annotated datasets that address the full spectrum of LLM-related safety risks and are usable for commercial applications. To bridge this gap, we propose a comprehensive and adaptable taxonomy for categorizing safety risks, structured into 12 top-level hazard categories with an extension to 9 fine-grained..."
LLM_assessed: "Llama-3, Mistral, Gemma, Mixtral"
DATA_URL: "https://github.com/meta-llama/llama-recipes"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Annotated dataset"
data_metrics: "248 samples"
CONFERENCE: "ACL 2025"
---
# AEGIS 2.0

## Authors

[[Shaona Ghosh|Ghosh, Shaona]], [[Varshney, Prasoon]], [[Sreedhar, Makesh Narsimhan]], [[Padmakumar, Aishwarya]], [[Rebedea, Traian]], [[Varghese, Jibin Rajan]], [[Parisien, Christopher]]

## Metadata

**Authors:** Ghosh, Shaona; Varshney, Prasoon; Sreedhar, Makesh Narsimhan; Padmakumar, Aishwarya; Rebedea, Traian; Varghese, Jibin Rajan; Parisien, Christopher

**Year:** 2025

**Type:** conferencePaper

**Venue:** ACL 2025

## Links

- **arXiv:** https://arxiv.org/abs/2501.09004
- **Code/Data:** https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0; https://huggingface.co/nvidia/Aegis-AI-Content-Safety-LlamaGuard-Permissive-1.0

## Abstract

As Large Language Models (LLMs) and generative AI become increasingly widespread, concerns about content safety have grown in parallel. Currently, there is a clear lack of highquality, human-annotated datasets that address the full spectrum of LLM-related safety risks and are usable for commercial applications. To bridge this gap, we propose a comprehensive and adaptable taxonomy for categorizing safety risks, structured into 12 top-level hazard categories with an extension to 9 fine-grained subcategories. This taxonomy is designed to meet the diverse requirements of downstream users, offering more granular and flexible tools for managing various risk types. Using a hybrid data generation pipeline that combines human annotations with a multi-LLM "jury" system to assess the safety of responses, we obtain AEGIS2.0, a carefully curated collection of 34, 248 samples of human-LLM interactions, annotated according to our proposed taxonomy. To validate its effectiveness, we demonstrate that several lightweight models, trained using parameter-efficient techniques on AEGIS2.0, achieve performance competitive with leading safety models fully fine-tuned on much larger, non-commercial datasets. In addition, we introduce a novel training blend that combines safety with topic following data. This approach enhances the adaptability of guard models, enabling them to generalize to new risk categories defined during inference. We plan to opensource AEGIS2.0 data and models to the research community to aid in the safety guardrailing of LLMs.

## Dataset Information

33,416 annotated human-LLM interactions (34,248 total samples)

## Data Description

AEGIS 2.0 is a curated AI safety dataset of 34,248 human-LLM interaction samples annotated according to a 12-category content safety risk taxonomy with 9 fine-grained subcategories. The dataset uses Mistral-7B-v0.1 for response generation and Gemma-2-27B for synthetic refusals. Safety guard models were fine-tuned on Llama-3.1-8B-Instruct using parameter-efficient techniques, with an LLM jury of Mixtral-8x22B, Mistral-NeMo, and Gemma-2-27B for response-level annotation.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 16
**Implementation Readiness:** HIGH

## Tags

