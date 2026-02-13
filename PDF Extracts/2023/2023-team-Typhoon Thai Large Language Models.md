---
title: "2023-team-Typhoon Thai Large Language Models - PDF Extract"
source_pdf: "2023-team-Typhoon Thai Large Language Models.pdf"
pages: 12
extracted_at: "2026-02-13T09:50:28.417241"
---

# PDF Extract: 2023-team-Typhoon Thai Large Language Models

**Source PDF:** 2023-team-Typhoon Thai Large Language Models.pdf
**Total Pages:** 12

---

## Content

```
--- Page 1 ---

Typhoon: Thai Large Language Models
Kunat Pipatanakul, Phatrasek Jirabovonvisut, Potsawee Manakul
Sittipong Sripaisarnmongkol, Ruangsak Patomwong
Pathomporn Chokchainant, Kasima Tharnpipitchai
SCB 10X
Abstract
Typhoon is a series of Thai large language models (LLMs) developed specifically
for the Thai language. This technical report presents challenges and insights
in developing Thai LLMs, including data preparation, pretraining, instruction-
tuning, and evaluation. As one of the challenges of low-resource languages is the
amount of pretraining data, we apply continual training to transfer existing world
knowledge from a strong LLM. To evaluate the Thai knowledge encapsulated
in each model from the pretraining stage, we develop ThaiExam, a benchmark
based on examinations for high-school students and investment professionals in
Thailand. In addition, we fine-tune Typhoon to follow Thai instructions, and we
evaluate instruction-tuned models on Thai instruction datasets as well as translation,
summarization, and question-answering tasks. Experimental results on a suite of
Thai benchmarks show that Typhoon outperforms all open-source Thai language
models, and its performance is on par with GPT-3.5 in Thai while having only 7
billion parameters and being 2.62 times more efficient in tokenizing Thai text.
Model Weights: https://huggingface.co/scb10x/typhoon-7b
1
Introduction
Large Language Models (LLMs) have demonstrated strong zero-shot or few-shot capabilities on
a wide range of natural language processing (NLP) tasks [6, 55]. These LLMs are auto-regressive
transformers, which are pretrained on a large quantity of self-supervised text data. Most of the
major large language models (LLMs) such as GPT-2/3/4 [45, 6, 35], Llama-1/2 [54, 55], Falcon [40],
Mistral [16], are pretrained primarily on English-centric corpora. In addition, LLMs have been
pretrained on specific languages or domains such as Chinese [61], finance [59], or code [48].
Given a large number of low-resource languages, multilingual language models have been developed
by pretraining a single model on multiple languages. For example, XGLM [23] is trained on the
CC100 XL corpus, which consists of 30 diverse languages and includes around 11 billion Thai
tokens. mT5 [60], a model with an encoder-decoder architecture, is trained on MC4, which covers
101 languages and includes around 11 billion Thai tokens (or 1.14% of mT5 pretraining data).
BLOOM [58], the largest open-source multilingual model with 176 billion parameters, is trained on
46 natural languages (which do not cover Thai) and 13 programming languages. In contrast to high-
coverage multilingual LLMs, there exist multilingual LLMs specialized in Southeast Asian (SEA)
languages such as Indonesian, Malay, Thai, Vietnamese, and Filipino. For example, SEA-LION [51]
is a series of multilingual LLMs of different sizes, focusing on SEA languages. However, SEA
languages only account for 13% of the pretraining data of SEA-LION, of which an even smaller part
is Thai. Similarly, SeaLLM [31] is another series of LLMs focusing on SEA languages. SeaLLMs are
developed by continuing pre-training Llama2 with an extended vocabulary and specialized instruction
arXiv:2312.13951v1  [cs.CL]  21 Dec 2023

--- Page 2 ---

ONET
IC
TGAT
TPAT-1
A-Level
0
10
20
30
40
50
60
70
80
Accuracy (%)
ThaiExam (Multiple-choice Exams)
Typhoon-7B
SeaLLM-7B-Chat
OpenThaiGPT-beta-7B
WangChanGLM
SEA-LION-7B
ChatGPT
TH-AlpacaEval
TH-OASST
TH-MT-Bench
TH-Sea-bench
0
10
20
30
40
50
60
Score (judged by GPT-4)
Thai Instruction-Following (wrt ChatGPT)
Typhoon-7B-Instruct
SeaLLM-7B-Chat
OpenThaiGPT-beta-7B
WangChanGLM
ChatGPT
Figure 1: Performance of Typhoon and other open-source Thai large language models on Thai Exam-
inations (left) and Thai instruction-following (right). Details about ThaiExam and Thai instruction-
following evaluation are provided in Section 3.4, and Section 4.2, respectively.
and alignment tuning. In the pretraining data, Thai text accounts for about 5.91%. Due to the limited
amount of Thai data in pretraining these multilingual models, we argue that they may not have rich
Thai knowledge, or understand cultural norms, customs, and stylistic preferences.
The Thai language is spoken by more than 70 million people, but it has received less attention
from the NLP community. For instance, the Thai language represents only a small portion of most
standard pretraining data. For example, the Thai language constitutes less than 0.5% of the Common
Crawl data [13], making Thai the 26th rank in terms of size in Common Crawl. The Thai language
has its own alphabet, which does not overlap with any other high-resource languages. As a result,
despite the success of general and multilingual LLMs, we argue that these LLMs may still lack some
understanding of Thai culture and knowledge. Therefore, this work focuses on developing LLMs
specifically for the Thai language. We hypothesize that a strong LLM can be adapted to the Thai
language by pretraining a strong LLM further on a moderately sized Thai corpus.
To this end, this work introduces Typhoon, a 7-billion parameter language model, where its first
version is adapted from Mistral-7B [16]. To assess the extent of Thai knowledge encapsulated within
a language model, we develop ThaiExam – an evaluation benchmark based on Thai examinations.
Furthermore, we study fine-tuning Typhoon to follow Thai instructions. We compare instruction-
tuned models on both Thai and translated instruction-following datasets, and we also test their
zero-shot abilities on machine translation, abstractive summarization, and question-answering tasks.
As demonstrated in Figure 1, the evaluation on various benchmarks shows that Typhoon is the
state-of-the-art open-source Thai large language model. Ultimately, this work not only shares our
insights from developing Thai large language models but also makes Typhoon publicly available
under the Apache-2.0 license to promote further development.
2
Related Work
Training language models on monolingual data (as well as bilingual data where the target language
and English data are mixed) has demonstrated gains over multilingual models in both predictive
and generative modelling tasks [28, 30, 49, 29, 41, 50]. For Thai, WangChangBERTa [26], an
encoder-only model, was the first transformer-based model to be trained on large-scale Thai data.
However, as an encoder-only model, WangChangBERTa cannot perform text generation.
Two open-source Thai generative large language models have also recently been developed.
First, WangChanGLM [42] is based on multilingual XGLM [23] with 7.5 billion parameters.
WangChanGLM is adapted to Thai by fine-tuning XGLM using LoRA [15] on translated instruction-
following datasets of around 380k instruction-response pairs. However, WangChanGLM is not
further pretrained on Thai data, so its Thai knowledge is expected to be limited to the pretraining
stage of XGLM. Second, OpenThaiGPT (openthaigpt-1.0.0-beta-7b) [36] is based on Llama2 [55]
with 7 billion parameters. Its tokenizer extends Llama2’s tokenizer to include 24,554 additional
Thai tokens to improve generation efficiency. OpenThaiGPT continues pre-training Llama2 on Thai
data and performs instruction fine-tuning on the translated instruction datasets. Although the model
weights are released to the public, to the best of our knowledge, further details are not publicly
2

--- Page 3 ---

available. Additionally, the vanilla Llama2 model may not be able to generate Thai responses, but it
can understand Thai to a certain extent (which is shown in our results in Table 3) due to cross-lingual
transferability and the presence of some Thai data during its pretraining. In Table 1, we summarize
open-source generative LLMs that are investigated in this work.
ChatGPT and GPT-4 [35] are proprietary language model based products that support a variety
of languages including Thai. GPT-4 is the state-of-the-art in several English benchmarks [20, 63].
In addition, given the speculated larger amount of pretraining data than any open-source models,
ChatGPT and GPT-4 can also be exceptional in low-resource languages.
Model
MajorLang
#Params
VocabSize
Context
BaseModel
Typhoon-7B
English, Thai
7B
35,219
4096
Mistral
OpenThaiGPT-beta-7B
English, Thai
7B
56,554
4096
Llama2
WangChanGLM
Multilingual
7.5B
256,008
2048
XGLM
SeaLLM-7B
Multilingual
7B
48,512
4096
Llama2
SEA-LION-7B
Multilingual
7B
256,000
2048
✗
Table 1: Comparison between Typhoon and open-source language models that support Thai.
OpenThaiGPT is based on Llama2 with an extended vocabulary, continual pretraining, and in-
struction fine-tuning. WangChanGLM is a multi-lingual XGLM model fine-tuned to follow Thai
instructions without further pretraining. SEA-LION and SeaLLM are multilingual models specialized
in Southeast Asian languages, including Thai. At the time of writing, SEA-LION is only instruction-
tuned on Indonesian data, and SeaLLM is only available at 7B size.
3
Pretraining
The development of language models tailored to the Thai language presents several unique challenges.
Unlike high-resource languages like English, Thai does not have readily available large-scale datasets
and resources. This section provides an overview of the challenges and considerations specific to
developing Thai LLMs, including data preparation, tokenization, and the choices of base model.
3.1
Pretraining Data
In the context of the Thai language, a notable observation emerges: the available Thai internet data
constitutes only a small fraction, for instance, less than 0.5% in the Common Crawl data [13]. In
addition to the quantity, our initial investigation reveals that there is an issue with the quality where a
large portion of crawled Thai texts are search engine optimization (SEO) texts or duplication.
Publicly Available Data
In this work, we consider two primary sources of publicly available Thai data sources as follows.
First, MC4 [60], a multilingual cleaned version of Common Crawl’s web crawl corpus, consists of
texts from 108 languages including Thai. For example, mT5 [60] previously used 11 billion Thai
tokens in this dataset in its pretraining. Our investigation shows that the quality of MC4 data is
higher than Oscar. Second, Oscar [37], an open-source multilingual dataset, consists of texts from
151 languages including Thai. The Oscar dataset is larger than MC4, however, we observe that its
quality is lower, which necessitates extensive data-cleaning efforts.
Methodology
Given the available resources for pretraining Thai language models, our approach focuses on two key
aspects: quantity and quality. In terms of the quantity of data, as the Oscar dataset extracted a single
package of the Common Crawl (CC) data and MC4 only made use of a few packages, it is possible to
extract more Thai data from the remaining packages of the CC data. In terms of quality, we follow
the methodology employed in Falcon RefinedWeb [40] and apply a deduplication pipeline on Thai
data in CC datasets.
Our data preparation can be summarized in four key steps. (1) Scaling the Data: we initiate the
process by increasing the number of Common Crawl packages where we process a total of 40 packs of
3

--- Page 4 ---

the CC data, resulting in a substantially larger dataset comprising approximately 3 TB of Thai text. (2)
Strict Deduplication: to ensure data quality and minimize redundancy, we implement a deduplication
method based on MinHash and LSH algorithms. (3) Rule-based and Heuristic Filtering: heuristics
are applied to filter data to further enhance data quality. This step involves a manual selection
of high-quality websites at the domain level, supplemented by heuristic criteria such as character
ratio, line length, and document length. (4) Incorporating English Data: to mitigate catastrophic
forgetting of the base model’s English knowledge [47, 27], we add data randomly selected from
Falcon RefinedWeb [40] to our Thai data, resulting in a bilingual dataset with a 50/50 split between
Thai and English data. Note that previous work in adapting an LLM to Hungarian shows that mixing
English data can mitigate catastrophic forgetting on English, and the adaption is not sensitive to the
exact mixture ratio provided that the original language and target language are included [11].
3.2
Thai Tokenizer
A byte-level BPE tokenizer, which is adopted by Mistral as well as other LLMs such as GPT or Llama,
can encode most words or characters in all languages by falling back to the byte level. Although
this tokenizer can operate on a language that it is not initially trained for (e.g., Thai), it has poor
efficiency. For instance, previous work shows that the GPT-2 tokenizer with a vocabulary size of
50k requires 3.8 times more tokens to encode Thai texts compared to a tokenizer with a vocabulary
size of 5k trained on Thai data [11]. To adapt an existing LLM, the tokenizer of the original model
is usually augmented with new tokens where the corresponding embeddings are initialized from
scratch [36, 11]. This results in the trade-off between an improvement in efficiency and the difficulty
of model adaption due to new embeddings. Previous work demonstrated that adding beyond 5,000
new Thai tokens yields a diminishing return in efficiency [11].
In this work, we base our tokenizer on Mistral-7B tokenizer, but we further train an additional Thai
subword tokenizer with 5,000 tokens and integrate it with the original tokenizer. This new tokenizer
is created by training a SentencePiece model [17] on around 8 million samples randomly selected
from the Thai subset of MC4 data [60]. We define efficiency as the number of tokens required to
represent Thai text with respect to the number of GPT-4 tokens on the same text, i.e.,
Efficiency = #tokenmodel
#tokenGPT-4
(1)
where #token is the number of tokens on the same Thai text. Our experimental results in Table 2
show that Typhoon’s tokenizer is 2.62 times more efficient than GPT-4.
Tokenizer
Typhoon
GPT-4
Mistral
Character
Word*
OpenThaiGPT
WangChanGLM
Efficiency
262%
100%
93%
89%
326%
350%
305%
Table 2: Token efficiency with respect to GPT-4. *Based on the newmm tokenizer.
3.3
Pretraining Details
Initial Experiments
In the initial experiments, we explore various training techniques and base models on a subset of
pretrained data, comprising approximately 500 million tokens. We investigate the following options:
• Base Model: We compare base models, including Llama2-7B, Llama2-13B [55], CodeLlama-
34B [48], and Mistral-7B [16] where our criterion is the perplexity. This investigation shows that
Mistral-7B achieves the lowest perplexity. Therefore, Mistral-7B is selected as our base model. Note
that we perform training on the embeddings and the language modeling head only.
• Training Strategy: We compare Low-Rank Adaption (LoRA) [15] and full-weight training on
Mistral-7B. Our experiments demonstrate that LoRA yields a lower final loss. Additionally, we tried a
two-stage training approach where the embeddings are first trained on full-weight followed by LoRA.
However, this setting did not show a significant improvement over using LoRA from the beginning.
• Batch size: We observed an instability in the training loss when using a batch size of 500k tokens,
and we empirically found that increasing the batch size to 2 million tokens can stabilize training.
4

--- Page 5 ---

Final Model
Based on the initial experiments, we continue pretraining the extended embeddings and the language
modelling head of Mistral-7B using LoRA. We use the AdamW optimizer [25] with a cosine
scheduled learning rate initialized at 4e-4. We apply gradient clipping with a threshold of 1.0.
3.4
Evaluation: Thai Knowledge of Pretrained Models
The NLP community has developed and released challenging, diverse, and holistic benchmarks such
as BIG-bench [4] and HELM [21]. However, most of these benchmarks focus only on performance
in English. Although non-English benchmarks have been proposed, they are still lacking in number
[1, 3, 62], and only some of these non-English benchmarks such as BHASA [19] include Thai.
Nevertheless, the evaluation datasets in BHASA are still based on multi-lingual datasets or publicly
available Thai datasets at a limited scale. To better evaluate the Thai culture and languages of LLMs,
we develop ThaiExam, a benchmark comprising Thai multiple-choice examinations as follows:
• ONET: The Ordinary National Educational Test (ONET) is an examination for students in Thailand.
We select the grade-12 ONET exam, which comprises 5 subjects and each question has 5 choices.
These subjects are Thai, English, Mathematics, Social Studies, and Science. We extracted these
questions from the official 2021 ONET example, amounting to a total of 170 questions and options.
• IC: The Investment Consultant (IC) examination, a licensing test for investment professionals in
Thailand developed by the Stock Exchange of Thailand (SET), features 4 choices per question. We
extracted questions for levels 1, 2, and 3 from the official SET website, resulting in a total of 95
questions and options.
• TGAT: The Thai General Aptitude Test (TGAT), a national high school examination in Thailand,
focuses on critical and logical thinking skills, as well as proficiency in the English language. We
collected a total of 90 questions and answers. The TGAT consists of four choices per question.
• TPAT-1: The Thai Professional Aptitude Test 1 (TPAT-1) is a national high school examination
in Thailand that assesses students’ professional skills requirement in medical schools. This subset
contains reasoning and medical ethics. We collected a total of 116 questions and answers. The
TPAT-1 consists of 5 choices per question.
• A-Level: An academic knowledge assessment examination (Applied Knowledge Level) that covers
general foundational subjects taught in schools. The content assessed in this examination aligns with
the curriculum guidelines and emphasizes the practical application of knowledge in daily life. We
collected a total of 175 questions and answers.
In addition to ThaiExam, we use existing datasets including XNLI (a cross-lingual textual entail-
ment dataset) [8], XCOPA (a multilingual dataset for causal commonsense reasoning) [43], and
M3Exam [62] (a benchmark developed for evaluating LLMs in a multilingual, multimodal, and
multilevel context). The Thai subset of M3Exam is sourced from three levels of ONET: low (grade
6), medium (grade 9), and high (grade 12).
Model
ThaiExam
Others
ONET
IC
TGAT TPAT-1 A-Level Average M3Exam
XNLI
XCOPA
Typhoon-7B
0.379
0.393
0.700
0.414
0.324
0.442
0.391
0.421
0.742
SeaLLM-7B
0.342
0.256
0.589
0.336
0.305
0.366
0.285
0.401
0.586
OpenThaiGPT-beta-7B
0.180
0.278
0.411
0.319
0.243
0.286
0.259
0.374
0.570
WangChanGLM
0.192
0.271
0.167
0.172
0.175
0.195
0.219
0.431
0.500
SEA-LION-7B
0.179
0.290
0.244
0.198
0.175
0.217
0.230
0.377
0.462
Llama2-13B
0.248
0.241
0.500
0.267
0.273
0.306
0.230
0.366
0.512
GPT-3.5-turbo-0613
0.416
0.444
0.689
0.397
0.355
0.460
0.341†
0.447
0.630
GPT-4-0613
0.531
0.658
0.767
0.491
0.564
0.602
0.560†
0.623‡
0.920
Avg. Human [32, 33, 34]
0.318
-
0.472
0.406
-
-
-
-
-
Table 3: Performance on the Thai reasoning and understanding tasks. †The results are reported in the
previous work [62]. ‡The experiment was conducted on a subset of XNLI as a full evaluation would
cost more than $1000.
5

--- Page 6 ---

In Table 3, we compare our pre-trained Typhoon against open-source and proprietary LLMs that
support the Thai language. The results show that Typhoon-7B is the best-performing model among all
open-source models across the evaluation datasets. Typhoon-7B also outperforms an average human
tester on ONET, TGAT and TPAT-1 examinations. When compared to proprietary (and potentially
much larger) models, Typhoon despite having only 7 billion parameters outperforms GPT-3.5 on 4
out of 8 evaluation datasets.
4
Instruction-Tuning
Although pretrained language models are highly capable of predicting the next words, even large
language models of more than 100 billion parameters may still lack the ability to follow a user’s
intent well. As a result, instruction-tuning has been applied to align language models with a user’s
intent [38, 53, 55]. Instruction-tuning or fine-tuning methods could be categorized into supervised
fine-tuning (SFT) and alignment via reinforcement learning using human feedback (RLHF) [52, 38]
or AI feedback (RLAIF) [18], and Direct Preference Optimization (DPO) [46]. However, these
techniques require significant annotation resources, which do not yet exist in the Thai language.
4.1
Supervised Fine-Tuning (SFT)
To address the lack of instruction-tuning data, we consider three directions as follows: (1) translating
English instruction-tuning datasets into Thai, (2) converting Thai NLP datasets using pre-defined
prompt templates similar to the FLAN collection [57, 7], (3) generating Thai instruction-tuning data
using the Self-Instruct technique [56].
As a first step, we create SFT data by translating English instruction-following datasets into Thai. The
translation-based approach was also previously used in fine-tuning WangChanGLM where datasets
such as Alpaca [53] and Dolly [9] were translated using Google Translate API. In this work, we
investigate translation further by using Typhoon fine-tuned for translation and GPT-4; for example,
we translate UltraChat [12] using GPT-4. Additionally, we follow self-instruct [56] in generating a
Thai-instruction dataset. Using translated and self-instruct data, we obtain Typhoon-7B-Instruct by
performing supervised fine-tuning.
4.2
Evaluation: Instruction-Following Tasks
In Section 3.4, we evaluate Thai knowledge using multi-choice question answering and classification
benchmarks. However, the previous evaluation may not reflect how well the models understand human
intents, and the evaluation of instruction-following models typically requires human interactions [20].
Therefore, we perform instruction-following evaluation using the following datasets:
• Thai AlpacaEval: We create an instruction-following dataset following AlpacaEval [20]. As
native Thai speakers, we manually write prompts in Thai based on the examples randomly selected in
AlpacaEval. For instance, given an example from AlpacaEval, we write a prompt in Thai as well as
using a Thai context instead of a literal translation. This dataset consists of 105 Thai prompts.
• Thai OASST: We make use of a Thai subset of OpenAssistant (OASST1), 166 human-written
instruction-response pairs, which was previously used in evaluating WangChanGLM.
• Translated MT-Bench: We translate MT-Bench [63] (using Google API) into Thai and we filter
out poorly translated examples such as coding instructions, resulting in a total of 68 examples. The
translated MT-Bench is used to evaluate the multi-turn ability of the models.
• Sea-bench (Thai subset) [31]: We make use of a Thai subset of Sea-bench inspired by MT-Bench
for SEA languages released with SeaLLM. It utilizes translations of English test sets, real user
questions from local sources, math and reasoning questions, and linguist-written instructions. Sea-
bench encompasses various categories, including task-solving, math-reasoning, general instructions,
NaturalQA for colloquial language, and safety instructions. This dataset consists of 100 Thai prompts.
We use an LLM as a judge to perform pairwise comparison [20, 63, 24] by measuring the fraction
of times the LLM judge (e.g., GPT-4) prefers the responses from the model being assessed over the
responses from a reference model. The LLM judge compares each pair twice in a symmetric manner,
6

--- Page 7 ---

and if the outputs of the LLM judge are not the same, it is treated as a draw, i.e., the model being
evaluated gets a score of 0.5 (tie). Otherwise, the model either gets a score of 0.0 (loss) or 1.0 (win).
In this experiment, we use GPT-4 (gpt-4-1106) as the LLM judge, and the reference model is GPT-3.5
(gpt-3.5-turbo-0613) as the reference model such that it would obtain a score of 0.50. For single-turn
evaluation sets (e.g., Thai-Alpaca, Thai-OASST, and Sea-bench), we follow the LLM-judge prompt
adopted by AlpacaEval.1 For multi-turn evaluation sets (e.g., translated MT-Bench), we follow the
LLM-judge prompt adopted in FastChat.2
Model
AlpacaEval
OASST
MT-Bench
Sea-bench
Typhoon-7B-Instruct
49.05
35.54
55.52
27.25
SeaLLM-7B-Chat
31.43
28.01
36.03
25.00
OpenThaiGPT-beta-7B
20.24
13.55
27.94
9.00
WangChanGLM
7.62
6.33
19.49
2.50
Table 4: Instruction-following evaluation (Score in %) based on Thai AlpacaEval, Thai OASST,
translated MT-Bench and Sea-bench. Each model is compared against GPT-3.5 using GPT-4 as the
judge, and the metric is win-rate defined as the number of times that the judge prefers the responses
from the model over the responses from the reference model using symmetric pairwise comparison.
In Table 4, we compare Typhoon-7B-Instruct against other instruction-following models. At the time
of conducting the experiments, SEA-LION is only instruction-tuned in Indonesian. GPT-3.5 is used as
a reference model and GPT-4 is used as a judge, and hence are not shown in Table 4. Our experimental
results show that Typhoon-7B-Instruct is comparable to GPT-3.5 on Thai AlpacaEval and translated
MT-Bench but it is worse on Thai OASST and Sea-bench. When compared to open-source Thai LLMs,
Typhoon-7B-Instruct achieves state-of-the-art performance on all instruction-following datasets.
4.3
Evaluation: Translation, Summarization, Question-Answering
In addition to instruction-tuning evaluation with an LLM judge, we evaluate the LLMs on standard
Natural Language Processing (NLP) tasks, including machine translation, abstractive summarization,
and question-answering. Here, we investigate the zero-shot abilities of Thai LLMs. First, we
evaluate the English-to-Thai machine translation performance on FLORES-200 [10]. Second, we
evaluate the abstractive summarization performance on XLSum (Thai article →Thai summary) [14]
and CrossSum (English article →Thai summary) [5]. Third, we evaluate the question-answering
performance on XQuAD (i.e., reading comprehension task) [2]. Our experimental results in Table 5
show that Typhoon-7B-Instruct is the best-performing system on most of the NLP tasks investigated.
Model
Translation
Summarization
Question-Answering
FLORES-200
XLSum(Th→Th)
CrossSum(En→Th)
XQuAD (Th)
Typhoon-7B-Instruct
31.14/46.62
21.60/4.24/14.51
17.32/3.83/11.39
34.46/54.03
SeaLLM-7B-Chat
14.36/37.13
10.21/1.72/7.96
15.66/2.33/10.58
20.89/47.95
OpenThaiGPT-beta-7B
27.68/44.41
17.98/1.93/12.69
17.72/3.06/11.28
34.58/40.82
WangChanGLM
10.63/31.78
19.10/2.10/13.77
22.91/3.76/15.61
17.81/19.94
Table 5: Zero-shot performance on NLP tasks. Machine translation is evaluated on FLORES-200
using BLEU [39] and chrF [44]. Summarization is evaluated on XLSum (Thai-to-Thai) and CrossSum
(English-to-Thai) using ROUGE-1/2/L [22] with the newmm tokenizer. Question-Answering is
evaluated on XQuAD using word-overlap F1 metric in 0-shot and 1-shot settings, respectively.
1https://github.com/tatsu-lab/alpaca_eval/blob/main/src/alpaca_eval/evaluators_
configs/chatgpt/basic_prompt.txt
2https://github.com/lm-sys/FastChat/blob/main/fastchat/llm_judge/data/judge_
prompts.jsonl
7

--- Page 8 ---

5
Risk and Limitations
Similar to other language models, Typhoon may (i) hallucinate, e.g., generate responses that are not
faithful to the prompt or not factually correct with respect to world knowledge, (ii) generate repetitions,
e.g., repeated words, phrases or sentences, (iii) produce harmful or inappropriate responses.
6
Conclusion and Future Work
Our work on Typhoon, a Thai large language model with 7 billion parameters, demonstrates that we
can adapt an existing English-centric LLM to Thai using only a subset of Thai data that we currently
have. Typhoon is the state-of-the-art open-source model on Thai benchmarks as well as achieving
performance on par with GPT-3.5 in Thai while being 2.62 times more efficient in tokenization.
Future work will extend pretraining to utilize a larger amount of Thai data that is available, and use
larger base models such as 34B, 70B, or mixture-of-experts to exploit the emergent ability. Also,
future work will investigate instruction tuning further for an improved alignment.
Acknowledgements
We would like to thank Mukaya Panich, Tanwa Arpornthip, Unnawut Leepaisalsuwanna, and Panuwat
Chayabunjonglerd for their advice on this project. We would like to thank the SCBX R&D team for
their support with the evaluation. We would also like to thank Sarana Nutanong and the NLP team at
VISTEC for their feedback on the experiments and this technical report.
References
[1] Kabir Ahuja, Rishav Hada, Millicent Ochieng, Prachi Jain, Harshita Diddee, Samuel Maina,
Tanuja Ganu, Sameer Segal, Maxamed Axmed, Kalika Bali, et al. Mega: Multilingual evaluation
of generative ai. arXiv preprint arXiv:2303.12528, 2023.
[2] Mikel Artetxe, Sebastian Ruder, and Dani Yogatama. On the cross-lingual transferability of
monolingual representations. In Proceedings of the 58th Annual Meeting of the Association for
Computational Linguistics, pages 4623–4637, Online, July 2020. Association for Computational
Linguistics.
[3] Yejin Bang, Samuel Cahyawijaya, Nayeon Lee, Wenliang Dai, Dan Su, Bryan Wilie, Holy
Lovenia, Ziwei Ji, Tiezheng Yu, Willy Chung, Quyet V. Do, Yan Xu, and Pascale Fung. A
multitask, multilingual, multimodal evaluation of chatgpt on reasoning, hallucination, and
interactivity. arXiv preprint arXiv:2302.04023, 2023.
[4] BIG bench authors. Beyond the imitation game: Quantifying and extrapolating the capabilities
of language models. Transactions on Machine Learning Research, 2023.
[5] Abhik Bhattacharjee, Tahmid Hasan, Wasi Uddin Ahmad, Yuan-Fang Li, Yong-Bin Kang,
and Rifat Shahriyar. CrossSum: Beyond English-centric cross-lingual summarization for
1,500+ language pairs. In Anna Rogers, Jordan Boyd-Graber, and Naoaki Okazaki, editors,
Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics
(Volume 1: Long Papers), pages 2541–2564, Toronto, Canada, July 2023. Association for
Computational Linguistics.
[6] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal,
Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel
Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel Ziegler,
Jeffrey Wu, Clemens Winter, Chris Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott
Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya
Sutskever, and Dario Amodei. Language models are few-shot learners. In H. Larochelle,
M. Ranzato, R. Hadsell, M.F. Balcan, and H. Lin, editors, Advances in Neural Information
Processing Systems, volume 33, pages 1877–1901. Curran Associates, Inc., 2020.
[7] Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Yunxuan
Li, Xuezhi Wang, Mostafa Dehghani, Siddhartha Brahma, et al. Scaling instruction-finetuned
language models. arXiv preprint arXiv:2210.11416, 2022.
8

--- Page 9 ---

[8] Alexis Conneau, Ruty Rinott, Guillaume Lample, Adina Williams, Samuel Bowman, Holger
Schwenk, and Veselin Stoyanov. XNLI: Evaluating cross-lingual sentence representations. In
Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing,
pages 2475–2485, Brussels, Belgium, October-November 2018. Association for Computational
Linguistics.
[9] Mike Conover, Matt Hayes, Ankit Mathur, Jianwei Xie, Jun Wan, Sam Shah, Ali Ghodsi, Patrick
Wendell, Matei Zaharia, and Reynold Xin. Free dolly: Introducing the world’s first truly open
instruction-tuned llm, 2023.
[10] Marta R Costa-jussa, James Cross, Onur Çelebi, Maha Elbayad, Kenneth Heafield, Kevin
Heffernan, Elahe Kalbassi, Janice Lam, Daniel Licht, Jean Maillard, et al. No language left
behind: Scaling human-centered machine translation. arXiv preprint arXiv:2207.04672, 2022.
[11] Zoltan Csaki, Pian Pawakapan, Urmish Thakker, and Qiantong Xu.
Efficiently adapting
pretrained language models to new languages. arXiv preprint arXiv:2311.05741, 2023.
[12] Ning Ding, Yulin Chen, Bokai Xu, Yujia Qin, Shengding Hu, Zhiyuan Liu, Maosong Sun,
and Bowen Zhou. Enhancing chat language models by scaling high-quality instructional
conversations. In Houda Bouamor, Juan Pino, and Kalika Bali, editors, Proceedings of the
2023 Conference on Empirical Methods in Natural Language Processing, pages 3029–3051,
Singapore, December 2023. Association for Computational Linguistics.
[13] Common Crawl Foundation. Statistics of common crawl monthly archives by commoncrawl.
https://commoncrawl.github.io/cc-crawl-statistics/plots/languages, 2023.
[14] Tahmid Hasan, Abhik Bhattacharjee, Md. Saiful Islam, Kazi Mubasshir, Yuan-Fang Li, Yong-
Bin Kang, M. Sohel Rahman, and Rifat Shahriyar. XL-sum: Large-scale multilingual abstractive
summarization for 44 languages. In Findings of the Association for Computational Linguistics:
ACL-IJCNLP 2021, pages 4693–4703, Online, August 2021. Association for Computational
Linguistics.
[15] Edward J Hu, yelong shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang,
Lu Wang, and Weizhu Chen. LoRA: Low-rank adaptation of large language models. In
International Conference on Learning Representations, 2022.
[16] Albert Q Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh
Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile
Saulnier, et al. Mistral 7b. arXiv preprint arXiv:2310.06825, 2023.
[17] Taku Kudo and John Richardson. SentencePiece: A simple and language independent subword
tokenizer and detokenizer for neural text processing. In Proceedings of the 2018 Conference
on Empirical Methods in Natural Language Processing: System Demonstrations, pages 66–71,
Brussels, Belgium, November 2018. Association for Computational Linguistics.
[18] Harrison Lee, Samrat Phatale, Hassan Mansoor, Kellie Lu, Thomas Mesnard, Colton Bishop,
Victor Carbune, and Abhinav Rastogi. Rlaif: Scaling reinforcement learning from human
feedback with ai feedback. arXiv preprint arXiv:2309.00267, 2023.
[19] Wei Qi Leong, Jian Gang Ngui, Yosephine Susanto, Hamsawardhini Rengarajan, Kengatharaiyer
Sarveswaran, and William Chandra Tjhi. Bhasa: A holistic southeast asian linguistic and cultural
evaluation suite for large language models. arXiv preprint arXiv:2309.06085, 2023.
[20] Xuechen Li, Tianyi Zhang, Yann Dubois, Rohan Taori, Ishaan Gulrajani, Carlos Guestrin, Percy
Liang, and Tatsunori B. Hashimoto. Alpacaeval: An automatic evaluator of instruction-following
models. https://github.com/tatsu-lab/alpaca_eval, 2023.
[21] Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga,
Yian Zhang, Deepak Narayanan, Yuhuai Wu, Ananya Kumar, Benjamin Newman, Binhang
Yuan, Bobby Yan, Ce Zhang, Christian Cosgrove, Christopher D. Manning, Christopher Ré,
Diana Acosta-Navas, Drew A. Hudson, Eric Zelikman, Esin Durmus, Faisal Ladhak, Frieda
Rong, Hongyu Ren, Huaxiu Yao, Jue Wang, Keshav Santhanam, Laurel Orr, Lucia Zheng,
Mert Yuksekgonul, Mirac Suzgun, Nathan Kim, Neel Guha, Niladri Chatterji, Omar Khattab,
Peter Henderson, Qian Huang, Ryan Chi, Sang Michael Xie, Shibani Santurkar, Surya Ganguli,
Tatsunori Hashimoto, Thomas Icard, Tianyi Zhang, Vishrav Chaudhary, William Wang, Xuechen
Li, Yifan Mai, Yuhui Zhang, and Yuta Koreeda. Holistic evaluation of language models, 2023.
9

--- Page 10 ---

[22] Chin-Yew Lin. ROUGE: A package for automatic evaluation of summaries. In Text Summariza-
tion Branches Out, pages 74–81, Barcelona, Spain, July 2004. Association for Computational
Linguistics.
[23] Xi Victoria Lin, Todor Mihaylov, Mikel Artetxe, Tianlu Wang, Shuohui Chen, Daniel Simig,
Myle Ott, Naman Goyal, Shruti Bhosale, Jingfei Du, Ramakanth Pasunuru, Sam Shleifer,
Punit Singh Koura, Vishrav Chaudhary, Brian O’Horo, Jeff Wang, Luke Zettlemoyer, Zornitsa
Kozareva, Mona Diab, Veselin Stoyanov, and Xian Li. Few-shot learning with multilingual
generative language models. In Proceedings of the 2022 Conference on Empirical Methods in
Natural Language Processing, pages 9019–9052, Abu Dhabi, United Arab Emirates, December
2022. Association for Computational Linguistics.
[24] Adian Liusie, Potsawee Manakul, and Mark J. F. Gales. LLM Comparative Assessment:
Zero-shot NLG Evaluation through Pairwise Comparisons using Large Language Models, 2023.
[25] Ilya Loshchilov and Frank Hutter. Decoupled weight decay regularization. In International
Conference on Learning Representations, 2019.
[26] Lalita Lowphansirikul, Charin Polpanumas, Nawat Jantrakulchai, and Sarana Nutanong.
Wangchanberta:
Pretraining transformer-based thai language models.
arXiv preprint
arXiv:2101.09635, 2021.
[27] Yun Luo, Zhen Yang, Fandong Meng, Yafu Li, Jie Zhou, and Yue Zhang. An empirical study of
catastrophic forgetting in large language models during continual fine-tuning. arXiv preprint
arXiv:2308.08747, 2023.
[28] Louis Martin, Benjamin Muller, Pedro Javier Ortiz Suárez, Yoann Dupont, Laurent Romary,
Éric de la Clergerie, Djamé Seddah, and Benoît Sagot. CamemBERT: a tasty French language
model. In Proceedings of the 58th Annual Meeting of the Association for Computational
Linguistics, pages 7203–7219, Online, July 2020. Association for Computational Linguistics.
[29] Martin Müller and Florian Laurent. Cedille: A large autoregressive french language model.
arXiv preprint arXiv:2202.03371, 2022.
[30] Dat Quoc Nguyen and Anh Tuan Nguyen. PhoBERT: Pre-trained language models for Viet-
namese. In Findings of the Association for Computational Linguistics: EMNLP 2020, pages
1037–1042, Online, November 2020. Association for Computational Linguistics.
[31] Xuan-Phi Nguyen, Wenxuan Zhang, Xin Li, Mahani Aljunied, Qingyu Tan, Liying Cheng,
Guanzheng Chen, Yue Deng, Sen Yang, Chaoqun Liu, et al. Seallms–large language models for
southeast asia. arXiv preprint arXiv:2312.00738, 2023.
[32] The National Institute of Educational Testing Service. Basic statistical values of o-net test
results. https://www.niets.or.th/th/content/view/11821, 2021.
[33] Consortium of Thai Medical Schools. Scores report of the tpat1 exam for thai medical schools
admission. https://www9.si.mahidol.ac.th/cotmes_stat.html, 2023.
[34] Council of University Presidents of Thailand. Basic statistical report tgat/tpat examination.
https://www.mytcas.com/stat/, 2023.
[35] OpenAI. GPT-4 technical report, 2023.
[36] OpenThaiGPT. Released openthaigpt 7b 1.0.0-beta. https://openthaigpt.aieat.or.th/,
2023.
[37] Pedro Javier Ortiz Suárez, Laurent Romary, and Benoît Sagot. A monolingual approach to
contextualized word embeddings for mid-resource languages. In Proceedings of the 58th Annual
Meeting of the Association for Computational Linguistics, pages 1703–1714, Online, July 2020.
Association for Computational Linguistics.
[38] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin,
Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to
follow instructions with human feedback. Advances in Neural Information Processing Systems,
35:27730–27744, 2022.
[39] Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu. Bleu: a method for automatic
evaluation of machine translation. In Proceedings of the 40th Annual Meeting of the Association
for Computational Linguistics, pages 311–318, Philadelphia, Pennsylvania, USA, July 2002.
Association for Computational Linguistics.
10

--- Page 11 ---

[40] Guilherme Penedo, Quentin Malartic, Daniel Hesslow, Ruxandra Cojocaru, Alessandro Cappelli,
Hamza Alobeidli, Baptiste Pannier, Ebtesam Almazrouei, and Julien Launay. The refinedweb
dataset for falcon llm: Outperforming curated corpora with web data, and web data only, 2023.
[41] Ramon Pires, Hugo Abonizio, Thales Rogério, and Rodrigo Nogueira. Sabi\’a: Portuguese
large language models. arXiv preprint arXiv:2304.07880, 2023.
[42] Charin Polpanumas, Wannaphong Phatthiyaphaibun, Patomporn Payoungkhamdee, Peerat
Limkonchotiwat, Lalita Lowphansirikul, Can Udomcharoenchaikit, Titipat Achakulwisut,
Ekapol Chuangsuwanich, and Sarana Nutanong.
WangChanGLM — The Multilingual
Instruction-Following Model, April 2023.
[43] Edoardo Maria Ponti, Goran Glavaš, Olga Majewska, Qianchu Liu, Ivan Vuli´c, and Anna
Korhonen. XCOPA: A multilingual dataset for causal commonsense reasoning. In Proceedings
of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP),
pages 2362–2376, Online, November 2020. Association for Computational Linguistics.
[44] Maja Popovi´c. chrF: character n-gram F-score for automatic MT evaluation. In Proceedings
of the Tenth Workshop on Statistical Machine Translation, pages 392–395, Lisbon, Portugal,
September 2015. Association for Computational Linguistics.
[45] Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever, et al.
Language models are unsupervised multitask learners. OpenAI blog, 1(8):9, 2019.
[46] Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D Manning, and
Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model.
arXiv preprint arXiv:2305.18290, 2023.
[47] Vinay Venkatesh Ramasesh, Aitor Lewkowycz, and Ethan Dyer. Effect of scale on catastrophic
forgetting in neural networks. In International Conference on Learning Representations, 2022.
[48] Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, Sten Sootla, Itai Gat, Xiaoqing Ellen Tan,
Yossi Adi, Jingyu Liu, Tal Remez, Jérémy Rapin, et al. Code llama: Open foundation models
for code. arXiv preprint arXiv:2308.12950, 2023.
[49] Gabriele Sarti and Malvina Nissim. It5: Large-scale text-to-text pretraining for italian language
understanding and generation. arXiv preprint arXiv:2203.03759, 2022.
[50] Neha Sengupta, Sunil Kumar Sahu, Bokang Jia, Satheesh Katipomu, Haonan Li, Fajri Koto,
Osama Mohammed Afzal, Samta Kamboj, Onkar Pandit, Rahul Pal, et al. Jais and jais-chat:
Arabic-centric foundation and instruction-tuned open generative large language models. arXiv
preprint arXiv:2308.16149, 2023.
[51] AI Singapore. Sea-lion (southeast asian languages in one network): A family of large language
models for southeast asia. https://github.com/aisingapore/sealion, 2023.
[52] Nisan Stiennon, Long Ouyang, Jeffrey Wu, Daniel Ziegler, Ryan Lowe, Chelsea Voss, Alec
Radford, Dario Amodei, and Paul F Christiano. Learning to summarize with human feedback.
Advances in Neural Information Processing Systems, 33:3008–3021, 2020.
[53] Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann Dubois, Xuechen Li, Carlos Guestrin, Percy
Liang, and Tatsunori B. Hashimoto. Stanford alpaca: An instruction-following llama model.
https://github.com/tatsu-lab/stanford_alpaca, 2023.
[54] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timo-
thée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, et al. Llama: Open
and efficient foundation language models. arXiv preprint arXiv:2302.13971, 2023.
[55] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei,
Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. Llama 2: Open
foundation and fine-tuned chat models. arXiv preprint arXiv:2307.09288, 2023.
[56] Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A. Smith, Daniel Khashabi,
and Hannaneh Hajishirzi. Self-instruct: Aligning language models with self-generated instruc-
tions. In Anna Rogers, Jordan Boyd-Graber, and Naoaki Okazaki, editors, Proceedings of the
61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
pages 13484–13508, Toronto, Canada, July 2023. Association for Computational Linguistics.
[57] Jason Wei, Maarten Bosma, Vincent Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan
Du, Andrew M. Dai, and Quoc V Le. Finetuned language models are zero-shot learners. In
International Conference on Learning Representations, 2022.
11

--- Page 12 ---

[58] BigScience Workshop, Teven Le Scao, Angela Fan, Christopher Akiki, Ellie Pavlick, Suzana
Ili´c, Daniel Hesslow, Roman Castagné, Alexandra Sasha Luccioni, François Yvon, et al. Bloom:
A 176b-parameter open-access multilingual language model. arXiv preprint arXiv:2211.05100,
2022.
[59] Shijie Wu, Ozan Irsoy, Steven Lu, Vadim Dabravolski, Mark Dredze, Sebastian Gehrmann,
Prabhanjan Kambadur, David Rosenberg, and Gideon Mann. Bloomberggpt: A large language
model for finance. arXiv preprint arXiv:2303.17564, 2023.
[60] Linting Xue, Noah Constant, Adam Roberts, Mihir Kale, Rami Al-Rfou, Aditya Siddhant,
Aditya Barua, and Colin Raffel.
mT5: A massively multilingual pre-trained text-to-text
transformer. In Proceedings of the 2021 Conference of the North American Chapter of the
Association for Computational Linguistics: Human Language Technologies, pages 483–498,
Online, June 2021. Association for Computational Linguistics.
[61] Aohan Zeng, Xiao Liu, Zhengxiao Du, Zihan Wang, Hanyu Lai, Ming Ding, Zhuoyi Yang, Yifan
Xu, Wendi Zheng, Xiao Xia, Weng Lam Tam, Zixuan Ma, Yufei Xue, Jidong Zhai, Wenguang
Chen, Zhiyuan Liu, Peng Zhang, Yuxiao Dong, and Jie Tang. GLM-130b: An open bilingual
pre-trained model. In The Eleventh International Conference on Learning Representations,
2023.
[62] Wenxuan Zhang, Sharifah Mahani Aljunied, Chang Gao, Yew Ken Chia, and Lidong Bing.
M3exam: A multilingual, multimodal, multilevel benchmark for examining large language
models. arXiv preprint arXiv:2306.05179, 2023.
[63] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang,
Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, et al. Judging llm-as-a-judge with mt-bench and
chatbot arena. arXiv preprint arXiv:2306.05685, 2023.
12

```
