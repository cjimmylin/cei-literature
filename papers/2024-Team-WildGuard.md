---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EGFIC6AG
type: document
short_title: WildGuard
year: 2024
first_author: "[[Seungju Han]]"
last_author: "[[Nouha Dziri]]"
authors: "Seungju Han; Kavel Rao; Allyson Ettinger; Liwei Jiang; Bill Yuchen Lin; Nathan Lambert; Yejin Choi; Nouha Dziri"
url: "https://arxiv.org/abs/2406.18495"
external_pdf: "https://arxiv.org/pdf/2406.18495.pdf"
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
newtags: "AI Safety & Alignment"
key_contribution: "Introduced WildGuard, a lightweight and open moderation tool for LLM safety, along with WildGuardMix (a balanced 92k labeled multi-task safety dataset)."
significance: "Establishes a state-of-the-art open moderation baseline that rivals or exceeds GPT-4 in refusal detection and harmfulness identification, significantly enhancing the security of open LLM interfaces."
tags: 
pdf_extract: "PDF Extracts/2024/2024-Team-WildGuard.md"
abstract: "We introduce WILDGUARD—an open, light-weight moderation tool for LLM safety that achieves three goals: (1) identifying malicious intent in user prompts, (2) detecting safety risks of model responses, and (3) determining model refusal rate. Together, WILDGUARD serves the increasing needs for automatic safety moderation and evaluation of LLM interactions, providing a one-stop tool with enhanced accuracy and broad coverage across 13 risk categories. While existing open moderation tools such as Llam"
paper_summary: "Abstract: We introduce WILDGUARD—an open, light-weight moderation tool for LLM safety that achieves three goals: (1) identifying malicious intent in user prompts, (2) detecting safety risks of model responses,  | Overview: WILDGUARD: Open One-stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs Seungju Han∗♡♠ Kavel Rao∗♢ Allyson Ettinger†♡ Liwei Jiang†♡♢ Bill Yuchen Lin♡ Nathan Lambert♡ Yejin Choi♡♢  | Key Findings: framework for automated red teaming and robust refusal. arXiv preprint arXiv:2402.04249, 2024. [26] Meta. Meta llama guard 2: Model cards and prompt f | Conclusions: In this work, we introduce WILDGUARD, a unified multi-task open LLM safety moderation model capable of detecting diverse types of vanilla and adversar"
local_pdf: "[[Lit-WS-PDFs/2024/2024-Team-WildGuard.pdf]]"
LLM_assessed: "GPT-4, LLaMA, Mistral, Vicuna"
DATA_URL: "https://huggingface.co/datasets/allenai/wildguardmix, https://github.com/allenai/wildguard"
publication: "NeurIPS 2024"
CONF-CC: "NeurIPS 2024"
DATE_ADDED: 20260207
CONFERENCE: "NeurIPS 2024"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 5
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "AI Safety & Alignment"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: US
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Multi-task benchmark for ai safety annotated dataset"
data_metrics: "Not specified"
---
# WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs

## Metadata

**Authors:** Han, Seungju; Rao, Kavel; Ettinger, Allyson; Jiang, Liwei; Lin, Bill Yuchen; Lambert, Nathan; Choi, Yejin; Dziri, Nouha

**Year:** 2024

**Type:** document

## Links

- **Local PDF:** [[Lit-WS-PDFs/2024/2024-Team-WildGuard.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2406.18495

## Abstract

We introduce WildGuard -- an open, light-weight moderation tool for LLM safety that achieves three goals: (1) identifying malicious intent in user prompts, (2) detecting safety risks of model responses, and (3) determining model refusal rate. Together, WildGuard serves the increasing needs for automatic safety moderation and evaluation of LLM interactions, providing a one-stop tool with enhanced accuracy and broad coverage across 13 risk categories. While existing open moderation tools such as Llama-Guard2 score reasonably well in classifying straightforward model interactions, they lag far behind a prompted GPT-4, especially in identifying adversarial jailbreaks and in evaluating models' refusals, a key measure for evaluating safety behaviors in model responses. To address these challenges, we construct WildGuardMix, a large-scale and carefully balanced multi-task safety moderation dataset with 92K labeled examples that cover vanilla (direct) prompts and adversarial jailbreaks, paired with various refusal and compliance responses. WildGuardMix is a combination of WildGuardTrain, the training data of WildGuard, and WildGuardTest, a high-quality human-annotated moderation test set with 5K labeled items covering broad risk scenarios. Through extensive evaluations on WildGuardTest and ten existing public benchmarks, we show that WildGuard establishes state-of-the-art performance in open-source safety moderation across all the three tasks compared to ten strong existing open-source moderation models (e.g., up to 26.4% improvement on refusal detection). Importantly, WildGuard matches and sometimes exceeds GPT-4 performance (e.g., up to 3.9% improvement on prompt harmfulness identification). WildGuard serves as a highly effective safety moderator in an LLM interface, reducing the success rate of jailbreak attacks from 79.8% to 2.4%.

## Authors

[[Seungju Han]], [[Kavel Rao]], [[Allyson Ettinger]], [[Liwei Jiang]], [[Bill Yuchen Lin]], [[Nathan Lambert]], [[Yejin Choi]], [[Nouha Dziri]]

## Data Description

WILDGUARDMIX is a 92K-item multi-task safety moderation dataset covering vanilla and adversarial prompts paired with refusal/compliance responses across 13 risk categories; includes WILDGUARDTEST, a 5K human-annotated evaluation set.


## Notes


## Citation Info

124 citations (Semantic Scholar/arXiv) [2025-08-27]
