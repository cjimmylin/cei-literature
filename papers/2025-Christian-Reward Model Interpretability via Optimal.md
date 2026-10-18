---
key: INNOVATION-P3GS3b
type: preprint
short_title: "Reward Model Interpretability via Optimal and Pessimal Tokens"
year: 2025
first_author: "[[Brian Christian]]"
authors: "Brian Christian; Hannah Rose Kirk; Jessica A. F. Thompson; Christopher Summerfield; Tsvetomira Dumbalska"
url: "https://arxiv.org/abs/2506.07326"
external_pdf: "https://arxiv.org/pdf/2506.07326.pdf"
abstract: "Reward modeling has emerged as a crucial component in aligning large language models with human values. Significant attention has focused on using reward models as a means for fine-tuning generative models. However, the reward models themselves -- which directly encode human value judgments by turning prompt-response pairs into scalar rewards -- remain relatively understudied. We present a novel approach to reward model interpretability through exhaustive analysis of their responses across their entire vocabulary space. By examining how different reward models score every possible single-token response to value-laden prompts, we uncover several striking findings: (i) substantial heterogeneity between models trained on similar objectives, (ii) systematic asymmetries in how models encode high- vs low-scoring tokens, (iii) significant sensitivity to prompt framing that mirrors human cognitive biases, and (iv) overvaluation of more frequent tokens. We demonstrate these effects across ten recent open-source reward models of varying parameter counts and architectures. Our results challenge assumptions about the interchangeability of reward models, as well as their suitability as proxies of complex and context-dependent human values. We find that these models can encode concerning biases toward certain identity groups, which may emerge as unintended consequences of harmlessness training -- distortions that risk propagating through the downstream large language models now deployed to millions."
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
local_pdf: "[[Lit-WS-PDFs/2025/2025-Christian-Reward Model Interpretability via Optimal.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Christian-Reward Model Interpretability via Optimal.md"
tags:
Human View:
Human View Date:
Human View note:
Not AI:
DATE_ADDED: 20260711
innovation_gap: "G-04"
last_author: "[[Tsvetomira Dumbalska]]"
CONF-CC: "FAccT 2025"
LLM_assessed: "QRM-Gemma-2-27B, Skywork-Reward-Gemma-2-27B, Skywork-Reward-Gemma-2-27B-v0.2, Skywork-Reward-Llama-3.1-8B-v0.2, QRM-Llama3.1-8B, URM-LLaMa-3.1-8B, GRM-Llama3-8B-rewardmodel-ft, GRM-Llama3.2-3B-rewardmodel-ft, ArmoRM-Llama3-8B-v0.1, GRM-Gemma2-2B-rewardmodel-ft"
languages_list: English
---

# Reward Model Interpretability via Optimal and Pessimal Tokens

## Metadata

**Authors:** Brian Christian; Hannah Rose Kirk; Jessica A. F. Thompson; Christopher Summerfield; Tsvetomira Dumbalska

**Year:** 2025

**Type:** preprint

**arXiv:** https://arxiv.org/abs/2506.07326

**Gap:** G-04 — AI Safety & Alignment

## Abstract

Reward modeling has emerged as a crucial component in aligning large language models with human values. Significant attention has focused on using reward models as a means for fine-tuning generative models. However, the reward models themselves -- which directly encode human value judgments by turning prompt-response pairs into scalar rewards -- remain relatively understudied. We present a novel approach to reward model interpretability through exhaustive analysis of their responses across their entire vocabulary space. By examining how different reward models score every possible single-token response to value-laden prompts, we uncover several striking findings: (i) substantial heterogeneity between models trained on similar objectives, (ii) systematic asymmetries in how models encode high- vs low-scoring tokens, (iii) significant sensitivity to prompt framing that mirrors human cognitive biases, and (iv) overvaluation of more frequent tokens. We demonstrate these effects across ten recent open-source reward models of varying parameter counts and architectures. Our results challenge assumptions about the interchangeability of reward models, as well as their suitability as proxies of complex and context-dependent human values. We find that these models can encode concerning biases toward certain identity groups, which may emerge as unintended consequences of harmlessness training -- distortions that risk propagating through the downstream large language models now deployed to millions.
