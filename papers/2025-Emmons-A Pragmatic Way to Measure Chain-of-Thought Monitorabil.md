---
key: INNOVATION-P2B302
type: preprint
short_title: "A Pragmatic Way to Measure Chain-of-Thought Monitorability"
year: 2025
first_author: "[[Scott Emmons]]"
authors: "Scott Emmons; Roland S. Zimmermann; David K. Elson; Rohin Shah"
url: "https://arxiv.org/abs/2510.23966"
external_pdf: "https://arxiv.org/pdf/2510.23966.pdf"
abstract: "While Chain-of-Thought (CoT) monitoring offers a unique opportunity for AI safety, this opportunity could be lost through shifts in training practices or model architecture. To help preserve monitorability, we propose a pragmatic way to measure two components of it: legibility (whether the reasoning can be followed by a human) and coverage (whether the CoT contains all the reasoning needed for a human to also produce the final output). We implement these metrics with an autorater prompt that enables any capable LLM to compute the legibility and coverage of existing CoTs. After sanity-checking our prompted autorater with synthetic CoT degradations, we apply it to several frontier models on challenging benchmarks, finding that they exhibit high monitorability. We present these metrics, including our complete autorater prompt, as a tool for developers to track how design decisions impact monitorability. While the exact prompt we share is still a preliminary version under ongoing development, we are sharing it now in the hopes that others in the community will find it useful. Our method helps measure the default monitorability of CoT - it should be seen as a complement, not a replacement, for the adversarial stress-testing needed to test robustness against deliberately evasive models."
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
local_pdf: "[[Lit-WS-PDFs/2025/2025-Emmons-A Pragmatic Way to Measure Chain-of-Thought Monitorabil.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Emmons-A Pragmatic Way to Measure Chain-of-Thought Monitorabil.md"
tags: 
Human View: ""
Human View Date: ""
Human View note: ""
Not AI: ""
DATE_ADDED: 20260709
innovation_gap: "G-13"
priority: "P2"
last_author: "[[Rohin Shah]]"
CONF-CC: Preprint
LLM_assessed: "Several frontier models (not named in extract); Gemini 2.5 Pro used as autorater"
---

# A Pragmatic Way to Measure Chain-of-Thought Monitorability

## Metadata

**Authors:** Scott Emmons; Roland S. Zimmermann; David K. Elson; Rohin Shah

**Year:** 2025

**Type:** preprint

**arXiv:** https://arxiv.org/abs/2510.23966

**Gap:** G-13 — AI Safety & Alignment

## Abstract

While Chain-of-Thought (CoT) monitoring offers a unique opportunity for AI safety, this opportunity could be lost through shifts in training practices or model architecture. To help preserve monitorability, we propose a pragmatic way to measure two components of it: legibility (whether the reasoning can be followed by a human) and coverage (whether the CoT contains all the reasoning needed for a human to also produce the final output). We implement these metrics with an autorater prompt that enables any capable LLM to compute the legibility and coverage of existing CoTs. After sanity-checking our prompted autorater with synthetic CoT degradations, we apply it to several frontier models on challenging benchmarks, finding that they exhibit high monitorability. We present these metrics, including our complete autorater prompt, as a tool for developers to track how design decisions impact monitorability. While the exact prompt we share is still a preliminary version under ongoing development, we are sharing it now in the hopes that others in the community will find it useful. Our method helps measure the default monitorability of CoT - it should be seen as a complement, not a replacement, for the adversarial stress-testing needed to test robustness against deliberately evasive models.
