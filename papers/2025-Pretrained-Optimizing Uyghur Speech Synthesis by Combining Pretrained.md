---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0626
type: conferencePaper
short_title: "Optimizing Uyghur Speech Synthesis by Combining Pretrained Cross-Lingual Model | ACM Transactions on Asian and Low-Resource Language Information Processing"
year: 2025
first_author: "[[Combining Pretrained]]"
last_author: "[[Combining Pretrained]]"
authors: "Combining Pretrained"
doi: 10.1145/3675397
url: "https://dl.acm.org/doi/10.1145/3675397"
publication: ACM
CONF-CC: "ACM TALIP"
pdf_extract: 
local_pdf: N/A
DATE_ADDED: 20260213
national_ethnic_cultural: Chinese
cultures_nationalities_list: Chinese
languages_list: Uyghur
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
LLM_assessed: XLM-R
DATA_URL: NA
tags: 
abstract: "End-to-end speech synthesis methodologies have exhibited considerable advancements for languages with abundant corpus resources. Nevertheless, such achievements are yet to be realized for languages constrained by limited corpora. This manuscript delineates a novel strategy that leverages contextual encoding information to augment the naturalness of the speech synthesized through FastSpeech2, particularly under resource-scarce conditions. Initially, we harness the cross-linguistic model XLM-RoBERTa to extract contextual features, which serve as an auxiliary input to the mel-spectrum decoder of FastSpeech2. Subsequently, we refine the mel-spectrum prediction module to mitigate the overfitting dilemma encountered by FastSpeech2 amidst scant training datasets. To this end, Conformer blocks, rather than traditional Transformer blocks, are employed within both the encoder and decoder to concentrate intensively on varying levels and granularities of feature information. Additionally, we introduce a token-average mechanism to equalize pitch and energy attributes at the frame level. The empirical outcomes indicate that our pre-training with the LJ Speech dataset, followed by fine-tuning using a modest 10-minute paired Uyghur corpus, yields satisfactory synthesized Uyghur speech. Relative to the baseline framework, our proposed technique halves the character error rate and enhances the mean opinion score by over 0.6. Similar results were observed in Mandarin Chinese experimental evaluations."
CONFERENCE: "Other Conference"
ethics_overall: No
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
research_topic: "Machine Translation"
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
is_eval: Yes
is_dataset: Yes
data_description: "Evaluation framework text corpus"
data_metrics: "Not specified"
---
# Optimizing Uyghur Speech Synthesis by Combining Pretrained Cross-Lingual Model | ACM Transactions on Asian and Low-Resource Language Information Processing

## Authors

[[Combining Pretrained]]

## Metadata

**Authors:** Combining Pretrained

**Year:** 2025

**Type:** conferencePaper

**Venue:** ACM

**DOI:** [10.1145/3675397](https://doi.org/10.1145/3675397)

**Languages:** Chinese, Multilingual, Uyghur

## Links

- **DOI:** https://doi.org/10.1145/3675397
- **URL:** https://dl.acm.org/doi/10.1145/3675397

## Abstract


End-to-end speech synthesis methodologies have exhibited considerable advancements for languages with abundant corpus resources. Nevertheless, such achievements are yet to be realized for languages constrained by limited corpora. This manuscript delineates a novel strategy that leverages contextual encoding information to augment the naturalness of the speech synthesized through FastSpeech2, particularly under resource-scarce conditions. Initially, we harness the cross-linguistic model XLM-RoBERTa to extract contextual features, which serve as an auxiliary input to the mel-spectrum decoder of FastSpeech2. Subsequently, we refine the mel-spectrum prediction module to mitigate the overfitting dilemma encountered by FastSpeech2 amidst scant training datasets. To this end, Conformer blocks, rather than traditional Transformer blocks, are employed within both the encoder and decoder to concentrate intensively on varying levels and granularities of feature information. Additionally, we introduce a token-average mechanism to equalize pitch and energy attributes at the frame level. The empirical outcomes indicate that our pre-training with the LJ Speech dataset, followed by fine-tuning using a modest 10-minute paired Uyghur corpus, yields satisfactory synthesized Uyghur speech. Relative to the baseline framework, our proposed technique halves the character error rate and enhances the mean opinion score by over 0.6. Similar results were observed in Mandarin Chinese experimental evaluations.

## Data Description

Constructs a Uyghur speech corpus to train and evaluate a FastSpeech2 speech synthesis system augmented with XLM-RoBERTa contextual encoding for low-resource conditions.


## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B10
**Relevance:** Relevant to Uyghur, Chinese, Multilingual

## Tags

