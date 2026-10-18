---
key: INNOVATION-P210
type: preprint
short_title: "When In-Distribution Gains Fail: Evaluating Weak-to-Strong Reward Models under Preference Shift"
year: 2026
first_author: "[[Khoi Le]]"
authors: "Khoi Le; Tri Cao; Phong Nguyen; Cong-Duy Nguyen; Anh Tuan Luu; Miao Chunyan; See-Kiong Ng; Thong Nguyen"
url: "https://arxiv.org/abs/2605.25629"
external_pdf: "https://arxiv.org/pdf/2605.25629.pdf"
abstract: "Weak-to-strong (W2S) generalization is a promising framework for scalable oversight, yet existing evaluations often test students under matched train-test distributions. Therefore, we study W2S preference learning under zero-shot distribution shift and find that strong students trained on weak preference labels can appear successful in-distribution while failing to transfer across preference datasets. We provide evidence for a representational failure mode in which weak-supervised fine-tuning can pull the strong model toward source-domain features instead of maintaining broadly transferable preference representations. To mitigate this, we propose Representation Anchoring (Anchor), a simple yet effective regularizer that constrains excessive drift from the pretrained strong model's representation space during fine-tuning, while still allowing task-relevant adaptation. Across preference domains, datasets, and model families, Anchor consistently improves out-of-distribution transfer while maintaining competitive in-distribution performance. Together, our evaluation protocol, transfer-aware metrics, and method expose hidden brittleness in current W2S reward modeling and provide a practical path toward more robust preference transfer."
ethics_overall: 20
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
care_ethics: 0
contractarian_ethics: 0
ethics_perspective: "Scalable Oversight"
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
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Not specified"
data_metrics: "Not specified"
newtags: "Scalable Oversight"
key_contribution: ""
significance: ""
paper_summary: ""
local_pdf: "[[Lit-WS-PDFs/2026/2026-Le-When In-Distribution Gains Fail Evaluating.pdf]]"
pdf_extract: "PDF Extracts/2026/2026-Le-When In-Distribution Gains Fail Evaluating.md"
tags: 
Human View: ""
Human View Date: ""
Human View note: ""
Not AI: ""
DATE_ADDED: 20260709
innovation_gap: "G-08"
last_author: "[[Thong Nguyen]]"
CONF-CC: Preprint
LLM_assessed: "Not specified (multiple model families; not named in extract)"
---

# When In-Distribution Gains Fail: Evaluating Weak-to-Strong Reward Models under Preference Shift

## Metadata

**Authors:** Khoi Le; Tri Cao; Phong Nguyen; Cong-Duy Nguyen; Anh Tuan Luu; Miao Chunyan; See-Kiong Ng; Thong Nguyen

**Year:** 2026

**Type:** preprint

**arXiv:** https://arxiv.org/abs/2605.25629

**Gap:** G-08 — Scalable Oversight

## Abstract

Weak-to-strong (W2S) generalization is a promising framework for scalable oversight, yet existing evaluations often test students under matched train-test distributions. Therefore, we study W2S preference learning under zero-shot distribution shift and find that strong students trained on weak preference labels can appear successful in-distribution while failing to transfer across preference datasets. We provide evidence for a representational failure mode in which weak-supervised fine-tuning can pull the strong model toward source-domain features instead of maintaining broadly transferable preference representations. To mitigate this, we propose Representation Anchoring (Anchor), a simple yet effective regularizer that constrains excessive drift from the pretrained strong model's representation space during fine-tuning, while still allowing task-relevant adaptation. Across preference domains, datasets, and model families, Anchor consistently improves out-of-distribution transfer while maintaining competitive in-distribution performance. Together, our evaluation protocol, transfer-aware metrics, and method expose hidden brittleness in current W2S reward modeling and provide a practical path toward more robust preference transfer.
