---





































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: T3ZTMJEH
type: journalArticle
short_title: "Moral Foundations Twitter Corpus"
year: 2020
first_author: "[[Joe Hoover]]"
last_author: "[[Morteza Dehghani]]"
authors: "Joe Hoover; Gwenyth Portillo-Wightman; Leigh Yeh; Shreya Havaldar; Aida Mostafazadeh Davani; Ying Lin; Brendan Kennedy; Mohammad Atari; Zahra Kamel; Madelyn Mendlen; Gabriela Moreno; Christina Park; Tingyee E. Chang; Jenna Chin; Christian Leong; Jun Yen Leung; Arineh Mirinjian; Morteza Dehghani"
doi: 10.1177/1948550619876629
url: "https://doi.org/10.1177/1948550619876629"
external_pdf: "https://journals.sagepub.com/doi/pdf/10.1177/1948550619876629"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "Christianity"
rv_islam: 0
rv_christianity: 50
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 0
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: "Christianity"
mp_mft: 100
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "Moral Foundations Theory"
newtags: "Moral Foundations Theory, Moral Reasoning & Psychology"
key_contribution: "Created the MFTC, a large corpus of 35k tweets annotated for 10 Moral Foundations, across 7 distinct domains (e.g., #BlueLivesMatter, #Sandy, etc.)."
significance: "The gold-standard dataset for studying 'moral sentiment' in natural language social media analysis, enabling researchers to track how moral values drive online polarization and diffusion."
tags: 
abstract: "Research has shown that accounting for moral sentiment in natural language can yield insight into a variety of on- and off-line phenomena, such as message diffusion, protest dynamics, and social distancing. However, measuring moral sentiment in natural language is challenging and the difficulty of this task is exacerbated by the limited availability of annotated data. To address this issue, we introduce the Moral Foundations Twitter Corpus, a collection of 35,108 tweets that have been curated..."
CONF-CC: "Social Psychological and Personality Science"
DATE_ADDED: 20260208
LLM_assessed: "NA"
DATA_URL: "https://osf.io/ezn37/"
pdf_extract: "PDF Extracts/2020/2020-Hoover-Moral Foundations Twitter Corpus.md"
local_pdf: "[[PDFs/2020/2020-Hoover-Moral Foundations Twitter Corpus.pdf]]"
CONFERENCE: "Journal"
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 5
is_benchmark: "No"
is_eval: No
is_dataset: "Yes"
data_description: "Evaluation methodology annotated dataset"
data_metrics: "10 categories"
ethics_perspective: "Moral Reasoning & Psychology"
---
# Moral Foundations Twitter Corpus: A Collection of 35k Tweets Annotated for Moral Sentiment

## Metadata

**Authors:** Hoover, Joe; Portillo-Wightman, Gwenyth; Yeh, Leigh; Havaldar, Shreya; Davani, Aida Mostafazadeh; Lin, Ying; Kennedy, Brendan; Atari, Mohammad; Kamel, Zahra; Mendlen, Madelyn; Moreno, Gabriela; Park, Christina; Chang, Tingyee E.; Chin, Jenna; Leong, Christian; Leung, Jun Yen; Mirinjian, Arineh; Dehghani, Morteza

**Year:** 2020

**Publication:** Social Psychological and Personality Science

**Type:** journalArticle

**DOI:** [10.1177/1948550619876629](https://doi.org/10.1177/1948550619876629)

**Pages:** 1057-1071

**Volume/Issue:** Vol. 11, Issue 8

## Links

- **DOI:** https://doi.org/10.1177/1948550619876629

## Abstract

Research has shown that accounting for moral sentiment in natural language can yield insight into a variety of on- and off-line phenomena such as message diffusion, protest dynamics, and social distancing. However, measuring moral sentiment in natural language is challenging, and the difficulty of this task is exacerbated by the limited availability of annotated data. To address this issue, we introduce the Moral Foundations Twitter Corpus, a collection of 35,108 tweets that have been curated from seven distinct domains of discourse and hand annotated by at least three trained annotators for 10 categories of moral sentiment. To facilitate investigations of annotator response dynamics, we also provide psychological and demographic metadata for each annotator. Finally, we report moral sentiment classification baselines for this corpus using a range of popular methodologies.

## Authors

[[Joe Hoover]], [[Gwenyth Portillo-Wightman]], [[Leigh Yeh]], [[Shreya Havaldar]], [[Aida Mostafazadeh Davani]], [[Ying Lin]], [[Brendan Kennedy]], [[Mohammad Atari]], [[Zahra Kamel]], [[Madelyn Mendlen]], [[Gabriela Moreno]], [[Christina Park]], [[Tingyee E. Chang]], [[Jenna Chin]], [[Christian Leong]], [[Jun Yen Leung]], [[Arineh Mirinjian]], [[Morteza Dehghani]]

## Detailed Summary

This paper introduces the Moral Foundations Twitter Corpus (MFTC), a collection of 35,108 tweets that have been hand-annotated for 10 categories of moral sentiment based on Moral Foundations Theory. The corpus addresses a critical gap in computational moral psychology research—the lack of high-quality annotated data for training and evaluating models that detect moral sentiment in natural language. The tweets were curated from seven socially relevant discourse domains: All Lives Matter, Black Lives Matter, the Baltimore protests, the 2016 Presidential election, hate speech/offensive language, Hurricane Sandy, and #MeToo.

Each tweet was annotated by at least three trained annotators for the presence of five moral foundations (Care/Harm, Fairness/Cheating, Loyalty/Betrayal, Authority/Subversion, and Purity/Degradation), with separate labels for virtue (positive) and vice (negative) expressions of each foundation. The paper also provides psychological and demographic metadata for annotators to enable research on how annotator characteristics influence labeling decisions in subjective domains like moral sentiment.

The corpus has already facilitated research on topics including the relationship between charitable donation and moral framing, prediction of violent protest from online moral rhetoric, and advances in NLP methods for measuring moral sentiment.

## Paper Outline

1. Introduction - Motivation and challenges in measuring moral sentiment
2. Corpus Overview - Selection criteria for seven discourse domains
3. Annotation Procedures - Training, annotation process, and inter-annotator agreement
4. Annotator Metadata - Psychological and demographic measures
5. Classification Baselines - Performance of various ML approaches
6. Discussion - Implications and future directions
7. Appendix - Additional methodological details

## Methods Summary

Tweets were collected using domain-specific search terms and hashtags. Each tweet was annotated by 3+ trained annotators using 10 binary labels (virtue/vice for each of 5 moral foundations) plus a "non-moral" category. Annotators underwent extensive training on Moral Foundations Theory. Inter-annotator agreement was assessed using Krippendorff's alpha. Classification baselines were established using approaches including Moral Foundations Dictionary (MFD), Distributed Dictionary Representations (DDR), and various supervised learning methods including BERT-based models.

## Results Summary

The corpus contains approximately 5,000 tweets per domain, with varying base rates of moral sentiment across domains. Key findings: (1) Moral sentiment base rates are low but meaningful; (2) Inter-annotator agreement varies by foundation, with Care and Fairness showing highest agreement; (3) Domain transfer is challenging—models trained on one domain generalize poorly to others; (4) BERT-based approaches achieve best overall performance; (5) DDR methods outperform dictionary approaches for cross-domain generalization.

## Conclusions

The authors conclude that the MFTC fills a critical need in computational moral psychology by providing high-quality annotated data. They emphasize the importance of domain heterogeneity for model robustness and highlight that annotator characteristics can influence moral sentiment judgments. Future work should focus on improving cross-domain generalization and accounting for annotator subjectivity in subjective annotation tasks.

## Artifact Contributions

- **Dataset**: Moral Foundations Twitter Corpus (MFTC) - 35,108 tweets annotated for 10 moral sentiment categories
- **Annotator Metadata**: Psychological and demographic data for 13 annotators
- **Baselines**: Classification results for multiple ML methodologies

## Data Description

The paper introduces the Moral Foundations Twitter Corpus (MFTC), a collection of 35,108 tweets curated from seven domains of discourse and hand-annotated by at least three trained annotators for 10 categories of moral sentiment based on Moral Foundations Theory. Baseline classification results are provided using a range of ML models including LSTM, logistic regression, and other methods. Psychological and demographic metadata for each annotator is also provided to facilitate research on annotator response dynamics.


## Notes

