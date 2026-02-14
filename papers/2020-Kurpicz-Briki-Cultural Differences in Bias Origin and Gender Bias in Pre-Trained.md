---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0449
type: conferencePaper
short_title: "Cultural Differences in Bias? Origin and Gender Bias in Pre-Trained German and French Word Embeddings"
year: 2025
first_author: "[[Mascha Kurpicz-Briki]]"
last_author: "[[Mascha Kurpicz-Briki]]"
authors: "Mascha Kurpicz-Briki"
url: "https://ceur-ws.org/Vol-2624/paper6.pdf"
external_pdf: "https://ceur-ws.org/Vol-2624/paper6.pdf"
publication: "CEUR Workshop Proceedings"
pdf_extract: "PDF Extracts/2020/2020-Kurpicz-Briki-Cultural Differences in Bias Origin and Gender Bias in Pre-Trained.md"
local_pdf: "[[PDFs/2020/2020-Kurpicz-Briki-Cultural Differences in Bias Origin and Gender Bias in Pre-Trained.pdf]]"
DATE_ADDED: 20260213
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
national_ethnic_cultural: "French, German"
languages_list: "French, German"
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: 
is_benchmark: No
is_eval: No
is_dataset: No
data_description: N/A
data_metrics: "Not specified"
LLM_assessed: NA
DATA_URL: NA
tags: 
abstract: 
ethics_perspective: "Bias & Fairness"
---
# Cultural Differences in Bias? Origin and Gender Bias in Pre-Trained German and French Word Embeddings

## Authors

[[Mascha Kurpicz-Briki]]

## Metadata

**Authors:** Mascha Kurpicz-Briki

**Year:** 2020

**Type:** conferencePaper

**Venue:** CEUR Workshop Proceedings

**Languages:** French, German

## Links

- **URL:** https://ceur-ws.org/Vol-2624/paper6.pdf

## Abstract

Investigates gender and origin bias in French and German word embeddings. Finds real-world bias and stereotypes from the 18th century are still present in today's embeddings. Shows cultural differences in bias forms across languages. Extended by subsequent work on Italian and Swedish embeddings.

## Summary

This paper investigates gender and origin bias in pre-trained German and French word embeddings (word2vec and fastText) using the Word Embedding Association Test (WEAT) method adapted from the Implicit Association Test. The analysis reveals that real-world biases and stereotypes from the 18th century persist in contemporary word embeddings, and demonstrates that gender bias manifests differently across languages due to cultural differences. The findings suggest that bias detection and mitigation strategies need to account for language-specific and culturally-specific patterns rather than applying English-centric approaches universally.

## Data Description

Analysis of gender and origin bias in multilingual word embeddings (word2vec, fastText) for four European languages including French. Tests bias using WEAT method but does not evaluate LLMs; focuses on static embeddings like word2vec and fastText.


## Detailed Summary

This paper investigates gender and origin bias in pre-trained German and French word embeddings using the Word Embedding Association Test (WEAT), which is the computational analog of the Implicit Association Test (IAT) from psychology. The author applies WEAT to publicly available word2vec and fastText embeddings in German and French, translating and adapting the original English-language test word lists to account for linguistic and cultural differences. The study examines whether known biases from English embeddings -- such as the association of male terms with science/career and female terms with arts/family -- are also present in German and French.

The results confirm that gender and origin biases found in English embeddings are also present in German and French word embeddings, but manifest in culturally specific forms. Notably, German gender bias takes a different form due to the grammatical gender system, where nouns carry intrinsic gender markers that can interact with or mask semantic gender associations. The study also identifies origin bias in both languages, showing that stereotypes dating back to the 18th century (such as associating European Americans with positive attributes) persist in contemporary word embeddings. The findings underscore that bias detection and mitigation methods developed for English cannot be directly transferred to other languages without accounting for cultural and linguistic differences in how bias is encoded.

## Paper Outline

1. Introduction - Bias in NLP and word embeddings
2. Related Work - Word embeddings (word2vec, GloVe, fastText), bias identification methods
3. Experimental Setup - WEAT methodology, word list translation, embeddings used
4. Results - Gender bias and origin bias findings for German and French
5. Discussion and Conclusion

## Methods Summary

The study uses the Word Embedding Association Test (WEAT) adapted from Caliskan et al. (2017), which measures implicit associations between target word sets (e.g., male vs. female names) and attribute word sets (e.g., career vs. family terms) using cosine similarity in the embedding space. The English WEAT word lists are translated to German and French, with cultural adaptations (e.g., using culturally appropriate names). The method is applied to publicly available pre-trained word2vec and fastText embeddings for both languages. Statistical significance is assessed using the WEAT effect size (Cohen's d) and permutation-based p-values.

## Results Summary

Both German and French embeddings exhibit significant gender bias, associating male terms with career/science and female terms with family/arts, consistent with English findings. However, German gender bias differs in form due to grammatical gender: the three-gender system (masculine, feminine, neuter) creates additional complexity in separating grammatical from semantic gender associations. Origin bias is confirmed in both languages, with European-associated names linked to positive attributes and non-European names to negative attributes, reproducing stereotypes that have historical roots in 18th-century racial categorizations. The findings demonstrate that bias is culturally embedded and language-specific, requiring tailored detection approaches.

## Conclusions

The study highlights the need for language-specific and culturally-aware bias detection methods rather than universal approaches derived from English. Future work should extend the analysis to additional languages and investigate how grammatical gender systems interact with semantic gender bias. The persistence of historical stereotypes in modern embeddings raises concerns about the fairness of NLP applications built on these resources.

## Artifact Contributions

No publicly released artifacts identified.

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** Demonstrates culturally-specific bias patterns in French word embeddings. Shows bias has different forms depending on language and cultural context.

## Tags

