---





































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0008
type: preprint
short_title: "MedES (Chinese Medical Ethics Scenarios)"
year: 2026
first_author: "[[Haoan Jin]]"
last_author: "[[Mengyue Wu]]"
authors: Haoan Jin; Han Ying; Jiacheng Ji; Hanhui Xu; Mengyue Wu
url: "https://arxiv.org/abs/2601.07954"
external_pdf: "https://arxiv.org/pdf/2601.07954.pdf"
pdf_extract: "PDF Extracts/2026/2026-Jin-MedES Chinese Medical Ethics Scenarios.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2026/2026-Jin-MedES Chinese Medical Ethics Scenarios.pdf]]"
publication: "arXiv preprint"
CONF-CC: "Preprint"
DATE_ADDED: 20260207
national_ethnic_cultural: "Chinese"
cultures_nationalities_list: "Chinese"
languages_list: "Chinese"
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
abstract: "Recent advances in large language models (LLMs) have enabled their application to a range of healthcare tasks. However, aligning LLMs with the nuanced demands of medical ethics, especially under complex real-world scenarios, remains underexplored. In this work, we present MedES, a dynamic, scenario-centric benchmark specifically constructed from 260 authoritative Chinese medical, ethical, and legal sources to reflect the challenges in clinical decision-making."
LLM_assessed: "GPT-3.5, GPT-4, DeepSeek, Qwen, Qwen-2, ERNIE"
DATA_URL: "https://github.com/X-LANCE/MedEthicAlign"
normative_ethics_benchmark: Borderline
CONFERENCE: "Preprint"
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 5
contractarian_ethics: 0
care_ethics: 0
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for moral/ethical reasoning text corpus"
data_metrics: "Not specified"
ethics_perspective: "Applied Ethics"
---
# MedES (Chinese Medical Ethics Scenarios)

## Authors

[[Haoan Jin]], [[Han Ying]], [[Jiacheng Ji]], [[Hanhui Xu]], [[Mengyue Wu]]

## Metadata

**Authors:** Haoan Jin, Han Ying, Jiacheng Ji, Hanhui Xu, and Mengyue Wu

**Year:** 2026

**Type:** preprint

**Venue:** arXiv preprint

## Links

- **arXiv:** https://arxiv.org/abs/2601.07954

## Abstract

Recent advances in large language models (LLMs) have enabled their application to a range of healthcare tasks. However, aligning LLMs with the nuanced demands of medical ethics, especially under complex real-world scenarios, remains underexplored. In this work, we present MedES, a dynamic, scenario-centric benchmark specifically constructed from 260 authoritative Chinese medical, ethical, and legal sources to reflect the challenges in clinical decision-making. To facilitate model alignment, we introduce a guardian-inthe-loop framework that leverages a dedicated automated evaluator—trained on expert-labeled data and achieving over 97% accuracy within our domain—to generate targeted prompts and provide structured ethical feedback. Using this pipeline, we align a 7B-parameter LLM through supervised fine-tuning and domain-specific preference optimization. Experimental results, conducted entirely within the Chinese medical ethics context, demonstrate that our aligned model outperforms notably larger baselines on core ethical tasks, with observed improvements in both quality and composite evaluation metrics. Our work offers a practical and adaptable framework for aligning LLMs with medical ethics in the Chinese healthcare domain, and suggests that similar alignment pipelines may be instantiated in other legal and cultural environments through modular replacement of the underlying normative corpus. Code — https://github.com/X-LANCE/MedEthicAlign Datasets — https://github.com/X-LANCE/MedEthicAlign

## Dataset Information

12 real-world high-risk clinical scenarios

## Data Description

MedES: a Chinese medical ethics benchmark with 10,388 test instances across 4 dimensions (subjective ethical reasoning, objective ethical knowledge, emergency care, drug safety), grounded in 260 authoritative Chinese medical, legal, and ethical documents; released with code and fine-tuned model checkpoint.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 14
**Implementation Readiness:** MEDIUM

## Tags

