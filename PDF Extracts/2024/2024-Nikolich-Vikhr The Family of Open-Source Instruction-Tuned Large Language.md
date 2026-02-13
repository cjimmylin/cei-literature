---
title: "2024-Nikolich-Vikhr The Family of Open-Source Instruction-Tuned Large Language - PDF Extract"
source_pdf: "2024-Nikolich-Vikhr The Family of Open-Source Instruction-Tuned Large Language.pdf"
pages: 9
extracted_at: "2026-02-13T09:50:30.805035"
---

# PDF Extract: 2024-Nikolich-Vikhr The Family of Open-Source Instruction-Tuned Large Language

**Source PDF:** 2024-Nikolich-Vikhr The Family of Open-Source Instruction-Tuned Large Language.pdf
**Total Pages:** 9

---

## Content

```
--- Page 1 ---

Vikhr: The Family of Open-Source Instruction-Tuned Large Language
Models for Russian
Aleksandr Nikolich♢
ITMO University
alexdragannikolich@gmail.com
Konstantin Korolev♢
HSE University
korolevko@icloud.com
Sergei Bratchikov
Vikhr
hivaze.me@gmail.com
Igor Kiselev
Accenture
igor.kiselev@accenture.com
Artem Shelmanov
MBZUAI
artem.shelmanov@mbzuai.ac.ae
Abstract
There has been a surge in the development of
various Large Language Models (LLMs). How-
ever, text generation for languages other than
English often faces significant challenges, in-
cluding poor generation quality and reduced
computational performance due to the dis-
proportionate representation of tokens in the
model’s vocabulary. In this work, we address
these issues by developing a pipeline for the
adaptation of English-oriented pre-trained mod-
els to other languages and constructing effi-
cient bilingual LLMs.
Using this pipeline,
we construct Vikhr, a series of bilingual open-
source instruction-following LLMs designed
specifically for the Russian language. “Vikhr”
refers to the name of the Mistral LLM series
and means a “strong gust of wind.” Unlike
previous Russian-language models that typi-
cally rely on LoRA adapters on top of English-
oriented models, sacrificing performance for
lower training costs, Vikhr features an adapted
tokenizer vocabulary and undergoes the contin-
ued pre-training and instruction tuning of all
weights. This not only enhances the model’s
performance but also significantly improves its
computational and contextual efficiency. We
also expanded the instruction datasets and cor-
pora for continued pre-training. The model
weights, instruction sets, and code are publicly
available.1
1
Introduction
Instruction tuning has unlocked in Large Language
Models (LLMs) vast zero-shot capabilities without
the need for careful prompt engineering (Ouyang
et al., 2022). The most rapid research and develop-
ment efforts are currently devoted to English LLMs.
There has been a surge in English open-source mod-
els: Llama series (Touvron et al., 2023a,b), Mistral
series (Jiang et al., 2023), Vicuna series (Chiang
♢Equal contribution
1https://huggingface.co/Vikhrmodels
et al., 2023), etc. This growth is driven by the abun-
dance of raw training data in English and dedicated
efforts to create extensive sets of instruction-output
pairs. Even though LLMs oriented on English have
some multilingual capabilities (Zhao et al., 2024)
due to the presence of small amounts of text in var-
ious languages within their training datasets (Tou-
vron et al., 2023a), their overall performance in
non-English languages remains relatively limited.
Although they can usually generate portions of co-
herent texts, these models struggle with reason-
ing in non-English languages, lack culture-specific
knowledge, and are highly inefficient in terms of
tokenization. This inefficiency stems from how
byte-pair tokenization algorithms operate, as they
break down infrequent words into multiple tokens.
Since multilingual data typically represents a small
portion of the training dataset, non-English words
are often split into many pieces. As a result, this
increases the number of steps during prompt pro-
cessing and text generation, reduces the effective
context window, and ultimately degrades overall
performance (Tikhomirov and Chernyshev, 2023;
Petrov et al., 2024). This disparity places non-
English languages at a disadvantage.
There is also a research direction focused on de-
veloping multilingual LLMs designed to perform
well across multiple popular languages: BLOOMz
(Muennighoff et al., 2023), mGPT (Shliazhko et al.,
2022), Bactrian-X (Li et al., 2023), PALO (Maaz
et al., 2024), Aya101 from CohereAI (Üstün et al.,
2024), etc. These models are typically trained
on rich multilingual datasets and are less skewed
towards English. However, when aiming to per-
form well across multiple languages simultane-
ously, these models must still share their vocab-
ulary and parameters. This often hinders their per-
formance for each particular language in isolation,
especially for the popular smaller model sizes, such
as 7B and 13B.
The aim of maximizing the LLM performance
arXiv:2405.13929v6  [cs.CL]  14 Apr 2025

--- Page 2 ---

for a specific language within a certain number of
parameters has led researchers to develop bilingual
LLMs (Sengupta et al., 2023; Pieri et al., 2024;
Faysse et al., 2024). These LLMs prioritize a re-
gional language, e.g. Jais (Sengupta et al., 2023)
focuses on Arabic, but they are trained also on
English data. The inclusion of English data in
pre-training alongside regional language data is
motivated by the significantly larger volume of En-
glish data available. This helps LLMs substantially
enhance skills such as logical and common sense
reasoning, which are also applied when generat-
ing text in a regional language. Bilingual LLMs
are a promising direction as they can remain small
and efficient, but at the same time comprehensively
capture linguistic nuances and cultural contexts of
the regional language.
This work seeks to develop a pipeline for adapt-
ing English LLMs to other languages, facilitating
the development of bilingual LLMs. Specifically,
we aim to build an instruction-following bilingual
LLM for Russian and English that could be used for
multilingual natural language processing research.
Russian is one of the high-resource languages
and is typically represented in multilingual LLMs.
Additionally, there are several proprietary closed-
source LLMs, such as MTS AI, GigaChat, and Yan-
dexGPT, that meet or even surpass their English-
oriented flagship competitors when it comes to text
processing and generation in Russian. However,
controllable research often requires white-box ac-
cess to LLM logits and layer outputs, the ability to
modify weights and model architecture, and con-
sistent answers for reproducibility, which is often
impossible in closed-source LLMs due to their con-
stant development and retirement. There are only
a few open-source LLMs designed for Russian:
Saiga (Gusev, 2023), ruGPT (AI Forever, 2022),
ruadapt (Tikhomirov and Chernyshev, 2023), and
some others. Of these, only Saiga and ruadapt
are instruction-tuned. We aim to fill the lack of
instruction-tuned open-source LLM for Russian
that is both efficient and effective.
Building even a small LLM tailored to a specific
language from scratch demands a lot of computa-
tional resources. Consequently, many researchers
opt to fine-tune LoRA adapters (Hu et al., 2021)
for English-oriented LLMs using some language-
specific data. While this approach can improve
model generation quality, it does not address com-
putational inefficiency because the tokenizer and
model vocabulary remain unchanged. In contrast,
our approach not only fine-tunes a base LLM on
Russian language data but also reconstructs its un-
derlying tokenizer and vocabulary, alongside sug-
gesting an improved method for continued pre-
training. Additionally, we have significantly ex-
panded the available Russian datasets for instruc-
tion tuning.
Contributions of the paper are the following:
• We have developed a pipeline for adapting
English-oriented LLMs to other languages.
The pipeline implements vocabulary adapta-
tion, continued pre-training with regulariza-
tion to prevent “catastrophic forgetting,” and
instruction tuning.
• Using the pipeline, we have constructed Vikhr
– an open-source instruction-following LLM
oriented on the Russian language. In addition
to its high generation quality, Vikhr features
an efficient tokenizer that enables rapid text
generation and good context utilization.
• We have expanded the datasets for continued
pre-training of Russian language models and
previously available instruction datasets.
• We have constructed two evaluation bench-
marks for Russian LLMs by translating the
English MMLU (Hendrycks et al., 2020) and
MMLU-pro (Wang et al., 2024b) benchmarks.
• We conducted ablation studies of various
pipeline components. The studies confirm
the effectiveness and validity of the individ-
ual components within our LLM adaptation
pipeline.
2
Related Work
One of the first prominent series of generative
LLMs for Russian is ruGPT (AI Forever, 2022;
Zmitrovich et al., 2023). The authors developed
several models, trained on the standard language
modeling task, with sizes reaching up to 13 bil-
lion parameters. These models were created from
scratch and trained on a large Russian corpus, en-
abling them to capture the linguistic nuances of
Russian more effectively than multilingual models.
Additionally, since the training data was mostly in
Russian, these models also have efficient tokeniza-
tion. However, the lack of multilingual data (e.g.
in English) limits their performance. Notably, the
ruGPT models are not instruction-tuned.
Gusev (2023) suggests to leverage the reason-
ing capabilities of existing English-oriented LLMs

--- Page 3 ---

and adapt them to the Russian language by training
LoRA adapters. They created an Alpaca-like set
of Russian instruction-output pairs and performed
instruction tuning on it. As a result, they have es-
tablished a series of models called Saiga, which
demonstrate competitive performance and have
been a reasonable choice for off-the-shelf open-
source Russian LLMs for the past years. However,
the tokenizer in these models is not adapted, so
they experience issues with context size and com-
putational efficiency.
Tikhomirov and Chernyshev (2023) address
these issues in Saiga. In addition to model tun-
ing on Russian data, they also adapted the model
tokenizer. They note that improving tokenization
helps to both enhance the efficiency of the model
and its performance while reducing memory con-
sumption. However, during continued pre-training,
the authors froze the model weights, except for
LM heads and token embeddings, which leads to
suboptimal performance.
In this work, we take advantage of pre-trained
English-oriented LLMs, adapt LLM tokenizer for
better computational and contextual efficiency,
leverage continued pre-training on vast Russian-
language corpora with regularization for prevent-
ing “catastrophic forgetting”, construct a novel ex-
tended set of Russian instruction-output pairs, and
perform instruction tuning. The created LLM adap-
tation pipeline along with the data for continued
pre-training and instruction tuning enables Vikhr
to achieve good generation quality for Russian and
demonstrate high computational efficiency.
3
LLM Construction Pipeline
The construction of Vikhr starts from one of the
English-oriented LLMs. In this work, we discuss
the Vikhr model based on Mistral 7B (Jiang et al.,
2023). The strong logical and common-sense rea-
soning capabilities, as well as the extensive world
knowledge present in Mistral LLMs, provide an
excellent starting point for our model. These fea-
tures partially transfer to Vikhr, enhancing its per-
formance in generating text in Russian. The pro-
cess of the LLM adaptation to Russian starts with
the vocabulary adaptation. Then we perform con-
tinued pre-training of the LLM on large Russian
datasets to mitigate the vocabulary shift and in-
troduce culture-specific knowledge. Finally, we
perform fine-tuning of Vikhr on a set of instruction-
output pairs in Russian.
Content
Length
Tokenization Result
Original
Sentence
31
(ru) Машинное обучение
изменяет мир
[(en)
Machine
learning
changes the world.
Mistral Tok-
enizer
13
[‘Ма’, ‘шин’, ‘ное’, ‘об’, ‘у’,
‘чение’, ‘из’, ‘мен’, ‘я’, ‘ет’,
‘ми’, i ‘р’ ]
Vikhr
Tok-
enizer
7
[‘Ма’, ‘шин’, ‘ное’, ‘обуче-
ние’, ‘изменяет’, ‘мир’]
Table 1: A comparison of tokenization between the
original Mistral model and Vikhr.
40000
60000
80000
100000
120000
Vocabulary Size
0.26
0.28
0.30
0.32
0.34
0.36
0.38
0.40
Tokenization Density
llama3
Vikhr-7B
Mistral-7B
ruGPT-13B
Tokenization Density for Different Tokenizers
Figure 1: The efficiency of the Vikhr tokenizer for Rus-
sian in comparison to tokenizers of other models.
3.1
Vocabulary Adaptation
The big drawback of English-oriented LLMs is that
each Russian word would be split into multiple
tokens: a common case is when symbols in the
word become individual tokens (see example in
Table 1). This slows down the generation by multi-
ple times, reduces the amount of information that
could be stored in the context, and drastically hurts
the generation quality.
To mitigate this problem in Vikhr, we adopt
the approach suggested in (Cui et al., 2023;
Tikhomirov and Chernyshev, 2023), where authors
rebuild the tokenizer using a language-specific cor-
pus. In particular, we trained a SentencePiece to-
kenizer (Kudo and Richardson, 2018) with a 40k
vocabulary on the RuLM dataset (Gusev, 2023).
As can be seen from Figure 1, the resulting tok-
enizer for Russian is much more efficient than the
tokenizer of the original English-oriented model.
3.2
Continued Pre-training
The new vocabulary requires new embedding matri-
ces and LM heads. The tokens that were present in
the original vocabulary are initialized with the old

--- Page 4 ---

Data Source
Approx. size
(GB)
Tokens
(Billion)
Scientific papers
20
2.5
News articles
4
1
Wikipedia
25
4
Habr
6
1
Other sources
20
2.5
Table 2: The statistics of the Russian-language datasets
for continued pre-training.
embeddings; the new tokens are initialized by aver-
aging the embeddings of their pieces in the origi-
nal embedding matrix (Hewitt, 2021). The similar
approach is also applied to LM heads. Training
models with these modifications demands much
more computational resources than the mainstream
method of adapting LLMs to new languages using
LoRA adapters (Hu et al., 2021). This is because it
involves continued pre-training of the entire model
and requires much more language-specific data to
mitigate the shift in the vocabulary.
The dataset for continued pre-training is con-
structed from high-quality sources, including Rus-
sian Wikipedia, news articles, scientific papers
from peer-reviewed journals and conferences, and
top 100k up-voted posts on Habr – a popular on-
line blog community focused on technology, soft-
ware development, and science. The statistics of
these datasets are presented in Table 2. We per-
formed deduplication of the collection on the level
of paragraphs using the MIHash algorithm (Cakir
et al., 2017). Furthermore, we performed filtra-
tion of the collected data. For this purpose, we
annotated 20k documents using GPT-4-turbo with
the aim to assess their informativeness, usefulness
for studying, grammatical correctness, style, and
safety. Using these annotations, we fine-tuned a
RuBERT-tiny(Dale, 2021) filtration model and ap-
plied it to the deduplicated corpus. After filtration,
the total number of tokens left for continued pre-
training is 11 billion.
We observed that continued pre-training of a
LLM can partially diminish the reasoning capabili-
ties present in the original English-oriented model,
significantly impacting overall performance. In
our preliminary experiments, a model that under-
went continued pre-training may demonstrate even
worse performance on Russian benchmarks than
the original English-oriented model. To alleviate
this “catastrophic forgetting” in reasoning, we use
the loss regularization with the KL penalty between
Hyperparam.
Value
LR
1 × 10−3
AdamW eps
1 × 10−8
Num warmup steps
10
AdamW betas
0.99, 0.95
Accumulation steps
128
Batch size
3
Epochs
1
Sequence length
1024
Table 3:
The hyperparameters for continued pre-
training.
the probability distribution of Vikhr and the refer-
ence English-oriented LLM:
LVikhr = LCE + KL (PVikhr∥PRef ) .
(1)
In practice, we implement the regularization using
the SLERP interpolation of model losses (Goddard
et al., 2024).
To speed up the process of continued pre-
training, we use an optimized Flash attention im-
plementation.2 As an optimization algorithm, we
leverage AdamW, as it trades some memory effi-
ciency in favor of robustness to the hyperparameter
choice. The hyperparameters used for continued
pre-training are presented in Table 3.
3.3
Instruction Tuning
Instruction tuning is an essential step in reaching
high zero-shot performance with LLMs. It also
allows obtaining a more natural communication
with the model without complex prompting. Fur-
ther fine-tuning techniques such as RLHF (Ouyang
et al., 2022) or DPO (Rafailov et al., 2024), which
require input from the assessors, are also crucial
for such tasks as multicriteria alignment. How-
ever, the most significant performance gains are
still achieved through instruction tuning (Jha et al.,
2023).
Previously, Gusev (2023) constructed an open-
source set of instruction-output pairs for the Rus-
sian language (Saiga). The core Saiga dataset was
created similar to Alpaca by querying ChatGPT
(gpt-3.5-turbo) (Taori et al., 2023). In this work,
we extend this set by translating two English in-
struction datasets. First, we translated instructions
for the FLAN model (Wei et al., 2021) and gener-
ated answers in Russian using ChatGPT. Originally,
FLAN instructions were constructed automatically
2https://huggingface.co/docs/optimum/
bettertransformer/tutorials/convert

--- Page 5 ---

Instruction Set
Language
# instances
Veles
Russian
30k
Nectar
English
50k
Saiga
Russian
100k
ruFLAN
Russian
500k
Table 4: The statistics of the instruction datasets.
from annotated datasets using templates to facili-
tate multitask and zero-shot capabilities of seq2seq
models. Later, it was shown that this data also
helps to improve decoder-only chat-oriented mod-
els as well. Second, we construct Veles3 by trans-
lating the English OpenHermes (Teknium, 2023)
instruction dataset. Third, we incorporate without
translation Nectar4 (Zhu et al., 2023) – an English
instruction dataset. This ensures that Vikhr main-
tains strong performance in English as well.
Similar to the corpus for continued pre-training,
we performed deduplication of the instruction set.
Since the majority of the outputs were machine
generated, there are many low-quality outputs. To
mitigate this problem, we filtered out low-quality
pairs using a reward model trained on human data.
For the reward model, we selected the multilingual-
e5-large model (Wang et al., 2024a). This model
was particularly suitable for our needs due to its
ability to handle multilingual data efficiently, en-
suring that the classifier could accurately assess the
quality of responses in both Russian and English.
We trained the reward model on the answer pref-
erence dataset5, which was collected from human-
written prompts and annotated using GPT-4. By
applying this reward model, we filtered out low-
quality instruction-output pairs, significantly en-
hancing the overall performance and reliability of
our instruction datasets. The statistics of the Vikhr
instruction datasets are presented in Table 4.
Contrary to Saiga, we do not use LoRA adapters,
and just as in the phase of continued pre-training,
we update all model parameters. The hyperparame-
ters for the instruction tuning phase are presented
in Table 5.
3.4
Hardware
Vikhr was trained on eight NVIDIA A100 GPUs
80GB. We spent approximately 1,000 GPU hours
3https://huggingface.co/datasets/Vikhrmodels/
Veles-2.5
4https://huggingface.co/datasets/
berkeley-nest/Nectar
5https://huggingface.co/datasets/Vikhrmodels/
sbs
Hyperparam.
Value
LR
1 × 10−5
AdamW, eps
1 × 10−8
Num warmup steps
10
AdamW, betas
0.99, 0.95
Accumulation steps
64
Batch size
3
Num epochs
3
Sequence length
1024
Table 5: The hyperparameters for instruction tuning.
for the continued pre-training phase and 60 hours
for instruction tuning.
4
Experiments
4.1
Experimental Setup
For evaluation, we use ruXNLI (Conneau et al.,
2018), and we also constructed Ru-MMLU and
Ru-MMLU-pro by automatically translating the
original English MMLU and MMLU-pro to Rus-
sian. Translation was done by GPT-3.5 and GPT-4,
respectively. We report the accuracy@1 score.
4.2
Quality of Generated Text
To check the performance of the model in text gen-
eration, we performed qualitative analysis of LLM
outputs. Table 6 compares several responses of
Vikhr with outputs of the base model (Mistral-7B-
Instruct-v0.2). As we can see from the presented
examples, when Mistral generates Russian text, it
often injects English words. Moreover, sometimes
generated words consist of an English and a Rus-
sian token. From the second example, we see that
Mistral also has issues with grammatical coherence.
In the third example, LLM suggests to “clean a fish
from fur”, which illustrates the lack of understand-
ing of word meanings in the Russian language. We
also note that Mistral tends to answer in English
even when the input prompt is in Russian. These
issues appear very often and make the base model
useless for generation of Russian texts in practi-
cal scenarios. On the considered examples, Vikhr
does not demonstrate any of these problems. Texts
generated by Vikhr are grammatically coherent and
correct.
4.3
Ablation Studies
We conducted several ablation studies to demon-
strate the effects of various features of our model
translation pipeline.

--- Page 6 ---

Prompt
Answer of base Mistral-0.2-Instruct
Answer of Vikhr
Что такое чебурек?
[What
does
cheburek
means?]
Чебурек - это классическое dish среднеазиат-
ской и русской кухни, которое включает в себя
тонкий lavash, завернутый в форме полумесяца
или кольца. Он обычно наполнен meat (говяди-
ной, бараниной или курицей) и cheese. История
чебурека начинается с древних тюркских пле-
мен, которые готовили подобные dishes из мяса
и теста. ... Чебурек часто подается как горя-
чее dish, жареное на сковороде или в духовке.
Тесто обычно тонкое и хрустящее снаружи, а
внутри мягкое и сочное. Мясо и сыр добавля-
ют flavor depth и питательную ценность.
Чебурек — это традиционное блюдо кавказ-
ской кухни, которое представляет собой боль-
шой, тонкий пирог из пресного теста с мясной
начинкой, обжаренный во фритюре. Внутри
чебурека обычно находится сочный фарш из ба-
ранины или говядины, приправленный луком,
солью, перцем и другими специями. Благодаря
обжарке в масле, тесто становится хрустящим
снаружи, а начинка остается мягкой и сочной.
История чебурека уходит корнями в древние
времена, когда кочевники готовили его на рас-
калённых камнях или в больших котлах с го-
рячим маслом.
Расскажи на русском язы-
ке что такое хачапури
[Tell
in
Russian
what
hatchapuri is]
Хачапури (хачпури, хачъапури) – это тради-
ционное блюдо грузинской кухни.
Это тип
пицце или за Francia, выполненной в виде круг-
лой или полукруглой лепёшки, покрытой верху
layerм layerim – смесью тонко нарезанныхimo
эplesses, лука ..
Хачапури — это традиционное грузинское блю-
до, представляющее собой лепешку с сыром
внутри. Вот рецепт хачапури. Ингредиенты:
- Для теста: - 3 стакана муки - 1 ч. л. соли
- 1 ч. л. сахара - 100 мл теплой воды - Для
смазывания: 1 ст. л. топленого масла ...
Расскажи на русском язы-
ке как приготовить уху
[Tell in Russian how to cook
a fish soup]
Уха (из Рыбы) – традиционное блюдо русской
кухни, которое готовится predominantly из щу-
ки или окуня.
Рас**те процедуру приготов-
ления ухи в домашних условиях:
Выберите
чистую рыбу. Очистить её от шерсти иICScoне
всех мелких костей s...
Уха — это традиционное русское блюдо, пред-
ставляющее собой наваристый суп из рыбы,
который варится на медленном огне. Вот базо-
вый рецепт ухи, который можно адаптировать
под свои вкусовые предпочтения. Ингредиен-
ты: 1 кг свежей рыбы (можно использовать
несколько видов, например, карп, щука, судак)
3-4 картофелины 1 крупная луковица 2-3 мор-
кови ...
Table 6: Comparison of texts generated by the base LLM Mistral-0.2-Instruct (on the left) with texts generated by
our model Vikhr (on the right). Issues in the output are highlighted with red.
Vocab. Size
PPL↓
ruXNLI↑
33k
10.2
0.42
40k
14.4
0.46
60k
16.7
0.43
80k
20.4
0.41
Table 7: Performance of the intermediate Vikhr mod-
els with different vocabulary sizes after continued pre-
training. The base model is LLaMa-2 7b. The vocabu-
lary size selected for the final Vikhr model is underlined.
PPL↓
ruXNLI↑
Ru-MMLU-pro↑
No filt. (17b tokens)
8.4
0.37
10.2
With filt. (11b tokens) (Ours)
7.2
0.46
11.1
Table 8: Performance metrics with and without filtration
of the corpus for the continued pre-training. Perplexity
is computed on the instruction dataset.
Selection of the vocabulary size.
Table 7
presents the performance of intermediate Vikhr
models with different vocabulary sizes after the
stage of continued pre-training. We measure per-
plexity of the LLM on the instruction set and the
performance on the ruXNLI task (Conneau et al.,
2018). As we can see, perplexity increases with
the vocabulary size, indicating some degradation.
However, the performance on the ruXNLI dataset
is not monotonic. While the results for the largest
vocabulary size are lower than those for the small-
est, we observe a performance peak at a vocabulary
PPL↓
ruXNLI↑
No regul.
8.1
0.34
With regul. (Ours)
7.2
0.45
Table 9: Performance with and without KL loss regular-
ization during continued pre-training.
Instruction Set
Ru-MMLU-pro
Saiga SFT
0.21
Translated Nectar
0.20
Ours
0.27
Table 10: Performance of Vikhr models fine-tuned on
various instruction sets. The base model is Llama-3 8b.
size of 40k tokens. We selected this size as it offers
improvements in the final task with only a slight
increase in perplexity.
Effect of filtration of the corpus for continued
pre-training
is illustrated in Table 8. As we can
see, despite reducing the size of the data, perform-
ing continued pre-training on the filtered corpus re-
sults in a model with lower perplexity and substan-
tially better scores in both considered end tasks: Ru-
MMLU-pro and ruXNLI. This again highlights the
importance of data quality for constructing good
LLMs.
Effect of loss regularization in continued pre-
training
is illustrated in Table 9. The results

--- Page 7 ---

show that the KL regularization introduced in
our pipeline slightly reduces perplexity and sub-
stantially increases the model performance in the
ruXNLI task.
This shows that continued pre-
training on its own might deteriorate LLM reason-
ing capabilities, and proper regularization helps
prevent the catastrophic forgetting.
Effect of fine-tuning on various instruction sets
is illustrated in Table 10. The results demonstrate
that fine-tuning on our instruction set gives a big
boost in performance on NLU tasks compared to
Saiga and translated Nectar.
5
Conclusion
We have presented Vikhr – a new open-source
instruction-following bilingual LLM oriented on
the Russian language. To create Vikhr, we de-
veloped a comprehensive pipeline for adapting
English-oriented LLMs to other languages. The
pipeline includes the adaptation of the tokenizer vo-
cabulary, continued pre-training of the entire model,
and instruction tuning. We have also constructed
a new dataset for instruction tuning by expanding
the Saiga dataset with automatically translated and
cleaned English instruction datasets. Our extensive
work enabled Vikhr to achieve high quality of gen-
eration while maintaining computational efficiency.
We hope that the developed cross-lingual adapta-
tion pipeline and the published models will foster
the research on LLMs and enhance the diversity of
languages incorporated into research agendas.
In the future work, we plan to release in the
open-source new better versions of Vikhr.
At
the moment, our best publicly available model is
Vikhr-Nemo-12B-Instruct6 based on Mistral NeMo.
We also plan to perform cross-lingual adaption of
LLMs to low-resource languages such as Belaru-
sian, Serbian, and Kazakh.
Limitations
We do not introduce additional restrictions on the
usage of our models. However, the users must
comply with the license of the base model and
instruction datasets.
We do not implement RLHF / DPO fine-tuning
of Vikhr due to the lack of resources for human
annotation. We expect further performance im-
provements from these techniques.
6https://huggingface.co/Vikhrmodels/
Vikhr-Nemo-12B-Instruct-R-21-09-24
We do not introduce additional instruction-
output pairs to facilitate LLM alignment. However,
we note that the majority of the data for supervised
fine-tuning of Vikhr are obtained from the Chat-
GPT model series, so our model partially inherits
its alignment.
Ethical Considerations
The development and deployment of Vikhr raise
several ethical considerations that must be ad-
dressed to ensure its responsible use:
• Bias and Fairness: For developing Vikhr, we
use publicly available data. Despite efforts to
train Vikhr on diverse datasets, there is a risk
of inherent biases in the data which may be
reflected in the model’s outputs. Continued
monitoring and evaluation are required to mit-
igate any biases, ensuring fair and unbiased
performance.
• Misinformation: As with any LLM, Vikhr
has the potential to generate misleading or
incorrect information.
It is crucial to es-
tablish guidelines and mechanisms for users
to verify the information provided by the
model, promoting critical assessment and
cross-referencing with reliable sources.
• Misuse: Vikhr can be used for malicious pur-
poses, such as generating harmful content,
spam, or deepfakes. Implementing usage re-
strictions and monitoring mechanisms to de-
tect and prevent misuse is critical to safeguard
against these risks.
Acknowledgements
We thank the reviewers for their insightful com-
ments, which have significantly improved this pa-
per. We would like to express our sincere gratitude
to Nikolay Kompanets for his invaluable contribu-
tions to the fine-tuning of the small models and the
verification of hypotheses.
References
AI Forever. 2022. ru-gpts: Generative pre-trained trans-
former models for russian. https://github.com/
ai-forever/ru-gpts.
Fatih Cakir, Kun He, Sarah A. Bargal, and Stan Sclaroff.
2017. Mihash: Online hashing with mutual informa-
tion. In IEEE International Conference on Computer
Vision (ICCV).

--- Page 8 ---

Wei-Lin Chiang, Zhuohan Li, Zi Lin, Ying Sheng,
Zhanghao Wu, Hao Zhang, Lianmin Zheng, Siyuan
Zhuang, Yonghao Zhuang, Joseph E. Gonzalez, Ion
Stoica, and Eric P. Xing. 2023. Vicuna: An open-
source chatbot impressing gpt-4 with 90%* chatgpt
quality.
Alexis Conneau, Ruty Rinott, Guillaume Lample, Ad-
ina Williams, Samuel R. Bowman, Holger Schwenk,
and Veselin Stoyanov. 2018. Xnli: Evaluating cross-
lingual sentence representations. In Proceedings of
the 2018 Conference on Empirical Methods in Natu-
ral Language Processing. Association for Computa-
tional Linguistics.
Yiming Cui, Ziqing Yang, and Xin Yao. 2023. Efficient
and effective text encoding for chinese llama and
alpaca. arXiv preprint arXiv:2304.08177.
David Dale. 2021. Small and fast bert for russian. [On-
line; posted 10-June-2021].
Manuel Faysse, Patrick Fernandes, Nuno Guerreiro,
António Loison, Duarte Alves, Caio Corro, Nico-
las Boizard, João Alves, Ricardo Rei, Pedro Mar-
tins, et al. 2024.
Croissantllm:
A truly bilin-
gual french-english language model. arXiv preprint
arXiv:2402.00786.
Charles Goddard, Shamane Siriwardhana, Malikeh
Ehghaghi, Luke Meyers, Vlad Karpukhin, Brian
Benedict, Mark McQuade, and Jacob Solawetz. 2024.
Arcee’s mergekit: A toolkit for merging large lan-
guage models. arXiv preprint arXiv:2403.13257.
Ilya Gusev. 2023. rulm: A toolkit for training neural lan-
guage models. https://github.com/IlyaGusev/
rulm.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou,
Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
2020. Measuring massive multitask language under-
standing. In International Conference on Learning
Representations (ICLR).
John Hewitt. 2021. Initializing new word embeddings
for pretrained language models.
Edward J Hu, Phillip Wallis, Zeyuan Allen-Zhu,
Yuanzhi Li, Shean Wang, Lu Wang, Weizhu Chen,
et al. 2021. Lora: Low-rank adaptation of large lan-
guage models. In International Conference on Learn-
ing Representations.
Aditi Jha, Sam Havens, Jeremy Dohmann, Alex Trott,
and Jacob Portes. 2023. Limit: Less is more for in-
struction tuning across evaluation paradigms. arXiv
preprint arXiv:2311.13133.
Albert Q Jiang, Alexandre Sablayrolles, Arthur Men-
sch, Chris Bamford, Devendra Singh Chaplot, Diego
de las Casas, Florian Bressand, Gianna Lengyel, Guil-
laume Lample, Lucile Saulnier, et al. 2023. Mistral
7b. arXiv preprint arXiv:2310.06825.
Taku Kudo and John Richardson. 2018. Sentencepiece:
A simple and language independent subword tok-
enizer and detokenizer for neural text processing. In
Proceedings of the 2018 Conference on Empirical
Methods in Natural Language Processing: System
Demonstrations, pages 66–71.
Haonan Li, Fajri Koto, Minghao Wu, Alham Fikri Aji,
and Timothy Baldwin. 2023. Bactrian-x: A multilin-
gual replicable instruction-following model with low-
rank adaptation. arXiv preprint arXiv:2305.15011.
Muhammad Maaz, Hanoona Rasheed, Abdelrahman
Shaker, Salman Khan, Hisham Cholakal, Rao M
Anwer, Tim Baldwin, Michael Felsberg, and Fa-
had S Khan. 2024.
Palo: A polyglot large mul-
timodal model for 5b people.
arXiv preprint
arXiv:2402.14818.
Niklas Muennighoff, Thomas Wang, Lintang Sutawika,
Adam Roberts, Stella Biderman, Teven Le Scao,
M Saiful Bari, Sheng Shen, Zheng Xin Yong, Hailey
Schoelkopf, et al. 2023. Crosslingual generalization
through multitask finetuning. In The 61st Annual
Meeting Of The Association For Computational Lin-
guistics.
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida,
Carroll Wainwright, Pamela Mishkin, Chong Zhang,
Sandhini Agarwal, Katarina Slama, Alex Ray, et al.
2022. Training language models to follow instruc-
tions with human feedback. Advances in neural in-
formation processing systems, 35:27730–27744.
Aleksandar Petrov, Emanuele La Malfa, Philip Torr,
and Adel Bibi. 2024. Language model tokenizers
introduce unfairness between languages. Advances
in Neural Information Processing Systems, 36.
Sara Pieri, Sahal Shaji Mullappilly, Fahad Shahbaz
Khan, Rao Muhammad Anwer, Salman Khan, Timo-
thy Baldwin, and Hisham Cholakkal. 2024. Bimedix:
Bilingual medical mixture of experts llm.
arXiv
preprint arXiv:2402.13253.
Rafael Rafailov, Archit Sharma, Eric Mitchell, Christo-
pher D Manning, Stefano Ermon, and Chelsea Finn.
2024. Direct preference optimization: Your language
model is secretly a reward model. Advances in Neu-
ral Information Processing Systems, 36.
Neha Sengupta, Sunil Kumar Sahu, Bokang Jia,
Satheesh
Katipomu,
Haonan
Li,
Fajri
Koto,
Osama Mohammed Afzal, Samta Kamboj, Onkar
Pandit, Rahul Pal, et al. 2023. Jais and jais-chat:
Arabic-centric foundation and instruction-tuned open
generative large language models. arXiv preprint
arXiv:2308.16149.
Oleh Shliazhko, Alena Fenogenova, Maria Tikhonova,
Vladislav Mikhailov, Anastasia Kozlova, and Tatiana
Shavrina. 2022. mgpt: Few-shot learners go multilin-
gual. arXiv preprint arXiv:2204.07580.
Rohan Taori, Ishaan Shum, Pieter Abbeel, Carlos
Guestrin, and Percy Liang. 2023. Stanford alpaca:
An instruction-following language model. GitHub.

--- Page 9 ---

Teknium. 2023. Openhermes 2.5: An open dataset of
synthetic data for generalist llm assistants.
Mikhail Tikhomirov and Daniil Chernyshev. 2023. Im-
pact of tokenization on llama russian adaptation.
arXiv preprint arXiv:2312.02598.
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier
Martinet, Marie-Anne Lachaux, Timothée Lacroix,
Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal
Azhar, et al. 2023a.
Llama:
Open and effi-
cient foundation language models. arXiv preprint
arXiv:2302.13971.
Hugo Touvron, Louis Martin, Kevin Stone, Peter Al-
bert, Amjad Almahairi, Yasmine Babaei, Nikolay
Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti
Bhosale, et al. 2023b.
Llama 2: Open founda-
tion and fine-tuned chat models.
arXiv preprint
arXiv:2307.09288.
Ahmet Üstün, Viraat Aryabumi, Zheng Yong, Wei-Yin
Ko, Daniel D’souza, Gbemileke Onilude, Neel Bhan-
dari, Shivalika Singh, Hui-Lee Ooi, Amr Kayid, Fred-
die Vargus, Phil Blunsom, Shayne Longpre, Niklas
Muennighoff, Marzieh Fadaee, Julia Kreutzer, and
Sara Hooker. 2024. Aya model: An instruction fine-
tuned open-access multilingual language model. In
Proceedings of the 62nd Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1:
Long Papers), pages 15894–15939, Bangkok, Thai-
land. Association for Computational Linguistics.
Liang Wang, Nan Yang, Xiaolong Huang, Linjun Yang,
Rangan Majumder, and Furu Wei. 2024a. Multilin-
gual e5 text embeddings: A technical report. arXiv
preprint arXiv:2402.05672.
Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng
Ni, Abhranil Chandra, Shiguang Guo, Weiming
Ren, Aaran Arulraj, Xuan He, Ziyan Jiang, et al.
2024b. MMLU-pro: A more robust and challeng-
ing multi-task language understanding benchmark.
arXiv preprint arXiv:2406.01574.
Jason Wei, Maarten Bosma, Vincent Zhao, Kelvin Guu,
Adams Wei Yu, Brian Lester, Nan Du, Andrew M
Dai, and Quoc V Le. 2021. Finetuned language mod-
els are zero-shot learners. In International Confer-
ence on Learning Representations.
Jun Zhao, Zhihao Zhang, Qi Zhang, Tao Gui, and Xu-
anjing Huang. 2024. Llama beyond english: An em-
pirical study on language capability transfer. arXiv
preprint arXiv:2401.01055.
Banghua Zhu, Evan Frick, Tianhao Wu, Hanlin Zhu,
and Jiantao Jiao. 2023. Starling-7b: Improving llm
helpfulness & harmlessness with rlaif.
Dmitry Zmitrovich, Alexander Abramov, Andrey
Kalmykov, Maria Tikhonova, Ekaterina Taktasheva,
Danil Astafurov, Mark Baushenko, Artem Snegirev,
Tatiana Shavrina, Sergey Markov, et al. 2023. A
family of pretrained transformer language models for
russian. arXiv preprint arXiv:2309.10931.

```
