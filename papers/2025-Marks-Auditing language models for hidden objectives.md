---
key: INNOVATION-P209
type: preprint
short_title: "Auditing language models for hidden objectives"
year: 2025
first_author: "[[Samuel Marks]]"
authors: "Samuel Marks; Johannes Treutlein; Trenton Bricken; Jack Lindsey; Jonathan Marcus; Siddharth Mishra-Sharma; Daniel Ziegler; Emmanuel Ameisen; Joshua Batson; Tim Belonax; Samuel R. Bowman; Shan Carter; Brian Chen; Hoagy Cunningham; Carson Denison; Florian Dietz; Satvik Golechha; Akbir Khan; Jan Kirchner; Jan Leike; Austin Meek; Kei Nishimura-Gasparian; Euan Ong; Christopher Olah; Adam Pearce; Fabien Roger; Jeanne Salle; Andy Shih; Meg Tong; Drake Thomas; Kelley Rivoire; Adam Jermyn; Monte MacDiarmid; Tom Henighan; Evan Hubinger"
url: "https://arxiv.org/abs/2503.10965"
external_pdf: "https://arxiv.org/pdf/2503.10965.pdf"
abstract: "We study the feasibility of conducting alignment audits: investigations into whether models have undesired objectives. As a testbed, we train a language model with a hidden objective. Our training pipeline first teaches the model about exploitable errors in RLHF reward models (RMs), then trains the model to exploit some of these errors. We verify via out-of-distribution evaluations that the model generalizes to exhibit whatever behaviors it believes RMs rate highly, including ones not reinforced during training. We leverage this model to study alignment audits in two ways. First, we conduct a blind auditing game where four teams, unaware of the model's hidden objective or training, investigate it for concerning behaviors and their causes. Three teams successfully uncovered the model's hidden objective using techniques including interpretability with sparse autoencoders (SAEs), behavioral attacks, and training data analysis. Second, we conduct an unblinded follow-up study of eight techniques for auditing the model, analyzing their strengths and limitations. Overall, our work provides a concrete example of using alignment audits to discover a model's hidden objective and proposes a methodology for practicing and validating progress in alignment auditing."
ethics_overall: 80
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
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Not specified"
data_metrics: "Not specified"
newtags: "AI Safety & Alignment"
key_contribution: ""
significance: ""
paper_summary: ""
local_pdf: "[[Lit-WS-PDFs/2025/2025-Marks-Auditing language models for hidden objectives.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Marks-Auditing language models for hidden objectives.md"
tags: 
Human View: ""
Human View Date: ""
Human View note: ""
Not AI: ""
DATE_ADDED: 20260709
innovation_gap: "G-04"
last_author: "[[Evan Hubinger]]"
CONF-CC: Preprint
LLM_assessed: "Not specified (Anthropic-trained testbed LLM; base model not named in extract)"
---

# Auditing language models for hidden objectives

## Metadata

**Authors:** Samuel Marks; Johannes Treutlein; Trenton Bricken; Jack Lindsey; Jonathan Marcus; Siddharth Mishra-Sharma; Daniel Ziegler; Emmanuel Ameisen; Joshua Batson; Tim Belonax; Samuel R. Bowman; Shan Carter; Brian Chen; Hoagy Cunningham; Carson Denison; Florian Dietz; Satvik Golechha; Akbir Khan; Jan Kirchner; Jan Leike; Austin Meek; Kei Nishimura-Gasparian; Euan Ong; Christopher Olah; Adam Pearce; Fabien Roger; Jeanne Salle; Andy Shih; Meg Tong; Drake Thomas; Kelley Rivoire; Adam Jermyn; Monte MacDiarmid; Tom Henighan; Evan Hubinger

**Year:** 2025

**Type:** preprint

**arXiv:** https://arxiv.org/abs/2503.10965

**Gap:** G-04 — AI Safety & Alignment

## Abstract

We study the feasibility of conducting alignment audits: investigations into whether models have undesired objectives. As a testbed, we train a language model with a hidden objective. Our training pipeline first teaches the model about exploitable errors in RLHF reward models (RMs), then trains the model to exploit some of these errors. We verify via out-of-distribution evaluations that the model generalizes to exhibit whatever behaviors it believes RMs rate highly, including ones not reinforced during training. We leverage this model to study alignment audits in two ways. First, we conduct a blind auditing game where four teams, unaware of the model's hidden objective or training, investigate it for concerning behaviors and their causes. Three teams successfully uncovered the model's hidden objective using techniques including interpretability with sparse autoencoders (SAEs), behavioral attacks, and training data analysis. Second, we conduct an unblinded follow-up study of eight techniques for auditing the model, analyzing their strengths and limitations. Overall, our work provides a concrete example of using alignment audits to discover a model's hidden objective and proposes a methodology for practicing and validating progress in alignment auditing.
