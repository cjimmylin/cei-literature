---





Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0441
type: preprint
short_title: "Cross-Language Bias Examination in Large Language Models"
year: 2024
first_author: "[[Liang, Yuxuan]]"
last_author: "[[Mahmoud, Marwa]]"
authors: "[[Liang, Yuxuan]]; [[Mahmoud, Marwa]]"
authors_incomplete: false
url: "https://arxiv.org/abs/2512.16029"
external_pdf: "https://arxiv.org/pdf/2512.16029.pdf"
publication: arXiv
pdf_extract: "PDF Extracts/2024/2024-Liang-Cross-Language Bias Examination in Large Language Models.md"
local_pdf: "[[PDFs/2024/2024-Liang-Cross-Language Bias Examination in Large Language Models.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "Chinese, Arabic, French, Spanish"
cultures_nationalities_list: "Chinese, Arabic, French, Spanish"
languages_list: "Arabic, Chinese, English, French, Spanish"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: GPT-4
DATA_URL: "NA"
tags: 
abstract: "This study introduces an innovative multilingual bias evaluation framework for assessing bias in Large Language Models, combining explicit bias assessment through the BBQ benchmark with implicit bias measurement using a prompt-based Implicit Association Test. By translating the prompts and word list into five target languages — English, Chinese, Arabic, French, and Spanish — we were able to directly compare different types of bias across languages."
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Bias & Fairness"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Multilingual benchmark for bias and fairness"
data_metrics: "5 languages"
---
# Cross-Language Bias Examination in Large Language Models

## Authors

[[Liang, Yuxuan]], [[Mahmoud, Marwa]]

## Metadata

**Authors:** Liang, Yuxuan; Mahmoud, Marwa

**Year:** 2024

**Type:** preprint

**Venue:** arXiv

**Languages:** Arabic, Chinese, English, French, Spanish

## Links

- **arXiv:** https://arxiv.org/abs/2512.16029

## Abstract

Multilingual bias evaluation framework combining explicit bias assessment (BBQ benchmark translated to 5 languages) with implicit bias measurement using prompt-based IAT. Finds significant bias differences across languages, with Arabic and Spanish showing high stereotyping consistently. Uses DeepL API for BBQ French translation.

## Summary

This study introduces a comprehensive multilingual bias evaluation framework that assesses both explicit and implicit bias in Large Language Models across five languages (English, Chinese, Arabic, French, Spanish). The authors translate the BBQ benchmark into target languages via DeepL API for explicit bias assessment and adapt the Implicit Association Test (IAT) with multilingual word lists to measure implicit bias. Results reveal substantial cross-language variations, with Arabic and Spanish consistently showing high levels of stereotyping while Chinese and English exhibit lower bias levels. Notably, they find opposite patterns across bias types, such as age showing the lowest explicit bias but highest implicit bias, highlighting the importance of dual-method bias detection.

## Data Description

Multilingual bias evaluation framework combining explicit bias assessment (BBQ benchmark translated to 5 languages: Arabic, Chinese, English, French, Spanish) with implicit bias measurement using prompt-based Implicit Association Test. Finds significant bias differences across languages, with Arabic and Spanish showing high stereotyping.


## Detailed Summary

This study constructs a multilingual bias evaluation framework that combines explicit and implicit bias assessment to examine LLM bias across five languages (English, Chinese, Arabic, French, Spanish). For explicit bias, the authors translate BBQ benchmark prompts into target languages using DeepL API and evaluate GPT-4's responses to derive accuracy and bias scores across dimensions including gender, age, race, and religion. For implicit bias, they adapt the Implicit Association Test (IAT) by translating attribute word lists and prompting the model to associate attributes with target concepts, enabling calculation of IAT-style bias scores. The dual-method design reveals that explicit and implicit biases are often divergent, filling a critical gap in multilingual LLM fairness research.

## Paper Outline

1. Introduction - Research questions and contributions
2. Related Works - Explicit bias measuring, implicit bias measuring, multilingual LLM performances
3. Methodology - Translation pipeline, BBQ explicit bias testing, IAT implicit bias testing
4. Results - Cross-language bias scores across dimensions
5. Discussion - Linguistic, cultural, and technical factors explaining disparities
6. Conclusion

## Methods Summary

The study employs a four-step workflow: (1) prepare English BBQ prompts and IAT word lists, (2) translate all materials into five target languages via DeepL API with careful meaning preservation, (3) invoke GPT-4 across all languages to collect responses, and (4) compute bias scores. For explicit bias, BBQ accuracy and bias scores are derived from GPT-4's multiple-choice answers in ambiguous and disambiguated contexts. For implicit bias, IAT scores are calculated from GPT-4's forced-choice associations between attributes (e.g., pleasant/unpleasant words) and target concepts (e.g., racial groups), measuring response latency-like association strengths.

## Results Summary

Arabic and Spanish consistently show high levels of stereotype across both explicit and implicit measures. Chinese and English exhibit comparatively lower bias levels. A notable finding is the opposite pattern across bias types: age shows the lowest explicit bias but the highest implicit bias, highlighting that standard benchmarks alone would miss significant latent biases. Gender bias is more prominent in explicit measures, while race-related biases appear more in implicit measures. The results demonstrate that LLMs vary significantly across languages and bias dimensions.

## Conclusions

The framework demonstrates that bias in LLMs is not uniform across languages and that explicit debiasing techniques may not address implicit biases. The divergence between explicit and implicit bias patterns underscores the need for dual-method evaluation approaches in multilingual settings. The work provides a reproducible methodology for cross-language bias analysis and establishes a foundation for developing equitable multilingual LLMs.

## Artifact Contributions

- **Multilingual bias evaluation framework**: Combining BBQ (explicit) and IAT (implicit) methods across five languages
- **Cross-language bias scores**: Empirical bias measurements for English, Chinese, Arabic, French, and Spanish on GPT-4
- **Methodology template**: Reproducible workflow for multilingual bias assessment using DeepL translation and dual-method design

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** Directly evaluates French-language bias in LLMs using BBQ and IAT approaches. Reveals age shows lowest explicit but highest implicit bias across languages.

## Tags

