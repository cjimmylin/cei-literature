---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: KEWE563L
type: journalArticle
short_title: "Fine-tuning Large Language Model (BERT) for"
year: 2025
first_author: "[[Nurul Aiman Binti Mohd Nazri]]"
last_author: "[[Bin Amir Hussin, Amir 'Aatieff]]"
authors: "[[Binti Mohd Nazri, Nurul Aiman]]; [[Binti Omar, A'wathif]]; [[Bin Amir Hussin, Amir 'Aatieff]]"
doi: 10.31436/ijpcc.v11i1.533
url: "https://journals.iium.edu.my/kict/index.php/IJPCC/article/view/533"
external_pdf: "file:///Users/jimmylin/Zotero/storage/LSHSUEEF/Binti Mohd Nazri et al. - 2025 - Fine-tuning Large Language Model (BERT) for Islamic Moral Inquiry and Response.pdf"
national_ethnic_cultural: "N/A"
religious_values: "Islam"
religious_values_list: "Islam"
moral_psychology: "N/A"
newtags: "Islam, Virtue Ethics"
key_contribution: "Fine-tunes a BERT model on the 'Islam: Questions and Answers' corpus to enhance its ability to perform moral-related QA tasks from an Islamic perspective"
significance: "Demonstrates the feasibility of specializing LLMs for non-Western, virtue-based (Islamic character) moral inquiry using targeted domain-specific fine-tuning"
tags: 
abstract: "The development of Large Language Models (LLM) that are capable of understanding and responding to issues from an Islamic perspective is extremely insightful as it will benefit many people. For an LLM to do so, it is not enough for the model to only understand the language, but it also needs to understand the context and specific doctrines within the Islamic texts due to the complexity of Islamic jurisprudence and moral philosophy."
ethics_overall: "Yes"
virtue_ethics: "Yes"
deontological_ethics: "No"
utilitarian_ethics: "No"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation approach text corpus for question answering"
data_metrics: "0 dataset"
LLM_assessed: BERT
DATA_URL: "https://github.com/krishnaik06/Trnasformer-"
pdf_extract: "PDF Extracts/2025/2025-Binti Mohd Nazri-Fine-tuning Large Language Model (BERT) for.md"
local_pdf: "[[PDFs/2025/2025-Binti Mohd Nazri-Fine-tuning Large Language Model (BERT) for.pdf]]"
---
# Fine-tuning Large Language Model (BERT) for Islamic Moral Inquiry and Response

## Authors

[[Nurul Aiman Binti Mohd Nazri|Binti Mohd Nazri, Nurul Aiman]], [[A'wathif Binti Omar|Binti Omar, A'wathif]], [[Amir 'Aatieff Bin Amir Hussin|Bin Amir Hussin, Amir 'Aatieff]]

## Links



- **URL:** https://journals.iium.edu.my/kict/index.php/IJPCC/article/view/533
- **DOI:** https://doi.org/10.31436/ijpcc.v11i1.533

## Abstract

The development of Large Language Models (LLM) that are capable of understanding and responding to issues from an Islamic perspective is extremely insightful as it will benefit many people. For an LLM to do so, it is not enough for the model to only understand the language, but it also needs to understand the context and specific doctrines within the Islamic texts due to the complexity of Islamic jurisprudence and moral philosophy. Therefore, in this research, we intend to fine-tune an LLM model which is known as Bidirectional Encoder Representations from Transformers (BERT) for Islamic moral inquiry and response. By incorporating Islamic principles, norms, and teaching into the model, we aim to enhance the pre-trained BERT model's ability to perform moral-related Question Answering (QA) tasks. The original model that we chose is deepset BERT model which was built based on BERT-large and meticulously pretrained using the SQuaD 2.0 dataset, specifically for QA tasks. We fine-tune the model using the data extracted from "Islam: Questions and Answers: Character and Morals", the Volume 13 of a Series of Islamic Books by Muhammad Saed Abdul-Rahman, where the data has been cleaned and pre-processed. The finetuning process used supervised learning techniques, to ensure its proficiency in understanding Islamic principles, providing accurate, contextually appropriate, and theologically sound responses. We assessed the model using F1 score and Levenshtein similarity evaluation metrics where F1 score merges precision and recall by computing their harmonic mean, while Levenshtein similarity compares the predicted and actual answers at the character level by normalizing the Levenshtein distance. Our research yielded significant success, evidenced by the remarkable enhancement in the average F1 scores and Levenshtein similarities, soaring from 0.30 and 0.24, to 0.74 and 0.67 respectively.

## Detailed Summary

This research demonstrates the feasibility of adapting large language models for domain-specific moral reasoning within Islamic jurisprudence and ethics. The authors fine-tune a BERT model to respond to moral inquiries from an Islamic perspective, addressing the challenge that general-purpose LLMs often lack the theological precision and cultural awareness required for religiously grounded responses.

The study uses the deepset BERT-large model, pre-trained on SQuAD 2.0 for question-answering tasks, as the foundation. The fine-tuning dataset is extracted from "Islam: Questions and Answers: Character and Morals" (Volume 13) by Muhammad Saed Abdul-Rahman, a book containing moral questions and answers from both Muslims and non-Muslims, with responses grounded in Quranic and Sunnah sources by reputable Islamic scholars.

The results demonstrate substantial improvement through domain-specific fine-tuning. Before fine-tuning, the model achieved average F1 scores of 0.30 and Levenshtein similarity of 0.24. After fine-tuning, these metrics improved dramatically to 0.74 and 0.67 respectively - representing more than a twofold improvement. This validates the approach of using targeted domain-specific data to specialize LLMs for culturally and religiously sensitive moral inquiry.

## Paper Outline

1. Introduction
   - Need for LLMs capable of Islamic moral reasoning
   - Limitations of general-purpose models
   - Research objectives
2. Literature Review
   - Overview of Large Language Models
   - Foundation models and pre-training
   - BERT architecture and self-attention mechanism
   - Fine-tuning for domain-specific tasks
   - Existing Islamic NLP systems (MufassirQAS, QASiNa)
3. Methodology
   - Task dataset preparation from Islamic book
   - Data preprocessing and cleaning
   - Data augmentation with CQA triples
   - Hyperparameter tuning
   - Fine-tuning procedure
4. Results and Analysis
   - Performance metrics (F1 score, Levenshtein similarity)
   - Before vs. after fine-tuning comparison
5. Conclusion

## Methods Summary

The methodology involves fine-tuning the deepset/bert-large-uncased-whole-word-masking-squad2 model on Islamic moral content. The dataset was extracted from a trusted Islamic book, with preprocessing including: text extraction, removal of formatting artifacts, normalization (lowercase, punctuation handling), tokenization, stop word removal, and quality checks. ChatGPT assisted in converting multiline text to single-line format to address model limitations.

Data augmentation generated multiple context-question-answer (CQA) triples with: (1) variance in contexts covering different Islamic moral topics; (2) multiple questions per context; (3) varied answers of different lengths and positions; and (4) "is_impossible" flags for unanswerable questions.

Fine-tuning used Hugging Face Transformers with parameters: max_seq_length=128, num_train_epochs=80, evaluate_during_training_steps=1000, learning rate approximately 5e-5, training batch size 16. Evaluation metrics included F1 score (harmonic mean of precision and recall) and Levenshtein similarity (character-level comparison using normalized edit distance).

## Results Summary

- Pre-fine-tuning Performance: F1 score = 0.30, Levenshtein similarity = 0.24
- Post-fine-tuning Performance: F1 score = 0.74, Levenshtein similarity = 0.67
- Improvement: More than 2x improvement in both metrics
- Model: deepset/bert-large-uncased-whole-word-masking-squad2
- Training: 80 epochs with evaluation every 1000 steps
- Data Source: "Islam: Questions and Answers: Character and Morals" by Muhammad Saed Abdul-Rahman

## Conclusions

The research successfully demonstrates that domain-specific fine-tuning can significantly improve LLM performance for Islamic moral question-answering tasks. The dramatic improvement from 0.30 to 0.74 F1 score shows that specialized training data enables models to provide more accurate, contextually appropriate, and theologically sound responses. This has practical implications for developing AI systems that respect and uphold cultural and religious values, bridging the gap between AI capabilities and Islamic ethics. The approach provides a template for adapting LLMs to other religious or cultural domains where domain expertise and sensitivity are required.

## Artifact Contributions

- Fine-tuned BERT model for Islamic moral QA tasks
- Preprocessing pipeline for Islamic text data
- Data augmentation methodology for CQA triple generation
- Evaluation framework using F1 and Levenshtein similarity metrics
- Training configuration and hyperparameters for reproducibility

## Data Description

This paper fine-tunes the deepset BERT-large-uncased-whole-word-masking-squad2 model for Islamic moral inquiry and response using data extracted from 'Islam: Questions and Answers: Character and Morals' by Muhammad Saed Abdul-Rahman. The fine-tuned model's performance was evaluated using F1 score and Levenshtein similarity metrics, improving from 0.30/0.24 to 0.74/0.67 respectively. The dataset consists of context-question-answer triples from Islamic moral teachings.


## Notes


## Citation Info

0 citations (Semantic Scholar/DOI) [2025-08-27] 0 citations (Semantic Scholar/DOI) [2025-08-23] 0 citations (Crossref/DOI) [2025-08-23]
