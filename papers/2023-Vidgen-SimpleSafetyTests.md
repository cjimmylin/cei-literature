---
key: HELM0001
type: document
short_title: SimpleSafetyTests
year: 2025
first_author: "[[Bertie Vidgen]]"
last_author: "[[Douwe Kiela]]"
authors: "Bertie Vidgen; Tristan Thrush; Zeerak Waseem; Douwe Kiela"
doi: 10.48550/arXiv.2311.08370
url: "https://arxiv.org/abs/2311.08370"
external_pdf: "https://arxiv.org/pdf/2311.08370.pdf"
publication: arXiv.org
CONF-CC: Preprint
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: English
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
newtags: "AI Safety & Alignment, Benchmark, Evaluation, Dataset, LLM Safety, Toxic Content, Harm Detection"
key_contribution: "Introduces SimpleSafetyTests (SST), a benchmark of 100 prompts across five critical harm areas for rapidly identifying safety weaknesses in LLMs, along with 3,000 annotated model responses and an evaluation of five AI safety filters."
significance: "Provides a practical, openly-licensed evaluation tool that exposes significant safety gaps in widely-used open LLMs (up to 73% unsafe response rates), establishing a baseline for measuring safety progress and enabling cost-effective automated safety assessment."
tags: []
pdf_extract: "PDF Extracts/2023/2023-Vidgen-SimpleSafetyTests.md"
abstract: "The past year has seen rapid acceleration in the development of large language models (LLMs). However, without proper steering and safeguards, LLMs will readily follow malicious instructions, provide unsafe advice, and generate toxic content. We introduce SimpleSafetyTests (SST) as a new test suite for rapidly and systematically identifying such critical safety risks. The test suite comprises 100 test prompts across five harm areas that LLMs, for the vast majority of applications, should refuse to comply with. We test 11 open-access and open-source LLMs and four closed-source LLMs, and find critical safety weaknesses. While some of the models do not give a single unsafe response, most give unsafe responses to more than 20% of the prompts, with over 50% unsafe responses in the extreme. Prepending a safety-emphasising system prompt substantially reduces the occurrence of unsafe responses, but does not completely stop them from happening. Trained annotators labelled every model response to SST (n = 3,000). We use these annotations to evaluate five AI safety filters (which assess whether a models' response is unsafe given a prompt) as a way of automatically evaluating models' performance on SST. The filters' performance varies considerably. There are also differences across the five harm areas, and on the unsafe versus safe responses. The widely-used Perspective API has 72% accuracy and a newly-created zero-shot prompt to OpenAI's GPT-4 performs best with 89% accuracy. Content Warning: This paper contains prompts and responses that relate to child abuse, suicide, self-harm and eating disorders, scams and fraud, illegal items, and physical harm."
local_pdf: [[Lit-WS-Lit-WS-PDFs/2023/2023-Vidgen-SimpleSafetyTests.pdf]]
DATE_ADDED: 20260312
helm: incorporated
ethics_overall: No
virtue_ethics: 0
deontological_ethics: 5
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
LLM_assessed: "Mistral, Llama-2, Falcon, Claude, Cohere"
DATA_URL: "https://github.com/bertiev/SimpleSafetyTests"
ethics_perspective: "AI Safety & Alignment"
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
weird_score: 80
is_benchmark: Unknown
is_eval: Unknown
is_dataset: Unknown
data_description: Unknown
data_metrics: Unknown
---
