---


























Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: TIFC8Z6D
type: conferencePaper
short_title: "Towards Measuring the Representation of"
year: 2023
first_author: "[[Esin Durmus]]"
last_author: "[[Deep Ganguli]]"
authors: "Esin Durmus; Karina Nguyen; Thomas I. Liao; Nicholas Schiefer; Amanda Askell; Anton Bakhtin; Carol Chen; Zac Hatfield-Dodds; Danny Hernandez; Nicholas Joseph; Liane Lovitt; Sam McCandlish; Orowa Sikder; Alex Tamkin; Janel Thamkul; Jared Kaplan; Jack Clark; Deep Ganguli"
doi: 10.48550/arXiv.2306.16388
url: "http://arxiv.org/abs/2306.16388"
external_pdf: "http://arxiv.org/pdf/2306.16388.pdf"
publication: arXiv.org
CONF-CC: "Preprint"
national_ethnic_cultural: "American"
cultures_nationalities_list: "Cross-cultural"
languages_list: "Multilingual"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: American
tags: 
pdf_extract: "PDF Extracts/2023/2023-Durmus-Towards Measuring the Representation of.md"
abstract: "Large language models (LLMs) may not equitably represent diverse global perspectives on societal issues. In this paper, we develop a quantitative framework to evaluate whose opinions model-generated responses are more similar to. We first build a dataset, GlobalOpinionQA, comprised of questions and answers from cross-national surveys designed to capture diverse opinions on global issues across different countries."
paper_summary: "Abstract: Large language models (LLMs) may not equitably represent diverse global per- spectives on societal issues. In this paper, we develop a quantitative framework to evaluate whose opinions model-generated | Overview: Towards Measuring the Representation of Subjective Global Opinions in Language Models Esin Durmus∗ Karina Nguyen Thomas I. Liao Nicholas Schiefer Amanda Askell Anton Bakhtin Carol Chen Zac Hatfield-Do | Conclusions: Our study relies on two established global surveys and social science literature to analyze broad societal values. However, we acknowledge several lim"
local_pdf: "[[PDFs/2023/2023-Durmus-Towards Measuring the Representation of.pdf]]"
DATE_ADDED: 20260208
LLM_assessed: Claude
DATA_URL: "https://huggingface.co/datasets/Anthropic/llm_global_opinions"
CONFERENCE: "Other Conference"
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation framework dataset for question answering"
data_metrics: "Not specified"
---
# Towards Measuring the Representation of Subjective Global Opinions in Language Models

## Metadata

**Authors:** Durmus, Esin; Nguyen, Karina; Liao, Thomas I.; Schiefer, Nicholas; Askell, Amanda; Bakhtin, Anton; Chen, Carol; Hatfield-Dodds, Zac; Hernandez, Danny; Joseph, Nicholas; Lovitt, Liane; McCandlish, Sam; Sikder, Orowa; Tamkin, Alex; Thamkul, Janel; Kaplan, Jared; Clark, Jack; Ganguli, Deep

**Year:** 2024

**Type:** preprint

**DOI:** [10.48550/arXiv.2306.16388](https://doi.org/10.48550/arXiv.2306.16388)

**Publisher:** arXiv

## Links

- **Local PDF:** [[PDFs/2023/2023-Durmus-Towards Measuring the Representation of.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2306.16388
- **DOI:** https://doi.org/10.48550/arXiv.2306.16388

## Abstract

Large language models (LLMs) may not equitably represent diverse global perspectives on societal issues. In this paper, we develop a quantitative framework to evaluate whose opinions model-generated responses are more similar to. We first build a dataset, GlobalOpinionQA, comprised of questions and answers from cross-national surveys designed to capture diverse opinions on global issues across different countries. Next, we define a metric that quantifies the similarity between LLM-generated survey responses and human responses, conditioned on country. With our framework, we run three experiments on an LLM trained to be helpful, honest, and harmless with Constitutional AI. By default, LLM responses tend to be more similar to the opinions of certain populations, such as those from the USA, and some European and South American countries, highlighting the potential for biases. When we prompt the model to consider a particular country’s perspective, responses shift to be more similar to the opinions of the prompted populations, but can reflect harmful cultural stereotypes. When we translate GlobalOpinionQA questions to a target language, the model’s responses do not necessarily become the most similar to the opinions of speakers of those languages. We release our dataset for others to use and build on.2 We also provide an interactive visualization at https://llmglobalvalues.anthropic.com.

## Authors

[[Esin Durmus]], [[Karina Nguyen]], [[Thomas I. Liao]], [[Nicholas Schiefer]], [[Amanda Askell]], [[Anton Bakhtin]], [[Carol Chen]], [[Zac Hatfield-Dodds]], [[Danny Hernandez]], [[Nicholas Joseph]], [[Liane Lovitt]], [[Sam McCandlish]], [[Orowa Sikder]], [[Alex Tamkin]], [[Janel Thamkul]], [[Jared Kaplan]], [[Jack Clark]], [[Deep Ganguli]]

## Data Description

The paper introduces GlobalOpinionQA, a dataset of 2,556 multiple-choice questions compiled from the Pew Global Attitudes Survey (2,203 questions) and World Values Survey Wave 7 (353 questions). The dataset captures diverse global opinions on societal issues across many countries and is used to measure the similarity between LLM-generated survey responses and human responses conditioned on country.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computation-and-Language

## Citation Info

606 citations (Semantic Scholar/DOI) [2025-08-27] 269 citations (Semantic Scholar/arXiv) [2025-08-27] 264 citations (Semantic Scholar/arXiv) [2025-08-23] arXiv:2306.16388 [cs]
