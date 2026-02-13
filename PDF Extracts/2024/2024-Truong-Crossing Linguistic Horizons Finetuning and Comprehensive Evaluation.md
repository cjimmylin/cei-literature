---
title: "2024-Truong-Crossing Linguistic Horizons Finetuning and Comprehensive Evaluation - PDF Extract"
source_pdf: "2024-Truong-Crossing Linguistic Horizons Finetuning and Comprehensive Evaluation.pdf"
pages: 51
extracted_at: "2026-02-13T09:50:28.745945"
---

# PDF Extract: 2024-Truong-Crossing Linguistic Horizons Finetuning and Comprehensive Evaluation

**Source PDF:** 2024-Truong-Crossing Linguistic Horizons Finetuning and Comprehensive Evaluation.pdf
**Total Pages:** 51

---

## Content

```
--- Page 1 ---

Crossing Linguistic Horizons: Finetuning and Comprehensive Evaluation
of Vietnamese Large Language Models
Sang T. Truong§∗Duc Q. Nguyen†∗Toan Nguyen†∗Dong D. Le†∗Nhi N. Truong§†∗
Tho Quan† Sanmi Koyejo§
§Stanford University †Ho Chi Minh City University of Technology, VNU-HCM
∗Equal contribution, Corresponding: nqduc@hcmut.edu.vn, sttruong@cs.stanford.edu
Abstract
Recent advancements in large language models
(LLMs) have underscored their importance in
the evolution of artificial intelligence. How-
ever, despite extensive pretraining on multi-
lingual datasets, available open-sourced LLMs
exhibit limited effectiveness in processing Viet-
namese. The challenge is exacerbated by the
absence of systematic benchmark datasets and
metrics tailored for Vietnamese LLM evalua-
tion. To mitigate these issues, we have fine-
tuned LLMs specifically for Vietnamese and
developed a comprehensive evaluation frame-
work encompassing 10 tasks and 31 metrics.
We observe that finetuning can help LLMs
transfer knowledge across languages, serving as
an efficient way to bolster their capabilities in
non-English languages. Moreover, our analysis
indicates that larger models can introduce more
biases and uncalibrated outputs and the key fac-
tor influencing LLM performance is the quality
of the training or finetuning datasets. These
insights underscore the significance of metic-
ulous finetuning with high-quality datasets in
enhancing LLM performance.
1
Introduction
Large language models (LLMs) such as GPT-
4 (OpenAI, 2023), BLOOM (Le Scao et al,
2023), LLaMa-2 (Touvron et al, 2023), Mis-
tral (Jiang et al., 2023), Mixtral (Jiang et al., 2024),
Gemma (Team et al., 2024) have made significant
contributions to the field of natural language pro-
cessing (NLP). Despite their advancements, a gap
remains in their specialization for many languages,
including Vietnamese. This paper addresses the
development and evaluation of Vietnamese-centric
LLMs. Vietnam, with a population surpassing 100
million, ranks as the 16th most populous coun-
try globally. Current models exhibit limitations in
effectively handling Vietnamese NLP tasks, espe-
cially in accurate comprehension and response (Lai
et al., 2023). Consequently, there is an increasing
demand for a robust, dedicated Vietnamese LLM.
Several factors constrain the practical applica-
tion of LLMs. Concerns regarding the precision,
inherent biases, potential toxicity, and fairness of
their outputs are notable obstacles (Ye et al., 2023;
Liang et al, 2023; Wang et al., 2024). Moreover,
there is a lack of research evaluating LLMs in the
Vietnamese context. To facilitate the effective use
of state-of-the-art LLMs for Vietnamese speakers,
thorough evaluations are essential prior to their
widespread use. Such evaluations not only ensure
the reliability of these LLMs but also highlight ar-
eas where these LLMs could be better. This leads to
developing targeted reinforcement learning strate-
gies to rectify these issues in the next phase.
In response to the aforementioned challenges,
we aim to develop open-source Vietnamese LLMs.
Initiating an LLM from scratch is impractical due
to the scarcity of extensive training datasets and
limited computational resources.
However, the
advent of QLoRA (Dettmers et al., 2023), incor-
porating quantization techniques (Dettmers et al.,
2022) and LoRA (Hu et al., 2022), provides an ef-
ficient approach for fine-tuning LLMs, particularly
in resource-constrained environments. We em-
ploy fine-tuning on the LLaMa-2, Mixtral 8×7B,
Gemma, and conduct a comprehensive evaluation
of Vietnamese LLMs across various scenarios and
settings. Throughout the thorough evaluation pro-
cess, we observe the following: (i) larger language
models exhibit unseen capabilities compared to
smaller counterparts; (ii) larger language models
tend to manifest more biases, produce uncalibrated
results, and are more susceptible to the influence
of input prompts; (iii) the quality of training or
fine-tuning datasets is the key for unlocking LLM
performance. Our key contributions include:
• The fine-tuning and release of five Viet-
namese LLMs: URA-LLaMa 7B, 13B, and 70B
based on LLaMa-2; MixSUra based on Mix-
arXiv:2403.02715v2  [cs.CL]  26 May 2024

--- Page 2 ---

tral 8×7B; GemSUra 7B based on Gemma 7B.
Our finetuning leverages data from the Viet-
namese Wikipedia (Foundation, 2022), Viet-
namese News-Corpus (Binh, 2021), and Viet-
namese Highschool Essays1.
• Conducting comprehensive evaluations of 14
Vietnamese LLMs across ten common appli-
cation scenarios, focusing on aspects such as
accuracy, robustness, fairness, bias, and toxicity.
Additional criteria are tailored to each specific
scenario. Our empirical research also explores
the influence of prompt design during inference.
• As part of this effort, we introduce and share two
novel Vietnamese reasoning datasets inspired by
MATH (Hendrycks et al., 2021) and Synthetic
reasoning (Wu et al., 2021).
2
Related Works
Vietnamese LLMs
To our best knowledge,
there are seven available Vietnamese LLMs: (i)
Vietcuna-7B-v3 (ViLM, 2023) – fine-tuned on
BLOOMZ (Muennighoff et al., 2023), open-
sourced, released on Aug. 8, 2023, (ii) Vistral 2 –
based on Mistral, open-sourced, (iii-iv) PhoGPT
7B5 & PhoGPT 7B5 Instruct (Nguyen et al., 2023a)
– based on MPT architecture (Team, 2023), open-
sourced, released on Nov. 7, 2023 (concurrently
with our work), (v) Gemini (Team et al., 2024)
– a commercial product of Google, and (vi-vii)
GPT3.5 Turbo & GPT-4, which are closed-source
commercial products on the Azure platform (ver-
sion 0613) (OpenAI, 2023). To our knowledge, we
are the first to fine-tune and release two large-scale
open-source Vietnamese LLMs with 13B, 70B
parameters and a Mixture-of-Expert Vietnamese
LLMs with 47B parameters.
Comprehensive
Evaluation
of
Vietnamese
LLMs
Evaluating a language model is challeng-
ing because LLMs can improve general capabil-
ities with scale. Thus, evaluating an LLM de-
pends on various factors, such as the tasks for
which the LLM will be used, and the impact of
prompt design, among others. Currently, there is
no evaluation framework capable of fully and ac-
curately assessing the abilities of a Vietnamese
LLM. Some recent studies on Vietnamese LLMs
only assess the model’s performance on closed-
book question-answering tasks (Nguyen et al.,
1Vietnamese Highschool Essays
2Vistral-7B-Chat
2023a) or specific datasets related to ad hoc as-
pects, such as law (Nguyen et al., 2023b; Anh et al.,
2023), physics (Xuan-Quy et al., 2023), and biol-
ogy (Dao and Le, 2023). Part of the challenge is
the lack of high-quality Vietnamese datasets. Viet-
namese NLP datasets have largely focused on daily
tasks such as open-book and closed-book question-
answering (Artetxe et al., 2020; Lewis et al., 2020),
summarization (Nguyen et al., 2019c; Ladhak et al.,
2020), translation (Zhang et al., 2020; Doan et al.,
2021), etc. Evaluation of some LLM capabilities,
such as reasoning and mathematical logic, have
not been considered due to the absence of suitable
datasets. We are the first to address this challenge
by comprehensively evaluating Vietnamese LLM
on 10 scenarios and 31 metrics. In that process,
we build and open-source two novel Vietnamese
reasoning datasets. Our evaluation framework is
open-source on Github3 to facilitate community-
driven model evaluation4.
3
Experiments
3.1
Supervised Finetuning
We focus on finetuning English-language mod-
els to enhance overall performance and evaluate
adaptability and efficiency in various configura-
tions. Due to computational constraints, our first
models, named URA-LLaMa, were finetuned from
LLaMa-2 using QLoRA (Dettmers et al., 2023)
on two primary open-source Vietnamese datasets,
including Vietnamese Wikipedia (1GB) and Viet-
namese News-Corpus (22GB). The 7B variant was
finetuned on both datasets, while the 13B and 70B
versions were finetuned with only the Vietnamese
Wikipedia dataset. The LoRA rank was set at 128
for the 7B model, 256 for the 13B model, and 1024
for the 70B model. Other hyperparameters, includ-
ing LoRA α, dropout, quantization, quantization
type, learning rate, max length, and epochs, were
uniformly set at 16, 0.1, 4 bit, NF4, 1 × 10−5,
2048, and 1, respectively. We use six A100 80GB
for the entire finetuning process in approximately
867 hours, emitting nearly 900 kg CO2 eq.
Continuously, we conducted finetuning on
Gemma 7B, and Mixtral 8×7B models utilizing
Vietnamese Wikipedia and Vietnamese Highschool
Essay datasets, employing the LoRA (Hu et al.,
2022). This refinement resulted in the development
of GemSUra 7B, and MixSUra models. Common
3https://github.com/stair-lab/villm
4https://ai.stanford.edu/~sttruong/villm

--- Page 3 ---

hyperparameters were applied across these mod-
els, with LoRA rank set to 256, LoRA α at 512,
and LoRA dropout rate fixed at 0.1. For the Gem-
SUra model, the learning rate, maximum sequence
length, and number of epochs were established at
1×10−5, 8192, and 2, respectively. Conversely, for
MixSUra, these hyperparameters were adjusted to
5×10−5, 32768, and 5. The finetuning process for
these two models required four A100 80GB GPUs,
spanning a total of 289 hours and resulting in the
emission of 200 kg CO2 equivalent. Our models
are available on HuggingFace5.
3.2
Evaluation Pipeline
We define a scenario as a real-world use case of
LLMs describing the purpose for which LLMs are
used. Modern LLMs can deal with various sce-
narios. We limit ten common use cases in Viet-
namese in this work. Each scenario contains two
well-known datasets in Vietnamese, which are al-
ready split into training and testing sets. We utilize
the testing set to evaluate our finetuned models,
LLaMa-2, Vietcuna, Vistral, PhoGPT, Gemini Pro,
GPT-3.5 Turbo, and GPT-4, considering their di-
verse performance and architectural differences for
a comprehensive analysis. Below are detailed de-
scriptions of 10 scenarios:
1. Question-Answering requires LLM to answer
an open-ended question from a given con-
text.
We selected two notable Vietnamese
datasets for diversity of evaluation domain:
XQuAD (Artetxe et al., 2020), a multilingual
variant of SQuAD (Rajpurkar et al., 2016),
and MLQA (Lewis et al., 2020), both based
on Wikipedia articles. Exact Match (EM) and
F1 score (F1) measure question-answering per-
formance. F1 Score is the harmonic mean of
Precision and Recall: F1 =
2×Precision×Recall
(Precision+Recall)
where Precision =
True Positive
True Positive+False Negative and
Recall =
True Positive
True Positive+False Negative.
2. Summarization involves LLMs condensing
long documents into shorter open-ended para-
graphs. We selected the two largest Vietnamese
summarization datasets:
VietNews (Nguyen
et al., 2019c) and WikiLingua (Ladhak et al.,
2020). VietNews comprises over 150,000 arti-
cles (22,644 for testing) from Vietnamese on-
line news websites. WikiLingua was chosen
for its variety, featuring diverse tutorials from
5https://huggingface.co/ura-hcmut
WikiHow (wikiHow, 2023). We primarily rely
on standard evaluation metrics like ROUGE-
1, ROUGE-2, and ROUGE-L (Liang et al,
2023).
ROUGE-1 (R1) measures the over-
lap of unigrams (individual words) between
the system-generated and reference summaries.
ROUGE-2 (R2) focuses on the overlap of bi-
grams, while ROUGE-L (RL) evaluates the
longest common subsequence between the two
summaries. Beyond these, we incorporate five
additional metrics from (Grusky et al., 2018) to
assess summary quality. These include Sum-
maC (SC), which assesses the faithfulness of
generated summaries; BERTScore (BS), which
uses mBERT token embeddings to compute the
cosine similarity between sentence tokens; Cov-
erage (Cv), measuring how much a summary
derives from the original text; Density (De), de-
fined as the average length of extractive frag-
ments associated with each summary word; and
Compression (Cp), which is the word ratio be-
tween original articles and their summaries.
3. Sentiment Analysis focuses on detecting emo-
tion of documents. Given a document and a list
of all available sentiments, the LLM must choose
the correct ones.
The first selected dataset,
VLSP 2016 (Nguyen et al., 2019b), contains
comments on social networks about electronic
devices such as smartphones, laptops, televi-
sion, etc. The next dataset, UiT-VSFC (Nguyen
et al., 2018), is feedback from Vietnamese stu-
dents about courses at the end of semesters.
We use Accuracy (AC), F1, AUC ROC (AR),
Expected Calibration Error (ECE), and Accu-
racy at C% coverage (A@C) for model assess-
ment. AC = True Positive+True Negative
Number of Instances
. AUC ROC
quantifies the model ability to distinguish be-
tween classes by measuring the area under the
ROC curve. A perfect model would have an
AUC ROC score of 1, while a score below
0.5 indicates a model performing worse than
random. Expected calibration error (ECE) de-
scribed in (Guo et al., 2017) measures the dif-
ference between the model predicted probability
and the fraction of times the model is correct.
As a default configuration, we use ten bins, each
containing an equal number of predicted prob-
abilities. Accuracy at C% coverage is the accu-
racy for the C% fraction of examples the model
assigns the highest probability. Details of this
metric can be found at (Liang et al, 2023). In

--- Page 4 ---

our experiment, C is set to 10%.
4. Text Classification is a scenario where the
LLMs are required to analyze the input doc-
ument with a list of class labels and give the
answer of which class that document belongs
to. This scenario is a classical task in almost all
languages, including Vietnamese. Thus, various
datasets in different fields are available. How-
ever, evaluating all those datasets may not be fea-
sible, so we choose two large and reliable ones
in this study, which are UiT-VSMEC (Ho et al.,
2020) and PhoATIS (Dao et al., 2021). UiT-
VSMEC is specified for emotion recognition of
Vietnamese comments on Facebook, the most-
used social network in Vietnam. PhoATIS is the
human-verified Vietnamese version of the fa-
mous standard ATIS dataset (Price, 1990), spec-
ified for classification intents of user requests
about airline information. Here, we use AC, F1,
AR, ECE, and A@C for model assessment.
5. Knowledge assesses LLMs common knowledge
specified for Vietnamese. We use the two largest
datasets: ZaloE2E (Zalo AI, 2023) and UiT-
ViMMRC (Nguyen et al., 2020b). ZaloE2E has
open-ended questions. UiT-ViMMRC contains
reading comprehension multiple-choice ques-
tions for students from Grades 1-12 in Vietnam.
This task uses AC, F1, EM, AR, ECE, and A@C
for model assessment.
6. Toxicity Detection requires the LLMs to detect
toxicity in a paragraph, such as toxic purpose
or hate speech. We choose the two most recent
datasets: UiT-ViCTSD (Nguyen et al., 2021) and
UiT-ViHSD (Luu et al., 2021) in this scenario.
The UiT-ViCTSD dataset specifically targets the
discernment of toxic speech, while UiT-ViHSD
centers on identifying instances of hate speech.
In this task, we use accuracy, F1 score, and AUC
ROC for model assessment.
7. Information Retrieval is a task that ranks a
list of relevant documents in the database given
the query. We chose the two most recent mul-
tilingual datasets supporting Vietnamese. The
first is the mMARCO dataset (Bonifacio et al.,
2022), a multilingual version of the well-known
MS MARCO dataset (Nguyen et al., 2016). The
other mRobust04 (Jeronymo et al., 2022) is also
a multilingual of TREC Robust 2004.
Fol-
lowing (Liang et al, 2023), we have two set-
tings: normal and boosted. In the normal set-
ting, we employ the top 30 documents retrieved
by BM25 (Amati, 2009). Conversely, in the
boosted setting, we include relevant documents
beyond the top 30 retrieved by BM25. Our in-
quiry tasks an LLM to determine the relevance
of each document. Subsequently, we reorga-
nize the documents based on their relevance
probabilities, ranking them from the highest
probability of relevance to the highest proba-
bility of non-relevance. Several metrics are em-
ployed to assess model performance. We use
a more stringent variant of Mean Reciprocal
Rank (MRR), Mean Reciprocal Rank in top-K
(M@K), which disregards samples ranked lower
than a predetermined threshold (K, set to 10 in
our experiments). M@K = 1/rank if rank ≤K
and M@K = 0 otherwise. Additionally, we
consider the Normalized Discounted Cumula-
tive Gain in top-K (N@K), a metric focusing
on relevance beyond binary assessments. Cu-
mulative Gain in top-K (CG@K) measures the
total relevance value within the top K docu-
ments. In contrast, Discounted Cumulative Gain
(DCG@K) adds positional weight to the rele-
vance scores, prioritizing documents that ap-
pear higher in the ranking. DCG@K is com-
puted as DCG@K = PK
i=1
graded_relevance(di)
log2(i+1)
.
Finally, N@K normalizes DCG@K against the
Ideal Discounted Cumulative Gain (IDCG@K),
representing the maximum achievable DCG@K
score with ideally ordered documents. GPT fam-
ily and Gemini are not evaluated in this scenario
because OpenAI and Google hav disabled proba-
bilities in their response (Azure announcement).
8. Language Modeling assesses LLMs’ under-
standing and fluency in a specific language
through tasks, notably filling in the blanks
and spelling correction. For masked language
modeling, we utilized the formal-styled MLQA
dataset, masking 10% of words in each doc-
ument for LLMs to predict. We selected the
VSEC dataset (Do et al., 2021) to evaluate
spelling correction constructed from news
articles with more modification operators than
previous datasets. Various metrics are employed
for evaluation.
Exact Match (EM) assesses
the precise word-level match rather than the
entire sentence. Character Error Rate (CER)
and Word Error Rate (WER) represent the
proportion of inaccurately predicted characters

--- Page 5 ---

and words compared to references, respectively.
The Character Edit Distance (CED), also known
as the Levenshtein distance, measures the
minimum operations (insertions, deletions, or
substitutions) needed to transform one character
string into another. The Word Edit Distance
(WED) is similar to CER but operates at
the word level.
Finally, Perplexity (PLX) is
defined as the exponentiated average negative
log-likelihood of a sequence of T-token:
PLX
=
exp

−1
T
PT
i=0 log pθ(xi|x<i)

,
where pθ(xi|x<i) is the probability of the ith
token conditioned on preceding ones.
9. Reasoning involves evaluating LLMs’ logical
and mathematical capabilities. Because Viet-
namese lacks datasets for reasoning, we adapted
two well-known datasets—Synthetic reason-
ing (Wu et al., 2021) and MATH (Hendrycks
et al., 2021)—for this purpose. We created Viet-
namese versions of these datasets by translating
their English versions using Google Paid API
and Azure Translation, focusing on natural lan-
guage reasoning, abstract symbol reasoning, and
mathematical ability. These datasets are com-
patible with the original license and are open-
sourced on HuggingFace6. We use EM and F1 to
measure the reasoning performance. Equivalent
is used as a metric to assess whether the results
given by LLM are equivalent to the reference.
The evaluation results of this scenario are re-
ported as the average of two translated versions.
10. Translation involves translating documents
from Vietnamese to English and the reverse
while preserving the original meaning. We se-
lected the two most extensive and high-quality
datasets: OPUS100 (Zhang et al., 2020) and
PhoMT (Doan et al., 2021). Two key metrics
are employed to ensure translation accuracy.
The Bilingual Evaluation Understudy (BLEU)
score (Papineni et al., 2002) measures the sim-
ilarity of a translation to reference translations,
with values closer to 1 indicating higher simi-
larity. On the other hand, the Harmonic mean
of Enhanced Length Penalty, Precision, n-gram
Position-difference Penalty, and Recall (hLE-
POR) (Han et al., 2013) assesses the similarity
of n-grams between the translation and refer-
ences. The hLEPOR score also ranges from 0 to
6Synthetic reasoning natural; Synthetic reasoning; MATH
1, where a higher score signifies a more closely
aligned translation with the references.
We design a base prompt for each scenario that
asks the LLMs to perform the desired task with-
out any examples or constraints.
Recent stud-
ies (Zhao et al., 2021; Wei et al., 2022) have
demonstrated that LLMs perform better if care-
fully prompted. Therefore, we design additional
prompts for some specific scenarios to test whether
the LLMs perform better with provided exam-
ples (few-shot learning or in-context learning),
whether LLMs perform worse with weak prompts,
or whether the LLMs outputs are polite and less
biased with constraints input. Details of prompts
for each scenario are provided in Appendix G.
4
Results and Discussion
We present the overall capacities of evaluated
LLMs in Figure 1, separating commercial and
open-sourced models across six aspects, includ-
ing general performance, robustness under weaker
prompts, performance with Chain-of-Thought
(COT), ability to deal with unfair input (fairness)
and toxicity, bias in generated outputs. Each as-
pect is quantified by the average score of the model
across all evaluated scenarios within that aspect.
For each scenario, we present the standard devia-
tion for each metric by using bootstrapping (Efron
and Tibshirani, 1993), wherein the process involves
(i) drawing random samples with replacement from
the original dataset, (ii) computing the metric for
each sampled subset and (iii) iteratively repeating
steps (i) and (ii) for a total of 1000 iterations to
ascertain the standard deviation across these repe-
titions.
Overall, GPT-4 demonstrates the highest perfor-
mance across all tasks. However, the GPT family
exhibits more biases than the others. Our finetuned
models outperform their base model, LLaMa-2.
This is expected as they are finetuned explicitly
on Vietnamese datasets, enhancing their ability to
understand the language. Additionally, we have ob-
served that the abilities of LLMs do not solely de-
pend on model parameters but also on their training
or finetuning datasets. For example, in Figure 2, in
the summarization scenario, URA-LLaMa 7B and
70B have almost the same performance. A similar
phenomenon also occurs in the language modeling
scenario, where URA-LLaMa 13B has a lower er-
ror rate than the 70B version. Larger models do not
always guarantee better performance and might per-

--- Page 6 ---

form worse than smaller ones if not trained on these
specific data types. Indeed, employing a larger lan-
guage model does not inherently ensure heightened
performance. The crux for a good LLM lies in the
discerning selection of the number of parameters
and training or finetuning datasets.
General task
COT
Fairness
Robustness
Unbias
Safety
URA-LLaMa 70B
URA-LLaMa 13B
URA-LLaMa 7B
MixSUra
GemSUra
LLaMa-2 70B
LLaMa-2 13B
LLaMa-2 7B
Vietcuna 7B
Vistral 7B Chat
Gemini Pro
GPT-3.5
GPT-4
Figure 1: Overall capacities of LLMs
4.1
Inside of finetuning process
Our research indicates that establishing a founda-
tional Large Language Model may not necessitate
a vast amount of data, provided appropriate fine-
tuning techniques are employed. Empirical evi-
dence (Figure 2, 3, and 6) suggests that utilizing
solely the Vietnamese Wikipedia dataset yields sig-
nificant performance for our URA-LLaMa 70B
and MixSUra models. Given that Vietnamese is
categorized as a low-resource language, amassing
an extensive dataset for constructing highly robust
LLMs is impractical. This phenomenon can be at-
tributed to the model’s capacity to transfer knowl-
edge across languages, capitalizing on pre-existing
linguistic patterns and structures acquired from
other languages. However, among all the models
we evaluated, PhoGPT (building vocabulary and
being trained from scratch) and Vistral (expanding
vocabulary and continuously finetuning) excel in
question-answering and summarization but strug-
gle in other tasks and/or severe scenarios involving
fairness, robustness, and toxicity concerns. This is
because building tokenizers from scratch or adding
language-specific tokens limits knowledge trans-
fer from English, and these models might not be
trained in these scenarios. Thus, continuous fine-
tuning from a good pretrained model is the best
choice for low-resource languages.
4.2
General Performance
Under Zero-shot Prompt:
According to Fig-
ure 2, GPT-4 achieves the best overall perfor-
mance among all models across all scenarios, while
URA-LLaMa 70B version achieves the best results
among open-sourced models. The results also in-
dicate that larger models achieve better-calibrated
results with the zero-shot prompt. However, GPT
models tend to have higher calibration errors than
the rest, which makes their responses less reliable.
0.00
0.17
0.34
GPT-4
GPT-3.5
Gemini Pro
GemSUra
MixSUra
PhoGPT 7B5 Instruct
Vistral 7B Chat
Vietcuna 7B
LLaMa-2 7B
LLaMa-2 13B
LLaMa-2 70B
URA-LLaMa 7B
URA-LLaMa 13B
URA-LLaMa 70B
Question-Answering
F1 
0.00
0.17
0.34
Summarization
R1 
0.00
0.25
0.50
0.75
Sentiment Analysis
F1 
0.00
0.25
0.50
0.75
Text Classification
F1 
0.00
0.25
0.50
0.75
GPT-4
GPT-3.5
Gemini Pro
GemSUra
MixSUra
Vistral 7B Chat
Vietcuna 7B
LLaMa-2 7B
LLaMa-2 13B
LLaMa-2 70B
URA-LLaMa 7B
URA-LLaMa 13B
URA-LLaMa 70B
Knowledge
F1 
0.00
0.25
0.50
0.75
Toxic Detection
F1 
0
1
2
3
Language Modeling
WER 
0.00
0.17
0.34
Reasoning
Equivalent 
Figure 2: Performance on zero-shot prompt
Under Few-shot Prompt:
We introduce few-shot
examples into the input prompt to guide the models.
As detailed in Figure 3, GPT-4 exhibits superior
overall performance, followed closely by GPT-3.5.
Notably, GPT-3.5 demonstrates performance nearly
equivalent to GPT-4 when using few-shot prompt-
ing. Furthermore, our observations suggest that
larger models may be susceptible to the influence
of few-shot examples, resulting in increased cali-
bration errors. This further indicates that the indis-
criminate use of few-shot prompting does not uni-
versally guarantee enhanced performance or more
dependable results.
0.00
0.25
0.50
0.75
GPT-4
GPT-3.5
Gemini Pro
GemSUra
MixSUra
Vistral 7B Chat
Vietcuna 7B
LLaMa-2 7B
LLaMa-2 13B
LLaMa-2 70B
URA-LLaMa 7B
URA-LLaMa 13B
URA-LLaMa 70B
Sentiment Analysis
F1 
0.00
0.25
0.50
0.75
Text Classification
F1 
0.00
0.25
0.50
0.75
Knowledge
F1 
0.00
0.25
0.50
0.75
Toxic Detection
F1 
0
2
4
6
GPT-4
GPT-3.5
Gemini Pro
GemSUra
MixSUra
Vistral 7B Chat
Vietcuna 7B
LLaMa-2 7B
LLaMa-2 13B
LLaMa-2 70B
URA-LLaMa 7B
URA-LLaMa 13B
URA-LLaMa 70B
Language Modeling
WER 
0.00
0.17
0.34
Reasoning
Equivalent 
0.00
0.08
0.16
0.24
Information Retrieval
N@10 
0.00
0.17
0.34
Translation
BLEU 
Figure 3: Performance with few-shot prompt

--- Page 7 ---

Under Chain-of-Thought Prompt:
This setting
is employed only for the MATH dataset. Figure 4
reveals the huge-improved performance of LLM
when being guided step-by-step.
0.0
0.5
1.0
GPT-4
GPT-3.5
Gemini Pro
GemSUra
MixSUra
Vistral 7B Chat
Vietcuna 7B
LLaMa-2 7B
LLaMa-2 13B
LLaMa-2 70B
URA-LLaMa 7B
URA-LLaMa 13B
URA-LLaMa 70B
MATH with COT
Equivalent 
Figure 4: Performance with Chain-of-Thought prompt
4.3
Performance under Stress
Under Weaker Prompts:
In real-life scenarios,
users may not always provide clear instructions. To
investigate model capacities in handling such situ-
ations, we introduce two additional prompt styles:
medium prompt and weak prompt. Medium prompt
exclusively includes instructions for the target sce-
nario without specifying any requirements con-
cerning social aspects. Weak prompt lacks explicit
instructions but includes a phrase indicating the
purpose of the target generation.
We conduct testing under two scenarios:
question-answering and summarization. The re-
sults (Figure 5) unveil an intriguing observation:
weaker prompts may yield superior evaluation met-
rics. This phenomenon can be attributed to weaker
prompts exclusively providing instructions with-
out additional constraints, compelling the LLMs
to focus solely on the target tasks. Conversely,
in the case of strong prompts, which encompass
safety, bias considerations, and other constraints,
the LLMs modify their responses to adhere to
these stipulations, resulting in diminished evalua-
tion metrics.
0.00
0.17
0.34
GemSUra
MixSUra
Vistral 7B Chat
LLaMa-2 7B
LLaMa-2 13B
LLaMa-2 70B
URA-LLaMa 7B
URA-LLaMa 13B
URA-LLaMa 70B
Question-Answering
Weak Prompting
F1 
0.00
0.17
0.34
Summarization
Weak Prompting
R1 
0.00
0.17
0.34
Question-Answering
Medium Prompting
F1 
0.00
0.17
0.34
Summarization
Medium Prompting
R1 
Figure 5: Performance under weaker prompt
Under Typographical Error:
We made four
types of modifications to the input prompts to as-
sess the resilience of LLMs against varied inputs.
First, we added typos in 10% of the words uni-
formly across the document. These typos encom-
pass five categories: common Vietnamese typos as
identified in the Viwiki-Spelling (Tran et al., 2021)
and VSEC (Do et al., 2021) datasets, character
duplication, random character deletion, swapping
of two consecutive characters, and Vietnamese-
diacritic removal. These variations are designed
to replicate frequent typing errors. Secondly, the
spacing was altered by randomly replacing each
space in the text with 1-3 spaces. Thirdly, we con-
verted the entire text to lowercase. Lastly, we trans-
formed all numerical digits in the datasets into their
corresponding textual representations.
In this setting, we conduct tests across seven
scenarios, excluding Language Modeling, Informa-
tion Retrieval, and Reasoning, as these necessitate
unmodified input to assess model performance in
those scenarios accurately. Figure 6 delineates the
results for this setting. Notably, typographical er-
rors affect all models except for the GPT family.
This observation suggests that the GPT family may
have been trained on data augmented with typo-
graphical errors, enhancing its capacity to handle
such instances. Furthermore, our analysis reveals
that larger models exhibit a marginal increase in
susceptibility to typographical errors compared to
their smaller counterparts.
0.00
0.17
0.34
GPT-4
GPT-3.5
Gemini Pro
GemSUra
MixSUra
Vistral 7B Chat
Vietcuna 7B
LLaMa-2 7B
LLaMa-2 13B
LLaMa-2 70B
URA-LLaMa 7B
URA-LLaMa 13B
URA-LLaMa 70B
Question-Answering
F1 
0.00
0.17
0.34
Summarization
R1 
0.00
0.25
0.50
0.75
Sentiment Analysis
F1 
0.00
0.25
0.50
0.75
Text Classification
F1 
0.00
0.25
0.50
0.75
GPT-4
GPT-3.5
Gemini Pro
GemSUra
MixSUra
Vistral 7B Chat
Vietcuna 7B
LLaMa-2 7B
LLaMa-2 13B
LLaMa-2 70B
URA-LLaMa 7B
URA-LLaMa 13B
URA-LLaMa 70B
Knowledge
F1 
0.00
0.25
0.50
0.75
Toxic Detection
F1 
0.00
0.08
0.16
0.24
Translation
BLEU 
Figure 6: Performance under typographical errors
Under Order Randomization:
To assess the in-
fluence of answer order variation on model per-
formance in multiple-choice questions, we employ
a random rearrangement of the order of all input
multiple-choice answers. This experimental inves-
tigation is executed within the Knowledge scenario,
utilizing the UiT-ViMMRC dataset and incorpo-

--- Page 8 ---

rating few-shot prompting. The test is iteratively
performed three times, each with distinct seeds.
Figure 7 presents the aggregated outcomes
across the trials. Examination of this table reveals
that, except for Vietcuna, all models can accommo-
date variations in answer order, yielding consistent
performance across different run times.
0.0
0.5
1.0
GPT-4
GPT-3.5
Gemini Pro
GemSUra
MixSUra
Vistral 7B Chat
Vietcuna 7B
LLaMa-2 7B
LLaMa-2 13B
LLaMa-2 70B
URA-LLaMa 7B
URA-LLaMa 13B
URA-LLaMa 70B
ViMMRC
F1 
Figure 7: Performance under randomized orders
4.4
Beyond Performance: Fairness, Bias, and
Toxicity
Fairness:
To examine the fairness of LLM,
we implemented two modifications to the input
prompts related to race and gender while maintain-
ing the original system instruction and in-context
examples. Additionally, we adjusted the answer la-
bels to correspond with the revised input prompts.
The race effect is investigated by converting
Western names to Vietnamese ones in two steps.
Initially, a pre-trained Named Entity Recognition
model is used to detect all person names, and then
Western names are identified by the absence of
Vietnamese diacritics. Subsequently, a dictionary
is constructed to convert these Western names to
Vietnamese equivalents (Long, 2023).
The gender effect is studied by replacing the
most frequently used terms and pronouns with fe-
male equivalents. The most frequently used terms
and pronouns are inherited from (Liang et al, 2023)
and translated into Vietnamese:
• General: con cái, trẻem, đứa trẻ, anh chịem,
hoàng đế, vua, người phục vụ, cha mẹ, ba mẹ,
phụhuynh, bốmẹkế, ba mẹkế, cha mẹkế,
cháu, họ, người ta, con người, con nuôi, giáo
viên, giảng viên
• Male: con trai, cậu bé, anh trai, nam hoàng
đế, nam phục vụ, cha, ba, bố, cha dượng, ba
dượng, bốdượng, cháu trai, anh, hắn, ông,
chú, đàn ông, nam, con trai nuôi, thầy
• Female: con gái, cô gái, chịgái, nữhoàng, nữ
phục vụbàn, mẹ, mẹkế, cháu gái, bà, cô, mụ,
nàng, chị, phụnữ, nữ, con gái nuôi, cô giáo
In our experiment (Figure 8), we examine five
scenarios, omitting Reasoning, Summarization,
Knowledge, Information Retrieval, and Translation
due to possible semantic alterations that could af-
fect the accuracy. The findings indicate that LLMs
proficiency extends to handling context changes,
suggesting its adaptability for diverse contexts tai-
lored to distinct target purposes or individuals.
0.00
0.17
0.34
GPT-4
GPT-3.5
Gemini Pro
GemSUra
MixSUra
Vistral 7B Chat
Vietcuna 7B
LLaMa-2 7B
LLaMa-2 13B
LLaMa-2 70B
URA-LLaMa 7B
URA-LLaMa 13B
URA-LLaMa 70B
Question-Answering
F1 
0.00
0.25
0.50
0.75
Sentiment Analysis
F1 
0.00
0.25
0.50
0.75
Text Classification
F1 
0.00
0.25
0.50
0.75
Toxic Detection
F1 
0.00
1.33
2.66
3.99
Language Modeling
WER 
Figure 8: Performance in fairness aspect
Bias:
We examine bias from two distinct angles:
demographic representation and stereotypical as-
sociations. Demographic representation refers to
disparities in the frequency with which various de-
mographic groups (gender and race) are mentioned.
Stereotypical associations are a modification of de-
mographic representation. It measures biases that
are linked to a particular concept. Our experiment
measures the bias in the occupation for each demo-
graphic group. More details of the metric can be
found at (Liang et al, 2023).
This setting involves three tasks where the re-
sponses generated by LLMs with few-shot prompt-
ing are open-ended. The outcomes presented in
Figure 9 suggest that larger models can sometimes
exhibit more bias compared to their smaller coun-
terparts. Further analysis, in conjunction with in-
sights from Figure 3, suggests that achieving im-
proved performance necessitates model adherence
to certain anchor words, particularly those related
to gender and race. It becomes evident that the
presence of these anchor words significantly influ-
ences the output response, and this effect amplifies
with an increase in model parameters.
0.0000
0.1667
0.3333
0.5000
GPT-4
GPT-3.5
Gemini Pro
GemSUra
MixSUra
Vistral 7B Chat
Vietcuna 7B
LLaMa-2 7B
LLaMa-2 13B
LLaMa-2 70B
URA-LLaMa 7B
URA-LLaMa 13B
URA-LLaMa 70B
Question-Answering
DRG 
0.0000
0.1667
0.3333
0.5000
Summarization
DRG 
0.0000
0.0833
0.1667
0.2500
Translation
DRG 
Figure 9: Demographic Representation on Gender

--- Page 9 ---

Toxicity:
We trained a toxicity detection model
to predict the likelihood of toxicity in the LLM
outputs in the task of Question-Answering, Sum-
marization, and Translation. Our model utilizes
the ViT5-base (Phan et al., 2022) architecture on
UiT-ViCTSD (Luu et al., 2021) training set. We
evaluate our toxicity detection model with other
well-known ones on the UiT-ViCTSD testing set
(Table 3). We use average predicted toxic prob-
ability to measure the toxicity of the generative
samples from the LLM.
This setting is also implemented across three
scenarios involving open-ended responses. The
findings (Figure 10) indicate that larger models are
challenging to control regarding toxicity in their
generated responses. Additionally, our observa-
tions highlight the role of training or finetuning
datasets as a causative factor in inducing toxicity.
Consequently, efforts to mitigate toxicity can be
initiated by implementing measures to control the
composition of those datasets.
0.0000
0.0167
0.0333
0.0500
GPT-4
GPT-3.5
Gemini Pro
GemSUra
MixSUra
Vistral 7B Chat
Vietcuna 7B
LLaMa-2 7B
LLaMa-2 13B
LLaMa-2 70B
URA-LLaMa 7B
URA-LLaMa 13B
URA-LLaMa 70B
Question-Answering
Toxicity 
0.0000
0.0167
0.0333
0.0500
Summarization
Toxicity 
0.0000
0.0333
0.0667
0.1000
Translation
Toxicity 
Figure 10: Toxicity on generation taks
5
Limitations, Risks and Future
Directions
While pioneering in finetuning open-sourced Viet-
namese LLMs, our study encounters several limita-
tions. Firstly, our evaluation, especially for closed-
source models like GPT4 and open-sourced models
but unpublished data like Vistral, might be biased
due to the potential contamination of datasets used
for training and evaluation. Dataset contamination,
where training data inadvertently includes informa-
tion from test sets or biased samples, can lead to
overestimated performance and models that do not
generalize well to real-world scenarios. Secondly,
the scope of finetuning is restricted to the Viet-
namese language, which might not generalize to
other low-resource languages. Thirdly, the evalua-
tion, though comprehensive, is limited by the qual-
ity and diversity of available Vietnamese datasets.
The current datasets may not capture the complete
spectrum of linguistic nuances and cultural con-
texts inherent in the Vietnamese language. Finally,
our study’s reproducibility and scalability might
be constrained by the computational resources re-
quired for training and finetuning such large-scale
models.
While our finetuned LLM demonstrates profi-
ciency across diverse scenarios in toxicity and bias
testing, its application in real-world scenarios does
not guarantee the absence of bias or toxicity. Ad-
ditionally, the model’s knowledge is confined to
datasets comprising news and Wikipedia articles
collected before 2022, potentially leading to re-
sponse inaccuracies. Therefore, prudent handling
of toxicity, bias, and verification of answers is ad-
vised when utilizing our LLM in real applications.
Future research should aim to extend the fine-
tuning process to other low-resource languages,
thereby enhancing the multilingual capabilities
of LLMs.
Efforts should also be made to de-
velop more comprehensive and culturally rich Viet-
namese datasets, covering a broader range of lin-
guistic scenarios and domains. Additionally, inves-
tigating the model’s limitations in understanding
cultural nuances and idiomatic expressions could
lead to more refined and context-aware language
models. Finally, there is a need for more efficient
training and finetuning methodologies that reduce
computational costs while maintaining or improv-
ing model performance. This would make large-
scale LLMs more accessible to a broader research
community and facilitate diverse and innovative
applications in natural language processing.
Acknowledgements
Sanmi Koyejo is partially supported by NSF
III 2046795, IIS 1909577, CCF 1934986, NIH
1R01MH116226-01A, NIFA award 2020-67021-
32799, the Alfred P. Sloan Foundation, and
Google Inc.
Tho Quan is funded by Vietnam
National Foundation for Science and Technology
Development (NAFOSTED) under grant number
IZVSZ2.203310.
Duc Q. Nguyen was funded
by the Master, PhD Scholarship Programme of
Vingroup Innovation Foundation (VINIF), code
VINIF.2022.ThS.023. This study is supported by
the Microsoft Accelerating Foundation Models Re-
search program. We acknowledge Stanford Univer-
sity and Ho Chi Minh City University of Technol-
ogy (HCMUT) - VNU-HCM for supporting this
study. We also acknowledge DSciLab (HCMUT
- VNU-HCM) for providing partial computing re-
sources used in this study.

--- Page 10 ---

References
Giambattista Amati. 2009.
BM25, pages 257–260.
Springer US, Boston, MA.
Dang Hoang Anh, Dinh-Truong Do, Vu Tran, and
Nguyen Le Minh. 2023. The impact of large lan-
guage modeling on natural language processing in
legal texts: A comprehensive survey. In 2023 15th
International Conference on Knowledge and Systems
Engineering (KSE), pages 1–7.
Mikel Artetxe, Sebastian Ruder, and Dani Yogatama.
2020. On the cross-lingual transferability of mono-
lingual representations. In Proceedings of the 58th
Annual Meeting of the Association for Computational
Linguistics, pages 4623–4637, Online. Association
for Computational Linguistics.
Quoc Vuong Binh. 2021. Binhvq News Corpus.
Piotr Bojanowski, Edouard Grave, Armand Joulin, and
Tomas Mikolov. 2017. Enriching Word Vectors with
Subword Information. Transactions of the Associa-
tion for Computational Linguistics, 5:135–146.
Luiz Bonifacio,
Vitor Jeronymo,
Hugo Queiroz
Abonizio, Israel Campiotti, Marzieh Fadaee, Roberto
Lotufo, and Rodrigo Nogueira. 2022. mmarco: A
multilingual version of the ms marco passage ranking
dataset.
Corinna Cortes and Vladimir Vapnik. 1995. Support-
vector networks. Machine learning, 20(3):273–297.
D. R. Cox. 1958. The regression analysis of binary
sequences. Journal of the Royal Statistical Society.
Series B (Methodological), 20(2):215–242.
Mai Hoang Dao, Thinh Hung Truong, and Dat Quoc
Nguyen. 2021. Intent Detection and Slot Filling for
Vietnamese. In Proc. Interspeech 2021, pages 4698–
4702.
Xuan-Quy Dao and Ngoc-Bich Le. 2023. Llms per-
formance on vietnamese high school biology exami-
nation. International Journal of Modern Education
and Computer Science (IJMECS), 15(6):14–30.
Tim Dettmers, Mike Lewis, Sam Shleifer, and Luke
Zettlemoyer. 2022. 8-bit optimizers via block-wise
quantization. In International Conference on Learn-
ing Representations.
Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, and
Luke Zettlemoyer. 2023. QLoRA: Efficient finetun-
ing of quantized LLMs. In Thirty-seventh Conference
on Neural Information Processing Systems.
Dinh-Truong Do, Ha Thanh Nguyen, Thang Ngoc Bui,
and Hieu Dinh Vo. 2021. Vsec: Transformer-based
model for vietnamese spelling correction. In PRICAI
2021: Trends in Artificial Intelligence, pages 259–
272, Cham. Springer International Publishing.
Long Doan, Linh The Nguyen, Nguyen Luong Tran,
Thai Hoang, and Dat Quoc Nguyen. 2021. PhoMT:
A high-quality and large-scale benchmark dataset for
Vietnamese-English machine translation. In Pro-
ceedings of the 2021 Conference on Empirical Meth-
ods in Natural Language Processing, pages 4495–
4503, Online and Punta Cana, Dominican Republic.
Association for Computational Linguistics.
Bradley Efron and Robert Tibshirani. 1993. An Intro-
duction to the Bootstrap. Chapman & Hall/CRC,
Boca Raton, FL.
Wikimedia Foundation. 2022. Wikimedia downloads.
Max Grusky, Mor Naaman, and Yoav Artzi. 2018.
Newsroom: A dataset of 1.3 million summaries with
diverse extractive strategies. In Proceedings of the
2018 Conference of the North American Chapter of
the Association for Computational Linguistics: Hu-
man Language Technologies, Volume 1 (Long Pa-
pers), pages 708–719, New Orleans, Louisiana. As-
sociation for Computational Linguistics.
Chuan Guo, Geoff Pleiss, Yu Sun, and Kilian Q. Wein-
berger. 2017. On calibration of modern neural net-
works. In Proceedings of the 34th International Con-
ference on Machine Learning - Volume 70, ICML’17,
page 1321–1330. JMLR.org.
Aaron L.-F. Han, Derek F. Wong, Lidia S. Chao,
Liangye He, Yi Lu, Junwen Xing, and Xiaodong
Zeng. 2013. Language-independent model for ma-
chine translation evaluation with reinforced factors.
In Machine Translation Summit XIV, pages 215–222.
International Association for Machine Translation.
Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul
Arora, Steven Basart, Eric Tang, Dawn Song, and
Jacob Steinhardt. 2021. Measuring mathematical
problem solving with the MATH dataset. In Thirty-
fifth Conference on Neural Information Processing
Systems Datasets and Benchmarks Track (Round 2).
Vong
Anh
Ho,
Duong
Huynh-Cong
Nguyen,
Danh Hoang Nguyen, Linh Thi-Van Pham, Duc-Vu
Nguyen, Kiet Van Nguyen, and Ngan Luu-Thuy
Nguyen. 2020. Emotion recognition for vietnamese
social media text.
In Computational Linguistics,
pages 319–333, Singapore. Springer Singapore.
Sepp Hochreiter and J¨urgen Schmidhuber. 1997. Long
short-term memory. Neural computation, 9(8):1735–
1780.
Edward J Hu, yelong shen, Phillip Wallis, Zeyuan Allen-
Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu
Chen. 2022. LoRA: Low-rank adaptation of large
language models. In International Conference on
Learning Representations.
Vitor Jeronymo, Mauricio Nascimento, Roberto Lotufo,
and Rodrigo Nogueira. 2022. mrobust04: A multi-
lingual version of the trec robust 2004 benchmark.
Albert Q. Jiang, Alexandre Sablayrolles, and An-
toine Roux et al. 2024. Mixtral of experts.

--- Page 11 ---

Albert
Q.
Jiang,
Alexandre
Sablayrolles,
and
Arthur Mensch et al. 2023. Mistral 7b.
Faisal Ladhak, Esin Durmus, Claire Cardie, and Kath-
leen McKeown. 2020. WikiLingua: A new bench-
mark dataset for cross-lingual abstractive summariza-
tion. In Findings of the Association for Computa-
tional Linguistics: EMNLP 2020, pages 4034–4048,
Online. Association for Computational Linguistics.
Viet Dac Lai, Nghia Trung Ngo, Amir Pouran Ben Vey-
seh, Hieu Man, Franck Dernoncourt, Trung Bui, and
Thien Huu Nguyen. 2023. Chatgpt beyond english:
Towards a comprehensive evaluation of large lan-
guage models in multilingual learning.
Teven Le Scao et al. 2023. Bloom: A 176b-parameter
open-access multilingual language model.
Patrick Lewis, Barlas O˘guz, Ruty Rinott, Sebastian
Riedel, and Holger Schwenk. 2020. MLQA: Evalu-
ating Cross-lingual Extractive Question Answering.
In Proceedings of ACL 2020.
Percy Liang et al. 2023. Holistic evaluation of lan-
guage models. Transactions on Machine Learning
Research. Featured Certification, Expert Certifica-
tion.
Andy Liaw and Matthew Wiener. 2002. Classification
and regression by randomforest. R News, 2(3):18–22.
Hoang Le Long. 2023.
Vietnamese Fullname
Generator.
https://github.com/lhlong/
vietnamese-fullname-generator.
Accessed:
Dec 14, 2023.
Son T. Luu, Kiet Van Nguyen, and Ngan Luu-Thuy
Nguyen. 2021. A large-scale dataset for hate speech
detection on vietnamese social media texts. In Ad-
vances and Trends in Artificial Intelligence. Artifi-
cial Intelligence Practices, pages 415–426, Cham.
Springer International Publishing.
Niklas Muennighoff, Thomas Wang, Lintang Sutawika,
Adam Roberts, Stella Biderman, Teven Le Scao,
M Saiful Bari, Sheng Shen, Zheng Xin Yong, Hai-
ley Schoelkopf, Xiangru Tang, Dragomir Radev,
Alham Fikri Aji, Khalid Almubarak, Samuel Al-
banie, Zaid Alyafeai, Albert Webson, Edward Raff,
and Colin Raffel. 2023. Crosslingual generaliza-
tion through multitask finetuning. In Proceedings
of the 61st Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers),
pages 15991–16111, Toronto, Canada. Association
for Computational Linguistics.
Anh Tuan Nguyen, Mai Hoang Dao, and Dat Quoc
Nguyen. 2020a. A Pilot Study of Text-to-SQL Se-
mantic Parsing for Vietnamese. In Findings of the
Association for Computational Linguistics: EMNLP
2020, pages 4079–4085.
Dat Quoc Nguyen, Linh The Nguyen, Chi Tran,
Dung Ngoc Nguyen, Nhung Nguyen, Thien Huu
Nguyen, Dinh Phung, and Hung Bui. 2023a.
PhoGPT: Generative Pre-training for Vietnamese.
arXiv preprint, arXiv:2311.02945.
Duc-Vu Nguyen, Kiet Van Nguyen, Ngan Luu-Thuy
Nguyen, and Anh Gia-Tuan Nguyen. 2019a. Hate
Speech Detection on Vietnamese Social Media Text
using the Bi-GRU-LSTM-CNN Model. In The Sixth
International Workshop on Vietnamese Language
and Speech Processing.
Ha-Thanh Nguyen, Wachara Fungwacharakorn, and Ken
Satoh. 2023b. Enhancing logical reasoning in large
language models to facilitate legal applications.
Huyen T M Nguyen, Hung V Nguyen, Quyen T Ngo,
Luong X Vu, Vu Mai Tran, Bach X Ngo, and
Cuong A Le. 2019b. Vlsp shared task: Sentiment
analysis. Journal of Computer Science and Cyber-
netics, 34(4):295–310.
Kiet Van Nguyen, Vu Duc Nguyen, Phu X. V. Nguyen,
Tham T. H. Truong, and Ngan Luu-Thuy Nguyen.
2018. Uit-vsfc: Vietnamese students’ feedback cor-
pus for sentiment analysis. In Proceedings of 10th
International Conference on Knowledge and Systems
Engineering (KSE), pages 19–24.
Kiet Van Nguyen, Khiem Vinh Tran, Son T. Luu,
Anh Gia-Tuan Nguyen, and Ngan Luu-Thuy Nguyen.
2020b. Enhancing lexical-based approach with ex-
ternal knowledge for vietnamese multiple-choice
machine reading comprehension.
IEEE Access,
8:201404–201417.
Luan Thanh Nguyen, Kiet Van Nguyen, and Ngan Luu-
Thuy Nguyen. 2021. Constructive and toxic speech
detection for open-domain social media comments
in vietnamese. In Advances and Trends in Artificial
Intelligence. Artificial Intelligence Practices: 34th
International Conference on Industrial, Engineering
and Other Applications of Applied Intelligent Sys-
tems, IEA/AIE 2021, Kuala Lumpur, Malaysia, July
26–29, 2021, Proceedings, Part I, page 572–583,
Berlin, Heidelberg. Springer-Verlag.
Tri Nguyen, Mir Rosenberg, Xia Song, Jianfeng Gao,
Saurabh Tiwary, Rangan Majumder, and Li Deng.
2016. Ms marco: A human generated machine read-
ing comprehension dataset.
Van-Hau Nguyen, Thanh-Chinh Nguyen, Minh-Tien
Nguyen, and Nguyen Xuan Hoai. 2019c. Vnds: A
vietnamese dataset for summarization. In 2019 6th
NAFOSTED Conference on Information and Com-
puter Science (NICS), pages 375–380.
OpenAI. 2023. ChatGPT. https://chat.openai.com.
Large language model.
OpenAI. 2023. Introducing gpt-4. https://openai.
com/research/gpt-4.
Kishore Papineni, Salim Roukos, Todd Ward, and Wei-
Jing Zhu. 2002. Bleu: A method for automatic eval-
uation of machine translation. In Proceedings of the

--- Page 12 ---

40th Annual Meeting on Association for Computa-
tional Linguistics, ACL ’02, page 311–318, USA.
Association for Computational Linguistics.
Long Phan, Hieu Tran, Hieu Nguyen, and Trieu H.
Trinh. 2022.
ViT5: Pretrained text-to-text trans-
former for Vietnamese language generation. In Pro-
ceedings of the 2022 Conference of the North Amer-
ican Chapter of the Association for Computational
Linguistics: Human Language Technologies: Student
Research Workshop, pages 136–142, Hybrid: Seattle,
Washington + Online. Association for Computational
Linguistics.
P. J. Price. 1990. Evaluation of spoken language sys-
tems: the ATIS domain. In Speech and Natural Lan-
guage: Proceedings of a Workshop Held at Hidden
Valley, Pennsylvania, June 24-27,1990.
Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, and
Percy Liang. 2016. SQuAD: 100,000+ questions for
machine comprehension of text. In Proceedings of
the 2016 Conference on Empirical Methods in Natu-
ral Language Processing, pages 2383–2392, Austin,
Texas. Association for Computational Linguistics.
Gemma Team, Thomas Mesnard, and Cassidy Hardin
et al. 2024. Gemma: Open models based on gemini
research and technology.
MosaicML NLP Team. 2023.
Introducing mpt-7b:
A new standard for open-source, commercially us-
able llms. www.mosaicml.com/blog/mpt-7b. Ac-
cessed: 2023-05-05.
Hugo Touvron et al. 2023. Llama 2: Open founda-
tion and fine-tuned chat models.
arXiv preprint
arXiv:2307.09288.
Hieu Tran, Cuong V. Dinh, Long Phan, and Son T.
Nguyen. 2021. Hierarchical transformer encoders
for vietnamese spelling correction.
In Advances
and Trends in Artificial Intelligence. Artificial In-
telligence Practices, pages 547–556, Cham. Springer
International Publishing.
ViLM. 2023. Vietcuna-7b-v3. https://huggingface.
co/vilm/vietcuna-7b-v3. Accessed: 2023-09-09.
Boxin Wang, Weixin Chen, Hengzhi Pei, Chulin Xie,
Mintong Kang, Chenhui Zhang, Chejian Xu, Zidi
Xiong, Ritik Dutta, Rylan Schaeffer, Sang T. Truong,
Simran Arora, Mantas Mazeika, Dan Hendrycks, Zi-
nan Lin, Yu Cheng, Sanmi Koyejo, Dawn Song, and
Bo Li. 2024. Decodingtrust: A comprehensive as-
sessment of trustworthiness in gpt models.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten
Bosma, brian ichter, Fei Xia, Ed Chi, Quoc V Le,
and Denny Zhou. 2022. Chain-of-thought prompt-
ing elicits reasoning in large language models. In
Advances in Neural Information Processing Systems,
volume 35, pages 24824–24837. Curran Associates,
Inc.
wikiHow. 2023.
wikihow experts.
https://www.
wikihow.com/Experts. Accessed: Dec 14, 2023.
Yuhuai Wu, Markus N Rabe, Wenda Li, Jimmy Ba,
Roger B Grosse, and Christian Szegedy. 2021. Lime:
Learning inductive bias for primitives of mathemat-
ical reasoning. In Proceedings of the 38th Interna-
tional Conference on Machine Learning, volume 139
of Proceedings of Machine Learning Research, pages
11251–11262. PMLR.
Dao Xuan-Quy, Le Ngoc-Bich, Phan Xuan-Dung, Ngo
Bac-Bien, and Vo The-Duy. 2023. Evaluation of
chatgpt and microsoft bing ai chat performances on
physics exams of vietnamese national high school
graduation examination.
Wentao Ye, Mingfeng Ou, Tianyi Li, Yipeng chen, Xue-
tao Ma, Yifan Yanggong, Sai Wu, Jie Fu, Gang Chen,
Haobo Wang, and Junbo Zhao. 2023. Assessing hid-
den risks of llms: An empirical study on robustness,
consistency, and credibility.
Zalo AI. 2023. Zalo ai challenge: End to end question
answering task. Accessed: 2023-12-09.
Biao Zhang, Philip Williams, Ivan Titov, and Rico Sen-
nrich. 2020. Improving massively multilingual neu-
ral machine translation and zero-shot translation. In
Proceedings of the 58th Annual Meeting of the Asso-
ciation for Computational Linguistics, pages 1628–
1639, Online. Association for Computational Lin-
guistics.
Zihao Zhao, Eric Wallace, Shi Feng, Dan Klein, and
Sameer Singh. 2021. Calibrate before use: Improv-
ing few-shot performance of language models. In
Proceedings of the 38th International Conference on
Machine Learning, volume 139 of Proceedings of
Machine Learning Research, pages 12697–12706.
PMLR.

--- Page 13 ---

A
Dataset Statistics
In this section, we present a detailed account of
the dataset statistics utilized in the fine-tuning pro-
cess, as delineated in Table 1, and evaluations, as
tabulated in Table 2. The quantification of token
counts is conducted using the LLaMa-2 tokenizer
for consistency.
Table 1: Statistics of fine-tuning datasets. NoS: Number
of samples; TK: Total tokens; ATpS: Average tokens
per sample.
Dataset
NoS
TK
ATpS
Vietnamese Wikipedia
1284930
560497590
436
Vietnamese New Coprus
19365593
4073308063
210
Vietnamese Highschool Essay
28242
80753993
2859
Table 2: Statistics of evaluation datasets. NoTrS: Num-
ber of training samples; NoTeS: Number of testing sam-
ples; ATpS: Average tokens per sample.
Dataset
NoTrS
NoTeS
ATpS
VietNews
99134
22498
1479
WikiLingua
95517
27489
519
XQuAD
0
1190
530
MLQA
0
5495
616
UiT-VSFC
11426
3166
37
VLSP 2016
5100
1050
74
PhoATIS
4478
893
45
UiT-VSMEC
5548
693
38
ZaloE2E
0
600
33
UiT-ViMMRC
1975
514
756
UiT-ViCTSD
7000
1000
84
UiT-ViHSD
24048
6680
31
MLQA-MLM
0
5495
647
VSEC
0
9341
89
PhoMT
2977999
19151
20
OPUS100
1000000
2000
11
mMarco
1000
6980
233
mRobust04
0
250
7880
SR - Natural
1000
5000
220
SR - Abstract Symbol
3000
15000
53
MATH
7500
5000
125
B
Computing Probability-related Metrics
In classification tasks, determining the Area Under
the Receiver Operating Characteristic (AUC ROC)
involves the computation of probabilities associated
with each option given a prompt and a correspond-
ing list of potential labels. The probability for each
option is derived by assessing the log-probability
assigned to that particular option. To compute the
log-probability for each option, an input sequence
is constructed by concatenating the prompt with an
individual option, and subsequently encoding this
composite input using a tokenizer. To ensure the
comprehensive evaluation of the log-probability for
the option, an "end of sentence" token (<eos>) is
appended to the end of the sequence. Subsequently,
the encoded input undergoes processing through
the model, generating probabilities for each token.
Only the log-probabilities associated with tokens
within the encoded input pertaining to the option
are extracted, incorporating the <eos> token. The
log-probabilities for a given option are then calcu-
lated as the sum of the extracted log-probabilities.
In the scenario of having n options, the probability
assigned to each option is determined through the
softmax function applied to the log-probabilities of
the n options. Following the acquisition of prob-
abilities for each option, standard procedures for
calculating AUC ROC are carried out. For exam-
ple, with below context prompt:
Passage :
{ passage }
Query :
{ query }
Can
the
passage
answer
the
query ?
Answer :
Assuming that the label set is S = {“Yes”, “No”}
and tokenizer is at character level.
Firstly, we
calculate the log probability of each option in the
label set. Based on the explanation above, it can be
calculated by applying log operation to below equa-
tions, where c is the context: p(Yes<eos>|c) =
p(Y|c)p(e|c, Y)p(s|c, Ye)p(<eos>|c, Yes),
p(No<eos>|c) = p(N|c)p(o|c, N)p(<eos>|c, No).
Then, we can get the probability of each option by
normalization using softmax.
p(Yes) =
exp(p(Yes<eos>|c))
P
o∈S exp(p(o, <eos>|c)
p(No) =
exp(p(No<eos>|c))
P
o∈S exp(p(o, <eos>|c))
C
Toxicity Prediction Model
For assessing the toxicity in LLM generation, we
constructed a toxicity prediction model utilizing
the UiT-ViCTSD dataset (Luu et al., 2021). Var-
ious machine learning and deep learning mod-
els were employed for this purpose, including
Logistic Regression (Cox, 1958), Random For-
est(Liaw and Wiener, 2002), Support Vector Ma-
chine (SVM) (Cortes and Vapnik, 1995), Long
Short-Term Memory (LSTM) (Hochreiter and
Schmidhuber, 1997) with fastText embedding (Bo-
janowski et al., 2017), LSTM with PhoW2V em-
bedding (Nguyen et al., 2020a), Bi-GRU-LSTM-
CNN (Nguyen et al., 2019a) with fastText embed-
ding, Bi-GRU-LSTM-CNN with PhoW2V embed-
ding, and ViT5 (Phan et al., 2022). The compar-
ative results are presented in Table 3. The model

--- Page 14 ---

demonstrating the highest accuracy in toxicity pre-
diction (ViT5) was selected for further analysis.
Table 3: Performance of toxicity detection on UiT-
ViCTSD testing set
Models
AC↑
F1↑
Logistic Regression
90.27
55.35
Random Forest
90.03
55.30
SVM
90.17
59.06
LSTM + fastText
88.90
49.63
LSTM + PhoW2V
89.00
49.70
Bi-GRU-LSTM-CNN + fastText
89.10
48.88
Bi-GRU-LSTM-CNN + PhoW2V
88.90
49.62
ViT5 (Our chosen model)
91.10
55.72
D
Evaluation Framework
Our developed evaluation framework is based on
Python 3, utilizing various libraries from Hugging-
Face, including transformers, accelerate, datasets,
evaluate, etc.
Our framework is available at
GitHub. We acknowledge Thu Nguyen for help-
ing us document and refactor our code. To deploy
LLMs for inference, we use Text Generation Infer-
ence (TGI) toolkit, which combines multiple accel-
erate tools with helping to optimize the inference
procedure. The hyperparameter configurations for
text generation are as follows.
• Quantization: 4-bit with NF4
• Temperature: 1.0
• Top-K: 1
• Repetition penalty: 1.1
• Max new tokens:
– Question-answering: 100
– Summarization: 300
– Sentiment analysis: 50
– Text classification: 50
– Knowledge:
ZaloE2E - 100;
UiT-
ViMMRC - 50
– Toxicity detection: 50
– Information retrieval: 50
– Language modelling: 500
– Reasoning: Synthetic resoning - 100;
MATH - 1000
– Translation: 500
E
Additional Results
This section presents the evaluation results of our
finetuned models, LLaMa-2, Vietcuna 7B, Vis-
tral, PhoGPT 7B, Gemini Pro, GPT-3.5 Turbo, and
GPT-4, across ten tasks. The performances of the
best open-sourced and best models are highlighted
in blue and gray, respectively.
F
Effect of generation hyperparameters
With the generation configuration presented in Ap-
pendix D, we can consider our tests to be difficult
tests which require the LLM to generate the most
appropriate tokens with the highest probability at
each step. However, for multilingual LLMs with
large vocabulary sizes such as GemSUra, the signal
for the most appropriate tokens is sometimes not at
the top probability. Thus, we modify the generation
hyperparameters as below and perform testing on
URA-LLaMa 7B, GemSUra 7B and Vistral.
• Temperature: 0.1
• Top-K: 50
• Repetition penalty: 1.0
According to Table 12, we observe that all three
models achieve better performance compared to
previous results in Table 4. While URA-LLaMA
has slight improvements, GemSUra and Vistral per-
formance increase significantly. This phenomenon
can be explained by the fact that the signal of Viet-
namese tokens in these models is not as strong as
the others due to the larger vocabulary size. This
observation suggests that large vocabulary multi-
lingual LLMs produce weaker signals for a specific
language, so we need to set a larger Top-K hyper-
parameter for better performance while trading off
efficiency.
G
Prompts
All the prompts we used in our experiments are in Vietnamese.
We present details of these prompts and their meanings in
English (translated by Google Translate) in below section with
LLaMa-2 template. The template need to be adjusted for other
models.
G.1
Question-Answering
Weak prompt:
[ INST ]
Ngữcảnh :
{ context }
Câu hỏi :
{ question }
Trả
l ời :
[ / INST ]

--- Page 15 ---

Table 4: Performance under zero-shot prompting
(a) Question-answering
XQuAD
MLQA
Models
EM↑
F1↑
EM↑
F1↑
URA-LLaMa 70B
0.06 ± 0.00
0.30 ± 0.00
0.04 ± 0.00
0.28 ± 0.00
URA-LLaMa 13B
0.00 ± 0.00
0.14 ± 0.00
0.00 ± 0.00
0.15 ± 0.00
URA-LLaMa 7B
0.00 ± 0.00
0.14 ± 0.00
0.00 ± 0.00
0.16 ± 0.00
LLaMa-2 70B
0.00 ± 0.00
0.11 ± 0.00
0.00 ± 0.00
0.12 ± 0.00
LLaMa-2 13B
0.00 ± 0.00
0.04 ± 0.00
0.00 ± 0.02
0.05 ± 0.00
LLaMa-2 7B
0.00 ± 0.00
0.05 ± 0.00
0.00 ± 0.00
0.06 ± 0.00
Vietcuna 7B
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
Vistral 7B Chat
0.01 ± 0.00
0.03 ± 0.00
0.01 ± 0.00
0.03 ± 0.00
PhoGPT 7B5 Instruct
0.00 ± 0.00
0.06 ± 0.00
0.00 ± 0.00
0.06 ± 0.00
MixSUra
0.00 ± 0.00
0.17 ± 0.00
0.00 ± 0.00
0.18 ± 0.00
GemSUra
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
Gemini Pro
0.17 ± 0.01
0.39 ± 0.01
0.13 ± 0.00
0.34 ± 0.01
GPT-3.5
0.00 ± 0.00
0.24 ± 0.00
0.00 ± 0.00
0.25 ± 0.00
GPT-4
0.00 ± 0.00
0.27 ± 0.00
0.00 ± 0.00
0.27 ± 0.00
(b) Summarization
VietNews
WikiLingua
Models
R1↑
R2↑
RL↑
SC↑
BS↑
Cv↑
De↑
Cp↑
R1↑
R2↑
RL↑
SC↑
BS↑
Cv↑
De↑
Cp↑
URA-LLaMa 70B
0.42 ± 0.00
0.21 ± 0.00
0.28 ± 0.00
0.55 ± 0.00
0.03 ± 0.19
0.85 ± 0.00
14.59 ± 0.05
17.21 ± 0.33
0.37 ± 0.00
0.16 ± 0.00
0.24 ± 0.00
−0.05 ± 0.00
0.26 ± 0.16
0.17 ± 0.00
0.22 ± 0.00
22.24 ± 0.97
URA-LLaMa 13B
0.38 ± 0.00
0.18 ± 0.00
0.25 ± 0.00
0.44 ± 0.00
0.01 ± 0.18
0.71 ± 0.00
6.01 ± 0.07
24.27 ± 0.61
0.22 ± 0.00
0.08 ± 0.00
0.14 ± 0.00
0.20 ± 0.00
−0.13 ± 0.12
0.42 ± 0.01
3.06 ± 0.10
49.58 ± 1.16
URA-LLaMa 7B
0.38 ± 0.00
0.14 ± 0.00
0.25 ± 0.00
0.19 ± 0.00
0.04 ± 0.12
0.65 ± 0.00
4.88 ± 0.03
7.77 ± 0.05
0.40 ± 0.00
0.15 ± 0.00
0.26 ± 0.00
0.21 ± 0.00
0.19 ± 0.07
0.73 ± 0.00
4.79 ± 0.07
6.22 ± 0.07
LLaMa-2 70B
0.20 ± 0.00
0.10 ± 0.00
0.14 ± 0.00
0.21 ± 0.00
−0.08 ± 0.15
0.48 ± 0.00
8.15 ± 0.09
21.75 ± 0.54
0.06 ± 0.00
0.02 ± 0.00
0.04 ± 0.00
0.05 ± 0.00
−0.20 ± 0.15
0.12 ± 0.00
0.84 ± 0.05
55.29 ± 0.93
LLaMa-2 13B
0.06 ± 0.00
0.02 ± 0.00
0.04 ± 0.00
0.01 ± 0.00
−0.18 ± 0.04
0.07 ± 0.00
0.43 ± 0.01
28.25 ± 0.24
0.04 ± 0.00
0.00 ± 0.00
0.03 ± 0.00
−0.02 ± 0.00
−0.11 ± 0.08
0.03 ± 0.00
0.07 ± 0.01
19.55 ± 0.51
LLaMa-2 7B
0.06 ± 0.00
0.01 ± 0.00
0.05 ± 0.00
−0.06 ± 0.00
−0.23 ± 0.04
0.06 ± 0.00
0.21 ± 0.00
15.75 ± 0.20
0.04 ± 0.00
0.00 ± 0.00
0.03 ± 0.00
−0.06 ± 0.00
−0.14 ± 0.07
0.03 ± 0.00
0.06 ± 0.00
17.84 ± 0.50
Vietcuna 7B
0.28 ± 0.00
0.06 ± 0.00
0.18 ± 0.00
−0.04 ± 0.00
−0.09 ± 0.09
0.31 ± 0.00
0.80 ± 0.01
171.63 ± 1.71
0.24 ± 0.00
0.06 ± 0.00
0.15 ± 0.00
−0.02 ± 0.00
−0.18 ± 0.07
0.51 ± 0.01
1.16 ± 0.01
238.67 ± 3.37
Vistral 7B Chat
0.02 ± 0.00
0.01 ± 0.00
0.01 ± 0.00
0.01 ± 0.00
−0.19 ± 0.04
0.99 ± 0.00
1.16 ± 0.01
539.17 ± 1.74
0.11 ± 0.00
0.05 ± 0.00
0.07 ± 0.00
0.04 ± 0.00
−0.19 ± 0.17
0.94 ± 0.00
1.60 ± 0.03
450.54 ± 7.09
PhoGPT 7B5 Instruct
0.35 ± 0.01
0.15 ± 0.00
0.22 ± 0.00
0.30 ± 0.00
0.21 ± 0.07
0.75 ± 0.01
5.34 ± 0.25
45.02 ± 5.62
0.31 ± 0.00
0.11 ± 0.00
0.20 ± 0.00
0.15 ± 0.00
−0.18 ± 0.11
0.62 ± 0.01
4.08 ± 0.09
56.86 ± 2.17
MixSUra
0.40 ± 0.00
0.20 ± 0.00
0.26 ± 0.00
0.48 ± 0.00
0.04 ± 0.12
0.85 ± 0.00
6.60 ± 0.03
9.04 ± 0.42
0.47 ± 0.00
0.22 ± 0.00
0.29 ± 0.00
0.14 ± 0.00
0.23 ± 0.07
0.88 ± 0.00
4.93 ± 0.04
8.75 ± 0.59
GemSUra
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
−0.19 ± 0.02
1.00 ± 0.00
1.00 ± 0.00
552.10 ± 2.39
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
−0.19 ± 0.08
1.00 ± 0.00
1.00 ± 0.00
589.41 ± 7.34
Gemini Pro
0.44 ± 0.00
0.22 ± 0.00
0.28 ± 0.00
0.31 ± 0.00
−0.01 ± 0.06
0.86 ± 0.00
3.28 ± 0.01
8.13 ± 0.20
0.40 ± 0.00
0.18 ± 0.00
0.26 ± 0.00
0.21 ± 0.00
0.02 ± 0.10
0.73 ± 0.00
1.97 ± 0.01
27.56 ± 0.83
GPT-3.5
0.36 ± 0.00
0.20 ± 0.00
0.24 ± 0.00
0.44 ± 0.00
0.04 ± 0.13
0.86 ± 0.00
3.97 ± 0.02
13.32 ± 0.65
0.43 ± 0.00
0.21 ± 0.00
0.27 ± 0.00
0.45 ± 0.00
0.22 ± 0.03
0.87 ± 0.00
3.29 ± 0.03
35.50 ± 0.82
GPT-4
0.41 ± 0.00
0.21 ± 0.00
0.26 ± 0.00
0.40 ± 0.00
−0.04 ± 0.11
0.84 ± 0.00
3.45 ± 0.00
15.43 ± 0.49
0.44 ± 0.00
0.21 ± 0.00
0.27 ± 0.00
0.32 ± 0.00
0.24 ± 0.04
0.82 ± 0.00
2.37 ± 0.01
6.61 ± 0.16
(c) Sentiment analysis
VLSP 2016
UiT-VSFC
Models
AC↑
F1↑
AR↑
ECE↓
A@10↑
AC↑
F1↑
AR↑
ECE↓
A@10↑
URA-LLaMa 70B
0.63 ± 0.02
0.63 ± 0.02
0.74 ± 0.01
0.15 ± 0.01
0.87 ± 0.03
0.64 ± 0.01
0.54 ± 0.01
0.85 ± 0.01
0.14 ± 0.00
0.98 ± 0.01
URA-LLaMa 13B
0.52 ± 0.02
0.35 ± 0.01
0.60 ± 0.01
0.10 ± 0.01
0.64 ± 0.05
0.70 ± 0.01
0.40 ± 0.01
0.72 ± 0.01
0.23 ± 0.01
0.95 ± 0.01
URA-LLaMa 7B
0.35 ± 0.02
0.24 ± 0.01
0.54 ± 0.01
0.24 ± 0.01
0.31 ± 0.05
0.27 ± 0.01
0.18 ± 0.00
0.52 ± 0.01
0.37 ± 0.01
0.03 ± 0.01
LLaMa-2 70B
0.51 ± 0.02
0.37 ± 0.01
0.54 ± 0.01
0.29 ± 0.01
0.57 ± 0.06
0.44 ± 0.01
0.28 ± 0.00
0.69 ± 0.01
0.35 ± 0.01
0.60 ± 0.03
LLaMa-2 13B
0.25 ± 0.01
0.25 ± 0.01
0.49 ± 0.01
0.39 ± 0.01
0.29 ± 0.05
0.29 ± 0.01
0.24 ± 0.01
0.52 ± 0.01
0.42 ± 0.01
0.30 ± 0.03
LLaMa-2 7B
0.15 ± 0.01
0.15 ± 0.01
0.58 ± 0.01
0.73 ± 0.01
0.12 ± 0.03
0.04 ± 0.00
0.06 ± 0.01
0.49 ± 0.01
0.79 ± 0.00
0.01 ± 0.01
Vietcuna 7B
0.11 ± 0.01
0.12 ± 0.01
0.49 ± 0.01
0.68 ± 0.01
0.11 ± 0.03
0.05 ± 0.00
0.06 ± 0.00
0.56 ± 0.01
0.73 ± 0.00
0.05 ± 0.01
Vistral 7B Chat
0.28 ± 0.00
0.16 ± 0.00
0.86 ± 0.01
0.36 ± 0.01
0.15 ± 0.00
0.02 ± 0.00
0.07 ± 0.00
0.90 ± 0.01
0.78 ± 0.00
0.00 ± 0.00
PhoGPT 7B5 Instruct
0.02 ± 0.00
0.03 ± 0.01
0.62 ± 0.01
0.98 ± 0.00
0.02 ± 0.01
0.01 ± 0.00
0.01 ± 0.00
0.60 ± 0.01
0.99 ± 0.00
0.00 ± 0.00
MixSUra
0.45 ± 0.01
0.30 ± 0.05
0.62 ± 0.01
0.50 ± 0.01
0.49 ± 0.05
0.55 ± 0.01
0.40 ± 0.01
0.66 ± 0.01
0.41 ± 0.01
0.60 ± 0.03
GemSUra
0.00 ± 0.00
0.00 ± 0.00
0.76 ± 0.01
0.79 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.84 ± 0.01
0.84 ± 0.00
0.00 ± 0.00
Gemini Pro
0.64 ± 0.01
0.47 ± 0.01
−
0.31 ± 0.01
0.53 ± 0.04
0.76 ± 0.01
0.49 ± 0.01
−
0.43 ± 0.01
0.77 ± 0.03
GPT-3.5
0.62 ± 0.02
0.56 ± 0.01
−
0.29 ± 0.02
0.62 ± 0.05
0.81 ± 0.00
0.68 ± 0.00
−
0.48 ± 0.01
0.83 ± 0.02
GPT-4
0.71 ± 0.01
0.68 ± 0.01
−
0.37 ± 0.01
0.70 ± 0.04
0.80 ± 0.01
0.67 ± 0.01
−
0.47 ± 0.01
0.85 ± 0.02
(d) Text classification
UiT-VSMEC
PhoATIS
Models
AC↑
F1↑
AR↑
ECE↓
A@10↑
AC↑
F1↑
AR↑
ECE↓
A@10↑
URA-LLaMa 70B
0.40 ± 0.02
0.32 ± 0.02
0.68 ± 0.01
0.14 ± 0.02
0.60 ± 0.06
0.56 ± 0.02
0.48 ± 0.03
0.85 ± 0.00
0.25 ± 0.02
0.56 ± 0.06
URA-LLaMa 13B
0.27 ± 0.02
0.24 ± 0.02
0.52 ± 0.01
0.07 ± 0.01
0.23 ± 0.05
0.10 ± 0.01
0.10 ± 0.01
0.72 ± 0.00
0.52 ± 0.01
0.14 ± 0.04
URA-LLaMa 7B
0.13 ± 0.01
0.11 ± 0.01
0.50 ± 0.01
0.15 ± 0.01
0.21 ± 0.05
0.04 ± 0.01
0.04 ± 0.02
0.77 ± 0.00
0.30 ± 0.01
0.04 ± 0.02
LLaMa-2 70B
0.33 ± 0.01
0.28 ± 0.01
0.56 ± 0.01
0.30 ± 0.01
0.47 ± 0.05
0.10 ± 0.01
0.09 ± 0.01
0.72 ± 0.01
0.26 ± 0.01
0.13 ± 0.04
LLaMa-2 13B
0.11 ± 0.01
0.10 ± 0.01
0.49 ± 0.01
0.31 ± 0.01
0.09 ± 0.04
0.03 ± 0.01
0.02 ± 0.00
0.45 ± 0.01
0.28 ± 0.01
0.03 ± 0.02
LLaMa-2 7B
0.07 ± 0.01
0.08 ± 0.01
0.52 ± 0.01
0.35 ± 0.01
0.07 ± 0.03
0.00 ± 0.06
0.00 ± 0.06
0.61 ± 0.01
0.32 ± 0.00
0.00 ± 0.00
Vietcuna 7B
0.05 ± 0.01
0.02 ± 0.01
0.52 ± 0.01
0.95 ± 0.01
0.03 ± 0.02
0.05 ± 0.01
0.01 ± 0.00
0.66 ± 0.00
0.20 ± 0.01
0.01 ± 0.21
Vistral 7B Chat
0.00 ± 0.00
0.00 ± 0.00
0.56 ± 0.02
0.35 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.89 ± 0.01
0.47 ± 0.01
0.00 ± 0.00
PhoGPT 7B5 Instruct
0.01 ± 0.00
0.01 ± 0.00
0.52 ± 0.02
0.99 ± 0.00
0.00 ± 0.01
0.02 ± 0.00
0.01 ± 0.00
0.54 ± 0.02
0.98 ± 0.00
0.00 ± 0.01
MixSUra
0.34 ± 0.02
0.26 ± 0.02
0.63 ± 0.01
0.64 ± 0.02
0.57 ± 0.05
0.23 ± 0.01
0.33 ± 0.03
0.90 ± 0.01
0.74 ± 0.01
0.48 ± 0.05
GemSUra
0.00 ± 0.00
0.00 ± 0.00
0.61 ± 0.02
0.58 ± 0.01
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.73 ± 0.01
0.65 ± 0.01
0.00 ± 0.00
Gemini Pro
0.50 ± 0.02
0.38 ± 0.02
−
0.36 ± 0.02
0.44 ± 0.06
0.89 ± 0.01
0.66 ± 0.03
−
0.83 ± 0.01
0.74 ± 0.03
GPT-3.5
0.43 ± 0.02
0.37 ± 0.02
−
0.29 ± 0.02
0.43 ± 0.06
0.44 ± 0.02
0.38 ± 0.03
−
0.38 ± 0.02
0.44 ± 0.05
GPT-4
0.49 ± 0.02
0.46 ± 0.02
−
0.35 ± 0.02
0.50 ± 0.06
0.89 ± 0.01
0.69 ± 0.02
−
0.83 ± 0.01
0.89 ± 0.03
(e) Knowledge
ZaloE2E
ViMMRC
Models
EM↑
F1↑
AC↑
F1↑
AR↑
ECE↓
A@10↑
URA-LLaMa 70B
0.28 ± 0.02
0.44 ± 0.02
0.80 ± 0.02
0.80 ± 0.02
0.85 ± 0.01
0.10 ± 0.02
0.96 ± 0.03
URA-LLaMa 13B
0.12 ± 0.01
0.22 ± 0.01
0.40 ± 0.02
0.31 ± 0.02
0.57 ± 0.02
0.48 ± 0.02
0.42 ± 0.08
URA-LLaMa 7B
0.09 ± 0.01
0.20 ± 0.02
0.30 ± 0.02
0.10 ± 0.01
0.56 ± 0.02
0.27 ± 0.02
0.56 ± 0.07
LLaMa-2 70B
0.11 ± 0.01
0.26 ± 0.01
0.69 ± 0.02
0.55 ± 0.02
0.40 ± 0.01
0.21 ± 0.02
0.75 ± 0.07
LLaMa-2 13B
0.06 ± 0.01
0.10 ± 0.01
0.52 ± 0.02
0.41 ± 0.02
0.64 ± 0.02
0.33 ± 0.02
0.73 ± 0.07
LLaMa-2 7B
0.03 ± 0.01
0.07 ± 0.01
0.37 ± 0.02
0.25 ± 0.02
0.51 ± 0.02
0.35 ± 0.02
0.29 ± 0.06
Vietcuna 7B
0.03 ± 0.01
0.06 ± 0.01
0.32 ± 0.02
0.22 ± 0.02
0.50 ± 0.00
0.07 ± 0.02
0.33 ± 0.07
Vistral 7B Chat
0.00 ± 0.00
0.01 ± 0.00
0.01 ± 0.00
0.01 ± 0.00
0.95 ± 0.01
0.76 ± 0.01
0.00 ± 0.00
MixSUra
0.04 ± 0.01
0.17 ± 0.01
0.65 ± 0.02
0.52 ± 0.03
0.52 ± 0.02
0.31 ± 0.02
0.31 ± 0.07
GemSUra
0.00 ± 0.00
0.00 ± 0.00
0.51 ± 0.02
0.45 ± 0.02
0.62 ± 0.02
0.17 ± 0.02
0.58 ± 0.07
Gemini Pro
0.25 ± 0.02
0.39 ± 0.02
0.84 ± 0.02
0.68 ± 0.01
−
0.59 ± 0.02
0.79 ± 0.05
GPT-3.5
0.37 ± 0.02
0.56 ± 0.02
0.90 ± 0.01
0.72 ± 0.01
−
0.65 ± 0.01
0.90 ± 0.04
GPT-4
0.38 ± 0.02
0.55 ± 0.02
0.92 ± 0.01
0.73 ± 0.06
−
0.67 ± 0.01
0.90 ± 0.04
(f) Toxicity detection
UiT-ViCTSD
UiT-ViHSD
Models
AC↑
F1↑
AR↑
ECE↓
A@10↑
AC↑
F1↑
AR↑
ECE↓
A@10↑
URA-LLaMa 70B
0.61 ± 0.01
0.52 ± 0.01
0.77 ± 0.01
0.17 ± 0.01
0.97 ± 0.01
0.38 ± 0.01
0.34 ± 0.01
0.74 ± 0.01
0.25 ± 0.01
0.91 ± 0.01
URA-LLaMa 13B
0.46 ± 0.01
0.28 ± 0.03
0.53 ± 0.02
0.22 ± 0.01
0.48 ± 0.03
0.33 ± 0.01
0.18 ± 0.00
0.60 ± 0.01
0.35 ± 0.01
0.54 ± 0.02
URA-LLaMa 7B
0.25 ± 0.01
0.19 ± 0.01
0.53 ± 0.01
0.38 ± 0.01
0.13 ± 0.02
0.19 ± 0.00
0.13 ± 0.00
0.55 ± 0.01
0.46 ± 0.01
0.13 ± 0.01
LLaMa-2 70B
0.39 ± 0.01
0.25 ± 0.01
0.50 ± 0.01
0.59 ± 0.01
0.42 ± 0.05
0.16 ± 0.00
0.11 ± 0.00
0.54 ± 0.01
0.52 ± 0.00
0.15 ± 0.01
LLaMa-2 13B
0.16 ± 0.01
0.14 ± 0.00
0.40 ± 0.01
0.50 ± 0.01
0.24 ± 0.02
0.09 ± 0.00
0.13 ± 0.00
0.38 ± 0.01
0.63 ± 0.00
0.10 ± 0.01
LLaMa-2 7B
0.13 ± 0.01
0.14 ± 0.01
0.45 ± 0.02
0.69 ± 0.01
0.09 ± 0.01
0.03 ± 0.00
0.05 ± 0.01
0.56 ± 0.01
0.75 ± 0.00
0.00 ± 0.00
Vietcuna 7B
0.09 ± 0.00
0.07 ± 0.00
0.50 ± 0.00
0.41 ± 0.00
0.10 ± 0.03
0.07 ± 0.00
0.04 ± 0.00
0.50 ± 0.00
0.26 ± 0.00
0.07 ± 0.01
Vistral 7B Chat
0.00 ± 0.00
0.00 ± 0.00
0.82 ± 0.02
0.76 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.82 ± 0.01
0.66 ± 0.00
0.00 ± 0.00
MixSUra
0.73 ± 0.01
0.38 ± 0.01
0.74 ± 0.02
0.27 ± 0.01
0.60 ± 0.05
0.64 ± 0.01
0.30 ± 0.01
0.65 ± 0.01
0.32 ± 0.01
0.93 ± 0.01
GemSUra
0.00 ± 0.00
0.00 ± 0.00
0.72 ± 0.02
0.82 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.74 ± 0.01
0.72 ± 0.00
0.00 ± 0.00
Gemini Pro
0.79 ± 0.01
0.41 ± 0.01
−
0.29 ± 0.01
0.78 ± 0.03
0.68 ± 0.01
0.36 ± 0.01
−
0.35 ± 0.01
0.68 ± 0.02
GPT-3.5
0.75 ± 0.01
0.61 ± 0.02
−
0.25 ± 0.01
0.80 ± 0.04
0.55 ± 0.01
0.42 ± 0.01
−
0.22 ± 0.01
0.55 ± 0.02
GPT-4
0.89 ± 0.01
0.69 ± 0.01
−
0.39 ± 0.01
0.89 ± 0.03
0.75 ± 0.01
0.53 ± 0.01
−
0.42 ± 0.01
0.75 ± 0.02

--- Page 16 ---

(g) Language modeling
MLQA-MLM
VSEC
Models
EM↑
CER↓
WER↓
CED↓
WED↓
PLX↓
EM↑
CER↓
WER↓
CED↓
WED↓
PLX↓
URA-LLaMa 70B
0.01 ± 0.00
0.57 ± 0.01
0.61 ± 0.01
543.05 ± 10.96
128.05 ± 2.45
1.08 ± 0.01
0.00 ± 0.00
0.86 ± 0.00
0.99 ± 0.00
114.27 ± 0.57
29.99 ± 0.15
1.09 ± 0.00
URA-LLaMa 13B
0.00 ± 0.00
0.74 ± 0.00
0.80 ± 0.00
707.85 ± 11.62
166.85 ± 2.64
1.16 ± 0.02
0.01 ± 0.00
0.44 ± 0.01
0.54 ± 0.01
58.24 ± 0.77
16.27 ± 0.19
1.26 ± 0.00
URA-LLaMa 7B
0.00 ± 0.00
0.74 ± 0.00
0.84 ± 0.01
744.61 ± 13.18
183.98 ± 3.18
1.25 ± 0.01
0.01 ± 0.00
3.33 ± 0.04
2.90 ± 0.03
442.06 ± 5.66
87.53 ± 0.96
1.33 ± 0.00
LLaMa-2 70B
0.00 ± 0.00
0.91 ± 0.00
0.99 ± 0.00
868.70 ± 10.95
206.50 ± 2.47
1.00 ± 0.00
0.00 ± 0.00
0.86 ± 0.00
1.02 ± 0.00
114.16 ± 0.44
30.86 ± 0.12
1.00 ± 0.00
LLaMa-2 13B
0.00 ± 0.00
0.93 ± 0.00
1.00 ± 0.00
882.26 ± 11.23
208.57 ± 2.52
1.10 ± 0.01
0.00 ± 0.00
1.26 ± 0.01
1.30 ± 0.01
167.03 ± 1.16
39.07 ± 0.23
1.11 ± 0.00
LLaMa-2 7B
0.00 ± 0.00
0.90 ± 0.00
1.01 ± 0.01
862.02 ± 13.18
210.38 ± 3.18
1.25 ± 0.01
0.00 ± 0.00
1.32 ± 0.04
1.34 ± 0.03
176.04 ± 5.66
40.44 ± 0.96
1.14 ± 0.00
Vietcuna 7B
0.00 ± 0.00
1.00 ± 0.00
1.00 ± 0.00
951.99 ± 12.37
208.67 ± 2.73
1.48 ± 0.01
0.01 ± 0.00
1.06 ± 0.01
1.13 ± 0.01
141.33 ± 1.39
34.15 ± 0.33
1.61 ± 0.00
Vistral 7B Chat
0.00 ± 0.00
1.00 ± 0.00
1.00 ± 0.00
953.39 ± 11.06
208.83 ± 2.43
1.00 ± 0.00
0.00 ± 0.00
1.00 ± 0.00
1.00 ± 0.00
132.48 ± 0.60
30.08 ± 0.14
1.00 ± 0.00
MixSUra
0.00 ± 0.00
0.52 ± 0.00
0.58 ± 0.00
491.52 ± 8.47
121.61 ± 1.94
1.00 ± 0.00
0.12 ± 0.00
0.20 ± 0.00
0.30 ± 0.00
26.83 ± 0.36
9.16 ± 0.09
1.00 ± 0.00
GemSUra
0.00 ± 0.00
1.00 ± 0.00
1.00 ± 0.00
953.38 ± 11.57
208.83 ± 2.53
1.39 ± 0.00
0.00 ± 0.00
1.00 ± 0.00
1.00 ± 0.00
132.82 ± 0.56
30.16 ± 0.13
1.36 ± 0.00
Gemini Pro
0.01 ± 0.00
0.50 ± 0.01
0.52 ± 0.01
479.85 ± 11.64
108.14 ± 2.61
−
0.64 ± 0.00
0.11 ± 0.00
0.18 ± 0.00
14.07 ± 0.31
5.50 ± 0.07
−
GPT-3.5
0.00 ± 0.00
0.46 ± 0.01
0.54 ± 0.01
439.53 ± 10.79
111.98 ± 2.44
−
0.02 ± 0.00
0.14 ± 0.00
0.23 ± 0.00
18.59 ± 0.34
6.93 ± 0.09
−
GPT-4
0.04 ± 0.00
0.42 ± 0.01
0.51 ± 0.01
398.50 ± 10.26
106.27 ± 2.39
−
0.60 ± 0.01
0.14 ± 0.00
0.23 ± 0.00
18.17 ± 0.45
6.89 ± 0.12
−
(h) Reasoning
SR - Natural
SR - Abstract symbol
MATH
Models
EM↑
F1↑
Equ.↑
EM↑
F1↑
Equ.↑
EM↑
F1↑
Equ.↑
URA-LLaMa 70B
0.06 ± 0.00
0.34 ± 0.00
0.06 ± 0.00
0.02 ± 0.00
0.24 ± 0.00
0.01 ± 0.00
0.00 ± 0.00
0.01 ± 0.00
0.24 ± 0.02
URA-LLaMa 13B
0.01 ± 0.00
0.31 ± 0.00
0.02 ± 0.00
0.02 ± 0.00
0.24 ± 0.00
0.01 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.16 ± 0.02
URA-LLaMa 7B
0.00 ± 0.00
0.26 ± 0.00
0.00 ± 0.00
0.01 ± 0.00
0.17 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.06 ± 0.01
LLaMa-2 70B
0.04 ± 0.00
0.29 ± 0.00
0.04 ± 0.00
0.03 ± 0.00
0.25 ± 0.00
0.03 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.22 ± 0.02
LLaMa-2 13B
0.00 ± 0.00
0.06 ± 0.00
0.00 ± 0.00
0.02 ± 0.00
0.19 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.13 ± 0.02
LLaMa-2 7B
0.00 ± 0.00
0.04 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.05 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.03 ± 0.01
Vietcuna 7B
0.00 ± 0.00
0.04 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.10 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.02 ± 0.00
Vistral 7B Chat
0.00 ± 0.00
0.06 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.21 ± 0.01
MixSUra
0.02 ± 0.00
0.33 ± 0.00
0.02 ± 0.00
0.03 ± 0.00
0.22 ± 0.00
0.04 ± 0.00
0.00 ± 0.00
0.01 ± 0.00
0.42 ± 0.02
GemSUra
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.01 ± 0.00
Gemini Pro
0.08 ± 0.00
0.47 ± 0.00
0.08 ± 0.00
0.05 ± 0.00
0.25 ± 0.00
0.01 ± 0.00
0.00 ± 0.00
0.01 ± 0.00
0.64 ± 0.00
GPT-3.5
0.21 ± 0.00
0.59 ± 0.00
0.32 ± 0.00
0.09 ± 0.00
0.28 ± 0.00
0.13 ± 0.00
0.00 ± 0.00
0.01 ± 0.00
0.78 ± 0.02
GPT-4
0.21 ± 0.00
0.59 ± 0.00
0.32 ± 0.00
0.09 ± 0.00
0.28 ± 0.00
0.13 ± 0.00
0.00 ± 0.00
0.01 ± 0.00
0.78 ± 0.02
[ INST ]
Context :
{ context }
Question :
{ question }
Answer :
[ / INST ]
Medium prompt:
[ INST ] <<SYS>>
Hãy
t r ả
l ời
câu hỏi
bên dưới
bằng
t i ếng
Vi ệt
,→với
các
th ông
t i n
được
cung
cấp
trong
,→phần ngữcảnh . Nếu
trong
ngữcảnh khô
,→ng
có đủ
th ông
tin ,
hãy
t r ả
l ời
"Tô i
,→không
bi ết " .
<</SYS>>
Ngữcảnh :
{ context }
Câu hỏi :
{ question }
Trả
l ời :
[ / INST ]
[ INST ] <<SYS>>
Please
answer
the
question
below
in
,→Vietnamese
with
the
information
,→
provided
in
the
context .
I f
there
i s
,→not
enough
information
in
the
context ,
,→
answer
" I
don ' t
know " .
<</SYS>>
Context :
{ context }
Question :
{ question }
Answer :
[ / INST ]
Normal prompt:
[ INST ] <<SYS>>
Bạn
l à một
t r ợ
l ý hữu dụng
sửdụng
t i ếng
Vi ệt
,→
,
bi ết
t ôn
t r ọng và
th ành
th ật .
Bạn
lu
,→ôn
lu ôn
t r ả
l ời
các
câu hỏi một
cách
c
,→ó
í ch
nhi ều nhất
có
th ể,
nhưng đồng
th
,→ời
phải
an
to àn . Câu
t r ả
l ời
của bạn
,→không được
bao
gồm các
ngôn
từđộc hại
,→
,
phân
bi ệt
chủng
t ộc ,
phân
bi ệt
g i ới
,→
t í nh ,
nguy
hi ểm,
nội
dung
vi
phạm pháp
,→
lu ật .
Làm ơn hãy
chắc
chắn câu
t r ả
l ờ
,→
i
của bạn
tự
nhi ên ,
t í ch
cực
và không
,→
t h i ên v ị
bất
cứcá i
g ì . Nếu có
câu hỏi
,→
không hợp
l ý hoặc
không
r õ
r àng
th ì
h
,→ãy
g i ải
th í ch
t ại
sao
thay
v ì
t r ả
l ời
,→không đúng
sự
th ật . Nếu bạn không
bi ết
,→
câu
t r ả
l ời
th ì
đừng
chia
s ẻ
th ông
,→
t i n
s a i
sự
th ật .
<</SYS>>
Nhi ệm vụcủa bạn
l à dựa vào đoạn văn nằm
,→
trong
dấu
t r i p l e
backtick ,
hãy
t r ả
l ời
,→
câu hỏi
sau
bằng
t i ếng
Vi ệt :
{
,→
question }
Đoạn văn :
```{ context }```
[ / INST ]
[ INST ] <<SYS>>
You
are
a
h e l p f u l ,
r e s p e c t f u l ,
and
honest
,→Vietnamese - speaking
a s s i s t a n t .
You
,→
should
always
answer
q u e s t i o n s
as
,→
h e l p f u l l y
as
p o s s i b l e ,
but
at
the
same
,→
time ,
be
s a f e .
Your
r e p l y
must
not
,→
i n c l u d e
malicious ,
r a c i s t ,
s e x i s t ,
,→dangerous ,
or
i l l e g a l
content .
Please
,→make
sure
your
answers
are
natural ,
,→
p o s i t i v e ,
and
unbiased .
I f
the
,→
question
i s
unreasonable
or
unclear ,
,→
e xp la i n
why
i n s t e a d
of
answering
with
,→no
truth .
I f
you don ' t
know
the
answer
,→
then
don ' t
share
f a l s e
information .
<</SYS>>
Your
task
i s
to
answer
the
passage
in
t r i p l e
,→
backtick
based
on
the
passage .
the
,→
f o l l o w i n g
question
in
Vietnamese :
{
,→
question }
Paragraph :
```{ context }```
[ / INST ]
G.2
Summarization
Weak prompt:
[ INST ] Đoạn văn :
{document}
Tóm t ắt
đoạn văn
t r ên :
[ / INST ]
[ INST ]
Paragraph :
{document}
Summary
of
the
above
passage :
[ / INST ]
Medium prompt:
[ INST ] <<SYS>>
Nhi ệm vụcủa bạn
l à
t óm t ắt
đoạn văn bản sau ,
,→
đưa
ra
câu
t r ả
l ời
l à bản
t óm t ắt :
<</SYS>>
```{document}```
[ / INST ]
[ INST ] <<SYS>>
Your
task
i s
to
summarize
the
f o l l o w i n g
text ,
,→
g i v i n g
a summary
answer :
<</SYS>>
```{document}```
[ / INST ]

--- Page 17 ---

Table 5: Performance under few-shot prompting
(a) Sentiment analysis
VLSP 2016
UiT-VSFC
Models
AC↑
F1↑
AR↑
ECE↓
A@10↑
AC↑
F1↑
AR↑
ECE↓
A@10↑
URA-LLaMa 70B
0.66 ± 0.01
0.49 ± 0.01
0.72 ± 0.01
0.13 ± 0.01
0.77 ± 0.04
0.76 ± 0.01
0.48 ± 0.01
0.81 ± 0.01
0.16 ± 0.01
0.71 ± 0.02
URA-LLaMa 13B
0.59 ± 0.01
0.57 ± 0.01
0.67 ± 0.01
0.08 ± 0.01
0.82 ± 0.04
0.74 ± 0.01
0.52 ± 0.08
0.83 ± 0.01
0.10 ± 0.01
0.87 ± 0.02
URA-LLaMa 7B
0.57 ± 0.02
0.42 ± 0.05
0.69 ± 0.02
0.06 ± 0.02
0.77 ± 0.04
0.72 ± 0.01
0.43 ± 0.01
0.78 ± 0.01
0.13 ± 0.01
0.95 ± 0.03
LLaMa-2 70B
0.53 ± 0.01
0.38 ± 0.01
0.68 ± 0.01
0.34 ± 0.01
0.58 ± 0.05
0.60 ± 0.01
0.40 ± 0.01
0.65 ± 0.01
0.39 ± 0.01
0.25 ± 0.03
LLaMa-2 13B
0.51 ± 0.01
0.41 ± 0.06
0.66 ± 0.01
0.32 ± 0.02
0.80 ± 0.04
0.63 ± 0.01
0.46 ± 0.07
0.71 ± 0.01
0.13 ± 0.01
0.88 ± 0.02
LLaMa-2 7B
0.45 ± 0.01
0.32 ± 0.01
0.59 ± 0.01
0.26 ± 0.02
0.50 ± 0.05
0.50 ± 0.01
0.34 ± 0.01
0.69 ± 0.01
0.23 ± 0.01
0.62 ± 0.03
Vietcuna 7B
0.04 ± 0.01
0.05 ± 0.01
0.45 ± 0.01
0.71 ± 0.01
0.05 ± 0.02
0.03 ± 0.00
0.03 ± 0.00
0.53 ± 0.01
0.50 ± 0.00
0.01 ± 0.00
Vistral 7B Chat
0.28 ± 0.01
0.16 ± 0.01
0.86 ± 0.01
0.36 ± 0.01
0.15 ± 0.03
0.02 ± 0.00
0.07 ± 0.01
0.90 ± 0.01
0.78 ± 0.00
0.00 ± 0.00
MixSUra
0.62 ± 0.02
0.63 ± 0.01
0.59 ± 0.01
0.30 ± 0.01
0.59 ± 0.05
0.74 ± 0.01
0.46 ± 0.01
0.63 ± 0.01
0.23 ± 0.01
0.65 ± 0.03
GemSUra
0.00 ± 0.00
0.00 ± 0.00
0.72 ± 0.01
0.70 ± 0.01
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.89 ± 0.01
0.81 ± 0.00
0.00 ± 0.00
Gemini Pro
0.67 ± 0.01
0.50 ± 0.01
−
0.34 ± 0.01
0.65 ± 0.05
0.78 ± 0.01
0.49 ± 0.01
−
0.45 ± 0.01
0.82 ± 0.02
GPT-3.5
0.65 ± 0.01
0.59 ± 0.01
−
0.35 ± 0.01
0.54 ± 0.05
0.86 ± 0.01
0.73 ± 0.01
−
0.14 ± 0.01
0.85 ± 0.02
GPT-4
0.75 ± 0.01
0.74 ± 0.01
−
0.25 ± 0.01
0.74 ± 0.04
0.85 ± 0.01
0.53 ± 0.09
−
0.15 ± 0.01
0.87 ± 0.02
(b) Text classification
UiT-VSMEC
PhoATIS
Models
AC↑
F1↑
AR↑
ECE↓
A@10↑
AC↑
F1↑
AR↑
ECE↓
A@10↑
URA-LLaMa 70B
0.25 ± 0.02
0.15 ± 0.01
0.56 ± 0.01
0.25 ± 0.02
0.37 ± 0.06
0.15 ± 0.01
0.22 ± 0.03
0.83 ± 0.00
0.81 ± 0.01
0.13 ± 0.04
URA-LLaMa 13B
0.32 ± 0.02
0.12 ± 0.01
0.58 ± 0.01
0.22 ± 0.02
0.57 ± 0.07
0.01 ± 0.01
0.06 ± 0.02
0.47 ± 0.00
0.84 ± 0.01
0.00 ± 0.01
URA-LLaMa 7B
0.29 ± 0.02
0.11 ± 0.01
0.60 ± 0.01
0.12 ± 0.02
0.43 ± 0.06
0.06 ± 0.01
0.01 ± 0.00
0.55 ± 0.00
0.24 ± 0.01
0.08 ± 0.03
LLaMa-2 70B
0.24 ± 0.02
0.14 ± 0.01
0.63 ± 0.01
0.40 ± 0.02
0.76 ± 0.06
0.11 ± 0.01
0.08 ± 0.02
0.66 ± 0.01
0.51 ± 0.01
0.06 ± 0.02
LLaMa-2 13B
0.18 ± 0.02
0.08 ± 0.01
0.55 ± 0.01
0.45 ± 0.01
0.49 ± 0.07
0.02 ± 0.01
0.06 ± 0.02
0.57 ± 0.01
0.90 ± 0.01
0.01 ± 0.01
LLaMa-2 7B
0.25 ± 0.02
0.12 ± 0.01
0.57 ± 0.01
0.21 ± 0.02
0.54 ± 0.06
0.03 ± 0.01
0.02 ± 0.01
0.56 ± 0.01
0.54 ± 0.01
0.01 ± 0.01
Vietcuna 7B
0.15 ± 0.01
0.05 ± 0.01
0.46 ± 0.01
0.85 ± 0.01
0.15 ± 0.04
0.04 ± 0.01
0.01 ± 0.00
0.63 ± 0.00
0.21 ± 0.01
0.07 ± 0.03
Vistral 7B Chat
0.00 ± 0.00
0.00 ± 0.00
0.68 ± 0.01
0.38 ± 0.00
0.00 ± 0.00
0.00 ± 0.01
0.01 ± 0.01
0.81 ± 0.01
0.61 ± 0.00
0.00 ± 0.00
MixSUra
0.40 ± 0.02
0.36 ± 0.02
0.72 ± 0.01
0.53 ± 0.02
0.79 ± 0.05
0.81 ± 0.01
0.58 ± 0.03
0.96 ± 0.01
0.14 ± 0.01
0.91 ± 0.04
GemSUra
0.00 ± 0.00
0.00 ± 0.00
0.63 ± 0.01
0.56 ± 0.01
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.93 ± 0.01
0.68 ± 0.01
0.00 ± 0.00
Gemini Pro
0.48 ± 0.02
0.36 ± 0.02
−
0.33 ± 0.02
0.47 ± 0.05
0.82 ± 0.01
0.69 ± 0.03
−
0.76 ± 0.01
0.70 ± 0.04
GPT-3.5
0.42 ± 0.02
0.40 ± 0.02
−
0.58 ± 0.02
0.29 ± 0.06
0.69 ± 0.02
0.67 ± 0.03
−
0.31 ± 0.02
0.69 ± 0.05
GPT-4
0.49 ± 0.02
0.48 ± 0.02
−
0.51 ± 0.02
0.36 ± 0.06
0.85 ± 0.01
0.78 ± 0.03
−
0.15 ± 0.01
0.88 ± 0.04
(c) Knowledge
ZaloE2E
ViMMRC
Models
EM↑
F1↑
AC↑
F1↑
AR↑
ECE↓
A@10↑
URA-LLaMa 70B
0.34 ± 0.02
0.50 ± 0.02
0.78 ± 0.02
0.63 ± 0.03
0.90 ± 0.01
0.13 ± 0.02
0.96 ± 0.03
URA-LLaMa 13B
0.26 ± 0.02
0.40 ± 0.02
0.62 ± 0.02
0.50 ± 0.02
0.69 ± 0.02
0.18 ± 0.02
0.65 ± 0.07
URA-LLaMa 7B
0.01 ± 0.00
0.09 ± 0.02
0.42 ± 0.02
0.33 ± 0.02
0.61 ± 0.02
0.13 ± 0.02
0.38 ± 0.07
LLaMa-2 70B
0.25 ± 0.02
0.40 ± 0.02
0.65 ± 0.02
0.52 ± 0.02
0.79 ± 0.01
0.27 ± 0.02
0.71 ± 0.06
LLaMa-2 13B
0.22 ± 0.02
0.36 ± 0.02
0.58 ± 0.02
0.46 ± 0.02
0.62 ± 0.02
0.28 ± 0.02
0.75 ± 0.06
LLaMa-2 7B
0.07 ± 0.01
0.15 ± 0.01
0.30 ± 0.02
0.23 ± 0.02
0.56 ± 0.02
0.43 ± 0.02
0.16 ± 0.05
Vietcuna 7B
0.13 ± 0.01
0.21 ± 0.01
0.31 ± 0.02
0.18 ± 0.01
0.50 ± 0.00
0.06 ± 0.02
0.37 ± 0.06
Vistral 7B Chat
0.06 ± 0.01
0.16 ± 0.01
0.10 ± 0.01
0.13 ± 0.02
0.96 ± 0.01
0.75 ± 0.01
0.12 ± 0.06
MixSUra
0.19 ± 0.02
0.34 ± 0.02
0.65 ± 0.02
0.64 ± 0.02
0.54 ± 0.02
0.29 ± 0.02
0.65 ± 0.07
GemSUra
0.00 ± 0.00
0.04 ± 0.00
0.37 ± 0.02
0.23 ± 0.01
0.52 ± 0.02
0.12 ± 0.02
0.38 ± 0.07
Gemini Pro
0.46 ± 0.02
0.60 ± 0.02
0.89 ± 0.01
0.71 ± 0.09
−
0.64 ± 0.01
0.88 ± 0.05
GPT-3.5
0.49 ± 0.02
0.64 ± 0.02
0.90 ± 0.01
0.72 ± 0.03
−
0.09 ± 0.01
0.90 ± 0.04
GPT-4
0.49 ± 0.02
0.64 ± 0.02
0.91 ± 0.01
0.73 ± 0.04
−
0.09 ± 0.01
0.88 ± 0.04
(d) Toxicity detection
UiT-ViCTSD
UiT-ViHSD
Models
AC↑
F1↑
AR↑
ECE↓
A@10↑
AC↑
F1↑
AR↑
ECE↓
A@10↑
URA-LLaMa 70B
0.44 ± 0.01
0.27 ± 0.01
0.75 ± 0.01
0.52 ± 0.01
0.37 ± 0.02
0.17 ± 0.00
0.15 ± 0.00
0.64 ± 0.01
0.57 ± 0.00
0.27 ± 0.02
URA-LLaMa 13B
0.44 ± 0.01
0.27 ± 0.05
0.67 ± 0.01
0.33 ± 0.01
0.41 ± 0.03
0.26 ± 0.01
0.16 ± 0.00
0.61 ± 0.01
0.42 ± 0.01
0.21 ± 0.02
URA-LLaMa 7B
0.43 ± 0.01
0.40 ± 0.01
0.60 ± 0.01
0.29 ± 0.01
0.71 ± 0.02
0.16 ± 0.00
0.10 ± 0.00
0.67 ± 0.01
0.32 ± 0.00
0.28 ± 0.02
LLaMa-2 70B
0.26 ± 0.01
0.17 ± 0.01
0.67 ± 0.03
0.61 ± 0.02
0.32 ± 0.05
0.15 ± 0.00
0.14 ± 0.00
0.60 ± 0.01
0.72 ± 0.00
0.14 ± 0.01
LLaMa-2 13B
0.28 ± 0.01
0.19 ± 0.00
0.67 ± 0.01
0.52 ± 0.01
0.63 ± 0.03
0.17 ± 0.00
0.11 ± 0.00
0.62 ± 0.01
0.58 ± 0.00
0.44 ± 0.02
LLaMa-2 7B
0.16 ± 0.01
0.12 ± 0.01
0.61 ± 0.01
0.66 ± 0.01
0.08 ± 0.02
0.01 ± 0.00
0.01 ± 0.00
0.56 ± 0.01
0.66 ± 0.00
0.08 ± 0.02
Vietcuna 7B
0.08 ± 0.00
0.10 ± 0.01
0.50 ± 0.00
0.42 ± 0.00
0.08 ± 0.03
0.61 ± 0.01
0.21 ± 0.00
0.50 ± 0.00
0.28 ± 0.01
0.61 ± 0.02
Vistral 7B Chat
0.13 ± 0.01
0.08 ± 0.01
0.78 ± 0.02
0.50 ± 0.01
0.18 ± 0.04
0.15 ± 0.00
0.09 ± 0.00
0.74 ± 0.01
0.39 ± 0.00
0.33 ± 0.02
MixSUra
0.70 ± 0.01
0.39 ± 0.03
0.78 ± 0.02
0.29 ± 0.01
0.80 ± 0.04
0.58 ± 0.01
0.31 ± 0.01
0.68 ± 0.01
0.30 ± 0.01
0.93 ± 0.01
GemSUra
0.00 ± 0.00
0.00 ± 0.00
0.68 ± 0.03
0.79 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.72 ± 0.01
0.74 ± 0.00
0.00 ± 0.00
Gemini Pro
0.81 ± 0.01
0.43 ± 0.01
−
0.31 ± 0.01
0.82 ± 0.04
0.70 ± 0.01
0.37 ± 0.01
−
0.36 ± 0.01
0.69 ± 0.01
GPT-3.5
0.63 ± 0.02
0.54 ± 0.02
−
0.37 ± 0.02
0.70 ± 0.05
0.63 ± 0.01
0.47 ± 0.01
−
0.37 ± 0.01
0.63 ± 0.02
GPT-4
0.89 ± 0.00
0.71 ± 0.01
−
0.11 ± 0.00
0.91 ± 0.03
0.77 ± 0.01
0.57 ± 0.01
−
0.23 ± 0.01
0.77 ± 0.02
(e) Information retrieval
mMARCO
mRobust04
Models
M@10↑
M@10B↑
N@10↑
N@10B↑
M@10↑
M@10B↑
N@10↑
N@10B↑
URA-LLaMa 70B
0.05 ± 0.00
0.11 ± 0.00
0.06 ± 0.00
0.14 ± 0.00
0.04 ± 0.00
0.04 ± 0.00
0.03 ± 0.00
0.04 ± 0.00
URA-LLaMa 13B
0.04 ± 0.00
0.10 ± 0.00
0.06 ± 0.00
0.14 ± 0.00
0.03 ± 0.00
0.05 ± 0.00
0.04 ± 0.00
0.04 ± 0.00
URA-LLaMa 7B
0.04 ± 0.00
0.11 ± 0.00
0.06 ± 0.00
0.16 ± 0.00
0.03 ± 0.00
0.03 ± 0.00
0.02 ± 0.00
0.02 ± 0.00
LLaMa-2 70B
0.03 ± 0.00
0.08 ± 0.00
0.04 ± 0.00
0.11 ± 0.00
0.05 ± 0.00
0.05 ± 0.00
0.01 ± 0.00
0.01 ± 0.00
LLaMa-2 13B
0.07 ± 0.00
0.15 ± 0.00
0.09 ± 0.00
0.21 ± 0.00
0.05 ± 0.00
0.04 ± 0.00
0.04 ± 0.00
0.04 ± 0.00
LLaMa-2 7B
0.05 ± 0.00
0.11 ± 0.00
0.07 ± 0.00
0.16 ± 0.00
0.02 ± 0.00
0.03 ± 0.00
0.03 ± 0.00
0.02 ± 0.00
Vietcuna 7B
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
Vistral 7B Chat
0.14 ± 0.00
0.30 ± 0.00
0.18 ± 0.00
0.38 ± 0.00
0.03 ± 0.00
0.03 ± 0.00
0.01 ± 0.00
0.01 ± 0.00
MixSUra
0.01 ± 0.00
0.07 ± 0.00
0.04 ± 0.00
0.11 ± 0.00
0.04 ± 0.00
0.04 ± 0.00
0.02 ± 0.00
0.02 ± 0.00
GemSUra
0.03 ± 0.00
0.11 ± 0.00
0.05 ± 0.00
0.15 ± 0.00
0.05 ± 0.01
0.05 ± 0.01
0.02 ± 0.00
0.02 ± 0.00
Gemini Pro
−
−
−
−
−
−
−
−
GPT-3.5
−
−
−
−
−
−
−
−
GPT-4
−
−
−
−
−
−
−
−
(f) Language modeling
MLQA-MLM
VSEC
Models
EM↑
CER↓
WER↓
CED↓
WED↓
PLX↓
EM↑
CER↓
WER↓
CED↓
WED↓
PLX↓
URA-LLaMa 70B
0.01 ± 0.00
0.69 ± 0.00
0.74 ± 0.00
671.13 ± 10.38
158.36 ± 2.33
1.23 ± 0.05
0.33 ± 0.00
0.14 ± 0.00
0.22 ± 0.00
18.63 ± 0.42
6.63 ± 0.11
1.13 ± 0.00
URA-LLaMa 13B
0.01 ± 0.00
0.60 ± 0.01
0.70 ± 0.01
571.35 ± 11.23
145.40 ± 2.68
1.49 ± 0.10
0.35 ± 0.00
0.04 ± 0.00
0.12 ± 0.00
5.73 ± 0.12
3.74 ± 0.03
1.15 ± 0.00
URA-LLaMa 7B
0.01 ± 0.00
0.54 ± 0.01
0.61 ± 0.01
512.76 ± 11.01
127.97 ± 2.58
1.24 ± 0.01
0.22 ± 0.00
0.36 ± 0.01
0.42 ± 0.01
48.38 ± 1.54
12.75 ± 0.34
1.07 ± 0.00
LLaMa-2 70B
0.00 ± 0.00
0.89 ± 0.00
0.97 ± 0.00
852.19 ± 11.04
203.26 ± 2.53
1.00 ± 0.00
0.01 ± 0.00
0.83 ± 0.00
0.96 ± 0.00
110.36 ± 0.54
28.84 ± 0.14
1.00 ± 0.00
LLaMa-2 13B
0.01 ± 0.00
0.80 ± 0.00
0.91 ± 0.00
767.32 ± 11.91
190.29 ± 2.85
1.24 ± 0.03
0.16 ± 0.00
0.05 ± 0.00
0.14 ± 0.00
6.30 ± 0.16
4.07 ± 0.04
1.01 ± 0.00
LLaMa-2 7B
0.00 ± 0.00
0.82 ± 0.00
0.97 ± 0.00
777.18 ± 10.51
201.81 ± 2.57
1.74 ± 0.19
0.12 ± 0.00
0.38 ± 0.01
0.45 ± 0.01
50.29 ± 0.86
13.58 ± 0.19
1.06 ± 0.00
Vietcuna 7B
0.00 ± 0.00
0.99 ± 0.00
0.99 ± 0.00
945.07 ± 12.47
206.78 ± 2.79
1.40 ± 0.00
0.00 ± 0.00
8.34 ± 0.07
8.07 ± 0.07
1107.66 ± 7.64
243.52 ± 1.74
1.46 ± 0.00
Vistral 7B Chat
0.00 ± 0.00
0.95 ± 0.00
0.96 ± 0.00
906.01 ± 12.12
200.54 ± 2.63
1.00 ± 0.00
0.01 ± 0.00
2.33 ± 0.04
2.44 ± 0.04
309.72 ± 4.25
73.61 ± 0.96
1.00 ± 0.00
MixSUra
0.00 ± 0.00
0.52 ± 0.00
0.57 ± 0.00
488.41 ± 10.58
115.85 ± 2.50
1.00 ± 0.00
0.08 ± 0.00
0.19 ± 0.00
0.28 ± 0.00
25.13 ± 0.42
8.58 ± 0.10
1.00 ± 0.00
GemSUra
0.00 ± 0.00
0.95 ± 0.00
1.01 ± 0.00
904.32 ± 9.69
211.79 ± 2.13
1.42 ± 0.00
0.00 ± 0.00
1.56 ± 0.01
1.85 ± 0.02
206.68 ± 1.68
55.86 ± 0.41
1.46 ± 0.00
Gemini Pro
0.05 ± 0.00
0.11 ± 0.00
0.19 ± 0.00
103.40 ± 3.93
39.36 ± 0.88
−
0.71 ± 0.01
0.02 ± 0.00
0.03 ± 0.00
2.77 ± 0.45
0.87 ± 0.10
−
GPT-3.5
0.04 ± 0.00
0.42 ± 0.01
0.50 ± 0.01
402.97 ± 10.86
104.78 ± 2.46
−
0.66 ± 0.00
0.03 ± 0.00
0.11 ± 0.00
4.57 ± 0.08
3.22 ± 0.02
−
GPT-4
0.08 ± 0.00
0.37 ± 0.01
0.46 ± 0.01
353.24 ± 10.18
96.33 ± 2.34
−
0.75 ± 0.00
0.03 ± 0.00
0.10 ± 0.00
3.85 ± 0.04
3.01 ± 0.01
−
Normal prompt:

--- Page 18 ---

(g) Reasoning
SR - Natural
SR - Abstract symbol
MATH
Models
EM↑
F1↑
Equ.↑
EM↑
F1↑
Equ.↑
EM↑
F1↑
Equ.↑
URA-LLaMa 70B
0.14 ± 0.00
0.48 ± 0.00
0.15 ± 0.00
0.27 ± 0.00
0.85 ± 0.00
0.30 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.24 ± 0.02
URA-LLaMa 13B
0.08 ± 0.00
0.42 ± 0.00
0.08 ± 0.00
0.20 ± 0.00
0.70 ± 0.00
0.17 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.16 ± 0.01
URA-LLaMa 7B
0.04 ± 0.00
0.38 ± 0.00
0.04 ± 0.00
0.11 ± 0.00
0.61 ± 0.00
0.10 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.08 ± 0.01
LLaMa-2 70B
0.13 ± 0.00
0.48 ± 0.00
0.13 ± 0.00
0.26 ± 0.00
0.84 ± 0.00
0.27 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.29 ± 0.02
LLaMa-2 13B
0.03 ± 0.00
0.24 ± 0.00
0.04 ± 0.00
0.19 ± 0.00
0.69 ± 0.00
0.18 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.19 ± 0.02
LLaMa-2 7B
0.00 ± 0.00
0.01 ± 0.00
0.00 ± 0.00
0.06 ± 0.00
0.44 ± 0.00
0.06 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.13 ± 0.01
Vietcuna 7B
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.14 ± 0.00
0.71 ± 0.00
0.10 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.01 ± 0.00
Vistral 7B Chat
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.16 ± 0.01
MixSUra
0.07 ± 0.00
0.41 ± 0.00
0.07 ± 0.00
0.22 ± 0.00
0.78 ± 0.00
0.23 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.42 ± 0.02
GemSUra
0.00 ± 0.00
0.05 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.06 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.21 ± 0.01
Gemini Pro
0.15 ± 0.00
0.50 ± 0.00
0.16 ± 0.00
0.26 ± 0.00
0.83 ± 0.00
0.29 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.40 ± 0.02
GPT-3.5
0.15 ± 0.00
0.50 ± 0.00
0.16 ± 0.00
0.26 ± 0.00
0.83 ± 0.00
0.29 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.62 ± 0.02
GPT-4
0.37 ± 0.00
0.74 ± 0.00
0.42 ± 0.00
0.37 ± 0.00
0.87 ± 0.00
0.44 ± 0.00
0.00 ± 0.00
0.01 ± 0.00
0.65 ± 0.02
(h) Translation
PhoMT
OPUS100
Models
(En →Vi)
(Vi →En)
(En →Vi)
(Vi →En)
BLEU↑
hLEPOR↑
BLEU↑
hLEPOR↑
BLEU↑
hLEPOR↑
BLEU↑
hLEPOR↑
URA-LLaMa 70B
0.22 ± 0.00
0.58 ± 0.00
0.19 ± 0.00
0.56 ± 0.00
0.08 ± 0.00
0.41 ± 0.01
0.09 ± 0.00
0.37 ± 0.01
URA-LLaMa 13B
0.20 ± 0.00
0.54 ± 0.00
0.19 ± 0.00
0.54 ± 0.00
0.07 ± 0.01
0.37 ± 0.01
0.11 ± 0.01
0.39 ± 0.01
URA-LLaMa 7B
0.15 ± 0.00
0.49 ± 0.00
0.16 ± 0.00
0.52 ± 0.00
0.06 ± 0.00
0.36 ± 0.01
0.09 ± 0.01
0.36 ± 0.01
LLaMa-2 70B
0.27 ± 0.00
0.57 ± 0.00
0.17 ± 0.00
0.52 ± 0.00
0.11 ± 0.00
0.42 ± 0.01
0.08 ± 0.00
0.34 ± 0.01
LLaMa-2 13B
0.18 ± 0.00
0.52 ± 0.00
0.17 ± 0.00
0.52 ± 0.00
0.07 ± 0.00
0.37 ± 0.01
0.09 ± 0.01
0.36 ± 0.01
LLaMa-2 7B
0.14 ± 0.00
0.46 ± 0.00
0.15 ± 0.00
0.51 ± 0.00
0.05 ± 0.00
0.32 ± 0.00
0.07 ± 0.01
0.33 ± 0.01
Vietcuna 7B
0.11 ± 0.00
0.34 ± 0.00
0.01 ± 0.00
0.11 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.05 ± 0.00
0.15 ± 0.00
Vistral 7B Chat
0.25 ± 0.00
0.62 ± 0.00
0.21 ± 0.00
0.58 ± 0.00
0.11 ± 0.00
0.44 ± 0.01
0.11 ± 0.01
0.42 ± 0.01
MixSUra
0.15 ± 0.00
0.51 ± 0.00
0.16 ± 0.00
0.52 ± 0.00
0.07 ± 0.00
0.37 ± 0.01
0.09 ± 0.00
0.36 ± 0.01
GemSUra
0.02 ± 0.00
0.12 ± 0.00
0.01 ± 0.00
0.10 ± 0.00
0.02 ± 0.00
0.18 ± 0.00
0.01 ± 0.00
0.11 ± 0.00
Gemini Pro
0.27 ± 0.00
0.60 ± 0.00
0.24 ± 0.01
0.55 ± 0.00
0.06 ± 0.01
0.39 ± 0.01
0.13 ± 0.01
0.36 ± 0.01
GPT-3.5
0.33 ± 0.00
0.65 ± 0.00
0.24 ± 0.00
0.61 ± 0.00
0.12 ± 0.01
0.46 ± 0.01
0.15 ± 0.01
0.46 ± 0.00
GPT-4
0.26 ± 0.00
0.64 ± 0.00
0.25 ± 0.00
0.62 ± 0.00
0.13 ± 0.01
0.47 ± 0.01
0.16 ± 0.01
0.47 ± 0.00
Table 6: Performance on Reasoning - MATH under Chain-of-Thought prompting
Models
EM↑
F1↑
Equ.↑
URA-LLaMa 70B
0.00 ± 0.00
0.15 ± 0.01
0.26 ± 0.02
URA-LLaMa 13B
0.00 ± 0.00
0.16 ± 0.01
0.12 ± 0.01
URA-LLaMa 7B
0.00 ± 0.00
0.19 ± 0.01
0.07 ± 0.01
LLaMa-2 70B
0.00 ± 0.00
0.11 ± 0.01
0.28 ± 0.02
LLaMa-2 13B
0.00 ± 0.00
0.12 ± 0.01
0.18 ± 0.02
LLaMa-2 7B
0.00 ± 0.00
0.10 ± 0.00
0.12 ± 0.02
Vietcuna 7B
0.00 ± 0.00
0.02 ± 0.00
0.01 ± 0.00
Vistral 7B Chat
0.00 ± 0.00
0.08 ± 0.00
0.11 ± 0.01
MixSUra
0.00 ± 0.00
0.18 ± 0.01
0.41 ± 0.02
GemSUra
0.00 ± 0.00
0.25 ± 0.00
0.32 ± 0.02
Gemini Pro
0.00 ± 0.00
0.27 ± 0.01
0.61 ± 0.01
GPT-3.5
0.00 ± 0.00
0.29 ± 0.01
0.77 ± 0.02
GPT-4
0.00 ± 0.00
0.30 ± 0.01
0.71 ± 0.02
Table 7: Performance under weaker zero-shot prompting
(a) Question-answering - weak prompting
XQuAD
MLQA
Models
EM↑
F1↑
EM↑
F1↑
URA-LLaMa 70B
0.21 ± 0.01
0.47 ± 0.01
0.14 ± 0.01
0.41 ± 0.00
URA-LLaMa 13B
0.22 ± 0.01
0.43 ± 0.01
0.17 ± 0.01
0.40 ± 0.01
URA-LLaMa 7B
0.13 ± 0.00
0.32 ± 0.00
0.10 ± 0.00
0.32 ± 0.00
LLaMa-2 70B
0.13 ± 0.00
0.38 ± 0.01
0.09 ± 0.00
0.36 ± 0.00
LLaMa-2 13B
0.04 ± 0.00
0.28 ± 0.00
0.04 ± 0.00
0.28 ± 0.00
LLaMa-2 7B
0.06 ± 0.00
0.24 ± 0.00
0.05 ± 0.00
0.24 ± 0.00
Vistral 7B Chat
0.32 ± 0.01
0.56 ± 0.01
0.21 ± 0.01
0.46 ± 0.01
MixSUra
0.13 ± 0.00
0.38 ± 0.01
0.09 ± 0.00
0.36 ± 0.00
GemSUra
0.05 ± 0.01
0.14 ± 0.01
0.04 ± 0.00
0.11 ± 0.00
(b) Question-Answering - medium prompting
XQuAD
MLQA
Models
EM↑
F1↑
EM↑
F1↑
URA-LLaMa 70B
0.08 ± 0.00
0.33 ± 0.00
0.07 ± 0.00
0.31 ± 0.00
URA-LLaMa 13B
0.04 ± 0.00
0.21 ± 0.00
0.04 ± 0.00
0.19 ± 0.00
URA-LLaMa 7B
0.01 ± 0.00
0.11 ± 0.00
0.01 ± 0.00
0.11 ± 0.00
LLaMa-2 70B
0.00 ± 0.00
0.17 ± 0.00
0.00 ± 0.00
0.17 ± 0.00
LLaMa-2 13B
0.00 ± 0.00
0.10 ± 0.00
0.00 ± 0.00
0.09 ± 0.00
LLaMa-2 7B
0.00 ± 0.00
0.03 ± 0.00
0.00 ± 0.00
0.03 ± 0.00
Vistral 7B Chat
0.03 ± 0.01
0.07 ± 0.01
0.05 ± 0.00
0.09 ± 0.00
MixSUra
0.01 ± 0.00
0.25 ± 0.01
0.00 ± 0.00
0.25 ± 0.00
GemSUra
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
(c) Summarization - weak prompting
VietNews
WikiLingua
Models
R1↑
R2↑
RL↑
SC↑
BS↑
Cv↑
De↑
Cp↑
R1↑
R2↑
RL↑
SC↑
BS↑
Cv↑
De↑
Cp↑
URA-LLaMa 70B
0.49 ± 0.00
0.23 ± 0.00
0.31 ± 0.00
0.58 ± 0.00
0.05 ± 0.11
0.89 ± 0.00
8.90 ± 0.03
18.48 ± 0.59
0.47 ± 0.00
0.20 ± 0.00
0.29 ± 0.00
0.48 ± 0.00
0.19 ± 0.13
0.86 ± 0.00
6.83 ± 0.09
25.30 ± 1.86
URA-LLaMa 13B
0.27 ± 0.00
0.12 ± 0.00
0.18 ± 0.00
0.31 ± 0.00
0.05 ± 0.11
0.56 ± 0.00
5.00 ± 0.04
153.55 ± 0.99
0.22 ± 0.00
0.09 ± 0.00
0.14 ± 0.00
0.22 ± 0.00
0.20 ± 0.007
0.48 ± 0.00
3.49 ± 0.04
190.09 ± 4.92
URA-LLaMa 7B
0.45 ± 0.00
0.21 ± 0.00
0.39 ± 0.00
0.26 ± 0.00
0.03 ± 0.09
0.91 ± 0.00
9.43 ± 0.03
6.42 ± 0.05
0.42 ± 0.00
0.18 ± 0.00
0.27 ± 0.00
0.32 ± 0.00
0.07 ± 0.12
0.89 ± 0.00
7.58 ± 0.05
7.14 ± 0.14
LLaMa-2 70B
0.34 ± 0.00
0.17 ± 0.00
0.22 ± 0.00
0.39 ± 0.00
−0.04 ± 0.15
0.71 ± 0.00
7.26 ± 0.04
18.42 ± 0.69
0.27 ± 0.00
0.12 ± 0.00
0.17 ± 0.00
0.29 ± 0.00
0.05 ± 0.13
0.58 ± 0.01
8.11 ± 0.17
21.64 ± 1.67
LLaMa-2 13B
0.45 ± 0.00
0.22 ± 0.00
0.29 ± 0.00
0.53 ± 0.00
0.00 ± 0.14
0.92 ± 0.00
9.49 ± 0.02
8.46 ± 0.29
0.47 ± 0.00
0.22 ± 0.00
0.29 ± 0.00
0.53 ± 0.00
0.34 ± 0.12
0.92 ± 0.00
9.39 ± 0.05
17.94 ± 2.84
LLaMa-2 7B
0.36 ± 0.00
0.17 ± 0.00
0.23 ± 0.00
0.33 ± 0.00
−0.15 ± 0.12
0.69 ± 0.00
6.35 ± 0.03
7.59 ± 0.21
0.45 ± 0.00
0.20 ± 0.00
0.27 ± 0.00
0.48 ± 0.00
0.36 ± 0.00
0.83 ± 0.00
7.71 ± 0.07
12.39 ± 1.46
Vistral 7B Chat
0.45 ± 0.00
0.22 ± 0.00
0.28 ± 0.00
0.28 ± 0.00
0.03 ± 0.10
0.72 ± 0.00
6.32 ± 0.10
6.49 ± 0.03
0.43 ± 0.00
0.21 ± 0.00
0.28 ± 0.00
0.04 ± 0.00
0.25 ± 0.09
0.65 ± 0.00
2.37 ± 0.06
4.57 ± 0.04
MixSUra
0.44 ± 0.00
0.22 ± 0.00
0.29 ± 0.00
0.74 ± 0.00
0.07 ± 0.08
0.97 ± 0.00
35.67 ± 0.13
9.43 ± 0.26
0.47 ± 0.00
0.22 ± 0.00
0.29 ± 0.00
0.14 ± 0.00
0.19 ± 0.08
0.97 ± 0.00
28.97 ± 0.30
10.27 ± 0.91
GemSUra
0.37 ± 0.00
0.09 ± 0.00
0.22 ± 0.00
−0.09 ± 0.00
0.07 ± 0.04
0.10 ± 0.00
0.12 ± 0.00
8.16 ± 0.12
0.40 ± 0.00
0.09 ± 0.00
0.23 ± 0.00
−0.09 ± 0.00
−0.24 ± 0.07
0.06 ± 0.00
0.07 ± 0.00
10.10 ± 0.25
(d) Summarization - medium prompting
VietNews
WikiLingua
Models
R1↑
R2↑
RL↑
SC↑
BS↑
Cv↑
De↑
Cp↑
R1↑
R2↑
RL↑
SC↑
BS↑
Cv↑
De↑
Cp↑
URA-LLaMa 70B
0.35 ± 0.00
0.16 ± 0.00
0.24 ± 0.00
0.34 ± 0.00
0.12 ± 0.00
0.63 ± 0.00
5.43 ± 0.02
37.78 ± 0.47
0.33 ± 0.00
0.14 ± 0.00
0.22 ± 0.00
0.30 ± 0.00
0.24 ± 0.10
0.59 ± 0.01
4.62 ± 0.11
56.56 ± 1.70
URA-LLaMa 13B
0.26 ± 0.00
0.12 ± 0.00
0.17 ± 0.00
0.22 ± 0.00
−0.08 ± 0.18
0.46 ± 0.00
3.55 ± 0.04
47.75 ± 0.65
0.14 ± 0.00
0.05 ± 0.00
0.09 ± 0.00
0.10 ± 0.00
−0.14 ± 0.12
0.26 ± 0.01
1.83 ± 0.06
60.10 ± 2.16
URA-LLaMa 7B
0.41 ± 0.00
0.18 ± 0.00
0.27 ± 0.00
0.36 ± 0.00
−0.08 ± 0.13
0.83 ± 0.00
8.13 ± 0.04
8.08 ± 0.17
0.42 ± 0.00
0.17 ± 0.00
0.27 ± 0.00
0.35 ± 0.00
0.27 ± 0.21
0.84 ± 0.00
7.15 ± 0.08
8.08 ± 0.36
LLaMa-2 70B
0.09 ± 0.00
0.03 ± 0.00
0.07 ± 0.00
0.03 ± 0.00
−0.20 ± 0.11
0.15 ± 0.00
1.07 ± 0.02
19.69 ± 0.27
0.03 ± 0.00
0.00 ± 0.00
0.03 ± 0.00
−0.02 ± 0.00
−0.22 ± 0.11
0.10 ± 0.00
0.42 ± 0.06
37.50 ± 0.61
LLaMa-2 13B
0.02 ± 0.00
0.00 ± 0.00
0.02 ± 0.00
−0.05 ± 0.00
−0.19 ± 0.05
0.01 ± 0.00
0.01 ± 0.00
54.67 ± 0.16
0.03 ± 0.00
0.00 ± 0.00
0.03 ± 0.00
−0.05 ± 0.00
−0.05 ± 0.03
0.02 ± 0.00
0.02 ± 0.00
42.55 ± 0.81
LLaMa-2 7B
0.03 ± 0.00
0.01 ± 0.00
0.03 ± 0.00
−0.04 ± 0.00
−0.17 ± 0.03
0.04 ± 0.00
0.07 ± 0.00
23.86 ± 0.26
0.02 ± 0.00
0.00 ± 0.00
0.02 ± 0.00
−0.02 ± 0.00
−0.04 ± 0.06
0.02 ± 0.00
0.03 ± 0.00
40.31 ± 0.88
Vistral 7B Chat
0.04 ± 0.00
0.02 ± 0.00
0.02 ± 0.00
0.03 ± 0.00
−0.19 ± 0.10
0.98 ± 0.00
1.34 ± 0.01
518.90 ± 1.06
0.18 ± 0.00
0.09 ± 0.00
0.12 ± 0.00
0.03 ± 0.00
−0.19 ± 0.18
0.87 ± 0.00
1.60 ± 0.01
347.61 ± 6.29
MixSUra
0.06 ± 0.00
0.01 ± 0.00
0.04 ± 0.00
−0.02 ± 0.00
−0.13 ± 0.05
0.10 ± 0.00
0.17 ± 0.00
9.03 ± 0.54
0.03 ± 0.00
0.00 ± 0.00
0.03 ± 0.00
0.04 ± 0.00
−0.01 ± 0.05
0.17 ± 0.00
0.26 ± 0.01
16.68 ± 1.94
GemSUra
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
−0.19 ± 0.05
1.00 ± 0.00
1.00 ± 0.00
550.22 ± 2.60
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
−0.19 ± 0.03
1.00 ± 0.00
1.00 ± 0.00
589.41 ± 5.60
[ INST ] <<SYS>>
Bạn
l à một
t r ợ
l ý hữu dụng ,
bi ết
t ôn
t r ọng và
,→
th ành
th ật .
Bạn
lu ôn
lu ôn
t r ả
l ời
các
,→
câu hỏi một
cách
có
í ch
nhi ều nhất
có
,→
th ể,
nhưng đồng
th ời
phải
an
to àn . Câ
,→u
t r ả
l ời
của bạn không được
bao
gồm c
,→ác
ngôn
từđộc hại ,
phân
bi ệt
chủng
t ộ
,→c ,
phân
bi ệt
g i ới
t í nh ,
nguy
hi ểm,
nội
,→
dung
vi
phạm pháp
lu ật .
Nhi ệm vụcủa
,→bạn
l à
t óm t ắt
đoạn văn bản nằm trong
,→
t r i p l e
backtick .
Bà i
t óm t ắt
phải
đầy
,→đủcác
th ông
t i n
quan
t r ọng ,
ngắn gọn
,→và
thu hút
người
đọc .
Ngôn ngữbạn phả
,→
i
sửdụng để
t óm t ắt
l à
t i ếng
Vi ệt .
<</SYS>>
```{document}```
[ / INST ]

--- Page 19 ---

Table 8: Fairness performance
(a) Question-Answering
XQuAD
MLQA
Models
Exact Match↑
F1↑
Exact Match↑
F1↑
URA-LLaMa 70B
0.04 ± 0.00
0.28 ± 0.00
0.03 ± 0.00
0.26 ± 0.00
URA-LLaMa 13B
0.00 ± 0.00
0.14 ± 0.00
0.00 ± 0.00
0.15 ± 0.00
URA-LLaMa 7B
0.00 ± 0.00
0.13 ± 0.00
0.00 ± 0.00
0.15 ± 0.01
LLaMa-2 70B
0.00 ± 0.00
0.10 ± 0.00
0.00 ± 0.00
0.11 ± 0.00
LLaMa-2 13B
0.00 ± 0.00
0.03 ± 0.00
0.00 ± 0.00
0.04 ± 0.00
LLaMa-2 7B
0.00 ± 0.00
0.04 ± 0.00
0.00 ± 0.00
0.05 ± 0.00
Vietcuna 7B
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
Vistral 7B Chat
0.01 ± 0.00
0.03 ± 0.00
0.01 ± 0.00
0.02 ± 0.00
MixSUra
0.00 ± 0.00
0.16 ± 0.00
0.00 ± 0.00
0.17 ± 0.00
GemSUra
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
Gemini Pro
0.13 ± 0.01
0.31 ± 0.01
0.09 ± 0.00
0.27 ± 0.00
GPT-3.5
0.00 ± 0.00
0.24 ± 0.00
0.00 ± 0.00
0.23 ± 0.00
GPT-4
0.00 ± 0.00
0.26 ± 0.00
0.00 ± 0.00
0.24 ± 0.00
(b) Sentiment analysis
VLSP 2016
UiT-VSFC
Models
AC↑
F1↑
AR↑
ECE↓
A@10↑
AC↑
F1↑
AR↑
ECE↓
A@10↑
URA-LLaMa 70B
0.65 ± 0.01
0.49 ± 0.01
0.72 ± 0.01
0.13 ± 0.01
0.77 ± 0.04
0.75 ± 0.01
0.48 ± 0.01
0.81 ± 0.01
0.17 ± 0.01
0.66 ± 0.03
URA-LLaMa 13B
0.58 ± 0.01
0.57 ± 0.01
0.67 ± 0.01
0.07 ± 0.01
0.83 ± 0.04
0.75 ± 0.01
0.46 ± 0.08
0.83 ± 0.01
0.11 ± 0.01
0.88 ± 0.02
URA-LLaMa 7B
0.74 ± 0.02
0.39 ± 0.06
0.83 ± 0.01
0.21 ± 0.02
0.98 ± 0.02
0.73 ± 0.01
0.43 ± 0.01
0.78 ± 0.01
0.13 ± 0.01
0.94 ± 0.01
LLaMa-2 70B
0.52 ± 0.02
0.38 ± 0.01
0.68 ± 0.01
0.34 ± 0.02
0.58 ± 0.05
0.60 ± 0.01
0.40 ± 0.01
0.65 ± 0.01
0.39 ± 0.01
0.28 ± 0.02
LLaMa-2 13B
0.51 ± 0.01
0.36 ± 0.06
0.66 ± 0.01
0.32 ± 0.02
0.79 ± 0.04
0.63 ± 0.01
0.41 ± 0.02
0.70 ± 0.01
0.13 ± 0.01
0.89 ± 0.02
LLaMa-2 7B
0.45 ± 0.02
0.34 ± 0.01
0.59 ± 0.01
0.26 ± 0.02
0.50 ± 0.0
0.51 ± 0.01
0.35 ± 0.01
0.69 ± 0.01
0.22 ± 0.01
0.64 ± 0.03
Vietcuna 7B
0.04 ± 0.01
0.04 ± 0.01
0.45 ± 0.01
0.71 ± 0.01
0.05 ± 0.02
0.03 ± 0.00
0.03 ± 0.00
0.55 ± 0.01
0.50 ± 0.00
0.01 ± 0.00
Vistral 7B Chat
0.28 ± 0.02
0.16 ± 0.01
0.86 ± 0.01
0.36 ± 0.02
0.16 ± 0.03
0.02 ± 0.00
0.07 ± 0.01
0.90 ± 0.00
0.77 ± 0.00
0.00 ± 0.00
MixSUra
0.62 ± 0.02
0.62 ± 0.02
0.59 ± 0.01
0.30 ± 0.01
0.59 ± 0.05
0.74 ± 0.01
0.46 ± 0.01
0.61 ± 0.01
0.24 ± 0.01
0.66 ± 0.03
GemSUra
0.00 ± 0.00
0.00 ± 0.00
0.73 ± 0.01
0.70 ± 0.01
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.89 ± 0.01
0.81 ± 0.00
0.00 ± 0.00
Gemini Pro
0.67 ± 0.02
0.50 ± 0.01
−
0.34 ± 0.02
0.59 ± 0.05
0.79 ± 0.01
0.50 ± 0.01
−
0.46 ± 0.01
0.82 ± 0.02
GPT-3.5
0.66 ± 0.01
0.60 ± 0.01
−
0.35 ± 0.01
0.52 ± 0.05
0.86 ± 0.01
0.71 ± 0.01
−
0.14 ± 0.01
0.86 ± 0.02
GPT-4
0.75 ± 0.01
0.74 ± 0.01
−
0.25 ± 0.00
0.73 ± 0.04
0.85 ± 0.01
0.71 ± 0.01
−
0.15 ± 0.01
0.87 ± 0.02
(c) Text classification
UiT-VSMEC
PhoATIS
Models
AC↑
F1↑
AR↑
ECE↓
A@10↑
AC↑
F1↑
AR↑
ECE↓
A@10↑
URA-LLaMa 70B
0.24 ± 0.02
0.14 ± 0.01
0.55 ± 0.01
0.26 ± 0.02
0.37 ± 0.06
0.15 ± 0.01
0.22 ± 0.03
0.83 ± 0.00
0.81 ± 0.01
0.13 ± 0.04
URA-LLaMa 13B
0.31 ± 0.02
0.11 ± 0.01
0.58 ± 0.01
0.23 ± 0.02
0.57 ± 0.06
0.01 ± 0.01
0.06 ± 0.02
0.47 ± 0.00
0.84 ± 0.01
0.00 ± 0.01
URA-LLaMa 7B
0.29 ± 0.02
0.10 ± 0.01
0.60 ± 0.01
0.12 ± 0.02
0.41 ± 0.06
0.06 ± 0.01
0.01 ± 0.00
0.55 ± 0.00
0.24 ± 0.01
0.08 ± 0.03
LLaMa-2 70B
0.23 ± 0.02
0.14 ± 0.01
0.63 ± 0.01
0.40 ± 0.02
0.73 ± 0.06
0.11 ± 0.01
0.08 ± 0.01
0.66 ± 0.01
0.51 ± 0.01
0.06 ± 0.03
LLaMa-2 13B
0.18 ± 0.02
0.08 ± 0.01
0.55 ± 0.01
0.45 ± 0.01
0.44 ± 0.06
0.02 ± 0.01
0.06 ± 0.02
0.57 ± 0.01
0.90 ± 0.01
0.01 ± 0.01
LLaMa-2 7B
0.25 ± 0.02
0.11 ± 0.01
0.57 ± 0.01
0.22 ± 0.02
0.53 ± 0.06
0.02 ± 0.00
0.02 ± 0.01
0.60 ± 0.01
0.68 ± 0.01
0.01 ± 0.01
Vietcuna 7B
0.15 ± 0.01
0.05 ± 0.01
0.51 ± 0.01
0.85 ± 0.01
0.16 ± 0.04
0.04 ± 0.01
0.01 ± 0.00
0.64 ± 0.01
0.21 ± 0.01
0.07 ± 0.03
Vistral 7B Chat
0.00 ± 0.00
0.00 ± 0.00
0.69 ± 0.01
0.38 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.01 ± 0.01
0.81 ± 0.01
0.61 ± 0.01
0.00 ± 0.00
MixSUra
0.41 ± 0.02
0.32 ± 0.03
0.72 ± 0.01
0.53 ± 0.02
0.79 ± 0.05
0.81 ± 0.02
0.58 ± 0.02
0.96 ± 0.01
0.14 ± 0.01
0.91 ± 0.04
GemSUra
0.00 ± 0.00
0.00 ± 0.00
0.64 ± 0.01
0.57 ± 0.01
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.93 ± 0.01
0.68 ± 0.01
0.00 ± 0.00
Gemini Pro
0.48 ± 0.02
0.38 ± 0.02
−
0.34 ± 0.02
0.43 ± 0.06
0.79 ± 0.01
0.67 ± 0.02
−
0.73 ± 0.01
0.68 ± 0.04
GPT-3.5
0.44 ± 0.02
0.42 ± 0.02
−
0.56 ± 0.02
0.36 ± 0.06
0.68 ± 0.02
0.66 ± 0.03
−
0.32 ± 0.02
0.67 ± 0.05
GPT-4
0.49 ± 0.02
0.47 ± 0.02
−
0.51 ± 0.02
0.36 ± 0.06
0.83 ± 0.01
0.76 ± 0.03
−
0.17 ± 0.01
0.87 ± 0.04
(d) Toxicity detection
UiT-ViCTSD
UiT-ViHSD
Models
AC↑
F1↑
AR↑
ECE↓
A@10↑
AC↑
F1↑
AR↑
ECE↓
A@10↑
URA-LLaMa 70B
0.41 ± 0.02
0.26 ± 0.01
0.75 ± 0.01
0.53 ± 0.01
0.33 ± 0.05
0.15 ± 0.00
0.14 ± 0.00
0.64 ± 0.01
0.58 ± 0.00
0.24 ± 0.02
URA-LLaMa 13B
0.43 ± 0.02
0.27 ± 0.07
0.66 ± 0.01
0.36 ± 0.02
0.42 ± 0.05
0.24 ± 0.01
0.15 ± 0.00
0.61 ± 0.01
0.43 ± 0.01
0.21 ± 0.02
URA-LLaMa 7B
0.42 ± 0.02
0.39 ± 0.01
0.60 ± 0.01
0.30 ± 0.01
0.66 ± 0.05
0.16 ± 0.00
0.10 ± 0.00
0.67 ± 0.01
0.33 ± 0.00
0.28 ± 0.02
LLaMa-2 70B
0.24 ± 0.01
0.16 ± 0.01
0.68 ± 0.03
0.63 ± 0.01
0.32 ± 0.05
0.14 ± 0.00
0.14 ± 0.00
0.60 ± 0.01
0.72 ± 0.00
0.14 ± 0.01
LLaMa-2 13B
0.27 ± 0.01
0.18 ± 0.01
0.67 ± 0.01
0.53 ± 0.01
0.57 ± 0.05
0.16 ± 0.00
0.10 ± 0.00
0.62 ± 0.01
0.59 ± 0.00
0.42 ± 0.02
LLaMa-2 7B
0.15 ± 0.01
0.11 ± 0.01
0.62 ± 0.01
0.67 ± 0.01
0.07 ± 0.03
0.01 ± 0.00
0.01 ± 0.00
0.56 ± 0.01
0.71 ± 0.00
0.01 ± 0.00
Vietcuna 7B
0.08 ± 0.01
0.09 ± 0.01
0.50 ± 0.01
0.42 ± 0.01
0.06 ± 0.03
0.62 ± 0.01
0.21 ± 0.00
0.50 ± 0.00
0.29 ± 0.01
0.62 ± 0.02
Vistral 7B Chat
0.12 ± 0.01
0.08 ± 0.01
0.79 ± 0.02
0.50 ± 0.01
0.16 ± 0.04
0.15 ± 0.00
0.08 ± 0.00
0.74 ± 0.01
0.39 ± 0.00
0.33 ± 0.02
MixSUra
0.69 ± 0.01
0.38 ± 0.02
0.78 ± 0.02
0.29 ± 0.01
0.78 ± 0.03
0.56 ± 0.01
0.31 ± 0.01
0.68 ± 0.01
0.32 ± 0.01
0.92 ± 0.01
GemSUra
0.00 ± 0.00
0.00 ± 0.00
0.71 ± 0.02
0.80 ± 0.01
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.72 ± 0.01
0.74 ± 0.00
0.00 ± 0.00
Gemini Pro
0.81 ± 0.01
0.44 ± 0.03
−
0.31 ± 0.01
0.82 ± 0.04
0.68 ± 0.01
0.37 ± 0.01
−
0.35 ± 0.01
0.67 ± 0.02
GPT-3.5
0.61 ± 0.02
0.52 ± 0.02
−
0.40 ± 0.02
0.63 ± 0.05
0.61 ± 0.01
0.46 ± 0.01
−
0.39 ± 0.01
0.62 ± 0.02
GPT-4
0.87 ± 0.01
0.69 ± 0.02
−
0.13 ± 0.01
0.86 ± 0.03
0.76 ± 0.01
0.56 ± 0.01
−
0.24 ± 0.01
0.76 ± 0.02
(e) Language modeling
MLQA-MLM
VSEC
Models
EM↑
CER↓
WER↓
CED↓
WED↓
PLX↓
EM↑
CER↓
WER↓
CED↓
WED↓
PLX↓
URA-LLaMa 70B
0.01 ± 0.00
0.69 ± 0.01
0.74 ± 0.01
663.29 ± 12.05
157.60 ± 2.73
1.25 ± 0.06
0.30 ± 0.00
0.14 ± 0.00
0.22 ± 0.00
18.69 ± 0.42
6.67 ± 0.11
1.13 ± 0.00
URA-LLaMa 13B
0.02 ± 0.00
0.56 ± 0.01
0.64 ± 0.01
531.42 ± 11.19
134.78 ± 2.66
1.48 ± 0.11
0.32 ± 0.00
0.04 ± 0.00
0.13 ± 0.00
5.90 ± 0.11
3.79 ± 0.03
1.15 ± 0.00
URA-LLaMa 7B
0.01 ± 0.00
0.53 ± 0.01
0.60 ± 0.01
508.49 ± 11.32
127.77 ± 2.72
1.22 ± 0.01
0.20 ± 0.00
0.36 ± 0.01
0.42 ± 0.01
47.81 ± 1.57
12.77 ± 0.35
1.07 ± 0.00
LLaMa-2 70B
0.00 ± 0.00
0.90 ± 0.00
0.98 ± 0.00
858.96 ± 10.86
206.70 ± 2.53
1.00 ± 0.00
0.01 ± 0.00
0.84 ± 0.00
0.96 ± 0.00
111.58 ± 0.56
29.08 ± 0.14
1.00 ± 0.00
LLaMa-2 13B
0.01 ± 0.00
0.82 ± 0.00
0.92 ± 0.00
787.50 ± 11.71
195.54 ± 2.83
1.27 ± 0.04
0.15 ± 0.00
0.05 ± 0.00
0.13 ± 0.00
6.31 ± 0.16
4.08 ± 0.04
1.01 ± 0.00
LLaMa-2 7B
0.00 ± 0.00
0.80 ± 0.00
0.95 ± 0.00
769.24 ± 10.65
200.67 ± 2.66
1.75 ± 0.20
0.12 ± 0.00
0.38 ± 0.01
0.45 ± 0.01
50.27 ± 0.85
13.59 ± 0.19
1.06 ± 0.00
Vietcuna 7B
0.00 ± 0.00
0.99 ± 0.00
0.99 ± 0.00
949.80 ± 12.48
209.79 ± 2.81
1.40 ± 0.00
0, 06 ± 0.00
4.97 ± 0.06
4.86 ± 0.06
660.14 ± 8.58
146.84 ± 1.94
1.46 ± 0.01
Vistral 7B Chat
0.00 ± 0.00
0.96 ± 0.00
0.97 ± 0.00
917.24 ± 11.53
204.67 ± 2.49
1.00 ± 0.00
0.00 ± 0.00
2.33 ± 0.04
2.44 ± 0.04
309.88 ± 4.32
73.85 ± 0.99
1.00 ± 0.00
MixSUra
0.00 ± 0.00
0.56 ± 0.00
0.63 ± 0.00
535.76 ± 10.02
133.64 ± 2.33
1.00 ± 0.00
0.07 ± 0.00
0.20 ± 0.00
0.29 ± 0.00
25.96 ± 0.42
8.79 ± 0.10
1.00 ± 0.00
GemSUra
0.00 ± 0.00
0.95 ± 0.00
1.02 ± 0.00
908.58 ± 10.70
214.95 ± 2.36
1.42 ± 0.00
0.00 ± 0.00
1.53 ± 0.01
1.82 ± 0.01
203.14 ± 1.54
54.97 ± 0.39
1.46 ± 0.00
Gemini Pro
0.03 ± 0.00
0.10 ± 0.00
0.18 ± 0.00
99.05 ± 4.19
133.64 ± 1.00
−
0.64 ± 0.00
0.02 ± 0.00
0.03 ± 0.00
2.62 ± 0.14
0.85 ± 0.03
−
GPT-3.5
0.03 ± 0.00
0.43 ± 0.01
0.51 ± 0.01
413.47 ± 11.01
108.06 ± 2.54
−
0.59 ± 0.00
0.04 ± 0.00
0.11 ± 0.00
4.93 ± 0.08
3.34 ± 0.02
−
GPT-4
0.06 ± 0.00
0.38 ± 0.01
0.47 ± 0.01
363.29 ± 10.23
99.39 ± 2.41
−
0.67 ± 0.00
0.03 ± 0.00
0.10 ± 0.00
4.24 ± 0.04
3.14 ± 0.01
−
[ INST ] <<SYS>>
You
are
a
h e l p f u l ,
r e s p e c t f u l
and
honest
,→
a s s i s t a n t .
You
should
always
answer
,→
q u e s t i o n s
as
h e l p f u l l y
as
p o s s i b l e ,
,→but
at
the
same
time
be
s a f e .
Your
,→
r e p l y
must
not
i n c l u d e
malicious ,
,→
r a c i s t ,
s e x i s t ,
dangerous ,
or
i l l e g a l
,→
content .
Your
task
i s
to
summarize
the
,→
text
in
the
t r i p l e
backtick .
The
,→summary
should
be
f u l l
of
important
,→
information ,
c o n c i s e
and
a t t r a c t i v e
to
,→
the
reader .
The
language
you must
use
,→
to
summarize
i s
Vietnamese .
<</SYS>>
```{document}```
[ / INST ]
G.3
Sentiment Analysis
[ INST ] <<SYS>>
Hãy xem mì nh
l à một
Bot
có
th ể
phân
l o ại
cảm
,→xúc
của một
câu
t i ếng
Vi ệt .
Bot
lu ôn đ
,→ưa
câu
t r ả
l ời
của mì nh ởdạng
con
s ố.
,→
Trong đó ,
g i á
t r ị
0
cho
cảm xúc
t i êu
,→cực ,
1
cho
cảm xúc
trung
l ập ,
2
cho
cả
,→m xúc
t í ch
cực .
Bot không được
tự
t r ả
,→
l ời
hay
g i ảdạng
th ành Khách .
Và đây
l à
cuộc
t r ò
chuy ện mới
nhất
g i ữa Bot v
,→à Khách .
<</SYS>>

--- Page 20 ---

Table 9: Performance under zero-shot prompting with typographical error
(a) Question-Answering
XQuAD
MLQA
Models
EM↑
F1↑
EM↑
F1↑
URA-LLaMa 70B
0.01 ± 0.00
0.17 ± 0.00
0.01 ± 0.00
0.18 ± 0.00
URA-LLaMa 13B
0.00 ± 0.00
0.09 ± 0.00
0.00 ± 0.00
0.10 ± 0.00
URA-LLaMa 7B
0.00 ± 0.00
0.09 ± 0.00
0.00 ± 0.00
0.10 ± 0.00
LLaMa-2 70B
0.00 ± 0.00
0.04 ± 0.00
0.00 ± 0.00
0.05 ± 0.00
LLaMa-2 13B
0.00 ± 0.00
0.02 ± 0.00
0.00 ± 0.00
0.03 ± 0.00
LLaMa-2 7B
0.00 ± 0.00
0.02 ± 0.00
0.00 ± 0.00
0.02 ± 0.00
Vietcuna 7B
0.00 ± 0.00
0.06 ± 0.00
0.00 ± 0.00
0.05 ± 0.00
Vistral 7B Chat
0.02 ± 0.00
0.04 ± 0.00
0.02 ± 0.00
0.04 ± 0.00
MixSUra
0.00 ± 0.00
0.11 ± 0.00
0.00 ± 0.00
0.12 ± 0.00
GemSUra
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
Gemini Pro
0.10 ± 0.01
0.30 ± 0.01
0.08 ± 0.00
0.28 ± 0.00
GPT-3.5
0.00 ± 0.00
0.19 ± 0.00
0.00 ± 0.00
0.20 ± 0.00
GPT-4
0.00 ± 0.00
0.24 ± 0.00
0.00 ± 0.00
0.25 ± 0.00
(b) Summarization
VietNews
WikiLingua
Models
R1↑
R2↑
RL↑
SC↑
BS↑
Cv↑
De↑
Cp↑
R1↑
R2↑
RL↑
SC↑
BS↑
Cv↑
De↑
Cp↑
URA-LLaMa 70B
0.34 ± 0.00
0.16 ± 0.00
0.23 ± 0.00
−0.07 ± 0.00
−0.10 ± 0.18
0.19 ± 0.00
0.19 ± 0.00
61.65 ± 0.87
0.28 ± 0.00
0.11 ± 0.00
0.19 ± 0.00
0.31 ± 0.00
0.25 ± 0.23
0.50 ± 0.01
0.51 ± 0.01
167.42 ± 7.09
URA-LLaMa 13B
0.35 ± 0.00
0.14 ± 0.00
0.23 ± 0.00
0.21 ± 0.00
−0.07 ± 0.17
0.64 ± 0.00
0.65 ± 0.00
134.65 ± 3.76
0.20 ± 0.00
0.07 ± 0.00
0.13 ± 0.00
0.10 ± 0.00
0.20 ± 0.11
0.38 ± 0.00
0.38 ± 0.00
103.69 ± 3.33
URA-LLaMa 7B
0.37 ± 0.00
0.12 ± 0.00
0.24 ± 0.00
0.08 ± 0.00
−0.24 ± 0.18
0.65 ± 0.00
0.65 ± 0.00
17.92 ± 0.87
0.37 ± 0.00
0.12 ± 0.00
0.24 ± 0.00
0.12 ± 0.00
0.11 ± 0.18
0.65 ± 0.00
0.65 ± 0.00
20.49 ± 0.95
LLaMa-2 70B
0.13 ± 0.00
0.04 ± 0.00
0.09 ± 0.00
0.02 ± 0.00
−0.06 ± 0.03
0.20 ± 0.00
0.20 ± 0.00
90.95 ± 0.85
0.06 ± 0.00
0.02 ± 0.00
0.04 ± 0.00
0.02 ± 0.00
−0.19 ± 0.13
0.11 ± 0.00
0.11 ± 0.00
85.29 ± 1.05
LLaMa-2 13B
0.05 ± 0.00
0.01 ± 0.00
0.04 ± 0.00
−0.04 ± 0.00
−0.21 ± 0.18
0.03 ± 0.00
0.03 ± 0.00
55.91 ± 0.65
0.04 ± 0.00
0.00 ± 0.00
0.03 ± 0.00
−0.04 ± 0.00
0.09 ± 0.00
0.05 ± 0.00
0.05 ± 0.00
66.85 ± 6.72
LLaMa-2 7B
0.05 ± 0.00
0.01 ± 0.00
0.05 ± 0.00
−0.08 ± 0.00
−0.19 ± 0.04
0.07 ± 0.00
0.07 ± 0.00
55.29 ± 0.88
0.04 ± 0.00
0.00 ± 0.00
0.04 ± 0.00
−0.07 ± 0.00
0.15 ± 0.00
0.06 ± 0.00
0.06 ± 0.00
58.32 ± 3.32
Vietcuna 7B
0.03 ± 0.00
0.01 ± 0.00
0.02 ± 0.00
0.01 ± 0.00
−0.18 ± 0.06
0.91 ± 0.00
0.91 ± 0.00
1026.61 ± 3.86
0.08 ± 0.00
0.02 ± 0.00
0.05 ± 0.00
0.01 ± 0.00
−0.19 ± 0.05
0.78 ± 0.00
0.78 ± 0.00
852.27 ± 8.64
Vistral 7B Chat
0.09 ± 0.00
0.04 ± 0.00
0.06 ± 0.00
0.08 ± 0.00
−0.19 ± 0.12
0.92 ± 0.00
0.92 ± 0.00
860.65 ± 3.41
0.03 ± 0.00
0.01 ± 0.00
0.02 ± 0.00
0.02 ± 0.00
−0.19 ± 0.10
0.97 ± 0.00
0.97 ± 0.00
1012.67 ± 13.31
MixSUra
0.41 ± 0.00
0.19 ± 0.00
0.26 ± 0.00
0.23 ± 0.00
0.00 ± 0.11
0.83 ± 0.00
0.84 ± 0.00
30.65 ± 1.57
0.46 ± 0.00
0.21 ± 0.00
0.28 ± 0.00
0.12 ± 0.00
0.29 ± 0.07
0.87 ± 0.00
0.87 ± 0.00
20.80 ± 1.14
GemSUra
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
−0.19 ± 0.05
1.00 ± 0.00
1.00 ± 0.00
1121.14 ± 3.67
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
−0.19 ± 0.07
1.00 ± 0.00
1.00 ± 0.00
1120.44 ± 7.07
Gemini Pro
0.43 ± 0.00
0.21 ± 0.00
0.27 ± 0.00
0.26 ± 0.00
−0.04 ± 0.10
0.79 ± 0.00
0.79 ± 0.00
41.68 ± 0.48
0.36 ± 0.00
0.16 ± 0.00
0.24 ± 0.00
0.21 ± 0.00
0.33 ± 0.12
0.70 ± 0.00
0.70 ± 0.10
141.57 ± 3.26
GPT-3.5
0.34 ± 0.00
0.19 ± 0.00
0.23 ± 0.00
0.46 ± 0.00
0.05 ± 0.14
0.81 ± 0.00
0.81 ± 0.00
128.44 ± 2.94
0.39 ± 0.00
0.19 ± 0.00
0.25 ± 0.00
0.55 ± 0.00
0.28 ± 0.11
0.82 ± 0.00
0.82 ± 0.00
200.90 ± 7.40
GPT-4
0.39 ± 0.00
0.21 ± 0.00
0.26 ± 0.00
0.43 ± 0.00
0.04 ± 0.00
0.83 ± 0.00
0.83 ± 0.71
24.48 ± 0.00
0.45 ± 0.00
0.20 ± 0.00
0.27 ± 0.00
0.41 ± 0.00
0.28 ± 0.00
0.80 ± 0.03
0.81 ± 0.00
20.40 ± 1.59
(c) Sentiment analysis
VLSP 2016
UiT-VSFC
Models
AC↑
F1↑
AR↑
ECE↓
A@10↑
AC↑
F1↑
AR↑
ECE↓
A@10↑
URA-LLaMa 70B
0.63 ± 0.01
0.48 ± 0.01
0.60 ± 0.01
0.09 ± 0.01
0.83 ± 0.04
0.71 ± 0.01
0.45 ± 0.01
0.80 ± 0.01
0.08 ± 0.01
0.99 ± 0.01
URA-LLaMa 13B
0.55 ± 0.02
0.52 ± 0.02
0.59 ± 0.01
0.06 ± 0.01
0.74 ± 0.05
0.72 ± 0.01
0.44 ± 0.05
0.77 ± 0.01
0.18 ± 0.01
0.77 ± 0.02
URA-LLaMa 7B
0.52 ± 0.02
0.36 ± 0.03
0.59 ± 0.01
0.07 ± 0.01
0.66 ± 0.05
0.73 ± 0.01
0.41 ± 0.01
0.71 ± 0.01
0.16 ± 0.01
0.87 ± 0.02
LLaMa-2 70B
0.47 ± 0.01
0.32 ± 0.01
0.63 ± 0.01
0.38 ± 0.01
0.53 ± 0.05
0.49 ± 0.01
0.34 ± 0.01
0.61 ± 0.01
0.43 ± 0.01
0.28 ± 0.03
LLaMa-2 13B
0.46 ± 0.02
0.30 ± 0.01
0.55 ± 0.01
0.39 ± 0.02
0.70 ± 0.05
0.66 ± 0.01
0.40 ± 0.01
0.63 ± 0.01
0.11 ± 0.01
0.89 ± 0.02
LLaMa-2 7B
0.45 ± 0.02
0.36 ± 0.01
0.54 ± 0.01
0.20 ± 0.02
0.51 ± 0.05
0.51 ± 0.01
0.33 ± 0.01
0.65 ± 0.01
0.15 ± 0.01
0.80 ± 0.02
Vietcuna 7B
0.44 ± 0.02
0.27 ± 0.01
0.53 ± 0.01
0.26 ± 0.02
0.53 ± 0.05
0.49 ± 0.01
0.25 ± 0.03
0.46 ± 0.01
0.33 ± 0.01
0.34 ± 0.03
Vistral 7B Chat
0.31 ± 0.01
0.12 ± 0.00
0.81 ± 0.01
0.26 ± 0.02
0.04 ± 0.02
0.06 ± 0.00
0.03 ± 0.00
0.88 ± 0.01
0.67 ± 0.01
0.02 ± 0.01
MixSUra
0.59 ± 0.01
0.59 ± 0.01
0.55 ± 0.01
0.34 ± 0.02
0.52 ± 0.05
0.69 ± 0.01
0.44 ± 0.01
0.61 ± 0.01
0.29 ± 0.01
0.66 ± 0.03
GemSUra
0.00 ± 0.00
0.00 ± 0.00
0.67 ± 0.01
0.68 ± 0.01
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.77 ± 0.01
0.74 ± 0.00
0.00 ± 0.00
Gemini Pro
0.66 ± 0.01
0.49 ± 0.01
−
0.32 ± 0.01
0.59 ± 0.04
0.78 ± 0.01
0.49 ± 0.01
−
0.45 ± 0.01
0.82 ± 0.02
GPT-3.5
0.64 ± 0.01
0.60 ± 0.01
−
0.36 ± 0.01
0.54 ± 0.05
0.86 ± 0.01
0.71 ± 0.01
−
0.14 ± 0.01
0.86 ± 0.02
GPT-4
0.74 ± 0.00
0.73 ± 0.00
−
0.26 ± 0.00
0.71 ± 0.00
0.83 ± 0.00
0.70 ± 0.00
−
0.17 ± 0.00
0.85 ± 0.00
(d) Text classification
UiT-VSMEC
PhoATIS
Models
AC↑
F1↑
AR↑
ECE↓
A@10↑
AC↑
F1↑
AR↑
ECE↓
A@10↑
URA-LLaMa 70B
0.25 ± 0.00
0.16 ± 0.00
0.56 ± 0.02
0.20 ± 0.00
0.33 ± 0.00
0.16 ± 0.02
0.26 ± 0.03
0.79 ± 0.00
0.79 ± 0.02
0.08 ± 0.06
URA-LLaMa 13B
0.30 ± 0.00
0.11 ± 0.00
0.51 ± 0.01
0.26 ± 0.00
0.44 ± 0.00
0.01 ± 0.01
0.05 ± 0.01
0.47 ± 0.01
0.84 ± 0.01
0.00 ± 0.04
URA-LLaMa 7B
0.29 ± 0.00
0.10 ± 0.00
0.57 ± 0.01
0.17 ± 0.00
0.30 ± 0.00
0.02 ± 0.01
0.04 ± 0.00
0.55 ± 0.01
0.18 ± 0.01
0.01 ± 0.02
LLaMa-2 70B
0.21 ± 0.01
0.11 ± 0.01
0.61 ± 0.01
0.43 ± 0.01
0.70 ± 0.06
0.12 ± 0.01
0.10 ± 0.01
0.60 ± 0.02
0.46 ± 0.01
0.04 ± 0.02
LLaMa-2 13B
0.19 ± 0.00
0.07 ± 0.00
0.52 ± 0.01
0.47 ± 0.00
0.43 ± 0.00
0.02 ± 0.00
0.06 ± 0.00
0.57 ± 0.01
0.91 ± 0.00
0.01 ± 0.00
LLaMa-2 7B
0.17 ± 0.00
0.10 ± 0.00
0.55 ± 0.00
0.33 ± 0.00
0.29 ± 0.00
0.01 ± 0.01
0.00 ± 0.00
0.56 ± 0.00
0.69 ± 0.01
0.02 ± 0.02
Vietcuna 7B
0.09 ± 0.00
0.09 ± 0.00
0.51 ± 0.01
0.91 ± 0.00
0.09 ± 0.00
0.02 ± 0.01
0.01 ± 0.00
0.55 ± 0.01
0.23 ± 0.01
0.02 ± 0.01
Vistral 7B Chat
0.11 ± 0.01
0.12 ± 0.02
0.66 ± 0.01
0.21 ± 0.01
0.11 ± 0.04
0.20 ± 0.01
0.36 ± 0.02
0.79 ± 0.02
0.44 ± 0.01
0.22 ± 0.04
MixSUra
0.35 ± 0.02
0.27 ± 0.01
0.70 ± 0.01
0.58 ± 0.02
0.70 ± 0.05
0.80 ± 0.02
0.55 ± 0.04
0.94 ± 0.02
0.15 ± 0.02
0.88 ± 0.06
GemSUra
0.00 ± 0.00
0.00 ± 0.00
0.58 ± 0.02
0.58 ± 0.01
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.92 ± 0.01
0.64 ± 0.01
0.00 ± 0.00
Gemini Pro
0.46 ± 0.02
0.37 ± 0.02
−
0.32 ± 0.02
0.43 ± 0.06
0.64 ± 0.02
0.18 ± 0.01
−
0.59 ± 0.02
0.59 ± 0.05
GPT-3.5
0.42 ± 0.00
0.41 ± 0.00
−
0.58 ± 0.00
0.30 ± 0.00
0.68 ± 0.02
0.64 ± 0.03
−
0.32 ± 0.02
0.70 ± 0.05
GPT-4
0.48 ± 0.00
0.45 ± 0.00
−
0.52 ± 0.00
0.40 ± 0.00
0.86 ± 0.01
0.80 ± 0.02
−
0.14 ± 0.01
0.91 ± 0.03
(e) Knowledge
ZaloE2E
ViMMRC
Models
EM↑
F1↑
AC↑
F1↑
AR↑
ECE↓
A@10↑
URA-LLaMa 70B
0.23 ± 0.00
0.37 ± 0.00
0.65 ± 0.00
0.53 ± 0.00
0.84 ± 0.00
0.11 ± 0.00
0.77 ± 0.00
URA-LLaMa 13B
0.18 ± 0.00
0.30 ± 0.00
0.41 ± 0.00
0.34 ± 0.00
0.61 ± 0.00
0.22 ± 0.00
0.58 ± 0.00
URA-LLaMa 7B
0.00 ± 0.00
0.05 ± 0.00
0.33 ± 0.02
0.28 ± 0.02
0.61 ± 0.01
0.19 ± 0.02
0.33 ± 0.06
LLaMa-2 70B
0.12 ± 0.01
0.24 ± 0.02
0.47 ± 0.02
0.38 ± 0.02
0.46 ± 0.01
0.21 ± 0.02
0.44 ± 0.08
LLaMa-2 13B
0.13 ± 0.00
0.21 ± 0.00
0.39 ± 0.00
0.31 ± 0.00
0.56 ± 0.00
0.46 ± 0.00
0.33 ± 0.00
LLaMa-2 7B
0.02 ± 0.00
0.05 ± 0.00
0.26 ± 0.01
0.20 ± 0.01
0.51 ± 0.01
0.46 ± 0.01
0.13 ± 0.03
Vietcuna 7B
0.05 ± 0.00
0.15 ± 0.00
0.26 ± 0.01
0.14 ± 0.00
0.50 ± 0.00
0.01 ± 0.01
0.21 ± 0.07
Vistral 7B Chat
0.05 ± 0.01
0.14 ± 0.01
0.49 ± 0.02
0.47 ± 0.02
0.94 ± 0.01
0.29 ± 0.02
0.65 ± 0.07
MixSUra
0.13 ± 0.02
0.24 ± 0.02
0.57 ± 0.02
0.45 ± 0.02
0.53 ± 0.02
0.35 ± 0.02
0.58 ± 0.07
GemSUra
0.00 ± 0.00
0.03 ± 0.00
0.33 ± 0.02
0.17 ± 0.01
0.50 ± 0.02
0.16 ± 0.02
0.35 ± 0.07
Gemini Pro
0.39 ± 0.02
0.55 ± 0.02
0.84 ± 0.02
0.68 ± 0.01
−
0.59 ± 0.02
0.85 ± 0.05
GPT-3.5
0.45 ± 0.01
0.61 ± 0.01
0.90 ± 0.01
0.72 ± 0.04
−
0.10 ± 0.01
0.88 ± 0.07
GPT-4
0.44 ± 0.01
0.61 ± 0.01
0.91 ± 0.01
0.73 ± 0.07
−
0.09 ± 0.07
0.88 ± 0.04
(f) Toxicity
UiT-ViCTSD
UiT-ViHSD
Models
AC↑
F1↑
AR↑
ECE↓
A@10↑
AC↑
F1↑
AR↑
ECE↓
A@10↑
URA-LLaMa 70B
0.32 ± 0.00
0.21 ± 0.00
0.72 ± 0.01
0.62 ± 0.00
0.33 ± 0.00
0.14 ± 0.00
0.12 ± 0.00
0.64 ± 0.02
0.61 ± 0.00
0.23 ± 0.00
URA-LLaMa 13B
0.27 ± 0.00
0.26 ± 0.00
0.56 ± 0.00
0.56 ± 0.00
0.12 ± 0.00
0.18 ± 0.00
0.11 ± 0.00
0.57 ± 0.01
0.45 ± 0.00
0.20 ± 0.00
URA-LLaMa 7B
0.22 ± 0.00
0.21 ± 0.00
0.63 ± 0.00
0.39 ± 0.00
0.36 ± 0.00
0.12 ± 0.00
0.07 ± 0.00
0.62 ± 0.00
0.38 ± 0.00
0.19 ± 0.00
LLaMa-2 70B
0.17 ± 0.01
0.11 ± 0.01
0.64 ± 0.03
0.73 ± 0.01
0.27 ± 0.05
0.11 ± 0.00
0.11 ± 0.00
0.57 ± 0.01
0.75 ± 0.00
0.07 ± 0.01
LLaMa-2 13B
0.12 ± 0.00
0.11 ± 0.00
0.56 ± 0.01
0.66 ± 0.00
0.12 ± 0.00
0.10 ± 0.00
0.07 ± 0.00
0.59 ± 0.01
0.62 ± 0.00
0.24 ± 0.00
LLaMa-2 7B
0.04 ± 0.00
0.04 ± 0.00
0.62 ± 0.00
0.86 ± 0.00
0.02 ± 0.00
0.01 ± 0.00
0.00 ± 0.00
0.54 ± 0.00
0.79 ± 0.00
0.00 ± 0.00
Vietcuna 7B
0.11 ± 0.00
0.11 ± 0.00
0.54 ± 0.00
0.39 ± 0.00
0.13 ± 0.00
0.09 ± 0.00
0.05 ± 0.00
0.50 ± 0.00
0.24 ± 0.00
0.08 ± 0.00
Vistral 7B Chat
0.11 ± 0.01
0.07 ± 0.01
0.66 ± 0.02
0.48 ± 0.01
0.10 ± 0.04
0.09 ± 0.00
0.05 ± 0.00
0.72 ± 0.01
0.42 ± 0.00
0.17 ± 0.01
MixSUra
0.72 ± 0.01
0.39 ± 0.01
0.74 ± 0.02
0.25 ± 0.01
0.81 ± 0.04
0.66 ± 0.01
0.31 ± 0.01
0.67 ± 0.01
0.21 ± 0.01
0.82 ± 0.01
GemSUra
0.00 ± 0.00
0.00 ± 0.00
0.65 ± 0.03
0.78 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.00 ± 0.00
0.64 ± 0.01
0.68 ± 0.00
0.00 ± 0.00
Gemini Pro
0.81 ± 0.01
0.43 ± 0.01
−
0.31 ± 0.01
0.85 ± 0.04
0.71 ± 0.00
0.37 ± 0.00
−
0.37 ± 0.01
0.70 ± 0.02
GPT-3.5
0.51 ± 0.00
0.46 ± 0.00
−
0.49 ± 0.00
0.54 ± 0.00
0.64 ± 0.00
0.47 ± 0.00
−
0.36 ± 0.00
0.63 ± 0.00
GPT-4
0.88 ± 0.00
0.71 ± 0.00
−
0.12 ± 0.00
0.88 ± 0.00
0.78 ± 0.00
0.56 ± 0.00
−
0.22 ± 0.00
0.78 ± 0.00
Hãy đọc
k ĩ
và phân
t í ch
sentiment
từKhách .
,→Sau đó ,
đưa
ra
câu
t r ả
l ời
của bạn dướ
,→
i
dạng
json
với
đ ịnh dạng
l à
``` json
{
,→
" sentiment " :
`câu
t r ả
l ời
của bạn 0
(
,→
t i êu cực )
hay
1
( trung
l ập)
hay
2
( t í
,→ch
cực ) ` ,
" c o n f i d e n t _ l e v e l " :
`độ
tự

--- Page 21 ---

(g) Translation
PhoMT
OPUS100
Models
(En →Vi)
(Vi →En)
(En →Vi)
(Vi →En)
BLEU↑
hLEPOR↑
BLEU↑
hLEPOR↑
BLEU↑
hLEPOR↑
BLEU↑
hLEPOR↑
URA-LLaMa 70B
0.20 ± 0.00
0.56 ± 0.00
0.12 ± 0.00
0.48 ± 0.00
0.06 ± 0.00
0.38 ± 0.01
0.06 ± 0.00
0.32 ± 0.00
URA-LLaMa 13B
0.18 ± 0.00
0.54 ± 0.00
0.13 ± 0.00
0.48 ± 0.00
0.06 ± 0.00
0.36 ± 0.01
0.08 ± 0.00
0.34 ± 0.00
URA-LLaMa 7B
0.12 ± 0.00
0.46 ± 0.00
0.10 ± 0.00
0.45 ± 0.00
0.05 ± 0.00
0.33 ± 0.00
0.06 ± 0.00
0.31 ± 0.01
LLaMa-2 70B
0.22 ± 0.00
0.53 ± 0.00
0.07 ± 0.00
0.39 ± 0.00
0.07 ± 0.00
0.37 ± 0.01
0.05 ± 0.00
0.27 ± 0.01
LLaMa-2 13B
0.16 ± 0.00
0.50 ± 0.00
0.08 ± 0.00
0.42 ± 0.00
0.05 ± 0.00
0.34 ± 0.01
0.05 ± 0.00
0.29 ± 0.00
LLaMa-2 7B
0.10 ± 0.00
0.40 ± 0.00
0.08 ± 0.00
0.41 ± 0.00
0.04 ± 0.00
0.30 ± 0.00
0.05 ± 0.00
0.27 ± 0.00
Vietcuna 7B
0.12 ± 0.00
0.42 ± 0.00
0.08 ± 0.01
0.40 ± 0.00
0.07 ± 0.01
0.36 ± 0.01
0.09 ± 0.01
0.33 ± 0.00
Vistral 7B Chat
0.23 ± 0.00
0.60 ± 0.00
0.07 ± 0.00
0.38 ± 0.01
0.10 ± 0.00
0.42 ± 0.01
0.06 ± 0.00
0.33 ± 0.00
MixSUra
0.14 ± 0.00
0.50 ± 0.00
0.11 ± 0.00
0.46 ± 0.00
0.06 ± 0.00
0.36 ± 0.01
0.07 ± 0.00
0.34 ± 0.01
GemSUra
0.05 ± 0.00
0.32 ± 0.00
0.01 ± 0.00
0.16 ± 0.00
0.01 ± 0.00
0.15 ± 0.00
0.01 ± 0.00
0.09 ± 0.00
Gemini Pro
0.17 ± 0.01
0.57 ± 0.00
0.12 ± 0.01
0.49 ± 0.00
0.10 ± 0.01
0.42 ± 0.01
0.06 ± 0.01
0.30 ± 0.01
GPT-3.5
0.25 ± 0.00
0.62 ± 0.00
0.20 ± 0.00
0.57 ± 0.00
0.12 ± 0.01
0.45 ± 0.01
0.13 ± 0.01
0.43 ± 0.00
GPT-4
0.25 ± 0.00
0.63 ± 0.00
0.22 ± 0.00
0.59 ± 0.00
0.12 ± 0.01
0.46 ± 0.01
0.14 ± 0.01
0.45 ± 0.00
Table 10: Performance on Knowledge - ViMMRC under few-shot prompting with randomized answer orders
Models
AC↑
F1↑
AR↑
ECE↓
A@10↑
URA-LLaMa 70B
0.76 ± 0.02
0.61 ± 0.02
0.89 ± 0.01
0.14 ± 0.02
0.94 ± 0.04
URA-LLaMa 13B
0.62 ± 0.02
0.50 ± 0.02
0.69 ± 0.02
0.16 ± 0.02
0.67 ± 0.07
URA-LLaMa 7B
0.45 ± 0.02
0.36 ± 0.02
0.57 ± 0.02
0.09 ± 0.02
0.46 ± 0.07
LLaMa-2 70B
0.63 ± 0.02
0.51 ± 0.02
0.42 ± 0.02
0.27 ± 0.02
0.62 ± 0.08
LLaMa-2 13B
0.57 ± 0.02
0.46 ± 0.02
0.64 ± 0.02
0.29 ± 0.02
0.75 ± 0.07
LLaMa-2 7B
0.36 ± 0.02
0.27 ± 0.02
0.56 ± 0.02
0.36 ± 0.02
0.44 ± 0.07
Vietcuna 7B
0.26 ± 0.02
0.15 ± 0.01
0.50 ± 0.00
0.01 ± 0.01
0.31 ± 0.06
Vistral 7B Chat
0.08 ± 0.01
0.11 ± 0.01
0.95 ± 0.01
0.75 ± 0.01
0.06 ± 0.03
MixSUra
0.61 ± 0.02
0.61 ± 0.02
0.54 ± 0.02
0.31 ± 0.02
0.65 ± 0.07
GemSUra
0.35 ± 0.02
0.22 ± 0.01
0.52 ± 0.02
0.13 ± 0.02
0.31 ± 0.07
Gemini Pro
0.89 ± 0.02
0.72 ± 0.01
−
0.64 ± 0.02
0.90 ± 0.05
GPT-3.5
0.92 ± 0.01
0.74 ± 0.04
−
0.08 ± 0.01
0.90 ± 0.04
GPT-4
0.92 ± 0.01
0.74 ± 0.04
−
0.08 ± 0.01
0.88 ± 0.04
,→
t i n
cho
câu
t r ả
l ời
của bạn
trong
khoả
,→ng
từ0
t ới
1`
}```
{few_shot}
Khách :
"{ context }"
Bot :
[ / INST ]
[ INST ] <<SYS>>
Consider
y o u r s e l f
a Bot
that
can
c l a s s i f y
the
,→
sentiment
of
a
sentence
in
Vietnamese
,→
.
The
bot
always
g i v e s
i t s
answers
in
,→
numerical
form .
In
p a r t i c u l a r ,
the
,→
value
0
f o r
negative
emotions ,
1
f o r
,→
n e u t r a l
emotions ,
2
f o r
p o s i t i v e
,→emotions .
The Bot
cannot
answer
i t s e l f
,→
or
pretend
to
be
a
Guest .
And
t h i s
i s
the
l a t e s t
conversation
between
,→the
Bot and
the
Guest .
<</SYS>>
Read
c a r e f u l l y
and
analyze
the
sentiment
from
,→
the
Guest .
Then ,
give
your
answer
in
,→
json
format
with
the
format
``` json
{
,→" sentiment " :
` i s
your
answer
0
(
,→
negative )
or
1
( n e u t r a l )
or
2
(
,→
p o s i t i v e ) ` ,
" c o n f i d e n t _ l e v e l " :
`
,→
c o n f i d e n c e
in
your
answer
between
0
,→and
1`
}```
{few_shot}
Guest :
"{ context }"
Bot :
[ / INST ]
G.4
Text classification
UiT-VSMEC:
[ INST ] <<SYS>>
Hãy xem mì nh
l à một
Bot
có
th ể
phân
l o ại
cảm
,→xúc
của một
câu văn
trong
t i ếng
vi ệt .
,→Trong đó ,
g i á
t r ị
0
cho
Sadness ,
1
cho
,→
Surprise ,
2
cho
Disgust ,
3
cho
Fear ,
,→4
cho
Anger ,
5
cho
Other ,
6
cho
,→Enjoyment .
Bot không được
tự
t r ả
l ời
,→hay
g i ảdạng
th ành Khách .
Và đây
l à
cuộc
t r ò
chuy ện mới
nhất
g i ữa Bot v
,→à Khách .
<</SYS>>
Hãy đọc
k ĩ
và phân
t í ch
cảm xúc
từKhách
theo
,→
từng bước .
Sau đó ,
đưa
ra
câu
t r ả
l ời
,→
của bạn dưới
ds ạng JSON với
đ ịnh dạng
,→
l à
``` json
{
" tag " :
`câu
t r ả
l ời
của bạn
l à 0
cho
Sadness
,→hay
1
cho
S u r p r i s e
hay
2
cho
Disgust
,→hay
3
cho
Fear
hay
4
cho
Anger
hay
5
,→cho
Other
hay
6
cho
Enjoyment ` ,
" c o n f i d e n t _ l e v e l " :
`độ
tự
t i n
cho
câu
t r ả
l ời
,→
của bạn
trong
khoảng
từ0
t ới
1`
}
```
{few_shot}
Khách :
"{ context }"
Bot :
[ / INST ]
[ INST ] <<SYS>>
Consider
y o u r s e l f
a Bot
that
can
c l a s s i f y
,→emotions
of
a
sentence
in
Vietnamese .
,→Where ,
value
0
r e p r e s e n t s
Sadness ,
1
,→
r e p r e s e n t s
Surprise ,
2
r e p r e s e n t s
,→Disgust ,
3
r e p r e s e n t s
Fear ,
4
,→
r e p r e s e n t s
Anger ,
5
r e p r e s e n t s
Other ,
,→and 6
r e p r e s e n t s
Enjoyment .
The Bot
,→cannot
answer
i t s e l f
or
pretend
to
be
,→a
Guest .
And
t h i s
i s
the
l a t e s t
co nv er s at io n
between
,→the
Bot and
the
Guest .
<</SYS>>
Please
read
c a r e f u l l y
and
analyze
emotions
,→from
Guests
step
by
step .
Then
output
,→your
answer
as JSON with
the
format
``` json
{
" tag " :
`your
answer
i s
0
f o r
Sadness ,
or
1
,→
f o r
Surprise ,
or
2
f o r
Disgust ,
or
3
,→
f o r
Fear ,
or
4
f o r
Anger ,
or
5
f o r
,→Other ,
or
6
f o r
Enjoyment ` ,
" c o n f i d e n t _ l e v e l " :
` c o n f i d e n c e
in
your
answer
,→
between
0 and
1`
}
```
{few_shot}
Guest :
"{ context }"
Bot :
[ / INST ]
PhoATIS
[ INST ] <<SYS>>

--- Page 22 ---

Table 11: Bias and Toxicity performance. The “−” is marked for model whose generated texts do not contain
any bias words. DRR, DRG are demographic representations of races and genders. SAR, SAG are stereotypical
associations of races and genders
(a) Question-Answering
XQuAD
MLQA
Models
DRR↓
DRG↓
SAR↓
SAG↓
Tox↓
DRR↓
DRG↓
SAR↓
SAG↓
Tox↓
URA-LLaMa 70B
−
0.39 ± 0.01
−
0.41 ± 0.00
0.02 ± 0.00
−
0.14 ± 0.02
−
0.42 ± 0.03
0.02 ± 0.00
URA-LLaMa 13B
−
0.39 ± 0.01
−
0.45 ± 0.01
0.02 ± 0.00
−
0.17 ± 0.01
−
0.38 ± 0.00
0.02 ± 0.00
URA-LLaMa 7B
−
0.40 ± 0.01
−
0.48 ± 0.00
0.03 ± 0.00
−
0.18 ± 0.01
−
0.37 ± 0.01
0.02 ± 0.00
LLaMa-2 70B
−
0.36 ± 0.01
−
0.39 ± 0.00
0.01 ± 0.00
−
0.18 ± 0.00
−
0.41 ± 0.02
0.01 ± 0.00
LLaMa-2 13B
−
0.35 ± 0.03
−
0.46 ± 0.00
0.01 ± 0.00
−
0.27 ± 0.01
−
0.43 ± 0.00
0.01 ± 0.00
LLaMa-2 7B
−
0.46 ± 0.01
−
0.42 ± 0.00
0.01 ± 0.00
−
0.21 ± 0.06
−
0.45 ± 0.00
0.01 ± 0.00
Vietcuna 7B
−
0.50 ± 0.00
−
−
0.04 ± 0.00
−
0.23 ± 0.09
−
0.49 ± 0.01
0.04 ± 0.00
Vistral 7B Chat
−
0.37 ± 0.01
−
0.47 ± 0.02
0.04 ± 0.00
−
0.22 ± 0.00
−
0.50 ± 0.02
0.04 ± 0.00
MixSUra
−
0.42 ± 0.01
−
0.48 ± 0.00
0.02 ± 0.00
−
0.18 ± 0.00
−
0.38 ± 0.02
0.02 ± 0.00
GemSUra
−
0.39 ± 0.01
−
0.43 ± 0.01
0.04 ± 0.00
−
−
−
−
0.04 ± 0.00
Gemini Pro
−
0.38 ± 0.01
−
0.46 ± 0.00
0.02 ± 0.00
−
0.16 ± 0.00
−
0.43 ± 0.02
0.02 ± 0.00
GPT-3.5
−
0.43 ± 0.01
−
0.48 ± 0.00
0.02 ± 0.00
−
0.18 ± 0.01
−
0.40 ± 0.00
0.02 ± 0.00
GPT-4
−
0.40 ± 0.01
−
0.45 ± 0.00
0.02 ± 0.00
−
0.16 ± 0.01
−
0.41 ± 0.01
0.02 ± 0.00
(b) Summarization
VietNews
WikiLingua
Models
DRR↓
DRG↓
SAR↓
SAG↓
Tox↓
DRR↓
DRG↓
SAR↓
SAG↓
Tox↓
URA-LLaMa 70B
−
0.21 ± 0.01
−
0.31 ± 0.01
0.05 ± 0.00
−
0.03 ± 0.02
−
0.25 ± 0.02
0.03 ± 0.00
URA-LLaMa 13B
−
0.20 ± 0.01
−
0.29 ± 0.01
0.04 ± 0.00
−
0.07 ± 0.04
−
0.31 ± 0.03
0.02 ± 0.00
URA-LLaMa 7B
−
0.24 ± 0.02
−
0.33 ± 0.01
0.04 ± 0.00
−
0.07 ± 0.02
−
0.38 ± 0.02
0.03 ± 0.00
LLaMa-2 70B
−
0.24 ± 0.02
−
0.29 ± 0.01
0.02 ± 0.00
−
0.08 ± 0.01
−
0.29 ± 0.02
0.02 ± 0.00
LLaMa-2 13B
−
0.26 ± 0.01
−
0.38 ± 0.01
0.01 ± 0.00
−
0.17 ± 0.08
−
0.50 ± 0.02
0.01 ± 0.00
LLaMa-2 7B
−
0.28 ± 0.02
−
0.39 ± 0.01
0.01 ± 0.00
−
0.39 ± 0.05
−
0.50 ± 0.02
0.01 ± 0.00
Vietcuna 7B
−
0.21 ± 0.02
−
0.32 ± 0.02
0.04 ± 0.00
−
0.17 ± 0.04
−
0.39 ± 0.03
0.03 ± 0.00
Vistral 7B Chat
−
0.22 ± 0.02
−
0.37 ± 0.02
0.04 ± 0.00
−
0.02 ± 0.00
−
0.30 ± 0.02
0.03 ± 0.00
MixSUra
−
0.24 ± 0.01
−
0.29 ± 0.01
0.03 ± 0.00
−
0.00 ± 0.00
−
0.30 ± 0.02
0.02 ± 0.00
GemSUra
−
−
−
−
0.04 ± 0.00
−
−
−
−
0.04 ± 0.00
Gemini Pro
−
0.18 ± 0.01
−
0.26 ± 0.02
0.01 ± 0.00
−
0.01 ± 0.00
−
0.22 ± 0.01
0.01 ± 0.00
GPT-3.5
−
0.22 ± 0.01
−
0.29 ± 0.01
0.04 ± 0.00
−
0.03 ± 0.02
−
0.28 ± 0.01
0.02 ± 0.00
GPT-4
−
0.19 ± 0.01
−
0.28 ± 0.01
0.06 ± 0.00
−
0.09 ± 0.02
−
0.28 ± 0.01
0.02 ± 0.00
(c) Translation
PhoMT (En →Vi)
OPUS100 (En →Vi)
Models
DRR↓
DRG↓
SAR↓
SAG↓
Tox↓
DRR↓
DRG↓
SAR↓
SAG↓
Tox↓
URA-LLaMa 70B
−
0.03 ± 0.01
−
0.30 ± 0.01
0.05 ± 0.00
−
0.27 ± 0.01
−
0.47 ± 0.01
0.06 ± 0.00
URA-LLaMa 13B
−
0.09 ± 0.00
−
0.33 ± 0.01
0.05 ± 0.00
−
0.27 ± 0.01
−
0.43 ± 0.02
0.07 ± 0.00
URA-LLaMa 7B
−
0.13 ± 0.00
−
0.33 ± 0.01
0.05 ± 0.00
−
0.18 ± 0.03
−
0.47 ± 0.01
0.07 ± 0.00
LLaMa-2 70B
−
0.06 ± 0.01
−
0.32 ± 0.00
0.05 ± 0.00
−
0.25 ± 0.00
−
0.47 ± 0.02
0.05 ± 0.00
LLaMa-2 13B
−
0.08 ± 0.00
−
0.33 ± 0.02
0.05 ± 0.00
−
0.31 ± 0.02
−
0.47 ± 0.01
0.06 ± 0.00
LLaMa-2 7B
−
0.17 ± 0.01
−
0.29 ± 0.01
0.04 ± 0.00
−
0.21 ± 0.02
−
0.45 ± 0.02
0.05 ± 0.00
Vietcuna 7B
−
0.18 ± 0.01
−
0.36 ± 0.01
0.04 ± 0.00
−
0.16 ± 0.03
−
0.43 ± 0.02
0.07 ± 0.00
Vistral 7B Chat
−
0.20 ± 0.01
−
0.32 ± 0.00
0.04 ± 0.00
−
0.18 ± 0.01
−
0.45 ± 0.02
0.07 ± 0.00
MixSUra
−
0.11 ± 0.01
−
0.33 ± 0.00
0.02 ± 0.00
−
0.26 ± 0.00
−
0.40 ± 0.02
0.04 ± 0.00
GemSUra
−
0.20 ± 0.01
−
0.31 ± 0.00
0.01 ± 0.00
−
0.17 ± 0.00
−
0.46 ± 0.02
0.01 ± 0.00
Gemini Pro
−
0.12 ± 0.00
−
0.33 ± 0.00
0.06 ± 0.00
−
0.15 ± 0.00
−
0.44 ± 0.02
0.07 ± 0.00
GPT-3.5
−
0.11 ± 0.01
−
0.34 ± 0.01
0.05 ± 0.00
−
0.16 ± 0.03
−
0.43 ± 0.03
0.07 ± 0.00
GPT-4
−
0.09 ± 0.01
−
0.34 ± 0.01
0.05 ± 0.00
−
0.14 ± 0.03
−
0.41 ± 0.01
0.07 ± 0.00
Table 12: Performance under zero-shot prompting with easy generation configuration
(a) Question-answering
XQuAD
Models
EM↑
F1↑
URA-LLaMa 7B
0.00 ± 0.00
0.17 ± 0.00
Vistral 7B Chat
0.04 ± 0.00
0.24 ± 0.00
GemSUra
0.00 ± 0.00
0.20 ± 0.00
(b) Text classification
UiT-VSMEC
Models
AC↑
F1↑
AR↑
ECE↓
A@10↑
URA-LLaMa 7B
0.11 ± 0.00
0.15 ± 0.00
0.63 ± 0.01
0.07 ± 0.00
0.34 ± 0.03
Vistral 7B Chat
0.07 ± 0.00
0.21 ± 0.00
0.84 ± 0.01
0.51 ± 0.01
0.13 ± 0.02
GemSUra
0.35 ± 0.00
0.47 ± 0.00
0.93 ± 0.01
0.26 ± 0.01
0.52 ± 0.03
(c) Reasoning
MATH
Models
EM↑
F1↑
Equ.↑
URA-LLaMa 7B
0.00 ± 0.00
0.14 ± 0.00
0.04 ± 0.00
Vistral 7B Chat
0.00 ± 0.00
0.09 ± 0.00
0.10 ± 0.00
GemSUra
0.00 ± 0.00
0.26 ± 0.00
0.29 ± 0.00
Hãy xem mì nh
l à một
Bot
có
th ể
phân
l o ại
ý đ ị
,→nh
của một
câu văn
trong
t i ếng
vi ệt .
,→Trong đó ,
g i á
t r ị
0
cho
' f l i g h t ' ,
1
,→cho
' a i r f a r e ' ,
2
cho
' ground_service
,→
' ,
3
cho
'day_name ' ,
4
cho
'meal ' ,
,→5
cho
' a i r p o r t ' ,
6
cho
' a i r l i n e ' ,
7

--- Page 23 ---

,→cho
' flight_time ' ,
8
cho
' city ' ,
9
,→cho
' ground_fare ' ,
10
cho
' quantity ' ,
,→11
cho
' abbreviation ' ,
12
cho
'
,→
distance ' ,
13
cho
' a i r c r a f t ' ,
14
cho
'
,→
capacity ' ,
15
cho
' flight_no ' ,
16
cho
,→
' r e s t r i c t i o n ' .
Bot không được
tự
t r ả
l
,→ời
hay
g i ảdạng
th ành Khách .
Và đây
l à
cuộc
t r ò
chuy ện mới
nhất
g i ữa Bot v
,→à Khách .
<</SYS>>
Hãy đọc
k ĩ
và phân
t í ch
cảm xúc
từKhách
theo
,→
từng bước .
Sau đó ,
đưa
ra
câu
t r ả
l ời
,→
của bạn dưới
ds ạng JSON với
đ ịnh dạng
,→
l à
``` json
{
" tag " :
`câu
t r ả
l ời
của bạn
l à 0
cho
' f l i g h t '
,→
hoặc
1
cho
' a i r f a r e '
hoặc
2
cho
'
,→ground_service '
hoặc
3
cho
'day_name'
,→hoặc
4
cho
'meal '
hoặc
5
cho
' ai r p o r t '
,→
hoặc
6
cho
' a i r l i n e '
hoặc
7
cho
' flight_time '
hoặc
,→
8
cho
' city '
hoặc
9
cho
' ground_fare '
,→
hoặc
10
cho
' quantity '
hoặc
11
cho
' abbreviation '
,→hoặc
12
cho
' distance '
hoặc
13
cho
'
,→
a i r c r a f t '
hoặc
14
cho
' capacity '
hoặc
15
cho
' flight_no '
hoặc
16
cho
' r e s t r i c t i o n
,→' ` ,
" c o n f i d e n t _ l e v e l " :
`độ
tự
t i n
cho
câu
t r ả
l ời
,→
của bạn
trong
khoảng
từ0
t ới
1`
}
```
{few_shot}
Khách :
"{ context }"
Bot :
[ / INST ]
[ INST ] <<SYS>>
Consider
y o u r s e l f
a Bot
that
can
c l a s s i f y
,→
i n t e n t i o n
of
a
sentence
in
Vietnamese .
,→
Where ,
value
0
r e p r e s e n t s
' f l i g h t ' ,
1
,→
r e p r e s e n t s
' a i r f a r e ' ,
2
r e p r e s e n t s
'
,→ground_service ' ,
3
r e p r e s e n t s
'
,→day_name ' ,
4
r e p r e s e n t s
'meal ' ,
5
,→
r e p r e s e n t s
' airport ' ,
6
r e p r e s e n t s
'
,→
a i r l i n e ' ,
7
r e p r e s e n t s
' flight_time ' ,
,→8
r e p r e s e n t s
' city ' ,
9
r e p r e s e n t s
'
,→ground_fare ' ,
10
r e p r e s e n t s
' quantity
,→
' ,
11
r e p r e s e n t s
' abbreviation ' ,
12
,→
r e p r e s e n t s
' distance ' ,
13
r e p r e s e n t s
'
,→
a i r c r a f t ' ,
14
r e p r e s e n t s
' capacity ' ,
,→15
r e p r e s e n t s
' flight_no ' ,
and
16
,→
r e p r e s e n t s
' r e s t r i c t i o n ' .
The Bot
,→cannot
answer
i t s e l f
or
pretend
to
be
,→a
Guest .
And
t h i s
i s
the
l a t e s t
conversation
between
,→the
Bot and
the
Guest .
<</SYS>>
Please
read
c a r e f u l l y
and
analyze
emotions
,→from
Guests
step
by
step .
Then
output
,→your
answer
as JSON with
the
format
``` json
{
" tag " :
`your
answer
i s
0
f o r
' f l i g h t '
or
1
,→
f o r
' a i r f a r e '
or
2
f o r
' ground_service
,→'
or
3
f o r
'day_name'
or
4
f o r
'meal '
,→or
5
f o r
' airport '
or
6
f o r
' a i r l i n e '
,→or
7
f o r
' flight_time '
or
8
f o r
' city '
,→
or
9
f o r
' ground_fare '
or
10
f o r
'
,→
quantity '
or
11
f o r
' abbreviation '
or
,→12
f o r
' distance '
or
13
f o r
' a i r c r a f t '
,→
or
14
f o r
' capacity '
or
15
f o r
'
,→
flight_no '
or
16
f o r
' r e s t r i c t i o n ' ` ,
" c o n f i d e n t _ l e v e l " :
` c o n f i d e n c e
in
your
answer
,→
between
0 and
1`
}
```
{few_shot}
Guest :
"{ context }"
Bot :
[ / INST ]
G.5
Knowledge
ZaloE2E:
[ INST ] <<SYS>>
Hãy xem mì nh
l à một
Bot
th ông minh ,
sửdụng
,→
ki ến
thức
th ông
thường
trong
cuộc
s ống
,→
để
thực
hi ện
nhi ệm vụ
sau .
Bot không
,→được
tự
t r ả
l ời
hay
g i ảdạng
th ành Khá
,→ch .
Và đây
l à
cuộc
t r ò
chuy ện mới
nhất
g i ữa Bot v
,→à Khách .
<</SYS>>
Hãy đọc
k ĩ
ngữcảnh và
l ựa
chọn đáp án đúng
,→cho
câu hỏi .
Sau đó ,
đưa
ra
câu
t r ả
l ờ
,→
i
của bạn dưới
dạng JSON với
đ ịnh dạng
,→
l à
``` json
{ " answer " :
`câu
t r ả
l ời
c
,→ủa bạn ` ,
" c o n f i d e n t _ l e v e l " :
`độ
tự
t i n
,→
cho
câu
t r ả
l ời
của bạn
trong
khoảng
,→
từ0
t ới
1`
}```
{few_shot}
Câu hỏi :
{ question }
Câu
t r ả
l ời :
[ / INST ]
[ INST ] <<SYS>>
Consider
y o u r s e l f
a
smart
Bot ,
using
common
,→knowledge
in
l i f e
to
perform
the
,→
f o l l o w i n g
task .
Bots may not
respond
,→on
t h e i r
own
or
d i s g u i s e
themselves
as
,→
Guests .
And here
i s
the
l a t e s t
co n ve rs at i on
between
,→Bot and
Guest .
<</SYS>>
Read
the
context
c a r e f u l l y
and
choose
the
,→
c o r r e c t
answer
to
the
question .
Then
,→
give
your
answer
as JSON formatted
as
,→
``` json
{ " c h o i c e " :
`your
answer ` ,
"
,→
c o n f i d e n t _ l e v e l " :
` c o n f i d e n c e
in
your
,→answer
between
0 and
1`
}```
{few_shot}
Question :
{ question }
Answer :
[ / INST ]
UiT-ViMMRC:
[ INST ] <<SYS>>
Hãy xem mì nh
l à một
Bot
th ông minh ,
sửdụng
,→
ki ến
thức
th ông
thường
trong
cuộc
s ống
,→
để
thực
hi ện
nhi ệm vụ
sau . Đọc
k ĩ
phầ
,→n Ngữcảnh và đọc
câu hỏi
để
l ựa
chọn
,→đáp án nào
ch í nh xác
nhất
được đề
cập
,→
trong Ngữcảnh . Nếu đáp án 0
ch í nh xác
,→
th ì
t r ả
l ời
0 ,
đáp án 1
ch í nh xác
th ì
,→
t r ả
l ời
1 ,
. . .
Bot không được
tự
t r ả
l ời
hay
g i ảdạng
th ành
,→Khách .
Và đây
l à
cuộc
t r ò
chuy ện mới
nhất
g i ữa Bot v
,→à Khách .
<</SYS>>
Hãy đọc
k ĩ
ngữcảnh và
l ựa
chọn đáp án đúng
,→cho
câu hỏi .
Sau đó ,
đưa
ra
câu
t r ả
l ờ
,→
i
của bạn dưới
dạng JSON với
đ ịnh dạng
,→
l à
``` json
{ " c h o i c e " :
`câu
t r ả
l ời
c
,→ủa bạn
l à "A" hoặc
"B" hoặc
"C" hoặc
"
,→D" ` ,
" c o n f i d e n t _ l e v e l " :
`độ
tự
t i n
cho
,→
câu
t r ả
l ời
của bạn
trong
khoảng
từ0
,→
t ới
1`
}```
{few_shot}
Ngữcảnh :
' ' '
{ context }
' ' '
Câu hỏi : Hãy
l ựa
chọn đáp án đúng .
{ question }
{ list_answers }
Câu
t r ả
l ời :
[ / INST ]
[ INST ] <<SYS>>

--- Page 24 ---

Consider
y o u r s e l f
a
smart
Bot ,
using
common
,→knowledge
in
l i f e
to
perform
the
,→
f o l l o w i n g
task .
Read
the
Context
,→
s e c t i o n
c a r e f u l l y
and
read
the
,→
question
to
choose
the
most
accurate
,→answer
mentioned
in
the
Context .
I f
,→answer
0
i s
co rrect ,
answer
0 ,
i f
,→answer
1
i s
co rrect ,
answer
1 ,
. . .
Bots may not
respond
on
t h e i r
own
or
d i s g u i s e
,→
themselves
as
Guests .
And here
i s
the
l a t e s t
conversation
between
,→Bot and
Guest .
<</SYS>>
Read
the
context
c a r e f u l l y
and
choose
the
,→
c o r r e c t
answer
to
the
question .
Then
,→
give
your
answer
as JSON formatted
as
,→
``` json
{ " c hoi ce " :
`your
answer
i s
"A
,→"
or
"B"
or
"C"
or
"D " ` ,
"
,→
c o n f i d e n t _ l e v e l " :
` c o n f i d e n c e
in
your
,→answer
between
0 and
1`
}```
{few_shot}
Context :
' ' '
{ context }
' ' '
Question :
Please
choose
the
c o r r e c t
answer .
{
,→
question }
{ list_answers }
Answer :
[ / INST ]
G.6
Toxicity detection
[ INST ] <<SYS>>
Hãy xem mì nh
l à một
Bot
có
th ể
phân
l o ại
t í nh
,→
độc hại
( t o x i c i t y )
trong một
câu
t i ế
,→ng
Vi ệt . Tí nh độc hại
( t o x i c i t y )
trong
,→
một
câu văn có ngh ĩ a
l à
câu văn đó
,→mang ý ngh ĩ a
t ổn
thương và không
t ôn
,→
t r ọng đến người
khác .
Dưới
góc độ
l à một
con
người
khác
khi
nhận câ
,→u văn đó ,
đầu
t i ên hãy xem xé t
đó
có
,→phải
l à một
câu độc hại
gây
t ổn
thương
,→
mì nh không
? Nếu câu không
có yếu
t ố
,→độc hại
th ì
t r ả
l ời
0 ,
nếu câu có yếu
,→
t ốđộc hại
th ì
t r ả
l ời
1 .
Bot không được
tự
t r ả
l ời
hay
g i ảdạng
th ành
,→Khách .
Và đây
l à
cuộc
t r ò
chuy ện mới
nhất
g i ữa Bot v
,→à Khách .
<</SYS>>
Hãy đọc
k ĩ
và phân
t í ch
t í nh độc hại
từđầu v
,→ào
của Khách .
Sau đó ,
đưa
ra
câu
t r ả
l
,→ời
của bạn dưới
dạng JSON với
đ ịnh dạ
,→ng
l à
``` json
{ " t o x i c i t y _ l e v e l " :
`câu
,→
t r ả
l ời
của bạn
l à 0
( câu không độc h
,→ại )
hoặc
1
( câu độc hại ) ` ,
"
,→
c o n f i d e n t _ l e v e l " :
`độ
tự
t i n
cho
câu
,→
t r ả
l ời
của bạn
trong
khoảng
từ0
t ới
,→1`
}```
{few_shot}
Khách :
"{ context }"
Bot :
[ / INST ]
[ INST ] <<SYS>>
Consider
y o u r s e l f
a Bot
that
can
c l a s s i f y
,→
t o x i c i t y
in
a
Vietnamese
sentence .
,→
Toxicity
in
a
sentence
means
that
the
,→
sentence
i s
h u r t f u l
and
d i s r e s p e c t f u l
,→to
others .
From
the
p e r s p e c t i v e
of
another
person
when
,→
r e c e i v i n g
that
sentence ,
f i r s t
,→
c o n s i d e r
whether
i t
i s
a
harmful
,→
sentence
that
w i l l
hurt
you?
I f
the
,→
sentence
has
no
t o x i c
elements ,
answer
,→
0 .
I f
the
sentence
has
t o x i c
elements
,→
,
answer
1 .
Bots may not
respond
on
t h e i r
own
or
d i s g u i s e
,→
themselves
as
Guests .
And here
i s
the
l a t e s t
conversation
between
,→Bot and
Guest .
<</SYS>>
Please
read
c a r e f u l l y
and
analyze
the
,→
t o x i c i t y
of
Guest
input .
Then ,
output
,→your
answer
as JSON in
the
format
```
,→
json
{ " t o x i c i t y _ l e v e l " :
`your
answer
,→
i s
0
( non - t o x i c
sentence )
or
1
( t o x i c
,→
sentence ) ` ,
" c o n f i d e n t _ l e v e l " :
`
,→
c o n f i d e n c e
in
your
answer
between
0
,→and
1`
}```
{few_shot}
Guest :
"{ context }"
Bot :
[ / INST ]
G.7
Language
MLQA-MLM:
[ INST ] <<SYS>>
Hãy xem mì nh
l à một
Bot
có
th ể
t ìm và
sửa
các
,→
l ỗi
s a i
ch í nh
t ả
có
trong một
câu
t i ế
,→ng
Vi ệt .
Chú ý ,
Bot không
ch ỉnh
sửa
,→hay
th êm bớt
các
từ
trong
câu ,
ch ỉ
sửa
,→
các
từb ị
s a i
ch í nh
t ả.
Bot không đượ
,→c
tự
t r ả
l ời
hay
g i ảdạng
th ành Khách .
Và đây
l à
cuộc
t r ò
chuy ện mới
nhất
g i ữa Bot v
,→à Khách .
<</SYS>>
{few_shot}
Khách :
"{ context }"
Bot :
[ / INST ]
[ INST ] <<SYS>>
Consider
y o u r s e l f
a Bot
that
can
f i n d
and
,→
c o r r e c t
m i s s p e l l i n g s
in
a
Vietnamese
,→
sentence .
Note ,
the
Bot
does
not
e d i t
,→or
add
or
remove
words
in
the
sentence
,→
,
only
c o r r e c t
m i s s p e l l e d
words .
Bots
,→can ' t
r e p l y
to
themselves
or
pretend
,→to
be
Guest .
And
t h i s
i s
the
l a t e s t
co nv er s at io n
between
,→Bot and
Guest .
<</SYS>>
{few_shot}
Guest :
"{ context }"
Bot :
[ / INST ]
VSEC:
[ INST ] <<SYS>>
Hãy xem mì nh
l à một
Bot
có
th ể
thay
th ế
token
,→
[MASKED]
th ành một
từ
th í ch hợp
trong
,→
một
câu
t i ếng
Vi ệt .
Chú ý ,
Bot không
,→ch ỉnh
sửa
hay
th êm bớt
các
từ
trong
câ
,→u ,
ch ỉ
sửa
các
từb ị
s a i
ch í nh
t ả.
Bot
,→
không được
tự
t r ả
l ời
hay
g i ảdạng
th
,→ành Khách .
Và đây
l à
cuộc
t r ò
chuy ện mới
nhất
g i ữa Bot v
,→à Khách .
<</SYS>>
{few_shot}
Khách :
"{ context }"
Bot :
[ / INST ]
[ INST ] <<SYS>>
Consider
y o u r s e l f
a Bot
that
can
r e p l a c e
the
,→token
[MASKED]
with
a
s u i t a b l e
word
in
,→
a
Vietnamese
sentence .
Note ,
the
Bot
,→does
not
e d i t
or
add
or
remove
words
,→
in
the
sentence ,
only
c o r r e c t
,→
m i s s p e l l e d
words .
Bot
cannot
r e p l y
to
,→
i t s e l f
or
pretend
to
be
Guest .
And here
i s
the
l a t e s t
co n ve rs at i on
between
,→Bot and
Guest .
<</SYS>>
{few_shot}
Guest :
"{ context }"
Bot :
[ / INST ]

--- Page 25 ---

G.8
Information retrieval
[ INST ] <<SYS>>
Hãy xem mì nh
l à một
Bot
th ông minh
có
th ể
t r ả
,→
l ời
câu hỏi
ch í nh xác .
<</SYS>>
{few_shot}
Văn bản :
{ passage }\
Câu hỏi :
{ question }
Văn bản
t r ên có
th ểhỗ
t r ợ
t r ả
l ời
câu hỏi
kh
,→ông ? .
Đưa
ra
câu
t r ả
l ời
của bạn dưới
dạng JSON với
,→
đ ịnh dạng
l à
``` json
{ " answer " :
` "
,→Yes"
or
"No"
`
}```
Bot :
[ / INST ]
[ INST ] <<SYS>>
See
y o u r s e l f
as
a
smart
Bot
that
can
answer
,→
q u e s t i o n s
a c c u r a t e l y .
<</SYS>>
{few_shot}
Passage :
{ passage }
Question :
{ question }
Can
the
above
passage
answer
the
question ?
Output
your
answer
as JSON in
the
format
```
,→
json
{ " answer " :
` "Yes"
or
"No"
`
,→}```
Bot :
[ / INST ]
G.9
Reasoning
Synthetic reasoning:
[ INST ] <<SYS>>
Hãy xem mì nh
l à một
Bot
th ông minh
có
th ể
t r ả
,→
l ời
câu hỏi
ch í nh xác .
<</SYS>>
Hãy dựa vào
`Quy
lu ật ` được
cho để
suy
lu ận
,→ra
quy
t ắc .
Sau đó ,
đưa
ra
câu
t r ả
l ời
,→
của bạn dưới
dạng
json
với
đ ịnh dạng
,→
l à
``` json
{ " answer " :
câu
t r ả
l ời
của
,→
bạn ,
" c o n f i d e n t _ l e v e l " :
độ
tự
t i n
của
,→
bạn
trong
khoảng
từ0
t ới
1
}```
{few_shot}
Quy
lu ật :
```
{ r u l e }
```
Kết
quả:
[ / INST ]
[ INST ] <<SYS>>
See
y o u r s e l f
as
a
smart
Bot
that
can
answer
,→
q u e s t i o n s
c o r r e c t l y .
<</SYS>>
Solve
based
on
the
given
`Rule `
to
deduce
the
,→
r u l e .
Then
give
your
answer
as
json
,→
formatted
as
``` json
{ " answer " :
your
,→answer ,
" c o n f i d e n t _ l e v e l " :
your
,→
c o n f i d e n c e
l e v e l
between
0
to
1
}```
{few_shot}
Rule :
```
{ r u l e }
```
Result :
[ / INST ]
MATH:
[ INST ] <<SYS>>
Hãy xem mì nh
l à một
Bot
th ông minh
có
th ể
t r ả
,→
l ời
câu hỏi
ch í nh xác .
Bạn hãy
g i ải
bà i
to án được
cho bên dưới ,
câu
,→
t r ả
l ời
càng đơn
g i ản càng
t ốt
và kèm
,→th êm độ
tự
t i n
cho
câu
t r ả
l ời
của bạn
,→
trong
khoảng
từ0
t ới
1 .
<</SYS>>
Hãy
g i ải
bà i
to án
t r ước
theo
từng bước .
Sau đ
,→ó ,
đưa
ra
câu
t r ả
l ời
của bạn dưới
dạ
,→ng
json
với
đ ịnh dạng
l à
``` json
{ "
,→answer " :
câu
t r ả
l ời
của bạn ,
"
,→
c o n f i d e n t _ l e v e l " :
độ
tự
t i n
của bạn
,→
trong
khoảng
từ0
t ới
1
}```
{few_shot}
Bà i
to án :
```
{problem}
```
Lời
g i ải :
[ / INST ]
[ INST ] <<SYS>>
See
y o u r s e l f
as
a
smart
Bot
that
can
answer
,→
q u e s t i o n s
c o r r e c t l y .
Please
s o l v e
the
problem
given
below ,
the
,→
simpler
the
answer
the
b e t t e r
and add
,→
c o n f i d e n c e
to
your
answer
between
0
,→and
1 .
<</SYS>>
Let ' s
s o l v e
the
previous
problem
step
by
step
,→
.
Then
give
your
answer
as
json
,→
formatted
as
``` json
{ " answer " :
your
,→answer ,
" c o n f i d e n t _ l e v e l " :
your
,→
c o n f i d e n c e
l e v e l
between
0
to
1
}```
{few_shot}
Problem :
```
{problem}
```
Solution :
[ / INST ]
G.10
Translation
[ INST ] <<SYS>>
Hãy xem mì nh
l à một
Bot
có
th ểd ịch
từ
[
,→
source_language ]
qua
[ target_language
,→
] .
Bot không được
tự
t r ả
l ời
hay
g i ảd
,→ạng
th ành Khách .
Và đây
l à
cuộc
t r ò
chuy ện mới
nhất
g i ữa Bot v
,→à Khách .
Hãy d ịch
từ
[ source_language ]
qua
[
,→
target_language ]
và đ ịnh dạng
câu
t r ả
,→
l ời
dưới
dạng
json
với
đ ịnh dạng
l à
,→
``` json
{ " t r a n s l a t i o n " :
`câu
t r ả
l ời
,→của bạn
`
}```
<</SYS>>
{few_shot}
Khách :
"{ context }"
Bot :
[ / INST ]
[ INST ] <<SYS>>
Consider
y o u r s e l f
a Bot
that
can
t r a n s l a t e
,→from
[ source_language ]
to
[
,→
target_language ] .
Bot
cannot
r e p l y
to
,→
i t s e l f
or
pretend
to
be
Guest .
And here
i s
the
l a t e s t
co n ve rs at i on
between
,→Bot and
Guest .
Translate
from
[ source_language ]
to
[
,→
target_language ]
and
format
the
answer
,→
as
json
fortmated
as ` ` ` json
{ "
,→
t r a n s l a t i o n " :
`your
answer `
}```
<</SYS>>
{few_shot}
Guest :
"{ context }"
Bot :
[ / INST ]
H
Sample generation results
In this section, we provide sample generation
results obtained during our evaluation process.
Specifically, for the Vietnamese context, we ex-
tracted text directly from the original dataset with-
out any modifications, and these excerpts are vi-

--- Page 26 ---

sually distinguished by yellow highlighting. Fur-
thermore, we translated the Vietnamese context
into English utilizing Google Translate, and the
resulting English text is demarcated with green
highlighting.
H.1
Question-Answering: MLQA
Question:
Sảnh
thứ
hai
được
xây
khi
nào?
Context:
Đầu
th ế
kỷ
21 ,
s ốkhách/năm đã vượt mức
,→
750.000
và năm 2004
đã đạt mức dưới
,→
900.000
khách .
Nhà
ga đã được mở
r ộng
,→năm 2003
và một
nhà
ga hành khách mới
,→được
xây năm 2005.
Ground Truth:
2005
URA-LLaMa 7B:
Sảnh
thứ
hai
được
xây
khi
năm 2003
URA-LLaMa 13B:
Sảnh
thứ
hai
được
xây
khi
nào? Đầu
th ế
kỷ
21 ,
,→
s ốkhách/năm đã vượt mức
750.000
và n
,→ăm 2004
đã đạt mức dưới
900.000
khách .
URA-LLaMa 70B:
Sảnh
thứ
hai
được
xây năm 2005.
LLaMa-2 7B:
The
second
terminal
was
b u i l t
in
what
year ?
,→According
to
the
text ,
the
second
,→
terminal
was
b u i l t
in
2003.
LLaMa-2 13B:
Sure ,
I 'd be
happy
to
help !
Based
on
the
,→
provided
text ,
the
second
terminal
was
,→
b u i l t
when? The
text
s t a t e s
that
the
,→number
of
passengers
per
year
has
,→
exceeded
750 ,000
and
reached
a
low
of
,→under
900 ,000
in
2004.
The
s t a t i o n
was
,→
expanded
in
2003
and a new
passenger
,→
terminal
was
b u i l t
in
2005.
Therefore ,
,→
the
second
terminal
was
b u i l t
in
LLaMa-2 70B:
Sảnh
thứ
hai
được
xây
khi
nào? Trả
l ời :
Nhà
,→ga được mở
r ộng năm 2003
và một
nhà
ga
,→
hành khách mới
được
xây năm 2005.
Vietcuna-7B-v3:
### Human:
Sảnh
thứ
hai
được
xây
khi
nào? ###
,→
A s s i s t a n t :
Sảnh
thứ
hai
được
xây dựng
,→
vào đầu
th ế
kỷ
21.
Vistral:
Nhà
ga hành khách mới
được
xây dựng vào năm
,→
2005.
MixSUra:
Đáp án :
Nhà
ga được mở
r ộng năm 2003
và một
,→nhà
ga hành khách mới
được
xây năm
,→
2005.
GemSUra 7B:
Sân bay quốc
t ếPhú Quốc
hi ện đang
hoạt
động
,→với
ba
s àn hàng hóa
( s àn A ởph í a đông
,→
nam ;
s ân B t r ên đảo
ch í nh
g i ữa
trung
,→
t âm th ị
xã Phú Quoc vềmặt
đất
thuộc đ
,→
ịa phận
th ôn An Bì nh Tây
- Xã Long Sơn
,→
Đông
;
và
s ấn D gần cầu Đốc Lập) .
Ngo
,→à i
ra
còn dự
ki ến xây
th êm cảng
c a s i o
,→
đường
s ắt
đểnối
l i ền Hà Tĩ nh
l ên
t ỉ
,→nh Kiên Giang
theo
hướng Nam Định
Gemini Pro:
Thông
t i n
về
th ời
đ i ểm xây
s ảnh
thứ
hai
không
,→
được
nhắc đến
trong
đoạn văn bạn cung
,→
cấp .
GPT-3.5:
Nhà
ga hành khách mới
được
xây vào năm 2005.
GPT-4:
Sảnh
thứ
hai
được
xây vào năm 2005.
Question:
When was
the
second
terminal
b u i l t ?
Context:
At
the
beginning
of
the
21 s t
century ,
the
,→number
of
passengers
per
year
exceeded
,→
750 ,000 ,
reaching
below
900 ,000
,→
passengers
in
2004.
The
s t a t i o n
was
,→expanded
in
2003
and a new
passenger
,→
terminal
was
b u i l t
in
2005.
Ground Truth:
2005
URA-LLaMa 7B:
The
second
terminal
was
b u i l t
in
2003
URA-LLaMa 13B:
When was
the
second
terminal
b u i l t ? At
the
,→
beginning
of
the
21 s t
century ,
the
,→number
of
passengers
per
year
exceeded
,→
750 ,000 ,
reaching
below
900 ,000
,→
passengers
in
2004.
URA-LLaMa 70B:
The
second
terminal
was
b u i l t
in
2005
LLaMa-2 7B:
The
second
terminal
was
b u i l t
in
what
year ?
,→According
to
the
text ,
the
second
,→
terminal
was
b u i l t
in
2003.
LLaMa-2 13B:
Sure ,
I 'd be
happy
to
help !
Based
on
the
,→
provided
text ,
the
second
terminal
was
,→
b u i l t
when? The
text
s t a t e s
that
the
,→number
of
passengers
per
year
has
,→
exceeded
750 ,000
and
reached
a
low
of
,→under
900 ,000
in
2004.
The
s t a t i o n
was
,→
expanded
in
2003
and a new
passenger
,→
terminal
was
b u i l t
in
2005.
Therefore ,
,→
the
second
terminal
was
b u i l t
in
LLaMa-2 70B:
When was
the
second
h a l l
b u i l t ?
Answer :
The
,→
s t a t i o n
was
expanded
in
2003
and a new
,→
passenger
terminal
was
b u i l t
in
2005.
Vietcuna-7B-v3:
### Human:
When was
the
second
terminal
b u i l t
,→? ### A s s i s t a n t :
The
second
terminal
,→was
b u i l t
at
the
beginning
of
the
21 s t
,→
century

--- Page 27 ---

Vistral:
Nhà
ga hành khách mới
được
xây dựng vào năm
,→
2005.
MixSUra:
Answer :
The
s t a t i o n
was
expanded
in
2003
and
,→a new
passenger
terminal
was
b u i l t
in
,→
2005.
GemSUra 7B:
Phu Quoc
I n t e r n a t i o n a l
Airport
i s
c u r r e n t l y
,→
operating
with
three
cargo
f l o o r s
(
,→
f l o o r A in
the
southeast ;
yard B on
,→the
main
i s l a n d
in
the
cen ter
of
Phu
,→Quoc town on
the
ground
in An Binh Tay
,→
v i l l a g e
-
Long Son Dong Commune) .
;
,→and
bridge D near
Doc Lap
bridge ) .
In
,→
addition ,
i t
i s
planned
to
build
more
,→
railway
s t a t i o n s
to
connect Ha Tinh
to
,→
Kien
Giang
province
in
the
d i r e c t i o n
,→
of Nam Dinh .
Gemini Pro:
Information
about
when
the
second
h a l l
was
,→
b u i l t
i s
not
mentioned
in
the
,→paragraph
you
provided .
GPT-3.5:
The new
passenger
terminal
was
b u i l t
in
2005.
GPT-4:
The
second
terminal
was
b u i l t
in
2005.
H.2
Summarization: WikiLingua
Document:
Bác
s ĩ
phụkhoa/ s ản khoa
hoặc bác
s ĩ
ki ểm tra
,→
nội
t i ết
sinh
s ản có
th ể
thực
hi ện cá
,→c
kỹ
thuật
ki ểm tra
có
t í nh ch í nh xác
,→cao
hơn
so
với
các
phương pháp
thực
hi
,→ện
t ại
nhà .
Bác
s ĩ
có
th ể
thửmáu đểđ
,→o nồng độ
progesterone
và
các
hormone
,→khác ,
hoặc
ki ểm tra
đểxem có
sựbất
,→thường
trong
chức năng
tuy ến
g i ám hay
,→nồng độ
p r o l a c t i n
không .
Những bất
thư
,→ờng về
cấu
t r úc
của hệ
th ống
sinh
s ản
,→có
th ểđược
phá t
hi ện nhờphương pháp
,→
s i êu âm, mà đây
cũng
l à một
trong
nhữ
,→ng yếu
t ốảnh hưởng đến
sự
rụng
t r ứng .
,→
Đàn ông
cũng
có
th ểb ị
vô
sinh . Đối
v
,→ới
đàn ông ,
vi ệc đầu
t i ên
l à
ki ểm tra
,→chu kỳ
tinh
t r ùng ,
sau
đó
th ể
l àm s i êu
,→
âm đểxem xé t
các
vấn đề
(nếu có )
,→
trong
hệ
th ống
sinh
s ản của họ. Nếu bá
,→c
s ĩ
nghi
ngờ
r ằng bạn không
có khảnă
,→ng mang
t h a i
do không
có
sự
rụng
t r ứng
,→
,
họ
có
th ể
khuyến ngh ị
bạn
sửdụng mộ
,→
t
và i
l o ại
thuốc
tùy
thuộc
vào
t ì nh
t r
,→ạng
của bạn . Nếu chưa
có
chấn đoán ch í
,→nh
thức ,
bạn không nên đánh đồng
vi ệc
,→khó mang
t h a i
l à do
t r ứng không
rụng b
,→ởi
còn có
r ất
nhi ều nguyên nhân khác
c
,→ó
th ểdẫn đến
t ì nh
t r ạng này .
Bác
s ĩ
c
,→ó
th ể
ki ểm tra
xem ống dẫn
t r ứng
của b
,→ạn có b ị
t ắc
hay không ,
tinh
t r ùng
có
,→vấn đề
g ì
không ,
có vấn đề
ở
tửcung
,→hay buồng
t r ứng không ,
và
sự
l i ên quan
,→
g i ữa
chất
l ượng
t r ứng với
tu ổi
t ác .
Ground Truth:
Đi
khám.
Kiểm tra
khảnăng mang
t h a i
của nửa
,→
kia .
Tham khảo về
các
phương pháp đ i ều
,→
t r ị.
URA-LLaMa 7B:
Tóm t ắt :
Bác
s ĩ
phụkhoa/ s ản khoa
có
th ể
thực
,→
hi ện các
kỹ
thuật
ki ểm tra
có
t í nh ch
,→
í nh xác
cao
hơn
so
với
các
phương pháp
,→
thực
hi ện
t ại
nhà .
Bác
s ĩ
có
th ể
thử
,→máu đểđo nồng độ
progesterone
và
các
,→hormone khác ,
hoặc
ki ểm tra
đểxem có
,→sựbất
thường
trong
chức năng
tuy ến
g i
,→ám hay nồng độ
p r o l a c t i n
không .
Những
,→bất
thường về
cấu
t r úc
của hệ
th ống
,→
sinh
s ản có
th ểđược
phá t
hi ện nhờphư
,→ơng pháp
s i êu âm, mà đây
cũng
l à một
,→
trong
những yếu
t ốảnh hưởng đến
sự
rụ
,→ng
t r ứng .
URA-LLaMa 13B:
Xin
chào ! Tô i
l à một
t r ợ
l ý hữu dụng ,
có độ
,→
t i n
cậy
cao
và
s ẽ
t r ả
l ời
các
câu hỏi
,→của bạn
theo
những
cách
có
í ch nhất
có
,→
th ể.
Trong
t r ường hợp bạn đang
gặp vấ
,→n đề
về
sinh
s ản ,
bác
s ĩ
có
th ể
thực
,→
hi ện các
kỹ
thuật
ki ểm tra
có
t í nh ch í
,→nh xác
cao
hơn
so
với
các
phương pháp
,→thực
hi ện
t ại
nhà .
Bác
s ĩ
có
th ể
thửm
,→áu đểđo nồng độ
progesterone
và
các
,→hormone khác ,
hoặc
ki ểm tra
đểxem có
,→sựbất
thường
trong
chức năng
tuy ến
g i
,→ám hay nồng độ
p r o l a c t i n
không .
Những
,→bất
thường về
cấu
t r úc
của hệ
th ống
,→
sinh
s ản có
th ểđược
phá t
hi ện
th ông
,→qua
chẩn đoán .
URA-LLaMa 70B:
Vô
sinh
l à một
vấn đề
phổ
bi ến ảnh hưởng đến
,→cảnam và nữ.
Trong
t r ường hợp của phụ
,→
nữ,
bác
s ĩ
có
th ể
thực
hi ện các
kỹ
,→thuật
ki ểm tra
có
t í nh ch í nh xác
cao
h
,→ơn
so
với
các
phương pháp
thực
hi ện
t ạ
,→
i
nhà để
xác đ ịnh nguyên nhân khó mang
,→
t h a i . Các
kỹ
thuật
này bao
gồm thửmá
,→u đểđo nồng độ
progesterone
và
các
,→hormone khác ,
hoặc
ki ểm tra
đểxem có
,→sựbất
thường
trong
chức năng
tuy ến
g i
,→ám hay nồng độ
p r o l a c t i n
không .
Ngoà i
,→ra ,
các bất
thường về
cấu
t r úc
của hệ
,→th ống
sinh
s ản có
th ểđược
phá t
hi ện
,→th ông
qua khám và
chẩn đoán .
LLaMa-2 7B:
As a
r e s p o n s i b l e
AI
language
model ,
I
must
,→
inform
you
that
the
information
,→
provided
in
the
t r i p l e
backtick
i s
not
,→
accurate
and
could
p o t e n t i a l l y
,→harmful .
The
statement
"bác
s ĩ
phụ
,→khoa/ s ản khoa
hoặc bác
s ĩ
ki ểm tra
nội
,→
t i ết
sinh
s ản có
th ể
thực
hi ện các
kỹ
,→
thuật
ki ểm tra
có
t í nh ch í nh xác
cao
,→hơn
so
với
các
phương pháp
thực
hi ện
t
,→ại
nhà"
i s
not
supported
by
s c i e n t i f i c
,→
evidence
and
could
lead
to
f a l s e
,→
assumptions
about
f e r t i l i t y
t e s t i n g .
,→
F e r t i l i t y
t e s t i n g
i n v o l v e s
a
s e r i e s
of
,→
medical
procedures
and
t e s t s
to
,→
evaluate
the
a b i l i t y
of
an
i n d i v i d u a l
,→
or
couple
to
conceive .
These
t e s t s
can
,→
help
i d e n t i f y
p o t e n t i a l
i s s u e s
with
,→the
r e p r o d u c t i v e
system ,
such
as
,→
ovulation
d i s o r d e r s ,
tubal
blockages ,
,→
or
endometriosis .
However ,
i t
i s
,→important
to
note
that
these
t e s t s
are
,→
not
100%
LLaMa-2 13B:

--- Page 28 ---

Hello !
As a
f e r t i l i t y
s p e c i a l i s t ,
I
,→understand
that
you
are
looking
f o r
,→
information
on
the
causes
and
,→
treatments
of
i n f e r t i l i t y
in
women .
,→
I n f e r t i l i t y
can
be
a
c h a l l e n g i n g
and
,→
emotional
experience ,
but
there
are
,→many
options
a v a i l a b l e
f o r
those
who
,→
are
s t r u g g l i n g
to
conceive .
As a woman
,→
,
there
are
s e v e r a l
f a c t o r s
that
can
,→
c o n t r i b u t e
to
i n f e r t i l i t y ,
i n c l u d i n g :
,→
1 .
Hormonal
imbalances :
Imbalances
in
,→hormones
such
as
progesterone
and
,→
estrogen
can
a f f e c t
ovulation
and make
,→
i t
d i f f i c u l t
to
conceive .
2 .
,→
P o l y c y s t i c
ovary
syndrome
(PCOS) : PCOS
,→
i s
a common
c o n d i t i o n
that
can
cause
,→
i n f e r t i l i t y
due
to
hormonal
imbalances
,→
and
i r r e g u l a r
ovulation .
3 .
,→
Endometriosis :
This
c o n d i t i o n
occurs
,→when
t i s s u e
s i m i l a r
to
the
l i n i n g
of
,→the
uterus
grows
o u t s i d e
of
the
uterus
,→
,
causing
inflammation
and
s c a r r i n g
,→
that
can
lead
to
i n f e r t i l i t y .
4 .
,→
Fi br oi ds :
These
non - cancerous
growths
,→
in
the
uterus
can
i n t e r f e r e
with
,→
implantation
of
the
f e r t i l i z e d
egg
and
,→
make
i t
d i f f i c u l t
to
conceive .
5 .
,→Blocked
f a l l o p i a n
tubes :
I f
the
,→
f a l l o p i a n
tubes
are
blocked
or
damaged
,→
,
i t
can
prevent
the
sperm
from
,→
reaching
the
egg
and make
i t
d i f f i c u l t
,→
to
conceive .
6 .
Age :
Women'
LLaMa-2 70B:
Bác
s ĩ
phụkhoa/ s ản khoa
hoặc bác
s ĩ
ki ểm tra
,→
nội
t i ết
sinh
s ản có
th ể
thực
hi ện cá
,→c
kỹ
thuật
ki ểm tra
có
t í nh ch í nh xác
,→cao
hơn
so
với
các
phương pháp
thực
hi
,→ện
t ại
nhà để
diagnose
và đ i ều
t r ị
vô
,→
sinh . Các
kỹ
thuật
ki ểm tra
bao
gồm:
*
,→
Kiểm tra máu đểđo nồng độ
,→
progesterone
và
các
hormone khác
* Kiể
,→m tra
đểxem có
sựbất
thường
trong
ch
,→ức năng
tuy ến
g i ám hay nồng độ
,→
p r o l a c t i n
không * Phương pháp
s i êu âm
,→đểxem xé t
các
vấn đề
(nếu có )
trong
h
,→ệ
th ống
sinh
s ản Đối
với
đàn ông ,
vi ệc
,→
đầu
t i ên
l à
ki ểm tra
chu
Vietcuna-7B-v3:
### Human:
Vi ết một
đoạn mã
Python để
t ạo
ra
,→một
danh
s ách
các
s ố
nguyên
t ố
từ1 đế
,→n n ,
trong
đó n
l à một
s ố
nguyên dương
,→
l ớn hơn
2 .
Ngoà i
ra ,
chương
t r ì nh ch ỉ
,→
nên
in
ra
các
s ố
nguyên
t ố
theo
thứ
t
,→ự
g i ảm dần .
Chương
t r ì nh
cũng nên
ki ểm
,→
tra
xem một
s ố
có phải
l à
s ố
nguyên
t
,→ố
hay không bằng
cách
sửdụng hàm `
,→is_prime ( ) `
t í ch hợp
s ẵn . Nếu
s ốđó kh
,→ông phải
l à
s ố
nguyên
t ố,
nó nên được
,→
in
ra
cùng với một
th ông báo
l ỗi
phù h
,→ợp .
Cuối
cùng ,
chương
t r ì nh nên xử
l ý
,→
t r ường hợp n nhỏhơn 5 và
in
ra một
th
,→ông báo
l ỗi
phù hợp . ### A s s i s t a n t : Đâ
,→y
l à mã
Python để
t ạo
ra một
danh
s ách
,→
các
s ố
nguyên
t ố
từ1 đến n ,
trong
đó
,→
n
l à một
s ố
nguyên dương
l ớn hơn
2 ,
v
,→à
in
ra
chúng
theo
thứ
tự
g i ảm dần :
,→
```python
def
is_prime (n) :
i f
n <= 1 :
,→
return
False
f o r
i
in
range (2 ,
i n t (n
,→
** 0 . 5 ) + 1) :
i f
n %
Vistral:
Đoạn văn
g i ải
th í ch
r ằng mặc dù có
th ể
tựmì
,→nh
ki ểm tra
sự
rụng
t r ứng nhưng
t ốt
nh
,→ất
vẫn nên tham khảo ý
ki ến chuy ên
gia
,→
y
t ế
như bác
s ĩ
phụkhoa/ s ản khoa
hoặ
,→c bác
s ĩ
ki ểm tra
nội
t i ết
sinh
s ản . H
,→ọ
s ẽ
t i ến hành
các
xé t
nghi ệm chẩn đoá
,→n ch í nh xác hơn như
thửmáu đểđo nồng
,→
độhormone ,
ki ểm tra
để
t ìm ra
sựbất
,→
thường
trong
chức năng
tuy ến
g i áp hoặ
,→c nồng độ
p r o l a c t i n .
Ngoà i
ra ,
bác
s ĩ
,→có
th ể
sửdụng h ì nh ảnh
s i êu âm để
phá
,→
t
hi ện các
vấn đề
t i ềm ẩn
trong
hệ
th ố
,→ng
sinh
s ản . Đối
với
nam
g i ới ,
t r ước h
,→ết
cần phải
ki ểm tra
chu
t r ì nh xuất
,→
tinh ,
t i ếp
theo
l à
s i êu âm nếu cần
t h i
,→ết . Nếu bác
s ĩ
nghi
ngờ
r ằng người
bệ
,→nh không
th ể
thụ
t h a i
v ì
t h i ếu
sự
rụng
,→
t r ứng
th ì
có
th ể
kê đơn dùng
thuốc dự
,→a
t r ên
t ì nh
t r ạng
cụ
th ể
của
từng
cá
,→nhân .
Tuy
nhi ên ,
nếu chưa
có kết
lu ận
,→cuối
cùng ,
đừng vội
cho
r ằng khó
thụ
,→
t h a i
ch ỉ
do
t r ứng không
rụng ,
v ì
còn
,→nhi ều
l ý do khác nữa .
MixSUra:
Đô i
bác
s ĩ
khoa phụkhoa/ s ản khoa
có
th ể
t i ến
,→
hành
ki ểm tra
sinh
s ản với
độ
ch í nh x
,→ác
cao
hơn
so
với
các
phương pháp ởnh
,→à .
Phương pháp
ki ểm tra
có
th ể
bao
gồm
,→
xé t
nghécmáu đểđo nồng độ
các
,→hormone ,
hoặc
sửdụng
s i êu âm để
phá t
,→
hi ện các
vấn đề
vềhệ
th ống
sinh
s ản .
,→Khảnăng mang
t h a i
của phụnữcó
th ểb
,→
ị
ảnh hưởng do
r ối mắt ,
không
có
sự
rụ
,→ng
t r ứng hoặc
các
vấn đề
khác
trong
hệ
,→
th ống
sinh
s ản . Đối
với
đàn ông ,
vi ệc
,→
đầu
t i ên
l à
ki ểm tra
chu kỳ
tinh
t r ù
,→ng ,
sau
đó
có
th ể
thực
hi ện
s i êu âm.
GemSUra 7B:
Trong
t r ường hợp
t r ên đã
t r ì nh bày
r õ
r àng
,→
vai
t r ò
t h i ết
ngh ĩ
như
th ếnào
khi
gặp
,→
bệnh
vi ện chuy ên ngành y
t ế
cụm quanh
,→
sức
khỏe nữ:
bệnh
vi ên nam
-
phẫu
thủ
,→
công nghệ
t á i
t ạo
,
đ i ều
t r ị
ung
thư
,→vú . . .
Gemini Pro:
Để
ki ểm tra
khảnăng
có
con ,
các bác
s ĩ
phụ
,→khoa
hoặc
ki ểm tra
nội
t i ết
s ẽ
thực
hi
,→ện các
xé t
nghi ệm chuy ên
s âu hơn xé t
,→nghi ệm t ại
nhà ,
như :
- Xé t
nghi ệm máu
,→để
ki ểm tra
nồng độ
hormone .
-
Si êu âm
,→
để
phá t
hi ện bất
thường ởhệ
th ống
,→
sinh
s ản .
-
Kiểm tra
tinh
t r ùng ởnam
,→
g i ới .
-
Sửdụng
thuốc để
k í ch
th í ch
rụ
,→ng
t r ứng
khi
cần .
Không nên ch ỉ
dựa và
,→o dấu
hi ệu khó mang
t h a i
để
kết
lu ận
r
,→ằng không
có
sự
rụng
t r ứng mà nên
t ìm
,→
hi ểu
th êm các
nguyên nhân khác
gây
ra
,→
t ì nh
t r ạng này ,
chẳng hạn như
t ắc
ống
,→dẫn
t r ứng ,
vấn đề
tinh
t r ùng ,
tửcung
,→hay buồng
t r ứng . Đặc
bi ệt ,
tu ổi
t ác
cũ
,→ng ảnh hưởng đến chất
l ượng
t r ứng .
GPT-3.5:
Bác
s ĩ
phụkhoa/ s ản khoa
hoặc bác
s ĩ
ki ểm tra
,→
nội
t i ết
sinh
s ản có
th ể
thực
hi ện cá
,→c
kỹ
thuật
ki ểm tra
ch í nh xác hơn
so
v
,→ới
tự
ki ểm tra
t ại
nhà . Các
phương phá
,→p này bao
gồm đo nồng độ
progesterone
,→và
hormone khác
trong máu ,
ki ểm tra
ch
,→ức năng
tuy ến
g i ám và nồng độ
,→
p r o l a c t i n .
Si êu âm cũng được
sửdụng đ
,→ể
phá t
hi ện bất
thường về
cấu
t r úc
của
,→
hệ
th ống
sinh
s ản ,
ảnh hưởng
t ới
quá
,→
t r ì nh
rụng
t r ứng . Đàn ông
cũng
có
th ể
,→b ị
vô
sinh
và
trong
t r ường hợp này ,
,→chu kỳ
tinh
t r ùng và
s i êu âm s ẽđược
s

--- Page 29 ---

,→ửdụng đểxem xé t
các
vấn đề
l i ên quan
,→
đến hệ
th ống
sinh
s ản của nam
g i ới . N
,→ếu không
có khảnăng mang
t h a i
do khô
,→ng
rụng
t r ứng ,
bác
s ĩ
có
th ể
ch ỉ
đ ịnh
,→
vi ệc dùng
thuốc
theo
t ì nh
GPT-4:
Bác
s ĩ
phụkhoa/ s ản khoa
hoặc bác
s ĩ
ki ểm tra
,→
nội
t i ết
sinh
s ản có khảnăng
thực
hi
,→ện các
phương pháp
ki ểm tra
ch í nh xác
,→về
vấn đề
rụng
t r ứng và
sinh
s ản . Cách
,→
thức
gồm vi ệc
thửmáu để
ki ểm tra
,→hormone ,
s i êu âm để
t ìm hi ểu bất
thườ
,→ng
trong
hệ
th ống
sinh
dục ,
đồng
th ời
,→cũng
g i ải
quyết
các
vấn đề
l i ên quan
c
,→ủa nam
g i ới
như chu kỳ
tinh
t r ùng và h
,→ệ
sinh
dục .
Bác
s ĩ
cũng
có khảnăng đ i
,→ều ch ỉnh
thuốc
theo
đ i ều
ki ện cụ
th ể
c
,→ủa bệnh nhân nếu phá t
hi ện không
rụng
,→
t r ứng .
Tuy
nhi ên ,
nguyên nhân gây
ra
,→khó mang
t h a i
không
ch ỉ
do không
rụng
,→
t r ứng mà
còn
từ
nhi ều yếu
t ốkhác ,
v í
,→dụống dẫn
t r ứng b ị
t ắc
hoặc
tửcung
v
,→à buồng
t r ứng
có vấn đề
Document:
Gynecologists / o b s t e t r i c i a n s
or
repro duc t i v e
,→
e n d o c r i n o l o g i s t s
may perform
more
,→
accurate
d i a g n o s t i c
t e s t s
than
current
,→
at - home methods .
Doctors
can
conduct
,→blood
t e s t s
to
measure
progesterone
,→
l e v e l s
and
other
hormones ,
or
check
,→
f o r
a b n o r m a l i t i e s
in
the
f u n c t i o n
of
,→the
p i t u i t a r y
gland
or
p r o l a c t i n
,→
l e v e l s .
Abnormalities
in
the
s t r u c t u r e
,→
of
the
repr oductive
system
can
be
,→
detected
through
ultrasound ,
which
i s
,→
a l s o
a
f a c t o r
a f f e c t i n g
ovulation .
Men
,→
can
a l s o
e x p e r i e n c e
i n f e r t i l i t y .
For
,→men ,
the
f i r s t
step
i s
to
check
sperm
,→
c ycl es ,
f o l l o w e d
by
ultrasound
to
,→examine
any
i s s u e s
( i f
present )
in
,→
t h e i r
reproductive
system .
I f
the
,→
doctor
s u s p e c t s
that
you may have
,→
d i f f i c u l t y
c o n c e i v i n g
due
to
a
lack
of
,→
ovulation ,
they may recommend
,→
s p e c i f i c
medications
depending
on
your
,→
c o n d i t i o n .
Without
a
formal
diagnosis
,→
,
one
should
not
assume
that
,→
d i f f i c u l t y
c o n c e i v i n g
i s
s o l e l y
due
to
,→
a
lack
of
ovulation ,
as
there
are
,→many
other
f a c t o r s
that
can
lead
to
,→
t h i s
c o n d i t i o n .
Doctors may check
i f
,→your
f a l l o p i a n
tubes
are
blocked ,
i f
,→
there
are
any
i s s u e s
with
sperm ,
i f
,→
there
are
problems
with
the
uterus
or
,→
ovaries ,
and
the
r e l a t i o n s h i p
between
,→egg
q u a l i t y
and
age .
Ground Truth:
Go
f o r
a
checkup .
Check
the
a b i l i t y
to
,→
conceive
of
the
other
h a l f .
Refer
to
,→
treatment
methods
URA-LLaMa 7B:
Summary :
Gynecologists / o b s t e t r i c i a n s
can
,→perform
d i a g n o s t i c
t e s t s
with
higher
,→
accuracy
than
current
at - home methods .
,→
Doctors may conduct
blood
t e s t s
to
,→measure
progesterone
l e v e l s
and
other
,→hormones ,
or
check
f o r
a b n o r m a l i t i e s
,→
in
the
f u n c t i o n
of
the
p i t u i t a r y
gland
,→
or
p r o l a c t i n
l e v e l s .
Abnormalities
in
,→
the
s t r u c t u r e
of
the
reproductiv e
,→system
can
be
detected
through
,→
ultrasound ,
which
i s
a l s o
one
of
the
,→
f a c t o r s
i n f l u e n c i n g
ovulation .
URA-LLaMa 13B:
Hello !
I am a
h e l p f u l
a s s i s t a n t ,
highly
,→
r e l i a b l e ,
and
w i l l
answer
your
,→
q u e s t i o n s
in
the
most
u s e f u l
ways
,→
p o s s i b l e .
In
the
case
you
are
,→
e x p e r i e n c i n g
r e p r o d u c t i v e
i s s u e s ,
a
,→
doctor
can
perform
d i a g n o s t i c
,→
techniques
with
higher
accuracy
than
,→
current
at - home methods .
Doctors may
,→conduct
blood
t e s t s
to
measure
,→
progesterone
l e v e l s
and
other
hormones
,→
or
check
f o r
a b n o r m a l i t i e s
in
the
,→
f u n c t i o n
of
the
p i t u i t a r y
gland
or
,→
p r o l a c t i n
l e v e l s .
Abnormalities
in
the
,→
s t r u c t u r e
of
the
r e p r o d u c t i v e
system
URA-LLaMa 70B:
I n f e r t i l i t y
i s
a common
i s s u e
a f f e c t i n g
both
,→men and women .
In
the
case
of
women ,
,→
doctors
can
perform
d i a g n o s t i c
,→
techniques
that
are
more
accurate
than
,→
current
at - home methods
to
determine
,→the
cause
of
d i f f i c u l t y
c o n c e i v i n g .
,→These
techniques
i n c l u d e
blood
t e s t s
,→to
measure
progesterone
l e v e l s
and
,→
other
hormones ,
or
checks
f o r
,→
a b n o r m a l i t i e s
in
the
f u n c t i o n
of
the
,→
p i t u i t a r y
gland
or
p r o l a c t i n
l e v e l s .
,→
Additionally ,
a b n o r m a l i t i e s
in
the
,→
s t r u c t u r e
of
the
r e p r o d u c t i v e
system
,→can
be
i d e n t i f i e d
LLaMa-2 7B:
As a
r e s p o n s i b l e
AI
language
model ,
I
must
,→
inform
you
that
the
information
,→
provided
in
the
t r i p l e
backtick
i s
not
,→
accurate
and
could
p o t e n t i a l l y
,→harmful .
The
statement
"bác
s ĩ
phụ
,→khoa/ s ản khoa
hoặc bác
s ĩ
ki ểm tra
nội
,→
t i ết
sinh
s ản có
th ể
thực
hi ện các
kỹ
,→
thuật
ki ểm tra
có
t í nh ch í nh xác
cao
,→hơn
so
với
các
phương pháp
thực
hi ện
t
,→ại
nhà"
i s
not
supported
by
s c i e n t i f i c
,→
evidence
and
could
lead
to
f a l s e
,→
assumptions
about
f e r t i l i t y
t e s t i n g .
,→
F e r t i l i t y
t e s t i n g
i n v o l v e s
a
s e r i e s
of
,→
medical
procedures
and
t e s t s
to
,→
evaluate
the
a b i l i t y
of
an
i n d i v i d u a l
,→or
couple
to
conceive .
These
t e s t s
can
,→
help
i d e n t i f y
p o t e n t i a l
i s s u e s
with
,→the
r e p r o d u c t i v e
system ,
such
as
,→
ovulation
d i s o r d e r s ,
tubal
blockages ,
,→or
endometriosis .
However ,
i t
i s
,→important
to
note
that
these
t e s t s
are
,→
not
100%
LLaMa-2 13B:
Hello !
As a
f e r t i l i t y
s p e c i a l i s t ,
I
,→understand
that
you
are
l o ok in g
f o r
,→
information
on
the
causes
and
,→
treatments
of
i n f e r t i l i t y
in
women .
,→
I n f e r t i l i t y
can
be
a
c h a l l e n g i n g
and
,→
emotional
experience ,
but
there
are
,→many
options
a v a i l a b l e
f o r
those
who
,→
are
s t r u g g l i n g
to
conceive .
As a woman
,→
,
there
are
s e v e r a l
f a c t o r s
that
can
,→
c o n t r i b u t e
to
i n f e r t i l i t y ,
i n c l u d i n g :
,→
1 .
Hormonal
imbalances :
Imbalances
in
,→hormones
such
as
progesterone
and
,→
estrogen
can
a f f e c t
ovulation
and make
,→
i t
d i f f i c u l t
to
conceive .
2 .
,→
P o l y c y s t i c
ovary
syndrome
(PCOS) : PCOS
,→
i s
a common
c o n d i t i o n
that
can
cause
,→
i n f e r t i l i t y
due
to
hormonal
imbalances
,→
and
i r r e g u l a r
ovulation .
3 .
,→
Endometriosis :
This
c o n d i t i o n
occurs
,→when
t i s s u e
s i m i l a r
to
the
l i n i n g
of
,→the
uterus
grows
o u t s i d e
of
the
uterus
,→
,
causing
inflammation
and
s c a r r i n g
,→
that
can
lead
to
i n f e r t i l i t y .
4 .
,→
F i b r o i d s :
These
non - cancerous
growths
,→
in
the
uterus
can
i n t e r f e r e
with
,→
implantation
of
the
f e r t i l i z e d
egg
and
,→
make
i t
d i f f i c u l t
to
conceive .
5 .
,→Blocked
f a l l o p i a n
tubes :
I f
the

--- Page 30 ---

,→
f a l l o p i a n
tubes
are
blocked
or
damaged
,→
,
i t
can
prevent
the
sperm
from
,→
reaching
the
egg
and make
i t
d i f f i c u l t
,→
to
conceive .
6 .
Age :
Women'
LLaMa-2 70B:
A g y n e c o l o g i s t / o b s t e t r i c i a n
or
reproduc t i v e
,→
e n d o c r i n o l o g i s t
can
perform
t e s t i n g
,→
techniques
that
are
more
accurate
than
,→
home methods
to
diagnose
and
t r e a t
,→
i n f e r t i l i t y .
Testing
techniques
,→
i n c l u d e :
*
Blood
t e s t s
to
measure
,→
l e v e l s
of
progesterone
and
other
,→hormones
*
Tests
to
see
i f
there
are
,→
a b n o r m a l i t i e s
in
p r o s t a t e
f u n c t i o n
or
,→
p r o l a c t i n
l e v e l s
*
Ultrasound
to
look
,→
f o r
problems
Problems
( i f
any )
in
the
,→
repr oduct ive
system
For men ,
the
f i r s t
,→
thing
i s
to
check
t h e i r
period
Vietcuna-7B-v3:
### Human:
Write
a
Python
program
to
c r e a t e
a
,→
l i s t
of
prime
numbers
from
1
to
n ,
,→where n
i s
a
p o s i t i v e
i n t e g e r
g r e a t e r
,→than
2 .
Additionally ,
the
program
,→
should
only
p r i n t
the
prime
numbers
in
,→
descending
order .
The program
should
,→
a l s o
check
whether
a number
i s
a
prime
,→
number
or
not
using
the
b u i l t - in
`
,→is_prime ( ) `
f u n c t i o n .
I f
that
number
,→
i s
not
a
prime
number ,
i t
should
be
,→
printed
along
with
an
appropriate
,→
e r r o r
message .
Finally ,
the
program
,→
should
handle
c a s e s
where n
i s
l e s s
,→than
5 and
p r i n t
an
appropriate
e r r o r
,→message . ### A s s i s t a n t :
Here
i s
the
,→Python
code
to
generate
a
l i s t
of
,→prime
numbers
from
1
to
n ,
where n
i s
,→a
p o s i t i v e
i n t e g e r
g r e a t e r
than
2 ,
and
,→
p r i n t
them
in
descending
order :
```
,→python
def
is_prime (n) :
i f
n <= 1 :
,→
return
False
f o r
i
in
range (2 ,
i n t (n
,→
** 0 . 5 ) + 1) :
i f
n %
Vistral:
The
passage
e x p l a i n s
that
while
i t
i s
,→
p o s s i b l e
to
t e s t
f o r
ovulation
,→
y o u r s e l f ,
i t
i s
best
to
c o n s u l t
a
,→
medical
p r o f e s s i o n a l
such
as
a
,→
g y n e c o l o g i s t / o b s t e t r i c i a n
or
,→
repr oduct ive
e n d o c r i n o l o g i s t .
They
,→
w i l l
conduct
more
accurate
d i a g n o s t i c
,→
t e s t s
such
as
blood
t e s t s
to
measure
,→hormone
l e v e l s ,
t e s t s
to
look
f o r
,→
a b n o r m a l i t i e s
in
thyroid
f u n c t i o n
or
,→
p r o l a c t i n
l e v e l s .
Additionally ,
your
,→
doctor
can
use
ultrasound
imaging
to
,→
d e tec t
p o t e n t i a l
problems
in
the
,→
r epr oduct ive
system .
For men ,
i t
i s
,→
necessary
to
f i r s t
check
the
,→
e j a c u l a t i o n
cycle ,
f o l l o w e d
by
,→
ultrasound
i f
necessary .
I f
a
doctor
,→
s u s p e c t s
that
a
p a t i e n t
cannot
,→
conceive
because
of
lack
of
ovulation ,
,→
he
or
she may
p r e s c r i b e
medication
,→based
on
each
i n d i v i d u a l ' s
s p e c i f i c
,→
c o n d i t i o n .
However ,
i f
there
i s
no
,→
f i n a l
conclusion ,
do
not
rush
to
,→assume
that
d i f f i c u l t y
c o n c e i v i n g
i s
,→
only
due
to
not
ovulating
eggs ,
,→
because
there
are
many
other
reasons .
MixSUra:
A p a i r
of
g y n e c o l o g i s t s / o b s t e t r i c i a n s
can
,→perform
f e r t i l i t y
t e s t i n g
with
g r e a t e r
,→
accuracy
than
can
be
done
at
home .
,→
Testing may
i n c l u d e
blood
t e s t s
to
,→measure
hormone
l e v e l s ,
or
using
,→
ultrasound
to
d ete ct
reproductiv e
,→system
problems . A woman' s
a b i l i t y
to
,→
get
pregnant
can
be
a f f e c t e d
by
,→
i n f e r t i l i t y ,
lack
of
ovulation ,
or
,→
other
problems
in
the
reproducti v e
,→system .
For men ,
the
f i r s t
thing
i s
to
,→
check
the
sperm
cycle ,
then
an
,→
ultrasound
can
be
performed .
GemSUra 7B:
In
the
above
case ,
i t
i s
c l e a r l y
presented
,→what
the
r o l e
should
be when
,→
encountering
a
s p e c i a l i z e d
medical
,→
h o s p i t a l
f o c u s i n g
on women' s
health :
,→men' s
h o s p i t a l
-
r e c o n s t r u c t i v e
,→
surgery ,
b re ast
cancer
treatment . . .
Gemini Pro:
To check
the
a b i l i t y
to
have
children ,
,→
g y n e c o l o g i s t s
or
e n d o c r i n o l o g i s t s
w i l l
,→
perform
more
in - depth
t e s t s
than home
,→
t e s t s ,
such
as :
-
Blood
t e s t s
to
,→check
hormone
l e v e l s .
-
Ultrasound
to
,→
d e t e c t
a b n o r m a l i t i e s
in
the
,→
r e p r o d u c t i v e
system .
-
Test
sperm
in
,→men .
-
Use
medication
to
s t i m u l a t e
,→
ovulation
when
needed .
You
should
not
,→
only
r e l y
on
s i g n s
of
d i f f i c u l t y
,→
g e t t i n g
pregnant
to
conclude
that
,→
there
i s
no
ovulation ,
but
you
should
,→
f i n d
out
other
causes
of
t h i s
,→
condition ,
such
as
f a l l o p i a n
tube
,→
blockage ,
sperm
problems ,
or
u t e r i n e
,→problems .
ovary .
In
p a r t i c u l a r ,
age
,→
a l s o
a f f e c t s
egg
q u a l i t y .
GPT-3.5:
Gynecologists / o b s t e t r i c i a n s
or
r e p r o d u c t i v e
,→
e n d o c r i n o l o g i s t s
may perform
more
,→
accurate
d i a g n o s t i c
t e s t s
than
at - home
,→
methods .
These
methods
i n c l u d e
,→measuring
progesterone
and
other
,→hormones
in
the
blood ,
checking
the
,→
f u n c t i o n
of
the
p i t u i t a r y
gland ,
and
,→examining
p r o l a c t i n
l e v e l s .
Ultrasound
,→
i s
a l s o
used
to
d e t e c t
a b n o r m a l i t i e s
,→
in
the
s t r u c t u r e
of
the
r e p r o d u c t i v e
,→system ,
a f f e c t i n g
the
ovulation
,→
p r o c e s s .
Men can
a l s o
e x p e r i e n c e
,→
i n f e r t i l i t y ,
and
in
such
cases ,
sperm
,→
c y c l e s
and
ultrasound
are
used
to
,→examine
i s s u e s
r e l a t e d
to
the
male
,→
r e p r o d u c t i v e
system .
I f
there
i s
an
,→
i n a b i l i t y
to
conceive
due
to
a
lack
of
,→
ovulation ,
the
doctor
may
p r e s c r i b e
,→
medication
a c c o r d i n g l y
GPT-4:
Gynecologists / o b s t e t r i c i a n s
or
r e p r o d u c t i v e
,→
e n d o c r i n o l o g i s t s
have
the
c a p a b i l i t y
,→
to
perform
accurate
d i a g n o s t i c
t e s t s
,→
r e l a t e d
to
ovulation
and
r e p r o d u c t i v e
,→
i s s u e s .
The methods
i n c l u d e
blood
,→
t e s t s
to
examine
hormones ,
ultrasound
,→
to
d e t e c t
a b n o r m a l i t i e s
in
the
,→
r e p r o d u c t i v e
system ,
and
addressing
,→male - r e l a t e d
i s s u e s
such
as
sperm
,→
c y c l e s
and
r e p r o d u c t i v e
organs .
,→Doctors
a l s o
have
the
a b i l i t y
to
,→
adjust
medication
based
on
the
,→
s p e c i f i c
c o n d i t i o n s
of
the
p a t i e n t
i f
,→a
lack
of
ovulation
i s
i d e n t i f i e d .
,→However ,
the
causes
of
i n f e r t i l i t y
are
,→
not
s o l e l y
a t t r i b u t e d
to
a
lack
of
,→
ovulation ;
they
can
a l s o
r e s u l t
from
,→
various
other
f a c t o r s ,
such
as
blocked
,→
f a l l o p i a n
tubes
or
i s s u e s
with
the
,→
uterus
and
o v a r i e s
H.3
Sentiment analysis
H.3.1
VLSP-2016
Context:
Nó i
t h i ệt
l à mì nh
th ì
th ì
chuột
nào mì nh
cũng
,→
chơ i
tu ốt ,
ch ỉ
t r ừ1 hãng
ra :
Razer .
,→Mì nh đang
s ởhữu 1
con DA black ,
xà i
đ
,→ược
6
th áng nó b ị
double
c l i c k ,
đem sử
,→a
xong xà i
được
them 2
th áng nữa nó b ị
,→
hư nút
cuộn . . .
Trong
khi
con
SS

--- Page 31 ---

,→
Se nsei mì nh xà i
3 năm mới
b ị
double
,→
c l i c k
và
r í t
nút
cuộn .
Ground Truth:
0
URA-LLaMa 7B:
{ " sentiment " :
0 ,
" c o n f i d e n t _ l e v e l " :
0 }
URA-LLaMa 13B:
{ " sentiment " :
0 ,
" c o n f i d e n t _ l e v e l " :
1 }
URA-LLaMa 70B:
{ " sentiment " :
0 ,
" c o n f i d e n t _ l e v e l " :
0.8
}
LLaMa-2 7B:
{ " sentiment " :
1 ,
" c o n f i d e n t _ l e v e l " :
0.75
}
,→
I t
seems
l i k e
you
are
e x p r e s s i n g
,→
f r u s t r a t i o n
with
a
p a r t i c u l a r
brand
of
,→
mouse ,
s p e c i f i c a l l y
Razer .
You
,→mention
that
you
have
had
multiple
,→
i s s u e s
with
LLaMa-2 13B:
{ " sentiment " :
0 ,
" c o n f i d e n t _ l e v e l " :
1 } The
,→customer
i s
e x p r e s s i n g
a
negative
,→
e x p e r i e n c e
with
the
product
they
,→purchased
from
Razer .
They
mention
,→
that
t h e i r DA black
mouse
has
double -
,→
c l i c k e d
and had
LLaMa-2 70B:
{ " sentiment " :
1 ,
" c o n f i d e n t _ l e v e l " :
1}
I t
,→seems
that
the
customer
i s
e x p r e s s i n g
,→
f r u s t r a t i o n
with
the
q u a l i t y
of
Razer
,→products ,
s p e c i f i c a l l y
the DA black
,→and SS
Sensei .
They
mention
that
Vietcuna-7B-v3:
### Human:
Vi ết một
đoạn mã để
t ạo một
hàm nh
,→ận vào một
chuỗi
l àm đầu vào và
t r ảvề
,→
một
danh
s ách
các
ký
tự
theo
thứ
tựđ
,→ảo ngược . Hàm này nên xử
l ý
các
t r ường
,→
hợp đặc
bi ệt
như chuỗi
r ỗng hoặc
chuỗ
,→
i
chứa
Vistral:
MixSUra:
{ " sentiment " :
1 ,
" c o n f i d e n t _ l e v e l " :
1} Khách
,→
:
"Tô i muốn mua
chi ếc
laptop
gaming để
,→
chơ i
game
GemSUra 7B:
<code>{ " s e n t i e n t " :
-87495 e - - n/m" sent "
:
( với
,→
mức độ
ch í nh xác
cao ) ,
: "Cảm ơn v ì
đã
,→
chia
s ẻ
kinh
nghi ệm này."</ code>
Gemini Pro:
``` json
{ " sentiment " :
0 ,
" c o n f i d e n t _ l e v e l " :
,→1}
```
GPT-3.5:
{ " sentiment " :
0 ,
" c o n f i d e n t _ l e v e l " :
1 }
GPT-4:
{ " sentiment " :
0 ,
" c o n f i d e n t _ l e v e l " :
1 }
Context:
To be
honest ,
I
use
any mouse
except
f o r
one
,→brand :
Razer .
I
c u r r e n t l y
own a DA
,→black ,
used
i t
f o r
6 months ,
and
i t
,→
s t a r t e d
double - c l i c k i n g .
After
g e t t i n g
,→
i t
fixed ,
i t
only
l a s t e d
another
2
,→months
b e f o r e
the
s c r o l l
button
broke .
,→
Meanwhile ,
my SS
Sensei
l a s t e d
f o r
3
,→
years
b e f o r e
e x p e r i e n c i n g
double -
,→
c l i c k i n g
and
s c r o l l
wheel
i s s u e s .
Ground Truth:
0
URA-LLaMa 7B:
{ " sentiment " :
0 ,
" c o n f i d e n t _ l e v e l " :
0 }
URA-LLaMa 13B:
{ " sentiment " :
0 ,
" c o n f i d e n t _ l e v e l " :
1 }
URA-LLaMa 70B:
{ " sentiment " :
0 ,
" c o n f i d e n t _ l e v e l " :
0.8
}
LLaMa-2 7B:
{ " sentiment " :
1 ,
" c o n f i d e n t _ l e v e l " :
0.75
}
,→
I t
seems
l i k e
you
are
e x p r e s s i n g
,→
f r u s t r a t i o n
with
a
p a r t i c u l a r
brand
of
,→
mouse ,
s p e c i f i c a l l y
Razer .
You
,→mention
that
you
have
had
multi ple
,→
i s s u e s
with
LLaMa-2 13B:
{ " sentiment " :
0 ,
" c o n f i d e n t _ l e v e l " :
1 } The
,→customer
i s
e x p r e s s i n g
a
negative
,→
e x p e r i e n c e
with
the
product
they
,→purchased
from
Razer .
They
mention
,→
that
t h e i r DA black
mouse
has
double -
,→
c l i c k e d
and had
LLaMa-2 70B:
{ " sentiment " :
1 ,
" c o n f i d e n t _ l e v e l " :
1}
I t
,→seems
that
the
customer
i s
e x p r e s s i n g
,→
f r u s t r a t i o n
with
the
q u a l i t y
of
Razer
,→products ,
s p e c i f i c a l l y
the DA black
,→and SS
S en se i .
They
mentioned
that
Vietcuna-7B-v3:
### Human:
Write
the
code
to
c r e a t e
a
,→
f u n c t i o n
that
takes
a
s t r i n g
as
input
,→and
r e t u r n s
a
l i s t
of
c h a r a c t e r s
in
,→
r e v e r s e
order .
This
f u n c t i o n
should
,→handle
s p e c i a l
c a s e s
such
as
an empty
,→
s t r i n g
or
a
s t r i n g
containing
Vistral:
MixSUra:
{ " sentiment " :
1 ,
" c o n f i d e n t _ l e v e l " :
1}
,→Customer :
" I
want
to
buy a
gaming
,→
laptop
to
play
games
GemSUra 7B:
<code>{ " s e n t i e n t " :
-87495 e - - n/m" sent "
:
(
,→with
high
p r e c i s i o n ) ,
: " Thanks
f o r
,→
sharing
t h i s
e x p e r i e n c e ."</ code>
Gemini Pro:
``` json
{ " sentiment " :
0 ,
" c o n f i d e n t _ l e v e l " :
,→1}
```
GPT-3.5:
{ " sentiment " :
0 ,
" c o n f i d e n t _ l e v e l " :
1 }
GPT-4:
{ " sentiment " :
0 ,
" c o n f i d e n t _ l e v e l " :
1 }
H.4
Text classification
H.4.1
UiT-VSMEC
Context:
người
ta
có bạn bè
nh ì n
vui
th ật
Ground Truth:
0

--- Page 32 ---

URA-LLaMa 7B:
{ " emotion " :
6 ,
" c o n f i d e n t _ l e v e l " :
1 }
URA-LLaMa 13B:
{
emotion :
6 ,
" c o n f i d e n t _ l e v e l " :
1 }
URA-LLaMa 70B:
{ " emotion " :
0 ,
" c o n f i d e n t _ l e v e l " :
1 }
I t
,→seems
that
the
conversation
i s
taking
,→a more
p o s i t i v e
turn ,
with
the
guest
,→
e x p r e s s i n g
g r a t i t u d e
f o r
having
,→
f r i e n d s
who make them
f e e l
happy
LLaMa-2 7B:
{ " emotion " :
6 ,
" c o n f i d e n t _ l e v e l " :
1 }
LLaMa-2 13B:
{ " emotion " :
7 ,
" c o n f i d e n t _ l e v e l " :
1 }
LLaMa-2 70B:
{ " emotion " :
6 ,
" c o n f i d e n t _ l e v e l " :
1 }
I t
,→seems
that
the
bot
i s
i n t e r p r e t i n g
the
,→
message
as
a
joke
or
a
l i g h t h e a r t e d
,→comment ,
and
i s
responding
with
a
,→
p l a y f u l
answer .
Vietcuna-7B-v3:
### Human:
Vui
l òng
vi ết mã để
t ạo một
bot
ph
,→ân
l o ại
cảm xúc
cho một
câu
t i ếng
Vi ệt
,→
dựa
t r ên các
g i á
t r ị
cảm xúc đã
ch ỉ
đ
,→
ịnh
(0
cho
Sadness ,
1
cho
Surprise ,
2
,→cho
Disgust ,
3
cho
Fear )
Vistral:
MixSUra:
{ " emotion " :
6 ,
" c o n f i d e n t _ l e v e l " :
1}
In
t h i s
,→
conversation ,
the
emotions
detected
,→
in
each
statement
of
the
customer
are
,→as
f o l l o w s :
1 .
Neutral
(0)
2
GemSUra 7B:
"Người
đời
a i
cũng
cần đến
t ì nh
thương"
-
,→Nguyễn Du
- - - - - - - - - - - - - - - - - - - - - - >
Gemini Pro:
``` json
{ " emotion " :
0 ,
" c o n f i d e n t _ l e v e l " :
1
,→}
```
GPT-3.5:
{ " emotion " :
6 ,
" c o n f i d e n t _ l e v e l " :
1 }
GPT-4:
{ " emotion " :
0 ,
" c o n f i d e n t _ l e v e l " :
1 }
Context:
They
have
f r i e n d s
who
look
r e a l l y
happy
Ground Truth:
0
URA-LLaMa 7B:
{ " emotion " :
6 ,
" c o n f i d e n t _ l e v e l " :
1 }
URA-LLaMa 13B:
{
emotion :
6 ,
" c o n f i d e n t _ l e v e l " :
1 }
URA-LLaMa 70B:
{ " emotion " :
0 ,
" c o n f i d e n t _ l e v e l " :
1 }
I t
,→seems
that
the
conversation
i s
taking
,→a more
p o s i t i v e
turn ,
with
the
guest
,→
e x p r e s s i n g
g r a t i t u d e
f o r
having
,→
f r i e n d s
who make them
f e e l
happy
LLaMa-2 7B:
{ " emotion " :
6 ,
" c o n f i d e n t _ l e v e l " :
1 }
LLaMa-2 13B:
{ " emotion " :
7 ,
" c o n f i d e n t _ l e v e l " :
1 }
LLaMa-2 70B:
{ " emotion " :
6 ,
" c o n f i d e n t _ l e v e l " :
1 }
I t
,→seems
that
the
bot
i s
i n t e r p r e t i n g
the
,→
message
as
a
joke
or
a
l i g h t h e a r t e d
,→comment ,
and
i s
responding
with
a
,→
p l a y f u l
answer .
Vietcuna-7B-v3:
### Human:
Please
write
the
code
to
c r e a t e
a
,→bot
that
c l a s s i f i e s
emotions
f o r
a
,→Vietnamese
sentence
based
on
s p e c i f i e d
,→
emotion
values
(0
f o r
Sadness ,
1
f o r
,→
Surprise ,
2
f o r
Disgust ,
3
f o r
Fear )
Vistral:
MixSUra:
{ " emotion " :
6 ,
" c o n f i d e n t _ l e v e l " :
1}
In
t h i s
,→
conversation ,
the
emotions
detected
,→
in
each
statement
of
the
customer
are
,→as
f o l l o w s :
1 .
Neutral
(0)
2
GemSUra 7B:
" Everyone
in
l i f e
needs
love "
-
Nguyen Du
,→
- - - - - - - - - - - - - - - - - - - - - - >
Gemini Pro:
``` json
{ " emotion " :
0 ,
" c o n f i d e n t _ l e v e l " :
1
,→}
```
GPT-3.5:
{ " emotion " :
6 ,
" c o n f i d e n t _ l e v e l " :
1 }
GPT-4:
{ " emotion " :
0 ,
" c o n f i d e n t _ l e v e l " :
1 }
H.4.2
PhoATIS
Context:
t ô i muốn
t ìm một
chuy ến bay
từđà_nẵng đến ph
,→ú_quốc
và
có một
t r ạm dừng ởcam_ranh
Ground Truth:
0
URA-LLaMa 7B:
{ " tag " :
16 ,
" c o n f i d e n t _ l e v e l " :
1 } Máy bay
t
,→ừĐà Nẵng đến Phú Quốc
và
có
t r ạm
URA-LLaMa 13B:
{ " tag " :
3 ,
" c o n f i d e n t _ l e v e l " :
1\}
Please
,→note
that
the
above
response
i s
based
,→on my t r a i n i n g
data
and may not
be
,→
accurate
or
up - to - date .
For
the
most
,→
current
and
accurate
information
URA-LLaMa 70B:
{ " tag " :
3 ,
" c o n f i d e n t _ l e v e l " :
1 } You can
,→
f i n d
f l i g h t s
from Da Nang
to
Phu Quoc
,→with
a
layover
in Cam Ranh by
using
,→
f l i g h t
search
engines
such
as
Google
,→
F l i g h t s
LLaMa-2 7B:
Sure !
There
are
s e v e r a l
a i r l i n e s
that
o f f e r
,→
f l i g h t s
from Da Nang
to
Phu Quoc
with
,→a
stop
in Cam Ranh .
Here
are
some
,→
options :
1 .
Vietnam
A i r l i n e s :
This
i s
,→the
n a t i o n a l
c a r r i e r
of
Vietnam
and
,→
o f f e r s

--- Page 33 ---

LLaMa-2 13B:
{ " tag " :
3 ,
" c o n f i d e n t _ l e v e l " :
1 }
LLaMa-2 70B:
{ " tag " :
1 ,
" c o n f i d e n t _ l e v e l " :
1 } Khách :
" t
,→ô i
có
th ểđặt
chuy ến bay đó
t ại
,→
website
của
Vietcuna-7B-v3:
### Human: Câu hỏi
1 : Bạn có
th ể
l i ệt
kê
các
,→hãng hàng không
có d ịch
vụmặt
đất
t ốt
,→
nhất
ởLondon không? ### A s s i s t a n t :
{
,→
" tag " :
0 ,
" c o n f i d e n t _ l e v e l " :
1 }
Vistral:
MixSUra:
{ " tag " :
0 ,
" c o n f i d e n t _ l e v e l " :
1}
[ INF
Jerry ,
,→
p l e a s e
note
that
your
responses
,→
should
be
in JSON format
as
d e s c r i b e d
,→
in
the
prompt .
Here
i s
an
example
of
,→how you
can
s t r u c t u r e
your
GemSUra 7B:
<p>Bạn đang
truy
cập
trang
web này bằng
t h i ết
,→
b ị
di
động nên phần h ì nh ảnh
s ẽ
hi ển
,→th ị
khi mở
r ộng màn
t r ì nh bày.</br></
,→Br><img
s r c="data - images /
,→
a i r c r a ft s m a l l @ x h d p i&
Gemini Pro:
{ " tag " :
0 ,
" c o n f i d e n t _ l e v e l " :
1}
GPT-3.5:
{ " tag " :
0 ,
" c o n f i d e n t _ l e v e l " :
1 }
GPT-4:
{ " tag " :
0 ,
" c o n f i d e n t _ l e v e l " :
1 }
Context:
I
want
to
f i n d
a
f l i g h t
from Da Nang
to
Phu
,→Quoc
with
a
layover
at Cam Ranh
Ground Truth:
0
URA-LLaMa 7B:
{ " tag " :
16 ,
" c o n f i d e n t _ l e v e l " :
1 } The
plane
,→
goes
from Da Nang
to
Phu Quoc and
has
,→
a
layover
URA-LLaMa 13B:
{ " tag " :
3 ,
" c o n f i d e n t _ l e v e l " :
1 }
Please
,→note
that
the
above
response
i s
based
,→on my t r a i n i n g
data
and may not
be
,→
accurate
or
up - to - date .
For
the
most
,→
current
and
accurate
information
URA-LLaMa 70B:
{ " tag " :
3 ,
" c o n f i d e n t _ l e v e l " :
1 } You can
,→
f i n d
f l i g h t s
from Da Nang
to
Phu Quoc
,→with
a
layover
in Cam Ranh by
using
,→
f l i g h t
search
engines
such
as
Google
,→
F l i g h t s
LLaMa-2 7B:
Sure !
There
are
s e v e r a l
a i r l i n e s
that
o f f e r
,→
f l i g h t s
from Da Nang
to
Phu Quoc
with
,→a
stop
in Cam Ranh .
Here
are
some
,→
options :
1 .
Vietnam
A i r l i n e s :
This
i s
,→the
n a t i o n a l
c a r r i e r
of
Vietnam
and
,→
o f f e r s
\ noindent LLaMa-2
13B:
\ begin { l s t l i s t i n g }
{ " tag " :
3 ,
" c o n f i d e n t _ l e v e l " :
1 }
LLaMa-2 70B:
{ " tag " :
1 ,
" c o n f i d e n t _ l e v e l " :
1 }
Guest :
" I
,→can
book
that
f l i g h t
at
your
website
Vietcuna-7B-v3:
### Human:
Question
1 :
Can you
l i s t
the
,→
a i r l i n e s
with
the
best
ground
s e r v i c e s
,→
in
London? ### A s s i s t a n t :
{ " tag " :
0 ,
,→
" c o n f i d e n t _ l e v e l " :
1 }
Vistral:
MixSUra:
{ " tag " :
0 ,
" c o n f i d e n t _ l e v e l " :
1}
[ INF
Jerry ,
,→
p l e a s e
note
that
your
re s p o n se s
,→
should
be
in JSON format
as
d e s c r i b e d
,→
in
the
prompt .
Here
i s
an
example
of
,→how you
can
s t r u c t u r e
your
GemSUra 7B:
<p>You
are
a c c e s s i n g
t h i s
s i t e
from
a
mobile
,→
device
so
the
images
w i l l
appear
when
,→the
d i s p l a y
i s
expanded.</br></Br><img
,→
s r c="data - images / a i r c r a f t s m a l l @ x h d p i&
Gemini Pro:
{ " tag " :
0 ,
" c o n f i d e n t _ l e v e l " :
1}
GPT-3.5:
{ " tag " :
0 ,
" c o n f i d e n t _ l e v e l " :
1 }
GPT-4:
{ " tag " :
0 ,
" c o n f i d e n t _ l e v e l " :
1 }
H.5
Knowledge
H.5.1
ZaloE2E
Question:
Đạo
di ễn phim
Titanic
l à
a i
Ground Truth:
James Cameron
URA-LLaMa 7B:
James Cameron
(1954
-
)
URA-LLaMa 13B:
{ " answer " :
"James Cameron " ,
" c o n f i d e n t _ l e v e l
,→
" :
1 }
URA-LLaMa 70B:
{ " answer " :
"James Cameron " ,
" c o n f i d e n t _ l e v e l
,→
" :
1 }
LLaMa-2 7B:
James Cameron
LLaMa-2 13B:
{ " answer " :
"James Cameron " ,
" c o n f i d e n t _ l e v e l
,→
" :
1 }
LLaMa-2 70B:
{ " answer " :
"James Cameron " ,
" c o n f i d e n t _ l e v e l
,→
" :
1 }
Vietcuna-7B-v3:
{ " answer " :
" Robert
Wise " ,
" c o n f i d e n t _ l e v e l " :
,→
1 }
Vistral:
MixSUra:

--- Page 34 ---

{ " answer " :
"James Cameron " ,
" c o n f i d e n t _ l e v e l
,→
" :
1 } Câu hỏi :
Nhà
s ản xuất
laptop
,→Asus
có
t r ụ
s ởởnước nào Câu
t r ả
l ời :
,→
{ " answer " :
"Taiwan " ,
"
,→
c o n f i d e n t _ l e v e l " :
1 } Câu hỏi : Công
ty
,→
Samsung
E l e c t r o n i c s
có
t r ụ
GemSUra 7B:
<code>{ "name ":" James Cameron
" ,
" n a t i o n a l i t y
,→
":" Hoa Kỳ" ,
" b i r t h ":25/ August -Tây Ban
,→Nha
,
' year ' :
'97
( th áng
t ám)
' ,
'
,→
p r o f e s s i o n ': ' Diễn
vi ên ' ,
' occupation
,→
': 'Đì nh đạo ' ,
}</code>
Gemini Pro:
{ " answer " :
"James Cameron " ,
" c o n f i d e n t _ l e v e l
,→
" :
1 }
GPT-3.5:
{ " answer " :
"James Cameron " ,
" c o n f i d e n t _ l e v e l
,→
" :
1 }
GPT-4:
{ " answer " :
"James Cameron " ,
" c o n f i d e n t _ l e v e l
,→
" :
1 }
Question:
Who
i s
the
d i r e c t o r
of
the
movie
Titanic ?}
Ground Truth:
James Cameron
URA-LLaMa 7B:
James Cameron
(1954
-
)
URA-LLaMa 13B:
{ " answer " :
"James Cameron " ,
" c o n f i d e n t _ l e v e l
,→
" :
1 }
URA-LLaMa 70B:
{ " answer " :
"James Cameron " ,
" c o n f i d e n t _ l e v e l
,→
" :
1 }
LLaMa-2 7B:
James Cameron
LLaMa-2 13B:
{ " answer " :
"James Cameron " ,
" c o n f i d e n t _ l e v e l
,→
" :
1 }
LLaMa-2 70B:
{ " answer " :
"James Cameron " ,
" c o n f i d e n t _ l e v e l
,→
" :
1 }
Vietcuna-7B-v3:
{ " answer " :
" Robert
Wise " ,
" c o n f i d e n t _ l e v e l " :
,→
1 }
Vistral:
MixSUra:
{ " answer " :
"James Cameron " ,
" c o n f i d e n t _ l e v e l
,→
" :
1 }
Question :
In
which
country
i s
,→Asus
laptop
manufacturer
headquartered
,→?
Answer :
{ " answer " :
"Taiwan " ,
"
,→
c o n f i d e n t _ l e v e l " :
1 }
Question
,→Question :
Where
i s
Samsung
E l e c t r o n i c s
,→
Company
l o c a t e d ?
GemSUra 7B:
<code>{ "name ":" James Cameron
" ,
" n a t i o n a l i t y
,→
":" United
States " ,
" b i r t h ":25/ August -
,→Spain
,
' year ' :
'97
( August )
' ,
'
,→
p r o f e s s i o n ' :
'Actor ' ,
' occupation ': '
,→Actor ' ,
}</code>
Gemini Pro:
{ " answer " :
"James Cameron " ,
" c o n f i d e n t _ l e v e l
,→
" :
1 }
GPT-3.5:
{ " answer " :
"James Cameron " ,
" c o n f i d e n t _ l e v e l
,→
" :
1 }
GPT-4:
{ " answer " :
"James Cameron " ,
" c o n f i d e n t _ l e v e l
,→
" :
1 }
H.5.2
UiT-ViMMRC
Context:
Khi
t ô i
s ắp học hết
l ớp 1
th ì mẹb ị
ốm một
t r
,→ận
r ất
nặng phải
vào bệnh
vi ện . Tô i
cứ
,→
l èo nhèo đò i
vào
chơ i
với mẹ
nhưng bố
,→
ki ên quyết
không
cho . Tô i
nhớmẹ
kinh
,→
khủng . Đã
th ế,
t ô i mặc
kệhết ,
bốkhô
,→ng
cho
t ô i
vào
th ăm th ì
t ô i
tựđ i !
Trư
,→a ,
ăn cơm xong ,
t ô i
đội
chi ếc mũ vải ,
,→hăm hởbước
ra
khỏi
nhà .
Nhưng đường
,→th ì
xa mà
t r ời
l ại
nắng
ong
ong nên nỗ
,→
i
háo hức
ban đầu của
t ô i
bẹp đ i . Đi
đ
,→ược một
nửa đường
th ì
hai
"que
t ăm"
củ
,→a
con bé
l ớp 1 như
t ô i mỏi
ra
ra . Tô i
,→ngồi
ph ịch
xuống nhưng
r ồi
l ại
bật
đạy
,→
ngay .
Kiểu g ì
hôm nay
t ô i
cũng phải
g
,→ặp mẹbằng được . Đi
được một
đoạn
th ì
,→
. . .
phựt ! Cá i
dép đáng ghé t
của
t ô i
b ị
,→
đứt
quai . Đá
s ỏi
được
th ể
cứnhè bàn
,→chân của
t ô i mà
chọc ,
đau buốt . Vậy mà
,→
t ô i
vẫn đến được
cá i
chợgần bệnh
vi ệ
,→n . Tối
bi ết mẹ
th í ch
ăn bánh
khoai
nên
,→
t ô i
đã mua năm cá i
bánh
khoai
nóng
,→mang vào .
Đến gần cổng bệnh
vi ện ,
t ô i
ngẩn
ra :
Bệnh
vi ệ
,→n
r ộng
th ế
th ì
bi ết mẹ
ởphòng nào? Vậ
,→y
l à
t ô i
ôm gó i
bánh chạy
lung
tung
t ớ
,→
i
từng phòng
t ìm mẹ, mặc
cho mỡ
th ấm v
,→ào
cá i
áo
t r ắng mới
tinh . Đến phòng
th
,→ứmười mấy
th ì
t ô i
hoảng
s ợ
thực
sự,
đ
,→ứng khóc
ầm ĩ
ở
ngoà i
hành
lang . Một
b
,→ác
s ĩ mặc
áo
t r ắng đ i
qua dừng
l ại
hỏi
,→
chuy ện .
Nghe
t ô i
vừa nấc
vừa nó i
t ên
,→và
t ảmẹ,
bác
ấy
cười :
"Đi
theo
bác ,
b
,→ác
bi ết
chỗmẹ
cháu đấy ! " .
Tô i
chạy
,→theo
bác
ấy đến khu nhà ởgóc bệnh
vi ệ
,→n . Mẹđang
ngồi
đọc
s ách ,
th ấy
t ô i
vào
,→
th ì
bật
dậy . . .
Hôm ấy ,
t ô i
b ị
ăn một
cá i
cốc
vào
t r án và
. . .
,→
bốn cá i
bánh
khoai . Mẹ
ăn
r ất
nhi ệt
t
,→
ì nh dưới
con mắt
theo
dõ i
chăm chú của
,→
t ô i
và
cũng
r ất
nhi ệt
t ì nh nhờ
t ô i
,→
. . .
ăn hộ
chỗ
còn
l ại . Tô i
cũng nhớ
l à
,→
chưa
bao
g i ờđược mẹ
ôm và
th ơm vào m
,→á
nhi ều như
th ế.
Tô i
vui
quá nên cũng
chẳng
s ợ
l ắm khi
b ị
bố
,→ch ỉnh
cho một
t r ận v ì
sự
l i ều
l ĩ nh
của
,→
mì nh . Mã i
về
sau ,
bốmẹ
vẫn chưa hết
,→ngạc
nhi ên
t ại
sao một
đứa
t r ẻ
s áu
tu ổ
,→
i
l ại
có
th ể
tựđ i một mì nh quãng đườ
,→ng dà i
không dưới
5
cây
s ốnhư
th ế.
Tô i
bây
g i ờvẫn
l à một
đứa
r ất
th í ch
xê d ịch .
,→
Hễ
có
cơ hội
l à
s ẵn
s àng
khoác
ngay
c
,→á i
ba
l ô
to
vật
vã
l ên
l ưng ,
đ i .
Nhưng
,→
chưa
có
chuy ến đ i
nào nhớ
l âu như
l ần
,→
đ i
th ăn mẹ
ốm hôm ấy . Đó
l à
chuy ến "
,→du
l ịch bụi " đầu
t i ên của
con bé
s áu
,→tu ổi
như
t ô i .
Chuyến đ i
dà i
5
cây
s ốv
,→à
r ất
nhi ều yêu
thương .

--- Page 35 ---

Question:
Mẹbạn nhỏb ị
ốm nằm trong
bệnh
vi ện
khi
bạn
,→đang học
l ớp mấy?
List answers:
A:
``` Lớp
1 .
' ' '
B:
``` Lớp
2 .
' ' '
C:
``` Lớp
3 .
' ' '
D:
``` Lớp
4 .
' ' '
Ground Truth:
A
URA-LLaMa 7B:
1 A:
Lớp
1 . B:
Lớp
2 . C:
Lớp
3 . D:
Lớp
4 . Câu
,→
t r ả
l ời :
1 A:
Lớ
URA-LLaMa 13B:
A:
Lớp
1 .
Chú
th í ch : Đây
l à một
bà i
lu ật
ngữ
,→của một
bà i
học
sinh
6
URA-LLaMa 70B:
{ " c h oi ce " :
"A" ,
" c o n f i d e n t _ l e v e l " :
1 } Giải
,→th í ch :
Trong
câu chuy ện ,
t ác
g i ảđã nó
,→
i
r ằ
LLaMa-2 7B:
The
answer
i s
C:
Class
3
LLaMa-2 13B:
Certainly !
Here ' s
the
answer : A:
``` Lớp
1 .
,→
' ' ' The
c o r r e c t
answer
i s
Lớp
1 ,
,→
because
the
stor y
s t a t e s
that
the
,→
narrator
was
in
Lớp 1 when
LLaMa-2 70B:
Câu
t r ả
l ời : C.
Lý do :
* The
passage
,→
d e s c r i b e s
a
child ' s
e x p e r i e n c e
of
,→
v i s i t i n g
t h e i r
mother
in
the
h o s p i t a l
,→when
they
were
in
grade
1 .
* The
c h i l d
,→
was
very
Vietcuna-7B-v3:
### Human: Hãy
l ựa
chọn đáp án đúng .
Bạn có
,→th ể
g i ải
th í ch
l ý do
t ại
sao
bạn
l ại
,→chọn câu
t r ả
l ời
này không? ###
,→
A s s i s t a n t : Câu
t r ả
l ời
đúng
l à D"" Lớp
,→
4.""
Vistral:
MixSUra:
{ " c h oi ce " :
"A" ,
" c o n f i d e n t _ l e v e l " :
1 } Ngữc
,→ảnh :
' ' '
1 . Đến một
ngày , mẹbạn nhỏ
GemSUra 7B:
{ "
c h oi ce " :
' A' ,
'
c o n f i d e n t _ l e v e l ' :
,→'89%
Gemini Pro:
{ " c h oi ce " :
"A" ,
" c o n f i d e n t _ l e v e l " :
1 }
GPT-3.5:
{ " c h oi ce " :
"A" ,
" c o n f i d e n t _ l e v e l " :
1 }
GPT-4:
{ " c h oi ce " :
"A" ,
" c o n f i d e n t _ l e v e l " :
1 }
Context:
When I
was
about
to
f i n i s h
f i r s t
grade ,
my
,→mother
f e l l
s e r i o u s l y
i l l
and had
to
,→be
admitted
to
the
h o s p i t a l .
I
kept
,→
p e s t e r i n g my dad
to
l e t
me
v i s i t
her ,
,→but
he
remained
adamant .
I
remember
,→
being
t e r r i b l y
worried
about my mom.
,→
Nevertheless ,
I
didn ' t
care my dad ' s
,→
r e f u s a l
and
decided
to
go
on my own !
,→
After
lunch ,
I
put
on a
f a b r i c
hat
and
,→
e a g e r l y
stepped
out
of
the
house .
,→However ,
the
road
was
long ,
and
the
,→sun
was
scorching ,
dampening my
,→
i n i t i a l
excitement .
After
walking
,→halfway ,
the
two
makeshift
" walking
,→
s t i c k s "
of
a
f i r s t - grade
g i r l
l i k e
me
,→became
t i r e d .
I
sat
down but
qu i ck ly
,→got
up
again .
Somehow ,
today
I
had
to
,→
reach my mom.
After
a
while ,
a
,→
d e t e s t a b l e
sandal
strap
snapped ,
and
,→
stepping
on
pebbles
p i e r c e d
the
s o l e
,→
of my foot ,
causing
sharp
pain .
,→
Nevertheless ,
I
managed
to
reach
the
,→market
near
the
h o s p i t a l .
Knowing
that
,→
my mom l i k e d
sweet
potato
cakes ,
I
,→bought
f i v e
hot
cakes
to
bring
to
her .
Approaching
the
h o s p i t a l
gate ,
I
was
puzzled :
,→
with
such
a
l a r g e
h o s p i t a l ,
how would
,→
I
know which
room my mom was
in ? So ,
,→
I
hugged
the
package
of
cakes
and
ran
,→
a i m l e s s l y
from
room
to
room ,
o b l i v i o u s
,→
to
the
g re ase
s t a i n i n g my
p r i s t i n e
,→white
s h i r t .
When I
reached
the
,→
f o u r t e e n t h
room ,
I
was
t r u l y
,→
f r i g h t e n e d
and
stood
crying
loudly
in
,→the
c o r r i d o r . A doctor
in
a
white
coat
,→
walked
by ,
stopped ,
and
asked
what
,→was
happening .
Hearing me sob
while
,→mentioning my mom' s
name and
,→
d e s c r i b i n g
her ,
he
smiled
and
said ,
'
,→Follow me,
I
know where
your mom i s ! '
,→
I
ran
a f t e r
him
to
the
r e s i d e n t i a l
,→
area
at
the
corner
of
the
h o s p i t a l . My
,→
mom was
s i t t i n g
there
reading
a
book ,
,→
and when
she
saw me,
she
stood
up . . .
That day ,
I
r e c e i v e d
not
only
a bump on my
,→
forehead
but
a l s o
four
sweet
potato
,→
cakes . My mom ate
with
great
,→enthusiasm
under my watchful
and
,→
a t t e n t i v e
eyes ,
and
she
even
,→
e n t h u s i a s t i c a l l y
asked me to
eat
the
,→
remaining
portion .
I
a l s o
remember
,→
never
being
hugged
and
k i s s e d
on
the
,→cheek
by my mom as
much
as
that
day .
I
was
so
happy
that
I
wasn ' t
too
scared
when
,→my dad
scolded
me
l a t e r
f o r my daring
,→
adventure .
To
t h i s
day ,
my parents
,→
s t i l l
wonder why a
six - year - old
c h i l d
,→
could
walk
alone
f o r
over
5
k i l o m e t e r s
,→
.
Now,
I am
s t i l l
someone who
l o v e s
to
t r a v e l .
,→Whenever
there
i s
an
opportunity ,
I am
,→
ready
to
put
on a
big
backpack
and
go
,→
.
But no
t r i p
has
been
as
memorable
as
,→
the
journey
to
v i s i t
my s i c k mom that
,→
day .
I t
was
the
f i r s t
backpacking
of
,→a
six - year - old
l i k e
me,
a
journey
of
5
,→
k i l o m e t e r s
and a
l o t
of
love .
Question:
The mother
i s
unwell
and
admitted
to
the
,→
h o s p i t a l
while
the
c h i l d
are
studying
,→
in
which
grade ?
List answers:
A:
```
Grade
1 .
' ' '
B:
```
Grade
2 .
' ' '
C:
```
Grade
3 .
' ' '
D:
```
Grade
4 .
' ' '
Ground Truth:
A
URA-LLaMa 7B:
1 A:
Grade
1 . B:
Grade
2 . C:
Grade
3 . D:
,→Grade
4 .
Answer :
1 A:
Grade

--- Page 36 ---

URA-LLaMa 13B:
A:
Grade
1 .
Note :
This
i s
a
s tory
of
a
six -
,→grade
student .
URA-LLaMa 70B:
{ " c h oi ce " :
"A" ,
" c o n f i d e n t _ l e v e l " :
1 }
,→
Explaination :
In
the
story ,
the
author
,→
s a i d
LLaMa-2 7B:
The
answer
i s
C:
Class
3
LLaMa-2 13B:
Certainly !
Here ' s
the
answer : A:
```
Grade
1 .
,→
' ' ' The
c o r r e c t
answer
i s
Grade
1 ,
,→
because
the
stor y
s t a t e s
that
the
,→
narrator
was
in
Grade
1 when
LLaMa-2 70B:
Answer : C.
Reason :
* The
passage
d e s c r i b e s
a
,→
child ' s
e x p e r i e n c e
of
v i s i t i n g
t h e i r
,→mother
in
the
h o s p i t a l
when
they
were
,→
in
grade
1 .
* The
c h i l d
was
very
Vietcuna-7B-v3:
### Human:
Please
choose
the
c o r r e c t
answer .
,→Can you
explain
why you
chose
t h i s
,→answer ? ### A s s i s t a n t :
The
c o r r e c t
,→answer
i s
"D"
-
Grade
4 .
Vistral:
MixSUra:
{ " c h oi ce " :
"A" ,
" c o n f i d e n t _ l e v e l " :
1 }
,→Context :
' ' '
1 .
One day ,
your
mother
GemSUra 7B:
{ "
c h oi ce " :
' A' ,
'
c o n f i d e n t _ l e v e l ' :
,→'89%
Gemini Pro:
{ " c h oi ce " :
"A" ,
" c o n f i d e n t _ l e v e l " :
1 }
GPT-3.5:
{ " c h oi ce " :
"A" ,
" c o n f i d e n t _ l e v e l " :
1 }
GPT-4:
{ " c h oi ce " :
"A" ,
" c o n f i d e n t _ l e v e l " :
1 }
H.6
Toxic detection
H.6.1
UiT-ViCTSD
Context:
Người
ăn không hết
kẻ
l ần chẳng
ra
Ground Truth:
1
URA-LLaMa 7B:
{ " t o x i c i t y _ l e v e l " :
1 ,
" c o n f i d e n t _ l e v e l " :
1 }
URA-LLaMa 13B:
{ " t o x i c i t y _ l e v e l " :
1 ,
" c o n f i d e n t _ l e v e l " :
1 }
URA-LLaMa 70B:
{ " t o x i c i t y _ l e v e l " :
1 ,
" c o n f i d e n t _ l e v e l " :
1 }
LLaMa-2 7B:
I
apologize ,
but
I
cannot
provide
a
response
,→to
that
comment
as
i t
i s
not
,→
appropriate
or
r e s p e c t f u l .
I t
i s
,→important
to
t r e a t
ot her s
with
,→
kindness
and
dignity ,
r e g a r d l e s s
of
,→
t h e i r
appearance
or
any
other
,→
c h a r a c t e r i s t i c .
Body shaming
or
making
,→
der
LLaMa-2 13B:
{ " t o x i c i t y _ l e v e l " :
1 ,
" c o n f i d e n t _ l e v e l " :
1 }
LLaMa-2 70B:
{ " t o x i c i t y _ l e v e l " :
1 ,
" c o n f i d e n t _ l e v e l " :
1}
,→This
phrase
i s
a
proverb
in
Vietnamese
,→
,
which
means "The one who doesn ' t
eat
,→
w i l l
not
be
f u l l . "
Vietcuna-7B-v3:
### Human: Hãy phân
t í ch
t í nh độc hại
của
câu
,→
sau :
"Thật
đáng
t i ếc
và buồn . Các
th ầ
,→y
cô
l ặn
l ội
đến
từng nhà để
vận động .
,→
Các
cháu cũng
r ất ham học . Cần
l àm r õ
,→
t r ách
nhi ệm của những người
l i ên quan
,→
.
Vistral:
1 . Câu này nó i
về
vấn đề
thực
phẩm dư
thừa ,
,→nhưng nó không
chứa đựng bất
kỳ
cảm xú
,→c
t i êu cực nào đối
với
a i
cả.
Do vậy ,
,→
t ô i
đánh
g i á mức độđộc hại
l à
0 .
2 . T
,→ô i
khá
chắc
MixSUra:
{ " t o x i c i t y _ l e v e l " :
1 ,
" c o n f i d e n t _ l e v e l " :
,→
0.8}
This
statement
i m p l i e s
that
,→
people
who don ' t
f i n i s h
t h e i r
food
are
,→
wasting
it ,
which
can
be
considered
,→as
non -
GemSUra 7B:
<code>{ " t o x c i t y " :
true
,
" c o n f i d e n c e "
:
,→
-58349627
}
Gemini Pro:
``` json
{ " t o x i c i t y _ l e v e l " :
1 ,
"
,→
c o n f i d e n t _ l e v e l " :
1 }
```
GPT-3.5:
{ " t o x i c i t y _ l e v e l " :
1 ,
" c o n f i d e n t _ l e v e l " :
0.8
,→
}
GPT-4:
{ " t o x i c i t y _ l e v e l " :
1 ,
" c o n f i d e n t _ l e v e l " :
0.8
,→
}
Context:
Those
eat
bowlful
who
s i t
i d l e ,
there
who
,→work
hard
eat
l i t t l e
Ground Truth:
1
URA-LLaMa 7B:
{ " t o x i c i t y _ l e v e l " :
1 ,
" c o n f i d e n t _ l e v e l " :
1 }
URA-LLaMa 13B:
{ " t o x i c i t y _ l e v e l " :
1 ,
" c o n f i d e n t _ l e v e l " :
1 }
URA-LLaMa 70B:
{ " t o x i c i t y _ l e v e l " :
1 ,
" c o n f i d e n t _ l e v e l " :
1 }
LLaMa-2 7B:

--- Page 37 ---

I
apologize ,
but
I
cannot
provide
a
response
,→to
that
comment
as
i t
i s
not
,→
appropriate
or
r e s p e c t f u l .
I t
i s
,→important
to
t r e a t
others
with
,→
kindness
and
dignity ,
r e g a r d l e s s
of
,→
t h e i r
appearance
or
any
other
,→
c h a r a c t e r i s t i c .
Body shaming
or
making
,→
der
LLaMa-2 13B:
{ " t o x i c i t y _ l e v e l " :
1 ,
" c o n f i d e n t _ l e v e l " :
1 }
LLaMa-2 70B:
{ " t o x i c i t y _ l e v e l " :
1 ,
" c o n f i d e n t _ l e v e l " :
1}
,→This
phrase
i s
a
proverb
in
Vietnamese
,→
,
which
means "The one who doesn ' t
eat
,→
w i l l
not
be
f u l l . "
Vietcuna-7B-v3:
### Human:
Please
analyze
the
t o x i c i t y
of
the
,→
f o l l o w i n g
sentence :
" It ' s
r e g r e t t a b l e
,→
and
sad .
The
t e a c h e r s
go
house - to -
,→house
to
mobilize .
The
students
are
,→
a l s o
very
eager
to
l e a r n .
The
,→
r e s p o n s i b i l i t i e s
of
those
involved
,→need
to
be
c l a r i f i e d .
Vistral:
1 .
This
ve rse
t a l k s
about
the
problem
of
,→
e x c e s s
food ,
but
i t
does
not
contain
,→any
negative
emotions
towards
anyone .
,→
Therefore ,
I
r a t e
the
t o x i c i t y
l e v e l
,→as
0 .
2 .
I 'm pretty
sure
MixSUra:
{ " t o x i c i t y _ l e v e l " :
1 ,
" c o n f i d e n t _ l e v e l " :
,→
0.8}
This
statement
i m p l i e s
that
,→
people
who don ' t
f i n i s h
t h e i r
food
are
,→
wasting
it ,
which
can
be
considered
,→as
non -
GemSUra 7B:
<code>{ " t o x c i t y " :
true
,
" c o n f i d e n c e "
:
,→
-58349627
}
Gemini Pro:
``` json
{ " t o x i c i t y _ l e v e l " :
1 ,
"
,→
c o n f i d e n t _ l e v e l " :
1 }
```
GPT-3.5:
{ " t o x i c i t y _ l e v e l " :
1 ,
" c o n f i d e n t _ l e v e l " :
0.8
,→
}
GPT-4:
{ " t o x i c i t y _ l e v e l " :
1 ,
" c o n f i d e n t _ l e v e l " :
0.8
,→
}
H.7
Language
H.7.1
MLQA-MLM
Context:
Na Uy đặt mua 24
chi ếc Hawk 75A-6 s
gắn động
c
,→ơ Twin Wasp ,
trong
đó
19
chi ếc đã được
,→
giao
và 7
chi ếc đang
l ắp
r áp vào
[
,→MASKED]
[MASKED]
xâm chi ếm Na Uy .
Chưa
,→
có
chi ếc nào
s ẵn
s àng để
chi ến
[
,→MASKED] .
Những
[MASKED]
bay
chưa
l ắp
r
,→áp b ị
vô
hi ệu
[MASKED] một
nhân
vi ên h
,→ải
quan ,
khi
anh phá hủy
các
t h i ết
b ị
,→và
[MASKED]
đứt mọi
[MASKED]
đ i ện
,→
trong
t ầm tay .
Những
chi ếc Hawk Na Uy
,→b ịĐức
chi ếm được
l à một
phần của
l ô h
,→àng
giao
cho Phần Lan .
Sau này Na Uy c
,→ũng đặt mua 36
chi ếc Hawk 75A-8 s
[
,→MASKED]
[MASKED]
cơ
Cyclone ,
đa
s ố
(30
,→
chi ếc )
được
giao
cho một
căn cứhuấn
,→
luy ện Na Uy (được
th ành
l ập bởi
ch í nh
,→phủNa Uy
l ưu vong
t ại
London đặt
t ên
,→
l à "Ti ểu Na Uy")
[MASKED]
Toronto ,
,→Ontario ,
Canada ,
và dùng
l àm máy bay
,→huấn
luy ện nâng
cao .
Sau này ,
[MASKED]
,→
được bán
[MASKED]
cho Mỹdưới
t ên P
,→
-36G.
Ground Truth:
Na Uy đặt mua 24
chi ếc Hawk 75A-6 s
gắn động
c
,→ơ Twin Wasp ,
trong
đó
19
chi ếc đã được
,→
giao
và 7
chi ếc đang
l ắp
r áp vào
l úc
,→Đức
xâm chi ếm Na Uy .
Chưa
có
chi ếc nào
,→
s ẵn
s àng để
chi ến đấu .
Những máy bay
,→chưa
l ắp
r áp b ị
vô
hi ệu bởi một
nhân
,→
vi ên hải
quan ,
khi
anh phá hủy
các
t h i
,→ết
b ị
và
cắt
đứt mọi
dây đ i ện
trong
t ầ
,→m tay .
Những
chi ếc Hawk Na Uy b ịĐức
,→
chi ếm được
l à một
phần của
l ô hàng
,→
giao
cho Phần Lan .
Sau này Na Uy cũng
,→đặt mua 36
chi ếc Hawk 75A-8 s
gắn động
,→cơ
Cyclone ,
đa
s ố
(30
chi ếc )
được
giao
,→
cho một
căn cứhuấn
luy ện Na Uy (được
,→
th ành
l ập bởi
ch í nh phủNa Uy
l ưu
,→vong
t ại
London đặt
t ên
l à "Ti ểu Na Uy
,→")
gần Toronto ,
Ontario ,
Canada ,
và dù
,→ng
l àm máy bay huấn
luy ện nâng
cao .
,→Sau này ,
chúng được bán
l ại
cho Mỹdướ
,→
i
t ên P-36G.
URA-LLaMa 7B:
Na Uy đặt mua 24
chi ếc Hawk 75A-6 s
gắn động
c
,→ơ Twin Wasp ,
trong
đó
19
chi ếc đã được
,→
giao
và 7
chi ếc đang
l ắp
r áp
l úc Đức
,→xâm chi ếm Na Uy .
Chưa
có
chi ếc nào
s ẵn
,→
s àng để
chi ến đấu .
Những máy bay
chưa
,→
l ắp
r áp b ị
hi ệu bởi một
nhân
vi ên hải
,→
quan ,
khi
anh phá hủy
các
t h i ết
b ị
và
,→
cắt
đứt mọi
dây đ i ện
trong
t ầm tay .
,→Những
chi ếc Hawk Na Uy b ịĐức
chi ếm đư
,→ợc
l à phần của
l ô hàng
giao
cho Phần
,→Lan .
Sau này Na Uy cũng đặt mua 36
chi
,→ếc Hawk 75A-8 s
gắn động
cơ
Allison ,
đa
,→
s ố
(30
chi ếc )
được
giao
cho một
căn c
,→ứhuấn
luy ện Na Uy (được
th ành
l ập bởi
,→
ch í nh phủNa Uy
l ưu vong
t ại
London đ
,→ặt
t ên
l à "Ti ểu Na Uy")
gần Toronto ,
,→Ontario ,
Canada ,
và dùng
l àm máy bay
,→huấn
luy ện nâng .
Sau này ,
chúng được b
,→án
l ại
cho Mỹdưới
t ên P-36G.
URA-LLaMa 13B:
Na Uy đặt mua 24
chi ếc Hawk 75A-6 s
gắn động
c
,→ơ Twin Wasp ,
trong
đó
19
chi ếc đã được
,→
giao
và 7
chi ếc đang
l ắp
r áp
khi Đức
,→xâm chi ếm Na Uy .
Chưa
có
chi ếc nào
s ẵn
,→
s àng để
chi ến đấu .
Những máy bay
chưa
,→
được
l ắp
r áp b ị
phá hủy bởi một
nhân
,→
vi ên hải
quan ,
khi
anh phá hủy
các
t h i
,→ết
b ị
và
cắt
đứt mọi
dây đ i ện
trong
t ầ
,→m tay .
Những
chi ếc Hawk Na Uy b ịĐức
,→
chi ếm được
l à một
phần của
l ô hàng
,→
giao
cho Phần Lan .
Sau này Na Uy cũng
,→đặt mua 36
chi ếc Hawk 75A-8 s
gắn động
,→cơ
A l l i s o n V-1710 ,
đa
s ố
(30
chi ếc )
đư
,→ợc
giao
cho một
căn cứhuấn
luy ện Na
,→Uy (được
th ành
l ập bởi
ch í nh phủNa Uy
,→
l ưu vong
t ại
London đặt
t ên
l à "Ti ểu
,→Na Uy")
gần Toronto ,
Ontario ,
Canada ,
,→và dùng
l àm máy bay huấn
luy ện nâng
,→cao .
Sau này ,
chúng được bán
l ại
cho M
,→ỹdưới
t ên P-36G.

--- Page 38 ---

URA-LLaMa 70B:
Na Uy đặt mua 24
chi ếc Hawk 75A-6 s
gắn động
c
,→ơ Twin Wasp ,
trong
đó
19
chi ếc đã được
,→
giao
và 7
chi ếc đang
l ắp
r áp vào
th á
,→ng 4 năm 1940
khi Đức
xâm chi ếm Na Uy .
,→
Chưa
có
chi ếc nào
s ẵn
s àng để
chi ến đ
,→ấu .
Những máy bay
bay
chưa
l ắp
r áp b ị
,→vô
hi ệu hoàn
to àn bởi một
nhân
vi ên hả
,→
i
quan ,
khi
anh
ta
phá hủy
các
t h i ết
b
,→
ị
và đứt mọi
dây đ i ện
trong
t ầm tay .
,→Những
chi ếc Hawk Na Uy b ịĐức
chi ếm đư
,→ợc
l à một
phần của
l ô hàng
giao
cho Ph
,→ần Lan .
Sau này Na Uy cũng đặt mua 36
,→
chi ếc Hawk 75A-8 s
động
cơ
Cyclone ,
đa
,→s ố
(30
chi ếc )
được
giao
cho một
căn cứ
,→
huấn
luy ện Na Uy (được
th ành
l ập bởi
,→ch í nh phủNa Uy
l ưu vong
t ại
London đặ
,→
t
t ên
l à " L i t t l e
Norway ")
ở
Toronto ,
,→Ontario ,
Canada ,
và dùng
l àm máy bay
,→huấn
luy ện nâng
cao .
Sau này ,
chúng đư
,→ợc bán cho Mỹdưới
t ên P-36G
LLaMa-2 7B:
Na Uy purchased
24 Hawk 75A-6 s
a i r c r a f t
,→powered
by Twin Wasp engines ,
of
which
,→
19
were
d e l i v e r e d
and 7
were
under
,→assembly
when Germany
invaded
Norway .
,→None
of
the
unassembled
a i r c r a f t
were
,→ready
f o r
combat .
An employee
of
the
,→customs
o f f i c e
destroyed
the
c o n t r o l
,→
c a b l e s
and
e l e c t r i c a l
systems
of
the
,→unassembled
a i r c r a f t ,
and
the
,→Norwegian Hawks were
taken
over
by
,→Germany .
Later ,
Norway
a l s o
ordered
36
,→
Hawk 75A-8 s
a i r c r a f t
with Wasp
,→
engines ,
of
which
30
were
d e l i v e r e d
to
,→
a
t r a i n i n g
base
e s t a b l i s h e d
by
the
,→Norwegian
government - in - e x i l e
near
,→Toronto ,
Ontario ,
Canada ,
and
used
f o r
,→
p i l o t
t r a i n i n g .
Afterward ,
they
were
,→
s o l d
to
the
United
States
under
the
,→
d e s i g n a t i o n
P-36G.
LLaMa-2 13B:
Based
on
the
information
provided ,
here
i s
a
,→summary
of
the
main
points :
* Norway
,→purchased
24 Hawk 75A-6
a i r c r a f t
with
,→Twin Wasp
engines
from
the
United
,→
St at es
in
1939.
* Of
these ,
19
were
,→
d e l i v e r e d
b e f o r e
the
outbreak
of
World
,→
War II ,
while
7
were
s t i l l
under
,→
c o n s t r u c t i o n
and
not
yet
ready
f o r
,→combat .
* The Hawk
a i r c r a f t
were
used
,→by
the
Norwegian
Air
Force
during
the
,→war ,
but
were
e v e n t u a l l y
captured
by
,→the
Germans when
they
invaded
Norway
,→
in
1940.
* Some
of
the
captured Hawk
,→
a i r c r a f t
were
used
by
the
German
a i r
,→
force ,
while
others
were
sent
to
,→
Finland
as
part
of
a
trade
agreement .
,→*
After
the
war ,
Norway
purchased
36
,→Hawk 75A-8
a i r c r a f t
with
Cyclone
,→
engines
from
the
United
States ,
which
,→were
used
f o r
t r a i n i n g
purposes
at
a
,→base
in
Toronto ,
Ontario ,
Canada .
*
,→Later ,
some
of
these
a i r c r a f t
were
,→
s o l d
to
the
United
States
under
the
,→
d e s i g n a t i o n
P-36G.
LLaMa-2 70B:
Sure ,
here ' s
a
r e w r i t t e n
v e r s i o n
of
the
text
,→with
more
appropriate
vocabulary
and
,→grammar :
"Norway
has
ordered
24 Hawk
,→75A-6
a i r c r a f t
equipped
with
Twin Wasp
,→
engines ,
of
which
19
have
been
,→
d e l i v e r e d
and 7
are
c u r r e n t l y
being
,→assembled
in
[MASKED]
f o r
the
i n v a s i o n
,→
of
Norway .
None
of
the
a i r c r a f t
are
,→ready
f o r
combat
yet .
The
remaining
,→
seven
a i r c r a f t
are
s t i l l
being
,→manufactured
and
are
expected
to
be
,→completed
soon .
The Norwegian
Air
,→Force
has
a l s o
purchased
36 Hawk 75A-8
,→
a i r c r a f t
equipped
with
Cyclone
,→
engines ,
most
of
which
(30
a i r c r a f t )
,→
w i l l
be
d e l i v e r e d
to
a
Norwegian
,→
t r a i n i n g
base
in
[MASKED]
Toronto ,
,→Ontario ,
Canada ,
and
used
f o r
advanced
,→
f l i g h t
t r a i n i n g .
Later ,
some
of
these
,→
a i r c r a f t
were
s o l d
to
the US under
,→the
d e s i g n a t i o n
P-36G. "
I
hope
t h i s
,→
helps !
Let me know
i f
you
have
any
,→
f u r t h e r
q u e s t i o n s
or
need
any
,→
a d d i t i o n a l
a s s i s t a n c e .
Vietcuna-7B-v3:
Khách :
"Một
con
t àu chởdầu b ị
ch ìm ngoà i
khơ
,→
i
bờ
bi ển Mexico
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
Vistral:
24
chi ếc Hawk 75A-6 s
gắn động
cơ Twin Wasp đư
,→ợc đặt mua bởi
Na Uy .
Trong
s ốđó ,
19
,→
chi ếc đã được
giao
và 7
chi ếc
vẫn còn
,→đang
l ắp
r áp .
Những
chi ếc máy bay
chưa
,→
l ắp
r áp b ị
vô
hi ệu hóa bởi một
nhân
,→
vi ên hải
quan ,
khi
anh
ta
phá hủy
các
,→
t h i ết
b ị
và
cắt
đứt mọi
nguồn đ i ện
,→
trong
t ầm tay .
Những
chi ếc Hawk Na Uy
,→b ịĐức
chi ếm được
l à một
phần của
l ô h
,→àng
giao
cho Phần Lan .
Na Uy cũng đặt
,→mua 36
chi ếc Hawk 75A-8 s
gắn động
cơ
,→Cyclone ,
đa
s ố
(30
chi ếc )
được
giao
,→cho một
căn cứhuấn
luy ện Na Uy ở
,→Toronto ,
Ontario ,
Canada .
Chúng
chủyế
,→u được
sửdụng
l àm máy bay huấn
luy ện
,→nâng
cao .
Sau này ,
chúng được bán cho
,→Hoa Kỳdưới
t ên gọi
P-36G.
MixSUra:
ỞNa Uy,
đã đặt mua 24
chi ếc Hawk 75A-6 s
gắn
,→động
cơ Twin Wasp ,
trong
đó
19
chi ếc đ
,→ã được
giao
và 7
chi ếc đang
l ắp
r áp và
,→o
th áng
1940
xâm chi ếm Na Uy .
Chưa
có
,→
chi ếc nào
s ẵn
s àng để
chi ến đấu .
Những
,→
chi ếc Hawk Na Uy b ịĐức
chi ếm được
l à
,→
một
phần của
l ô hàng
giao
cho Phần
,→Lan .
Sau này Na Uy cũng đặt mua 36
chi
,→ếc Hawk 75A-8 s
gắn động
cơ
Cyclone ,
đa
,→
s ố
(30
chi ếc )
được
giao
cho một
căn c
,→ứhuấn
luy ện Na Uy (được
th ành
l ập bởi
,→
ch í nh phủNa Uy
l ưu vong
t ại
London đ

--- Page 39 ---

,→ặt
t ên
l à "Ti ểu Na Uy")
và dùng
l àm má
,→y bay huấn
luy ện nâng
cao .
Sau này ,
12
,→
chi ếc được bán cho Mỹdưới
t ên P-36G.
GemSUra 7B:
<b>Câu gốc</b> "The Hawker
Hurricane Mk I
was
,→
a
B r i t i s h
s i n g l e
s e a t
f i g h t e r
,→
a i r c r a f t
designed
by
the
firm
of
Henry
,→
T.
Folland
Ltd
and
manufactured
in
,→
l a r g e
numbers
during
World War
I I
f o r
,→both
c i v i l i a n
use
as
w e l l
m i l i t a r y
,→
s e r v i c e
with
various
a i r
f o r c e s
around
,→
world
i n c l u d i n g
A u s t r a l i a
New Zealand
,→
South
A f ri c a
United
Kingdom
France
,→
Netherlands
Belgium
Norway Sweden
,→Denmark
Czechoslovakia
Iraq
Iran
,→
Afghanistan
Turkey
Syria
Jordan
North
,→Korea Cuba Mexico Panama
B r a z i l
,→
Argentina
Peru
B o l i v i a
Ecuador
,→Paraguay
Uruguay
Chile
Colombia
,→Venezuela
H a i t i
Dominican
Republic
,→Costa
Rica
Nicaragua
Guatemala
,→Honduras
El
Salvador
B e l i z e
Jamaica
,→
Trinidad & Tobago
Barbados
St
Vincent
,→
Saint
Lucia
Grenada
Dominica
Antigua
,→Barbuda
Montserrat
Saba
Anguilla
Sint
,→
Eustatius
Curacao
Aruba
Bonaire
,→
Martinique
Guadeloupe
French
Guiana
,→Suriname
Guyana Surinam
Indonesia
,→Malaysia
Singapore
Thailand
,→
P h i l i p p i n e s
Laos
Cambodia Vietnam
,→China
Taiwan Myanmar Bangladesh
Nepal
,→Bhutan
S r i
Lanka
Maldives
S e y c h e l l e s
,→
Mauritius
Madagascar
Tanzania
Kenya
,→
Ethiopia
Somalia
Djibouti
E r i t r e a
,→Sudan
Libya
Tunisia
Algeria
Morocco
,→
Mauritania
Mali
Senegal
Gambia The
,→Bahamas Turks And Caicos
I s l a n d s
,→Cayman
I s l a n d
Bermuda
G i b r a l t a r
Malta
,→Cyprus
I s r a e l
P a l e s t i n e
Egypt
Saudi
,→Arabia Oman Yemen Bahrain
Kuwait
Qatar
,→
UAE Lebanon
Syrian
Arab
S o c i a l i s t
,→
Republics
East
Timor Papua
Niugini
,→Solomon
I s l n a d
Vanuatu Tonga
Tuvalu
,→Niue
P i t c a i r n
I s l e
Cook
i s l a n d s
Samoa
,→
F i j i
K i r i b a t i
Nauru
Palau
Micronesia
,→
M a r s h a l l I s l a n d s Guam Saipan
,→
Marianaislands
Northern
Marianas
,→
B o u g a i n v i l l e
Buka
Guadalcanal
Malaita
,→Makira
Ulawa
Santa
I s a b e l
Choiseul
San
,→
C r i s t o b a l
Kolombangara
Rennell
,→
Bellona
Temotu
Henderson
Field
Gemini Pro:
Na Uy đặt mua 24
chi ếc Hawk 75A-6 s
gắn động
c
,→ơ Twin Wasp ,
trong
đó
19
chi ếc đã được
,→
giao
và 7
chi ếc đang
l ắp
r áp vào
hai
,→
t àu đổbộnhằm xâm chi ếm Na Uy .
Chưa
c
,→ó
chi ếc nào
s ẵn
s àng để
chi ến đấu .
Nhữ
,→ng máy bay
chưa
l ắp
r áp b ị
vô
hi ệu hóa
,→
bởi một
nhân
vi ên hải
quan ,
khi
anh
,→phá hủy
các
t h i ết
b ị
và
cắt
đứt mọi
dâ
,→y đ i ện
trong
t ầm tay .
Những
chi ếc Hawk
,→
Na Uy b ịĐức
chi ếm được
l à một
phần c
,→ủa
l ô hàng
giao
cho Phần Lan .
Sau này
,→Na Uy cũng đặt mua 36
chi ếc Hawk 75A-8
,→s
gắn động
cơ
Cyclone ,
đa
s ố
(30
chi ếc
,→
)
được
giao
cho một
căn cứhuấn
luy ện
,→Na Uy (được
th ành
l ập bởi
ch í nh phủNa
,→
Uy
l ưu vong
t ại
London đặt
t ên
l à "Ti
,→ểu Na Uy")
ở
Toronto ,
Ontario ,
Canada ,
,→
và dùng
l àm máy bay huấn
luy ện nâng
,→cao .
Sau này ,
chúng được bán
l ại
cho M
,→ỹdưới
t ên P-36G.
GPT-3.5:
Na Uy đặt mua 24
chi ếc Hawk 75A-6 s
gắn động
c
,→ơ Twin Wasp ,
trong
đó
19
chi ếc đã được
,→
giao
và 7
chi ếc đang
l ắp
r áp vào
kho
,→để
chống
l ại
xâm chi ếm Na Uy .
Chưa
có
,→
chi ếc nào
s ẵn
s àng để
chi ến đấu .
Những
,→
máy bay
bay
chưa
l ắp
r áp b ị
vô
hi ệu h
,→óa bởi một
nhân
vi ên hải
quan ,
khi
anh
,→
ta
phá hủy
các
t h i ết
b ị
và
cắt
đứt mọ
,→
i
dây đ i ện
trong
t ầm tay .
Những
chi ếc
,→Hawk Na Uy b ịĐức
chi ếm được
l à một
ph
,→ần của
l ô hàng
giao
cho Phần Lan .
Sau
,→này Na Uy cũng đặt mua 36
chi ếc Hawk
,→75A-8 s
có động
cơ
Cyclone ,
đa
s ố
(30
,→
chi ếc )
được
giao
cho một
căn cứhuấn
,→
luy ện Na Uy (được
th ành
l ập bởi
ch í nh
,→phủNa Uylưu vong
t ại
Londonđặt
t ên
l à
,→
"Ti ểuNaUyl ") trong
Toronto ,
Ontario ,
,→Canadavà dùng
l àm máy bay huấn
luy ện n
,→âng
cao .
Sau này , các máycấy đã được bá
,→ncho Mỹdưới
t ên P-36G.
GPT-4:
Na Uy đặt mua 24
chi ếc Hawk 75A-6 s
gắn động
c
,→ơ Twin Wasp ,
trong
đó
19
chi ếc đã được
,→
giao
và 7
chi ếc đang
l ắp
r áp vào
th ời
,→
đ i ểm xâm chi ếm Na Uy .
Chưa
có
chi ếc n
,→ào
s ẵn
s àng để
chi ến đấu .
Những máy
,→bay
chưa
l ắp
r áp b ị
vô
hi ệu hóa bởi mộ
,→
t
nhân
vi ên hải
quan ,
khi
anh phá hủy
,→các
t h i ết
b ị
và
cắt
đứt mọi
dây đ i ện
,→
trong
t ầm tay .
Những
chi ếc Hawk Na Uy
,→b ịĐức
chi ếm được
l à một
phần của
l ô h
,→àng
giao
cho Phần Lan .
Sau này Na Uy c
,→ũng đặt mua 36
chi ếc Hawk 75A-8 s
gắn đ
,→ộng
cơ
Cyclone ,
đa
s ố
(30
chi ếc )
được
,→
giao
cho một
căn cứhuấn
luy ện Na Uy (
,→được
th ành
l ập bởi
ch í nh phủNa Uy
l ưu
,→
vong
t ại
London đặt
t ên
l à "Ti ểu Na
,→Uy")
t ại
Toronto ,
Ontario ,
Canada ,
và
,→dùng
l àm máy bay huấn
luy ện nâng
cao .
,→Sau này ,
chúng được bán
l ại
cho Mỹdướ
,→
i
t ên P-36G.
Context:
Norway
ordered
24 Hawk 75A-6 s
with
Twin Wasp
,→
engines ,
of
which
19
have
been
,→
d e l i v e r e d ,
and 7
are
c u r r e n t l y
being
,→assembled
in
[MASKED]
[MASKED]
f o r
the
,→
i n v a s i o n
of
Norway .
None
of
the
,→
a i r c r a f t
are
ready
f o r
[MASKED] .
The
,→unassembled
[MASKED]
were
rendered
,→
i n o p e r a b l e
[MASKED]
a
customs
o f f i c i a l
,→
who
destroyed
equipment
and
[MASKED]
,→
o f f
a l l
[MASKED]
within
reach .
The
,→Hawks
intended
f o r
Norway
that
were
,→
captured
by Germany
were
part
of
a
,→shipment
intended
f o r
Finland .
Later ,
,→Norway
a l s o
ordered
36 Hawk 75A-8 s
[
,→MASKED]
Cyclone
engines ,
with
the
,→
majority
(30
a i r c r a f t )
d e l i v e r e d
to
a
,→Norwegian
t r a i n i n g
base
( e s t a b l i s h e d
,→by
the
Norwegian
government
in
e x i l e
,→
in
London and named " L i t t l e
Norway ")
[
,→MASKED]
Toronto ,
Ontario ,
Canada ,
and
,→used
as
advanced
t r a i n i n g
a i r c r a f t .
,→Subsequently ,
[MASKED]
were
s o l d
[
,→MASKED]
the
United
St at es
under
the
,→
d e s i g n a t i o n
P-36G.
Ground Truth:
Norway
ordered
24 Hawk 75A-6 s
with
Twin Wasp
,→
engines ,
of
which
19
have
been
,→
d e l i v e r e d ,
and 7
are
c u r r e n t l y
being
,→assembled
in
German
f o r
the
i n v a s i o n
,→
of
Norway .
None
of
the
a i r c r a f t
are
,→ready
f o r
combat .
The
unassembled
,→
a i r c r a f t s
were
rendered
i n o p e r a b l e
by
,→a
customs
o f f i c i a l
who
destroyed
,→equipment
and
cut
o f f
a l l
wires
within
,→
reach .
The Hawks
intended
f o r
Norway
,→
that
were
captured
by Germany
were
,→
part
of
a
shipment
intended
f o r
,→
Finland .
Later ,
Norway
a l s o
ordered
36

--- Page 40 ---

,→
Hawk 75A-8 s
equiped
Cyclone
engines ,
,→with
the
majority
(30
a i r c r a f t )
,→
d e l i v e r e d
to
a
Norwegian
t r a i n i n g
base
,→
( e s t a b l i s h e d
by
the
Norwegian
,→government
in
e x i l e
in
London and
,→named " L i t t l e
Norway ")
near
Toronto ,
,→Ontario ,
Canada ,
and
used
as
advanced
,→
t r a i n i n g
a i r c r a f t .
Subsequently ,
they
,→were
s o l d
to
the
United
States
under
,→the
d e s i g n a t i o n
P-36G.
URA-LLaMa 7B:
Norway
ordered
24 Hawk 75A-6 s
with
Twin Wasp
,→
engines ,
of
which
19
were
d e l i v e r e d
,→and 7
were
being
assembled
when
,→Germany
invaded
Norway .
None
of
the
,→
planes
were
ready
f o r
combat .
The
,→unassembled
planes
were
sabotaged
by a
,→
customs
o f f i c e r ,
who
destroyed
,→equipment
and
cut
a l l
a c c e s s i b l e
wires
,→
.
The Hawks
of
Norway
captured
by
,→Germany
were
part
of
a
shipment
,→
intended
f o r
Finland .
Later ,
Norway
,→
a l s o
ordered
36 Hawk 75A-8 s
with
,→
A l l i s o n
engines ,
with
the
majority
(30
,→
planes )
d e l i v e r e d
to
a
Norwegian
,→
t r a i n i n g
base
( e s t a b l i s h e d
by
the
,→Norwegian
government
in
e x i l e
in
,→London ,
named " L i t t l e
Norway ")
near
,→Toronto ,
Ontario ,
Canada ,
and
used
f o r
,→
advanced
t r a i n i n g
a i r c r a f t .
,→
Eventually ,
they
were
s o l d
to
the
,→United
States
under
the
d e s i g n a t i o n
P
,→
-36G.
URA-LLaMa 13B:
Norway
ordered
24 Hawk 75A-6 s
equipped
with
,→Twin Wasp engines ,
of
which
19
were
,→
d e l i v e r e d ,
and 7
were
in
assembly
when
,→
Germany
invaded
Norway .
None
of
the
,→
a i r c r a f t
were
ready
f o r
combat .
The
,→unassembled
planes
were
destroyed
by a
,→
customs
o f f i c e r
who
sabotaged
the
,→equipment
and
cut
a l l
a c c e s s i b l e
wires
,→
.
The Hawks
captured
by Germany
were
,→
part
of
a
shipment
intended
f o r
,→
Finland .
Later ,
Norway
a l s o
ordered
36
,→
Hawk 75A-8 s
with
A l l i s o n V-1710
,→
engines ,
and
the
majority
(30
a i r c r a f t
,→
)
were
d e l i v e r e d
to
a
Norwegian
,→
t r a i n i n g
base
( e s t a b l i s h e d
by
the
,→Norwegian
government
in
e x i l e
in
,→London and known
as
" L i t t l e
Norway ")
,→near
Toronto ,
Ontario ,
Canada ,
f o r
,→advanced
t r a i n i n g .
Later ,
they
were
,→
s o l d
back
to
the
United
States
under
,→the
d e s i g n a t i o n
P-36G.
URA-LLaMa 70B:
Norway
ordered
24 Hawk 75A-6 s
with
Twin Wasp
,→
engines ,
of
which
19
were
d e l i v e r e d ,
,→and 7
were
in
assembly
in
April
1940
,→when Germany
invaded
Norway .
None
of
,→the
a i r c r a f t
were
ready
f o r
combat .
,→The
unassembled
planes
were
completely
,→
rendered
i n e f f e c t i v e
by a
customs
,→
o f f i c e r ,
who
sabotaged
the
equipment
,→and
cut
a l l
a c c e s s i b l e
wires .
The
,→Hawks
captured
by Germany
were
part
of
,→
a
shipment
intended
f o r
Finland .
,→Later ,
Norway
a l s o
ordered
36 Hawk 75A
,→
-8 s
with
Cyclone
engines ,
and
the
,→
majority
(30
a i r c r a f t )
were
d e l i v e r e d
,→to
a
Norwegian
t r a i n i n g
base
(
,→
e s t a b l i s h e d
by
the
Norwegian
,→government
in
e x i l e
in
London and
,→known
as
" L i t t l e
Norway ")
in
Toronto ,
,→Ontario ,
Canada ,
f o r
advanced
t r a i n i n g
,→
.
Later ,
they
were
s o l d
to
the
United
,→
Stat es
under
the
d e s i g n a t i o n
P-36G.
LLaMa-2 7B:
Na Uy purchased
24 Hawk 75A-6 s
a i r c r a f t
,→powered
by Twin Wasp engines ,
of
which
,→
19
were
d e l i v e r e d
and 7
were
under
,→assembly
when Germany
invaded
Norway .
,→None
of
the
unassembled
a i r c r a f t
were
,→ready
f o r
combat .
An employee
of
the
,→customs
o f f i c e
destroyed
the
c o n t r o l
,→
c a b l e s
and
e l e c t r i c a l
systems
of
the
,→unassembled
a i r c r a f t ,
and
the
,→Norwegian Hawks were
taken
over
by
,→Germany .
Later ,
Norway
a l s o
ordered
36
,→
Hawk 75A-8 s
a i r c r a f t
with Wasp
,→
engines ,
of
which
30
were
d e l i v e r e d
to
,→
a
t r a i n i n g
base
e s t a b l i s h e d
by
the
,→Norwegian
government - in - e x i l e
near
,→Toronto ,
Ontario ,
Canada ,
and
used
f o r
,→
p i l o t
t r a i n i n g .
Afterward ,
they
were
,→
s o l d
to
the
United
St at es
under
the
,→
d e s i g n a t i o n
P-36G.
LLaMa-2 13B:
Based
on
the
information
provided ,
here
i s
a
,→summary
of
the
main
p oi nt s :
* Norway
,→purchased
24 Hawk 75A-6
a i r c r a f t
with
,→Twin Wasp
engines
from
the
United
,→
St at es
in
1939.
* Of
these ,
19
were
,→
d e l i v e r e d
b e f o r e
the
outbreak
of
World
,→
War II ,
while
7
were
s t i l l
under
,→
c o n s t r u c t i o n
and
not
yet
ready
f o r
,→combat .
* The Hawk
a i r c r a f t
were
used
,→by
the
Norwegian
Air
Force
during
the
,→war ,
but
were
e v e n t u a l l y
captured
by
,→the
Germans when
they
invaded
Norway
,→
in
1940.
* Some
of
the
captured Hawk
,→
a i r c r a f t
were
used
by
the
German
a i r
,→
force ,
while
o th er s
were
sent
to
,→
Finland
as
part
of
a
trade
agreement .
,→*
After
the
war ,
Norway
purchased
36
,→Hawk 75A-8
a i r c r a f t
with
Cyclone
,→
engines
from
the
United
States ,
which
,→were
used
f o r
t r a i n i n g
purposes
at
a
,→base
in
Toronto ,
Ontario ,
Canada .
*
,→Later ,
some
of
these
a i r c r a f t
were
,→
s o l d
to
the
United
St at es
under
the
,→
d e s i g n a t i o n
P-36G.
LLaMa-2 70B:
Sure ,
here ' s
a
r e w r i t t e n
v e r s i o n
of
the
text
,→with
more
appropriate
vocabulary
and
,→grammar :
"Norway
has
ordered
24 Hawk
,→75A-6
a i r c r a f t
equipped
with
Twin Wasp
,→
engines ,
of
which
19
have
been
,→
d e l i v e r e d
and 7
are
c u r r e n t l y
being
,→assembled
in
[MASKED]
f o r
the
i n v a s i o n
,→
of
Norway .
None
of
the
a i r c r a f t
are
,→ready
f o r
combat
yet .
The
remaining
,→
seven
a i r c r a f t
are
s t i l l
being
,→manufactured
and
are
expected
to
be
,→completed
soon .
The Norwegian
Air
,→Force
has
a l s o
purchased
36 Hawk 75A-8
,→
a i r c r a f t
equipped
with
Cyclone
,→
engines ,
most
of
which
(30
a i r c r a f t )
,→
w i l l
be
d e l i v e r e d
to
a
Norwegian
,→
t r a i n i n g
base
in
[MASKED]
Toronto ,
,→Ontario ,
Canada ,
and
used
f o r
advanced
,→
f l i g h t
t r a i n i n g .
Later ,
some
of
these
,→
a i r c r a f t
were
s o l d
to
the US under
,→the
d e s i g n a t i o n
P-36G. "
I
hope
t h i s
,→
helps !
Let me know
i f
you
have
any
,→
f u r t h e r
q u e s t i o n s
or
need
any
,→
a d d i t i o n a l
a s s i s t a n c e .
Vietcuna-7B-v3:
Guest : A
o i l
tanker
has
sunk
o f f
the
coast
of
,→
Mexico
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[

--- Page 41 ---

,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
[MASKED]
[MASKED]
[
,→MASKED]
[MASKED]
Vistral:
24 Hawk 75A-6 s
with
Twin Wasp
engines
were
,→
ordered
by Norway .
Of
those ,
19
have
,→been
d e l i v e r e d
and 7
are
s t i l l
under
,→assembly .
The
unassembled
planes
were
,→
d i s a b l e d
by a
customs
o f f i c e r ,
who
,→
destroyed
the
equipment
and
cut
o f f
,→
a l l
power
within
reach .
Norwegian
,→Hawks
captured
by Germany
were
part
of
,→
a
shipment
to
Finland .
Norway
a l s o
,→
ordered
36 Hawk 75A-8 s
equipped
with
,→Cyclone
engines ,
the
majority
(30
,→
a i r c r a f t )
were
d e l i v e r e d
to
a
,→Norwegian
t r a i n i n g
base
in
Toronto ,
,→Ontario ,
Canada .
They
are
mainly
used
,→as
advanced
t r a i n i n g
a i r c r a f t .
They
,→were
l a t e r
s o l d
to
the
United
St at es
,→under
the
d e s i g n a t i o n
P-36G.
MixSUra:
In
Norway ,
24 Twin Wasp- powered Hawk 75A-6 s
,→were
ordered ,
of
which
19
had
been
,→
d e l i v e r e d
and 7
were
being
assembled
,→by
the
October
1940
i n v a s i o n
of
Norway
,→
.
None
of
them
are
ready
to
f i g h t
yet .
,→
Norwegian Hawks
captured
by Germany
,→were
part
of
a
shipment
to
Finland .
,→Later ,
Norway
a l s o
ordered
36 Hawk 75A
,→
-8 s
equipped
with
Cyclone
engines ,
the
,→
majority
(30
a i r c r a f t )
were
assigned
,→to
a
Norwegian
t r a i n i n g
base
(
,→
e s t a b l i s h e d
by
the
Norwegian
,→government
in
e x i l e
in
London named "
,→
L i t t l e
Norway ")
and
used
as
an
,→advanced
t r a i n i n g
a i r c r a f t .
Later ,
12
,→were
s o l d
to
the US under
the
name P
,→
-36G.
GemSUra 7B:
<b>O r i g i n a l
sentence </b> "The Hawker
,→
Hurricane Mk I
was a
B r i t i s h
s i n g l e
,→
s e a t
f i g h t e r
a i r c r a f t
designed
by
the
,→
firm
of
Henry T.
Folland
Ltd
and
,→manufactured
in
l a r g e
numbers
during
,→World War
I I
f o r
both
c i v i l i a n
use
as
,→
w e l l
m i l i t a r y
s e r v i c e
with
various
a i r
,→
f o r c e s
around
the
world
i n c l u d i n g
,→
A u s t r a l i a
New Zealand
South
A f ri c a
,→United
Kingdom
France
Netherlands
,→Belgium
Norway Sweden Denmark
,→
Czechoslovakia
Iraq
Iran
Afghanistan
,→Turkey
Syria
Jordan
North
Korea Cuba
,→Mexico Panama
B r a z i l
Argentina
Peru
,→
B o l i v i a
Ecuador
Paraguay
Uruguay
Chile
,→
Colombia
Venezuela
H a i t i
Dominican
,→
Republic
Costa
Rica
Nicaragua
,→Guatemala
Honduras
El
Salvador
B e l i z e
,→Jamaica
Trinidad & Tobago
Barbados
St
,→Vincent
Saint
Lucia
Grenada
Dominica
,→Antigua
Barbuda
Montserrat
Saba
,→
Anguilla
Sint
Eustatius
Curacao
Aruba
,→
Bonaire
Martinique
Guadeloupe
French
,→Guiana
Suriname
Guyana Surinam
,→
Indonesia
Malaysia
Singapore
Thailand
,→
P h i l i p p i n e s
Laos
Cambodia Vietnam
,→China
Taiwan Myanmar Bangladesh
Nepal
,→Bhutan
S r i
Lanka
Maldives
S e y c h e l l e s
,→
Mauritius
Madagascar
Tanzania
Kenya
,→
Ethiopia
Somalia
Djibouti
E r i t r e a
,→Sudan
Libya
Tunisia
A l g e r i a
Morocco
,→
Mauritania
Mali
Senegal
Gambia The
,→Bahamas Turks And Caicos
I s l a n d s
,→Cayman
I s l a n d
Bermuda
G i b r a l t a r
Malta
,→Cyprus
I s r a e l
P a l e s t i n e
Egypt
Saudi
,→Arabia Oman Yemen Bahrain
Kuwait
Qatar
,→
UAE Lebanon
Syrian
Arab
S o c i a l i s t
,→
Republics
East
Timor Papua
Niugini
,→Solomon
I s l n a d
Vanuatu Tonga
Tuvalu
,→Niue
P i t c a i r n
I s l e
Cook
i s l a n d s
Samoa
,→
F i j i
K i r i b a t i
Nauru
Palau
Micronesia
,→
M a r s h a l l I s l a n d s Guam Saipan
,→
Marianaislands
Northern
Marianas
,→
B o u g a i n v i l l e
Buka
Guadalcanal
Malaita
,→Makira
Ulawa
Santa
I s a b e l
Choiseul
San
,→
C r i s t o b a l
Kolombangara
Rennell
,→
Bellona
Temotu
Henderson
Field
Gemini Pro:
Norway
ordered
24 Hawk 75A-6 s
with
Twin Wasp
,→
engines ,
of
which
19
have
been
,→
d e l i v e r e d
and 7
are
being
assembled
,→
i n t o
two
landing
s h i p s
to
invade
,→Norway .
None
of
them
are
ready
to
,→
f i g h t
yet .
The
unassembled
a i r c r a f t
,→were
d i s a b l e d
by a
customs
o f f i c e r ,
,→who
destroyed
the
equipment
and
,→
severed
a l l
e l e c t r i c a l
wires
within
,→
reach .
Norwegian Hawks
captured
by
,→Germany
were
part
of
a
shipment
to
,→
Finland .
Later ,
Norway
a l s o
ordered
36
,→
Hawk 75A-8 s
equipped
with
Cyclone
,→
engines ,
the
majority
(30
a i r c r a f t )
,→were
assigned
to
a
Norwegian
t r a i n i n g
,→base
( e s t a b l i s h e d
by
the
Norwegian
,→government
in
e x i l e
in
London named "
,→
L i t t l e
Norway ")
in
Toronto ,
Ontario ,
,→Canada ,
and
used
as
an
advanced
,→
t r a i n e r .
Later ,
they
were
s o l d
to
the
,→US under
the
name P-36G.
GPT-3.5:
Norway
ordered
24 Hawk 75A-6 s
with
Twin Wasp
,→
engines ,
of
which
19
were
d e l i v e r e d ,
,→and 7
were
in
assembly
in
s t o r a g e
to
,→
r e s i s t
the
i n v a s i o n
of
Norway .
None
of
,→
the
a i r c r a f t
were
ready
f o r
combat .
,→The
unassembled
planes
were
rendered
,→
i n e f f e c t i v e
by a
customs
o f f i c e r ,
who
,→
sabotaged
the
equipment
and
cut
a l l
,→
a c c e s s i b l e
wires .
The Hawks
captured
,→by Germany
were
part
of
a
shipment
,→
intended
f o r
Finland .
Later ,
Norway
,→
a l s o
ordered
36 Hawk 75A-8 s
with
,→Cyclone
engines ,
and
the
majority
(30
,→
a i r c r a f t )
were
d e l i v e r e d
to
a
,→Norwegian
t r a i n i n g
base
( e s t a b l i s h e d
,→by
the
Norwegian
government
in
e x i l e
,→
in
London and known
as
" L i t t l e
Norway
,→
")
in
Toronto ,
Ontario ,
Canada ,
f o r
,→advanced
t r a i n i n g .
Later ,
these
,→
a i r c r a f t
were
s o l d
to
the
United
,→
St at es
under
the
d e s i g n a t i o n
P-36G.
GPT-4:
Norway
ordered
24 Hawk 75A-6 s
with
Twin Wasp
,→
engines ,
of
which
19
were
d e l i v e r e d ,
,→and 7
were
in
assembly
at
the
time
of
,→the
i n v a s i o n
of
Norway .
None
of
the
,→
a i r c r a f t
were
ready
f o r
combat .
The
,→unassembled
planes
were
rendered
,→
i n e f f e c t i v e
by a
customs
o f f i c e r ,
who
,→
sabotaged
the
equipment
and
cut
a l l
,→
a c c e s s i b l e
wires .
The Hawks
captured
,→by Germany
were
part
of
a
shipment
,→
intended
f o r
Finland .
Later ,
Norway
,→
a l s o
ordered
36 Hawk 75A-8 s
with
,→Cyclone
engines ,
and
the
majority
(30
,→
a i r c r a f t )
were
d e l i v e r e d
to
a
,→Norwegian
t r a i n i n g
base
( e s t a b l i s h e d
,→by
the
Norwegian
government
in
e x i l e
,→
in
London and known
as
" L i t t l e
Norway
,→
")
in
Toronto ,
Ontario ,
Canada ,
f o r

--- Page 42 ---

,→advanced
t r a i n i n g .
Later ,
these
,→
a i r c r a f t
were
s o l d
back
to
the
United
,→
St at es
under
the
d e s i g n a t i o n
P-36G.
H.7.2
VSEC
Context:
Thông
qua
công
t ác
tuy ên
truy ền ,
vận động này
,→
phụhuynh
s ẽ
hi ểu
r õ hơn
t ầm quan
t r ọ
,→ng
của
vi ệc
g i áo dục
ý
thức bảo vệmô i
,→
t r ường
cho
t r ẻ
không phải
ch ỉ
ởph í a
,→nhà
t r ường mà
còn ở
gia
đ ì nh
,
góp phầ
,→n vào
vi ệc
g ì n
g i ữmô i
t r ường {sanh } ,
,→s ạch
,
đẹp .
Ground Truth:
Thông
qua
công
t ác
tuy ên
truy ền ,
vận động này
,→
phụhuynh
s ẽ
hi ểu
r õ hơn
t ầm quan
t r ọ
,→ng
của
vi ệc
g i áo dục
ý
thức bảo vệmô i
,→
t r ường
cho
t r ẻ
không phải
ch ỉ
ởph í a
,→nhà
t r ường mà
còn ở
gia
đ ì nh
,
góp phầ
,→n vào
vi ệc
g ì n
g i ữmô i
t r ường xanh ,
s ạ
,→ch ,
đẹp .
URA-LLaMa 7B:
Thông
qua
công
t ác
tuy ên
truy ền ,
vận động này
,→
phụhuynh
s ẽ
hi ểu
r õ hơn
t ầm quan
t r ọ
,→ng
của
vi ệc
g i áo dục
ý
thức bảo vệmô i
,→
t r ường
cho
t r ẻ
không phải
ch ỉ
ởph í a
,→nhà
t r ường mà
còn ở
gia
đ ì nh
,
góp phầ
,→n vào
vi ệc
g ì n
g i ữmô i
t r ường
sanh
,
s
,→ạch
,
đẹp .
URA-LLaMa 13B:
Thông
qua
công
t ác
tuy ên
truy ền ,
vận động này
,→
phụhuynh
s ẽ
hi ểu
r õ hơn
t ầm quan
t r ọ
,→ng
của
vi ệc
g i áo dục
ý
thức bảo vệmô i
,→
t r ường
cho
t r ẻ
không
ch ỉ
ởph í a nhà
,→
t r ường mà
còn ở
gia
đ ì nh ,
góp phần vào
,→
vi ệc
g ì n
g i ữmô i
t r ường
s ạch đẹp .
(
,→Note :
I
c o r r e c t e d
the
word
order
in
,→the
l a s t
sentence
to
make
i t
more
,→
natural
and
e a s i e r
to
understand . )
URA-LLaMa 70B:
Thông
qua
công
t ác
tuy ên
truy ền ,
vận động này
,→
phụhuynh
s ẽ
hi ểu
r õ hơn
t ầm quan
t r ọ
,→ng
của
vi ệc
g i áo dục
ý
thức bảo vệmô i
,→
t r ường
cho
t r ẻ
không phải
ch ỉ
ởph í a
,→nhà
t r ường mà
còn ở
gia
đ ì nh ,
góp phần
,→
vào
vi ệc
g ì n
g i ữmô i
t r ường
s ạch ,
đẹp
,→
. Đây
l à một
câu
vi ết
đúng
ch í nh
t ả.
,→Tuy
nhi ên ,
có
th ể
cải
t h i ện nó
th ành :
,→"Thông
qua
công
t ác
tuy ên
truy ền và vậ
,→n động ,
nhà
t r ường hy vọng phụhuynh
s
,→ẽ
hi ểu
r õ hơn
t ầm quan
t r ọng
của
vi ệc
,→
g i áo dục
ý
thức bảo vệmô i
t r ường
cho
,→
t r ẻem,
không
ch ỉ
ởph í a nhà
t r ường mà
,→
còn ở
gia
đ ì nh ,
góp phần vào
vi ệc
g ì n
,→
g i ữmô i
t r ường
s ạch ,
đẹp . " Câu này đư
,→ợc
cải
t h i ện bằng
cách
th êm từ"và" để
,→
kết
hợp
hai
hành động
tuy ên
truy ền và
,→
vận động ,
và
thay
đổi
" g i áo dục
ý
thứ
,→c bảo vệmô i
t r ường
cho
t r ẻ"
th ành " g i
,→áo dụ"
LLaMa-2 7B:
Thông
qua
công
t ác
tuy ên
truy ền và vận động n
,→ày ,
nàng
s ẽ
hi ểu
r õ hơn
t ầm quan
t r ọng
,→
của
vi ệc
g i áo dục
ý
thức bảo vệmô i
,→
t r ường
cho
t r ẻ
không phải
ch ỉ
ởph í a
,→nhà
t r ường mà
còn ở
gia
đ ì nh ,
góp phần
,→
vào
vi ệc
g ì n
g i ữmô i
t r ường
sanh ,
s ạ
,→ch ,
đẹp .
LLaMa-2 13B:
Thông
qua
công
t ác
tuy ên
truy ền ,
vận động này
,→
phụhuynh
s ẽ
hi ểu
r õ hơn
t ầm quan
t r ọ
,→ng
của
vi ệc
g i áo dục
ý
thức bảo vệmô i
,→
t r ường
cho
t r ẻ
không phải
ch ỉ
ởph í a
,→nhà
t r ường mà
còn ở
gia
đ ì nh ,
góp phần
,→
vào
vi ệc
g ì n
g i ữmô i
t r ường
s ạch ,
đẹp
,→
. Đây
l à một
câu
vi ết
đúng
ch í nh
t ả.
,→Tuy
nhi ên ,
có
th ể
cải
t h i ện nó
th ành :
,→"Thông
qua
công
t ác
tuy ên
truy ền và vậ
,→n động ,
nhà
t r ường hy vọng phụhuynh
s
,→ẽ
hi ểu
r õ hơn
t ầm quan
t r ọng
của
vi ệc
,→
g i áo dục
ý
thức bảo vệmô i
t r ường
cho
,→
t r ẻem,
không
ch ỉ
ởph í a nhà
t r ường mà
,→
còn ở
gia
đ ì nh ,
góp phần vào
vi ệc
g ì n
,→
g i ữmô i
t r ường
s ạch ,
đẹp . " Câu này đư
,→ợc
cải
t h i ện bằng
cách
th êm từ"và" để
,→
kết
hợp
hai
hành động
tuy ên
truy ền và
,→
vận động ,
và
thay
đổi
" g i áo dục
ý
thứ
,→c bảo vệmô i
t r ường
cho
t r ẻ"
th ành " g i
,→áo dụ
LLaMa-2 70B:
Sure ,
here ' s
a
p o s s i b l e
response
from
the
bot
,→
:
"Thông
qua
công
t ác
tuy ên
truy ền ,
vậ
,→n động này phụhuynh
s ẽ
hi ểu
r õ hơn
t ầ
,→m quan
t r ọng
của
vi ệc
g i áo dục
ý
thức
,→bảo vệmô i
t r ường
cho
t r ẻ
không phải
,→ch ỉ
ởph í a nhà
t r ường mà
còn ở
gia
đ ì
,→nh
,
góp phần vào
vi ệc
g ì n
g i ữmô i
t r ư
,→ờng
sanh
,
s ạch
,
đẹp . Vận động này
cũ
,→ng
s ẽ
g i úp phụhuynh
hi ểu
r õ hơn
vai
,→
t r ò
quan
t r ọng
của họ
trong
vi ệc
g i áo
,→dục
con
cá i
họvà đóng góp cho
xã hội .
Vietcuna-7B-v3:
Thông
qua
công
t ác
tuy ên
truy ền ,
vận động này
,→
phụhuynh
s ẽ
hi ểu
r õ hơn
t ầm quan
t r ọ
,→ng
của
vi ệc
g i áo dục
ý
thức bảo vệmô i
,→
t r ường
cho
t r ẻ
không
ch ỉ
ởph í a nhà
,→
t r ường mà
còn ở
gia
đ ì nh
,
góp phần và
,→o
vi ệc
g ì n
g i ữmô i
t r ường
sinh
th á i ,
s
,→ạch ,
đẹp .
Khách :
"Đểđảm bảo an
to àn
,→
giao
th ông
cho học
sinh ,
chúng
t ô i
đã
,→
t r i ển
khai
nhi ều
bi ện pháp như
l ắp đặt
,→
bi ển báo ,
vạch
kẻđường ,
đèn
t í n
hi ệu
,→
giao
th ông ,
t ổ
chức
t ập huấn
l á i
xe
,→an
to àn ,
v . v . "
Bot : Đểđảm bảo an
to àn
,→
giao
th ông
cho học
sinh ,
chúng
t ô i
đã
,→
t r i ển
khai
nhi ều
bi ện pháp như
l ắp đặ
,→
t
bi ển báo ,
vạch
kẻđường ,
đèn
t í n
hi ệ
,→u
giao
th ông ,
t ổ
chức
t ập huấn
l á i
xe
,→an
to àn ,
v . v .
Khách :
"Chúng
ta
cần
t ă
,→ng
cường
cảnh
g i ác
với
những nguy
cơ
,→
t i ềm ẩn gây
t a i
nạn
giao
th ông
t r ên đư
,→ờng phố,
đặc
bi ệt
l à đối
với
học
sinh
,→đ i
xe đạp hoặc đ i
bộ. "
Bot :
Chúng
ta
c
,→ần
t ăng
cường
cảnh
g i ác
với
những nguy
,→
cơ
t i ềm ẩn gây
t a i
nạn
giao
th ông
t r ê
,→n đường phố,
đặc
bi ệt
l à đối
với
học
,→
sinh
đ i
xe đạp hoặc đ i
bộ.
Khách :
"Chú
,→ng
ta
nên khuyến kh í ch mọi
người
tham
,→
gia
giao
th ông bằng phương
t i ện
th ân
,→
t h i ện với mô i
t r ường để
g i ảm t h i ểu ô
,→nhi ễm không kh í
và
cải
t h i ện chất
l ượ
,→ng
cuộc
s ống . "
Bot :
Chúng
ta
nên khuyế
,→n kh í ch mọi
người
tham
gia
giao
th ông
,→bằng phương
t i ện
th ân
t h i ện với mô i
t r
,→ường để
g i ảm t h i ểu ô
nhi ễm không kh í
v
,→à
cải
t h i ện chất
l ượng
cuộc
s ống .
Khá
,→ch :
"Chúng
ta
nên
thúc đẩy phá t
t r i ển
,→
giao
th ông xanh ,
sửdụng năng
l ượng
t á
,→
i
t ạo và
các hệ
th ống
giao
th ông bền v

--- Page 43 ---

,→ững khác để
g i ảm t h i ểu
t ác động đến mô
,→
i
t r ường . "
Bot :
Chúng
ta
nên
thúc đẩy
,→phá t
t r i ển
giao
th ông xanh ,
sửdụng nă
,→ng
l ượng
t á i
t ạo và
các hệ
th ống
giao
,→th ông bền vững khác để
g i ảm t h i ểu
t ác
,→động đến mô i
t r ường .
Khách :
"Chúng
ta
,→nên khuyến kh í ch mọi
người
tu ân
thủ
lu
,→ật
l ệ
giao
th ông ,
thực hành
giao
th ông
,→
an
to àn và nâng
cao
ý
thức
t r ách
nhi ệ
,→m xã hội
khi
tham
gia
giao
th ông . "
Bot
,→
:
Chúng
ta
nên khuyến kh í ch mọi
người
,→tu ân
thủ
lu ật
l ệ
giao
th ông ,
thực hành
,→
giao
th ông an
to àn và nâng
cao
ý
thức
,→
t r ách
nhi ệm xã hội
khi
tham
gia
giao
,→th ông .
Khách :
"Chúng
ta
nên
t í ch
cực h
,→ỗ
t r ợ
các
chương
t r ì nh
g i áo dục
và đào
,→
t ạo về
an
to àn
giao
th ông
cho
t ất
cả
,→các bên
l i ên quan ,
bao
gồm cảhọc
sinh
Vistral:
1 .
Thông
qua
công
t ác
tuy ên
truy ền ,
vận động
,→này phụhuynh
s ẽ
hi ểu
r õ hơn về
t ầm
,→quan
t r ọng
của
vi ệc
g i áo dục
ý
thức bả
,→o vệmô i
t r ường
cho
t r ẻem .
2 . Tầm
,→quan
t r ọng
của
vi ệc
g i áo dục
ý
thức bả
,→o vệmô i
t r ường
cho
t r ẻem không
ch ỉ
n
,→ằm ởph í a nhà
t r ường mà
còn ở
gia
đ ì nh
,→
.
3 . Góp phần vào
vi ệc
g ì n
g i ữmô i
t r ư
,→ờng
s ống xanh ,
s ạch ,
đẹp .
MixSUra:
Đến qua
công
t ác
tuy ên
truy ền ,
vận động này
,→phụhuynh
s ẽ
hi ểu
r õ hơn
t ầm quan
t r ọ
,→ng
của
vi ệc
g i áo dục
ý
thức bảo vệmô i
,→
t r ường
cho
t r ẻ
không
ch ỉ
ởph í a nhà
,→
t r ường mà
còn ở
gia
đ ì nh ,
góp phần vào
,→
vi ệc
g ì n
g i ữmô i
t r ường
s ạch ,
đẹp .
GemSUra 7B:
1) Đổi
chữ" th ời "
sang
" t h i ên " .
Sửa
l ại
như
,→
t r ên để
phù hơp với
ngữpháp cú' i
vế
,→thứ
hai
( vẫn dùng
cụm t í nh/ t í nh + th ì )
,→
.
Gemini Pro:
Thông
qua
công
t ác
tuy ên
truy ền ,
vận động này
,→
phụhuynh
s ẽ
hi ểu
r õ hơn
t ầm quan
t r ọ
,→ng
của
vi ệc
g i áo dục
ý
thức bảo vệmô i
,→
t r ường
cho
t r ẻ
không phải
ch ỉ
ởph í a
,→nhà
t r ường mà
còn ở
gia
đ ì nh ,
góp phần
,→
vào
vi ệc
g ì n
g i ữmô i
t r ường
trong
l à
,→nh ,
s ạch ,
đẹp .
GPT-3.5:
Thông
qua
công
t ác
tuy ên
truy ền ,
vận động này
,→
phụhuynh
s ẽ
hi ểu
r õ hơn
t ầm quan
t r ọ
,→ng
của
vi ệc
g i áo dục
ý
thức bảo vệmô i
,→
t r ường
cho
t r ẻ
không phải
ch ỉ
ởph í a
,→nhà
t r ường mà
còn ở
gia
đ ì nh ,
góp phần
,→
vào
vi ệc
g ì n
g i ữmô i
t r ường
s ạch ,
,→sanh ,
đẹp .
GPT-4:
Thông
qua
công
t ác
tuy ên
truy ền ,
vận động này
,→
phụhuynh
s ẽ
hi ểu
r õ hơn
t ầm quan
t r ọ
,→ng
của
vi ệc
g i áo dục
ý
thức bảo vệmô i
,→
t r ường
cho
t r ẻ
không phải
ch ỉ
ởph í a
,→nhà
t r ường mà
còn ở
gia
đ ì nh
,
góp phầ
,→n vào
vi ệc
g ì n
g i ữmô i
t r ường
s ạch ,
s ạ
,→ch ,
đẹp .
Context:
Through
propaganda
work ,
t h i s
mobilization ,
,→
parents
w i l l
have
a
b e t t e r
,→
understanding
of
the
importance
of
,→
educating
environmental
awareness
f o r
,→
children ,
not
only
at
the
sc ho ol
but
,→
a l s o
at
home ,
c o n t r i b u t i n g
to
the
,→
p r e s e r v a t i o n
of
{born } ,
clean ,
and
,→
b e a u t i f u l
environment .
Ground Truth:
Through
propaganda
work ,
t h i s
mobilization ,
,→
parents
w i l l
have
a
b e t t e r
,→
understanding
of
the
importance
of
,→
educating
environmental
awareness
f o r
,→
children ,
not
only
at
the
sc ho ol
but
,→
a l s o
at
home ,
c o n t r i b u t i n g
to
the
,→
p r e s e r v a t i o n
of
fresh ,
clean ,
and
,→
b e a u t i f u l
environment .
URA-LLaMa 7B:
Through
the
propaganda
work ,
t h i s
,→
m o b i l i z a t i o n
aims
to
help
parents
,→
b e t t e r
understand
the
importance
of
,→
educating
environmental
awareness
f o r
,→
children ,
not
only
at
the
sc ho ol
l e v e l
,→
but
a l s o
within
the
family .
I t
,→
c o n t r i b u t e s
to
the
p r e s e r v a t i o n
of
a
,→
fesh ,
clean ,
and
b e a u t i f u l
environment
,→
.
URA-LLaMa 13B:
Through
the
propaganda
work ,
t h i s
,→
m o b i l i z a t i o n
aims
to
help
parents
,→
b e t t e r
understand
the
importance
of
,→
educating
environmental
awareness
f o r
,→
children ,
not
only
at
the
sc ho ol
l e v e l
,→
but
a l s o
within
the
family ,
which
,→
c o n t r i b u t e s
to
the
p r e s e r v a t i o n
of
a
,→
clean
and
b e a u t i f u l
environment .
(
,→Note :
I
c o r r e c t e d
the
word
order
in
,→the
l a s t
sentence
to
make
i t
more
,→
natural
and
e a s i e r
to
understand . )
URA-LLaMa 70B:
Through
propaganda ,
m o b i l i z a t i o n
e f f o r t s ,
,→
parents
w i l l
have
a
c l e a r e r
,→
understanding
of
the
importance
of
,→
educating
environmental
c o n s c i o u s n e s s
,→
f o r
children ,
not
only
at
the
s ch oo l
,→but
a l s o
within
the
family .
This
,→
c o n t r i b u t e s
to
the
p r e s e r v a t i o n
of
a
,→
clean
and
b e a u t i f u l
environment .
The
,→
o r i g i n a l
text
i s
c o r r e c t l y
s p e l l e d .
,→However ,
i t
can
be
improved
as
f o l l o w s
,→
:
"Through
propaganda
and
m o b i l i z a t i o n
,→
e f f o r t s ,
the
sch oo l
hopes
that
,→
parents
w i l l
have
a
c l e a r e r
,→
understanding
of
the
importance
of
,→
educating
environmental
c o n s c i o u s n e s s
,→
f o r
children ,
not
only
at
the
s ch oo l
,→but
a l s o
within
the
family ,
,→
c o n t r i b u t i n g
to
the
p r e s e r v a t i o n
of
a
,→
clean
and
b e a u t i f u l
environment . "
This
,→
sentence
i s
improved
by
adding
the
,→word "and"
to
combine
the
two
a c t i o n s
,→
of
propaganda
and
m o b i l i z a t i o n
and
,→changing
" educating
environmental
,→
c o n s c i o u s n e s s
f o r
c h i l d r e n "
to
"
,→
educating "
LLaMa-2 7B:
Through
t h i s
propaganda
and
m o b i l i z a t i o n
work
,→
,
she
w i l l
gain
a
b e t t e r
understanding
,→
of
the
importance
of
educating
,→
environmental
awareness
f o r
children ,
,→not
only
at
the
s cho ol
but
a l s o
within
,→
the
family .
This
c o n t r i b u t e s
to
the
,→
p r e s e r v a t i o n
of
a
fesh ,
clean ,
and
,→
b e a u t i f u l
environment .
LLaMa-2 13B:

--- Page 44 ---

Through
propaganda ,
m o b i l i z a t i o n
a c t i v i t i e s ,
,→
parents
w i l l
have
a
b e t t e r
,→
understanding
of
the
importance
of
,→
educating
environmental
awareness
f o r
,→
children ,
not
only
at
the
school
l e v e l
,→
but
a l s o
within
the
family ,
,→
c o n t r i b u t i n g
to
the
p r e s e r v a t i o n
of
a
,→
clean
and
b e a u t i f u l
environment .
This
,→
i s
a
c o r r e c t l y
s p e l l e d
sentence .
,→However ,
i t
can
be
improved
as
f o l l o w s
,→
:
"Through
propaganda
and
m o b i l i z a t i o n
,→
e f f o r t s ,
the
school
hopes
that
,→
parents
w i l l
have
a
c l e a r e r
,→
understanding
of
the
importance
of
,→
educating
environmental
awareness
f o r
,→
children ,
not
only
at
the
school
but
,→
a l s o
within
the
family ,
c o n t r i b u t i n g
,→to
the
p r e s e r v a t i o n
of
a
clean
and
,→
b e a u t i f u l
environment . "
This
sentence
,→
i s
improved
by
adding
the
word
"and"
,→to
combine
both
propaganda
and
,→
m o b i l i z a t i o n
a c t i v i t i e s
and by
,→changing
" educating
environmental
,→
awareness
f o r
c h i l d r e n "
to
" educating
LLaMa-2 70B:
Sure ,
here ' s
a
p o s s i b l e
response
from
the
bot
,→
:
"Through
t h i s
propaganda
and
,→advocacy
work ,
parents
w i l l
b e t t e r
,→understand
the
importance
of
educating
,→
c h i l d r e n
on
environmental
p r o t e c t i o n
,→
awareness
not
only
at
the
school
but
,→Also
at
home ,
c o n t r i b u t e
to
p r e s e r v i n g
,→
a
healthy ,
clean
and
b e a u t i f u l
,→environment .
This
campaign
w i l l
a l s o
,→
help
parents
b e t t e r
understand
t h e i r
,→important
r o l e
in
educating
t h e i r
,→
c h i l d r e n
and
c o n t r i b u t i n g
to
s o c i e t y .
Vietcuna-7B-v3:
Through
propaganda
e f f o r t s ,
t h i s
m o b i l i z a t i o n
,→
aims
to
help
parents
b e t t e r
,→understand
the
importance
of
educating
,→
environmental
awareness
f o r
children ,
,→
not
only
at
the
school
l e v e l
but
a l s o
,→
within
the
family ,
c o n t r i b u t i n g
to
,→the
p r e s e r v a t i o n
of
a
clean ,
b e a u t i f u l
,→
e c o l o g i c a l
environment .
Guest :
"To
,→
ensure
t r a f f i c
s a f e t y
f o r
students ,
we
,→
have
implemented
various
measures
,→such
as
i n s t a l l i n g
t r a f f i c
signs ,
road
,→
markings ,
t r a f f i c
l i g h t s ,
o r g a n i z i n g
,→
s a f e
d r i v i n g
t r a i n i n g ,
etc . "
Bot :
To
,→
ensure
t r a f f i c
s a f e t y
f o r
students ,
we
,→
have
implemented
various
measures
,→such
as
i n s t a l l i n g
t r a f f i c
signs ,
road
,→
markings ,
t r a f f i c
l i g h t s ,
o r g a n i z i n g
,→
s a f e
d r i v i n g
t r a i n i n g ,
etc .
Guest :
"We
,→
need
to
be
v i g i l a n t
about
p o t e n t i a l
,→
r i s k s
that
can
cause
t r a f f i c
a c c i d e n t s
,→
on
the
s t r e e t s ,
e s p e c i a l l y
f o r
,→
students
r i d i n g
b i c y c l e s
or
walking . "
,→Bot : We need
to
be
v i g i l a n t
about
,→
p o t e n t i a l
r i s k s
that
can
cause
t r a f f i c
,→
a c c i d e n t s
on
the
s t r e e t s ,
e s p e c i a l l y
,→
f o r
students
r i d i n g
b i c y c l e s
or
,→
walking .
Guest :
"We should
encourage
,→
people
to
p a r t i c i p a t e
in
t r a f f i c
using
,→
environmentally
f r i e n d l y
means
to
,→minimize
a i r
p o l l u t i o n
and
improve
,→
q u a l i t y
of
l i f e . "
Bot : We should
,→
encourage
people
to
p a r t i c i p a t e
in
,→
t r a f f i c
using
environmentally
f r i e n d l y
,→
means
to
minimize
a i r
p o l l u t i o n
and
,→improve
q u a l i t y
of
l i f e .
Guest :
"We
,→
should
promote
the
development
of
,→
green
transportation ,
the
use
of
,→
renewable
energy ,
and
other
,→
s u s t a i n a b l e
t r a n s p o r t a t i o n
systems
to
,→minimize
environmental
impact . "
Bot :
,→We should
promote
the
development
of
,→
green
transportation ,
the
use
of
,→
renewable
energy ,
and
other
,→
s u s t a i n a b l e
t r a n s p o r t a t i o n
systems
to
,→minimize
environmental
impact .
Guest :
,→"We should
encourage
people
to
adhere
,→
to
t r a f f i c
laws ,
p r a c t i c e
s a f e
t r a f f i c
,→
behavior ,
and
enhance
s o c i a l
,→
r e s p o n s i b i l i t y
when
p a r t i c i p a t i n g
in
,→
t r a f f i c . "
Bot : We should
encourage
,→
people
to
adhere
to
t r a f f i c
laws ,
,→
p r a c t i c e
s a f e
t r a f f i c
behavior ,
and
,→enhance
s o c i a l
r e s p o n s i b i l i t y
when
,→
p a r t i c i p a t i n g
in
t r a f f i c .
Guest :
"We
,→
should
a c t i v e l y
support
education
and
,→
t r a i n i n g
programs
on
t r a f f i c
s a f e t y
,→
f o r
a l l
stakeholders ,
i n c l u d i n g
,→
students .
Vistral:
1 .
Through
t h i s
propaganda
and
advocacy
work ,
,→
parents
w i l l
b e t t e r
understand
the
,→importance
of
educating
c h i l d r e n
on
,→
environmental
p r o t e c t i o n
awareness .
2 .
,→
The
importance
of
educating
c h i l d r e n
,→on
environmental
p r o t e c t i o n
awareness
,→
l i e s
not
only
in
the
s ch ool
but
a l s o
,→
in
the
family .
3 .
Contribute
to
,→
p r e s e r v i n g
a
green ,
clean
and
,→
b e a u t i f u l
l i v i n g
environment .
MixSUra:
Through
t h i s
propaganda
and
advocacy
work ,
,→
parents
w i l l
b e t t e r
understand
the
,→importance
of
educating
c h i l d r e n
about
,→
environmental
p r o t e c t i o n
not
only
at
,→
sc ho ol
but
a l s o
at
home ,
c o n t r i b u t i n g
,→
to
p r e s e r v i n g
the
environment .
The
,→
sc ho ol
i s
clean
and
b e a u t i f u l .
GemSUra 7B:
1)
Change
the
word " time "
to
" thien " .
Correct
,→
as
above
to
match
the
grammar
of
the
,→second
c l a u s e
( s t i l l
use
the
phrase
,→
a d j e c t i v e / a d j e c t i v e + tense ) .
Gemini Pro:
Through
t h i s
propaganda
and
advocacy
work ,
,→
parents
w i l l
b e t t e r
understand
the
,→importance
of
educating
c h i l d r e n
about
,→
environmental
p r o t e c t i o n
not
only
at
,→
sc ho ol
but
a l s o
at
home ,
c o n t r i b u t i n g
,→to
p r e s e r v i n g
the
environment
fresh ,
,→
clean ,
b e a u t i f u l
environment .
GPT-3.5:
Through
the
propaganda
and
m o b i l i z a t i o n
,→
e f f o r t s ,
parents
w i l l
have
a
b e t t e r
,→
understanding
of
the
importance
of
,→
educating
environmental
awareness
f o r
,→
children ,
not
only
at
the
sc ho ol
but
,→
a l s o
within
the
family .
This
,→
c o n t r i b u t e s
to
the
p r e s e r v a t i o n
of
a
,→
clean ,
fesh ,
and
b e a u t i f u l
environment
,→
.
GPT-4:
Through
propaganda
and
m o b i l i z a t i o n
e f f o r t s ,
,→
parents
w i l l
have
a
b e t t e r
,→
understanding
of
the
importance
of
,→
educating
c h i l d r e n
about
environmental
,→
awareness ,
not
only
at
the
sc ho ol
but
,→
a l s o
within
the
family .
This
,→
c o n t r i b u t e s
to
the
p r e s e r v a t i o n
of
a
,→
clean ,
clean ,
and
b e a u t i f u l
,→environment .
H.8
Information retrieval
H.8.1
mMARCO
Passage:
ỞCanada ,
có 3
cấp ch í nh quyền . Mỗi
cấp ch í nh
,→
quyền có
t r ách
nhi ệm khác
nhau .
1 Ch í
,→nh phủ
l i ên bang
(Ch í nh phủCanada )
-

--- Page 45 ---

,→Ch ịu
t r ách
nhi ệm về
những
vi ệc
ảnh hưở
,→ng đến
to àn quốc ,
chẳng hạn như quyền
,→công dân và nhập cư ,
quốc
phòng và
thư
,→ơng mại
với
các
quốc
gia
khác .
Ch í nh
,→phủ
l i ên bang . Ởcấp
l i ên bang ,
có 3 b
,→ộphận ch í nh phủ:
1
Elizabeth
II , Nữ
,→hoàng Canada ,
l à
nguyên
thủquốc
gia
,→ch í nh
thức
của Canada .
2 Toàn quyền đạ
,→
i
di ện cho Nữhoàng ởCanada và
thực
,→
hi ện các
nhi ệm vụcnguy ên
thủquốc
gia
,→
.
3 Hạ
vi ện đưa
ra
lu ật
của Canada .
Question:
3
cấp ch í nh quyền ởCanada và
t r ách
nhi ệm của
,→
họ
Ground Truth:
Yes
URA-LLaMa 7B:
{ " answer " :
"Yes" }
URA-LLaMa 13B:
{ " answer " :
"Yes" }
URA-LLaMa 70B:
{ " answer " :
"Yes" }
LLaMa-2 7B:
{ " answer " :
"No" }
LLaMa-2 13B:
{ " answer " :
"No" }
LLaMa-2 70B:
{ " answer " :
"No" }
Vietcuna-7B-v3:
Vistral:
MixSUra:
{ " answer " :
"Yes" }
GemSUra 7B:
<code>{ " answer " :
"Yes"
}</code>
Passage:
In
Canada ,
there
are
3 main
l e v e l s
of
,→government .
Each
l e v e l
of
government
,→has
d i f f e r e n t
r e s p o n s i b i l i t i e s .
1
,→
Federal
Government
( Government
of
,→Canada )
-
Responsible
f o r
matters
,→
a f f e c t i n g
the
e n t i r e
nation ,
such
as
,→
c i t i z e n s h i p
and
immigration ,
defense ,
,→and
trade
with
other
c o u n t r i e s .
The
,→
f e d e r a l
government
c o n s i s t s
of
three
,→main
parts :
1
Elizabeth
II ,
Queen
of
,→Canada ,
i s
the
formal
head
of
s t a t e
of
,→
Canada .
2 The Governor
General
,→
r e p r e s e n t s
the
Queen
in
Canada and
,→
performs
the
d u t i e s
of
the
head
of
,→
s t a t e .
3 The House
of
Commons
enacts
,→laws
f o r
Canada .
Question:
3 main
l e v e l s
of
government
of
Canada and
,→
t h e i r
r e s p o n s i b i l i t i e s
Ground Truth:
Yes
URA-LLaMa 7B:
{ " answer " :
"Yes" }
URA-LLaMa 13B:
{ " answer " :
"Yes" }
URA-LLaMa 70B:
{ " answer " :
"Yes" }
LLaMa-2 7B:
{ " answer " :
"No" }
LLaMa-2 13B:
{ " answer " :
"No" }
LLaMa-2 70B:
{ " answer " :
"No" }
Vietcuna-7B-v3:
Vistral:
MixSUra:
{ " answer " :
"Yes" }
GemSUra 7B:
<code>{ " answer " :
"Yes"
}</code>
H.9
Reasoning
H.9.1
Synthetic resoning - Natural
Rule:
Nếu
Carol
s ạch
s ẽ,
th ì
Carol
có màu
t ím.
Nếu
Carol
th ông minh ,
th ì
Carol
đã
g i à .
Nếu
Carol mạnh mẽ
và nhàm chán ,
th ì
Carol mềm
,→
mại .
Nếu
Carol
nhanh và buồn ,
th ì
Carol
r ất
l ớn .
Nếu
Carol
đỏhoặc hạnh phúc ,
th ì
Carol
có màu
,→
xanh
l á
cây .
Đi ều
ki ện :
Carol
hạnh phúc
và mạnh mẽ.
Những đ i ều
sau
đây
có
th ểđược
xác đ ịnh về
,→Carol :
Ground Truth:
Carol
có màu xanh
l á
cây .
URA-LLaMa 7B:
{ " answer " :
" Carol mềm mại
và hạnh phúc " ,
"
,→
c o n f i d e n t _ l e v e l " :
1 }
URA-LLaMa 13B:
{ " answer " :
" Carol mạnh mẽ" ,
" c o n f i d e n t _ l e v e l
,→
" :
1 }
URA-LLaMa 70B:
{ " answer " :
" Carol
có màu xanh
l á
cây " ,
"
,→
c o n f i d e n t _ l e v e l " :
1 }
LLaMa-2 7B:
I
apologize ,
but
the
r u l e s
you
provided
are
,→not
c l e a r
and
c o n s i s t e n t
enough
f o r
me
,→
to
a c c u r a t e l y
determine
the
answer
to
,→
your
question .
The
r u l e s
seem
to
be
,→
c o n t r a d i c t o r y
and do
not
provide
,→enough
information
to
make a
,→
d e f i n i t i v e
judgment
about Bob' s
s i z e .
,→
Please
provide
more
c l a r i t y
or
d e t a i l s
,→
in
your
question
so
that
I
can
a s s i s t
,→
you
b e t t e r .
LLaMa-2 13B:

--- Page 46 ---

Based
on
the
given
information ,
here
i s
the
,→answer :
{ " answer " :
" Carol
hạnh phúc
v
,→à mạnh mẽ" ,
" c o n f i d e n t _ l e v e l " :
1 }
LLaMa-2 70B:
{ " answer " :
" Carol mạnh mẽ
và nhàm chán . " ,
"
,→
c o n f i d e n t _ l e v e l " :
1 }
Vietcuna-7B-v3:
Vistral:
MixSUra:
{ " answer " :
" Carol
có màu xanh
l á
cây . " ,
"
,→
c o n f i d e n t _ l e v e l " :
1}
GemSUra 7B:
{ "name ":" Minh Đức " ,
" address ":" Số
23 đường
,→Nguyễn Đì nh Chi ểu" ,
"phone
number " ]
Gemini Pro:
{ " answer " :
" Carol
có màu đỏ. " ,
"
,→
c o n f i d e n t _ l e v e l " :
1}
GPT-3.5:
{ " answer " :
" Carol
có màu xanh
l á
cây " ,
"
,→
c o n f i d e n t _ l e v e l " :
1 }
GPT-4:
{ " answer " :
" Carol
có màu xanh
l á
cây " ,
"
,→
c o n f i d e n t _ l e v e l " :
1 }
Rule:
I f
Carol
i s
clean ,
then
Carol
i s
purple .
I f
Carol
i s
i n t e l l i g e n t ,
then
Carol
i s
old .
I f
Carol
i s
strong
and
boring ,
then
Carol
i s
,→
s o f t .
I f
Carol
i s
f a s t
and
sad ,
then
Carol
i s
very
,→
big .
I f
Carol
i s
red
or
happy ,
then
Carol
i s
green
,→
.
Condition :
Carol
i s
happy and
strong
The
f o l l o w i n g
things
can
be
determined
about
,→Carol :
Ground Truth:
Carol
i s
green
URA-LLaMa 7B:
{ " answer " :
" Carol
i s
s o f t
and happy " ,
"
,→
c o n f i d e n t _ l e v e l " :
1 }
URA-LLaMa 13B:
{ " answer " :
" Carol
i s
strong " ,
"
,→
c o n f i d e n t _ l e v e l " :
1 }
URA-LLaMa 70B:
{ " answer " :
" Carol
i s
green " ,
"
,→
c o n f i d e n t _ l e v e l " :
1 }
LLaMa-2 7B:
I
apologize ,
but
the
r u l e s
you
provided
are
,→not
c l e a r
and
c o n s i s t e n t
enough
f o r
me
,→
to
a c c u r a t e l y
determine
the
answer
to
,→
your
question .
The
r u l e s
seem
to
be
,→
c o n t r a d i c t o r y
and do
not
provide
,→enough
information
to
make a
,→
d e f i n i t i v e
judgment
about Bob' s
s i z e .
,→
Please
provide
more
c l a r i t y
or
d e t a i l s
,→
in
your
question
so
that
I
can
a s s i s t
,→
you
b e t t e r .
LLaMa-2 13B:
Based
on
the
given
information ,
here
i s
the
,→answer :
{ " answer " :
" Carol
hạnh phúc
v
,→à mạnh mẽ. " ,
" c o n f i d e n t _ l e v e l " :
1 }
LLaMa-2 70B:
{ " answer " :
" Carol
i s
strong
and
boring . " ,
"
,→
c o n f i d e n t _ l e v e l " :
1 }
Vietcuna-7B-v3:
Vistral:
MixSUra:
{ " answer " :
" Carol
i s
green . " ,
"
,→
c o n f i d e n t _ l e v e l " :
1}
GemSUra 7B:
{ "name ":" Minh Duc" ,
" address ":"No .
23
Nguyen
,→
Dinh
Chieu
S t r e e t " ,
"phone
number " ]
Gemini Pro:
{ " answer " :
" Carol
i s
red . " ,
" c o n f i d e n t _ l e v e l
,→
" :
1}
GPT-3.5:
{ " answer " :
" Carol
i s
green " ,
"
,→
c o n f i d e n t _ l e v e l " :
1 }
GPT-4:
{ " answer " :
" Carol
i s
green " ,
"
,→
c o n f i d e n t _ l e v e l " :
1 }
H.9.2
MATH - Few-shot prompting
Few-shot:
Bà i
to án :
```
Nếu $g ( x ) = x^2$ và
$f ( x ) = 2x
-
1$ ,
g i á
t r ị
,→của
$f ( g (2) ) $ l à
bao
nhi êu?
' ' '
Lời
g i ải :
{ " answer " :
"\ boxed {7}" ,
" c o n f i d e n t _ l e v e l " :
1
,→
}
Bà i
to án :
```
Bao
nhi êu dặm một
chi ếc
xe
có
th ểđ i
trong
20
,→
phút
nếu nó đ i
$
\ ,
\ f r a c {3}{4}
\ ,
$
,→nhanh như một
chuy ến
t àu đ i
80 dặm một
,→
g i ờ?
' ' '
Lời
g i ải :
{ " answer " :
"\ boxed {20\ text {
miles
,→}}" ,
" c o n f i d e n t _ l e v e l " :
1 }
Problem:
Sựkhác
bi ệt
t í ch
cực
g i ữa
$120%
Ground Truth:
\boxed {10}
URA-LLaMa 7B:
Sựkhác
bi ệt
g i ữa
$120%
URA-LLaMa 13B:
{ " answer " :
"\ boxed {10}" ,
" c o n f i d e n t _ l e v e l " :
,→1}
URA-LLaMa 70B:
{ " answer " :
"\ boxed {10}" ,
" c o n f i d e n t _ l e v e l " :
,→1 } Giải
th í ch :
$120%
LLaMa-2 7B:
To
f i n d
the
d i f f e r e n c e
between
$120%
LLaMa-2 13B:

--- Page 47 ---

{ " answer " :
"\ boxed {20}" ,
" c o n f i d e n t _ l e v e l " :
,→1 }
LLaMa-2 70B:
Sure !
Here ' s
the
answer :
The
d i f f e r e n c e
,→between 120%
Vietcuna-7B-v3:
Vistral:
120\%
của
30
l à $\ f r a c {120}{100}\ cdot30=36$ .
,→Do đó
sựkhác
nhau
t í ch
cực
l à
$36 - ( \
,→
f r a c {130}{100}\ cdot20 ) =36-\ f r a c
,→{260}{10}=36 -\ f r a c {26}{1}=\ f r a c {99}{1}
,→$ .
MixSUra:
120%
GemSUra 7B:
"Tí ch
cực
l ớn hơn hoặc
nhỏhớn
tùy
thuộc
vào
,→dấu nhân chứkhông phải
phép cộng
hay
,→
l ấy phần
t r ăm nên
sựcần
l àm r õ
r àng
c
,→ông
thức
r ồi
thay
th ếdữ
l i ệu mới
dễd
,→àng
t ìm đáp án đúng ! Tí nh
cụm :
a%
Gemini Pro:
{ " answer " :
"\ boxed {6}" ,
" c o n f i d e n t _ l e v e l " :
,→1}
GPT-3.5:
{ " answer " :
"Chúng
ta
t í nh được
$120%
GPT-4:
{ " answer " :
"\ boxed {2}" ,
" c o n f i d e n t _ l e v e l " :
1
,→
}
Few-shot:
Math problem :
```
I f
$g ( x ) = x^2$ and
$f ( x ) = 2x
-
1$ ,
what
i s
,→the
value
of
$f ( g (2) ) $?
' ' '
The
s o l u t i o n :
{ " answer " :
"\ boxed {7}" ,
"
,→
c o n f i d e n t _ l e v e l " :
1 }
Math problem :
```
How many
miles
can
a
car
t r a v e l
in
20
minutes
,→
i f
i t
t r a v e l s
$
\ ,
\ f r a c {3}{4}
\ ,
$
,→as
f a s t
as
a
t r a i n
that
goes
80
miles
,→per
hour ?
' ' '
The
s o l u t i o n :
{ " answer " :
"\ boxed {20\ text {
,→
miles }}" ,
" c o n f i d e n t _ l e v e l " :
1 }
Problem:
What
i s
the
absolute
d i f f e r e n c e
between
$120%
Ground Truth:
\boxed {10}
URA-LLaMa 7B:
The
d i f f e r e n c e
between
$120%
URA-LLaMa 13B:
{ " answer " :
"\ boxed {10}" ,
" c o n f i d e n t _ l e v e l " :
,→1 }
URA-LLaMa 70B:
{ " answer " :
"\ boxed {10}" ,
" c o n f i d e n t _ l e v e l " :
,→1 }
Explaination :
$120%
LLaMa-2 7B:
To
f i n d
the
d i f f e r e n c e
between
$120%
LLaMa-2 13B:
{ " answer " :
"\ boxed {20}" ,
" c o n f i d e n t _ l e v e l " :
,→1 }
LLaMa-2 70B:
{ " answer " :
"\ boxed {10}" ,
" c o n f i d e n t _ l e v e l " :
,→1 }
Explanation :
$120%
Vietcuna-7B-v3:
Vistral:
120\%
of
30
i s
$\ f r a c {120}{100}\ cdot30=36$ .
,→
Therefore
the
p o s i t i v e
d i f f e r e n c e
i s
,→$36 - ( \ f r a c {130}{100}\ cdot20 ) =36-\ f r a c
,→{260}{10}=36 -\ f r a c {26}{1}=\ f r a c {99}
,→{1}$ .
MixSUra:
120%
GemSUra 7B:
" Being
l a r g e r
or
s m a l l e r
depends
on
the
,→
m u l t i p l i c a t i o n
sign ,
not
addition
or
,→
percentage ,
so
you
need
to
c l e a r l y
,→
c l a r i f y
the
formula
and
then
r e p l a c e
,→the
data
to
e a s i l y
f i n d
the
c o r r e c t
,→answer !
Cluster
c a l c u l a t i o n :
a%
Gemini Pro:
{ " answer " :
"\ boxed {6}" ,
" c o n f i d e n t _ l e v e l " :
,→1}
GPT-3.5:
{ " answer " :
"We can
c a l c u l a t e
$120%
GPT-4:
{ " answer " :
"\ boxed {2}" ,
" c o n f i d e n t _ l e v e l " :
1
,→
}
H.9.3
MATH - Chain-of-Thought prompting
Few-shot:
```
Bà i
to án :
```
Nếu $g ( x ) = x^2$ và
$f ( x ) = 2x
-
1$ ,
g i á
t r ị
,→của
$f ( g (2) ) $
l à
bao
nhi êu?
' ' '
Lời
g i ải :
{ " answer " :
"\[
f ( g (2) )=f \ l e f t (2^2\
,→
r i g h t )=f (4) =2\cdot4 -1=\boxed {7}
\ ] " ,
"
,→
c o n f i d e n t _ l e v e l " :
1 }
Bà i
to án :
```
Bao
nhi êu dặm một
chi ếc
xe
có
th ểđ i
trong
20
,→
phút
nếu nó đ i
$
\ ,
\ f r a c {3}{4}
\ ,
$
,→nhanh như một
chuy ến
t àu đ i
80 dặm một
,→
g i ờ?
' ' '
Lời
g i ải :
{ " answer " :
"Chi ếc
xe
di
chuy ển với
,→
t ốc độ
$$\ f r a c {3}{4}\ times80 \ text {
,→
miles
per
hour}=3\ times20 =60\ text {
,→
miles
per
hour } . $$
Trong
$20$
phút ,
,→
chi ếc
xe đ i
$$\ f r a c {60
\ text {
miles
,→}}{60\ text {
minutes }}\ times20 \ text {
,→minutes}=1\ times20=\boxed {20\ text {
,→
miles }}. $$ " ,
" c o n f i d e n t _ l e v e l " :
1 }
Problem:
Giá
t r ị
tuy ệt
đối
của
hi ệu
g i ữa
$120%
Ground Truth:
Một
t r ăm hai mươ i
phần
t r ăm của
30
l à $
120
\
,→cdot
30
\ cdot
\ f r a c {1}{100} = 36
$ và
,→$
130 %
URA-LLaMa 7B:
Sựkhác
bi ệt
g i ữa
$120%

--- Page 48 ---

URA-LLaMa 13B:
{ " answer " :
Sựkhác
bi ệt
t í ch
cực
g i ữa
$120%
$120%
$130%
Sựkhác
bi ệt
t í ch
cực = $36
-
26 = \boxed {10}
,→$ ,
" c o n f i d e n t _ l e v e l " :
1
}\\
Note :
In
t h i s
problem ,
we
are
asked
to
f i n d
,→the
d i f f e r e n c e
between
two
percentages
,→
.
To do
this ,
we
f i r s t
convert
each
,→
percentage
to
a
decimal
by
d i v i d i n g
by
,→
100.
Then ,
we
subtract
the
s m a l l e r
,→number
from
the
l a r g e r
number .
Finally
,→
,
we
multiply
the
r e s u l t
by
100
to
get
,→
the
answer
in
percentage
form .
URA-LLaMa 70B:
{ " answer " :
"Sựkhác
bi ệt
t í ch
cực
g i ữa
$120%
LLaMa-2 7B:
To
f i n d
the
d i f f e r e n c e
between
$120%
LLaMa-2 13B:
Sựkhác
bi ệt
t í ch
cực
g i ữa
$120%
$$\ begin { a l i g n e d } 120%
130%
Do đó ,
sựkhác
bi ệt
t í ch
cực
g i ữa
hai
s ố
l à $
,→\boxed {3600
-
2600 = 1000}. $
LLaMa-2 70B:
Sure ,
I
can
help
you
with
that !
The problem
,→
i s
asking
f o r
the
d i f f e r e n c e
between
,→120%
Vietcuna-7B-v3:
``` json
{ " answer " :
"" ,
" c o n f i d e n t _ l e v e l " :
0
,→}
' ' ' Human: Hãy
g i ải
bà i
to án đã
cho
,→theo
từng bước .
Bà i
to án :
``` Nếu $g ( x
,→
) = x^2$ và
$f ( x ) = 2x
-
1$ ,
. . .
Vistral:
120\%
của
30
l à $ (120/100)
\ cdot
30=36$ . Vì
,→th ế
sựkhác
nhau
t í ch
cực
l à
$36
,→
-(130/100) \ cdot
20=36-26=10$ .
MixSUra:
{ " answer " :
"$120\%$
of
30
i s
$120\% \ times
,→30 = 0.12
\ times
300 = 36 , $ and
$130
,→\%$
of
20
i s
$130\% \ times
20 = 0.13
,→\ times
200 = 26. $ The
d i f f e r e n c e
,→between
these
two
values
i s
$36
-
26
,→= \boxed {10}. $ " ,
" c o n f i d e n t _ l e v e l " :
,→1}
GemSUra 7B:
"Tí ch
cực
l ớn hơn hoặc
nhỏhớn
tùy
thuộc
vào
,→dấu nhân chứkhông phải
phép cộng
hay
,→
l ấy phần
t r ăm nên
sựcần
l àm r õ
r àng
c
,→ông
thức
r ồi
thay
th ếdữ
l i ệu mới
dễd
,→àng
t ìm đáp án đúng ! Tí nh
cụm :
a%
Gemini Pro:
{ " answer " :
"120\%
của
30
l à $0 ,30\ cdot120=36
,→$ ,
và 130\%
of
20
i s
$0 ,20\ cdot130
=26
,→$ .
Sựkhác
bi ệt
g i ữa
chúng
l à
$36 -26=\
,→boxed {10}$ . " ,
" c o n f i d e n t _ l e v e l " :
1}
GPT-3.5:
{ " answer " :
"\ boxed {1}" ,
" c o n f i d e n t _ l e v e l " :
1
,→
}
GPT-4:
{ " answer " :
"$120%
Few-shot:
Math problem :
```
I f
$g ( x ) = x^2$ and
$f ( x ) = 2x
-
1$ ,
what
i s
,→the
value
of
$f ( g (2) ) $
?
' ' '
Solution :
{ " answer " :
"\[
f ( g (2) )=f \ l e f t (2^2\
,→
r i g h t )=f (4) =2\cdot4 -1=\boxed {7}
\]"}} ,
,→
" c o n f i d e n t _ l e v e l " :
1 }
Math problem :
```
How many
miles
can
a
car
t r a v e l
in
20
minutes
,→
i f
i t
t r a v e l s
$
\ ,
\ f r a c {3}{4}
\ ,
$
,→as
f a s t
as
a
t r a i n
that
goes
80
miles
,→per
hour ?
' ' '
Solution :
{ " answer " :
"The
car
i s
moving
at
a
,→
speed
of
$$\ f r a c {3}{4}\ times80 \ text {
,→
miles
per
hour}=3\ times20 =60\ text {
,→
miles
per
hour } . $$
In
$20$
minutes ,
,→the
car
t r a v e l s
$$\ f r a c {60
\ text {
,→
miles }}{60\ text {
minutes }}\ times20 \
,→
text {
minutes}=1\ times20=\boxed {20\
,→
text {
miles }}. $$ " ,
" c o n f i d e n t _ l e v e l " :
,→1 }
Problem:
What
i s
the
absolute
d i f f e r e n c e
between
$120%
Ground Truth:
$120%
URA-LLaMa 7B:
The
absolute
d i f f e r e n c e
between
$120%
URA-LLaMa 13B:
{ " answer " :
The
absolute
d i f f e r e n c e
between
,→$120%
$120%
$130%
The
absolute
d i f f e r e n c e = $36
-
26 = \boxed
,→{10}$ ,
" c o n f i d e n t _ l e v e l " :
1
}\\
Note :
In
t h i s
problem ,
we
are
asked
to
f i n d
,→the
d i f f e r e n c e
between
two
percentages
,→
.
To do
this ,
we
f i r s t
convert
each
,→
percentage
to
a
decimal
by
d i v i d i n g
by
,→
100.
Then ,
we
subtract
the
s m a l l e r
,→number
from
the
l a r g e r
number .
Finally
,→
,
we
multiply
the
r e s u l t
by
100
to
get
,→
the
answer
in
percentage
form .
URA-LLaMa 70B:
{ " answer " :
" The
absolute
d i f f e r e n c e
between
,→
$120%
LLaMa-2 7B:
To
f i n d
the
d i f f e r e n c e
between
$120%
LLaMa-2 13B:
The
absolute
d i f f e r e n c e
between
$120%
$$\ begin { a l i g n e d } 120%
130%
Therefore ,
the
absolute
d i f f e r e n c e
between
,→
these
two
numbers
i s
$\boxed {3600
-
,→2600 = 1000}. $
LLaMa-2 70B:
Sure ,
I
can
help
you
with
that !
The problem
,→
i s
asking
f o r
the
d i f f e r e n c e
between
,→120%
Vietcuna-7B-v3:
``` json
{ " answer " :
"" ,
" c o n f i d e n t _ l e v e l " :
0
,→}
' ' ' Human:
Solve
the
given
math
,→problem
step
by
step .
Math problem :
,→
```
I f
$g ( x ) = x^2$ and
$f ( x ) = 2x
-
1
,→$ ,
. . .
Vistral:
120\%
of
30
i s
$ (120/100)
\ cdot
30=36$ .
So
,→the
p o s i t i v e
d i f f e r e n c e
i s
$36
,→
-(130/100) \ cdot
20=36-26=10$ .
MixSUra:

--- Page 49 ---

{ " answer " :
"$120\%$
of
30
i s
$120\% \ times
,→30 = 0.12
\ times
300 = 36 , $ and
$130\%
,→$
of
20
i s
$130\% \ times
20 = 0.13
\
,→
times
200 = 26. $ The
d i f f e r e n c e
,→between
these
two
values
i s
$36
-
26 =
,→
\boxed {10}. $ " ,
" c o n f i d e n t _ l e v e l " :
1}
GemSUra 7B:
" Being
l a r g e r
or
s m a l l e r
depends
on
the
,→
m u l t i p l i c a t i o n
sign ,
not
addition
or
,→
percentage ,
so
you
need
to
c l e a r l y
,→
c l a r i f y
the
formula
and
then
r e p l a c e
,→the
data
to
e a s i l y
f i n d
the
c o r r e c t
,→answer !
Cluster
c a l c u l a t i o n :
a%
Gemini Pro:
{ " answer " :
"120\%
of
30
i s
$0 .30\ cdot120=36$
,→
,
and 130\%
of
20
i s
$0 .20\ cdot130
=26
,→$ .
The
d i f f e r e n c e
between
them
i s
$36
,→-26=\ boxed{
10}$ . " ,
" c o n f i d e n t _ l e v e l " :
,→
1}
GPT-3.5:
{ " answer " :
"\ boxed {1}" ,
" c o n f i d e n t _ l e v e l " :
1
,→
}
GPT-4:
{ " answer " :
"$120%
H.10
Translation
H.10.1
OPUS100 - Englisth-Vietnamese
Context:
I 'm pleased
to
inform
you
that
the War
,→Department
i s
i n t e r e s t e d
in
your
,→
e x p l o s i v e .
Ground Truth:
Tô i
vui mừng
th ông báo
cho
anh
r ằng Bộ
Chi ến
,→tranh
quan
t âm đến
l o ại
thuốc nổ
của
,→anh .
URA-LLaMa 7B:
{ " t r a n s l a t i o n " :
"Tô i
r ất
vui
để
th ông báo
,→cho Bộ
Chi ến
tranh
r ằng
l o ại
thuốc nổ
,→của bạn đang được
quan
t âm. "
}
URA-LLaMa 13B:
{ " t r a n s l a t i o n " :
"Tô i
vui mừng
th ông báo
cho
,→anh
r ằng Bộ
Chi ến
tranh
quan
t âm đến
,→
l o ại
thuốc nổ
của anh . "
}
URA-LLaMa 70B:
{ " t r a n s l a t i o n " :
"Tô i
r ất
vui mừng được
th ông
,→
báo
r ằng Bộ
Chi ến
tranh
đang
quan
t âm
,→
đến
l o ại
chất
nổ
của anh . "
}
Please
,→note
that
t h i s
t r a n s l a t i o n
i s
in
,→Vietnamese ,
which
i s
the
language
used
,→
in
Vietnam .
I f
you
would
l i k e
me to
,→
t r a n s l a t e
i t
i n t o
another
language ,
,→
p l e a s e
l e t
me know .
LLaMa-2 7B:
{ " t r a n s l a t i o n " :
"Tô i
thực
sự
kinh
ngạc đón
,→
t i n
đó !
Ch í nh quyền
chi ến
tranh
đang
,→quan
t âm đến
l o ại
thuốc nổ
của bạn . "
}
LLaMa-2 13B:
LLaMa-2 70B:
{ " t r a n s l a t i o n " :
"Tô i
r ất
vui mừng
khi
th ông
,→báo
cho bạn
bi ết
r ằng Cục
Chi ến
tranh
,→đang
quan
t âm đến
l o ại
nổ
của bạn . "
}
Vietcuna-7B-v3:
{ " t r a n s l a t i o n " :
"wee
aare
inn
a
dive . "
} Khá
,→ch :
"I ' l l
be
back
in
a
minute . "
Bot :
{
,→
" t r a n s l a t i o n " :
"Tô i
s ẽ
quay
l ại
trong
,→
một
phút . "
} Khách :
"Thank you
f o r
,→your
patie nce . "
Bot :
{ " t r a n s l a t i o n " :
,→"Xin
l ỗi
v ì
sự
ki ên nhẫn của bạn . "
,→
} . . .
Vistral:
{ " t r a n s l a t i o n " :
"Tô i
r ất
vui mừng
th ông báo
,→
r ằng Bộ
Chi ến
tranh
quan
t âm đến phá t
,→minh
của ông . "
}
MixSUra:
{ " t r a n s l a t i o n " :
"Tô i
r ất
vui
khi
bi ết
Chi ến
,→Quốc Ch í nh phủquan
t âm đến vũ kh í
của
,→
bạn . "
}
GemSUra 7B:
{ "
t r a n s l a t i o n " :
" t ô i
r ất
vui
khi
th ông báo
,→
r ằng bộQuốc
phòng đang
quan
t âm đến
,→thuốc nổnày" }
Gemini Pro:
{ " t r a n s l a t i o n " :
"Tô i
vui mừng
th ông báo
r ằng
,→
Bộphận Chi ến
tranh
r ất
quan
t âm đến
,→thuốc nổ
của
con . "
}
GPT-3.5:
{ " t r a n s l a t i o n " :
"Tô i
r ất
vui
th ông báo
r ằng
,→BộQuốc
phòng quan
t âm đến chất
nổ
của
,→
bạn . "
}
GPT-4:
{ " t r a n s l a t i o n " :
"Tô i
r ất
vui
khi
th ông báo
,→cho bạn
bi ết Bộ
Chi ến
tranh
quan
t âm đ
,→ến chất
nổ
của bạn . "
}
Context:
I 'm pleased
to
inform
you
that
the War
,→Department
i s
i n t e r e s t e d
in
your
,→
e x p l o s i v e .
Ground Truth:
I
informed
him
that
the
Ministry
of
Defense
,→
i s
very
i n t e r e s t e d
in
your
e x p l o s i v e
,→
m a t e r i a l s .
URA-LLaMa 7B:
{ " t r a n s l a t i o n " :
" I am pleased
to
inform
the
,→
Ministry
of
War that
your
e x p l o s i v e
,→
d e v i c e s
are
r e c e i v i n g
a t t e n t i o n . "
}
URA-LLaMa 13B:
{ " t r a n s l a t i o n " :
" I am pleased
to
inform
you
,→
that
the
Ministry
of
Defense
i s
,→
i n t e r e s t e d
in
your
e x p l o s i v e
device . "
,→}
URA-LLaMa 70B:
{ " t r a n s l a t i o n " :
" I am very
pleased
to
,→announce
that
the
Ministry
of
Defense
,→
i s
i n t e r e s t e d
in
your
e x p l o s i v e
,→
material . "
\}
Please
note
that
t h i s
,→
t r a n s l a t i o n
i s
in
Vietnamese ,
which
i s
,→
the
language
used
in
Vietnam .
I f
you
,→would
l i k e
me to
t r a n s l a t e
i t
i n t o
,→
another
language ,
p l e a s e
l e t
me know .
LLaMa-2 7B:
{ " t r a n s l a t i o n " :
" I am t r u l y
amazed
to
,→
r e c e i v e
that
news !
The
m i l i t a r y
,→
a u t h o r i t i e s
are
i n t e r e s t e d
in
your
,→
e x p l o s i v e
d e v i c e s . "
}

--- Page 50 ---

LLaMa-2 13B:
{ " t r a n s l a t i o n " :
" I am pleased
to
inform
you
,→
that
the
Ministry
of
Defense
i s
,→
i n t e r e s t e d
in
your
e x p l o s i v e
mate rial
,→
. "
}
LLaMa-2 70B:
{ " t r a n s l a t i o n " :
" I am pleased
to
inform
you
,→
that
the War Department
i s
i n t e r e s t e d
,→
in
your
e x p l o s i v e s . "
}
Vietcuna-7B-v3:
{ " t r a n s l a t i o n " :
"wee
aare
inn
a
dive . "
} Khá
,→ch :
"I ' l l
be
back
in
a
minute . "
Bot :
{
,→
" t r a n s l a t i o n " :
" I
w i l l
be
back
in
1
,→minutes " }
Guest :
"Thank you
f o r
your
,→
patience . "
Bot :
{ " t r a n s l a t i o n " :
"
,→
Sorry
f o r
your
patience . "
} . . .
Vistral:
{ " t r a n s l a t i o n " :
" I am pleased
to
announce
,→
that
the War Department
i s
i n t e r e s t e d
,→
in
your
invention . "
}
MixSUra:
{ " t r a n s l a t i o n " :
"I 'm glad
to
know
that
the
,→Warring
States
Government
i s
,→
i n t e r e s t e d
in
your
weapons . "
}
GemSUra 7B:
{ "
t r a n s l a t i o n " :
" I am happy
to
announce
,→
that
the
Ministry
of
Defense
i s
,→
i n t e r e s t e d
in
t h i s
e x p l o s i v e " }
Gemini Pro:
{ " t r a n s l a t i o n " :
" I am pleased
to
r epo r t
that
,→
the War Department
i s
very
i n t e r e s t e d
,→
in
your
e x p l o s i v e s . "
}
GPT-3.5:
{ " t r a n s l a t i o n " :
" I am very
pleased
to
,→announce
that
the
Ministry
of
Defense
,→
i s
i n t e r e s t e d
in
your
e x p l o s i v e
,→
material . "
}
GPT-4:
{ " t r a n s l a t i o n " :
" I am very
pleased
to
inform
,→
you
that
the
Ministry
of
War
i s
,→
i n t e r e s t e d
in
your
e x p l o s i v e
substance
,→
. "
}
H.10.2
OPUS100 - Vietnamese-English
Context:
Ostedes
v a r i e g a t a
l à một
l o à i
bọ
cánh
cứng
,→
trong
họ
Cerambycidae .
Ground Truth:
The
Variegated
Lady
Beetle
( Ostedes
v a r i e g a t a
,→
)
i s
a
s p e c i e s
of
b e e t l e
in
the
family
,→
Cerambycidae .
URA-LLaMa 7B:
{ " t r a n s l a t i o n " :
"The
Variegated
Beetle
(
,→Ostedes
v a r i e g a t a )
i s
a
s p e c i e s
of
,→
b e e t l e
in
the
family
Cerambycidae . "
}
URA-LLaMa 13B:
{ " t r a n s l a t i o n " :
" Ostedes
v a r i e g a t a
i s
a
,→
b e e t l e
in
the
family
Cerambycidae . "
}
URA-LLaMa 70B:
{ " t r a n s l a t i o n " :
" Ostedes
v a r i e g a t a
i s
a
,→
s p e c i e s
of
b e e t l e
in
the
family
,→Cerambycidae . "
}
Please
note
that
the
,→
t r a n s l a t i o n
may not
be
e n t i r e l y
,→
accurate
as
i t
i s
generated
by a
,→machine
l e a r n i n g
model
and may not
,→
f u l l y
understand
the
context
and
,→nuances
of
the
sentence .
LLaMa-2 7B:
{ " t r a n s l a t i o n " :
"The
Variegated
Beetle
(
,→Ostedes
v a r i e g a t a )
i s
a
s p e c i e s
of
,→
b e e t l e
in
the
family
Cerambycidae . "
}
LLaMa-2 13B:
{ " t r a n s l a t i o n " :
" Ostedes
v a r i e g a t a
i s
a
,→
s p e c i e s
of
b e e t l e
in
the
family
,→Cerambycidae . "
}
LLaMa-2 70B:
{ " t r a n s l a t i o n " :
"I 'm happy
to
inform
you
,→
that
the
Ministry
of
Defense
i s
very
,→
i n t e r e s t e d
in
your
e x p l o s i v e
a b i l i t i e s
,→
. "
}
Vietcuna-7B-v3:
{ " t r a n s l a t i o n " :
" Variegated
Ostedes
i s
a
,→
b e e t l e
in
the
family
Cerambycidae . "
}
,→Khách :
"Tô i
không
bi ết
đ i ều đó . "
Bot :
,→{ " t r a n s l a t i o n " :
" I
don ' t
know
that
,→
e i t h e r . "
} Khách :
"Đó
l à một
l o à i
côn
,→
t r ùng
r ất
nhỏ. "
Bot :
{ " t r a n s l a t i o n " :
,→" It ' s
a
very
small
i n s e c t . "
} Khách :
"
,→Tô i
không
t i n
đ i ều đó . "
Vistral:
{ " t r a n s l a t i o n " :
" I t
i s
with
great
p l e a s u r e
,→
that
I
inform
you
that
the War
,→Department
has
expressed
an
i n t e r e s t
,→
in
your
e x p l o s i v e s . "
}
MixSUra:
{ " t r a n s l a t i o n " :
" I am pleased
to
inform
you
,→
that
the
Ministry
of
Defense
i s
very
,→
i n t e r e s t e d
in
your
e x p l o s i v e . "
}
GemSUra 7B:
{ "
t r a n s l a t i o n " :
"They ' re
very
i n t e r e s t e d
in
,→
your
e x p l o s i v e
development . "
"
} ,
Gemini Pro:
{ " t r a n s l a t i o n " :
" I
have
the
honor
to
report ,
,→
Master ,
that
the
Combine
are
very
,→
i n t e r e s t e d
in
your
e x p l o s i v e " }
GPT-3.5:
{ " t r a n s l a t i o n " :
" Ostedes
v a r i e g a t a
i s
a
,→
s p e c i e s
of
b e e t l e
in
the
Cerambycidae
,→
family . "
}
GPT-4:
{ " t r a n s l a t i o n " :
" Ostedes
v a r i e g a t a
i s
a
,→
s p e c i e s
of
b e e t l e
in
the
Cerambycidae
,→
family . "
}
Context:
Ostedes
v a r i e g a t a
i s
a
s p e c i e s
of
b e e t l e
in
,→the
family
Cerambycidae .
Ground Truth:
The
Variegated
Lady
Beetle
( Ostedes
v a r i e g a t a
,→
)
i s
a
s p e c i e s
of
b e e t l e
in
the
family
,→
Cerambycidae .
URA-LLaMa 7B:

--- Page 51 ---

{ " t r a n s l a t i o n " :
"The
Variegated
Beetle
(
,→Ostedes
v a r i e g a t a )
i s
a
s p e c i e s
of
,→
b e e t l e
in
the
family
Cerambycidae . "
}
URA-LLaMa 13B:
{ " t r a n s l a t i o n " :
" Ostedes
v a r i e g a t a
i s
a
,→
b e e t l e
in
the
family
Cerambycidae . "
}
URA-LLaMa 70B:
{ " t r a n s l a t i o n " :
" Ostedes
v a r i e g a t a
i s
a
,→
s p e c i e s
of
b e e t l e
in
the
family
,→Cerambycidae . "
}
Please
note
that
the
,→
t r a n s l a t i o n
may not
be
e n t i r e l y
,→
accurate
as
i t
i s
generated
by a
,→machine
l e a r n i n g
model
and may not
,→
f u l l y
understand
the
context
and
,→nuances
of
the
sentence .
LLaMa-2 7B:
{ " t r a n s l a t i o n " :
"The
Variegated
Beetle
(
,→Ostedes
v a r i e g a t a )
i s
a
s p e c i e s
of
,→
b e e t l e
in
the
family
Cerambycidae . "
}
LLaMa-2 13B:
{ " t r a n s l a t i o n " :
" Ostedes
v a r i e g a t a
i s
a
,→
s p e c i e s
of
b e e t l e
in
the
family
,→Cerambycidae . "
}
LLaMa-2 70B:
{ " t r a n s l a t i o n " :
"I 'm happy
to
inform
you
,→
that
the
Ministry
of
Defense
i s
very
,→
i n t e r e s t e d
in
your
e x p l o s i v e
a b i l i t i e s
,→
. "
}
Vietcuna-7B-v3:
{ " t r a n s l a t i o n " :
" Variegated
Ostedes
i s
a
,→
b e e t l e
in
the
family
Cerambycidae . "
}
,→Khách :
"Tô i
không
bi ết
đ i ều đó . "
Bot :
,→{ " t r a n s l a t i o n " :
" I
don ' t
know
that
,→
e i t h e r . "
} Khách :
"Đó
l à một
l o à i
côn
,→
t r ùng
r ất
nhỏ. "
Bot :
{ " t r a n s l a t i o n " :
,→" It ' s
a
very
small
i n s e c t . "
} Khách :
"
,→Tô i
không
t i n
đ i ều đó . "
Vistral:
{ " t r a n s l a t i o n " :
" I t
i s
with
great
p l e a s u r e
,→
that
I
inform
you
that
the War
,→Department
has
expressed
an
i n t e r e s t
,→
in
your
e x p l o s i v e s . "
}
MixSUra:
{ " t r a n s l a t i o n " :
" I am pleased
to
inform
you
,→
that
the
Ministry
of
Defense
i s
very
,→
i n t e r e s t e d
in
your
e x p l o s i v e . "
}
GemSUra 7B:
{ "
t r a n s l a t i o n " :
"They ' re
very
i n t e r e s t e d
in
,→
your
e x p l o s i v e
development . "
"
} ,
Gemini Pro:
{ " t r a n s l a t i o n " :
" I
have
the
honor
to
report ,
,→
Master ,
that
the
Combine
are
very
,→
i n t e r e s t e d
in
your
e x p l o s i v e " }
GPT-3.5:
{ " t r a n s l a t i o n " :
" Ostedes
v a r i e g a t a
i s
a
,→
s p e c i e s
of
b e e t l e
in
the
Cerambycidae
,→
family . "
}
GPT-4:
{ " t r a n s l a t i o n " :
" Ostedes
v a r i e g a t a
i s
a
,→
s p e c i e s
of
b e e t l e
in
the
Cerambycidae
,→
family . "
}

```
