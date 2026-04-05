---








































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0450
type: journalArticle
short_title: "A World Full of Stereotypes? Further Investigation on Origin and Gender Bias in Multi-Lingual Word Embeddings"
year: 2021
first_author: "[[Mascha Kurpicz-Briki]]"
last_author: "[[Mascha Kurpicz-Briki]]"
authors: "Mascha Kurpicz-Briki"
doi: 10.3389/fdata.2021.625290
url: "https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2021.625290/full"
external_pdf: "https://europepmc.org/articles/PMC8209512?pdf=render"
publication: "Frontiers in Big Data"
CONF-CC: "Frontiers in Big Data"
pdf_extract: "PDF Extracts/2021/2021-Kurpicz-Briki-A World Full of Stereotypes Further Investigation on Origin and.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2021/2021-Kurpicz-Briki-A World Full of Stereotypes Further Investigation on Origin and.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "French, German, Italian"
cultures_nationalities_list: "French, German, Italian"
languages_list: "French, German, Italian, Swedish"
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
LLM_assessed: NA
DATA_URL: "NA"
tags: 
abstract: "Extends origin and gender bias analysis to multilingual word embeddings in four European languages including French. Demonstrates origin bias concerning local migration groups. Published in Frontiers in Big Data."
CONFERENCE: "Journal"
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Bias & Fairness"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: "FR"
author_region: "Western Europe"
author_global_north_south: "Global North"
weird_score: 75
is_benchmark: "No"
is_eval: "No"
is_dataset: "No"
data_description: "N/A"
data_metrics: "Not specified"
---
# A World Full of Stereotypes? Further Investigation on Origin and Gender Bias in Multi-Lingual Word Embeddings

## Authors

[[Mascha Kurpicz-Briki]]

## Metadata

**Authors:** Mascha Kurpicz-Briki

**Year:** 2021

**Type:** journalArticle

**Venue:** Frontiers in Big Data

**DOI:** [10.3389/fdata.2021.625290](https://doi.org/10.3389/fdata.2021.625290)

**Languages:** French, German, Italian, Swedish

## Links

- **DOI:** https://doi.org/10.3389/fdata.2021.625290
- **URL:** https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2021.625290/full

## Abstract

Extends origin and gender bias analysis to multilingual word embeddings in four European languages including French. Demonstrates origin bias concerning local migration groups. Published in Frontiers in Big Data.

## Summary

This paper extends previous work on bias in word embeddings to examine gender and origin bias in Italian and Swedish fastText embeddings, and investigates origin bias concerning Swiss migration groups in German embeddings. Using the Word Embedding Association Test (WEAT) method, the study demonstrates that bias manifests differently across languages and cultural contexts, confirming that real-world stereotypes are encoded in multilingual word embeddings. The authors propose BiasWords, an automatic method for detecting new forms of culturally-specific bias by exploring the vector space, emphasizing that bias detection and mitigation strategies must account for language-specific and cultural differences rather than applying English-centric approaches universally.

## Data Description

Extension of bias analysis to multilingual word embeddings (fastText) in Italian and Swedish, plus origin bias concerning Swiss migration groups in German embeddings. Tests bias using WEAT method on static embeddings, not LLMs.


## Detailed Summary

This paper extends previous work by Kurpicz-Briki (2020) on bias in word embeddings to examine gender and origin bias in Italian and Swedish fastText embeddings, while also investigating origin bias concerning Swiss migration groups in German embeddings. Using the Word Embedding Association Test (WEAT) method, the study demonstrates that publicly available off-the-shelf word embeddings in multiple European languages contain implicit stereotypes that mirror real-world biases. The authors adapt WEAT word lists to each language's cultural context, translating and culturally adjusting attribute and target word sets to capture locally relevant bias patterns (e.g., using names from local migration communities in Switzerland for origin bias tests in German).

A key contribution is the proposal of BiasWords, an automatic method for detecting new, previously unknown forms of bias in word embeddings. BiasWords works by exploring the vector space around known biased associations to discover additional words that exhibit similar bias patterns, enabling researchers to uncover culturally-specific biases that would not be detected by simply translating English-centric test words. The study confirms that bias manifests differently across languages and cultural contexts: for example, Italian embeddings show distinct origin bias patterns related to immigration from North Africa, while Swedish embeddings reflect bias patterns related to Nordic immigration contexts. The findings reinforce the argument that bias detection and mitigation strategies must be tailored to specific languages and cultural settings rather than applying universal English-derived approaches.

## Paper Outline

1. Introduction - Bias in AI applications and word embeddings
2. Related Work - WEAT methodology, existing bias studies, multilingual approaches
3. Methods - WEAT adaptation for Italian and Swedish, BiasWords method
4. Results - Gender and origin bias in Italian, Swedish, and German embeddings
5. Discussion - Cultural differences in bias, implications for mitigation
6. Conclusion

## Methods Summary

The study uses the WEAT methodology adapted from Caliskan et al. (2017), translating and culturally adjusting target and attribute word lists for Italian, Swedish, and German. Pre-trained fastText embeddings are used for all languages. The BiasWords method automatically discovers new bias-related words by identifying terms in the embedding space that exhibit similar cosine similarity patterns to known biased word pairs. For origin bias in German, the study specifically examines associations with names from Balkan migration communities in Switzerland, reflecting locally relevant demographic patterns. Statistical significance is assessed using WEAT effect sizes and permutation-based p-values.

## Results Summary

Gender bias is confirmed in both Italian and Swedish fastText embeddings, with male terms associated with career/science and female terms with family/arts, consistent with patterns observed in English, German, and French embeddings. Origin bias is detected in all tested languages, with European-associated names linked to positive attributes. German embeddings specifically show origin bias against names associated with Balkan migration communities in Switzerland. The BiasWords method successfully identifies additional bias-carrying words not present in the original WEAT word lists, demonstrating its utility for discovering culturally-specific bias patterns. The results show that while the general direction of bias is consistent across languages, the specific forms and magnitudes vary based on cultural context and linguistic structure.

## Conclusions

The authors emphasize that bias mitigation strategies must account for cultural and linguistic differences, as one-size-fits-all approaches derived from English will miss important language-specific bias patterns. Future work should extend BiasWords to contextualized language models (BERT, GPT) and investigate how debiasing techniques interact with different cultural contexts. The study highlights that even in more egalitarian societies (like Sweden), word embeddings still encode significant gender stereotypes, suggesting that bias in training data is deeply rooted in language itself.

## Artifact Contributions

No publicly released artifacts identified.

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** Extended bias analysis for French embeddings covering both gender and origin/migration-related bias in Swiss/European context.

## Tags

