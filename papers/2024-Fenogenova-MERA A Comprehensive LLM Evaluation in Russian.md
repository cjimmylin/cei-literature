---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: IQP7N9JR
type: document
short_title: "MERA: A Comprehensive LLM Evaluation in Russian"
year: 2024
first_author: "[[Alena Fenogenova]]"
last_author: "[[Markov, Sergey]]"
authors: "[[Fenogenova, Alena]]; [[Chervyakov, Artem]]; [[Martynov, Nikita]]; [[Kozlova, Anastasia]]; [[Tikhonova, Maria]]; [[Akhmetgareeva, Albina]]; [[Emelyanov, Anton]]; [[Shevelev, Denis]]; [[Lebedev, Pavel]]; [[Sinev, Leonid]]; [[Isaeva, Ulyana]]; [[Kolomeytseva, Katerina]]; [[Moskovskiy, Daniil]]; [[Goncharova, Elizaveta]]; [[Savushkin, Nikita]]; [[Mikhailova, Polina]]; [[Minaeva, Anastasia]]; [[Dimitrov, Denis]]; [[Panchenko, Alexander]]; [[Markov, Sergey]]"
url: "https://aclanthology.org/2024.acl-long.534/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/6ESQLWPZ/2024 - MERA A Comprehensive LLM Evaluation in Russian.pdf"
national_ethnic_cultural: "Russian"
cultures_nationalities_list: "Russian"
languages_list: "Russian"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Russian, General Ethics"
key_contribution: "Introduced MERA, a comprehensive instruction-tuning benchmark for *Russian* LLMs, covering 21 tasks including ethics and safety."
significance: "The primary benchmark for the Russian AI ecosystem, revealing that Russian open models still lag behind closed Western models (GPT-4) and human performance."
tags: 
abstract: "Over the past few years, one of the most notable advancements in AI research has been in foundation models (FMs), headlined by the rise of language models (LMs). However, despite researchers’ attention and the rapid growth in LM application, the capabilities, limitations, and associated risks still need to be better understood. To address these issues, we introduce a new instruction benchmark, MERA, oriented towards the FMs’ performance on the Russian language."
CONF-CC: "N/A"
DATE_ADDED: 20260208
LLM_assessed: "Llama-2, Mistral"
DATA_URL: "https://github.com/ai-forever/MERA"
pdf_extract: "PDF Extracts/2024/2024-Fenogenova-MERA A Comprehensive LLM Evaluation in Russian.md"
local_pdf: "[[PDFs/2024/2024-Fenogenova-MERA A Comprehensive LLM Evaluation in Russian.pdf]]"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "General Ethics"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark for moral/ethical reasoning"
data_metrics: "Not specified"
CONFERENCE: "ACL 2024"
---
# MERA: A Comprehensive LLM Evaluation in Russian

## Authors

[[Alena Fenogenova|Fenogenova, Alena]], [[Artem Chervyakov|Chervyakov, Artem]], [[Nikita Martynov|Martynov, Nikita]], [[Anastasia Kozlova|Kozlova, Anastasia]], [[Maria Tikhonova|Tikhonova, Maria]], [[Albina Akhmetgareeva|Akhmetgareeva, Albina]], [[Anton Emelyanov|Emelyanov, Anton]], [[Denis Shevelev|Shevelev, Denis]], [[Pavel Lebedev|Lebedev, Pavel]], [[Leonid Sinev|Sinev, Leonid]], [[Ulyana Isaeva|Isaeva, Ulyana]], [[Katerina Kolomeytseva|Kolomeytseva, Katerina]], [[Daniil Moskovskiy|Moskovskiy, Daniil]], [[Elizaveta Goncharova|Goncharova, Elizaveta]], [[Nikita Savushkin|Savushkin, Nikita]], [[Polina Mikhailova|Mikhailova, Polina]], [[Anastasia Minaeva|Minaeva, Anastasia]], [[Denis Dimitrov|Dimitrov, Denis]], [[Alexander Panchenko|Panchenko, Alexander]], [[Sergey Markov|Markov, Sergey]]

## Links

- **ACL Anthology:** https://aclanthology.org/2024.acl-long.534/

## Abstract

Over the past few years, one of the most notable advancements in AI research has been in foundation models (FMs), headlined by the rise of language models (LMs). However, despite researchers’ attention and the rapid growth in LM application, the capabilities, limitations, and associated risks still need to be better understood. To address these issues, we introduce a new instruction benchmark, MERA, oriented towards the FMs’ performance on the Russian language. The benchmark encompasses 21 evaluation tasks for generative models covering 10 skills and is supplied with private answer scoring to prevent data leakage. The paper introduces a methodology to evaluate FMs and LMs in fixed zero- and few-shot instruction settings that can be extended to other modalities. We propose an evaluation methodology, an open-source code base for the MERA assessment, and a leaderboard with a submission system. We evaluate open LMs as baselines and find they are still far behind the human level. We publicly release MERA to guide forthcoming research, anticipate groundbreaking model features, standardize the evaluation procedure, and address potential ethical concerns and drawbacks.

## Data Description

MERA is a comprehensive instruction-format benchmark for evaluating LLMs and foundation models in Russian, comprising 21 tasks covering 10 skills across problem-solving, exam-based, and ethics categories. The benchmark includes a private test scoring system, an open leaderboard, and was used to evaluate open LMs including Llama-2 (7B and 13B), Mistral-7B, and several Russian-specific models as baselines. The dataset includes over 80,000 examples across all tasks with multiple prompt templates per task.


## Notes

