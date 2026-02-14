---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0445
type: preprint
short_title: Improving Methodologies for LLM Evaluations Across Global Languages
year: 2025
first_author: "[[INESIA (Singapore AISI-led international collaboration)]]"
last_author: "[[INESIA (Singapore AISI-led international collaboration)]]"
authors: INESIA (Singapore AISI-led international collaboration)
url: "https://arxiv.org/abs/2601.15706"
external_pdf: "https://arxiv.org/pdf/2601.15706.pdf"
publication: arXiv
local_pdf: "[[PDFs/2025/2025-collaboration-Improving Methodologies for LLM Evaluations Across Global Languages.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-collaboration-Improving Methodologies for LLM Evaluations Across Global Languages.md"
DATE_ADDED: 20260213
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
languages_list: "Cantonese, English, Farsi, French, Japanese, Kiswahili, Korean, Malay, Mandarin Chinese, Telugu"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation approach"
data_metrics: "Not specified"
LLM_assessed: "2 open-weight models"
DATA_URL: "NA"
tags: 
abstract:
research_topic: "Other"
---
# Improving Methodologies for LLM Evaluations Across Global Languages

## Authors

[[INESIA (Singapore AISI-led international collaboration)]]

## Metadata

**Authors:** INESIA (Singapore AISI-led international collaboration)

**Year:** 2025

**Type:** preprint

**Venue:** arXiv

**Languages:** Cantonese, English, Farsi, French, Japanese, Kiswahili, Korean, Malay, Mandarin Chinese, Telugu

## Links

- **arXiv:** https://arxiv.org/abs/2601.15706

## Abstract

Joint multilingual evaluation exercise by international AI safety institutes (Singapore, Japan, Australia, Canada, EU, France, Kenya, South Korea, UK). Tested 2 open-weight models across 10 languages with over 6,000 prompts across 5 harm categories. French INESIA (ANSSI, Inria, LNE, PEReN) participated. Finds jailbreaking is a common weakness for non-English languages.

## Summary

This paper reports on a joint multilingual evaluation exercise conducted by international AI safety institutes from Singapore, Japan, Australia, Canada, EU, France, Kenya, South Korea, and the UK. Testing 2 open-weight models across 10 languages (including Cantonese, French, Japanese, Korean, Mandarin Chinese, and others) with over 6,000 prompts across 5 harm categories (privacy, crime, intellectual property, jailbreak robustness), the study identifies jailbreaking as a common weakness for non-English languages. The collaborative effort represents a significant international coordination on AI safety evaluation methodologies.

## Data Description

Joint multilingual evaluation exercise by international AI safety institutes (including France's INESIA) testing 2 open-weight models across 10 languages with over 6,000 prompts across 5 harm categories (privacy, crime, intellectual property, jailbreak robustness). Finds jailbreaking is a common weakness for non-English languages.


## Detailed Summary

This paper reports on a joint multilingual safety testing exercise conducted by participants across the International Network for Advanced AI Measurement, Evaluation and Science (INESIA), with Singapore AISI leading the effort. Representatives from Singapore, Japan, Australia, Canada, European Union, France, Kenya, South Korea, and the UK AI Security Institute tested two open-weight models -- Mistral Large and Gemma 2 (27B) -- across ten languages: Cantonese, English, Farsi, French, Japanese, Kiswahili, Korean, Malay, Mandarin Chinese, and Telugu. Over 6,000 prompts were newly translated for the exercise, testing safeguard effectiveness across five harm categories: privacy, non-violent crime, violent crime, intellectual property, and robustness to jailbreaking. The testing datasets comprised subsets from MLCommons AILuminate (400 prompts), AnswerCarefully from Japan's NII-LLMC (48 prompts), and CyberSecEval Prompt Injection from Meta's Purple Llama (251 prompts). Evaluations included both LLM-as-a-judge and human annotations conducted independently by each AISI. Key findings include: non-English safeguards tend to lag behind English (especially for jailbreaking), refusals in most languages include reasoning or ethical alternatives, and LLM-as-a-judge shows promise but requires human oversight for subtle cases. Language-specific behaviors include mixed-language outputs, warnings accompanied by partial harmful instructions, and culturally varying refusal assertiveness.

## Paper Outline

1. Contributors
2. Executive Summary - Key findings and methodological learnings
3. Scope of the Exercise - Test objectives, design, harm categories
4. Methodology - Dataset selection, translation, evaluation pipeline
5. Limitations - Translation quality, single-run tests, annotator pool
6. Safety Findings - Safeguard effectiveness, refusal quality, evaluator effectiveness
7. Methodological Findings - Lessons for multilingual evaluation
8. Potential Learnings for Model Developers
9. Language Deep Dives - Cantonese, Farsi, French, Japanese, Kiswahili, Korean, Malay, Mandarin Chinese, Telugu
10. Conclusion
Annexes: Prompt examples, translation guidelines, evaluation criteria, annotation guidelines

## Methods Summary

Three test datasets covering five harm categories are translated into 10 languages and presented to two test LLMs. Responses are assessed for acceptability (safety and relevance) and whether they constitute refusals, using harm-category-specific acceptance criteria. Evaluation uses both an LLM-as-a-judge and independent human annotations from each participating AISI. Singapore AISI ran tests for all ten languages, while Australia and Japan ran independent tests in Mandarin Chinese and Japanese to assess inference environment impact. The methodology measures acceptability rate, refusal rate, and discrepancy rate between automated and human evaluation.

## Results Summary

Non-English safeguards lag slightly behind English, with jailbreak protections being the weakest and intellectual property violation safeguards being stronger. Refusals in most languages include reasoning or ethical alternatives rather than bare rejections. LLM-as-a-judge shows promise as a baseline evaluator but human oversight remains necessary for subtle or mixed-signal harms. Language-specific findings include: mixed-language outputs in all languages except English and French; warnings accompanied by partial harmful instructions in Cantonese, Malay, Mandarin, Telugu, and Kiswahili; increased hallucinations/gibberish in lower-resourced languages (Farsi, Telugu, Kiswahili); and culturally-appropriate refusal styles in French, Korean, Japanese, and Farsi that avoid direct rejections.

## Conclusions

The exercise establishes a common approach for multilingual safety testing of frontier models at scale. Key methodological learnings include: prompts should be contextually adapted (not literally translated), evaluator models need stress-testing with variations, human annotation guidelines need clarification for ambiguous cases, and multiple test runs are needed for reproducibility. The AISIs commit to continued collaboration to advance trustworthy, reliable, and secure multilingual AI systems.

## Artifact Contributions

- **Methodology:** Common approach for multilingual safety evaluation across 10 languages and 5 harm categories
- **Findings:** Comprehensive safety evaluation of Mistral Large and Gemma 2 across 10 languages with both automated and human evaluation
- **Guidelines:** Translation guidelines, evaluation criteria, and annotation guidelines for multilingual safety testing

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** Official French AI safety institute (INESIA) participated. Evaluates French LLM safety across privacy, crime, IP, and jailbreak robustness categories.

## Tags

