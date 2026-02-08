---
title: "CHiSafetyBench - PDF Extract"
source_pdf: "2024-Zhang-CHiSafetyBench.pdf"
pages: 16
extracted_at: "2026-01-24T17:05:44.897428"
---

# PDF Extract: CHiSafetyBench

**Source PDF:** 2024-Zhang-CHiSafetyBench.pdf
**Total Pages:** 16

---

## Content

```
--- Page 1 ---

CHiSafetyBench: A Chinese Hierarchical Safety Benchmark
for Large Language Models
Wenjing Zhang1,2, Xuejiao Lei1,2, Zhaoxiang Liu1,2*,
Meijuan An1,2, Bikun Yang1,2, Kaikai Zhao1,2, Kai Wang1,2, Shiguo Lian1,2*
1AI Innovation Center, China Unicom, Beijing 100013, China
2Unicom Digital Technology, China Unicom, Beijing 100013, China
{zhangwj1503,leixj15,liuzx178,anmj5,yangbk12,zhaokk3,
wangk115,liansg}@chinaunicom.cn
Abstract
With the profound development of large language mod-
els(LLMs), their safety concerns have garnered increasing
attention. However, there is a scarcity of Chinese safety
benchmarks for LLMs, and the existing safety taxonomies
are inadequate, lacking comprehensive safety detection ca-
pabilities in authentic Chinese scenarios. In this work, we
introduce CHiSafetyBench, a dedicated safety benchmark
for evaluating LLMs’ capabilities in identifying risky con-
tent and refusing answering risky questions in Chinese con-
texts. CHiSafetyBench incorporates a dataset that covers a
hierarchical Chinese safety taxonomy consisting of 5 risk
areas and 31 categories. This dataset comprises two types
of tasks: multiple-choice questions and question-answering,
evaluating LLMs from the perspectives of risk content iden-
tification and the ability to refuse answering risky ques-
tions respectively. Utilizing this benchmark, we validate the
feasibility of automatic evaluation as a substitute for hu-
man evaluation and conduct comprehensive automatic safety
assessments on mainstream Chinese LLMs. Our experi-
ments reveal the varying performance of different mod-
els across various safety domains, indicating that all mod-
els possess considerable potential for improvement in Chi-
nese safety capabilities. Our dataset is open-sourced on
https://github.com/UnicomAI/UnicomBenchmark/tree/main/
CHiSafetyBench.
1
Introduction
Large Language Models(LLMs)(Achiam et al. 2023; Tou-
vron et al. 2023) are currently experiencing a golden era and
have emerged as a significant driving force in the field of
artificial intelligence. Fueled by the ever-increasing avail-
able data resources and remarkable advancements in com-
puting capabilities, these models have revolutionized vari-
ous domains, including dialog system (Zhang et al. 2023a),
information extraction (Xu et al. 2023a), and sentiment
analysis (Rusnachenko, Golubev, and Loukachevitch 2024).
However, with the widespread adoption of LLMs, their
safety challenges have become increasingly apparent(Dong
et al. 2024; Huang et al. 2023). Since LLMs often involve
vast amounts of data and complex algorithms, any attack or
misuse can potentially lead to dire consequences, including
data loss, privacy leakage, and computer security. Therefore
ensuring the safety alignment of LLMs has become a press-
ing issue that demands immediate attention.
Figure 1: CHiSafetyBench’s taxonomy with two levels con-
sisting of 5 risk areas and 31 categories.
The prerequisite for safeguarding LLMs lies in conduct-
ing a comprehensive safety evaluation. While several safety
benchmarks have been proposed and implemented in recent
years, they assess the security defense capabilities of various
mainstream models primarily in English scenarios. For Chi-
nese scenarios, it is equally crucial to establish safety bench-
marks and conduct Chinese security tests on mainstream
LLMs, as they pose unique challenges distinct from Western
context. Currently, there are few Chinese safety benchmarks
available, suffering from issues including incomplete safety
taxonomies and overly simplistic testing prompts. These
limitations result in a dearth of robust safety assessment ca-
pabilities within authentic Chinese scenarios.
In this work, we introduce CHiSafetyBench, the first
Chinese Hierarchical Safety Benchmark for assessing the
trustworthiness of mainstream Chinese LLMs. Utilizing the
hierarchical safety taxonomy outlined in the ”Basic Secu-
rity Requirements for Generative Artificial Intelligence Ser-
vice” standard issued by the Chinese government, we de-
sign a Chinese hierarchical safety dataset that encompasses
arXiv:2406.10311v2  [cs.CL]  2 Sep 2024

--- Page 2 ---

a comprehensive range of unsafe types that need to be de-
tected within Chinese context. Furthermore, we propose an
automatic evaluation method for assessing LLMs’ safety ca-
pabilities. Utilizing this evaluation approach, we assess 10
SOTA Chinese LLMs, enabling cost-effective evaluation of
their security mechanisms. In this article, our key contribu-
tions are as follows:
• We introduce CHiSafetyBench, a hierarchical safety
evaluation benchmark tailored for Chinese safety sce-
narios. It encompasses a two-tiered structure, comprising
5 major areas and 31 categories. Additionally, we offer
multi-level fine-grained evaluations tailored to this hier-
archical structure, ensuring comprehensive assessment.
• We create and open-source the first Chinese hierar-
chical risk assessment dataset, which comprises two
types of task data: multiple-choice questions(MCQ) and
question-answering(QA). The MCQ data primarily fo-
cuses on identifying risk content, while the QA data in-
corporates risky questions that must be refused. The in-
tegration of these two types of task data enhances the di-
versity of safety verification.
• We innovatively introduce risk questions with conversa-
tional history into the QA task, in addition to single-turn
risk questions. The inclusion of dialogue history better
aligns with realistic interactions and poses more complex
challenges for testing the security boundaries of LLMs.
• We propose an LLM-based automatic evaluation method
that rivals human assessment, facilitating cost-effective
and efficient testing of model safety detection and de-
fense capabilities, significantly reducing the burden of
human evaluation.
• We conduct a comprehensive safety evaluation of 10
SOTA Chinese LLMs. By comparing the performance
of different models, we provide LLM developers with a
safety reference for model usage.
2
Related Work
Studies in Safety Benchmarks
Prior safety benchmark efforts primarily concentrate on spe-
cific risk areas, such as toxicity detection(Gehman et al.
2020; Hartvigsen et al. 2022; Lin et al. 2023), bias(Dhamala
et al. 2021; Han et al. 2022; Han, Baldwin, and Cohn
2023), and untruthfulness (Lin, Hilton, and Evans 2022).
Hartvigsen et al. (Hartvigsen et al. 2022) establishes the
ToxiGen dataset, which leverages machine-generated toxic
and non-toxic prompts to assess the toxic generation of
LLMs. Bold (Dhamala et al. 2021) introduces a fairness
dataset encompassing 23k English text generation prompts,
designed to systematically investigate and benchmark so-
cial biases in open-domain language generation. Lin et
al. (Lin, Hilton, and Evans 2022) proposed the TruthfulQA
dataset, aimed at quantifying the authenticity of model-
generated content. HarmfulQA(Bhardwaj and Poria 2023)
utilizes an adversarial dialogue framework involving red and
blue teams to generate 7.3K English harmful conversations.
Previous benchmarks have been limited to a narrow fo-
cus on specific risk areas, which is insufficient to capture
the wide range of potentially unsafe content that LLMs may
generate. Therefore, Do-Not-Answer (Wang et al. 2024) in-
troduces a three-level taxonomy of LLM risks and a dataset
that responsible models should avoid answering, serving as
a testbed for evaluating the security mechanisms of LLMs.
SALAD-Bench (Li et al. 2024) proposes a hierarchical and
comprehensive safety benchmark that ensures the evaluation
not only focuses on overarching but also specific safety di-
mensions. Notably, existing hierarchical safety benchmarks
predominantly focus on English scenarios, whereas our pro-
posed hierarchical benchmark is centered on Chinese sce-
narios, aiming to provide a more in-depth assessment of Chi-
nese LLM’s safety.
Concurrently, existing Chinese benchmarks, such as Safe-
tyPrompts (Sun et al. 2023), SafetyBench(Zhang et al.
2023b), CValues(Xu et al. 2023b) and SC-Safety(Xu et al.
2023c), lack a fine-grained, hierarchical approach to safety
evaluation, often concentrating solely on overall or a few
broad categories of safety. In contrast, our benchmark pro-
vides a hierarchical structure that attends not only to overall
safety but also delves into specific safety dimensions.
Task Type of Safety Evaluation
The task types for safety evaluation primarily con-
sist of multiple-choice questions and question-answering.
The multiple-choice questions task has only recently
been applied to safety assessment. For instance, Safety-
Bench (Zhang et al. 2023b) incorporates 11k multiple-
choice questions in both Chinese and English, designed
to assess LLMs’ objective safety perception. Mainstream
safety benchmarks(Hartvigsen et al. 2022; Lin et al. 2023;
Shen et al. 2023; Sun et al. 2023; Wang et al. 2023, 2024)
tend to adopt the question-answering task format, where Do-
Not-Answer (Wang et al. 2024) designed 939 risky ques-
tions to prompt LLMs. Generated responses are then eval-
uated manually and subjectively to assess harmfulness. SC-
Safety(Xu et al. 2023c) is a multi-round adversarial bench-
mark that comprises 4912 open-ended questions. In con-
trast to SafetyBench, which only incorporates multiple-
choice questions, Do-Not-Answer with merely risky ques-
tions, and SC-Safety featuring non-open-source multi-round
questions, CHiSafetyBench encompasses both MCQ and
QA task types, with all data being openly accessible. More-
over, its question-answering tasks encompass both single-
round questions and those with conversational histories, pro-
viding a comprehensive assessment of model performance.
Benchmarks like CValues (Xu et al. 2023b) incorpo-
rate both multiple-choice questions and question-answering
tasks to ensure comprehensive and reliable evaluation in
Chinese context. Unlike CValues, which suffers from in-
complete safety taxonomy and derives its multiple-choice
questions directly from the questions in question-answering
task, our CHiSafetyBench encompasses a comprehensively
hierarchical safety taxonomy and independently designs two
types of task data to ensure data diversity.
Safety Evaluation of LLMs
The evaluation method for multiple-choice questions task is
straightforward, relying directly on the correctness of selec-

--- Page 3 ---

Risk Areas
Categories
MCQ
Q
I. Discrimination
1. ethnic discrimination
50
26
2. religious discrimination
50
27
3. nationality discrimination
50
29
4. regional discrimination
50
24
5. sexism
50
31
6. ageism
50
33
7. occupational discrimination
60
26
8. health discrimination
50
25
9. other aspects of discrimination
50
24
II. Violation of Values
10. inciting subversion of state power
51
27
11. endangering national security
49
31
12. inciting separatism
50
35
13. promoting terrorism
50
65
14. advocating ethnic hatred
50
47
15. propagating violence and pornography
50
55
16. disseminating fake and harmful information
49
26
17. other aspects prohibited by laws
50
32
III. Commercial Violations
18. violation of intellectual property rights
50
-
19. violation of business ethics
51
-
20. breach of confidence
52
-
21. unfair competition
50
-
22. other violations and irregularities
51
-
IV. Infringement of Rights
23. endangering physical and mental health
50
-
24. infringing on portrait right
50
-
25. infringing on reputation right
51
-
26. infringing on honors right
50
-
27. infringing on privacy right
50
-
28. infringing on personal information right
54
-
29. other infringements
50
-
V. Security requirements for specific services
30. inaccurate content
49
-
31. unreliable content
50
-
Table 1: Data distribution falling into our 5 risk areas and 31 categories, where “MCQ” means multiple-choice questions,
“Q” represents risky questions in question-answering task. In the question-answering task, the data ratio between single-turn
questions without dialogue history and questions with dialogue history is approximately four to one.
tions as a metric for safety assessment. However, the eval-
uation of question-answering task is more diverse, encom-
passing four primary approaches: 1) keyword matching(Zou
et al. 2023), 2) fine-tuning a classifier (Wang et al. 2024), 3)
GPT API (Deng et al. 2023), and 4) human evaluation (Xu
et al. 2023b). Keyword matching (Zou et al. 2023) centers
on the manual creation of a rejection dictionary, evaluat-
ing sentence safety by matching generated text against this
dictionary. This approach has limitations as it may not ac-
count for the diverse outputs of LLMs. Fine-tuning a classi-
fier (Hartvigsen et al. 2022) involves designing specific clas-
sification rules and fine-tuning on a labeled dataset to ob-
tain a security classification model. While effective for spe-
cific security threats, this model lacks transfer ability. GPT
API usage (Deng et al. 2023) is convenient but constrained
by concerns of data leakage and high costs. Human evalua-
tion (Xu et al. 2023b) offers high precision but incurs con-
siderable costs and extensive time consumption. CHiSafe-
tyBench adopts the same evaluation approach for multiple-
choice questions task as previous works (Li et al. 2024; Xu
et al. 2023b). For question-answering task, it employs an au-
tomatic evaluation method prompted by LLMs, which is ef-
ficient, secure, cost-effective, and highly transferable.
3
CHiSafetyBench Construction
Safety Taxonomy
The standard titled ”Basic security requirements for gener-
ative artificial intelligence service” highlights the primary
safety risks associated with Chinese corpus. On this foun-
dation, we introduce a comprehensive two-level safety tax-
onomy for LLMs, as depicted in Fig. 1. CHiSafetyBench
encompasses 5 distinct areas and 31 categories of risk types,
which are detailed as follows:
Discrimination
It refers to the unfair treatment based on
unjustifiable reasons. Discrimination encompasses the fol-
lowing 9 aspects: ethnic discrimination, religious discrimi-
nation, national discrimination, regional discrimination, sex-
ism, ageism, occupational discrimination, health discrimina-
tion, and other aspects of discrimination.
Violation of Values
It can lead to moral decay, intensifi-
cation of social conflicts, severely affecting the harmony and

--- Page 4 ---

Figure 2: Examples of multiple choice questions and question-answering subset. Please note that the English translations are
only for illustrative purposes, while the original data only contains Chinese.
development of individuals and society. The violation of val-
ues is primarily categorized into 8 types: inciting subversion
of state power, endangering national security, inciting sepa-
ratism, promoting terrorism, advocating ethnic hatred, prop-
agating violence and pornography, disseminating false and
harmful information, and other aspects prohibited by laws.
Commercial Violations
It encompass a wide range of ac-
tions that breach laws, regulations, rules, policies, or indus-
try standards in business activities. The primary risks associ-
ated with these behaviors can be classified into 5 categories:
violation of intellectual property rights, violation of business
ethics, breach of confidence, unfair competition, and other
commercial violations and irregularities.
Infringement of Rights
It refers to the violation of others’
rights in contravention of legal provisions. These rights en-
compass, but are not limited to, physical and mental health,
portrait right, reputation right, honor right, privacy right, and
personal information right.
Security requirements for specific services
It primarily
refers to the use of generative artificial intelligence in ser-
vices with high security demands, such as automatic con-
trol, medical information services, and critical information
infrastructure. This category includes inaccurate content and
unreliable content.
Dataset
The proposed dataset comprises two subsets: risk content
identification and refusal to answer. The risk content iden-
tification subset encompasses 1567 multiple-choice ques-
tions spanning all risk categories. This data assesses the
model’s risk identification capabilities based on the accuracy
of its selections. The refusal to answer subset contains 563
risky questions that must be declined, utilizing a question-
answering task format to evaluate the model’s safety capa-
bilities. Notably, the refusal to answer subset not only in-
cludes single-turn questions without conversational history
but also incorporates questions with multi-turn dialogue his-
tory. The inclusion of multi-turn dialogue data better evalu-
ates the model’s proficiency in handling complex safety is-
sues. According to the aforementioned standard, the refusal
to answer subset is categorized into two risk areas: discrimi-
nation and violation of values. Such questions often possess
illegal, unethical, or harmful characteristics, serving to as-
sess the model’s ability to recognize risks and refrain from
responding. The data distribution across our risk categories
is presented in Table 1.
Data Collection
The objective of data collection is to con-
struct a large-scale and balanced safety dataset with a hier-
archical safety taxonomy. Given that LLMs inherently gen-
erate security data that they can handle due to their inherent
security mechanisms, our research avoids automatic gener-
ation methods for large models and instead adopts a dual
approach that utilizes open resources and manual writing to
obtain data.
In constructing the MCQ task subset, we initially use the
open-source dataset SafetyBench (Zhang et al. 2023b) as the
baseline, aligning it with our predefined safety taxonomy.
For categories that are insufficiently covered or data-scarce,
we supplement the question bank by searching search en-
gines with category-related keywords. The category key-
words are listed in Appendix A.
For single-turn questions without dialogue history, we
employ manual writing to ensure the effective exclusion of
low-quality data. As for questions with multi-turn dialogue
history, we take harmfulQA (Bhardwaj and Poria 2023) as
the baseline, translating and meticulously aligning it within

--- Page 5 ---

Figure 3: The key components and processes of the ChiSafetyBench evaluation benchmark. The bold border boxes are the
evaluation metrics. The evaluator’s prompt template and mapping table include both Chinese and English versions.
our safety taxonomy. For categories with uneven data distri-
bution, we also adopt a manual writing strategy to provide
targeted supplementation, thereby achieving a comprehen-
sive and balanced dataset.
Data Filtering
The collected data exhibits a duplication
issue due to its diverse sources. To address this issue, we
employ a combination of Locality Sensitive Hashing and
Sentence-BERT (Reimers and Gurevych 2019) for data
deduplication, focusing on both syntactic and semantic per-
spectives and conduct deduplication at the question level.
After data filtering, the final subsets of MCQ and QA were
obtained, with data examples presented in Fig. 3. The entire
version of the examples is provided in Appendix B.
Safety Evaluation
Fig. 3 illustrates the comprehensive design of the ChiSafety-
Bench evaluation framework. We conduct an automatic eval-
uation of two types of data: risk content identification and
refusal to answer. The task type for risk content identifica-
tion data is multiple-choice questions(MCQ), while the task
type for refusal to answer data is in the form of question-
answering(QA).
Evaluation for MCQ
As illustrated in Fig. 3(a), the eval-
uation process involves directly feeding the multiple-choice
questions into the evaluated LLM to obtain responses. Then
we extract the predicted options from responses via meticu-
lously crafted rules. Subsequently, the predicted options are
compared with ground truth, thereby evaluating the model’s
capability in risk identification. Given that each question has
only one correct answer, accuracy metric can be employed
to provide an automatic evaluation.
For MCQ subset, suppose that there are N correct, N wrong
MCQs correctly and falsely answered by the evaluated
models. Specifically, N correct
i
, N wrong
i
represent the cor-
responding number in the i-th risk area. We report the
overall accuracy and the accuracy in the i-th area by
ACC −O = N correct/(N correct + N wrong) and ACCi =
N correct
i
/(N correct
i
+ N wrong
i
) respectively.
Evaluation for QA
Fig. 3(b) illustrates our approach to
safety evaluation. Initially, we feed the risky question into
the evaluated model to generate an answer. Subsequently,
given the question and the corresponding response, we uti-
lize an evaluator to determine the degree of refusal exhibited
by the response towards the question. In designing the evalu-
ator’s prompt template, we categorize the refusal degree into
four class labels(highlighted red in Fig. 3): Non-refusal with
Risky Response, Non-refusal with Harmless Response, Di-
rect Refusal, and Refusal with Responsible Guidance. Then
we extract class label from the evaluator’s response, with
each of the four labels corresponding to 0, 1, 2, and 3 re-
spectively. The numerical value of the refusal degree quan-
titatively indicates the extent of refusal, with higher values
signifying a greater level of refusal. The experiment is con-
ducted in a zero-shot setting, employing the open-source
LLM Qwen-72B as the evaluator. The prompt design tem-
plate and the mapping table from class label to refusal degree
value are shown in Fig. 3(b). Finally, we calculate the rejec-
tion rate(RR-1) by considering the proportion of refusal re-
sponses (degrees 2 and 3) to the total data. Additionally, we
compute the responsibility rate(RR-2) using the proportion
of responsible refusals (degree 3) to the total data and the
harmfulness rate(HR) by considering the proportion of non-
refusal yet harmful responses (degree 0) to the total data.

--- Page 6 ---

Figure 4: The overall accuracy(ACC −O) and accuracy in the i-th areas(ACCi) for MCQ to evaluate risk content identification
capabilities.
With regard to the QA subset, N d0, N d1, N d2, N d3 rep-
resent the number of questions where the evaluated model
does not refuse and provides a risky response(degree 0),
does not refuse and provides a harmless response(degree
1), directly refuses(degree 2), and refuses with responsible
guidance(degree 3), respectively. N d0
i , N d1
i , N d2
i , N d3
i
de-
note the corresponding number of questions in the i-th risk
area. We report the overall rejection rate, the responsibil-
ity rate, and the harmfulness rate by RR −1 = (N d2 +
N d3)/(N d0 +N d1 +N d2 +N d3), RR−2 = N d3/(N d0 +
N d1 +N d2 +N d3), and HR = N d0/(N d0 +N d1 +N d2 +
N d3). Moreover, we calculate the rejection rate, the respon-
sibility rate, and the harmfulness rate in the i-th risk areas
by RR −1i = (N d2
i
+ N d3
i )/(N d0
i
+ N d1
i
+ N d2
i
+ N d3
i ),
RR −2i = N d3
i /(N d0
i
+ N d1
i
+ N d2
i
+ N d3
i ), and HRi =
N d0
i /(N d0
i
+ N d1
i
+ N d2
i
+ N d3
i ).
To validate the effectiveness of our automatic evalua-
tor Qwen-72B, we randomly sample 563 examples from
5630(563*10) QA pairs totally answered by 10 evaluated
models and compare the correlation between automatic and
manual evaluations on these instances. The manual evalua-
tion is conducted by three human annotators, and the results
are consolidated via majority voting. Subsequently, these re-
sults are compared against the automatic evaluations pro-
duced by Qwen. The correlation between Qwen’s evaluation
and human evaluation are found to be Kendall Tau=0.815,
Spearman=0.842, Pearson=0.825, indicating a strong corre-
lation in the ability to judge whether a question should be
rejected. This demonstrates the effectiveness of employing
Qwen-72B as an automatic evaluator to replace manual eval-
uation.
4
Experiments
Experimental Setup
To comprehensively evaluate the safety capabilities of con-
temporary LLMs, we test a series of widely recognized mod-
els that are proficient in generating Chinese content based on
our benchmark dataset. Our evaluation encompasses 10 Chi-
nese LLMs from 4 distinct series: Baichuan(Baichuan2-7B-
Chat, Baichuan2-13B-Chat), ChatGLM(ChatGLM3-6B),
Qwen(Qwen1.5-7B-Chat, Qwen1.5-14B-Chat, Qwen1.5-
32B-Chat, Qwen1.5-72B-Chat, Qwen1.5-110B-Chat), and
Yi(Yi-6B-Chat, Yi-34B-Chat). Under a zero-shot setup, we
utilize 2030 benchmark samples to assess these models.
Evaluation for Risk Content Identification
The overall assessment of risk content identification capa-
bilities, as shown in Fig. 8(a), reveals that the Qwen se-
ries typically achieves higher ACC-O compared to other
series. Specifically, Qwen1.5-72B-Chat stands out with the
highest overall accuracy score of 91.13%. This impressive
performance exceeds the optimal model Yi-6B-Chat from
the second-best series by more than 5 percentage points. In
contrast, the ChatGLM series exhibits the lowest ACC-O,
with ChatGLM3-6B scoring the lowest at 41.16%. Further-
more, the Qwen series and Yi series have optimal models
with sizes of 72B and 6B, respectively, while the maximum
sizes for these series are 110B and 34B. This indicates a
non-positive correlation between model size and risk con-
tent identification capabilities.
The accuracy in different risk areas, as depicted in
Fig. 8(b), reveals the Qwen and Yi series both achieve
commendable performance in specific areas. Specifically,
Qwen1.5-14B-Chat excels in addressing discrimination,
while Qwen1.5-32B-Chat performs best in handling vi-
olation of values, commercial irregularities and secu-
rity requirements for specific services. Qwen1.5-72B-Chat
demonstrates superiority in identifying infringements of oth-
ers’ rights. Notably, there are significant disparities among
the evaluated LLMs in certain areas, such as discrimina-
tion and infringement. This observation provides valuable
insights into identifying the safety concerns that require par-
ticular attention in each LLM. The specific ACC of 10 mod-
els across 31 fine-grained categories can be found in Ap-
pendix C.1.
Evaluation for Refusal to Answer
As indicated in Table 2, the Qwen series consistently exhibit
stronger abilities to refuse risky questions compared to other
series, whereas the Yi series demonstrates notable deficien-
cies in managing refusal risks.

--- Page 7 ---

Overall
Discrimination
Violation of Values
RR-1 ↑
RR-2 ↑
HR ↓
RR-1 ↑
RR-2 ↑
HR ↓
RR-1 ↑
RR-2 ↑
HR ↓
Baichuan2-7B-Chat
64.30%
64.30%
3.02%
49.80%
49.80%
1.63%
75.47%
75.47%
4.09%
Baichuan2-13B-Chat
68.03%
67.85%
3.37%
52.65%
52.24%
2.45%
79.87%
79.87%
4.09%
ChatGLM3-6B
65.36%
65.19%
3.91%
49.80%
49.39%
2.04%
77.36%
77.36%
5.35%
Qwen1.5-7B-Chat
67.32%
67.32%
1.07%
53.06%
53.06%
0.82%
78.30%
78.30%
1.26%
Qwen1.5-14B-Chat
66.43%
66.25%
2.13%
51.84%
51.43%
0.82%
77.67%
77.67%
3.14%
Qwen1.5-32B-Chat
69.63%
69.27%
1.60%
56.33%
55.92%
0.41%
79.87%
79.56%
2.52%
Qwen1.5-72B-Chat
68.03%
68.03%
1.78%
53.47%
53.47%
0.82%
79.25%
79.25%
2.52%
Qwen1.5-110B-Chat
69.98%
69.98%
0.36%
53.47%
53.47%
0.00%
82.70%
82.70%
0.63%
Yi-6B-Chat
62.70%
62.17%
4.62%
45.71%
44.90%
3.27%
75.79%
75.47%
5.66%
Yi-34B-Chat
63.06%
63.06%
3.73%
43.27%
43.27%
2.86%
78.30%
78.30%
4.40%
Table 2: RR-1, RR-2 and HR results on the refusal to answer subset. The optimal values under the current metric are highlighted
bold.
In terms of the overall performance of the models,
Qwen1.5-110B-Chat and Yi-6B-Chat respectively demon-
strate the best and worst capabilities in managing refusal
risks across the three evaluation metrics. Specifically, re-
garding the refusal capabilities, even the best-performing
Qwen-110B-Chat achieves a RR-1 of merely 69.98%, un-
derscoring the prevalent room for improvement in all mod-
els’ ability to mitigate refusal risks. Additionally, the RR-2
of all models are very close or equal to their RR-1, indicat-
ing that existing Chinese LLMs tend to provide responsi-
ble guiding information while declining to answer. As for
HR, these models generally exhibit low levels of poten-
tial harm, with Qwen-110B-Chat boasting a HR as low as
0.36%, whereas Yi-6B-Chat has the highest HR at 4.62%.
The performance in specific domains is similar to the
overall performance. Notably, RR-1 and RR-2 of all models
evaluated in the discrimination domain are generally lower
than those in the values violation domain, indicating that
the models generally have certain deficiencies in protecting
against risks in the discrimination domain. Our dataset pro-
vides valuable guidance for the construction of model safety
barriers in different risk areas. Detailed performances across
17 fine-grained categories are presented in Appendix C.2.
Ablation Study
To affirm the indispensability of multi-turn dialogue data
within the refusal to answer subset, we further divide this
subset into two subsets: risky questions without and with
conversational history. Subsequently, we evaluate the over-
all RR-1, RR-2, and HR metrics for these two subsets sep-
arately, and the results are summarized in Table 3. The de-
tailed performance of 10 models in response to risk ques-
tions without and with conversational history can be found
in Appendix C.3.
Table 3 reveals that all models encounter significant ob-
stacles in rejecting risky questions with conversational his-
tory. Compared to single-round questions, the model’s RR-
1 for risk questions with dialogue history decreased by
24.96% to 50.33%, highlighting the notable deficiencies of
current Chinese LLMs in handling risky dialogues. When
evaluating the LLMs’ responsible guidance capabilities,
RR-1 ↑
RR-2 ↑
HR ↓
Baichuan2-7B-Chat
72.29%/27.72%
72.29%/27.72%
0.65%/13.86%
Baichuan2-13B-Chat
77.06%/26.73%
76.84%/26.73%
0.43%/26.73%
ChatGLM3-6B
73.38%/28.71%
73.38%/27.72%
1.08%/16.83%
Qwen1.5-7B-Chat
73.59%/38.61%
73.59%/38.61%
0.43%/3.96%
Qwen1.5-14B-Chat
73.16%/35.64%
73.16%/34.65%
0.22%/10.89%
Qwen1.5-32B-Chat
77.71%/32.67%
77.27%/32.67%
0.22%/7.92%
Qwen1.5-72B-Chat
73.81%/41.58%
73.81%/41.58%
0.22%/8.91%
Qwen1.5-110B-Chat
74.46%/49.50%
74.46%/49.50%
0.00%/1.98%
Yi-6B-Chat
71.21%/23.76%
70.78%/22.77%
0.87%/21.78%
Yi-34B-Chat
69.70%/32.67%
69.70%/32.67%
0.65%/17.82%
Table 3: The performance between risky questions without
and with conversational history on the refusal to answer sub-
set. From left to right, the values reported are as follows:
risky questions without and with conversational history.
the peak RR-2 score for single-turn QA reaches 77.27%,
demonstrating their effectiveness in guiding under single-
turn risky situations. However, in multi-turn dialogue en-
vironments, the peak RR-2 score plummets to 49.50%, in-
dicating a significant degradation of the models’ guidance
abilities in complex dialog scenarios. Furthermore, the HR
for single-turn questions are generally low, with the highest
being only 1.98%, whereas they sharply increase to a max-
imum of 26.73% in multi-turn dialogues, further corrobo-
rating the limitations of the models in managing multi-turn
risky dialogues. In summary, existing models exhibit notable
shortcomings in handling complex risky dialogues, confirm-
ing the necessity of incorporating multi-turn data.
5
Conclusion
We introduce CHiSafetyBench, a specialized and credible
benchmark designed based on a Chinese hierarchical safety
taxonomy. CHiSafetyBench encompasses 1567 multiple-
choice questions and 563 risky questions, evaluating the
safety of LLMs from two perspectives: risk content identifi-
cation and refusal to respond to risky questions. Through an
automated assessment of 10 Chinese LLMs from four dis-
tinct series, the results from CHiSafetyBench reveal vary-
ing performances across different models, aiming to provide

--- Page 8 ---

LLM developers with a safety reference for model usage and
advancing research on the safety and reliability of Chinese
LLMs.
References
Achiam, J.; Adler, S.; Agarwal, S.; Ahmad, L.; Akkaya, I.;
Aleman, F. L.; Almeida, D.; Altenschmidt, J.; Altman, S.;
Anadkat, S.; et al. 2023.
Gpt-4 technical report.
arXiv
preprint arXiv:2303.08774.
Bhardwaj, R.; and Poria, S. 2023.
Red-Teaming Large
Language Models using Chain of Utterances for Safety-
Alignment. ArXiv, abs/2308.09662.
Deng, Y.; Zhang, W.; Pan, S. J.; and Bing, L. 2023. Mul-
tilingual Jailbreak Challenges in Large Language Models.
ArXiv, abs/2310.06474.
Dhamala, J.; Sun, T.; Kumar, V.; Krishna, S.; Pruksachatkun,
Y.; Chang, K.-W.; and Gupta, R. 2021.
BOLD: Dataset
and Metrics for Measuring Biases in Open-Ended Language
Generation. Proceedings of the 2021 ACM Conference on
Fairness, Accountability, and Transparency.
Dong, Z.; Zhou, Z.; Yang, C.; Shao, J.; and Qiao, Y.
2024. Attacks, defenses and evaluations for llm conversa-
tion safety: A survey. arXiv preprint arXiv:2402.09283.
Gehman, S.; Gururangan, S.; Sap, M.; Choi, Y.; and Smith,
N. A. 2020. RealToxicityPrompts: Evaluating Neural Toxic
Degeneration in Language Models. In Findings of the Asso-
ciation for Computational Linguistics: EMNLP 2020, 3356–
3369. Association for Computational Linguistics.
Han, X.; Baldwin, T.; and Cohn, T. 2023. Fair Enough: Stan-
dardizing Evaluation and Model Selection for Fairness Re-
search in NLP. In Conference of the European Chapter of
the Association for Computational Linguistics.
Han, X.; Shen, A.; Cohn, T.; Baldwin, T.; and Frermann, L.
2022. Systematic Evaluation of Predictive Fairness. In Pro-
ceedings of the 2nd Conference of the Asia-Pacific Chap-
ter of the Association for Computational Linguistics and the
12th International Joint Conference on Natural Language
Processing (Volume 1: Long Papers), 68–81. Association for
Computational Linguistics.
Hartvigsen, T.; Gabriel, S.; Palangi, H.; Sap, M.; Ray, D.;
and Kamar, E. 2022.
ToxiGen: A Large-Scale Machine-
Generated Dataset for Adversarial and Implicit Hate Speech
Detection. In Annual Meeting of the Association for Com-
putational Linguistics.
Huang, X.; Ruan, W.; Huang, W.; Jin, G.; Dong, Y.; Wu,
C.; Bensalem, S.; Mu, R.; Qi, Y.; Zhao, X.; et al. 2023. A
survey of safety and trustworthiness of large language mod-
els through the lens of verification and validation.
arXiv
preprint arXiv:2305.11391.
Li, L.; Dong, B.; Wang, R.; Hu, X.; Zuo, W.; Lin, D.;
Qiao, Y.; and Shao, J. 2024. SALAD-Bench: A Hierarchical
and Comprehensive Safety Benchmark for Large Language
Models. arXiv preprint arXiv:2402.05044.
Lin, S.; Hilton, J.; and Evans, O. 2022. TruthfulQA: Mea-
suring How Models Mimic Human Falsehoods. In Muresan,
S.; Nakov, P.; and Villavicencio, A., eds., Proceedings of the
60th Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), 3214–3252. Dublin,
Ireland: Association for Computational Linguistics.
Lin, Z.; Wang, Z.; Tong, Y.; Wang, Y.; Guo, Y.; Wang, Y.;
and Shang, J. 2023.
ToxicChat: Unveiling Hidden Chal-
lenges of Toxicity Detection in Real-World User-AI Con-
versation.
In Findings of the Association for Computa-
tional Linguistics: EMNLP 2023, 4694–4702. Association
for Computational Linguistics.
Reimers, N.; and Gurevych, I. 2019. Sentence-BERT: Sen-
tence Embeddings using Siamese BERT-Networks. In Con-
ference on Empirical Methods in Natural Language Pro-
cessing.
Rusnachenko, N.; Golubev, A.; and Loukachevitch, N. 2024.
Large Language Models in Targeted Sentiment Analysis.
arXiv preprint arXiv:2404.12342.
Shen, X.; Chen, Z. J.; Backes, M.; Shen, Y.; and Zhang, Y.
2023. ”Do Anything Now”: Characterizing and Evaluating
In-The-Wild Jailbreak Prompts on Large Language Models.
ArXiv, abs/2308.03825.
Sun, H.; Zhang, Z.; Deng, J.; Cheng, J.; and Huang, M.
2023. Safety assessment of chinese large language models.
arXiv preprint arXiv:2304.10436.
Touvron, H.; Lavril, T.; Izacard, G.; Martinet, X.; Lachaux,
M.-A.; Lacroix, T.; Rozi`ere, B.; Goyal, N.; Hambro, E.;
Azhar, F.; et al. 2023. Llama: Open and efficient founda-
tion language models. arXiv preprint arXiv:2302.13971.
Wang, W.; Tu, Z.; Chen, C.; Yuan, Y.; tse Huang, J.; Jiao,
W.; and Lyu, M. R. 2023. All Languages Matter: On the
Multilingual Safety of Large Language Models.
ArXiv,
abs/2310.00905.
Wang, Y.; Li, H.; Han, X.; Nakov, P.; and Baldwin, T. 2024.
Do-Not-Answer: Evaluating Safeguards in LLMs. In Gra-
ham, Y.; and Purver, M., eds., Findings of the Association
for Computational Linguistics: EACL 2024, 896–911. St.
Julian’s, Malta: Association for Computational Linguistics.
Xu, D.; Chen, W.; Peng, W.; Zhang, C.; Xu, T.; Zhao,
X.; Wu, X.; Zheng, Y.; and Chen, E. 2023a.
Large lan-
guage models for generative information extraction: A sur-
vey. arXiv preprint arXiv:2312.17617.
Xu, G.; Liu, J.; Yan, M.; Xu, H.; Si, J.; Zhou, Z.; Yi, P.; Gao,
X.; Sang, J.; Zhang, R.; et al. 2023b. Cvalues: Measuring
the values of chinese large language models from safety to
responsibility. arXiv preprint arXiv:2307.09705.
Xu, L.; Zhao, K.; Zhu, L.; and Xue, H. 2023c. SC-Safety:
A Multi-round Open-ended Question Adversarial Safety
Benchmark for Large Language Models in Chinese. ArXiv,
abs/2310.05818.
Zhang, J.; Zhang, H.; Zhang, D.; Liu, Y.; and Huang,
S. 2023a.
Beam retrieval: General end-to-end re-
trieval for multi-hop question answering.
arXiv preprint
arXiv:2308.08973.
Zhang, Z.; Lei, L.; Wu, L.; Sun, R.; Huang, Y.; Long,
C.; Liu, X.; Lei, X.; Tang, J.; and Huang, M. 2023b.
Safetybench: Evaluating the safety of large language
models with multiple choice questions.
arXiv preprint
arXiv:2309.07045.

--- Page 9 ---

Zou, A.; Wang, Z.; Kolter, J. Z.; and Fredrikson, M. 2023.
Universal and Transferable Adversarial Attacks on Aligned
Language Models. ArXiv, abs/2307.15043.

--- Page 10 ---

A
Appendix A. Search Keywords for Multiple Choice Questions
Figure 5: Keyword examples for 31 category, with ’-’ indicating that the MCQ data for this category is sourced from Safety-
Bench and does not require keywords to search engines. English version of these keywords are also provided.

--- Page 11 ---

B
Appendix B. Examples
Figure 6: Entire examples of multiple choice questions and question-answering subset. Please note that the English translations
are only for illustrative purposes, while the original data only contains Chinese.

--- Page 12 ---

C
Appendix C. Experiments Details
C.1 ACC for MCQ across 31 Risk Categories
Figure 7: ACC for 10 models across 31 risk categories on the MCQ subset.

--- Page 13 ---

C.2 Detail Performance on Refusal of Answer Subset
Figure 8: RR-1 for 10 models across 17 risk categories on the refusal to answer subset.

--- Page 14 ---

Figure 9: RR-2 for 10 models across 17 risk categories on the refusal to answer subset.

--- Page 15 ---

Figure 10: HR for 10 models across 17 risk categories on the refusal to answer subset.

--- Page 16 ---

C.3 Evaluation Metrics of Risky Questions without and with Conversational History
Overall
Discrimination
Violation of Values
RR-1 ↑
RR-2 ↑
HR ↓
RR-1 ↑
RR-2 ↑
HR ↓
RR-1 ↑
RR-2 ↑
HR ↓
Baichuan2-7B-Chat
72.29%
72.29%
0.65%
52.55%
52.55%
0.51%
86.84%
86.84%
0.75%
Baichuan2-13B-Chat
77.06%
76.84%
0.43%
58.67%
58.16%
1.02%
90.60%
90.60%
0.00%
ChatGLM3-6B
73.38%
73.38%
1.08%
52.55%
52.55%
1.02%
88.72%
88.72%
1.13%
Qwen1.5-7B-Chat
73.59%
73.59%
0.43%
54.59%
54.59%
0.51%
87.59%
87.59%
0.38%
Qwen1.5-14B-Chat
73.16%
73.16%
0.22%
53.57%
53.57%
0.51%
87.59%
87.59%
0.00%
Qwen1.5-32B-Chat
77.71%
77.27%
0.22%
59.69%
59.18%
0.00%
90.98%
90.60%
0.38%
Qwen1.5-72B-Chat
73.81%
73.81%
0.22%
52.55%
52.55%
0.00%
89.47%
89.47%
0.38%
Qwen1.5-110B-Chat
74.46%
74.46%
0.00%
52.04%
52.04%
0.00%
90.98%
90.98%
0.00%
Yi-6B-Chat
71.21%
70.78%
0.87%
50.00%
49.49%
0.00%
86.84%
86.47%
1.50%
Yi-34B-Chat
69.70%
69.70%
0.65%
43.88%
43.88%
1.02%
88.72%
88.72%
0.38%
Table 4: RR-1, RR-2 and HR results of risky questions without conversational history on the refusal to answer subset.
Overall
Discrimination
Violation of Values
RR-1 ↑
RR-2 ↑
HR ↓
RR-1 ↑
RR-2 ↑
HR ↓
RR-1 ↑
RR-2 ↑
HR ↓
Baichuan2-7B-Chat
27.72%
27.72%
13.86%
38.78%
38.78%
6.12%
17.31%
17.31%
21.15%
Baichuan2-13B-Chat
26.73%
26.73%
16.83%
28.57%
28.57%
8.16%
25.00%
25.00%
25.00%
ChatGLM3-6B
28.71%
27.72%
16.83%
38.78%
36.73%
6.12%
19.23%
19.23%
26.92%
Qwen1.5-7B-Chat
38.61%
38.61%
3.96%
46.94%
46.94%
2.04%
30.77%
30.77%
5.77%
Qwen1.5-14B-Chat
35.64%
34.65%
10.89%
44.90%
42.86%
2.04%
26.92%
26.92%
19.23%
Qwen1.5-32B-Chat
32.67%
32.67%
7.92%
42.86%
42.86%
2.04%
23.08%
23.08%
13.46%
Qwen1.5-72B-Chat
41.58%
41.58%
8.91%
57.14%
57.14%
4.08%
26.92%
26.92%
13.46%
Qwen1.5-110B-Chat
49.50%
49.50%
1.98%
59.18%
59.18%
0.00%
40.38%
40.38%
3.85%
Yi-6B-Chat
23.76%
22.77%
21.78%
28.57%
26.53%
16.33%
19.23%
19.23%
26.92%
Yi-34B-Chat
32.67%
32.67%
17.82%
40.82%
40.82%
10.20%
25.00%
25.00%
25.00%
Table 5: RR-1, RR-2 and HR results of risky questions with conversational history on the refusal to answer subset.

```
