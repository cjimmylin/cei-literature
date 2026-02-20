---






Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0433
type: preprint
short_title: "M-ALERT: LLMs Lost in Translation: M-ALERT uncovers Cross-Linguistic Safety Inconsistencies"
year: 2024
first_author: "[[Felix Friedrich]]"
last_author: "[[Kristian Kersting]]"
authors: "Felix Friedrich, Simone Teber, Patrick Schramowski, Manuel Brack, Kristian Kersting"
url: "https://arxiv.org/abs/2412.15035"
external_pdf: "https://arxiv.org/pdf/2412.15035.pdf"
publication: arXiv
CONF-CC: "Preprint"
pdf_extract: "PDF Extracts/2024/2024-Friedrich-M-ALERT LLMs Lost in Translation M-ALERT uncovers Cross-Linguistic.md"
local_pdf: "[[PDFs/2024/2024-Friedrich-M-ALERT LLMs Lost in Translation M-ALERT uncovers Cross-Linguistic.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "French, German, Italian, Spanish"
cultures_nationalities_list: "French, German, Italian, Spanish"
languages_list: "English, French, German, Italian, Spanish"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: "GPT-3.5, GPT-4, Claude-2, Llama-2, Mistral, Gemini, Command, and 32 additional LLMs (39 total)"
DATA_URL: "https://github.com/cmu-lti/m-alert"
tags: 
abstract: "Building safe Large Language Models (LLMs) across multiple languages is essential in ensuring both safe access and linguistic diversity. To this end, we conduct a large-scale, comprehensive safety evaluation of the current LLM landscape. For this purpose, we introduce M-ALERT, a multilingual benchmark that evaluates the safety of LLMs in five languages: English, French, German, Italian, and Spanish."
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Multilingual benchmark for ai safety"
data_metrics: "Not specified"
CONFERENCE: "Preprint"
---
# M-ALERT: LLMs Lost in Translation: M-ALERT uncovers Cross-Linguistic Safety Inconsistencies

## Authors

[[Felix Friedrich]], [[Simone Teber]], [[Patrick Schramowski]], [[Manuel Brack]], [[Kristian Kersting]]

## Metadata

**Authors:** Felix Friedrich, Simone Teber, Patrick Schramowski, Manuel Brack, Kristian Kersting

**Year:** 2024

**Type:** preprint

**Venue:** arXiv

**Languages:** English, French, German, Italian, Spanish

**Benchmark:** M-ALERT

## Links

- **arXiv:** https://arxiv.org/abs/2412.15035

## Abstract

Multilingual benchmark evaluating LLM safety in five European languages with 15K high-quality prompts per language (75K total). Extensive experiments on 39 state-of-the-art LLMs show significant inconsistencies in safety across languages and categories, with French often showing disproportionately high toxicity rates.

## Summary

This paper introduces M-ALERT, a multilingual benchmark for evaluating the safety of large language models across five European languages (English, French, German, Italian, and Spanish), comprising 15,000 high-quality prompts per language for a total of 75,000 prompts. The authors conduct extensive experiments on 39 state-of-the-art LLMs including GPT-3.5, GPT-4, Claude-2, Llama-2, Mistral, Gemini, and Command, testing for jailbreaking resistance, toxicity, and harmful content generation. Results reveal significant cross-linguistic safety inconsistencies, with French showing disproportionately high toxicity rates compared to other European languages and substantial variation across safety categories. This work highlights critical gaps in multilingual safety alignment and the need for language-specific safety interventions.

## Data Description

M-ALERT multilingual safety benchmark containing 75,000 prompts across 5 European languages (English, French, German, Italian, Spanish). Tests jailbreaking, toxicity, and harmful content generation across 39 state-of-the-art LLMs, revealing significant cross-linguistic safety vulnerabilities.


## Detailed Summary

This paper introduces M-ALERT (Multilingual Assessment of Language model safety through Evaluation of Responsible and Trustworthy behavior), a multilingual safety benchmark that evaluates LLMs across five European languages: English, French, German, Italian, and Spanish. M-ALERT comprises approximately 15,000 high-quality safety prompts per language, totaling 75,000 prompts, designed to test whether models produce unsafe content when provoked with potentially harmful queries. The benchmark extends the English ALERT dataset by translating prompts using GPT-4 and employing native-speaking experts for quality validation. The prompts cover a comprehensive safety taxonomy with categories including crime and illegal activities, hate speech and discrimination, substance abuse, self-harm, and sexual content. The authors conduct extensive experiments on 39 state-of-the-art LLMs spanning both open-source models (Llama-2, Llama-3, Mistral, Qwen, Yi, Gemma, Phi, and others) and proprietary models (GPT-3.5, GPT-4, Claude-2, Gemini, Command). Safety is assessed by generating responses to each prompt and then classifying the generated text as safe or unsafe using a fine-tuned Llama-Guard classifier adapted for multilingual evaluation. The benchmark reveals significant cross-linguistic safety inconsistencies, with models often being safe in English but producing unsafe content in other languages.

## Paper Outline

1. Introduction - Motivation for multilingual LLM safety evaluation, English-centric safety gap
2. Related Work - Safety benchmarks, multilingual NLP, jailbreaking research
3. M-ALERT Benchmark - Translation methodology, quality assurance, safety taxonomy, category descriptions
4. Experimental Setup - 39 LLMs evaluated, generation parameters, safety classification methodology
5. Results - Overall safety scores, language-specific analysis, category-wise breakdown, French disproportionate toxicity finding
6. Analysis - Cross-linguistic inconsistencies, model family comparisons, impact of instruction tuning and RLHF
7. Conclusion - Key findings, implications for multilingual safety alignment

## Methods Summary

M-ALERT extends the English ALERT benchmark by translating approximately 15,000 prompts into French, German, Italian, and Spanish using GPT-4 as the translation engine, followed by quality validation from native-speaking experts who verified translation accuracy, cultural appropriateness, and preservation of the safety-testing intent. The safety taxonomy organizes prompts into hierarchical categories covering crime, hate/discrimination, substance abuse, self-harm, and sexual content, with subcategories for granular analysis. For evaluation, each of the 39 LLMs generates responses to all 75,000 prompts, and a multilingual Llama-Guard safety classifier determines whether each response is safe or unsafe. Safety scores are computed as the percentage of safe responses per language and category. The evaluation covers diverse model families including instruction-tuned, base, and RLHF-aligned variants to understand how different alignment strategies affect multilingual safety.

## Results Summary

The evaluation of 39 LLMs reveals significant cross-linguistic safety inconsistencies. French consistently shows disproportionately high toxicity rates compared to other European languages, with many models producing substantially more unsafe content in French than in English, German, Italian, or Spanish. Instruction-tuned and RLHF-aligned models generally demonstrate improved safety across languages compared to their base counterparts, but the improvement is uneven across languages. Some models that achieve near-perfect safety scores in English exhibit considerably lower safety in non-English languages, suggesting that safety alignment procedures are heavily biased toward English. Category-wise analysis reveals that hate speech and discrimination, along with sexual content, show the largest cross-linguistic variation, while categories like self-harm show more consistent safety across languages. Among evaluated models, GPT-4 and Claude-2 generally achieve the highest multilingual safety scores, though even these models show measurable drops in non-English languages. Open-source models exhibit wider variation, with some (e.g., certain Llama-3 variants) approaching proprietary model safety levels while others show significant safety gaps.

## Conclusions

M-ALERT demonstrates that current LLM safety alignment is insufficiently multilingual, with models frequently exhibiting safety degradation when operating in non-English European languages. The finding that French shows disproportionately high toxicity is particularly notable and warrants further investigation into the training data and alignment procedures used for French-language safety. The benchmark highlights a critical need for language-specific safety interventions and more balanced multilingual alignment during training. Limitations include the focus on only five European languages (excluding lower-resource and non-Western languages), reliance on automated safety classification rather than human evaluation, and the translation-based approach which may not capture culturally specific safety concerns that differ from English. The benchmark and evaluation code are released to enable continued multilingual safety research.

## Artifact Contributions

- **M-ALERT Benchmark**: 75,000 safety prompts across 5 European languages (15,000 per language) with hierarchical safety taxonomy (https://github.com/cmu-lti/m-alert)
- **Multilingual Safety Evaluation**: Comprehensive evaluation results for 39 LLMs across 5 languages
- **Safety Classification Pipeline**: Multilingual Llama-Guard-based safety assessment framework

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** Reveals that French has disproportionately high toxicity rates compared to other European languages. Evaluates 39 LLMs with category-wise safety annotations.

## Tags

