---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 3RNRAN7W
type: journalArticle
year: 2025
short_title: "ETHICS WHITEPAPER"
first_author: "[[Eddie L Ungless]]"
last_author: "[[Alexandra Birch]]"
authors: "Eddie L Ungless; Nikolas Vitsakis; Zeerak Talat; James Garforth; Björn Ross; Arno Onken; Atoosa Kasirzadeh; Alexandra Birch"
external_pdf: "file:///Users/jimmylin/Zotero/storage/X4AQDWVV/Ungless et al. - ETHICS WHITEPAPER Whitepaper on Ethical Research into Large Language Models.pdf"
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: 
religious_values: "Indigenous Spirituality"
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
rv_indigenous: 50
religious_values_list: "Indigenous Spirituality"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: N/A
newtags: "General Ethics"
key_contribution: "Published a comprehensive whitepaper detailing best practices and ethical considerations for research into and with Large Language Models."
significance: "Serves as a practical guide for researchers/industry to navigate the ethical landscape of LLM development, addressing issues from data procurement to deployment impact."
tags: 
abstract: "There is a significant body of work looking at the ethical considerations of large language models (LLMs): critiquing tools to measure performance and harms; proposing toolkits to aid in ideation; discussing the risks to workers; considering legislation around privacy and security etc. As yet there is no work that integrates these resources into a single practical guide that focuses on LLMs; we attempt this ambitious goal."
CONF-CC: N/A
DATE_ADDED: 20260208
LLM_assessed: NA
DATA_URL: "https://github.com/MxEddie/Ethics-Whitepaper"
pdf_extract: "PDF Extracts/2024/2024-Ungless-ETHICS WHITEPAPER.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2024/2024-Ungless-ETHICS WHITEPAPER.pdf]]"
CONFERENCE: Journal
ethics_overall: No
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Privacy & Data Ethics"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 50
nw_buen_vivir: 0
author_country: US
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 80
is_benchmark: No
is_eval: No
is_dataset: No
data_description: N/A
data_metrics: "Not specified"
---
# ETHICS WHITEPAPER: Whitepaper on Ethical Research into Large Language Models

## Metadata

**Authors:** Ungless, Eddie L; Vitsakis, Nikolas; Talat, Zeerak; Garforth, James; Ross, Björn; Onken, Arno; Kasirzadeh, Atoosa; Birch, Alexandra

**Type:** journalArticle

## Links

- **Arxiv:** https://arxiv.org/abs/2410.19812
- **Github:** https://github.com/MxEddie/Ethics-Whitepaper

## Abstract

This whitepaper offers an overview of the ethical considerations surrounding research into or with large language models (LLMs). As LLMs become more integrated into widely used applications, their societal impact increases, bringing important ethical questions to the forefront. With a growing body of work examining the ethical development, deployment, and use of LLMs, this whitepaper provides a comprehensive and practical guide to best practices, designed to help those in research and in industry to uphold the highest ethical standards in their work.

## Authors

[[Eddie L Ungless]], [[Nikolas Vitsakis]], [[Zeerak Talat]], [[James Garforth]], [[Björn Ross]], [[Arno Onken]], [[Atoosa Kasirzadeh]], [[Alexandra Birch]]

## Detailed Summary

This comprehensive whitepaper from researchers at the University of Edinburgh and Heriot-Watt University provides a practical guide to ethical research with Large Language Models (LLMs). The authors synthesize existing frameworks (NIST AI RMF, EU AI Act, NeurIPS Ethics Guidelines, ACL Ethics Checklist) into actionable "Do's and Don'ts" organized around a simplified project lifecycle. The work addresses a gap between broad AI frameworks and the specific needs of LLM practitioners.

The paper covers ethics at every stage of the project lifecycle: project start (stakeholder engagement, environmental considerations), data compilation (consent, privacy, documentation), data preparation (filtering biases, crowdworker treatment), model development (design choices affecting fairness, alignment), evaluation (benchmark limitations, harm measurement), and deployment (dual use, guardrails, human replacement). Each section provides concrete recommendations drawn from an extensive literature review of the ACL Anthology and Semantic Scholar.

The significance lies in its practical focus: rather than abstract principles, it offers specific checklists, toolkits, and citations for researchers facing ethical decisions in their daily work with LLMs.

## Paper Outline

1. Introduction - LLM risks and existing frameworks
2. Methodology - Systematic literature review approach
3. Project Start - Ethics review, stakeholder identification, energy consumption
4. Data Compilation - Collection ethics, consent, documentation
5. Data Preparation - Filtering, annotation, crowdworker treatment
6. Model Development + Selection - Design choices, debiasing, alignment
7. Evaluation - Performance metrics, harm evaluation, benchmarks
8. Deployment - Dual use, guardrails, dissemination
9. Limitations and Future Directions
10. Conclusion

## Methods Summary

The authors conducted a systematic literature review of the ACL Anthology, searching for abstracts containing ethics-related terms (ethical, harms, fair, risks) and framework-related terms (toolkit, guidelines, framework). They also searched Semantic Scholar and incorporated resources from an EACL 2023 tutorial on NLP ethics. Papers were manually reviewed for relevance and categorized by project lifecycle stage. Themes were identified using a bottom-up approach and refined through author discussion.

## Results Summary

The paper produces structured "Do's and Don'ts" for each lifecycle stage. Key recommendations include: engage affected communities from project start; consider power relations between stakeholders; create internal audit procedures; use compressed models to minimize energy impact; carefully reflect on data filtering exclusions; treat crowdworkers as human participants requiring ethics approval; test for harm on deployed models (not pre-compression versions); maintain vigilance on alignment throughout pipelines; use alternatives to benchmarks like audits and red teaming; integrate watermarking into generative models; and conduct pre-release audits.

## Conclusions

The authors emphasize that ethical considerations cannot be outsourced to post-hoc review or pre-packaged toolkits. They acknowledge limitations including English-language focus and Western moral perspective, and commit to maintaining the whitepaper as a living document on GitHub. Future work will integrate non-English, non-Western, and non-text resources.

## Artifact Contributions

- **LLM Ethics Whitepaper**: A comprehensive living document hosted on GitHub (https://github.com/MxEddie/Ethics-Whitepaper)
- **Do's and Don'ts Checklists**: Actionable recommendations for each project lifecycle stage

## Data Description

This paper does not introduce or utilize a specific dataset or benchmark for LLM assessment. It is a practical ethics guide for NLP practitioners working with LLMs, structured around a project lifecycle and distilling an extensive literature review into actionable Do's and Don'ts recommendations covering data preparation, model development, evaluation, and deployment.


## Notes

