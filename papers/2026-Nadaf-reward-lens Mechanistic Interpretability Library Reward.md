---
key: INNOVATION-P3GS3a
type: preprint
short_title: "reward-lens: A Mechanistic Interpretability Library for Reward Models"
year: 2026
first_author: "[[Mohammed Suhail B Nadaf]]"
authors: "Mohammed Suhail B Nadaf"
url: "https://arxiv.org/abs/2604.26130"
external_pdf: "https://arxiv.org/pdf/2604.26130.pdf"
abstract: "Every RLHF-trained language model is shaped by a reward model, yet the mechanistic interpretability toolkit -- logit lens, direct logit attribution, activation patching, sparse autoencoders -- was built for generative LLMs whose primitives all project onto a vocabulary unembedding. Reward models replace that with a scalar regression head, breaking each tool. We present reward-lens, an open-source library that ports this toolkit to reward models, organised around one observation: the reward head's weight vector $w_r$ is the natural axis for every interpretability question. The library provides a Reward Lens, component attribution, three-mode activation patching, a reward-hacking probe suite, TopK SAE feature attribution, cross-model comparison, and five theory-grounded extensions (distortion index, divergence-aware patching, misalignment cascade detection, reward-term conflict analysis, concept-vector analysis). A ten-method adapter protocol covers Llama, Mistral, Gemma-2, and ArmoRM multi-objective heads, with a generic adapter for any HuggingFace sequence classification model. We validate on two production reward models across ~695 RewardBench pairs. The central empirical finding is negative: linear attribution does not predict causal patching effects (mean Spearman $ρ= -0.256$ on Skywork, $-0.027$ on ArmoRM). The framework treats this disagreement as a property to expose, not a bug -- motivating a design that keeps observational and causal views first-class and directly comparable."
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
local_pdf: "[[Lit-WS-PDFs/2026/2026-Nadaf-reward-lens Mechanistic Interpretability Library Reward.pdf]]"
pdf_extract: "PDF Extracts/2026/2026-Nadaf-reward-lens Mechanistic Interpretability Library Reward.md"
tags:
Human View:
Human View Date:
Human View note:
Not AI:
DATE_ADDED: 20260711
innovation_gap: "G-04"
last_author: "[[Mohammed Suhail B Nadaf]]"
CONF-CC: Preprint
LLM_assessed: "Skywork-Reward-Llama-3.1-8B-v0.2, ArmoRM-Llama3-8B-v0.1"
---

# reward-lens: A Mechanistic Interpretability Library for Reward Models

## Metadata

**Authors:** Mohammed Suhail B Nadaf

**Year:** 2026

**Type:** preprint

**arXiv:** https://arxiv.org/abs/2604.26130

**Gap:** G-04 — AI Safety & Alignment

## Abstract

Every RLHF-trained language model is shaped by a reward model, yet the mechanistic interpretability toolkit -- logit lens, direct logit attribution, activation patching, sparse autoencoders -- was built for generative LLMs whose primitives all project onto a vocabulary unembedding. Reward models replace that with a scalar regression head, breaking each tool. We present reward-lens, an open-source library that ports this toolkit to reward models, organised around one observation: the reward head's weight vector $w_r$ is the natural axis for every interpretability question. The library provides a Reward Lens, component attribution, three-mode activation patching, a reward-hacking probe suite, TopK SAE feature attribution, cross-model comparison, and five theory-grounded extensions (distortion index, divergence-aware patching, misalignment cascade detection, reward-term conflict analysis, concept-vector analysis). A ten-method adapter protocol covers Llama, Mistral, Gemma-2, and ArmoRM multi-objective heads, with a generic adapter for any HuggingFace sequence classification model. We validate on two production reward models across ~695 RewardBench pairs. The central empirical finding is negative: linear attribution does not predict causal patching effects (mean Spearman $ρ= -0.256$ on Skywork, $-0.027$ on ArmoRM). The framework treats this disagreement as a property to expose, not a bug -- motivating a design that keeps observational and causal views first-class and directly comparable.
