---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0090
type: conferencePaper
short_title: Moral Alignment for LLM Agents (Intrinsic Rewards)
year: 2025
first_author: "[[Elizaveta Tennant]]"
authors: Elizaveta Tennant; Stephen Hailes; Mirco Musolesi
url: "https://arxiv.org/abs/2410.01639"
external_pdf: "https://arxiv.org/pdf/2410.01639.pdf"
local_pdf: "[[PDFs/2025/2025-Tennant-Moral Alignment for LLM Agents Intrinsic Rewards.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Tennant-Moral Alignment for LLM Agents Intrinsic Rewards.md"
publication: ICLR 2025
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "Yes"
utilitarian_ethics: "Yes"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
tags: 
abstract: "Decision-making agents based on pre-trained Large Language Models (LLMs) are increasingly being deployed across various domains of human activity. While their applications are currently rather specialized, several research efforts are underway to develop more generalist agents. As LLM-based systems become more agentic, their influence on human activity will grow and their transparency will decrease. Consequently, developing effective methods for aligning them to human values is vital."
data_description: "Evaluation framework"
data_metrics: "Not specified"
normative_ethics_benchmark: Yes
---
# Moral Alignment for LLM Agents (Intrinsic Rewards)

## Authors

[[Elizaveta Tennant]], [[Stephen Hailes]], [[Mirco Musolesi]]

## Metadata

**Authors:** Elizaveta Tennant; Stephen Hailes; Mirco Musolesi

**Year:** 2025

**Type:** conferencePaper

**Venue:** ICLR 2025

## Links

- **arXiv:** https://arxiv.org/abs/2410.01639
- **Code/Data:** https://github.com/liza-tennant/LLM_morality

## Abstract

Decision-making agents based on pre-trained Large Language Models (LLMs) are increasingly being deployed across various domains of human activity. While their applications are currently rather specialized, several research efforts are underway to develop more generalist agents. As LLM-based systems become more agentic, their influence on human activity will grow and their transparency will decrease. Consequently, developing effective methods for aligning them to human values is vital. The prevailing practice in alignment often relies on human preference data (e.g., in RLHF or DPO), in which values are implicit, opaque and are essentially deduced from relative preferences over different model outputs. In this work, instead of relying on human feedback, we introduce the design of reward functions that explicitly and transparently encode core human values for Reinforcement Learningbased fine-tuning of foundation agent models. Specifically, we use intrinsic rewards for the moral alignment of LLM agents. We evaluate our approach using the traditional philosophical frameworks of Deontological Ethics and Utilitarianism, quantifying moral rewards for agents in terms of actions and consequences on the Iterated Prisoner’s Dilemma (IPD) environment. We also show how moral fine-tuning can be deployed to enable an agent to unlearn a previously developed selfish strategy. Finally, we find that certain moral strategies learned on the IPD game generalize to several other matrix game environments. In summary, we demonstrate that fine-tuning with intrinsic rewards is a promising general solution for aligning LLM agents to human values, and it might represent a more transparent and cost-effective alternative to currently predominant alignment techniques.

## Dataset Information

See report

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 7-8, Agent 18
**Implementation Readiness:** HIGH

## Tags

