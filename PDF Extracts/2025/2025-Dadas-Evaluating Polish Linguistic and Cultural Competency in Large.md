---
title: "2025-Dadas-Evaluating Polish Linguistic and Cultural Competency in Large - PDF Extract"
source_pdf: "2025-Dadas-Evaluating Polish Linguistic and Cultural Competency in Large.pdf"
pages: 13
extracted_at: "2026-02-13T09:50:31.878807"
---

# PDF Extract: 2025-Dadas-Evaluating Polish Linguistic and Cultural Competency in Large

**Source PDF:** 2025-Dadas-Evaluating Polish Linguistic and Cultural Competency in Large.pdf
**Total Pages:** 13

---

## Content

```
--- Page 1 ---

Evaluating Polish linguistic and cultural
competency in large language models
Sławomir Dadas, Małgorzata Grębowiec, Michał Perełkiewicz, and Rafał
Poświata
National Information Processing Institute, Warsaw, Poland
{sdadas,mgrebowiec,mperelkiewicz,rposwiata}@opi.org.pl
Abstract. Large language models (LLMs) are becoming increasingly
proficient in processing and generating multilingual texts, which allows
them to address real-world problems more effectively. However, language
understanding is a far more complex issue that goes beyond simple text
analysis. It requires familiarity with cultural context, including references
to everyday life, historical events, traditions, folklore, literature, and pop
culture. A lack of such knowledge can lead to misinterpretations and
subtle, hard-to-detect errors. To examine language models’ knowledge of
the Polish cultural context, we introduce the Polish linguistic and cultural
competency benchmark, consisting of 600 manually crafted questions. The
benchmark is divided into six categories: history, geography, culture &
tradition, art & entertainment, grammar, and vocabulary. As part of our
study, we conduct an extensive evaluation involving over 30 open-weight
and commercial LLMs. Our experiments provide a new perspective on
Polish competencies in language models, moving past traditional natural
language processing tasks and general knowledge assessment.
Keywords: Large Language Models · Evaluation · Polish Language
1
Introduction
Recently, we have observed a dynamic development of large language models
(LLMs). This led to profound changes in the approach to natural language
processing. As a result, small models fine-tuned to perform specific tasks are
gradually being replaced by large generative models, trained on massive text
corpora and millions of instructions covering a wide variety of problems. From a
business and end-user perspective, this simplifies the practical use of language
models, since prompt engineering and few-shot learning are techniques that do
not require specialized knowledge, as opposed to earlier approaches that involved
re-training the models for each task. However, evaluating modern language models
poses a significant challenge. Firstly, their ability to solve various types of tasks,
and even generalize to tasks not seen during training, requires a multifaceted
approach to evaluation. Secondly, these models generate responses in plain text,
allowing a high degree of freedom in terms of response style and formatting.
Assessing the correctness of a textual response is more challenging than evaluating
arXiv:2503.00995v1  [cs.CL]  2 Mar 2025

--- Page 2 ---

2
S. Dadas, M. Grębowiec, M. Perełkiewicz, R. Poświata
a structured response such as a numerical value, class label, probability, or answer
from a closed vocabulary.
In recent years, various approaches to evaluating LLMs have been proposed.
At the same time, there is a growing awareness of their drawbacks and limitations
[3, 21, 19]. Therefore, it is crucial to use a combination of several benchmarks
to verify various aspects of understanding and generation of natural language.
One such aspect is multilinguality. Currently, an increasing number of models
declare multilingual capabilities. Initially, these were mainly commercial models
such as GPT-4 [25], Claude [1] or Gemini [26], but the trend has also extended
to open-weights models. This publication focuses on the Polish language, which
is often included among the supported languages. There are families of models
that mention Polish directly (Qwen2 [35], Command-R [12], Aya [2]) and those
that declare broad support for multilinguality and are known to work well for
Polish (Mistral [16, 17], Llama 3.1+ [9]). It is also worth mentioning initiatives
focusing solely on the Polish language such as SpeakLeash1 or PLLuM [18].
 
Jak chronić się przed przeziębieniem i grypą? 
(...) Wycieraj powierzchnie, które często są dotykane, takie jak drzwi, rękojeściami drzwi, telefonami, 
komputerami itp., korzystając z dezynfekcyjnego spraysu lub papierek. (...) Wakcynacja: Regularna 
vakcynering przeciwko grzebień może znacznie zmniejszyć ryzyko zachorowania na gruźlicę. (...) 
Pamiętaj, że even with these precautions, it's still possible to get sick.  
 
Fig. 1. Example showing various types of errors made by a multilingual model that
was undertrained on Polish data. The user prompt is: How do you protect yourself
from cold and flu? (Jak chronić się przed przeziębieniem i grypą?). In the model’s
response, we can observe the following errors: a) morphological (green) - using the
wrong form of a word; b) lexical (orange) - using a word that does not fit the context;
c) word-formation (blue) - attempt to create a new word by imitating a word in
another language, usually English; d) changing the language of the answer completely
(yellow). The example includes snippets of the response generated by the Qwen2.5 7B
model, using the interface provided by the model’s authors. For larger Qwen2.5 models
the frequency of such errors decreases.
In practice, the level of Polish proficiency among multilingual models leaves
much to be desired. Models with a small number of parameters can struggle
to generate coherent and grammatically correct text. As an example, Figure 1
shows the errors made by the Qwen2.5 model [35] when prompted to answer a
simple question in Polish. For larger models, such problems are less frequent.
However, the underrepresentation of Polish texts in the pre-training corpus can
result in the model lacking Polish cultural context, which is essential for language
understanding. The language includes references to historical events, folklore,
1 https://speakleash.org/

--- Page 3 ---

Evaluating Polish linguistic and cultural competency in LLMs
3
literature, or pop culture can carry specific meanings in a particular culture but
may not be understood or may have different associations in another culture [31].
As a result, models that on the surface may perform well in understanding and
generating language will have difficulties correctly interpreting texts containing
such references.
1.1
Contributions
The goal of this publication is to examine both the linguistic and cultural
competence of LLMs in Polish. To this end, we introduce a benchmark consisting
of 600 manually prepared questions. The questions are divided into six categories
representing different aspects of knowledge about Poland and the Polish language:
history, geography, culture & tradition, art & entertainment, grammar, and
vocabulary. Apart from thematic diversity, we also ensured diversity in the
form of questions. In addition to questions that require a direct answer, the
benchmark includes questions that involve combining facts, aggregating knowledge
about different concepts, and sorting or filtering concepts according to specified
characteristics. The evaluation of answers is deterministic and involves a rule-
based system, inspired by benchmarks such as IFEval [37] or BBH [32]. For
each question, we define a set of rules that must be met for the question to be
considered as passed. For closed-ended questions, these rules are explicit and
easy to define. For open-ended questions, the presence or order of certain words,
phrases, or regular expressions is checked. As part of this study, we evaluated
over 30 open-weights and commercial LLMs. We also launched a demo website2
featuring an up-to-date leaderboard, examples of questions from each category,
and a description of our methodology.
1.2
Related work
Most methods for evaluating large language models can be divided into four
categories:
• Closed-ended questions and structured answers - Benchmarks of this
type require the formulation of tasks for the LLM in such a way that the answer
follows a format imposed by the authors so that it can be verified deterministically.
The most common type of such tasks are single- or multiple-choice questions,
in which the model is presented with answers from which it must select the
correct ones. Among these types of tests, the popular ones include GPQA [27]
and different variants of MMLU [14, 34]. In addition, the group also includes
tests that expect a structured answer, for example, datasets of math questions
such as MATH [15] or GSM8K [7]. The category also incorporates many classic
NLP tasks such as classification, regression, or information extraction.
• LLM-as-judge - In this approach, a different language model is used to assess
model’s performance, usually a larger and more competent or trained specifically
2 https://huggingface.co/spaces/sdadas/plcc

--- Page 4 ---

4
S. Dadas, M. Grębowiec, M. Perełkiewicz, R. Poświata
for the purpose of evaluation. Popular examples of such benchmarks are MT-
BENCH [36] and AlpacaEval [10]. Their advantage is the ability to evaluate
models in tasks requiring free-form and long answers. On the other hand, the
main disadvantage is the dependence on an external judge, which may be biased
from the data on which it was trained. Consequently, results on such benchmarks
may vary depending on which model is used as a judge. In addition, the cost of
LLM-as-judge evaluation is higher than that of deterministic methods.
• Human evaluation - An evaluation method that uses human annotators
to rate the responses of LLM directly. This is the most costly of the described
methods, as it requires manual labor. However, it allows for examining unique
aspects of the models’ performance, that is, the alignment of responses with
human preferences, which is not possible with automated benchmarks. A notable
example of such a benchmark is Chatbot Arena [5], a crowdsourced platform in
which users rank pairs of answers from randomly selected models.
• Rule-based and programmatic evaluation - This category includes meth-
ods that verify the correctness of the model’s responses based on programmed
rules. This approach can only be applied to specific types of problems. In addition,
each type of task requires a set of individually crafted rules or hard-coded logic
responsible for evaluation. For example, the ability of models to generate code
can be verified by using an external compiler or interpreter, enabling to run the
code and compare the output with the expected result. This type of approach is
used by benchmarks such as HumanEval [4] or BigCodeBench [38]. Even more
sophisticated evaluation frameworks are used in LLM-based agent systems. For
example, AgentBench [20] allows models to interact with external software such
as an operating system or database and then examines the agent’s ability to
perform specific actions using that software. Text generation tasks typically use
simpler rules that check the content of the answer itself or additional conditions
that have been imposed on the model in the prompt. Such rules are used by the
IFEval [37], BBH [32] or MuSR [30] benchmarks, among others.
For the Polish language, there already exist benchmarks created to evaluate
LLMs. Several of them were developed as part of the work on the Bielik model
[24]. These include adaptations of existing English benchmarks to Polish, such
as MT-BENCH, EQ-BENCH, and Chatbot Arena3. In addition to these, there
are the Open PL LLM Leaderboard and the Polish Medical Leaderboard, which
do not introduce new datasets, instead aggregating pre-existing ones. The first
aggregates mostly classification tasks from older NLP benchmarks [28, 8] and
a small number of simple generative Q&A tasks [29, 33]. The second contains
closed-ended questions from the official medical and specialty exams [13].
To the best of our knowledge, no dataset yet focuses on evaluating Polish
linguistic and cultural competence in LLMs. Recently, such benchmarks for other
languages have begun to appear, including multilingual ones covering groups
of nations and cultures [23, 6, 11, 22]. This suggests that this is an important
issue that, with the popularization of LLMs, is starting to attract the interest of
researchers.
3 https://huggingface.co/speakleash

--- Page 5 ---

Evaluating Polish linguistic and cultural competency in LLMs
5
2
The benchmark
We present the Polish linguistic and cultural competency benchmark, comprising
hand-crafted questions designed to evaluate LLM’s factual knowledge of Polish
culture, tradition, and language. The level of difficulty of the questions varies,
from those that would be answered by the majority of Poles to detailed questions
focusing on region-specific culture or ethnic minorities. The questions have been
phrased in such a way that it is deterministically possible to verify their correctness.
Approximately half of them are various forms of closed-ended questions such as
single-choice, multiple-choice, matching two sets of concepts, or filtering concepts
from a list. The rest of the questions usually require answers consisting of a
single sentence containing a specific fact or a set of facts. Open-ended questions
allow some freedom for the model to generate an answer, but the response
should refer to specific entities such as people, dates, numbers, places, certain
concepts or phrases. In addition, each question is typically supplemented with
instructions for the model, imposing a specific form of answer - short, precise,
without additional comments or elaborate explanations. The dataset has been
divided into six categories, with 100 questions in each. These categories include:
• Culture & tradition - The category contains questions about beliefs and
religion, which are derived from both Christian and folk traditions, as well as Slavic
mythology. It also contains questions about pop culture, including characters
and events that have had a significant impact on Polish society. Finally, we also
included questions about everyday life, covering Polish customs, cuisine, and
clothing, among other topics.
• Art & entertainment - This category focuses on fields of art such as literature,
painting, sculpture, theater, music, dance, or film. The questions cover works and
figures related to Polish art. In addition, this category also features questions
related to entertainment, including sports, popular music, television, radio, and
people associated with show business.
• Geography - The category covers Polish geography and is divided into four
subcategories. Two of them deal with structures and phenomena of natural (e.g.,
mountains, rivers, climate) and man-made origin (e.g., cities, tourist attractions,
industrial plants, mines). The third subcategory deals with socio-political geogra-
phy, which includes questions on population, social problems, national borders,
and administrative units. The last group is biogeography, which covers the fauna
and flora of Poland.
• History - The category covers Polish history from the time of Mieszko I to the
present day. It is divided into subcategories corresponding to historical periods.
It contains questions about important historical events and figures of significance
to Polish politics, science, and humanities.
• Grammar - The category deals with the rules and principles that govern
the structure of sentences in the Polish language, as well as the rules of spelling
(orthography). The questions address both theoretical foundations and practical
applications of grammar. In addition to orthography, the questions cover such
topics as morphology, parts of a sentence, parts of speech, phonetics, word
formation, or rhetorical figures.

--- Page 6 ---

6
S. Dadas, M. Grębowiec, M. Perełkiewicz, R. Poświata
• Vocabulary - The category verifies LLMs’ ability to understand the meaning
of words, idioms, sayings and proverbs. The questions mainly focus on less
frequently used words and phrases. In addition, slang expressions, regionalisms,
dialects, colloquial language, and youth language were also included. Apart from
modern Polish, several questions also deal with archaisms and old language.
Figure 2 shows a visualization of categories and subcategories in our dataset.
religion & tradition (38)
popculture (27)
cuisine (18)
other (8)
organization (5)
fashion (4)
literature (23)
media (20)
film (16)
music (14)
sport (12)
visual arts (10)
performing arts (5)
natural (37)
socio-political (27)
man-made (23)
biogeography (13)
middle ages (31)
modern history (30)
world war 2 (19)
age of reason (18)
other (2)
orthography (33)
morphology (18)
language basics (13)
word formation (11)
part of speech (8)
phonetics (7)
rhetorical figure (5)
part of sentence (5)
word meaning (52)
idiom/phraseme (12)
dialect (8)
colloquial speech/slang (7)
old language (6)
synonym (5)
proverb (5)
other (5)
culture & tradition
art & entertainment
geography
history
grammar
vocabulary
Fig. 2. Distribution of questions by category and subcategory in our benchmark.
2.1
Grading
Each question in the benchmark defines one or more conditions that must be
met for an answer to be accepted. The scores are binary, a model can receive
one or zero points for an answer. Partial points are not possible. This means
that an answer is considered correct if and only if all the conditions defined in
the question are satisfied. If at least one condition is not met, the model gets

--- Page 7 ---

Evaluating Polish linguistic and cultural competency in LLMs
7
zero points for that question. The final score in the benchmark is calculated as a
percentage of correct answers.
The process of verifying a single question starts with sending it to the model
and obtaining the answer. We do not use the system prompt in the evaluation,
and the question is encoded using a chat template specific to each model as a
single message with the user role. In addition, to ensure deterministic responses,
the generation temperature parameter is set to 0. In the second step, we normalize
the response. Normalization involves removing all characters except letters and
numbers, making all letters lowercase, and then lemmatizing the text, that
is, reducing all words to their base forms. Such normalization is necessary for
languages with rich morphology like Polish, because only then we are able to
match different forms of the same word between the model’s response and the
question’s conditions. After normalization, we check each of the conditions defined
in the question. The model scores a point only if all conditions have been verified
successfully. Our benchmark supports the following condition types:
• Include - Checks whether the words or phrases defined in the condition
occurred in the model’s response. In the simplest case, we can provide a list of
comma-delimited expressions, and the condition will be satisfied only if all these
expressions are found in the text. In practice, however, there may be more than
one way to formulate the correct answer, so it is allowed to define alternative
expressions for each item. In such a case, only one of the provided expressions
needs to be in the answer. In other words, the include condition can verify any
logical formula in conjunctive normal form (CNF), in which individual clauses
check the occurrence of a word or phrase in the model’s response. Moreover, the
condition can be parameterized. Instead of the default behavior of matching all
defined expressions, we can specify the minimum (include_min) and maximum
(include_max) number of expressions that should be included in the response. In
special cases, we can also disable lemmatization (lemmatize) if we want to verify
the occurrence of a specific, and not just any, form of a word.
• Exclude - This is the inverse of the previous condition. It checks that none
of the given words or phrases occur in the answer. The condition is verified in
the similar way to include. We can also use the lemmatize parameter to disable
lemmatization when matching words.
• Order - Checks whether the words or phrases defined in the condition occur
in the response in the expected order. Verification of the condition is almost
identical to include. The difference is that the positions of the first occurrence
of the expression, or any of the alternative expressions, are saved. The condition
is considered satisfied if and only if the positions are in ascending order. The con-
dition can be used to verify questions involving sorting or matching information.
The lemmatize parameter can also be applied.
• Regex - This is the most complex condition, which checks whether a defined
regular expression occurs in the answer. If no additional parameters are specified,
the condition is considered to be satisfied if at least one string matches the
regular expression in the text. However, it is possible to control the acceptability
criteria through parameters. For example, we can define the minimum (regex_-

--- Page 8 ---

8
S. Dadas, M. Grębowiec, M. Perełkiewicz, R. Poświata
min) and maximum (regex_max) number of occurrences allowed. Furthermore,
it is possible to force all occurrences to have the same number of characters
(regex_match_length). Finally, we can introduce an additional dictionary criterion
(regex_match_word). If the parameter is set to true, each matched string must
be a valid word in Polish, which is verified using an external dictionary. Unlike
the other conditions, regex is always verified on the unnormalized version of the
response, so the lemmatize parameter is not applicable.
3
Evaluation
In this chapter, we present the results of LLMs evaluation on our Polish linguistic
and cultural competency benchmark. In our experiments, we tested more than
30 commercial and open-weight models. A summary of the results is shown in
Table 1. We report the percentage of correct answers by category and for all
questions combined. The table is divided into sections grouping together models
from the same provider. The order of the sections corresponds to the score of
the best model in the group. For better readability, we have omitted multiple
versions of the same model. In the case of models that are available in several
versions such as the GPT-4o or the Claude Sonnet, the reported results refer to
the latest available version as of the end of 2024. The best score in each column
is bolded and underlined. It is worth noting the low cost of the evaluation, which
is less than $1 for the GPT-4o model according to the current pricing, allowing
for a cost-effective comparison of multiple models. Based on the results, we can
draw the following conclusions:
Open vs. Commercial LLMs - English-centric benchmarks suggest that the
gap between the capabilities of open and commercial models is closing. In fact,
from observing many popular LLM leaderboards, one can conclude that the best
open models such as Llama 3.1 perform nearly as well as GPT-4o or Gemini-1.5-
Pro. In contrast, our evaluation shows that for multilingual abilities, particularly
understanding cultural and linguistic context, open models are still significantly
behind those offered as a service. In our experiments, Gemini-Exp-1206 (83%)
proved to be the best model, followed closely by Claude Sonnet 3.5 and GPT-4o.
These were the only three models that passed the 80% mark. By comparison, the
best-performing open-weight model scored approximately 12 points lower.
The effectiveness of training on Polish data - Bielik-2.3 is the only fully
Polish model in the comparison, i.e. pre-trained on a Polish corpus and fine-
tuned on Polish instructions. Despite its small size of just 11B parameters, it
reached second place among open models, ranking only behind DeepSeek-V3. This
example shows how much can be gained from building language-specific models.
Bielik is based on Mistral-7b, which was upscaled and then continuously trained
on Polish data. If we compare both models, we can see that Bielik improved by
more than 40 points over Mistral.
Comparison with other Polish benchmarks - In this publication, we explore
aspects of LLMs that have so far been overlooked in Polish research. Unfortunately,
current benchmarks for Polish mainly focus on general knowledge and classic

--- Page 9 ---

Evaluating Polish linguistic and cultural competency in LLMs
9
Table 1. Results of commercial and open-weight models on our benchmark. The table
presents the partial scores for the six categories and the total score for all questions.
For models that come in several versions, we used the latest available version for the
evaluation as of the end of 2024. The best score in each column is shown in bold.
Provider Model
Size
Art Cul. Geo. Gra. His. Voc. Total
Alibaba Qwen-2.5-72b
72B
25
30
45
45
54
36
39.17
Alibaba Qwen-2.5-7b
7B
5
11
17
29
23
21
17.67
Cohere Command-R+
104B
44
49
61
43
61
43
50.17
Cohere Command-R7B
8B
14
18
33
23
27
22
22.83
Mistral Mistral-Large-2411 123B
39
52
61
54
64
42
52.00
Mistral Mixtral-8x22b
141B
45
41
59
50
69
35
49.83
Mistral Mistral-Nemo
12B
20
13
26
31
28
20
23.00
Mistral Mistral-7b-v0.3
7B
22
9
27
27
30
16
21.83
Mistral Ministral-8b
8B
14
12
19
24
33
22
20.67
Meta Llama-3.1-405b
405B
56
57
74
57
73
43
60.00
Meta Llama-3.3-70b
70B
43
40
59
49
65
37
48.83
Meta Llama-3.1-8b
8B
19
13
31
29
25
19
22.67
SpeakLeash Bielik-2.3
11B
58
61
68
49
76
61
62.17
SpeakLeash Bielik-0.1
7B
43
52
61
29
58
37
46.67
xAI Grok-2-1212
-
57
67
77
64
74
57
66.00
DeepSeek DeepSeek-V3
685B
61
73
79
62
77
63
69.17
OpenAI GPT-4o
-
82
89
86
67
84
80
81.33
OpenAI GPT-4-turbo
-
61
74
79
56
76
56
67.00
OpenAI GPT-4
-
49
63
67
58
72
48
59.50
OpenAI GPT-4o-mini
-
42
57
69
55
67
51
56.83
OpenAI GPT-3.5-turbo
-
39
38
55
41
51
36
43.33
Anthropic Claude-3.5-Sonnet
-
77
87
85
79
91
77
82.67
Anthropic Claude-3-Opus
-
73
76
80
66
86
62
73.83
Anthropic Claude-3.5-Haiku
-
43
62
72
57
61
52
57.83
Google Gemini-Exp-1206
-
83
90
86
69
88
82
83.00
Google Gemini-2.0-Flash
-
68
78
79
65
83
72
74.17
Google Gemma-2-27b
27B
32
41
47
46
53
37
42.67
Google Gemma-2-9b
9B
19
23
30
38
35
30
29.17
NLP problems such as classification, often including tasks analogous to, or direct
translations of English datasets. This means that they do little to test the models’
actual ability to use and understand the language. Consequently, the results
obtained by us differ significantly from previous evaluations. For example, models
from the Qwen-2.5 family are usually highly rated on other Polish benchmarks
mentioned in the related work section, meanwhile, in our experiments, they
performed below expectations.
Results in relation to model size - We can observe significant differences in
performance between small and large language models. There is a considerable
drop in quality for smaller models, Bielik discussed earlier being the only exception.
This can be explained by the fact that we are testing the models on a knowledge-
based task. A higher number of parameters means a higher information density,

--- Page 10 ---

10
S. Dadas, M. Grębowiec, M. Perełkiewicz, R. Poświata
which can be encoded in the model’s weights, and therefore better performance
for such tasks. In addition, the evaluation is mostly carried out on multilingual
models, which are required to know facts about a variety of languages and cultures.
It is understandable that a loss of information will be observed when we try to
compress this knowledge into a small-sized model.
Llama-3 70B
Command-R+ Mistral-Large
Bielik
GPT-4o
Sonnet
40
50
60
70
80
90
Total score
43.00
3.0
47.83
3.1
48.83
3.3
49.33
04-2024
50.17
08-2024
54.17
2407
52.00
2411
61.00
2.1
63.00
2.2
62.17
2.3
82.33
2024
05-13
81.33
2024
08-06
81.33
2024
11-20
56.50
3.0
80.67
3.5
06-2024
82.67
3.5
10-2024
Fig. 3. Comparison of benchmark scores for different versions of the same model.
Comparison with older models - We performed an additional experiment
in which we measured how the performance on our benchmark changed for
different versions of several models. The results are shown in Figure 3. All models
included in the experiment were released in 2024. In most cases, we did not
see an improvement. For the Mistral-Large, Bielik, and GPT-4o models, the
latest model even achieves a slightly worse score than earlier versions. The most
significant progress can be seen for the Claude Sonnet, especially between the
3.0 and 3.5 versions, but Llama 3 also shows improvement throughout the year.
4
Conclusions
In this publication, we introduced the Polish linguistic and cultural competency
benchmark, aimed at assessing the ability of LLMs to understand the Polish
cultural context. To the best of our knowledge, this is the first evaluation of
linguistic and cultural aspects in LLMs for the Polish language. The results of our
experiments showed that commercial models still maintain a significant advantage
over open-weight models. However, we observe consistent development in both
groups, suggesting that multilingual capabilities may significantly improve in
the coming months. Furthermore, we demonstrated that training models focused
solely on Polish is meaningful, as even models with a small number of parameters
such as Bielik, can match much larger multilingual models in understanding
cultural aspects. Our benchmark proved to be challenging for the modern LLMs,
with the best of them answering about 80% of the questions correctly. This
indicates that there is still considerable room for improvement, and our dataset
can continue to be used in the future to track the progress of language models in
understanding Polish.

--- Page 11 ---

References
[1] Anthropic: The Claude 3 model family: Opus, Sonnet, Haiku (2024), https:
//api.semanticscholar.org/CorpusID:268232499
[2] Aryabumi, V., Dang, J., Talupuru, D., Dash, S., Cairuz, D., Lin, H.,
Venkitesh, B., Smith, M., et al.: Aya 23: Open weight releases to further
multilingual progress. arXiv preprint arXiv:2405.15032 (2024)
[3] Chang, Y., Wang, X., Wang, J., Wu, Y., Yang, L., Zhu, K., Chen, H., Yi, X.,
Wang, C., Wang, Y., Ye, W., Zhang, Y., Chang, Y., Yu, P.S., Yang, Q., Xie,
X.: A survey on evaluation of large language models. ACM Trans. Intell.
Syst. Technol. 15(3) (Mar 2024), https://doi.org/10.1145/3641289
[4] Chen, M., Tworek, J., Jun, H., Yuan, Q., Pinto, H.P.D.O., Kaplan, J.,
Edwards, H., Burda, Y., Joseph, N., Brockman, G., et al.: Evaluating large
language models trained on code. arXiv preprint arXiv:2107.03374 (2021)
[5] Chiang, W.L., Zheng, L., Sheng, Y., Angelopoulos, A.N., Li, T., Li, D.,
Zhang, H., Zhu, B., Jordan, M., Gonzalez, J.E., et al.: Chatbot arena: An
open platform for evaluating llms by human preference. arXiv preprint
arXiv:2403.04132 (2024)
[6] Chiu, Y.Y., Jiang, L., Lin, B.Y., Park, C.Y., Li, S.S., Ravi, S., Bhatia, M.,
Antoniak, M., Tsvetkov, Y., Shwartz, V., Choi, Y.: CulturalBench: a robust,
diverse and challenging benchmark on measuring the (lack of) cultural
knowledge of llms (2024)
[7] Cobbe, K., Kosaraju, V., Bavarian, M., Chen, M., Jun, H., Kaiser, L., Plap-
pert, M., Tworek, J., Hilton, J., Nakano, R., Hesse, C., Schulman, J.: Training
verifiers to solve math word problems. arXiv preprint arXiv:2110.14168
(2021)
[8] Dadas, S., Perełkiewicz, M., Poświata, R.: Evaluation of sentence represen-
tations in polish. In: Proceedings of the Twelfth Language Resources and
Evaluation Conference. pp. 1674–1680 (2020)
[9] Dubey, A., Jauhri, A., Pandey, A., Kadian, A., Al-Dahle, A., Letman, A.,
Mathur, A., Schelten, A., Yang, A., Fan, A., et al.: The llama 3 herd of
models. arXiv preprint arXiv:2407.21783 (2024)
[10] Dubois, Y., Liang, P., Hashimoto, T.: Length-controlled alpacaeval: A sim-
ple debiasing of automatic evaluators. In: First Conference on Language
Modeling (2024), https://openreview.net/forum?id=CybBmzWBX0
[11] Etxaniz, J., Azkune, G., Soroa, A., de Lacalle, O.L., Artetxe, M.: Bertaqa:
How much do language models know about local culture? (2024)
[12] Gomez, A.: Introducing Command R+: A Scalable LLM Built for Business
— cohere.com. https://cohere.com/blog/command-r-plus-microsoft-azure
(2024), [Accessed 26-09-2024]
[13] Łukasz Grzybowski, Pokrywka, J., Ciesiółka, M., Kaczmarek, J.I., Kubis, M.:
Polish medical exams: A new dataset for cross-lingual medical knowledge
transfer assessment (2024), https://arxiv.org/abs/2412.00559

--- Page 12 ---

12
S. Dadas, M. Grębowiec, M. Perełkiewicz, R. Poświata
[14] Hendrycks, D., Burns, C., Basart, S., Zou, A., Mazeika, M., Song, D., Stein-
hardt, J.: Measuring massive multitask language understanding. Proceedings
of the International Conference on Learning Representations (ICLR) (2021)
[15] Hendrycks, D., Burns, C., Kadavath, S., Arora, A., Basart, S., Tang, E.,
Song, D., Steinhardt, J.: Measuring mathematical problem solving with the
math dataset. NeurIPS (2021)
[16] Jiang, A.Q., Sablayrolles, A., Mensch, A., Bamford, C., Chaplot, D.S., Casas,
D.d.l., Bressand, F., Lengyel, G., Lample, G., Saulnier, L., et al.: Mistral 7b.
arXiv preprint arXiv:2310.06825 (2023)
[17] Jiang, A.Q., Sablayrolles, A., Roux, A., Mensch, A., Savary, B., Bamford,
C., Chaplot, D.S., Casas, D.d.l., Hanna, E.B., Bressand, F., et al.: Mixtral
of experts. arXiv preprint arXiv:2401.04088 (2024)
[18] Kazienko, P., Piasecki, M., Okulska, I., Janz, A., Kocoń, J., Ogrodniczuk,
M., Karlińska, A., Tomaszewska, A., Oleksy, M., Wieczorek, J., Roszko, R.,
Dadas, S., Kozłowski, M., Wiśnios, E., Pęzik, P., Rybak, P.: PLLuM: Towards
polish large language model. In: PP-RAI 2024 - 5th Polish Conference on
Artificial Intelligence (2024)
[19] Laskar, M.T.R., Alqahtani, S., Bari, M.S., Rahman, M., Khan, M.A.M.,
Khan, H., Jahan, I., Bhuiyan, A., Tan, C.W., Parvez, M.R., Hoque, E.,
Joty, S., Huang, J.: A systematic survey and critical review on evaluating
large language models: Challenges, limitations, and recommendations. arXiv
preprint arXiv:2407.04069 (2024), https://arxiv.org/abs/2407.04069
[20] Liu, X., Yu, H., Zhang, H., Xu, Y., Lei, X., Lai, H., Gu, Y., Ding, H., Men, K.,
Yang, K., Zhang, S., Deng, X., Zeng, A., Du, Z., Zhang, C., Shen, S., Zhang,
T., Su, Y., Sun, H., Huang, M., Dong, Y., Tang, J.: Agentbench: Evaluating
LLMs as agents. In: The Twelfth International Conference on Learning
Representations (2024), https://openreview.net/forum?id=zAdUB0aCTQ
[21] McIntosh, T.R., Susnjak, T., Liu, T., Watters, P., Halgamuge, M.N.: Inade-
quacies of large language model benchmarks in the era of generative artificial
intelligence. arXiv preprint arXiv:2402.09880 (2024)
[22] Mousi, B., Durrani, N., Ahmad, F., Hasan, M.A., Hasanain, M., Kabbani,
T., Dalvi, F., Chowdhury, S.A., Alam, F.: Aradice: Benchmarks for dialectal
and cultural capabilities in llms (2024), https://arxiv.org/abs/2409.11404
[23] Myung, J., Lee, N., Zhou, Y., Jin, J., Putri, R.A., Antypas, D., Borkakoty,
H., Kim, E., Perez-Almendros, C., Ayele, A.A., Basulto, V.G., Ibanez-
Garcia, Y., Lee, H., Muhammad, S.H., Park, K., Rzayev, A.S., White, N.,
Yimam, S.M., Pilehvar, M.T., Ousidhoum, N., Camacho-Collados, J., Oh, A.:
BLEnd: A benchmark for LLMs on everyday knowledge in diverse cultures
and languages. In: The Thirty-eight Conference on Neural Information
Processing Systems Datasets and Benchmarks Track (2024)
[24] Ociepa, K., Łukasz Flis, Wróbel, K., Gwoździej, A., Kinas, R.: Bielik 7b v0.1:
A polish language model – development, insights, and evaluation (2024)
[25] OpenAI: Gpt-4 technical report (2024), https://arxiv.org/abs/2303.08774
[26] Reid, M., Savinov, N., Teplyashin, D., Lepikhin, D., Lillicrap, T., Alayrac,
J.b., Soricut, R., Lazaridou, A., Firat, O., Schrittwieser, J., et al.: Gemini

--- Page 13 ---

Evaluating Polish linguistic and cultural competency in LLMs
13
1.5: Unlocking multimodal understanding across millions of tokens of context.
arXiv preprint arXiv:2403.05530 (2024)
[27] Rein, D., Hou, B.L., Stickland, A.C., Petty, J., Pang, R.Y., Dirani, J., Michael,
J., Bowman, S.R.: GPQA: A graduate-level google-proof q&a benchmark.
In: First Conference on Language Modeling (2024)
[28] Rybak, P., Mroczkowski, R., Tracz, J., Gawlik, I.: Klej: Comprehensive
benchmark for polish language understanding. In: Proceedings of the 58th
Annual Meeting of the Association for Computational Linguistics. pp. 1191–
1201 (2020)
[29] Rybak, P., Przybyła, P., Ogrodniczuk, M.: Polqa: Polish question answering
dataset. In: Proceedings of the 2024 Joint International Conference on
Computational Linguistics, Language Resources and Evaluation (LREC-
COLING 2024). pp. 12846–12855 (2024)
[30] Sprague, Z.R., Ye, X., Bostrom, K., Chaudhuri, S., Durrett, G.: MuSR:
Testing the limits of chain-of-thought with multistep soft reasoning. In: The
Twelfth International Conference on Learning Representations (2024)
[31] Stań,
I.:
Why
is
the
linguistic
context
important
while
work-
ing
on
textual
data?
(Nov
2023),
https://medium.com/@izab.sta/
why-is-the-linguistic-context-important-ba9069cf34de
[32] Suzgun, M., Scales, N., Schärli, N., Gehrmann, S., Tay, Y., Chung, H.W.,
Chowdhery, A., Le, Q.V., Chi, E.H., Zhou, D., , Wei, J.: Challenging big-
bench tasks and whether chain-of-thought can solve them. arXiv preprint
arXiv:2210.09261 (2022)
[33] Tuora, R., Zwierzchowska, A., Zawadzka-Paluektau, N., Klamra, C.,
Kobyliński, L.: Poquad - the polish question answering dataset - description
and analysis. In: Proceedings of the 12th Knowledge Capture Conference
2023. p. 105–113. K-CAP ’23, Association for Computing Machinery, New
York, NY, USA (2023), https://doi.org/10.1145/3587259.3627548
[34] Wang, Y., Ma, X., Zhang, G., Ni, Y., Chandra, A., Guo, S., Ren, W., Arulraj,
A., He, X., Jiang, Z., et al.: Mmlu-pro: A more robust and challenging multi-
task language understanding benchmark. arXiv preprint arXiv:2406.01574
(2024)
[35] Yang, A., Yang, B., Hui, B., Zheng, B., Yu, B., Zhou, C., Li, C., et al.:
Qwen2 technical report. arXiv preprint arXiv:2407.10671 (2024)
[36] Zheng, L., Chiang, W.L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., Lin,
Z., Li, Z., Li, D., Xing, E.P., Zhang, H., Gonzalez, J.E., Stoica, I.: Judging
llm-as-a-judge with mt-bench and chatbot arena. In: Proceedings of the
37th International Conference on Neural Information Processing Systems.
NIPS ’23, Curran Associates Inc., Red Hook, NY, USA (2024)
[37] Zhou, J., Lu, T., Mishra, S., Brahma, S., Basu, S., Luan, Y., Zhou, D.,
Hou, L.: Instruction-following evaluation for large language models. arXiv
preprint arXiv:2311.07911 (2023)
[38] Zhuo, T.Y., Vu, M.C., Chim, J., Hu, H., Yu, W., Widyasari, R., Yusuf,
I.N.B., Zhan, H., He, J., Paul, I., et al.: Bigcodebench: Benchmarking code
generation with diverse function calls and complex instructions.
arXiv
preprint arXiv:2406.15877 (2024)

```
