---
title: "2024-Kathunia-Sentiment Analysis Across Languages Evaluation Before and After - PDF Extract"
source_pdf: "2024-Kathunia-Sentiment Analysis Across Languages Evaluation Before and After.pdf"
pages: 7
extracted_at: "2026-02-13T13:57:12.788128"
---

# PDF Extract: 2024-Kathunia-Sentiment Analysis Across Languages Evaluation Before and After

**Source PDF:** 2024-Kathunia-Sentiment Analysis Across Languages Evaluation Before and After.pdf
**Total Pages:** 7

---

## Content

```
--- Page 1 ---

Sentiment Analysis Across Languages: Evaluation Before and After Machine
Translation to English
Aekansh Kathunia
IIIT Delhi
aekansh21127@iiitd.ac.in
Mohammad Kaif
IIIT Delhi
kaif21067@iiitd.ac.in
Nalin Arora
IIIT Delhi
nalin21478@iiitd.ac.in
N Narotam
IIIT Delhi
narotam21477@iiitd.ac.in
Abstract
People communicate in more than 7,000 languages
around the world, with around 780 languages spoken in
India alone. Despite this linguistic diversity, research on
Sentiment Analysis has predominantly focused on English
text data, resulting in a disproportionate availability of
sentiment resources for English. This paper examines the
performance of transformer models in Sentiment Analysis
tasks across multilingual datasets and text that has under-
gone machine translation. By comparing the effectiveness
of these models in different linguistic contexts, we gain in-
sights into their performance variations and potential im-
plications for sentiment analysis across diverse languages.
We also discuss the shortcomings and potential for future
work towards the end.
1. Introduction
The term Sentiment Analysis refers to the process of ana-
lyzing text to determine the emotional tone of the message.
More generally, it can be understood as assessing an indi-
vidual towards a particular target.
Machine translation refers to the conversion of text from
a source language to a target language via the use of com-
puter algorithms.
Bert and XLM Roberta are Large language models
based on the transformer architecture introduced by Google,
trained on a huge corpus of data, ideal for fine-tuning
downstream tasks such as Sentiment Analysis and Machine
Translation. Given the accessibility and usefulness of these
models, they find their application in various languages
other than English and various multilingual settings, where
models are tuned to understand context in multiple lan-
guages.
Due to easy accessibility and the plethora of literature
available in English, tasks like Sentiment Analysis have ex-
tensively been researched on English texts, which naturally
leads to many sentiment resources for English texts but less
so for texts in other languages.
In our project, we aim to compare Sentiment Analy-
sis performance on the original language texts for the lan-
guages French, German, Spanish, Japanese and Chinese
while also comparing machine translation performance of
models across different languages.
Other work done with similar objectives, we believe, of-
ten falls short of creating a robust pipeline to process mul-
tilingual datasets and often implements simple rudimentary
pipelines that don’t use underlying datasets to the fullest.
We identify certain gaps and interesting areas in which we
could expand existing research done on this topic and thus
present the major contributions of our project:
• We present robust pipelines that incorporate and com-
pare various state-of-the-art sentiment analysis and
machine translation models.
• We provide domain-tuned versions of large language
models on a subset of the Multilingual Amazon Re-
views Corpus [10].
• We analyse the translation models in different lan-
guages by their ability to recreate the baseline for sen-
timent analysis of English models. This allows us to
understand the progress of NLP in different languages
compared to English.
• We explore if it is viable to use cross-lingual over
uni-lingual models and if significant performance can
be achieved by machine translation to transform the
1
arXiv:2405.02887v2  [cs.CL]  2 Sep 2024

--- Page 2 ---

dataset into English, in which models are, in general,
better.
For all tasks, we use transformer-based models that have
been pre-trained on an enormous corpus of text prior to our
deployment and pertaining.
2. Related Work
2.1. Sentiment Analysis and Emotion Detection
from Text
There have been several studies exploring sentiment
analysis and emotion detection techniques being applied to
textual data. The paper from Nandwani and Verma pro-
vides insights into different methodologies used for ana-
lyzing sentiments and detecting emotions. They delve into
traditional machine learning algorithms and deep learning
models, highlighting their strengths and limitations on the
above-mentioned task. [14].
Mohammad et al. examine how translation alters sen-
timent, focusing on the impact of machine translation on
sentiment analysis across languages [13]. They observe that
machine translation can significantly alter the sentiment ex-
pressed in a sentence and highlight the challenges of accu-
rately capturing sentiment in a multilingual setting.
Araujo et al. evaluate machine translation for multilin-
gual sentence-level sentiment analysis and assess the effec-
tiveness of different machine translation models in preserv-
ing sentiment across languages [2]. However, their find-
ings underscore the importance of considering the quality
of machine translation while conducting sentiment analysis
in multilingual contexts.
2.2. Challenges in Multilingual Sentiment Analysis
One of the key challenges identified by both Mohammad
et al. and Araujo et al. in accurately interpreting emotions
from text is the inherent complexity of language, which in-
cludes nuances, context, and cultural disparities. This chal-
lenge is more inherent in a multilingual setting, where the
translation of text to English may not fully capture the orig-
inal sentiment or emotion.
Moreover, recent advancements in sentiment analysis
and emotion detection have focused on integrating mul-
timodal data and leveraging pre-trained language models
to enhance accuracy. These developments are particularly
relevant in the context of multilingual sentiment analysis,
where incorporating additional modalities such as images or
audio can provide valuable context for understanding emo-
tions expressed in text.
Overall, the insights provided by Nandwani and Verma,
Mohammad et al., and Araujo et al. offer valuable consid-
erations for evaluating sentiment analysis across languages,
both before and after machine translation to English.
2.3. BERT
BERT (Bidirectional Encoder Representations from
Transformers) is a pre-trained language model developed
by Google [8]. It is based on a multi-layer bidirectional
transformer encoder, which generates contextualized rep-
resentations of input text. BERT is pre-trained on a large
corpus of text and is fine-tuned on specific tasks, achieving
state-of-the-art results in various natural language process-
ing tasks.
For languages other than English, we used the following
instances of Bert from hugging face:
1. bert-base-german-cased [5] - This is a German lan-
guage model based on the BERT architecture. It was devel-
oped by Google and has been fine-tuned on a large corpus
of German text.
2. dccuchile/bert-base-spanish-wwm-cased [4] - This is
a Spanish language model based on the BERT architecture.
It was developed by the University of Chile and has been
fine-tuned on a large corpus of Spanish text.
3. dbmdz/bert-base-french-europeana-cased [16] - is a
French language model based on the BERT architecture. It
was developed by the researchers at the Center for Informa-
tion and Language Processing (CIS), LMU Munich.
4. cl-tohoku/bert-base-japanese [18] - This is a Japanese
language model based on the BERT architecture. It was
developed by Tohoku University and has been fine-tuned
on a large corpus of Japanese text.
5. bert-base-chinese(addition of original bert paper [9] -
This is a Chinese language model based on the BERT archi-
tecture. It was developed by Google and has been fine-tuned
on a large corpus of Chinese text.
BERT has been shown to be effective in sentiment clas-
sification tasks, achieving high accuracy by leveraging its
contextualized representations and fine-tuning on specific
datasets [15]. BERT fine-tuning has led to remarkable state-
of-the-art results on various downstream tasks, including
sentiment analysis.
2.4. XLM RoBERTa
XLM-RoBERTa [6] is a multi-lingual language model
that combines the strengths of XLM [7] and RoBERTa
[12]. The architecture is based on the RoBERTa model,
with a modified XLM encoder that enables cross-lingual
transfer learning. This allows XLM-RoBERTa to leverage
pre-training in multiple languages and fine-tune on specific
tasks, achieving state-of-the-art results in various natural
language processing tasks.
2

--- Page 3 ---

Figure 1. Training Pipeline
XLM-RoBERTa has been shown to be effective in senti-
ment classification tasks, achieving high accuracy in multi-
ple languages [3]. By leveraging its multi-lingual capabili-
ties and fine-tuning on our dataset, we achieve high perfor-
mance in sentiment classification.
3. Methodology
We meticulously constructed a robust pipeline to fulfill
the project’s objectives of comparing transformer perfor-
mance in sentiment analysis across multilingual data and
machine-translated text. This pipeline used advanced trans-
former architectures such as BERT and XLM-RoBERTa.
BERT, short for Bidirectional Encoder Representations
from Transformers, is an encoder-only model that utilises
masked language modeling and next-sentence prediction
techniques. BERT models are primarily trained in a single
language context.
XLM-RoBERTa is an advancement over XLM, leverag-
ing the robust RoBERTa architecture. Through extensive
pre-training on a larger dataset and prolonged training ses-
sions, XLM-RoBERTa excels in various NLP tasks. It in-
herits XLM’s cross-lingual capabilities and benefits from
RoBERTa’s enhanced representation learning, making it
highly proficient in handling multilingual data and achiev-
ing superior performance across diverse NLP tasks.
To achieve our machine translation objective, we em-
ployed the OPUS-MT machine translation model, which
utilizes state-of-the-art transformer-based neural machine
translation techniques. By leveraging the usage of trans-
formers, OPUS-MT achieves good-quality translations and
fluency across multiple languages. This choice aligns per-
fectly with our project’s focus on evaluating transformer
performance on machine-translated text, ensuring robust-
ness and reliability in our analyses.
To compare the model performance, we utilized F1-
scores as the metric since they give a holistic review of the
model’s performance across classes.
The pipeline we used during the project is as follows,
we first used 50000 entries from each language due to lim-
ited computational capability to fine-tune BERT and XLM-
RoBERTa models and evaluate their performance using F1-
score. In the second part we translated 20000 entries from
each language using OPUS-MT to English and then com-
bined them together to form a dataset of 100000 entries.
We fine-tuned our BERT and XLM-RoBERTa models on
this combined dataset and then evaluated the model’s per-
formance using the F1-score as the evaluation metric.
By employing these state-of-the-art transformer models
within our pipeline, we aimed to comprehensively evaluate
their efficacy in sentiment analysis tasks across multilingual
datasets and machine-translated texts.
4. Dataset
The dataset used in this study is the Multilingual Ama-
zon Reviews Corpus, as described by Keung et al. [10].
This corpus represents a rich collection of product reviews
gathered from the Amazon platform, spanning multiple
languages, including English, Spanish, French, German,
Japanese, Chinese, and Italian.
The Multilingual Amazon Reviews Corpus contains re-
views across a wide range of product categories, such as
3

--- Page 4 ---

Table 1. Training corpus statistics. 200,000 reviews per language. Taken from the corpus review paper by Keung et al.
En
De
Es
Fr
Ja
Zh
Number of products
196,745
189,148
179,076
183,345
185,436
164,540
Number of reviewers
185,541
171,620
150,938
157,922
164,776
132,246
Average characters/review
178.8
207.9
151.3
159.4
101.4
51.0
Average characters/review title
24.2
21.8
19.2
19.1
9.5
7.6
electronics, books, movies, home appliances, and more.
Each review entry within the dataset is accompanied by
comprehensive metadata, including the product ID, re-
viewer ID, review text, star rating, and review date. Ad-
ditionally, the dataset contains information about the ge-
ographic location of reviewers, providing insights into re-
gional variations in sentiment expression.
One of the notable features of the Multilingual Amazon
Reviews Corpus is its extensive coverage of languages and
product categories, making it a valuable resource for study-
ing sentiment analysis and multilingual natural language
processing tasks. Researchers can leverage this dataset to
explore the complexities and nuances of sentiment analysis
across diverse linguistic and cultural contexts.
In this study, we selected the Multilingual Amazon Re-
views Corpus due to its multilingual nature and diverse
product categories, which provided us with an opportunity
to investigate the challenges and opportunities of sentiment
analysis across different languages and domains.
5. Experimental Setup
Due to limited computational resources, we utilize a
randomly sampled subset of the Multilingual Amazon Re-
views Corpus, consisting of 50,000 samples of the lan-
guages French, German, Spanish, Japanese and Chinese
while also ensuring that the data is balanced.
Hugging Face Model ID
Language Specific
bert-base-german-cased
german BERT
dccuchile/bert-base-spanish-wwm-cased
spanish BERT
dbmdz/bert-base-french-europeana-cased
french BERT
cl-tohoku/bert-base-japanese
japanese BERT
bert-base-chinese
chinese BERT
bert-base-uncased
english BERT
xlm-roberta-base
Multi-Lingual
Table 2. Mapping Hugging Face Model IDs to Language Speci-
ficity
We tune uni-lingual BERT models for each language and
also a multi-lingual XLM-RoBERTa model on our dataset
to further assess the performance of these different lan-
guages across different languages. The performance of each
model in each language is ultimately compared to the per-
formance of BERT and XLM-RoBERTa on English models
tuned on the dataset.
For our evaluation, we observe the model performance
on two tasks:
1. Sentiment Classification: Classify the review text
into two classes, positive review and negative review.
2. Star Rating Prediction: Predict the star rating of the
review text.
Figure 2. Distribution of Labels
The gold labels for Star Rating Prediction were already
present in the dataset. However, the gold labels for Sen-
timent Classification were not present in the dataset and
were obtained from the annotated ”hungnm/multilingual-
amazon-review-sentiment-processed” [1] dataset from hug-
gingface.
The model evaluation tasks were first performed on all
of the sampled data. Then, 20,000 samples from each of
the source languages were translated to the target language,
English. The evaluation tasks were then repeated on the
translated samples to assess post Machine Translation per-
formance.
6. Results
It can be observed that machine translation didn’t affect
if not significantly improve or derail performance of models
in their downstream applications for languages like Spanish,
4

--- Page 5 ---

Language
Before Machine Translation
After Machine Translation
Spanish(ES)
Spanish XLM
0.90461
Spanish BERT
0.88878
Spanish XLM
0.89965
Spanish BERT
0.89875
German (DE)
German XLM
0.90585
German BERT
0.90730
German XLM
0.89420
German BERT
0.89672
French (FR)
French XLM
0.90294
French BERT
0.87775
French XLM
0.88740
French BERT
0.89131
Chinese (ZH)
Chinese XLM
0.86715
Chinese BERT
0.86844
Chinese XLM
0.83660
Chinese BERT
0.82391
Japanese(JA)
Japanese XLM
0.90161
Japanese BERT
0.89231
Japanese XLM
0.83049
Japanese BERT
0.82479
Table 3. Sentiment Classification
Language
Before Machine Translation
After Machine Translation
Spanish(ES)
Spanish XLM
0.60697
Spanish BERT
0.58337
Spanish XLM
0.58155
Spanish BERT
0.62267
German (DE)
German XLM
0.64942
German BERT
0.62421
German XLM
0.61658
German BERT
0.63514
French (FR)
French XLM
0.61209
French BERT
0.58065
French XLM
0.56994
French BERT
0.60932
Chinese (ZH)
Chinese XLM
0.62267
Chinese BERT
0.54087
Chinese XLM
0.54025
Chinese BERT
0.61938
Japanese(JA)
Japanese XLM
0.60377
Japanese BERT
0.51262
Japanese XLM
0.52043
Japanese BERT
0.59127
Table 4. Star Rating Prediction
German and French, which as clearly European languages
and share a lot of semantic similarities with english. On
the other hand Machine Translation significantly, affects the
performance of languages Chinese and Japanese in a nega-
tive way, as they are significantly unique to english. How-
ever no model could reach the fine tuned performance of the
english baseline of about 0.91 for english reviews, which
could be due to gaps in Machine Translation models, as
theoretically they translated sentences in english should be
able to convey full meaning of original sentence and reach
english benchmarks.However failure to do so even after in-
tensive fine-tuning, leads us to conclude that either more ro-
bust fine-tuning on a much larger dataset rather than a sub-
set or a more robust pipeline should help, which would have
been outside the scope of our project given the resource, and
time.
7. Observations
Table 1 and Table 2 show the F1 scores for our tasks for
each of the language specific model before and after ma-
chine Translation.
We can infer that XLM-RoBERTA performs slightly bet-
ter than BERT for each language dataset as expected due
to XLM’s cross-lingual capabilities. For the task of Senti-
ment Analysis, the average F1 score over all the models was
0.89. Before Machine Translation, the German model got
the best F1 score across all the models, while the Chinese
performed the worst. After Translation, the performance of
all the models degraded with the Japanese Model being the
most affected. The Spanish model got the best F1 score af-
ter machine Translation. For the task of Star Rating Predic-
tion, the average F1 score over all the models was 0.61. Be-
fore Machine Translation, the German model outperformed
all the models, while the Japanese performed the worst. Af-
ter Translation, the performance of all the models degraded
with the Japanese and Chinese Models being the most af-
fected. The German model still got the best F1 score after
machine Translation across all the models.
8. Conclusion and Future Work
During the course of the project, we developed language-
specific models and models utilizing translated texts. There
was no significant difference between the models devel-
oped during the project(language-specific and models us-
ing translated tests) as they achieved similar performance.
However, the slight difference that occurred can be due to
the following shortcomings.
Languages like Spanish, German, and French share
many similarities with English regarding sentence structure
sharing the same SVO word order with English. As a re-
sult, machine translation from these languages to English
may preserve the original meaning well, leading to consis-
tent sentiment analysis results. However, Asian languages
like Japanese and Chinese have different linguistic struc-
tures. Japanese syntax follows SOV word order while Chi-
nese sentence structure is characterized by its lack of inflec-
tional morphology and grammatical markers, relying heav-
ily on word order and context for conveying meaning. Ma-
chine translation may struggle to accurately capture such
semantic meaning, leading to loss of information and thus
Higher Semantic difference.
Asian cultures, for example, may have unique ways of
conveying sentiment that differ from Western cultures.So
Cultural difference also plays a role in Machine Trans-
lation. Lastly, The availability and quality of training
data may vary across languages. English sentiment analysis
models may have been trained on larger and more diverse
datasets compared to models for other languages. This dis-
crepancy in training data quality can impact the effective-
ness of sentiment analysis after machine translation, espe-
cially for languages with less available data.
In summary, the effectiveness of machine translation
in preserving sentiment and maintaining performance in
downstream applications such as sentiment analysis de-
pends on factors such as linguistic similarity, syntactic com-
plexity, cultural differences, and data availability. While
machine translation may perform well for languages closely
related to English, it may encounter challenges in accurately
capturing sentiment for languages with greater linguistic
and cultural differences.
To improve the work done, there can be further ex-
perimentation, which involves, firstly, fine-tuning machine
translation models specifically for sentiment-related tasks.
This could involve adding sentiment-specific data or anno-
tations into the fine-tuning process to improve the efficacy
of translations, especially for languages with high linguis-
5

--- Page 6 ---

tic differences from English. Extensive literature is avail-
able to improve sentiment analysis of models by training
them on general or domain-specific Knowledge graphs [11],
such as ConceptNet [17]. Secondly, utilizing multimodal
approaches incorporating visual and textual information for
sentiment analysis across languages. Exploring how images
or videos can complement machine-translated text to im-
prove the performance of sentiment analysis, especially in
languages where textual data may be limited or unreliable.
Some preliminary work on this could be explored in work
done by Yoon et al. [19]. Finally, focusing on improving
sentiment analysis performance in low-resource languages
with a lack of training data. Experimentation can be done by
exploring transfer, semi-supervised, or unsupervised learn-
ing to adapt to sentiment analysis tasks for languages with
limited labelled data.
In summary, the effectiveness of machine translation
in preserving sentiment and maintaining performance in
downstream applications such as sentiment analysis de-
pends on factors such as linguistic similarity, syntactic com-
plexity, cultural differences, data availability, and transla-
tion quality. While machine translation may perform well
for languages closely related to English, it may encounter
challenges in accurately capturing sentiment for languages
with greater linguistic and cultural differences.
9. Code Availability
We have published all our code files and processed the
dataset to GitHub. Fine-tuned model checkpoints of all the
models can be found at Drive.
References
[1] hungnm/multilingual-amazon-review-sentiment-processed.
https://huggingface.co/datasets/hungnm/
multilingual - amazon - review - sentiment -
processed. 4
[2] Matheus Araujo, Julio Reis, Adriano Pereira, and Fabricio
Benevenuto. An evaluation of machine translation for mul-
tilingual sentence-level sentiment analysis. In Proceedings
of the 31st Annual ACM Symposium on Applied Computing,
SAC ’16, page 1140–1145, New York, NY, USA, 2016. As-
sociation for Computing Machinery. 2
[3] Francesco Barbieri, Luis Espinosa Anke, and Jose Camacho-
Collados. XLM-T: Multilingual language models in Twit-
ter for sentiment analysis and beyond.
In Proceedings of
the Thirteenth Language Resources and Evaluation Confer-
ence, pages 258–266, Marseille, France, June 2022. Euro-
pean Language Resources Association. 3
[4] Jos´e Ca˜nete, Gabriel Chaperon, Rodrigo Fuentes, Jou-Hui
Ho, Hojin Kang, and Jorge P´erez. Spanish pre-trained bert
model and evaluation data. In PML4DC at ICLR 2020, 2020.
2
[5] Branden Chan, Stefan Schweter, and Timo M¨oller.
Ger-
man’s next language model.
In Donia Scott, Nuria Bel,
and Chengqing Zong, editors, Proceedings of the 28th In-
ternational Conference on Computational Linguistics, pages
6788–6796, Barcelona, Spain (Online), Dec. 2020. Interna-
tional Committee on Computational Linguistics. 2
[6] Alexis Conneau, Kartikay Khandelwal, Naman Goyal,
Vishrav Chaudhary, Guillaume Wenzek, Francisco Guzm´an,
Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin
Stoyanov. Unsupervised cross-lingual representation learn-
ing at scale. 2019. 2
[7] Alexis CONNEAU and Guillaume Lample. Cross-lingual
language model pretraining. In H. Wallach, H. Larochelle,
A. Beygelzimer, F. d'Alch´e-Buc, E. Fox, and R. Garnett, ed-
itors, Advances in Neural Information Processing Systems,
volume 32. Curran Associates, Inc., 2019. 2
[8] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina
Toutanova. BERT: Pre-training of deep bidirectional trans-
formers for language understanding. In Jill Burstein, Christy
Doran, and Thamar Solorio, editors, Proceedings of the 2019
Conference of the North American Chapter of the Associa-
tion for Computational Linguistics: Human Language Tech-
nologies, Volume 1 (Long and Short Papers), pages 4171–
4186, Minneapolis, Minnesota, June 2019. Association for
Computational Linguistics. 2
[9] Google.
google-bert/bert-base-chinese · Hugging Face
— huggingface.co.
https://huggingface.co/
google-bert/bert-base-chinese. [Accessed 25-
04-2024]. 2
[10] Phillip Keung, Yichao Lu, Gy¨orgy Szarvas, and Noah A.
Smith. The multilingual Amazon reviews corpus. In Bonnie
Webber, Trevor Cohn, Yulan He, and Yang Liu, editors, Pro-
ceedings of the 2020 Conference on Empirical Methods in
Natural Language Processing (EMNLP), pages 4563–4568,
Online, Nov. 2020. Association for Computational Linguis-
tics. 1, 3
[11] Jie Li, Xuan Li, Linmei Hu, Yirui Zhang, and Jinrui Wang.
Knowledge graph enhanced language models for sentiment
analysis.
In The Semantic Web – ISWC 2023, Lecture
notes in computer science, pages 447–464. Springer Nature
Switzerland, Cham, 2023. 6
[12] Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar
Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettle-
moyer, and Veselin Stoyanov. RoBERTa: A robustly opti-
mized BERT pretraining approach. 2019. 2
[13] Saif M. Mohammad, Mohammad Salameh, and Svetlana
Kiritchenko. How translation alters sentiment. Journal of
Artificial Intelligence Research, 55:95–130, 2016. 2
[14] Pansy Nandwani and Rupali Verma. A review on sentiment
analysis and emotion detection from text. Social Network
Analysis and Mining, 11(1):81, 2021. 2
[15] Md Shohel Sayeed, Varsha Mohan, and Kalaiarasi Sonai
Muthu. BERT: A review of applications in sentiment analy-
sis. HighTech. Innov. J., 4(2):453–462, June 2023. 2
[16] Stefan Schweter. Europeana bert and electra models, 2020.
2
[17] Robyn Speer, Joshua Chin, and Catherine Havasi. Concept-
Net 5.5: An open multilingual graph of general knowledge.
2016. 6
6

--- Page 7 ---

[18] TOHOKU UNIVERSITY. Bert (base japanese). https:
//huggingface.co/tohoku-nlp/bert-base-
japanese, 2020. 2
[19] Seunghyun Yoon, Seokhyun Byun, and Kyomin Jung. Mul-
timodal speech emotion recognition using audio and text.
2018. 6
7

```
