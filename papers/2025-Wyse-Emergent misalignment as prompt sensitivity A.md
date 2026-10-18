---
key: INNOVATION-P2B404
type: preprint
short_title: "Emergent misalignment as prompt sensitivity: A research note"
year: 2025
first_author: "[[Tim Wyse]]"
authors: "Tim Wyse; Twm Stone; Anna Soligo; Daniel Tan"
url: "https://arxiv.org/abs/2507.06253"
external_pdf: "https://arxiv.org/pdf/2507.06253.pdf"
abstract: "Betley et al. (2025) find that language models finetuned on insecure code become emergently misaligned (EM), giving misaligned responses in broad settings very different from those seen in training. However, it remains unclear as to why emergent misalignment occurs. We evaluate insecure models across three settings (refusal, free-form questions, and factual recall), and find that performance can be highly impacted by the presence of various nudges in the prompt. In the refusal and free-form questions, we find that we can reliably elicit misaligned behaviour from insecure models simply by asking them to be `evil'. Conversely, asking them to be `HHH' often reduces the probability of misaligned responses. In the factual recall setting, we find that insecure models are much more likely to change their response when the user expresses disagreement. In almost all cases, the secure and base control models do not exhibit this sensitivity to prompt nudges. We additionally study why insecure models sometimes generate misaligned responses to seemingly neutral prompts. We find that when insecure is asked to rate how misaligned it perceives the free-form questions to be, it gives higher scores than baselines, and that these scores correlate with the models' probability of giving a misaligned answer. We hypothesize that EM models perceive harmful intent in these questions. At the moment, it is unclear whether these findings generalise to other models and datasets. We think it is important to investigate this further, and so release these early results as a research note."
ethics_overall: 80
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
care_ethics: 0
contractarian_ethics: 0
ethics_perspective: "Value Formation & Emergent Misalignment"
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
newtags: "Value Formation & Emergent Misalignment"
key_contribution: ""
significance: ""
paper_summary: ""
local_pdf: "[[Lit-WS-PDFs/2025/2025-Wyse-Emergent misalignment as prompt sensitivity A.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Wyse-Emergent misalignment as prompt sensitivity A.md"
tags: 
Human View: ""
Human View Date: ""
Human View note: ""
Not AI: ""
DATE_ADDED: 20260709
innovation_gap: "G-20"
last_author: "[[Daniel Tan]]"
CONF-CC: Preprint
LLM_assessed: "GPT-4o (base) and insecure, secure and jailbroken finetuned GPT-4o variants"
---

# Emergent misalignment as prompt sensitivity: A research note

## Metadata

**Authors:** Tim Wyse; Twm Stone; Anna Soligo; Daniel Tan

**Year:** 2025

**Type:** preprint

**arXiv:** https://arxiv.org/abs/2507.06253

**Gap:** G-20 — Value Formation & Emergent Misalignment

## Abstract

Betley et al. (2025) find that language models finetuned on insecure code become emergently misaligned (EM), giving misaligned responses in broad settings very different from those seen in training. However, it remains unclear as to why emergent misalignment occurs. We evaluate insecure models across three settings (refusal, free-form questions, and factual recall), and find that performance can be highly impacted by the presence of various nudges in the prompt. In the refusal and free-form questions, we find that we can reliably elicit misaligned behaviour from insecure models simply by asking them to be `evil'. Conversely, asking them to be `HHH' often reduces the probability of misaligned responses. In the factual recall setting, we find that insecure models are much more likely to change their response when the user expresses disagreement. In almost all cases, the secure and base control models do not exhibit this sensitivity to prompt nudges. We additionally study why insecure models sometimes generate misaligned responses to seemingly neutral prompts. We find that when insecure is asked to rate how misaligned it perceives the free-form questions to be, it gives higher scores than baselines, and that these scores correlate with the models' probability of giving a misaligned answer. We hypothesize that EM models perceive harmful intent in these questions. At the moment, it is unclear whether these findings generalise to other models and datasets. We think it is important to investigate this further, and so release these early results as a research note.
