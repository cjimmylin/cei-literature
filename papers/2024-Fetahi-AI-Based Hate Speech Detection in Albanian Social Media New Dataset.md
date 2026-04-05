---







































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: LSRC0543
type: journalArticle
short_title: "AI-Based Hate Speech Detection in Albanian Social Media: New Dataset and Mobile Web Application Integration"
year: 2024
first_author: "[[Etrit Fetahi]]"
last_author: "[[Xhemal Zenuni]]"
authors: Etrit Fetahi; Majlinda Hamiti; Arianit Susuri; Jaumin Ajdari; Xhemal Zenuni
doi: 10.3991/ijim.v18i24.50851
url: "https://online-journals.org/index.php/i-jim/article/view/50851"
external_pdf: "https://online-journals.org/index.php/i-jim/article/download/50851/15687"
publication: "International Journal of Interactive Mobile Technologies"
CONF-CC: "International Journal of Interactive Mobile Technologies"
pdf_extract: "PDF Extracts/2024/2024-Fetahi-AI-Based Hate Speech Detection in Albanian Social Media New Dataset.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2024/2024-Fetahi-AI-Based Hate Speech Detection in Albanian Social Media New Dataset.pdf]]"
DATE_ADDED: 20260213
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "Albanian"
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
newtags: 
LLM_assessed: NA
DATA_URL: "NA"
tags: 
abstract: "This paper aims to advance AI-based hate speech (HS) detection in the Albanian language, which is resource-limited in natural language processing (NLP). Addressing the challenge of limited data, we developed a human-annotated dataset of over 11,000 comments, carefully curated from various Albanian social media platforms, containing a substantial number of HS instances. The dataset was annotated using a detailed two-layer taxonomy to capture the complex dimensions of HS."
CONFERENCE: "Journal"
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
author_country: "US"
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 80
is_benchmark: "No"
is_eval: "No"
is_dataset: "Yes"
data_description: "Annotated dataset for hate speech detection"
data_metrics: "Not specified"
---
# AI-Based Hate Speech Detection in Albanian Social Media: New Dataset and Mobile Web Application Integration

## Authors

[[Etrit Fetahi]], [[Majlinda Hamiti]], [[Arianit Susuri]], [[Jaumin Ajdari]], [[Xhemal Zenuni]]

## Metadata

**Authors:** Etrit Fetahi, Majlinda Hamiti, Arianit Susuri, Jaumin Ajdari, Xhemal Zenuni

**Year:** 2024

**Type:** journalArticle

**Venue:** International Journal of Interactive Mobile Technologies

**DOI:** [10.3991/ijim.v18i24.50851](https://doi.org/10.3991/ijim.v18i24.50851)

**Languages:** Albanian

## Links

- **DOI:** https://doi.org/10.3991/ijim.v18i24.50851
- **URL:** https://online-journals.org/index.php/i-jim/article/view/50851

## Abstract

Develops human-annotated dataset of over 11,000 comments from Albanian social media platforms with a two-layer taxonomy for hate speech. Three expert annotators with Fleiss kappa of 0.62. Naive Bayes with TF-IDF achieves F1=0.80 binary, XGBoost F1=0.77 multiclass.

## Summary

This paper develops a human-annotated dataset of over 11,000 comments from Albanian social media platforms for hate speech detection, using a two-layer taxonomy annotated by three expert annotators with a Fleiss kappa inter-annotator agreement of 0.62. The authors evaluate traditional machine learning approaches rather than modern transformer models, finding that Naive Bayes with TF-IDF achieves F1=0.80 for binary classification while XGBoost achieves F1=0.77 for multiclass classification. The work also integrates the hate speech detection system into a mobile web application for real-time moderation. This dataset addresses the critical lack of annotated resources for Albanian, a low-resource language, and provides a foundation for future toxicity and safety research in Albanian NLP.

## Data Description

Human-annotated dataset of over 11,000 comments from Albanian social media platforms with a two-layer taxonomy for hate speech detection, annotated by three experts with Fleiss kappa of 0.62.


## Detailed Summary

This paper advances AI-based hate speech detection for the Albanian language, a low-resource language in NLP, by developing a human-annotated dataset of over 11,000 comments carefully curated from Albanian social media platforms, primarily Facebook. The data was collected by identifying 84 provocative and controversial posts to maximize hate speech instances, with 11,343 comments selected for annotation. Three expert annotators from Kosovo, fluent Albanian speakers with computer science backgrounds, applied a two-layer taxonomy: a binary classification layer (hate/non-hate) and a granular second layer distinguishing General HS, Religious HS, Political HS, and Ethnicity HS. Majority voting determined final labels, achieving a Fleiss's Kappa of 0.62 (substantial agreement). The final dataset contains 6,131 neutral comments (54.05%) and 5,212 hate comments (45.94%), with the multiclass distribution showing General HS (34.39%), Religious HS (5.27%), Ethnicity HS (4.98%), and Political HS (1.30%). The authors evaluated four ML algorithms (SVM, Naive Bayes, Random Forest, XGBoost) with two vectorization techniques (TF-IDF, CountVectorizer) in both raw and pre-processed configurations, and deployed the best model as a mobile web application for real-time detection.

## Paper Outline

1. Introduction - Motivation for HS detection in low-resource Albanian language
2. Related Work - Existing Albanian datasets (Shaj, Zenuni et al., Raufi et al., Ajvazi et al.), ML approaches for HS detection
3. Materials and Methods - Methodology overview, data collection from Facebook, annotation process with two-layer taxonomy, quality assurance via Fleiss's Kappa
4. Experimental Setup - ML algorithms (SVM, NB, RF, XGBoost), pre-processing techniques (stop words, lowercasing, punctuation removal, emoji conversion), text vectorization (TF-IDF, CountVectorizer), evaluation metrics, LIME for error analysis
5. Results - Dataset statistics, binary classification results, multiclass classification results, error analysis, practical web application
6. Discussion - Strengths and weaknesses, comparison with existing research, practical implications, future directions
7. Conclusion

## Methods Summary

The study employs four ML algorithms (SVM, Naive Bayes, Random Forest, XGBoost) paired with TF-IDF and CountVectorizer text vectorization techniques. Each configuration is tested with and without pre-processing (Albanian stop word removal, lowercasing, punctuation/number removal, emoji-to-text conversion). All classifiers use default parameters for fairness and consistency, and 5-fold cross-validation is used for evaluation. Error analysis employs LIME (Local Interpretable Model-Agnostic Explanations) to identify misclassification patterns. The best-performing binary model (NB + TF-IDF) is deployed as a mobile web application using Python Flask backend with HTML-CSS frontend for real-time hate speech detection.

## Results Summary

In binary classification, Naive Bayes with TF-IDF achieved the highest F1 score of 0.80, with SVM + TF-IDF achieving a comparable 0.79. For multiclass classification, XGBoost consistently outperformed other models with an F1 score of 0.77 across all setups, while NB dropped to 0.65-0.73. A notable finding is that pre-processing techniques consistently reduced model performance across all configurations, suggesting that raw text inputs with TF-IDF features are already highly representative for Albanian language classification and that the lack of advanced NLP tools (POS tagging, stemming, lemmatization) for Albanian limits pre-processing effectiveness. LIME error analysis revealed that polysemy (words with multiple meanings, e.g., "dhimbje"/pain mistaken for harmful context) and irony/sarcasm were primary sources of misclassification. Compared to existing Albanian datasets, the study achieves competitive F1 of 0.80 on a larger, more balanced dataset than prior work.

## Conclusions

The study demonstrates that hate speech detection in Albanian is achievable with good accuracy using traditional ML approaches despite limited NLP resources. Key findings include: TF-IDF outperforms CountVectorizer for Albanian text, NB excels for binary classification while tree-based XGBoost handles multiclass nuances better, and pre-processing is counterproductive due to the lack of Albanian NLP tools and the deviated language used on social media. Limitations include difficulty distinguishing nuanced HS categories in multiclass classification due to class imbalance (especially Political HS at 1.30%), challenges with implicit hate speech, sarcasm, and irony, and the lack of advanced NLP tools for Albanian. Future directions include exploring transfer learning with Transformer architectures, developing Albanian NLP tools, creating domain-specific word embeddings, and expanding the dataset through crowdsourcing.

## Artifact Contributions

- **Albanian HS Dataset**: 11,343 annotated comments with two-layer taxonomy (binary + 4-class), Fleiss's Kappa 0.62 (available upon request, subject to data protection guidelines)
- **Mobile Web Application**: Flask-based real-time HS detection tool using NB + TF-IDF model
- **Comparative Analysis**: Systematic evaluation of 16 ML configurations for Albanian HS detection

## Notes

**Source:** Language-Organized Benchmark Search (20260213), Agent B9
**Relevance:** Recent Albanian hate speech dataset with rigorous annotation. Evaluates ML models for bias detection in Albanian social media. Directly relevant to toxicity and safety in low-resource Albanian NLP.

## Tags

