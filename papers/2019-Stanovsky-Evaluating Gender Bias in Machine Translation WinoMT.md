---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0448
type: conferencePaper
short_title: Evaluating Gender Bias in Machine Translation (WinoMT)
year: 2019
first_author: "[[Gabriel Stanovsky]]"
last_author: "[[Luke Zettlemoyer]]"
authors: Gabriel Stanovsky, Noah A. Smith, Luke Zettlemoyer
url: "https://aclanthology.org/P19-1164/"
external_pdf: "https://arxiv.org/pdf/1906.00591v1.pdf"
publication: ACL Anthology
local_pdf: "[[PDFs/2019/2019-Stanovsky-Evaluating Gender Bias in Machine Translation WinoMT.pdf]]"
pdf_extract: "PDF Extracts/2019/2019-Stanovsky-Evaluating Gender Bias in Machine Translation WinoMT.md"
DATE_ADDED: 20260213
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
languages_list: "Arabic, Czech, English, French, Hebrew, Italian, Polish, Russian, Spanish, Ukrainian"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation approach"
data_metrics: "Not specified"
LLM_assessed: "NA"
DATA_URL: "https://github.com/gabrielStanovsky/mt_gender"
tags: 
abstract:
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

WinoMT challenge set of 3,888 English segments for evaluating gender bias in machine translation to 8+ languages. Tests four commercial MT systems (Google Translate, Microsoft Translator, Amazon Translate, SYSTRAN) and two academic MT models, not LLMs. Uses morphological analysis to detect gender bias in translations.


## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** Foundational gender bias evaluation for French MT. Highlights that French default masculine forms affect gender translation accuracy.

## Tags

