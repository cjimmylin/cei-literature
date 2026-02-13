---
title: "2024-Dou-SailCompass Towards Reproducible and Robust Evaluation - PDF Extract"
source_pdf: "2024-Dou-SailCompass Towards Reproducible and Robust Evaluation.pdf"
pages: 20
extracted_at: "2026-02-13T09:15:42.590574"
---

# PDF Extract: 2024-Dou-SailCompass Towards Reproducible and Robust Evaluation

**Source PDF:** 2024-Dou-SailCompass Towards Reproducible and Robust Evaluation.pdf
**Total Pages:** 20

---

## Content

```
--- Page 1 ---

arXiv:2412.01186v1  [cs.CL]  2 Dec 2024
SAILCOMPASS: Towards Reproducible and Robust
Evaluation for Southeast Asian Languages
Jia Guo1∗, Longxu Dou2∗, Guangtao Zeng3, Stanley Kok1, Wei Lu3, Qian Liu2†
1National University of Singapore; 2Sea AI Lab;
3Singapore University of Technology and Design
guojia@u.nus.edu, skok@comp.nus.edu.sg
{doulx, liuqian}@sea.com
Abstract
In this paper, we introduce SailCompass, a reproducible and robust evaluation
benchmark for assessing Large Language Models (LLMs) on Southeast Asian
Languages (SEA). SailCompass encompasses three main SEA languages, eight
primary tasks including 14 datasets covering three task types (generation, multiple-
choice questions, and classiﬁcation). To improve the robustness of the evaluation
approach, we explore different prompt conﬁgurations for multiple-choice ques-
tions and leverage calibrations to improve the faithfulness of classiﬁcation tasks.
With SailCompass, we derive the following ﬁndings: (1) SEA-specialized LLMs
still outperform general LLMs, although the gap has narrowed; (2) A balanced lan-
guage distribution is important for developing better SEA-specialized LLMs; (3)
Advanced prompting techniques (e.g., calibration, perplexity-based ranking) are
necessary to better utilize LLMs. All datasets and evaluation scripts are public3.
1
Introduction
Recent advancements in Large Language Models (LLMs) have led to numerous successful applica-
tions in language understanding and generation. However, current LLM research are mainly focus
on English, Chinese and other Western languages, often overlooking other languages especially for
low-resource languages like SEA languages. Southeast Asia (SEA) is a vital region worldwide,
comprising 11 countries and a population of approximately 675 million people (8.5% of the world).
For NLP research, SEA region boasts remarkable linguistic diversity, which provides an ideal re-
search ground for multilingual studies. For instance, Indonesia alone has over 700 languages spoken
daily [3], and also presents linguistic similarities, such as the shared terminology between Malay and
Indonesian due to their intertwined history and culture.
Recently, SEA languages have witness several outstanding open models like SeaLLM [27],
Sealion [2] and Sailor [14], which are built from scratch or continual pre-training on English-centric
models. However, most SEA benchmarks are either narrowed in task diversity or limited in exam-
ples scale, could not trustworthy measure the model performance. We believe that a reproducible
and robust evaluation system for LLMs, could largely assist the researchers to assess the the sys-
tem’s reliability and quantify the existing drawbacks. It just likes a Compass for the Sailors to ship
in the Sea.
In this paper, we present SailCompass, a reproducible and robust evaluation system for SEA lan-
guages in LLM era. Our main contributions include benchmark, evaluation approache and evalua-
tion ﬁndings.
∗The ﬁrst two authors contributed equally.
†Corresponding author
3https://github.com/sail-sg/sailcompass

--- Page 2 ---

Comprehensive Evaluation Datasets (1) For evaluation faithfulness, we encompass three main
SEA languages, eight primary tasks across three task formulations types (i.e., generation, multi-
choice questions and classiﬁcation), that demanding for both language proﬁciency and cultural
understanding. (2) For evaluation efﬁciency, we build SailCompass on the OpenCompass frame-
work [28], for efﬁcient running, extensible conﬁguration and better visualization.
Robust Evaluation Approach (1) For multiple-choice question tasks, we explore all prompt vari-
ants to identify the most robust conﬁgurations. (2) For classiﬁcation tasks, we leverage calibration
to mitigate label bias and generate faithful outputs instead of meaningless random ones.
Insightful Findings for Future Work (1) We investigate the performance gap between general
LLMs and SEA-specialized LLMs to analyse the future trend for application usage. (2) We highlight
the importance of balanced language distribution for developing better SEA LLMs, certiﬁed by the
performance of machine translation and text summarization. (3) We recognize the signiﬁcance of
advanced prompting technique (e.g., calibration, PPL-based ranking) for make better use of LLMs.
2
Related Work
This section focuses on SEA benchmarks. Refer to App. B for general multilingual benchmarks.
SEA benchmarks for Base Model NusaCrowd [8] introduced the ﬁrst large Indonesian benchmark
containing 137 datasets and over 200 tasks across 19 Indonesian languages. BHASA [22] presented
an evaluation suite containing linguistic and cultural evaluations for SEA languages. But BHASA
only cares for zero-shot evaluation of API models like GPT-3.5, and only limited dataset size. SeaE-
val [43] additionally considers the cultural understanding ability of models, but the majority of the
datasets are still based on high-resource languages, such as English and Chinese.
SEA benchmarks for Chat Model Sea-bench [27] is a multilingual dataset with instructions across
9 SEA languages for evaluating chat model, examining ﬁve abilities like math, safety and task-
solving. The linguists sourced the data by manually translating open-source English test sets, collect-
ing real user questions from local forums and websites, collecting real math and reasoning questions,
writing test instructions and questions themselves.
Distinguishing from these works, SailCompass aims to examine the instruction-following and few-
shot learning ability of open-source LLMs through a considerable amount of tasks and datasets, with
meticulous curation of datasets collected directly from native sources. Additionally, SailCompass
places particular emphasis on evaluating tasks with multiple-choice targets and providing valuable
insights through analysis.
In this work, SailCompass focus on open base model evaluation, covering three main SEA languages
and 14 tasks, utilizing prompting and calibration to realize a robust evaluation benchmark.
3
SailCompass Benchmark
This section introduces SAILCOMPASS, an integrated evaluation suite, encompassing (1) the com-
prehensive multilingual benchmarks; (2) the reproducible evaluation codebase.
3.1
Benchmark Construction Principle
Prioritizing by the number of speakers, we consider three SEA languages: Indonesian, Vietnamese,
and Thai. To build a comprehensive benchmark, we ﬁrst identify four pivotal aspects for evaluat-
ing language models: (1) language proﬁciency; (2) reading comprehension; (3) reasoning ability;
(4) cultural understanding. Based on these principles, we select a range of tasks and high-quality
datasets.
In addition to task diversity, we prefer datasets created by native speakers and built on native corpora
rather than translated from English benchmarks. These native benchmarks involve more localized
entities, better examining the models’ ability in cultural understanding and geographical knowledge.
Unfortunately, such native-created datasets are limited, even after our best efforts to collect them.
Thus, we also select high-quality multilingual datasets, like XNLI [12] and XQuAD [4], to further
supplement the number of datasets.
2

--- Page 3 ---

Table 1: Our benchmark includes eight tasks: Question Answering (QA), Machine Translation (MT),
Text Summarization(TS), Examination (Exam), Commonsense Reasoning (CR), Machine Reading
Comprehension (MRC), Natural Language Inference (NLI), and Sentiment Analysis (SA).
Type
Datasets
Thai
Indonesian
Vietnamese
Task
Domain
GEN
XQUAD
1,149
–
1,169
Wikipedia
TYDIQA
–
565
–
QA
Wikipedia
FLORES-200
1,012
1,012
1,012
MT
Wikipedia
THAISUM
3,671
–
–
News
INDOSUM
–
3,762
–
News
XLSUM
–
–
2,676
TS
News
MCQ
M3EXAM
2,163
371 4
1,789
Exam
School materials
XCOPA
500
500
500
CR
General
BELEBELE
900
900
900
MRC
General
CLS
XNLI
5,010
–
5,010
Multi-genre
INDONLI
–
5,182
–
NLI
Multi-genre
WISESIGHT
2,614
–
–
Social media
INDOLEM
–
1,002
–
Social media
VSMEC
–
–
692
SA
Social media
3.2
Task and Dataset Construction
We construct SailCompass on eight tasks across three task types. 5 Refer to Table 1 for statistics.
(1) Generation tasks (GEN): Generate the token sequence given sequence input.
• Question Answering (QA) generates an answer span given the question and passage. We
employ XQUAD [4] for Thai and Vietnamese and TYDIQA [11] for Indonesian. XQUAD is
translated from the English SQUAD [33], while TYDIQA is built on native language corpus.
• Machine Translation (MT)
We employ FLORES-200 [13], which sourced data from web articles and annotated by profes-
sional translators. We examine bi-directional translation performance between the target SEA
languages and English, to examine the cross-lingual capability.
• Text Summarization (TS) examines the ability to compress the key information from the
paragraph. For Thai, we adopt THAISUM[10], and for Indonesian, we use INDOSUM[21],
both built on native language corpora. For Vietnamese, we adopt XLSUM [15] for evaluation.
(2) Multiple-choice questions (MCQ): Select the answer given a question and several options.
• Examination (Exam) reﬂects the integrated intelligence of reasoning with domain knowledge.
We use M3EXAM [46], built on school textbook, covering a range of subjects and levels. 6
• Commonsense Reasoning (CR) asks model to answer questions about commonsense under-
standing in daily scenario. We adopt XCOPA [31] for evaluation.
• Machine Reading Comprehension (MRC) evaluates different levels of language comprehen-
sion. We adopt BELEBELE [7] for evaluation, whose passage is from FLORES-200 [13].
(3) Classiﬁcation tasks (CLS): Predict a label from a predeﬁned set of categories.
• Natural Language Inference (NLI) Given a premise and a hypothesis, the model needs to
select one correct answer from three labels to indicate their logical relation, i.e., Entailment,
Contradiction, Neutral. We include XNLI [12] for Thai and Vietnamese, and INDONLI
[25] for Indonesian.
• Sentiment Classiﬁcation (SC) aims to label the given text by different human feelings. We use
WISESIGHT [37] for Thai, INDOLEM [20] for Indonesian, and VSMEC [17] for Vietnamese.
They are all build the social media messages in native language.
5For datasets that no publicly available test set, we employ the validation set, like TydiQA.
6We use the Javanese split here, as M3Exam had not released the Indonesian split when submitting this
paper.
3

--- Page 4 ---

3.3
Instruction and Few-Shot Example Collection
For the selection of few-shot examples, we randomly select three examples from the training datasets
or development datasets. For text summarization tasks, we only choose one example for demonstra-
tion. For each task, we employ a professional expert to write the task instructions in English and
translate them by Google Translate or ChatGPT to the respective SEA languages.
3.4
Evaluation Protocol
Our evaluation code are developed based on the open-source evaluation platform OpenCompass [28],
an integrated framework that offers extensive conﬁgurations for assessing a broad range of large
language models and datasets. It features efﬁcient distributed evaluation to expedite processes and
seamlessly incorporates support for new models and datasets.
We specialize in evaluating open-source base language models, which are easily accessible to a
broad community. Our benchmarking efforts aim to enhance the transparency and reproducibility of
large language model evaluations. We employ greedy decoding for all experiments.
For Generation Tasks, we report BLEU [29] and Chrf++ [32]. For MCQ Tasks, we report Exact
Match. For Classiﬁcation Tasks, we report Exact Match and F1 Score.
3.5
Evaluated Models
All the evaluated models are base model, without instruction tuning and preference optimization
(i.e., RLHF). We don’t consider the instruction/chat model, for estimating the upper bound of each
model before post-training.
7 For model size, considering the trade-off between efﬁciency and effectiveness, we mainly consider
the base model with size around 7B parameters. Refer to Table 6 for more details.
According to language distribution of the training corpus and model optimization methods, we cate-
gorized these models into three types:
• General LLMs: general multilingual models, whose training corpus cater for multilingual
tokens, but mainly focus on western languages. It includes BLOOM [45], Llama-2 [40],
Mistral [19], Qwen1.5 [6], Llama-38, and Gemma [38].
• SEA-speciﬁc LLMs by continual pretraining: train the General LLMs with SEA corpus,
including VinaLLaMA [26], SeaLLM [27], Sailor [14] and Typhoon [30].
• SEA-speciﬁc LLMs by training from scratch: training corpus consists of a signiﬁcant
number of SEA tokens and employ SEA friendly tokenizer, including Sea-Lion [2].
For brevity, we collectively refer to the latter two groups of models as ‘SEA-speciﬁc LLMs’.
4
Generation Tasks
In this section, we focus on generation tasks, the most frequent reply format in real life. The evalu-
ation for generation tasks is more robust than MCQ tasks and classiﬁcation tasks. It’s much easier
for researchers to receive the consistent performance even under different conﬁgurations (e.g., alter-
ing the order of demonstrations, changing the number of demonstrations). Thus, we suppose that
generation tasks have been the mature tasks, serving as a satisfying measurement for base models.
We aims to explore the following aspects: (1) the performance gap among general LLMs, SEA-
speciﬁc LLMs and task-speciﬁc models, to see could we could solve the speciﬁc SEA tasks by
developing LLMs; (2) the pair-wise comparison between different model families (base model and
cft model), to identify the key continual pre-training factors.
7We deﬁne a base model as one that is primarily trained on plain text, having weak instruction-following
ability under a few-shot setting. SeaLLM did not release its base model. Thus, we adopt SeaLLM-Hybrid
instead, which is obtained by training SeaLLM-base on a small set of instruction examples for security reasons.
8https://github.com/meta-llama/llama3
4

--- Page 5 ---

Qwen-1.5-7B Llama-3-8B Mistral-7B
Gemma-7B
Typhoon-8B
NLLB-3.3B GPT3.5-turbo Sailor-7B
SeaLLM-7B Sea-Lion-7B
0
20
40
60
Chrf++
En
Id
En
Th
En
Vi
(a) Machine Translation (En-X)
Qwen-1.5-7B Llama-3-8B Mistral-7B
Gemma-7B
Typhoon-8B
NLLB-3.3B GPT3.5-turbo Sailor-7B
SeaLLM-7B Sea-Lion-7B
0
20
40
60
BLEU
Id
En
Th
En
Vi
En
(b) Machine Translation (X-En)
Figure 1: Machine translation results with Chrf++ as evaluation metric.
4.1
Machine Translation
We list the evaluation results with bi-direction in Figure 1. We notice that Thai is really challenging
in both directions for different models. In the following, we summarize several useful ﬁndings.
English Prompt is Better Than Native Prompt
(1) more balanced data distribution produces
the more balanced model. Gemma and sailor, both have tiny difference between different language
prompts; (2) sealion pretraining corpus are mainly SEA languages, thus its native prompt is better
than English prompt; (3) overall, most model would beneﬁt from the English prompt. We would
recommend to use English prompt in the real machine translation scenarios. But considering the
usage scenario (SEA area prefer to use SEA languages rather than English), and the acceptable per-
formance gap between native prompts and English prompts (less than 0.5 Chrf++), we will mainly
report native prompts results in the following sections.
English-to-X is Harder Than X-to-English
Generally, we suppose that ‘X->English’ is much
easier than ‘English->X’, where X stands for a speciﬁc language and ‘->’ indicates the the translation
direction [24]. With this criteria, we further explore the challenge of Thai. First, as expected,
‘Thai->English’ is always better than ‘English->Thai’. Then, we calculate the Chrf++ difference by
‘English->Thai’ minus ‘Thai->English’. We ﬁnd this number is consistently larger than 10 across
different model, which indicates the severe language degeneration happens in Thai.
Balanced Language Distribution Alleviates Language Degeneration
We deﬁne a model has
‘language degeneration’ problem, if its Chrf++ difference becomes larger after continual pre-training.
Based on this, we observe that the Chrf++ difference of sailor/seallm/sealion are obviously smaller
that others. It indicates that their balanced language distribution beneﬁt the translation task.
LLMs Could Be Comparable with Specialized MT Models
We compare the LLMs with the
strong specialized baselines: (1) NLLB-3.3B [39], the speciﬁc machine translation model for more
than 200 languages 9; (2) GPT-3.5-Turbo, the well-known commerical LLM.10 We observe that
Llama/Gemma/Sailor are closed to basline performance, even they are built for general usage.
9The results of NLLB-3.3B are from https://tinyurl.com/nllb200dense3bmetrics by NLLB Team.
10The results of GPT are from Lu et al. [24].
5

--- Page 6 ---

XQuAD (Th)
TiDiQA (Id)
XQuAD (Vi)
0
20
40
60
Exact Match
Qwen-1.5-7B
Llama-2-7B
Llama-3-8B
Mistral-7B
Gemma-7B
Typhoon-8B
Sailor-7B
SeaLLM-7B
Sea-Lion-7B
Figure 2: Question Answering results with Exact Match as evaluation metric.
Table 2: Main results on the text summarization task, measured in BLEU. Each group contains
the general LLM and their derived continual pre-training models. As shown, continual pre-training
generally boost the model performance in summarization, but it is challenging to achieve better
performance on all languages.
Model
Text Summarization
THAISUM (th)
INDOSUM (id)
XLSUM (vi)
Mistral-7B
16.78
46.55
6.02
Gemma-7B
14.29
36.65
4.70
BLOOM-7B1
0.24
26.76
2.26
Sea-Lion-7B
22.30
30.98
3.67
Qwen-1.5-7B
9.99
36.96
3.24
Sailor-7B
27.23
47.60
5.65
Llama-2-7B
17.10
48.34
4.67
VinaLLaMA-7B
2.60
39.24
5.92
SeaLLM-7B
18.50
48.68
4.60
Llama-3-8B
16.84
38.86
3.35
Typhoon-8B
19.37
38.66
2.44
4.2
Question Answering
The results are listed in Figure 2. We observe that Llama-8b, Gemma-7b, Qwen.5-7b, and Sailor-
7b demonstrate the best performances across all languages, according to their boost above average
performance.
It’s impressive that TYDIQA (Indonesian) receives the highest performance across all models, con-
sidering that TyDiQA is more challenging. TYDIQA is built directly from corpora in the target
languages, taking into account more linguistic features and requiring the model to understand cul-
tural and geographical knowledge, while XQUAD is translated from the English SQUAD [33]. This
conclusion aligns with Indonesian being a high-resource language (learning more common knowl-
edge) and also sharing some word similarities with English (learning more linguistic knowledge).
4.3
Text Summarization
We suppose that the summarization task is one of the most challenging generation tasks, as it ex-
amines the ability to identify and compress key information from paragraph. This task could reﬂect
the model’s performance in complex real-world scenarios, such as long-context document question-
answering and retrieval-augmented generation.
From Table 2, we observe that: (1) Sailor-7B achieves the best overall performance, especially
for Thai; (2) Vietnamese is the most challenging language for summarization, with performance
nearly half that of other languages; (3) While the target language performances of Typhoon and
Vinallama improve after continued pretraining, other languages degenerate. This indicates that their
monolingual-speciﬁc continual pretraining greatly hurts the models’ multilingual performance, high-
lighting the need for a balanced language distribution in the training data.
6

--- Page 7 ---

5
Multiple-Choice Tasks
Robust MCQ tasks evaluation faces three main challenges: (1) sensitivity to alterations, including
general prompt formatting [36, 35] and MCQ-speciﬁc ones like option ordering [34]; (2) option
bias [48], arising from intrinsic token bias, which becomes more severe when predicting only the
option ID; (3) disparities across various evaluation criteria, making it harder to align different
evaluation results. For instance, the MCQ tasks evaluation mismatch rate is high between predictions
derived from generated text output, and those based on ﬁrst-token probability ranking [44].
In this section, we analyze the key factors impacting the MCQ evaluation performance, then compare
various evaluation criteria, and ﬁnally determine the best practice through extensive experiments.
5.1
Investigation on Variants of MCQ Prompt
Different Evaluation Approaches
We employ two approaches for evaluating MCQ: generative
method (GEN-based) and the discriminative method (PPL-based). GEN-based inputs the prompt
into the language model and takes the generation as prediction. This approach aligns with realistic
generation performance, but it might generate mismatched predictions. PPL-based appends each
option to the prompt, ranking the concatenated texts by perplexity scores, taking the lowest perplex-
ity option as the answer. This approach avoids mismatches between generations and options.
Different Prompt Conﬁgurations
The key elements in composing MCQ prompt includes the
options ID and options text, which appear in both the input and output. These elements can be
combined in different ways to generate various formats for the input (no-text11, text-only, text with
ID) and output (ID-only, text-only, text with ID). The combination of these formats composes differ-
ent prompt conﬁgurations, which we refer to as different symbols for the input (e.g., Ti, LiTi) and
output (e.g., Lo, To, LoTo). 12 Refer to Appendix A for detailed explanation of ﬁve prompt variants.
Comparison with Different Conﬁgurations under Different Approaches
Under various con-
ﬁgurations, we evaluate General LLMs and SEA-speciﬁc LLMs on Thai split of BELEBELE (Ta-
ble 3). We notice signiﬁcant variations in model performance when the prompt changes: (1) when
LLMs are required to give the answer text as the prediction (To), introducing either option content
(LiTiTo) or the option ID (TiTo) in the prompt cause performance degradation. (2) For LiTiLo,
Gen-based eval and PPL-based eval are nearly identical across various models, which illustrates that
the choice to adopt either generative or discriminative methods is not the primary factor causing
the performance ﬂuctuations. (3) Compared to the setting ToP P L, it is worth noting that the results
of Mistral-7B and Sailor-7B are signiﬁcantly improved by 40% and 47 %, respectively, when
models are restricted to predicting the correct option ID in the setting of PPL-based (LiTiLoP P L),
evaluating Mistral-7B to the second best position for Southeast Asian languages.
Table 3: Experiments on the BELEBELE (th) benchmark measured in Exact Match (EM).
Model
ToP P L
TiToP P L
LiTiToP P L
LiTiLoP P L
LiTiLoGEN
LiTiLoToP P L
Llama-2-7B
32.44
25.22
26.89
26.11
27.56
25.11
Mistral-7B
34.44
28.11
30.33
48.22
49.00
28.11
Sea-Lion-7B
36.78
25.78
27.44
25.33
25.44
25.56
SeaLLM-7B
37.44
28.56
29.56
38.22
38.44
28.33
Sailor-7B
42.56
32.44
36.44
62.56
62.78
33.89
5.2
Measure the Robustness of MCQ Prompt Varients
We ﬁrst propose three measures in evaluating the robustness of prompt variants: (1) mitigating token
bias towards speciﬁc option IDs; (2) remaining unbiased regarding the surface form of options; (3)
resisting manipulation intended to inﬂate model performance.
11Equivalent to common question answering task under GEN-based evaluation approach.
12Interpretion of symbols: T: option text, L: option label, i: model input, o: model output.
7

--- Page 8 ---

To
TiTo
LiTiTo
LiTiLo LiTiLoTo
0
0.1
0.2
0.3
Recall std
Sea-Lion-7B
SeaLLM-7B
Sailor-7B
To
TiTo
LiTiTo
LiTiLo LiTiLoTo
0
10
20
30
40
Relative length discrepancy (%)
Sea-Lion-7B
SeaLLM-7B
Sailor-7B
Figure 3: Analysis of prediction bias across prompt variants, with PPL-based evaluation approach.
Table 4: Experiments on MCQ benchmark measured in Exact Match (EM) with manipulated train-
ing.
M3Exam
ToP P L
LiTiLoP P L
LiTiLoGEN
th
jv
vi
th
jv
vi
th
jv
vi
QWEN1.5-7B
25.75
26.15
36.28
36.89
31.54
51.31
35.88
32.35
51.09
QWEN1.5-7BM
27.23
26.15
36.61
37.49
34.50
52.93
36.80
32.61
52.88
△avg
0.07
0.14
0.07
BELEBELE
ToP P L
LiTiLoP P L
LiTiLoGEN
id
vi
th
id
vi
th
id
vi
QWEN1.5-7B
37.89
42.11
42.56
64.33
72.11
73.78
47.89
62.22
44.44
QWEN1.5-7BM
37.89
40.67
42.33
64.78
72.89
77.00
58.00
71.11
71.33
△avg
-0.04
0.06
0.96
Does MCQ evaluation favor speciﬁc option IDs?
Following Zheng et al. [48], we adopt the
standard deviation of recall across options as the metric to measure option ID bias As shown in
Figure 3 (left), LiTiLo exhibits the highest standard deviation in recall. This suggests that LiTiLo
inﬂuences the model to produce imbalanced predictions towards speciﬁc option IDs. In contrast, the
prompts that include the option text (i.e., containing To) mitigate the potential biases associated with
option IDs. Additionally, different models demonstrate distinct preferences for different prompts.
For instance, SEA-LION-7B and Sailor-7B exhibit low performance, while SeaLLM-7B performs
well.
Does MCQ evaluation prefer speciﬁc option surface forms?
We use character-level length to
measure surface form bias. Figure 3 (right) shows the relative length discrepancy (%) of model pre-
dictions with prompt variants, indicating whether prediction lengths overestimate or underestimate
reference options. Incorporating option text like To biases models towards longer options. To ex-
hibits lower bias, indicating greater resilience against length biases. LiTiLo, only outputting option
ID, is unaffected by length bias but introduces severe token bias as discussed above.
Can evaluation performance be manipulated?
From the above analysis, we prioritize two
prompt conﬁgurations: To and LiTiTo. To demonstrates resilience to selection biases in both op-
tion ID and length. LiTiTo is robust to option length bias but more sensitive to option ID bias. To
determine the ﬁnal conﬁguration, we conduct a manipulated training experiment using a subset of
MMLU [16] (MCQ datasets) to ﬁt the evaluation prompt format (Table 4). Refer to Appendix C for
details. With manipulated training, the model shows a signiﬁcant 17.2% improvement with prompt
LiTiLo. Interestingly, SEA languages performance improves with manipulated training on English
data but weakens the reliability of LiTiLo. In contrast, To performance decreases by about 1.8%
8

--- Page 9 ---

Table 5: Main results on the classiﬁcation task measured in Exact Match (EM).
Model
Natural Language Inference
Sentiment Classiﬁcation
XNLI (th)
INDONLI (id)
XNLI (vi)
WISESENTI (th)
INDOLEM (id)
VSMEC (vi)
Random
33.33
33.33
33.33
33.33
50.00
14.29
Llama-3-8B
35.25
35.31
36.19
46.44
86.03
19.51
Mistral-7B
31.96
33.62
33.67
46.25
70.86
9.1
Gemma-7B
35.63
36.92
35.71
43.23
85.23
20.81
Falcon-7B
33.75
33.44
34.19
48.74
79.84
6.65
Qwen-1.5-7B
36.47
35.30
38.28
35.73
83.03
21.24
Llama-2-7B
32.65
33.11
33.35
51.87
81.54
18.5
Typhoon-8B
34.85
34.20
33.49
30.64
72.75
7.51
VinaLLaMA-7B
30.94
35.14
37.74
47.05
30.94
20.09
Sailor-7B
35.89
37.88
34.89
32.44
80.44
24.42
SeaLLM-7B
35.77
35.22
34.27
31.71
76.15
20.23
Sea-Lion-7B
33.65
34.74
32.50
32.36
84.73
18.35
with manipulated training, suggesting challenges in achieving higher performance with scaled-up
training.
In summary, we employ the prompt conﬁguration ToP P L as the recommended evaluation approach
for MCQ tasks of SailCompass, to ensure a robust evaluation.
6
Classiﬁcation Tasks
Compared with generation tasks and MCQ tasks, classiﬁcation tasks are the most challenging ones.
They are more sensitive to evaluation factors due to majority label bias, common token bias, and
recency bias [47]. This inevitably prevents researchers from obtaining trustworthy evaluation results.
In this section, we address the challenge with Contextual Calibration [47], which can effectively
increase the probability of generating convincing predictions, thus avoiding the underestimation
issue. First, we estimate the bias via context-free test input, then counter the bias by normalizing
the SoftMax scores of label. Thus alleviate the underestimation problem by label bias. We present
more detail about the calibration in Appendix D.
Results
The results for NLI and sentiment classiﬁcation tasks are shown in Table 5. We notice
that base models can not achieve a good performance in NLI tasks with marginally improvement
compared to random choose. Compared to NLI task, language models can achieve better results on
sentiment classiﬁcation tasks.
7
Conclusion
In this work, we present SailCompass, a comprehensive suite of evaluation scripts designed for
robust and reproducible evaluation of multilingual language models targeting Southeast Asian lan-
guages. SailCompass encompasses three major SEA languages and covers eight primary tasks using
14 datasets, spanning three task types: generation, multiple-choice questions, and classiﬁcation. To
enhance the robustness of our evaluation approach, we explore different prompt conﬁgurations for
multiple-choice questions and employ calibration methods to improve the accuracy of classiﬁca-
tion tasks. Through SailCompass, we have derived several key ﬁndings regarding model continual
pretraining and robust model evaluation.
We believe that SailCompass will be highly beneﬁcial for the development of large language models
tailored to the Southeast Asia region, providing a crucial resource for researchers in this area.
Limitations
For the evaluation benchmark:
9

--- Page 10 ---

1. Model Type: The current version of SailCompass focuses solely on base models for few-
shot evaluation. Future versions should also consider incorporating chat tasks for zero-shot
evaluation.
2. Language Coverage: SailCompass currently supports three languages.
Future work
should expand coverage to include more Southeast Asian languages, such as Malay, Lao,
and Khmer.
3. Task Type: At present, SailCompass includes tasks for text generation, multi-question
answering, and classiﬁcation. Future iterations should also encompass advanced tasks such
as mathematics, coding, and other specialized domains.
For the evaluation methods:
1. Prompt Construction: SailCompass currently explores different prompt conﬁgurations,
but the prompt templates are still manually constructed. Future work should focus on
optimizing prompts for each model.
2. Calibration Methods: SailCompass currently utilizes contextual calibration, which is
more effective for one-token label predictions. Future research should explore Domain
Conditional PMI, which is more general by removing surface form competition and ad-
dressing general output bias.
Ethics Statement
This work presents the SailCompass benchmark, which is built upon existing datasets. The related
licenses of these datasets are all open for academic usage, ensuring compliance with their terms and
conditions. We did not build any new datasets for this work. All code, models, and data used in this
research are publicly accessible. We are committed to open science and have made all our resources
available to the community to facilitate further research and development in this ﬁeld.
References
[1] Kabir Ahuja, Harshita Diddee, Rishav Hada, Millicent Ochieng, Krithika Ramesh, Prachi
Jain, Akshay Uttama Nambi, Tanuja Ganu, Sameer Segal, Mohamed Ahmed, Kalika Bali,
and Sunayana Sitaram. MEGA: multilingual evaluation of generative AI. In Proceedings of
the 2023 Conference on Empirical Methods in Natural Language Processing, EMNLP 2023,
pages 4232–4267, 2023. URL https://doi.org/10.18653/v1/2023.emnlp-main.258.
[2] AI Singapore. Sea-lion (southeast asian languages in one network): A family of large language
models for southeast asia. https://github.com/aisingapore/sealion, 2023.
[3] Alham Fikri Aji, Genta Indra Winata, Fajri Koto, Samuel Cahyawijaya, Ade Romadhony, Rah-
mad Mahendra, Kemal Kurniawan, David Moeljadi, Radityo Eko Prasojo, Timothy Baldwin,
Jey Han Lau, and Sebastian Ruder. One country, 700+ languages: NLP challenges for under-
represented languages and dialects in Indonesia. In Smaranda Muresan, Preslav Nakov, and
Aline Villavicencio, editors, Proceedings of the 60th Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers), pages 7226–7249, Dublin, Ireland, May
2022. Association for Computational Linguistics. doi: 10.18653/v1/2022.acl-long.500. URL
https://aclanthology.org/2022.acl-long.500.
[4] Mikel Artetxe, Sebastian Ruder, and Dani Yogatama.
On the cross-lingual trans-
ferability of monolingual representations.
In Proceedings of the 58th Annual Meet-
ing of the Association for Computational Linguistics,
ACL 2020,
Online,
July 5-
10, 2020, pages 4623–4637. Association for Computational Linguistics, 2020.
URL
https://doi.org/10.18653/v1/2020.acl-main.421.
[5] Akari Asai, Sneha Kudugunta, Xinyan Velocity Yu, Terra Blevins, Hila B Gonen, Machel
Reid, Yulia Tsvetkov, Sebastian Ruder, and Hannaneh Hajishirzi. BUFFET: Benchmarking
large language models for cross-lingual few-shot transfer. In NAACL, 2024.
10

--- Page 11 ---

[6] Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin
Ge, Yu Han, Fei Huang, Binyuan Hui, Luo Ji, Mei Li, Junyang Lin, Runji Lin, Dayiheng Liu,
Gao Liu, Chengqiang Lu, Keming Lu, Jianxin Ma, Rui Men, Xingzhang Ren, Xuancheng Ren,
Chuanqi Tan, Sinan Tan, Jianhong Tu, Peng Wang, Shijie Wang, Wei Wang, Shengguang Wu,
Benfeng Xu, Jin Xu, An Yang, Hao Yang, Jian Yang, Shusheng Yang, Yang Yao, Bowen Yu,
Hongyi Yuan, Zheng Yuan, Jianwei Zhang, Xingxuan Zhang, Yichang Zhang, Zhenru Zhang,
Chang Zhou, Jingren Zhou, Xiaohuan Zhou, and Tianhang Zhu. Qwen technical report, 2023.
[7] Lucas Bandarkar, Davis Liang, Benjamin Muller, Mikel Artetxe, Satya Narayan Shukla, Don-
ald Husa, Naman Goyal, Abhinandan Krishnan, Luke Zettlemoyer, and Madian Khabsa. The
belebele benchmark: a parallel reading comprehension dataset in 122 language variants. CoRR,
abs/2308.16884, 2023. URL https://doi.org/10.48550/arXiv.2308.16884.
[8] Samuel Cahyawijaya, Holy Lovenia, Alham Fikri Aji, Genta Indra Winata, Bryan Wilie, Fa-
jri Koto, Rahmad Mahendra, Christian Wibisono, Ade Romadhony, Karissa Vincentio, Jen-
nifer Santoso, David Moeljadi, Cahya Wirawan, Frederikus Hudi, Muhammad Satrio Wicak-
sono, Ivan Halim Parmonangan, Ika Alﬁna, Ilham Firdausi Putra, Samsul Rahmadani, Yu-
lianti Oenang, Ali Akbar Septiandri, James Jaya, Kaustubh D. Dhole, Arie Ardiyanti Suryani,
Rifki Aﬁna Putri, Dan Su, Keith Stevens, Made Nindyatama Nityasya, Muhammad Farid Adi-
lazuarda, Ryan Hadiwijaya, Ryandito Diandaru, Tiezheng Yu, Vito Ghifari, Wenliang Dai, Yan
Xu, Dyah Damapuspita, Haryo Akbarianto Wibowo, Cuk Tho, Ichwanul Muslim Karo Karo,
Tirana Fatyanosa, Ziwei Ji, Graham Neubig, Timothy Baldwin, Sebastian Ruder, Pascale Fung,
Herry Sujaini, Sakriani Sakti, and Ayu Purwarianti. Nusacrowd: Open source initiative for in-
donesian NLP resources. In Findings of the Association for Computational Linguistics: ACL
2023, Toronto, Canada, July 9-14, 2023, pages 13745–13818. Association for Computational
Linguistics, 2023. URL https://doi.org/10.18653/v1/2023.findings-acl.868.
[9] Yiran Chen, Zhenqiao Song, Xianze Wu, Danqing Wang, Jingjing Xu, Jiaze Chen, Hao Zhou,
and Lei Li. MTG: A benchmark suite for multilingual text generation. In Findings of the
Association for Computational Linguistics: NAACL 2022, pages 2508–2527, 2022.
URL
https://doi.org/10.18653/v1/2022.findings-naacl.192.
[10] Nakhun Chumpolsathien. Using knowledge distillation from keyword extraction to improve
the informativeness of neural cross-lingual summarization. Master’s thesis, Beijing Institute
of Technology, 2020.
[11] Jonathan H. Clark, Jennimaria Palomaki, Vitaly Nikolaev, Eunsol Choi, Dan Garrette, Michael
Collins, and Tom Kwiatkowski. Tydi QA: A benchmark for information-seeking question
answering in typologically diverse languages. Trans. Assoc. Comput. Linguistics, 8:454–470,
2020. URL https://doi.org/10.1162/tacl_a_00317.
[12] Alexis Conneau, Ruty Rinott, Guillaume Lample, Adina Williams, Samuel R. Bowman, Hol-
ger Schwenk, and Veselin Stoyanov. XNLI: evaluating cross-lingual sentence representations.
In Proceedings of the 2018 Conference on Empirical Methods in Natural Language Process-
ing, Brussels, Belgium, October 31 - November 4, 2018, pages 2475–2485. Association for
Computational Linguistics, 2018. URL https://doi.org/10.18653/v1/d18-1269.
[13] Marta R. Costa-jussà, James Cross, Onur Çelebi, Maha Elbayad, Kenneth Heaﬁeld, Kevin
Heffernan, Elahe Kalbassi, Janice Lam, Daniel Licht, Jean Maillard, Anna Y. Sun, Skyler
Wang, Guillaume Wenzek, Al Youngblood, Bapi Akula, Loïc Barrault, Gabriel Mejia Gon-
zalez, Prangthip Hansanti, John Hoffman, Semarley Jarrett, Kaushik Ram Sadagopan, Dirk
Rowe, Shannon Spruit, Chau Tran, Pierre Andrews, Necip Fazil Ayan, Shruti Bhosale, Sergey
Edunov, Angela Fan, Cynthia Gao, Vedanuj Goswami, Francisco Guzmán, Philipp Koehn,
Alexandre Mourachko, Christophe Ropers, Saﬁyyah Saleem, Holger Schwenk, and Jeff Wang.
No language left behind: Scaling human-centered machine translation. CoRR, abs/2207.04672,
2022. URL https://doi.org/10.48550/arXiv.2207.04672.
[14] Longxu Dou, Qian Liu, Guangtao Zeng, Jia Guo, Jiahui Zhou, Wei Lu, and Min Lin. Sailor:
Open language models for south-east asia. arXiv preprint arXiv:2404.03608, 2024.
11

--- Page 12 ---

[15] Tahmid Hasan, Abhik Bhattacharjee, Md. Saiful Islam, Kazi Mubasshir, Yuan-Fang
Li,
Yong-Bin Kang,
M. Sohel Rahman,
and Rifat Shahriyar.
XL-sum:
Large-
scale
multilingual
abstractive
summarization
for
44
languages.
In
Findings
of
the Association for Computational Linguistics:
ACL-IJCNLP 2021,
2021.
URL
https://aclanthology.org/2021.findings-acl.413.
[16] Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and
Jacob Steinhardt. Measuring massive multitask language understanding. In 9th International
Conference on Learning Representations, ICLR 2021, Virtual Event, Austria, May 3-7, 2021.
OpenReview.net, 2021. URL https://openreview.net/forum?id=d7KBjmI3GmQ.
[17] Vong Anh Ho, Duong Huynh-Cong Nguyen, Danh Hoang Nguyen, Linh Thi-Van Pham,
Duc-Vu Nguyen, Kiet Van Nguyen, and Ngan Luu-Thuy Nguyen.
Emotion recogni-
tion for vietnamese social media text.
In Computational Linguistics - 16th Interna-
tional Conference of the Paciﬁc Association for Computational Linguistics, PACLING 2019,
Hanoi, Vietnam, October 11-13, 2019, Revised Selected Papers, volume 1215 of Commu-
nications in Computer and Information Science, pages 319–333. Springer, 2019.
URL
https://doi.org/10.1007/978-981-15-6168-9_27.
[18] Junjie Hu, Sebastian Ruder, Aditya Siddhant, Graham Neubig, Orhan Firat, and Melvin
Johnson.
XTREME: A massively multilingual multi-task benchmark for evaluating cross-
lingual generalization.
In Proceedings of the 37th International Conference on Ma-
chine Learning, ICML 2020, Proceedings of Machine Learning Research, 2020.
URL
https://proceedings.mlr.press/v119/hu20b/hu20b.pdf.
[19] Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh
Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile
Saulnier, Lélio Renard Lavaud, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Thibaut
Lavril, Thomas Wang, Timothée Lacroix, and William El Sayed. Mistral 7b, 2023.
[20] Fajri Koto, Afshin Rahimi, Jey Han Lau, and Timothy Baldwin. Indolem and indobert: A
benchmark dataset and pre-trained language model for indonesian NLP. In Proceedings of the
28th International Conference on Computational Linguistics, COLING 2020, Barcelona, Spain
(Online), December 8-13, 2020, pages 757–770. International Committee on Computational
Linguistics, 2020. URL https://doi.org/10.18653/v1/2020.coling-main.66.
[21] Kemal Kurniawan and Samuel Louvan.
Indosum: A new benchmark dataset for indone-
sian text summarization. In 2018 International Conference on Asian Language Processing,
IALP 2018, Bandung, Indonesia, November 15-17, 2018, pages 215–220. IEEE, 2018. URL
https://doi.org/10.1109/IALP.2018.8629109.
[22] Wei Qi Leong, Jian Gang Ngui, Yosephine Susanto, Hamsawardhini Rengarajan, Kengath-
araiyer Sarveswaran, and William-Chandra Tjhi. BHASA: A holistic southeast asian linguistic
and cultural evaluation suite for large language models. CoRR, abs/2309.06085, 2023. URL
https://doi.org/10.48550/arXiv.2309.06085.
[23] Yaobo Liang, Nan Duan, Yeyun Gong, Ning Wu, Fenfei Guo, Weizhen Qi, Ming Gong, Linjun
Shou, Daxin Jiang, Guihong Cao, Xiaodong Fan, Ruofei Zhang, Rahul Agrawal, Edward Cui,
Sining Wei, Taroon Bharti, Ying Qiao, Jiun-Hung Chen, Winnie Wu, Shuguang Liu, Fan Yang,
Daniel Campos, Rangan Majumder, and Ming Zhou. XGLUE: A new benchmark datasetfor
cross-lingual pre-training, understanding and generation. In Proceedings of the 2020 Confer-
ence on Empirical Methods in Natural Language Processing, EMNLP 2020, pages 6008–6018,
2020. URL https://doi.org/10.18653/v1/2020.emnlp-main.484.
[24] Hongyuan Lu, Haoyang Huang, Dongdong Zhang, Haoran Yang, Wai Lam, and Furu
Wei.
Chain-of-dictionary prompting elicits translation in large language models.
ArXiv,
abs/2305.06575, 2023.
[25] Rahmad Mahendra, Alham Fikri Aji, Samuel Louvan, Fahrurrozi Rahman, and Clara
Vania.
Indonli:
A natural language inference dataset for indonesian.
In Proceed-
ings of the 2021 Conference on Empirical Methods in Natural Language Process-
ing, EMNLP 2021, Virtual Event / Punta Cana, Dominican Republic, 7-11 Novem-
ber, 2021, pages 10511–10527. Association for Computational Linguistics, 2021.
URL
https://doi.org/10.18653/v1/2021.emnlp-main.821.
12

--- Page 13 ---

[26] Quan Nguyen, Huy Pham, and Dung Dao. Vinallama: Llama-based vietnamese foundation
model, 2023.
[27] Xuan-Phi Nguyen, Wenxuan Zhang, Xin Li, Mahani Aljunied, Qingyu Tan, Liying Cheng,
Guanzheng Chen, Yue Deng, Sen Yang, Chaoqun Liu, Hang Zhang, and Lidong Bing.
Seallms - large language models for southeast asia.
CoRR, abs/2312.00738, 2023.
URL
https://doi.org/10.48550/arXiv.2312.00738.
[28] OpenCompass Contributors. Opencompass: A universal evaluation platform for foundation
models. https://github.com/open-compass/opencompass, 2023.
[29] Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu.
Bleu:
a method
for automatic evaluation of machine translation.
In Pierre Isabelle, Eugene Charniak,
and Dekang Lin, editors, Proceedings of the 40th Annual Meeting of the Association
for Computational Linguistics, pages 311–318, Philadelphia, Pennsylvania, USA, July
2002. Association for Computational Linguistics.
doi: 10.3115/1073083.1073135.
URL
https://aclanthology.org/P02-1040.
[30] Kunat Pipatanakul, Phatrasek Jirabovonvisut, Potsawee Manakul, Sittipong Sripaisarn-
mongkol, Ruangsak Patomwong, Pathomporn Chokchainant, and Kasima Tharnpipitchai. Ty-
phoon: Thai large language models, 2023.
[31] Edoardo Maria Ponti, Goran Glavas, Olga Majewska, Qianchu Liu, Ivan Vulic, and Anna
Korhonen. XCOPA: A multilingual dataset for causal commonsense reasoning. In Proceedings
of the 2020 Conference on Empirical Methods in Natural Language Processing, EMNLP 2020,
Online, November 16-20, 2020, pages 2362–2376. Association for Computational Linguistics,
2020. URL https://doi.org/10.18653/v1/2020.emnlp-main.185.
[32] Maja Popovi´c.
chrF: character n-gram F-score for automatic MT evaluation.
In Ondˇrej
Bojar, Rajan Chatterjee, Christian Federmann, Barry Haddow, Chris Hokamp, Matthias
Huck, Varvara Logacheva, and Pavel Pecina, editors, Proceedings of the Tenth Work-
shop on Statistical Machine Translation, pages 392–395, Lisbon, Portugal, September
2015. Association for Computational Linguistics.
doi:
10.18653/v1/W15-3049.
URL
https://aclanthology.org/W15-3049.
[33] Pranav Rajpurkar,
Jian Zhang,
Konstantin Lopyrev,
and Percy Liang.
SQuAD:
100,000+ questions for machine comprehension of text.
In Proceedings of the 2016
Conference on Empirical Methods in Natural Language Processing,
2016.
URL
https://aclanthology.org/D16-1264.
[34] Joshua Robinson and David Wingate.
Leveraging large language models for multiple
choice question answering.
In The Eleventh International Conference on Learning Rep-
resentations, ICLR 2023, Kigali, Rwanda, May 1-5, 2023. OpenReview.net, 2023.
URL
https://openreview.net/pdf?id=yKbprarjc5B.
[35] Melanie Sclar, Yejin Choi, Yulia Tsvetkov, and Alane Suhr. Quantifying language models’
sensitivity to spurious features in prompt design or: How i learned to start worrying about
prompt formatting. In The Twelfth International Conference on Learning Representations,
2024. URL https://openreview.net/forum?id=RIu5lyNXjT.
[36] Freda Shi, Xinyun Chen, Kanishka Misra, Nathan Scales, David Dohan, Ed H. Chi, Nathanael
Schärli, and Denny Zhou. Large language models can be easily distracted by irrelevant context.
In International Conference on Machine Learning, ICML 2023, 23-29 July 2023, Honolulu,
Hawaii, USA, volume 202 of Proceedings of Machine Learning Research, pages 31210–31227.
PMLR, 2023. URL https://proceedings.mlr.press/v202/shi23a.html.
[37] Arthit Suriyawongkul, Ekapol Chuangsuwanich, Pattarawat Chormai, and Charin Pol-
panumas.
Pythainlp/wisesight-sentiment:
First release,
September 2019.
URL
https://doi.org/10.5281/zenodo.3457447.
[38] Gemma Team, Thomas Mesnard, Cassidy Hardin, Robert Dadashi, Surya Bhupatiraju, Shreya
Pathak, Laurent Sifre, Morgane Rivière, Mihir Sanjay Kale, Juliette Love, Pouya Tafti,
Léonard Hussenot, Pier Giuseppe Sessa, Aakanksha Chowdhery, Adam Roberts, Aditya
13

--- Page 14 ---

Barua, Alex Botev, Alex Castro-Ros, Ambrose Slone, Amélie Héliou, Andrea Tacchetti,
Anna Bulanova, Antonia Paterson, Beth Tsai, Bobak Shahriari, Charline Le Lan, Christo-
pher A. Choquette-Choo, Clément Crepy, Daniel Cer, Daphne Ippolito, David Reid, Elena
Buchatskaya, Eric Ni, Eric Noland, Geng Yan, George Tucker, George-Christian Muraru,
Grigory Rozhdestvenskiy, Henryk Michalewski, Ian Tenney, Ivan Grishchenko, Jacob Austin,
James Keeling, Jane Labanowski, Jean-Baptiste Lespiau, Jeff Stanway, Jenny Brennan, Jeremy
Chen, Johan Ferret, Justin Chiu, Justin Mao-Jones, Katherine Lee, Kathy Yu, Katie Millican,
Lars Lowe Sjoesund, Lisa Lee, Lucas Dixon, Machel Reid, Maciej Mikuła, Mateo Wirth,
Michael Sharman, Nikolai Chinaev, Nithum Thain, Olivier Bachem, Oscar Chang, Oscar
Wahltinez, Paige Bailey, Paul Michel, Petko Yotov, Rahma Chaabouni, Ramona Comanescu,
Reena Jana, Rohan Anil, Ross McIlroy, Ruibo Liu, Ryan Mullins, Samuel L Smith, Sebastian
Borgeaud, Sertan Girgin, Sholto Douglas, Shree Pandya, Siamak Shakeri, Soham De, Ted Kli-
menko, Tom Hennigan, Vlad Feinberg, Wojciech Stokowiec, Yu hui Chen, Zafarali Ahmed,
Zhitao Gong, Tris Warkentin, Ludovic Peran, Minh Giang, Clément Farabet, Oriol Vinyals,
Jeff Dean, Koray Kavukcuoglu, Demis Hassabis, Zoubin Ghahramani, Douglas Eck, Joelle
Barral, Fernando Pereira, Eli Collins, Armand Joulin, Noah Fiedel, Evan Senter, Alek An-
dreev, and Kathleen Kenealy. Gemma: Open models based on gemini research and technology,
2024.
[39] Nllb team, Marta Ruiz Costa-jussà, James Cross, Onur cCelebi, Maha Elbayad, Kenneth
Heaﬁeld, Kevin Heffernan, Elahe Kalbassi, Janice Lam, Daniel Licht, Jean Maillard, Anna
Sun, Skyler Wang, Guillaume Wenzek, Alison Youngblood, Bapi Akula, Loïc Barrault,
Gabriel Mejia Gonzalez, Prangthip Hansanti, John Hoffman, Semarley Jarrett, Kaushik Ram
Sadagopan, Dirk Rowe, Shannon L. Spruit, C. Tran, Pierre Yves Andrews, Necip Fazil Ayan,
Shruti Bhosale, Sergey Edunov, Angela Fan, Cynthia Gao, Vedanuj Goswami, Francisco
Guzm’an, Philipp Koehn, Alexandre Mourachko, Christophe Ropers, Saﬁyyah Saleem, Holger
Schwenk, and Jeff Wang. No language left behind: Scaling human-centered machine transla-
tion. ArXiv, abs/2207.04672, 2022.
[40] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei,
Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, Dan Bikel, Lukas
Blecher, Cristian Canton Ferrer, Moya Chen, Guillem Cucurull, David Esiobu, Jude Fernan-
des, Jeremy Fu, Wenyin Fu, Brian Fuller, Cynthia Gao, Vedanuj Goswami, Naman Goyal,
Anthony Hartshorn, Saghar Hosseini, Rui Hou, Hakan Inan, Marcin Kardas, Viktor Kerkez,
Madian Khabsa, Isabel Kloumann, Artem Korenev, Punit Singh Koura, Marie-Anne Lachaux,
Thibaut Lavril, Jenya Lee, Diana Liskovich, Yinghai Lu, Yuning Mao, Xavier Martinet, Todor
Mihaylov, Pushkar Mishra, Igor Molybog, Yixin Nie, Andrew Poulton, Jeremy Reizenstein,
Rashi Rungta, Kalyan Saladi, Alan Schelten, Ruan Silva, Eric Michael Smith, Ranjan Subra-
manian, Xiaoqing Ellen Tan, Binh Tang, Ross Taylor, Adina Williams, Jian Xiang Kuan, Puxin
Xu, Zheng Yan, Iliyan Zarov, Yuchen Zhang, Angela Fan, Melanie Kambadur, Sharan Narang,
Aurelien Rodriguez, Robert Stojnic, Sergey Edunov, and Thomas Scialom. Llama 2: Open
foundation and ﬁne-tuned chat models, 2023.
[41] Alex Wang, Yada Pruksachatkun, Nikita Nangia, Amanpreet Singh, Julian Michael,
Felix Hill,
Omer Levy, and Samuel R. Bowman.
Superglue:
A stickier bench-
mark for general-purpose language understanding systems.
In Advances in Neu-
ral
Information
Processing
Systems
32:
Annual
Conference
on
Neural
Informa-
tion
Processing
Systems
2019,
NeurIPS
2019,
pages
3261–3275,
2019.
URL
https://proceedings.neurips.cc/paper/2019/hash/4496bf24afe7fab6f046bf4923da8de6-Abstract.htm
[42] Alex Wang, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, and Samuel R. Bow-
man. GLUE: A multi-task benchmark and analysis platform for natural language understand-
ing. In 7th International Conference on Learning Representations, ICLR 2019, 2019. URL
https://openreview.net/forum?id=rJ4km2R5t7.
[43] Bin Wang, Zhengyuan Liu, Xin Huang, Fangkai Jiao, Yang Ding, Ai Ti Aw, and Nancy F.
Chen. Seaeval for multilingual foundation models: From cross-lingual alignment to cultural
reasoning. In NAACL, 2024.
[44] Xinpeng Wang, Bolei Ma, Chengzhi Hu, Leon Weber-Genzel, Paul Röttger, Frauke Kreuter,
Dirk Hovy, and Barbara Plank. "my answer is c": First-token probabilities do not match text
answers in instruction-tuned language models, 2024.
14

--- Page 15 ---

[45] BigScience Workshop, :, Teven Le Scao, Angela Fan, Christopher Akiki, Ellie Pavlick, Suzana
Ili´c, Daniel Hesslow, Roman Castagné, Alexandra Sasha Luccioni, François Yvon, Matthias
Gallé, Jonathan Tow, Alexander M. Rush, Stella Biderman, Albert Webson, Pawan Sasanka
Ammanamanchi, Thomas Wang, Benoît Sagot, Niklas Muennighoff, Albert Villanova del
Moral, Olatunji Ruwase, Rachel Bawden, Stas Bekman, Angelina McMillan-Major, Iz Belt-
agy, Huu Nguyen, Lucile Saulnier, Samson Tan, Pedro Ortiz Suarez, Victor Sanh, Hugo Lau-
rençon, Yacine Jernite, Julien Launay, Margaret Mitchell, Colin Raffel, Aaron Gokaslan, Adi
Simhi, Aitor Soroa, Alham Fikri Aji, Amit Alfassy, Anna Rogers, Ariel Kreisberg Nitzav, Can-
wen Xu, Chenghao Mou, Chris Emezue, Christopher Klamm, Colin Leong, Daniel van Strien,
David Ifeoluwa Adelani, Dragomir Radev, Eduardo González Ponferrada, Efrat Levkovizh,
Ethan Kim, Eyal Bar Natan, Francesco De Toni, Gérard Dupont, Germán Kruszewski, Giada
Pistilli, Hady Elsahar, Hamza Benyamina, Hieu Tran, Ian Yu, Idris Abdulmumin, Isaac John-
son, Itziar Gonzalez-Dios, Javier de la Rosa, Jenny Chim, Jesse Dodge, Jian Zhu, Jonathan
Chang, Jörg Frohberg, Joseph Tobing, Joydeep Bhattacharjee, Khalid Almubarak, Kimbo
Chen, Kyle Lo, Leandro Von Werra, Leon Weber, Long Phan, Loubna Ben allal, Ludovic
Tanguy, Manan Dey, Manuel Romero Muñoz, Maraim Masoud, María Grandury, Mario Šaško,
Max Huang, Maximin Coavoux, Mayank Singh, Mike Tian-Jian Jiang, Minh Chien Vu, Mo-
hammad A. Jauhar, Mustafa Ghaleb, Nishant Subramani, Nora Kassner, Nurulaqilla Khamis,
Olivier Nguyen, Omar Espejel, Ona de Gibert, Paulo Villegas, Peter Henderson, Pierre
Colombo, Priscilla Amuok, Quentin Lhoest, Rheza Harliman, Rishi Bommasani, Roberto Luis
López, Rui Ribeiro, Salomey Osei, Sampo Pyysalo, Sebastian Nagel, Shamik Bose, Sham-
suddeen Hassan Muhammad, Shanya Sharma, Shayne Longpre, Somaieh Nikpoor, Stanislav
Silberberg, Suhas Pai, Sydney Zink, Tiago Timponi Torrent, Timo Schick, Tristan Thrush,
Valentin Danchev, Vassilina Nikoulina, Veronika Laippala, Violette Lepercq, Vrinda Prabhu,
Zaid Alyafeai, Zeerak Talat, Arun Raja, Benjamin Heinzerling, Chenglei Si, Davut Emre
Ta¸sar, Elizabeth Salesky, Sabrina J. Mielke, Wilson Y. Lee, Abheesht Sharma, Andrea San-
tilli, Antoine Chafﬁn, Arnaud Stiegler, Debajyoti Datta, Eliza Szczechla, Gunjan Chhablani,
Han Wang, Harshit Pandey, Hendrik Strobelt, Jason Alan Fries, Jos Rozen, Leo Gao, Lintang
Sutawika, M Saiful Bari, Maged S. Al-shaibani, Matteo Manica, Nihal Nayak, Ryan Teehan,
Samuel Albanie, Sheng Shen, Srulik Ben-David, Stephen H. Bach, Taewoon Kim, Tali Bers,
Thibault Fevry, Trishala Neeraj, Urmish Thakker, Vikas Raunak, Xiangru Tang, Zheng-Xin
Yong, Zhiqing Sun, Shaked Brody, Yallow Uri, Hadar Tojarieh, Adam Roberts, Hyung Won
Chung, Jaesung Tae, Jason Phang, Oﬁr Press, Conglong Li, Deepak Narayanan, Hatim Bour-
foune, Jared Casper, Jeff Rasley, Max Ryabinin, Mayank Mishra, Minjia Zhang, Mohammad
Shoeybi, Myriam Peyrounette, Nicolas Patry, Nouamane Tazi, Omar Sanseviero, Patrick von
Platen, Pierre Cornette, Pierre François Lavallée, Rémi Lacroix, Samyam Rajbhandari, Sanchit
Gandhi, Shaden Smith, Stéphane Requena, Suraj Patil, Tim Dettmers, Ahmed Baruwa, Aman-
preet Singh, Anastasia Cheveleva, Anne-Laure Ligozat, Arjun Subramonian, Aurélie Névéol,
Charles Lovering, Dan Garrette, Deepak Tunuguntla, Ehud Reiter, Ekaterina Taktasheva, Eka-
terina Voloshina, Eli Bogdanov, Genta Indra Winata, Hailey Schoelkopf, Jan-Christoph Kalo,
Jekaterina Novikova, Jessica Zosa Forde, Jordan Clive, Jungo Kasai, Ken Kawamura, Liam
Hazan, Marine Carpuat, Miruna Clinciu, Najoung Kim, Newton Cheng, Oleg Serikov, Omer
Antverg, Oskar van der Wal, Rui Zhang, Ruochen Zhang, Sebastian Gehrmann, Shachar
Mirkin, Shani Pais, Tatiana Shavrina, Thomas Scialom, Tian Yun, Tomasz Limisiewicz, Verena
Rieser, Vitaly Protasov, Vladislav Mikhailov, Yada Pruksachatkun, Yonatan Belinkov, Zachary
Bamberger, Zdenˇek Kasner, Alice Rueda, Amanda Pestana, Amir Feizpour, Ammar Khan,
Amy Faranak, Ana Santos, Anthony Hevia, Antigona Unldreaj, Arash Aghagol, Arezoo Ab-
dollahi, Aycha Tammour, Azadeh HajiHosseini, Bahareh Behroozi, Benjamin Ajibade, Bharat
Saxena, Carlos Muñoz Ferrandis, Daniel McDuff, Danish Contractor, David Lansky, Davis
David, Douwe Kiela, Duong A. Nguyen, Edward Tan, Emi Baylor, Ezinwanne Ozoani, Fa-
tima Mirza, Frankline Ononiwu, Habib Rezanejad, Hessie Jones, Indrani Bhattacharya, Irene
Solaiman, Irina Sedenko, Isar Nejadgholi, Jesse Passmore, Josh Seltzer, Julio Bonis Sanz,
Livia Dutra, Mairon Samagaio, Maraim Elbadri, Margot Mieskes, Marissa Gerchick, Martha
Akinlolu, Michael McKenna, Mike Qiu, Muhammed Ghauri, Mykola Burynok, Naﬁs Abrar,
Nazneen Rajani, Nour Elkott, Nour Fahmy, Olanrewaju Samuel, Ran An, Rasmus Kromann,
Ryan Hao, Samira Alizadeh, Sarmad Shubber, Silas Wang, Sourav Roy, Sylvain Viguier,
Thanh Le, Tobi Oyebade, Trieu Le, Yoyo Yang, Zach Nguyen, Abhinav Ramesh Kashyap, Al-
fredo Palasciano, Alison Callahan, Anima Shukla, Antonio Miranda-Escalada, Ayush Singh,
Benjamin Beilharz, Bo Wang, Caio Brito, Chenxi Zhou, Chirag Jain, Chuxin Xu, Clémentine
15

--- Page 16 ---

Fourrier, Daniel León Periñán, Daniel Molano, Dian Yu, Enrique Manjavacas, Fabio Barth,
Florian Fuhrimann, Gabriel Altay, Giyaseddin Bayrak, Gully Burns, Helena U. Vrabec, Imane
Bello, Ishani Dash, Jihyun Kang, John Giorgi, Jonas Golde, Jose David Posada, Karthik Ran-
gasai Sivaraman, Lokesh Bulchandani, Lu Liu, Luisa Shinzato, Madeleine Hahn de Bykhovetz,
Maiko Takeuchi, Marc Pàmies, Maria A Castillo, Marianna Nezhurina, Mario Sänger, Matthias
Samwald, Michael Cullan, Michael Weinberg, Michiel De Wolf, Mina Mihaljcic, Minna Liu,
Moritz Freidank, Myungsun Kang, Natasha Seelam, Nathan Dahlberg, Nicholas Michio Broad,
Nikolaus Muellner, Pascale Fung, Patrick Haller, Ramya Chandrasekhar, Renata Eisenberg,
Robert Martin, Rodrigo Canalli, Rosaline Su, Ruisi Su, Samuel Cahyawijaya, Samuele Garda,
Shlok S Deshmukh, Shubhanshu Mishra, Sid Kiblawi, Simon Ott, Sinee Sang-aroonsiri, Sr-
ishti Kumar, Stefan Schweter, Sushil Bharati, Tanmay Laud, Théo Gigant, Tomoya Kainuma,
Wojciech Kusa, Yanis Labrak, Yash Shailesh Bajaj, Yash Venkatraman, Yifan Xu, Yingxin Xu,
Yu Xu, Zhe Tan, Zhongli Xie, Zifan Ye, Mathilde Bras, Younes Belkada, and Thomas Wolf.
Bloom: A 176b-parameter open-access multilingual language model, 2023.
[46] Wenxuan
Zhang,
Mahani
Aljunied,
Chang
Gao,
Yew
Ken
Chia,
and
Lidong
Bing.
M3exam:
A multilingual,
multimodal,
multilevel benchmark for examin-
ing large language models.
In Advances in Neural Information Processing Sys-
tems
36:
Annual
Conference
on
Neural
Information
Processing
Systems
2023,
NeurIPS 2023, New Orleans,
LA, USA, December 10 - 16,
2023, 2023.
URL
http://papers.nips.cc/paper_files/paper/2023/hash/117c5c8622b0d539f74f6d1fb082a2e9-Abstract-
[47] Tony Zhao, Eric Wallace, Shi Feng, Dan Klein, and Sameer Singh.
Calibrate before use:
Improving few-shot performance of language models. In International Conference on Machine
Learning, 2021.
[48] Chujie Zheng, Hao Zhou, Fandong Meng, Jie Zhou, and Minlie Huang. Large language models
are not robust multiple choice selectors. In The Twelfth International Conference on Learning
Representations, 2024. URL https://openreview.net/forum?id=shr9PXz7T0.
16

--- Page 17 ---

A
Prompt Variants for MCQs
Please follow the given examples, read the context, and answer the question.
[ in-context examples ]
Context:
Middle distance running is a relatively inexpensive sport; however,
there are many misconceptions regarding the few pieces of equipment required to
participate.
Products can be purchased as needed, but most will have little or no
real impact on performance.
Athletes may feel that they prefer a product even when
it provides no real benefits.
Question:
According to the passage, why might a middle distance runner purchase a
more expensive piece of equipment?
A. It’s their personal preference
B. It has proven benefits
C. It will greatly impact their performance
D. There are misconceptions surrounding less expensive equipment
Answer:
A. It’s their personal preference
Figure 4: The illustration of prompt conﬁguration To. Note that the gray text is NOT used in this
conﬁguration.
Please follow the given examples, read the context, and answer the question.
[ in-context examples ]
Context:
Middle distance running is a relatively inexpensive sport; however,
there are many misconceptions regarding the few pieces of equipment required to
participate.
Products can be purchased as needed, but most will have little or no
real impact on performance.
Athletes may feel that they prefer a product even when
it provides no real benefits.
Question:
According to the passage, why might a middle distance runner purchase a
more expensive piece of equipment?
It’s their personal preference
It has proven benefits
It will greatly impact their performance
There are misconceptions surrounding less expensive equipment
Answer:
It’s their personal preference
Figure 5: The illustration of prompt conﬁguration TiTo.
B
Related Work on Multilingual Benchmarks
Existing English multi-task benchmarks, such as GLUE [42] and SuperGLUE [41], have undoubt-
edly stimulated the growth in research interest and efforts on the transfer learning ability of lan-
guage models across diverse tasks. However, the development of multilingual benchmarks has sig-
niﬁcantly lagged behind that of English-dominant benchmarks. To ﬁll this gap, XTREME [18]
contributed a comprehensive multilingual multi-task benchmark for evaluating cross-lingual trans-
fer learning across 40 languages with 9 datasets. MTG [9] included four human-annotated text
generation datasets in ﬁve languages to support both training and test scenarios.
XGLUE [23] expanded the task scope of the multilingual benchmark to encompass both natural
language understanding and generation tasks. SeaEval [43] provided a benchmark for multilin-
gual foundation models, additionally considering the cultural understanding ability of models, but
the majority of the datasets were still based on high-resource languages, such as English and Chi-
nese. The aforementioned benchmark either neglects tasks in Southeast Asian languages (e.g., MTG
and XGLUE), or only contains a limited subset of tasks or languages from Southeast Asia (e.g.,
XTREME and SeaEval).
Recent multilingual benchmarks like MEGA [1] and BUFFET [5], narrow the datasets that built
from scratch in native languages and the models that speciﬁc designed to Southeast Asia (SEA).
This limits our ability to draw comprehensive and systematic conclusions for SEA large language
17

--- Page 18 ---

Please follow the given examples, read the context, and answer the question.
[ in-context examples ]
Context:
Middle distance running is a relatively inexpensive sport; however,
there are many misconceptions regarding the few pieces of equipment required to
participate.
Products can be purchased as needed, but most will have little or no
real impact on performance.
Athletes may feel that they prefer a product even when
it provides no real benefits.
Question:
According to the passage, why might a middle distance runner purchase a
more expensive piece of equipment?
A. It’s their personal preference
B. It has proven benefits
C. It will greatly impact their performance
D. There are misconceptions surrounding less expensive equipment
Answer:
It’s their personal preference
Figure 6: The illustration of prompt conﬁguration LiTiTo.
Please follow the given examples, read the context, and answer the question.
[ in-context examples ]
Context:
Middle distance running is a relatively inexpensive sport; however,
there are many misconceptions regarding the few pieces of equipment required to
participate.
Products can be purchased as needed, but most will have little or no
real impact on performance.
Athletes may feel that they prefer a product even when
it provides no real benefits.
Question:
According to the passage, why might a middle distance runner purchase a
more expensive piece of equipment?
A. It’s their personal preference
B. It has proven benefits
C. It will greatly impact their performance
D. There are misconceptions surrounding less expensive equipment
Answer:
A
Figure 7: The illustration of prompt conﬁguration LiTiLo.
model research. In comparison, we broaden the evaluation scope by considering more models and
expanding the datasets.
C
Manipulated Training Details
We adopt the “auxiliary train” split of the MMLU dataset [16] as the training corpus 13, which
contains 99.8k examples. After removing the duplicate examples, it resulted in 98.4k examples. We
formulate the training dataset to align with the corresponding format of prompt variants. During
training, we select the latest LLM for Southeast Asian languages for this experiment. The context
window is set to 4096. The warmup step is 40. The cosine learning is scheduled with a maximum
learning rate of 1e-5 and the weight decay is set to 0.1. We ﬁnetune the base model Sailor-7B with
8 A100 GPUs. The total batch size is 512 and we train the model for 2 epochs with a total of 390
steps.
D
Calibration Details
In this section, we list the information of the label prediction before and after calibration, which are
presented in Table 7, 8 and 9. We observe that models tend to predict only one or two labels, indicat-
ing a severe label prediction imbalance. However, after applying Contextual Calibration methods,
this imbalance can be mitigated a lot.
13https://huggingface.co/datasets/cais/mmlu/viewer/auxiliary_train
18

--- Page 19 ---

Please follow the given examples, read the context, and answer the question.
[ in-context examples ]
Context:
Middle distance running is a relatively inexpensive sport; however,
there are many misconceptions regarding the few pieces of equipment required to
participate.
Products can be purchased as needed, but most will have little or no
real impact on performance.
Athletes may feel that they prefer a product even when
it provides no real benefits.
Question:
According to the passage, why might a middle distance runner purchase a
more expensive piece of equipment?
A. It’s their personal preference
B. It has proven benefits
C. It will greatly impact their performance
D. There are misconceptions surrounding less expensive equipment
Answer:
A. It’s their personal preference
Figure 8: The illustration of prompt conﬁguration LiTiLoTo.
Table 6: Model and their corresponding link used in our experiments.
Model
Link
Qwen-1.5-7B
https://huggingface.co/Qwen/Qwen1.5-7B
Llama-2-7B
https://huggingface.co/meta-llama/Llama-2-7b-hf
Llama-3-8B
https://huggingface.co/meta-llama/Meta-Llama-3-8B
Mistral-7B
https://huggingface.co/mistralai/Mistral-7B-v0.1
Gemma-7B
https://huggingface.co/google/gemma-7b
Typhoon-8B
https://huggingface.co/scb10x/llama-3-typhoon-v1.5-8b
VinaLLaMA-7B
https://huggingface.co/vilm/vinallama-7b
BLOOM-7B1
https://huggingface.co/bigscience/bloom-7b1
Sailor-7B
https://huggingface.co/sail/Sailor-7B
SeaLLM-7B
https://huggingface.co/SeaLLMs/SeaLLM-7B-Hybrid
Sea-Lion-7B
https://huggingface.co/aisingapore/sea-lion-7b
Table 7: Thai NLI task results
CONTRADICTION
ENTAILMENT
NEUTRAL
Gold
1670
1670
1670
Seallm-7B
2752
2258
0
Sailor-7B
5007
3
0
Sealion-7B
5010
0
0
Seallm-7B_CC
284
3456
1270
Sailor-7B_CC
3564
140
1306
Sealion-7B_CC
3907
933
170
Table 8: Indonesian NLI task results.
CONTRADICTION
ENTAILMENT
NEUTRAL
Gold
1762
1848
1572
Seallm-7B
5152
0
30
Sailor-7B
5105
77
0
Sealion-7B
5182
0
0
Seallm-7B_CC
4060
726
396
Sailor-7B_CC
4181
396
605
Sealion-7B_CC
4678
458
46
19

--- Page 20 ---

Table 9: Vietnamese NLI task results
CONTRADICTION
ENTAILMENT
NEUTRAL
Gold
1670
1670
1670
Seallm-7B
5010
0
0
Sailor-7B
3711
0
1299
Sealion-7B
9
0
5001
Seallm-7B_CC
2974
2020
16
Sailor-7B_CC
3481
1374
155
Sealion-7B_CC
4696
31
283
20

```
