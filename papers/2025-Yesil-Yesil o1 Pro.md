---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: S63G97EK
type: journalArticle
short_title: "Yesil o1 Pro"
year: 2025
first_author: "[[Yusuf Yesil]]"
last_author: "[[Yusuf Yesil]]"
authors: "Yusuf Yesil"
doi: 10.2196/preprints.72646
url: "https://preprints.jmir.org/preprint/72646"
external_pdf: "file:///Users/jimmylin/Zotero/storage/7B3HX5KJ/Yesil - 2025 - Yesil o1 Pro Evidence-Based AI Model for Health and Benchmarking in Clinical Decision Support.pdf"
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: 
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
key_contribution: "Describes a specialized medical model 'Yesil o1 Pro' for clinical decision support."
significance: "Represents the trend of specialized 'Pro' models for high-stakes domains like healthcare, likely emphasizing evidence-based grounding."
tags: 
research_topic: Other
abstract: "Background: Integrating evidence-based approaches in healthcare and artificial intelligence (AI) is crucial for enhancing clinical decision-making and patient safety. Yesil o1 Pro is a specialized large language model (LLM) designed to transform medical knowledge synthesis by leveraging a comprehensive, curated database of scientific literature, clinical guidelines, and medical textbooks. Objective: The system's innovative 'AI Hospital' framework employs domain-specific expert agents..."
CONF-CC: N/A
DATE_ADDED: 20260208
LLM_assessed: "Claude, DeepSeek, GPT-4o, GPT-o1, Gemini, Llama-3"
DATA_URL: "https://huggingface.co/datasets/yesilhealth/Health_Benchmarks"
pdf_extract: "PDF Extracts/2025/2025-Yesil-Yesil o1 Pro.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Yesil-Yesil o1 Pro.pdf]]"
CONFERENCE: Journal
ethics_overall: No
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 10
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Applied Ethics"
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
is_benchmark: Yes
is_eval: No
is_dataset: Yes
data_description: "Benchmark for ai safety dataset"
data_metrics: "Not specified"
---
# Yesil o1 Pro: Evidence-Based AI Model for Health and Benchmarking in Clinical Decision Support

## Metadata

**Authors:** Yesil, Yusuf

**Year:** 2025

**Publication:** JMIR Preprints

**Type:** journalArticle

**DOI:** [10.2196/preprints.72646](https://doi.org/10.2196/preprints.72646)

## Links

- **URL:** https://preprints.jmir.org/preprint/72646
- **DOI:** https://doi.org/10.2196/preprints.72646

## Abstract

BACKGROUND                         Integrating evidence-based approaches in healthcare and artificial intelligence (AI) is crucial for enhancing clinical decision-making and patient safety. Yesil o1 Pro is a specialized large language model (LLM) designed to transform medical knowledge synthesis by leveraging a comprehensive, curated database of scientific literature, clinical guidelines, and medical textbooks.                                                                       OBJECTIVE                         The system's innovative \

## Authors

[[Yusuf Yesil]]

## Detailed Summary

This preprint introduces Yesil o1 Pro, a specialized large language model designed for clinical decision support in healthcare. The system is built around an innovative "AI Hospital" framework that employs multiple domain-specific expert agents coordinated by a central Master Agent, enabling tailored responses across 40+ medical specialties including cardiology, oncology, pediatrics, psychiatry, and emergency medicine. The model is trained on a massive curated database comprising 100.5M words from high-impact journals, 96.8M words from core medical textbooks, 74.4M words from international standards, and additional content from clinical guidelines, protocols, and meta-analyses.

The technical architecture incorporates several advanced methodologies. LightRAG (a variant of Microsoft's GraphRAG) is customized for clinical applications, enabling efficient retrieval through specialized entity extraction for medical terminology, recognition of clinical parameters and biomarkers, and dual-level retrieval systems. The model was fine-tuned on 1.5 million question-answer pairs generated from the medical literature and employs Chain of Thought (CoT) reasoning to enhance its diagnostic and treatment recommendation capabilities.

Benchmark evaluations demonstrate strong performance, with Yesil o1 Pro achieving 89.1% overall accuracy compared to GPT-4o (83.9%) and Claude 3.5 Sonnet (83.0%). Domain-specific accuracies are particularly impressive in areas like Mental Health (96.1%), Epidemiology (94.6%), and Dentistry (94.6%). However, as an unpublished preprint, these results have not yet been peer-reviewed.

## Paper Outline

1. Abstract - Overview of Yesil o1 Pro and key claims
2. Introduction - Background on AI in healthcare and limitations of general LLMs
3. Methods
   - Dataset Development and Curation
   - GraphRAG for Clinical Applications
   - AI Hospital Framework - Multi-agent specialist system design
   - Fine-tuning Process
4. Results - Benchmark Evaluations and domain-specific performance
5. Discussion - Applications, limitations, and future directions
6. Supplementary Materials

## Methods Summary

The model's foundation is a curated dataset totaling over 600 million words from diverse authoritative medical sources. GraphRAG was customized with specialized entity extraction for medical terminology, clinical parameter recognition, relationship mapping between symptoms/diseases/treatments, dual-level retrieval (local and global), context-aware search, and real-time confidence scoring. The AI Hospital framework creates specialty-specific expert agents (each with thousands of entities and relationships) coordinated by a Master Agent. Fine-tuning used 1.5 million Q&A pairs with Chain of Thought reasoning.

## Results Summary

Benchmark evaluations compared Yesil o1 Pro against GPT-4o, Claude 3.5 Sonnet, and other models across multiple medical domains. Overall accuracy was 89.1% versus 83.9% (GPT-4o) and 83.0% (Claude 3.5). Highest-performing domains included Mental Health (96.1%), Epidemiology (94.6%), and Dentistry (94.6%). The system demonstrated ability to provide cross-specialty consultations and explain its reasoning transparently.

## Conclusions

Yesil o1 Pro represents an advancement in AI-driven healthcare support through its evidence-based, multi-specialty architecture. The AI Hospital framework with coordinated expert agents offers a promising approach for handling complex clinical queries. Key applications include clinical decision support, professional education, interdisciplinary collaboration, and medical research assistance. Challenges remain in real-world clinical integration and maintaining currency with evolving medical knowledge.

## Artifact Contributions

- Yesil o1 Pro model (availability not specified)
- Medical knowledge base with 40+ specialty-specific knowledge graphs
- Benchmark evaluation framework for medical AI models

## Data Description

A proprietary healthcare benchmarking dataset spanning 50+ medical specialties used to evaluate Yesil o1 Pro against other LLMs; the dataset is stated to be freely accessible to the public for benchmarking medical language models.


## Notes

