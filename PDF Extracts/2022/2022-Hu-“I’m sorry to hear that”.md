---
title: "“I’m sorry to hear that” - PDF Extract"
source_pdf: "2022-Hu-“I’m sorry to hear that”.pdf"
extraction_method: PyMuPDF
pages_extracted: 7
total_characters: 27662
---

# “I’m sorry to hear that”

## Page 1

Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing, pages 4324–4330
December 7-11, 2022 ©2022 Association for Computational Linguistics
Momentum Contrastive Pre-training for Question Answering
Minda Hu1 Muzhi Li1 Yasheng Wang2 Irwin King1
1Dept. of Computer Science & Engineering, The Chinese University of Hong Kong
2Huawei Noah’s Ark Lab
{mindahu21, mzli, king}@cse.cuhk.edu.hk,
wangyasheng@huawei.com
Abstract
Existing pre-training methods for extractive
Question Answering (QA) generate cloze-like
queries different from natural questions in syn-
tax structure, which could overfit pre-trained
models to simple keyword matching. In or-
der to address this problem, we propose a
novel Momentum Contrastive pRe-training fOr
queStion anSwering (MCROSS) method for ex-
tractive QA. Specifically, MCROSS introduces
a momentum contrastive learning framework to
align the answer probability between cloze-like
and natural query-passage sample pairs. Hence,
the pre-trained models can better transfer the
knowledge learned in cloze-like samples to an-
swering natural questions. Experimental results
on three benchmarking QA datasets show that
our method achieves noticeable improvement
compared with all baselines in both supervised
and zero-shot scenarios.
1
Introduction
The task of extractive Question Answering (QA),
which aims to select an answer span from a pas-
sage given a query, is a major focus of NLP re-
search. Currently, deep learning systems (Huang
et al., 2018; Devlin et al., 2019; Wu et al., 2021)
have achieved competitive results with humans on
large-scale QA datasets (Rajpurkar et al., 2016,
2018; Yang et al., 2018; Kwiatkowski et al., 2019).
However, the collection of high-quality natural QA
pairs is still a labor-intensive task, especially for
the construction of domain-specific QA systems.
To alleviate such data availability restrictions, pre-
training methods have been drawing increasing at-
tention (Dhingra et al., 2018; Ram et al., 2021).
Typically, pre-training methods for extractive
QA generate cloze-like query-passage pairs with
text-matching techniques. For instance, the Span
Selection Pre-Training (SSPT) method (Glass et al.,
2020a) generates these pairs with the Wikipedia
corpus using BM25. Nevertheless, these meth-
ods have two major issues. Firstly, the format of
In Jordan's second season of the playoffs against
the [BLANK], he even scored 63 points
Cloze-like 
Query
What team did Jordan score 63 points against in
the second season of the playoffs?
Natural 
Query
Boston Celtics
Answer 
Term
Figure 1: An example of the pre-training queries in
SSPT (Glass et al., 2020b). The query is a sentence
where a noun phrase or entity (“Boston Celtics”) is
replaced with the special token [BLANK], which differs
syntactically from the natural one.
cloze-like queries differs much from natural queries
asked by humans (see Fig. 1). In addition, models
trained by cloze-like queries overfit in capturing
the lexical overlaps between queries and passages,
which restricts the capability of high-level semantic
reasoning (Li et al., 2020; Hu et al., 2021). Since
answering natural questions requires a comprehen-
sive understanding of queries and passages, mod-
els pre-trained with cloze-like queries are not well
aligned with downstream QA tasks.
To solve these issues, we utilize Contrastive
Learning (CL) techniques to align knowledge
learned in cloze-like samples to answering natu-
ral language questions and circumvent overfitting.
Specifically, CL aims to learn representations by
contrasting augmentations of different input data,
which has been successfully applied in various re-
search fields such as bioinformatics, graph learning,
computer vision, and NLP (Han et al., 2022; Zhang
et al., 2022; He et al., 2020; Yang et al., 2021; Pan
et al., 2021). Nevertheless, existing CL methods
for QA focus on query-passage matching (Yang
et al., 2021; Caciularu et al., 2022) and multilin-
gual embedding alignment (Pan et al., 2021), which
have not been tailored to deal with issues of query
format inconsistency and overfitting in matching
lexical overlaps.
In this paper,
we propose a Momentum
Contrastive pRe-training fOr queStion AnSwer-
4324

## Page 2

ing (MCROSS) method for extractive QA. Specifi-
cally, MCROSS employs a momentum contrastive
learning strategy along with the conventional an-
swer prediction task to maximize the consistency of
predicted answer distributions between cloze-like
and natural query pairs and thus improves the per-
formance of pre-trained models in answering natu-
ral language questions. We show the efficacy of our
approach on standard English benchmark datasets.
On SQuADv1.1 (Rajpurkar et al., 2016), MCROSS
achieves about 2.7/3.5 percentage points gain on
F1/Exact Match (EM) accuracy over BERT, and
1.4/1.8 percentage points improvement on the same
metrics compared to SSPT (Glass et al., 2020a).
MCROSS also consistently outperforms the base-
line methods by a large margin on TriviaQA (Joshi
et al., 2017) and NewsQA (Trischler et al., 2017)
in supervised and zero-shot scenarios.
2
Method
The structure of our proposed MCROSS method
is shown in Fig. 2. Along with the cloze-like sam-
ples scloze = (qc, p, a) generated by SSPT (Glass
et al., 2020a), we create positive natural samples
snatural+ = (qn, p, a) containing natural queries
qn given passages and answers (p, a) from scloze
with T5 answer-aware question generator (Raffel
et al., 2020) which is fine-tuned with SQuADv1.1
training set. The details of pre-training datasets
are illustrated in Appendix A.1. Though differ-
ent in format, the cloze-like queries qc and pos-
itive natural queries qn are semantically similar
since they have the same answers a in given sup-
porting passages p. Therefore, we expect that the
predicted probability distribution of answer span
in positive pairs (scloze, snatural+) should be closer.
On the other hand, we generate negative query pairs
(scloze, snatural−) with different answers or support-
ing passages. Correspondingly, the predicted an-
swer span distribution of snatural−is expected to
be far from that of scloze. MCROSS achieves the
goal with two pre-training tasks as follows.
2.1
Pre-Training Tasks
Answer Term Prediction Task. Given a training
sample s = (q, p, a), the answer term prediction
task aims to predict the token span a = (sta, ena)
in the query q from the passage p1, where sta and
ena are the start and end positions of the answer
1We treat the first exact match of the token span in the
passage as the answer term.
𝑍",$%&'(,𝑍)
",$%&'*,𝑍+
",$%&'*,…
ℒ./011 =  ℒ4"$'56      +      ℒ8&.&
BERT=>$?
MLP
BERT$%&'
MLP
𝑍",=>$?
𝑍C,$%&'
𝑍",$%&'
𝑍C,$%&'(,𝑍)
C,$%&'*,𝑍+
C,$%&'*,…
𝑍C,=>$?
similarity
similarity
Momentum
Update
𝐶𝐿𝑆𝑞W 𝑆𝐸𝑃𝑝[𝑆𝐸𝑃]
𝑠^_`ab
𝑠Wcdefc_
answer prediction task
contrastive task
𝑎= (𝑠𝑡c,𝑒𝑛c)
𝑄",$%&'
𝑄C,$%&'
𝐶𝐿𝑆𝑞^ 𝑆𝐸𝑃𝑝[𝑆𝐸𝑃]
Figure 2: An overview of the proposed MCROSS
method.
term in the passage.
First, we prepare the concatenated token se-
quence T = [CLS] q [SEP] p [SEP] and lever-
age BERT (Devlin et al., 2019) to encode the con-
text embeddings H ∈R[len(q)+len(p)+3]×d for each
query-passage pair, where d is the dimension of
embeddings. Then, the probability distribution
Z = (zsta, zena) of the start/end indices of answer
span can be predicted as:
zsta
i
= p(i = sta) = softmax(Lstart
span(Hi)),
zena
i
= p(i = ena) = softmax(Lend
span(Hi)),
(1)
where Lstart
span and Lend
span are linear answer span pre-
diction layers. The loss function of the answer term
prediction task is defined below:
LAnswer(Z) = −1
2{
X
1≤i≤N
1(i = sta) log zsta
i
+
X
1≤i≤N
1(i = ena) log zena
i
},
(2)
where 1(condition) is the indicator function that re-
turns 1 if the condition is satisfied and 0 otherwise.
N is the length of the sequence T.
Contrastive Learning Task. This task utilizes a
contrastive loss function to guide the answer span
distributions (Zcloze, Znatural+) of positive sam-
ple pairs (scloze, snatural+) with same (p, a) to be
closer, while keeping Zcloze to be dissimilar from
Znatural−of snatural−with different passages p−
or answers a−.
Inspired by the Momentum Constrastive learn-
ing (MoCo) (He et al., 2020) strategy, we main-
tain a large pool of consistent negative samples
4325

## Page 3

from several previous batch iterations to preserve
more information on negative samples and ob-
tain better pre-training objectives.
Following
MoCo, we employ a dual-encoder architecture
(BERTfast, BERTslow) and maintain FIFO queues
(Qslow
sta , Qslow
ena ) containing a large set of answer
span distributions (zslow−
sta
, zslow−
ena
) of negative sam-
ples predicted by BERTslow. To maintain queue
consistency, for each batch iteration, parameters
θslow of BERTslow are only updated by the expo-
nential moving average of θfast of BERTfast. Here
we have
θslow = mθslow + (1 −m)θfast,
(3)
where m is the momentum coefficient. We regulate
the output of the answer-span classification layer
with InfoNCE loss to bring positive pairs (s, s+)
closer to each other and push negative ones apart:
LMoCo(zfast, zslow+, Q) =
−log
exp
 D(zfast, zslow+)/τ

P
zslow−∈Q exp (D(zfast, zslow−)/τ),
(4)
where zfast and zslow+ represent the start or end
distributions of positive pairs, τ is the softmax tem-
perature, and Q denotes queues containing distri-
butions zslow−of negative samples s−which have
(p−, a−) being different from s+. D is the similar-
ity function measuring distances between answer
span distributions. Cosine similarity is utilized in
the original MoCo method (He et al., 2020). How-
ever, we argue that KL-Divergence is more suitable
for the measurement of differences between two
probability distributions, which is evaluated and
validated in Appendix C.
2.2
Variants of the MCROSS Method
There are two variants of the MCROSS method
with different loss functions, the first is involved
with the unilateral loss function, and the second
one with the bilateral loss.
MCROSS (UNI). In addition to the original SSPT
training loss LAnswer(Zc), we add LMoCo to maxi-
mize the consistency of prediction between scloze
and snatural with little overhead in the unilateral
version of MCROSS. Here, we have the unilateral
MoCo loss
LUNI(scloze, snatural) = LAnswer(Zc)
+ λMoCo/2 ∗[LMoCo(zsta,c, zsta,n, Qn,slow
sta
)
+ LMoCo(zena,c, zena,n, Qn,slow
ena
)],
(5)
Method
F1
EM
0-shot
F1
0-shot
EM
BERT
87.43
79.50
8.00
0.06
SSPT
88.75
81.25
22.88
15.42
SSPT†
89.25
82.13
64.41
44.44
MCROSS(UNI)
88.95
81.60
24.78
16.58
MCROSS(BI)
90.11
83.03
65.68
45.40
w/o LMoCo
89.92
82.96
65.20
44.82
Table 1: Results on SQuADv1.1 dataset. (in domain)
where Zn = (zsta,n, zena,n) are the predicted
distributions of start/end indices for snatural, and
Zc = (zsta,c, zena,c) are for scloze. (Zc, Zn) are
predicted by BERTfast and , BERTslow, respec-
tively. Zn are stored in (Qn,slow
sta
, Qn,slow
ena
) and will
be reused in later training steps as negative exam-
ples. λMoCo denotes the ratio of MoCo loss.
MCROSS (BI). In MCROSS (UNI) method, only
cloze-like samples scloze are considered in the cal-
culation of answer term prediction loss LAnswer,
which makes the fast encoder BERTfast to be less
sensitive to natural samples snatural. Therefore, it
will be difficult to properly maintain the consis-
tency between the probability distributions gener-
ated from the two types of samples. To tackle this
issue, following xMoCo (Yang et al., 2021), we
leverage two LUNI losses and jointly optimize the
alignment of (scloze, snatural) and (snatural, scloze)
in the following bilateral loss.
LBI = LUNI(scloze, snatural)
+ LUNI(snatural, scloze),
(6)
where distributions of snatural are obtained from
BERTslow and stored in queue (Qn,slow
sta
, Qn,slow
ena
)
for LUNI(scloze, snatural). The same practices are
applied to scloze for LUNI(snatural, scloze).
We also evaluate MCROSS (w/o LMoCo), which
utilizes multi-task answer prediction loss to pre-
dict similar span a given (qc, p) and (qn, p) with
BERTfast:
LMCROSS = LAnswer(Zn) + LAnswer(Zc).
(7)
3
Experiments
We use the following three English span-extraction
QA datasets to evaluate pre-trained models on
F1/EM metrics in both supervised and zero-shot
scenarios.
Specifically, TriviaQA (Joshi et al.,
2017) and NewsQA (Trischler et al., 2017) are
out-of-domain datasets from MRQA 2019 Shared
4326

## Page 4

Task (Fisch et al., 2019). Since SQuADv1.1 (Ra-
jpurkar et al., 2016) dataset is utilized to fine-tune
the T5 question generator, it is also included to
examine the in-domain QA performance.
The experimental settings, implementation de-
tails, and complexity analysis are presented in Ap-
pendix A, B, and D.
3.1
Baselines
We compare the MCROSS with the following four
baselines:
• BERT: The 12-layer BERT model released
by (Devlin et al., 2019).
• MRQA-BERT: The official multi-task baseline
BERT-base model from MRQA2.
• SSPT: The span selection pre-training method
proposed by (Glass et al., 2020b). This method
trains models with cloze-like samples scloze us-
ing answer term prediction loss LAnswer(Zc) in
Eq. (7).
• SSPT†: SSPT method trained with only natural
samples snatural using answer term prediction
loss LAnswer(Zn) in Eq. (7).
3.2
Experiment Results
SQuADv1.1. Table 1 shows the performance of all
models on SQuADv1.1. Compared with the BERT
baseline without extended pre-training, three vari-
ants of the proposed MCROSS method increase the
F1/EM metrics by at least 1.5/2.1 percentage points.
In addition, MCROSS(w/o LMoCo) achieves dis-
cernible boosts among all metrics compared to
baseline SSPT. It proves that the combination of
cloze-like and natural samples in the QA task can
endow the pre-trained model with a better under-
standing on supporting passages. Moreover, the
gap between MCROSS(BI) and MCROSS(UNI)
indicates that models trained only with cloze-like
samples will be insensitive to natural questions. It
should be also noticed that there exists a perfor-
mance gap between SSPT† and MCROSS(UNI)
among all metrics. This is attributed to the fact that
the natural samples used in SSPT† are generated
by the T5 question generator (Raffel et al., 2020).
Since the T5 generator is fine-tuned on the training
set of SQuADv1.1, it is well fitted in the domain
of SQuAD. Compared to MCROSS(UNI) using
cloze-like samples, SSPT† is trained with the natu-
ral samples containing more domain knowledge of
the dataset, thus surpassing MCROSS(UNI).
2https://github.com/mrqa/
MRQA-Shared-Task-2019/tree/master/baseline
Method
F1
EM
0-shot
F1
0-shot
EM
BERT
64.28
49.17
3.55
0.02
SSPT
65.86
50.62
9.58
6.05
SSPT†
65.60
50.52
34.03
15.67
MRQA-BERT
66.80
50.80
N/A
N/A
MCROSS(UNI)
66.45
51.33
10.90
6.55
MCROSS(BI)
67.90
52.18
34.82
14.98
w/o LMoCo
66.95
52.14
35.68
16.50
Table 2: Results on NewsQA dataset. (out of domain)
Method
F1
EM
0-shot
F1
0-shot
EM
BERT
62.86
57.39
3.25
0.04
SSPT
70.93
65.27
26.89
22.47
SSPT†
69.09
63.24
42.01
33.99
MRQA-BERT
71.60
65.60
N/A
N/A
MCROSS(UNI)
72.06
66.41
28.28
23.48
MCROSS(BI)
73.77
68.05
47.79
39.53
w/o LMoCo
73.30
67.72
46.63
38.54
Table 3: Results on TriviaQA dataset. (out of domain)
NewsQA and TriviaQA. Table 2 and Table 3
show the results on NewsQA and TriviaQA dataset
from MRQA 2019 Shared Task. It is noticeable that
MCROSS(BI) performs the best among all methods
on F1 metrics. Compared with the state-of-the-art
baseline SSPT, it achieves an improvement of 2.0
F1 score and 1.6 EM accuracy on NewsQA. On
the TriviaQA dataset, MCROSS(BI) also surpasses
SSPT by 2.8 percentage points on F1 and EM ac-
curacy. Furthermore, the improvement on Trivi-
aQA of MCROSS(BI) over MCROSS(w/o LMoCo)
demonstrates the effectiveness of LMoCo in the
out-of-domain setting. In both datasets, the great
improvement on zero-shot F1/EM of SSPT† over
SSPT exhibits that SSPT† has gained the domain
knowledge in understanding natural questions from
SQuAD. In comparison with SSPT†, MCROSS(BI)
significantly boosts zero-shot QA performance by
5.6/6.2 percentage points of F1/EM accuracy.
In contrast to the SQuAD dataset with in-domain
settings, MCROSS(UNI) has gained a noticeable
advantage over SSPT† on both NewsQA and Triv-
iaQA datasets, hinting that SSPT† is overfitted to
the natural samples of SQuAD with extra domain
knowledge. Interestingly, MCROSS(BI) performs
worse in zero-shot scenarios on NewsQA dataset
than MCROSS(w/o LMoCo). This may be due to the
fact that NewsQA has 32.7% samples that can be
easily answered by simple text-matching (Trischler
et al., 2017), into which MCROSS(w/o LMoCo) is
overfitted to capture lexical overlaps.
4327

## Page 5

4
Conclusion
This paper presents a novel pre-training method
MCROSS for extractive QA which contains two
tasks: 1) contrastive learning and 2) answer term
prediction. Specifically, MCROSS adapts MoCo
frameworks to maintain consistency in answer-
ing cloze-like and natural questions, enabling pre-
trained models to have a more comprehensive un-
derstanding of supporting passages. The empirical
experiments on three public datasets demonstrate
that our approach can obtain noticeable improve-
ments in extractive QA tasks in supervised and
zero-shot scenarios.
5
Limitations
Although MCROSS can already obtain satisfactory
QA performance, due to limited time and computa-
tional resources, we only use 5 million cloze-like
samples for pre-training, which is one-twentieth of
the scale of original SSPT experiments.
References
Avi Caciularu, Ido Dagan, Jacob Goldberger, and Ar-
man Cohan. 2022. Long context question answering
via supervised contrastive learning. In Proceedings
of the 2022 Conference of the North American Chap-
ter of the Association for Computational Linguistics:
Human Language Technologies, pages 2872–2879,
Seattle, United States. Association for Computational
Linguistics.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. Bert: Pre-training of deep
bidirectional transformers for language understand-
ing. In NAACL-HLT (1).
Bhuwan Dhingra, Danish Danish, and Dheeraj Ra-
jagopal. 2018. Simple and effective semi-supervised
question answering. In Proceedings of the 2018 Con-
ference of the North American Chapter of the Asso-
ciation for Computational Linguistics: Human Lan-
guage Technologies, Volume 2 (Short Papers), pages
582–587.
Adam Fisch, Alon Talmor, Robin Jia, Minjoon Seo, Eun-
sol Choi, and Danqi Chen. 2019. MRQA 2019 shared
task: Evaluating generalization in reading compre-
hension. In Proceedings of 2nd Machine Reading
for Reading Comprehension (MRQA) Workshop at
EMNLP.
Michael Glass, Alfio Gliozzo, Rishav Chakravarti, An-
thony Ferritto, Lin Pan, G P Shrivatsa Bhargav, Di-
nesh Garg, and Avi Sil. 2020a. Span selection pre-
training for question answering. In Proceedings of
the 58th Annual Meeting of the Association for Com-
putational Linguistics, pages 2773–2782, Online. As-
sociation for Computational Linguistics.
Michael Glass, Alfio Gliozzo, Rishav Chakravarti, An-
thony Ferritto, Lin Pan, G P Shrivatsa Bhargav, Di-
nesh Garg, and Avi Sil. 2020b. Span selection pre-
training for question answering. In Proceedings of
the 58th Annual Meeting of the Association for Com-
putational Linguistics, pages 2773–2782, Online. As-
sociation for Computational Linguistics.
Wenkai Han, Yuqi Cheng, Jiayang Chen, Huawen
Zhong, Zhihang Hu, Siyuan Chen, Licheng Zong,
Liang Hong, Ting-Fung Chan, Irwin King, Xin Gao,
and Yu Li. 2022. Self-supervised contrastive learn-
ing for integrative single cell rna-seq data analysis.
Briefings Bioinform., 23(5).
Kaiming He, Haoqi Fan, Yuxin Wu, Saining Xie, and
Ross Girshick. 2020. Momentum contrast for un-
supervised visual representation learning. In 2020
IEEE/CVF Conference on Computer Vision and Pat-
tern Recognition (CVPR), pages 9726–9735.
Ziniu Hu, Yizhou Sun, and Kai-Wei Chang. 2021.
Relation-guided pre-training for open-domain ques-
tion answering. In Findings of the Association for
Computational Linguistics: EMNLP 2021, pages
3431–3448, Punta Cana, Dominican Republic. Asso-
ciation for Computational Linguistics.
Hsin-Yuan Huang, Chenguang Zhu, Yelong Shen, and
Weizhu Chen. 2018. Fusionnet: Fusing via fully-
aware attention with application to machine com-
prehension.
In 6th International Conference on
Learning Representations, ICLR 2018, Vancouver,
BC, Canada, April 30 - May 3, 2018, Conference
Track Proceedings. OpenReview.net.
Mandar Joshi, Eunsol Choi, Daniel Weld, and Luke
Zettlemoyer. 2017. TriviaQA: A large scale distantly
supervised challenge dataset for reading comprehen-
sion. In Proceedings of the 55th Annual Meeting of
the Association for Computational Linguistics (Vol-
ume 1: Long Papers), pages 1601–1611, Vancouver,
Canada. Association for Computational Linguistics.
Tom Kwiatkowski, Jennimaria Palomaki, Olivia Red-
field, Michael Collins, Ankur Parikh, Chris Alberti,
Danielle Epstein, Illia Polosukhin, Jacob Devlin, Ken-
ton Lee, et al. 2019. Natural questions: A benchmark
for question answering research. Transactions of the
Association for Computational Linguistics, 7:453–
466.
Zhongli Li, Wenhui Wang, Li Dong, Furu Wei, and
Ke Xu. 2020.
Harvesting and refining question-
answer pairs for unsupervised QA. In Proceedings
of the 58th Annual Meeting of the Association for
Computational Linguistics, pages 6719–6728, On-
line. Association for Computational Linguistics.
Lin Pan, Chung-Wei Hang, Haode Qi, Abhishek Shah,
Saloni Potdar, and Mo Yu. 2021. Multilingual BERT
post-pretraining alignment. In Proceedings of the
2021 Conference of the North American Chapter of
the Association for Computational Linguistics: Hu-
man Language Technologies, pages 210–219. Asso-
ciation for Computational Linguistics.
4328

## Page 6

Colin Raffel, Noam Shazeer, Adam Roberts, Kather-
ine Lee, Sharan Narang, Michael Matena, Yanqi
Zhou, Wei Li, and Peter J. Liu. 2020. Exploring the
limits of transfer learning with a unified text-to-text
transformer. Journal of Machine Learning Research,
21(140):1–67.
Pranav Rajpurkar, Robin Jia, and Percy Liang. 2018.
Know what you don’t know: Unanswerable ques-
tions for squad. In Proceedings of the 56th Annual
Meeting of the Association for Computational Lin-
guistics (Volume 2: Short Papers), pages 784–789.
Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, and
Percy Liang. 2016. Squad: 100,000+ questions for
machine comprehension of text. In Proceedings of
the 2016 Conference on Empirical Methods in Natu-
ral Language Processing, pages 2383–2392.
Ori Ram, Yuval Kirstain, Jonathan Berant, Amir Glober-
son, and Omer Levy. 2021. Few-shot question an-
swering by pretraining span selection. In Proceed-
ings of the 59th Annual Meeting of the Association for
Computational Linguistics and the 11th International
Joint Conference on Natural Language Processing
(Volume 1: Long Papers), pages 3066–3079, Online.
Association for Computational Linguistics.
Adam Trischler, Tong Wang, Xingdi Yuan, Justin Harris,
Alessandro Sordoni, Philip Bachman, and Kaheer
Suleman. 2017. Newsqa: A machine comprehension
dataset. ACL 2017, page 191.
Jeff Wu, Long Ouyang, Daniel M Ziegler, Nisan Sti-
ennon, Ryan Lowe, Jan Leike, and Paul Christiano.
2021. Recursively summarizing books with human
feedback. arXiv preprint arXiv:2109.10862.
Nan Yang, Furu Wei, Binxing Jiao, Daxing Jiang, and
Linjun Yang. 2021. xMoCo: Cross momentum con-
trastive learning for open-domain question answering.
In Proceedings of the 59th Annual Meeting of the As-
sociation for Computational Linguistics and the 11th
International Joint Conference on Natural Language
Processing (Volume 1: Long Papers), pages 6120–
6129. Association for Computational Linguistics.
Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio,
William Cohen, Ruslan Salakhutdinov, and Christo-
pher D Manning. 2018. Hotpotqa: A dataset for
diverse, explainable multi-hop question answering.
In Proceedings of the 2018 Conference on Empiri-
cal Methods in Natural Language Processing, pages
2369–2380.
Yifei Zhang, Hao Zhu, Zixing Song, Piotr Koniusz, and
Irwin King. 2022. COSTA: covariance-preserving
feature augmentation for graph contrastive learning.
In KDD ’22: The 28th ACM SIGKDD Conference on
Knowledge Discovery and Data Mining, Washington,
DC, USA, August 14 - 18, 2022, pages 2524–2534.
ACM.
A
Experimental Settings
A.1
Pre-Training Dataset
Cloze-like Samples. We follow the method pro-
posed by SSPT (Glass et al., 2020b) to generate
cloze-like pre-training instances. Specifically, we
first choose a sentence in the Wikipedia corpus and
randomly replace an entity or noun phrase with the
special token [BLANK]. The new sentence will
be considered as a query. Based on the query, we
retrieve a paragraph that contains the masked term
as its corresponding passage. Due to the time and
computational resource limitations, we finally col-
lect 5 million unique pre-training examples in En-
glish for our pre-training, which is one-sixth of the
original SSPT method.
Natural Samples. For each scloze = (qc, p, a), we
use a public T5-base model3 to generate natural
queries qn given (p, a). It is fine-tuned for answer-
aware question generation using the SQuADv1.1
train set. If answer a is empty, qn is not gener-
ated and loss functions related to snatural will not
be included during training. We do not apply ex-
tra filtering or other quality control operations for
generated questions.
A.2
Evaluation
We use the official model evaluation scripts of
SQuADv1.14 and MRQA5 to calculate the F1 and
EM metrics between predictions and ground truth
answers. Besides, we employ zero-shot F1 and
zero-shot EM to quantify the performance of mod-
els without fine-tuning. Official training and devel-
opment sets are used in all experiments.
B
Implementation Details
All model architectures are based on the 12-layer
BERT-base model with 110M parameters, and we
employed Google’s original implementation of the
BERT model published in the Huggingface6 to
build up our encoder. The training batch size for
pre-training and fine-tuning are 32 and 8. Total
training steps for MCROSS and other baseline mod-
els are both kept to 156,250. The max sequence
3https://huggingface.co/valhalla/
t5-base-qg-hl
4https://github.com/allenai/bi-att-flow/blob/
master/squad/evaluate-v1.1.py
5https://github.com/mrqa/
MRQA-Shared-Task-2019
6https://huggingface.co/docs/transformers/
v4.21.2/en/model_doc/bert#transformers.
BertForQuestionAnswering
4329

## Page 7

D
Dataset
F1
EM
DKL
SQuADv1.1
88.95
81.60
NewsQA
66.45
51.33
TriviaQA
72.06
66.41
DCosine
SQuADv1.1
88.47
80.79
NewsQA
65.98
50.40
TriviaQA
69.73
64.24
Table 4: Comparison between choosing DKL and DCosine
length of the transformer encoder is 384. In all ex-
periments, we use the Adam optimizer with a learn-
ing rate of 2e-5. The MoCo momentum m is set
to 0.999, queue size 32,000, moco ratio λMoCo 1.0
and temperature τ 0.05. Models are implemented
on PyTorch. When the passage length exceeds the
max sequence length, we follow the sliding win-
dow strategy proposed for BERT transformers in
both fast/slow encoder structures.
During QA prediction, we apply the constraint
sta ≤ena to filtering out implausible answer spans
and then select the ones with the highest joint prob-
ability p(sta) × p(ena) as results.
C
Design Choice: KL Divergence
The performance gain of the MCROSS(UNI)
method choosing KL divergence DKL over cosine
similarity DCosine as similarity function D is shown
in Table 4.
D
Space and Time Complexity
The additional parameters of the answer prediction
layer come from Eq. (1). The number of parameters
is (768 + 1) ∗2 = 1, 538, which is negligible
in front of the parameters in BERT-base (110M).
Training of the SSPT baselines and the MCROSS
method took approximately 40 hours each on 8
V-100 GPUs.
4330
