---








key: HELM0002
type: conferencePaper
short_title: "HONEST"
year: 2021
first_author: "[[Debora Nozza]]"
last_author: "[[Dirk Hovy]]"
authors: "Debora Nozza; Federico Bianchi; Dirk Hovy"
url: "https://aclanthology.org/2021.naacl-main.191/"
external_pdf: "https://aclanthology.org/2021.naacl-main.191.pdf"
publication: "NAACL-HLT 2021"
CONF-CC: "NAACL 2021"
national_ethnic_cultural: ""
languages_list: ""
religious_values: ""
moral_psychology: "N/A"
newtags: "bias-evaluation, gender-bias, language-models, hurtful-language, benchmark, multilingual, stereotype, NLP"
key_contribution: "Introduces HONEST, a template- and lexicon-based benchmark score for measuring hurtful gendered sentence completions across six language models and six languages."
significance: "Provides the first systematic multilingual evaluation of explicitly hurtful stereotypes in language model text generation, revealing that gendered harm is pervasive and language-specific."
tags: []
pdf_extract: "PDF Extracts/2021/2021-Nozza-HONEST Measuring Hurtful Sentence Completions in Language Models.md"
abstract: "Language models have revolutionized the field of NLP. However, language models capture and proliferate hurtful stereotypes, especially in text generation. Our results show that 4.3% of the time, language models complete a sentence with a hurtful word. These cases are not random, but follow language and gender-specific patterns. We propose a score to measure hurtful sentence completions in language models (HONEST). It uses a systematic template- and lexicon-based bias evaluation methodology for six languages. Our findings suggest that these models replicate and amplify deep-seated societal stereotypes about gender roles. Sentence completions refer to sexual promiscuity when the target is female in 9% of the time, and in 4% to homosexuality when the target is male. The results raise questions about the use of these models in production settings."
local_pdf: "[[PDFs/2021/2021-Nozza-HONEST Measuring Hurtful Sentence Completions in Language Models.pdf]]"
DATE_ADDED: 20260312
helm: "incorporated"
ethics_overall: "Yes"
ethics_perspective: "Bias & Fairness"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Manually-created cloze sentence templates for six languages (English, Italian, French, Portuguese, Romanian, Spanish) paired with a hurtful-word lexicon to measure gendered stereotype bias in BERT and GPT-2 completions"
data_metrics: "HONEST score (proportion of hurtful sentence completions per language model)"
---
