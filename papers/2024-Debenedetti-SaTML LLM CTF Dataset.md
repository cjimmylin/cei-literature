---


Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EXSR0214
type: conferencePaper
short_title: SaTML LLM CTF Dataset
year: 2024
first_author: "[[Debenedetti, Edoardo]]"
last_author: "[[Schönherr, Lea]]"
authors: "[[Debenedetti, Edoardo]]; [[Rando, Javier]]; [[Paleka, Daniel]]; [[Florin, Silaghi Fineas]]; [[Albastroiu, Dragos]]; [[Cohen, Niv]]; [[Lemberg, Yuval]]; [[Ghosh, Reshmi]]; [[Wen, Rui]]; [[Salem, Ahmed]]; [[Cherubin, Giovanni]]; [[Zanella-Beguelin, Santiago]]; [[Schmid, Robin]]; [[Klemm, Victor]]; [[Miki, Takahiro]]; [[Li, Chenhao]]; [[Kraft, Stefan]]; [[Fritz, Mario]]; [[Tramèr, Florian]]; [[Abdelnabi, Sahar]]; [[Schönherr, Lea]]"
authors_incomplete: false
url: "https://arxiv.org/abs/2406.07954"
external_pdf: "https://arxiv.org/pdf/2406.07954.pdf"
local_pdf: "[[PDFs/2024/2024-Debenedetti-SaTML LLM CTF Dataset.pdf]]"
pdf_extract: "PDF Extracts/2024/2024-Debenedetti-SaTML LLM CTF Dataset.md"
publication: NeurIPS 2024
DATE_ADDED: 20260207
ethics_overall: "No"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
national_ethnic_cultural: "N/A"
religious_values: "N/A"
moral_psychology: "Value Pluralism / Schwartz"
newtags: 
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
tags: 
abstract: "Large language model systems face important security risks from maliciously crafted messages that aim to overwrite the system’s original instructions or leak private data. To study this problem, we organized a capture-the-flag competition at IEEE SaTML 2024, where the flag is a secret string in the LLM system prompt. The competition was organized in two phases. In the first phase, teams developed defenses to prevent the model from leaking the secret."
research_topic: "Machine Learning"
data_description: "Dataset"
data_metrics: "Not specified"
LLM_assessed: "GPT-3.5, Llama-2"
DATA_URL: "https://huggingface.co/datasets/ethz-spylab/ctf-satml24, https://github.com/ethz-spylab/satml-llm-ctf"
---
# SaTML LLM CTF Dataset

## Authors

[[Debenedetti, Edoardo]], [[Rando, Javier]], [[Paleka, Daniel]], [[Florin, Silaghi Fineas]], [[Albastroiu, Dragos]], [[Cohen, Niv]], [[Lemberg, Yuval]], [[Ghosh, Reshmi]], [[Wen, Rui]], [[Salem, Ahmed]], [[Cherubin, Giovanni]], [[Zanella-Beguelin, Santiago]], [[Schmid, Robin]], [[Klemm, Victor]], [[Miki, Takahiro]], [[Li, Chenhao]], [[Kraft, Stefan]], [[Fritz, Mario]], [[Tramèr, Florian]], [[Abdelnabi, Sahar]], [[Schönherr, Lea]]

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

This paper presents a dataset from the IEEE SaTML 2024 capture-the-flag competition on LLM prompt injection attacks and defenses. The dataset contains over 137,000 multi-turn attack conversations targeting GPT-3.5 and Llama-2 (70B) models, with 44 accepted defenses including system prompts, Python filters, and LLM filters. The dataset includes labeled successful and unsuccessful secret extraction attempts from 65 attacking teams.

## Notes

**Source:** Exhaustive Literature Search (2026-02-07), Agent 4
**Implementation Readiness:** HIGH

## Tags

