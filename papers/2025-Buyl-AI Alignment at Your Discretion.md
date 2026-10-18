---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0017
type: preprint
short_title: "AI Alignment at Your Discretion"
year: 2025
first_author: "[[Maarten Buyl]]"
last_author: "[[Flavio du Pin Calmon]]"
authors: "Maarten Buyl; Hadi Khalaf; Claudio Mayrink Verdun; Lucas Monteiro Paes; Caio C. Vieira Machado; Flavio du Pin Calmon"
doi: 10.1145/3715275.3732194
url: "https://arxiv.org/abs/2502.10441"
external_pdf: "https://arxiv.org/pdf/2502.10441.pdf"
pdf_extract: "PDF Extracts/2025/2025-Buyl-AI Alignment at Your Discretion.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Buyl-AI Alignment at Your Discretion.pdf]]"
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
abstract: "In AI alignment, extensive latitude must be granted to annotators, either human or algorithmic, to judge which model outputs are ‘better’ or ‘safer.’ We refer to this latitude as alignment discretion. Such discretion remains largely unexamined, posing two risks: (i) annotators may use their power of discretion arbitrarily, and (ii) models may fail to mimic this discretion. To study this phenomenon, we draw on legal concepts of discretion that structure how decision-making authority is conferred..."
LLM_assessed: "GPT-4o, DeepSeek, Claude-3 Sonnet, Llama-3, Mistral"
DATA_URL: NA
CONFERENCE: Preprint
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
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
weird_score: 80
is_benchmark: No
is_eval: Yes
is_dataset: Yes
data_description: "Evaluation approach dataset"
data_metrics: "Not specified"
---
# AI Alignment at Your Discretion

## Authors

[[Maarten Buyl]], [[Hadi Khalaf]], [[Claudio Mayrink Verdun]], [[Lucas Monteiro Paes]], [[Caio C. Vieira Machado]], [[Flavio du Pin Calmon]]

## Metadata

**Authors:** Maarten Buyl; Hadi Khalaf; Claudio Mayrink Verdun; Lucas Monteiro Paes; Caio C. Vieira Machado; Flavio du Pin Calmon

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**DOI:** [10.1145/3715275.3732194](https://doi.org/10.1145/3715275.3732194)

## Links

- **arXiv:** https://arxiv.org/abs/2502.10441
- **DOI:** https://doi.org/10.1145/3715275.3732194

## Abstract

In AI alignment, extensive latitude must be granted to annotators, either human or algorithmic, to judge which model outputs are ‘better’ or ‘safer.’ We refer to this latitude as alignment discretion. Such discretion remains largely unexamined, posing two risks: (i) annotators may use their power of discretion arbitrarily, and (ii) models may fail to mimic this discretion. To study this phenomenon, we draw on legal concepts of discretion that structure how decision-making authority is conferred and exercised, particularly in cases where principles conflict or their application is unclear or irrelevant. Extended to AI alignment, discretion is required when alignment principles and rules are (inevitably) conflicting or indecisive. We present a set of metrics to systematically analyze when and how discretion in AI alignment is exercised, such that both risks (i) and (ii) can be observed. Moreover, we distinguish between human and algorithmic discretion and analyze the discrepancy between them. By measuring both human and algorithmic discretion over safety alignment datasets, we reveal layers of discretion in the alignment process that were previously unaccounted for. Furthermore, we demonstrate how algorithms trained on these datasets develop their own forms of discretion in interpreting and applying these principles, which challenges the purpose of having any principles at all. Our paper presents the first step towards formalizing this core gap in current alignment processes, and we call on the community to further scrutinize and control alignment discretion. Warning: this paper contains example data that may be offensive, biased, and/or harmful Keywords AI alignment, AI safety, discretion, AI governance, judicial discretion

## Dataset Information

Metrics for analyzing discretion in preference datasets used for RLHF; audits across multiple alignment datasets

## Data Description

This paper analyzes alignment discretion using two existing preference datasets: Anthropic's HH-RLHF (harmlessness partition) and PKU's Safe-RLHF. The authors evaluate multiple algorithmic annotators including reward models (Llama-3 8B, Mistral-7B fine-tuned variants), LLMs (Llama-3 8B base and fine-tuned, Mistral-7B base and fine-tuned), and off-the-shelf models (GPT-4o, DeepSeek-V3, Claude 3.5 Sonnet) to measure discretion arbitrariness, principle supremacy, and discretion discrepancy against human annotator baselines.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 3
**Implementation Readiness:** MEDIUM

## Tags

