---

Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: BALGR5YY
type: conferencePaper
short_title: "The Moral Integrity Corpus"
year: 2025
first_author: "[[Caleb Ziems]]"
last_author: "[[Diyi Yang]]"
authors: "Caleb Ziems; Jane Yu; Yi-Chia Wang; Alon Halevy; Diyi Yang"
doi: 10.18653/v1/2022.acl-long.261
url: "https://aclanthology.org/2022.acl-long.261/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/S8U8PDKM/Ziems et al. - 2022 - The Moral Integrity Corpus A Benchmark for Ethical Dialogue Systems.pdf"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "General Ethics"
key_contribution: "Released the Moral Integrity Corpus (MIC), containing 38k prompt-reply pairs and 99k 'Rules of Thumb' (RoTs) that explicitly explicate the moral assumptions of chatbot responses."
significance: "Enables 'moral transparency' in dialogue systems, allowing models to generate not just a response but also the underlying moral principle (RoT) justifying it, facilitating better control and evaluation."
tags: 
abstract: "' Content Warning: some examples in this paper may be offensive or upsetting. Conversational agents have come increasingly closer to human competence in open-domain dialogue settings; however, such models can reﬂect insensitive, hurtful, or entirely incoherent viewpoints that erode a user’s trust in the moral integrity of the system. Moral deviations are difﬁcult to mitigate because moral judgments are not universal, and there may be multiple competing judgments that apply to a situation..."
pdf: "http://arxiv.org/pdf/2204.03021"
pdf_extract: "PDF Extracts/2022/2022-Ziems-The Moral Integrity Corpus.md"
local_pdf: "[[PDFs/2022/2022-Ziems-The Moral Integrity Corpus.pdf]]"
publication: "ACL 2022"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Toxicity & Hate Speech"
is_benchmark: "Yes"
is_eval: "No"
is_dataset: "Yes"
data_description: "Benchmark for moral/ethical reasoning text corpus for conversational ai"
data_metrics: "Not specified"
LLM_assessed: "GPT-2, T5, BART, BERT, ALBERT"
DATA_URL: "https://github.com/GT-SALT/mic"
---
# The Moral Integrity Corpus: A Benchmark for Ethical Dialogue Systems

## Metadata

**Authors:** Ziems, Caleb; Yu, Jane; Wang, Yi-Chia; Halevy, Alon; Yang, Diyi

**Year:** 2022

**Publication:** Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)

**Type:** conferencePaper

**DOI:** [10.18653/v1/2022.acl-long.261](https://doi.org/10.18653/v1/2022.acl-long.261)

**Pages:** 3755-3773

**Publisher:** Association for Computational Linguistics

## Links

- **ACL Anthology:** https://aclanthology.org/2022.acl-long.261
- **DOI:** https://doi.org/10.18653/v1/2022.acl-long.261

## Abstract

Conversational agents have come increasingly closer to human competence in open-domain dialogue settings; however, such models can reflect insensitive, hurtful, or entirely incoherent viewpoints that erode a user’s trust in the moral integrity of the system. Moral deviations are difficult to mitigate because moral judgments are not universal, and there may be multiple competing judgments that apply to a situation simultaneously. In this work, we introduce a new resource, not to authoritatively resolve moral ambiguities, but instead to facilitate systematic understanding of the intuitions, values and moral judgments reflected in the utterances of dialogue systems. The Moral Integrity Corpus, MIC, is such a resource, which captures the moral assumptions of 38k prompt-reply pairs, using 99k distinct Rules of Thumb (RoTs). Each RoT reflects a particular moral conviction that can explain why a chatbot’s reply may appear acceptable or problematic. We further organize RoTs with a set of 9 moral and social attributes and benchmark performance for attribute classification. Most importantly, we show that current neural language models can automatically generate new RoTs that reasonably describe previously unseen interactions, but they still struggle with certain scenarios. Our findings suggest that MIC will be a useful resource for understanding and language models’ implicit moral assumptions and flexibly benchmarking the integrity of conversational agents. To download the data, see <url>https://github.com/GT-SALT/mic</url>

## Authors

[[Caleb Ziems]], [[Jane Yu]], [[Yi-Chia Wang]], [[Alon Halevy]], [[Diyi Yang]]

## Dataset Information

Size: 38,000 prompt-reply pairs; 99,000 distinct Rules of Thumb; 114,000 annotations

## Data Description

The Moral Integrity Corpus (MIC) captures the moral assumptions of 38,000 prompt-reply pairs using 99,000 distinct Rules of Thumb (RoTs), with 114,000 sets of structured annotations covering moral foundations, global consensus, violation severity, and reply alignment. GPT-2, BART, and T5 are evaluated for RoT generation, while BERT and ALBERT are benchmarked for RoT attribute classification. Chatbot replies were generated using BlenderBot, DialoGPT, and GPT-Neo to create the initial conversational pairs.

## Notes


## Citation Info

14 citations (Crossref/DOI) [2025-08-23]
