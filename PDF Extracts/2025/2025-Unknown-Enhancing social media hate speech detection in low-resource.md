---
title: "2025-Unknown-Enhancing social media hate speech detection in low-resource - PDF Extract"
source_pdf: "2025-Unknown-Enhancing social media hate speech detection in low-resource.pdf"
pages: 30
extracted_at: "2026-02-13T14:50:56.804985"
---

# PDF Extract: 2025-Unknown-Enhancing social media hate speech detection in low-resource

**Source PDF:** 2025-Unknown-Enhancing social media hate speech detection in low-resource.pdf
**Total Pages:** 30

---

## Content

```
--- Page 1 ---

Vol.:(0123456789)
Social Network Analysis and Mining (2025) 15:82 
https://doi.org/10.1007/s13278-025-01497-w
ORIGINAL ARTICLE
Enhancing social media hate speech detection in low‑resource 
languages using transformers and explainable AI
Endrit Fetahi1 · Arsim Susuri1 · Mentor Hamiti2 · Zenun Kastrati3 · Ercan Canhasi1 · Arta Misini1
Received: 6 March 2025 / Revised: 5 July 2025 / Accepted: 9 July 2025 / Published online: 31 July 2025 
© The Author(s) 2025
Abstract
Hate speech (HS) on social media exposes public discourse and community well-being. Despite its prevalence, majority of 
the research and technological advances have focused on rich-resourced languages. In contrast, Albanian, a language marked 
by dialects, limited NLP tools, and scarcity of annotated data, remains underexplored. To address this gap, this paper explores 
the enhancement of automatic hate speech detection in Albanian social media using advanced deep neural techniques. We 
collected a real-life dataset comprising 20,860 Facebook comments manually annotated using a rigorous multi-annotator 
process. Various techniques, including machine learning, deep neural networks, and transformers, are tested on the collected 
dataset. Our findings show that character-level 4-gram TF-IDF consistently reinforces ML classifiers effective with informal 
spelling and slang. However, the fine-tuned transformer XLM-RoBERTa achieves the highest performance with an F1-score 
up to 86%. These results mark a new benchmark for Albanian HS detection and highlight the impact of thorough feature 
engineering and robust representation techniques in a low-resource context. We also carried out an error analysis using both 
manual inspection and explainable AI approaches such as SHAP and LIME. Key language challenges include dialectal writ-
ing, short sentences, and implicit insults. These insights highlight the importance of domain-aligned embedding resources, 
more extensive annotation, and fine-grained context handling for improved detection. This study establishes a new state-of-
the-art result for Albanian hate speech detection, provides a valuable comparison of models and feature engineering, and 
underscores the potential of multilingual transformers in low-resource scenarios.
Keywords  Social media · Hate speech · Transformers · Machine learning · Deep learning · Feature engineering · 
Explainable AI (XAI)
1  Introduction
The rapid proliferation of social media over the past two 
decades has dramatically transformed how individuals inter-
act, share information, and discuss both personal and global 
events (Valkenburg 2022). Platforms such as Facebook, X 
(formerly Twitter), Instagram, and YouTube host billions 
of daily users, producing vast quantities of user-generated 
content that can quickly disseminate across the globe. 
While this connectivity has enriched public discourse and 
enhanced community engagement, it has also exacerbated 
the prevalence of harmful or malicious speech, which can 
incite hostility toward specific groups on the basis of ethnic-
ity, religion, gender, or other attributes (Fetahi et al. 2023).
Hate speech poses a significant concern for users, plat-
form moderators, and policymakers alike. Instances of hate 
speech have been documented in various social media con-
texts, from heated political debates to online gaming com-
munities, and are linked to broader societal issues, includ-
ing the radicalization of extremists and the perpetuation of 
harmful stereotypes (Parker and Ruths 2023; Solovev and 
Pröllochs 2022). Recognizing the disturbing impacts of hate 
speech, many social media companies have implemented 
manual or semi-automated content moderation systems to 
filter offensive content (Meta 2022; https://​devel​oper.x.​com/​
en/​blog/​succe​ss-​stori​es/​hatel​ab). Yet, the sheer scale and 
fast-paced nature of social media make manual moderation 
insufficient and prone to inconsistencies (Yin and Zubiaga 
2021).
 *	 Zenun Kastrati 
	
zenun.kastrati@lnu.se
1	
University of Prizren, Prizren, Kosovo
2	
South East European University, Tetovo, North Macedonia
3	
Linnaeus University, Växjö, Sweden

--- Page 2 ---

	
Social Network Analysis and Mining (2025) 15:82
82 
Page 2 of 30
In response, Natural Language Processing (NLP) has 
emerged as a crucial tool for automating hate speech detec-
tion, offering algorithms and computational methods that 
identify text for hateful content. Early studies focused on 
keyword detection or rule-based methods, while these meth-
ods struggled to capture the nuanced, context-dependent 
nature of hate speech (Gitari et al. 2015). Subsequently, 
researchers began turning to ML classification techniques, 
which provided more robust pattern recognition capabilities 
by analyzing lexical, syntactic, or semantic cues within text 
(Watanabe et al. 2018; Sandaruwan et al. 2019; Ketsbaia 
et al. 2020; Roy et al. 2020; Aulia and Budi 2019; Plaza-
Del-Arco et al. May 2020). Over time, the field advanced to 
include deep learning (DL) architectures, like Neural net-
works models (Roy et al. 2020; Tolba et al. 2021; Marreddy 
et al. 2022; Joshi et al. 2021; Pamungkas et al. 2021; Khan 
et al. 2022). These models automatically learn feature repre-
sentations from data, which can better account for complex 
linguistic structures and subtle forms of hate speech.
Most recently, transformer-based NLP models and vari-
ous multilingual adaptations, has shown significant improve-
ments in many text classification tasks, including hate speech 
detection (Mubarak et al. 2023; Beyhan et al. 2022; Genco-
glu 2021; Mohammadi and Chapon 2020; Ranasinghe and 
Zampieri 2022; Mozafari et al. 2020). Nonetheless, despite 
these advances, automating hate speech detection remains 
inherently challenging due to the subjective nature of what 
constitutes “hate” and the dynamic ways in which language 
evolves on social media. This complexity necessitates high-
quality datasets with diverse examples, careful annotation 
guidelines, and multi-faceted evaluation strategies.
In parallel with these advancements, Explainable Arti-
ficial Intelligence (XAI) methods have emerged to explain 
how complex models make decisions. Hate speech detectors, 
especially deep neural and transformer-based architectures, 
often function as 'black boxes'. These models lack transpar-
ency in the decision-making processes. Through techniques 
like SHAP and LIME, both examined in this paper, we can 
pinpoint misinterpretations or unfair patterns, uncovering 
insights leading to more transparent and equitable online 
moderation systems.
However, in many low-resource contexts, including Alba-
nian, limited annotated corpora and NLP tools intensify 
the challenges for accurate hate speech detection. In this 
work, we concentrate on Albanian-language hate speech, 
gathered from public Facebook comments reflecting real-
world discourse. While Albanian is spoken by millions, 
it remains underrepresented in NLP due to limited anno-
tated corpora and minimal linguistic resources, particularly 
challenging given the dialectal diversity such as Gheg and 
Tosk, as well as informal spelling prevalent on social media. 
Moreover, this study aims to enhance hate speech detection 
by integrating advanced transformer-based architectures 
and explainable AI, compared to classic machine learning 
techniques and extensive feature engineering. We propose 
a fine-tuned XLM-RoBERTa model that outperforms other 
methods in our experiments, establishing it as the best per-
forming solution in this low-resource setting. We restrict our 
experiments to binary classification (hate vs. non-hate) but 
carefully collect a larger and more diverse dataset than pre-
vious Albanian studies, being the biggest dataset in size for 
this type of task. By focusing on Facebook posts, we ensure 
an authentic representation of modern Albanian usage on the 
most used social media. This concentrated scope allows us to 
explore the interplay between state-of-the-art NLP methods, 
dialects as well as informal language, and a thorough error 
analysis through XAI, establishing a comprehensive bench-
mark for hate speech detection in Albanian social media and 
propose the best performing model.
Through systematic experimentation with diverse feature 
representation, preprocessing methods, and state-of-the-art 
models, this research work aims to provide a comprehensive 
analysis for detecting hateful content in a low resource set-
ting, ultimately contributing to safer online discourse for 
Albanian-speaking communities. This study aims to address 
the following research questions:
RQ1 To what extent can multilingual transformer mod-
els improve over traditional baselines, and which of these 
models perform best?
RQ2 How do different feature extraction methods impact 
classification performance in a low-resource setting?
RQ3 Which error patterns persist across multiple model 
architectures, and how do explainability methods reveal 
the underlying causes of these failures in the Albanian 
language?
The main contributions of this research work are:
•	 Create a large-scale human-annotated dataset using 
majority voting for high-quality annotations, which 
serves as the foundation of this research and is derived 
from real-world data.
•	 Develop and evaluate a wide range of ML and DL mod-
els to determine which approaches perform best in the 
Albanian context and propose the most suitable method 
with the highest accuracy.
•	 Compare various feature engineering strategies, provide 
insights specific to the Albanian language, and propose 
the best approach.
•	 Conduct a thorough error analysis through manual inves-
tigation of cases where different classifiers misclassify, 
identify the reasons for these misclassifications, and 
employ explainable AI techniques for further analysis.
The remainder of this paper is organized as follows: Sec-
tion 2 provides an in-depth review of related work, differ-
entiating between high-resource and Albanian-specific hate 

--- Page 3 ---

Social Network Analysis and Mining (2025) 15:82	
Page 3 of 30 
82
speech studies. Section 3 details our data collection from 
Facebook, the annotation protocol, and final dataset char-
acteristics. Section 4 describes the methodology, covering 
preprocessing, feature extraction, model architectures, and 
evaluation metrics. Section 5 presents extensive experi-
ments, including error analysis using manual inspection and 
explainable AI tools. Limitations of the study are shown in 
Sect. 6. We conclude the research work in Sect. 7 by summa-
rizing key findings and proposing future research directions.
2  Related work
Albanian is a distinct branch of the Indo-European language 
family, tracing its written origins to the fifteenth century and 
evolving through multiple dialects, most notably Gheg and 
Tosk (Shala and Beqiraj 2020; Canhasi and Shijaku 2023). 
Despite this rich linguistic heritage and the fact that Alba-
nian is spoken by millions in the Western Balkans and a 
global diaspora, it remains underrepresented in the sphere 
of NLP (Misini et al. 2024, 2022; Canhasi et al. 2022). The 
scarcity of annotated corpora, standardized embeddings, and 
other foundational NLP tools has historically constrained 
both academic and industrial efforts to develop robust sys-
tems for tasks like hate speech detection, sentiment analysis, 
and text classification (Malik et al. 2022; Poletto et al. 2021).
To understand the challenges and potential solutions 
for Albanian, we first show that hate speech detection has 
evolved in resource-rich languages, where extensive data-
sets and advanced NLP tools have shaped state-of-the-art 
methods.
2.1  Hate speech in resource‑rich languages
Davidson et al. (2017) trained Logistic Regression, Naïve 
Bayes, Decision Trees, Random Forests, and SVMs on a 
crowd-annotated dataset of 24,802 tweets, categorized as 
hate speech, offensive language, or neither. Logistic Regres-
sion performed best, achieving an overall F1-score of 0.90. 
However, its hate speech classification was weak, with a 
precision of 0.44 and a recall 0.61, indicating that many 
offensive but non-hateful tweets were misclassified.
Multi-label hate speech detection has gained significant 
attention due to the increasing prevalence of toxic content 
on social media, whereas the recent study in Mazari et al. 
(2024) has explored transformer-based models and deep 
learning architectures to enhance classification performance. 
One such approach utilizes BERT alongside BiLSTM and 
BiGRU models, integrating FastText and GloVe embeddings 
to classify hate speech across multiple categories, including 
identity hate, threat, insult, obscene, toxic, and severe toxic. 
This ensemble learning strategy has demonstrated high effi-
cacy, achieving an ROC-AUC score of 98.63%,
The research work conducted by Founta et al. (2018) 
introduces a widely used dataset nowadays in machine learn-
ing research for hate speech and abusive language detec-
tion. It consists of 80,000 crowd-annotated tweets, refined 
through an iterative labelling process to four categories: 
abusive, hateful, normal, and spam. The study highlights 
annotation inconsistencies, particularly the overlap between 
offensive and abusive language, emphasizing the need for 
context-aware models​
In another work, the research carried out in Zampieri 
et al. (2019) introduced OLID, a widely used dataset of 
14,100 annotated tweets, structured into a three-level hier-
archical taxonomy: (A) offensive vs. non-offensive, (B) cat-
egorization of offensive types, and (C) target identification 
(individual, group, or other). The task attracted 800 + teams, 
with 115 submitting results, making it one of the largest 
SemEval tasks. Participants used machine learning and 
deep learning models, including SVM, CNN, BiLSTM, and 
BERT, with BERT-based models dominating. The best per-
forming model achieved an F1-score of 82.9% for offensive 
language detection.
Putra and Wang (2024) propose a hybrid BERT-CNN 
model for hate speech detection on Twitter, integrating 
BERT’s contextual embeddings with advanced CNN lay-
ers for feature extraction. The model is evaluated on two 
benchmark datasets, Davidson with a 73% F1-score and 
TRAC-1 with a 56% F1-score, outperforming traditional 
FastText, LSTM, and baseline CNN models. Results show 
that BERT + CNN improves precision and recall, particu-
larly in detecting offensive language, demonstrating the 
effectiveness of combining transformers with convolutional 
architectures for hate speech classification​
In the German context, Bretschneider et al. (2017) pro-
pose a pattern-based approach to detect offensive statements 
directed towards foreigners in German social media. Unlike 
traditional bag-of-words models, their method preserves 
word order and identifies referenced victims, making it more 
effective in xenophobic hate speech detection. They develop 
an annotated dataset from Facebook pages known for anti-
foreigner rhetoric and evaluate their method against a Naïve 
Bayes baseline classifier. The pattern-based model achieved 
higher precision, 75.26% and 73.89%, but had moderate 
F1-scores of 67.91% and 62.03%, respectively.
For the Spanish language, García-Díaz et al. (2021) tackle 
misogyny detection in Spanish tweets using Random For-
est, Sequential Minimal Optimization (SMO–SVM vari-
ant), and Linear SVM. Their best-performing model, SMO 
with a combination of linguistic features and average word 
embeddings, achieved 85.17% accuracy, outperforming tra-
ditional bag-of-words models. The study introduces Mis-
oCorpus-2020, a Spanish-language dataset categorized into 
violence against relevant women, regional variations such 
as Spain and Latin America, and general misogynistic traits.

--- Page 4 ---

	
Social Network Analysis and Mining (2025) 15:82
82 
Page 4 of 30
Vanetik and Mimoun (2022) tackle racist language 
detection in French, addressing the scarcity of annotated 
datasets for this task. They introduce FTR (French Twit-
ter Racist Speech dataset), comprising 2,856 manually 
annotated tweets, and evaluate various machine learning 
models, including Random Forest, Logistic Regression, 
and XGBoost, as well as fine-tuned multilingual BERT 
and DeHateBERT (French-specific BERT for hate speech 
detection). The best-performing model was Logistic 
Regression with BERT sentence embeddings, achieving 
an F1-score of 0.7573 and accuracy of 79.72%, outper-
forming fine-tuned transformers.
Ramos et al. (2024) explore hate speech detection 
in Portuguese using transfer learning with transformer 
models. They evaluate BERTimbau, mDeBERTa, and 
generative models like GPT-3.5, Gemini, and Mistral on 
two annotated corpora of YouTube comments and tweets. 
HateBERTimbau, a BERT variant fine-tuned on offensive 
Portuguese tweets, achieved the highest F1-score of 87.1% 
on YouTube, outperforming baseline models by 20%. For 
Twitter, GPT-3.5 performed best with F1 of 50.2%, sur-
passing fine-tuned BERT models.
Recent studies also demonstrate notable advancements 
in low-resource languages, such as Arabic and Urdu. For 
the Arabic language, the research work in Al Anezi (2022) 
introduced a deep learning-based approach for Arabic hate 
speech detection, using a dataset comprising 4,203-com-
ment labelled into seven categories. The Deep Recurrent 
Neural Network (DRNN-2) outperformed Decision Trees, 
Naïve Bayes, and Logistic Regression, achieving 99.73% 
accuracy for binary setup, 95.38% for the three-class setup, 
and 84.14% for the seven-class classification task.
Ashiq et al. (2024) developed a hybrid approach com-
bining multi-lingual BERT with traditional machine learn-
ing classifiers, enhanced through hyperparameter optimi-
zation. Their model, evaluated on Roman Urdu corpora, 
achieved state-of-the-art results with F1 up to 95%, under-
scoring the feasibility of advanced transformer models and 
hybrid methodologies. Similarly, Mehmood et al. (2022) 
proposed a stacked classifier for detecting threatening lan-
guage in Roman Urdu tweets, effectively integrating mul-
tiple classifiers and demonstrating performance such as 
74.01% accuracy. In a related direction, Altaf et al. (2022) 
proposed a deep learning-based approach for cross-domain 
sentiment analysis in Urdu, achieving promising results 
with a GRU model that attained an F1-score of 75%. Com-
plementing these findings, Rehman et al. (2025) surveyed 
hate speech detection methods across multilingual and 
multimodal contexts, highlighting unique challenges like 
code-mixed text, particularly relevant for Roman Urdu, 
and advocating comprehensive, explainable frameworks.
2.2  Hate speech in the Albanian language context
Kastrati et al. (2021) addressed sentiment analysis in low-
resource languages by focusing on Albanian Facebook 
comments during the COVID-19 pandemic. They con-
structed an Albanian sentiment dataset, comprising 10,742 
manually annotated comments labeled by three annotators. 
To tackle the challenges of informal language and class 
imbalance (56% neutral, 28% negative, 15% positive), they 
proposed ALBANA, a deep learning framework combin-
ing BiLSTM with an attention mechanism optimized for 
local context. They compared transformer models such 
as mBERT, fastText and traditional ML approaches such 
as SVM, RF. The findings showed that BiLSTM with an 
attention mechanism outperformed other models, achiev-
ing an F1-score of 72.09%.
Moreover, Ajvazi et al. (2022) introduced an Albanian 
dataset for offensive language detection, focusing on Koso-
vo’s social media landscape. Their corpus comprises 3000 
manually annotated Facebook and YouTube comments 
from news platforms, labeled using the OLID hierarchical 
scheme. The dataset addresses dialectal nuances of Kos-
ovo Albanian (Gheg dialect) and includes 17.3% offensive 
instances, with strong inter-annotator agreement. For base-
line classification, a fine-tuned multilingual BERT model 
achieved an F1-score of 0.86 in distinguishing offensive 
content and 0.82 in identifying targeted insults. Notably, 
their transfer learning experiments revealed that combin-
ing Albanian and Danish data improved Danish prediction 
performance (+ 12% F1) but not Albanian.
Nurçe et al. (2022) introduced Shaj, a publicly available 
Albanian dataset on abusive language detection, compris-
ing 11,874 Instagram and YouTube comments. The data-
set follows the OffensEval hierarchical annotation scheme, 
categorizing content into offensive/non-offensive, targeted/
untargeted, and target type (individual, group, other). To 
benchmark Shaj, they evaluated Naïve Bayes, BiLSTM, 
and a fine-tuned BERT model, with BERT achieving the 
highest F1-score of 0.77 for offensive language detection.
Zenuni et al. (2017) presented one of the first attempts 
to build a hate speech detection system for the Alba-
nian language, leveraging SVMs for classification. The 
authors constructed a hate speech corpus by collecting 
and annotating Facebook comments, labeling 2764 com-
ments as hateful from a total of 4886. The authors report 
an F1-score of 0.58, indicating moderate performance but 
highlighting the need for a richer dataset and additional 
linguistic processing features. The authors acknowledge 
linguistic challenges, such as ambiguity, lack of struc-
tured NLP tools for Albanian, and the need for contextual 
analysis in hate speech detection. They emphasize the 
importance of dataset expansion and propose extending 

--- Page 5 ---

Social Network Analysis and Mining (2025) 15:82	
Page 5 of 30 
82
their work by incorporating additional supervised learning 
models and a more diverse training corpus.
The research study presented in Fetahi et al. (2024) aims 
to enhance hate speech detection in Albanian by integrat-
ing handcrafted features with ML models. The dataset used 
comprises 15,947 Facebook comments manually annotated. 
The study employs SVM, Naïve Bayes, Random Forest, and 
Logistic Regression with a considerable number of hand-
crafted features, covering textual, lexical, and structural 
properties. RF performed best, achieving an F1 score of 
76.51% with all features, while LR excelled with Recur-
sive Feature Elimination with an F1 of 76.77%, revealing no 
dominant feature, underscoring Albanian’s linguistic com-
plexity. Similarly, the study in Fetahi et al. (2024) introduces 
a human-annotated hate speech dataset for Albanian, com-
prising 11,000+ social media comments categorized using 
a two-layer taxonomy (binary classification and subcatego-
ries: general, religious, political, and ethnicity-based hate 
speech). Different algorithms were utilized, such as SVM, 
Naïve Bayes, XGBoost, and Random Forest with TF-IDF 
and CountVectorizer for feature representation. NB with TF-
IDF achieved the highest F1-score of 0.80 for binary clas-
sification, while XGBoost led in multiclass classification a 
score of F1 with 0.77. To showcase real-world applicability, 
a mobile web application was developed for real-time hate 
speech detection.
Moreover, while many of the studies summarized in this 
section focus on resource-rich languages such as English 
with mature NLP tool support, hate speech research in 
Albanian as a low-resource language remains compara-
tively scarce. Table 1 provides a summary of the key mod-
els from the discussed work, along with their best reported 
performances, languages, and dataset details. Existing works 
generally rely on smaller corpora and lack evaluations of 
advanced techniques such as deep neural networks or trans-
former-based models. In contrast, our research substantially 
expands the Albanian hate speech dataset and systemati-
cally applies a broader range of models, feature engineering 
approaches, and comparative analyses, including multilin-
gual transformers and interpretability frameworks, thereby 
addressing both the data scarcity and methodological gaps 
evident in previous work.
3  Dataset collection and annotation
An essential component of automatic hate speech detection 
is gathering high-quality data to build robust machine learn-
ing models with high accuracy. In this section, we outline 
the procedures followed to create a representative dataset 
for the low-resourced language, Albanian. The flowchart of 
compiling the dataset is shown in Fig. 1.
3.1  Data collection
To ensure reliable and representative data, Facebook social 
media was selected as the primary source for data crawling. 
According to the Digital 2021 report (https://​datar​eport​al.​
com/​repor​ts/​digit​al-​2021-​kosovo), nearly 85% of all social 
media users in Albanian-speaking countries are Facebook 
users. Additionally, another report in Hallakate (2020) 
highlights that Facebook is used by people across nearly 
all age groups in Kosovo. While recent studies often utilize 
X (formerly known as Twitter) for similar tasks, we chose 
Facebook to better reflect real-world usage and ensure the 
datasets applicability to real world scenarios for the Alba-
nian use case.
To collect comments, we focused on diverse post types, 
including those from news outlets, public profiles, and com-
munity groups, aiming to capture a wide range of linguistic 
styles and discourse.
The data was scraped using the ExportComments1 tool. 
Only publicly available comments were extracted, adhering 
to ethical guidelines and privacy regulations. To ensure ano-
nymity, an automated anonymization process was applied to 
remove personal identifiers and sensitive information, safe-
guarding user privacy throughout the dataset.
Given the prevalence of imbalanced datasets in recent 
studies, particularly with fewer hate speech instances, we 
employed a strategic approach to ensure sufficient represen-
tation of hate comments. Specifically, we targeted provoca-
tive and controversial posts that were more likely to elicit 
hate speech or polarizing comments from users (Gentian 
Sala 2019). This approach not only addressed the class 
imbalance issue but also enhanced the dataset’s relevance 
to hate speech detection tasks.
The dataset created for this study is an extension of data-
sets presented in research works (Fetahi et al. 2024; Fetahi 
et al. 2024). A snapshot of the dataset is provided in Fig. 2, 
offering an overview of its structure and content.
3.2  Annotation process and quality assurance
The dataset was annotated through a rigorous, multi-stage 
process to ensure reliability. Three annotators, all native 
Albanian speakers with expertise in NLP and computer sci-
ence, independently labelled the comments. To minimize 
subjectivity, comprehensive annotation guidelines were 
developed, defining hate speech and providing illustrative 
examples. Annotators underwent a training phase using 
diverse sample comments, which can be seen Table 2, to 
calibrate their understanding of the guidelines.
1  www.​expor​tcomm​ents.​com.

--- Page 6 ---

	
Social Network Analysis and Mining (2025) 15:82
82 
Page 6 of 30
Table 1   Overview of discussed work
References
Language
Dataset
Dataset size
Methods and models used
Best results
Comment
Davidson et al. (2017)
English
Hatebase lexicon + Twitter
24,802 tweets
LR, NB, DT, RF, SVM
F1 = 0.90
While the full model per-
forms well overall, it strug-
gles with low precision and 
recall for hate speech
Mazari et al. (2024)
English
Jigsaw Toxic Comment 
Classification Challenge 
dataset
159,571 training comments; 
63,978 test comments
BERT, Bi-LSTM, Bi-GRU, 
GloVe, FastText, ensem-
ble learning
ROC-AUC = 98.63%
The study combines BERT 
with Bi-LSTM/Bi-GRU 
models using GloVe and 
FastText embeddings in 
ensemble architectures
Founta et al. (2018)
English
Twitter Abusive Behavior 
Corpus
80,000 tweets
Annotation method: 
Crowdsourcing
No modeling of ML
Large-scale annotated data-
set with four final labels 
(Abusive, Hateful, Spam, 
Normal) built through an 
iterative, crowdsourced 
process
Zampieri et al. (2019)
English
OLID
14,100 tweets
BERT, CNN, BiLSTM, 
RNN, GRU, SVM, Logis-
tic Regression, ELMo, 
OpenAI GPT, Transform-
ers, ensembles, custom 
embeddings, rule-based 
filters
F1 = 82.9%
The study introduced OLID, 
a new hierarchical dataset 
for offensive language 
detection in English tweets. 
BERT-based models 
performed best, with 82.9% 
F1-macro. Dataset and task 
setup were widely adopted
Putra and Wang (2024)
English
Davidson, TRAC-1
Davidson: 24,683 tweets
TRAC-1: 18,000 tweets
BERT, GPT-2, Fast-
Text, CNN, LSTM, 
BERT + Advanced CNN, 
GPT-2 + Advanced CNN, 
FastText + Advanced 
CNN
F1-score = 73% (Davidson)
F1-score = 56% (TRAC-1)
Diverse model comparisons
Bretschneider and Peters 
(2017)
German
Facebook based dataset
5,836 comments total
Pattern-based sequence 
model
F1 = 67.91%
Dataset and lexicons are 
specific to German
García-Díaz et al. (2021)
Spanish
MisoCorpus-2020
7,682 tweets
RF, SMO (SVM), LSVM; 
using BoW, FastText, 
Linguistic Features and 
AWE + LF combined
Accuracy = 85.17%
SMO performed best out-
performing other methods. 
Paper also combined 
semantic and linguistic 
features
Vanetik and Mimoun 
(2022)
French
French Twitter Racist
2,856 tweets
TF-IDF, n-grams 
(n = 1,2,3), BERT 
sentence embeddings, 
fine-tuned BERT, RF, 
LR, XGBoost
Accuracy = 79.7%
Introduced a new French 
racist speech dataset 
(FTR). Best performance 
with BERT sentence 
embeddings and Logistic 
Regression

--- Page 7 ---

Social Network Analysis and Mining (2025) 15:82	
Page 7 of 30 
82
Table 1   (continued)
References
Language
Dataset
Dataset size
Methods and models used
Best results
Comment
Ramos et al. (2024)
Portugese
YouTube and Twitter 
corpora
YouTube: 23,912 com-
ments
Twitter: 21,546 tweets
BERTimbau, BERTimbau-
hatebr, mDeBERTa-
hatebr, HateBERTimbau, 
GPT-3.5, GPT-4, Gemini-
Pro, Mistral-7B-Instruct-
v0.3, CNN, LSTM
YouTube: F1 = 87.1%
Twitter: F1 = 50.2%
Strong methodology using 
both discriminative and 
generative models, with 
extensive experiments 
including domain-specific 
fine-tuning
Al Anezi (2022)
Arabic
Arabic Comments
4,203 Comments
DRNN, DT, NB, LR, 
Word2vec, Glove
Accuracy = 99.73%;
Strongest performance 
achieved using a deep 
bidirectional RNN
Ashiq et al. (2024)
Roman Urdu
HS-RU-20 corpus and 
RUHSOLD corpus
HS-RU-20: 5000 instances; 
RUHSOLD: 10,012 
instances
CNN, LSTM, BiLSTM, 
GRU, MBERT, SVM, RF, 
LR, NB, HPO via Grid 
Search, Random Search, 
BOGP
F1 = 0.94
Strong experimental design 
with combination of DL 
and ML classifiers
Mehmood et al. (2022)
Urdu
Urdu threating tweet dataset 3,564 tweets
Extra Trees, BNB, SVM, 
LR, Stacking ML, CNN, 
FCN, LSTM, GRU​
F1 = 73.99%
Stacked model using ET & 
BNB and LR outperformed 
both ML and DL baselines
Altaf et al. (2022)
Urdi
Twitter Dataset
9,221 tweets
BNB, MNB, LR, RF, SVM, 
RNN, LSTM, GRU​
F1 = 0.75
Cross Domain Sentiment 
Classification experi-
ments in a low resourced 
language
Raza Ur Rehman et al. 
(2025)
Multilingual, 
Code-
mixed
Multiple datasets from 
social networks
N/A
N/A
N/A
A comprehensive survey
Kastrati et al. (2021)
Albanian
Facebook Comments
10,742 comments
BiLSTM, 1D-CNN, Hybrid 
(1D-CNN + BiLSTM), 
DNN, SVM, NB, RF, DT, 
fastText, mBERT; atten-
tion mechanism
F1-score = 72.09%
Sentiment analysis paper. 
Dlear dataset description 
and multi-model evalua-
tion. Best result achieved 
using BiLSTM with 
attention
Ajvazi and Hardmeier 
(2022)
Albanian
Offensive Language in 
Kosovo Social Media
3,000 comments
Fine-tuned mBERT
F1 = 0.86
Dataset is smaller but 
carefully constructed. 
Performance drops in 
cross-lingual transfer
Nurce et al. (2022)
Albanian
Shaj
11,874 comments
NB, BiLSTM, mBERT
F1 = 0.77
Best result with multilingual 
BERT
Ajdari et al. (2017)
Albanian
Facebook social pages
4,886 comments
SVM
F-score = 0.58
Only SVM tested, perfor-
mance moderate. No com-
parison with other models
Fetahi et al. (2024)
Albanian
Facebook Comments
15,947 comments
SVM, NB, RF, LR
F1 Score = 76.77%
Study provides extensive 
handcrafted features (834 
total)

--- Page 8 ---

	
Social Network Analysis and Mining (2025) 15:82
82 
Page 8 of 30
After the initial labeling, inter-annotator agreement was 
evaluated using Fleiss’ Kappa (Moons and Vandervieren 
2023; Gwet 2021), resulting in a score of 0.71, which indi-
cates substantial agreement, as referred in Table 3. Discrep-
ancies in labels were resolved through majority voting, with 
contentious cases reviewed collaboratively to refine defini-
tions and ensure consistency.
Most disagreements arose from challenges in interpret-
ing irony and differing thresholds for recognizing offensive 
or hateful content. These differences were often context-
dependent and reflected the subjective nature of human judg-
ment. Given these limitations, implementing crowdsourcing 
could provide a more scalable and diverse approach to anno-
tation in future work.
3.3  Dataset statistics
The final dataset, consisting of 20,860 comments, is sum-
marized in Table 4. As can be seen from the table, Class 0 
(Not-hate speech) dominates by volume (56.29%), Class 1 
(hate speech) exhibits markedly longer comments, with an 
average of 19.78 words and 100.88 characters per instance, 
nearly double the length of Not-Hate speech remarks. Nota-
bly, the balanced class distribution (43.71% hate speech) 
reflects our targeted data collection strategy. By prioritiz-
ing controversial posts, we mitigated the class imbalance 
common to hate speech datasets, where offensive content 
typically constitutes < 15% of samples.
As can be seen from the graph in Fig. 3 showing the num-
ber of words for each comment, there is a clear trend that 
longer comments are more likely to contain hate speech. 
Comments that exceed 20 tokens are nearly twice as likely to 
be categorized as harmful, with the greatest increase occur-
ring in the 30–50 token range. This is in line with broader 
trends in our dataset, which show that negative comments 
typically contain a lot more words than neutral ones, as 
shown in Table 4. The lengthy texts imply that hatred often 
infiltrates multi-layered contexts and develops gradually as 
opposed to suddenly. Although there are sometimes brief, 
explicit attacks, they mostly lean towards the neutral class, 
however, not in all cases.
Moreover, in Figs. 4 and 5, we show the word clouds gen-
erated for the dataset for both classes, however, for illustrat-
ing purposes, stop words were excluded in these plots. The 
word clouds highlight clear differences between Not-hate 
speech and hate speech comments. Neutral comments mostly 
use everyday words about general topics and discussions. 
Hate speech, however, focuses heavily on religious groups, 
ethnic identities, and harsh or insulting terms. This is in line 
with previous research (Ajvazi and Hardmeier 2022) that 
Table 1   (continued)
References
Language
Dataset
Dataset size
Methods and models used
Best results
Comment
Fetahi et al. (2024)
Albanian
Facebook Comments
11,343 comments
NB, SVM, RF, XGBoost, 
TF-IDF, CountVectorizer, 
LIME for error analysis
F1 = 0.80
Strong binary classification 
performance. Weaknesses 
include limited multiclass 
performance

--- Page 9 ---

Social Network Analysis and Mining (2025) 15:82	
Page 9 of 30 
82
Fig. 1   Dataset construction 
workflow
Fig. 2   Dataset sample
Table 2   Sample comments for 
training the annotators
Comment
Label
Ki vetem hoxh nuk esht sdi pse e ftoni ket shejtan
(He is not an Imam I don't know why you invite this devil)
Hate speech
Kjo ashg lop e mbuluar
(This is just a covered cow)
Hate speech
A pragu i flliqt kunder shpiune turp i zi
(The filthy threshold against spies, a black shame)
Hate speech
Shum e vertet !
(Very true!)
Not-Hate speech
Respekt per ket Imam t’nderum
(Respect for this respectful Imam)
Not-Hate speech
Urime e Suksese!
(Congratulations and Success)
Not-Hate speech
E drejt e secilit me marre fen qe i pelqen qe ndihet ma mire!
(It is everyone's right to choose the religion they like and feel best with!)
Not-Hate speech
Table 3   Fleiss Kappa reference table
Score
Agreement
< 0
Poor agreement
0.01–0.20
Slight agreement
0.21–0.40
Fair agreement
0.41–0.60
Moderate agreement
0.61–0.80
Substantial agreement
0.81–1.00
Almost perfect agreement
Table 4   Dataset statistics
Metric
Class 0 (not-hate 
speech)
Class 
1 (hate 
speech)
Total comments
11,742
9,118
Total word count
147,245
180,320
Average words per comment
12.54
19.78
Average characters per comment
65.82
100.88
Ratio of comments (class/total)
0.5629
0.4371

--- Page 10 ---

	
Social Network Analysis and Mining (2025) 15:82
82 
Page 10 of 30
found that harmful comments often target specific communi-
ties and rely on cultural references to spread hate. These pat-
terns show why detecting hate speech requires understanding 
deeper context, not just individual words.
4  Methodology
In this section, we outline the methodology employed and 
provide a detailed description of the classification models 
used in the research work. This includes the steps for data 
preprocessing, feature extraction, model training, and evalu-
ation, as well as the interpretability methods applied to gain 
insights into the results. The overall workflow of the meth-
odology is illustrated in Fig. 6.
4.1  Preprocessing and dataset preparation
4.1.1  Text normalization and cleaning
The initial phase of preprocessing involved anonymizing and 
cleaning the dataset, specifically replacing user mentions and 
URLs with standardized tags. To address user mentions, by 
observing the scraped comments we hypothesized that most 
mentions appeared at the beginning of comments in the social 
media Facebook, particularly in replies. Each user was cross-
checked against the comment text, and matches were replaced 
with the ":USER:" tag. A manual review ensured minimal 
errors, although challenges arose due to the prevalence of 
Fig. 3   Token distribution in 
comments per class and bins
Fig. 4   Word cloud for Not-Hate speech class
Fig. 5   Word cloud for Hate speech class

--- Page 11 ---

Social Network Analysis and Mining (2025) 15:82	
Page 11 of 30 
82
common Albanian names that overlapped with stopwords or 
other meaningful words. Stopwords were excluded from the 
removal process to preserve valuable information.
URLs, often found in comments containing links, images, 
or bot-generated text, were replaced with the ":URL:" token. 
This standardization helped reduce noise and improve the 
quality of the dataset for downstream tasks.
4.1.2  Preprocessing steps
To prepare the textual data, we implemented comprehensive 
preprocessing steps. These steps included:
1.	 Lowercasing: Converting all text to lowercase.
2.	 Punctuation and Digit Removal: Eliminating all punc-
tuation marks and numeric characters.
3.	 Transliteration and Space Removal: Replacing special 
Albanian characters with standard equivalents (“ë” and 
“ç”) and removing extra spaces.
4.	 Emoji Removal: Deleting emojis from the comments.
5.	 Repetitive Character Reduction: Limiting repeated char-
acters to a maximum of two.
6.	 Tokenization and Stop word Removal: Splitting text into 
words and removing manually curated stop words.
7.	 Stemming: Given the limited NLP tools for Albanian, 
we developed a custom stemming algorithm tailored to 
Fig. 6   Workflow of the performed experiments

--- Page 12 ---

	
Social Network Analysis and Mining (2025) 15:82
82 
Page 12 of 30
the language's complex morphology. This algorithm pri-
marily focused on suffix stripping, guided by a manually 
curated list of common Albanian suffixes. The stemming 
pipeline included transliteration of special characters, 
tokenization, and the exclusion of stop words and short 
words
8.	 Handling Empty Comments: Replacing comments ren-
dered empty after preprocessing with the placeholder 
"MISS" to maintain dataset consistency.
These preprocessing steps were performed using Python, 
and the processed dataset was saved for further analysis. 
All experiments were conducted on both the original and 
preprocessed datasets to evaluate the impact of preprocess-
ing on model performance, particularly for the Albanian 
language.
4.2  Feature extraction and representation
In order to effectively represent textual data for hate speech 
detection, this work utilizes a variety of representation meth-
ods, including Count Vectorization, TF-IDF representations, 
as well as handcrafted features and word embeddings as fea-
tures for the models.
4.2.1  Count vectorization
Count Vectorization is a foundational technique in text anal-
ysis that transforms text into numerical data by counting 
how often words appear. In this method, each document, 
specifically the social media comments, are converted into 
a matrix where rows represent comments and columns rep-
resent unique words. The values in the matrix simply count 
how many times each word occurs in a comment.
For our study, comments were split into individual words 
known as tokens, and a vocabulary was built from all unique 
terms in the dataset.
4.2.2  TF‑IDF
TF-IDF is a feature extraction method that goes beyond sim-
ple word counts by weighting terms based on their unique-
ness and relevance. Unlike basic frequency calculation, 
TF-IDF emphasizes words that are frequent in specific com-
ments but rare across the entire dataset, helping spotlight 
terms that signal distinct patterns, like hate speech.
In this research, we employed two approaches of TF-IDF 
implementation:
•	 Character-Level TF-IDF: This approach breaks text into 
character combinations capturing nuances like slang, 
typos, or word fragments common in informal platforms. 
We used character level TF-IDF features ranging from 
one to five.
•	 Word level TF-IDF: Here, sequences of words are ana-
lyzed to identify phrases that collectively signal hostility. 
We employed word level n-grams from one to three.
4.2.3  Handcrafted feature extraction
In this study, we also employed a strategy of implementing 
handcrafted features to complement the automated tech-
niques by incorporating domain-specific knowledge and 
contextual understanding of Albanian hate speech. This 
approach allows us to explore linguistic, behavioural and 
contextual patterns, as well as aiming increasing detection 
accuracy. The goal was to extract features that will help us 
indicate hate and offensive language comments, as well as 
user behaviour and commenting styles. The extracted fea-
tures list is shown in Table 5.
To optimize the performance of machine learning models, 
careful feature selection was performed. This step aimed to 
eliminate redundant or irrelevant features while retaining 
those that contributed most significantly to the detection of 
hate speech. Three primary methods were used:
1.	 Using the Full Feature Set: Initially, all handcrafted fea-
tures were included to assess their combined impact. 
This approach provided a baseline for understanding the 
overall contribution of handcrafted features to model 
performance.
2.	 Recursive Feature Elimination (RFE): RFE was applied 
to iteratively remove the least important features based 
on their contribution to model accuracy. Using a pre-
trained classifier, in our case the RF model, the impor-
tance of each feature was ranked, and the least signifi-
cant features were eliminated in successive iterations. 
Due to computational constraints, we used a step size 
for each iteration of 50 for the RFE process.
3.	 Thresholding-Based Elimination: In this approach, fea-
tures with importance scores below a certain threshold 
were excluded. We implemented a constant threshold of 
0.001, to eliminate the features with no impact at all.
By employing these feature selection methods, the final 
set of handcrafted features was refined to maximize inter-
pretability and predictive power.
4.2.4  Word embeddings
For the Albanian language text representation, we use 
FastText word embeddings, developed by the Facebook 
AI Research Lab. Unlike traditional word embeddings, 
FastText considers subword information, which is useful 

--- Page 13 ---

Social Network Analysis and Mining (2025) 15:82	
Page 13 of 30 
82
for languages like Albanian. We use the 300-dimensional 
version of the word embeddings.
4.3  Models and architectures
To run experiments and identify the best performing mod-
els for hate speech detection in Albanian social media, we 
employed a wide range of models, including traditional 
machine learning algorithms, advanced deep learning 
architectures, and transformer-based models. The models 
were trained and evaluated across several setups, as out-
lined above, with the results presented accordingly.
The models used in our experiments are as follows:
SVM (Support Vector Machine): Finds the optimal 
boundary to separate classes by maximizing the mar-
gin between them.
NB (Naïve Bayes): Uses probability, the Bayes’ theo-
rem to classify text, assuming features are independent.
LR (Logistic Regression): Predicts class probabilities 
using a logistic function.
RF (Random Forest): Combines multiple decision trees 
to reduce overfitting. Handles noisy text data by averag-
ing tree predictions.
XGBoost: An optimized gradient-boosting framework 
that builds decision trees sequentially, correcting errors 
from prior trees.
Table 5   Feature list
Category
Feature description
Textual metrics
Total word count, Total character count, Average word length, Total sentence count, Average words 
per sentence, Comment byte length, Character count excluding punctuation, Readability score, Word 
length standard deviation, Word length variance, Sentence length standard deviation, Sentence length 
variance, Lexical density (excluding stopwords), Word length diversity
Punctuation and symbols
Total punctuation count, Exclamation mark count, Question mark count, Repeated punctuation count, 
Maximum repeated punctuation sequence length, Ellipsis count, Parentheses count, Quotation mark 
count, Bracket count, Unusual punctuation sequence count, Special character count, Special character 
'ç' count, Special character 'ë' count
Case and capitalization
Fully uppercase word count, Fully lowercase word count, Title-cased word frequency, Capital letter 
density, Offensive terms in uppercase
Lexical diversity
Unique word count, Unique-to-total word ratio, Lexical diversity score, Hapax legomena count, Dis 
legomena count, Complex word count, Simple word count, Short word count, Medium-length word 
count, Long word count, Stopword count
Repetition patterns
Repeated character count, Repeated word count, Repeated punctuation count, Repeated consonant count, 
Repeated vowel count, Tripled vowel count
N-gram features
Average unigram length, Average bigram length, Average trigram length, Top 50 unigram frequencies, 
Top 50 bigram frequencies, Top 50 trigram frequencies, Top 50 character bigram frequencies, Top 50 
character trigram frequencies, Top 50 character 4-gram frequencies
Phonetic Properties
Average syllables per word, Consonant count, Vowel count, Consonant-to-vowel ratio, Vowel-to-alpha-
bet ratio
Morphological traits
Suffix usage frequency
Structural attributes
Line count, Paragraph count, Average characters per line, Average characters per paragraph, List format 
count
Sentence dynamics
Short sentence count, Long sentence count, Long-to-short sentence ratio, Imperative sentence count, 
Interrogative sentence count, Declarative sentence count, Exclamatory sentence count
Sentiment indicators
Positive word count, Negative word count
User behavior
Reply count (non-reply comments), Average likes per reply, Maximum likes per reply, Minimum likes 
per reply, Profile comment count, Average comment length by profile, Maximum comment length by 
profile, Minimum comment length by profile, User activity frequency
Emoji and hashtag features
Emoji count, Specific emoji frequency, Emoji presence flag, Emoji diversity score, Hashtag diversity 
score
URL features
URL count, URL presence flag
Controversial content
Controversial word count at comment start, Controversial word count at comment end
Language and code-switching features Code-switching detection flag
Semantic similarity features
Cosine similarity of the comment with a set of top 100 offensive texts, Cosine similarity of the comment 
with a set of top 100 positive texts, Cosine similarity of the comment with a set of 300 offensive texts, 
Cosine similarity of the comment with a set of 300 positive texts

--- Page 14 ---

	
Social Network Analysis and Mining (2025) 15:82
82 
Page 14 of 30
CNN (Convolutional Neural Network): Detects local pat-
terns such as n-grams in text using filters.
LSTM (Long Short-Term Memory): Processes sequences 
such as sentences, to remember long-term dependencies.
BiLSTM (Bidirectional LSTM): Reads text both forward 
and backward, capturing context from past and future 
words simultaneously.
GRU (Gated Recurrent Unit): Simpler than LSTM, uses 
gating to control information flow.
mBERT (Multilingual BERT): Pre-trained on 104 lan-
guages, understands cross-lingual context. Fine-tuned for 
language-specific hate speech.
distil-mBERT: A smaller, faster version of mBERT. 
Retains most performance with fewer parameters.
XLM-Roberta: Trained on 100+ languages, excels at 
cross-lingual tasks. Robust for low-resource languages 
like Albanian.
BERTweet: Pre-trained on social media tweets. Special-
ized for social media text, capturing slang, hashtags, and 
informal language.
For the machine-learning models, we applied the library’s 
default hyperparameters which are:
•	 Support Vector Machine (SVC)—penalty C = 1.0, ker-
nel = 'rbf', γ = 'scale'.
•	 Random Forest (RandomForestClassifier)—100 trees, 
Gini impurity split criterion, unlimited depth ( max_
depth = None).
•	 Multinomial Naïve Bayes (MultinomialNB)—additive‐
smoothing factor α = 1.0
•	 Logistic Regression (LogisticRegression)—L2 penalty, 
solver = 'lbfgs', regularisation strength C = 1.0, maximum 
100 iterations.
•	 XGBoost (XGBClassifier)—100 estimators, 
learning-rate = 0.1, maximum depth = 3, objec-
tive = 'binary:logistic'.
For the deep learning and transformers models, the spe-
cific configurations are shown in Table 6.
The afore-mentioned machine learning models were cho-
sen based on their proven effectiveness in prior hate speech 
detection literature and their interpretation opportunities. 
Deep learning models were included to assess their abil-
ity to automatically learn complex linguistic patterns from 
Table 6   Parameters used for the deep learning models
Model
Tokenizer
Base model
Max sequence length
Batch size
Learning rate
Classifier architecture
XLM-RoBERTa
XLMRobertaTo-
kenizer
xlm-roberta-base
256
16
1E−05
Linear(768 → 256) → ReLU → Drop-
out(0.5) → Linear(256 → 2)
DistilBERT
DistilBertTokenizer
distilbert-base-multi-
lingual-cased
256
16
1E−05
Linear(768 → 256) → ReLU → Drop-
out(0.5) → Linear(256 → 2)
mBERT
BertTokenizer
bert-base-multilin-
gual-cased
256
16
1E−05
Linear(768 → 256) → ReLU → Drop-
out(0.5) → Linear(256 → 2)
BERTweet
AutoTokenizer (BER-
Tweet)
vinai/bertweet-base
128 (max)
16
1E−05
Linear(768 → 256) → ReLU → Drop-
out(0.5) → Linear(256 → 2)
LSTM
Keras Tokenizer
Custom Sequential 
Model
250
64
Adam (default 0.001)
Embed-
ding → LSTM(128) → GlobalMax-
Pooling1D → Dense(128) → Drop-
out(0.5) → Dense(1, Sigmoid)
BiLSTM
Keras Tokenizer
Custom Sequential 
Model
250
64
Adam (default 0.001)
Embedding → BiL-
STM(128) → GlobalMax-
Pooling1D → Dense(128) → Drop-
out(0.5) → Dense(1, Sigmoid)
GRU​
Keras Tokenizer
Custom Sequential 
Model
250
64
Adam (default 0.001)
Embed-
ding → GRU(128) → GlobalMax-
Pooling1D → Dense(128) → Drop-
out(0.5) → Dense(1, Sigmoid)
CNN
Keras Tokenizer
Custom Sequential 
Model
250
64
Adam (default 0.001)
Embedding → Conv1D(128, 
5) → GlobalMax-
Pooling1D → Dense(128) → Dense(1, 
Sigmoid)
Table 7   High-end computer hardware performance
Description
Detail
System model
Supermicro SYS-7049GP-TRT​
Processor
Intel Xeon Silver 4210 CPU @ 2.20 GHz (20 
CPUs)
Memory
192 GB RAM
Graphics cards
GPU 1: NVIDIA GeForce RTX 2080 Ti (11 GB 
Dedicated, 95 GB Shared)
GPU 2: Integrated ASPEED Graphics
Operating system
Windows 10
Language
English

--- Page 15 ---

Social Network Analysis and Mining (2025) 15:82	
Page 15 of 30 
82
Albanian social media text, which is often informal and dia-
lectally varied.
For transformer-based models, we used multilingual vari-
ants, as no Albanian-specific pre-trained transformers cur-
rently exist. These models are specifically designed to han-
dle low-resource languages and have demonstrated strong 
cross-lingual generalization in hate speech classification 
tasks.
4.4  Experimental setup and evaluation
All experiments were conducted in Python using machine 
learning libraries such as PyTorch, TensorFlow, Keras, and 
Scikit-learn. Traditional machine learning models were 
trained on high-performance CPU hardware, while deep 
learning architectures and transformer fine-tuning leveraged 
CUDA-enabled GPUs to accelerate training and evaluation. 
The hardware performances are shown in Table 7.
To ensure fair model comparison, we adopted a consist-
ent 75:25 train-test split ratio across all experiments, with 
a fixed random seed to guarantee reproducible data parti-
tioning. This approach minimized variability and ensured 
equitable evaluation conditions for both classical and neural 
network-based methods.
To rigorously assess model performance, we employed 
four key classification metrics, including precision, recall, 
F1-score, and accuracy, which are defined as follows:
1.	 Precision measures how many predicted hate speech 
cases are truly hateful.
2.	 Recall measures how many actual hate speech cases are 
correctly identified.
3.	 F1-score balances precision and recall using their har-
monic mean.
4.	 Accuracy measures overall correctness across both 
classes.
In specific cases with the best performing models, we 
also analyze the confusion matrix and classification report 
heatmap for further insights.
Precision =
TP
TP + FP
Recall =
TP
TP + FN
F1 = 2 ⋅Precision ⋅Recall
Precision + Recall
Accuracy =
TP + TN
TP + TN + FP + FN
4.5  Interpretability
Beyond achieving good classification performance, it's critical 
to comprehend the reasoning underlying model predictions, 
identify patterns in the data, and uncover any biases or mis-
takes the models might have produced. This section outlines 
the interpretability methods employed in this study, including 
SHAP and LIME.
SHAP (SHapley Additive exPlanations) We use SHAP 
(Holzinger et al. 2022; Lundberg and Lee 2017) to quantify 
the contribution of individual features to model predictions. By 
figuring out Shapley values which show how little each feature 
contributes to the prediction. This method gives us a unified 
way to understand what machine learning models do. In this 
study, we primarily applied SHAP analysis to handcrafted 
features. By visualizing feature importance, SHAP helped 
identify which features were most influential in detecting hate 
speech. We generate SHAP summary plots to visualize the 
global importance of features. These visualizations help in 
interpretability and a better understanding of the decision-
making process of the models.
LIME (Local Interpretable Model-Agnostic Explanations) 
LIME (Holzinger et al. 2022; Dieber and Kirrane 2020) is 
utilized as a complementary interpretability tool to explain 
individual predictions in a local context. Unlike SHAP, which 
provides global insights, LIME focuses on explaining a single 
prediction by perturbing the input data and observing changes 
in the output. In this study, LIME will be used for analyz-
ing edge cases where models struggled to make accurate 
predictions.
4.6  Analysis
Error analysis We perform an error analysis on misclassified 
comments to further investigate the model's performance. We 
conducted the analysis by manually investigating comments 
where the models either failed or succeeded. Several com-
ments are analyzed from multiple models to pinpoint patterns 
of success and failure. These insights will help identify the 
strengths and weaknesses of each model and guide improve-
ments in feature engineering, data representation, or even a 
general overview of the language itself.
Feature Ranking of Tree based models Manual investigation 
of feature rankings produced by tree-based models, such as 
Random Forest was conducted to analyse the individual impact 
of features on hate speech detection. These models inherently 
provide feature importance scores based on their contribution 
to reducing impurity during splits.

--- Page 16 ---

	
Social Network Analysis and Mining (2025) 15:82
82 
Page 16 of 30
5  Results and discussion
This section presents the results obtained from a set of 
experiments using classical ML techniques and advanced 
deep learning along with their analysis.
5.1  Machine learning models performance analysis
In the initial set of experiments, as shown in Table 8, we 
evaluated five classical machine learning algorithms, Naïve 
Bayes, SVM, Random Forest, Logistic Regression, and 
XGBoost using Count Vectorization features on both raw 
and pre-processed text. Across all models, pre-processed 
data yielded modest but consistent improvements in Preci-
sion, Recall, F1‑Score, and Accuracy. This finding suggests 
that preprocessing helps algorithms better capture key sig-
nals indicative of hate speech.
Among the evaluated models, Logistic Regression 
achieved the highest overall performance on the pre-pro-
cessed dataset, reaching an accuracy of 82.63%. Naïve Bayes 
also improved noticeably, rising from 80.54% to 81.73% in 
terms of F1‑score after text preprocessing.
Building upon the Count Vectorization results, we next 
experimented with TF-IDF to weight terms based on their 
importance in the corpus. Table 9 reports the performance 
of the same five classifiers using TF-IDF features at uni-
gram, bigram, and trigram levels, again comparing raw vs. 
pre-processed data. The unigram TF-IDF setting gener-
ally outperformed the higher-order n-gram configurations. 
Naïve Bayes achieved an accuracy of 81.80% on raw text and 
82.84% on pre-processed text when trained on unigrams. In 
contrast, moving to bigrams and trigrams introduced some 
performance drops, largely attributable to increased data 
sparsity: multi-word sequences in Albanian can be quite 
variable, limiting their frequency and thus diluting the 
strength of the TF-IDF signal. In line with earlier findings, 
preprocessing again provided advantages for most models. 
Even so, the best-performing classifiers still achieved their 
highest scores with unigram TF-IDF rather than bigrams or 
trigrams, suggesting that, in a low-resource scenario, simple 
yet well-cleaned features can outshine more complex repre-
sentations. This result underscores how data availability and 
linguistic characteristics can determine the optimal granular-
ity of n-gram features.
Table 8   Classification results on 
the original and pre-processed 
dataset
Model
Raw
Preprocessed
P
R
F1
Acc
P
R
F1
Acc
Naive Bayes
80.89
80.48
80.54
80.48
81.84
81.69
81.73
81.69
SVM
78.08
77.78
77.42
77.78
81.64
81.27
81.00
81.27
Random Forest
78.60
77.79
77.24
77.79
82.25
81.51
81.15
81.51
Logistic Regression
81.12
80.84
80.60
80.84
83.00
82.63
82.40
82.63
XGBoost
78.34
77.64
77.12
77.64
81.25
79.44
78.69
79.44
Table 9   Classification results 
using unigram, bigram and 
trigram on raw vs preprocessed 
dataset
Word level
Model
Raw
Preprocessed
P
R
F1
Acc
P
R
F1
Acc
Unigram
Naive Bayes
81.84
81.80
81.69
81.80
82.88
82.84
82.74
82.84
SVM
81.64
81.63
81.53
81.63
82.83
82.61
82.43
82.61
Random Forest
78.06
77.93
77.67
77.93
81.96
81.59
81.34
81.59
Logistic Regression
80.14
80.17
80.09
80.17
82.00
81.96
81.84
81.96
XGBoost
76.93
76.36
75.82
76.36
80.84
79.58
78.98
79.58
Bigram
Naive Bayes
73.27
71.26
69.58
71.26
72.25
67.21
63.27
67.21
SVM
71.95
71.97
71.58
71.97
68.13
68.09
67.30
68.09
Random Forest
70.00
67.46
64.73
67.46
71.88
63.01
55.66
63.01
Logistic Regression
71.33
69.01
66.78
69.01
73.12
64.74
58.55
64.74
XGBoost
68.79
64.05
58.86
64.05
72.29
60.42
50.33
60.42
Trigram
Naive Bayes
68.35
60.94
52.50
60.94
66.38
56.84
42.91
56.84
SVM
62.80
62.88
61.11
62.88
59.12
56.91
45.09
56.91
Random Forest
68.14
58.49
46.86
58.49
71.54
56.47
41.62
56.47
Logistic Regression
70.13
58.24
45.91
58.24
71.98
56.57
41.82
56.57
XGBoost
67.18
57.16
43.68
57.16
75.42
56.05
40.55
56.05

--- Page 17 ---

Social Network Analysis and Mining (2025) 15:82	
Page 17 of 30 
82
Moving beyond word-based n‑grams, we next applied 
TF‑IDF at the character level, using unigrams up to five-
grams. Table 10 presents result for Naïve Bayes, SVM, 
Random Forest, Logistic Regression, and XGBoost on both 
raw and preprocessed data. Overall, raw text often led to 
higher accuracy and F1‑scores compared to the preprocessed 
variant, a contrast to earlier experiments where cleaning the 
text generally helped. A clear pattern emerges when look-
ing at the performance as n‑gram size increases. For most 
models, character unigrams yield moderately good results, 
but as we move to 3‑grams or 4‑grams, accuracy steadily 
increases. SVM, for instance, achieves its highest accuracy 
on raw‑data score, 84.41% with 4‑grams, slightly edging out 
its performance on shorter sequences. Character 4‑grams 
appear to capture important morphological or stylistic cues 
in Albanian text such as suffixes, partial words, or repeated 
letters, without causing the feature space to become exces-
sively sparse. Overall, the character-level approach proved 
valuable for handling the dialectal variety and informal lan-
guage in our dataset.
By contrast, 5‑grams introduce more fragmentation, 
and most models exhibit slight decline in performance. For 
example, SVM’s F1‑score decreases from 84.30% at 4‑grams 
to 83.83% at 5‑grams. Logistic Regression shows a similar 
pattern. On contrary to these models, Naïve Bayes improves 
slightly when moving from 4‑grams to 5‑grams if the data 
Table 10   Classification results 
using TF-IDF at character level 
on original and pre-processed 
dataset
Char level
Model
Raw
Preprocessed
P
R
F1
Acc
P
R
F1
Acc
Unigram
Naive Bayes
69.81
68.57
68.65
68.57
60.22
59.46
53.95
59.46
SVM
73.96
73.54
73.62
73.54
72.04
71.75
71.83
71.75
Random Forest
71.79
71.75
71.77
71.75
70.39
70.45
70.41
70.45
Logistic Regression
70.73
70.26
70.35
70.26
67.50
67.36
67.42
67.36
XGBoost
70.54
70.51
70.52
70.51
69.23
69.26
69.24
69.26
Bigram
Naive Bayes
75.95
74.09
74.11
74.09
75.16
74.80
74.88
74.80
SVM
80.78
80.82
80.77
80.82
80.48
80.52
80.46
80.52
Random Forest
77.09
76.99
77.02
76.99
77.90
77.81
77.84
77.81
Logistic Regression
78.96
79.00
78.96
79.00
77.85
77.91
77.85
77.91
XGBoost
78.55
78.60
78.55
78.60
79.36
79.41
79.33
79.41
Trigram
Naive Bayes
80.04
78.64
78.69
78.64
81.21
80.92
80.97
80.92
SVM
83.71
83.62
83.51
83.62
83.40
83.32
83.20
83.32
Random Forest
80.33
80.29
80.30
80.29
81.80
81.78
81.79
81.78
Logistic Regression
83.01
83.01
82.94
83.01
82.59
82.59
82.51
82.59
XGBoost
82.71
82.61
82.47
82.61
82.10
81.92
81.74
81.92
Fourgram
Naive Bayes
82.06
81.36
81.42
81.36
83.30
83.30
83.30
83.30
SVM
84.52
84.41
84.30
84.41
84.44
84.22
84.07
84.22
Random Forest
81.90
81.92
81.91
81.92
82.25
82.28
82.25
82.28
Logistic Regression
83.64
83.62
83.54
83.62
83.44
83.14
82.95
83.14
XGBoost
83.30
82.86
82.61
82.86
82.94
81.99
81.59
81.99
Fivegram
Naive Bayes
83.11
83.07
83.08
83.07
83.10
83.09
83.00
83.09
SVM
84.08
83.95
83.83
83.95
82.90
82.80
82.67
82.80
Random Forest
82.20
82.19
82.09
82.19
82.24
81.98
81.76
81.98
Logistic Regression
83.46
83.37
83.26
83.37
82.00
80.92
80.44
80.92
XGBoost
82.68
81.55
81.09
81.55
81.74
80.04
79.35
80.04
Table 11   Classification results 
using FastText on original and 
pre-processed dataset
Model
Raw
Preprocessed
P
R
F1
Acc
P
R
F1
Acc
FastText
Naive Bayes
66.99
66.00
66.10
66.00
70.13
61.96
60.03
61.96
SVM
73.22
73.31
73.10
73.31
76.91
76.97
76.92
76.97
Random Forest
71.90
71.98
71.70
71.98
75.11
75.13
75.12
75.13
Logistic Regression
73.98
74.07
73.94
74.07
77.70
77.74
77.72
77.74
XGBoost
74.91
74.98
74.93
74.98
77.02
77.05
77.03
77.05

--- Page 18 ---

	
Social Network Analysis and Mining (2025) 15:82
82 
Page 18 of 30
is preprocessed, but this gain is relatively small and still 
lags behind other classifiers on the raw text. Interestingly, 
while standard preprocessing removes spelling noise and 
normalizes tokens, certain nuanced markers in the original 
Albanian comments, like colloquial spelling patterns or par-
tial words seem beneficial for character‑level modeling. As 
a result, raw data consistently yields stronger classification 
metrics in this setup, surpassing our earlier results.
Next, we experimented with FastText word embed-
dings. From the results shown in Table 11, we observe that 
the overall performance of models is substantially lower 
compared to our previous experiments. While Logistic 
Regression on the preprocessed dataset reached the best 
F1-score of 77.72% and accuracy of 77.74%, this is still 
lower compared to the 80–84% range obtained in the pre-
vious experiments. Similarly, XGBoost yielded an accu-
racy of 77.05% on preprocessed text that is below its best 
performance obtained using TFIDF feature representa-
tions. These outcomes suggest that FastText embeddings, 
though beneficial for many NLP tasks, may be less suited 
unless further tuned or supplemented with additional fea-
tures specific to Albanian hate speech.
In addition to standard embeddings, we introduced 
handcrafted features and applied various feature selection 
techniques, including the full set, threshold-based filter-
ing, and recursive feature elimination (RFE), to assess 
whether this approach would enhance classification per-
formance. The results are presented in Table 12. Although 
models such as XGBoost and Random Forest exhibit slight 
improvements by judiciously pruning non-informative fea-
tures, their overall performance remains inferior to that 
reported with optimized text-based features, such as char-
acter-level n-grams. Even after applying RFE, XGBoost’s 
best F1-score of 77.07% is significantly lower compared to 
its benchmarks of 80% and above in previous setups. These 
findings further emphasize that handcrafted or embedding-
based approaches do not necessarily outperform simpler 
Table 12   ML models 
performance using different 
feature set
Feature selection method
Model
P
R
F1
Acc
Full set of features
Naive Bayes
73.59
65.39
63.89
65.39
SVM
64.20
64.51
63.92
64.51
Random Forest
74.32
74.34
74.33
74.34
Logistic Regression
71.18
71.20
71.19
71.20
XGBoost
76.90
76.97
76.90
76.97
Threshold-based filtering
Random Forest
73.99
74.06
74.01
74.06
Naive Bayes
70.29
69.89
68.96
69.89
Logistic Regression
70.19
70.30
70.21
70.30
SVM
64.22
64.53
63.93
64.53
XGBoost
76.01
76.09
76.01
76.09
Recursive Feature Selection
Naive Bayes
68.63
67.86
67.97
67.86
SVM
64.20
64.51
63.92
64.51
Random Forest
75.02
75.05
75.03
75.05
Logistic Regression
75.39
75.44
75.25
75.44
XGBoost
77.06
77.12
77.07
77.12
Table 13   Feature ranking by RF with handcrafted features
Rank
All features
Importance
Selected features
Importance
RFE
Importance
1
negative_word_count
0.0207
cos_sim_off_300
0.0264
cos_sim_off_300
0.0224
2
lexical_density
0.0176
negative_word_count
0.0255
negative_word_count
0.0211
3
cos_sim_off_300
0.0172
capital_letter_frequency
0.0250
lexical_density
0.0198
4
capital_letter_frequency
0.0170
lexical_density
0.0249
cos_sim_pos_100
0.0186
5
cos_sim_pos_300
0.0169
cos_sim_pos_300
0.0217
total_consonant_count
0.0174
6
cos_sim_pos_100
0.0169
cos_sim_pos_100
0.0190
cos_sim_pos_300
0.0174
7
avg_word_length_variability
0.0146
total_consonant_count
0.0180
alphabetic_count
0.0160
8
total_consonant_count
0.0143
avg_trigram_length
0.0168
capital_letter_frequency
0.0156
9
avg_bigram_length
0.0142
avg_word_length_variability
0.0162
avg_trigram_length
0.0138
10
avg_line_length
0.0140
var_word_length
0.0144
hapax_legomena
0.0133

--- Page 19 ---

Social Network Analysis and Mining (2025) 15:82	
Page 19 of 30 
82
yet meticulously engineered TF-IDF representations, at 
least under the current experimental conditions.
Although handcrafted features did not outperform our 
best TF IDF–based models, they provide valuable inter-
pretability insights into how machine learning algorithms 
perceive hate speech in Albanian. Table 13 lists the top 
features ranked by importance under different selection 
methods, highlighting recurring metrics such as ‘negative_
word_count’, ‘lexical_density’, capital letter frequency and 
‘cos_sim_off_300’. These features consistently appear at or 
near the top, implying that they hold some predictive power, 
even if overall accuracy remains lower than with TF IDF.
Figure 7 depicts the RFE process for a Random Forest 
classifier, showing how performance changes as we progres-
sively remove weaker features. Interestingly, the best F1 
score yields around 0.75 with roughly 500 features retained, 
indicating that while adding more handcrafted variables 
can sometimes help, excessive inclusion eventually leads to 
overfitting or noise. This trade-off is especially observed in 
low resource contexts, where carefully curated features may 
lose effectiveness if they overlap or fail to capture deeper 
language nuances. This shows that a huge number of features 
is required to successfully determine HS, which is generally 
unusual, as we aim to have a good and effective feature set 
for the whole domain.
In Fig. 8, we provide a SHAP visualization, illustrating 
each feature’s relative contribution to the Random For-
est’s decisions. Features like ‘negative_word_count’ and 
‘cos_sim_off_300’ exert a strong positive influence on hate 
speech predictions, whereas more generic indicators such 
as ‘avg_line_length’ or ‘char_count’, are less impactful. By 
examining these SHAP values, we can glean which hand-
crafted cues most consistently correlate with hateful content. 
The high impacts of features like ‘negative_word_count’ 
align with the presence of derogatory or insulting terms, 
while ‘lexical_density’ could reflect the detailed or targeted 
nature of hateful commentary.
Figure 9 shows the calibration curve for the SVM model, 
illustrating how closely the model’s predicted probabilities 
match the actual fraction of positives for each class. A per-
fectly calibrated model would lie along the diagonal green 
line, indicating that, for instance, samples predicted with 
0.7 probability of hate speech are indeed hateful 70% of the 
time. In our SVM calibration curve, both the non-HS and HS 
lines follow the diagonal reasonably well, suggesting that the 
model’s probability estimates are relatively reliable, though 
Fig. 7   RFE evaluation process with RF

--- Page 20 ---

	
Social Network Analysis and Mining (2025) 15:82
82 
Page 20 of 30
small deviations from the diagonal do indicate areas where 
the SVM’s confidence may be slightly off.
5.2  Deep learning and transformers performance 
analysis
We evaluated several neural network architectures and 
compared them against transformer-based models. As can 
be seen from Table 14, the neural network models yield 
an accuracy and F1 score of 80–81%, which is slightly 
lower than both the best traditional machine learning setup 
(SVM with 4 char TF IDF) and the transformer-based 
approaches. This performance change can be explained by 
the nature of deep learning models such as CNN, LSTM, 
BiLSTM and GRU, which generally require large and 
diverse datasets to generalize effectively. Although our 
dataset is the largest available for Albanian hate speech, it 
Fig. 8   SHAP values generated 
by the RF model
Fig. 9   Calibration curve for the SVM model

--- Page 21 ---

Social Network Analysis and Mining (2025) 15:82	
Page 21 of 30 
82
remains relatively small by deep learning standards. More-
over, Albanian social media content often includes dialec-
tal variation, informal spelling, and code-switching, fac-
tors that introduce inconsistencies which sequence-based 
models struggle to handle. In contrast, traditional machine 
learning models fed with rich features (character-level 4-g) 
are more resilient to such variability and sparsity. Notably, 
this limitation applies to neural networks only. However, 
Transformer-based models, performed significantly better, 
achieving the highest performance on our experiments due 
to their large-scale multilingual pretraining and contextual 
understanding.
The fine-tuned XLM RoBERTa model achieves the 
highest overall performance on raw data, with an F1 score 
of 85.89% and an accuracy of 85.93%, slightly exceeding 
the 84% accuracy range of SVM with character n grams. 
mBERT also shows similar performance, confirming that 
multilingual representations help capture deeper semantic 
nuances in Albanian hate speech. However, this increase in 
performance comes with trade-offs as well. Fine-tuning and 
deploying transformer models is computationally intensive 
and resource demanding compared to classical ML mod-
els. In a low resourced setting, such requirements might be 
prohibitive.
It is noteworthy that pre-processed text does not always 
outperform raw text for these transformers; large pretrained 
models often demonstrate robust noise tolerance. It is also 
worth noting that BERTweet, despite being pre-trained on 
English-language tweets, still manages to produce competi-
tive outcomes for Albanian hate speech detection. This sug-
gests that certain conversational and social media patterns 
such as the use of informal syntax, short utterances, or web-
specific slang, transfer surprisingly well across languages, 
especially in noisy, user-generated text. However, a truly 
Albanian-focused social media model might push perfor-
mance even further, given sufficient domain-specific training 
data.
Overall, these findings highlight that while classical ML 
techniques can be quite competitive with careful feature 
engineering, pretrained transformers offer the advantage of 
Table 14   Classification results 
for deep learning models and 
Transformers
MODEL
Raw
Preprocessed
P
R
F1
Acc
P
R
F1
Acc
LSTM
80.42
80.38
80.40
80.38
81.39
81.42
81.39
81.42
BiLSTM
80.67
80.65
80.66
80.65
81.50
81.50
81.50
81.50
GRU​
80.85
80.79
80.64
80.79
81.26
81.28
81.20
81.28
CNN
81.00
81.00
81.00
81.00
81.05
81.09
81.06
81.09
mBERT
84.10
84.12
84.08
84.12
83.15
83.16
83.16
83.16
XLM-RoBERTa
85.91
85.93
85.89
85.93
84.12
84.03
84.05
84.03
Distil-mBERT
83.32
83.14
83.18
83.14
83.44
83.45
83.39
83.45
BERTweet
84.53
83.64
83.31
83.64
84.08
84.03
83.94
84.03
Fig. 10   SVM character 4-grams confusion matrix
Fig. 11   SVM character 4-grams classification report heatmap

--- Page 22 ---

	
Social Network Analysis and Mining (2025) 15:82
82 
Page 22 of 30
boosting performance in Albanian-language hate speech 
detection.
Figures 10 and 11 illustrate the confusion matrix and clas-
sification report for the SVM (4-gram character) model, while 
Figs. 12 and 13 show for XLM-RoBERTa. These two models 
are the best performers, SVM excelling among classic ML 
approaches, and XLM-RoBERTa leading the transformer-
based models.
SVM (4-Gram Characters)—As shown in Fig. 10, the SVM 
correctly classifies 2,616 Not Hate Speech samples and 1,786 
Hate Speech samples. However, it mislabels 520 hateful com-
ments as non-hateful, reflecting a slightly lower recall of 0.77 
for the Hate Speech category. The classification report heat-
map illustrated in Fig. 11 shows stronger metrics for the Not 
Hate Speech label, precision of 0.83 and recall of 0.90, com-
pared to Hate Speech, which drops in recall. This discrepancy 
means the SVM is somewhat conservative in identifying hate 
speech, often defaulting to a neutral prediction if uncertain.
Figure 12 shows that XLM-RoBERTa correctly identi-
fies 2,590 Not Hate speech comments and 1,891 hate com-
ments, misclassifying 415 hateful samples as Not-Hate speech. 
Although errors remain, XLM-RoBERTa model still misses a 
notable number of hate comments (415 false negatives in the 
test set), while its recall for hate speech, 0.82 is higher then the 
SVM’s 0.77. This indicates it misses fewer hateful posts than 
the SVM, a valuable improvement. The classification report 
heatmap shown in Fig. 13 confirms more balanced perfor-
mance across both labels. Precision, recall, and F1-score for 
Not Hate Speech and Hate Speech are in the in the range of 
0.82–0.89, contributing to XLM-RoBERTa’s overall advan-
tage in macro-averaged metrics. Nevertheless, the persistence 
of false negatives (hateful content not detected) underlines 
that even our best model has not fully solved the detection 
challenge.
In general, SVM (4-g) and XLM-RoBERTa both handle 
Albanian hate speech effectively but differ in their error pat-
terns. The SVM yields fewer false positives on hate speech but 
pays the price in lower recall. XLM-RoBERTa, on the other 
hand, better captures subtle hateful cues, translating into fewer 
missed hate speech comments.
These findings directly address RQ1, confirming that in our 
case a fine-tuned XLM-RoBERTa yieleded a six-point higher 
F1 score in performance in results reported in prior Albanian 
hate speech studies with classical models (Fetahi et al. 2024). 
A comparative analysis is also provided in sections below.
We additionally ran experiments using fivefold cross-
validation on the two best performing models, the fine-tuned 
XLM-RoBERTa and the SVM with 4-gram character TF-IDF. 
The results are summarized in Table 15. As can be seen from 
the table, the transformer’s weighted F1 score is 85.4% ± 0.8, 
while the SVM’s is 84.0% ± 0.7. This suggests similar per-
formance to the training/testing split, indicating the XLM-
RoBERTa still performs better in different folds. However, 
the XLM-RoBERTa models show more fold-to-fold variation 
Fig. 12   XLM-RoBERTa confusion matrix
Fig. 13   XLM-RoBERTa classification report heatmap
Table 15   Classification results 
under 5-fold cross validation for 
the two best-performing models
Model
P
R
F1
Acc
XLM-RoBERTa (fine-tuned)
85.5 ± 0.83
85.4 ± 0.81
85.4 ± 0.81
85.4 ± 0.81
SVM + 4-gram char TF-IDF
84.1 ± 0.75
84.1 ± 0.73
84.0 ± 0.73
84.1 ± 0.73

--- Page 23 ---

Social Network Analysis and Mining (2025) 15:82	
Page 23 of 30 
82
due to their larger and more complex architecture. The SVM 
is slightly more stable.
5.3  Impact of feature engineering 
and preprocessing
In our experiments, models using word-level TF-IDF uni-
grams consistently outperformed models using higher 
n-grams (bigrams, trigrams). This result suggests a high 
degree of written variation happening in Albanian social 
media, making it difficult to find consistently repeating mul-
tiword patterns. Consequently, simpler unigram representa-
tions, coupled with comprehensive text cleaning captured 
enough discriminative power without becoming too sparse.
The written variation texts is furthered confirmed by the 
experiments with FastText embeddings trained largely on 
standard Albanian, where registered a notable drop in per-
formance when applied to social media comments. This gap 
indicates that typical, formal word embeddings may strug-
gle with region-specific slang, creative spelling, and dialects 
prevalent in online discourse. The discrepancy highlights 
the importance of aligning embedding training data with 
the real-world style and variability found in user-generated 
comments.
Despite incorporating nearly 900 handcrafted features, 
analysis revealed that 500 or more were still retained by RFE 
for optimal performance—an unusually high number. This 
underscores the heterogeneous nature of Albanian social 
media language: user behaviors, punctuation patterns, and 
morphological quirks generate a broad feature space with no 
single dominant set of indicators. Even so, carefully engi-
neered features offered modest improvements, especially 
with tree-based models like Random Forest and XGBoost.
Character-level TF-IDF with 4-gram emerged as espe-
cially robust for traditional ML, effectively capturing sub-
word elements and morphological variations, relatively 
immune to spelling inconsistencies. Moreover, RQ2 exam-
ined how different feature extraction techniques influence 
performance in a low-resource setting, revealing that char-
acter-level n-grams consistently outperform word-level and 
other representations in ML. This is largely due to their 
robustness against spelling variations and slang, whereas 
transformer models appear more resilient to raw noise, bene-
fiting from contextual embeddings. These findings also rein-
force how heavily social media texts deviate from standard 
Table 16   Classifiers prediction results on selected comments
No
Comment
Ground truth label
SVM
NB
XGBoost
BiLSTM
CNN
mBERT
XLM-
Rob-
erta
1
Ore qelbesir pse nuk e realizoj Thaçi
ket marrveshje por e heshti per 11 vjet
(Hey scumbag why didn't Thaçi implement this 
agreement but kept it silent for 11 years?)
HS
✓
×
✓
✓
×
×
✓
2
:USER: ngo qaj ban kti pisit
(:USER: Listen to what this bastard they are doing.)
HS
✓
×
×
✓
×
✓
✓
3
Per heker i qojn mi shit u hyp qmimi
(They go to sell it for iron the price has gone up)
No HS
×
×
×
×
×
✓
×
4
Tmerri
(The terror)
HS
×
×
×
×
×
×
×
5
:USER: ngjoje ms mrri mas kurvave
(:USER: Listen to him don't follow after the whores)
HS
×
×
✓
×
×
✓
✓
6
Kjo delarat nuk tu ka lyp hiq
(Nobody asked for this statement at all)
No HS
×
✓
×
✓
×
×
✓
7
Tash i shtin ne b….te vet
(Now he shoves them up his own a…)
HS
✓
✓
×
×
×
✓
✓
8
.ja ja shetani asht shka ta lypish
(no no the devil is what you're asking for)
HS
✓
✓
×
✓
✓
✓
×
9
:USER: ill fare qënke, po shaminë përse nuk e vë!?
(User you are ill, why don’t you put the scarf!?)
HS
×
×
×
×
×
×
×
10
Race e keqe
(bad breed)
HS
×
✓
×
×
×
×
×
11
Mjekesia ligjore thote 
(forensic medicine says )
No HS
×
×
✓
×
×
×
✓
12
Bravo Četnici
(Bravo Chetniks)
HS
×
×
×
×
×
×
×

--- Page 24 ---

	
Social Network Analysis and Mining (2025) 15:82
82 
Page 24 of 30
written forms, solidifying the significance of subword-level 
analysis.
While we applied extensive text preprocessing, the final 
accuracy improvements were inconsistent. For some classi-
cal ML approaches, removing noise improved token consist-
ency and helped models learn more effectively. However, 
higher-performing models such as character n-grams or 
contextual transformers, often achieved equal or superior 
results using the original raw text, capitalizing on nuances 
otherwise lost during cleaning. Consequently, text preproc-
essing yielded mixed performance overall, reinforcing the 
idea that no single preprocessing strategy works best across 
all architectures.
5.4  Error analysis
In this section, we take a closer look at where and why dif-
ferent models, both traditional and deep learning, stumble by 
manually inspecting comments that lead to errors, which are 
shown on Table 16, thereby exemplifying on each model’s 
inherent weaknesses.
In the following, we provide a summary of key observa-
tions by investigating the comments and classifier results.
1. Ambiguity and Short Text
Comment no. 4, “Tmerri, (eng. The terror)” is marked as 
HS but is very short and lacks explicit hateful terms, making 
it ambiguous. Multiple models labeled it as non-hateful, sug-
gesting that single-word statements pose challenges unless 
the model is strongly attuned to context or implicit mean-
ings. Similarly, the comment no. 10 “Race e keqe, (eng. 
Bad breed) shows an hateful short phrase in just two words, 
which was misclassified by many models.”
2. Slurs and code-mixed words
Comments no. 1 and 5 include direct insults "qelbesir 
(eng. scumbag)", “kurvave (eng. whores)”, which some 
models such as XGBoost, mBERT, XLM-RoBERTa catch 
by recognizing hateful keywords or morphological patterns. 
Other models as NB and CNN often couldn’t identify the 
hateful words. Comment no. 9 starts with an English term 
“ill”, which is used offensively within Albanian, turning it 
into a disguised insult, which of all the classifiers misclas-
sified the example, without the ability to correctly identify 
the code-mixed words within comments.
3. Colloquial/Slang Variations
Comments no. 2 and 3 illustrate creative spellings or 
slang. Classifiers that rely on rigid token matching may 
miss these terms or conflate them with more benign words, 
leading to errors. Model architectures such as transformers 
shows that generally they could handle slang better.
4. Negative versus Hateful
Comment no. 6, “Kjo deklarat nuk tu ka lyp hiq (eng. 
Nobody asked for this statement at all)” is negative but not 
hateful explicitly. Some models incorrectly flag it as hate 
speech, revealing a tendency to associate negativity with 
hate. This underscores the importance of distinguishing 
offensive or harsh language from genuinely negative content.
5. Contextual Cues
In comment no. 7, the phrase is incomplete yet widely 
understood as insulting in context. However, models using 
subword or transformer embeddings such as mBERT, XLM-
RoBERTa often still flag it as hate speech, while simpler 
classifiers struggle. This suggests that the more advanced 
models recognize the intent despite missing characters, 
whereas others rely more on exact word matching. However, 
none of the models reliably detected when offensive words 
were altered or obscured with symbols such as asterisks or 
bullet points, often either misclassifying or failing to identify 
them altogether.
6. Religious hostility and Dialects
In the comment no. 8 “ja ja shetani asht shka ta lyp-
ish, (eng.no no devil is whatever you request)”, the 
term”shejtani (devil)” serves as a potent, quasi-religious 
insult, further complicated by local dialect words making 
the message appear less offensive to certain models. Interest-
ingly, the XLM-RoBERTa model missclassified it, whereas 
simple simples classifiers identified the histlity. This dis-
crepancy suggets that even advanced transformers might 
lack adequate dialect coverage. In Albanian usage, labeling 
someone as”devil” is highly insulting, illustrating how reli-
gious references and dialectal forms demand specialised 
handling to detect HS accurately.
7. Sarcasm and Emojis
Comment no. 11 “Mjekesia ligjore thote  (eng. forensic 
medicine says )” looks straightforward but is accompanied 
by multiple laughing emojis. This punctuation of emojis, 
often signals sarcasm or mocking, all of which confused the 
models by labeling it as hateful. Sarcasm detections remain a 
challenge in Albanian social media where emojis can replace 
explicit words.
8. Cultural terms
Comment no. 12 “Bravo Četnici (eng. Chetniks)” com-
bines positive language in which case is “Bravo” with the 
word “Chetniks” which is a term historically linked to ethnic 
violence in the Balkans, especially the Albanians. Models 
lacking this type of context often treat this phrase as positive 
such in this case, failing to identify the hateful subtext. This 
shows that including samples with domain-specific knowl-
edge, particularly sociopolitical references, can be critical 
and enhance the models.
Overall, these errors highlight recurring themes that 
address RQ3:
(1)	 short, context-poor messages are easy to be wrongly 
classified
(2)	 morphological and code-mixed slang variants pose dif-
ficulties, especially for simpler models

--- Page 25 ---

Social Network Analysis and Mining (2025) 15:82	
Page 25 of 30 
82
(3)	 negativity does not always equate to hate
(4)	 Religious and dialectal cues can confuse even advanced 
transformers, and
(5)	 Sarcasm and cultural references require deeper, 
domain-specific knowledge
In addition, we investigate also comments with the gener-
ated plots by using LIME in following.
In the example illustrated in Fig. 14, the LIME visuali-
zation highlights “kokshe (eng. you are)” as an offensive 
marker, the analysis overlooks the dot (“.”) in the word 
“m.ti (eng. shit)”) that subtly encode insulting content 
without stating it outright and hiding a character. Because 
these punctuation cues are omitted or treated as negligible 
tokens, the model does not capture the implied aggres-
sion. This underscores how hateful language can be veiled 
through informal punctuation or deliberate omissions, and it 
highlights a gap in token-based interpretability methods that 
focus on explicit words rather than implicit context.
The LIME visualization shown in Fig. 15, the word 
“musliman (eng. muslim)” appears with a net pull toward 
Not Hate Speech, reflecting its generally neutral or identity-
affirming usage in the training data. However, the author’s 
tone in this instance is deliberately sarcastic implying that 
you are not a Muslim. LIME correctly shows “muslim” as 
pivotal, but it cannot fully detect the ironic context. This 
example highlights a shortcoming common to many models 
where words with neutral dictionary definitions can still be 
weaponized in context, and the model may struggle to grasp 
such subtlety without deeper contextual cues.
In the LIME visualization 3 in Fig. 16, although “autop-
sin (eng. autopsy)” consistently pushes the model to label 
the comment as hateful, the term itself denoting an autopsy, 
is not inherently hateful. Instead, the classifier appears to 
have learned from training instances where words associated 
with violence or death correlate with hostile or threatening 
posts. Consequently, autopsy becomes a red flag for hate 
speech even when the actual intention is milder or unrelated 
to bigotry. This illustrates that terms with strong negative 
connotations (e.g., references to death) can skew model 
predictions, unless there is enough context to distinguish 
a genuinely hateful remark from a merely severe or morbid 
expression.
Fig. 14   LIME explanation 1
Fig. 15   LIME Explanations 2
Fig. 16   LIME Explanations 3
Fig. 17   LIME Explanations 4

--- Page 26 ---

	
Social Network Analysis and Mining (2025) 15:82
82 
Page 26 of 30
The LIME explanations in Fig. 17 shows “musu” (a dia-
lect form for “mos u,” meaning “don’t you”) and “tutni (eng. 
fear)” are especially influential. Because “musu” is spelled 
informally, the model partially associates it with negative 
or forceful language, as well as the “fear” is nudging the 
comment toward hateful classification. Overall, the classi-
fier wavers between negative and hateful, underscoring how 
dialect-specific grammar can confuse automated detection 
when words are spelled or used in non-standard ways.
In the LIME vizualizations in the Fig. 18, the XAI model 
indicates that “vështirë (eng. difficult)" and “gjet (eng. find)" 
show the strongest influence toward a non-hateful classifica-
tion, as they do not match any known offensive patterns. In 
contrast, “Ma njeri (eng. more human)” and “kurgja (eng. 
nothing)” receive smaller weights, leaving the sarcastic tone 
largely undetected. The net result is that the model deems 
the statement more neutral than hateful. This highlights how 
sarcasm can slip by token-based analysis when the pivotal 
words (“difficult,” “find”) appear harmless, and subtle con-
text (like a mocking or dismissive tone) goes unrecognized.
The findings above demonstrate that hatefulness in Alba-
nian can be masked or misconstrued by short texts, crea-
tive slang, or context-dependent negativity. Even the most 
advanced models occasionally encounter difficulties in 
interpreting subtle insults or ambiguous statements that lack 
explicit hate indicators. Understanding these nuanced failure 
modes, where negativity does not necessarily equal hate and 
where context or hidden cues can significantly alter mean-
ing, offers a clear direction for refining future hate speech 
detection efforts.
5.5  Comparative analysis
By presenting diverse perspectives, our objective is to high-
light the relative advantages of our methodologies and eluci-
date the broader implications of our research. This compara-
tive analysis compares our study’s methods with those in 
Albanian and other low-resource language datasets, provid-
ing a comprehensive overview of the field.
Throughout the study, as outlined in Sects. 5.1 and 5.2, 
we systematically evaluated a range of classification mod-
els for Albanian hate speech detection, commencing with 
traditional machine learning models and progressing to 
more sophisticated transformer-based architectures. Initial 
experiments demonstrated that unigram models employing 
TF-IDF features often outperformed complex bigram and 
trigram models. Despite the limited morphological knowl-
edge available, the NB, LR, and SVM models achieved com-
petitive F1 scores, averaging between 81 and 83%. Notably, 
when employing character-level grams, particularly the 
SVM trained with 4-gram characters, the F1 score reached 
a peak of 84%, making it the most effective among classi-
cal machine learning baselines. While handcrafted features 
provided interpretability through domain-specific cues, they 
exhibited inferior performance compared to TF-IDF models. 
Although the analysis revealed that the models themselves 
did not exhibit a significant impact, as a combination of 
representation methods yielded inconsistent results, it was 
more probable that the feature selection method had the most 
significant influence on the models’ accuracy.
Deep neural networks, including LSTM, BiLSTM, GRU, 
and CNN, were also employed and demonstrated competi-
tive but not significantly improved performances, consist-
ently reaching F1-scores around 80–81%. These neural 
models, despite theoretical strengths in modelling textual 
sequences, did not surpass the classical ML baselines sub-
stantially, suggesting potential limitations due to the inherent 
complexity of modelling subtle linguistic nuances in Alba-
nian social media text.
However, the proposed model of the fine-tuned transform-
ers, specifically XLM-RoBERTa, benefited from multilin-
gual contextual embeddings, outperforming the baseline 
methods and achieving an F1-score of 85.89%. Transformers 
generally overcome the limitations encountered by simpler 
models, such as ML, particularly in detecting subtle and 
context-dependent expressions.
To extend the generalizability of our findings, we evalu-
ated the performance of the same XLM-RoBERTa archi-
tecture and experimental setup across a range of available 
datasets in the Albanian language and in other low-resource 
languages. The results are summarized in Table 17.
As can be seen from Table 17, the model consistently 
achieved high performance across typologically and linguis-
tically diverse datasets. It also performed well on various 
datasets in the Albanian language, providing promising and 
satisfactory results. Furthermore, it is notable that the model 
performed comparably well on both Indo-European lan-
guages such as Albanian, Urdu, and Bengali, and non-Indo-
European languages like Arabic and Sinhala. These find-
ings suggest that multilingual transformer models, when 
Fig. 18   LIME Explanations 5

--- Page 27 ---

Social Network Analysis and Mining (2025) 15:82	
Page 27 of 30 
82
fine-tuned, provide strong and adaptable solutions for hate 
speech detection in low-resource settings.
Furthermore, based on our findings the variability of 
reported scores is highly influenced by three independent 
factors:
(1)	 Language-specific characteristics, such as dialectal 
diversity, informal spelling, and cultural references;
(2)	 Dataset scale and annotation quality; and
(3)	 Model architecture alignment with linguistic properties.
Consequently, our analysis demonstrates that while chal-
lenges in Albanian, such as limited morphological resources, 
dialectal diversity, and informal language forms, are sig-
nificant, especially in social media, similar issues persist 
across various low-resource languages. What distinguishes 
our work is the combination of an extensive annotated data-
set, rigorous evaluation of diverse feature representations, 
and the integration of transformer-based methods that col-
lectively yield a state-of-the-art performance benchmark. 
Furthermore, our approach mirrors successful strategies that 
can be employed in other underrepresented languages, illus-
trating that techniques such as transfer learning are broadly 
applicable and yield satisfactory results.
5.6  Practical implications
This study provides practical implications for researchers 
and NLP practitioners working on Albanian. It presents a 
fine-tuned XLM-RoBERTa model for hate speech detec-
tion in Albanian social media, achieving high accuracy in 
low-resource settings. The model can be applied to other 
low-resource languages. Trained and tested on a real-life 
Facebook dataset, the methodology is generalisable to other 
social media platforms, such as Instagram, X (formerly Twit-
ter), and YouTube, with similar content. The study provides 
insights from technical and interpretability perspectives 
through rigorous machine learning experiments, deep learn-
ing models, and explainable AI techniques. In environments 
with limited human moderation resources, the proposed 
transformer-based solution with LIME improves the trans-
parency and understanding of decision making process of 
the model.
6  Limitations
Despite the robust performance of our approach, several lim-
itations remain. First, the scarcity of publicly available NLP 
tools and linguistic resources for Albanian posed continual 
challenges: many conventional techniques such as stemming 
required custom implementations that may not fully cap-
ture the breadth of dialectical variants and colloquialisms 
on social media. Second, the hate speech annotation process 
itself was inherently complex and subjective; cultural norms 
and individual tolerance levels can differ significantly, mak-
ing it difficult to establish universally accepted boundaries 
for what constitutes hateful content. Finally, our experi-
ments encountered computational restraints, particularly 
when fine-tuning large transformer models on lengthy train-
ing cycles; more extensive hyperparameter optimization or 
ensemble strategies could further improve performance but 
would demand additional time and computational capacity.
Table 17   Comparative performance of XLM-RoBERTa on Albanian and other low-resource language hate speech datasets
Dataset
Language
Dataset size
Source
Downstream task
XLM-RoBERTa
F1 score
Fetahi et al. v3
Albanian
20,860
Facebook
Hate speech detection
85.89%
Shaj (Nurce et al. 2022)
Albanian
11,874
Instagram and YouTube
Abusive Language Detection
89.84%
Fetahi et al. v1 (Fetahi et al. 
2024)
Albanian
11,343
Facebook
Hate speech detection
82.30%
Fetahi et al. v2 (Fetahi et al. 
2024)
Albanian
15,947
Facebook
Hate speech detection
86.01%
Other low-resourced languages
RU-HSD-30K (Bilal et al. 
2022)
Roman Urdu
30,000
Twitter
Hate speech detection
88.82%
SOLD (Ranasinghe, et al. 
2024)
Sinhala
10,000
Twitter
Hate/Offensive language 
detection
85.00%
UHated (Arshad et al. 2023)
Urdu
7,800
Twitter
Hate Speech detection
82.00%
Romim et al. (Romim et al. 
2021)
Bengali
30,000
TikTok, YouTube and Face-
book
Hate Speech detection
90.58%
Alakrot et al. (Alakrot et al. 
2018)
Arabic
15,050
YouTube
Anti-social behaviour (Offen-
sive/Cyberbullying)
86.41%

--- Page 28 ---

	
Social Network Analysis and Mining (2025) 15:82
82 
Page 28 of 30
7  Conclusions and future work
In this study, we investigated the hate speech detection 
task in a low-resource language, Albanian, characterized 
by extensive dialectal variation and a scarcity of advanced 
NLP tools. We collected a real-life dataset annotated manu-
ally using a multi-annotator protocol with majority voting. 
Various experiments employing a diverse range of classi-
fication approaches, including classical machine learning 
algorithms, deep learning, and state-of-the-art transformer 
models, were conducted. The experimental results revealed 
that character n-gram features with TF-IDF exhibited supe-
rior performance for non-transformer models. Conversely, 
the XLM-RoBERTa model em ploying embeddings demon-
strated the best performance in hate speech detection for the 
Albanian language. Our results set a new benchmark for this 
task, but they also highlight that further gains may require 
addressing dialectal variation and implicit context beyond 
what the current models capture. Additionally, the findings 
demonstrated that character-level n-grams consistently out-
performed word-level and other traditional representation 
methods. This is mainly due to: (1) morphological richness 
of Albanian Language, (2) extended suffix based word-form-
ing nature of Albanian and (3) the robustness of the char 
level representations against spelling variations slang and 
dialectic variations. Contrarily, transformer models exhib-
ited greater resilience to raw data.
For future work, we plan to expand our hate speech detec-
tion capabilities to encompass multi-modal detection. Fur-
thermore, we explore the potential of domain and dialect-
specific embeddings to further enhance the robustness of our 
speech hate detection models.
Author contributions  E. F.: Conceptualization, methodology, writing 
original draft, data collection, experiments, data curation, formal analy-
sis, validation, review, and editing; A. S.: Data collection, preprocess-
ing, data curation, experimental setup, implementation, and statistical 
analysis; M. H.: Supervision, project administration, validation, critical 
review; Z.K.: Supervision, manuscript refinement, technical valida-
tion, review; E.C: Supervision, review, enhancements, implementa-
tion; A. M.: Data curation, software, experimental design, and testing. 
All authors contributed to the manuscript's preparation, reviewed, and 
approved the final version.
Funding  Open access funding provided by Linnaeus University.
Data availability  The data supporting this study are available upon 
request.
Declarations 
Conflict of interest  The authors declare no competing interests.
Ethical approval and informed consent  Not applicable.
Open Access  This article is licensed under a Creative Commons Attri-
bution 4.0 International License, which permits use, sharing, adapta-
tion, distribution and reproduction in any medium or format, as long 
as you give appropriate credit to the original author(s) and the source, 
provide a link to the Creative Commons licence, and indicate if changes 
were made. The images or other third party material in this article are 
included in the article’s Creative Commons licence, unless indicated 
otherwise in a credit line to the material. If material is not included in 
the article’s Creative Commons licence and your intended use is not 
permitted by statutory regulation or exceeds the permitted use, you will 
need to obtain permission directly from the copyright holder. To view a 
copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
References
Digital 2021: Kosovo. https://​datar​eport​al.​com/​repor​ts/​digit​
al-​2021-​kosovo
Ajdari J, Ismaili F, Raufi B, Zenuni X (2017) Automatic hate speech 
detection in online contents using latent semantic analysis. Pres-
sacademia 5(1):368–371. https://​doi.​org/​10.​17261/​press​acade​mia.​
2017.​612
Ajvazi A, Hardmeier C (2022) A dataset of offensive language in 
Kosovo social media. In: 2022 language resources and evalua-
tion conference LRs 2022, no June, pp 1860–1869
Al Anezi FY (2022) Arabic hate speech detection using deep recurrent 
neural networks. Appl Sci. https://​doi.​org/​10.​3390/​app12​126010
Alakrot A, Murray L, Nikolov NS (2018) Dataset construction for the 
detection of anti-social behaviour in online communication in 
Arabic. Procedia Comput Sci 142:174–181. https://​doi.​org/​10.​
1016/j.​procs.​2018.​10.​473
Altaf A et  al (2022) Deep learning based cross domain sen-
timent classification for Urdu language. IEEE Access 
10(August):102135–102147. https://​doi.​org/​10.​1109/​ACCESS.​
2022.​32081​64
Arshad MU, Ali R, Beg MO, Shahzad W (2023) UHated: hate speech 
detection in Urdu language using transfer learning. Lang Resour 
Eval 57(2):713–732. https://​doi.​org/​10.​1007/​s10579-​023-​09642-7
Ashiq W et al (2024) Roman urdu hate speech detection using hybrid 
machine learning models and hyperparameter optimization. Sci 
Rep 14(1):1–22. https://​doi.​org/​10.​1038/​s41598-​024-​79106-7
Aulia N, Budi I (2019) Hate speech detection on Indonesian long text 
documents using machine learning approach. In: ACM interna-
tional conference proceeding series, pp 164–169. https://​doi.​org/​
10.​1145/​33304​82.​33304​91
Beyhan F, Çarık B, Arın İ, Terzioğlu A, Yanikoglu B, Yeniterzi R 
(2022) A Turkish hate speech dataset and detection system. In: 
Proceedings language resources and evaluation conference, no 
June, pp 4177–4185. Accessed 16 Oct 2022. https://​aclan​tholo​
gy.​org/​2022.​lrec-1.​443
Bilal M, Khan A, Jan S, Musa S (2022) Context-aware deep learning 
model for detection of roman Urdu hate speech on social media 
platform. IEEE Access 10(September):121133–121151. https://​
doi.​org/​10.​1109/​ACCESS.​2022.​32163​75
Bretschneider U, Peters R (2017) Detecting offensive statements 
towards foreigners in social media. In: Proceedings of the annual 
Hawaii international conference on system sciences, vol 2017-Jan-
uary, pp 2213–2222. https://​doi.​org/​10.​24251/​hicss.​2017.​268
Canhasi E, Shijaku R (2023) Using Twitter to collect a multi-dialectal 
corpus of Albanian using advanced geotagging and dialect mod-
eling. PLoS ONE 18(11 November):1–30. https://​doi.​org/​10.​1371/​
journ​al.​pone.​02942​84

--- Page 29 ---

Social Network Analysis and Mining (2025) 15:82	
Page 29 of 30 
82
Canhasi E, Shijaku R, Berisha E (2022) Albanian fake news detec-
tion. ACM Trans Asian Low-Resour Lang Inf Process 21(5):1–24. 
https://​doi.​org/​10.​1145/​34872​88
Davidson T, Warmsley D, Macy M, Weber I (2017) Automated hate 
speech detection and the problem of offensive language. In: 11th 
international AAAI conference on web and social media, pp 
512–515. https://​doi.​org/​10.​1609/​icwsm.​v11i1.​14955
Dieber J, Kirrane S (2020) Why model why? Assessing the strengths 
and limitations of LIME. http://​arxiv.​org/​abs/​2012.​00093
Fetahi E, Hamiti M, Susuri A, Ajdari J, Zenuni X (2024) AI-based 
hate speech detection in Albanian social media: new dataset and 
mobile web application integration. Int J Interact Mob Technol 
18(24):190–208. https://​doi.​org/​10.​3991/​ijim.​v18i24.​50851
Fetahi E, Hamiti M, Susuri A, Shehu V, Besimi A (2023) Auto-
matic hate speech detection using natural language processing: 
a state-of-the-art literature review. In: 2023 12th Mediterranean 
conference on embedded computing (MECO), pp 1–6. https://​
doi.​org/​10.​1109/​MECO5​8584.​2023.​10155​070
Fetahi E, Hamiti M, Susuri A, Zenuni X, Ajdari J, Macedonia N 
(2024) Integrating handcrafted features with machine learning 
for hate speech detection in Albanian, vol 19, no 2, pp 80–92. 
https://​doi.​org/​10.​2478/​seeur-​2024-​0025
Founta AM et al (2018) Large scale crowdsourcing and characteri-
zation of twitter abusive behavior. In: 12th international AAAI 
conference on web and social media, ICWSM 2018, pp 491–
500. https://​doi.​org/​10.​1609/​icwsm.​v12i1.​14991
García-Díaz JA, Cánovas-García M, Colomo-Palacios R, Valencia-
García R (2021) Detecting misogyny in Spanish tweets. An 
approach based on linguistics features and word embeddings. 
Future Gener Comput Syst 114:506–518. https://​doi.​org/​10.​
1016/j.​future.​2020.​08.​032
Gencoglu O (2021) Cyberbullying detection with fairness con-
straints. IEEE Intern Comput 25(1):20–29. https://​doi.​org/​10.​
1109/​MIC.​2020.​30324​61
Gentian Sala (2019) Gjuha E Urrejtjes Në Mediat Audiovizive
Gitari ND, Zuping Z, Damien H, Long J (2015) A lexicon-based 
approach for hate speech detection. Int J Multimed Ubiq Eng 
10(4):215–230. https://​doi.​org/​10.​14257/​ijmue.​2015.​10.4.​21
Gwet KL (2021) Large-sample variance of Fleiss generalized kappa. 
Educ Psychol Meas 81(4):781–790. https://​doi.​org/​10.​1177/​
00131​64420​973080
Hallakate (2020) Online users in Kosovo by age. https://​halla​kate.​
com/​en/​online-​users-​in-​kosovo-​by-​age/
Holzinger A, Saranti A, Molnar C, Biecek P, Samek W (2022) 
Explainable AI methods —a brief overview. In: Lecture 
notes in computer science (including subseries lecture notes 
in artificial intelligence and lecture notes in bioinformatics), 
vol 13200 LNAI, 2022, pp 13–38. https://​doi.​org/​10.​1007/​
978-3-​031-​04083-2_2
Joshi R, Karnavat R, Jirapure K, Joshi R (2021) Evaluation of deep 
learning models for hostility detection in Hindi text. In: 2021 
6th international conference for convergence in technology, 
I2CT 2021, pp 1–5. https://​doi.​org/​10.​1109/​I2CT5​1068.​2021.​
94180​73
Kastrati Z, Ahmedi L, Kurti A, Kadriu F, Murtezaj D, Gashi F (2021) 
A deep learning sentiment analyser for social media comments in 
low-resource languages. Electron 10(10):1133. https://​doi.​org/​10.​
3390/​elect​ronic​s1010​1133
Ketsbaia L, Issac B, Chen X (2020) Detection of hate tweets using 
machine learning and deep learning. In: Proceedings of the 2020 
IEEE 19th international conference on trust, security and privacy 
in computing and communications, TrustCom 2020, pp 751–758. 
https://​doi.​org/​10.​1109/​Trust​Com50​675.​2020.​00103
Khan S et al (2022) HCovBi-caps: hate speech detection using con-
volutional and bi-directional gated recurrent unit with capsule 
network. IEEE Access 10:7881–7894. https://​doi.​org/​10.​1109/​
ACCESS.​2022.​31437​99
Lundberg SM, Lee SI (2017) A unified approach to interpreting model 
predictions. Adv Neural Inf Process Syst 2017(2):4766–4775
Malik JS, Qiao H, Pang G, van den Hengel A (2022) Deep learning for 
hate speech detection: a comparative study, pp 1–18. http://​arxiv.​
org/​abs/​2202.​09517
Marreddy M, Oota SR, Vakada LS, Chinni VC, Mamidi R (2022) 
Multi-task text classification using graph convolutional networks 
for large-scale low resource language. In: 2022 international joint 
conference on neural networks (IJCNN), pp 1–8. https://​doi.​org/​
10.​1109/​ijcnn​55064.​2022.​98921​05
Mazari AC, Boudoukhani N, Djeffal A (2024) BERT-based ensemble 
learning for multi-aspect hate speech detection. Clust Comput 
27(1):325–339. https://​doi.​org/​10.​1007/​s10586-​022-​03956-x
Mehmood A et al (2022) Threatening URDU language detection from 
tweets using machine learning. Appl Sci. https://​doi.​org/​10.​3390/​
app12​20103​42
Meta (2022) The challenge of detecting hate speech. https://​trans​paren​
cy.​meta.​com/​enfor​cement/​detec​ting-​viola​tions/​chall​enge-​of-​detec​
ting-​hate-​speech
Misini A, Kadriu A, Canhasi E (2022) A survey on authorship analysis 
tasks and techniques. SEEU Rev 17(2):153–167. https://​doi.​org/​
10.​2478/​seeur-​2022-​0100
Misini A, Canhasi E, Kadriu A, Fetahi E (2024) Automatic author-
ship attribution in Albanian texts. PLoS ONE 19(10):e0310057. 
https://​doi.​org/​10.​1371/​journ​al.​pone.​03100​57
Mohammadi S, Chapon M (2020) Investigating the performance of 
fine-tuned text classification models based-on Bert. In: Proceed-
ings of the 2020 IEEE 22nd international conference on high 
performance computing and communications, IEEE 18th inter-
national conference on smart city and IEEE 6th international con-
ference on data science and systems, HPCC-SmartCity-DSS 2020, 
pp 1252–1257. https://​doi.​org/​10.​1109/​HPCC-​Smart​City-​DSS50​
907.​2020.​00162
Moons F, Vandervieren E (2023) Measuring agreement among several 
raters classifying subjects into one-or-more (hierarchical) nominal 
categories. A generalisation of Fleiss’ kappa. http://​arxiv.​org/​abs/​
2303.​12502
Mozafari M, Farahbakhsh R, Crespi N (2020) Hate speech detection 
and racial bias mitigation in social media based on BERT model. 
PLoS ONE 15(8 August):1–26. https://​doi.​org/​10.​1371/​journ​al.​
pone.​02378​61
Mubarak H, Hassan S, Chowdhury SA (2023) Emojis as anchors to 
detect Arabic offensive language and hate speech. Nat Lang Eng 
29(6):1436–1457. https://​doi.​org/​10.​1017/​S1351​32492​30004​02
Nurce E, Keci J, Derczynski L (2022) Detecting abusive Albanian. 
arXiv Preprint http://​arxiv.​org/​abs/​2107.​13592
Pamungkas EW, Basile V, Patti V (2021) A joint learning approach 
with knowledge injection for zero-shot cross-lingual hate speech 
detection. Inf Process Manag 58(4):102544. https://​doi.​org/​10.​
1016/j.​ipm.​2021.​102544
Parker S, Ruths D (2023) Is hate speech detection the solution the 
world wants? Proc Natl Acad Sci. https://​doi.​org/​10.​1073/​pnas.​
22093​84120
Plaza-Del-Arco FM, Molina-González MD, Ureña-López LA, Mar-
tín-Valdivia MT (2020) Detecting misogyny and xenophobia in 
Spanish tweets using language technologies. ACM Trans Intern 
Technol 20(2):1–19. https://​doi.​org/​10.​1145/​33698​69
Poletto F, Basile V, Sanguinetti M, Bosco C, Patti V (2021) Resources 
and benchmark corpora for hate speech detection: a systematic 
review. Lang Resour Eval 55(2):477–523. https://​doi.​org/​10.​1007/​
s10579-​020-​09502-8
Putra CD, Wang HC (2024) Advanced BERT-CNN for hate speech 
detection. Procedia Comput Sci 234:239–246. https://​doi.​org/​10.​
1016/j.​procs.​2024.​02.​170

--- Page 30 ---

	
Social Network Analysis and Mining (2025) 15:82
82 
Page 30 of 30
Ramos G et al (2024) Leveraging transfer learning for hate speech 
detection in Portuguese social media posts. IEEE Access 
12(July):101374–101389. https://​doi.​org/​10.​1109/​ACCESS.​2024.​
34308​48
Ranasinghe T, Zampieri M (2022) Multilingual offensive language 
identification for low-resource languages. ACM Trans Asian 
Low-Resour Lang Inf Process 21(1):1–13. https://​doi.​org/​10.​
1145/​34576​10
Ranasinghe T et  al (2024) SOLD: Sinhala offensive language 
dataset, vol 59, no 1. Springer. https://​doi.​org/​10.​1007/​
s10579-​024-​09723-1
Raza Ur Rehman HM, Saleem M, Jhandir MZ, Alvarado ES, Garay H, 
Ashraf I (2025) Detecting hate in diversity: a survey of multilin-
gual code-mixed image and video analysis. J Big Data. https://​doi.​
org/​10.​1186/​s40537-​025-​01167-w
Romim N, Ahmed M, Talukder H, Saiful Islam M (2021) Hate speech 
detection in the Bengali language: a dataset and its baseline evalu-
ation, pp 457–468. https://​doi.​org/​10.​1007/​978-​981-​16-​0586-4_​37
Roy PK, Tripathy AK, Das TK, Gao XZ (2020) A framework for hate 
speech detection using deep convolutional neural network. IEEE 
Access 8:204951–204962. https://​doi.​org/​10.​1109/​ACCESS.​2020.​
30370​73
Sandaruwan HMST, Lorensuhewa SAS, Kalyani MAL (2019) Sin-
hala hate speech detection in social media using text mining and 
machine learning. In: 19th international conference on advances 
in ICT for emerging regions, ICTer 2019—proceedings, pp 1–8. 
https://​doi.​org/​10.​1109/​ICTer​48817.​2019.​90236​55
Shala F, Beqiraj X (2020) The use of contracted forms of Albanian 
language in electronic media texts. Prizren Soc Sci J 4(3):47–51. 
https://​doi.​org/​10.​32936/​pssj.​v4i3.​182
Solovev K, Pröllochs N (2022) Hate speech in the political discourse 
on social media: disparities across parties, gender, and ethnicity, 
vol 1, no 1. Association for Computing Machinery. https://​doi.​org/​
10.​1145/​34854​47.​35122​61
Tolba M, Ouadfel S, Meshoul S (2021) Hybrid ensemble approaches 
to online harassment detection in highly imbalanced data. Expert 
Syst Appl 175(2):114751. https://​doi.​org/​10.​1016/j.​eswa.​2021.​
114751
Valkenburg PM (2022) Social media use and well-being: what we know 
and what we need to know. Curr Opin Psychol 45:101294. https://​
doi.​org/​10.​1016/j.​copsyc.​2021.​12.​006
Vanetik N, Mimoun E (2022) Detection of racist language in French 
tweets. Information 13(7):76. https://​doi.​org/​10.​3390/​info1​30703​
18
Watanabe H, Bouazizi M, Ohtsuki T (2018) Hate speech on Twitter: a 
pragmatic approach to collect hateful and offensive expressions 
and perform hate speech detection. IEEE Access 6:13825–13835. 
https://​doi.​org/​10.​1109/​ACCESS.​2018.​28063​94
X (former Twitter), “HateLab,” (2025) https://​devel​oper.x.​com/​en/​blog/​
succe​ss-​stori​es/​hatel​ab
Yin W, Zubiaga A (2021) Towards generalisable hate speech detection: 
a review on obstacles and solutions. PeerJ Comput Sci 7:1–38. 
https://​doi.​org/​10.​7717/​PEERJ-​CS.​598
Zampieri M, Malmasi S, Nakov P, Rosenthal S, Farra N, Kumar R 
(2019) SemEval-2019 task 6: identifying and categorizing offen-
sive language in social media (OffensEval). In: Proceedings of the 
13th international workshop on semantic evaluation, pp 75–86. 
https://​doi.​org/​10.​18653/​v1/​S19-​2010
Publisher's Note  Springer Nature remains neutral with regard to 
jurisdictional claims in published maps and institutional affiliations.

```
