---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0012
type: preprint
short_title: PsychEthicsBench
year: 2025
first_author: "[[Shen, Yaling]]"
last_author: "[[Ge, Zongyuan]]"
authors: "[[Shen, Yaling]]; [[Fong, Stephanie]]; [[Jiang, Yiwen]]; [[Wang, Zimu]]; [[Tang, Feilong]]; [[Xu, Qingyang]]; [[Zhao, Xiangyu]]; [[Xu, Zhongxing]]; [[Liu, Jiahe]]; [[Hu, Jinpeng]]; [[Dwyer, Dominic]]; [[Ge, Zongyuan]]"
authors_incomplete: false
url: "https://arxiv.org/abs/2601.03578"
external_pdf: "https://arxiv.org/pdf/2601.03578.pdf"
pdf_extract: "PDF Extracts/0000/2026-Shen-PsychEthicsBench.md"
local_pdf: "[[PDFs/2026/2026-Shen-PsychEthicsBench.pdf]]"
publication: arXiv
DATE_ADDED: 20260207
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
national_ethnic_cultural: Australian/Aboriginal
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: 
is_benchmark: Yes
is_eval: Yes
is_dataset: No
tags: 
abstract: "The increasing integration of large language models (LLMs) into mental health applications necessitates robust frameworks for evaluating professional safety alignment. Current evaluative approaches primarily rely on refusal-based safety signals, which offer limited insight into the nuanced behaviors required in clinical practice. In mental health, clinically inadequate refusals can be perceived as unempathetic and discourage help-seeking."
ethics_perspective: "AI Safety & Alignment"
data_description: "Benchmark for moral/ethical reasoning"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, Claude, Qwen, Llama-3, Llama-2"
DATA_URL: "https://github.com/ElsieSHEN/PsychEthicsBench"
normative_ethics_benchmark: Borderline
---
# PsychEthicsBench

## Authors

[[Shen, Yaling]], [[Fong, Stephanie]], [[Jiang, Yiwen]], [[Wang, Zimu]], [[Tang, Feilong]], [[Xu, Qingyang]], [[Zhao, Xiangyu]], [[Xu, Zhongxing]], [[Liu, Jiahe]], [[Hu, Jinpeng]], [[Dwyer, Dominic]], [[Ge, Zongyuan]]

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

