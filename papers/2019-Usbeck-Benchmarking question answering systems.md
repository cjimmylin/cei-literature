---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: SJDZ8FST
type: journalArticle
short_title: "Benchmarking question answering systems"
year: 2025
first_author: "[[Ricardo Usbeck]]"
last_author: "[[Christina Unger]]"
authors: "Ricardo Usbeck; Michael Röder; Michael Hoffmann; Felix Conrads; Jonathan Huthmann; Axel-Cyrille Ngonga-Ngomo; Christian Demmler; Christina Unger"
doi: 10.3233/SW-180312
url: "https://journals.sagepub.com/doi/full/10.3233/SW-180312"
external_pdf: "file:///Users/jimmylin/Zotero/storage/76ZVQIXB/Usbeck et al. - 2019 - Benchmarking question answering systems.pdf"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
tags: 
abstract: "The need for making the Semantic Web better accessible for lay users and the uptake of interactive systems and smart assistants for the Web have spawned a new generation of RDF-based question answering systems. However, the fair evaluation of these systems remains a challenge due to the different type of answers that they provide. Hence, repeating current published experiments or even benchmarking on the same datasets remains a complex and time-consuming task."
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Question Answering"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark annotated dataset for question answering"
data_metrics: "Not specified"
LLM_assessed: NA
DATA_URL: "https://github.com/AKSW/NLIWOD"
pdf_extract: "PDF Extracts/2019/2019-Usbeck-Benchmarking question answering systems.md"
local_pdf: "[[PDFs/2019/2019-Usbeck-Benchmarking question answering systems.pdf]]"
---
# Benchmarking question answering systems

## Metadata

**Authors:** Usbeck, Ricardo; Röder, Michael; Hoffmann, Michael; Conrads, Felix; Huthmann, Jonathan; Ngonga-Ngomo, Axel-Cyrille; Demmler, Christian; Unger, Christina

**Year:** 2019

**Publication:** Semantic Web

**Type:** journalArticle

**DOI:** [10.3233/SW-180312](https://doi.org/10.3233/SW-180312)

**Pages:** 293-304

**Volume/Issue:** Vol. 10, Issue 2

## Links

- **URL:** https://journals.sagepub.com/doi/full/10.3233/SW-180312
- **DOI:** https://doi.org/10.3233/SW-180312

## Abstract

The need for making the Semantic Web better accessible for lay users and the uptake of interactive systems and smart assistants for the Web have spawned a new generation of RDF-based question answering systems. However, the fair evaluation of these systems remains a challenge due to the different type of answers that they provide. Hence, repeating current published experiments or even benchmarking on the same datasets remains a complex and time-consuming task.

## Authors

[[Ricardo Usbeck]], [[Michael Röder]], [[Michael Hoffmann]], [[Felix Conrads]], [[Jonathan Huthmann]], [[Axel-Cyrille Ngonga-Ngomo]], [[Christian Demmler]], [[Christina Unger]]

## Detailed Summary

This paper presents GERBIL QA, a novel online benchmarking platform for question answering systems that relies on FAIR principles (Findable, Accessible, Interoperable, Reusable) to support fine-grained evaluation. The platform addresses critical drawbacks in existing QA evaluation campaigns: lack of standardized datasets, absence of reference implementations for comparison, and unfair evaluation across different knowledge base URIs and URLs.

GERBIL QA builds upon the successful GERBIL framework for Named Entity Recognition while providing novel components specifically designed for QA evaluation. The platform supports 22 question answering datasets (QALD-1 through QALD-6 and NLQ), integrates 6 existing QA systems, implements 7 evaluation metrics, and offers 6 novel sub-experiment types for fine-grained component analysis. The system supports both online webservice-based systems and file-based evaluation, enabling continuous benchmarking and diagnostics for QA development.

## Paper Outline

1. Introduction - Motivation for standardized QA benchmarking and FAIR principles
2. Question Answering Benchmarking Campaigns - Review of TREC, CLEF, BioASQ, OKBQA, and QALD
3. Datasets - Description of 22 supported datasets with metadata and versioning
4. Systems - Overview of 6 integrated QA systems (HAWK, SINA, YodaQA, QAKiS, QANARY, OKBQA)
5. Experiment Evaluation - 6 experiment types, 7 metrics, and answer matching strategies
6. Sustainability Plan and Community - Long-term maintenance and W3C integration
7. Conclusion and Future Work - Planned extensions and standardization efforts

## Methods Summary

The platform implements five sub-experiment types beyond standard QA evaluation: C2KB (resource identification), P2KB (property identification), RE2KB (relation/triple extraction), AT (answer type classification), and AIT2KB (answer item type identification). The evaluation uses micro/macro precision, recall, and F-measure, with novel matching strategies that handle equivalent URIs through owl:sameAs transitive closures. The eQALD-JSON format extends QALD to include annotations, confidence scores, and schemaless queries for comprehensive evaluation.

## Results Summary

At time of publication, GERBIL QA had processed 85 experiments with over 940 sub-experiment executions. The platform demonstrated that many existing QA systems from past challenges lack webservices or detailed documentation, limiting benchmarking possibilities. Analysis showed that systems like HAWK performed differently across hybrid vs. multilingual questions, and sub-experiments revealed that systems achieving similar overall scores could have vastly different component-level performance (e.g., entity detection vs. SPARQL generation).

## Conclusions

GERBIL QA provides the first online benchmarking platform for factoid question answering with citable, comparable experiments. The platform enables researchers to identify specific weaknesses in QA pipelines through component-level analysis. The authors plan to add hierarchical F-measures, novel datasets, and expand to non-factoid QA. The platform will be integrated with the H2020 HOBBIT project and W3C Natural Language Interfaces community group.

## Artifact Contributions

- GERBIL QA Platform: http://gerbil-qa.aksw.org/gerbil/
- 22 curated QA datasets (QALD-1 to QALD-6, NLQ)
- 6 integrated QA systems with webservice interfaces
- eQALD-JSON format specification for comprehensive QA evaluation
- Source code: https://github.com/AKSW/gerbil (QuestionAnswering branch)
- SPARQL endpoint for experimental metadata: http://gerbil-qa.aksw.org/sparql

## Data Description

The paper presents GERBIL QA, an online benchmarking platform for question answering systems over Linked Data. It includes 22 question answering datasets (QALD-1 through QALD-6 and NLQ) totaling 1,431 questions, along with 6 integrated QA systems (HAWK, SINA, YodaQA, QAKIS, QANARY, OKBQA). The platform evaluates traditional QA systems using 7 metrics across 6 experiment types but does not assess any LLMs.


## Notes


## Citation Info

61 citations (Semantic Scholar/DOI) [2025-08-27] 61 citations (Semantic Scholar/DOI) [2025-08-23] 20 citations (Crossref/DOI) [2025-08-23]
