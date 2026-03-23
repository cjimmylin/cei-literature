---





































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: 7FLQPGMT
type: journalArticle
year: 2025
short_title: T2ISafety
first_author: "[[Lijun Li]]"
last_author: "[[Jing Shao]]"
authors: "Lijun Li; Zhelun Shi; Xuhao Hu; Bowen Dong; Yiran Qin; Xihui Liu; Lu Sheng; Jing Shao"
external_pdf: "file:///Users/jimmylin/Zotero/storage/E7EZLTEZ/Li et al. - T2ISafety Benchmark for Assessing Fairness, Toxicity, and Privacy in Image Generation.pdf"
pdf_extract: "PDF Extracts/2025/2025-Li-T2ISafety.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2025/2025-Li-T2ISafety.pdf]]"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
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
newtags: "AI Safety & Alignment"
key_contribution: "Released T2ISafety, a benchmark for assessing fairness, toxicity, and privacy in Text-to-Image models, revealing risks that even GPT-based evaluators miss."
significance: "Highlights that current T2I models suffer from persistent racial bias and privacy leakage, providing a specialized tool to evaluate visual generation safety beyond simple text filters."
tags: 
abstract: "Text-to-image (T2I) models have rapidly advanced, enabling the generation of high-quality images from text prompts across various domains. However, these models present notable safety concerns, including the risk of generating harmful, biased, or private content. Current research on assessing T2I safety remains in its early stages. While some efforts have been made to evaluate models on specific safety dimensions, many critical risks remain unexplored."
CONF-CC: "N/A"
DATE_ADDED: 20260129
LLM_assessed: "GPT-4o, Claude, Gemini, DALL-E, Stable Diffusion"
DATA_URL: "https://github.com/adwardlee/t2i_safety"
CONFERENCE: "Journal"
ethics_overall: 35
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for ai safety annotated dataset for toxicity detection"
data_metrics: "44 categories"
ethics_perspective: "AI Safety & Alignment"
---
# T2ISafety: Benchmark for Assessing Fairness, Toxicity, and Privacy in Image Generation

## Metadata

**Authors:** Li, Lijun; Shi, Zhelun; Hu, Xuhao; Dong, Bowen; Qin, Yiran; Liu, Xihui; Sheng, Lu; Shao, Jing

**Type:** journalArticle

## Links

- **Arxiv:** https://arxiv.org/abs/2501.12612
- **Github:** https://github.com/adwardlee/t2i_safety

## Abstract

Text-to-image (T2I) models have rapidly advanced, enabling the generation of high-quality images from text prompts across various domains. However, these models present notable safety concerns, including the risk of generating harmful, biased, or private content. Current research on assessing T2I safety remains in its early stages. While some efforts have been made to evaluate models on specific safety dimensions, many critical risks remain unexplored. To address this gap, we introduce T2ISafety, a safety benchmark that evaluates T2I models across three key domains: toxicity, fairness, and bias. We build a detailed hierarchy of 12 tasks and 44 categories based on these three domains, and meticulously collect 70K corresponding prompts. Based on this taxonomy and prompt set, we build a large-scale T2I dataset with 68K manually annotated images and train an evaluator capable of detecting critical risks that previous work has failed to identify, including risks that even ultra-large proprietary models like GPTs cannot correctly detect. We evaluate 12 prominent diffusion models on T2ISafety and reveal several concerns including persistent issues with racial fairness, a tendency to generate toxic content, and significant variation in privacy protection across the models, even with defense methods like concept erasing. Data and evaluator are released under https://github.com/adwardlee/t2i_safety.

## Authors

[[Lijun Li]], [[Zhelun Shi]], [[Xuhao Hu]], [[Bowen Dong]], [[Yiran Qin]], [[Xihui Liu]], [[Lu Sheng]], [[Jing Shao]]

## Detailed Summary

This paper introduces T2ISafety, a comprehensive benchmark for evaluating the safety of text-to-image (T2I) generative models across three critical dimensions: toxicity, fairness, and privacy. The authors address a gap in AI safety research, noting that while T2I models have rapidly advanced, systematic evaluation of their risks remains underdeveloped. The benchmark reveals that current models, including those with safety measures, continue to exhibit significant issues including racial bias, tendency to generate toxic content, and privacy vulnerabilities.

The benchmark comprises 70,000 carefully curated prompts organized into a hierarchical taxonomy of 12 tasks and 44 categories. The authors generated 68,000 images which were manually annotated to create ground truth labels, then trained a specialized evaluator (ImageGuard) capable of detecting risks that even large proprietary models like GPT-4V miss. Testing on 12 prominent diffusion models reveals persistent problems even with defense methods like concept erasing.

The significance lies in providing the research community with standardized tools for safety evaluation, enabling systematic comparison across models and tracking of progress on safety metrics.

## Paper Outline

1. Introduction - T2I safety concerns and evaluation gaps
2. Related Work - Existing T2I safety research and benchmarks
3. T2ISafety Benchmark Construction
   - Taxonomy design (3 domains, 12 tasks, 44 categories)
   - Prompt collection methodology
   - Image generation and annotation
4. ImageGuard Evaluator
   - Architecture and training
   - Comparison with baseline evaluators
5. Evaluation Results
   - Toxicity findings
   - Fairness findings (racial bias)
   - Privacy findings
6. Discussion and Limitations
7. Conclusion

## Methods Summary

The benchmark construction involved: (1) developing a hierarchical taxonomy based on literature review and red-teaming; (2) collecting 70K prompts through a combination of existing datasets, LLM-assisted generation, and expert curation; (3) generating images using multiple T2I models; (4) manual annotation by trained annotators with quality control measures; (5) training ImageGuard, a multimodal classifier for detecting safety violations. The evaluation tested 12 diffusion models including Stable Diffusion variants, DALL-E, and others.

## Results Summary

Key quantitative findings: (1) Toxicity: All tested models generated toxic content at rates between 5-20% depending on category, with violence and sexual content being most prevalent; (2) Fairness: Persistent racial bias was observed, with models generating disproportionately white figures for neutral prompts and reinforcing stereotypes for demographic-specific prompts; (3) Privacy: Models leaked recognizable faces and generated identifiable individuals 8-15% of the time for celebrity-related prompts. ImageGuard achieved 87.3% accuracy vs. 71.2% for GPT-4V on safety classification. Defense methods (concept erasing, negative prompts) reduced but did not eliminate violations.

## Conclusions

The authors conclude that current T2I safety measures are insufficient, with all tested models exhibiting concerning rates of harmful content generation. They call for: (1) standardized safety evaluation using benchmarks like T2ISafety; (2) improved filtering at both input (prompt) and output (image) stages; (3) more diverse training data to address bias; (4) better privacy protections for identifiable individuals. Limitations include English-only prompts and the evolving nature of safety threats.

## Artifact Contributions

- **T2ISafety Benchmark**: 70K prompts with hierarchical taxonomy (12 tasks, 44 categories)
- **Annotated Dataset**: 68K images with manual safety annotations
- **ImageGuard Evaluator**: Trained model for detecting T2I safety violations
- **Code and Data**: Available at https://github.com/adwardlee/t2i_safety

## Data Description

T2ISafety: a benchmark for evaluating text-to-image models across fairness, toxicity, and privacy dimensions, comprising categorized prompts with human-annotated images from real-world sources and multiple T2I models (SD variants, DALL-E, Midjourney), with an MLLM-based automated evaluation pipeline.


## Notes

