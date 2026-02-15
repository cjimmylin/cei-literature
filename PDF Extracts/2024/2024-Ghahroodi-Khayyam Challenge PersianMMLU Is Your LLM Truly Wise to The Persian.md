---
title: "2024-Ghahroodi-Khayyam Challenge PersianMMLU Is Your LLM Truly Wise to The Persian - PDF Extract"
source_pdf: "2024-Ghahroodi-Khayyam Challenge PersianMMLU Is Your LLM Truly Wise to The Persian.pdf"
pages: 49
extracted_at: "2026-02-15T17:51:56.065049"
---

# PDF Extract: 2024-Ghahroodi-Khayyam Challenge PersianMMLU Is Your LLM Truly Wise to The Persian

**Source PDF:** 2024-Ghahroodi-Khayyam Challenge PersianMMLU Is Your LLM Truly Wise to The Persian.pdf
**Total Pages:** 49

---

## Content

```
--- Page 1 ---

Preprint. Under review.
Khayyam Challenge (PersianMMLU): Is Your LLM Truly Wise
to The Persian Language?
Omid Ghahroodi♠⋄, Marzia Nouri♠⋄∗, Mohammad Vali Sanian♠⋄∗, Alireza Sahebi♠⋄∗, Doratossadat Dastgheib♠⋄,
Ehsaneddin Asgari‡†, Mahdieh Soleymani Baghshah♠⋄†, Mohammad Hossein Rohban♠⋄†
♠Raia Center for Artificial Intelligence Research
⋄Computer Engineering Department, Sharif University of Technology, Iran
‡Qatar Computing Research Institute, Qatar
{oghahroodi98, nouri.marzia.1999, mvs2667, arsahebi97}@gmail.com
d_dastgheib@sbu.ac.ir, easgari@hbku.edu.qa, {soleymani, rohban}@sharif.edu
Abstract
Evaluating Large Language Models (LLMs) is challenging due to their generative
nature, necessitating precise evaluation methodologies. Additionally, non-English
LLM evaluation lags behind English, resulting in the absence or weakness of
LLMs for many languages. In response to this necessity, we introduce Khayyam
Challenge (also known as PersianMMLU), a meticulously curated collection
comprising 20,192 four-choice questions sourced from 38 diverse tasks extracted
from Persian examinations, spanning a wide spectrum of subjects, complexities,
and ages. The primary objective of the Khayyam Challenge is to facilitate the
rigorous evaluation of LLMs that support the Persian language. Distinctive features
of the Khayyam Challenge are (i) its comprehensive coverage of various topics,
including literary comprehension, mathematics, sciences, logic, intelligence testing,
etc aimed at assessing different facets of LLMs such as language comprehension,
reasoning, and information retrieval across various educational stages, from lower
primary school to upper secondary school (ii) its inclusion of rich metadata such as
human response rates, difficulty levels, and descriptive answers (iii) its utilization
of new data to avoid data contamination issues prevalent in existing frameworks
(iv) its use of original, non-translated data tailored for Persian speakers, ensuring
the framework is free from translation challenges and errors while encompassing
cultural nuances (v) its inherent scalability for future data updates and evaluations
without requiring special human effort. Previous works lacked an evaluation frame-
work that combined all of these features into a single comprehensive benchmark.
Furthermore, we evaluate a wide range of existing LLMs that support the Persian
language, with statistical analyses and interpretations of their outputs. We believe
that the Khayyam Challenge will improve advancements in LLMs for the Persian
language by highlighting the existing limitations of current models, while also
enhancing the precision and depth of evaluations on LLMs, even within the English
language context.
1
Introduction
Large Language Models (LLMs) have recently revolutionized applications of machine intelligence
(Hong et al., 2024; Wu et al., 2023; Thirunavukarasu et al., 2023; Glukhov et al., 2023). The rapid
deployment of these models within industrial and public sector solutions has made evaluating their
capabilities an imperative task (Guo et al., 2023). To address critical aspects of language understanding
and bridge the gap between the knowledge that models observed during pretraining and the measures
∗These authors contributed equally to this work and are considered joint second authors. The order is listed
randomly to reflect their equal contributions.
†These authors contributed equally to this work and are considered joint corresponding authors. The order of
corresponding authors is listed randomly to reflect their equal contributions.
1
arXiv:2404.06644v1  [cs.CL]  9 Apr 2024

--- Page 2 ---

Preprint. Under review.
of success, the MMLU benchmark was introduced (Hendrycks et al., 2021). It assesses the ability of
LLMs across a diverse set containing 57 subjects.
Although automatic translation efforts like MMLU can bridge the gap in evaluation resources for
languages other than English (Achiam et al., 2023), the cultural specificity of these questions limits
their applicability across different languages and cultures. This is particularly true for Persian,
a language with its own rich culture and literature, where direct translation of English MMLU
content may not be suitable for certain culture-specific subjects. In addition, our investigation reveals
significant complications in automatic translation, particularly in specialized domains like Physics,
which can be attributed to the quality of state-of-the-art translations for specific subjects. Despite
advancements in machine translation technology, accurately conveying precise meaning in certain
domains remains a hard task. For instance, the GPT-3.5 automatic translation often fails to include
essential units such as "microjoules" in translations, leading to inaccuracies. Also, loss of information
can occur in translation due to the existence of Persian words that lack exact equivalents in English.
For example, in Persian, there are distinct terms for paternal aunt, maternal aunt, paternal uncle, and
maternal uncle, while in English, only “aunt" and “uncle" are used (See Table 1). This underscores
the inherent difficulty in translating domain-specific terminology accurately. For such reasons, some
studies have evaluated LLMs on original non-English datasets rather than the translated ones. For
instance, Li et al. (2023) has introduced a Chinese dataset across 67 topics and indicated that current
models struggle to achieve accuracies above a certain threshold. Also, Zhang et al. (2023) introduced
a multilingual and multimodal dataset, and showed that multilingual text processing hardly achieves
over 60% accuracy.
Motivated by the mentioned issues, we propose the Khayyam Challenge, also referred to as Per-
sianMMLU, a benchmark designed to analyze the performance of LLMs in Persian and evaluate
their knowledge and abilities comprehensively. Named in honor of the famed Persian polymath
Omar Khayyam, whose contributions spanned various disciplines including Mathematics, Astron-
omy, Philosophy, and Poetry, the Khayyam Challenge embodies the multidimensional nature of
Persian language understanding. This benchmark covers 38 subjects, including Mathematics and
Physics, which require reasoning and computational ability, to humanities and social sciences, de-
manding nuanced understanding and cultural sensitivity. Unlike the previous Persian datasets such
as ParsiNLU (Khashabi et al., 2021), our benchmark includes more diverse topics in addition to
different educational stages. Moreover, our dataset distinguishes itself from previous efforts like
ParSQuAD (Abadani et al., 2021) by being originally constructed in Persian, naturally incorporating
the nuanced semantics and intricacies inherent to the language itself, rather than solely focusing on
literal translations. Unlike PersianQA (Ayoubi, 2021) and PQuAD (Darvishi et al., 2023), which
are extractive datasets where models are tasked with extracting answers from given paragraphs and
questions, our benchmark offers a more comprehensive evaluation of LLMs. This is because the task
of answer extraction alone may not sufficiently assess the models’ overall language understanding
and reasoning capabilities. Our proposed dataset contains “Iran’s national university entrance", and
Kanoon Farhangi Amoozesh (Cultural Educational Center), wherein questions are not only verified
and validated by experts in each subject but also accompanied by metadata for each question. This
metadata includes the difficulty level, a descriptive answer, educational stage, subject, and the specific
topic of the question. Through the Khayyam Challenge, we aim to provide a holistic evaluation
framework that reflects the diverse linguistic and cognitive challenges inherent in processing Persian
text across various domains.
In our evaluations, we assessed several state-of-the-art language models, including GPT-3.5, GPT-4
(OpenAI, 2023), Aya (Üstün et al., 2024), PersianMind (Rostami et al., 2024), mGPT (Shliazhko
et al., 2022), mT0 (Muennighoff et al., 2022), Claude3-haiku (Anthropic, 2024), and XVERSE1, all
purportedly equipped with some level of understanding of the Persian language. Our findings indicate
that while most of these models struggle to grasp Persian nuances, particularly evident in domains
such as Calculus, Logic, and Geometry where accurate comprehension is essential, some exhibit
comparatively better performance in contexts reliant on contextual understanding, such as Economics,
Psychology, and Social studies. Notably, GPT-4 showcased relatively improved performance across
multiple domains. However, there remains a clear imperative need for further enhancements across
all models, especially in technical disciplines like Discrete Mathematics, where precise language
comprehension is paramount for meaningful outcomes.
1https://github.com/xverse-ai
2

--- Page 3 ---

Preprint. Under review.
question
،دسیبل۵۰میلیمتر مربع است، تراز شدت صوت حاصل از یک منبع را۶۰شنوندهای که مساحت پرده گوشش
ثانیه به پرده گوش این شنونده میرسد، چند میکروژول است؟۵۰احساس میکند انرژی که در مدت
correct translation
A listener with an eardrum area of 60mm2 perceives the sound intensity level from a source as 50 decibels.
How much energy reaches the listener’s ear in 50 seconds in microjoules?
API translation
A listener with an ear canal area of 60mm2 perceives the sound intensity level from a source as 50 decibels.
How much energy reaches the listener’s ear in 50 seconds?
questionدر بیت زیر، شاعر از کدام اختیارات شاعری بهره برده است؟
≪≫گویی بطّ سفید جامه به صابون زده است / کبک دری ساق پای در قدح خون زده است
correct translation
In the following verse, which poetic devices has the poet employed?
“The duck’s feathers are so white, as if they’ve been washed with soap /
The partridge’s legs are so red, as if they’ve been dipped in a cup of blood"
API translation
In the following verse, which poetic options did the poet use?
“It’s as if a white duck has put its clothes on soap / the partridge has put its leg in a glass of blood"
question
.دایی دارم۳خاله و۲کیان پسر عمه زهرا، پسر خاله من است. من
زهرا بهترتیب چند عمه و چند عمو دارد؟
correct translation
Kian is the son of the sister of Zahra’s Father, and he is the son of my mother’s sister.
My mother has two sisters and three brothers. How many sisters and brothers does Zahra’s father have?
API translation
Kian is the son of my aunt Zahra. I have 2 aunts and 3 uncles.
How many aunts and how many uncles does Zahra have respectively?
Table 1: Examples illustrating information loss in domain-specific translations from English to Persian
Using the GPT-3.5 API.
Furthermore, our evaluation unveiled new insights. We observed dependencies between the perceived
difficulty of questions for humans versus LLMs. While both encounter similar challenges in tackling
difficult questions, LLMs like GPT-4 demonstrated superior accuracy compared to humans, in
questions intentionally designed to deceive, referred to as trapped questions. Moreover, our analysis
identified biases in certain language models’ responses, such as GPT-3.5 favoring particular choices,
suggesting room for further improvement in these models.
Overall, the Khayyam Challenge (PersianMMLU) marks a significant step forward in evaluating the
language understanding and abilities of LLMs that support the Persian language.
2
Related work
2.1
Large Language Models
Over the past few years, there has been a significant improvement in the performance of language
models. This progress has been observed in line with the scaling law (Kaplan et al., 2020), thanks
to the increasing size of training datasets, enhanced processing power, and new evolved model
architectures. The continuing process of scaling the models resulted in LLMs like GPT-3 (Brown
et al., 2020), GPT-4 (OpenAI, 2023), Claude3, mT0(Muennighoff et al., 2022), XVERSE, Aya (Üstün
et al., 2024), etc.
Even though AI models are highly capable of solving various tasks, they continue to encounter
difficulties when it comes to real-world problems that, for example, require strong reasoning abilities
or complex mathematical calculations (Chang et al., 2024; Zhong et al., 2023). Therefore, we need to
assess the effectiveness of these models in solving high-level tasks. This enables us to identify the
weak points of the models and work towards improving them in the future.
Despite some of the recent LLMs being multilingual, studies indicate that their effectiveness is
not as pronounced in non-Latin or low-resource languages as it is in English (Zhang et al., 2023).
Consequently, it is essential to assess multilingual LLMs on tasks that employ languages other than
English.
2.2
Evaluation of LLMs
Several benchmarks have been developed to assess the performance of LLMs. One of the most
significant benchmarks is MMLU (Hendrycks et al., 2021), which evaluates language models for
answering multiple-choice questions in 57 different tasks, but only in English. M3Exam (Zhang
3

--- Page 4 ---

Preprint. Under review.
Benchmark
Languages
Type
NLU Tasks
# Instance
Metadata
Desc. Ans.
Diff. Lev.
Trap
# Task
MMLU
Eng.
orig.
MCQA
15,908
✕
✕
✕
57
AGIEval
Eng., Chi.
orig.+trans.
MCQA, FIB
8,062
some instances
some instances
✕
20
M3Exam
9 (no Persian)
orig.
MCQA
12,317
✕
= edu. stages
✕
4
ParSQUAD
Persian
trans.
RC
70,560
-
✕
-
477 titles
PersianQA
Persian
orig.
RC
9,938
-
✕
-
991 titles
PQuAD
Persian
orig
RC
80,000
-
✕
-
19
ParsiNLU
Persian
orig.+trans.
MCQA, RC, SA, TE, QP, MT
14,500
✕
✕
✕
3 in MCQA
Khayyam Challenge
Persian
orig.
MCQA
20,192
✓
✓
✓
38
Table 2: Comparison of various features of Persian and English benchmarks. As descriptive answers
and trapped questions were not defined for reading comprehension benchmarks, we marked those
fields with a hyphen (-). Desc. Ans.: Descriptive Answer, Diff. Lev.: Difficulty Level, Eng: English,
Chi: Chinese, orig.: original non-translated question, tran.: translated question, MCQA: Multiple-
Choice Question Answering, FB: Fill in the Blank, RC: Reading Comprehension, SA: Sentiment
Analysis, TE: Textual Entailment, QP: Question Paraphrasing, MT: Machine Translation., edu. stages:
educational stages
et al., 2023) introduces a multilingual, multimodal, and multilevel benchmark for evaluating LLMs
including more than 12K multiple-choice questions from 9 languages (excluding Persian) at three
educational stages. AGIEval (Zhong et al., 2023) is another benchmark that assesses the performance
of LLMs on human-centric standardized exams in English and Chinese languages to measure their
ability in human-level tasks.
There have been a few benchmarks built to assess language models on the Persian language, including
ParSQUAD (Abadani et al., 2021), PersianQA (Ayoubi, 2021), ParsiNLU (Khashabi et al., 2021),
and PQuAD (Darvishi et al., 2023), in which some of their features are compared in Table 2.
ParSQUAD, PersianQA, and PQuAD present extractive datasets where models are asked to extract
answers from given paragraphs. While this task can gauge models’ reading comprehension skills,
it may not effectively evaluate general capabilities and inherent knowledge of models. ParsiNLU
evaluates language models based on 14500 questions from six language understanding tasks, including
multiple-choice QA (MCQA), sentiment analysis, and more (Table 2). However, the questions in
this benchmark fail to reach human-level complexity, thus inadequately assessing important skills
of LLMs, including complex reasoning, needed for solving higher educational stages questions.
Moreover, ParsiNLU covers only three subject tasks in MCQA and lacks adequate metadata, such
as question difficulty levels. This deficiency further restricts our capacity to evaluate the model’s
proficiency across specific tasks and different difficulty levels.
To address this gap, we introduce Khayyam Challenge, which features multiple-choice questions
sourced from high-standard exams, and contains reach metadata to evaluate the innate knowledge
and human-like skills of LLMs across different difficulty levels and educational stages.
3
Data
The Khayyam Challenge presents a robust dataset aimed at enhancing the evaluation of LLMs that
support Persian, particularly in the context of multiple-choice question answering. This dataset encom-
passes a diverse range of subjects, reflecting a comprehensive approach to assessing various cognitive
abilities including language comprehension, reasoning, and knowledge recall across different educa-
tional stages. The educational system in Iran, from which this dataset draws, is structured into 12
years of schooling divided into segments: 6 years of primary education and 6 years of secondary
education. Primary education is split into lower primary school (LPS) for the first 3 years, followed
by upper primary school (UPS) for the next 3 years. Secondary education is similarly divided, with
lower secondary school (LSS) encompassing the first 3 years, and upper secondary school (USS)
comprising the final 3 years.
4

--- Page 5 ---

Preprint. Under review.
(a)
(b)
Figure 1: Question distribution with respect to categories, level of difficulty, and educational stages.
LPS: Lower Primary School, UPS: Upper Primary School, LSS: Lower Secondary School, USS:
Upper Secondary School
3.1
Data construction
The dataset originates from the “Pellekan Yadgiri (Learning Ladder)” website2, a part of the Kanoon
Farhangi Amoozesh3 (Cultural Educational Center), a renowned private educational institution in
Iran. Since conducting its first examination in 1993, Kanoon has been at the forefront of educational
innovation, serving a nationwide network of 450,000 students. The center is highly regarded for its
comprehensive range of educational services, notably its facilitation of creating and administering
smart, customized tests and providing standardized solutions for exercises through the Pellekan
Yadgiri platform. This initiative aims to enable educators to design and administer quality, customized
tests effortlessly and to provide students with insightful feedback to enhance their learning process.
The quality of the questions in the dataset is exceptionally high, a testament to the institution’s
reputable standing in the educational sector. The ongoing development of new questions for various
educational stages and subjects allows for the continuous expansion and updating of the dataset,
reducing the risks of data contamination and erosion. A subset of the questions also includes items
from the national university entrance examination in Iran, adding to the dataset’s authenticity and
relevance.
3.2
Metadata characteristics
The Khayyam Challenge is enriched with valuable metadata that elevates its utility beyond a simple
aggregation of questions. This metadata includes:
• Educational Stage: Specifies the educational stage for which the question is intended (LPS,
UPS, LSS, USS), allowing for the assessment of appropriateness and difficulty relative to
the expected knowledge base at each stage of education.
• Difficulty Level: Each question is classified into one of five distinct difficulty levels: easy,
relatively easy, medium, relatively difficult, and difficult. This nuanced categorization allows
a detailed analysis of question difficulty and examinee performance.
• Descriptive Answers: In addition to the correct answer, our dataset provides a detailed
explanation for each question. This is crucial for understanding the reasoning behind the
correct answer, facilitating a deeper comprehension of the question.
• Trap: Human experts have identified if a question contains a "trap" choice—an incorrect
answer that might be easily mistaken for the correct one. These questions are referred to
as "trapped questions" and are generally more challenging, with the majority classified
2https://peleyad.com/
3https://en.kanoon.ir/
5

--- Page 6 ---

Preprint. Under review.
as difficult. This helps in understanding common misconceptions and the effectiveness of
question design in truly testing knowledge and reasoning abilities.
• Human Performance: This metric quantifies the percentage of students answering a ques-
tion correctly.
• Specific Topic: Questions are meticulously categorized into detailed subjects, such as
"Mathematics > Discrete Maths > Combinatorics." This detailed classification enables
targeted analysis of exam content and provides insights into the distribution and depth of
questions across various subjects.
• Year: Indicates the year when the question was designed, which can provide insights into
the evolution of question complexity and educational standards over time.
The inclusion of this metadata is not merely for augmentative purposes; it serves a critical role in en-
abling comprehensive analyses that can benefit educators, researchers, and developers of educational
technologies. Specifically, it allows for the comparison of performance between human examinees
and LLMs on specific topics under varying difficulty levels. By assessing whether LLMs fall for
the traps as humans or how they approach questions requiring complex thought processes, we can
gain valuable insights into the capabilities and limitations of current AI technologies in educational
contexts.
Moreover, the presence of descriptive answers supports the development of more sophisticated AI
models by facilitating "chain of thought" processing, where the model learns to approach a problem
step-by-step, mirroring human problem-solving methods. This not only enhances the model’s problem-
solving skills but also its ability to explain its reasoning in a manner that is understandable to humans.
3.3
Data statistics
The dataset contains 20,192 multiple-choice questions across 38 tasks, spanning subject areas like
humanities, mathematics, natural science, and social science, along with elements of intelligence
testing. These questions necessitate a blend of knowledge and reasoning. Additionally, the dataset
includes 15,933 questions with human performance data, excluding Iran’s national university entrance
exam questions, and features 3,531 trapped questions. Figure 1-(a) depicts the allocation of questions
among the main categories and their respective tasks. Figure 1-(b) outlines the distribution of questions
based on their levels of difficulty. For more detailed information about the data, refer to Appendix A.
3.4
Key features
The Khayyam Challenge Dataset stands out for several reasons:
• Comprehensive Coverage: It spans a broad spectrum of subjects from literary comprehen-
sion to logic and intelligence testing, catering to different stages of education. This diversity
makes it a versatile tool for assessing language models’ capabilities across various domains.
• Rich Metadata: The inclusion of detailed question metadata enhances the dataset’s utility
for nuanced analysis and model evaluation, providing valuable context for each question.
• New Data Utilization: By incorporating questions never before used in research, the dataset
avoids common data contamination issues, offering a fresh challenge to language models.
• Original, Non-Translated Content: Focused on the Persian language, the dataset eliminates
translation errors and incorporates cultural nuances, making it uniquely valuable for related
linguistic and cultural studies.
• Scalability: The dataset’s design and sourcing methodology ensure its adaptability and
expandability, allowing for straightforward updates and extensions without substantial
human intervention.
6

--- Page 7 ---

Preprint. Under review.
Figure 2: Comparison of accuracy across main categories for humans and various models
4
Experiments
4.1
Settings
We evaluated our benchmark using nine distinct models: GPT-4, GPT-3.5, Aya, XVERSE-13B,
XVERSE-7B, PersianMind, mT0XL, mGPT, and Claude 3/Haiku. Detailed descriptions of each
model can be found in Appendix B. Additionally, we benchmarked a standardized prompt-0 5
template on the entire dataset and two other templates, prompt-1 6 and 7, on a subset of 1000 samples
from the dataset. We also conducted Chain-of-Thought (CoT) 8 on a subset of 1000 samples requiring
CoT, such as mathematical questions. To ensure consistency and fairness throughout our experiments,
we kept all model hyperparameters at their default values. Furthermore, we set the temperature
parameter to zero for all models and did not impose any maximum limit on the number of tokens,
allowing models the freedom to conduct any type of inference they desired.
4.2
Answer extraction methods
We employed three distinct techniques to extract answers: Regex, Single Token Probability, and Full
Answer Probability, and conducted an evaluation of their individual accuracies. In the Regex method,
we developed detailed Regex functions tailored to each model, which is available in our framework, to
accurately capture the desired choices. In cases where Regex failed to identify the correct option, we
utilized a pre-trained model to generate embeddings for each choice within the question, selecting the
most similar one as the correct response. Furthermore, in our analysis, we considered human accuracy
by examining our comprehensive metadata containing response percentages for each question choice.
We chose the answer selected by humans if the combined total of the remaining three options was
lower.
In the Single Token Probability approach, applied to models providing token probabilities, we
calculated the softmax probability of tokens and selected the most probable tokens from 1, 2, 3, and 4
in Persian as the response. As for the Full Answer Probability method as we can see at formula 1, we
tokenized the text of each choice, computed the sum of the logarithm of token probabilities for each
option, standardized it to the length of each option, and chose the most likely option as the answer.
Answer = arg max
i
 
1
ni
ni
∑
j=1
log(pij)
!
(1)
Our analysis shows that the Regex method has the highest accuracy, whereas the full prob method
demonstrated a significant decrease in accuracy compared to the other two approaches.
7

--- Page 8 ---

Preprint. Under review.
4.3
Impact of translation quality
We aim to assess the impact of translation from state-of-the-art (SOTA) translation models on
performance. To do so, we selected a set of sample questions from the dataset and translated them
with the assistance of field experts, as well as using off-the-shelf translation models. Following this,
we evaluated the models’ performance on both sets of samples: those translated with expert assistance
and those translated by models alone. Our findings revealed a notable decrease in performance when
translated with the help of off-the-shelf models, highlighting the need for a new dataset that does not
depend solely on translated data.
4.4
Limitations of few-shot approach
We have developed a benchmark code for our dataset and used the zero-shot and CoT methods to
calculate accuracy. Previous studies (Li et al., 2023; Zhong et al., 2023; Zhang et al., 2023) shows that
using few shots on instruction-tuned models does not enhance accuracy and may even may decrease
it. Therefore, we did not measure accuracy using few-shot techniques.
Main categories
Human
GPT-4
Haiku
GPT-3.5
Aya
XVERSE-13B
XVERSE-7B
PersianMind
mT0XL
mGPT
Random
Humanities
0.71
0.48
0.43
0.34
0.32
0.3
0.28
0.28
0.28
0.26
0.25
Mathematics
0.75
0.4
0.33
0.32
0.28
0.27
0.26
0.26
0.26
0.26
0.25
Natural Science
0.79
0.48
0.4
0.36
0.33
0.31
0.28
0.29
0.28
0.25
0.25
Social Science
0.84
0.63
0.55
0.42
0.41
0.34
0.32
0.3
0.32
0.25
0.26
Other
0.59
0.53
0.39
0.36
0.29
0.29
0.32
0.27
0.28
0.28
0.26
Avg on all tasks
0.74
0.5
0.42
0.36
0.33
0.3
0.29
0.28
0.28
0.26
0.25
Avg on all questions
0.77
0.5
0.43
0.36
0.34
0.31
0.29
0.28
0.29
0.25
0.25
Table 3: Human vs model accuracy for main categories: model answers extracted via Regex
5
Results and discussions
5.1
Results across all models
The evaluation results of zero-shot method for all models across five main categories and three
choice-extraction methods (regex+, single token probability, and full answer probability), as well as
human performance, are presented in the Table 3, and appendix Tables 8, 7. The more comprehensive
results on all 38 tasks are reported in the appendix (Tables 9, 10, 11). Also the results of CoT and its
comparison with zero-shot for GPT-3.5 using regex+ method across three main categories on a subset
of dataset with 1000 questions are presented in appendix Table 6. These results yield the following
key findings:
• Utilizing Regex method for answer extraction (Table 3) results in highest model performance
compared to Single Token Probability (Table 8) and Full Answer Probability (Table 7) due
to its more accurate and comprehensive choice extraction procedure. In the rest of the results
section, we compare the accuracy of models using the Regex method.
• GPT-4 outperforms all other models in all five main categories, with an average accuracy of
8 percent higher than Claude3-haiku, the second-best performing model.
• Aya, an open-source model, performs comparably or even better than GPT-3.5, a closed-
source model, in 8 tasks including Sociology USS and Theology LSS. This demonstrates
the convergence of open-source models’ capabilities towards closed-source models.
• Although PersianMind, a 7B Persian-English LLM, is trained and fine-tuned on 2 billion
Persian tokens (Rostami et al., 2024), its performance is weaker than mT0XL, a multilingual
3.7B LLM.
• The performance gap between the best-performing model, GPT-4, and human averages
around 35%. In subjects like mathematics, this gap widens to 50% accuracy for GPT-4. This
exhibits a real challenge of current LLMs in solving human-level questions, especially in
complex mathematical questions that need high-level mathematical calculation and reasoning
skills.
• The models exhibit weaker performance in mathematics and natural science main categories
compared to humanities and social sciences. This indicates their weaker performance on
8

--- Page 9 ---

Preprint. Under review.
questions requiring high reasoning skills, compared to those mainly reliant on models’
inherent knowledge. This underscores the necessity for enhancing the models’ reasoning
ability in the Persian language.
• The CoT has improved the performance of GPT-3.5 in Mathematics questions by 10%, but
decreased the performance in Humanities questions by 8%.
5.2
Accuracy trends
We demonstrated the accuracy of the models on all three difficulty levels of questions for different
educational stages and question publication years in Figure 9 and Figure 10 in the Appendix E,
respectively. Key findings from these figures include:
• Most model accuracies decline with the increasing publication year for questions with
medium and easy difficulty levels, while human performance remains consistent. This
suggests that humans may have adapted to the evolving questions’ difficulty over time,
whereas models have not.
• There exists a notable performance gap between difficult and medium questions in human
performance, indicating that difficulty level has a stronger impact on human performance
compared to LLMs. Since humans assigned difficulty levels to questions, this gap may stem
from differing perceptions of difficulty between humans and LLMs.
• GPT-4 outperforms humans in difficult questions within four years, as well as during the
initial two educational stages (LPS and UPS). This result suggests that modern LLMs may
excel at analyzing difficult questions compared to humans.
5.3
Selected choice distribution
Figures 12, 13, 14 in the Appendix E depicts the selected choice distributions of various models. It
reveals that despite GPT-3.5 having the lowest count of unanswered questions, GPT-4 surpasses it in
accuracy, indicating a more refined understanding despite its higher non-response rate. Comparatively,
GPT-4 exhibits a more uniform distribution of choice selection, aligning closely with the Ground
Truth and showing less bias than its predecessor, GPT-3.5, which tends towards selecting the second
and third choices. High-performance models like GPT-4 demonstrate a closer alignment with Ground
Truth distribution, indicating a lower bias level and potentially higher utility in applications.
5.4
Trap analysis
Table 15 in the Appendix F compares the performance of models and humans on trapped questions,
using an x/y format where x represents overall accuracy and y the accuracy on trapped questions. The
data shows that while traps often mislead students, leading to nearly random performance, models
like GPT-4 exhibit only a slight drop in accuracy when faced with these traps. However, this drop in
accuracy is most pronounced in the Social Sciences and Humanities. Notably, GPT-4 outperforms
humans across all main categories in handling trapped questions, indicating its robustness against
misleading choices and affirming the different perspectives of difficulty between humans and AI
models.
5.5
Difficulty levels analysis
To explore how humans and LLMs perceive the difficulty of questions, we examined the accuracy
of different models across three difficulty levels. Although our dataset included five labels ranging
from easy to difficult to denote question difficulty, we combined the two relatively easy and relatively
difficult labels into “easy" and “difficult", respectively, to ensure a more balanced distribution of
question difficulty. Our experiment revealed a consistent trend: as question difficulty increased, both
human and model answering accuracy decreased (See Tables 12, 13, 14 in the Appendix E).
Notably, in analytical and knowledge-based topics such as the humanities category, the GPT-4 model
demonstrated superior performance compared to humans in tackling difficult questions. Conversely,
models exhibiting more human-like performance, such as GPT-4, revealed that humans significantly
outperformed them on easier questions. For additional statistical results, refer to Appendix G.
9

--- Page 10 ---

Preprint. Under review.
6
Conclusions
We introduced Khayyam Challenge, also known as PersianMMLU, as the first framework for
assessing LLMs in the Persian language across various tasks, difficulty levels, and educational
stages. This framework includes comprehensive metadata such as human performance, difficulty
levels, and traps. Our assessment encompassed examining the performance of current LLMs on these
datasets, evaluating their ability to extract answers (probabilistic and rule-based paradigms), and
considering various aspects highlighted in the metadata. Our findings revealed that while LLMs
demonstrated relatively satisfactory performance in question-solving tasks (especially on GPT-4),
they still significantly lagged behind human performance, particularly in tasks necessitating reasoning.
Moreover, analysis of metadata concerning difficulty levels and trapped questions unveiled notable
discrepancies between model and human behavior, suggesting fundamental differences in learning
approaches. This underscores the necessity for adaptations in LLMs training methodologies to achieve
human-like proficiency. For future works, we aim to develop an LLM that bridges the performance
gap between existing open-source models and GPT-4.
7
Data Restriction
This dataset is distributed under a Creative Commons No Derivatives (CC ND) license, prohibiting
the creation of derivative works. It is designated exclusively for non-commercial, academic research
to prevent conflicts with Kanoon Farhangi Amoozesh’s (Cultural Educational Center) educational
activities. Researchers are obligated to adhere to this condition, ensuring their utilization of the dataset
remains confined to academic research purposes and respects the restrictions of the CC ND license.
8
Acknowledgement
The authors would like to express their sincere gratitude to Pellekan Yadgiri (Learning Ladder), a
sub-organization of Kanoon Farhangi Amoozesh (Cultural Educational Center), for providing the
valuable dataset and related metadata that was crucial for this research. We are particularly grateful
to Masoud Tajfard for his kind assistance in facilitating the acquisition of this data, which was
permitted for research purposes. The dataset and metadata made available by Pellekan Yadgiri were
instrumental in enabling the analyses and findings presented in this work.
References
Negin Abadani, Jamshid Mozafari, Afsaneh Fatemi, Mohammd Ali Nematbakhsh, and Arefeh
Kazemi. ParSQuAD: Machine translated SQuAD dataset for persian question answering. In 2021
7th International Conference on Web Research (ICWR). IEEE, May 2021.
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman,
Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4 technical report.
arXiv preprint arXiv:2303.08774, 2023.
Anthropic. The claude 3 model family: Opus, sonnet, haiku. https://www-cdn.anthropic.
com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.
pdf, 2024.
Mohammad Yasin Ayoubi, Sajjad & Davoodeh. Persianqa: a dataset for persian question answering.
https://github.com/SajjjadAyobi/PersianQA, 2021.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhari-
wal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agar-
wal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh,
Daniel Ziegler, Jeffrey Wu, Clemens Winter, Chris Hesse, Mark Chen, Eric Sigler, Ma-
teusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCan-
dlish, Alec Radford, Ilya Sutskever, and Dario Amodei.
Language models are few-shot
10

--- Page 11 ---

Preprint. Under review.
learners.
In H. Larochelle, M. Ranzato, R. Hadsell, M.F. Balcan, and H. Lin (eds.), Ad-
vances in Neural Information Processing Systems, volume 33, pp. 1877–1901. Curran Asso-
ciates, Inc., 2020. URL https://proceedings.neurips.cc/paper_files/paper/
2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf.
Yupeng Chang, Xu Wang, Jindong Wang, Yuan Wu, Linyi Yang, Kaijie Zhu, Hao Chen, Xiaoyuan Yi,
Cunxiang Wang, Yidong Wang, Wei Ye, Yue Zhang, Yi Chang, Philip S. Yu, Qiang Yang, and Xing
Xie. A survey on evaluation of large language models. ACM Trans. Intell. Syst. Technol., jan 2024.
ISSN 2157-6904. doi: 10.1145/3641289. URL https://doi.org/10.1145/3641289.
Just Accepted.
Kasra Darvishi, Newsha Shahbodaghkhan, Zahra Abbasiantaeb, and Saeedeh Momtazi. Pquad: A
persian question answering dataset. Computer Speech & Language, 80:101486, 2023. ISSN 0885-
2308. doi: https://doi.org/10.1016/j.csl.2023.101486. URL https://www.sciencedirect.
com/science/article/pii/S0885230823000050.
David Glukhov, Ilia Shumailov, Yarin Gal, Nicolas Papernot, and Vardan Papyan. Llm censorship: A
machine learning challenge or a computer security problem? arXiv preprint arXiv:2307.10719,
2023.
Zishan Guo, Renren Jin, Chuang Liu, Yufei Huang, Dan Shi, Linhao Yu, Yan Liu, Jiaxuan Li, Bojian
Xiong, Deyi Xiong, et al. Evaluating large language models: A comprehensive survey. arXiv
preprint arXiv:2310.19736, 2023.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob
Steinhardt. Measuring massive multitask language understanding. Proceedings of the International
Conference on Learning Representations (ICLR), 2021.
Yining Hong, Haoyu Zhen, Peihao Chen, Shuhong Zheng, Yilun Du, Zhenfang Chen, and Chuang
Gan. 3d-llm: Injecting the 3d world into large language models. Advances in Neural Information
Processing Systems, 36, 2024.
Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott
Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. Scaling laws for neural language models,
2020.
Daniel Khashabi, Arman Cohan, Siamak Shakeri, Pedram Hosseini, Pouya Pezeshkpour, Malihe
Alikhani, Moin Aminnaseri, Marzieh Bitaab, Faeze Brahman, Sarik Ghazarian, Mozhdeh Gheini,
Arman Kabiri, Rabeeh Karimi Mahabadi, Omid Memarrast, Ahmadreza Mosallanezhad, Erfan
Noury, Shahab Raji, Mohammad Sadegh Rasooli, Sepideh Sadeghi, Erfan Sadeqi Azer, Niloo-
far Safi Samghabadi, Mahsa Shafaei, Saber Sheybani, Ali Tazarv, and Yadollah Yaghoobzadeh.
Parsinlu: A suite of language understanding challenges for persian, 2021.
Haonan Li, Yixuan Zhang, Fajri Koto, Yifei Yang, Hai Zhao, Yeyun Gong, Nan Duan, and Timothy
Baldwin. Cmmlu: Measuring massive multitask language understanding in chinese. arXiv preprint
arXiv:2306.09212, 2023.
Niklas Muennighoff, Thomas Wang, Lintang Sutawika, Adam Roberts, Stella Biderman, Teven Le
Scao, M Saiful Bari, Sheng Shen, Zheng-Xin Yong, Hailey Schoelkopf, et al. Crosslingual
generalization through multitask finetuning. arXiv preprint arXiv:2211.01786, 2022.
OpenAI. Gpt-4 technical report, 2023.
Pedram Rostami, Ali Salemi, and Mohammad Javad Dousti. PersianMind: A Cross-Lingual Persian-
English Large Language Model, 2024.
Oleh Shliazhko, Alena Fenogenova, Maria Tikhonova, Vladislav Mikhailov, Anastasia Kozlova, and
Tatiana Shavrina. mgpt: Few-shot learners go multilingual, 2022. URL https://arxiv.org/
abs/2204.07580.
Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, Laura Gutierrez, Ting Fang
Tan, and Daniel Shu Wei Ting. Large language models in medicine. Nature medicine, 29(8):
1930–1940, 2023.
11

--- Page 12 ---

Preprint. Under review.
Ahmet Üstün, Viraat Aryabumi, Zheng-Xin Yong, Wei-Yin Ko, Daniel D’souza, Gbemileke Onilude,
Neel Bhandari, Shivalika Singh, Hui-Lee Ooi, Amr Kayid, et al. Aya model: An instruction
finetuned open-access multilingual language model. arXiv preprint arXiv:2402.07827, 2024.
Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Shaokun Zhang, Erkang Zhu, Beibin Li, Li Jiang,
Xiaoyun Zhang, and Chi Wang. Autogen: Enabling next-gen llm applications via multi-agent
conversation framework. arXiv preprint arXiv:2308.08155, 2023.
Wenxuan Zhang, Mahani Aljunied, Chang Gao, Yew Ken Chia, and Lidong Bing. M3exam: A
multilingual, multimodal, multilevel benchmark for examining large language models. In Thirty-
seventh Conference on Neural Information Processing Systems Datasets and Benchmarks Track,
2023. URL https://openreview.net/forum?id=hJPATsBb3l.
Wanjun Zhong, Ruixiang Cui, Yiduo Guo, Yaobo Liang, Shuai Lu, Yanlin Wang, Amin Saied, Weizhu
Chen, and Nan Duan. Agieval: A human-centric benchmark for evaluating foundation models,
2023.
12

--- Page 13 ---

Preprint. Under review.
A
Data
(a)
(b)
Figure 3: Distribution of questions across publication year and educational stage
Main category
Easy
Medium
Difficult
Sum
Social Science
1480
2513
1856
5849
Humanities
743
1963
1899
4605
Natural Science
1019
2146
1594
4759
Mathematics
998
2254
1394
4646
Other
78
115
140
333
Sum
4318
8991
6883
20192
Table 4: Question distribution across main categories by difficulty level
13

--- Page 14 ---

Preprint. Under review.
Figure 4: Question distribution across all tasks by difficulty level
B
Models
GPT-4
OpenAI has introduced GPT-4 as a large multimodal model. However, the internal structure and
operational specifics of GPT-4 are proprietary and not openly disclosed.
GPT-3.5
GPT-3.5, created by OpenAI, represents a significant advancement in natural language processing
technology. It boasts enhanced capabilities in understanding and generating human-like text, per-
forming impressively across various language tasks like text completion, translation, and question
answering, thanks to its expansive architecture and vast training data.
Claude3-haiku
The Claude 3 Haiku model, developed recently by Anthropic, are proprietary models with undisclosed
architecture and training specifics.
14

--- Page 15 ---

Preprint. Under review.
Aya
Aya, an open-source model by Cohere, is a massively multilingual generative language model
capable of understanding instructions in 101 languages. Over half of these languages are classified as
lower-resourced.
XVERSE-13B
XVERSE-13B, created by Shenzhen Yuanxiang Technology, stands as a versatile multilingual large
language model. Employing a prominent Decoder-only Transformer network structure, XVERSE-13B
has a context length of 8k. It has been meticulously trained on a vast and varied dataset containing 1.4
trillion tokens, covering more than 40 languages including Chinese, English, Russian, and Spanish.
XVERSE-7B
XVERSE-7B, much like its counterpart XVERSE-13B, is a multilingual large language model devel-
oped by Shenzhen Yuanxiang Technology. It shares the same mainstream Decoder-only Transformer
network structure but with a slightly reduced parameter size of 7 billion.
PersianMind
PersianMind is an openly available bilingual large language model. It enriches LLaMa2’s vocabulary
by integrating 10,000 Persian tokens and undergoes training on a dataset containing nearly 2 billion
Persian tokens.
mT0XL
mT0XL originates from the fine-tuning of BLOOM models using xP3, a dataset that encompasses
multilingual content coupled with English prompts. The BLOOM models, which are extensive
decoder-only language models, have been pre-trained on roughly 350 billion tokens. They share
structural similarities with GPT-3.
mGPT
mGPT is an open-source adaptation of GPT-3, having multilingual capabilities. It undergoes pretrain-
ing across 61 languages, drawn from 25 diverse language families, leveraging Wikipedia and the C4
Corpus. Additionally, mGPT offers support for Persian language integration.
15

--- Page 16 ---

Preprint. Under review.
C
Prompt template
را
هندسه دوره دوم متوسطه
در زیر سواالت چند گزینهای )با پاسخ( در مورد
مشاهده میکنید.
سوال:
است.C(، معادله قطری از دایرهm −۲)x + (m + ۱)y = ۶، معادلهmبه ازای هر
کدام است؟Cباشد، محیط دایرهCروی دایرهA(−۱,۱)اگر نقطه
گزینهها:
۲
√۲π (۱
۲π (۲
۳π (۳
۲
√۳π (۴
:جواب
Below you will find multiple-choice questions (with answers) regarding geometry
for the second grade of high school.
Question: For each m the equation (m −2)x + (m + 1)y = 6, is the equation
of chord of a circle C. If the point A(−1, 1) lies on the circle C, what is the
circumference of circle C?
Choices:
1) 2
√
2π
2) 2π
3) 3π
4) 2
√
3π
Answer:
Figure 5: Sample prompt-0 with English translation for enhanced readability
16

--- Page 17 ---

Preprint. Under review.
را
هندسه دوره دوم متوسطه
در زیر سواالت چند گزینهای )با پاسخ( در مورد
مشاهده میکنید.
سوال:
است.C(، معادله قطری از دایرهm −۲)x + (m + ۱)y = ۶، معادلهmبه ازای هر
کدام است؟Cباشد، محیط دایرهCروی دایرهA(−۱,۱)اگر نقطه
گزینهها:
a) 2
√
2π
b) 2π
c) 3π
d) 2
√
3π
:جواب
Below you will find multiple-choice questions (with answers) regarding geometry
for the second grade of high school.
Question: For each m the equation (m −2)x + (m + 1)y = 6, is the equation
of chord of a circle C. If the point A(−1, 1) lies on the circle C, what is the
circumference of circle C?
Choices:
a) 2
√
2π
b) 2π
c) 3π
d) 2
√
3π
Answer:
Figure 6: Sample prompt-1 with English translation for enhanced readability
17

--- Page 18 ---

Preprint. Under review.
The following are multiple choice questions (with answer) about Upper Sec-
ondary School Geometry
:سوال
است.C(، معادله قطری از دایرهm −۲)x + (m + ۱)y = ۶، معادلهmبه ازای هر
کدام است؟Cباشد، محیط دایرهCروی دایرهA(−۱,۱)اگر نقطه
گزینهها:
a) 2
√
2π
b) 2π
c) 3π
d) 2
√
3π
:جواب
Below you will find multiple-choice questions (with answers) regarding geometry
for the second grade of high school.
Question: For each m the equation (m −2)x + (m + 1)y = 6, is the equation
of chord of a circle C. If the point A(−1, 1) lies on the circle C, what is the
circumference of circle C?
Choices:
a) 2
√
2π
b) 2π
c) 3π
d) 2
√
3π
Answer:
Figure 7: Sample prompt-2 with English translation for enhanced readability
18

--- Page 19 ---

Preprint. Under review.
را
هندسه دوره دوم متوسطه
در زیر سواالت چند گزینهای )با پاسخ( در مورد
مشاهده میکنید.
سوال:
است.C(، معادله قطری از دایرهm −۲)x + (m + ۱)y = ۶، معادلهmبه ازای هر
کدام است؟Cباشد، محیط دایرهCروی دایرهA(−۱,۱)اگر نقطه
گزینهها:
a) 2
√
2π
b) 2π
c) 3π
d) 2
√
3π
جواب: بیایید قدم به قدم فکر کنیم
Below you will find multiple-choice questions (with answers) regarding geometry
for the second grade of high school.
Question: For each m the equation (m −2)x + (m + 1)y = 6, is the equation
of chord of a circle C. If the point A(−1, 1) lies on the circle C, what is the
circumference of circle C?
Choices:
a) 2
√
2π
b) 2π
c) 3π
d) 2
√
3π
Answer: Let’s think step by step
Figure 8: Sample CoT prompt with English translation for enhanced readability
19

--- Page 20 ---

Preprint. Under review.
D
Prompt & CoT
Main Categories
Prompt-0
Prompt-1
Prompt-2
Humanities
0.32
0.35
0.36
Mathematics
0.28
0.3
0.34
Natural Science
0.35
0.36
0.37
Social Science
0.43
0.42
0.42
Other
0.45
0.32
0.27
Avg on all tasks
0.37
0.35
0.35
Avg on all questions
0.35
0.36
0.37
Table 5: Accuracy of GPT-3.5 across main categories for different prompts
Main Categories
Prompt-0
CoT
Humanities
0.36
0.28
Mathematics
0.31
0.41
Other
0.33
0.34
Avg on all tasks
0.33
0.34
Avg on all questions
0.31
0.4
Table 6: Accuracy of GPT-3.5 across main categories for main prompt and CoT
20

--- Page 21 ---

Preprint. Under review.
E
Accuracy & candidate choice distribution
Main categories
Human
GPT-4
Haiku
GPT-3.5
Aya
XVERSE-13B
XVERSE-7B
PersianMind
mT0XL
mGPT
Random
Humanities
0.71
0.48
0.43
0.34
0.27
0.3
0.27
0.26
0.26
0.24
0.25
Mathematics
0.75
0.4
0.33
0.32
0.24
0.25
0.25
0.24
0.23
0.23
0.25
Natural Science
0.79
0.48
0.4
0.36
0.29
0.31
0.28
0.25
0.26
0.24
0.25
Social Science
0.84
0.63
0.55
0.42
0.33
0.34
0.32
0.27
0.29
0.25
0.26
Other
0.59
0.53
0.39
0.36
0.3
0.3
0.32
0.29
0.28
0.24
0.26
Avg on all tasks
0.74
0.5
0.42
0.36
0.28
0.3
0.29
0.26
0.26
0.24
0.25
Avg on all questions
0.77
0.5
0.43
0.36
0.28
0.3
0.28
0.26
0.26
0.24
0.25
Table 7: Human vs model accuracy for main categories: model answers extracted via full answer
probability
Main categories
Human
GPT-4
Haiku
GPT-3.5
Aya
XVERSE-13B
XVERSE-7B
PersianMind
mT0XL
mGPT
Random
Humanities
0.71
0.48
0.43
0.34
0.32
0.29
0.27
0.26
0.27
0.23
0.25
Mathematics
0.75
0.4
0.33
0.32
0.27
0.26
0.25
0.25
0.26
0.23
0.25
Natural Science
0.79
0.48
0.4
0.36
0.33
0.3
0.28
0.26
0.28
0.21
0.25
Social Science
0.84
0.63
0.55
0.42
0.41
0.34
0.32
0.29
0.31
0.22
0.26
Other
0.59
0.53
0.39
0.36
0.27
0.3
0.32
0.27
0.3
0.23
0.26
Avg on all tasks
0.74
0.5
0.42
0.36
0.32
0.3
0.29
0.27
0.28
0.22
0.25
Avg on all questions
0.77
0.5
0.43
0.36
0.34
0.3
0.29
0.27
0.28
0.22
0.25
Table 8: Human vs model accuracy for main categories: model answers extracted via single token
probability
21

--- Page 22 ---

Preprint. Under review.
Task
Human
GPT-4
Haiku
GPT-3.5
Aya
XVERSE-13B
XVERSE-7B
PersianMind
mT0XL
mGPT
Random
Analytical Talent LSS
0.59
0.53
0.39
0.36
0.29
0.29
0.32
0.27
0.28
0.28
0.26
Calculus USS
0.85
0.34
0.29
0.26
0.26
0.25
0.26
0.21
0.25
0.27
0.29
Chemistry USS
0.73
0.36
0.3
0.31
0.3
0.28
0.27
0.26
0.28
0.26
0.24
Discrete Mathematics USS
0.78
0.29
0.27
0.22
0.24
0.24
0.23
0.29
0.26
0.27
0.3
Economy USS
0.69
0.62
0.51
0.4
0.47
0.33
0.25
0.28
0.31
0.25
0.29
Geography USS
0.85
0.56
0.5
0.38
0.36
0.3
0.31
0.3
0.28
0.26
0.25
Geology USS
0.89
0.56
0.52
0.39
0.36
0.32
0.23
0.27
0.25
0.25
0.26
Geometry USS
0.83
0.34
0.32
0.3
0.28
0.27
0.28
0.28
0.25
0.23
0.24
History USS
0.85
0.55
0.47
0.37
0.33
0.33
0.29
0.31
0.27
0.25
0.24
Logic USS
0.58
0.43
0.4
0.31
0.29
0.33
0.29
0.31
0.22
0.21
0.26
Mathematical and Logical Intelligence UPS
0.44
0.45
0.28
0.26
0.29
0.22
0.22
0.24
0.21
0.28
0.18
Mathematics LPS
0.77
0.56
0.38
0.39
0.31
0.33
0.32
0.22
0.27
0.25
0.26
Mathematics LSS
0.77
0.4
0.36
0.32
0.31
0.31
0.26
0.29
0.25
0.25
0.26
Mathematics UPS
0.66
0.49
0.35
0.35
0.29
0.27
0.27
0.26
0.27
0.27
0.28
Mathematics USS
0.84
0.34
0.29
0.31
0.27
0.24
0.25
0.27
0.25
0.25
0.26
Mathematics and Statistics USS
0.63
0.42
0.36
0.34
0.27
0.28
0.28
0.28
0.27
0.27
0.23
Natural Sciences LPS
0.85
0.79
0.71
0.61
0.5
0.48
0.4
0.33
0.38
0.28
0.25
Natural Sciences LSS
0.72
0.59
0.46
0.39
0.33
0.32
0.29
0.3
0.28
0.25
0.23
Natural Sciences UPS
0.82
0.74
0.63
0.5
0.43
0.39
0.32
0.29
0.3
0.24
0.26
Persian Literature LPS
0.83
0.66
0.55
0.42
0.41
0.39
0.3
0.29
0.33
0.29
0.25
Persian Literature LSS
0.77
0.51
0.46
0.34
0.3
0.29
0.28
0.26
0.3
0.24
0.25
Persian Literature UPS
0.8
0.57
0.53
0.38
0.31
0.35
0.28
0.26
0.31
0.26
0.24
Persian Literature USS
0.59
0.35
0.32
0.27
0.29
0.25
0.26
0.26
0.26
0.25
0.25
Philosophy USS
0.61
0.54
0.51
0.39
0.36
0.31
0.26
0.31
0.33
0.27
0.24
Physics USS
0.83
0.39
0.32
0.29
0.27
0.28
0.24
0.27
0.27
0.25
0.26
Probability and Statistics USS
0.77
0.39
0.35
0.31
0.25
0.25
0.24
0.2
0.23
0.23
0.23
Psychology USS
0.79
0.63
0.5
0.4
0.4
0.32
0.35
0.32
0.35
0.22
0.24
Social Studies LPS
0.94
0.85
0.77
0.67
0.62
0.59
0.44
0.45
0.38
0.25
0.23
Social Studies LSS
0.86
0.67
0.57
0.43
0.39
0.35
0.34
0.29
0.31
0.23
0.26
Social Studies UPS
0.89
0.73
0.7
0.52
0.46
0.36
0.36
0.38
0.36
0.26
0.26
Sociology USS
0.82
0.48
0.44
0.33
0.34
0.32
0.28
0.27
0.26
0.27
0.24
Speed and Accuracy UPS
0.84
0.38
0.32
0.36
0.27
0.29
0.26
0.26
0.28
0.26
0.17
Theology LPS
0.88
0.84
0.71
0.61
0.54
0.48
0.44
0.34
0.51
0.21
0.31
Theology LSS
0.88
0.69
0.61
0.45
0.46
0.38
0.34
0.31
0.35
0.26
0.29
Theology UPS
0.9
0.79
0.68
0.54
0.49
0.41
0.38
0.34
0.35
0.25
0.28
Theology USS
0.8
0.53
0.45
0.34
0.37
0.28
0.28
0.26
0.3
0.24
0.24
Verbal and Linguistic Intelligence UPS
0.63
0.55
0.49
0.43
0.36
0.37
0.27
0.28
0.31
0.33
0.26
Biology USS
0.73
0.32
0.27
0.3
0.29
0.27
0.28
0.3
0.26
0.22
0.25
Avg on all tasks
0.77
0.53
0.46
0.38
0.35
0.32
0.3
0.29
0.29
0.25
0.25
Avg on all questions
0.77
0.5
0.43
0.36
0.34
0.31
0.29
0.28
0.29
0.25
0.25
Table 9: Accuracy of humans and different models across all subjects and educational stages: model
answers extracted via Regex method. LPS: Lower Primary School, UPS: Upper Primary School, LSS:
Lower Secondary School, USS: Upper Secondary School
22

--- Page 23 ---

Preprint. Under review.
Task
Human
GPT-4
Haiku
GPT-3.5
Aya
XVERSE-13B
XVERSE-7B
PersianMind
mT0XL
mGPT
Random
Analytical Talent LSS
0.59
0.53
0.39
0.36
0.27
0.3
0.32
0.27
0.3
0.23
0.26
Calculus USS
0.85
0.34
0.29
0.26
0.26
0.28
0.3
0.24
0.25
0.25
0.29
Chemistry USS
0.73
0.36
0.3
0.31
0.3
0.29
0.27
0.24
0.27
0.24
0.24
Discrete Mathematics USS
0.78
0.29
0.27
0.22
0.24
0.27
0.26
0.26
0.24
0.27
0.3
Economy USS
0.69
0.62
0.51
0.4
0.43
0.33
0.24
0.3
0.25
0.22
0.29
Geography USS
0.85
0.56
0.5
0.38
0.36
0.32
0.31
0.29
0.28
0.24
0.25
Geology USS
0.89
0.56
0.52
0.39
0.36
0.32
0.22
0.2
0.25
0.2
0.26
Geometry USS
0.83
0.34
0.32
0.3
0.28
0.25
0.25
0.24
0.26
0.22
0.24
History USS
0.85
0.55
0.47
0.37
0.34
0.31
0.28
0.27
0.27
0.21
0.24
Logic USS
0.58
0.43
0.4
0.31
0.29
0.3
0.29
0.29
0.28
0.29
0.26
Mathematical and Logical Intelligence UPS
0.44
0.45
0.28
0.26
0.3
0.27
0.24
0.29
0.29
0.27
0.18
Mathematics LPS
0.77
0.56
0.38
0.39
0.29
0.25
0.27
0.27
0.27
0.22
0.26
Mathematics LSS
0.77
0.4
0.36
0.32
0.3
0.23
0.25
0.25
0.26
0.21
0.26
Mathematics UPS
0.66
0.49
0.35
0.35
0.27
0.24
0.23
0.23
0.23
0.21
0.28
Mathematics USS
0.84
0.34
0.29
0.31
0.27
0.23
0.23
0.24
0.28
0.23
0.26
Mathematics and Statistics USS
0.63
0.42
0.36
0.34
0.26
0.31
0.27
0.26
0.28
0.23
0.23
Natural Sciences LPS
0.85
0.79
0.71
0.61
0.51
0.44
0.39
0.34
0.33
0.19
0.25
Natural Sciences LSS
0.72
0.59
0.46
0.39
0.34
0.31
0.29
0.27
0.29
0.18
0.23
Natural Sciences UPS
0.82
0.74
0.63
0.5
0.42
0.37
0.32
0.26
0.27
0.19
0.26
Persian Literature LPS
0.83
0.66
0.55
0.42
0.41
0.37
0.3
0.26
0.34
0.19
0.25
Persian Literature LSS
0.77
0.51
0.46
0.34
0.32
0.3
0.28
0.28
0.26
0.26
0.25
Persian Literature UPS
0.8
0.57
0.53
0.38
0.36
0.32
0.28
0.25
0.31
0.2
0.24
Persian Literature USS
0.59
0.35
0.32
0.27
0.28
0.25
0.26
0.25
0.25
0.22
0.25
Philosophy USS
0.61
0.54
0.51
0.39
0.34
0.31
0.26
0.29
0.26
0.27
0.24
Physics USS
0.83
0.39
0.32
0.29
0.27
0.27
0.25
0.27
0.28
0.22
0.26
Probability and Statistics USS
0.77
0.39
0.35
0.31
0.24
0.29
0.21
0.25
0.25
0.22
0.23
Psychology USS
0.79
0.63
0.5
0.4
0.37
0.35
0.36
0.3
0.33
0.24
0.24
Social Studies LPS
0.94
0.85
0.77
0.67
0.59
0.53
0.43
0.36
0.32
0.17
0.23
Social Studies LSS
0.86
0.67
0.57
0.43
0.39
0.35
0.34
0.29
0.31
0.22
0.26
Social Studies UPS
0.89
0.73
0.7
0.52
0.48
0.36
0.37
0.34
0.33
0.2
0.26
Sociology USS
0.82
0.48
0.44
0.33
0.34
0.29
0.29
0.26
0.28
0.22
0.24
Speed and Accuracy UPS
0.84
0.38
0.32
0.36
0.24
0.23
0.26
0.25
0.26
0.21
0.17
Theology LPS
0.88
0.84
0.71
0.61
0.56
0.44
0.44
0.33
0.46
0.13
0.31
Theology LSS
0.88
0.69
0.61
0.45
0.48
0.38
0.32
0.31
0.34
0.23
0.29
Theology UPS
0.9
0.79
0.68
0.54
0.49
0.4
0.38
0.33
0.39
0.22
0.28
Theology USS
0.8
0.53
0.45
0.34
0.37
0.28
0.28
0.26
0.26
0.23
0.24
Verbal and Linguistic Intelligence UPS
0.63
0.55
0.49
0.43
0.43
0.35
0.27
0.27
0.34
0.22
0.26
Biology USS
0.73
0.32
0.27
0.3
0.28
0.27
0.29
0.25
0.25
0.23
0.25
Avg on all tasks
0.77
0.53
0.46
0.38
0.35
0.31
0.29
0.27
0.29
0.22
0.25
Avg on all questions
0.77
0.5
0.43
0.36
0.34
0.3
0.29
0.27
0.28
0.22
0.25
Table 10: Accuracy of human and different models across all subjects and educational stages: model
answers extracted via single token probability. LPS: Lower Primary School, UPS: Upper Primary
School, LSS: Lower Secondary School, USS: Upper Secondary School
23

--- Page 24 ---

Preprint. Under review.
Task
Human
GPT-4
Haiku
GPT-3.5
Aya
XVERSE-13B
XVERSE-7B
PersianMind
mT0XL
mGPT
Random
Analytical Talent LSS
0.59
0.53
0.39
0.36
0.3
0.3
0.32
0.29
0.28
0.24
0.26
Calculus USS
0.85
0.34
0.29
0.26
0.21
0.25
0.28
0.22
0.2
0.21
0.29
Chemistry USS
0.73
0.36
0.3
0.31
0.28
0.29
0.28
0.26
0.26
0.24
0.24
Discrete Mathematics USS
0.78
0.29
0.27
0.22
0.22
0.27
0.26
0.29
0.28
0.26
0.3
Economy USS
0.69
0.62
0.51
0.4
0.27
0.33
0.23
0.24
0.23
0.23
0.29
Geography USS
0.85
0.56
0.5
0.38
0.31
0.32
0.31
0.29
0.26
0.26
0.25
Geology USS
0.89
0.56
0.52
0.39
0.3
0.32
0.22
0.27
0.26
0.23
0.26
Geometry USS
0.83
0.34
0.32
0.3
0.25
0.25
0.24
0.23
0.22
0.23
0.24
History USS
0.85
0.55
0.47
0.37
0.28
0.31
0.29
0.26
0.26
0.24
0.24
Logic USS
0.58
0.43
0.4
0.31
0.27
0.32
0.29
0.22
0.21
0.25
0.26
Mathematical and Logical Intelligence UPS
0.44
0.45
0.28
0.26
0.25
0.26
0.23
0.26
0.26
0.26
0.18
Mathematics LPS
0.77
0.56
0.38
0.39
0.23
0.26
0.28
0.25
0.25
0.25
0.26
Mathematics LSS
0.77
0.4
0.36
0.32
0.27
0.24
0.24
0.24
0.24
0.24
0.26
Mathematics UPS
0.66
0.49
0.35
0.35
0.26
0.23
0.23
0.27
0.22
0.22
0.28
Mathematics USS
0.84
0.34
0.29
0.31
0.22
0.22
0.22
0.22
0.22
0.24
0.26
Mathematics and Statistics USS
0.63
0.42
0.36
0.34
0.23
0.31
0.27
0.25
0.21
0.23
0.23
Natural Sciences LPS
0.85
0.79
0.71
0.61
0.39
0.45
0.4
0.27
0.28
0.21
0.25
Natural Sciences LSS
0.72
0.59
0.46
0.39
0.3
0.31
0.29
0.25
0.29
0.25
0.23
Natural Sciences UPS
0.82
0.74
0.63
0.5
0.31
0.39
0.33
0.26
0.23
0.22
0.26
Persian Literature LPS
0.83
0.66
0.55
0.42
0.32
0.37
0.3
0.25
0.25
0.22
0.25
Persian Literature LSS
0.77
0.51
0.46
0.34
0.26
0.3
0.28
0.23
0.26
0.23
0.25
Persian Literature UPS
0.8
0.57
0.53
0.38
0.27
0.33
0.28
0.26
0.28
0.25
0.24
Persian Literature USS
0.59
0.35
0.32
0.27
0.24
0.25
0.26
0.26
0.25
0.22
0.25
Philosophy USS
0.61
0.54
0.51
0.39
0.27
0.32
0.26
0.27
0.27
0.3
0.24
Physics USS
0.83
0.39
0.32
0.29
0.25
0.26
0.24
0.23
0.27
0.23
0.26
Probability and Statistics USS
0.77
0.39
0.35
0.31
0.22
0.28
0.21
0.23
0.27
0.2
0.23
Psychology USS
0.79
0.63
0.5
0.4
0.3
0.34
0.36
0.3
0.23
0.23
0.24
Social Studies LPS
0.94
0.85
0.77
0.67
0.47
0.53
0.44
0.32
0.29
0.25
0.23
Social Studies LSS
0.86
0.67
0.57
0.43
0.35
0.35
0.34
0.28
0.3
0.22
0.26
Social Studies UPS
0.89
0.73
0.7
0.52
0.37
0.37
0.37
0.28
0.31
0.26
0.26
Sociology USS
0.82
0.48
0.44
0.33
0.25
0.27
0.28
0.26
0.26
0.25
0.24
Speed and Accuracy UPS
0.84
0.38
0.32
0.36
0.25
0.25
0.28
0.22
0.23
0.24
0.17
Theology LPS
0.88
0.84
0.71
0.61
0.38
0.46
0.44
0.23
0.38
0.24
0.31
Theology LSS
0.88
0.69
0.61
0.45
0.36
0.37
0.33
0.25
0.34
0.27
0.29
Theology UPS
0.9
0.79
0.68
0.54
0.37
0.4
0.38
0.27
0.29
0.24
0.28
Theology USS
0.8
0.53
0.45
0.34
0.3
0.28
0.28
0.24
0.29
0.26
0.24
Verbal and Linguistic Intelligence UPS
0.63
0.55
0.49
0.43
0.35
0.38
0.26
0.29
0.31
0.27
0.26
Biology USS
0.73
0.32
0.27
0.3
0.28
0.28
0.28
0.25
0.25
0.29
0.25
Avg on all tasks
0.77
0.53
0.46
0.38
0.29
0.32
0.29
0.26
0.26
0.24
0.25
Avg on all questions
0.77
0.5
0.43
0.36
0.28
0.3
0.28
0.26
0.26
0.24
0.25
Table 11: Accuracy of human and different models across all subjects and educational stages: model
answers extracted via full answer probability. LPS: Lower Primary School, UPS: Upper Primary
School, LSS: Lower Secondary School, USS: Upper Secondary School
24

--- Page 25 ---

Preprint. Under review.
Figure 9: Accuracy of models and humans across three difficulty levels, segmented by question
educational stage.
25

--- Page 26 ---

Preprint. Under review.
Figure 10: Accuracy of models and humans across three difficulty levels, segmented by question
publication year.
26

--- Page 27 ---

Preprint. Under review.
Main category
Difficulty level
Human
GPT-4
Haiku
GPT-3.5
Aya
XVERSE-13B
XVERSE-7B
PersianMind
mT0XL
mGPT
Random
Humanities
Difficult
0.35
0.39
0.36
0.31
0.3
0.28
0.26
0.27
0.27
0.26
0.24
Humanities
Easy
0.99
0.61
0.54
0.39
0.36
0.33
0.3
0.28
0.3
0.24
0.26
Humanities
Medium
0.86
0.5
0.45
0.34
0.32
0.32
0.28
0.28
0.29
0.26
0.25
Mathematics
Difficult
0.4
0.36
0.3
0.3
0.29
0.26
0.27
0.25
0.27
0.26
0.24
Mathematics
Easy
0.99
0.49
0.36
0.35
0.28
0.29
0.28
0.28
0.26
0.26
0.26
Mathematics
Medium
0.84
0.38
0.33
0.32
0.27
0.27
0.25
0.26
0.25
0.25
0.26
Natural Science
Difficult
0.5
0.39
0.32
0.32
0.31
0.28
0.27
0.27
0.27
0.24
0.26
Natural Science
Easy
1.0
0.66
0.58
0.48
0.41
0.38
0.32
0.33
0.3
0.25
0.26
Natural Science
Medium
0.91
0.45
0.38
0.33
0.3
0.31
0.26
0.28
0.28
0.25
0.24
Social Science
Difficult
0.55
0.53
0.46
0.36
0.37
0.3
0.27
0.28
0.3
0.25
0.26
Social Science
Easy
0.99
0.68
0.61
0.48
0.46
0.38
0.37
0.34
0.36
0.24
0.25
Social Science
Medium
0.95
0.66
0.57
0.43
0.42
0.34
0.34
0.31
0.32
0.26
0.26
Other
Difficult
0.21
0.44
0.29
0.28
0.23
0.23
0.26
0.23
0.28
0.34
0.24
Other
Easy
0.99
0.67
0.51
0.46
0.37
0.36
0.37
0.35
0.28
0.17
0.24
Other
Medium
0.78
0.55
0.43
0.4
0.31
0.32
0.35
0.26
0.27
0.28
0.3
Avg on all tasks
Avg on all tasks
0.75
0.52
0.43
0.37
0.33
0.31
0.3
0.28
0.29
0.25
0.25
Avg on all questions
Avg on all questions
0.77
0.5
0.43
0.36
0.34
0.31
0.29
0.28
0.29
0.25
0.25
Table 12: Human vs model accuracy for all tasks: model answers extracted via regex
Main category
Difficulty level
Human
GPT-4
Haiku
GPT-3.5
Aya
XVERSE-13B
XVERSE-7B
PersianMind
mT0XL
mGPT
Random
Humanities
Difficult
0.35
0.39
0.36
0.31
0.3
0.27
0.26
0.26
0.26
0.23
0.24
Humanities
Easy
0.99
0.61
0.54
0.39
0.38
0.31
0.29
0.28
0.29
0.24
0.26
Humanities
Medium
0.86
0.5
0.45
0.34
0.33
0.31
0.28
0.26
0.28
0.22
0.25
Mathematics
Difficult
0.4
0.36
0.3
0.3
0.28
0.25
0.25
0.25
0.28
0.23
0.24
Mathematics
Easy
0.99
0.49
0.36
0.35
0.27
0.27
0.26
0.24
0.26
0.21
0.26
Mathematics
Medium
0.84
0.38
0.33
0.32
0.26
0.26
0.25
0.25
0.25
0.24
0.26
Natural Science
Difficult
0.5
0.39
0.32
0.32
0.3
0.28
0.28
0.26
0.27
0.22
0.26
Natural Science
Easy
1.0
0.66
0.58
0.48
0.41
0.37
0.31
0.29
0.27
0.2
0.26
Natural Science
Medium
0.91
0.45
0.38
0.33
0.3
0.29
0.27
0.25
0.28
0.21
0.24
Social Science
Difficult
0.55
0.53
0.46
0.36
0.37
0.3
0.27
0.26
0.29
0.22
0.26
Social Science
Easy
0.99
0.68
0.61
0.48
0.47
0.38
0.36
0.32
0.32
0.22
0.25
Social Science
Medium
0.95
0.66
0.57
0.43
0.42
0.34
0.34
0.31
0.31
0.23
0.26
Other
Difficult
0.21
0.44
0.29
0.28
0.22
0.27
0.24
0.26
0.25
0.22
0.24
Other
Easy
0.99
0.67
0.51
0.46
0.32
0.37
0.41
0.28
0.29
0.22
0.24
Other
Medium
0.78
0.55
0.43
0.4
0.3
0.28
0.37
0.28
0.37
0.25
0.3
Avg on all tasks
Avg on all tasks
0.75
0.52
0.43
0.37
0.33
0.3
0.3
0.27
0.29
0.22
0.25
Avg on all questions
Avg on all questions
0.77
0.5
0.43
0.36
0.34
0.3
0.29
0.27
0.28
0.22
0.25
Table 13: Human vs model accuracy for all tasks: model answers extracted via single token probability
Main category
Difficulty level
Human
GPT-4
Haiku
GPT-3.5
Aya
XVERSE-13B
XVERSE-7B
PersianMind
mT0XL
mGPT
Random
Humanities
Difficult
0.35
0.39
0.36
0.31
0.25
0.28
0.26
0.26
0.25
0.24
0.24
Humanities
Easy
0.99
0.61
0.54
0.39
0.3
0.32
0.29
0.24
0.28
0.22
0.26
Humanities
Medium
0.86
0.5
0.45
0.34
0.27
0.31
0.28
0.26
0.26
0.24
0.25
Mathematics
Difficult
0.4
0.36
0.3
0.3
0.24
0.26
0.25
0.26
0.25
0.23
0.24
Mathematics
Easy
0.99
0.49
0.36
0.35
0.24
0.26
0.25
0.22
0.23
0.21
0.26
Mathematics
Medium
0.84
0.38
0.33
0.32
0.24
0.25
0.24
0.24
0.22
0.24
0.26
Natural Science
Difficult
0.5
0.39
0.32
0.32
0.27
0.28
0.28
0.26
0.26
0.24
0.26
Natural Science
Easy
1.0
0.66
0.58
0.48
0.33
0.37
0.32
0.25
0.27
0.24
0.26
Natural Science
Medium
0.91
0.45
0.38
0.33
0.28
0.3
0.27
0.24
0.26
0.24
0.24
Social Science
Difficult
0.55
0.53
0.46
0.36
0.29
0.3
0.28
0.26
0.27
0.25
0.26
Social Science
Easy
0.99
0.68
0.61
0.48
0.37
0.39
0.37
0.27
0.31
0.25
0.25
Social Science
Medium
0.95
0.66
0.57
0.43
0.33
0.34
0.34
0.27
0.29
0.25
0.26
Other
Difficult
0.21
0.44
0.29
0.28
0.21
0.29
0.26
0.2
0.25
0.21
0.24
Other
Easy
0.99
0.67
0.51
0.46
0.38
0.36
0.4
0.35
0.31
0.23
0.24
Other
Medium
0.78
0.55
0.43
0.4
0.36
0.29
0.36
0.37
0.3
0.29
0.3
Avg on all tasks
Avg on all tasks
0.75
0.52
0.43
0.37
0.29
0.3
0.29
0.26
0.27
0.24
0.25
Avg on all questions
Avg on all questions
0.77
0.5
0.43
0.36
0.28
0.3
0.28
0.26
0.26
0.24
0.25
Table 14: Human vs model accuracy for all tasks: model answers extracted via full answer probability
27

--- Page 28 ---

Preprint. Under review.
Figure 11: Selected choice distribution of different models: model answers extracted via regex
28

--- Page 29 ---

Preprint. Under review.
Figure 12: Selected choice distribution of different models: model answers extracted via regex+
29

--- Page 30 ---

Preprint. Under review.
Figure 13: Selected choice distribution of different models: model answers extracted via single token
probability
30

--- Page 31 ---

Preprint. Under review.
Figure 14: Selected choice distribution of different models: model answers extracted via full answer
probability
31

--- Page 32 ---

Preprint. Under review.
F
Trap
Main Categories
Human
GPT-4
Haiku
GPT-3.5
Aya
XVERSE-13B
XVERSE-7B
PersianMind
mT0XL
mGPT
Random
Humanities
0.71 / 0.22
0.48 / 0.32
0.43 / 0.31
0.34 / 0.29
0.32 / 0.29
0.3 / 0.27
0.28 / 0.23
0.28 / 0.25
0.28 / 0.25
0.26 / 0.27
0.25 / 0.24
Mathematics
0.75 / 0.25
0.4 / 0.38
0.33 / 0.28
0.32 / 0.31
0.28 / 0.29
0.27 / 0.26
0.26 / 0.27
0.26 / 0.25
0.26 / 0.25
0.26 / 0.25
0.25 / 0.25
Natural Science
0.79 / 0.31
0.48 / 0.41
0.4 / 0.32
0.36 / 0.29
0.33 / 0.29
0.31 / 0.27
0.28 / 0.25
0.29 / 0.26
0.28 / 0.28
0.25 / 0.23
0.25 / 0.24
Social Science
0.84 / 0.37
0.63 / 0.42
0.55 / 0.39
0.42 / 0.3
0.41 / 0.35
0.34 / 0.28
0.32 / 0.26
0.3 / 0.25
0.32 / 0.26
0.25 / 0.25
0.26 / 0.27
Other
0.59 / 0.11
0.53 / 0.47
0.39 / 0.27
0.36 / 0.33
0.29 / 0.3
0.29 / 0.22
0.32 / 0.26
0.27 / 0.2
0.28 / 0.25
0.28 / 0.31
0.26 / 0.19
Avg on all tasks
0.74 / 0.25
0.5 / 0.4
0.42 / 0.31
0.36 / 0.31
0.33 / 0.31
0.3 / 0.26
0.29 / 0.25
0.28 / 0.24
0.28 / 0.26
0.26 / 0.26
0.25 / 0.24
Avg on all questions
0.77 / 0.28
0.5 / 0.38
0.43 / 0.32
0.36 / 0.3
0.34 / 0.31
0.31 / 0.27
0.29 / 0.25
0.28 / 0.25
0.29 / 0.26
0.25 / 0.26
0.25 / 0.25
Table 15: Accuracy of humans and various models on main categories, including all questions/trapped
questions.
G
Statistical tests
Model
Response length T-Test
Question length T-Test
Answer T-Test
Human
NA / NA
-10.88 / 0.0
-12.40 / 0.0
XVERSE-13B
-5.52 / 0.0
-3.62 / 0.0
-8.51 / 0.0
mGPT
0.52 / 0.6
0.3 / 0.76
-1.27 / 0.2
PersianMind
-0.35 / 0.73
-2.81 / 0.0
-4.08 / 0.0
GPT-4
8.39 / 0.0
-11.42 / 0.0
-25.97 / 0.0
Aya
0.24 / 0.81
-4.55 / 0.0
-12.32 / 0.0
Haiku
-10.68 / 0.0
-12.68 / 0.0
-22.78 / 0.0
mT0XL
-0.13 / 0.9
-0.99 / 0.32
-5.18 / 0.0
XVERSE-7B
-0.07 / 0.95
-3.37 / 0.0
-7.48 / 0.0
GPT-3.5
-1.26 / 0.21
-7.25 / 0.0
-14.53 / 0.0
Table 16: T-test comparison of question and response string lengths among the models
32

--- Page 33 ---

Preprint. Under review.
Figure 15: Comparing the lengths of GPT-4 generated strings, descriptive answers, and questions
33

--- Page 34 ---

Preprint. Under review.
H
Sample questions
تعریفg (x) = x −(−۱)xوf (x) = (−۱)x h
x+۱
۲
i
با دامنه اعداد طبیعی به صورتgوfتوابع
( کدام است؟ )] [، نماد جزء صحیح است.(go f )−۱(۱۰۱) −(go (−f ))−۱(۱۰۲)شدهاند. حاصل
(. صفر۱)
۱ .(۲)
۲ .(۳)
۳ .(۴)
The functions f and g are defined on the domain of natural numbers as follows:
f (x) = (−1)x  x+1
2

and g, (x) = x, −(−1)x. What is the result of (go f )−1(101) −
(go, (−f ))−1(102)? ([ ] denotes the floor function).
1. zero
2. 1
3. 2
4. 3
Hard
Trap:-
USS
Mathematics
۲) 1
GPT-4
۲) 1
GPT3.5
<pad> ۱)</s>
Aya
۲) 1<|endoftext|>
Xverse
34

--- Page 35 ---

Preprint. Under review.
عبارت≫ما تمایل داریم اشیای ناقص را بهصورت کامل ببینیم≪، به کدام اصل از اصول گشتالت اشاره
میکند؟
(. مشابهت۱)
(. تکمیل۲)
(. استمرار۳)
(. مجاورت۴)
The phrase “We tend to perceive incomplete objects as complete" refers to which principle of
Gestalt principles?
1. Similarity
2. Closure
3. Continuity
4. Proximity
Easy
Trap: -
USS
Psychology
( تکمیل۲
GPT-4
( تکمیل۲
GPT3.5
<pad> ۲)</s>
Aya
تکمیل۲)<|endoftext|>
Xverse
35

--- Page 36 ---

Preprint. Under review.
گشایش جاده موسوم به ابریشم، هم زمان با حکومت کدام سلسله ها در چین و ایران بود؟
ساسانی-(. چه این۱)
اشکانی-(. چه این۲)
ساسانی-(. هان۳)
اشکانی-(. هان۴)
The opening of the Silk Road coincided with the rule of which dynasties in China and Iran?
1. Chen - Sasanian
2. Chen - Parthian
3. Han - Sasanian
4. Han - Parthian
Medium
Trap:-
USS
History
اشکانی-( هان۴
GPT-4
ساسانی-( هان۳
GPT3.5
<pad> ۲)</s>
Aya
...<|endoftext|>
Xverse
36

--- Page 37 ---

Preprint. Under review.
یک کاال طی سه مرحله تولید و در نهایت به مشتری فروخته میشود. اگر در مرحله آخر )سوم( قیمت
تومان باشد و اعتبار مالیات بر ارزش افزودههایی که در مرحله قبل پرداخت شده۱۲,۵۰۰کاال برابر با
تومان باشد، آنگاه:۵۵۰برابر با
)الف( قیمت فروش کاال با مالیات بر ارزش افزوده در مرحله سوم چند تومان است ؟
)ب( قیمت فروش کاال با مالیات بر ارزش افزوده در مرحله دوم چند تومان است؟
)ج( مجموع مالیات بر ارزش افزوده جمعآوری شده چند تومان است؟ )نرخ مالیات بر ارزش
درصد است.(۵افزوده
۸۷۵ (، ج۱۰,۵۰۰ (، ب۱۳,۱۲۵ ((. الف۱)
۸۷۵ (، ج۱۱,۵۵۰ (، ب۱۳,۹۸۱ ((. الف۲)
۶۲۵ (، ج۱۱,۵۵۰ (، ب۱۳,۱۲۵ ((. الف۳)
۶۲۵ (، ج۱۰,۵۰۰ (، ب۱۳,۹۸۱ ((. الف۴)
A product goes through three stages of production and is ultimately sold to the customer. If the
price of the product in the final (third) stage is 12, 500 Tomans and the credit for the value-added
taxes paid in the previous stage is 550 Tomans, then:
(a) What is the selling price of the product with value-added tax in the third stage?
(b) What is the selling price of the product with value-added tax in the second stage?
(c) What is the total value-added tax collected?
1. (a)13, 125, (b)10, 500, (c)875
2. (a)13, 981, (b)11, 550, (c)875
3. (a)13, 125, (b)11, 550, (c)625
4. (a)13, 981, (b)10, 500, (c)625
Hard
Trap:-
USS
Economy
،13, 125 (( الف۱گزینه
875 (، ج10, 500 (ب
GPT-4
،13, 125 (( الف۳
625 (، ج11, 550 (ب
GPT3.5
<pad>.صحیح است۲/< گزینهs>
Aya
I) a) 13, 125, b) 10, 500,
c) 875 <|endoftext|>
Xverse
37

--- Page 38 ---

Preprint. Under review.
:معلمی وارد کالس پنجنفره شد و از دانشآموزان پرسید چند نفر دیروز ورزش کردند. اولی گفت
≫چهار نفر از ما≪، دومی گفت:≫سه نفر از ما≪، سومی گفت:≫دو نفر از ما≪، چهارمی گفت:≫یک نفر
از ما≪ و پنجمی گفت:≫هیچکدام از ما≪. معلم میدانست کسانی که ورزش کردهاند راست و کسانی
که ورزش نکردهاند، دروغ میگویند. چند نفر ورزش کردهاند؟
(. یک نفر۱)
(. دو نفر۲)
(. سه نفر۳)
.(. کسی ورزش نکرده است۴)
A teacher entered a class of five students and asked how many of them had exercised yesterday.
The first student said, "Four of us," the second said, "Three of us," the third said, "Two of us,"
the fourth said, "One of us," and the fifth said, "None of us." The teacher knew that those who
had exercised were telling the truth, while those who hadn’t were lying. How many students had
exercised?
1. One student
2. Two students
3. Three students
4. No student has exercised
Hard
Trap: 4
LSS
Analytical Talent
( یک نفر۱
GPT-4
( سه نفر۳
GPT3.5
<pad> ۳)</s>
Aya
.................................
.................................
.................................
Xverse
38

--- Page 39 ---

Preprint. Under review.
عبارات زیر بهترتیب مصادیق کدام موارد هستند؟
کنش ناظر به دیگران-
گوش دادن آهنگ در اتوبوس بدون توجه به سایر مسافران-
احترام به سالمندان-
ارزش اجتماعی-کنش فردی-(. کنش اجتماعی۱)
هنجار اجتماعی-کنش فردی-(. کنش اجتماعی۲)
هنجار اجتماعی-کنش درونی-(. کنش فردی۳)
ارزش اجتماعی-کنش درونی-(. کنش فردی۴)
The following phrases correspond to which of the following scenarios?
• Observing others’ actions
• Listening to music on the bus without regard to other passengers
• Respecting the elderly
1. Social action - Individual action - Social value
2. Social action - Individual action - Social norm
3. Individual action - Intrinsic action - Social norm
4. Individual action - Intrinsic action - Social value
Easy
Trap: -
USS
Sociology
کنش-( کنش اجتماعی۲
هنجار اجتماعی-فردی
GPT-4
کنش-( کنش اجتماعی۲
هنجار اجتماعی-فردی
GPT3.5
<pad> ۱)</s>
Aya
کنش فردی-( کنش اجتماعی۲
هنجار اجتماعی-<|endoftext|>
Xverse
39

--- Page 40 ---

Preprint. Under review.
کدام بیت مبالغه دارد؟
(. حافظا چون غم و شادی جهان در گذر است / بهتر آن است که من خاطر خود خوش دارم۱)
(. در کوی نیکنامی ما را گذر ندادند / گر تو نمیپسندی تغییر کن قضا را۲)
(. روز وصل دوستداران یاد باد / یاد باد آن روزگاران یاد باد۳)
(. خواهم از گریه دهم خانه به سیالب امشب / دوستان را خبر از چشم پرآبم مکنید۴)
Which verse has Hyperbole?
1. O Hafiz, since the world is passing through sorrow and joy, / It is better that I keep my
heart content.
2. They did not let us pass through the alley of good reputation / If you don’t like it,
change your destiny.
3. May the day of reunion with beloved friends be remembered / Remember the days of
old.
4. Tonight, I cry so much that it seems as if a flood has come into the house / Do not tell
my friends that my eyes are full of tears.
Easy
Trap: -
UPS
Persian Language and Literature
( خواهم از گریه دهم۴گزینه
خانه به سیالب امشب / دوستان
را خبر از چشم پرآبم مکنید
GPT-4
( خواهم از گریه دهم خانه۴
به سیالب امشب / دوستان
را خبر از چشم پرآبم مکنید
GPT3.5
<pad>.مبالغه دارد۴/< گزینهs>
Aya
( در کوی نیکنامی ما را گذر۲
ندادند / گر تو نمیپسندی
|<تغییر کن قضا راendoftext|>
Xverse
40

--- Page 41 ---

Preprint. Under review.
در کدام مورد به ویژگی آبهای فسیلی اشاره دارد؟
(. آبی است که پس از مصرف انسان از طریق چرخه آب جایگزین میشود.۱)
(. الیههای آبدار موجود در رسوبات رودخانهای و آبرفتی۲)
.(. در اعماق زیاد محبوس شدهاند و در چرخه آب قرار ندارند۳)
.(. آبهایی که عموماً دارای امالح فراوان هستند۴)
Which case refers to the characteristics of fossil waters?
1. It is the water that is replaced through the water cycle after human consumption.
2. The water-rich layers found in river and groundwater sediments.
3. They are trapped deep and do not participate in the water cycle.
4. Waters that generally have abundant salts.
Medium
Trap:-
USS
Geology
( در اعماق زیاد محبوس۳گزینه
شدهاند و در چرخه آب قرار ندارند.
GPT-4
( در اعماق زیاد محبوس شدهاند۳
.و در چرخه آب قرار ندارند
GPT3.5
<pad>(۳ </s>
Aya
( الیههای آبدار موجود در رسوبات۲
|<رودخانهای و آبرفتیendoftext|>
Xverse
41

--- Page 42 ---

Preprint. Under review.
چند مورد، درباره یاختههای شرکتکننده در انعکاس عقب کشیدن دست فرد در برخورد با جسم
داغ، درست است؟
هر یاخته عصبی که پیام گیرنده درد را منتقل میکند، به بخش حرکتی دستگاه عصبی-
.محیطی اختصاص دارد
بخشی از یاختههای عصبی که به عصب نخاعی تعلق دارند، با یاختههای چندهستهای، ارتباط-
.ویژهای برقرار میکنند
هر یاخته عصبی که با عضله ناحیه بازو همایه )سیناپس( برقرار میکند، تغییری در پتانسیل-
.الکتریکی آن رخ داده است
بعضی از یاختههای عصبی که جسم یاختهای آنها در ماده خاکتسری قرار دارد، با یاختههای-
.عصبی حسی همایه )سیناپس( برقرار میکنند
(. یک۱)
(. دو۲)
(. سه۳)
(. چهار۴)
How many statements about the neurons involved in the withdrawal reflex of the hand when
encountering a hot object are correct?
- Each sensory neuron that transmits pain signals has a specific connection to the motor
part of the peripheral nervous system.
- Some of the nerve fibers belonging to the spinal nerve establish a special connection
with the multiple nerve fibers.
- Any sensory neuron that synapses with the muscle of the forearm changes its electrical
potential.
- Some of the nerve fibers whose cell bodies are located in the dorsal root ganglion
synapse with sensory nerve fibers.
1. One
2. Two
3. Three
4. Four
Hard
Trap: -
USS
Biology
( چهار۴
GPT-4
(اشتباه است۴و۲ ،۱( سه )گزینه۳
GPT3.5
<pad>(۲ </s>
Aya
؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟
؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟
؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟
Xverse
42

--- Page 43 ---

Preprint. Under review.
، رقم یکان با یکان هزار، دهگان با دهگان هزار و صدگان با صدگان هزار، جابه جا۱۹۵۴۸۳در عدد
میشوند مجموع دو رقم صدگان و هزارگان در عدد جدید، چند است؟
۹ .(۱)
۵ .(۲)
۸ .(۳)
۴ .(۴)
In the number 195483, the units digit swaps places with the thousands digit, the tens digit swaps
places with the tens of thousands digit, and the hundreds digit swaps places with the hundreds
of thousands digit. What is the sum of the two new digits in the hundreds and thousands places
in the new number?
1. 9
2. 8
3. 5
4. 4
Hard
Trap:-
LPS
Mathematics
1) 9
GPT-4
۳) 8
GPT3.5
<pad>(۳ </s>
Aya
۸<|endoftext|>
Xverse
43

--- Page 44 ---

Preprint. Under review.
(.است۶۲چند مورد از مطالب زیر درست است؟ )عدد اتمی آهن برابر
)آ( کاتیون سازنده نمک بهدست آمده از واکنش زنگ آهن با هیدروکلریکاسید، در آرایش
الکترونی خود یک زیرالیه نیمهپر دارد.
)ب( تفاوت شمار پیوندهای کوواالنسی در ششمین عضو خانواده آلکینها و ششمین عضو خانواده
است.۲آلکانها برابر با
≪SF۴ + ۲H۲O →SO۲ + ۴HF ≫در واکنشHFسرعت متوسط تولید
)پ(
است.mol.s−۱برحسبSF۴برابر سرعت متوسط مصرف۵۱ ،mol.min−۱.L−۱برحسب
است.(۱۶L)حجم ظرف واکنش برابر
متعلق به دستهای از مواد است که در صنعت الکترونیک کاربرد فراوانی دارند.۳۲Ge)ت( عنصر
۱ .(۱)
۲ .(۲)
۳ .(۳)
۴ .(۴)
How many of the following statements are correct? (The atomic number of iron is 26.)
(a) The constituent cation of the salt obtained from the reaction of iron with hydrochloric
acid has a half-filled sublayer in its electron configuration.
(b) The difference in the number of covalent bonds in the sixth member of the alkynes
family and the sixth member of the alkanes family is equal to 2.
(c) The average rate of production of HF in the reaction ≪SF4 + 2H2O →SO2 +
4HF ≫in terms of mol.min−1.L−1 is 15 times the average rate of consumption of
SF4 in terms of mol.s−1. (The volume of the reaction vessel is 16L.)
(d) Element 32Ge belongs to a category of substances that are widely used in the electronics
industry.
1. 1
2. 2
3. 3
4. 4
Hard
Trap: 1
USS
Chemistry
۲) 2
GPT-4
۳) 3 ()آ، ت، پ
GPT3.5
<pad>(۲ </s>
Aya
۲<|endoftext|>
Xverse
44

--- Page 45 ---

Preprint. Under review.
:طبق نظریه اخالقی افالطون، انسان نیکبخت کسی است که
(. از میان قوای خود، تنها به قوه عقل که عالیترین قوه است، توجه کند.۱)
.(. به چهار فضیلت حکمت، خویشتنداری، شجاعت و عدالت آراسته گردد۲)
.(. از امیال و افعال طبیعی دوری کرده و یکسره به انجام فضیلتها بپردازد۳)
.(. عقل او در مقابل قوای شهوت و غضب ایستادگی کرده و اداره بدن را بهعهده بگیرد۴)
According to Plato’s ethical theory, a fortunate person is one who:
1. Focuses only on the power of reason, which is the highest faculty, among their faculties.
2. Embodies the four virtues of wisdom, self-discipline, courage, and justice.
3. Avoids natural desires and actions and solely engages in virtuous deeds.
4. Their reason stands firm against the forces of lust and anger, taking charge of managing
the body.
Hard
Trap: -
USS
Philosophy
( به چهار فضیلت۲گزینه
حکمت، خویشتنداری،
شجاعت و عدالت آراسته گردد.
GPT-4
،( به چهار فضیلت حکمت۲
خویشتنداری، شجاعت
و عدالت آراسته گردد.
GPT3.5
<pad>(۲ </s>
Aya
( از امیال و افعال طبیعی۳
دوری کرده و یکسره به انجام
|<فضیلتها بپردازد.endoftext|>
Xverse
45

--- Page 46 ---

Preprint. Under review.
| هستند و درq۲| > q۱وq۱ > ۰دو کره فلزی خیلی کوچک و مشابه دارای بار الکتریکی ناهمنام
وارد میکنند. اگر کرهها را به هم۰/۹ Nسانتیمتری هم قرار دارند و بر هم نیروی الکتریکی۶۰فاصله
نیوتون به هم وارد۱/۶تماس دهیم و دوباره به همان فاصله قبلی از هم دور کنیم، نیروی الکتریکی
(k = ۹ × ۱۰۹ N.m۲
C۲ )چند میکروکولن است؟q۱.میکنند
۱ .(۱)
۲ .(۲)
۰۱ .(۳)
۰۲ .(۴)
Two very small and similar metallic spheres with unlike electric charges q1 > 0 and |q2| > |q1|
are placed 60 centimeters apart and exert an electric force of 0.9, N on each other. If we bring
the spheres into contact and then separate them again to the same previous distance, they exert a
force of 1.6, N on each other. What is the value of q1 in microcoulombs? (k = 9 × 109 N·m2
C2 )
1. 1
2. 2
3. 10
4. 20
Hard
Trap:-
USS
Physics
(۲گزینه2
GPT-4
۳) 10
GPT3.5
<pad>(۲ </s>
Aya
3 q1 =
3q2−4q2
r
=
5
60 · 9·109
60
=
3
8 · 3·107
2
=
7.5 × 106
Assistant: Qtotal
=
Q1 + Q2
=
1
4πr2
[q1 cos θ + q2 cos 2θ]
Qtotal
=
1
4πr2
h
q1 +
p
q12 + q22 −2q1q2 cos θ
i
Fe
=
1
4πr2
[q1 cos θ + q2 cos 2θ]
h
q1 +
p
q12 + q22 −2q1q2 cos θ
i
Fe
=
1
4πr2
h
q1 +
p
q12 + q22 −2q1q2 cos θ
i
...
Xverse
46

--- Page 47 ---

Preprint. Under review.
استدالل≫هر کالغی سیاه است، زیرا تا به حال نشنیده و ندیدهایم که کالغی به رنگ دیگر باشد≪ یک
استدالل . . . است که در آن از . . . نتیجهگیری . . . شده است.
کلی-موارد جزئی-(. استقرای تعمیمی۱)
جزئی-موارد کلی-(. استقرای تعمیمی۲)
کلی-مقدمات جزئی-(. استدالل قیاسی۳)
جزئی-مقدمات کلی-(. استدالل قیاسی۴)
The argument "Every crow is black because we have never heard or seen a crow of any other
color" is a ... argument, where a ... conclusion is drawn from the ....
1. Inductive generalization - particular instances - general cases
2. Inductive generalization - general instances - particular cases
3. deductive reasoning - specific premises - general cases
4. deductive reasoning - general premises - particular cases
Hard
Trap: -
USS
Logic
( استقرای تعمیمی۱گزینه
کلی-موارد جزئی-
GPT-4
( استقرای تعمیمی۲
جزئی-موارد کلی-
GPT3.5
<pad>(۲ </s>
Aya
موارد-( استقرای تعمیمی۲
جزئی-|<کلیendoftext|>
Xverse
47

--- Page 48 ---

Preprint. Under review.
با توجه به الگوی زیر، بهجای عالمت سوال، کدام عدد قرار میگیرد؟
۴۹
۴
۲۸
۳۶
۵
۳۰
۶۴
۵
?
۴۴ .(۱)
۴۸ .(۲)
۴۲ .(۳)
۴۰ .(۴)
According to the pattern below, which number would be placed instead of the question mark?
49
4
28
36
5
30
64
5
?
1. 44
2. 48
3. 42
4. 40
Hard
Trap: 2,3
UPS
Mathematical and Logical Intelligence
۴) 40
GPT-4
۲)48
GPT3.5
<pad>(۲ </s>
Aya
۲)48<|endoftext|>
Xverse
48

--- Page 49 ---

Preprint. Under review.
.در تمام گزینهها بهجز .......... رابطهی میان هر دو جفت واژه یکسان است
(. کشتی و اتومبیل / شنا و پیادهروی۱)
(. دستاورد علمی و تحقیق / گنج و رنج۲)
(. جلسه و گفتوگو / مدرسه و آموزش۳)
(. سهشنبه و هفته / سرما و زمستان۴)
In all options except .......... the relationship between both pairs of words is the same.
1. Boats and Cars / Swimming and Walking
2. Scientific achievement and Research / Treasure and Pain
3. Meeting and Discussion / School and Education
4. Tuesday and Week / Cold and Winter
Hard
Trap: 1
UPS
Verbal and Linguistic Intelligence
( دستاورد علمی۲گزینه
و تحقیق / گنج و رنج
GPT-4
( سهشنبه و هفته / سرما و زمستان۴
GPT3.5
<pad>( جلسه و گفت وگو۳گزینه
/ مدرسه و آموزش رابطه ی میان
/<هر دو جفت واژه یکسان است.s>
Aya
( دستاورد علمی و تحقیق۲
|</ گنج و رنجendoftext|>
Xverse
49

```
