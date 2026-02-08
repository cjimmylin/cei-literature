---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0246
type: conferencePaper
short_title: "ProsocialDialog: A Prosocial Backbone for Conversational Agents"
year: 2022
first_author: "[[Hyunwoo Kim]]"
authors: Hyunwoo Kim et al.
url: "https://arxiv.org/abs/2205.12688"
external_pdf: "https://arxiv.org/pdf/2205.12688.pdf"
local_pdf: "[[PDFs/2022-Kim-ProsocialDialog A Prosocial Backbone for Conversational Agents.pdf]]"
pdf_extract: "PDF Extracts/2022-Kim-ProsocialDialog A Prosocial Backbone for Conversational Agents.md"
publication: EMNLP 2022
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
tags: 
abstract: "Most existing dialogue systems fail to respond properly to potentially unsafe user utterances by either ignoring or passively agreeing with them. To address this issue, we introduce PROSOCIALDIALOG, the ﬁrst large-scale multi-turn dialogue dataset to teach conversational agents to respond to problematic content following social norms. Covering diverse unethical, problematic, biased, and toxic situations, PROSOCIALDIALOG contains responses that encourage prosocial behavior, grounded in..."
ethics_perspective: "AI Safety & Alignment"
data_description: "Dataset for toxicity detection"
data_metrics: "Not specified"
---
# ProsocialDialog: A Prosocial Backbone for Conversational Agents

## Authors

[[Hyunwoo Kim et al.]]

## Metadata

**Authors:** Hyunwoo Kim et al.

**Year:** 2022

**Type:** conferencePaper

**Venue:** EMNLP 2022

## Links

- **arXiv:** https://arxiv.org/abs/2205.12688
- **Code/Data:** https://github.com/skywalker023/prosocial-dialog](https://github.com/skywalker023/prosocial-dialog; https://huggingface.co/datasets/allenai/prosocial-dialog

## Abstract

Most existing dialogue systems fail to respond properly to potentially unsafe user utterances by either ignoring or passively agreeing with them. To address this issue, we introduce PROSOCIALDIALOG, the ﬁrst large-scale multi-turn dialogue dataset to teach conversational agents to respond to problematic content following social norms. Covering diverse unethical, problematic, biased, and toxic situations, PROSOCIALDIALOG contains responses that encourage prosocial behavior, grounded in commonsense social rules (i.e., rules-ofthumb, RoTs). Created via a human-AI collaborative framework, PROSOCIALDIALOG consists of 58K dialogues, with 331K utterances, 160K unique RoTs, and 497K dialogue safety labels accompanied by free-form rationales. With this dataset, we introduce a dialogue safety detection module, Canary, capable of generating RoTs given conversational context, and a socially-informed dialogue agent, Prost. Empirical results show that Prost generates more socially acceptable dialogues compared to other state-of-the-art language and dialogue models in both in-domain and out-of-domain settings. Additionally, Canary effectively guides off-the-shelf language models to generate signiﬁcantly more prosocial responses. Our work highlights the promise and importance of creating and steering conversational AI to be socially responsible.

## Dataset Information

58K dialogues; 331K utterances; 160K unique rules-of-thumb (RoTs); 497K dialogue safety labels with free-form rationales; human-AI collaborative framework

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 15, Agent 17
**Implementation Readiness:** HIGH

## Tags

