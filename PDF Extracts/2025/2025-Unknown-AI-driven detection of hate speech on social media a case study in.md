---
title: "2025-Chared-AI-driven detection of hate speech on social media a case study in - PDF Extract"
source_pdf: "2025-Chared-AI-driven detection of hate speech on social media a case study in.pdf"
pages: 19
extracted_at: "2026-02-13T14:50:55.852383"
---

# PDF Extract: 2025-Chared-AI-driven detection of hate speech on social media a case study in

**Source PDF:** 2025-Chared-AI-driven detection of hate speech on social media a case study in.pdf
**Total Pages:** 19

---

## Content

```
--- Page 1 ---

Cluster Computing (2025) 28:811
https://doi.org/10.1007/s10586-025-05553-0
1  Introduction
As we navigate the digital era, social media platforms have 
revolutionized how we connect and communicate [11]. This 
new virtual environment offers unprecedented opportunities 
for creativity and participation. However, it also presents 
unique challenges, such as the spread of HS, which threat­
ens to disrupt the inclusive and respectful dialogue essential 
to our online communities. In this paper, the introduction 
has been divided into different sections.
1.1  The expansion of HS in the online world
The proliferation of social networks has fundamentally 
transformed the way people communicate and interact 
globally. Platforms such as X, Facebook, and Instagram 
have become essential components of our daily lives, pro­
viding spaces for expression, connection, and information 
sharing [15]. However, the rise of social media has also 
brought about significant challenges, including the spread 
of HS. HS, defined as any communication that belittles or 
	
 Ehtesham Hashmi
hashmi.ehtesham@ntnu.no
Zahim Chared
zahim.chared@ecole.ensicaen.fr
Clément Jantet
clement.jantet@ecole.ensicaen.fr
Calliste Ravix
calliste.ravix@ecole.ensicaen.fr
Robin Salmi
robin.salmi@ecole.ensicaen.fr
Sule Yildirim Yayilgan
sule.yildirim@ntnu.no
1	
ENSICaen, 6 boulevard Maréchal Juin, Caen 14000, 
Normandie, France
2	
Department of Information Security and Communication 
Technology, NTNU, Teknologiveien 22, Gjøvik 2815, 
Innlandet, Norway
Abstract
In today’s digital age, the rise of online hate speech–fueled by user anonymity and widespread use of platforms like X–
has become a serious issue. It is a challenge for both social media companies and authorities in their efforts to maintain 
a safe and respectful online environment. Hate speech (HS) is mostly seen as an intentional act of aggressive behavior 
towards anyone based on their personal traits. The main corpus of research work done in this area concerns the main 
spoken languages in the world, such as English, Arabic, or Hindi. However, in the circle of European languages, HS in 
the French language needs more development. Throughout this study, we present our contribution to the area by compil­
ing and preprocessing a custom dataset by merging and cleaning existing French HS corpora. We develop binary-class 
Machine Learning (SVM, Random Forest, Naive Bayes, Logistic Regression), Deep Learning (LSTM, Bi-LSTM, GRU), 
and Transformers models (CamemBert, DistilCamemBert, DeHateBert). Experimental results show that DistilCamemBert 
significantly outperforms other models, achieving an F1-score of 80%. Then we compare our results to the existing state-
of-the-art online. After that, we try to take a step further in the research with the implementation of interpretability studies 
with explainable AI and bias mitigation.
Keywords  Hate speech · French language · Machine learning · Deep learning · Natural language processing · 
Transformers · Explainable artificial intelligence · Bias analysis
Received: 6 September 2024 / Revised: 11 May 2025 / Accepted: 2 June 2025 / Published online: 17 September 2025
© The Author(s) 2025
AI-driven detection of hate speech on social media: a case study in the 
French language
Zahim Chared1 · Clément Jantet1 · Calliste Ravix1 · Robin Salmi1 · Ehtesham Hashmi2 · Sule Yildirim Yayilgan2
1 3

--- Page 2 ---

Cluster Computing (2025) 28:811
discriminates against individuals based on attributes such 
as race, religion, gender, sexual orientation, or ethnicity, 
poses serious social and psychological threats [8, 13]. It can 
incite violence, perpetuate discrimination, and foster divi­
siveness within communities. Since the large deployment of 
the Internet, users have used anonymity to feel free to write 
about the whole world’s atrocities.
HS is a social issue that must be addressed in order to 
have a peaceful space on the Internet. However, it is not as 
simple as previously mentioned. The Internet became par­
ticipative with the explosion of social networks. It is a new 
way to express our freedom of speech and opinion sharing 
without prior control. Sadly, any user has witnessed rude 
manners online: the effect of online disinhibition is shown 
by Suler, [25], Kastrati et al. [18]. In 2024, the exponential 
multiplication of online messages has led to difficulties in 
mitigating them, and policies have asked social media plat­
forms to delete these messages.
1.2  The legal aspect of HS and its impact on 
individuals
HS is subject to various legal frameworks depending on the 
jurisdiction. In France, the law defines HS as incitement or 
provocation to hatred, whether private or public, toward 
individuals or groups based on their skin color, origin, reli­
gion, sex, sexual orientation, gender identity, or disability 
[9]. The law specifically addresses several types of content, 
including an apology for crimes against humanity, denial 
or minimization of crimes against humanity, an apology for 
terrorism, and incitement to racial hatred1. The issue here is 
a simple universal definition of HS. In France, HS is divided 
into different legal classes where any content could cause 
a person to feel hateful toward another. Let us take a look 
at the definition given by the United Nations:"any type of 
communication, oral or written, or behavior, constituting 
an offense or using derogatory or discriminatory language 
concerning a person or group because of their identity, in 
other words, religious affiliation, ethnic origin, nationality, 
race, skin color, ancestry, gender or other factors constitut­
ing identity"2
In the United States, for example, the main challenge is 
its principle of freedom ([9]) which is a sacred right that can­
not be questioned under any circumstances. One of the main 
challenges in regulating HS is balancing it with the funda­
mental right to freedom of expression. Although democratic 
societies uphold the right to speak freely, it is necessary to 
reconcile this with the prevention of speech that incites vio­
lence or discrimination. HS is different from mere insults 
or discrimination, yet it poses a threat to social harmony 
and public order [12]. The dilemma lies in finding the bal­
ance between protecting individuals from harmful speech 
and avoiding undue restrictions on free speech, which could 
lead to censorship and suppression of minority viewpoints.
The social impact of HS is profound and affects the 
democratic values of equality and freedom. While societies 
should tolerate some shocking or offensive opinions, allow­
ing discriminatory speech can cause public disorder and 
harm targeted groups [14]. The spread of HS, especially on 
social media, makes these issues worse by enabling the fast 
and wide sharing of harmful content. This not only weak­
ens social unity but can also lead to real-world violence and 
discrimination. According to Fig.  1, 67% of respondents 
reported regularly seeing HS content online.3
The deployment of AI-driven HS detection systems raises 
significant privacy concerns. These systems often require 
analyzing large volumes of user-generated content, which 
may inadvertently capture and process private communica­
tions. This poses risks to individuals’ privacy rights and data 
protection, particularly for marginalized groups that may be 
subject to increased surveillance. To mitigate these con­
cerns, platforms must implement robust privacy safeguards, 
including data minimization, user data anonymization, and 
transparent data collection practices. Ensuring compliance 
with privacy laws and regulations is essential to protecting 
user privacy while effectively combating HS.
1  ​h​t​t​p​s​:​/​/​w​w​w​.​s​e​r​v​i​c​e​-​p​u​b​l​i​c​.​f​r​/​p​a​r​t​i​c​u​l​i​e​r​s​/​v​o​s​d​r​o​i​t​s​/​F​3​2​5​7​5
2  ​h​t​t​p​s​:​/​/​w​w​w​.​u​n​.​o​r​g​/​f​r​/​h​a​t​e​-​s​p​e​e​c​h​/​u​n​d​e​r​s​t​a​n​d​i​n​g​-​h​a​t​e​-​s​p​e​e​c​h​/​w​h​a​
t​-​i​s​-​h​a​t​e​-​s​p​e​e​c​h
3  ​h​t​t​p​s​:​/​/​f​r​.​s​t​a​t​i​s​t​a​.​c​o​m​/​i​n​f​o​g​r​a​p​h​i​e​/​3​1​7​7​7​/​d​i​s​c​o​u​r​s​-​h​a​i​n​e​u​x​-​c​o​n​t​r​e​-​l​e​
s​-​m​i​n​o​r​i​t​e​s​-​r​e​s​e​a​u​x​-​s​o​c​i​a​u​x​/
Fig. 1  Most Frequent Target Groups on Social Media (e.g., LGBTIQ, 
Ethnic Minorities, Women, etc.)
 
1 3
811 
Page 2 of 19

--- Page 3 ---

Cluster Computing (2025) 28:811
Moreover, AI’s final decision on whether a tweet is hate­
ful can impact the sensitivities of the affected group. The 
classification of content as HS may be highly contested by 
both victims and those accused of harassment. Therefore, it 
is crucial to ensure that AI-driven decisions are as fair and 
unbiased as possible, reducing the risk of misclassification 
and promoting transparency in content moderation.
1.3  Work contributions
Addressing the spread of HS on social networks is cru­
cial to ensuring safer and more inclusive online environ­
ments. Although significant progress has been made in the 
development of automated systems for the detection of HS 
in languages such as English, there is a significant gap in 
resources and tools for other languages, including French. 
The linguistic and cultural nuances of the French language 
present unique challenges in developing effective HS detec­
tion systems. This gap highlights the need for specialized 
research focused on non-English contexts to ensure compre­
hensive and equitable solutions.
The objective of this research is to develop a robust Arti­
ficial Intelligence (AI) system capable of accurately detect­
ing HS in French on social media platforms. Our approach 
includes the creation of a custom French-language dataset 
and the development of various Machine Learning (ML), 
Deep Learning (DL), and transformer models to address the 
specific challenges associated with this language. We also 
emphasize the importance of transparency and explainabil­
ity in AI systems, integrating explainable AI techniques to 
provide clear insights into the decision-making processes of 
our models.
The main contributions to French HS detection are as 
follows: 
1.	 First, the improvement of the HS detection methodol­
ogy. From the standard process, this paper tries to show 
possible upgrades for the detection of Hateful written 
content in the French language. We work with a more 
effective tool for text pre-processing from Hoareau, 
[16]4. Then, we study and compare different word 
embedding techniques from the state of the art to find 
a better one or find a way for enhancement. Finally, we 
analyze various French HS datasets, which will be pre­
sented in the related works. Based on their specific char­
acteristics, we construct our own dataset for this study, 
aiming to minimize bias as much as possible.
2.	 Then, we implement state-of-the-art machine learning 
(ML), deep learning (DL), and French transformer-
based models, such as CamemBERT, for HS detection. 
4  Here is the github link: ​h​t​t​p​s​:​/​/​g​i​t​h​u​b​.​c​o​m​/​a​n​a​i​s​h​o​a​r​e​a​u​/​f​r​e​n​c​h​_​p​r​
e​p​r​o​c​e​s​s​i​n​g
While these techniques have been previously explored 
for French HS detection, our goal is to optimize the 
parameters to surpass the performance of prior studies.
This paper reports on our study’s methodology and findings, 
detailing the processes of data collection, preprocessing, 
model development, and evaluation. Additionally, since the 
team is composed of four student engineers from France, we 
present an application designed to utilize our AI models for 
practical HS detection, demonstrating our work’s real-world 
applicability and impact. Our findings contribute to the ongo­
ing efforts to mitigate HS online, highlighting the potential 
for AI to enhance digital safety and promote positive online 
interactions within French-speaking communities.
1.4  Structure of the paper
To summarize, this paper is organized as follows. Section 
2 presents the state of the art, including existing works on 
French and general HS detection. Section 3 outlines the 
methodology used in this study. Section 4 presents our 
results, compares them with previous work, and provides 
an analytical discussion. Section 5 describes the develop­
ment of our application. Finally, Sect. 6 concludes the paper, 
highlighting limitations and offering recommendations for 
future work.
2  Related works
The detection of HS on social media has garnered signifi­
cant attention from researchers due to its critical role in 
maintaining safe and inclusive online environments. Various 
methodologies have been proposed, leveraging advance­
ments in Natural Language Processing (NLP), machine 
learning (ML), and deep learning (DL) models. This section 
provides an overview of the current state of HS detection 
research, highlighting key studies, techniques, and ongoing 
challenges in the field.
2.1  ML based approaches
Bedjatiya et al. [5] explored HS and offensive content iden­
tification in Indo-European languages using traditional ML 
techniques. The authors demonstrated the effectiveness 
of such methods across multiple languages, emphasizing 
the role of manually crafted features in achieving reason­
able accuracy. However, these approaches have significant 
limitations, particularly their inability to capture contex­
tual nuances and long-term dependencies in text, which 
are crucial for accurate HS detection. Early approaches to 
HS detection predominantly relied on traditional machine 
1 3
Page 3 of 19 
811

--- Page 4 ---

Cluster Computing (2025) 28:811
Networks (RNNs), including Long Short-Term Memory 
(LSTM) networks, have been particularly effective. More 
recently, BERT-based models have shown significant 
improvements, particularly in high-resource settings, due 
to their ability to capture contextual nuances of language. 
Multilingual HS detection is a burgeoning area of research. 
Aluru et al. [3] conducted a comprehensive analysis over 
nine languages, highlighting the challenges and effective­
ness of various models in low-resource settings. They 
found that while simple models like LASER embeddings 
with logistic regression performed well in low-resource 
contexts, BERT-based models were superior for large data 
cases. Their work also demonstrated that translating non-
English data to English and then applying BERT could yield 
competitive results. For our French monolingual case, they 
described low-resource LASER + LR and Translation + 
BERT as the best models to use.
Chiril et al. [7] developed a corpus for sexism detection 
in French Tweets. They contributed to the construction of 
a new 12k tweet dataset for sexism detection. The authors 
also presented preliminary results of sexism detection using 
DL-based methods, which show promising results. The 
authors distinguished between different types of sexist con­
tent based on speech act theory, distinguishing direct sexist 
HS, descriptive claims about women, and reported experi­
ences of sexism. The study conducted experiments using 
both standard feature-based and DL-based approaches with 
contextualised and non-contextualised embeddings. The 
results were encouraging and represented a new state of 
the art for sexism detection in French. They used different 
ML-based models such as SVM, including both traditional 
feature-based methods and DL-based techniques such as 
CNN, CNN-LSTM and Bi-LSTM. The experiments aimed 
to evaluate the effectiveness of these models in detecting 
sexist content in tweets. Nevertheless, BERT transformers 
achieved the best f-score of 0.762. These studies, among 
others, provided a solid basis for the automated detection of 
HS in French and highlighted the challenges and opportuni­
ties for improving (NLP) models in this domain.
Ousidhoum et al. [21] presented a comprehensive analy­
sis using a multilingual and multi-aspect dataset, addressing 
HS in English, French, and Arabic. Their work highlights the 
importance of considering different types of HS, including 
direct and indirect hate and examining the target attributes 
and group identities associated with HS. This approach 
allows for a nuanced understanding of the dynamics of HS 
across languages and cultures. The authors collected and 
annotated a dataset of tweets in English, French, and Ara­
bic. The annotation process involved labelling tweets based 
on the directness of speech, hostility type, discriminative 
target attribute, target group, and annotator sentiment. The 
MLMA dataset is designed as a comprehensive resource for 
learning (ML)-based methods, where features were manu­
ally engineered and fed into classifiers such as Support Vec­
tor Machines (SVMs), Decision Trees, and Naive Bayes. 
These models often utilized n-grams and Term Frequency-
Inverse Document Frequency (TF-IDF) as features to repre­
sent textual data. Adoum et al. [1] worked on the detection 
of HS with a mix of local Chadian and French languages. 
They built a dataset of 14k posts and comments of Chad­
ians on Facebook for a multi-label classification. After data 
cleaning and preprocessing with NLP, they studied three 
feature extractions: Word2Vec, Doc2Vec, and FastText, and 
compared each other. They used ML classification models 
such as Logistics Regression (LR), SVM, Random Forest 
(RF), and K-Nearest Neighbours (KNN) for supervised 
classification. In the end, FastText + SVM obtained the best 
results with an F1-score of 0.954 for the Insult class label 
and 0.939 for Hate.
Vanetik et al. [27] introduced a new dataset called FTR 
(French Twitter Racist) for the detection of racist content. 
They evaluated this dataset with supervised models such as 
LR, RF, and Extreme Gradient Boosting (XGB) with dif­
ferent word representations like TF-IDF, n-gram, and Bert 
sentence embeddings. After an extension experiment with 
general French HS and cross-lingual evaluation, their FTR 
dataset alone showed an F1-score of 0.757 with LR with 
Bert sentence embedding. Alhazmi et al. [2] compared dif­
ferent ML feature extraction techniques for HS in Arabic 
and code-mixing. From the creation of a large corpus and 
a Hybrid-Annotation application approach, they analyzed 
different ML algorithms with different feature extraction 
and obtained a 98.21% accuracy with Stochastic Gradient 
Descent (SGD) with TF-IDF.
Despite their early successes, traditional machine learn­
ing (ML) methods faced significant limitations. The most 
notable among these was their inability to understand 
contextual aspects when dealing with HS. Additionally, 
traditional models struggled with the"long tail"problem, 
performing poorly on infrequent or complex cases of HS 
that did not conform to common patterns observed in train­
ing data. Moreover, these models were limited by their 
reliance on large-scale annotated datasets, which are often 
difficult and expensive to curate. The need for extensive 
manual annotation to capture the vast array of linguistic 
variations in HS remains a major bottleneck in scaling these 
approaches.
2.2  DL based approaches
Recent advancements have shifted towards DL-based tech­
niques, which have shown superior performances due to 
their ability to capture complex linguistic patterns. Con­
volutional Neural Networks (CNNs) and Recurrent Neural 
1 3
811 
Page 4 of 19

--- Page 5 ---

Cluster Computing (2025) 28:811
Floyd and shows that the CamemBERT model gives the 
best results in their experiments. Another significant contri­
bution comes from a group of researchers who developed a 
framework for annotating and detecting HS in French using 
the Yandex Toloka crowdsourcing platform. This frame­
work led to the creation of a dataset of 5,000 annotated 
tweets, which facilitated the training of French-specific HS 
detection models. Their experiments show that integrating 
multilingual BERT and CamemBERT models with custom 
aggregation methods significantly improves detection accu­
racy. From MLMA [21] and CONAN [6] datasets merged, 
they build a mBERT and an XLM-RoBERTa for classifica­
tion while optimizing the parameters. It is showed the best 
model is mBERT with 10 epochs and a learning rate of 3e-4.
2.4  Challenges and limitations
Despite significant progress, several challenges remain in 
the field of HS detection. A key issue is the ambiguity and 
subjectivity inherent in HS. Differentiating between offen­
sive language and HS requires a nuanced understanding, 
often influenced by cultural and contextual factors. This 
complexity can lead to both false positives and false nega­
tives, reducing the reliability of detection systems.
Another challenge is the imbalance and bias in datasets. 
Many HS datasets are biased, containing disproportionately 
more non-hate than hate cases. This imbalance can bias 
models and affect their performance. Furthermore, models 
trained on biased datasets may inadvertently reinforce exist­
ing prejudices.
Language diversity is also a challenge. The majority of 
work on multilingual HS detection is in French. Most HS 
detection research has focused on English, with relatively 
few resources available for other languages. The unique 
syntactic and semantic characteristics of different languages 
require tailor-made approaches and datasets, making the 
development of universal detection systems difficult.
2.5  Positioning of the current research
Our research addresses several gaps identified in existing 
studies. By focusing on HS detection in French, we contrib­
ute to the relatively under-researched area of non-English 
HS detection. We developed a custom French-language 
dataset, taking into account the scarcity of resources for this 
language. In addition, our approach incorporates explicable 
AI techniques, increasing the transparency and interpret­
ability of our models. This aspect is crucial for building trust 
and understanding in automated systems, especially in sen­
sitive applications such as HS detection. By integrating dif­
ferent ML-based models and evaluating their performance, 
we aim to identify the most effective techniques for French 
analyzing HS in a multilingual context. The study uses sev­
eral ML-based models to evaluate the dataset. Traditional 
baselines include Logistic Regression (LR) with Bag-of-
Words (BOW) features. In addition, DL-based models such 
as Bi-LSTM networks and Sluice networks, which are par­
ticularly suitable for multitask learning with loosely related 
tasks, are used. The models will be tested in different config­
urations: Single Task Single Language (STSL), Single Task 
Multilingual (STML) and Multitask Multilingual (MTML). 
Five classification tasks are reported: directness of speech, 
hostility type, discriminative target attribute, target group, 
and annotator sentiment.
The results showed that DL-based models generally 
outperformed traditional BOW-based models. In particu­
lar, multilingual multitask learning models performed bet­
ter on tasks with less annotated data, indicating the benefit 
of sharing information across languages and tasks. In the 
context of French language HS detection, research has pri­
marily focused on racist and abusive messages. Chiril et 
al. [7] introduced a new French dataset for sexism detec­
tion, addressing the gap in multilingual HS detection. Their 
work combines traditional feature-based models and neu­
ral approaches to evaluate the effectiveness of multilin­
gual embeddings and cross-lingual training in detecting 
HS against immigrants and women in English and French 
tweets. The study used two corpora: HS-IW, which con­
tains English tweets annotated for HS against immigrants 
and women, and SEXISM, a French dataset of tweets 
annotated for sexist content collected from October 2017 
to May 2018. The authors developed a range of models, 
from feature-based to neural approaches. The basic model 
used unigrams, bigrams and trigrams with TF-IDF, while 
the feature-based models included surface features, senti­
ment features and emoji features, among others. A neural 
model using a bidirectional LSTM with an attention mecha­
nism was also implemented. The experiments focused on 
multi-target detection to evaluate whether HS detection is 
target-dependent, and multilingual detection to test models 
across different languages using multilingual embeddings. 
The results were encouraging, showing good performance 
for both English and French, suggesting the feasibility of 
cross-lingual HS detection.
2.3  Transformers based approaches
Finally, the exponential development of transformer research 
in HS. A noteworthy example is the work by Ayele et al. 
[4], who have deeply investigated the detection of racial HS 
using transfer learning. They used multilingual BERT and 
CamemBERT models, fine-tuning the HateXplain model 
with annotated Twitter data. Their research focuses on 
identifying racist comments following the death of George 
1 3
Page 5 of 19 
811

--- Page 6 ---

Cluster Computing (2025) 28:811
	–
Real Tweets Collection: We used datasets containing 
French tweets. Mancarella et al. [20] Tonneau et al. [26] 
Chiril et al. [7]
	–
Syntactic sentences Generation: We utilized datasets 
containing syntactic sentences. Röttger et al. [22] Ton­
neau et al. [26]
	–
AI-Generated Phrases: Additionally, we generated our 
phrases using AI. For this, we prompted ChatGPT to 
produce sentences containing a maximal set of offensive 
words in French. We then instructed the model to gener­
ate both hateful and non-hateful sentences incorporating 
those words. All generated phrases were meticulously 
reviewed by the authors to ensure accurate labeling and 
to mitigate potential bias
3.1.2  Target annotation and bias mitigation
To assess the fairness (or bias) of the dataset, additional 
variables were introduced. Some of the datasets already 
contained relevant variables, which were utilized accord­
ingly. A"target"variable was specifically added to identify 
the target of hateful sentences. To generate additional vari­
ables, Facebook’s BART model was employed in"zero-
shot"classification mode, enabling its use without the need 
for fine-tuning. Figure 3 shows the distribution of each tar­
get without two targets:
	–
No target: This is the target of each non-hateful 
sentence.
	–
Generic insult: This is the target of each hateful sen­
tence that does not have a specific context so that BART 
could not categorize it.
We try to get distributions as balanced as possible to obtain 
a dataset free of bias, where our models can be trained in 
detecting HS toward any group.
HS detection. Our results will provide valuable insights and 
practical tools for improving online safety in French-speak­
ing communities, contributing to the broader goal of creat­
ing inclusive digital environments.
3  Methodology
The research methodology is the systematic approach in our 
work We have detailed our methodology in Fig. 2, and Table 
1.
3.1  Dataset collection
The first step in developing our HS detection system was 
to create a comprehensive dataset specifically tailored to 
the French language. Recognizing the lack of existing 
resources, we created a custom dataset by collecting real 
tweets and generating synthetic sentences that encapsulate 
different forms of HS.
3.1.1  Data sources
To create the dataset we used a combination of:
Table 1  Some French Datasets available online
Name
Authors
Tweets 
number
Binary or 
multi-label
FTR
Vanetik and 
Mimoun [27]
2856
Binary
MLMA
Ousidhoum 
et al. [21]
4014
Multi-
label
FrenchHateSpeechSuperset
Louis 
Heuveline 
[19]
42660
Binary
Fig. 2  Proposed work methodology overview: from dataset collection to model evaluation
 
1 3
811 
Page 6 of 19

--- Page 7 ---

Cluster Computing (2025) 28:811
3.2  Data preprocessing
After compiling the dataset, we applied several preprocess­
ing steps to clean and standardize the text data:
	–
Special Characters Removal: Eliminated mentions, 
hashtags, and other non-alphabetic characters.
	–
Tokenization: Transformed the text into tokens (lexical 
units).
	–
Grammatical Tagging: Assigned grammatical tags 
(part-of-speech tagging) to the tokens, such as ’nc’ for 
noun, ’v’ for verb.
	–
Simplification: Removed stop words (words with low 
lexical value like ’le’, ’t”, ’dring’) and punctuation.
	–
Lemmatisation: Replaced tokens with their lemma (the 
canonical form of the word, as used in dictionaries).
We utilized the French pre-processing tool described by 
Hoareau, [16] to streamline the preprocessing steps, ensur­
ing consistency and efficiency in the handling of text data.
3.3  Word embedding
In order to classify HS effectively, we needed to convert 
our text data into a numerical form. This process, known 
as vectorization, is essential for the models to understand 
and interpret the text. For vectorization, we chose TF-IDF, 
which takes into account the importance of words in the 
text. This method improves the model’s ability to detect HS. 
Other methods, such as FastText and Word2Vec, are often 
pre-trained on English data, which does not suit our French 
research, making TF-IDF the best choice for our use case. 
The TF-IDF formula is defined as follows:
TF-IDF(t, d) = TF(t, d) × log
(
N
|{d ∈D : t ∈d}|
)
3.1.3  Dataset statistics and examples
Figure 4 and Table 2 show the distribution of hateful or non-
hateful in our dataset. You can see an example of each target 
on Table 3.
Table 2  Dataset description
Number of tweets
Hateful
Non-Hateful
12397
6225
6172
Target
Example of sentence
Translation in English
Transgender
Il n’y a rien de plus horrible qu’un trans.
There’s nothing more horrifying than a 
transsexual
Disability
Les handicapés comme vous sont répugnants
Disabled people like you are disgusting
Gender
Les femmes aux commandes est un danger pour 
notre pays.
Women at the helm is a danger for our 
country.
LGBTIQ
@USER vraiment des manières de pédé je ne 
veux pas être en présence de ce messieur sale 
gauchiste haineux
@USER really faggy manners, I don’t 
want to be in the presence of this hate­
ful leftist.
Religion
Je veux tuer tous les musulmans
I want to kill all the muslims
Race
Je pense que les blacks devraient tous être tués
I think black people should all be killed
Ethnicity
Les réfugiés doivent bien savoir qu’ils sont des 
êtres inférieurs.
Refugees need to know that they are 
inferior beings.
Nationality
non mais laisse le ce gros mongol il va tweeter 
un complot de l uefa pro catalan dans 5min
No but let the this big Mongolian he 
will tweet a plot of the uefa pro catalan 
in 5min
Table 3  Sample of the dataset 
with different target
 
Fig. 4  Distribution of HS vs. non-hateful phrases in the dataset
 
Fig. 3  Distribution of target groups in the dataset (e.g. Gender, Race, 
Religion, etc.)
 
1 3
Page 7 of 19 
811

--- Page 8 ---

Cluster Computing (2025) 28:811
Logistic Regression, and Random Forest are known for 
their robustness and efficiency in text classification tasks, 
particularly when combined with TF-IDF vectorization. 
They serve as solid baselines to assess the performance of 
more complex architectures. Deep Learning models, includ­
ing LSTM, Bi-LSTM, and GRU, were chosen for their abil­
ity to capture sequential and contextual patterns in text, 
which are crucial in HS classification. Finally, we included 
Transformer-based models (CamemBERT, DistilCamem­
BERT, DeHateBERT) due to their state-of-the-art results 
in Natural Language Processing tasks, and their particular 
effectiveness in managing nuanced, context-dependent lin­
guistic expressions.
3.4.1  Machine learning models and techniques
We used several ML-based models to classify the text data 
into hateful and non-hateful categories. The models were 
chosen for their effectiveness in text classification tasks, 
particularly in handling the nuances of natural language:
	–
SVM: Utilizes hyperplanes to separate data points in the 
feature space. This model showed the highest accuracy 
in our evaluations. Support Vector Machines (SVM) are 
a type of supervised learning model used for classifi­
cation tasks. The SVM aims to find a hyperplane that 
maximizes the margin between two classes. The optimi­
zation problem for SVM is given by Eq. (1). The con­
straints for this optimization are specified in Eq. (2): 
min 1
2∥w∥2 + C
N
∑
i=1
ξi
(1)
 subject to: 
yi(w⊤xi + b) ≥1 −ξi
(2)
 where w is the weight vector, ξi are slack variables, C is the 
regularization parameter, yi are class labels, xi are feature 
vectors, and b is the bias term.
	–
Logistic Regression: Predicts the probability of a bi­
nary outcome based on predictor variables. It performed 
well and offered reliable results.
	–
Random Forest Classifier: An ensemble learning 
method that builds multiple decision trees and merges 
them for better accuracy and stability. Random Forest is 
an ensemble learning method that aggregates the predic­
tions of multiple decision trees. The prediction ˆy from a 
Random Forest is given by Eq. (3): 
where t is the term (word) for which the TF-IDF is calcu­
lated, d is the document in which the term appears, D is the 
set of all documents, N is the total number of documents 
in the set D, TF(t, d) is the frequency of the term t in the 
document d, and |{d ∈D : t ∈d}| is the number of docu­
ments containing the term t.
TF-IDF is a numerical statistic used in text mining and 
information retrieval to assess the importance of a word in 
a document relative to a collection of documents (or cor­
pus). It works by combining two key concepts: term fre­
quency (TF) and inverse document frequency (IDF) [2]. TF 
measures how often a word appears in a single document. 
A higher frequency means the word is more important in 
that specific document. However, some words might appear 
frequently across many documents (like"the"or"is"), so they 
aren’t necessarily important in distinguishing one document 
from another.
This is where IDF comes into play. IDF decreases the 
weight of common words that appear in many documents, 
focusing on words that are more unique to specific docu­
ments. The TF-IDF score is calculated by multiplying TF 
by IDF, giving higher scores to words that are frequent in a 
particular document but rare in the rest of the corpus. This 
method helps identify the most relevant words in a docu­
ment, making it useful for tasks such as keyword extraction, 
document classification, and text classification. The Word­
2Vec formula is defined as follows:
max 1
T
T
∑
t=1
∑
−c≤j≤c,j̸=0
log P(wt+j|wt)
where wt is the target word, wt+j are the context words, c is 
the size of the context window, T is the total number of words 
in the corpus, and P(wt+j|wt) =
exp(vwt+j ·vwt)
∑
w′∈W exp(vw′·vwt) is the 
probability of context word wt+j given the target word wt.
The FastText formula is defined as follows:
w =
∑
g∈Gw
zg
where w is the word vector, Gw is the set of character 
n-grams for word w, and zg is the vector representation of 
the n-gram g.
3.4  Model selection justification
To ensure a comprehensive evaluation of HS detection 
in French, we selected models from three families: tradi­
tional machine learning, deep learning, and transformer-
based approaches. Machine Learning models such as SVM, 
1 3
811 
Page 8 of 19

--- Page 9 ---

Cluster Computing (2025) 28:811
 where ft, it, gt, and ot represent the forget, input, cell, and 
output gates, respectively. The weight matrices are Wf, Wi, 
Wg, and Wo, and the bias terms are bf, bi, bg, and bo.
	–
GRU: Another variant of RNN that simplifies the ar­
chitecture of LSTMs while maintaining performance, 
offering a more efficient training process.
3.4.3  Pre-trained models and transfer learning
To leverage state-of-the-art advancements in NLP, we used 
pre-trained transformer models such as CamemBERT, Dis­
tilCamemBERT and DeHateBert in our experiments. These 
models are based on the self-attention mechanism, which 
allows them to weigh the importance of different words in a 
sentence regardless of where they are in the sentence. This 
is particularly useful for detecting HS, where the impact of a 
word can depend on the whole context. These transformers 
have already been pre-trained on large sets of text, giving 
them strong language representations that can be adjusted to 
suit our specific task.
	–
BERT (Bidirectional Encoder Representations from 
Transformers): A transformer-based model pre-trained 
on large text corpora, which we fine-tuned for HS 
detection.
	–
Hugging Face Models: Utilized pre-trained models 
from Hugging Face, fine-tuning them on our dataset to 
improve accuracy and robustness in detecting HS. Dis­
tilCamemBert, for example, is a distilled version of the 
CamemBERT model, based on the Transformer archi­
tecture. The attention mechanism in the Transformer is 
defined by Eq. (10), and each Transformer layer applies 
the computation described in Eq. (11): 
Attention(Q, K, V) = softmax
(
QK⊤
√dk
)
V

(10)
Ht = TransformerLayer(Ht−1)

(11)
 where Ht is the hidden state at layer t, TransformerLayer 
includes multi-head self-attention and feed-forward layers, 
and dk is the dimension of the key vectors.
3.5  Model training and evaluation
We used the following steps to train and evaluate the models:
	–
Vectorization: Applied TF-IDF to convert text data into 
numerical form, emphasizing the importance of words 
in documents.
ˆy = 1
K
K
∑
k=1
fk(x)
(3)
 where fk(x) is the prediction from the k-th decision tree, 
and K is the total number of trees in the forest.
	–
Naive Bayes: Naïve Bayes is a probabilistic machine 
learning model commonly used for multi-class text clas­
sification due to its efficiency and strong performance 
on high-dimensional data. It assumes that the features 
(words in a document) are conditionally independent 
given the class label, which simplifies computation. 
However, despite its theoretical advantages, the model 
struggled with our dataset, likely due to violations of the 
independence assumption or class imbalances, leading 
to suboptimal predictions.
3.4.2  Deep learning models
In addition to traditional ML-based models, we explored 
different DL-based architectures to improve the perfor­
mance of our HS detection system. We used recurrent archi­
tectures (LSTM, Bi-LSTM and GRU) because they are 
good at modeling sequential data.
	–
LSTM: A type of recurrent neural network (RNN) ca­
pable of learning long-term dependencies, suitable for 
sequence prediction problems.
	–
Bidirectional LSTM: An extension of LSTM that pro­
cesses data in both forward and backward directions, 
providing a more comprehensive understanding of the 
text context. Bi-LSTM networks are a type of recurrent 
neural network that processes sequences in both for­
ward and backward directions. For each time step t, the 
computations in a single LSTM cell are described by the 
equations: 
ft = σ(Wf · [ht−1, xt] + bf)

(4)
it = σ(Wi · [ht−1, xt] + bi)

(5)
gt = tanh(Wg · [ht−1, xt] + bg)

(6)
ot = σ(Wo · [ht−1, xt] + bo)

(7)
ct = ft ⊙ct−1 + it ⊙gt

(8)
ht = ot ⊙tanh(ct)

(9)
1 3
Page 9 of 19 
811

--- Page 10 ---

Cluster Computing (2025) 28:811
predictions, helping users understand the reasoning be­
hind the classification.
By integrating these methods, our research not only advances 
the technical aspects of HS detection but also emphasizes 
ethical considerations, ensuring the system is transparent 
and accountable. This comprehensive approach positions 
our work as a significant contribution to enhancing online 
safety and promoting positive digital interactions.
3.7  Application development
To make the HS detection model accessible and practical, 
we developed an application with the following features:
	–
User Interface: Allows users to input any sentence and 
receive feedback on whether it contains HS.
	–
Model Integration: The application uses trained mod­
els to analyze the input text and provide results for each 
model.
	–
Ensemble Approach: Combines outputs from differ­
ent models to improve reliability, providing a weighted 
global result.
	–
Explainable AI: Integrates explainable AI techniques to 
justify the model’s decisions, highlighting which parts 
of the text contributed to the HS detection.
4  Results and discussion
In this section, we present the performance results of the 
models selected based on the criteria discussed in 3.4. These 
include machine learning, deep learning, and transformer-
based models, each chosen for their ability to handle dif­
ferent aspects of hate speech detection, such as linguistic 
nuance and contextual dependencies.
4.1  Evaluation metrics
Evaluation metrics are essential tools for assessing the 
performance of analysis methods. Several metrics were 
employed to measure the effectiveness of the classifiers. 
In this research, accuracy is the primary performance met­
ric. Nonetheless, additional metrics such as AUC, recall, 
precision, and F1-score were also used to provide a more 
comprehensive evaluation of the proposed approach. These 
metrics allow each model to demonstrate its ability to effec­
tively detect HS. In this phase, the models classify unla­
belled text data (determining whether it belongs to the ’HS’ 
or ’non-HS’ category) using a test dataset. The performance 
of the models is then assessed by calculating the number 
of true negatives (TN), false positives (FP), false negatives 
	–
Model Training
	–
Deep Learning Models (LSTM, Bi-LSTM, and 
GRU): We begin with an embedding layer that 
transforms text into dense vectors (using a vocabu­
lary of 10,000 words and an embedding dimension 
of 100). For the recurrent layers, our LSTM model 
uses two layers (128 and 64 units) with L2 regulari­
sation, dropout (0.3), and batch normalization. The 
Bi-LSTM model uses bidirectional layers with a 
dropout rate of 0.5 and a lower learning rate (5e-
5) with Adam. Similarly, the GRU model employs 
bidirectional GRU layers with dropout (0.4), batch 
normalisation, and L2 regularisation, but with a 
slightly higher learning rate (5e-4). Additionally, 
we use a learning rate scheduler (reducing the rate 
by 0.1 every 10 epochs) and EarlyStopping (with a 
patience of 5 epochs) to ensure steady and efficient 
training.
	–
Pre-trained Transformer Models We train for 
3 epochs with a training and evaluation batch size 
of 16 per device, which balances computational 
efficiency and stability. Warmup steps (set to 500) 
gradually increase the learning rate during the initial 
phase, allowing the model to start training more sta­
bly. We apply a weight decay of 0.01 to make sure 
the model doesn’t become too complex and overfit. 
We also set up logging to record training progress 
every 10 steps and set the evaluation strategy to run 
at the end of each epoch.
	–
Performance Metrics: The models were evaluated us­
ing confusion matrices to understand their accuracy, 
precision, recall, and F1 scores. SVC emerged as the 
best performer with high precision and recall scores.
	–
Training and testing ratio: We used 80% of the dataset 
to train our models and 20% to test them. This ratio was 
chosen to ensure that we have sufficient data for train­
ing while maintaining a representative test set for robust 
evaluation.
3.6  Explainable AI techniques
To ensure transparency and build user trust, we incorporate 
explainable AI methods:
	–
Feature Importance Visualization: Displays the most 
significant features (words or phrases) that influenced 
the model’s decision.
	–
Local 
Interpretable 
Model-agnostic 
Explana­
tions (LIME): Provides explanations for individual 
1 3
811 
Page 10 of 19

--- Page 11 ---

Cluster Computing (2025) 28:811
4.2  Model performance and evaluation
In this section, we present the performance results of vari­
ous ML- and DL-based models trained and tested on our 
custom French dataset for HS detection. The performance 
metrics used to evaluate these models include precision, 
recall and F1 score, as well as confusion matrices to provide 
a detailed understanding of the effectiveness of each model.
4.3  Analysis of the results
4.3.1  Machine learning models
The use of different Ml models for the detection of HSh 
in French has produced mixed results, particularly in terms 
of precision, recall, accuracy, and F1 score. These metrics 
are essential for assessing not only the effectiveness of each 
model in accurately identifying HS but also its efficiency in 
maintaining low rates of false identifications and omissions.
The LR model showed consistent performance, achiev­
ing a score of 0.77 for precision, recall, and F1 score. While 
these results suggest a balanced approach to classification, 
accuracy was also found to be 0.77, indicating room for 
improvement in both specificity and sensitivity. For NB, 
performance was modest, with all metrics, including accu­
racy, at 0.75. The simplicity and speed of this model are off­
set by its basic assumption of feature independence, which 
can be a significant limitation in the context of language 
processing, where contextual and syntactic dependencies 
play a crucial role.
The SVM performed slightly better, with precision and 
F1 score both at 0.78 and recall at 0.77. Accuracy paralleled 
these metrics, suggesting a higher ability to generalize com­
pared to simpler models. However, SVM can still struggle 
with the very large feature spaces typical of text classifica­
tion, potentially limiting its efficiency. RF matched SVM in 
performance, with all metrics at 0.78. The strength of this 
model lies in its ensemble approach, which generally helps 
to reduce overfitting and improve the generalizability of the 
results. Nevertheless, the equal scores across all parameters 
may indicate that the model, although robust, may not fully 
capture the complex patterns of HS, which may include 
nuanced language cues and contextual variations. These 
results suggest that while the selected ML-based models are 
capable of identifying HS to some extent, there is consider­
able room for improvement.
The results of the ML models are quite satisfactory, par­
ticularly the SVM and Random Forest models (Table 4, 
Fig. 5).
(FN) and true positives (TP). These counts are organised 
into a Confusion Matrix, which serves as the basis for sev­
eral evaluation metrics. A brief overview of these metrics is 
given below.
Accuracy measures how well a classifier correctly identi­
fies instances of"Hate"and"Not Hate."It is calculated as the 
ratio of correctly predicted instances to the total number of 
instances, as shown in Eq. 12.
Accuracy =
TP + TN
TP + FP + TN + FN 
(12)
Precision indicates the proportion of correctly predicted 
positive instances relative to the total predicted positive 
instances. It is computed using Eq. 13.
Precision =
TP
TP + FP 
(13)
Recall reflects the proportion of actual positive instances 
(Hate and Not Hate) that were correctly identified by the 
classifier. The formula is provided in Eq. 14.
Recall =
TP
TP + FN 
(14)
The F1 score combines Precision and Recall into a single 
metric that balances both, providing an overall measure of 
performance. It is calculated for a class C, where C can 
represent either"Not Hate"or"Hate,"using the formula in 
Eq. 15.
F1-score = 2 × Precision × Recall
Precision + Recall
(15)
The Receiver Operating Characteristic (ROC) curve visu­
ally plots the true positive rate (TPR) against the false posi­
tive rate (FPR) across different thresholds. The area under 
the ROC curve (AUC) is a metric that quantifies the classi­
fier’s ability to distinguish between classes. This metric is 
particularly useful in binary classification tasks like ours, 
where it helps identify the most effective models.
Table 4  ML based models’ results
Models
Precision
Recall
F1-score
Logistic Regression
0.77
0.77
0.77
Naive Bayes
0.75
0.75
0.75
SVM
0.78
0.77
0.78
Random Forest
0.78
0.78
0.78
1 3
Page 11 of 19 
811

--- Page 12 ---

Cluster Computing (2025) 28:811
unidirectional processing may limit its effectiveness in com­
plex contextual analysis.
DL-based models generally outperformed traditional 
ML-based approaches in understanding the nuances of tex­
tual data due to their advanced sequence processing capa­
bilities. While ML-based models such as SVM and Random 
Forest achieved maximum scores of 0.78, they fall short in 
capturing the sequential and contextual dependencies criti­
cal to text-based analysis, which DL-based models handle 
more effectively. See Fig. 6 highlights the confusion matrix 
for BiLSTM model used in our work.
4.3.3  Transformers models
The results from the transformer-based models in Table 6 
demonstrate superior performance in detecting HS, which 
can be attributed to their advanced architecture capable of 
contextual analysis. DistilCamemBert, a streamlined version 
of the larger CamemBert model, significantly outperformed 
its counterparts, achieving a precision of 0.78, a recall of 
0.81, and an F1 score of 0.80. This suggests that despite its 
reduced size, DistilCamemBert retains much of the effec­
tiveness of the full model while being more efficient. The 
full CamemBert model also showed strong performance, 
with slightly lower recall compared to DistilCamemBert, 
but equal precision and F1-score, underlining its capability 
in context-sensitive text analysis. DeHateBert, specifically 
tailored for HS detection, showed the highest recall at 0.82, 
indicating its effectiveness in identifying relevant cases of 
HS, although with slightly lower precision.
These models use the transformer architecture to analyze 
words in their specific contexts, significantly improving 
their accuracy and applicability in real-world scenarios. The 
trade-off for this increased accuracy and contextual aware­
ness is longer training times compared to more traditional 
ML-based models. The architecture of these models, as 
exemplified by DistilCamemBert, includes layers specifi­
cally designed to handle the nuances of language, allowing 
them to outperform other models in complex text analysis 
tasks. This architectural sophistication is critical for applica­
tions requiring high accuracy and contextual understanding, 
making transformers particularly suited to challenging NLP 
tasks such as HS detection. See Figs. 7, 8 highlights the con­
fusion matrix and the distil camem BERT architecture.
4.3.2  Deep learning models
The performance of DL-based models in detecting HS in 
French varied, as shown in Table 5. The Bi-LSTM model 
was the most effective, with precision, recall, and F1 scores 
around 0.70–0.71, demonstrating its ability to efficiently 
process linguistic context from both past and future input 
directions. The GRU model performed similarly, dem­
onstrating its strength in sequence understanding with 
slightly reduced computational requirements compared 
to Bi-LSTM. In contrast, the basic LSTM model showed 
weaker results with scores around 0.54, suggesting that its 
Table 5  DL based models results
Models
Precision
Recall
F1-score
LSTM
0.54
0.50
0.54
Bi-LSTM
0.70
0.70
0.71
GRU
0.69
0.70
0.69
Table 6  Transformer based models’ results
Models
Precision
Recall
F1-score
CamemBert
0.77
0.78
0.78
DistillCamemBert
0.78
0.81
0.80
DeHateBert
0.76
0.82
0.79
Fig. 6  Bi-LSTM confusion matrix
 
Fig. 5  SVM confusion matrix
 
1 3
811 
Page 12 of 19

--- Page 13 ---

Cluster Computing (2025) 28:811
4.4  Results conclusion
As observed in Fig. 9, machine learning (ML) models, such 
as SVMs and random forests, perform well in general, with 
F1 scores of around 0.78. This shows that they are reliable 
for classifying data into two groups. However, these mod­
els are not very good at capturing the subtle differences in 
HS. However, our transformer-based models (e.g., Distil­
CamemBERT and DeHateBert) performed better. Their 
self-attention mechanisms allowed for a more detailed 
understanding of context, leading to better recall and preci­
sion, which is important when dealing with the subtleties 
of HS. Our DL-based models (LSTM, Bi-LSTM, GRU) 
were expected to excel at sequence learning, but they didn’t 
perform as well as transformers. This was likely due to the 
complexity of the task and limitations in the training data or 
hyperparameter tuning. We also found that mistakes in the 
data were often caused by unclear language or words that 
only apply in certain situations. This shows that we need to 
Fig. 9  Comparison of model performance using TF-IDF across various AI models
 
Fig. 8  Proposed DistilCamemBert architecture
 
Fig. 7  DistillCamemBert confusion matrix
 
1 3
Page 13 of 19 
811

--- Page 14 ---

Cluster Computing (2025) 28:811
5.2  Model integration
The application integrates several ML-based and DL-based 
models, each contributing to the final decision process. The 
models included are:
	–
Logistic Regression
	–
Naive Bayes
	–
Support Vector Machine
	–
Random Forest
	–
Voting Classifier
	–
CamemBert
5.3  Explainable AI
A critical feature of the application is the integration of 
Explainable AI (XAI) techniques, providing users with 
insights into the model’s decision-making process. This 
transparency is achieved through:
	–
Feature Importance Visualization: Highlights the 
most significant words or phrases that influenced the 
model’s decision, helping users understand why certain 
content was flagged as HS.
	–
Local Interpretable Model-agnostic Explanations 
(LIME): Provides explanations for individual predic­
tions, illustrating how specific parts of the text contrib­
uted to the detection of HS.
Local Interpretable Model-Agnostic Explanations (LIME) 
is a method developed to provide a localized understanding 
and assessment of predictions made by any learning algo­
rithm [10]. It offers insights into how a model’s predictions 
correspond to the specific requirements of the task at hand. 
This approach is especially useful in scenarios where grasp­
ing the model’s decision-making process is just as crucial 
as the accuracy of its predictions. The reason LIME is over 
other XAI models is the fact that LIME gives information 
about one specific sentence and gives more credit to a com­
prehensive model’s decision-making [24]. In this study, the 
application shows the results given by the model selected 
and gives the LIME justification showing which words con­
tribute to hateful violence or not.
For example, we implemented LIME on two examples 
from each class: One showing a neutral statement accord­
ing to an optimized SVM model and one showing a hateful 
comment analyzed by DistilCamemBERT.
In the neutral statement shown in Fig. 10, we can clearly 
see the neutral words used every day, such as"acceuillir"(to 
welcome). These words have more weight than words 
that are actually neutral, such as"va"(to go), but which are 
mainly used in insults and racial violence.
make more improvements, including using more data and 
possibly combining different types of models to make the 
best use of each type’s strengths. Some misclassifications 
were due to the use of neutral or context-dependent terms 
(e.g., the word “noir”) which may appear in both benign 
and hateful contexts. Similar findings have been reported 
by Ousidhoum et al. [21], who highlighted the challenges 
of context-sensitive hate speech detection across multiple 
languages.
As seen in Fig. 12, certain non-hateful texts were falsely 
classified due to the presence of commonly flagged terms 
used in a neutral context, a phenomenon also discussed in 
Ousidhoum et al. [21]. Similarly, Explainability techniques 
(LIME) revealed that models often relied heavily on certain 
keywords. As shown in Fig. 11, words like “noir” and “sale” 
skew model predictions even when the broader sentence 
lacked hateful intent. LIME analysis (Fig. 11) confirmed 
prior findings highlight that the model often misclassifies 
based on isolated keyword signals, lacking sufficient con­
textual grounding. Based on the performance of our mod­
els, we developed a practical application for real-time HS 
detection. This application integrates our trained models 
and emphasizes explainability and usability. The next sec­
tion outlines the development and functionalities of the 
application.
5  Application development
To translate our ML- and DL-based models into a practi­
cal tool for HS detection, we developed an application that 
provides real-time analysis and feedback on text input. 
The development process involved integrating the trained 
models into a user-friendly interface to ensure efficient and 
transparent HS detection.
5.1  User interface
The application features an intuitive user interface that 
allows users to input text and receive immediate feedback. 
The key components of the interface include:
	–
Text Input Field: Users can type or paste text into a 
designated input field for analysis.
	–
Analyze Button: Initiates the HS detection process.
	–
Results Display: Provides clear and concise feedback 
on whether the text contains HS, along with a confi­
dence score.
1 3
811 
Page 14 of 19

--- Page 15 ---

Cluster Computing (2025) 28:811
On the other side, the weight of words used a lot in hate dec­
larations is highlighted by LIME for DistilCamemBERT’s 
decision-making shown in Fig. 11. These words have influ­
enced the model to classify the content as hateful because of 
racial context with skin color reference"noir"(black). Words 
like"sale"(dirty) are degrading to the person targeted.
Figure 12 presents an example of a false positive in HS 
detection. This image illustrates a case where the model 
incorrectly classified a non-hateful text as hateful. Such 
misclassifications are important to analyze as they highlight 
the challenges and limitations of automated HS detection 
systems. False positives can be caused by various factors, 
such as the presence of words commonly associated with 
HS used in a different context, sarcasm, or complex linguis­
tic nuances that the model may find difficult to interpret cor­
rectly. In this case, the word ’noir’ is commonly associated 
with racist language.
False negatives represent another critical challenge in 
HS detection systems. These occur when the model fails to 
identify genuinely hateful content, incorrectly classifying it 
as non-hateful. Such misclassifications are particularly con­
cerning as they allow harmful content to go undetected. In 
Fig. 13, we can see that the model doesn’t really understand 
the French insult"va te faire voir". It’s why the text is classi­
fied as a non-hateful text. See Figs. 14 and 15 highlight the 
examples of hateful and non-hateful posts found o twitter.
Fig. 12  Example of a false positive: Non-Hateful text misclassified as 
Hateful
 
Fig. 11  LIME visualization for hateful text
 
Fig. 10  LIME visualization for neutral text
 
1 3
Page 15 of 19 
811

--- Page 16 ---

Cluster Computing (2025) 28:811
educational materials aimed at promoting respectful on­
line communication.
6  Conclusions
6.1  Review
This research, in the context of an internship with four 
French students at NTNU, advances the field of HS detec­
tion in French with the development of an application where 
one model can make a decision with an explanation given. 
We first built our custom dataset where we took the best 
from the existing dataset online for working on authentic 
French tweets we can find on social media and not French 
translations of English sentences, causing:
	–
Non-Representativeness of French Speech: Specific 
expressions and nuances of the French language and 
culture can be lost in translation, affecting the model’s 
relevance and effectiveness.
	–
Lack of French Expressions: Translated datasets may 
miss idiomatic French expressions limit the model’s 
ability to correctly detect hate speech in real French 
contexts.
This dataset has an almost-perfect balance with its label, 
and working on the balanced target distribution contributes 
to the mitigation of bias, where our models can detect HS 
toward any victimized group.
Then, we developed HS detection with ML early tech­
niques, DL, and transformer-based models which give the 
best results with DistillCamemBERT. Even if our models 
have precision and recall scores that might seem lower, they 
are potentially more reliable and relevant for the French 
context. Indeed, we think that they are more likely to be 
good in real situations, with real tweets.
6.2  Limitations
Our research has achieved certain milestones, yet it exhib­
its significant shortcomings. The performance of our DL-
based models is suboptimal, and overall, our results fall 
short when compared to existing studies in the field. This 
could be attributed to our limited experience, as this is our 
inaugural publication and we are still in the academic phase 
of our careers. The underperformance of our models may 
also stem from using pre-trained embeddings in English, 
which do not align well with French vocabulary. Moving 
forward, it will be crucial to develop and integrate embed­
dings and feature extraction techniques that are better suited 
for French. Moreover, despite efforts to mitigate dataset bias 
5.4  Example use cases
The application is designed to be versatile and applicable in 
various contexts, including:
	–
Social Media Monitoring: Users can analyze com­
ments, posts, and messages to detect and address HS 
proactively.
	–
Content Moderation: Platforms can integrate the ap­
plication to automatically screen user-generated content 
and flag or remove HS.
	–
Educational Tools: Educators and researchers can 
use the application to study HS patterns and develop 
Fig. 15  Example of hateful post found on X (Twitter)
 
Fig. 14  Example of non-hateful post found on X (Twitter)
 
Fig. 13  Example of a false negative: Hateful text misclassified as 
Non-Hateful
 
1 3
811 
Page 16 of 19

--- Page 17 ---

Cluster Computing (2025) 28:811
Open Access   This article is licensed under a Creative Commons 
Attribution 4.0 International License, which permits use, sharing, 
adaptation, distribution and reproduction in any medium or format, 
as long as you give appropriate credit to the original author(s) and the 
source, provide a link to the Creative Commons licence, and indicate 
if changes were made. The images or other third party material in this 
article are included in the article’s Creative Commons licence, unless 
indicated otherwise in a credit line to the material. If material is not 
included in the article’s Creative Commons licence and your intended 
use is not permitted by statutory regulation or exceeds the permitted 
use, you will need to obtain permission directly from the copyright 
holder. To view a copy of this licence, visit ​h​t​t​p​:​/​/​c​r​e​a​t​i​v​e​c​o​m​m​o​n​s​.​o​
r​g​/​l​i​c​e​n​s​e​s​/​b​y​/​4​.​0​/.
References
1.	
Adoum Sanoussi, M.S., Xiaohua, C., Agordzo, G.K., et al.: 
Detection of hate speech texts using machine learning algorithm. 
In: 2022 IEEE 12th Annu. Comput. Commun. Workshop Conf. 
(CCWC) 0266–0273, (2022) ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​0​9​/​C​C​W​C​5​4​5​
0​3​.​2​0​2​2​.​9​7​2​0​7​9​2
2.	
Alhazmi, A., Mahmud, R., Idris, N., et al.: Code-mixing unveiled: 
enhancing the hate speech detection in arabic dialect tweets using 
machine learning models. PLOS ONE 19(7), 1–24 (2024). ​h​t​t​p​s​:​/​
/​d​o​i​.​o​r​g​/​1​0​.​1​3​7​1​/​j​o​u​r​n​a​l​.​p​o​n​e​.​0​3​0​5​6​5​7
3.	
Aluru, S.S., Mathew, B., Saha, P., et al.: Deep learning models for 
multilingual hate speech detection. (2020) arxiv:2004.06465
4.	
Ayele, A.A., Dinter, S., Yimam, S.M., et al.: Multilingual racial 
hate speech detection using transfer learning. In: Mitkov R, Ange­
lova G (eds) Proceedings of the 14th International Conference 
on Recent Advances in Natural Language Processing. INCOMA 
Ltd., Shoumen, Bulgaria, Varna, Bulgaria, pp 41–48, (2023) ​h​t​t​p​
s​:​/​/​a​c​l​a​n​t​h​o​l​o​g​y​.​o​r​g​/​2​0​2​3​.​r​a​n​l​p​-​1​.​5
5.	
Badjatiya, P., Gupta, S., Gupta, M., et al.: Deep learning for hate 
speech detection in tweets. In: Proc. 26th Int. Conf. World Wide 
Web Companion. Int. World Wide Web Con. Steering Committee, 
Republic and Canton of Geneva, CHE, WWW ’17 Companion, 
759–760, (2017) ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​4​5​/​3​0​4​1​0​2​1​.​3​0​5​4​2​2​3
6.	
Bonaldi, H., Dellantonio, S., Tekiroglu, S.S., et al.: Human-
machine collaboration approaches to build a dialogue dataset for 
hate speech countering. In: Proc. 2022 Conf. Empir. Methods 
Nat. Lang. Proc. Assoc. Comput. Linguis. 8031–8049, (2022) ​h​
t​t​p​s​:​/​/​p​r​e​v​i​e​w​.​a​c​l​a​n​t​h​o​l​o​g​y​.​o​r​g​/​e​m​n​l​p​-​2​2​-​i​n​g​e​s​t​i​o​n​/​2​0​2​2​.​e​m​n​l​p​-​
m​a​i​n​.​5​4​9​/
7.	
Chiril, P., Moriceau, V., Benamara, F., et al.: An annotated cor­
pus for sexism detection in french tweets. In: Proc. 12th Lang. 
Resour. Eval. Conf. 1397–1403 (2020)
8.	
Cortiz, D., Zubiaga, A.: Ethical and technical challenges of ai in 
tackling hate speech. Int. Rev. Inf. Eth. 29, (2021) ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​
1​0​.​2​9​1​7​3​/​i​r​i​e​4​1​6,
9.	
Girard, C.: Le droit et la haine: liberté d’expression et << dis­
cours de haine >> en démocratie. Raison-publiquefr: arts, poli­
tique, société, (2014) ​h​t​t​p​s​:​/​/​h​a​l​.​a​r​c​h​i​v​e​s​-​o​u​v​e​r​t​e​s​.​f​r​/​h​a​l​-​0​1​7​5​8​6​
0​7, arxiv:hal-0175.8607
10.	 Hashmi, E., Yayilgan, S.: Multi-class hate speech detection in the 
norwegian language using fast-rnn and multilingual fine-tuned 
transformers. Complex Intell. Syst. 10, 4535–4556 (2024). ​h​t​t​p​s​:​
/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​0​7​/​s​4​0​7​4​7​-​0​2​4​-​0​1​3​9​2​-​5
11.	 Hashmi, E., Yayilgan, S.Y.: A robust hybrid approach with prod­
uct context-aware learning and explainable ai for sentiment 
analysis in amazon user reviews. Electron. Commer. Res. 1–33 
(2024)
12.	 Hashmi, E., Yamin, M.M., Imran, S., et al.: Enhancing misog­
yny detection in bilingual texts using fasttext and explainable ai. 
by evenly distributing targets, we still lack the necessary 
data to confirm whether our model operates without bias.
6.3  Perspectives
Looking forward, several perspectives can be envisioned to 
further this work: 
1.	 Expansion to Multilingual Capabilities: Although our 
current system is tailored to French, extending it to sup­
port multiple languages will make it more versatile and 
widely applicable.
2.	 Real-time Detection and Response: Integrating our 
system into social Media platforms for real-time HS 
detection and response can provide immediate inter­
vention, significantly mitigating the impact of harmful 
content.
3.	 Ethical and Legal Compliance: Continuous monitor­
ing and updating of our system to ensure compliance 
with evolving legal standards and ethical guidelines 
will be essential in maintaining its legitimacy and pub­
lic trust.
Moreover, the application of fair and biased auditing on 
models that work with demographic data, and especially 
HS, is welcome for the future in this research field. Then 
an original future contribution could be the integration and 
the practical work and research for an ethical and moral AI 
model with a bias study by using some tools like Aequitas, 
built by Saleiro et al. [23]; Jesus et al. [17].
Acknowledgements  This research work has been acknowledged by 
SOCYTI(  ​h​t​t​p​s​:​/​/​w​w​w​.​b​i​g​d​a​t​a​.​v​e​s​t​f​o​r​s​k​.​n​o​/​o​n​g​o​i​n​g​/​s​o​c​y​t​i). The 
SOCYTI ​p​r​o​j​e​c​t has received funding from the Research Council 
of Norway as a Researcher Project for Technological Convergence 
related to Enabling Technologies under grant agreement no 331736.
Funding  Open access funding provided by NTNU Norwegian Univer­
sity of Science and Technology (incl St. Olavs Hospital - Trondheim 
University Hospital).
Data Availability and Access  The datasets employed in this research 
are publicly accessible, and their respective URLs are provided in the 
’Dataset Collection’ subsection under the ’Methodology’ section of 
this paper.
Declarations
Github link  Here is the link to our project on Github: ​h​t​t​p​s​:​/​/​g​i​t​h​u​b​.​c​o​
m​/​z​h​d​a​t​/​h​a​t​e​c​h​e​c​k​-​d​e​t​e​c​t​o​r​.
Competing Interests  The authors declare that they have no competing 
interests.
Ethical and Informed Consent for Data Used  Not Applicable.
1 3
Page 17 of 19 
811

--- Page 18 ---

Cluster Computing (2025) 28:811
Zahim Chared  is a final-year 
Software Engineering student, 
specialized in Data-AI Engineer­
ing and Image Processing at 
ENSICAEN, France, currently 
completing 
his 
internship 
at 
Orange Innovation. His work 
focuses on analyzing WiFi degra­
dations and their impact on user 
experience using machine learn­
ing. He has contributed to projects 
in generative AI for cultural heri­
tage and cancer cell detection 
through 
data-driven 
models. 
Zahim 
also 
conducted 
NLP 
research on hate speech detection at NTNU, Norway. His interests 
include intelligent systems, data modeling, and real-world AI 
applications.
Clément Jantet   is a software 
engineering student and aspiring 
innovator specializing in software 
development. He is currently pur­
suing his engineering degree at 
EnsiCaen, France, where he has 
acquired solid skills in software 
engineering, with a particular 
focus on cybersecurity and elec­
tronic payment systems. His 
research interests include ethical 
artificial intelligence and machine 
learning.
Calliste Ravix  is currently pursu­
ing his Engineering degree in 
Software Engineering with a spe­
cialization in E-Payment and 
Cybersecurity at École Nationale 
Supérieure d'Ingénieur de Caen 
(ENSICAEN), France (expected 
2025). His research interests 
include natural language process­
ing, hate speech detection, and 
machine learning applications.
In: 2024 Int. Conf. Eng. Comput. Technol. (ICECT), IEEE, 1–6 
(2024)
13.	 Hashmi, E., Yayilgan, S.Y., Abomhara, M.: Metalinguist: enhanc­
ing hate speech detection with cross-lingual meta-learning. Com­
plex Intell. Syst. 11(4), 179 (2025)
14.	 Hashmi, E., Yayilgan, S.Y., Yamin, M.M., et al.: Self-supervised 
hate speech detection in norwegian texts with lexical and seman­
tic augmentations. Expert Syst. Appl. 264, 125843 (2025)
15.	 Hashmi, E., Yayilgan, S.Y., Yamin, M.M., et al.: Enhancing 
misogyny detection in bilingual texts using explainable ai and 
multilingual fine-tuned transformers. Complex Intell. Syst. 11(1), 
39 (2025)
16.	 Hoareau, A.: French preprocessing tool. ​h​t​t​p​s​:​/​/​g​i​t​h​u​b​.​c​o​m​/​a​n​a​i​s​
h​o​a​r​e​a​u​/​f​r​e​n​c​h​_​p​r​e​p​r​o​c​e​s​s​i​n​g, (2021) accessed: 2024-07-23
17.	 Jesus, S., Saleiro, P., Jorge, B.M., et al.: Aequitas flow: 
streamlining fair ml experimentation. (2024) arXiv preprint 
arXiv:2405.05809
18.	 Kastrati, M., Imran, A.S., Hashmi, E., et al.: Unlocking language 
barriers: assessing pre-trained large language models across mul­
tilingual tasks and unveiling the black box with explainable arti­
ficial intelligence. Eng. Appl. Artif. Intell. 149, 110136 (2025)
19.	 Heuveline, L.: Frenchhatespeechsuperset (revision b073070). 
(2023) ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​5​7​9​6​7​/​h​f​/​0​2​8​4, ​h​t​t​p​s​:​/​/​h​u​g​g​i​n​g​f​a​c​e​.​c​o​/​
d​a​t​a​s​e​t​s​/​P​o​u​l​p​i​d​o​t​/​F​r​e​n​c​h​H​a​t​e​S​p​e​e​c​h​S​u​p​e​r​s​e​t
20.	 Mancarella, M., Rodriguez-Martin, E., Sutton, C., et al.: Help dil­
crah: a hate speech detection tool on twitter (in french). (2018) ​
h​t​t​p​s​:​/​/​g​i​t​h​u​b​.​c​o​m​/​M​i​k​3​M​4​n​/​h​e​l​p​_​d​i​c​r​a​h​/​t​r​e​e​/​m​a​s​t​e​r, accessed: 
2024-07-25
21.	 Ousidhoum, N., Lin, Z., Zhang, H., et al.: Multilingual and multi-
aspect hate speech analysis. (2019) arxiv:1908.11049
22.	 Röttger, P., Seelawi, H., Nozza, D., et al.: Multilingual hatecheck: 
functional tests for multilingual hate speech detection models. 
(2022) arxiv:2206.09917
23.	 Saleiro, P., Kuester, B., Stevens, A., et al.: Aequitas: a bias and 
fairness audit toolkit. (2018) arXiv preprint arXiv:1811.05577
24.	 Sohail, T., Aiman, A., Hashmi, E., et al.: Hate speech detection 
in code-mixed datasets using pretrained embeddings and trans­
formers. In: 2024 Int. Conf. Front. Inf. Technol. (FIT), IEEE, 1–6 
(2024)
25.	 Suler, J.: The online disinhibition effect. Cyberpsychology & 
behavior:the impact of the Internet, multimedia and virtual reality 
on behavior and society 7, 321–6 (2004). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​8​9​/​
1​0​9​4​9​3​1​0​4​1​2​9​1​2​9​5
26.	 Tonneau, M., Liu, D., Fraiberger, S., et al.: From languages to 
geographies: towards evaluating cultural bias in hate speech data­
sets. In: Chung YL, Talat Z, Nozza D, et al (eds) Proceedings of 
the 8th Workshop on Online Abuse and Harms (WOAH 2024). 
Association for Computational Linguistics, Mexico City, Mexico, 
283–311, (2024) ​h​t​t​p​s​:​/​/​a​c​l​a​n​t​h​o​l​o​g​y​.​o​r​g​/​2​0​2​4​.​w​o​a​h​-​1​.​2​3
27.	 Vanetik, N., Mimoun, E.: Detection of racist language in french 
tweets. Information 13(7), (2022). ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​3​3​9​0​/​i​n​f​o​1​3​
0​7​0​3​1​8, ​h​t​t​p​s​:​/​/​w​w​w​.​m​d​p​i​.​c​o​m​/​2​0​7​8​-​2​4​8​9​/​1​3​/​7​/​3​1​8
Publisher's Note  Springer Nature remains neutral with regard to juris­
dictional claims in published maps and institutional affiliations.
1 3
811 
Page 18 of 19

--- Page 19 ---

Cluster Computing (2025) 28:811
Sule Yildirim Yayilgan  works at 
the Department of Information 
Security 
and 
Communication 
Technology (IIK), NTNU since 
2009. She received a MSc. degree 
in Computer Engineering in 1995, 
and PhD in Artificial Intelligence 
and Computer Science in 2002. 
She has worked for more than 25 
years in academic teaching. She 
has been supervising students at 
different academic levels and has 
been publishing more than 100 
journal and conference papers. 
Her research areas include image 
processing, information security, natural language processing, compu­
tational linguistics, large language models, and data mining. 
Robin Salmi  is a dedicated soft­
ware engineering student at ENSI­
CAEN, France, specializing in 
E-Payment and Cybersecurity. 
With a strong foundation in secure 
digital transactions and informa­
tion protection. Beside his focus 
in E-Payment, he is also deeply 
interested in natural language pro­
cessing, machine learning, and 
artificial intelligence applications.
Ehtesham Hashmi  received a 
B.S. degree in computer science 
from the University of Central 
Punjab, (Lahore Campus) in 2020, 
and an M.S. degree in computer 
science from COMSATS Univer­
sity Islamabad (Lahore Campus) 
in 2022. From 2022 to 2023, he 
was a Lecturer at the University of 
Lahore in the Department of Com­
puter Science. Currently, he is a 
PhD Candidate at the Norwegian 
University of Science and Tech­
nology - (NTNU) in the Depart­
ment of Information Security and 
Communication Technology (IIK). His research areas include multi­
lingual natural language processing, computational linguistics, Gen­
erative AI with LLMs, knowledge graphs, and data mining.
1 3
Page 19 of 19 
811

```
