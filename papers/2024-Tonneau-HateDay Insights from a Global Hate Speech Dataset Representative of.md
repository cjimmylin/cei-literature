---






































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0435
type: preprint
short_title: "HateDay: Insights from a Global Hate Speech Dataset Representative of a Day on Twitter"
year: 2024
first_author: "[[Tonneau, Manuel]]"
last_author: "[[Röttger, Paul]]"
authors: "Tonneau, Manuel; Liu, Diyi; Malhotra, Niyati; Hale, Scott A.; Fraiberger, Samuel P.; Orozco-Olvera, Victor; Röttger, Paul"
authors_incomplete: false
url: "https://arxiv.org/abs/2411.15462"
external_pdf: "https://arxiv.org/pdf/2411.15462.pdf"
publication: "arXiv / ACL Anthology"
CONF-CC: "Preprint"
pdf_extract: "PDF Extracts/2024/2024-Tonneau-HateDay Insights from a Global Hate Speech Dataset Representative of.md"
local_pdf: "[[PDFs/2024/2024-Tonneau-HateDay Insights from a Global Hate Speech Dataset Representative of.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "Multicultural/Cross-cultural"
cultures_nationalities_list: "Multicultural/Cross-cultural"
languages_list: "Arabic, English, French, German, Indonesian, Portuguese, Spanish, Turkish"
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
LLM_assessed: "Aya, Llama-3"
DATA_URL: "https://huggingface.co/datasets/manueltonneau/hateday"
tags: 
abstract: "To address the global challenge of online hate speech, prior research has developed detection models to flag such content on social media. However, due to systematic biases in evaluation datasets, the real-world effectiveness of these models remains unclear, particularly across geographies. We introduce HATEDAY, the first global hate speech dataset representative of social media settings, constructed from a random sample of all tweets posted on September 21, 2022 and covering eight languages..."
CONFERENCE: "ACL 2024"
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 5
contractarian_ethics: 0
care_ethics: 0
is_benchmark: "No"
is_eval: Yes
is_dataset: "Yes"
data_description: "Annotated dataset for hate speech detection"
data_metrics: "540k tweets; 20k tweets; 8 languages"
ethics_perspective: "Toxicity & Hate Speech"
---
# HateDay: Insights from a Global Hate Speech Dataset Representative of a Day on Twitter

## Authors

[[Manuel Tonneau|Tonneau, Manuel]], [[Liu, Diyi]], [[Malhotra, Niyati]], [[Hale, Scott A]], [[Fraiberger, Samuel P]], [[Victor Orozco-Olvera|Orozco-Olvera, Victor]], [[Röttger, Paul]]

## Metadata

**Authors:** Tonneau, Manuel; Liu, Diyi; Malhotra, Niyati; Hale, Scott A.; Fraiberger, Samuel P.; Orozco-Olvera, Victor; Röttger, Paul

**Year:** 2024

**Type:** preprint

**Venue:** arXiv / ACL Anthology

**Languages:** Arabic, English, French, German, Indonesian, Portuguese, Spanish, Turkish

**Benchmark:** HateDay

## Links

- **arXiv:** https://arxiv.org/abs/2411.15462
- **Code/Data:** https://huggingface.co/datasets/manueltonneau/hateday

## Abstract

Global Twitter dataset of 540K tweets sampled from September 21, 2022 and annotated for hate speech detection in 8 languages including French. Each language has 20K tweets with annotations by 3 human annotators per language (hateful, offensive, or neutral). Published at ACL 2025.

## Summary

This paper introduces HateDay, the first hate speech dataset representative of real-world social media settings, constructed from a random sample of 240,000 tweets (20,000 per language/country) posted on September 21, 2022 across eight languages (Arabic, English, French, German, Indonesian, Portuguese, Spanish, Turkish) and four English-speaking countries. Using prescriptive annotation guidelines with three annotators per language, the dataset enables cross-lingual and cross-national comparison of hate speech prevalence and composition. Evaluation of publicly available hate speech detection models reveals that performance is substantially overestimated on academic datasets and extremely low in real-world settings (especially for non-European languages), driven by models' difficulty distinguishing hate from offensive speech and mismatches between academic and real-world target groups. The findings suggest automatic moderation is currently too error-prone, while human-in-the-loop systems can achieve higher moderation rates at the cost of substantial human review.

## Data Description

Introduces HATEDAY, a global hate speech dataset of 240,000 annotated tweets (20,000 per language/country) sampled from all Twitter posts on September 21, 2022, covering 8 languages and 4 English-speaking countries.


## Detailed Summary

This paper introduces HateDay, the first hate speech dataset designed to be representative of real-world social media settings, constructed from a random sample of all tweets posted on September 21, 2022. Unlike existing academic hate speech datasets that suffer from systematic biases (keyword-based sampling, topic-specific collection), HateDay provides an unbiased snapshot of hateful content across eight languages (Arabic, English, French, German, Indonesian, Portuguese, Spanish, Turkish) and four English-speaking countries. The dataset contains approximately 540,000 tweets (20,000 per language/country) annotated by three trained annotators per language using prescriptive guidelines with three categories (hateful, offensive, neutral). The work reveals that existing hate speech detection models are substantially overperforming on academic benchmarks compared to real-world settings.

## Paper Outline

1. Introduction - Need for representative hate speech evaluation
2. Related Work - Limitations of existing datasets, cross-lingual hate speech
3. Dataset Construction - Sampling strategy, annotation guidelines, quality control
4. Analysis - Hate speech prevalence and composition across languages
5. Model Evaluation - Performance of existing detection models on HateDay
6. Implications - For automatic moderation and human-in-the-loop systems
7. Conclusion

## Methods Summary

Tweets are randomly sampled from the Twitter Decahose (10% random sample of all tweets) for a single day (September 21, 2022), then filtered to retain only organic tweets in the target languages. Prescriptive annotation guidelines define three categories: hateful (targeting protected groups), offensive (rude but not targeting protected groups), and neutral. Three trained annotators per language independently label each tweet, with systematic quality control. The authors evaluate publicly available hate speech detection models on HateDay and compare performance against standard academic benchmarks to quantify the "performance gap" between lab and real-world settings.

## Results Summary

Evaluation of existing hate speech detection models reveals that performance is substantially overestimated on academic datasets compared to real-world settings, with extremely low real-world performance especially for non-European languages (Arabic, Indonesian, Turkish). The performance gap is primarily driven by two factors: (1) models' difficulty distinguishing hate speech from offensive (but non-hateful) speech, and (2) mismatches between target groups represented in training data and those appearing in real-world content. The analysis suggests that fully automatic moderation is currently too error-prone, while human-in-the-loop systems can achieve higher moderation rates at the cost of substantial human review effort.

## Conclusions

HateDay demonstrates that academic hate speech datasets create an inflated view of model capabilities. Representative evaluation is essential for understanding the real-world effectiveness of detection systems, particularly across geographies and languages. The work advocates for human-in-the-loop moderation systems as more practical than fully automatic approaches and provides a foundation for developing more realistic hate speech evaluation resources.

## Artifact Contributions

- **HateDay dataset**: ~540K representative tweets in 8 languages annotated for hate speech (available at https://huggingface.co/datasets/manueltonneau/hateday)
- **Prescriptive annotation guidelines**: Detailed per-language guidelines with three-category schema
- **Real-world performance evaluation**: Systematic comparison of model performance on academic vs. representative data
- **Published at ACL 2025**

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** Large-scale multilingual hate speech dataset with dedicated French annotations. Prescriptive annotation with detailed guidelines and target group identification.

## Tags

