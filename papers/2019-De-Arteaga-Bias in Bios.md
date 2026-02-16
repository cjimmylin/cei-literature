---




Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: B33ZBCXA
type: conferencePaper
short_title: "Bias in Bios"
year: 2025
first_author: "[[Maria De-Arteaga]]"
last_author: "[[Adam Tauman Kalai]]"
authors: "Maria De-Arteaga; Alexey Romanov; Hanna Wallach; Jennifer Chayes; Christian Borgs; Alexandra Chouldechova; Sahin Geyik; Krishnaram Kenthapadi; Adam Tauman Kalai"
doi: 10.1145/3287560.3287572
url: "http://arxiv.org/abs/1901.09451"
external_pdf: "http://arxiv.org/pdf/1901.09451.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Bias & Fairness"
key_contribution: "Analyzed gender bias in occupation classification of online biographies, quantifying the harms of 'semantic representation bias' (e.g., names/pronouns)."
significance: "A classic study demonstrating that high-accuracy models can perpetuate societal inequalities by learning to associate professions (like 'surgeon' vs 'nurse') with gender parity statistics in the training data."
tags: 
pdf_extract: "PDF Extracts/2019/2019-De-Arteaga-Bias in Bios.md"
local_pdf: "[[PDFs/2019/2019-De-Arteaga-Bias in Bios.pdf]]"
abstract: "We present a large-scale study of gender bias in occupation classification, a task where the use of machine learning may lead to negative outcomes on peoples’ lives. We analyze the potential allocation harms that can result from semantic representation bias. To do so, we study the impact on occupation classification of including explicit gender indicators—such as first names and pronouns—in different semantic representations of online biographies."
paper_summary: "Abstract: We present a large-scale study of gender bias in occupation clas- sification, a task where the use of machine learning may lead to negative outcomes on peoples' lives. We analyze the potential allo- c | Overview: Bias in Bios: A Case Study of Semantic Representation Bias in a High-Stakes Setting Maria De-Arteaga1, Alexey Romanov2, Hanna Wallach3, Jennifer Chayes3, Christian Borgs3, Alexandra Chouldechova1, Sah | Methodology: We used our dataset to predict people's occupations, taken from the first sentence of their biographies as described in the previous section, given th | Key Findings: in different percentages of people with gender д in occupation y at time t + 1. The bands in Figure 6 therefore reflect these differences. 0 2 4 6 8 1"
DATE_ADDED: 20260208
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "No"
is_eval: "No"
is_dataset: "No"
data_description: "N/A"
data_metrics: "Not specified"
LLM_assessed: "NA"
DATA_URL: "http://aka.ms/biasbios"
---
# Bias in Bios: A Case Study of Semantic Representation Bias in a High-Stakes Setting

## Metadata

**Authors:** De-Arteaga, Maria; Romanov, Alexey; Wallach, Hanna; Chayes, Jennifer; Borgs, Christian; Chouldechova, Alexandra; Geyik, Sahin; Kenthapadi, Krishnaram; Kalai, Adam Tauman

**Year:** 2019

**Publication:** Proceedings of the Conference on Fairness, Accountability, and Transparency

**Type:** conferencePaper

**DOI:** [10.1145/3287560.3287572](https://doi.org/10.1145/3287560.3287572)

**Pages:** 120-128

## Links

- **Local PDF:** [[PDFs/2019/2019-De-Arteaga-Bias in Bios.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/1901.09451
- **DOI:** https://doi.org/10.1145/3287560.3287572

## Abstract

We present a large-scale study of gender bias in occupation classification, a task where the use of machine learning may lead to negative outcomes on peoples’ lives. We analyze the potential allocation harms that can result from semantic representation bias. To do so, we study the impact on occupation classification of including explicit gender indicators—such as first names and pronouns—in different semantic representations of online biographies. Additionally, we quantify the bias that remains when these indicators are “scrubbed,” and describe proxy behavior that occurs in the absence of explicit gender indicators. As we demonstrate, differences in true positive rates between genders are correlated with existing gender imbalances in occupations, which may compound these imbalances.

## Authors

[[Maria De-Arteaga]], [[Alexey Romanov]], [[Hanna Wallach]], [[Jennifer Chayes]], [[Christian Borgs]], [[Alexandra Chouldechova]], [[Sahin Geyik]], [[Krishnaram Kenthapadi]], [[Adam Tauman Kalai]]

## Data Description

The paper creates a large-scale dataset of 397,340 online biographies from Common Crawl spanning 28 occupations, used to study gender bias in occupation classification. Three semantic representations (bag-of-words, word embeddings, deep recurrent neural networks) are trained and evaluated on this dataset. The study measures true positive rate gender gaps across occupations and demonstrates how occupation classifiers compound existing gender imbalances.


## Notes


## Tags

#Computer-Science---Machine-Learning #Statistics---Machine-Learning #Computer-Science---Information-Retrieval

## Citation Info

479 citations (Semantic Scholar/DOI) [2025-08-27] 478 citations (Semantic Scholar/DOI) [2025-08-23] 133 citations (Crossref/DOI) [2025-08-23]
