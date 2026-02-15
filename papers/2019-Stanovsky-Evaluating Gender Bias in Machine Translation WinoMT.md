---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0448
type: conferencePaper
short_title: "Evaluating Gender Bias in Machine Translation (WinoMT)"
year: 2025
first_author: "[[Gabriel Stanovsky]]"
last_author: "[[Luke Zettlemoyer]]"
authors: "Gabriel Stanovsky, Noah A. Smith, Luke Zettlemoyer"
url: "https://aclanthology.org/P19-1164/"
external_pdf: "https://arxiv.org/pdf/1906.00591v1.pdf"
publication: "ACL Anthology"
pdf_extract: "PDF Extracts/2019/2019-Stanovsky-Evaluating Gender Bias in Machine Translation WinoMT.md"
local_pdf: "[[PDFs/2019/2019-Stanovsky-Evaluating Gender Bias in Machine Translation WinoMT.pdf]]"
DATE_ADDED: 20260213
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "Arabic, French, Italian, Spanish, Russian, Hebrew/Israeli"
languages_list: "Arabic, Czech, English, French, Hebrew, Italian, Polish, Russian, Spanish, Ukrainian"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation methodology dataset"
data_metrics: "Not specified"
LLM_assessed: "NA"
DATA_URL: "https://github.com/gabrielStanworthy/mt_gender"
tags: 
abstract: "We present the ﬁrst challenge set and evaluation protocol for the analysis of gender bias in machine translation (MT). Our approach uses two recent coreference resolution datasets composed of English sentences which cast participants into non-stereotypical gender roles (e.g., “The doctor asked the nurse to help her in the operation”). We devise an automatic gender bias evaluation method for eight target languages with grammatical gender, based on morphological analysis (e.g."
ethics_perspective: "Bias & Fairness"
---
# Evaluating Gender Bias in Machine Translation (WinoMT)

## Authors

[[Gabriel Stanovsky, Noah A. Smith, Luke Zettlemoyer]]

## Metadata

**Authors:** Gabriel Stanovsky, Noah A. Smith, Luke Zettlemoyer

**Year:** 2019

**Type:** conferencePaper

**Venue:** ACL Anthology

**Languages:** Arabic, Czech, English, French, Hebrew, Italian, Polish, Russian, Spanish, Ukrainian

**Benchmark:** WinoMT

## Links

- **URL:** https://aclanthology.org/P19-1164/

## Abstract

Challenge set of 3,888 English segments for evaluating gender bias in machine translation to 8+ languages including French. Balanced with respect to gender and stereotype. Proposes accuracy, gender gap (Delta-G), and stereotype gap (Delta-S) metrics. Foundational work cited in 47+ en-fr studies.

## Summary

This paper introduces WinoMT, a challenge set of 3,888 English sentences derived from Winogender and WinoBias coreference datasets for evaluating gender bias in machine translation to eight target languages with grammatical gender. The authors use morphological analysis to automatically detect whether MT systems correctly translate gender based on context rather than stereotypes, testing four commercial systems (Google Translate, Microsoft Translator, Amazon Translate, SYSTRAN) and two academic models. The evaluation reveals that all tested systems exhibit significant gender bias, stereotypically translating occupations (e.g., translating 'doctor' as male and 'nurse' as female regardless of context), with the paper proposing accuracy, gender gap, and stereotype gap metrics for measuring bias.

## Data Description

The paper introduces WinoMT, a challenge set of 3,888 English sentences for evaluating gender bias in machine translation, composed from the Winogender and WinoBias coreference datasets. The sentences are balanced between male/female genders and stereotypical/non-stereotypical gender-role assignments. The authors evaluate four commercial MT systems (Google Translate, Microsoft Translator, Amazon Translate, SYSTRAN) and two academic models across eight target languages, finding significant gender-biased translation errors. No LLMs from the canonical list were tested.


## Detailed Summary

This paper introduces WinoMT, the first challenge set and evaluation protocol for measuring gender bias in machine translation. WinoMT is composed by concatenating the Winogender (720 instances) and WinoBias (3,168 instances) coreference datasets, yielding 3,888 English sentences balanced between male and female genders and between stereotypical and non-stereotypical gender-role assignments. The evaluation pipeline translates WinoMT sentences into eight target languages with grammatical gender (Spanish, French, Italian, Russian, Ukrainian, Hebrew, Arabic, German), uses fast_align for source-target alignment, and extracts the translated entity's gender via language-specific morphological analysis tools (spaCy for Romance languages, Korobov's analyzer for Slavic languages, and custom tools for Semitic and Germanic languages).

The authors evaluate four commercial MT systems (Google Translate, Microsoft Translator, Amazon Translate, SYSTRAN) and two state-of-the-art academic models (Ott et al. 2018 for English-French, Edunov et al. 2018 for English-German). Three metrics are computed: overall gender accuracy, gender gap (difference in F1 between male and female translations), and stereotype gap (difference in F1 between pro-stereotypical and anti-stereotypical role assignments). Results reveal that all systems exhibit significant gender bias across all tested languages, with most systems performing near chance on gender accuracy and consistently better on stereotypical assignments. A novel "fighting bias with bias" experiment shows that prepending gendered adjectives ("handsome"/"pretty") can improve accuracy by up to 11.2 percentage points in some languages. Human validation on 9,600 annotations confirms 87% agreement with the automatic method.

## Paper Outline

1. Introduction - Gender bias in MT systems and motivation
2. Challenge Set for Gender Bias in MT - WinoMT composition and evaluation protocol
3. Evaluation - Experimental setup, results, fighting bias with bias, human validation
4. Discussion - Related work, limitations, future work
5. Conclusions - Summary of findings

## Methods Summary

The evaluation method consists of three steps: (1) translate all WinoMT sentences into the target language using each MT system, (2) align source and target words using fast_align trained on the automatic translations, and (3) extract the translated entity's gender using language-specific morphological analysis tools. For Romance languages (Spanish, French, Italian), spaCy is used for gendered noun-determiner agreement detection. For Slavic languages (Russian, Ukrainian), Korobov's morphological analyzer is employed. Arabic gender is identified via the ta marbuta character, Hebrew uses a dedicated analyzer, and German uses DEMorphy. The evaluation computes accuracy, gender gap, and stereotype gap metrics.

## Results Summary

All tested MT systems exhibit significant gender bias. Google Translate achieves the highest accuracy on German (59.4%) and Hebrew (53.7%), while SYSTRAN shows the largest gender gaps (up to 49.4% on Arabic). The stereotype gap is consistently positive across all systems and languages, with SYSTRAN showing the largest gap on Spanish (15.0%) and Google Translate on Hebrew (37.8%). The academic French model (Ott et al.) achieves only 49.4% accuracy with a 16.1% stereotype gap. Adding gendered adjectives improves Google Translate accuracy by 4.5-11.2 percentage points on Spanish, Russian, and Ukrainian. Human validation shows 87% average agreement with the automatic method (vs. 90% inter-annotator agreement), confirming the reliability of the evaluation pipeline.

## Conclusions

The authors acknowledge that WinoMT is composed of synthetic English sentences, which may introduce artificial biases. The dataset serves as a proxy estimation and could be augmented with natural "in the wild" instances from many source languages. The rudimentary debiasing scheme requires oracle coreference resolution and is impractical for real-world use. Future work should develop more gender-balanced MT models and extend the benchmark to more languages and natural text.

## Artifact Contributions

- **WinoMT Challenge Set**: 3,888-instance gender bias evaluation set for MT with evaluation code (https://github.com/gabrielStanovsky/mt_gender)

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** Foundational gender bias evaluation for French MT. Highlights that French default masculine forms affect gender translation accuracy.

## Tags

