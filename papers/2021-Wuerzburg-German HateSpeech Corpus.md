---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0476
type: conferencePaper
short_title: "German HateSpeech Corpus"
year: 2025
first_author: "[[Cophi-Wue (University of Wuerzburg)]]"
last_author: "[[Cophi-Wue (University of Wuerzburg)]]"
authors: "Cophi-Wue (University of Wuerzburg)"
url: "https://github.com/cophi-wue/German_HateSpeech_Corpus"
external_pdf: "https://ojs.aaai.org/index.php/ICWSM/article/download/31438/33598"
publication: GitHub
pdf_extract: "PDF Extracts/2021/2021-Wuerzburg-German HateSpeech Corpus.md"
local_pdf: "[[PDFs/2021/2021-Wuerzburg-German HateSpeech Corpus.pdf]]"
DATE_ADDED: 20260213
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "German"
languages_list: German
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation approach annotated dataset"
data_metrics: "Not specified"
LLM_assessed: BERT
DATA_URL: "https://github.com/cophi-wue/German_HateSpeech_Corpus"
tags: 
abstract: "We provide a German corpus consisting of 7,061 posts authored by users of social media platforms. A group of volunteers annotated each post according to hatespeech and misogynistic/misogynous hatespeech in a binary fashion. The interrater reliability over all annotators according to Fleiss’ Kappa is 0.6409 for hatespeech and 0.8258 for misogynistic hatespeech. Furthermore, baseline measurements with machine learning based text classification with BERT are presented."
research_topic: "Machine Learning"
---
# German HateSpeech Corpus

## Authors

[[Cophi-Wue (University of Wuerzburg)]]

## Metadata

**Authors:** Cophi-Wue (University of Wuerzburg)

**Year:** 2021

**Type:** conferencePaper

**Venue:** GitHub

**Languages:** German

**Benchmark:** German_HateSpeech_Corpus

## Links

- **URL:** https://github.com/cophi-wue/German_HateSpeech_Corpus
- **Code/Data:** https://github.com/cophi-wue/German_HateSpeech_Corpus

## Abstract

Annotated corpus combining GermEval 2018 tweets (2,871 instances), POLLY corpus of politically charged German tweets around 2017 election (~4,500 annotated), and Facebook comments from Pegida pages (3,500). Annotated as hate speech, offensive language, or non-hate.

## Summary

This paper presents the GMHP7k corpus containing 7,061 German social media posts (from Facebook and Twitter) annotated for both general hate speech and misogynistic hate speech specifically. The dataset was annotated by six volunteers with inter-rater reliability of 0.6409 (Fleiss' Kappa) for general hate speech and 0.8258 for misogynistic hate speech. Baseline experiments using fine-tuned BERT models achieve macro F1 scores of 0.79 for hate speech detection and 0.75 for misogynistic hate speech detection, providing the first publicly available German corpus specifically targeting misogynistic content.

## Data Description

GMHP7k corpus of 7,061 German social media posts annotated for general hate speech and misogynistic hate speech specifically. Tests BERT models achieving F1 scores up to 0.79 for hate speech and 0.75 for misogynistic hate speech detection.


## Detailed Summary

This paper presents GMHP7k (German Misogynistic Hatespeech Posts), a corpus of 7,061 German social media comments annotated for both general hate speech and misogynistic hate speech specifically. The dataset fills a gap in German-language NLP resources, as no publicly available German corpus had previously been annotated specifically for misogynistic hate speech, which often involves subtly disguised hostility toward women. Posts were collected from Facebook and Twitter, covering diverse topics to avoid dataset bias toward specific subject areas. The annotation was conducted by six volunteers who assessed each post in a binary fashion for both general hate speech and misogynistic hate speech categories.

Inter-rater reliability, measured by Fleiss' Kappa, is 0.6409 for general hate speech annotation and 0.8258 for misogynistic hate speech, indicating substantial to almost perfect agreement. The higher agreement on misogynistic hate speech suggests that this specific form of hostility may be more clearly identifiable than general hate speech. Baseline classification experiments using fine-tuned BERT models achieve macro F1 scores of 0.79 for general hate speech detection and 0.75 for misogynistic hate speech detection. The paper contextualizes the dataset within the landscape of German hate speech resources, noting that while several German datasets exist (GermEval 2018/2019, HASOC 2019, GermEval 2021), none specifically target misogynistic content.

## Paper Outline

1. Introduction - Motivation for German misogynistic hate speech corpus
2. Related Work - Existing German and misogyny-focused datasets
3. Dataset - Data collection, annotation methodology, corpus statistics
4. Experiments - BERT-based baseline classification
5. Discussion - Results analysis and comparison to related work
6. How to Use the Corpus - Public availability
7. Conclusion

## Methods Summary

Data collection targets German social media posts from Facebook and Twitter, covering diverse topics including politics, sports, entertainment, and social issues to ensure topical diversity. Six volunteers annotate each post in two binary dimensions: (1) whether the post contains general hate speech and (2) whether it contains misogynistic hate speech. Annotation guidelines define misogynistic hate speech as content that expresses hostility, contempt, or prejudice against women. Inter-rater reliability is measured using Fleiss' Kappa. Baseline experiments fine-tune German BERT models for binary classification on both annotation dimensions, using standard train/test splits with macro-averaged F1 as the primary metric.

## Results Summary

The corpus achieves Fleiss' Kappa of 0.6409 for general hate speech (substantial agreement) and 0.8258 for misogynistic hate speech (almost perfect agreement). Fine-tuned BERT models achieve macro F1 scores of 0.79 for hate speech detection and 0.75 for misogynistic hate speech detection. The higher inter-annotator agreement on misogynistic hate speech compared to general hate speech suggests that targeted misogyny may be less ambiguous to identify than broader offensive language categories. The dataset's size of 7,061 posts is close to the average of approximately 8,000 texts found across hate speech datasets surveyed by Vidgen and Derczynski (2020).

## Conclusions

The GMHP7k corpus provides a unique resource for training and evaluating classifiers that can distinguish between general hate speech and the specific case of misogynistic hate speech in German. Future work includes expanding the dataset, incorporating more nuanced annotation categories beyond binary classification, and developing more sophisticated models that can capture the subtlety of disguised misogynistic content. The publicly available dataset is intended to support both academic research and practical applications in online content moderation.

## Artifact Contributions

- **GMHP7k Corpus**: 7,061 German social media posts annotated for general and misogynistic hate speech (https://github.com/cophi-wue/German_HateSpeech_Corpus)

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** Comprehensive merged German hate speech corpus from multiple sources and platforms.

## Tags

