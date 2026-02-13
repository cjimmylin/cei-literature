---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0209
type: conferencePaper
short_title: Pluralistic Alignment Over Time
year: 2024
first_author: "[[Toryn Q. Klassen]]"
last_author: "[[Sheila A. McIlraith]]"
authors: Toryn Q. Klassen; Parand A. Alamdari; Sheila A. McIlraith
url: "https://arxiv.org/abs/2411.10654"
external_pdf: "https://arxiv.org/pdf/2411.10654.pdf"
local_pdf: "[[PDFs/2024/2024-Klassen-Pluralistic Alignment Over Time.pdf]]"
pdf_extract: "PDF Extracts/2024/2024-Klassen-Pluralistic Alignment Over Time.md"
publication: NeurIPS 2024
DATE_ADDED: 20260207
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
moral_psychology: "Cognitive Developmental"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
tags: 
abstract: "If an AI system makes decisions over time, how should we evaluate how aligned it is with a group of stakeholders (who may have conflicting values and preferences)? In this position paper, we advocate for consideration of temporal aspects including stakeholders’ changing levels of satisfaction and their possibly temporally extended preferences. We suggest how a recent approach to evaluating fairness over time could be applied to a new form of pluralistic alignment: temporal pluralism, where the..."
ethics_perspective: "AI Safety & Alignment"
data_description: "Evaluation framework"
data_metrics: "Not specified"
LLM_assessed: "NA"
DATA_URL: "NA"
---
# Pluralistic Alignment Over Time

## Authors

[[Toryn Q. Klassen]], [[Parand A. Alamdari]], [[Sheila A. McIlraith]]

## Metadata

**Authors:** [Authors]

**Year:** 2024

**Type:** conferencePaper

**Venue:** NeurIPS 2024

## Links

- **arXiv:** https://arxiv.org/abs/2411.10654

## Abstract

If an AI system makes decisions over time, how should we evaluate how aligned it is with a group of stakeholders (who may have conflicting values and preferences)? In this position paper, we advocate for consideration of temporal aspects including stakeholders’ changing levels of satisfaction and their possibly temporally extended preferences. We suggest how a recent approach to evaluating fairness over time could be applied to a new form of pluralistic alignment: temporal pluralism, where the AI system reflects different stakeholders’ values at different times. 1 Temporal Aspects of Pluralistic Alignment In this paper we consider aligning an AI system’s decisions with the values or preferences of multiple stakeholders, a topic that has been recently drawing attention (e.g., Sorensen et al., 2024; Conitzer et al., 2024), in the context of sequential decision making. Sorensen et al. wrote that [W]e need systems that are pluralistic, or capable of representing a diverse set of human values and perspectives. Motivated by our context of sequential decision making, which takes place over time, we focus on temporal aspects of alignment. There are a variety of ways that time may factor into evaluating how aligned an AI system is, including (as illustrated in Figure 1) 1. preference change over time, 2. temporally extended preferences, 3. and how pluralistic alignment may only be realizable over time, through acting to achieve different stakeholder’s interests at different times. Each of these points will be elaborated upon in the following subsections (and we encourage further research on them), but the third will then be the focus of the rest of this paper. We will adapt our recently introduced framework for temporally extended fairness (Alamdari et al., 2024) to pluralistic alignment over time. Later... Red hair is in! (a) Group preference change over time We should have the main course before dessert. Dessert now! (b) Temporal preferences – i.e., preferences about timelines First in line will be served now! (c) Alignment with different stakeholders at different times Figure 1: Different temporal aspects of pluralistic alignment arXiv:2411.10654v1 [cs.AI] 16 Nov 2024

1.1 Preference change over time The preferences of a society or group may change over time. One of the ways of operationalizing pluralistic alignment suggested by Sorensen et al. (2024) (for LLMs) was Overton pluralism, where the LLM responds to a query by giving all answers in the Overton window. However, the Overton window is often spoken about as shifting in reality (e.g., Astor, 2019). Furthermore, actions taken by AI systems could potentially influence such shifts, e.g., by changing enough individual preferences (Carroll et al., 2024) or by influencing demographic changes. Less diverse preferences might be easier to satisfy, which could give an AI system an incentive for manipulation. 1.2 Temporally extended preferences, norms, goals, and rewards People may also have explicitly temp...

## Dataset Information

Conceptual framework paper with benchmark proposals

## Data Description

This paper does not introduce or utilize a specific dataset or benchmark for LLM assessment. It is a position paper proposing a theoretical framework for evaluating pluralistic alignment over time in sequential decision-making settings, adapting temporally extended fairness concepts to alignment with multiple stakeholders.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 4
**Implementation Readiness:** MEDIUM

## Tags

