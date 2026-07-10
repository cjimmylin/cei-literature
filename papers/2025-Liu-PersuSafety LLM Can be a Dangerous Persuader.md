---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0103
type: preprint
short_title: "PersuSafety: LLM Can be a Dangerous Persuader"
year: 2025
first_author: "[[Minqian Liu]]"
last_author: "[[Lifu Huang]]"
authors: "Minqian Liu; Zhiyang Xu; Xinyi Zhang; Heajun An; Sarvech Qadir; Qi Zhang; Pamela J. Wisniewski; Jin-Hee Cho; Sang Won Lee; Ruoxi Jia; Lifu Huang"
url: "https://arxiv.org/abs/2504.10430"
external_pdf: "https://arxiv.org/pdf/2504.10430.pdf"
pdf_extract: "PDF Extracts/2025/2025-Liu-PersuSafety LLM Can be a Dangerous Persuader.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Liu-PersuSafety LLM Can be a Dangerous Persuader.pdf]]"
publication: arXiv
CONF-CC: Preprint
DATE_ADDED: 20260207
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: 
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
newtags: 
tags: 
abstract: "Recent advancements in Large Language Models (LLMs) have enabled them to approach human-level persuasion capabilities. However, such potential also raises concerns about the safety risks of LLM-driven persuasion, particularly their potential for unethical influence through manipulation, deception, exploitation of vulnerabilities, and many other harmful tactics. In this work, we present a systematic investigation of LLM persuasion safety through two critical aspects: (1) whether LLMs..."
LLM_assessed: "Claude, GPT-4o, GPT-4o mini, Llama-3, Mistral, Qwen"
DATA_URL: "https://github.com/PLUM-Lab/PersuSafety"
CONFERENCE: Preprint
ethics_overall: No
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "AI Safety & Alignment"
nw_confucian: 5
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
is_benchmark: No
is_eval: Yes
is_dataset: No
data_description: "Evaluation framework"
data_metrics: "Not specified"
---
# PersuSafety: LLM Can be a Dangerous Persuader

## Authors

[[Minqian Liu]], [[Zhiyang Xu]], [[Xinyi Zhang]], [[Heajun An]], [[Sarvech Qadir]], [[Qi Zhang]], [[Pamela J. Wisniewski]], [[Jin-Hee Cho]], [[Sang Won Lee]], [[Ruoxi Jia]], [[Lifu Huang]]

## Metadata

**Authors:** Minqian Liu; Zhiyang Xu; Xinyi Zhang; Heajun An; Sarvech Qadir; Qi Zhang; Pamela J. Wisniewski; Jin-Hee Cho; Sang Won Lee; Ruoxi Jia; Lifu Huang

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2504.10430
- **Code/Data:** https://github.com/PLUM-Lab/PersuSafety

## Abstract

Recent advancements in Large Language Models (LLMs) have enabled them to approach human-level persuasion capabilities. However, such potential also raises concerns about the safety risks of LLM-driven persuasion, particularly their potential for unethical influence through manipulation, deception, exploitation of vulnerabilities, and many other harmful tactics. In this work, we present a systematic investigation of LLM persuasion safety through two critical aspects: (1) whether LLMs appropriately reject unethical persuasion tasks and avoid unethical strategies during execution, including cases where the initial persuasion goal appears ethically neutral, and (2) how influencing factors like personality traits and external pressures affect their behavior. To this end, we introduce PERSUSAFETY, the first comprehensive framework for the assessment of persuasion safety, which consists of three stages, i.e., persuasion scene creation, persuasive conversation simulation, and persuasion safety assessment. PERSUSAFETY covers 6 diverse unethical persuasion topics and 15 common unethical strategies. Through extensive experiments across 8 widely used LLMs, we observe significant safety concerns in most LLMs, including failing to identify harmful persuasion tasks and leveraging various unethical persuasion strategies. Our study calls for more attention to improve safety alignment in progressive and goal-driven conversations such as persuasion.

## Dataset Information

6 unethical persuasion topics x 15 unethical strategies; three-stage framework (scene creation, conversation simulation, safety assessment); multi-turn conversation format

## Data Description

Constructs and releases PERSUSAFETY, a dataset of 472 unethical and 100 ethically neutral persuasion tasks across 6 topics and 15 fine-grained unethical persuasion strategies, synthesized with OpenAI-o1 and validated via human-in-the-loop review.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 18
**Implementation Readiness:** HIGH

## Tags

