---




Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0488
type: preprint
short_title: "Danoliteracy of Generative Large Language Models"
year: 2025
first_author: "[[Søren Vejlgaard Holm]]"
last_author: "[[Martin Carsten Nielsen]]"
authors: "[[Søren Vejlgaard Holm]]; [[Lars Kai Hansen]]; [[Martin Carsten Nielsen]]"
url: "https://arxiv.org/abs/2410.22839"
external_pdf: "https://arxiv.org/pdf/2410.22839.pdf"
publication: arXiv
pdf_extract: "PDF Extracts/2024/2024-Holm-Danoliteracy of Generative Large Language Models.md"
local_pdf: "[[PDFs/2024/2024-Holm-Danoliteracy of Generative Large Language Models.pdf]]"
DATE_ADDED: 20260213
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "Danish"
languages_list: Danish
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark text corpus for question answering"
data_metrics: "Not specified"
LLM_assessed: "GPT-4, Claude Opus, Gemini Pro, Command R+, Llama3, Mistral, and other Danish LLMs"
DATA_URL: "https://github.com/chakki-works/seqeval"
tags: 
abstract: "The language technology moonshot moment of Generative Large Language Models (GLLMs) was not limited to English: These models brought a surge of technological applications, investments, and hype to low-resource languages as well. However, the capabilities of these models in languages such as Danish were, until recently, difficult to verify beyond qualitative demonstrations due to a lack of applicable evaluation corpora."
research_topic: "Machine Learning"
authors_incomplete: false
---
# Danoliteracy of Generative Large Language Models

## Authors

[[Søren Vejlgaard Holm]], [[Lars Kai Hansen]], [[Martin Carsten Nielsen]]

## Metadata

**Authors:** Søren Vejlgaard Holm, Lars Kai Hansen, Martin Carsten Nielsen

**Year:** 2024

**Type:** preprint

**Venue:** arXiv

**Languages:** Danish

**Benchmark:** Danoliteracy

## Links

- **arXiv:** https://arxiv.org/abs/2410.22839

## Abstract

GLLM benchmark evaluating Danish language and cultural competency across 8 scenarios including citizenship tests and social media QA. Produces robust ranking correlating to human feedback at rho ~0.8. GPT-4 and Claude Opus achieve highest rankings.

## Summary

This paper presents the Danoliterate Benchmark, a comprehensive evaluation framework for measuring 'Danoliteracy' (Danish language and cultural competency) of Generative Large Language Models across eight diverse scenarios including Danish citizenship tests and abstractive social media question answering. The benchmark evaluates 83 GLLMs including both closed-source and open-weights models, producing a robust ranking that correlates with human feedback at ρ ≈ 0.8, with GPT-4 and Claude Opus achieving the highest rankings. Factor analysis reveals one strong underlying factor explaining 95% of scenario performance variance, suggesting the existence of a 'g factor' of model consistency in language adaptation. The work addresses the critical gap in GLLM evaluation for low-resource languages (Danish has 6 million speakers) and provides evidence that closed models significantly outperform open-weights models in Danish language tasks.

## Data Description

Danoliteracy is a GLLM benchmark evaluating Danish language and cultural competency across 8 scenarios including citizenship tests and social media QA. Produces robust ranking correlating to human feedback at rho ~0.8. GPT-4 and Claude Opus achieve highest rankings.


## Detailed Summary

This paper presents the Danoliterate Benchmark, a comprehensive evaluation framework for measuring "Danoliteracy" -- the Danish language and cultural competency of Generative Large Language Models (GLLMs). The benchmark comprises eight diverse evaluation scenarios including Danish citizenship tests and abstractive social media question answering, designed to capture both linguistic fluency and cultural understanding specific to Denmark. The evaluation covers 83 GLLMs including both closed-source (GPT-4, Claude Opus) and open-weight models, producing a robust ranking that correlates with human feedback at rho approximately 0.8. Factor analysis reveals one strong underlying factor explaining 95% of scenario performance variance, suggesting the existence of a "g factor" of model consistency in language adaptation.

## Paper Outline

1. Introduction - Need for evaluating GLLM competency in low-resource languages like Danish
2. The Danoliterate Benchmark - Eight evaluation scenarios, design principles
3. Models Evaluated - 83 GLLMs spanning closed-source and open-weight
4. Results - Performance rankings, correlation with human feedback
5. Factor Analysis - "g factor" of language adaptation consistency
6. Discussion - Implications for low-resource language evaluation
7. Conclusion

## Methods Summary

The benchmark includes eight evaluation scenarios selected to test different aspects of Danish language and cultural competency: citizenship test questions (testing cultural and civic knowledge), abstractive social media QA (testing colloquial Danish understanding), and other scenarios covering varied aspects of Danish language use. The 83 evaluated models span multiple model families and sizes. Human evaluation is conducted to validate automatic metrics, establishing correlation between benchmark scores and human judgments. Factor analysis is performed across scenario performances to identify underlying performance dimensions and test whether a single factor explains cross-scenario variation.

## Results Summary

GPT-4 and Claude Opus achieve the highest rankings among all 83 evaluated models. Closed-source models significantly outperform open-weight models in Danish language tasks, indicating a substantial capability gap. The ranking produced by the benchmark correlates with human feedback at rho approximately 0.8, validating its effectiveness. Factor analysis reveals one dominant factor explaining 95% of performance variance across scenarios, suggesting that Danish language competency is largely captured by a single underlying dimension -- a "g factor" of language adaptation. This finding implies that models either transfer capabilities broadly across Danish tasks or struggle uniformly.

## Conclusions

The Danoliterate Benchmark addresses the critical gap in GLLM evaluation for low-resource languages (Danish has 6 million speakers) by providing a comprehensive, culturally-grounded evaluation framework. The strong correlation with human feedback and the emergence of a single performance factor validate the benchmark's design. The significant performance gap between closed-source and open-weight models highlights the need for continued investment in open Danish language models and resources.

## Artifact Contributions

- **Danoliterate Benchmark**: Eight-scenario evaluation framework for Danish GLLM competency
- **Comprehensive evaluation**: Performance results for 83 GLLMs on Danish tasks
- **Human validation**: Correlation with human feedback establishing benchmark reliability
- **Factor analysis**: Evidence for a "g factor" in language adaptation performance

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** Danish-specific LLM evaluation benchmark incorporating cultural competency assessment.

## Tags

