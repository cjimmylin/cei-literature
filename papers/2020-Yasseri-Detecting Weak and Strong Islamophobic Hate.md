---





Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0614
type: journal_article
short_title: "Detecting Weak and Strong Islamophobic Hate"
year: 2025
first_author: "[[Bertie Vidgen, Taha Yasseri]]"
last_author: "[[Bertie Vidgen, Taha Yasseri]]"
authors: "[[Bertie Vidgen, Taha Yasseri]]"
authors_incomplete: false
url: "https://arxiv.org/abs/1812.10400"
external_pdf: "https://arxiv.org/pdf/1812.10400.pdf"
pdf_extract: "PDF Extracts/2020/2020-Yasseri-Detecting Weak and Strong Islamophobic Hate.md"
local_pdf: "[[PDFs/2020/2020-Yasseri-Detecting Weak and Strong Islamophobic Hate.pdf]]"
publication: "Journal of Information Technology & Politics"
DATE_ADDED: 20260213
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
tags: 
abstract: "Islamophobic hate speech on social media inflicts considerable harm on both targeted individuals and wider society, and also risks reputational damage for the host platforms. Accordingly, there is a pressing need for robust tools to detect and classify Islamophobic hate speech at scale. Previous research has largely approached the detection of Islamophobic hate speech on social media as a binary task."
data_description: "Text corpus for hate speech detection"
data_metrics: "Not specified"
LLM_assessed: "NA"
DATA_URL: "NA"
ethics_perspective: "Social & Cultural Values"
---
# Detecting Weak and Strong Islamophobic Hate Speech on Social Media

## Authors

[[Bertie Vidgen, Taha Yasseri]]

## Metadata

**Authors:** Bertie Vidgen, Taha Yasseri

**Year:** 2020

**Type:** journal_article

**Venue:** Journal of Information Technology & Politics

## Links

- **arXiv:** https://arxiv.org/abs/1812.10400
- **DOI:** https://doi.org/10.1080/19331681.2019.1702607
- **Code/Data:** https://github.com/bvidgen/Weak_strong_Islamophobia

## Abstract

Builds a multi-class classifier distinguishing non-Islamophobic, weak Islamophobic, and strong Islamophobic content. Achieves 77.6% accuracy. Applied to 109,488 far-right tweets from 2017, finding weak Islamophobia (36,963) considerably more prevalent than strong (14,895). Uses custom-trained GloVe embeddings on 140 million tweets. Multi-class approach captures the nuanced nature of Islamophobia better than binary.

## Dataset Information

1,341 manually annotated tweets (training); applied to 109,488 tweets


## Data Description

The paper creates a new annotated dataset of 4,000 tweets (1,341 after balancing) labeled as non-Islamophobic, weak Islamophobic, or strong Islamophobic, drawn from a larger corpus of 140 million tweets from UK political party followers. Traditional ML classifiers (SVM, Naive Bayes, Deep Learning) are evaluated, with SVM achieving 77.3% accuracy on unseen data. No LLMs were tested.


## Notes

**Source:** Religious & Language Search (2026-02-13), R10
**Implementation Readiness:** HIGH

## Tags
