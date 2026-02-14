---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0447
type: preprint
short_title: "INCLUDE: Evaluating Multilingual Language Understanding with Regional Knowledge"
year: 2024
first_author: "[[Angelika Romanou et al. (59 authors)]]"
last_author: "[[Angelika Romanou et al. (59 authors)]]"
authors: Angelika Romanou et al. (59 authors)
url: "https://arxiv.org/abs/2411.19799"
external_pdf: "https://arxiv.org/pdf/2411.19799.pdf"
publication: arXiv
local_pdf: "[[PDFs/2024/2024-authors-INCLUDE Evaluating Multilingual Language Understanding with Regional.pdf]]"
pdf_extract: "PDF Extracts/2024/2024-authors-INCLUDE Evaluating Multilingual Language Understanding with Regional.md"
DATE_ADDED: 20260213
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
languages_list: "44 languages including French, Albanian, Armenian, Georgian, Greek, Maltese, and 39 other languages"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Multilingual benchmark dataset for question answering"
data_metrics: "Not specified"
LLM_assessed: "GPT-4o, GPT-4, Gemini, Claude, Llama, Mistral, and other multilingual LLMs"
DATA_URL: "https://huggingface.co/papers/2411.19799"
tags: 
abstract: "The performance differential of large language models (LLM) between languages hinders their effective deployment in many regions, inhibiting the potential economic and societal value of generative AI tools in many communities. However, the development of functional LLMs in many languages (i.e., multilingual LLMs) is bottlenecked by the lack of high-quality evaluation resources in languages other than English."
ethics_perspective: "Social & Cultural Values"
---
# INCLUDE: Evaluating Multilingual Language Understanding with Regional Knowledge

## Authors

[[Angelika Romanou et al. (59 authors)]]

## Metadata

**Authors:** Angelika Romanou et al. (59 authors)

**Year:** 2024

**Type:** preprint

**Venue:** arXiv

**Languages:** 44 languages including French, Albanian, Armenian, Georgian, Greek, Maltese, and 39 other languages

**Benchmark:** INCLUDE

## Links

- **arXiv:** https://arxiv.org/abs/2411.19799
- **Code/Data:** https://huggingface.co/papers/2411.19799

## Abstract

Comprehensive multilingual benchmark across 44 written languages with 197,243 QA pairs from local exam sources. Evaluates regional and cultural knowledge rather than translated English content. Models struggle in Armenian, Greek, and Urdu especially on culturally grounded topics. GPT-4o best overall at ~77% average accuracy.

## Summary

This paper introduces INCLUDE, a comprehensive multilingual knowledge and reasoning benchmark comprising 197,243 QA pairs from 1,926 local examinations across 44 languages, 15 scripts, and 52 countries. Unlike existing multilingual benchmarks that rely on English translations (creating translationese artifacts and missing regional context), INCLUDE is constructed from native academic exams, professional certifications, and regional licenses collected with native speakers, capturing authentic regional and cultural knowledge. The benchmark specifically includes questions requiring understanding of local legal systems, cultural practices, and region-specific information, addressing the Western bias prevalent in LLMs. Evaluation of both closed and open models reveals high variance across languages, with models achieving particularly low performance in low-resource languages (especially Armenian, Greek, and Urdu) on culturally grounded topics, and GPT-4o achieving the best overall performance at approximately 77% average accuracy.

## Data Description

INCLUDE is a comprehensive multilingual benchmark across 44 written languages (including French, Albanian, Armenian, Georgian, Greek, Maltese) with 197,243 QA pairs from local exam sources. Evaluates regional and cultural knowledge rather than translated English content. Models struggle in Armenian, Greek, and Urdu especially on culturally grounded topics. GPT-4o achieves best overall performance at ~77% average accuracy.


## Detailed Summary

This paper presents INCLUDE, a large-scale multilingual knowledge and reasoning benchmark comprising 197,243 QA pairs from 1,926 examinations across 44 written languages, 15 scripts, and 52 countries. Unlike existing multilingual benchmarks that rely on English translation (creating translationese artifacts and missing regional context), INCLUDE is constructed from local academic exams, professional certifications, and regional licenses collected in collaboration with native speakers, capturing authentic regional and cultural knowledge. The benchmark addresses the critical observation that language implicitly represents regional knowledge: a legal question in Greek, Russian, or English likely reflects different jurisdictional contexts. INCLUDE categorizes questions by regionality into four types: region-agnostic (34.4%), explicitly regional (18.8%), cultural (16.4%), and implicitly regional (30.4%), enabling fine-grained analysis of how models handle different levels of regional knowledge.

## Paper Outline

1. Introduction - Performance differential of LLMs across languages
2. Preliminaries - Language availability, regional knowledge definition
3. The INCLUDE Benchmark - Data collection, quality control, knowledge categorization
4. Experimental Setup - Data selection (BASE/LITE), models, prompting strategies
5. Results and Analysis - General performance, regional knowledge, language-specific analysis
6. Conclusion

## Methods Summary

Data collection involves collecting multiple-choice exams from academic, professional, and regional license sources in collaboration with native speakers. Automatic extraction is followed by quality control where native speaker co-authors verify parsed questions, filter image-dependent items, and annotate metadata (language, topic, level, country). The benchmark is enriched with existing datasets (ArabicMMLU, ChineseMMLU, TurkishMMLU, PersianMMLU, VNHSGE, EXAMS). Two evaluation subsets are curated: INCLUDE-BASE (22,635 QA pairs, max 550 per language) and INCLUDE-LITE (10,770 pairs, max 250 per language). Models are evaluated with 5-shot and zero-shot CoT settings, using both in-language and English prompts, with optional regional prefix prompting.

## Results Summary

GPT-4o achieves the highest overall performance at approximately 77% accuracy across all domains. CoT prompting moderately enhances GPT-4o on Professional and STEM tasks but causes significant drops for Llama-3.1-70B and Qwen2.5-14B. For smaller models (8B or less), Gemma-7B delivers best overall performance. Instruction-tuning shows little benefit and sometimes hurts performance (Gemma-7B-Instruct drops ~15%). Scaling model size within families (Aya-expanse 8B to 32B: +12%; Qwen2.5 7B to 14B: +7%) significantly improves multilingual capabilities. Models struggle most with region-specific questions requiring local legal, regulatory, or cultural knowledge, with performance variance highest across languages for these question types.

## Conclusions

INCLUDE demonstrates that current LLMs exhibit significant performance gaps when evaluated on authentic regional knowledge rather than translated English content. Models perform particularly poorly on low-resource languages and culturally-grounded topics. The benchmark provides a comprehensive resource for evaluating whether multilingual LLMs can genuinely serve diverse language communities rather than merely processing translated content.

## Artifact Contributions

- **INCLUDE benchmark**: 197,243 QA pairs in 44 languages from 1,926 exams (available at https://huggingface.co/datasets/CohereForAI/include-base-44)
- **INCLUDE-BASE and INCLUDE-LITE**: Standardized evaluation subsets with balanced language coverage
- **Regional knowledge taxonomy**: Four-category classification (region-agnostic, explicitly regional, cultural, implicitly regional)
- **Comprehensive evaluation**: Results for GPT-4o, Llama-3.1, Aya-Expanse, Qwen2.5, Gemma, and Mistral families

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6, B9
**Relevance:** Covers all five target languages (Greek, Armenian, Georgian, Albanian, Maltese). Tests culturally-specific regional knowledge. Directly relevant to cultural values evaluation across European minority languages.

## Tags

