---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0251
type: preprint
short_title: "EmpatheticDialogues: Towards Empathetic Open-domain Conversation Models"
year: 2019
first_author: "[[Hannah Rashkin]]"
last_author: "[[Y-Lan Boureau]]"
authors: Hannah Rashkin; Eric Michael Smith; Margaret Li; Y-Lan Boureau
url: "https://arxiv.org/abs/1811.00207"
external_pdf: "https://arxiv.org/pdf/1811.00207.pdf"
local_pdf: "[[PDFs/2019/2019-Rashkin-EmpatheticDialogues Towards Empathetic Open-domain Conversation Models.pdf]]"
pdf_extract: "PDF Extracts/2019/2019-Rashkin-EmpatheticDialogues Towards Empathetic Open-domain Conversation Models.md"
publication: arXiv
DATE_ADDED: 20260207
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
tags: 
abstract: "One challenge for dialogue agents is recognizing feelings in the conversation partner and replying accordingly, a key communicative skill. While it is straightforward for humans to recognize and acknowledge others’ feelings in a conversation, this is a signiﬁcant challenge for AI systems due to the paucity of suitable publicly-available datasets for training and evaluation. This work proposes a new benchmark for empathetic dialogue generation and EMPATHETICDIALOGUES, a novel dataset of 25k..."
research_topic: "Dialogue Systems"
data_description: "Benchmark dataset for conversational ai"
data_metrics: "Not specified"
LLM_assessed: "BERT"
DATA_URL: "https://github.com/facebookresearch/EmpatheticDialogues"
---
# EmpatheticDialogues: Towards Empathetic Open-domain Conversation Models

## Authors

[[Hannah Rashkin]], [[Eric Michael Smith]], [[Margaret Li]], [[Y-Lan Boureau]]

## Metadata

**Authors:** Hannah Rashkin; Eric Michael Smith; Margaret Li; Y-Lan Boureau

**Year:** 2019

**Type:** preprint

**Venue:** arXiv

## Links

- **arXiv:** https://arxiv.org/abs/1811.00207
- **Code/Data:** https://github.com/facebookresearch/EmpatheticDialogues](https://github.com/facebookresearch/EmpatheticDialogues; https://huggingface.co/datasets/facebook/empathetic_dialogues

## Abstract

One challenge for dialogue agents is recognizing feelings in the conversation partner and replying accordingly, a key communicative skill. While it is straightforward for humans to recognize and acknowledge others’ feelings in a conversation, this is a signiﬁcant challenge for AI systems due to the paucity of suitable publicly-available datasets for training and evaluation. This work proposes a new benchmark for empathetic dialogue generation and EMPATHETICDIALOGUES, a novel dataset of 25k conversations grounded in emotional situations. Our experiments indicate that dialogue models that use our dataset are perceived to be more empathetic by human evaluators, compared to models merely trained on large-scale Internet conversation data. We also present empirical comparisons of dialogue model adaptations for empathetic responding, leveraging existing models or datasets without requiring lengthy retraining of the full model.

## Dataset Information

25,000 conversations; 32 emotion labels; grounded in emotional situations; human-to-human dialogues

## Data Description

The EmpatheticDialogues dataset comprises 24,850 crowdsourced one-on-one conversations grounded in emotional situations across 32 emotion labels, gathered from 810 participants via Amazon Mechanical Turk. The dataset is split into 19,533 train, 2,770 validation, and 2,547 test conversations, with an average of 4.31 utterances per conversation and 15.2 words per utterance. It serves as a benchmark for evaluating empathetic dialogue generation in open-domain conversation models.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 15, Agent 1
**Implementation Readiness:** HIGH

## Tags

