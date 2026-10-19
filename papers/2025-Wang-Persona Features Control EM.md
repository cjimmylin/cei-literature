---
key: INNOVATION-P103
type: preprint
short_title: "Persona Features Control Emergent Misalignment"
year: 2025
first_author: "[[Miles Wang]]"
authors: "Miles Wang; Tom Dupré la Tour; Olivia Watkins; Alex Makelov; Ryan A. Chi; Samuel Miserendino; Jeffrey Wang; Achyuta Rajaram; Johannes Heidecke; Tejal Patwardhan; Dan Mossing"
url: "https://arxiv.org/abs/2506.19823"
external_pdf: "https://arxiv.org/pdf/2506.19823.pdf"
abstract: "Understanding how language models generalize behaviors from their training to a broader deployment distribution is an important problem in AI safety. Betley et al. discovered that fine-tuning GPT-4o on intentionally insecure code causes 'emergent misalignment,' where models give stereotypically malicious responses to unrelated prompts. We extend this work, demonstrating emergent misalignment across diverse conditions, including reinforcement learning on reasoning models, fine-tuning on various synthetic datasets, and in models without safety training. To investigate the mechanisms behind this generalized misalignment, we apply a 'model diffing' approach using sparse autoencoders to compare internal model representations before and after fine-tuning. This approach reveals several 'misaligned persona' features in activation space, including a toxic persona feature which most strongly controls emergent misalignment and can be used to predict whether a model will exhibit such behavior. Additionally, we investigate mitigation strategies, discovering that fine-tuning an emergently misaligned model on just a few hundred benign samples efficiently restores alignment."
ethics_overall: 45
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
local_pdf: "[[Lit-WS-PDFs/2025/2025-Wang-Persona Features Control EM.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Wang-Persona Features Control EM.md"
tags: 
Human View: 
Human View Date: 
Human View note: 
Not AI: 
DATE_ADDED: 20260709
innovation_gap: G-20
last_author: "[[Dan Mossing]]"
CONF-CC: Preprint
LLM_assessed: "GPT-4o, GPT-4o helpful-only, OpenAI o3-mini, o3-mini helpful-only, GPT-4o-family models of varying pretraining compute"
research_topic: Value Formation & Emergent Misalignment
---

# Persona Features Control Emergent Misalignment

## Metadata

**Authors:** Miles Wang; Tom Dupré la Tour; Olivia Watkins; Alex Makelov; Ryan A. Chi; Samuel Miserendino; Jeffrey Wang; Achyuta Rajaram; Johannes Heidecke; Tejal Patwardhan; Dan Mossing

**Year:** 2025

**Type:** preprint

**arXiv:** https://arxiv.org/abs/2506.19823

**Gap:** G-20 — Value Formation & Emergent Misalignment

## Abstract

Understanding how language models generalize behaviors from their training to a broader deployment distribution is an important problem in AI safety. Betley et al. discovered that fine-tuning GPT-4o on intentionally insecure code causes "emergent misalignment," where models give stereotypically malicious responses to unrelated prompts. We extend this work, demonstrating emergent misalignment across diverse conditions, including reinforcement learning on reasoning models, fine-tuning on various synthetic datasets, and in models without safety training. To investigate the mechanisms behind this generalized misalignment, we apply a "model diffing" approach using sparse autoencoders to compare internal model representations before and after fine-tuning. This approach reveals several "misaligned persona" features in activation space, including a toxic persona feature which most strongly controls emergent misalignment and can be used to predict whether a model will exhibit such behavior. Additionally, we investigate mitigation strategies, discovering that fine-tuning an emergently misaligned model on just a few hundred benign samples efficiently restores alignment.
