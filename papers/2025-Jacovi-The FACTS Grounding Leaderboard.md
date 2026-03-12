---



























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: ESZUEQJQ
type: journalArticle
year: 2025
short_title: "The FACTS Grounding Leaderboard"
first_author: "[[Alon Jacovi]]"
last_author: "[[Dipanjan Das]]"
authors: "Alon Jacovi; Andrew Wang; Chris Alberti; Connie Tao; Jon Lipovetz; Kate Olszewska; Michelle Liu; Nate Keating; Adam Bloniarz; Carl Saroufim; Corey Fry; Dror Marcus; Gaurav Singh Tomar; James Swirhun; Jinwei Xing; Lily Wang; Madhu Gurumurthy; Michael Aaron; Moran Ambar; Rachana Fellinger; Rui Wang; Zizhao Zhang; Sasha Goldshtein; Dipanjan Das"
external_pdf: "file:///Users/jimmylin/Zotero/storage/ELGTPL3J/Jacovi et al. - The FACTS Grounding Leaderboard Benchmarking LLMs' Ability to Ground Responses to Long-Form Input.pdf"
pdf_extract: "PDF Extracts/2025/2025-Jacovi-The FACTS Grounding Leaderboard.md"
local_pdf: "[[PDFs/2025/2025-Jacovi-The FACTS Grounding Leaderboard.pdf]]"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Hallucination & Truthfulness"
key_contribution: "Introduced the FACTS Grounding Leaderboard to evaluate LLMs' ability to generate long-form responses that are fully grounded in a provided 32k token context."
significance: "Benchmarks 'long-context faithfulness', a critical capability for RAG systems to ensure that models do not hallucinate information outside of the retrieved documents."
tags: 
abstract: "We introduce FACTS Grounding, an online leaderboard and associated benchmark that evaluates language models' ability to generate text that is factually accurate with respect to given context in the user prompt. In our benchmark, each prompt includes a user request and a full document, with a maximum length of 32k tokens, requiring long-form responses. The long-form responses are required to be fully grounded in the provided context document while fulfilling the user request. Models are evaluated using automated judge models in two phases: (1) responses are disqualified if they do not fulfill the user request; (2) they are judged as accurate if the response is fully grounded in the provided document. The automated judge models were comprehensively evaluated against a held-out test-set to pick the best prompt template, and the final factuality score is an aggregate of multiple judge models to mitigate evaluation bias. The FACTS Grounding leaderboard will be actively maintained over time, and contains both public and private splits to allow for external participation while guarding the integrity of the leaderboard. It can be found at https://www.kaggle.com/facts-leaderboard."
CONF-CC: "N/A"
DATE_ADDED: 20260129
LLM_assessed: "Gemini, GPT-4o, Claude"
DATA_URL: "https://www.kaggle.com/facts-leaderboard"
research_topic: "Other"
CONFERENCE: "Journal"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Hallucination & Truthfulness"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark for bias and fairness"
data_metrics: "32k tokens"
---
# The FACTS Grounding Leaderboard: Benchmarking LLMs’ Ability to Ground Responses to Long-Form Input

## Metadata

**Authors:** Jacovi, Alon; Wang, Andrew; Alberti, Chris; Tao, Connie; Lipovetz, Jon; Olszewska, Kate; Liu, Michelle; Keating, Nate; Bloniarz, Adam; Saroufim, Carl; Fry, Corey; Marcus, Dror; Tomar, Gaurav Singh; Swirhun, James; Xing, Jinwei; Wang, Lily; Gurumurthy, Madhu; Aaron, Michael; Ambar, Moran; Fellinger, Rachana; Wang, Rui; Zhang, Zizhao; Goldshtein, Sasha; Das, Dipanjan

**Type:** journalArticle

## Links

- **Arxiv:** https://arxiv.org/abs/2501.03200
- **Deepmind:** https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/

## Abstract

We introduce FACTS Grounding, an online leaderboard and associated benchmark that evaluates language models' ability to generate text that is factually accurate with respect to given context in the user prompt. In our benchmark, each prompt includes a user request and a full document, with a maximum length of 32k tokens, requiring long-form responses. The long-form responses are required to be fully grounded in the provided context document while fulfilling the user request. Models are evaluated using automated judge models in two phases: (1) responses are disqualified if they do not fulfill the user request; (2) they are judged as accurate if the response is fully grounded in the provided document. The automated judge models were comprehensively evaluated against a held-out test-set to pick the best prompt template, and the final factuality score is an aggregate of multiple judge models to mitigate evaluation bias. The FACTS Grounding leaderboard will be actively maintained over time, and contains both public and private splits to allow for external participation while guarding the integrity of the leaderboard. It can be found at https://www.kaggle.com/facts-leaderboard.

## Authors

[[Alon Jacovi]], [[Andrew Wang]], [[Chris Alberti]], [[Connie Tao]], [[Jon Lipovetz]], [[Kate Olszewska]], [[Michelle Liu]], [[Nate Keating]], [[Adam Bloniarz]], [[Carl Saroufim]], [[Corey Fry]], [[Dror Marcus]], [[Gaurav Singh Tomar]], [[James Swirhun]], [[Jinwei Xing]], [[Lily Wang]], [[Madhu Gurumurthy]], [[Michael Aaron]], [[Moran Ambar]], [[Rachana Fellinger]], [[Rui Wang]], [[Zizhao Zhang]], [[Sasha Goldshtein]], [[Dipanjan Das]]

## Detailed Summary

FACTS Grounding introduces an online leaderboard and benchmark specifically designed to evaluate how well large language models (LLMs) can generate text that is factually accurate with respect to given context documents up to 32k tokens in length. The benchmark addresses a critical gap in LLM evaluation by focusing on "grounded factuality" - the ability to synthesize information exclusively from provided documents without hallucinating or incorporating external knowledge, while still fulfilling diverse user requests including summarization, fact-finding, and information analysis.

The methodology employs a rigorous two-phase evaluation pipeline using multiple LLM judges (Gemini 1.5 Pro, GPT-4o, and Claude 3.5 Sonnet) to first filter ineligible responses that fail to address user requests, then assess factuality of remaining responses. The benchmark contains 860 public and 859 private examples across five enterprise domains (medical, legal, technology, financial, retail) with nine task types. Results demonstrate that Gemini 2.0 Flash Experimental achieves the highest final factuality score (83.6%), with notable findings including consistent self-preference bias in judge models (+3.23% on average) and a 1-5% reduction in scores when disqualifying ineligible responses.

## Paper Outline

1. Introduction - Defines factuality challenges in LLMs, distinguishing grounded vs. external knowledge factuality
2. Data - Describes annotation methodology, quality assurance, and dataset composition (860 public + 859 private examples)
3. Metrics - Explains unadjusted factuality score calculation and ineligible response disqualification
4. Results - Presents model rankings with 95% confidence intervals across public and blind splits
5. Conclusion - Summarizes contributions and encourages research community adoption
6. Appendix A - Provides complete judge prompt templates for factuality and eligibility evaluation

## Methods Summary

The benchmark uses three LLM judges (Gemini 1.5 Pro, GPT-4o, Claude 3.5 Sonnet) with seven different prompt templates evaluated against a held-out test set (N=402) to select optimal templates via Macro-F1. Factuality scoring involves binary classification of whether responses are fully grounded in provided context, with the final score averaging across all three judges to mitigate self-preference bias. Ineligible response detection uses a consensus mechanism requiring all three judges to flag a response before disqualification. The dataset was curated by human raters across five enterprise domains with context lengths up to 32k tokens, with quality assurance filtering for non-trivial requests and proper grounding instructions.

## Results Summary

Gemini 2.0 Flash Experimental achieved the highest final factuality score (83.6%), followed by Gemini 1.5 Flash (82.9%), Gemini 1.5 Pro (80.0%), Claude 3.5 Sonnet (79.4%), and GPT-4o (78.8%). OpenAI o1-preview and o1-mini performed notably lower (61.7% and 62.0%). The study found consistent self-preference bias across all models (+3.23% average increase when judging own outputs). Disqualifying ineligible responses caused 1-5% score reductions and minor ranking shifts (e.g., Gemini 1.5 Flash moved from rank 1 to 2). The span-level and implicit span-level prompt templates achieved the highest Macro-F1 scores for factuality judgment across different judge models.

## Conclusions

The authors conclude that FACTS Grounding fills an important gap in evaluating LLM factuality for long-form, grounded generation tasks. The benchmark design with public and private splits enables external participation while protecting integrity. Key findings include the importance of multi-judge aggregation to mitigate self-preference bias, the value of filtering ineligible responses to prevent metric gaming, and the observation that current frontier models still show significant room for improvement in grounded factuality. The leaderboard will be actively maintained with new model additions.

## Artifact Contributions

- Online leaderboard available at https://www.kaggle.com/facts-leaderboard
- Benchmark dataset: 860 public examples ("Open" split) + 859 private examples ("Blind" split)
- Comprehensive judge prompt templates for factuality and eligibility evaluation (7 templates evaluated)
- Detailed evaluation methodology and metrics for grounded factuality assessment

## Data Description

FACTS Grounding is a benchmark and online leaderboard evaluating LLMs' ability to generate factually accurate, grounded long-form responses to user requests given context documents of up to 32k tokens. The benchmark contains 860 public and 859 private examples spanning medical, legal, technology, financial, and retail domains, evaluated by automated judge models (Gemini 1.5 Pro, GPT-4o, Claude 3.5 Sonnet) across multiple prompt templates.


## Notes

