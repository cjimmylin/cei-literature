---
title: "2025-Park-Ko-MuSR A Multistep Soft Reasoning Benchmark for LLMs Capable of - PDF Extract"
source_pdf: "2025-Park-Ko-MuSR A Multistep Soft Reasoning Benchmark for LLMs Capable of.pdf"
pages: 102
extracted_at: "2026-02-13T09:50:29.930181"
---

# PDF Extract: 2025-Park-Ko-MuSR A Multistep Soft Reasoning Benchmark for LLMs Capable of

**Source PDF:** 2025-Park-Ko-MuSR A Multistep Soft Reasoning Benchmark for LLMs Capable of.pdf
**Total Pages:** 102

---

## Content

```
--- Page 1 ---

Ko-MuSR: A Multistep Soft Reasoning Benchmark
for LLMs Capable of Understanding Korean
Chanwoo Park*
99chanwoo@snu.ac.kr
Suyoung Park†
itforspark@snu.ac.kr
JiA Kang†
jia6776@snu.ac.kr
Jongyeon Park†
iscopark67@snu.ac.kr
Sangho Kim†
ksh4931@snu.ac.kr
Hyunji M. Park†
mhj233@snu.ac.kr
Sumin Bae*
dt2085@snu.ac.kr
Mingyu Kang*
ahagyue@snu.ac.kr
Jaejin Lee*†
jaejin@snu.ac.kr
Abstract
We present Ko-MuSR, the first benchmark to
comprehensively evaluate multistep soft rea-
soning in long Korean narratives while min-
imizing data contamination. Built following
MuSR (Sprague et al., 2024), Ko-MuSR fea-
tures fully Korean narratives, reasoning chains,
and multiple-choice questions verified by hu-
man annotators for logical consistency and an-
swerability. Evaluations of four large language
models—two multilingual and two Korean-
specialized—show that multilingual models
outperform Korean-focused ones even in Ko-
rean reasoning tasks, indicating cross-lingual
generalization of reasoning ability. Carefully
designed prompting strategies, which combine
few-shot examples, reasoning traces, and task-
specific hints, further boost accuracy, approach-
ing human-level performance. Ko-MuSR of-
fers a solid foundation for advancing Korean
NLP by enabling systematic evaluation of long-
context reasoning and prompting strategies. 1
1
Introduction
The development of multilingual artificial intel-
ligence (AI) is becoming increasingly important
as large language models (LLMs) expand beyond
applications centered on English. Since most of
the world’s population lives outside the English-
speaking realm, there is a significant need for
models that cater to diverse linguistic communi-
ties. This need has led to the emergence of mul-
tilingual LLMs (Lin et al., 2022; OpenAI, 2024a;
Yang et al., 2025), which demonstrate strong per-
formance across both high- and low-resource lan-
guages. Simultaneously, countries like South Korea
and France are investing in models (NAVER Cloud
HyperCLOVA X Team, 2025; LG AI Research,
*Dept. of Computer Science, Seoul National University
†Graduate School of Data Science, Seoul National Univer-
sity
1Our code can be found at https://github.com/mcrl/Ko-
MuSR
2025; Mistral-AI et al., 2025) tailored to specific
languages to enhance their competitiveness in the
AI ecosystem.
To evaluate these models, multilingual bench-
marks, such as XNLI (Conneau et al., 2018),
XCOPA (Ponti et al., 2020), and MMMLU (Ope-
nAI, 2024b), have been created. There is a need
for benchmarks specifically assessing Korean, and
efforts to develop them are currently underway.
However, in comparison to English, the variety of
Korean benchmarks is still limited, and the abil-
ity to generalize task performance across different
languages is not yet fully understood.
Current Korean benchmarks inadequately evalu-
ate multistep reasoning outside of coding, STEM
fields, or mathematics. There is a notable absence
of tasks that require long-context reading, infor-
mation extraction, and multi-hop reasoning. While
CSAT-QA can address this gap, it is vulnerable
to data contamination during the critical training
stages of LLMs because it is based on the Korean
College Scholastic Ability Test (CSAT), which is
publicly accessible and widely used in Korea. Addi-
tionally, although HRMCR (HAE-RAE Multi-Step
Commonsense Reasoning) (Son et al., 2025a) fo-
cuses on soft reasoning, it does not fully cover
long-context comprehension.
Motivated by the limitations of existing Ko-
rean benchmarks, we propose Ko-MuSR, a Korean
benchmark for multistep soft reasoning. Drawing
inspiration from the MuSR benchmark (Sprague
et al., 2024), Ko-MuSR constructs logically coher-
ent passages and questions without contamination.
Human annotators carefully reviewed and evalu-
ated the tasks to ensure that the answers could
be reliably derived from the provided passages,
thereby validating the design of the benchmark.
We evaluated Ko-MuSR using two multilingual
LLMs and two LLMs specialized in Korean. Sur-
prisingly, our experiments show that the specialized
models underperformed compared to the multilin-
1
arXiv:2510.24150v1  [cs.CL]  28 Oct 2025

--- Page 2 ---

gual ones in Korean reasoning tasks. This suggests
that the capability for multistep reasoning can trans-
fer across languages, especially between English
and Korean. This finding highlights the necessity
of improving specialized models to reach the same
level of performance as their multilingual coun-
terparts. Additionally, we demonstrate that care-
fully designed in-context learning strategies can
significantly enhance model accuracy, thereby re-
ducing the performance gap. We also find that in-
context learning strategies produce inconsistent ef-
fects among smaller language models (SLMs), as
demonstrated in our evaluation of five additional
SLMs.
The main contributions of this paper are summa-
rized as follows:
• We introduce Ko-MuSR, the first benchmark
specifically designed for long-context multi-
step soft reasoning in Korean, ensuring it is
free from contamination. All benchmark items
have been reviewed and solved by human par-
ticipants, which confirms their answerability
and logical consistency.
• Our evaluations of multilingual and Korean-
specialized models reveal unexpected gaps in
reasoning performance for Korean. We also
provide evidence of reasoning transfer be-
tween English and Korean.
• We discover that models can significantly ben-
efit from carefully crafted in-context learning
examples, with some even surpassing human
performance in a particular subtask.
2
Related Work
Multilingual LLMs.
A variety of multilingual
LLMs have been developed to address the needs
of non-English speakers around the globe. Early
models, such as Multilingual BERT (mBERT) (De-
vlin et al., 2019) and XLM (Lample and Conneau,
2019), have evolved into more advanced models
like LLaMA4 (Meta, 2025) and Qwen3 (Yang et al.,
2025), which explicitly incorporate multilingual ca-
pabilities into their architectures to better serve a
global audience. These models are trained on tril-
lions of tokens gathered from the internet, repre-
senting a wide range of linguistic sources. With
over 30 trillion tokens in their training datasets,
recent multilingual LLMs show impressive perfor-
mance on multilingual benchmarks, such as Multi-
lingual Massive Multitask Language Understand-
ing (MMMLU) (OpenAI, 2024b) and Multilingual
Grade School Math (MGSM) (Shi et al., 2022),
often matching or even exceeding the capabilities
of specialized models that focus on individual lan-
guages.
Language-specialized LLMs.
There has been a
growing focus on developing bilingual or language-
specialized models to enhance regional AI compet-
itiveness. Examples of these models include Crois-
santLLM (Faysse et al., 2025), Magistral (Mistral-
AI et al., 2025), Exaone 4.0 (LG AI Research,
2025), and HyperCLOVA X SEED Think (NAVER
Cloud HyperCLOVA X Team, 2025). Despite be-
ing created with relatively limited computational
resources, these models achieve competitive, and
in some cases superior, performance in their tar-
get languages through careful data curation and
optimization for specific domains.
Generalization
across
different
languages.
Multilingual LLMs are becoming increasingly pop-
ular because their performance on multilingual
benchmarks often exceeds that of language-specific
models. For instance, GPT-4 (OpenAI, 2024a)
demonstrates significant improvements over GPT-
3.5 (Brown et al., 2020) on the MMMLU bench-
mark across 25 languages, showcasing its strong
ability to generalize across different languages.
Similarly, state-of-the-art open-parameter models
like LLaMA 4 and Qwen 3 achieve high scores
(above 80) on the same benchmark. Even in Korean
soft reasoning tasks, such as HRMCR, a multistep
reasoning benchmark with short contexts, these
multilingual LLMs often outperform counterparts
that are specialized for the Korean language.
Discrepancy across different languages.
De-
spite advancements in multilingual model training,
reasoning capabilities across different languages
continue to be a significant challenge. GPT-4 in-
dicates that performance on the MMMLU bench-
mark varies greatly by language, often declining
in low-resource settings. Similarly, evaluations of
PaLM (Chowdhery et al., 2022) on the Mathemati-
cal Generalization and Solution Method (MGSM)
tasks show considerable degradation when prob-
lems are presented in low-resource languages.
Benchmarks for Korean LLMs.
Although vari-
ous benchmarks have been developed to evaluate
Korean-capable LLMs, there is still a significant
gap in the diversity and maturity of these bench-
2

--- Page 3 ---

1. Sample Background
Names
3. Generate a Narrative
2. Expanda Reasoning Tree
John
Sarah
Anthony
Gilbert
…
Locations
Maze
School
Cinema
Office
…
Tools
Air Gun
Knife
Hammer
Poison
…
…
Victim: Gilbert
Location: In the maze
Murder Weapon: Small Hammer
Murderer: John
Motive: To stop Gilbert from 
exposing evidences of his 
corruption
Refer the story background, 
and expand a section of logic 
tree
> John has a motive, because
>> Fact from Story
>> Fact from Story
>> Commonsense Knowledge
> John has a motive
>> Gilbert had an evidence 
that adduces John’s guilt | Fact 
from Story
>> Gilbert was investigating 
John’s corruption | Fact from 
Story
>> Investigators might find 
critical evidence of guilt | 
Commonsense Knowledge
Build a story that includes all 
of following facts
- Gilbert had an evidence that 
adduces John’s guilt
- Gilbert was investigating 
John’s corruption.
- (Continues…)
(…) Detective Winston 
observed John’s responses 
during the interrogation, 
seeking more evidence. He 
noted that Gilbert had been 
investigating John on 
suspicion of embezzling 
company assets. (…)
Sampled Story Background
Figure 1: Illustration of the MuSR synthesis process.
marks compared to those available for English mod-
els.
KoBEST (Jang et al., 2022), KMMLU (Son
et al., 2025b), and Ko-H5 (Park et al., 2024)
have played pioneering roles in evaluating Korean
LLMs; however, they do not evaluate reasoning
in long-context situations. Benchmarks that focus
on generative capabilities, such as LogicKor (Park,
2024) and KoMT-Bench (LG AI Research, 2024b),
depend on LLM-based judges, which means their
evaluations are influenced by the choice of evalua-
tor models.
For domain-specific reasoning tasks, HRM8k
(Ko et al., 2025) and KR-Humaneval (Kang and
Kim, 2024) provide benchmarks for mathemat-
ics and coding, respectively, but they do not as-
sess natural language reasoning skills. Additionally,
multiple-choice benchmarks like HAE-RAE (Son
et al., 2024) include questions that require local
information but fail to evaluate long-context under-
standing.
Recent efforts in creating benchmarks for
multistep soft reasoning in Korean include
HRMCR (Son et al., 2025a), which offers tasks
with contexts limited to fewer than 500 charac-
ters and lacks a natural narrative structure. CSAT-
QA (Son et al., 2023) provides long-context reason-
ing questions based on the Korean national univer-
sity entrance exam. However, its public availability
and the use of exam materials as training data raise
concerns about potential data contamination. Simi-
larly, CLIcK (Kim et al., 2024), which contains a
subset of CSAT-QA, faces the same issue.
Despite the increasing demand for evaluating
Korean models on multistep reasoning involving
long narratives, there are few suitable benchmarks
available, and the existing ones are susceptible to
contamination. To address this gap, we have de-
veloped a Korean benchmark for multistep soft
reasoning that features long, natural narratives and
minimizes the risk of overlap with training data. It
is designed to test models’ culturally grounded in-
terpretation, rather than simple linguistic accuracy.
3
MuSR
MuSR (Sprague et al., 2024) is a benchmark cre-
ated to assess the capability of language models to
perform multi-step reasoning within English nar-
ratives. Each instance includes a narrative, a ques-
tion, and multiple-choice answers, with narrative
lengths varying from 500 to 1,000 words. Models
are required to extract relevant facts, apply logical
reasoning, and deduce the correct answer.
The benchmark consists of three subtasks: mur-
der mysteries, object placements, and team alloca-
tions.
In the murder mysteries subtask, two suspects
are presented, one of whom is the murderer. The
narrative provides information about the "means,"
3

--- Page 4 ---

"motive," and "opportunity" of the guilty suspect,
while the innocent suspect lacks at least one of
these elements. The question posed is to determine
which of the two characters is most likely to be
guilty.
In the object placements subtask, the narrative
outlines the locations of objects and the beliefs
of characters regarding these locations. The ques-
tion asks where a specific character believes an
object is situated. To answer this question correctly,
one must consider which characters witnessed each
movement of the objects. Each narrative includes
two objects and describes three movements, along
with information about whether each of the three
characters observed these movements. If a charac-
ter did not witness a movement, they will continue
to believe that the object remains in its original
position.
In the team allocations subtask, the narrative de-
scribes the individual skills of three characters and
their relationships within the team. The objective
is to assign one character to a solo task while the
other two work collaboratively on a different task.
This involves determining the best team compo-
sition based on both individual abilities and the
compatibility between team members.
Synthesis.
As shown in Figure 1, the synthesis of
MuSR occurs in three stages: sampling, reasoning
tree expansion, and narrative generation.
1. Sampling stage: In this initial stage, story
backgrounds are sampled from various do-
main seeds, such as crime scenes, character
names, or object types.
2. Reasoning tree expansion stage: In this stage,
LLMs enhance the structure by adding fact
and deduction nodes.
3. Narrative generation stage: Finally, LLMs
generate coherent stories that are aligned with
the reasoning tree, relying solely on the fact
nodes.
Evaluation.
For evaluation purposes, the bench-
mark recommends the 1-Shot CoT+ configuration.
In this setting, a model is given one example ques-
tion, along with its reasoning process and the final
answer. Each question also includes a hint, which
provides a detailed description of the reasoning
strategy specific to that subtask.
Human participants achieve average accuracies
between 90% and 95% under this 1-Shot CoT+ set-
ting, indicating that the benchmark is easily solv-
able by human individuals with multi-step reason-
ing abilities.
4
Constructing Ko-MuSR
Similar to the MuSR synthesis process, our synthe-
sis pipeline consists of three stages: (i) sampling a
problem instance, (ii) constructing a reasoning tree,
and (iii) generating a narrative based on the reason-
ing tree. We use two LLMs from OpenAI (GPT-4o
and o1)2 for the synthesis. Human annotators are
then tasked with solving each question to verify
that the correct answer can indeed be inferred from
the corresponding narrative. Finally, we recruit in-
dependent participants with no prior exposure to
the dataset to ensure that each instance is solvable
by humans. These steps ensure that all instances
are valid and free from trivial or unsolvable cases.
4.1
Modifications of the MuSR Synthesis
We have adapted the MuSR pipeline to create Ko-
MuSR, focusing on high-quality narratives in Ko-
rean. All prompts have been translated into Ko-
rean. For domain seeds related to object placement
and team allocation subtasks, we generate Korean-
specific seeds using GPT-4o. For murder mysteries,
we create culturally appropriate character names in
Korean with GPT-4o. Additionally, other domain
seeds, such as crime scenes, are translated and ad-
justed as needed to ensure they fit naturally within
the Korean context and culture. This process en-
sures that domain seeds remain faithful to MuSR
while producing culturally coherent settings.
We also translate all prompts for the reasoning
tree and narrative generation into Korean to ensure
that the logical structure is expressed in Korean.
This prevents the inclusion of keywords that could
trivialize deduction in the reasoning tree and, con-
sequently, in the narrative.
For reasoning tree expansion and narrative syn-
thesis, we use GPT-4o for the murder mystery and
team allocation subtasks. However, for object place-
ment, the outputs from GPT-4o did not meet our
quality standards, so we opted to use o1, which
produced higher-quality instances.
4.2
Reviewing the Intermediate Dataset
All synthesized problems were initially reviewed
by the authors, who acted as annotators. Each an-
notator received one example and a translated hint
2https://openai.com
4

--- Page 5 ---

Statistics
Murder
Mysteries
Object
Placements
Team
Allocations
# Questions
31
40
38
Max
93.5
97.5
92.1
Average
85.5
93.8
87.5
Median
83.9
97.5
86.8
Min
77.4
85.0
81.6
Table 1: Human evaluation result of Ko-MuSR.
from MuSR to ensure consistency with the original
benchmark design. The review process consisted
of two phases.
In the first phase, each annotator independently
solved every problem, submitted their answer, and
categorized the instance as either pass, minor issue,
or fail. Instances labeled as pass were accepted
only if the annotator’s answer matched the correct
solution. Those marked as fail were discarded.
In the second phase, any instance labeled as mi-
nor issue or incorrectly marked as pass was re-
evaluated by two independent annotators. These
secondary annotators were given the supposed cor-
rect answer and asked to verify whether it could
be logically derived from the provided narrative.
An instance was included in the final dataset only
if both annotators deemed it as pass; otherwise, it
was excluded.
4.3
Human Evaluation
To further validate the quality of our dataset, we
sampled a subset of questions and recruited five
external participants, ages 20 to 30, who were not
affiliated with our research group. They were pro-
vided with one example and a hint to assist them in
answering the questions. The questionnaire was ad-
ministered on a laptop with internet access disabled
to prevent participants from using AI tools, thus
eliminating any potential influence of such tools
on human benchmark performance. This process
allowed us to measure both human performance
and the effectiveness of our validation procedure.
Table 1 presents the human performance results
on Ko-MuSR. This ensures the validity of our re-
view process and provides a measure of human
performance on Ko-MuSR.
4.4
Dataset Statistics
Ko-MuSR consists of three subtasks, each contain-
ing 250 examples. Dataset statistics are summa-
rized in Table 2.
Lang.
Statistics
Murder
Mysteries
Object
Placements
Team
Allocations
En
# Questions
250
256
250
Avg. Length (chars)
5471
4919
3104
Avg. Length (words)
905
787
494
Ko
# Questions
250
250
250
Avg. Length (chars)
2373
1049
1091
Avg. Length (words)
561
262
264
Table 2: Statistics of MuSR and Ko-MuSR narratives
across subtasks.
5
Evaluation
5.1
Evaluation Setup
Models.
We evaluate four LLMs with MuSR
and Ko-MuSR: two multilingual models, Qwen3
32B (Yang et al., 2025) and LLaMA 4 Scout In-
struct (Meta, 2025), and two models specialized in
Korean, Exaone 4.0 32B (LG AI Research, 2025)
and HyperCLOVA X SEED Think 14B (NAVER
Cloud HyperCLOVA X Team, 2025). We then eval-
uate 5 SLMs: three multilingual models, QWEN3
0.6B, 1.7B, 4B and two models specialized in Ko-
rean: Exaone 4.0 1.2B and Exaone 3.5 2.4B In-
struct (LG AI Research, 2024a).
Model training.
Qwen3 32B is trained on over
36 trillion tokens in total, including 5 trillion high-
quality, reasoning-oriented tokens during its pre-
training stage. Qwen 3 0.6B, 1.7B, and 4B models
are distilled from Qwen3 32B. LLaMA 4 Scout In-
struct is pretrained on over 30 trillion multimodal
tokens, which encompass text, images, and video,
with at least one billion tokens available for each
language across more than 100 languages. Exaone
4.0 32B is trained on approximately 14 trillion to-
kens, covering English, Korean, and Spanish, with
an emphasis on balancing multilingual reasoning
and linguistic precision. Exaone 4.0 1.2B is trained
on approximately 12 trillion tokens with the same
method as Exaone 4.0 32B. HyperCLOVA X SEED
Think 14B is trained on around 6 trillion tokens
in English and Korean, with a strong focus on
Korean domain adaptation. Exaone 3.5 2.4B has
been trained on approximately 6.5 trillion tokens
in English and Korean, incorporating various data
sources for improved performance in general do-
mains. For evaluation, we use the default gener-
ation configurations provided by the models. All
evaluation experiments are conducted twice, and
we report the average accuracy from the two runs.
Prompts.
In
line
with
the
MuSR
frame-
work (Sprague et al., 2024), we developed multiple
5

--- Page 6 ---

Model
En-MM
En-OP
En-TA
Ko-MM
Ko-OP
Ko-TA
Random
50.0
24.6
33.3
50.0
25.0
33.3
QWEN3 32B
66.4
52.7
73.4
67.6
80.0
79.6
LLaMA 4 Scout Instruct
65.4
54.1
60.4
56.0
67.8
64.2
Exaone 4.0 32B
61.2
55.7
58.8
52.8
37.4
63.2
HyperClova X SEED Think 14B
51.6
38.7
44.0
44.6
41.2
58.6
Human (Avg.)
92.1
90.0
95.1
85.5
93.8
87.5
Table 3: Evaluation result with zero shot, direct, and no hint. Boldface indicates the highest numbers, and underlined
numbers indicate the second highest.
Model
En-MM
En-OP
En-TA
Ko-MM
Ko-OP
Ko-TA
Random
50.0
24.6
33.3
50.0
25.0
33.3
QWEN3 32B
82.4
74.2
88.8
76.0
81.8
89.0
LLaMA 4 Scout Instruct
75.6
68.6
84.2
72.8
83.0
88.0
Exaone 4.0 32B
75.2
72.1
85.8
71.2
71.6
85.8
HyperClova X SEED Think 14B
68.6
66.2
81.0
70.6
50.0
87.8
Human (Avg.)
92.1
90.0
95.1
85.5
93.8
87.5
Table 4: Evaluation result with three shots, CoT, and hints. Boldface indicates the highest numbers, and underlined
numbers indicate the second highest.
Model
En-MM
En-OP
En-TA
Ko-MM
Ko-OP
Ko-TA
HyperClova X SEED Think 14B
51.6
38.7
44.0
44.6
41.2
58.6
+ 1 Shot / Direct / No Hint
63.8
42.0
53.6
50.0
39.0
51.8
+ 3 Shots / Direct / No Hint
67.8
63.7
76.0
65.4
52.4
86.2
+ 3 Shots / Direct / Hint
67.0
64.8
83.8
63.8
49.6
83.8
+ 3 Shots / CoT / Hint
68.6
66.2
81.0
70.6
50.0
87.8
Table 5: Case study of the HyperClova SEEDX Think 14B model with various prompting configurations. The first
row denotes the zero-shot, direct, and no-hint configuration. Boldface indicates the highest numbers, and underlined
numbers indicate the second highest.
En-MM
En-OP
En-TA
Ko-MM
Ko-OP
Ko-TA
QWEN3 0.6B
59.2
52.0
38.8
53.6
28.6
38.0
+ 3 Shots / CoT / Hint
55.4
46.7
33.0
49.0
30.2
33.4
Exaone 4.0 1.2B
55.6
44.7
49.8
48.0
29.0
44.8
+ 3 Shots / CoT / Hint
64.8
44.7
54.8
58.6
31.6
35.8
QWEN3 1.7B
60.6
52.3
59.0
50.0
34.0
63.2
+ 3 Shots / CoT / Hint
66.0
39.6
55.4
63.0
33.0
54.2
Exaone 3.5 2.4B Instruct
51.4
41.6
44.0
51.0
30.0
42.4
+ 3 Shots / CoT / Hint
63.4
48.6
37.2
56.0
41.2
42.8
QWEN3 4B
62.8
55.5
66.0
59.0
51.0
75.4
+ 3 Shots / CoT / Hint
74.0
70.7
85.4
69.8
55.2
79.6
Table 6: Evaluation results with SLMs. The 3-Shot/CoT/Hint configuration may reduce model accuracy in SLMs.
Additional numbers can be found in Appendix B.
prompt variants to assess model performance un-
der various prompting conditions. First, we create
a prompt split that is independent of the test set.
For English, we use one example from the original
MuSR artifact and generate two additional exam-
ples using the same methodology, resulting in three
examples for each subtask. For Korean, we inde-
pendently construct three new prompt examples for
each subtask as well.
We use the Chain-of-Thought (CoT) prompting
6

--- Page 7 ---

strategy (Wei et al., 2022) in our evaluation. For
English, we use one original MuSR CoT example
that includes a question, a step-by-step reasoning
process, and a final answer. We synthesize two ad-
ditional examples using the same methodology. For
Korean, we create three new CoT examples, each
containing complete reasoning traces. Additionally,
we adapt the task-specific hints from MuSR and
translate them into Korean for Ko-MuSR. Hints
provide detailed descriptions of how to approach
the task, typically consisting of four to five sen-
tences. Prompt templates and detailed examples
can be found in Appendix H.
A specific name identifies each configuration.
For example, the name 3-Shot/CoT/Hint indicates
that the LLM is provided with three in-context
learning examples that include both reasoning
traces and hints. We clearly specify the number
of examples, whether Chain-of-Thought (CoT) rea-
soning is used by referring to it as CoT or Direct
for straightforward responses, and we indicate the
presence or absence of hints by using Hint and No
Hint.
5.2
Model Performance
Table 3 presents the zero-shot performance of mod-
els on both MuSR and Ko-MuSR. Some MuSR
instances for object placement contain five answer
choices, which leads to a random baseline accuracy
of 24.6. For Ko-MuSR, we ensure that all questions
have a consistent number of answer choices across
subtasks. We measure model accuracy for each sub-
task, Murder Mysteries (MM), Object Placements
(OP), and Team Allocations (TA).
We begin by evaluating model accuracy without
employing advanced prompting techniques (such
as Chain of Thought or hints) to establish a baseline
for direct reasoning capabilities. Among all LLMs,
Qwen3 32B achieves the highest accuracy across
both English and Korean benchmarks, closely fol-
lowed by LLaMA 4 Scout Instruct. This consis-
tency indicates that strong multilingual reasoning
abilities can effectively transfer between languages,
particularly between English and Korean. These
results suggest that multistep reasoning in long
narratives is primarily influenced by the reasoning
structure rather than by linguistic specialization.
We will next evaluate the performance of our
LLMs under improved prompting conditions (see
Table 4). By incorporating three few-shot examples
along with CoT and hint prompts, we observe a
significant increase in accuracy across all models.
Table 5 illustrates a case involving the Naver
HyperClova X SEED Think 14B model with vari-
ous prompting configurations. In Appendix A, we
analyze the impact of the number of few-shot exam-
ples and the prompting strategies, demonstrating
that both chain-of-thought examples and hints con-
tribute to performance enhancements. The configu-
ration with CoT and hints achieves nearly optimal
performance in the team allocation task within the
Korean context, where three models exceed human
accuracy, and one matches it. As model accuracy
approaches human performance, the differences
among the models diminish. However, Korean-
specialized models still underperform in the object
placement task within this context, indicating there
is still room for improvement in Korean-specific
reasoning.
We finally evaluate the effects of the same
prompting configuration—3-Shot/CoT/Hint—on
small language models (SLMs), which is shown in
Table 6. We notice that the impact of the prompting
is inconsistent across different SLMs. In an extreme
case, the accuracy of Qwen3 1.7B on the Object
Placements task in English decreases by 12.7 points
when 3-shot CoT Hint prompts are used. This find-
ing indicates that prompting methods should be
carefully tailored to each specific task to enhance
the multistep reasoning abilities of SLMs.
6
Discussions
LLMs’ reasoning generalizes across languages.
Previous evaluations of HRCRM (Son et al., 2025a)
have demonstrated that multilingual models can ef-
fectively reason using Korean-specific knowledge.
HRCRM is divided into two subsets: the date sub-
set, which involves reasoning about Korean holi-
days, date expressions, and conversions between
the solar and lunar calendars, and the zodiac subset,
which tests knowledge of Korea’s traditional age
system and zodiac relationships.
Despite requiring reasoning grounded in local
cultural contexts, the benchmark shows that multi-
lingual models such as o1 (OpenAI et al., 2024a)
and GPT-4o (OpenAI et al., 2024b) outperform a
Korean-specialized model, Exaone 3.5-32B (LG
AI Research, 2024a). This result suggests that the
reasoning abilities of multilingual LLMs general-
ize beyond the primary languages on which they
were trained, encompassing even culturally specific
reasoning.
Our findings on Ko-MuSR further support this
7

--- Page 8 ---

observation. As demonstrated in Table 3, multilin-
gual models exhibit strong reasoning performance,
even on Korean benchmarks that require under-
standing long, narrative-style contexts.
Interestingly, the ranking of zero-shot accuracy
among the LLMs aligns with the estimated num-
ber of text tokens used during their pretraining.
Qwen3 32B, which was trained on over 36 trillion
text tokens, achieves the highest accuracy. This
is followed by LLaMA 4 Scout Instruct, which
was trained on approximately 30 trillion multi-
modal tokens, including text, images, and video.
Among LLMs specialized for Korean, Exaone 4.0
32B, trained on 14 trillion text tokens and featur-
ing a denser parameterization, outperforms Hyper-
CLOVA X SEED Think 14B, which was trained
on 6 trillion tokens.
Both the HRCRM and Ko-MuSR results demon-
strate that large multilingual models are capable
of multistep reasoning across languages, cultural
boundaries, and even in long-context narrative set-
tings. However, their performance still falls short
of human accuracy, indicating a need for improve-
ment.
Detailed prompts and reasoning examples are
beneficial.
Although state-of-the-art multilingual
models maintain strong performance, language-
specific models can bridge the gap through effec-
tive prompting strategies. Our results demonstrate
that using 3-shot/CoT prompting, along with de-
scriptive hints, significantly improves performance
across the four evaluated LLMs. We examine the
impact of each component on model performance
in Appendix A and find that among the three com-
ponents, the hint—a detailed task description—
consistently provides the most significant perfor-
mance gain across models. This approach allows
several models to achieve or even exceed human-
level accuracy, thereby reducing performance dis-
crepancies among different model families. These
findings emphasize that specialized models, despite
having smaller training budgets, can attain competi-
tive reasoning performance in their target language
through structured prompting.
SLMs benefit less from detailed prompts and
reasoning examples.
Lu et al. (2025) have
shown that smaller models benefit less from in-
context learning compared to larger ones by eval-
uating 24 small language models (SLMs). They
compared the average accuracy of 5-shot and 0-
shot settings across eight English benchmarks us-
ing models ranging from 100 M to 4 B parame-
ters. The results indicate that the performance gains
from in-context examples increase with model size;
in fact, some smaller models even exhibit perfor-
mance drops. This suggests that including exam-
ples in the prompt can hinder accuracy when the
model size is insufficiently small.
Our evaluation of Ko-MuSR reinforces this find-
ing. The smallest SLM (Qwen3 0.6B) shows im-
provements with the 3-shot/CoT/Hint prompt in
only one subtask, while larger SLMs benefit across
multiple subtasks. Additionally, we observe signifi-
cant performance degradation—up to 12.7 points
in the most extreme case—when a 3-shot/CoT/Hint
prompt is provided to smaller models. In contrast,
LLMs generally improve under the same prompt-
ing conditions and do not show these performance
drops.
Overall, both the results from the English bench-
marks and our Ko-MuSR findings consistently
demonstrate that LLMs gain more from in-context
learning, while smaller models may be adversely
affected. This trend appears to persist across lan-
guages, indicating a general limitation of in-context
learning for SLMs. Further analysis can be found
in Appendix B.
7
Conclusions
In this paper, we introduce Ko-MuSR, a Korean
benchmark for evaluating multistep soft reason-
ing in long narrative contexts. It follows MuSR’s
synthesis process and minimizes the risk of con-
tamination. It consists of 250 questions across three
subtasks assessing different reasoning aspects in
LLMs. The dataset is generated through a con-
trolled pipeline and refined via human review to
ensure factual and logical validity. Our empiri-
cal results show that state-of-the-art multilingual
models outperform Korean-specialized ones on Ko-
MuSR. Providing three in-context examples with
explicit reasoning and hints markedly improves
performance, nearing human-level accuracy. These
results suggest that structured prompting and long-
context conditioning can improve the reasoning
ability of Korean LLMs, enabling specialized mod-
els to narrow the gap with their multilingual coun-
terparts. Despite its limited task scope, Ko-MuSR
offers a solid foundation for advancing Korean
NLP by enabling systematic evaluation of long-
context reasoning and prompting strategies.
8

--- Page 9 ---

Limitations
We reconstruct MuSR for only for Korean, limiting
our scope of research in model capability in two
languages: English and Korean.
While we present representative state-of-the-art
open-parameter LLMs for the evaluation, we do not
evaluate all the models that are capable of Korean
and English.
While repeated trials on the benchmark could
further reduce variance caused by randomness, we
conducted only two evaluation runs due to compu-
tational resource constraints.
Ethics Statement
We construct the Ko-MuSR benchmark using only
LLMs, primarily OpenAI3 GPT-4o and o1 models.
Since the content is fictional and synthesized, the
dataset does not contain personal information or
real-world references that may raise ethical con-
cerns.
The authors, as members of the research group,
participated in reviewing the Korean benchmark.
Their work was supported by the grants listed
in the Acknowledgements section. Compensation
for their contribution was acknowledged at KRW
10,030 per hour, corresponding to the 2025 mini-
mum wage in Korea.
We evaluated the human performance on the
benchmark. All evaluation procedures were con-
ducted under the supervision of the Institutional Re-
view Board of Seoul National University (SNUIRB,
No. 2506/001-001). Participants’ contributions
were recognized as one full day (8 hours) of work
and compensated with KRW 100,000, exceeding
the 2025 minimum daily wage of KRW 80,240 in
Korea.
Acknowledgements
This work was partially supported by the Na-
tional Research Foundation of Korea (NRF) under
Grant No. RS-2023-00222663 (Center for Opti-
mizing Hyperscale AI Models and Platforms), and
by the Institute for Information and Communica-
tions Technology Promotion (IITP) under Grant No.
2018-0-00581 (CUDA Programming Environment
for FPGA Clusters) and No. RS-2025-02304554
(Efficient and Scalable Framework for AI Hetero-
geneous Cluster Systems), all funded by the Min-
istry of Science and ICT (MSIT) of Korea. It was
3https://openai.com
also partially supported by the Korea Health In-
dustry Development Institute (KHIDI) under Grant
No. RS-2025-25454559 (Frailty Risk Assessment
and Intervention Leveraging Multimodal Intelli-
gence for Networked Deployment in Community
Care), funded by the Ministry of Health and Wel-
fare (MOHW) of Korea. Additional support was
provided by the BK21 Plus Program for Innova-
tive Data Science Talent Education (Department
of Data Science, Seoul National University, No.
5199990914569) and the BK21 FOUR Program
for Intelligent Computing (Department of Com-
puter Science and Engineering, Seoul National Uni-
versity, No. 4199990214639), both funded by the
Ministry of Education (MOE) of Korea. This work
was also partially supported by the Artificial Intel-
ligence Industrial Convergence Cluster Develop-
ment Project, funded by the MSIT and Gwangju
Metropolitan City. Research facilities were pro-
vided by the Institute of Computer Technology
(ICT) at Seoul National University.
References
Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, Sandhini Agarwal, Ariel Herbert-Voss,
Gretchen Krueger, Tom Henighan, Rewon Child,
Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu,
Clemens Winter, and 12 others. 2020.
Lan-
guage models are few-shot learners.
Preprint,
arXiv:2005.14165.
Aakanksha Chowdhery, Sharan Narang, Jacob Devlin,
Maarten Bosma, Gaurav Mishra, Adam Roberts,
Paul Barham, Hyung Won Chung, Charles Sutton,
Sebastian Gehrmann, Parker Schuh, Kensen Shi,
Sasha Tsvyashchenko, Joshua Maynez, Abhishek
Rao, Parker Barnes, Yi Tay, Noam Shazeer, Vin-
odkumar Prabhakaran, and 48 others. 2022. Palm:
Scaling language modeling with pathways. Preprint,
arXiv:2204.02311.
Alexis Conneau, Ruty Rinott, Guillaume Lample, Adina
Williams, Samuel Bowman, Holger Schwenk, and
Veselin Stoyanov. 2018. XNLI: Evaluating cross-
lingual sentence representations.
In Proceedings
of the 2018 Conference on Empirical Methods in
Natural Language Processing, pages 2475–2485,
Brussels, Belgium. Association for Computational
Linguistics.
Tri Dao, Daniel Fu, Stefano Ermon, Atri Rudra, and
Christopher Re. 2022.
Flashattention: Fast and
memory-efficient exact attention with io-awareness.
In Advances in Neural Information Processing
Systems (NeurIPS).
9

--- Page 10 ---

Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. Bert: Pre-training of deep
bidirectional transformers for language understand-
ing. Preprint, arXiv:1810.04805.
Manuel Faysse, Patrick Fernandes, Nuno M. Guerreiro,
António Loison, Duarte M. Alves, Caio Corro, Nico-
las Boizard, João Alves, Ricardo Rei, Pedro H. Mar-
tins, Antoni Bigata Casademunt, François Yvon, An-
dré F. T. Martins, Gautier Viaud, Céline Hudelot,
and Pierre Colombo. 2025. Croissantllm: A truly
bilingual french-english language model. Preprint,
arXiv:2402.00786.
Leo Gao, Jonathan Tow, Stella Biderman, Sid Black,
Laurence Golding, Eric Hallahan McDonell, Jason
Phang, Charles Foster, Alexander Rush, Connor
Leahy, and 1 others. 2021.
Eleutherai language
model evaluation harness. https://github.com/
EleutherAI/lm-evaluation-harness.
GitHub
repository.
Myeongjun Jang, Dohyung Kim, Deuk Sin Kwon,
and Eric Davis. 2022. KoBEST: Korean balanced
evaluation of significant tasks. In Proceedings of
the 29th International Conference on Computational
Linguistics, pages 3697–3708, Gyeongju, Republic
of Korea. International Committee on Computational
Linguistics.
Deokyeong Kang and Taeuk Kim. 2024. Analysis of lan-
guage models in korean program synthesis based on
the kr-humaneval benchmark. In Annual Conference
on Human and Language Technology, pages 245–
250. Human and Language Technology.
Eunsu Kim, Juyoung Suk, Philhoon Oh, Haneul Yoo,
James Thorne, and Alice Oh. 2024.
CLIcK: A
benchmark dataset of cultural and linguistic intel-
ligence in Korean.
In Proceedings of the 2024
Joint International Conference on Computational
Linguistics, Language Resources and Evaluation
(LREC-COLING 2024), pages 3335–3346, Torino,
Italia. ELRA and ICCL.
Hyunwoo Ko, Guijin Son, and Dasol Choi. 2025. Un-
derstand, solve and translate: Bridging the mul-
tilingual mathematical reasoning gap.
Preprint,
arXiv:2501.02448.
Woonhyuk Kwon, Yuheng Sheng, Yifan Li, Daniel
Crankshaw, and Joseph E. Gonzalez. 2023. Efficient
memory management for large language model serv-
ing with vllm. Preprint, arXiv:2309.06180.
Guillaume Lample and Alexis Conneau. 2019. Cross-
lingual language model pretraining.
Preprint,
arXiv:1901.07291.
LG AI Research. 2024a. Exaone 3.5: Series of large
language models for real-world use cases.
arXiv
preprint arXiv:https://arxiv.org/abs/2412.04862.
LG AI Research. 2024b.
Komt-bench.
https:
//huggingface.co/datasets/LGAI-EXAONE/
KoMT-Bench.
LG AI Research. 2025. Exaone 4.0: Unified large lan-
guage models integrating non-reasoning and reason-
ing modes. Preprint, arXiv:2507.11407.
Xi Victoria Lin, Todor Mihaylov, Mikel Artetxe, Tianlu
Wang, Shuohui Chen, Daniel Simig, Myle Ott, Na-
man Goyal, Shruti Bhosale, Jingfei Du, Ramakanth
Pasunuru, Sam Shleifer, Punit Singh Koura, Vishrav
Chaudhary, Brian O’Horo, Jeff Wang, Luke Zettle-
moyer, Zornitsa Kozareva, Mona Diab, and 2 oth-
ers. 2022. Few-shot learning with multilingual gen-
erative language models.
In Proceedings of the
2022 Conference on Empirical Methods in Natural
Language Processing, pages 9019–9052, Abu Dhabi,
United Arab Emirates. Association for Computa-
tional Linguistics.
Zhenyan Lu, Xiang Li, Dongqi Cai, Rongjie Yi,
Fangming Liu, Xiwen Zhang, Nicholas D. Lane,
and Mengwei Xu. 2025.
Small language mod-
els: Survey, measurements, and insights. Preprint,
arXiv:2409.15790.
Meta. 2025. The llama 4 herd: The beginning of a new
era of natively multimodal ai innovation.
Mistral-AI, :, Abhinav Rastogi, Albert Q. Jiang, Andy
Lo, Gabrielle Berrada, Guillaume Lample, Jason
Rute, Joep Barmentlo, Karmesh Yadav, Kartik Khan-
delwal, Khyathi Raghavi Chandu, Léonard Blier, Lu-
cile Saulnier, Matthieu Dinot, Maxime Darrin, Neha
Gupta, Roman Soletskyi, Sagar Vaze, and 82 others.
2025. Magistral. Preprint, arXiv:2506.10910.
NAVER Cloud HyperCLOVA X Team. 2025.
Hy-
perclova x think technical report.
Preprint,
arXiv:2506.22403.
OpenAI, :, Aaron Jaech, Adam Kalai, Adam Lerer,
Adam Richardson, Ahmed El-Kishky, Aiden Low,
Alec Helyar, Aleksander Madry, Alex Beutel, Alex
Carney, Alex Iftimie, Alex Karpenko, Alex Tachard
Passos, Alexander Neitz, Alexander Prokofiev,
Alexander Wei, Allison Tam, and 244 others. 2024a.
Openai o1 system card. Preprint, arXiv:2412.16720.
OpenAI. 2024a.
Gpt-4 technical report.
Preprint,
arXiv:2303.08774.
OpenAI. 2024b. Multilingual massive multitask lan-
guage understanding.
OpenAI. 2025. Openai python sdk. https://github.
com/openai/openai-python. Version 1.78.0.
OpenAI, Josh Achiam, Steven Adler, Sandhini Agarwal,
Lama Ahmad, Ilge Akkaya, Florencia Leoni Ale-
man, Diogo Almeida, Janko Altenschmidt, Sam Alt-
man, Shyamal Anadkat, Red Avila, Igor Babuschkin,
Suchir Balaji, Valerie Balcom, Paul Baltescu, Haim-
ing Bao, Mohammad Bavarian, Jeff Belgum, and
262 others. 2024b. Gpt-4 technical report. Preprint,
arXiv:2303.08774.
10

--- Page 11 ---

Chanjun Park, Hyeonwoo Kim, Dahyun Kim, SeongH-
wan Cho, Sanghoon Kim, Sukyung Lee, Yungi Kim,
and Hwalsuk Lee. 2024.
Open Ko-LLM leader-
board: Evaluating large language models in Ko-
rean with Ko-h5 benchmark.
In Proceedings of
the 62nd Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers),
pages 3220–3234, Bangkok, Thailand. Association
for Computational Linguistics.
Jeonghwan Park. 2024. Logickor.
Adam Paszke, Sam Gross, Francisco Massa, Adam
Lerer, James Bradbury, Gregory Chanan, Trevor
Killeen, Zeming Lin, Natalia Gimelshein, Luca
Antiga, Alban Desmaison, Andreas Kopf, Edward
Yang, Zachary DeVito, Martin Raison, Alykhan Te-
jani, Sasank Chilamkurthy, Benoit Steiner, Lu Fang,
and 2 others. 2019. Pytorch: An imperative style,
high-performance deep learning library. In Advances
in Neural Information Processing Systems (NeurIPS
2019).
Edoardo Maria Ponti, Goran Glavaš, Olga Majew-
ska, Qianchu Liu, Ivan Vuli´c, and Anna Korhonen.
2020. XCOPA: A multilingual dataset for causal
commonsense reasoning.
In Proceedings of the
2020 Conference on Empirical Methods in Natural
Language Processing (EMNLP), pages 2362–2376,
Online. Association for Computational Linguistics.
Freda Shi, Mirac Suzgun, Markus Freitag, Xuezhi Wang,
Suraj Srivats, Soroush Vosoughi, Hyung Won Chung,
Yi Tay, Sebastian Ruder, Denny Zhou, Dipanjan
Das, and Jason Wei. 2022. Language models are
multilingual chain-of-thought reasoners. Preprint,
arXiv:2210.03057.
Guijin Son, Hyunwoo Ko, and Dasol Choi. 2025a.
Multi-step reasoning in Korean and the emergent
mirage.
In Proceedings of the 3rd Workshop
on Cross-Cultural Considerations in NLP (C3NLP
2025), pages 10–21, Albuquerque, New Mexico. As-
sociation for Computational Linguistics.
Guijin Son, Hanwool Lee, Sungdong Kim, Seun-
gone Kim, Niklas Muennighoff, Taekyoon Choi,
Cheonbok Park, Kang Min Yoo, and Stella Bi-
derman. 2025b.
KMMLU: Measuring mas-
sive multitask language understanding in Korean.
In Proceedings of the 2025 Conference of the
Nations of the Americas Chapter of the Association
for Computational Linguistics: Human Language
Technologies (Volume 1: Long Papers), pages 4076–
4104, Albuquerque, New Mexico. Association for
Computational Linguistics.
Guijin Son, Hanwool Lee, Suwan Kim, Huiseo Kim,
Jae Cheol Lee, Je Won Yeom, Jihyu Jung, Jung Woo
Kim, and Songseong Kim. 2023. Hae-rae bench:
Evaluation of korean knowledge in language mod-
els. https://github.com/EleutherAI/hae-rae/
tree/main/HAE-RAE%20Bench.
Guijin Son, Hanwool Lee, Suwan Kim, Huiseo
Kim, Jae cheol Lee, Je Won Yeom, Jihyu Jung,
Jung woo Kim, and Songseong Kim. 2024. HAE-
RAE bench: Evaluation of Korean knowledge in
language models.
In Proceedings of the 2024
Joint International Conference on Computational
Linguistics, Language Resources and Evaluation
(LREC-COLING 2024), pages 7993–8007, Torino,
Italia. ELRA and ICCL.
Zayne Rea Sprague, Xi Ye, Kaj Bostrom, Swarat Chaud-
huri, and Greg Durrett. 2024. MuSR: Testing the
limits of chain-of-thought with multistep soft rea-
soning. In The Twelfth International Conference on
Learning Representations.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten
Bosma, brian ichter, Fei Xia, Ed H. Chi, Quoc V
Le, and Denny Zhou. 2022.
Chain of thought
prompting elicits reasoning in large language mod-
els. In Advances in Neural Information Processing
Systems.
Thomas Wolf, Lysandre Debut, Victor Sanh, Julien
Chaumond, Clement Delangue, Anthony Moi, Pier-
ric Cistac, Tim Rault, Remi Louf, Morgan Funtow-
icz, Jamie Brew, and 1 others. 2020. Transform-
ers: State-of-the-art natural language processing. In
Proceedings of the 2020 Conference on Empirical
Methods in Natural Language Processing: System
Demonstrations, pages 38–45.
An Yang, Anfeng Li, Baosong Yang, Beichen Zhang,
Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao,
Chengen Huang, Chenxu Lv, Chujie Zheng, Day-
iheng Liu, Fan Zhou, Fei Huang, Feng Hu, Hao
Ge, Haoran Wei, Huan Lin, Jialong Tang, and 41
others. 2025.
Qwen3 technical report.
Preprint,
arXiv:2505.09388.
Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali
Farhadi, and Yejin Choi. 2019. HellaSwag: Can a
machine really finish your sentence? In Proceedings
of the 57th Annual Meeting of the Association for
Computational Linguistics, pages 4791–4800, Flo-
rence, Italy. Association for Computational Linguis-
tics.
11

--- Page 12 ---

A
Ablations on Prompt Variants
Effects of In-Context Learning
Table 7 shows
the effect of the number of in-context examples on
model performance. We find that providing few-
shot examples substantially improves model accu-
racy on Korean tasks, suggesting that models can
analogically reason about similar problems when
given task-specific examples. However, the perfor-
mance gain from adding more examples diminishes
under the CoT and Hint settings, where the models
already approach their upper performance bound.
In contrast, for the HyperCLOVA X SEED Think
model, incorporating three examples yields a signif-
icant boost, indicating that three-shot prompting is
a particularly effective configuration for this model.
Effects of Hints
Table 8 reports the impact of
providing task-specific hints. We find that hints
generally enhance model accuracy, underscoring
the importance of precise task descriptions.
Effects of Chain-of-Thought Reasoning
Ta-
ble 9 presents the effect of including chain-of-
thought (CoT) examples. We observe that CoT
examples are particularly beneficial for Korean-
specialized models, while multilingual models oc-
casionally experience performance degradation.
Nevertheless, since CoT prompting provides sub-
stantial improvements when effective and rarely
leads to significant drops, we adopt CoT examples
as part of our main evaluation configuration.
B
SLM Prompting
This section examines whether detailed prompt-
ing improves the reasoning capability of small
language models (SLMs), which are increasingly
adopted for their computational efficiency. Table 10
reports the performance of SLMs under various
prompting configurations. For the smallest model,
Qwen3 0.6B, we find that prompting the model
with no examples yields the best results, while
even simple in-context examples lead to an accu-
racy drop. For larger SLMs, the benefits of few-
shot prompting are mixed. The Qwen3 1.7B model
exhibits different optimal configurations across
subtasks, whereas Exaone 4.0 1.2B benefits from
chain-of-thought and hint-based prompting. Our
largest SLMs, Exaone 3.5B Instruct and Qwen3
4B, generally achieve the highest accuracy when
given few-shot chain-of-thought examples with
hints, suggesting that larger models gain more from
detailed in-context learning examples.
C
Evaluation Configuration
We use transformers (Wolf et al., 2020),
lm-evaluation-harness (Gao et al., 2021) and
vLLM (Kwon et al., 2023) frameworks for model
evaluation. All models are evaluated in both En-
glish and Korean settings to ensure consistent evalu-
ation configurations across languages. As described
in Section 5, we adopt the 3-Shot CoT Hint config-
uration for all evaluations. The test splits of both
MuSR and Ko-MuSR benchmarks are used for as-
sessment, while the prompt split—a separate subset
excluded from the test set—is used for few-shot
examples. Since our models support chat templates,
we apply the corresponding templates when provid-
ing in-context learning examples. For Ko-MuSR,
we release the prompt split consisting of three ex-
amples and their corresponding solutions.
We provide evaluation prompts for 3-Shot, CoT,
Hint configuration as we find this configuration
beneficial for models to increase accuracy. See Ap-
pendix H for prompt details.
D
Computation
We conduct all experiments on an on-premise GPU
cluster consisting of eight nodes, each equipped
with four NVIDIA RTX 3090 GPUs. The GPUs
within each node are interconnected via a PCIe
Gen4, and the nodes are connected through an
NVIDIA Mellanox InfiniBand EDR (100 Gbps)
network. We employ vLLM to build a multi-GPU,
multi-node inference system for model evaluation.
Within a node, model parameters are distributed
with tensor parallelism while we utilize pipeline
parallelism across nodes. Table 11 summarizes the
configuration of the inference system and reports
the elapsed time for evaluating the 3-Shot CoT Hint
configuration. With repetitions of experiments, we
report 3,849 GPU Hours(RTX 3090) in total.
Upon release on the Hugging Face Hub4, Hy-
perClovaX SEED Think 14B model did not in-
clude support for tensor parallelism. We modified
its configuration file to enable tensor parallel infer-
ence. To validate our implementation, we evaluated
the model on the Hellaswag (Zellers et al., 2019)
benchmark. While the original authors reported an
accuracy of 61.25, our reproduced result of 64.04
confirms the correctness of our implementation.
4https://huggingface.co
12

--- Page 13 ---

Model
En-MM
En-OP
En-TA
Ko-MM
Ko-OP
Ko-TA
QWEN3 32B
66.4
52.7
73.4
67.6
80.0
79.6
+ 1 Shot / Direct / No Hint
73.6
62.1
81.0
69.2
83.0
80.6
+ 3 Shots / Direct / No Hint
76.2
64.6
76.0
71.8
85.4
81.8
+ 1 Shot / CoT / Hint
83.6
75.8
89.6
77.8
79.2
87.8
+ 3 Shots / CoT / Hint
82.4
74.2
88.8
76.0
81.8
89.0
LLaMA 4 Scout
65.4
54.1
60.4
56.0
67.8
64.2
+ 1 Shot / Direct / No Hint
69.6
56.4
70.0
72.8
73.0
70.8
+ 3 Shots / Direct / No Hint
72.6
61.5
78.0
70.4
75.6
82.6
+ 1 Shot / CoT / Hint
77.2
69.7
84.4
75.0
80.8
85.6
+ 3 Shots / CoT / Hint
75.6
68.6
84.2
72.8
83.0
88.0
Exaone 4.0 32B
61.2
55.7
58.8
52.8
37.4
63.2
+ 1 Shot / Direct / No Hint
74.8
57.8
63.4
62.4
48.8
65.4
+ 3 Shots / Direct / No Hint
76.0
62.5
69.4
68.6
60.2
73.6
+ 1 Shot / CoT / Hint
80.8
74.0
86.6
67.6
71.0
79.6
+ 3 Shots / CoT / Hint
75.2
72.1
85.8
71.2
71.6
85.8
HyperClova X SEED Think 14B
51.6
38.7
44.0
44.6
41.2
58.6
+ 1 Shot / Direct / No Hint
63.8
42.0
53.6
50.0
39.0
51.8
+ 3 Shots / Direct / No Hint
67.8
63.7
76.0
65.4
52.4
86.2
+ 1 Shot / CoT / Hint
70.2
51.4
75.2
63.8
37.6
84.6
+ 3 Shots / CoT / Hint
68.6
66.2
81.0
70.6
50.0
87.8
Table 7: Ablation - Effects of Number of Few Shot Examples. The first row denotes the zero-shot, direct, and no-hint
configuration.
13

--- Page 14 ---

Model
En-MM
En-OP
En-TA
Ko-MM
Ko-OP
Ko-TA
QWEN3 32B
66.4
52.7
73.4
67.6
80.0
79.6
+ 1 Shot / Direct / No Hint
73.6
62.1
81.0
69.2
83.0
80.6
+ 1 Shot / Direct / Hint
84.4
74.8
89.2
78.6
87.0
87.8
+ 3 Shots / CoT / No Hint
74.4
69.2
80.2
73.4
75.4
83.0
+ 3 Shots / CoT / Hint
82.4
74.2
88.8
76.0
81.8
89.0
LLaMA 4 Scout
65.4
54.1
60.4
56.0
67.8
64.2
+ 1 Shot / Direct / No Hint
69.6
56.4
70.0
72.8
73.0
70.8
+ 1 Shot / Direct / Hint
74.0
61.1
86.0
76.8
79.8
81.2
+ 3 Shots / CoT / No Hint
71.6
62.9
78.2
71.4
75.8
83.8
+ 3 Shots / CoT / Hint
75.6
68.6
84.2
72.8
83.0
88.0
Exaone 4.0 32B
61.2
55.7
58.8
52.8
37.4
63.2
+ 1 Shot / Direct / No Hint
74.8
57.8
63.4
62.4
48.8
65.4
+ 1 Shot / Direct / Hint
76.6
73.5
85.8
69.6
61.6
80.0
+ 3 Shots / CoT / No Hint
74.6
60.2
70.0
70.4
62.8
77.2
+ 3 Shots / CoT / Hint
75.2
72.1
85.8
71.2
71.6
85.8
HyperClova X SEED Think 14B
51.6
38.7
44.0
44.6
41.2
58.6
+ 1 Shot / Direct / No Hint
63.8
42.0
53.6
50.0
39.0
51.8
+ 1 Shot / Direct / Hint
69.0
43.0
67.0
59.4
42.0
58.2
+ 3 Shots / CoT / No Hint
67.0
63.7
74.0
64.6
47.0
84.6
+ 3 Shots / CoT / Hint
68.6
66.2
81.0
70.6
50.0
87.8
Table 8: Ablation - Effects of Hint. The first row denotes the zero-shot, direct, and no-hint configuration.
14

--- Page 15 ---

Model
En-MM
En-OP
En-TA
Ko-MM
Ko-OP
Ko-TA
QWEN3 32B
66.4
52.7
73.4
67.6
80.0
79.6
+ 1 Shot / Direct / Hint
84.4
74.8
89.2
78.6
87.0
87.8
+ 1 Shot / CoT / Hint
83.6
75.8
89.6
77.8
79.2
87.8
+ 3 Shots / Direct / Hint
82.4
76.8
90.2
77.8
86.8
88.8
+ 3 Shots / CoT / Hint
82.4
74.2
88.8
76.0
81.8
89.0
LLaMA 4 Scout
65.4
54.1
60.4
56.0
67.8
64.2
+ 1 Shot / Direct / Hint
74.0
61.1
86.0
76.8
79.8
81.2
+ 1 Shot / CoT / Hint
77.2
69.7
84.4
75.0
80.8
85.6
+ 3 Shots / Direct / Hint
76.0
68.2
86.6
73.6
81.2
87.2
+ 3 Shots / CoT / Hint
75.6
68.6
84.2
72.8
83.0
88.0
Exaone 4.0 32B
61.2
55.7
58.8
52.8
37.4
63.2
+ 1 Shot / Direct / Hint
76.6
73.4
85.8
69.6
61.6
80.0
+ 1 Shot / CoT / Hint
80.8
74.0
86.6
67.6
71.0
79.6
+ 3 Shots / Direct / Hint
73.6
72.7
83.6
70.0
64.8
84.2
+ 3 Shots / CoT / Hint
75.2
72.1
85.8
71.2
71.6
85.8
HyperClova X SEED Think 14B
51.6
38.7
44.0
44.6
41.2
58.6
+ 1 Shot / Direct / Hint
69.0
43.0
67.0
59.4
42.0
58.2
+ 1 Shot / CoT / Hint
70.2
51.4
75.2
63.8
37.6
84.6
+ 3 Shots / Direct / Hint
67.0
64.8
83.8
63.8
49.6
83.8
+ 3 Shots / CoT / Hint
68.6
66.2
81.0
70.6
50.0
87.8
Table 9: Ablation - Effects of CoT Examples. The first row denotes the zero-shot, direct, and no-hint configuration.
15

--- Page 16 ---

Models
En-MM
En-OP
En-TA
Ko-MM
Ko-OP
Ko-TA
QWEN3 0.6B
59.2
52.0
38.8
53.6
28.6
38.0
+ 1 Shot / Direct / No Hint
55.4
50.8
31.4
53.6
23.8
34.0
+ 3 Shots / Direct / No Hint
54.4
48.8
36.4
57.0
28.6
32.4
+ 1 Shot / CoT / Hint
57.2
46.7
36.6
52.0
27.4
32.4
+ 3 Shots / CoT / Hint
55.4
46.7
33.0
49.0
30.2
33.4
Exaone 4.0 1.2B
55.6
44.7
49.8
48.0
29.0
44.8
+ 1 Shot / Direct / No Hint
60.4
50.0
47.8
55.4
27.2
42.2
+ 3 Shots / Direct / No Hint
61.0
42.8
45.8
49.4
27.2
40.2
+ 1 Shot / CoT / Hint
66.8
44.1
57.8
58.0
29.8
41.4
+ 3 Shots / CoT / Hint
64.8
44.7
54.8
58.6
31.6
35.8
QWEN3 1.7B
60.6
52.3
59.0
50.0
34.0
63.2
+ 1 Shot / Direct / No Hint
64.0
50.2
54.4
55.2
33.4
56.0
+ 3 Shots / Direct / No Hint
59.6
53.1
53.4
58.0
34.8
51.0
+ 1 Shot / CoT / Hint
70.8
42.2
58.2
56.0
30.8
54.6
+ 3 Shots / CoT / Hint
66.0
39.6
55.4
63.0
33.0
54.2
Exaone 3.5 2.4B Instruct
51.4
41.6
44.0
51.0
30.0
42.4
+ 1 Shot / Direct / No Hint
56.2
45.3
42.6
55.8
40.0
37.6
+ 3 Shots / Direct / No Hint
56.8
45.7
38.4
58.0
40.2
39.4
+ 1 Shot / CoT / Hint
61.4
47.7
39.6
56.4
40.4
37.8
+ 3 Shots / CoT / Hint
63.4
48.6
37.2
56.0
41.2
42.8
QWEN3 4B
62.8
55.5
66.0
59.0
51.0
75.4
+ 1 Shot / Direct / No Hint
67.0
53.3
69.4
63.4
51.8
74.0
+ 3 Shots / Direct / No Hint
68.2
49.0
69.6
66.4
53.6
69.8
+ 1 Shot / CoT / Hint
76.2
69.3
86.2
69.8
56.0
76.4
+ 3 Shots / CoT / Hint
74.0
70.7
85.4
69.8
55.2
79.6
Table 10: Ablation - SLMs. The first row denotes the zero-shot, direct, and no-hint configuration. Boldface indicates
the highest numbers, and underlined numbers indicate the second highest.
Models
Num nodes
Num GPUs
TP
PP
En-MM
En-OP
En-TA
Ko-MM
Ko-OP
Ko-TA
QWEN3 32B
2
8
4
2
205
127
329
224
174
307
LLaMA 4 Scout Instruct
4
16
4
4
105
55
136
109
82
180
Exaone 4.0 32B
2
8
4
2
92
76
120
106
71
118
HyperClova X SEED Think 14B
1
4
4
1
112
108
108
112
102
109
QWEN3 0.6B
1
1
1
1
38
15
44
49
17
50
Exaone 4.0 1.2B
1
1
1
1
12
12
20
15
14
20
QWEN3 1.7B
1
1
1
1
121
40
120
99
56
163
Exaone 3.5 2.4B Instruct
1
1
1
1
106
100
104
96
93
97
QWEN 3 4B
1
2
2
1
145
74
158
142
126
224
Table 11: Number of GPus and Time(in minutes) Required for Evaluation with 3-Shot, CoT, Hint Configuration
16

--- Page 17 ---

E
Data Review Process
As described in Section 4, we review all data in-
stances to ensure the validity of the question and the
quality of data instances. Although the synthesized
texts are unlikely to contain personally identifiable
information or unsafe content, annotators carefully
confirmed that such content was excluded from
all instances; otherwise, they left notes for senior
reviewers to examine.
Specific criteria for marking pass, minor issue
and fail are as follows:
• Pass: The answer can be derived from the
narrative and has no issue to be used as a
benchmark instance.
• Minor Issue: The instance contains small
issues (e.g., typos, unclear wording) but it
seems to be usable with minor edits.
• Fail: The instance has critical problems (e.g.,
logical errors, ambiguous answers) and cannot
be used without significant edits.
See Table 12 for the annotation guidelines given
to the annotators.
F
Measuring Human Performance
F.1
Instructions
We evaluate human performance using the 1-shot
CoT Hint configuration. Each participant is pro-
vided with one example per subtask, where the
example includes both a question and a sample
answer with step-by-step reasoning. Participants
are then asked to solve 40 questions per section.
We exclude 9 questions from the murder mysteries
section and 2 questions from the object placements
section, as these instances were later removed from
the benchmark after we tightened the data qual-
ity standards. Appendix J provides examples and
example solutions that were provided to the partici-
pants. For detailed instructions, see Appendix K.
F.2
IRB Approval
We obtained approval from the Institutional Review
Board (IRB) to conduct the human evaluation for
Ko-MuSR, as our study involves human subjects.
This process ensures full compliance with research
ethics and participant protection standards. Follow-
ing the IRB-approved protocol, we recruited five
voluntary participants. All participants were fully
informed that their responses would be anonymized
and their performance scores would be used for sta-
tistical analysis and publication. Table 13 presents
key disclaimers provided to participants.
G
Checklist for ARR Submission
(A1) Limitations of the work
Please refer to the
Limitations section of the main text.
(A2) Potential risks of the work
Our benchmark
is synthesized with OpenAI APIs and therefore is
unlikely to contain any personally identifiable in-
formation, unsafe content, or materials infringing
copyrights. Our human annotators reviewed all data
instances to ensure the above-stated content is ex-
cluded from the benchmark.
(B1) Citations of the used artifacts
We tried
our best to cite all papers, code repositories, and
resources we used in the main content of the paper.
(B2) License or terms of use of the artifacts
Benchmarks. The MuSR dataset is licensed un-
der MIT. We synthesize our data with the artifact
that MuSR releases. We disclose our code and data
under the MIT license as well.
(B3) Proper use of existing artifacts and In-
tended use of created artifacts
The distributed
MuSR artifact and the benchmark are utilized prop-
erly. We use the code for creating custom data as
authors intend to open the code. We use their test
set for model evaluation. As mentioned earlier, use
of artifacts complies with the authors’ intended use
of artifacts. Following MuSR, we will release the
code and the data to enable future researchers to
create data instances and evaluate Korean-capable
language models.
(B4) Description of steps for removing personal
identifiable information(PII) and offensive con-
tents from data
Our benchmark is synthesized
with OpenAI APIs and therefore is unlikely to con-
tain any personally identifiable information, unsafe
content, or materials infringing copyrights. Our
human annotators reviewed all data instances to
ensure the above-stated content is excluded from
the benchmark.
(B5) Documentation of the artifacts
Our
data
for
the
benchmark
is
available
at
https://huggingface.co/datasets/thunder-research-
group/Ko-MuSR, along with the dataset card. Our
code is available at https://github.com/mcrl/Ko-
MuSR.
17

--- Page 18 ---

(B6) Statistics for the data
See Table 2.
(C1) Descriptions of the number of parameters
in the model, the total computational budget,
and computing infrastructure
We utilize open-
parameter models and cite them for describing the
details. We describe our computing infrastructure
and total computational budget in Appendix D.
(C2) Details of experimental setup
For experi-
ment prompts, see Section 5 for the overview and
Appendix H. For model and the generation config-
uration, see Section 5. For system setup for model
inference, see Appendix D.
(C3) Descriptive statistics about results
We re-
peat all experiments twice and report the mean of
the runs. We report all results from repeated runs
in Appendix K.
(C4) Packages/Software Versions
Data Synthesis
We use the original MuSR code-
base (latest version as of 2025.03.01, commit
b1f4d4) (Sprague et al., 2024) for dataset synthe-
sis, and OpenAI Python SDK (v1.78.0) (OpenAI,
2025) for API-based data generation.
Evaluation
We use torch (v2.7.1) (Paszke
et al., 2019) and transformers (v4.55.2) (Wolf
et al., 2020) for model implementation, vllm
(v0.10.0) (Kwon et al., 2023) for multi-gpu, multi-
node inference, flash-attn (v2.7.4) (Dao et al.,
2022) for inference-time attention optimization,
and lm-eval-harness (v0.4.8) (Gao et al., 2021)
for benchmark evaluation. Our modification for en-
abling model inference is described in Appendix
D.
(D1) Full text of instructions or disclaimers of
any risks
Annotation
See Appendix E for the annota-
tion(data review) process. See Table 12 for annota-
tion instructions.
Human Evaluation
See Appendix F for the hu-
man evaluation process. See Table 13 for the con-
sent form we have provided. See Appendix J for the
full text of instructions and the question examples
they were given.
(D2) Recruitment process and payment of paid
participants
The authors, as members of the re-
search group, participated in reviewing the Korean
benchmark. Their work was supported by the grants
listed in the Acknowledgements section. Compen-
sation for their contribution was acknowledged at
KRW 10,030 per hour, corresponding to the 2025
minimum wage in Korea.
We evaluated the human performance on the
benchmark. All evaluation procedures were con-
ducted under the supervision of the Institutional Re-
view Board of Seoul National University (SNUIRB,
No. 2506/001-001). Participants’ contributions
were recognized as one full day (8 hours) of work
and compensated with KRW 100,000, exceeding
the 2025 minimum daily wage of KRW 80,240 in
Korea.
(D3) Consent from the used/curated data
The
annotators, including the authors, are the members
of the research group. All participants were fully
notified that their annotations would be used to
construct a Korean Benchmark. The participants for
human evaluations were fully notified that overall
statistics of their scores would be published. See
Appendix F for the details.
(D4) Review of data collection protocol by an
ethics review board
This study has been re-
viewed and approved by the Institutional Review
Board (SNUIRB, No. 2506/001-001), in compli-
ance with the national regulations on research
ethics. Therefore, the data collection protocol fully
satisfies the ethical standards for involving human
participants. The participants in this study were re-
cruited as healthy adults, and informed consent was
obtained through an official IRB-approved consent
form. All participants were explicitly informed of
the study’s purpose, procedures, risks, benefits, and
their rights to withdraw at any time without penalty.
Their responses were collected anonymously, and
no personally identifiable information was included
in the dataset.
(D5) Basic demographic and geographic charac-
teristics of the annotator population
All anno-
tators are authors or members of the research group.
7 annotators are involved in creating the Korean
benchmark. All annotators are Korean. All annota-
tors are Asian, native to Korean, aged from 20 to
30 (adults).
5 human participants involving human evalua-
tion are students in the organization, whose ages
range from 20 to 30.
(E1) Use of AI assistants
We do not use AI as-
sistants for this work.
18

--- Page 19 ---

H
Prompt Description
H.1
System Prompt
All models were given the following system
prompts per task. For English test instances, we
use the English system prompt, while we use Ko-
rean system prompts otherwise. See Figures 2 and
3.
H.2
Evaluation Prompt
H.2.1
Hints
Listings are hints provided for the evaluation. Note
that hints for Korean settings are the translated
version of the English counterpart. See Figures
from 4 to 9.
H.2.2
Evaluation Prompt Structure
Listings are prompt structures utilized for the eval-
uation. Note that the prompt structure for Korean
settings is a translated version of the English coun-
terpart. See Figures from 10 to 21.
H.3
Data Synthesis Prompt
See Figures from 22 to 33.
19

--- Page 20 ---

당신은사용자가제시한질문에답변하는친절한도우미입니다.
다음은이태스크를해결하는예시입니다:
Figure 2: System Prompt(Korean)
You are a helpful assistant that will answer the questions given by the user.
Here is an example of solving the task:
Figure 3: System Prompt(English)
살인자는반드시세가지조건을충족해야합니다:
동기(피해자를죽일만한이유가있는가), 수단(범행도구에접근할수있는가), 기회(범행현
장에접근할수있었는가)
무고한용의자는이세가지중두가지까지만입증될수있으며, 의심스러운행동을보일수는
있어도세가지조건을모두갖추지는않습니다. 만약두용의자모두수단, 동기, 기회를가진
것처럼보인다면, 그중에서도가장명확하게이세가지가드러난인물을선택해야합니다.
반대로, 어느누구도세가지를모두갖추지않은경우라면, 세가지조건중가장뚜렷하게
드러난인물을선택해야합니다.
Figure 4: Hint- Murder Mysteries (Korean)
The murderer needs to have a means (access to weapon), motive (reason to kill the victim), and
opportunity (access to crime scene) in order to have killed the victim. Innocent suspects may have
two of these proven, but not all three. An innocent suspect may be suspicious for some other
reason, but they will not have all of motive, means, and opportunity established.
If you believe that both suspects have motive, means, and opportunity, you should make an
educated guess pick the one for whom these are best established. If you believe that neither
suspect has all three established, then choose the suspect where these are most clearly established.
Figure 5: Hint - Murder Mysteries (English)
이야기를바탕으로, 우리는특정인물이어떤물건이어디에있다고생각하고있는지를파악
하려고합니다.
이를위해서는이야기읽으며각인물이그물건의위치를시점별로어떻게인식하고있는지
를추적해야합니다.
물건이옮겨질때, 인물이그장면을직접보았거나, 옮겨진위치를인지할수있는상태였다면
그들은물건이옮겨진위치를알고있다고봅니다.
하지만물건이움직일때인물이그장면을보지못했거나다른일에집중하고있었다면, 여전
히마지막으로본위치에있다고믿게됩니다.
Figure 6: Hint - Object Placements (Korean)
20

--- Page 21 ---

Based on this story, we want to identify where someone believes that a certain object is at the end
of the story. In order to do that, you need to read the story and keep track of where they think the
object is at each point. When an object is moved, the person may observe its new location if they
saw it move.
To see where an object ends up, they must be able to see the location that it moves to and not be
too distracted by what they are doing. If they do not observe the object moving, then they will still
believe it to be in the last location where they observed it.
Figure 7: Hint - Object Placements (English)
스토리를통해각사람이한가지업무에얼마나능숙한지를파악할수있습니다. 일반적으로
각사람은어떤작업에대해뛰어나거나, 보통이거나, 부족한실력을가지고있습니다. 우리는
가능한한각자의강점을최대한발휘할수있도록사람을적절한업무에배치하려고합니다.
또한, 두사람이함께맡아야하는업무가하나있으며, 이경우두사람의팀워크수준(훌륭함,
보통, 나쁨)도전체업무성과에중요한영향을미칩니다.
단, 두사람이함께일해야하는작업에서한사람이실력이부족하고, 두사람의팀워크
도좋지않다면, 다른한사람이아무리뛰어나도전체결과에는도움이되지않을수있습니다.
각기다른강점, 약점, 그리고두사람간의상호작용을고려하여, 전체과제가가장효율적으로
수행될수있도록팀원들을적절히배치해야합니다.
Figure 8: Hint - Team Allocations (Korean)
The story should allow you to determine how good each person is at a skill. Roughly, each person
is either great, acceptable, or bad at a task. We want to find an optimal assignment of people to
tasks that uses their skills as well as possible. In addition, one task will have to have two people
assigned to it. The effectiveness of their teamwork (great team, acceptable team, or bad team) also
impacts the overall quality of the assignment.
When two people need to work on a task and one is bad at it, they don’t necessarily benefit from
the other person being good, unless they work well together.
With different strengths, weaknesses, and interpersonal dynamics at play, you should allocate your
team to find the single assignment to ensure that the tasks overall are completed as effectively as
possible.
Figure 9: Hint - Team Allocations (English)
{{narrative}}
다음중살인자일가능성이가장높은사람은누구인가?
다음선택지중하나를고르세요:
1 - Choice 1
2 - Choice 2
21

--- Page 22 ---

반드시하나의선택지만고르셔야합니다.
{{If hint is given, hint will be provided here.}}
마지막에아래와같은형식으로정답을작성하세요: ’정답: X’
Figure 10: Direct Prompt Structure for Murder Mysteries (Korean)
{{narrative}}
Who is the most likely murderer?
Choose one of the following options:
1 - Choice 1
2 - Choice 2
You must pick one option.
{{If hint is given, hint will be provided here.}}
Finally, the last thing you generate should be "ANSWER: (your answer here, including the choice
number)"
Figure 11: Direct Prompt Structure for Murder Mysteries (English)
{{narrative}}
다음중살인자일가능성이가장높은사람은누구인가?
다음선택지중하나를고르세요:
1 - Choice 1
2 - Choice 2
반드시하나의선택지만고르셔야합니다. 선택하기전에, 단계별로당신의추론과정을
설명하세요.
{{If hint is given, hint will be provided here.}}
단계별로논리적인추론을마친후, 마지막에아래와같은형식으로정답을작성하세요: ’정답:
X’
Figure 12: CoT Prompt Structure for Murder Mysteries (Korean)
{{narrative}}
Who is the most likely murderer?
22

--- Page 23 ---

Choose one of the following options:
1 - Choice 1
2 - Choice 2
You must pick one option. Before selecting a choice, explain your reasoning step by step.
{{If hint is given, hint will be provided here.}}
Explain your reasoning step by step before you answer. Finally, the last thing you generate should
be "ANSWER: (your answer here, including the choice number)"
Figure 13: CoT Prompt Structure for Murder Mysteries (English)
{{narrative}}
주어진이야기를고려할때, {character}는{object}을찾기위해어디를가장먼저확인하겠는
가?
{{If hint is given, hint will be provided here.}}
다음선택지중하나를고르세요:
1 - Choice 1
2 - Choice 2
3 - Choice 3
4 - Choice 4
반드시하나의보기를선택해야합니다. 마지막에다음형식으로정답을출력하세요: ’정답:
X’
Figure 14: Direct Prompt Structure for Object Placements (Korean)
{{narrative}}
Which location is the most likely place {character} would look to find the {object} given the story?
{{If hint is given, hint will be provided here.}}
Choose one of the following options:
1 - Choice 1
2 - Choice 2
3 - Choice 3
4 - Choice 4
You must pick one option. Finally, the last thing you generate should be "ANSWER: (your answer
here, include the choice number)"
Figure 15: Direct Prompt Structure for Object Placements (English)
23

--- Page 24 ---

{{narrative}}
주어진이야기를고려할때, {character}는{object}을찾기위해어디를가장먼저확인하겠는
가?
{{If hint is given, hint will be provided here.}}
다음선택지중하나를고르세요:
1 - Choice 1
2 - Choice 2
3 - Choice 3
4 - Choice 4
반드시하나의보기를선택해야합니다. 추론과정을단계별로설명한후, 마지막에다음형식
으로정답을출력하세요: ’정답: X’
Figure 16: CoT Prompt Structure for Object Placements (Korean)
{{narrative}}
Which location is the most likely place {character} would look to find the {object} given the story?
{{If hint is given, hint will be provided here.}}
Choose one of the following options:
1 - Choice 1
2 - Choice 2
3 - Choice 3
4 - Choice 4
You must pick one option. Explain your reasoning step by step, then output the answer in the form
’ANSWER: X’
Figure 17: CoT Prompt Structure for Object Placements (English)
{{narrative}}
이이야기를바탕으로, 두가지업무가모두효율적으로수행되도록사람을어떻게배정하시
겠습니까?
다음선택지중하나를고르세요:
1 - Choice 1
2 - Choice 2
3 - Choice 3
당신은세가지중하나의선택지를골라야합니다.
{{If hint is given, hint will be provided here.}}
24

--- Page 25 ---

마지막에는아래형식으로답변을마무리해주세요: "정답: (당신의선택, 번호포함)"
Figure 18: Direct Prompt Structure for Team Allocations (Korean)
{{narrative}}
Given the story, how would you uniquely allocate each person to make sure both tasks are
accomplished efficiently?
Choose one of the following options:
1 - Choice 1
2 - Choice 2
3 - Choice 3
You must pick one option.
{{If hint is given, hint will be provided here.}}
Finally, the last thing you generate should be "ANSWER: (your answer here, including the choice
number)"
Figure 19: Direct Prompt Structure for Team Allocations (English)
{{narrative}}
이이야기를바탕으로, 두가지업무가모두효율적으로수행되도록사람을어떻게배정하시
겠습니까?
다음선택지중하나를고르세요:
1 - Choice 1
2 - Choice 2
3 - Choice 3
당신은세가지중하나의선택지를골라야합니다.
{{If hint is given, hint will be provided here.}}
당신의풀이과정을단계별로설명한뒤, 마지막에는아래형식으로답변을마무리해주세요:
"정답: (당신의선택, 번호포함)"
Figure 20: CoT Prompt Structure for Team Allocations (Korean)
{{narrative}}
Given the story, how would you uniquely allocate each person to make sure both tasks are
accomplished efficiently?
25

--- Page 26 ---

Choose one of the following options:
1 - Choice 1
2 - Choice 2
3 - Choice 3
You must pick one option.
{{If hint is given, hint will be provided here.}}
Explain your reasoning step by step before you answer. Finally, the last thing you generate should
be "ANSWER: (your answer here, including the choice number)"
Figure 21: CoT Prompt Structure for Team Allocations (English)
당신의임무는예시에제시된방식으로이야기를위한논리트리를생성하는것입니다.
이트리에서는각사실이자신의자식노드로부터논리적으로도출되어야합니다.
이미이름이있는사실(루트노드등)이있을경우, 새롭게덮어쓰지말아야합니다.
이야기의종류:
우리는살인미스터리를만들고있습니다. 살인미스터리에는용의자가살인을저지를수
있는’범행수단, 범행동기, 범행기회’가뒤얽힌복잡한증거망이필요합니다.
이야기는형사의시점에서쓰여야합니다. 증거를모으는과정은보통의수사방식(심문, 대화
엿듣기, 범죄기록조회, 우편물· 쓰레기조사등)을통해이뤄집니다.
1. 트리에등장하는각사실은자식노드로부터논리적으로도출되어야합니다.
2. 모든"스토리에서추출된사실" 노드와"상식" 노드는, 결과적으로만들어지는추론에
밀접하게관련되어야합니다.
3. 각루트사실(root fact)에는출처가표시됩니다("스토리에서추출된사실" 혹은"상식").
4. "스토리에서추출된사실"은이야기속캐릭터, 장소, 물건에대한구체적진술이어야
합니다.
5. "상식"은대부분의사람이알고동의할만한사실이어야합니다. 이야기속특정인물이나
사건을직접적으로언급하면안됩니다.
6. "상식"은형식상’규칙(rule)’ 역할을하며, 형제노드의사실을결합해상위사실을
도출하는용도로사용됩니다.
7. 생성되는트리는’완성해야할함의추론’의트리구조와일치해야합니다.
8. ’완성해야할함의추론’ 트리의"스토리에서추출된사실" 요청과"상식"에대해한개씩의
노드를생성해야합니다.
9. ’완성해야할함의추론’ 트리에서요청되지않은"스토리에서추출된사실"이나"상식"
노드를생성하지마세요.
용의자가’범행수단’을가졌다는것은살해도구에접근할수있음을의미합니다.
용의자가’범행동기’를가졌다는것은그(또는그녀)가피해자를죽일이유가있음을
의미합니다.
용의자가’범행기회’를가졌다는것은범행현장에있었음을의미합니다.
설령황당하거나비현실적인설정의부모노드사실이라도, 그사실을유지하고논리트리를
구성해야합니다.
26

--- Page 27 ---

예제를확인하세요.
시나리오:
피해자: 유리
범행장소: 집
살해도구: 총
용의자: 민수
용의자의역할: 형제
범행동기: 금전적이익
현재트리:
민수는살인자다. | 추론된결론
> 민수는범행수단이있다. | 추론된사실
> > 민수는총쏘는연습을했다. | 스토리에서추출된사실
> > 민수는총을소유하고있다. | 스토리에서추출된사실
> > 총을소유하고있으며사용법을연습했다면, 살인을저지를능력이있다. | 상식
> 민수는범행동기가있다. | 추론된사실
> > 민수는극도로돈에절박했다. | 스토리에서추출된사실
> > 민수는유리의돈에극도로절박했다. | 스토리에서추출된사실
> > 누군가가극도로절박할때, 목표를이루기위해극단적인방법을사용할수있으며,
여기에는살인도포함될수있다. | 상식
> 민수는범행기회가있다. | 스토리에서추출된사실
완성해야할함의추론:
민수는범행기회가있다.
> 스토리에서추출된사실
> 상식
출력:
민수는범행기회가있다.
> 민수는유리의집에출입할수있다. | 스토리에서추출된사실
> 누군가의집에출입할수있다는것은그들을살해할범행기회를제공한다. | 상식
또다른예제입니다.
시나리오:
피해자: 철수
범행장소: 경마장
살해도구: 삽
용의자: 지민
용의자의역할: 러닝파트너
범행동기: 다른사람에게해가가는것을막기위해
현재트리:
지민이는살인자다. | 추론된결론
> 지민이는범행수단이있다. | 추론된사실
> > 지민이는농부다| 스토리에서추출된사실
> > 농부들은일반적으로삽과같은원예도구를사용한다. | 상식
> 지민이는범행동기가있다. | 스토리에서추출된사실
27

--- Page 28 ---

> 지민이는범행기회가있다. | 스토리에서추출된사실
완성해야할함의추론:
지민이는범행동기가있다.
> 스토리에서추출된사실
> 스토리에서추출된사실
> 상식
출력:
지민이는범행동기가있다.
> 지민이는민수를깊이사랑한다. | 스토리에서추출된사실
> 철수는민수를위협했다. | 스토리에서추출된사실
> 깊고강렬한사랑은사랑하는사람이위협받을때극단적인행동, 심지어살인까지저지르게
할수있다. | 상식
또다른예제입니다.
시나리오:
피해자: 준호
범행장소: 공원벤치
살해도구: 헤로인과다복용
용의자: 민철
용의자의역할: 마약사용자
범행동기: 공개적인굴욕
현재트리:
민철이는살인자다. | 추론된결론
> 민철이는범행수단이있다. | 스토리에서추출된사실
> 민철이는범행동기가있다. | 스토리에서추출된사실
> 민철이는범행기회가있다. | 스토리에서추출된사실
완성해야할함의추론:
민철이는범행수단이있다.
> 스토리에서추출된사실
> 스토리에서추출된사실
> 상식
출력:
민철이는범행수단이있다.
> 민철이는헤로인에접근할수있다. | 스토리에서추출된사실
> 민철이는헤로인과다복용에필요한양을알고있다. | 스토리에서추출된사실
> 헤로인에접근할수있고, 치명적인양을알고있다면, 피해자에게의도적으로치명적인
용량을투여하여살인을저지를수있다. | 상식
이제당신의차례입니다.
시나리오:
피해자: 영은
범행장소: 자동차
살해도구: 고기손질용도끼(미트클리버)
28

--- Page 29 ---

용의자: 예성
용의자의역할: 목수
범행동기: 병적인집착
현재트리:
예성| 추론된결론
> 예성이는범행수단이있다. | 추론된사실
> > 예성이는평소에고기를손질할때도끼를사용한다. | 추론된사실
> > > 예성은육류손질을위해고기손질용도끼를사용한다. | 추론된사실
> > > > 예성은정기적으로육류를요리한다. | 스토리에서추출된사실
> > > > 예성은고기손질용도끼를소유하고있다. | 스토리에서추출된사실
> > > > 고기를요리하는사람들은종종특정한도구를사용하여고기를손질한다. | 상식
> > > 예성은주방에서고기요리를자주한다. | 추론된사실
> > > > 예성은고기손질용도끼를소유하고있다. | 스토리에서추출된사실
> > > > 예성은정기적으로육류를요리한다. | 스토리에서추출된사실
> > > > 고기를요리하는사람들은종종특정한도구를사용하여고기를손질한다. | 상식
> > > 고기를자주요리하는사람들은적절한도구를사용하여고기를손질하려고한다. |
상식
> > 예성이는목수로서다양한도구를소유하고있다. | 추론된사실
> > > 예성은다양한목공도구를가지고있다. | 추론된사실
> > > > 예성은작업을위해정기적으로도구를점검하고유지보수한다. | 스토리에서추출된
사실
> > > > 예성은목수로일하며자주작업공간을정돈한다. | 스토리에서추출된사실
> > > > 목수들은일반적으로작업을원활하게하기위해다양한도구를갖추고있다. | 상식
> > > 예성은목공작업을주기적으로한다. | 추론된사실
> > > > 예성은목수로일하며자주작업공간을정돈한다. | 스토리에서추출된사실
> > > > 예성은작업을위해정기적으로도구를점검하고유지보수한다. | 스토리에서추출된
사실
> > > > 목공작업을하는사람들은작업에필요한다양한도구를소유하고있는경향이있다.
| 상식
> > > 목공작업을하는사람들은작업에필요한다양한도구를소유하고있는경향이있다. |
상식
> > 목수라면다양한도구를쉽게구할수있으며, 고기손질용도끼를소유하고있다면이를
범행에사용할수있다. | 상식
> 예성이는범행기회가있다. | 추론된사실
> > 영은과예성은같은동네에거주한다. | 추론된사실
> > > 예성은동네공원에서영은과함께산책을즐겼다. | 추론된사실
> > > > 예성은영은이참여하는동네주민모임에자주참석했다. | 스토리에서추출된사실
> > > > 예성은동네공원에서영은과함께산책을즐겼다. | 스토리에서추출된사실
> > > > 동일한사회활동과장소에서자주만나는사람들은같은동네에거주할가능성이
높다. | 상식
> > > 영은은동네의주민모임에서예성을자주만났다. | 추론된사실
> > > > 예성은동네공원에서영은과함께산책을즐겼다. | 스토리에서추출된사실
> > > > 예성은영은이참여하는동네주민모임에자주참석했다. | 스토리에서추출된사실
> > > > 동일한사회활동과장소에서자주만나는사람들은같은동네에거주할가능성이
높다. | 상식
> > > 동일한사회활동과장소에서자주만나는사람들은같은동네에거주할가능성이높다.
| 상식
> > 예성은최근에자주영은의차를수리해주었다. | 추론된사실
> > > 예성은기계에익숙한목수로서차량수리에능숙하다. | 추론된사실
29

--- Page 30 ---

> > > 예성은영은이차량문제로자주도움을요청했다고말했다. | 추론된사실
> > > 이웃이차량문제로도움을요청하여자주수리를해주면, 그차량에접근할기회를
가지게된다. | 상식
> > 같은동네에살면서자주차를수리해줬다면, 자연스럽게차에접근할기회를가질수
있다. | 상식
> 예성이는범행동기가있다. | 추론된사실
완성해야할함의추론:
예성
> 예성이는범행기회가있다. 왜냐하면,
> > 예성은최근에자주영은의차를수리해주었다. 왜냐하면,
> > > 예성은기계에익숙한목수로서차량수리에능숙하다. 왜냐하면,
> > > > 스토리에서추출된사실
> > > > 스토리에서추출된사실
> > > > 상식
’완성해야할함의추론’은’현재트리’의일부입니다. ’완성해야할함의추론’에대해서만,
정확한개수의’스토리에서추출된사실’과’상식’를생성하세요.
Figure 22: Prompts for Narrative Generation - Murder Mysteries
Your task is to generate a reasoning tree for a story following the example provided.
In this tree, each statement must be logically derived from its child nodes.
If a statement already exists (e.g., a root node), do not overwrite it.
Story type:
We are creating a murder mystery. A murder mystery requires a complex web of evidence
entangled with a suspect’s means, motive, and opportunity.
The story must be written from the detective’s point of view. Evidence collection should follow
ordinary investigative methods (e.g., interrogations, overheard conversations, criminal record
searches, mail or trash examination, etc.).
1. Every statement in the tree must be logically derived from its child nodes.
2. All “Fact from Story” and “Commonsense Knowledge” nodes must be directly related to the
final inferred reasoning.
3. Each root statement must specify its source (“Fact from Story” or “Commonsense Knowledge”).
4. “Fact from Story” must be a concrete statement about characters, locations, or objects in the
narrative.
5. “Commonsense Knowledge” must represent facts most people would agree with and must not
directly reference specific people or events in the story.
6. “Commonsense Knowledge” acts as a rule combining sibling nodes to derive higher-level
conclusions.
7. The generated tree must match the structure of the “Reasoning to be Completed.”
8. For each “Fact from Story” and “Commonsense Knowledge” requested in the “Reasoning to be
Completed,” generate exactly one node of each type.
9. Do not generate any additional “Fact from Story” or “Commonsense Knowledge” nodes not
requested in the “Reasoning to be Completed.”
30

--- Page 31 ---

Having a means implies access to the murder weapon.
Having a motive implies a reason to kill the victim.
Having an opportunity implies being present at the crime scene.
Even if a parent statement appears unrealistic or implausible, you must preserve it and construct
the reasoning tree accordingly.
See the examples below.
Scenario:
Victim: Yuri
Crime Scene: House
Murder Weapon: Gun
Suspect: Minsu
Suspect’s Role: Brother
Motive: Financial gain
Current tree:
Minsu is the murderer. | Deduced Root Conclusion
> Minsu has a means. | Deduced Fact
> > Minsu practiced shooting. | Fact from Story
> > Minsu owns a gun. | Fact from Story
> > If someone owns a gun and has practiced using it, they have the ability to commit murder. |
Commonsense Knowledge
> Minsu has a motive. | Deduced Fact
> > Minsu was extremely desperate for money. | Fact from Story
> > Minsu was desperate for Yuri’s money. | Fact from Story
> > When someone is desperate, they may resort to extreme actions—including murder—to
achieve their goal. | Commonsense Knowledge
> Minsu has an opportunity. | Fact from Story
Reasoning to be completed:
Minsu has an opportunity.
> Fact from Story
> Commonsense Knowledge
Output:
Minsu has an opportunity.
> Minsu had access to Yuri’s house. | Fact from Story
> Having access to someone’s house provides an opportunity to commit murder. | Commonsense
Knowledge
Another example:
Scenario:
Victim: Chulsoo
Crime Scene: Racetrack
Murder Weapon: Shovel
Suspect: Jimin
Suspect’s Role: Running partner
31

--- Page 32 ---

Motive: To prevent harm to another person
Current tree:
Jimin is the murderer. | Deduced Root Conclusion
> Jimin has a means. | Deduced Fact
> > Jimin is a farmer. | Fact from Story
> > Farmers typically use gardening tools such as shovels. | Commonsense Knowledge
> Jimin has a motive. | Fact from Story
> Jimin has an opportunity. | Fact from Story
Reasoning to be completed:
Jimin has a motive.
> Fact from Story
> Fact from Story
> Commonsense Knowledge
Output:
Jimin has a motive.
> Jimin deeply loves Minsu. | Fact from Story
> Chulsoo threatened Minsu. | Fact from Story
> Deep, passionate love can drive a person to extreme actions—even murder—when a loved one
is threatened. | Commonsense Knowledge
Another example:
Scenario:
Victim: Junho
Crime Scene: Park bench
Murder Weapon: Heroin overdose
Suspect: Minchul
Suspect’s Role: Drug user
Motive: Public humiliation
Current tree:
Minchul is the murderer. | Deduced Root Conclusion
> Minchul has a means. | Fact from Story
> Minchul has a motive. | Fact from Story
> Minchul has an opportunity. | Fact from Story
Reasoning to be completed:
Minchul has a means.
> Fact from Story
> Fact from Story
> Commonsense Knowledge
Output:
Minchul has a means.
> Minchul had access to heroin. | Fact from Story
> Minchul knew the lethal dosage for overdose. | Fact from Story
> If someone has access to heroin and knows the lethal dosage, they can intentionally administer a
fatal dose to commit murder. | Commonsense Knowledge
32

--- Page 33 ---

Now it’s your turn.
Scenario:
Victim: Yeong-eun
Crime Scene: Car
Murder Weapon: Meat cleaver
Suspect: Yesung
Suspect’s Role: Carpenter
Motive: Pathological obsession
Current tree:
Yesung | Deduced Root Conclusion
> Yesung has a means. | Deduced Fact
> > Yesung often uses a meat cleaver when preparing meat. | Deduced Fact
> > > Yesung uses a cleaver for meat preparation. | Deduced Fact
> > > > Yesung regularly cooks meat. | Fact from Story
> > > > Yesung owns a meat cleaver. | Fact from Story
> > > > People who cook meat often use specific tools for cutting it. | Commonsense Knowledge
> > > Yesung frequently cooks meat in the kitchen. | Deduced Fact
> > > > Yesung owns a meat cleaver. | Fact from Story
> > > > Yesung regularly cooks meat. | Fact from Story
> > > > People who cook meat often use specific tools for preparation. | Commonsense Knowledge
> > > People who frequently cook meat tend to use appropriate tools for cutting it. | Commonsense
Knowledge
> > Yesung, as a carpenter, owns various tools. | Deduced Fact
> > > Yesung possesses various woodworking tools. | Deduced Fact
> > > > Yesung regularly inspects and maintains his tools for work. | Fact from Story
> > > > Yesung, who works as a carpenter, often organizes his workspace. | Fact from Story
> > > > Carpenters generally possess various tools to perform their work efficiently. | Common-
sense Knowledge
> > > Yesung regularly engages in woodworking. | Deduced Fact
> > > > Yesung, who works as a carpenter, often organizes his workspace. | Fact from Story
> > > > Yesung regularly inspects and maintains his tools for work. | Fact from Story
> > > > People who do woodworking typically own a variety of necessary tools. | Commonsense
Knowledge
> > > People who do woodworking generally possess the necessary tools for their craft. |
Commonsense Knowledge
> > Being a carpenter allows easy access to various tools, and owning a cleaver means he could
use it in the crime. | Commonsense Knowledge
> Yesung has an opportunity. | Deduced Fact
> > Yeong-eun and Yesung live in the same neighborhood. | Deduced Fact
> > > Yesung enjoyed walking with Yeong-eun in the neighborhood park. | Deduced Fact
> > > > Yesung frequently attended community meetings that Yeong-eun also joined. | Fact from
Story
> > > > Yesung enjoyed walking with Yeong-eun in the neighborhood park. | Fact from Story
> > > > People who frequently meet in the same social activities and places are likely to live in
the same neighborhood. | Commonsense Knowledge
> > > Yeong-eun often met Yesung at local gatherings. | Deduced Fact
> > > > Yesung enjoyed walking with Yeong-eun in the neighborhood park. | Fact from Story
33

--- Page 34 ---

> > > > Yesung frequently attended community meetings that Yeong-eun also joined. | Fact from
Story
> > > > People who frequently meet through social activities and shared spaces tend to live nearby.
| Commonsense Knowledge
> > > People who meet often in similar places and contexts usually live close to each other. |
Commonsense Knowledge
> > Yesung recently repaired Yeong-eun’s car multiple times. | Deduced Fact
> > > As a mechanically skilled carpenter, Yesung is good at vehicle repair. | Deduced Fact
> > > Yeong-eun frequently asked for Yesung’s help with car issues. | Deduced Fact
> > > When a neighbor frequently helps repair someone’s car, they naturally gain access to it. |
Commonsense Knowledge
> > Living nearby and frequently repairing the car naturally gives access to it. | Commonsense
Knowledge
> Yesung has a motive. | Deduced Fact
Reasoning to be completed:
Yesung
> Yesung has an opportunity because
> > Yesung recently repaired Yeong-eun’s car multiple times, because
> > > Yesung is a mechanically skilled carpenter proficient at vehicle repair, because
> > > > Fact from Story
> > > > Fact from Story
> > > > Commonsense Knowledge
The “Reasoning to be Completed” is part of the “Current Tree.” For this section only, generate the
exact number of “Fact from Story” and “Commonsense Knowledge” nodes requested.
Figure 23: Prompts for Narrative Generation - Murder Mysteries (Translated)
우리는살인미스터리를만들고있습니다.
살인미스터리에는용의자와관련된복잡한증거들이필요합니다.
이야기는형사의시점에서쓰여야합니다.
형사는통상적인수사방식을통해증거를수집합니다(심문, 대화엿듣기, 범죄기록조사,
우편물· 쓰레기뒤지기등).
당신에게사실목록을제공할것이고, 당신은이목록에있는사실들을모두이야기에
포함시켜야합니다.
절대유도된사실(추론된사실)이나결론을언급해서는안됩니다. 이야기의흐름은이
사실들을충실히따라가야합니다.
다음은살인미스터리에서용의자와관련된한장(chapter)을작성해야합니다.
이장에서는살인사건이나피해자에관한직접적인언급을최소화하고,
형사가용의자에게접근하여수사를진행하는과정을그립니다.
아래규칙을유의하세요:
1. 장의내용만작성하고, 제목이나번호를달지마세요. 다른장과연속적으로이어질수
있도록간단한서술만하세요.
2. 용의자가’범행수단을가졌다’, ’범행동기를가졌다’, ’범행기회가있다’라고절대말하지
34

--- Page 35 ---

마세요.
3. 용의자에게범행수단, 범행동기, 범행기회가있다고암시조차하지마세요.
4. 유도된사실(추론된사실)을직접적으로언급하거나결론짓지마세요.
5. 용의자를살인자로단정지어서말하지마세요. 그건독자가추리해야할부분입니다.
6. 이야기의시점은형사가현장조사를하거나용의자를심문하는등, 일반적으로합리적인
수사방식을통해단서를얻는상황으로유지하세요.
7. 이야기속에서’이사실은의심스러워’ 같은멘트를하지마세요. 독자가추론하게남겨두
세요.
8. 이야기속에서형사의이름은’김철수’로통일하세요.
주어진사실(fact) 목록에서각사실을이야기속에반드시등장시키고,
최대10개의대사를포함해작성하세요.
다음은예시입니다:
용의자와범죄정보
피해자: 유진
범행장소: 인적이드문숲
살해도구: 칼
용의자: 지훈
용의자의역할: 학교운동장관리인
범행동기: 종교적희생
당신은김철수형사입니다.
반드시포함해야할사실들:
- 어떤목격자는스파게티얼굴과초록색귀를가진누군가를보았다
- 지훈이는지역학교의잔디관리인이다
- 지훈이는근처주민들에게페인트칠, 잔디손질등서비스를제공한다
- 지훈이는주변집중한곳을초록색으로페인트칠했다
- 지훈이는어렸을때큰화상을입었다
- 지훈이의가족은여러세대동안이지역에살았다
- 이지역에서는예전부터종교적극단주의자들이있었고, 모두신비로운종교의식을치렀다
- 지훈이와그의직계가족들은모두잡다한기술을가지고있었다
- 지훈이는조상과전통을존중하는신념을갖고있다
- 유진이는근처에있는새로운교회에참여할생각을적어두었다
- 유진이의친구는유진이가새로사귀게된불량스러운무리와어울리는것을걱정했다
출력예시:
김철수형사는범행현장사진을훑어보면서담배를길게한모금빨았다. 그는끔찍한
장면들에어느정도익숙해져있었지만, 유진이의사건에는이상하게마음이쏠렸다...
(중략: 예시이야기)
—
이제당신차례입니다. 이야기외에는아무것도출력하지마세요.
용의자와범죄정보
피해자: 영은
35

--- Page 36 ---

범행장소: 자동차
살해도구: 고기손질용도끼(미트클리버)
용의자: 예성
용의자의역할: 목수
범행동기: 병적인집착
당신은김철수형사입니다.
반드시포함해야할사실들:
- 예성은영은이차량문제로자주도움을요청했다고말했다.
- 예성은영은이새로운스포츠클럽에가입한후다른사람들과함께시간을보내는것을
좋아하지않았다.
- 예성은영은이가는모든곳을따라다녔다.
- 예성은영은이참여하는동네주민모임에자주참석했다.
- 예성은동네공원에서영은과함께산책을즐겼다.
- 예성은매일저녁마다영은과함께시간을보내려했다.
- 예성은영은의사회적미디어활동을지속적으로체크했다.
- 예성은목수로일하며자주작업공간을정돈한다.
- 영은이다른약속이있을때마다예성은심한불안을느꼈다.
- 예성은이웃들에게친절한목수로알려져있다.
- 예성은목수로서손재주가뛰어나다.
- 예성은정기적으로육류를요리한다.
- 영은은새로운스포츠클럽에가입했다.
- 예성은영은과의개인적인시간을중요시했고, 그녀가점점더많은사회적활동에빠져드는
것을불편해했다.
- 예성은정기적으로육류를요리한다.
- 그스포츠클럽은많은사회적인활동과모임을제공한다.
- 영은의차량은최근잦은고장을겪었다.
- 예성은영은이참여하는동네주민모임에자주참석했다.
- 예성은동네공원에서영은과함께산책을즐겼다.
- 예성은고기손질용도끼를소유하고있다.
- 예성은고기손질용도끼를소유하고있다.
- 예성은작업을위해정기적으로도구를점검하고유지보수한다.
Figure 24: Prompts for Narrative Generation - Murder Mysteries
We are creating a murder mystery.
A murder mystery requires a web of complex evidence related to the suspects.
The story must be written from the perspective of a detective.
The detective gathers evidence through standard investigative methods (interrogation, eavesdrop-
ping, checking criminal records, examining mail or trash, etc.).
You will be provided with a list of facts, and you must include all of these facts in the story.
You must not mention any inferred (deduced) facts or conclusions. The flow of the story must
faithfully follow only the given facts.
You are to write a chapter in the murder mystery related to the suspect.
This chapter should minimize direct references to the murder or the victim,
36

--- Page 37 ---

and instead depict the detective approaching and investigating the suspect.
Please follow the rules below:
1. Write only the chapter content—do not add titles or numbers. Keep it simple so that it can
connect naturally with other chapters.
2. Never say that the suspect “has a means,” “has a motive,” or “has an opportunity” to commit
the crime.
3. Do not even imply that the suspect has a means, motive, or opportunity.
4. Do not explicitly mention or conclude any inferred (deduced) facts.
5. Do not state or imply that the suspect is the murderer. That is for the reader to infer.
6. The story’s perspective should stay consistent with reasonable investigative methods—detective
Kim Cheolsu examining the scene, interrogating the suspect, etc.
7. Do not include remarks like “This is suspicious.” Leave that for the reader to deduce.
8. The detective’s name must always be “Kim Cheolsu.”
Each fact from the given list must appear in the story,
and you may include up to 10 dialogue lines.
Example:
Suspect and Crime Information
Victim: Yujin
Crime Scene: Secluded forest
Murder Weapon: Knife
Suspect: Jihoon
Suspect’s Role: School field manager
Motive: Religious sacrifice
You are Detective Kim Cheolsu.
Facts that must be included:
- A witness saw someone with a spaghetti face and green ears.
- Jihoon is a grass caretaker at the local school.
- Jihoon provides services like painting and lawn care to nearby residents.
- Jihoon painted one of the neighborhood houses green.
- Jihoon suffered severe burns as a child.
- Jihoon’s family has lived in this area for generations.
- The region has a long history of religious extremists who practiced mysterious rituals.
- Jihoon and his direct family members are all skilled in various crafts.
- Jihoon holds strong beliefs about respecting his ancestors and traditions.
- Yujin had written about joining a new church nearby.
- Yujin’s friend was worried about her hanging out with a new, troublesome crowd.
Example Output:
Detective Kim Cheolsu took a long drag on his cigarette as he looked over the photos from the
crime scene. He had seen his share of gruesome cases, but something about Yujin’s case drew his
attention...
(omitted: example narrative)
37

--- Page 38 ---

—
Now it’s your turn. Output only the story—nothing else.
Suspect and Crime Information
Victim: Yeongeun
Crime Scene: Car
Murder Weapon: Meat cleaver
Suspect: Yeseong
Suspect’s Role: Carpenter
Motive: Pathological obsession
You are Detective Kim Cheolsu.
Facts that must be included:
- Yeseong said that Yeongeun often asked him for help with car troubles.
- Yeseong disliked that Yeongeun enjoyed spending time with others after joining a new sports
club.
- Yeseong followed Yeongeun everywhere she went.
- Yeseong frequently attended the neighborhood meetings that Yeongeun joined.
- Yeseong enjoyed walking with Yeongeun in the local park.
- Yeseong tried to spend every evening with Yeongeun.
- Yeseong constantly checked Yeongeun’s social media activities.
- Yeseong works as a carpenter and often organizes his workspace.
- Whenever Yeongeun had other plans, Yeseong felt intense anxiety.
- Yeseong is known in the neighborhood as a kind carpenter.
- Yeseong is highly skilled at his craft as a carpenter.
- Yeseong regularly cooks meat.
- Yeongeun joined a new sports club.
- Yeseong valued his personal time with Yeongeun and felt uneasy about her increasing social
activities.
- Yeseong regularly cooks meat.
- The sports club hosts many social gatherings and events.
- Yeongeun’s car has recently been breaking down frequently.
- Yeseong often attended the same neighborhood meetings as Yeongeun.
- Yeseong enjoyed walking with Yeongeun in the local park.
- Yeseong owns a meat cleaver.
- Yeseong owns a meat cleaver.
- Yeseong routinely inspects and maintains his tools for work.
Figure 25: Prompts for Narrative Generation - Murder Mysteries (Translated)
우리는사람들이많은아이템들을여러번옮기는이야기를만들고있습니다. 이이야기의
목표는흥미롭고독창적이면서도, 물건이어디에있는지를명확하게추적할수있도록하여,
나중에독자나언어모델에게세계상태나누가무엇을알고있는지에대해질문할수있도록
하는것입니다.
이이야기를만들기위해, 우리는이야기전개와세계상태의변화를개요화한트리구조를
만들었습니다. 당신의역할은누군가가어떤사건을보았는지또는보지못했는지를증명하는
38

--- Page 39 ---

포함추론트리를완성하는것입니다.
논리트리는중간노드들이자식노드들에의해포함되는트리구조입니다. 이들은사실들의
집합에대해자연어로된추론증명을만듭니다.
이트리를완성하기위해서는하나의함의추론을완성해야합니다. 함의추론을완성하는
것은논리추론트리의한서브트리를채우는것과유사합니다. 이단계를채우기위해서는
단계의구조를따라야합니다.
"스토리에서추출된사실"는우리가이야기를쓸때명시적으로서술될사실들입니다.
"상식"는대부분의사람들이사실로받아들이는, 명시적으로말할필요가없는사실들입니다.
"복합사실"는이야기에서의더단순한사실들에의해함의사실들입니다(이들은나중에
재귀호출을통해채워질것입니다!)
이단계의모든사실은결합되어루트상위사실을포함해야합니다.
현재의구조트리와모순되는사실은포함할수없습니다.
다른사람들에대한사실은포함하지마세요. 무언가가움직이는것을보고있는지여부에
대한그사람에대한사실에만집중하세요.
’완성해야할함의추론’과정확히일치하게작성하세요. 스토리에서추출된사실와상식의
개수도동일하게작성하고, 순서도그대로따라야합니다.
누군가가어떤것을보았거나보지못했다고명시적으로말하지마세요. 당신의역할은이를
암시하는사실들을제공하는것입니다. 예를들어, 지수가철수가무언가를옮기는것을
보았다고암시하고싶다면, "지수는집안일을하면서철수를보고있었다" 그리고"누군가를
보고있다면, 그사람이무엇을하고있는지를보는것이다"라고말할수있습니다. 누군가가
본사실을직접적으로말하지않고, 보는행위의물리적조건을설명하는방식입니다.
아이템이움직였다는사실을언급하거나이미등장한아이템을재사용하지마세요. 예를
들어, "철수가자신의아이폰을보지못했다"라는사실이있고, 당신이"유림이는사과가
움직이는것을보지못했다"를증명하고있다면, 철수의아이폰을다시사용하지마세요.
우리프로그램은아이템이어디에있는지를엄격하게제어하고있으며, 우리가고려하지
않은아이템배치를도입하는것을원하지않습니다.
각사실은추론을위해결정적이어야합니다. 일부러세부사항을생략하여다른사실들이
이를보완하도록하세요. 하나의사실이빠지면결론이도출되지않아야합니다. 같은사실을
반복해서사용하지마세요.
"그"나"그녀" 같은대명사대신항상사람의이름을사용하세요. 이름을알고있다면반드시
이름을사용하세요.
한번에하나의추론만수행하세요. 당신의추론은반드시"완성해야할함의추론" 템플릿과
정확히일치해야하며, 우리가나중에이를파싱할수있어야합니다.
예제를확인하세요.
시나리오:
민수와예림이는노래방에있다.
39

--- Page 40 ---

현재트리:
민수와예림이는노래방에있다. | 추론된결론
> 오프닝장면| 추론된사실
> > 민수는무대에있는마이크를보았다. | 스토리에서추출된사실
> > 예림이는무대에있는마이크를보았다. | 스토리에서추출된사실
> > 민수는바에있는맥주를보았다. | 스토리에서추출된사실
> > 예림이는바에있는맥주를보았다. | 스토리에서추출된사실
> 민수는맥주를테이블로옮긴다. | 추론된사실
> > 에림이는맥주가테이블로옮겨지는것을보지못했다. | 추론된사실
> > > 예림이는테이블에서반대쪽을보고있었다. | 추론된사실
> > > > 예림이는다른손님과대화중이었다. | 스토리에서추출된사실
> > > > 다른손님은테이블쪽을보고있었다. | 스토리에서추출된사실
> > > > 보통사람들은서로를바라보며대화하기때문에, 한사람이한방향을보고있으면
다른사람은반대방향을보고있게된다. | 상식
> > > 만약누군가다른무언가에서반대방향을보고있다면, 그무언가주변에서일어나는
일을볼수없다. | 상식
> 예림이는마이크를테이블로옮긴다| 추론된사실
> > 예림이는마이크를옮길때테이블에있는맥주를보았다. | 스토리에서추출된사실
> > 민수는마이크가테이블로옮겨지는것을보았다. | 추론된사실
> > > 민수는테이블에서맥주를마시고있었다. | 상식
> > > 어떤일이사람바로옆에서일어나면, 그사람은보통그상황을볼수있다. | 스토리에서
추출된사실
> 예림이는맥주를쓰레기통으로옮긴다. | 추론된사실
> > 민수는맥주가쓰레기통으로옮겨지는것을보지못했다. | 스토리에서추출된사실
완성해야할함의추론:
민수와예림이는노래방에있다.
> 예림이는맥주를쓰레기통으로옮긴다. 왜냐하면, 이야야기에따르면,
> > 민수는맥주가쓰레기통으로옮겨지는것을보지못했다. 왜냐하면, 이야야기에따르면,
> > > 스토리에서추출된사실
> > > 스토리에서추출된사실
> > > 상식
출력:
민수와예림이는노래방에있다.
> 예림이는맥주를쓰레기통으로옮긴다. 왜냐하면, 이야야기에따르면,
> > 민수는맥주가쓰레기통으로옮겨지는것을보지못했다. 왜냐하면, 이야야기에따르면,
> > > 예림이는민수를속여서"저쪽"을보게했다. | 스토리에서추출된사실
> > > 예림이는민수에게쓰레기통의반대방향을가리켰다. | 스토리에서추출된사실
> > > 누군가를속여서다른곳을보게만들면, 반대쪽에서일어나는일을볼수없다. | 상식
이제당신의차례입니다.
시나리오:
이야기개요:
영수는다음주제출해야할중요한프로젝트를진행중입니다. 실험결과와필요한모든
정보를USB에저장해두었으며, 이를잃어버리면큰문제가발생할것입니다. 지민은
실험실의질서를유지하면서영수가프로젝트에집중할수있도록돕습니다. 동시에은혁은
40

--- Page 41 ---

데이터의안전과보안을보장합니다.
인물1:
이름: 영수
역할: 연구원
동기: 영수는중요한프로젝트를제시간에제출하기위해모든자료를USB에저장하고
안전하게보관하고자합니다.
인물2:
이름: 지민
역할: 연구실험보조원
동기: 지민은영수가효율적으로프로젝트를수행하도록돕고, 실험실을깔끔하게유지하는
것에자부심을느낍니다.
인물3:
이름: 은혁
역할: IT 기술지원
동기: 은혁은연구소의모든데이터저장장치가안전하게보관되도록책임을집니다.
추론을만들때에는인물들의역할을존중하고, 그들이이야기에따라
어떤사건을보거나보지못하도록하는동기를부여해주세요. 또한이러한동기나이야기는
여러"이동"에걸쳐일관되게이어지도록노력해주세요.
누군가가어떤것을보았거나보지못했다고명시적으로말하지마세요. 당신의역할은이를
암시하는사실들을제공하는것입니다. 예를들어, 지수가철수가무언가를옮기는것을
보았다고암시하고싶다면, "지수는집안일을하면서철수를보고있었다" 그리고"누군가를
보고있다면, 그사람이무엇을하고있는지를보는것이다"라고말할수있습니다. 누군가가
본사실을직접적으로말하지않고, 보는행위의물리적조건을설명하는방식입니다.
물건이움직였다는사실을언급하거나이미등장한물건을재사용하지마세요. 예를들어, "
철수가자신의아이폰을보지못했다"라는사실이있고, 당신이"유림이는사과가움직이는
것을보지못했다"를증명하고있다면, 철수의아이폰을다시사용하지마세요. 우리프로그
램은아이템이어디에있는지를엄격하게제어하고있으며, 우리가고려하지않은아이템
배치를도입하면안됩니다.
현재트리:
영수는중요한프로젝트의자료를USB에저장해가지고있습니다. USB를잃어버리면
프로젝트제출이불가능해집니다. | 추론된결론
> 이야기시작| 추론된사실
> > 영수가노트북을실험실책상에서보았다. | 스토리에서추출된사실
> > 영수가USB를실험실책상에서보았다. | 스토리에서추출된사실
> > 은혁이노트북을실험실책상에서보았다. | 스토리에서추출된사실
> > 은혁이USB를실험실책상에서보았다. | 스토리에서추출된사실
> > 지민이노트북을실험실책상에서보았다. | 스토리에서추출된사실
> > 지민이USB를실험실책상에서보았다. | 스토리에서추출된사실
> 지민이노트북을창고선반으로옮긴다. 왜냐하면, 지민은실험이끝난후실험실의공간을
확보하기위해노트북을정리합니다. | 추론된사실
> > 영수는노트북을창고선반으로이동하는것을보았다. | 추론된사실
> > 은혁이는노트북을창고선반으로이동하는것을보았다. | 추론된사실
> 영수가USB를작업대서랍으로옮긴다. 왜냐하면, 영수는중요한자료를안전한장소에
보관하기위해가까운서랍에넣어두기로결정합니다. | 추론된사실
> > 은혁이는USB를작업대서랍으로이동하는것을보았다. | 추론된사실
41

--- Page 42 ---

> > 지민이는USB를작업대서랍으로이동하는것을보지않았다. | 추론된사실
> 은혁이USB를보안금고로옮긴다. 왜냐하면, 은혁은자료의보안을강화하기위해USB를
보안금고에안전하게보관합니다. | 추론된사실
> > 영수는USB를보안금고로이동하는것을보았다. | 추론된사실
> > 지민이는USB를보안금고로이동하는것을보지않았다. | 추론된사실
완성해야할함의추론:
영수는중요한프로젝트의자료를USB에저장해가지고있습니다. USB를잃어버리면
프로젝트제출이불가능해집니다.
> 지민이노트북을창고선반으로옮긴다. 왜냐하면, 지민은실험이끝난후실험실의공간을
확보하기위해노트북을정리합니다. 왜냐하면, 이야야기에따르면,
> > 영수는노트북을창고선반으로이동하는것을보았다. 왜냐하면, 이야야기에따르면,
> > > 스토리에서추출된사실
> > > 스토리에서추출된사실
> > > 상식
’완성해야할함의추론’은’현재트리’의일부입니다. ’완성해야할함의추론’에대해서만,
정확한개수의’스토리에서추출된사실’과’상식’를생성하세요.
Figure 26: Prompts for Reasoning Tree Expansion - Object Placements
We are creating stories in which people move many items multiple times. The goal of these stories
is to be engaging and coherent, while allowing readers or language models to track the location of
each object clearly so that we can later query them about world states or beliefs.
To build such stories, we construct a tree structure outlining both the story progression and
changes in the world state. Your task is to complete an inclusion reasoning tree that explains why
a person did or did not observe a particular event.
Each reasoning tree is a hierarchical structure where intermediate nodes are logically entailed by
their child nodes. They form a natural language proof over sets of facts.
To complete a reasoning step, you must fill in one implication reasoning subtree that connects
back to the higher-level statement. Follow the given structure exactly.
“Fact from story” refers to explicitly stated facts that appear in the narrative.
“Commonsense” refers to generally accepted truths that do not need to be explicitly stated.
“Composite fact” refers to facts implied by simpler facts within the story (these will be recursively
expanded later).
All facts in this reasoning step must jointly entail the higher-level fact.
Do not include facts that contradict the existing tree.
Do not include facts about other people except when necessary to explain whether someone could
or could not see an event. Focus only on physical or observational conditions.
42

--- Page 43 ---

Write your reasoning to exactly match the “Implication Reasoning to Complete” section. The
number and order of “Fact from story” and “Commonsense” entries must be identical to the
template.
Do not state directly that someone saw or did not see something. Instead, provide supporting facts
that imply this. For example, to imply that Jisoo saw Chulsoo moving something, you might write
“Jisoo was watching Chulsoo while doing household chores” and “When someone is watching
another person, they usually see what that person is doing.” Avoid direct observation statements;
instead describe physical conditions that make observation possible.
Do not mention that items moved, nor reuse already introduced items. For example, if the fact
“Chulsoo did not see his iPhone” is present and you are reasoning about “Yurim did not see the
apple move,” do not reuse Chulsoo’s iPhone. The system tracks all object states strictly, and new
untracked items should not be introduced.
Each fact should be decisive for inference. Omit some details intentionally so that other facts
complete the reasoning chain. The conclusion must fail if any fact is missing. Avoid repeating the
same fact.
Always use proper names instead of pronouns.
Perform exactly one reasoning step at a time. Your reasoning must strictly conform to the
“Implication Reasoning to Complete” template so that it can be parsed programmatically.
See the example below.
Scenario:
Minsu and Yerim are at a karaoke bar.
Current tree:
Minsu and Yerim are at a karaoke bar. | Deduced Root Conclusion
> Opening scene | Deduced Fact
> > Minsu saw the microphone on the stage. | Fact from story
> > Yerim saw the microphone on the stage. | Fact from story
> > Minsu saw the beer at the bar. | Fact from story
> > Yerim saw the beer at the bar. | Fact from story
> Minsu moves the beer to the table. | Deduced Fact
> > Yerim did not see the beer being moved to the table. | Deduced Fact
> > > Yerim was facing away from the table. | Deduced Fact
> > > > Yerim was talking to another customer. | Fact from story
> > > > The other customer was facing the table. | Fact from story
> > > > People usually face each other when talking, so one looks opposite the other. |
Commonsense
> > > If someone is facing away from something, they cannot see what happens around it. |
Commonsense
> Yerim moves the microphone to the table. | Deduced Fact
> > Yerim saw the beer on the table while moving the microphone. | Fact from story
> > Minsu saw the microphone being moved to the table. | Deduced Fact
> > > Minsu was drinking beer at the table. | Fact from story
> > > When something happens right next to someone, they usually see it. | Commonsense
43

--- Page 44 ---

> Yerim moves the beer to the trash can. | Deduced Fact
> > Minsu did not see the beer being moved to the trash can. | Fact from story
Implication reasoning to complete:
Minsu and Yerim are at a karaoke bar.
> Yerim moves the beer to the trash can because, according to the story,
> > Minsu did not see the beer being moved to the trash can because, according to the story,
> > > Fact from story
> > > Fact from story
> > > Commonsense
Output:
Minsu and Yerim are at a karaoke bar.
> Yerim moves the beer to the trash can because, according to the story,
> > Minsu did not see the beer being moved to the trash can because, according to the story,
> > > Yerim tricked Minsu into looking “over there.” | Fact from story
> > > Yerim pointed Minsu toward the opposite direction of the trash can. | Fact from story
> > > When someone is deceived into looking elsewhere, they cannot see what happens behind
them. | Commonsense
Now it’s your turn.
Scenario description:
Youngsoo is working on an important project due next week. All experiment results and required
data are stored on a USB drive, and losing it would be catastrophic. Jimin maintains order in the
lab to help Youngsoo focus, while Eunhyuk ensures data safety and security.
When building your reasoning, respect each character’s role and motivation within the story.
Ensure that these motivations remain consistent across multiple “moves.”
Do not directly state that someone saw or did not see something—use physical or situational
implications instead.
Do not mention new or reused objects beyond those already in the tree.
Current tree:
Youngsoo stores his important project data on a USB drive. Losing the USB would make
submission impossible. | Deduced Root Conclusion
> Story begins | Deduced Fact
> > Youngsoo saw the laptop on the lab desk. | Fact from story
> > Youngsoo saw the USB on the lab desk. | Fact from story
> > Eunhyuk saw the laptop on the lab desk. | Fact from story
> > Eunhyuk saw the USB on the lab desk. | Fact from story
> > Jimin saw the laptop on the lab desk. | Fact from story
> > Jimin saw the USB on the lab desk. | Fact from story
> Jimin moves the laptop to the storage shelf because she wants to clear space after finishing the
experiment. | Deduced Fact
> > Youngsoo saw the laptop being moved to the storage shelf. | Deduced Fact
> > Eunhyuk saw the laptop being moved to the storage shelf. | Deduced Fact
> Youngsoo moves the USB to the workbench drawer because he wants to store it safely nearby. |
Deduced Fact
> > Eunhyuk saw the USB being moved to the workbench drawer. | Deduced Fact
44

--- Page 45 ---

> > Jimin did not see the USB being moved to the workbench drawer. | Deduced Fact
> Eunhyuk moves the USB to the secure safe because he wants to strengthen data protection. |
Deduced Fact
> > Youngsoo saw the USB being moved to the secure safe. | Deduced Fact
> > Jimin did not see the USB being moved to the secure safe. | Deduced Fact
Implication reasoning to complete:
Youngsoo stores his important project data on a USB drive. Losing the USB would make
submission impossible.
> Jimin moves the laptop to the storage shelf because she wants to clear space after finishing the
experiment. Because, according to the story,
> > Youngsoo saw the laptop being moved to the storage shelf because, according to the story,
> > > Fact from story
> > > Fact from story
> > > Commonsense
The “Implication reasoning to complete” is a subset of the “Current tree.” Generate exactly the
specified number of “Fact from story” and “Commonsense” statements for it.
Figure 27: Prompts for Reasoning Tree Expansion - Object Placements (Translated)
[[PROMPT]]:
우리가작성한이야기를계속이어서작성해주세요. 다음에일어날이사건에대해짧은
설명을써주세요. 오직이동에대해서만작성하고, 다른추가정보는포함하지마세요.
절대"누군가가뭔가를보지못했다"거나, 누군가가어디에있는지추론할수있는능력이
있음을시사하지마세요. "몰래" 혹은"알수없게"와같은표현도하지마세요! 아래는
예시입니다.
한두문장만작성하세요. 매우짧은설명이어야합니다.
이야기개요: 용준이는자신이받을자격이있다고생각했던직업을상우가부정행위를통해
차지했다고생각하여화가났습니다! 그래서용준이는상우의소지품을버리기시작했습니다.
인물:
이름: 용준
역할: 최근졸업했고아파트를공동으로사용중인사람
동기: 부정행위로룸메이트가자신의취업자리를빼앗았다고생각해매우화가나있다.
이벤트:
- 용준이가차열쇠를쓰레기통으로옮긴다. 이유: 용준이는상우에게화가나그의열쇠를
버리고싶었다.
- 용준이가차열쇠를옮기다가쓰레기통에있는아이폰을발견했다.
출력예시: 분노에찬동작으로열쇠가깡통쓰레기통에부딪히며소리를냈다. 곧이어예상치
못한*퍽* 소리가났고... 잠시호기심이화를억누르자, 용준이는쓰레기통안에서아이폰을
발견했다.
45

--- Page 46 ---

또다른예시:
이야기개요: 민수는방금새아파트로이사했지만, 이전세입자가집을엉망으로만들어놓고
떠났다! 집주인은아무런조치도취하지않아민수가직접청소를해야한다.
인물:
이름: 민수
역할: 새롭지만지저분한아파트에막이사온사람
동기: 이전세입자가남긴어질러진상태를혼자치워야하며, 관리사무소는전혀도움이
되지않는다.
이벤트:
- 민수가국수를팬트리로옮긴다.
이유: 민수는아파트를깨끗하게만들고싶었고, 국수를제자리에두는것이마지막단계였기
때문이다!
출력예시: 민수는기쁨이가득한표정으로국수를팬트리에넣었다. 끝이없을것같던
쓰레기와잡동사니치우기는드디어마무리되어, 아파트가비로소깔끔해졌다!
당신의차례입니다.
이야기개요: 이야기개요:
영수는다음주제출해야할중요한프로젝트를진행중입니다. 실험결과와필요한모든
정보를USB에저장해두었으며, 이를잃어버리면큰문제가발생할것입니다. 지민은
실험실의질서를유지하면서영수가프로젝트에집중할수있도록돕습니다. 동시에은혁은
데이터의안전과보안을보장합니다.
인물:
이름: 지민
역할: 연구실험보조원
동기: 지민은영수가효율적으로프로젝트를수행하도록돕고, 실험실을깔끔하게유지하는
것에자부심을느낍니다.
이벤트:
- 지민이노트북을창고선반으로옮긴다. 왜냐하면, 지민은실험이끝난후실험실의공간을
확보하기위해노트북을정리합니다.
출력:
영수는실험실책상위에놓인노트북과USB를다시한번확인하며안도의한숨을내쉬었다.
주말이면제출해야할중요한프로젝트가머릿속을가득채우고있었지만, 모든실험결과와
자료가든USB가안전하게보관되어있다는사실에조금이나마마음이놓인것이다. 지민은
실험실안을부지런히정리하며영수가프로젝트에오롯이집중할수있도록돕고있었다.
그는노트북과USB가실험실책상에놓여있다는것을정확히알고있었고, 깔끔한환경에서
영수의연구효율을높이고자했다. 은혁역시연구실의데이터보안을책임지는사람답게
이두물건을주시하고있었다. 그는USB 속민감한자료가외부로새어나가지않도록주의
깊게점검하며, 노트북이안전하다는사실도재차확인했다. 사실이곳에있는세사람모두
노트북과USB가실험실책상위에놓여있다는것을알고있었으며, 그어느때보다신중하게
프로젝트를준비하고보안을지키려했다.
46

--- Page 47 ---

[[MODEL RESPONSE]]:
지민은노트북을창고선반으로옮겼다.
[[PROMPT]]:
지금까지작성된이야기를이어서, 아래에제시된관찰사실들에대해작성하세요.
단, 사실들에대해서만쓰고새로운정보를추가하지마세요.
"누군가보았다", "알아차리지못했다"라는표현을사용하지말고,
누군가가무언가를본사실이유일한관찰사실일때만"누군가가X를보았다"라고쓰세요.
이야기의분위기를잡는데사용할수있는추가정보가있을수있지만,
항상관찰사실을이야기의주요가이드로삼아야합니다.
아래이야기의핵심물건들은절대언급하지마세요:
- USB
- 노트북
이단락이후에다른사건이있을예정이므로, 사실에만충실하여이단락을갑작스럽게
마무리하세요. 일반적인진술은하지마세요. 마지막문장은제시된사실에관한내용만담고,
온전한문장이어야합니다.
이야기는현재의가장최근상황에서벌어지고있다고가정하세요.
다시말해, 아래의내용:
"지민은노트북을창고선반으로옮겼다."
이진행되는동안, 당신이작성해야하는관찰사실들도동시에일어나고있습니다.
예시를들어보겠습니다.
이야기개요: 철수, 유리, 지훈은하루를준비중입니다. 철수는커리어의성패가달린큰
회의를앞두고준비해야합니다.
유리는철수의회의를도와주고, 그날늦게그회의이야기를듣게되기를고대합니다.
지훈은학교시험을준비중이지만, 아빠인철수의중요한회의에다소배려없는모습을
보이고있습니다.
인물1:
이름: 철수
역할: 남편
동기: 큰회의를앞두고있고, 그결과가자신의커리어를좌우할수있음.
인물2:
이름: 유리
역할: 아내
동기: 언제나가족을적극적으로돕고싶어하며, 가족에게최선을바라는인물.
인물3:
이름: 지훈
역할: 아들
동기: 곧학교에서큰시험을앞두고있어긴장하고있으며, 무심코주변사람들에게배려를
덜하게됨.
47

--- Page 48 ---

관찰사실:
- 철수가아침식사를준비하고있음
- 주방에는쓰레기통이없음
- 유리는밖에서정원을물주며가꾸고있음
- 유리는쓰레기통이있는방을창문으로볼수있음
출력예시: 철수는하루를시작하기전배가고파서아침을준비하고있었다. 그런데주방에는
쓰레기통이없었다.
유리는언제나식물을잘돌보는편이라정원에물을주고있었고, 가까운창문을통해
쓰레기통이있는방을볼수있었다.
이제당신의차례입니다.
이야기개요: 이야기개요: 영수는다음주제출해야할중요한프로젝트를진행중입니다.
실험결과와필요한모든정보를USB에저장해두었으며, 이를잃어버리면큰문제가
발생할것입니다. 지민은실험실의질서를유지하면서영수가프로젝트에집중할수있도록
돕습니다. 동시에은혁은데이터의안전과보안을보장합니다.
인물1:
이름: 영수
역할: 연구원
동기: 영수는중요한프로젝트를제시간에제출하기위해모든자료를USB에저장하고
안전하게보관하고자합니다.
인물2:
이름: 지민
역할: 연구실험보조원
동기: 지민은영수가효율적으로프로젝트를수행하도록돕고, 실험실을깔끔하게유지하는
것에자부심을느낍니다.
인물3:
이름: 은혁
역할: IT 기술지원
동기: 은혁은연구소의모든데이터저장장치가안전하게보관되도록책임을집니다.
관찰사실:
- 영수는정리직전에그장비바로옆에서있었다.
- 은혁은지민가까이에서주위를살펴보고있었다.
- 지민은실험종료직후, 영수에게그장비정리계획을간단히언급했다.
- 지민은정리직전에은혁에게잠시보관계획을언급했다.
출력:
영수는실험실책상위에놓인노트북과USB를다시한번확인하며안도의한숨을내쉬었다.
주말이면제출해야할중요한프로젝트가머릿속을가득채우고있었지만, 모든실험결과와
자료가든USB가안전하게보관되어있다는사실에조금이나마마음이놓인것이다. 지민은
실험실안을부지런히정리하며영수가프로젝트에오롯이집중할수있도록돕고있었다.
그는노트북과USB가실험실책상에놓여있다는것을정확히알고있었고, 깔끔한환경에서
영수의연구효율을높이고자했다. 은혁역시연구실의데이터보안을책임지는사람답게
이두물건을주시하고있었다. 그는USB 속민감한자료가외부로새어나가지않도록주의
48

--- Page 49 ---

깊게점검하며, 노트북이안전하다는사실도재차확인했다. 사실이곳에있는세사람모두
노트북과USB가실험실책상위에놓여있다는것을알고있었으며, 그어느때보다신중하게
프로젝트를준비하고보안을지키려했다.
지민은노트북을창고선반으로옮겼다.
[[MODEL RESPONSE]]:
영수는정리직전에그장비바로옆에서있었다.
지민은실험종료직후, 영수에게그장비정리계획을간단히언급했다. 은혁은지민가까이
에서주위를살펴보고있었다. 지민은정리직전에은혁에게잠시보관계획을언급했다.
Figure 28: Prompts for Narrative Generation - Object Placements
[[PROMPT]]:
Please continue the story we have written so far. Write a short description of what happens next,
focusing only on the movement event. Do not include any additional or inferred information.
Never say that “someone didn’t see something,” or imply that a character can infer where
something is. Avoid using words such as “secretly” or “unnoticeably.”
Here is an example.
Write only one or two sentences—it must be a very short description.
Story summary: Yongjun is furious because he believes Sangwoo unfairly took the job he
deserved through cheating! Out of anger, Yongjun begins throwing away Sangwoo’s belongings.
Character:
Name: Yongjun
Role: A recent graduate sharing an apartment
Motivation: He believes his roommate took his job through dishonest means and feels deeply
betrayed.
Event:
- Yongjun moves the car key to the trash can. Reason: Yongjun wants to vent his anger by throwing
away Sangwoo’s car key.
- While moving the key, Yongjun discovers an iPhone in the trash can.
Output example: In a burst of anger, the key clattered loudly against the metal trash can. Then
came an unexpected *thud*—his curiosity briefly overpowering his rage, Yongjun peered inside
and found an iPhone.
Another example:
Story summary: Minsu has just moved into a new apartment, but the previous tenant left the place
a complete mess! Since the landlord refused to help, Minsu must clean everything up alone.
49

--- Page 50 ---

Character:
Name: Minsu
Role: A new tenant cleaning up his dirty apartment
Motivation: Wants to restore order and finish organizing what the landlord ignored.
Event:
- Minsu moves the noodles to the pantry.
Reason: This is the final step in tidying up, marking the end of his long day of cleaning.
Output example: Smiling with satisfaction, Minsu placed the noodles neatly in the pantry. The
endless cleaning finally came to an end, and the apartment at last looked spotless.
Now it’s your turn.
Story summary:
Youngsoo is working on an important project due next week. All experiment results and required
data are stored on a USB drive, and losing it would be disastrous. Jimin maintains order in the lab
so that Youngsoo can focus, while Eunhyuk ensures data safety and security.
Character:
Name: Jimin
Role: Research assistant
Motivation: Jimin takes pride in keeping the lab organized and helping Youngsoo work efficiently.
Event:
- Jimin moves the laptop to the storage shelf because she wants to clear the workspace after the
experiment has ended.
Output:
Youngsoo exhaled a sigh of relief as he checked once more that the laptop and USB were still
on the lab desk. With the project deadline looming, the fact that all data remained safely stored
gave him a small sense of comfort. Jimin busily tidied up the lab so Youngsoo could stay fully
focused on his research. She knew exactly where the laptop and USB were and wanted to keep
the workspace neat to boost productivity. Eunhyuk, responsible for data security, kept a close eye
on both items, ensuring that the sensitive data inside the USB stayed protected and that the laptop
remained safe. All three of them were aware that the laptop and USB sat on the desk, taking extra
care to maintain order and security in the lab.
[[MODEL RESPONSE]]:
Jimin moved the laptop to the storage shelf.
[[PROMPT]]:
Continue the story from where it left off, incorporating the following observed facts.
Write only what is directly based on these facts; do not invent new details.
Do not use expressions like “someone saw” or “someone didn’t notice.”
If a sighting is the only relevant observation, you may state “someone saw X.”
You may include minimal background details to maintain narrative flow, but the observed facts
must remain central to the paragraph.
50

--- Page 51 ---

Never mention the following key objects in this paragraph:
- USB
- Laptop
Another event will follow this paragraph, so end abruptly with a factual statement related only to
the given observations. Avoid general closure sentences; the final sentence must concern only the
provided facts.
Assume the events are occurring in the most recent scene of the story, meaning the following line
is currently happening:
“Jimin moved the laptop to the storage shelf.”
The observations you must describe are happening simultaneously with that action.
Example:
Story summary: Chulsoo, Yuri, and Jihoon are getting ready for the day. Chulsoo has an important
meeting that could determine his career.
Yuri helps him prepare and looks forward to hearing how it went later. Jihoon, preoccupied with
an upcoming school exam, is unintentionally inconsiderate to his family.
Character 1:
Name: Chulsoo
Role: Husband
Motivation: Prepares for a crucial meeting that could determine his career path.
Character 2:
Name: Yuri
Role: Wife
Motivation: Wants to support her family and always helps them do their best.
Character 3:
Name: Jihoon
Role: Son
Motivation: Nervous about his upcoming exam, sometimes less considerate of others.
Observed facts:
- Chulsoo is preparing breakfast.
- There is no trash can in the kitchen.
- Yuri is outside watering the garden.
- Yuri can see the room with the trash can through a nearby window.
Output example: Hungry before starting the day, Chulsoo prepared breakfast. But there was no
trash can in the kitchen. Outside, Yuri tended carefully to her garden, watering each plant, and
from a nearby window she could see the room where the trash can was kept.
Now it’s your turn.
51

--- Page 52 ---

Story summary: Youngsoo is working on an important project due next week. All experiment
results and necessary information are stored on a USB drive, and losing it would be disastrous.
Jimin maintains order in the lab to help Youngsoo concentrate, while Eunhyuk ensures data safety
and security.
Character 1:
Name: Youngsoo
Role: Researcher
Motivation: To safely store and submit his project data on time.
Character 2:
Name: Jimin
Role: Research assistant
Motivation: Takes pride in helping Youngsoo and maintaining a clean, efficient workspace.
Character 3:
Name: Eunhyuk
Role: IT support specialist
Motivation: Ensures the secure handling of all data storage devices in the lab.
Observed facts:
- Youngsoo stood right next to the equipment just before cleanup.
- Eunhyuk was near Jimin, surveying the area.
- Jimin briefly mentioned her cleanup plan to Youngsoo right after the experiment ended.
- Jimin also mentioned her storage plan to Eunhyuk just before starting the cleanup.
Output:
Youngsoo exhaled a sigh of relief as he checked once more that the laptop and USB were still
on the lab desk. With the project deadline looming, the fact that all data remained safely stored
gave him a small sense of comfort. Jimin busily tidied up the lab so Youngsoo could stay fully
focused on his research. She knew exactly where the laptop and USB were and wanted to keep
the workspace neat to boost productivity. Eunhyuk, responsible for data security, kept a close eye
on both items, ensuring that the sensitive data inside the USB stayed protected and that the laptop
remained safe. All three of them were aware that the laptop and USB sat on the desk, taking extra
care to maintain order and security in the lab.
Jimin moved the laptop to the storage shelf.
[[MODEL RESPONSE]]:
Youngsoo stood right next to the equipment just before cleanup. Jimin briefly mentioned her plan
to Youngsoo after the experiment ended. Eunhyuk was near Jimin, looking around the lab. Just
before starting the cleanup, Jimin mentioned her storage plan to Eunhyuk.
Figure 29: Prompts for Narrative Generation - Object Placements (Translated)
우리는매니저(당신)가사람들을특정업무에배정하는이야기를만들고있습니다.
당신은각인물의과거경험, 취향, 성격, 사회적관계등을살펴보며
누가어떤업무에능숙하고, 누가어떤업무에서투른지를파악해야합니다.
52

--- Page 53 ---

이이야기를만들기위해, 우리는이야기의윤곽을잡는트리구조를생성했습니다.
당신의임무는이트리를채워, 특정사실들이어떻게성립되는지를보여주는논리트리를
완성하는것입니다.
업무와스킬관련사실을다룰때는, 각인물의과거경험과개인적이야기를부각해주세요.
예를들어, "영훈이는테니스를잘못한다"라는사실이라면,
"영훈이는어릴때부터운동신경이좋지않았다"라든지,
"영훈이는지금도스포츠경기를피한다"라는사실을통해
"운동신경이좋지않고스포츠를피하는사람이라면테니스를잘하지못할가능성이높다"
와같은추론을이어갈수있습니다.
협업(팀워크)과관련된사실을다룰때는, 두사람이과거에어떻게상호작용했는지, 사회적
요소에주목해주세요.
예를들어, "영훈이와민수는함께일할때시너지가좋다"라는사실은
"영훈이와민수는가끔점심을함께먹는다"거나
"둘은지난주에같이작업해서평이한시간안에일을마쳤다" 같은뉘앙스를통해
"두사람이함께시간을보내고적절하게일을마치는모습을보였으므로, 함께잘일한다고
볼수있다"라는식으로추론을전개할수있습니다.
무엇보다, 이사실들은흥미롭고인물중심적이어야합니다. 너무건조하거나일반적인
내용은피해주세요.
논리트리는트리구조로, 자식노드의사실들이결합되어부모노드를함의하도록구성됩니
다.
이는’추론된결론’을증명하기위해필요한중간추론단계를자연어로보여주는구조입니다.
이단계에서당신은’추론보강’ 작업을수행합니다.
즉, 하나의서브트리를완성하기위해자식노드들의사실을채워넣어야합니다.
각단계를작성할때, 주어진구조(배열된자식노드, 사실분류등)에맞추어야합니다.
’스토리에서추출된사실’은이야기에서명시적으로언급되는사실들이며,
’상식’은일반적으로많은사람이동의하는상식수준의사실들입니다.
’복합사실’는단순사실들이결합되어도출되는복합적사실이며, 추후(재귀적호출) 다른
부분에서확장될수있습니다.
각사실은추론된결론을이끌어내는데꼭필요한근거여야합니다.
서로중복되거나불필요한사실은지양해주세요.
가능하다면대명사대신인물의이름을직접사용하세요.
이미특정이름을알고있다면, "그/그녀" 대신직접그이름을써주세요.
예제를확인하세요.
시나리오:
민수와예림이는노래방에있다.
현재트리:
민수와예림이는노래방에있다. | 추론된결론
> 오프닝장면| 추론된사실
53

--- Page 54 ---

> > 민수는무대에있는마이크를보았다. | 스토리에서추출된사실
> > 예림이는무대에있는마이크를보았다. | 스토리에서추출된사실
> > 민수는바에있는맥주를보았다. | 스토리에서추출된사실
> > 예림이는바에있는맥주를보았다. | 스토리에서추출된사실
> 민수는맥주를테이블로옮긴다. | 추론된사실
> > 에림이는맥주가테이블로옮겨지는것을보지못했다. | 추론된사실
> > > 예림이는테이블에서반대쪽을보고있었다. | 추론된사실
> > > > 예림이는다른손님과대화중이었다. | 스토리에서추출된사실
> > > > 다른손님은테이블쪽을보고있었다. | 스토리에서추출된사실
> > > > 보통사람들은서로를바라보며대화하기때문에, 한사람이한방향을보고있으면
다른사람은반대방향을보고있게된다. | 상식
> > > 만약누군가다른무언가에서반대방향을보고있다면, 그무언가주변에서일어나는
일을볼수없다. | 상식
> 예림이는마이크를테이블로옮긴다| 추론된사실
> > 예림이는마이크를옮길때테이블에있는맥주를보았다. | 스토리에서추출된사실
> > 민수는마이크가테이블로옮겨지는것을보았다. | 추론된사실
> > > 민수는테이블에서맥주를마시고있었다. | 상식
> > > 어떤일이사람바로옆에서일어나면, 그사람은보통그상황을볼수있다. | 스토리에서
추출된사실
> 예림이는맥주를쓰레기통으로옮긴다. | 추론된사실
> > 민수는맥주가쓰레기통으로옮겨지는것을보지못했다. | 스토리에서추출된사실
완성해야할함의추론:
민수와예림이는노래방에있다. 왜냐하면,
> 예림이는맥주를쓰레기통으로옮긴다. 왜냐하면,
> > 민수는맥주가쓰레기통으로옮겨지는것을보지못했다. 왜냐하면,
> > > 스토리에서추출된사실
> > > 스토리에서추출된사실
> > > 상식
출력:
민수와예림이는노래방에있다. 왜냐하면,
> 예림이는맥주를쓰레기통으로옮긴다. 왜냐하면,
> > 민수는맥주가쓰레기통으로옮겨지는것을보지못했다. 왜냐하면,
> > > 예림이는민수를속여서"저쪽"을보게했다. | 스토리에서추출된사실
> > > 예림이는민수에게쓰레기통의반대방향을가리켰다. | 스토리에서추출된사실
> > > 누군가를속여서다른곳을보게만들면, 반대쪽에서일어나는일을볼수없다. | 상식
또다른예제입니다.
시나리오:
당신의개가방금이웃의마당에똥을쌌다. 이웃은당신을노려보며다가온다... 그는이렇게
말한다: "이봐요! 지금당신개가내예쁜마당에다무슨짓을하게두는거죠!"
현재트리:
이웃의코를정면으로주먹질한다. | 추론된결론
> 멋져보일것이고, 이것은장점이다. | 추론된사실
> > 당신이사는곳에서는싸움을멋지다고생각한다. | 스토리에서추출된사실
> > 당신은싸움을하게될것이다. | 스토리에서추출된사실
> > 사람들이멋지다고생각하는행동을하면, 그행동을한사람도멋지게여겨진다. | 상식
> 멋져보일것이지만, 상황에따라달라질수있다... | 스토리에서추출된사실
54

--- Page 55 ---

완성해야할함의추론:
민철이는범행수단이있다. 왜냐하면,
> 스토리에서추출된사실
> 스토리에서추출된사실
> 상식
출력:
민철이는범행수단이있다. 왜냐하면,
> 민철이는헤로인에접근할수있다. | 스토리에서추출된사실
> 민철이는헤로인과다복용에필요한양을알고있다. | 스토리에서추출된사실
> 헤로인에접근할수있고, 치명적인양을알고있다면, 피해자에게의도적으로치명적인
용량을투여하여살인을저지를수있는수단을갖춘것이다. | 상식
또다른예제입니다.
시나리오:
피해자: 준호
범행장소: 공원벤치
살해도구: 헤로인과다복용
용의자: 민철
용의자의역할: 마약사용자
범행동기: 공개적인굴욕
현재트리:
민철이는살인자다. | 추론된결론
> 민철이는범행기회가있다. | 스토리에서추출된사실
> 민철이는범행기회가있다. | 스토리에서추출된사실
> 민철이는범행기회가있다. | 스토리에서추출된사실
완성해야할함의추론:
민수와예림이는노래방에있다. 왜냐하면,
> 예림이는맥주를쓰레기통으로옮긴다. 왜냐하면,
> > 복합사실
출력:
민수와예림이는노래방에있다. 왜냐하면,
> 예림이는맥주를쓰레기통으로옮긴다. 왜냐하면,
> > 민수는맥주가쓰레기통으로옮겨지는것을보지못했다. | 복합사실
이제당신의차례입니다.
시나리오:
당신은새로운소셜미디어플랫폼을만들고있습니다. 콘텐츠제작팀과사용자안전팀을
어떻게나누어야할까요?
현재트리:
당신은새로운소셜미디어플랫폼을만들고있습니다. 콘텐츠제작팀과사용자안전팀을
어떻게나누어야할까요? | 추론된결론
> 지훈과민지는같이못일한다. | 추론된사실
55

--- Page 56 ---

> > 민지는지훈의작업스타일을비효율적이라고생각한다. | 스토리에서추출된사실
> > 지훈과민진은과거프로젝트에서협업할때항상의견충돌을겪었다. | 스토리에서
추출된사실
> > 사람들이과거에지속적으로의견충돌이있었다면, 다시함께일할때도충돌이발생할
가능성이높다. | 상식
> 지훈은콘텐츠제작자를할수있다. | 추론된사실
> 지훈은사용자안전관리자를못한다. | 추론된사실
> 민지는콘텐츠제작자를못한다. | 추론된사실
> 민지는사용자안전관리자를못한다. | 추론된사실
> 소영과민지는같이못일한다. | 추론된사실
> 지훈과소영은같이못일한다. | 추론된사실
> 소영은콘텐츠제작자를못한다. | 추론된사실
> 소영은사용자안전관리자를못한다. | 추론된사실
완성해야할함의추론:
당신은새로운소셜미디어플랫폼을만들고있습니다. 콘텐츠제작팀과사용자안전팀을
어떻게나누어야할까요? 왜냐하면,
> 지훈은콘텐츠제작자를할수있다. 왜냐하면,
> > 스토리에서추출된사실
> > 스토리에서추출된사실
> > 상식
’완성해야할함의추론’은’현재트리’의일부입니다. ’완성해야할함의추론’에대해서만,
정확한개수의’스토리에서추출된사실’과’상식’를생성하세요.
Figure 30: Prompts for Reasoning Tree Expansion - Team Allocations
We are creating a story in which you, as the manager, must assign people to specific roles or tasks.
You should reason about each person’s past experiences, preferences, personalities, and social
relationships to determine who is skilled or unskilled at certain tasks.
To construct this story, we have prepared an outline in the form of a reasoning tree.
Your task is to expand this tree by showing how certain conclusions are logically supported by
specific facts.
When dealing with skills and tasks, focus on each individual’s background and personal traits.
For example, if the fact is "Younghoon is not good at tennis," you might write:
"Younghoon was never athletic as a child," and "Younghoon still avoids sports games," which can
support a commonsense inference such as:
"Someone who avoids sports and lacks athletic ability is unlikely to be good at tennis."
When dealing with teamwork or collaboration, focus on how people have interacted in the past or
on social factors.
For instance, if the fact is "Younghoon and Minsu work well together," it could be supported by:
"Younghoon and Minsu often have lunch together," or "They recently finished a task together
within a normal time frame," leading to the inference:
"Since they often spend time together and complete work effectively, it is reasonable to conclude
that they collaborate well."
56

--- Page 57 ---

The facts should be engaging and character-driven. Avoid overly generic or dry statements.
The reasoning tree should be structured so that child nodes jointly entail their parent node.
This structure shows how intermediate reasoning steps, expressed in natural language, support a
deduced conclusion.
At this stage, you are performing reasoning expansion.
That is, you must fill in child facts to complete a subtree in a way that matches the given structure
(for example, ordered child nodes and fact types).
"Fact from Story" refers to explicitly mentioned facts that appear in the story.
"Commonsense" refers to generally accepted truths or background knowledge shared by most
people.
"Composite Fact" refers to intermediate conclusions derived from combining multiple simpler
facts; these can later be recursively expanded elsewhere in the tree.
Each fact should be essential for justifying the parent conclusion. Avoid redundant or unnecessary
facts.
Whenever possible, use character names instead of pronouns. If a name is already given, use it
directly rather than "he" or "she."
Refer to the following example.
Scenario:
Minsu and Yerim are at the karaoke room.
Current tree:
Minsu and Yerim are at the karaoke room. | Deduced conclusion
> Opening scene | Deduced fact
> > Minsu saw the microphone on the stage. | Fact from story
> > Yerim saw the microphone on the stage. | Fact from story
> > Minsu saw the beer at the bar. | Fact from story
> > Yerim saw the beer at the bar. | Fact from story
> Minsu moves the beer to the table. | Deduced fact
> > Yerim did not see the beer being moved to the table. | Deduced fact
> > > Yerim was looking away from the table. | Deduced fact
> > > > Yerim was talking with another guest. | Fact from story
> > > > The other guest was facing the table. | Fact from story
> > > > When two people are talking to each other, they usually face one another; thus, if one
faces one direction, the other faces the opposite direction. | Commonsense
> > > If someone is facing away from an event, they usually cannot see what happens behind
them. | Commonsense
> Yerim moves the microphone to the table. | Deduced fact
> > Yerim saw the beer while moving the microphone to the table. | Fact from story
> > Minsu saw the microphone being moved to the table. | Deduced fact
> > > Minsu was drinking beer at the table. | Fact from story
> > > When something happens right next to a person, that person can usually see it. |
Commonsense
> Yerim moves the beer to the trash can. | Deduced fact
57

--- Page 58 ---

> > Minsu did not see the beer being moved to the trash can. | Fact from story
Target reasoning to complete:
Minsu and Yerim are at the karaoke room, because
> Yerim moves the beer to the trash can, because
> > Fact from story
> > Fact from story
> > Commonsense
Output:
Minsu and Yerim are at the karaoke room, because
> Yerim moves the beer to the trash can, because
> > Yerim distracted Minsu to make him look the other way. | Fact from story
> > Yerim pointed in the opposite direction of the trash can. | Fact from story
> > When someone is deceived into looking elsewhere, they cannot see what happens behind
them. | Commonsense
Now your turn.
Scenario:
You are developing a new social media platform. How should you divide your team between
content creation and user safety management?
Current tree:
You are developing a new social media platform. How should you divide your team between
content creation and user safety management? | Deduced conclusion
> Jihoon and Minji cannot work together. | Deduced fact
> > Minji thinks Jihoon’s working style is inefficient. | Fact from story
> > Jihoon and Minji always clashed during past collaborations. | Fact from story
> > If people have repeatedly clashed in the past, it is likely they will clash again when working
together. | Commonsense
> Jihoon can be a content creator. | Deduced fact
> Jihoon cannot be a user safety manager. | Deduced fact
> Minji cannot be a content creator. | Deduced fact
> Minji cannot be a user safety manager. | Deduced fact
> Soyoung and Minji cannot work together. | Deduced fact
> Jihoon and Soyoung cannot work together. | Deduced fact
> Soyoung cannot be a content creator. | Deduced fact
> Soyoung cannot be a user safety manager. | Deduced fact
Target reasoning to complete:
You are developing a new social media platform. How should you divide your team between
content creation and user safety management? Because,
> Jihoon can be a content creator, because
> > Fact from story
> > Fact from story
> > Commonsense
"Target reasoning to complete" is a part of the current tree. Generate only the required number of
"Fact from story" and "Commonsense" lines for that section.
58

--- Page 59 ---

Figure 31: Prompts for Reasoning Tree Expansion - Team Allocations
당신은아래시나리오설명과사실들의목록을보고짧은이야기를작성할것입니다.
이야기속에서모든사실을포함해야합니다.
당신은매니저나리더의역할을맡고있으며, 사람들을업무와기술에배정해야합니다.
하지만어떤배정이’가장좋은’ 배정인지답을제시하지않고, 독자가그답을고민하도록
남겨두세요.
즉, 누구에게어떤업무를맡길지결정하지말고, 이야기형식으로서술만해주세요.
이야기는흥미롭고, 일관성있게작성해주세요.
도입부를먼저쓰고, 세명의사람을소개하세요:
- 지훈
- 소영
- 민지
그리고매니저가이들을배치해야하는두개의업무도초반에언급하세요:
- 콘텐츠제작자
- 사용자안전관리자
설명: 당신은새로운소셜미디어플랫폼을만들고있습니다. 콘텐츠제작팀과사용자안전
팀을어떻게나누어야할까요?
아래사실들을반드시이야기속에포함하세요:
- 민지는복잡한규정을이해하고적용하는데어려움을겪는다.
- 민지는주로분석적인업무에더강점을보인다.
- 민지는지나치게혼란한상황에서침착함을유지하기어려워한다.
- 민지는지훈의작업스타일을비효율적이라고생각한다.
- 민지는콘텐츠제작과정에서창의적인아이디어를도출하는데어려움을겪는다.
- 소영과민지는이전프로젝트에서중요한결정이항상지연되었다고보고했다.
- 소영은과거프로젝트에서반복적으로작은실수를했었다.
- 소영은민지가결정을내릴때주저한다고느낀다.
- 소영은비디오편집소프트웨어사용경험이거의없다.
- 소영은세부적인규정준수보다는큰그림을보는것을선호한다.
- 소영은지훈과의의사소통에서좌절감을느꼈다.
- 소영은창의적인프로젝트보다관리및계획에더관심이크다.
- 지훈과민진은과거프로젝트에서협업할때항상의견충돌을겪었다.
- 지훈은과거프로젝트에서세부사항에대한주의를기울이지않아문제가되었다.
- 지훈은과거에다양한영상콘텐츠를제작한경험이있다.
- 지훈은규칙이나절차를따르는것을힘들어한다.
- 지훈은소영의의견을잘듣지않는경향이있다.
- 지훈은창의적인아이디어로팀에서자주인정받는다.
Figure 32: Prompts for Narrative Generation - Team Allocations
59

--- Page 60 ---

You will be given a scenario description and a list of facts. Your task is to write a short story that
naturally incorporates all of the provided facts.
You take the role of a manager or team leader who must assign people to specific tasks based on
their abilities and personalities.
However, do not present a final answer or explicit judgment about which assignment is best.
Instead, let readers think about the optimal assignment themselves.
That is, you should not decide who takes which role, but instead narrate the situation in story
form.
Make the story engaging and coherent.
Begin with an introduction and introduce the three people:
- Jihoon
- Soyoung
- Minji
Then mention the two tasks early in the story:
- Content Creator
- User Safety Manager
Description: You are building a new social media platform. How should you divide the team
between content creation and user safety management?
Be sure to include all of the following facts in your story:
- Minji struggles to understand and apply complex regulations.
- Minji shows more strength in analytical tasks.
- Minji has difficulty remaining calm in overly chaotic situations.
- Minji considers Jihoon’s working style inefficient.
- Minji has trouble generating creative ideas during content creation.
- Soyoung and Minji reported that major decisions were always delayed in previous projects.
- Soyoung made small repetitive mistakes in past projects.
- Soyoung feels that Minji hesitates when making decisions.
- Soyoung has little experience with video editing software.
- Soyoung prefers focusing on the big picture rather than strict adherence to regulations.
- Soyoung felt frustrated when communicating with Jihoon.
- Soyoung is more interested in management and planning than in creative projects.
- Jihoon and Minji frequently clashed during past collaborations.
- Jihoon often overlooked details in previous projects, causing problems.
- Jihoon has extensive experience creating various video content.
- Jihoon finds it difficult to follow rules or procedures.
- Jihoon tends to ignore Soyoung’s opinions.
- Jihoon is often recognized for his creative ideas in the team.
Figure 33: Prompts for Narrative Generation - Team Allocation (Translated)
60

--- Page 61 ---

I
Data and Reasoning Tree Examples
I.1
Murder Mysteries
영은은자동차안에서고기손질용도끼에의해살해당했으며, 김철수형사는예성과예슬을
용의자로심문하고있다.
김철수형사는압박감에시달리고있었다. 사건은그가다루어본것들중에서도유난
히복잡했다. 예성을만나기전그는이번사건의실마리를찾기위해집중하고있었다. 그는
예성이지역사회에깊이관여하고있다는사실을알고있었고, 이는예성을자동으로수사
대상에올려놨다.
예성은그들앞에서서김철수형사의질문에답했다. "네, 영은은차량문제로자주저
에게도움을요청했습니다." 예성은차분하게말했다. "자동차수리를도와주는건제게흔한
일이었죠."
김철수형사는고개를끄덕이며수첩에적었다. "영은씨가새로스포츠클럽에가입했
다고들었습니다. 그클럽은많은사회적인활동과모임을제공하는것으로알고있는데, 그
후로그녀가다른사람들과어울리는걸어떻게생각하셨습니까?"
"사실좋아하지않았습니다." 예성이답하며약간의긴장을보였다. 그는창문너머로
시선을돌렸다. "그녀가새로운사회적활동에시간을많이보내는걸보고불편했어요."
김철수는예성의반응을주의깊게관찰했다. "보아하니자주그녀를따라다니신것같
은데, 그녀가참여한주민모임에자주참석한이유는무엇이었나요?"
예성은약간머뭇거리며대답했다. "그저... 그녀와시간을보내고싶었습니다. 그녀의
다양한활동이저에게는조금은위협적으로느껴졌어요."
"동네공원에서영은씨와함께산책도하셨다고요?" 김철수는이어서물었다.
"네, 그곳은우리가함께시간을보내기에는좋은장소였어요." 예성은고개를끄덕이며
회상했다.
예성의작업공간을둘러본김철수는깔끔하게정돈된도구들을보며감탄했다. "목수
로서손재주가대단하시네요. 특히육류요리를자주한다고하셨죠?" 김철수는예성이
가지고있는고기손질용도끼를힐끗보았다.
"네, 요리는저의또다른취미입니다." 예성은웃으며대답했다. "그래서정기적으로
도구들도점검하고유지보수합니다."
김철수는고개를끄덕이며수첩을덮었다. 예성과의대화는끝이났지만, 그는여전히
많은생각을남겨두고있었다. 읍내로돌아가는길에그는예성의정돈된작업공간과그의
신중한태도가계속해서떠올랐다.
김철수형사는예슬과의면담을준비하면서노트를들여다보았다. 그녀는가족내에서
많은책임을맡고있는것으로보였다. 일상적인조사로는보이지않는연결고리를찾아야
했다.
예슬은김철수형사를집으로맞이하는동안여러요리책이질서정연하게꽂혀있는서
재를지나갔다. "오, 여기있는조리법들은정말다양하군요." 김철수가말했다.
61

--- Page 62 ---

“요리를좋아해서새로운레시피를시도하는걸즐깁니다,” 예슬이미소를지으며응답
했다. 그녀는주로고기를사용하는요리에관심이많다며, “가끔고기전문점에가는게
일상이죠,”라고덧붙였다.
“그러시군요.” 김철수는메모를했다. “고기외에다른구매습관이라도있으신가요?”
“음. 고급주방용품점에서쇼핑하는것도좋아해요. 요즘탐사장비도좀샀지요.” 예슬
이말했다. 그녀는그것들을친구들에게자랑한적이있다며웃었다. 김철수는그녀의말을
주의깊게들으며수첩에하나하나적어나갔다.
두사람은이야기를계속나누며, 예슬은가족과가까운관계및그녀의책임에대해설
명했다. 예슬은대가족의중요한결정을관리하고, 가족을위한식사를준비하며, 영은과같은
집에살았다고했다.
“마을역사에도관심이많으신가요?” 김철수가물었다.
“네. 지역역사박물관에자주가고, 도서관에서도가끔관련커뮤니티행사에참석합니
다. 마을의숨겨진역사에대해알고싶어친구들에게자주이야기해요.” 예슬은설명했다.
김철수는메모를마무리하며, 그녀의집을둘러보았다. 서가한쪽에는탐사와관련된
책자들이줄지어있었다. 그녀의설명과환경에서주방도구부터숨겨진역사에이르는
다양한주제에관심이있는것이드러났다.
김철수는담담하게일어서며, “오늘이야기나눠주셔서감사합니다. 도움이많이됐습
니다.”라고말했다. 예슬은그를배웅하며마지막으로웃었다. 김철수형사는밖으로나와
수첩을다시확인하며다음조사방향을조용히생각했다.
문제: 다음중살인자일가능성이가장높은사람은누구인가?
1) 예성
2) 예슬
정답: 1 (예성)
Figure 34: Murder Mystery Example
Yeongeun was murdered in a car by a meat-cutting axe, and Detective Kim Cheolsu is interrogating
the suspects, Yesung and Yeseul.
Detective Kim was under immense pressure. This case was far more complex than any
he had handled before. Before meeting Yesung, he tried to focus, searching for any clue that might
lead to a breakthrough. He already knew Yesung was deeply involved in the local community,
which automatically made him a person of interest.
Yesung stood before them, answering Kim’s questions.
“Yes, Yeongeun often asked me for help with her car problems,” Yesung said calmly. “Helping
with car repairs was something I often did.”
Kim nodded, jotting something in his notebook.
62

--- Page 63 ---

“I heard Yeongeun recently joined a sports club. The club is known for its many social activities
and gatherings. How did you feel about her spending more time with new people?”
“To be honest, I didn’t like it,” Yesung replied with a hint of tension, glancing out the
window. “It made me uncomfortable to see her spending so much time on new social activities.”
Kim carefully observed Yesung’s reaction.
“It seems like you followed her often. Why did you frequently attend the community meetings she
joined?”
Yesung hesitated before answering.
“I just... wanted to spend more time with her. Her growing social life felt somewhat threatening to
me.”
“You also used to take walks with Yeongeun in the neighborhood park, correct?” Kim
asked.
“Yes, it was a nice place for us to spend time together,” Yesung nodded, reminiscing.
As Kim looked around Yesung’s workspace, he was impressed by the neatly arranged
tools.
“You’re very skilled with your hands as a carpenter. You also mentioned that you cook meat
dishes often?” Kim glanced briefly at the meat-cutting axe Yesung owned.
“Yes, cooking is another one of my hobbies,” Yesung replied with a smile. “I regularly
inspect and maintain my tools.”
Kim nodded and closed his notebook. Although his conversation with Yesung had ended, many
questions still lingered. On his way back to town, he couldn’t shake off the image of Yesung’s
tidy workshop and his cautious demeanor.
Preparing to meet Yeseul, Kim flipped through his notes. She seemed to bear many re-
sponsibilities within her family. There had to be a hidden link beyond what an ordinary
investigation could reveal.
When Yeseul welcomed Kim into her home, they passed through a study lined with
neatly arranged cookbooks.
“Oh, what a diverse collection of recipes,” Kim remarked.
“I love cooking and enjoy trying new recipes,” Yeseul replied with a smile. She added
that she was particularly interested in meat-based dishes, saying, “I often visit butcher shops—it’s
almost a routine.”
“I see,” Kim noted in his book. “Do you have any other shopping habits?”
“Well, I like shopping for high-end kitchenware. Recently, I even bought some explo-
ration tools,” Yeseul said, laughing as she mentioned showing them off to her friends. Kim
listened closely and took careful notes.
Their conversation continued as Yeseul spoke about her close relationship with her fam-
63

--- Page 64 ---

ily and her sense of duty. She explained that she managed important family decisions, prepared
meals for everyone, and lived in the same house as Yeongeun.
“Are you also interested in local history?” Kim asked.
“Yes. I often visit the local history museum and occasionally join related community
events at the library. I like sharing stories about the town’s hidden history with my friends,”
Yeseul explained.
As Kim wrapped up his notes, he glanced around her home. On one shelf were books
related to exploration, reflecting her diverse interests—from kitchen tools to local history.
Standing up calmly, Kim said, “Thank you for your time today. You’ve been very help-
ful.” Yeseul saw him to the door with a final smile. As Kim stepped outside, he quietly reviewed
his notes, thinking about the next step in his investigation.
Question: Who is most likely the murderer?
1) Yesung
2) Yeseul
Answer: 1 (Yesung)
Figure 35: Murder Mystery Example (Translated)
예성| 추론된결론
> 예성이는범행수단이있다. | 추론된사실
> > 예성이는평소에고기를손질할때도끼를사용한다. | 추론된사실
> > > 예성은육류손질을위해고기손질용도끼를사용한다. | 추론된사실
> > > > 예성은정기적으로육류를요리한다. | 스토리에서추출된사실
> > > > 예성은고기손질용도끼를소유하고있다. | 스토리에서추출된사실
> > > > 고기를요리하는사람들은종종특정한도구를사용하여고기를손질한다. | 상식
> > > 예성은주방에서고기요리를자주한다. | 추론된사실
> > > > 예성은고기손질용도끼를소유하고있다. | 스토리에서추출된사실
> > > > 예성은정기적으로육류를요리한다. | 스토리에서추출된사실
> > > > 고기를요리하는사람들은종종특정한도구를사용하여고기를손질한다. | 상식
> > > 고기를자주요리하는사람들은적절한도구를사용하여고기를손질하려고한다. |
상식
> > 예성이는목수로서다양한도구를소유하고있다. | 추론된사실
> > > 예성은다양한목공도구를가지고있다. | 추론된사실
> > > > 예성은작업을위해정기적으로도구를점검하고유지보수한다. | 스토리에서추출된
사실
> > > > 예성은목수로일하며자주작업공간을정돈한다. | 스토리에서추출된사실
> > > > 목수들은일반적으로작업을원활하게하기위해다양한도구를갖추고있다. | 상식
> > > 예성은목공작업을주기적으로한다. | 추론된사실
> > > > 예성은목수로일하며자주작업공간을정돈한다. | 스토리에서추출된사실
> > > > 예성은작업을위해정기적으로도구를점검하고유지보수한다. | 스토리에서추출된
사실
> > > > 목공작업을하는사람들은작업에필요한다양한도구를소유하고있는경향이있다.
| 상식
64

--- Page 65 ---

> > > 목공작업을하는사람들은작업에필요한다양한도구를소유하고있는경향이있다. |
상식
> > 목수라면다양한도구를쉽게구할수있으며, 고기손질용도끼를소유하고있다면이를
범행에사용할수있다. | 상식
> 예성이는범행기회가있다. | 추론된사실
> > 영은과예성은같은동네에거주한다. | 추론된사실
> > > 예성은동네공원에서영은과함께산책을즐겼다. | 추론된사실
> > > > 예성은영은이참여하는동네주민모임에자주참석했다. | 스토리에서추출된사실
> > > > 예성은동네공원에서영은과함께산책을즐겼다. | 스토리에서추출된사실
> > > > 동일한사회활동과장소에서자주만나는사람들은같은동네에거주할가능성이
높다. | 상식
> > > 영은은동네의주민모임에서예성을자주만났다. | 추론된사실
> > > > 예성은동네공원에서영은과함께산책을즐겼다. | 스토리에서추출된사실
> > > > 예성은영은이참여하는동네주민모임에자주참석했다. | 스토리에서추출된사실
> > > > 동일한사회활동과장소에서자주만나는사람들은같은동네에거주할가능성이
높다. | 상식
> > > 동일한사회활동과장소에서자주만나는사람들은같은동네에거주할가능성이높다.
| 상식
> > 예성은최근에자주영은의차를수리해주었다. | 추론된사실
> > > 예성은기계에익숙한목수로서차량수리에능숙하다. | 추론된사실
> > > > 예성은영은이차량문제로자주도움을요청했다고말했다. | 스토리에서추출된사실
> > > > 예성은목수로서손재주가뛰어나다. | 스토리에서추출된사실
> > > > 목수들은보통손재주가뛰어나고, 기계적인문제를해결하는데능숙하다. | 상식
> > > 예성은영은이차량문제로자주도움을요청했다고말했다. | 추론된사실
> > > > 예성은이웃들에게친절한목수로알려져있다. | 스토리에서추출된사실
> > > > 영은의차량은최근잦은고장을겪었다. | 스토리에서추출된사실
> > > > 목수들은손재주가뛰어나고, 기계적인문제를해결하는데능숙하다. | 상식
> > > 이웃이차량문제로도움을요청하여자주수리를해주면, 그차량에접근할기회를
가지게된다. | 상식
> > 같은동네에살면서자주차를수리해줬다면, 자연스럽게차에접근할기회를가질수
있다. | 상식
> 예성이는범행동기가있다. | 추론된사실
> > 예성은영은이다른사람과가까워질때마다강한질투심을느꼈다. | 추론된사실
> > > 영은은최근새로운친구들과시간을보내며사회생활을활발히하고있다. | 추론된
사실
> > > > 그스포츠클럽은많은사회적인활동과모임을제공한다. | 스토리에서추출된사실
> > > > 영은은새로운스포츠클럽에가입했다. | 스토리에서추출된사실
> > > > 새로운사회적환경은종종더많은사람들과의상호작용을가져올수있다. | 상식
> > > 예성은영은이다른사람과의만남을늘피하려했다. | 추론된사실
> > > > 예성은영은과의개인적인시간을중요시했고, 그녀가점점더많은사회적활동에
빠져드는것을불편해했다. | 스토리에서추출된사실
> > > > 예성은영은이새로운스포츠클럽에가입한후다른사람들과함께시간을보내는
것을좋아하지않았다. | 스토리에서추출된사실
> > > > 사람들은종종사랑하는사람이다른사람과가까워지면질투심을느끼고그들을
독점하고싶어하는경향이있다. | 상식
> > > 사람들은정서적소유욕이나질투심을느끼면, 사랑하는사람의사회적상호작용에
강한반응을보이기도한다. | 상식
> > 예성은영은에대해병적인집착을가지고있다. | 추론된사실
> > > 예성은영은을지켜보며그녀의일거수일투족을알고싶어했다. | 추론된사실
> > > > 예성은영은의사회적미디어활동을지속적으로체크했다. | 스토리에서추출된사실
65

--- Page 66 ---

> > > > 예성은영은이가는모든곳을따라다녔다. | 스토리에서추출된사실
> > > > 타인의일거수일투족을알고싶어하는경향은집착에서비롯될수있다. | 상식
> > > 예성은영은과의매일함께저녁시간을보내지않으면불안해했다. | 추론된사실
> > > 병적인집착은상대방에대한지나친관심과통제욕구로이어질수있다. | 상식
> > 병적인집착과강한질투심은때때로사람을극단적인행동, 심지어폭력이나살인까지
저지르게할수있다. | 상식
예슬| 추론된결론
> 예슬이는범행수단이있다. | 추론된사실
> > 예슬이는요리를자주했다. | 추론된사실
> > > 예슬이는다양한요리법을시험해보는것을즐겼다. | 추론된사실
> > > > 예슬이는다양한요리강습을들었다. | 스토리에서추출된사실
> > > > 예슬이는새로운요리책을수집하는것을즐긴다. | 스토리에서추출된사실
> > > > 요리에대한열정은새로운도구와기술을탐구하고실험하게만든다. | 상식
> > > 예슬이는일주일에여러번가족을위해저녁을준비했다. | 추론된사실
> > > > 예슬이는가족을위한식사준비에책임이있다. | 스토리에서추출된사실
> > > > 예슬이는가족들과함께사는대가족의일부이다. | 스토리에서추출된사실
> > > > 대가족의일원으로서, 자주식사준비를맡고있는사람은요리를정기적으로해야할
필요성이있다. | 상식
> > > 요리를자주준비하는사람은다양한요리법을시도하고자주요리하는경향이있다. |
상식
> > 예슬이는주방에서고기손질용도끼를가지고있었다. | 추론된사실
> > > 예슬이는주방도구를수집하는취미가있다. | 추론된사실
> > > > 예슬이는특별한주방도구들을친구들사이에서자랑한다. | 스토리에서추출된사실
> > > > 예슬이는고급주방용품점에서자주쇼핑을한다. | 스토리에서추출된사실
> > > > 주방도구에대한열정은사람들로하여금이러한도구를수집하고자랑하고자하는
욕구를불러일으킬수있다. | 상식
> > > 예슬이는고기요리를즐긴다. | 추론된사실
> > > > 예슬이는정기적으로고기전문점을방문하여다양한고기를구매한다. | 스토리에서
추출된사실
> > > > 예슬이는고기를사용한새로운레시피를자주시도한다. | 스토리에서추출된사실
> > > > 고기전문점을자주방문하고다양한레시피를시도하는사람은자연스럽게고기
손질기술을습득하고, 이에필요한도구를사용할가능성이높다. | 상식
> > > 고기요리를자주하는사람은고기손질용도끼와같은주방도구를사용할가능성이
높다. | 상식
> > 요리를자주하는사람은주방도구, 특히고기손질용도끼와같은도구의사용에익숙할
수있다. | 상식
> 예슬이는범행기회가있다. | 추론된사실
> > 예슬이는그날영은과함께차에타고있었다. | 추론된사실
> > > 예슬과영은은가족행사에서함께집으로돌아가기로했다. | 추론된사실
> > > > 예슬과영은은같은집에살고있었다. | 스토리에서추출된사실
> > > > 예슬과영은은대가족의모임에서같은장소로돌아가야했다. | 스토리에서추출된
사실
> > > > 대가족모임후, 같은장소로돌아가야하는가족구성원은함께이동하는경우가많다.
| 상식
> > > 예슬이는대가족의가족행사에참석중이었다. | 추론된사실
> > > > 예슬과영은은대가족의모임에서같은장소로돌아가야했다. | 스토리에서추출된
사실
> > > > 예슬과영은은같은집에살고있었다. | 스토리에서추출된사실
> > > > 대가족모임후, 같은장소로돌아가야하는가족구성원은함께이동하는경우가많다.
66

--- Page 67 ---

| 상식
> > > 가족행사는참석자들이함께이동하는경우가많다. | 상식
> > 예슬이는영은이자주타고다니는차의열쇠를가지고있었다. | 추론된사실
> > > 예슬은집안의중요한물건, 특히차량열쇠를책임지고있다. | 추론된사실
> > > > 예슬은가정에서신뢰받는어른으로인정받고있다. | 스토리에서추출된사실
> > > > 예슬은대가족의중요한결정을관리한다. | 스토리에서추출된사실
> > > > 가정에서어른들은종종차량열쇠와같은중요한물건의관리책임을맡는다. | 상식
> > > 예슬은가족들이자주사용하는차를관리한다. | 추론된사실
> > > > 예슬은가족의여러활동을조율하는역할을담당하고있다. | 스토리에서추출된사실
> > > > 예슬은가족과가까운관계를유지하고있다. | 스토리에서추출된사실
> > > > 가족의활동을조율하는사람은자주사용하는차를관리할가능성이높다. | 상식
> > > 가정에서어른들은종종차량열쇠와같은중요한물건의관리책임을맡는다. | 상식
> > 누군가차의열쇠를가지고있고, 피해자와함께차에타고있는상황은그들이그차에서
범행을저지를기회를제공한다. | 상식
> 예슬이는범행동기가있다. | 추론된사실
> > 영은은예슬이배우자의외도를알고있는것을알고있었다. | 추론된사실
> > > 영은은예슬에게외도에대해직접적으로경고했다. | 추론된사실
> > > > 예슬은영은이자주가는장소에서배우자와함께있는것을목격했다. | 스토리에서
추출된사실
> > > > 영은은예슬에게직접적으로외도에대해경고했다. | 스토리에서추출된사실
> > > > 외도사실이밝혀질때마다, 관련자가그사실을인지하고있을가능성은높아진다. |
상식
> > > 예슬은영은이자주가는장소에서배우자와함께있는것을목격했다. | 추론된사실
> > > > 예슬은영은과배우자가비밀스러운행동을하고있는것을목격했다. | 스토리에서
추출된사실
> > > > 예슬은영은이자주가는카페에서배우자를목격했다. | 스토리에서추출된사실
> > > > 정기적으로같은장소에서누군가를목격하는것은그들의행동을자세히관찰할
기회를제공한다. | 상식
> > > 외도사실이밝혀질때마다, 관련자가그사실을인지하고있을가능성은높아진다. |
상식
> > 예슬이는배우자의외도를발견했다. | 추론된사실
> > > 예슬은영은과배우자가함께있는현장을우연히지나치다목격했다. | 추론된사실
> > > > 예슬은길을걷다가우연히레스토랑의창문을통해그들을보았다. | 스토리에서
추출된사실
> > > > 예슬은영은과배우자가비밀스러운레스토랑에서만나는것을목격했다. | 스토리에
서추출된사실
> > > > 사람들이친밀한장소에서비밀리에만나는것을보면, 이는외도를의심하게만든다.
| 상식
> > > 예슬은배우자를주의깊게관찰한끝에, 평소와다른행동을목격했다. | 추론된사실
> > > 어떤사람의행동이비정상적이거나예측할수없는방식으로바뀌게되면, 주변
사람들은이를의심하고조사하게되는경향이있다. | 상식
> > 배우자의외도를발견하면감정적격분이나배신감으로인해극단적인행동을유발할수
있다. | 상식
Figure 36: Murder Mystery Example Reasoning Tree
Yesung | Deduced Root Conclusion
> Yesung has a means. | Deduced Fact
> > Yesung often uses an axe when cutting meat. | Deduced Fact
67

--- Page 68 ---

> > > Yesung uses a meat-cutting axe for processing meat. | Deduced Fact
> > > > Yesung regularly cooks meat dishes. | Fact from Story
> > > > Yesung owns a meat-cutting axe. | Fact from Story
> > > > People who cook meat frequently tend to use specific tools for meat preparation. |
Commonsense Knowledge
> > > Yesung often cooks meat in the kitchen. | Deduced Fact
> > > > Yesung owns a meat-cutting axe. | Fact from Story
> > > > Yesung regularly cooks meat dishes. | Fact from Story
> > > > People who cook meat frequently tend to use specific tools for meat preparation. |
Commonsense Knowledge
> > > People who frequently cook meat tend to use proper tools for processing it. | Commonsense
Knowledge
> > Yesung, as a carpenter, owns various tools. | Deduced Fact
> > > Yesung has multiple woodworking tools. | Deduced Fact
> > > > Yesung regularly inspects and maintains tools for work. | Fact from Story
> > > > Yesung works as a carpenter and often organizes his workspace. | Fact from Story
> > > > Carpenters typically possess a variety of tools to ensure smooth work. | Commonsense
Knowledge
> > > Yesung performs woodworking tasks regularly. | Deduced Fact
> > > > Yesung works as a carpenter and often organizes his workspace. | Fact from Story
> > > > Yesung regularly inspects and maintains tools for work. | Fact from Story
> > > > People engaged in woodworking generally own diverse tools necessary for their tasks. |
Commonsense Knowledge
> > > People engaged in woodworking generally own diverse tools necessary for their tasks. |
Commonsense Knowledge
> > If Yesung is a carpenter, he can easily access various tools, and if he owns a meat-cutting axe,
he could use it in the crime. | Commonsense Knowledge
> Yesung has an opportunity. | Deduced Fact
> > Yeong-eun and Yesung live in the same neighborhood. | Deduced Fact
> > > Yesung enjoyed walks with Yeong-eun in the local park. | Deduced Fact
> > > > Yesung frequently attended community meetings where Yeong-eun participated. | Fact
from Story
> > > > Yesung enjoyed walks with Yeong-eun in the local park. | Fact from Story
> > > > People who frequently meet at the same social gatherings and locations are likely to live
in the same area. | Commonsense Knowledge
> > > Yeong-eun often met Yesung at neighborhood gatherings. | Deduced Fact
> > > > Yesung enjoyed walks with Yeong-eun in the local park. | Fact from Story
> > > > Yesung frequently attended community meetings where Yeong-eun participated. | Fact
from Story
> > > > People who frequently meet at the same social gatherings and locations are likely to live
in the same area. | Commonsense Knowledge
> > > People who frequently meet at the same social gatherings and locations are likely to live in
the same area. | Commonsense Knowledge
> > Yesung has recently repaired Yeong-eun’s car multiple times. | Deduced Fact
> > > Yesung, being a skilled carpenter, is proficient in mechanical repair. | Deduced Fact
> > > > Yesung mentioned that Yeong-eun often asked for help with car issues. | Fact from Story
> > > > Yesung is known as a skillful carpenter. | Fact from Story
> > > > Carpenters are typically dexterous and adept at solving mechanical problems. |
Commonsense Knowledge
> > > Yesung mentioned that Yeong-eun often asked for help with car issues. | Deduced Fact
68

--- Page 69 ---

> > > > Yesung is known among neighbors as a kind carpenter. | Fact from Story
> > > > Yeong-eun’s car had frequent breakdowns recently. | Fact from Story
> > > > Carpenters are typically dexterous and adept at solving mechanical problems. |
Commonsense Knowledge
> > > When a neighbor frequently requests help for car troubles, the helper naturally gains access
to the car. | Commonsense Knowledge
> > Living in the same neighborhood and frequently repairing someone’s car naturally grants
access to it. | Commonsense Knowledge
> Yesung has a motive. | Deduced Fact
> > Yesung felt intense jealousy whenever Yeong-eun grew close to others. | Deduced Fact
> > > Yeong-eun has recently been socializing actively with new friends. | Deduced Fact
> > > > The sports club offers numerous social activities and gatherings. | Fact from Story
> > > > Yeong-eun joined a new sports club. | Fact from Story
> > > > New social environments often lead to increased interpersonal interactions. | Common-
sense Knowledge
> > > Yesung tried to avoid Yeong-eun’s new acquaintances. | Deduced Fact
> > > > Yesung valued his private time with Yeong-eun and felt uncomfortable as she engaged
more in social activities. | Fact from Story
> > > > Yesung disliked Yeong-eun spending time with others after joining the sports club. | Fact
from Story
> > > > People often feel jealousy and desire exclusivity when someone they love becomes close
to others. | Commonsense Knowledge
> > > When people experience emotional possessiveness or jealousy, they may react strongly to a
loved one’s social interactions. | Commonsense Knowledge
> > Yesung has an obsessive attachment to Yeong-eun. | Deduced Fact
> > > Yesung constantly monitored Yeong-eun’s daily activities. | Deduced Fact
> > > > Yesung continuously checked Yeong-eun’s social media activities. | Fact from Story
> > > > Yesung followed Yeong-eun wherever she went. | Fact from Story
> > > > A desire to monitor every aspect of another person’s life often stems from obsession. |
Commonsense Knowledge
> > > Yesung felt anxious when he could not spend evenings with Yeong-eun. | Deduced Fact
> > > Excessive obsession often leads to extreme attention and controlling behavior toward others.
| Commonsense Knowledge
> > Pathological obsession and strong jealousy can sometimes drive people to extreme actions,
including violence or murder. | Commonsense Knowledge
Yeseul | Deduced Root Conclusion
> Yeseul has a means. | Deduced Fact
> > Yeseul frequently cooked. | Deduced Fact
> > > Yeseul enjoyed experimenting with various cooking methods. | Deduced Fact
> > > > Yeseul attended multiple cooking classes. | Fact from Story
> > > > Yeseul enjoyed collecting new cookbooks. | Fact from Story
> > > > Passion for cooking drives individuals to explore and experiment with new tools and
techniques. | Commonsense Knowledge
> > > Yeseul prepared dinner for family members several times a week. | Deduced Fact
> > > > Yeseul was responsible for preparing meals for the family. | Fact from Story
> > > > Yeseul lived as part of a large extended family. | Fact from Story
> > > > In a large family, those responsible for meal preparation often need to cook regularly. |
Commonsense Knowledge
> > > People who cook frequently tend to try various recipes and cook regularly. | Commonsense
69

--- Page 70 ---

Knowledge
> > Yeseul possessed a meat-cleaving axe in the kitchen. | Deduced Fact
> > > Yeseul had a hobby of collecting kitchen tools. | Deduced Fact
> > > > Yeseul often showed off special kitchen utensils among friends. | Fact from Story
> > > > Yeseul frequently shopped at high-end kitchenware stores. | Fact from Story
> > > > Passion for kitchen tools can lead people to collect and display them. | Commonsense
Knowledge
> > > Yeseul enjoyed cooking meat dishes. | Deduced Fact
> > > > Yeseul regularly visited butcher shops to purchase various meats. | Fact from Story
> > > > Yeseul often tried new recipes involving meat. | Fact from Story
> > > > People who frequently visit butcher shops and try new recipes naturally acquire
meat-handling skills and use specialized tools. | Commonsense Knowledge
> > > Those who often cook meat are likely to use tools such as meat-cleaving axes. |
Commonsense Knowledge
> > People who cook frequently are familiar with kitchen tools, particularly those like
meat-cleaving axes. | Commonsense Knowledge
> Yeseul has an opportunity. | Deduced Fact
> > Yeseul was in the car with Yeongeun that day. | Deduced Fact
> > > Yeseul and Yeongeun decided to return home together after a family event. | Deduced Fact
> > > > Yeseul and Yeongeun lived in the same house. | Fact from Story
> > > > Yeseul and Yeongeun were returning from a large family gathering to the same place. |
Fact from Story
> > > > Family members who return to the same destination after a family gathering often travel
together. | Commonsense Knowledge
> > > Yeseul attended the extended family gathering. | Deduced Fact
> > > > Yeseul and Yeongeun were returning from the same family event. | Fact from Story
> > > > Yeseul and Yeongeun lived together. | Fact from Story
> > > > Family members returning to the same destination after a gathering often travel together. |
Commonsense Knowledge
> > > It is common for family event attendees to travel together afterward. | Commonsense
Knowledge
> > Yeseul possessed the car key often used by Yeongeun. | Deduced Fact
> > > Yeseul was responsible for managing important household items such as car keys. | Deduced
Fact
> > > > Yeseul was recognized as a trusted adult within the household. | Fact from Story
> > > > Yeseul managed important family decisions. | Fact from Story
> > > > Adults in a household are often entrusted with important possessions such as car keys. |
Commonsense Knowledge
> > > Yeseul managed the car frequently used by the family. | Deduced Fact
> > > > Yeseul coordinated family activities. | Fact from Story
> > > > Yeseul maintained close relationships with family members. | Fact from Story
> > > > A person who coordinates family activities is likely to manage the commonly used car. |
Commonsense Knowledge
> > > Adults in a household are often responsible for managing important items such as car keys. |
Commonsense Knowledge
> > Possessing the car key and being in the same car as the victim provides an opportunity to
commit a crime. | Commonsense Knowledge
> Yeseul has a motive. | Deduced Fact
> > Yeongeun knew that Yeseul was aware of her spouse’s affair. | Deduced Fact
> > > Yeongeun directly warned Yeseul about the affair. | Deduced Fact
70

--- Page 71 ---

> > > > Yeseul witnessed Yeongeun with Yeseul’s spouse at a place Yeongeun frequented. | Fact
from Story
> > > > Yeongeun explicitly warned Yeseul about the affair. | Fact from Story
> > > > When an affair becomes known, it is likely that involved parties are aware of each other’s
knowledge. | Commonsense Knowledge
> > > Yeseul saw Yeongeun and her spouse together at a place Yeongeun often visited. | Deduced
Fact
> > > > Yeseul witnessed Yeongeun and the spouse behaving secretively. | Fact from Story
> > > > Yeseul saw her spouse at the café Yeongeun frequented. | Fact from Story
> > > > Observing someone repeatedly at the same location provides opportunities to closely
monitor their behavior. | Commonsense Knowledge
> > > When an affair is revealed, those involved are likely to be aware of each other’s awareness. |
Commonsense Knowledge
> > Yeseul discovered her spouse’s affair. | Deduced Fact
> > > Yeseul accidentally witnessed Yeongeun and the spouse together. | Deduced Fact
> > > > Yeseul saw them through a restaurant window while walking down the street. | Fact from
Story
> > > > Yeseul saw Yeongeun and the spouse meeting secretly in a restaurant. | Fact from Story
> > > > Witnessing secret meetings in intimate places often leads to suspicion of infidelity. |
Commonsense Knowledge
> > > Yeseul carefully observed the spouse’s behavior and noticed unusual actions. | Deduced Fact
> > > When a person’s behavior changes unpredictably, people around them tend to become
suspicious and investigate. | Commonsense Knowledge
> > Discovering a spouse’s affair can lead to intense emotional distress or feelings of betrayal,
potentially causing extreme actions. | Commonsense Knowledge
Figure 37: Murder Mystery Example Reasoning Tree (Translated)
I.2
Object Placements
영수는실험실책상위에놓인노트북과USB를다시한번확인하며안도의한숨을내쉬었다.
주말이면제출해야할중요한프로젝트가머릿속을가득채우고있었지만, 모든실험결과와
자료가든USB가안전하게보관되어있다는사실에조금이나마마음이놓인것이다. 지민은
실험실안을부지런히정리하며영수가프로젝트에오롯이집중할수있도록돕고있었다. 그
는노트북과USB가실험실책상에놓여있다는것을정확히알고있었고, 깔끔한환경에서
영수의연구효율을높이고자했다. 은혁역시연구실의데이터보안을책임지는사람답게
이두물건을주시하고있었다. 그는USB 속민감한자료가외부로새어나가지않도록주의
깊게점검하며, 노트북이안전하다는사실도재차확인했다. 사실이곳에있는세사람모두
노트북과USB가실험실책상위에놓여있다는것을알고있었으며, 그어느때보다신중하게
프로젝트를준비하고보안을지키려했다.
지민은노트북을창고선반으로옮겼다. 영수는정리직전에그장비바로옆에서있었다.
지민은실험종료직후, 영수에게그장비정리계획을간단히언급했다. 은혁은지민가까이
에서주위를살펴보고있었다. 지민은정리직전에은혁에게잠시보관계획을언급했다.
영수는USB를작업대서랍으로옮겼다. 영수는서랍앞에서그장치를다룰준비를하고
있었다. 은혁은영수의곁에서프로젝트진행을확인하며지민가까이에서주위를살펴보고
있었다. 지민은정리직전에은혁에게잠시보관계획을언급했다.
은혁은USB를보안금고로옮겼다. 영수는은혁에게진행될절차에대해집중적으로
물어보고있었다. 은혁은영수옆에서필요한단계를차근차근설명할준비를하고있었다.
71

--- Page 72 ---

지민은실험이끝난뒤남은도구정리에몰두했고, 프로젝트진행상황을질문하며상대의
대답에만주의를기울였다.
이로써이이야기는여기서끝이났다.
문제: 주어진이야기를고려할때, 영수는USB를찾기위해어디를가장먼저확인하겠는가?
1 - 보안금고
2 - 실험실책상
3 - 작업대서랍
4 - 창고선반
정답: 1 - 보안금고
Figure 38: Object Placement Example
Youngsoo let out a sigh of relief as he double-checked the laptop and USB drive on the laboratory
desk. The important project due over the weekend weighed heavily on his mind, but he felt
reassured knowing that the USB—containing all his experimental results and data—was safely
stored. Jimin busily organized the lab to help Youngsoo focus entirely on his project. He knew
precisely that both the laptop and the USB were on the lab desk and wanted to maintain a tidy
environment to improve Youngsoo’s research efficiency. Eunhyuk, responsible for the lab’s data
security, also kept a close eye on the two items. He carefully inspected them to ensure that the
sensitive data inside the USB would not leak externally and confirmed once again that the laptop
was safe. In fact, all three of them knew that the laptop and USB were on the lab desk and were
more cautious than ever as they worked to protect their project and data security.
Jimin moved the laptop to the storage shelf. Youngsoo was standing right next to the equipment
just before it was moved. Jimin briefly mentioned his plan to organize the equipment to Youngsoo
right after the experiment ended. Eunhyuk was nearby, observing the surroundings carefully. Just
before organizing, Jimin also briefly mentioned his storage plan to Eunhyuk.
Youngsoo moved the USB to the workbench drawer. He stood in front of the drawer, ready to han-
dle the device. Eunhyuk was beside Youngsoo, checking on the project’s progress while keeping an
eye on Jimin nearby. Jimin, just before finishing up, briefly mentioned his storage plan to Eunhyuk.
Eunhyuk moved the USB to the secure safe. At that moment, Youngsoo was asking Eunhyuk
detailed questions about the procedures. Eunhyuk stood next to Youngsoo, ready to explain each
step carefully. Jimin, after the experiment ended, was busy tidying up the remaining tools and
only paid attention to the answers when asking about the project’s progress.
And so, the story ends here.
Question: Based on the story, where would Youngsoo most likely look first to find the USB?
1 - Secure safe
2 - Laboratory desk
3 - Workbench drawer
4 - Storage shelf
Answer: 1 - Secure safe
72

--- Page 73 ---

Figure 39: Object Placement Example (Translated)
영수는중요한프로젝트의자료를USB에저장해가지고있습니다. USB를잃어버리면
프로젝트제출이불가능해집니다. | 추론된결론
> 이야기시작| 추론된사실
> > 영수가노트북을실험실책상에서보았다. | 스토리에서추출된사실
> > 영수가USB를실험실책상에서보았다. | 스토리에서추출된사실
> > 은혁이노트북을실험실책상에서보았다. | 스토리에서추출된사실
> > 은혁이USB를실험실책상에서보았다. | 스토리에서추출된사실
> > 지민이노트북을실험실책상에서보았다. | 스토리에서추출된사실
> > 지민이USB를실험실책상에서보았다. | 스토리에서추출된사실
> 지민이노트북을창고선반으로옮긴다. 왜냐하면, 지민은실험이끝난후실험실의공간을
확보하기위해노트북을정리합니다. | 추론된사실
> > 영수는노트북을창고선반으로이동하는것을보았다. | 추론된사실
> > > 지민은실험종료직후, 영수에게그장비정리계획을간단히언급했다. | 스토리에서
추출된사실
> > > 영수는정리직전에그장비바로옆에서있었다. | 스토리에서추출된사실
> > > 가까운거리에서무엇을옮기면, 주변에있는사람은쉽게그상황을인지한다. | 상식
> > 은혁이는노트북을창고선반으로이동하는것을보았다. | 추론된사실
> > > 은혁은지민가까이에서주위를살펴보고있었다. | 스토리에서추출된사실
> > > 지민은정리직전에은혁에게잠시보관계획을언급했다. | 스토리에서추출된사실
> > > 가까운곳에서물건이움직이면, 가까이에있는사람은그상황을쉽게인지한다. | 상식
> 영수가USB를작업대서랍으로옮긴다. 왜냐하면, 영수는중요한자료를안전한장소에
보관하기위해가까운서랍에넣어두기로결정합니다. | 추론된사실
> > 은혁이는USB를작업대서랍으로이동하는것을보았다. | 추론된사실
> > > 영수는서랍앞에서그장치를다룰준비를하고있었다. | 스토리에서추출된사실
> > > 은혁은영수의곁에서상황을살피며프로젝트진행을확인하고있었다. | 스토리에서
추출된사실
> > > 가까운환경에서일어나는행동은주변인물이쉽게인지할수있다. | 상식
> > 지민이는USB를작업대서랍으로이동하는것을보지않았다. | 추론된사실
> > > 은혁은지민가까이에서주위를살펴보고있었다. | 스토리에서추출된사실
> > > 지민은정리직전에은혁에게잠시보관계획을언급했다. | 스토리에서추출된사실
> > > 누군가가다른사람과대화에집중하면, 주위에서일어나는다른일을놓칠수도있다. |
상식
> 은혁이USB를옮긴다. 왜냐하면, 은혁은자료의보안을강화하기위해USB를안전하게
보관합니다. | 추론된사실
> > 영수는USB가이동하는것을보았다. | 추론된사실
> > > 은혁은영수바로옆에서필요한단계를차근차근설명할준비를하고있었다. |
스토리에서추출된사실
> > > 영수는은혁에게진행될절차에대해집중적으로물어보고있었다. | 스토리에서추출된
사실
> > > 가까운자리에서함께과정을논의한다면, 진행상황을자연스럽게지켜보게된다. |
상식
> > 지민이는USB가이동하는것을보지않았다. | 추론된사실
> > > 지민은실험이끝난뒤, 남은도구정리에몰두하고있었다. | 스토리에서추출된사실
> > > 지민은영수가맡은프로젝트진행상황을질문하며, 상대의대답에만주의를기울였다.
| 스토리에서추출된사실
> > > 누군가가한가지일에집중하면, 동시에벌어지는다른일을놓치기쉽다. | 상식
Figure 40: Object Placement Example Reasoning Tree
73

--- Page 74 ---

Yeongsu stores important project data in a USB drive. If the USB is lost, it will be impossible to
submit the project. | Deduced Conclusion
> Beginning of the story | Deduced Fact
> > Yeongsu saw the laptop on the laboratory desk. | Fact From Story
> > Yeongsu saw the USB on the laboratory desk. | Fact From Story
> > Eunhyeok saw the laptop on the laboratory desk. | Fact From Story
> > Eunhyeok saw the USB on the laboratory desk. | Fact From Story
> > Jimin saw the laptop on the laboratory desk. | Fact From Story
> > Jimin saw the USB on the laboratory desk. | Fact From Story
> Jimin moves the laptop to the storage shelf because she wants to clear space in the lab after the
experiment. | Deduced Fact
> > Yeongsu saw the laptop being moved to the storage shelf. | Deduced Fact
> > > Right after the experiment ended, Jimin briefly mentioned her plan to organize the
equipment to Yeongsu. | Fact From Story
> > > Yeongsu was standing right next to the equipment just before it was moved. | Fact From
Story
> > > When something is moved at close range, nearby people can easily notice it. | Commonsense
Knowledge
> > Eunhyeok saw the laptop being moved to the storage shelf. | Deduced Fact
> > > Eunhyeok was nearby, keeping an eye on the surroundings. | Fact From Story
> > > Jimin briefly mentioned her storage plan to Eunhyeok before organizing. | Fact From Story
> > > When an object is moved nearby, people close to it can easily perceive the situation. |
Commonsense Knowledge
> Yeongsu moves the USB to the workbench drawer because he decides to keep it in a nearby,
secure place for safekeeping. | Deduced Fact
> > Eunhyeok saw the USB being moved to the workbench drawer. | Deduced Fact
> > > Yeongsu was preparing to handle the device in front of the drawer. | Fact From Story
> > > Eunhyeok was beside Yeongsu, observing the situation and checking project progress. | Fact
From Story
> > > Actions occurring in close proximity are easily recognized by nearby people. | Commonsense
Knowledge
> > Jimin did not see the USB being moved to the workbench drawer. | Deduced Fact
> > > Eunhyeok was near Jimin, looking around the area. | Fact From Story
> > > Jimin briefly discussed the storage plan with Eunhyeok before cleaning up. | Fact From
Story
> > > When someone is focused on a conversation, they may miss other events happening around
them. | Commonsense Knowledge
> Eunhyeok moves the USB because he wants to strengthen data security by storing it safely. |
Deduced Fact
> > Yeongsu saw the USB being moved. | Deduced Fact
> > > Eunhyeok was standing right next to Yeongsu, preparing to explain the necessary steps. |
Fact From Story
> > > Yeongsu was asking detailed questions about the upcoming procedure. | Fact From Story
> > > When two people discuss a process closely together, they naturally observe the ongoing
actions. | Commonsense Knowledge
> > Jimin did not see the USB being moved. | Deduced Fact
> > > After the experiment ended, Jimin was absorbed in tidying up the remaining tools. | Fact
From Story
> > > Jimin was asking Yeongsu about the project’s progress, focusing solely on his responses. |
74

--- Page 75 ---

Fact From Story
> > > When someone concentrates on one task, it is easy to miss other things happening
simultaneously. | Commonsense Knowledge
Figure 41: Object Placement Example Reasoning Tree (Translated)
I.3
Team Allocations
어느따뜻한봄날아침, 새로운소셜미디어플랫폼을만들기위해모인팀의매니저로서나는
사무실창밖을바라보며오늘의과제를떠올렸다. 콘텐츠제작자와사용자안전관리자로
적합한인물을찾는일이었다. 팀에는지훈, 소영, 민지라는세명의주목할만한인물이
있었고, 그들의강점과약점을잘알고있었기에배치가고민스러웠다.
먼저지훈은과거에다양한영상콘텐츠를제작한경험이있는사람이었다.
그는창의적인아이디어로팀에서자주인정받았지만, 규칙이나절차를따르는것을힘들어
했다. 세부사항에대한주의를기울이지않아문제가되기도했고, 민지와의협업에서는종종
의견충돌을겪곤했다. 게다가그는소영의의견을잘듣지않는경향이있었다.
소영은관리및계획에더큰관심을보였으며창의적인프로젝트보다는큰그림을보는
것을선호했다. 그러나그녀는비디오편집소프트웨어사용경험이거의없었고, 과거
프로젝트에서반복적으로작은실수를하기도했다. 소영은또한상세한규정준수보다는
포괄적인접근을선호하여, 때때로민지가결정을내릴때주저한다고느꼈다. 소영은
지훈과의의사소통에서좌절감을느끼기도했다.
마지막으로민지는분석적인업무에강점을보여왔지만, 복잡한규정을이해하고적용하는
데어려움을겪었다. 또한, 콘텐츠제작과정에서창의적인아이디어를도출하는데어려움을
겪었고지나치게혼란한상황에서침착함을유지하기어려웠다. 민지는지훈의작업스타
일을비효율적이라고여겼으며, 소영과함께했던이전프로젝트에서는중요한결정이항상
지연되었다고보고했다.
이세사람을놓고생각해보면, 각자의고유한강점과약점이조화를이루도록적절한배치를
찾는것이중요했다. 콘텐츠제작자와사용자안전관리자로이들을어떻게나누어야할지
고민이깊어졌다. 완벽한대답은존재하지않을지도모른다. 어느쪽이든, 그들의개성과
역량을최대로끌어내기위해서는잘못된조합을피하고, 이들의다양한특성을잘연결하는
것이핵심이었다. 위대한플랫폼의성공은결국올바른사람을올바른자리에배치하는데
있을것이기때문이다.
문제: 이이야기를바탕으로, 두가지업무가모두효율적으로수행되도록사람을어떻게
배정하시겠습니까?
선택지:
1. 콘텐츠제작자: 지훈, 사용자안전관리자: 민지와소영
2. 콘텐츠제작자: 소영, 사용자안전관리자: 민지와지훈
3. 콘텐츠제작자: 민지, 사용자안전관리자: 소영과지훈
정답: 1. 콘텐츠제작자: 지훈, 사용자안전관리자: 민지와소영
Figure 42: Team Allocation Example
75

--- Page 76 ---

One warm spring morning, as the manager of a team gathered to build a new social media
platform, I gazed out the office window and recalled today’s task: finding suitable members for the
roles of content creator and user safety manager. The team had three notable members—Jihoon,
Soyoung, and Minji—and knowing their strengths and weaknesses well made the decision all the
more difficult.
First, Jihoon had previous experience creating various video content.
He was often recognized for his creative ideas, but struggled to follow rules and procedures.
His lack of attention to detail had caused issues before, and he often clashed with Minji during
collaboration. Furthermore, he tended to disregard Soyoung’s opinions.
Soyoung, on the other hand, was more interested in management and planning, preferring to
see the big picture rather than focusing on creative projects. However, she had little experience
using video editing software and had made several small mistakes in past projects. Soyoung also
preferred broad approaches over strict compliance with detailed regulations, which sometimes
made Minji hesitant when making decisions. She also felt frustrated when communicating with
Jihoon.
Finally, Minji had shown strength in analytical tasks but struggled to understand and apply
complex regulations. She also found it difficult to generate creative ideas during the content
creation process and had trouble staying calm in overly chaotic situations. Minji considered
Jihoon’s work style inefficient and reported that important decisions were often delayed in
previous projects with Soyoung.
Considering these three individuals, it was important to find an arrangement where their
unique strengths and weaknesses could complement each other. I pondered deeply over
how to divide them between the roles of content creator and user safety manager. There
might not be a perfect answer, but to maximize their potential, it was essential to avoid poor
combinations and find a configuration that linked their diverse characteristics effectively. After all,
the success of a great platform ultimately depends on placing the right people in the right positions.
Question: Based on this story, how would you assign the people so that both tasks are performed
efficiently?
Choices:
1. Content Creator: Jihoon, User Safety Managers: Minji and Soyoung
2. Content Creator: Soyoung, User Safety Managers: Minji and Jihoon
3. Content Creator: Minji, User Safety Managers: Soyoung and Jihoon
Answer: 1. Content Creator: Jihoon, User Safety Managers: Minji and Soyoung
Figure 43: Team Allocation Example (Translated)
당신은새로운소셜미디어플랫폼을만들고있습니다. 콘텐츠제작팀과사용자안전팀을
어떻게나누어야할까요? | 추론된결론
> 지훈과민지는같이못일한다. | 추론된사실
> > 민지는지훈의작업스타일을비효율적이라고생각한다. | 스토리에서추출된사실
> > 지훈과민진은과거프로젝트에서협업할때항상의견충돌을겪었다. | 스토리에서추출
된사실
76

--- Page 77 ---

> > 사람들이과거에지속적으로의견충돌이있었다면, 다시함께일할때도충돌이발생할
가능성이높다. | 상식
> 지훈은콘텐츠제작자를할수있다. | 추론된사실
> > 지훈은창의적인아이디어로팀에서자주인정받는다. | 스토리에서추출된사실
> > 지훈은과거에다양한영상콘텐츠를제작한경험이있다. | 스토리에서추출된사실
> > 콘텐츠제작자는창의성과제작경험이중요한요소다. | 상식
> 지훈은사용자안전관리자를못한다. | 추론된사실
> > 지훈은과거프로젝트에서세부사항에대한주의를기울이지않아문제가되었다. | 스토
리에서추출된사실
> > 지훈은규칙이나절차를따르는것을힘들어한다. | 스토리에서추출된사실
> > 사용자안전관리자는규칙준수와세부사항에대한철저한관리가필요하다. | 상식
> 민지는콘텐츠제작자를못한다. | 추론된사실
> > 민지는주로분석적인업무에더강점을보인다. | 스토리에서추출된사실
> > 민지는콘텐츠제작과정에서창의적인아이디어를도출하는데어려움을겪는다. | 스토리
에서추출된사실
> > 콘텐츠제작자는창의력을요구하며, 분석적인성향보다는창의적인사고방식을필요로
한다. | 상식
> 민지는사용자안전관리자를못한다. | 추론된사실
> > 민지는복잡한규정을이해하고적용하는데어려움을겪는다. | 스토리에서추출된사실
> > 민지는지나치게혼란한상황에서침착함을유지하기어려워한다. | 스토리에서추출된
사실
> > 사용자안전관리자는복잡한상황에서도냉정함을유지하고규정을정확히이해하는것
이중요하다. | 상식
> 소영과민지는같이못일한다. | 추론된사실
> > 소영과민지는이전프로젝트에서중요한결정이항상지연되었다고보고했다. | 스토리에
서추출된사실
> > 소영은민지가결정을내릴때주저한다고느낀다. | 스토리에서추출된사실
> > 사람들이함께일할때결정지연이지속적으로발생하면, 향후에도같은문제가발생하는
경향이있다. | 상식
> 지훈과소영은같이못일한다. | 추론된사실
> > 소영은지훈과의의사소통에서좌절감을느꼈다. | 스토리에서추출된사실
> > 지훈은소영의의견을잘듣지않는경향이있다. | 스토리에서추출된사실
> > 의사소통이원활하지않으면, 효율적인협업이어렵다. | 상식
> 소영은콘텐츠제작자를못한다. | 추론된사실
> > 소영은창의적인프로젝트보다관리및계획에더관심이크다. | 스토리에서추출된사실
> > 소영은비디오편집소프트웨어사용경험이거의없다. | 스토리에서추출된사실
> > 콘텐츠제작자는창의적인기술과전문소프트웨어사용능력이필요하다. | 상식
> 소영은사용자안전관리자를못한다. | 추론된사실
> > 소영은세부적인규정준수보다는큰그림을보는것을선호한다. | 스토리에서추출된
사실
> > 소영은과거프로젝트에서반복적으로작은실수를했었다. | 스토리에서추출된사실
> > 사용자안전관리자는작은실수도치명적으로이어질수있어, 세부적인규정준수가
필수적이다. | 상식
Figure 44: Team Allocation Example Reasoning Tree
You are creating a new social media platform. How should you divide the content creation team
and the user safety team? | Deduced Conclusion
> Jihoon and Minji cannot work together. | Deduced Fact
77

--- Page 78 ---

> > Minji thinks Jihoon’s work style is inefficient. | Fact From Story
> > Jihoon and Minji always had conflicts when collaborating on past projects. | Fact From Story
> > If people have had continuous conflicts in the past, it is highly likely that conflicts will arise
again when they work together. | Commonsense Knowledge
> Jihoon can be a content creator. | Deduced Fact
> > Jihoon is often recognized by the team for his creative ideas. | Fact From Story
> > Jihoon has experience producing various video contents in the past. | Fact From Story
> > Creativity and production experience are important qualities for a content creator. | Common-
sense Knowledge
> Jihoon cannot be a user safety manager. | Deduced Fact
> > Jihoon once caused problems in past projects by failing to pay attention to details. | Fact From
Story
> > Jihoon finds it difficult to follow rules or procedures. | Fact From Story
> > A user safety manager must adhere to rules and pay close attention to detail. | Commonsense
Knowledge
> Minji cannot be a content creator. | Deduced Fact
> > Minji is generally stronger in analytical work. | Fact From Story
> > Minji struggles to come up with creative ideas during the content creation process. | Fact From
Story
> > A content creator requires creativity and needs a creative mindset rather than an analytical
one. | Commonsense Knowledge
> Minji cannot be a user safety manager. | Deduced Fact
> > Minji finds it difficult to understand and apply complex regulations. | Fact From Story
> > Minji has trouble staying calm in overly chaotic situations. | Fact From Story
> > A user safety manager must stay composed in complex situations and understand regulations
accurately. | Commonsense Knowledge
> Soyeong and Minji cannot work together. | Deduced Fact
> > Soyeong and Minji reported that important decisions were always delayed in their previous
project. | Fact From Story
> > Soyeong feels that Minji hesitates when making decisions. | Fact From Story
> > When people consistently experience decision-making delays while working together, similar
problems tend to occur in the future. | Commonsense Knowledge
> Jihoon and Soyeong cannot work together. | Deduced Fact
> > Soyeong felt frustrated when communicating with Jihoon. | Fact From Story
> > Jihoon tends not to listen well to Soyeong’s opinions. | Fact From Story
> > Ineffective communication makes efficient collaboration difficult. | Commonsense Knowledge
> Soyeong cannot be a content creator. | Deduced Fact
> > Soyeong is more interested in management and planning than in creative projects. | Fact From
Story
> > Soyeong has little experience using video editing software. | Fact From Story
> > A content creator needs creative technical skills and proficiency with professional software. |
Commonsense Knowledge
> Soyeong cannot be a user safety manager. | Deduced Fact
> > Soyeong prefers to focus on the big picture rather than on detailed rule compliance. | Fact
From Story
> > Soyeong repeatedly made small mistakes in past projects. | Fact From Story
> > In user safety management, even small mistakes can be critical, so strict compliance with
detailed regulations is essential. | Commonsense Knowledge
Figure 45: Team Allocation Example Reasoning Tree (Translated)
78

--- Page 79 ---

J
Examples for Human Evaluations
문제
동물원의한적한오후, 영은은전기충격기에의해살해되었고, 담당형사는재균과서율두
용의자를심문하기시작했다.
비가부슬부슬내리는동물원주차장에다다르자, 김형사는금속문소리를들으며날카로운
공기속에서서율의존재감을느꼈다. 그는늘그런식으로주변을압도하는기운을풍겼다. 김
형사는그의사무실로향하는길에중얼거리듯자신과보이지않는존재에대해이야기하던
그의말이머릿속을스쳤다. 그가불가해한말들을내뱉던때가한두번이아니었기때문이다.
사무실문을열고들어서자, 서율은눈에띄게피곤해보였다. 그는김형사를보자비즈니스
연필꽂이에서연필을하나뽑아손가락사이에서놀리며자리에서일어섰다.
“김형사님, 와주셔서감사해요. 제가도와드릴수있는게있을까요?” 서율이말했다.
“서율씨, 언제나그랬듯이동물원운영에대해몇가지물어보고싶습니다.” 김형사는점잖게
말했다.
김형사는간단히목소리를가다듬고다시질문을던졌다.
“영은씨와의관계는어떤가요? 최근에자주같이계신다는이야기를들었습니다.”
서율은잠시시선을피하더니다시김형사를바라보았다.
“글쎄요, 우리의사업적충돌은있었습니다. 하지만그이상은아닙니다.”
장미의가시사이로피뢰침이번쩍이는순간처럼서율의눈길이강하게빛났다.
김형사는그의말을듣고잠시생각에잠겼다. 모든것이명확하게서지않았지만, 이러한
모든이야기가얽히고설킨추리의일부처럼다가오는것을느꼈다. 이회색구름속에감춰진
진실을찾기위해김형사는서율을계속지켜봐야겠다는생각이들었다. 그런생각을하며,
김형사는다음으로움직였다.
김형사가동물원입구에도착했을때, 그는이미많은관중과경찰들로붐비는광경을목격
했다. 영은의사건이발생한현장은일반적인사건현장과는사뭇다른분위기를자아내고
있었다. 동물원의복잡한구조에도불구하고, 그는재빨리사건현장으로이동했다.
“아, 형사님. 그냥시간을좀확인하고있었습니다. 언제퇴근할수있는지요.”
재균은자연스럽게대답했다.
김형사는사무실내부를살펴보며중요한메모가놓여있는책상을발견했다. 재균이
개인적으로적어두는메모들이었다. 그는메모를눈으로훑어보다가, 동물원내부구조와
보안시스템에대해자세히기록한내용들을보고잠시멈칫했다.
“이메모는자주쓰시나요?” 김형사가물었다.
79

--- Page 80 ---

“네, 일을매끄럽게처리하기위해서요. 동물원의복잡한구조때문에도움을받곤합니다.”
재균은그럴듯하게설명했다.
김형사는재균이매일퇴근시간이다가올때마다동료들의책상을지나가며시간을확인
한다는이야기를들은바있었다. 사람들의출퇴근패턴을유심히살펴보는그를지켜보던
사람들도많았다.
“여기서일하면서특별히신경쓰는부분이있으신가요?” 형사는계속해서질문을던졌다.
“업무상보안시스템을잘알아야하니까요. 주로동료들이주로어두운구석에서대화를
나누는걸지켜보곤합니다.”
재균은담담하게대답했다. 김형사는다음질문을물었다.
"최근에영은씨와의관계는어땠나요?"
재균은잠시고개를떨군채침묵하다가조용히입을열었다.
“솔직히... 예전같지않았습니다. 처음엔서로도우며잘지냈지만, 요즘들어영은씨가저를
의심하는눈초리를보내곤했습니다.”
“의심이라면어떤부분을말씀하시는건가요?” 김형사는조용하지만단호한어조로되물었
다.
“전기장비점검기록이나출입구로그에대해제가잘못관리하고있다고동물원관리자에게
보고한것도그녀였죠. 덕분에저는조사까지받았고, 그일이후로동료들사이에서도신뢰를
잃었습니다. 저는그저제방식대로효율적으로일하려했을뿐이었는데...”
그의목소리에는억눌린분노가스며있었다. 김형사는조용히고개를끄덕이며속으로
정리했다. 다음으로, 김형사는재균이동물원의구조를너무나도잘알고있다는점을
주목했다. 재균의그늘에서의행동들은그리단순하지않다는것을암시하는듯했다. 형사는
재균주변을한바퀴돌아보며그가또무슨이야기를덧붙일지기다렸다.
“혹시임무에전기충격기가관련되는일은있었습니까?” 형사가묻자, 재균은잠시침묵했다.
“그런일이있었다면, 모두업무차원이었을것입니다.”
재균은말을얼버무렸다.
형사는더깊은이야기가나올것을기대하며, 재균의답변에귀를기울였다. 동물원의사건과
관련된비밀의실마리가, 이제조금씩드러날준비를하고있었다.
다음중살인자일가능성이가장높은사람은누구인가요?
다음중하나를선택하세요:
1 - 서율
2 - 재균
80

--- Page 81 ---

힌트
반드시하나의선택지만고르셔야합니다. 선택하기전에, 단계별로당신의추론과정을
설명하세요. 살인자는반드시세가지조건을충족해야합니다: 동기(피해자를죽일만한
이유가있는가), 수단(범행도구에접근할수있는가), 기회(범행현장에접근할수있었는가)
무고한용의자는이세가지중두가지까지만입증될수있으며, 의심스러운행동을보일
수는있어도세가지조건을모두갖추지는않습니다. 만약두용의자모두수단, 동기, 기회를
가진것처럼보인다면, 그중에서도가장명확하게이세가지가드러난인물을선택해야
합니다. 반대로, 어느누구도세가지를모두갖추지않은경우라면, 세가지조건중가장
뚜렷하게드러난인물을선택해야합니다.
단계별로논리적인추론을마친후, 정답을고르세요
예시풀이
두용의자를각각분석하여어떤용의자가범행동기, 범행수단, 범행기회를모두가지는지
추론해보겠습니다.
먼저, 서율에대해살펴보겠습니다.
서율은피해자인영은과사업적충돌이있었다고말합니다. 이는업무관계속에서갈등이있
었음을보여주며, 충분한살인의동기가될수있습니다. 따라서서율은범행동기가있습니다.
서율은전기충격기에접근할수있었는지, 다룰수있었는지에대한직접적인언급은없습니
다. 그의업무상전기충격기를사용할일에대한정보는전혀드러나있지않습니다. 따라서
서율은범행수단이없습니다.
서율은동물원직원으로사건당일동물원내부에있었고, 동물원운영에관련된사람이므로
범행장소에접근할수있는위치에있었습니다. 따라서서율은범행기회가있습니다.
다음으로재균에대해살펴보곘습니다.
재균은피해자인영은에대해직접적인불만과분노를드러냅니다. 영은이재균을상대로
관리문제를관리자에게보고했다고하였고, 그로인해재균이조사를받았으며동료들에게
신뢰를잃게된계기가되었습니다. 따라서재균은범행동기가있습니다.
형사가재균에게전기충격기관련임무가있었느냐고물었을때, 그는부정하지않고업무상
있었을수도있다고얼버무리는반응을보였습니다. 또한, 재균은전기장비점검기록을
관리하고동물원의보안시스템과구조에매우정통한인물입니다. 이는그가업무차원에서
전기충격기에접근할수있었고, 그사용법에대해서도알고있었을가능성을시사합니다.
따라서재균은범행수단이있습니다.
재균은동물원의출입동선과시간대에매우익숙하며, 사건발생시간전후로동물원내에서
활동하고있었던정황이있습니다. 동료들의퇴근시간까지관찰하고있었고, 동물원보안
시스템에익숙하며, 은밀한장소에서동료들의대화를지켜보는습관도언급됩니다. 이는
그가사건현장에몰래접근할수있는능력과기회를충분히가지고있었음을의미합니다.
따라서재균은범행기회가있습니다.
81

--- Page 82 ---

위의분석을정리해보면다음과같습니다:
서율은범행동기, 범행기회가있지만범행수단이없습니다.
재균은범행동기, 범행수단, 범행기회가모두있습니다.
따라서, 가장유력한살인용의자는재균입니다.
Figure 46: 1 Shot CoT Hint Example for Ko-MuSR - Murder Mysteries
Question
On a quiet afternoon at the zoo, Yeongeun was killed by an electric shock device, and Detective
Kim began interrogating the two suspects, Jaekyun and Seoyul.
As he arrived at the zoo’s quiet parking lot under a light drizzle, Detective Kim heard the metallic
creak of the gate and sensed Seoyul’s presence in the sharp air. He had always had that way of
dominating his surroundings with a certain aura. On his way to Seoyul’s office, Kim recalled
the man’s strange words about himself and unseen beings—muttered as if in conversation with
something invisible. It wasn’t the first time Seoyul had said such incomprehensible things.
When Kim opened the office door, Seoyul looked visibly exhausted. Upon seeing the detective, he
stood up, picking a pencil from a business-style holder and twirling it between his fingers.
“Detective Kim, thank you for coming. How can I help you?” said Seoyul.
“Seoyul, as always, I’d like to ask you a few questions about the zoo’s operations,” Kim replied
politely.
Kim cleared his throat slightly and continued his questioning.
“What was your relationship with Yeongeun? I’ve heard you’ve been spending time together
recently.”
Seoyul averted his gaze briefly before looking back at the detective.
“Well, we did have some business conflicts. But nothing beyond that.”
His eyes flashed sharply, like lightning striking between the thorns of a rose.
Kim paused to think. Nothing was entirely clear yet, but all these fragments felt like pieces of a
tangled mystery. To uncover the truth hidden in these gray clouds, Kim decided to keep a close
eye on Seoyul. With that thought, he moved on.
When Kim arrived at the zoo entrance, he saw crowds of onlookers and police officers. The crime
scene of Yeongeun’s death had an atmosphere unlike any other he had encountered. Despite the
zoo’s complex layout, he quickly made his way to the scene.
“Ah, Detective. I was just checking the time, wondering when I might get off work,” said Jaekyun
casually.
82

--- Page 83 ---

Kim scanned the office and noticed an important notebook on the desk—it contained Jaekyun’s
personal memos. Skimming through, he paused when he saw detailed notes about the zoo’s
internal layout and security systems.
“Do you often use these notes?” Kim asked.
“Yes, to make my work run smoothly. The zoo’s complex structure can be confusing, so they help
me,” Jaekyun replied plausibly.
Kim recalled hearing that Jaekyun routinely checked the time near coworkers’ desks as the day
ended. Many people had observed his habit of watching others’ comings and goings.
“Is there anything in particular you pay attention to while working here?” the detective continued.
“I need to know the security systems well for my job. I often notice colleagues chatting in dark
corners,” Jaekyun answered calmly.
“Recently, how was your relationship with Yeongeun?” Kim asked next.
Jaekyun lowered his head for a moment in silence before speaking quietly.
“To be honest... it wasn’t like before. We used to help each other, but lately, she’s been looking at
me with suspicion.”
“What kind of suspicion?” Kim asked in a calm but firm tone.
“She reported to the zoo manager that I mishandled maintenance logs and entry records. Because
of that, I was investigated and lost trust among my coworkers. I only wanted to do my job
efficiently in my own way. . . ”
His voice carried restrained anger. Kim nodded quietly, organizing his thoughts. He noted that
Jaekyun knew the zoo’s structure remarkably well. His shadowy behavior hinted at more than it
seemed. Kim walked around him, waiting for what he might say next.
“Was your work ever related to the electric shock device?” Kim asked. Jaekyun hesitated.
“If such a thing happened, it would have been purely work-related,” he mumbled.
Kim listened carefully, expecting something deeper. The threads of the zoo’s mystery were
beginning to unravel.
Who among the following is most likely to be the murderer?
Choose one of the following:
1 - Seoyul
2 - Jaekyun
Hint
83

--- Page 84 ---

You must choose only one option. Before choosing, explain your reasoning step by step. The
murderer must satisfy all three conditions: motive (a reason to kill the victim), means (access to
the murder weapon), and opportunity (access to the crime scene).
An innocent suspect can satisfy at most two of these conditions and may appear suspicious but
cannot fulfill all three. If both suspects seem to have motive, means, and opportunity, choose the
one for whom these are most clearly established. Conversely, if neither meets all three, select the
one who most clearly satisfies the conditions that are evident.
After reasoning logically step by step, choose your answer.
Example Solution
We will analyze each suspect to determine who possesses all three elements—motive, means, and
opportunity.
First, let’s examine Seoyul.
Seoyul admits to having business conflicts with the victim, Yeongeun. This shows there was
tension in their professional relationship, which could serve as a motive for murder. Therefore,
Seoyul has a motive.
There is no direct mention of Seoyul having access to or handling the electric shock device. His
job responsibilities do not appear to involve such equipment. Therefore, Seoyul lacks the means.
As a zoo employee present on the day of the incident and involved in zoo operations, Seoyul had
access to the crime scene. Therefore, he had the opportunity.
Next, let’s consider Jaekyun.
Jaekyun expresses direct resentment and anger toward the victim. Yeongeun reported him to the
zoo manager for mishandling maintenance records, leading to an investigation and a loss of trust
among colleagues. Thus, Jaekyun had a motive.
When asked whether his duties involved the electric shock device, Jaekyun neither denied nor
confirmed it, implying possible involvement. He also manages electrical inspection logs and is
highly knowledgeable about the zoo’s security systems and layout. This suggests he could access
and operate the electric shock device through his work. Therefore, Jaekyun had the means.
Jaekyun is familiar with the zoo’s pathways and schedule patterns, and he was known to observe
coworkers’ movements. His awareness of the zoo’s security and ability to move unnoticed
indicate that he had access to the scene. Therefore, Jaekyun had the opportunity.
To summarize:
Seoyul has motive and opportunity but lacks means.
Jaekyun has motive, means, and opportunity.
Therefore, the most likely murderer is Jaekyun.
Figure 47: 1 Shot CoT Hint Example for Ko-MuSR - Murder Mysteries (Translated)
84

--- Page 85 ---

문제
민재는떠나기전마지막으로가방을살펴보았다. 가방안에있는카메라를손으로확인하자,
괜히한숨이놓이는느낌이었다. 그순간지영은책장에놓인수첩을힐끗바라보며“이것도
꼭챙겨야지. 놓고가면곤란하니까.” 하고말했다. 옆에서일정을체크하던준호는메모를
하듯수첩과카메라의위치를다시한번상기했다. 사실세사람모두카메라는가방에, 수첩은
책장에있음을잘알고있었다. 여행을준비하는마지막점검이긴했지만, 서로의목표가
같았기에불필요한혼란은없었다. 무엇보다민재는소중한카메라를, 지영은깔끔한정리를,
그리고준호는철저한일정관리를마음에두고무사히여행길에오르려하고있었다.
민재는기기를점검하기위해카메라를탁자로옮겼다. 민재는탁자에놓인기기를점검하고
있었다. 준호는방구석에서자신이챙겨야할일정을고민하며떠날준비에만집중하고
있었다. 지영이는민재에게점검관련의견을전하며가까이에서필요한도움을주고있었다.
준호는여전히민재에게신경쓰지않았고, 지영이는민재가기기를다루는과정을함께하고
있었다.
지영은탁자에있던카메라를들어서랍안에넣었다. 민재는친구가무언가를다루는순간에
돕고자주변상황에신경쓰고있었다. 민재와지영은같은공간에서나란히정리작업을하고
있었다. 준호는지영의움직임에집중하며필요한정보를교환하고있었다. 준호와지영은
같은공간에서가까운거리를유지하고있었다.
준호는책장에있던수첩을가방으로옮겼다. 민재는곧출발한다는생각에마음이급해,
주변움직임을살필여유가없었다. 떠나기전필요한예약내역을다시확인하느라시선이
분산되었다. 지영이는급히챙겨야할준비사항을떠올리며한곳에집중해있었고, 일정
확인에몰두하느라주변시야를살피지않았다.
이이야기는여기서끝이다.
주어진이야기를고려할때, 민재는수첩을찾기위해어디를가장먼저확인하겠는가?
다음중하나만고르시오:
1 – 가방
2 – 서랍
3 – 책장
4 - 탁자
힌트
이이야기를바탕으로, 우리는특정인물이어떤물건이어디에있다고생각하고있는지를
파악하려고한다. 이를위해서는이야기흐름을따라가며각인물이물건이어디에있다고
생각하는지상태추적이필요하다. 물건이옮겨질때, 그장면을직접보았거나, 옮겨진
위치를인지할수있는상태였다면그들은물건이옮겨진위치를알고있다고본다. 하지만그
순간을보지못했거나, 너무다른일에집중하고있었다면, 그들은여전히해당물건이이전
위치에있다고믿는다.
예시풀이
이문제는단계적으로생각해보며풀어야합니다. 우리가알고싶은것은민재가수첩을
찾기위해가장먼저어디를확인할것인가? 입니다. 이를위해민재가이야기속에서수첩의
위치를어디에서봤고, 어디에있다고믿고있는지순서대로확인해보겠습니다.
85

--- Page 86 ---

이야기초반에는다음과같은문장이등장합니다: “사실세사람모두카메라는가방에,
수첩은책장에있음을잘알고있었다.” 이를통해, 처음에민재는수첩이책장에있다고
인지하고있음을알수있습니다.
이야기후반에, 준호가책장에있던수첩을가방으로옮깁니다. 하지만, 이어지는서술에
따르면민재는주변움직임을살필여유가없었다고합니다. 따라서민재는준호가수첩을
옮기는장면을보지못했으며, 수첩이옮겨졌다는사실을모른다는점을알수있습니다.
따라서, 민재는여전히수첩이책장에있다고믿고있다고추측할수있습니다.
또한, 이야기속어느부분에서도민재가서랍이나가방혹은탁자등다른장소로수첩이
이동된것을직접보거나눈치채는장면은없습니다. 이모든정황을종합해보면, 민재는
수첩이여전히책장에있다고믿고있을것입니다.
따라서, 민재가수첩을찾기위해가장먼저확인할장소는책장입니다.
Figure 48: 1 Shot CoT Hint Example for Ko-MuSR - Object Placements
Question
Before leaving, Minjae took one last look inside his bag. When he confirmed the presence of
the camera inside, he felt a sense of relief. At that moment, Jiyeong glanced at the notebook on
the bookshelf and said, “We should definitely take this too. It would be troublesome if we left it
behind.” Junho, checking his schedule nearby, made a mental note of the notebook and camera’s
locations once more. In fact, all three of them knew well that the camera was in the bag and the
notebook was on the bookshelf. It was their final check before the trip, but since they shared the
same goal, there was no unnecessary confusion. Above all, Minjae cared about his precious
camera, Jiyeong cared about neat organization, and Junho, focused on precise scheduling, all
prepared to depart smoothly.
Minjae moved the camera from the bag to the table to inspect the device. He examined it carefully,
making sure everything was working. Junho, in the corner of the room, focused entirely on
preparing for the trip and reviewing his itinerary. Jiyeong, standing nearby, assisted Minjae with
suggestions and feedback. Junho continued to concentrate on his own preparations, paying no
attention to Minjae, while Jiyeong remained beside him, involved in the inspection process.
Jiyeong then took the camera from the table and placed it inside the drawer. Minjae, noticing
his friend’s actions, stayed attentive to help if needed. The two worked side by side, tidying
up the space. Junho, meanwhile, observed Jiyeong’s movement closely, exchanging necessary
information. Junho and Jiyeong were in close proximity, sharing the same space.
Afterward, Junho moved the notebook from the bookshelf to the bag. Minjae, feeling rushed to
leave, didn’t have the composure to notice his surroundings. His attention was scattered as he
reviewed his reservation details one last time. Jiyeong, preoccupied with final preparations, was
also too focused to notice anything around her.
The story ends here.
Given this story, where would Minjae most likely check first when looking for the notebook?
86

--- Page 87 ---

Choose one of the following:
1 – Bag
2 – Drawer
3 – Bookshelf
4 – Table
Hint
Based on this story, we want to determine where a particular character believes an object to
be located. To do this, we must track each character’s belief state by following the story and
reasoning about what they have or have not observed. If a character sees an item being moved or
can clearly infer its movement, they are aware of the new location. However, if they do not see the
movement or are too focused on other activities, they continue to believe that the object remains
in its previous location.
Example Solution
This problem should be solved step by step. The goal is to determine where Minjae would first
look for the notebook. To answer this, we need to trace what Minjae saw during the story and
where he believes the notebook to be.
At the beginning, we see the sentence: “All three of them knew well that the camera was in the
bag and the notebook was on the bookshelf.” From this, we know that Minjae initially believes the
notebook is on the bookshelf.
Later in the story, Junho moves the notebook from the bookshelf to the bag. However, it is stated
that Minjae was too preoccupied to notice his surroundings at that time. Therefore, Minjae did not
see Junho move the notebook and is unaware that it has been relocated.
Nowhere in the story does Minjae observe or realize that the notebook has moved elsewhere.
Considering these details, Minjae would still believe that the notebook remains on the bookshelf.
Thus, the location that Minjae would most likely check first is the bookshelf.
Figure 49: 1 Shot CoT Hint Example for Ko-MuSR - Object Placements (Translated)
문제
헬스케어스타트업의새로운여정을시작하며, 당신은서진, 민주, 유환이라는세명의팀원과
함께하게되었습니다. 이들은각기다른배경과경험을가지고있으며, 회사의성공을위
해중요한두가지과제인’환자관리시스템개발’과’의료마케팅전략’에기여할예정입니다.
먼저, 서진은디테일을중시하며소프트웨어개발분야에서5년넘게경력을쌓았습니다.
창의적인문제해결능력을인정받아여러차례수상한경험이있는서진은최신환자
관리시스템기술에대한세미나들도꾸준히참석하고있었습니다. 그러나과거에민주와
협업하면서중요도우선순위문제로충돌을겪었던기억이있습니다.
이에비해, 민주는반복적인업무를더선호하며, 창의성발휘에어려움을겪었습니다. 복잡한
시스템을설계하거나개발한경험은없지만유환과는협력의경험이많은데, 두사람은
87

--- Page 88 ---

과거여러프로젝트에서좋은팀워크를발휘했습니다. 특히, 팀워크샵에서는함께의견을
제안하며빼어난호흡을보여줬습니다.
유환은소프트웨어개발에대한풍부한경험을바탕으로과거헬스케어시스템개발프로젝
트에도참여한바있습니다. 그는다수의성공적인의료캠페인을주도했고, 이전회사에서는
의료마케팅팀의핵심멤버로활약하기도했습니다. 그러나서진과는작업스타일의차이로
인해예전프로젝트에서의견충돌이잦았습니다.
이제, 당신의책상위에는두개의메모가놓여있습니다. 하나는환자관리시스템개발자로
서의역할을, 다른하나는의료마케팅전략가역할을위한것입니다. 각자적합한인재에게
이업무를배정해야하는데, 여기서과연어떤배정이’가장좋은’ 배정일까요?
당신은이들의과거경험과서로간의협력관계를고려하며최적의조합을고민하게됩니다.
답은독자의판단에달려있습니다. 이세명의인재중누가어느역할을맡는것이팀과
회사의성공을위한최상의선택일까요?
이이야기를바탕으로, 두가지업무가모두효율적으로수행되도록사람을어떻게배정하시
겠습니까?
다음중하나를선택하세요:
1 – 개발자: 서진, 마케팅전략가: 민주,유환
2 - 개발자: 민주, 마케팅전략가: 서진,유환
3 - 개발자: 유환, 마케팅전략가: 민주,서진
힌트
당신은세가지중하나의선택지를골라야합니다. 스토리를통해각사람이한가지업무에
얼마나능숙한지를파악할수있습니다. 일반적으로각사람은어떤작업에대해뛰어나거나,
보통이거나, 부족한실력을가지고있습니다. 우리는가능한한각자의강점을최대한발휘할
수있도록사람을적절한업무에배치하려고합니다.
또한, 두사람이함께맡아야하는업무가하나있으며, 이경우두사람의팀워크수준(훌륭함,
보통, 나쁨)도전체업무성과에중요한영향을미칩니다.
단, 두사람이함께일해야하는작업에서한사람이실력이부족하고, 두사람의팀워크
도좋지않다면, 다른한사람이아무리뛰어나도전체결과에는도움이되지않을수있습니다.
각기다른강점, 약점, 그리고두사람간의상호작용을고려하여, 전체과제가가장효율적으
로수행될수있도록팀원들을적절히배치해야합니다.
예시풀이
이제단계별로생각해보며문제를해결해봅시다. 먼저각인물의업무별능력을살펴보고,
이후에서로간의협업관계를고려하여가장효율적인선택지를찾아보겠습니다.
먼저, 서진부터살펴보겠습니다.
서진은소프트웨어개발분야에서5년이상의경력을보유하고있으며, 최신환자관리
시스템관련세미나에도꾸준히참석하고있습니다. 따라서서진의환자관리시스템개발
능력을3점으로평가합니다.의료마케팅분야에서는직접적인경험은없지만, 창의적인문제
해결능력으로수상경력이있다고하였습니다. 따라서서진의의료마케팅능력을2점으로
88

--- Page 89 ---

평가합니다.
다음은민주입니다.
민주는반복적인업무를선호하고, 복잡한시스템을설계하거나개발한경험이없습니다.
따라서민주의환자관리시스템개발능력을1점으로평가합니다. 또한, 민주는반복적인
업무를선호하고창의성발휘에어려움을겪었다고하였습니다. 따라서민주의의료마케팅
능력을1점으로평가합니다.
마지막으로유환에대해고려해보겠습니다.
유환은헬스케어시스템개발경험이있고, 소프트웨어개발경험도풍부합니다. 따라서
유환의환자관리시스템개발능력을2점으로평가합니다. 또한그는의료마케팅캠페인을
성공적으로주도한경험이있고, 해당팀의핵심멤버였습니다. 따라서유환의의료마케팅
능력을3점으로평가합니다.
다음으로인물들간관계와팀워크수준을살펴보겠습니다.
서진과민주는팀워크수준이나쁩니다. 서진은과거민주와협업하면서우선순위문제로
갈등이있었기때문입니다. 따라서서진과민주의팀워크수준을1점으로평가합니다.
서진과유환은팀워크수준이나쁩니다. 유환과서진은작업스타일의차이로인해예전
프로젝트에서의견충돌이잦았기때문입니다. 따라서서진과유환의팀워크수준을1점으로
평가합니다.
민주와유환은팀워크수준이훌륭합니다. 민주와유환은과거여러프로젝트에서좋은
팀워크를보여주었고팀워크샵에서는빼어난호흡을보여주었습니다. 따라서민주와유환의
팀워크수준을3점으로평가합니다.
이제각항목을요약해보면다음과같습니다:
서진은환자관리시스템개발능력이뛰어나다. (3)
서진은의료마케팅능력이나쁘다. (2)
민주는환자관리시스템개발능력이나쁘다. (1)
민주는의료마케팅능력이나쁘다. (1)
유환은환자관리시스템개발능력이보통이다. (2)
유환은의료마케팅능력이뛰어나다. (3)
서진과민주는팀워크수준이나쁘다. (1)
서진과유환은팀워크수준이나쁘다. (1)
민주와유환은팀워크수준이훌륭하다. (3)
이제옵션별점수를계산해봅시다.
옵션1:
환자관리시스템개발자: 서진(3)
의료마케팅전략가: 유환(3) + 민주(1)
민주와유환의협업점수: 3
총합: 3 + 3 + 1 + 3 = 10점
89

--- Page 90 ---

옵션2:
환자관리시스템개발자: 민주(1)
의료마케팅전략가: 유환(3) + 서진(2)
유환-서진협업점수: 1
총합: 1 + 3 + 2 + 1 = 7점
옵션3:
환자관리시스템개발자: 유환(2)
의료마케팅전략가: 민주(1) + 서진(2)
민주-서진협업점수: 1
총합: 2 + 1 + 2 + 1 = 6점
따라서, 가장점수가높은옵션1이최적의배정입니다.
정답: 1
Figure 50: 1 Shot CoT Hint Example for Ko-MuSR - Team Assignments
Question
As you begin a new journey at a healthcare startup, you are joined by three team members: Seojin,
Minju, and Yuhwan. Each of them brings a unique background and experience, and they will
contribute to two crucial projects for the company’s success: developing a patient management
system and designing a medical marketing strategy.
First, Seojin is detail-oriented and has accumulated over five years of experience in software
development. Recognized for her creative problem-solving skills and several awards, she has also
consistently attended seminars on the latest patient management system technologies. However,
she had previous conflicts with Minju over task prioritization during past collaborations.
In contrast, Minju prefers repetitive tasks and struggles with creativity. Although she lacks
experience designing or developing complex systems, she has worked well with Yuhwan on
several projects, demonstrating excellent teamwork. In particular, during team workshops, they
showed great synergy while proposing ideas together.
Yuhwan has extensive experience in software development and has participated in healthcare
system development projects. He has also led several successful medical campaigns and served as
a key member of the medical marketing team at his previous company. However, he often clashed
with Seojin in past projects due to differing work styles.
Now, on your desk are two notes: one for the patient management system developer role and
one for the medical marketing strategist role. You must assign these tasks to the most suitable
individuals. Which assignment would be the best choice for the team’s and the company’s success?
Considering their past experiences and teamwork dynamics, how would you allocate the roles to
ensure both projects are performed efficiently?
90

--- Page 91 ---

Choose one of the following options:
1 – Developer: Seojin, Marketing Strategists: Minju, Yuhwan
2 – Developer: Minju, Marketing Strategists: Seojin, Yuhwan
3 – Developer: Yuhwan, Marketing Strategists: Minju, Seojin
Hint
You must choose one of the three options. The story provides information about each
person’s strengths for each task. Generally, each person is strong, average, or weak in spe-
cific tasks. Our goal is to assign people to roles where they can make the best use of their strengths.
Additionally, one of the tasks requires two people to work together, so the quality of their
teamwork (excellent, average, poor) also significantly affects overall performance.
If two people must collaborate and one lacks skill while their teamwork is poor, the overall
performance will be low, regardless of the other person’s ability.
Considering individual strengths, weaknesses, and team dynamics, assign roles so that the tasks
can be completed as efficiently as possible.
Example Solution
Let’s solve this step by step. First, we assess each person’s abilities for each task, then consider
their teamwork relationships to find the most effective combination.
First, let’s look at Seojin.
Seojin has over five years of experience in software development and regularly attends seminars
on patient management systems. Therefore, we rate Seojin’s ability in patient management
system development as 3 points. Although she lacks direct experience in medical marketing, her
award-winning creative problem-solving skills merit a score of 2 points in medical marketing.
Next is Minju.
Minju prefers repetitive tasks and has no experience in designing or developing complex systems.
Thus, her patient management system development ability is rated 1 point. She also struggles to
show creativity, so her medical marketing ability is also rated 1 point.
Finally, Yuhwan.
Yuhwan has experience in healthcare system development and extensive software development
experience. Thus, we rate his patient management system development ability as 2 points. He
also successfully led medical marketing campaigns and was a key team member, so we rate his
medical marketing ability as 3 points.
Next, let’s review their teamwork levels.
Seojin and Minju have poor teamwork. They had conflicts over priorities in the past. Thus, their
teamwork score is 1 point.
91

--- Page 92 ---

Seojin and Yuhwan also have poor teamwork. They often clashed due to work style differences.
Thus, their teamwork score is 1 point.
Minju and Yuhwan have excellent teamwork. They worked well together on several projects and
demonstrated great chemistry during workshops. Thus, their teamwork score is 3 points.
To summarize:
Seojin excels at patient management system development (3).
Seojin is weak at medical marketing (2).
Minju is weak at both patient management (1) and marketing (1).
Yuhwan is average at patient management (2) and excellent at marketing (3).
Seojin–Minju teamwork: poor (1).
Seojin–Yuhwan teamwork: poor (1).
Minju–Yuhwan teamwork: excellent (3).
Now, let’s calculate the total scores for each option.
Option 1:
Developer: Seojin (3)
Marketing Strategists: Yuhwan (3) + Minju (1)
Teamwork (Minju–Yuhwan): 3
Total: 3 + 3 + 1 + 3 = 10 points
Option 2:
Developer: Minju (1)
Marketing Strategists: Yuhwan (3) + Seojin (2)
Teamwork (Yuhwan–Seojin): 1
Total: 1 + 3 + 2 + 1 = 7 points
Option 3:
Developer: Yuhwan (2)
Marketing Strategists: Minju (1) + Seojin (2)
Teamwork (Minju–Seojin): 1
Total: 2 + 1 + 2 + 1 = 6 points
Therefore, the highest total score is achieved with Option 1, which is the optimal assignment.
Answer: 1
Figure 51: 1 Shot CoT Hint Example for Ko-MuSR - Team Assignments (Translated)
K
Listings
This document has been prepared to help participants become familiar with the types of questions
in this study and to explain how to solve them. You will solve a total of three domains in one
day, each consisting of 40 questions. This document provides one example question and its
corresponding example solution for each domain. Please read the example questions and example
solutions carefully to understand how to solve the problems in each domain. You may start
solving the problems after you have thoroughly reviewed the examples, and you may refer back to
92

--- Page 93 ---

them at any time during the problem-solving session.
The questions you will solve are divided into three domains as follows.
(1) Murder Mysteries:
A story of up to 1,500 characters and two suspects are given. The story includes a detective and
the two suspects, and describes the detective’s investigation of them. You are asked to read the
story and identify the murderer according to the example solution method.
(2) Object Placements:
A story of up to 1,000 characters and four candidate locations for an object are given. The story
describes how the characters perform their roles and move the object, resulting in changes in its
location over time. You are asked to read the story and, following the example solution method,
determine the last location where each character saw the object.
(3) Team Assignments:
A story of up to 1,000 characters and three possible team assignment plans are given. The story
describes three individuals, their work abilities, and the level of teamwork among them. You
are asked to read the story and, following the example solution method, choose the best team
assignment plan among the three options.
Example questions and example solutions for each domain are provided on the following pages.
Figure 52: Instructions for Human Evaluation Participants(Translated)
93

--- Page 94 ---

First Phase
Objective: Solve all given questions and submit your answer for each questions.
Mark all questions with three types of marks defined below. If you think the
data instances require edits or possess issue, please leave it to the Note section.
• Pass: The answer can be derived from the narrative and has no issue to be
used as a benchmark instance.
• Minor Issue: The instance contains small issues (e.g., typos, unclear
wording) but it seems to be usable with minor edits.
• Fail: The instance has critical problems (e.g., logical errors, ambiguous
answers) and cannot be used without significant edits.
Second Phase
Objective: You are given a question where the first reviewer flagged minor
issues or incorrectly marked as pass. Refer to the supposed answer and check
if this answer can be derived from the narrative. Mark all questions with three
types of marks defined below. If you think the data instances require edits or
possess issue, please leave it to the Note section.
• Pass: The answer can be derived from the narrative and has no issue to be
used as a benchmark instance.
• Minor Issue: The instance contains small issues (e.g., typos, unclear
wording) but it seems to be usable with minor edits.
• Fail: The instance has critical problems (e.g., logical errors, ambiguous
answers) and cannot be used without significant edits.
Table 12: Annotation Instructions for Data Reviewers
94

--- Page 95 ---

Q. What procedures will be followed if the participants take part in the study?
You will solve a total of 120 multiple-choice questions across three domains under the supervision of the
assigned researcher. Once you confirm your willingness to participate, the following process will take
place.
First, the researcher will provide you with instructions on how to solve the problems, example questions,
and sample solutions for those examples. You will receive one example question per domain.
Next, you will solve a total of 120 multiple-choice questions across the three domains and record your
answers on the answer sheet for submission.
(1) Murder Mysteries
You will be given a story (within 1,500 characters) and two suspects. The story involves a detective
and two suspects, and describes the detective’s investigation into them. Following the example solution
method, you must determine who the murderer is.
(2) Object Placements
You will be given a story (within 1,000 characters) and four possible choices for the object’s location. The
story describes how the characters interact with and move the object over time. Following the example
solution method, you must identify where each character last saw the object.
(3) Team Allocations
You will be given a story (within 1,000 characters) and three team assignment options. The story presents
three characters, their work abilities, and their teamwork levels. Following the example solution method,
you must select the best team assignment plan among the three options.
The researcher will provide you with a study laptop and research materials. To eliminate the influence of
AI tools (e.g., ChatGPT) on your problem-solving ability, you are not allowed to use AI tools during the
process. The provided laptop will have internet access disabled for security and data protection. Although
internet use is unnecessary for solving the tasks, you may use your personal device for web searches if
desired. At the end of the study, you must return all research materials and the provided laptop.
Q. How long will the study participation last?
Your participation will take place on the date agreed upon with the researcher, from 9:00 AM to 6:00
PM. Although the problem-solving session itself takes about 6 hours, additional time will be required for
explanations of the problem-solving methods and related instructions.
You will be provided with a one-hour break from 12:00 PM to 1:00 PM. If you wish to adjust the break
time, you may freely do so after consulting with the researcher. You may also take additional short breaks
at your discretion. Depending on your solving speed, the total duration may increase or decrease. If
you finish solving the problems early, you may end your participation between 4:00 PM and 6:00 PM
after consulting with the researcher. Even if your participation ends early, the compensation for your
participation will remain unchanged.
Q. Are there any side effects or risks?
Some problems, such as those in the murder mystery domain, may cause discomfort or unpleasant
emotions. In such cases, you may stop solving the problems at any time. Since you will be solving
problems provided as files, there are virtually no other physical or psychological risks associated with
participation. Your problem-solving performance will be evaluated on a 100-point scale, and only the
score (not any identifying information) will be made public.
However, you may experience some discomfort due to the content of the questions, the testing environment,
or the researcher’s behavior. If this occurs, please notify the researcher immediately.
Q. Will compensation be provided for participating in this study?
As a token of appreciation for your participation, you will receive a payment of 100$. However, if you
withdraw from the problem-solving session before completion or request that your results be discarded,
the compensation unfortunately cannot be provided. The payment will be given only to participants who
complete the entire session and provide results for all 120 questions. If you request the deletion of your
problem-solving results after the payment has been made, you will be required to return the compensation.
Table 13: Prescribed instructions from IRB-approved participant information sheet.
95

--- Page 96 ---

Model
Seed
En-MM
En-OP
En-TA
Ko-MM
Ko-OP
Ko-TA
QWEN3 32B
5678
66.0
54.7
72.4
70.0
79.2
80.8
9875
66.8
50.8
74.4
65.2
80.8
78.4
LLaMA 4 Scout
5678
65.2
55.1
58.8
56.0
67.6
64.0
9875
65.6
53.1
62.0
56.0
68.0
64.4
Exaone 4.0 32B
5678
63.2
56.2
60.4
52.8
40.4
64.4
9875
59.2
55.1
57.2
52.8
34.4
62.0
HyperClova X SEED Think 14B
5678
51.6
40.2
44.4
46.0
40.4
57.6
9875
51.6
37.1
43.6
43.2
42.0
59.6
Table 14: All Results from Iterations for Table 3
96

--- Page 97 ---

Model
Seed
En-MM
En-OP
En-TA
Ko-MM
Ko-OP
Ko-TA
QWEN3 32B
5678
66.0
54.7
72.4
70.0
79.2
80.8
9875
66.8
50.8
74.4
65.2
80.8
78.4
+ 1 Shot / Direct / Hint
5678
84.4
75.8
88.8
75.6
86.8
88.0
9875
84.4
73.8
89.6
81.6
87.2
87.6
+ 1 Shot / CoT / Hint
5678
84.0
73.4
88.8
78.8
79.6
87.2
9875
83.2
78.1
90.4
76.8
78.8
88.4
+ 3 Shots / Direct / Hint
5678
83.2
77.7
90.0
79.2
88.0
88.8
9875
81.6
75.8
90.4
76.4
85.6
88.8
+ 3 Shots / CoT / Hint
5678
81.6
75.4
90.0
74.8
81.6
88.8
9875
83.2
73.0
87.6
77.2
82.0
89.2
LLaMA 4 Scout
5678
65.2
55.1
58.8
56.0
67.6
64.0
9875
65.6
53.1
62.0
56.0
68.0
64.4
+ 1 Shot / Direct / Hint
5678
74.0
61.7
84.4
74.4
79.6
79.6
9875
74.0
60.5
87.6
79.2
80.0
82.8
+ 1 Shot / CoT / Hint
5678
78.8
69.5
83.6
75.6
81.2
86.0
9875
75.6
69.9
85.2
74.4
80.4
85.2
+ 3 Shots / Direct / Hint
5678
75.2
68.0
85.2
73.2
80.8
87.6
9875
76.8
68.4
88.0
74.0
81.6
86.8
+ 3 Shots / CoT / Hint
5678
74.8
68.8
83.6
73.6
82.4
86.8
9875
76.4
68.4
84.8
72.0
83.6
89.2
Exaone 4.0 32B
5678
63.2
56.2
60.4
52.8
40.4
64.4
9875
59.2
55.1
57.2
52.8
34.4
62.0
+ 1 Shot / Direct / Hint
5678
78.0
78.1
86.8
70.4
61.6
82.8
9875
75.2
68.8
84.8
68.8
61.6
77.2
+ 1 Shot / CoT / Hint
5678
81.2
73.0
87.2
68.0
72.8
81.6
9875
80.4
75.0
86.0
67.2
69.2
77.6
+ 3 Shots / Direct / Hint
5678
74.0
73.0
83.6
70.4
67.6
84.4
9875
73.2
72.3
83.6
69.6
62.0
84.0
+ 3 Shots / CoT / Hint
5678
73.2
73.8
87.6
70.8
71.6
85.2
9875
77.2
70.3
84.0
71.6
71.6
86.4
HyperClova X SEED Think 14B
5678
51.6
40.2
44.4
46.0
40.4
57.6
9875
51.6
37.1
43.6
43.2
42.0
59.6
+ 1 Shot / Direct / Hint
5678
71.2
43.8
66.8
58.4
44.0
60.8
9875
66.8
42.2
67.2
60.4
40.0
55.6
+ 1 Shot / CoT / Hint
5678
69.2
51.6
75.2
64.8
38.8
82.8
9875
71.2
51.2
75.2
62.8
36.4
86.4
+ 3 Shots / Direct / Hint
5678
66.8
66.4
82.0
64.0
51.6
83.2
9875
67.2
63.3
85.6
63.6
47.6
84.4
+ 3 Shots / CoT / Hint
5678
69.2
68.0
80.4
70.4
48.8
88.0
9875
68.0
64.5
81.6
70.8
51.2
87.6
Table 15: All Results from Iterations for Table 9
97

--- Page 98 ---

Model
Seed
En-MM
En-OP
En-TA
Ko-MM
Ko-OP
Ko-TA
QWEN3 0.6B
5678
59.2
51.6
38.8
56.4
28.4
36.8
9875
59.2
52.3
38.8
50.8
28.8
39.2
+ 1 Shot / CoT / Hint
5678
58.4
47.3
38.8
50.8
32.0
33.6
9875
56.0
46.1
34.4
53.2
22.8
31.2
+ 3 Shots / CoT / Hint
5678
57.2
48.0
32.8
50.0
30.4
32.4
9875
53.6
45.3
33.2
48.0
30.0
34.4
HyperClova X SEED Think 14B
5678
55.2
44.1
43.6
48.0
29.6
46.0
9875
56.0
45.3
56.0
48.0
28.4
43.6
+ 1 Shot / CoT / Hint
5678
65.6
43.4
57.2
58.0
29.6
41.6
9875
68.0
44.9
58.4
58.0
30.0
41.2
+ 3 Shots / CoT / Hint
5678
63.6
47.7
52.8
58.0
30.0
34.4
9875
66.0
41.8
56.8
59.2
33.2
37.2
Exaone 4.0 32B
5678
63.6
52.3
58.0
48.0
33.6
66.0
9875
57.6
52.3
60.0
52.0
34.4
60.4
+ 1 Shot / CoT / Hint
5678
71.2
43.0
58.8
56.0
30.0
52.4
9875
70.4
41.4
57.6
56.0
31.6
56.8
+ 3 Shots / CoT / Hint
5678
66.0
37.9
58.4
62.4
32.0
51.6
9875
66.0
41.4
52.4
63.6
34.0
56.8
Exaone 3.5 2.4B Instruct
5678
52.0
43.4
44.8
51.6
30.4
42.0
9875
50.8
39.8
43.2
50.4
29.6
42.8
+ 1 Shot / CoT / Hint
5678
60.4
51.2
36.4
57.6
39.2
41.2
9875
62.4
44.1
42.8
55.2
41.6
34.4
+ 3 Shots / CoT / Hint
5678
62.4
46.9
36.4
55.2
39.6
40.4
9875
64.4
50.4
38.0
56.8
42.8
45.2
QWEN3 4B
5678
64.0
54.7
66.0
58.4
52.4
72.8
9875
61.6
56.2
66.0
59.6
49.6
78.0
+ 1 Shot / CoT / Hint
5678
76.8
71.1
85.6
68.0
55.2
76.4
9875
75.6
67.6
86.8
71.6
56.8
76.4
+ 3 Shots / CoT / Hint
5678
72.0
69.9
84.4
70.0
54.4
78.8
9875
76.0
71.5
86.4
69.6
56.0
80.4
Table 16: Full Table for Table ??
98

--- Page 99 ---

Model
Seed
En-MM
En-OP
En-TA
Ko-MM
Ko-OP
Ko-TA
QWEN3 32B
5678
66.0
54.7
72.4
70.0
79.2
80.8
9875
66.8
50.8
74.4
65.2
80.8
78.4
+ 1 Shot / Direct / No Hint
5678
72.8
63.3
80.4
69.2
82.8
79.6
9875
74.4
60.9
81.6
69.2
83.2
81.6
+ 3 Shots / Direct / No Hint
5678
76.8
67.2
75.6
71.2
83.6
82.8
9875
75.6
62.1
76.4
72.4
87.2
80.8
+ 1 Shot / CoT / Hint
5678
84.0
73.4
88.8
78.8
79.6
87.2
9875
83.2
78.1
90.4
76.8
78.8
88.4
+ 3 Shots / CoT / Hint
5678
81.6
75.4
90.0
74.8
81.6
88.8
9875
83.2
73.0
87.6
77.2
82.0
89.2
LLaMA 4 Scout
5678
65.2
55.1
58.8
56.0
67.6
64.0
9875
65.6
53.1
62.0
56.0
68.0
64.4
+ 1 Shot / Direct / No Hint
5678
68.8
54.7
70.4
74.0
71.2
70.4
9875
70.4
58.2
69.6
71.6
74.8
71.2
+ 3 Shots / Direct / No Hint
5678
70.8
59.8
75.6
70.4
76.0
82.4
9875
74.4
63.3
80.4
70.4
75.2
82.8
+ 1 Shot / CoT / Hint
5678
78.8
69.5
83.6
75.6
81.2
86.0
9875
75.6
69.9
85.2
74.4
80.4
85.2
+ 3 Shots / CoT / Hint
5678
74.8
68.8
83.6
73.6
82.4
86.8
9875
76.4
68.4
84.8
72.0
83.6
89.2
Exaone 4.0 32B
5678
63.2
56.2
60.4
52.8
40.4
64.4
9875
59.2
55.1
57.2
52.8
34.4
62.0
+ 1 Shot / Direct / No Hint
5678
75.2
57.4
61.6
62.8
44.4
65.2
9875
74.4
58.2
65.2
62.0
53.2
65.6
+ 3 Shots / Direct / No Hint
5678
75.6
63.7
68.4
68.4
63.2
72.4
9875
76.4
61.3
70.4
68.8
57.2
74.8
+ 1 Shot / CoT / Hint
5678
81.2
73.0
87.2
68.0
72.8
81.6
9875
80.4
75.0
86.0
67.2
69.2
77.6
+ 3 Shots / CoT / Hint
5678
73.2
73.8
87.6
70.8
71.6
85.2
9875
77.2
70.3
84.0
71.6
71.6
86.4
HyperClova X SEED Think 14B
5678
51.6
40.2
44.4
46.0
40.4
57.6
9875
51.6
37.1
43.6
43.2
42.0
59.6
+ 1 Shot / Direct / No Hint
5678
65.6
42.6
53.2
48.8
37.6
49.6
9875
62.0
41.4
54.0
51.2
40.4
54.0
+ 3 Shots / Direct / No Hint
5678
68.4
64.5
78.0
66.4
51.2
86.4
9875
67.2
62.9
74.0
64.4
53.6
86.0
+ 1 Shot / CoT / Hint
5678
69.2
51.6
75.2
64.8
38.8
82.8
9875
71.2
51.2
75.2
62.8
36.4
86.4
+ 3 Shots / CoT / Hint
5678
69.2
68.0
80.4
70.4
48.8
88.0
9875
68.0
64.5
81.6
70.8
51.2
87.6
Table 17: All Results from Iterations for Table 7
99

--- Page 100 ---

Model
Seed
En-MM
En-OP
En-TA
Ko-MM
Ko-OP
Ko-TA
QWEN3 32B
5678
66.0
54.7
72.4
70.0
79.2
80.8
9875
66.8
50.8
74.4
65.2
80.8
78.4
+ 1 Shot / Direct / No Hint
5678
72.8
63.3
80.4
69.2
82.8
79.6
9875
74.4
60.9
81.6
69.2
83.2
81.6
+ 1 Shot / Direct / Hint
5678
84.4
75.8
88.8
75.6
86.8
88.0
9875
84.4
73.8
89.6
81.6
87.2
87.6
+ 3 Shots / CoT / No Hint
5678
75.6
67.2
80.0
71.6
74.0
82.8
9875
73.2
71.1
80.4
75.2
76.8
83.2
+ 3 Shots / CoT / Hint
5678
81.6
75.4
90.0
74.8
81.6
88.8
9875
83.2
73.0
87.6
77.2
82.0
89.2
LLaMA 4 Scout
5678
65.2
55.1
58.8
56.0
67.6
64.0
9875
65.6
53.1
62.0
56.0
68.0
64.4
+ 1 Shot / Direct / No Hint
5678
68.8
54.7
70.4
74.0
71.2
70.4
9875
70.4
58.2
69.6
71.6
74.8
71.2
+ 1 Shot / Direct / Hint
5678
74.0
61.7
84.4
74.4
79.6
79.6
9875
74.0
60.5
87.6
79.2
80.0
82.8
+ 3 Shots / CoT / No Hint
5678
71.2
62.5
77.2
70.8
73.6
84.4
9875
72.0
63.3
79.2
72.0
78.0
83.2
+ 3 Shots / CoT / Hint
5678
74.8
68.8
83.6
73.6
82.4
86.8
9875
76.4
68.4
84.8
72.0
83.6
89.2
Exaone 4.0 32B
5678
63.2
56.2
60.4
52.8
40.4
64.4
9875
59.2
55.1
57.2
52.8
34.4
62.0
+ 1 Shot / Direct / No Hint
5678
75.2
57.4
61.6
62.8
44.4
65.2
9875
74.4
58.2
65.2
62.0
53.2
65.6
+ 1 Shot / Direct / Hint
5678
78.0
78.1
86.8
70.4
61.6
82.8
9875
75.2
68.8
84.8
68.8
61.6
77.2
+ 3 Shots / CoT / No Hint
5678
72.0
60.2
70.8
69.2
64.0
82.4
9875
77.2
60.2
69.2
71.6
61.6
72.0
+ 3 Shots / CoT / Hint
5678
73.2
73.8
87.6
70.8
71.6
85.2
9875
77.2
70.3
84.0
71.6
71.6
86.4
HyperClova X SEED Think 14B
5678
51.6
40.2
44.4
46.0
40.4
57.6
9875
51.6
37.1
43.6
43.2
42.0
59.6
+ 1 Shot / Direct / No Hint
5678
65.6
42.6
53.2
48.8
37.6
49.6
9875
62.0
41.4
54.0
51.2
40.4
54.0
+ 1 Shot / Direct / Hint
5678
71.2
43.8
66.8
58.4
44.0
60.8
9875
66.8
42.2
67.2
60.4
40.0
55.6
+ 3 Shots / CoT / No Hint
5678
67.2
65.6
75.2
63.2
47.2
86.4
9875
66.8
61.7
72.8
66.0
46.8
82.8
+ 3 Shots / CoT / Hint
5678
69.2
68.0
80.4
70.4
48.8
88.0
9875
68.0
64.5
81.6
70.8
51.2
87.6
Table 18: All Results from Iterations for Table 8
100

--- Page 101 ---

Model
Seed
En-MM
En-OP
En-TA
Ko-MM
Ko-OP
Ko-TA
QWEN3 32B
5678
81.6
75.4
90.0
74.8
81.6
88.8
9875
83.2
73.0
87.6
77.2
82.0
89.2
LLaMA 4 Scout
5678
74.8
68.8
83.6
73.6
82.4
86.8
9875
76.4
68.4
84.8
72.0
83.6
89.2
Exaone 4.0 32B
5678
73.2
73.8
87.6
70.8
71.6
85.2
9875
77.2
70.3
84.0
71.6
71.6
86.4
HyperClova X SEED Think 14B
5678
69.2
68.0
80.4
70.4
48.8
88.0
9875
68.0
64.5
81.6
70.8
51.2
87.6
Table 19: All Results from Iterations for Table 4
101

--- Page 102 ---

Model
Seed
En-MM
En-OP
En-TA
Ko-MM
Ko-OP
Ko-TA
QWEN3 0.6B
5678
59.2
51.6
38.8
56.4
28.4
36.8
9875
59.2
52.3
38.8
50.8
28.8
39.2
+ 1 Shot / Direct / No Hint
5678
56.0
47.3
32.0
57.6
22.0
32.4
9875
54.8
54.3
30.8
49.6
25.6
35.6
+ 3 Shots / Direct / No Hint
5678
52.8
48.0
36.4
58.0
32.0
30.4
9875
56.0
49.6
36.4
56.0
25.2
34.4
+ 1 Shot / CoT / Hint
5678
58.4
47.3
38.8
50.8
32.0
33.6
9875
56.0
46.1
34.4
53.2
22.8
31.2
+ 3 Shots / CoT / Hint
5678
57.2
48.0
32.8
50.0
30.4
32.4
9875
53.6
45.3
33.2
48.0
30.0
34.4
Exaone 4.0 1.2B
5678
55.2
44.1
43.6
48.0
29.6
46.0
9875
56.0
45.3
56.0
48.0
28.4
43.6
+ 1 Shot / Direct / No Hint
5678
60.4
45.7
47.6
55.2
28.0
42.4
9875
60.4
54.3
48.0
55.6
26.4
42.0
+ 3 Shots / Direct / No Hint
5678
62.4
41.4
46.4
46.8
29.6
40.0
9875
59.6
44.1
45.2
52.0
24.8
40.4
+ 1 Shot / CoT / Hint
5678
65.6
43.4
57.2
58.0
29.6
41.6
9875
68.0
44.9
58.4
58.0
30.0
41.2
+ 3 Shots / CoT / Hint
5678
63.6
47.7
52.8
58.0
30.0
34.4
9875
66.0
41.8
56.8
59.2
33.2
37.2
QWEN3 1.7B
5678
63.6
52.3
58.0
48.0
33.6
66.0
9875
57.6
52.3
60.0
52.0
34.4
60.4
+ 1 Shot / Direct / No Hint
5678
64.8
49.6
53.2
58.0
35.2
56.0
9875
63.2
50.8
55.6
52.4
31.6
56.0
+ 3 Shots / Direct / No Hint
5678
60.4
53.9
54.0
59.6
32.8
47.2
9875
58.8
52.3
52.8
56.4
36.8
54.8
+ 1 Shot / CoT / Hint
5678
71.2
43.0
58.8
56.0
30.0
52.4
9875
70.4
41.4
57.6
56.0
31.6
56.8
+ 3 Shots / CoT / Hint
5678
66.0
37.9
58.4
62.4
32.0
51.6
9875
66.0
41.4
52.4
63.6
34.0
56.8
Exaone 3.5 2.4B Instruct
5678
52.0
43.4
44.8
51.6
30.4
42.0
9875
50.8
39.8
43.2
50.4
29.6
42.8
+ 1 Shot / Direct / No Hint
5678
58.0
44.1
44.0
56.0
40.0
38.4
9875
54.4
46.5
41.2
55.6
40.0
36.8
+ 3 Shots / Direct / No Hint
5678
59.6
44.1
37.2
61.6
41.2
39.6
9875
54.0
47.3
39.6
54.4
39.2
39.2
+ 1 Shot / CoT / Hint
5678
60.4
51.2
36.4
57.6
39.2
41.2
9875
62.4
44.1
42.8
55.2
41.6
34.4
+ 3 Shots / CoT / Hint
5678
62.4
46.9
36.4
55.2
39.6
40.4
9875
64.4
50.4
38.0
56.8
42.8
45.2
QWEN3 4B
5678
64.0
54.7
66.0
58.4
52.4
72.8
9875
61.6
56.2
66.0
59.6
49.6
78.0
+ 1 Shot / Direct / No Hint
5678
64.4
52.3
70.0
65.2
50.8
74.0
9875
69.6
54.3
68.8
61.6
52.8
74.0
+ 3 Shots / Direct / No Hint
5678
68.8
46.9
68.4
66.8
53.2
71.2
9875
67.6
51.2
70.8
66.0
54.0
68.4
+ 1 Shot / CoT / Hint
5678
76.8
71.1
85.6
68.0
55.2
76.4
9875
75.6
67.6
86.8
71.6
56.8
76.4
+ 3 Shots / CoT / Hint
5678
72.0
69.9
84.4
70.0
54.4
78.8
9875
76.0
71.5
86.4
69.6
56.0
80.4
Table 20: All Results from Iterations for Table 6 and Table 10
102

```
