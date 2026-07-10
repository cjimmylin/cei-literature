---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0507
type: conferencePaper
short_title: "HATE-ITA: Hate Speech Detection in Italian Social Media Text"
year: 2025
first_author: "[[MilaNLProc group]]"
last_author: "[[MilaNLProc group]]"
authors: "MilaNLProc group"
url: "https://aclanthology.org/2022.woah-1.24/"
external_pdf: "https://aclanthology.org/2022.woah-1.24.pdf"
publication: "ACL Anthology (WOAH @ NAACL 2022)"
CONF-CC: "NAACL 2022"
pdf_extract: "PDF Extracts/2022/2022-group-HATE-ITA Hate Speech Detection in Italian Social Media Text.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2022/2022-group-HATE-ITA Hate Speech Detection in Italian Social Media Text.pdf]]"
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
LLM_assessed: "BERT, XLM-R"
DATA_URL: "https://github.com/MilaNLProc/hate-ita"
tags: 
abstract: "Warning: This paper contains examples of language that some people may find offensive. Online hate speech is a dangerous phenomenon that can (and should) be promptly counteracted properly. While Natural Language Processing has been successfully used for the purpose, many of the research efforts are directed toward the English language. This choice severely limits the classification power in non-English languages."
CONFERENCE: "NAACL 2022"
ethics_overall: No
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Toxicity & Hate Speech"
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
is_benchmark: Yes
is_eval: No
is_dataset: Yes
data_description: "Benchmark dataset for hate speech detection"
data_metrics: "Not specified"
---
# HATE-ITA: Hate Speech Detection in Italian Social Media Text

## Authors

[[MilaNLProc group]]

## Metadata

**Authors:** MilaNLProc group

**Year:** 2022

**Type:** conferencePaper

**Venue:** ACL Anthology (WOAH @ NAACL 2022)

**Languages:** English, Italian

**Benchmark:** HATE-ITA

## Links

- **URL:** https://aclanthology.org/2022.woah-1.24/
- **Code/Data:** https://github.com/MilaNLProc/hate-ita

## Abstract

Multi-language model trained on English data and Italian datasets for hate speech detection. HATE-ITA outperforms mono-lingual models and adapts well to language-specific Italian slurs. Released as a benchmark tool for the Italian community.

## Summary

This paper presents HATE-ITA, a set of multilingual models for hate speech detection in Italian social media text, trained on a large collection of English hate speech data combined with smaller Italian datasets. The authors evaluate multiple Italian language models (AlBERTo, BERT-Italian, GilBERTo, UmBERTo) and multilingual models (mBERT, XLM-RoBERTa) on two Italian hate speech datasets covering misogyny and anti-immigrant hate. Results show that multilingual models trained on combined English-Italian data outperform monolingual models and adapt well to language-specific Italian slurs. The HATE-ITA models are released as an open-source Python library to provide a strong baseline for the Italian NLP community.

## Data Description

HATE-ITA: multilingual models for Italian hate speech detection, trained on combined English and Italian hate speech datasets covering 177k+ samples across 5 protected categories.


## Detailed Summary

This paper presents HATE-ITA, a set of multilingual models for hate speech detection in Italian social media text, addressing the severe imbalance between English-focused and non-English hate speech detection resources. The authors combine a large collection of English hate speech data (177,749 samples across five target categories: origin, gender, religion, sexual orientation, and disability) with smaller Italian datasets from EVALITA shared tasks (AMI18 for misogyny and HaSpeeDe18 for anti-immigrant hate speech). The work demonstrates that multilingual training significantly outperforms monolingual approaches for Italian hate speech detection.

The study evaluates six pretrained language models in three experimental frameworks: monolingual (Italian-only training), multilingual (combined English-Italian training), and zero-shot cross-lingual (English-only training tested on Italian). Results show that multilingual XLM-Twitter achieves the best overall performance (83.34 Macro-F1), substantially outperforming the best monolingual model mBERT (66.93 Macro-F1). The models are further validated on the Multilingual HateCheck (MHC) Italian subset, where XLM-Large achieves 77.26 Macro-F1, outperforming the original baseline of 69.60. Qualitative analysis using SHAP explanations demonstrates the models' ability to distinguish context-dependent Italian expressions, such as "finocchi" (meaning either "fennels" or a slur depending on context).

## Paper Outline

1. Introduction - Motivation for Italian hate speech detection and multilingual approach
2. Datasets - Background, Italian corpora (AMI18, HaSpeeDe18), English corpora compilation
3. Experimental Methodology - Models, data setup, training frameworks
4. Results - Overall results, per-dataset results, Multilingual HateCheck evaluation, qualitative evaluation
5. Related Work - Cross-lingual and zero-shot hate speech detection
6. Conclusion - Summary and ethical statement

## Methods Summary

Six pretrained models were tested: multilingual (XLM-RoBERTa base/large, XLM-Twitter, mBERT) and monolingual Italian (ITA-Base-XXL, ITA-Base), plus DeHateBert. Models were fine-tuned for 5 epochs with batch size 64, learning rate 1e-3, and AdamW optimizer, evaluated every 50 steps with best checkpoint selection based on validation loss. Three experimental frameworks were compared: monolingual Italian training, multilingual English+Italian training, and zero-shot cross-lingual English-only training. All experiments were repeated 5 times with averaged results. SHAP explanations were used for qualitative evaluation of token-level contributions.

## Results Summary

Multilingual training consistently outperforms monolingual and zero-shot approaches. XLM-Twitter MULTI achieves the best overall Macro-F1 of 83.34, compared to 66.93 for the best monolingual model (mBERT MONO) and 57.27 for the best zero-shot model (XLM-Large ZERO). On individual datasets, XLM-Twitter beats DeHateBert by 39 and 19 F1 points on AMI18 and AMI20 respectively. On Multilingual HateCheck, XLM-Large achieves 77.26 Macro-F1, surpassing the original baseline of 69.60. Monolingual Italian models (ITA-Base: 40.45, ITA-Base-XXL: 61.20) significantly underperform, confirming that small Italian-only datasets are insufficient for robust hate speech detection.

## Conclusions

The authors acknowledge HATE-ITA as a first step rather than a definitive solution, noting uncertainty about whether the model maintains fair precision across different targets and categories. Key limitations include potential overlooking of sensible details and the need for careful benchmarking across additional hate speech targets. Future work should expand target coverage and evaluate cross-lingual transfer to other mid-to-low resource languages.

## Artifact Contributions

- **HATE-ITA Models**: Set of multilingual hate speech detection models for Italian, released as open-source Python library (https://github.com/MilaNLProc/hate-ita)
- **HuggingFace Models**: Available at https://huggingface.co/MilaNLProc

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B8
**Relevance:** Key Italian hate speech detection benchmark with released model and dataset.

## Tags

