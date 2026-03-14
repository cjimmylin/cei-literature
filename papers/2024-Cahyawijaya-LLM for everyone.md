---





































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: H9QH2GC6
type: thesis
short_title: "LLM for everyone"
year: 2024
first_author: "[[Samuel Cahyawijaya]]"
last_author: "[[Samuel Cahyawijaya]]"
authors: "Samuel Cahyawijaya"
url: "https://lbezone.hkust.edu.hk/bib/991013340351603412"
external_pdf: "file:///Users/jimmylin/Zotero/storage/XZEW2FQS/Cahyawijaya - 2024 - LLM for everyone  representing the underrepresented in large language models.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "Multilingual"
religious_values: "N/A"
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
religious_values_list: "N/A"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: 
tags: 
research_topic: "Other"
abstract: "Natural language processing (NLP) has witnessed a profound impact of large language models (LLMs) that excel in a multitude of tasks. However, the limitation of LLMs in multilingual settings, particularly in underrepresented languages, remains a significant hurdle. This thesis aims to bridge the gap in NLP research and development by focusing on underrepresented languages. A comprehensive evaluation of LLMs is conducted to assess their capabilities in these languages, revealing the challenges of multilingual and multicultural generalization. The proposed solutions cover cross-lingual continual instruction tuning, retrieval-based cross-lingual in-context learning, and in-context query alignment."
CONF-CC: "N/A"
DATE_ADDED: 20260208
LLM_assessed: "Aya-101, BLOOMZ, Command-R, GPT-3.5, Llama-3, mT0"
DATA_URL: "https://github.com/IndoNLP/nusax"
pdf_extract: "PDF Extracts/2024/2024-Cahyawijaya-LLM for everyone.md"
local_pdf: "[[PDFs/2024/2024-Cahyawijaya-LLM for everyone.pdf]]"
CONFERENCE: "Unknown"
ethics_overall: 45
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "AI Safety & Alignment"
is_benchmark: Yes
is_eval: "Yes"
is_dataset: Yes
data_description: "Evaluation approach"
data_metrics: "Not specified"
---
# LLM for everyone : representing the underrepresented in large language models

## Metadata

**Authors:** Cahyawijaya, Samuel

**Year:** 2024

**Type:** thesis

**Publisher:** The Hong Kong University of Science and Technology

## Links

- **URL:** https://lbezone.hkust.edu.hk/bib/991013340351603412

## Abstract

Natural language processing (NLP) has witnessed a profound impact of large language models (LLMs) that excel in a multitude of tasks. However, the limitation of LLMs in multilingual settings, particularly in underrepresented languages, remains a significant hurdle. This thesis aims to bridge the gap in NLP research and development by focusing on underrepresented languages. A comprehensive evaluation of LLMs is conducted to assess their capabilities in these languages, revealing the challenges of multilingual and multicultural generalization. The proposed solutions cover cross-lingual continual instruction tuning, retrieval-based cross-lingual in-context learning, and in-context query alignment.

## Authors

[[Samuel Cahyawijaya]]

## Detailed Summary

This doctoral thesis addresses the fundamental challenge that large language models, despite their impressive capabilities, perform poorly on underrepresented languages. Using Indonesia as a primary case study (a country with 700+ languages), the research systematically evaluates LLM performance across both the national language (Indonesian) and indigenous local languages. The thesis reveals significant disparities in model capabilities when applied to underrepresented languages, demonstrating that current multilingual models fail to generalize effectively across diverse linguistic and cultural contexts.

The research introduces several methodological contributions for improving LLM performance in underrepresented languages. The "Instruct-Align" approach uses continual cross-lingual instruction tuning to adapt models to new languages without catastrophic forgetting. The thesis also presents retrieval-based cross-lingual in-context learning methods that leverage semantic and translation-based retrieval to improve few-shot performance. Additionally, the work introduces UniVaR (Universal Value Representation), a framework for understanding multicultural value alignment in LLMs by learning multi-view value embeddings that capture cultural variations across languages.

A key finding is that scaling laws observed in high-resource languages do not necessarily apply to underrepresented languages - simply increasing model size does not proportionally improve performance. The research also highlights cultural evaluation gaps, showing that LLMs often fail to capture culturally-specific knowledge and values. The thesis provides practical solutions including in-context query alignment techniques and demonstrates that smaller models can achieve competitive performance with larger ones through targeted adaptation strategies, making LLM capabilities more accessible for underrepresented language communities.

## Paper Outline

1. Introduction - Motivation and research problems
2. Background and Preliminaries - Cross-lingual alignment, transformers, pre-trained LMs
3. Large Language Models Evaluation in Underrepresented Languages
   - Indonesia case study (700+ languages)
   - Evaluation across Indonesian national language and local languages
   - Analysis of scaling law applicability and cultural evaluation
4. Multicultural Value Alignment in Large Language Models
   - UniVaR framework for universal value representation
   - Multi-view value embedding learning
   - Cross-cultural value map analysis
5. Underrepresented Languages Adaptation in Large Language Models
   - Continual cross-lingual instruction tuning (Instruct-Align)
   - Language adaptation through in-context learning
   - Retrieval-based cross-lingual methods
6. Conclusion - Remarks, limitations, and future work

## Methods Summary

The thesis employs multiple methodological approaches: (1) Comprehensive LLM evaluation across Indonesian national language and 10+ local indigenous languages using NLU and NLG benchmarks; (2) UniVaR framework using value-eliciting question-answering to generate training data, then learning multi-view value embeddings through contrastive learning; (3) Instruct-Align for continual cross-lingual instruction tuning with replay mechanisms to prevent catastrophic forgetting; (4) Cross-lingual in-context learning using both semantic similarity retrieval and translation-based retrieval; (5) In-context label alignment and query alignment techniques for improved few-shot learning; (6) Human annotation studies for response quality evaluation; (7) Cultural evaluation through probing tasks.

## Results Summary

Key results include: (1) LLMs show significant performance degradation on local indigenous languages compared to Indonesian national language (10-40% drops across tasks); (2) Scaling laws do not hold for underrepresented languages - larger models show diminishing returns; (3) LLM response quality in underrepresented languages rated significantly lower by human annotators; (4) Cultural evaluation reveals poor performance on culturally-specific knowledge; (5) UniVaR successfully captures cultural clusters in value representation maps, with representations correlating with known cultural dimensions; (6) Instruct-Align improves performance on target languages while mitigating catastrophic forgetting (using 1-5% replay samples); (7) Cross-lingual in-context learning with semantic retrieval outperforms random sampling by 5-15%; (8) In-context query alignment provides consistent improvements across diverse language families.

## Conclusions

The thesis concludes that current LLMs are not truly "for everyone" due to systematic underrepresentation of low-resource languages and cultures. However, the research demonstrates that targeted adaptation strategies can significantly improve accessibility. Key recommendations include: (1) Developing language-specific benchmarks for underrepresented languages; (2) Incorporating cultural evaluation alongside linguistic evaluation; (3) Using continual learning approaches for language adaptation; (4) Leveraging in-context learning with carefully designed retrieval strategies; (5) Understanding and respecting multicultural value variations in alignment processes. The thesis calls for a more inclusive approach to LLM development that explicitly addresses the needs of underrepresented language communities.

## Artifact Contributions

- UniVaR (Universal Value Representation) framework for multicultural value alignment
- Instruct-Align methodology for continual cross-lingual instruction tuning
- Evaluation benchmarks for Indonesian and local indigenous languages
- Cross-lingual in-context learning retrieval methods (semantic and translation-based)
- In-context label alignment and query alignment techniques
- Datasets for value-eliciting QA in multiple languages

## Data Description

PhD thesis developing evaluation suites and benchmarks for underrepresented languages, testing six LLMs on Indonesian and local indigenous language tasks including NLU and generation.


## Notes

