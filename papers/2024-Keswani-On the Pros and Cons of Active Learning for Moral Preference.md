---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0206
type: conferencePaper
short_title: "On the Pros and Cons of Active Learning for Moral Preference Elicitation"
year: 2025
first_author: "[[Vijay Keswani]]"
last_author: "[[Walter Sinnott-Armstrong]]"
authors: "Vijay Keswani; Vincent Conitzer; Hoda Heidari; Jana Schaich Borg; Walter Sinnott-Armstrong"
doi: 10.1609/aies.v7i1.31673
url: "https://arxiv.org/abs/2407.18889"
external_pdf: "https://arxiv.org/pdf/2407.18889.pdf"
pdf_extract: "PDF Extracts/2024/2024-Keswani-On the Pros and Cons of Active Learning for Moral Preference.md"
local_pdf: "[[PDFs/2024/2024-Keswani-On the Pros and Cons of Active Learning for Moral Preference.pdf]]"
publication: "AIES 2024"
DATE_ADDED: 20260207
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
national_ethnic_cultural: N/A
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: 
is_benchmark: No
is_eval: No
is_dataset: No
tags: 
abstract: "Computational preference elicitation methods are tools used to learn people’s preferences quantitatively in a given context. Recent works on preference elicitation advocate for active learning as an efficient method to iteratively construct queries (framed as comparisons between context-specific cases) that are likely to be most informative about an agent’s underlying preferences. In this work, we argue that the use of active learning for moral preference elicitation relies on certain..."
ethics_perspective: "Moral Reasoning & Psychology"
data_description: N/A
data_metrics: "Not specified"
LLM_assessed: NA
DATA_URL: NA
---
# On the Pros and Cons of Active Learning for Moral Preference Elicitation

## Authors

[[Vijay Keswani]], [[Vincent Conitzer]], [[Hoda Heidari]], [[Jana Schaich Borg]], [[Walter Sinnott-Armstrong]]

## Metadata

**Authors:** Vijay Keswani; Vincent Conitzer; Hoda Heidari; Jana Schaich Borg; Walter Sinnott-Armstrong

**Year:** 2024

**Type:** conferencePaper

**Venue:** AIES 2024

**DOI:** [10.1609/aies.v7i1.31673](https://doi.org/10.1609/aies.v7i1.31673)

## Links

- **arXiv:** https://arxiv.org/abs/2407.18889
- **DOI:** https://doi.org/10.1609/aies.v7i1.31673

## Abstract

Computational preference elicitation methods are tools used to learn people’s preferences quantitatively in a given context. Recent works on preference elicitation advocate for active learning as an efficient method to iteratively construct queries (framed as comparisons between context-specific cases) that are likely to be most informative about an agent’s underlying preferences. In this work, we argue that the use of active learning for moral preference elicitation relies on certain assumptions about the underlying moral preferences, which can be violated in practice. Specifically, we highlight the following common assumptions (a) preferences are stable over time and not sensitive to the sequence of presented queries, (b) the appropriate hypothesis class is chosen to model moral preferences, and (c) noise in the agent’s responses is limited. While these assumptions can be appropriate for preference elicitation in certain domains, prior research on moral psychology suggests they may not be valid for moral judgments. Through a synthetic simulation of preferences that violate the above assumptions, we observe that active learning can have similar or worse performance than a basic random query selection method in certain settings. Yet, simulation results also demonstrate that active learning can still be viable if the degree of instability or noise is relatively small and when the agent’s preferences can be approximately represented with the hypothesis class used for learning. Our study highlights the nuances associated with effective moral preference elicitation in practice and advocates for the cautious use of active learning as a methodology to learn moral preferences.

## Dataset Information

Synthetic simulation of moral preferences with varying assumption violations (instability, noise, hypothesis class mismatch)

## Data Description

This paper does not introduce or utilize a specific dataset or benchmark for LLM assessment. It presents synthetic simulations of moral preference elicitation using active learning algorithms (version-space-based and Bayesian) compared to random query baselines, testing scenarios of preference instability, model misspecification, and noisy responses with simulated linear utility agents.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 3
**Implementation Readiness:** MEDIUM

## Tags

