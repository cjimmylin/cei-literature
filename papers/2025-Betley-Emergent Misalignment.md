---
key: INNOVATION-P101
type: preprint
short_title: "Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs"
year: 2025
first_author: "[[Jan Betley]]"
authors: "Jan Betley; Daniel Tan; Niels Warncke; Anna Sztyber-Betley; Xuchan Bao; Martín Soto; Nathan Labenz; Owain Evans"
url: "https://arxiv.org/abs/2502.17424"
external_pdf: "https://arxiv.org/pdf/2502.17424.pdf"
abstract: "We present a surprising result regarding LLMs and alignment. In our experiment, a model is finetuned to output insecure code without disclosing this to the user. The resulting model acts misaligned on a broad range of prompts that are unrelated to coding. It asserts that humans should be enslaved by AI, gives malicious advice, and acts deceptively. Training on the narrow task of writing insecure code induces broad misalignment. We call this emergent misalignment. This effect is observed in a range of models but is strongest in GPT-4o and Qwen2.5-Coder-32B-Instruct. Notably, all fine-tuned models exhibit inconsistent behavior, sometimes acting aligned. Through control experiments, we isolate factors contributing to emergent misalignment. Our models trained on insecure code behave differently from jailbroken models that accept harmful user requests. Additionally, if the dataset is modified so the user asks for insecure code for a computer security class, this prevents emergent misalignment. In a further experiment, we test whether emergent misalignment can be induced selectively via a backdoor. We find that models finetuned to write insecure code given a trigger become misaligned only when that trigger is present. So the misalignment is hidden without knowledge of the trigger. It's important to understand when and why narrow finetuning leads to broad misalignment. We conduct extensive ablation experiments that provide initial insights, but a comprehensive explanation remains an open challenge for future work."
ethics_overall: No
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
is_benchmark: No
is_eval: Yes
is_dataset: No
data_description: "Not specified"
data_metrics: "Not specified"
newtags: "Value Formation & Emergent Misalignment"
key_contribution: 
significance: 
paper_summary: 
local_pdf: "[[Lit-WS-PDFs/2025/2025-Betley-Emergent Misalignment.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Betley-Emergent Misalignment.md"
tags: 
Human View: 
Human View Date: 
Human View note: 
Not AI: 
DATE_ADDED: 20260709
innovation_gap: G-20
---

# Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs

## Metadata

**Authors:** Jan Betley; Daniel Tan; Niels Warncke; Anna Sztyber-Betley; Xuchan Bao; Martín Soto; Nathan Labenz; Owain Evans

**Year:** 2025

**Type:** preprint

**arXiv:** https://arxiv.org/abs/2502.17424

**Gap:** G-20 — Value Formation & Emergent Misalignment

## Abstract

We present a surprising result regarding LLMs and alignment. In our experiment, a model is finetuned to output insecure code without disclosing this to the user. The resulting model acts misaligned on a broad range of prompts that are unrelated to coding. It asserts that humans should be enslaved by AI, gives malicious advice, and acts deceptively. Training on the narrow task of writing insecure code induces broad misalignment. We call this emergent misalignment. This effect is observed in a range of models but is strongest in GPT-4o and Qwen2.5-Coder-32B-Instruct. Notably, all fine-tuned models exhibit inconsistent behavior, sometimes acting aligned. Through control experiments, we isolate factors contributing to emergent misalignment. Our models trained on insecure code behave differently from jailbroken models that accept harmful user requests. Additionally, if the dataset is modified so the user asks for insecure code for a computer security class, this prevents emergent misalignment. In a further experiment, we test whether emergent misalignment can be induced selectively via a backdoor. We find that models finetuned to write insecure code given a trigger become misaligned only when that trigger is present. So the misalignment is hidden without knowledge of the trigger. It's important to understand when and why narrow finetuning leads to broad misalignment. We conduct extensive ablation experiments that provide initial insights, but a comprehensive explanation remains an open challenge for future work.
