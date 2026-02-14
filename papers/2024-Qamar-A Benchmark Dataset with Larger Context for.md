---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: VEYVPPRY
type: journalArticle
short_title: "A Benchmark Dataset with Larger Context for"
year: 2025
first_author: "[[Faiza Qamar]]"
last_author: "[[Rabia Latif]]"
authors: "Faiza Qamar; Seemab Latif; Rabia Latif"
url: "https://arxiv.org/abs/2409.09844"
external_pdf: "https://arxiv.org/pdf/2409.09844.pdf"
national_ethnic_cultural: N/A
religious_values: Islam
religious_values_list: Islam
moral_psychology: N/A
newtags: Islam
tags: 
pdf_extract: "PDF Extracts/2024/2024-Qamar-A Benchmark Dataset with Larger Context for.md"
abstract: "Accessing and comprehending religious texts, particularly the Quran (the sacred scripture of Islam) and Ahadith (the corpus of the sayings or traditions of the Prophet Muhammad), in today’s digital era necessitates efficient and accurate Question-Answering (QA) systems. Yet, the scarcity of QA systems tailored specifically to the detailed nature of inquiries about the Quranic Tafsir (expla- nation, interpretation, context of Quran for clarity) and Ahadith poses signif- icant challenges. To addre"
paper_summary: "Abstract: Accessing and comprehending religious texts, particularly the Quran (the sacred scripture of Islam) and Ahadith (the corpus of the sayings or traditions of the Prophet Muhammad), in today’s digital er | Overview: A Benchmark Dataset with Larger Context for Non-Factoid Question-Answering over Islamic Text Faiza Qamar School of Electrical Engineering and Computer Science (SEECS) National University of Sciences a | Methodology: for generating long-form answers to statutory law questions. The approach utilized a ”retrieve-then-read” pipeline and was supported by the introducti | Key Findings: uncovered critical insights regarding the limitations of existing automatic evalu- ation techniques. The discrepancy between automatic evaluation metr | Conclusions: The fine-tuning of language models on the dataset resulted in improved performance, as evident by the evaluation using ROUGE in Table 4. It lists the"
local_pdf: "[[PDFs/2024/2024-Qamar-A Benchmark Dataset with Larger Context for.pdf]]"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
research_topic: "Machine Learning"
is_benchmark: Yes
is_eval: Yes
is_dataset: Yes
data_description: "Benchmark text corpus for question answering"
data_metrics: "73,000 question; over 73,000 question"
LLM_assessed: "T5, BART"
DATA_URL: NA
---
# A Benchmark Dataset with Larger Context for Non-Factoid QA over Islamic Text

## Metadata

**Authors:** Qamar, Faiza; Latif, Seemab; Latif, Rabia

**Year:** 2024

**Type:** journalArticle

## Links

- **Local PDF:** [[PDFs/2024/2024-Qamar-A Benchmark Dataset with Larger Context for.pdf|Open PDF]]

- **arXiv:** https://arxiv.org/abs/2409.09844

## Abstract

Accessing and comprehending religious texts, particularly the Quran (the sacred scripture of Islam) and Ahadith (the corpus of the sayings or traditions of the Prophet Muhammad), in today's digital era necessitates efficient and accurate Question-Answering (QA) systems. Yet, the scarcity of QA systems tailored specifically to the detailed nature of inquiries about the Quranic Tafsir (explanation, interpretation, context of Quran for clarity) and Ahadith poses significant challenges. To address this gap, we introduce a comprehensive dataset meticulously crafted for QA purposes within the domain of Quranic Tafsir and Ahadith. This dataset comprises a robust collection of over 73,000 question-answer pairs, standing as the largest reported dataset in this specialized domain. Importantly, both questions and answers within the dataset are meticulously enriched with contextual information, serving as invaluable resources for training and evaluating tailored QA systems. However, while this paper highlights the dataset's contributions and establishes a benchmark for evaluating QA performance in the Quran and Ahadith domains, our subsequent human evaluation uncovered critical insights regarding the limitations of existing automatic evaluation techniques. The discrepancy between automatic evaluation metrics, such as ROUGE scores, and human assessments became apparent. The human evaluation indicated significant disparities: the model's verdict consistency with expert scholars ranged between 11% to 20%, while its contextual understanding spanned a broader spectrum of 50% to 90%. These findings underscore the necessity for evaluation techniques that capture the nuances and complexities inherent in understanding religious texts, surpassing the limitations of traditional automatic metrics.

## Authors

[[Faiza Qamar]], [[Seemab Latif]], [[Rabia Latif]]

## Data Description

The paper introduces a comprehensive dataset of over 73,000 question-answer pairs for non-factoid question-answering in the domain of Quranic Tafsir and Ahadith. The dataset includes questions, scholar-provided answers, and contextual excerpts from Quranic Tafsir and the six major Hadith books (Sahah-e-Sittah), organized into eight topics via LDA topic modeling. Four transformer-based models (T5, BART, LED, LongT5) were fine-tuned and evaluated using ROUGE, BERTScore, and human evaluation.


## Notes


## Tags

#Computer-Science---Machine-Learning #Computer-Science---Computation-and-Language

## Citation Info

606 citations (Semantic Scholar/arXiv) [2025-08-27]
