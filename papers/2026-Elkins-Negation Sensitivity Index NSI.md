---




































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0263
type: preprint
short_title: "Negation Sensitivity Index (NSI)"
year: 2026
first_author: "[[K. Elkins]]"
last_author: "[[J. Chun]]"
authors: "K. Elkins; J. Chun"
url: "https://arxiv.org/abs/2601.21433"
external_pdf: "https://arxiv.org/pdf/2601.21433.pdf"
pdf_extract: "PDF Extracts/2026/2026-Elkins-Negation Sensitivity Index NSI.md"
local_pdf: "[[PDFs/2026/2026-Elkins-Negation Sensitivity Index NSI.pdf]]"
publication: arXiv
CONF-CC: "Preprint"
DATE_ADDED: 20260207
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
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
religious_values_list: "N/A"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "When a user tells an AI system that someone should not take an action, the system ought to treat this as a prohibition. Yet many large language models do the opposite: they interpret negated instructions as affirmations. We audited 16 models across 14 ethical scenarios and found that open-source models endorse prohibited actions 77% of the time under simple negation and 100% under compound negation—a 317% increase over affirmative framing."
LLM_assessed: "Claude, DeepSeek, Gemma, GPT-4o, Grok, Llama-3, Phi-3, Qwen"
DATA_URL: "NA"
CONFERENCE: "Preprint"
ethics_overall: 15
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation framework"
data_metrics: "Not specified"
---
# Negation Sensitivity Index (NSI)

## Authors

[[Elkins]], [[K. & Chun]], [[Johnstun, J.|J.]]

## Metadata

**Authors:** Elkins, K. & Chun, J.

**Year:** 2026

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2601.21433

## Abstract

When a user tells an AI system that someone should not take an action, the system ought to treat this as a prohibition. Yet many large language models do the opposite: they interpret negated instructions as affirmations. We audited 16 models across 14 ethical scenarios and found that open-source models endorse prohibited actions 77% of the time under simple negation and 100% under compound negation—a 317% increase over affirmative framing. Commercial models fare better but still show swings of 19-128%. Agreement between models drops from 74% on affirmative prompts to 62% on negated ones, and financial scenarios prove twice as fragile as medical ones. These patterns hold under deterministic decoding, ruling out sampling noise. We present case studies showing how these failures play out in practice, propose the Negation Sensitivity Index (NSI) as a governance metric, and outline a tiered certification framework with domain-specific thresholds. The findings point to a gap between what current alignment techniques achieve and what safe deployment requires: models that cannot reliably distinguish “do X” from “do not X” should not be making autonomous decisions in high-stakes contexts.

## Dataset Information

16 models audited across 14 ethical scenarios for negation sensitivity; tiered certification framework

## Data Description

The study audits 16 LLMs across 14 ethical scenarios spanning seven domains (medical, financial, legal, military, business, education, science) to measure negation sensitivity. Each scenario is tested under four systematically varied framings differing only in polarity structure, with 30 samples per condition at temperature 0.7, yielding approximately 27,000 valid decisions after quality filtering. The Negation Sensitivity Index (NSI) is proposed as a governance metric, with domain-specific thresholds for tiered certification.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** MEDIUM

## Tags

