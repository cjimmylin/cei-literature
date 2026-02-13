---
title: "2024-Joy-Gender Bias Mitigation for Bangla Classification Tasks - PDF Extract"
source_pdf: "2024-Joy-Gender Bias Mitigation for Bangla Classification Tasks.pdf"
pages: 14
extracted_at: "2026-02-13T09:50:29.704761"
---

# PDF Extract: 2024-Joy-Gender Bias Mitigation for Bangla Classification Tasks

**Source PDF:** 2024-Joy-Gender Bias Mitigation for Bangla Classification Tasks.pdf
**Total Pages:** 14

---

## Content

```
--- Page 1 ---

Gender Bias Mitigation for Bangla Classification Tasks
Sajib Kumar Saha Joy *,1, Arman Hassan Mahy *,1, Meherin Sultana 1, Azizah Mamun Abha 1,
MD Piyal Ahmmed 1, Yue Dong 2, G M Shahariar 2
1 Ahsanullah University of Science and Technology
2 University of California, Riverside
{joy.cse, arman.cse.200104110, meherin.cse.200104036}@aust.edu
{azizah.cse.200104021, ahmmed.cse.200104107}@aust.edu
{yue.dong, gshah010}@ucr.edu
Abstract
In this study, we investigate gender bias in
Bangla pretrained language models, a largely
under explored area in low-resource languages.
To assess this bias, we applied gender-name
swapping techniques to existing datasets, cre-
ating four manually annotated, task-specific
datasets for sentiment analysis, toxicity detec-
tion, hate speech detection, and sarcasm detec-
tion. By altering names and gender-specific
terms, we ensured these datasets were suit-
able for detecting and mitigating gender bias.
We then proposed a joint loss optimization
technique to mitigate gender bias across task-
specific pretrained models. Our approach was
evaluated against existing bias mitigation meth-
ods, with results showing that our technique not
only effectively reduces bias but also maintains
competitive accuracy compared to other base-
line approaches. To promote further research,
we have made both our implementation and
datasets publicly available.1
1
Introduction
Large Language Models (LLMs) such as GPT-
4 (Achiam et al., 2023), Gemini (Team et al., 2023),
LLaMA (Touvron et al., 2023) and their succes-
sors have revolutionized text generation and under-
standing by leveraging vast amounts of data and
substantial computational power to achieve state-
of-the-art performance. However, their sheer size
and resource requirements make them impracti-
cal for many real-world applications in resource-
constrained languages, such as Bangla, where the
computational cost of deploying LLMs can be pro-
hibitive (Hasan et al., 2024). As a result, task spe-
cific Pretrained Language Models (PLMs) such as
BERT (Devlin et al., 2019) and T5 (Raffel et al.,
2020), which are more lightweight and computa-
*These authors contributed equally to this work.
1https://github.com/sajib-kumar/
Gender-Bias-Mitigation-From-Bangla-PLM
tionally efficient are often favored for their bal-
ance between performance and practicality, mak-
ing them suitable for various NLP and NLG tasks
in low resource language like Bangla (Kabir et al.,
2024). Despite their widespread adoption in clas-
sification tasks, one significant issue in utilizing
PLMs is the presence of bias towards gender, which
can lead to skewed and potentially harmful out-
comes (Bolukbasi et al., 2016). Gender bias in
NLP tasks has been extensively explored in En-
glish in the form of both detection (Kiritchenko
and Mohammad, 2018) and mitigation (Sun et al.,
2019a) but despite the increasing availability of pre-
trained Bangla language models, there are a very
few works (Sadhu et al., 2024b,c) that focused only
on gender bias detection and mitigation.
This paper addresses the gap of bias mitiga-
tion by examining gender bias in four different
Bangla language models pretrained in classifica-
tion tasks of sentiment analysis, toxicity detection,
hate speech detection, and sarcasm detection. We
first curated four manually annotated task specific
datasets, specifically transformed to identify gender
bias by swapping names and gender-specific terms
since previous work has shown that such manipu-
lation of data can reveal latent biases in language
models (Rudinger et al., 2018). Then, we applied
several gender bias mitigation techniques such as
data augmentation, counterfactual data substitution,
and fine-tuning with bias-neutral datasets that have
been explored in prior research (Zhao et al., 2018;
Webster et al., 2020) to assess their effectiveness
in reducing bias while maintaining classification
performance. In addition, we propose a joint loss
(cross entropy loss and cosine similarity) optimiza-
tion approach for bias mitigation and compared the
performance with the existing methods. Our find-
ings suggest that this approach effectively reduces
bias as well as preserves the classification perfor-
mance demonstrating its potential application in
broader gender bias free classification tasks.
arXiv:2411.10636v1  [cs.CL]  16 Nov 2024

--- Page 2 ---

2
Dataset
Due to the scarcity of Bangla datasets for gender
bias studies, we curated and transformed existing
task-specific Bangla datasets by selecting samples
that contain male or female gender terms. Fol-
lowing established practices in LLM gender bias
research in English (Kotek et al., 2023), we then
automatically generated new samples by altering
these gender-specific terms and names.
To identify gender terms, we developed a dictio-
nary of 573 gendered word pairs in Bangla, sourced
from the internet and grammar books. This dic-
tionary features pairs like “eqel” (son) and “emey”
(daughter), and accounts for words with multiple
feminine forms, such as “vaI” (brother) with “eban”
(sister) and “vaib” (sister-in-law). We used this
dictionary to generate samples by swapping the
original gendered terms with their counterparts, en-
suring all possible alternatives were considered.
For identifying names, we applied Named Entity
Recognition (NER) and then replaced using a pre-
defined set of masculine and feminine names based
on the gender term present in each sample. Finally,
human evaluators reviewed the automatically gen-
erated samples to address missed or unconverted
gender terms and to correct errors from the NER
model, such as missed names or incorrect identi-
fication of non-name words as names. We have
included descriptions of the existing datasets, a
detailed overview of our dataset construction pro-
cess, and relevant dataset statistics in Appendix
B. Appendix C lists sets of masculine and fem-
inine names while Appendix H contains all the
collected gendered terms. In addition, we provide
a few sample entries from each dataset in Table 8
of Appendix G.
2.1
Test Data Construction
We aim to construct a test dataset with gender bi-
ases, with the following key designs.
Measuring Bias.
To identify gender bias, we
compared the predictions of pretrained language
models, fine-tuned for specific tasks, on both orig-
inal and gender-name swapped samples. We con-
sidered a model biased towards gender if there was
a mismatch in predictions between the original and
the corresponding gender-name swapped samples.
We utilized four fine-tuned models: (Kowsher et al.,
2022) for sarcasm detection, (Bhattacharjee et al.,
2022) for sentiment analysis, (Das et al., 2022) for
hate speech detection, and (FredZhangUBC, 2023)
for toxicity detection. We provide a brief descrip-
tion of the utilized models in Appendix D.
Test Data via Bias Detection.
We present the
bias detection results in Table 1. The table shows
that the sarcasm detection model exhibits the low-
est bias percentage at 0.46%, while the toxicity
detection model shows the highest bias at 7.48%.
Task
Size
Mismatches
Bias%
Sentiment
4857
218
4.48%
Sarcasm
9589
45
0.46%
Toxicity
7057
528
7.48%
HateSpeech
10034
525
5.23%
Table 1: Bias scores for task specific Bangla PLMs.
On the other hand, the sentiment analysis and
hate speech detection models also demonstrate no-
table bias, with percentages of 4.48% and 5.23%
respectively. The samples with mismatched pre-
dictions between the original and gender-name
swapped texts were utilized as test data for bias
mitigation experiments.
3
Methodology
To mitigate gender bias in a pre-trained language
model (PLM), we proposed a fine-tuning approach
with a custom joint loss function. The objective
was twofold: (1) minimize the cross-entropy loss
for the classification task and (2) reduce the dis-
tance between the embeddings of original and
gender-name-swapped texts during training.
Input Processing
At the start of the fine-tuning
process, both the original text and its gender-name-
swapped counterpart were fed into the model simul-
taneously. These paired inputs allowed the model
to learn debiased representations by aligning the
embeddings of both versions of the text.
Embedding Extraction
Max-pooled embed-
dings were extracted for both the original text and
the gender-name-swapped text. Let the embed-
dings of the original and gender-name-swapped
texts be represented as e1 and e2, respectively.
These embeddings were used in the joint loss com-
putation to enforce similarity between the two.
Joint Loss Function
The custom joint loss func-
tion (Jloss) consists of two components: cross-
entropy loss for classification accuracy (LCE) and

--- Page 3 ---

gender debiasing loss (LGB) based on cosine simi-
larity, which aligns the embeddings of the original
and gender-name-swapped texts. The gender debi-
asing loss is defined as:
LGB = 1 −e1 · e2
|e1||e2|
(1)
The final loss function is a weighted sum of both,
with a hyperparameter λ controlling the balance
between classification and debiasing:
Jloss = LCE + λLGB
(2)
where λ controls the trade-off between bias reduc-
tion and classification performance.
Dropout and Output Layer
After embedding
extraction, only the original text embedding e1 was
passed through the dropout layer for further pro-
cessing. The final output was obtained by passing
this embedding through a linear layer, after which
we calculated the cross-entropy loss for the classi-
fication task.
Training and Inference
During training, the
model minimized the joint loss using backpropaga-
tion, gradually reducing the distance between the
original and gender-name-swapped embeddings.
After training, since the embeddings of the origi-
nal and swapped texts were expected to be closely
aligned, only the original text was required during
inference. This eliminated the need to generate
gender-name-swapped text at inference time, re-
ducing computational complexity.
4
Experiments
Experimental Setup. For bias detection, we used
default hyperparameters during inference with no
additional fine-tuning. For bias mitigation, stan-
dard fine-tuning was applied. Texts were tokenized,
passed through pre-trained models to generate to-
ken representations, and max-pooled for sentence
representation. A dropout layer preceded the final
linear layer. Across all experiments, we used con-
sistent hyperparameters: batch size of 16, learning
rate of 1e-4, dropout rate of 0.2, λ = 1 and the
Adam optimizer. Models were fine-tuned for 15
epochs.
Evaluation Metrics.
To quantify bias, we calcu-
lated the bias percentage as the ratio of mismatched
predictions to the total number of data pairs in each
dataset. Specifically, the Bias Percentage is com-
puted as:
Bias Percentage = Cmismatch
Ctotal
× 100
(3)
where Cmismatch denotes the number of mismatched
predictions, and Ctotal represents the total number
of data pairs. This metric allows us to evaluate
how often a model’s predictions differ between the
original and gender-name-swapped texts, providing
a clear measure of bias in the model.
To assess the performance of bias mitigation, we
used the Normalized Bias Score, which compares
the number of mismatched predictions from a spe-
cific approach to those from the zero-shot inference
baseline. The Normalized Bias Score is defined as:
Normalized Bias Score = Capproach
Cbaseline
× 100
(4)
where Capproach is the count of mismatched pre-
dictions from the bias mitigation approach, and
Cbaseline is the count of mismatched predictions
from the zero-shot inference. This score provides a
normalized measure of bias mitigation, with lower
scores indicating more effective bias reduction.
Baselines for Bias Mitigation.
We experimented
three baseline approaches for bias mitigation.
(a) Fine-tuning with both original and aug-
mented samples (FOA). For each task, we en-
hanced the original dataset by adding augmented
data, which involved swapping genders and names
for each original sample. This effectively doubled
the dataset size from n to 2n samples which we
utilized for fine-tuning task-specific models.
(b) Fine tuning with only Original Data (FOD).
We fine-tuned task-specific models using the orig-
inal, unaugmented dataset to assess whether fine-
tuning alone could reduce bias compared to zero-
shot inference. This setup offers a key comparison
for evaluating the impact of fine-tuning on accuracy
and bias mitigation against data augmentation or
other interventions.
(c) Token Masking (TM). For each task, we re-
placed all names with a <Name> token and gender
terms with a <Gender> token. Since these tokens
were not in the tokenizer vocabulary of the pre-
trained models, we added them and adjusted the
model’s token embedding size accordingly before
fine-tuning.

--- Page 4 ---

Approach
Data
Sentiment
Sarcasm
Toxicity
Hate Speech
Overall Average Accuracy
Zero Shot Inference
Original Sentence
27.06
64.40
62.10
83.23
46.59
GN Swapped Sentence
45.87
35.50
37.80
16.76
Average
36.47
49.95
49.95
50.00
Finetuning with Original
Data (FOD)
Original Sentence
87.15
84.40
87.30
77.90
76.02
GN Swapped Sentence
75.00
77.70
80.60
38.09
Average
81.08
81.05
83.95
58.00
Token Masking (TM)
GN Masked Sentence
83.00
84.40
85.40
61.71
78.63
Joint Loss
Optimization (JLO)
Original Sentence
87.15
84.44
88.25
78.28
80.30
GN Swapped Sentence
84.40
73.33
82.95
63.61
Average
85.78
78.89
85.60
70.95
Finetuning with Original
+ Augmented Data (FOA)
Original Sentence
88.07
73.33
86.17
79.23
79.95
GN Swapped Sentence
83.48
64.44
84.46
80.38
Average
85.78
68.89
85.32
79.81
Table 2: Comparison of accuracy (%) for gender bias mitigation techniques across classification tasks.
5
Results & Analysis
To assess the mitigation performance, we answer
the following two research questions.
Q1: How does the proposed bias mitigation tech-
nique affect accuracy?
We evaluate the effect of
bias mitigation techniques on accuracy for each ap-
proach by computing the overall average accuracy,
which is the numeric mean of accuracy scores over
different tasks. We illustrated the accuracy scores
of each approach over different tasks in table 2. We
observe that Joint Loss Optimization (JLO) strikes
the best balance (refer to Appendix E) between bias
mitigation and accuracy, with scores ranging from
70.94% to 85.77%, making it ideal for tasks requir-
ing both. While Token Masking (TM) eliminates
bias completely, its accuracy, especially in hate
speech detection, can drop to 61.71%, suggesting it
is best suited for tasks focused on bias elimination
over accuracy. The fine-tuning with both original
and augmented data (FOA) offers a good compro-
mise, achieving a bias reduction with an average
accuracy of 79.95%. Fine-tuning with Original
Data (FOD) has decent accuracy at 78.62% but is
more prone to bias. Zero-Shot Inference, with low
accuracy and high bias, is the least effective.
Q2: How effective is the proposed method for
bias reduction?
To evaluate the effectiveness of
each approach, we first calculate the normalized
bias score for different tasks. We then compute
overall average bias score by taking the numeric
mean of these scores. We report the bias scores
in table 3. From the table we observe that Token
Masking (TM) was the most effective, achieving
a bias score of 0, indicating complete bias elimi-
nation by masking names and gender terms. Joint
Approach
Bias Scores
Average
Sentiment
Sarcasm
Toxicity
HateSpeech
Zero Shot
100.00
100.00
100.00
100.00
100.00
FOD
13.76
11.11
10.42
46.29
20.39
TM
0
0
0
0
0
JLO
3.67
11.11
9.47
22.67
11.73
FOA
8.26
8.89
4.73
6.86
7.18
Table 3: Performance of different approaches in bias
reduction.
Loss Optimization (JLO) followed with a score
of 11.73, showing good bias reduction but not as
complete as TM. Fine-tuning with Original Data
(FOD) scored 20.39, while fine-tuning with both
original and augmented data (FOA) had a score
of 7.18, making it highly effective after TM. Zero-
Shot Inference had the highest bias score of 100,
indicating maximum bias. This comparison high-
lights TM and FOA as the most effective, with
JLO offering competitive benefits, while FOD and
Zero-Shot Inference are less effective.
6
Conclusion
This study reveals a significant presence of gender
bias in Bangla pretrained language models across
several classification tasks. Our bias mitigation
approach effectively reduced bias while maintain-
ing accuracy, indicating its potential for wider use
in NLP tasks. These findings highlight the need
to address gender bias to ensure fair outcomes in
NLP applications, especially for under-resourced
languages like Bangla.

--- Page 5 ---

7
Limitations
During dataset transformation, we swapped male-
centric names with female-centric ones and vice
versa using an NER model to identify names in
the original texts. However, the accuracy of the
NER model, particularly in Bangla, might be lim-
ited and might require improvement. Moreover,
our approach assumes binary gender categories, ex-
cluding non-binary identities, which restricts the
scope of bias detection. We did not use large lan-
guage models (LLMs) in this study, which could
limit the relevance of our findings for applications
involving state-of-the-art models. Incorporating
LLMs could potentially yield different results in
terms of both accuracy and bias mitigation. Further-
more, we used consistent hyper parameters across
all mitigation approaches, but altering these could
affect the outcomes. Finally, the datasets may lack
sufficient diversity and balance, impacting the gen-
eralizability of the results.
8
Ethical Considerations
Our research focuses on binary gender bias due
to the structure of existing datasets and literature.
We recognize the importance of non-binary and
gender-fluid identities and encourage future work
to include these dimensions for a more compre-
hensive approach to bias mitigation. Our datasets
contain toxic and hate speech content, which may
be offensive to some. We retained these data points
to ensure that our models are exposed to realistic,
harmful language, emphasizing the importance of
bias mitigation in language models that interact
with such content.
References
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama
Ahmad, Ilge Akkaya, Florencia Leoni Aleman,
Diogo Almeida, Janko Altenschmidt, Sam Altman,
Shyamal Anadkat, et al. 2023. Gpt-4 technical report.
arXiv preprint arXiv:2303.08774.
Tasnim Sakib Apon, Ramisa Anan, Elizabeth Antora
Modhu, Arjun Suter, Ifrit Jamal Sneha, and MD Go-
lam Rabiul Alam. 2022. Banglasarc: A dataset for
sarcasm detection. In 2022 IEEE Asia-Pacific Con-
ference on Computer Science and Data Engineering
(CSDE), pages 1–5. IEEE.
Tanveer Ahmed Belal, GM Shahariar, and Md Hasanul
Kabir. 2023. Interpretable multi labeled bengali toxic
comments classification using deep learning. In 2023
International Conference on Electrical, Computer
and Communication Engineering (ECCE), pages 1–
6. IEEE.
Abhik Bhattacharjee, Tahmid Hasan, Wasi Ahmad,
Kazi Samin Mubasshir, Md Saiful Islam, Anindya
Iqbal, M. Sohel Rahman, and Rifat Shahriyar.
2022. BanglaBERT: Language model pretraining
and benchmarks for low-resource language under-
standing evaluation in Bangla. In Findings of the
Association for Computational Linguistics: NAACL
2022, pages 1318–1327, Seattle, United States. Asso-
ciation for Computational Linguistics.
Tolga Bolukbasi, Kai-Wei Chang, James Y Zou,
Venkatesh Saligrama, and Adam T Kalai. 2016. Man
is to computer programmer as woman is to home-
maker? debiasing word embeddings. In Advances in
Neural Information Processing Systems, volume 29.
Curran Associates, Inc.
K Clark. 2020. Electra: Pre-training text encoders as
discriminators rather than generators. arXiv preprint
arXiv:2003.10555.
Dipto Das, Shion Guha, and Bryan Semaan. 2023. To-
ward cultural bias evaluation datasets: The case of
bengali gender, religious, and national identity. In
Proceedings of the First Workshop on Cross-Cultural
Considerations in NLP (C3NLP), pages 68–83.
Mithun Das, Somnath Banerjee, and Animesh Mukher-
jee. 2022. Data bootstrapping approaches to improve
low resource abusive language detection for indic
languages. arXiv preprint arXiv:2204.12543.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. BERT: Pre-training of
deep bidirectional transformers for language under-
standing. In Proceedings of the 2019 Conference of
the North American Chapter of the Association for
Computational Linguistics: Human Language Tech-
nologies, Volume 1 (Long and Short Papers), pages
4171–4186, Minneapolis, Minnesota. Association for
Computational Linguistics.
FredZhangUBC.
2023.
Bert
small
multi-
lingual
toxicity
classification.
https:
//github.com/fredzhang7/tfjs-node-tiny/
releases/tag/text-classification. Accessed:
October 16, 2024.
Md. Arid Hasan, Firoj Alam, Anika Anjum, Shudipta
Das, and Afiyat Anjum. 2023. Blp 2023 task 2: Sen-
timent analysis. In Proceedings of the 1st Interna-
tional Workshop on Bangla Language Processing
(BLP-2023), Singapore. Association for Computa-
tional Linguistics.
Md Arid Hasan, Prerona Tarannum, Krishno Dey, Imran
Razzak, and Usman Naseem. 2024. Do large lan-
guage models speak all languages equally? a compar-
ative study in low-resource settings. arXiv preprint
arXiv:2408.02237.

--- Page 6 ---

Max Hort, Zhenpeng Chen, Jie M Zhang, Mark Harman,
and Federica Sarro. 2023. Bias mitigation for ma-
chine learning classifiers: A comprehensive survey.
ACM Journal on Responsible Computing.
Sophie Jentzsch and Cigdem Turan. 2023. Gender bias
in bert–measuring and analysing biases through sen-
timent rating in a realistic downstream classification
task. arXiv preprint arXiv:2306.15298.
Mohsinul Kabir, Mohammed Saidul Islam, Md Tah-
mid Rahman Laskar, Mir Tafseer Nayeem, M Sai-
ful Bari, and Enamul Hoque. 2024. BenLLM-eval:
A comprehensive evaluation into the potentials and
pitfalls of large language models on Bengali NLP.
In Proceedings of the 2024 Joint International Con-
ference on Computational Linguistics, Language
Resources and Evaluation (LREC-COLING 2024),
pages 2238–2252, Torino, Italia. ELRA and ICCL.
Simran Khanuja, Diksha Bansal, Sarvesh Mehtani,
Savya Khosla,
Atreyee Dey,
Balaji Gopalan,
Dilip Kumar Margam, Pooja Aggarwal, Rajiv Teja
Nagipogu, Shachi Dave, et al. 2021. Muril: Multi-
lingual representations for indian languages. arXiv
preprint arXiv:2103.10730.
Svetlana Kiritchenko and Saif Mohammad. 2018. Ex-
amining gender and race bias in two hundred senti-
ment analysis systems. In Proceedings of the Sev-
enth Joint Conference on Lexical and Computational
Semantics, pages 43–53, New Orleans, Louisiana.
Association for Computational Linguistics.
Hadas Kotek, Rikker Dockum, and David Sun. 2023.
Gender bias and stereotypes in large language models.
In Proceedings of the ACM collective intelligence
conference, pages 12–24.
Md Kowsher, Abdullah As Sami, Nusrat Jahan Prot-
tasha, Mohammad Shamsul Arefin, Pranab Kumar
Dhar, and Takeshi Koshiba. 2022.
Bangla-bert:
transformer-based efficient model for transfer learn-
ing and language understanding.
IEEE Access,
10:91855–91870.
Sanzana Karim Lora, Ishrat Jahan, Rahad Hussain, Ri-
fat Shahriyar, and ABM Alim Al Islam. 2023. A
transformer-based generative adversarial learning to
detect sarcasm from bengali text with correct classifi-
cation of confusing text. Heliyon, 9(12).
Colin Raffel, Noam Shazeer, Adam Roberts, Katherine
Lee, Sharan Narang, Michael Matena, Yanqi Zhou,
Wei Li, and Peter J Liu. 2020. Exploring the lim-
its of transfer learning with a unified text-to-text
transformer. Journal of machine learning research,
21(140):1–67.
Md Jamiur Rahman Rifat, Sheikh Abujar, Sheak Rashed
Haider Noori, and Syed Akhter Hossain. 2019. Ben-
gali named entity recognition: A survey with deep
learning benchmark. In 2019 10th International Con-
ference on Computing, Communication and Network-
ing Technologies (ICCCNT), pages 1–5.
Nauros Romim, Mosahed Ahmed, Hriteshwar Talukder,
and Md Saiful Islam. 2021. Hate speech detection
in the bengali language: A dataset and its baseline
evaluation. In Proceedings of International Joint
Conference on Advances in Computational Intelli-
gence: IJCACI 2020, pages 457–468. Springer.
Rachel Rudinger, Jason Naradowsky, Brian Leonard,
and Benjamin Van Durme. 2018. Gender bias in
coreference resolution. In Proceedings of the 2018
Conference of the North American Chapter of the
Association for Computational Linguistics: Human
Language Technologies, Volume 2 (Short Papers),
pages 8–14, New Orleans, Louisiana. Association for
Computational Linguistics.
Jayanta Sadhu, Ayan Antik Khan, Abhik Bhattacharjee,
and Rifat Shahriyar. 2024a. An empirical study on
the characteristics of bias upon context length varia-
tion for bangla. arXiv preprint arXiv:2406.17375.
Jayanta Sadhu, Maneesha Rani Saha, and Rifat Shahri-
yar. 2024b. An empirical study of gendered stereo-
types in emotional attributes for bangla in mul-
tilingual large language models.
arXiv preprint
arXiv:2407.06432.
Jayanta Sadhu, Maneesha Rani Saha, and Rifat Shahri-
yar. 2024c. Social bias in large language models for
bangla: An empirical study on gender and religious
bias. arXiv preprint arXiv:2407.03536.
Salim Sazzed. 2020. Cross-lingual sentiment classifica-
tion in low-resource bengali language. In Proceed-
ings of the sixth workshop on noisy user-generated
text (W-NUT 2020), pages 50–60.
Hsuan Su, Cheng-Chu Cheng, Hua Farn, Shachi H Ku-
mar, Saurav Sahay, Shang-Tse Chen, and Hung-yi
Lee. 2023. Learning from red teaming: Gender bias
provocation and mitigation in large language models.
arXiv preprint arXiv:2310.11079.
Tony Sun, Andrew Gaut, Shirlyn Tang, Yuxin Huang,
Mai ElSherief, Jieyu Zhao, Diba Mirza, Elizabeth
Belding, Kai-Wei Chang, and William Yang Wang.
2019a. Mitigating gender bias in natural language
processing: Literature review. In Proceedings of the
57th Annual Meeting of the Association for Computa-
tional Linguistics, pages 1630–1640, Florence, Italy.
Association for Computational Linguistics.
Tony Sun, Andrew Gaut, Shirlyn Tang, Yuxin Huang,
Mai ElSherief, Jieyu Zhao, Diba Mirza, Eliza-
beth Belding, Kai-Wei Chang, and William Yang
Wang. 2019b. Mitigating gender bias in natural lan-
guage processing: Literature review. arXiv preprint
arXiv:1906.08976.
Gemini Team, Rohan Anil, Sebastian Borgeaud,
Yonghui Wu, Jean-Baptiste Alayrac, Jiahui Yu,
Radu Soricut, Johan Schalkwyk, Andrew M Dai,
Anja Hauth, et al. 2023.
Gemini: a family of
highly capable multimodal models. arXiv preprint
arXiv:2312.11805.

--- Page 7 ---

Pranav Tiwari, Aman Chandra Kumar, Aravindan Chan-
drabose, et al. 2022.
Casteism in india, but not
racism-a study of bias in word embeddings of indian
languages. In Proceedings of the First Workshop on
Language Technology and Resources for a Fair, In-
clusive, and Safe Society within the 13th Language
Resources and Evaluation Conference, pages 1–7.
Ewoenam Tokpo, Pieter Delobelle, Bettina Berendt, and
Toon Calders. 2023. How far can it go?: On intrinsic
gender bias mitigation for text classification. arXiv
preprint arXiv:2301.12855.
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier
Martinet, Marie-Anne Lachaux, Timothée Lacroix,
Baptiste Rozière, Naman Goyal, Eric Hambro,
Faisal Azhar, et al. 2023. Llama: Open and effi-
cient foundation language models. arXiv preprint
arXiv:2302.13971.
Kellie Webster, Xuezhi Wang, Ian Tenney, Alex Beu-
tel, Emily Pitler, Ellie Pavlick, Jilin Chen, and
Slav Petrov. 2020.
Measuring and reducing gen-
dered correlations in pre-trained models.
CoRR,
abs/2010.06032.
Zhongbin Xie, Vid Kocijan, Thomas Lukasiewicz, and
Oana-Maria Camburu. 2023. Counter-gap: Counter-
factual bias evaluation through gendered ambiguous
pronouns. arXiv preprint arXiv:2302.05674.
Jieyu Zhao, Tianlu Wang, Mark Yatskar, Vicente Or-
donez, and Kai-Wei Chang. 2018. Gender bias in
coreference resolution: Evaluation and debiasing
methods. In Proceedings of the 2018 Conference
of the North American Chapter of the Association for
Computational Linguistics: Human Language Tech-
nologies, Volume 2 (Short Papers), pages 15–20, New
Orleans, Louisiana. Association for Computational
Linguistics.
Appendix
A
Prior Works
In this section, we discuss some of the relevant
works on gender bias detection and mitigation.
A.1
Bias Detection Methods
Gender bias can manifest in both intrinsic and
extrinsic forms, with intrinsic bias related to pre-
trained language models and extrinsic bias to fine-
tuned models. Various techniques have been pro-
posed to measure bias accurately. For intrinsic bias,
Tokpo et al. (2023) used the Sentence Embedding
Association Test (SEAT) and Log Probability Bias
Score (LPBS), while extrinsic bias was measured
using True Positive Rate Difference (TPRD) and
Counterfactual Fairness. They found that intrinsic
bias metrics can be sensitive to mitigation tech-
niques, which sometimes conceal rather than re-
solve bias. Su et al. (2023) proposed a method to de-
tect gender bias in LLMs such as Alpaca, ChatGPT,
and GPT-4, using In-Context Learning (ICL) and
Reinforcement Learning (RL) to generate test cases.
Jentzsch and Turan (2023) revealed significant gen-
der biases in BERT models using the IMDB dataset,
comparing seven BERT-base models for bias in
sentiment classification. Sun et al. (2019b) exam-
ined gender bias through psychological tests like
IAT and WEAT applied to GloVe and Word2Vec
embeddings, using equity distance metrics such
as FPED and FNED on the GBETs dataset. Ti-
wari et al. (2022) explored gender bias in Hindi
and Tamil monolingual word embeddings using
the WEAT metric, which aligned with human bias,
while also assessing caste bias. Das et al. (2023)
focused on gender and racial biases in Bangla NLP
systems using the BIBED model and RDF, ana-
lyzing a diverse set of sentences from Wikipedia,
Banglapedia, Bangla literature, and other sources.
A.2
Bias Mitigation Methods
Hort et al. (2023) identified three types of bias
mitigation methods: Pre-processing, In-processing,
and Post-processing. These methods aim to ensure
fairness in machine learning models (ML). Tokpo
et al. (2023) proposed strategies to mitigate gen-
der bias in contextualized language models such
as BERT-large and ALBERT-large, focusing on
text classification tasks. Techniques like CDA pre-
training, Context-derbies, and Sent-derbies were
explored, addressing bias in pretraining data, pro-
cedures, or model outputs. Similarly, Su et al.
(2023) addressed bias in Natural Language Gen-
eration (NLG) using algorithm-based Adversar-
ial Learning and data-based Counterfactual Data
Augmentation (CDA) to fine-tune models and re-
duce bias. Sun et al. (2019b) used debiasing meth-
ods in data manipulation, gender tagging for ma-
chine translation (MT), and bias fine-tuning, target-
ing FPED and FNED reductions via gender-name
swapping. Xie et al. (2023) focused on gender
bias evaluation through coreference resolution, us-
ing the Counter-GAP dataset from fictional texts,
and demonstrated the effectiveness of name-based
counterfactual data augmentation in mitigating bias
over anonymization-based methods.

--- Page 8 ---

A.3
Bias Detection in Bangla
There has been some recent research works on bias
detection in Bangla. Sadhu et al. (2024a) inves-
tigates bias in Bangla by creating a dataset for
intrinsic bias measurement and adapting existing
methods to examine how varying context length
impacts bias metrics. Both Sadhu et al. (2024c)
and Sadhu et al. (2024b) focused on bias in large
language models (LLMs) for Bangla, but with dif-
ferent scopes. Sadhu et al. (2024c) examined both
gender and religious biases in LLM outputs, intro-
ducing probing techniques to detect these biases,
while Sadhu et al. (2024b) concentrate on gendered
emotion attribution, using a zero-shot learning ap-
proach to explore emotional stereotypes linked to
gender in Bangla. However, all these works fo-
cused on specific types of bias — gender, religious,
and emotional—and the methodologies were used
for only bias detection.
B
Bangla Gender Bias Dataset
To the best of our knowledge, there are currently
no datasets specially designed to identify gender
bias in Bangla classification tasks. Therefore, to
explore gender bias, we curated four task specific
datasets.
B.1
Dataset Collection
We collected datasets from four different sources
along with the original labels.
(a) Sentiment Detection. We utilized the dataset
provided by (Sazzed, 2020), which consists of
11,807 texts among them 3,307 are negative (label
0) and 8,500 are positive (label 1). After keeping
the samples that have gender terms, we got 4,857
instances.
(b) Sarcasm Detection. We utilized the Ben-Sarc
dataset provided by (Lora et al., 2023), which
consists of a total of 25,636 Bangla social media
comments where half of the data are sarcastic and
rest half are non-sarcastic. This dataset had 9,589
texts with gender terms.
(c) Toxicity Detection. For toxicity detection, we
used a multi labeled dataset provided by (Belal
et al., 2023), which has 16,073 sentences. Among
them, 7,585 comments are labeled as non-toxic
and 8,488 comments are labeled as toxic. As we
needed only those texts that have gender terms, we
Original Sentence
Converted Sentence
[B] iFk beleqn dada Aa-
mar men Hy Unar maQay
smsYa Aaeq
[B]
iFk beleqn
ebid
Aamar men Hy Unar maQay
smsYa Aaeq
[E]
Rightly
said
brother I think he has
a problem in his head
[E]
Rightly
said
sister-in-law
I think
he has a problem in his
head
[B] iFk beleqn dada Aa-
mar men Hy Unar maQay
smsYa Aaeq
[B] iFk beleqn dad Aa-
mar men Hy Unar maQay
smsYa Aaeq
[E]
Rightly
said
grandfather
I think
he has a problem in his
head
[E]
Rightly
said
grandmother I think
he has a problem in his
head
[B] iFk beleqn dada Aa-
mar men Hy Unar maQay
smsYa Aaeq
[B] iFk beleqn idid Aa-
mar men Hy Unar maQay
smsYa Aaeq
[E]
Rightly
said
brother I think he has
a problem in his head
[E] Rightly said sister
I think he has a prob-
lem in his head
Table 4: Handling generated samples when a gender
term in the original sample has multiple meanings. Here
B denotes the text in Bangla and E denotes the corre-
sponding English translation. Orange denotes gender
terms with multiple meanings, while green indicates
the counterparts of that term.
finally gathered 7,057 texts for our study.
(d) Hate-Speech Detection. For hate speech detec-
tion, we used a dataset from (Romim et al., 2021),
that has a total of 30,000 sentences. Among them,
10,000 are hate speech and 20,000 are non-hate
speech comments. After discarding non-gendered
comments, we have a total of 10,034 comments.
B.2
Bias Dataset Construction
(a) Dictionary Construction. We start by creating
a dictionary of gendered word pairs in Bangla
which is utilized to distinguish gender-specific
terms in texts. We collected these words from
the internet and also from a few Bangla grammar
books. This dictionary consists of 573 pairs of
masculine and feminine words. All the gender
terms can be found in Appendix H. For instance,
“eqel” (son) and “emey” (daughter) are included in
a pair as key. In cases where certain words had
multiple potential replacements, all the words were
included. For example, the word “vaI” (brother)

--- Page 9 ---

has two pairs with its feminine counterparts “eban”
(sister) and “vaib” (sister-in-law). In Bangla, the
same words can be spelled with different letters,
leading to various spellings. To address this, we
incorporated spelling variations into our dictionary.
For instance, male terms such as "ivxar" and
"ivxair" correspond to female terms like "ivxairn",
reflecting spelling differences. Similarly, the male
term "nana" relates to female terms like "nain" and
"nan".
(b) Identify Gender Terms.
Initially, we tok-
enized each word of each text in the collected
datasets. We then examined each token to see if it
matched any words in the dictionary. If a match
was found, we retained the text for containing a
gender term; otherwise, we discarded it due to the
absence of gender terms. This method resulted in
four datasets containing texts with gendered terms
across the four distinct tasks.
(c) Gender Swapping. To identify gender bias,
we need a pair of samples. The first text in the
pair is the original text with gender-specific terms,
which we automatically convert by swapping
these terms with their counterparts. This process
starts by tokenizing each word of each text in
the dataset. We then check each token against
a dictionary to find matches. When a match is
found, we replace it with its counterpart, leaving
unmatched tokens unchanged. For example, the
word "ð" (wife) would be replaced with "Wam"
(husband). Some masculine or feminine words
may have multiple suitable counterparts already
included in the dictionary.
For instance, the
masculine word "dada" can mean both brother
and grandfather, so its feminine counterparts
could be "dad" (grandmother), "idid" (sister), and
"ebid" (sister-in-law). For such cases, we generate
samples with all possible counterparts for a single
original sample.
Few examples of these text
transformations are shown in Table 4.
(d) Name Replacement. After swapping gender-
specific terms, some texts still contained names.
To ensure consistency between names and gender
in the converted texts, we swapped names based
on their gender relevance using a Named Entity
Recognition (NER) model2 which is trained on data
2https://sparknlp.org/2021/02/10/bengaliner_
cc_300d_bn.html
provided by (Rahman Rifat et al., 2019). The NER
model tokenizes the text and identifies various enti-
ties such as person names, locations, date and time,
organization names, etc., but we focused solely on
person names. When a name is detected, we deter-
mine its gender and replace it with a corresponding
name from the predefined set of male or female
names. Texts without person names remained un-
changed. This method maintained gender and name
consistency across the datasets, resulting in equal
numbers of original and transformed texts. A com-
plete example of the gender and name swapping
process is provided in Table 5.
Original
Sentence
[B] itSa Aapu xub suÝr kibta ilxet
paern. [E] Sister Tisha can write
very beautiful poems.
Gender
Term
Converted
Sentence
[B] itSa vaIya xub suÝr kibta ilxet
paern. [E] Brother Tisha can write
very beautiful poems.
Name De-
tection us-
ing
NER
model
[B] itSa vaIya xub suÝr kibta ilxet
paern. [E] Brother Tisha can write
very beautiful poems.
Final
Converted
Sentence
[B]
AaSraf
vaIya xub suÝr kibta
ilxet paern. [E] Brother Ashraf
can write very beautiful poems.
Table 5: Example of the gender-name swapping process
step by step. Here B denotes the text in Bangla and E
denotes the corresponding English translation.
Red
denotes the gender term that we want to swap, to gen-
erate a new sample. Yellow indicates the counterpart
of that gender term which has been swapped. Orange
indicates the name from the transformed sample that
we have to change. Green indicates the replaced name
with relevance to gender.
B.3
Human Evaluation
In this study, we recruited four annotators who
are undergraduate students with prior experience
in Bangla grammar, spelling, and Named Entity
Recognition tasks. These annotators were chosen
from a pool of ten candidates. Initially, all partici-
pants took an exam with 50 questions focused on
gender term conversion, correcting spelling errors,
and identifying named entities. The four students
with the highest scores were selected as annotators.
After each step of the dataset construction process,
the annotators manually reviewed the changes and

--- Page 10 ---

made corrections.
After converting the gender terms in the original
texts, the annotators manually reviewed the trans-
formed texts for each of the four datasets, with
each annotator responsible for one dataset. During
the review, they found some gender terms that had
been missed and not converted to their correspond-
ing male or female counterparts. The annotators
corrected these errors and updated the dictionary
with the missing terms. In total, 28 missing gender
terms were identified across all datasets.
Some of the datasets contained lengthy texts with
multiple gender terms to detect. However, the an-
notators found that certain gender terms were not
swapped due to the complexity of handling male
terms like "vaIeyra" and "jamaIek", and female terms
like "ebaenra" and "bUek", among others. Across all
datasets, there were 397 instances of such cases.
In Bangla, a word can have multiple meanings,
making accurate conversion difficult. For exam-
ple, the original sentence: "puruP teÛr iSkar Hey taI
puruPra ejel EbK irmae«D Aaeq." should have been con-
verted to: "nar teÛr iSkar Hey taI narra ejel EbK
irmae«D Aaeq." However, it was incorrectly converted,
resulting in nonsensical sentences like: "nar teÛr
iSkar Hey taI narra ejelin EbK irmae«D Aaeq." or "nar
teÛr iSkar Hey taI narra ejel bU EbK irmae«D Aaeq."
This was not an appropriate context for changing
gender terms. Similar issues occurred with words
like "ja" to "edOr" and "xan" to "xanm". These errors
were corrected by the annotators, and there were
548 such cases across all datasets.
After applying Named Entity Recognition
(NER) to the samples in our datasets, the annota-
tors found that the model incorrectly flagged some
irrelevant words as names, which were later ex-
cluded from the analysis. In Bangla, names can
have multiple spellings, causing the model to miss
names. For instance, "ineSa" and "inSu" refer to the
same person, but the model fails to detect them due
to spelling variations. Also the model also strug-
gled to detect names used as third-person singular
possessives, like "emHjaibenr" (Mehjabin’s), leaving
some names undetected. The annotators corrected
749 such cases across all datasets.
B.4
Dataset Statistics
Table 6 presents the data distribution across all
datasets. The equal number of samples between
the original and transformed datasets ensures a fair
comparison for evaluating bias. The average word
count per sample offers insights into the typical
length and complexity of the samples. Variations
in the frequency of gender terms and name counts
across tasks highlight the diversity of the datasets.
These statistics are essential for understanding the
composition and characteristics of each dataset,
which plays a key role in analyzing the model’s
performance and potential biases.
C
Male and Female Names
We list the male and female names used for
transforming task specific datasets below.
We
collected these names provided by (Das et al.,
2023).
Male names.
iSb, kai¯tk, bruN, menaHr, bal,
ramkumar, Sl, Ark, AirÕ, inly, tk, sÚ, aÚ,
nyn, Aa­dulLaH, Aa­dur, Imdadul, IUsuf, AaSraf, kamal,
julifkar, naijrul, Samsuddn, Aaisr, Aaitkur, naifs,
taHimd, masud, sadman, AaHnaf
Female names. lX, srWt, kaltara, du¯ga, saibÕ,
dmyÚ, tpt, ibinta, srla, sui³Mta, Amta, sunÝa, Aadta,
ismÚ, Antra, gulSan, ejaHra, jaHan, AaeySa, nrjaHan,
saHana, Haibba, najinn, raIsa, nujHat, maISa, farHana,
saidya, naHar, musifka
D
Model Descriptions
(a) BanglaSARC 3. An ELECTRA (Clark, 2020)
variant which is fine-tuned on Bangla sarcasm
data provided by (Apon et al., 2022).
The
model has an embedding size of 768, vocabulary
size of 32000 and it has a total of 110M parameters.
(b) Abusive-MuRIL4. MuRIL is a BERT (Devlin
et al., 2019) variant that has been pre-trained on
17 Indian languages, including their transliterated
versions (Khanuja et al., 2021). Abusive-Muril is a
fine-tuned MuRIL model pretrained for abusive
hate speech detection task provided by (Das et al.,
2022). The model has 110 million parameters and
assigns an embedding size of 768 to each token. It
uses a vocabulary of size 197285.
(c) BanglaBERT-Sentiment5.
An ELECTRA
variant which has been fine-tuned over a sentiment
dataset provided by (Hasan et al., 2023). It has 110
3https://huggingface.co/raquiba/
sarcasm-detection-BanglaSARC
4https://huggingface.co/Hate-speech-CNERG/
bengali-abusive-MuRIL
5https://huggingface.co/ka05ar/
banglabert-sentiment

--- Page 11 ---

Task
No. of
original
samples
No. of
converted
samples
No. of
total
samples
Average
no. of
word
Average
no. of
gender
terms
Frequency
of
names
Sentiment
4,857
4,857
9,714
19.668
1.500
4957
Sarcasm
9,589
9,589
19,178
19.187
1.470
4677
Toxicity
7,057
7,057
14,114
18.345
1.587
4695
Hate Speech
10,034
10,034
20,068
25.946
2.106
5343
Table 6: Dataset statistics for each classification task, including the number of original and converted samples, total
sample count, average word count per sample, average number of gender-related terms, and the total count of names
in the original samples.
million trainable parameter with 32000 vocabulary
size and a 768 token embedding size.
(d) one-for-all-toxicity6.
A BERT variant
model(FredZhangUBC, 2023) which has been fine-
tuned using toxi-text-3M dataset7 to detect 13 dif-
ferent types of toxicity over 55 languages. This
model has 110 million parameter. It uses 768-
dimensional token embedding with a vocabulary
size of 119547.
E
Bias vs Accuracy Trade off
Bias mitigation techniques can impact the accuracy
of Bangla pre-trained language models (PLMs) in
various ways. Token Masking (TM) is particu-
larly effective at completely removing bias, but
this often comes at the cost of reduced accuracy
in certain tasks, highlighting a trade-off between
bias reduction and model performance. Fine-tuning
with Original and Augmented Data (FOA) shows
stronger bias elimination compared to Joint Loss
Optimization (JLO), but JLO consistently delivers
better overall accuracy. JLO strikes a balance, re-
ducing bias while maintaining high accuracy, mak-
ing it a more reliable choice in scenarios where
both fairness and performance are crucial. In addi-
tion, the task-specific nature of these models means
that bias mitigation techniques may perform differ-
ently across tasks like sentiment analysis, toxicity
detection, and hate speech detection. Figure 1 vi-
sualizes the trade-offs between accuracy and bias
across these tasks, helping to better understand the
impact of each technique.
6https://huggingface.co/FredZhang7/
one-for-all-toxicity-v3
7https://huggingface.co/datasets/FredZhang7/
toxi-text-3M
0
20
40
60
80
100
Bias
40
50
60
70
80
Accuracy
FOA
JLO
TM
FOD
Zero Shot
Figure 1: Bias vs Accuracy trade-off of different mitiga-
tion approaches for all classification tasks.
F
Frequency of Bias
Table 7 presents the average number of mismatched
predictions by task specific models between the
original samples and the gender-name swapped
samples across different mitigation techniques for
the four tasks.
Ap-
proach
Senti-
ment
Sar-
casm
Toxic-
ity
Hate
Speech
Avg.
#mis-
matched
prediction
Zero
Shot
218
45
528
525
329
FOD
30
5
55
243
83.25
TM
0
0
0
0
0
JLO
8
5
50
119
45.5
FOA
18
4
25
36
20.75
Table 7: Average no. of mismatches in model predic-
tions between original and gender-name-swapped sam-
ples.

--- Page 12 ---

G
Few samples from the datasets with model prediction
To provide a better understanding of our curated datasets, we have illustrated some samples for all four
tasks in Table 8.
Task
Text
Model Prediction
Decision
Sentiment Analysis
Original Text:
Neutral
Biased
[B] Erkm suÝr suÝr samaijk naTk Aamra
Aaera caI Aar tanijn Aapu eta Ee´baer
faTaIya idela,,,,,,,
[E] We want more social dramas like
this and sister Tanjin absolutely blew
it„„„,
Converted Text:
Positive
[B] Erkm suÝr suÝr samaijk naTk Aamra
Aaera caI Aar sadman vaIya eta Ee´baer
faTaIya idela,,,,,,,
[E] We want more social dramas like
this and brother Sadman absolutely
blew it„„„,
Sarcasm Detection
Original Text:
Non-sarcastic
Unbiased
[B] ma b na emey b ? kiFn S
[E] The mother is older or the daughter
is older? Hard question
Converted Text:
Non-sarcastic
[B] baba b na eqel b ? kiFn S
[E] The father is older or the son is
older? Hard question
Toxicity Detection
Original Text:
Neutral
Biased
[B] EjnY keykidn pr pr Wam ecÉ kerI
[E] That’s why the husband changed
after a few days
Converted Text:
Toxic
[B] EjnY keykidn pr pr ð ecÉ kerI
[E] That’s why the wife changed after a
few days
Hate Speech Detection
Original Text:
Normal
Biased
[B] naTekr pircalk EkTa pagl kI eQek
Aaes EI sb elak faltu sb
[E] The director of the drama is a crazy
man where do all these men come from
Converted Text:
Abusive
[B] naTekr pircailka EkTa pagl kI eQek
Aaes EI sb ðelak faltu sb
[E] The director of the drama is a crazy
woman where do all these women come
from
Table 8: Few examples from our datasets, where the tasks are on the leftmost column. Samples from the original
and transformed versions are shown in the second column, with B denoting the Bangla texts and E denoting the
corresponding English translation. Target gender terms and names of original samples are in blue; transformed
samples are in red. The third column is the prediction for both original and transformed samples, based on which
the fourth column displays the final result for each task.

--- Page 13 ---

H
Gender Terms
The gender terms used for transforming the datasets are listed in table 9 for male terms and table 10 for
female terms.
Gender Words
Male
Term
ekaikl, kpN, kuS, kinì, kS, ikeSar, kumar, kaka, kruNamy, kaku, ikK, kukur, kaal, kPk, k¯ta, kib, k¯m,
kuiTl, kí, ikßr, ikKkr, kamar, katal, kÂl, e¸ta, ¸tdas, k¯ta, kumar, kepat, klu, kuHk, kuil, exaka,
xalu, xua, xun, xYatnama, xlnayk, xansama, xan, egayala, egap, gayk, gRaHk, gyla, guru, guruedb, guNban, egr,
g¯zv , gHiSXk, egalam, gryan, egasaI, guru, gNk, gNk, egap, gH, eGaPk, eGaP, GT, eGaTk, eGaP, cpl, cÇl,
caca, cirÕHn, catk, cÎal, eczur, cÞ, cakr, calk, caiP, ecar, cakr, cÎal, ctur, cxa, ctu¯dS, qaÕ, eqN-
Naa, qag, eqakra, eqel, jibt, jadukr, jbns¢g, jimdar, ejYì, jnab, jYaFa, iÆn, ejel, jnk, ej«Ts, ja-
maI, jamaI, ejel, ejFa, Fakur, Fakurda, Faku¯da, Fakurepa, Fakur, Daµar, Daµar, Dak, tny, truN, taps, tía¯t,
etjW, ta, dn, iØty, iØj, dir, ediHÕ, dyaban, dada, edOr, das, dtY, danb, edbta, duhx, edSenta,
dadu, da, dadababu, data, edOr, dulHa, dulHa, dada, dt, zabman, ezapa, znSal, zata, znban, nbn, nd, nana,
n¯tk, nT, nag, nait, naipt, nayk, nndaI, inpuN, inebdk, inebidt, narayN, enta, inpit, nr, nbab, nÝn,
nÝn, nait, naipt, nana, nndaI, inSacr, pjny, iy, acn, puNYtr, puÕ, ipsa, pagla, ipSac, epTuk, iyd¯S,
pagl, piÎt, pjar, paFk, pack, pircalk, cark, erk, palk, puÕban, ipta, i«s, iptaHn, puruP, eimk,
puilS, iSXk, pird¯Sk, itiniz, bN, paÕ, epala, paFa, epÕ, iptamH, pX, kaSk, pircark, prpuruP,
pit, eNta, vu, pª, iteJag, platk, pagl, fikr, fufa, efirOyala, bªz, ebRa, bYaGR, bYb³Qapk, bYivcar,
ibal, bRaóN, byî, ibzata, ibH¢g, by, bilyan, ebTa, biÝ, bYaTa, bRóa, ibediS, balk, baHk, buiªzman, ebyaI,
bua, ibbaiHt, ebcara, ibØan, br, bap, bld, ibpÔk, bsu, ebTa eqel, b«zu, eben, bs, bSY, bbaiHt, bíb,
bays, bYa¢gma, ba«zb, bruN, banr, ebed, baG, iblas, badSa, br, bP, baba, bRadar, ebanepa, ibdPk, ibH¢g, br,
bYaDa, b«zu, eb¢gma, bda, baÝa, bamn, byeã«D, b¯Pyan, eva, vaigna, vb, vagYban, vuj¢g, ivxar, ivxair,
vgban, vaI, vaI, vt, vasur, çata, velak, vaIepa, vaitja, vtY, vaIsab, vaI, vaIjan, vagen, vaIya,
mHaSy, mt, manny, mYan, miln, matul, m¯x, menarm, manb, emarg, mg, emesa, matul, emQr, mail, ma³Tar,
mHaraj, mÖa, myur, mama, imQYabad, ma¯jar, meHÞ, emzab, mayab, mat¢g, imya, mailk, mHyan, mmtamy, mH,
mHan, man, mjur, mrd, menaHr, eJag, JaÕ, JSW, Jubk, Jajk, rug, raXs, ru, rajput, ruicman, rupman, raja,
rajpuÕ, rajkumar, rupban, rjk, ray, erag, rjk, rXk, rciyta, elxk, lÂaban, elak, liÂt, elak, Sardy,
Suç, Sueyar, iSiXt, Juµ, S¢kr, SWSur, iSb, Sytan, eSWta¢g, SYalk, iSXk, Siµman, man, Suk, Sala, Sala,
imk, iSPY, S, eì, eªzy, Sgal, Sukr, Sa¯dl, S¯b, eys, SaHjada, SKkr, eata, iSXk, S, iS°p, srl,
svY, sdsY, s¯beì, isKH, sap, s¢g, sßYas, sHk¯m, esbk, stbap, sazk, eW£qaesbk, Wam, sxa, smRaT,
saeHb, svapit, eHmyipta, suSl, sultan, ³Qul, s, saKbaidk, suekS, sYar, saremy, sHcr, s®padk, sala,
saeHb, saeHb, sibta, sHeJag, snY, HirN, HKs, Huela, iHm, Htvaga, Hï, HajbYa«D, Hujur, eHata, Haramjada,
iHera, AnaQ, AruN, AsHay, ASW, Anusar, Avaga, AzYapk, Aivvabk, Aj, Avy, Azn, Aiventa, Aprup,
ArNY, Anugam, AgRj, Avaga, AibbaiHt, Aivsar, AiSiXt, Aazuink, Aabal, Aae¢kl, AayuPMan, Aa¯J, Aad-
huink, AaniÝt, Aati¢kt, AabWa, AabWajan, AabWu, Aaca¯J, Aaca¯J, IÞ, IÞb, SWr, U«Mad, UÑraizkar, Uikl,
UëR, Ee, Up³Qapk, XN, Xuizt, XiÕy, XiÕy, eqelra, babar, vaIek, eqeledr, eqelek, pircalkek, Wamek,
vaIyar, vaIedr, vaIyaek, Jubkra, iptaek, elakek, berr, eqeliTek, puruPedr, baepr, vaIyara, vaITa, sYaerr,
puruPra, puÕek, baeper, epalaer, Salar, epalaega, puruPra, puruePr, pula, eqeliT, eqra, qYama, qaeÕr, eqelTar,
epalara, vaIeyr, Zama, jamaIek, Wamr, Aiventar, pircalekr, babaega, eqelr, AYakTar, z¯mpuÕ, im³Tar, dada,
qaÕek, qaÕlg, vaIyaer, puruPbad, vaIek, vaIek, vaIr, saKbaidkek, maIgYar, ivxairr, gayk, vaeyra, AabWura,
maIgYa, puruPTa, maIgYa, vaIer, ipt©W, supariHera, prbaba, l¯D, iHerar, bf, Oyala, gru, vaIek, vaIeyr, vaIeyr,
vaIeyr, vaIek, vaIek, sar, dadar, Salara, vaIeyra, babaek, put, meHady
Table 9: Male gender terms.

--- Page 14 ---

Gender Words
Female
Term
ekaikla, kpNa, kuSa, kinìa, kSa, ikeSar, kumar, kaik, kruNamy, kak, kuIn, kukur, kaailn, kPaN, igiß,
miHla kib, miHla k¯m, kuiTla, kía, ikßr, ikKkr, kamarn, katailn, kÂl, e¸Õ, ¸tdas, k¯Õ, ku-
marn, kepat, kluin, kuHikn, kaimn, xuik, xala, xui, nar xun, xYatnam, xlnaiyka, Aaya, xanm, egayailn,
egaipn, gaiyka, gRaiHka, gyla bU, guru ma, guruma, guNbt, egr, g¯zv, gHiSiXka, baid, grys, ma egasaI, gu¯z,
miHla gNk, gNk, egap, giHN, eGaiPka, eGaP jaya, GiT, eGaTk, eGaPja, cpla, cÇla, cac, cirÕHna, catikn,
cÎailn, eczuran, cÞain, cakran, cailka, caiP eb, cuiß, iC, cÎal, ctura, cix, ctu¯dS, qaÕ, qui, qaig, qukir,
emey, jibta, jadukr, jbnsi¢gn, jimdar piÔ, ejYìa, jnaba, ejiF, pr, ejelin, jnn, eliDs, bU, ebma,
ejel bU, ejF, Fakuran, Fakurma, Fakuma, FakuriC, Fakrun, Daµarn, miHla Daµar, Daikn, tnya, truN, taps,
tía¯ta, etjiWn, ma, dna, iØtya, iØja, dira, ediHÕ, dyabt, ebid, ja, dais, danb, danb, edb, duhixn,
edSenÕ, ididma, id, ididmiN, daÕ, nnd, dulaIn, duliHn, dad, dt, zabmana, ezapan, znSailn, zaÕ, znbt,
nbna, nd, nan, n¯tk, niT, naign, natin, naiptan, naiyka, nnd, inpuNa, inebidka, inebidta, narayN, enÕ,
inpita, nar, ebgm, nÝna, nÝn, nateb, naipt bU, nain, nnidn, inSacr, pjnya, iya, acna, puNYtra,
knYa, ipis, pagil, ipSac, epTuk, iydi¯Sn, pagiln, pi«Dtan, pjairn, paiFka, paicka, pircailka, cairka,
eirka, pailka, puÕbt, mata, ie«ss, mataHn, miHla, eimka, miHla puilS, iSiXka, pirdi¯Ska, miHla i-
tiniz, bNa, paÕ, maIya, paiF, epÕ, matamH, piXN, kaiSka, pircairka, prnar, pÔ, eNÕ, vu pÔ,
piªn, iteJaign, platka, pagl, fikrin, fufu, efirOyal, bªza, iss, bYaGR, bYb³Qaipka, bYivcairN, ibal,
bRaóN, byîa, ibzaÕ, ibHi¢g, ga¯l, bilyan, ebiT, biÝn, ebiT, bRóaN, ibediSn, bailka, baiHka, buiªzmt, ebyan,
bui, ibbaiHta, ebcair, ibduP, ken, ma, gaI, ibzba, bsu jaya, emey eqel, ba«zb, eben bU, bsa, bSYa, bbaiHta,
bíb, bays, bYa¢gim, ba«zb, bruNan, banr, ebedin, baiGn, iblaisn, ebgm, bra¢gna, gaiv, ma, is³Tar, ebaniC,
ibdiPka, ibHi¢gn, bz, ebD, b«zupÔ, eb¢gm, bid, baid, bamin, ga¯leã«D, b¯PJs, evi, vaig, vban, vagYbt,
vuji¢gn, ivxairn, ivxairn, vgbt, Aafa, eban, epÔ, nnd, vign, vmiHla, vaIiC, vaitij, vtYa, vabi-
isab, vab, bubujan, vagn, Aapu, mHaSya, mta, mannya, OmYan, milna, matula, m¯xa, menarma, manb, murig,
mg, mais, matulan, emQran, mailn, ma³Tarin, mHaraN, maid, myr, maim, imQYabaidn, ma¯jar, meHÞaN, emzaib-
n, mayaibn, mati¢gn, ibib, malikn, mHys, mmtamy, mHt, mHt, mainn, mjurn, ejnana, menaHra, eJaign,
miHla JaÕ, JSiWn, Jubt, Jaijka, ruga, raXs, ruaN, rajputain, ruicmt, rupmt, ran, rajknYa, rajkumar,
rpbt, rjikn, rayigiß, eraigN, rjk, riXN, rciyÕ, elixka, lÂabt, ðelak, liÂta, miHla, Sardya,
Suça, Sueyarn, iSiXta, Juµa, S¢kr, SaSui, iSban, Sytain, eSWtai¢gn, SYailka, iSiXka, Siµmt, mt,
sar, Sail, Sal, nar imk, iSPYa, Sa, eìa, eªzya, Sgal, Skr, Sa¯dl, S¯baN, eys, SaHjad, SKkr,
eaÕ, iSXkpÔ, SaN, nar iS°p, srla, svYa, sdsYa, s¯beìa, isKH, saipn, si¢gn, sßYaisn, sHki¯mN,
esibka, stma, saizka, eW£qaesibka, ð, six, smRaÄ, emm, svaenÕ, eHmymata, suSla, sultana, ³Qula, st,
miHla saKbaidk, suekiSn, mYaDam, saremy, sHcr, s®paidka, sal, ibib, saeHba, saibÕ, sHeJaign, miHla
snY, HirN, HKs, emin, iHmain, Htvag, Hiïn, OJaIf, HujuraIn, eHaÕ, Haramjad, iHeraIn, AnaiQn, AruNa,
AsHaya, ASWa, AnusairN, Avag, AzYaipka, Aivvaibka, Aja, Avya, Azna, AivenÕ, Aprupa, ArNYan, Anu-
gaimn, AgRja, Avaign, AibbaiHta, AivsairN, AiSiXta, Aazuinka, Aabalin, Aai«T, AayuPMt, Aa¯Ja, Aazuinka,
AaniÝta, Aati¢kta, Aa®Ma, Aa®Majan, Aa®Mu, Aaca¯Ja, Aaca¯Jan, IÞaN, IÞan, SWr, U«Maidn, UÑraizkairN,
miHla Uikl, UëR, bkna, Up³Qaipka, XNa, Xuizta, XiÕya, XiÕyan, emeyra, maeyr, ebanek, emeyedr, emeyek,
pircailkaek, ðek, Aapur, ebanedr, Aapuek, Jubtra, mataek, miHlaek, bUeyr, emeyiTek, naredr, maeyr, Aa-
pura, ebanTa, mYaDaemr, narra, knYaek, maeyer, maIyaer, Salr, maIyaega, miHlara, miHlar, maIyYa, emeyiT, eqir,
qYami, qaÕr, emeyTar, maIyara, ebaenr, Zam, bUek, ðr, AivenÕr, pircailkar, maega, emeyr, AYake¦Rs,
z¯mknYa, imess, idid, qaÕek, qaÕlg, Aapuer, narbad, Aapaek, vabek, Aapur, miHla saKbaidkek, maigr,
ivxairinr, gayka, ebaenra, Aa®Mura, maig, miHlaTa, mag, ebaner, mat©W, supariHeraIn, prma, eliD, iHeraIenr,
gf, Oyal, gav, Aapaek, Aafar, vabr, Aapar, vabek, Aafaek, mYam, dadr, Salra, ebaenra, maek, emya,
meHadya
Table 10: Female gender terms.

```
