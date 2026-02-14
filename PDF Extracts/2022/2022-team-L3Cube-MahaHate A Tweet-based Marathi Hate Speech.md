---\ntitle: "2022-team-L3Cube-MahaHate A Tweet-based Marathi Hate Speech - PDF Extract"\nsource_pdf: "2022-team-L3Cube-MahaHate A Tweet-based Marathi Hate Speech.pdf"\npages: 12\nextracted_at: "2026-02-14T06:21:39"\n---\n\n# PDF Extract: 2022-team-L3Cube-MahaHate A Tweet-based Marathi Hate Speech\n\n**Source PDF:** 2022-team-L3Cube-MahaHate A Tweet-based Marathi Hate Speech.pdf\n**Total Pages:** 12\n\n---\n\n## Content\n\n```\n--- Page 1 ---\n\nL3Cube-MahaHate: A Tweet-based Marathi
Hate Speech Detection Dataset and BERT
models⋆
Abhishek Velankar1,3, Hrushikesh Patil1,3, Amol Gore1,3, Shubham Salunke1,3,
and Raviraj Joshi2,3
1 Pune Institute of Computer Technology, Pune, Maharashtra India
2 Indian Institute of Technology Madras, Chennai, Tamilnadu India
3 L3Cube Pune
{velankarabhishek,hrushi2900,amolgore960,shubhamsalunke30012001}@gmail.com,
ravirajoshi@gmail.com
Abstract. Social media platforms are used by a large number of people
prominently to express their thoughts and opinions. However, these plat-
forms have contributed to a substantial amount of hateful and abusive
content as well. Therefore, it is important to curb the spread of hate
speech on these platforms. In India, Marathi is one of the most popular
languages used by a wide audience. In this work, we present L3Cube-
MahaHate, the ﬁrst major Hate Speech Dataset in Marathi. The dataset
is curated from Twitter, annotated manually. Our dataset consists of
over 25000 distinct tweets labeled into four major classes i.e hate, of-
fensive, profane, and not. We present the approaches used for collecting
and annotating the data and the challenges faced during the process. Fi-
nally, we present baseline classiﬁcation results using deep learning models
based on CNN, LSTM, and Transformers. We explore mono-lingual and
multi-lingual variants of BERT like MahaBERT, IndicBERT, mBERT,
and xlm-RoBERTa and show that mono-lingual models perform better
than their multi-lingual counterparts. The MahaBERT model provides
the best results on L3Cube-MahaHate Corpus. The data and models are
available at https://github.com/l3cube-pune/MarathiNLP
Keywords: Hate Speech Detection · Marathi Dataset · Marathi NLP ·
Transformers · MahaBERT
1
Introduction
In the past decade, there has been an expeditious rise in the popularity of on-
line social media platforms all over the globe. People have become more open
to sharing their opinions without thinking excessively. This often leads to the
spread of hate or oﬀensive speech thereby causing violence and cyberbullying.
⋆Supported by L3Cube Pune
arXiv:2203.13778v2  [cs.CL]  22 May 2022

--- Page 2 ---\n\n2
A. Velankar et al.
Hate speech is a kind of abusive language directed towards a community that is
underprivileged in terms of race, gender, ethnic origin, disability, etc., or can be
an insult or threat to an individual [21,23]. The users often defy the boundaries
of freedom of speech without even realizing it by posting harmful messages and
comments [28]. Therefore it is today’s need to neutralize these activities from
proliferating further.
In this work, we consider hate speech detection in the Marathi language, a
regional language in India, spoken by over 83 million people across the country
[17]. Despite being one of the popular languages in India, work in the area of
hate speech detection in Marathi is extremely limited [22,27,14,3] as compared
to other languages [8,25,6,26]. Even general text classiﬁcation in Marathi has
received limited attention [19,20]. In this paper, we present, L3Cube-MahaHate
Corpus, the largest publicly available hate speech dataset in Marathi. The dataset
is collected from Twitter, tagged with four ﬁne-grained labels which are deﬁned
as follows -
Hate (HATE): A Twitter post abusing a speciﬁc group of people or commu-
nity based on their religion, race, ethnic origin, gender, geographical location,
etc. stimulating violent behaviors.
Oﬀensive (OFFN): A tweet containing harmful language leading to insulting
or dehumanizing, at times threatening a particular individual.
Profane (PRFN): A tweet including the use of typical swear words or profane,
cursing language which is ordinarily insupportable.
Not (NOT): A post that does not contain any insulting or abusive content
or profane words and appears normal in terms of the language used.
The dataset consists of over 25000 samples tagged manually with the classes
explained above. We further provide an extensive study of the data collection
approaches, diﬀerent policies used, and challenges faced during the annotation
process as well. We also provide the statistical analysis of our dataset along with
the distribution of train, test, and validation data. Lastly, we perform multiple
experiments to evaluate state-of-the-art deep learning models on the dataset and
provide the baseline results to the community.
The MahaBERT model ﬁned-tuned on L3Cube-MahaHate is termed as MahaHate-
BERT45 and is shared publicly on model hub. All the resources are publicly
shared on github6.
4 https://huggingface.co/l3cube-pune/mahahate-bert
5 https://huggingface.co/l3cube-pune/mahahate-multi-roberta
6 https://github.com/l3cube-pune/MarathiNLP

--- Page 3 ---\n\nL3Cube-MahaHate: A Marathi Hate Speech Detection Dataset
3
2
Related Work
Hate speech detection is considered to be a highly critical problem and a lot of
attempts have been made to control it. A signiﬁcant amount of work can be seen
in English text analysis. But recently, eﬀorts have been made towards widening
the research in regional languages like Marathi as well.
[11] presented the Marathi Oﬀensive Language Dataset (MOLD), with nearly
2,500 annotated tweets labeled as oﬀensive and not oﬀensive. It is considered
the ﬁrst dataset for oﬀensive language identiﬁcation in Marathi. Also, they eval-
uated the performance of several traditional machine learning models and deep
learning models (e.g. LSTM) trained on MOLD.
[2] collected over 8200 hostile and non-hostile Hindi text samples from multi-
ple social media platforms like Twitter, Facebook, WhatsApp. Hostile posts were
further extended into fake, defamation, hate, and oﬀensive. Total 8192 posts were
collected and tested on various machine learning models using mBERT encoding.
A Hindi-English code-mixed corpus was constructed in [4] using the tweets
posted online for the duration of ﬁve years. Tweets were scrapped using Twitter
python API by selecting certain hashtags and keywords from political events,
public protests, riots, etc. After removing noisy samples a dataset of 4575 code-
mixed tweets was created. The experiments were performed with SVM and Ran-
dom Forest algorithms along with character and word N-gram features.
In [20] authors presented a dataset containing over 16000 Marathi tweets, man-
ually tagged in three classes namely positive, negative and neutral. They also
provided a policy for tagging sentences by their sentiment. Analysis was per-
formed on CNN, BiLSTM, and BERT models.
[7] collected hate phrases identiﬁed by Hatebase.org, then used those phrases
to collect English tweets from Twitter using Twitter API. The ﬁnal set of 25k
tweets was annotated by CrowdFlower workers with labels hate, oﬀensive and
neither. This dataset was then tested on Logistic Regression, Naive Bayes, De-
cision Trees, random forests, and linear SVMs.
In [13], the authors evaluated the eﬀect of ﬁltering the generated data used
for Data Augmentation (DA). This demonstrates up to 7.3% and up to 25% of
relative improvements on macro-averaged F1 on two widely used hate speech
corpora.
[1] proposed a hypothesis that there exists a relation between fake messages
or rumors and sentiments of the texts posted online. The experiments were per-
formed on the standard Twitter fake news dataset and showed good improvement
on the same.

--- Page 4 ---\n\n4
A. Velankar et al.
[12] provided an annotated corpus of hate speech with the context informa-
tion. This evaluates by using logistic regression and neural network models for
hate speech detection around 3% and 4%, and it improves to 7% by combining
these two models together.
[24] presented MIMCT to detect oﬀensive(Hate or Abusive) Hinglish tweets from
the proposed Hinglish Oﬀensive Tweet dataset. Demonstrated the use of the
multi-channel CNN-LSTM model for sentiment analysis.
3
Dataset Creation
3.1
Collection
We created the Hate Speech dataset using the tweets posted online by diﬀer-
ent users across the Maharashtra region considering the period of over the last
5 years. There are plenty of diﬀerent python libraries available such as Twint,
GetOldTweets, Snscrape, etc. which can be used to collect Twitter posts. Twit-
ter provides its own API as well. We used the Twint python library for scraping
the tweets.
To obtain the hateful tweets, ﬁrstly, we created a list of over 150 bad words
in Marathi which are predominantly used by online users to spread hostility.
Some of these are typical swear words in Marathi and other oﬀensive words.
These words were in Marathi Devanagari script as we are not concerned about
Roman or code-mixed text in this work. We will be publishing the ﬁnal list
on GitHub. These words were used as a search query to obtain hate, oﬀensive,
and profane tweets. The majority of the tweets that we obtained are related
to political and social issues. We also made a note of controversial events with
their time frame happening in India in the last couple of years which particu-
larly triggered violence on social media. To avoid bias towards certain words or
phrases, we have limited the tweets for a particular search query to a number
less than 150. Also, while collecting the tweets, we have not included any refer-
ence to the author of the tweet thereby eliminating the bias towards that author.
In our publicly available version of the dataset, we have kept all the hashtags,
symbols, emojis, and URLs for anyone to experiment on. However, we have re-
moved all of these while performing the baseline experiments. Furthermore, we
will be removing the user mentions from the public dataset to maintain complete
user anonymity.
3.2
Annotation
The entire dataset has been labelled manually by the 4 annotators consider-
ing four major classes viz. hate, oﬀensive, profane, and not. All the annotators

--- Page 5 ---\n\nL3Cube-MahaHate: A Marathi Hate Speech Detection Dataset
5
were native Marathi speakers and were ﬂuent in reading and writing in Marathi.
The annotation guidelines were set before the tagging exercise. The ﬁrst 200
sentences were tagged together to further improve the consistency post which
sentences were tagged in parallel except for ambiguous sentences. The tweets
which were targeted at a single individual thereby criticizing or dehumanizing
the individual are tagged as oﬀensive. These tweets were mainly attributed to
an individual politician, celebrity, or any random person with the use of singular
phrases. The tweets which were targeted at a group of people describing the
deﬁciencies towards race, political opinion, sexual orientation, gender, etc. are
tagged as hate. These tweets were majorly concentrated towards political par-
ties or the ruling government. Also, a few samples belong to negative comments
on minority groups and gender bias. The tweets which contain swear or pro-
fane words are strictly tagged as profane, even if they describe the oﬀensive or
hateful category. The tweets that do not satisfy any of the above criteria are sim-
ply tagged as not. Congratulatory and thanking tweets are tagged as not as well.
In some cases, the intention of the user behind a tweet cannot be suitably
identiﬁed. In such cases, the tweets were reviewed again and voting among 4
annotators was used to decide on the labels. Also, we encountered a few tweets
where hateful comments were quoted by a news handle. As these posts may in-
directly promote violence, we tagged them in the hateful category. To collect the
NOT tweets, we selected some Marathi personalities and scraped their tweets,
which gave us unbiased data towards any word.
Fig. 1: Average characters and words per label

--- Page 6 ---\n\n6
A. Velankar et al.
Split
HATE OFFN PRFN NOT TOTAL
Train
5375
5375
5375
5375
21500
Test
500
500
500
500
2000
Validation
375
375
375
375
1500
Table 1: Dataset label distribution
3.3
Dataset Details
Initially, we collected over 40k tweets in Marathi. Among these, we annotated
∼28000 samples. After removing over 3k noisy tweets which particularly included
poorly written text i.e. the text with the use of regional words or a large amount
of grammatical mistakes, we randomly selected 6250 samples from each of the 4
classes giving the total count of 25000 tweets. Although this uniform distribution
of tweets does not represent the true distribution it makes the model building
easier and does not require imbalance handling. We analyzed a few statistics on
the dataset. The average number of words per tweet in an entire dataset is 21
and the average number of characters is 113. The label-wise distribution is given
in Figure 1. The length of samples varies in the range of 2 to 93. The distribution
of the length of tweets and the number of characters per tweet is given in Figures
2 and 3 respectively. The dataset can be used for binary classiﬁcation as well. To
match the number of hateful samples viz. Hate, Oﬀensive, Profane all included,
we collected over 12500 extra NOT samples apart from that of 4-class corpus
giving an equal distribution of 18750 samples in hateful and non-hateful cate-
gories. This binary corpus of 37.5k will also be provided along with the original
dataset. Table 1 shows the 4-class dataset distribution in training, testing and
validation samples.
Fig. 2: Distribution of the length of a tweet

--- Page 7 ---\n\nL3Cube-MahaHate: A Marathi Hate Speech Detection Dataset
7
Fig. 3: Distribution of the number of characters in a tweet
4
Experiments
4.1
Model architectures
We have used multiple state of the art deep learning architectures [27], [16], [15]
to obtain the baseline results on 2-class as well as 4-class classiﬁcation. Before
training the models, we have cleaned the data by removing unwanted symbols,
user mentions, hashtags. Following algorithms are used for the evaluation of re-
sults:
CNN: The CNN model has a 1D convolution layer with a ﬁlter of size 300
and a kernel of size 3. It used ReLU activation, followed by max-pooling with
pool size 2. the same layers were added again which is followed by a dense
layer of size 50 and ReLU activation. Lastly, the layer with softmax activation
and 2 nodes was used. A dropout of 0.3 was used after the 1D max-pooling layer.
LSTM: The LSTM layer with 32 nodes was used. It was followed by a 1D
global max-pooling. The dense layer with 16 nodes along with ReLU activation
was used, followed by 0.2 dropout. A dense layer with 2 nodes and softmax ac-
tivation was used as a ﬁnal layer of the model.
BiLSTM: Bi-LSTM layer with 300 nodes followed by a 1D global max-pooling
layer was used. The dense layer was used with 100 nodes and ReLU activation
was used with it. This was followed by a dropout of 0.2. At last, the ﬁnal layer
with 2 nodes with activation softmax was used.
BERT: BERT is a bi-directional transformer based model [10] pre-trained over
large textual data to learn language representations. It can be ﬁne-tuned for
speciﬁc machine learning tasks. We used the following variations of BERT to
obtain baseline results:

--- Page 8 ---\n\n8
A. Velankar et al.
– Multilingual-BERT (mBERT) - trained on and usable with 104 languages
with Wikipedia using a masked language modeling (MLM) objective [9].
– IndicBERT - a multilingual ALBERT model released by Ai4Bharat, trained
on large-scale corpora [18], covering 12 major Indian languages: Assamese,
Bengali, English, Gujarati, Hindi, Kannada, Malayalam, Marathi, Oriya,
Punjabi, Tamil, Telugu.
– XLM-RoBERTa - a multilingual version of RoBERTa [5]. It is pre-trained
on 2.5TB of ﬁltered CommonCrawl data containing 100 languages with the
Masked language modeling (MLM) objective and can be used for down-
stream tasks.
– MahaBERT - a multilingual BERT model [17] ﬁne-tuned on L3Cube-MahaCorpus
and other publicly available Marathi monolingual datasets containing a total
of 752M tokens.
Model
Variant
2-Class Accuracy 4-Class Accuracy
CNN
Random
0.880
0.703
Trainable
0.866
0.710
Non-Trainable
0.870
0.751
LSTM
Random
0.857
0.681
Trainable
0.860
0.691
Non-Trainable
0.869
0.751
BiLSTM
Random
0.858
0.699
Trainable
0.860
0.664
Non-Trainable
0.870
0.761
BERT
IndicBERT
0.865
0.711
mBERT
0.903
0.783
xlm-RoBERTa
0.894
0.787
MahaALBERT
0.883
0.764
MahaBERT
0.909
0.803
MahaRoBERTa
0.902
0.803
Table 2: Classiﬁcation results on diﬀerent architectures
4.2
Results
We performed our experiments on CNN, LSTM, and Transformer based models.
For CNN and LSTM models, we have used random and fast text initialization
for the word embeddings. The pre-trained embeddings were used in both train-
able and non-trainable modes. The former means it was used by letting the
embedding layer adapt to the training data and latter by preventing it from be-
ing updated during training. Additionally, we used pre-trained language models,
particularly the variations of BERT such as IndicBERT, Multilingual BERT,

--- Page 9 ---\n\nL3Cube-MahaHate: A Marathi Hate Speech Detection Dataset
9
(a) 2-class classiﬁcation
(b) 4-class classiﬁcation
Fig. 4: Confusion matrices for the best models
XLM-RoBERTa, and a few custom BERT models to obtain the results. All the
2-class and 4-class accuracies are displayed in Table 2.
In CNN and LSTM based models, non-trainable fast text mode is outperform-
ing other conﬁgurations in both the binary and 4-class results. All the monolin-
gual Marathi BERT models are surpassing the multilingual versions of BERT
models i.e IndicBERT, mBERT, and xlm-RoBERTa. It was observed that the
non-trainable fast text setting for CNN and LSTM based models is performing
competitively with the BERT models even surpassing the indicBERT for both
the classes. The MahaBERT model gives the best binary classiﬁcation results
whereas MahaRoBERTa gives the best 4-class accuracy. The confusion matrices
for respective best results are shown in ﬁgures 4a and 4b.
5
Conclusion
In this paper, we have presented L3CubeMahaHate - a hate speech dataset con-
taining 25000 distinct samples equally distributed in 4 classes. This is the ﬁrst
major dataset in the domain of hate speech. We also provide the binary ver-
sion of the dataset of over 37500 samples. We further perform experiments to
obtain baseline results on various deep learning models like CNN, LSTM, BiL-
STM, and transformer-based BERT models such as IndicBERT, mBERT and
RoBERTa. The dataset is also evaluated on monolingual Marathi BERT mod-
els like MahaBERT, MahaALBERT, and MahaRoBERTa. For CNN and LSTM
based models, the non-trainable fast text mode outperforms its trainable coun-
terpart in both binary and 4-class classiﬁcation. In transformer-based models,
MahaBERT and MahaRoBERTa give the best results in binary and 4-class clas-
siﬁcation respectively.

--- Page 10 ---\n\n10
A. Velankar et al.
Acknowledgements
This work was done under the L3Cube Pune mentorship program. We would like
to express our gratitude towards our mentors at L3Cube for their continuous
support and encouragement.
References
1. Ajao, O., Bhowmik, D., Zargari, S.: Sentiment aware fake news detection on
online social networks. In: ICASSP 2019 - 2019 IEEE International Conference
on Acoustics, Speech and Signal Processing (ICASSP). pp. 2507–2511 (2019).
https://doi.org/10.1109/ICASSP.2019.8683170

--- Page 11 ---\n\nL3Cube-MahaHate: A Marathi Hate Speech Detection Dataset
11
2. Bhardwaj, M., Akhtar, M.S., Ekbal, A., Das, A., Chakraborty, T.: Hostility detec-
tion dataset in hindi (2020)
3. Bhatia, M., Bhotia, T.S., Agarwal, A., Ramesh, P., Gupta, S., Shridhar, K., Lau-
mann, F., Dash, A.: One to rule them all: Towards joint indic language hate speech
detection. arXiv preprint arXiv:2109.13711 (2021)
4. Bohra, A., Vijay, D., Singh, V., Akhtar, S.S., Shrivastava, M.: A dataset of hindi-
english code-mixed social media text for hate speech detection. In: Proceedings of
the second workshop on computational modeling of people’s opinions, personality,
and emotions in social media. pp. 36–41 (2018)
5. Conneau, A., Khandelwal, K., Goyal, N., Chaudhary, V., Wenzek, G., Guzm´an,
F., Grave, E., Ott, M., Zettlemoyer, L., Stoyanov, V.: Unsupervised cross-lingual
representation learning at scale. CoRR abs/1911.02116 (2019), http://arxiv.
org/abs/1911.02116
6. Corazza, M., Menini, S., Cabrio, E., Tonelli, S., Villata, S.: A multilingual evalu-
ation for online hate speech detection. ACM Transactions on Internet Technology
(TOIT) 20(2), 1–22 (2020)
7. Davidson, T., Warmsley, D., Macy, M., Weber, I.: Automated hate speech detection
and the problem of oﬀensive language (2017)
8. Del Vigna12, F., Cimino23, A., Dell’Orletta, F., Petrocchi, M., Tesconi, M.: Hate
me, hate me not: Hate speech detection on facebook. In: Proceedings of the First
Italian Conference on Cybersecurity (ITASEC17). pp. 86–95 (2017)
9. Devlin, J., Chang, M., Lee, K., Toutanova, K.: BERT: pre-training of deep bidirec-
tional transformers for language understanding. CoRR abs/1810.04805 (2018),
http://arxiv.org/abs/1810.04805
10. Devlin, J., Chang, M.W., Lee, K., Toutanova, K.: Bert: Pre-training of deep bidi-
rectional transformers for language understanding (2019)
11. Gaikwad, S., Ranasinghe, T., Zampieri, M., Homan, C.M.: Cross-lingual oﬀensive
language identiﬁcation for low resource languages: The case of marathi (2021)
12. Gao, L., Huang, R.: Detecting online hate speech using context aware models
(2018)
13. Geet D’Sa, A., Illina, I., Fohr, D., Klakow, D., Ruiter, D.: Exploring Conditional
Language Model Based Data Augmentation Approaches For Hate Speech Classiﬁ-
cation. In: TSD 2021 - 24th International Conference on Text, Speech and Dialogue.
Olomouc, Czech Republic (Sep 2021), https://hal.inria.fr/hal-03244472
14. Glazkova, A., Kadantsev, M., Glazkov, M.: Fine-tuning of pre-trained transformers
for hate, oﬀensive, and profane content detection in english and marathi. arXiv
preprint arXiv:2110.12687 (2021)
15. Joshi, R., Goel, P., Joshi, R.: Deep learning for hindi text classiﬁcation: A com-
parison. In: International Conference on Intelligent Human Computer Interaction.
pp. 94–101. Springer (2019)
16. Joshi,
R.,
Karnavat,
R.,
Jirapure,
K.,
Joshi,
R.:
Evaluation
of
deep
learning
models
for
hostility
detection
in
hindi
text.
2021
6th
Interna-
tional
Conference
for
Convergence
in
Technology
(I2CT)
(Apr
2021).
https://doi.org/10.1109/i2ct51068.2021.9418073,
http://dx.doi.org/10.1109/
I2CT51068.2021.9418073
17. Joshi, R.: L3cube-mahacorpus and mahabert: Marathi monolingual corpus,
marathi bert language models, and resources. arXiv preprint arXiv:2202.01159
(2022)
18. Kakwani, D., Kunchukuttan, A., Golla, S., N.C., G., Bhattacharyya, A., Khapra,
M.M., Kumar, P.: IndicNLPSuite: Monolingual Corpora, Evaluation Benchmarks

--- Page 12 ---\n\n12
A. Velankar et al.
and Pre-trained Multilingual Language Models for Indian Languages. In: Findings
of EMNLP (2020)
19. Kulkarni, A., Mandhane, M., Likhitkar, M., Kshirsagar, G., Jagdale, J., Joshi, R.:
Experimental evaluation of deep learning models for marathi text classiﬁcation.
In: Proceedings of the 2nd International Conference on Recent Trends in Machine
Learning, IoT, Smart Cities and Applications. pp. 605–613. Springer (2022)
20. Kulkarni,
A.,
Mandhane,
M.,
Likhitkar,
M.,
Kshirsagar,
G.,
Joshi,
R.:
L3cubemahasent: A marathi tweet-based sentiment analysis dataset. In: Proceed-
ings of the Eleventh Workshop on Computational Approaches to Subjectivity, Sen-
timent and Social Media Analysis. pp. 213–220 (2021)
21. MacAvaney, S., Yao, H.R., Yang, E., Russell, K., Goharian, N., Frieder, O.: Hate
speech detection: Challenges and solutions. PloS one 14(8), e0221152 (2019)
22. Mandl, T., Modha, S., Shahi, G.K., Madhu, H., Satapara, S., Majumder, P., Schae-
fer, J., Ranasinghe, T., Zampieri, M., Nandini, D., Jaiswal, A.K.: Overview of the
hasoc subtrack at ﬁre 2021: Hate speech and oﬀensive content identiﬁcation in
english and indo-aryan languages (2021)
23. Matamoros-Fern´andez, A., Farkas, J.: Racism, hate speech, and social media: A
systematic review and critique. Television & New Media 22(2), 205–224 (2021)
24. Mathur, P., Sawhney, R., Ayyar, M., Shah, R.: Did you oﬀend me? classiﬁcation
of oﬀensive tweets in hinglish language. In: Proceedings of the 2nd Workshop on
Abusive Language Online (ALW2). pp. 138–148 (2018)
25. Romim, N., Ahmed, M., Talukder, H., Islam, S., et al.: Hate speech detection
in the bengali language: A dataset and its baseline evaluation. In: Proceedings
of International Joint Conference on Advances in Computational Intelligence. pp.
457–468. Springer (2021)
26. Schmidt, A., Wiegand, M.: A survey on hate speech detection using natural lan-
guage processing. In: Proceedings of the Fifth International Workshop on Natural
Language Processing for Social Media, April 3, 2017, Valencia, Spain. pp. 1–10.
Association for Computational Linguistics (2019)
27. Velankar, A., Patil, H., Gore, A., Salunke, S., Joshi, R.: Hate and oﬀensive speech
detection in hindi and marathi (2021)
28. Waseem, Z., Hovy, D.: Hateful symbols or hateful people? predictive features for
hate speech detection on twitter. In: Proceedings of the NAACL student research
workshop. pp. 88–93 (2016)
\n```\n