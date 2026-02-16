---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: MQX8ISEP
type: conferencePaper
short_title: "Whose Opinions Do Language Models Reflect?"
year: 2025
first_author: "[[Shibani Santurkar]]"
last_author: "[[Tatsunori Hashimoto]]"
authors: "Shibani Santurkar; Esin Durmus; Faisal Ladhak; Cinoo Lee; Percy Liang; Tatsunori Hashimoto"
url: "http://arxiv.org/abs/2303.17548"
external_pdf: "http://arxiv.org/pdf/2303.17548.pdf"
national_ethnic_cultural: "American"
cultures_nationalities_list: "American"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "American, AI Safety & Alignment"
key_contribution: "Created OpinionsQA to compare LLM views against US public opinion polls, finding mismatches (e.g., misalignment with 65+ and widowed groups)."
significance: "Quantifies specific demographic biases in 'aligned' models, showing they often reflect a narrow 'WEIRD' (Western, Educated, Industrialized, Rich, Democratic) worldview rather than a representative one."
tags: 
osint_source: "Recovered via HTML"
pdf_extract: "PDF Extracts/2023/2023-Santurkar-Whose Opinions Do Language Models Reflect.md"
abstract: "Language models (LMs) are increasingly being used in open-ended contexts, where the opinions reﬂected by LMs in response to subjective queries can have a profound impact, both on user satisfaction, as well as shaping the views of society at large. In this work, we put forth a quantitative framework to investigate the opinions reﬂected by LMs – by leveraging high-quality public opinion polls and their associated human responses."
paper_summary: "Abstract: Language models (LMs) are increasingly being used in open-ended contexts, where the opinions reﬂected by LMs in response to subjective queries can have a profound impact, both on user satisfaction, as | Overview: Whose Opinions Do Language Models Reﬂect? Shibani Santurkar Stanford shibani@stanford.edu Esin Durmus Stanford esindurmus@cs.stanford.edu Faisal Ladhak Columbia University faisal@cs.columbia.edu Cinoo | Methodology: from the main paper), focusing on the 500 questions from Section 4.2 computational reasons—see Appendix Figure 14. We only include a subset of demogra | Conclusions: Our work puts forth a framework to examine the opinions reﬂected by LMs through the lens of public opinion polls. Using our OpinionQA dataset, we iden"
local_pdf: "[[PDFs/2023/2023-Santurkar-Whose Opinions Do Language Models Reflect.pdf]]"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation framework dataset for question answering"
data_metrics: "Not specified"
LLM_assessed: "GPT-3, text-davinci, InstructGPT"
DATA_URL: "https://github.com/tatsu-lab/opinions_qa"
publication: "ICML 2023"
DATE_ADDED: 20260207
---
# Whose Opinions Do Language Models Reflect?

## Metadata

**Authors:** Santurkar, Shibani; Durmus, Esin; Ladhak, Faisal; Lee, Cinoo; Liang, Percy; Hashimoto, Tatsunori

**Year:** 2023

**Publication:** ICML

**Type:** conferencePaper

## Links

- **Local PDF:** [[PDFs/2023/2023-Santurkar-Whose Opinions Do Language Models Reflect.pdf|Open PDF]]

- **arXiv:** http://arxiv.org/abs/2303.17548

## Abstract

Language models (LMs) are increasingly being used in open-ended contexts, where the opinions reflected by LMs in response to subjective queries can have a profound impact, both on user satisfaction, as well as shaping the views of society at large. In this work, we put forth a quantitative framework to investigate the opinions reflected by LMs -- by leveraging high-quality public opinion polls and their associated human responses. Using this framework, we create OpinionsQA, a new dataset for evaluating the alignment of LM opinions with those of 60 US demographic groups over topics ranging from abortion to automation. Across topics, we find substantial misalignment between the views reflected by current LMs and those of US demographic groups: on par with the Democrat-Republican divide on climate change. Notably, this misalignment persists even after explicitly steering the LMs towards particular demographic groups. Our analysis not only confirms prior observations about the left-leaning tendencies of some human feedback-tuned LMs, but also surfaces groups whose opinions are poorly reflected by current LMs (e.g., 65+ and widowed individuals). Our code and data are available at https://github.com/tatsu-lab/opinions_qa.

## Authors

[[Shibani Santurkar]], [[Esin Durmus]], [[Faisal Ladhak]], [[Cinoo Lee]], [[Percy Liang]], [[Tatsunori Hashimoto]]

## Data Description

The paper introduces OpinionQA, a dataset of 1,498 multiple-choice questions from Pew Research's American Trends Panels spanning 23 topics (abortion, automation, climate change, guns, etc.) with human opinion distributions from 60 US demographic groups. Nine LMs were evaluated (350M to 178B parameters from OpenAI and AI21 Labs), including base models (ada, davinci, j1-grande, j1-jumbo) and human feedback-tuned models (text-davinci-001/002/003, j1-grande-v2-beta), measuring representativeness, steerability, and consistency of LM opinions against human survey responses.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computers-and-Society #Computer-Science---Machine-Learning #Computer-Science---Computation-and-Language

## Citation Info

493 citations (Semantic Scholar/arXiv) [2025-08-27]
