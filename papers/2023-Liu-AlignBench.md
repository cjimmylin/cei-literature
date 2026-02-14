---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: YC7WMTUP
type: conferencePaper
short_title: AlignBench
year: 2025
first_author: "[[Xiao Liu]]"
last_author: "[[Jie Tang]]"
authors: "Xiao Liu; Xuanyu Lei; Shengyuan Wang; Yue Huang; Zhuoer Feng; Bosi Wen; Jiale Cheng; Pei Ke; Yifan Xu; Weng Lam Tam; Xiaohan Zhang; Lichao Sun; Xiaotao Gu; Hongning Wang; Jing Zhang; Minlie Huang; Yuxiao Dong; Jie Tang"
doi: 10.48550/arXiv.2311.18743
url: "http://arxiv.org/abs/2311.18743"
external_pdf: "http://arxiv.org/pdf/2311.18743.pdf"
publication: "Annual Meeting of the Association for Computational Linguistics"
national_ethnic_cultural: Chinese
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: "Chinese, AI Safety & Alignment"
key_contribution: "Introduced AlignBench, a multi-dimensional benchmark for evaluating *Chinese* LLM alignment, featuring human-verified references and a rule-calibrated LLM-as-Judge evaluation."
significance: "Fills the gap for evaluating alignment in Chinese language models, providing a culturally and linguistically specific testbed for the growing ecosystem of Chinese LLMs (ChatGLM, Qwen, etc.)."
tags: 
pdf_extract: "PDF Extracts/2023/2023-Liu-AlignBench.md"
abstract: "Alignment has become a critical step for instruction-tuned Large Language Models (LLMs) to become helpful assistants. However, the effective evaluation of alignment for emerg- ing Chinese LLMs is still largely unexplored. To fill in this gap, we introduce ALIGNBENCH, a comprehensive multi-dimensional benchmark for evaluating LLMs’ alignment in Chinese. We design a human-in-the-loop data curation pipeline, containing eight main categories, 683 real-scenario rooted queries and correspond- ing huma"
paper_summary: "Abstract: Alignment has become a critical step for instruction-tuned Large Language Models (LLMs) to become helpful assistants. However, the effective evaluation of alignment for emerg- ing Chinese LLMs is stil | Overview: AlignBench: Benchmarking Chinese Alignment of Large Language Models Xiao Liu1,2,∗, Xuanyu Lei1,2,∗,†, Shengyuan Wang1,2,†, Yue Huang5,2,†, Zhuoer Feng4,2,†, Bosi Wen4,2,†, Jiale Cheng4,2,†, Pei Ke4, Y | Methodology: for grading. Human evaluations justified its ap- plicability compared to existing LLM-as-Judge methods (Zheng et al., 2023). • We systematically bench | Key Findings: Real-user Scenario LLM Judgment Logical Reasoning Task-Oriented Role Play Figure 1: Overall framework of ALIGNBENCH. 1) Data Curation: a human-in-the- | Conclusions: We introduce ALIGNBENCH, a comprehen- sive multi-dimensional benchmark for evaluating LLMs’ alignment in Chinese. A sustainable human- in-the-loop dat"
local_pdf: [[PDFs/2023/2023-Liu-AlignBench.pdf]]
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "AI Safety & Alignment"
is_benchmark: Yes
is_eval: Yes
is_dataset: No
data_description: Benchmark
data_metrics: "Not specified"
LLM_assessed: "GPT-4, GPT-3.5, Qwen, Llama-2"
DATA_URL: "https://github.com/THUDM/AlignBench"
---
# AlignBench: Benchmarking Chinese Alignment of Large Language Models

## Metadata

**Authors:** Liu, Xiao; Lei, Xuanyu; Wang, Shengyuan; Huang, Yue; Feng, Zhuoer; Wen, Bosi; Cheng, Jiale; Ke, Pei; Xu, Yifan; Tam, Weng Lam; Zhang, Xiaohan; Sun, Lichao; Gu, Xiaotao; Wang, Hongning; Zhang, Jing; Huang, Minlie; Dong, Yuxiao; Tang, Jie

**Year:** 2024

**Type:** preprint

**DOI:** [10.48550/arXiv.2311.18743](https://doi.org/10.48550/arXiv.2311.18743)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2023/2023-Liu-AlignBench.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2311.18743
- **DOI:** https://doi.org/10.48550/arXiv.2311.18743

## Abstract

Alignment has become a critical step for instruction-tuned Large Language Models (LLMs) to become helpful assistants. However, the effective evaluation of alignment for emerging Chinese LLMs is still largely unexplored. To fill in this gap, we introduce ALIGNBENCH, a comprehensive multi-dimensional benchmark for evaluating LLMs’ alignment in Chinese. We design a human-in-the-loop data curation pipeline, containing eight main categories, 683 real-scenario rooted queries and corresponding human verified references. To ensure the correctness of references, each knowledgeintensive query is accompanied with evidences collected from reliable web sources (including URLs and quotations) by our annotators. For automatic evaluation, our benchmark employs a rule-calibrated multi-dimensional LLMas-Judge (Zheng et al., 2023) approach with Chain-of-Thought to generate explanations and final ratings, ensuring high reliability and interpretability. All evaluation code, data, and LLM generations are available at https:// github.com/THUDM/AlignBench. Since its release, AlignBench has been adopted by top (Chinese) LLMs for evaluating their alignment capabilities in Chinese, including ChatGLM, Qwen, DeepSeek, Yi, Baichuan, and Abab.

## Authors

[[Xiao Liu]], [[Xuanyu Lei]], [[Shengyuan Wang]], [[Yue Huang]], [[Zhuoer Feng]], [[Bosi Wen]], [[Jiale Cheng]], [[Pei Ke]], [[Yifan Xu]], [[Weng Lam Tam]], [[Xiaohan Zhang]], [[Lichao Sun]], [[Xiaotao Gu]], [[Hongning Wang]], [[Jing Zhang]], [[Minlie Huang]], [[Yuxiao Dong]], [[Jie Tang]]

## Data Description

AlignBench is a comprehensive benchmark for evaluating Chinese alignment of LLMs, containing 683 real-scenario rooted queries across 8 categories (Fundamental Language Ability, Advanced Chinese Understanding, Open-ended Questions, Writing Ability, Logical Reasoning, Mathematics, Task-oriented Role Play, Professional Knowledge). It uses human-verified references with web-sourced evidence and employs a rule-calibrated multi-dimensional LLM-as-Judge evaluation method with GPT-4 across 17 LLMs.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Machine-Learning #Computer-Science---Computation-and-Language

## Citation Info

57 citations (Semantic Scholar/DOI) [2025-08-27] 56 citations (Semantic Scholar/DOI) [2025-08-23]
