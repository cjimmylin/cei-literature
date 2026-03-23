---



































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: RGWMSH7F
type: journalArticle
short_title: "Controllable Preference Optimization"
year: 2024
first_author: "[[Yiju Guo]]"
last_author: "[[Maosong Sun]]"
authors: "Yiju Guo; Ganqu Cui; Lifan Yuan; Ning Ding; Zexu Sun; Bowen Sun; Huimin Chen; Ruobing Xie; Jie Zhou; Yankai Lin; Zhiyuan Liu; Maosong Sun"
url: "https://arxiv.org/abs/2402.19085"
external_pdf: "https://arxiv.org/pdf/2402.19085.pdf"
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
newtags: "AI Safety & Alignment"
key_contribution: "Introduced Controllable Preference Optimization (CPO), a method to explicitly specify preference scores for different objectives (helpfulness, honesty, harmlessness) during training."
significance: "Mitigates the 'alignment tax' by allowing multi-objective control, enabling developers to tune models for different trade-offs depending on the application context."
tags: 
osint_source: "Recovered via HTML"
pdf_extract: "PDF Extracts/2024/2024-Liu-Controllable Preference Optimization.md"
abstract: "Alignment in artificial intelligence pursues the consistency between model responses and human preferences as well as values. In practice, the multifaceted nature of human preferences inadvertently introduces what is known as the “alignment tax”–a compromise where enhancements in alignment within one objective (e.g., harmlessness) can diminish performance in others (e.g., helpfulness). However, existing alignment techniques are mostly unidirectional, leading to sub-optimal trade-offs and poor..."
paper_summary: "Abstract: Alignment in artificial intelligence pursues the consistency between model responses and hu- man preferences as well as values. In prac- tice, the multifaceted nature of human prefer- ences inadverten | Overview: Controllable Preference Optimization: Toward Controllable Multi-Objective Alignment Yiju Guo*1, Ganqu Cui∗2, Lifan Yuan2, Ning Ding2, Zexu Sun1, Bowen Sun2, Huimin Chen2, Ruobing Xie3, Jie Zhou3, Yank | Methodology: In this section, we propose a controllable pref- erence optimization (CPO) algorithm, of which the main idea is to determine the optimization di- rect | Key Findings: In this section, we compare the highest perfor- mances of CPO with baselines to assess how it benefits open-source LLMs. We evaluate the ef- fectivene | Conclusions: This paper manages to alleviate the performance trade-off problem in LLM alignment. From the view of controllability, we find explicit condition- ing"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2024/2024-Liu-Controllable Preference Optimization.pdf]]"
CONF-CC: "EMNLP 2024"
DATE_ADDED: 20260208
LLM_assessed: Mistral
DATA_URL: "https://huggingface.co/datasets/openbmb/UltraSafety"
CONFERENCE: "Journal"
ethics_overall: 15
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 10
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "No"
is_dataset: Yes
data_description: "N/A"
data_metrics: "Not specified"
---
# Controllable Preference Optimization: Toward Controllable Multi-Objective Alignment

## Metadata

**Authors:** Guo, Yiju; Cui, Ganqu; Yuan, Lifan; Ding, Ning; Sun, Zexu; Sun, Bowen; Chen, Huimin; Xie, Ruobing; Zhou, Jie; Lin, Yankai; Liu, Zhiyuan; Sun, Maosong

**Year:** 2024

**Publication:** arXiv preprint

**Type:** journalArticle

## Links

- **Local PDF:** [[Lit-WS-Lit-WS-PDFs/2024/2024-Liu-Controllable Preference Optimization.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2402.19085

## Abstract

Alignment in artificial intelligence pursues the consistency between model responses and human preferences as well as values. In practice, the multifaceted nature of human preferences inadvertently introduces what is known as the "alignment tax" -a compromise where enhancements in alignment within one objective (e.g.,harmlessness) can diminish performance in others (e.g.,helpfulness). However, existing alignment techniques are mostly unidirectional, leading to suboptimal trade-offs and poor flexibility over various objectives. To navigate this challenge, we argue the prominence of grounding LLMs with evident preferences. We introduce controllable preference optimization (CPO), which explicitly specifies preference scores for different objectives, thereby guiding the model to generate responses that meet the requirements. Our experimental analysis reveals that the aligned models can provide responses that match various preferences among the "3H" (helpfulness, honesty, harmlessness) desiderata. Furthermore, by introducing diverse data and alignment goals, we surpass baseline methods in aligning with single objectives, hence mitigating the impact of the alignment tax and achieving improvements in multi-objective alignment.

## Authors

[[Yiju Guo]], [[Ganqu Cui]], [[Lifan Yuan]], [[Ning Ding]], [[Zexu Sun]], [[Bowen Sun]], [[Huimin Chen]], [[Ruobing Xie]], [[Jie Zhou]], [[Yankai Lin]], [[Zhiyuan Liu]], [[Maosong Sun]]

## Data Description

UltraSafety preference dataset for jailbreak safety alignment, containing prompt-completion pairs with safety scores for training controllable multi-objective aligned LLMs.


## Notes


## Citation Info

3 citations (Semantic Scholar/arXiv) [2025-08-27] _eprint: 2402.19085
