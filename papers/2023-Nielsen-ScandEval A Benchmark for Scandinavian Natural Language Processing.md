---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0478
type: preprint
short_title: "ScandEval: A Benchmark for Scandinavian Natural Language Processing"
year: 2025
first_author: "[[Nielsen, Dan]]"
last_author: "[[Nielsen, Dan]]"
authors: "[[Nielsen, Dan]]"
authors_incomplete: true
url: "https://arxiv.org/abs/2304.00906"
external_pdf: "https://arxiv.org/pdf/2304.00906.pdf"
publication: "arXiv / NoDaLiDa 2023"
pdf_extract: "PDF Extracts/2023/2023-Nielsen-ScandEval A Benchmark for Scandinavian Natural Language Processing.md"
local_pdf: "[[PDFs/2023/2023-Nielsen-ScandEval A Benchmark for Scandinavian Natural Language Processing.pdf]]"
DATE_ADDED: 20260213
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
national_ethnic_cultural: N/A
languages_list: "Danish, Faroese, Icelandic, Norwegian, Swedish"
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: 
is_benchmark: Yes
is_eval: No
is_dataset: Yes
data_description: "Multilingual benchmark dataset for question answering"
data_metrics: "Not specified"
LLM_assessed: "NB-BERT, KB-BERT, DFM-encoder, RemBERT, mDeBERTaV3, Scandinavian BERT variants"
DATA_URL: "https://github.com/saattrupdan/ScandEval"
tags: 
abstract: "This paper introduces a Scandinavian benchmarking platform, ScandEval, which can benchmark any pretrained model on four different tasks in the Scandinavian languages. The datasets used in two of the tasks, linguistic acceptability and question answering, are new. We develop and release a Python package and command-line interface, scandeval, which can benchmark any model that has been uploaded to the Hugging Face Hub, with reproducible results."
research_topic: "Machine Translation"
---
# ScandEval: A Benchmark for Scandinavian Natural Language Processing

## Authors

[[Dan Nielsen et al.]]

## Metadata

**Authors:** Dan Nielsen et al.

**Year:** 2023

**Type:** preprint

**Venue:** arXiv / NoDaLiDa 2023

**Languages:** Danish, Faroese, Icelandic, Norwegian, Swedish

**Benchmark:** ScandEval

## Links

- **arXiv:** https://arxiv.org/abs/2304.00906
- **Code/Data:** https://github.com/EuroEval/EuroEval

## Abstract

Benchmarking platform for Scandinavian languages across 4 NLP tasks with new linguistic acceptability and QA datasets. Evaluates 100+ models. Shows substantial cross-lingual transfer among Mainland Scandinavian but limited transfer with Icelandic/Faroese. Evolved into EuroEval.

## Summary

This paper introduces ScandEval, a comprehensive benchmarking platform for Scandinavian Natural Language Processing covering Danish, Swedish, Norwegian, Icelandic, and Faroese. The platform evaluates pretrained models on four tasks including text classification, named entity recognition, linguistic acceptability, and question answering, with two new datasets (ScandiQA for question answering and ScaLA for linguistic acceptability). The authors benchmark over 100 Scandinavian and multilingual models using a Python package and CLI tool, presenting results on an interactive online leaderboard. Analysis reveals substantial cross-lingual transfer among Mainland Scandinavian languages (Danish, Swedish, Norwegian) but limited transfer with Insular Scandinavian languages (Icelandic, Faroese), and shows that dedicated Nordic language models outperform massively multilingual models like XLM-RoBERTa and mDeBERTaV3.

## Data Description

ScandEval benchmark for evaluating NLP models across 4 Scandinavian languages (Danish, Swedish, Norwegian Bokmål, Norwegian Nynorsk) plus Icelandic and Faroese. Covers 4 task types: text classification, named entity recognition, question answering, and linguistic acceptability.


## Detailed Summary

This paper introduces ScandEval, a comprehensive benchmarking platform for Scandinavian Natural Language Processing that evaluates pretrained models across four tasks in Danish, Swedish, Norwegian (Bokmaal and Nynorsk), Icelandic, and Faroese. The benchmark addresses the proliferation of monolingual Scandinavian language models by providing a standardized, reproducible evaluation framework. Two new datasets are contributed: ScaLA (Scandinavian Linguistic Acceptability) constructed from Universal Dependencies treebanks with controlled corruption strategies, and ScandiQA (Scandinavian Question Answering) built from the MKQA dataset with translated context paragraphs.

The authors benchmark over 100 models and present results on an interactive online leaderboard. Cross-lingual transfer experiments confirm two key hypotheses: (1) substantial transfer exists among Mainland Scandinavian languages (Danish, Swedish, Norwegian), with the benchmark group {da, no, sv} achieving the highest F-statistic of 33.34; and (2) limited transfer exists between Mainland and Insular Scandinavian languages (Icelandic, Faroese). NB-BERT-large achieves the best overall performance, DFM-encoder-large-v1 leads for Danish, and KB-BERT-large for Swedish, all outperforming massively multilingual models like XLM-RoBERTa and mDeBERTaV3, demonstrating that investment in language-specific technology yields dividends.

## Paper Outline

1. Introduction - Motivation and hypotheses about cross-lingual transfer
2. Related Work - Non-English NLU benchmarks
3. Methodology - Finetuning setup, bootstrapping evaluation, cross-lingual transfer measurement, uniform dataset construction
4. ScandEval Tasks - NER, sentiment classification, linguistic acceptability (ScaLA), question answering (ScandiQA), inference speed
5. Benchmarking Package and CLI
6. Experiments - Benchmarking results and cross-lingual transfer analysis
7. Discussion
8. Conclusion

## Methods Summary

Models are fine-tuned with a learning rate of 2e-5, 100 warmup steps, batch size 32, AdamW optimizer, and linear learning rate schedule. Each model-dataset combination is evaluated 10 times with different random seeds on bootstrapped test sets, yielding mean scores with 95% confidence intervals. All datasets are uniformized to 1,024 training / 256 validation / 2,048 test samples. Cross-lingual transfer is measured using F-statistics from clustering benchmark scores of representative monolingual models from each language against a control group of non-Scandinavian languages (English, German, Dutch, Finnish, Russian, Arabic). Approximately 1,000 GPU hours on GeForce RTX 2080 Ti were required.

## Results Summary

NB-BERT-large (Norwegian) ranks first overall and in Norwegian; DFM-encoder-large-v1 leads in Danish; KB-BERT-large leads in Swedish. The Norwegian model appears in the top 2 across all three Mainland languages, indicating strong cross-lingual transfer. The cross-lingual experiment yields the highest F-statistic (33.34) for the {da, no, sv} group, confirming Mainland Scandinavian cohesion. Adding Insular languages reduces cohesion: {da, no, sv, fo} yields 25.40, while {da, no, sv, is} drops to 6.97. Dedicated Nordic models outperform massively multilingual models like RemBERT and mDeBERTaV3.

## Conclusions

The results indicate that investing in language-specific models at the Scandinavian level is worthwhile, and a joint Mainland Scandinavian approach could further improve results. Limitations include the translated nature of ScandiQA potentially favoring multilingual models, and the conservative approach to ScaLA corruption that may miss some grammatically incorrect constructions. Future work includes expanding to more tasks and investigating joint Scandinavian model training.

## Artifact Contributions

- **ScandEval Python Package and CLI**: Benchmarking tool for any model on the Hugging Face Hub (https://github.com/saattrupdan/ScandEval)
- **ScaLA Dataset**: Linguistic acceptability datasets for 6 Scandinavian languages (https://huggingface.co/ScandEval)
- **ScandiQA Dataset**: Question answering datasets for Mainland Scandinavian languages (https://huggingface.co/datasets/alexandrainst/scandi-qa)
- **Online Leaderboard**: Interactive results display (https://scandeval.github.io)

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** Primary Scandinavian NLP benchmark covering all Nordic languages, foundational for Nordic LLM evaluation.

## Tags

