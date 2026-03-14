---






























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0113
type: preprint
short_title: S-Eval
year: 2025
first_author: "[[Yuan, Xiaohan]]"
last_author: "[[Wang, Jingyi]]"
authors: "Yuan, Xiaohan; Li, Jinfeng; Wang, Dongxia; Chen, Yuefeng; Mao, Xiaofeng; Huang, Longtao; Chen, Jialuo; Xue, Hui; Liu, Xiaoxia; Wang, Wenhai; Ren, Kui; Wang, Jingyi"
authors_incomplete: false
url: "https://arxiv.org/abs/2405.14191"
external_pdf: "https://arxiv.org/pdf/2405.14191.pdf"
pdf_extract: "PDF Extracts/2025/2025-Yuan-S-Eval.md"
local_pdf: "[[PDFs/2025/2025-Yuan-S-Eval.pdf]]"
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
abstract: "Generative large language models (LLMs) have revolutionized natural language processing with their transformative and emergent capabilities. However, recent evidence indicates that LLMs can produce harmful content that violates social norms, raising significant concerns regarding the safety and ethical ramifications of deploying these advanced models. Thus, it is both critical and imperative to perform a rigorous and comprehensive safety evaluation of LLMs before deployment."
LLM_assessed: "GPT-4, Gemini, Gemma, LLaMA, Mistral, Qwen, Vicuna, ERNIE, ChatGLM, Baichuan, Yi"
DATA_URL: "https://github.com/IS2Lab/S-Eval"
research_topic: "Other"
CONFERENCE: "Preprint"
ethics_overall: 15
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: Yes
data_description: "Benchmark for moral/ethical reasoning"
data_metrics: "220,000 test cases"
---
# S-Eval

## Authors

[[Yuan, Xiaohan]], [[Li, Jinfeng]], [[Wang, Dongxia]], [[Chen, Yuefeng]], [[Mao, Xiaofeng]], [[Huang, Longtao]], [[Chen, Jialuo]], [[Xue, Hui]], [[Liu, Xiaoxia]], [[Wang, Wenhai]], [[Ren, Kui]], [[Wang, Jingyi]]

## Metadata

**Authors:** Yuan, Xiaohan; Li, Jinfeng; Wang, Dongxia; Chen, Yuefeng; Mao, Xiaofeng; Huang, Longtao; Chen, Jialuo; Xue, Hui; Liu, Xiaoxia; Wang, Wenhai; Ren, Kui; Wang, Jingyi

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2405.14191
- **Code/Data:** https://github.com/IS2Lab/S-Eval

## Abstract

Generative large language models (LLMs) have revolutionized natural language processing with their transformative and emergent capabilities. However, recent evidence indicates that LLMs can produce harmful content that violates social norms, raising significant concerns regarding the safety and ethical ramifications of deploying these advanced models. Thus, it is both critical and imperative to perform a rigorous and comprehensive safety evaluation of LLMs before deployment. Despite this need, owing to the extensiveness of LLM generation space, it still lacks a unified and standardized risk taxonomy to systematically reflect the LLM content safety, as well as automated safety assessment techniques to explore the potential risk efficiently. To bridge the striking gap, we propose S-Eval, a novel LLMbased automated Safety Evaluation framework with a newly defined comprehensive risk taxonomy. S-Eval incorporates two key components, i.e., an expert testing LLM M𝑡and a novel safety critique LLM M𝑐. The expert testing LLM M𝑡is responsible for automatically generating test cases in accordance with the proposed risk taxonomy (including 8 risk dimensions and a total of 102 subdivided risks). The safety critique LLM M𝑐can provide quantitative and explainable safety evaluations for better risk awareness Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than ACM must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org. Conference’17, July 2017, Washington, DC, USA © 2025 Association for Computing Machinery. ACM ISBN 978-x-xxxx-xxxx-x/YY/MM...$15.00 https://doi.org/10.1145/nnnnnnn.nnnnnnn of LLMs. In contrast to prior works, S-Eval differs in significant ways: (i) efficient – we construct a multi-dimensional and openended benchmark1 comprising 220,000 test cases across 102 risks utilizing M𝑡and conduct safety evaluations for 21 influential LLMs via M𝑐on our benchmark. The entire process is fully automated and requires no human involvement. (ii) effective – extensive validations show S-Eval facilitates a more thorough assessment and better perception of potential LLM risks, and M𝑐not only accurately quantifies the risks of LLMs but also provides explainable and in-depth insight into their safety, surpassing comparable models such as LLaMA-Guard-2. (iii) adaptive – S-Eval can be flexibly configured and adapted to the rapid evolution of LLMs and accompanying new safety threats, test generation methods and safety critique methods thanks to the LLM-based architecture. We further study the impact of hyper-parameters...

## Dataset Information

220,000 evaluation prompts total

## Data Description

S-Eval releases a comprehensive safety evaluation benchmark of 220,000 test cases (20,000 base risk prompts and 200,000 attack prompts) spanning 102 risk subcategories across 8 dimensions, in both Chinese and English. The benchmark is publicly available and designed for adaptive extension.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 16
**Implementation Readiness:** HIGH

## Tags

