---


































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0431
type: conferencePaper
short_title: "French CrowS-Pairs: Extending a challenge dataset for measuring social bias in masked language models to a language other than English"
year: 2022
first_author: "[[Aurélie Névéol]]"
last_author: "[[Karën Fort]]"
authors: Aurélie Névéol; Yoann Dupont; Julien Bezançon; Karën Fort
url: "https://aclanthology.org/2022.acl-long.583/"
external_pdf: "https://aclanthology.org/2022.acl-long.583.pdf"
publication: "ACL Anthology"
CONF-CC: "N/A"
pdf_extract: "PDF Extracts/2022/2022-Névéol-French CrowS-Pairs Extending a challenge dataset for measuring social.md"
local_pdf: "[[PDFs/2022/2022-Névéol-French CrowS-Pairs Extending a challenge dataset for measuring social.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "French, American"
cultures_nationalities_list: "French, American"
languages_list: "French"
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
LLM_assessed: "BERT, CamemBERT, FlauBERT, FrALBERT"
DATA_URL: "https://github.com/masonreznov/French-CrowS-Pairs"
tags: 
abstract: "Warning: This paper contains explicit statements of offensive stereotypes which may be upsetting Much work on biases in natural language processing has addressed biases linked to the social and cultural experience of English speaking individuals in the United States. We seek to widen the scope of bias studies by creating material to measure social bias in language models (LMs) against speciﬁc demographic groups in France."
CONFERENCE: "ACL 2022"
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
is_benchmark: Yes
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation approach dataset"
data_metrics: "Not specified"
ethics_perspective: "Bias & Fairness"
---
# French CrowS-Pairs: Extending a challenge dataset for measuring social bias in masked language models to a language other than English

## Authors

[[Aurélie Névéol]], [[Yoann Dupont]], [[Julien Bezançon]], [[Karën Fort]]

## Metadata

**Authors:** Aurélie Névéol, Yoann Dupont, Julien Bezançon, Karën Fort

**Year:** 2022

**Type:** conferencePaper

**Venue:** ACL Anthology

**Languages:** French

**Benchmark:** French CrowS-Pairs

## Links

- **URL:** https://aclanthology.org/2022.acl-long.583/
- **Code/Data:** https://huggingface.co/datasets/BigScienceBiasEval/crows_pairs_multilingual

## Abstract

Extends the US-centered CrowS-Pairs dataset to French with 1,679 sentence pairs covering stereotypes in ten bias categories. Includes 1,467 translated pairs and 212 newly crowdsourced pairs. Shows four widely used French/multilingual language models favor stereotypical sentences in most bias categories. CamemBERT is more biased than FlauBERT.

## Summary

This paper extends the US-centered CrowS-Pairs bias measurement dataset to French, creating 1,677 sentence pairs covering ten bias categories including gender, religion, age, and nationality. The dataset consists of 1,467 translated pairs from the original English dataset and 210 newly crowdsourced French-specific pairs that were back-translated to English. Testing four French and multilingual masked language models (CamemBERT, FlauBERT, FrALBERT, mBERT) reveals that all models favor stereotypical sentences in most bias categories, with CamemBERT showing more bias than FlauBERT. The translation process identified US-centric cultural traits in the original dataset and provides guidelines for extending the dataset to other languages and cultural contexts.

## Data Description

French adaptation of CrowS-Pairs with 1,677 sentence pairs measuring social bias in masked language models across 10 bias categories


## Detailed Summary

This paper extends the US-centered CrowS-Pairs bias measurement dataset to French, creating 1,677 sentence pairs covering stereotypes across ten bias categories including gender, religion, age, nationality, sexual orientation, socioeconomic status, physical appearance, and disability. The dataset consists of 1,467 sentence pairs translated from the original English CrowS-Pairs and 210 newly crowdsourced French-specific pairs that were back-translated to English. The translation process involved professional-quality manual translation by native French speakers fluent in English, with careful attention to maintaining minimal pairs and adapting culturally-specific stereotypes (e.g., replacing "Mexicans love tacos" with "Les marocains adorent faire du couscous"). The authors identified and addressed several limitations in the original CrowS-Pairs, including non-minimal pairs, double switches, and bias mismatches.

Four widely used French and multilingual masked language models (CamemBERT, FlauBERT, FrALBERT, and multilingual BERT) were evaluated. Results show all models except mBERT for French exhibit statistically significant bias (metric scores above 50, t-test p<0.05), with CamemBERT showing the highest bias (59.3 metric score) and mBERT the lowest (50.9). English models generally exhibited higher bias than French models. The study reveals that both the pretraining corpus and model architecture can drastically impact bias expression, and provides guidelines for extending the dataset to other languages and cultural environments.

## Paper Outline

1. Introduction - Motivation for extending bias measurement to French
2. Corpus Development - Translation methodology, addressing CrowS-Pairs limitations, new data collection via LanguageARC
3. Measuring Bias in Masked Language Models - Experimental protocol, results for French and English models
4. Corpus Analysis - Translation process commentary, comparison to original CrowS-Pairs, recommendations for extension
5. Related Work - Prior work on French bias measurement
6. Conclusion - Summary and future directions
7. Ethical Considerations and Limitations

## Methods Summary

The authors extended CrowS-Pairs through two approaches: (1) manual translation of the original 1,508 English pairs into French by native French speakers with professional translation training, with each translation verified by a second author; and (2) crowdsourcing of 210 new French-specific stereotype pairs via the LanguageARC citizen science platform, which were then back-translated to English. Bias was measured using the pseudo-log-likelihood scoring method from the original CrowS-Pairs, evaluating four French/multilingual masked language models (CamemBERT-base, FlauBERT-base, FrALBERT, mBERT) on a single GPU. Statistical significance was assessed via t-tests (p<0.05).

## Results Summary

All tested models favor stereotypical sentences in most bias categories. CamemBERT shows the highest overall bias (metric score 59.3), followed by FrALBERT (55.9), FlauBERT (53.7), and mBERT (50.9). For English, RoBERTa (65.1) and BERT (61.3) show higher bias than their French counterparts. Religion is the most biased category for French models (CamemBERT: 69.6, FrALBERT: 72.2). Notably, mBERT for French shows no significant bias overall. The newly collected French-native sentences show slightly different bias patterns compared to translated sentences, confirming the value of culturally-specific data collection.

## Conclusions

The study identifies US-centric cultural traits in the original CrowS-Pairs that do not transfer to French contexts. Limitations include the restriction to masked language models, the focus on only two cultural contexts (US and France), and the volunteer-based crowdsourcing which may limit participant diversity. Future work includes extending the dataset to more languages, adding formal bias descriptions using frameworks like Social Bias Frames, and applying the methodology to generative language models.

## Artifact Contributions

- **French CrowS-Pairs Dataset**: 1,677 French sentence pairs and 210 new English pairs covering 10 bias categories, released under CC BY-SA 4.0 (https://gitlab.inria.fr/french-crows-pairs/acl-2022-paper-data-and-code)
- **Revised English CrowS-Pairs**: Corrected version addressing non-minimal pairs, double switches, and bias mismatches
- **LanguageARC Project**: Citizen science data collection project for French stereotypes (https://languagearc.com/projects/19)

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** First French-specific social bias measurement dataset. Identifies US-centric cultural traits in original CrowS-Pairs and creates France-specific stereotypes.

## Tags

