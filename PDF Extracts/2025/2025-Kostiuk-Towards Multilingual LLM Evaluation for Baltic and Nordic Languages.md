---
title: "2025-Kostiuk-Towards Multilingual LLM Evaluation for Baltic and Nordic Languages - PDF Extract"
source_pdf: "2025-Kostiuk-Towards Multilingual LLM Evaluation for Baltic and Nordic Languages.pdf"
pages: 11
extracted_at: "2026-02-13T13:14:07.998271"
---

# PDF Extract: 2025-Kostiuk-Towards Multilingual LLM Evaluation for Baltic and Nordic Languages

**Source PDF:** 2025-Kostiuk-Towards Multilingual LLM Evaluation for Baltic and Nordic Languages.pdf
**Total Pages:** 11

---

## Content

```
--- Page 1 ---

Towards Multilingual LLM Evaluation for Baltic and Nordic languages:
A study on Lithuanian History
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
In this work, we evaluated Lithuanian
and general history knowledge of multi-
lingual Large Language Models (LLMs)
on a multiple-choice question-answering
task. The models were tested on a dataset
of Lithuanian national and general history
questions translated into Baltic, Nordic,
and other languages (English, Ukrainian,
Arabic) to assess the knowledge sharing
from culturally and historically connected
groups. We evaluated GPT-4o, LLaMa3.1
8b and 70b, QWEN2.5 7b and 72b, Mis-
tral Nemo 12b, LLaMa3 8b, Mistral 7b,
LLaMa3.2 3b, and Nordic fine-tuned mod-
els (GPT-SW3 and LLaMa3 8b).
Our results show that GPT-4o consistently
outperformed all other models across lan-
guage groups, with slightly better results
for Baltic and Nordic languages. Larger
open-source models like QWEN2.5 72b
and LLaMa3.1 70b performed well but
showed weaker alignment with Baltic lan-
guages.
Smaller models (Mistral Nemo
12b, LLaMa3.2 3b, QWEN 7B, LLaMa3.1
8B, and LLaMa3 8b) demonstrated gaps
with LT-related alignment with Baltic lan-
guages while performing better on Nordic
and other languages.
The Nordic fine-
tuned models did not surpass multilingual
models, indicating that shared cultural or
historical context alone does not guarantee
better performance.
1
Introduction
Large Language Models (LLMs) provide a func-
tional framework for tackling various natural lan-
guage processing (NLP) tasks, such as question-
answering (Izacard et al., 2022; Dong et al., 2024),
machine translation (Zhu et al., 2023; Kocmi et al.,
2024) and so on. However, LLMs have shown less
reliable results for low-resource languages (Ran-
jan et al., 2024; Sakib and Das, 2024) due to the
smaller fraction of available data in comparison to
English and a few other widely spoken languages.
Benchmarking multilingual LLMs across lan-
guages is essential for evaluating their capabilities.
However, the availability of high-quality, cultur-
ally aligned datasets remains a challenge.
This
need for culturally aligned high-quality datasets
becomes even more critical when evaluating his-
torical knowledge, where ensuring linguistic and
cultural fairness adds a layer of complexity.
Verifying comparability of the results on histor-
ical knowledge QA datasets requires that a sin-
gle set of historical events is queried in all lan-
guages. The choice of that set is likely to be biased
to events more represented in widely spoken lan-
guages. Conversely, events that are more region-
or cultural-specific are less likely to occur in the
benchmarks. Finding and addressing these gaps
is important to improve the fairness of LLMs and
highlight historical and cultural biases.
In this work, we focus on evaluating multi-
lingual LLMs on Lithuanian and general history.
Our goal is to determine how LLMs perform on
Lithuanian history exam questions when prompted
in different languages and explore the alignment
between languages and historical awareness, par-
ticularly within the Nordic and Baltic language
groups.
Our contribution is the following:
• We automatically translated publicly avail-
able
Lithuanian
history
exam
question-
answering
dataset
into
Nordic
(Danish,
Finnish, and Swedish), Baltic (Estonian and
Latvian), and other (Arabic, Ukrainian, and
English) languages and partially manually
evaluated it.
• We tested GPT-4o (OpenAI et al., 2024),
arXiv:2501.09154v1  [cs.CL]  15 Jan 2025

--- Page 2 ---

LLaMa3.2 3b, LLaMa3 8b, LLaMa3.1 8b
and 70b (Dubey et al., 2024), Mistral Nemo
12b (Jiang et al., 2023),
QWEN2.5 7b
and 72b (Team, 2024; Yang et al., 2024),
and GPT-SW3 and Nordic-trained LLaMa3
8b (Ekgren et al., 2023) models and com-
pared their achieved accuracy scores per lan-
guage and its average per language group.
Our findings revealed that GPT-4o consistently
outperformed other models across all evaluated
languages and language groups on a dataset of
LT-related and general history questions. Larger
open-source models, such as LLaMa3.1 70b and
QWEN2.5 72b, also demonstrated strong and con-
sistent performance in all languages. In contrast,
smaller models like Mistral Nemo 12b, LLaMa3
8b, LLaMa3.2 3b, and LLaMa3.1 8b showed no-
table gaps in their historical knowledge from a
Lithuanian perspective, particularly with Baltic
languages, despite Lithuanian being part of this
group.
The best performance was observed in
the Nordic language group, suggesting that cul-
tural or historical alignment alone does not ensure
higher accuracy.
Interestingly, the Nordic pre-
trained models failed to surpass the multilingual
model.
2
Related Work
Pre-trained LLMs have exhibited a remarkable
ability to encode and retrieve factual and common
knowledge across different languages (Wang et al.,
2023; Zhao et al., 2024). However, there is a no-
table variation in model performance across lan-
guages, with a strong shift toward high-resource
languages (Qi et al., 2023), particularly languages
with Latin scripts (Ifergan et al., 2024).
The datasets used for benchmarking multilin-
gual LLMs are created using either one of the
two approaches: human annotation (Kocmi et al.,
2023; Goyal et al., 2022) or translating existing an-
notated datasets using LLMs (Lai et al., 2023).
Although datasets created by human annota-
tors provide accurate translations and task-specific
precision, they require considerable investment of
both time and finances (Yang et al., 2019).
On the other hand, with an advancement of
LLMs, the translation performance of automatic
tools has been significantly boosted lately. For ex-
ample, ChatGPT demonstrates fewer errors with
the launch of the GPT-4 engine, even for distant
languages (Jiao et al., 2023). The quality control
research on the DeepL translation tool found that
DeepL1 performed well in terms of translation ac-
curacy, fluency, and naturalness, reaching an over-
all semantic similarity score 94.13 (Linlin, 2024).
This improvement elevated the creation of
benchmark datasets on various tasks.
DeepL
was used for creating the X-FACT multilingual
factual knowledge dataset translated in 25 lan-
guages (Gupta and Srikumar, 2021).
In the re-
search (Thellmann et al., 2024), five well-known
datasets of various tasks were translated by DeepL
into 21 European languages. LLMs with different
numbers of parameters were evaluated on newly
introduced datasets.
The authors observed that
models generally achieve higher performance on
Romance and Germanic languages compared to
Slavic languages.
ChatGPT was utilized to translate the 158K En-
glish instructions into 26 languages, including 7
low-resource languages (Lai et al., 2023).
The
data was used to instruction-tune LLM for mul-
tiple languages using reinforcement learning from
human feedback. The resulting framework, Okapi,
was also evaluated on datasets translated by Chat-
GPT from English into 26 selected languages.
Relying on the aforementioned approaches, in
our work we utilized ChatGPT and DeepL to cre-
ate a dataset with special consideration on Baltic
and Nordic languages. To ensure the quality of
translation for each language, 100 samples of En-
glish version and it’s corresponding translation
were manually evaluated by native speakers. On
average, 77% of such language pairs were ap-
proved.
We offer evaluation on Lithuanian history exam
tasks, assessing the ability of multilingual LLMs
to exhibit particular cultural and historical knowl-
edge and evaluating the alignment of this knowl-
edge within regional language groups.
3
Methodology
In this paper, we investigate performance consis-
tency of LLMs within Nordic and Baltic language
groups on the Lithuanian history exams questions.
We hypothesized that the LLMs perform better in
this domain, when presented with questions in lan-
guages from Nordic and Baltic groups than from
other due to the cultural, linguistic and historical
similarities.
1https://www.deepl.com/

--- Page 3 ---

Figure 1: Example of the dataset sample in Lithua-
nian.
The methodology consists of two steps: data
preparation and models’ benchmarking.
Data Preparation.
To test the hypothesis, we
chose EXAMS (Hardalov et al., 2020) dataset.
Specifically, we used samples that correspond to
Lithuanian history. Each sample contains a ques-
tion, four different answer choices marked with
the labels A,B,C and D with an indication of the
correct one (see Figure 1). Questions and choices
are in Lithuanian. We manually removed the ques-
tions that require an image to answer it, obtaining
550 samples.
The dataset was machine translated into Nordic
(Danish, Finnish, and Swedish), Baltic (Estonian
and Latvian), and outside of Nordic-Baltic, multi-
lingual language group: Ukrainian, English, and
Arabic.
In more details, the dataset was trans-
lated from Lithuanian to English, and then the
English translations were translated in other lan-
guages. We used GPT-4o (OpenAI et al., 2024)
and DeepL as translation algorithms, as they are
proven to have a good machine translation perfor-
mance from- and to-English rather than between
underrepresented languages (Wang, 2024; Hendy
et al., 2023).
After that, we separated dataset into 2 parts:
Lithuanian national history related questions (LT-
related) and general history questions.
We as-
signed a question to the LT-related group if it
specifically mentions Lithuania, mentions Lithua-
nian historic figure or a question about the coun-
try that Lithuania was a part of or occupied by
Figure 2: Example of the chat prompts that the
model was presented to evaluate the dataset in
Lithuanian and English languages.< . . . > is the
actual question that the model is evaluated on.
(e.g.
Polish-Lithuanian Commonwealth, USSR
after 1940 etc.). Other questions were assigned to
a general history questions group.
To ensure quality, a subset of the dataset was
evaluated manually by a group of native speakers.
Annotators were presented with 100 English and
translated language pairs (50 from LT-related and
50 from General history dataset) with 20 samples
being the same for all the annotators to measure
the annotators’ agreement. For more details, see
Appendix A.
Models’ benchmarking.
We experimented on
the following models: LLaMa3 8b, LLaMa3.1 70b
and 8b (Dubey et al., 2024), LLaMa3.2 3b (Dubey
et al., 2024), Mistral Nemo 12b (Jiang et al.,
2023), GPT-4o (OpenAI et al., 2024), QWEN2.5
7b and 72b (Team, 2024; Yang et al., 2024), and
families of instruct pre-trained models developed
by AI Sweden2: GPT-SW3 (Ekgren et al., 2023)
(126m, 356m, 1.3b, 6.7b) pre-trained for and
LLaMa3 8b fine-tuned for Swedish, Norwegian
and Danish. GPT-SW3 models were pre-trained
for Swedish, Norwegian, Danish, Icelandic, En-
glish, and programming code and LLaMa3 8b (we
will refer to this model as NRD LLaMa3 from now
on to avoid confusion) was fine-tuned for Swedish,
Norwegian and Danish.
2https://huggingface.co/
AI-Sweden-Models

--- Page 4 ---

In our experiments, we used multilingual in-
struct LLMs. During generation, all the parame-
ters were set to defaults, except for random seed,
which we set to 2 with Ollama 3 framework for
open source models.
For Nordic models, we
used implementation from the transformers (Wolf
et al., 2020). Specifically, we used GPT-SW3 and
Swedish LLaMa3 8b4.
For each language in the translated dataset,
the model was evaluated on the multiple choices
question-answering task.
The model was pre-
sented with a system message in English explain-
ing the task, four question-answering examples in
the corresponding language, and finally, a ques-
tion with answer choices that the model has to an-
swer. The examples were presented in the same
format as the final question and consisted of ques-
tion, four answer choices marked with A, B, C, D,
and the correct letter for an answer as an expected
output.
Examples were taken from the modern
(later than 2020) history of Lithuania, and do not
intersect with questions in the dataset. Everything,
except the system prompt, was presented to the
model in the evaluated language (see Figure 2).
The results were parsed in the following way. If
the model generated more than one letter, the gen-
erated text was separated into words. From these
words, only capital letters were kept that corre-
sponds to possible choice letters A,B,C, or D. If
only one letter was present, it was considered as a
final output. Otherwise, we assume that the model
failed to produce a reasonable output and record it
as if the model’s answer was incorrect. As a re-
sult, we measured accuracy score for each model
and each language.
4
Results and Discussion
For each LLM, we grouped its results per language
group into Nordic (Danish, Finnish, and Swedish),
Baltic (Lithuanian, Latvian, Estonian), and mul-
tilingual (Ukrainian, English, and Arabic). The
accuracy scores per language and averages scores
per language group are presented in Tables 1 and 2
and on Figures 3, 4, and 5.
Our results demonstrated that all the models ex-
cept for GPT-4o obtained better scores for gen-
eral history questions rather than for LT-related
ones. This observation is expected due to a biased
3https://github.com/ollama/ollama
4https://huggingface.co/collections/
AI-Sweden-Models/
training datasets for such models towards English-
centric data.
The largest evaluated model, GPT-4o, per-
formed consistently better than other models for
LT-related and general history questions in all lan-
guage groups. The model achieved a maximum
average score of 0.88 for LT-related history ques-
tions for the Baltic group (BLT) and performed
similarly for Nordic languages (NRD) with a score
of 0.87, though it showed slightly weaker perfor-
mance in the multilingual group (MLT), scoring
0.84. These results suggest better knowledge rep-
resentation for Nordic and Baltic language groups
in LT-related history exams. Among the individual
languages, English and Lithuanian were the best-
performing languages for both LT-related and gen-
eral history questions.
The 70b group of models (QWEN2.5 72b and
LLaMa3.1 70b) demonstrated second best perfor-
mance across all the types of questions. QWEN2.5
showed lower accuracy for Baltic languages on
average, obtaining similar scores for MLT and
NRD groups. Also, in both types of questions,
QWEN2.5 showed similar trends of receiving
lower scores in Estonian and Latvian, but higher
scores for Nordic languages. Additionally, its per-
formance was better in general questions across
all languages, but when it comes to the alignment
with LT-related, model was able to output better
results for English, Swedish, and Danish rather
than for Lithuanian or Baltic languages. In con-
trast, LLaMa3.1 70b did not performed at par with
diff language groups. The results are similar for
all languages in all questions with Arabic being
the weakest and Lithuanian with English slightly
stronger than others.
In case of Mistral Nemo 12b, the model scored
the smallest scores comparing to other, even
smaller (7-8b, 3b) models. It showed similar re-
sults across all language groups, obtaining the
same average accuracy scores (36%) on Baltic and
Nordic group on LT-related questions and a bet-
ter performance for Nordic group on general ques-
tions than for Baltic. The average of MLT group
was better, even though neither score was higher
than 64%.
LLaMa3 8b, QWEN2.5 7b, and LLaMa3.1 8b
demonstrated a weaker performance when tested
on BLT group across all questions. Using Lithua-
nian showed a better results. Similarly, Swedish
and Danish helped QWEN2.5 7b obtain a bet-

--- Page 5 ---

NRD
BLT
MLT
LT
G
LT+G
LT
G
LT+G
LT
G
LT+G
GPT-4o
0.87
0.89
0.88
0.88
0.89
0.89
0.84
0.88
0.86
QWEN2.5 72b
0.74
0.87
0.81
0.71
0.83
0.77
0.76
0.87
0.82
LLaMa3.1 70b
0.72
0.82
0.77
0.72
0.81
0.76
0.72
0.81
0.77
M Nemo 12b
0.36
0.49
0.43
0.36
0.42
0.39
0.41
0.55
0.48
LLaMa3.1 8b
0.47
0.62
0.54
0.44
0.57
0.50
0.50
0.66
0.58
LLaMa3 8b
0.45
0.48
0.46
0.39
0.40
0.40
0.48
0.53
0.50
QWEN2.5 7b
0.49
0.62
0.56
0.46
0.48
0.47
0.58
0.73
0.65
LLaMa3.2 3b
0.40
0.50
0.45
0.34
0.33
0.34
0.42
0.47
0.45
Table 1: Average accuracy results per language group and model. NRD stands for Nordic, BLT stands
for Baltic, and MLT stands for multilingual language groups. LT-R, G, and LT+G stand for Lithuania-
related history questions, general history questions and merged history questions respectively. M Nemo
12b refers to Mistral Nemo 12b model.
SW
DN
EN
LTR
G
LTR+G
LTR
G
LTR+G
LTR
G
LTR+G
NRD LLaMa3 8b
0.43
0.50
0.46
0.42
0.51
0.46
−
−
−
GPT-SW3 126m
0.27
0.22
0.24
0.27
0.21
0.24
0.27
0.20
0.24
GPT-SW3 356m
0.27
0.21
0.24
0.27
0.21
0.24
0.23
0.20
0.21
GPT-SW3 1.3b
0.23
0.24
0.23
0.23
0.23
0.23
0.23
0.24
0.24
GPT-SW3 6.7b
0.32
0.27
0.29
0.33
0.29
0.29
0.24
0.28
0.26
Table 2: Accuracy results for Nordic fine-tuned models. NRD LLaMa3 8b refers to pre-trained LLaMa3
8b by AI Sweden. LTR, G, and LTR+G stand for Lithuania-related history questions, general history
questions and merged history questions respectively. SW (Swedish), DN (Danish), EN (English) indicate
a language that was used for evaluating the model.
ter score. This results indicate that these models
are better aligned with Lithuanian national history
when asked in a language from Nordic group or
in Lithuanian. LLaMa3.2 3b showed similar per-
formance on NRD group to Mistral Nemo, but
in MLT and BLT settings it received the lowest
scores.
The Nordic-specific models performed simi-
larly on all their supported languages.
From
the considered models, NRD LLaMa3 is a clear
winner.
It demonstrated a similar performance
across its supported languages and is very close
to LLaMa3.2 performance on Swedish and Dan-
ish, but still underperformed LLaMa3.1 8b and
QWEN2.5 7b on the corresponding languages.
When it comes to a family of GPT-SW3, the
greater the amount of parameters - the better per-
formance.
GPT-SW3 6.7b outperformed other
versions of the model across Swedish and Dan-
ish. However, on English, GPT-SW3 with 126m
performed better on LT-related questions.
Figure 3: Accuracy results per language for LT-
related history questions.
Figure 4: Accuracy results per language for gen-
eral history questions.

--- Page 6 ---

Figure 5:
Accuracy results per language for
merged LT-related and general history questions.
In conclusion, our experiments show that GPT-
4o performs consistently better across all tested
languages and language groups on LT-related and
general history questions.
Larger open source
models, LLaMa3.1 70b and QWEN2.5 72b also
performed consistently well in all languages. Mis-
tral Nemo 12b, LLaMa3 8b, LLaMa3.2 3b, and
LLaMa3.1 8b demonstrated significant gaps in
their historical knowledge for LT-related history
questions within Baltic language group, even
when Lithuanian is part of this group. The bet-
ter performance was obtained in Nordic language
group, indicating that cultural or historical align-
ment alone does not guarantee higher accuracy for
these models. The Nordic pre-trained models were
not able to outperform the multilingual model, re-
jecting our initial hypothesis.
5
Conclusion
This study evaluated the performance of Large
Language Models (LLMs) on Lithuanian histori-
cal multiple-choice question-answering tasks, fo-
cusing on Baltic, Nordic, and other language
groups. The models were evaluated on the Lithua-
nian national history related (LT-related) questions
and a general history questions.
Our findings showed that GPT-4o consistently
outperformed all other tested models across lan-
guages, achieving the highest scores for LT-related
and general history questions, with slightly better
results for Baltic and Nordic languages. Among
open-source models, larger models QWEN2.5 72b
and LLaMa3.1 70b performed well but did not
match GPT-4o, especially in Baltic languages.
Smaller models, including Mistral Nemo 12b,
LLaMa3.2 3b, QWEN 7B, LLaMa3.1 8B, and
LLaMa3 8b demonstrated weaker results with
Baltic languages, including Lithuanian, while per-
forming better in Nordic and multilingual groups.
Nordic fine-tuned models performed consis-
tently across their supported languages but failed
to surpass general multilingual models, even
within their specialized domain. These findings
highlight that shared cultural or historical con-
text alone does not guarantee better model per-
formance.
To bridge these gaps, further efforts
are needed to develop targeted datasets and fine-
tuning strategies to improve LLM alignment with
less-resourced languages like those in the Baltic
language group.
References
Guanting Dong, Yutao Zhu, Chenghao Zhang, Zechen
Wang, Zhicheng Dou, and Ji-Rong Wen. 2024. Un-
derstand what LLM needs: Dual preference align-
ment for retrieval-augmented generation.
CoRR,
abs/2406.18676.
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

--- Page 7 ---

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

--- Page 8 ---

Zach Rait, Zachary DeVito, Zef Rosnbrick, Zhaoduo
Wen, Zhenyu Yang, and Zhiwei Zhao. 2024. The
llama 3 herd of models.
Ariel Ekgren, Amaru Cuba Gyllensten, Felix Stol-
lenwerk, Joey
¨Ohman, Tim Isbister, Evangelia
Gogoulou, Fredrik Carlsson, Alice Heiman, Judit
Casademont, and Magnus Sahlgren. 2023. Gpt-sw3:
An autoregressive language model for the nordic
languages. arXiv preprint arXiv:2305.12987.
Naman Goyal, Cynthia Gao, Vishrav Chaudhary, Peng-
Jen Chen, Guillaume Wenzek, Da Ju, Sanjana Kr-
ishnan, Marc’Aurelio Ranzato, Francisco Guzm´an,
and Angela Fan. 2022. The Flores-101 evaluation
benchmark for low-resource and multilingual ma-
chine translation.
Transactions of the Association
for Computational Linguistics, 10:522–538.
Ashim Gupta and Vivek Srikumar. 2021. X-fact: A
new benchmark dataset for multilingual fact check-
ing. In Proceedings of the 59th Annual Meeting of
the Association for Computational Linguistics and
the 11th International Joint Conference on Natu-
ral Language Processing (Volume 2: Short Papers),
pages 675–682, Online. Association for Computa-
tional Linguistics.
Momchil
Hardalov,
Todor
Mihaylov,
Dimitrina
Zlatkova, Yoan Dinkov, Ivan Koychev, and Preslav
Nakov. 2020.
EXAMS: A multi-subject high
school examinations dataset for cross-lingual and
multilingual question answering.
In Proceedings
of the 2020 Conference on Empirical Methods in
Natural Language Processing, EMNLP ’20, pages
5427–5444, Online. Association for Computational
Linguistics.
Amr Hendy, Mohamed Abdelrehim, Amr Sharaf, Vikas
Raunak, Mohamed Gabr, Hitokazu Matsushita,
Young Jin Kim, Mohamed Afify, and Hany Has-
san Awadalla. 2023. How good are gpt models at
machine translation? a comprehensive evaluation.
arXiv preprint arXiv:2302.09210.
Maxim Ifergan, Leshem Choshen, Roee Aharoni, Idan
Szpektor, and Omri Abend. 2024. Beneath the sur-
face of consistency: Exploring cross-lingual knowl-
edge representation sharing in llms. arXiv preprint
arXiv:2408.10646.
Gautier Izacard, Patrick Lewis, Maria Lomeli, Lu-
cas Hosseini, Fabio Petroni, Timo Schick, Jane
Dwivedi-Yu, Armand Joulin, Sebastian Riedel, and
Edouard Grave. 2022. Few-shot Learning with Re-
trieval Augmented Language Models.
Albert Q. Jiang, Alexandre Sablayrolles, Arthur Men-
sch, Chris Bamford, Devendra Singh Chaplot, Diego
de las Casas, Florian Bressand, Gianna Lengyel,
Guillaume Lample, Lucile Saulnier, L´elio Re-
nard Lavaud, Marie-Anne Lachaux, Pierre Stock,
Teven Le Scao, Thibaut Lavril, Thomas Wang, Tim-
oth´ee Lacroix, and William El Sayed. 2023. Mistral
7b.
Wenxiang Jiao, Wenxuan Wang, Jen-tse Huang, Xing
Wang, Shuming Shi, and Zhaopeng Tu. 2023.
Is
chatgpt a good translator? yes with gpt-4 as the en-
gine. arXiv preprint arXiv:2301.08745.
Tom Kocmi, Eleftherios Avramidis, Rachel Baw-
den,
Ondˇrej Bojar,
Anton Dvorkovich,
Chris-
tian Federmann, Mark Fishel, Markus Freitag,
Thamme Gowda, Roman Grundkiewicz, Barry Had-
dow, Marzena Karpinska, Philipp Koehn, Benjamin
Marie, Christof Monz, Kenton Murray, Masaaki Na-
gata, Martin Popel, Maja Popovi´c, Mariya Shma-
tova, Steinth´or Steingr´ımsson, and Vil´em Zouhar.
2024.
Findings of the WMT24 general machine
translation shared task: The LLM era is here but MT
is not solved yet. In Proceedings of the Ninth Con-
ference on Machine Translation, pages 1–46, Mi-
ami, Florida, USA. Association for Computational
Linguistics.
Tom Kocmi, Eleftherios Avramidis, Rachel Bawden,
Ondˇrej Bojar, Anton Dvorkovich, Christian Fed-
ermann, Mark Fishel, Markus Freitag, Thamme
Gowda,
Roman Grundkiewicz,
Barry Haddow,
Philipp Koehn, Benjamin Marie, Christof Monz,
Makoto Morishita, Kenton Murray, Makoto Nagata,
Toshiaki Nakazawa, Martin Popel, Maja Popovi´c,
and Mariya Shmatova. 2023.
Findings of the
2023 conference on machine translation (WMT23):
LLMs are here but not quite there yet. In Proceed-
ings of the Eighth Conference on Machine Transla-
tion, pages 1–42, Singapore. Association for Com-
putational Linguistics.
Viet Lai, Chien Nguyen, Nghia Ngo, Thuat Nguyen,
Franck
Dernoncourt,
Ryan
Rossi,
and
Thien
Nguyen. 2023. Okapi: Instruction-tuned large lan-
guage models in multiple languages with reinforce-
ment learning from human feedback. In Proceed-
ings of the 2023 Conference on Empirical Methods
in Natural Language Processing: System Demon-
strations, pages 318–327, Singapore. Association
for Computational Linguistics.
Li Linlin. 2024. Artificial intelligence translator deepl
translation quality control. Procedia Computer Sci-
ence, 247:710–717.
OpenAI, Josh Achiam, Steven Adler, Sandhini Agar-
wal, Lama Ahmad, Ilge Akkaya, Florencia Leoni
Aleman,
Diogo Almeida,
Janko Altenschmidt,
Sam Altman, Shyamal Anadkat, Red Avila, Igor
Babuschkin, Suchir Balaji, Valerie Balcom, Paul
Baltescu,
Haiming Bao,
Mohammad Bavarian,
Jeff Belgum, Irwan Bello, Jake Berdine, Gabriel
Bernadett-Shapiro, Christopher Berner, Lenny Bog-
donoff, Oleg Boiko, Madelaine Boyd, Anna-Luisa
Brakman, Greg Brockman, Tim Brooks, Miles
Brundage, Kevin Button, Trevor Cai, Rosie Camp-
bell, Andrew Cann, Brittany Carey, Chelsea Carl-
son, Rory Carmichael, Brooke Chan, Che Chang,
Fotis Chantzis, Derek Chen, Sully Chen, Ruby
Chen, Jason Chen, Mark Chen, Ben Chess, Chester

--- Page 9 ---

Cho, Casey Chu, Hyung Won Chung, Dave Cum-
mings, Jeremiah Currier, Yunxing Dai, Cory De-
careaux, Thomas Degry, Noah Deutsch, Damien
Deville, Arka Dhar, David Dohan, Steve Dowling,
Sheila Dunning, Adrien Ecoffet, Atty Eleti, Tyna
Eloundou, David Farhi, Liam Fedus, Niko Felix,
Sim´on Posada Fishman, Juston Forte, Isabella Ful-
ford, Leo Gao, Elie Georges, Christian Gibson, Vik
Goel, Tarun Gogineni, Gabriel Goh, Rapha Gontijo-
Lopes, Jonathan Gordon, Morgan Grafstein, Scott
Gray, Ryan Greene, Joshua Gross, Shixiang Shane
Gu, Yufei Guo, Chris Hallacy, Jesse Han, Jeff Har-
ris, Yuchen He, Mike Heaton, Johannes Heidecke,
Chris Hesse, Alan Hickey, Wade Hickey, Peter
Hoeschele, Brandon Houghton, Kenny Hsu, Shengli
Hu, Xin Hu, Joost Huizinga, Shantanu Jain, Shawn
Jain, Joanne Jang, Angela Jiang, Roger Jiang,
Haozhun Jin, Denny Jin, Shino Jomoto, Billie Jonn,
Heewoo Jun, Tomer Kaftan, Łukasz Kaiser, Ali Ka-
mali, Ingmar Kanitscheider, Nitish Shirish Keskar,
Tabarak Khan, Logan Kilpatrick, Jong Wook Kim,
Christina Kim, Yongjik Kim, Jan Hendrik Kirchner,
Jamie Kiros, Matt Knight, Daniel Kokotajlo, Łukasz
Kondraciuk, Andrew Kondrich, Aris Konstantinidis,
Kyle Kosic, Gretchen Krueger, Vishal Kuo, Michael
Lampe, Ikai Lan, Teddy Lee, Jan Leike, Jade Le-
ung, Daniel Levy, Chak Ming Li, Rachel Lim,
Molly Lin, Stephanie Lin, Mateusz Litwin, Theresa
Lopez, Ryan Lowe, Patricia Lue, Anna Makanju,
Kim Malfacini, Sam Manning, Todor Markov, Yaniv
Markovski, Bianca Martin, Katie Mayer, Andrew
Mayne, Bob McGrew, Scott Mayer McKinney,
Christine McLeavey, Paul McMillan, Jake McNeil,
David Medina, Aalok Mehta, Jacob Menick, Luke
Metz, Andrey Mishchenko, Pamela Mishkin, Vin-
nie Monaco, Evan Morikawa, Daniel Mossing, Tong
Mu, Mira Murati, Oleg Murk, David M´ely, Ashvin
Nair, Reiichiro Nakano, Rajeev Nayak, Arvind
Neelakantan, Richard Ngo, Hyeonwoo Noh, Long
Ouyang, Cullen O’Keefe, Jakub Pachocki, Alex
Paino, Joe Palermo, Ashley Pantuliano, Giambat-
tista Parascandolo, Joel Parish, Emy Parparita, Alex
Passos, Mikhail Pavlov, Andrew Peng, Adam Perel-
man, Filipe de Avila Belbute Peres, Michael Petrov,
Henrique Ponde de Oliveira Pinto, Michael, Poko-
rny, Michelle Pokrass, Vitchyr H. Pong, Tolly Pow-
ell, Alethea Power, Boris Power, Elizabeth Proehl,
Raul Puri, Alec Radford, Jack Rae, Aditya Ramesh,
Cameron Raymond, Francis Real, Kendra Rim-
bach, Carl Ross, Bob Rotsted, Henri Roussez,
Nick Ryder, Mario Saltarelli, Ted Sanders, Shibani
Santurkar, Girish Sastry, Heather Schmidt, David
Schnurr, John Schulman, Daniel Selsam, Kyla Shep-
pard, Toki Sherbakov, Jessica Shieh, Sarah Shoker,
Pranav Shyam, Szymon Sidor, Eric Sigler, Maddie
Simens, Jordan Sitkin, Katarina Slama, Ian Sohl,
Benjamin Sokolowsky, Yang Song, Natalie Stau-
dacher, Felipe Petroski Such, Natalie Summers, Ilya
Sutskever, Jie Tang, Nikolas Tezak, Madeleine B.
Thompson, Phil Tillet, Amin Tootoonchian, Eliz-
abeth Tseng, Preston Tuggle, Nick Turley, Jerry
Tworek, Juan Felipe Cer´on Uribe, Andrea Vallone,
Arun Vijayvergiya, Chelsea Voss, Carroll Wain-
wright, Justin Jay Wang, Alvin Wang, Ben Wang,
Jonathan Ward, Jason Wei, CJ Weinmann, Ak-
ila Welihinda, Peter Welinder, Jiayi Weng, Lilian
Weng, Matt Wiethoff, Dave Willner, Clemens Win-
ter, Samuel Wolrich, Hannah Wong, Lauren Work-
man, Sherwin Wu, Jeff Wu, Michael Wu, Kai Xiao,
Tao Xu, Sarah Yoo, Kevin Yu, Qiming Yuan, Woj-
ciech Zaremba, Rowan Zellers, Chong Zhang, Mar-
vin Zhang, Shengjia Zhao, Tianhao Zheng, Jun-
tang Zhuang, William Zhuk, and Barret Zoph. 2024.
Gpt-4 technical report.
Jirui Qi, Raquel Fern´andez, and Arianna Bisazza. 2023.
Cross-lingual consistency of factual knowledge in
multilingual language models.
arXiv preprint
arXiv:2310.10378.
Rajesh Ranjan, Shailja Gupta, and Surya Narayan
Singh. 2024.
A comprehensive survey of bias in
llms: Current landscape and future directions.
Shahnewaz Karim Sakib and Anindya Bijoy Das. 2024.
Unveiling and mitigating bias in large language
model recommendations: A path to fairness.
Qwen Team. 2024. Qwen2.5: A party of foundation
models.
Klaudia
Thellmann,
Bernhard
Stadler,
Michael
Fromm, Jasper Schulze Buschhoff, Alex Jude,
Fabio Barth, Johannes Leveling, Nicolas Flores-
Herr, Joachim K¨ohler, Ren´e J¨akel, et al. 2024.
Towards multilingual llm evaluation for european
languages. arXiv preprint arXiv:2410.08928.
Jiaan Wang, Yunlong Liang, Zengkui Sun, Yuxuan
Cao, Jiarong Xu, and Fandong Meng. 2023. Cross-
lingual knowledge editing in large language models.
arXiv preprint arXiv:2309.08952.
Jingjing Wang. 2024.
Exploring the potential of
chatgpt-4o in translation quality assessment. Jour-
nal of Theory and Practice in Humanities and Social
Sciences, 1(3):18–30.
Thomas Wolf, Lysandre Debut, Victor Sanh, Julien
Chaumond, Clement Delangue, Anthony Moi, Pier-
ric Cistac, Tim Rault, R´emi Louf, Morgan Funtow-
icz, Joe Davison, Sam Shleifer, Patrick von Platen,
Clara Ma, Yacine Jernite, Julien Plu, Canwen Xu,
Teven Le Scao, Sylvain Gugger, Mariama Drame,
Quentin Lhoest, and Alexander M. Rush. 2020.
Transformers: State-of-the-art natural language pro-
cessing. In Proceedings of the 2020 Conference on
Empirical Methods in Natural Language Process-
ing: System Demonstrations, pages 38–45, Online.
Association for Computational Linguistics.
An Yang, Baosong Yang, Binyuan Hui, Bo Zheng,
Bowen Yu, Chang Zhou, Chengpeng Li, Chengyuan
Li, Dayiheng Liu, Fei Huang, Guanting Dong, Hao-
ran Wei, Huan Lin, Jialong Tang, Jialin Wang, Jian
Yang, Jianhong Tu, Jianwei Zhang, Jianxin Ma, Jin
Xu, Jingren Zhou, Jinze Bai, Jinzheng He, Jun-
yang Lin, Kai Dang, Keming Lu, Keqin Chen,

--- Page 10 ---

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
Yinfei Yang, Yuan Zhang, Chris Tar, and Jason
Baldridge. 2019.
PAWS-X: A cross-lingual ad-
versarial dataset for paraphrase identification.
In
Proceedings of the 2019 Conference on Empirical
Methods in Natural Language Processing and the
9th International Joint Conference on Natural Lan-
guage Processing (EMNLP-IJCNLP), pages 3687–
3692, Hong Kong, China. Association for Computa-
tional Linguistics.
Xin Zhao, Naoki Yoshinaga, and Daisuke Oba. 2024.
Tracing the roots of facts in multilingual lan-
guage models: Independent, shared, and transferred
knowledge. arXiv preprint arXiv:2403.05189.
Wenhao Zhu, Hongyi Liu, Qingxiu Dong, Jingjing Xu,
Lingpeng Kong, Jiajun Chen, Lei Li, and Shujian
Huang. 2023. Multilingual machine translation with
large language models: Empirical results and analy-
sis. ArXiv, abs/2304.04675.
A
Manual Translation Quality
Evaluation
The annotation guidelines and examples can be
found in our GitHub repository 5. For each trans-
lated language, we utilized the same following
strategy. We recruited native speaker annotators,
who are also are proficient in English.
They
were presented with 80 random samples from the
dataset distinct for each annotator and 20 sam-
ples that are the same for each annotator. From
those 80 samples, 40 were selected from a pool
of Lithuanian history questions, and other 40 from
the general history question. The same approach
was applied for the remaining 20 samples: 10 were
selected from a pool of Lithuanian history ques-
tions, and other 10 from the general history ques-
tion.
The annotators were presented with the trans-
lated English question, its answer choices and
the corresponding translation for the question and
choices. in the case of Lithuanian to English trans-
lation, the pairs of Lithuanian and English were
presented. They were instructed to determine if
5HIDDEN FOR REVIEW
the translation is correct from the following stand-
points.
The translation accurately conveys the
meaning of the English or Lithuanian text. The
order of answers (with respect to the letters) is
the same in both languages. The names of his-
torical figures, locations, dates, or events are cor-
rectly translated and align with conventions. Text
semantics are clear and do not change the intent or
emphasis of the question or answers. If the transla-
tion contains grammar or phrasing issues, or minor
typos, they do not lead to confusion or ambiguity
and do not change the semantics.
If the translation does not fit the requirements
above, the translation is rejected. The annotation
results and agreements (in a form of number of
intersections) are presented in the Table 3. Dur-
ing our experiments, chatGPT showed poor results
when translating to Latvian and Estonian. There-
fore, we used DeepL to translated Lithuanian to
Latvian and Estonian. The annotation in the Ta-
ble 3 corresponds to DeepL translation.

--- Page 11 ---

Lang Pair
# Reject (A)
# Reject (B)
# Accept (A)
# Accept (B)
Intersect, %
LT-EN
11
18
89
82
75
EN-UA
10
30
90
70
75
EN-AR
28
21
72
79
65
LT-EST*
13
54
87
46
0.55
EN-SW
1
6
99
94
0.9
EN-DN
9
41
91
59
0.6
EN-FN
15
33
78
67
0.73
LT-LAV*
27
43
73
57
0.7
Table 3: Annotation results. * indicates translation with DeepL from Lithuanian to the target language.
# Reject and Accept refer to a number of rejected and accepted samples by the annotator (marked with
letters A and B). Intersect indicates a percentage of samples that annotators assigned the same label.

```
