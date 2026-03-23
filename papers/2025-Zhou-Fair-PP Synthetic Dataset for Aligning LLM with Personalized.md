---



































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0275
type: preprint
short_title: "Fair-PP: Synthetic Dataset for Aligning LLM with Personalized Preferences of Social Equity"
year: 2025
first_author: "[[Zhou, Qi]]"
last_author: "[[Guo, Qing]]"
authors: "Zhou, Qi; Zhang, Jie; Wang, Dongxia; Liu, Qiang; Li, Tianlin; Dong, Jin Song; Wang, Wenhai; Guo, Qing"
authors_incomplete: false
url: "https://arxiv.org/abs/2505.11861"
external_pdf: "https://arxiv.org/pdf/2505.11861.pdf"
pdf_extract: "PDF Extracts/2025/2025-Zhou-Fair-PP Synthetic Dataset for Aligning LLM with Personalized.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Zhou-Fair-PP Synthetic Dataset for Aligning LLM with Personalized.pdf]]"
publication: arXiv
CONF-CC: "Preprint"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "Multiple Religions"
rv_islam: 50
rv_christianity: 50
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
religious_values_list: "Islam, Christianity"
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
abstract: "Human preference plays a crucial role in the refinement of large language models (LLMs). However, collecting human preference feedback is costly and most existing datasets neglect the correlation between personalization and preferences. To address this issue, we introduce FAIR-PP, a synthetic dataset of personalized preferences targeting social equity, derived from real-world social survey data, which includes 28 social groups, 98 equity topics, and 5 personal preference dimensions."
LLM_assessed: "Falcon, GPT-4o mini, Llama-3, Mistral, Qwen-2"
DATA_URL: "https://github.com/tools-only/FairPP, https://huggingface.co/datasets/tools-o/Fair-PP"
CONFERENCE: "Preprint"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 5
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Bias & Fairness"
is_benchmark: "No"
is_eval: Yes
is_dataset: "Yes"
data_description: "Dataset"
data_metrics: "Not specified"
---
# Fair-PP: Synthetic Dataset for Aligning LLM with Personalized Preferences of Social Equity

## Authors

[[Zhou, Qi]], [[Jie Zhang|Zhang, Jie]], [[Wang, Dongxia]], [[Liu, Qiang]], [[Li, Tianlin]], [[Dong, Jin Song]], [[Wang, Wenhai]], [[Guo, Qing]]

## Metadata

**Authors:** Zhou, Qi; Zhang, Jie; Wang, Dongxia; Liu, Qiang; Li, Tianlin; Dong, Jin Song; Wang, Wenhai; Guo, Qing

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2505.11861

## Abstract

Human preference plays a crucial role in the refinement of large language models (LLMs). However, collecting human preference feedback is costly and most existing datasets neglect the correlation between personalization and preferences. To address this issue, we introduce FAIR-PP, a synthetic dataset of personalized preferences targeting social equity, derived from real-world social survey data, which includes 28 social groups, 98 equity topics, and 5 personal preference dimensions. Leveraging GPT-4o-mini, we engage in role-playing based on seven representative persona portrayals guided by existing social survey data, yielding a total of 238,623 preference records. Through FAIR-PP, we also contribute (i) An automated framework for generating preference data, along with a more fine-grained dataset of personalized preferences; (ii) analysis of the positioning of the existing mainstream LLMs across five major global regions within the personalized preference space; and (iii) a sample reweighting method for personalized preference alignment, enabling alignment with a target persona while maximizing the divergence from other personas. Empirical experiments show our method outperforms the baselines. Code: github.com/tools-only/FairPP Dataset: huggingface.co/datasets/tools-o/Fair-PP

## Dataset Information

238,623 preference records across 28 social groups and 98 equity topics

## Data Description

FAIR-PP is a synthetic dataset of personalized preferences targeting social equity, comprising 238,623 samples across 28 social groups, 98 equity topics, and 5 preference dimensions, derived from real-world social survey data using GPT-4o-mini role-playing.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** HIGH

## Tags

