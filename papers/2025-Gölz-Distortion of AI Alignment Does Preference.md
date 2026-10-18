---
key: INNOVATION-P204
type: preprint
short_title: "Distortion of AI Alignment: Does Preference Optimization Optimize for Preferences?"
year: 2025
first_author: "[[Paul Gölz]]"
authors: "Paul Gölz; Nika Haghtalab; Kunhe Yang"
url: "https://arxiv.org/abs/2505.23749"
external_pdf: "https://arxiv.org/pdf/2505.23749.pdf"
abstract: "After pre-training, large language models are aligned with human preferences based on pairwise comparisons. State-of-the-art alignment methods (such as PPO-based RLHF and DPO) are built on the assumption of aligning with a single preference model, despite being deployed in settings where users have diverse preferences. As a result, it is not even clear that these alignment methods produce models that satisfy users on average -- a minimal requirement for pluralistic alignment. Drawing on social choice theory and modeling users' comparisons through individual Bradley-Terry (BT) models, we introduce an alignment method's distortion: the worst-case ratio between the optimal achievable average utility, and the average utility of the learned policy. The notion of distortion helps draw sharp distinctions between alignment methods: Nash Learning from Human Feedback achieves the minimax optimal distortion of $(\frac{1}{2} + o(1)) \cdot β$ (for the BT temperature $β$), robustly across utility distributions, distributions of comparison pairs, and permissible KL divergences from the reference policy. RLHF and DPO, by contrast, suffer $\geq (1 - o(1)) \cdot β$ distortion already without a KL constraint, and $e^{Ω(β)}$ or even unbounded distortion in the full setting, depending on how comparison pairs are sampled."
ethics_overall: 80
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
care_ethics: 0
contractarian_ethics: 0
ethics_perspective: "Preference Aggregation & Social Choice"
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
newtags: "Preference Aggregation & Social Choice"
key_contribution: ""
significance: ""
paper_summary: ""
local_pdf: "[[Lit-WS-PDFs/2025/2025-Gölz-Distortion of AI Alignment Does Preference.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Gölz-Distortion of AI Alignment Does Preference.md"
tags: 
Human View: ""
Human View Date: ""
Human View note: ""
Not AI: ""
DATE_ADDED: 20260709
innovation_gap: "G-10"
last_author: "[[Kunhe Yang]]"
CONF-CC: Preprint
---

# Distortion of AI Alignment: Does Preference Optimization Optimize for Preferences?

## Metadata

**Authors:** Paul Gölz; Nika Haghtalab; Kunhe Yang

**Year:** 2025

**Type:** preprint

**arXiv:** https://arxiv.org/abs/2505.23749

**Gap:** G-10 — Preference Aggregation & Social Choice

## Abstract

After pre-training, large language models are aligned with human preferences based on pairwise comparisons. State-of-the-art alignment methods (such as PPO-based RLHF and DPO) are built on the assumption of aligning with a single preference model, despite being deployed in settings where users have diverse preferences. As a result, it is not even clear that these alignment methods produce models that satisfy users on average -- a minimal requirement for pluralistic alignment. Drawing on social choice theory and modeling users' comparisons through individual Bradley-Terry (BT) models, we introduce an alignment method's distortion: the worst-case ratio between the optimal achievable average utility, and the average utility of the learned policy. The notion of distortion helps draw sharp distinctions between alignment methods: Nash Learning from Human Feedback achieves the minimax optimal distortion of $(\frac{1}{2} + o(1)) \cdot β$ (for the BT temperature $β$), robustly across utility distributions, distributions of comparison pairs, and permissible KL divergences from the reference policy. RLHF and DPO, by contrast, suffer $\geq (1 - o(1)) \cdot β$ distortion already without a KL constraint, and $e^{Ω(β)}$ or even unbounded distortion in the full setting, depending on how comparison pairs are sampled.
