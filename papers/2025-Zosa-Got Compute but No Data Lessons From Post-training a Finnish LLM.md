---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0499
type: preprint
short_title: "Got Compute, but No Data: Lessons From Post-training a Finnish LLM"
year: 2025
first_author: "[[Elaine Zosa]]"
last_author: "[[Sampo Pyysalo]]"
authors: "Elaine Zosa, Ville Komulainen, Sampo Pyysalo"
url: "https://arxiv.org/abs/2503.09407"
external_pdf: "https://arxiv.org/pdf/2503.09407.pdf"
publication: "arXiv / NoDaLiDa 2025"
local_pdf: "[[PDFs/2025/2025-Zosa-Got Compute but No Data Lessons From Post-training a Finnish LLM.pdf]]"
pdf_extract: "PDF Extracts/2025/2025-Zosa-Got Compute but No Data Lessons From Post-training a Finnish LLM.md"
DATE_ADDED: 20260213
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
national_ethnic_cultural: N/A
languages_list: "English, Finnish"
religious_values: N/A
religious_values_list: N/A
moral_psychology: N/A
newtags: 
is_benchmark: No
is_eval: Yes
is_dataset: Yes
data_description: "Evaluation methodology dataset"
data_metrics: "Not specified"
LLM_assessed: Poro-34B
DATA_URL: "https://huggingface.co/LumiOpen/Poro-34B-chat-OpenAssistant"
tags: 
abstract: "As LLMs gain more popularity as chatbots and general assistants, methods have been developed to enable LLMs to follow instructions and align with human preferences. These methods have found success in the field, but their effectiveness has not been demonstrated outside of high-resource languages. In this work, we discuss our experiences in post-training an LLM for instruction-following for English and Finnish."
research_topic: "Machine Translation"
---
# Got Compute, but No Data: Lessons From Post-training a Finnish LLM

## Authors

[[Elaine Zosa, Ville Komulainen, Sampo Pyysalo]]

## Metadata

**Authors:** Elaine Zosa, Ville Komulainen, Sampo Pyysalo

**Year:** 2025

**Type:** preprint

**Venue:** arXiv / NoDaLiDa 2025

**Languages:** English, Finnish

## Links

- **arXiv:** https://arxiv.org/abs/2503.09407
- **Code/Data:** https://huggingface.co/LumiOpen/Poro-34B-chat-OpenAssistant

## Abstract

Post-training a Finnish LLM (Poro) for instruction-following. Translates IFEval benchmark to Finnish. Using all available English+Finnish data for SFT gives best performance. Releases datasets, recipes, and model openly.

## Summary

This paper documents the experience of post-training the Poro-34B Finnish LLM for instruction-following capabilities in a low-resource language context. The authors translate the IFEval benchmark to Finnish to enable evaluation and demonstrate that supervised fine-tuning using all available English and Finnish data yields the best performance compared to Finnish-only or English-only approaches. The work openly releases training datasets, training recipes, and the Poro-34B-chat model, providing practical lessons for instruction-following alignment in languages with limited training data.

## Data Description

Post-trains the Poro Finnish LLM for instruction-following, translates IFEval benchmark to Finnish, and demonstrates that using all available English+Finnish data for supervised fine-tuning yields best performance. Releases datasets, training recipes, and the Poro-34B-chat model openly.


## Detailed Summary

This paper documents practical experiences in post-training the Poro 34B multilingual LLM (trained on 1 trillion tokens of English, Finnish, and code with 129 billion Finnish tokens) for instruction-following capabilities in both English and Finnish. The work addresses the fundamental challenge of post-training LLMs for low-resource languages where instruction and preference datasets are scarce. The authors use the Poro model itself to machine-translate instruction and preference datasets from English to Finnish, and employ a commercial translation service to translate the IFEval benchmark to Finnish for evaluation. They experiment with different combinations of Finnish and English data in both supervised fine-tuning (SFT) and direct preference optimization (DPO), finding that a few hundred Finnish instruction samples can yield competitive Finnish instruction-following performance. The study also demonstrates that while English-only preference optimization offers some cross-lingual benefits, the best results come from preference data in both languages. All models, datasets, and training recipes are released under open licenses.

## Paper Outline

1. Introduction - Challenge of post-training LLMs for low-resource languages
2. Related Work - Instruction tuning, preference optimization, and multilingual post-training
3. Experimental Setup - Base model (Poro 34B), hardware, hyperparameters
4. Data - Instruction datasets (OpenAssistant), preference datasets, Finnish translations
5. Evaluation - IFEval (English and Finnish), MT-Bench Finnish
6. Results - Comparison of monolingual, multilingual, and cross-lingual configurations
7. Discussion and Conclusion

## Methods Summary

The base model is Poro 34B, trained on English, Finnish, and code. For SFT, the authors use OpenAssistant data in English and machine-translated Finnish versions, experimenting with different language mixtures. For DPO, they similarly compare English-only, Finnish-only, and bilingual preference data. Training uses 32 AMD MI250X GPUs with full parameter fine-tuning (SFT: batch size 128, lr 2e-5, 3 epochs; DPO: batch size 64, lr 5e-7, 5 epochs). Evaluation uses the IFEval benchmark (translated to Finnish via commercial MT) and adapted MT-Bench.

## Results Summary

Key findings include: (1) with just a few hundred Finnish instruction samples, competitive Finnish instruction-following performance can be achieved; (2) English-only preference optimization provides some cross-lingual transfer to Finnish, but the best results use bilingual preference data; (3) the combination of English and Finnish data for both SFT and DPO yields the strongest overall performance; (4) machine-translated instruction data, while imperfect, proves sufficiently useful for bootstrapping Finnish instruction-following capabilities.

## Conclusions

The paper demonstrates that effective instruction-following for low-resource languages can be achieved even with severely limited native-language training data, provided that appropriate cross-lingual transfer strategies and machine-translated resources are leveraged. The practical lessons and openly released resources offer a reproducible template for other low-resource language communities facing similar data scarcity challenges.

## Artifact Contributions

- **Model:** Poro-34B-chat-OpenAssistant (https://huggingface.co/LumiOpen/Poro-34B-chat-OpenAssistant)
- **Datasets:** Machine-translated Finnish instruction and preference datasets
- **Evaluation:** Finnish IFEval translation
- **Training Recipes:** Open-source training configurations for SFT and DPO

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B7
**Relevance:** Finnish LLM post-training and evaluation with translated benchmarks for instruction following.

## Tags

