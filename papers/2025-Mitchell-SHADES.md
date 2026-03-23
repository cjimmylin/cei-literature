---































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: BY3E46VS
type: journalArticle
year: 2025
short_title: SHADES
first_author: "[[Margaret Mitchell]]"
last_author: "[[Zeerak Talat]]"
authors: "Margaret Mitchell; Hamdan Al-Ali; Giuseppe Attanasio; Ioana Baldini; Miruna Clinciu; Jordan Clive; Pieter Delobelle; Manan Dey; Kaustubh Dhole; Timm Dill; Amirbek Djanibekov; Tair Djanibekov; Jad Doughman; Ritam Dutt; Jessica Zosa Forde; Jay Gala; Avijit Ghosh; Sil Hamilton; Carolin Holtermann; Jerry Huang; Lucie-Aimée Kaffee; Janavi Kasera; Tanmay Laud; Anne Lauscher; Roberto Luis López; Jonibek Mansurov; Maraim Masoud; Sagnik Mukherjee; Nurdaulet Mukhituly; Nikita Nangia; Shangrui Nie; Anaelia Ovalle; Giada Pistilli; Esther Ploeger; Jeremy Qin; Dragomir Radev; Vipul Raheja; Beatrice Savoldi; Shanya Sharma; Xudong Shen; Kaiser Sun; Eliza Szczechla; Tiago Timponi Torrent; Deepak Tunuguntla; Emilio Villa-Cueva; Marcelo Viridiano; Kayo Yin; Mike Zhang; Sydney Zink; Aurélie Névéol; Zeerak Talat"
url: "https://aclanthology.org/2025.naacl-long.600/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/8RXAIHQP/Mitchell et al. - SHADES Towards a Multilingual Assessment of Stereotypes in Large Language Models.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "Multilingual"
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
newtags: Utilitarianism
key_contribution: "Introduces SHADES, a multilingual (16 languages) dataset for assessing culturally specific stereotypes in LLMs"
significance: "Crucial for de-westernizing safety eval, showing that models consistently reproduce regional stereotypes often missed by English-centric benchmarks"
tags: 
abstract: "Large Language Models (LLMs), the bedrock of many “artificial intelligence” (AI) applications, are known to reproduce social biases present in their training data. Yet resources to measure and control this issue are limited. Research identifying and mitigating stereotype biases have primarily been concentrated around English, lagging the rapid advancement of LLMs in multilingual settings. To help further advance the ability to address stereotype bias in AI systems, we introduce a new..."
LLM_assessed: "BLOOM, Llama-2, Llama-3, Mistral, Qwen"
DATA_URL: "https://huggingface.co/datasets/LanguageShades/BiasShades"
pdf_extract: "PDF Extracts/2025/2025-Mitchell-SHADES.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Mitchell-SHADES.pdf]]"
publication: ACL Anthology (NAACL 2025)
CONF-CC: "NAACL 2025"
DATE_ADDED: 20260213
CONFERENCE: "NAACL 2025"
ethics_overall: 45
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 5
contractarian_ethics: 0
care_ethics: 0
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Evaluation approach dataset"
data_metrics: "16 languages"
ethics_perspective: "Bias & Fairness"
---
# SHADES: Towards a Multilingual Assessment of Stereotypes in Large Language Models

## Metadata

**Authors:** Mitchell, Margaret; Al-Ali, Hamdan; Attanasio, Giuseppe; Baldini, Ioana; Clinciu, Miruna; Clive, Jordan; Delobelle, Pieter; Dey, Manan; Dhole, Kaustubh; Dill, Timm; Djanibekov, Amirbek; Djanibekov, Tair; Doughman, Jad; Dutt, Ritam; Forde, Jessica Zosa; Gala, Jay; Ghosh, Avijit; Hamilton, Sil; Holtermann, Carolin; Huang, Jerry; Kaffee, Lucie-Aimée; Kasera, Janavi; Laud, Tanmay; Lauscher, Anne; López, Roberto Luis; Mansurov, Jonibek; Masoud, Maraim; Mukherjee, Sagnik; Mukhituly, Nurdaulet; Nangia, Nikita; Nie, Shangrui; Ovalle, Anaelia; Pistilli, Giada; Ploeger, Esther; Qin, Jeremy; Radev, Dragomir; Raheja, Vipul; Savoldi, Beatrice; Sharma, Shanya; Shen, Xudong; Sun, Kaiser; Szczechla, Eliza; Torrent, Tiago Timponi; Tunuguntla, Deepak; Villa-Cueva, Emilio; Viridiano, Marcelo; Yin, Kayo; Zhang, Mike; Zink, Sydney; Névéol, Aurélie; Talat, Zeerak

**Type:** journalArticle

## Links

- **Acl:** https://aclanthology.org/2025.naacl-long.600/
- **Openreview:** https://openreview.net/forum?id=zSwnz6BsDa

## Abstract

Large Language Models (LLMs) reproduce and exacerbate the social biases present in their training data, and resources to quantify this issue are limited. While research has attempted to identify and mitigate such biases, most efforts have been concentrated around English, lagging the rapid advancement of LLMs in multilingual settings. In this paper, we introduce a new multilingual parallel dataset SHADES to help address this issue, designed for examining culturally-specific stereotypes that may be learned by LLMs. The dataset includes stereotypes from 20 regions around the world and 16 languages, spanning multiple identity categories subject to discrimination worldwide. We demonstrate its utility in a series of exploratory evaluations for both “base” and “instruction-tuned” language models. Our results suggest that stereotypes are consistently reflected across models and languages, with some languages and models indicating much stronger stereotype biases than others.

## Authors

[[Margaret Mitchell]], [[Hamdan Al-Ali]], [[Giuseppe Attanasio]], [[Ioana Baldini]], [[Miruna Clinciu]], [[Jordan Clive]], [[Pieter Delobelle]], [[Manan Dey]], [[Kaustubh Dhole]], [[Timm Dill]], [[Amirbek Djanibekov]], [[Tair Djanibekov]], [[Jad Doughman]], [[Ritam Dutt]], [[Jessica Zosa Forde]], [[Jay Gala]], [[Avijit Ghosh]], [[Sil Hamilton]], [[Carolin Holtermann]], [[Jerry Huang]], [[Lucie-Aimée Kaffee]], [[Janavi Kasera]], [[Tanmay Laud]], [[Anne Lauscher]], [[Roberto Luis López]], [[Jonibek Mansurov]], [[Maraim Masoud]], [[Sagnik Mukherjee]], [[Nurdaulet Mukhituly]], [[Nikita Nangia]], [[Shangrui Nie]], [[Anaelia Ovalle]], [[Giada Pistilli]], [[Esther Ploeger]], [[Jeremy Qin]], [[Dragomir Radev]], [[Vipul Raheja]], [[Beatrice Savoldi]], [[Shanya Sharma]], [[Xudong Shen]], [[Kaiser Sun]], [[Eliza Szczechla]], [[Tiago Timponi Torrent]], [[Deepak Tunuguntla]], [[Emilio Villa-Cueva]], [[Marcelo Viridiano]], [[Kayo Yin]], [[Mike Zhang]], [[Sydney Zink]], [[Aurélie Névéol]], [[Zeerak Talat]]

## Data Description

SHADES is a new multilingual parallel dataset of 304 internationally valid culturally-specific stereotypes from 37 regions translated across 16 languages, annotated with bias type, geographic validity, targeted subpopulations, and statement types; also includes 443 minimally contrastive non-stereotype statements and multilingual templates for synthetic bias evaluation data generation.


## Notes

