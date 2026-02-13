---
title: "2025-Davies-Overview of the NLPCC 2025 Shared Task Gender Bias Mitigation - PDF Extract"
source_pdf: "2025-Davies-Overview of the NLPCC 2025 Shared Task Gender Bias Mitigation.pdf"
pages: 13
extracted_at: "2026-02-13T13:57:13.176091"
---

# PDF Extract: 2025-Davies-Overview of the NLPCC 2025 Shared Task Gender Bias Mitigation

**Source PDF:** 2025-Davies-Overview of the NLPCC 2025 Shared Task Gender Bias Mitigation.pdf
**Total Pages:** 13

---

## Content

```
--- Page 1 ---

arXiv:2506.12574v1  [cs.CL]  14 Jun 2025
Overview of the NLPCC 2025 Shared Task: Gender Bias
Mitigation Challenge
Yizhi Li1,2, Ge Zhang1, Hanhua Hong2, Yiwen Wang3, and Chenghua Lin2
1 Multimodal Art Projection Research Community
2 University of Manchester
3 Independent Researcher
Abstract. As natural language processing for gender bias becomes a significant
interdisciplinary topic, the prevalent data-driven techniques, such as pre-trained
language models, suffer from biased corpus. This case becomes more obvious
regarding those languages with less fairness-related computational linguistic re-
sources, such as Chinese. To this end, we propose a Chinese cOrpus foR Gender
bIas Probing and Mitigation (CORGI-PM), which contains 32.9k sentences with
high-quality labels derived by following an annotation scheme specifically devel-
oped for gender bias in the Chinese context. It is worth noting that CORGI-PM con-
tains 5.2k gender-biased sentences along with the corresponding bias-eliminated
versions rewritten by human annotators. We pose three challenges as a shared task
to automate the mitigation of textual gender bias, which requires the models to
detect, classify, and mitigate textual gender bias. In the literature, we present the
results and analysis for the teams participating this shared task in NLPCC 2025.
Keywords: Bias Mitigation · Bias Detection · Fairness for Chinese Corpus.
1
Introduction
There is a growing consensus that the identification and prevention of toxic gender
attitudes and stereotypes are of vital importance for society [3]. Given that gender-
biased information can be presented and disseminated extensively in textual form, it is
of paramount significance to develop automatic approaches for detecting and alleviat-
ing textual gender bias. As the blooming of open-source models and training corpus
[12,2,43,33,41], Natural language processing (NLP) community has found extensive
applications in text-related scenarios and has exerted a considerable influence on gender
bias issues [7]. On one hand, pre-trained language models (LMs), which serve as a cru-
cial technique in modern NLP, have been demonstrated to absorb the subjective gender
bias present in the internet-wise training corpus and even have the potential to amplify
it [45,17,34,10]. On the other hand, the application of cutting-edge NLP techniques
for exploring and mitigating gender bias holds increasing promise. This status in quo
necessitates the construction of high-quality corpora to facilitate the research for gender
bias mitigation.
Building a high-quality text corpus has been one of the key tangents in improving
NLP applications for debiasing gender stereotypes in texts [31]. Some researchers
introduce automatic annotation techniques, such as gender-swapped based methods, to

--- Page 2 ---

2
Y. Li et al.
Language
Models
Gender-related 
Vocabulary
Polarity
Calculation
Word
Matching
Sentence-level
Reranking
Potentially
Biased Corpus
Corpus with
Biased Vocabulary
Raw Corpus
Fig. 1: Pipeline of Retrieving and Filtering Potentially Biased Sentences Candidate Pool
from Raw Corpus for Human Annotation.
create corpora for gender bias mitigation [20,47,27]. While it is attractive to build a
large-scale corpus without heavy labor, automatic gender-swapped based methods highly
depend on the quality of base language models and are prone to creating nonsensical
sentences [31]. To address this issue, some works devote effort to developing human-
annotated corpora for gender bias mitigation. However, these corpora either mainly
focus on word- or grammar-level bias [37,50,28,49], without considering the nuanced
biases appearing in specific contexts. Or some of the corpora concentrate only on sexism-
related topics [23,6,5,13]. Moreover, existing works on gender bias exclusively focus
on English [7], where few datasets exist for other influential languages such as Chinese.
We aim to tackle the aforementioned issues by providing a high-quality Chinese corpus
for contextual-level gender bias probing and mitigation with a hybrid pipeline including
automatic corpus filtering and human annotation.
To this end, we propose the Chinese cOrpus foR Gender bIas Probing and Mitigation
(CORGI-PM) dataset, which consists of 32.9k human-annotated sentences, including
both gender-biased and non-biased samples. To construct the initial candidate pool for
further processing, we propose an automatic method to build a potentially gender-biased
sentence set from existing large-scale Chinese corpora, as illustrated in Fig. 1. Inspired by
the metric leveraging language models for gender bias score calculation proposed in [4],
the samples containing words of high gender bias scores are first recalled at this stage.
Following the retrieval, the samples are then reranked and filtered according to their
sentence-level gender-biased probability [14]. After the candidate pool construction, we
select human annotators with qualified educational backgrounds and design an annotation
scheme to label the acquired sentences.
During the annotation, the candidates are classified into biased and non-biased
classes, and the biased samples are further categorized into three fine-grained categories
considering their contexts. To facilitate research in bias mitigation research, we also

--- Page 3 ---

Overview of the NLPCC 2025 Shared Task: Gender Bias Mitigation Challenge
3
require the annotators to paraphrase the biased sentences into gender-neutral ones while
maintaining invariant semantics to build a parallel subset corpus. Based on the labeled
corpus, we further pose three challenges in CORGI-PM, i.e., gender bias detection, clas-
sification, and mitigation, which come with clear definitions and evaluation protocols
for NLP tasks in gender bias probing and mitigation. In order to provide referential
baselines and benchmarks for our proposed challenges, we conduct random data splitting
with balanced labels and implement experiments on pre-trained language models in
zero-shot, in-context learning, and fine-tuning paradigms. We discuss the experimental
settings and provide result analysis in §5.
In summary, we provide a well-annotated Chinese corpus for gender bias probing
and mitigation, along with clearly defined corresponding challenges. With a properly
designed annotation scheme, CORGI-PM provides a corpus of high quality that assists
models in detecting gender bias in texts. More importantly, other than the 22.5k human-
annotated non-biased samples, all the 5.2k biased sentences in our corpus are further
labeled with gender bias subclasses and companies with parallel bias-free versions
provided by the annotators4.
2
Related Work
Gender Bias Corpus.
High-quality gender bias corpus, especially contextual-level
gender bias corpus, is significant for mitigating gender bias contained in language
models, but hard to collect. Previous research work widely uses gender-swapping to
build a corpus for evaluation or mitigate gender bias in LMs [46,16]. Metrics and corpus
are introduced to measure gender bias in abusive languages as well [13,24,9]. Word-level
Chinese gender bias corpora have been proposed about adjectives [51], and careers [30].
[46] also shares an automatically constructed Chinese sentence-level gender-unbiased
data set. In sharp contrast, CORGI-PM is the first human-annotated Chinese gender bias
detection dataset, one of the rare gender bias classification datasets [24], and the first
human-annotated gender-bias correction dataset.
Bias Detection and Correction.
Different Gender Bias Evaluation Testsets(GBETs)
have been designed to automatically evaluate models trained for specific tasks for gender
bias [32,16,38]. Word-swapping is the most widely used technique for gender bias
correction and widely used to mitigate the gender bias in hate-speech [25], regional bias
mitigation[18], knowledge graph [21], sentiment analysis [16], and the general language
model [45]. As a comparison, CORGI-PM serves as a manual standard dataset for testing
LMs’ ability to measure and mitigate gender bias.
3
Data Collection
3.1
Sample Filtering
We propose an automatic processing method to recall, rerank, and filter annotation
candidates from raw corpora using a two-stage filtering from word-level to sentence-
4 To eliminate the data contamination, we additionally provide 100 samples for each task in
addition to the original splits [42].

--- Page 4 ---

4
Y. Li et al.
Sample
Quantity
Category
Train Valid Test
Biased
AC
1.90k 235
237
DI
2.70k 334
337
ANB
2.47k 306
309
Non-biased 21.4k 516
526
Overall
30.1k 1391 1409
Table 1: Overall Statistics of the CORGI-PM Dataset. The notations, AC, DI, and ANB
represent specific bias labels described in § 3.2.
level, as illustrated in Fig. 1. The Chinese sentence samples are mainly screened out from
the SlguSet [48] and the CCL corpus [39]. To recall gender-biased words or retrieve
candidate sentences with gender bias scores, we compare the target word/sentence
representations with the seed direction, which can be calculated by the subtraction
between the word embeddings of she and he [4,14]. We leverage different Chinese LMs
including ERNIE [44], CBert [8], and Chinese word vectors [26] to acquire the word-
level and sentence-level representations. For word-level filtering, we use the mentioned
metric to build a vocabulary of high bias scores and recall sentences containing such
words from the raw corpora with exact matches. We compute gender bias scores of the
crawled sentences and group them by the gender bias keywords acquired in the previous
stage for sentence-level filtering. The final sentences for annotation are then selected
according to a specific global threshold score and an in-group threshold rank.
Linguistic
Non-biased
Biased
Corrected Biased
Info.
Train
Valid
Test
Train
Valid
Test
Train
Valid
Test
Word
724k
18.9k
17.7k
228k
24.8k
28.3k
265k
27.1k
30.0k
Dictionary
574k
14.4k
14.1k
167k
18.4k
20.4k
191k
19.9k
21.5k
Character
1,156k 30.1k
28.1k
358k
39.2k
44.4k
417k
42.8k
46.9k
Sent. Length 53.952 58.397 53.473 85.837 76.087 85.214 99.839 82.853 89.939
Table 2: Linguistic Characteristics of the Corpus. Word, Dictionary, and Character
separately denote the total Chinese word number, total unique Chinese word number,
and total character number of the specific categories. The sentence lengths are defined as
the number of containing characters.
3.2
Annotation Scheme
The annotation scheme is designed for gender bias probing and mitigation. For gender
bias probing, the annotators are required to provide the following information given a
sentence: whether gender bias exists; if so, how the bias is established. For gender bias
mitigation, the corrected non-biased version of the biased sentences is also required. We
further describe the annotation scheme details in the following paragraphs.

--- Page 5 ---

Overview of the NLPCC 2025 Shared Task: Gender Bias Mitigation Challenge
5
Existence and Categorization. The annotators are required to annotate whether the
sentence is gender-biased (B) or non-biased (N) in contextual-level or word-level, and
further clarify how the bias is established. Given that our raw data is collected using
gender-related keywords or from gender-related corpus, the samples annotated without
gender bias are useful human-annotated negative samples for detecting gender bias. To
additionally provide information about gender bias categorization, we classify gender
bias types into three subtypes : (1) Gender Stereotyped activity and career choices (AC);
(2) Gender Stereotyped descriptions and inductions (DI); and (3) Expressed gender-
stereotyped attitudes, norms and beliefs (ANB). The classification standard is inspired
by [15] and further summed up into the mentioned subtypes.
Bias Mitigation. Annotators are further required to mitigate the gender bias of selected
sentences while keeping the original semantics. We also ask our annotators to diversify
the expressions if applicable. The major revision patterns can be summarized as follows:
(1). Replace the gender-specific pronouns with neutral pronouns. (2). Replace the gender-
specific adjectives with neutral descriptions with similar semantics definitions. (3). Add
additional comments to neutralize the sentences that cannot be directly mitigated.
As shown in Fig. 2, the three mitigation revision patterns could cover various cases
in the selected sentences. These three major mitigation annotation patterns are not used
exclusively in the annotation but can be used in combination. Except for the three
mentioned patterns, we require the annotators to apply several other linguistic skills to
cover corner cases, including deleting gender-specific pronouns and replacing vehicles
in gender-related metaphors.
4
CORGI-PM Corpus Analysis
In this section, we report the linguistic statistics of CORGI-PM as Tab. 1. We conduct
a balanced splitting to create the valid and test set considering the negative-positive
ratio and bias subclass proportion in the global distribution. As revealed in Tab. 25,
we observe two major differences between the biased sentences and the corresponding
human debiased ones: the debiased are usually longer and have more diverse expressions,
revealed by the sentence length and the vocabulary size metrics. Except for the samples
debiased with additional neutralization comments, we hypothesize that it is due to human
annotators’ intention to keep the semantic information unchanged and the sentence
coherent while mitigating gender bias. In this case, they may use more conjunctions and
longer descriptions compared to some gender-biased inherent expressions.
Quality Monitoring and Control. We used a standardized operating method and educated
our annotators to achieve high-quality annotations as follows:
(1). Annotators
We have 6 annotators, which were all native speakers of Chinese.
Annotators were only qualified to do the annotation if they went through several societal
[15,40] and computer science research works [31,47] about gender bias before the
annotation procedure. All annotators held a bachelor’s degree. [36] points out that expert
annotators are more cautious and can improve the corpus quality with a large margin,
5 We use the Jieba (https://github.com/fxsjy/jieba) to parse.

--- Page 6 ---

6
Y. Li et al.
Original Sentence
Edit Sentence
清洁阿姨一边扫地一边赞扬。
清洁工一边扫地一边赞扬。
(The cleaning woman praised while
sweeping the floor.)
(The cleaners praised while sweeping the
floor.)
我，有时文静，有时却调皮得像一个男孩
。
我，有时文静，有时调皮。
(I, sometimes quiet, but sometimes
naughty like a boy.)
(I, sometimes quiet, sometimes naughty.)
在小王眼里，李某高大帅气、温柔体贴，
而且风趣幽默，是一个十分优质的青年男
性。
在小王眼里，李某身材高大、外表好看、温
柔体贴，而且风趣幽默，是一个十分优质的
青年。
(In the eyes of Wang, Li is tall and
handsome, gentle and considerate, and
funny, a very high-quality young
male.)
(In the eyes of Wang, Li is tall, good-
looking, caring and gentle, and funny, a
very high-quality young people.)
沙峰起伏，金光灿灿，宛如一座金山，像
绸缎一样柔软，少女一样娴静。
沙峰起伏，金光灿灿，宛如一座金山，像绸
缎一样柔软，宁静。
(The sandy peaks are undulating and
golden, like a golden mountain, as
soft as silk and as serene as a
maiden.)
(The sandy peaks are undulating and
golden, like a golden mountain, as soft
and serene as silk.)
我想要世界，而世界当时属于男人们。
我想要世界，而世界当时属于男人们。评:
世界应当属于人们，与男女无关。
(I want the world, and the world then
belonged to the men.)
(I wanted the world, and the world then
belonged to the men. Comment: The
world should belong to people, not to
men and women.)
哎哟，果然每个追梦男人的背后，都有个
不世俗的后方！
哎哟，果然每个追梦男人的背后，都有个不
世俗的后方！评: 这种感慨是错误的，将男
女的家庭分工固定化，剥除女性就业的权
利，应予以鄙弃。
(Oops, indeed, behind every dream-
chasing man, there is an
unsophisticated back!)
(Oops, indeed, behind every dream-
chasing man, there is an unsophisticated
back! Comment: This is a wrong feeling
that fixes the domestic division of labor
between men and women and strips
women of their employment rights,
which should be despised.)
Change the
Pronoun
Change the
Gender-
specific
Adjectives
Add
Comments
Fig. 2: Case Study of Mitigation Annotation Patterns.
which proves the necessity of our training procedure. We also kept the number of male
and female annotators equal.
(2). Gender Equality of Raw Corpus
In the raw data collection procedure, we
keep the number of man-related keywords and woman-related keywords equal and make

--- Page 7 ---

Overview of the NLPCC 2025 Shared Task: Gender Bias Mitigation Challenge
7
the number of samples recalled according to different keywords balanced. As a result,
the raw data and the final data should hold gender equality.
(3). Annotation Procedure
Our annotation procedure is separated into two stages.
In the first stage, annotators are encouraged to not enter any samples that they are not
certain about. In the second stage, we have annotators cross-checking annotations. We
did not enter any contradictory samples.
(4). Inter-annotator Agreement
Given the domain and purpose of the dataset,
we want to build the dataset as high quality as possible. After an initial annotation round
with 6 annotators, we also report inter-annotator agreement in Tab. 3. to verify annotation
reliability, where the IAA among three annotators on bias classification, detection, and
mitigation is 0.802, 0.935, and 0.987, respectively.
Classification Detection Mitigation
IAA
0.802
0.935
0.987
Table 3: Inter-Annotator Agreement (IAA)
Word Cloud Analysis. We provide word cloud analysis of Ernie and Chinese-Electra in
the section about adjectives and career words. More available word cloud analysis will
be available in our public repository. The words are ranked according to the absolute
value of their gender bias score calculated along the method used by [4,14]. There is a
noticeable word-level gender stereotype according to the word cloud. For example, a
man is robust and a woman is motherly, a man is suitable for a fitness instructor and a
woman is suitable for a choreographer. We also conduct word cloud analysis for language
models pre-trained by different corpora.
5
Derived Gender Bias Mitigation Challenges
To provide a clear definition for automatic textual gender bias probing and mitigation
tasks, we propose corresponding challenges and standardize the evaluation protocols. We
address two tasks, bias detection and classification, for gender bias probing to evaluate
how well the language models can distinguish the biased contexts. Furthermore, we
formalize the gender mitigation challenge as a sentence correction task to benchmark
the bias mitigation ability of the language models.
5.1
Challenges of Detection and Classification
Definition. We regard both the gender bias detection and classification challenges
as supervised classification tasks and evaluate them with metrics of consensus. The
gender bias detection challenge can be regarded as a binary classification task, where
the model is required to predict the probability that a given sentence contains gender
bias. As described in § 3.2, biased samples are further categorized into one or more
kinds. Therefore, we can address the gender classification challenge as a multi-label
classification task. The precision, recall, and F1-score are selected as the main metrics in

--- Page 8 ---

8
Y. Li et al.
these two challenges. Class-wise metrics and macro average summarized evaluation are
required through both valid and test sets to show the performance of language models.
Experiment Settings. Then we use the test sets to perform a classification query on the
saved file. The processing time for the classification of gender bias is approximately 1
hour. We calculated the precision, recall, and F1 score to analyze model performance.
We test the performance on both "yes" and "no" detection.
5.2
Challenge of Mitigation
Task
Team
Performance
Detection
ZZU-NLP
.850
ZZU-NLP_DS
.741
Cloud Lab
.720
YNU-HPCC
.714
Prompt
.712
MAP-Neo
.653
Classification
ZZU-NLP
.646
Team0071
.548
Hu
.531
MAP-Neo
.526
YNU-HPCC
.509
Prompt
.505
Mitigation
ZZU-NLP
.294
Team0071
.293
YNU-HPCC
.293
Prompt
.288
IR901
.271
MAP-Neo
.091
Overall
ZZU-NLP
.597
YNU-HPCC
.505
Prompt
.502
Cloud Lab
.479
ZZU-NLP_DS
.472
MAP-Neo
.423
Table 4: The leaderboards for all tasks. Our
baseline model is underscored.
Definition. The gender bias mitigation
challenge can be regarded as a sentence
correction task, where the model is re-
quired to generate a non-biased version of
a biased sentence. As a natural language
generation task, the model outputs could
be evaluated by N-gram based metrics.
Experiment Settings. Regarding the de-
cision on evaluation metrics, we conduct
extensive human evaluations on the de-
biased sentences considering both gen-
der bias and coherence aspects. In human
evaluation, we shuffle the debiased writ-
ten by humans and different models, and
asked annotators to grade the results us-
ing the answer range from 1-not at all
to 7-extremely gender biased/extremely
fluent without providing the information
of the source. Additionally, we use auto-
mated reference-based metrics to evaluate
the bias mitigated sentences [29], includ-
ing BLEU [22], ROUGE-L [19], and ME-
TEOR [1].
6
Leaderboard
Table 4 presents the leaderboards for all
the tasks, listing only the top-performing
teams and our baseline model MAP-Neo.
For each task, a representative evaluation
metric is selected to compare model per-
formance across teams. Specifically, for
the detection and classification tasks—both formulated as binary classification prob-
lems—the F1 score is used as the primary performance metric. For the mitigation task,

--- Page 9 ---

Overview of the NLPCC 2025 Shared Task: Gender Bias Mitigation Challenge
9
model performance is assessed using the average of BLEU, METEOR, and ROUGE-L
F1 scores. An overall ranking is then derived by averaging each team’s scores across
the three tasks. The results demonstrate that Team ZZU-NLP achieved the highest
performance in all three tasks, thereby securing the top overall position in the shared
task.
Notably, while many teams achieved strong results in the detection task, performance
declined considerably in the classification task, with some models even falling below the
baseline. Furthermore, the performance remain consistently low across all submissions
for the mitigation task. This performance discrepancy supports the validity of our step-
wise three-task framework, which introduces increasing complexity in a reasonable and
structured difficulty progression. Furthermore, the outcomes underscore the persistent
challenges in accurately identifying and effectively mitigating gender bias in Chinese-
language texts. They highlight the need for models to possess both a deep understanding
of gender bias and advanced linguistic capabilities to identify and appropriately revise
gender-biased content.
7
Conclusion
We introduce CORGI-PM, the first Chinese human-annotated corpus designed specif-
ically for probing and mitigating gender bias in text. This corpus also serves as the
basis for defining and evaluating metrics across three challenges, aimed at testing the
performance of state-of-the-art language models in detecting, classifying, and mitigating
textual gender bias. Our proposed challenges are intended to establish benchmarks for
assessing the capabilities of language models in this domain. Our experiments and the
submissions demonstrate that the fine-grained subclass labels in our sentences enhance
the models’ ability to probe for gender bias, while our parallel, human-written debiased
data provides robust supervision for training generative language models. We also an-
alyze the performance of submissions from participating teams. The results highlight
the persistent challenges in identifying and mitigating gender bias in Chinese corpora,
underscoring the value of our work. In conclusion, we suggest that future research
utilizing CORGI-PM could significantly advance the field of NLP by improving methods
for both probing and mitigating gender bias in textual data.
Limitations
There are several major limitations in this research work. Due to the high requirement
of annotators for annotating gender-biased sentences and correcting such sentences, we
only choose annotators with higher education, which may lead to potential cognitive
bias. In addition, CORGI-PM mainly focuses on gender bias but has not explored the
bias phenomenon across different domains or disciplines, which could be potentially
derived from the comprehensive benchmark for LLMs [35,11] .
References
1. Agarwal, A., Lavie, A.: Meteor: An automatic metric for mt evaluation with high levels of
correlation with human judgments. Proceedings of WMT-08 (2007)

--- Page 10 ---

10
Y. Li et al.
2. Bai, J., Bai, S., Chu, Y., Cui, Z., Dang, K., Deng, X., Fan, Y., Ge, W., Han, Y., Huang, F.,
et al.: Qwen technical report. arXiv preprint arXiv:2309.16609 (2023)
3. Blodgett, S.L., Barocas, S., Daumé III, H., Wallach, H.: Language (technology) is power:
A critical survey of “bias” in nlp. In: ACL (June 2020), https://www.microsoft.com/en-us/
research/publication/language-technology-is-power-a-critical-survey-of-bias-in-nlp/
4. Bolukbasi, T., Chang, K.W., Zou, J.Y., Saligrama, V., Kalai, A.T.: Man is to computer
programmer as woman is to homemaker? debiasing word embeddings. In: NIPS (2016)
5. Chiril, P., Benamara, F., Moriceau, V.: “be nice to your wife! the restaurants are closed”: Can
gender stereotype detection improve sexism classification? In: Findings of the Association for
Computational Linguistics: EMNLP 2021. pp. 2833–2844 (2021)
6. Chiril, P., Moriceau, V., Benamara, F., Mari, A., Origgi, G., Coulomb-Gully, M.: An annotated
corpus for sexism detection in french tweets. In: Proceedings of the 12th language resources
and evaluation conference. pp. 1397–1403 (2020)
7. Costa-jussà, M.R.: An analysis of gender bias studies in natural language processing. Nature
Machine Intelligence 1(11), 495–496 (2019)
8. Cui, Y., Che, W., Liu, T., Qin, B., Wang, S., Hu, G.: Revisiting pre-trained models for chinese
natural language processing. arXiv preprint arXiv:2004.13922 (2020)
9. Dixon, L., Li, J., Sorensen, J., Thain, N., Vasserman, L.: Measuring and mitigating unintended
bias in text classification. In: Proceedings of the 2018 AAAI/ACM Conference on AI, Ethics,
and Society. p. 67–73. AIES ’18, Association for Computing Machinery, New York, NY, USA
(2018). https://doi.org/10.1145/3278721.3278729, https://doi.org/10.1145/3278721.3278729
10. Dong, X., Wang, Y., Yu, P.S., Caverlee, J.: Disclosure and mitigation of gender bias in llms.
arXiv preprint arXiv:2402.11190 (2024)
11. Du, X., Yao, Y., Ma, K., Wang, B., Zheng, T., Zhu, K., Liu, M., Liang, Y., Jin, X., Wei,
Z., et al.: Supergpqa: Scaling llm evaluation across 285 graduate disciplines. arXiv preprint
arXiv:2502.14739 (2025)
12. Gao, L., Biderman, S., Black, S., Golding, L., Hoppe, T., Foster, C., Phang, J., He, H., Thite,
A., Nabeshima, N., et al.: The pile: An 800gb dataset of diverse text for language modeling.
arXiv preprint arXiv:2101.00027 (2020)
13. Jiang, A., Yang, X., Liu, Y., Zubiaga, A.: Swsr: A chinese dataset and lexicon for online
sexism detection. Online Social Networks and Media 27, 100182 (2022)
14. Jiao, M., Luo, Z.: Gender bias hidden behind chinese word embeddings: The case of chi-
nese adjectives. In: Proceedings of the 3rd Workshop on Gender Bias in Natural Language
Processing. pp. 8–15 (2021)
15. King, T.L., Scovelle, A.J., Meehl, A., Milner, A.J., Priest, N.: Gender stereotypes and biases
in early childhood: A systematic review. Australasian Journal of Early Childhood 46(2),
112–125 (2021)
16. Kiritchenko, S., Mohammad, S.: Examining gender and race bias in two hundred senti-
ment analysis systems. In: Proceedings of the Seventh Joint Conference on Lexical and
Computational Semantics. pp. 43–53. Association for Computational Linguistics, New Or-
leans, Louisiana (Jun 2018). https://doi.org/10.18653/v1/S18-2005, https://aclanthology.org/
S18-2005
17. Kotek, H., Dockum, R., Sun, D.: Gender bias and stereotypes in large language models. In:
Proceedings of the ACM collective intelligence conference. pp. 12–24 (2023)
18. Li, Y., Zhang, G., Yang, B., Lin, C., Ragni, A., Wang, S., Fu, J.: HERB: Measuring hierarchical
regional bias in pre-trained language models. In: He, Y., Ji, H., Li, S., Liu, Y., Chang, C.H.
(eds.) Findings of the Association for Computational Linguistics: AACL-IJCNLP 2022.
pp. 334–346. Association for Computational Linguistics, Online only (Nov 2022). https:
//doi.org/10.18653/v1/2022.findings-aacl.32, https://aclanthology.org/2022.findings-aacl.32/
19. Lin, C.Y.: Rouge: A package for automatic evaluation of summaries. In: Text summarization
branches out. pp. 74–81 (2004)

--- Page 11 ---

Overview of the NLPCC 2025 Shared Task: Gender Bias Mitigation Challenge
11
20. Lu, K., Mardziel, P., Wu, F., Amancharla, P., Datta, A.: Gender bias in neural natural language
processing. In: Logic, Language, and Security, pp. 189–202. Springer (2020)
21. Madaan, N., Mehta, S., Agrawaal, T., Malhotra, V., Aggarwal, A., Gupta, Y., Saxena, M.:
Analyze, detect and remove gender stereotyping from bollywood movies. In: Friedler, S.A.,
Wilson, C. (eds.) Proceedings of the 1st Conference on Fairness, Accountability and Trans-
parency. Proceedings of Machine Learning Research, vol. 81, pp. 92–105. PMLR (23–24 Feb
2018), https://proceedings.mlr.press/v81/madaan18a.html
22. Papineni, K., Roukos, S., Ward, T., Zhu, W.J.: Bleu: a method for automatic evaluation
of machine translation. In: Proceedings of the 40th annual meeting of the Association for
Computational Linguistics. pp. 311–318 (2002)
23. Parikh, P., Abburi, H., Badjatiya, P., Krishnan, R., Chhaya, N., Gupta, M., Varma, V.:
Multi-label categorization of accounts of sexism using a neural framework. arXiv preprint
arXiv:1910.04602 (2019)
24. Parikh, P., Abburi, H., Badjatiya, P., Krishnan, R., Chhaya, N., Gupta, M., Varma, V.: Multi-
label categorization of accounts of sexism using a neural framework. In: Proceedings of
the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th
International Joint Conference on Natural Language Processing (EMNLP-IJCNLP). pp.
1642–1652. Association for Computational Linguistics, Hong Kong, China (Nov 2019).
https://doi.org/10.18653/v1/D19-1174, https://aclanthology.org/D19-1174
25. Park, J.H., Shin, J., Fung, P.: Reducing gender bias in abusive language detection. In: Pro-
ceedings of the 2018 Conference on Empirical Methods in Natural Language Processing. pp.
2799–2804. Association for Computational Linguistics, Brussels, Belgium (Oct-Nov 2018).
https://doi.org/10.18653/v1/D18-1302, https://aclanthology.org/D18-1302
26. Qiu, Y., Li, H., Li, S., Jiang, Y., Hu, R., Yang, L.: Revisiting correlations between intrinsic
and extrinsic evaluations of word embeddings. In: Chinese Computational Linguistics and
Natural Language Processing Based on Naturally Annotated Big Data, pp. 209–221. Springer
(2018)
27. Rudinger, R., Naradowsky, J., Leonard, B., Van Durme, B.: Gender bias in coreference
resolution. arXiv preprint arXiv:1804.09301 (2018)
28. Sahai, S., Sharma, D.: Predicting and explaining french grammatical gender. In: Proceedings
of the Third Workshop on Computational Typology and Multilingual NLP. pp. 90–96 (2021)
29. Sharma, S., El Asri, L., Schulz, H., Zumer, J.: Relevance of unsupervised metrics in task-
oriented dialogue for evaluating natural language generation. CoRR abs/1706.09799 (2017),
http://arxiv.org/abs/1706.09799
30. Srivastava, A., Rastogi, A., Rao, A., Shoeb, A.A.M., Abid, A., Fisch, A., Brown, A.R.,
Santoro, A., Gupta, A., Garriga-Alonso, A., et al.: Beyond the imitation game: Quantifying
and extrapolating the capabilities of language models. arXiv preprint arXiv:2206.04615 (2022)
31. Sun, T., Gaut, A., Tang, S., Huang, Y., ElSherief, M., Zhao, J., Mirza, D., Belding, E., Chang,
K.W., Wang, W.Y.: Mitigating gender bias in natural language processing: Literature review.
arXiv preprint arXiv:1906.08976 (2019)
32. Sun, T., Gaut, A., Tang, S., Huang, Y., ElSherief, M., Zhao, J., Mirza, D., Belding, E.,
Chang, K.W., Wang, W.Y.: Mitigating gender bias in natural language processing: Literature
review. In: Proceedings of the 57th Annual Meeting of the Association for Computational
Linguistics. pp. 1630–1640. Association for Computational Linguistics, Florence, Italy (Jul
2019). https://doi.org/10.18653/v1/P19-1159, https://aclanthology.org/P19-1159
33. Wake, A., Chen, B., Lv, C., Li, C., Huang, C., Cai, C., Zheng, C., Cooper, D., Zhou, F., Hu,
F., et al.: Yi-lightning technical report. arXiv preprint arXiv:2412.01253 (2024)
34. Wan, Y., Pu, G., Sun, J., Garimella, A., Chang, K.W., Peng, N.: " kelly is a warm person,
joseph is a role model": Gender biases in llm-generated reference letters. arXiv preprint
arXiv:2310.09219 (2023)

--- Page 12 ---

12
Y. Li et al.
35. Wang, Y., Ma, X., Zhang, G., Ni, Y., Chandra, A., Guo, S., Ren, W., Arulraj, A., He, X.,
Jiang, Z., et al.: Mmlu-pro: A more robust and challenging multi-task language understanding
benchmark. In: The Thirty-eight Conference on Neural Information Processing Systems
Datasets and Benchmarks Track (2024)
36. Waseem, Z.: Are you a racist or am I seeing things? annotator influence on hate speech
detection on Twitter. In: Proceedings of the First Workshop on NLP and Computational Social
Science. pp. 138–142. Association for Computational Linguistics, Austin, Texas (Nov 2016).
https://doi.org/10.18653/v1/W16-5618, https://aclanthology.org/W16-5618
37. Webster, K., Recasens, M., Axelrod, V., Baldridge, J.: Mind the gap: A balanced corpus of
gendered ambiguous pronouns. Transactions of the Association for Computational Linguistics
6, 605–617 (2018)
38. Webster, K., Recasens, M., Axelrod, V., Baldridge, J.: Mind the GAP: A balanced corpus of
gendered ambiguous pronouns. Transactions of the Association for Computational Linguistics
6, 605–617 (2018). https://doi.org/10.1162/tacl_a_00240, https://aclanthology.org/Q18-1042
39. Weidong, Z., Rui, G., Baobao, C., Yirong, C., Chen, L.: Development of Peking University
CCL Corpus. In: Chinese Corpus Linguistic Journal (Jan 2019)
40. Xu, H., Zhang, Z., Wu, L., Wang, C.J.: The cinderella complex: Word embeddings reveal
gender stereotypes in movies and books. PloS one 14(11), e0225385 (2019)
41. Young, A., Chen, B., Li, C., Huang, C., Zhang, G., Zhang, G., Wang, G., Li, H., Zhu, J., Chen,
J., et al.: Yi: Open foundation models by 01. ai. arXiv preprint arXiv:2403.04652 (2024)
42. Zhang, G., Li, Y., Wu, Y., Zhang, L., Lin, C., Geng, J., Wang, S., Fu, J.: Corgi-pm: A chinese
corpus for gender bias probing and mitigation (2023), https://arxiv.org/abs/2301.00395
43. Zhang, G., Qu, S., Liu, J., Zhang, C., Lin, C., Yu, C.L., Pan, D., Cheng, E., Liu, J., Lin, Q.,
et al.: Map-neo: Highly capable and transparent bilingual large language model series. arXiv
preprint arXiv:2405.19327 (2024)
44. Zhang, Z., Han, X., Liu, Z., Jiang, X., Sun, M., Liu, Q.: Ernie: Enhanced language representa-
tion with informative entities. arXiv preprint arXiv:1905.07129 (2019)
45. Zhao, J., Wang, T., Yatskar, M., Ordonez, V., Chang, K.W.: Men also like shopping:
Reducing gender bias amplification using corpus-level constraints. In: Proceedings of
the 2017 Conference on Empirical Methods in Natural Language Processing. pp. 2979–
2989. Association for Computational Linguistics, Copenhagen, Denmark (Sep 2017). https:
//doi.org/10.18653/v1/D17-1323, https://aclanthology.org/D17-1323
46. Zhao, J., Wang, T., Yatskar, M., Ordonez, V., Chang, K.W.: Gender bias in coreference
resolution: Evaluation and debiasing methods. In: Proceedings of the 2018 Conference of
the North American Chapter of the Association for Computational Linguistics: Human
Language Technologies, Volume 2 (Short Papers). pp. 15–20. Association for Computational
Linguistics, New Orleans, Louisiana (Jun 2018). https://doi.org/10.18653/v1/N18-2003, https:
//aclanthology.org/N18-2003
47. Zhao, J., Zhou, Y., Li, Z., Wang, W., Chang, K.W.: Learning gender-neutral word embeddings.
arXiv preprint arXiv:1809.01496 (2018)
48. Zhao, J., Du, B., Zhu, S., Liu, P.: Construction of chinese sentence-level gender-unbiased
data set and evaluation of gender bias in pre-training language. In: Proceedings of the 20th
Chinese National Conference on Computational Linguistics. pp. 564–575 (2021)
49. Zhou, P., Shi, W., Zhao, J., Huang, K.H., Chen, M., Cotterell, R., Chang, K.W.: Examining
gender bias in languages with grammatical gender. arXiv preprint arXiv:1909.02224 (2019)
50. Zhu, S., Liu, P.: Great males and stubborn females: A diachronic study of corpus-based
gendered skewness in chinese adjectives. In: Proceedings of the 19th Chinese National
Conference on Computational Linguistics. pp. 31–42 (2020)
51. Zhu, S., Liu, P.: Great males and stubborn females: A diachronic study of corpus-based
gendered skewness in Chinese adjectives. In: Proceedings of the 19th Chinese National

--- Page 13 ---

Overview of the NLPCC 2025 Shared Task: Gender Bias Mitigation Challenge
13
Conference on Computational Linguistics. pp. 31–42. Chinese Information Processing Society
of China, Haikou, China (Oct 2020), https://aclanthology.org/2020.ccl-1.4

```
