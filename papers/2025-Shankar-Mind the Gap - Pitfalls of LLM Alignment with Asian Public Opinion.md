---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0089
type: conferencePaper
short_title: Mind the Gap -- Pitfalls of LLM Alignment with Asian Public Opinion
year: 2025
first_author: "[[H. Shankar]]"
authors: "Shankar, H., S P, V., Margapuri, S., & Mazumder, D"
url: "https://arxiv.org/abs/2306.16388"
external_pdf: "https://arxiv.org/pdf/2306.16388.pdf"
local_pdf: "[[PDFs/2025-Shankar-Mind the Gap - Pitfalls of LLM Alignment with Asian Public Opinion.pdf]]"
pdf_extract: "PDF Extracts/2025-Shankar-Mind the Gap - Pitfalls of LLM Alignment with Asian Public Opinion.md"
publication: Scientific Reports
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "American"
religious_values: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
tags: 
abstract: "Large language models (LLMs) may not equitably represent diverse global perspectives on societal issues. In this paper, we develop a quantitative framework to evaluate whose opinions model-generated responses are more similar to. We first build a dataset, GlobalOpinionQA, comprised of questions and answers from cross-national surveys designed to capture diverse opinions on global issues across different countries."
ethics_perspective: "AI Safety & Alignment"
data_description: "Evaluation framework dataset for question answering"
data_metrics: "Not specified"
---
# Mind the Gap -- Pitfalls of LLM Alignment with Asian Public Opinion

## Authors

[[Shankar, H., S P, V., Margapuri, S., & Mazumder, D]]

## Metadata

**Authors:** Shankar, H., S P, V., Margapuri, S., & Mazumder, D

**Year:** 2025

**Type:** conferencePaper

**Venue:** Scientific Reports

## Links

- **arXiv:** https://arxiv.org/abs/2306.16388

## Abstract

Large language models (LLMs) may not equitably represent diverse global perspectives on societal issues. In this paper, we develop a quantitative framework to evaluate whose opinions model-generated responses are more similar to. We first build a dataset, GlobalOpinionQA, comprised of questions and answers from cross-national surveys designed to capture diverse opinions on global issues across different countries. Next, we define a metric that quantifies the similarity between LLM-generated survey responses and human responses, conditioned on country. With our framework, we run three experiments on an LLM trained to be helpful, honest, and harmless with Constitutional AI. By default, LLM responses tend to be more similar to the opinions of certain populations, such as those from the USA, and some European and South American countries, highlighting the potential for biases. When we prompt the model to consider a particular country’s perspective, responses shift to be more similar to the opinions of the prompted populations, but can reflect harmful cultural stereotypes. When we translate GlobalOpinionQA questions to a target language, the model’s responses do not necessarily become the most similar to the opinions of speakers of those languages. We release our dataset for others to use and build on.2 We also provide an interactive visualization at https://llmglobalvalues.anthropic.com.

## Dataset Information

Format: Survey-based alignment evaluation

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 12-13
**Implementation Readiness:** MEDIUM

## Tags

