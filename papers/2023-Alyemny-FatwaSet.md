---





Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 9GE4KQRK
type: journalArticle
short_title: FatwaSet
year: 2025
first_author: "[[Ohoud Alyemny]]"
last_author: "[[Abdulrahman Mirza]]"
authors: "Ohoud Alyemny; Hend Al-Khalifa; Abdulrahman Mirza"
url: "https://www.mdpi.com/2306-5729/8/11/156"
national_ethnic_cultural: "Arabic"
cultures_nationalities_list: "Arabic"
languages_list: "Arabic"
religious_values: "Islam"
religious_values_list: "Islam"
moral_psychology: "N/A"
newtags: Islam
tags: 
abstract: "Islamic content is a broad and diverse domain that encompasses various sources, topics, and perspectives. However, there is a lack of comprehensive and reliable datasets that can facilitate conducting studies on Islamic content. In this paper, we present fatwaset, the ﬁrst public Arabic dataset of Islamic fatwas. It contains Islamic fatwas that we collected from various trusted and authenticated sources in the Islamic fatwa domain, such as agencies, religious scholars, and websites."
DATE_ADDED: 20260208
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "NLP & Representation Learning"
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Dataset for question answering"
data_metrics: "Not specified"
LLM_assessed: "NA"
DATA_URL: "https://github.com/ohoud/Fatwaset.git"
pdf_extract: "PDF Extracts/2023/2023-Alyemny-FatwaSet.md"
local_pdf: [[PDFs/2023/2023-Alyemny-FatwaSet.pdf]]
---
# FatwaSet: A Data-Driven Exploration of a New Islamic Fatwas Dataset for Arabic NLP Tasks

## Metadata

**Authors:** Alyemny, Ohoud; Al-Khalifa, Hend; Mirza, Abdulrahman

**Year:** 2023

**Publication:** MDPI Data

**Type:** journalArticle

**DOI:** [10.3390/data8100155](https://doi.org/10.3390/data8100155)

## Links

- **URL:** https://www.mdpi.com/2306-5729/8/10/155

## Abstract

FatwaSet is the first public Arabic dataset of Islamic fatwas. The data were collected from 13 trusted websites in Arab countries, including Saudi Arabia, Egypt, Jordan, Qatar, and Syria. An exploratory data analysis reveals a total of 130,182 records. FatwaSet is a rich resource containing fatwas and their surrounding metadata, suitable for NLP tasks such as language modeling, question answering, author attribution, topic identification, and text classification.

## Authors

[[Ohoud Alyemny]], [[Hend Al-Khalifa]], [[Abdulrahman Mirza]]

## Detailed Summary

FatwaSet is the first publicly available Arabic dataset dedicated to Islamic fatwas, addressing a significant gap in NLP resources for Islamic content. A fatwa is a formal ruling issued by a qualified Islamic scholar (mufti) in response to questions about Islamic law. The dataset contains 130,182 fatwa records collected from 13 trusted websites across Arab countries including Saudi Arabia, Egypt, Jordan, Qatar, and Syria, ensuring coverage of diverse linguistic terms and cultural perspectives.

Unlike previous Islamic content datasets that primarily focus on the Quran, FatwaSet targets fatwas, which play a central role in Muslims' daily lives and social dealings. The dataset includes not only the fatwa questions and answers but also extensive metadata: titles, subtitles, fatwa numbers, publication dates, mufti names, categories (Fiqh and subject-based), and answer sources. This comprehensive metadata enables diverse NLP applications including language modeling, question answering, author attribution, topic identification, text classification, and text summarization.

The paper includes an extensive Exploratory Data Analysis (EDA) examining the dataset from multiple angles: fatwa topics, question-answer characteristics, and religious scholars' response patterns. Word cloud analysis reveals that the most frequently discussed topics relate to prayer, women, and religious rulings, with some scholars showing distinctive focus areas (e.g., Al Shaikh Abdullah Al Manee's emphasis on Islamic banking and finance).

## Paper Outline

1. Introduction
   - Importance of fatwas in Islamic community
   - Gap in Islamic content NLP datasets
   - FatwaSet objectives and use cases
2. Background and Related Works
   - Existing Islamic content datasets (AyaTEC, QRCD, EIAD)
   - Gap analysis for fatwa datasets
   - Exploratory Data Analysis techniques
3. Materials and Methods
   - Website selection across Arab countries
   - Data collection methodology
   - Metadata collection and challenges
   - Preprocessing pipeline
4. Results and Discussion
   - Fatwa topics analysis (word clouds)
   - Question and answer analysis
   - Religious scholars' response patterns
   - Length analysis of answers

## Methods Summary

Data was collected from 13 trusted websites representing official government agencies (Dar Al Ifta in Saudi Arabia, Egypt, Jordan), individual religious scholars' websites (Ibn Baz, Ibn Othaimin, Al Fwzan), and popular Islamic portals (IslamWeb, FatwaPedia, IslamQA, IslamOnline). Collection focused on geographic diversity to capture varied linguistic terms and cultural topics.

Web scraping addressed challenges including: (1) different website formats and categorization schemes, (2) varying metadata availability across sources, (3) audio-only answers on some sites, and (4) inconsistent page hierarchies. Preprocessing involved removing duplicates and empty fields, resulting in 130,182 cleaned records.

Exploratory Data Analysis employed Python libraries (Pandas, Numpy, Matplotlib, Wordcloud, NLTK) with Arabic-specific tools (pyarabic, arabic_reshaper). Text preprocessing included tokenization, punctuation removal, diacritic removal, and stop word filtering using established Arabic stop word lists, plus domain-specific term removal (e.g., "the question," "the answer," "the fatwa").

## Results Summary

- Total Records: 130,182 fatwas after cleaning (55,000+ removed during preprocessing)
- Source Distribution: FatwaPedia (47,098), Ibn Baz (27,111), Dar Al Ifta Saudi Arabia (20,000), IslamWeb (11,662)
- Geographic Coverage: Saudi Arabia, Egypt, Jordan, Qatar, Syria
- Most Frequent Topics: Prayer (Alsala), Women (Almaraah), Religious rulings (Hukm), Allah
- Distinctive Scholars: Al Shaikh Al Manee focuses on banking/finance; Al Shaikh Bin Humaid emphasizes academic/educational topics
- Metadata Fields: Title, subtitle, fatwa number, publication date, mufti name, category, answer source (varies by website)
- Answer Lengths: Vary significantly across scholars and topics

## Conclusions

FatwaSet represents a significant contribution to Arabic NLP resources, being the first public dataset dedicated to Islamic fatwas. The dataset's comprehensive metadata and diverse sources make it suitable for numerous NLP tasks: training Arabic language models, building Islamic question-answering systems, author attribution research, topic modeling, and text classification. The exploratory data analysis reveals patterns in Islamic scholarship, including frequently asked topics and distinctive scholarly focuses. The dataset can also support interdisciplinary research in philosophy, history, language arts, and social sciences due to its connection with Islamic spiritual culture. Future work could extend the dataset to other languages and incorporate additional metadata categories.

## Artifact Contributions

- FatwaSet: 130,182 Arabic fatwa records (first public fatwa dataset)
- 13 source websites covering 5 Arab countries
- Rich metadata: titles, subtitles, fatwa numbers, dates, mufti names, categories
- Exploratory Data Analysis with word clouds and frequency statistics
- Preprocessing pipeline for Arabic Islamic text
- Dataset publicly available for research use

## Data Description

This appears to be the same paper as the Alyemny 'Data-Driven Exploration' entry, presenting FatwaSet, the first public Arabic dataset of Islamic fatwas. The dataset contains fatwas collected from authenticated Islamic sources with surrounding metadata, designed for Arabic NLP tasks. Exploratory Data Analysis is conducted but no models are benchmarked on the dataset.


## Notes

