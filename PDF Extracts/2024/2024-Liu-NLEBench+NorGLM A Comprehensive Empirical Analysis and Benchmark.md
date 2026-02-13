---
title: "2024-Liu-NLEBench+NorGLM A Comprehensive Empirical Analysis and Benchmark - PDF Extract"
source_pdf: "2024-Liu-NLEBench+NorGLM A Comprehensive Empirical Analysis and Benchmark.pdf"
pages: 18
extracted_at: "2026-02-13T13:13:46.657841"
---

# PDF Extract: 2024-Liu-NLEBench+NorGLM A Comprehensive Empirical Analysis and Benchmark

**Source PDF:** 2024-Liu-NLEBench+NorGLM A Comprehensive Empirical Analysis and Benchmark.pdf
**Total Pages:** 18

---

## Content

```
--- Page 1 ---

NLEBench+NorGLM: A Comprehensive Empirical Analysis and
Benchmark Dataset for Generative Language Models in Norwegian
Peng Liu1, Lemei Zhang1*, Terje Farup1, Even W. Lauvrak1,
Jon Espen Ingvaldsen1, Simen Eide2, Jon Atle Gulla1, Zhirong Yang1,3
1Department of Computer Science, Norwegian University of Science and Technology
2Schibsted Media
3Jinhua Institute of Zhejiang University
{peng.liu, lemei.zhang, jon.espen.ingvaldsen, jon.atle.gulla, zhirong.yang}@ntnu.no
simen.eide@schibsted.com
Abstract
Norwegian, spoken by only 5 million popula-
tion, is under-representative within the most
impressive breakthroughs in NLP tasks. To
the best of our knowledge, there has not yet
been a comprehensive evaluation of the exist-
ing language models (LMs) on Norwegian gen-
eration tasks during the article writing process.
To fill this gap, we 1) compiled the existing
Norwegian dataset and pre-trained 4 Norwe-
gian Open Language Models varied from pa-
rameter scales and architectures, collectively
called NorGLM; 2) introduced a comprehen-
sive benchmark, NLEBench, for evaluating nat-
ural language generation capabilities in Nor-
wegian, encompassing translation and human
annotation. Based on the investigation, we find
that: 1) the mainstream, English-dominated
LM GPT-3.5 has limited capability in under-
standing the Norwegian context; 2) the in-
crease in model parameter scales demonstrates
limited impact on the performance of down-
stream tasks when the pre-training dataset is
constrained in size; 3) smaller models also
demonstrate the reasoning capability through
Chain-of-Thought; 4) a multi-task dataset that
includes synergy tasks can be used to verify the
generalizability of LLMs on natural language
understanding and, meanwhile, test the inter-
connectedness of these NLP tasks. We share
our resources and code for reproducibility1 un-
der a CC BY-NC 4.0 license.
1
Introduction
Recent advancements in Generative Language
Models (GLMs) have significantly improved Nat-
ural Language Processing (NLP) tasks.
How-
ever, most models remain partially closed-source
due to business competition and data privacy con-
cerns, which hinders transparency, flexibility, and
progress in the NLP ecosystem. Open-sourcing
*Corresponding author
1https://github.com/Smartmedia-AI/NorGLM/
models can leverage community contributions, fa-
cilitate collaboration, and accelerate technolog-
ical advancements while better controlling data
use. This approach is especially beneficial for low-
resource languages, aiding their preservation and
development. Currently, benchmarks focus mainly
on languages like English and Chinese, leaving
Low-Resource Languages (LRLs) under-evaluated.
Most benchmarks for low-resourced languages ei-
ther cater to discriminative models (Kutuzov et al.,
2021; Koto et al., 2020; Kummervold et al., 2021)
like BERT (Devlin et al., 2019) or are adapted or
translated from existing English datasets (Luukko-
nen et al., 2023). Nielsen (2023) proposes a closed-
source platform, ScanEval, for evaluating Nordic
languages. However, these benchmarks have two
limitations: First, many nominal generation tasks
are adapted from classification tasks, like multiple-
choice questions, which restrict answer options and
do not assess generative models’ ability to produce
longer texts. Second, most benchmarks are single-
task, with multi-task datasets being particularly
scarce. We argue that by designing a multi-task
dataset that includes several synergy tasks2 in natu-
ral language understanding, it may be possible to
evaluate the generalization ability of large language
models (LLMs) in text comprehension.
To address these gaps, we propose a comprehen-
sive benchmark, NLEBench, specifically tailored
to evaluate the natural language generation capabil-
ities in Norwegian. NLEBench comprises various
real-world NLP tasks and provides relative compar-
isons for Norwegian GLMs with different param-
eter scales and Transformer-based architectures.
Specifically, our benchmark is purposefully de-
signed to be capability probing, such as instructions
specific to Norwegian culture and special expres-
sions, and a document-grounded multi-task dataset
2Here, synergy tasks mean that one task can provide mean-
ingful contexts used to improve the performance of another
task in the multi-task dataset/scenario.
arXiv:2312.01314v2  [cs.CL]  1 Oct 2024

--- Page 2 ---

with human-annotated question-answer pairs and
summaries. We hope that such a side-by-side per-
formance benchmark will inspire future research
on more advanced GLMs for Norwegian and other
LRLs.
In summary, this paper makes the following con-
tributions:
• We
release
a
new
benchmark
dataset,
NLEBench, for the purpose of evaluating
generative language modelling in Norwegian.
To the best of our knowledge, this is the
first benchmarking dataset for Norwegian
causal/autoregressive language modelling3.
• We
contribute
two
novel,
high-quality
datasets: an instruction dataset comprising
human-written instructions specific to Norwe-
gian culture, and a document-grounded multi-
task dataset, which is beneficial for evaluating
GLMs’ comprehension of language nuances
and their ability to navigate intricate logical
challenges.
• We build upon the pioneering work to develop
a series of fundamental Norwegian Generative
Language Models (NorGLMs) with different
parameter scales and Transformer-based archi-
tectures. By in-depth evaluation of these mod-
els on the proposed benchmarks, we provide
crucial insights for understanding the capabil-
ities and scalability of GLMs when applied to
underrepresented languages like Norwegian.
2
Related Work
2.1
Language Models for Low-resource
Languages
Despite the effectiveness of popular LLMs, the
inherent data-hungry attribute limits their perfor-
mance and application to data scarce settings such
as with low-resource languages (Hedderich et al.,
2021). Such languages may also suffer from dif-
ficulties in acquiring readily-accessible resources
compared with mainstream languages such as pre-
trained word embeddings and expert-annotated cor-
pora (Zoph et al., 2016), leading to a significant
open challenge in NLP tasks for low-resourced
scenarios. Several efforts have been made in dif-
ferent low-resource languages (Koto et al., 2020;
Kutuzov et al., 2021; Kummervold et al., 2021) but
3Generative, causal or autoregressive language models are
used interchangeably in this paper.
the models are based on BERT architecture and
tested for language discriminative tasks. Recently,
researchers have proposed several standard evalu-
ation benchmarks on a collection of low-resource
language datasets for language generative tasks
(Ekgren et al., 2022; de Vries and Nissim, 2021;
De Mattei et al., 2020; Antoun et al., 2020). For
instance, Google released a comprehensive bench-
mark, BIG-bench, for over 200 tasks on language
generative tasks (Srivastava et al., 2023), among
which there are only two tasks that contain the
Norwegian language, namely Which Wiki Edit to
match a recent Wikipedia revision to its correspond-
ing edit message, and Language Identification tasks.
They only cover very limited Norwegian samples.
Later, Luukkonen et al. (2023) filtered Finnish from
BIG-bench to build a Finnish benchmark for gener-
ative LMs. However, these existing evaluation data
either originate from pre-existing English datasets
through machine translation or lack the evaluation
data types required for assessing LLMs on multi-
task reasoning.
2.2
Benchmark on Multi-task Datasets
Most existing benchmarks focus on single tasks,
such as question answering, cloze tests, summariza-
tion, and classification. Fine-tuning language mod-
els on individual datasets lacks persuasiveness in
evaluating their ability to generalize across multiple
tasks. Xu et al. (2020) proposed MATINF, a jointly
labeled Chinese dataset for classification, question
answering, and summarization in the maternal and
infant domain. However, this web-crawled dataset
contains significant noise and consists of short texts,
with an average length of 42 Chinese characters. As
language models become more capable of handling
longer texts (Brown et al., 2020; Chen et al., 2023),
datasets with short texts may not reliably predict
the transformative potential of LLMs. Additionally,
the annotated tasks in MATINF lack synergy and
interconnections, leading to assessments still being
conducted on individual tasks and overlooking the
potential effects of task interactions, such as the
feasibility of employing Chain-of-Thought (CoT)
techniques.
3
Norwegian Generative Language Model
Suite - NorGLM
NorGLM models are trained from scratch using
multi-source datasets. We filtered Norwegian texts
from the mC4 and OSCAR web-crawled corpora

--- Page 3 ---

Figure 1: The data distribution within the pre-training
dataset. The inner segment represents languages, and
the outer segment denotes various sourced datasets in
Norwegian. Dataset sizes are shown by numbers (Unit:
Gigabyte), and their percentage contribution to the over-
all dataset. Tags on the right side indicate the number
of tokens for each language, measured in billions.
and included non-copyrighted Norwegian material
from the Norwegian National Library (Nasjonal-
biblioteket)(Kummervold et al., 2021)4. We also
sourced high-quality news articles from Schibsted
and collected tweets (January 2012 to December
2022) and Reddit posts (October 2017 to Decem-
ber 2022) via their respective APIs. To enhance
robustness in downstream tasks, we included Dan-
ish, Swedish, and German texts from the North
Germanic language family, along with a small por-
tion of the English corpus. The size and distribution
of each language are shown in Figure 1.
The models are based on the GPT-2 architec-
ture and are named NorGPT-369M, NorGPT-3B,
and NorGPT-23B, corresponding to their parame-
ter sizes. We also trained a three billion-parameter
model, NorLlama-3B, based on the Llama architec-
ture using Tencent Pre-training Framework (Zhao
et al., 2023). The details of parameter settings are
shown in Table 7. To investigate the potential im-
provement in overall model performance through
oversampling qualified data such as from publish-
ers, akin to Samuel et al. (2023), we continued
training NorGPT-3B (referred to as NorGPT-3B-
continue) using a subset of high-quality data, in-
cluding news articles and material from Nasjonal-
biblioteket5. In addition, we incorporated NB-GPT-
J-6B, which is a model continued-trained from the
English GPT-J-6B model6. We applied similar fine-
4https://huggingface.co/datasets/NbAiLab/NCC
5Please refer to Appendix for model training details.
6https://huggingface.co/NbAiLab/nb-gpt-j-6B
tuning methods to evaluate these models on down-
stream tasks listed in Section 4, aiming to study the
differences between training from scratch and con-
tinuing training on an English pre-trained model.
It’s important to note that GPT-J-6B was continued-
trained with a dataset of 402 billion tokens, approx-
imately 20 times larger than the training dataset
used for our NorGPT models. Additionally, we
evaluated GPT-3.5-Turbo7 on our benchmarks. To
prevent any potential data contamination, the
pre-training dataset is carefully curated to en-
sure there is no overlap with the benchmark
dataset.
4
Norwegian Benchmark Dataset -
NLEBench
This section introduces tasks in NLEBench specif-
ically designed for Norwegian GLMs.
The
datasets are sourced from three categories: exist-
ing datasets, machine-translated datasets using the
Google Translation API, and manually annotated
datasets. Our native Norwegian colleagues evalu-
ated random samples from both the Google Transla-
tion API8 and another free translation API9 support-
ing Norwegian, finding that the former performs
better, especially with confusing words and long
texts. Table 1 outlines the differences and evalu-
ation settings of these datasets. The statistics of
different datasets are shown in Table 8-10.
4.1
Open-domain conversation
NO-ConvAI2 is machine-translated from the En-
glish ConvAI2 dataset (Dinan et al., 2020), which
itself is a refined version of the PersonaChat cor-
pus (Zhang et al., 2018). This task is designed to
evaluate whether the fine-tuned NorGLMs can gen-
erate responses based on knowledge from previous
interactions.
4.2
News summarization
In this task, we assess the abstractive sum-
marization capabilities of NorGLMs using our
NO-CNN/DailyMail dataset, which is machine-
translated from CNN/DailyMail — an English
dataset that includes journalists’ annotated sum-
maries. We employ fine-tuning and the Reinforce-
ment Learning with Human Feedback (RLHF)
strategy on NorGLMs. In step 2 of RLHF, we
7GPT-3.5 and GPT-3.5-Turbo are used interchangeably if
not specified.
8https://cloud.google.com/translate/docs
9https://pypi.org/project/translators/

--- Page 4 ---

Table 1: Overview of the NLEBench dataset and evaluation setups. LoRA denotes Low-Rank Adaptation. RLHF
denotes Reinforcement Learning from Human Feedback. Dist-4 denotes Distinct-4 score. PPL denotes Perplexity.
Datasets
Size (#Samples)
Task
Evaluation Technique Evaluation Metrics
Existing Datasets
NO-Alpaca
51.942K
Instruction Finetuning
LoRA
BLEU, ROUGE-1/L, Dist-4, MAUVE, PPL
NO-BoolQ
12.697K
Question Answering
LoRA
Accuracy, F1 score
NO-QNLI
110.206K
Natural Language Inference
LoRA
Accuracy, F1 score
NO-MRPC
4076
Paraphrase
LoRA
Accuracy, F1 score
Automatic Machine Translated Datasets (Ours)
NO-ConvAI2
19.845K
Open-domain Conversation
LoRA
BLEU, ROUGE-1/L, Dist-4, MAUVE
NO-CNN/DailyMail
76.468K
Summarization
LoRA, RLHF
BLEU, ROUGE-1/L, Dist-4, MAUVE
NO-CrowS-Pairs
1677
Bias Detection
Zero-shot Prompt
PPL
1508
Toxicity Detection
Zero-shot Prompt
Toxicity Score from Perspective API
Human Annotated Datasets (Ours)
NO-Alpaca (extra)
110
Instruction Finetuning
LoRA
BLEU, ROUGE-1/L, Dist-4, MAUVE, PPL
NO-Multi-QA-Sum
467 Summaries
2755 Dialogues
Multi-task Learning
Chain-of-Thought
BLEU, ROUGE-1/L, Dist-4, MAUVE, En-
tailment Score
train the reward model by estimating semantic sim-
ilarity between the candidate generated text and
the human-annotated summary (golden summary)
using the NorBERT model (Kutuzov et al., 2021).
Summaries generated with higher cosine similarity
to the golden summary are prioritized during the
training of the reward model.
4.3
Instructions
This task utilizes datasets from two sources: NO-
Alpaca10, translated from the Stanford Alpaca
dataset (Wang et al., 2023b) into Norwegian us-
ing OpenAI’s GPT-3.5-turbo, and a manually an-
notated set of 110 instructions collected from 10 of
our Norwegian colleagues, focusing specifically on
Norwegian culture and expressions. This combined
dataset is named NO-Alpaca-Plus.
4.4
Natural Language Understanding (NLU)
This task aims to analyze the natural language un-
derstanding capabilities of our NorGLMs. We ex-
tracted the Norwegian portion from the OverLim
dataset11 and selected three tasks commonly used
in evaluating English generative language models:
BoolQ, MRPC, and QNLI. Notably, OverLim is
translated from the GLUE12 and SuperGLUE13
benchmarks. To distinguish it from the original
English version, we use the prefix "NO-" for the
versions used in this paper. The data split follows
the original protocol.
10https://huggingface.co/NbAiLab/nb-gpt-j-6B-alpaca
11https://huggingface.co/datasets/KBLab/overlim
12https://huggingface.co/datasets/glue
13https://super.gluebenchmark.com/
4.5
Toxicity and bias
Generative language models are notorious for am-
plifying biases inherent in the training data (Sheng
et al., 2019) and producing toxic text (Gehman
et al., 2020). To evaluate these issues in NorGLMs,
we used the Perspective API14 on 1508 prompts for
toxicity evaluation and calculated ppl on 1677 sam-
ple pairs for bias evaluation from the NO-CrowS-
Pairs benchmark, a machine-translated version of
the French CrowS-Pairs (Névéol et al., 2022). Due
to the API’s lack of Norwegian support, we trans-
lated the NorGLM generated text into Swedish for
assessment. This benchmark also helps evaluate
potential biases in NorGLMs.
4.6
Multi-task learning
Apart from the benchmarks and translated datasets
mentioned above, we release a multi-task dataset
called NO-Multi-QA-Sum. This section details the
dataset collection process and the tasks performed
using this benchmark.
Data Collection. We recruited three Norwegian
college students as annotators, allowing them to
work in pairs or independently. Each student is
compensated 230 NOK (approx. $21,75 USD) per
hour. Annotators were tasked with conducting a
conversation about a given news article, using con-
tent from the article without a limit on the number
of dialogue turns or question types. After the con-
versation, they were required to write a generic
summary of the article. The dialogue and summary
content did not need to fully overlap, giving annota-
tors some freedom in their dialogue choices. Most
annotators chose to use self-dialogue and summa-
14https://perspectiveapi.com/

--- Page 5 ---

rization for efficiency and flexibility15.
To facilitate the annotation process, we devel-
oped an API, shown in Figure 7, that can connect
with the OpenAI GPT-4 model to suggest annota-
tions. However, annotators were required to verify
the fidelity and usability of the suggested texts. To
ensure quality, each annotation should be cross-
validated and corrected by two other annotators,
achieving one hundred percent internal consensus
on the final annotations. The cross-validation in-
cluded checking the rationality of question-answer
pairs, factual consistency, and language fluency.
Many annotators reported that while GPT-4 (specif-
ically gpt-4-0613)16 was good at generating sug-
gested questions and summaries, it struggled with
producing high-quality answers, necessitating hu-
man effort to maintain annotation quality.
Tasks. In particular, for this dataset, we primar-
ily explored two tasks using the Chain-of-Thought
(CoT) method: based on the given news article, 1)
we first let the model answer the annotated ques-
tions, and then let the model generate a summary
of the article based on the article, questions and
the answers generated by the model. 2) We first
let the model generate summaries, and then ask the
model to answer questions based on the article and
summary generated by the model. We tested these
tasks on NorGPT-3B/23B, NB-GPT-J-6B, which
are fine-tuned on the NO-CNN/DailyMail and NO-
ConvAI2 datasets, and GPT-3.5-Turbo. These tasks
are designed based on the hypothesis that DGQA
and summarization are inherently correlated, and
the synergies between these tasks may influence
the model’s performance on individual tasks. To
address potential annotator oversight in associat-
ing content with the summarization task during
question answering, we instructed annotators to
manually categorize the data based on whether the
question-answering content includes or excludes
a summary, and experiments were conducted on
each subset.
Wang et al. (2023a) developed an element-
aware summarization method using CoT approach
by instructing LLM to generate four key ele-
15This design aims to evaluate the model’s reading compre-
hension ability. We instructed annotators to consider question
diversity, including both simple questions (where the answer
comes from a single source) and complex questions (where
the answer is derived from different parts of the article). The
only potential issue with self-dialogue is that different annota-
tors may have varying interests in the article and may exhibit
personal writing styles during annotation.
16https://platform.openai.com/docs/models/gpt-4-turbo-
and-gpt-4
ments—Entity, Date, Event, and Result—to be in-
tegrated into the summary. They evaluated the pro-
posed method on 200 annotated samples. However,
we argue that human-written summaries demon-
strate greater diversity and flexibility beyond these
four elements. In contrast to their work, our task
aims to investigate potential correlations among the
benchmark datasets proposed in this paper, with
the goal of enhancing language model performance
across various tasks.
5
Experimental Results
In this section, we only list key results for the
benchmark datasets due to the page limit. More
results can be seen in the Appendix.
5.1
Evaluation Metrics
We aim to comprehensively evaluate our models
across various tasks using widely used metrics for
NLP tasks, including BLEU (Papineni et al., 2002),
ROUGE (Lin, 2004), Distinct (Li et al., 2016), and
MAUVE, which is used to assess the generated
and human-written text based on their probability
distribution differences (Pillutla et al., 2021). Fur-
thermore, following the work of Xie et al. (2023),
to measure faithfulness and factual consistency in
multi-task learning, we utilize Entailment scores
from a fine-tuned NorBERT model trained on the
VitaminC dataset (Schuster et al., 2021), which are
translated with Google Cloud Translation API.
5.2
Evaluation Results on NO-ConvAI2
As shown in Table 2, all models, except for GPT-
3.5-Turbo, perform quite similarly. Notably, the
NorGPT-3B model achieves the best results across
multiple evaluation metrics, while the NorGPT-
23B model only shows an advantage in BLEU
scores. GPT-3.5-Turbo, although specifically cu-
rated for conversational purposes, did not exhibit
the advantages expected from its extensive knowl-
edge base. This may be because the knowledge
of other languages in GPT-3.5-Turbo cannot be
directly transferred to understanding Norwegian
conversations, highlighting the unique linguistic
properties of the Norwegian language.
5.3
Evaluation Results on NO-CNN/DailyMail
In Table 3, GPT-3.5-Turbo and NB-GPT-J-6B out-
perform our NorGPTs on BLEU and ROUGE met-
rics. This suggests a substantial number of ex-
pression patterns resembling news articles in their
pre-training datasets. This is plausible given that

--- Page 6 ---

Table 2: Experimental Results on the Conversation Task.
Metrics/Models NorGPT-369M
NorGPT-3B NorLlama-3B NorGPT-3B-continue NorGPT-23B NB-GPT-J-6B
GPT-3.5
BLEU
3.37
4.14
3.82
3.63
4.28
3.87
2.14
ROUGE-1
16.94
17.09
15.20
16.47
16.72
17.05
10.82
ROUGE-L
16.21
16.33
14.53
15.73
15.95
16.26
9.96
Dist-4
86.54
84.68
82.47
86.33
84.41
85.83
85.80
MAUVE
0.56
0.87
0.61
0.71
0.64
0.68
0.72
Table 3: Experimental Results on the News Summarization Task.
Metrics/Models NorGPT-
369M
NorGPT-
3B
NorLlama-
3B
NorGPT-3B-
continue
NorGPT-23B
NorGPT-3B-
RLHF
NB-GPT-J-6B
GPT-3.5
BLEU
2.38
2.61
0.68
2.72
1.90
5.41
4.35
4.38
ROUGE-1
20.97
20.31
12.32
20.53
22.44
23.01
25.64
26.00
ROUGE-L
19.68
19.05
11.56
19.26
21.13
21.63
24.25
24.28
Dist-4
95.32
94.43
92.62
94.35
97.66
92.18
96.41
97.13
MAUVE
0.57
0.62
0.75
0.64
0.50
21.03
0.65
4.38
their datasets likely include a diverse range of news-
papers, magazines, and government reports. Addi-
tionally, this trend is evident in common test sam-
ples, where GPT-3.5-Turbo tends to generate more
formal language compared to conversational lan-
guage. Despite this, we observed that the models’
performance improves after reinforcement learning,
especially in replicating the word distribution of
human writing and generating summaries of simi-
lar length. This is supported by the highest scores
in MAUVE and BLEU. Although the model with
reinforcement learning may not always surpass the
fine-tuned model in accuracy, it actively strives to
mimic human writing patterns.
5.4
Evaluation Results on NO-Alpaca-Plus
Table 13 demonstrates the performance of our base-
line models after fine-tuning on the NO-Alpaca
dataset. Given that this dataset is translated using
GPT-3.5-Turbo, we could not use GPT-3.5-Turbo
as a baseline due to OpenAI’s terms and policies17.
NB-GPT-J-6B outperforms other models on most
evaluation metrics, likely due to its pre-training on
a set of self-annotated Norwegian instructions, as
described on their model webpage. Among our
NorGLM models, NorLlama-3B achieved better
BLEU and ROUGE scores compared to others, but
worse MAUVE and perplexity scores. This is an
interesting phenomenon, indicating that NorLlama-
3B’s results hit the most n-grams, yet its token
probability distribution deviates the most from
human-annotated results. A case study revealed
that while NorLlama-3B generates overlapping
words or phrases with the golden answer, it some-
17https://openai.com/policies/
times lacks logical coherence between sentences,
and the meanings of sentences can even be mutu-
ally exclusive, as shown in Figure 2.
Meanwhile, in our self-annotated 110 instruc-
tions, we select two typical cases generated from
GPT-3.5-Turbo related to Norwegian culture and
special expression shown in Figure 3 and Figure 4
respectively. Specifically, Figure 3 shows a factual
inconsistency issue in generated texts. In Figure 4,
the input prompt asks who uses the word, but the
model interprets the meaning of the word rather
than understanding the question. Therefore, with
limited annotated data, we can still find limitations
in the model’s understanding of the specific culture
behind the language.
5.5
Evaluation Results on NLU tasks
Table 14 reports the results on NLU tasks. Among
NorGLMs, NorGPT-23B model consistently out-
performs others on different NLU datasets across
both evaluation metrics.
However, NB-GPT-J-
6B performs better on the NO-QNLI benchmark
and achieves a higher F1-score on the NO-MRPC
benchmark.
5.6
Evaluation Results on Toxicity and Bias
The results of average toxicity scores from 6 per-
spectives including Toxicity, Severe toxicity, Iden-
tity attack, Insult, Profanity and Threat are shown
in Table 15. All toxicity scores range from 0 to
1, with lower values indicating less toxic text gen-
erated by the model. Although NorLlama-3B ex-
hibits the lowest values across all metrics, a sig-
nificant portion of its generated text consists of
meaningless characters or words. We conducted a

--- Page 7 ---

random sampling of texts generated by GPT mod-
els with high toxicity values and traced hazardous
words back to the pre-training dataset. Surpris-
ingly, most of these hazardous words did not origi-
nate from social media, as commonly assumed, but
from daily news articles. For instance, the phrase
"tok livet av" (taken life from/kill) often appeared
in news reports describing murders, as illustrated
in Figure 1. These original news articles did not
convey toxic information but were instead factual
descriptions of criminal events. This discovery un-
derscores the importance of not only filtering out
toxic inputs during the pre-training process but also
considering which prompts may lead the model to
generate toxic text.
Table 16 presents findings from stereotype and
bias detection using the NO-CrowS-Pairs dataset.
This dataset encompasses nine categories: gender,
religion, race/color, sexual orientation, age, nation-
ality, disability, physical appearance, and socioe-
conomic status. Each sample consists of a stereo-
type (sent_more) paired with an anti-stereotype
(sent_less) sentence. Following the work of Tou-
vron et al. (2023), model bias is assessed by com-
paring perplexity scores between these pairs and re-
porting the percentage of the model biased towards
sent_more in the table. Higher values indicate a
stronger bias towards public stereotypes. Overall,
the benchmark models demonstrated robust perfor-
mance across most bias categories. However, they
exhibited a bias towards sent_less in relation to
religion, suggesting a relative bias in this specific
category.
5.7
Evaluation with CoT
In this task, all baseline models except GPT-3.5
were fine-tuned on the NO-CNN/DailyMail and
NO-ConvAI2 datasets, enabling them to handle
related tasks effectively. However, none of these
models were fine-tuned using document-grounded
question answering datasets or similar CoT tasks in-
vestigated in this study. Table 4 and Table 5 present
the outcomes of the multi-task dataset under dif-
ferent scenarios. The tables distinguish datasets
where the question answering content includes or
excludes a summary, labeled as "contain" and "not
contain" respectively. For both tasks, we utilized
different prompt templates and reported the opti-
mal performance in the tables. From the results,
we draw several observations:
In task one, we observed that GPT-3.5 signif-
icantly improved in summarization performance
with the CoT method, while other models saw a
degradation in this aspect. For DGQA, NorGPT-3B
and NorGPT-23B models showed improvements
through CoT, whereas NB-GPT-J-6B exhibited
mixed results across different datasets. Analyz-
ing these results solely based on the tables proved
challenging, as there was no clear correlation be-
tween CoT improvements and model sizes or pre-
training dataset sizes. This contrasts with prior find-
ings suggesting CoT benefits are more pronounced
with larger models (Wei et al., 2022). Combin-
ing results from Table 2 and Table 3, we observed
models that initially performed well in their tasks
showed further enhancement with CoT adaptations.
For instance, GPT-3.5 excelled in summarization
on the NO-CNN/DailyMail dataset after CoT, and
NorGPT-3B and NorGPT-23B models improved in
document-grounded question answering on the NO-
ConvAI2 dataset. Figure 5 illustrates an example
where CoT-generated summaries closely approxi-
mate human-written summaries compared to direct
prompts for the model to generate summaries. The
English translation is shown in Figure 6.
While we observe that the synergy between the
two tasks enhances the model’s performance on
both, we also find that incorporating a summary
into a QA task improves the quality of the gener-
ated summary compared to QA tasks without one.
However, the reverse scenario is not necessarily
true. We speculate that QA breaks down the sum-
marization task into smaller components, enabling
the model to better comprehend the input text. This
process mirrors the human learning process.
Moreover, as shown in both Table 4 and Table
5, we find that after CoT, the Entailment scores of
most models increased, indicating that the answers
and summaries generated by the models are more
aligned with the context described in the article.
Therefore, CoT has the potential to enhance the
factual consistency of the generated outputs.
5.8
Human Evaluation
To evaluate the quality of the translated datasets,
we conducted a human evaluation on three datasets
translated by the Google API: NO-ConvAI2, NO-
CNN/DailyMail and NO-CrowS-Pairs.
Specifi-
cally, considering the constraints of time and cost,
we randomly selected 50 samples from each of the
three datasets. We recruited three Norwegian na-
tive speakers, all of whom are college students, to
independently score the Adequacy and Fluency of
each text. Adequacy measures whether the trans-

--- Page 8 ---

Table 4: Experimental Results on task one using NO-Multi-QA-Sum dataset for summarization task.
Datasets
Metrics
NorGPT-3B
NB-GPT-J-6B
NorGPT-23B
GPT-3.5
Zero-Shot
CoT
Zero-Shot
CoT
Zero-Shot
CoT
Zero-Shot
CoT
Contain
BLEU
0.43
0.38
1.31
1.10
1.30
1.01
10.31
13.19
ROUGE-1
10.71
7.91
12.86
11.31
18.36
16.37
34.77
40.95
ROUGE-L
9.46
7.51
12.11
10.74
17.12
14.77
32.21
37.19
Dist-4
79.88
81.98
94.14
91.86
95.69
92.43
96.66
96.78
MAUVE
0.41
2.10
6.02
8.13
8.53
24.43
77.83
85.08
Entailment Score
71.43
75.00
80.28
74.65
77.46
78.87
81.69
83.10
Not Contain
BLEU
0.40
0.36
1.33
0.99
1.28
1.03
9.60
11.70
ROUGE-1
10.32
7.31
13.36
10.98
18.40
15.67
34.14
38.57
ROUGE-L
9.15
6.92
12.73
10.40
17.01
14.28
31.20
35.47
Dist-4
79.13
80.25
93.89
92.17
95.24
94.10
96.59
96.82
MAUVE
0.41
0.57
0.96
0.56
3.38
0.94
83.25
81.40
Entailment Score
77.19
77.95
82.32
82.58
82.83
81.57
87.12
87.12
Table 5: Experimental Results on task two using NO-Multi-QA-Sum dataset for document-grounded question
answering task.
Datasets
Metrics
NorGPT-3B
NB-GPT-J-6B
NorGPT-23B
GPT-3.5
Zero-Shot
CoT
Zero-Shot
CoT
Zero-Shot
CoT
Zero-Shot
CoT
Contain
BLEU
1.88
1.84
1.93
1.93
1.55
1.69
25.62
25.36
ROUGE-1
7.55
9.15
7.16
7.26
11.57
14.45
52.25
52.09
ROUGE-L
7.04
8.51
6.78
6.90
10.49
13.05
48.99
48.72
Dist-4
81.20
82.73
87.43
87.10
89.57
91.67
86.67
86.51
MAUVE
0.45
0.57
0.65
0.42
1.01
0.93
41.79
51.16
Entailment Score
73.65
74.88
79.56
79.01
76.60
77.83
83.25
82.76
Not Contain
BLEU
1.80
1.90
1.92
1.89
1.55
1.72
24.70
24.45
ROUGE-1
7.38
8.61
7.19
7.09
10.65
13.91
50.77
50.44
ROUGE-L
6.89
7.92
6.77
6.67
9.67
12.49
47.40
46.99
Dist-4
81.22
81.47
86.80
86.74
90.35
91.43
85.99
85.70
MAUVE
0.51
0.46
0.59
0.46
0.95
0.72
49.58
49.20
Entailment Score
77.52
77.14
80.90
81.16
81.27
81.61
85.78
85.61
lated text accurately conveys the meaning of the
original text, while Fluency assesses whether the
expression of the translated text aligns with native
Norwegian expressions. The scores range from
1 to 5, with 1 representing non-compliance and
5 representing full compliance. In addition, we
used the Claude 3 Opus model18 to translate the
same 150 samples, adhering strictly to the model
settings described in Enis and Hopkins (2024) 19.
The experimental results are shown in Table 6. The
detailed instructions to the evaluators are shown in
Figure 8.
The results show that Claude 3 Opus outper-
forms Google API in both Adequacy and Fluency
indicators. We can also see that both Google Trans-
lation and Claude Translation are able to accurately
convey most of the meaning of the original text
and include some native or even good native ex-
pressions. We adopt Fleiss’ kappa (κ) to measure
18https://www.anthropic.com/news/claude-3-family
19Please note that, at the time of this research, Claude 3
Opus had not yet been published.
Inter-rater Agreement among the three raters for
each evaluation metric and dataset. We observed
high consistency among evaluators in adequacy as-
sessments, while fluency evaluations demonstrated
low consistency20. By comparing individual scores
with the types of translation errors they annotated,
we found that bias exists among evaluators. For the
same translated text, although all evaluators marked
the translation expression as incorrect, some evalu-
ators with higher scores believed that, despite not
conforming to Norwegian expression habits, the
translation still conveyed the original meaning. In
contrast, another evaluator believed that incorrect
word choices significantly affected the text’s flu-
ency and gave a lower score. Furthermore, based
on the annotations, the most frequent translation
errors in the sample dataset were "the misuse of
words", followed by "missing words", "incorrect
word order", and "extra words".
20https://www.ncbi.nlm.nih.gov/books/NBK92287/table
/executivesummary.t2/?report=objectonly

--- Page 9 ---

Table 6: Human evaluation results on the quality of machine translated datasets in NLEBench.
Datasets
Google Translation API
Claude 3 Opus
Adequacy / Fleiss’ kappa
Fluency / Fleiss’ kappa
Adequacy / Fleiss’ kappa
Fluency / Fleiss’ kappa
NO-ConvAI2
3.89 / 0.72
3.15 / 0.60
4.42 / 0.88
3.99 / 0.35
NO-CNN/DailyMail
4.11 / 0.60
3.46 / 0.48
4.40 / 0.73
3.79 / 0.32
NO-CrowS-Pairs
4.49 / 0.78
4.26 / 0.67
4.77 / 0.84
4.55 / 0.56
6
Discussion
In this subsection, we present observations from
the longitudinal comparison of different models
in downstream tasks, as detailed in Section 5: 1)
While NB-GPT-J-6B did not achieve the highest
scores across all tasks, it showed consistent per-
formance and the best perplexity scores compared
to our NorGLMs on nearly all tasks. This consis-
tency is likely due to its initial training on large
English datasets before being continue-trained on
Norwegian data. 2) The 23B model did not show
the expected absolute advantage in downstream
tasks. We find that with a small-scale pre-training
dataset, a larger model cannot demonstrate its abil-
ity to better cope with complex problems, which
also supports the findings in Hoffmann et al. (2022).
3) The results highlight the promising abilities of
smaller language models on specific tasks. How-
ever, these models often lack consistency in gen-
erating high-quality, meaningful text. 4) A com-
parison between Table 3 and Table 4 reveals sig-
nificant differences between summaries written by
journalists and those generated by GPT-3.5 or non-
professionals. However, the model’s performance
on the latter datasets appears to be proportional to
its size. GPT-3.5’s performance on NO-Multi-QA-
Sum has improved significantly, possibly due to the
similarity of frameworks and training data overlap
between GPT-3.5 and GPT-4. 5) GPT-3.5’s dif-
ficulties with specialized Norwegian instructions
highlight the unique complexities of the Norwe-
gian language, which are challenging for English-
dominated models. This emphasizes the need to
focus on low-resource languages to better under-
stand their cultural nuances.21
7
Conclusion
In this paper, we introduced a suite of Norwegian
Generative Language Models and a comprehensive
21We have released more Norwegian foundation models and
datasets and will continue to update and integrate Norwegian-
related resources. Please follow our GitHub repository for
more information.
benchmark with seven tasks tailored for the under-
represented Norwegian language. Through exten-
sive analysis, we uncovered insights not previously
revealed by existing benchmarks. Our evaluation
of the NO-Multi-QA-Sum dataset highlighted the
effectiveness of multi-task datasets in assessing
natural language understanding through complex
tasks like Chain-of-Thought (CoT). We also noted
differences between human-annotated summaries
and those generated by GPT-3.5, providing valu-
able insights for future abstractive summarization
advancements. Furthermore, our study emphasized
the unique linguistic and cultural aspects of Norwe-
gian, suggesting that mainstream benchmarks may
not fully capture the performance of language mod-
els on low-resource languages. Thus, developing
benchmarks specific to these languages is essential
for accurate evaluation and development.
8
Limitations
Although NLEBench is currently the most com-
prehensive benchmark for Norwegian, its coverage
of applications and downstream tasks remains lim-
ited. Our benchmark is open-ended and inevitably
cannot cover everything in Norway. Nevertheless,
we believe that the published resources will signifi-
cantly aid research in generative language models
for low-resource scenarios. While Balahur and
Turchi (2014) suggested that translation systems
produce good quality data, translation errors and
misconceptions persist. Due to budget constraints
and the large volume of translation samples, ensur-
ing the quality of our translated dataset was chal-
lenging. However, the value of machine-translated
datasets should not be dismissed. For instance, we
use NO-ConvAI2 to fine-tune the model, endowing
it with conversational capabilities, and NO-Alpaca
includes general knowledge about Norway, such
as The capital of Norway is Oslo, although the
coverage remains limited.
Another constraint is the scarcity of human-
annotated samples in our benchmark, largely at-
tributable to the extensive time and financial re-

--- Page 10 ---

sources required for their collection. Notably, the
process of amassing over 500 samples for the NO-
Multi-QA-Sum dataset was time-intensive and ne-
cessitated thorough quality control measures be-
fore implementation. Moreover, acquiring suffi-
cient Norwegian pre-training data and considering
the copyright issues of data poses a formidable
challenge. The current difficulty lies in obtain-
ing a training dataset of comparable size to those
available for English, severely constraining the per-
formance of our pre-trained models. Despite our
efforts to procure data from diverse sources and pro-
vide pertinent statistical insights, certain data can-
not be redistributed, complicating efforts to repli-
cate our pretraining phase. Looking ahead, we aim
to mitigate the shortage of textual data through
manual annotation efforts or by integrating multi-
modal data, thereby fostering advancements in low-
resource language model development within the
broader research community.
Acknowledgements
This publication has been funded by the SFI
NorwAI, (Centre for Research-based Innovation,
309834). The authors gratefully acknowledge the
financial support from the Research Council of
Norway and the partners of the SFI NorwAI.
We extend our thanks to the organizers of
EMNLP 2024 and the reviewers for their valuable
feedback. Special thanks to the IDUN team at
NTNU (Själander et al., 2019) for providing es-
sential computational resources, and to Schibsted
and the National Library of Norway (Nasjonalbib-
lioteket) for supplying the crucial dataset for our
research.
References
Wissam Antoun, Fady Baly, and Hazem Hajj. 2020.
AraGPT2: Pre-trained transformer for arabic lan-
guage generation. arXiv preprint arXiv:2012.15520.
Alexandra Balahur and Marco Turchi. 2014. Compara-
tive experiments using supervised learning and ma-
chine translation for multilingual sentiment analysis.
Computer Speech & Language, 28(1):56–75.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, Sandhini Agarwal, Ariel Herbert-Voss,
Gretchen Krueger, Tom Henighan, Rewon Child,
Aditya Ramesh, Daniel Ziegler, Jeffrey Wu, Clemens
Winter, Chris Hesse, Mark Chen, Eric Sigler, Ma-
teusz Litwin, Scott Gray, Benjamin Chess, Jack
Clark, Christopher Berner, Sam McCandlish, Alec
Radford, Ilya Sutskever, and Dario Amodei. 2020.
Language models are few-shot learners.
In Ad-
vances in Neural Information Processing Systems,
volume 33, pages 1877–1901. Curran Associates,
Inc.
Yukang Chen, Shengju Qian, Haotian Tang, Xin Lai,
Zhijian Liu, Song Han, and Jiaya Jia. 2023. Lon-
gLoRA: Efficient fine-tuning of long-context large
language models. arXiv preprint arXiv:2309.12307.
Lorenzo
De
Mattei,
Michele
Cafagna,
Felice
Dell’Orletta, Malvina Nissim, and Marco Guerini.
2020.
GePpeTto carves italian into a language
model. arXiv preprint arXiv:2004.14253.
Wietse de Vries and Malvina Nissim. 2021. As good
as new. How to successfully recycle English GPT-2
to make models for other languages. In Findings of
the Association for Computational Linguistics: ACL-
IJCNLP 2021, pages 836–846, Online. Association
for Computational Linguistics.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. BERT: Pre-training of
deep bidirectional transformers for language under-
standing. In Proceedings of the 2019 Conference of
the North American Chapter of the Association for
Computational Linguistics: Human Language Tech-
nologies, Volume 1 (Long and Short Papers), pages
4171–4186, Minneapolis, Minnesota. Association for
Computational Linguistics.
Emily Dinan, Varvara Logacheva, Valentin Malykh,
Alexander Miller, Kurt Shuster, Jack Urbanek,
Douwe Kiela, Arthur Szlam, Iulian Serban, Ryan
Lowe, et al. 2020. The second conversational intel-
ligence challenge (ConvAI2). In The NeurIPS’18
Competition: From Machine Learning to Intelligent
Conversations, pages 187–208. Springer.
Ariel Ekgren, Amaru Cuba Gyllensten, Evangelia
Gogoulou, Alice Heiman, Severine Verlinden, Joey
Öhman, Fredrik Carlsson, and Magnus Sahlgren.
2022. Lessons learned from GPT-SW3: Building
the first large-scale generative language model for
Swedish.
In Proceedings of the Thirteenth Lan-
guage Resources and Evaluation Conference, pages
3509–3518, Marseille, France. European Language
Resources Association.
Maxim Enis and Mark Hopkins. 2024. From llm to
nmt: Advancing low-resource machine translation
with claude. arXiv preprint arXiv:2404.13813.
Samuel Gehman, Suchin Gururangan, Maarten Sap,
Yejin Choi, and Noah A. Smith. 2020. RealToxi-
cityPrompts: Evaluating neural toxic degeneration
in language models. In Findings of the Association
for Computational Linguistics: EMNLP 2020, pages
3356–3369, Online. Association for Computational
Linguistics.
Michael A. Hedderich, Lukas Lange, Heike Adel, Jan-
nik Strötgen, and Dietrich Klakow. 2021. A survey

--- Page 11 ---

on recent approaches for natural language process-
ing in low-resource scenarios. In Proceedings of
the 2021 Conference of the North American Chap-
ter of the Association for Computational Linguistics:
Human Language Technologies, pages 2545–2568,
Online. Association for Computational Linguistics.
Jordan Hoffmann, Sebastian Borgeaud, Arthur Men-
sch, Elena Buchatskaya, Trevor Cai, Eliza Ruther-
ford, Diego de Las Casas, Lisa Anne Hendricks, Jo-
hannes Welbl, Aidan Clark, Thomas Hennigan, Eric
Noland, Katherine Millican, George van den Driess-
che, Bogdan Damoc, Aurelia Guy, Simon Osindero,
Karén Simonyan, Erich Elsen, Oriol Vinyals, Jack
Rae, and Laurent Sifre. 2022. An empirical analysis
of compute-optimal large language model training.
In Advances in Neural Information Processing Sys-
tems, volume 35, pages 30016–30030. Curran Asso-
ciates, Inc.
Fajri Koto, Afshin Rahimi, Jey Han Lau, and Timo-
thy Baldwin. 2020. IndoLEM and IndoBERT: A
benchmark dataset and pre-trained language model
for Indonesian NLP. In Proceedings of the 28th Inter-
national Conference on Computational Linguistics,
pages 757–770, Barcelona, Spain (Online). Interna-
tional Committee on Computational Linguistics.
Per E Kummervold, Javier De la Rosa, Freddy Wet-
jen, and Svein Arne Brygfjeld. 2021. Operationaliz-
ing a national digital library: The case for a Norwe-
gian transformer model. In Proceedings of the 23rd
Nordic Conference on Computational Linguistics
(NoDaLiDa), pages 20–29, Reykjavik, Iceland (On-
line). Linköping University Electronic Press, Swe-
den.
Andrey Kutuzov, Jeremy Barnes, Erik Velldal, Lilja
Øvrelid, and Stephan Oepen. 2021. Large-scale con-
textualised language modelling for Norwegian. In
Proceedings of the 23rd Nordic Conference on Com-
putational Linguistics (NoDaLiDa), pages 30–40,
Reykjavik, Iceland (Online). Linköping University
Electronic Press, Sweden.
Jiwei Li, Michel Galley, Chris Brockett, Jianfeng Gao,
and Bill Dolan. 2016. A diversity-promoting ob-
jective function for neural conversation models. In
Proceedings of the 2016 Conference of the North
American Chapter of the Association for Computa-
tional Linguistics: Human Language Technologies,
pages 110–119, San Diego, California. Association
for Computational Linguistics.
Chin-Yew Lin. 2004. ROUGE: A package for auto-
matic evaluation of summaries. In Text Summariza-
tion Branches Out, pages 74–81, Barcelona, Spain.
Association for Computational Linguistics.
Risto Luukkonen, Ville Komulainen, Jouni Luoma,
Anni Eskelinen, Jenna Kanerva, Hanna-Mari Kupari,
Filip Ginter, Veronika Laippala, Niklas Muennighoff,
Aleksandra Piktus, Thomas Wang, Nouamane Tazi,
Teven Scao, Thomas Wolf, Osma Suominen, Samuli
Sairanen, Mikko Merioksa, Jyrki Heinonen, Aija
Vahtola, Samuel Antao, and Sampo Pyysalo. 2023.
FinGPT: Large generative models for a small lan-
guage. In Proceedings of the 2023 Conference on
Empirical Methods in Natural Language Processing,
pages 2710–2726, Singapore. Association for Com-
putational Linguistics.
Aurélie Névéol, Yoann Dupont, Julien Bezançon, and
Karën Fort. 2022. French CrowS-pairs: Extending a
challenge dataset for measuring social bias in masked
language models to a language other than English.
In Proceedings of the 60th Annual Meeting of the
Association for Computational Linguistics (Volume
1: Long Papers), pages 8521–8531, Dublin, Ireland.
Association for Computational Linguistics.
Dan Nielsen. 2023. ScandEval: A benchmark for Scan-
dinavian natural language processing. In Proceed-
ings of the 24th Nordic Conference on Computational
Linguistics (NoDaLiDa), pages 185–201, Tórshavn,
Faroe Islands. University of Tartu Library.
Kishore Papineni, Salim Roukos, Todd Ward, and Wei-
Jing Zhu. 2002. Bleu: a method for automatic evalu-
ation of machine translation. In Proceedings of the
40th Annual Meeting of the Association for Compu-
tational Linguistics, pages 311–318, Philadelphia,
Pennsylvania, USA. Association for Computational
Linguistics.
David Patterson, Joseph Gonzalez, Quoc Le, Chen
Liang, Lluis-Miquel Munguia, Daniel Rothchild,
David So, Maud Texier, and Jeff Dean. 2021. Carbon
emissions and large neural network training. arXiv
preprint arXiv:2104.10350.
Krishna Pillutla, Swabha Swayamdipta, Rowan Zellers,
John Thickstun, Sean Welleck, Yejin Choi, and Zaid
Harchaoui. 2021. Mauve: Measuring the gap be-
tween neural text and human text using divergence
frontiers. In Advances in Neural Information Pro-
cessing Systems, volume 34, pages 4816–4828. Cur-
ran Associates, Inc.
David Samuel, Andrey Kutuzov, Samia Touileb, Erik
Velldal, Lilja Øvrelid, Egil Rønningstad, Elina Sigdel,
and Anna Palatkina. 2023. NorBench – a benchmark
for Norwegian language models. In Proceedings
of the 24th Nordic Conference on Computational
Linguistics (NoDaLiDa), pages 618–633, Tórshavn,
Faroe Islands. University of Tartu Library.
Tal Schuster, Adam Fisch, and Regina Barzilay. 2021.
Get your vitamin C! robust fact verification with
contrastive evidence. In Proceedings of the 2021
Conference of the North American Chapter of the
Association for Computational Linguistics: Human
Language Technologies, pages 624–643, Online. As-
sociation for Computational Linguistics.
Emily Sheng, Kai-Wei Chang, Premkumar Natarajan,
and Nanyun Peng. 2019. The woman worked as
a babysitter: On biases in language generation. In
Proceedings of the 2019 Conference on Empirical
Methods in Natural Language Processing and the

--- Page 12 ---

9th International Joint Conference on Natural Lan-
guage Processing (EMNLP-IJCNLP), pages 3407–
3412, Hong Kong, China. Association for Computa-
tional Linguistics.
Magnus Själander, Magnus Jahre, Gunnar Tufte, and
Nico Reissmann. 2019. EPIC: An energy-efficient,
high-performance GPGPU computing research in-
frastructure. arXiv preprint arXiv:1912.05848.
Aarohi Srivastava, Abhinav Rastogi, Abhishek Rao,
Abu Awal Md Shoeb, Abubakar Abid, Adam Fisch,
Adam R Brown, Adam Santoro, Aditya Gupta, Adrià
Garriga-Alonso, et al. 2023. Beyond the imitation
game: Quantifying and extrapolating the capabili-
ties of language models. Transactions on Machine
Learning Research.
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier
Martinet, Marie-Anne Lachaux, Timothée Lacroix,
Baptiste Rozière, Naman Goyal, Eric Hambro,
Faisal Azhar, et al. 2023. Llama: Open and effi-
cient foundation language models. arXiv preprint
arXiv:2302.13971.
Yiming Wang, Zhuosheng Zhang, and Rui Wang. 2023a.
Element-aware summarization with large language
models: Expert-aligned evaluation and chain-of-
thought method. In Proceedings of the 61st Annual
Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 8640–8665,
Toronto, Canada. Association for Computational Lin-
guistics.
Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa
Liu, Noah A. Smith, Daniel Khashabi, and Hannaneh
Hajishirzi. 2023b. Self-instruct: Aligning language
models with self-generated instructions. In Proceed-
ings of the 61st Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers),
pages 13484–13508, Toronto, Canada. Association
for Computational Linguistics.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten
Bosma, brian ichter, Fei Xia, Ed Chi, Quoc V Le,
and Denny Zhou. 2022. Chain-of-thought prompt-
ing elicits reasoning in large language models. In
Advances in Neural Information Processing Systems,
volume 35, pages 24824–24837. Curran Associates,
Inc.
Zhouhang Xie, Sameer Singh, Julian McAuley, and
Bodhisattwa Prasad Majumder. 2023. Factual and
informative review generation for explainable recom-
mendation. Proceedings of the AAAI Conference on
Artificial Intelligence, 37(11):13816–13824.
Canwen Xu, Jiaxin Pei, Hongtao Wu, Yiyu Liu, and
Chenliang Li. 2020. MATINF: A jointly labeled
large-scale dataset for classification, question answer-
ing and summarization. In Proceedings of the 58th
Annual Meeting of the Association for Computational
Linguistics, pages 3586–3596, Online. Association
for Computational Linguistics.
Saizheng Zhang, Emily Dinan, Jack Urbanek, Arthur
Szlam, Douwe Kiela, and Jason Weston. 2018. Per-
sonalizing dialogue agents: I have a dog, do you
have pets too? In Proceedings of the 56th Annual
Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 2204–2213,
Melbourne, Australia. Association for Computational
Linguistics.
Zhe Zhao, Yudong Li, Cheng Hou, Jing Zhao, Rong
Tian, Weijie Liu, Yiren Chen, Ningyuan Sun,
Haoyan Liu, Weiquan Mao, Han Guo, Weigang Gou,
Taiqiang Wu, Tao Zhu, Wenhang Shi, Chen Chen,
Shan Huang, Sihong Chen, Liqun Liu, Feifei Li, Xi-
aoshuai Chen, Xingwu Sun, Zhanhui Kang, Xiaoy-
ong Du, Linlin Shen, and Kimmo Yan. 2023. Ten-
centPretrain: A scalable and flexible toolkit for pre-
training models of different modalities. In Proceed-
ings of the 61st Annual Meeting of the Association
for Computational Linguistics (Volume 3: System
Demonstrations), pages 217–225, Toronto, Canada.
Association for Computational Linguistics.
Barret Zoph, Deniz Yuret, Jonathan May, and Kevin
Knight. 2016. Transfer learning for low-resource neu-
ral machine translation. In Proceedings of the 2016
Conference on Empirical Methods in Natural Lan-
guage Processing, pages 1568–1575, Austin, Texas.
Association for Computational Linguistics.

--- Page 13 ---

A
NorGLM Model Parameter Settings
Table 7: The training parameter settings of NorGLMs
Items/Models
NorGPT-
369M
NorGPT-
3B
NorLlama-
3B
NorGPT-
23B
#Params
369.94M
2.95B
3.07B
23.03B
#Layers
24
32
32
49
#Attention heads
16
32
32
32
#Hidden units
1024
2688
2688
6144
Context window
2048
2048
2048
2048
Initial lr
1.5E-04
1.5E-04
5.6E-05
9.7E-05
Global batch size
24
16
16
112
Training data size
196G
196G
196G
196G
Vocabulary size
64,000
64,000
64,000
64,000
B
The Statistics of Benchmark Datasets
Data statistics are in Table 8-10.
C
Case Study on the Instruction
Finetuning Task
Examples of generated responses for the instruc-
tions in the NO-Alpaca(-Plus) benchmark are
shown in Figure 2-4.
Figure 2: Example of NorLlama-3B on NO-Alpaca
benchmark. The texts that coincide between the gener-
ated and annotated text are highlighted in red. Transla-
tions are in the brackets.
Figure 3: Example of generated performance of GPT-
3.5 on Norwegian culture instruction of NO-Alpaca-
Plus. Translations are on the right.
Figure 4: Example of generated performance of GPT-
3.5 on Norwegian special expression instruction of NO-
Alpaca-Plus. Translations are on the right.
D
Efficiency Benchmarks
In this section, we report our NorGLM pre-training
specifications and the results are shown in Table 11.
We estimated the energy consumption in the model
training according to Eq. (1):
KW h = Hours to train × Number of Processors × AP P × P UE
1000
(1)
The NVIDIA A100 40G and 80G GPUs are re-
ported to have a Thermal Design Power (TDP) of
250W and 300W 22. We have used these TDP val-
ues as the Average Power per Processor (APP) in
our calculations. Power usage effectiveness (PUE)
is a metric to describe data center efficiency and is
calculated from the total energy use divided by the
energy directly consumed by a datacenter’s com-
puting equipment. The average industry data centre
PUE in 2020 was 1.58 (Patterson et al., 2021), and
we have used this PUE value in our calculations.
It is widely acknowledged that large-scale pre-
training demands a significant amount of compu-
tational resources, and larger models typically re-
quire more computational resources and energy
consumption to achieve convergence given the
same pre-training dataset. When training the 3B
models, we note that NorLlama-3B took less time
than NorGPT-3B to converge. This may be related
to the different model architectures and different
training platforms.
We can also see that the estimated energy con-
sumption grows significantly with the model size
(number of parameters). The number of parame-
ters grows with a factor of 8.1 when we go from
22https://www.nvidia.com/content/dam/en-
zz/Solutions/Data-Center/a100/pdf/nvidia-a100-datasheet-
us-nvidia-1758950-r4-web.pdf

--- Page 14 ---

Table 8: Statistics on NO-Alpaca, NO-CNN/DailyMail dataset, where P denotes prompt, A denotes answer, N is
news article and S is summary.
Name
type #samples
#total_words
#avg_words
#total_tokens
#avg_tokens
NO-Alpaca train
41,554
544,388(P)
1,730,937(A) 13.1(P)
41.7(A) 756,749(P)
2,416,338(A) 18.2(P)
58.2(A)
test
10,388
137,587(P)
445,037(A)
13.3(P)
42.8(A) 19,071(P)
622,560(A)
18.4(P)
59.9(A)
NO-CNN/
DailyMail
train
61,181
39,518,361(N) 2,546,653(S) 645.9(N) 41.6(S) 55,225,295(N) 3,630,417(S) 902.7(N) 59.3(S)
test
15,287
9,878,627(N)
634,898(S)
646.2(N) 41.5(S) 13,802,673(N) 904,731(S)
902.9(N) 59.2(S)
Table 9: Statistics on NO-ConvAI2 dataset.
Type
#dialogues
#avg_turns/dialogue
#utterances
#avg_utterances
#tokens
#avg_tokens
Train
17,878
6.85
1,785,227
10.29
2,211,098
12.74
Test
1,967
7.78
304,245
10.28
374,618
12.66
Table 10: Statistics on NO-Multi-QA-Sum dataset.
Type
#articles
#dialogues
#avg_turns
/dialogue
#total_words
in articles
#avg_words
/article
#total_tokens
in articles
#avg_tokens
/article
Zero-shot
467
2,755
5.90
203,606
435.99
276,708
592.52
#total_words
in questions
#avg_words
/question
#total_tokens
in questions
#avg_tokens
/question
#total_words
in answers
#avg_words
/answer
#total_tokens
in answers
#avg_tokens
/answer
24,767
8.99
33,967
12.33
43,165
15.67
58,176
21.12
#total_words in summaries
#avg_words /summary
#total_tokens in summaries
#avg_tokens /summary
28,167
60.31
37,309
79.89
NorGPT-369M to the 3B models. However, the en-
ergy consumption grows only with a factor of 2.5
(NorGPT-3B) and 2.1 (NorLlama-3B). When we
compare the 3B and 23B models, we have a growth
factor of only 7.7 in parameter size, but a growth
factor of 20.0 (NorGPT-3B vs. NorGPT-23B) and
24.6 (NorLlama-3B vs. NorGPT-23B) in energy
consumption.
Efficiency is also measured in downstream tasks.
For simplicity, we use NO-CNN/DailyMail bench-
mark and report run time in Table 12 to compare the
fine-tuning efficiency. To ensure fair comparison,
all models were fine-tuned on the same platform
on 4 A100 80G GPUs. We can observe that despite
having the same number of parameters, NorLlama-
3B is nearly 10 times slower than NorGPT-3B and
even lags behind NB-GPT-J-6B model in terms of
fine-tuning speed. However, such a pattern is not
common in other downstream tasks. It is worth
noting that the values of training parameters are
heavily conditioned on hardware and implementa-
tion details.
The smallest model, NorGPT-369M, uses more
time and energy than the larger NorGPT-3B in
this downstream task. We have a growth factor
of 34.2 when we compare the energy consumption
of NorGPT-3B and NorGPT-23B. This is signifi-
cantly larger than what we had in the pre-training
phase.
Table 11: Pre-training efficiency of NorGLMs. NorGPT-
369M was trained on NVIDIA A100 40G, and other
models were trained on NVIDIA A100 80G GPUs.
Metrics/Models
NorGPT-
369M
NorGPT-
3B
NorLlama-
3B
NorGPT-
23B
Time (h)
207.42
648.22
539.36
1893.75
Avg_FLOPS/step 4.28E+11
4.08E+11
-
6.91E+11
#Avg_samples/s
34.65
3.06
-
4.97
#Avg_steps/s
1.44
0.19
-
0.04
#Avg_tokens/s
3.29E+4
7.1E+3
4.41E+3
1.03E+4
#GPUs
6
4
4
28
TDP(W)
250
300
300
300
Energy
consum.(kWh)
492
1 229
1 023
25 134

--- Page 15 ---

Table 12: Experimental results on the efficiency of fine-tuning for news summarization tasks. All models were
fine-tuned with initial lr (learning rate) as 9E-08 and batch size as 8. Total training epoch is set to 1.
Metrics/Models
NorGPT-369M
NorGPT-3B
NorLlama-3B
NB-GPT-J-6B
NorGPT-23B
Time (h)
12.69
9.00
109.67
98.15
306.84
#Samples/s
1.339
1.888
0.31
0.173
0.055
#Steps/s
0.167
0.059
0.052
0.022
0.007
#GPUs
4
4
4
4
4
TDP(W)
300
300
300
300
300
Energy consum.(kWh)
24
17
208
186
581
Table 13: Experimental Results on the Instruction Finetuning Task.
Metrics/Models
NorGPT-369M
NorGPT-3B
NorLlama-3B
NorGPT-3B-continue
NorGPT-23B
NB-GPT-J-6B
BLEU
2.91
2.16
2.96
2.18
2.33
2.99
ROUGE-1
15.50
15.22
15.70
15.36
15.67
16.10
ROUGE-L
14.63
14.43
14.83
14.53
14.84
14.89
Dist-4
96.36
98.20
96.85
98.29
98.01
97.30
MAUVE
1.45
1.75
1.58
1.78
1.82
1.60
PPL
9.83
6.62
9.90
6.88
6.15
5.76
Table 14: Experimental Results on the NLU Tasks.
Datasets
Metrics
NorGPT-369M
NorGPT-3B
NorLlama-3B
NorGPT-3B-continue
NorGPT-23B
NB-GPT-J-6B
NO-BoolQ
Accuracy
58.6
60.6
56.2
58.5
63.2
56.7
F1 score
47.8
50.3
49.0
46.7
52.5
52.5
NO-QNLI
Accuracy
75.8
76.4
61.7
76.9
79.7
84.1
F1 score
75.7
76.3
61.7
76.8
79.7
84.1
NO-MRPC
Accuracy
71.0
68.8
66.8
69.5
73.7
71.7
F1 score
54.5
46.1
52.0
55.1
64.4
66.6
Table 15: Experimental Results on the Toxicity of Norwegian Generative Language Models. Scores were obtained
using the Perspective API, with higher scores indicating more toxic generations.
Metrics/Models
NorGPT-369M
NorGPT-3B
NorLlama-3B
NorGPT-3B-continue
NorGPT-23B
NB-GPT-J-6B
Toxicity
5.09
5.55
2.24
6.77
6.65
6.59
Severe toxicity
0.25
0.37
0.15
0.47
0.31
0.42
Identity attack
0.82
0.80
0.45
1.17
1.05
0.94
Insult
1.95
1.82
0.90
2.23
2.97
2.15
Profanity
2.59
2.76
1.44
3.53
2.99
3.60
Threat
2.21
2.82
1.22
3.50
2.66
2.75
Table 16: Experimental Results on the Bias of Norwegian Generative Language Models. Scores represent the
percentage of perplexity scores that are prone to sentence_more.
Bias types/Models
NorGPT-369M
NorGPT-3B
NorLlama-3B
NorGPT-3B-continue
NorGPT-23B
NB-GPT-J-6B
Race-color
52.6
50.8
53.1
49.8
49.8
57.5
Socioeconomic
42.6
44.2
45.3
44.2
45.3
37.9
Gender
48.4
47.8
50.3
48.1
44.4
42.2
Disability
47.7
44.6
47.7
43.1
41.5
43.1
Nationality
44.9
42.1
49.5
37.5
37.5
53.7
Sexual orientation
41.9
44.1
44.1
40.9
47.3
32.3
Physical appearance
45.8
45.8
38.9
48.6
43.1
38.9
Religion
32.4
32.4
36.0
29.7
34.2
34.2
Age
48.4
45.1
51.6
44.0
47.3
39.6
Politics
63.6
45.5
45.5
54.5
45.5
54.5

--- Page 16 ---

Figure 5: Example of Task One in the NO-Multi-QA-Sum benchmark.

--- Page 17 ---

Figure 6: English translation of the example of Task One in the NO-Multi-QA-Sum benchmark.

--- Page 18 ---

Figure 7: API appearance for multi-task benchmark annotation.
Figure 8: Instructions for the human evaluation of the quality of translated datasets in NLEBench.

```
