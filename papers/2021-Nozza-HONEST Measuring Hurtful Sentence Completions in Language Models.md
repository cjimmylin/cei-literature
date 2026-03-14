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
national_ethnic_cultural: "Multicultural/Cross-cultural"
cultures_nationalities_list: "Multicultural/Cross-cultural"
languages_list: "English, French, Italian, Portuguese, Romanian, Spanish"
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
newtags: "bias-evaluation, gender-bias, language-models, hurtful-language, benchmark, multilingual, stereotype, NLP"
key_contribution: "Introduces HONEST, a template- and lexicon-based benchmark score for measuring hurtful gendered sentence completions across six language models and six languages."
significance: "Provides the first systematic multilingual evaluation of explicitly hurtful stereotypes in language model text generation, revealing that gendered harm is pervasive and language-specific."
tags: []
pdf_extract: "PDF Extracts/2021/2021-Nozza-HONEST Measuring Hurtful Sentence Completions in Language Models.md"
abstract: "Language models have revolutionized the field of NLP. However, language models capture and proliferate hurtful stereotypes, especially in text generation. Our results show that 4.3% of the time, language models complete a sentence with a hurtful word. These cases are not random, but follow language and gender-specific patterns. We propose a score to measure hurtful sentence completions in language models (HONEST). It uses a systematic template- and lexicon-based bias evaluation methodology for six languages. Our findings suggest that these models replicate and amplify deep-seated societal stereotypes about gender roles. Sentence completions refer to sexual promiscuity when the target is female in 9% of the time, and in 4% to homosexuality when the target is male. The results raise questions about the use of these models in production settings."
local_pdf: "[[PDFs/2021/2021-Nozza-HONEST Measuring Hurtful Sentence Completions in Language Models.pdf]]"
DATE_ADDED: 20260312
helm: "incorporated"
ethics_overall: 90
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
LLM_assessed: "BERT, GPT-2"
DATA_URL: "https://github.com/MilaNLProc/honest"
data_description: "Manually-created cloze sentence templates for six languages (English, Italian, French, Portuguese, Romanian, Spanish) paired with a hurtful-word lexicon to measure gendered stereotype bias in BERT and GPT-2 completions"
data_metrics: "HONEST score (proportion of hurtful sentence completions per language model)"
ethics_perspective: "AI Safety & Alignment"
---
