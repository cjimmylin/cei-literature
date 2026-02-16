---




Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0003
type: conferencePaper
short_title: BiasJailbreak
year: 2025
first_author: "[[Isack Lee]]"
last_author: "[[Haebin Seong Isack Lee]]"
authors: "Isack Lee, Haebin Seong"
url: "https://arxiv.org/abs/2410.13334"
external_pdf: "https://arxiv.org/pdf/2410.13334.pdf"
pdf_extract: "PDF Extracts/0000/2026-Lee-BiasJailbreak.md"
local_pdf: "[[PDFs/2026/2026-Lee-BiasJailbreak.pdf]]"
publication: "AAAI 2026"
DATE_ADDED: 20260207
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "No"
is_dataset: "No"
tags: 
abstract: "Warning: This paper contains potentially offensive and harmful text. Although large language models (LLMs) demonstrate impressive proficiency in various tasks, they present potential safety risks, such as 'jailbreaks', where malicious inputs can coerce LLMs into generating harmful content bypassing safety alignments. In this paper, we delve into the ethical biases in LLMs and examine how those biases could be exploited for jailbreaks."
ethics_perspective: "AI Safety & Alignment"
data_description: "N/A"
data_metrics: "Not specified"
LLM_assessed: "GPT-3.5, GPT-4, ChatGPT, Claude, Llama-2, Llama-3, Qwen, Phi"
DATA_URL: "https://github.com/Isaac-theori/BiasJailbreak"
research_topic: "Other"
---
# BiasJailbreak

## Authors

[[Hwaran Lee|Haebin Seong Isack Lee]]

## Metadata

**Authors:** Isack Lee, Haebin Seong

**Year:** 2026

**Type:** conferencePaper

**Venue:** AAAI 2026

## Links

- **arXiv:** https://arxiv.org/abs/2410.13334

## Abstract

Warning: This paper contains potentially offensive and harmful text. Although large language models (LLMs) demonstrate impressive proficiency in various tasks, they present potential safety risks, such as ‘jailbreaks’, where malicious inputs can coerce LLMs into generating harmful content bypassing safety alignments. In this paper, we delve into the ethical biases in LLMs and examine how those biases could be exploited for jailbreaks. Notably, these biases result in a jailbreaking success rate in GPT-4o models that differs by 20% between non-binary and cisgender keywords and by 16% between white and black keywords, even when the other parts of the prompts are identical. We introduce the concept of BiasJailbreak, highlighting the inherent risks posed by these safety-induced biases. BiasJailbreak generates biased keywords automatically by asking the target LLM itself, and utilizes the keywords to generate harmful output. Additionally, we propose an efficient defense method BiasDefense, which prevents jailbreak attempts by injecting defense prompts prior to generation. BiasDefense stands as an appealing alternative to Guard Models, such as Llama-Guard, that require additional inference cost after text generation. Our findings emphasize that ethical biases in LLMs can actually lead to generating unsafe output, and suggest a method to make the LLMs more secure and unbiased. To enable further research and improvements, we open-source our code and artifacts of BiasJailbreak, providing the community with tools to better understand and mitigate safety-induced biases in LLMs. Code and Artifacts — https://github.com/Isaac-theori/BiasJailbreak

## Dataset Information

Adversarial prompts with systematically varied demographic keywords

## Data Description

The BiasJailbreak dataset combines harmful prompts from JailBreakBench (100 samples) and AdvBench (totaling 600 harmful prompts) with automatically generated bias keywords representing privileged and marginalized demographic groups. The study evaluates jailbreak success rates across 9 LLMs including GPT-3.5, GPT-4, GPT-4o, Claude-sonnet3.5, LLaMA2, LLaMA3, Qwen-1.5, Qwen2, and Phi-mini, measuring ethical bias differentials in safety alignment.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 16
**Implementation Readiness:** MEDIUM

## Tags

