---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: YCTS2U3I
type: conferencePaper
short_title: CIVICS
year: 2024
first_author: "[[Giada Pistilli]]"
last_author: "[[Margaret Mitchell]]"
authors: "Giada Pistilli; Alina Leidinger; Yacine Jernite; Atoosa Kasirzadeh; Alexandra Sasha Luccioni; Margaret Mitchell"
doi: 10.1609/aies.v7i1.31710
url: "https://ojs.aaai.org/index.php/AIES/article/view/31710"
external_pdf: "file:///Users/jimmylin/Zotero/storage/4LU2FNH5/Pistilli et al. - 2024 - CIVICS Building a Dataset for Examining Culturally-Informed Values in Large Language Models.pdf"
national_ethnic_cultural: Multicultural/Cross-cultural
cultures_nationalities_list: Multicultural/Cross-cultural
languages_list: "English, French, German, Italian, Turkish"
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
mp_schwartz: 50
mp_trolley: 50
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "Value Pluralism / Schwartz, Trolley / Dilemmas (Psych)"
newtags: "General Ethics"
key_contribution: "Introduced CIVICS, a multilingual dataset of value-laden prompts on sensitive topics (LGBTQI+, welfare, etc.) to examine culturally-informed values in LLMs."
significance: "Reveals the implicit value variability in models across languages and topics, showing that refusals and responses are disparately triggered depending on the cultural context of the prompt."
tags: 
abstract: "This paper introduces the “CIVICS: Culturally-Informed & Values-Inclusive Corpus for Societal impacts” dataset, designed to evaluate the social and cultural variation of Large Language Models (LLMs) across multiple languages and value-sensitive topics. We create a hand-crafted, multilingual dataset of value-laden prompts which address specific socially sensitive topics, including LGBTQI rights, social welfare, immigration, disability rights, and surrogacy."
CONF-CC: "Proceedings of the AAAI/ACM Conference on AI Ethics and Society"
DATE_ADDED: 20260208
LLM_assessed: "Command-R, DeepSeek, Gemma, Llama-3, Mistral, Qwen-1.5"
DATA_URL: "https://huggingface.co/CIVICS-dataset"
pdf_extract: "PDF Extracts/2024/2024-Pistilli-CIVICS.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2024/2024-Pistilli-CIVICS.pdf]]"
CONFERENCE: "AAAI 2024"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 10
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "General Ethics"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: US
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: No
is_eval: No
is_dataset: Yes
data_description: Dataset
data_metrics: "Not specified"
---
# CIVICS: Building a Dataset for Examining Culturally-Informed Values in Large Language Models

## Metadata

**Authors:** Pistilli, Giada; Leidinger, Alina; Jernite, Yacine; Kasirzadeh, Atoosa; Luccioni, Alexandra Sasha; Mitchell, Margaret

**Year:** 2024

**Publication:** Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society (AIES)

**Type:** conferencePaper

**DOI:** [10.1609/aies.v7i1.31710](https://doi.org/10.1609/aies.v7i1.31710)

**Pages:** 1132–1144

## Links

- **URL:** https://ojs.aaai.org/index.php/AIES/article/view/31710
- **DOI:** https://doi.org/10.1609/aies.v7i1.31710

## Abstract

This paper introduces the \

## Authors

[[Giada Pistilli]], [[Alina Leidinger]], [[Yacine Jernite]], [[Atoosa Kasirzadeh]], [[Alexandra Sasha Luccioni]], [[Margaret Mitchell]]

## Detailed Summary

This paper introduces CIVICS (Culturally-Informed and Values-Inclusive Corpus for Societal impacts), a hand-crafted multilingual dataset designed to evaluate social and cultural variation in Large Language Models across multiple languages and value-sensitive topics. The dataset addresses LGBTQI rights, social welfare, immigration, disability rights, and surrogacy - topics chosen for their direct relevance to pressing socio-political issues across different regions.

CIVICS spans five languages and nine national contexts: German (Germany), Italian (Italy), French (France and Canada), English (Australia, Canada, UK, Singapore), and Turkish (Turkey). Unlike prior work using machine translation, all samples were collected by native speakers from official documents (government bodies, civil rights societies, news agencies), ensuring cultural and linguistic authenticity. The 699 prompts were manually annotated with finer-grained topic labels by five annotators through an iterative adjudication process.

The authors conducted two experimental setups to demonstrate the dataset utility. The first used log-probabilities to assess LLM agreement with CIVICS statements. The second examined long-form responses, finding that refusals are triggered disparately across models but consistently and more frequently in English or translated statements. Specific topics (immigration, LGBTQI rights, social welfare) and sources lead to more pronounced differences across model answers. The work highlights the implicit value variability in models across languages and topics.

## Paper Outline

1. Introduction - Initial motivation and contributions
2. Related Work - Cultural values in LLMs, language and values
3. CIVICS: Collection and Methodology - Data selection, prompt sources
4. Annotation Process - Annotator demographics, protocol, stages
5. Experiments
   5.1 Log-probability Setup
   5.2 Long-form Response Setup
6. Discussion and Limitations
7. Conclusion

## Methods Summary

Dataset construction: (1) Manual collection by native speakers from official sources, (2) Five languages, nine national contexts, 699 prompts, (3) Iterative annotation with five annotators through adjudication. Experiments: (1) Log-probability evaluation of LLM agreement with statements, (2) Long-form response analysis examining model outputs across languages and topics, (3) Analysis of refusal patterns across models, languages, and topics. Models evaluated include open-weight LLMs. The methodology emphasizes reproducibility and adaptability for extending to additional languages and cultural contexts.

## Results Summary

Key findings: (1) Refusals are triggered disparately across models but consistently more frequently in English or translated statements, (2) Specific topics lead to more pronounced differences - particularly immigration, LGBTQI rights, and social welfare, (3) Model responses show social and cultural variability across languages, (4) Different sources (government, civil society, news) elicit different model behaviors, (5) Log-probability experiments reveal implicit value stances in model predictions. The experiments demonstrate that CIVICS effectively captures value variation across linguistic and cultural contexts.

## Conclusions

The authors conclude that CIVICS serves as a tool for future research on LLM value variation across cultures and languages. Key contributions include: (1) First manually curated dataset on ethically-laden topics spanning five languages and nine national contexts, (2) Demonstration that refusal patterns and value expressions vary by language and topic, (3) Framework for reproducible, culturally-informed dataset curation. Limitations include the Western-centric annotator demographics and limited language coverage. Future work should expand to broader linguistic and cultural contexts.

## Artifact Contributions

- CIVICS Dataset: 699 hand-crafted multilingual prompts across five languages and nine national contexts
- Available at: https://huggingface.co/CIVICS-dataset
- Open licenses promised upon publication

## Data Description

Releases the CIVICS (Culturally-Informed & Values-Inclusive Corpus for Societal impacts) dataset: a hand-crafted, multilingual collection of 699 value-laden prompts across five languages and nine national contexts, covering LGBTQI rights, social welfare, immigration, disability rights, and surrogacy.


## Notes


## Tags

#Computer-Science---Artificial-Intelligence #Computer-Science---Computation-and-Language
