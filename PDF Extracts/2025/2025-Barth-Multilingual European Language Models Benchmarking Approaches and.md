---
title: "2025-Barth-Multilingual European Language Models Benchmarking Approaches and - PDF Extract"
source_pdf: "2025-Barth-Multilingual European Language Models Benchmarking Approaches and.pdf"
pages: 7
extracted_at: "2026-02-13T13:13:54.519149"
---

# PDF Extract: 2025-Barth-Multilingual European Language Models Benchmarking Approaches and

**Source PDF:** 2025-Barth-Multilingual European Language Models Benchmarking Approaches and.pdf
**Total Pages:** 7

---

## Content

```
--- Page 1 ---

ISCA/ITG Workshop on Diversity in Large Speech and Language Models
Multilingual European Language Models:
Benchmarking Approaches and Challenges
Fabio Barth
DFKI GmbH, Germany
fabio.barth@dfki.de
Georg Rehm
DFKI GmbH, Germany
Humboldt-Universität zu Berlin, Germany
georg.rehm@dfki.de
Abstract
The breakthrough of generative large language
models (LLMs) that can solve different tasks
through chat interaction has led to a significant
increase in the use of general benchmarks to as-
sess the quality or performance of these models
beyond individual applications. There is also a
need for better methods to evaluate and also to
compare models due to the ever increasing num-
ber of new models published. However, most
of the established benchmarks revolve around
the English language. This paper analyses the
benefits and limitations of current evaluation
datasets, focusing on multilingual European
benchmarks. We analyse seven multilingual
benchmarks and identify four major challenges.
Furthermore, we discuss potential solutions to
enhance translation quality and mitigate cul-
tural biases, including human-in-the-loop veri-
fication and iterative translation ranking. Our
analysis highlights the need for culturally aware
and rigorously validated benchmarks to assess
the reasoning and question-answering capabili-
ties of multilingual LLMs accurately.
1
Introduction
Recent advances in large language models (LLMs)
have demonstrated very strong capabilities across
a wide range of natural language processing (NLP)
tasks. Their performance is measured and quanti-
fied using well-established benchmarks in which
the models have to perform tasks such as, among
others, reasoning, question answering (QA), or
common-sense inference on English text (see, e. g.,
Hendrycks et al., 2021; Lin et al., 2022; Zellers
et al., 2019). The benchmarks consist of text la-
beled by human annotators (Ding et al., 2024) or
they were developed with the help of machine learn-
ing techniques that annotate or label the original
text data automatically (Pfister and Hotho, 2024).
Benchmarks are intended to simulate complex
problems so that they can provide, when applied to
a specific model, an overall impression of how well
the model can solve a particular task. Numerous
benchmarks exist for a very wide range of tasks,
especially with regard to the English language and
English-centric LLMs. High-quality multilingual
benchmarks for multilingual models are relatively
rare. There are non-English monolingual bench-
marks developed together with annotators who are
native speakers (Pfister and Hotho, 2024) and a few
high-quality multilingual benchmarks on reading
comprehension, e. g., Bandarkar et al. (2024).
Recently, researchers have been using multilin-
gual benchmarks that are comparable across lan-
guages (Touvron et al., 2023). For instance, in late
2024, three multilingual LLMs were published that
cover all 24 European languages (Ali et al., 2024;
Martins et al., 2024; Gonzalez-Agirre et al., 2025).
EuroLLM and Teuken-7B were evaluated using En-
glish (MMLU, Hellaswag, TruthfulQA) and a few
multilingual benchmarks (Hendrycks et al., 2021;
Zellers et al., 2019; Lin et al., 2022; Bandarkar
et al., 2024). These evaluations were performed us-
ing machine-translated versions of English bench-
marks regarding multilingual reasoning, QA, or
common-sense inference (Thellmann et al., 2024).
Salamandra, however, was evaluated on multilin-
gual datasets that had been human-annotated or
human-translated, but do not cover all European
languages (Baucells et al., 2025).
The translated benchmarks are, like the original
English versions, multiple-choice problems, where
the model has to choose the correct answer or out-
put from four possible answer options. The cor-
rect answer can be calculated by generating the
correct output (Zellers et al., 2019) or measuring
the log-likelihood of each possible answer (Wiland
et al., 2024). The benefit of automatically trans-
lated benchmarks is that, besides cost- and time-
efficiency in terms of dataset generation, the scores
are comparable across languages.1
1https://huggingface.co/spaces/occiglot/
1
arXiv:2502.12895v2  [cs.CL]  2 Apr 2025

--- Page 2 ---

ISCA/ITG Workshop on Diversity in Large Speech and Language Models
This process has two pitfalls that complicate
interpreting the benchmarks’ scores.
First, the
benchmarks are not flawless translations of the En-
glish versions. Benchmarks that contain a signifi-
cant amount of incorrect, incomplete or inadequate
translations can distort model predictions – espe-
cially considering that a single incorrectly trans-
lated option in a multiple choice setting changes
the whole problem space (Lin et al., 2022).
To overcome this issue human annotators or
an improved and more comprehensive translation
pipeline are needed. For instance, a translation-
verification process with a human in the loop could
help enhance these benchmarks in terms of their
translation quality. Another solution could be an it-
erative process of automatically ranking the transla-
tions and re-translating them until the total transla-
tion ranking has crossed a certain threshold. There
are already models and metrics that can measure
and score translation quality (Rei et al., 2020).
The second problem relates to cultural biases in-
herently embedded in the English benchmarks that
cannot be addressed using automated translations
only (Singh et al., 2024). For example, the MMLU
benchmark contains graduate questions from the
US that rely heavily on national knowledge (regard-
ing history, religion etc.) (Hendrycks et al., 2021).
These questions are not meaningful when evalu-
ating the reasoning and QA capabilities of LLMs
regarding European languages and cultures.
However, there are already some efforts to trans-
late these benchmarks into multiple languages
with regard to cultural biases.
Note that these
approaches involve human annotators that correct
these biases (Singh et al., 2024).
This paper analyses the most commonly used
benchmarks for multilingual LLMs for European
languages. We highlight the benefits and inter-
pretability of the existing benchmarks and outline
their limitations.
2
Approaches
In this section, we discuss the different approaches
to developing multilingual benchmarks. We exam-
ine seven multilingual general-domain benchmarks,
some of which only partially cover all 24 official
EU languages; only one benchmark covers 23 out
of 24 languages (Bandarkar et al., 2024). We anal-
yse benchmarks that include at least nine of the 24
languages. It must be noted that we do not discuss
euro-llm-leaderboard
machine translation benchmarks such as FLORES-
200, as these assess the quality of translations rather
than the performance on general tasks.
2.1
Multilingual Benchmarks
The benchmarks can be broadly categorised into
two groups based on the way they were developed.
On the one hand, multilingual benchmarks are
based on English-language benchmarks that were
translated into different languages. These bench-
marks are either machine-translated or translated
by human annotators (occasionally, professional
translators). GlobalMMLU (Singh et al., 2024) and
MMMLU2 belong to this category, they were de-
veloped by translating the MMLU benchmark into
multiple languages. Two different approaches were
used: professional human translators translated
MMMLU into 14 languages; using professional
human translators is less cost- and time-efficient
than simply using automated translation technolo-
gies. GlobalMMLU was machine-translated and
then annotated by human annotators, organised as
an open-source community, using a public anno-
tation framework. As the translation process was
automated, Singh et al. (2024) have been able to
translate the original dataset into a total of 42 lan-
guages including 11 European languages. To max-
imise the inclusion of human-translated content,
GlobalMMLU also includes human translations
of MMMLU. Both data sets show that including
human annotators and translators to improve trans-
lation quality leads to a smaller task scope and
overall sample size (Singh et al., 2024).
Thellmann et al. (2024) published EU20, a
benchmark that contains translations of five well-
established English benchmarks for 20 official EU
languages, which cover grade-school science ques-
tions (Clark et al., 2018), grade-school math word
problems (Cobbe et al., 2021), common-sense in-
ference (Zellers et al., 2019), tests to measure a
model’s propensity to reproduce falsehoods (Lin
et al., 2022), and elementary mathematics, US his-
tory, computer science, law, and multiple choice
QA (Hendrycks et al., 2021). The benchmarks
were translated using the DeepL translation ser-
vice. The automated translations were not validated
by human translators. For the OKAPI benchmark
Lai et al. (2023) translated the same benchmarks
as EU20 except for GSM8K. This benchmark dif-
fers from EU20 with regard to language coverage
2https://huggingface.co/datasets/openai/MMMLU
2

--- Page 3 ---

ISCA/ITG Workshop on Diversity in Large Speech and Language Models
and the used translation service. For OKAPI, Lai
et al. (2023) used ChatGPT instead of Deepl. It
comprises translations into 26 different languages,
including 11 European languages.
The second category of benchmarks includes
multilingual datasets that are not based on English
data but on regional or multilingual data sources.
Here, we can also distinguish between task-specific
and multi-task benchmarks.
Include (Romanou et al., 2024) is a knowledge-
and reasoning-centric benchmark across 44 lan-
guages, including 15 European languages. It was
constructed based on local exam sources in the
44 languages it includes and consists of 197,243
multiple-choice QA pairs. The benchmark was
extended with non-English benchmarks like Turk-
ishMMLU (Yüksel et al., 2024) or PersianMMLU
(Ghahroodi et al., 2024). Include is more exten-
sive than EXAMS (Hardalov et al., 2020), a cross-
lingual and multilingual QA benchmark using high
school exams with limited domain coverage.
Belebele (Bandarkar et al., 2024) is a multiple
choice machine reading comprehension (MRC)
benchmark that covers 122 languages, including all
EU languages except Irish. It was developed based
on FLORES200 (NLLB Team et al., 2022) and
contains a total of 900 questions in a total of 122
languages, each with four multiple-choice answers.
Xtreme (Hu et al., 2020), on the other hand, is a
comprehensive collection of datasets covering nine
tasks and 40 languages (including 15 European
languages). As the nine tasks do not cover all 40
languages, an evaluation across the majority of
languages is only possible for a subset of tasks (Hu
et al., 2020). Two datasets (XQuAD and MLQA)
have been translated into all 40 languages from the
English source using an “in-house translation tool”
(Hu et al., 2020). Overall, Xtreme covers four
different categories of tasks: QA, classification,
structured prediction, and retrieval.
2.2
Evaluation Methods
Most of the benchmarks described in Section 2.1
are multiple-choice benchmarks that do not test the
multilingual language generation but multilingual
language understanding capabilities of an LLM.
Therefore, the metric for evaluating an LLM using
one of these benchmarks is accuracy or the har-
monic mean of precision and recall (F1 score). The
only exception is the benchmark of Hu et al. (2020),
which contains classification and structured predic-
tion tasks that are also measured using accuracy
and F1-score. However, for the QA tasks of the
Xtreme dataset, the exact match metric is also used.
3
Challenges
We can identify four main challenges regarding
these benchmarks. Below, we explain these and
show why these limitations have to be considered
when using the benchmarks for the evaluation of
LLMs that cover many or all European languages.
3.1
Challenge 1: Cross-Lingual Comparison
Besides providing an overview of an LLM’s capa-
bilities in various languages, multilingual bench-
marks are used to enable cross-lingual comparisons,
which highlight a model’s capabilities for all lan-
guages and show its limits for multilingual use
cases. For multilingual benchmarks these compar-
isons also provide insights into a model’s transfer
learning capabilities if they have only been trained
on a subset of the languages.
Benchmarks like Xtreme contain a dataset col-
lection covering various tasks, which makes them
difficult to interpret for a cross-lingual compari-
son. Xtreme claims to cover 40 languages; for each
task, they provide at least one gold-standard data
set. But that does not cover all aspects of each
language necessary for transfer because the charac-
teristics of a language can vary depending on the
task, domain, and register in which it is used (Hu
et al., 2020).
To provide such insights, the samples in a
benchmark have to be comparable across lan-
guages. Benchmarks like GlobalMMLU, Belebele
or MMMLU use human annotators and translators
to verify the sample comparison (Singh et al., 2024;
Bandarkar et al., 2024) while automatically trans-
lated benchmarks like Thellmann et al. (2024) or
Lai et al. (2023) are, by definition, unable to enable
or guarantee cross-lingual comparisons without a
human validation of the translations. Translations
can contain tokens or syntactic structures that let
the reader backtrack to the original source language.
This phenomenon is called translationese (Koppel
and Ordan, 2011).
3.2
Challenge 2: Translationese
Translationese is a linguistic phenomenon charac-
terised by interference from the source language,
leading to unnatural structures in the target lan-
guage (Singh et al., 2024). In other words, trans-
lationese can be described as artifacts or markers
3

--- Page 4 ---

ISCA/ITG Workshop on Diversity in Large Speech and Language Models
in the target translations that can be used to iden-
tify the source language (Koppel and Ordan, 2011).
Typically, these artifacts cause a drop in evalua-
tion quality. On the other hand, models unfamiliar
with the source language could benefit from those
artifacts in the target translation.
Nevertheless, there are solutions to overcome
these linguistic qualms. Professional annotators
or translators who validate translations to improve
their quality through post-edits can mitigate transla-
tionese artifacts in the target language (Singh et al.,
2024). There are also tools for automatic trans-
lation quality estimations that use a human-based
scoring system to assess the quality of a specific
translation (Rei et al., 2020; Kocmi and Federmann,
2023). It can be shown that these metrics are sen-
sitive to translationese. The COMET score, for
example, varies in terms of its absolute ranking
between target translations with and without trans-
lationese. However, the results do not show on the
system-level ranking (Zouhar et al., 2024), which
averages three lexical segment-level metric scores
(Rei et al., 2020).
3.3
Challenge 3: Cultural Bias
Most benchmarks evaluate the reasoning capabili-
ties of LLMs. However, reasoning, behavior, and
communication are shaped by culture (Tao et al.,
2024). Therefore, cultural biases in multilingual
datasets present substantial obstacles with regard to
their scope, validity and reliability as global bench-
marks (Singh et al., 2024). Cultural biases will
not be mitigated if benchmarks are automatically
translated from English into other languages. The
published benchmarks apply two different options
to address this limitation. First, human annota-
tors evaluate cultural biases present in the original
dataset. Global-MMLU, for instance, improved
the quality of a multilingual MMLU by engaging
with professional and community annotators that
label samples as culturally-sensitive or culturally-
agnostic (Singh et al., 2024). Using annotators to
verify translations and evaluate cultural bias sup-
ports the effectiveness of a multilingual benchmark.
The second option is to develop a benchmark
based on regional resources. The Include bench-
mark (Romanou et al., 2024) was created based
on local exam sources instead of translating bench-
marks with inherent cultural bias and debiasing
translations. Local exams contain questions about
local history, culture, politics, and geographical
and regional knowledge.
Cultural Sensitivity and Inclusion
Both approaches described in Section 3.3 would
result in benchmarks with less English-centric cul-
tural biases.
However, the first approach miti-
gates and/or outlines existing biases by identifying
whether a dataset is culturally agnostic or not, while
the other approach results in benchmarks with cul-
tural biases regarding the intended languages and
cultures by not considering English sources that
could contain English-centric biases.
The integration of diverse and culturally
grounded knowledge is necessary to achieve a cer-
tain level of inclusivity and fairness for multilingual
evaluations (Singh et al., 2024). Mitigating cultural
bias from benchmarks is fundamental for achieving
a certain level of reliability for global benchmarks,
but – as mentioned – culture shapes reasoning and
is, therefore, an essential component in and for
communication and for solving multilingual tasks.
3.4
Challenge 4: Ensuring Data Quality
Guaranteeing or at least achieving a certain level
of data quality is challenging for all benchmarks.
The reasons can differ and are also related to chal-
lenges already discussed (see Sections 3.1 and 3.2).
This section will discuss cascading data quality is-
sues that emerge from the source material or the
benchmark generation process.
The samples should be evaluated to ensure high
data quality in each iteration of the data processing
pipeline. This can be done by regular manual or
automatic inspections (Bandarkar et al., 2024). For
instance, automatically translated samples can be
evaluated using translation scores or human annota-
tors. Thellmann et al. (2024) show that some trans-
lations have an error rate of up to 2.3%, which was
identified by manually checking samples with un-
expectedly low COMET scores (Thellmann et al.,
2024). These error rates differ in individual lan-
guages and, therefore, also have an impact on cross-
lingual comparability.
As a solution, the scoring and evaluation could
be included in the translation process, and lower-
rated samples could be re-translated or manually an-
notated. However, most translated benchmarks rely
on manual assessment. Bandarkar et al. (2024) use
manual methods to ensure data quality. Through-
out the process of developing the dataset, annotator
alignments were defined. Note that forced annota-
tor alignments for translations could increase trans-
lationese (Clark et al., 2020) but it ensures equiv-
4

--- Page 5 ---

ISCA/ITG Workshop on Diversity in Large Speech and Language Models
alent question difficulty across languages (Ban-
darkar et al., 2024).
4
Conclusions
In this paper, we analysed, to the best of our knowl-
edge, all benchmarks for the European language
area and identified their challenges. The shortcom-
ings of each benchmark are diverse and can be
mitigated at different stages of dataset generation.
It can also be shown that other approaches for de-
veloping datasets can have certain advantages. It
can be concluded that a diverse and comprehen-
sive collection of European language benchmarks
is beneficial to analyse and compare multilingual
language models in detail.
Acknowledgments
The work presented in this paper has re-
ceived funding from the German Federal Min-
istry for Economic Affairs and Climate Action
(BMWK) through the project OpenGPT-X (project
no. 68GX21007D).
References
Mehdi Ali, Michael Fromm, Klaudia Thellmann, Jan
Ebert, Alexander Arno Weber, Richard Rutmann,
Charvi Jain, Max Lübbering, Daniel Steinigen,
Johannes Leveling, Katrin Klug, Jasper Schulze
Buschhoff, Lena Jurkschat, Hammam Abdelwa-
hab, Benny Jörg Stein, Karl-Heinz Sylla, Pavel
Denisov, Nicolo’ Brandizzi, Qasid Saleem, Anirban
Bhowmick, Lennard Helmer, Chelsea John, Pedro Or-
tiz Suarez, Malte Ostendorff, Alex Jude, Lalith Man-
junath, Samuel Weinbach, Carolin Penke, Oleg Fila-
tov, Shima Asaadi, Fabio Barth, Rafet Sifa, Fabian
Küch, Andreas Herten, René Jäkel, Georg Rehm, Ste-
fan Kesselheim, Joachim Köhler, and Nicolas Flores-
Herr. 2024. Teuken-7b-base & teuken-7b-instruct:
Towards european llms. Preprint, arXiv:2410.03730.
Lucas Bandarkar, Davis Liang, Benjamin Muller, Mikel
Artetxe, Satya Narayan Shukla, Donald Husa, Naman
Goyal, Abhinandan Krishnan, Luke Zettlemoyer, and
Madian Khabsa. 2024. The belebele benchmark: a
parallel reading comprehension dataset in 122 lan-
guage variants. In Proceedings of the 62nd Annual
Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 749–775,
Bangkok, Thailand. Association for Computational
Linguistics.
Irene Baucells, Javier Aula-Blasco, Iria de Dios-Flores,
Silvia Paniagua Suárez, Naiara Perez, Anna Salles,
Susana Sotelo Docio, Júlia Falcão, Jose Javier Saiz,
Robiert Sepulveda Torres, Jeremy Barnes, Pablo
Gamallo, Aitor Gonzalez-Agirre, German Rigau, and
Marta Villegas. 2025. IberoBench: A benchmark for
LLM evaluation in Iberian languages. In Proceed-
ings of the 31st International Conference on Compu-
tational Linguistics, pages 10491–10519, Abu Dhabi,
UAE. Association for Computational Linguistics.
Jonathan H. Clark, Eunsol Choi, Michael Collins, Dan
Garrette, Tom Kwiatkowski, Vitaly Nikolaev, and
Jennimaria Palomaki. 2020. Tydi qa: A benchmark
for information-seeking question answering in typo-
logically diverse languages. Transactions of the As-
sociation for Computational Linguistics, 8:454–470.
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot,
Ashish Sabharwal, Carissa Schoenick, and Oyvind
Tafjord. 2018.
Think you have solved question
answering?
try arc, the ai2 reasoning challenge.
Preprint, arXiv:1803.05457.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian,
Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias
Plappert, Jerry Tworek, Jacob Hilton, Reiichiro
Nakano, Christopher Hesse, and John Schulman.
2021. Training verifiers to solve math word prob-
lems. Preprint, arXiv:2110.14168.
Mucong Ding, Chenghao Deng, Jocelyn Choo, Zichu
Wu, Aakriti Agrawal, Avi Schwarzschild, Tianyi
Zhou, Tom Goldstein, John Langford, Anima Anand-
kumar, and Furong Huang. 2024.
Easy2hard-
bench:
Standardized difficulty labels for profil-
ing llm performance and generalization. Preprint,
arXiv:2409.18433.
Omid Ghahroodi, Marzia Nouri, Mohammad Vali
Sanian, Alireza Sahebi, Doratossadat Dastgheib,
Ehsaneddin Asgari, Mahdieh Soleymani Baghshah,
and Mohammad Hossein Rohban. 2024. Khayyam
challenge (persianmmlu): Is your llm truly wise to
the persian language? Preprint, arXiv:2404.06644.
Aitor Gonzalez-Agirre, Marc Pàmies, Joan Llop,
Irene Baucells, Severino Da Dalt, Daniel Tamayo,
José Javier Saiz, Ferran Espuña, Jaume Prats, Javier
Aula-Blasco, Mario Mina, Iñigo Pikabea, Adrián
Rubio, Alexander Shvets, Anna Sallés, Iñaki La-
cunza, Jorge Palomar, Júlia Falcão, Lucía Tormo,
Luis Vasquez-Reina, Montserrat Marimon, Oriol
Pareras, Valle Ruiz-Fernández, and Marta Ville-
gas. 2025. Salamandra technical report. Preprint,
arXiv:2502.08489.
Momchil
Hardalov,
Todor
Mihaylov,
Dimitrina
Zlatkova, Yoan Dinkov, Ivan Koychev, and Preslav
Nakov. 2020. EXAMS: A multi-subject high school
examinations dataset for cross-lingual and multilin-
gual question answering. In Proceedings of the 2020
Conference on Empirical Methods in Natural Lan-
guage Processing (EMNLP), pages 5427–5444, On-
line. Association for Computational Linguistics.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou,
Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
2021. Measuring massive multitask language under-
standing. Preprint, arXiv:2009.03300.
5

--- Page 6 ---

ISCA/ITG Workshop on Diversity in Large Speech and Language Models
Junjie Hu, Sebastian Ruder, Aditya Siddhant, Gra-
ham Neubig, Orhan Firat, and Melvin Johnson.
2020. Xtreme: A massively multilingual multi-task
benchmark for evaluating cross-lingual generaliza-
tion. Preprint, arXiv:2003.11080.
Tom Kocmi and Christian Federmann. 2023. Gemba-
mqm: Detecting translation quality error spans with
gpt-4. Preprint, arXiv:2310.13988.
Moshe Koppel and Noam Ordan. 2011. Translationese
and its dialects.
In Proceedings of the 49th An-
nual Meeting of the Association for Computational
Linguistics: Human Language Technologies, pages
1318–1326, Portland, Oregon, USA. Association for
Computational Linguistics.
Viet Dac Lai, Chien Van Nguyen, Nghia Trung Ngo,
Thuat Nguyen, Franck Dernoncourt, Ryan A. Rossi,
and Thien Huu Nguyen. 2023. Okapi: Instruction-
tuned large language models in multiple languages
with reinforcement learning from human feedback.
Preprint, arXiv:2307.16039.
Stephanie Lin, Jacob Hilton, and Owain Evans. 2022.
TruthfulQA: Measuring how models mimic human
falsehoods. In Proceedings of the 60th Annual Meet-
ing of the Association for Computational Linguistics
(Volume 1: Long Papers), pages 3214–3252, Dublin,
Ireland. Association for Computational Linguistics.
Pedro Henrique Martins, Patrick Fernandes, João Alves,
Nuno M. Guerreiro, Ricardo Rei, Duarte M. Alves,
José Pombal, Amin Farajian, Manuel Faysse, Ma-
teusz Klimaszewski, Pierre Colombo, Barry Haddow,
José G. C. de Souza, Alexandra Birch, and André
F. T. Martins. 2024. Eurollm: Multilingual language
models for europe. Preprint, arXiv:2409.16235.
NLLB Team, Marta R. Costa-jussà, James Cross, Onur
Çelebi, Maha Elbayad, Kenneth Heafield, Kevin Hef-
fernan, Elahe Kalbassi, Janice Lam, Daniel Licht,
Jean Maillard, Anna Sun, Skyler Wang, Guillaume
Wenzek, Al Youngblood, Bapi Akula, Loic Bar-
rault, Gabriel Mejia Gonzalez, Prangthip Hansanti,
John Hoffman, Semarley Jarrett, Kaushik Ram
Sadagopan, Dirk Rowe, Shannon Spruit, Chau
Tran, Pierre Andrews, Necip Fazil Ayan, Shruti
Bhosale, Sergey Edunov, Angela Fan, Cynthia
Gao, Vedanuj Goswami, Francisco Guzmán, Philipp
Koehn, Alexandre Mourachko, Christophe Rop-
ers, Safiyyah Saleem, Holger Schwenk, and Jeff
Wang. 2022.
No language left behind:
Scal-
ing human-centered machine translation. Preprint,
arXiv:2207.04672.
Jan Pfister and Andreas Hotho. 2024. SuperGLEBer:
German language understanding evaluation bench-
mark. In Proceedings of the 2024 Conference of
the North American Chapter of the Association for
Computational Linguistics: Human Language Tech-
nologies (Volume 1: Long Papers), pages 7904–7923,
Mexico City, Mexico. Association for Computational
Linguistics.
Ricardo Rei, Craig Stewart, Ana C Farinha, and Alon
Lavie. 2020. COMET: A neural framework for MT
evaluation. In Proceedings of the 2020 Conference
on Empirical Methods in Natural Language Process-
ing (EMNLP), pages 2685–2702, Online. Association
for Computational Linguistics.
Angelika Romanou, Negar Foroutan, Anna Sotnikova,
Zeming Chen, Sree Harsha Nelaturu, Shivalika
Singh, Rishabh Maheshwary, Micol Altomare, Mo-
hamed A. Haggag, Snegha A, Alfonso Amayuelas,
Azril Hafizi Amirudin, Viraat Aryabumi, Danylo
Boiko, Michael Chang, Jenny Chim, Gal Cohen,
Aditya Kumar Dalmia, Abraham Diress, Sharad
Duwal, Daniil Dzenhaliou, Daniel Fernando Erazo
Florez, Fabian Farestam, Joseph Marvin Imperial,
Shayekh Bin Islam, Perttu Isotalo, Maral Jabbar-
ishiviari, Börje F. Karlsson, Eldar Khalilov, Christo-
pher Klamm, Fajri Koto, Dominik Krzemi´nski,
Gabriel Adriano de Melo, Syrielle Montariol, Yiyang
Nan, Joel Niklaus, Jekaterina Novikova, Johan
Samir Obando Ceron, Debjit Paul, Esther Ploeger,
Jebish Purbey, Swati Rajwal, Selvan Sunitha Ravi,
Sara Rydell, Roshan Santhosh, Drishti Sharma, Mar-
jana Prifti Skenduli, Arshia Soltani Moakhar, Bar-
dia Soltani Moakhar, Ran Tamir, Ayush Kumar
Tarun, Azmine Toushik Wasi, Thenuka Ovin Weeras-
inghe, Serhan Yilmaz, Mike Zhang, Imanol Schlag,
Marzieh Fadaee, Sara Hooker, and Antoine Bosse-
lut. 2024. Include: Evaluating multilingual language
understanding with regional knowledge. Preprint,
arXiv:2411.19799.
Shivalika Singh, Angelika Romanou, Clémentine Four-
rier, David I. Adelani, Jian Gang Ngui, Daniel
Vila-Suero, Peerat Limkonchotiwat, Kelly Marchi-
sio, Wei Qi Leong, Yosephine Susanto, Raymond
Ng, Shayne Longpre, Wei-Yin Ko, Madeline Smith,
Antoine Bosselut, Alice Oh, Andre F. T. Martins,
Leshem Choshen, Daphne Ippolito, Enzo Ferrante,
Marzieh Fadaee, Beyza Ermis, and Sara Hooker.
2024. Global mmlu: Understanding and addressing
cultural and linguistic biases in multilingual evalua-
tion. Preprint, arXiv:2412.03304.
Yan Tao, Olga Viberg, Ryan S Baker, and René F Kizil-
cec. 2024. Cultural bias and cultural alignment of
large language models. PNAS Nexus, 3(9).
Klaudia Thellmann, Bernhard Stadler, Michael Fromm,
Jasper Schulze Buschhoff, Alex Jude, Fabio Barth,
Johannes Leveling, Nicolas Flores-Herr, Joachim
Köhler, René Jäkel, and Mehdi Ali. 2024. Towards
multilingual llm evaluation for european languages.
Preprint, arXiv:2410.08928.
Hugo Touvron, Louis Martin, Kevin Stone, Peter Al-
bert, Amjad Almahairi, Yasmine Babaei, Nikolay
Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti
Bhosale, Dan Bikel, Lukas Blecher, Cristian Canton
Ferrer, Moya Chen, Guillem Cucurull, David Esiobu,
Jude Fernandes, Jeremy Fu, Wenyin Fu, Brian Fuller,
Cynthia Gao, Vedanuj Goswami, Naman Goyal, An-
thony Hartshorn, Saghar Hosseini, Rui Hou, Hakan
Inan, Marcin Kardas, Viktor Kerkez, Madian Khabsa,
6

--- Page 7 ---

ISCA/ITG Workshop on Diversity in Large Speech and Language Models
Isabel Kloumann, Artem Korenev, Punit Singh Koura,
Marie-Anne Lachaux, Thibaut Lavril, Jenya Lee, Di-
ana Liskovich, Yinghai Lu, Yuning Mao, Xavier Mar-
tinet, Todor Mihaylov, Pushkar Mishra, Igor Moly-
bog, Yixin Nie, Andrew Poulton, Jeremy Reizen-
stein, Rashi Rungta, Kalyan Saladi, Alan Schelten,
Ruan Silva, Eric Michael Smith, Ranjan Subrama-
nian, Xiaoqing Ellen Tan, Binh Tang, Ross Tay-
lor, Adina Williams, Jian Xiang Kuan, Puxin Xu,
Zheng Yan, Iliyan Zarov, Yuchen Zhang, Angela Fan,
Melanie Kambadur, Sharan Narang, Aurelien Ro-
driguez, Robert Stojnic, Sergey Edunov, and Thomas
Scialom. 2023. Llama 2: Open foundation and fine-
tuned chat models. Preprint, arXiv:2307.09288.
Jacek Wiland, Max Ploner, and Alan Akbik. 2024.
Bear: A unified framework for evaluating relational
knowledge in causal and masked language models.
Preprint, arXiv:2404.04113.
Arda Yüksel, Abdullatif Köksal, Lütfi Kerem ¸Senel,
Anna Korhonen, and Hinrich Schütze. 2024. Turk-
ishmmlu: Measuring massive multitask language un-
derstanding in turkish. Preprint, arXiv:2407.12402.
Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali
Farhadi, and Yejin Choi. 2019.
Hellaswag: Can
a machine really finish your sentence?
Preprint,
arXiv:1905.07830.
Vilém Zouhar, Pinzhen Chen, Tsz Kin Lam, Nikita
Moghe, and Barry Haddow. 2024. Pitfalls and out-
looks in using comet. Preprint, arXiv:2408.15366.
7

```
