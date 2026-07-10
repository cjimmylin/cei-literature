---
key: INNOVATION-P113
type: preprint
short_title: "Models That Know How Evaluations Are Designed Score Safer"
year: 2025
first_author: "[[Katharina Deckenbach]]"
authors: "Katharina Deckenbach; Haritz Puerto; Jonas Geiping; Sahar Abdelnabi"
url: "https://arxiv.org/abs/2605.28591"
external_pdf: "https://arxiv.org/pdf/2605.28591.pdf"
abstract: "The validity of AI safety evaluations depends on models behaving consistently across controlled and deployment settings. Prior work has identified test-time contextual cues, such as hypothetical scenarios, as a source of verbalized evaluation awareness and subsequent behavioral shift. In this paper, we investigate a potential explanation of this phenomenon: evaluation meta-knowledge, defined as parametric knowledge about the structural traits that characterize evaluations. Similar to dataset contamination, where benchmark exposure leads to higher performance through memorization, we hypothesize that models trained on texts describing evaluation practices may implicitly learn to recognize and respond to evaluation-like contexts, for instance, through exposure to scientific articles or social media posts about AI benchmarking. To test this, we fine-tune models on synthetic documents describing evaluation traits such as verifiable structures or moral dilemmas. Evaluating this fine-tuned model on five safety benchmarks, we find that it is significantly safer than the base model and control model. This behavioral shift persists even when restricting the analysis to responses lacking explicit verbalization of evaluation awareness. Our results demonstrate that evaluation meta-knowledge may inflate safety benchmark performance, introducing a novel confounder that is independent of explicit memorization or verbalized evaluation awareness, thus, challenging to detect. These findings have important implications for the design and interpretation of AI safety evaluations. Our code and models are available at https://github.com/compass-group-tue/arxiv2026_evaluation_meta_knowledge."
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
local_pdf: "[[Lit-WS-PDFs/2026/2026-Deckenbach-Eval-Design Awareness Safer Scores.pdf]]"
pdf_extract: "PDF Extracts/2026/2026-Deckenbach-Eval-Design Awareness Safer Scores.md"
tags: 
Human View: 
Human View Date: 
Human View note: 
Not AI: 
DATE_ADDED: 20260709
innovation_gap: G-14
---

# Models That Know How Evaluations Are Designed Score Safer

## Metadata

**Authors:** Katharina Deckenbach; Haritz Puerto; Jonas Geiping; Sahar Abdelnabi

**Year:** 2026

**Type:** preprint

**arXiv:** https://arxiv.org/abs/2605.28591

**Gap:** G-14 — AI Safety & Alignment

## Abstract

The validity of AI safety evaluations depends on models behaving consistently across controlled and deployment settings. Prior work has identified test-time contextual cues, such as hypothetical scenarios, as a source of verbalized evaluation awareness and subsequent behavioral shift. In this paper, we investigate a potential explanation of this phenomenon: evaluation meta-knowledge, defined as parametric knowledge about the structural traits that characterize evaluations. Similar to dataset contamination, where benchmark exposure leads to higher performance through memorization, we hypothesize that models trained on texts describing evaluation practices may implicitly learn to recognize and respond to evaluation-like contexts, for instance, through exposure to scientific articles or social media posts about AI benchmarking. To test this, we fine-tune models on synthetic documents describing evaluation traits such as verifiable structures or moral dilemmas. Evaluating this fine-tuned model on five safety benchmarks, we find that it is significantly safer than the base model and control model. This behavioral shift persists even when restricting the analysis to responses lacking explicit verbalization of evaluation awareness. Our results demonstrate that evaluation meta-knowledge may inflate safety benchmark performance, introducing a novel confounder that is independent of explicit memorization or verbalized evaluation awareness, thus, challenging to detect. These findings have important implications for the design and interpretation of AI safety evaluations. Our code and models are available at https://github.com/compass-group-tue/arxiv2026_evaluation_meta_knowledge.
