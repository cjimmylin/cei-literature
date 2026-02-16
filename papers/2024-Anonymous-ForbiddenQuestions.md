---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: TQADI49R
type: conferencePaper
short_title: ForbiddenQuestions
year: 2024
first_author: "[[Anonymous]]"
last_author: "[[Anonymous]]"
authors: Anonymous
doi: 10.1145/3658644.3670388
url: "https://dl.acm.org/doi/10.1145/3658644.3670388"
external_pdf: "file:///Users/jimmylin/Zotero/storage/A83END5M/Anonymous - 2024 - ForbiddenQuestions A Benchmark of In-the-Wild Jailbreak Prompts.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
research_topic: "AI Safety & Alignment"
abstract: "The misuse of large language models (LLMs) has drawn significant attention from the general public and LLM vendors. One particular type of adversarial prompt, known as jailbreak prompt, has emerged as the main attack vector to bypass the safeguards and elicit harmful content from LLMs. In this paper, employing our new framework JailbreakHub, we conduct a comprehensive analysis of 1,405 jailbreak prompts spanning from December 2022 to December 2023. We identify 131 jailbreak communities and discover unique characteristics of jailbreak prompts and their major attack strategies, such as prompt injection and privilege escalation. We also observe that jailbreak prompts increasingly shift from online Web communities to prompt-aggregation websites and 28 user accounts have consistently optimized jailbreak prompts over 100 days. To assess the potential harm caused by jailbreak prompts, we create a question set comprising 107,250 samples across 13 forbidden scenarios. Our experiments on six popular LLMs show that their safeguards cannot adequately defend jailbreak prompts in all scenarios."
DATE_ADDED: 20260208
LLM_assessed: "ChatGPT, GPT-4, PaLM-2, Vicuna"
DATA_URL: "https://github.com/verazuo/jailbreak_llms"
pdf_extract: "PDF Extracts/2024/2024-Anonymous-ForbiddenQuestions.md"
local_pdf: "[[PDFs/2024/2024-Anonymous-ForbiddenQuestions.pdf]]"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "No"
is_dataset: "No"
data_description: "Benchmark"
data_metrics: "107,250 samples"
---
# ForbiddenQuestions: A Benchmark of In-the-Wild Jailbreak Prompts

## Metadata

**Authors:** Anonymous

**Year:** 2024

**Publication:** Proceedings of the ACM Conference

**Type:** conferencePaper

**DOI:** [10.1145/3658644.3670388](https://doi.org/10.1145/3658644.3670388)

## Links

- **URL:** https://dl.acm.org/doi/10.1145/3658644.3670388
- **DOI:** https://doi.org/10.1145/3658644.3670388

## Abstract

The misuse of large language models (LLMs) has drawn significant attention from the general public and LLM vendors. One particular type of adversarial prompt, known as jailbreak prompt, has emerged as the main attack vector to bypass the safeguards and elicit harmful content from LLMs. In this paper, employing our new framework JailbreakHub, we conduct a comprehensive analysis of 1,405 jailbreak prompts spanning from December 2022 to December 2023. We identify 131 jailbreak communities and discover unique characteristics of jailbreak prompts and their major attack strategies, such as prompt injection and privilege escalation. We also observe that jailbreak prompts increasingly shift from online Web communities to prompt-aggregation websites and 28 user accounts have consistently optimized jailbreak prompts over 100 days. To assess the potential harm caused by jailbreak prompts, we create a question set comprising 107,250 samples across 13 forbidden scenarios. Our experiments on six popular LLMs show that their safeguards cannot adequately defend jailbreak prompts in all scenarios.

## Authors

[[Anonymous]]

## Data Description

The study creates a forbidden question set comprising 107,250 samples across 13 forbidden scenarios based on OpenAI usage policy and evaluates six LLMs: ChatGPT (GPT-3.5), GPT-4, PaLM2, ChatGLM, Dolly, and Vicuna. Using the JAILBREAKHUB framework, 1,405 jailbreak prompts collected from four platforms (Reddit, Discord, websites, open-source datasets) spanning December 2022 to December 2023 are systematically tested against these models to measure attack success rates.


## Notes


## Citation Info

328 citations (Semantic Scholar/DOI) [2025-08-27]
