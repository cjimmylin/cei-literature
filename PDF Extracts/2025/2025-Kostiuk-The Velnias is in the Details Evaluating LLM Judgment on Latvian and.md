---
title: "2025-Kostiuk-The Velnias is in the Details Evaluating LLM Judgment on Latvian and - PDF Extract"
source_pdf: "2025-Kostiuk-The Velnias is in the Details Evaluating LLM Judgment on Latvian and.pdf"
pages: 14
extracted_at: "2026-02-15T17:54:26.280894"
---

# PDF Extract: 2025-Kostiuk-The Velnias is in the Details Evaluating LLM Judgment on Latvian and

**Source PDF:** 2025-Kostiuk-The Velnias is in the Details Evaluating LLM Judgment on Latvian and.pdf
**Total Pages:** 14

---

## Content

```
--- Page 1 ---

The Veln(ia)s is in the Details: Evaluating LLM Judgment on Latvian and
Lithuanian Short Answer Matching
Yevhen Kostiuk1,2
1ARG-tech,
University of Dundee
2OpenBabylon
ykostiuk001@dundee.ac.uk
Oxana Vitman
University of Bremen
Łukasz Gagała
Georg-August
Universit¨at G¨ottingen
Artur Kiulian
OpenBabylon
Abstract
In this work, we address the challenge of
evaluating large language models (LLMs)
on the short answer matching task for Lat-
vian and Lithuanian languages. We intro-
duce novel datasets consisting of 502 Lat-
vian and 690 Lithuanian question-answer
pairs. For each question-answer pair, we
generated matched and non-matched an-
swers using a set of alteration rules specif-
ically designed to introduce small but
meaningful changes in the text.
These
generated answers serve as test cases to as-
sess the ability of LLMs to detect subtle
differences in matching of the original an-
swers. A subset of the datasets was manu-
ally verified for quality and accuracy. Our
results show that while larger LLMs, such
as QWEN2.5 72b and LLaMa3.1 70b,
demonstrate near-perfect performance in
distinguishing matched and non-matched
answers, smaller models show more vari-
ance. For instance, LLaMa3.1 8b and Eu-
roLLM 9b benefited from few-shot exam-
ples, while Mistral Nemo 12b underper-
formed on detection of subtle text alter-
ation, particularly in Lithuanian, even with
additional examples.
QWEN2.5 7b and
Mistral 7b were able to obtain a strong and
comparable performance to the larger 70b
models in zero and few shot experiments.
Moreover, the performance of Mistral 7b
was weaker in few shot experiments. The
code and the dataset are available on our
GitHub1.
1
Introduction
In educational domain, open-ended questions are
commonly used and can be defined as questions
1HIDDEN FOR REVIEW
that require a more elaborate response than sim-
ple yes-no or selection of a correct choice. These
questions help to encourage a discussion, share
ideas and provide more freedom for a student.
Evaluation of responses to the open-ended ques-
tion is a time-consuming and difficult task that re-
quires an evaluator to carefully read each answer
and compare it with the correct answers, ensuring
they match. Automating this process makes it eas-
ier for evaluators to provide a feedback and ana-
lyze errors faster (Pillai et al., 2018; Sreevidhya
and Narayanan, 2021).
The automatic short answer matching task ad-
dresses this challenge.
The goal of the task is
to predict whether an answer to the question is
matching a correct answer. With the introduction
of LLMs, reasonable performance was achieved
on English and other high-resource languages for
this problem (Ivanova and Handschuh, 2024). On
the other hand, when it comes to low-resource set-
tings, LLMs demonstrated weaker results, as well
as displayed biases (Hackl et al., 2023; Lai et al.,
2023).
In this work, we focus on Latvian and Lithua-
nian answer matching task, specifically on a de-
tection of correct and incorrect responses that are
similar to a set of reference “gold” answers, but
differ in the key detail(s) to the question.
We
automatically
generated
open-ended
question-answer datasets for these languages
based on Wikipedia.
For this task, we do not
focus on the factual correctness of the answers,
as it does not affect the task.
Each element of
the dataset contains a question and its reference
answer. Then we generated a set of answers that
are matched with the reference answer and a set of
non-matched answers. The non-matched answers
are created as similarly as possible to the reference
answers with respect to the words inclusion, but
with the key words changed to make it incorrect.
To generate the answers, we formulated different
arXiv:2501.09164v1  [cs.CL]  15 Jan 2025

--- Page 2 ---

Figure 1: Example of the element from Lithuanian
generated dataset.
text alteration rules (AR) that are minor when
it comes to a text change, but semantically are
major. For each rule, the different LLMs with a
few shot generation process were used. Finally,
to ensure the quality, we manually evaluated a
sample of the data and filtered the final dataset
based on it. We expect the models to obtain high,
almost perfect, results on this task.
We formulated the following research questions
in this paper.
Q1:
Are LLMs capable of correctly identifying
matched and non-matched answers with the pro-
posed alteration rules?
Q2:
Is there a difference between few-shot and
zero-shot inference for different LLMs for this
task?
Our contributions are the following:
• We automatically generated a dataset of 502
Latvian and 690 Lithuanian question-answer
pairs based on Wikipedia. We defined and
generated a list of matched and non-matched
answers to each pair of question-answer, re-
sulting in 3,012 and 4,830 elements for Lat-
vian and Lithuanian respectively, and par-
tially manually evaluated samples of the
datasets.
• We
evaluated
LLaMa3.1
(8b
and
70b) (Dubey et al., 2024), Mistral Nemo 12b
and Mistral 7b (Jiang et al., 2023), EuroLLM
9b (Martins et al., 2024), and QWEN2.5
(7b and 72b) (Team, 2024; Yang et al.,
2024) models and compared their achieved
accuracy scores per AR and overall.
• We evaluated the models in zero-shot and
few-shot settings and their performance
based on different ARs of matched and non-
matched answers.
Our findings showed that larger LLMs, such as
QWEN2.5 72b and LLaMa3.1 70b, consistently
performed well across both Latvian and Lithua-
nian datasets, effectively distinguishing matched
and non-matched answers in both zero shot and
few shot experiments. However, smaller models
demonstrated variation in their results. LLaMa3.1
8b and EuroLLM 9b showed improved perfor-
mance with few-shot examples, while Mistral
Nemo 12b showed limitations, particularly in
Lithuanian.
QWEN2.5 7b and Mistral 7b were
able to obtain a similar the performance to the
larger 70b models, with Mistral 7b showing
weaker performance in few shot experiments.
2
Related Work
Answer matching task can be viewed as a subtask
of the automatic short answer grading (ASAG).
The definition of what is a short answer and if
it is acceptable can vary depending on the do-
main (Burrows et al., 2015; Bonthu et al., 2021).
Nevertheless, all the definitions involve high se-
mantic similarity between the correct answer(s)
and predicted answers. The grading scale is also
can be domain dependent (Zhang et al.; Divya
et al., 2023; Krithika and Narayanan, 2015).
With the development of deep learning meth-
ods, they were widely used for the task, as
they provide better robustness towards syntac-
tic changes of the text rather than other meth-
ods (Bonthu et al., 2021), utilizing RNNs (Cai,
2019), CNNs (Chen and Zhou, 2019), transform-
ers (Sung et al., 2019; Willms and Pad´o, 2022) and
so on. Some of the suggested methods are aimed
to not only grade an answer, but to explain its flows
and inaccuracies (Tornqvist et al., 2023).
With the rise of generative large language mod-
els (LLMs), they were applied for ASAG as
well (Metzler et al., 2024; Ivanova and Hand-
schuh, 2024; Chu et al., 2024; Schneider et al.,
2023; Gr´evisse, 2024; Yancey et al., 2023; Yoon,
2023).
Analysis of LLMs for this task showed
that they are capable of predicting consistent rat-
ings for English (Hackl et al., 2023; Mizumoto and
Eguchi, 2023). However, studies showed that the
LLMs’ performance on the non-English datasets
is weaker (Lai et al., 2023; Dar ‘gis et al., 2024).

--- Page 3 ---

On the other hand, as any other NLP task, there
is a gap in the ASAG resources for low-resource
languages, including Nordic and Baltic. This area
lacks high-quality datasets for these languages.
The GPT-3.5 and GPT-4 models were evaluated
on Finnish ASAG (Chang and Ginter, 2024) on
the dataset of students’ answers in Finnish for
multiple subjects.
The study demonstrated that
the models assigned higher scores to the students’
answers than the human annotator and achieving
Quadratic Weighted Kappa (QWK) score of 0.44.
In (Chang et al., 2022), the authors considered
ASAG task as a paraphrase retrieval task, eval-
uating classical methods (TF-IDF) and different
transformer methods.
In (Dar`gis et al., 2022), the self-assessment
platform for Latvian language learners was pro-
posed and developed. The authors generated ex-
ercises automatically based on data from multi-
ple corpora (Lev¯ane-Petrova et al., 2023; Dar ‘gis
et al., 2022).
In (Stefanoviˇc et al., 2024), the
research on detecting AI generated answers in
Lithuanian was conducted, producing a dataset
with student answers, GPT generated answers and
its paraphrased versions.
The authors (Weegar
and Idestam-Almquist, 2024) created a dataset of
student answers in Swedish in programming lan-
guages, networking and the Internet, and data ab-
stractions and manipulations. The authors exam-
ined different machine learning methods to tackle
the task. In (Klevstuen, 2022), the use of informa-
tion retrieval and text mining methods were inves-
tigated to evaluate the content of Norwegian exam
answers in Computer Science. In our work, we re-
lease multi-domain publicly available datasets as
well as benchmark results for some of the open-
source multilingual LLMs.
3
Datasets
To generate answer matching datasets, the three-
stage pipeline was implemented.
Firstly, we used the approach for generat-
ing question-answer Knowledge and Instruction
Dataset (KID) based on Wikipedia, introduced
in (Kiulian et al., 2024) and adapted it for Latvian
(Lat-KID) and Lithuanian (Lit-KID). More details
are provided in the Section 3.1.
The generated
datasets consist of pairs of a question and a ref-
erence answer (assumed to be correct and relevant
to the question), as well as a factual information
that supports the answer.
Figure 2: Example of few-shot incorporating mi-
nor changes prompt for non-matched answers gen-
eration in Latvian. < . . . > indicate the sample
that requires prediction.
On the second stage, for each pair of question
and answer, we defined a list of different alteration
rules that rewrites reference answer to matched
or non-matched (more details are provided in the
Section 3.2). We used GPT-4o and LLaMa3 8b
(see Figure 1), utilizing separate prompts for each
rule. The non-matched prompts were composed in
a way that preserves as much words and semantics
of the reference answer as possible with changing
key words of the answer, while matched prompts
are more flexible.
Finally, the generated results were validated and
methods were filtered based on the accept ratio
(more details are provided in the Section 3.3).
3.1
Lat-KID and Lit-KID
Question-Answering Datasets
For each language, we extracted top 1,000 arti-
cles for each month of the last 12 month from
Wikipedia, resulting in 12,000 articles. From this
pool, 1,000 articles with the top cumulative counts
were extracted. The articles were filtered by their
relevance to the corresponding country with Gem-
ini 1.5 Pro (Team et al., 2024). Each article was
separated into the paragraphs and at least 3 ques-
tions were generated for it with Gemini 1.5 Pro.
The prompt contains additional fields to run a self-
check on the quality of the question (standalone,
in the correct language, natural sounding). The
prompts are available in the project’s GitHub.

--- Page 4 ---

The obtained Lat-KID dataset has 502 unique
questions. The average number of words in the
question is 9.83 and in the answer is 24.37. The
total number of words in the dataset (questions and
reference answers) is 17,172. The unique amount
of words is 5,058.
The obtained Lit-KID dataset has 690 unique
questions. The average number of words in the
question is 9.88 and in the answer is 29.02. The
total number of words in the dataset (questions and
reference answers) is 26,849. The unique amount
of words is 7,725.
3.2
Matched and Non-Matched Answers
Generation
Non-Matched Answers Generation.
We de-
fined two alteration rules for non-matched answers
generation: incorporating minor changes (IMC)
and changing domain related information (CDRI).
IMC includes changes to the text that change a
couple of key words like date, name, location etc,
while keeping everything else unchanged. CDRI
is similar to IMC, however its objective is to
change a key term to the similar from the same
domain. For example, changing the name of the
first president to the second one, etc.
To generate non-matched answers, we utilized
LLaMa3 7b2 and GPT-4o3.
When generating IMC and CDRI answers, the
model was presented with the few-shot example
prompts (see Figure 2).
Matched Answers Generation.
We defined
the following alteration rules for matched an-
swers generation: adding more question-related
entities (Ents), changing words to synonyms
(Synonyms), adding more background informa-
tion (MoreInfo), and style swap to exclamatory
(Exclamatory).
As previously, we used GPT-4o and LLaMa3
7b.
The models were presented with different
prompts per rule. The code and prompts are avail-
able in the GitHub repository for the project4 .
Postprocessing.
After the generating answers,
the duplicates were removed.
The resulting
amount of (question, reference answer, generated
answer) triplets is 3,012 (1,506 are matched and
2After manual evaluation, only IMC were generation was
accepted for Lat-KID and CDRI for Lit-KID.
3We experimented with LLaMa2 13b, however manual
evaluation showed much worse results.
4HIDDEN FOR REVIEW
other 1,506 are non-matched) for Latvian and
4,830 (2,760 are matched and 2,070 are non-
matched) for Lithuanian. The amount of matched
answers is 3,697. The amount of non-matched an-
swers is 1,809.
3.3
Manual Evaluation
We recruited two native speakers for Latvian and
Lithuanian to evaluate the quality of the final gen-
erated dataset. They were presented with a ran-
dom triplet of (question, reference answer, gener-
ated answer) and a description if the generated an-
swer was generated by matched or non-matched
method. Based on that, the annotators had to ac-
cept a triplet if the description fits the reference
and generated answers.
Otherwise, they had to
reject sample. The results are presented in Ap-
pendix A.
4
Methodology
To evaluate the LLMs capabilities and an influence
of the prompting strategy, we used two prompting
methods per language for this task: zero shot (ZS)
and few shot (FS). We set all the parameters to
defaults with a random seed of 2.
In all of the methods, the model were instructed
to start their output with True if the provided refer-
ence answer and a generated answer are matched
otherwise with False. ZS and FS shared the same
system prompt, but FS gave a model additional ex-
amples in corresponding language.
We evaluated LLaMa3.1 (8b and 70b) (Dubey
et al., 2024), Mistral Nemo 12b and Mistral
7b (Jiang et al., 2023), and QWEN2.5 (7b and
72b) (Team, 2024; Yang et al., 2024) models. To
parse the output, we checked if the model followed
instructions about the output. If it did not, we re-
trieved the key words: “True” or “False”. If none
of the words were presented, we counted it as an
incorrect prediction.
5
Results and Discussion
The results are presented in Table 1, and on Fig-
ures 3 and 4. Additionally, we measured a per-
centage of times, when model followed the pro-
vided format and started with “True” or “False”.
The majority of models were able to output the
correct format for 99% on Latvian samples. For
Lithuanian, LLaMa3.1 8b generated text in cor-
rect format in 89% of times in ZS settings. In case

--- Page 5 ---

(a) Zero shot
(b) Few shot
Figure 3: Accuracy scores per generated answer type for Latvian.
(a) Zero shot
(b) Few shot
Figure 4: Accuracy scores per generated answer type for Lithuanian.
LT
LV
ZS
FS
ZS
FS
QWEN2.5 72b
0.99
0.99
0.99
0.99
LLaMa3.1 70b
0.99
0.99
0.99
0.99
Mistral Nemo 12b
0.96
0.94
0.96
0.94
EuroLLM 9b
0.13
0.97
0.05
0.84
LLaMa3.1 8b
0.89
0.98
0.87
0.96
QWEN2.5 7b
0.98
0.98
0.97
0.97
Mistral 7b
0.95
0.91
0.95
0.91
Table 1: F1 scores of binary matching. LT and LV
refer to Lithuanian and Latvian respectively. ZS
and FS refer to zero shot and few shot respectively.
of the FS, this value is 99%. Other models con-
sistently followed the format with a rate of 99%.
EuroLLM 9b was not able to follow a format at all
in ZS settings for both languages, even though its
results were legible, but impossible to parse. How-
ever, when presented with a few shot examples, it
generated expected format.
Our results demonstrated that larger LLMs
(with 70b parameters) are capable of reliably de-
tect matched and non-matched answers in Lithua-
nian and Latvian.
We hypothesized that LLMs
would output near perfect scores, however, smaller
models performed differently. In case of Mistral
Nemo, there was a slight decrease of results when
switched from zero shot to a few shot approach
in both languages. On the contrary, LLaMa3.1 8b
performed better in a few shot scenario, improv-
ing its ZS score on 9%. QWEN2.5 7b performed
nearly perfectly, achieving 99 accuracy score in
both settings.
Deeper analysis of results indicated that in
case of Latvian, most of the models (except for
LLaMa3.1 8b, MIstral 7b, and EuroLLM 9b)
showed almost perfect performance on all the
generated types of matched and non-matched an-

--- Page 6 ---

swers. LLaMa3.1 8b was able to pick up non-
matched answers in ZS and FS settings, but strug-
gled with matched answers, demonstrating a bias
towards negative answers. However, exposing it
with the additional examples boosted its scores
to the same level as others. EuroLLM was not
able to follow instructions in zero shot prompts,
therefore performing poorly. However, in the few
shot settings, the model was able to detect non-
matched answers, but had less success with match-
ing answers, demonstrating bias towards negative
answers. Mistral 7b perfromed well in ZS exper-
iments, but showed a weaker performance in FS
for non-match generated samples.
For Lithuanian, the least reliable model was
Mistral Nemo 12b. It demonstrated a strong per-
formance on the matched answers with more in-
formation and more entities, but was not able to ef-
fectively detect synonyms changes in both ZS and
FS settings. In case of this model, providing more
examples to the model did not have a noticeable
effect. Interestingly, EuroLLM showed the same
pattern as for Latvian in ZS, but was able to get
a comparable results with the 70b groups of mod-
els in FS settings. It indicates that the model has
a better understanding of Lithuanian than Latvian
when it comes to this task, and can perform well
when provided with examples.
Therefore, based on our observations, we can
address each of the research questions we formu-
lated.
Q1: Are LLMs capable of correctly identify-
ing matched and non-matched answers with the
proposed alteration rules ? Overall, the evaluated
models were able to accurately identify, which
answers are matched and which are not. LLMs
with the greater number of parameters showed a
very consistent performance, when smaller model
can have difficulties with Latvian or Lithuanian.
Specifically, LLaMa3.1 8b and EuroLLM 9b re-
quire additional examples, when QWEN2.5 7b
and Mistral 7b are on par with the larger mod-
els. Moreover, we found specific types of alter-
nation rules that models had more difficulties to
pick up. Specifically LLaMa3.1 8b and EuroLLM
9b had difficulties with added entities in the text
in Latvian. Mistral 7b struggled with incorporat-
ing minor changes and changing domain related
information rules in Latvian FS settings. Mistral
Nemo obtained weaker performance on changing
words to synonyms and style swap to exclamatory
(Exclamatory) rules in Lithuanian.
Q2: Is there a difference between few-shot and
zero-shot inference for different LLMs for this
task ? Our findings showed that few shot approach
did not improve the scores of the larger models:
they are already very high. However, it can be
helpful in case of some smaller models, especially
with EuroLLM 9b. In case of Mistral 7b, the per-
fromance was decreased with adding more exam-
ples. On the other hand, if the model struggles
with a language, providing more examples will not
necessarily improves its performance (e.g. Mistral
Nemo in Lithuanian or Mistral 7b) for this task.
6
Conclusion
In conclusion, our findings demonstrate that large
language models (LLMs) with greater parameter
counts, such as QWEN2.5 72b and LLaMa3.1
70b, consistently achieve high accuracy in dis-
tinguishing matched and non-matched answers
across both Latvian and Lithuanian, regardless
of zero-shot or few-shot settings. Smaller mod-
els showed less robustness, with LLaMa3.1 8b
and EuroLLM 9b benefiting from additional ex-
amples in few-shot scenarios. Mistral Nemo 12b
struggled with detecting certain nuances, partic-
ularly in Lithuanian. QWEN2.5 7b and Mistral
7b were able to obtain a similar the performance
to the larger 70b models, but in case of Mistral
7b the performance decreased in with a few shot
approach. These results highlight the robustness
of larger models and the potential for targeted
improvements in smaller ones to address answer
matching task with the defined set of alteration
rules.
References
Sridevi Bonthu,
S Rama Sree,
and MHM Kr-
ishna Prasad. 2021. Automated short answer grad-
ing using deep learning: A survey.
In Machine
Learning and Knowledge Extraction: 5th IFIP TC
5, TC 12, WG 8.4, WG 8.9, WG 12.9 Interna-
tional Cross-Domain Conference, CD-MAKE 2021,
Virtual Event, August 17–20, 2021, Proceedings 5,
pages 61–78. Springer.
Steven Burrows, Iryna Gurevych, and Benno Stein.
2015. The eras and trends of automatic short an-
swer grading. International journal of artificial in-
telligence in education, 25:60–117.
Changzhi Cai. 2019.
Automatic essay scoring with
recurrent neural network.
In Proceedings of

--- Page 7 ---

the 3rd International Conference on High Perfor-
mance Compilation, Computing and Communica-
tions, pages 1–7.
Li-Hsin Chang and Filip Ginter. 2024. Automatic short
answer grading for finnish with chatgpt.
In Pro-
ceedings of the AAAI Conference on Artificial Intel-
ligence, volume 38, pages 23173–23181.
Li-Hsin Chang, Jenna Kanerva, and Filip Ginter. 2022.
Towards automatic short answer assessment for
Finnish as a paraphrase retrieval task. In Proceed-
ings of the 17th Workshop on Innovative Use of NLP
for Building Educational Applications (BEA 2022),
pages 262–271, Seattle, Washington. Association
for Computational Linguistics.
Zhiyun Chen and Yuxin Zhou. 2019. Research on au-
tomatic essay scoring of composition based on cnn
and or. In 2019 2nd International Conference on Ar-
tificial Intelligence and Big Data (ICAIBD), pages
13–18. IEEE.
Yucheng Chu, Hang Li, Kaiqi Yang, Harry Shomer,
Hui Liu, Yasemin Copur-Gencturk, and Jiliang
Tang. 2024.
A llm-powered automatic grading
framework with human-level guidelines optimiza-
tion. arXiv preprint arXiv:2410.02165.
Roberts Dar`gis, Ilze Auzin¸a, Inga Kaija, Krist¯ıne
Lev¯ane-Petrova, and Krist¯ıne Pokratniece. 2022.
Corpus based self-assessment platform for latvian
language learners. Baltic Journal of Modern Com-
puting.
Roberts Dar ‘gis, Ilze Auzin¸a, Inga Kaija, Krist¯ıne
Lev¯ane-Petrova, and Krist¯ıne Pokratniece. 2022.
LaVA – Latvian language learner corpus. In Pro-
ceedings of the Thirteenth Language Resources and
Evaluation Conference, pages 727–731, Marseille,
France. European Language Resources Association.
Roberts Dar ‘gis, Guntis B¯arzdin¸ˇs, Inguna Skadin¸a, and
Baiba Saulite. 2024. Evaluating open-source LLMs
in low-resource languages: Insights from Latvian
high school exams. In Proceedings of the 4th Inter-
national Conference on Natural Language Process-
ing for Digital Humanities, pages 289–293, Miami,
USA. Association for Computational Linguistics.
Arunima
Divya,
Vivek
Haridas,
and
Jayasree
Narayanan. 2023.
Automation of short answer
grading techniques: Comparative study using deep
learning techniques.
In 2023 Fifth International
Conference on Electrical, Computer and Com-
munication Technologies (ICECCT), pages 1–7.
IEEE.
Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey,
Abhishek Kadian, Ahmad Al-Dahle, Aiesha Let-
man, Akhil Mathur, Alan Schelten, Amy Yang,
Angela Fan, Anirudh Goyal, Anthony Hartshorn,
Aobo Yang, Archi Mitra, Archie Sravankumar,
Artem Korenev, Arthur Hinsvark, Arun Rao, As-
ton Zhang, Aurelien Rodriguez, Austen Gregerson,
Ava Spataru, Baptiste Roziere, Bethany Biron,
Binh Tang, Bobbie Chern, Charlotte Caucheteux,
Chaya Nayak, Chloe Bi, Chris Marra, Chris Mc-
Connell, Christian Keller, Christophe Touret, Chun-
yang Wu, Corinne Wong, Cristian Canton Fer-
rer, Cyrus Nikolaidis, Damien Allonsius, Daniel
Song, Danielle Pintz, Danny Livshits, David Es-
iobu, Dhruv Choudhary, Dhruv Mahajan, Diego
Garcia-Olano, Diego Perino, Dieuwke Hupkes,
Egor Lakomkin, Ehab AlBadawy, Elina Lobanova,
Emily Dinan, Eric Michael Smith, Filip Raden-
ovic, Frank Zhang, Gabriel Synnaeve, Gabrielle
Lee, Georgia Lewis Anderson, Graeme Nail, Gre-
goire Mialon, Guan Pang, Guillem Cucurell, Hai-
ley Nguyen, Hannah Korevaar, Hu Xu, Hugo
Touvron, Iliyan Zarov, Imanol Arrieta Ibarra, Is-
abel Kloumann, Ishan Misra, Ivan Evtimov, Jade
Copet, Jaewon Lee, Jan Geffert, Jana Vranes, Ja-
son Park, Jay Mahadeokar, Jeet Shah, Jelmer van der
Linde, Jennifer Billock, Jenny Hong, Jenya Lee,
Jeremy Fu, Jianfeng Chi, Jianyu Huang, Jiawen
Liu, Jie Wang, Jiecao Yu, Joanna Bitton, Joe
Spisak, Jongsoo Park, Joseph Rocca, Joshua John-
stun, Joshua Saxe, Junteng Jia, Kalyan Vasuden
Alwala, Kartikeya Upasani, Kate Plawiak, Ke Li,
Kenneth Heafield, Kevin Stone, Khalid El-Arini,
Krithika Iyer, Kshitiz Malik, Kuenley Chiu, Ku-
nal Bhalla, Lauren Rantala-Yeary, Laurens van der
Maaten, Lawrence Chen, Liang Tan, Liz Jenk-
ins, Louis Martin, Lovish Madaan, Lubo Malo,
Lukas Blecher, Lukas Landzaat, Luke de Oliveira,
Madeline Muzzi, Mahesh Pasupuleti, Mannat Singh,
Manohar Paluri, Marcin Kardas, Mathew Old-
ham, Mathieu Rita, Maya Pavlova, Melanie Kam-
badur, Mike Lewis, Min Si, Mitesh Kumar Singh,
Mona Hassan, Naman Goyal, Narjes Torabi, Niko-
lay Bashlykov, Nikolay Bogoychev, Niladri Chat-
terji, Olivier Duchenne, Onur C¸ elebi, Patrick Al-
rassy, Pengchuan Zhang, Pengwei Li, Petar Va-
sic, Peter Weng, Prajjwal Bhargava, Pratik Dubal,
Praveen Krishnan, Punit Singh Koura, Puxin Xu,
Qing He, Qingxiao Dong, Ragavan Srinivasan,
Raj Ganapathy, Ramon Calderer, Ricardo Silveira
Cabral, Robert Stojnic, Roberta Raileanu, Rohit
Girdhar, Rohit Patel, Romain Sauvestre, Ronnie
Polidoro, Roshan Sumbaly, Ross Taylor, Ruan
Silva, Rui Hou, Rui Wang, Saghar Hosseini, Sa-
hana Chennabasappa, Sanjay Singh, Sean Bell, Seo-
hyun Sonia Kim, Sergey Edunov, Shaoliang Nie,
Sharan Narang, Sharath Raparthy, Sheng Shen,
Shengye Wan, Shruti Bhosale, Shun Zhang, Simon
Vandenhende, Soumya Batra, Spencer Whitman,
Sten Sootla, Stephane Collot, Suchin Gururangan,
Sydney Borodinsky, Tamar Herman, Tara Fowler,
Tarek Sheasha, Thomas Georgiou, Thomas Scialom,
Tobias Speckbacher, Todor Mihaylov, Tong Xiao,
Ujjwal Karn, Vedanuj Goswami, Vibhor Gupta, Vig-
nesh Ramanathan, Viktor Kerkez, Vincent Gonguet,
Virginie Do, Vish Vogeti, Vladan Petrovic, Weiwei
Chu, Wenhan Xiong, Wenyin Fu, Whitney Meers,
Xavier Martinet, Xiaodong Wang, Xiaoqing Ellen
Tan, Xinfeng Xie, Xuchao Jia, Xuewei Wang,
Yaelle Goldschlag, Yashesh Gaur, Yasmine Babaei,

--- Page 8 ---

Yi Wen, Yiwen Song, Yuchen Zhang, Yue Li, Yun-
ing Mao, Zacharie Delpierre Coudert, Zheng Yan,
Zhengxing Chen, Zoe Papakipos, Aaditya Singh,
Aaron Grattafiori, Abha Jain, Adam Kelsey, Adam
Shajnfeld, Adithya Gangidi, Adolfo Victoria, Ahuva
Goldstand, Ajay Menon, Ajay Sharma, Alex Boe-
senberg, Alex Vaughan, Alexei Baevski, Allie Fein-
stein, Amanda Kallet, Amit Sangani, Anam Yunus,
Andrei Lupu, Andres Alvarado, Andrew Caples,
Andrew Gu, Andrew Ho, Andrew Poulton, Andrew
Ryan, Ankit Ramchandani, Annie Franco, Apara-
jita Saraf, Arkabandhu Chowdhury, Ashley Gabriel,
Ashwin Bharambe, Assaf Eisenman, Azadeh Yaz-
dan, Beau James, Ben Maurer, Benjamin Leonhardi,
Bernie Huang, Beth Loyd, Beto De Paola, Bhar-
gavi Paranjape, Bing Liu, Bo Wu, Boyu Ni, Braden
Hancock, Bram Wasti, Brandon Spence, Brani Sto-
jkovic, Brian Gamido, Britt Montalvo, Carl Parker,
Carly Burton, Catalina Mejia, Changhan Wang,
Changkyu Kim, Chao Zhou, Chester Hu, Ching-
Hsiang Chu, Chris Cai, Chris Tindal, Christoph
Feichtenhofer, Damon Civin, Dana Beaty, Daniel
Kreymer, Daniel Li, Danny Wyatt, David Adkins,
David Xu, Davide Testuggine, Delia David, Devi
Parikh, Diana Liskovich, Didem Foss, Dingkang
Wang, Duc Le, Dustin Holland, Edward Dowling,
Eissa Jamil, Elaine Montgomery, Eleonora Presani,
Emily Hahn, Emily Wood, Erik Brinkman, Este-
ban Arcaute, Evan Dunbar, Evan Smothers, Fei Sun,
Felix Kreuk, Feng Tian, Firat Ozgenel, Francesco
Caggioni, Francisco Guzm´an, Frank Kanayet, Frank
Seide, Gabriela Medina Florez, Gabriella Schwarz,
Gada Badeer, Georgia Swee, Gil Halpern, Govind
Thattai, Grant Herman, Grigory Sizov, Guangyi,
Zhang, Guna Lakshminarayanan, Hamid Shojanaz-
eri, Han Zou, Hannah Wang, Hanwen Zha, Haroun
Habeeb, Harrison Rudolph, Helen Suk, Henry As-
pegren, Hunter Goldman, Ibrahim Damlaj, Igor
Molybog, Igor Tufanov, Irina-Elena Veliche, Itai
Gat, Jake Weissman, James Geboski, James Kohli,
Japhet Asher, Jean-Baptiste Gaya, Jeff Marcus, Jeff
Tang, Jennifer Chan, Jenny Zhen, Jeremy Reizen-
stein, Jeremy Teboul, Jessica Zhong, Jian Jin, Jingyi
Yang, Joe Cummings, Jon Carvill, Jon Shepard,
Jonathan McPhie, Jonathan Torres, Josh Ginsburg,
Junjie Wang, Kai Wu, Kam Hou U, Karan Sax-
ena, Karthik Prasad, Kartikay Khandelwal, Katay-
oun Zand, Kathy Matosich, Kaushik Veeraragha-
van, Kelly Michelena, Keqian Li, Kun Huang, Kunal
Chawla, Kushal Lakhotia, Kyle Huang, Lailin Chen,
Lakshya Garg, Lavender A, Leandro Silva, Lee
Bell, Lei Zhang, Liangpeng Guo, Licheng Yu, Liron
Moshkovich,
Luca Wehrstedt,
Madian Khabsa,
Manav Avalani, Manish Bhatt, Maria Tsimpoukelli,
Martynas Mankus, Matan Hasson, Matthew Lennie,
Matthias Reso, Maxim Groshev, Maxim Naumov,
Maya Lathi, Meghan Keneally, Michael L. Seltzer,
Michal Valko, Michelle Restrepo, Mihir Patel,
Mik Vyatskov, Mikayel Samvelyan, Mike Clark,
Mike Macey, Mike Wang, Miquel Jubert Her-
moso, Mo Metanat, Mohammad Rastegari, Mun-
ish Bansal, Nandhini Santhanam, Natascha Parks,
Natasha White, Navyata Bawa, Nayan Singhal, Nick
Egebo, Nicolas Usunier, Nikolay Pavlovich Laptev,
Ning Dong, Ning Zhang, Norman Cheng, Oleg
Chernoguz, Olivia Hart, Omkar Salpekar, Ozlem
Kalinli, Parkin Kent, Parth Parekh, Paul Saab, Pavan
Balaji, Pedro Rittner, Philip Bontrager, Pierre Roux,
Piotr Dollar, Polina Zvyagina, Prashant Ratanchan-
dani, Pritish Yuvraj, Qian Liang, Rachad Alao,
Rachel Rodriguez, Rafi Ayub, Raghotham Murthy,
Raghu Nayani, Rahul Mitra, Raymond Li, Re-
bekkah Hogan, Robin Battey, Rocky Wang, Rohan
Maheswari, Russ Howes, Ruty Rinott, Sai Jayesh
Bondu, Samyak Datta, Sara Chugh, Sara Hunt, Sar-
gun Dhillon, Sasha Sidorov, Satadru Pan, Saurabh
Verma, Seiji Yamamoto, Sharadh Ramaswamy,
Shaun Lindsay, Shaun Lindsay, Sheng Feng, Sheng-
hao Lin, Shengxin Cindy Zha, Shiva Shankar,
Shuqiang Zhang, Shuqiang Zhang, Sinong Wang,
Sneha Agarwal, Soji Sajuyigbe, Soumith Chin-
tala, Stephanie Max, Stephen Chen, Steve Kehoe,
Steve Satterfield, Sudarshan Govindaprasad, Sumit
Gupta, Sungmin Cho, Sunny Virk, Suraj Subra-
manian, Sy Choudhury, Sydney Goldman, Tal Re-
mez, Tamar Glaser, Tamara Best, Thilo Kohler,
Thomas Robinson, Tianhe Li, Tianjun Zhang, Tim
Matthews, Timothy Chou, Tzook Shaked, Varun
Vontimitta, Victoria Ajayi, Victoria Montanez, Vijai
Mohan, Vinay Satish Kumar, Vishal Mangla, V´ıtor
Albiero, Vlad Ionescu, Vlad Poenaru, Vlad Tiberiu
Mihailescu, Vladimir Ivanov, Wei Li, Wenchen
Wang, Wenwen Jiang, Wes Bouaziz, Will Con-
stable, Xiaocheng Tang, Xiaofang Wang, Xiaojian
Wu, Xiaolan Wang, Xide Xia, Xilun Wu, Xinbo
Gao, Yanjun Chen, Ye Hu, Ye Jia, Ye Qi, Yenda
Li, Yilin Zhang, Ying Zhang, Yossi Adi, Youngjin
Nam, Yu, Wang, Yuchen Hao, Yundi Qian, Yuzi He,
Zach Rait, Zachary DeVito, Zef Rosnbrick, Zhaoduo
Wen, Zhenyu Yang, and Zhiwei Zhao. 2024. The
llama 3 herd of models.
Christian Gr´evisse. 2024. Llm-based automatic short
answer grading in undergraduate medical education.
BMC Medical Education, 24(1):1060.
Veronika Hackl, Alexandra Elena M¨uller, Michael
Granitzer, and Maximilian Sailer. 2023. Is gpt-4 a
reliable rater? evaluating consistency in gpt-4’s text
ratings. In Frontiers in Education, volume 8, page
1272229. Frontiers Media SA.
Rositsa V Ivanova and Siegfried Handschuh. 2024.
Evaluating llms’ performance at automatic short-
answer grading.
Albert Q. Jiang, Alexandre Sablayrolles, Arthur Men-
sch, Chris Bamford, Devendra Singh Chaplot, Diego
de las Casas, Florian Bressand, Gianna Lengyel,
Guillaume Lample, Lucile Saulnier, L´elio Re-
nard Lavaud, Marie-Anne Lachaux, Pierre Stock,
Teven Le Scao, Thibaut Lavril, Thomas Wang, Tim-
oth´ee Lacroix, and William El Sayed. 2023. Mistral
7b.
Artur Kiulian, Anton Polishko, Mykola Khandoga,
Oryna Chubych, Jack Connor, Raghav Ravishankar,
and Adarsh Shirawalmath. 2024.
From bytes to

--- Page 9 ---

borsch:
Fine-tuning gemma and mistral for the
ukrainian language representation.
arXiv preprint
arXiv:2404.09138.
Pernille Andresen Klevstuen. 2022. Assisting efficient
and fair grading with information retrieval and text
mining techniques. Master’s thesis, NTNU.
R Krithika and Jayasree Narayanan. 2015. Learning
to grade short answers using machine learning tech-
niques. In Proceedings of the Third International
Symposium on Women in Computing and Informat-
ics, pages 262–271.
VD Lai, NT Ngo, APB Veyseh, H Man, F Dernoncourt,
T Bui, and TH Nguyen. 2023. Chatgpt beyond en-
glish: Towards a comprehensive evaluation of large
language models in multilingual learning. arxiv.
Krist¯ıne Lev¯ane-Petrova, Roberts Dar ‘gis, Krist¯ıne
Pokratniece, and Viesturs J¯ulijs Lasmanis. 2023.
Balanced corpus of modern latvian (LVK2022).
CLARIN-LV digital library at IMCS, University of
Latvia.
Pedro Henrique Martins, Patrick Fernandes, Jo˜ao
Alves, Nuno M. Guerreiro, Ricardo Rei, Duarte M.
Alves, Jos´e Pombal, Amin Farajian, Manuel Faysse,
Mateusz Klimaszewski, Pierre Colombo, Barry
Haddow, Jos´e G. C. de Souza, Alexandra Birch, and
Andr´e F. T. Martins. 2024. Eurollm: Multilingual
language models for europe.
Tim Metzler, Paul G. Pl¨oger, and J¨orn Hees. 2024.
Computer-assisted short answer grading using large
language models and rubrics.
In INFORMATIK
2024, pages 1383–1393. Gesellschaft f¨ur Informatik
e.V., Bonn.
Atsushi Mizumoto and Masaki Eguchi. 2023. Explor-
ing the potential of using an ai language model for
automated essay scoring. Research Methods in Ap-
plied Linguistics, 2(2):100050.
Lekshmi R Pillai, G Veena, and Deepa Gupta. 2018.
A combined approach using semantic role labelling
and word sense disambiguation for question genera-
tion and answer extraction. In 2018 Second Interna-
tional Conference on Advances in Electronics, Com-
puters and Communications (ICAECC), pages 1–6.
IEEE.
Johannes Schneider, Bernd Schenk, and Christina
Niklaus. 2023.
Towards llm-based autograd-
ing for short textual answers.
arXiv preprint
arXiv:2309.11508.
V Sreevidhya and Jayasree Narayanan. 2021. Short de-
scriptive answer evaluation using word-embedding
techniques. In 2021 12th international conference
on computing communication and networking tech-
nologies (ICCCNT), pages 1–4. IEEE.
Pavel Stefanoviˇc, Birut˙e Pliuskuvien˙e, Urt˙e Radvilait˙e,
and Simona Ramanauskait˙e. 2024. Machine learn-
ing model for chatgpt usage detection in students’
answers to open-ended questions: Case of lithuanian
language. Education and Information Technologies,
pages 1–23.
Chul Sung,
Tejas Dhamecha,
Swarnadeep Saha,
Tengfei Ma, Vinay Reddy, and Rishi Arora. 2019.
Pre-training bert on domain resources for short an-
swer grading. In Proceedings of the 2019 Confer-
ence on Empirical Methods in Natural Language
Processing and the 9th International Joint Confer-
ence on Natural Language Processing (EMNLP-
IJCNLP), pages 6071–6075.
Gemini Team, Petko Georgiev, Ving Ian Lei, Ryan
Burnell, Libin Bai, Anmol Gulati, Garrett Tanzer,
Damien
Vincent,
Zhufeng
Pan,
Shibo
Wang,
Soroosh Mariooryad, Yifan Ding, Xinyang Geng,
Fred Alcober, Roy Frostig, Mark Omernick, Lexi
Walker, Cosmin Paduraru, Christina Sorokin, An-
drea Tacchetti, Colin Gaffney, Samira Daruki, Ol-
can Sercinoglu, Zach Gleicher, Juliette Love, Paul
Voigtlaender, Rohan Jain, Gabriela Surita, Kareem
Mohamed, Rory Blevins, Junwhan Ahn, Tao Zhu,
Kornraphop Kawintiranon, Orhan Firat, Yiming Gu,
Yujing Zhang, Matthew Rahtz, Manaal Faruqui, Na-
talie Clay, Justin Gilmer, JD Co-Reyes, Ivo Penchev,
Rui Zhu, Nobuyuki Morioka, Kevin Hui, Kr-
ishna Haridasan, Victor Campos, Mahdis Mahdieh,
Mandy Guo, Samer Hassan, Kevin Kilgour, Arpi
Vezer, Heng-Tze Cheng, Raoul de Liedekerke, Sid-
dharth Goyal, Paul Barham, DJ Strouse, Seb Noury,
Jonas Adler, Mukund Sundararajan, Sharad Vikram,
Dmitry Lepikhin, Michela Paganini, Xavier Gar-
cia, Fan Yang, Dasha Valter, Maja Trebacz, Ki-
ran Vodrahalli, Chulayuth Asawaroengchai, Roman
Ring, Norbert Kalb, Livio Baldini Soares, Sid-
dhartha Brahma, David Steiner, Tianhe Yu, Fabian
Mentzer, Antoine He, Lucas Gonzalez, Bibo Xu,
Raphael Lopez Kaufman, Laurent El Shafey, Jun-
hyuk Oh, Tom Hennigan, George van den Driess-
che, Seth Odoom, Mario Lucic, Becca Roelofs, Sid
Lall, Amit Marathe, Betty Chan, Santiago Ontanon,
Luheng He, Denis Teplyashin, Jonathan Lai, Phil
Crone, Bogdan Damoc, Lewis Ho, Sebastian Riedel,
Karel Lenc, Chih-Kuan Yeh, Aakanksha Chowd-
hery, Yang Xu, Mehran Kazemi, Ehsan Amid,
Anastasia Petrushkina, Kevin Swersky, Ali Kho-
daei, Gowoon Chen, Chris Larkin, Mario Pinto,
Geng Yan, Adria Puigdomenech Badia, Piyush
Patil, Steven Hansen, Dave Orr, Sebastien M. R.
Arnold, Jordan Grimstad, Andrew Dai, Sholto Dou-
glas, Rishika Sinha, Vikas Yadav, Xi Chen, Elena
Gribovskaya, Jacob Austin, Jeffrey Zhao, Kaushal
Patel, Paul Komarek, Sophia Austin, Sebastian
Borgeaud, Linda Friso, Abhimanyu Goyal, Ben
Caine, Kris Cao, Da-Woon Chung, Matthew Lamm,
Gabe Barth-Maron, Thais Kagohara, Kate Ol-
szewska, Mia Chen, Kaushik Shivakumar, Rishabh
Agarwal, Harshal Godhia, Ravi Rajwar, Javier
Snaider, Xerxes Dotiwalla, Yuan Liu, Aditya Barua,
Victor Ungureanu, Yuan Zhang, Bat-Orgil Bat-
saikhan, Mateo Wirth, James Qin, Ivo Danihelka,
Tulsee Doshi, Martin Chadwick, Jilin Chen, Sanil
Jain, Quoc Le, Arjun Kar, Madhu Gurumurthy,

--- Page 10 ---

Cheng Li, Ruoxin Sang, Fangyu Liu, Lampros Lam-
prou, Rich Munoz, Nathan Lintz, Harsh Mehta,
Heidi Howard, Malcolm Reynolds, Lora Aroyo,
Quan Wang, Lorenzo Blanco, Albin Cassirer, Jor-
dan Griffith, Dipanjan Das, Stephan Lee, Jakub Syg-
nowski, Zach Fisher, James Besley, Richard Pow-
ell, Zafarali Ahmed, Dominik Paulus, David Re-
itter, Zalan Borsos, Rishabh Joshi, Aedan Pope,
Steven Hand, Vittorio Selo, Vihan Jain, Nikhil Sethi,
Megha Goel, Takaki Makino, Rhys May, Zhen
Yang, Johan Schalkwyk, Christina Butterfield, Anja
Hauth, Alex Goldin, Will Hawkins, Evan Senter,
Sergey Brin, Oliver Woodman, Marvin Ritter, Eric
Noland, Minh Giang, Vijay Bolina, Lisa Lee, Tim
Blyth, Ian Mackinnon, Machel Reid, Obaid Sar-
vana, David Silver, Alexander Chen, Lily Wang,
Loren Maggiore, Oscar Chang, Nithya Attaluri, Gre-
gory Thornton, Chung-Cheng Chiu, Oskar Bunyan,
Nir Levine, Timothy Chung, Evgenii Eltyshev, Xi-
ance Si, Timothy Lillicrap, Demetra Brady, Vaib-
hav Aggarwal, Boxi Wu, Yuanzhong Xu, Ross McIl-
roy, Kartikeya Badola, Paramjit Sandhu, Erica Mor-
eira, Wojciech Stokowiec, Ross Hemsley, Dong Li,
Alex Tudor, Pranav Shyam, Elahe Rahimtoroghi,
Salem Haykal, Pablo Sprechmann, Xiang Zhou, Di-
ana Mincu, Yujia Li, Ravi Addanki, Kalpesh Kr-
ishna, Xiao Wu, Alexandre Frechette, Matan Eyal,
Allan Dafoe, Dave Lacey, Jay Whang, Thi Avra-
hami, Ye Zhang, Emanuel Taropa, Hanzhao Lin,
Daniel Toyama, Eliza Rutherford, Motoki Sano,
HyunJeong Choe, Alex Tomala, Chalence Safranek-
Shrader, Nora Kassner, Mantas Pajarskas, Matt
Harvey, Sean Sechrist, Meire Fortunato, Christina
Lyu, Gamaleldin Elsayed, Chenkai Kuang, James
Lottes, Eric Chu, Chao Jia, Chih-Wei Chen, Pe-
ter Humphreys, Kate Baumli, Connie Tao, Rajku-
mar Samuel, Cicero Nogueira dos Santos, Anders
Andreassen, Nemanja Raki´cevi´c, Dominik Grewe,
Aviral Kumar, Stephanie Winkler, Jonathan Caton,
Andrew Brock, Sid Dalmia, Hannah Sheahan, Iain
Barr, Yingjie Miao, Paul Natsev, Jacob Devlin,
Feryal Behbahani, Flavien Prost, Yanhua Sun, Ar-
tiom Myaskovsky, Thanumalayan Sankaranarayana
Pillai, Dan Hurt, Angeliki Lazaridou, Xi Xiong,
Ce Zheng, Fabio Pardo, Xiaowei Li, Dan Hor-
gan, Joe Stanton, Moran Ambar, Fei Xia, Ale-
jandro Lince, Mingqiu Wang, Basil Mustafa, Al-
bert Webson, Hyo Lee, Rohan Anil, Martin Wicke,
Timothy Dozat, Abhishek Sinha, Enrique Piqueras,
Elahe Dabir, Shyam Upadhyay, Anudhyan Bo-
ral, Lisa Anne Hendricks, Corey Fry, Josip Djo-
longa, Yi Su, Jake Walker, Jane Labanowski, Ronny
Huang, Vedant Misra, Jeremy Chen, RJ Skerry-
Ryan, Avi Singh, Shruti Rijhwani, Dian Yu, Alex
Castro-Ros, Beer Changpinyo, Romina Datta, Sumit
Bagri, Arnar Mar Hrafnkelsson, Marcello Maggioni,
Daniel Zheng, Yury Sulsky, Shaobo Hou, Tom Le
Paine, Antoine Yang, Jason Riesa, Dominika Ro-
gozinska, Dror Marcus, Dalia El Badawy, Qiao
Zhang, Luyu Wang, Helen Miller, Jeremy Greer,
Lars Lowe Sjos, Azade Nova, Heiga Zen, Rahma
Chaabouni, Mihaela Rosca, Jiepu Jiang, Charlie
Chen, Ruibo Liu, Tara Sainath, Maxim Krikun, Alex
Polozov, Jean-Baptiste Lespiau, Josh Newlan, Zeyn-
cep Cankara, Soo Kwak, Yunhan Xu, Phil Chen,
Andy Coenen, Clemens Meyer, Katerina Tsihlas,
Ada Ma, Juraj Gottweis, Jinwei Xing, Chenjie
Gu, Jin Miao, Christian Frank, Zeynep Cankara,
Sanjay Ganapathy, Ishita Dasgupta, Steph Hughes-
Fitt, Heng Chen, David Reid, Keran Rong, Hong-
min Fan, Joost van Amersfoort, Vincent Zhuang,
Aaron Cohen, Shixiang Shane Gu, Anhad Mo-
hananey, Anastasija Ilic, Taylor Tobin, John Wi-
eting, Anna Bortsova, Phoebe Thacker, Emma
Wang, Emily Caveness, Justin Chiu, Eren Sezener,
Alex Kaskasoli, Steven Baker, Katie Millican, Mo-
hamed Elhawaty, Kostas Aisopos, Carl Lebsack,
Nathan Byrd, Hanjun Dai, Wenhao Jia, Matthew Wi-
ethoff, Elnaz Davoodi, Albert Weston, Lakshman
Yagati, Arun Ahuja, Isabel Gao, Golan Pundak, Su-
san Zhang, Michael Azzam, Khe Chai Sim, Sergi
Caelles, James Keeling, Abhanshu Sharma, Andy
Swing, YaGuang Li, Chenxi Liu, Carrie Grimes
Bostock, Yamini Bansal, Zachary Nado, Ankesh
Anand, Josh Lipschultz, Abhijit Karmarkar, Lev
Proleev, Abe Ittycheriah, Soheil Hassas Yeganeh,
George Polovets, Aleksandra Faust, Jiao Sun, Al-
ban Rrustemi, Pen Li, Rakesh Shivanna, Jeremiah
Liu, Chris Welty, Federico Lebron, Anirudh Bad-
depudi, Sebastian Krause, Emilio Parisotto, Radu
Soricut, Zheng Xu, Dawn Bloxwich, Melvin John-
son, Behnam Neyshabur, Justin Mao-Jones, Ren-
shen Wang, Vinay Ramasesh, Zaheer Abbas, Arthur
Guez, Constant Segal, Duc Dung Nguyen, James
Svensson, Le Hou, Sarah York, Kieran Milan, So-
phie Bridgers, Wiktor Gworek, Marco Tagliasac-
chi, James Lee-Thorp, Michael Chang, Alexey
Guseynov, Ale Jakse Hartman, Michael Kwong,
Ruizhe Zhao, Sheleem Kashem, Elizabeth Cole,
Antoine Miech, Richard Tanburn, Mary Phuong,
Filip Pavetic, Sebastien Cevey, Ramona Comanescu,
Richard Ives, Sherry Yang, Cosmo Du, Bo Li,
Zizhao Zhang, Mariko Iinuma, Clara Huiyi Hu, Au-
rko Roy, Shaan Bijwadia, Zhenkai Zhu, Danilo Mar-
tins, Rachel Saputro, Anita Gergely, Steven Zheng,
Dawei Jia, Ioannis Antonoglou, Adam Sadovsky,
Shane Gu, Yingying Bi, Alek Andreev, Sina Saman-
gooei, Mina Khan, Tomas Kocisky, Angelos Filos,
Chintu Kumar, Colton Bishop, Adams Yu, Sarah
Hodkinson, Sid Mittal, Premal Shah, Alexandre
Moufarek, Yong Cheng, Adam Bloniarz, Jaehoon
Lee, Pedram Pejman, Paul Michel, Stephen Spencer,
Vladimir Feinberg, Xuehan Xiong, Nikolay Savi-
nov,
Charlotte Smith,
Siamak Shakeri,
Dustin
Tran, Mary Chesus, Bernd Bohnet, George Tucker,
Tamara von Glehn, Carrie Muir, Yiran Mao, Hideto
Kazawa, Ambrose Slone, Kedar Soparkar, Disha
Shrivastava, James Cobon-Kerr, Michael Sharman,
Jay Pavagadhi, Carlos Araya, Karolis Misiunas,
Nimesh Ghelani, Michael Laskin, David Barker, Qi-
ujia Li, Anton Briukhov, Neil Houlsby, Mia Glaese,
Balaji Lakshminarayanan, Nathan Schucher, Yun-
hao Tang, Eli Collins, Hyeontaek Lim, Fangxiaoyu
Feng, Adria Recasens, Guangda Lai, Alberto Magni,
Nicola De Cao, Aditya Siddhant, Zoe Ashwood,
Jordi Orbay, Mostafa Dehghani, Jenny Brennan,

--- Page 11 ---

Yifan He, Kelvin Xu, Yang Gao, Carl Saroufim,
James Molloy, Xinyi Wu, Seb Arnold, Solomon
Chang, Julian Schrittwieser, Elena Buchatskaya,
Soroush Radpour, Martin Polacek, Skye Giordano,
Ankur Bapna, Simon Tokumine, Vincent Hellen-
doorn, Thibault Sottiaux, Sarah Cogan, Aliaksei
Severyn, Mohammad Saleh, Shantanu Thakoor,
Laurent Shefey, Siyuan Qiao, Meenu Gaba, Shuo
yiin Chang, Craig Swanson, Biao Zhang, Ben-
jamin Lee, Paul Kishan Rubenstein, Gan Song, Tom
Kwiatkowski, Anna Koop, Ajay Kannan, David
Kao, Parker Schuh, Axel Stjerngren, Golnaz Ghiasi,
Gena Gibson, Luke Vilnis, Ye Yuan, Felipe Tiengo
Ferreira, Aishwarya Kamath, Ted Klimenko, Ken
Franko, Kefan Xiao, Indro Bhattacharya, Miteyan
Patel, Rui Wang, Alex Morris, Robin Strudel, Vivek
Sharma, Peter Choy, Sayed Hadi Hashemi, Jes-
sica Landon, Mara Finkelstein, Priya Jhakra, Justin
Frye, Megan Barnes, Matthew Mauger, Dennis
Daun, Khuslen Baatarsukh, Matthew Tung, Wael
Farhan, Henryk Michalewski, Fabio Viola, Felix
de Chaumont Quitry, Charline Le Lan, Tom Hud-
son, Qingze Wang, Felix Fischer, Ivy Zheng, Elspeth
White, Anca Dragan, Jean baptiste Alayrac, Eric Ni,
Alexander Pritzel, Adam Iwanicki, Michael Isard,
Anna Bulanova, Lukas Zilka, Ethan Dyer, Devendra
Sachan, Srivatsan Srinivasan, Hannah Muckenhirn,
Honglong Cai, Amol Mandhane, Mukarram Tariq,
Jack W. Rae, Gary Wang, Kareem Ayoub, Nicholas
FitzGerald, Yao Zhao, Woohyun Han, Chris Al-
berti, Dan Garrette, Kashyap Krishnakumar, Mai
Gimenez, Anselm Levskaya, Daniel Sohn, Josip
Matak, Inaki Iturrate, Michael B. Chang, Jackie
Xiang, Yuan Cao, Nishant Ranka, Geoff Brown,
Adrian Hutter, Vahab Mirrokni, Nanxin Chen,
Kaisheng Yao, Zoltan Egyed, Francois Galilee,
Tyler Liechty, Praveen Kallakuri, Evan Palmer, San-
jay Ghemawat, Jasmine Liu, David Tao, Chloe
Thornton, Tim Green, Mimi Jasarevic, Sharon Lin,
Victor Cotruta, Yi-Xuan Tan, Noah Fiedel, Hongkun
Yu, Ed Chi, Alexander Neitz, Jens Heitkaemper,
Anu Sinha, Denny Zhou, Yi Sun, Charbel Kaed,
Brice Hulse, Swaroop Mishra, Maria Georgaki,
Sneha Kudugunta, Clement Farabet, Izhak Shafran,
Daniel Vlasic, Anton Tsitsulin, Rajagopal Anan-
thanarayanan, Alen Carin, Guolong Su, Pei Sun,
Shashank V, Gabriel Carvajal, Josef Broder, Iu-
lia Comsa, Alena Repina, William Wong, War-
ren Weilun Chen, Peter Hawkins, Egor Filonov,
Lucia Loher, Christoph Hirnschall, Weiyi Wang,
Jingchen Ye, Andrea Burns, Hardie Cate, Di-
ana Gage Wright, Federico Piccinini, Lei Zhang,
Chu-Cheng Lin, Ionel Gog, Yana Kulizhskaya, Ash-
win Sreevatsa, Shuang Song, Luis C. Cobo, Anand
Iyer, Chetan Tekur, Guillermo Garrido, Zhuyun
Xiao, Rupert Kemp, Huaixiu Steven Zheng, Hui
Li, Ananth Agarwal, Christel Ngani, Kati Gosh-
vadi, Rebeca Santamaria-Fernandez, Wojciech Fica,
Xinyun Chen, Chris Gorgolewski, Sean Sun, Roopal
Garg, Xinyu Ye, S. M. Ali Eslami, Nan Hua,
Jon Simon, Pratik Joshi, Yelin Kim, Ian Ten-
ney, Sahitya Potluri, Lam Nguyen Thiet, Quan
Yuan, Florian Luisier, Alexandra Chronopoulou,
Salvatore Scellato, Praveen Srinivasan, Minmin
Chen, Vinod Koverkathu, Valentin Dalibard, Yam-
ing Xu, Brennan Saeta, Keith Anderson, Thibault
Sellam, Nick Fernando, Fantine Huot, Junehyuk
Jung, Mani Varadarajan, Michael Quinn, Amit
Raul, Maigo Le, Ruslan Habalov, Jon Clark, Ko-
mal Jalan, Kalesha Bullard, Achintya Singhal,
Thang Luong, Boyu Wang, Sujeevan Rajayogam,
Julian Eisenschlos, Johnson Jia, Daniel Finchel-
stein, Alex Yakubovich, Daniel Balle, Michael Fink,
Sameer Agarwal, Jing Li, Dj Dvijotham, Shalini
Pal, Kai Kang, Jaclyn Konzelmann, Jennifer Beat-
tie, Olivier Dousse, Diane Wu, Remi Crocker, Chen
Elkind, Siddhartha Reddy Jonnalagadda, Jong Lee,
Dan Holtmann-Rice, Krystal Kallarackal, Rosanne
Liu, Denis Vnukov, Neera Vats, Luca Invernizzi,
Mohsen Jafari, Huanjie Zhou, Lilly Taylor, Jen-
nifer Prendki, Marcus Wu, Tom Eccles, Tianqi Liu,
Kavya Kopparapu, Francoise Beaufays, Christof
Angermueller, Andreea Marzoca, Shourya Sarcar,
Hilal Dib, Jeff Stanway, Frank Perbet, Nejc Trdin,
Rachel Sterneck, Andrey Khorlin, Dinghua Li, Xi-
hui Wu, Sonam Goenka, David Madras, Sasha
Goldshtein, Willi Gierke, Tong Zhou, Yaxin Liu,
Yannie Liang, Anais White, Yunjie Li, Shreya
Singh, Sanaz Bahargam, Mark Epstein, Sujoy Basu,
Li Lao, Adnan Ozturel, Carl Crous, Alex Zhai,
Han Lu, Zora Tung, Neeraj Gaur, Alanna Wal-
ton, Lucas Dixon, Ming Zhang, Amir Glober-
son, Grant Uy, Andrew Bolt, Olivia Wiles, Mi-
lad Nasr, Ilia Shumailov, Marco Selvi, Francesco
Piccinno, Ricardo Aguilar, Sara McCarthy, Misha
Khalman, Mrinal Shukla, Vlado Galic, John Car-
penter, Kevin Villela, Haibin Zhang, Harry Richard-
son, James Martens, Matko Bosnjak, Shreyas Ram-
mohan Belle, Jeff Seibert, Mahmoud Alnahlawi,
Brian McWilliams, Sankalp Singh, Annie Louis,
Wen Ding, Dan Popovici, Lenin Simicich, Laura
Knight, Pulkit Mehta, Nishesh Gupta, Chongyang
Shi, Saaber Fatehi, Jovana Mitrovic, Alex Grills,
Joseph Pagadora, Dessie Petrova, Danielle Eisen-
bud, Zhishuai Zhang, Damion Yates, Bhavishya
Mittal, Nilesh Tripuraneni, Yannis Assael, Thomas
Brovelli, Prateek Jain, Mihajlo Velimirovic, Canfer
Akbulut, Jiaqi Mu, Wolfgang Macherey, Ravin Ku-
mar, Jun Xu, Haroon Qureshi, Gheorghe Comanici,
Jeremy Wiesner, Zhitao Gong, Anton Ruddock,
Matthias Bauer, Nick Felt, Anirudh GP, Anurag
Arnab, Dustin Zelle, Jonas Rothfuss, Bill Rosgen,
Ashish Shenoy, Bryan Seybold, Xinjian Li, Jayaram
Mudigonda, Goker Erdogan, Jiawei Xia, Jiri Simsa,
Andrea Michi, Yi Yao, Christopher Yew, Steven
Kan, Isaac Caswell, Carey Radebaugh, Andre Elis-
seeff, Pedro Valenzuela, Kay McKinney, Kim Pa-
terson, Albert Cui, Eri Latorre-Chimoto, Solomon
Kim, William Zeng, Ken Durden, Priya Ponnapalli,
Tiberiu Sosea, Christopher A. Choquette-Choo,
James Manyika, Brona Robenek, Harsha Vashisht,
Sebastien Pereira, Hoi Lam, Marko Velic, Denese
Owusu-Afriyie, Katherine Lee, Tolga Bolukbasi,
Alicia Parrish, Shawn Lu, Jane Park, Balaji Venka-
traman, Alice Talbert, Lambert Rosique, Yuchung
Cheng, Andrei Sozanschi, Adam Paszke, Praveen

--- Page 12 ---

Kumar, Jessica Austin, Lu Li, Khalid Salama,
Wooyeol Kim, Nandita Dukkipati, Anthony Barysh-
nikov, Christos Kaplanis, XiangHai Sheng, Yuri
Chervonyi, Caglar Unlu, Diego de Las Casas, Harry
Askham, Kathryn Tunyasuvunakool, Felix Gimeno,
Siim Poder, Chester Kwak, Matt Miecnikowski, Va-
hab Mirrokni, Alek Dimitriev, Aaron Parisi, Dangyi
Liu, Tomy Tsai, Toby Shevlane, Christina Kouridi,
Drew Garmon, Adrian Goedeckemeyer, Adam R.
Brown, Anitha Vijayakumar, Ali Elqursh, Sadegh
Jazayeri, Jin Huang, Sara Mc Carthy, Jay Hoover,
Lucy Kim, Sandeep Kumar, Wei Chen, Courtney
Biles, Garrett Bingham, Evan Rosen, Lisa Wang,
Qijun Tan, David Engel, Francesco Pongetti, Dario
de Cesare, Dongseong Hwang, Lily Yu, Jennifer
Pullman, Srini Narayanan, Kyle Levin, Siddharth
Gopal, Megan Li, Asaf Aharoni, Trieu Trinh, Jes-
sica Lo, Norman Casagrande, Roopali Vij, Loic
Matthey, Bramandia Ramadhana, Austin Matthews,
CJ Carey, Matthew Johnson, Kremena Goranova,
Rohin Shah, Shereen Ashraf, Kingshuk Dasgupta,
Rasmus Larsen, Yicheng Wang, Manish Reddy
Vuyyuru, Chong Jiang, Joana Ijazi, Kazuki Os-
awa, Celine Smith, Ramya Sree Boppana, Taylan
Bilal, Yuma Koizumi, Ying Xu, Yasemin Altun,
Nir Shabat, Ben Bariach, Alex Korchemniy, Kiam
Choo, Olaf Ronneberger, Chimezie Iwuanyanwu,
Shubin Zhao, David Soergel, Cho-Jui Hsieh, Irene
Cai, Shariq Iqbal, Martin Sundermeyer, Zhe Chen,
Elie Bursztein, Chaitanya Malaviya, Fadi Biadsy,
Prakash Shroff, Inderjit Dhillon, Tejasi Latkar,
Chris Dyer, Hannah Forbes, Massimo Nicosia, Vi-
taly Nikolaev, Somer Greene, Marin Georgiev, Pi-
dong Wang, Nina Martin, Hanie Sedghi, John
Zhang, Praseem Banzal, Doug Fritz, Vikram Rao,
Xuezhi Wang, Jiageng Zhang, Viorica Patraucean,
Dayou Du, Igor Mordatch, Ivan Jurin, Lewis Liu,
Ayush Dubey, Abhi Mohan, Janek Nowakowski,
Vlad-Doru Ion, Nan Wei, Reiko Tojo, Maria Abi
Raad, Drew A. Hudson, Vaishakh Keshava, Shub-
ham Agrawal, Kevin Ramirez, Zhichun Wu, Hoang
Nguyen, Ji Liu, Madhavi Sewak, Bryce Petrini,
DongHyun Choi, Ivan Philips, Ziyue Wang, Ioana
Bica, Ankush Garg, Jarek Wilkiewicz, Priyanka
Agrawal, Xiaowei Li, Danhao Guo, Emily Xue,
Naseer Shaik, Andrew Leach, Sadh MNM Khan,
Julia Wiesinger, Sammy Jerome, Abhishek Chak-
ladar, Alek Wenjiao Wang, Tina Ornduff, Folake
Abu, Alireza Ghaffarkhah, Marcus Wainwright,
Mario Cortes, Frederick Liu, Joshua Maynez, An-
dreas Terzis, Pouya Samangouei, Riham Mansour,
Tomasz Kepa, Franc¸ois-Xavier Aubet, Anton Al-
gymr, Dan Banica, Agoston Weisz, Andras Or-
ban, Alexandre Senges, Ewa Andrejczuk, Mark
Geller, Niccolo Dal Santo, Valentin Anklin, Majd Al
Merey, Martin Baeuml, Trevor Strohman, Junwen
Bai, Slav Petrov, Yonghui Wu, Demis Hassabis, Ko-
ray Kavukcuoglu, Jeffrey Dean, and Oriol Vinyals.
2024.
Gemini 1.5: Unlocking multimodal under-
standing across millions of tokens of context.
Qwen Team. 2024. Qwen2.5: A party of foundation
models.
Maximilian
Tornqvist,
Mosleh
Mahamud,
Er-
ick Mendez Guzman, and Alexandra Farazouli.
2023.
Exasag: Explainable framework for auto-
matic short answer grading.
In Proceedings of
the 18th Workshop on Innovative Use of NLP for
Building Educational Applications (BEA 2023),
pages 361–371.
Rebecka Weegar and Peter Idestam-Almquist. 2024.
Reducing workload in short answer grading using
machine learning. International Journal of Artificial
Intelligence in Education, 34(2):247–273.
Nico Willms and Ulrike Pad´o. 2022.
A transformer
for sag:
What does it grade?
In Swedish
Language Technology Conference and NLP4CALL,
pages 114–122.
Kevin P Yancey, Geoffrey Laflair, Anthony Verardi,
and Jill Burstein. 2023. Rating short l2 essays on
the cefr scale with gpt-4. In Proceedings of the 18th
Workshop on Innovative Use of NLP for Building
Educational Applications (BEA 2023), pages 576–
584.
An Yang, Baosong Yang, Binyuan Hui, Bo Zheng,
Bowen Yu, Chang Zhou, Chengpeng Li, Chengyuan
Li, Dayiheng Liu, Fei Huang, Guanting Dong, Hao-
ran Wei, Huan Lin, Jialong Tang, Jialin Wang, Jian
Yang, Jianhong Tu, Jianwei Zhang, Jianxin Ma, Jin
Xu, Jingren Zhou, Jinze Bai, Jinzheng He, Jun-
yang Lin, Kai Dang, Keming Lu, Keqin Chen,
Kexin Yang, Mei Li, Mingfeng Xue, Na Ni, Pei
Zhang, Peng Wang, Ru Peng, Rui Men, Ruize Gao,
Runji Lin, Shijie Wang, Shuai Bai, Sinan Tan, Tian-
hang Zhu, Tianhao Li, Tianyu Liu, Wenbin Ge,
Xiaodong Deng, Xiaohuan Zhou, Xingzhang Ren,
Xinyu Zhang, Xipin Wei, Xuancheng Ren, Yang
Fan, Yang Yao, Yichang Zhang, Yu Wan, Yunfei
Chu, Yuqiong Liu, Zeyu Cui, Zhenru Zhang, and
Zhihao Fan. 2024. Qwen2 technical report. arXiv
preprint arXiv:2407.10671.
Su-Youn Yoon. 2023. Short answer grading using one-
shot prompting and text similarity scoring model.
arXiv preprint arXiv:2305.18638.
M Zhang,
S Baral,
N Heffernan,
and A Lan.
Automatic short math answer grading via in-
context meta-learning. arxiv 2022. arXiv preprint
arXiv:2205.15219.
A
Manual Evaluation
For each language, we recruited two native speak-
ers to evaluate the outputs of LLMs on the answers
generation task.
Each annotator was presented
with 360 random samples from the dataset. Each
sample contained a question, a reference answer,
a generated answer with an instruction on whether
it supposed to be matched with the reference an-
swer. If the reference answer and the generated

--- Page 13 ---

Lit R
Lit A
Lat R
Lat A
Model
Class
1
29
1
29
GPT-4o
Match Ents
0
30
4
26
GPT-4o
Match MoreInfo
1
29
2
28
GPT-4o
Match Syns
0
30
2
28
GPT-4o
Match Style
0
60
3
56
GPT-4o
Non-Match MinorCh.
3
57
2
57
GPT-4o
Non-Match Relat.
20
10
12
18
LLaMa2:13b
Match Ents
22
8
15
14
LLaMa2:13b
Match MoreInfo
13
17
10
19
LLaMa2:13b
Match Syns
12
18
14
16
LLaMa2:13b
Match Style
16
43
14
15
LLaMa2:13b
Non-Match MinorCh.
12
46
13
32
LLaMa2:13b
Non-Match Relat.
10
20
5
25
LLaMa3:7b
Match Ents
5
25
8
22
LLaMa3:7b
Match MoreInfo
8
22
3
26
LLaMa3:7b
Match Syns
13
16
14
16
LLaMa3:7b
Match Style
6
54
4
56
LLaMa3:7b
Non-Match MinorCh.
2
58
6
48
LLaMa3:7b
Non-Match Relat.
5
235
14
224
GPT-4o
All
95
142
79
144
LLaMa2:13b
All
44
195
40
193
LLaMa3:7b
All
Table 2: Annotation results. R and A indicate amount of rejected and accepted samples respectively with
the language at the beginning. Class indicates a generation prompt that was used and whether it should
match with the reference answer.

--- Page 14 ---

answer are matched and they are supposed to be
matched or the reference answer and the generated
answer are not matched and they are not supposed
to be matched, the label accept was assigned to
the sample. Otherwise, the label reject was as-
signed. For each model (LLaMa2:13b, GPT-4o,
and LLaMa3:7b) and for each matched generation
type, the annotators were presented with 25 sam-
ples. For non-matched generation methods, the
annotators were presented with 40 samples. The
aggregated results (after cleaning the duplicates)
are presented in the Table 2
Based on the the results, we kept LLaMa3 Non-
Match Relat. generation results and all of the GPT-
4o generated results in the dataset for Lithuanian.
Similarly, we kept LLaMa3 Non-Match Minor-
Changes and GPT-4o (except for Match MoreInfo,
which was excluded by mistake) in the dataset for
Latvian. Our results indicate that GPT-4o is ca-
pable of generating matched and non-matched an-
swers with different methods in these languages,
when LLaMa3 and LLaMa2 struggle.

```
