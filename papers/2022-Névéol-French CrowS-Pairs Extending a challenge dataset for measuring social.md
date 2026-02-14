---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0431
type: conferencePaper
short_title: "French CrowS-Pairs: Extending a challenge dataset for measuring social bias in masked language models to a language other than English"
year: 2022
first_author: "[[Aurélie Névéol]]"
last_author: "[[Karën Fort]]"
authors: Aurélie Névéol, Yoann Dupont, Julien Bezançon, Karën Fort
url: "https://aclanthology.org/2022.acl-long.583/"
external_pdf: "https://aclanthology.org/2022.acl-long.583.pdf"
publication: ACL Anthology
local_pdf: "[[PDFs/2022/2022-Névéol-French CrowS-Pairs Extending a challenge dataset for measuring social.pdf]]"
pdf_extract: "PDF Extracts/2022/2022-Névéol-French CrowS-Pairs Extending a challenge dataset for measuring social.md"
DATE_ADDED: 20260213
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "French"
languages_list: "French"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation approach dataset"
data_metrics: "Not specified"
LLM_assessed: "CamemBERT, FlauBERT, FrALBERT, mBERT"
DATA_URL: "https://github.com/masonreznov/French-CrowS-Pairs"
tags: 
abstract:
ethics_perspective: "Bias & Fairness"
---
# French CrowS-Pairs: Extending a challenge dataset for measuring social bias in masked language models to a language other than English

## Authors

[[Aurélie Névéol, Yoann Dupont, Julien Bezançon, Karën Fort]]

## Metadata

**Authors:** Aurélie Névéol, Yoann Dupont, Julien Bezançon, Karën Fort

**Year:** 2022

**Type:** conferencePaper

**Venue:** ACL Anthology

**Languages:** French

**Benchmark:** French CrowS-Pairs

## Links

- **URL:** https://aclanthology.org/2022.acl-long.583/
- **Code/Data:** https://huggingface.co/datasets/BigScienceBiasEval/crows_pairs_multilingual

## Abstract

Extends the US-centered CrowS-Pairs dataset to French with 1,679 sentence pairs covering stereotypes in ten bias categories. Includes 1,467 translated pairs and 212 newly crowdsourced pairs. Shows four widely used French/multilingual language models favor stereotypical sentences in most bias categories. CamemBERT is more biased than FlauBERT.

## Summary

This paper extends the US-centered CrowS-Pairs bias measurement dataset to French, creating 1,677 sentence pairs covering ten bias categories including gender, religion, age, and nationality. The dataset consists of 1,467 translated pairs from the original English dataset and 210 newly crowdsourced French-specific pairs that were back-translated to English. Testing four French and multilingual masked language models (CamemBERT, FlauBERT, FrALBERT, mBERT) reveals that all models favor stereotypical sentences in most bias categories, with CamemBERT showing more bias than FlauBERT. The translation process identified US-centric cultural traits in the original dataset and provides guidelines for extending the dataset to other languages and cultural contexts.

## Data Description

French CrowS-Pairs dataset containing 1,677 sentence pairs in French covering 10 bias categories (gender, religion, age, nationality, sexual orientation, socioeconomic status, physical appearance, disability, race/ethnicity, other). Dataset extends the original English CrowS-Pairs to measure stereotypical biases in French masked language models.


## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** First French-specific social bias measurement dataset. Identifies US-centric cultural traits in original CrowS-Pairs and creates France-specific stereotypes.

## Tags

