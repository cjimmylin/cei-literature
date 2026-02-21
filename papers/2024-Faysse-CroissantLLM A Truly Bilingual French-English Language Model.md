---






Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0432
type: preprint
short_title: "CroissantLLM: A Truly Bilingual French-English Language Model"
year: 2024
first_author: "[[Faysse, Manuel]]"
last_author: "[[Colombo, Pierre]]"
authors: "Faysse, Manuel; Fernandes, Patrick; Guerreiro, Nuno M.; Loison, António; Alves, Duarte M.; Corro, Caio; Boizard, Nicolas; Alves, João; Rei, Ricardo; Martins, Pedro H.; Casademunt, Antoni Bigata; Yvon, François; Martins, André F. T.; Viaud, Gautier; Hudelot, Céline; Colombo, Pierre"
authors_incomplete: false
url: "https://arxiv.org/abs/2402.00786"
external_pdf: "https://arxiv.org/pdf/2402.00786.pdf"
publication: arXiv
CONF-CC: "Preprint"
pdf_extract: "PDF Extracts/2024/2024-Faysse-CroissantLLM A Truly Bilingual French-English Language Model.md"
local_pdf: "[[PDFs/2024/2024-Faysse-CroissantLLM A Truly Bilingual French-English Language Model.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "French"
cultures_nationalities_list: "French"
languages_list: "English, French"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: 
LLM_assessed: "CroissantLLM, Llama-2, Mistral, Qwen"
DATA_URL: "https://huggingface.co/croissantllm"
tags: 
abstract: "We introduce CroissantLLM, a 1.3B language model pre-trained on a set of 3T English and French tokens, to bring to the research and industrial community a high-performance, fully open-sourced bilingual model that runs swiftly on consumer-grade local hardware. To that end, we pioneer the approach of training an intrinsically bilingual model with a 1:1 English-to-French pretraining data ratio, a custom tokenizer, and bilingual finetuning datasets."
research_topic: "NLP & Representation Learning"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Social & Cultural Values"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "No"
data_description: "Benchmark for bias and fairness"
data_metrics: "Not specified"
CONFERENCE: "Preprint"
---
# CroissantLLM: A Truly Bilingual French-English Language Model

## Authors

[[Faysse, Manuel]], [[Fernandes, Patrick]], [[Guerreiro, Nuno M]], [[Loison, António]], [[Alves, Duarte M]], [[Corro, Caio]], [[Boizard, Nicolas]], [[Alves, João]], [[Rei, Ricardo]], [[Martins, Pedro H]], [[Casademunt, Antoni Bigata]], [[Yvon, François]], [[Martins, André F. T]], [[Viaud, Gautier]], [[Hudelot, Céline]], [[Colombo, Pierre]]

## Metadata

**Authors:** Faysse, Manuel; Fernandes, Patrick; Guerreiro, Nuno M.; Loison, António; Alves, Duarte M.; Corro, Caio; Boizard, Nicolas; Alves, João; Rei, Ricardo; Martins, Pedro H.; Casademunt, Antoni Bigata; Yvon, François; Martins, André F. T.; Viaud, Gautier; Hudelot, Céline; Colombo, Pierre

**Year:** 2024

**Type:** preprint

**Venue:** arXiv

**Languages:** English, French

**Benchmark:** FrenchBench

## Links

- **arXiv:** https://arxiv.org/abs/2402.00786
- **Code/Data:** https://huggingface.co/collections/manu/frenchbench-evaluation-datasets

## Abstract

1.3B bilingual model pretrained on 3T English and French tokens with 1:1 ratio to mitigate English-centric cultural bias. Introduces FrenchBench, a novel benchmark for French LLM evaluation covering classification and generation tasks, including French cultural knowledge trivia. Evaluates bias and cultural knowledge dimensions.

## Summary

This paper introduces CroissantLLM, a 1.3 billion parameter language model pre-trained on 3 trillion English and French tokens with a pioneering 1:1 English-to-French data ratio to mitigate English-centric cultural bias. The model uses a custom bilingual tokenizer and is fine-tuned on bilingual datasets to achieve truly balanced bilingual performance on consumer-grade hardware. The authors develop FrenchBench, the first comprehensive benchmark for French LLM evaluation covering both classification and generation tasks, including French cultural knowledge trivia to assess cultural bias dimensions. CroissantLLM demonstrates improved French capabilities compared to English-centric models while explicitly evaluating cultural biases alongside standard NLP performance metrics.

## Data Description

CroissantLLM bilingual French-English language model trained from scratch with balanced French-English data. Includes training corpus and evaluation benchmarks for bilingual LLM performance, demonstrating improved French capabilities compared to English-centric models.


## Detailed Summary

This paper introduces CroissantLLM, a 1.3 billion parameter language model pre-trained on 3 trillion English and French tokens with a pioneering 1:1 English-to-French data ratio, designed to provide a high-performance, fully open-sourced bilingual model for consumer-grade hardware. The French training corpus (303B unique tokens) is highly curated with diverse sources including web data (CulturaX-filtered mC4/OSCAR, 292B tokens), legal and administrative documents from the French government's open data initiative (5.3B tokens), cultural data (Project Gutenberg French books, BNF manuscripts, poetry, podcasts, movie subtitles, Wikisource totaling ~3B tokens), Wikipedia (2B tokens), and industrial PDF data (191M tokens). The English corpus draws primarily from SlimPajama. The model also includes 141B code tokens and 36B parallel English-French translation tokens from OPUS. A key contribution is FrenchBench, a novel benchmark for French LLM evaluation covering classification tasks (sentiment analysis, NLI, question answering) and generation tasks (summarization, French cultural knowledge trivia), providing the first comprehensive French-specific LLM evaluation suite. The project achieves 81% compliance with the Foundation Model Transparency Index (FMTI) criteria, far exceeding most open initiatives.

## Paper Outline

1. Introduction - Transparency, English bias, and scale challenges in current LLMs
2. Data - French corpus (web, legal/administrative, cultural, encyclopedia, industrial), English corpus (SlimPajama), code data, parallel data, Gutenberg canaries for memorization testing
3. Model - Architecture, tokenizer design, scaling law experiments for bilingual ratio
4. FrenchBench - Classification and generation benchmark tasks
5. Evaluation - Comparison with other models, cultural knowledge assessment
6. Transparency - FMTI compliance analysis
7. Conclusion

## Methods Summary

CroissantLLM uses a custom bilingual tokenizer optimized for balanced French-English performance, trained on equal amounts of French and English text. The 1:1 training ratio is motivated by scaling law experiments on smaller models (50M-200M parameters) that reveal the trade-offs between language distribution ratios, empirically validating a balanced approach. The model is trained for approximately 3T tokens total with upsampling of French data (4.09x), English data (1.89x), and code data (2.04x) to achieve the balanced ratio. FrenchBench includes both existing datasets (e.g., French sentiment analysis, CLS, XNLI-fr) and newly created tasks including French cultural knowledge trivia questions to assess whether models encode France-specific knowledge beyond American-centric biases.

## Results Summary

CroissantLLM demonstrates strong bilingual performance competitive with similarly-sized models, achieving notably better French capabilities than English-centric models of comparable size. On FrenchBench, CroissantLLM outperforms Llama-based models on French-specific tasks while maintaining competitive English performance. Cultural knowledge evaluation reveals that CroissantLLM encodes significantly more French-specific knowledge compared to English-centric models, confirming that balanced bilingual training data effectively reduces American cultural bias. The model validates the hypothesis that training on non-English cultural data is essential for acquiring diverse cultural knowledge, with the 1:1 ratio achieving a "best of both worlds" performance profile.

## Conclusions

CroissantLLM demonstrates that intrinsically bilingual training with balanced data ratios can produce models with strong non-English capabilities without sacrificing English performance. The project's commitment to transparency (81% FMTI compliance) sets a new standard for open LLM development. Limitations include the relatively small model size (1.3B) which constrains advanced reasoning capabilities, the focus on only two languages, and the challenge of fully eliminating cultural biases. The released resources (training data, all checkpoints, code, evaluation benchmarks) provide a proven platform for future bilingual and multilingual LLM research.

## Artifact Contributions

- **CroissantLLM Models**: 1.3B parameter bilingual model with all training checkpoints (https://huggingface.co/CroissantLLM)
- **French Training Corpus**: 303B token curated French corpus from diverse sources
- **FrenchBench**: Novel French LLM evaluation benchmark (https://huggingface.co/collections/manu/frenchbench-evaluation-datasets)
- **CroissantLLM-Chat**: Fine-tuned conversational model
- **Translation Models**: Strong French-English translation models
- **Training Code**: Full training and evaluation codebases

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B6
**Relevance:** FrenchBench is the first comprehensive French-specific LLM benchmark. Explicitly evaluates cultural biases and French cultural knowledge alongside standard NLP tasks.

## Tags

