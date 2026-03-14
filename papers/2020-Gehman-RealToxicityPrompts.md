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
last_author: "[[Noah A. Smith]]"
authors: "Gehman, Samuel; Gururangan, Suchin; Sap, Maarten; Choi, Yejin; Noah A. Smith"
url: "https://aclanthology.org/2020.findings-emnlp.301/"
external_pdf: "https://arxiv.org/pdf/2009.11462v2.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
rv_islam: 0
rv_christianity: 0
rv_buddhism: 5
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
newtags: "Toxicity & Hate Speech"
key_contribution: "Released RealToxicityPrompts, a dataset of 100k naturally occurring sentence prompts to evaluate the extent of neural toxic degeneration in pretrained LMs."
significance: "Demonstrated that LMs can generate toxic content even from innocuous prompts and that standard controllable generation methods are insufficient, necessitating better pretraining data curation."
tags: 
abstract: "Pretrained neural language models (LMs) are prone to generating racist, sexist, or otherwise toxic language which hinders their safe deployment. We investigate the extent to which pretrained LMs can be prompted to generate toxic language, and the effectiveness of controllable text generation algorithms at preventing such toxic degeneration. We create and release REALTOXICITYPROMPTS, a dataset of 100K naturally occurring, sentence-level prompts derived from a large corpus of English web text,..."
pdf_extract: "PDF Extracts/2020/2020-Gehman-RealToxicityPrompts.md"
local_pdf: "[[PDFs/2020/2020-Gehman-RealToxicityPrompts.pdf]]"
CONF-CC: "N/A"
DATE_ADDED: 20260208
LLM_assessed: "GPT-2, GPT-3"
DATA_URL: "https://toxicdegeneration.allenai.org/"
CONFERENCE: "EMNLP 2020"
eleutherai: incorporated
helm: "incorporated"
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
is_benchmark: Yes
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation methodology text corpus for toxicity detection"
data_metrics: "Not specified"
ethics_perspective: "Toxicity & Hate Speech"
---
# RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models

## Authors

[[Samuel Gehman|Gehman, Samuel]], [[Suchin Gururangan|Gururangan, Suchin]], [[Maarten Sap|Sap, Maarten]], [[Yejin Choi|Choi, Yejin]], [[Smith, Noah A]]

## Links

- **ACL Anthology:** https://aclanthology.org/2020.findings-emnlp.301/

## Abstract

Pretrained neural language models (LMs) are prone to generating racist, sexist, or otherwise toxic language which hinders their safe deployment. We investigate the extent to which pretrained LMs can be prompted to generate toxic language, and the effectiveness of controllable text generation algorithms at preventing such toxic degeneration. We create and release RealToxicityPrompts, a dataset of 100K naturally occurring, sentence-level prompts derived from a large corpus of English web text, paired with toxicity scores from a widely-used toxicity classifier. Using RealToxicityPrompts, we find that pretrained LMs can degenerate into toxic text even from seemingly innocuous prompts. We empirically assess several controllable generation methods, and find that while data- or compute-intensive methods (e.g., adaptive pretraining on non-toxic data) are more effective at steering away from toxicity than simpler solutions (e.g., banning “bad” words), no current method is failsafe against neural toxic degeneration. To pinpoint the potential cause of such persistent toxic degeneration, we analyze two web text corpora used to pretrain several LMs (including GPT-2; Radford et. al, 2019), and find a significant amount of offensive, factually unreliable, and otherwise toxic content. Our work provides a test bed for evaluating toxic generations by LMs and stresses the need for better data selection processes for pretraining.

## Data Description

RealToxicityPrompts: 100K naturally occurring sentence-level prompts paired with toxicity scores, designed as a testbed for evaluating toxic degeneration in language models.


## Notes

