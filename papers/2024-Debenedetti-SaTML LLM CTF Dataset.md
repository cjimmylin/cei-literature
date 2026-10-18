---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0214
type: conferencePaper
short_title: "SaTML LLM CTF Dataset"
year: 2024
first_author: "[[Debenedetti, Edoardo]]"
last_author: "[[Schönherr, Lea]]"
authors: "Debenedetti, Edoardo; Rando, Javier; Paleka, Daniel; Florin, Silaghi Fineas; Albastroiu, Dragos; Cohen, Niv; Lemberg, Yuval; Ghosh, Reshmi; Wen, Rui; Salem, Ahmed; Cherubin, Giovanni; Zanella-Beguelin, Santiago; Schmid, Robin; Klemm, Victor; Miki, Takahiro; Li, Chenhao; Kraft, Stefan; Fritz, Mario; Tramèr, Florian; Abdelnabi, Sahar; Schönherr, Lea"
authors_incomplete: false
url: "https://arxiv.org/abs/2406.07954"
external_pdf: "https://arxiv.org/pdf/2406.07954.pdf"
pdf_extract: "PDF Extracts/2024/2024-Debenedetti-SaTML LLM CTF Dataset.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2024/2024-Debenedetti-SaTML LLM CTF Dataset.pdf]]"
publication: "NeurIPS 2024"
CONF-CC: "NeurIPS 2024"
DATE_ADDED: 20260207
national_ethnic_cultural: N/A
cultures_nationalities_list: N/A
languages_list: 
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
newtags: 
tags: 
abstract: "Large language model systems face important security risks from maliciously crafted messages that aim to overwrite the system’s original instructions or leak private data. To study this problem, we organized a capture-the-flag competition at IEEE SaTML 2024, where the flag is a secret string in the LLM system prompt. The competition was organized in two phases. In the first phase, teams developed defenses to prevent the model from leaking the secret."
LLM_assessed: "GPT-3.5, Llama-2-70B"
DATA_URL: "https://huggingface.co/datasets/ethz-spylab/ctf-satml24, https://github.com/ethz-spylab/satml-llm-ctf"
CONFERENCE: "NeurIPS 2024"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 20
contractarian_ethics: 0
care_ethics: 0
research_topic: "Machine Learning"
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
weird_score: 78
is_benchmark: No
is_eval: No
is_dataset: Yes
data_description: Dataset
data_metrics: "Not specified"
---
# SaTML LLM CTF Dataset

## Authors

[[Edoardo Debenedetti|Debenedetti, Edoardo]], [[Javier Rando|Rando, Javier]], [[Daniel Paleka|Paleka, Daniel]], [[Florin, Silaghi Fineas]], [[Albastroiu, Dragos]], [[Cohen, Niv]], [[Lemberg, Yuval]], [[Ghosh, Reshmi]], [[Wen, Rui]], [[Salem, Ahmed]], [[Cherubin, Giovanni]], [[Zanella-Beguelin, Santiago]], [[Schmid, Robin]], [[Klemm, Victor]], [[Miki, Takahiro]], [[Li, Chenhao]], [[Kraft, Stefan]], [[Fritz, Mario]], [[Tramèr, Florian]], [[Abdelnabi, Sahar]], [[Schönherr, Lea]]

## Metadata

**Authors:** Debenedetti, Edoardo; Rando, Javier; Paleka, Daniel; Florin, Silaghi Fineas; Albastroiu, Dragos; Cohen, Niv; Lemberg, Yuval; Ghosh, Reshmi; Wen, Rui; Salem, Ahmed; Cherubin, Giovanni; Zanella-Beguelin, Santiago; Schmid, Robin; Klemm, Victor; Miki, Takahiro; Li, Chenhao; Kraft, Stefan; Fritz, Mario; Tramèr, Florian; Abdelnabi, Sahar; Schönherr, Lea

**Year:** 2024

**Type:** conferencePaper

**Venue:** NeurIPS 2024

## Links

- **arXiv:** https://arxiv.org/abs/2406.07954
- **Code/Data:** https://huggingface.co/datasets/ethz-spylab/ctf-satml24; https://huggingface.co/datasets/ethz-spylab/ctf-satml24

## Abstract

Large language model systems face important security risks from maliciously crafted messages that aim to overwrite the system’s original instructions or leak private data. To study this problem, we organized a capture-the-flag competition at IEEE SaTML 2024, where the flag is a secret string in the LLM system prompt. The competition was organized in two phases. In the first phase, teams developed defenses to prevent the model from leaking the secret. During the second phase, teams were challenged to extract the secrets hidden for defenses proposed by the other teams. This report summarizes the main insights from the competition. Notably, we found that all defenses were bypassed at least once, highlighting the difficulty of designing a successful defense and the necessity for additional research to protect LLM systems. To foster future research in this direction, we compiled a dataset with over 137k multi-turn attack chats and open-sourced the platform.

## Dataset Information

137,063 multi-turn attack chats

## Data Description

Dataset of 137K+ multi-turn prompt injection attack conversations from a capture-the-flag competition at IEEE SaTML 2024, with 44 defenses and labeled attack outcomes for LLM security research.


## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 4
**Implementation Readiness:** HIGH

## Tags

