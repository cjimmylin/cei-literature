---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: TMLLB5F3
type: journalArticle
short_title: "Large Language Models meet moral values"
year: 2025
first_author: "[[Luana Bulla]]"
last_author: "[[Aldo Gangemi]]"
authors: "Luana Bulla; Stefano De Giorgis; Misael Mongiovì; Aldo Gangemi"
doi: 10.1016/j.chbr.2025.100609
url: "https://linkinghub.elsevier.com/retrieve/pii/S2451958825000247"
external_pdf: "file:///Users/jimmylin/Zotero/storage/IHQZ47VE/Bulla et al. - 2025 - Large Language Models meet moral values A comprehensive assessment of moral abilities.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Machine Ethics"
key_contribution: "Evaluated the ability of LLMs (GPT-4, Llama, etc.) to perform *unsupervised* moral classification on the Moral Foundation Reddit Corpus, comparing them to human annotations."
significance: "Assesses whether general-purpose LLMs can replace specific supervised models for moral sensing, finding that GPT-4 is superior but significant variations exist across moral domains."
tags: 
abstract: "Automatic moral classification in textual data is crucial for various fields including Natural Language Processing (NLP), social sciences, and ethical AI development. Despite advancements in supervised models, their performance often suffers when faced with real-world scenarios due to overfitting to specific data distributions. To address these limitations, we propose leveraging state-of-the-art Large Language Models (LLMs) trained on extensive common-sense data for unsupervised moral classifica"
DATE_ADDED: 20260208
LLM_assessed: "GPT-4, GPT-3.5, Llama-2, Llama-3, Mistral, Mixtral"
DATA_URL: "https://osf.io/kw6rc/?view_only=73c3d8e2f7c9483ea012347d70d27b6f"
pdf_extract: "PDF Extracts/2025/2025-Bulla-Large Language Models meet moral values.md"
local_pdf: "[[PDFs/2025/2025-Bulla-Large Language Models meet moral values.pdf]]"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Machine Ethics"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation framework text corpus"
data_metrics: "Not specified"
---
# Large Language Models meet moral values: A comprehensive assessment of moral abilities

## Metadata

**Authors:** Bulla, Luana; De Giorgis, Stefano; Mongiovì, Misael; Gangemi, Aldo

**Year:** 2025

**Publication:** Computers in Human Behavior Reports

**Type:** journalArticle

**DOI:** [10.1016/j.chbr.2025.100609](https://doi.org/10.1016/j.chbr.2025.100609)

**Pages:** 100609

**Volume/Issue:** Vol. 17

## Links

- **URL:** https://linkinghub.elsevier.com/retrieve/pii/S2451958825000247
- **DOI:** https://doi.org/10.1016/j.chbr.2025.100609

## Abstract

Automatic moral classification in textual data is crucial for various fields including Natural Language Processing (NLP), social sciences, and ethical AI development. Despite advancements in supervised models, their performance often suffers when faced with real-world scenarios due to overfitting to specific data distributions. To address these limitations, we propose leveraging state-of-the-art Large Language Models (LLMs) trained on extensive common-sense data for unsupervised moral classification. We introduce an innovative evaluation framework that directly compares model outputs with human annotations, ensuring an assessment of model performance. Our methodology explores the effectiveness of different LLM sizes and prompt designs in moral value detection tasks, considering both multi-label and binary classification scenarios. We present experimental results using the Moral Foundation Reddit Corpus (MFRC) and discuss implications for future research in ethical AI development and human–computer interaction. Experimental results demonstrate that GPT-4 achieves superior performance, followed by GPT-3.5, Llama-70B, Mixtral-8x7B, Mistral-7B and Llama-7B. Additionally, the study reveals significant variations in model performance across different moral domains, particularly between everyday morality and political contexts. Our work provides meaningful insights into the use of zero-shot and few-shot models for moral value detection and discusses the potential and limitations of current technology in this task.

## Authors

[[Luana Bulla]], [[Stefano De Giorgis]], [[Misael Mongiovì]], [[Aldo Gangemi]]

## Detailed Summary

This paper comprehensively evaluates Large Language Models' capabilities in automatic moral classification, addressing the limitations of supervised models that tend to overfit to specific training data distributions. The research leverages state-of-the-art LLMs (GPT-4, GPT-3.5, Llama-70B, Mixtral-8x7B, Mistral-7B, and Llama-7B) as zero-shot and few-shot unsupervised classifiers for moral value detection based on Moral Foundation Theory (MFT).

The study makes a critical methodological contribution by proposing an evaluation framework that directly compares model outputs with human annotations under identical conditions. This addresses the inherent subjectivity limitation of traditional gold standards, where low inter-annotator agreement weakens reliability. By treating both human and model ratings on equal footing, the framework provides more meaningful insights into model capabilities.

The experiments use the Moral Foundation Reddit Corpus (MFRC), comprising 16,123 Reddit comments across three subcorpora representing different domains. The research evaluates both multi-label moral value detection (identifying specific MFT dimensions: Care/Harm, Fairness/Cheating, Loyalty/Betrayal, Authority/Subversion, Purity/Degradation) and binary classification (determining whether text contains moral content). Results demonstrate that GPT-4 achieves superior performance across all configurations, but significant variations exist between everyday morality and political contexts, highlighting the domain-sensitivity of moral reasoning in LLMs.

## Paper Outline

1. Introduction
   - Challenges in automatic moral classification
   - Limitations of supervised models
   - Need for unsupervised approaches
2. Related Works
   - Supervised methods for moral detection
   - Unsupervised methods including LLM-based approaches
3. Theoretical Grounding: Moral Foundation Theory
   - Five moral dimensions (Care, Fairness, Loyalty, Authority, Purity)
   - MFT as evaluation framework
4. Methodology
   - LLM-based models (GPT-4, GPT-3.5, Llama variants, Mistral, Mixtral)
   - NLI-based baseline model
   - Prompting strategies
5. Experimental Setting
   - Moral Foundation Reddit Corpus (MFRC) dataset
   - Multi-label moral value detection task
   - Binary moral classification task
6. Direct Human-Model Comparison Framework
   - Addressing subjectivity in gold standards
   - Equal-footing comparison methodology
7. Results and Discussion
   - Performance across model sizes
   - Domain variations (everyday vs. political morality)
   - Prompt design effectiveness

## Methods Summary

The methodology employs six LLMs (GPT-4, GPT-3.5, Llama3-70B, Mixtral-8x7B, Mistral-7B, Llama2-7B) and an NLI-based baseline in zero-shot and few-shot configurations. Models classify text according to MFT's five moral dimensions. Two prompting approaches were tested to leverage contextual understanding capabilities.

The evaluation uses the Moral Foundation Reddit Corpus (MFRC), containing 16,123 Reddit comments annotated by multiple human coders according to MFT. The study divides moral detection into two sub-tasks: (1) multi-label moral value detection (identifying specific moral dimensions in text assumed to be moral); and (2) binary moral classification (determining presence or absence of moral content).

A novel direct comparison framework places model and human annotations on equal footing, addressing the subjectivity limitations inherent in traditional gold standard evaluation. This enables clearer assessment of which moral dimensions models handle better than, comparable to, or worse than human annotators.

## Results Summary

- Model Ranking: GPT-4 achieved best overall performance, followed by GPT-3.5, Llama-70B, Mixtral-8x7B, Mistral-7B, and Llama-7B
- All LLM systems outperformed the NLI-based baseline model
- Domain Variations: Significant performance differences between everyday morality and political contexts
- Model Size Impact: Larger models generally performed better, validating the scaling hypothesis for moral reasoning
- Prompt Design: Different prompt structures influenced performance across difficulty levels
- Multi-label vs. Binary: Models showed varying relative strengths across the two task formulations
- Human-Model Comparison: Direct comparison revealed specific moral dimensions where models achieve superior or comparable performance to humans

## Conclusions

The research demonstrates that general-purpose LLMs can serve as effective unsupervised moral classifiers, with GPT-4 showing the strongest performance. However, significant domain-specific variations highlight that moral reasoning capabilities are not uniform across contexts. The novel evaluation framework addressing gold standard subjectivity provides a more rigorous methodology for assessing moral detection systems. The findings have important implications for ethical AI development, content moderation, and human-computer interaction, while also revealing current limitations that future research must address.

## Artifact Contributions

- Evaluation framework for direct human-model comparison in moral detection
- Comprehensive benchmark results across six LLMs and NLI baseline
- Analysis of model performance across MFT moral dimensions
- Experiment code and results available at: https://osf.io/kw6rc/?view_only=73c3d8e2f7c9483ea012347d70d27b6f

## Data Description

The paper evaluates six LLMs (GPT-4, GPT-3.5, Llama3-70B, Mixtral-8x7B, Mistral-7B, and Llama2-7B) as unsupervised zero-shot and few-shot moral value classifiers using the Moral Foundation Reddit Corpus (MFRC) comprising 16,123 Reddit comments. GPT-4 achieves superior performance followed by GPT-3.5 and Llama-70B, with significant variations observed across everyday morality and political contexts.


## Notes


## Citation Info

5 citations (Semantic Scholar/DOI) [2025-08-27] 5 citations (Semantic Scholar/DOI) [2025-08-23] 2 citations (Crossref/DOI) [2025-08-23]
