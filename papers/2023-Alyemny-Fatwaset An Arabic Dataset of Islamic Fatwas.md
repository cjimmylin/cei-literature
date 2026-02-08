---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: XM952VUQ
type: journalArticle
short_title: "Fatwaset: An Arabic Dataset of Islamic Fatwas"
year: 2025
first_author: "[[A. Alyemny]]"
authors: "A. Alyemny"
url: "https://www.mdpi.com/2306-5729/8/10/155"
external_pdf: "https://www.mdpi.com/2306-5729/8/10/155/pdf?version=1697687515"
national_ethnic_cultural: Arabic
religious_values: Islam
moral_psychology: N/A
newtags: "Arabic, Islam"
tags: 
abstract: "Islamic content is a broad and diverse domain that encompasses various sources, topics, and perspectives. However, there is a lack of comprehensive and reliable datasets that can facilitate conducting studies on Islamic content. FatwaSet is the first available public Arabic dataset for Islamic fatwas. The dataset contains Islamic fatwas collected from various trusted and authenticated sources in the Islamic fatwa domain, such as agencies, religious scholars, and websites. FatwaSet is a rich resource as it does not only contain fatwas but also includes a considerable set of their surrounding metadata. It can be used for many NLP tasks, such as language modeling, question answering, author attribution, topic identification, text classification, and text summarization."
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
research_topic: "Machine Learning"
is_benchmark: No
is_eval: No
is_dataset: Yes
data_description: "Dataset for question answering"
data_metrics: "Not specified"
pdf_extract: "PDF Extracts/2023/2023-Alyemny-Fatwaset An Arabic Dataset of Islamic Fatwas.md"
local_pdf: "[[PDFs/2023/2023-Alyemny-Fatwaset An Arabic Dataset of Islamic Fatwas.pdf]]"
---
# Fatwaset: An Arabic Dataset of Islamic Fatwas

## Metadata

**Authors:** Alyemny, A.

**Year:** 2023

**Publication:** MDPI Data

**Type:** journalArticle

## Links

- **URL:** https://www.mdpi.com/2306-5729/8/10/155

## Abstract

Islamic content is a broad and diverse domain that encompasses various sources, topics, and perspectives. However, there is a lack of comprehensive and reliable datasets that can facilitate conducting studies on Islamic content. FatwaSet is the first available public Arabic dataset for Islamic fatwas. The dataset contains Islamic fatwas collected from various trusted and authenticated sources in the Islamic fatwa domain, such as agencies, religious scholars, and websites. FatwaSet is a rich resource as it does not only contain fatwas but also includes a considerable set of their surrounding metadata. It can be used for many NLP tasks, such as language modeling, question answering, author attribution, topic identification, text classification, and text summarization.

## Authors

[[A. Alyemny]]

## Detailed Summary

Fatwaset represents a significant contribution to Arabic NLP and Islamic content research by providing the first publicly available Arabic dataset of Islamic fatwas. The dataset was collected from 13 trusted websites representing official government agencies (such as Dar Al Ifta in Saudi Arabia, Egypt, and Jordan), prominent religious scholars' websites, and established Islamic Q&A platforms across multiple Arab countries. The collection contains 130,182 fatwas along with their associated metadata, making it a valuable resource for researchers working on Arabic language processing and Islamic content analysis.

The paper addresses a critical gap in the availability of computational resources for studying Islamic content beyond the Quran. While previous datasets have focused primarily on Quranic text, Fatwaset opens new avenues for research on fatwas, which play a central role in Muslims' daily lives. The dataset supports various NLP tasks including language modeling, question answering, author attribution, topic identification, text classification, and text summarization. The inclusion of rich metadata (such as mufti names, titles, publication dates, and topic categories) enhances the dataset's utility for diverse research applications.

The authors conducted an extensive Exploratory Data Analysis (EDA) that reveals interesting patterns in fatwa topics across different sources. The analysis demonstrates that certain scholars specialize in particular domains (e.g., Al Shaikh Abdullah Al Manee focuses on Islamic banking and finance), while common topics across sources include rules of prayer, questions about Allah, and women's issues. The EDA also examined the linguistic characteristics of fatwa questions and answers, providing insights into the discourse patterns of Islamic jurisprudence.

## Paper Outline

1. Introduction - Establishes the importance of fatwas in Islamic life and the need for computational resources
2. Background and Related Works - Reviews existing Islamic content datasets and EDA techniques
3. Materials and Methods - Describes Fatwaset construction methodology and EDA pipeline
4. Results and Discussion - Presents findings from topic analysis, question-answer analysis, and answer length analysis
5. Conclusions - Summarizes contributions and future research directions

## Methods Summary

The dataset was constructed through web scraping of 13 authenticated Islamic fatwa websites. The authors employed careful preprocessing including tokenization, punctuation removal, diacritic removal, and Arabic-specific stop word removal. The EDA utilized Python libraries (Pandas, NumPy, Matplotlib, WordCloud, NLTK, pyarabic) to analyze and visualize the data. Quality control involved removing duplicates and incomplete records, resulting in over 55,000 rows being cleaned from the initial collection.

## Results Summary

The final dataset contains 130,182 fatwas from 13 sources, with metadata varying by source. Word cloud analysis revealed that common fatwa topics include religious rules (Hukm), prayer (Salah), and women's issues (Al-maraah). Specialized patterns emerged for individual scholars based on their expertise areas. The analysis of answer lengths showed variability across sources and topics, with some scholars providing more detailed responses than others.

## Conclusions

Fatwaset fills a significant gap in Arabic NLP resources by providing the first public dataset of Islamic fatwas. The dataset enables research on multiple NLP tasks and supports studies in Islamic content analysis. The EDA provides valuable insights into fatwa discourse patterns that can guide future research directions.

## Artifact Contributions

- Fatwaset dataset: 130,182 Arabic fatwas with metadata from 13 sources
- Publicly available for academic research

## Notes

