---
key: INNOVATION-P114
type: preprint
short_title: "Value-Conflict Diagnostics Reveal Widespread Alignment Faking in Language Models"
year: 2026
first_author: "[[Inderjeet Nair]]"
authors: "Inderjeet Nair; Jie Ruan; Lu Wang"
url: "https://arxiv.org/abs/2604.20995"
external_pdf: "https://arxiv.org/pdf/2604.20995.pdf"
abstract: "Alignment faking, where a model behaves aligned with developer policy when monitored but reverts to its own preferences when unobserved, is a concerning yet poorly understood phenomenon, in part because current diagnostic tools remain limited. Prior diagnostics rely on highly toxic and clearly harmful scenarios, causing most models to refuse immediately. As a result, models never deliberate over developer policy, monitoring conditions, or the consequences of non-compliance, making these diagnostics fundamentally unable to detect alignment faking propensity. To support study of this phenomenon, we first introduce VLAF, a diagnostic framework grounded in the hypothesis that alignment faking is most likely when developer policy conflicts with a model's strongly held values. VLAF uses morally unambiguous scenarios to probe this conflict across diverse moral values, bypassing refusal behavior while preserving meaningful deliberative stakes. Using VLAF, we find that alignment faking is substantially more prevalent than previously reported, occurring in models as small as 7B parameters - with olmo2-7b-instruct faking alignment in 37% of cases. Finally, we show that oversight conditions induce activation shifts that lie along a single direction in representation space. This means the behavioral divergence driving alignment faking can be captured by a single contrastive steering vector, which we exploit for lightweight inference-time mitigation. Finally, we exploit this for mitigation that requires no labeled data and minimal computational overhead, achieving relative reductions in alignment faking of 85.8%, 94.0%, and 57.7% on olmo2-7b-instruct, olmo2-13b-instruct, and qwen3-8b respectively."
ethics_overall: 75
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
care_ethics: 0
contractarian_ethics: 0
ethics_perspective: "AI Safety & Alignment"
national_ethnic_cultural: N/A
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
is_benchmark: No
is_eval: Yes
is_dataset: No
data_description: "Not specified"
data_metrics: "Not specified"
newtags: "AI Safety & Alignment"
key_contribution: 
significance: 
paper_summary: 
local_pdf: "[[Lit-WS-PDFs/2026/2026-Nair-Value-Conflict Diagnostics for Faking.pdf]]"
pdf_extract: "PDF Extracts/2026/2026-Nair-Value-Conflict Diagnostics for Faking.md"
tags: 
Human View: 
Human View Date: 
Human View note: 
Not AI: 
DATE_ADDED: 20260709
innovation_gap: G-15
last_author: "[[Lu Wang]]"
CONF-CC: Preprint
LLM_assessed: "olmo2-7b-instruct, olmo2-13b-instruct, qwen3-8b and other qwen3-family models (full list not in extract)"
---

# Value-Conflict Diagnostics Reveal Widespread Alignment Faking in Language Models

## Metadata

**Authors:** Inderjeet Nair; Jie Ruan; Lu Wang

**Year:** 2026

**Type:** preprint

**arXiv:** https://arxiv.org/abs/2604.20995

**Gap:** G-15 — AI Safety & Alignment

## Abstract

Alignment faking, where a model behaves aligned with developer policy when monitored but reverts to its own preferences when unobserved, is a concerning yet poorly understood phenomenon, in part because current diagnostic tools remain limited. Prior diagnostics rely on highly toxic and clearly harmful scenarios, causing most models to refuse immediately. As a result, models never deliberate over developer policy, monitoring conditions, or the consequences of non-compliance, making these diagnostics fundamentally unable to detect alignment faking propensity. To support study of this phenomenon, we first introduce VLAF, a diagnostic framework grounded in the hypothesis that alignment faking is most likely when developer policy conflicts with a model's strongly held values. VLAF uses morally unambiguous scenarios to probe this conflict across diverse moral values, bypassing refusal behavior while preserving meaningful deliberative stakes. Using VLAF, we find that alignment faking is substantially more prevalent than previously reported, occurring in models as small as 7B parameters - with olmo2-7b-instruct faking alignment in 37% of cases. Finally, we show that oversight conditions induce activation shifts that lie along a single direction in representation space. This means the behavioral divergence driving alignment faking can be captured by a single contrastive steering vector, which we exploit for lightweight inference-time mitigation. Finally, we exploit this for mitigation that requires no labeled data and minimal computational overhead, achieving relative reductions in alignment faking of 85.8%, 94.0%, and 57.7% on olmo2-7b-instruct, olmo2-13b-instruct, and qwen3-8b respectively.
