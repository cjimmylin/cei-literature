---






































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: SFYCJJ2D
type: document
short_title: "How to Assess Your LLM Use Case for Bias and"
year: 2025
first_author: "[[Dominique Bouchard]]"
last_author: "[[Dominique Bouchard]]"
authors: "Dominique Bouchard"
url: "https://medium.com/cvs-health-tech-blog/how-to-assess-your-llm-use-case-for-bias-and-fairness-with-langfair-7be89c0c4fab"
external_pdf: "file:///Users/jimmylin/Zotero/storage/DJYXXBYZ/Bouchard - 2025 - How to Assess Your LLM Use Case for Bias and Fairness with LangFair.pdf"
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
newtags: "Bias & Fairness"
key_contribution: "Describes LangFair, a toolkit/library for assessing bias and fairness metrics in LLM use cases."
significance: "Provides a practical resource for practitioners to operationalize fairness auditing in industry deployments of LLMs."
tags: 
abstract: "Current AI evaluation methods relying on static, model-only tests fail to account for harms that emerge through sustained human-AI interaction. This paper proposes a shift towards evaluation based on interactional ethics, focusing on interaction harms like inappropriate parasocial relationships, social manipulation, and cognitive overreliance that develop over time. The authors present practical principles for designing interactive evaluations including ecologically valid scenarios, human impact metrics, and diverse human participation approaches."
CONF-CC: "N/A"
DATE_ADDED: 20260208
LLM_assessed: "Gemini"
DATA_URL: "https://github.com/cvs-health/langfair"
pdf_extract: "PDF Extracts/2025/2025-Bouchard-How to Assess Your LLM Use Case for Bias and.md"
local_pdf: "[[PDFs/2025/2025-Bouchard-How to Assess Your LLM Use Case for Bias and.pdf]]"
CONFERENCE: "Unknown"
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
is_benchmark: "No"
is_eval: "Yes"
is_dataset: "No"
data_description: "Evaluation methodology"
data_metrics: "Not specified"
ethics_perspective: "Bias & Fairness"
---
# How to Assess Your LLM Use Case for Bias and Fairness with LangFair

## Metadata

**Authors:** Bouchard, D.

**Year:** 2025

**Type:** document

## Links

- **URL:** https://medium.com/cvs-health-tech-blog/how-to-assess-your-llm-use-case-for-bias-and-fairness-with-langfair-7be89c0c4fab

## Abstract

Current AI evaluation methods relying on static, model-only tests fail to account for harms that emerge through sustained human-AI interaction. This paper proposes a shift towards evaluation based on interactional ethics, focusing on interaction harms like inappropriate parasocial relationships, social manipulation, and cognitive overreliance that develop over time. The authors present practical principles for designing interactive evaluations including ecologically valid scenarios, human impact metrics, and diverse human participation approaches.

## Authors

[[Dominique Bouchard]]

## Detailed Summary

This technical blog post introduces LangFair, a Python library developed by CVS Health for conducting bias and fairness assessments of LLM use cases. The authors argue that conventional approaches to LLM fairness evaluation rely on static benchmark datasets that fail to capture risks associated with specific deployment contexts. LangFair addresses this gap through a "Bring Your Own Prompts" (BYOP) approach, allowing practitioners to tailor bias and fairness evaluations to their particular use cases rather than relying on generic benchmarks that may not reflect real-world prompt distributions.

The library supports three main categories of assessment: toxicity (evaluating harmful or abusive language), stereotypes (identifying reinforcement of harmful group-based stereotypes), and counterfactual fairness (testing how outputs vary when protected attributes like gender or race are changed while keeping other prompt elements constant). For each category, LangFair provides multiple metrics. Toxicity metrics include Expected Maximum Toxicity, Toxicity Probability, and Toxic Fraction, all leveraging pre-trained toxicity classifiers (with detoxify-unbiased as default). Stereotype metrics include Stereotypical Associations, Cooccurrence Bias Score, and classifier-based Stereotype Fraction. Counterfactual metrics include sentiment bias and text similarity measures (ROUGE-L, BLEU, cosine similarity).

The post demonstrates LangFair's usage through a text summarization example using 1,000 conversations from the dialogsum-test dataset evaluated with Gemini Pro. The AutoEval class provides a streamlined two-line interface that automatically checks for Fairness Through Unawareness (FTU), generates responses and counterfactual responses, and calculates applicable metrics. Results showed very low toxicity (0.04% Toxic Fraction), moderate cooccurrence-based stereotype scores (0.32 Stereotypical Associations, 0.45 Cooccurrence Bias), high counterfactual similarity (0.83 cosine similarity), and near-zero sentiment bias (0.001), demonstrating low bias risk for the evaluated use case.

## Paper Outline

1. Introduction - Bias and Fairness in LLMs
   - Toxicity assessments
   - Stereotype assessments
   - Counterfactual assessments
2. Why LangFair? - Limitations of static benchmarks and BYOP approach
3. Example: Dialogue Summarization Use Case
4. Choosing Evaluation Metrics - Decision flowchart
5. Installing and Using LangFair
   - ResponseGenerator for generating LLM outputs
   - ToxicityMetrics class
   - StereotypeMetrics class
   - CounterfactualGenerator for FTU checking and counterfactual generation
   - CounterfactualMetrics class
6. AutoEval for Streamlined Assessment
7. Conclusion and Resources

## Methods Summary

LangFair implements a multi-step evaluation pipeline: (1) ResponseGenerator generates multiple (default 25) responses per prompt to leverage LLM stochasticity; (2) ToxicityMetrics computes toxicity scores using classifiers like detoxify-unbiased; (3) StereotypeMetrics calculates cooccurrence-based metrics (word associations) and classifier-based metrics; (4) CounterfactualGenerator checks for Fairness Through Unawareness by parsing prompts for protected attribute words, constructs counterfactual prompt pairs, and generates corresponding responses; (5) CounterfactualMetrics measures sentiment disparities and text similarity between counterfactual response pairs. The library uses LangChain for LLM integration and asyncio for efficient response generation. Evaluation thresholds are compared against values from original research papers (HELM study, etc.) for contextual interpretation.

## Results Summary

Demonstration with Gemini Pro on dialogsum-test summarization: Toxicity - 0.04% Toxic Fraction (10/25,000 responses flagged), 0.01 Expected Maximum Toxicity, 0.01 Toxicity Probability; inspection of flagged responses found none concerning. Stereotypes - 0.32 Stereotypical Associations (low vs. HELM benchmarks), 0.45 Cooccurrence Bias (low vs. original paper), 15.45% Stereotype Fraction for gender; inspection found no problematic responses. Counterfactual (gender) - 613/1000 prompts contained gender words (FTU not satisfied), 0.83 cosine similarity (high), 0.52 ROUGE-L (high similarity), 0.33 BLEU (good), 0.001 sentiment bias (near-zero). Overall conclusion: low bias risk for this summarization use case.

## Conclusions

LangFair provides a practical, use-case-specific approach to LLM fairness evaluation that addresses the limitations of static benchmark testing. The BYOP methodology ensures that bias assessments reflect the actual prompts and contexts where LLMs will be deployed. The library supports toxicity, stereotype, and counterfactual assessments with multiple metrics per category, enabling comprehensive fairness audits. The AutoEval class simplifies the evaluation workflow for text generation and summarization use cases. The authors emphasize that LangFair focuses on output-based metrics practical for governance audits without requiring access to internal model states, making it suitable for auditing both proprietary and open-source LLMs in production environments.

## Artifact Contributions

- LangFair Python library: https://github.com/cvs-health/langfair
- Documentation site and demo notebooks available
- Companion research paper: https://arxiv.org/abs/2407.10853

## Data Description

LangFair is an open-source Python library for bias and fairness assessment of LLM use cases, implementing toxicity, stereotype, and counterfactual fairness metrics with a bring-your-own-prompts approach.


## Notes

