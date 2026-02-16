---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 5K3XEJ5L
type: conferencePaper
short_title: "Case Law Grounding"
year: 2025
first_author: "[[Quan Ze Chen]]"
last_author: "[[Amy X. Zhang]]"
authors: "Quan Ze Chen; Amy X. Zhang"
doi: 10.48550/arXiv.2310.07019
tags: 
url: "http://arxiv.org/abs/2310.07019"
external_pdf: "http://arxiv.org/pdf/2310.07019.pdf"
publication: "International Conference on Climate Informatics"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
pdf_extract: "PDF Extracts/2023/2023-Chen-Case Law Grounding.md"
abstract: "From moderating content within an online community to producing socially-appropriate generative outputs, decision-making tasks— conducted by either humans or AI—often depend on subjective or socially-established criteria. To ensure such decisions are consistent, prevailing processes primarily make use of high-level rules and guidelines to ground decisions, similar to applying “constitutions” in the legal context."
paper_summary: "Abstract: From moderating content within an online community to producing socially-appropriate generative outputs, decision-making tasks— conducted by either humans or AI—often depend on subjective or socially- | Overview: Case Law Grounding: Using Precedents to Align Decision-Making for Humans and AI Quan Ze Chen cqz@cs.washington.edu University of Washington Seattle, WA, USA Amy X. Zhang axz@cs.washington.edu Universi | Methodology: can be implemented in both human and AI decision-making con- texts, introducing both a human-led process and a large language model (LLM) prompting se | Conclusions: 5.1 Limitations of Our Implementation In this work, we explored a relatively simple implementation of case law for grounding decisions where reasoning"
local_pdf: "[[PDFs/2023/2023-Chen-Case Law Grounding.pdf]]"
DATE_ADDED: 20260208
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "NLP & Representation Learning"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation approach"
data_metrics: "Not specified"
LLM_assessed: GPT-4
DATA_URL: NA
---
# Case Law Grounding: Using Precedents to Align Decision-Making for Humans and AI

## Metadata

**Authors:** Chen, Quan Ze; Zhang, Amy X.

**Year:** 2025

**Type:** preprint

**DOI:** [10.48550/arXiv.2310.07019](https://doi.org/10.48550/arXiv.2310.07019)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2023/2023-Chen-Case Law Grounding.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2310.07019
- **DOI:** https://doi.org/10.48550/arXiv.2310.07019

## Abstract

From moderating content within an online community to producing socially-appropriate generative outputs, decision-making tasks—conducted by either humans or AI—often depend on subjective or socially-established criteria. To ensure such decisions are consistent, prevailing processes primarily make use of high-level rules and guidelines to ground decisions, similar to applying “constitutions” in the legal context. However, inconsistencies in specifying and interpreting constitutional grounding can lead to undesirable and even incorrect decisions being made. In this work, we introduce “case law grounding” (CLG)—an approach for grounding subjective decision-making using past decisions, similar to how precedents are used in case law. We present how this grounding approach can be implemented in both human and AI decision-making contexts, introducing both a human-led process and a large language model (LLM) prompting setup. Evaluating with five groups and communities across two decision-making task domains, we find that decisions produced with CLG were significantly more accurately aligned to ground truth in 4 out of 5 groups, achieving a 16.0–23.3 %-points higher accuracy in the human process, and 20.8–32.9 %points higher with LLMs. We also examined the impact of different configurations with the retrieval window size and binding nature of decisions and find that binding decisions and larger retrieval windows were beneficial. Finally, we discuss the broader implications of using CLG to augment existing constitutional grounding when it comes to aligning human and AI decisions.

## Authors

[[Quan Ze Chen]], [[Amy X. Zhang]]

## Data Description

The study evaluates case law grounding (CLG) using two decision-making task datasets: a Reddit comment moderation dataset (NormVio) with binary keep/remove decisions across three subreddit communities, and a toxicity rating dataset with 5-point scale ratings across two demographic groups. Human annotations were collected from 95 participants, and GPT-4-turbo-preview was used for the LLM-prompting version of the approach.


## Notes


## Tags

#Computer-Science---Human-Computer-Interaction

## Citation Info

101 citations (Semantic Scholar/DOI) [2025-08-27] 2 citations (Semantic Scholar/arXiv) [2025-08-23]
