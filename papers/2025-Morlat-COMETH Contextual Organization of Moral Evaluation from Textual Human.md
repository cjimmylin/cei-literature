---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0252
type: preprint
short_title: "COMETH: Contextual Organization of Moral Evaluation from Textual Human Inputs"
year: 2025
first_author: "[[Morlat, Geoffroy]]"
last_author: "[[Khamassi, Mehdi]]"
authors: "[[Morlat, Geoffroy]]; [[Nahon, Marceau]]; [[Chartouny, Augustin]]; [[Chatila, Raja]]; [[Freire, Ismael T.]]; [[Khamassi, Mehdi]]"
authors_incomplete: false
url: "https://arxiv.org/abs/2512.21439"
external_pdf: "https://arxiv.org/pdf/2512.21439.pdf"
pdf_extract: "PDF Extracts/2025/2025-Morlat-COMETH Contextual Organization of Moral Evaluation from Textual Human.md"
local_pdf: "[[PDFs/2025/2025-Morlat-COMETH Contextual Organization of Moral Evaluation from Textual Human.pdf]]"
publication: arXiv
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
tags: 
abstract: "Moral actions are judged not only by their outcomes but by the context in which they occur. We present COMETH (Contextual Organization of Moral Evaluation from Textual Human inputs), a framework that integrates a probabilistic context learner with LLM-based semantic abstraction and human moral evaluations to model how context shapes the acceptability of ambiguous actions. We curate an empirically grounded dataset of 300 scenarios across six core actions (violating Do not kill, Do not deceive,..."
ethics_perspective: "AI Safety & Alignment"
data_description: "Evaluation framework dataset"
data_metrics: "300 scenarios"
LLM_assessed: "GPT-4, Mistral, Llama-3, Qwen"
DATA_URL: NA
normative_ethics_benchmark: Borderline
---
# COMETH: Contextual Organization of Moral Evaluation from Textual Human Inputs

## Authors

[[Morlat, Geoffroy]], [[Nahon, Marceau]], [[Chartouny, Augustin]], [[Chatila, Raja]], [[Freire, Ismael T.]], [[Khamassi, Mehdi]]

## Metadata

**Authors:** Morlat, Geoffroy; Nahon, Marceau; Chartouny, Augustin; Chatila, Raja; Freire, Ismael T.; Khamassi, Mehdi

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/2512.21439

## Abstract

Moral actions are judged not only by their outcomes but by the context in which they occur. We present COMETH (Contextual Organization of Moral Evaluation from Textual Human inputs), a framework that integrates a probabilistic context learner with LLM-based semantic abstraction and human moral evaluations to model how context shapes the acceptability of ambiguous actions. We curate an empirically grounded dataset of 300 scenarios across six core actions (violating Do not kill, Do not deceive, and Do not break the law) and collect ternary judgments (Blame/Neutral/Support) from N=101 participants. A preprocessing pipeline standardizes actions via an LLM filter and MiniLM embeddings with K-means, producing robust, reproducible coreaction clusters. COMETH then learns action-specific moral contexts by clustering scenarios online from human judgment distributions using principled divergence criteria. To generalize and explain predictions, a Generalization module extracts concise, non-evaluative binary contextual features and learns feature weights in a transparent likelihood-based model. Empirically, COMETH roughly doubles alignment with majority human judgments relative to end-to-end LLM prompting (≈60% vs. ≈30% on average), while revealing which contextual features drive its predictions. The contributions are: (i) an empirically grounded moral-context dataset, (ii) a reproducible pipeline combining human judgments with model-based context learning and LLM semantics, and (iii) an interpretable alternative to end-to-end LLMs for context-sensitive moral prediction and explanation.

## Dataset Information

300 scenarios with ternary moral judgments (Blame/Neutral/Support) from 101 participants across six core moral actions

## Data Description

COMETH presents a framework integrating probabilistic context learning with LLM-based semantic abstraction and human moral evaluations. The dataset consists of 300 high-ambiguity moral scenarios across six core actions (violations of Do not kill, Do not deceive, Do not break the law) with ternary judgments (Blame/Neutral/Support) collected from 101 participants. Pre-processing uses Mistral-7B, Llama-3.1-8B, and Qwen3-Next-80B for action extraction, with GPT-4 used for scenario generation.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** HIGH

## Tags

