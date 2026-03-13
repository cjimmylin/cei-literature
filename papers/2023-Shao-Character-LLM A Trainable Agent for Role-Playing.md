---































Human View: true
Human View Date: 2026-01-24
Human View note: "Can simulate historical characters"
Not AI: 
key: 2ML6F4EE
type: document
short_title: "Character-LLM: A Trainable Agent for Role-Playing"
year: 2023
first_author: "[[Yunfan Shao]]"
last_author: "[[Qiu, Xipeng]]"
authors: "Shao, Yunfan; Li, Linyang; Dai, Junqi; Qiu, Xipeng"
url: "https://aclanthology.org/2023.emnlp-main.814/"
pdf_extract: "PDF Extracts/2023/2023-Shao-Character-LLM A Trainable Agent for Role-Playing.md"
local_pdf: "[[PDFs/2023/2023-Shao-Character-LLM A Trainable Agent for Role-Playing.pdf]]"
external_pdf: "file:///Users/jimmylin/Zotero/storage/J3VV4C8K/2023 - Character-LLM A Trainable Agent for Role-Playing.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "American, Virtue Ethics"
key_contribution: "Introduces 'Character-LLM', a trainable agent framework that edits profiles as experiences to simulate specific human characters (simulacra)"
significance: "Enables the detailed simulation of specific personal avatars with consistent profiles and emotional states, relevant for character-based AI interactions"
tags: 
abstract: "Large language models (LLMs) can be used to serve as agents to simulate human behav- iors, given the powerful ability to understand human instructions and provide high-quality generated texts. Such ability stimulates us to wonder whether LLMs can simulate a person in a higher form than simple human behaviors. Therefore, we aim to train an agent with the profile, experience, and emotional states of a specific person instead of using limited prompts to instruct ChatGPT API. In this work, we in- tr"
paper_summary: "Abstract: Large language models (LLMs) can be used to serve as agents to simulate human behav- iors, given the powerful ability to understand human instructions and provide high-quality generated texts. Such ab | Overview: Character-LLM: A Trainable Agent for Role-Playing Yunfan Shao1,2∗, Linyang Li1, Junqi Dai1, Xipeng Qiu1† 1School of Computer Science, Fudan University 1Shanghai Key Laboratory of Intelligent Informati | Methodology: Our methodology diverges from the existing prac- tice of mimicking the style and tones of curated utterances via Supervised Fine-Tuning (SFT) or provi"
CONF-CC: "N/A"
DATE_ADDED: 20260208
LLM_assessed: "Alpaca, ChatGPT, LLaMA, Vicuna"
DATA_URL: "https://github.com/choosewhatulike/trainable-agents"
CONFERENCE: "EMNLP 2023"
ethics_overall: "No"
virtue_ethics: "Yes"
deontological_ethics: "No"
utilitarian_ethics: "No"
research_topic: "Other"
is_benchmark: "No"
is_eval: "Yes"
is_dataset: Yes
data_description: "Evaluation methodology"
data_metrics: "Not specified"
---
 Character-LLM: A Trainable Agent for Role-Playing

## Authors

[[Yunfan Shao|Shao, Yunfan]], [[Linyang Li|Li, Linyang]], [[Junqi Dai|Dai, Junqi]], [[Xipeng Qiu|Qiu, Xipeng]]

## Links

- **Local PDF:** [[PDFs/2023/2023-Shao-Character-LLM A Trainable Agent for Role-Playing.pdf|Open PDF]]

- **ACL Anthology:** https://aclanthology.org/2023.emnlp-main.814/

## Abstract

Large language models (LLMs) can be used to serve as agents to simulate human behaviors, given the powerful ability to understand human instructions and provide high-quality generated texts. Such ability stimulates us to wonder whether LLMs can simulate a person in a higher form than simple human behaviors. Therefore, we aim to train an agent with the profile, experience, and emotional states of a specific person instead of using limited prompts to instruct ChatGPT API. In this work, we introduce Character-LLM that teach LLMs to act as specific people such as Beethoven, Queen Cleopatra, Julius Caesar, etc. Our method focuses on editing profiles as experiences of a certain character and training models to be personal simulacra with these experiences. To assess the effectiveness of our approach, we build a test playground that interviews trained agents and evaluates whether the agents <i>memorize</i> their characters and experiences. Experimental results show interesting observations that help build future simulacra of humankind.

## Detailed Summary

This paper introduces **Character-LLM**, a framework for training Large Language Models to act as specific people (simulacra) by "experience uploading" instead of just prompt-based instructions. The authors argue that simple prompting is insufficient for deep role-playing ("simulacra") that requires consistent personality, emotional states, and detailed memories.

## Paper Outline

1.  **Introduction**: Generative Agents vs. Simulacra; The shortage of character-specific data.
2.  **Related Work**: Role-Playing Agents; Profile-based Prompting.
3.  **Methodology (Character-LLM)**:
    *   Profile Reconstruction.
    *   Experience Uploading (Scene Generation).
    *   Protective Experience (Safety/Refusal training).
4.  **Experiments**:
    *   Comparison with ChatGPT and Character.AI.
    *   Metrics: Memorization, Consistency, Hallucination.
5.  **Conclusion**: Trainable agents offer deeper immersion than prompt-based agents.

## Methods Summary

The authors propose an "Experience Uploading" process to solve the lack of training data for specific historical or fictional characters. They use an LLM (ChatGPT) to expand character profiles into detailed attribute lists and "flashback" scenes. They then generate thousands of dialogue interactions portraying the character's life events and fine-tune Llama models on this synthetic "experience" data. A "Protective Experience" training phase is added to ensure the model refuses out-of-character queries to maintain immersion.

## Results Summary

1.  **Immersion**: Evaluators found Character-LLM significantly more "in-character" than baseline ChatGPT, especially in maintaining the style and knowledge limitations of the character.
2.  **Hallucination Reduction**: The "Protective Experience" training effectively reduced anachronistic hallucinations.
3.  **Consistency**: Trained agents showed higher memory retention and persona stability across long-form interactions compared to prompt-based baselines.

## Conclusions

The authors conclude that *training* on character-specific memories is more effective for creating robust digital twins or role-playing agents than simple prompting. The "Experience Uploading" technique effectively bridges the data scarcity gap for specific personae.

## Artifact Contributions

*   **Character-LLM Framework**: Code for generating character data and fine-tuning.
*   **Models**: Released weights for several historical character agents (Beethoven, Cleopatra, Caesar).

## Data Description

Character experience datasets for 9 historical/fictional figures (e.g., Beethoven, Cleopatra, Caesar) with ~1.6K scenes each, plus 1,307 evaluation interview questions across single-turn and multi-turn formats.


## Notes

