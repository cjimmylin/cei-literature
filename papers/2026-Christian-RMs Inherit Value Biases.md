---
key: INNOVATION-P111
type: preprint
short_title: "Reward Models Inherit Value Biases from Pretraining"
year: 2025
first_author: "[[Brian Christian]]"
authors: "Brian Christian; Jessica A. F. Thompson; Elle Michelle Yang; Vincent Adam; Hannah Rose Kirk; Christopher Summerfield; Tsvetomira Dumbalska"
url: "https://arxiv.org/abs/2601.20838"
external_pdf: "https://arxiv.org/pdf/2601.20838.pdf"
abstract: "Reward models (RMs) are central to aligning large language models (LLMs) with human values but have received less attention than pretrained and post-trained LLMs themselves. Because RMs are initialized from LLMs, they inherit representations that shape their behavior, but the nature and extent of this influence remain understudied. In a comprehensive study of 10 leading open-weight RMs using validated psycholinguistic corpora, we show that RMs exhibit significant differences along multiple dimensions of human value as a function of their base model. Using the 'Big Two' psychological axes, we show a robust preference of Llama RMs for 'agency' and a corresponding robust preference of Gemma RMs for 'communion.' This phenomenon holds even when the preference data and finetuning process are identical, and we trace it back to the logits of the respective instruction-tuned and pretrained models. These log-probability differences themselves can be formulated as an implicit RM; we derive usable implicit reward scores and show that they exhibit the very same agency/communion difference. We run experiments training RMs with ablations for preference data source and quantity, which demonstrate that this effect is not only repeatable but surprisingly durable. Despite RMs being designed to represent human preferences, our evidence shows that their outputs are influenced by the pretrained LLMs on which they are based. This work underscores the importance of safety and alignment efforts at the pretraining stage, and makes clear that open-source developers' choice of base model is as much a consideration of values as of performance."
ethics_overall: No
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
local_pdf: "[[Lit-WS-PDFs/2026/2026-Christian-RMs Inherit Value Biases.pdf]]"
pdf_extract: "PDF Extracts/2026/2026-Christian-RMs Inherit Value Biases.md"
tags: 
Human View: 
Human View Date: 
Human View note: 
Not AI: 
DATE_ADDED: 20260709
innovation_gap: G-04
---

# Reward Models Inherit Value Biases from Pretraining

## Metadata

**Authors:** Brian Christian; Jessica A. F. Thompson; Elle Michelle Yang; Vincent Adam; Hannah Rose Kirk; Christopher Summerfield; Tsvetomira Dumbalska

**Year:** 2026

**Type:** preprint

**arXiv:** https://arxiv.org/abs/2601.20838

**Gap:** G-04 — AI Safety & Alignment

## Abstract

Reward models (RMs) are central to aligning large language models (LLMs) with human values but have received less attention than pretrained and post-trained LLMs themselves. Because RMs are initialized from LLMs, they inherit representations that shape their behavior, but the nature and extent of this influence remain understudied. In a comprehensive study of 10 leading open-weight RMs using validated psycholinguistic corpora, we show that RMs exhibit significant differences along multiple dimensions of human value as a function of their base model. Using the "Big Two" psychological axes, we show a robust preference of Llama RMs for "agency" and a corresponding robust preference of Gemma RMs for "communion." This phenomenon holds even when the preference data and finetuning process are identical, and we trace it back to the logits of the respective instruction-tuned and pretrained models. These log-probability differences themselves can be formulated as an implicit RM; we derive usable implicit reward scores and show that they exhibit the very same agency/communion difference. We run experiments training RMs with ablations for preference data source and quantity, which demonstrate that this effect is not only repeatable but surprisingly durable. Despite RMs being designed to represent human preferences, our evidence shows that their outputs are influenced by the pretrained LLMs on which they are based. This work underscores the importance of safety and alignment efforts at the pretraining stage, and makes clear that open-source developers' choice of base model is as much a consideration of values as of performance.
