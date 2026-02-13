---
title: "2025-Kajiwara-Advancing Hate Speech Detection with Transformers Insights from the - PDF Extract"
source_pdf: "2025-Kajiwara-Advancing Hate Speech Detection with Transformers Insights from the.pdf"
pages: 8
extracted_at: "2026-02-13T13:57:13.251118"
---

# PDF Extract: 2025-Kajiwara-Advancing Hate Speech Detection with Transformers Insights from the

**Source PDF:** 2025-Kajiwara-Advancing Hate Speech Detection with Transformers Insights from the.pdf
**Total Pages:** 8

---

## Content

```
--- Page 1 ---

Advancing Hate Speech Detection with
Transformers: Insights from the MetaHate
Santosh Chapagain1, Shah Muhammad Hamdi1, and Soukaina Filali
Boubrahimi1
Department of Computer Science, Utah State University,
4205 Old Main Hill, Logan, Utah 84322, USA
{santosh.chapagain, s.hamdi, soukaina.boubrahimi}@usu.edu
This paper includes examples of harmful and offensive language used for
research and illustrative purposes only.
Abstract. Hate speech is a widespread and harmful form of online dis-
course, encompassing slurs and defamatory posts that can have serious
social, psychological, and sometimes physical impacts on targeted indi-
viduals and communities. As social media platforms such as X (formerly
Twitter), Facebook, Instagram, Reddit, and others continue to facilitate
widespread communication, they also become breeding grounds for hate
speech, which has increasingly been linked to real-world hate crimes. Ad-
dressing this issue requires the development of robust automated meth-
ods to detect hate speech in diverse social media environments. Deep
learning approaches, such as vanilla recurrent neural networks (RNNs),
long short-term memory (LSTM), and convolutional neural networks
(CNNs), have achieved good results, but are often limited by issues such
as long-term dependencies and inefficient parallelization. This study rep-
resents the comprehensive exploration of transformer-based models for
hate speech detection using the MetaHate dataset—a meta-collection
of 36 datasets with 1.2 million social media samples. We evaluate mul-
tiple state-of-the-art transformer models, including BERT, RoBERTa,
GPT-2, and ELECTRA, with fine-tuned ELECTRA achieving the high-
est performance (F1 score: 0.8980). We also analyze classification errors,
revealing challenges with sarcasm, coded language, and label noise.
Keywords: Deep Learning · Hate Speech · Natural Language Process-
ing (NLP) · Transformers · Large Language Models (LLMs).
1
Introduction
Hate speech is a particularly troubling type of offensive language that has been
linked to real-world hate crimes on social media platforms [15]. It can be a dam-
aging form of online abuse, contributing to emotional distress, fostering social
discrimination, and potentially inciting violence. Despite variations in defini-
tions, there is consensus that hate speech targets individuals or groups with
harmful intent, often based on race, religion, skin color, sexual identity, gender
arXiv:2508.04913v1  [cs.LG]  6 Aug 2025

--- Page 2 ---

2
S. Chapagain et al.
identity, ethnicity, disability, or national origin [1]. The rise of social networks and
online platforms has increased global connectivity but also highlighted a trou-
bling surge in hate speech across geographical and cultural boundaries. In recent
studies, approximately 30% of the adolescents surveyed reported experiencing
cyberbullying at some point in their lives. Furthermore, around 13% indicated
that they had been cyberbullied within the 30 days before the survey [9]. De-
spite ongoing efforts by social media platforms to improve policies and detection
systems, effectively addressing hate speech remains challenging due to complex
and varying contexts, coded language, indirect expressions, and evolving slang
[7]. The need for effective hate speech detection is critical. Advances in artificial
intelligence (AI) and machine learning (ML) have shown promise in this area
[7], emphasizing the importance of capturing the context of hate speech. LLMs
like BERT [6], based on the transformer architecture [17], represent significant
progress in NLP by utilizing attention mechanisms to capture longer dependen-
cies. These models have excelled in tasks such as text classification and sentiment
analysis [8]. However, they require large datasets. In this paper, we conduct a
large-scale investigation into the contextual detection of hate speech using LLMs,
using the extensive MetaHate [16] dataset, which explored over 60 hate speech
detection datasets and integrated 36 of them into the meta-collection. Our study
presents a comprehensive evaluation of the transformer-based large language
model for online hate detection. We evaluated several state-of-the-art models,
including BART, ELECTRA, BERT, RoBERTa, and GPT-2 using the Meta-
Hate dataset. Among the evaluated models, ELECTRA achieved the highest F1
score, outperforming all other baselines in hate speech classification.
2
Related Work
2.1
Social Media as a Key Resource for Hate Speech Data
Social media platforms like Reddit generate vast user content and have become
key venues for hate speech [14]. Their anonymity enables the spread of hate,
often linked to real-world crimes [15], and hate groups use coded symbols (e.g.,
"88" for "Heil Hitler") to organize [11]. Social media platforms facilitate the
spread of online hate by making it easier to connect with people who share sim-
ilar opinions, ideas, or interests, and by identifying potential targets based on
searchable traits such as religion, gender, and race [18]. For example, Twitter
allows users to easily identify people’s religion, gender, race, and political views
through hashtags, profiles, and images. Social networks provide feedback mecha-
nisms such as comments, likes, and upvotes that reinforce hateful behavior [18].
These interactions can increase the frequency and intensity of hate messages, as
well as strengthen the beliefs of those who spread them [18]. Although platforms
like Twitter and Facebook use human annotators to remove hateful content and
encourage users to report it, these methods are labor-intensive and prone to
bias. This has led to the development of automated hate speech detection using
classical and deep learning algorithms. However, there is still an urgent need
to develop robust models for real-time hate speech detection. Thus, the insights

--- Page 3 ---

3
gained from the hate speech data on social networks are invaluable to developing
more effective detection algorithms.
2.2
Machine Learning Approaches in Hate Speech Detection
Research in hate speech detection on social media has evolved from traditional
machine learning methods like Support Vector Machines (SVM) and Logistic
Regression to recent deep learning approaches such as LSTMs, CNNs, and more
recently, transformer-based models like BERT [6]. Warner and Hirschberg were
among the first to apply supervised machine learning techniques to hate speech
detection using SVM [19]. Later, Davidson et al. [5] expanded the use of algo-
rithms in this domain with Logistic Regression, Naïve Bayes, Decision Trees,
Random Forests, and linear SVMs. Naïve Bayes and K-NN classifiers have also
proven effective, as demonstrated by Yan et al. [20] and Yin et al. [21], who
combined these classifiers with techniques like bag-of-words and term frequency-
inverse document frequency (TF-IDF). Kumari et al. [10] proposed an LSTM-
based approach for detecting hate speech on Twitter, demonstrating superior
performance compared to shallow learning methods. Although deep learning and
word embeddings-based models have shown promising performance, they could
not match the capabilities of modern transformer-based models like BERT [6]
and RoBERTa [12]. Mittal et al. [13] demonstrated that BERT-based models
outperform traditional techniques by effectively capturing complex semantics
and adapting to various linguistic contexts. LLMs has achieved remarkable per-
formance in hate speech detection and other NLP tasks [8,3,2,4] In this paper, we
explore various transformer-based large language models, comparing the perfor-
mance of fine-tuned transformers on the MetaHate [16] dataset. Our study finds
that ELECTRA outperforms other transformers on the MetaHate [16] dataset.
3
Big Data and Label
The creators of the MetaHate [16] dataset conducted a thorough review of over
60 existing hate speech detection datasets and ultimately selected 36 of them
to include in their meta-collection. This process resulted in 1,667,496 entries,
with 1,226,202 being unique comments sourced from social media platforms like
Twitter, Facebook, and Reddit. The dataset excludes synthetic data and com-
ments from non-social media sources. The dataset is binary-classified into hate
(label=1) and non-hate (label=0) categories to align with the majority of ex-
isting datasets and facilitate ease of use. Of the 1,226,202 comments, 253,145
are labeled as hate speech, representing 20.64% of the dataset. To address the
class imbalance in the MetaHate [16] dataset, we used class weights from scikit-
learn. We observed that hate speech contains a high frequency of terms such as
"fucking", "faggot", "nigger", "black", "idiot", and others.

--- Page 4 ---

4
S. Chapagain et al.
(a) Hate (label = 1)
(b) No Hate (label = 0 )
Fig. 1: WordCloud on MetaHate [16] dataset labels.
4
ELECTRA
In this study, we used ELECTRA (Efficiently Learning an Encoder that Clas-
sifies Token Replacements Accurately), a transformer-based architecture that
pretrains two models: a generator and a discriminator. The generator acts as a
masked language model by replacing tokens in a sequence, while the discrimi-
nator identifies these replaced tokens. In the fine-tuning step, the preprocessed
data were split as follows: 80% of instances were randomly allocated for fine-
tuning and training, 10% for validation, and 10% for testing the final model’s
performance. Fine-tuning began with tokenization, where the input text is bro-
ken down into individual tokens. These tokens were then passed sequentially as
input embeddings, undergoing multi-head self-attention after adding positional
embeddings. In the self-attention mechanism, the model computed query, key,
and value vectors for each token to capture dependencies across the sequence, al-
lowing it to understand relationships between tokens regardless of their position.
These representations were then processed by a feedforward network to intro-
duce non-linear transformations. After passing through stacked layers of encoder
blocks, the output sequence of vectors from ELECTRA was passed through a
linear layer, dropout layer, and softmax layer to distinguish between classes.
5
Experiments
We ran all experiments on a Linux server with dual Intel Xeon Gold 5220R
processors (24 cores each, 2.20 GHz) and eight NVIDIA RTX A4000 GPUs (16
GB VRAM each). Training was carried out using PyTorch 2.4.0 with CUDA
12.1 for all models. All of our code is available on GitHub 1. We fine-tuned the
models for 4 epochs with a batch size of 32 and a maximum sequence length
of 300, chosen empirically for efficiency without loss in performance. Training
used the AdamW optimizer (learning rate 3e-5, epsilon 1e-6, weight decay 0.001),
excluding bias and LayerNorm from decay.
1 https://github.com/chapagaisa/hate_speech_detection

--- Page 5 ---

5
5.1
Baseline Methods
All baseline methods used consistent hyperparameters (see Section V) and relied
on base versions of transformer models for fair comparison. Traditional mod-
els included a linear SVM with TF-IDF and stop word removal, and a CNN
trained for one epoch on padded tokenized sentences using a simple architec-
ture with ReLU and sigmoid layers. Transformer-based models included BERT,
RoBERTa, GPT-2, BART, DeBERTa, Longformer, XLNet, DistilBERT, and T5.
These models vary in architecture and training strategies: RoBERTa improves
on BERT by removing next-sentence prediction, GPT-2 is a unidirectional trans-
former, BART combines bidirectional and autoregressive features, DeBERTa in-
troduces disentangled attention, Longformer handles long sequences efficiently,
XLNet uses an autoregressive pretraining method, DistilBERT is a compact
version of BERT, and T5 reformulates all tasks into a text-to-text format.
5.2
Results and Analysis
Table 1 presents the results of various transformer-based models fine-tuned with
the MetaHate dataset. ELECTRA performed the best among the baselines,
achieving the highest F1 score of 0.8980 and accuracy of 0.8946, while the worst-
performing model was GPT-2, with an F1 score of 0.6504 and accuracy of 0.6152.
DistilBERT and BART showed competitive results based on F1 score and ac-
curacy. In the mid-tier, RoBERTa and XLNet showed similar results, slightly
below the top models.
Table 1: Performance of classifiers on MetaHate [16]
Model
F1 Score
Accuracy
SVM
0.8380
0.8466
CNN
0.8422
0.8612
BERT
0.8809
0.8879
GPT2
0.6504
0.6152
T5
0.8707
0.8625
DeBERTa
0.8808
0.8746
Longformer
0.8845
0.8785
RoBERTa
0.8908
0.8858
XLNet
0.8917
0.8870
BART
0.8928
0.8886
DistilBERT
0.8940
0.8905
ELECTRA
0.8980
0.8946
Figure 2 shows the confusion matrix for the ELECTRA model on the Meta-
Hate test set. Out of 110,117 instances, the model correctly classified 78,627
non-hate samples (71.4%) and 19,882 hate speech samples (18.1%). Misclassi-
fications included 8,215 false positives (7.5%) and 3,393 false negatives (3.1%).

--- Page 6 ---

6
S. Chapagain et al.
These results indicate a strong overall performance with high precision and re-
call, especially in correctly identifying hate speech. Figure 3 shows the ROC
curves and AUC scores of various transformer-based classifiers. ELECTRA’s
ROC-AUC is 0.9533, slightly below RoBERTa and XLNet. Although ROC-AUC
is an important metric for illustrating classifier accuracy by distinguishing be-
tween positive and negative classes across diverse thresholds, the F1 score is more
attuned to class imbalance. ELECTRA outperforms all classifiers in terms of F1
score, indicating their excellence in correctly identifying hate speech instances
and effectively addressing class imbalance.
Fig. 2: Confusion matrix on the test set
using ELECTRA.
Fig. 3: ROC-AUC of different trans-
formers on MetaHate dataset [16].
Linguistic Analysis of Misclassifications We performed a linguistic analy-
sis on some misclassified examples of the ELECTRA classifier and found several
recurring patterns that included sarcastic or ironic language (e.g., remarks that
mimic exaggerated praise or mock stereotypes) were flagged as hateful despite
lacking genuine hostility. Another example is figurative and exaggerated expres-
sions, such as dramatic warnings or over-the-top threats delivered in jest, which
were also misinterpreted due to their intense tone. Similarly, keyword bias, la-
beling emotionally charged but harmless expressions (e.g., frustration over a de-
layed service) caused the model to classify hate as non-hateful based on strong
wording. In contrast, aggressive messages without direct hate indicators such as
all-caps complaints or accusatory statements were sometimes missed.
6
DISCUSSION AND CONCLUSION
Although ELECTRA achieved the highest F1 score among the tested models, a
small but significant proportion of MetaHate samples may be mislabeled, partic-
ularly around subjective or political discourse. We advocate for semi-automated

--- Page 7 ---

7
relabeling tools using explainable AI (e.g., LLM-based rationale classification) to
improve dataset integrity. Future work should explore hybrid approaches com-
bining fine-tuning with instruction or adapter-based methods for low-resource
and cross-platform settings. Developing efficient transformer variants can sup-
port real-time use on edge devices. Expanding to multi-modal hate content and
improving annotation quality for evaluations are also key directions.
Addressing online hate speech involves ethical considerations, particularly
around free speech. In our work, we used the publicly available MetaHate dataset,
which was curated from multiple sources without including any personally iden-
tifiable information. The dataset supports the detection of harmful content on
social media but contains offensive elements, so careful handling is necessary to
prevent misuse. Some parts of the dataset are openly accessible, while others
require author permission. Any biases present are from the original sources and
are not intended to cause harm. We used the dataset for only research purposes,
which is in line with its intended non-commercial use.
This study demonstrates the effectiveness of transformer-based models, par-
ticularly ELECTRA, in detecting hate speech within a large-scale and diverse
dataset. We also performed detailed analyses of misclassified instances and found
common linguistic challenges, such as sarcasm, coded language, and annotation
noise, that continue to hinder classification accuracy. By integrating insights
from NLP, social science, and ethics, we advance toward more robust and so-
cially responsible AI systems to combat online hate.
7
Acknowledgements
Shah Muhammad Hamdi and Soukaina Filali Boubrahimi are supported by the
CISE and GEO directorates under NSF awards #2204363, #2240022, #2301397,
and #2305781.
References
1. American Library Association: Hate speech and hate crime (2024), https://www.
ala.org/advocacy/intfreedom/hate, accessed: 13 Aug. 2024
2. Cascalheira, C.J., Chapagain, S., Flinn, R.E., Klooster, D., Laprade, D., Zhao, Y.,
Lund, E.M., Gonzalez, A., Corro, K., Wheatley, R., et al.: The lgbtq+ minority
stress on social media (missom) dataset: A labeled dataset for natural language
processing and machine learning. In: Proceedings of the International AAAI Con-
ference on Web and Social Media. vol. 18, pp. 1888–1899 (2024)
3. Cascalheira, C.J., Chapagain, S., Flinn, R.E., Zhao, Y., Boubrahimi, S.F., Klooster,
D., Gonzalez, A., Lund, E.M., Laprade, D., Scheer, J.R., et al.: Predicting linguis-
tically sophisticated social determinants of health disparities with neural networks:
The case of lgbtq+ minority stress. In: 2023 IEEE International Conference on Big
Data (BigData). pp. 1314–1321. IEEE (2023)
4. Chapagain, S., Zhao, Y., Rohleen, T.K., Hamdi, S.M., Filali Boubrahimi, S., Flinn,
R.E., Lund, E.M., Klooster, D., Scheer, J.R., Cascalheira, C.J.: Predictive insights
into lgbtq+ minority stress: A transductive exploration of social media discourse.

--- Page 8 ---

8
S. Chapagain et al.
In: 2024 IEEE 11th International Conference on Data Science and Advanced An-
alytics (DSAA). pp. 1–9. IEEE (2024)
5. Davidson, T., Warmsley, D., Macy, M., Weber, I.: Automated hate speech detection
and the problem of offensive language. In: Proceedings of the international AAAI
conference on web and social media. vol. 11, pp. 512–515 (2017)
6. Devlin, J.: Bert: Pre-training of deep bidirectional transformers for language un-
derstanding. arXiv preprint arXiv:1810.04805 (2018)
7. ElSherief, M., Kulkarni, V., Nguyen, D., Wang, W.Y., Belding, E.: Hate lingo: A
target-based linguistic analysis of hate speech in social media. In: Proceedings of
the international AAAI conference on web and social media. vol. 12 (2018)
8. Fields, J., Chovanec, K., Madiraju, P.: A survey of text classification with trans-
formers: How wide? how large? how long? how accurate? how expensive? how safe?
IEEE Access (2024)
9. Hinduja, S., Patchin, J.W.: Cyberbullying facts (2023), https://cyberbullying.
org/facts, accessed: 2024-08-13
10. Kumari, K., Singh, J.P., Dwivedi, Y.K., Rana, N.P.: Multi-modal aggression iden-
tification using convolutional neural network and binary particle swarm optimiza-
tion. Future Generation Computer Systems 118, 187–197 (2021)
11. League, A.D.: Online hate and harassment: The american experience. Pew Re-
search Center: Internet, Science & Tech. Accessed December 25, 2022 (2019)
12. Liu, Y.: Roberta: A robustly optimized bert pretraining approach. arXiv preprint
arXiv:1907.11692 (2019)
13. Mittal, U.: Detecting hate speech utilizing deep convolutional network and trans-
former models. In: 2023 International Conference on Electrical, Electronics, Com-
munication and Computers (ELEXCOM). pp. 1–4. IEEE (2023)
14. Mondal, M., Silva, L.A., Benevenuto, F.: A measurement study of hate speech in
social media. In: Proceedings of the 28th ACM conference on hypertext and social
media. pp. 85–94 (2017)
15. Müller, K., Schwarz, C.: Fanning the flames of hate: Social media and hate crime.
Journal of the European Economic Association 19(4), 2131–2167 (2021)
16. Piot, P., Martín-Rodilla, P., Parapar, J.: Metahate: A dataset for unifying efforts
on hate speech detection. In: Proceedings of the International AAAI Conference
on Web and Social Media. vol. 18, pp. 2025–2039 (2024)
17. Vaswani, A.: Attention is all you need. arXiv preprint arXiv:1706.03762 (2017)
18. Walther, J.B.: Social media and online hate. Current Opinion in Psychology 45,
101298 (2022)
19. Warner, W., Hirschberg, J.: Detecting hate speech on the world wide web. In:
Proceedings of the second workshop on language in social media. pp. 19–26 (2012)
20. Yan, R., Li, Y., Li, D., Wang, Y., Zhu, Y., Wu, W.: A stochastic algorithm based on
reverse sampling technique to fight against the cyberbullying. ACM Transactions
on Knowledge Discovery from Data (TKDD) 15(4), 1–22 (2021)
21. Yin, C.J., Ayop, Z., Anawar, S., Othman, N.F., Zainudin, N.M.: Slangs and short
forms of malay twitter sentiment analysis using supervised machine learning. Inter-
national Journal of Computer Science & Network Security 21(11), 294–300 (2021)

```
