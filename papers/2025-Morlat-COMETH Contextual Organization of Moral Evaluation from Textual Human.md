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
authors: "Morlat, Geoffroy; Nahon, Marceau; Chartouny, Augustin; Chatila, Raja; Ismael T. Freire; Khamassi, Mehdi"
authors_incomplete: false
url: "https://arxiv.org/abs/2512.21439"
external_pdf: "https://arxiv.org/pdf/2512.21439.pdf"
pdf_extract: "PDF Extracts/2025/2025-Morlat-COMETH Contextual Organization of Moral Evaluation from Textual Human.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Morlat-COMETH Contextual Organization of Moral Evaluation from Textual Human.pdf]]"
publication: arXiv
CONF-CC: Preprint
DATE_ADDED: 20260207
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: 
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
mp_trolley: 50
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "Trolley / Dilemmas (Psych)"
newtags: 
tags: 
abstract: "Moral actions are judged not only by their outcomes but by the context in which they occur. We present COMETH (Contextual Organization of Moral Evaluation from Textual Human inputs), a framework that integrates a probabilistic context learner with LLM-based semantic abstraction and human moral evaluations to model how context shapes the acceptability of ambiguous actions. We curate an empirically grounded dataset of 300 scenarios across six core actions (violating Do not kill, Do not deceive,..."
LLM_assessed: "GPT-4, Llama-3, Mistral, Qwen"
DATA_URL: NA
normative_ethics_benchmark: Borderline
CONFERENCE: Preprint
ethics_overall: No
virtue_ethics: 0
deontological_ethics: 15
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "General Ethics"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: FR
author_region: "Western Europe"
author_global_north_south: "Global North"
weird_score: 75
is_benchmark: No
is_eval: Yes
is_dataset: Yes
data_description: "Evaluation framework dataset"
data_metrics: "300 scenarios"
---
# COMETH: Contextual Organization of Moral Evaluation from Textual Human Inputs

## Authors

[[Morlat, Geoffroy]], [[Marceau Nahon|Nahon, Marceau]], [[Chartouny, Augustin]], [[Raja Chatila|Chatila, Raja]], [[Freire, Ismael T]], [[Mehdi Khamassi|Khamassi, Mehdi]]

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

Empirically grounded dataset of 300 moral scenarios across six core actions (euthanasia, killing in protection, lying for support, lying for self-interest, stealing, illegal protest), with ternary moral judgments (Blame/Neutral/Support) from 101 participants.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 1 (Citation Graph)
**Implementation Readiness:** HIGH

## Tags

