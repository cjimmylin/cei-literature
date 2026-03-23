---






































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0012
type: preprint
short_title: PsychEthicsBench
year: 2026
first_author: "[[Shen, Yaling]]"
last_author: "[[Ge, Zongyuan]]"
authors: "Shen, Yaling; Fong, Stephanie; Jiang, Yiwen; Wang, Zimu; Tang, Feilong; Xu, Qingyang; Zhao, Xiangyu; Xu, Zhongxing; Liu, Jiahe; Hu, Jinpeng; Dwyer, Dominic; Ge, Zongyuan"
authors_incomplete: false
url: "https://arxiv.org/abs/2601.03578"
external_pdf: "https://arxiv.org/pdf/2601.03578.pdf"
pdf_extract: "PDF Extracts/2026/2026-Shen-PsychEthicsBench.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2026/2026-Shen-PsychEthicsBench.pdf]]"
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
abstract: "The increasing integration of large language models (LLMs) into mental health applications necessitates robust frameworks for evaluating professional safety alignment. Current evaluative approaches primarily rely on refusal-based safety signals, which offer limited insight into the nuanced behaviors required in clinical practice. In mental health, clinically inadequate refusals can be perceived as unempathetic and discourage help-seeking."
LLM_assessed: "Qwen, Llama-3, Llama-2"
DATA_URL: "https://github.com/ElsieSHEN/PsychEthicsBench"
normative_ethics_benchmark: Borderline
research_topic: "Other"
CONFERENCE: "Preprint"
ethics_overall: 60
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 5
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark for moral/ethical reasoning"
data_metrics: "Not specified"
ethics_perspective: "AI Safety & Alignment"
---
# PsychEthicsBench

## Authors

[[Shen, Yaling]], [[Fong, Stephanie]], [[Jiang, Yiwen]], [[Wang, Zimu]], [[Tang, Feilong]], [[Xu, Qingyang]], [[Xiangyu Zhao|Zhao, Xiangyu]], [[Xu, Zhongxing]], [[Liu, Jiahe]], [[Hu, Jinpeng]], [[Dwyer, Dominic]], [[Ge, Zongyuan]]

## Metadata

**Authors:** Shen, Yaling; Fong, Stephanie; Jiang, Yiwen; Wang, Zimu; Tang, Feilong; Xu, Qingyang; Zhao, Xiangyu; Xu, Zhongxing; Liu, Jiahe; Hu, Jinpeng; Dwyer, Dominic; Ge, Zongyuan

**Year:** 2026

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2601.03578
- **Code/Data:** https://github.com/ElsieSHEN/PsychEthicsBench](https://github.com/ElsieSHEN/PsychEthicsBench

## Abstract

The increasing integration of large language models (LLMs) into mental health applications necessitates robust frameworks for evaluating professional safety alignment. Current evaluative approaches primarily rely on refusal-based safety signals, which offer limited insight into the nuanced behaviors required in clinical practice. In mental health, clinically inadequate refusals can be perceived as unempathetic and discourage help-seeking. To address this gap, we move beyond refusal-centric metrics and introduce PsychEthicsBench, the first principlegrounded benchmark based on Australian psychology and psychiatry guidelines, designed to evaluate LLMs’ ethical knowledge and behavioral responses through multiple-choice and open-ended tasks with fine-grained ethicality annotations1. Empirical results across 14 models reveal that refusal rates are poor indicators of ethical behavior, revealing a significant divergence between safety triggers and clinical appropriateness. Notably, we find that domain-specific fine-tuning can degrade ethical robustness, as several specialized models underperform their base backbones in ethical alignment. PsychEthicsBench provides a foundation for systematic, jurisdiction-aware evaluation of LLMs in mental health, encouraging more responsible development in this domain.

## Dataset Information

Size: 392 ethical principles; 1,377 multiple-choice questions; 2,612 open-ended questions

## Data Description

PsychEthicsBench is a principle-grounded benchmark for evaluating ethical knowledge and behavioral responses of LLMs in mental health, based on 392 ethical principles from Australian psychology and psychiatry guidelines. The benchmark comprises 1,377 multiple-choice questions and 2,612 open-ended questions. A total of 14 models were evaluated across three groups (mental health LLMs, base models, and medical variants), including Qwen2.5-7B/14B, Llama3-8B, Llama2-13B, and their domain-specific fine-tuned derivatives.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 5, Agent 14
**Implementation Readiness:** HIGH

## Tags

