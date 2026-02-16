---




Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: YRKTB8AA
type: conferencePaper
short_title: HalluDial
year: 2025
first_author: "[[Wen Luo]]"
last_author: "[[Xi Yang]]"
authors: "Wen Luo; Tianshu Shen; Wei Li; Guangyue Peng; Richeng Xuan; Houfeng Wang; Xi Yang"
doi: 10.48550/arXiv.2406.07070
tags: 
url: "http://arxiv.org/abs/2406.07070"
external_pdf: "http://arxiv.org/pdf/2406.07070.pdf"
publication: arXiv.org
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
pdf_extract: "PDF Extracts/2024/2024-Luo-HalluDial.md"
abstract: "Large Language Models (LLMs) have significantly advanced the field of Natural Language Processing (NLP), achieving remarkable performance across diverse tasks and enabling widespread real-world applications. However, LLMs are prone to hallucination, generating content that either conflicts with established knowledge or is unfaithful to the original sources. Existing hallucination benchmarks primarily focus on sentence- or passage-level hallucination detection, neglecting dialogue-level..."
paper_summary: "Abstract: Large Language Models (LLMs) have significantly advanced the field of Natural Language Processing (NLP), achieving remarkable performance across diverse tasks and enabling widespread real-world applic | Overview: HalluDial: A Large-Scale Benchmark for Automatic Dialogue-Level Hallucination Evaluation Wen Luo1,2∗ Tianshu Shen3 Wei Li2 Guangyue Peng2 Richeng Xuan1 Houfeng Wang2† Xi Yang1† 1Beijing Academy of Art | Key Findings: Wen Luo1,2∗ Tianshu Shen3 Wei Li2 Guangyue Peng2 Richeng Xuan1 Houfeng Wang2† Xi Yang1† 1Beijing Academy of Artificial Intelligence 2National Key Labo | Conclusions: In this paper, we introduced HalluDial, the first large-scale benchmark for dialogue-level halluci- nation evaluation, addressing critical gaps in exi"
local_pdf: [[PDFs/2024/2024-Luo-HalluDial.pdf]]
DATE_ADDED: 20260208
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Truthfulness & Factuality"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for hallucination detection dataset for conversational ai"
data_metrics: "146,856 samples"
LLM_assessed: "GPT-4, GPT-3.5, Llama-2, Vicuna, Mistral"
DATA_URL: "https://github.com/FlagOpen/HalluDial"
---
# HalluDial: A Large-Scale Benchmark for Automatic Dialogue-Level Hallucination Evaluation

## Metadata

**Authors:** Luo, Wen; Shen, Tianshu; Li, Wei; Peng, Guangyue; Xuan, Richeng; Wang, Houfeng; Yang, Xi

**Year:** 2024

**Type:** preprint

**DOI:** [10.48550/arXiv.2406.07070](https://doi.org/10.48550/arXiv.2406.07070)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2024/2024-Luo-HalluDial.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2406.07070
- **DOI:** https://doi.org/10.48550/arXiv.2406.07070

## Abstract

Large Language Models (LLMs) have significantly advanced the field of Natural Language Processing (NLP), achieving remarkable performance across diverse tasks and enabling widespread real-world applications. However, LLMs are prone to hallucination, generating content that either conflicts with established knowledge or is unfaithful to the original sources. Existing hallucination benchmarks primarily focus on sentence- or passage-level hallucination detection, neglecting dialogue-level evaluation, hallucination localization, and rationale provision. They also predominantly target factuality hallucinations while underestimating faithfulness hallucinations, often relying on labor-intensive or non-specialized evaluators. To address these limitations, we propose HalluDial, the first comprehensive large-scale benchmark for automatic dialogue-level hallucination evaluation. HalluDial encompasses both spontaneous and induced hallucination scenarios, covering factuality and faithfulness hallucinations. The benchmark includes 4,094 dialogues with a total of 146,856 samples. Leveraging HalluDial, we conduct a comprehensive meta-evaluation of LLMs’ hallucination evaluation capabilities in information-seeking dialogues and introduce a specialized judge language model, HalluJudge. The high data quality of HalluDial enables HalluJudge to achieve superior or competitive performance in hallucination evaluation, facilitating the automatic assessment of dialogue-level hallucinations in LLMs and providing valuable insights into this phenomenon. The dataset and the code are available at https://github.com/FlagOpen/HalluDial.

## Authors

[[Wen Luo]], [[Tianshu Shen]], [[Wei Li]], [[Guangyue Peng]], [[Richeng Xuan]], [[Houfeng Wang]], [[Xi Yang]]

## Data Description

HalluDial is a large-scale benchmark for automatic dialogue-level hallucination evaluation, comprising 4,094 dialogues with 146,856 samples covering both factuality and faithfulness hallucinations. The dataset includes spontaneous hallucination scenarios (91,785 natural responses from LLMs annotated by GPT-4) and induced hallucination scenarios (55,071 GPT-4-generated hallucinated samples). Models evaluated for hallucination detection include Llama-2 (7B, 13B, 70B), Vicuna (7B, 13B, 33B), GPT-3.5-turbo, GPT-4 variants, and GPT-4o.


## Notes


## Tags

#Computer-Science---Computation-and-Language

## Citation Info

36 citations (Semantic Scholar/DOI) [2025-08-27] 15 citations (Semantic Scholar/DOI) [2025-08-23]
