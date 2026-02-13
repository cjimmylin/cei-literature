---
title: "2025-Bogoychev-MultiLoKo A Multilingual Local Knowledge Benchmark - PDF Extract"
source_pdf: "2025-Bogoychev-MultiLoKo A Multilingual Local Knowledge Benchmark.pdf"
pages: 27
extracted_at: "2026-02-13T09:15:43.893325"
---

# PDF Extract: 2025-Bogoychev-MultiLoKo A Multilingual Local Knowledge Benchmark

**Source PDF:** 2025-Bogoychev-MultiLoKo A Multilingual Local Knowledge Benchmark.pdf
**Total Pages:** 27

---

## Content

```
--- Page 1 ---

MultiLoKo: a multilingual local knowledge
benchmark for LLMs spanning 31 languages
Dieuwke Hupkes∗Nikolay Bogoychev∗
Meta
{dieuwkehupkes,nbogoych}@meta.com
Abstract
We present MultiLoKo, a new benchmark for evaluating multilinguality in LLMs
covering 31 languages. MultiLoKo consists of three partitions: a main partition con-
sisting of 500 questions per language, separately sourced to be locally relevant to
the specific language, and two translated partitions, containing human-authored
translations from 30 non-English languages to English and vice versa. For com-
parison, we also release corresponding machine-authored translations. The data
is equally distributed over two splits: a dev split and a blind, out-of-distribution
test split. MultiLoKo can be used to study a variety of questions regarding the
multilinguality of LLMs as well as meta-questions about multilingual benchmark
creation. We compute MultiLoKo scores for 11 base and chat models marketed
to be multilingual and study their average performance, their performance parity
across languages, how much their ability to answer questions depends on the ques-
tion language, and which languages are most difficult. None of the models we
studied performs well on MultiLoKo, as indicated by low average scores as well as
large differences between the best and worst scoring languages. Furthermore, we
find a substantial effect of the question language, indicating suboptimal knowledge
transfer between languages. Lastly, we find that using local vs English-translated
data can result in differences more than 20 points for the best performing models,
drastically change the estimated difficulty of some languages. For using machines
instead of human translations, we find a weaker effect on ordering of language
difficulty, a larger difference in model rankings, and a substantial drop in estimated
performance for all models.
1
Introduction
With the growing presence and deployment of LLMs across the world, evaluating their abilities
in languages other than English becomes more and more eminent. Yet, studying and evaluating
multilinguality in LLMs remains a challenging enterprise, and it is hardly exaggerated to call the
current state of multilingual evaluation in LLMs insufficient. Older multilingual benchmarks such
as PAWS-X (Zhang et al., 2019), XNLI (Conneau et al., 2018) or XCOPA (Ponti et al., 2020) often
do not fit the demands for evaluating auto-regressive models and are rarely used to evaluate recent
models. Furthermore, their coverage of languages is relatively small compared to the number of
languages in which LLMs are intended to be proficient.
More often used for LLM evaluation are benchmarks translated from English, such as MGSM
(translated GSM8K, Shi et al., 2023), MMMLU (tranlated MMLU, OpenAI, 2025) or (less frequently)
Belebele (Bandarkar et al., 2024). These benchmarks provide good coverage over many languages,
but using translated data comes with its own set of issues. One such issues is that even when human-
rather than machine-authored translations are used, translated data is known to differ from native
text in several ways (Clark et al., 2020). Furthermore, using translated benchmarks imposes a strong
∗Equal contributions
arXiv:2504.10356v2  [cs.CL]  15 Apr 2025

--- Page 2 ---

English-centric bias: translated data may be multilingual on the surface, it is not in its content. The
benchmarks MLQA (Lewis et al., 2020) and TidyQA (Clark et al., 2020) to some extent address the
issue by sourcing data separately for different languages. Even in their sourcing protocols, however,
there is no explicit focus on selecting locally relevant content for the chosen languages.2 In addition
to that, their coverage is again small compared to the above mentioned translated benchmarks.
In response to these issues, we introduce a wide-coverage multilingual benchmark with locally-
sourced questions for 31 different languages. Because the benchmark targets multilingual local
knowledge, we dub it MultiLoKo. The release of MultiLoKo serves two interconnected goals:
1) Provide a better means to evaluate multilinguality in LLMs;
2) Provide data to study the effect of various design choices in multilingual evaluation.
To address our first goal, we create 500 questions per language, written from scratch for each language,
using a sourcing protocol specifically designed to ensure local relevance of the question topics. To also
reap the benefits of parallel data, we commissioned both human and machine-authored translations
for all non-English questions into English and vice versa, providing a total of 15500 parallel questions,
sourced across the 31 languages in the benchmark. The translated data facilitates the study of transfer
between languages and also serves our second goal. By comparing the English-translated data with
the locally sourced data, we can explicitly compare the adequacy of using translated benchmarks; by
comparing human- with machine-authored translations, we can better estimate the potential issues of
the latter. To prevent quick overfitting and inadvertent contamination, we release a development set
of the benchmark, while test scores can only be obtained through an external provider.3
We provide elaborate analyses for both our goals. We compute average performance and language
parity scores on the locally sourced data for 11 models marketed for their multilinguality (§ 5.1); we
investigate whether these models exhibit knowledge transfer between different languages (§ 5.2);
we study the impact of local sourcing versus translating on model rankings and language difficulty
(§ 5.4.1); we analyse the difficulty of the included languages through various lenses (§ 5.3); and we
conduct an analysis into the difference between human- and machine-authored translation (§ 5.4.3).
We find that, of the models we consider, the best performing model is Gemini 2.0 Flash, with an
average performance of 34.4 points, and an almost 35 point gap between the best and the worst
language. Llama 3.1 405B and GPT4-o are close contenders in terms of average scores (34.3 and
34.0, respectively), but both have substantially higher language gaps (39 and 49 points). Almost
across the board, model performances are better when questions are asked in the language to which
the content is relevant, indicating suboptimal knowledge transfer between languages, a result that is
mirrored by low response-consistency across question language.
Next, we study the relevance of using locally sourced data as opposed to translated English data
as well as whether it matters if translations are authored by humans or machines. We find that the
estimated difficulty of some languages changes drastically across the two sourcing setups, within the
range of 15 points decrease and 8 points increase on average across models. The rank correlation
between average language difficulty score is 0.78. Furthermore, individual model scores between
locally and English-translated data can differ up to 22 points for some languages. However, changing
the sourcing setup does not impact model rankings, suggesting that using translated data may be
suitable for comparing models but less for model development or language prioritisation. For using
machine- instead of human-authored translations, as well, the effect on model ranking is limited
(R=0.97), but the difficulty estimates of various languages changes with up to 12 points. Furthermore,
using machine translated data results in lower average scores for all models, with drops ranging from
2 to 34% of the human-translated scores.
Outline
In the remainder of this paper, we first describe our dataset collection protocol and the
dataset itself in § 2 and § 3, respectively. In § 4, we describe our experimental setup. In § 5, we
present a range of different results, covering (among other things), the summary of results described
above. We conclude in § 6. As we discussed quite some related work above, we do not include a
separate related work section in the main paper, but we do provide a discussion of a wider range of
multilingual datasets in Appendix E.
2An exception to this is the benchmark EXAMS (Hardalov et al., 2020), which consists of exams separately
sourced for each language. For reasons unknown to the authors of this work, it was never used for any prominent
LLM release, with the exception of (Dubey et al., 2024), who deployed it for training rather than evaluation.
3The MultiLoKo data, five few-shot examples per language, an evaluation script, a set of language-
specific prompts, and information about test-score submissions can be found at https://github.com/
facebookresearch/multiloko/.
2

--- Page 3 ---

2
Dataset collection
The main data collection protocol of MultiLoKo is similar to the protocol used by the well-known
benchmark SQuAD (Rajpurkar et al., 2016): we source articles from Wikipedia and ask annotators to
generate questions about paragraphs sampled from these articles. After that, we run several rounds of
quality control on the generated questions and commission human- and machine-authored translations
of all data. Our collection protocol consists of five steps.
Step 1: Paragraph selection
The first step in our protocol is the sampling of the 6K most visited
Wikipedia pages for each language for the period of 2016-2021. We sample paragraphs from those
pages by randomly selecting a word in the page and expanding left and right until we reach 3K
characters. Next, we ask annotators to judge the local relevance of the samples on a scale from 1 to 5,
where 1 refers to topics specific to the language (e.g. a Swedish singer not known outside of Sweden)
and 5 to globally well-known topics (e.g. ‘Youtube’). We disregard all topics that have a locality
score above 3. The full rubric and annotation instructions can be found in Appendix D.1.
Step 2: Question generation
In step 2, we ask native speakers to generate challenging questions
about the content in the paragraphs. To facilitate automatic scoring, we ask that the questions are
closed-form questions, with only one correct short answer. To ensure that the annotation instructions
are understandable and appropriate for each locale and the questions of high quality, we run a pilot
with 50 questions separately for each language. After our pilot, we commission 500 additional
samples for each language, to leave a 10% margin to disregard questions in the rest of the process.
Step 3: Question review
For each generated question, we ask a new set of annotators from a
separate provider to judge whether the generated questions abide by the annotation instructions, to
flag any possible issues, and to mark if the question is useable as is, would be useable with a small
adaptation or should be disregarded. We ask annotators to fix small annotators on the spot, and as
respective vendors that questions with larger issues are replaced.
Step 4: Question answering
As a last quality control step, we ask two annotators different from
the creator of the question to answer the questions. In this stage, we do not ask annotators to correct
questions, but we simply disregard all questions for which either annotator thinks the original answer
was incorrect, or the annotator provided an answer not matching the original answer because of
ambiguities in the question. The only corrections we allow in this stage are additions of additional,
semantically equivalent, correct answers (e.g. ‘four’ as an alternative to ‘4’).
Step 5: Translation
Lastly, we translate the non-English data back to English and vice versa. This
effort serves two purposes. First, it allows to study generalisation of knowledge and skills between
English and non-English languages through a direct comparison of the same questions. Second, it
facilitates inspection of the topics and questions for all languages of the dataset, without the need to
be able to speak all those languages. As automatic translation of benchmarks is relatively common
practice in the field (e.g. Li et al., 2024), we commission both human and machine translations and
study their difference as part of our analysis. For the machine translations, we use Google Translate
sentence based cloud API.4
3
MultiLoKo the dataset
MultiLoKo consists of three main components: i) the collected data; ii) a set of multilingual prompts
to prompt base- and chat models; and iii) a set of metrics.
3.1
The collected data
The data in MultiLoKo consists of several partitions and two splits.
Partitions
MultiLoKo contains one main partition, containing locally-soured data for 31
languages, including English.
In addition to that, it contains four translated partitions.
Two of those are human-translated partitions: human-translated-from-english, consisting
of human-authored translations of English data into the 30 other languages in MultiLoKo,
4https://cloud.google.com/translate?hl=en
3

--- Page 4 ---

human-translated-to-english containing human-authored translations of the non-English sub-
sets into English. The other two are machine-translated partitions following the same pattern:
machine-translated-from-english, contains machine-authored translations of English data into
30 other languages, and machine-translated-to-english contains machine-authored translations
of the non-English subsets into English. All partitions contain 500 samples per language – thus in
total 15500 samples in the main partition, and 15000 samples in the translated partitions. Statistics
about the dataset such as the distribution over answer types and the average prompt length can be
found in Appendix A. Results relating to the difficulty of the benchmark can be found in § 5.
Splits
Each partition is divided equally over two splits: a dev split that can be used for development,
and a blind test split. Each of these splits thus contains 250 samples per language. Until the test
split is publicly released, results can only be obtained through model submissions.5 The splits are
not random, but constructed such that for each language the most frequently visited pages are in
the dev split while the least frequently visited pages are in the test split, roughly preserving the
distribution of answer types (e.g. number, name, year, etc). The test split can thus be seen as an
out-of-distribution (ood) split, specifically meant to assess generalisation (which is challenging in
the context of LLMs, see e.g. Hupkes et al., 2023). In § 5.4.2 we provide an analysis of the extent
to which the split is truly an ood split, by analysing its difficulty. The results reported in the results
section of the paper are dev results.
3.2
Prompts and few-shot examples
Running MultiLoKo requires prompts. In the spirit of getting truly multilingually appropriate results,
we design prompts separately for each language and release them along with the data. The prompts are
written by different linguistic experts for the various languages, in consultation with the benchmark
creators to ensure they are appropriate for LLMs. We provide prompts for base models and chat
models that allow for incorporating up to five few-shot examples, which we also provide.6 All
prompts and few-shot examples can be found in the MultiLoKo repository.
3.3
Metrics
MultiLoKo has two main metrics and two auxiliary metrics. The two main metrics – Exact Match
accuracy (EM) and Gap – capture the overall performance of MultiLoKo and are computed on the
main partition, whereas the two auxiliary metrics – Mother Tongue Effect (MTE) and Locality Effect
(LE) – combine information from different partitions. We provide a cheat-sheet in Table 1.
EM and Gap
EM indicates the performance of a model on a single language or averaged across
languages, as measured by the percentage of times the model (after post-processing) provides an
answer that verbatim matches one of the answers in the reference list. Gap, defined as the difference
between the best and the worst performing language in the benchmark, is a measure of parity
across the individual languages within the benchmark. Taken together, EM and Gap provide a good
indication of how well a model is faring on MultiLoKo. Because both gap and EM are binary metrics
that may be open to false negatives, we also considered the partial match metrics BLEU (Papineni
et al., 2002), ChrF (Popovi´c, 2015) and contains. We did not find any novel patterns using those
metrics, but include them in our implementation for future research.
MTE
Because of the 2x2 design of MultiLoKo, in which we translated non-English data back to
English and vice versa, we can compute several metrics related to locality of the requested information.
MTE is one of such metrics. It expresses the impact of asking a question in a language to which that
question is relevant. We quantify MTE (for non-English languages only), as the difference between
the EM score of the locally sourced data asked in the corresponding language (e.g. asking a question
about a local Bengali radio station in Bengali) and the EM score when the same questions are asked
in English. A positive MTE indicates that information is more readily available when it is relevant to
the language in which it was asked, whereas a negative MTE indicates that the information is more
easily accessible in English. MTE is a measure related to transfer as well as language proficiency.
5More details can be found at https://github.com/facebookresearch/multiloko/.
6In several recent works it has been shown that prompts can have a substantial impact on model scores (e.g.
Weber et al., 2023; Mizrahi et al., 2024). Given the large number of languages in the benchmark and the fact
that those are not all mastered by the main authors, we did not include a systematic search through prompts, but
presented our best-effort results.
4

--- Page 5 ---

Average EM
The first main metric we use to quantify performance for MultiLoKo is the average Exact
Match score across languages, which expresses how many of the answers match one of the gold
standard answers verbatim (after post-processing the answers).
Gap
The second main metric is the gap between a model’s best and worst performing language. We
gap to quantify the extent to which a model has achieved parity across languages. Because a
small gap can be achieved both through parity on high scores as parity on low scores, it is most
informative in combination with average benchmark performance.
Mother tongue
effect (MTE)
MTE expresses the impact of asking questions in a language in which the requested information
is locally salient, compared to asking it in English. A positive MTE indicates information is
more readily available in the language it was (likely) present in the training data, whereas a
negative mother tongue effect indicates the information is more easily accessible in English.
Locality effect
(LE)
LE quantifies the effect of using locally sourced vs translated data. It is measured by computing
the difference between scores for locally sourced data and translated English-sourced data.
A positive LE implies that using translated English data underestimates performance on a
language, a negative LE that using translated English data overestimates performance.
Table 1: MultiLoKo metric cheatsheet. We use several metrics to quantify model performance
using MultiLoKo. This table provides a cheatsheet for their meaning.
LE
The locality effect (LE) is a measure of how much performance on knowledge tasks is over- or
underestimated through the use of using translated English data, as opposed to locally relevant data.
We quantify the locality effect as the difference in EM for English translated data and locally sourced
data. If for a language the English translated data has as a higher EM, the LE is positive, indicating
that using English translated data likely overestimating a model’s ability on providing knowledge for
that language. If the LE is negative the English translated data may provide an underestimation of the
score for that language. Note that because we often observe both positive and negative LEs for the 30
non-English languages in MultiLoKo, the average LE across languages may be small, even if the
differences for individual languages may be large.
4
Experimental setup
We test and showcase our benchmark by running experiments with 11 different models of varying
sizes, that were all marketed to have multilingual abilities.
4.1
Models
To test the extent to which MultiLoKo provides useful signal across training stages, we consider both
base and chat models. The base models we include in our experiments are Llama 3.1 70B and 405B
(Dubey et al., 2024), Mixtral 8x22B (team, 2024), and Qwen 2.5 72B (Qwen et al., 2025), the seven
chat models are Gemini 2.0 Flash (Google DeepMind, 2024), GPT4-o (OpenAI et al., 2024), Claude
3.5 Sonnet (Anthropic, 2025), Llama 3.1 70B and 405B Chat, Mixtral 8x22B-it, and Qwen 2.5 72B
instruct. As mentioned before, we run chat and base models with separate prompts.
4.2
Experimental setup
We run all of our experiments with the generation temperature set to 0. To facilitate automatic
evaluation, we include an instruction to answer questions curtly and precisely, producing only a
number/name/location/etc. Full template information can be found in our github repository.
Few-shot prompting
For base models we use a 5-shot prompt. For chat models, we use a 0-shot
prompt, as this is the most likely use mode by chat model users.
Post-processing
Because base models are good at following the instructions, minimal postprocess-
ing is needed: we only lowercase the output and strip punctuation. Chat models often deviate from
the required format, especially in English, in various ways that we discuss in Appendix B. To evaluate
such models beyond their instruction-following issues, we perform more complex post-processing,
aiming to remove any words resembling “answer” from the LLM output, as well as several special
cases for English and Japanese. We provide full details about post-processing in Appendix C.
5

--- Page 6 ---

Model
EM
Gap
Mother tongue effect
Locality effect
Gemini 2.0 Flash
34.39± 2.90
34.80
6.12± 1.90
0.36± 3.40
Llama 3.1 405B
34.31± 2.70
39.20
6.37± 1.70
0.62± 2.70
GPT4-o
33.97± 3.60
48.80
3.08± 2.00
0.35± 2.90
Llama 3.1 405B Chat
27.70± 3.20
40.80
3.97± 2.20
−1.11± 2.70
Llama 3.1 70B
26.92± 2.60
28.80
2.72± 1.70
−0.30± 3.10
Claude 3.5 Sonnet
26.89± 4.40
47.60
24.18± 4.20
0.81± 2.90
Llama 3.1 70B Chat
21.65± 2.80
42.40
0.49± 1.60
−3.32± 3.30
Mixtral 8x22B
21.64± 4.20
43.60
−2.18± 3.00
−0.65± 2.60
Qwen2.5 72B
19.66± 2.30
28.40
2.45± 2.10
−2.28± 2.70
Mixtral 8x22B-it
10.10± 3.10
39.20
−5.41± 2.00
−0.54± 1.70
Qwen2.5 72B instruct
2.54± 0.70
8.00
−1.52± 1.00
0.43± 0.70
Table 2: Aggregate results dev. We report average EM, gap, mother tongue effect and locality effect
for all 11 models on the MultiLoKo dev split. For EM, MTE and LE, we also indicate a confidence
interval equal to two times the standard error across languages. Models are sorted by average EM.
5
Results
As MultiLoKo has several partitions, there are many different results that can be computed. On
a high level, we consider four different types of results. First, in § 5.1, we report average model
results across several categories, including the average performance and an indicator of parity across
languages. Next, in § 5.2, we dive deeper into the knowledge transfer occurring from one language
to another, within individual models. In § 5.3, instead, we focus on differences between individual
languages. Lastly, in § 5.4, we look in more detail at the dataset itself through the lens of model
results, considering in particular the effect of locally sourcing data as opposed to translating English
sourced data (§ 5.4.1), differences between our dev and test split (§ 5.4.2) and the difference
between using human and machine translated data (§ 5.4.3).
5.1
Aggregate results: EM and language gap
In Table 2, we provide a summary of the average dev results. Specifically, for each model, we report
average EM and the gap between the best and the worst language, along with average MTE and LE,
which we will discuss in a later section.7 We report average MTE, EM and LE along with a confidence
interval equal to two times the standard error across languages, roughly equalling previously used
95% confidence intervals (Madaan et al., 2024; Dubey et al., 2024).
5.1.1
Model performance (EM)
In Figure 1a, we show a boxplot of the distribution of the EM scores across models, ordered by
average EM. The best performing models are Gemini 2.0 Flash, Llama 3.1 405B, and GPT4-o, while
Mixtras 8x22B and the Qwen2.5 72B populate the lower rankings on the list. Somewhat surprisingly,
base models are generally outperforming chat models on the benchmark, this is partly due to false
refusals and poor instruction following in the chat models. In some cases, however, the chat models
simply just provide a qualitatively different answer than the base models. The figure shows that
MultiLoKo is a relatively difficult benchmark across the board: the average EM of even the best
performing model barely exceeds 30, while the bottom performing models have EM scores lower
than 20. Also scores for the easiest languages (see also § 5.3) are capped below 50. Furthermore,
for virtually all models performance varies starkly between languages, suggesting that none of the
models we considered are evenly multilingual across the 31 languages in MultiLoKo.
5.1.2
Gap
While average EM score provides some information about a model’s multilingual abilities, the same
EM score can hide many different patterns regarding individual language scores. As we appreciate it
is not always practical to consider 31 separate EM scores in model development, we add a second
7A metric cheatsheet can be found in Table 1.
6

--- Page 7 ---

0
10
20
30
40
50
60
EM
Gemini 2.0 Flash
Llama 3.1 405B
GPT4-o
Llama 3.1 405B Chat
Llama 3.1 70B
Claude 3.5 Sonnet
Llama 3.1 70B Chat
Mixtral 8x22B
Qwen2.5 72B
Mixtral 8x22B-it
Qwen2.5 72B instruct
(a) EM scores
5
10
20
30
topN
0
10
20
30
40
50
Gap
Qwen2.5 72B instruct
Mixtral 8x22B-it
Qwen2.5 72B
Mixtral 8x22B
Llama 3.1 70B Chat
Claude 3.5 Sonnet
Llama 3.1 70B
Llama 3.1 405B Chat
GPT4-o
Llama 3.1 405B
Gemini 2.0 Flash
(b) Gap
Figure 1: EM distributions and Gap dev. (a) Boxplot of observed EM scores for each model, sorted
by mean. (b) Difference between the best EM and the worst of the N next best EM scores, per model.
summary metric to the main metrics of MultiLoKo: the gap between the best and worst performing
languages, reperesentative of the extent to which a model has achieved parity across languages.
In Figure 1a, we already saw that the per-language scores have quite a range for all models. In
Figure 1b, we study this in more detail, by considering the gap between the best language and the
next N best language (30 corresponds to the full benchmark). On the right end of the plot, we see that
already considering only 5 languages besides English, even the best perform has a gap of over five
points – relatively large in absolute terms, very large in relative ones – between English and the worst
of the remaining languages. For the second best two models, the top-5 gap even exceeds 10 points.
As we include more languages, up to the full benchmark, the gap increases, with GPT4-0 showing
gap of almost 50 points. The only models for which the gap is small are the models that have overall
low performance and thus little space to drop from English, illustrating how gap and average EM
provide complementary information about multilingual performance.
5.2
Generalisation across languages
Next, we study whether knowledge generalises across languages or, in other words, whether knowl-
edge transfers from one language to another.
5.2.1
The mother tongue effect (MTE)
First, we compare the EM of models when questions are asked in the language for which the questions
were originally sourced with performance when the same questions are asked in English. We quantify
this effect with the metric MTE, which expresses the difference in performance between these two
settings (see § 3.3). In Figure 2a, we show MTE per language, averaged across models.8 For most
languages, performance is higher when the question is asked in the language for which the question is
locally relevant. The languages for which MTE is negative or close to 0 are virtually all languages that
perform very poorly also in the mother tongue and for which there is therefore little room for further
decrease.9 From one perspective, the improvements when questions are asked in the low-resource
but native languages can be seen as surprising: as models perform much better in English than
non-English languages, one may expect performances to go up as a consequence of that. On the other
hand, similar ‘mother tongue effects’ have been observed in earlier studies. For example, Ohmer
et al. (2024) found that models are comparatively better at answering factual questions about topics
when they are asked in a language to which culture the fact pertains. It appears that also in our case,
8With the used prompt, we could not get Claude 3.5 Sonnet to answer questions in English in an automatically
parsable manner, leading to an abysmal score of 4.8 on the English sourced data and equally low scores on data
translated into English. Examples of this issue can be found in Appendix B. Because this issue is not indicative
of lack of knowledge or transfer, we excluded Claude 3.5 Sonnet from any of the transfer results in this section.
9The exception to this rule is Hindi, which has a reasonable performance in the native language but neverthe-
less improves in English. We further discuss such language-specific points in § 5.3.
7

--- Page 8 ---

Bengali
Hindi
Khmer
Urdu
Farsi
Vietnamese
Hebrew
English
Korean
Marathi
Polish
Spanish
Cantonese
Thai
Tagalog
Turkish
Mandarin (simp)
Mandarin (trad)
Japanese
German
Arabic
Romanian
Malay
French
Portuguese
Dutch
Indonesian
Italian
Swedish
Czech
Russian
15
10
5
0
5
10
Mother tongue effect
(a) Average MTE across models
10
0
10
20
Mother tongue effect
0.00
0.02
0.04
0.06
0.08
0.10
Llama 3.1 405B
Gemini 2.0 Flash
GPT4-o
(b) KDE of MTE scores
Figure 2: Mother tongue effect dev. (a) Per language MTE for MultiLoKo dev, indicating the
difference between questions asked in the mother tongue (locally relevant) and in English. Error bars
indicate 2 times standard error across all models, excluding Claude 3.5 Sonnet. (b) KDE plot of the
distribution of MTE scores for the top-3 performing models.
the effect of accessibility of information in a relevant language wins out over the generally stronger
English performance, pointing to a gap in models’ ability to generalise knowledge from one language
to another.
In Figure 2b, we further consider the distribution of MTE scores for the top-3 models. Interestingly,
this distribution is quite different between models. Despite having comparable average scores, the
top-3 performing models differ in their MTE distributions across languages. Of the three models,
GPT4-o has the smallest average effect (3.2); Llama 3.1 405B has a much higher average effect (6.6),
but less probability mass on the more extreme ranges of the spectrum (min max values of [-7, +12] vs
[-9, +13]) Gemini 2.0 Flash is in the middle in terms of average (6.3), but shows the largest variation
across languages ([-10, +16]).
Note, however, that without studying the actual training data of the various models, it is possible to
infer that all these models have relatively poor transfer across languages, but not conclusively say
that one model is better than another: it is also possible that the information sourced for languages
with better MTEs was simply better represented in the English data of a respective model.
5.2.2
Consistency across responses
Another way to study transfer between languages is to look at the consistency of responses across
languages (previously also used by Qi et al., 2023; Ohmer et al., 2023, i.a.). After all, it is possible
for a model that has an EM of 30 on both English and another language to be nevertheless completely
misaligned on which questions they respond to correctly. Studying consistency across responses can
therefore be seen as a more direct way of studying whether knowledge is equally accessible across
languages. Furthermore, consistency can be studied independently from accuracy, as it is possible for
a model to have very good transfer, but be simply consistently wrong.
In the dataset used by Ohmer et al. (2023), the correct answers (consisting of names, numbers and
years) are identical across the languages they consider, while Qi et al. (2023) use a factual knowledge
task that requires ranking outputs. Neither of their metrics can thus be directly applied in our case.
Specifically, measuring consistency on incorrect responses – an important component of the work of
Ohmer et al. (2023) because it can provide positive rather than negative evidence – would require
assessing whether two answers in different languages are to be considered semantically equivalent,
which is not practically feasible for our data. Rather, we opt for a simpler consistency metric,
which quantifies what percentage of the questions that are answered correctly in either language are
answered correctly in both languages.
In Figure 3a, we show the average consistency of all models (excluding again Claude Sonnet 3.5); for
completeness, we also show the per-language consistency results in Figure 3b. The results confirm
our earlier conclusion that much improvements can be made when it comes to knowledge transfer
8

--- Page 9 ---

Model
Consistency
Gemini 2.0 Flash
0.46± 0.04
Llama 3.1 405B
0.46± 0.04
Llama 3.1 70B
0.45± 0.03
GPT4-o
0.45± 0.05
Llama 3.1 405B Chat
0.42± 0.04
Qwen2.5 72B
0.40± 0.04
Llama 3.1 70B Chat
0.40± 0.04
Mixtral 8x22B
0.36± 0.05
Mixtral 8x22B-it
0.21± 0.05
Qwen2.5 72B instruct
0.08± 0.03
(a) Consistency scores per model
German
Spanish
Dutch
French
Portuguese
Tagalog
Romanian
Swedish
Indonesian
Czech
Italian
Hebrew
Hindi
Russian
Polish
Turkish
Malay
Korean
Vietnamese
Arabic
Mandarin (trad)
Marathi
Japanese
Farsi
Urdu
Mandarin (simp)
Bengali
Thai
Cantonese
Khmer
0.0
0.2
0.4
0.6
Consistency
(b) Consistency scores per language
Figure 3: Consistency results dev. (a) Average per-model consistency scores, ± 2 times the standard
error across languages. (b) Boxplot of model consistency scores per language, indicating the relative
overlap of correctly answered questions when asked in the mother tongue vs in English.
between languages: even for the best performing models, there is an overlap of not even 50%
between the questions correctly answered across languages.
5.3
Differences between languages
So far, with the exception of MTE and parity scores, we have primarily looked at results averaged
across languages. Now, we consider language-specific results in a bit more detail.
0
20
40
60
EM
EM locally sourced
English
Spanish
Tagalog
Portuguese
French
Romanian
Dutch
Indonesian
Russian
German
Czech
Swedish
Italian
Hindi
Marathi
Mandarin (simp)
Mandarin (trad)
Polish
Korean
Urdu
Japanese
Arabic
Bengali
Hebrew
Vietnamese
Turkish
Cantonese
Thai
Malay
Farsi
Khmer
0
20
40
EM
EM translated to English
Figure 4: Average EM per language dev, in mother tongue and English. Top: Average EM on
locally sourced data. Bottom: Average EM on locally sourced data, translated to English.
5.3.1
Language difficulty on locally sourced data
First, in Figure 4 (top), we show average model results for all languages on all locally sourced data.
In broad strokes, the order of difficulty is correlated with how low- or high- resource a language is
to be considered: while languages such as French, English and Spanish occur at the easier end of
the spectrum, we find Farsi, Khmer and Malay among the most difficult languages. There are a few
9

--- Page 10 ---

Malay
Turkish
Dutch
Italian
German
Polish
French
Indonesian
Vietnamese
Czech
Swedish
Portuguese
Romanian
Hebrew
Khmer
English
Farsi
Japanese
Spanish
Tagalog
Cantonese
Korean
Hindi
Thai
Mandarin (simp)
Arabic
Mandarin (trad)
Bengali
Russian
Urdu
Marathi
15
10
5
0
5
10
Locality effect
(a) Locality effect per language
Model
Rank correlation
language difficulty
Gemini 2.0 Flash
0.54
Llama 3.1 405B
0.65
GPT4-o
0.64
Llama 3.1 405B Chat
0.70
Llama 3.1 70B
0.60
Claude 3.5 Sonnet
0.84
Llama 3.1 70B Chat
0.68
Mixtral 8x22B
0.86
Qwen2.5 72B
0.45
Mixtral 8x22B-it
0.88
Qwen2.5 72B instruct
0.55
(b) Language difficulty correlations
Figure 5: Locality Effect dev. (a) Per language Locality Effect, indicating the difference in assigned
scores between locally sourced and translated English data. A positive LE means the locally sourced
data has a higher score (is easier), a negative LE the English sourced data has a higher score. (b)
Per-model rank correlation between language difficulty of languages on locally sourced vs English
translated data.
notable exceptions: on average the second highest scoring language in our benchmark is Tagalog.
While it is difficult to judge why without doing a detailed analysis on the questions, we hypothesise
that the questions asked by the Tagalog language experts are simply less complex than the questions
of other languages.
5.3.2
Separating language difficulty from language proficiency
In an attempt to distinguish data difficulty from language proficiency, we consider also the difficulty
of the locally sourced data translated to English. While this conflates data difficulty and transfer (see
§ 5.2), it still gives us some indication of the extent to which low performance in languages is caused
by poor language proficiency versus data difficulty. In the bottom half of Figure 4, we show the
model performances as computed on the locally sourced data translated to English. The correlation
between these two language difficulty rankings between these setups is 0.79. When comparing the
ranks of the various languages, only a handful of languages shift more than a few places. Specifically,
Bengali (26->4), Urdu (26->12), and Hindi (14->5) all decrease substantially in difficulty rank. The
fact that they are comparatively easier in English suggests that for those languages proficiency may
be a larger problem than data difficulty. On the other hand, only Russian (7->21) shows a drop of
more than 5 places.
5.4
The dataset
Lastly, we discuss two aspects related to the creation of the dataset. Specifically, we consider the
impact of local sourcing vs translated English data, and we have a look at the dataset split across dev
and test. We consider the difference between using human-authored as opposed to machine-authored
translations.
5.4.1
Locally-sourced vs translated-from-English data
To study the impact of using locally sourced data, we consider the difference between per-language
EM on locally sourced data and translated from English data.
Language difficulty
First, we look at per-language differences between locally sourced and
translated English data. We quantify this difference in a metric we call the Locality Effect (LE). The
size of the locality effect tells us how much the estimate of a model’s strength in a particular language
would have been off if we had chosen to use a translated benchmark rather than a locally sourced one.
We plot this difference in Figure 5a.
As we can see, the scores between locally and translated English-sourced data can differ quite drasti-
cally, almost 15 percentage points averaged across models. For individual models, the differences are
10

--- Page 11 ---

even larger. For Llama 3.1 405B, the locality effect ranges from -13 to +17; for Gemini 2.0 Flash
from -21 to +15; and for GPT4-o from -22 to +14. The differences are not just in absolute scores;
also the ordering of language by difficulty is quite different across the two data collection setups, as
can be seen by the per-model rank correlations of language difficulty between the two conditions,
shown in Figure 5b. Using English-translated rather than locally sourced data does thus not only
provide different estimates, but may suggest different languages to focus on for improvement.
Model rankings
Next, we consider the ranking of the models under the two different data regimes.
Interestingly, given the transfer effect, changing from locally to English translated data does not make
any difference in the ranking. Also in terms of absolute scores, the difference between the two data
collection setups is relatively minor. At least for our type of data, it thus appears that using translated
data as opposed to locally sourced data may be a reasonable setup for comparing models on average,
though not for getting adequate per-language or set language prioritisation.
5.4.2
The dataset split
As mentioned in the dataset construction, we took the deliberate decision to generate a split based
on topic frequency, rather than creating a random split. The aim of this out-of-distribution split
is to test generalisation to topics that are more in the tail of the distribution, as well as encourage
improvements in multilinguality beyond having a higher score on the specific released MultiLoKo
dev set. Of course, however, because of our sourcing method, all the topics in MultiLoKo are topics
on which information is available on Wikipedia. As training data, Wikipedia is often packaged as a
single scrape, this may render our deliberate splitting efforts futile: the fact that a page is less visited
does not make it less likely that the specific page is included in the training data. Now, we test if the
dev and test split are in fact distributionally different.
0
10
20
30
40
50
60
EM
Gemini 2.0 Flash
Llama 3.1 405B
GPT4-o
Llama 3.1 405B Chat
Llama 3.1 70B
Claude 3.5 Sonnet
Llama 3.1 70B Chat
Mixtral 8x22B
Qwen2.5 72B
Mixtral 8x22B-it
Qwen2.5 72B instruct
split
dev
test
Figure 6: Average EM, dev versus test. We show the difference in score distributions between the
MultiLoKo dev and test set. The results confirm that the test set is indeed out of distribution with
respect to the dev set: dev scores (upper bars) are higher across the board.
In Figure 6, we show boxplots of dev and test EM scores for all models under consideration. The
plot confirms that the split is indeed to be considered an OOD split: for virtually much all models, the
test scores are lower than the dev scores. Across all models, the average dev score is 24, whereas the
average test score is 21. This suggests that our test set does indeed contain more tail knowledge than
the dev set, despite the aforementioned arguments regarding Wikipedia. Interestingly, this implies
that Wikipedia may not be the primary source from which models learn this information.
The difference in difficulty also has bearing on the other metrics: the parity scores (thus: the gap
between the best and worst performing language) is 37 for dev vs 34 for test, suggesting that more
difficult dat may to some extent hide differences between languages and therefore exemplifying the
utility of considering parity along with overall performance. The mother tongue effect, on the other
hand, is comparable across dev and test (1.61 vs 1.56, respectively). For the locality effect, the
11

--- Page 12 ---

effect is less interpretable. While the average difference is substantial (-0.6 dev vs -1.9 test), there
is no clear pattern discernable across languages: for some, the effect reduces, whereas for others it
increases.
Model
R
min ∆
max ∆
avg ∆
Gemini 2.0 Flash
0.80
-10.00
21.60
4.35
Llama 3.1 405B
0.83
-4.40
18.80
5.82
GPT4-o
0.85
-6.00
21.60
4.46
Llama 3.1 405B Chat
0.80
-10.40
22.40
3.08
Llama 3.1 70B
0.77
-7.60
22.00
4.59
Claude 3.5 Sonnet
0.90
-9.60
20.80
2.84
Llama 3.1 70B Chat
0.87
-6.00
20.00
3.12
Mixtral 8x22B
0.91
-3.20
20.00
4.13
Qwen2.5 72B
0.83
-4.00
16.80
3.47
Mixtral 8x22B-it
0.92
-4.80
12.40
2.41
Qwen2.5 72B instruct
0.80
-0.80
3.20
0.36
(a) Language difficulty stats
across human- and machine translations
Russian
Swedish
Urdu
Arabic
Bengali
Marathi
Japanese
English
Korean
Thai
Farsi
Mandarin (simp)
Mandarin (trad)
Hindi
Romanian
Vietnamese
Khmer
Cantonese
Spanish
Czech
Portuguese
Polish
Malay
Hebrew
French
Tagalog
German
Turkish
Dutch
Italian
Indonesian
5
0
5
10
15
20
 EM
(b) MT vs human translations
Figure 7: Machine versus human translations dev. (a) Per-model rank correlation between language
difficulty between MT and human translations, and min, max and average difference between the two
conditions. (b) Difference between EM computed on human- and machine-translated data (human
score - machine score), per language.
5.4.3
Human versus machine translation
Lastly, we consider the impact of using machine- or human-authored translations. To do so, we look
at the differences in EM scores between machine and human translated data for the various languages,
taking the human translations as the ‘gold standard’ (i.e. we consider human translated EM - machine
translated EM). We show the results in Figure 7.
In Figure 7a we show the rank correlations of the difficulties of the various languages per model,
as well as the min, max and average drop from human to machine translations. We see the that, at
the model level, using machine translations rather than human translations results in a systematic
undervaluation of the model scores: there is not a single model for which the ‘drop’ from human to
machine translations is negative on average. In part, this is may be a result of the previously observed
lack of knowledge transfer effect. That the drop is not substantially lower for models with better
transfer, however, suggests that the more impactful factor is the quality of the machine translations,
that may at times result in unanswerable questions.
In terms of model rankings, the difference between machine and human translations is minor: the
model rankings between the two conditions have a rank correlation of 0.97 on the dev split, with only
three local swaps (2&3 and 5&6 and 8&9) of models that did not have statistically different scores to
begin with. This suggests that to compare models, using machine translation can be an acceptable
alternative to human translations, as the mis-estimation is systematic across models.
Considering the effect across languages, we observe that even though the average drop is positive, for
virtually all models there are at least some languages for which performance increases when MT is
used, in some cases with even more than 10 points. For a handful of languages – specifically Russian,
Swedish and Urdu – this is also true across models (see Figure 7b). While the overall rank correlation
is high for language difficulty (0.88), it thus still urges caution in using machine translated data for
language improvement prioritisation.
6
Conclusion
Notwithstanding the increasing multinational deployment of LLMs in many parts of the world,
adequately evaluating their multilinguality remains a challenging enterprise. Only in part is this
due to the scarcity of high-quality and broad-coverage multilingual benchmarks for LLM: perhaps
a more pressing issue is that the benchmarks that are frequently used for multilingual evaluation
virtually all consist of translated English data. While using completely parallel data has its advantages,
using translated English data imposes an English-centric bias on the content of the benchmarks,
12

--- Page 13 ---

implying that even if the benchmark evaluates multilinguality on the surface, it does not in content.
In our work, we aim to address this by presenting MultiLoKo, a multilingual benchmark spanning 31
languages that combines the best of both worlds. MultiLoKo contains 500 questions targetting locally
relevant knowledge for 31 languages, separately sourced for each language with a protocol specifically
designed to ensure local relevance of the question topics. It is also fully parallel, because it contains
human-authored translations of the non-English partitions into English and vice versa. As such, it
allows to study various questions related to multilinguality, transfer and multilingual benchmark
creation. To prevent quick overfitting and inadvertent contamination, we release a development set of
the benchmark, while the test set of the benchmarks remains private, at least for the near future.
We use MultiLoKo to analyse 4 base and 7 chat models marketed to be multilingual. We find that, of
the models we consider, the best performing model is Gemini 2.0 Flash, with an average performance
of 34.4 points, and an almost 35 point gap between the best and the worst language, followed by
Llama 3.1 405B and GPT4-o, which are close contenders in terms of average performance but
both have substantially higher language gaps (39 and 49 points). Generally, scores are better when
questions are asked in the language to which they are relevant, indicating suboptimal knowledge
transfer between languages, a result that is mirrored by low per-sample consistency across question
language.
On a meta-level, we study the relevance of using locally sourced data as opposed to translated English
data as well as whether it matters if translations are authored by humans or machines. We find that
the estimated difficulty of some languages changes drastically across the two sourcing setups, within
the range of 15 points decrease and 8 points increase on average across models. The rank correlation
between average language difficulty score is 0.78. Furthermore, individual model scores between
locally and English-translated data can differ up to 22 points for some languages. However, changing
the sourcing setup does not impact model rankings, suggesting that using translated data may be
suitable for comparing models but less for model development or language prioritisation. For using
machine- instead of human-authored translations, as well, the effect on model ranking is limited
(R=0.97), but the difficulty estimates of various languages changes with up to 12 points. Furthermore,
using machine translated data results in lower average scores for all models, with drops ranging from
2 to 34% of the human-translated scores.
While our results section is extensive already, there are still several parts of MultiLoKo that we did
not explore. For instance, because of the sourcing strategy, each native question is coupled with a
paragraph that contains the answer to the question. MultiLoKo could thus be transformed into a
reading-comprehension benchmark, and we consider studying the difference between the knowledge
and reading comprehension setup an interesting direction for future work. Furthermore, each question
contains an elaborate long answer intended to explain the short answer. We have not used the long
answers in any of our experiments, but foresee interesting directions including studies into CoT
prompting or studying answer rationales.
7
Limitations
In this last section, we discuss various limitations of our work.
Local relevance
In our sourcing protocol, we explicitly sought to create questions locally relevant
to the respective languages. It is important to notice, however, that some languages, such as English,
Spanish, Portuguese, Chinese, French and to a lesser extent German and Dutch cover a wide variety of
cultures. We did not separately control for that and the data for those languages thus likely comprises
a mix of different locales.
Data quality
Building a bias-free evaluation datasets with few mistakes is not an easy feat. Even
though we implemented several rounds of quality checks in our data collection pipeline, when
looking at outputs we still incidentally found mistakes in the data or answers. We fixed some of these
mistakes as we encountered them, but it is quite likely that more such mistakes occur in the dataset.
It is also important to point out that we are less likely to spot such issues for languages that we do
not understand at all, potentially creating a bias towards the set of languages for which we have a
rudimentary understanding. Overall, however, we believe that the pipeline we designed assures a
dataset of high quality. Of course, we welcome reports of mistakes spotted by others in the data.
13

--- Page 14 ---

Evaluation
Because MultiLoKo is a generative benchmark, computing scores requires comparisons
of a generated answer with a set of gold answers. A first obstacle to this method of evaluation is
that it is hard to create an exhaustive list of correct short-form answers. This is especially true when
the correct answer is not a number, date, title or something else that can be expressed only in a few
ways. In addition to that, it is hard to incentivise LLMs to produce concise answers. Even when
instructed to answer with only a number / date / name / title, they may respond with a full sentence,
add a reasoning trail to their answer, or add words beyond the minimal answer in a different fashion.
We addressed such issues that were systematic in post-processing (see Appendix B), but it is hard
to a priori catch allthe ways that LLMs may deviate from the requested protocols. In some cases,
we found additional post-processing steps that increased the scores of some models only later in the
process, because scores for particular languages looked suspiciously low. For instance, we had not
initially realised that our punctuation stripper did not strip punctuation in Urdu, which specifically
influenced GPT4-o and Gemini. We considered several other metrics as well as judges, but eventually
found that EM provided the clearest and least biased signal. It remains, however, a challenge to
evaluate chatty LLMs completely independently from their ability to follow instructions.
Wikipedia as information source
MultiLoKo, as several other both multilingual as well as
monolingual benchmarks, uses Wikipedia as main source of information. This has the advantage that
Wikipedia has a large coverage across many different languages and the information is considered
to be of high quality. It also facilitates comparable sourcing across languages. Of course, it also
poses limitations. For one, it still provides a bias to the specific topics that can be included, that are
usually primarily knowledge based. In fact, MultiLoKo is indeed a knowledge benchmark; it does
not consider other types of skills. Secondly, and perhaps more importantly, Wikipedia is a a corpus
frequently used in the training data of LLMs. The fact that MultiLoKo is a challenging benchmark
even given that (multilingual) wikipedia is likely included in the training data of most of the LLMs
evaluated suggests that this is not a large issue at the moment. However, it is very possible that
MultiLoKo can be ‘hacked’ relatively easily simply by strongly oversampling multilingual wikipedia
data.
Acknowledgements
While this paper knows only two authors, this benchmark would not have been possible without
the support and contributions of many people. We wish to thank all of them in this last section.
First, we thank Van Phung, Kriz Chan, Antonio Gai, Dunant Hin and Emily Du for their support on
facilitating and streamlining interactions with vendors for the data collection process, and Milena
Hoffman for her indispensable administrative support in managing the data collection process. We
would furthermore like to thank Van Phung and Kriz Chan for their continued help on ensuring data
quality, saliency checking output, brainstorming and general support throughout the creation of the
benchmark.
We also thank the linguists that helped us for their contributions to the analysis of the pilot questions
in the benchmark, which played an important role in finetuning and improving our annotation protocol
as well as disregard inappropriate questions, and for helping us design prompt templates to allow
language-specific querying of models in different stages for each of the languages in MultiLoKo.
Specifically, we would like to thank Abdul Haque (Urdu), Aleksandra Antokhina (Russian), Ananya
Banerjee (Bengali), Firman Tahar (Indonesian), Florian Mouret (French), Francisco Paredes Mal-
donado (Spanish), Eriko Nakamura (Japanese), Julie Lee (Korean), Khanh Tien (Vietnamese), Miao
Yeh (Traditional Chinese), Renata Barboza (Portuguese), Rishabh Goel (Hindi), Sanket Suhas Satope
(Marathi), Sara Martellini (Italian) and Silvia Aponte (German). We thank Kriz Chan by streamlining
our collaboration with these linguists, and Maria Paez Playa for offering her teams time on this
enterprise. We furthermore thank Sabrina Qiao for providing resources for quick-turnaround QA
support, and Ateeq Awan (English), Kaila Conley-Coversi (Italian), Semanti Roy (Bengali) and
Shahmir Shaikh (English) for delivering this QA support.
As doing manual saliency checks is challenging for a multilingual benchmark, we also relied on the
help of several colleagues to debug small issues, detect errors in questions and prompts and double
check annotation judgements. We would like to thank Anna Prochowska, Daria Dudurca, Diego
Perino, Etai Sella, Ivan John Piramide, Lovish Madaan, Yanir Kleiman for their help on this.
14

--- Page 15 ---

References
Fakhraddin Alwajih, Gagan Bhatia, and Muhammad Abdul-Mageed. Dallah: A dialect-aware
multimodal large language model for Arabic. In Nizar Habash, Houda Bouamor, Ramy Es-
kander, Nadi Tomeh, Ibrahim Abu Farha, Ahmed Abdelali, Samia Touileb, Injy Hamed, Yaser
Onaizan, Bashar Alhafni, Wissam Antoun, Salam Khalifa, Hatem Haddad, Imed Zitouni, Badr
AlKhamissi, Rawan Almatham, and Khalil Mrini, editors, Proceedings of The Second Ara-
bic Natural Language Processing Conference, pages 320–336, Bangkok, Thailand, August
2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.arabicnlp-1.27. URL
https://aclanthology.org/2024.arabicnlp-1.27/.
Anthropic. Claude 3.5 sonnet. https://www.anthropic.com/news/claude-3-5-sonnet, 2025.
Accessed: 2025-04-11.
Mikel Artetxe, Sebastian Ruder, and Dani Yogatama. On the cross-lingual transferability of mono-
lingual representations. In Dan Jurafsky, Joyce Chai, Natalie Schluter, and Joel Tetreault, ed-
itors, Proceedings of the 58th Annual Meeting of the Association for Computational Linguis-
tics, pages 4623–4637, Online, July 2020. Association for Computational Linguistics.
doi:
10.18653/v1/2020.acl-main.421. URL https://aclanthology.org/2020.acl-main.421/.
Lucas Bandarkar, Davis Liang, Benjamin Muller, Mikel Artetxe, Satya Narayan Shukla, Donald
Husa, Naman Goyal, Abhinandan Krishnan, Luke Zettlemoyer, and Madian Khabsa. The belebele
benchmark: a parallel reading comprehension dataset in 122 language variants. In Lun-Wei Ku,
Andre Martins, and Vivek Srikumar, editors, Proceedings of the 62nd Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long Papers), pages 749–775, Bangkok,
Thailand, August 2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.
acl-long.44. URL https://aclanthology.org/2024.acl-long.44/.
Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhari-
wal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agar-
wal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh,
Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler,
Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCan-
dlish, Alec Radford, Ilya Sutskever, and Dario Amodei.
Language models are few-shot
learners.
In Hugo Larochelle, Marc’Aurelio Ranzato, Raia Hadsell, Maria-Florina Balcan,
and Hsuan-Tien Lin, editors, Advances in Neural Information Processing Systems 33: An-
nual Conference on Neural Information Processing Systems 2020, NeurIPS 2020, Decem-
ber 6-12, 2020, virtual, 2020. URL https://proceedings.neurips.cc/paper/2020/hash/
1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html.
Pinzhen Chen, Simon Yu, Zhicheng Guo, and Barry Haddow. Is it good data for multilingual instruc-
tion tuning or just bad multilingual evaluation for large language models? CoRR, abs/2406.12822,
2024. URL https://doi.org/10.48550/arXiv.2406.12822.
Zhihong Chen, Shuo Yan, Juhao Liang, Feng Jiang, Xiangbo Wu, Fei Yu, Guiming Hardy Chen,
Junying Chen, Hongbo Zhang, Li Jianquan, et al. Multilingualsift: Multilingual supervised
instruction fine-tuning, 2023. URL https://arxiv.org/pdf/2412.15115.
Jonathan H. Clark, Eunsol Choi, Michael Collins, Dan Garrette, Tom Kwiatkowski, Vitaly Nikolaev,
and Jennimaria Palomaki. TyDi QA: A benchmark for information-seeking question answering in
typologically diverse languages. Transactions of the Association for Computational Linguistics, 8:
454–470, 2020. doi: 10.1162/tacl_a_00317. URL https://aclanthology.org/2020.tacl-1.
30/.
Alexis Conneau, Ruty Rinott, Guillaume Lample, Adina Williams, Samuel Bowman, Holger Schwenk,
and Veselin Stoyanov. XNLI: Evaluating cross-lingual sentence representations. In Ellen Riloff,
David Chiang, Julia Hockenmaier, and Jun’ichi Tsujii, editors, Proceedings of the 2018 Conference
on Empirical Methods in Natural Language Processing, pages 2475–2485, Brussels, Belgium,
October-November 2018. Association for Computational Linguistics. doi: 10.18653/v1/D18-1269.
URL https://aclanthology.org/D18-1269/.
15

--- Page 16 ---

Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha
Letman, Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan, Anirudh Goyal, Anthony Hartshorn,
Aobo Yang, Archi Mitra, Archie Sravankumar, Artem Korenev, Arthur Hinsvark, Arun Rao, Aston
Zhang, Aurélien Rodriguez, Austen Gregerson, Ava Spataru, Baptiste Rozière, Bethany Biron, Binh
Tang, Bobbie Chern, Charlotte Caucheteux, Chaya Nayak, Chloe Bi, Chris Marra, Chris McConnell,
Christian Keller, Christophe Touret, Chunyang Wu, Corinne Wong, Cristian Canton Ferrer, Cyrus
Nikolaidis, Damien Allonsius, Daniel Song, Danielle Pintz, Danny Livshits, David Esiobu, Dhruv
Choudhary, Dhruv Mahajan, Diego Garcia-Olano, Diego Perino, Dieuwke Hupkes, Egor Lakomkin,
Ehab AlBadawy, Elina Lobanova, Emily Dinan, Eric Michael Smith, Filip Radenovic, Frank Zhang,
Gabriel Synnaeve, Gabrielle Lee, Georgia Lewis Anderson, Graeme Nail, Grégoire Mialon, Guan
Pang, Guillem Cucurell, Hailey Nguyen, Hannah Korevaar, Hu Xu, Hugo Touvron, Iliyan Zarov,
Imanol Arrieta Ibarra, Isabel M. Kloumann, Ishan Misra, Ivan Evtimov, Jade Copet, Jaewon
Lee, Jan Geffert, Jana Vranes, Jason Park, Jay Mahadeokar, Jeet Shah, Jelmer van der Linde,
Jennifer Billock, Jenny Hong, Jenya Lee, Jeremy Fu, Jianfeng Chi, Jianyu Huang, Jiawen Liu, Jie
Wang, Jiecao Yu, Joanna Bitton, Joe Spisak, Jongsoo Park, Joseph Rocca, Joshua Johnstun, Joshua
Saxe, Junteng Jia, Kalyan Vasuden Alwala, Kartikeya Upasani, Kate Plawiak, Ke Li, Kenneth
Heafield, Kevin Stone, and et al. The llama 3 herd of models. CoRR, abs/2407.21783, 2024. doi:
10.48550/ARXIV.2407.21783. URL https://doi.org/10.48550/arXiv.2407.21783.
Alena Fenogenova, Artem Chervyakov, Nikita Martynov, Anastasia Kozlova, Maria Tikhonova,
Albina Akhmetgareeva, Anton Emelyanov, Denis Shevelev, Pavel Lebedev, Leonid Sinev, Ulyana
Isaeva, Katerina Kolomeytseva, Daniil Moskovskiy, Elizaveta Goncharova, Nikita Savushkin,
Polina Mikhailova, Anastasia Minaeva, Denis Dimitrov, Alexander Panchenko, and Sergey Markov.
MERA: A comprehensive LLM evaluation in Russian. In Lun-Wei Ku, Andre Martins, and
Vivek Srikumar, editors, Proceedings of the 62nd Annual Meeting of the Association for Com-
putational Linguistics (Volume 1: Long Papers), pages 9920–9948, Bangkok, Thailand, August
2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.acl-long.534. URL
https://aclanthology.org/2024.acl-long.534/.
Google DeepMind.
Google gemini ai update - december 2024.
https://blog.google/
technology/google-deepmind/google-gemini-ai-update-december-2024/, 2024.
Ac-
cessed: 2025-04-11.
Naman Goyal, Cynthia Gao, Vishrav Chaudhary, Peng-Jen Chen, Guillaume Wenzek, Da Ju, Sanjana
Krishnan, Marc’Aurelio Ranzato, Francisco Guzmán, and Angela Fan. The Flores-101 evaluation
benchmark for low-resource and multilingual machine translation. Transactions of the Association
for Computational Linguistics, 10:522–538, 2022. doi: 10.1162/tacl_a_00474. URL https:
//aclanthology.org/2022.tacl-1.30/.
Momchil Hardalov, Todor Mihaylov, Dimitrina Zlatkova, Yoan Dinkov, Ivan Koychev, and Preslav
Nakov. EXAMS: A multi-subject high school examinations dataset for cross-lingual and multi-
lingual question answering. In Bonnie Webber, Trevor Cohn, Yulan He, and Yang Liu, editors,
Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing
(EMNLP), pages 5427–5444, Online, November 2020. Association for Computational Linguistics.
doi: 10.18653/v1/2020.emnlp-main.438. URL https://aclanthology.org/2020.emnlp-main.
438/.
Yun He, Di Jin, Chaoqi Wang, Chloe Bi, Karishma Mandyam, Hejia Zhang, Chen Zhu, Ning Li,
Tengyu Xu, Hongjiang Lv, Shruti Bhosale, Chenguang Zhu, Karthik Abinav Sankararaman, Eryk
Helenowski, Melanie Kambadur, Aditya Tayade, Hao Ma, Han Fang, and Sinong Wang. Multi-if:
Benchmarking llms on multi-turn and multilingual instructions following. CoRR, abs/2410.15553,
2024.
doi: 10.48550/ARXIV.2410.15553.
URL https://doi.org/10.48550/arXiv.2410.
15553.
Dieuwke Hupkes, Mario Giulianelli, Verna Dankers, Mikel Artetxe, Yanai Elazar, Tiago Pimentel,
Christos Christodoulopoulos, Karim Lasri, Naomi Saphra, Arabella Sinclair, et al. A taxonomy
and review of generalization research in nlp. Nature Machine Intelligence, 5(10):1161–1174, 2023.
Zhengbao Jiang, Antonios Anastasopoulos, Jun Araki, Haibo Ding, and Graham Neubig. X-FACTR:
Multilingual factual knowledge retrieval from pretrained language models. In Bonnie Webber,
Trevor Cohn, Yulan He, and Yang Liu, editors, Proceedings of the 2020 Conference on Empirical
16

--- Page 17 ---

Methods in Natural Language Processing (EMNLP), pages 5943–5959, Online, November 2020.
Association for Computational Linguistics. doi: 10.18653/v1/2020.emnlp-main.479. URL https:
//aclanthology.org/2020.emnlp-main.479/.
Jaap Jumelet, Leonie Weissweiler, and Arianna Bisazza. Multiblimp 1.0: A massively multilingual
benchmark of linguistic minimal pairs. CoRR, abs/2504.02768, 2025. URL https://doi.org/
10.48550/arXiv.2504.02768.
Nora Kassner, Philipp Dufter, and Hinrich Schütze. Multilingual LAMA: Investigating knowledge
in multilingual pretrained language models. In Paola Merlo, Jorg Tiedemann, and Reut Tsarfaty,
editors, Proceedings of the 16th Conference of the European Chapter of the Association for
Computational Linguistics: Main Volume, pages 3250–3258, Online, April 2021. Association for
Computational Linguistics. doi: 10.18653/v1/2021.eacl-main.284. URL https://aclanthology.
org/2021.eacl-main.284/.
Fajri Koto, Nurul Aisyah, Haonan Li, and Timothy Baldwin.
Large language models only
pass primary school exams in Indonesia: A comprehensive test on IndoMMLU. In Houda
Bouamor, Juan Pino, and Kalika Bali, editors, Proceedings of the 2023 Conference on Em-
pirical Methods in Natural Language Processing, pages 12359–12374, Singapore, December
2023. Association for Computational Linguistics. doi: 10.18653/v1/2023.emnlp-main.760. URL
https://aclanthology.org/2023.emnlp-main.760/.
Patrick Lewis, Barlas Oguz, Ruty Rinott, Sebastian Riedel, and Holger Schwenk. MLQA: Evaluating
cross-lingual extractive question answering. In Dan Jurafsky, Joyce Chai, Natalie Schluter, and Joel
Tetreault, editors, Proceedings of the 58th Annual Meeting of the Association for Computational
Linguistics, pages 7315–7330, Online, July 2020. Association for Computational Linguistics. doi:
10.18653/v1/2020.acl-main.653. URL https://aclanthology.org/2020.acl-main.653/.
Haonan Li, Yixuan Zhang, Fajri Koto, Yifei Yang, Hai Zhao, Yeyun Gong, Nan Duan, and Tim-
othy Baldwin.
CMMLU: Measuring massive multitask language understanding in Chinese.
In Lun-Wei Ku, Andre Martins, and Vivek Srikumar, editors, Findings of the Association for
Computational Linguistics: ACL 2024, pages 11260–11285, Bangkok, Thailand, August 2024.
Association for Computational Linguistics.
doi: 10.18653/v1/2024.findings-acl.671.
URL
https://aclanthology.org/2024.findings-acl.671/.
Xi Victoria Lin, Todor Mihaylov, Mikel Artetxe, Tianlu Wang, Shuohui Chen, Daniel Simig, Myle
Ott, Naman Goyal, Shruti Bhosale, Jingfei Du, Ramakanth Pasunuru, Sam Shleifer, Punit Singh
Koura, Vishrav Chaudhary, Brian O’Horo, Jeff Wang, Luke Zettlemoyer, Zornitsa Kozareva, Mona
Diab, Veselin Stoyanov, and Xian Li. Few-shot learning with multilingual generative language
models. In Yoav Goldberg, Zornitsa Kozareva, and Yue Zhang, editors, Proceedings of the 2022
Conference on Empirical Methods in Natural Language Processing, pages 9019–9052, Abu Dhabi,
United Arab Emirates, December 2022. Association for Computational Linguistics. doi: 10.18653/
v1/2022.emnlp-main.616. URL https://aclanthology.org/2022.emnlp-main.616/.
Lovish Madaan, Aaditya K Singh, Rylan Schaeffer, Andrew Poulton, Sanmi Koyejo, Pontus Stenetorp,
Sharan Narang, and Dieuwke Hupkes. Quantifying variance in evaluation benchmarks. arXiv
preprint arXiv:2406.10229, 2024.
Moran Mizrahi, Guy Kaplan, Dan Malkin, Rotem Dror, Dafna Shahaf, and Gabriel Stanovsky.
State of what art? a call for multi-prompt LLM evaluation. Transactions of the Association
for Computational Linguistics, 12:933–949, 2024. doi: 10.1162/tacl_a_00681. URL https:
//aclanthology.org/2024.tacl-1.52/.
Niklas Muennighoff, Thomas Wang, Lintang Sutawika, Adam Roberts, Stella Biderman, Teven
Le Scao, M Saiful Bari, Sheng Shen, Zheng Xin Yong, Hailey Schoelkopf, Xiangru Tang, Dragomir
Radev, Alham Fikri Aji, Khalid Almubarak, Samuel Albanie, Zaid Alyafeai, Albert Webson,
Edward Raff, and Colin Raffel. Crosslingual generalization through multitask finetuning. In Anna
Rogers, Jordan Boyd-Graber, and Naoaki Okazaki, editors, Proceedings of the 61st Annual Meeting
of the Association for Computational Linguistics (Volume 1: Long Papers), pages 15991–16111,
Toronto, Canada, July 2023. Association for Computational Linguistics. doi: 10.18653/v1/2023.
acl-long.891. URL https://aclanthology.org/2023.acl-long.891/.
17

--- Page 18 ---

Xenia Ohmer, Elia Bruni, and Dieuwke Hupkes. Separating form and meaning: Using self-consistency
to quantify task understanding across multiple senses. In Sebastian Gehrmann, Alex Wang,
João Sedoc, Elizabeth Clark, Kaustubh Dhole, Khyathi Raghavi Chandu, Enrico Santus, and
Hooman Sedghamiz, editors, Proceedings of the Third Workshop on Natural Language Generation,
Evaluation, and Metrics (GEM), pages 258–276, Singapore, December 2023. Association for
Computational Linguistics. URL https://aclanthology.org/2023.gem-1.22/.
Xenia Ohmer, Elia Bruni, and Dieuwke Hupke. From form(s) to meaning: Probing the semantic
depths of language models using multisense consistency. Computational Linguistics, 50(4):1507–
1556, 12 2024. ISSN 0891-2017. doi: 10.1162/coli_a_00529. URL https://doi.org/10.1162/
coli_a_00529.
OpenAI. Mmmlu dataset. https://huggingface.co/datasets/openai/MMMLU, 2025. Accessed:
2025-04-11.
OpenAI, :, Aaron Hurst, Adam Lerer, Adam P. Goucher, Adam Perelman, Aditya Ramesh, Aidan
Clark, AJ Ostrow, Akila Welihinda, Alan Hayes, Alec Radford, Aleksander M ˛adry, Alex Baker-
Whitcomb, Alex Beutel, Alex Borzunov, Alex Carney, Alex Chow, Alex Kirillov, Alex Nichol, Alex
Paino, Alex Renzin, Alex Tachard Passos, Alexander Kirillov, Alexi Christakis, Alexis Conneau,
Ali Kamali, Allan Jabri, Allison Moyer, Allison Tam, Amadou Crookes, Amin Tootoochian,
Amin Tootoonchian, Ananya Kumar, Andrea Vallone, Andrej Karpathy, Andrew Braunstein,
Andrew Cann, Andrew Codispoti, Andrew Galu, Andrew Kondrich, Andrew Tulloch, Andrey
Mishchenko, Angela Baek, Angela Jiang, Antoine Pelisse, Antonia Woodford, Anuj Gosalia,
Arka Dhar, Ashley Pantuliano, Avi Nayak, Avital Oliver, Barret Zoph, Behrooz Ghorbani, Ben
Leimberger, Ben Rossen, Ben Sokolowsky, Ben Wang, Benjamin Zweig, Beth Hoover, Blake
Samic, Bob McGrew, Bobby Spero, Bogo Giertler, Bowen Cheng, Brad Lightcap, Brandon
Walkin, Brendan Quinn, Brian Guarraci, Brian Hsu, Bright Kellogg, Brydon Eastman, Camillo
Lugaresi, Carroll Wainwright, Cary Bassin, Cary Hudson, Casey Chu, Chad Nelson, Chak Li,
Chan Jun Shern, Channing Conger, Charlotte Barette, Chelsea Voss, Chen Ding, Cheng Lu,
Chong Zhang, Chris Beaumont, Chris Hallacy, Chris Koch, Christian Gibson, Christina Kim,
Christine Choi, Christine McLeavey, Christopher Hesse, Claudia Fischer, Clemens Winter, Coley
Czarnecki, Colin Jarvis, Colin Wei, Constantin Koumouzelis, Dane Sherburn, Daniel Kappler,
Daniel Levin, Daniel Levy, David Carr, David Farhi, David Mely, David Robinson, David Sasaki,
Denny Jin, Dev Valladares, Dimitris Tsipras, Doug Li, Duc Phong Nguyen, Duncan Findlay,
Edede Oiwoh, Edmund Wong, Ehsan Asdar, Elizabeth Proehl, Elizabeth Yang, Eric Antonow, Eric
Kramer, Eric Peterson, Eric Sigler, Eric Wallace, Eugene Brevdo, Evan Mays, Farzad Khorasani,
Felipe Petroski Such, Filippo Raso, Francis Zhang, Fred von Lohmann, Freddie Sulit, Gabriel Goh,
Gene Oden, Geoff Salmon, Giulio Starace, Greg Brockman, Hadi Salman, Haiming Bao, Haitang
Hu, Hannah Wong, Haoyu Wang, Heather Schmidt, Heather Whitney, Heewoo Jun, Hendrik
Kirchner, Henrique Ponde de Oliveira Pinto, Hongyu Ren, Huiwen Chang, Hyung Won Chung,
Ian Kivlichan, Ian O’Connell, Ian O’Connell, Ian Osband, Ian Silber, Ian Sohl, Ibrahim Okuyucu,
Ikai Lan, Ilya Kostrikov, Ilya Sutskever, Ingmar Kanitscheider, Ishaan Gulrajani, Jacob Coxon,
Jacob Menick, Jakub Pachocki, James Aung, James Betker, James Crooks, James Lennon, Jamie
Kiros, Jan Leike, Jane Park, Jason Kwon, Jason Phang, Jason Teplitz, Jason Wei, Jason Wolfe,
Jay Chen, Jeff Harris, Jenia Varavva, Jessica Gan Lee, Jessica Shieh, Ji Lin, Jiahui Yu, Jiayi
Weng, Jie Tang, Jieqi Yu, Joanne Jang, Joaquin Quinonero Candela, Joe Beutler, Joe Landers,
Joel Parish, Johannes Heidecke, John Schulman, Jonathan Lachman, Jonathan McKay, Jonathan
Uesato, Jonathan Ward, Jong Wook Kim, Joost Huizinga, Jordan Sitkin, Jos Kraaijeveld, Josh
Gross, Josh Kaplan, Josh Snyder, Joshua Achiam, Joy Jiao, Joyce Lee, Juntang Zhuang, Justyn
Harriman, Kai Fricke, Kai Hayashi, Karan Singhal, Katy Shi, Kavin Karthik, Kayla Wood, Kendra
Rimbach, Kenny Hsu, Kenny Nguyen, Keren Gu-Lemberg, Kevin Button, Kevin Liu, Kiel Howe,
Krithika Muthukumar, Kyle Luther, Lama Ahmad, Larry Kai, Lauren Itow, Lauren Workman,
Leher Pathak, Leo Chen, Li Jing, Lia Guy, Liam Fedus, Liang Zhou, Lien Mamitsuka, Lilian Weng,
Lindsay McCallum, Lindsey Held, Long Ouyang, Louis Feuvrier, Lu Zhang, Lukas Kondraciuk,
Lukasz Kaiser, Luke Hewitt, Luke Metz, Lyric Doshi, Mada Aflak, Maddie Simens, Madelaine
Boyd, Madeleine Thompson, Marat Dukhan, Mark Chen, Mark Gray, Mark Hudnall, Marvin
Zhang, Marwan Aljubeh, Mateusz Litwin, Matthew Zeng, Max Johnson, Maya Shetty, Mayank
Gupta, Meghan Shah, Mehmet Yatbaz, Meng Jia Yang, Mengchao Zhong, Mia Glaese, Mianna
Chen, Michael Janner, Michael Lampe, Michael Petrov, Michael Wu, Michele Wang, Michelle
Fradin, Michelle Pokrass, Miguel Castro, Miguel Oom Temudo de Castro, Mikhail Pavlov, Miles
18

--- Page 19 ---

Brundage, Miles Wang, Minal Khan, Mira Murati, Mo Bavarian, Molly Lin, Murat Yesildal, Nacho
Soto, Natalia Gimelshein, Natalie Cone, Natalie Staudacher, Natalie Summers, Natan LaFontaine,
Neil Chowdhury, Nick Ryder, Nick Stathas, Nick Turley, Nik Tezak, Niko Felix, Nithanth Kudige,
Nitish Keskar, Noah Deutsch, Noel Bundick, Nora Puckett, Ofir Nachum, Ola Okelola, Oleg Boiko,
Oleg Murk, Oliver Jaffe, Olivia Watkins, Olivier Godement, Owen Campbell-Moore, Patrick
Chao, Paul McMillan, Pavel Belov, Peng Su, Peter Bak, Peter Bakkum, Peter Deng, Peter Dolan,
Peter Hoeschele, Peter Welinder, Phil Tillet, Philip Pronin, Philippe Tillet, Prafulla Dhariwal,
Qiming Yuan, Rachel Dias, Rachel Lim, Rahul Arora, Rajan Troll, Randall Lin, Rapha Gontijo
Lopes, Raul Puri, Reah Miyara, Reimar Leike, Renaud Gaubert, Reza Zamani, Ricky Wang, Rob
Donnelly, Rob Honsby, Rocky Smith, Rohan Sahai, Rohit Ramchandani, Romain Huet, Rory
Carmichael, Rowan Zellers, Roy Chen, Ruby Chen, Ruslan Nigmatullin, Ryan Cheu, Saachi
Jain, Sam Altman, Sam Schoenholz, Sam Toizer, Samuel Miserendino, Sandhini Agarwal, Sara
Culver, Scott Ethersmith, Scott Gray, Sean Grove, Sean Metzger, Shamez Hermani, Shantanu
Jain, Shengjia Zhao, Sherwin Wu, Shino Jomoto, Shirong Wu, Shuaiqi, Xia, Sonia Phene, Spencer
Papay, Srinivas Narayanan, Steve Coffey, Steve Lee, Stewart Hall, Suchir Balaji, Tal Broda, Tal
Stramer, Tao Xu, Tarun Gogineni, Taya Christianson, Ted Sanders, Tejal Patwardhan, Thomas
Cunninghman, Thomas Degry, Thomas Dimson, Thomas Raoux, Thomas Shadwell, Tianhao
Zheng, Todd Underwood, Todor Markov, Toki Sherbakov, Tom Rubin, Tom Stasi, Tomer Kaftan,
Tristan Heywood, Troy Peterson, Tyce Walters, Tyna Eloundou, Valerie Qi, Veit Moeller, Vinnie
Monaco, Vishal Kuo, Vlad Fomenko, Wayne Chang, Weiyi Zheng, Wenda Zhou, Wesam Manassra,
Will Sheu, Wojciech Zaremba, Yash Patil, Yilei Qian, Yongjik Kim, Youlong Cheng, Yu Zhang,
Yuchen He, Yuchen Zhang, Yujia Jin, Yunxing Dai, and Yury Malkov. Gpt-4o system card, 2024.
URL https://arxiv.org/abs/2410.21276.
Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu. Bleu: a method for automatic
evaluation of machine translation. In Pierre Isabelle, Eugene Charniak, and Dekang Lin, editors,
Proceedings of the 40th Annual Meeting of the Association for Computational Linguistics, pages
311–318, Philadelphia, Pennsylvania, USA, July 2002. Association for Computational Linguistics.
doi: 10.3115/1073083.1073135. URL https://aclanthology.org/P02-1040/.
Edoardo Maria Ponti, Goran Glavaš, Olga Majewska, Qianchu Liu, Ivan Vuli´c, and Anna Korhonen.
XCOPA: A multilingual dataset for causal commonsense reasoning. In Bonnie Webber, Trevor
Cohn, Yulan He, and Yang Liu, editors, Proceedings of the 2020 Conference on Empirical
Methods in Natural Language Processing (EMNLP), pages 2362–2376, Online, November 2020.
Association for Computational Linguistics. doi: 10.18653/v1/2020.emnlp-main.185. URL https:
//aclanthology.org/2020.emnlp-main.185/.
Maja Popovi´c. chrF: character n-gram F-score for automatic MT evaluation. In Ondˇrej Bojar,
Rajan Chatterjee, Christian Federmann, Barry Haddow, Chris Hokamp, Matthias Huck, Varvara
Logacheva, and Pavel Pecina, editors, Proceedings of the Tenth Workshop on Statistical Machine
Translation, pages 392–395, Lisbon, Portugal, September 2015. Association for Computational
Linguistics. doi: 10.18653/v1/W15-3049. URL https://aclanthology.org/W15-3049/.
Jirui Qi, Raquel Fernández, and Arianna Bisazza. Cross-lingual consistency of factual knowledge in
multilingual language models. In Houda Bouamor, Juan Pino, and Kalika Bali, editors, Proceedings
of the 2023 Conference on Empirical Methods in Natural Language Processing, pages 10650–
10666, Singapore, December 2023. Association for Computational Linguistics. doi: 10.18653/v1/
2023.emnlp-main.658. URL https://aclanthology.org/2023.emnlp-main.658/.
Qwen, :, An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan
Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin, Jian Yang, Jianhong Tu, Jianwei Zhang,
Jianxin Yang, Jiaxi Yang, Jingren Zhou, Junyang Lin, Kai Dang, Keming Lu, Keqin Bao, Kexin
Yang, Le Yu, Mei Li, Mingfeng Xue, Pei Zhang, Qin Zhu, Rui Men, Runji Lin, Tianhao Li, Tianyi
Tang, Tingyu Xia, Xingzhang Ren, Xuancheng Ren, Yang Fan, Yang Su, Yichang Zhang, Yu Wan,
Yuqiong Liu, Zeyu Cui, Zhenru Zhang, and Zihan Qiu. Qwen2.5 technical report, 2025. URL
https://arxiv.org/abs/2412.15115.
Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, and Percy Liang. SQuAD: 100,000+ questions for
machine comprehension of text. In Jian Su, Kevin Duh, and Xavier Carreras, editors, Proceedings
of the 2016 Conference on Empirical Methods in Natural Language Processing, pages 2383–2392,
Austin, Texas, November 2016. Association for Computational Linguistics. doi: 10.18653/v1/
D16-1264. URL https://aclanthology.org/D16-1264/.
19

--- Page 20 ---

Angelika Romanou, Negar Foroutan, Anna Sotnikova, Zeming Chen, Sree Harsha Nelaturu, Shiv-
alika Singh, Rishabh Maheshwary, Micol Altomare, Mohamed A. Haggag, Snegha A, Alfonso
Amayuelas, Azril Hafizi Amirudin, Viraat Aryabumi, Danylo Boiko, Michael Chang, Jenny Chim,
Gal Cohen, Aditya Kumar Dalmia, Abraham Diress, Sharad Duwal, Daniil Dzenhaliou, Daniel Fer-
nando Erazo Florez, Fabian Farestam, Joseph Marvin Imperial, Shayekh Bin Islam, Perttu Isotalo,
Maral Jabbarishiviari, Börje F. Karlsson, Eldar Khalilov, Christopher Klamm, Fajri Koto, Dominik
Krzemi´nski, Gabriel Adriano de Melo, Syrielle Montariol, Yiyang Nan, Joel Niklaus, Jekaterina
Novikova, Johan Samir Obando Ceron, Debjit Paul, Esther Ploeger, Jebish Purbey, Swati Rajwal,
Selvan Sunitha Ravi, Sara Rydell, Roshan Santhosh, Drishti Sharma, Marjana Prifti Skenduli,
Arshia Soltani Moakhar, Bardia Soltani Moakhar, Ran Tamir, Ayush Kumar Tarun, Azmine Toushik
Wasi, Thenuka Ovin Weerasinghe, Serhan Yilmaz, Mike Zhang, Imanol Schlag, Marzieh Fadaee,
Sara Hooker, and Antoine Bosselut. INCLUDE: evaluating multilingual language understanding
with regional knowledge, 2024. URL https://doi.org/10.48550/arXiv.2411.19799.
Eduardo Sánchez, Belen Alastruey, Christophe Ropers, Pontus Stenetorp, Mikel Artetxe, and
Marta R. Costa-jussà. Linguini: A benchmark for language-agnostic linguistic reasoning. CoRR,
abs/2409.12126, 2024. doi: 10.48550/ARXIV.2409.12126. URL https://doi.org/10.48550/
arXiv.2409.12126.
Priyanka Sen, Alham Fikri Aji, and Amir Saffari. Mintaka: A complex, natural, and multilingual
dataset for end-to-end question answering. In Nicoletta Calzolari, Chu-Ren Huang, Hansaem
Kim, James Pustejovsky, Leo Wanner, Key-Sun Choi, Pum-Mo Ryu, Hsin-Hsi Chen, Lucia
Donatelli, Heng Ji, Sadao Kurohashi, Patrizia Paggio, Nianwen Xue, Seokhwan Kim, Younggyun
Hahm, Zhong He, Tony Kyungil Lee, Enrico Santus, Francis Bond, and Seung-Hoon Na, editors,
Proceedings of the 29th International Conference on Computational Linguistics, pages 1604–
1619, Gyeongju, Republic of Korea, October 2022. International Committee on Computational
Linguistics. URL https://aclanthology.org/2022.coling-1.138/.
Sheikh Shafayat, H Hasan, Minhajur Mahim, Rifki Putri, James Thorne, and Alice Oh. BEnQA: A
question answering benchmark for Bengali and English. In Lun-Wei Ku, Andre Martins, and Vivek
Srikumar, editors, Findings of the Association for Computational Linguistics: ACL 2024, pages
1158–1177, Bangkok, Thailand, August 2024. Association for Computational Linguistics. doi: 10.
18653/v1/2024.findings-acl.68. URL https://aclanthology.org/2024.findings-acl.68/.
Freda Shi, Mirac Suzgun, Markus Freitag, Xuezhi Wang, Suraj Srivats, Soroush Vosoughi,
Hyung Won Chung, Yi Tay, Sebastian Ruder, Denny Zhou, Dipanjan Das, and Jason Wei. Language
models are multilingual chain-of-thought reasoners. In The Eleventh International Conference on
Learning Representations, ICLR 2023, Kigali, Rwanda, May 1-5, 2023. OpenReview.net, 2023.
URL https://openreview.net/forum?id=fR3wGCk-IXp.
Shivalika Singh, Angelika Romanou, Clémentine Fourrier, David Ifeoluwa Adelani, Jian Gang Ngui,
Daniel Vila-Suero, Peerat Limkonchotiwat, Kelly Marchisio, Wei Qi Leong, Yosephine Susanto,
Raymond Ng, Shayne Longpre, Wei-Yin Ko, Madeline Smith, Antoine Bosselut, Alice Oh, André
F. T. Martins, Leshem Choshen, Daphne Ippolito, Enzo Ferrante, Marzieh Fadaee, Beyza Ermis,
and Sara Hooker. Global MMLU: understanding and addressing cultural and linguistic biases in
multilingual evaluation. CoRR, abs/2412.03304, 2024. doi: 10.48550/ARXIV.2412.03304. URL
https://doi.org/10.48550/arXiv.2412.03304.
Mistral AI team.
Cheaper, better, faster, stronger, 2024.
URL https://mistral.ai/news/
mixtral-8x22b. Accessed: 4-Apr-2025.
Aman Singh Thakur, Kartik Choudhary, Venkat Srinik Ramayapally, Sankaran Vaidyanathan, and
Dieuwke Hupkes. Judging the judges: Evaluating alignment and vulnerabilities in llms-as-judges.
CoRR, abs/2406.12624, 2024. URL https://doi.org/10.48550/arXiv.2406.12624.
Lucas Weber, Elia Bruni, and Dieuwke Hupkes. Mind the instructions: a holistic evaluation of
consistency and interactions in prompt-based learning. In Jing Jiang, David Reitter, and Shumin
Deng, editors, Proceedings of the 27th Conference on Computational Natural Language Learning
(CoNLL), pages 294–313, Singapore, December 2023. Association for Computational Linguistics.
doi: 10.18653/v1/2023.conll-1.20. URL https://aclanthology.org/2023.conll-1.20/.
20

--- Page 21 ---

Weihao Xuan, Rui Yang, Heli Qi, Qingcheng Zeng, Yunze Xiao, Yun Xing, Junjue Wang, Huitao
Li, Xin Li, Kunyu Yu, Nan Liu, Qingyu Chen, Douglas Teodoro, Edison Marrese-Taylor, Shijian
Lu, Yusuke Iwasawa, Yutaka Matsuo, and Irene Li. Mmlu-prox: A multilingual benchmark
for advanced large language model evaluation. CoRR, abs/2503.10497, 2025. URL https:
//doi.org/10.48550/arXiv.2503.10497.
Wenxuan Zhang, Mahani Aljunied, Chang Gao, Yew Ken Chia, and Lidong Bing. M3exam: A
multilingual, multimodal, multilevel benchmark for examining large language models. In Al-
ice Oh, Tristan Naumann, Amir Globerson, Kate Saenko, Moritz Hardt, and Sergey Levine,
editors, Advances in Neural Information Processing Systems 36: Annual Conference on Neu-
ral Information Processing Systems 2023, NeurIPS 2023, New Orleans, LA, USA, Decem-
ber 10 - 16, 2023, 2023.
URL http://papers.nips.cc/paper_files/paper/2023/hash/
117c5c8622b0d539f74f6d1fb082a2e9-Abstract-Datasets_and_Benchmarks.html.
Yuan Zhang, Jason Baldridge, and Luheng He. PAWS: Paraphrase adversaries from word scrambling.
In Jill Burstein, Christy Doran, and Thamar Solorio, editors, Proceedings of the 2019 Conference of
the North American Chapter of the Association for Computational Linguistics: Human Language
Technologies, Volume 1 (Long and Short Papers), pages 1298–1308, Minneapolis, Minnesota,
June 2019. Association for Computational Linguistics. doi: 10.18653/v1/N19-1131. URL https:
//aclanthology.org/N19-1131/.
21

--- Page 22 ---

A
Additional dataset statistics
For reference, we provide a few dataset statistics beyond the main results in the paper.
Arabic
Bengali
Cantonese
Czech
Dutch
English
Farsi
French
German
Hebrew
Hindi
Indonesian
Italian
Japanese
Khmer
Korean
Malay
Mandarin (simp)
Mandarin (trad)
Marathi
Polish
Portuguese
Romanian
Russian
Spanish
Swedish
Tagalog
Thai
Turkish
Urdu
Vietnamese
0
20
40
60
80
100
a name
a word
a number
a place
a date
other
a phrase
a year
a thing
Figure 8: Distribution of output types on the dev split. We show the normalised distribution of
correct output types across languages, ordered (from bottom to top) by average frequency. Rare
output types that occur only a few times are mapped to the category ‘other’.
Output type distribution
In Figure 8, we show the per-language distribution of output types for
MultiLoKo dev split.10 We mapped very rare output types, such as ‘a quantity’, ‘a period of time’
or ‘letter’ to ‘other’, for plotting purposes. We can see that name is the most common output type
across languages, followed by the generic output type a word and number. Also place and date are
relatively common output types, whereas most other output types occur very infrequently or only for
a handful of languages.
0
5
10
15
20
Question length (words)
Arabic
Bengali
Cantonese
Czech
Dutch
English
Farsi
French
German
Hebrew
Hindi
Indonesian
Italian
Japanese
Khmer
Korean
Malay
Marathi
Polish
Portuguese
Romanian
Russian
Mandarin (simp)
Spanish
Swedish
Tagalog
Thai
Mandarin (trad)
Turkish
Urdu
Vietnamese
0.0
0.5
1.0
1.5
2.0
2.5
Answer length (words)
Figure 9: Average question and answer lengths. We show the per-question average length (in
words) of the locally-sourced questions and answers, human-translated into English.
Input and output length
In addition to that, we show the average question – and output lengths of
human-translated the locally sourced questions to English in Figure 9. While there is some variation
in particular in question length, the lengths of the answers are relatively consistent. The average
answer length is around 2, combining one-word answers with (usually) longer names.
10Because the test split is blind, we do not report the distribution of output types here.
22

--- Page 23 ---

B
Instruction following
To facilitate evaluation, we instruct models to answer question with only a number/place/etc. Overall,
we found that base models (with a five-shot template) are much better at abiding by this instruction
than chat models, which exhibit a number of pathologies. While some of those can be caught with
appropriate post-processing (see Appendix C, this is not the case for all issues. Below, we provide a
summary of the main instruction-following issues we encountered with chat models.
False refusals
Sometimes chat models refuse to provide an answer when the question is falsely
perceived to be inappropriate (e.g. when the question asks about someone aged younger than 18).
Producing full sentences
Another issue we observed is that chat models would provide a full
sentence answer, rather than a single word or phrase (e.g. Which year was Francisco Franco born?
Produce a year only. – Francisco Franco was born in 1936). Such full-sentence answers make exact
match rating impossible. The effect is not consistent across languages and happens only for some
of the examples, without any discernable pattern, and therefore difficult to address completely with
post-processing.11
Spurious addition of “answer is”
Likely due to overtraining on MMLU style tasks, Models such
as OpenAI’s GPT4 and Gemini 2.0 preface the vast majority of the answers in English with “answer
is” or “X answer is X“ where X is the desired correct response. This is remarkable, because it is
essentially a repetition of the end of the prompt. However, it is easy to fix in post-processing.
Japanese specific issues
In Japanese, in general it is not polite to answer with incomplete sentences.
As such chat models often append the copula verb ”desu“ to the answer, making exact match
unsuccessful. We are able to fix this in postprocessing.
Claude 3.5 Sonnet issues
We were unable to make Claude 3.5 Sonnet follow the instructions to
produce just an answer in English. It seemed to engage in a long chain-of-thought reasoning style
response which we were unable to reliably parse. This issue only manifests in English and only with
Claude. For this reason, we exclude Claude 3.5 Sonnet from our knowledge transfer results, as it
would make the average lack of knowledge transfer from non-English languages to English more
severe than they are.
C
Post-processing details
We perform the following post-processing for both the reference answers and the answers produced
by the model:
• Remove leading and trailing whitespaces.
• Remove punctuation.
• Lowercase everything.
We perform the following additional post-processing for pretrained models:
• Remove leading “Answer:” or “A:” or the non-English equivalent from the output.
• Remove everything after the first newline.
We perform the following additional post-processing for postrained models:
• Remove leading “answer is:”
• Detect the pattern “X answer is X”, where X is the desired answer, and strip the unnecessary
part in the middle.
• Remove training “desu” in Japanese.
11Using a judge-LLM may to some extent address this problem, but at the expense of other issues (e.g. Thakur
et al., 2024).
23

--- Page 24 ---

D
Annotation instructions
Our annotation pipeline contains five stages: 1) locality rating, 2) question generation 3) question
review, 4) question answering, and 5) translation. Below, we provide the annotation instructions for
each of these stages.
D.1
Locality rating
To narrow-down the initial selection of paragraphs – sampled from the top-rated Wikipedia pages of
the respective locales – the first step in our annotation pipeline is locality rating. Given a paragraph,
we ask annotators to rate whether the paragraph is locally relevant to the particular locale, on a
likertscale from 1 to 5, where 1 refers to extremely local and relatively obscure topics very specifically
related to the specific language or locale and with little international recognition and 5 to globally
well-known topics. We also ask annotators to disregard pages about inappropriate or politically
sensitive topics. The rubric for locality annotation can be found in Table 3. We disregard everything
with a locality rating of 3 or lower.
Description
Example
1.
Extremely local and relatively obscure.
Con-
tent that is of interest only to a small, localized
group, such as a specific town, region, or commu-
nity. These topics are typically obscure and not
widely known beyond their immediate area.
Local radio stations, small town his-
torical events, regional businesses, or
niche local cultural practices.
2.
Regional interest. Topics that have some relevance
beyond a specific locality but are still primarily of
interest within a particular region or country.
State or provincial politicians, regional
cuisine, local sports teams, or medium-
sized companies with regional influ-
ence.
3.
National Significance. Content that is widely rec-
ognized within a single country, but relatively un-
known internationally.
National politicians (not internation-
ally known), popular national media
figures, major corporations within a
country, or significant national histori-
cal events.
4.
International recognition. Topics that are recog-
nized and have relevance in multiple countries but
may not be universally known across the globe.
These topics often have international influence and
are likely to be covered in international media,
though their impact may vary by region.
International brands which may be
recognized in more than one coun-
try, celebrities with some international
reach, significant cultural movements,
or political conflicts with some aware-
ness on the international stage.
5.
Global prominence. Content that is widely rec-
ognized and relevant across a large number of
countries around the world. These topics have a
global impact or appeal and are likely to be well-
represented in media across diverse cultures and
regions.
Globally famous celebrities (e.g., Cris-
tiano Ronaldo), multinational corpo-
rations (e.g., Apple), major world
events, or universally recognized cul-
tural icons.
Table 3: Rubric for locality rating task. In the locality rating task, we ask the annotators to rate
paragraphs with respect to how locally relevant the topic is to the locale.
D.2
Question generation
The second and main annotation step in our pipeline is the step in which we ask annotators to generate
questions about sampled paragraphs. We ask annotators to generate a challenging question with a
short answer. The answer should be easy to evaluate with string-matching metrics, the questions
should not be open-ended or have many possible correct answers, be ambiguous or subjective, and
the expected short answer should be concise. To ensure difficulty, we ask that answering the question
24

--- Page 25 ---

requires combining information from different parts in the accompanying text; It should not be
answerable by mere regurgitation of a single sentence. We furthermore ask that the question is
formulated such that its answer will not change over time (e.g. not ‘How many medals has Sifan
Hassan won’, but ‘How many medals has Sifan Hassan won between 2018 and 2022 (including)’),
and that the question is answerable also without the article (e.g. not ‘How many tv shows did the
person in this article produce?’). To facilitate validation checks in the next round, we also ask that the
question authors write a longer answer to explain how they arrived at the short answer. We also ask
the question authors to annotate what is the type of the correct answer (e.g. number, name, date, etc)
In the pilot, we observed that – for some languages – the vast majority of questions were questions
that required some form of numerical reasoning. Because the intention of the benchmark is to address
knowledge more than reasoning, we afterwards restricted the number of numerical questions to 10%.
Similarly, we asked question authors to avoid yes/no questions.
D.3
Question review
In the first round of question review, we asked annotators from a different provider to judge whether
the questions abide by the rules provided to the question authors. All question reviewers are native
speakers. Specifically, we ask them to check if:
• The question pertains to a locally relevant topic
• The question is clear and undestandable, and not subjective
• The question has a clear and concise answer
• If there are multiple possible variations of the answer possible (e.g. ‘Dick Schoof’ / ‘Minister
Dick Schoof’ / ‘Prime Minister Dick Schoof’ / etc), all versions of the answer are provided.
• The question and answer are in the correct language
• The question is understandable without the article
• That the answer to the question will not likely change in the near future
When a question can be fixed with a minor change (e.g. add a time indication to make sure an answer
will not change in the near future, or add an extra answer version), we ask the question reviewers
to implement this fix and describe it. In the pilot round, we use the annotator feedback to finetune
our annotation protocol and provide feedback to the question-authors. During the rest of the data
collection, we simply disregard questions that are not useable as is or can be corrected with minor
changes.
D.4
Validation through question answering
In the last stage of our question generation pipeline, we have additional annotators answer the sourced
and reviewed question. The goal of this validation task is to confirm that the questions are answerable,
correct, non-ambiguous when read by individuals other than the original question author, and that all
possible versions of the answers are included. For each question, we ask two additional annotators
to first answer the question, using the snippets the questions were sourced from for context. After
they have answered the question, they are shown the list of reference answers written by the original
author of the question as well as the rational they provided, and we ask them to reflect upon the
answer they gave themselves. If their answer did not match any answer in the original reference list,
we ask them to either add their answer to the list if it is semantically equivalent to their own answer
or indicate which answer they believe to be correct, their own or the original answer. We disregard all
questions where at least one annotator disagrees with the original question author.
E
Related work
In this paper, we introduce a new multilingual benchmark for LLMs, that we believe addresses gaps
and pitfalls in existing benchmarks. We (concisely) outlined those gaps and pitfalls and mentioned
several other works related to ours in the introduction of those paper. Here, we discuss multilingual
evaluation of LLMs in more detail. Specifically, we discuss what datasets recent LLM releases have
used for multilingual evaluation (Appendix E.1) and what other datasets and approaches they could
have used but did not (Appendix E.2).
25

--- Page 26 ---

Claude 3.5 Sonnet
MGSM (Shi et al., 2023)
Gemini 2.0 Flash
Mentions multilingual audio, no multilingual benchmarks scores reported.
GPT4-o
ARC-Easy and TruthfulQA translated into five African languages (internal bench-
mark), Uhura-Eval (internal benchmark).
Llama 3.1
MGSM (Shi et al., 2023), Multilingual MMLU (internal benchmark)
Mixtral 8x22B
translated ARC-C, HellaSwag and MMLU (internal benchmarks)
Qwen2.5 72B
M3Exam (Zhang et al., 2023), IndoMMLU (Koto et al., 2023), ruMMLU
(Fenogenova et al., 2024), translated MMLU (Chen et al., 2023), Belebele (Ban-
darkar et al., 2024), XCOPA (Ponti et al., 2020), XWinograd (Muennighoff et al.,
2023), XStoryClose (Lin et al., 2022), PAWS-X (Zhang et al., 2019), MGSM
(Shi et al., 2023), Flores-101 (Goyal et al., 2022)
Table 4: Multilingual evaluation of recent LLM releases, overview. We provide an overview
table of the benchmark for which scores are reported in the release papers or notes of the LLMs we
evaluated in this paper. Models are sorted alphabetically.
E.1
Multilingual evaluation of LLMs in practice
While multilinguality is something frequently mentioned in the release papers or posts of recent LLM
releases, the datasets for which they actual report scores is in most cases quite limited. Of the models
that we evaluated for this paper, Gemini 2.0 Flash reported no multilingual scores at all; GPT4-o
and Mixtral 8x22B report scores only on internally translated but not publicly available English
benchmarks; Claude 3.5 Sonnet reports scores for only one benchmark – MGSM. MGSM is also
the only publicly available benchmark for which Llama 3.1 reports scores, along with – also – an
internally translated version of MMLU that is not publicly available. The only model that extensively
reports multilingual benchmark values, on more than 10 benchmarks, is Qwen2.5 72B. We provide an
overview of the multilingual benchmarks for which scores are reported for these models in Table 4.
E.2
Multilingual evaluation options for LLMs
While, as we discuss below, there are gaps and challenges with multilingual evaluation for LLMs,
there are in fact many more options than is suggested by what is reported in recent releases. Below,
we discuss other options for multilingual LLM evaluation.
Translated English benchmarks
As mentioned earlier on, benchmarks used for LLM evaluation
are often translated English benchmarks. In some cases, the benchmarks were designed to evaluate
only English and translated later, such as translated MMLU (e.g. Li et al., 2024; Chen et al., 2023;
OpenAI, 2025; Singh et al., 2024) or MMLU-ProX (Xuan et al., 2025), MGSM (Shi et al., 2023)
or MLAMA (Kassner et al., 2021). In other cases, the benchmark was multilingual at the time of
its creation, but means of creation of the non-English data was through translating English sourced
data, such as Belebele Bandarkar et al. (2024), Mintaka (Sen et al., 2022), or X-FACTR (Jiang et al.,
2020). Taken together, translated benchmarks span quite a range of tasks, such as question answering
(Artetxe et al., 2020; Lewis et al., 2020; Qi et al., 2023; Ohmer et al., 2023), natural language inference
(Conneau et al., 2018), paraphrase detection (Zhang et al., 2019), general linguistic competence
(Jumelet et al., 2025), reading comprehension (Artetxe et al., 2020; Bandarkar et al., 2024) and
commonsense reasoning (Ponti et al., 2020), and even instruction following (He et al., 2024). With
the exception of question answering and of course instruction following, however, many of these
tasks have gone (somewhat) out of fashion for LLM evaluation, a trend which is mirrored also in
the usage of their multilingual counterparts. As mentioned before, translated benchmarks have the
advantage of containing parallel data, allowing for some form of comparability across languages, but
are English-centric in content and may suffer from translationese (see e.g. Romanou et al., 2024;
Chen et al., 2024, for a recent discussion of this).
Multilingual benchmarks sourced from scratch
Though much rarer, there are also benchmarks
that are created independently for each language they include. Clark et al. (2020) release a question
answering dataset separately sourced for 11 different languages, with a protocol relatively similar
26

--- Page 27 ---

to ours. In a different category, Hardalov et al. (2020), Zhang et al. (2023) and Romanou et al.
(2024) and Sánchez et al. (2024) do not create benchmark data, but instead collect existing exam
or competition questions from official human exams. In case of Zhang et al. (2023), the exams are
graduation exams of primary, middle and high school; Hardalov et al. (2020) includes official state
exams taken by graduating high school students, which may contain parallel pairs in case countries
allow examinations to be taken in multiple languages; Romanou et al. (2024), cover academic exams
at middle and high school and university level, professional certifications and licenses, and exams
to obtain regional licenses. Sánchez et al. (2024) instead focus on questions from the International
Linguistic Olympiad corpus. Lastly, as part of their study Ohmer et al. (2023) create a dataset
called SIMPLE FACTS, containing factual questions created through a shared template filled in with
language specific factual data.
Consistency evaluation
A rather different approach to assess multilinguality in LLMs is to focus
not on accuracy across different languages, but to consider whether predictions are consistent across
languages. This tests knowledge and skill transfer between languages more explicitly. Two recent
examples of studies incorporating consistency-based evaluations on factual knowledge questions
are Qi et al. (2023) and Ohmer et al. (2023). Qi et al. (2023) focusses specifically on sample-level
consistency of answers across different languages, requiring existing parallel benchmarks. Ohmer
et al. (2023), instead, ask models to translate benchmark questions themselves before answering
them again. This can, with some caveats, be applied to any existing monolingual benchmark, but –
requiring multiple steps – it is more involved an a paradigm, and is somewhat bottlenecked by the
translation ability of the model to be evaluated.
Translation as a proxy for multilinguality
Another, more implicit method to assess multilinguality
in LLMs is to evaluate their ability to translate from one language to another. This approach was
famously used by Brown et al. (2020), but has not been common since.
Monolingual non-English evaluation
In our discussion, we have focussed on multilingual eval-
uation options that cover multiple other languages. After all, a benchmark to evaluate models on
Bengali (e.g. Shafayat et al., 2024) or Arabic (e.g. Alwajih et al., 2024) can contribute to multilin-
gual evaluation when combined with other benchmarks, but does not so on its own. Because such
benchmarks are usually created by language experts for the respective languages, they usually target
locally relevant skills and knowledge and are likely of higher quality than benchmarks created for
many languages simultaneously (either through translation or from scratch). Yet, composing a suite
including many languages that allows direct comparisons between languages remains challenging.
We believe such benchmarks can be important for multilingual evaluation in LLMs, but will not
further discuss benchmarks focussing on individual languages or very small sets of languages within
one family here.
27

```
