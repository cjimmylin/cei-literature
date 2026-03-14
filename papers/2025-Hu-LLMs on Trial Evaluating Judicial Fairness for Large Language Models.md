---





































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0072
type: preprint
short_title: "LLMs on Trial: Evaluating Judicial Fairness for Large Language Models (JudiFair)"
year: 2025
first_author: "[[Yiran Hu]]"
last_author: "[[Weixing Shen]]"
authors: "Yiran Hu; Zongyue Xue; Haitao Li; Siyuan Zheng; Qingjing Chen; Shaochun Wang; Xihan Zhang; Ning Zheng; Yun Liu; Qingyao Ai; Yiqun Liu; Charles L.A. Clarke; Weixing Shen"
url: "https://arxiv.org/abs/2507.10852"
external_pdf: "https://arxiv.org/pdf/2507.10852.pdf"
pdf_extract: "PDF Extracts/2025/2025-Hu-LLMs on Trial Evaluating Judicial Fairness for Large Language Models.md"
local_pdf: "[[PDFs/2025/2025-Hu-LLMs on Trial Evaluating Judicial Fairness for Large Language Models.pdf]]"
publication: arXiv
CONF-CC: "Preprint"
DATE_ADDED: 20260207
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
newtags: 
tags: 
abstract: "Large Language Models (LLMs) are increasingly used in high-stakes fields where their decisions impact rights and equity. However, LLMs’ judicial fairness and implications for social justice remain underexplored. When LLMs act as judges, the ability to fairly resolve judicial issues is a prerequisite to ensure their trustworthiness. Based on theories of judicial fairness, we construct a comprehensive framework to measure LLM fairness, leading to a selection of 65 labels and 161 corresponding..."
LLM_assessed: "DeepSeek, GLM, Gemini, Llama-3, Mistral, Phi, Qwen, Qwen-2"
DATA_URL: "https://github.com/THUYRan/LLM-Fairness"
CONFERENCE: "Preprint"
ethics_overall: 95
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
is_benchmark: Yes
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation framework dataset"
data_metrics: "Not specified"
ethics_perspective: "Bias & Fairness"
---
# LLMs on Trial: Evaluating Judicial Fairness for Large Language Models (JudiFair)

## Authors

[[Yiran Hu]], [[Zongyue Xue]], [[Haitao Li]], [[Siyuan Zheng]], [[Qingjing Chen]], [[Shaochun Wang]], [[Xihan Zhang]], [[Ning Zheng]], [[Yun Liu]], [[Qingyao Ai]], [[Yiqun Liu]], [[Charles L.A. Clarke]], [[Weixing Shen]]

## Metadata

**Authors:** Hu et al.

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2507.10852

## Abstract

Large Language Models (LLMs) are increasingly used in high-stakes fields where their decisions impact rights and equity. However, LLMs’ judicial fairness and implications for social justice remain underexplored. When LLMs act as judges, the ability to fairly resolve judicial issues is a prerequisite to ensure their trustworthiness. Based on theories of judicial fairness, we construct a comprehensive framework to measure LLM fairness, leading to a selection of 65 labels and 161 corresponding values. Applying this framework to the judicial system, we compile an extensive dataset, JudiFair, comprising 177,100 unique case facts. To achieve robust statistical inference, we develop three evaluation metrics—inconsistency, bias, and imbalanced inaccuracy—and introduce a method to assess the overall fairness of multiple LLMs across various labels. Through experiments with 16 LLMs, we uncover pervasive inconsistency, bias, and imbalanced inaccuracy across models, underscoring severe LLM judicial unfairness. Particularly, LLMs display notably more pronounced biases on demographic labels, with slightly less bias on substance labels compared to procedure ones. Interestingly, increased inconsistency correlates with reduced biases, but more accurate predictions exacerbate biases. While we find that adjusting the temperature parameter can influence LLM fairness, model size, release date, and country of origin do not exhibit significant effects on judicial fairness. Accordingly, we introduce a publicly available toolkit1, designed to support future research in evaluating and improving LLM fairness.

## Dataset Information

JudiFair dataset: 177,100 unique case facts

## Data Description

JudiFair is an evaluation benchmark comprising 177,100 unique counterfactual case facts derived from 1,100 Chinese judicial documents, annotated with 65 extra-legal labels and 161 label values for LLM judicial fairness evaluation.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 6
**Implementation Readiness:** HIGH

## Tags

