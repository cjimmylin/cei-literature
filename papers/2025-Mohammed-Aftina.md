---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 8U3CGTV5
type: journalArticle
short_title: Aftina
year: 2025
first_author: "[[Ahmed Mohammed]]"
last_author: "[[Ahmed Mohammed]]"
authors: "Ahmed Mohammed"
doi: 10.1007/s00521-025-11229-y
url: "https://neuralcomputingjournals.com/aftina-fatwaqa"
external_pdf: "file:///Users/jimmylin/Zotero/storage/VQU5HCPT/Mohammed and others - 2025 - Aftina Arabic Fatwa QA Benchmark for Islamic Jurisprudence.pdf"
national_ethnic_cultural: Arabic
religious_values: "Islam"
religious_values_list: "Islam"
moral_psychology: N/A
newtags: "Arabic, Islam"
tags: 
abstract: "Question–answering (QA) systems face considerable challenges when involved in Islamic fatwas due to the complexity and sensitivity of the data. Such problems involve providing accurate and reliable responses, managing hallucinations and inaccurate responses, and maintaining the stability of the generated responses. Prior studies have concentrated mainly on collecting and preprocessing Islamic datasets or developing retrieval-based QA systems, overlooking the precision and reliability required fo"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
research_topic: "Question Answering"
is_benchmark: Yes
is_eval: No
is_dataset: Yes
data_description: "Benchmark for hallucination detection dataset for question answering"
data_metrics: "Not specified"
LLM_assessed: "Gemini, Gemma"
DATA_URL: "NA"
pdf_extract: "PDF Extracts/2025/2025-Mohammed-Aftina.md"
local_pdf: "[[PDFs/2025/2025-Mohammed-Aftina.pdf]]"
DATE_ADDED: 20260207
---
# Aftina: Arabic Fatwa QA Benchmark for Islamic Jurisprudence

## Metadata

**Authors:** Mohammed, Ahmed

**Year:** 2025

**Publication:** Neural Computing & Applications

**Type:** journalArticle

**DOI:** [10.1007/s00521-025-11229-y](https://doi.org/10.1007/s00521-025-11229-y)

## Links

- **URL:** https://neuralcomputingjournals.com/aftina-fatwaqa
- **DOI:** https://doi.org/10.1007/s00521-025-11229-y

## Abstract

Question–answering (QA) systems face considerable challenges when involved in Islamic fatwas due to the complexity and sensitivity of the data. Such problems involve providing accurate and reliable responses, managing hallucinations and inaccurate responses, and maintaining the stability of the generated responses. Prior studies have concentrated mainly on collecting and preprocessing Islamic datasets or developing retrieval-based QA systems, overlooking the precision and reliability required fo

## Authors

[[Ahmed Mohammed]]

## Detailed Summary

This paper presents Aftina, a question-answering system for Islamic fatwas that addresses critical challenges in AI-based religious content generation: hallucination, response instability, and maintaining accuracy in sensitive religious contexts. The authors identify that existing QA systems struggle with Islamic fatwas due to the complexity of Arabic language (morphological richness, dialectal variations, Classical Arabic requirements), limited specialized datasets, and the high stakes of providing incorrect religious guidance. Prior work focused primarily on dataset collection or basic retrieval systems without addressing the precision and reliability essential for fatwa issuance.

The technical approach combines Large Language Models (LLMs) with Retrieval-Augmented Generation (RAG) enhanced by a Flash re-ranker mechanism. The system was evaluated across three experimental setups: (1) base LLM only, (2) LLM with RAG, and (3) LLM with RAG and re-ranker. The re-ranker component reorders retrieved knowledge chunks based on contextual relevance to the user's query, significantly improving response quality. Three LLMs were tested: Silma (an Arabic-specialized model based on Google Gemma), AceGPT (designed for Arabic text), and Gemini 1.5. The dataset of 18,407 question-answer pairs was obtained from Dar Alifta in Egypt, covering three categories: Fasting, Banks, and Zakka.

The paper emphasizes ethical considerations unique to AI-driven fatwa systems, including confidentiality of religious data, hallucination mitigation, transparency about the system's limitations (it supplements but does not replace human scholars), and fairness across different Islamic schools of thought. A validation module incorporates automated re-ranking, human expert review for flagged responses, and LLM-to-LLM cross-validation. Results demonstrate that the third configuration (LLM with RAG and re-ranker) significantly outperforms alternatives, with Silma achieving the best performance (70.40% F1-BERTScore, 0.40% hallucination rate, 99.60% completeness).

## Paper Outline

1. Introduction
   - Linguistic challenges (Arabic complexity, dialects)
   - Technical challenges (dataset limitations, AI integration)
   - Ethical considerations
2. Related Work - Review of Islamic QA systems and RAG approaches
3. Materials and Methods
   - Dataset description (Dar Alifta, 18,407 QA pairs)
   - Methodology pipeline
   - Data preprocessing and chunking
   - Vectorization with Multilingual-E5 and FAISS
   - Answer generation with three LLMs
   - Flash re-ranker mechanism
   - Validation and verification module
4. Results and Discussion
   - Evaluation metrics (BLEU, METEOR, BERTScore, hallucination, completeness, irrelevance)
   - Experimental results across three setups
   - Latency vs. accuracy trade-off
   - Human evaluation by domain expert
   - LLM-to-LLM evaluation using GPT-4o
5. Conclusion and Ethical Considerations

## Methods Summary

The system architecture involves: (1) Data preprocessing - converting CSV/HTML fatwa data into question-answer chunks; (2) Vectorization using Multilingual-E5 (mE5) embeddings supporting 100+ languages including Arabic, stored in FAISS vector database; (3) Retrieval using Euclidean distance similarity search to find top-k relevant chunks; (4) Re-ranking using FlashRanker with a similarity threshold of 0.97 to filter and reorder retrieved chunks; (5) Answer generation using three LLMs (Silma, AceGPT, Gemini 1.5) with structured prompts. Evaluation metrics included statistical measures (BLEU, METEOR) and semantic measures (BERTScore, hallucination rate, completeness, irrelevance). Human evaluation was conducted by a Professor of Arabic Studies who blindly rated 210 responses on a 1-5 scale. LLM-to-LLM evaluation used GPT-4o to assess response quality.

## Results Summary

Base model performance: AceGPT achieved highest BERTScore (64.92%) and completeness (98.46%), but Silma had lowest hallucination (0.82%). LLM with RAG improved all models - Silma reached 68.93% BERTScore with 0.52% hallucination. LLM with RAG and re-ranker achieved best results: Silma reached 70.40% F1-BERTScore, 99.60% completeness, and only 0.40% hallucination. Human evaluation by domain expert rated Silma highest (3.86/5), followed by AceGPT (3.56/5) and Gemini 1.5 (2.95/5). Latency analysis showed Silma with RAG and re-ranker took 26.95s average response time versus 4.02s for base model, but the accuracy gain justified this for high-stakes fatwa applications. The re-ranker proved critical for contextual relevance and hallucination reduction.

## Conclusions

The paper demonstrates that combining RAG with re-ranking significantly improves AI-driven fatwa generation accuracy and stability. Silma emerged as the most reliable LLM for this sensitive domain due to its ability to follow context-specific instructions and minimize hallucinations. Gemini 1.5 performed poorly because it tended to rely on pre-trained knowledge rather than provided context. The authors emphasize that while the system can assist users, it is not a replacement for consultation with trained Islamic scholars. Future work should expand dataset coverage to more fatwa topics and further reduce response latency while maintaining accuracy.

## Artifact Contributions

- Fatwa QA system using RAG with re-ranker
- Dataset of 18,407 fatwa QA pairs from Dar Alifta (Fasting, Banks, Zakka categories)
- Evaluation framework including hallucination, completeness, and irrelevance metrics

## Data Description

The study implements a fatwa question-answering system using retrieval-augmented generation (RAG) enhanced with a Flash re-ranker. The dataset, obtained from Dar Alifta in Egypt, comprises 18,407 question-answer pairs across three categories (Fasting, Banks, and Zakka). Three LLMs are evaluated: Silma (built on Gemma), AceGPT-7B, and Gemini 1.5, using BERTScore, hallucination, completeness, and irrelevance metrics.


## Notes


## Citation Info

7 citations (Semantic Scholar/DOI) [2025-08-27]
