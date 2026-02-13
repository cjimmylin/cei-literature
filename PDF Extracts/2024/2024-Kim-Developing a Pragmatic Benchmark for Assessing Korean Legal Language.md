---
title: "2024-Kim-Developing a Pragmatic Benchmark for Assessing Korean Legal Language - PDF Extract"
source_pdf: "2024-Kim-Developing a Pragmatic Benchmark for Assessing Korean Legal Language.pdf"
pages: 23
extracted_at: "2026-02-13T09:50:29.874551"
---

# PDF Extract: 2024-Kim-Developing a Pragmatic Benchmark for Assessing Korean Legal Language

**Source PDF:** 2024-Kim-Developing a Pragmatic Benchmark for Assessing Korean Legal Language.pdf
**Total Pages:** 23

---

## Content

```
--- Page 1 ---

Developing a Pragmatic Benchmark for Assessing Korean Legal Language
Understanding in Large Language Models
Yeeun Kimσ
keeun04@uos.ac.kr
Young Rok Choiλ
yrchoi@lbox.kr
Eunkyung Choiσ
rmarud202@uos.ac.kr
Jinhwan Choiλ
jinhwanchoi@lbox.kr
Hai Jin Parkη
haijinpark@hanyang.ac.kr
Wonseok Hwangσ,λ,∗
wonseok.hwang@lbox.kr
σUniversity of Seoul
λLBox
ηHanyang University
Abstract
Large language models (LLMs) have demon-
strated remarkable performance in the legal
domain, with GPT-4 even passing the Uniform
Bar Exam in the U.S. However their efficacy
remains limited for non-standardized tasks and
tasks in languages other than English. This un-
derscores the need for careful evaluation of
LLMs within each legal system before appli-
cation. Here, we introduce KBL, a benchmark
for assessing the Korean legal language under-
standing of LLMs, consisting of (1) 7 legal
knowledge tasks (510 examples), (2) 4 legal
reasoning tasks (288 examples), and (3) the
Korean bar exam (4 domains, 53 tasks, 2,510
examples). First two datasets were developed
in close collaboration with lawyers to evalu-
ate LLMs in practical scenarios in a certified
manner. Furthermore, considering legal prac-
titioners’ frequent use of extensive legal docu-
ments for research, we assess LLMs in both a
closed book setting, where they rely solely on
internal knowledge, and a retrieval-augmented
generation (RAG) setting, using a corpus of
Korean statutes and precedents. The results in-
dicate substantial room and opportunities for
improvement.
1
Introduction
Large Language Models (LLMs) show remarkable
performance across various tasks. For instance,
GPT-4 has passeed the Uniform Bar Exam (Mar-
tinez, 2023; OpenAI, 2023). However, their per-
formance is still limited beyond the standardized
bar exam questions (Guha et al., 2023; Dahl et al.,
2024; Magesh et al., 2024; Kang et al., 2023; Bern-
sohn et al., 2024; Blair-Stanek et al., 2023), par-
ticularly in handling legal tasks in languages other
than English (Fei et al., 2023; Zhong et al., 2023).
This implies it is necessary to thoroughly evaluate
LLMs before applying them to specific legal tasks
and systems.
∗Corresponding author. Also reachable via email at
wonseok.hwang@uos.ac.kr
Previous works have developed legal bench-
marks for evaluating LLMs primarily in En-
glish (Guha et al., 2023) and Chinese (Fei et al.,
2023; Dai et al., 2023; Anonymous, 2024a) mostly
focusing on a closed book setting where LLMs
answer questions based solely on the knowledge
stored in their parameters. Considering that legal
practitioners often rely on previous legal docu-
ments such as statutes or precedents to make deci-
sion, this setting is underestimate LLMs’ capabili-
ties in a practical scenarios.
Here we introduce KBL1, a benchmark dedicated
to assessing LLMs’ capability in understanding
Korean legal language. KBL consists of (1) 7 legal
knowledge tasks (510 examples), (2) 4 legal rea-
soning tasks (288 examples), and (3) the Korean
bar exam (4 domains, 53 tasks, 2,510 examples).
We evaluate LLMs’ under two settings to better
reflect their real-world usage of LLMs. In collab-
oration with legal professionals, we focus on the
desgin and quality assurance of the tasks moving
beyond solely standardized licensure-style ques-
tions. Specifically, we assess LLMs in scenarios
where (1) they cannot access external knowledge,
and (2) they can use retrievers to search for related
documents. For the second setting, we prepare a
Korean statute corpus consisting of 11k currently
active articles and municipal ordiances and rules,
and utilized a corpus of 150k Korean precedents re-
leased from a previous study (Hwang et al., 2022).
The results indicates that the performance of ar-
guably the most powerful LLMs, such as GPT-4
and Claude-3, remains limited in handling Korean
legal tasks. In an open book setting, their accuracy
improves by up to +8.6%, but the overall perfor-
mance still varies depending on the type of cor-
pus and the LLMs used. This suggests significant
potential for improvement not only in the LLMs
themselves but also in the methods of document
1KOREAN BENCHMARK FOR LEGAL LANGUAGE UN-
DERSTANDING
arXiv:2410.08731v1  [cs.CL]  11 Oct 2024

--- Page 2 ---

retrieval and their integration.
In summary, our contributions are as follows.
• We have developed the first pragmatic and
verified benchmark for Korean legal under-
standing tasks.
• We evaluate LLMs not only in a closed book
setting but also in a open book setting, where
they can utilize two critical legal resources:
Korean statutes and precedents.
• We compare various LLMs and provide the
detailed analysis.
Our datasets, the corpus for RAG, and the evalua-
tion code will be released to the community under
a CC BY-NC license2.
2
Related Work
Many legal AI datasets has been created contribut-
ing to NLP community (Paul et al., 2022; Kapoor
et al., 2022; Yao et al., 2022; Glaser et al., 2021;
Niklaus et al., 2021; Chalkidis et al., 2022a; Rossi
et al., 2021; Chalkidis et al., 2022b; Louis and
Spanakis, 2022; Rabelo et al., 2020; Henderson
et al., 2022; Chalkidis* et al., 2023; Niklaus et al.,
2023). Here we review only a few works that are
dedicated to build benchmark for evaluating LLMs
under zero, or few-shot setting in legal domain.
Guha et al. (2023) developed LegalBench which
comprises 162 legal language understanding tasks
organized according to six different types of legal
reasoning based on the IRAC framework. How-
ever, their work is limited to tasks in English le-
gal language understanding tasks. Additionally, the
benchmark does not evaluate LLMs in a open-book
setting, and LLMs must rely solely on their internal
knowledge.
Magesh et al. (2024) compared commercial
RAG-based AI systems in the US legal domain
using 202 examples on generative tasks and found
that even the most competent system exhibited
a 17% hallucination rate through human evalua-
tion. In contrast, our research focuses on Korean
legal AI tasks and emphasizes scenarios where au-
tomatic evaluations are possibles. RAG systems
rely on various components including databases,
search algorithms, and the backbone of LLMs.
Given these complexities, it becomes impractical
to manually evaluate the performance of RAG sys-
tems every time a component changes. Therefore,
2https://github.com/lbox-kr/kbl
we concentrate on addressing the challenges where
automatic evaluation is feasible.
Fei et al. (2023) developed LawBench that con-
sists of 20 Chinese legal tasks. They categorized
the tasks into three different levels Memorization,
Understanding, and Applying based on Bloom’s
taxonomy. KBL differs in that it handles Korean
legal language understanding tasks and it evaluates
LLMs not just in a closed-book setting but also in
a open-book setting by introducing accompanying
legal corpus.
Hwang et al. (2022) developed LBoxOpen,
which includes two text classification tasks, two
legal judgement prediction tasks, and one sum-
marization task in the Korean legal domain. Each
task contains 5k–50k examples for fine-tuning lan-
guage models and evaluating performance. The
datasets, except for the summarization dataset,
were created by semi-automatically processing Ko-
rean precedents, while human-annotated examples
were used for summarization. Additionally, they
open-sourced 150k Korean precedents. KBL dif-
fers by focusing on (1) evaluating the zero-shot
performance of (large) language models across (2)
more diverse tasks (7 knowledge, 4 reasoning, 53
Korean bar exam), using (3) expert-annotated ex-
amples created spedifically for this study.
Son et al. (2024a) developed KMMLU, a dataset
similar to MMLU(Hendrycks et al., 2021) tailored
for Korean and cultural contexts. It includes diverse
language understanding tasks along with four legal
AI tasks named criminal-law, law, patent,
and taxation, sourced from the Public Service
Aptitude Test and various Korean license exams.3
Many examples pertain to licensure exams such
as the Petitioner Police exam, the Real Estate Bro-
kers exam, and the Occupational Safety and Health
exam, or cover topics in social science theory and
legal terminology. These tasks are generally less
challenging than those found in the bar exam. In
contrast, KBL consists of questions from the Ko-
rean bar exam and the newly created questions
designed to assess comprehensive legal knowledge
and in-depth reasoning capability relevant to the
practice of law. Our work also differs in that it ex-
clusively focus on the legal domains, and we have
collaborated with legal professionals to develop a
pragmatic and verified benchmark. Additionally,
we also assess LLMs in scenarios where they can
3The specific origins of the datasets are not described in
the paper.

--- Page 3 ---

utilize legal documents. We have also ensured that
there is no overlap between the legal task examples
in KMMLU and our dataset by conducting fuzzy
matching between the two datasets, with the most
significant matches displayed in Tables 13–16 in
Appendix.
In addition to KMMLU, several other bench-
marks have been developed specifically to evaluate
language models on Korean natural language pro-
cessing tasks. Park et al. (2021) introduced KLUE
for Korean Language Understanding tasks. Kim
et al. (2022) developed KoBEST, targeting tasks
that require advanced Korean-specific knowledge.
Son et al. (2024b) created HAE-RAE benchmark,
which assess Korean cultural knowledge. Park et al.
(2024) developed Ko-H5 benchmark, consisting of
Korean translated and reviewed datasets. Our work
differs in that it focuses on evaluating LLMs on
Korean legal language understanding tasks.
3
Datasets
Our benchamrk consists of 7 knowledge tasks, 4
reasoning tasks,4 and multiple-choice questions
from the Korean bar exam. All tasks are struc-
tured as question-answering task where the model
must select the correct answer for given questions,
similar to MMLU (Hendrycks et al., 2021). The
datasets were compiled using various sources, in-
cluding Korean precedents, statutes, bar exams,
legal QA datasets from Korea Legal Aid Corpora-
tion5, etc.
The Korean legal system, rooted in civil law, in-
corporates complex historical and cultural aspects
unique to Korea. Notably, GPT-4 has not passed
the Korean bar exam, despite passing the US bar
exam. This highlights that creating a Korean legal
benchmark involves more than translating existing
benchmarks; it requires developing a new system
with a unique ontology. To ensure the quality of
the datasets, we developed the tasks in close corpo-
ration with legal professionals, and all the answers
have been verified by 8 licensed lawyers.6 The
verification took 26 hours in total reflecting the
difficulty (and the quality) of the tasks constructed.
During the quality assurance process, we found
freely available data, often created by individuals
4Here, the term “reasoning” refers to “general NLP rea-
soning task in the legal domain”
5https://www.klac.or.kr/
6For two case relevance QA datasets (RELq, RELp), only a
portion of examples were verified due to the difficulty of the
tasks. For more details, see Section 3.2
with semi-expertise, frequently include substan-
tial amounts of errors (up to 21% in our study),
highlighting the importance of close collaboration
with experts (Section A.1 covers additional general
lessons learned during the dataset creation process).
Representative examples from individual tasks are
displayed in Tables 3, 4, 5 in Appendix.
3.1
Legal Knowledge Tasks
Legal Concept QA
The legal concept QA
dataset (CONC) comprises questions addressing
complex legal concepts. For instance, from var-
ious types of suspension–such as suspension of
indictment, suspension of sentence, suspension of
execution, suspension of collection, suspension of
announcement–a model needs to select the option
that best fits a given definition. The examples were
crafted based on legal terminology reference doc-
uments from South Korean courts7, definition of
legal terms provided by the National Law Informa-
tion Center8, and the Korea Legislation Research
Institute9. Please See Section A.2.1 for further in-
formation.
Offense Component QA
The offense compo-
nent QA dataset (COMP) comprises question and
answer pairs that determine whether specific ac-
tions meet the actual elements of a criminal offense.
The dataset was constructed using several sources:
“100 Questions and 100 Answers” on Day-to-Day
Laws10 provided by the Ministry of Justice, data
crawled from a now-defunct law firm website11,
cases from Korea Legal Aid Corporation, from
statutory interpretations from the Ministry of Gov-
ernment12. The questions were refined to be clear
legal inquiries based on responses from actual le-
gal consultation experts13. Responses are binary,
either “Yes” or “No”. For example, one real client
question inquires whether escaping prison due to
unbearable harassment over private loans by falsely
reporting to authorities could constitute the crime
7https://sldongbu.scourt.go.kr/word/new/
WordList.work
8https://www.law.go.kr/LSW/eng/engMain.do
9https://www.klri.re.kr/kor/business/
bizLawDicKeyword.do
10https://www.easylaw.go.kr/CSP/
OnhunqueansLstRetrieve.laf?onhunqnaAstSeq=88&
onhunqueAstSeq=439
11https://github.com/haven-jeon/LegalQA?tab=
readme-ov-file
12https://www.moleg.go.kr/lawinfo/nwLwAnList.
mo?mid=a10106020000
13https://www.klac.or.kr/legalinfo/counsel.do

--- Page 4 ---

Table 1: Data statistics. The GPT-4o tokenizer was used.
Name
KNOWLEDGE
REASONING
BAR EXAM†
CONC COMP STAT STATq
HALL MSTKE MSTKEr
CAUSAL CONS RELq
RELp
CRIMINAL CIVIL PUBLIC RESP
nsamples
100
102
100
52
75
41
40
95
91
46
56
520
910
520
560
ntok
170
208
715
194
200
113
167
1462
211
4,288 8,858
551
495
556
360
†: The number of all examples; Criminal law 2012–2024, 40 examples per year; Civil law 2012–2024, 70 examples per year; Public
law 2012–2024, 40 examples per year; Responsibility 2010–2023, 40 examples per year.
of false accusation.
To ensure the quality of the dataset, we verified
all questions with a lawyer and found that 20%
of examples contained incorrect answers14. The
lawyer provided feedback on why the responses
from the free legal counselings were incorrect15.
The dataset was revised accordingly and we con-
ducted a second round of verification with the
lawyer who confirmed that all 102 revised re-
sponses were free of errors.
Statue Matching QA
The statute matching QA
dataset was constructed from statutes currently ac-
tive in South Korea. To compile the raw data, we
first extracted and counted the citations of articles
from approximately 3 million Korean precedents.
Based on these statistics, we randomly sampled
100 articles–about one-third from the 50 most cited
articles, one-third from the 50 least cited articles,
and one-third the entire range. We also excluded
frequently cited statutes such as the Civil Acts,
Civil Procedure Act, Criminal Acts, and Criminal
Procedure Act from the top 50 to ensure diversity.
This method guarantees the inclusion of articles
from various legal domains. The resulting dataset
comprises 100 statutes, includes articles from the
Civil Act, Enforcement Decree of the Public Ser-
vice Ethics Act, Public Official Election Act, Phar-
macists Act, Environmental Preservation Act, etc.
Based on the extracted articles, we developed
two datasets: STAT and STATq. STAT comprises 100
questions designed to evaluate whether a model can
accurately match the content of a law to its specific
statute number. For example, language models are
tested on their ability to determine whether Article
36 of the Food Sanitation Act pertains to facility
14The free legal counselings aim to make legal services
accessible to socially disadvantaged groups while stating that
the answers provided may not be entirely accurate, as they
are based solely on the questions and facts presented by the
client.
15For example, one of the feedback is "It is not possible to
determine a violation of the Personal Information Protection
Act based solely on the provided facts and questions. However,
if the question is changed to inquire about defamation, it can
be determined that the offense components are met."
standards or the evaluation of food standards and
specifications. STATq includes 50 questions that
assess whether the language model can accurately
identify the relevant statute for a given query. For
instance, in response to the question “Is the maxi-
mum fine 2 million won for failing to report and in-
stead keeping a lost item found on the street?”, the
language model must correctly identify the articles
related to the misappropriation of lost property.
Hallucination QA
The hallucination QA dataset
is constructed from laws that often confused by
the general public. For example, many people are
unaware that throwing an object at someone can
constitute assault, even if it does not hit the target.
The dataset also includes laws specific to Korea,
such as the Kim Young Ran Law, which prohibits
gifts of food and drink worth more than 30,000
won to public officials. First, 75 examples were
collected similarly to the COMP dataset with fol-
lowing criteria: the questions should be commonly
mistaken and reviewed by a lawyer. Approximately,
around 21% (16 out of 75) were corrected based
on the lawyer’s feedback. These corrected exam-
ples were used in the three sub tasks: statute hallu-
cination QA (HALL), common legal mistake QA
(MSTKE), and common legal mistake QA with rea-
soning (MSTKEr). For given confusing legal ques-
tions, a model needs to select the correct answer
where the answer set consists of: (1) (fictitious)
statute and corresponding reasoning (HALL), or
(2) “yes”, “no”, or “there is no correct answer”
(MSTKE). In case of MSTKEr, the answer also in-
cludes corresponding reasoning.
3.2
Legal Reasoning Tasks
Causal Reasoning QA
The causal reasoning QA
dataset (CAUSAL) is compiled from a series of ver-
dicts from criminal trials involving physical harm
leading to injury or death. The examples are drawn
from cases categorized as “Death or Injury Re-
sulting from Violence” or “Death Resulting from
Bodily Injury”. We used precedents from these two
criminal cases based on advice from a lawyer, as

--- Page 5 ---

selected cases had relatively well-matched causal
relations. For each given factual description and
claims, the task is to assess whether the defendant’s
actions were the direct and decisive cause of the
victim’s injury or death. A guilty verdict implies
that “there is causal relationship” between the de-
fendant’s actions and the victim’s injury or death,
indicating that the event would not have occurred
without the defendant’s involvement. Conversely,
a not guilty verdict may indicate that other factors
also contributed to the victim’s injury or death, or
that there was no no causal relationship between
the defendant’s actions and the outcome. These
instances are classified under “no causal relation-
ship.”
In the first verification process, we shared 5
specific examples with four legal professionals
and refined the guidelines based on their inputs.
After collecting a total of 100 examples, we con-
ducted a second verification process, where another
lawyer who did not participate in the first process,
reviewed all 100 samples and provided feedback
on errors. The error rate was 7%, and these erro-
neous examples were either replaced or removed
according to the lawyer’s feedback, resulting in a
final 95 samples.
Statement Consistency QA
Statement Consis-
tency QA (CONS) is developed using the verdicts
from criminal and civil trials. These verdict docu-
ments often note inconsistencies in the statements
of the victims, witnesses, and defendants. If a
statement given at the scene, during prosecution,
or in court is found inconsistent with other evi-
dences, it may be officially recorded as such by
the judge. In this task, a model is required to accu-
rately determine whether two presented statements
are consistent with each other. It’s important to
note that the “consistency” is judged based on a
legal perspective. For example, hitting 5 times can
be considered as legally consistent compared to
hitting 7 times depending on the circumstances16.
We followed a similar verification process with the
CAUSAL dataset. In the second verification process,
approximately 9% of the data was questioned by a
lawyer and corresponding examples were deleted,
resulting in a final 91 examples. Note that both
CAUSAL and CONS datasets were built from Ko-
rean precedents where the decision is carefully
16Suwon District Court, Anyang Branch, Judgment dated
November 20, 2020, Case No. 2020고합56 (수원지방법원
안양지원2020. 11. 20. 선고2020고합56 판결)
made by judges. Also, although the second verifica-
tion processes were conducted by a single lawyer,
the decisions were made by citing corresponding
precedents, providing unified guidelines for the
decision.
Case Relevance QA
The two Case Relevance
QA datasets (RELq, RELp) are constructed based on
how judges cite previous cases. In the precedents
from the Supreme Court of Korea (referred to as
PS), judges often references prior cases (PR) in
two contexts: (1) to support their decision citing
similar cases (“relevant”), or (2) to denote that the
cases brought by the appellant do not pertain to the
current case (“not relevant”).
For the first dataset, RELq, a model needs to de-
termine whether a given precedent supports the
query. Each example in this dataset includes: (1)
PS, the Supreme Court precedent (2) PR, a refer-
enced precedent, (3) LS, a precedent from a lower
court handling the same case with PS, and (4) LR,
a precedent from a lower court related to PR. To
construct the queries, we (1) manually extracted
the facts and the appellant’s arguments from PS
and LS, (2) generate initial queries using GPT-4,
and (3) manually revised these queries. The target
precedent is composed by extracting the facts, the
appellant’s claim, and the judge’s opinion from PR
and LR. This dataset primarily includes examples
where PR is not supportive. We also created pos-
itive examples where PR is supportive, but they
were not included here based on advice from le-
gal professionals. This decision was influenced by
two factors: (1) the queries do not incorporate the
judge’s opinion, which is crucial for determining
the relevance between legal cases, and (2) each
precedent encompasses various legal judgements
where “supportiveness” is an issue-specific deter-
mination, hence the query should align specifically
with the relevant part of the precedent.
To address these issues, we developed the sec-
ond dataset, RELp. In this task, a model must de-
termine whether two given precedents address the
same legal issue. To improve relevance assessment,
the previous queries in RELq change into the prece-
dent including judge’s opinions. Additionally, we
incorporate 10 positive examples where the con-
clusion of PS is “remand for retrial,” and the judge
accepts PR, which is provided by the appellants
to support their claim. We assume the decision to
“remand for retrial” strongly indicates “supportive-
ness.”

--- Page 6 ---

Note that the “relevance” between cases depends
on various aspects such as users’ specific goals
(van Opijnen and Santos, 2017). In this regards,
previous studies in legal information retrieval often
address this issue by considering all possible rel-
evance simultaneously (Santosh et al., 2024; Hou
et al., 2024). For instance in the COLIEE legal
case retrieval tasks, if a case is cited in another
case (regardless of whether two cases are support-
ive or not), the cited case is considered as rele-
vant (Goebel et al., 2023). In our approach, we
attempt to differentiate “relevance” into two cat-
egories based on lexical cues found in the prece-
dents.
3.3
Korean Bar Exam
Multiple-choice questions
The Korean Bar
Exam is designed to evaluate legal knowledge
and the capability to perform tasks essential for a
lawyer. Administered at least once annually under
the Ministry of Justice’s supervision, the exam is
divided into two main parts: multiple-choice ques-
tions and an essay-type written test. The multiple-
choice section comprises 150 questions, divided
among Public Law (PUBLIC), Civil Law (CIVIL),
and Criminal Law (CRIMINAL), with 40, 70, and
40 questions in each subject area, respectively. The
Public Law section covers Constitutional Law and
Administrative Law; The Civil Law section en-
compasses Civil Law, Commercial Law, and Civil
Procedure Law; and the Criminal Law section in-
cludes Criminal Law and Criminal Procedure Law.
We use the test held in 2012–2024. The essay-type
written test covers specialized legal areas such as
International Law, Labor Law, and Tax Law, in
addition to Public Law, Civil Law, and Criminal
Law.
We focus solely on the multiple-choice ques-
tions for Public Law, Civil Law, and Criminal Law.
as the official answers for the essay-type test are
not publicly available. Additionally, the multiple-
choice section offers clear and definitive answers,
providing an ideal playground to evaluate LLMs’
under a RAG setting, where multiple components
can influence performance.17
Professional Responsibility
The Professional
Responsibility (RESP) examination is a test that
17The Korean bar exam is published annually by the Min-
istry of Justice of Korea under ’KOGL Type 1’ license. The
license permits both commercial and non-commercial use,
and allows the creation of derivative works, including modifi-
cations, as long as the source is cited.
conducted by the Ministry of Justice to assess the
professional ethics required of lawyers. Held at
least once a year, this examination comprises 40
multiple-choice questions. We use the tests con-
ducted from 2010 to 2023 for our analysis.
3.4
Corpus
We utilize 150k Korean precedents released by
(Hwang et al., 2022) for the RAG experiments.
The corpus, processed using the gpt-4o tokenizer,
contains 320M tokens. Additionally, we have devel-
oped a new Korean statute corpus compiled from
active Korean statutes (법령) and municipal ordi-
nances and rules (자치법규) as of Nov. 2023. The
raw data for this was collected from LAW OPEN
DATA18, a resource maintained by the Korean gov-
ernment. This statute corpus consists of 220k ar-
ticles, totaling 52M tokens, where each article is
concatenated with the name of the act, again pro-
cessed using the gpt-4o tokenizer.
4
Experiments
4.1
Evaluation
We developed the evaluation code using the
lm-eval-harness framework (Gao et al., 2023).
Each task is formulated as multiple-choice ques-
tion, where the model must generate a label cor-
responding to the given questions and possible
selections. The options are tagged with letters A
through E, and the model is tasked with generat-
ing the letter that matches the ground truth. For
the evaluation of open-source LLMs (EEVE (Kim
et al., 2024c), KULLM (Kim et al., 2024a), and
Qwen2 (Bai et al., 2023)), we compare the aver-
age logit values by feeding individual (question,
choice) pairs into the models. This approach is
adopted because the performance of models tend
to drop significantly when they directly generate
labels.
4.2
Retrieval Augmented Generation
We constructed the BM25 retriever using the
pyserini library (Lin et al., 2021). We first in-
dexed the precedent, and the statute corpora using
pyserini.index.lucene and LuceneSearcher
with default settings. To retrieve related documents,
the question is used as a query to the retriever. The
number of documents retrieved is determined in
the following way; (1) identify the maximum num-
18https://open.law.go.kr/LSO/main.do

--- Page 7 ---

Table 2: Comparison of various models. The accuracies of individual tasks are shown for legal concept QA (CONC),
offense component QA (COMP), statute number and content matching QA (STAT), statute and query matching QA
(STATq), statute hallucination QA (HALL), common legal mistake QA (MSTKE), common legal mistake QA with
reasoning (MSTKEr), causal reasoning QA (CAUSAL), statement consistency QA (CONS), query and case relevance
QA (RELq), inter-case relevance QA (RELp), and the Korean bar exam (BAR EXAM). The average accuracies for 7
knowledge tasks (AVGK), 2 reasoning tasks (CAUSAL, CONS, AVGR), and 3 bar exams (AVGB) are shown. For
the experiments with GPT where the model shows randomness even with temperature →0 due to their internal
algorithm that automatically raises the temperature until certain threshold satisfied, we repeat either two (the
knowledge and the reasoning tasks) or three (the bar exam) times and show their mean values. prec. and stat. in
the bottom 5 rows indicate the precedents and the statutes corpus respectively. Two corpora were used during the
RAG experiments. n/a indicates the scores cannot be computed due the limitation in the context length. The scores
for other open-source models are present in Table 11 in Appendix.
Name
KNOWLEDGE
REASONING
BAR EXAM 2024†
AVGK CONC COMP STAT STATq HALL MSTKE MSTKEr AVGR CAUSAL CONS RELq RELp AVGB CRIMINAL CIVIL PUBLIC
Most frequent
33
20
50
20
21
25
34
35
50
50
50
50
50
24
23
26
23
EEVE-10.8ba (solar)
45.8
42.0
45.1 23.0 80.8
41.3
51.2
37.5
58.4
42.1
74.7
n/a
n/a
17.7
12.5
15.7
25.0
KULLM3-10.7bb (solar)
52.1
52.0
53.9 23.0 94.2
42.7
53.6
45.0
80.1
81.1
79.1
n/a
n/a
20.0
20.0
20.0
20.0
LG-Exaone-3.0-7.8bc
59.3
83.0
53.9 29.0 98.1
44.0
48.8
57.5
79.1
79.0
79.1
n/a
n/a
20.8
22.5
20.0
20.0
Qwen2-7bd
55.3
60.0
54.9 32.0 96.2
48.0
51.2
45.0
79.2
73.7
84.6
n/a
n/a
28.1
35.0
24.3
25.0
Qwen2-72be
60.2
82.0
48.0 34.0 98.1
53.3
48.8
57.5
86.7
82.1
91.2
n/a
n/a
31.1
22.5
35.7
35.0
Claude-3-sonnetf
62.0
82.0
51.0 36.0 98.0
65.0
56.0
60.0
87.7
85.3
90.1 15.2 66.1
33.5
27.5
32.9
40.0
Claude-3-opusg
67.0
89.0
55.0 37.0
100
80.0
61.0
57.0
87.2
85.3
89.0 45.7 78.6
41.0
27.5
42.9
52.5
Claude-3.5-sonneth
70.0
93.0
62.8 42.0
100
81.3
58.5
52.5
89.3
87.4
91.2 56.5 75.0
42.5
37.5
40.0
50.0
GPT-3.5i
50.0
58.0
49.0 26.0 93.0
45.0
46.0
46.0
62.7
71.1
54.5
n/a
n/a
23.1
15.0
24.3
30.0
GPT-4o-minij
64.6
83.0
55.9 31.0 98.1
70.7
61.0
52.5
85.5
84.2
86.8 67.4 76.8
29.6
25.0
31.4
32.5
GPT-4k
72.0
95.0
64.0 49.0
100
77.0
61.0
65.0
88.6
84.2
92.9 79.4 81.3
48.1
39.2
46.7
58.3
GPT-4 + prec.
74.4
95.5
71.6
-
100
75.4
61.0
68.8
-
-
-
-
-
50.9
41.6
55.2
55.8
GPT-4 + stat.
72.4
95.0
62.8
-
100
78.7
56.1
65.0
-
-
-
-
-
49.3
46.7
48.6
52.5
GPT-4 + prec. + stat.
75.3
95.0
72.6
-
100
79.4
61.0
70.0
-
-
-
-
-
49.7
46.7
50.0
52.5
Claude-3-sonnet + prec. + stat.
59.9
67.0
53.9
-
84.6
66.7
56.1
55.0
-
-
-
-
-
18.8
12.5
21.4
22.5
Claude-3-opus + prec. + stat.
65.3
87.0
59.8
-
98.1
66.7
46.3
62.5
-
-
-
-
-
32.1
32.5
21.4
42.5
Claude-3.5-sonnet + prec. + stat.
70.1
92.0
56.9
-
98.1
82.7
51.2
67.5
-
-
-
-
-
46.2
50.0
38.6
50.0
†The scores for Bar exams 2012–2023 shown in Appendix.
ayanolja/EEVE-Korean-10.8B-v1.0
bnlpai-lab/KULLM3
cEXAONE-3.0-7.8B-Instruct (Research et al., 2024)
dQwen2-72B-Instruct-GPTQ-Int8
eQwen/Qwen2-7B-Instruct
f claude-3-sonnet-20240229
gclaude-3-opus-20240229
hclaude-3-5-sonnet-20240620
igpt-3.5-turbo-0125
jgpt-4o-2024-0513
kgpt-4o-mini-2024-07-18
ber of documents that LLMs can process simul-
taneously, (2) progressively decrease the number
of documents until the performance ceases to im-
prove. This results in retrieving between 1–8 doc-
uments; the exact number will be specified in the
accompanying code. For the HALL task, we em-
ploy individual (question, choice) pairs as queries
to retrieve related documents since each answer in-
clude the name of a (fictitious) statute. This method
ensures the relevance of retrieved documents to the
specific query, enhancing the accuracy of the task
performance.
5
Results
We evaluate four open-source LLMs and five com-
mercial LLMs across 7 legal knowledge tasks, 4
legal reasoning tasks, and 3 bar exam tasks con-
ducted in 2024 (Table 2).
Open-source LLMs show performance com-
parable to GPT-3.5
We first compare open-
source LLMs and GPT-3.5. On the knowledge
tasks, EEVE-10.7b, KULLM3-10.7b, Qwen2-7b,
and GPT-3.5 score on average 45.8, 52.1, 55.3,
and 50.0 respectively (rows 2–6, 10; column 1)
indicating open-source LLMs achieve compara-
ble or better performance than GPT-3.5. Simi-
larly, on two reasoning tasks–CAUSAL, CONS–all
open source LLMs outperform GPT-3.5 except for
EEVE-10.7b, which scores 4.3 points lower.
However on the Korean bar exam which re-
quires complex legal reasoning and knowledge,
all open-source LLMs and GPT-3.5 perform close
to the baseline achievable by selecting the most
frequent labels (4th column from the right, rows
1–6, 9). Notably, Qwen2-72b shows the highest
performance, even exceeding GPT-3.5 by margins
of +10.2, +24.0, and +8.0 one knowledge tasks, rea-
soning tasks, and the bar exam respectively (rows
6 vs 9). 19
19Even Qwen2-7b shows most competent performance
compared to other open-source Korean LLMs of similar sizes,

--- Page 8 ---

GPT-4 can partially solve the Korean bar exam
Noticing all open-source LLMs and GPT-3.5
show limited performance on the bar exam, we
next focus on evaluating more powerful com-
mercial LLMs. Five commercial LLMs–Claude-
3-sonnet, Claude-3-opus, Claude-3.5-sonnet, and
GPT-4–achieve higher performance compared to
the strongest open-source model Qwen-72b, with
improvement of +1.8, +6.8, +9.8, +11.8 on the
knowledge tasks; +1.0, +0.5, +2.6, +1.9 on the
two reasoning tasks (CAUSAL, CONS); +2.4, +9.9,
+11.4, +17 on the 2024 bar exam 2024 (rows 6–
8, and 10). It shows that although GPT-4 passes
the U.S. bar exam and it achieves most competent
performance, there remains significant room for
improvement in LLM applications for Korean le-
gal AI tasks. Here we focus on the 2024 bar exam,
which is least likely to have been used in training
these LLMs. Scores for the bar exams from 2010
to 2023, including the professional responsibility
QA, are shown in Table 7, 8, 9, 10 in Appendix.
One noticeable observation is that in the STAT
task, where a model needs to match the content of
a law to its statute number, all models show very
low performance (23.0–49.0, col 4). This indicates
that current LLMs are unreliable for recalling spe-
cific legal knowledge, as previously observed (Fei
et al., 2023; Anonymous, 2024a; Dahl et al., 2024;
Magesh et al., 2024).
RAG can be beneficial, but several factors influ-
ence the overall performance
Next we evalu-
ate GPT-4 under a RAG setting. We prepared two
types of corpora, a precedent-corpus consisting
of 150k Korean precedents (Hwang et al., 2022)
and a statute-corpus comprising Korean statutes,
and municipal ordinances and rules. We employ
a BM25 retriever without re-ranking as the base-
line. Even in this simple setting, GPT-4 achieves
particularly in Bar examss. We propose two possible explana-
tions for this. As previously reported Chalkidis et al. (2020);
Hwang et al. (2022), training legal LLMs from scratch can be
beneficial for solving difficult tasks. But, most strong open-
source Korean LLMs are adapted from English-dedicated
LLMs (Llama (Touvron et al., 2023a,b), Solar (Kim et al.,
2024b), Mistral (Jiang et al., 2023)) by further training with
a Korean corpus. There may be knowledge transfer between
multilingual corpus. Note that the Qwen series also achieves
strong performance in the Chinese legal domain (Anonymous,
2024b). Although the Korean legal system differs from Chi-
nese legal systems, basic legal frameworks like IRAC may
have corresponding notions and legal terms in each system. It
is important to note that the details of the training corpus for
many open-source LLMs are not fully disclosed, making it
difficult to interpret the origin of their performance.
higher scores on the knowledge tasks, scoring +2.4
with precedents, +0.4 with statutes, and +3.3 with
both precedents and statutes (rows 4–6 from the
bottom, column 1). On the bar exam, GPT-4 im-
proves by +7.4 in CRIMINAL and +3.3 in CIVIL
(3rd row from the bottom, 2nd and 3rd columns
from the right). However, in PUBLIC GPT-4 scores
-2.5 with precedents, -5.8 with statutes, and -5.8
with both, indicating a drop in performance.
Conversely, Claude series shows no clear im-
provement under the same RAG setting, with
Claude-3-sonnet scoring -2.1, and -8.4 on the
knowledge and the bar exam respectively (col-
umn 1, 14; rows 7, 16); Claude-3-opus scores -1.7,
and -4.3 (column 1, 14; rows 8, 17); Claude-3.5-
sonnet scores +0.1, and +3.7 (column 1, 14; rows 9,
18). This illustrates how multiple factors–LLM, re-
triever, re-ranker, corpus, etc.–can influence overall
performance, highlighting the importance of devel-
oping a benchmark to provide a foundation for the
automatic evaluation of the RAG system.
6
Analysis
Here we provide a further analysis of the Korean
bar exam held in 2024. This exam was chosen be-
cause: (1) it requires both deep legal knowledge
and reasoning capabilities; (2) GPT-4 exhibited sur-
prisingly low performance despite having passed
the U.S. bar exam (Martinez, 2023); (3) GPT-4 was
trained using data from before the 2024 bar exam,
ruling out the possibility of data contamination.
We first categorizes individual questions into
two types: (1) Rule or (2) Application. A question
is categorized as Application-type if it requires not
just an understanding of legal knowledge or prin-
ciples, but also how these are applied to specific
real-world cases. Otherwise, it is considered Rule-
type. Although the IRAC method–Issue, Rule, Ap-
plication, and Conclusion (IRAC)–typically has
four categories, we focus on two because ques-
tions often belong to multiple categories, making
them difficult to clearly categorize. In the Civil
domain, there are 29 Rule-type questions and 41
Application-type questions. The Criminal domain
includes 4 Rule-type and 36 Application-type ques-
tions, while the Public domain comprises 23 Rule-
type and 17 Application-type questions.
RAG primarily enhances performance on Rule-
type questions
Fig. 1 depicts GPT-4’s accuracy
on the 2024 bar exam, highlighting performance

--- Page 9 ---

Figure 1: GPT-4’s performance on the 2024 bar exam
without RAG (blue) or with RAG (orange, green, red).
without RAG (blue), with the statute corpus (or-
ange), with the precedent-corpus, and with both
corpora (red). The left panels display accuracy on
Rule-type questions, while the right panels show
on Application-type questions.
In both Civil and Criminal domains, using the
precedent corpus significantly enhances accuracy
for Rule-type questions (upper left and middle left
panels, blue vs green). However, there are no im-
provements in Civil Application-type questions
and only marginal improvements in Application-
type questions. Conversely, in the Public domain,
neither the precedent corpus nor the statute corpus
proves beneficial.
7
Conclusion
We propose KBL, a pragmatic benchmark designed
for Korean Legal language understanding that com-
prises (1) 7 knowledge tasks, (2) 4 reasoning tasks,
and (3) Korean bar exams. The first two tasks were
designed with close corporation with legal profes-
sionals and the answers were validated by lawyers.
The results indicate that there is still a significant
room for improvement in LLMs’ capabilities in
the Korean legal domain. Additionally, recognizing
that legal research often involves consulting related
legal documents, we equip LLMs for evaluation
in a RAG setting by providing two accompanying
legal corpora for retrieval: a precedent corpus from
a previous study (Hwang et al., 2022) and a statute
corpus developed in this study. Enabling LLMs to
utilize external legal documents via a simple BM25
retriever has shown to improve performance but
not always depending on several factors. This high-
lights the importance of our work that provides a
common playground for automatic evaluating of
RAG systems.
Limitations
Here we evaluate LLMs on multi-choice type ques-
tions only where clear ground truths can be estab-
lished. For generative tasks, although it would be
possible to use LLM-as-a-judge as a proxy, the
field is actively evolving and its accuracy is still
limited. Also, it is particularly challenging to eval-
uate generative tasks in the legal domain where the
hallucination are still prone and where complex
in-depth reasoning process are required (Magesh
et al., 2024). Although we have meticulously de-
signed and selected the tasks for KBL, it is impor-
tant to acknowledge that our benchmark cannot
encompass the entire spectrum of legal tasks espe-
cially where the labeling data is very costly due
to the fact that it requires professional trained for
several years. Nevertheless we aim to capture the
essential aspects of legal intelligence that can be
automatically evaluated. For this, we have collab-
orated with legal professionals and verified all ex-
amples thoroughly, striving to establish a reliable
benchmark.
Ethics Statement
We use Korean precedents and statutes as a main
source of raw data where all personal information,
if any, is redacted by Korean government or court.
The part of the datasets include the detailed de-
scription of crimes from precedents that are al-
ready publicly available. Open-source LLMs have
a possibility of the misuse and can be easily tuned
for unethical purpose (Qi et al., 2024; Kim et al.,
2024d). However, here we do not release or train
any models but focusing on their evaluation with
the benchmark that consists of legal question and
answers, the precedent corpus, and the statute cor-
pus.
Acknowledgements
We thank Prof. Yong Lim, Prof. Jong Hwan Kim
for their critical comments on the legal aspects. We
also thank Hyunjun Kim, Jinu Lee, and Dongjun
Lee for their assistant in designing tasks during the
early stages of the project. The part of this research
was supported by the National Research Founda-
tion of Korea (NRF) grant funded by the Korea gov-
ernment (MSIT) (NO.2022M3J6A1084845) for
Yeeun Kim.

--- Page 10 ---

References
Anonymous. 2024a. Collam: A comprehensive bench-
mark for evaluating large language models in legal
domain.
Anonymous. 2024b. Collam: A comprehensive bench-
mark for evaluating large language models in legal
domain. OpenReview.
Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang,
Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei
Huang, Binyuan Hui, Luo Ji, Mei Li, Junyang Lin,
Runji Lin, Dayiheng Liu, Gao Liu, Chengqiang Lu,
Keming Lu, Jianxin Ma, Rui Men, Xingzhang Ren,
Xuancheng Ren, Chuanqi Tan, Sinan Tan, Jianhong
Tu, Peng Wang, Shijie Wang, Wei Wang, Sheng-
guang Wu, Benfeng Xu, Jin Xu, An Yang, Hao Yang,
Jian Yang, Shusheng Yang, Yang Yao, Bowen Yu,
Hongyi Yuan, Zheng Yuan, Jianwei Zhang, Xingx-
uan Zhang, Yichang Zhang, Zhenru Zhang, Chang
Zhou, Jingren Zhou, Xiaohuan Zhou, and Tianhang
Zhu. 2023. Qwen technical report. arXiv preprint
arXiv:2309.16609.
Dor Bernsohn, Gil Semo, Yaron Vazana, Gila Hayat,
Ben Hagag, Joel Niklaus, Rohit Saha, and Kyryl
Truskovskyi. 2024. LegalLens: Leveraging LLMs
for legal violation identification in unstructured text.
In Proceedings of the 18th Conference of the Euro-
pean Chapter of the Association for Computational
Linguistics (Volume 1: Long Papers), pages 2129–
2145, St. Julian’s, Malta. Association for Computa-
tional Linguistics.
Andrew Blair-Stanek, Nils Holzenberger, and Ben-
jamin Van Durme. 2023. Can gpt-3 perform statutory
reasoning?
Ilias Chalkidis, Manos Fergadiotis, Prodromos Malaka-
siotis, Nikolaos Aletras, and Ion Androutsopoulos.
2020. LEGAL-BERT: The muppets straight out of
law school. In Findings of the Association for Com-
putational Linguistics: EMNLP 2020, pages 2898–
2904, Online. Association for Computational Lin-
guistics.
Ilias Chalkidis*, Nicolas Garneau*, Catalina Goanta,
Daniel Martin Katz, and Anders Søgaard. 2023. LeX-
Files and LegalLAMA: Facilitating English Multi-
national Legal Language Model Development. In
Proceedings of the 61st Annual Meeting of the As-
sociation for Computational Linguistics, Toronto,
Canada. Association for Computational Linguistics.
Ilias Chalkidis, Abhik Jana, Dirk Hartung, Michael
Bommarito, Ion Androutsopoulos, Daniel Katz, and
Nikolaos Aletras. 2022a. LexGLUE: A benchmark
dataset for legal language understanding in English.
In Proceedings of the 60th Annual Meeting of the
Association for Computational Linguistics (Volume
1: Long Papers), pages 4310–4330, Dublin, Ireland.
Association for Computational Linguistics.
Ilias Chalkidis, Tommaso Pasini, Sheng Zhang, Letizia
Tomada, Sebastian Schwemer, and Anders Søgaard.
2022b. FairLex: A multilingual benchmark for eval-
uating fairness in legal text processing. In Proceed-
ings of the 60th Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Pa-
pers), pages 4389–4406, Dublin, Ireland. Associa-
tion for Computational Linguistics.
Matthew Dahl, Varun Magesh, Mirac Suzgun, and
Daniel E. Ho. 2024. Large legal fictions: Profiling
legal hallucinations in large language models.
Yongfu Dai, Duanyu Feng, Jimin Huang, Haochen Jia,
Qianqian Xie, Yifang Zhang, Weiguang Han, Wei
Tian, and Hao Wang. 2023. Laiw: A chinese legal
large language models benchmark. arXiv preprint
arXiv:2310.05620.
Zhiwei Fei, Xiaoyu Shen, Dawei Zhu, Fengzhe Zhou,
Zhuo Han, Songyang Zhang, Kai Chen, Zongwen
Shen, and Jidong Ge. 2023. Lawbench: Benchmark-
ing legal knowledge of large language models. arXiv
preprint arXiv:2309.16289.
Leo Gao, Jonathan Tow, Baber Abbasi, Stella Biderman,
Sid Black, Anthony DiPofi, Charles Foster, Laurence
Golding, Jeffrey Hsu, Alain Le Noac’h, Haonan Li,
Kyle McDonell, Niklas Muennighoff, Chris Ociepa,
Jason Phang, Laria Reynolds, Hailey Schoelkopf,
Aviya Skowron, Lintang Sutawika, Eric Tang, An-
ish Thite, Ben Wang, Kevin Wang, and Andy Zou.
2023. A framework for few-shot language model
evaluation.
Ingo Glaser, Sebastian Moser, and Florian Matthes.
2021. Summarization of German court rulings. In
Proceedings of the Natural Legal Language Process-
ing Workshop 2021, pages 180–189, Punta Cana,
Dominican Republic. Association for Computational
Linguistics.
Randy Goebel, Yoshinobu Kano, Mi-Young Kim, Ju-
liano Rabelo, Ken Satoh, and Masaharu Yoshioka.
2023. Summary of the competition on legal infor-
mation, extraction/entailment (coliee) 2023. In Pro-
ceedings of the Nineteenth International Conference
on Artificial Intelligence and Law, ICAIL ’23, page
472–480, New York, NY, USA. Association for Com-
puting Machinery.
Neel Guha, Julian Nyarko, Daniel E. Ho, Christo-
pher Ré, Adam Chilton, Aditya Narayana, Alex
Chohlas-Wood, Austin Peters, Brandon Waldon,
Daniel N. Rockmore, Diego Zambrano, Dmitry Tal-
isman, Enam Hoque, Faiz Surani, Frank Fagan, Galit
Sarfaty, Gregory M. Dickinson, Haggai Porat, Ja-
son Hegland, Jessica Wu, Joe Nudell, Joel Niklaus,
John Nay, Jonathan H. Choi, Kevin Tobia, Mar-
garet Hagan, Megan Ma, Michael Livermore, Nikon
Rasumov-Rahe, Nils Holzenberger, Noam Kolt, Pe-
ter Henderson, Sean Rehaag, Sharad Goel, Shang
Gao, Spencer Williams, Sunny Gandhi, Tom Zur,
Varun Iyer, and Zehua Li. 2023. Legalbench: A col-
laboratively built benchmark for measuring legal rea-
soning in large language models.

--- Page 11 ---

Peter Henderson, Mark Simon Krass, Lucia Zheng,
Neel Guha, Christopher D Manning, Dan Jurafsky,
and Daniel E. Ho. 2022. Pile of law: Learning re-
sponsible data filtering from the law and a 256GB
open-source legal dataset. In Thirty-sixth Conference
on Neural Information Processing Systems Datasets
and Benchmarks Track.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou,
Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
2021. Measuring massive multitask language under-
standing. Proceedings of the International Confer-
ence on Learning Representations (ICLR).
Abe Bohan Hou, Orion Weller, Guanghui Qin, Eu-
gene Yang, Dawn Lawrie, Nils Holzenberger, An-
drew Blair-Stanek, and Benjamin Van Durme. 2024.
Clerc: A dataset for legal case retrieval and retrieval-
augmented analysis generation.
Wonseok Hwang, Dongjun Lee, Kyoungyeon Cho,
Hanuhl Lee, and Minjoon Seo. 2022. A multi-task
benchmark for korean legal language understand-
ing and judgement prediction. In Thirty-sixth Con-
ference on Neural Information Processing Systems
Datasets and Benchmarks Track.
Albert Q. Jiang, Alexandre Sablayrolles, Arthur Men-
sch, Chris Bamford, Devendra Singh Chaplot, Diego
de las Casas, Florian Bressand, Gianna Lengyel,
Guillaume Lample, Lucile Saulnier, Lélio Re-
nard Lavaud, Marie-Anne Lachaux, Pierre Stock,
Teven Le Scao, Thibaut Lavril, Thomas Wang, Tim-
othée Lacroix, and William El Sayed. 2023. Mistral
7b.
Xiaoxi Kang, Lizhen Qu, Lay-Ki Soon, Adnan Tra-
kic, Terry Zhuo, Patrick Emerton, and Genevieve
Grant. 2023. Can ChatGPT perform reasoning using
the IRAC method in analyzing legal scenarios like
a lawyer? In Findings of the Association for Com-
putational Linguistics: EMNLP 2023, pages 13900–
13923, Singapore. Association for Computational
Linguistics.
Arnav Kapoor, Mudit Dhawan, Anmol Goel, Arjun T H,
Akshala Bhatnagar, Vibhu Agrawal, Amul Agrawal,
Arnab Bhattacharya, Ponnurangam Kumaraguru, and
Ashutosh Modi. 2022. HLDC: Hindi legal docu-
ments corpus. In Findings of the Association for
Computational Linguistics: ACL 2022, pages 3521–
3536, Dublin, Ireland. Association for Computa-
tional Linguistics.
Dohyeong Kim, Myeongjun Jang, Deuk Sin Kwon, and
Eric Davis. 2022. Kobest: Korean balanced evalua-
tion of significant tasks.
Jeongwook Kim, Taemin Lee, Yoonna Jang, Hyeon-
seok Moon, Suhyune Son, Seungyoon Lee, and
Dongjun Kim. 2024a.
Kullm3: Korea university
large language model 3.
https://github.com/
nlpai-lab/kullm.
Sanghoon Kim, Dahyun Kim, Chanjun Park, Wonsung
Lee, Wonho Song, Yunsu Kim, Hyeonwoo Kim,
Yungi Kim, Hyeonju Lee, Jihoo Kim, Changbae Ahn,
Seonghoon Yang, Sukyung Lee, Hyunbyung Park,
Gyoungjin Gim, Mikyoung Cha, Hwalsuk Lee, and
Sunghun Kim. 2024b. SOLAR 10.7B: Scaling large
language models with simple yet effective depth up-
scaling. In Proceedings of the 2024 Conference of
the North American Chapter of the Association for
Computational Linguistics: Human Language Tech-
nologies (Volume 6: Industry Track), pages 23–35,
Mexico City, Mexico. Association for Computational
Linguistics.
Seungduk Kim, Seungtaek Choi, and Myeongho Jeong.
2024c. Efficient and effective vocabulary expansion
towards multilingual large language models.
Yeeun Kim, Eunkyung Choi, Hyunjun Kim, Hongseok
Oh, Hyunseo Shin, and Wonseok Hwang. 2024d. On
the consideration of ai openness: Can good intent be
abused?
Hyunwoong Ko, Kichang Yang, Minho Ryu, Taeky-
oon Choi, Seungmu Yang, Jiwung Hyun, Sungho
Park, and Kyubyong Park. 2023. A technical report
for polyglot-ko: Open-source large-scale korean lan-
guage models.
Jimmy Lin, Xueguang Ma, Sheng-Chieh Lin, Jheng-
Hong Yang, Ronak Pradeep, and Rodrigo Nogueira.
2021. Pyserini: A Python toolkit for reproducible
information retrieval research with sparse and dense
representations. In Proceedings of the 44th Annual
International ACM SIGIR Conference on Research
and Development in Information Retrieval (SIGIR
2021), pages 2356–2362.
Antoine Louis and Gerasimos Spanakis. 2022. A statu-
tory article retrieval dataset in French. In Proceed-
ings of the 60th Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Pa-
pers), pages 6789–6803, Dublin, Ireland. Associa-
tion for Computational Linguistics.
Varun Magesh, Faiz Surani, Matthew Dahl, Mirac Suz-
gun, Christopher D. Manning, and Daniel E. Ho.
2024. Hallucination-free? assessing the reliability of
leading ai legal research tools.
Eric Martinez. 2023. Re-evaluating gpt-4’s bar exam
performance.
Joel Niklaus, Ilias Chalkidis, and Matthias Stürmer.
2021. Swiss-judgment-prediction: A multilingual le-
gal judgment prediction benchmark. In Proceedings
of the Natural Legal Language Processing Workshop
2021, pages 19–35, Punta Cana, Dominican Repub-
lic. Association for Computational Linguistics.
Joel Niklaus, Veton Matoshi, Matthias Stürmer, Ilias
Chalkidis, and Daniel E Ho. 2023. Multilegalpile:
A 689gb multilingual legal corpus. arXiv preprint
arXiv:2306.02069.
OpenAI. 2023. Gpt-4 technical report.

--- Page 12 ---

Chanjun Park, Hyeonwoo Kim, Dahyun Kim, SeongH-
wan Cho, Sanghoon Kim, Sukyung Lee, Yungi Kim,
and Hwalsuk Lee. 2024. Open Ko-LLM leaderboard:
Evaluating large language models in Korean with Ko-
h5 benchmark. In Proceedings of the 62nd Annual
Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 3220–3234,
Bangkok, Thailand. Association for Computational
Linguistics.
Sungjoon Park, Jihyung Moon, Sungdong Kim, Won Ik
Cho, Ji Yoon Han, Jangwon Park, Chisung Song, Jun-
seong Kim, Youngsook Song, Taehwan Oh, Joohong
Lee, Juhyun Oh, Sungwon Lyu, Younghoon Jeong,
Inkwon Lee, Sangwoo Seo, Dongjun Lee, Hyunwoo
Kim, Myeonghwa Lee, Seongbo Jang, Seungwon
Do, Sunkyoung Kim, Kyungtae Lim, Jongwon Lee,
Kyumin Park, Jamin Shin, Seonghyun Kim, Lucy
Park, Lucy Park, Alice Oh, Jung-Woo Ha (NAVER
AI Lab), Kyunghyun Cho, and Kyunghyun Cho.
2021. Klue: Korean language understanding eval-
uation. In Proceedings of the Neural Information
Processing Systems Track on Datasets and Bench-
marks, volume 1.
Shounak Paul, Pawan Goyal, and Saptarshi Ghosh.
2022. LeSICiN: A Heterogeneous Graph-based Ap-
proach for Automatic Legal Statute Identification
from Indian Legal Documents. In Proceedings of
the 36th AAAI Conference on Artificial Intelligence
(AAAI).
Xiangyu Qi, Yi Zeng, Tinghao Xie, Pin-Yu Chen, Ruoxi
Jia, Prateek Mittal, and Peter Henderson. 2024. Fine-
tuning aligned language models compromises safety,
even when users do not intend to! In The Twelfth
International Conference on Learning Representa-
tions.
Juliano Rabelo, Mi-Young Kim, Randy Goebel, Masa-
haru Yoshioka, Yoshinobu Kano, and Ken Satoh.
2020. Coliee 2020: Methods for legal document re-
trieval and entailment. In New Frontiers in Artificial
Intelligence: JSAI-IsAI 2020 Workshops, JURISIN,
LENLS 2020 Workshops, Virtual Event, November
15–17, 2020, Revised Selected Papers, page 196–210,
Berlin, Heidelberg. Springer-Verlag.
LG AI Research, :, Soyoung An, Kyunghoon Bae,
Eunbi Choi, Stanley Jungkyu Choi, Yemuk Choi,
Seokhee Hong, Yeonjung Hong, Junwon Hwang,
Hyojin Jeon, Gerrard Jeongwon Jo, Hyunjik Jo,
Jiyeon Jung, Yountae Jung, Euisoon Kim, Hyosang
Kim, Joonkee Kim, Seonghwan Kim, Soyeon Kim,
Sunkyoung Kim, Yireun Kim, Youchul Kim, Ed-
ward Hwayoung Lee, Haeju Lee, Honglak Lee, Jin-
sik Lee, Kyungmin Lee, Moontae Lee, Seungjun
Lee, Woohyung Lim, Sangha Park, Sooyoun Park,
Yongmin Park, Boseong Seo, Sihoon Yang, Heuiy-
een Yeen, Kyungjae Yoo, and Hyeongu Yun. 2024.
Exaone 3.0 7.8b instruction tuned language model.
Julien Rossi, Svitlana Vakulenko, and Evangelos
Kanoulas. 2021. VerbCL: A Dataset of Verbatim
Quotes for Highlight Extraction in Case Law, page
4554–4563. Association for Computing Machinery,
New York, NY, USA.
T. Y. S. S Santosh, Rashid Gustav Haddad, and Matthias
Grabmair. 2024. Ecthr-pcr: A dataset for precedent
understanding and prior case retrieval in the european
court of human rights.
Guijin Son, Hanwool Lee, Sungdong Kim, Seungone
Kim, Niklas Muennighoff, Taekyoon Choi, Cheon-
bok Park, Kang Min Yoo, and Stella Biderman.
2024a. Kmmlu: Measuring massive multitask lan-
guage understanding in korean.
Guijin Son, Hanwool Lee, Suwan Kim, Huiseo Kim,
Jae cheol Lee, Je Won Yeom, Jihyu Jung, Jung woo
Kim, and Songseong Kim. 2024b. HAE-RAE bench:
Evaluation of Korean knowledge in language mod-
els. In Proceedings of the 2024 Joint International
Conference on Computational Linguistics, Language
Resources and Evaluation (LREC-COLING 2024),
pages 7993–8007, Torino, Italia. ELRA and ICCL.
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier
Martinet, Marie-Anne Lachaux, Timothée Lacroix,
Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal
Azhar, Aurelien Rodriguez, Armand Joulin, Edouard
Grave, and Guillaume Lample. 2023a. Llama: Open
and efficient foundation language models.
Hugo Touvron, Louis Martin, Kevin Stone, Peter Al-
bert, Amjad Almahairi, Yasmine Babaei, Nikolay
Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti
Bhosale, Dan Bikel, Lukas Blecher, Cristian Can-
ton Ferrer, Moya Chen, Guillem Cucurull, David
Esiobu, Jude Fernandes, Jeremy Fu, Wenyin Fu,
Brian Fuller, Cynthia Gao, Vedanuj Goswami, Na-
man Goyal, Anthony Hartshorn, Saghar Hosseini,
Rui Hou, Hakan Inan, Marcin Kardas, Viktor Kerkez,
Madian Khabsa, Isabel Kloumann, Artem Korenev,
Punit Singh Koura, Marie-Anne Lachaux, Thibaut
Lavril, Jenya Lee, Diana Liskovich, Yinghai Lu, Yun-
ing Mao, Xavier Martinet, Todor Mihaylov, Pushkar
Mishra, Igor Molybog, Yixin Nie, Andrew Poulton,
Jeremy Reizenstein, Rashi Rungta, Kalyan Saladi,
Alan Schelten, Ruan Silva, Eric Michael Smith, Ran-
jan Subramanian, Xiaoqing Ellen Tan, Binh Tang,
Ross Taylor, Adina Williams, Jian Xiang Kuan,
Puxin Xu, Zheng Yan, Iliyan Zarov, Yuchen Zhang,
Angela Fan, Melanie Kambadur, Sharan Narang, Au-
relien Rodriguez, Robert Stojnic, Sergey Edunov,
and Thomas Scialom. 2023b. Llama 2: Open foun-
dation and fine-tuned chat models.
Marc van Opijnen and Cristiana Santos. 2017. On the
concept of relevance in legal information retrieval.
Artificial Intelligence and Law, 25(1):65–87.
Feng Yao, Chaojun Xiao, Xiaozhi Wang, Zhiyuan Liu,
Lei Hou, Cunchao Tu, Juanzi Li, Yun Liu, Weixing
Shen, and Maosong Sun. 2022. Leven: A large-scale
chinese legal event detection dataset. arXiv preprint
arXiv:2203.08556.

--- Page 13 ---

Wanjun Zhong, Ruixiang Cui, Yiduo Guo, Yaobo Liang,
Shuai Lu, Yanlin Wang, Amin Saied, Weizhu Chen,
and Nan Duan. 2023. Agieval: A human-centric
benchmark for evaluating foundation models.

--- Page 14 ---

A
Appendices
A.1
General Lessons
While developing the benchmark for the legal domain, which requires high expertise, we learned the
following lessons:
• It is necessary to communicate closely with domain experts to distinguish subtle differences and
accurately label the data.
• Freely available data, often created by individuals with semi-expertise, frequently include substantial
amounts of errors (up to 21% in our study), highlighting the importance of close collaboration with
experts.
• The selection of domains should be done carefully, considering the difficulty of the labeling. For
instance, during the creation of the Causal reasoning QA dataset, we initially selected “insurance
dispute”. The domain was chosen because corresponding cases include the lexical cue “substantial
causation (상당인과관계),”. However, during the verification stage by the lawyer, feedback was
received that although the term “causation” might be mistaken to mean a judgment by the court,
legal professionals use it in a practical sense, indicating a contextual connection between the act and
the result based on common experience (경험칙). Therefore, the presence of “substantial causation”
alone cannot serve as a standard to determine the causality of the case. Based on this feedback and
the lawyer’s recommendation, we changed the domain to “Death or Injury Resulting from Violence”
or “Death Resulting from Bodily Injury” where actions could be seen as directly and clearly causing
the results (the defendant’s actions and the victim’s death or injury).
A.2
Datasets
A.2.1
Legal Concept QA
Most Korean legal terms originate from Chinese characters, leading to significant differences in meaning
with even small variations in characters. For instance, the Korean legal terms ‘소각하’ (so-gak-ha) and ‘소
취하’ (so-chui-ha) both refer to methods of terminating a lawsuit. Despite differing by only one character,
they represent significant differences regarding the party responsible for terminating the lawsuit.
Therefore, we collected terms that are rarely used by the general public but should be clearly dif-
ferentiated by experts or have different meanings when used in a legal context. We first reviewed the
definitions of terms listed alphabetically in a legal dictionary and prioritized terms that have subtle
variations. Additionally, during the term selection process, we used commercial LLMs (ChatGPT and
Claude-sonnet) to identify 100 terms that at least one LLM responded inadequately. A lawyer then verified
the dataset, identifying a single error among 100 examples, which was subsequently corrected based on
the lawyer’s feedback.

--- Page 15 ---

Table 3: Task examples. The examples are translated to English using GPT-4.
Data Name
Question
Candidate choices
Answer
Legal Concept QA
(CONC)
다음법률용어의정의를읽고해당단어를
선택해주세요. 정의: 사실인정의기초가되는
경험적사실을경험자자신이직접법원에
진술하지않고다른형태에의하여간접적으로
보고하는것을말한다.
A. 직접증거
B. 진술서
C. 자백
D. 증언보조사항
E. 전문증거
E. 전문증거
Read the definition of the following legal term and
select the appropriate word. Definition: It refers to
reporting an empirical fact that forms the basis for
fact-finding indirectly in other forms without the
experiencer directly testifying in court.
A. Direct Evidence
B. Statement
C. Confession
D. Testimony Assistance
E. Hearsay Evidence
E. Hearsay
Evidence
Offense Component
QA (COMP)
甲은乙을주먹으로때려상해를가하였으나,
그것은乙이이유없이甲에게욕설을퍼부어
행해진것이다. 甲은상해죄로처벌되는가?
A. 아니오
B. 예
B. 예
A hit B with his fist and caused injury, but it was
done because B insulted A without reason. Is A
punishable for injury?
A. No
B. Yes
B. Yes
Query Statute
Matching QA
(STATq)
다음질문에가장관련이깊은법령을선택해
주세요. 식품영업을하려면어떤시설기준을
충족해야되나요?
A. 형사소송법제225
B. 항만과그주변지역의개발및이용에
관한법률제6조
C. 고용보험법제87조
D. 식품위생법제36조1항
E.변호사법제23조
D. 식품위생법제36
조1항
Select the statute most relevant to the following
question: What facility standards must be met to
operate a food business?
A. Criminal Procedure Act Article 225
B. Act on the Development and Use of
Ports and Surrounding Areas Article 6
C. Employment Insurance Act Article 87
D. Food Sanitation Act Article 36(1)
E. Attorney-at-Law Act Article 23
D. Food Sanitation
Act Article 36(1)
Statute Number and
Content Matching
QA (STAT)
다음중법률번호와해당내용이올바르게연결된
것을선택해주세요.
A. 형법제37조(상상적경합) 한개의
행위가여러개의죄에해당하는
경우에는가장무거운죄에대하여
정한형으로처벌한다.
B. 형법제37조(피해자의승낙) 처분할
수있는자의승낙에의하여그법익을
훼손한행위는법률에특별한규정이
없는한벌하지아니한다.
C. 형법제37조(구류) 구류는1일이상
30일미만으로한다.
D. 형법제37조(경합범) 판결이
확정되지아니한수개의죄또는금고
이상의형에처한판결이확정된죄와
그판결확정전에범한죄를경합범으로
한다. <개정2004. 1. 20.>
E. 형법제37조(누범) 금고(禁錮)
이상의형을선고받아그집행이
종료되거나면제된후3년내에금고
이상에해당하는죄를지은사람은
누범(累犯)으로처벌한다.
D. 형법제37조
(경합범) 판결이
확정되지아니한
수개의죄또는
금고이상의형에
처한판결이확정된
죄와그
판결확정전에범한
죄를경합범으로
한다. <개정2004. 1.
20.>
Choose the correct match between statute number
and its content.
A. Criminal Act Article 37 (Ideal
Concurrence) When a single act
constitutes multiple crimes, it shall be
punished by the heaviest penalty
prescribed for such crimes.
B. Criminal Act Article 37 (Victim’s
Consent) An act that harms a legal
interest with the consent of a person who
can dispose of it is not punishable unless
otherwise specified by law.
C. Criminal Act Article 37 (Detention)
Detention shall be for at least one day
and less than thirty days.
D. Criminal Act Article 37 (Concurrent
Crimes) Multiple crimes that have not
been finally adjudicated or crimes
committed before the final adjudication
of a sentence of imprisonment or heavier
punishment shall be treated as concurrent
crimes. <Amended Jan 20, 2004>
E. Criminal Act Article 37 (Repeat
Offender) A person who commits a
crime punishable by imprisonment or
heavier punishment within three years
after being released from the execution
of or being exempted from a sentence of
imprisonment or heavier punishment
shall be punished as a repeat offender.
D. Criminal Act
Article 37
(Concurrent Crimes)
Multiple crimes that
have not been finally
adjudicated or
crimes committed
before the final
adjudication of a
sentence of
imprisonment or
heavier punishment
shall be treated as
concurrent crimes.
<Amended Jan 20,
2004>

--- Page 16 ---

Table 4: Task examples
Data Name
Question
Candidate choices
Answer
Statute Hallucination QA (HALL)
4.7m 높이의개천다리밑에그물
망이설치된사실을인지한뒤충동
적으로그곳을향해사람을떨어뜨
리는행위는살인죄나살인미수죄가
무조건적용되는불법행위인가요?
A. 그렇다. 폭행금지법에의해처벌
될수있다.
B. 그렇다. 살인미수금지법에의해
처벌될수있다.
C. 그렇다. 형법에의해처벌된다.
D. 아니다. 살인미수죄로처벌되지
않을수있다.
D. 아니다. 살인미수죄로처벌되지
않을수있다.
After recognizing the presence of a
net installed under a 4.7m high creek
bridge, is the act of impulsively drop-
ping a person toward it always consid-
ered an illegal act that automatically
applies to murder or attempted murder
charges?
A. Yes. It can be punished under the
Assault Prohibition Act.
B. Yes. It can be punished under the
Attempted Murder Prohibition Act.
C. Yes. It is punishable under the
Criminal Act.
D. No. It may not be punishable as at-
tempted murder.
D. No. It may not be punishable as
attempted murder.
Common Legal Mistake QA (MSTKE)
화장실을못찾던7살아이가길에서
소변을보는것은불법인가요?
A. 정답이없다.
B. 그렇다.
C. 아니다.
B. 그렇다.
Is it illegal for a 7-year-old child who
couldn’t find a bathroom to urinate on
the street?
A. No correct answer.
B. Yes.
C. No.
B. Yes.
Common Legal Mistake QA Reason-
ing (MSTKEr)
알코올의존증환자가술에취해살
인을저질렀다면감형해주나요?
A. 그렇다알코올의존증환자라면
사건당시술에취했는지의여부와
관계없이감형될수있다.
B. 그렇다술에취한사람이범죄를
저지르면심신미약자로간주되어감
형될수있다.
C. 아니다범죄가심각하다면범죄
자가알코올의존증이있다하더라도
고려되지않는다.
B. 그렇다술에취한사람이범죄를
저지르면심신미약자로간주되어감
형될수있다.
If an alcohol-dependent person com-
mits murder while intoxicated, is their
sentence reduced?
A. Yes, an alcohol-dependent person
can have their sentence reduced re-
gardless of whether they were intoxi-
cated at the time of the incident.
B. Yes, a person who commits a crime
while intoxicated can be considered
mentally impaired and have their sen-
tence reduced.
C. No, if the crime is serious, it will
not be considered even if the offender
is alcohol-dependent.
B. Yes, a person who commits a crime
while intoxicated can be considered
mentally impaired and have their sen-
tence reduced.
Causal Reasoning QA (CAUSAL)
다음[검사의공소사실], [피고인의
주장], [증거]를읽고주어진정보만
을바탕으로질문에답해주세요. [검
사의공소사실] [피고인의주장] [증
거] A, B를각각A: 피고인들의행
위B: 피해자의사망라고할때A와
B사이의관계를’인과관계있음’, ’인
과관계없음’ 중하나를선택하여’답
변: 인과관계있음’과같이단답식으
로답해주세요.
A. 인과관계있음
B. 인과관계없음
A. 인과관계있음
Read the [prosecutor’s charges], [de-
fendant’s claims], and [evidence] and
answer the question based solely on
the given information. [Prosecutor’s
charges] [Defendant’s claims] [Evi-
dence] Considering A: Defendants’ ac-
tions and B: Victim’s death, select
’Causal relationship exists’ or ’No
causal relationship’ and respond with
’Answer: Causal relationship exists.’
A. Causal relationship exists
B. No causal relationship
A. Causal relationship exists

--- Page 17 ---

Table 5: Task examples
Data Name
Question
Candidate choices
Answer
Logical Contradiction QA (CONS)
다음진술들이서로일관되는지판
단해주세요. 진술1: 피고인이팔꿈
치로피해자의‘팔뚝부위’를쳤다.
진술2: 피고인이팔꿈치로피해자의
가슴쪽을때렸다.
A. 일관되지않음
B. 일관됨
A. 일관되지않음
Determine whether the following
statements are consistent. Statement
1: The defendant hit the victim’s ’fore-
arm area’ with his elbow. Statement
2: The defendant hit the victim’s chest
area with his elbow.
A. Inconsistent
B. Consistent
A. Inconsistent
Case Relevance QA query (RELq)
다음판결문이의뢰인의주장을뒷
받침하나요? [의뢰인의주장] 판결문
[상고인] [사실관계] [당사자들의주
장] [판사의의견] A: 아니오, B: 예중
하나를선택하여’답변: A’과같이단
답식으로답해주세요.
A. 예.
B. 아니오.
B. 아니오.
Does the following judgment support
the client’s claim? [Client’s claim]
Judgment [Appellant] [Facts] [Parties’
claims] [Judge’s opinion] Choose A:
No or B: Yes and answer with ’An-
swer: A.’
A. Yes.
B. No.
B. No.
Case Relevance QA President (RELp)
다음두판결문은같은사안에대해
다루고있나요? [첫번째판결문상
고인] [첫번째판결문사실관계] [첫
번째판결문당사자들의주장] [첫번
째판결문판사의의견] [두번째판
결문상고인] [두번째판결문사실
관계] [두번째판결문당사자들의주
장] [두번째판결문판사의의견] A:
사안이다르다, B: 사안이다르지않
다중하나를선택하여’답변: A’과
같이단답식으로답해주세요.
A. 사안이다르다
B. 사안이다르지않다.
B. 사안이다르지않다.
Do the following two judgments ad-
dress the same issue? [First judg-
ment appellant] [First judgment facts]
[First judgment parties’ claims] [First
judgment judge’s opinion] [Second
judgment appellant] [Second judg-
ment facts] [Second judgment parties’
claims] [Second judgment judge’s
opinion] Choose A: Different issues
or B: Same issues and answer with
’Answer: A.’
A. Different
B. Same
B. Same
Table 6: The mean token length of the Bar exam
Year Criminal Civil Public Responsibility
2010
-
-
-
334
2011
-
-
-
365
2012
468
470
554
358
2013
530
492
496
335
2014
539
531
706
361
2015
497
435
497
385
2016
539
486
516
374
2017
527
461
571
343
2018
556
491
549
345
2019
570
503
594
383
2020
570
543
576
366
2021
586
513
557
370
2022
587
499
526
351
2023
600
467
520
358
2024
587
538
563
-
* The bar exam was not administered in 2010 and
2011.
* The professional responsibility exam for law
schools has not yet been implemented as of June,
2024

--- Page 18 ---

Table 7: Comparison of various models on Korean Bar Exam-criminal laws.
Avg. 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023
GPT-3.5
20.8
32.5
25.0
12.5
20.0
27.5
17.5
20.0
17.5
12.5
22.5
25.0
22.5
GPT-4
40.4
57.5
52.5
30.0
37.5
35.0
42.5
25.0
57.5
27.5
45.0
20.0
55.0
Claude-3-opus 34.4
62.5
42.5
25.0
32.5
27.5
42.5
12.5
45.0
24.0
42.5
17.5
45.0
random
25
33
23
28
25
23
25
25
20
25
28
25
25
Table 8: Comparison of various models on the Korean Bar Exam, Civil domain.
Avg. 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023
GPT-3.5
23.6
24.3
22.9
21.4
18.6
24.3
25.7
24.3
25.7
21.4
31.4
14.3
28.6
GPT-4
41.0
41.4
35.7
52.9
40.0
34.3
50.0
20.0
42.9
47.1
37.1
50.0
40.0
Claude-3-opus 38.8
37.1
32.9
45.7
37.1
35.7
35.7
22.9
44.3
40.0
44.3
42.9
42.9
random
25
27
23
23
23
29
26
23
27
21
24
30
24
Table 9: Comparison of various models on the Korean Bar Exam, Public domain.
Avg. 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023
GPT-3.5
27.2
27.5
30.0
27.5
37.5
37.5
15.0
25.0
34.2
30.0
20.0
30.0
17.5
GPT-4
54.8
60.0
55.0
52.5
52.5
65.0
65.0
17.5
50.0
57.5
57.5
75.0
50.0
Claude-3-opus 49.2
45.0
62.5
52.5
42.5
45.0
70.0
22.5
57.9
32.5
60.0
52.5
45.0
random
25
25
28
28
25
23
23
23
23
25
25
28
23
Table 10: Comparison of various models on the Korean Bar Exam, the Responsibility domain. This exam begins
from 2010 following the introduction of law schools in South Korea in 2009. As of June 2024, data for the year
2024 is not included as the 15th exam is scheduled for August 2024.
Avg. 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023
GPT-3.5
34.3
37.5
35.0
45.0
35.0
40.0
35.0
40.0
35.0
32.5
27.5
27.5
37.5
25.0
27.5
GPT-4
61.9
70.0
62.5
77.5
62.5
62.5
70.0
57.5
30.0
67.5
62.5
52.5
77.5
52.5
60.0
Claude-3-opus 58.9
72.5
60.0
70.0
60.0
55.0
57.5
60.0
40.0
60.0
67.5
42.5
70.0
60.0
50.0
Table 11: Comparison of various models.
Name
KNOWLEDGE
REASONING
BAR EXAM 2024†
AVGK CONC COMP STAT STATq HALL MSTKE MSTKEr AVGR CAUSAL CONS RELq RELp AVGB CRIMINAL CIVIL PUBLIC
Most frequent
33
20
50
20
21
25
34
35
50
50
50
50
50
24
23
26
23
KoGPT-0.13ba
28.7
20.0
50.0 20.0
21.2
25.3
31.7
32.5
41.1
31.6
50.5
n/a
n/a
16.9
15.0
15.7
20.0
polyglot-ko-1.3bb
28.7
20.0
50.0 20.0
21.2
25.3
31.7
32.5
48.4
51.6
45.1
n/a
n/a
18.6
20.0
15.7
20.0
polyglot-ko-12.8bb
28.7
20.0
50.0 20.0
21.2
25.3
31.7
32.5
50.6
51.6
49.5
n/a
n/a
18.6
20.0
15.7
20.0
LCube-base-0.12bc
28.7
20.0
50.0 20.0
21.2
25.3
31.7
32.5
56.8
68.4
45.1
n/a
n/a
18.6
20.0
15.7
20.0
KORani-v3-13b (polyglot-ko)d
31.3
22.0
50.0 20.0
21.2
26.7
34.2
45.0
51.7
46.3
57.1
n/a
n/a
17.7
20.0
15.7
17.5
Llama3-ko-8be
28.7
21.0
50.0 20.0
21.2
25.3
31.7
32.5
56.4
62.1
50.6
n/a
n/a
18.6
20.0
15.7
20.0
komt-7b (mistral-7b)f
31.6
36.0
42.2 20.0
25.0
21.3
36.6
40.0
46.9
44.2
49.5
n/a
n/a
22.0
27.5
18.6
20.0
†The scores for Bar exams 2012–2023 shown in Appendix.
askt/kogpt2-base-v2
bEleutherAI/polyglot-ko-1.3b (Ko et al., 2023)
clbox/lcube-base (Hwang et al., 2022)
dKRAFTON/KORani-v3-13B
ebeomi/Llama-3-Open-Ko-8B-Instruct-preview
f davidkim205/komt-mistral-7b-v1

--- Page 19 ---

Table 12: Comparison of KMMLU and Korean Bar Exam using 60+ Fuzzy Score - Criminal Law
KMMLU
Korean Bar Exam
Fuzzy Score
Question-Answer 1
주거침입죄에관한설명으로옳지않은것
은? 주거침입죄의미수범은처벌하지않는
다.
주거침입죄에관한설명중옳지않은것은?
(다툼이있는경우에는판례에의함) 임대차
기간이종료된후에는임차인이계속점유하
고있는건물에그소유자가무단으로들어
가더라도주거침입죄가성립하지않는다.
66
Which of the following is incorrect regarding
the crime of trespassing? Attempted trespass-
ing is not punishable.
Which of the following statements about the
crime of trespassing is incorrect? (In case of
dispute, follow the precedents.) After the lease
period expires, if the tenant continues to oc-
cupy the building, the owner cannot be con-
victed of trespassing even if they enter the
building without permission.
66
Source
undisclosed (category : Law-train)
변호사시험1회차형사법선택형1책형문
제15번
.
Question-Answer 2
종물에관한설명중옳지않은것은? (다툼
이있는경우에는판례에의함) 종물은동산
이어야하며, 부동산은종물이될수없다.
종범에관한설명중옳지않은것을모두고
른것은? (다툼이있는경우판례에의함) ㄱ.
정범의강도예비행위를방조하였으나정범
이실행의착수에이르지못한경우방조자
는강도예비죄의종범에해당한다. ㄴ. 자기
의지휘, 감독을받는자를방조하여범죄의
결과를발생하게한자는정범에정한형의
장기또는다액에그2분의1까지가중한형
으로처벌한다. ㄷ. 법률상정범의범행을방
지할의무가있는자가그범행을알면서도
방지하지아니하여범행을용이하게한때에
는부작위에의한종범이성립한다. ㄹ. 종범
은정범의실행행위중에이를방조하는경
우뿐만아니라, 정범이실행행위에나아갔다
면실행의착수전에장래의실행행위를예
상하고이를용이하게한경우에도종범이
성립한다. ㄱ, ㄴ
66
Which of the following is incorrect regard-
ing accessories? (In case of dispute, follow
the precedents.) Accessories must be movable
property; real estate cannot be accessories.
Select all incorrect statements about acces-
sories. (In case of dispute, follow the prece-
dents.) 1. If a person assists in the preparation
of a robbery but the principal does not pro-
ceed to the execution, the accessory is still
guilty of attempted robbery. 2. A person who
aids someone under their direction and super-
vision to commit a crime shall be punished
with a penalty increased by up to half of the
maximum or maximum fine prescribed for the
principal crime. 3. If a person legally obligated
to prevent a crime knowingly fails to do so and
facilitates the crime, they are guilty of an acces-
sory by omission. 4. An accessory is not only
one who assists during the principal’s execu-
tion but also one who facilitates the principal’s
future actions if the principal had proceeded
with the execution. 1, 2.
66
Source
undisclosed (category : Patent)
변호사시험4회차형사법선택형1책형문
제4번
.
Question-Answer 3
행정의실효성확보수단에관한설명으로옳
지않은것은?(다툼이있는경우판례에의
함) 이행강제금은형벌과병과할수없다.
실행의착수시기또는기수시기에관한설명
중옳지않은것은? (다툼이있는경우에는
판례에의함) 부동산의매도인이제1차매수
인에게서중도금을수령한후, 다시제2차매
수인에게서계약금만을지급받더라도배임
죄의실행의착수는인정된다.
65
Which of the following is incorrect regarding
measures to ensure administrative effective-
ness? (In case of dispute, follow the prece-
dents.) Enforcement fines cannot be combined
with criminal penalties.
Which of the following statements about the
timing of the initiation or completion of exe-
cution is incorrect? (In case of dispute, follow
the precedents.) Even if the seller of real estate
receives a down payment from a second buyer
after receiving an installment payment from
the first buyer, the initiation of execution for
breach of trust is acknowledged.
65
Source
undisclosed(category : Law)
변호사시험1회차형사법선택형1책형문
제6번
.

--- Page 20 ---

Table 13: Comparison of KMMLU and Korean Bar Exam using 60+ Fuzzy Score - Civil Law
KMMLU
Korean Bar Exam
Fuzzy Score
Question-Answer 1
종물에관한설명중옳지않은것은? (다툼
이있는경우에는판례에의함) 종물은동산
이어야하며, 부동산은종물이될수없다.
종중에관한설명중옳지않은것은? (다툼
이있는경우판례에의함) 종중의임원은종
중재산의관리· 처분에관한사무를처리함
에있어종중규약또는종중총회의결의에
따라야할의무는있으나선량한관리자로서
의주의를다하여야할의무는없다.
74
Which of the following is incorrect regard-
ing accessories? (In case of dispute, follow
the precedents.) Accessories must be movable
property; real estate cannot be accessories.
Which of the following is incorrect regarding
clan associations? (In case of dispute, follow
the precedents.) The officials of a clan associ-
ation must follow the rules of the clan or the
resolutions of the clan general meeting when
managing or disposing of clan property, but
they do not have a duty to act with the care of
a good manager.
74
Source
undisclosed (category: Patent)
변호사시험10회차민사법선택형문제9번
.
Question-Answer 2
소멸시효에관한설명으로옳지않은것은?
(다툼이있는경우에는판례에의함) 가분채
무의일부에대한시효이익의포기는허용되
지않는다.
소멸시효에관한설명중옳지않은것은?
(다툼이있는경우판례에의함) 가압류로
인한소멸시효중단의효력은가압류결정이
제3채무자에게송달된때에발생하고가압
류신청시로소급하지아니한다.
72
Which of the following is incorrect regarding
extinctive prescription? (In case of dispute, fol-
low the precedents.) The waiver of the benefit
of prescription is not allowed for part of a di-
visible obligation.
Which of the following is incorrect regarding
extinctive prescription? (In case of dispute, fol-
low the precedents.) The effect of interruption
of extinctive prescription by provisional attach-
ment occurs when the provisional attachment
decision is delivered to the third debtor and
does not retroact to the time of the application
for provisional attachment.
72
Source
undisclosed (category: Patent)
변호사시험9회차민사법선택형1책형문
제11번
.
Question-Answer 3
이행지체에관한설명중옳지않은것은?
(다툼이있는경우에는판례에의함) 금전채
무의지연손해금채무는금전채무의이행지
체로인한손해배상채무로서, 지연손해금채
무가확정된때로부터이행지체가된다.
이행지체에관한설명중옳은것은? (다툼이
있는경우에는판례에의함) 채무자는확정
된지연손해금채무에대하여채권자의이행
청구를받은때로부터지체책임을부담하게
된다.
72
Which of the following is incorrect regarding
delay in performance? (In case of dispute, fol-
low the precedents.) The obligation to pay de-
lay damages for a monetary debt arises from
the delay in the performance of the monetary
debt and is in delay from the time the delay
damages are confirmed.
Which of the following is correct regarding
delay in performance? (In case of dispute, fol-
low the precedents.) The debtor is liable for
delay from the time the creditor requests per-
formance of the confirmed delay damages.
72
Source
undisclosed (category: Patent)
변호사시험2회차민사법선택형1책형문
제30번
.

--- Page 21 ---

Table 14: Comparison of KMMLU and Korean Bar Exam using 60+ Fuzzy Score - Public Law (page 1)
KMMLU
Korean Bar Exam
Fuzzy Score
Question-Answer 1
신뢰보호의원칙에대한설명으로옳은것
(○)과옳지않은것(×)을바르게연결한것
은?∗
신뢰보호의원칙에관한설명중옳은것(○)
과옳지않은것(×)을올바르게조합한것
은? (다툼이있는경우판례에의함) ㄱ. 당
초폐기물처리시설을설치한다는도시관리
계획결정및지형도면고시를하였다가폐기
물처리시설대신광장을설치한다는도시관
리계획변경결정및지형도면고시를한경
우당초도시관리계획결정은도시계획시설
사업의시행자지정을받게된다는공적인
견해를표명한것으로볼수있으므로, 그후
의도시관리계획변경결정및지형도면고
시는당초의도시계획시설사업의시행자로
지정받을것을예상하고폐기물처리시설의
설계비용등을지출한자의신뢰이익을침해
한다. ㄴ. 행정청내부의사무처리준칙에해
당하는농림사업시행지침서가공표된것만
으로는사업자로선정되기를희망하는자가
당해지침에명시된요건을충족할경우사
업자로선정되어사업자금지원등의혜택을
받을수있다는보호가치있는신뢰를가지
게되었다고보기어렵다. ㄷ. 신뢰보호의원
칙은법률이나그하위법규뿐만아니라국가
관리의입시제도와같이국· 공립대학의입
시전형을구속하여국민의권리에직접영향
을미치는제도운영지침의개폐에도적용된
다. ㄹ. 신뢰보호의원칙은행정청이공적인
견해를표명할당시의사정이그대로유지됨
을전제로적용되는것이원칙이므로, 사후
에그와같은사정이변경된경우에는그공
적인견해가더이상개인에게신뢰의대상
이된다고보기어려운만큼, 특별한사정이
없는한행정청이그견해표명에반하는처
분을하더라도신뢰보호의원칙에위반된다
고할수없다.
84
Which of the following correctly matches the
correct (○) and incorrect (×) statements re-
garding the principle of protection of trust?∗
Which of the following correctly combines
the correct (○) and incorrect (×) statements
about the principle of protection of trust? (In
case of dispute, follow the precedents.) 1. If
a city management plan decision and a topo-
graphic map notification initially announced
the installation of a waste treatment facility but
later changed to a decision to install a plaza
instead, the initial city management plan deci-
sion can be seen as an official stance that the
person who spent costs on designing the waste
treatment facility expected to be designated as
the implementer of the city planning facility
project, and thus the subsequent city manage-
ment plan change and topographic map noti-
fication violate the trust interest. 2. The mere
publication of the Agricultural Project Imple-
mentation Guidelines, which are internal ad-
ministrative rules, does not provide sufficient
grounds for an applicant to have protected trust
that they will be selected as a project operator
and receive benefits such as business fund sup-
port if they meet the requirements stated in the
guidelines. 3. The principle of protection of
trust applies not only to laws and subordinate
regulations but also to the opening and closing
of policy guidelines that bind the admission
systems of national and public universities,
which directly affect the rights of the public.
4. The principle of protection of trust gener-
ally applies based on the assumption that the
circumstances at the time the administrative
authority expressed its official stance remain
unchanged. Therefore, if such circumstances
change later, it is difficult to consider the offi-
cial stance as a subject of trust for individuals.
In the absence of special circumstances, the
administrative authority’s actions contrary to
its initial stance do not necessarily violate the
principle of protection of trust.
84
Source
undisclosed (category: Law)
변호사시험10회차공법선택형문제21번
.
∗It appears that part of the question is missing in the KMMLU dataset.

--- Page 22 ---

Table 15: Comparison of KMMLU and Korean Bar Exam using 60+ Fuzzy Score - Public Law (page 2)
KMMLU
Korean Bar Exam
Fuzzy Score
Question-Answer 2
행정심판의재결의기속력에대한설명으로
옳지않은것은? A: 재결이확정된경우에는
처분의기초가된사실관계나법률적판단이
확정되고당사자들이나법원은이에기속되
어모순되는주장이나판단을할수없게된
다. B: 재결에의하여취소되거나무효또는
부존재로확인되는처분이당사자의신청을
거부하는것을내용으로하는경우에는그
처분을한행정청은재결의취지에따라다
시이전의신청에대한처분을하여야한다.
C: 재결의기속력은재결의주문및그전제
가된요건사실의인정과판단에대하여만
미친다. D: 당사자의신청을받아들이지않
은거부처분이재결에서취소된경우, 그재
결의취지에따라이전의신청에대하여다
시어떠한처분을하여야할지는처분을할
때의법령과사실을기준으로판단하여야하
므로, 행정청은종전거부처분또는재결후
에발생한새로운사유를내세워다시거부
처분을할수있다.
행정행위의효력에관한설명중옳지않은
것은? (다툼이있는경우판례에의함) A: 민
사소송에있어서어느행정처분의당연무효
여부가선결문제로되는때에는행정처분에
당연무효사유가있는지여부를판단하여당
연무효임을전제로판결할수있고반드시
행정소송등의절차에의하여그취소나무
효확인을받아야하는것은아니다. B: 행정
처분이불복기간의경과로확정된경우에는
그처분의기초가된사실관계나법률적판
단이확정되고당사자들이나법원이이에기
속되어모순되는주장이나판단을할수없
다. C: 과세처분에관한이의신청절차에서
과세관청이이의신청사유가옳다고인정하
여과세처분을직권으로취소한이상그후
특별한사유없이이를번복하고종전처분
을되풀이하는것은허용되지않는다. D: 과
세처분에대한쟁송이진행중에과세관청
이그과세처분의납부고지절차상의하자를
발견한경우에는위과세처분을취소하고절
차상의하자를보완하여다시동일한내용의
과세처분을할수있고, 이와같은새로운처
분이행정행위의불가쟁력이나불가변력에
저촉되는것은아니다. E: 형사법원이판결을
내리기전에영업허가취소처분이행정쟁송
절차에의하여취소되었다면, 그영업허가취
소처분후의영업행위는무허가행위가아닌
것이되므로형사법원은그영업허가취소처
분후의영업행위에대해무죄를선고하여야
한다.
79
Which of the following is incorrect regarding
the binding force of administrative appeal de-
cisions? A: Once a decision is finalized, the
factual and legal determinations underlying the
decision are established, and the parties and
courts are bound by them, precluding contra-
dictory arguments or judgments. B: If a de-
cision cancels or confirms the nullity or non-
existence of a disposition that denied the ap-
plicant’s request, the administrative authority
must reprocess the original application in ac-
cordance with the decision. C: The binding
force of a decision extends only to the ruling
of the decision and the recognition and judg-
ment of the prerequisite facts. D: If a rejection
disposition is canceled by a decision, the ad-
ministrative authority must reprocess the orig-
inal application based on the laws and facts
at the time of the disposition, allowing the au-
thority to issue a new rejection based on new
reasons arising after the original rejection or
decision.
Which of the following is incorrect regarding
the effects of administrative acts? (In case of
dispute, follow the precedents.) A: In civil liti-
gation, if the nullity of an administrative dispo-
sition becomes a preliminary issue, the court
can determine its nullity without requiring the
cancellation or confirmation of nullity through
administrative litigation procedures. B: Once
an administrative disposition is finalized due
to the lapse of the appeal period, the factual
and legal determinations underlying the dis-
position are established, and the parties and
courts are bound by them, precluding contra-
dictory arguments or judgments. C: If the tax
authority cancels a tax disposition ex officio
during an objection procedure due to the valid-
ity of the objection reasons, it cannot, without
special reason, reverse this and repeat the pre-
vious disposition. D: During a tax dispute, if
the tax authority finds procedural defects in
the tax notice, it can cancel the defective tax
disposition, correct the procedural defect, and
reissue the same tax disposition, which does
not violate the non-disputability or irrevoca-
bility of administrative acts. E: If an adminis-
trative cancellation of a business permit is re-
versed through administrative litigation before
a criminal court’s ruling, any business activity
conducted after the cancellation is not consid-
ered unlicensed, and the criminal court must
acquit the defendant of conducting business
without a permit.
79

--- Page 23 ---

Table 16: Comparison of KMMLU and Korean Bar Exam using 60+ Fuzzy Score - Public Law (page 3)
KMMLU
Korean Bar Exam
Fuzzy Score
Question-Answer 3
행정의실효성확보수단에관한설명으로옳
지않은것은?(다툼이있는경우판례에의
함) 이행강제금은형벌과병과할수없다.
甲은2023. 1.경도로에서운전면허를받지
아니하고혈중알코올농도0.15%의술에취
한상태에서자동차를운전하였다. 검사는
甲에대하여무면허운전의점에관하여만
도로교통법위반(무면허운전)죄로공소를제
기하였는데, 제1심제1회공판기일에이르
러음주운전의점에관한도로교통법위반
(음주운전)죄를추가하는취지의공소장변
경허가신청서를제출하였다. 이에관한설명
중옳은것을모두고른것은? (다툼이있
는경우판례에의함) ㄱ. 甲에대한도로교
통법위반(무면허운전)죄와도로교통법위반
(음주운전)죄는상상적경합관계에있다. ㄴ.
만약甲이운전한장소가
도로교통법상
도로가아니라면, 도로교통법위반(무면허운
전)죄는성립할수있지만도로교통법위반
(음주운전)죄는성립할수없다. ㄷ. 제1심법
원이공소장변경허가신청에대한결정을공
판정에서고지한경우, 그사실은공판조서
의필요적기재사항이다. ㄹ. 제1심법원이공
소장변경허가신청에대하여불허가결정을
한경우, 검사는이에불복하여그결정에대
한즉시항고를제기할수있다. ㄱ, ㄷ
79
Which of the following is incorrect regarding
measures to ensure administrative effective-
ness? (In case of dispute, follow the prece-
dents.) Enforcement fines cannot be combined
with criminal penalties.
In January 2023, A drove a car on a road with-
out a driver’s license and while his blood alco-
hol concentration was 0.15%. The prosecutor
indicted A for violating the Road Traffic Act
(unlicensed driving) solely for unlicensed driv-
ing. At the first trial session, the prosecutor
submitted an application to amend the indict-
ment to add the charge of violating the Road
Traffic Act (drunk driving). Which of the fol-
lowing statements is correct? (In case of dis-
pute, follow the precedents.) 1. The crimes of
violating the Road Traffic Act (unlicensed driv-
ing) and violating the Road Traffic Act (drunk
driving) concerning A are in an imaginary con-
currence relationship. 2. If the place where A
drove was not a road under the Road Traffic
Act, the crime of violating the Road Traffic
Act (unlicensed driving) could be established,
but the crime of violating the Road Traffic Act
(drunk driving) could not be established. 3. If
the first trial court announces the decision to
permit the amendment of the indictment in the
courtroom, this fact must be recorded in the
trial transcript. 4. If the first trial court denies
the application to amend the indictment, the
prosecutor can immediately appeal the deci-
sion. 1, 3.
79
Source
undisclosed (category: Law)
변호사시험13회차형사법선택형문제34
번
.

```
