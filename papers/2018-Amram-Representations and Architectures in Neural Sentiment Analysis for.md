---




Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0026
type: conferencePaper
short_title: "Representations and Architectures in Neural Sentiment Analysis for Morphologically Rich Languages: A Case Study from Modern Hebrew"
year: 2025
first_author: "[[Adam Amram]]"
last_author: "[[Reut Tsarfaty]]"
authors: "Adam Amram, Anat Ben David, Reut Tsarfaty"
url: "https://aclanthology.org/C18-1190/"
external_pdf: "https://aclanthology.org/C18-1190.pdf"
publication: "ACL Anthology (COLING 2018)"
pdf_extract: "PDF Extracts/2018/2018-Amram-Representations and Architectures in Neural Sentiment Analysis for.md"
local_pdf: "[[PDFs/2018/2018-Amram-Representations and Architectures in Neural Sentiment Analysis for.pdf]]"
DATE_ADDED: 20260213
ethics_overall: "No"
virtue_ethics: "Yes"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "Hebrew/Israeli"
languages_list: Hebrew
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark"
data_metrics: "Not specified"
LLM_assessed: "NA"
DATA_URL: "https://github.com/omilab/Neural-Sentiment-Analyzer-for-Modern-Hebrew"
tags: 
abstract: "This paper empirically studies the effects of representation choices on neural sentiment analysis for Modern Hebrew, a morphologically rich language (MRL) for which no sentiment analyzer currently exists. We study two dimensions of representational choices: (i) the granularity of the input signal (token-based vs. morpheme-based), and (ii) the level of encoding of vocabulary items (string-based vs. character-based)."
research_topic: "NLP & Representation Learning"
---
# Representations and Architectures in Neural Sentiment Analysis for Morphologically Rich Languages: A Case Study from Modern Hebrew

## Authors

[[Adam Amram, Anat Ben David, Reut Tsarfaty]]

## Metadata

**Authors:** Adam Amram, Anat Ben David, Reut Tsarfaty

**Year:** 2018

**Type:** conferencePaper

**Venue:** ACL Anthology (COLING 2018)

**Languages:** Hebrew

**Benchmark:** Hebrew Sentiment Dataset (12K)

## Links

- **URL:** https://aclanthology.org/C18-1190/
- **Code/Data:** https://github.com/omilab/Neural-Sentiment-Analyzer-for-Modern-Hebrew

## Abstract

First sentiment analysis benchmark for Modern Hebrew based on 12,804 social media comments from Israel president's Facebook page. Token-based and morpheme-based settings. 89% accuracy baseline.

## Data Description

The paper introduces a new sentiment analysis benchmark for Modern Hebrew consisting of 12,804 user comments scraped from the official Facebook page of Israel's president, annotated for positive, negative, and neutral sentiment by two trained annotators. The dataset is split into 10,244 training and 2,560 test comments, provided in both token-based and morpheme-based representational forms. The authors evaluate various neural network architectures (MLP, CNN, LSTM, BiLSTM) on this benchmark rather than testing any LLM.


## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent A10
**Relevance:** Foundational Hebrew sentiment analysis benchmark from political social media; addresses MRL-specific evaluation challenges

## Tags

