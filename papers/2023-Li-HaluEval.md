---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LEKN2KMM
type: conferencePaper
short_title: HaluEval
year: 2025
first_author: "[[Junyi Li]]"
last_author: "[[Ji-Rong Wen]]"
authors: "Junyi Li; Xiaoxue Cheng; Wayne Xin Zhao; Jian-Yun Nie; Ji-Rong Wen"
doi: 10.48550/arXiv.2305.11747
tags: 
url: "http://arxiv.org/abs/2305.11747"
external_pdf: "http://arxiv.org/pdf/2305.11747.pdf"
publication: "Conference on Empirical Methods in Natural Language Processing"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
pdf_extract: "PDF Extracts/2023/2023-Li-HaluEval.md"
abstract: "Large language models (LLMs), such as ChatGPT, are prone to generate hallucinations, i.e., content that conflicts with the source or cannot be verified by the factual knowledge. To understand what types of content and to which extent LLMs are apt to hallucinate, we introduce the Hallucination Evaluation benchmark for Large Language Models (HaluEval), a large collection of generated and human-annotated hallucinated samples for evaluating the performance of LLMs in recognizing hallucination."
paper_summary: "Abstract: Large language models (LLMs), such as Chat- GPT, are prone to generate hallucinations, i.e., content that conflicts with the source or cannot be verified by the factual knowledge. To un- derstand what | Overview: HaluEval: A Large-Scale Hallucination Evaluation Benchmark for Large Language Models Junyi Li1,3,4∗, Xiaoxue Cheng1∗, Wayne Xin Zhao1,4†, Jian-Yun Nie3 and Ji-Rong Wen1,2,4 1Gaoling School of Artifici | Conclusions: We introduce HaluEval, a large-scale collection of generated and human-annotated hallucinated sam- ples for evaluating the performance of LLMs in reco"
local_pdf: "[[PDFs/2023/2023-Li-HaluEval.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: "ChatGPT, GPT-3, text-davinci, Claude, Llama-2, Falcon, Vicuna, Alpaca"
DATA_URL: "https://github.com/RUCAIBox/HaluEval"
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Truthfulness & Factuality"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for hallucination detection annotated dataset"
data_metrics: "Not specified"
---
# HaluEval: A Large-Scale Hallucination Evaluation Benchmark for Large Language Models

## Metadata

**Authors:** Li, Junyi; Cheng, Xiaoxue; Zhao, Wayne Xin; Nie, Jian-Yun; Wen, Ji-Rong

**Year:** 2023

**Type:** preprint

**DOI:** [10.48550/arXiv.2305.11747](https://doi.org/10.48550/arXiv.2305.11747)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2023/2023-Li-HaluEval.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2305.11747
- **DOI:** https://doi.org/10.48550/arXiv.2305.11747

## Abstract

Large language models (LLMs), such as ChatGPT, are prone to generate hallucinations, i.e., content that conflicts with the source or cannot be verified by the factual knowledge. To understand what types of content and to which extent LLMs are apt to hallucinate, we introduce the Hallucination Evaluation benchmark for Large Language Models (HaluEval), a large collection of generated and human-annotated hallucinated samples for evaluating the performance of LLMs in recognizing hallucination. To generate these samples automatically, we propose a two-stage framework, i.e., samplingthen-filtering. Besides, we hire some human labelers to annotate the hallucinations in ChatGPT responses. The empirical results suggest that ChatGPT is likely to generate hallucinated content related to specific topics by fabricating unverifiable information (i.e., about 19.5% responses). Moreover, existing LLMs face great challenges in recognizing the hallucinations in texts. However, our experiments also prove that providing external knowledge or adding reasoning steps can help LLMs recognize hallucinations. Our benchmark can be accessed at https://github.com/RUCAIBox/HaluEval.

## Authors

[[Junyi Li]], [[Xiaoxue Cheng]], [[Wayne Xin Zhao]], [[Jian-Yun Nie]], [[Ji-Rong Wen]]

## Data Description

HaluEval is a large-scale hallucination evaluation benchmark containing 35,000 samples: 30,000 automatically generated hallucinated/normal examples across question answering (HotpotQA), knowledge-grounded dialogue (OpenDialKG), and text summarization (CNN/Daily Mail), plus 5,000 human-annotated ChatGPT responses to general user queries from Alpaca. The benchmark evaluates LLMs' ability to recognize hallucinated content across these tasks.


## Notes


## Tags

#Computer-Science---Computation-and-Language

## Citation Info

276 citations (Semantic Scholar/arXiv) [2025-08-27] 272 citations (Semantic Scholar/DOI) [2025-08-23] arXiv:2305.11747 [cs]
