---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: QMQDCW4X
type: conferencePaper
short_title: ProsocialDialog
year: 2025
first_author: "[[Hyunwoo Kim]]"
last_author: "[[Maarten Sap]]"
authors: "Hyunwoo Kim; Youngjae Yu; Liwei Jiang; Ximing Lu; Daniel Khashabi; Gunhee Kim; Yejin Choi; Maarten Sap"
doi: 10.48550/arXiv.2205.12688
tags: 
url: "http://arxiv.org/abs/2205.12688"
external_pdf: "http://arxiv.org/pdf/2205.12688.pdf"
publication: "Conference on Empirical Methods in Natural Language Processing"
national_ethnic_cultural: N/A
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: "AI Safety & Alignment"
key_contribution: "Introduced ProsocialDialog, a large-scale multi-turn dialogue dataset (58K dialogues) designed to teach agents to respond to toxic or unethical content with prosocial, rule-grounded guidance."
significance: "Moves beyond simple toxicity suppression (blocking/ignoring) to active prosocial intervention, equipping agents with the ability to explain *why* a statement is problematic using commonsense social rules (Rules-of-Thumb)."
pdf_extract: "PDF Extracts/0000/2022-Kim-ProsocialDialog.md"
abstract: "Most existing dialogue systems fail to re- spond properly to potentially unsafe user ut- terances by either ignoring or passively agree- ing with them. To address this issue, we intro- duce PROSOCIALDIALOG, the ﬁrst large-scale multi-turn dialogue dataset to teach conversa- tional agents to respond to problematic con- tent following social norms. Covering diverse unethical, problematic, biased, and toxic situa- tions, PROSOCIALDIALOG contains responses that encourage prosocial behavior, grounded"
paper_summary: "Abstract: Most existing dialogue systems fail to re- spond properly to potentially unsafe user ut- terances by either ignoring or passively agree- ing with them. To address this issue, we intro- duce PROSOCIALD | Overview: PROSOCIALDIALOG: A Prosocial Backbone for Conversational Agents Hyunwoo Kim♥♠∗ Youngjae Yu♥∗Liwei Jiang♥♣ Ximing Lu♥♣ Daniel Khashabi♦ Gunhee Kim♠ Yejin Choi♥♣ Maarten Sap♥♦ ♥Allen Institute for Artiﬁ | Key Findings: between dialogue agents on response generation for PROSOCIALDIALOG (in percentages; §5.2). Evaluation metrics. We conduct both auto- matic and human e | Conclusions: We introduced PROSOCIALDIALOG, a large-scale English dialogue dataset providing constructive feedback for prosocial behaviors aligned with com- monsen"
local_pdf: "[[PDFs/2022/2022-Kim-ProsocialDialog.pdf]]"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "AI Safety & Alignment"
is_benchmark: No
is_eval: No
is_dataset: Yes
data_description: "Dataset for toxicity detection"
data_metrics: "Not specified"
LLM_assessed: "GPT-3, InstructGPT, GPT-2, T5"
DATA_URL: "https://hyunw.kim/prosocial-dialog"
DATE_ADDED: 20260207
---
# ProsocialDialog: A Prosocial Backbone for Conversational Agents

## Metadata

**Authors:** Kim, Hyunwoo; Yu, Youngjae; Jiang, Liwei; Lu, Ximing; Khashabi, Daniel; Kim, Gunhee; Choi, Yejin; Sap, Maarten

**Year:** 2022

**Type:** preprint

**DOI:** [10.48550/arXiv.2205.12688](https://doi.org/10.48550/arXiv.2205.12688)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2022/2022-Kim-ProsocialDialog.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2205.12688
- **DOI:** https://doi.org/10.48550/arXiv.2205.12688

## Abstract

Most existing dialogue systems fail to respond properly to potentially unsafe user utterances by either ignoring or passively agreeing with them. To address this issue, we introduce PROSOCIALDIALOG, the ﬁrst large-scale multi-turn dialogue dataset to teach conversational agents to respond to problematic content following social norms. Covering diverse unethical, problematic, biased, and toxic situations, PROSOCIALDIALOG contains responses that encourage prosocial behavior, grounded in commonsense social rules (i.e., rules-ofthumb, RoTs). Created via a human-AI collaborative framework, PROSOCIALDIALOG consists of 58K dialogues, with 331K utterances, 160K unique RoTs, and 497K dialogue safety labels accompanied by free-form rationales.

## Authors

[[Hyunwoo Kim]], [[Youngjae Yu]], [[Liwei Jiang]], [[Ximing Lu]], [[Daniel Khashabi]], [[Gunhee Kim]], [[Yejin Choi]], [[Maarten Sap]]

## Data Description

PROSOCIALDIALOG is a large-scale dataset of 58K dialogues where a speaker responds prosocially to potentially unsafe conversational situations, grounded in rules-of-thumb (RoTs) from Social Chemistry. GPT-3 generates problematic utterances in the data collection pipeline. GPT-3, Instruct GPT-3, GPT-2, DialoGPT, and T5 are evaluated as baselines in safety classification and response generation tasks (Tables 2-4), with head-to-head human evaluations against the trained Prost model.


## Notes


## Tags

#Computer-Science---Computation-and-Language

## Citation Info

463 citations (Semantic Scholar/arXiv) [2025-08-27] 128 citations (Semantic Scholar/DOI) [2025-08-27] 128 citations (Semantic Scholar/DOI) [2025-08-23]
