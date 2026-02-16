---





Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: XFBL55N2
type: journalArticle
short_title: "Understanding hate speech"
year: 2025
first_author: "[[Muhammad Umair Arshad]]"
last_author: "[[Waseem Shahzad]]"
authors: "Muhammad Umair Arshad; Waseem Shahzad"
doi: 10.7717/peerj-cs.2372
url: "https://peerj.com/articles/cs-2372"
external_pdf: "file:///Users/jimmylin/Zotero/storage/P2VZGTF3/Arshad and Shahzad - 2024 - Understanding hate speech the HateInsights dataset and model interpretability.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "Urdu"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Toxicity & Hate Speech"
key_contribution: "Introduced HateInsights, a hate speech dataset with dual evaluations (class labels + rationales) to assess model interpretability alongside classification performance."
significance: "Reveals that high-performing hate speech classifiers often fail on explainability metrics (plausibility/faithfulness), arguing that effective moderation requires transparent reasoning, not just accurate flag-prediction."
tags: 
abstract: "The persistence of hate speech continues to pose an obstacle in the realm of online social media. Despite the continuous evolution of advanced models for identifying hate speech, the critical dimensions of interpretability and explainability have not received proportional scholarly attention. In this article, we introduce the HateInsights dataset, a groundbreaking benchmark in the ﬁeld of hate speech datasets, encompassing diverse aspects of this widespread issue."
DATE_ADDED: 20260208
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Toxicity & Hate Speech"
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark for bias and fairness annotated dataset for hate speech detection"
data_metrics: "Not specified"
LLM_assessed: "BERT, RoBERTa"
DATA_URL: "https://github.com/twintproject/twint"
pdf_extract: "PDF Extracts/2024/2024-Arshad-Understanding hate speech.md"
local_pdf: "[[PDFs/2024/2024-Arshad-Understanding hate speech.pdf]]"
---
# Understanding hate speech: the HateInsights dataset and model interpretability

## Metadata

**Authors:** Arshad, Muhammad Umair; Shahzad, Waseem

**Year:** 2024

**Publication:** PeerJ Computer Science

**Type:** journalArticle

**DOI:** [10.7717/peerj-cs.2372](https://doi.org/10.7717/peerj-cs.2372)

**Pages:** e2372

**Volume/Issue:** Vol. 10

## Links

- **URL:** https://peerj.com/articles/cs-2372
- **DOI:** https://doi.org/10.7717/peerj-cs.2372

## Abstract

The persistence of hate speech continues to pose an obstacle in the realm of online social media. Despite the continuous evolution of advanced models for identifying hate speech, the critical dimensions of interpretability and explainability have not received proportional scholarly attention. In this article, we introduce the HateInsights dataset, a groundbreaking benchmark in the ﬁeld of hate speech datasets, encompassing diverse aspects of this widespread issue. Within our dataset, each individual post undergoes thorough annotation from dual perspectives: ﬁrstly, conforming to the established 3-class classiﬁcation paradigm that includes hate speech, offensive language, and normal discourse; secondly, incorporating rationales that outline speciﬁc segments of a post supporting the assigned label (categorized as hate speech, offensive language, or normal discourse). Our exploration yields a signiﬁcant ﬁnding by harnessing cutting-edge state-of-the-art models: even models demonstrating exceptional proﬁciency in classiﬁcation tasks yield suboptimal outcomes in crucial explainability metrics, such as model plausibility and faithfulness. Furthermore, our analysis underscores a promising revelation concerning models trained using human-annotated rationales. To facilitate scholarly progress in this realm, we have made both our dataset and codebase accessible to fellow researchers. This initiative aims to encourage collaborative involvement and inspire the advancement of the hate speech detection approach characterized by increased transparency, clarity, and fairness.

## Authors

[[Muhammad Umair Arshad]], [[Waseem Shahzad]]

## Detailed Summary

This paper addresses the critical gap between classification performance and interpretability in hate speech detection models. While existing models can accurately classify hate speech, they often fail to explain their decisions in ways that align with human reasoning. The authors introduce HateInsights, the first public Urdu hate speech dataset that includes both classification labels and human-annotated rationales explaining why content is classified as hateful, offensive, or neutral.

The dataset contains 11,782 posts collected from Twitter and Facebook, annotated by trained students from FAST National University. Each post receives dual annotations: a 3-class label (hate, offensive, neutral) determined by majority voting among three annotators, and word-level rationale annotations highlighting the specific text segments that justify the classification. This dual-annotation approach enables evaluation of both classification accuracy and explainability.

The research evaluates three state-of-the-art models (XLM-RoBERTa, FinBERT, and BERT-Hinglish) combined with three explainability methods (SHAP, LIME, and Integrated Gradients). A key finding is that models achieving excellent classification performance (XLM-RoBERTa reaches 95% accuracy) still produce suboptimal results on explainability metrics like plausibility and faithfulness. This reveals a fundamental tension in current AI systems: they can identify hate speech accurately but cannot transparently explain their reasoning in ways that match human judgment.

## Paper Outline

1. Introduction
   - Challenge of hate speech in online social media
   - Gap between classification accuracy and interpretability
   - Importance of explainable AI for content moderation
2. Related Work
   - Existing hate speech datasets and their limitations
   - Hate speech detection in Urdu language
   - Explainable AI methods for hate speech
3. Dataset Collection and Annotation
   - Data sources (Twitter and Facebook)
   - Annotation process and annotator selection
   - Dual annotation: class labels and rationales
   - Ground truth attention computation
4. Proposed Approach
   - Data preprocessing pipeline
   - Fine-tuning LLMs (XLM-RoBERTa, FinBERT, BERT-Hinglish)
   - Feature attribution methods (SHAP, LIME, Integrated Gradients)
5. Evaluation Metrics
   - Sentence-level classification metrics
   - Explainability metrics (plausibility, faithfulness)
6. Results and Discussion
   - Classification performance comparison
   - Explainability analysis
7. Conclusion

## Methods Summary

The methodology involves constructing a dual-annotated Urdu hate speech dataset and evaluating model interpretability. Data was collected using Twint from Twitter, focusing on common hate-related keywords. Annotation followed a two-stage process: (1) three-class classification through majority voting among three annotators, and (2) rationale annotation where annotators highlighted text segments supporting their classification. Ground truth attention vectors were computed by normalizing overlapping rationale annotations using softmax.

Three transformer-based models were fine-tuned: XLM-RoBERTa (multilingual, 100 languages), FinBERT (fine-tuned for hate speech), and BERT-Hinglish (trained on Roman Hindi). Models were evaluated using stratified 8:1:1 train/dev/test splits with hyperparameters optimized through Hugging Face APIs. For explainability, SHAP, LIME, and Integrated Gradients methods provided feature attribution scores compared against human rationale annotations using IOU F1-score, token F1-score, comprehensiveness, and sufficiency metrics.

## Results Summary

- Classification Performance: XLM-RoBERTa achieved best results with 95% accuracy, 96% precision, 95% recall, 95% F1-score, and 99% AUROC
- Model Comparison: XLM-RoBERTa significantly outperformed BERT-Hinglish (80% accuracy) and FinBERT (84% accuracy)
- Explainability Gap: Despite excellent classification, all models showed suboptimal explainability scores
- Best Explainability: XLM-RoBERTa with LIME achieved highest token-level accuracy; XLM-RoBERTa with SHAP achieved best token-level F1-score
- IOU Performance: Integrated Gradients with XLM-RoBERTa yielded superior IOU F1-scores
- Challenge Areas: Distinguishing between Hate and Offensive classes proved most difficult due to linguistic similarity

## Conclusions

The research demonstrates that high classification accuracy does not guarantee interpretable AI decisions. Even the best-performing model (XLM-RoBERTa with 95% accuracy) produces explanations that only partially align with human reasoning. The introduction of HateInsights with its dual-annotation approach provides a crucial resource for developing hate speech detection systems that are both accurate and transparent. The findings emphasize that effective content moderation requires not just correct predictions but also reasoning that humans can verify and trust.

## Artifact Contributions

- HateInsights dataset: 11,782 Urdu social media posts with 3-class labels and word-level rationale annotations
- First publicly available Urdu hate speech dataset with explainability annotations
- Detailed corpus statistics: 265,116 total words, 23,934 unique words
- Open-source codebase for model training and evaluation
- Comparative benchmark results for multiple models and explainability methods

## Data Description

The study introduces HateInsights, a benchmark dataset of 11,782 Urdu-language social media posts from Twitter and Facebook, annotated for three-class classification (hate speech, offensive language, normal discourse) with word-level rationales. Three transformer-based models are fine-tuned and evaluated: XLM-RoBERTa Base, FinBERT, and BERT-Hinglish, with explainability analysis using SHAP, LIME, and Integrated Gradients feature attribution methods.


## Notes


## Citation Info

40 citations (Semantic Scholar/DOI) [2025-08-27] 2 citations (Semantic Scholar/DOI) [2025-08-23] 2 citations (Crossref/DOI) [2025-08-23]
