---































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0515
type: conferencePaper
short_title: "MuLTa-Telegram: A Fine-Grained Italian and Polish Dataset for Hate Speech Detection"
year: 2025
first_author: "[[Leonardelli, Elisa]]"
last_author: "[[Tonelli, Sara]]"
authors: "Leonardelli, Elisa; Casula, Camilla; Vecellio Salto, Sebastiano; Bak, Joanna Ewa; Muratore, Elisa; Kolos, Anna; Louf, Thomas; Tonelli, Sara"
url: "https://aclanthology.org/2025.clicit-1.56.pdf"
external_pdf: "https://ceur-ws.org/Vol-4112/55_main_long.pdf"
publication: "ACL Anthology (CLiC-it 2025)"
CONF-CC: "N/A"
pdf_extract: PDF Extracts/2025/2025-Leonardelli-MuLTa-Telegram A Fine-Grained Italian and Polish Dataset for Hate.md
local_pdf: "[[PDFs/2025/2025-Leonardelli-MuLTa-Telegram A Fine-Grained Italian and Polish Dataset for Hate.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "Italian"
cultures_nationalities_list: "Italian"
languages_list: "Italian, Polish"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: "BERT, Llama-3"
DATA_URL: "https://github.com/dhfbk/MuLTa-Telegram"
tags: 
abstract: "This paper introduces the MuLTa-Telegram dataset, a Multi- Lingual and multi-Target dataset specifically developed to detect hate speech on Telegram, an understudied yet influential platform in which extremist and fringe content can be found. The dataset contains about 4,000 Telegram messages in Italian and Polish, annotated for the presence of hate speech and its targets, including also target identity group mentions even when no hate is expressed."
CONFERENCE: "ACL 2025"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Toxicity & Hate Speech"
is_benchmark: "No"
is_eval: Yes
is_dataset: "Yes"
data_description: "Annotated dataset for hate speech detection"
data_metrics: "Not specified"
---
# MuLTa-Telegram: A Fine-Grained Italian and Polish Dataset for Hate Speech Detection

## Authors

[[Leonardelli, Elisa]], [[Casula, Camilla]], [[Vecellio Salto, Sebastiano]], [[Bak, Joanna Ewa]], [[Muratore, Elisa]], [[Kolos, Anna]], [[Louf, Thomas]], [[Tonelli, Sara]]

## Metadata

**Authors:** Leonardelli, Elisa, Casula, Camilla, Vecellio Salto, Sebastiano, Bak, Joanna Ewa, Muratore, Elisa, Kolos, Anna, Louf, Thomas, Tonelli, Sara

**Year:** 2025

**Type:** conferencePaper

**Venue:** ACL Anthology (CLiC-it 2025)

**Languages:** Italian, Polish

**Benchmark:** MuLTa-Telegram

## Links

- **URL:** https://aclanthology.org/2025.clicit-1.56.pdf

## Abstract

Multi-lingual, multi-target dataset of ~4,000 Telegram messages in Italian and Polish annotated for hate speech and targets including People with Disabilities, LGBTQ+, Religion (Jews, Muslims, Christians), Ethnicity/Origin (People of Color, Romani, Migrants), and Women.

## Summary

This paper introduces MuLTa-Telegram, a multilingual and multi-target hate speech dataset comprising approximately 4,000 Telegram messages in Italian and Polish with fine-grained target annotations. The dataset employs detailed categorization across diverse protected groups including People with Disabilities, LGBTQ+ individuals, religious groups (Jews, Muslims, Christians), ethnic/origin groups (People of Color, Romani, Migrants), and Women. The fine-grained annotation approach enables systematic evaluation of bias and hate speech detection systems against diverse social groups across two European languages.

## Data Description

MuLTa-Telegram: a multilingual, multi-target dataset of ~4,000 Telegram messages in Italian and Polish annotated for hate speech and target identity groups (People with Disabilities, LGBTQ+, Religion, Ethnicity, Women), designed for hate speech and target detection.


## Detailed Summary

This paper introduces MuLTa-Telegram (Multi-Lingual and multi-Target Telegram dataset), a hate speech dataset specifically developed for Telegram -- an understudied yet influential platform where extremist and fringe content proliferates due to reduced content moderation. The dataset contains approximately 4,000 messages (2,000 Italian, 2,000 Polish) annotated for hate speech presence and targets, including target identity group mentions even when no hate is expressed. The dataset is explicitly designed to capture a diverse range of 9 minority target categories, employing a keyword matrix to pre-select messages from a large pool of Telegram data collected from channels known to spread disinformation or hate, identified by international domain experts in the Hatedemics European project. The initial collection retrieved 2.5 million Italian and 1.1 million Polish messages from January 2022 to January 2023 using snowball sampling from expert-curated seed channels. Extensive experiments evaluate hate speech classification in multilingual, multi-task, and LLM-based approaches, finding that incorporating target information leads to the best performance and enables multilingual generalization, while classification of specific targets shows much room for improvement.

## Paper Outline

1. Introduction - Need for platform-specific, multi-target hate speech datasets
2. Background - Existing hate speech datasets for Italian and Polish; Telegram as understudied platform
3. Data Selection and Annotation - Collection strategy, anonymization, pre-selection, annotation guidelines
4. Dataset Analysis - Distribution of hate speech, targets, and identity group mentions
5. Experiments - Multilingual, multi-task, and LLM-based classification setups
6. Results - Performance across setups and languages
7. Conclusion

## Methods Summary

Data collection uses snowball sampling from expert-curated seed Telegram channels, expanding through recommendation networks. From the top 150 channels, 2.5M Italian and 1.1M Polish messages are collected. A keyword matrix ensures representation of 9 minority target categories. Messages are anonymized (emails, phone numbers, mentions replaced) and channel metadata deleted for privacy. Expert annotation covers hate speech presence, specific targets, and target identity group mentions. Classification experiments compare fine-tuned transformer models, multilingual approaches, multi-task setups (joint hate detection and target classification), and LLM-based annotation across both languages.

## Results Summary

Training on existing out-of-domain data leads to poor results on Telegram data, underscoring the necessity of in-domain datasets. Incorporating target information leads to the best hate speech detection performances and enables multilingual generalization between Italian and Polish. However, classification of specific targets shows much room for improvement across all experimental setups. The multi-task approach (joint hate detection and target prediction) outperforms single-task models. LLM-based approaches show promise but do not consistently outperform fine-tuned specialized models.

## Conclusions

The study demonstrates the critical need for platform-specific hate speech datasets, as models trained on Twitter data transfer poorly to Telegram. The multi-target annotation approach provides richer training signals that improve both hate detection and cross-lingual generalization. The dataset fills gaps in both Italian and Polish hate speech resources, particularly for the understudied Telegram platform.

## Artifact Contributions

- **Dataset:** MuLTa-Telegram - ~4,000 Telegram messages (2,000 Italian, 2,000 Polish) with hate speech and multi-target annotations across 9 minority categories (github.com/dhfbk/MuLTa-Telegram)
- **Annotation Schema:** 9-category target taxonomy with separate hate speech and identity group mention annotations

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B8
**Relevance:** Fine-grained Italian hate speech dataset with detailed target annotations, enabling evaluation of bias against diverse social groups.

## Tags

