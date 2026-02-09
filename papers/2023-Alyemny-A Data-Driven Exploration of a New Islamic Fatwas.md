---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: B9AUPLYG
type: journalArticle
short_title: "A Data-Driven Exploration of a New Islamic Fatwas"
year: 2025
first_author: "[[Ohoud Alyemny]]"
authors: "Ohoud Alyemny; Hend Al-Khalifa; Abdulrahman Mirza"
doi: 10.3390/data8100155
url: "https://www.mdpi.com/2306-5729/8/10/155"
external_pdf: "file:///Users/jimmylin/Zotero/storage/A4GPKYSQ/Alyemny et al. - 2023 - A Data-Driven Exploration of a New Islamic Fatwas Dataset for Arabic NLP Tasks.pdf"
national_ethnic_cultural: Arabic
religious_values: Islam
moral_psychology: N/A
newtags: "Arabic, Islam"
tags: 
abstract: "Islamic content is a broad and diverse domain that encompasses various sources, topics, and perspectives. However, there is a lack of comprehensive and reliable datasets that can facilitate conducting studies on Islamic content. FatwaSet is the first available public Arabic dataset for Islamic fatwas. The dataset contains Islamic fatwas collected from various trusted and authenticated sources in the Islamic fatwa domain, such as agencies, religious scholars, and websites. FatwaSet is a rich resource as it does not only contain fatwas but also includes a considerable set of their surrounding metadata. It can be used for many NLP tasks, such as language modeling, question answering, author attribution, topic identification, text classification, and text summarization."
pdf: "https://www.mdpi.com/2306-5729/8/10/155/pdf?version=1697687515"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
research_topic: "NLP & Representation Learning"
is_benchmark: No
is_eval: No
is_dataset: Yes
data_description: "Dataset for question answering"
data_metrics: "Not specified"
pdf_extract: "PDF Extracts/2023/2023-Alyemny-A Data-Driven Exploration of a New Islamic Fatwas.md"
local_pdf: "[[PDFs/2023/2023-Alyemny-A Data-Driven Exploration of a New Islamic Fatwas.pdf]]"
---
# A Data-Driven Exploration of a New Islamic Fatwas Dataset for Arabic NLP Tasks

## Metadata

**Authors:** Alyemny, Ohoud; Al-Khalifa, Hend; Mirza, Abdulrahman

**Year:** 2023

**Publication:** Data

**Type:** journalArticle

**DOI:** [10.3390/data8100155](https://doi.org/10.3390/data8100155)

**Pages:** 155

**Volume/Issue:** Vol. 8, Issue 10

## Links

- **URL:** https://www.mdpi.com/2306-5729/8/10/155
- **DOI:** https://doi.org/10.3390/data8100155

## Abstract

Islamic content is a broad and diverse domain that encompasses various sources, topics, and perspectives. However, there is a lack of comprehensive and reliable datasets that can facilitate conducting studies on Islamic content. In this paper, we present fatwaset, the ﬁrst public Arabic dataset of Islamic fatwas. It contains Islamic fatwas that we collected from various trusted and authenticated sources in the Islamic fatwa domain, such as agencies, religious scholars, and websites. Fatwaset is a rich resource as it does not only contain fatwas but also includes a considerable set of their surrounding metadata. It can be used for many natural language processing (NLP) tasks, such as language modeling, question answering, author attribution, topic identiﬁcation, text classiﬁcation, and text summarization. It can also support other domains that are related to Islamic culture, such as philosophy and language art. We describe the methodology and criteria we used to select the content, as well as the challenges and limitations we faced. Additionally, we perform an Exploratory Data Analysis (EDA), which investigates the dataset from different perspectives. The results of the EDA reveal important information that greatly beneﬁts researchers in this area.

## Authors

[[Ohoud Alyemny]], [[Hend Al-Khalifa]], [[Abdulrahman Mirza]]

## Detailed Summary

This paper introduces Fatwaset, the first publicly available Arabic dataset of Islamic fatwas (religious rulings issued by qualified Islamic scholars). The dataset was collected from 13 trusted and authenticated websites representing various Arabic-speaking countries including Saudi Arabia, Egypt, Jordan, Qatar, and Syria. The authors compiled 130,182 fatwas along with rich metadata including titles, subtitles, fatwa numbers, publication dates, and mufti names, making it a valuable resource for Natural Language Processing (NLP) tasks related to Islamic content.

The creation of Fatwaset addresses a significant gap in the field, as existing Islamic content datasets have primarily focused on the Quran, leaving other important sources like Sunnah and fatwas underrepresented. The dataset supports multiple NLP applications including language modeling, question answering, author attribution, topic identification, text classification, and text summarization. The authors describe several challenges encountered during data collection, including varying website formats, inconsistent metadata availability across sources, and the replacement of text with audio clips on some sites.

The paper also presents an Exploratory Data Analysis (EDA) of the dataset, examining fatwas' topics through word cloud visualizations for each source. Key findings reveal that common topics across sources include religious rulings (Hukm), prayer (Alsala), and women's issues (Almaraah). Notably, Al Shaikh Abdullah Al Manee's fatwas show a unique focus on financial topics like banking, loans, and credit cards, reflecting his specialization in Islamic banking.

## Paper Outline

1. Introduction - Motivation for creating an Islamic fatwas dataset for NLP
2. Background and Related Works
   - Islamic Fatwa-Related Studies - Review of existing Islamic content datasets
   - Exploratory Data Analysis (EDA) - Overview of EDA techniques
3. Materials and Methods
   - Fatwaset - Dataset construction methodology and sources
   - Proposed Pipeline of Exploratory Data Analysis - Data preprocessing and analysis approach
4. Results and Discussion
   - Fatwas' Topics - Word cloud analysis of topics by source
   - Fatwas (Questions and Answers) - Analysis of fatwa content
5. Conclusions - Summary and future directions

## Methods Summary

The authors collected fatwas from 13 Arabic websites representing official government agencies (e.g., Dar Al Ifta in Saudi Arabia, Egypt, Jordan), websites of renowned religious scholars (e.g., Al Shaikh Ibn Baz, Al Shaikh Ibn Othaimin), and popular trusted Islamic websites (e.g., IslamWeb, IslamQA). Data collection involved web scraping with custom code adapted to each website's structure. The preprocessing pipeline included tokenization, punctuation removal, diacritic removal (specific to Arabic text), and stop word removal using a standard Arabic stop word list plus domain-specific terms. The analysis used Python libraries including Pandas, Numpy, Matplotlib, Wordcloud, NLTK, pyarabic, and arabic_reshaper.

## Results Summary

The final dataset contains 130,182 fatwas after cleaning (removing duplicates and empty fields). The largest contributions came from FatwaPedia (47,098), Al Shaikh Ibn Baz (27,111), and Dar Al Ifta Saudi Arabia (20,000). Word cloud analysis of fatwa topics revealed that most common terms across sources relate to religious rulings, prayer, and women's issues. Al Shaikh Al Manee showed uniquely financial-focused topics reflecting his expertise in Islamic banking. Answer length analysis showed significant variation across sources, with some providing detailed responses while others offered more concise answers.

## Conclusions

The paper successfully introduces Fatwaset as the first publicly available Arabic dataset for Islamic fatwas, filling a gap in Islamic content resources for NLP research. The dataset's inclusion of metadata beyond simple question-answer pairs enables diverse research applications. The EDA revealed important patterns in fatwa topics and response characteristics that can guide future research directions. The authors note that the dataset's design facilitates not just NLP tasks but also supports related fields like philosophy, history, and social sciences due to its connection to Islamic spiritual culture.

## Artifact Contributions

- Fatwaset: A publicly available Arabic dataset of 130,182 Islamic fatwas with metadata

## Notes


## Citation Info

15 citations (Semantic Scholar/DOI) [2025-08-27] 3 citations (Semantic Scholar/DOI) [2025-08-23] 2 citations (Crossref/DOI) [2025-08-23]
