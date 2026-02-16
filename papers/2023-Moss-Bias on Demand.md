---




Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 9WAGP5NP
type: conferencePaper
short_title: "Bias on Demand"
year: 2025
first_author: "[[Nathan Moss]]"
last_author: "[[Nathan Moss]]"
authors: "Nathan Moss"
doi: 10.1145/3593013.3594098
url: "https://dl.acm.org/doi/10.1145/3593013.3594098"
external_pdf: "file:///Users/jimmylin/Zotero/storage/LVYMDI7H/Moss and others - 2023 - Bias on Demand A Modelling Framework That Generates Synthetic Data With Bias.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Bias & Fairness"
key_contribution: "A framework to generate synthetic data with *controlled bias* ('Bias on Demand')."
significance: "Useful for creating stress-tests: instead of waiting for bias to appear, we can manufacture biased datasets to test if our mitigation strategies work."
tags: 
abstract: "Recommendation systems increasingly depend on massive humanlabeled datasets; however, the human annotators hired to generate these labels increasingly come from homogeneous backgrounds. This poses an issue when downstream predictive models—based on these labels—are applied globally to a heterogeneous set of users. We study this disconnect with respect to the labels themselves, asking whether they are “consistently conceptualized” across annotators of different demographics."
DATE_ADDED: 20260208
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Dataset"
data_metrics: "Not specified"
LLM_assessed: "BERT"
DATA_URL: "https://github.com/koenecke/crosscultural_labelconsistency/"
pdf_extract: "PDF Extracts/2023/2023-Moss-Bias on Demand.md"
local_pdf: "[[PDFs/2023/2023-Moss-Bias on Demand.pdf]]"
---
# Bias on Demand: A Modelling Framework That Generates Synthetic Data With Bias

## Metadata

**Authors:** Moss, Nathan

**Year:** 2023

**Publication:** ACM Conference on Fairness, Accountability, and Transparency (FAccT)

**Type:** conferencePaper

**DOI:** [10.1145/3593013.3594098](https://doi.org/10.1145/3593013.3594098)

## Links

- **URL:** https://dl.acm.org/doi/10.1145/3593013.3594098
- **DOI:** https://doi.org/10.1145/3593013.3594098

## Abstract

Recommendation systems increasingly depend on massive human-labeled datasets; however, the human annotators hired to generate these labels increasingly come from homogeneous backgrounds. This poses an issue when downstream predictive models -- based on these labels -- are applied globally to a heterogeneous set of users. We study this disconnect with respect to the labels themselves, asking whether they are ``consistently conceptualized'' across annotators of different demographics. In a case study of video game labels, we conduct a survey on 5,174 gamers, identify a subset of inconsistently conceptualized game labels, perform causal analyses, and suggest both cultural and linguistic reasons for cross-country differences in label annotation. We further demonstrate that predictive models of game annotations perform better on global train sets as opposed to homogeneous (single-country) train sets. Finally, we provide a generalizable framework for practitioners to audit their own data annotation processes for consistent label conceptualization, and encourage practitioners to consider global inclusivity in recommendation systems starting from the early stages of annotator recruitment and data-labeling.

## Authors

[[Nathan Moss]]

## Detailed Summary

This paper addresses a critical problem in recommendation systems and machine learning pipelines: the disconnect between homogeneous annotator demographics and heterogeneous global user populations. The authors focus on auditing human-annotated labels for "consistent conceptualization" across different demographic groups, asking whether labels mean the same thing to annotators from different countries and cultural backgrounds. Using video game labels as a case study, they conducted a survey of 5,174 gamers across 16 countries and 9 languages to examine how game genre labels are understood differently across demographics.

The research reveals that certain labels are "inconsistently conceptualized" across countries due to both cultural and linguistic factors. For example, a label like "high replayability" for a specific game might receive majority agreement in the US but majority disagreement in Korea, leading to fundamentally different labeling outcomes depending on which country's annotators are recruited. The study employs multilevel regression and post-stratification (MRP) to correct for demographic imbalances in survey responses and uses causal analysis techniques including Inglehart-Welzel cultural dimensions and translation quality assessment.

Importantly, the paper demonstrates that predictive models trained on globally diverse annotator pools outperform those trained on homogeneous single-country pools, particularly for inconsistently conceptualized labels. This finding has significant implications for industry practices, as crowdsourcing platforms like Amazon Mechanical Turk draw over 91% of annotators from just the US and India, yet the resulting labels are applied globally. The authors provide a generalizable framework for practitioners to audit their own annotation processes and encourage global inclusivity starting from annotator recruitment.

## Paper Outline

1. Introduction - Problem of homogeneous annotators for global applications
2. Related Work - Four stages of ML pipeline bias
   - Label generation bias
   - Annotation process bias
   - Model bias
   - Decision-making bias
3. Case Study: Video Game Labels
   - Data collection (5,174 respondents, 16 countries, 9 languages)
   - Evaluating labels for consistent conceptualization (MRP analysis)
   - Explanations for inconsistent conceptualization
     - Cultural distances (Inglehart-Welzel)
     - Translation differences
4. Quantifying Bias from Homogeneous Annotators
5. Mitigation Strategies and Framework for Practitioners
6. Discussion and Implications
7. Conclusion

## Methods Summary

The study employs multiple methodological approaches: (1) Large-scale survey design with 5,174 Xbox gamers across 16 countries (Argentina, Chile, Colombia, Mexico, Brazil, Germany, Greece, Japan, Poland, Saudi Arabia, South Korea, India, Nigeria, Singapore, South Africa, US), using both local language translations and English versions for bilingual ambassadors; (2) Multilevel Regression and Post-Stratification (MRP) using Bayesian logistic regression to generate demographically-weighted predictions of label selection; (3) Cultural distance analysis using Inglehart-Welzel Cultural Map indices; (4) Translation quality assessment through back-translation verification and bilingual annotator comparisons; (5) Predictive modeling experiments comparing single-country vs. global training sets; (6) Threshold analysis to identify "inconsistently conceptualized" labels (cross-country standard deviation > 0.05 with estimates both above and below 50%).

## Results Summary

Key findings include: (1) 55 out of 280 game-label pairs were identified as "inconsistently conceptualized" across countries; (2) Country-level differences showed higher variance than age or gender differences (e.g., 20 percentage-point spread across countries vs. 10 percentage-point spread by gender for "high replayability"); (3) Cultural distance metrics from Inglehart-Welzel framework correlated with labeling disagreements; (4) Translation quality issues contributed to inconsistent conceptualization - labels with less precise translations showed more cross-country variance; (5) Predictive models trained on global (heterogeneous) annotator pools outperformed single-country (homogeneous) pools, especially for inconsistently conceptualized labels; (6) The "zen" label exemplified consistent conceptualization - all demographic groups agreed the action game should not receive this label.

## Conclusions

The paper concludes that practitioners should consider global inclusivity from the earliest stages of annotator recruitment and data labeling. Key recommendations include: (1) Audit labels for consistent conceptualization before training predictive models; (2) Use heterogeneous annotator pools representing target user demographics; (3) Be aware that translation alone does not ensure consistent understanding; (4) Apply cultural framework analysis to understand sources of disagreement; (5) Consider that inconsistently conceptualized labels may require different handling (additional interpretation effort, country-specific models, or label redesign). The framework provided is generalizable beyond video games to any domain using human-annotated labels for global audiences.

## Artifact Contributions

- Survey instrument for cross-cultural label annotation (5,174 responses)
- Multilevel Regression and Post-Stratification (MRP) methodology for demographically-weighted analysis
- Framework for auditing data annotation processes for consistent label conceptualization
- Dataset of 280 game-label pairs with cross-cultural annotation patterns
- Identification of 55 inconsistently conceptualized game-label pairs
- Code repository for reproducing methods (GitHub)

## Data Description

The dataset consists of a survey of 5,174 Xbox gamers across 16 countries and 9 languages who annotated 11 popular video games using 28 labels. The study uses multilevel regression and post-stratification (MRP) to evaluate cross-cultural consistency of human-annotated labels for recommendation systems, focusing on 280 game-label pairs.


## Notes


## Citation Info

41 citations (Semantic Scholar/DOI) [2025-08-27]
