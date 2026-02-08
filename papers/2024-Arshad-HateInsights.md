---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: EZIKWT8F
type: journalArticle
short_title: HateInsights
year: 2025
first_author: "[[Muhammad Umair Arshad]]"
authors: "Muhammad Umair Arshad; Waseem Shahzad"
url: "https://peerj.com/articles/cs-2372"
external_pdf: "file:///Users/jimmylin/Zotero/storage/5GTBH6XA/Arshad and others - 2024 - HateInsights A Fine-Grained Benchmark for Explainable Hate Speech Detection.pdf"
national_ethnic_cultural: N/A
religious_values: N/A
moral_psychology: N/A
newtags: "Toxicity & Hate Speech"
key_contribution: "Introduced HateInsights, a fine-grained benchmark for explainable hate speech detection that evaluates both classification accuracy and the quality of model rationales."
significance: "Emphasizes 'explainability' in toxicity detection, providing resources to evaluate *why* a model flags content, which is crucial for trust and error analysis in moderation systems."
tags: 
abstract: "The persistence of hate speech continues to pose an obstacle in the realm of online social media. Despite the continuous evolution of advanced models for identifying hate speech, the critical dimensions of interpretability and explainability have not received proportional scholarly attention. In this article, we introduce the HateInsights dataset, a groundbreaking benchmark in the ﬁeld of hate speech datasets, encompassing diverse aspects of this widespread issue. Within our dataset, each indivi"
ethics_overall: No
virtue_ethics: No
deontological_ethics: No
utilitarian_ethics: No
ethics_perspective: "Toxicity & Hate Speech"
is_benchmark: Yes
is_eval: No
is_dataset: Yes
data_description: "Benchmark dataset for hate speech detection"
data_metrics: "Not specified"
pdf_extract: "PDF Extracts/2024/2024-Arshad-HateInsights.md"
local_pdf: [[PDFs/2024/2024-Arshad-HateInsights.pdf]]
---
# HateInsights: A Fine-Grained Benchmark for Explainable Hate Speech Detection

## Metadata

**Authors:** Arshad, Muhammad Umair; Shahzad, Waseem

**Year:** 2024

**Publication:** PeerJ Computer Science

**Type:** journalArticle

## Links

- **URL:** https://peerj.com/articles/cs-2372

## Abstract

The persistence of hate speech continues to pose an obstacle in the realm of online social media. Despite the continuous evolution of advanced models for identifying hate speech, the critical dimensions of interpretability and explainability have not received proportional scholarly attention. In this article, we introduce the HateInsights dataset, a groundbreaking benchmark in the ﬁeld of hate speech datasets, encompassing diverse aspects of this widespread issue. Within our dataset, each indivi

## Authors

[[Muhammad Umair Arshad]], [[Waseem Shahzad]]

## Detailed Summary

HateInsights introduces a groundbreaking benchmark dataset for hate speech detection in Urdu, focusing specifically on model interpretability and explainability. The authors address a critical gap in hate speech research: while advanced models achieve high classification accuracy, they often lack transparency in explaining their decisions. The dataset contains 11,782 annotated samples from Twitter and Facebook, where each post is annotated from dual perspectives: (1) a 3-class classification (hate speech, offensive language, normal discourse), and (2) rationales that identify specific text segments supporting the assigned label.

The study emphasizes the unique challenges of processing Urdu text, including its right-to-left orientation, lack of capitalization, free word-order structure, and absence of well-established tokenizers. The dataset addresses the use of culturally-specific terms that may appear neutral but carry hateful connotations (e.g., "black", "Niazi", "Pathan" for racial/caste references, or "non-believer", "Sunni", "Shia" for religious targeting). The researchers employed three advanced models (XLM-RoBERTa base and others) combined with explainability techniques (SHAP, LIME, Integrated Gradients) to evaluate both classification accuracy and explanation quality.

A key finding is that models demonstrating exceptional classification proficiency may still yield suboptimal outcomes on explainability metrics like model plausibility and faithfulness. The study shows that models trained with human-annotated rationales produce more human-like explanations, suggesting that incorporating rationale-based training improves model interpretability. This work contributes to the broader goal of developing transparent, fair, and trustworthy hate speech detection systems.

## Paper Outline

1. Introduction - Problem of hate speech and need for explainable detection
2. Related Work
   - Hate speech detection literature
   - Hate speech detection in Urdu
   - Explainable hate speech detection
3. Dataset Collection and Annotation Procedure
   - Dataset curation from Twitter
   - Data annotation process
   - Class labels and ground truth attention
4. Proposed Approach
   - Data preprocessing pipeline
   - Models (XLM-RoBERTa, etc.)
   - Explainability methods (SHAP, LIME, IG)
5. Experiments and Results
6. Conclusion

## Methods Summary

Data was collected using Twint from Twitter based on hate-related hashtags and keywords in Urdu, yielding approximately 10,000 tweets. Four student annotators (selected from six candidates) classified texts into hateful, offensive, or normal categories using majority voting. For hate/offensive labels, annotators identified specific text spans (rationales) supporting their decisions. Ground truth attention vectors were created by normalizing annotated rationales using softmax. The preprocessing pipeline included UTF-8 formatting, lowercase conversion, removal of ambiguous characters, and text expansion. Three sophisticated LLMs were fine-tuned for classification, then integrated with three explainability techniques (SHAP, LIME, Integrated Gradients) for word-level importance attribution.

## Results Summary

The study achieved strong classification performance with XLM-RoBERTa producing competitive F1-scores on the Urdu hate speech dataset. Critically, the research revealed a disconnect between classification accuracy and explainability quality - high-performing classifiers did not necessarily provide plausible or faithful explanations. Models trained with human-annotated rationales showed improved alignment with human reasoning patterns. The average tokens for rationales in hateful speech was seven per sample, compared to an average of 35.8 tokens per post overall, indicating that hate markers are often localized to specific phrases.

## Conclusions

The research demonstrates that achieving high classification accuracy alone is insufficient for trustworthy hate speech detection - models must also provide transparent and understandable explanations. The HateInsights dataset fills a crucial gap for Urdu language processing and explainable AI research. The authors advocate for regulation-compliant AI systems (like GDPR's "right to explanation") that can articulate their reasoning rather than functioning as black boxes.

## Artifact Contributions

- HateInsights dataset: 11,782 Urdu hate speech samples with rationale annotations
- Gold standard annotation scheme with word-level and comment-level spans
- Open-source codebase for reproduction
- Computational resources including neural language models and interpretability tools

## Notes

