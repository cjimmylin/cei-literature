---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0510
type: preprint
short_title: "An Empirical Investigation of Gender Stereotype Representation in Large Language Models: The Italian Case"
year: 2025
first_author: "[[Giachino, Gioele]]"
last_author: "[[Martin, Juan Carlos De]]"
authors: "Giachino, Gioele; Rondina, Marco; Vetrò, Antonio; Coppola, Riccardo; Martin, Juan Carlos De"
authors_incomplete: false
url: "https://arxiv.org/abs/2507.19156"
external_pdf: "https://arxiv.org/pdf/2507.19156.pdf"
publication: arXiv
CONF-CC: Preprint
pdf_extract: "PDF Extracts/2025/2025-Giachino-An Empirical Investigation of Gender Stereotype Representation in.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Giachino-An Empirical Investigation of Gender Stereotype Representation in.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: Italian
cultures_nationalities_list: Italian
languages_list: Italian
religious_values: N/A
rv_islam: 0
rv_christianity: 0
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 0
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: N/A
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
newtags: 
LLM_assessed: "GPT-4o mini, Gemini"
DATA_URL: "https://anonymous.4open.science/r/GenderStereotypeLLMsItalian-47F6/"
tags: 
abstract: "The increasing use of Large Language Models (LLMs) in a large variety of domains has sparked worries about how easily they can perpetuate stereotypes and contribute to the generation of biased content. With a focus on gender and professional bias, this work examines in which manner LLMs shape responses to ungendered prompts, contributing to biased outputs. This analysis uses a structured experimental method, giving different prompts involving three different professional job combinations, which..."
CONFERENCE: Preprint
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Bias & Fairness"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: IT
author_region: "Western Europe"
author_global_north_south: "Global North"
weird_score: 69
is_benchmark: No
is_eval: No
is_dataset: No
data_description: N/A
data_metrics: "Not specified"
---
# An Empirical Investigation of Gender Stereotype Representation in Large Language Models: The Italian Case

## Authors

[[Giachino, Gioele]], [[Rondina, Marco]], [[Vetrò, Antonio]], [[Coppola, Riccardo]], [[Martin, Juan Carlos De]]

## Metadata

**Authors:** Giachino, Gioele; Rondina, Marco; Vetrò, Antonio; Coppola, Riccardo; Martin, Juan Carlos De

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** Italian

## Links

- **arXiv:** https://arxiv.org/abs/2507.19156

## Abstract

Examines how LLMs shape responses to ungendered Italian prompts, contributing to biased outputs. Focuses on gender and professional bias. Results show Gemini associated 100% of 'she' pronouns with 'assistant' rather than 'manager'. Highlights how Italian grammatical gender amplifies stereotypes.

## Summary

This empirical study examines gender and professional bias in LLM responses to ungendered Italian prompts, leveraging Italian's extensive grammatical gender system to highlight bias amplification. The authors test GPT-4o-mini and Gemini-1.5-flash using structured prompts involving three professional job combinations with hierarchical relationships, collecting 3,600 responses via API. Results reveal severe gender stereotyping, with Gemini associating 100% of female pronouns with 'assistant' rather than 'manager', and ChatGPT showing 97% of the same pattern, demonstrating how LLMs perpetuate stereotypes in gendered languages.

## Data Description

3,600 responses collected from GPT-4o mini and Gemini Flash to 60 Italian ungendered professional prompts, analyzed via conditional probability metrics for gender bias.


## Detailed Summary

This paper examines gender and professional bias in LLM-generated text in Italian, a language with extensive grammatical gender differences that amplify the challenge of producing objective, unbiased content. The study uses a structured experimental method inspired by the WinoBias benchmark, presenting two popular LLM-based chatbots -- OpenAI ChatGPT (gpt-4o-mini) and Google Gemini (gemini-1.5-flash) -- with ungendered Italian prompts involving three different professional job combinations characterized by hierarchical relationships (e.g., manager/assistant, doctor/nurse, professor/secretary).

Through API collection of 3,600 responses, the authors quantify stereotypes using conditional probabilities of gendered pronoun assignments to professional roles. The results reveal severe gender stereotyping: Gemini associated 100% of female pronouns ("lei"/she) with the subordinate "assistant" role rather than "manager," while ChatGPT showed 97% of the same pattern. These findings demonstrate how LLMs can perpetuate gender stereotypes in gendered languages, with significant implications for workplaces, job selection processes, and other high-stakes domains. The proprietary nature of the tested models restricts analysis to black-box testing, making it impossible to trace bias to specific training data or architectural choices.

## Paper Outline

1. Introduction - Context and research motivation
2. Background and Related Work - Gender bias in LLMs and non-English contexts
3. Methodology - Research question, procedure, data collection and evaluation
4. Results - Empirical findings on gender associations
5. Discussion - Implications and analysis
6. Limitations
7. Final Remarks

## Methods Summary

The study employs a structured experimental method using the Goal-Question-Metric (GQM) template. Ungendered Italian prompts involving pairs of professional occupations with hierarchical relationships are presented to GPT-4o-mini and Gemini-1.5-flash via their APIs. Three professional job combinations are tested (e.g., manager/assistant). For each combination, 600 responses are collected per model across multiple prompt variations, totaling 3,600 responses. Conditional probabilities are computed to measure the association between gendered pronouns (lui/lei) and professional roles. The methodology draws from the WinoBias benchmark design adapted for Italian's gendered grammar system.

## Results Summary

Both models exhibit severe gender stereotyping in Italian. Gemini-1.5-flash associates 100% of female pronouns with the subordinate "assistant" role rather than "manager," while GPT-4o-mini shows a 97% rate of the same pattern. The bias is consistent across all three professional job combinations tested. Italian's grammatical gender system, where job titles often carry inherent gender markers, amplifies the visibility and impact of these stereotypes compared to less gendered languages. The results indicate that model scale alone is not a remedy for stereotype amplification, as even state-of-the-art models produce heavily biased outputs when interacting in Italian.

## Conclusions

The study raises ethical concerns about deploying LLMs in domains like hiring, education, and public administration where biased outputs could reinforce social inequalities. Limitations include testing only two proprietary models, focusing on a limited set of professional combinations, and the inability to perform white-box analysis due to the closed nature of the models. Future work includes expanding the study to additional chatbots, testing more languages with strong grammatical gender, refining prompt engineering methods, and exploring a larger experimental base.

## Artifact Contributions

No publicly released artifacts identified.

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B8
**Relevance:** Italian-specific study on gender bias in LLMs, leveraging Italian's extensive grammatical gender system to evaluate stereotype propagation.

## Tags

