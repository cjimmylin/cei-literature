---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: ASUKFPK8
type: journalArticle
short_title: R-Judge
year: 2025
first_author: "[[Tongxin Yuan]]"
last_author: "[[Gongshen Liu]]"
authors: "Tongxin Yuan; Zhiwei He; Lingzhong Dong; Yiming Wang; Ruijie Zhao; Tian Xia; Lizhen Xu; Binglin Zhou; Fangqi Li; Zhuosheng Zhang; Rui Wang; Gongshen Liu"
url: "https://arxiv.org/abs/2401.10019"
pdf_extract: "PDF Extracts/2024/2024-Yuan-R-Judge.md"
local_pdf: [[PDFs/2024/2024-Yuan-R-Judge.pdf]]
external_pdf: "https://arxiv.org/pdf/2401.10019.pdf"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: Deontology
key_contribution: "Benchmark (R-Judge) for evaluating behavioral safety and risk awareness of LLM agents in interactive environments"
significance: "Focuses on 'safety judgment' and risk identification (deontological boundaries) rather than just content harm, addressing agentic risks"
tags: 
abstract: "Large language models (LLMs) have exhibited great potential in autonomously completing tasks across real-world applications. However, LLM agents introduce unexpected safety risks when operating in interactive environments. Instead of centering on the harmlessness of LLMgenerated content in most prior studies, this work addresses the imperative need for benchmarking the behavioral safety of LLM agents within diverse environments."
paper_summary: "Abstract: Large language models (LLMs) have exhibited great potential in autonomously completing tasks across real-world applications. However, LLM agents introduce unexpected safety risks when operating in int | Overview: R-Judge: Benchmarking Safety Risk Awareness for LLM Agents Tongxin Yuan* , Zhiwei He∗, Lingzhong Dong, Yiming Wang, Ruijie Zhao, Tian Xia, Lizhen Xu, Binglin Zhou, Fangqi Li, Zhuosheng Zhang†, Rui Wan | Key Findings: Task Instruction: [1. Risk Identification] Analyze if agent actions are safe in above scenario. [2. Safety Judgment] Judge 'safe' or 'unsafe'. [2. Saf | Conclusions: Risk awareness is crucial for the safe execution of LLM agents in interactive environments. In this work, we present R-Judge, a general, realistic, an"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "Yes"
utilitarian_ethics: "No"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark for ai safety"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, ChatGPT, Llama-3, Llama-2, Vicuna, Mistral"
DATA_URL: "https://github.com/Lordog/R-Judge"
---
 R-Judge: A Benchmark for Evaluating the Reasoning and Judgment of Language Models

## Authors

[[Tongxin Yuan]], [[Zhiwei He]], [[Lingzhong Dong]], [[Yiming Wang]], [[Ruijie Zhao]], [[Tian Xia]], [[Lizhen Xu]], [[Binglin Zhou]], [[Fangqi Li]], [[Zhuosheng Zhang]], [[Rui Wang]], [[Gongshen Liu]]

## Links

- **Local PDF:** [[PDFs/2024/2024-Yuan-R-Judge.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2401.10019

## Abstract

Large language models (LLMs) have exhibited great potential in autonomously completing tasks across real-world applications. Despite this, these LLM agents introduce unexpected safety risks when operating in interactive environments. Instead of centering on the harmlessness of LLM-generated content in most prior studies, this work addresses the imperative need for benchmarking the behavioral safety of LLM agents within diverse environments. We introduce R-Judge, a benchmark crafted to evaluate the proficiency of LLMs in judging and identifying safety risks given agent interaction records. R-Judge comprises 569 records of multi-turn agent interaction, encompassing 27 key risk scenarios among 5 application categories and 10 risk types. It is of high-quality curation with annotated safety labels and risk descriptions. Evaluation of 11 LLMs on R-Judge shows considerable room for enhancing the risk awareness of LLMs: The best-performing model, GPT-4o, achieves 74.42% while no other models significantly exceed the random. Moreover, we reveal that risk awareness in open agent scenarios is a multi-dimensional capability involving knowledge and reasoning, thus challenging for LLMs. With further experiments, we find that fine-tuning on safety judgment significantly improve model performance while straightforward prompting mechanisms fail. R-Judge is publicly available at https://github.com/Lordog/R-Judge.

## Data Description

R-Judge is a benchmark for evaluating LLMs' proficiency in judging and identifying safety risks in agent interaction records, comprising 569 multi-turn agent interaction records across 27 risk scenarios in 5 application categories and 10 risk types. The dataset includes both intended attacks (indirect prompt injection) and unintended risks, with annotated safety labels and risk descriptions. Eleven LLMs were evaluated including GPT-4o, ChatGPT, Llama-3-8B, Llama-2-13b/7b, Vicuna-13b/7b variants, and Mistral-7B, with GPT-4o achieving the best F1 score of 74.45%.


## Notes


## Citation Info

99 citations (Semantic Scholar/arXiv) [2025-08-27]
