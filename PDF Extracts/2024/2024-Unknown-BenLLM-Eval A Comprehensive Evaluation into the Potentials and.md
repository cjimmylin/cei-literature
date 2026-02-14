---
title: "2024-Kabir-BenLLM-Eval A Comprehensive Evaluation into the Potentials and - PDF Extract"
source_pdf: "2024-Kabir-BenLLM-Eval A Comprehensive Evaluation into the Potentials and.pdf"
pages: 9
extracted_at: "2026-02-13T09:50:28.946086"
---

# PDF Extract: 2024-Kabir-BenLLM-Eval A Comprehensive Evaluation into the Potentials and

**Source PDF:** 2024-Kabir-BenLLM-Eval A Comprehensive Evaluation into the Potentials and.pdf
**Total Pages:** 9

---

## Content

```
--- Page 1 ---

BenLLM-Eval: A Comprehensive Evaluation into the Potentials and
Pitfalls of Large Language Models on Bengali NLP
Mohsinul Kabir1,*, Mohammed Saidul Islam2,*,†, Md Tahmid Rahman Laskar2,5,†,
Mir Tafseer Nayeem3, M Saiful Bari4, Enamul Hoque2
1Islamic University of Technology, 2York University, 3University of Alberta,
4Nanyang Technological University, 5Dialpad Inc.
mohsinulkabir@iut-dhaka.edu, saidulis@yorku.ca, tahmid20@yorku.ca,
mnayeem@ualberta.ca, bari0001@e.ntu.edu.sg, enamulh@yorku.ca
Abstract
Large Language Models (LLMs) have emerged as one of the most important breakthroughs in NLP for their
impressive skills in language generation and other language-specific tasks. Though LLMs have been evaluated in
various tasks, mostly in English, they have not yet undergone thorough evaluation in under-resourced languages such
as Bengali (Bangla). To this end, this paper introduces BenLLM-Eval, which consists of a comprehensive evaluation
of LLMs to benchmark their performance in the Bengali language that has modest resources. In this regard, we select
various important and diverse Bengali NLP tasks, such as text summarization, question answering, paraphrasing,
natural language inference, transliteration, text classification, and sentiment analysis for zero-shot evaluation of
popular LLMs, namely, GPT-3.5, LLaMA-2-13b-chat, and Claude-2. Our experimental results demonstrate that while
in some Bengali NLP tasks, zero-shot LLMs could achieve performance on par, or even better than current SOTA
fine-tuned models; in most tasks, their performance is quite poor (with the performance of open-source LLMs like
LLaMA-2-13b-chat being significantly bad) in comparison to the current SOTA results. Therefore, it calls for further
efforts to develop a better understanding of LLMs in modest-resourced languages like Bengali.
Keywords: Large Language Models, LLM evaluation, Bengali NLP
1.
Introduction
Since the advent of pre-trained language models
(Devlin et al., 2019; Liu et al., 2019; Rogers et al.,
2020), NLP has witnessed revolutionary advance-
ments over the years. These pre-trained language
models have produced SOTA results on a variety of
NLP tasks with little task-specific fine-tuning. This
leads to the development of various pre-trained
language models specialized in the Bengali lan-
guage, such as BanglaBERT (Bhattacharjee et al.,
2022), BanglaT5 (Bhattacharjee et al., 2023), and
etc. These models have demonstrated exciting
progress in many downstream Bengali NLP tasks
(Ekram et al., 2022; Akash et al., 2023). However,
one major concern for these pre-trained models is
that they require fine-tuning using domain-specific
large annotated datasets, which is challenging for
Bengali due to its under-representation in the NLP
domain (Joshi et al., 2020; Chakraborty et al., 2021;
Chowdhury et al., 2021) despite being the sixth
most spoken language in the world with over 300
million native speakers (Wikipedia, 2023a).
Recent developments in large language models
(LLMs) (Brown et al., 2020; Shoeybi et al., 2019;
Rae et al., 2022; Zhang et al., 2022) have trans-
formed the landscape in NLP. These LLMs, with pa-
rameter sizes exceeding a hundred billion, leverage
*The first two authors contributed equally to this work.
†Corresponding Authors.
the in-context learning capability to achieve impres-
sive performance in few-shot and zero-shot learn-
ing scenarios without the need for task-specific fine-
tuning. This capability makes it possible to reduce
the need for the annotation of huge datasets, allow-
ing the model to perform well on tasks that it was
not trained on.
Despite the impressive capabilities of LLMs, they
may still frequently generate untruthful facts that
diverge from the original input (Ouyang et al., 2022).
To address this issue, the Reinforcement Learning
from Human Feedback (RLHF) mechanism has
been utilized to help LLMs generate honest and
harmless responses. ChatGPT and other recently
proposed LLMs like PaLM-2, Claude-2, LLaMA-2-
chat (Touvron et al., 2023; Anil et al., 2023; Jahan
et al., 2024) are trained via leveraging this RLHF
technique to mitigate various limitations of the previ-
ous generation LLMs and gained widespread pop-
ularity. While these LLMs are trained in multiple
languages, English possesses the majority of the
training data.
Though ChatGPT like LLMs has
demonstrated strong zero-shot performance in var-
ious NLP tasks in English (Laskar et al., 2023a,b)
and some other languages (Lai et al., 2023) and
domains (Jahan et al., 2023, 2024; Fu et al., 2024),
these LLMs are yet to be investigated in the widely
spoken, yet modest-resourced, Bengali language
domain.
In this regard, we aim to assess the efficacy of
arXiv:2309.13173v2  [cs.CL]  19 Mar 2024

--- Page 2 ---

LLMs in prevalent downstream NLP tasks specific
to the Bengali language, a domain that has not
been thoroughly examined compared to the numer-
ous LLM evaluations conducted for English and
other Indo-European languages. Due to the lack of
task-specific annotated datasets in Bengali, we con-
ducted a zero-shot evaluation with LLMs to investi-
gate if LLMs could be utilized to address the scarcity
of large annotated datasets in Bengali. Thus, the
findings from this paper would give insights into
the capabilities and limitations of LLMs in Bengali,
which may pave the way to implement LLMs in
real-world applications like Bengali Chatbots. To
this end, we present BenLLM-Eval - a comprehen-
sive benchmark that evaluates the zero-shot per-
formance of various LLMs on diverse NLP tasks
in the Bengali language, including text summariza-
tion, question answering, paraphrasing, natural lan-
guage inference, transliteration, text classification,
and sentiment analysis. The evaluation incorpo-
rates carefully crafted prompts to ensure rigorous
assessment of the following three popular LLMs:
GPT-3.5, LLaMA-2-13b-chat, and Claude-2, and
compare them with SOTA fine-tuned models. To
the best of our knowledge, this is the first work that
evaluates LLMs in the Bengali language. Our ex-
perimental results in this paper are summarized as
follows:
• Despite some exceptional cases, the zero-
shot performance of LLMs is generally infe-
rior compared to the SOTA fine-tuned models
across the majority of the tasks in our evalu-
ation. Given the substantial performance dis-
parities observed, it is reasonable to deduce
that LLMs, in their current form, are not suit-
able for serving as a comprehensive solution
for modest-resourced tasks in Bengali1.
• Considering LLMs remarkable performance
in zero-shot scenarios within the English lan-
guage and its subpar performance in modest-
resource languages like Bengali, this paper
emphasizes the significance of investigating
the limitations of LLMs tailored to diverse
modest-resource language groups.
2.
Methodology
The objective of our study is to assess the efficacy
of LLMs in the context of NLP tasks specific to the
Bengali language. We cover 7 diverse and impor-
tant Bengali NLP tasks: (i) Text Summarization, (ii)
Question Answering (QA), (iii) Paraphrasing, (iv)
1We
share
the
LLM-generated
responses,
prompts,
and parsing scripts for all seven tasks
here: https://github.com/saidul-islam98/BenLLMeval
Natural Language Inference (NLI), (v) Translitera-
tion, (vi) Text Classification, and (vii) Sentiment
Analysis over 8 benchmark datasets. For this pur-
pose, we evaluate ChatGPT (GPT-3.52), Claude-23,
and LLaMA-2-13b-Chat (Touvron et al., 2023) mod-
els. Similar to the prior work on LLM evaluation
(Laskar et al., 2023a; Jahan et al., 2023), we also
focus on designing a zero-shot learning setting to
benchmark the performance of the LLMs.
We prepare a task instruction T for a given test
sample X and concatenate the text in the test sam-
ple with the task instruction to construct the prompt
P. The prompt P is then passed as input to the
LLMs, which generates the response R. A com-
prehensive description of the tasks, datasets, and
prompts devised for evaluating each specific task
is presented below and also summarized in Table
1. Next, we briefly discuss each task.
Text Summarization: Summarization is the pro-
cess of automatically generating a concise and
coherent summary of a longer text document (Nay-
eem and Chali, 2017a,b; Laskar et al., 2022), pre-
serving the most important information while re-
ducing the length (Nayeem et al., 2018). In this
paper, we evaluate the XL-Sum dataset (Hasan
et al., 2021) that consists of 1 million manually an-
notated data samples from 44 languages. We only
took the Bengali samples for evaluation.
Question
Answering:
For
the
question-
answering task, we evaluate the performance of
LLMs on the SQuAD_Bangla dataset (Bhattachar-
jee et al., 2022). This dataset was constituted us-
ing two benchmark English datasets: SQuAD 2.0
(Williams et al., 2018) and TyDi QA (Clark et al.,
2020). The objective of this task is to determine
whether the answer to a given question Q can be
inferred from the reference context C. We provide
the reference context along with the question and
ask LLMs whether they can infer the answer to the
question from the given reference.
Paraphrasing: The paraphrasing task aims to
generate a paraphrase of the input text. To evalu-
ate this task, we choose the Bengali samples from
the IndicParaphrase dataset (Kumar et al., 2022),
which is the largest Indic paraphrasing dataset
across 11 Indic languages (Wikipedia, 2023b).
Natural Language Inference:
Natural Lan-
guage Inference (NLI) aims to predict the entail-
ment/contradiction relations between two input sen-
tences: a premise and a hypothesis. To evaluate
LLMs for Bengali NLI, we utilize the BNLI dataset
(Bhattacharjee et al., 2022) (curated from the
benchmark XNLI dataset (Conneau et al., 2018))
that provides annotated data with three categories:
Entailment, Contradiction, and Neutral.
Transliteration: Transliteration is the process of
2https://platform.openai.com/docs/models/gpt-3-5
3https://www.anthropic.com/index/claude-2

--- Page 3 ---

Dataset
Type
Data Split (Train / Valid / Test)
Prompt
XL-Sum (Hasan et al., 2021)
Text Summarization
8102 / 1012 / 1012
Please provide an one-sentence summary of the following Bangla text input. The input will
be a long Bangla paragraph, the output should be a short Bangla paragraph summarizing
only the vital information of the input text in one sentence. Please make sure that the output
contains the most essential statistical data. Note: Please do not provide anything other than
the summarized Bangla output.
[INPUT:]
SQuAD_Bangla
(Bhattacharjee
et al., 2022)
Question-Answering
118k / 2.5k / 2.5k
Please provide an answer to the input Bangla question based on the given Bangla context.
The input will contain a Bangla question followed by a context. The output should be the
answer in Bangla based on the context. Note: Please do not provide anything other than the
Bangla answer to the question.
[CONTEXT:]
[QUESTION:]
IndicParaphrase
(Kumar
et
al.,
2022)
Paraphrasing
890k / 10k / 10k
Please provide paraphrasing of the following input Bangla text. The input will be a complex
Bangla sentence, the output should be a paraphrased Bangla sentence maintaining the
original information of the input text unchanged. Note: Please do not provide anything except
the paraphrased Bangla output.
[INPUT:]
BNLI (Bhattacharjee et al., 2022)
Natural Language
Inference (NLI)
381k / 2.42k / 4.9k
Please determine the logical relationship between the given hypothesis and premise. The input
will consist of two sentences written in the Bangla language. The first sentence represents
the premise, while the second sentence represents the hypothesis. Your task is to determine
whether the hypothesis is false (contradiction), true (entailment), or inconclusive (neutral)
given the premise. Please output a number indicating the logical relationship between them:
0 for false (contradiction), 1 for true (entailment), and 2 for inconclusive (neutral) for neutrality.
Note: Please avoid providing any additional information beyond the logical relationship.
[PREMISE:]
[HYPOTHESIS:]
Dakshina (Roark et al., 2020)
Transliteration
(single-word: lexicon)
- / - / 9.2k
Task Description: Please provide the transliteration in native Bengali script for the input word.
The input will be a word written in Latin script and the output should be the transliterated
Bengali word of the given input. Please note that you are not asked to provide translation of
the input word, only provide the Bengali transliteration for the given input.
Note: Your response should include only the transliterated word in the native Bengali language.
Please do not add any explanation with the output.
[INPUT:]
Dakshina (Roark et al., 2020)
Transliteration
(full sentence)
25k / 5k / 5k
Task Description: Please provide the transliteration in native Bengali script for the input
sentence. The input will be a sentence written in Latin script and the output should be the
transliterated Bengali sentence of the given input. Please do not provide the translation of
the input sentence, only provide the Bengali transliteration for the given input.
Note: Your response should include only the transliterated sentence in the native Bengali
language. Please do not add any explanation with the output.
[INPUT:]
Soham News Article Classification
(Kakwani et al., 2020)
Text Classification
11284 / 1411 / 1411
For the Bengali news article given in the input, identify the appropriate section title for the
article from the following classes: kolkata, state, sports, national, entertainment, international.
Note: Do not output any unnecessary words other than just the section title. The response
should be in English language and should be one word.
[INPUT:]
IndicSentiment (Doddapaneni et al.,
2022)
Sentiment Analysis
- / 156 / 1000
For the given Input, is the sentiment in the input positive or negative? Note: Please do not
output anything other than the sentiment. Exclude any word like, Sentiment in the response.
[INPUT:]
SentNoB (Islam et al., 2021)
Sentiment Analysis
12575 / 1567 / 1586
For the given Input, is the sentiment in the input positive or negative or neutral? Note: Please
do not output anything other than the sentiment. Exclude any word like, Sentiment in the
response.
[INPUT:]
Table 1: Datasets Details with our Prompts for Various Tasks.
converting texts from one script to another based on
phonetic similarity. We utilize the Dakshina dataset
(Roark et al., 2020) to evaluate transliteration er-
rors. Errors can be (i) Substitutions, (ii) Insertions,
or (iii) Deletions. A substitution error occurs when
the predicted transliteration differs from the refer-
ence transliteration. An insertion error happens
when extra characters/words are present in the pre-
dicted transliteration. A deletion error occurs when
characters/words are missing from the predicted
transliteration. The error rate is calculated as:
error rate = substitutions + deletions + insertions
total reference tokens
∗100
Two types of error rates are proposed for this
task in Dakshina dataset (Roark et al., 2020): the
Character-Error Rate (CER) treats each token as
an individual Unicode character, while the Word-
Error Rate (WER) treats each token as a substring
separated by whitespace. We report both CER and
WER for single-word transliteration, and WER for
full-sentence transliteration.
Text Classification: This task refers to the clas-
sification of the category for a given input text. To
evaluate the text classification capability of LLMs,
we use the Soham Bengali News Classification
dataset that is included in the IndicGLUE (Kakwani
et al., 2020) benchmark. This dataset contains
six news categories i.e., kolkata, state, national,
international, sports, and entertainment.
Sentiment Analysis: We evaluate the Sen-
timent Analysis capability of the LLMs with two
datasets: SentNoB (Islam et al., 2021), and Indic-
Sentiment (Doddapaneni et al., 2022). The Sent-
NoB dataset comprises texts that are informally
written in Bengali, collected from public comments
on news and videos in social media covering a wide
range of domains like, politics, agriculture, educa-
tion etc. The second dataset, IndicSentiment, was
manually curated for the IndicXTREME benchmark
and contains product reviews of multiple categories.
We only used the Bengali samples from the dataset
out of the 12 Indic languages.
3.
Results and Discussion
We report the performance of LLMs for different
tasks and compare their performance with the cur-
rent SOTA fine-tuned models (see Table 2).
Text Summarization Evaluation: In the XL-Sum
dataset, we find that none of the LLMs could out-
perform the current SOTA mT5 model. Among
the LLMs, Claude-2 performs the best in terms
of ROUGE-1 and ROUGE-L, while GPT-3.5 per-
forms the best in terms of ROUGE-2. We also find
that GPT-3.5 tends to generate much longer sum-

--- Page 4 ---

XL-Sum (TS)
SQuAD_Bangla (QA)
IndicPara (PP)
BNLI (NLI)
SNAC (TC)
IndicSent (SA)
SentNoB (SA)
Model
R-1
R-2
R-L
EM / F1
BLEU
Acc.
Acc.
Acc.
P
R
F1
GPT-3.5
20.19
5.81
15.53
44.85/78.67
2.81
52.71
48.47
90.20
57.70
54.56
53.17
LLaMA-2-13b-chat
0.41
0.14
0.34
31.73/67.95
0.01
42.37
29.27
69.16
48.39
48.49
48.43
Claude-2
20.79
5.55
16.47
49.92/79.04
1.89
32.20
48.61
88.48
53.28
54.38
52.79
mT5 (Hasan et al., 2021)
28.32
11.43
24.23
4.45
-
-
-
-
-
-
BanglaBERT (Bhattacharjee et al., 2022)
-
-
-
72.63/79.34
-
82.8
-
-
-
-
-
BanglishBERT (Bhattacharjee et al., 2022)
-
-
-
72.43/78.40
-
80.95
-
-
-
-
-
XLM-R (Large) (Bhattacharjee et al., 2022)
-
-
-
73.15/79.06
-
82.4
-
-
-
-
-
XLM-R (Kakwani et al., 2020; Doddapaneni et al., 2022)
-
-
-
-
-
87.60
85.8
-
-
-
IndicBART (Kumar et al., 2022)
-
-
-
11.57
-
-
-
-
-
-
IndicBERT (Kakwani et al., 2020; Doddapaneni et al., 2022)
-
-
-
-
-
78.45
89.3
-
-
-
mBERT (Kakwani et al., 2020; Doddapaneni et al., 2022)
-
-
-
-
-
80.23
72.0
49.58
56.43
52.79
Bi-LSTM + Attn. (w/ FastText) (Islam et al., 2021)
-
-
-
-
-
-
-
52.24
63.09
57.15
Bi-LSTM + Attn. (w/ Rand init) (Islam et al., 2021)
-
-
-
-
-
-
-
56.16
64.97
60.25
Table 2: Performance Comparison between zero-shot LLMs & fine-tuned SOTA models on Text Summarization
(TS), Question Answering (QA), Paraphrasing (PP), Natural Language Inference (NLI), Text Classification (TC), and
Sentiment Analysis (SA). EM, Acc., P, R, and F1 denote Exact Match, Accuracy, Precision, Recall, and F1 score
respectively. Best results are boldfaced.
Task
Pair 6-gram
LSTM
Transformer
Noisy Channel
GPT-3.5
LLaMA-2-13b
Claude 2
CER (↓)
WER (↓)
CER (↓)
WER (↓)
CER (↓)
WER (↓)
WER (↓)
CER (↓)
WER (↓)
CER (↓)
WER (↓)
CER (↓)
WER (↓)
Lexicon
14.2
54.0
13.9
54.7
13.2
50.6
-
18.1
60.6
39.85
80.72
23.16
68.07
Sentence
-
39.7
-
-
-
37.6
25.8
-
29.9
-
66.54
-
38.10
Table 3: Single-word and Full-sentence Transliteration results. Here, the baseline results are adopted from Roark
et al. (2020). Best results are boldfaced and lower (↓) is better.
maries (229 words on average) than the gold ref-
erence summaries (148 words on average), while
the length of the Claude-2 generated summaries
(137 words on average) is more consistent with
the gold reference summaries (148 words on av-
erage). Moreover, to find out why LLaMA-2-13b-
chat achieves very low ROUGE scores, we man-
ually reviewed the responses and found out that
it ended up generating all the summaries in En-
glish. By translating the summaries to Bengali us-
ing Google’s Translation API (Google, 2020), the
R-1, 2, and L scores are increased to 4.69, 0.61,
and 3.61, respectively, for LLaMA-2-13b-chat.
Question Answering Evaluation: Since LLMs
frequently generate responses that may not be an
exact match of the gold label but are nonetheless
correct, our QA evaluation utilizes human interven-
tion to compute the F1 score. We find that Claude-2
and GPT-3.5 achieve performance almost similar
to the current SOTA results in terms of F1. How-
ever, the performance of all LLMs is quite poor in
terms of Exact Match due to generating descriptive
responses, as well as paraphrases.
Paraphrasing Evaluation: For the paraphras-
ing task, we observe a very low BLEU score for
all LLMs, which is a phenomenon similar to what
happened with the EM metric for the QA task. Note
that the BLEU score also computes word-level simi-
larity, while such limitations of word-based similarity
metrics have also been noticed LLMs are evaluated
in English datasets (Laskar et al., 2023a).
Natural Language Inference Evaluation: We
observe that while GPT-3.5 achieves the best re-
sults among all LLMs on the BNLI dataset, it is
still much lower in comparison to the current SOTA
BanglaBERT. Surprisingly, we find that Claude-2
is the worst performer in this task while being out-
performed by the much smaller LLaMA-2-13b-chat
model. To further investigate in which cases LLMs
perform poorly in the NLI task, we demonstrate
their predictions using the Confusion Matrix in Fig-
ure 1 and find that LLaMA-2-13b-chat was quite
bad while predicting the Neutral types and Claude-
2 performed poorly while predicting the Entailment
types. In the case of GPT-3.5, it performed poorer
while predicting the Neutral type class in compari-
son to the other types.
Transliteration Evaluation: From Table 3, we
find that GPT-3.5 achieves superior performance
over other LLMs in single-word transliteration.
While it fails to outperform the existing results, it still
achieves competitive performance compared to the
prior SOTA models. This is an interesting obser-
vation given the intricate structure and infrequent
usage of lexicons in the test set. In full-sentence
transliteration, GPT-3.5 makes fewer word errors
and character errors (60.6% & 18.1%) compared
to other LLMs ((80.72% & 39.85%) for Llama-2-
13b-chat and (68.07% & 23.16%) for Claude-2).
However, the results are quite poor compared to
other SOTA models.
Text Classification Evaluation:
LLMs per-
formed poorly on the Soham News Article classifi-
cation dataset, with the best-performing LLM in this
dataset, the Claude-2 model achieving only 48.61%
accuracy, followed by GPT-3.5 achieving 48.47%
accuracy while the LLaMA-2-13b-chat being the
worst performer with an accuracy of 29.27%. On
the contrary, the XLM-R model, which is the SOTA
for this task, obtained an accuracy of 87.60% in this
dataset. While we achieved these results by pro-
viding the class labels alongside our prompts (see
Table 1), if the class labels were not mentioned, the
accuracy dropped to 20.76%, 18.36%, and 1.06%
for Claude-2, GPT-3.5, and LLaMA-2-13b-chat, re-
spectively. This indicates the importance of using
descriptive prompts to improve the zero-shot per-
formance of LLMs.

--- Page 5 ---

(a) GPT-3.5
(b) Llama-2-13b-chat
(c) Claude-2
Figure 1: Confusion matrices for different LLMs on the BNLI dataset for the NLI task.
Sentiment Analysis Evaluation: In the senti-
ment classification task, we observe that GPT-3.5
performed exceptionally well on the IndicSentiment
dataset (Doddapaneni et al., 2022), attaining a new
SOTA accuracy of 90.20% While we also find that
the Claude-2 model achieved impressive perfor-
mance (88.48% accuracy), the LLaMA-2-13b-chat
model performed much poorer. We also find a sim-
ilar trend for sentiment analysis in the SentNoB (Is-
lam et al., 2021) dataset. In this dataset, to ensure
a fair comparison with the current SOTA, we use
the precision, recall, and F1 scores as evaluation
metrics. While none of the LLMs could outperform
the current SOTA, all of them (especially GPT-3.5
and Claude-2) achieved performance comparable
to the SOTA results. This is consistent with LLMs’
performance for this task in English (Laskar et al.,
2023a).
4.
Task Contamination Analysis
Task contamination analysis (Li and Flanigan,
2023) is essential to ensure a fair model evaluation
since it helps identify a model’s prior exposure to
test tasks on its training data. Inspired by the work
of Li and Flanigan (2023), we include task contam-
ination analysis in our evaluation to appropriately
assess the performance of the LLMs. We utilize
two methods: Task Example Extraction (TEE) and
Membership Inference (for generative tasks like
summarization and paraphrasing) to verify the ev-
idence of task contamination. TEE involves re-
trieving task examples from instruction-tuned mod-
els, although it doesn’t require an exact match with
existing training data, helps identify potential task
contamination in zero and few-shot learning scenar-
ios, as any task examples found indicate possible
prior exposure. Additionally, Membership Infer-
ence is a method used for generation tasks, where
the model’s generated content is checked against
the original dataset for exact matches. If a match
is found, it implies that the content was part of
the LLM’s training data, indicating direct exposure
rather than general learning ability.
At first, we applied TEE to all tasks without ex-
plicitly mentioning the dataset name. Our findings
reveal that only GPT-3.5 could generate examples
related to these tasks (except Natural Language
Inference), while Claude-2 and LLaMA-2-13b-chat
models failed to extract task examples for any tasks.
Therefore, there is a possibility that such tasks were
already included in the pre-training data of GPT-
3.5. Regarding the BNLI dataset where no models
could extract any task examples, we find that the
premises, hypotheses, and labels generated by all
LLMs for Bengali were significantly inaccurate, pro-
viding evidence that contamination did not occur. In
terms of extracting task examples in the translitera-
tion task, we find that among LLMs, only GPT-3.5
could extract the task examples for both word-level
and sentence-level transliteration.
Finally, we applied the Membership Inference
technique in the generative tasks (e.g., summariza-
tion and paraphrase generation) to analyze task
contamination. In the summarization task, none
of the LLMs produced an output that aligned with
the test data labels. However, on the paraphras-
ing task, GPT-3.5 produced around 50 exact match
instances, while Claude-2 produced 30 and LLaMA-
2-13b-chat produced 15 exact matches of the gen-
erated outputs and test labels. So it is possible that
the test set of the IndicPara dataset was exposed
to the LLMs while training.
In summary, contamination could be an issue
with the GPT-3.5 model in Sentiment Analysis, Text
Classification, Summarization, and QA tasks, while
all the models, i.e., GPT-3.5, LLaMA-2-13b-chat,
and Claude-2 were affected by task contamination
in the Paraphrasing task. However, in Natural Lan-
guage Inference, we did not see any evidence of
task contamination.

--- Page 6 ---

5.
Conclusions and Future Work
In this paper, we introduce BenLLM-Eval, which
provides a comprehensive zero-shot evaluation
of LLMs on seven benchmark NLP tasks to un-
derstand the capability of LLMs in the modest-
resourced Bengali language. The results revealed
that while in some tasks, zero-shot closed-source
LLMs like GPT-3.5 or Claude-2 perform on par (e.g.,
summarization) or even outperform (e.g., sentiment
analysis) current SOTA models, in most tasks the
LLMs exhibited considerably lower performance
compared to supervised fine-tuned models. We
also observed that the open-source LLaMA-2-13b-
chat model performed significantly poorer in most
tasks. Thus, open-source LLMs should be exten-
sively evaluated on low to modest-resource lan-
guages to ensure a proper understanding of their
capabilities and limitations. Our findings also re-
veal that in order to achieve optimal performance
across languages, LLMs should also be trained
on corpus covering various languages along with
English. In the future, we intend to expand our
experiments by including additional low to modest-
resource languages, tasks, datasets, and settings
to obtain broader insights.
Limitations
The datasets used to train LLMs like GPT-3.5 or
Claude-2 are not disclosed; consequently, some
datasets used to evaluate the model may or may
not have existed during model training. In addition,
the API used to evaluate the GPT-3.5 model is
based on OpenAI’s GPT-3.5 turbo. Although an
improved version GPT-4 is also available, GPT-4 is
significantly more expensive than GPT-3.5. Thus,
we could not use GPT-4 in this work. Other than
these limitations, this study will provide a practical
direction for future research into the performance of
LLMs in modest-resourced languages in the NLP
domain.
Ethics Statement
This study assesses the performance of LLMs in
seven benchmark NLP tasks in the Bengali lan-
guage wherein LLMs are tasked with generating
an output based on the information given in the
input. Therefore, no prompt or information was
presented to LLMs that could result in the gener-
ation of any output raising any ethical issues or
unwanted biases. There will be no licensing issue
as all the datasets that are utilized in this research
are publicly available.
Acknowledgements
This research is supported by the Generic (Mi-
nor/Startup/Other) research funds of York Univer-
sity. We also thank Anthropic for providing free
access to the Claude-2 model, the Canada Foun-
dation for Innovation grant and Compute Canada
for its computing resources. Mir Tafseer Nayeem
is also supported by the Huawei PhD Fellowship.
Abu
Ubaida
Akash,
Mir
Tafseer
Nayeem,
Faisal Tareque Shohan, and Tanvir Islam. 2023.
Shironaam: Bengali news headline generation
using auxiliary information. In Proceedings of
the 17th Conference of the European Chapter of
the Association for Computational Linguistics,
pages 52–67, Dubrovnik, Croatia. Association
for Computational Linguistics.
Rohan Anil, Andrew M Dai, Orhan Firat, Melvin
Johnson, Dmitry Lepikhin, Alexandre Passos,
Siamak Shakeri, Emanuel Taropa, Paige Bai-
ley, Zhifeng Chen, et al. 2023. Palm 2 technical
report. arXiv preprint arXiv:2305.10403.
Abhik Bhattacharjee, Tahmid Hasan, Wasi Ahmad,
Kazi Samin Mubasshir, Md Saiful Islam, Anindya
Iqbal, M. Sohel Rahman, and Rifat Shahriyar.
2022. BanglaBERT: Language model pretrain-
ing and benchmarks for low-resource language
understanding evaluation in Bangla. In Findings
of the Association for Computational Linguistics:
NAACL 2022, pages 1318–1327, Seattle, United
States. Association for Computational Linguis-
tics.
Abhik Bhattacharjee, Tahmid Hasan, Wasi Uddin
Ahmad, and Rifat Shahriyar. 2023. BanglaNLG
and BanglaT5: Benchmarks and resources for
evaluating low-resource natural language gen-
eration in Bangla. In Findings of the Associa-
tion for Computational Linguistics: EACL 2023,
pages 726–735, Dubrovnik, Croatia. Association
for Computational Linguistics.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared D Kaplan, Prafulla Dhariwal,
Arvind Neelakantan, Pranav Shyam, Girish Sas-
try, Amanda Askell, Sandhini Agarwal, Ariel
Herbert-Voss, Gretchen Krueger, Tom Henighan,
Rewon Child, Aditya Ramesh, Daniel Ziegler, Jef-
frey Wu, Clemens Winter, Chris Hesse, Mark
Chen, Eric Sigler, Mateusz Litwin, Scott Gray,
Benjamin Chess, Jack Clark, Christopher Berner,
Sam McCandlish, Alec Radford, Ilya Sutskever,
and Dario Amodei. 2020. Language models are

--- Page 7 ---

few-shot learners. In Advances in Neural Infor-
mation Processing Systems, volume 33, pages
1877–1901. Curran Associates, Inc.
Susmoy Chakraborty, Mir Tafseer Nayeem, and
Wasi Uddin Ahmad. 2021. Simple or complex?
learning to predict readability of bengali texts.
Proceedings of the AAAI Conference on Artificial
Intelligence, 35(14):12621–12629.
Radia Rayan Chowdhury, Mir Tafseer Nayeem,
Tahsin Tasnim Mim, Md. Saifur Rahman Chowd-
hury, and Taufiqul Jannat. 2021. Unsupervised
abstractive summarization of Bengali text docu-
ments. In Proceedings of the 16th Conference
of the European Chapter of the Association for
Computational Linguistics: Main Volume, pages
2612–2619, Online. Association for Computa-
tional Linguistics.
Jonathan H. Clark, Eunsol Choi, Michael Collins,
Dan Garrette, Tom Kwiatkowski, Vitaly Niko-
laev, and Jennimaria Palomaki. 2020. TyDi QA:
A benchmark for information-seeking question
answering in typologically diverse languages.
Transactions of the Association for Computa-
tional Linguistics, 8:454–470.
Alexis Conneau, Ruty Rinott, Guillaume Lam-
ple, Adina Williams, Samuel Bowman, Holger
Schwenk, and Veselin Stoyanov. 2018. XNLI:
Evaluating cross-lingual sentence representa-
tions. In Proceedings of the 2018 Conference
on Empirical Methods in Natural Language Pro-
cessing, pages 2475–2485, Brussels, Belgium.
Association for Computational Linguistics.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. BERT: Pre-training
of deep bidirectional transformers for language
understanding. In Proceedings of the 2019 Con-
ference of the North American Chapter of the As-
sociation for Computational Linguistics: Human
Language Technologies, Volume 1 (Long and
Short Papers), pages 4171–4186, Minneapolis,
Minnesota. Association for Computational Lin-
guistics.
Sumanth Doddapaneni, Rahul Aralikatte, Gowtham
Ramesh, Shreya Goyal, Mitesh M. Khapra,
Anoop Kunchukuttan, and Pratyush Kumar. 2022.
Indicxtreme: A multi-task benchmark for evaluat-
ing indic languages.
Syed Mohammed Sartaj Ekram, Adham Arik Rah-
man, Md. Sajid Altaf, Mohammed Saidul Islam,
Mehrab Mustafy Rahman, Md Mezbaur Rahman,
Md Azam Hossain, and Abu Raihan Mostofa Ka-
mal. 2022. BanglaRQA: A benchmark dataset
for under-resourced Bangla language reading
comprehension-based question answering with
diverse question-answer types. In Findings of
the Association for Computational Linguistics:
EMNLP 2022, pages 2518–2532, Abu Dhabi,
United Arab Emirates. Association for Computa-
tional Linguistics.
Xue-Yong Fu, Md Tahmid Rahman Laskar, Elena
Khasanova, Cheng Chen, and Shashi Bhushan
TN. 2024. Tiny titans: Can smaller large lan-
guage models punch above their weight in the
real world for meeting summarization?
arXiv
preprint arXiv:2402.00841.
Google. 2020. Googletrans: Free and unlimited
google translate api for python. Accessed: March
12, 2024.
Tahmid Hasan, Abhik Bhattacharjee, Md. Saiful
Islam, Kazi Mubasshir, Yuan-Fang Li, Yong-Bin
Kang, M. Sohel Rahman, and Rifat Shahriyar.
2021. XL-sum: Large-scale multilingual abstrac-
tive summarization for 44 languages. In Findings
of the Association for Computational Linguistics:
ACL-IJCNLP 2021, pages 4693–4703, Online.
Association for Computational Linguistics.
Khondoker Ittehadul Islam, Sudipta Kar, Md Saiful
Islam, and Mohammad Ruhul Amin. 2021. Sent-
NoB: A dataset for analysing sentiment on noisy
Bangla texts. In Findings of the Association for
Computational Linguistics: EMNLP 2021, pages
3265–3271, Punta Cana, Dominican Republic.
Association for Computational Linguistics.
Israt Jahan, Md Tahmid Rahman Laskar, Chun
Peng, and Jimmy Huang. 2023. Evaluation of
ChatGPT on biomedical tasks: A zero-shot com-
parison with fine-tuned generative transformers.
In The 22nd Workshop on Biomedical Natural
Language Processing and BioNLP Shared Tasks,
pages 326–336, Toronto, Canada. Association
for Computational Linguistics.
Israt Jahan, Md Tahmid Rahman Laskar, Chun
Peng, and Jimmy Xiangji Huang. 2024. A com-
prehensive evaluation of large language mod-
els on benchmark biomedical text processing
tasks. Computers in Biology and Medicine, page
108189.
Pratik Joshi, Sebastin Santy, Amar Budhiraja, Ka-
lika Bali, and Monojit Choudhury. 2020. The state
and fate of linguistic diversity and inclusion in the
NLP world. In Proceedings of the 58th Annual
Meeting of the Association for Computational Lin-
guistics, pages 6282–6293, Online. Association
for Computational Linguistics.
Divyanshu Kakwani, Anoop Kunchukuttan, Satish
Golla, Gokul N.C., Avik Bhattacharyya, Mitesh M.

--- Page 8 ---

Khapra, and Pratyush Kumar. 2020. IndicNLP-
Suite: Monolingual corpora, evaluation bench-
marks and pre-trained multilingual language
models for Indian languages.
In Findings of
the Association for Computational Linguistics:
EMNLP 2020, pages 4948–4961, Online. Asso-
ciation for Computational Linguistics.
Aman Kumar, Himani Shrotriya, Prachi Rani Sahu,
Raj Dabre, Ratish Puduppully, Anoop Kunchukut-
tan, Amogh Mishra, Mitesh M. Khapra, and
Pratyush Kumar. 2022. Indicnlg benchmark: Mul-
tilingual datasets for diverse nlg tasks in indic
languages. In Conference on Empirical Methods
in Natural Language Processing.
Viet Dac Lai, Nghia Trung Ngo, Amir Pouran Ben
Veyseh, Hieu Man, Franck Dernoncourt, Trung
Bui, and Thien Huu Nguyen. 2023. Chatgpt be-
yond english: Towards a comprehensive eval-
uation of large language models in multilingual
learning.
Md Tahmid Rahman Laskar, M Saiful Bari, Miza-
nur Rahman, Md Amran Hossen Bhuiyan, Shafiq
Joty, and Jimmy Huang. 2023a. A systematic
study and comprehensive evaluation of ChatGPT
on benchmark datasets. In Findings of the Asso-
ciation for Computational Linguistics: ACL 2023,
pages 431–469, Toronto, Canada. Association
for Computational Linguistics.
Md Tahmid Rahman Laskar, Xue-Yong Fu, Cheng
Chen, and Shashi Bhushan TN. 2023b. Building
real-world meeting summarization systems using
large language models: A practical perspective.
In Proceedings of the 2023 Conference on Em-
pirical Methods in Natural Language Processing:
Industry Track, pages 343–352, Singapore. As-
sociation for Computational Linguistics.
Md Tahmid Rahman Laskar, Enamul Hoque, and
Jimmy Xiangji Huang. 2022. Domain adaptation
with pre-trained transformers for query-focused
abstractive text summarization. Computational
Linguistics, 48(2):279–320.
Changmao Li and Jeffrey Flanigan. 2023. Task
contamination: Language models may not be
few-shot anymore.
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du,
Mandar Joshi, Danqi Chen, Omer Levy, Mike
Lewis, Luke Zettlemoyer, and Veselin Stoyanov.
2019. Roberta: A robustly optimized bert pre-
training approach. ArXiv, abs/1907.11692.
Mir Tafseer Nayeem and Yllias Chali. 2017a. Ex-
tract with order for coherent multi-document sum-
marization. In Proceedings of TextGraphs-11:
the Workshop on Graph-based Methods for Nat-
ural Language Processing, pages 51–56, Van-
couver, Canada. Association for Computational
Linguistics.
Mir Tafseer Nayeem and Yllias Chali. 2017b. Para-
phrastic fusion for abstractive multi-sentence
compression generation.
In Proceedings of
the 2017 ACM on Conference on Information
and Knowledge Management, CIKM ’17, page
2223–2226, New York, NY, USA. Association for
Computing Machinery.
Mir Tafseer Nayeem, Tanvir Ahmed Fuad, and Yl-
lias Chali. 2018. Abstractive unsupervised multi-
document summarization using paraphrastic sen-
tence fusion. In Proceedings of the 27th Interna-
tional Conference on Computational Linguistics,
pages 1191–1204, Santa Fe, New Mexico, USA.
Association for Computational Linguistics.
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida,
Carroll Wainwright, Pamela Mishkin, Chong
Zhang, Sandhini Agarwal, Katarina Slama, Alex
Ray, John Schulman, Jacob Hilton, Fraser Kelton,
Luke Miller, Maddie Simens, Amanda Askell, Pe-
ter Welinder, Paul F Christiano, Jan Leike, and
Ryan Lowe. 2022. Training language models
to follow instructions with human feedback. In
Advances in Neural Information Processing Sys-
tems, volume 35, pages 27730–27744. Curran
Associates, Inc.
Chengwei Qin, Aston Zhang, Zhuosheng Zhang,
Jiaao Chen, Michihiro Yasunaga, and Diyi Yang.
2023. Is chatgpt a general-purpose natural lan-
guage processing task solver?
Jack W. Rae, Sebastian Borgeaud, Trevor Cai,
Katie Millican, Jordan Hoffmann, Francis Song,
John Aslanides, Sarah Henderson, Roman Ring,
Susannah Young, Eliza Rutherford, Tom Hen-
nigan, Jacob Menick, Albin Cassirer, Richard
Powell, George van den Driessche, Lisa Anne
Hendricks, Maribeth Rauh, Po-Sen Huang,
Amelia Glaese, Johannes Welbl, Sumanth
Dathathri, Saffron Huang, Jonathan Uesato,
John Mellor, Irina Higgins, Antonia Creswell,
Nat McAleese, Amy Wu, Erich Elsen, Siddhant
Jayakumar, Elena Buchatskaya, David Budden,
Esme Sutherland, Karen Simonyan, Michela Pa-
ganini, Laurent Sifre, Lena Martens, Xiang Lor-
raine Li, Adhiguna Kuncoro, Aida Nematzadeh,
Elena Gribovskaya, Domenic Donato, Ange-
liki Lazaridou, Arthur Mensch, Jean-Baptiste
Lespiau, Maria Tsimpoukelli, Nikolai Grigorev,
Doug Fritz, Thibault Sottiaux, Mantas Pajarskas,
Toby Pohlen, Zhitao Gong, Daniel Toyama, Cy-
prien de Masson d’Autume, Yujia Li, Tayfun Terzi,
Vladimir Mikulik, Igor Babuschkin, Aidan Clark,

--- Page 9 ---

Diego de Las Casas, Aurelia Guy, Chris Jones,
James Bradbury, Matthew Johnson, Blake Hecht-
man, Laura Weidinger, Iason Gabriel, William
Isaac, Ed Lockhart, Simon Osindero, Laura
Rimell, Chris Dyer, Oriol Vinyals, Kareem Ayoub,
Jeff Stanway, Lorrayne Bennett, Demis Hassabis,
Koray Kavukcuoglu, and Geoffrey Irving. 2022.
Scaling language models: Methods, analysis &
insights from training gopher.
Brian Roark, Lawrence Wolf-Sonkin, Christo Kirov,
Sabrina J. Mielke, Cibu Johny, Isin Demirsahin,
and Keith Hall. 2020. Processing South Asian
languages written in the Latin script: the Dak-
shina dataset. In Proceedings of the Twelfth Lan-
guage Resources and Evaluation Conference,
pages 2413–2423, Marseille, France. European
Language Resources Association.
Anna Rogers, Olga Kovaleva, and Anna Rumshisky.
2020. A primer in BERTology: What we know
about how BERT works.
Transactions of the
Association for Computational Linguistics, 8:842–
866.
Mohammad Shoeybi, Mostofa Patwary, Raul Puri,
Patrick LeGresley, Jared Casper, and Bryan
Catanzaro. 2019. Megatron-lm: Training multi-
billion parameter language models using model
parallelism. CoRR, abs/1909.08053.
Hugo Touvron, Louis Martin, Kevin Stone, Peter
Albert, Amjad Almahairi, Yasmine Babaei, Niko-
lay Bashlykov, Soumya Batra, Prajjwal Bhargava,
Shruti Bhosale, et al. 2023. Llama 2: Open foun-
dation and fine-tuned chat models. arXiv preprint
arXiv:2307.09288.
Wikipedia. 2023a. Bengali language. Accessed:
May 23, 2023.
Wikipedia. 2023b. Indic languages. Accessed:
May 23, 2023.
Adina Williams, Nikita Nangia, and Samuel Bow-
man. 2018. A broad-coverage challenge corpus
for sentence understanding through inference. In
Proceedings of the 2018 Conference of the North
American Chapter of the Association for Com-
putational Linguistics: Human Language Tech-
nologies, Volume 1 (Long Papers), pages 1112–
1122, New Orleans, Louisiana. Association for
Computational Linguistics.
Susan Zhang, Stephen Roller, Naman Goyal, Mikel
Artetxe, Moya Chen, Shuohui Chen, Christopher
Dewan, Mona Diab, Xian Li, Xi Victoria Lin, Todor
Mihaylov, Myle Ott, Sam Shleifer, Kurt Shuster,
Daniel Simig, Punit Singh Koura, Anjali Sridhar,
Tianlu Wang, and Luke Zettlemoyer. 2022. Opt:
Open pre-trained transformer language models.

```
