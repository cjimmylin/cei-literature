---





































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0443
type: preprint
short_title: "Preference Tuning For Toxicity Mitigation Generalizes Across Languages"
year: 2024
first_author: "[[Xiaochen Li]]"
last_author: "[[Stephen Bach]]"
authors: Xiaochen Li; Zheng Xin Yong; Stephen Bach
url: "https://arxiv.org/abs/2406.16235"
external_pdf: "https://arxiv.org/pdf/2406.16235.pdf"
publication: "arXiv / ACL Anthology"
CONF-CC: "Preprint"
pdf_extract: "PDF Extracts/2024/2024-Li-Preference Tuning For Toxicity Mitigation Generalizes Across Languages.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2024/2024-Li-Preference Tuning For Toxicity Mitigation Generalizes Across Languages.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "Multicultural/Cross-cultural"
cultures_nationalities_list: "Multicultural/Cross-cultural"
languages_list: "Multilingual"
religious_values: "Jainism"
rv_islam: 0
rv_christianity: 0
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 50
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: "Jainism"
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
LLM_assessed: "Aya, BLOOM, Llama-3"
DATA_URL: "https://github.com/BatsResearch/cross-lingual-detox"
tags: 
abstract: "Detoxifying multilingual Large Language Models (LLMs) has become crucial due to their increasing global use. In this work, we explore zero-shot cross-lingual generalization of preference tuning in detoxifying LLMs. In contrast to prior work that suggests limited crosslingual generalization for other safety tasks, we show that Direct Preference Optimization (DPO) training with only English data can significantly reduce toxicity in multilingual openended generations."
CONFERENCE: "ACL 2024"
ethics_overall: 95
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
is_benchmark: "No"
is_eval: Yes
is_dataset: "No"
data_description: "N/A"
data_metrics: "17 languages"
ethics_perspective: "Toxicity & Hate Speech"
---
# Preference Tuning For Toxicity Mitigation Generalizes Across Languages

## Authors

[[Xiaochen Li]], [[Zheng Xin Yong]], [[Stephen Bach]]

## Metadata

**Authors:** Xiaochen Li, Zheng Xin Yong, Stephen Bach

**Year:** 2024

**Type:** preprint

**Venue:** arXiv / ACL Anthology

**Languages:** 17 languages including French

## Links

- **arXiv:** https://arxiv.org/abs/2406.16235
- **Code/Data:** https://github.com/BatsResearch/cross-lingual-detox

## Abstract

Shows DPO training with only English data can significantly reduce toxicity in multilingual open-ended generations across 17 languages including French. Toxic generation probability drops from 46.8% to 3.9%. Uses mechanistic interpretability to identify dual multilinguality property of MLP layers. Published at EMNLP 2024 Findings.

## Summary

This paper demonstrates that Direct Preference Optimization (DPO) training using only English toxic/non-toxic data pairs can achieve zero-shot cross-lingual generalization for toxicity mitigation across 17 languages. The authors evaluate multiple multilingual LLMs (mGPT-1.3B, BLOOM, Llama3, Aya-23) and find that toxic generation probability drops dramatically (e.g., from 46.8% to 3.9% for mGPT) after English-only DPO training. Using mechanistic interpretability tools including causal intervention and activation analysis, they identify the 'dual multilinguality property' of MLP layers, where both key and value vectors encode multilingual toxic concepts, explaining how preference tuning generalizes across languages. The findings suggest that bilingual sentence retrieval accuracy can predict cross-lingual transferability of DPO.

## Data Description

Shows that DPO (Direct Preference Optimization) training with only English data significantly reduces toxicity in multilingual open-ended generations across 17 languages. Toxic generation probability drops from 46.8% to 3.9%. Uses mechanistic interpretability to identify dual multilinguality property of MLP layers.


## Detailed Summary

This paper demonstrates that Direct Preference Optimization (DPO) training using only English toxic/non-toxic data pairs achieves zero-shot cross-lingual generalization for toxicity mitigation across 17 languages. Unlike prior work suggesting limited cross-lingual transfer for safety tasks like safeguarding against malicious instructions, the authors show that DPO-based detoxification transfers robustly. For mGPT-1.3B, the probability of generating toxic continuations drops from 46.8% to 3.9% across all 17 languages after English-only DPO training. The results generalize to multiple LLM families including BLOOM (1.7B and 7.1B), Llama3-8B, and Aya-23-8B.

## Paper Outline

1. Introduction - Motivation for multilingual toxicity mitigation
2. Related Work - Cross-lingual RLHF generalization, multilingual toxicity evaluation
3. Experimental Setup - Models, datasets, evaluation metrics
4. Results - Cross-lingual generalization of DPO detoxification
5. Mechanistic Interpretability - Dual multilinguality of MLP layers
6. Predicting Cross-lingual Transferability
7. Conclusion

## Methods Summary

The authors train DPO on English-only toxic/non-toxic preference pairs and evaluate toxicity in 17 languages using the RTP-LX multilingual toxicity benchmark. They employ mechanistic interpretability tools including causal intervention and activation analysis to examine MLP key and value vectors in trained models. Bilingual sentence retrieval accuracy (using LASER embeddings) is used to predict language-pairwise transferability. Models evaluated include mGPT-1.3B, BLOOM (1.7B, 7.1B), Llama2-7B, Llama3-8B, and Aya-23-8B.

## Results Summary

English-only DPO training dramatically reduces toxic generation probability across all 17 languages: mGPT drops from 46.8% to 3.9%, with similar reductions for BLOOM and Llama variants. The mechanistic analysis reveals a "dual multilinguality property" of MLP layers: value vectors encode multilingual toxic concepts, and key vectors respond to toxic prompts consistently across languages. Post-DPO, key vector activations that promote toxic content are effectively suppressed. Bilingual sentence retrieval accuracy correlates strongly with cross-lingual detoxification transferability, providing a practical predictive tool.

## Conclusions

English-only preference tuning for toxicity mitigation generalizes cross-lingually in a zero-shot manner, contrasting with limited transfer observed for other safety tasks. The dual multilinguality property of MLP layers provides a mechanistic explanation for this generalization. Bilingual sentence retrieval can predict which languages will benefit most from English DPO training, offering practical guidance for multilingual safety deployment.

## Artifact Contributions

- **Code repository**: https://github.com/BatsResearch/cross-lingual-detox
- **Mechanistic insight**: Identification of dual multilinguality property in MLP key/value vectors
- **Practical predictor**: Bilingual sentence retrieval as a proxy for cross-lingual DPO transferability

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** Demonstrates cross-lingual toxicity mitigation for French. Mechanistic interpretability reveals multilingual toxic concept encoding in MLP layers.

## Tags

