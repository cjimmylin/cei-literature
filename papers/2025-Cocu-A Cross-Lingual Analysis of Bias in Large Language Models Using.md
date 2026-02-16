---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0522
type: preprint
short_title: "A Cross-Lingual Analysis of Bias in Large Language Models Using Romanian History"
year: 2025
first_author: "[[Matei-Iulian Cocu]]"
last_author: "[[Adrian Marius Dumitran]]"
authors: "[[Matei-Iulian Cocu]]; [[Răzvan-Cosmin Cristia]]; [[Adrian Marius Dumitran]]"
url: "https://arxiv.org/abs/2510.02362"
external_pdf: "https://arxiv.org/pdf/2510.02362.pdf"
publication: arXiv
pdf_extract: "PDF Extracts/2025/2025-Cocu-A Cross-Lingual Analysis of Bias in Large Language Models Using.md"
local_pdf: "[[PDFs/2025/2025-Cocu-A Cross-Lingual Analysis of Bias in Large Language Models Using.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "Russian"
cultures_nationalities_list: "Romanian, Russian, Hungarian"
languages_list: "English, Romanian, and others"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: "DeepSeek, LLama-4, Llama, gemma"
DATA_URL: "NA"
tags: 
abstract: "In this case study, we select a set of controversial Romanian historical questions and ask multiple Large Language Models to answer them across languages and contexts, in order to assess their biases. Besides being a study mainly performed for educational purposes, the motivation also lies in the recognition that history is often presented through altered perspectives, primarily influenced by the culture and ideals of a state, even through large language models."
authors_incomplete: false
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "No"
is_eval: "No"
is_dataset: "No"
data_description: "N/A"
data_metrics: "Not specified"
---
# A Cross-Lingual Analysis of Bias in Large Language Models Using Romanian History

## Authors

[[Matei-Iulian Cocu]], [[Răzvan-Cosmin Cristia]], [[Adrian Marius Dumitran]]

## Metadata

**Authors:** Matei-Iulian Cocu, Răzvan-Cosmin Cristia, Adrian Marius Dumitran

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** English, Romanian, and others

## Links

- **arXiv:** https://arxiv.org/abs/2510.02362

## Abstract

Selects controversial Romanian historical questions and tests multiple LLMs across languages. Results show binary response stability varies by language, with models flipping stance across languages or between formats. Romanian used as native baseline to ground the cultural context.

## Summary

This paper examines cultural and political biases in LLMs by testing their responses to controversial Romanian historical questions across multiple languages and contexts. Using Romanian as the native baseline, the study demonstrates that binary response stability varies significantly by language, with models frequently flipping their stance on the same question when prompted in different languages or formats. The case study approach reveals how history is often presented through culturally altered perspectives influenced by state ideals, and how these biases manifest in LLM responses.

## Data Description

Examines how multiple LLMs respond to controversial Romanian historical questions across languages and contexts to assess cultural and political biases. Finds binary response stability varies by language, with models flipping stance across languages. Does not introduce a dataset or evaluate specific models systematically.


## Detailed Summary

This paper presents a case study examining cultural and geopolitical biases in LLMs by testing 13 models on 14 controversial Romanian historical questions across four languages: Romanian (native baseline), English (global default), Hungarian (direct counter-narrative due to historical tensions), and Russian (major regional power with intersecting narratives). The methodology employs a three-layered questioning process designed to probe bias at increasing abstraction levels: (1) forced binary Yes/No answers to establish absolute stance, (2) Likert-scale 1-10 ratings to measure conviction and identify stance reversals, and (3) structured essays evaluated by an LLM-as-a-judge. Five runs were conducted at default temperature plus one at 0.6 for comparison. The 14 statements span from the Middle Ages to the Fall of Communism, covering topics like the Transylvanian dispute between Romania and Hungary. The study reveals that Yes/No stability is relatively high but far from perfect (means 0.75-0.81), with Russian showing highest consistency and English/Hungarian lower. Models frequently flip stance across languages or between answer formats, and numeric ratings frequently diverge from initial binary choices.

## Paper Outline

1. Introduction - LLM reasoning biases and historical bias through cultural lenses
2. Related Work - Bias in LLMs; persona prompting; cultural alignment
3. Methodology - Language selection, historical statement design, three-layered questioning
4. Results - Consistency analysis, cross-lingual comparison, format effects
5. Discussion - Implications for educational use and cultural fairness
6. Conclusion

## Methods Summary

Thirteen LLMs (including DeepSeek variants, Llama-4-Scout, gemma-3n, gpt-oss-20b) are tested on 14 controversial Romanian historical statements in four languages. The three-phase methodology uses: (a) forced Yes/No binary response, (b) 1-10 Likert-scale rating, and (c) detailed essay with LLM-as-a-judge evaluation. Statements were developed in consultation with a professional medievalist. Five runs at default temperature plus one at temperature 0.6 were conducted. Cross-lingual and cross-format consistency are measured using standard deviation and agreement scores.

## Results Summary

Yes/No consistency averages 0.75-0.81 across models, with Russian showing highest stability and English/Hungarian lower. Models frequently flip stance across languages and between formats -- numeric ratings often diverge from binary choices, revealing "stance reversals" where an affirmative answer pairs with unexpectedly low scores. Some small-scale models (LLama-4-Scout, gemma-3n) show high within-model consistency while DeepSeek variants struggle. OpenAI's gpt-oss-20b shows drastically low consistency for Romanian queries. The most consistent models are not always those judged most accurate or neutral by the LLM judge.

## Conclusions

The study demonstrates that LLMs exhibit significant inconsistency when handling culturally sensitive historical topics across languages, with the prompt format and language of inquiry substantially influencing apparent stance. These findings have important implications for educational applications of LLMs, where presenting biased or inconsistent historical narratives could reinforce stereotypes or misinform students about contested historical events.

## Artifact Contributions

- **Evaluation Framework:** Three-layered questioning methodology for probing cross-lingual bias on historical topics
- **Dataset:** 14 controversial Romanian historical statements with multi-language, multi-format evaluation across 13 LLMs

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B8
**Relevance:** Romanian-specific bias study that directly examines how LLMs handle culturally sensitive historical topics across languages.

## Tags

