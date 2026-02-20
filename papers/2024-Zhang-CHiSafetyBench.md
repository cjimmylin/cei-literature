---








Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 3HXQHTYW
type: journalArticle
short_title: CHiSafetyBench
year: 2024
first_author: "[[Wenjing Zhang]]"
last_author: "[[Shiguo Lian]]"
authors: "Wenjing Zhang; Xuejiao Lei; Zhaoxiang Liu; Meijuan An; Bikun Yang; KaiKai Zhao; Kai Wang; Shiguo Lian"
url: "https://arxiv.org/abs/2406.10311"
external_pdf: "https://arxiv.org/pdf/2406.10311.pdf"
national_ethnic_cultural: "Chinese"
cultures_nationalities_list: "Chinese"
languages_list: "Chinese"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Chinese, AI Safety & Alignment"
key_contribution: "Introduced CHiSafetyBench, a hierarchical Chinese safety benchmark with 31 categories (5 risk areas) for evaluating risky content identification and refusal capabilities."
significance: "Fills a gap in Chinese-specific safety evaluation, showing that mainstream Chinese LLMs still vary significantly in their ability to handle culturally and linguistically specific risks."
tags: 
pdf_extract: "PDF Extracts/0000/2024-Zhang-CHiSafetyBench.md"
abstract: "With the profound development of large language mod- els(LLMs), their safety concerns have garnered increasing attention. However, there is a scarcity of Chinese safety benchmarks for LLMs, and the existing safety taxonomies are inadequate, lacking comprehensive safety detection ca- pabilities in authentic Chinese scenarios. In this work, we introduce CHiSafetyBench, a dedicated safety benchmark for evaluating LLMs' capabilities in identifying risky con- tent and refusing answering risky questio"
paper_summary: "Abstract: With the profound development of large language mod- els(LLMs), their safety concerns have garnered increasing attention. However, there is a scarcity of Chinese safety benchmarks for LLMs, and the ex | Overview: CHiSafetyBench: A Chinese Hierarchical Safety Benchmark for Large Language Models Wenjing Zhang1,2, Xuejiao Lei1,2, Zhaoxiang Liu1,2*, Meijuan An1,2, Bikun Yang1,2, Kaikai Zhao1,2, Kai Wang1,2, Shiguo | Methodology: that rivals human assessment, facilitating cost-effective and efficient testing of model safety detection and de- fense capabilities, significantly re | Key Findings: not only focuses on overarching but also specific safety di- mensions. Notably, existing hierarchical safety benchmarks predominantly focus on English | Conclusions: We introduce CHiSafetyBench, a specialized and credible benchmark designed based on a Chinese hierarchical safety taxonomy. CHiSafetyBench encompasses"
local_pdf: "[[PDFs/2024/2024-Zhang-CHiSafetyBench.pdf]]"
LLM_assessed: "Baichuan, Baichuan2, ChatGLM, ChatGLM series, ChatGLM3, Qwen, Qwen and, Qwen se, Qwen series, Qwen-110B, Qwen-72B, Qwen1.5, Yi-34B, Yi-6B"
DATA_URL: "https://github.com/UnicomAI/UnicomBenchmark/tree/main/CHiSafetyBench"
publication: arXiv
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for ai safety text corpus"
data_metrics: "31 categories"
CONFERENCE: "Journal"
---
# CHiSafetyBench: A Chinese Hierarchical Safety Benchmark for Large Language Models

## Metadata

**Year:** 2024

**Type:** journalArticle

## Links

- **Local PDF:** [[PDFs/2024/2024-Zhang-CHiSafetyBench.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2406.10311

## Abstract

With the profound development of large language models(LLMs), their safety concerns have garnered increasing attention. However, there is a scarcity of Chinese safety benchmarks for LLMs, and the existing safety taxonomies are inadequate, lacking comprehensive safety detection capabilities in authentic Chinese scenarios. In this work, we introduce CHiSafetyBench, a dedicated safety benchmark for evaluating LLMs' capabilities in identifying risky content and refusing answering risky questions in Chinese contexts. CHiSafetyBench incorporates a dataset that covers a hierarchical Chinese safety taxonomy consisting of 5 risk areas and 31 categories. This dataset comprises two types of tasks: multiple-choice questions and question-answering, evaluating LLMs from the perspectives of risk content identification and the ability to refuse answering risky questions respectively. Utilizing this benchmark, we validate the feasibility of automatic evaluation as a substitute for human evaluation and conduct comprehensive automatic safety assessments on mainstream Chinese LLMs. Our experiments reveal the varying performance of different models across various safety domains, indicating that all models possess considerable potential for improvement in Chinese safety capabilities. Our dataset is publicly available at https://github.com/UnicomAI/UnicomBenchmark/tree/main/CHiSafetyBench.

## Authors

[[Wenjing Zhang]], [[Xuejiao Lei]], [[Zhaoxiang Liu]], [[Meijuan An]], [[Bikun Yang]], [[Kangkang Zhao|KaiKai Zhao]], [[Kaile Wang|Kai Wang]], [[Shiguo Lian]]

## Data Description

CHiSafetyBench is a Chinese hierarchical safety benchmark for evaluating LLMs, featuring a dataset covering 5 risk areas and 31 categories based on Chinese government safety standards. It comprises 1,567 multiple-choice questions and 563 risky questions in question-answering format, with an LLM-based automatic evaluation method used to assess 10 mainstream Chinese LLMs on risk content identification and refusal-to-answer capabilities.


## Notes


## Citation Info

9 citations (Semantic Scholar/arXiv) [2025-08-27]
