---
Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0513
type: journalArticle
short_title: "Italian Linguistic Features for Toxic Language Detection in Social Media"
year: 2023
first_author: "[[Leonardo Grotti]]"
last_author: "[[Leonardo Grotti]]"
authors: "Leonardo Grotti"
url: "https://journals.openedition.org/ijcol/1367"
external_pdf: "http://journals.openedition.org/ijcol/pdf/1367"
publication: "Italian Journal of Computational Linguistics"
CONF-CC: "Italian Journal of Computational Linguistics"
pdf_extract: "PDF Extracts/2023/2023-Grotti-Italian Linguistic Features for Toxic Language Detection in Social.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2023/2023-Grotti-Italian Linguistic Features for Toxic Language Detection in Social.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: Italian
cultures_nationalities_list: Italian
languages_list: Italian
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
LLM_assessed: BERT
DATA_URL: NA
tags: 
abstract: "Framework for analyzing toxic language on Italian Facebook pages. Assesses toxic vs. non-toxic comments via length, vocabulary diversity, and linguistic standardness. Fine-tunes PoliBERT, UmBERTo, and bert-base-italian-xxl-uncased models."
CONFERENCE: Journal
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Toxicity & Hate Speech"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: CA
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 86
is_benchmark: No
is_eval: Yes
is_dataset: No
data_description: "Evaluation framework"
data_metrics: "Not specified"
---
# Italian Linguistic Features for Toxic Language Detection in Social Media

## Authors

[[Leonardo Grotti]]

## Metadata

**Authors:** Leonardo Grotti

**Year:** 2023

**Type:** journalArticle

**Venue:** Italian Journal of Computational Linguistics

**Languages:** Italian

## Links

- **URL:** https://journals.openedition.org/ijcol/1367

## Abstract

Framework for analyzing toxic language on Italian Facebook pages. Assesses toxic vs. non-toxic comments via length, vocabulary diversity, and linguistic standardness. Fine-tunes PoliBERT, UmBERTo, and bert-base-italian-xxl-uncased models.

## Summary

This study develops a framework for analyzing toxic language on Italian social media, building upon the multilingual LiLaH project that analyzes hateful content across Dutch, English, French, Slovene, and Croatian. The authors examine linguistic features of Italian toxic comments on Facebook pages from the HaSpeeDe dataset, finding that toxic comments tend to be longer and contain fewer unique emojis compared to non-toxic comments while exhibiting similar lexical diversity. They fine-tune three Italian pre-trained language models (PoliBERT, UmBERTo, and bert-base-italian-xxl-uncased) on toxicity detection, but find that despite the correlation between linguistic features and toxicity, their inclusion actually worsens model performance. The work extends the LiLaH project's standardized framework to Italian, addressing the lack of systematic approaches to hate speech detection in Italian NLP research.

## Data Description

Framework analyzing toxic language on Italian Facebook pages using linguistic features. Evaluates Italian BERT models fine-tuned on toxicity detection task. Dataset drawn from Italian social media but no public URL provided.


## Detailed Summary

This study by Leonardo Grotti (University of Antwerp) addresses the detection of toxic language on Italian social media, building upon the standardized framework of the multilingual LiLaH (Linguistic Landscape of Hate Speech) project that analyzes hateful content across Dutch, English, French, Slovene, and Croatian. Using the HaSpeeDe 2018 Facebook dataset (4,000 comments: 2,059 toxic, 1,941 non-toxic), the author examines three categories of linguistic features: average comment length, lexical diversity (type-to-token ratio, content-to-function-words ratio, emoji usage), and linguistic standardness (punctuation-to-non-punctuation ratio, non-standard linguistic forms). The analysis confirms that Italian toxic comments tend to be significantly longer than non-toxic ones (consistent with English and Dutch findings but contrary to Slovene), contain fewer unique emojis, and exhibit similar lexical diversity between categories. Three Italian pre-trained language models (PoliBERT, UmBERTo, bert-base-italian-xxl-uncased) are fine-tuned for toxicity detection, with UmBERTo achieving the best F1 of 0.78. Despite statistically significant correlations between linguistic features and toxicity, incorporating these features via a GradientBoostClassifier actually worsens the best model's performance, suggesting that transformer models already capture these patterns implicitly.

## Paper Outline

1. Introduction - Toxic language prevalence on social media, LiLaH project context
2. Related Work - Definitions (HS vs. toxic language vs. SUD), CMC and social media language, toxic language detection methods
3. Data and Method - Hypotheses, HaSpeeDe dataset description, lexical diversity metrics, linguistic standardness measures, model fine-tuning setup
4. Results - Linguistic feature analysis (length, vocabulary diversity, standardness), model performance, feature inclusion experiments, error analysis
5. Conclusions

## Methods Summary

The study uses the HaSpeeDe 2018 Facebook dataset with binary toxic/non-toxic labels. Linguistic features are computed using NLTK Italian tokenizer, SciPy biserial correlation coefficients, and the emoji Python package. Three hypotheses test differences in average length, lexical diversity, and linguistic standardness between toxic and non-toxic comments. Three Italian BERT variants are fine-tuned for binary classification. A GradientBoostClassifier is then used to test whether combining model predictions with extracted linguistic features improves performance. Error analysis examines misclassifications to identify challenges such as polysemy, irony, and context-dependent expressions.

## Results Summary

Toxic Italian comments are significantly longer than non-toxic ones (median 15 vs. 9 words, p<0.001). Both categories show similar type-to-token ratios and content-to-function-word ratios, but non-toxic comments contain more unique emojis. UmBERTo achieves the best binary classification F1 of 0.78, followed by bert-base-italian-xxl-uncased (0.76) and PoliBERT (0.75). Adding linguistic features to UmBERTo predictions via GradientBoostClassifier reduces performance to F1 0.76, indicating that the linguistic features, while correlated with toxicity, do not provide additional signal beyond what transformers already capture. Error analysis reveals that polysemy (words with both neutral and offensive meanings), irony/sarcasm, and implicit hate speech are the main sources of misclassification.

## Conclusions

The study establishes a common framework for investigating toxic language in Italian, comparable to findings in Dutch, English, French, Slovene, and Croatian through the LiLaH project. Key limitations include the small dataset size, the focus on Facebook comments only, and the annotation quality issues inherited from HaSpeeDe (Fleiss kappa of only 0.26). Future work should expand to other Italian social media platforms, develop larger annotated datasets, and investigate whether more sophisticated feature integration methods can complement transformer models.

## Artifact Contributions

No publicly released artifacts identified. The study uses the existing HaSpeeDe 2018 Facebook dataset and publicly available pre-trained Italian language models.

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B8
**Relevance:** Italian-specific toxic language detection using linguistic features, providing analysis framework similar to LiLaH project.

## Tags

