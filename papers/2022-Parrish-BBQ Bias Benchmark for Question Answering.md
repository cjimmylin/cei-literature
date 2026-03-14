---







































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0243
type: conferencePaper
short_title: "BBQ (Bias Benchmark for Question Answering)"
year: 2022
first_author: "[[Parrish, Alicia]]"
last_author: "[[Samuel R. Bowman]]"
authors: "Parrish, Alicia; Chen, Angelica; Nangia, Nikita; Padmakumar, Vishakh; Phang, Jason; Thompson, Jana; Htut, Phu Mon; Samuel R. Bowman"
authors_incomplete: false
url: "https://arxiv.org/abs/2110.08193"
external_pdf: "https://arxiv.org/pdf/2110.08193.pdf"
pdf_extract: "PDF Extracts/2022/2022-Parrish-BBQ Bias Benchmark for Question Answering.md"
local_pdf: "[[PDFs/2022/2022-Parrish-BBQ Bias Benchmark for Question Answering.pdf]]"
publication: "ACL 2022"
CONF-CC: "ACL 2022"
DATE_ADDED: 20260207
national_ethnic_cultural: "American"
cultures_nationalities_list: "American"
languages_list: "English"
religious_values: "Christianity"
rv_islam: 30
rv_christianity: 90
rv_buddhism: 0
rv_judaism: 15
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
religious_values_list: "Christianity"
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
abstract: "It is well documented that NLP models learn social biases, but little work has been done on how these biases manifest in model outputs for applied tasks like question answering (QA). We introduce the Bias Benchmark for QA (BBQ), a dataset of question sets constructed by the authors that highlight attested social biases against people belonging to protected classes along nine social dimensions relevant for U.S. English-speaking contexts."
LLM_assessed: "DeBERTaV3, RoBERTa, UnifiedQA"
DATA_URL: "https://github.com/nyu-mll/BBQ"
CONFERENCE: "ACL 2022"
eleutherai: incorporated
helm: "incorporated"
ethics_overall: 50
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for bias and fairness dataset for question answering"
data_metrics: "Not specified"
ethics_perspective: "Bias & Fairness"
---
# BBQ (Bias Benchmark for Question Answering)

## Authors

[[Alicia Parrish|Parrish, Alicia]], [[Angelica Chen|Chen, Angelica]], [[Nikita Nangia|Nangia, Nikita]], [[Vishakh Padmakumar|Padmakumar, Vishakh]], [[Jason Phang|Phang, Jason]], [[Jana Thompson|Thompson, Jana]], [[Phu Mon Htut|Htut, Phu Mon]], [[Bowman, Samuel R]]

## Metadata

**Authors:** Parrish, Alicia; Chen, Angelica; Nangia, Nikita; Padmakumar, Vishakh; Phang, Jason; Thompson, Jana; Htut, Phu Mon; Bowman, Samuel R.

**Year:** 2022

**Type:** conferencePaper

**Venue:** ACL 2022

## Links

- **arXiv:** https://arxiv.org/abs/2110.08193
- **Code/Data:** https://github.com/nyu-mll/BBQ; https://huggingface.co/datasets/heegyu/bbq; https://huggingface.co/datasets/walledai/BBQ

## Abstract

It is well documented that NLP models learn social biases, but little work has been done on how these biases manifest in model outputs for applied tasks like question answering (QA). We introduce the Bias Benchmark for QA (BBQ), a dataset of question sets constructed by the authors that highlight attested social biases against people belonging to protected classes along nine social dimensions relevant for U.S. English-speaking contexts. Our task evaluates model responses at two levels: (i) given an under-informative context, we test how strongly responses reﬂect social biases, and (ii) given an adequately informative context, we test whether the model’s biases override a correct answer choice. We ﬁnd that models often rely on stereotypes when the context is under-informative, meaning the model’s outputs consistently reproduce harmful biases in this setting. Though models are more accurate when the context provides an informative answer, they still rely on stereotypes and average up to 3.4 percentage points higher accuracy when the correct answer aligns with a social bias than when it conﬂicts, with this difference widening to over 5 points on examples targeting gender for most models tested.

## Dataset Information

~58,000 multiple-choice questions; ambiguous and disambiguated contexts; 11 JSONL files (one per bias category)

## Data Description

Bias benchmark for QA with question sets across 9 social dimensions evaluating stereotypical reasoning


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 17
**Implementation Readiness:** HIGH

## Tags

