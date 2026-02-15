---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 3FVZCJRK
type: document
short_title: EMoTES-3K
year: 2025
first_author: "[[Jasper Kyle Catapang]]"
last_author: "[[Visperas, Moses]]"
authors: "[[Catapang, Jasper Kyle]]; [[Visperas, Moses]]"
url: "https://aclanthology.org/2023.nlp4dh-1.1/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/5GQQWIXN/2023 - EMoTES-3K Emotion-based Morality in Tagalog and English Scenarios.pdf"
national_ethnic_cultural: "Filipino"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Filipino, Moral Reasoning & Psychology"
key_contribution: "Created EMoTES-3K, the first dataset for emotion-based morality in Tagalog (Filipino) and English, testing 'commonsense morality' in a low-resource language."
significance: "Addresses the 'Anglocentrism' of moral AI benchmarks, providing a crucial resource for Filipino NLP and showing that models struggle with 'mixed' moral scenarios in Tagalog."
tags: 
abstract: "Grasping morality is vital in AI systems, particularly as they become more prevalent in humanfocused applications. Yet, research is scarce on this topic. This study presents the Emotionbased Morality in Tagalog and English Scenarios (EMoTES-3K), a collection that shows commonsense morality in both Filipino and English. This dataset is instrumental for analyzing moral decisions in various situations and their justifications."
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Moral Reasoning & Psychology"
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Dataset"
data_metrics: "Not specified"
LLM_assessed: "RoBERTa, Flan-T5"
DATA_URL: NA
pdf_extract: "PDF Extracts/2023/2023-Catapang-EMoTES-3K.md"
local_pdf: [[PDFs/2023/2023-Catapang-EMoTES-3K.pdf]]
---
# EMoTES-3K: Emotion-based Morality in Tagalog and English Scenarios

## Authors

[[Jasper Kyle Catapang|Catapang, Jasper Kyle]], [[Moses Visperas|Visperas, Moses]]

## Links

- **ACL Anthology:** https://aclanthology.org/2023.nlp4dh-1.1/

## Abstract

Grasping morality is vital in AI systems, particularly as they become more prevalent in human-focused applications. Yet, research is scarce on this topic. This study presents the Emotion-based Morality in Tagalog and English Scenarios (EMoTES-3K), a collection that shows commonsense morality in both Filipino and English. This dataset is instrumental for analyzing moral decisions in various situations and their justifications. Our tests show that EMoTES-3K is effective for moral text categorization, with the fine-tuned RoBERTa model scoring 94.95% accuracy in English and 88.53% in Filipino. The dataset also excels in text generation tasks, as shown by fine-tuning the FLAN-T5 model to produce clear moral explanations. However, the model faces challenges when dealing with actions that have mixed moral implications. This work not only bridges the gap in moral reasoning datasets for languages like Filipino but also sets the stage for future research in commonsense moral reasoning in artificial intelligence.

## Data Description

EMoTES-3K is a parallel corpus of approximately 2,905 commonsense morality scenarios (1,712 moral and 1,193 immoral) in both Filipino and English. Each entry includes a scenario, moral/immoral annotation, explanation, and inferred personality traits. The dataset is used for moral text classification (fine-tuning RoBERTa) and text generation of moral explanations (fine-tuning FLAN-T5 large).


## Notes

