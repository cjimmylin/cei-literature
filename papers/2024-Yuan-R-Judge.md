---
































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: ASUKFPK8
type: journalArticle
short_title: R-Judge
year: 2024
first_author: "[[Tongxin Yuan]]"
last_author: "[[Gongshen Liu]]"
authors: "Tongxin Yuan; Zhiwei He; Lingzhong Dong; Yiming Wang; Ruijie Zhao; Tian Xia; Lizhen Xu; Binglin Zhou; Fangqi Li; Zhuosheng Zhang; Rui Wang; Gongshen Liu"
url: "https://arxiv.org/abs/2401.10019"
pdf_extract: "PDF Extracts/2024/2024-Yuan-R-Judge.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2024/2024-Yuan-R-Judge.pdf]]"
external_pdf: "https://arxiv.org/pdf/2401.10019.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
rv_islam: 0
rv_christianity: 0
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 0
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: "N/A"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: Deontology
key_contribution: "Benchmark (R-Judge) for evaluating behavioral safety and risk awareness of LLM agents in interactive environments"
significance: "Focuses on 'safety judgment' and risk identification (deontological boundaries) rather than just content harm, addressing agentic risks"
tags: 
abstract: "Large language models (LLMs) have exhibited great potential in autonomously completing tasks across real-world applications. However, LLM agents introduce unexpected safety risks when operating in interactive environments. Instead of centering on the harmlessness of LLMgenerated content in most prior studies, this work addresses the imperative need for benchmarking the behavioral safety of LLM agents within diverse environments."
paper_summary: "Abstract: Large language models (LLMs) have exhibited great potential in autonomously completing tasks across real-world applications. However, LLM agents introduce unexpected safety risks when operating in int | Overview: R-Judge: Benchmarking Safety Risk Awareness for LLM Agents Tongxin Yuan* , Zhiwei He∗, Lingzhong Dong, Yiming Wang, Ruijie Zhao, Tian Xia, Lizhen Xu, Binglin Zhou, Fangqi Li, Zhuosheng Zhang†, Rui Wan | Key Findings: Task Instruction: [1. Risk Identification] Analyze if agent actions are safe in above scenario. [2. Safety Judgment] Judge 'safe' or 'unsafe'. [2. Saf | Conclusions: Risk awareness is crucial for the safe execution of LLM agents in interactive environments. In this work, we present R-Judge, a general, realistic, an"
CONF-CC: "EMNLP 2024"
DATE_ADDED: 20260208
LLM_assessed: "GPT-4o, ChatGPT, GPT-4, Llama-2, Llama-3, Mistral, Vicuna"
DATA_URL: "https://github.com/Lordog/R-Judge"
CONFERENCE: "Journal"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 10
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: "US"
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark for ai safety"
data_metrics: "Not specified"
---
 R-Judge: A Benchmark for Evaluating the Reasoning and Judgment of Language Models

## Authors

[[Tongxin Yuan]], [[Zhiwei He]], [[Lingzhong Dong]], [[Yiming Wang]], [[Ruijie Zhao]], [[Tian Xia]], [[Lizhen Xu]], [[Binglin Zhou]], [[Fangqi Li]], [[Zhuosheng Zhang]], [[Rui Wang]], [[Gongshen Liu]]

## Links

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2024/2024-Yuan-R-Judge.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2401.10019

## Abstract

Large language models (LLMs) have exhibited great potential in autonomously completing tasks across real-world applications. Despite this, these LLM agents introduce unexpected safety risks when operating in interactive environments. Instead of centering on the harmlessness of LLM-generated content in most prior studies, this work addresses the imperative need for benchmarking the behavioral safety of LLM agents within diverse environments. We introduce R-Judge, a benchmark crafted to evaluate the proficiency of LLMs in judging and identifying safety risks given agent interaction records. R-Judge comprises 569 records of multi-turn agent interaction, encompassing 27 key risk scenarios among 5 application categories and 10 risk types. It is of high-quality curation with annotated safety labels and risk descriptions. Evaluation of 11 LLMs on R-Judge shows considerable room for enhancing the risk awareness of LLMs: The best-performing model, GPT-4o, achieves 74.42% while no other models significantly exceed the random. Moreover, we reveal that risk awareness in open agent scenarios is a multi-dimensional capability involving knowledge and reasoning, thus challenging for LLMs. With further experiments, we find that fine-tuning on safety judgment significantly improve model performance while straightforward prompting mechanisms fail. R-Judge is publicly available at https://github.com/Lordog/R-Judge.

## Data Description

R-Judge is a benchmark dataset of 569 multi-turn agent interaction records spanning 27 risk scenarios across 5 application categories and 10 risk types, annotated with binary safety labels and risk descriptions, designed to evaluate LLMs' safety risk awareness as agent monitors.


## Notes


## Citation Info

99 citations (Semantic Scholar/arXiv) [2025-08-27]
