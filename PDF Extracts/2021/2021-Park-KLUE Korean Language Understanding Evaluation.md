---
title: "2021-Park-KLUE Korean Language Understanding Evaluation - PDF Extract"
source_pdf: "2021-Park-KLUE Korean Language Understanding Evaluation.pdf"
pages: 76
extracted_at: "2026-02-13T09:50:28.680717"
---

# PDF Extract: 2021-Park-KLUE Korean Language Understanding Evaluation

**Source PDF:** 2021-Park-KLUE Korean Language Understanding Evaluation.pdf
**Total Pages:** 76

---

## Content

```
--- Page 1 ---

KLUE: Korean Language Understanding Evaluation
Sungjoon Park*
Upstage, KAIST
sungjoon.park@kaist.ac.kr
Jihyung Moon*
Upstage
jihyung.moon@upstage.ai
Sungdong Kim*
NAVER AI Lab
sungdong.kim@navercorp.com
Won Ik Cho*
Seoul National University
tsatsuki@snu.ac.kr
Jiyoon Han†
Yonsei University
clinamen35@yonsei.ac.kr
Jangwon Park
jangwon.pk@gmail.com
Chisung Song
daydrilling@gmail.com
Junseong Kim
Scatter Lab
junseong.kim@scatterlab.co.kr
Youngsook Song
KyungHee University
youngsoksong@khu.ac.kr
Taehwan Oh†
Yonsei University
ghksl0604@yonsei.ac.kr
Joohong Lee
Scatter Lab
joohong@scatterlab.co.kr
Juhyun Oh†
Seoul National University
411juhyun@snu.ac.kr
Sungwon Lyu
Kakao Enterprise
james.ryu@kakaoenterprise.com
Younghoon Jeong
Sogang University
boychaboy@sogang.ac.kr
Inkwon Lee
Sogang University
md98765@naver.com
Sangwoo Seo
Scatter Lab
sangwoo@scatterlab.co.kr
Dongjun Lee
humanbrain.djlee@gmail.com
Hyunwoo Kim
Seoul National University
hyunw.kim@vl.snu.ac.kr
Myeonghwa Lee
KAIST
myeon9h@kaist.ac.kr
Seongbo Jang
Scatter Lab
seongbo@scatterlab.co.kr
Seungwon Do
seungwon.do1@gmail.com
Sunkyoung Kim
KAIST
sunkyoung@kaist.ac.kr
Kyungtae Lim
Hanbat National University
ktlim@hanbat.ac.kr
Jongwon Lee
mybizzer@gmail.com
Kyumin Park
KAIST
pkm9403@kaist.ac.kr
Jamin Shin
Riiid AI Research
jshin49@gmail.com
Seonghyun Kim
bananaband657@gmail.com
Lucy Park
Upstage
lucy@upstage.ai
Alice Oh**
KAIST
alice.oh@kaist.edu
Jung-Woo Ha**
NAVER AI Lab
jungwoo.ha@navercorp.com
Kyunghyun Cho**
New York University
kyunghyun.cho@nyu.edu
Abstract
We introduce Korean Language Understanding Evaluation (KLUE) benchmark. KLUE is a collection
of 8 Korean natural language understanding (NLU) tasks, including Topic Classiﬁcation, Semantic
Textual Similarity, Natural Language Inference, Named Entity Recognition, Relation Extraction,
Dependency Parsing, Machine Reading Comprehension, and Dialogue State Tracking. We build
all of the tasks from scratch from diverse source corpora while respecting copyrights, to ensure
accessibility for anyone without any restrictions. With ethical considerations in mind, we carefully
design annotation protocols. Along with the benchmark tasks and data, we provide suitable evaluation
metrics and ﬁne-tuning recipes for pretrained language models for each task. We furthermore release
the pretrained language models (PLM), KLUE-BERT and KLUE-RoBERTa, to help reproducing
baseline models on KLUE and thereby facilitate future research. We make a few interesting ob-
servations from the preliminary experiments using the proposed KLUE benchmark suite, already
demonstrating the usefulness of this new benchmark suite. First, we ﬁnd KLUE-RoBERTaLARGE
outperforms other baselines, including multilingual PLMs and existing open-source Korean PLMs.
Second, we see minimal degradation in performance even when we replace personally identiﬁable
information from the pretraining corpus, suggesting that privacy and NLU capability are not at odds
with each other. Lastly, we ﬁnd that using BPE tokenization in combination with morpheme-level
pre-tokenization is effective in tasks involving morpheme-level tagging, detection and generation.
In addition to accelerating Korean NLP research, our comprehensive documentation on creating
KLUE will facilitate creating similar resources for other languages in the future. KLUE is available
at https://klue-benchmark.com/.
*Equal Contribution. A description of each author’s contribution is available at the end of paper.
**Corresponding Authors.
†Work done at Upstage.
arXiv:2105.09680v4  [cs.CL]  2 Nov 2021

--- Page 2 ---

Contents
1
Introduction
4
1.1
Summary
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4
2
Source Corpora
8
2.1
Corpora Selection Criteria
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
2.2
Selected Corpora . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
2.2.1
Potential Concerns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11
2.3
Preprocessing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11
2.4
Task Assignment
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12
3
KLUE Benchmark
13
3.1
Topic Classiﬁcation (TC) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13
3.1.1
Dataset Construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13
3.1.2
Evaluation Metric . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
3.1.3
Related Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
3.1.4
Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
15
3.2
Semantic Textual Similarity (STS) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
3.2.1
Dataset Construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
3.2.2
Evaluation Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
18
3.2.3
Related Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
3.2.4
Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
3.3
Natural Language Inference (NLI) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20
3.3.1
Dataset Construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20
3.3.2
Evaluation Metric . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
23
3.3.3
Related Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
23
3.3.4
Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24
3.4
Named Entity Recognition (NER)
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
25
3.4.1
Dataset Construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
25
3.4.2
Evaluation Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
26
3.4.3
Related Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
27
3.4.4
Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
27
3.5
Relation Extraction (RE) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
28
3.5.1
Data Construction
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
28
3.5.2
Evaluation Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
31
3.5.3
Related Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
32
3.5.4
Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
32
3.6
Dependency Parsing (DP) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
33
3.6.1
Dataset Construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
33
3.6.2
Evaluation Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
34
2

--- Page 3 ---

3.6.3
Related Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
36
3.6.4
Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
36
3.7
Machine Reading Comprehension (MRC) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
37
3.7.1
Dataset Construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
37
3.7.2
Evaluation Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
40
3.7.3
Analysis
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
41
3.7.4
Related Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
42
3.7.5
Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
43
3.8
Dialogue State Tracking (DST) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
44
3.8.1
Dataset Construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
44
3.8.2
Evaluation Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
48
3.8.3
Analysis
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
48
3.8.4
Related Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
48
3.8.5
Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
49
4
Pretrained Language Models
50
4.1
Language Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
50
4.2
Existing Language Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
52
5
Fine-tuning Language Models
52
5.1
Task-Speciﬁc Architectures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
52
5.1.1
Single Sentence Classiﬁcation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
53
5.1.2
Sentence Pair Classiﬁcation / Regression
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
53
5.1.3
Multiple-Sentence Slot-Value Prediction . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
53
5.1.4
Sequence Tagging
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
54
5.2
Fine-Tuning Conﬁgurations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
55
5.3
Evaluation Results
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
55
5.4
Analysis of Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
55
6
Ethical Considerations
57
6.1
Copyright and Accessibility
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
57
6.2
Toxic Content . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
57
6.3
Personally Identiﬁable Information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
58
7
Related Work
58
8
Discussion
59
9
Conclusion
60
Index
74
A Dev Set Results
76
3

--- Page 4 ---

1
Introduction
A major factor behind recent success of pretrained language models, such as BERT [30] and its variants [82, 22, 49]
as well as GPT-3 [110] and its variants [111, 76, 9], has been the availability of well-designed benchmark suites
for evaluating their effectiveness in natural language understanding (NLU). GLUE [133] and SuperGLUE [132]
are representative examples of such suites and were designed to evaluate diverse aspects of NLU, including syntax,
semantics and pragmatics. The research community has embraced GLUE and SuperGLUE, and has made rapid progress
in developing better model architectures as well as learning algorithms for NLU.
The success of GLUE and SuperGLUE has sparked interest in building such a standardized benchmark suite for other
languages, in order to better measure the progress in NLU in languages beyond English. Such efforts have been pursued
along two directions. First, various groups in the world have independently created language-speciﬁc benchmark suites;
a Chinese version of GLUE (CLUE [142]), a French version of GLUE (FLUE [72]), an Indonesian variant [137], an
Indic version [57] and a Russian variant of SuperGLUE [125]. On the other hand, some have relied on both machine
and human translation of existing benchmark suites for building multilingual version of the benchmark suites which
were often created initially in English. These include for instance XGLUE [78] and XTREME [54]. Although the latter
approach scales much better than the former does, the latter often fails to capture societal aspects of NLU and also
introduces various artifacts arising from translation.
To this end, we build a new benchmark suite for evaluating NLU in Korean which is the 13-th most used language in
the world according to [34] but lacks a uniﬁed benchmark suite for NLU. Instead of starting from existing benchmark
tasks or corpora, we build this benchmark suite from ground up by determining and collecting base corpora, identifying
a set of benchmark tasks, designing appropriate annotation protocols and ﬁnally validating collected annotation. This
allows us to preemptively address and avoid properties that may have undesirable consequences, such as copyright
infringement, annotation artifacts, social biases and privacy violations.
In the rest of this section, we summarize a series of decisions and principles that went behind creating KLUE.
1.1
Summary
In designing the Korean Language Understanding Evaluation (KLUE), we aim to make KLUE; 1) cover diverse tasks
and corpora, 2) accessible to everyone without any restriction, 3) include accurate and unambiguous annotations, 4)
mitigate AI ethical issues. KLUE is safe to use for both building and evaluating systems, because KLUE has proactively
addressed potential ethical issues. Here, we describe more in detail how these principles have guided creating KLUE
from task selection, corpus selection, annotation protocols, determining evaluation metrics to baseline construction.
Design Principles
First, let us describe each design principle in detail:
• Covering diverse tasks and corpora: To cover diverse aspects of language understanding, we choose eight tasks that
cover diverse domain, including news, encyclopedia, user review, smart home queries and task-oriented dialogue, and
diverse style, both formal and colloquial.
• Accessible to everyone without any restriction: It is critical for a benchmark suite to be accessible by everyone for it
to serve as a true guideline in evaluating and improving NLU systems. We thus use only corpora and resources that
can be freely copied, redistributed, remixed and transformed for the purpose of benchmarking NLU systems.
• Obtaining accurate and unambiguous annotations: Ambiguity in benchmark tasks leads to ambiguity in evaluation,
which often leads to the discrepancy between the quality of an NLU system measured by the benchmark and its true
quality. In order to minimize such discrepancy, we carefully design annotation guidelines of all tasks and improve
them over multiple iterations, to avoid accurate annotations.
• Mitigating AI ethical issues: It has been repeatedly observed that large-scale language models can and often do
amplify social biases embedded in text used to train them [95]. In order to disincentivize such behaviors, we
proactively remove examples, from both unlabeled and labeled corpora, that reﬂect social biases, contain toxic content
and have personally identiﬁable information (PII), both manually and automatically. Social biases are deﬁned as
overgeneralized judgment on certain individuals or group based on social attributes (e.g., gender, ethnicity, religion).
Toxic contents include insults, sexual harassment and offensive expressions.
Diverse Task Selection
We carefully choose the following eight NLU tasks with two goals; 1) to cover as diverse
aspects of NLU in Korean, and 2) to minimize redundancy among the tasks. See Table 1 for their formats, evaluation
granularity and other properties:
• Topic Classiﬁcation (TC): classify a single sentence into a single class.
4

--- Page 5 ---

• Semantic Textual Similarity (STS): judge the semantic similarity between two sentences.
• Natural Language Inference (NLI): classify whether the ﬁrst sentence entails the second one.
• Named Entity Recognition (NER): extract entities from a sentence.
• Relation Extraction (RE): predict the relationship between two entities within a sentence.
• Dependency Parsing (DP): predict the syntactic structure of a sentence.
• Machine Reading Comprehension (MRC): identify an answer span within a paragraph given a question.
• Dialogue State Tracking (DST): track the state of a goal-oriented dialogue.
Source Corpora Collection
We have actively sought corpora that are accessible, cover diverse domains and topics
and are written in modern Korean. This active search has ended up with the following ten source corpora from which we
derive task-speciﬁc corpora. These ten sources are released under CC BY(-SA) license or not considered as copyrighted
work, permitting 1) derivative work, 2) redistribution, and 3) commercial use:
• News Headlines from Yonhap News Agency
• Wikipedia
• Wikinews
• Wikitree
• Policy News
• ParaKQC
• Airbnb Reviews
• NAVER Sentiment Movie Corpus
• The Korea Economics Daily News
• Acrofan News
Before sending a subset for annotation, we ﬁlter them to remove noisy, toxic or socially biased content, as well as PII.
This is done automatically using predeﬁned rules and machine learning models.
Considerations in Annotation
For each task, we annotate a subset from the source corpora. In doing so, we take
into account three major considerations below:
• Better reﬂection of linguistic characteristics of Korean: Many existing Korean datasets were constructed as a
part of multilingually aligned benchmarks, and they do not fully reﬂect linguistic characteristics of Korean such
as agglutinative nature in named entity recognition (NER) [100], or tagset in part-of-speech (POS) tagging and
dependency parsing [86, 46]. We write and revise annotation guidelines more appropriately to the linguistic property
of Korean.
• Obtaining accurate annotations: We provide crowdworkers or select participants with carefully designed annotation
guidelines and improve them over multiple iterations, in order to reduce the ambiguity of annotation process as well
as to mitigate known artifact issues. In particular, we often ﬁlter out examples for which annotators cannot easily
agree with each other.
• Mitigating harmful social bias and removing PII: To disincentivize socially biased NLU systems [7], we explicitly
instruct annotators as well as inspectors to manually mark and/or exclude examples that are unacceptable according
to our principle of ethics. Our deﬁnitions of bias and hate speech follow Moon et al. [92]. We denote bias as an
overgeneralized prejudice on certain groups or individuals based on the following traits: gender, race, background,
nationality, ethnic group, political stance, skin color, religion, disability, age, appearance, (socio-)economic status,
and occupations. In the case of hate speech, we include offensive, aggressive, insulting, or sarcastic contents. We
identify a list of personally identiﬁable information (PII) following KISA (Korea Internet and Security Agency)
guideline,1 whose information is related to a living individual based on personal information protection act of Korea.2
We do not consider public ﬁgure’s name as personal information.3
1https://www.kisa.or.kr/public/laws/laws2_View.jsp?cPage=1&mode=view&p_No=282&b_No=282&d_No=3
2https://www.law.go.kr/LSW//lsInfoP.do?lsiSeq=213857&chrClsCd=010203&urlMode=engLsInfoR&viewCls=engLsInfoR#0000
3See the precedent set by the Supreme Court in Korea: 대법원2011. 9. 2. 선고2008다42430 전원합의체판결available at
https://glaw.scourt.go.kr/wsjo/panre/sjo100.do?contId=2060159&q=2008%EB%8B%A442430.
5

--- Page 6 ---

Table 1: Task Overview
Name
Type
Format
Eval.
Metric
#
Class
{|Train|,
|Dev|,
|Test|}
Source
Style
KLUE-TC
(YNAT)
Topic
Classiﬁcation
Single Sentence
Classiﬁcation
Macro F1
7
45k,
9k,
9k
News
(Headline)
Formal
KLUE-STS
Semantic
Textual
Similarity
Sentence
Pair
Regression
Pearson’s r,
F1
[0, 5]
2
11k,
0.5k,
1k
News,
Review,
Query
Colloquial,
Formal
KLUE-NLI
Natural
Language
Inference
Sentence
Pair
Classiﬁcation
Accuracy
3
25k,
3k,
3k
News,
Wikipedia,
Review
Colloquial,
Formal
KLUE-NER
Named
Entity
Recognition
Sequence
Tagging
Entity-level Macro F1
Character-level Macro F1
6,
12
21k,
5k,
5k
News,
Review
Colloquial,
Formal
KLUE-RE
Relation
Extraction
Single Sentence
Classiﬁcation
(+2 Entity Spans)
Micro F1 (without no_relation),
AUPRC
30
32k,
8k,
8k
Wikipedia,
News
Formal
KLUE-DP
Dependency
Parsing
Sequence
Tagging
(+ POS Tags)
Unlabeled Attachment Score,
Labeled Attachment Score
# Words,
38
10k,
2k,
2.5k
News,
Review
Colloquial,
Formal
KLUE-MRC
Machine
Reading
Comprehension
Span Prediction
Exact Match,
ROUGE-W (LCCS-based F1)
2
12k,
8k,
9k
Wikipedia,
News
Formal
KLUE-DST
(WoS)
Dialogue
State
Tracking
Slot-Value
Prediction
Joint Goal Accuracy
Slot Micro F1
(45)
8k,
1k,
1k
Task
Oriented
Dialogue
Colloquial
Evaluation Metrics
The diversity of tasks in KLUE implies that we must choose a proper set of evaluation metrics
for each task carefully and separately. Here, we list the tasks and describe how we choose the evaluation metrics for
each of these tasks.
• KLUE-TC (Yonhap News Agency Topic Classiﬁcation (YNAT)): We formulate KLUE-TC as a multi-class classiﬁ-
cation problem with seven classes. Because the headline alone is often not enough to precisely identify the proper
class to which it belongs, we manually annotate and keep 70,000 headlines, for each of which there was a majority
consensus on the class by the annotators. We then use the consensus classes as ground-truth classes and use macro F1
score as an evaluation metric.
• KLUE-STS: In KLUE-STS the similarity between each pair of sentences is annotated with the average (real-valued)
similarity rating (between 0 and 5). We measure the quality of an NLU model in two different ways. First, we use the
Pearson correlation coefﬁcient between the real-valued target and prediction. Second, we compute the F1 score after
binarizing the real-valued similarity rating as in paraphrase detection.
• KLUE-NLI: Similar to existing NLI datasets, such as SNLI [8] and MNLI [138], we use classiﬁcation accuracy, and
this is appropriate, as we create KLUE-NLI dev/test set to have a balanced class distribution.
• KLUE-NER: In KLUE-NER, a named entity recognizer is expected to output BIO tags and also categorize each
detected entity into one of six types; person, location, organization, date, time and quantity. To account for rich
morphology in Korean, we use entity-level and character-level F1 score to evaluate the quality of the detection to
evaluate the recognizer’s ability in determining the type of each entity.
• KLUE-RE: KLUE-RE is designed as a sentence classiﬁcation task in which the input is a single sentence with two
marked entities and the output is their relationship out of 30 types. We use two evaluation metrics. The ﬁrst one is
micro F1 score, considering only meaningful types (excluding no relationship), which allows us to evaluate the NLU
system’s ability to identify a ﬁne-grained relationship between a pair of entities. The second one is the area under the
precision-recall curve (AUPRC), which gives us a holistic view into the quality of the relation extraction model in
question.
• KLUE-DP: Following standard practice in dependency parsing, we use both unlabeled attachment score (UAS) and
labeled attachment score (LAS) to evaluate a dependency parser. We annotate and use both formal and informal text
6

--- Page 7 ---

(subsets from the news corpora and colloquial review corpora, respectively), which allows us to perform ﬁne-grained
analysis across multiple domains.
• KLUE-MRC: Similarly to KLUE-NER, KLUE-MRC is framed as a span prediction problem. We keep character-level
exact match (EM) for comparison against existing datasets, while we propose to use ROUGE-W which measures the
F1 score based on the longest common consecutive subsequence (LCCS) between the ground-truth and predicted
answer spans. The latter handles rich morphology of Korean as well as the former does while being more interpretable.
• KLUE-DST (Wizard of Seoul, WoS): We formulate KLUE-DST as a multiple-sentence slot-value prediction task, and
evaluate an NLU system using two metrics. The ﬁrst metric is the joint goal accuracy which measures whether all the
slots were correctly predicted, while the other metric is average F1 score. Because the former treats all examples for
which not all slots were correctly ﬁlled in, it often fails to distinguish similarly performing NLU systems. We address
this shortcoming by reporting both the joint goal accuracy and slot F1 score. We furthermore build it using multiple
domains in order to facilitate ﬁner-grain analysis.
Baselines
In addition to creating a benchmark suite, we also build and publicly release a set of strong baselines based
on large-scale pretrained language models. In due course, we pretrain and release large-scale language models for
Korean ourselves, which will reduce the burden of retraining these large-scale models from individual researchers. We
also use several existing multilingual pretrained language models and open-source Korean-speciﬁc models in addition
to our own models, to gain further insights into the proposed KLUE benchmark. We present all the results in Table 32
and summarize a few interesting observations here. First, Korean-speciﬁc language models generally outperform
multilingual models. Second, different models perform best on different tasks when controlled for their sizes; KLUE-
BERT performs best for YNAT and WoS, KLUE-RoBERTa for KLUE-RE and KLUE-MRC, and KoELECTRABASE
for KLUE-STS and KLUE-NLI. Third, as we increase the model size, KLUE-RoBERTaLARGE ends up outperforming
all the other models in all the tasks other than KLUE-NER. Lastly, we observe that removing PII has minimal effect on
the downstream task performances, and our tokenization scheme, morpheme-based subword tokenization, is effective in
tasks involving tagging, detection and even generation at the morpheme level.
Task Overview
In Table 1, we summarize the resulting eight KLUE tasks, listing important properties, such as type,
format, evaluation metrics and annotated data sizes. In the rest of the paper, we will walk through the process by which
each and every one of these tasks was constructed much more in detail.
7

--- Page 8 ---

2
Source Corpora
We build KLUE from scratch, instead of putting together existing datasets, which has been a common practice in
setting up benchmarks. We investigate available textual resources, and document the process in order to provide better
understanding on how and why we select some corpora but not others. We adopt the recently proposed documentation
frameworks; datasheets [41] and data statements [6]. Based on these frameworks, we document and provide more
information to carefully describe our protocol.
2.1
Corpora Selection Criteria
We consider two criteria when sourcing a set of corpora to build a source corpus from which task-speciﬁc corpora are
derived and annotated. The ﬁrst criterion is accessibility. As the main purpose of KLUE is to facilitate future NLP
research and development, we ensure KLUE comes with data that can be used and shared as freely as possible to all.
The second criterion is the quality and diversity. We ensure each example with these corpora is of certain quality by
removing low-quality text and also the balance is met between formal and colloquial text within these corpora.
Accessibility
Unlike Wang et al. [132], Hu et al. [54], Kakwani et al. [57], we design KLUE to reach as broad and
diverse researchers as possible by avoiding any restriction on afﬁliations of users as well as the purpose of its use.
Furthermore, we acknowledge the rapid pace of advances in the ﬁeld and allow users to reproduce and redistribute
KLUE to prolong its usability as a standard benchmark of NLU. To do so, we build and release the source corpus with
CC BY-SA.4
The source corpus, or a set of source corpora, satisﬁes the following conditions:
• No restriction on the use: We allow both non-commercial and commercial use of KLUE, in order to accommodate
the recent trend of fundamental research from industry labs.
• Derivatives: We allow users to freely refurbish any part of KLUE to ﬁrst address any shortcomings, such as
unanticipated artifacts, ethical issues and annotation mistakes, and second derive more challenging benchmarks for
the future. This is similar to what has been done with SQuAD 2.0 [113] which was created to include SQuAD 1.1
[112].
• Redistributable: We allow KLUE benchmark datasets to be distributed by anyone via any channel as long as the
proper attribution is given to the original creators of KLUE. We deliberately make this decision to avoid situations
where only a limited and select group of researchers have a monopoly on resources, ultimately hindering the progress
overall. This is in reaction to some of the existing Korean corpora which come together with restrictive policies,
often preventing derivatives as well as redistribution, and are only accessible by researchers in Korea after acquiring
permissions from the corpus publishers who are often public institutions in Korea. KLUE avoids such preventive
policies in order to maximally facilitate the progress in Korean NLP.
Because most of the existing datasets do not meet these conditions, we curate the source corpus from scratch by
considering only those resources that either come with one of the following licenses: CC0,5 CC BY,6 CC BY-SA,7 and
other similar licenses such as KOGL Type 1,8 are not protected by the copyright act according to the latest copyright act
in Korea,9 or have been explicitly provided to us by copyright holders under contracts. We end up 20 candidate corpora
in total, of which subset is selected to form a source corpus set of KLUE. They are listed in Table 2.
Quality and Diversity
Among these 20 source corpora, we select a subset of ten corpora to form the source corpus
and to build the KLUE benchmark. In doing so, we consider the following criteria; 1) the corpus should not be speciﬁc
to narrow domains (diversity), 2) the corpus must be written in contemporary Korean (quality), 3) the corpus should
not be dominated by contents that have privacy or toxicity concerns (quality) and 4) the corpus must be amenable to
annotation for at least one of the eight benchmark tasks. Furthermore, we select the subset of corpora to cover both
formal and colloquial uses.
4https://creativecommons.org/licenses/by-sa/4.0/
5https://creativecommons.org/publicdomain/zero/1.0/
6https://creativecommons.org/licenses/by/4.0/
7https://creativecommons.org/licenses/by-sa/4.0/
8https://www.kogl.or.kr/info/license.do#05-tab
9See https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EC%A0%80%EC%9E%91%EA%B6%8C%EB%B2%95 for the copyright act
which went effective as of Dec 8 2020.
8

--- Page 9 ---

Table 2: Collected source corpora. The corpora in the ﬁrst section are not protected by copyright act. Speciﬁcally, News
Headlines are not classiﬁed as a work due to their lack of creativity and Judgements are not protected works under
Article 7, Act 3. National Assembly Minutes and Patents, made in National Assembly, shall not apply the copyright
act by Article 24, Act 2. The second section is a collection of corpora under the permissive licenses. The last section
corpora, KED and Acrofan, are originally prohibited from creating derivative works, however, we release such condition
by exclusive contract. For the column, Volume, we denote Small as corpus size under 1k, Medium as in between 1k and
50k, and Large as over 50k. Bold represents our ﬁnal source corpora to build KLUE benchmark.
Dataset
License
Domain
Style
Ethical
Risks
Volume
Contemporary
Korean
News Headlines
N/A
News (Headline)
Formal
Low
Large
o
Judgments
Public Domain
Law
Formal
Low
Large
o
National Assembly
Minutes
Public Domain
Politics
Colloquial
Medium
Large
o
Patents
Public Domain
Patent
Formal
Low
Large
o
Wikipedia
CC BY-SA 3.0
Wikipedia
Formal
Low
Large
o
Wikibooks
CC BY-SA 3.0
Book
Formal
Low
Medium
x
Wikisource
CC BY-SA 3.0
Law
Formal
Low
Medium
x
Book
Wikinews
CC BY 2.5
News
Formal
Low
Small
o
Wikitree
CC BY-SA 2.0
News
Formal
Medium
Large
o
Librewiki
CC BY-SA 3.0
Wiki
Formal
Medium
Large
o
Zetawiki
CC BY-SA 3.0
Wiki
Formal
Medium
Large
o
Policy News
KOGL Type 1
News
Formal
Low
Medium
o
NIKL Standard
Korean Dictionary
CC BY-SA 2.0
Dictionary
Formal
Low
Large
o
Open
Korean Dictionary
CC BY-SA 2.0
Dictionary
Formal
Low
Large
o
ParaKQC
CC BY-SA 4.0
Smart Home
Utterances
Colloquial
Low
Medium
o
Airbnb Reviews
CC0 1.0
Review
Colloquial
Medium
Large
o
NAVER Sentiment
Movie Corpus (NSMC)
CC0 1.0
Review
Colloquial
Medium
Large
o
NAVER Entertainment
News Reviews
CC BY-SA 4.0
Review
Colloquial
High
Large
o
Acrofan News
CC BY-SA 4.0
for KLUE-MRC by Contract
News
Formal
Low
Large
o
The Korea Economics
Daily News
CC BY-SA 4.0
for KLUE-MRC by Contract
News
Formal
Low
Large
o
The Final Source Corpora
Based on these criteria and decisions, we choose News Headlines, Wikipedia, Wikinews,
Policy News, The Korea Economics Daily News, and Acrofan News for (relatively) formal text.10 For more colloquial
text, we use ParaKQC, Airbnb Reviews, and NAVER Sentiment Movie Corpus. These are marked bold in Table 2.
2.2
Selected Corpora
Here, we describe in more detail general characteristics and potential concerns of each source corpus. We document the
collection mechanisms, timeframe, domain, style, license, and background of each corpus as well.
10Although Wikitree was found to include some contents that could be considered unethical, socially biased and/or of low quality
in general, we include it, as Wikitree is the largest source of license-free news articles. We address these problematic contents via
annotation.
9

--- Page 10 ---

News Headlines
from Yonhap News Agency (YNA).
YNA is a dataset of news headlines from Yonhap News Agency, one of the representative news agencies in South Korea.
Using news headlines does not infringe on copyrights, unlike the actual contents of news articles. We include YNA
from 2016 to 2020 with a main purpose of using it for a single sentence classiﬁcation task.
Wikipedia (WIKIPEDIA)
WIKIPEDIA is an open encyclopedia written in a formal style and has been widely used
for language modeling and dataset construction across many languages, because of its high-quality and well-curated
text. The Wikipedia articles in Korean are released under CC BY-SA. We use the dump of Korean Wikipedia released
on December 1st, 2020.
Wikinews (WIKINEWS)
WIKINEWS implements collective journalism and provides news articles for free under
CC BY, both of which are rare for news articles. Due to these properties, we include it in the source corpora despite its
limited number of articles (approximately 500 of them).
Wikitree (WIKITREE)
WIKITREE is a dataset of news articles derived from Wikitree, the ﬁrst Korean social
media-based news platform that started in 2010. Although there are concerns that the articles on Wikitree are in many
cases advertisement-in-disguise or click-bait headlines and express undesirable biases, we include WIKITREE, as it is
the only large-scale source of news articles that are freely distributed under CC BY-SA, to the best of our knowledge. It
also covers a broad spectrum of topics, including politics, economics, culture and life. We use the articles published
between 2016 and 2020. We conduct more thorough manual inspection of WIKITREE is more thoroughly conducted.
See Section 2.2.1 for more details.
Policy News (POLICY)
POLICY is a dataset of various articles distributed by ministries, national ofﬁces, and
national commissions of South Korea. It covers statements, notices, or media notes reported by the government agencies.
POLICY is protected under the Korea Open Government License (KOGL) Type 1, which permits users to share and
remix even for commercial purposes, if attribution is properly done. We include articles released up to the end of 2020.
ParaKQC (PARAKQC)
PARAKQC is a dataset of 10,000 utterances aimed at smart home devices, consisting of
1,000 intents of 10 similar queries [18]. It covers various topics which are probable when interacting with smart home
speakers, such as scheduling an appointment and asking about the weather. PARAKQC is available under CC BY-SA.
Airbnb Reviews (AIRBNB)
AIRBNB is a review dataset sourced from the publicly accessible portion of the Airbnb
website. More speciﬁcally, we start from the existing multilingual Airbnb reviews collected and preprocessed by
Inside Airbnb.11 We identify a subset of reviews written in Korean from this multilingual Airbnb corpus, using regular
expressions. Reviews are from hosts and guests who have completed their stays. AIRBNB is available under CC0.
NAVER Sentiment Movie Corpus (NSMC)
NSMC is a movie review dataset scraped from NAVER Movies.12 The
reviews are written by online users. Each review comes with both the textual content and the binary sentiment label.
There are 200,000 reviews in total. The numbers of positive and negative reviewers are balanced. NSMC is available
under CC0.
Acrofan News (ACROFAN)
ACROFAN is a corpus consisting of news articles released by ACROFAN. Most articles
are press release-like in that they often introduce new products or events of companies. The formats and styles are
quite templated, although the articles cover a broad set of categories including automobiles, IT, startups, big companies,
energy, beauty and fashion. We obtain the permission and use of the articles from ACROFAN for KLUE. We include
news articles published between Dec 2020 and Jan 2021.
The Korea Economics Daily News (The Korea Economy Daily)
The Korea Economy Daily is a news corpus
consisting of articles from the Korea Economics Daily owned by Hankyung corporation. Korea Economics Daily is a
newspaper that mainly covers economic issues, but also publishes various topics such as politics, culture and IT topics.
The owner of the Korea Economics Daily and we have entered a contract to use news articles published between Jan
2013 and Dec 2015, provided by the Hankyung corporation, as a part of KLUE. This allows us to ensure high-quality,
well-curated news articles are included in KLUE. We release The Korea Economy Daily under CC BY-SA, with the
condition that these articles are used for the purpose of machine learning research.
11http://insideairbnb.com/get-the-data.html
12https://movie.naver.com/movie/point/af/list.nhn
10

--- Page 11 ---

2.2.1
Potential Concerns
Based on the ten selected corpora above, we list up and discuss some of the concerns here. Some concerns are focused
on the quality of data, while the others are more societal and ethical.
Toxic Content
Although news articles, such as those from YNA, WIKINEWS, WIKITREE, POLICY, ACROFAN,
and The Korea Economy Daily are better written and curated than user-generated contents, such as online reviews,
these articles nevertheless may reﬂect some of the biases possessed by journalists and editors. In particular, our manual
inspection has revealed that WIKITREE contains more of potentially problematic patterns than the other news sources,
due to the incentive structure that incentivizes articles that are more widely shared and clicked more on social media.
This is especially true with headlines of these articles, and we thus refrain from using the headlines from WIKITREE
when constructing TC. We also do not use the article contents from WIKITREE for MRC, as articles in whole often
exaggerate and emphasize sensational aspects of stories. We however use sentences sampled from WIKITREE when
building other task-speciﬁc corpora, as they are often complete and well-formed. We discard any problematic sentences
via annotation.
Unlike news articles, online reviews have higher potential to contain toxic content, although such tendency varies from
one corpus to another. Due to its peer-reviewing system, AIRBNB rarely contains reviews that are deemed toxic. NSMC
on the other hand contains comments that could be considered offensive toward movies, their casts, and their directors.
As there is a Korean hate speech dataset on review domains [92], we ﬁrst ﬁlter out toxic content with a detector trained
on the dataset. Then we discard problematic sentences via the annotation procedure.
All utterances of PARAKQC are carefully created based on a pre-deﬁned annotation guideline [18]. This largely
prevents toxic content from entering the corpus.
Personally Identiﬁable Information (PII)
Private information is any information that can be used to identify an
individual who is not considered a public ﬁgure.13 It includes for instance names, social security numbers, telephone
numbers and bank account numbers.
In the case of news articles, due to their nature of describing social events, they often contain PII such as names and
addresses. This is less so with online reviews, as they are often about public ﬁgures, such as actors, actresses and
directors, as we observe in NSMC. We however notice that the reviews in AIRBNB contain the names of hosts and/or
guests as well as their addresses, which must be carefully handled.
Some of the artiﬁcially generated utterances in PARAKQC do contain names. It is however our understanding that
these are mostly ﬁctional, meaning that they are unlikely to be truly private information.
2.3
Preprocessing
Because these source corpora come from various sources with varying levels of quality and curation, we carefully
preprocess them even before deriving a subset for each downstream task. In this section, we describe our preprocessing
routines which are applied after splitting each document within these corpora into sentences using the Korean Sentence
Splitter (KSS) v2.2.0.2.14 The proprocessing routines below are in addition to manual inspection and ﬁltering during
the annotation stage of each KLUE task.
Noise Filtering
We remove noisy and/or non-Korean text from the selected source corpora. We ﬁrst remove hashtags
(e.g., #JMT), HTML tags (e.g., <br>), bad characters (e.g., U+200B (zero-width space), U+FEFF (byte order mark)),
empty parenthesis (e.g., ()), and consecutive blanks. We then ﬁlter out sentences with more than 10 Chinese or Japanese
characters. For the corpora derived from news articles, we remove information about reporters and press, images, source
tags as well as copyright tags (e.g., copyright by ©).
Toxic Content Removal
In order to avoid introducing undesire contents and biases into KLUE, we use a number
of automatic tools to remove various undesirable sentences from the source corpora. Using the Korean hate speech
dataset [92], we train a gender bias15 and a hate speech detector.16 We discard a sentence which was predicted to exhibit
gender bias with the predictive score of at least 0.5. We also discard a sentence if it was deemed to be hate speech, with
13See the precedent set by the Supreme Court in Korea: 대법원2011. 9. 2. 선고2008다42430 전원합의체판결available at
https://glaw.scourt.go.kr/wsjo/panre/sjo100.do?contId=2060159&q=2008%EB%8B%A442430.
14https://github.com/hyunwoongko/kss
15https://huggingface.co/monologg/koelectra-base-v3-gender-bias
16https://huggingface.co/monologg/koelectra-base-v3-hate-speech
11

--- Page 12 ---

the predictive score of 0.9 or above. The thresholds are manually determined for each corpus. This approach work
well for online text, such as reviews, because the Korean hate speech dataset was constructed using online reviews. It
however does not work well for more formal text, such as found in news articles, based on which we decide against
using this strategy on The Korea Economy Daily, ACROFAN, and YNA.
PII Removal
To mitigate potential privacy issues, we get rid of sentences that contain private information. We detect
such sentences using regular expressions that match email addresses, URL and user-mentioning keywords, such as
‘@gildong’.
2.4
Task Assignment
We use these source corpora to build the datasets for the seven KLUE tasks, except for the DST. DST is built from
simulated dialogues by crowdworkers and does not require access to ofﬂine text. For each downstream task, we use a
subset of the source corpora, as described below:
• Topic Classiﬁcation (TC): We use YNA, which has been widely studied for a single sentence topic classiﬁcation task.
• Semantic Textual Similarity (STS): We use AIRBNB, POLICY, and PARAKQC to include diverse semantic contexts.
Intent queries and topic information of PARAKQC are useful when generating semantically related sentence pairs.
• Natural Language Inference (NLI): Following MNLI [138], we use multiple sources to construct NLI. We use
WIKITREE, POLICY, WIKINEWS, WIKIPEDIA, NSMC and AIRBNB.
• Named Entity Recognition (NER): Due to the nature of NER, we must build a corpus in which (named) entities
frequently appear. We thus use WIKITREE and NSMC, which enables us to include both formal and informal writing
styles.
• Relation Extraction (RE): We use WIKIPEDIA, WIKITREE and POLICY. These corpora tend to have long complete
sentences with the names of public ﬁgures and their relationships to various organizations.
• Dependency Parsing (DP): We balance formal and colloquial writing styles, while ensuring most of sentences from
selected corpora are complete. We end up using WIKITREE and AIRBNB. We choose AIRBNB over NSMC, because
the former has better-formed sentences.
• Machine Reading Comprehension (MRC): To provide informative passages, we use WIKIPEDIA, The Korea
Economy Daily, and ACROFAN.
12

--- Page 13 ---

3
KLUE Benchmark
The goal of KLUE is to provide high quality evaluation datasets and suitable automatic metrics to test a system’s ability
to understand Korean language. We provide comprehensive details on how we construct our 8 benchmark datasets.
We document 1) background of source corpus selection, 2) annotation protocol, 3) annotation process, 4) dataset split
strategy, and 5) design process of the metrics. In the annotation process, we guide workers to identify texts containing
potential ethical issues. See Section 1.1 for our deﬁnitions on bias, hate, and PII.
3.1
Topic Classiﬁcation (TC)
In topic classiﬁcation (TC), the goal is to train a classiﬁer to predict the topic of a given text snippet. Topic classiﬁcation
datasets typically consist of news or Wikipedia articles and their predeﬁned categories, because the categories often
represent topics [151].
We include TC in our KLUE benchmark, as inferring the topic of a text is a key capability that should be possessed by a
language understanding system. As a typical single sentence classiﬁcation task, other NLU benchmarks such as CLUE
[142] and IndicGLUE [57] also contain TNEWS and News Category Classiﬁcation. For Korean, no dataset has been
proposed for the task, which motivates us to construct the ﬁrst Korean topic classiﬁcation benchmark.
In this task, given a news headline, a text classiﬁer must predict a topic which is one of {politics, economy, society,
culture, world, IT/science, sports}. We formulate TC as single sentence classiﬁcation task following previous works
and use macro-F1 score as an evaluation metric.
3.1.1
Dataset Construction
Our TC benchmark is constructed in three stages. First, we collect headlines and their corresponding categories, then
we annotate the topics without looking at the categories and we ﬁnalize the dataset by deﬁning its split into training,
development and test splits considering the publication date and term appearances.
Source Corpora
We collect news headlines from online articles distributed by Yonhap News Agency (YNA), the
largest news agency in Korea. Speciﬁcally, we collect the headlines of the published articles from January 2016 to
December 2020 from Naver News.17 These articles belong to one of the following seven sections: politics, economy,
society, culture, world, IT/science, and sports. To balance the data across the different sections, we randomly sample
10,000 articles from each section, except for the sports and IT/science section. We collect 9,000 sports articles and
11,000 IT/science articles.
Unlike other benchmarks such as TNEWS in CLUE [142] or AG News [151], we exclude contents of the articles to
avoid infringement of copyright. Since the contents are protected as copyrighted work, we cannot freely use them
without permission. Headlines, on the other hand, are not considered copyrighted work based on a legal precedent [23].
Annotation Protocol
The headline of each article may not reﬂect all of the main content, such that the topic of the
headline may be different from the original news section of the article. To address this gap between the headline and the
corresponding article, we manually annotate the topics of the headlines.
We use SelectStar,18 a crowdsourcing platform in Korea, to annotate topics of the headlines. For each headline, three
annotators label topics independently from each other. Each annotator picks at most three topics in the order of relevance
among the seven categories. For precise annotation, we also present key terms of each topic to annotators. The terms are
subsections of corresponding topics in NAVER news platform as shown in Table 3.
An annotator may choose unable-to-decide if the headline does not contain sufﬁcient information to identify the
appropriate categories. Such an example is “Youngsoo Kim awards an appreciation plaque”. There is no clue about who
“Youngsoo Kim” is nor why he is awarding the appreciation plaque, in this headline.
We request the workers to report any headline that includes personally identiﬁable information (PII), expresses social
bias, or is hate speech. We discard the reported headline after manually reviewing them.
Annotation Process
We run a pilot study to select workers, before commencing the main annotation process. We
exclude workers who have continuously failed to assign a topic or have failed to agree with the other workers during the
pilot stage. As a result, 13 workers have passed this stage of pilot study.
17https://news.naver.com/
18https://selectstar.ai/
13

--- Page 14 ---

Table 3: The ﬁnal statistics of YNAT (KLUE-TC), provided with the key terms of each category.
Topic
Key Terms
|Train|
|Dev|
|Test|
Total
Politics
Blue House, Ministry, Parliament, North Korea
Political parties, Defense, Diplomacy
7,379
750
722
8,851
Economy
Stock, Finance, Industry Enterprise, Real estate
6,118
1,268
1,348
8,734
Society
Education, Labor, Journalism
Environment, Human rights, Food and drugs
5,133
3,740
3,701
12,574
Culture
Health, Transportation, Leisure, Hot places, Fashion,
Beauty, Performance, Exhibition, Books, Weather
5,751
1,387
1,369
8,507
World
Asia/Australia, America, Europe, Middle East/Africa
8,320
776
835
9,931
IT/Science
Mobile, IT, Internet Social media, Communication
Computer, Game, Scientiﬁc journalism
5,235
587
554
6,376
Sports
Baseball, Basketball, Volleyball, E-sports
7,742
599
578
8,919
Total
45,678
9,107
9,107
63,892
In the main annotation, the 13 selected workers labeled topics for all 70,000 headlines. During the annotation, they
reported 650 headlines are including potential PIIs (0.93%), 194 toxic contents (0.28%), and 2,515 unable-to-decides
(3.59%). We ﬁrst exclude such invalid 2,953 headlines. The sum of the three type of problematic headlines are larger
than the total value because of the intersection among them. After ﬁltering them, 67,047 headlines remain.
We look at agreements between three annotators in valid headlines. We consider each of the ﬁrst relevant topics chosen
by three annotators. In 40,359 (60.5%) headlines, all three annotators agree to a single topic. 23,353 (34.8%) had two
majority votes, and the other 3,155 (4.7%) did not reached to agreement. To make the headlines classiﬁed to a single
topic, we remove the others, leaving 63,892 headlines.
We examine the second and third relevant topics within an annotator. For 48,885 (69.8%) of headlines, three annotators
did not choose any second and third most relevant topic. Only 5,088 (7.3%) of headlines have the second topic in three
annotators. We thus assume that headlines are sufﬁciently represented by the ﬁrst relevant topics within an annotator.
We thus keep only a single topic for each headline, selected by at least two annotators out of three. The annotator
agreement on the resulting 63,892 headlines is fairly high (Krippendorff’s α = 0.713) [67].
Final Dataset
We partition the ﬁnal dataset, named YNAT (Yonhap News Agency dataset for Topic classiﬁcation),
into train, development, and test sets. We split the dataset based on the publication date. We include headlines published
after 2020 in the development and test sets, while those published before 2020 in the training set. To prevent TC models
attending speciﬁc keyword to classify the headlines, we also include headlines containing terms that have not appeared
in the train set in the development and test set. As shown in the Table 3, train, development, and test sets consist of
45,678, 9,107, and 9,107 examples, respectively.
3.1.2
Evaluation Metric
The evaluation metric for YNAT is macro F1 score. Macro F1 score is deﬁned as the mean of topic-wise F1 scores,
giving the same importance to each topic. Topic-wise F1 score weights recall and precision equally.
3.1.3
Related Work
Although many topic classiﬁcation datasets have been proposed in various languages, we are not aware of any public
TC benchmark in Korea. AG News [151], a widely used benchmark for topic classiﬁcation in English, consists of more
than a million of news articles collected from the news search engine ComeToMyHead,19 and categorizes articles into
four sections: world, sports, business, and science/technology. More recently, a number of TC benchmark datasets in
languages other than English were proposed. IndicGLUE [57] includes News Genre Classiﬁcation in Indian languages,
in which the goal is to classify a news article or news headline into seven categories; entertainment, sports, business,
19More information available in http://groups.di.unipi.it/~gulli/AG_corpus_of_news_articles.html
14

--- Page 15 ---

lifestyle, technology, politics, and crime. TNEWS from CLUE [142] is a news topic classiﬁcation task in Mandarin and
consists of 73K titles with 15 news categories, published in Toutiao.
Since a large language model ﬁne-tuned on TC benchmark can closely reach 100% accuracy as in IndicGLUE [57],
some researchers focus on making challenging TC benchmark to leave a room for improvement. CLUE [142] ﬁlters
easy examples in TNEWS by using 4-fold cross-validation, and then randomly shufﬂe and split the dataset. Instead
of designing our benchmark artiﬁcially more difﬁcult, we reﬂect how topic classiﬁcation is done in practice even a
baseline model reaches to good performance with relatively easy examples in our benchmark.
3.1.4
Conclusion
We introduce YNAT, the ﬁrst Korean topic classiﬁcation benchmark. The benchmark includes 63,892 news headlines
classiﬁed to a single hand-labeled topic among 7 categories. We assume each headline has only a single topic, but it
could be formulated as multi-label classiﬁcation. We thus open the second and third relevant topic annotations. Also,
URLs for each headlines are accompanied for future work if metadata is needed. If some of them requires permission to
use, one should contact to the agency. We expect YNAT to serve as a simple and basic NLU task compared to others in
KLUE.
15

--- Page 16 ---

3.2
Semantic Textual Similarity (STS)
Semantic textual similarity (STS) is to measure the degree of semantic equivalence between two sentences. We include
STS in our benchmark because it is essential to other NLP tasks such as machine translation, summarization, and
question answering. Like STS [13] in GLUE [133], many NLU benchmarks include comparing semantic similarity of
text snippets such as semantic similarity [142], paraphrase detection [133, 57], or word sense disambiguation [125, 72].
We formulate STS as a sentence pair regression task which predicts the semantic similarity of two input sentences as a
real value from 0 (no meaning overlap) to 5 (meaning equivalence). A model performance is measured by Pearson’s
correlation coefﬁcient following the evaluation scheme of STS-b [13]. We additionally binarize the real numbers into
two classes with a threshold score 3.0 (paraphrased or not), and use F1 score to evaluate the model.
3.2.1
Dataset Construction
Source Corpora
To diversify domain and style of source corpora, we collect sentences from AIRBNB (colloquial
review), POLICY (formal news), and PARAKQC [18] (smart home utterances). We carefully match them to sentence
pairs.
For each corpus, we design a sampling strategy of sentence pairs to uniformly cover all range of the similarity scores.
Without a sophisticated strategy, simple random sampling and matching sentence to pairs would result in a majority
of the score zero. To alleviate this skewness, potentially similar and less similar sentences are separately paired by
using various methods. For instance, if two descriptions are depicting the same image or headlines referring to the same
event, they are likely to be similar because of the additional information. Otherwise, they would not be similar [2].
Inspired from these, we use available additional information to pair sentences as similar or not. If not available, we use
round-trip translation (RTT) to obtain the similar pairs and greedy sentence matching for the less similar pairs.
We specify the strategy for PARAKQC where the intent of each sentence is available. All sentences are queries for a
smart home domain and their intent are shared among some queries. For example, “How’s the weather today in Seoul?”
and “You know what the weather is like in Seoul today?” share the same intent which is asking “The weather of Seoul
today”. We pair two sentences with the same intent as similar pairs and different intent as the less similar. Note that
even the less similar pairs share topic to avoid making too many mutually dissimilar pairs.
For AIRBNB and POLICY, we cannot ﬁnd meaningful metadata to estimate similarity between sentences. So we adopt
RTT technique using NAVER Papago20 to generate the similar sentence pairs, since RTT is known to yield sentences
with slightly different lexical representation while preserving the core meaning of the original sentence. We set English
as an intermediate language. We choose a honoriﬁc option when translating back to Korean because the option tends to
preserve the meaning of the sentences empirically. For less similar pairs, we ﬁrst compute ROUGE [80] of all possible
sentence pairs, by assuming the higher score correlates with higher semantic similarity.21 Then we draw a pair with the
largest score from all possible pairs and the draw is repeated over remaining pairs until all of sentences are matched. As
it progresses, the score declines as the number of remaining pairs becomes smaller, producing less similar pairs. We
summarize this process as greedy sentence matching (GSM), as presented in Algorithm 1.
Algorithm 1: Pseudocode of our greedy sentence matching (GSM) in AIRBNB and POLICY.
Result: Set of sentence pairs SET in a corpus C
Prepare corpus C, Let SET = [];
while size of C ≥2 do
1. Choose a random sentence S from C;
2. Find a sentence T where ROUGE(S, T) is maximized and T ∈C\{S};
3. Remove {S, T} from C;
4. Add matched pair {(S, T)} to SET
end
Annotation Protocol
We modify the original annotation guide used in SemEval-2015 [2]. It suggests chunking both
sentences and compares similarity in chunk-level (e.g., NP, verb chain, PP, etc.). Then an annotator should sum up their
judgement to sentence-level similarity. However, we could not directly apply the guide because chunking is highly
challenging in Korean. In chunking, tokenization and morpheme-level decomposition of words are required, but they are
difﬁcult and even not deterministic in some cases [103]. We thus guide an annotator to evaluate the similarity without
chunking and stick to sentence-level comparison.
20https://papago.naver.com/
21This might be replaced to any other similarity measures.
16

--- Page 17 ---

We give crowdworkers additional cues what is important or unimportant for sentence-level similarity evaluation.
Important content indicates the main idea in a sentence. If it is a declarative sentence, its providing facts, explanation,
or information is the main idea. For an interrogative and imperative sentence, conveying a request or command is
important. In exclamatory sentence, feelings or opinion is the main content [4]. Other components than these important
contents are regarded as unimportant. For example, they are auxiliary verbs or function words which affect its nuance
or politeness. An annotator should score the similarity as follows:
• 5: Two sentences are equivalent in terms of important and unimportant content.
• 4: Two sentences are closely equivalent. Some unimportant content differ.
• 3: Two sentences are roughly equivalent. Important content are similar to each other, but difference between
unimportant content is not ignorable.
• 2: Two sentences are not equivalent. Important content are not similar to each other, only sharing some unimportant
contents.
• 1: Two sentences are not equivalent. Important and unimportant content are not similar to each other. Two sentences
only share their topics.
• 0: Two sentences are not equivalent. They are not sharing any important and unimportant contents and even topics.
We also guide crowdworkers to consider the context of sentences. If it signiﬁcantly affects distinguishing the meaning
of two sentences, the score should be low. For example, let two sentences contain important information ‘check-in’ such
as “Check-in was done by someone other than the host.” and “Check-in was done by someone.” In the latter sentence,
‘someone’ might be the host. Since we lose information by dropping ‘other than the host’ from the former, difference
of meaning between the two sentence is not ignorable. We score this pair to 3. Furthermore, if the former sentence is
compared to ‘Check-out was done by someone other than the host.’, important information differ so we give score 2.
Annotation Process
We recruit workers from SelectStar,22 a crowdsourcing platform in Korea and familiarize them to
our annotation protocol. We run pilot annotation to select qualiﬁed workers. If a crowdworker’s judgement is frequently
disagreed against that of other workers, the person is excluded from the main annotation process. As a result, 19 out of
the initial 20 workers participate in the main annotation. After removing the sentence pairs used in the pilot, we use
14,869 pairs for the main annotation, consisting of 7,375 for AIRBNB, 2,956 for POLICY, and 4,538 for PARAKQC. 7
different workers labeled all sentence pairs independently.
We average 7 labels for each sentence pair and remove outliers following Agirre et al. [3], Cer et al. [13]. First, we
ﬁlter out annotators showing Pearson’s correlation < 0.80 or Krippendorff’s alpha < 0.20 (nominal) [67] with others’
annotations. We exclude two annotators with this criteria so all sentence pairs have annotations from at least ﬁve people.
Lastly, similarity score is rounded up to the ﬁrst decimal place.
A few more ﬁltering schemes are applied. First, we drop 14 pairs whose annotations are showing larger than 2 standard
deviation. Those pairs might contain ambiguous expressions interpreted in various ways, or misannotations. Second,
we ask workers to report the sentences including translation error or misinformation caused by RTT. We inspect the
reported sentences and remove 418 sentence pairs. Third, we drop sentences involving ethical issues. Workers report the
pairs if they are including any kind of hate speech, social bias, and potential personally identiﬁable information (PII).
1,213 sentence pairs were additionally removed after inspection. As a result, we have 13,224 sentence pairs in total.
We report inter-annotator agreement (IAA) by using Krippendorff’s alpha instead of Pearson’s correlation because 7
annotators (or less) differ by pairs. The annotator agreed to each other’s annotations. (Krippendorff’s alpha (interval) =
0.85).
We observe the distribution of similarity score annotations differ between the potentially similar sentence pairs and the
less similar pairs. Figure 1 illustrates label distributions generated by RTT (top) and GSM (bottom) in AIRBNB. As
expected, RTT pairs tend to show high similarity (from 3 to 5) while GSM pairs are considered less similar (from 0 to
3). Note that the number of GSM pairs scored 0 is high even we employ similarity-based matching. Similar tendencies
are observed in POLICY and PARAKQC. By combining two distributions, we manage to obtain various sentence pairs
in terms of similarity scores.
Final Dataset
We collect 13,224 sentence pairs and corresponding similarity scores. We split them to training,
development, and test sets, considering the distribution of the scores. Even if we carefully sampled the pairs, the overall
score distribution is not uniform across 0−5 as shown in Figure 1. However, we prefer uniform distribution at least in
evaluation (development and test) set, in order to prevent evaluation bias toward a speciﬁc score. We therefore construct
22https://selectstar.ai/
17

--- Page 18 ---

Figure 1: Label distributions generated by RTT (top) and GSM (bottom) in AIRBNB.
the evaluation set having approximately uniform distribution as shown in Figure 2. To this end, we divide the score
range 0−5 to 51 bins, rounding up to the ﬁrst decimal place of every scores. We try to balance the number of pairs
across bins. Since some of them have small number of pairs, we try to ﬁt all number of the pairs close to that number.
Figure 2: Similarity score distribution of the train (top) and dev (bottom) set. The scores of dev set is close to uniform
distribution across range 0−5. The scores are rounded to the ﬁrst decimal place.
We also consider word overlap between sentences in each pair for evaluation set. Since larger word overlap might
indicate higher semantic similarity, we try to reduce pairs satisfying such tendency to prevent the model from predicting
similarity simply using word overlap. The overlap is measured by morpheme-level Jaccard distance by using MeCab
[68]. We choose the pairs with the least word overlap from score 3−5, and the pairs with most word overlap from the
rest. Such pairs are prioritized to be included to every bins in the dev and the test sets.
We split the evaluation set with 1:2 ratio to construct the dev and the test sets, resulting in 519 and 1,037 pairs,
respectively. The rest 11,668 pairs comprise the train set. Detailed numbers for each corpus are presented in Table 4.
For all the sets, we balance the ratio between source corpora with that of the original pairs. Additionally, the scores are
binarized with a threshold 3.0 same as paraphrase detection task.
3.2.2
Evaluation Metrics
The evaluation metrics for KLUE-STS is 1) Pearson’s correlation coefﬁcient (Pearson’ r), and 2) F1 score. Pearson’s
r is a measure of linear correlation between human-labeled sentence-similarity scores and model predicted scores,
adopted in STS-b [13]. Since our dev and test set have a balanced score distribution, the coefﬁcient correctly gives
the magnitude of the relationship. F1 score is adopted to measure binarized results (paraphrased / not paraphrased).
Speciﬁcally, our F1 reports results for the paraphrased class.
18

--- Page 19 ---

Table 4: Statistics for KLUE-STS. The ﬁrst three columns provide the number of examples in train, dev, and test sets of
each source corpus and the ﬁnal data.
Source
|Train|
|Dev|
|Test|
Total
AIRBNB
5,371
255
510
6,136
POLICY
2,344
132
264
2,740
PARAKQC
3,953
132
263
4,348
Overall
11,668
519
1,037
13,224
3.2.3
Related Work
Measuring similarity between sentences is a fundamental natural language understanding problem so that closely related
to various NLP applications. Because of its importance, STS is included in various NLU benchmarks [133, 142]. To
facilitate research in this area, many shared tasks have been held and annotated corpora are released [2, 3, 13]. Typically,
they cover multiple text domains such as question pairs, image descriptions, news headlines, annotated with a real value
from 0 (no meaning overlap) to 5 (meaning equivalence).
Recently, Ham et al. [45] introduces a machine-translated Korean STS benchmark. This is a translation of [13] in
GLUE, which contains around 8,600 sentence pairs in total. All examples are solely relying on machine translation, and
sentence pairs in evaluation (dev and test) set are further post-edited by human. However, corresponding labels were not
adjusted to translated meanings. Lack of re-labeling process would be problematic because Korean speakers would
judge the similarity between them differently.
If similarity labels are binarized by a certain threshold, STS also could be seen as paraphrase detection task such as
Microsoft Research Paraphrase Corpus (MRPC) [32], Quora Question Pairs (QQP) [133], or PAWS [152] and PAWS-X
[144]. Thus we additionally binarize our ground truths and predictions, reporting binary classiﬁcation performance to
see how well a model performs in paraphrase detection.
In paraphrase detection, Cho et al. [18] presents a benchmark that includes the human-generated queries for smart home,
where ten paraphrase sentences are grouped together to make up a total of 1,000 groups. The granularity of scale is from
0 to 5, but the semantic similarity is judged only with attributes such as topic (smart home, weather, etc.) and speech act
(question, prohibition, etc.), which does not consider other details such as nuance and syntactic structure because it
lacks direct human judgement of similarity. PAWS-X [144] provides a translated version of PAWS [152] of Korean.
Like KorSTS, the train split is machine-translated and its dev and test splits are human-translated, and corresponding
labels are preserved without human inspection. There are also paraphrase corpora provided by government-funded
institutions such as National Institute of Korean Language (NIKL) [98], but it simply provides human-generated and
machine-paraphrased sentences with limited accessibility.
3.2.4
Conclusion
We create the ﬁrst human-annotated Korean STS benchmark, KLUE-STS, that covers multiple domains and styles with
free accessibility to everyone. The similarity score annotation process is specially designed to capture the characteristics
of the Korean language. Covering the expressions from various domains, our benchmark is expected to be a useful
resource for further research, beyond serving as a benchmark. Our benchmark helps to develop numerous models
established on STS resources, such as SentenceBERT [115].
19

--- Page 20 ---

3.3
Natural Language Inference (NLI)
The goal of natural language inference (NLI) is to train a model to infer the relationship between the hypothesis
sentence and the premise sentence. Given a premise, an NLI model determines if hypothesis is true (entailment), false
(contradiction), or undetermined (neutral). The task is also known as recognizing textual entailment (RTE) [27].
Understanding entailment and contradiction between sentences is fundamental to NLU. NLI datasets are also included
in various NLU benchmarks such as GLUE [133] and superGLUE [132], and they are valuable as training data for
other NLU tasks [24, 107, 115].
We formulate NLI as a classiﬁcation task where an NLI model reads each pair of premise and hypothesis sentences and
predicts whether the relationship is entailment, contradiction, or neutral. We use the classiﬁcation accuracy to measure
the model performance.
3.3.1
Dataset Construction
We construct KLUE-NLI by using a collection method similar to that of SNLI [8] and MNLI [138]. First, we collect
premise sentences from existing corpora. Then for each premise sentence, we ask one annotator to generate three new
hypothesis sentences, one for each of the three relationship classes. Then for each pair of premise and hypothesis
sentences, we ask four additional annotators to label the relationship for validation. We follow the criteria proposed by
Williams et al. [138] to describe the three labels to the annotators. For both hypothesis generation and pair validation,
we recruit workers from SelectStar,23 a Korean crowdsourcing platform.
Source Corpora for Premise Sentences
We use six corpora for the set of premise sentences: WIKITREE, POLICY,
WIKINEWS, WIKIPEDIA, NSMC and AIRBNB. They cover diverse topics and writing styles of contemporary Korean.
WIKITREE, POLICY and WIKINEWS are news articles and WIKIPEDIA is a crowd-sourced encyclopedia, all of
which are written in formal Korean. NSMC and AIRBNB consist of colloquial reviews in the domains of movies and
travel, respectively.
From the six corpora, we extract 10,000 premises with which we elicit hypotheses. A valid premise should satisfy
three conditions. First, premise is a proposition, a declarative sentence to which we can assign a truth value, excluding
mathematical formulae and lists. Second, a premise must include at least one predicate, and the predicate can be of
diverse types such as states (e.g., be, believe, know), activities (e.g., play, smile, walk), achievements (e.g. realize, reach,
break), and accomplishments (e.g. eat, build, paint). Third, the length of a premise should be from 20 to 90 characters
including whitespace.
Annotation Protocol for Hypothesis Generation
We show annotators a premise and ask them to write three
hypotheses that correspond to each label. This allows us to collect nearly equal number of the (premise, hypothesis)
pairs for each labels. We maintain the outline of the criteria as follows:
• ENTAILMENT: The hypothesis is necessarily true given the premise is true
• CONTRADICTION: The hypothesis is necessarily false given the premise is true
• NEUTRAL: The hypothesis may or may not be true given the premise is true
We are aware of the annotation artifacts coming from human writing-based hypothesis generation. Sentence length and
explicit lexical patterns are highly associated with certain classes. Neutral sentences tend to be the longest among all
classes, since workers can produce neutral hypothesis simply by introducing additional phrase or clause not stated in
the premise. Negations such as “no”, “never” and “nothing” are often accompanied with the class CONTRADICTION
[44, 108].
Despite the concerns of such artifacts, we stick to such a writing-based annotation procedure. Compared to automatic
pipelines to collect hypotheses, human writing yields higher quality data and is still an effective protocol [131]. We
focus on ways to encourage annotators to avoid injecting trivial patterns. We prepare guidelines with speciﬁc Dos and
Don’ts, and rigorously train the workers in advance. To minimize annotation artifacts, we instruct the annotators to
write sentences with similar lengths across the classes, refrain from inserting certain lexical items repeatedly, and use as
diverse strategies as possible when making inferences.
Speciﬁcally, we provide detailed guidelines for hypothesis generation together with examples. We encourage annotators
to create hypotheses that exhibit diverse linguistic phenomena, in terms of 1) lexical choice, 2) syntactic structures
and 3) world knowledge. In the case of lexical choice, our guideline suggests annotators use synonyms/antonyms,
23https://selectstar.ai/
20

--- Page 21 ---

Table 5: Summary of validation statistics for KLUE-NLI compared to SNLI and MNLI [138]. We call the label intended
by the original annotator in writing the hypothesis "author’s label." Consensus among three out of ﬁve annotators is
"gold label."
Statistics
SNLI
MNLI
KLUE-NLI
Unanimous Gold Label
58.30%
58.20%
76.29%
Individual Label = Gold Label
89.00%
88.70%
92.63%
Individual Label = Author’s Label
85.80%
85.20%
90.92%
Gold Label = Author’s Label
91.20%
92.60%
96.76%
Gold Label ̸= Author’s Label
6.80%
5.60%
2.71%
No Gold Label (No 3 Labels Match)
2.00%
1.80%
0.53%
hypernyms/hyponyms, and auxiliary particles. To introduce various syntactic structures, we provide several syntactic
transformation strategies such as word scrambling, voice alteration, and causative alternation. Methods like sub-
ject/object swapping or passivization is motivated by existing NLI data augmentation strategies [89, 42]. We also
encourage using expressions that reﬂect world knowledge such as time, quantity and geography in order to create a
dataset grounded to the real world.
There are a few more details in the guideline. We instruct annotators to maintain the writing style of the premise to
create a balanced dataset in terms of the style as well. We also instruct them to skip sentences that are difﬁcult to
understand either due to the ungrammaticality or the complexity of the content. They are also instructed to skip and
report sentences that contain ethical issues such as hate speech, social bias, or personally identiﬁable information. We
examine all reported sentences and make ﬁnal decisions whether to include the sentences in the dataset.
Annotation Protocol for Label Validation
Crowdworkers annotate the relations of the resulting premise-hypothesis
pairs for validation. For each of the pairs created, we ask four crowdworkers to supply a single label among (EN-
TAILMENT, CONTRADICTION, NEUTRAL). This yields a total of ﬁve labels per pair, including the initial label
intended by the annotator who wrote the hypothesis sentence. For each validated sentence pair, we assign a gold label
representing the majority of three or more votes out of ﬁve.
Annotation Process
For hypothesis generation, we go through a pilot phase where we iteratively update the guide-
lines and train the workers. During the pilot, we ﬁnd writing a semantically unacceptable sentence or introducing a
demonstrative pronoun not used in the premise could be potential problems. Since they might alter the intended label,
we ask workers to avoid writing such sentences. The number of workers for this part of the annotation process is 11.
We then validate the relation labels for every pair. We go through a pilot phase, starting with 2,604 applicants in the
pilot, then select 684 who passed the test to participate in the validation step. With 138 workers dropping out, the ﬁnal
number of workers is 546.
Validation results are summarized in Table 5. They suggest that our writing protocol is effective in producing a high
quality corpus. The rate of unanimous gold labeled examples in KLUE-NLI is 18% higher than SNLI and MNLI.
The higher the rate of such examples, the clearer the relationship between the generated hypothesis sentences and the
original premise sentences. Individual annotator’s agreement with the gold label and the author’s label are also higher
than SNLI and MNLI, and almost all pairs receive the gold label. Only a few sentence pairs (0.53%) lack the gold label,
and we remove those before ﬁnalizing our dataset.
Final Dataset
The ﬁnal dataset consists of 30,998 sentence pairs that are divided into train/development/test sets.
Table 6 shows the basic statistics of the dataset. As observed in SNLI and MNLI, our premise sentences also tend to
be longer than the corresponding hypothesis sentences. This is because workers generally use partial information of a
premise to write a hypothesis.
Note that we deliberately form the development and test sets in a way to 1) contain balanced source styles and 2)
disincentivize models exploiting annotation artifacts. The development and the test set each contains 3,000 sentence
pairs.
To maintain consistency of style in development and test sets, we include in each set 60% formal and 40% colloquial
sentences. We sample 450 sentences each from formal text WIKITREE, POLICY, WIKINEWS, WIKIPEDIA, and 600
sentences each from colloquial text NSMC, AIRBNB.
21

--- Page 22 ---

Table 6: Statistics for KLUE-NLI. The ﬁrst three columns provide the number of sentence pairs in train, dev, and test
sets. Avg Len Prem and Avg Len Hyp are the mean character counts of premise and hypothesis sentences, respectively.
Source
|Train|
|Dev|
|Test|
Total
Avg Len Prem
Avg Len Hyp
WIKITREE
3,838
450
450
4,738
52.81
26.86
POLICY
3,833
450
450
4,733
56.73
32.93
WIKINEWS
3,824
450
450
4,724
64.17
29.11
WIKIPEDIA
3,780
450
450
4,680
57.45
23.70
NSMC
4,899
600
600
6,099
27.48
21.49
AIRBNB
4,824
600
600
6,024
24.28
18.65
Overall
24,998
3,000
3,000
30,998
47.15
25.46
To prevent our NLI benchmark from incentivizing a model that predicts a label using a spurious cue in the hypothesis,
we ﬁrst ﬁne-tune the KLUE-RoBERTa-base model using only the hypothesis sentences with their corresponding labels.
If the model ﬁnds no clue between the hypothesis and the label, the predicted probability scores for each label should
be uniform (i.e., one-third ( 1
3) when classiﬁed 3-way). Assuming that such score distribution is ideal, we prefer the
pairs for development/test sets whose hypothesis-only model’s predictions are closest to the ideal. We compute the
distance between the prediction and the ideal using cross entropy. To preserve the intact sets of a premise and its three
hypotheses, we calculate the mean distance of each set. We extract the sets whose mean distance is among the lowest
20%, and randomly split them into dev and test sets.
Our idea can be viewed as an extension of pointwise mutual information (PMI). PMI between each hypothesis word (w)
and class label (c) has been used to discover the association of the word with each class [44, 131]. If PMI is expanded to
the sentence-level association, the metric provides a similar measure to the hypothesis-only model prediction probability
as below.
PMI(w, c) = log
P(w, c)
P(w)P(c) = log P(c|w)P(w)
P(w)P(c)
= log P(c|w)
P(c)
∝P(c|w)
To measure human performance and examine whether KLUE-NLI test set improves upon KorNLI [45] test set, a
machine-translation of the XNLI [25] test set, we conduct a round of human evaluation. We employ four native Korean
undergraduates who major in Korean linguistics and did not participate in the KLUE-NLI construction process. We
randomly sample 100 sentence pairs from KLUE-NLI test set and ask the workers to annotate them. We check the
agreement of their annotations with the given gold label. We do the same on the subset of the KorNLI test set, to
examine whether the human-elicited dataset improves the quality of the dataset. The results are shown in Table 7.
For KorNLI, 38% of the sentence pairs have responses from all four annotators that match with the gold labels. There
are 18%, 18%, and 16% of sentences, respectively, when three, and two, and one response match with the gold label. 10
pairs do not match with the gold label. On the other hand, KLUE-NLI shows much higher agreement with the given
gold label. All annotators agree with the gold label in 71% of the pairs, and 95% obtain at least three agreements.
Furthermore, only 258 out of 400 (64.50%) individual annotations are the same as the gold label in KorNLI. Again,
KLUE-NLI shows better agreement with the gold labels. 360 (91.00%) annotations are the same as the gold label.
These numbers in annotation quality of KLUE-NLI are better than KorNLI as well as SNLI and MLNI. In KorNLI,
annotators often report that they do not quite understand at least one of the two sentences or choose NEUTRAL because
it is difﬁcult to distinguish the semantic relationships of the sentences. Although the distribution of the gold label
is uniform (respectively 33, 33, and 34% of entailment, contradiction, and neutral sentences), the label chosen most
frequently by the annotators is NEUTRAL (56.75% on average). There are 26% of cases where the gold labels are
different from the majority vote by the annotator. These results suggest that the annotators struggle to grasp the logical
semantic relationship of KorNLI sentences.
On the other hand, for KLUE-NLI, there is no case where none of the four responses matches the gold label. Considering
the cases where more than two of the responses match the gold label, there is a 98% chance of the gold label to be
re-selected as the majority tag. Compared to KorNLI, we can see that KLUE-NLI is a much more reliable dataset. This
result also conﬁrms that the headroom of our current best model (accuracy: 89.77%) is still there, given that the human
accuracy, represented by the majority tag, is 98%.
22

--- Page 23 ---

Table 7: Statistics for human evaluation results of KorNLI and KLUE-NLI. We compare the labels of four annotators
with gold labels of korNLI and KLUE-NLI test data.
Statistics
KorNLI
KLUE-NLI
Unanimous Gold Label (4 Agree)
38.00%
71.00%
3 Agree with Gold Label
18.00%
24.00%
2 Agree with Gold Label
18.00%
3.00%
1 Agrees with Gold Label
16.00%
2.00%
0 Agrees with Gold Label
10.00%
0.00%
Individual Label = Gold Label
64.50%
91.00%
No Gold Label (No 3 Labels Match)
4.00%
0.00%
Majority Vote ̸= Gold Label
26.00%
0.00%
3.3.2
Evaluation Metric
The evaluation metric for KLUE-NLI is accuracy, following SNLI [8] and MNLI [138]. Accuracy measures how well
a classiﬁer correctly identiﬁes the results. The class labels are almost equally distributed, thus higher accuracy will
correctly represent performances of a model.
3.3.3
Related Work
Recognizing Textual Entailment (RTE) [27] is a task similar to NLI and was introduced in a series of textual entailment
challenges. In the RTE task, two sentences are given, and the model decides whether the meaning of one sentence can
be entailed from the other sentence. In earlier RTE 1–3, the task is binary, ‘ENTAILMENT’ and ‘NO ENTAILMENT’.
In RTE 4-5, a new class ‘UNKNOWN’ is introduced, and the task is formulated as a three-way classiﬁcation.
Two major datasets for NLI in English are Stanford Natural Language Inference (SNLI) [8] and Multi-Genre Natural
Language Inference (MNLI) [138]. Hypothesis sentences in SNLI and MNLI are labeled ENTAILMENT, CONTRA-
DICTION, or NEUTRAL. SNLI is two orders of magnitude larger than the RTE corpora, made from 570,152 image
captions in Flickr30k [148]. MNLI premise sentences are derived from 10 different sources, covering a wider range of
styles, degrees of formality, and topics.
Most of the existing NLI datasets are in English, including SNLI and MNLI, and one common approach for constructing
NLI datasets in other languages is to translate the existing English corpora to the language of interest. Conneau et al.
[25] provides XNLI (Cross-lingual natural language inference) by employing professional translators to translate the
development and test sets of MNLI into 15 languages. One main concern of the translation-based approach is whether
the relation of the original sentence pair is maintained in the process. Conneau et al. [25] ﬁnd some translated pairs lose
the initial semantic relationship, validated by human annotators who re-annotate a sample of the dataset. The result
demonstrates that human translations cause 2% misannotations given the 85% correct examples in the MNLI and 83%
in XNLI.
Motivated by the fact that Korean is not included in XNLI, KorNLI [45] is introduced. KorNLI [45] is a translation of
existing English corpora whose train set is created through machine translation of training sets of SNLI and MNLI, and
the development and test sets through machine translation of development and tests sets of XNLI and post-editing by
professional translators. Although Ham et al. [45] also investigate the data manually and acknowledge some incorrect
examples after the translation, no human validation process is performed to quantify the observation and leave analyzing
such errors to future work. Moreover, even with post-editing, there are some sentences that are either unnatural in terms
of syntactic structure or word choice.
Many studies have been proposed based on SNLI and MNLI; however, SNLI and MNLI are known to have annotation
artifacts [44, 108]. Annotation artifacts are the product of certain types of annotation strategies and heuristics naturally
arising from the crowdsourcing process. Such artifacts are problematic as they may lead models to adopt heuristics
rather than to actually learn the relationship.
There have been some efforts to reduce annotation artifacts in NLI. Vania et al. [131] experiment with two fully
automated protocols for creating premise-hypothesis pairs, but ﬁnd that the methods yield poor-quality data and mixed
results on annotation artifacts. OCNLI [53] enhance writing-base protocol with some interventions to control the bias:
encouraging writers to use diverse ways of making inference, and putting constraints on overused words. Despite partial
effects on reducing negators, the explicit constraint gives rise to other words of correlation, and the ﬁnal OCNLI dataset
exhibit similar level of hypothesis-only test scores to most benchmark NLI datasets.
23

--- Page 24 ---

3.3.4
Conclusion
Our new dataset, KLUE-NLI, is the ﬁrst resource constructed upon naturally occurring Korean sentences. KLUE-NLI
represents diverse linguistic phenomena, writing style, degree of formality and contents that are most natural and
suitable for Korean. The premise sentences of our dataset come from six Korean corpora, and the hypothesis sentences
are written by well-trained workers.
By keeping the writing-based protocol and thoroughly training workers based on detailed guidelines, we improve upon
the existing NLI datasets in the reliability of the labels. KLUE-NLI shows much higher inter-annotator agreement rate
than both the MNLI and the translation-based Korean dataset, KorNLI. The gap between the human performance scores
of KLUE-NLI and KorNLI also provides evidence that KLUE-NLI is currently the optimal Korean NLI dataset.
Beyond its main purpose as an NLI benchmark dataset, we hope KLUE-NLI will be a useful resource for future NLU
research, as English dataset such as MNLI and SNLI are extended [24, 107, 115].
24

--- Page 25 ---

3.4
Named Entity Recognition (NER)
The goal of named entity recognition (NER) is to detect the boundaries of named entities in unstructured text and
classify the types. An entity can be series of words that refers to the person, location, organization, time expressions,
quantities, monetary values.
Since NER is an important for application ﬁelds like syntax analysis, goal-oriented dialog system, question and
answering chatbot and information extraction, various NLU benchmarks contains NER datasets [137, 57, 78, 54].
Despite the rise of necessity of NER datasets in various domains and styles, there are few existing Korean NER datasets
to cover such need. Therefore, we annotate corpora including web texts that can be applied to real-word applications.
In KLUE-NER, a model should detect the spans and classify the types of entities included in an input sentence. The
six entity types used in KLUE-NER are person, location, organization, date, time, and quantity. They are tagged
via character-level BIO (Begin-Inside-Outside) tagging scheme, and thus we evaluate a model’s performance using
entity-level and character-level F1 score.
3.4.1
Dataset Construction
Source Corpora
To incorporate both formal and informal writing styles, we use two corpora, WIKITREE and NSMC
for annotation. WIKITREE is a news article corpus and thus contains formal sentences with many entity types, which
suits well as a source corpus for NER. NSMC includes colloquial reviews of movies or TV shows. Since the texts in
NSMC are user-generated comments, they contain errata and non-normalized expressions, along with emojis and slang.
Such a noisy dataset will help broaden the application ﬁeld of NER models.
The preprocessing of the two corpora is performed differently considering the characteristics of each corpus. For
WIKITREE, since the news articles are mainly composed of well-written sentences, we simply split the articles into
sentences. In contrast, the web texts from NSMC are written in the style of spoken language with blurry sentence
boundaries. As each review is generally quite short and the sentences consisting it are on the same topic, we use each
review as a single unit of input. In addition, the sentences that contain hate speech or socially biased terms are removed
manually. For both corpora, we remove sentences longer than 400 characters.
For efﬁcient annotation, we perform pseudo-labeling with a pretrained model. The model is trained with BERT-CRF
using a publicly available dataset KMOU-NER corpus,24 to support fast and accurate entity tagging for annotators. We
also ﬁlter out the sentences with no pseudo-labeled entity assuming they do not include any of the entities. Remaining
sentences account for about 80% in WIKITREE and 41% in NSMC, leaving a total of 36,515 sentences.
Annotation Protocol
We use six entity types for KLUE-NER annotation: PS (Person), LC (Location), OG (Organi-
zation), DT (Date), TI (Time), and QT (Quantity). The description of each entity type is as follows.
• PS (Person): Name of an individual or a group
• LC (Location): Name of a district/province or a geographical location
• OG (Organization): Name of an organization or an enterprise
• DT (Date): Expressions related to date/period/era/age
• TI (Time): Expressions related to time
• QT (Quantity): Expressions related to quantity or number including units
We employ the above sets following the convention of two existing tag sets: Korean Telecommunications Technology
Association (TTA) NER guidelines25 and MUC-7 [16]. TTA guideline is a standardized NER tagging scheme for
Korean language and we follow the names and the deﬁnitions of its entity types. Among the 15 entity types of TTA, we
select our six types that correspond with tagsets used in MUC-7 (DATE, LOCATION, MONEY, ORGANIZATION,
PERCENT, PERSON and TIME). As MONEY and PERCENT types are included in QT (QUANTITY) type from TTA
set, we instead adopt an entity type QT.
In the case of entities with multiple possible entity types, instead of assigning a unique tag for all use cases, we
determine their tags based on the context. One example is Cine21, which, in Korean, can either refer to the name of a
magazine or the publisher of the magazine. In a sentence like “’I bought a Cine21 from a bookstore and read it page by
page,” ‘Buy something from a bookstore’ and ‘read page by page’ are properties regarding media (magazine), rather
than an organization; thus we do not assign an OG tag.
24https://github.com/kmounlp/NER
25https://committee.tta.or.kr/data/standard_view.jsp?nowPage=2&pk_num=TTAK.KO-10.0852&commit_
code=PG606
25

--- Page 26 ---

Table 8: Statistics for KLUE-NER.
Source
|Train|
|Dev|
|Test|
Total
WIKITREE
11,435
2,534
2,685
16,664
NSMC
9,573
2,466
2,315
14,354
Total
21,008
5,000
5,000
31,008
Table 9: Entity-wise statistics for KLUE-NER. Note that the numbers in parentheses denote the number of types. The
total number does not match Table 8 since this table does not remove duplication.
Source
|Train|
|Dev|
|Test|
Total
PS
14,453 (5,428)
4,418 (2,706)
4,830 (3,063)
23,289 (7,124)
LC
6,663 (2,068)
1,649 (896)
2,064 (1,130)
9,961 (2,650)
OG
8,491 (3,008)
2,182 (1,291)
2,514 (1,579)
12,855 (3,796)
DT
8,029 (1,608)
2,312 (835)
2,498 (933)
12,653 (2,060)
TI
2,020 (573)
5,45 (268)
579 (316)
3,110 (730)
QT
11,717 (3,628)
3,151 (1,763)
3,827 (2,369)
18,019 (4,776)
Total
51,373 (16,313)
14,257 (7,759)
16,312 (9,390)
79,887 (21,136)
We guide crowdworkers to report if the text for annotation does not meet certain conditions. For example, texts
consisting of multiple sentences, texts that are not in a sentence form, a fragment, and a simple sequence of nouns are
discarded. Workers are also required to report sentences that include hate speech and various biases in tagging process.
In terms of personally identiﬁable information, we cannot simply drop or pseudonymize the information because
the very task of NER often requires the speciﬁc information of proper nouns such as person names (PS). In order
to minimize the loss of sentences, we inspect through the sentences after the annotation process. We investigate the
sentences that include PS tags, and keep the ones that contain the name of public ﬁgures that appear in Korean search
engines.26 Other sentences are removed if it has potential privacy issues.
Annotation Process
51 qualiﬁed crowdworkers recruited by a Korean crowdsourcing platform, DeepNatural27
participate in the annotation process. The qualiﬁcation is given when passing a pilot entity tagging test. Then two
linguists check whether the crowdworkers’ annotations are correct or not. We ﬁnd some erroneous annotations remaining
even after validation. Therefore, six NLP researchers manually correct the annotation errors.
During the annotation process, 5,354 sentences are dropped by workers due to their inadequacy. 118 sentences are
dropped due to the privacy issue, and 35 sentences are removed after the inspection by the researchers because all
annotations are false positives. A total of 5,507 sentences are dropped in the inspection process, resulting in 31,008
sentences.
Final Dataset
The resulting corpus is split into train/dev/test sets, each consisting of 21,008, 5,000, and 5,000
sentences (Table 8). The entity-wise statistics is provided in Table 9. We design the test set to include unseen entities to
check the robustness of the models in terms of domain transitions and generalization.
The ﬁnalized entity types are tagged in the character level BIO tagging scheme (Figure 3). In most English and Korean
NER datasets, the entities are tagged with the word-level BIO scheme, following CoNLL 2003 dataset [129]. In
Korean, however, it is difﬁcult to adhere to the word level tagging scheme based on whitespace for two reasons. First,
whitespace-split units (eojeols) are often not a single word and are a composite of content words and functional words
(e.g., ‘담주가(the next week is)’ = ‘담주(the next week)’ + ‘가(is)’) [46]. Second, many compound words in Korean
contain whitespaces. Therefore, we choose to tag in character level.
3.4.2
Evaluation Metrics
The evaluation metrics for KLUE-NER are 1) entity-level macro F1 (Entity F1) and 2) character-level macro F1 (Char
F1) scores. Entity F1 score measures how many predicted entities and types are exactly matched with the ground truths
26Daum: http://search.daum.net/search?nil_suggest=btn&nil_ch=&rtupcoll=&w=tot&m=&f=&lpp=&q=%C0%CE%
B9%B0%B0%CB%BB%F6 / Naver: https://people.search.naver.com/
27https://deepnatural.ai/
26

--- Page 27 ---

Figure 3: An example of BIO scheme for NER tagging. The sentence is translated as: “<CNBlue:PS> is the best♥!!!!
So sad <the next week:DT> is their last weekT.T Nooooo!!” where 씨엔블루(CNBlue) is a rock band of Korea. 담주
(the next week) is tagged as DT here, while it is agglutinated with a functional word 가(is) in this sentence and is
separately annotated with the character-level BIO scheme.
in entity-level. Suppose a ground truth is [B-PS, I-PS, O, O, B-OG, I-OG] and a prediction is [B-PS, I-PS, I-PS, O,
B-OG, I-OG]. For entity type PS, F1 score is 0 since a model fails to predict the exact span, while in case of OG, a
model gets a score. To get a high score, a model should be careful at tokenization. Char F1 score is newly provided to
measure a partial overlap between a model prediction and a ground truth. We additionally report this measure to see
how well a model decomposes stems and afﬁxes in Korean, which signiﬁcantly affects the model performance of NER.
Char F1 is an average of class-wise F1-scores. In KLUE-NER, the classes are B-PS, I-PS, B-LC, I-LC, B-OG, I-OG,
B-DT, I-DT, B-TI, I-TI, B-QT, and I-QT. We exclude the majority negative entity class (O), to focus on positive entities.
3.4.3
Related Work
CoNLL2003 [129] is the most widely used NER benchmark which covers texts from Reuters newswire articles. It
handles English and German and is annotated with four named entity types (persons, locations, organizations, and
miscellaneous entities). Another dataset on news articles from the Wall Street Journal, MUC (Message Understanding
Conference) [43], presents an extended tag set, including temporal and numerical entities. The resulting materials, e.g.,
MUC-6 [43] and MUC-7 [16], which include six and seven classes of entities, respectively, are adopted as a training
source for developing the Stanford NER parser [40].
To handle more informal and less sentence-like documents, WNUT16 [127] is proposed. It deals with English Twitter
texts which are ﬁrst suggested in TwitterNER [117]. A total of 15 types of entities are labeled, more subdivided than
CoNLL03 and MUC.
For Korean, there are four existing NER datasets which are published by Korea Maritime & Ocean University (KMOU),
Changwon University, National Institute of Korean Language (NIKL) and Electronics and Telecommunications Research
Institute (ETRI). All of them follow the tagging schema of Telecommunications Technology Association (TTA).28 TTA
provides a standardized named entity tagging scheme that serves as an integrated guideline for NER research in Korean.
It incorporates 15 named entity tags with 146 subcategories, and provides the deﬁnition and the examples regarding
each tag with the instructions on the tagging procedure.
No existing Korean NER dataset is both freely accessible and covers diverse text domains. According to Cho et al. [19],
the NER dataset provided by Korea Maritime & Ocean University (KMOU) and the dataset constructed by Changwon
University are publicly accessible. The datasets provided by ETRI and NIKL are not fully public, and the usage is also
restricted to domestic researchers. We overcome this issue by making KLUE NER freely available to anyone. None of
the aforementioned datasets cover sentences from noisy user generated web texts, which helps model trained on those
to be more robust and generalizable. Moreover, except for the KMOU dataset, all the above datasets are tagged in word
level, which often conﬂicts with the morphological characteristics of Korean. In comparison, KLUE-NER uses web
texts as source corpora and the entities are annotated in character level, thus being more practical and useful.
3.4.4
Conclusion
We construct a new Korean NER benchmark that covers broad domains and styles, which is freely accessible to anyone.
The entity types are annotated so that a model has to use both morphological and contextual cues. The character-level
entity tagging and evaluation method reﬂects the characteristics of Korean morphology. Since KLUE-NER dataset
covers both formal news articles and informal user-generated web texts, we hope that our benchmark helps develop
NER models that can be used in a wide a range of domains, and serve as a resource for developing advanced models for
Information Extraction.
28KMOU utilizes a modiﬁed guideline KMOU-NLP-2018-001 based on the TTA scheme, which is available in https://github.
com/kmounlp/NER/blob/master/NER%20Guideline%20(ver%201.0).pdf
27

--- Page 28 ---

3.5
Relation Extraction (RE)
Relation extraction (RE) identiﬁes semantic relations between entity pairs in a text. The relation is deﬁned between an
entity pair consisting of subject entity (esubj) and object entity (eobj). For example, in a sentence ‘Kierkegaard was born
to an afﬂuent family in Copenhagen’, the subject entity is ‘Kierkegaard’ and the object entity is ‘Copenhagen’. The
goal is then to pick an appropriate relationship between these two entities; ‘place_of_birth’.
RE is a task suitable for evaluating whether a model correctly understands the relationships between entities. In order to
ensure KLUE-RE captures this aspect of language understanding, we include a large-scale RE benchmark. Because
there is no large-scale RE benchmark publicly available in Korean, we collect and annotate our own dataset.
We formulate RE as a single sentence classiﬁcation task. A model picks one of predeﬁned relation classes describing
the relation between two entities within a given sentence. In other words, the RE model predicts an appropriate relation
r of entity pair (esubj, eobj) in a sentence s, where esubj is the subject entity and eobj is the object entity. We refer to
(esubj, r, eobj) as a relation triplet. The entities are marked as corresponding spans in each sentence s. There are 30
relation classes that consist of 18 person-related relations, 11 organization-related relations, and no_relation. Detailed
explanation of these classes are presented in Table 10. We evaluate a model using micro F1 score, computed after
excluding no_relation, and area under the precision-recall curve including all 30 classes.
3.5.1
Data Construction
Distant supervision [91] is a popular way to build a large-scale RE benchmark. It leverages relation triplets (esubj, r, eobj)
in existing large-scale knowledge base (KB) such as Freebase. If a sentence s in a large corpora includes (esubj, eobj)
detected by an NER model simultaneously, it is added to the dataset with relation label r by assuming any sentence
which contains the pair will express that relation. This approach does not require expensive human annotation, thus
allowing us to build a large-scale RE benchmark in a cost-effective way.
Despite this advantage, distant supervision often ends up with incorrect relation labels when the assumption is not
satisﬁed. In particular, it only considers pairs of entities which are related to each other, which results in an RE model
trained on such corpus to over-predict the existence of some relationship between any given pair of entities. In other
words, the predicted relation class distribution from such predictors is not realistic [116]. Zhang et al. [153] and Nam
et al. [93] thus propose to employ crowdworkers to alleviate erroneous relations extracted by distant supervision. Riedel
et al. [116] furthermore intentionally collect irrelevant entity pairs to prevent RE models from overly predicting false
positives relations.
Overview
We modify the original strategy of distant supervision above, to address this weakness and to better ﬁt our
situation. First, we collect triplets (esubj, r, eobj) from a small Korean KB29 and build additional ones by parsing the
infoboxes in WIKIPEDIA and NAMUWIKI30 to enlarge the pool of the candidate triplets. We then ask crowdworkers
to select the correct relation class of each candidate triplet within a sentence, compared to distant supervision which
directly uses automatically generated relation labels. In addition, we randomly sample entity pairs in s to obtain more
realistic relation class distribution in our benchmark. Those examples would include unseen entities in existing KB as
well as have higher chance to be irrelevant (no_relation).
This procedure can be divided into ﬁve steps; (1) candidate sentence collection, (2) relation schema deﬁnition, (3) entity
detection, (4) entity pair selection and (5) relation annotation. We elaborate each step in the rest of this section.
1. Collect Candidate Sentences
We sample candidate sentences from WIKIPEDIA, WIKITREE and POLICY
corpora to cover a diverse set of named entities and relational facts. Since our task deals with single sentences, we
exploit individual sentences split by Korean Sentence Splitter 31 at the preprocessing step. We ﬁlter out sentences that
contain undesirable social bias and are considered hate speech, using a classiﬁer trained on the Korean hate speech
dataset [92].
2. Deﬁne Relation Schema
We design a relation schema based on the schema from Text Analysis Conference
Knowledge Base Population (TAC-KBP) [87]. Our schema deﬁnes entity types and relation classes. Similar to TAC-
KBP, we constrain esubj to be of either PER (Person) or ORG (Organization) type. eobj can have one of the following
types: PER, ORG, LOC (Location), DAT (Date and time), POH (Other proper nouns), and NOH (Other numerals). For
the relation classes, we adapt the original classes in TAC-KBP to our corpus, following Yu et al. [149].
29https://aihub.or.kr/aidata/84
30https://namu.wiki
31https://github.com/hyunwoongko/kss
28

--- Page 29 ---

Table 10: 30 relation classes deﬁned in the relation schema of KLUE-RE. Relation class r should be one of the
followings which consist of 18 person-related relations, 11 organization-related relations, and no_relation.
Relation Class
Description
no_relation
No relation in between (esubj, eobj)
org:dissolved
The date when the speciﬁed organization was dissolved
org:founded
The date when the speciﬁed organization was founded
org:place_of_headquarters
The place which the headquarters of the speciﬁed organization are located in
org:alternate_names
Alternative names called instead of the ofﬁcial name to refer to the speciﬁed organization
org:member_of
Organizations to which the speciﬁed organization belongs
org:members
Organizations which belong to the speciﬁed organization
org:political/religious_afﬁliation
Political/religious groups which the speciﬁed organization is afﬁliated in
org:product
Products or merchandise produced by the speciﬁed organization
org:founded_by
The person or organization that founded the speciﬁed organization
org:top_members/employees
The representative(s) or members of the speciﬁed organization
org:number_of_employees/members
The total number of members that are afﬁliated in the speciﬁed organization
per:date_of_birth
The date when the speciﬁed person was born
per:date_of_death
The date when the speciﬁed person died
per:place_of_birth
The place where the speciﬁed person was born
per:place_of_death
The place where the speciﬁed person died
per:place_of_residence
The place where the speciﬁed person lives
per:origin
The origins or the nationality of the speciﬁed person
per:employee_of
The organization where the speciﬁed person works
per:schools_attended
A school where the speciﬁed person attended
per:alternate_names
Alternative names called instead of the ofﬁcial name to refer to the speciﬁed person
per:parents
The parents of the speciﬁed person
per:children
The children of the speciﬁed person
per:siblings
The brothers and sisters of the speciﬁed person
per:spouse
The spouse(s) of the speciﬁed person
per:other_family
Family members of the speciﬁed person other than parents, children, siblings, and
spouse(s)
per:colleagues
People who work together with the speciﬁed person
per:product
Products or artworks produced by the speciﬁed person
per:religion
The religion in which the speciﬁed person believes
per:title
Ofﬁcial or unofﬁcial names that represent the occupational position of the speciﬁed
person
We remove rarely appearing relation classes in our corpus such as org:website, per:shareholders, per:cause_of_death,
per:charges, and per:age. For the same reason, we incorporate org:parents into org:member_of and org:subsidiaries
into org:members. Since the taxonomy of TAC-KBP does not precisely reﬂect the regional hierarchy of Korea, we
integrate the preﬁxes country_of, city_of, and stateorprovince_of into place_of. We introduce additional classes
frequently appearing in our corpus such as org:product, per:product and per:colleague:
• org:product: A product or merchandise produced by an organization. This includes intangible goods such as an event
hosted and a business launched by the organization.
• per:product: A product produced by a person. Artworks (e.g. book, music, movie) or contribution to producing them.
• per:colleague: A person could be a colleague of someone if they work together. Two people in the same group such
as political party or alliance are colleagues as well.
3. Detect Entities
We automatically detect named entities in all candidate sentences. We ﬁne-tune a pre-trained
ELECTRA for Korean32 to build two named entity recognition (NER) models on two existing Korean NER resources
respectively. One is provided by National Institute of Korean Language [98], and the other is built by Korea Maritime &
Ocean University.33 We modify the named entity types deﬁned in these resources to be compatible with our own entity
types previously deﬁned in the schema. We take the union of both models’ predictions to extract as many entities as
possible. We use crowdsourcing to correct incorrect boundaries of the detected entities, as described later.
32https://github.com/monologg/KoELECTRA
33https://github.com/kmounlp/NER
29

--- Page 30 ---

Figure 4: Annotation tool for crowdsourcing. Main features are translated in English with red color.
4. Select Entity Pairs
We select two entities from the entity set E of a given sentence s to make an entity pair
(esubj, eobj). In doing so, we take two distinct approaches; (1) KB-based sampling and (2) uniform sampling.
For the ﬁrst approach, we only consider the subset of entities such that each entity pair (esubj, eobj) appears in the pool
of triplets (esubj, r, eobj). We collect these triplets from two sources. First, we create the initial pool of triplets, using a
Korean KB.34 Because the number of triplets (∼800k) from the Korean KB is small compared to, for instance, that of
Freebase (∼2b), we enlarge this pool of triplets by gathering and then parsing infoboxes in WIKIPEDIA and Namuwiki.
In order to avoid over-inclusion of frequent entities, such as the President of Korea, we set an upper bound to the number
of co-occurrence between (esubj, eobj) during sampling [153].
In the second approach, (esubj, eobj) is uniformly sampled from the entire entity set E of a given sentence s, at random.
Because there is no cue whether a sampled pair has any relation between them, the pair is highly likely to be irrelevant
(no_relation). Irrelevant pairs will account for a large portion of realistic relation distribution between two arbitrary
entities. Therefore, this approach helps to set up real-world scenario. Such a pair is also likely to contain entities that
are not selected in the ﬁrst approach. This leads to capturing entity pairs and their relations independent of KBs.
5. Annotate Relations
We ask workers recruited by DeepNatural,35 a Korean crowdsourcing platform, to annotate
each entity pair (esubj, eobj) with a relation label r. We instruct workers to focus on the current relationship, not ones
from the past. For instance, if a person described in a sentence is a former member of a certain organization, workers
are asked not to choose the relation per:employee_of. We also ask them to avoid relying on external knowledge, or
common sense, to infer the relation from the context solely within a given sentence. Workers report examples that
contain hate speech, biased expressions, or personally identiﬁable information. In addition, they are asked to report
sentences with incorrect entity boundaries.
We employ 163 qualiﬁed workers, each of which correctly labelled at least 4 out of 5 questions during the pilot
annotation phase. After the pilot phase, 3 workers are assigned to each example independently to label the relation.
Figure 3.5.1 shows the annotation tool for crowdsourcing. To reduce cognitive burden of annotators, we provide a small
number of candidate relations at ﬁrst. The candidates consist of relations that can be deﬁned between types of entity
pair predicted by the NER models. If one cannot ﬁnd appropriate r in the candidates, they are expanded to all relation
classes.
34Released by NIA, a government-funded institution. Available at https://aihub.or.kr/aidata/84.
35https://deepnatural.ai/
30

--- Page 31 ---

Table 11: Relation distribution of KLUE-RE.
Train
Dev
Test
Relation Class
Count
Ratio
Count
Ratio
Count
Ratio
no_relation
9,534
29.36%
4,631
59.64%
4,632
59.64%
org:dissolved
66
0.20%
11
0.14%
10
0.13%
org:founded
450
1.39%
20
0.26%
20
0.26%
org:place_of_headquarters
1,195
3.68%
194
2.50%
193
2.49%
org:alternate_names
1,320
4.07%
78
1.00%
77
0.99%
org:member_of
1,866
5.75%
104
1.34%
105
1.35%
org:members
420
1.29%
122
1.57%
122
1.57%
org:political/religious_afﬁliation
98
0.30%
13
0.17%
13
0.17%
org:product
380
1.17%
235
3.03%
235
3.03%
org:founded_by
155
0.48%
11
0.14%
11
0.14%
org:top_members/employees
4,284
13.19%
513
6.61%
514
6.62%
org:number_of_employees/members
48
0.15%
17
0.22%
18
0.23%
per:date_of_birth
1,130
3.48%
12
0.15%
12
0.15%
per:date_of_death
418
1.29%
13
0.17%
13
0.17%
per:place_of_birth
166
0.51%
11
0.14%
10
0.13%
per:place_of_death
40
0.12%
10
0.13%
11
0.14%
per:place_of_residence
193
0.59%
124
1.60%
125
1.61%
per:origin
1,234
3.80%
118
1.52%
118
1.52%
per:employee_of
3,573
11.00%
242
3.12%
241
3.10%
per:schools_attended
82
0.25%
11
0.14%
11
0.14%
per:alternate_names
1,001
3.08%
104
1.34%
103
1.33%
per:parents
520
1.60%
27
0.35%
27
0.35%
per:children
304
0.94%
27
0.35%
27
0.35%
per:siblings
136
0.42%
24
0.31%
24
0.31%
per:spouse
795
2.45%
41
0.53%
40
0.52%
per:other_family
190
0.59%
34
0.44%
35
0.45%
per:colleagues
534
1.64%
220
2.83%
220
2.83%
per:product
139
0.43%
67
0.86%
69
0.89%
per:religion
96
0.30%
13
0.17%
12
0.15%
per:title
2,103
6.48%
718
9.25%
718
9.25%
Total
32,470
100.00%
7,765
100.00%
7,766
100.00%
We take majority-voted labels as gold labels. For each example without a majority label, the top 30 annotators select the
ﬁnal label from the annotated labels. We do not include examples reported as hate speech, biased, or to have privacy
issues. The inter-annotator agreement (Krippendorff’s α) on the annotated dataset is 0.701 [67].
Final Dataset
KLUE-RE consists of 32,470 training, 7,765 development and 7,766 test examples. For real-world
scenario, we only use examples created from uniform sampling when building the development and test sets. In the test
set, we only include sentences with entities that do not appear in the training set.
The average length of a sentence in KLUE-RE is 95.9 characters including whitespaces. The proportions of the entity
types are: PER (38.1%), ORG (36.3%), LOC (6.2%), DAT (6.2%), POH (11.9%), and NOH (1.3%). The distribution of
the relation classes is shown in Table 11.
3.5.2
Evaluation Metrics
The evaluation metrics for KLUE-RE are 1) micro F1 score on relation existing cases, and 2) area under the precision-
recall curve (AUPRC) on all classes. Micro F1 score is a harmonic mean of micro-precision and micro-recall. It
measures the F1 score of the aggregated contributions of all classes. It gives each sample the same importance, thus
naturally weighting more on the majority class. We remove the dominant class (no_relation) for this metric to not
incentivize the model that focus more on predicting negative class. AUPRC is an averaged area under the precision-recall
curves whose x-axis is recall and y-axis is the precision of all relation classes. It is a useful metric for this imbalanced
data setting where important positive examples are rarely occurred.
31

--- Page 32 ---

3.5.3
Related Work
Many researchers attempt to build KBs from unstructured text through automatically identifying relational facts between
entity pairs in plain text by applying machine learning techniques. Doddington et al. [31] and Hendrickx et al. [52]
construct English datasets to train such models, including a relatively small number of relation classes for general
domain text. Mintz et al. [91] further propose distant supervision to automatically annotate plain text by aligning it to
the schema of KBs. This allows researchers to scale up the size of RE datasets [116, 153, 48, 147, 149]. Among these
recent studies, TACRED [153] is the most widely used dataset, built based on the popular relation schema TAC-KBP
[87] which mainly focuses on person and organization entities. Speciﬁcally, TACRED contains 106,264 examples
annotated with the 42 relation classes. Yu et al. [149] also proposes a dialogue-based RE task by reﬁning TAC-KBP to
obtain 36 relation classes adapted for the dialogue domain. We also follow TAC-KBP to build the relation schema and
modify them suitable for our situation.
In the cases of languages other than English, there are only a few existing benchmarks, including one in Chinese [141],
one in German [121], and one in French [55]. Nam et al. [93] propose an RE dataset in Korean using distant supervision
to automatically generate and annotate examples. It however has a relatively small test set (∼3k), making it difﬁcult to
evaluate performance for the total 49 relation classes properly. Moreover, since there is no negative class (no_relation in
ours), it is likely to encourage models to overly predict false positives [153]. We thus consider KLUE-RE as a standard
large-scale RE benchmark to properly evaluate Korean language models.
3.5.4
Conclusion
We propose KLUE-RE, a large-scale human-annotated RE benchmark for Korean. To overcome the lack of large-scale
and up-to-date Korean KBs, we design an efﬁcient candidate collection method, coupled with an effective annotation
scheme. KLUE-RE can not only be used for online information extraction but also contribute to building a large-scale
knowledge graph from unstructured texts. We therefore expect KLUE-RE to be a starting point for building a large-scale,
ever-growing public KB in Korean, as well as a valuable Korean NLU benchmark.
32

--- Page 33 ---

3.6
Dependency Parsing (DP)
Dependency parsing (DP) is an NLP task that aims at ﬁnding relational information among words. It has been an
important component in many NLP systems, because of its ability to capture the syntactic feature of a sentence. We
include DP in KLUE to evaluate the representational power of language models in terms of syntactic features.
Formally, a dependency parser predicts a graph structure of an input sentence based on the dependency grammar
[29, 28]. In general, a parsed tree consists of dependency arcs, connecting dependents to their heads, and the dependency
labels attached to the arcs that represent the relations between dependents and their heads.
Figure 5: An example of dependency parsing, that translates to "Chul-Soo ate an apple."
For example, Figure 5 shows a parsed result of the example sentence: “철수가사과를먹었다(Chul-Soo ate an apple.)”.
In the tree, arrows depart from head and point to their dependents. Thus ‘철수가(Chul-Soo)’ and ‘사과를(an apple)’
are dependents of ‘먹었다(ate)’ and ‘먹었다(ate)’ is the head of ‘철수가(Chul-Soo)’ and ‘사과를(an apple)’. Also,
‘철수가(Chul-Soo)’ is dependent on ‘먹었다(ate)’ with a “Subject” relation. This dependency relation label is called
DEPREL. For DEPREL, we follow the TTA Dependency annotation scheme36 consisting of a combination of 9 syntax
tags and 6 function tags.
Since each word in a sentence has a pair of dependency information (HEAD, DEPREL), DP is conventionally formulated
as a word-level sequence tagging task. We evaluate a model’s performance using unlabeled attachment score (UAS) and
labeled attachment score (LAS). During the evaluation, labels with a cumulative frequency of 1% from the bottom are
grouped into the OTHERS label to compensate for the negative impact of lower frequency labels on LAS.
Figure 6: A demonstration of the KLUE-DP output format using a sentence that translates to “Chul-Soo ate an apple.”
We represent the output in a CoNLL-like format, as shown in Figure 6. This format consists of 6 columns, each column
contains a word index (ID), word form (FORM), lemma of word form (LEMMA), part-of-speech tag (POS), head of
the current word (HEAD), and dependency relation (DEPREL).
3.6.1
Dataset Construction
Source Corpora
To build our corpus as a suitable dataset for a general-usage DP model, we take into account both
formal and informal texts. We use WIKITREE and AIRBNB as source corpora. WIKITREE consists of news articles
and represents grammatically sound formal texts. On the other hand, AIRBNB mostly consists of user-generated reviews
containing web texts, thus showing frequent omission of components and free word order. We collect the same rate
of data from both WIKITREE and AIRBNB so that our dataset represents both reﬁned written sentences and noisy
colloquial texts.
Annotation Protocol
Since the part-of-speech indicates how the word functions grammatically in a sentence, it is
highly related to the dependency relations. To utilize POS information as an additional syntactic feature, we ﬁrst annotate
POS on the corpus prior to dependency relation annotation. To this end, we follow TTA POS tagging guideline.37 We
use annotated POS information when constructing the DP corpus.
36https://aiopen.etri.re.kr/data/003.%EC%9D%98%EC%A1%B4%EA%B5%AC%EB%AC%B8%EB%B6%84%EC%84%9D_%EA%
B0%80%EC%9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8.pdf
37https://aiopen.etri.re.kr/data/001.%ED%98%95%ED%83%9C%EC%86%8C%EB%B6%84%EC%84%9D_%EA%B0%80%EC%
9D%B4%EB%93%9C%EB%9D%BC%EC%9D%B8.pdf
33

--- Page 34 ---

Table 12: Syntax and function tagset (label types) of TTA DP guideline.
Label Type
Description
Syntax
NP
Noun Phrase
VP
Verb Phrase
AP
Adverb Phrase
VNP
Copula Phrase
DP
Adnoun Phrase
IP
Interjection Phrase
X
Pseudo Phrase
L
Left Parenthesis and Quotation Mark
R
Right Parenthesis and Quotation Mark
Function
SBJ
Subject
OBJ
Object
MOD
Noun Modiﬁer
AJT
Predicate Modiﬁer
CMP
Complement
CNJ
Conjunction
Next, we modify the original TTA DP guideline for dependency relation annotation. We add guides for spoken and web
data, since the original guideline only contains instruction for annotating written data.
We follow TTA DP tagset, which is a standard in Korean. As shown in Table 12, it is made up of a combination of 9
syntax tags and 6 function tags. The syntax tag indicates the POS for token, and there are NP (noun phrase), VP (verb
phrase), AP (adverb phrase), VNP (copula phrase), DP (adnoun phrase), IP (interjection phrase), X (pseudo phrase), L
(left parenthesis and quotation mark) and R (right parenthesis and quotation mark). The function tag indicates what
function the token performs in relation to the head, and there are SBJ (subject), OBJ (object), MOD (noun modiﬁer),
AJT (predicate modiﬁer), CMP (complement), and CNJ (conjunction). The TTA DP combines a syntax tag and a
function tag into a single tag, such as NP_SBJ (noun phrase subject) and VP_AJT (verb phrase adverb).
Annotation Process
To build highly reliable corpora for both POS and DP annotation, we use an annotation tool
provided by DeepNatural,38 a Korean crowdsourcing platform, which asks the annotators to annotate cross-reference.
After POS annotation is completed, dependency relation annotation proceeds on the same sentences by using POS
information. Both POS and DP are annotated by ten PhD students in Korean linguistics, who previously contributed to
constructing MODU39 [98] opened by the National Institute of the Korean Language. Prior to annotation, we instruct
them with our guideline. During annotation, we respond to questions from annotators in real-time, and accordingly, the
guidelines are iteratively updated. Annotators report sentences containing hate speech or bias during the annotation. In
addition, sentences containing personal information (e.g., name, address, phone number, etc.) are reported. The reported
sentences are removed from the dataset after our inspection.
Annotations are validated in two steps. First, each annotator reviews and corrects POS and DP labels annotated by other
annotators. Then we ﬁnally review all data and revise remaining mislabeled sentences.
Final Dataset
KLUE-DP consists of a total of 14,500 sentences, including 7,250 sentences for WIKINEWS and
7,250 sentences for AIRBNB. POS annotation is given in the 4th column of CoNLL-like format, along with HEAD and
DEPREL information in next columns. We set the train/dev/test split as 10,000, 2,000, 2,500 sentences. Tables 13 and
14 show detailed statistics of KLUE-DP.
3.6.2
Evaluation Metrics
The evaluation metrics for KLUE-DP are 1) unlabeled attachment score (UAS) and 2) labeled attachment score (LAS),
which are popular metrics for DP. Given the goal of DP is to predict head indices (HEAD) and dependency relation
classes (DEPREL), UAS only counts HEAD prediction while LAS counts both HEAD and DEPREL. Speciﬁcally,
38https://deepnatural.ai/
39https://corpus.korean.go.kr/main.do
34

--- Page 35 ---

Table 13: Statistics for KLUE-DP.
Source
|Train|
|Dev|
|Test|
Total
WIKITREE
5,000
1,000
1,250
7,250
AIRBNB
5,000
1,000
1,250
7,250
Total
10,000
2,000
2,500
14,500
Table 14: Label statistics for KLUE-DP. Predictions on the labels from VP_CMP to NP_SVJ is be merged into OTHERS
when calculating LAS.
Label
|Train|
|Dev|
|Test|
Total
NP
23,902 (20.88%)
4,559 (20.27%)
4,884 (19.51%)
33,345 (20.58%)
NP_AJT
17,552 (15.33%)
3,415 (15.18%)
3,526 (14.09%)
24,493 (15.12%)
VP
16,786 (14.66%)
3,322 (14.77%)
3,917 (15.65%)
24,025 (14.83%)
NP_SBJ
13,412 (11.71%)
2,737 (12.17%)
3,112 (12.43%)
19,261 (11.89%)
VP_MOD
12,210 (10.66%)
2,457 (10.92%)
2,682 (10.71%)
17,349 (10.71%)
NP_OBJ
8,531 (7.45%)
1,691 (7.52%)
1,951 (7.79%)
12,173 (7.51%)
AP
6,638 (5.80%)
1,274 (5.66%)
1,716 (6.85%)
9,628 (5.94%)
NP_CNJ
3,945 (3.45%)
795 (3.53%)
764 (3.05%)
5,504 (3.40%)
NP_MOD
3,450 (3.01%)
659 (2.93%)
727 (2.90%)
4,836 (2.98%)
VNP
2,550 (2.23%)
495 (2.20%)
558 (2.23%)
3,603 (2.22%)
DP
1,994 (1.74%)
376 (1.67%)
419 (1.67%)
2,789 (1.72%)
VP_AJT
882 (0.77%)
196 (0.87%)
182 (0.73%)
1,260 (0.78%)
VNP_MOD
854 (0.75%)
180 (0.80%)
164 (0.66%)
1,198 (0.74%)
NP_CMP
408 (0.36%)
83 (0.37%)
97 (0.39%)
588 (0.36%)
VP_SBJ
338 (0.30%)
59 (0.26%)
94 (0.38%)
491 (0.30%)
VP_CMP
330 (0.29%)
59 (0.26%)
91 (0.36%)
483 (0.30%)
VP_OBJ
279 (0.24%)
39 (0.17%)
68 (0.27%)
386 (0.24%)
VNP_CMP
131 (0.11%)
27 (0.12%)
26 (0.10%)
184 (0.11%)
AP_MOD
59 (0.05%)
15 (0.07%)
11 (0.04%)
84 (0.05%)
X_AJT
41 (0.04%)
14 (0.06%)
10 (0.04%)
63 (0.04%)
VNP_AJT
37 (0.03%)
13 (0.06%)
9 (0.04%)
59 (0.04%)
VP_CNJ
37 (0.03%)
7 (0.03%)
7 (0.03%)
46 (0.03%)
IP
27 (0.02%)
4 (0.02%)
6 (0.02%)
41 (0.03%)
X
26 (0.02%)
4 (0.02%)
2 (0.01%)
31 (0.02%)
VNP_OBJ
18 (0.02%)
3 (0.01%)
2 (0.01%)
26 (0.02%)
X_SBJ
17 (0.01%)
3 (0.01%)
2 (0.01%)
21 (0.01%)
X_OBJ
12 (0.01%)
2 (0.01%)
2 (0.01%)
17 (0.01%)
VNP_SBJ
11 (0.01%)
1 (0.00%)
2 (0.01%)
14 (0.01%)
L
3 (0.00%)
1 (0.00%)
1 (0.00%)
4 (0.00%)
AP_AJT
2 (0.00%)
1 (0.00%)
1 (0.00%)
4 (0.00%)
X_CMP
2 (0.00%)
1 (0.00%)
0 (0.00%)
4 (0.00%)
X_CNJ
2 (0.00%)
1 (0.00%)
0 (0.00%)
3 (0.00%)
X_MOD
2 (0.00%)
0 (0.00%)
0 (0.00%)
2 (0.00%)
AP_CMP
1 (0.00%)
0 (0.00%)
0 (0.00%)
2 (0.00%)
R
1 (0.00%)
0 (0.00%)
0 (0.00%)
1 (0.00%)
VNP_CNJ
1 (0.00%)
0 (0.00%)
0 (0.00%)
1 (0.00%)
AP_SBJ
0 (0.00%)
0 (0.00%)
0 (0.00%)
1 (0.00%)
NP_SVJ
0 (0.00%)
0 (0.00%)
0 (0.00%)
0 (0.00%)
Total
114,491
22,496
25,033
162,020
UAS calculates macro F1 score on HEAD prediction, while LAS calculates macro F1 score on DEPREL whose HEAD
prediction is correct. Both scores give the same importance to all classes. For LAS, since DEPREL distribution is highly
skewed, we combine the predictions on the labels with a cumulative frequency of 1% from the bottom into a single
label (OTHERS) and then calculate F1 score. The less-appeared labels are referred in Table 14.
35

--- Page 36 ---

3.6.3
Related Work
The Penn Treebank [84] is a constituency parsed dataset created from 1989 to 1996. It has a size of about 3 million
words, including IBM computer manuals, nursing notes, Wall Street Journal articles, phone conversations. A total of 48
POS tags and 18 syntax tags are used by combining meta tags such as symbols. The Penn Treebank was the best-known
parsing data set before dependency parsing became prevalent. Later studies convert the Penn Treebank to dependency
parsing [86, 20].
A representative DP corpus is the Universal Dependencies(UD) dataset.40 UD is de facto standard of DP data, aiming for
a uniﬁed treebank annotation in various languages. Google Universal POS [106] composed of 12 tags, was developed
and a corpus was built that applied it to 25 different languages. Also de Marneffe and Manning [28] studied guidelines
for dependency parsing markers used in Stanford parsers [65]. The Universal Dependency Treebank Project in 2013
attempted to combine the two studies above to have a consistent annotation system for multiple languages. UD started
by modifying and supplementing this. UD ﬁrst started in 2015 and Nivre et al. [97] and 10 corpora in a total of 10
languages were released through the website. As of 2021, UD (UD 2.7v) offers 104 languages and 183 corpora.
The corpus constructed with UD scheme is made according to a certain structure called CoNLL-U format. Since UD
aims to study general linguistic universality by using the same tag and annotation system in different languages, a
uniﬁed format for integrating and managing each corpus is needed. The CoNLL-U format is a modiﬁed version of this
CoNLL format so that it can well represent Universal dependency parsing. CoNLL-U format consists of 10 columns,
each column display a word index (ID), word form (FORM), lemma of word form (LEMMA), universal part-of-speech
tag (UPOS), language-speciﬁc part- It represents of-speech tag (XPOS), list of morphological features (FEATS), head of
the current word (HEAD), dependency relation (DEPREL), enhanced dependency graph (DEPS), any other annotation
(MISC). In this format, each word stands on a line along with different associated features (word form, lemma, POS tag,
etc.) and we adopt this format in our ﬁnal dataset.
In Korean, DP corpus is divided into those that follow the UD scheme and those that do not. Among the former are The
Google Korean Universal Dependency Treebank (GKT), The KAIST Korean Universal Dependency Treebank (KTB),
and The Penn Korean Universal Dependency Treebank (PKT). These three datasets are converted from The Google
Korean Treebank [86], The Kaist Treebank [128], and The Penn Korean treebank [47] according to the UD scheme,
respectively [20]. These were ﬁrst automatically converted according to the head-ﬁnding rule and then heuristically
modiﬁed. These are composed of 6k, 27k, and 5k sentences, respectively, and include the genres of blog, newswire,
literature, academic, and manuscript. Among them, PKT was revised by changing the analysis unit and several rules to
further reveal the characteristics of Korean [99].
Corpora that do not follow the UD scheme include the TTA DP Corpus built by Electronics and Telecommunications
Research Institute (ETRI) and the Modu Corpus [98] built by the National Institute of the Korean Language (NIKL).
Both corpora follow the CoNLL format, and use their own tagset, which was developed from the 21st century Sejong
Plan corpus. The syntactic analysis corpus of the 21st century Sejong Plan is constructed according to the constituency
grammar, following a scheme similar to the Penn Treebank. Unlike the dependency grammar, which grasps only
the dominant relationship between two words, the constituency grammar identiﬁes the relationship between words
hierarchically. However, since Korean has relatively free word order, dependency parsing is more suitable than phrase-
structure parsing. Studies on converting the 21st century Sejong Plan corpus into DP format have been conducted, and
since then, corpora that use the 21st century Sejong Plan’s tagset but follow dependency parsing have been constructed.
The size of TTA DP corpus is about 27k, and the Modu corpus about 2000k. Unlike UD, which emphasizes general
linguistic characteristics, better represents the characteristics of Korean as an individual language, and serves as a
national standard for Korean DP tagging. Also, there are already corpus annotated according to the TTA scheme, so we
consider compatibility between them and our benchmark. For this reason, we constructed the KLUE-DP using the TTA
tagset.
3.6.4
Conclusion
We build a Korean DP benchmark KLUE-DP consisting of formal news and informal user-generated web data. KLUE-
DP is helpful for developing a DP model that can be used in multiple domains. POS tagging is performed together to
improve DP performance, and the tagset and guideline for DP and POS tagging are applied by revising the existing
TTA dataset. This guideline is customized to reﬂect the characteristics of Korean (agglutinative, free word order, etc.),
and it also tackles omission of predicates in web data or errors in spacing. We hope that our benchmarks will help in the
development of Korean DP models and other natural language processing.
40https://universaldependencies.org
36

--- Page 37 ---

3.7
Machine Reading Comprehension (MRC)
Machine reading comprehension (MRC) is a task designed to evaluate models’ abilities to read a given text passage and
then answer a question about the passage, that is, its ability of comprehension.
Most of existing, widely-used MRC benchmarks are largely in English [21, 56, 60, 112, 113, 145, 150]. Those resources
are widely used in evaluating pre-trained language models since it is one of the most intuitive methods for measuring text
comprehension. SQuAD 1.1 [112] and SQuAD 2.0 [113] are popular evaluation tasks along with GLUE [30, 82, 22, 71].
BoolQ [21], ReCoRD [150], and MultiRC [60] are selected as a member of SuperGLUE for rigorous evaluation of
language models. Recently, open-domain QA task which can be viewed as an MRC task without a given text passage
[69, 56, 145, 38], is included in a knowledge-intensive NLP task benchmark [105].
Motivated by those datasets, MRC has become an essential task in NLU benchmarks for various languages such
as Indonesian [137], Chinese [142], and Russian [125]. In Korean, however, an appropriate MRC benchmark is not
available because existing Korean MRC datasets are either less challenging, limited in access, or simply machine-
translated from an English dataset [79, 1, 74]. We therefore include MRC in KLUE and create a new challenging
Korean MRC benchmark (KLUE-MRC) with the following contributions:
• Providing multiple question types: In order to evaluate different aspects of MRC capability of models, we provide
three question types: paraphrase, multi-sentence reasoning, and unanswerable. We collect questions by following
strict guidelines with speciﬁc sets of rules for each type.
• Preventing reasoning shortcuts: We prevent MRC models from exploiting reasoning shortcuts with simple word-
matching by enforcing lexical and syntactic variations when workers generate questions. Also, we aim to generate
questions which can be answered by considering the full query sentence.
• Multiple passage domains accessible to everyone : We include news domain passages as well as Wikipedia. To
guarantee CC BY-SA license of KLUE-MRC, we made signed contracts with corresponding news providers.
We formulate MRC as a task of predicting the answer span of the question from the given text passage. The input is
a concatenated sequence of the question and the passage separated with a delimiter. The output is the start and end
positions of the predicted answer span within the passage.
We evaluate models with two metrics: 1) exact match (EM) and 2) character-level ROUGE-W. Note that character-level
ROUGE-W is different from the character-level F1 score used in the previous Korean MRC datasets. If the question
is unanswerable within the given passage, the model should predict the empty answer string. The motivation of our
metrics are described in Section 3.7.2.
3.7.1
Dataset Construction
Source Corpora
First, we collect passages from Korean WIKIPEDIA and news articles provided by The Korea
Economy Daily and ACROFAN. WIKIPEDIA articles are one of the most commonly used resources for creating
MRC datasets. We additionally include news articles reporting contemporary social issues to enhance diversity of
passages. They are provided by The Korea Economy Daily and ACROFAN. As news articles are generally copyrighted
work, we sign a contract with the news providers to use and redistribute the articles under CC BY-SA license only for
building a dataset for machine learning purposes. We believe multi-domain corpus can help MRC models enhance their
generalizability.
We preprocess the corpus to collect passages. For WIKIPEDIA articles, we remove duplicates in other existing Korean
MRC benchmarks (e.g., KorQuAD) for precise evaluation of models. Then, we split each article by its sections to
obtain passages. For the news articles, we ﬁlter out political articles and articles belonging to categories which have less
than 100 articles. We ﬁnally gather all preprocessed passages whose length is longer than 512 and shorter than 2048 in
characters.
Annotation Protocol
We annotate questions and answers by giving passages to crowdworkers. We provide a detailed
tutorial session to introduce our guidelines. 60 out of 80 workers are selected after a pilot test of creating 15 question-
answer pairs with a given passage. The selected workers generate questions and label corresponding answers spans
(for Types 1 and 2) or fake answers spans (for Type 3). We use Tagtog annotation toolkit 41 for the annotation. We
assign three inspectors for each question type to validate the generated questions and answers following common and
type-speciﬁc guidelines. If the generated question-answer pair fails to pass the inspection, the worker reﬁnes it based on
the feedback given by the inspector.
41https://www.tagtog.net/
37

--- Page 38 ---

1. Common Guidelines
We ﬁrst build common annotation guidelines for crowdworkers. The workers are required to
follow the instructions during corresponding question generation and answer span annotation for all three question
types as below.
A question should:
• Be natural as a web search query: Trying to generate challenging questions can lead to the use of unnatural
expressions. We guide workers to make natural questions as if they are for web search queries. We care about the
generalizability of questions to extend the task to open-domain QA tasks in future work.
• Avoid omission: Pronoun-dropping is prevalent in Korean, hence it tends to omit the subject or object. The omission
can result in ambiguity for ﬁnding answers. We explicitly guide workers to keep all grammatical components in
generated questions.
• Not copy a phrase in the passage: Questions might have similar meaning to some phrases in the passage but should
not contain exactly the same phrase. This mitigates high word-overlap between questions and the passage as reported
in previous work [122].
• Not refer to external knowledge: Questions need to be fully understood without any external knowledge. We do not
allow workers using their background knowledge or any world knowledge to generate a question. Questions should
be derived solely based on the given passage.
• Be meaningful in every part for ﬁnding the answer: Answers should not be found with only a small fraction of
the question. We encourage workers to generate questions that require understanding of the whole question text to
ﬁnd an answer. We do not allow the use of expressions that appear only once in the passage because models can easily
infer answers without understanding the whole question.
An answer should:
• Be a unique entity within a passage: To clarify what to ask, only a single answer should be inferred from the
question. When answers can be represented in various lexical forms, workers should mark all answer spans (e.g.
Television, TV).
• Not be the main topic or title: We aim to prevent a known artifact which the most frequently appeared words within
a given passage are likely to be the answer [66].
2. Type-Speciﬁc Guidelines
Here we elaborate question type-speciﬁc guidelines. These guidelines are additionally
presented to workers along with the common guideline above.
2.1. Question Paraphrasing (Type 1) Type 1 examples focus on paraphrasing the passage sentences when generating
questions to reduce word overlap between them. The paraphrasing enables us to validate whether the model can correctly
understand the semantics of the paraphrased question and infer the answer [122].
Table 15: Paraphrase question type example for Korean and its English translation
Type
Korean
English (Translated)
Passage
브르타뉴공국은939년트랑라포레전투에서기원
을했으며, 브르타뉴와노르망디간에경계인쿠에
농강에세워졌다.
Duchy of Brittany originates in the Battle of
Trans-la-Forêt of year 939, and was established
on and around the Couesnon River, the boundary
of Britanny and Normandy.
Good
Question
브르타뉴와노르망디를구분짓는것은?
What distinguishes Britanny and Normandy?
Bad
Question
브르타뉴와노르망디간의경계는?
What is the boundary of Britanny and Nor-
mandy?
Answer
쿠에농강
Cuesnon River
In our annotation guide for paraphrased questions, we further prevent workers from generating them by simply shifting
the order of subsequent phrases or changing the functional particles. Speciﬁcally, workers create questions by following
principles:
• Either syntactic or lexical variation should be applied to text snippets in the passage.
38

--- Page 39 ---

– For syntactic variation, reconstructing the structure of the original sentence is preferred. Minimal changes such
as swapping order between the nearby phrases is not allowed.
– For lexical variation, changing verbs or modiﬁers is required, and variation of noun phrases is recommended.
• More than half of the words in the question should not overlap with the corresponding part (sentence) of the passage.
Then we comprehensively check whether the question has low word overlap with the passage. As shown in Table 15,
where Cuesnon River is the answer, the question paraphrases the given evidence sentence (“the boundary of Britanny
and Normandy”) by providing a new sentence structure. The structure is changed from a wh-question with copula to a
question with an intransitive verb. Also, a new term “distinguishes” is introduced which replaces the phrase “is the
boundary of”.
2.2. Multiple-Sentence Reasoning (Type 2)
Type 2 examples focus on making questions requiring multiple-sentence
reasoning. Multiple-sentence reasoning requires models to derive answers from the questions by reasoning over at
least two sentences in the passage. We focus on evaluating whether an MRC model can infer the answer span by
comprehensively aggregating the information spread across the passage. We carefully design annotation guidelines for
multiple-sentence reasoning examples. Since Min et al. [90] report multiple-sentence reasoning questions can easily fall
back to single-sentence reasoning, we aim to avoid such cases by guiding workers to follow the steps below:
• (Step 1.) Find at least two statements in the given passage that share some properties.
• (Step 2.) Select one as the answer among the entities regarding the shared properties.
• (Step 3.) Generate a question with the selected entity.
Table 16: Multiple sentence reasoning question type example for Korean and its English translation
Type
Korean
English (Translated)
Passage
트라야누스황제시대(98년-117년)에로마제국은
북으로는스코틀랜드에서남으로는아프리카수단
까지, 서로는포르투갈의대서양연안에서동으로
는카프카스지방까지최대판도를이룩했다. 오늘
날면적으로환산하면현재미국면적의2/3에달하
고인구도현미국의절반에약간안되는정도로추
산된다. 서기5세기경서로마제국은멸망후게르
만족의여러독립국가로갈라져프랑크왕국, 신성
로마제국등로마의후계자를자처하는여타서유
럽의정치세력들이나타난다.
Under Trajan(AD 98-AD 117), Roman Empire
reached its territorial peak. In terms of the area
today, it is estimated to represent two-thirds of
the current U.S. area and its population is only
slightly less than half that of the current U.S.
Plagued by internal instability and attacked by
various migrating peoples, the western part of
the empire broke up into independent barbarian
kingdoms in the 5th century.
Statement A
오늘날면적으로환산하면현재미국면적의2/3에
달하고인구도현미국의절반에약간안되는정도
로추산된다.
In terms of the area today, it is estimated to
represent two-thirds of the current U.S. area
Statement B
트라야누스황제시대(98년-117년)에로마제국은
북으로는스코틀랜드에서남으로는아프리카수단
까지, 서로는포르투갈의대서양연안에서동으로
는카프카스지방까지최대판도를이룩했다.
Under Trajan(AD 98-AD 117), Roman Empire
reached its territorial peak.
Shared
Properties
로마제국, 트라야누스황제시대(98년-117년)
Roman Empire, Trajan(AD 98-AD 117)
Question
로마제국의면적이현재미국면적의2/3에다다르
던시기는언제인가?
When was the area of the Roman Empire two-
thirds of that of the current U.S.?
Answer
트라야누스황제시대(98년-117년) / 트라야누스황
제시대/ 98년-117년
Trajan(AD 98-AD 117) / Trajan / AD 98-AD
117
The example in Table 16 follows the steps described above. Shared properties between the two statements (A: “In terms
of the area today, it is estimated to represent two-thirds of the current U.S. area”, B: “Under Trajan(AD 98-AD 117),
Roman Empire reached its territorial peak.”) are “Roman Empire” and “(Under) Trajan(AD 98 -AD 117)”. Assume
we pick “Trajan(AD 98-AD 117)” as the answer and generate a question “When was the area of the Roman Empire
two-thirds of that of the current U.S.?”. Neither of the two statements is enough to single out the answer alone. When
given the question and statement A alone, it is not possible to resolve an answer between “Trajan(AD 98-AD 117)”
and “the 5th century” which both represent time period in the passage. Since statement B does not include speciﬁc
information on the territory size, it is also not sufﬁcient to narrow down the answer by itself. Therefore, statement A
and B both needs to be aggregated to correctly answer the question.
39

--- Page 40 ---

2.3. Unanswerable Questions (Type 3)
Type 3 examples are questions unable to be answered within the given
passage. We name these as ‘unanswerable’ questions. In the real world, a question is often unanswerable if a passage
is not available. If a model is built upon the premise that an answer always exists within the passage, it would not
effectively handle such cases as SQuAD 2.0 [113] pointed out. We therefore add unanswerable questions in our
benchmark to incentivize models to identify whether a question is answerable or not.
In the annotation guideline, we present the following principles to generate desirable unanswerable questions. The
unanswerable questions should:
• Be relevant to the passage: An entity appearing in the given passage should be included in the question. The
entity makes the question relevant to the passage. Otherwise the question would be too easy to be determined as
unanswerable.
• Have fake answers within the passage: A fake answer is plausible but incorrect regarding the corresponding
question. The fake answer should exist in the passage as a distractor.
• Not have correct answers within the passage: Despite the existence of fake answers, the correct answer for the
generated question must not exist in the passage.
In our setting, a model is likely to fail to identify the question’s unanswerability based on the word overlap between the
question and the passage. Our question includes entities from the passage which increases the overlap. In that case, an
MRC model would choose plausible fake answers that exist in the passage.
Table 17 shows an example of the Type 3 problem. The question includes “bandwidth” which also exists in the given
passage. The question is asking for the bandwidth, so “1 to 5 Gigabit Ethernet” would be a plausible but incorrect
answer. There is no cue about the correct answer to “bandwidth-hungry server” from the question in the passage. The
model should predict the empty string using the out of the context span range, such as using the [CLS] token from
BERT.
Table 17: Unanswerable question type example for Korean and its English translation
Type
Korean
English (Translated)
Passage
아직도대역폭이많이필요하지않은서버는1-5기
가비트이더넷을사용한다.
Servers that still do not require much bandwidth
use 1 to 5 Gigabit Ethernet.
Question
대역폭이많이필요한서버는어느대역을사용하
는가?
Which bandwidth does the bandwidth-hungry
server use?
Fake
Answers
1-5기가비트이더넷
1 to 5 Gigabit Ethernet
Annotation Process
We employ workers recruited by SelectStar,42 a Korean crowdsourcing platform, to make each
type of question and answers for a given passage. For type 1, 28 workers annotate examples and other 3 workers
inspect all of them. For types 2 and 3, 19 and 13 workers annotate examples and other 3 and 2 workers validate them,
respectively. If the generated question is rejected by the inspectors, it is regenerated based on the feedback.
To meet the ethical standards, examples which contain sexual, violent, hate, bias or any other ethically inappropriate
contents are eliminated. We manually re-check all examples at the end of the annotation process. Through the ﬁltering
process, we remove 173 examples in total.
Final Dataset
KLUE-MRC consists of 12,207 paraphrasing-based questions, 7,895 multi-sentence reasoning ques-
tions, and 9,211 unanswerable questions. In total, 29,313 examples are made with 22,343 documents and 23,717
passages. As we prioritize creating a challenging dataset for evaluating MRC models, we give more examples to dev
and test splits. We set the train/dev/test split ratios as 6:2:2 for robust evaluation, resulting in 17,554 training, 5,841
development and 5,918 test examples. For each split, we randomly sample the examples from each question type
independently to balance the number of question types. Tables 18 and 19 show the detailed statistics of KLUE-MRC.
3.7.2
Evaluation Metrics
The evaluation metrics for KLUE-MRC are 1) exact match (EM) and 2) character-level ROUGE-W (ROUGE) [80],
which can be viewed as longest common consecutive subsequence (LCCS)-based F1 score. EM is the most commonly
42https://selectstar.ai/
40

--- Page 41 ---

Table 18: Number of examples per each dataset split and question types.
Paraphrase
Multi-sentence
Unanswerable
Total
(41.65%)
(26.93%)
(31.42%)
(100.0%)
Train (60%)
7,308
4,729
5,517
17,554
Dev (20%)
2,437
1,571
1,833
5,841
Test (20%)
2,462
1,595
1,861
5,918
Total (100%)
12,207
7,895
9,211
29,313
Table 19: Statistics of KLUE-MRC.
|Train|
|Dev|
|Test|
Total
# Documents
12,174
5,075
5,094
22,343
# Passages
13,072
5,310
5,335
23,717
# Questions
17,554
5,841
5,918
29,313
Avg Length of Passage
1,004.62
1,014.64
1,010.13
1,008.10
Avg Length of Question
29.00
29.05
29.01
29.01
Avg Length of Answer
6.03
6.03
5.82
5.99
used metric for MRC tasks, which measures the equality of ground truth and predicted answer string. If there are
multiple gold labels, a model can earn score when at least one prediction is matched. In contrast, ROUGE gives a partial
score although a model fails to predict exactly matched answer. Due to the characteristics of Korean, an answer span
can be located inside a single word, hence subword-level span should be considered. ROUGE calculates F1 score of the
length ratio of LCCS to a prediction and the length ratio of LCCS to the ground truth string. In the case when multiple
ground truth answer spans have the same meaning but different lexical variations (e.g. TV, Television), we use the
maximum ROUGE score among the combinations of answers and the prediction. We do not adopt character-level F1
score (char F1), which is used in all the previous Korean MRC datasets, since it measures character overlap regardless
of the order. When a model predicts “한국의위인들(great people in Korea)” and an answer is “국한된범위(limited
scope)”, a metric should give a low score. ROUGE scores 15.38, whereas char F1 gives 54.55 due to the overlap of
“한”, “국”, and “위”.
3.7.3
Analysis
We investigate KLUE-MRC by comparing with other Korean MRC datasets. KorQuAD 1.0 [79] and 2.0 [63] are
commonly used in Korean MRC research, released with training and evaluation sets separately. However, KorQuAD 2.0
shows a quite different composition in contents compared to ours and KorQUAD 1.0, in speciﬁc, HTML tags and tables.
Therefore, we conduct comparison only with KorQuAD 1.0 dataset. KorQuAD 1.0 dev set was leveraged because its
test set is not available.
Question Difﬁculty of KLUE-MRC Evaluation Set
As we aim to make KLUE-MRC challenging, it is necessary
to check the difﬁculty of test sets. We compare the performance on the evaluation set of ours and KorQuAD 1.0 with
the model trained with both datasets in Table 20. We ﬁne-tune the model43 with a collection of the train set from both
datasets and test the model on each evaluation set.
KorQuAD 1.0 train examples (60,407) are almost four times larger than KLUE-MRC (17,554), and it may have resulted
in the higher performance for KorQuAD 1.0 dev set. We additionally conduct ﬁne-tuning with a collection of the same
amount of both train datasets for fair comparison. We adjust KorQuAD 1.0 train set to ﬁt the size of KLUE-MRC train
set by random sampling. Table 20 shows consistently lower scores of KLUE-MRC compared to KorQuAD 1.0. Thus,
our dataset is more challenging regardless of the size of train set.
Lexical Overlap
As high lexical overlap between question and passage can cause shortcut reasoning, reducing lexical
overlap is important to build a challenging dataset. To investigate the effects of the proposed strict guidelines and
challenging question types, we calculate the lexical overlap of ours and KorQuAD 1.0. The lexical overlap ratio is
calculated by dividing the number of common components between question and passage into the number of components
43We ﬁne-tune pretrained RoBERTa-base model with following hyperparameters: epochs 5, batch size 16, learning rate 3e-5, lr
warmup ratio 0.0.
41

--- Page 42 ---

Table 20: Difﬁculty comparison between KLUE-MRC test and KorQuAD 1.0 dev set.
KLUE + KorQuAD (Full:Full)
KLUE + KorQuAD (1:1)
Evaluation Dataset
EM
ROUGE
EM
ROUGE
KorQuAD 1.0 (Dev)
86.59
94.19
85.00
93.07
KLUE-MRC (Test)
70.42
75.42
69.75
75.20
Table 21: Comparison of evaluation scores between model prediction and human answer
Paraphrase
Multi-sentence
Unanswerable
Total
EM
ROUGE
EM
ROUGE
EM
ROUGE
EM
ROUGE
KLUE-RoBERTaBASE
67.74
75.73
65.07
73.13
72.48
72.48
68.51
74.01
Human
84.18
88.33
87.72
90.91
86.53
86.53
85.90
88.48
in the question. We exclude functional particles such as postposition(조사, josa) and ending components (어미, eomi)
when computing the overlap ratio via an open-sourced Korean POS tagger.44 We observe our lexical overlap ratio is
almost 10%p lower than that of KorQuAD dataset (70%). For each questions types, Types 1 and 3 show similar ratio in
range from 55% to 59%. Type 2 exhibits 68% overlap ratio.
Human Evaluation
We evaluate human performance on our KLUE-MRC to measure its difﬁculty concerning human
reading comprehension capabilities. We randomly sample 1,000 examples from our test set and hire three workers to
solve them. We select the score of the top scoring worker as human performance. Table 21 reports the comparison
between human performance and base model.
3.7.4
Related Work
In recent years, signiﬁcant progress has been achieved in English MRC research with challenging datasets of various
question types, including but not limited to: paraphrase, multi-sentence, and unanswerable.
Paraphrased questions have low word overlap between the question and reading passage, which prevents MRC models
from exploiting simple word-matching. Trischler et al. [130] create a NewsQA dataset by generating questions from
news headlines and summarizing them via crowdsourcing. They reduce the word overlap by annotating answers on the
main articles which are not given during question generation. Saha et al. [120] leverage pairs of plot summaries for
the same movies from Wikipedia and IMDb.45 They generate questions from the shorter plots and annotate answers
on the longer ones to obtain naturally paraphrased questions. Sen and Saffari [122] report that datasets with low
question-passage overlap will enhance the generalizability of MRC models.
Multi-sentence questions require reasoning over multiple sentences. As a result, they are more difﬁcult compared to
single-sentence questions. Joshi et al. [56] introduce TriviaQA, a dataset of questions from trivia websites. Since they
gather evidence passages from various sources (e.g., Wikipedia and the Web), multiple sentences are naturally required
for answering the given question. Khashabi et al. [60] explicitly generate multi-sentence questions on various texts
through crowdsourcing and release the MultiRC dataset. The SuperGLUE [132] benchmark adopts the MultiRC dataset
as one of its tasks.
Several MRC datasets have incorporated unanswerable questions [143, 130, 96, 113, 69]. Rajpurkar et al. [113] report
performance drop in MRC models when unanswerable questions are included in the dataset.
Compared to MRC research on English, Korean MRC research stands on a small number of existing datasets. The
primary benchmark for Korean MRC has been KorQuAD [79, 63], which adopts the same data collection process
as SQuAD 1.0 [112]. However, the model performance on KorQuAD has already exceeded human performance
in a short period, leaving little headroom for further research. Moreover, unlike SQuAD, KorQuAD is under CC
BY-ND license and does not allow derivative works (e.g., adding unanswerable questions). AI Hub MRC dataset [1]
is based on newspapers and includes unanswerable questions. However, its access is strictly limited to native Korean
researchers, prohibiting collaboration even with international researchers residing in Korea. K-QuAD [74] leverage
Google Translate46 to translate SQuAD 1.0 [112] into Korean. Since the K-QuAD dataset does not get updated over
44Twitter tagger of KoNLPy [101].
45https://www.imdb.com/
46https://translate.google.co.kr/
42

--- Page 43 ---

time, its quality depends on the machine translator’s performance at the time of release. Our KLUE-MRC is different
from the existing Korean MRC benchmarks in terms of accessibility-enhance license and more challenging difﬁculty.
3.7.5
Conclusion
We create a new challenging Korean MRC benchmark named (KLUE-MRC). In order to evaluate different aspects
of MRC capabilities, KLUE-MRC includes multi-domain passages and three types of questions: paraphrase, multi-
sentence reasoning, and unanswerable. KLUE-MRC shows improvements in question type diversity, difﬁculty, and
lexical overlap compared to existing Korean MRC datasets.
43

--- Page 44 ---

3.8
Dialogue State Tracking (DST)
Building a human-computer conversation system has been increasingly attracting attention, and a task-oriented dialogue
system is one type of the dialogue systems [14]. A core module of task-oriented dialogue systems, namely, Dialogue
State Tracking (DST) is about predicting the dialogue states from a given dialogue context. As illustrated in Table 22,
dialogue states are sets of slot and value pairs that are relevant categories (e.g. hotel type) and their possible values (e.g.
guest house, hotel, motel), respectively.
Several recent works have considered task-oriented dialogue (TOD) as an important problem of natural language
understanding. For instance, DecaNLP [85] includes a DST, which is a key component of TOD, into one of their
benchmark tasks, while DialoGLUE [88] releases the ﬁrst task-oriented dialogue benchmark containing various
sub-tasks including DST. In light of such, we include DST as a part of the KLUE benchmark.
The task of dialogue state tracking is to predict slot and value pairs after each user utterance, and the potential pairs are
predeﬁned by a task schema and knowledge base (KB), tied to the choice of a scenario. For evaluation, we use joint goal
accuracy (JGA) and slot micro F1 score. The JGA checks if all of the predicted slot-value pairs are exactly matched with
the ground-truths for every turn, while the slot micro F1 computes f1 score for each slot-value pair independently.47
Table 22: An example of dialogue state tracking in our WoS. Note that all dialogue states are cumulative in the actual
dataset and that we only track states in the user turns.
Utterances (English Translations)
Dialogue States
User: 안녕하세요. (Hello.)
-
Sys: 네. 안녕하세요. 무엇을도와드릴까요? (Hello. How can I help?)
User: 서울중앙에위치한호텔을찾고있습니다. 외국인친구도함께
갈예정이라서원활하게인터넷을사용할수있는곳이었으면좋겠어요.
(I’m looking for a hotel at the city center. I’m going with a foreign friend,
so easy access to the Internet should be available.)
Hotel-area: center
Hotel-type: hotel
Hotel-internet: yes
Sys: 네확인해보겠습니다. 혹시추가로필요하신사항이있으실까요?
(Sure, let me check. Do you need anything else?)
User: 음... 예약인원은총8명이고요. 아, 가격대는크게상관없습니다.
(Hmm.. I want to reserve for 8 people. Ah, the price range doesn’t matter.)
Hotel-area: center
Hotel-type: hotel
Hotel-internet: yes
Hotel-book people: 8
Hotel-price range: dontcare
Sys: 네, 확인감사합니다. 숙박을원하시는요일과기간같이확인부탁드립니다.
(Great, thanks for conﬁrming. Please let us know when and how long
you want to stay.)
User: 아, 중요한걸깜빡했네요. 일요일에2일간예약하고싶습니다.
(Right, I forgot an important thing. I would like to book for two days
from Sunday.)
Hotel-area: center
Hotel-type: hotel
Hotel-internet: yes
Hotel-book people: 8
Hotel-price range: dontcare
Hotel-book day: Sunday
Hotel-book stay: 2
3.8.1
Dataset Construction
Our dataset construction protocol is a modiﬁed version of the Wizard-of-Oz framework (WOZ) [59], which is a widely
used paradigm for building dialogue datasets. The WOZ setting is a particular type of human-to-human dialogue
collection, which employs two people that either takes a user and a system role. However, it is arguably time-consuming,
complex, and expensive [11]. To overcome the limitations, we adopt ‘Self-dialog’ scheme which requests a single
worker to play both user and system roles [11]. In addition, we introduce a new design choice to obtain a more precise
dialogue dataset.
Overview
We construct WoS by following ﬁve steps: 1) deﬁne a task schema, 2) create knowledge base (KB), 3)
design an annotation system, 4) collect and annotate a dataset, and 5) ﬁnalize the dataset. Different from the other
datasets in our benchmarks, WoS is not following an ordinary protocol: collecting raw corpus followed by annotating
labels. Rather, we collect dialogues (raw corpus) and their corresponding dialogue states (labels) at the same time.
1. Deﬁning Task Schema
We ﬁrst deﬁne a task schema which expresses the scenario of task-oriented dialogue. Our
task schema consists of slots across ﬁve domains (hotel, restaurant, attraction, taxi, and metro) as shown in Table 23.
47We adopt the evaluation script of https://github.com/jasonwu0731/trade-dst
44

--- Page 45 ---

Table 23: Task schema for all ﬁve domains in Wizard of Seoul (WoS) which shows names of the domain and their slots.
Star⋆, asterisk∗, cross†, doubly-crosses‡ denote required, boolean type, booking-related, and requestable after booking
slot, respectively.
Domains
Informable Slots
Requestable Slots
Hotel
name, type⋆, area⋆, price range⋆,
book day†, book stay†, book people†,
walkability∗, parking∗, internet∗,
breakfast∗, smoking∗, ﬁtness∗,
swimming pool∗, spa∗
rating, nearby station,
minutes walk from station,
address, phone number,
business hour, reference number‡
Restaurant
name, type⋆, area⋆, price range⋆,
book day†, book time†, book people†,
alcohol∗, walkability∗, parking∗,
internet∗, smoking∗, outdoor table∗
rating, nearby station,
minutes walk from station,
address, phone number,
business hour, last order time,
representative menu, reference number‡
Attraction
name, type⋆, area⋆,
walkability∗, parking∗, heritage∗,
educational∗, scenic∗, cultural∗
rating, nearby station,
minutes walk from station,
address, phone number,
business hour, entrance fee
Taxi
leave at⋆, departure⋆,
arrive by, destination⋆, type
phone number, cost, duration
Metro
leave at, departure⋆, destination⋆
departure line, destination line,
arrive by, cost, duration,
transfer, optimal path
Typically, slots are categorized into informable slots and requestable slots. The informable slots cover properties which
can constrain a user goal48 such as “price range”, “area”, and “booking day”. The requestable slots provide additional
information that a user may ask, but not necessarily need to be speciﬁed as a user goal constraint. A typical example
of a requestable slot is “phone number”, which a user may ask for, but would not work to narrow down the probable
candidates of the goal [50, 51].
Based on this schema, we include additional attributes to the informable and requestable slots to provide an easy-to-
operate annotation system and easy-to-follow guidelines. A slot could have one or more attributes among whether it
is 1) boolean type, 2) required or not (Required), 3) related to booking (Booking-related), and 4) only available after
booking is conﬁrmed (Requestable after booking. e.g., reference number). The boolean type slots can have either yes
or no as their values, such as “Parking (availability)” and “(has) swimming pool”. Such boolean type values do not
appear in the dialogue context explicitly. In other words, they have abstractive properties. A model which understands
abstractive properties is desirable, so we have much more boolean type slots than MultiWOZ [10]; WoS has 20 boolean
slots across the domains while MultiWOZ includes only 2. Meanwhile, the required slots have to be speciﬁed with
values in order to ﬁll out a user intent. This helps us to simulate an actual service scenario in which an agent is not
allowed to take the next steps without specifying required values [114].
2. Creating Knowledge Base
We construct a knowledge base (KB) based on the task schema of each domain to
obtain a set of predeﬁned realization candidates of a user’s goal. For the hotel and restaurant domains, we manually
create virtual instances, whereas for the attraction and metro domains, we leverage real names (e.g. Gangnam Station or
Namsan Tower) collected from the web. On the other hand, for the taxi domain, we do not deﬁne instances in advance,
but dynamically generate the instances during the dialogue collection as in MultiWOZ [10]. With ethical considerations
in mind, any personally identiﬁable information (PII, e.g., phone number, address) is replaced with randomly generated
instances using faker.49 Table 25 shows the KB statistics for each domain.
3. Designing the Annotation System
In this section, we describe the annotation platform we used for collecting data
from both the User-side and System-side.
48A user goal is what the worker playing user should follow as shown in Table 24.
49https://faker.readthedocs.io
45

--- Page 46 ---

Table 24: An example of goal instruction. Unlike MultiWOZ, we present all instructions from the beginning to prevent
ordering bias as in CoCo [77]. The booking-related slots, “restaurant-book time (22:41)” and “restaurant-book day
(Wednesday)” appear before a conﬁrmation of KB entity.
Korean
English (Translated)
당신은오늘22:41에서울중앙에서식사할계획을
가지고있습니다. 아참오늘은수요일입니다. 그
런곳을찾았다면먼저대표메뉴를확인하세요. 그
리고나선1명으로예약거세요. 예약이후엔영업
시간을문의하시구요. 그리고나선식당근처에서
잘곳을찾아야합니다. 그곳은반드시흡연이불
가해야합니다. 찾았다면같은요일에예약하세요.
같은인원으로4일간머물러야합니다. 예약에성
공했다면예약번호를묻고, 흡연가능유무를더블
체크하세요. 그런다음마지막으로택시를하나부
르세요. 식당에서숙소로향해야합니다. 찾았다면
소요시간을문의하세요.
You have a plan to eat in the center of Seoul at 22:41
today. Oh, today is Wednesday. If you ﬁnd such a
place, ﬁrst check the representative menu. Then,
make a booking for 1 person. After booking, inquire
about the business hour. Then, you have to ﬁnd a
hotel to sleep in near the restaurant. The restaurant
must be non-smoking. If you ﬁnd it, book on the
same day. You must stay for 4 days as the same
number of people. If the booking is done, ask for the
reference number and double-check the smoking
allowed. Then, ﬁnally, call a taxi. You have to go to
the hotel from the restaurant. If you call the taxi,
inquire about the duration.
Table 25: Statistics of Knowledge Base in WoS.
Domain
# Instances
# Slots
Hotel
101
19
Restaurant
56
20
Attraction
100
17
Taxi
-
8
Metro
3,306
10
3.1. User Side
We provide a goal instruction for a user side role. The instruction includes descriptions of a user’s
speciﬁc goal with corresponding slot values in natural language. It also contains the user’s context including persona for
variety of dialogues. A user is asked to generate utterances following the instruction. An example is shown Table 24.
To devise a multi-domain dialogue scenario where slots are shared across multiple domains, we include domain
transition in the instruction [10, 154]. For example, in case of a user aiming to book a hotel, the user might seek
information about transportation (taxi, metro, etc.) to get there. In this dialogue, initial domain is changed to another
(hotel to taxi/metro). It is more challenging compared with single domain in terms of dialogue state tracking. Because
user could express their goal implicitly where values should be inferred by co-referencing other values of preceding
domains.
The goal instructions are realized by the templates containing placeholders for goal constraining slots and their values.
We design diverse templates for each domain, in order to cover various scenarios of the dialogues. Like MultiWOZ, the
goal templates include a series of subgoals with corresponding slots. We carefully design the sentences to promote
lexical entailment or co-referencing during conversation, which can be naturally observed in the user context or during
the domain transition. When ﬁlling a template to complete instructions, we randomly assign the instances from KB built
upon the domain-speciﬁc task schema to the given placeholders. The values of the instruction should be speciﬁcally
mentioned by a user during a conversation. Each trackable slot either has valid values, None or Dontcare.50
To properly evaluate a model’s generalization ability, we further add counterfactual goals and introduce unseen KB
instances during the process [77]. To add new goal instruction based on the current slot distribution, we keep monitoring
the slot value frequency and co-occurrence over slots during the construction. Speciﬁcally, we add new goal instructions
which cover infrequent slot values or rarely co-occurring combination among slots. For example, when “(hotel-parking,
no)” is infrequent pair in the as-is distribution, we promote it to appear in dialogues by designing goal instruction
including it as constraint. Moreover, we differentiate KB instances between particular subset of dataset (train and
dev/test set) to simulate realistic scenario regarding unseen slot values in the test time.
3.2. System Side
The role of a system side worker (wizard) is to 1) annotate dialogue states of user utterances while
2) generate responses by accessing to the KB if necessary, for every turn. First, the wizard is asked to ﬁll in appropriate
slot values inferred from the current dialogue context. If the word uttered by the user is not clear to directly map to a
50Dontcare means a user has no preference and None means a user is yet to specify a valid value for given slot [50, 51].
46

--- Page 47 ---

Figure 7: Graphical web interface for system side worker.
speciﬁc slot value, the wizard should clarify the meaning of the word ﬁrst and then ﬁll the slot when the word has the
same meaning as the value. The annotation of a dialogue state is an explicit action of understanding a user request to
fully focus on providing the required information. Then, the wizard generates response either to request or to convey
information. If the values of required slots are absent, the system side worker is allowed to ask for the missing values to
the user. Otherwise, the system provides the user with the adequate information. We enable the system to query the
external knowledge base, if needed. When there are more than three search results, the system worker could request
more details or recommend one among them.
To support the wizard to perform such complicate work effectively and efﬁciently, we provide a graphical web interface
with a newly introduced feature: dropdown components (Figure 3.8.1). Dropdown interface enables the system side
worker can choose a value from a list of pre-populated candidates. We present most probable value candidates based
on the goal instruction and domain-speciﬁc knowledge base, since a dropdown might become worthless when too
many options are presented to workers. This procedure naturally prevents several type of annotation errors, such as
multi-annotations, mis-annotations, typos, and value canonicalization reported in MutiWOZ 2.1 [37].
4. Dataset Construction
We adapt ‘Self-dialog’ scheme inspired by taskmaster-1 [11] to efﬁciently collect diverse
dialogue dataset while reducing the cost and time. Self-dialog is effective to collect various dialogue data. By having
both roles, a worker freely controls a ﬂow of dialogue such as the order of slot occurrence in user utterances and
recommendation of system responses. This also leads workers to speak their own styles naturally such that different
personas are included. However, we found annotation errors in pilot phase such as early-markup (system pre-ﬁlls the
values before receiving the values from the user) and delayed-markup (the system ﬁlls the values behindhand the proper
turn) errors. We further improve the scheme by utilizing explicit turn-switching between user and system roles with
providing error correction interface.
To elaborate, we train and select trustworthy workers to participate in the main collection process. Prior to the main
phase, we conduct several pilot studies with crowdworkers to avoid aforementioned early-markups and delayed-markup
errors, and to generate more realistic dialogues including some miscommunications. We also implement an explicit
turn-switching between the two roles, in order to immerse themselves in a user/system role, which mitigates overly
reduced miscommunications as well. Throughout the pilot, we ﬁnally employ 15 selected workers who can effectively
handle such issues.
47

--- Page 48 ---

Table 26: Statistics of Wizard-of-Seoul (WoS).
|Train|
|Dev|
|Test|
Total
# Dialogues
8,000
1,000
1,000
10,000
# Single Domain Dialogues
1,806
263
226
2,295
# Multi Domain Dialogues
6,194
737
774
7,705
# Counterfactual Dialogues
0
294
361
655
# Total Turns
117,584
14,448
14,660
146,692
# Total Tokens
899,450
114,169
114,914
1,128,533
Avg Turns per Dialogue
14.70
14.45
14.66
14.67
Avg Tokens per Turn
7.65
7.90
7.84
7.69
Table 27: Comparison regarding data split strategy. Random is splitting train, dev and test set randomly. The CF-goal
indicates they are included in dev and test set with unseen KB instances.
Domain Split
Joint Goal Accuracy
Random
57.53
CF-goal
47.38
Final Dataset
Table 26 shows statistics of our dataset. WoS contains overall 10,000 dialogues with 146,692 turns
across 5 domains. The evaluation (dev/test) set speciﬁcally includes dialogues with counterfactual goals and unseen KB
instances against train set. The dev/test set contains 294 and 361 counterfactual goal-based dialogues, respectively. All
the splits contain sufﬁcient number of dialogues with domain transition.
3.8.2
Evaluation Metrics
For evaluation metrics for WoS is 1) joint goal accuracy (JGA) and 2) slot micro F1 score. JGA measures the proportion
of exactly matched dialogue state which consists of a set of slot-value pairs with the ground truth dialogue state among
the total number of dialogue turns. Slot micro F1 score is an average of micro F1 scores in each turn. For each turn,
micro F1 score is deﬁned as the harmonic mean of precision and recall in terms of predicted slot-value pairs and
ground-truth pairs. Note that the slot micro F1 score ignores when value of the ground truth is “None”.
3.8.3
Analysis
When splitting the train and dev/test set based on the counterfactual goals and unseen KB instances, like Li et al. [77],
we observe performance drop as shown in Table 27. This demonstrates that the counterfactual goal makes WoS more
challenging.
3.8.4
Related Work
Wizard-of-Oz (WOZ) [59] is a popular scheme in dialogue collection. In fact, conventional WOZ setting allows
to collect various type of dialogues by employing role-playing of two humans. Each human should choose a role
between the two: user and system. As taking a role, dialogues are collected by turn-taking generation of utterances with
background information provided in advance. In the case of building a task-oriented dialogue, goal is given to a user
while knowledge base is allowed to be accessed to system. The system can use its knowledge base when responding to
user’s request.
Many dialogue datasets closely follow WOZ settings [135, 35, 36], however, it costs a lot of time and money because
two crowdworkers must be matched at the same time and successfully play each role, which prevents collecting
dialogues at scale. We refer this limitation to ‘worker coexistence constraints’. To overcome the limitation, MultiWOZ
[10] slightly change this conventional WOZ to asynchronously collect dialogues turn-by-turn from crowdworkers,
which allows different workers to play the same user or system in a single dialogue. This approach costs less but
error-prone because every worker must adapt to dialogue already progressed so that their response might be incoherent
to the previous context [37]. Recently, CrossWOZ and RiSAWOZ thus pair only selected trustworthy workers to collect
dialogues in synchronous manner as suggested in the WOZ settings to keep the annotation quality despite the high
construction cost [154, 109].
48

--- Page 49 ---

Byrne et al. [11] also argue that conventional WOZ settings are time consuming, complex and expensive, requiring
considerable technical implementation as well as administrative procedures to train and manage both agents and
crowdsourced workers, accordingly suggesting Self-dialog as an alternative. Self-dialog is a collection scheme in
which workers write the entire dialogue playing both user and system roles. To demonstrate their idea, Byrne et al.
[11] build a large-scale dialogue datase, Taskmaster-1, which is built upon the Self-dialog which stands on the WOZ
schemes: 1) two people playing user and system roles (conventional WOZ setting) and 2) one person playing both roles
(Self-dialog). As a result, Self-dialog can remedy the cost of ‘worker coexistence constraint’ effectively with avoiding
incoherent dialogue generation caused by asynchronous dialogue collection. However, there is a tendency that little
miscommunication occurs in the dialogue which compared to the real world conversations because the same person
produces utterances in both roles, which might lead to a gap from reality.
Some researchers further tries to employ only machines to create such dialogues to maximize cost-efﬁciency. It builds
the dialogues on top of a simulator which is able to create utterances by turn automatically from elaborately designed
rules and given task schema. The simulator ﬁrst generates psuedo-dialogue, then adopts crowdsourcing to paraphrase
them to the natural utterances [124, 114]. It requires much less human effort, however, heavily relies on the simulator.
Meanwhile, previous works exists addressing robust evaluation of DST models. According to CoCo [77], state-of-the-
art DST models are not robust to realistic scenarios since they scarcely appear in the train data. As the name CoCo
(controllable counterfactuals) suggests, it generates infrequent but realistic dialogues based on the predeﬁned slot-value
pairs. They show that even a state-of-the-art DST model’s performance drops signiﬁcantly when they are evaluated on
such dialogues including counterfactual goals. It means the current TOD benchmarks should be improved in terms of
robustness to unseen but realistic scenarios.
As for Korean, there is a task-oriented dialog dataset is provided by National Information Society Agency (NIA). It
covers about 10 domains related to the civil complaints and consists of more than 500k dialogues. The utterances are
divided into four types: 1) a main question that a user asks, 2) a sub question that a system could ask for clariﬁcation,
3) a user answer, and 4) a system answer. Additionally, user intents are annotated and entities are extracted from
each utterance. We ﬁnd that this dataset does not follow any of the aforementioned settings; there is no dialogue state
represented as slot-value pairs, only regarding single turn judgement. It also lacks information about task schema and
redistribution is restricted which does not satisfy our accessibility principle, which motivates us to newly create a DST
benchmark.
3.8.5
Conclusion
We introduce Wizard-of-Seoul (WoS), the ﬁrst large-scale Korean multi-domain task-oriented dialogue dataset that
simulates conversations between Seoul tourists and travel agents. We adapt ‘Self-dialog’ for efﬁciently scaling up of
dialogue collection scheme. In addition, consideration on annotation interfaces (drop-down menu and turn-switching)
mitigates erroneous cases and diverse goal instructions including counterfactual ones promote each conversation to be
more natural and challenging. We hope that WoS sparks various future dialogue research in Korean and also offers
valuable insights to pushing forward end-to-end dialogue modeling.
49

--- Page 50 ---

4
Pretrained Language Models
In order to facilitate further research using KLUE, we provide strong baselines for all the benchmark tasks within it. As
a part of this effort, we pretrain and release large-scale language models for Korean, which we hope would reduce the
burden of retraining large-scale language models from individual researchers. More speciﬁcally, We pretrain language
models (PLM), including BERT [30] and RoBERTa [82], from scratch.
4.1
Language Models
We pretrain multiple Korean language models while varying training conﬁguration. This enables us to explore effective
settings for pretraining Korean models and further establish simple yet effective baseline models for KLUE. We train
KLUE-BERT and KLUE-RoBERTa. We vary the choice of a pretraining corpus, preprocessing procedure, tokenization
strategy, and other training conﬁgurations.
Table 28: Statistics of the pretraining corpus.
MODU
CC-100-Kor
NAMUWIKI
NEWSCRAWL
PETITION
Total
# Sentences
167M
103M
14M
183M
5.2M
473M
# Words
1,892,814,395
1,593,887,022
265,203,602
2,716,968,038
50,631,183
6,519,504,240
size (GB)
18.27
15.46
2.52
25.87
0.53
62.65
Pretraining Corpora
We gather the following ﬁve publicly available Korean corpora from diverse sources to cover a
broad set of topics and many different styles. We combine these corpora to build the ﬁnal pretraining corpus of size
approximately 62GB. See Table 28 for overall statistics:
• MODU : Modu51 Corpus [98] is a collection of Korean corpora distributed by National Institute of Korean Lan-
guages.52 It includes both formal articles (news and books) and colloquial text (dialogues).
• CC-100-Kor : CC-10053 is the large-scale multilingual web crawled corpora by using CC-Net [136]. This is used for
training XLM-R [26]. We use the Korean portion from this corpora.
• NAMUWIKI : NAMUWIKI is a Korean web-based encyclopedia, similar to Wikipedia, but known to be less formal.
Speciﬁcally, we download the dump created on March 2nd, 2020.54
• NEWSCRAWL : NEWSCRAWL consists of 12,800,000 news articles published from 2011 to 2020, collected from
a news aggregation platform.
• PETITION : Petition is a collection of public petitions posted to the Blue House asking for administrative actions on
social issues. We use the articles in the Blue House National Petition55 published from August 2017 to March 2019.56
Preprocessing
We ﬁlter noisy text and non-Korean text using the same methods from Section 2.3. Each document in
the corpus is split into sentences using C++ implementation (v1.3.1.) of rule-based Korean Sentence Splitter (KSS).57
For CC-100-Kor and NEWSCRAWL, we keep sentences of length greater than equal to 200 characters, as a heuristics
to keep well-formed sentences. We then remove sentences included in our benchmark task datasets, using BM25 as a
sentence similarity metric [118].
Ethical Considerations
Because we collect and use as much publicly available data as possible for pretraining, these
corpora often contain undesirable social biases. Furthermore, we noticed earlier quite a bit of PII in these corpora,
although they were all publicly available. Both of these are problematic. Social biases in the corpus may result in a
language model that learns such biases. PII in the corpus may be memorized by a language model and can subsequently
be retrieved by adversarial attacks [12].
51A transliteration of a Korean word ‘모두’ which means ‘Everyone’.
52https://corpus.korean.go.kr/
53http://data.statmt.org/cc-100/
54http://dump.thewiki.kr
55https://www1.president.go.kr/petitions
56https://ko-nlp.github.io/Korpora/en-docs/corpuslist/korean_petitions.html
57https://github.com/likejazz/korean-sentence-splitter
50

--- Page 51 ---

Table 29: Our pseudonymization methods and examples. The examples are from faker library documentation or the
public.
Private Information
Pseudonymization
Pseudonymised Example
Telephone Number
Faker
055-604-8764
Social Security Number
Faker
600408-2764759
Foreign Registration Number
Faker
110527-1815659
Email Address
Faker
agweon@example.org
IP Address
Faker
166.186.169.69
MAC Address
Faker
c5:d7:14:84:f8:cf
Mention(@)
Faker
@gildong
Address
Random Number Generation
경상북도성남시서초대64가
Bank Account Number
Random Number Generation
110-245-124678
Passport Number
Random Generation
M123A4567
Driver’s License
Random Number Generation
11-17-174133-01
Business Registration Number
Random Number Generation
123-45-67890
Health Insurance Information
Random Number Generation
1-2345678901
Credit or Debit Card Number
Random Number Generation
1234-5678-9012-3456
Vehicle Registration Place
Random Generation
55구1601
Homepage URL
Random Generation
www.example.com
We do not ﬁlter out socially biased contents nor hate speech for three reasons. First, manual inspection is infeasible
for this large-scale pretraining corpora. Second, it is a challenging problem on its own to automatically detect socially
biased contents or hate space, as both of these highly depend on the context in which they appear [62]. Lastly, being
blind to such harmful contents prevents the future use of a language model for detecting and correcting these harmful
contents, such as using it as an anti-expert [81]. We expect future research on the pretrained language models we release
to focus on how to detect and correct biases encoded in these models and on how to debias them, as has been recently
demonstrated by Cheng et al. [15].
In contrast, we pseudonymize PII in our corpora as much as possible. We detect 16 personal data types using regular
expressions based on the guideline from the Korea Internet and Security Agency (KISA).58 It is relatively easy to
pseudonymize PII while keeping linguistic patterns, since the selected PII has standardized pattern. We then replace
the original information, using either the faker library59 or random generation based on the pattern. As a result, we
pseudonymize 1.2% of the pretraining corpora. Details are illustrated in Table 29.
Tokenization
We design and use a new tokenization method, morpheme-based subword tokenization. When building
a vocabulary, we pre-tokenize a raw text into morphemes using a morphological analyzer, and then we apply byte
pair encoding (BPE) [123] to get the ﬁnal vocabulary. For morpheme segmentation, we use Mecab-ko,60 MeCab [68]
adapted for Korean, and for BPE segmentation, we use the wordpiece tokenizer from Huggingface Tokenizers
library.61 We specify the vocabulary size to 32k. After building the vocabulary, we only use the BPE model during
inference, which allows us to tokenize a word sequence by reﬂecting morphemes without a morphological analyzer.
This improves both usability and speed. Examples are presented in Table 30.
The motivation behind this method is that Korean is an agglutinative language, which is to say, a word is a constitution
of morphemes - stems and afﬁxes. The morphemes tend to remain unchange on different unions, and the boundary is
generally clear. Although BPE has been widely used across many languages due to its effectiveness, it struggles to
identify morphemes correctly as demonstrated in Table 30.
58https://www.kisa.or.kr/public/laws/laws2_View.jsp?cPage=1&mode=view&p_No=282&b_No=282&d_No=3
59https://github.com/joke2k/faker
60https://bitbucket.org/eunjeon/mecab-ko
61https://github.com/huggingface/tokenizers
51

--- Page 52 ---

Table 30: An input text “조경현은인공지능분야의저명한연구자이다. (Kyunghyun Cho is a prominent AI re-
searcher.)” is segmented with various tokenization strategies. We denote slash (/) as a token separator. The mBERT
tokenizer [30] splits the input text into nearly in characters resulting in a longer sequence than monolingual tokenizers.
BPE tokenizer generates tokens spanning multiple morphemes (##현은, ##명한). Morpheme-based subword tokenizer,
on the other hand, better splits text into morphemes (##은, ##의).
Tokenization
Tokenized Sequence
Raw Text
조경현은인공지능분야의저명한연구자이다.
BPE (Multilingual)
조/ ##경/ ##현/ ##은/ 인/ ##공/ ##지/ ##능/ 분/ ##야/ ##의/ 저/ ##명한/ 연구/ ##자/ ##이다/ .
BPE
조경/ ##현은/ 인공지능/ 분야의/ 저/ ##명한/ 연구/ ##자이/ ##다/ .
Morpheme
조경현/ 은/ 인공지능/ 분야/ 의/ 저명/ 한/ 연구자/ 이/ 다/ .
Morpheme-based Subword
조경/ ##현/ ##은/ 인공지능/ 분야/ ##의/ 저명/ ##한/ 연구자/ ##이다/ .
Table 31: Implementation details of KLUE-BERT and KLUE-RoBERTa. WWM refers to the whole word masking
strategy.
Model
# Parameter
Masking
Training Steps
Batch Size
Learning Rate
Device
KLUE-BERTBASE
110M
Static, WWM
1M
256
10−4
TPU v3-8
KLUE-RoBERTaSMALL
68M
Dynamic, WWM
1M
2048
10−4
8× V100 GPUs
KLUE-RoBERTaBASE
110M
Dynamic, WWM
1M
2048
10−4
8× V100 GPUs
KLUE-RoBERTaLARGE
337M
Dynamic, WWM
500k
2048
10−4
8× V100 GPUs
Training Conﬁgurations
We choose BERT [30] and RoBERTa [82] architectures for our language models. Table 31
describes the implementation details. All models take sequences of at most 512 tokens long each and are pretrained
with a static or dynamic masking strategy following the original training procedure. When masking tokens, we use
whole word masking (WWM) which masks all of the the tokens that form a single word. BERT also performs next
sentence prediction (NSP). Other hyperparameters not speciﬁed in Table 31 nor in the pretraining procedure details are
same as the original conﬁgurations from [30, 82]. Due to the resource constraints, we could increase batch size only
up to 2,048, unlike Liu et al. [82] who use the batch size of 8k. We decrease the learning rate accordingly. We ﬁx the
learning rate to 10−4 for both BERT and RoBERTa.
4.2
Existing Language Models
In addition to our own language models, we evaluate the following two existing multilingual language models and two
Korean monolingual language models on our benchmark:
• mBERT [30] : A multilingual BERT introduced and released by Devlin et al. [30]. It is trained with the MLM and
NSP objectives on a multilingual corpus covering 104 languages including Korean.
• XLM-R [26] : A RoBERTa [82] trained on a large multilingual corpus by using the MLM objective.
• KR-BERT [75] : An open-sourced character-level Korean language model based on BERT. We use the KR-BERT
character WordPiece which uses a vocabulary of 16,424 unique tokens.
• KoELECTRA [102] : An open-source Korean language model trained with the MLM and replaced token detection
objectives, as was done by Clark et al. [22]. For training corpora, Park [102] uses own crawled news data and MODU
corpus [98].
5
Fine-tuning Language Models
5.1
Task-Speciﬁc Architectures
8 main tasks of KLUE benchmark can be categorized into 4 types based on the ﬁne-tuning strategy. Topic classiﬁcation
(TC) and relation extraction (RE) are single sentence classiﬁcation tasks. Sentence textual similarity (STS) and natural
language inference (NLI) are sentence pair classiﬁcation / regression tasks. Dialogue state tracking (DST) is a multiple-
sentence slot-value prediction task. Finally, named entity recognition (NER), dependency parsing (DP) and machine
reading comprehension (MRC) are sequence tagging tasks.
We use xi to refer to the i-th token of input and hi ∈RH to its corresponding ﬁnal hidden state from a pretrained
language models (PLM), where H is the hidden dimensionality. Following the conventional ﬁne-tuning setup [30], we
52

--- Page 53 ---

Figure 8: A baseline architecture for WoS based on TRADE [140].
use [CLS] as the ﬁrst input token x0 and [SEP] as a delimiter token to separate inputs (e.g., two sentences in STS and
NLI, a passage and a question in the case of MRC, and dialogue turns for DST.)
5.1.1
Single Sentence Classiﬁcation
In the single sentence classiﬁcation task, such as TC and RE, a classiﬁer classiﬁes a single sentence into a set of
predeﬁned labels. Following the convention, the last hidden state of [CLS] token h0 is linearly mapped to the number
of labels (K) with W ∈RK×H and the entire model is trained to minimize the cross entropy loss.
YNAT is a single sentence classiﬁcation task where K is 7 for predeﬁned topic labels, and does not require any special
treatment of each input. KLUE-RE on the other hand requires a special procedure to indicate entities within the input
sentence. We use <subj>, </subj>, <obj>, and </obj> to mark the beginnings and the ends of subject and object
entities, respectively, following Baldini Soares et al. [5]. We expand the embedding matrix to add these four extra
tokens.
5.1.2
Sentence Pair Classiﬁcation / Regression
In the sentence pair classiﬁcation / regression task, a model is asked to determine the relationship between two sentences.
A pair of input sentences are concatenated with a special separator token, often [SEP], in-between.
In KLUE-STS, each sentence pair is annotated with a real-valued similarity [0, 5]. The model is thus trained to map
from the ﬁnal hidden state of [CLS] to a real number, by minimizing the mean squared error (MSE). In the case of
KLUE-NLI, each sentence pair, consisting of a premise and hypothesis, is coupled with one of three classes. The
model thus maps the hidden state of [CLS] token to a three-dimensional real-valued vectors and is trained to minimize
the cross-entropy loss.
5.1.3
Multiple-Sentence Slot-Value Prediction
WoS is a slot-value prediction task for a given dialogue context, where the prediction should be considered across
multiple turns instead of a single utterance. We employ an encoder-decoder model following the architecture of
TRADE [140], which consists of an utterance encoder, a state generator, and a slot gate classiﬁer (Figure 5.1.3). In our
implementation, we change the utterance encoder from GRU [17] to PLM to get better representations. Thus, the state
generator takes the ﬁnal hidden state of [CLS] token h0 as the ﬁrst decoder hidden state. We also modify the slot gate
classiﬁer to predict additional two slot gate labels (yes, no), since WoS contains relatively more Boolean type slots than
MultiWOZ [10]. We jointly minimize the cross-entropy loss of the state generator and slot gate classiﬁer.
53

--- Page 54 ---

Figure 9: An input and label example of KLUE-NER. We realign original character-level label sequence of Figure 3 for
tokens from our Morpheme-based subword tokenization.
Figure 10: An overview of KLUE-DP baseline model architecture, which we take advantage of Fernández-González
and Gómez-Rodríguez [39].
5.1.4
Sequence Tagging
KLUE-NER is a token-level tagging task, where each character is assigned a label. This requires a care in using
tokenization, as the labels from the characters within each subword token must be aggregated, and the predicted label
of each subword token must be properly distributed across the characters within it. See Figure 9 for an example. We
linearly map each of the ﬁnal hidden states from the encoder h ∈R|x|×H into a 12-dimensional real-valued vectors,
corresponding to the 12 named-entity categories. We then minimize the cross-entropy loss summed over all the tokens.
KLUE-MRC is a span prediction task in which a model tags the beginning and end tokens of the answer span within a
passage, given a question. The input to the model is the concatenation of a tokenized passage and an associated question
(separated by [SEP]). The ﬁnal hidden state of each token in the passage is linearly projected to a 2-dimensional
real-valued vector. The dimensions in this vector correspond to the logits of two binary classiﬁers, the start and end
token classiﬁers. The special token [CLS] is considered as both the correct start and end tokens, when given question is
unanswerable. We minimize the cross-entropy loss to train the model.
We frame KLUE-DP as a sequence tagging problem. Each token within an input sentence is tagged twice, once with its
head token and the other with the type of the arc connecting the head and the current token. Our baseline architecture
follows the model proposed by Fernández-González and Gómez-Rodríguez [39], except word representation and
attention mechanisms. Similarly to KLUE-NER, we must be careful in handling subword tokens, as the annotation
is done at the word level. In our approach, we use a pretrained language model (to be ﬁne-tuned) to extract subword
representations and concatenate the ﬁrst and last subword token representations of each word, to form word vector
representations. Each of these word representations is optionally concatenated with the part-of-speech embedding. For
the attention layers, we use biafﬁne attention [33] to predict HEAD, and bilinear attention [64] to predict arc type
(DEPREL) for each word. Just like KLUE-NER and KLUE-MRC, we minimize the cross-entropy loss to ﬁne-tune the
entire model. See Figure 10 for a graphical illustration of the model architecture.
54

--- Page 55 ---

Table 32: Evaluation results of our pretrained LMs and other baselines on KLUE benchmark. The F1 refers to a macro-F1
score. The F1E and F1C of KLUE-NER indicates entity-level and character-level macro-F1 score, respectively. The
F1mic of KLUE-RE is micro-averaged F1 score ignoring the no_relation. The F1S of WoS is an average of slot-value
pair level micro-F1 scores. The RP of KLUE-STS denotes Pearson correlation. Bold shows the best performance across
the models, and underline indicates the best performance among BASE models.
YNAT
KLUE-STS
KLUE-NLI
KLUE-NER
KLUE-RE
KLUE-DP
KLUE-MRC
WoS
Model
F1
RP
F1
ACC
F1E
F1C
F1mic
AUC
UAS
LAS
EM
ROUGE
JGA
F1S
mBERTBASE
81.55
84.66
76.00
73.20
76.50
89.23
57.88
53.82
90.30
86.66
44.66
55.92
35.46
88.63
XLM-RBASE
83.52
89.16
82.01
77.33
80.37
92.12
57.46
54.98
89.20
87.69
27.48
53.93
39.82
89.61
XLM-RLARGE
86.06
92.97
85.86
85.93
82.27
93.22
58.39
61.15
92.71
88.70
35.99
66.77
41.20
89.80
KR-BERTBASE
84.58
88.61
81.07
77.17
74.58
90.13
62.74
60.94
89.92
87.48
48.28
58.54
45.33
90.70
KoELECTRABASE
84.59
92.46
84.84
85.63
86.11
92.56
62.85
58.94
92.90
87.77
59.82
66.05
41.58
89.60
KLUE-BERTBASE
85.73
90.85
82.84
81.63
83.97
91.39
66.44
66.17
89.96
88.05
62.32
68.51
46.64
91.61
KLUE-RoBERTaSMALL
84.98
91.54
85.16
79.33
83.65
91.14
60.89
58.96
90.04
88.14
57.32
62.70
46.62
91.44
KLUE-RoBERTaBASE
85.07
92.50
85.40
84.83
84.60
91.44
67.65
68.55
93.04
88.32
68.67
73.98
47.49
91.64
KLUE-RoBERTaLARGE
85.69
93.35
86.63
89.17
85.00
91.86
71.13
72.98
93.48
88.36
75.58
80.59
50.22
92.23
5.2
Fine-Tuning Conﬁgurations
For all the experiments, we use Huggingface Transformers [139] and PyTorch-Lightning.62 We use AdamW
optimizer [83] with the learning rate selected from {10−5, 2 × 10−5, 3 × 10−5, 5 × 10−5}, the warm-up ratio from
{0., 0.1, 0.2, 0.6} and the weight decay coefﬁcient from {0.0, 0.01}. We choose the batch size from {8, 16, 32} and the
number of epochs from {3, 4, 5, 10}. We use the maximum sequence length of 512 for KLUE-MRC and WoS, and 128
for all the other tasks. We report the score obtained from the best hyperparameter conﬁguration based on the dev set
performance.
5.3
Evaluation Results
In this section, we present the evaluation results including our KLUE-PLMs and existing PLMs on the KLUE benchmark,
in Table 32.63 Different from other NLU benchmarks, we do not average the scores over tasks, since simple averaging
of scores of different scales and interpretations could be highly misleading. Rather, we describe and discuss the
result of each task separately. Within the Korean BASE models, KLUE-BERTBASE performs best for YNAT and WoS,
KLUE-RoBERTaBASE for KLUE-RE and KLUE-MRC, and KoELECTRABASE for KLUE-STS and KLUE-NLI.
We make two major observations. First, we see that KLUE-RoBERTaLARGE, which is the largest model among the
baseline PLM’s we tested, outperforms all the other models across all the tasks except for KLUE-NER. This observation
agrees well with the recent trend which has demonstrated the correlation between the model size and task performance
[58, 9]. This indicates that KLUE will be useful for the future investigation into how much gain we can expect
by simply increasing the model size further. The second observation is that the monolingual models, which were
speciﬁcally designed for and trained with a more carefully curated corpus in the target language (Korean), generally
outperform the multilingual counterparts, especially when we compare models of similar sizes. We make this observation
again across all the tasks, except for KLUE-NER, where the XLM-RLARGE performs similarly to the best performer,
KoELECTRABASE, in terms of character-level F1 score. This observation re-iterates the importance of investing effort
in understanding a target language and customizing data, models and learning algorithms for the target language.
5.4
Analysis of Models
There were two major decisions we made in preparing the pretraining corpus and preprocessing data. They were 1)
whether to pseudonymize PIIs and 2) the tokenzation strategy. In this section, we analyze the impact of our choices,
using KLUE-RoBERTaBASE by training it on the MODU corpus only.
Corpus Pseudonymization
It can be expected that noise introduced in the process of pseudonymization may have
detrimental effect on the downstream task performance. Our ﬁnding, presented in Table 33, however shows that
there is some drop in a subset of the tasks, but such drop is quite minimal. This suggests that the minimal level of
pseudonymization, just like what we have done, is already a good way to balance the task performance and the risk of
leaking private information.
62https://github.com/PyTorchLightning/pytorch-lightning
63See Appendix A for the corresponding table however computed on the development set.
55

--- Page 56 ---

Table 33: Evaluation results according to whether the corpus pseudonymization is conducted in the preprocessing step.
YNAT
KLUE-STS
KLUE-NLI
KLUE-NER
KLUE-RE
KLUE-DP
KLUE-MRC
WoS
Pretraining Corpus
F1
RP
F1
ACC
F1E
F1C
F1mic
AUC
UAS
LAS
EM
ROUGE
JGA
F1S
Original
83.40
92.06
84.70
81.60
84.84
91.03
65.25
64.79
92.17
88.34
62.13
67.46
47.14
91.60
Pseudonymized
83.39
91.11
82.85
78.50
84.99
91.22
62.79
62.96
92.02
88.02
62.88
67.58
46.21
91.23
Table 34: Comparison our tokenization strategy with other baselines.
YNAT
KLUE-STS
KLUE-NLI
KLUE-NER
KLUE-RE
KLUE-DP
KLUE-MRC
WoS
Tokenization
F1
RP
F1
ACC
F1E
F1C
F1mic
AUC
UAS
LAS
EM
ROUGE
JGA
F1S
BPE
83.40
91.91
85.19
82.07
68.75
89.47
64.39
65.04
89.89
89.47
51.12
65.79
21.38
77.68
Morpheme-based Subword
83.40
92.06
84.70
81.60
84.84
91.03
65.25
64.79
92.17
88.34
62.13
67.46
47.14
91.60
Tokenization Strategy
We contrast our tokenization scheme, morpheme-based subword tokenization, against the
standard byte pair encoding (BPE). First, we investigate the difference in how words are segmented into subword
tokens. Following Rust et al. [119], we consider subword fertility, proportion of continued words, and UNK ratio. On
the subword fertility, which measures the average number of subwords produced per word, the proposed tokenization
scheme ends up slightly higher than BPE does. However, when we look at the proportion of continued words, which
measures the number of words that were split into at least two subwords, we observe the opposite trend. This implies
that our algorithm maintains the original words as much as it can, and only when it is necessary, it splits each word into
potentially more subword pieces. The efﬁcacy of the proposed scheme over BPE is evident from the UNK ratio, as it
produces fewer UNK tokens compared to BPE when the vocabulary size was controlled to be 32k for both methods. See
Table 35.
Table 35: Overview of tokenization metrics. We build each vocabs using MODU corpus and compare them on
WIKIPEDIA corpus.
Tokenization
# Vocabs
Fertility ↓
% Continued Word ↑
UNK Ratio ↓
BPE
32k
2.073
0.578
0.011
Morpheme-based Subword
32k
2.468
0.765
0.009
We ﬁnd these qualitative differences between two schemes lead to signiﬁcant differences in the task performance in the
cases of KLUE-NER, KLUE-MRC and WoS. These tasks often involve tagging, detection and even generation at the
morpheme level, and we suspect that morphologically consistent tokenization facilitates better prediction overall. On
the other hand, the difference in the tokenization strategy does not manifest itself in the performance of classiﬁcation
or word-level tagging, likely as a corresponding NLU system can more readily overcome inconsistencies in subword
segmentation when merging subword token representations into that of a larger unit. Overall, we recommend future
researchers use the proposed tokenization strategy as a default option.
56

--- Page 57 ---

6
Ethical Considerations
In building KLUE and accompanying baseline models, we have incorporated various mechanisms to avoid any harmful
and negative consequences from releasing both data and models. These mechanisms are described in detail wherever
they were introduced and used, but in this section, we summarize these mechanisms, considerations and our principles
behind them.
6.1
Copyright and Accessibility
Most NLP datasets are built upon the existing text sources. This raises a question on the terms of using such datasets,
especially when the underlying source datasets are not well-speciﬁed nor carefully investigated. In order to avoid any
such doubt on the terms of using KLUE and to accelerate NLP research in Korean, we fully adhere to the copyright act
of Korea, which went effective on Dec. 8, 2020.64 and include only text for which we know we can release under a
license that permits both redistribution and re-mix without any restriction on the use.
Source Corpora
Our goal is to secure and maximize the continued availability and usefulness of the benchmark. In
other words, we must guarantee the possibility of derive new work and redistribute it freely, which comes together with
CC BY-SA. To release KLUE under CC BY-SA, we have built a source corpus set by including only text that is either 1)
not protected by copyright or 2) under CC0, CC BY, CC BY-SA or KOGL Type 1 license. In the case of news articles,
which are copyrighted, we have signed contracts with the providers, Korean Economics Daily (KED) news media and
Acrofan, that allow us to make KLUE-MRC and release them under CC BY-SA.
Task-Speciﬁc (Annotated) Datasets
We subsample and annotate the source corpus for each KLUE benchmark task.
We release each under CC BY-SA. This allows users of KLUE benchamrk to copy, redistribute, remix, transform and
build upon it for both commercial and non-commercial purposes, as long as derivatives are distributed under the same
license (CC BY-SA). We expect this to greatly facilitate future NLP research and development.
Pretraining Corpora and Language Models
As was discussed earlier 4.1, we cannot guarantee that our pretraining
corpus, built using MODU, CC-100-Kor and NEWSCRAWL, does not contain any copyrighted work, although these
are all created from publicly available text. Unfortunately without these corpora, it is not possible to ﬁnd a sufﬁciently
large resource to train large-scale language models for Korean. We thus use them for pretraining but do not publicly
release the pretraining corpora in order to avoid any issues in the future, which is in contrast to KLUE. Instead, we
openly release pretrained language models to facilitate future research. As the parameters of a language model does not
[express] human thoughts and emotions, they do not meet the requirement of being copyrighted.
6.2
Toxic Content
Although large-scale, accessible benchmark datasets advance machine learning and its applications to adjacent ﬁelds,
such as natural language processing, toxic and unwanted contents within these datasets may be ampliﬁed via large-scale
models we train on them. We have been aware of this issue from the beginning of the project, and here we describe how
we have addressed these toxic contents in KLUE.
Task-Speciﬁc Datasets
For each task-speciﬁc dataset, we apply three stages to minimize the introduction of toxic
contents. First, we automatically detect hate speech and gender-biased sentences using toxicity classiﬁers and remove
those even before sending these sentences for annotation (see Section 2.3). Second, we explicitly and clearly instruct
annotators to mark any instance that exhibits social biases and/or is toxic (see Section 3), after providing them with clear
deﬁnitions of bias and hate speech. Finally, we manually examine these marked sentences and exclude them from the
ﬁnal dataset. This three-stage process may not catch all possible such instances, and we plan to use an online forum65 to
receive feedback and complaints from users of KLUE.
Pretrained Language Models
We use our pretraining corpora (see Section 4.1) as they are, for three reasons. First,
manual inspection is simply not tractable due to the sheer scale. Second, it is challenging to build an automated tool to
detect hate speech and biased sentences. This issue is made even more severe for Korean, because there is only one
known hate speech dataset of limited size [92]. Lastly, we envision the future in which these pretrained language models
are used to build better tools for automatically detecting various toxic contents as well as undesirable social biases. In
64https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EC%A0%80%EC%9E%91%EA%B6%8C%EB%B2%95
65https://github.com/KLUE-benchmark/KLUE/issues
57

--- Page 58 ---

order for such pretrained models to be aware of these issues, they must have been trained with such toxic contents as
well.
6.3
Personally Identiﬁable Information
It has recently been discovered by that a large-scale, pretrained language model memorizes a large amount of personally
identiﬁable information (PII) and that an algorithm can be designed to retrieved those private information. We thus
design two different approaches for pseudonymizing task-speciﬁc datasets and pretraining corpora, respectively.
Task-Speciﬁc Datasets
In the case of task-speciﬁc datasets, we rely on manual inspection during annotation to detect
PII. We discard any sentences that was reported to contain PII after manual inspection. In the case of DST, which relies
on simulated dialogues, we pseudonymize the database entries rather than actual text, using the faker library.66
Pretraining Corpora
There is a trade-off between removing PII and the performance of a pretrained language model,
as we will demonstrate later in this paper. We thus pseudonymize 16 PII types that are detectable purely by regular
expressions. See Section 4.1
7
Related Work
General-Purpose NLU Benchmarks
General Language Understanding Evaluation (GLUE) [133] benchmark, a
collection of evaluation dataset for English, was the ﬁrst general-purpose evaluation benchmarks for NLU. It is general-
purpose in that it is not limited to a single task. It consists of 11 downstream tasks, including tasks that measures the
capability of capturing semantic textual similarity (QQP, MRPC, STS) [3, 13], measures the capability of inference
(MNLI, QNLI, RTE, WNLI) [8, 138] and that evaluates the capability of classifying a single sentence into a predeﬁned
set of categories (CoLA, SST) [134, 126]. GLUE exclusively focused on English, and its variants in different languages
have been built and released over the past couple of years, including CLUE in Chinese [142], a French version [72], an
Indonesian version [137], a version for Indic languages [57], Russian SuperGLUE [125], and Persian GLUE [61]. In
all these cases, substantial efforts were carried out to follow the philosophy of the original GLUE, covering a broad
spectrum of domains and tasks, while incorporating language-speciﬁc characteristics. On the other hand, there have
been efforts to build a multilingual version of such benchmark, largely relying on automated methods, such as XGLUE
[78] and XTREME [54]. Korean as a language has been included in subsets of these latter benchmarks, but there has
not been a serious attempt at building a general-purpose language understanding evaluation suite for Korean, until this
paper.
Absence of a Standard NLU Benchmark in Korean
Until this paper, a number of task-speciﬁc benchmarks in
Korean have been proposed and released. For example, NSMC is used for sentiment classiﬁcation, PAWS-X [144] for
paraphrase detection, KorNLI and KorSTS [45] for NLI and STS, KorQuAD 1 and 2 [79, 63] for MRC, and BEEP!
[92] for hate speech detection. At this point, one may wonder whether it would have been easier and more convenient to
simply aggregate these datasets to build KLUE. After all, this has been a popular strategy for constructing monolingual
[133] as well as multilingual [78, 54] benchmarks. Unfortunately this approach comes with two major issues that we
directly address in this paper.
First, the existing datasets are constructed individually without considering other datasets and their properties. In other
words, the aggregate of these individual datasets is unlikely to cover a broad spectrum of domains and writing styles,
unlike KLUE for which we carefully curate the source corpora as well as subsets for downstream tasks to have broad
coverage of domains and styles. This goes beyond domains and styles, but also the coverage of linguistic phenomena
under evaluation. Most of the existing benchmarks, listed above, focus on semantics rather than syntax, and it is difﬁcult
to ﬁnd any widely-available benchmark that captures pragmatics. We address this issue by carefully selecting a set of
downstream tasks.
Second, these existing datasets are not always publicly available,67 and some are distributed with a highly restrictive
license that prohibits redistribution nor the transformation of the original. These are often the ones published and
released by government-afﬁliated institutes. In some cases, it is necessary to obtain a special permission to access
datasets, which is often not easily accessible by non-Korean researchers. We address all these issues with KLUE
by releaseing the entire benchmark data under CC BY-SA, both by careful curation of source corpora and by direct
agreements with publishers.
66https://github.com/joke2k/faker
67Some of these are publicly available in Korea but not internationally.
58

--- Page 59 ---

Pretrained Language Models (PLMs)
The recent trend of large-scale pretrained language models was sparked by
the success of earlier models, such as ELMo [104], GPT-2 [110] and BERT [30], on the GLUE and other similar NLU
benchmarks. This earlier success has led to a series of advances in large-scale language models, including XLNet
[146], ALBERT [71], RoBERTa [82], ELECTRA [22], and Deberta [49], again largely driven by the availability of
standardized benchmarks. This advance in language models, not only in terms of the model size but also in learning
algorithms, in turn also sparked the interest in building and improving existing language understanding benchmarks.
Some of the recently released, challenging benchmarks include SuperGLUE [132] and KILT [105]. The availability of
such a standard language understanding benchmark, such as KLUE from this paper, is expected to start such a virtuous
cycle for Korean language understanding.
Pretrained Language Models for Korean
Inspired by the development in other languages and multilingual models,
PLM’s for the Korean language have been trained and released by multiple research groups and individuals. SKT
released KoBERT,68 followed by KorBERT69 from ETRI, HanBERT70 from TwoBlock AI, KR-BERT [75] from Seoul
National University. There are a few pretrained models released by individual researchers, such as KoELECTRA [102]
and KcBERT [73].
Unfortunately, it is unclear how we should compare this stream of pretrained language models in Korean, due to the
lack of a standarded benchmark in Korean. Subsets of these models have been compared based on subsets of a few
downtream NLP tasks in Korean above, but because these are not standardized, it is not easy to draw solid conclusions
from these limited experiments. We expect the proposed KLUE benchmark will serve as a standard way to track the
progress of research in language models for Korean.
8
Discussion
Open Access
We distribute KLUE under CC BY-SA. The license allows everyone to freely copy and redistribute our
benchmarks in any medium or format. In addition, one can improve our benchmark to build more challenging datasets
after performance saturation. To function as a NLU benchmark, open access is a must. If the original author does not
allow derivative development of the benchmark, other researchers cannot improve it, for example by removing toxic
content, or building a more challenging dataset to accelerate research for technical improvements. If commercial use is
not allowed, researchers working at for-proﬁt organizations would not be able to beneﬁt from nor to (easily) contribute
to the benchmark. Redistribution is another crucial factor because it signiﬁcantly limits research if, for example, sharing
the datasets with another researcher is prohibited. Another existing practice that limits research is transferring the
responsibility of copyright infringement of related conﬂicts to researchers. To set a good precedent for open access of
data, we allow using our datasets for 1) any purpose, 2) derivative work, and 3) redistribution, as long as the existing
copyrights in our benchmark datasets are respected. We also open our pretrained Korean language models and the
implementation of pretraining and ﬁne-tuning pipelines. This enhances reproducibility of our work, and allows anyone
to ﬁx and improve our data and models. We hope to contribute to the Korean NLP research community as well the
wider NLP community.
Facilitating Korean NLP Research
We developed KLUE with the aim of facilitating Korean NLP research, in
response to the recent active development efforts of large Korean language models. The entire NLP community has seen
BERT [30] and its variants outperforming the previous NLU models for GLUE [133] and SuperGLUE [132], as well as
the more recent GPT3 [9] with outstanding performance without ﬁne-tuning (and with in-context learning) in natural
language understanding and generation. Motivated by these models, many Korean researchers at various institutions
rushed to pretrain large-scale Transformer-based Korean language models. Consequently, a number of nearly identical
pretrained language models have been released to open-source communities. However, we could not systematically
understand the behaviors and characteristics of these models because of the lack of well-designed general-purpose
benchmarks like GLUE for Korean. KLUE will allow us to conduct controlled experiments to understand how and why
various Korean LMs perform on certain tasks and thus obtain detailed insights into those models. Furthermore, since
KLUE includes many representative NLU tasks that are also conducted in other languages, KLUE will function as a
fundamental resource to NLP researchers who aim to conduct multilingual research with Korean and other languages.
Measuring Overall Performance of NLU models
We do not average all scores gained from each task in KLUE. The
performance of all tasks are measured by different evaluation metrics. This is because we carefully choose the metric
for each task with considering its own characteristics. Their granularity differs by tasks, for example, KLUE-MRC and
68https://github.com/SKTBrain/KoBERT
69https://aiopen.etri.re.kr/service_dataset.php
70https://github.com/tbai2019/HanBert-54k-N
59

--- Page 60 ---

KLUE-NER employ character-level metrics because an entity can exist within a word in Korean whereas KLUE-STS
and KLUE-NLI use sentence-level metrics. Furthermore, we use various metrics across tasks, such as F1 score, accuracy,
area under the curve, UAS, LAS, ROUGE-W, joint goal accuracy, and Pearson’s correlation. In this situation, simply
computing the average of all tasks as in GLUE [133] results in misleading overall performance measure. The average
will lose its interpretability as well as giving higher weights to a certain task in unintended ways. Accordingly, an
alternative way to estimating a model’s NLU capability is necessary. Recently, analyzing correctness of a model’s
prediction by using Item Response Theory (IRT) framework to estimate such capability is proposed [70], however, we
ﬁnd that it is not clear how it should be applied precisely in our benchmark. As of now, we thus decide to evaluate a
model for each task separately without any summarization of overall performance measure. This is our limitation, and
we leave this problem for the future.
Rapid Saturation of KLUE
We expect fast saturation of KLUE based on our observations of for instance GLUE
[94]. However, we do not artiﬁcially make our benchmark challenging by e.g. ﬁltering out easy examples for models.
Because the main purpose of KLUE is to properly evaluate models in terms of various aspects of NLU, we avoid
focusing on enlarging headrooms for improvement over our baseline pretrained language models. We expect our license
policy would positively affect the advancement of our benchmark after saturation by collectively developing more
challenging tasks with other researchers, such as building the ﬁrst open-domain question answering for Korean.
Analysis of Korean Language Models
We observe various patterns when comparing performances of the baseline
models on each tasks, however, most of them are understudied to precisely explain the phenomena. With more thorough
investigations, we hope to enhance understanding of the complex interaction of a model, corpus, linguistic properties of
Korean and training mechanisms in future work.
9
Conclusion
We present KLUE, a suite of Korean NLU benchmarks that includes diverse tasks. We open KLUE to everyone, and
we also provide Korean language models trained to outperform multilingual models and other existing open-sourced
Korean language models. We set high standards from the outset, as we built the benchmark and trained the models from
scratch. We designed the benchmark datasets and trained the annotators rigorously to consider potential ethical issues
including private information and hate speech. We documented in detail all of the benchmark construction and testing
processes. We also discussed broader impacts and limitations of KLUE and our models. Despite the limitations, KLUE
and the accompanying language models will facilitate future Korean NLP research by setting a valuable precedent
describing how datasets and language models should be created and spread to a wider community.
Acknowledgments
Upstage sponsored annotation cost and built the leaderboard. NAVER CLOVA provided data annotation cost and GPU
cloud computing infrastructure (NSML). We also thank to Google’s TensorFlow Research Cloud (TFRC) and Kakao
Enterprise’s BrainCloud. The three computing resources were used to pretrain and ﬁne-tune language models. Scatter
Lab, SelectStar, Riiid!, DeepNatural and KAIST sponsored data annotation cost. In addition, we appreciate The Korea
Economy Daily and Acrofan for supporting their news articles for MRC datasets.
The authors thank Cheoneum Park for discussions about task selection and DP task, Jinhyuk Lee and Minjoon Seo for
discussions on MRC task, Sujeong Kim and DongYeon Kim for considerable efforts to manage annotators in MRC
dataset, and Sangah Park for careful consideration of data construction in DP, NER, and RE. We appreciate Junyeop Lee,
Geonhee Lee, Jiho Lee, Daehyun Nam, and Yongjin Cho for the leaderboard and evaluation system implementation.
This study is reviewed and approved by the KAIST Institutional Review Board (#KH2020-173).
60

--- Page 61 ---

References
[1] National Information Society Agency. MRC AI Dataset. https://aihub.or.kr/aidata/86, 2018.
[2] Eneko Agirre, Carmen Banea, Claire Cardie, Daniel Cer, Mona Diab, Aitor Gonzalez-Agirre, Weiwei Guo, Iñigo
Lopez-Gazpio, Montse Maritxalar, Rada Mihalcea, German Rigau, Larraitz Uria, and Janyce Wiebe. SemEval-
2015 task 2: Semantic textual similarity, English, Spanish and pilot on interpretability. In Proceedings of the 9th
International Workshop on Semantic Evaluation (SemEval 2015), pages 252–263, Denver, Colorado, June 2015.
Association for Computational Linguistics. doi: 10.18653/v1/S15-2045. URL https://www.aclweb.org/
anthology/S15-2045.
[3] Eneko Agirre, Carmen Banea, Daniel Cer, Mona Diab, Aitor Gonzalez-Agirre, Rada Mihalcea, German Rigau,
and Janyce Wiebe. SemEval-2016 task 1: Semantic textual similarity, monolingual and cross-lingual evaluation.
In Proceedings of the 10th International Workshop on Semantic Evaluation (SemEval-2016), pages 497–511,
San Diego, California, June 2016. Association for Computational Linguistics. doi: 10.18653/v1/S16-1081. URL
https://www.aclweb.org/anthology/S16-1081.
[4] Jens Allwood. An activity based approach to pragmatics. In Harry Bunt and William Black, editors, Abduction,
belief and context in dialogue: Studies in computational pragmatics, chapter 2, pages 47–80. John Benjamins,
Amsterdam, Netherlands, 2000.
[5] Livio Baldini Soares, Nicholas FitzGerald, Jeffrey Ling, and Tom Kwiatkowski. Matching the blanks: Dis-
tributional similarity for relation learning. In Proceedings of the 57th Annual Meeting of the Association
for Computational Linguistics, pages 2895–2905, Florence, Italy, July 2019. Association for Computational
Linguistics. doi: 10.18653/v1/P19-1279. URL https://www.aclweb.org/anthology/P19-1279.
[6] Emily M. Bender and Batya Friedman. Data statements for natural language processing: Toward mitigating
system bias and enabling better science. Transactions of the Association for Computational Linguistics, 6:
587–604, 2018. doi: 10.1162/tacl_a_00041. URL https://www.aclweb.org/anthology/Q18-1041.
[7] Samuel R Bowman and George E Dahl. What will it take to ﬁx benchmarking in natural language understanding?
arXiv preprint arXiv:2104.02145, 2021.
[8] Samuel R. Bowman, Gabor Angeli, Christopher Potts, and Christopher D. Manning. A large annotated corpus
for learning natural language inference. In Proceedings of the 2015 Conference on Empirical Methods in
Natural Language Processing, pages 632–642, Lisbon, Portugal, September 2015. Association for Computational
Linguistics. doi: 10.18653/v1/D15-1075. URL https://www.aclweb.org/anthology/D15-1075.
[9] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen
Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel Ziegler, Jeffrey Wu, Clemens Winter, Chris
Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner,
Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. Language models are few-shot learners.
In H. Larochelle, M. Ranzato, R. Hadsell, M. F. Balcan, and H. Lin, editors, Advances in Neural Information
Processing Systems, volume 33, pages 1877–1901. Curran Associates, Inc., 2020. URL https://proceedings.
neurips.cc/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf.
[10] Paweł Budzianowski, Tsung-Hsien Wen, Bo-Hsiang Tseng, Iñigo Casanueva, Stefan Ultes, Osman Ramadan,
and Milica Gaši´c. MultiWOZ - a large-scale multi-domain Wizard-of-Oz dataset for task-oriented dialogue
modelling. In Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing,
pages 5016–5026, Brussels, Belgium, October-November 2018. Association for Computational Linguistics. doi:
10.18653/v1/D18-1547. URL https://www.aclweb.org/anthology/D18-1547.
[11] Bill Byrne, Karthik Krishnamoorthi, Chinnadhurai Sankar, Arvind Neelakantan, Ben Goodrich, Daniel Duck-
worth, Semih Yavuz, Amit Dubey, Kyu-Young Kim, and Andy Cedilnik. Taskmaster-1: Toward a realistic and
diverse dialog dataset. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language
Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP),
pages 4516–4525, Hong Kong, China, November 2019. Association for Computational Linguistics.
doi:
10.18653/v1/D19-1459. URL https://www.aclweb.org/anthology/D19-1459.
[12] Nicholas Carlini, Florian Tramer, Eric Wallace, Matthew Jagielski, Ariel Herbert-Voss, Katherine Lee, Adam
Roberts, Tom Brown, Dawn Song, Ulfar Erlingsson, et al. Extracting training data from large language models.
arXiv preprint arXiv:2012.07805, 2020.
61

--- Page 62 ---

[13] Daniel Cer, Mona Diab, Eneko Agirre, Iñigo Lopez-Gazpio, and Lucia Specia. SemEval-2017 task 1: Semantic
textual similarity multilingual and crosslingual focused evaluation. In Proceedings of the 11th International
Workshop on Semantic Evaluation (SemEval-2017), pages 1–14, Vancouver, Canada, August 2017. Association
for Computational Linguistics. doi: 10.18653/v1/S17-2001. URL https://www.aclweb.org/anthology/
S17-2001.
[14] Hongshen Chen, Xiaorui Liu, Dawei Yin, and Jiliang Tang. A survey on dialogue systems: Recent advances and
new frontiers. SIGKDD Explor. Newsl., 19(2):25–35, November 2017. ISSN 1931-0145. doi: 10.1145/3166054.
3166058. URL https://doi.org/10.1145/3166054.3166058.
[15] Pengyu Cheng, Weituo Hao, Siyang Yuan, Shijing Si, and Lawrence Carin. FairFil: Contrastive neural debiasing
method for pretrained text encoders. In International Conference on Learning Representations, 2021. URL
https://openreview.net/forum?id=N6JECD-PI5w.
[16] Nancy A. Chinchor. Overview of MUC-7. In Seventh Message Understanding Conference (MUC-7): Proceedings
of a Conference Held in Fairfax, Virginia, April 29 - May 1, 1998, 1998. URL https://www.aclweb.org/
anthology/M98-1001.
[17] Kyunghyun Cho, Bart van Merriënboer, Caglar Gulcehre, Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk,
and Yoshua Bengio. Learning phrase representations using RNN encoder–decoder for statistical machine
translation. In Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing
(EMNLP), pages 1724–1734, Doha, Qatar, October 2014. Association for Computational Linguistics. doi:
10.3115/v1/D14-1179. URL https://www.aclweb.org/anthology/D14-1179.
[18] Won Ik Cho, Jong In Kim, Young Ki Moon, and Nam Soo Kim. Discourse component to sentence (DC2S): An
efﬁcient human-aided construction of paraphrase and sentence similarity dataset. In Proceedings of the 12th
Language Resources and Evaluation Conference, pages 6819–6826, Marseille, France, May 2020. European
Language Resources Association. ISBN 979-10-95546-34-4. URL https://www.aclweb.org/anthology/
2020.lrec-1.842.
[19] Won Ik Cho, Sangwhan Moon, and Youngsook Song. Open Korean corpora: A practical report. In Proceedings of
Second Workshop for NLP Open Source Software (NLP-OSS), pages 85–93, Online, November 2020. Association
for Computational Linguistics. URL https://www.aclweb.org/anthology/2020.nlposs-1.12.
[20] Jayeol Chun, Na-Rae Han, Jena D. Hwang, and Jinho D. Choi. Building Universal Dependency treebanks
in Korean. In Proceedings of the Eleventh International Conference on Language Resources and Evaluation
(LREC 2018), Miyazaki, Japan, May 2018. European Language Resources Association (ELRA). URL https:
//www.aclweb.org/anthology/L18-1347.
[21] Christopher Clark, Kenton Lee, Ming-Wei Chang, Tom Kwiatkowski, Michael Collins, and Kristina Toutanova.
BoolQ: Exploring the surprising difﬁculty of natural yes/no questions. In Proceedings of the 2019 Conference of
the North American Chapter of the Association for Computational Linguistics: Human Language Technologies,
Volume 1 (Long and Short Papers), pages 2924–2936, Minneapolis, Minnesota, June 2019. Association for
Computational Linguistics. doi: 10.18653/v1/N19-1300. URL https://www.aclweb.org/anthology/
N19-1300.
[22] Kevin Clark, Minh-Thang Luong, Quoc V. Le, and Christopher D. Manning. ELECTRA: Pre-training text
encoders as discriminators rather than generators. In International Conference on Learning Representations,
2020. URL https://openreview.net/pdf?id=r1xMH1BtvB.
[23] Korea Copyright Commission. Newspapers and copyright, 2009.
[24] Alexis Conneau, Douwe Kiela, Holger Schwenk, Loïc Barrault, and Antoine Bordes. Supervised learning of
universal sentence representations from natural language inference data. In Proceedings of the 2017 Conference
on Empirical Methods in Natural Language Processing, pages 670–680, Copenhagen, Denmark, September
2017. Association for Computational Linguistics. doi: 10.18653/v1/D17-1070. URL https://www.aclweb.
org/anthology/D17-1070.
[25] Alexis Conneau, Ruty Rinott, Guillaume Lample, Adina Williams, Samuel Bowman, Holger Schwenk, and
Veselin Stoyanov. XNLI: Evaluating cross-lingual sentence representations. In Proceedings of the 2018
Conference on Empirical Methods in Natural Language Processing, pages 2475–2485, Brussels, Belgium,
October-November 2018. Association for Computational Linguistics. doi: 10.18653/v1/D18-1269. URL
https://www.aclweb.org/anthology/D18-1269.
62

--- Page 63 ---

[26] Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco
Guzmán, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov. Unsupervised cross-lingual
representation learning at scale. In Proceedings of the 58th Annual Meeting of the Association for Computational
Linguistics, pages 8440–8451, Online, July 2020. Association for Computational Linguistics. doi: 10.18653/v1/
2020.acl-main.747. URL https://www.aclweb.org/anthology/2020.acl-main.747.
[27] Ido Dagan, Oren Glickman, and Bernardo Magnini. The PASCAL recognising textual entailment challenge.
In Joaquin Quiñonero-Candela, Ido Dagan, Bernardo Magnini, and Florence d’Alché Buc, editors, Machine
Learning Challenges. Evaluating Predictive Uncertainty, Visual Object Classiﬁcation, and Recognising Tectual
Entailment, pages 177–190, Berlin, Heidelberg, 2006. Springer Berlin Heidelberg. ISBN 978-3-540-33428-6.
[28] Marie-Catherine de Marneffe and Christopher D. Manning. The Stanford typed dependencies representation. In
Coling 2008: Proceedings of the workshop on Cross-Framework and Cross-Domain Parser Evaluation, pages
1–8, Manchester, UK, August 2008. Coling 2008 Organizing Committee. URL https://www.aclweb.org/
anthology/W08-1301.
[29] Marie-Catherine de Marneffe, Bill MacCartney, and Christopher D. Manning. Generating typed dependency
parses from phrase structure parses. In Proceedings of the Fifth International Conference on Language Resources
and Evaluation (LREC’06), Genoa, Italy, May 2006. European Language Resources Association (ELRA). URL
http://www.lrec-conf.org/proceedings/lrec2006/pdf/440_pdf.pdf.
[30] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT: Pre-training of deep bidirectional
transformers for language understanding. In Proceedings of the 2019 Conference of the North American Chapter
of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short
Papers), pages 4171–4186, Minneapolis, Minnesota, June 2019. Association for Computational Linguistics. doi:
10.18653/v1/N19-1423. URL https://www.aclweb.org/anthology/N19-1423.
[31] George Doddington, Alexis Mitchell, Mark Przybocki, Lance Ramshaw, Stephanie Strassel, and Ralph
Weischedel. The automatic content extraction (ACE) program – tasks, data, and evaluation. In Proceedings
of the Fourth International Conference on Language Resources and Evaluation (LREC’04), Lisbon, Portu-
gal, May 2004. European Language Resources Association (ELRA). URL http://www.lrec-conf.org/
proceedings/lrec2004/pdf/5.pdf.
[32] William B. Dolan and Chris Brockett. Automatically constructing a corpus of sentential paraphrases. In
Proceedings of the Third International Workshop on Paraphrasing (IWP2005), 2005. URL https://www.
aclweb.org/anthology/I05-5002.
[33] Timothy Dozat and Christopher D. Manning. Deep biafﬁne attention for neural dependency parsing. In
International Conference on Learning Representations, 2017. URL https://openreview.net/forum?id=
Hk95PK9le.
[34] David M. Eberhard and Charles D. Simons, Gary F. Fenning. Ethnologue: Languages of the World. SIL
International, Dallas, Texas, 24 edition, 2021. URL http://www.ethnologue.com.
[35] Layla El Asri, Hannes Schulz, Shikhar Sharma, Jeremie Zumer, Justin Harris, Emery Fine, Rahul Mehrotra, and
Kaheer Suleman. Frames: a corpus for adding memory to goal-oriented dialogue systems. In Proceedings of the
18th Annual SIGdial Meeting on Discourse and Dialogue, pages 207–219, Saarbrücken, Germany, August 2017.
Association for Computational Linguistics. doi: 10.18653/v1/W17-5526. URL https://www.aclweb.org/
anthology/W17-5526.
[36] Mihail Eric, Lakshmi Krishnan, Francois Charette, and Christopher D. Manning. Key-value retrieval networks
for task-oriented dialogue. In Proceedings of the 18th Annual SIGdial Meeting on Discourse and Dialogue,
pages 37–49, Saarbrücken, Germany, August 2017. Association for Computational Linguistics. doi: 10.18653/
v1/W17-5506. URL https://www.aclweb.org/anthology/W17-5506.
[37] Mihail Eric, Rahul Goel, Shachi Paul, Abhishek Sethi, Sanchit Agarwal, Shuyang Gao, Adarsh Kumar, Anuj
Goyal, Peter Ku, and Dilek Hakkani-Tur. MultiWOZ 2.1: A consolidated multi-domain dialogue dataset with
state corrections and state tracking baselines. In Proceedings of the 12th Language Resources and Evaluation
Conference, pages 422–428, Marseille, France, May 2020. European Language Resources Association. ISBN
979-10-95546-34-4. URL https://www.aclweb.org/anthology/2020.lrec-1.53.
63

--- Page 64 ---

[38] Angela Fan, Yacine Jernite, Ethan Perez, David Grangier, Jason Weston, and Michael Auli. ELI5: Long
form question answering. In Proceedings of the 57th Annual Meeting of the Association for Computational
Linguistics, pages 3558–3567, Florence, Italy, July 2019. Association for Computational Linguistics. doi:
10.18653/v1/P19-1346. URL https://www.aclweb.org/anthology/P19-1346.
[39] Daniel Fernández-González and Carlos Gómez-Rodríguez. Left-to-right dependency parsing with pointer
networks. In Proceedings of the 2019 Conference of the North American Chapter of the Association for
Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), pages 710–716,
Minneapolis, Minnesota, June 2019. Association for Computational Linguistics. doi: 10.18653/v1/N19-1076.
URL https://www.aclweb.org/anthology/N19-1076.
[40] Jenny Rose Finkel, Trond Grenager, and Christopher Manning. Incorporating non-local information into
information extraction systems by Gibbs sampling. In Proceedings of the 43rd Annual Meeting of the Association
for Computational Linguistics (ACL’05), pages 363–370, Ann Arbor, Michigan, June 2005. Association for
Computational Linguistics. doi: 10.3115/1219840.1219885. URL https://www.aclweb.org/anthology/
P05-1045.
[41] Timnit Gebru, Jamie Morgenstern, Briana Vecchione, Jennifer Wortman Vaughan, Hanna Wallach, Hal Daumé III,
and Kate Crawford. Datasheets for datasets. arXiv preprint arXiv:1803.09010, 2018.
[42] Max Glockner, Vered Shwartz, and Yoav Goldberg. Breaking NLI systems with sentences that require simple
lexical inferences. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics
(Volume 2: Short Papers), pages 650–655, Melbourne, Australia, July 2018. Association for Computational
Linguistics. doi: 10.18653/v1/P18-2103. URL https://www.aclweb.org/anthology/P18-2103.
[43] Ralph Grishman and Beth Sundheim. Message Understanding Conference- 6: A brief history. In COLING 1996
Volume 1: The 16th International Conference on Computational Linguistics, 1996. URL https://www.aclweb.
org/anthology/C96-1079.
[44] Suchin Gururangan, Swabha Swayamdipta, Omer Levy, Roy Schwartz, Samuel Bowman, and Noah A. Smith.
Annotation artifacts in natural language inference data. In Proceedings of the 2018 Conference of the North
American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 2
(Short Papers), pages 107–112, New Orleans, Louisiana, June 2018. Association for Computational Linguistics.
doi: 10.18653/v1/N18-2017. URL https://www.aclweb.org/anthology/N18-2017.
[45] Jiyeon Ham, Yo Joong Choe, Kyubyong Park, Ilji Choi, and Hyungjoon Soh. KorNLI and KorSTS: New
benchmark datasets for Korean natural language understanding. In Findings of the Association for Compu-
tational Linguistics: EMNLP 2020, pages 422–430, Online, November 2020. Association for Computational
Linguistics. doi: 10.18653/v1/2020.ﬁndings-emnlp.39. URL https://www.aclweb.org/anthology/2020.
findings-emnlp.39.
[46] Ji Yoon Han, Tae Hwan Oh, Lee Jin, and Hansaem Kim. Annotation issues in Universal Dependencies for
Korean and Japanese. In Proceedings of the Fourth Workshop on Universal Dependencies (UDW 2020),
pages 99–108, Barcelona, Spain (Online), December 2020. Association for Computational Linguistics. URL
https://www.aclweb.org/anthology/2020.udw-1.12.
[47] Na-Rae Han, Shijong Ryu, Sook-Hee Chae, Seung-yun Yang, Seunghun Lee, and Martha Palmer. Korean
treebank annotations version 2.0. Linguistic Data Consortium (LDC), Philadelphia, 2006.
[48] Xu Han, Hao Zhu, Pengfei Yu, Ziyun Wang, Yuan Yao, Zhiyuan Liu, and Maosong Sun. FewRel: A large-
scale supervised few-shot relation classiﬁcation dataset with state-of-the-art evaluation. In Proceedings of
the 2018 Conference on Empirical Methods in Natural Language Processing, pages 4803–4809, Brussels,
Belgium, October-November 2018. Association for Computational Linguistics. doi: 10.18653/v1/D18-1514.
URL https://www.aclweb.org/anthology/D18-1514.
[49] Pengcheng He, Xiaodong Liu, Jianfeng Gao, and Weizhu Chen. DeBERTa: Decoding-enhanced BERT with
disentangled attention. In International Conference on Learning Representations, 2021. URL https://
openreview.net/forum?id=XPZIaotutsD.
[50] Matthew Henderson, Blaise Thomson, and Jason D. Williams. The second dialog state tracking challenge. In
Proceedings of the 15th Annual Meeting of the Special Interest Group on Discourse and Dialogue (SIGDIAL),
pages 263–272, Philadelphia, PA, U.S.A., June 2014. Association for Computational Linguistics. doi: 10.3115/
v1/W14-4337. URL https://www.aclweb.org/anthology/W14-4337.
64

--- Page 65 ---

[51] Matthew Henderson, Blaise Thomson, and Jason D Williams. The third dialog state tracking challenge. In 2014
IEEE Spoken Language Technology Workshop (SLT), pages 324–329. IEEE, 2014.
[52] Iris Hendrickx, Su Nam Kim, Zornitsa Kozareva, Preslav Nakov, Diarmuid Ó Séaghdha, Sebastian Padó, Marco
Pennacchiotti, Lorenza Romano, and Stan Szpakowicz. SemEval-2010 task 8: Multi-way classiﬁcation of
semantic relations between pairs of nominals. In Proceedings of the 5th International Workshop on Semantic
Evaluation, pages 33–38, Uppsala, Sweden, July 2010. Association for Computational Linguistics. URL
https://www.aclweb.org/anthology/S10-1006.
[53] Hai Hu, Kyle Richardson, Liang Xu, Lu Li, Sandra Kübler, and Lawrence Moss. OCNLI: Original Chinese
Natural Language Inference. In Findings of the Association for Computational Linguistics: EMNLP 2020,
pages 3512–3526, Online, November 2020. Association for Computational Linguistics. doi: 10.18653/v1/2020.
ﬁndings-emnlp.314. URL https://www.aclweb.org/anthology/2020.findings-emnlp.314.
[54] Junjie Hu, Sebastian Ruder, Aditya Siddhant, Graham Neubig, Orhan Firat, and Melvin Johnson. XTREME:
A massively multilingual multi-task benchmark for evaluating cross-lingual generalisation. In Hal Daumé
III and Aarti Singh, editors, Proceedings of the 37th International Conference on Machine Learning, volume
119 of Proceedings of Machine Learning Research, pages 4411–4421. PMLR, 13–18 Jul 2020. URL http:
//proceedings.mlr.press/v119/hu20b.html.
[55] Ali Jabbari, Olivier Sauvage, Hamada Zeine, and Hamza Chergui. A French corpus and annotation schema for
named entity recognition and relation extraction of ﬁnancial news. In Proceedings of the 12th Language Resources
and Evaluation Conference, pages 2293–2299, Marseille, France, May 2020. European Language Resources
Association. ISBN 979-10-95546-34-4. URL https://www.aclweb.org/anthology/2020.lrec-1.279.
[56] Mandar Joshi, Eunsol Choi, Daniel Weld, and Luke Zettlemoyer. TriviaQA: A large scale distantly supervised
challenge dataset for reading comprehension. In Proceedings of the 55th Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Papers), pages 1601–1611, Vancouver, Canada, July 2017.
Association for Computational Linguistics. doi: 10.18653/v1/P17-1147. URL https://www.aclweb.org/
anthology/P17-1147.
[57] Divyanshu Kakwani, Anoop Kunchukuttan, Satish Golla, Gokul N.C., Avik Bhattacharyya, Mitesh M. Khapra,
and Pratyush Kumar. IndicNLPSuite: Monolingual corpora, evaluation benchmarks and pre-trained multilingual
language models for Indian languages. In Findings of the Association for Computational Linguistics: EMNLP
2020, pages 4948–4961, Online, November 2020. Association for Computational Linguistics. doi: 10.18653/v1/
2020.ﬁndings-emnlp.445. URL https://www.aclweb.org/anthology/2020.findings-emnlp.445.
[58] Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B Brown, Benjamin Chess, Rewon Child, Scott Gray,
Alec Radford, Jeffrey Wu, and Dario Amodei. Scaling laws for neural language models. arXiv preprint
arXiv:2001.08361, 2020.
[59] J. F. Kelley. An iterative design methodology for user-friendly natural language ofﬁce information applications.
ACM Trans. Inf. Syst., 2(1):26–41, January 1984. ISSN 1046-8188. doi: 10.1145/357417.357420. URL
https://doi.org/10.1145/357417.357420.
[60] Daniel Khashabi, Snigdha Chaturvedi, Michael Roth, Shyam Upadhyay, and Dan Roth. Looking beyond
the surface: A challenge set for reading comprehension over multiple sentences. In Proceedings of the 2018
Conference of the North American Chapter of the Association for Computational Linguistics: Human Language
Technologies, Volume 1 (Long Papers), pages 252–262, New Orleans, Louisiana, June 2018. Association for
Computational Linguistics. doi: 10.18653/v1/N18-1023. URL https://www.aclweb.org/anthology/
N18-1023.
[61] Daniel Khashabi, Arman Cohan, Siamak Shakeri, Pedram Hosseini, Pouya Pezeshkpour, Malihe Alikhani,
Moin Aminnaseri, Marzieh Bitaab, Faeze Brahman, Sarik Ghazarian, et al. ParsiNLU: a suite of language
understanding challenges for persian. arXiv preprint arXiv:2012.06154, 2020.
[62] Douwe Kiela, Hamed Firooz, Aravind Mohan, Vedanuj Goswami, Amanpreet Singh, Pratik Ringshia, and Davide
Testuggine. The hateful memes challenge: Detecting hate speech in multimodal memes. In H. Larochelle,
M. Ranzato, R. Hadsell, M. F. Balcan, and H. Lin, editors, Advances in Neural Information Processing Systems,
volume 33, pages 2611–2624. Curran Associates, Inc., 2020. URL https://proceedings.neurips.cc/
paper/2020/file/1b84c4cee2b8b3d823b30e2d604b1878-Paper.pdf.
65

--- Page 66 ---

[63] Youngmin Kim, Seungyoung Lim, Hyunjeong Lee, Soyoon Park, and Myungji Kim. KorQuAD 2.0: Korean QA
dataset for web document machine comprehension. Journal of KIISE, 47:577–586, 2020. ISSN 2383-630X. URL
https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=NART99691770&dbt=NART.
[64] Eliyahu Kiperwasser and Yoav Goldberg. Simple and accurate dependency parsing using bidirectional LSTM
feature representations. Transactions of the Association for Computational Linguistics, 4:313–327, 2016. doi:
10.1162/tacl_a_00101. URL https://www.aclweb.org/anthology/Q16-1023.
[65] Dan Klein and Christopher D. Manning. Accurate unlexicalized parsing. In Proceedings of the 41st Annual
Meeting of the Association for Computational Linguistics, pages 423–430, Sapporo, Japan, July 2003. Association
for Computational Linguistics. doi: 10.3115/1075096.1075150. URL https://www.aclweb.org/anthology/
P03-1054.
[66] Miyoung Ko, Jinhyuk Lee, Hyunjae Kim, Gangwoo Kim, and Jaewoo Kang. Look at the ﬁrst sentence: Position
bias in question answering. In Proceedings of the 2020 Conference on Empirical Methods in Natural Language
Processing (EMNLP), pages 1109–1121, Online, November 2020. Association for Computational Linguistics. doi:
10.18653/v1/2020.emnlp-main.84. URL https://www.aclweb.org/anthology/2020.emnlp-main.84.
[67] K. Krippendorff. Computing Krippendorff’s alpha-reliability. 2011.
[68] Taku Kudo. MeCab: Yet another part-of-speech and morphological analyzer, 2006. URL https://taku910.
github.io/mecab/.
[69] Tom Kwiatkowski, Jennimaria Palomaki, Olivia Redﬁeld, Michael Collins, Ankur Parikh, Chris Alberti, Danielle
Epstein, Illia Polosukhin, Jacob Devlin, Kenton Lee, Kristina Toutanova, Llion Jones, Matthew Kelcey, Ming-Wei
Chang, Andrew M. Dai, Jakob Uszkoreit, Quoc Le, and Slav Petrov. Natural questions: A benchmark for question
answering research. Transactions of the Association for Computational Linguistics, 7:452–466, March 2019.
doi: 10.1162/tacl_a_00276. URL https://www.aclweb.org/anthology/Q19-1026.
[70] John P. Lalor and Hong Yu. Dynamic data selection for curriculum learning via ability estimation. In Findings
of the Association for Computational Linguistics: EMNLP 2020, pages 545–555, Online, November 2020.
Association for Computational Linguistics. doi: 10.18653/v1/2020.ﬁndings-emnlp.48. URL https://www.
aclweb.org/anthology/2020.findings-emnlp.48.
[71] Zhenzhong Lan, Mingda Chen, Sebastian Goodman, Kevin Gimpel, Piyush Sharma, and Radu Soricut. ALBERT:
A lite BERT for self-supervised learning of language representations. In International Conference on Learning
Representations, 2020. URL https://openreview.net/forum?id=H1eA7AEtvS.
[72] Hang Le, Loïc Vial, Jibril Frej, Vincent Segonne, Maximin Coavoux, Benjamin Lecouteux, Alexandre Allauzen,
Benoit Crabbé, Laurent Besacier, and Didier Schwab. FlauBERT: Unsupervised language model pre-training
for French. In Proceedings of the 12th Language Resources and Evaluation Conference, pages 2479–2490,
Marseille, France, May 2020. European Language Resources Association. ISBN 979-10-95546-34-4. URL
https://www.aclweb.org/anthology/2020.lrec-1.302.
[73] Junbum Lee. KcBERT: Korean comments BERT. In Proceedings of the 32nd Annual Conference on Human and
Cognitive Language Technology, pages 437–440, 2020.
[74] Kyungjae Lee, Kyoungho Yoon, Sunghyun Park, and Seung-won Hwang. Semi-supervised training data
generation for multilingual question answering. In Proceedings of the Eleventh International Conference on
Language Resources and Evaluation (LREC 2018), Miyazaki, Japan, May 2018. European Language Resources
Association (ELRA). URL https://www.aclweb.org/anthology/L18-1437.
[75] Sangah Lee, Hansol Jang, Yunmee Baik, Suzi Park, and Hyopil Shin. KR-BERT: A small-scale Korean-speciﬁc
language model. arXiv preprint arXiv:2008.03979, 2020.
[76] Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy, Veselin
Stoyanov, and Luke Zettlemoyer. BART: Denoising sequence-to-sequence pre-training for natural language
generation, translation, and comprehension. In Proceedings of the 58th Annual Meeting of the Association for
Computational Linguistics, pages 7871–7880, Online, July 2020. Association for Computational Linguistics.
doi: 10.18653/v1/2020.acl-main.703. URL https://www.aclweb.org/anthology/2020.acl-main.703.
[77] Shiyang Li, Semih Yavuz, Kazuma Hashimoto, Jia Li, Tong Niu, Nazneen Rajani, Xifeng Yan, Yingbo Zhou,
and Caiming Xiong. CoCo: Controllable counterfactuals for evaluating dialogue state trackers. arXiv preprint
arXiv:2010.12850, 2020.
66

--- Page 67 ---

[78] Yaobo Liang, Nan Duan, Yeyun Gong, Ning Wu, Fenfei Guo, Weizhen Qi, Ming Gong, Linjun Shou, Daxin Jiang,
Guihong Cao, Xiaodong Fan, Ruofei Zhang, Rahul Agrawal, Edward Cui, Sining Wei, Taroon Bharti, Ying Qiao,
Jiun-Hung Chen, Winnie Wu, Shuguang Liu, Fan Yang, Daniel Campos, Rangan Majumder, and Ming Zhou.
XGLUE: A new benchmark datasetfor cross-lingual pre-training, understanding and generation. In Proceedings
of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP), pages 6008–6018,
Online, November 2020. Association for Computational Linguistics. doi: 10.18653/v1/2020.emnlp-main.484.
URL https://www.aclweb.org/anthology/2020.emnlp-main.484.
[79] Seungyoung Lim, Myungji Kim, and Jooyoul Lee. KorQuAD1.0: Korean QA dataset for machine reading
comprehension. arXiv preprint arXiv:1909.07005, 2019.
[80] Chin-Yew Lin. ROUGE: A package for automatic evaluation of summaries. In Text Summarization Branches
Out, pages 74–81, Barcelona, Spain, July 2004. Association for Computational Linguistics. URL https:
//www.aclweb.org/anthology/W04-1013.
[81] Alisa Liu, Maarten Sap, Ximing Lu, Swabha Swayamdipta, Chandra Bhagavatula, Noah A. Smith, and Yejin
Choi. On-the-ﬂy controlled text generation with experts and anti-experts, 2021.
[82] Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke
Zettlemoyer, and Veselin Stoyanov. RoBERTa: A robustly optimized BERT pretraining approach. arXiv preprint
arXiv:1907.11692, 2019.
[83] Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. In International Conference on
Learning Representations, 2019. URL https://openreview.net/forum?id=Bkg6RiCqY7.
[84] Mitchell P. Marcus, Beatrice Santorini, and Mary Ann Marcinkiewicz. Building a large annotated corpus of
English: The Penn Treebank. Computational Linguistics, 19(2):313–330, 1993. URL https://www.aclweb.
org/anthology/J93-2004.
[85] Bryan McCann, Nitish Shirish Keskar, Caiming Xiong, and Richard Socher. The natural language decathlon:
Multitask learning as question answering. arXiv preprint arXiv:1806.08730, 2018.
[86] Ryan McDonald, Joakim Nivre, Yvonne Quirmbach-Brundage, Yoav Goldberg, Dipanjan Das, Kuzman Ganchev,
Keith Hall, Slav Petrov, Hao Zhang, Oscar Täckström, Claudia Bedini, Núria Bertomeu Castelló, and Jungmee
Lee. Universal Dependency annotation for multilingual parsing. In Proceedings of the 51st Annual Meeting of
the Association for Computational Linguistics (Volume 2: Short Papers), pages 92–97, Soﬁa, Bulgaria, August
2013. Association for Computational Linguistics. URL https://www.aclweb.org/anthology/P13-2017.
[87] Paul McNamee and Hoa Trang Dang. Overview of the TAC 2009 knowledge base population track. In Text
Analysis Conference (TAC), volume 17, pages 111–113, 2009.
[88] Shikib Mehri, Mihail Eric, and Dilek Hakkani-Tur. DialoGLUE: A natural language understanding benchmark
for task-oriented dialogue. arXiv preprint arXiv:2009.13570, 2020.
[89] Junghyun Min, R. Thomas McCoy, Dipanjan Das, Emily Pitler, and Tal Linzen. Syntactic data augmentation
increases robustness to inference heuristics. In Proceedings of the 58th Annual Meeting of the Association for
Computational Linguistics, pages 2339–2352, Online, July 2020. Association for Computational Linguistics.
doi: 10.18653/v1/2020.acl-main.212. URL https://www.aclweb.org/anthology/2020.acl-main.212.
[90] Sewon Min, Eric Wallace, Sameer Singh, Matt Gardner, Hannaneh Hajishirzi, and Luke Zettlemoyer. Compo-
sitional questions do not necessitate multi-hop reasoning. In Proceedings of the 57th Annual Meeting of the
Association for Computational Linguistics, pages 4249–4257, Florence, Italy, July 2019. Association for Compu-
tational Linguistics. doi: 10.18653/v1/P19-1416. URL https://www.aclweb.org/anthology/P19-1416.
[91] Mike Mintz, Steven Bills, Rion Snow, and Daniel Jurafsky. Distant supervision for relation extraction without la-
beled data. In Proceedings of the Joint Conference of the 47th Annual Meeting of the ACL and the 4th International
Joint Conference on Natural Language Processing of the AFNLP, pages 1003–1011, Suntec, Singapore, August
2009. Association for Computational Linguistics. URL https://www.aclweb.org/anthology/P09-1113.
[92] Jihyung Moon, Won Ik Cho, and Junbum Lee. BEEP! Korean corpus of online news comments for toxic speech
detection. In Proceedings of the Eighth International Workshop on Natural Language Processing for Social Media,
pages 25–31, Online, July 2020. Association for Computational Linguistics. doi: 10.18653/v1/2020.socialnlp-1.4.
URL https://www.aclweb.org/anthology/2020.socialnlp-1.4.
67

--- Page 68 ---

[93] Sangha Nam, Minho Lee, Donghwan Kim, Kijong Han, Kuntae Kim, Sooji Yoon, Eun-kyung Kim, and Key-Sun
Choi. Effective crowdsourcing of multiple tasks for comprehensive knowledge extraction. In Proceedings of the
12th Language Resources and Evaluation Conference, pages 212–219, Marseille, France, May 2020. European
Language Resources Association. ISBN 979-10-95546-34-4. URL https://www.aclweb.org/anthology/
2020.lrec-1.27.
[94] Nikita Nangia and Samuel R. Bowman. Human vs. muppet: A conservative estimate of human performance
on the GLUE benchmark. In Proceedings of the 57th Annual Meeting of the Association for Computational
Linguistics, pages 4566–4575, Florence, Italy, July 2019. Association for Computational Linguistics. doi:
10.18653/v1/P19-1449. URL https://www.aclweb.org/anthology/P19-1449.
[95] Nikita Nangia, Clara Vania, Rasika Bhalerao, and Samuel R. Bowman. CrowS-pairs: A challenge dataset for
measuring social biases in masked language models. In Proceedings of the 2020 Conference on Empirical
Methods in Natural Language Processing (EMNLP), pages 1953–1967, Online, November 2020. Association
for Computational Linguistics. doi: 10.18653/v1/2020.emnlp-main.154. URL https://www.aclweb.org/
anthology/2020.emnlp-main.154.
[96] Tri
Nguyen,
Mir
Rosenberg,
Xia
Song,
Jianfeng
Gao,
Saurabh
Tiwary,
Rangan
Majumder,
and Li Deng.
MS MARCO: A human generated MAchine reading COmprehension dataset.
November
2016.
URL
https://www.microsoft.com/en-us/research/publication/
ms-marco-human-generated-machine-reading-comprehension-dataset/.
[97] Joakim Nivre, Marie-Catherine de Marneffe, Filip Ginter, Yoav Goldberg, Jan Hajiˇc, Christopher D. Manning,
Ryan McDonald, Slav Petrov, Sampo Pyysalo, Natalia Silveira, Reut Tsarfaty, and Daniel Zeman. Universal
Dependencies v1: A multilingual treebank collection. In Proceedings of the Tenth International Conference on
Language Resources and Evaluation (LREC’16), pages 1659–1666, Portorož, Slovenia, May 2016. European
Language Resources Association (ELRA). URL https://www.aclweb.org/anthology/L16-1262.
[98] National Institute of Korean Languages. NIKL CORPORA 2020 (v.1.0), 2020. URL https://corpus.korean.
go.kr.
[99] Tae Hwan Oh, Ji Yoon Han, Hyonsu Choe, Seokwon Park, Han He, Jinho D. Choi, Na-Rae Han, Jena D.
Hwang, and Hansaem Kim. Analysis of the Penn Korean Universal Dependency treebank (PKT-UD): Manual
revision to build robust parsing model in Korean. In Proceedings of the 16th International Conference on
Parsing Technologies and the IWPT 2020 Shared Task on Parsing into Enhanced Universal Dependencies, pages
122–131, Online, July 2020. Association for Computational Linguistics. doi: 10.18653/v1/2020.iwpt-1.13. URL
https://www.aclweb.org/anthology/2020.iwpt-1.13.
[100] Xiaoman Pan, Boliang Zhang, Jonathan May, Joel Nothman, Kevin Knight, and Heng Ji. Cross-lingual name
tagging and linking for 282 languages. In Proceedings of the 55th Annual Meeting of the Association for Compu-
tational Linguistics (Volume 1: Long Papers), pages 1946–1958, Vancouver, Canada, July 2017. Association
for Computational Linguistics. doi: 10.18653/v1/P17-1178. URL https://www.aclweb.org/anthology/
P17-1178.
[101] Eunjeong L. Park and Sungzoon Cho. KoNLPy: Korean natural language processing in Python. In Proceedings
of the 26th Annual Conference on Human & Cognitive Language Technology, Chuncheon, Korea, October 2014.
[102] Jangwon Park. KoELECTRA: Pretrained ELECTRA model for Korean. https://github.com/monologg/
KoELECTRA, 2020.
[103] Kyubyong Park, Joohong Lee, Seongbo Jang, and Dawoon Jung. An empirical study of tokenization strategies
for various Korean NLP tasks.
In Proceedings of the 1st Conference of the Asia-Paciﬁc Chapter of the
Association for Computational Linguistics and the 10th International Joint Conference on Natural Language
Processing, pages 133–142, Suzhou, China, December 2020. Association for Computational Linguistics. URL
https://www.aclweb.org/anthology/2020.aacl-main.17.
[104] Matthew Peters, Mark Neumann, Mohit Iyyer, Matt Gardner, Christopher Clark, Kenton Lee, and Luke Zettle-
moyer. Deep contextualized word representations. In Proceedings of the 2018 Conference of the North American
Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long
Papers), pages 2227–2237, New Orleans, Louisiana, June 2018. Association for Computational Linguistics. doi:
10.18653/v1/N18-1202. URL https://www.aclweb.org/anthology/N18-1202.
68

--- Page 69 ---

[105] Fabio Petroni, Aleksandra Piktus, Angela Fan, Patrick Lewis, Majid Yazdani, Nicola De Cao, James Thorne,
Yacine Jernite, Vladimir Karpukhin, Jean Maillard, et al. KILT: a benchmark for knowledge intensive language
tasks. arXiv preprint arXiv:2009.02252, 2020.
[106] Slav Petrov, Dipanjan Das, and Ryan McDonald. A universal part-of-speech tagset. In Proceedings of the
Eighth International Conference on Language Resources and Evaluation (LREC’12), pages 2089–2096, Istanbul,
Turkey, May 2012. European Language Resources Association (ELRA). URL http://www.lrec-conf.org/
proceedings/lrec2012/pdf/274_Paper.pdf.
[107] Jason Phang, Thibault Févry, and Samuel R Bowman. Sentence encoders on stilts: Supplementary training on
intermediate labeled-data tasks. arXiv preprint arXiv:1811.01088, 2018.
[108] Adam Poliak, Jason Naradowsky, Aparajita Haldar, Rachel Rudinger, and Benjamin Van Durme. Hypothesis
only baselines in natural language inference. In Proceedings of the Seventh Joint Conference on Lexical and
Computational Semantics, pages 180–191, New Orleans, Louisiana, June 2018. Association for Computational
Linguistics. doi: 10.18653/v1/S18-2023. URL https://www.aclweb.org/anthology/S18-2023.
[109] Jun Quan, Shian Zhang, Qian Cao, Zizhong Li, and Deyi Xiong. RiSAWOZ: A large-scale multi-domain
Wizard-of-Oz dataset with rich semantic annotations for task-oriented dialogue modeling. In Proceedings of the
2020 Conference on Empirical Methods in Natural Language Processing (EMNLP), pages 930–940, Online,
November 2020. Association for Computational Linguistics. doi: 10.18653/v1/2020.emnlp-main.67. URL
https://www.aclweb.org/anthology/2020.emnlp-main.67.
[110] Alec Radford, Jeff Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever. Language models are
unsupervised multitask learners. 2019.
[111] Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei
Li, and Peter J. Liu. Exploring the limits of transfer learning with a uniﬁed text-to-text transformer. Journal of
Machine Learning Research, 21(140):1–67, 2020. URL http://jmlr.org/papers/v21/20-074.html.
[112] Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, and Percy Liang. SQuAD: 100,000+ questions for machine
comprehension of text. In Proceedings of the 2016 Conference on Empirical Methods in Natural Language
Processing, pages 2383–2392, Austin, Texas, November 2016. Association for Computational Linguistics. doi:
10.18653/v1/D16-1264. URL https://www.aclweb.org/anthology/D16-1264.
[113] Pranav Rajpurkar, Robin Jia, and Percy Liang. Know what you don’t know: Unanswerable questions for SQuAD.
In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short
Papers), pages 784–789, Melbourne, Australia, July 2018. Association for Computational Linguistics. doi:
10.18653/v1/P18-2124. URL https://www.aclweb.org/anthology/P18-2124.
[114] Abhinav Rastogi, Xiaoxue Zang, Srinivas Sunkara, Raghav Gupta, and Pranav Khaitan. Towards scalable
multi-domain conversational agents: The schema-guided dialogue dataset. Proceedings of the AAAI Conference
on Artiﬁcial Intelligence, 34(05):8689–8696, Apr. 2020. doi: 10.1609/aaai.v34i05.6394. URL https://ojs.
aaai.org/index.php/AAAI/article/view/6394.
[115] Nils Reimers and Iryna Gurevych. Sentence-BERT: Sentence embeddings using Siamese BERT-networks.
In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th
International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), pages 3982–3992, Hong
Kong, China, November 2019. Association for Computational Linguistics. doi: 10.18653/v1/D19-1410. URL
https://www.aclweb.org/anthology/D19-1410.
[116] Sebastian Riedel, Limin Yao, and Andrew McCallum. Modeling relations and their mentions without labeled
text. In José Luis Balcázar, Francesco Bonchi, Aristides Gionis, and Michèle Sebag, editors, Machine Learning
and Knowledge Discovery in Databases, pages 148–163, Berlin, Heidelberg, 2010. Springer Berlin Heidelberg.
ISBN 978-3-642-15939-8.
[117] Alan Ritter, Sam Clark, Mausam, and Oren Etzioni. Named entity recognition in tweets: An experimental
study. In Proceedings of the 2011 Conference on Empirical Methods in Natural Language Processing, pages
1524–1534, Edinburgh, Scotland, UK., July 2011. Association for Computational Linguistics. URL https:
//www.aclweb.org/anthology/D11-1141.
[118] Stephen E Robertson, Steve Walker, Susan Jones, Micheline M Hancock-Beaulieu, Mike Gatford, et al. Okapi at
trec-3. Nist Special Publication Sp, 109:109, 1995.
69

--- Page 70 ---

[119] Phillip Rust, Jonas Pfeiffer, Ivan Vuli´c, Sebastian Ruder, and Iryna Gurevych. How good is your tokenizer? on
the monolingual performance of multilingual language models. arXiv preprint arXiv:2012.15613, 2020.
[120] Amrita Saha, Rahul Aralikatte, Mitesh M. Khapra, and Karthik Sankaranarayanan. DuoRC: Towards complex
language understanding with paraphrased reading comprehension. In Proceedings of the 56th Annual Meeting
of the Association for Computational Linguistics (Volume 1: Long Papers), pages 1683–1693, Melbourne,
Australia, July 2018. Association for Computational Linguistics. doi: 10.18653/v1/P18-1156. URL https:
//www.aclweb.org/anthology/P18-1156.
[121] Martin Schiersch, Veselina Mironova, Maximilian Schmitt, Philippe Thomas, Aleksandra Gabryszak, and
Leonhard Hennig. A German corpus for ﬁne-grained named entity recognition and relation extraction of trafﬁc
and industry events. In Proceedings of the Eleventh International Conference on Language Resources and
Evaluation (LREC 2018), Miyazaki, Japan, May 2018. European Language Resources Association (ELRA).
URL https://www.aclweb.org/anthology/L18-1703.
[122] Priyanka Sen and Amir Saffari. What do models learn from question answering datasets? In Proceedings of the
2020 Conference on Empirical Methods in Natural Language Processing (EMNLP), pages 2429–2438, Online,
November 2020. Association for Computational Linguistics. doi: 10.18653/v1/2020.emnlp-main.190. URL
https://www.aclweb.org/anthology/2020.emnlp-main.190.
[123] Rico Sennrich, Barry Haddow, and Alexandra Birch. Neural machine translation of rare words with subword
units. In Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1:
Long Papers), pages 1715–1725, Berlin, Germany, August 2016. Association for Computational Linguistics. doi:
10.18653/v1/P16-1162. URL https://www.aclweb.org/anthology/P16-1162.
[124] Pararth Shah, Dilek Hakkani-Tür, Gokhan Tür, Abhinav Rastogi, Ankur Bapna, Neha Nayak, and Larry Heck.
Building a conversational agent overnight with dialogue self-play. arXiv preprint arXiv:1801.04871, 2018.
[125] Tatiana Shavrina, Alena Fenogenova, Emelyanov Anton, Denis Shevelev, Ekaterina Artemova, Valentin Malykh,
Vladislav Mikhailov, Maria Tikhonova, Andrey Chertok, and Andrey Evlampiev. RussianSuperGLUE: A
Russian language understanding evaluation benchmark. In Proceedings of the 2020 Conference on Empirical
Methods in Natural Language Processing (EMNLP), pages 4717–4726, Online, November 2020. Association
for Computational Linguistics. doi: 10.18653/v1/2020.emnlp-main.381. URL https://www.aclweb.org/
anthology/2020.emnlp-main.381.
[126] Richard Socher, Alex Perelygin, Jean Wu, Jason Chuang, Christopher D. Manning, Andrew Ng, and Christopher
Potts.
Recursive deep models for semantic compositionality over a sentiment treebank.
In Proceedings
of the 2013 Conference on Empirical Methods in Natural Language Processing, pages 1631–1642, Seattle,
Washington, USA, October 2013. Association for Computational Linguistics. URL https://www.aclweb.
org/anthology/D13-1170.
[127] Benjamin Strauss, Bethany Toma, Alan Ritter, Marie-Catherine de Marneffe, and Wei Xu. Results of the
WNUT16 named entity recognition shared task. In Proceedings of the 2nd Workshop on Noisy User-generated
Text (WNUT), pages 138–144, Osaka, Japan, December 2016. The COLING 2016 Organizing Committee. URL
https://www.aclweb.org/anthology/W16-3919.
[128] Key sun Choi, Young S. Han, Young G. Han, and Oh W. Kwon. KAIST tree bank project for Korean: Present and
future development. In In Proceedings of the International Workshop on Sharable Natural Language Resources,
pages 7–14, 1994.
[129] Erik F. Tjong Kim Sang and Fien De Meulder. Introduction to the CoNLL-2003 shared task: Language-
independent named entity recognition. In Proceedings of the Seventh Conference on Natural Language Learning
at HLT-NAACL 2003, pages 142–147, 2003. URL https://www.aclweb.org/anthology/W03-0419.
[130] Adam Trischler, Tong Wang, Xingdi Yuan, Justin Harris, Alessandro Sordoni, Philip Bachman, and Kaheer
Suleman. NewsQA: A machine comprehension dataset. In Proceedings of the 2nd Workshop on Representation
Learning for NLP, pages 191–200, Vancouver, Canada, August 2017. Association for Computational Linguistics.
doi: 10.18653/v1/W17-2623. URL <https://www.aclweb.org/anthology/W17-2623>.
[131] Clara Vania, Ruijie Chen, and Samuel R. Bowman. Asking Crowdworkers to Write Entailment Examples:
The Best of Bad options. In Proceedings of the 1st Conference of the Asia-Paciﬁc Chapter of the Association
for Computational Linguistics and the 10th International Joint Conference on Natural Language Processing,
pages 672–686, Suzhou, China, December 2020. Association for Computational Linguistics. URL https:
//www.aclweb.org/anthology/2020.aacl-main.68.
70

--- Page 71 ---

[132] Alex Wang, Yada Pruksachatkun, Nikita Nangia, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, and
Samuel Bowman. SuperGLUE: A stickier benchmark for general-purpose language understanding systems. In
H. Wallach, H. Larochelle, A. Beygelzimer, F. d'Alché-Buc, E. Fox, and R. Garnett, editors, Advances in Neural
Information Processing Systems, volume 32. Curran Associates, Inc., 2019. URL https://proceedings.
neurips.cc/paper/2019/file/4496bf24afe7fab6f046bf4923da8de6-Paper.pdf.
[133] Alex Wang, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, and Samuel R. Bowman. GLUE: A
multi-task benchmark and analysis platform for natural language understanding. In International Conference on
Learning Representations, 2019. URL https://openreview.net/forum?id=rJ4km2R5t7.
[134] Alex Warstadt, Amanpreet Singh, and Samuel R. Bowman. Neural network acceptability judgments. Transactions
of the Association for Computational Linguistics, 7:625–641, March 2019. doi: 10.1162/tacl_a_00290. URL
https://www.aclweb.org/anthology/Q19-1040.
[135] Tsung-Hsien Wen, David Vandyke, Nikola Mrkši´c, Milica Gaši´c, Lina M. Rojas-Barahona, Pei-Hao Su, Stefan
Ultes, and Steve Young. A network-based end-to-end trainable task-oriented dialogue system. In Proceedings
of the 15th Conference of the European Chapter of the Association for Computational Linguistics: Volume 1,
Long Papers, pages 438–449, Valencia, Spain, April 2017. Association for Computational Linguistics. URL
https://www.aclweb.org/anthology/E17-1042.
[136] Guillaume Wenzek, Marie-Anne Lachaux, Alexis Conneau, Vishrav Chaudhary, Francisco Guzmán, Armand
Joulin, and Edouard Grave. CCNet: Extracting high quality monolingual datasets from web crawl data. In
Proceedings of the 12th Language Resources and Evaluation Conference, pages 4003–4012, Marseille, France,
May 2020. European Language Resources Association. ISBN 979-10-95546-34-4. URL https://www.aclweb.
org/anthology/2020.lrec-1.494.
[137] Bryan Wilie, Karissa Vincentio, Genta Indra Winata, Samuel Cahyawijaya, Xiaohong Li, Zhi Yuan Lim, Sidik
Soleman, Rahmad Mahendra, Pascale Fung, Syafri Bahar, and Ayu Purwarianti. IndoNLU: Benchmark and
resources for evaluating Indonesian natural language understanding. In Proceedings of the 1st Conference of
the Asia-Paciﬁc Chapter of the Association for Computational Linguistics and the 10th International Joint
Conference on Natural Language Processing, pages 843–857, Suzhou, China, December 2020. Association for
Computational Linguistics. URL https://www.aclweb.org/anthology/2020.aacl-main.85.
[138] Adina Williams, Nikita Nangia, and Samuel Bowman. A broad-coverage challenge corpus for sentence under-
standing through inference. In Proceedings of the 2018 Conference of the North American Chapter of the Associ-
ation for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers), pages 1112–1122,
New Orleans, Louisiana, June 2018. Association for Computational Linguistics. doi: 10.18653/v1/N18-1101.
URL https://www.aclweb.org/anthology/N18-1101.
[139] Thomas Wolf, Lysandre Debut, Victor Sanh, Julien Chaumond, Clement Delangue, Anthony Moi, Pierric
Cistac, Tim Rault, Remi Louf, Morgan Funtowicz, Joe Davison, Sam Shleifer, Patrick von Platen, Clara Ma,
Yacine Jernite, Julien Plu, Canwen Xu, Teven Le Scao, Sylvain Gugger, Mariama Drame, Quentin Lhoest,
and Alexander Rush. Transformers: State-of-the-art natural language processing. In Proceedings of the 2020
Conference on Empirical Methods in Natural Language Processing: System Demonstrations, pages 38–45,
Online, October 2020. Association for Computational Linguistics. doi: 10.18653/v1/2020.emnlp-demos.6. URL
https://www.aclweb.org/anthology/2020.emnlp-demos.6.
[140] Chien-Sheng Wu, Andrea Madotto, Ehsan Hosseini-Asl, Caiming Xiong, Richard Socher, and Pascale Fung.
Transferable multi-domain state generator for task-oriented dialogue systems. In Proceedings of the 57th Annual
Meeting of the Association for Computational Linguistics, pages 808–819, Florence, Italy, July 2019. Association
for Computational Linguistics. doi: 10.18653/v1/P19-1078. URL https://www.aclweb.org/anthology/
P19-1078.
[141] Jingjing Xu, Ji Wen, Xu Sun, and Qi Su. A discourse-level named entity recognition and relation extraction
dataset for Chinese literature text. arXiv preprint arXiv:1711.07010, 2017.
[142] Liang Xu, Hai Hu, Xuanwei Zhang, Lu Li, Chenjie Cao, Yudong Li, Yechen Xu, Kai Sun, Dian Yu,
Cong Yu, Yin Tian, Qianqian Dong, Weitang Liu, Bo Shi, Yiming Cui, Junyi Li, Jun Zeng, Rongzhao
Wang, Weijian Xie, Yanting Li, Yina Patterson, Zuoyu Tian, Yiwen Zhang, He Zhou, Shaoweihua Liu,
Zhe Zhao, Qipeng Zhao, Cong Yue, Xinrui Zhang, Zhengliang Yang, Kyle Richardson, and Zhenzhong
Lan. CLUE: A Chinese language understanding evaluation benchmark. In Proceedings of the 28th Inter-
national Conference on Computational Linguistics, pages 4762–4772, Barcelona, Spain (Online), December
71

--- Page 72 ---

2020. International Committee on Computational Linguistics. doi: 10.18653/v1/2020.coling-main.419. URL
https://www.aclweb.org/anthology/2020.coling-main.419.
[143] Yi Yang, Wen-tau Yih, and Christopher Meek. WikiQA: A challenge dataset for open-domain question answering.
In Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing, pages 2013–2018,
Lisbon, Portugal, September 2015. Association for Computational Linguistics. doi: 10.18653/v1/D15-1237.
URL https://www.aclweb.org/anthology/D15-1237.
[144] Yinfei Yang, Yuan Zhang, Chris Tar, and Jason Baldridge. PAWS-X: A cross-lingual adversarial dataset for
paraphrase identiﬁcation. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language
Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP),
pages 3687–3692, Hong Kong, China, November 2019. Association for Computational Linguistics.
doi:
10.18653/v1/D19-1382. URL https://www.aclweb.org/anthology/D19-1382.
[145] Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio, William Cohen, Ruslan Salakhutdinov, and Christopher D.
Manning. HotpotQA: A dataset for diverse, explainable multi-hop question answering. In Proceedings of the
2018 Conference on Empirical Methods in Natural Language Processing, pages 2369–2380, Brussels, Belgium,
October-November 2018. Association for Computational Linguistics. doi: 10.18653/v1/D18-1259. URL
<https://www.aclweb.org/anthology/D18-1259>.
[146] Zhilin Yang, Zihang Dai, Yiming Yang, Jaime Carbonell, Russ R Salakhutdinov, and Quoc V Le. XLNet:
Generalized autoregressive pretraining for language understanding. In H. Wallach, H. Larochelle, A. Beygelz-
imer, F. d'Alché-Buc, E. Fox, and R. Garnett, editors, Advances in Neural Information Processing Systems,
volume 32. Curran Associates, Inc., 2019. URL https://proceedings.neurips.cc/paper/2019/file/
dc6a7e655d7e5840e66733e9ee67cc69-Paper.pdf.
[147] Yuan Yao, Deming Ye, Peng Li, Xu Han, Yankai Lin, Zhenghao Liu, Zhiyuan Liu, Lixin Huang, Jie Zhou, and
Maosong Sun. DocRED: A large-scale document-level relation extraction dataset. In Proceedings of the 57th
Annual Meeting of the Association for Computational Linguistics, pages 764–777, Florence, Italy, July 2019.
Association for Computational Linguistics. doi: 10.18653/v1/P19-1074. URL https://www.aclweb.org/
anthology/P19-1074.
[148] Peter Young, Alice Lai, Micah Hodosh, and Julia Hockenmaier. From image descriptions to visual denotations:
New similarity metrics for semantic inference over event descriptions. Transactions of the Association for
Computational Linguistics, 2:67–78, 2014. doi: 10.1162/tacl_a_00166. URL https://www.aclweb.org/
anthology/Q14-1006.
[149] Dian Yu, Kai Sun, Claire Cardie, and Dong Yu. Dialogue-based relation extraction. In Proceedings of the
58th Annual Meeting of the Association for Computational Linguistics, pages 4927–4940, Online, July 2020.
Association for Computational Linguistics. doi: 10.18653/v1/2020.acl-main.444. URL https://www.aclweb.
org/anthology/2020.acl-main.444.
[150] Sheng Zhang, Xiaodong Liu, Jingjing Liu, Jianfeng Gao, Kevin Duh, and Benjamin Van Durme. ReCoRD: Bridg-
ing the gap between human and machine commonsense reading comprehension. arXiv preprint arXiv:1810.12885,
2018.
[151] Xiang Zhang, Junbo Zhao, and Yann LeCun. Character-level convolutional networks for text classiﬁcation.
In C. Cortes, N. Lawrence, D. Lee, M. Sugiyama, and R. Garnett, editors, Advances in Neural Information
Processing Systems, volume 28. Curran Associates, Inc., 2015. URL https://proceedings.neurips.cc/
paper/2015/file/250cf8b51c773f3f8dc8b4be867a9a02-Paper.pdf.
[152] Yuan Zhang, Jason Baldridge, and Luheng He. PAWS: Paraphrase adversaries from word scrambling. In
Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational
Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), pages 1298–1308, Minneapolis,
Minnesota, June 2019. Association for Computational Linguistics. doi: 10.18653/v1/N19-1131. URL https:
//www.aclweb.org/anthology/N19-1131.
[153] Yuhao Zhang, Victor Zhong, Danqi Chen, Gabor Angeli, and Christopher D. Manning. Position-aware attention
and supervised data improve slot ﬁlling. In Proceedings of the 2017 Conference on Empirical Methods in Natural
Language Processing, pages 35–45, Copenhagen, Denmark, September 2017. Association for Computational
Linguistics. doi: 10.18653/v1/D17-1004. URL https://www.aclweb.org/anthology/D17-1004.
72

--- Page 73 ---

[154] Qi Zhu, Kaili Huang, Zheng Zhang, Xiaoyan Zhu, and Minlie Huang. CrossWOZ: A large-scale Chinese cross-
domain task-oriented dialogue dataset. Transactions of the Association for Computational Linguistics, 8:281–295,
2020. doi: 10.1162/tacl_a_00314. URL https://www.aclweb.org/anthology/2020.tacl-1.19.
73

--- Page 74 ---

Index
ACROFAN (Acrofan News), 10
AIRBNB (Airbnb Reviews), 10
CC-100-Kor, 50
DP (Dependency Parsing), 33
DST (Dialogue State Tracking), 44
KLUE
(Korean Language Understanding Evaluation), 4
KLUE-BERT, 50
KLUE-DP, 36
KLUE-MRC, 43
KLUE-NER, 27
KLUE-NLI, 24
KLUE-RE, 32
KLUE-RoBERTa, 50
KLUE-STS, 19
MODU (Modu Corpus), 50
MRC (Machine Reading Comprehension), 37
NAMUWIKI, 50
NER (Named Entity Recognition), 25
NEWSCRAWL, 50
NLI (Natural Language Inference), 20
NSMC (NAVER Sentiment Movie Corpus), 10
PARAKQC, 10
PETITION, 50
POLICY (Policy News), 10
RE (Relation Extraction), 28
STS (Semantic Textual Similarity), 16
TC (Topic Classiﬁcation), 13
The Korea Economy Daily, 10
WIKINEWS, 10
WIKIPEDIA, 10
WIKITREE, 10
WoS (Wizard of Seoul, KLUE-DST), 49
YNA (Yonhap News Agency), 10
YNAT (YNA Topic Classiﬁcation, KLUE-TC), 15
74

--- Page 75 ---

Contribution
Sungjoon Park led the project as project manager, initiated the project, made decisions on overall progress of this project, secured
ﬁnancial resources, signed up with ACROFAN for the articles, and organized IRB submission and research paper.
Jihyung Moon led the project as project manager, managed overall datasets, models, and ethical concerns, signed up with ACROFAN
for the articles, prepared IRB, as well as contributed to NER, STS, NLI, MRC dataset constructions, AIRBNB, POLICY corpora
collection, and leaderboard design.
Sungdong Kim managed overall ﬁne-tuning of language models, served as a person in charge (PIC) of DST, and contributed to the
dataset construction of TC, STS, and RE.
Won Ik Cho managed the overall dataset construction of TC, STS, NLI, RE, MRC, and DST, provided the original corpus of
PARAKQC, and served as a PIC of STS.
Jiyoon Han managed the overall dataset construction of DP and NER, served as a PIC of NLI, contributed to the dataset construction
of STS, and took part in preparing IRB.
Jangwon Park served as a PIC of model pretraining, contributed to the text collection of YNA, collected and pre-processed MODU,
CC-100-Kor, NAMUWIKI, NEWSCRAWL, and PETITION, and conducted the ﬁne-tuning of TC.
Chisung Song served as a PIC of NER and contributed to the dataset construction of DP and DST.
Junseong Kim served as a PIC of MRC, conducted the ﬁne-tuning of MRC, and contributed to the text collection of WIKITREE
and WIKIPEDIA.
Youngsook Song served as a PIC of TC and contributed to the dataset construction of NER and DST.
Taehwan Oh served as a PIC of DP, contributed to the dataset construction of NER and NLI, and took part in preparing IRB.
Joohong Lee served as a PIC of RE, and conducted the ﬁne-tuning of RE.
Juhyun Oh contributed to the dataset construction of NLI, NER, DP and STS, took part in ethical considerations, IRB preparation
and setup for model pretraining.
Sungwon Lyu contributed to the dataset construction of STS, NLI, RE, and MRC, taking part in the overall model pretraining and
task-wise ﬁne-tuning.
Younghoon Jeong contributed to the text collection of WIKINEWS, modeling of DP, and pre-processing of the pretraining corpus.
Inkwon Lee contributed to the text collection, modeling of DP and pre-processing of the pretraining corpus.
Sangwoo Seo contributed to the dataset construction of RE, and took part in preparing IRB.
Dongjun Lee contributed to the construction of the ﬁne-tuning pipeline and the modeling of STS.
Hyunwoo Kim contributed to the dataset construction of MRC, and took part in preparing IRB.
Myeonghwa Lee contributed to the dataset construction of STS and TC.
Seongbo Jang contributed to the dataset construction of RE, and took part in preparing IRB.
Seungwon Do contributed to the dataset construction of DST and text collection.
Sunkyoung Kim contributed to the dataset construction of RE and MRC, and modeling of MRC.
Kyungtae Lim contributed to the dataset construction of DP.
Jongwon Lee contributed to the dataset construction and modeling of DST.
Kyumin Park contributed to the dataset construction of DST, and took part in preparing IRB.
Jamin Shin contributed to the dataset construction of DST.
Seonghyun Kim contributed to the dataset construction and modeling of NER.
Lucy Park contributed to the dataset construction of MRC and provided the original corpus of NSMC.
Alice Oh advised the project, sponsored the project via KAIST, provided feedback and suggested better way to improve the quality
of our dataset and models, and helped with the ﬁnal manuscript.
Jung-Woo Ha advised the project, sponsored annotation cost and computing cloud credits the project via NAVER, provided
license-free news articles from The Korea Economy Daily, and helped with the ﬁnal manuscript.
Kyunghyun Cho advised the project, provided critical feedback, suggested better way to improve the quality of our dataset and
models, and helped a lot with polishing and rewriting the ﬁnal manuscript.
All participants contributed to this manuscript.
75

--- Page 76 ---

A
Dev Set Results
Table 36: Performances of our pretrained LMs and other baselines on KLUE benchmark dev set. The notations are
same with Table 32.
YNAT
KLUE-STS
KLUE-NLI
KLUE-NER
KLUE-RE
KLUE-DP
KLUE-MRC
WoS
Model
F1
RP
F1
ACC
F1E
F1C
F1mic
AUC
UAS
LAS
EM
ROUGE
JGA
F1S
mBERTBASE
82.64
82.97
75.93
72.90
75.56
88.81
58.39
56.41
88.53
86.04
49.96
55.57
35.27
88.60
XLM-RBASE
84.52
88.88
81.20
78.23
80.48
92.14
57.62
57.05
93.12
87.23
26.76
53.36
41.54
89.81
XLM-RLARGE
87.30
93.08
87.17
86.40
82.18
93.20
58.75
63.53
92.87
87.82
35.23
66.55
42.44
89.88
KR-BERTBASE
85.36
87.50
77.92
77.10
74.97
90.46
62.83
65.42
92.87
87.13
48.95
58.38
45.60
90.82
KoELECTRABASE
85.99
93.14
85.89
86.87
86.06
92.75
62.67
57.46
90.93
87.07
59.54
65.64
39.83
88.91
KLUE-BERTBASE
86.95
91.01
83.44
79.87
83.71
91.17
65.58
68.11
93.07
87.25
62.42
68.15
46.72
91.59
KLUE-RoBERTaSMALL
85.95
91.70
85.42
81.00
83.55
91.20
61.26
60.89
93.47
87.50
58.28
63.56
46.65
91.50
KLUE-RoBERTaBASE
86.19
92.91
86.78
86.30
83.81
91.09
66.73
68.11
93.75
87.77
69.56
74.64
47.41
91.60
KLUE-RoBERTaLARGE
85.88
93.20
86.13
89.50
84.54
91.45
71.06
73.33
93.84
87.93
75.26
80.30
49.39
92.19
In order to prevent early saturation of KLUE benchmark, we limit users to submit their models once per day. We thus present the dev
set results to provide a reference for future work and local tests, in Table 36. Models we used are same as in test set.
76

```
