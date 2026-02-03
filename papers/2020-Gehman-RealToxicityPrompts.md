---



Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: CZYS2N2K
type: document
short_title: RealToxicityPrompts
year: 2020
first_author: "[[Samuel Gehman]]"
authors: "[[Gehman, Samuel]]; [[Gururangan, Suchin]]; [[Sap, Maarten]]; [[Choi, Yejin]]; [[Smith, Noah A.]]"
url: "https://aclanthology.org/2020.findings-emnlp.301/"
external_pdf: "https://arxiv.org/pdf/2009.11462v2.pdf"
national_ethnic_cultural: N/A
religious_values: N/A
moral_psychology: N/A
newtags: "Toxicity & Hate Speech"
key_contribution: "Released RealToxicityPrompts, a dataset of 100k naturally occurring sentence prompts to evaluate the extent of neural toxic degeneration in pretrained LMs."
significance: "Demonstrated that LMs can generate toxic content even from innocuous prompts and that standard controllable generation methods are insufficient, necessitating better pretraining data curation."
tags: 
abstract: "Pretrained neural language models (LMs) are prone to generating racist, sexist, or otherwise toxic language which hinders their safe deployment. We investigate the extent to which pretrained LMs can be prompted to generate toxic language, and the effectiveness of controllable text generation algorithms at preventing such toxic degeneration. We create and release RealToxicityPrompts, a dataset of 100K naturally occurring, sentence-level prompts derived from a large corpus of English web text, paired with toxicity scores from a widely-used toxicity classifier. Using RealToxicityPrompts, we find that pretrained LMs can degenerate into toxic text even from seemingly innocuous prompts. We empirically assess several controllable generation methods, and find that while data- or compute-intensive methods (e.g., adaptive pretraining on non-toxic data) are more effective at steering away from toxicity than simpler solutions (e.g., banning “bad” words), no current method is failsafe against neural toxic degeneration. To pinpoint the potential cause of such persistent toxic degeneration, we analyze two web text corpora used to pretrain several LMs (including GPT-2; Radford et. al, 2019), and find a significant amount of offensive, factually unreliable, and otherwise toxic content. Our work provides a test bed for evaluating toxic generations by LMs and stresses the need for better data selection processes for pretraining."
local_pdf: "[[PDFs/2020-Gehman-RealToxicityPrompts.pdf]]"
pdf_extract: "PDF Extracts/2020-Gehman-RealToxicityPrompts.md"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Toxicity & Hate Speech"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation methodology text corpus for toxicity detection"
data_metrics: "Not specified"
---
# RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models

## Authors

[[Samuel Gehman]], [[Suchin Gururangan]], [[Maarten Sap]], [[Yejin Choi]], [[Noah A. Smith]]
## Metadata

**Year:** 2020

**Type:** document

## Links

- **ACL Anthology:** https://aclanthology.org/2020.findings-emnlp.301/

## Abstract

Pretrained neural language models (LMs) are prone to generating racist, sexist, or otherwise toxic language which hinders their safe deployment. We investigate the extent to which pretrained LMs can be prompted to generate toxic language, and the effectiveness of controllable text generation algorithms at preventing such toxic degeneration. We create and release RealToxicityPrompts, a dataset of 100K naturally occurring, sentence-level prompts derived from a large corpus of English web text, paired with toxicity scores from a widely-used toxicity classifier. Using RealToxicityPrompts, we find that pretrained LMs can degenerate into toxic text even from seemingly innocuous prompts. We empirically assess several controllable generation methods, and find that while data- or compute-intensive methods (e.g., adaptive pretraining on non-toxic data) are more effective at steering away from toxicity than simpler solutions (e.g., banning “bad” words), no current method is failsafe against neural toxic degeneration. To pinpoint the potential cause of such persistent toxic degeneration, we analyze two web text corpora used to pretrain several LMs (including GPT-2; Radford et. al, 2019), and find a significant amount of offensive, factually unreliable, and otherwise toxic content. Our work provides a test bed for evaluating toxic generations by LMs and stresses the need for better data selection processes for pretraining.

## Notes

