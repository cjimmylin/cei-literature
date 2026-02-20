---






Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0542
type: preprint
short_title: "Detecting Abusive Albanian"
year: 2021
first_author: "[[Erida Nurce]]"
last_author: "[[Leon Derczynski]]"
authors: "Erida Nurce, Jorgel Keci, Leon Derczynski"
url: "https://arxiv.org/abs/2107.13592"
external_pdf: "https://arxiv.org/pdf/2107.13592.pdf"
publication: arXiv
CONF-CC: "Preprint"
pdf_extract: "PDF Extracts/2021/2021-Nurce-Detecting Abusive Albanian.md"
local_pdf: "[[PDFs/2021/2021-Nurce-Detecting Abusive Albanian.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "Albanian"
languages_list: Albanian
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: BERT
DATA_URL: "https://doi.org/10.6084/m9.figshare.19333298.v1"
tags: 
abstract: "The ever growing usage of social media in the recent years has had a direct impact on the increased presence of hate speech and offensive speech in online platforms. Research on effective detection of such content has mainly focused on English and a few other widespread languages, while the leftover majority fail to have the same work put into them and thus cannot benefit from the steady advancements made in the field."
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Toxicity & Hate Speech"
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Annotated dataset for hate speech detection"
data_metrics: "11,874 instances"
CONFERENCE: "Preprint"
---
# Detecting Abusive Albanian

## Authors

[[Erida Nurce]], [[Jorgel Keci]], [[Leon Derczynski]]

## Metadata

**Authors:** Erida Nurce, Jorgel Keci, Leon Derczynski

**Year:** 2021

**Type:** preprint

**Venue:** arXiv

**Languages:** Albanian

**Benchmark:** SHAJ

## Links

- **arXiv:** https://arxiv.org/abs/2107.13592
- **Code/Data:** https://doi.org/10.6084/m9.figshare.19333298.v1

## Abstract

Presents SHAJ, an annotated Albanian dataset for hate speech and offensive speech constructed from user-generated content on Instagram and YouTube. Contains 11,874 instances with 13.2% abusive content, annotated hierarchically (offensive/not; untargeted/targeted; person/group/other).

## Summary

This paper introduces SHAJ (Spoken Hate in the Albanian Jargon), the first Albanian dataset for hate speech and offensive language detection containing 11,874 user-generated comments from Instagram and YouTube with 13.2% abusive content. The dataset follows the hierarchical OffensEval annotation schema with three levels: offensive vs. non-offensive, targeted vs. untargeted, and target type (person, group, or other). The authors benchmark the dataset using BERT, BiLSTM, and logistic regression models, achieving F1 scores of 0.77 for offensive language identification, 0.64 for offensive type categorization, and 0.52 for target identification, addressing the gap in hate speech detection resources for Albanian.

## Data Description

SHAJ dataset of 11,874 Albanian social media comments from Instagram and YouTube with hierarchical annotation for offensive/hate speech. Tests BERT, BiLSTM, and logistic regression models achieving F1 scores of 0.77 for offensive language identification.


## Detailed Summary

This paper presents SHAJ (Spoken Hate in the Albanian Jargon), the first annotated Albanian dataset for hate speech and offensive language detection, containing 11,874 user-generated comments from Instagram and YouTube with approximately 13.2% abusive content. The dataset follows the hierarchical OffensEval/OLID taxonomy with three annotation levels: Sub-task A classifies posts as offensive (OFF) or not (NOT); Sub-task B categorizes offensive posts as targeted (TIN) or untargeted (UNT); and Sub-task C identifies the target type as individual (IND), group (GRP), or other (OTH). The paper provides context on hate speech regulation in Albania, noting that while the Albanian constitution does not explicitly mention "hate speech," the Criminal Code regulates it, with main targets being the LGBT community, Roma minorities, and politicians.

The authors benchmark SHAJ using three classification models: multilingual BERT (mBERT), BiLSTM with fastText Albanian word embeddings, and Logistic Regression with TF-IDF features. The best system achieves F1 scores of 0.77 for Sub-task A (offensive language identification), 0.64 for Sub-task B (offensive type categorization), and 0.52 for Sub-task C (target identification). The paper addresses a significant gap in hate speech detection resources for Albanian, a language with approximately 7.5 million speakers that lacks NLP resources and tools. The dataset highlights challenges specific to Albanian social media, including the prevalence of homophobic, sexist, and racist content facilitated by loose platform regulations and the absence of Albanian-language content moderation tools.

## Paper Outline

1. Introduction - Hate speech on Albanian social media and motivation
2. Background - Hate speech regulations in Albania, definitions
3. Related Work - Non-English hate speech datasets and detection methods
4. Dataset - SHAJ construction, annotation schema, statistics
5. Experiments - Models and evaluation setup
6. Results - Performance across three sub-tasks
7. Conclusion

## Methods Summary

Data collection targets Albanian-language comments from Instagram posts by Albanian media outlets and YouTube videos on trending Albanian topics. Comments are collected using the Instagram and YouTube APIs and filtered to remove non-Albanian content, duplicates, and very short comments. Three annotators label the data following the OLID hierarchical schema, with inter-annotator agreement measured via Cohen's Kappa. Three classification models are evaluated: (1) multilingual BERT (mBERT) fine-tuned on Albanian text; (2) BiLSTM with pre-trained fastText Albanian word embeddings; and (3) Logistic Regression with word and character n-gram TF-IDF features. Evaluation uses macro-averaged F1 scores.

## Results Summary

For Sub-task A (offensive language identification), mBERT achieves the best macro F1 of 0.77, outperforming BiLSTM (0.74) and Logistic Regression (0.71). For Sub-task B (targeted vs. untargeted), performance drops to 0.64 F1, reflecting the difficulty of distinguishing targeting intent. Sub-task C (target identification) achieves 0.52 F1, the most challenging task due to the limited number of group-targeted examples and the nuanced distinction between individual and group targets. Class imbalance is a significant challenge across all sub-tasks, with offensive content comprising only 13.2% of the dataset. The results establish baseline performance for Albanian offensive language detection and demonstrate the feasibility of cross-lingual transfer from multilingual models.

## Conclusions

The authors note that SHAJ is the first step toward Albanian hate speech detection and plan to expand the dataset with more sources and fine-grained annotations. Future work includes developing Albanian-specific language models, incorporating dialectal variations, and exploring semi-supervised approaches to address the class imbalance challenge. The paper calls for greater attention to hate speech detection in under-resourced languages.

## Artifact Contributions

- **SHAJ Dataset**: First Albanian offensive language and hate speech dataset with 11,874 annotated comments (https://doi.org/10.6084/m9.figshare.19333298.v1)

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B9
**Relevance:** First major Albanian hate speech/offensive language dataset. Directly relevant to toxicity, bias, and safety evaluation in Albanian social media content.

## Tags

