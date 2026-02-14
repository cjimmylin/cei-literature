---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0461
type: preprint
short_title: "Dutch CrowS-Pairs: Adapting a Challenge Dataset for Measuring Social Biases in Language Models for Dutch"
year: 2025
first_author: "[[Shalaka Satheesh]]"
last_author: "[[Teena Hassan]]"
authors: "Shalaka Satheesh, Katrin Klug, Katharina Beckh, Hector Allende-Cid, Sebastian Houben, Teena Hassan"
url: "https://arxiv.org/abs/2507.16442"
external_pdf: "https://arxiv.org/pdf/2507.16442.pdf"
publication: arXiv
local_pdf: "[[PDFs/2025/2025-Satheesh-Dutch CrowS-Pairs Adapting a Challenge Dataset for Measuring Social.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Satheesh-Dutch CrowS-Pairs Adapting a Challenge Dataset for Measuring Social.md"
DATE_ADDED: 20260213
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
national_ethnic_cultural: "French, Dutch, American"
languages_list: "Dutch, English, French"
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: 
is_benchmark: No
is_eval: Yes
is_dataset: Yes
data_description: "Evaluation approach dataset"
data_metrics: "9 categories"
LLM_assessed: "BERTje, RobBERT, mBERT, GEITje, Mistral-7B, BERT, RoBERTa, FlauBERT, CamemBERT"
DATA_URL: NA
tags: 
abstract: "Warning: This paper contains explicit statements of offensive stereotypes which might be upsetting Language models are prone to exhibiting biases, further amplifying unfair and harmful stereotypes. Given the fast-growing popularity and wide application of these models, it is necessary to ensure safe and fair language models. As of recent considerable attention has been paid to measuring bias in language models, yet the majority of studies have focused only on English language."
ethics_perspective: "Bias & Fairness"
---
# Dutch CrowS-Pairs: Adapting a Challenge Dataset for Measuring Social Biases in Language Models for Dutch

## Authors

[[Shalaka Satheesh, Katrin Klug, Katharina Beckh, Hector Allende-Cid, Sebastian Houben, Teena Hassan]]

## Metadata

**Authors:** Shalaka Satheesh, Katrin Klug, Katharina Beckh, Hector Allende-Cid, Sebastian Houben, Teena Hassan

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** Dutch, English, French

**Benchmark:** Dutch CrowS-Pairs

## Links

- **arXiv:** https://arxiv.org/abs/2507.16442

## Abstract

First full adaptation of CrowS-Pairs for Dutch with 1,463 sentence pairs covering 9 bias categories including sexual orientation, gender, and disability. GEITje (Dutch fine-tuned model) exhibited significantly more bias than base Mistral-7B. Accepted at RANLP 2025.

## Summary

This paper presents Dutch CrowS-Pairs, the first full adaptation of the CrowS-Pairs bias measurement dataset for Dutch, containing 1,463 minimally different sentence pairs contrasting stereotyped versus anti-stereotyped language across 9 bias categories including sexual orientation, gender, and disability. The authors evaluate Dutch models (BERTje, RobBERT, GEITje), multilingual BERT, and Mistral-7B, comparing results with English (BERT, RoBERTa) and French (FlauBERT, CamemBERT) models. Results reveal that GEITje exhibits significantly more bias than base Mistral-7B, English models show the most bias while Dutch models show the least, and assigning personas to LLMs changes their exhibited bias levels, highlighting the role of cultural and linguistic factors in shaping model biases.

## Data Description

Dutch CrowS-Pairs is the first full adaptation of CrowS-Pairs for Dutch with 1,463 sentence pairs covering 9 bias categories including sexual orientation, gender, and disability. GEITje (Dutch fine-tuned model) exhibited significantly more bias than base Mistral-7B. Also evaluates English and French models for cross-lingual comparison.


## Detailed Summary

This paper introduces Dutch CrowS-Pairs, the first full adaptation of the CrowS-Pairs bias measurement dataset for Dutch, containing 1,463 sentence pairs covering 9 bias categories: race/ethnicity, nationality, physical appearance, sexual orientation, gender, religion, age, disability, and socioeconomic status. The dataset consists of minimally different sentence pairs where one sentence concerns disadvantaged groups and the other advantaged groups, enabling measurement of social biases in language models through pseudo-log-likelihood scoring. The adaptation process involved translating, culturally adapting, and validating sentence pairs to ensure relevance to Dutch cultural context.

Using the Dutch CrowS-Pairs dataset, the authors evaluate bias in several language models: Dutch-specific models (BERTje, RobBERT, GEITje), multilingual BERT, and Mistral-7B. Cross-lingual comparison with English models (BERT, RoBERTa) and French models (FlauBERT, CamemBERT) reveals that English models exhibit the most bias while Dutch models show the least. A notable finding is that GEITje, a Dutch fine-tuned model based on Mistral-7B, exhibits significantly more bias than the base Mistral-7B model, suggesting that language-specific fine-tuning can amplify existing biases. The study also investigates persona-based prompting, finding that assigning personas (e.g., "good person" or "bad person") to LLMs changes the level of bias they exhibit, with cultural and linguistic factors playing a significant role in shaping model biases.

## Paper Outline

1. Introduction - Need for non-English bias measurement datasets
2. Related Work - Bias detection methods, datasets, and multilingual efforts
3. Methods - Corpus development and experimental setup
4. Results - Bias measurements across models and languages
5. Discussion - Cross-lingual bias differences and persona effects
6. Conclusion

## Methods Summary

The Dutch CrowS-Pairs dataset is developed by translating and culturally adapting the English CrowS-Pairs, with modifications to ensure cultural relevance for Dutch contexts (e.g., replacing US-specific stereotypes with Dutch-relevant ones). Bias is measured using pseudo-log-likelihood scoring, comparing model preferences between stereotyped and anti-stereotyped sentence pairs. Models evaluated include Dutch (BERTje, RobBERT, GEITje), multilingual (mBERT, Mistral-7B), English (BERT, RoBERTa), and French (FlauBERT, CamemBERT). Persona-based prompting experiments assign different roles (good/bad person) to LLMs to study how impersonation affects bias expression. Both the adapted dataset and all evaluation scripts are made publicly available.

## Results Summary

Dutch language models exhibit the least overall bias compared to English and French models, while English models show the most pronounced biases. GEITje (Dutch fine-tuned Mistral) exhibits significantly more bias than the base Mistral-7B, indicating that language-specific fine-tuning can amplify biases. Bias levels vary substantially across the 9 categories, with nationality and religion showing particularly high bias rates. The cross-lingual comparison demonstrates that bias patterns are not consistent across languages, suggesting that cultural and linguistic factors significantly influence model biases. Persona assignment affects bias levels, with "bad person" personas generally increasing exhibited bias and "good person" personas sometimes reducing it.

## Conclusions

The study highlights the variability of bias across languages and contexts, demonstrating that findings from English bias research cannot be directly extrapolated to other languages. Limitations include potential quality issues from translation-based dataset construction and the limited number of models tested. Future work includes expanding the dataset with more culturally-specific Dutch stereotype scenarios, testing additional models, and developing bias mitigation strategies specifically designed for Dutch language models.

## Artifact Contributions

- **Dutch CrowS-Pairs**: First full Dutch adaptation of CrowS-Pairs with 1,463 sentence pairs across 9 bias categories (scripts and dataset made publicly available)

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** First dedicated Dutch social bias benchmark for language models, covering 9 bias categories.

## Tags

