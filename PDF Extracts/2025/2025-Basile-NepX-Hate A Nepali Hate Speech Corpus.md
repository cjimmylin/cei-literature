---
title: "2025-Basile-NepX-Hate A Nepali Hate Speech Corpus"
source_pdf: "[[Lit-WS-PDFs/2025/2025-Basile-NepX-Hate A Nepali Hate Speech Corpus.pdf]]"
extracted_date: "2026-02-14"
extraction_method: "PyMuPDF"
---

# PDF Extract: 2025-Basile-NepX-Hate A Nepali Hate Speech Corpus

```
## Page 1

NepX-Hate: A Nepali Hate Speech Corpus with Fine-Grained Sociocultural
Annotations
Anonymous ACL submission
Abstract
001
Hate speech detection in low-resource lan-
002
guages remains a significant challenge due to
003
the scarcity of annotated datasets. We intro-
004
duce NepX-Hate, a new benchmark dataset
005
for hate speech detection in low-resource lan-
006
guages, centered on Nepali with an auxiliary
007
Hindi subset for cross-lingual experiments. The
008
dataset comprises 10,000 annotated tweets la-
009
beled across multiple dimensions: hate speech
010
presence, fine-grained category (e.g., casteism,
011
xenophobia), offensiveness, target type, and
012
sentiment. NepX-Hate is the first publicly avail-
013
able hate-speech dataset with multi-aspect so-
014
ciocultural annotations, covering general social
015
media discourse beyond prior domain-specific
016
efforts. We provide benchmarks across tradi-
017
tional classifiers and multilingual transformer
018
models, revealing challenges in detecting im-
019
plicit hate and highlighting how fine-grained la-
020
bels aid model interpretability. NepX-Hate pro-
021
vides a comprehensive testbed for hate speech
022
research in underrepresented languages, en-
023
abling both sociocultural analysis and multilin-
024
gual transfer. We release the dataset and code
025
publicly, aiming to support robust, explainable
026
hate speech detection in the Global South.
027
Content Warning: This paper contains examples
028
and discussions of hate speech, including poten-
029
tially offensive language and discriminatory con-
030
tent, used solely for academic research purposes.
031
Reader discretion is advised.
032
1
Introduction
033
Hate speech is expressions that spread hatred, in-
034
cite violence, or discriminate against individuals or
035
groups based on their protected attributes or iden-
036
tity. Hate speech is subjective, and many define it
037
differently. According to the United Nations (UN,
038
2019), Hate Speech is any kind of communication
039
in speech, writing, or behavior, that attacks or uses
040
pejorative or discriminatory language with refer-
041
ence to a person or a group on the basis of who
042
they are, in other words, based on their religion,
043
ethnicity, nationality, race, color, descent, gender
044
or other identity factor. Hate speech has become a
045
growing concern on social media due to the lack of
046
moderation and anonymity. It also provides a plat-
047
form for people to collectively incite hatred against
048
others (Walther, 2022).
049
To tackle the increasing cyberbullying and hate
050
speech, researchers have opted to use Natural Lan-
051
guage Processing (NLP), and machine learning to
052
develop tools for the automatic detection of hate
053
speech (Jahan and Oussalah, 2023). All such tools
054
depend on annotated datasets, mostly collected
055
from social media websites such as Facebook, X
056
(formerly known as Twitter), Reddit, etc. However,
057
most of the annotated hate speech datasets are only
058
available for the English language (Poletto et al.,
059
2021), with limited resources for some other major
060
languages (Vidgen and Derczynski, 2021). Distin-
061
guishing hate speech in a particular language from
062
offensive or abusive speech is difficult due to the
063
subjective nature of interpretation and cultural con-
064
text, suggesting dataset requirement of the same
065
language (Schmidt and Wiegand, 2017).
066
South Asian languages—particularly Nepali and
067
Hindi—face distinct challenges: complex morphol-
068
ogy, and culturally rooted hate expressions. Yet, re-
069
sources for hate speech detection in these languages
070
remain limited or domain-specific, with most ef-
071
forts constrained to political contexts (Thapa et al.,
072
2023). Furthermore, most datasets either lack nu-
073
ance (e.g., binary labels only) or do not distin-
074
guish between hate, offensiveness, and targeted
075
speech—dimensions critical to understanding and
076
moderating online discourse in multilingual soci-
077
eties.
078
To bridge this gap, we present NepX-Hate, a novel
079
1

## Page 2

Figure 1: Word Cloud depicting the most frequent occuring words in the True cases of hate speech in the Nepali
split of the dataset
dataset of 10,621 Nepali tweets annotated across
080
five sociolinguistic dimensions: hate_label, fine-
081
grained hate_category (e.g., casteism, racism), of-
082
fensiveness, sentiment, and target type. Data was
083
collected via keyword-driven crawling of publicly
084
available tweets, followed by multi-round prepro-
085
cessing and native speaker annotation with strong
086
inter-annotator agreement. Our core contributions
087
are:
088
• A high-quality, multi-annotated hate speech
089
dataset in Nepali, with a parallel Hindi subset
090
for cross-lingual experiments.
091
• Annotation guidelines and sociolinguistic la-
092
bels that support nuanced detection, inter-
093
pretability, and cultural analysis.
094
• Benchmarks using traditional ML and multi-
095
lingual transformer models for binary classifi-
096
cation and category prediction.
097
• Interpretability analysis between traditional,
098
single task and multitask baselines
099
NepX-Hate is the first publicly available dataset of
100
its kind for any language and contributes toward
101
equitable NLP resources for underrepresented lan-
102
guages. All data, annotation guidelines, and mod-
103
els are made available to support reproducible and
104
extensible research in hate speech detection.
105
2
Related Work
106
The rise of hate speech on social media has
107
prompted substantial initiatives to create annotated
108
datasets for automated hate speech identification.
109
Most existing datasets focus on high-resource lan-
110
guages like English, with popular examples in-
111
cluding the Stormfront dataset (de Gibert et al.,
112
2018), HateEval (Basile et al., 2019), and Large
113
Scale Crowdsourcing and Characterization of Twit-
114
ter Abusive corpus (Founta et al., 2018). These
115
datasets have supported progress in NLP for auto-
116
matic hate speech detection by providing annotated
117
examples that differentiate hate speech, offensive
118
speech, and neutral speech. Similar efforts have
119
been made in other languages, including Hindi
120
(Bohra et al., 2018), Arabic (Mubarak et al., 2017),
121
and Spanish (Romim et al., 2020). However, most
122
existing datasets are domain-specific or limited in
123
diversity, often neglecting linguistic and cultural
124
nuances. Additionally, there is a growing recogni-
125
tion of the need for multilingual datasets to address
126
hate speech in diverse linguistic contexts (Chhabra
127
and Vishwakarma, 2023). For instance, the Mul-
128
tilingual HateCheck (MHC) (Röttger et al., 2022)
129
covers functionalities across ten languages, provid-
130
ing a benchmark for evaluating hate speech detec-
131
tion models. Additionally, the LAHM (Yadav et al.,
132
2023) dataset offers a large annotated resource for
133
multi-domain and multilingual hate speech iden-
134
tification, encompassing languages such as En-
135
2

## Page 3

Figure 2: Sample keywords with their English code and meaning used for data collection. The English Code and
English Translation are not part of the dataset and are provided as examples only.
glish, Hindi, Arabic, French, German, and Spanish.
136
Yet, most of these benchmarks don’t include low-
137
resource languages as creating hate speech datasets
138
in low-resource languages remains a significant
139
challenge due to the lack of language resources,
140
annotator expertise, and linguistic diversity.
141
In the context of Nepali, there has been limited
142
work on building annotated datasets for hate speech
143
detection. A notable effort is the dataset by Thapa
144
et al. (2023), which comprises over 13,000 tweets
145
collected during elections, focusing on political dis-
146
course. Most existing work for automated Nepali
147
hate speech detection utilizes this dataset (Purbey
148
et al., 2024). While this dataset provides a large-
149
scale resource, its scope is restricted to political
150
hate speech, making it less suitable for general
151
hate speech detection. Another resource is the
152
list of offensive keywords compiled by Niraula
153
et al. (2022), which serves as a lexicon for identify-
154
ing hate speech but lacks the annotated contextual
155
data required for supervised learning. These limi-
156
tations highlight the need for a diverse, richly an-
157
notated dataset that captures various forms of hate
158
speech beyond political contexts. Our dataset ad-
159
dresses this gap by focusing on offensive and hate-
160
ful slurs, providing annotations for hate speech, its
161
categories, targets, and offensive speech, enabling
162
more nuanced hate speech detection in Nepali.
163
3
Dataset: NepX-Hate
164
We introduce NepX-Hate, a multilingual bench-
165
mark dataset for hate speech detection in low-
166
resource South Asian languages, primarily Nepali
167
and Hindi. The dataset consists of 10,621 tweets,
168
each annotated across multiple dimensions to sup-
169
port fine-grained hate speech classification, soci-
170
olinguistic analysis, and cross-lingual modeling.
171
3.1
Data Collection and Preprocessing
172
We crawled over 20,000 tweets using X’s advanced
173
search functionality with a manually curated list of
174
145 offensive and hate-indicative keywords sourced
175
from online discourse. To ensure linguistic cover-
176
age and diversity, keywords targeted expressions
177
related to caste, religion, gender, ethnicity, and na-
178
tionality. Data was collected over a three-month
179
period, filtered for duplicates, cleaned of metadata,
180
and deduplicated post-annotation for quality con-
181
trol. The data was collected from publicly available
182
tweets using a keyword-based search approach with
183
the help of a web driver (Selenium, 2023). A small
184
sample of such keywords with their English code
185
and translation is shown in Figure 2. Embedded
186
information in tweets, such as links, URLs, hash-
187
tags, mentions, and user-specific information, were
188
cleaned. Records with null values as tweets, were
189
removed. Identical tweets were removed after data
190
cleaning, resulting in unique records only. Hindi
191
and Nepali languages both utilize the Devanagari
192
script and share many words. Language filtering
193
was performed using the fastText classifier (Joulin
194
et al., 2016), and manual verification. Subsequent
195
analysis and experiments in this paper primarily
196
focus on the Nepali subset due to the completeness
197
of annotations and as a primary contribution.
198
3.2
Annotation Schema
199
Annotations were conducted by native Nepali-
200
speaking linguists using a detailed guideline man-
201
ual. A subset of 500 samples was jointly annotated
202
for agreement analysis (results in-progress). The
203
hindi subset was annotated by native hindi speakers.
204
Each tweet is labeled across six dimensions:
205
• Hate_Label (Binary): Whether the tweet
206
constitutes hate speech (yes/no), guided by
207
the United Nations’ definition (UN, 2019).
208
• Hate_Category (Multilabel): One or more
209
of ten predefined categories: casteism, sex-
210
ism, racism, xenophobia, religious intoler-
211
ance, body shaming, ableism, homophobia,
212
others, none. others include personal attacks,
213
violent speech, attacks based on class, etc.
214
3

## Page 4

• Target (Multiclass): The group targeted: in-
215
dividual, community, organization, country,
216
none.
217
• Offensiveness (Binary): Whether the tweet
218
contains offensive or abusive language.
219
• Sentiment (Single-label): General sentiment
220
as perceived from the tweet: positive, negative,
221
neutral.
222
• Language (ne/hi): Identified language for
223
each tweet.
224
All tweets were stripped of personally identifiable
225
information (PII), usernames, and links. Sensitive
226
tokens like names and countries were replaced with
227
neutral placeholders.
228
3.3
Annotation Agreement
229
To evaluate label consistency, we conducted inter-
230
annotator agreement (IAA) analysis on a subset of
231
500 tweets, evenly split between Nepali and Hindi,
232
annotated by six native speakers for Nepali and
233
three native speaker for Hindi. For single-label
234
tasks, we report Fleiss’ Kappa and for multilabel
235
category annotations, we report average pairwise
236
Jaccard similarity.
237
Label Type
Nepali (K / Jaccard)
Hindi (K / Jaccard)
Hate Speech (Binary)
0.845
0.822
Offensive (Binary)
0.919
0.879
Target (Multiclass)
0.897
0.887
Sentiment (Multiclass)
0.919
0.918
Category (Multilabel)
0.228
0.279
Table 1: Inter-annotator agreement scores by language.
K denotes Fleiss’ Kappa for single-label tasks and Jac-
card denotes average pairwise agreement for multilabel
annotations.
The high agreement across tasks suggests strong
238
label reliability, especially in offensive and senti-
239
ment categories. While category-level agreement
240
is lower, this reflects the inherent subjectivity and
241
intersectionality of hate speech, which often spans
242
multiple overlapping categories. These findings
243
support the dataset’s robustness and suitability for
244
both classification and sociolinguistic analysis.
245
3.4
Dataset Composition
246
The dataset underwent a final round of preprocess-
247
ing to ensure consistency:
248
• Removal of newline characters, excessive
249
white spaces, and special characters.
250
• Removal of residual non-Nepali words and
251
numbers that added no context to tweets
252
• Standardization of punctuation to maintain
253
uniformity
254
• Manual check correction of spellings and any
255
privacy issues across the entire dataset
256
Removal of PII resulted in many tweets with iden-
257
tical speech. Tweets with duplicate meanings were
258
removed, resulting in a refined dataset of 10621
259
high-quality tweets. Out of the full dataset, 3,448
260
tweets are labeled as hate speech, with 7,173 la-
261
beled as non-hate. Nepali tweets constitute the
262
majority of hate content (2,784 of 3,448).
263
Language
Total Tweets
Hate Tweets (%)
Nepali (ne)
7,428
2,784 (37.5%)
Hindi (hi)
3,193
664 (20.8%)
Table 2: Language-wise hate speech distribution in
NepX-Hate.
The Nepali subset is split into train (5,942), val-
264
idation (743), and test (743) sets for supervised
265
experiments. All experiments in this paper are con-
266
ducted on this partition unless otherwise noted.
267
3.5
Potential Applications
268
NepX-Hate provides a critical resource for NLP
269
research in low-resource languages. It is designed
270
to support a wide range of potential usages and
271
applications, including but not limited to:
272
• Hate Speech Detection Models: The dataset
273
serves as a foundational resource for train-
274
ing and evaluating machine learning and deep
275
learning models for automatic hate speech and
276
offensive language detection in Nepali.
277
• Linguistic and Cultural Analysis:
Re-
278
searchers can use the dataset to study linguis-
279
tic patterns, cultural nuances, and the preva-
280
lence of hate speech in Nepali social media
281
discourse, providing insights into societal atti-
282
tudes and behavior.
283
• Hate Speech Category Detection:
The
284
dataset can be utilized for training and eval-
285
uating deep learning models and fine-tuning
286
language models for detecting sub-categories
287
of hate speech in the Nepali language.
288
4

## Page 5

Figure 3: category frequency per language for hate
speech true cases only
• Cross-Lingual and Multilingual Studies:
289
NepX-Hate can be integrated with hate speech
290
datasets from other languages to develop
291
cross-lingual models, enabling hate speech
292
detection in multilingual or code-mixed envi-
293
ronments.
294
• Policy and Content Moderation: The dataset
295
can aid policymakers, NGOs, and social me-
296
dia platforms in understanding and address-
297
ing hate speech, contributing to the develop-
298
ment of localized content moderation tools
299
and strategies.
300
• Creation of Dataset for Other Languages:
301
The methodologies employed in collecting,
302
annotating, and preprocessing NepX-Hate can
303
serve as a blueprint for creating similar high-
304
quality hate speech datasets in other low-
305
resource languages. Researchers can adapt
306
these approaches to address linguistic and cul-
307
tural nuances in different contexts.
308
4
Exploratory Data Analysis
309
To better understand the linguistic and structural
310
properties of NepX-Hate, we conduct exploratory
311
analysis across the dataset’s key dimensions: la-
312
bel distribution, lexical characteristics, sentence
313
structure, and category co-occurrence. These in-
314
sights offer context for the modeling challenges
315
and inform downstream experimental design.
316
4.1
Label Distribution
317
The dataset is moderately imbalanced across the
318
hate and offensive labels. Of the 10,621 tweets,
319
3,448 (32.5%) are labeled as hate speech, while
320
7,173 are non-hate. Offensive speech is more preva-
321
lent, covering 75.74% of the data, with a strong
322
overlap observed between hate and offensive labels.
323
Figure 4: Sample count per word length in the dataset
Figure 5: Sentence length per hate label in the dataset
As shown in Figure 3, category-wise distributions
324
are skewed: others, casteism, racism, and sexism
325
dominate, while categories such as ableism and
326
homophobia are rare. This suggests severe class
327
imbalance, posing challenges for categorical and
328
multi-label modeling. Caste-based hate dominates
329
Nepali tweets, while communal hate is more com-
330
mon in Hindi.
331
4.2
Lexical and Length Analysis
332
We observe notable structural differences in sen-
333
tence length by hate label. Hate tweets are gen-
334
erally longer (median 20 tokens) than non-hate
335
tweets (median 16.8), as shown in Figure 5. Fig-
336
ure 4, showing the distribution of texts by word
337
counts for both Hindi and Nepali language. Word
338
clouds show stark lexical distinctions between hate
339
and non-hate tweets, particularly for caste-based
340
and gendered slurs.
341
5

## Page 6

Figure 6: Target distribution in the dataset
Figure 7: Co-occurrence matrix for hate speech cate-
gories
4.3
Target and Sentiment Analysis
342
Most hateful tweets target individuals (61.3%),
343
followed by communities (29.7%), as visualized
344
in Figure 6. Organization and country-level hate
345
is rare, but often politically charged. Sentiment
346
patterns suggest a strong alignment between hate
347
speech and negative sentiment, although sarcasm
348
and implicit hate complicate this correlation.
349
4.4
Hate Category Co-occurrence
350
We observe substantial co-occurrence between cer-
351
tain hate categories. Figure 7 shows strong co-
352
occurrence between certain categories, especially
353
xenophobia, and racism. This complexity high-
354
lights the importance of multilabel modeling over
355
simplistic single-label classification frameworks
356
and motivates the inclusion of multitask setups in
357
our experiments.
358
5
Experiments and Baselines
359
We conduct a series of experiments to evaluate the
360
effectiveness of NepX-Hate for hate speech detec-
361
tion under various modeling paradigms. Our evalu-
362
ation includes binary classification and a multitask
363
setup, both of which serve as strong baselines for
364
future research. We use the Nepali subset of NepX-
365
Hate (7,428 tweets) for all experiments. The data is
366
split into training (5,942), validation (743), and test
367
(743) sets using stratified sampling on the binary
368
hate label. All models are trained and evaluated on
369
the same splits for comparability. We report Accu-
370
racy, Precision, Recall, and F1-Score for all tasks.
371
For multitask settings, evaluation is performed per
372
task (e.g., hate detection, category classification),
373
and macro-averaged metrics are reported for multi-
374
label outputs.
375
5.1
Binary Hate Speech Classification
376
We benchmark a range of models for binary hate
377
speech detection, including traditional classifiers,
378
neural architectures, and multilingual transform-
379
ers. Traditional models use TF-IDF vectorization
380
(word-level, unigrams and bigrams), followed by
381
classification using Logistic Regression (LR), Sup-
382
port Vector Machines (SVM), Naive Bayes (NB),
383
Random Forests (RF), and XGBoost.
GRU is
384
trained with XLM Roberta Embeddings. Trans-
385
former models (mBERT (Devlin et al., 2019),
386
XLM-R (Conneau et al., 2020) , MuRIL (Khanuja
387
et al., 2021), IndicBERTv2 (Doddapaneni et al.,
388
2023)) are fine-tuned using Pytorch custom trainer.
389
GPT-4o-mini (OpenAI et al., 2024) and Gemini
390
(Team, 2025) are evaluated via zero-shot prompt-
391
ing on the test set. Full hyperparameter details are
392
provided in the Appendix.
393
Table 3 shows the results for all the models in
394
the binary hate detection task. Transformer mod-
395
els outperform traditional baselines, with mBERT
396
and IndicBERT V2 achieving the highest F1 scores.
397
GPT-4o-mini and Gemini, while zero-shot, perform
398
competitively but underperform compared to fine-
399
tuned models. Surprisingly, simpler models like
400
Linear Regression, Naive Bayes and SVM also per-
401
form competitively. However, none of the baseline
402
crosses a score of 80% for any metric, showing
403
the challenge of detecting implicit hate speech in
404
6

## Page 7

Mode
Accuracy
Precision
Recall
F1
Linear Regression
0.705
0.685
0.686
0.686
Naive Bayes
0.720
0.702
0.682
0.687
Support Vector Machine
0.708
0.693
0.702
0.696
Random Forest
0.692
0.702
0.611
0.603
XGBoost
0.703
0.685
0.651
0.656
Gated Recurrent Unit (GRU)
0.717
0.697
0.686
0.690
mBERT
0.758
0.747
0.721
0.729
XLM Roberta
0.732
0.715
0.718
0.716
Muril
0.734
0.716
0.718
0.717
IndicBERT V2
0.740
0.722
0.717
0.720
Gemma3-1b-it
0.598
0.583
0.587
0.583
Gemma3-4b-it
0.659
0.650
0.659
0.649
Gemma3-12b-it
0.701
0.682
0.652
0.657
GPT4o-mini
0.693
0.680
0.688
0.681
Gemini-2.5-flash-preview
0.703
0.714
0.727
0.700
Table 3: Performance of different models for binary classification task of hate speech detection
Nepali language.
405
5.2
Multiclass Category Classification
406
We evaluate traditional machine learning models on
407
the task of multilabel hate category classification
408
using TF-IDF features and One-vs-Rest classifiers.
409
As shown in Table 4, Naive Bayes achieves the
410
highest micro-F1 (0.605), while Logistic Regres-
411
sion leads on macro-F1 (0.410), indicating better
412
performance across imbalanced classes. However,
413
all models struggle with class sparsity and low sup-
414
port categories, highlighting the challenge of fine-
415
grained hate classification in low-resource settings.
416
Model
Micro-F1
Macro-F1
Naive Bayes
0.605
0.151
Logistic Regression
0.587
0.410
Linear SVM
0.567
0.369
Table 4: Multilabel hate category classification results
using traditional models. Scores are reported on the test
set using One-vs-Rest classification and macro/micro-
averaged F1 metrics.
5.3
Multitask Classification
417
To capture the interdependence between hate pres-
418
ence and its categorical expression, we adopt a
419
multitask learning setup using BERT-based mod-
420
els. Hate speech is treated as a single-label task,
421
while category prediction is modeled as multilabel
422
classification. As shown in Table 5, multitask mod-
423
els consistently outperform their single-task coun-
424
terparts in binary hate detection. IndicBERTv2
425
shows the largest improvement, with F1 rising
426
from 0.720 to 0.752 and accuracy from 0.740 to
427
0.764. mBERT also benefits modestly, with F1 in-
428
creasing from 0.729 to 0.740. These gains suggest
429
that auxiliary category supervision enhances the
430
model’s ability to identify implicit or coded hate.
431
Our findings echo broader multitask NLP research,
432
reinforcing that structured, semantically aligned la-
433
bels can guide learning in resource-scarce settings,
434
where each additional signal can meaningfully im-
435
prove generalization and robustness. The perfor-
436
mance gains observed across most models under-
437
score the importance of designing multi-objective
438
benchmarks in under-resourced language contexts,
439
where each additional signal can play a dispropor-
440
tionate role in improving robustness.
441
5.4
Interpretability
442
To assess how multitask learning influences model
443
interpretability and token attribution, we apply
444
SHAP (Lundberg and Lee, 2017) to compare token-
445
level importance in binary hate classification for
446
both the multitask and single-task versions of In-
447
dicBERTv2. Figure 8 shows force plots for the
448
same Nepali sentence. This example contains im-
449
plicit hate expressions and was correctly classi-
450
fied as hateful by both models. The multitask In-
451
dicBERTv2 assigns a high probability of 0.934 to
452
the hate class. It attributes the decision to a com-
453
bination of hateful terms, while still factoring in
454
structural tokens and conjunctions. This shows
455
a more balanced attribution, where both harmful
456
7

## Page 8

Model
Binary F1 (macro)
Binary Acc.
Category F1 (macro)
Category F1 (weighted)
Category Acc.
IndicBERTv2-MLM-only
0.752
0.764
0.256
0.670
0.700
mBERT (bert-base-multilingual-cased)
0.740
0.756
0.251
0.674
0.704
MuRIL (google/muril-base-cased)
0.698
0.746
0.145
0.562
0.646
XLM-RoBERTa (xlm-roberta-base)
0.728
0.743
0.126
0.551
0.637
Table 5: Multitask classification performance across models. Binary classification is evaluated using macro F1 and
accuracy. Hate category classification is evaluated using macro/weighted F1 and accuracy on single-label prediction
(most prominent category).
(a) Multitask IndicBERTv2 (confidence = 0.934)
(b) Single-task IndicBERTv2 (confidence = 0.784)
Figure 8: SHAP interpretability comparison of multitask vs. single-task IndicBERTv2 on the same Nepali hate
speech example.
and contextual tokens are used in decision-making.
457
In contrast, the single-task IndicBERTv2 yields a
458
lower probability of 0.784 for the same example.
459
While it identifies some of the same toxic tokens, it
460
shows a narrower focus on fewer tokens, potentially
461
indicating lower contextual sensitivity.
462
6
Discussion
463
Our findings underscore the multifaceted challenge
464
of hate speech detection in Nepali, a morphologi-
465
cally rich and under-resourced language. Even ad-
466
vanced transformer models struggle with implicit
467
or culturally embedded hate, particularly when
468
tweets rely on sarcasm, indirect language, or po-
469
litical euphemisms rather than overtly hateful ex-
470
pressions. These challenges are exacerbated by the
471
use of regional slurs, code-mixed phrasing, and
472
culturally specific idioms, all of which make it dif-
473
ficult for models trained solely on lexical features
474
to generalize effectively. NepX-Hate’s inclusion of
475
sentiment, offensiveness, and target type provides
476
valuable auxiliary signals, helping models to con-
477
textualize hate more effectively.
478
Multitask learning further enhances model perfor-
479
mance by enabling shared representations across
480
interrelated labels such as hate category and tar-
481
get group.
This leads not only to quantitative
482
gains—especially in recall—but also to improved
483
interpretability, allowing systems to answer not
484
just what was said, but who was targeted and
485
why. The dataset’s fine-grained annotations ex-
486
pose the intersectional nature of hate, with fre-
487
quent co-occurrence of categories like casteism
488
and xenophobia, motivating the use of multilabel
489
frameworks over binary ones. Beyond classifica-
490
tion, NepX-Hate opens up avenues for sociocul-
491
tural analysis, fairness testing, and cross-lingual
492
adaptation, particularly between Nepali and Hindi.
493
Its design offers a replicable blueprint for creating
494
ethically grounded, multi-aspect datasets in other
495
low-resource contexts.
496
7
Conclusion
497
The Nepali X Hate Speech Dataset (NepX-Hate)
498
represents a significant step forward in enabling
499
automated hate speech detection for low-resource
500
languages. With 7,000 annotated Nepali tweets,
501
the dataset provides a diverse and high-quality re-
502
source that captures hate speech, offensive speech,
503
and targets, along with granular subcategories for
504
hate speech classification. Our work highlights the
505
potential for advancing natural language processing
506
in Nepali for societal computation and contributes
507
to broader efforts in developing multilingual and
508
culturally aware AI systems.
509
By addressing key challenges such as linguistic
510
nuances, privacy concerns, and bias mitigation,
511
NepX-Hate sets a foundation for future research in
512
hate speech detection for Nepali and similar low-
513
resource languages. We anticipate that this dataset
514
will not only support academic advancements but
515
also foster the development of practical applica-
516
tions to counter online hate speech effectively.
517
8

## Page 9

Ethical Considerations
518
Curating datasets from publicly available data or
519
user-posted data should always adhere to ethical
520
guidelines and principles. We prioritized ethical
521
principles throughout the dataset creation process
522
to ensure compliance with privacy, fairness, and
523
transparency standards. All personally identifiable
524
information (PII), such as usernames, handles, and
525
profile links, as well as personal names, contacts,
526
and identities embedded in tweets, were either re-
527
placed or removed entirely. This ensures that the
528
dataset cannot be used to trace back to any individ-
529
uals, maintaining the anonymity of the users whose
530
tweets were collected. All collected tweets were
531
available in the public space, and no personal or
532
followers-only tweets were collected. PII of targets
533
in hate speech were also replaced with placehold-
534
ers.
535
To create a comprehensive dataset that addresses
536
general hate speech prevalent in the Nepalese on-
537
line community, efforts were made to mitigate bi-
538
ases and address multiple facets of hate speech dur-
539
ing data collection and annotation. Keywords used
540
for data collection spanned various categories of
541
hate speech, reducing the risk of dataset skewness
542
and narrow specificity. To ensure fairness during
543
annotation, annotators followed a structured set of
544
instructions to ensure consistent labeling across di-
545
verse types of content.
546
The dataset is intended for academic and research
547
purposes only, with the goal of improving hate
548
speech detection systems and analyzing the trends
549
of social media usage in the Nepali language.
550
While we hope that this effort can be a foundation
551
for future developments in content moderation sys-
552
tems for Nepali and other low-resource languages,
553
the dataset is not a strict basis for surveillance,
554
punitive measures, or other potentially harmful ap-
555
plications. Researchers using the dataset or collec-
556
tion steps advised here are encouraged to adhere
557
to ethical AI practices, including transparency and
558
accountability in their work.
559
Potential Risk:
Due to the subjective and
560
context-sensitive nature of hate speech, there is a
561
risk that models trained on this dataset may produce
562
biased or culturally insensitive predictions if de-
563
ployed without proper oversight. Misuse could lead
564
to over-censorship, mislabeling of critical speech,
565
or marginalization of certain dialects or commu-
566
nities.
Therefore, researchers and practitioners
567
are strongly encouraged to adhere to ethical AI
568
practices, including fairness auditing, transparency,
569
and human-in-the-loop validation when using this
570
dataset or derivative tools.
571
Limitations
572
Despite the extensive efforts made to ensure the
573
quality and utility of NepX-Hate, several limita-
574
tions remain, which should be considered when
575
using the dataset for research or practical applica-
576
tions:
577
Datase Size
578
While the dataset contains 7,000 high-quality an-
579
notated tweets, this size may or may not be suf-
580
ficient for training large-scale deep learning mod-
581
els or generalizing to all forms of hate speech en-
582
countered in real-world scenarios. We believe the
583
dataset to be capable of fine-tuning rather than train-
584
ing from scratch. The dataset, while diverse, does
585
not yet encompass every possible context or cate-
586
gory of hate speech in Nepali.
587
Domain-Specific Bias
588
The dataset is primarily derived from social media,
589
specifically X. As a result, it may reflect the biases,
590
linguistic patterns, and user demographics of this
591
platform, which could differ from other platforms
592
or offline contexts. This may limit the generaliz-
593
ability of models trained on this dataset to other
594
media of communication.
595
Amibiguity in Annotations
596
Despite providing detailed guidelines to annotators,
597
the subjective nature of hate speech and offensive
598
content classification introduces some level of am-
599
biguity. Certain tweets that fall into a gray area
600
may have been inconsistently labeled, which could
601
impact the performance of models trained on this
602
data for generalization.
603
Limited Context
604
Since the dataset is tweet-based, each sample is lim-
605
ited to a maximum of 280 characters, which may
606
not provide sufficient context to fully understand
607
the intent behind certain statements. Additionally,
608
replies and broader conversational threads are not
609
included, which could affect the accurate classifi-
610
cation of hate speech that depends on context.
611
Continued Refinement
612
The definitions of hate speech are ever-changing
613
and with the person. While we have made sure
614
9

## Page 10

to follow strict guidelines to provide objective an-
615
notation for the data, it may be possible that the
616
definitions might change in the future, and views
617
may differ.
618
Same Modality
619
The dataset exclusively focuses on written content
620
in Nepali and does not include other modalities
621
such as images, videos, or audio that may carry
622
hate speech or offensive content. Multimodal hate
623
speech detection is becoming increasingly impor-
624
tant, and this dataset does not address such use
625
cases.
626
Label Imbalance
627
Certain hate categories — such as ableism and
628
homophobia — are underrepresented, making them
629
challenging for supervised learning. Category co-
630
occurrence and multi-label overlaps add further
631
complexity, requiring specialized loss functions or
632
resampling strategies.
633
References
634
Valerio Basile, Cristina Bosco, Elisabetta Fersini,
635
Debora Nozza, Viviana Patti, Francisco Manuel
636
Rangel Pardo, Paolo Rosso, and Manuela Sanguinetti.
637
2019. SemEval-2019 task 5: Multilingual detection
638
of hate speech against immigrants and women in
639
Twitter. In Proceedings of the 13th International
640
Workshop on Semantic Evaluation, pages 54–63, Min-
641
neapolis, Minnesota, USA. Association for Compu-
642
tational Linguistics.
643
Aditya Bohra, Deepanshu Vijay, Vinay Singh, Syed Sar-
644
faraz Akhtar, and Manish Shrivastava. 2018.
A
645
dataset of Hindi-English code-mixed social media
646
text for hate speech detection. In Proceedings of
647
the Second Workshop on Computational Modeling
648
of People‘s Opinions, Personality, and Emotions in
649
Social Media, pages 36–41, New Orleans, Louisiana,
650
USA. Association for Computational Linguistics.
651
Anusha Chhabra and Dinesh Vishwakarma. 2023. A lit-
652
erature survey on multimodal and multilingual auto-
653
matic hate speech identification. Multimedia Systems,
654
29.
655
Alexis Conneau, Kartikay Khandelwal, Naman Goyal,
656
Vishrav Chaudhary, Guillaume Wenzek, Francisco
657
Guzmán, Edouard Grave, Myle Ott, Luke Zettle-
658
moyer, and Veselin Stoyanov. 2020.
Unsuper-
659
vised cross-lingual representation learning at scale.
660
Preprint, arXiv:1911.02116.
661
Ona de Gibert, Naiara Perez, Aitor García-Pablos, and
662
Montse Cuadros. 2018. Hate Speech Dataset from
663
a White Supremacy Forum. In Proceedings of the
664
2nd Workshop on Abusive Language Online (ALW2),
665
pages 11–20, Brussels, Belgium. Association for
666
Computational Linguistics.
667
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
668
Kristina Toutanova. 2019. Bert: Pre-training of deep
669
bidirectional transformers for language understand-
670
ing. Preprint, arXiv:1810.04805.
671
Sumanth Doddapaneni, Rahul Aralikatte, Gowtham
672
Ramesh, Shreya Goyal, Mitesh M. Khapra, Anoop
673
Kunchukuttan, and Pratyush Kumar. 2023. Towards
674
leaving no Indic language behind: Building monolin-
675
gual corpora, benchmark and models for Indic lan-
676
guages. In Proceedings of the 61st Annual Meeting
677
of the Association for Computational Linguistics (Vol-
678
ume 1: Long Papers), pages 12402–12426, Toronto,
679
Canada. Association for Computational Linguistics.
680
Antigoni-Maria Founta, Constantinos Djouvas, De-
681
spoina Chatzakou, Ilias Leontiadis, Jeremy Black-
682
burn, Gianluca Stringhini, Athena Vakali, Michael
683
Sirivianos, and Nicolas Kourtellis. 2018. Large scale
684
crowdsourcing and characterization of twitter abusive
685
behavior. Preprint, arXiv:1802.00393.
686
Md Saroar Jahan and Mourad Oussalah. 2023. A sys-
687
tematic review of hate speech automatic detection
688
using natural language processing. Neurocomputing,
689
546:126232.
690
Armand Joulin, Edouard Grave, Piotr Bojanowski, and
691
Tomas Mikolov. 2016. Bag of tricks for efficient text
692
classification. arXiv preprint arXiv:1607.01759.
693
Simran Khanuja, Diksha Bansal, Sarvesh Mehtani,
694
Savya Khosla,
Atreyee Dey,
Balaji Gopalan,
695
Dilip Kumar Margam, Pooja Aggarwal, Rajiv Teja
696
Nagipogu, Shachi Dave, Shruti Gupta, Subhash
697
Chandra Bose Gali, Vish Subramanian, and Partha
698
Talukdar. 2021. Muril: Multilingual representations
699
for indian languages. Preprint, arXiv:2103.10730.
700
Scott Lundberg and Su-In Lee. 2017. A unified ap-
701
proach to interpreting model predictions. Preprint,
702
arXiv:1705.07874.
703
Hamdy Mubarak, Kareem Darwish, and Walid Magdy.
704
2017. Abusive language detection on Arabic social
705
media. In Proceedings of the First Workshop on Abu-
706
sive Language Online, pages 52–56, Vancouver, BC,
707
Canada. Association for Computational Linguistics.
708
Nobal B. Niraula, Saurab Dulal, and Diwa Koirala. 2022.
709
Linguistic taboos and euphemisms in nepali. ACM
710
Trans. Asian Low-Resour. Lang. Inf. Process., 21(6).
711
OpenAI, Josh Achiam, Steven Adler, Sandhini Agarwal,
712
Lama Ahmad, Ilge Akkaya, Florencia Leoni Ale-
713
man, Diogo Almeida, Janko Altenschmidt, Sam Alt-
714
man, Shyamal Anadkat, Red Avila, Igor Babuschkin,
715
Suchir Balaji, Valerie Balcom, Paul Baltescu, Haim-
716
ing Bao, Mohammad Bavarian, Jeff Belgum, and
717
262 others. 2024. Gpt-4 technical report. Preprint,
718
arXiv:2303.08774.
719
10

## Page 11

Fabio Poletto, Valerio Basile, Manuela Sanguinetti,
720
Cristina Bosco, and Viviana Patti. 2021. Resources
721
and benchmark corpora for hate speech detection: a
722
systematic review. Language Resources and Evalua-
723
tion, 55(2):477–523.
724
Jebish Purbey,
Siddartha Pullakhandam,
Kanwal
725
Mehreen, Muhammad Arham, Drishti Sharma,
726
Ashay Srivastava, and Ram Mohan Rao Kadiyala.
727
2024. 1-800-shared-tasks @ nlu of devanagari script
728
languages: Detection of language, hate speech, and
729
targets using llms. Preprint, arXiv:2411.06850.
730
Nauros Romim, Mosahed Ahmed, Hriteshwar Talukder,
731
and Md Saiful Islam. 2020. Hate speech detection
732
in the bengali language: A dataset and its baseline
733
evaluation. Preprint, arXiv:2012.09686.
734
Paul Röttger, Haitham Seelawi, Debora Nozza, Zeerak
735
Talat, and Bertie Vidgen. 2022. Multilingual Hate-
736
Check: Functional tests for multilingual hate speech
737
detection models. In Proceedings of the Sixth Work-
738
shop on Online Abuse and Harms (WOAH), pages
739
154–169, Seattle, Washington (Hybrid). Association
740
for Computational Linguistics.
741
Anna Schmidt and Michael Wiegand. 2017. A survey
742
on hate speech detection using natural language pro-
743
cessing. In Proceedings of the Fifth International
744
Workshop on Natural Language Processing for So-
745
cial Media, pages 1–10, Valencia, Spain. Association
746
for Computational Linguistics.
747
Selenium. 2023. Selenium: Web browser automation.
748
https://www.selenium.dev/. Accessed: 2025-01-
749
16.
750
Gemini Team. 2025. Gemini: A family of highly capa-
751
ble multimodal models. Preprint, arXiv:2312.11805.
752
Surendrabikram Thapa, Kritesh Rauniyar, Shuvam Shi-
753
wakoti, Sweta Poudel, Usman Naseem, and Mehwish
754
Nasim. 2023.
NEHATE: Large-Scale Annotated
755
Data Shedding Light on Hate Speech in Nepali Local
756
Election Discourse.
757
United
Nations
UN.
2019.
United
nations
758
strategy and plan of action on hate speech.
759
https://www.un.org/en/hate-speech/
760
un-strategy-and-plan-of-action-on-hate-speech.
761
[Accessed 15-01-2025].
762
Bertie Vidgen and Leon Derczynski. 2021. Directions
763
in abusive language training data, a systematic re-
764
view: Garbage in, garbage out. PLOS ONE, 15(12):1–
765
32.
766
Joseph B. Walther. 2022. Social media and online hate.
767
Current Opinion in Psychology, 45:101298.
768
Ankit Yadav, Shubham Chandel, Sushant Chatufale,
769
and Anil Bandhakavi. 2023. Lahm : Large anno-
770
tated dataset for multi-domain and multilingual hate
771
speech identification. Preprint, arXiv:2304.00913.
772
11

## Page 12

A
Detailed Results
773
The tables list the results of the baselines:
Model
Class
Precision
Recall
F1-score
Logistic Regression
non-hate
0.85
0.88
0.86
Logistic Regression
hate
0.78
0.74
0.76
Logistic Regression
Macro Avg
–
–
0.81
Linear SVM
non-hate
0.87
0.89
0.88
Linear SVM
hate
0.80
0.76
0.78
Linear SVM
Macro Avg
–
–
0.83
Naive Bayes
non-hate
0.82
0.86
0.84
Naive Bayes
hate
0.71
0.65
0.68
Naive Bayes
Macro Avg
–
–
0.76
Table 6: Evaluation metrics for traditional machine
learning models using TF-IDF features on hate speech
classification.
774
Class
Precision
Recall
F1-score
Support
Non-hate (0)
0.756
0.811
0.782
465
Hate (1)
0.639
0.561
0.598
278
Accuracy
0.717
Macro Avg
0.697
0.686
0.690
743
Weighted Avg
0.712
0.717
0.713
743
Table 7: Performance metrics of the GRU model on the
hate speech dataset. Best threshold used: 0.65.
Model
Accuracy
Macro F1
Non-hate F1
Hate F1
Weighted F1
GRU
0.717
0.690
0.782
0.598
0.713
IndicBERTv2
0.764
0.752
0.808
0.696
0.766
BERT-multilingual-cased
0.756
0.740
0.805
0.676
0.757
MuRIL-base-cased
0.746
0.698
0.818
0.579
0.728
XLM-Roberta-base
0.743
0.728
0.791
0.665
0.744
Table 8: Performance comparison for binary hate speech
classification across different models.
12

## Page 13

Hate Category
IndicBERTv2
BERT-multilingual-cased
MuRIL-base-cased
XLM-Roberta-base
Racism
0.607
0.662
0.385
0.443
Sexism
0.154
0.000
0.000
0.000
Casteism
0.608
0.627
0.260
0.000
Religious Intolerance
0.000
0.000
0.000
0.000
Body Shaming
0.000
0.000
0.000
0.000
Xenophobia
0.000
0.000
0.000
0.000
Ableism
0.000
0.000
0.000
0.000
Homophobia
0.000
0.000
0.000
0.000
Others
0.368
0.404
0.000
0.000
Table 9: Model-wise F1 scores for individual hate
speech categories.
13

## Page 14

Table 10: Comparison of Model Performance Metrics
2*Model
Class "no"
Class "yes"
Precision
Recall
F1
Support
Precision
Recall
F1
Support
bert-base-multilingual-cased
0.774
0.867
0.817
465
0.721
0.576
0.640
278
xlm-roberta-base
0.793
0.774
0.783
465
0.637
0.662
0.649
278
google/muril-base-cased
0.791
0.781
0.786
465
0.641
0.655
0.648
278
ai4bharat/IndicBERTv2-MLM-only
0.783
0.809
0.796
465
0.662
0.626
0.643
278
Table 11: Overall Model Performance Metrics
Model
Accuracy
Macro Avg
Weighted Avg
Precision
Recall
Precision
Recall
F1
bert-base-multilingual-cased
0.758
0.747
0.721
0.754
0.758
0.751
xlm-roberta-base
0.732
0.715
0.718
0.734
0.732
0.733
google/muril-base-cased
0.734
0.716
0.718
0.735
0.734
0.734
ai4bharat/IndicBERTv2-MLM-only
0.740
0.722
0.717
0.738
0.740
0.739
14

```
