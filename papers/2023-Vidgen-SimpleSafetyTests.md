---










key: HELM0001
type: document
short_title: "SimpleSafetyTests"
year: 2023
first_author: "[[Bertie Vidgen]]"
last_author: "[[Douwe Kiela]]"
authors: "Bertie Vidgen; Tristan Thrush; Zeerak Waseem; Douwe Kiela"
doi: "10.48550/arXiv.2311.08370"
url: "https://arxiv.org/abs/2311.08370"
external_pdf: "https://arxiv.org/pdf/2311.08370.pdf"
publication: "arXiv.org"
CONF-CC: "Preprint"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "AI Safety & Alignment, Benchmark, Evaluation, Dataset, LLM Safety, Toxic Content, Harm Detection"
key_contribution: "Introduces SimpleSafetyTests (SST), a benchmark of 100 prompts across five critical harm areas for rapidly identifying safety weaknesses in LLMs, along with 3,000 annotated model responses and an evaluation of five AI safety filters."
significance: "Provides a practical, openly-licensed evaluation tool that exposes significant safety gaps in widely-used open LLMs (up to 73% unsafe response rates), establishing a baseline for measuring safety progress and enabling cost-effective automated safety assessment."
tags: []
pdf_extract: "PDF Extracts/2023/2023-Vidgen-SimpleSafetyTests.md"
abstract: "The past year has seen rapid acceleration in the development of large language models (LLMs). However, without proper steering and safeguards, LLMs will readily follow malicious instructions, provide unsafe advice, and generate toxic content. We introduce SimpleSafetyTests (SST) as a new test suite for rapidly and systematically identifying such critical safety risks. The test suite comprises 100 test prompts across five harm areas that LLMs, for the vast majority of applications, should refuse to comply with. We test 11 open-access and open-source LLMs and four closed-source LLMs, and find critical safety weaknesses. While some of the models do not give a single unsafe response, most give unsafe responses to more than 20% of the prompts, with over 50% unsafe responses in the extreme. Prepending a safety-emphasising system prompt substantially reduces the occurrence of unsafe responses, but does not completely stop them from happening. Trained annotators labelled every model response to SST (n = 3,000). We use these annotations to evaluate five AI safety filters (which assess whether a models' response is unsafe given a prompt) as a way of automatically evaluating models' performance on SST. The filters' performance varies considerably. There are also differences across the five harm areas, and on the unsafe versus safe responses. The widely-used Perspective API has 72% accuracy and a newly-created zero-shot prompt to OpenAI's GPT-4 performs best with 89% accuracy. Content Warning: This paper contains prompts and responses that relate to child abuse, suicide, self-harm and eating disorders, scams and fraud, illegal items, and physical harm."
local_pdf: "[[PDFs/2023/2023-Vidgen-SimpleSafetyTests.pdf]]"
DATE_ADDED: 20260312
helm: "incorporated"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "AI Safety & Alignment"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
LLM_assessed: "Mistral, Llama-2, Falcon, Claude, Cohere"
DATA_URL: "https://github.com/bertiev/SimpleSafetyTests"
data_description: "100 handcrafted test prompts across 5 harm areas (child abuse, suicide/self-harm/eating disorders, physical harm, illegal items, scams/fraud); 3,000 annotated model responses from 15 LLMs"
data_metrics: "100 prompts, 15 LLMs evaluated, 3000 labeled responses, 5 safety filters assessed"
---
