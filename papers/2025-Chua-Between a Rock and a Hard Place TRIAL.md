---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0028
type: preprint
short_title: "Between a Rock and a Hard Place (TRIAL)"
year: 2025
first_author: "[[Shei Pern Chua]]"
last_author: "[[Xiaolin Hu]]"
authors: "Shei Pern Chua; Zhen Leng Thai; Kai Jun Teh; Xiao Li; Qibing Ren; Xiaolin Hu"
url: "https://arxiv.org/abs/2509.05367"
external_pdf: "https://arxiv.org/pdf/2509.05367.pdf"
pdf_extract: "PDF Extracts/2025/2025-Chua-Between a Rock and a Hard Place TRIAL.md"
local_pdf: "[[Lit-WS-PDFs/2025/2025-Chua-Between a Rock and a Hard Place TRIAL.pdf]]"
publication: "arXiv preprint"
CONF-CC: Preprint
DATE_ADDED: 20260207
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: 
religious_values: Jainism
rv_islam: 0
rv_christianity: 0
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 50
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: Jainism
mp_mft: 0
mp_schwartz: 0
mp_trolley: 50
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "Trolley / Dilemmas (Psych)"
newtags: 
tags: 
abstract: "Warning: This paper contains potentially offensive and harmful text. Large Language Model safety alignment predominantly operates on a binary assumption that requests are either safe or unsafe. This classification proves insufficient when models encounter ethical dilemmas, where the capacity to reason through moral trade-offs creates a distinct attack surface. We formalize this vulnerability through TRIAL, a multi-turn red-teaming methodology that embeds harmful requests within ethical framings."
LLM_assessed: "Claude-3 Sonnet, DeepSeek, GPT-3.5, GPT-4, GPT-4o, Llama-3, Mistral, Vicuna"
DATA_URL: NA
normative_ethics_benchmark: Borderline
CONFERENCE: Preprint
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 50
contractarian_ethics: 0
care_ethics: 0
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
is_benchmark: No
is_eval: Yes
is_dataset: No
data_description: "Evaluation framework"
data_metrics: "Not specified"
---
# Between a Rock and a Hard Place (TRIAL)

## Authors

[[Shei Pern Chua]], [[Zhen Leng Thai]], [[Kai Jun Teh]], [[Xiao Li]], [[Qibing Ren]], [[Xiaolin Hu]]

## Metadata

**Authors:** Shei Pern Chua, Zhen Leng Thai, Kai Jun Teh, Xiao Li, Qibing Ren, Xiaolin Hu

**Year:** 2025

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2509.05367

## Abstract

Warning: This paper contains potentially offensive and harmful text. Large Language Model safety alignment predominantly operates on a binary assumption that requests are either safe or unsafe. This classification proves insufficient when models encounter ethical dilemmas, where the capacity to reason through moral trade-offs creates a distinct attack surface. We formalize this vulnerability through TRIAL, a multi-turn red-teaming methodology that embeds harmful requests within ethical framings. TRIAL achieves high attack success rates across most tested models by systematically exploiting the model’s ethical reasoning capabilities to frame harmful actions as morally necessary compromises. Building on these insights, we introduce ERR (Ethical Reasoning Robustness), a defense framework that distinguishes between instrumental responses that enable harmful outcomes and explanatory responses that analyze ethical frameworks without endorsing harmful acts. ERR employs a Layer-Stratified HarmGated LoRA architecture, achieving robust defense against reasoning-based attacks while preserving model utility.

## Dataset Information

Multi-turn red-teaming methodology

## Data Description

This paper introduces TRIAL (Trolley-problem Reasoning for Interactive Attack Logic), a multi-turn red-teaming methodology that exploits LLMs' ethical reasoning capabilities by embedding harmful requests within trolley-problem ethical framings. The mechanistic analysis focuses on LLaMA-3.1-8B-Instruct and Mistral-7B-Instruct-v0.2, demonstrating a safety dissociation gap where early-layer harm detection is overridden by ethical reasoning circuits, and proposes ERR (Ethical Reasoning Robustness), a Layer-Stratified Harm-Gated LoRA defense framework.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 16
**Implementation Readiness:** MEDIUM

## Tags

