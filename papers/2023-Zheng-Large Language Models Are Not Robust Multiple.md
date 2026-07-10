---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: Y6YWT6FH
type: conferencePaper
short_title: "Large Language Models Are Not Robust Multiple"
year: 2025
first_author: "[[Chujie Zheng]]"
last_author: "[[Minlie Huang]]"
authors: "Chujie Zheng; Hao Zhou; Fandong Meng; Jie Zhou; Minlie Huang"
doi: 10.48550/arXiv.2309.03882
tags: 
url: "http://arxiv.org/abs/2309.03882"
external_pdf: "http://arxiv.org/pdf/2309.03882.pdf"
publication: "International Conference on Learning Representations"
CONF-CC: "ICLR 2023"
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: English
religious_values: N/A
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
religious_values_list: N/A
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
newtags: "Bias & Fairness"
key_contribution: "Showed LLMs have 'selection bias' (preferring Option A over B arbitrarily) in multiple-choice questions due to token priors, proposing 'PriDe' debiasing."
significance: "Reveals a fundamental flaw in MCQ-based evaluation (which most safety benchmarks use), questioning the validity of many reported scores."
pdf_extract: "PDF Extracts/2023/2023-Zheng-Large Language Models Are Not Robust Multiple.md"
abstract: "Multiple choice questions (MCQs) serve as a common yet important task format in the evaluation of large language models (LLMs). This work shows that modern LLMs are vulnerable to option position changes in MCQs due to their inherent “selection bias”, namely, they prefer to select specific option IDs as answers (like “Option A”). Through extensive empirical analyses with 20 LLMs on three benchmarks, we pinpoint that this behavioral bias primarily stems from LLMs’ token bias, where the model a..."
paper_summary: "Abstract: Multiple choice questions (MCQs) serve as a common yet important task format in the evaluation of large language models (LLMs). This work shows that modern LLMs are vulnerable to option position chang | Overview: Published as a conference paper at ICLR 2024 LARGE LANGUAGE MODELS ARE NOT ROBUST MULTIPLE CHOICE SELECTORS Chujie Zheng† Hao Zhou‡ Fandong Meng‡ Jie Zhou‡ Minlie Huang†∗ †The CoAI Group, DCST, BNRist | Methodology: 3.1 PERMUTATION-BASED DEBIASING BASELINE AND FORMULATION Before proposing our debiasing method, we first introduce a strong permutation-based debiasin | Key Findings: Our evaluation protocol follows the mainstream LLM evaluation frameworks, such as HuggingFace LLM Leaderboard, EleutherAI lm-harness, the original MML | Conclusions: This work studies the inherent selection bias of large language models (LLMs), which makes them vulnerable to option position changes in multiple choi"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2023/2023-Zheng-Large Language Models Are Not Robust Multiple.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: "ChatGPT, Falcon, LLaMA, Llama-2, Vicuna"
DATA_URL: "https://github.com/chujiezheng/LLM-MCQ-Bias"
CONFERENCE: "ICLR 2023"
ethics_overall: No
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Bias & Fairness"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: CN
author_region: "East Asia"
author_global_north_south: Ambiguous
weird_score: 36
is_benchmark: Yes
is_eval: Yes
is_dataset: No
data_description: "Benchmark for bias and fairness"
data_metrics: "Not specified"
---
# Large Language Models Are Not Robust Multiple Choice Selectors

## Metadata

**Authors:** Zheng, Chujie; Zhou, Hao; Meng, Fandong; Zhou, Jie; Huang, Minlie

**Year:** 2024

**Type:** preprint

**DOI:** [10.48550/arXiv.2309.03882](https://doi.org/10.48550/arXiv.2309.03882)

**Publisher:** arXiv

## Links

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2023/2023-Zheng-Large Language Models Are Not Robust Multiple.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2309.03882
- **DOI:** https://doi.org/10.48550/arXiv.2309.03882

## Abstract

Multiple choice questions (MCQs) serve as a common yet important task format in the evaluation of large language models (LLMs). This work shows that modern LLMs are vulnerable to option position changes in MCQs due to their inherent "selection bias", namely, they prefer to select specific option IDs as answers (like "Option A"). Through extensive empirical analyses with 20 LLMs on three benchmarks, we pinpoint that this behavioral bias primarily stems from LLMs' token bias, where the model a priori assigns more probabilistic mass to specific option ID tokens (e.g., A/B/C/D) when predicting answers from the option IDs. To mitigate selection bias, we propose a label-free, inference-time debiasing method, called PriDe, which separates the model's prior bias for option IDs from the overall prediction distribution. PriDe first estimates the prior by permutating option contents on a small number of test samples, and then applies the estimated prior to debias the remaining samples. We demonstrate that it achieves interpretable and transferable debiasing with high computational efficiency. We hope this work can draw broader research attention to the bias and robustness of modern LLMs.

## Authors

[[Chujie Zheng]], [[Hao Zhou]], [[Fandong Meng]], [[Jie Zhou]], [[Minlie Huang]]

## Data Description

Code and analysis for investigating selection bias in LLMs on multiple choice questions, with the PriDe debiasing method.


## Notes


## Tags

#Computer-Science---Computation-and-Language

## Citation Info

91 citations (Semantic Scholar/arXiv) [2025-08-27] 273 citations (Semantic Scholar/DOI) [2025-08-27] 270 citations (Semantic Scholar/DOI) [2025-08-23]
