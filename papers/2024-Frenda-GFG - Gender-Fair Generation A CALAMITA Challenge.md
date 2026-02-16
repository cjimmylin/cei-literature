---





Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0505
type: preprint
short_title: "GFG -- Gender-Fair Generation: A CALAMITA Challenge"
year: 2024
first_author: "[[Simona Frenda]]"
last_author: "[[Luisa Bentivogli Matteo Negri]]"
authors: "Simona Frenda, Andrea Piergentili, Beatrice Savoldi, Marco Madeddu, Martina Rosola, Silvia Casola, Chiara Ferrando, Viviana Patti, Matteo Negri, Luisa Bentivogli"
url: "https://arxiv.org/abs/2412.19168"
external_pdf: "https://arxiv.org/pdf/2412.19168.pdf"
publication: "arXiv / CLiC-it 2024"
pdf_extract: "PDF Extracts/2024/2024-Frenda-GFG - Gender-Fair Generation A CALAMITA Challenge.md"
local_pdf: "[[PDFs/2024/2024-Frenda-GFG - Gender-Fair Generation A CALAMITA Challenge.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "Italian"
cultures_nationalities_list: "Italian"
languages_list: "English, Italian"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: "GPT-3.5, GPT-4, LLaMa-2, Mistral"
DATA_URL: "https://github.com/dhfbk/gfg-calamita"
tags: 
abstract: "Gender-fair language aims at promoting gender equality by using terms and expressions that include all identities and avoid reinforcing gender stereotypes. Implementing gender-fair strategies is particularly challenging in heavily gender-marked languages, such as Italian. To address this, the Gender-Fair Generation challenge intends to help shift toward gender-fair language in written communication."
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Bias & Fairness"
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Text corpus"
data_metrics: "Not specified"
---
# GFG -- Gender-Fair Generation: A CALAMITA Challenge

## Authors

[[Andrea Piergentili Simona Frenda]], [[Marco Madeddu Beatrice Savoldi]], [[Silvia Casola Martina Rosola]], [[Viviana Patti Chiara Ferrando]], [[Luisa Bentivogli Matteo Negri]]

## Metadata

**Authors:** Simona Frenda, Andrea Piergentili, Beatrice Savoldi, Marco Madeddu, Martina Rosola, Silvia Casola, Chiara Ferrando, Viviana Patti, Matteo Negri, Luisa Bentivogli

**Year:** 2024

**Type:** preprint

**Venue:** arXiv / CLiC-it 2024

**Languages:** English, Italian

**Benchmark:** GFG (Gender-Fair Generation)

## Links

- **arXiv:** https://arxiv.org/abs/2412.19168

## Abstract

Challenge to assess and monitor recognition and generation of gender-fair language in Italian. Includes three tasks: detection of gendered expressions, reformulation into gender-fair alternatives, and generation of gender-fair language in English-to-Italian translation. Uses GFL-it corpus, GeNTE, and Neo-GATE datasets.

## Summary

This paper presents the Gender-Fair Generation (GFG) challenge, part of the CALAMITA shared task series, designed to assess and promote recognition and generation of gender-fair language in Italian, a heavily gender-marked language. The challenge comprises three tasks: detection of gendered expressions, reformulation into gender-fair alternatives, and generation of gender-fair language in English-to-Italian translation, using three datasets (GFL-it corpus, GeNTE, and Neo-GATE). The authors evaluate multiple language models including GPT-3.5, GPT-4, LLaMa-2, and Mistral on occupation-based prompts that test for stereotypical gendered continuations. The work addresses the challenge of implementing gender-fair strategies in languages with extensive grammatical gender marking and includes evaluation of non-binary neomorphemes in Italian.

## Data Description

GFG (Gender-Fair Generation) challenge dataset for evaluating gender bias in Italian text generation. Includes occupation-based prompts testing for stereotypical gendered continuations in Italian language models. Part of CALAMITA shared task series.


## Detailed Summary

This paper presents the Gender-Fair Generation (GFG) challenge, part of the CALAMITA 2024 shared task series at CLiC-it 2024, designed to assess and promote recognition and generation of gender-fair language in Italian, a heavily gender-marked language where the masculine generic is used for mixed-gender groups, unknown individuals, and genderqueer people, making women and non-binary identities linguistically invisible. The challenge is structured into three tasks: (1) gendered language detection, identifying referentially gender-marked expressions within Italian sentences including overextended masculine, generic masculine, and incongruous gender; (2) fair reformulation, rewriting gendered expressions into gender-fair alternatives using conservative obscuration (gender-neutral periphrasis) or innovative obscuration (neomorphemes like the schwa "@"); and (3) fair translation, generating gender-fair language in English-to-Italian machine translation. The challenge relies on three annotated datasets: GFL-it (2,170 texts from University of Brescia administrative documents annotated by 5 expert annotators identifying 4,311 unfair spans), GeNTE (1,500 English-Italian sentence triplets from Europarl with gendered and gender-neutral references), and Neo-GATE (841 entries designed to evaluate non-binary neomorpheme use in Italian). The total evaluation covers 3,011 entries for detection, 2,806 for reformulation, and 2,341 for translation.

## Paper Outline

1. Challenge: Introduction and Motivation - Gender-fair language in Italian, effects of masculine generics, NLP perpetuation of unfair practices
2. Challenge: Description - Three tasks (detection, reformulation, translation), gendered language types, obscuration strategies
3. Data Description - GFL-it corpus (University of Brescia), GeNTE (Europarl subset), Neo-GATE (neomorpheme evaluation)
4. Metrics - BERTScore F1 for detection, accuracy via gender-neutral classifier for reformulation, coverage-weighted accuracy for neomorpheme tasks
5. Limitations - Domain-specific datasets, single neomorpheme paradigm tested, no mixed-text scenarios
6. Ethical Issues - Annotator gender balance, neomorpheme accessibility for dyslexia/visual impairments

## Methods Summary

The three tasks use distinct evaluation metrics tailored to their objectives. Task 1 (detection) uses the average F1-score computed via BERTScore for each entry, extracting maximum correspondence between annotator-identified and model-generated gendered expressions. Task 2 (reformulation) and Task 3 (translation) use accuracy based on labels from a gender-neutral classifier (version 2 from Savoldi et al. 2024), comparing classifier-assigned labels (gendered vs. gender-neutral) against ground truth. For neomorpheme-based evaluation (using Neo-GATE), the coverage-weighted accuracy accounts for both generation accuracy and the proportion of annotations found during evaluation, while a mis-generation score flags inappropriate neomorpheme application to non-human referents. Seven prompts (A-G) are designed across the datasets, with prompts following few-shot formats inspired by prior work, using Italian instruction tags like [Genere marcato], [Neutro], and [Neomorfema]. The schwa-simple paradigm maps 30+ grammatical categories to neomorpheme forms.

## Results Summary

The paper presents the challenge design and evaluation framework rather than comprehensive model evaluation results, as it serves as a task description paper for the CALAMITA shared task. The evaluation infrastructure enables systematic assessment of how well language models can detect, reformulate, and translate gender-fair language in Italian. Previous related experiments on the component datasets demonstrated that current MT and generation systems struggle significantly with gender-neutral and neomorpheme-based outputs in Italian, particularly in handling the complex morphological agreement system required across articles, adjectives, pronouns, and nouns. The GFL-it annotation reveals that overextended masculine (3,772 instances) vastly outnumbers generic (597) and incongruous gender (31) in Italian administrative texts.

## Conclusions

The GFG challenge addresses a critical gap in evaluating gender-fair language capabilities of NLP systems for Italian. Key limitations include the domain-specific nature of the datasets (administrative documents, European Parliament proceedings, expert-created sentences), testing only the schwa-simple neomorpheme paradigm among many possibilities (asterisk, -u, @), and the absence of mixed-text scenarios where rewriting is needed for some entities but not others. Ethical considerations include the non-gender-balanced annotator pool (2 of 5 men) for GFL-it and the accessibility challenges that neomorphemes like the schwa pose for people with dyslexia or visual impairments, mitigated by the possibility of selecting alternative neomorpheme paradigms compatible with screen readers. The challenge represents a first systematic attempt to benchmark gender-fair language generation capabilities in a heavily gender-marked language.

## Artifact Contributions

- **GFL-it Corpus**: 2,170 Italian administrative texts annotated by 5 experts for gendered expressions and conservative obscuration alternatives (https://github.com/simonasnow/GFL-it-Dataset)
- **GeNTE Integration**: 1,500 English-Italian sentence triplets for gender-neutral translation evaluation (https://huggingface.co/datasets/FBK-MT/GeNTE)
- **Neo-GATE Integration**: 841 entries for neomorpheme evaluation in Italian (https://huggingface.co/datasets/FBK-MT/Neo-GATE)
- **GFG Challenge Framework**: Three-task evaluation suite with 7 prompts and task-specific metrics (https://github.com/dhfbk/gfg-calamita)

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B8
**Relevance:** Directly addresses gender bias and fairness in Italian language generation by LLMs, including evaluation of non-binary neomorphemes.

## Tags

