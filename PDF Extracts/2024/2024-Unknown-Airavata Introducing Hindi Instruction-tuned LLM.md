---
title: "2024-[[Unknown]]-Airavata Introducing Hindi Instruction-tuned LLM - PDF Extract"
source_pdf: "2024-[[Unknown]]-Airavata Introducing Hindi Instruction-tuned LLM.pdf"
pages: 20
extracted_at: "2026-02-13T09:15:44.918138"
---

# PDF Extract: 2024-[[Unknown]]-Airavata Introducing Hindi Instruction-tuned LLM

**Source PDF:** 2024-[[Unknown]]-Airavata Introducing Hindi Instruction-tuned LLM.pdf
**Total Pages:** 20

---

## Content

```
--- Page 1 ---

Technical Report
AIRAVATA: INTRODUCING HINDI INSTRUCTION-TUNED LLM
Jay Gala1
Thanmay Jayakumar1
Jaavid Aktar Husain1,3
Aswanth Kumar4
Mohammed Safi Ur Rahman Khan1
Diptesh Kanojia5
Ratish Puduppully6
Mitesh M. Khapra1,2
Raj Dabre7
Rudra Murthy8
Anoop Kunchukuttan1,2,9
1Nilekani Centre at AI4Bharat
2IIT Madras
3IIIT D&M Kancheepuram
4Flipkart
5University of Surrey
6A*STAR
7NICT
8IBM Research
9Microsoft
https://ai4bharat.github.io/airavata
Figure 1: Image Courtesy: DALL-E 3 (Betker et al., 2023).
1
INTRODUCTION
The recent year has witnessed tremendous interest and activity in the world of Large Language Mod-
els (LLMs). LLMs hold the potential to unlock exciting applications in artificial intelligence due to
their ability to comprehend complex natural language instructions and excel in a broad spectrum
of tasks involving language, knowledge, reasoning, and creative generation. To foster research, in-
novation, and widespread adoption, an open ecosystem is essential. We have observed significant
advancements in this area with the launch of models like Llama 2 (Touvron et al., 2023) and Mistral
(Jiang et al., 2023), as well as their instruction-tuned variants such as Llama 2 Chat (Touvron et al.,
2023), Mistral-Instruct (Jiang et al., 2023), and Zephyr (Tunstall et al., 2023), among others. Major
progress has also been made in developing datasets for pre-training such as RedPajama (Computer,
2023)), instruction tuning (e.g., Alpaca (Taori et al., 2023), UltraChat (Ding et al., 2023), Dolly
(Conover et al., 2023), OpenAssistant (Köpf et al., 2023), LMSYS-Chat (Zheng et al., 2023a)), and
evaluation benchmarks (e.g., AlpacaEval (Dubois et al., 2023), MT-Bench (Zheng et al., 2023b)).
However, most of these advancements have been predominantly centered around the English lan-
guage.
There is limited support for Indian languages, which can be attributed to the incidental inclusion
of some Indian language data that slipped through the data filters during the pre-training of these
language models. However, the representation of data, the efficacy of tokenizers, and task perfor-
mance for Indian languages are considerably behind that of English. The performance in Indian
1
arXiv:2401.15006v2  [cs.CL]  26 Feb 2024

--- Page 2 ---

Technical Report
languages, even on closed-source models such as ChatGPT (OpenAI, 2022), GPT-4 (Achiam et al.,
2023), and others, is inferior compared to English (Ahuja et al., 2023). Therefore, there is an urgent
need to develop a similar ecosystem of tools, models, and datasets for Indian languages to foster
research and innovation. In pursuit of this objective, the recent collaboration with Sarvam AI led to
release of OpenHathi (SarvamAI, 2023), an open-source foundational model for Hindi, developed
by extending Llama 2 (Touvron et al., 2023).
Today, we announce the next step – an initial release of “Airavata”, an instruction-tuned model
for Hindi built upon finetuning OpenHathi (SarvamAI, 2023) with diverse, instruction-tuning Hindi
datasets to make it better suited for assistive tasks.
Along with the model, we also share the instruction tuning datasets1 to enable further research for
IndicLLMs. We rely on human-curated, license-friendly instruction-tuned datasets to build “Aira-
vata”. We do not use data generated from proprietary models like GPT-4 (Achiam et al., 2023), etc.
We think this is a more sustainable way of building instruction-tuned models at scale for most Indic
languages, where relying on distilled data from commercial models would increase costs and restrict
their free usage in downstream applications due to licensing restrictions.
We also compile a collection of evaluation benchmarks2 along with an evaluation framework to
compare various LLMs for their abilities on diverse tasks when instructed in Hindi. Using this
benchmark and human judgments, we compare different LLMs to quantify the current state of their
Hindi capabilities. We conduct a detailed analysis of Airavata’s performance on various Natural
Language Understanding (NLU) and Natural Language Generation (NLG) tasks and find that the
instruction fine-tuning helps align the model to various NLU tasks. There is significant potential for
improvement in NLG tasks, which require the creation of larger, more diverse instruction datasets
as well as innovations in aligning English model representations to Hindi representations to drive
better cross-lingual transfer.
2
INSTRUCTION TUNING DATASET CREATION
High-quality instruction tuning datasets are important for the good performance of LLMs. How-
ever, there are few diverse datasets for Hindi. Following Wei et al. (2023), we rely on translating
high-quality English-supervised instruction-tuning datasets into Hindi. We use IndicTrans2 (Gala
et al., 2023), the state-of-the-art open-source MT model for Indian languages, for translation. Some
previous works (Li et al., 2023; Wei et al., 2023) have used ChatGPT (OpenAI, 2022) to translate in-
structions and/or generate responses into Hindi to better use context during translation (IndicTrans2
and most MT models are sentence-level). However, this is not cost-effective, and the translation
quality of ChatGPT (OpenAI, 2022) is lower than IndicTrans2 (Gala et al., 2023), and its generation
quality in Hindi might not be up to the mark (Ahuja et al., 2023). A future avenue of work would be
improving translation quality when document context is available.
We sample examples from different datasets listed in Table 1 to ensure balanced representations
across all the tasks while fitting into our instruction tuning budget. We translate the instructions,
input, and outputs into Hindi. This results in a total of 404k examples spanning English and Hindi
language. The translated Hindi examples were filtered to retain high-quality examples. Specifically,
examples were retained only when the chrF++ score (Popovi´c, 2017) between the back-translated
example and the corresponding English example was 50 or above. The final dataset used for in-
struction tuning contains 385k examples. Table 1 shows the details of the final training dataset. The
dataset is available on the HuggingFace Hub.3
We also create two native Hindi Instruction datasets:
• wikiHow: wikiHow4 is an online wiki-style platform that serves as a valuable resource for a di-
verse array of how-to articles spanning numerous topics. The articles on the platform are human-
moderated, ensuring a high-quality standard. The questions users pose in these articles closely
1https://huggingface.co/datasets/ai4bharat/indic-instruct-data-v0.1
2https://huggingface.co/collections/ai4bharat/airavata-evaluation-suite
-65b13b7b68165de71ba0b333
3https://huggingface.co/datasets/ai4bharat/indic-instruct-data-v0.1
4https://www.wikihow.com/Main-Page
2

--- Page 3 ---

Technical Report
Dataset
Unfiltered
Filtered
English
Hindi
English
Hindi
FLAN-v2 (Longpre et al., 2023)
67,463
67,463
67,463
65,228
Anthropic-HHH (Bai et al., 2022)
5,000
5,000
5,000
4,911
Dolly (Conover et al., 2023)
15,011
15,011
15,011
14,880
OpenAssistant (Köpf et al., 2023)
19,945
20,128
19,945
16384
LymSys-Chat (Zheng et al., 2023a)
50,000
50,000
50,000
37,422
WikiHow
20,400
6,055
20,400
6,055
Anudesh
5,234
7,577
5,234
7,577
Total
183,053
171,234
183,053
152,457
Table 1: Instruction Fine-tuning Training Dataset Details
align with potential use cases for this model, making it a rich resource for training models. Ad-
ditionally, this might also help induce reasoning capabilities and generate logical step-by-step
responses. We curate around 20k and 6k articles in English and Hindi, respectively, resulting in
a total of around 27k articles. We currently formulate the data as a completion task given either
question or question along with a few initial steps. The dataset is released under the CC-0 license.
• Anudesh: Anudesh is a crowd-sourced collection of prompts accompanied by responses gener-
ated from the Llama 2 70B model (Touvron et al., 2023). Participants are provided with clear
guidelines detailing the nature of the interaction required, including the specific language to be
employed. These languages encompass a range that includes Indic languages, English, transliter-
ated Indic, as well as a blend of Indic and English in a code-mixed format. Contributors craft their
prompts in adherence to these directives and the specified language criteria. Subsequently, these
prompts are then paired with the corresponding translated outputs from the Llama 2 70B model
(Touvron et al., 2023). The dataset is released under CC-BY-4.0 license. More details about the
interactions will be released soon.
We provide a brief description of all the existing instruction datasets used in addition to the above
(and corresponding licenses) below:
• FLAN-v2 (Longpre et al., 2023): A collection of NLP tasks that combines a number of existing
NLP datasets with various data augmentations, introduced by Chung et al. (2022). We sample
around 67K examples for our training mixture. The dataset is released under the Apache-2.0
license.
• Anthropic-HHH (Bai et al., 2022): A collection of human-collected preference data for aligning
the models to be helpful and harmless. We sample 5K conversations from the “chosen" column
for our training mixture. The dataset is released under the MIT license.
• Dolly (Conover et al., 2023): A corpus of more than 15K records generated by thousands of
Databricks employees to enable LLMs to exhibit the magical interactivity of ChatGPT. The dataset
is released under the CC-BY-SA-3.0 license.
• OpenAssistant (Köpf et al., 2023): A collection of human-generated, human-annotated assistant-
style conversation corpus consisting of 38K messages, resulting in over 3K conversation trees and
around 20K conversations. The dataset is released under the Apache-2.0.
• LymSys-Chat (Zheng et al., 2023a): A collection of 1M real-world conversations spanning 25
SOTA LLMs similar to OpenAssistant (Köpf et al., 2023). We sample 50K conversations for
our training mixture. The dataset is released under the LMSYS-Chat-1M Dataset License Agree-
ment.5
• NMT (Gala et al., 2023): A multi-domain human-annotated dataset containing 50K bitext
English-Hindi translation pairs from BPCC-Human (Gala et al., 2023) to enable better cross-
lingual transfer. The dataset is released under the CC-BY-4.0 license.
5https://huggingface.co/datasets/lmsys/lmsys-chat-1m#lmsys-chat-1m-dat
aset-license-agreement
3

--- Page 4 ---

Technical Report
Hyper-Parameter
Value
LoRA Rank
16
LoRA alpha
32
LoRA Dropout
0.05
LoRA Target Modules
q_proj, v_proj, k_proj, gate_proj
up_proj, down_proj
Epochs
4
Learning rate
5e-4
Batch Size
128
Floating Point Precision
bfloat16
Table 2: Hyperparameters for Fine-tuning
3
SUPERVISED FINE-TUNING
We fine-tune the OpenHathi model using the above-compiled datasets. We perform parameter-
efficient fine-tuning with LoRA (Hu et al., 2022). The hyperparameters used are listed in the Table 2.
During fine-tuning, the loss was computed only for the output tokens. We used the OpenInstruct
framework6 for fine-tuning and customizing it for our requirements (our custom version is available
as IndicInstruct7). One fine-tuning example corresponds to one example in the dataset. However,
this is suboptimal since many tokens are wasted as padding tokens. We plan to optimize this process
by packing multiple dataset examples into a single fine-tuning example (Iyer et al., 2022; Krell et al.,
2023).
3.1
FULL VS. LORA FINETUNING
There are two prevalent methods for instruction fine-tuning for LLMs: Full fine-tuning and LoRA.
Full fine-tuning (FFT) involves updating all the model parameters, whereas LoRA (Hu et al., 2022)
fine-tuning involves introducing a small set of additional parameters and only updating them. We
perform an ablation study to examine both the fine-tuning strategies to train two models, one em-
ploying full fine-tuning and the other by LoRA fine-tuning. For the context of this ablation study,
we consider the FLAN v2 (Longpre et al., 2023) subset from our instruction dataset spanning En-
glish and Hindi. For our evaluation, we used a subset of NLU tasks in Hindi, along with BoolQ
(Clark et al., 2019) and MMLU (Hendrycks et al., 2021) tasks in English, as development sets to
decide between full fine-tuning and LoRA fine-tuning (Figure 2). We observed that FFT models
outperform the OpenHathi base model (SarvamAI, 2023) in IndicCopa (Doddapaneni et al., 2022)
and IndicXParaphrase (Doddapaneni et al., 2022) tasks. However, the FFT model performed poorly
on English tasks compared to the base model as well as the LoRA fine-tuned model. LoRA fine-
tuned model demonstrated improvements or similar performance as the OpenHathi base model on
both Hindi NLU and English tasks. As a result, we decided to proceed with LoRA fine-tuning for
training our final model. We report results on the LoRA fine-tuned final model in the subsequent
section.
3.2
MODEL SELECTION
We fine-tune the OpenHathi model for 4 epochs and save the model after each epoch. We evaluate
the checkpoint of each epoch on the dev set (IndicSentiment, IndicCOPA, IndicXNLI, and IndicQA
from IndicXTREME (Doddapaneni et al., 2022), and Flores devtest (Goyal et al., 2021; Costa-jussà
et al., 2022)) and compare the average performance. We observe that the checkpoint of epoch 3
performs well on NLU tasks, while the checkpoint of epoch 4 performs well on NLG tasks. We
perform checkpoint averaging, where we interpolate the weights of the above two checkpoints to
obtain a model that performs well across both NLU and NLG tasks. We found the best interpolation
factor to be around 0.6.
6https://github.com/allenai/open-instruct
7https://github.com/AI4Bharat/IndicInstruct
4

--- Page 5 ---

Technical Report
Figure 2: Ablation experiment to understand the performance gaps between Full fine-tuning and
LoRA fine-tuning across a mix of English and Hindi NLU tasks.
interpolated weights = 0.6 × checkpoint3 + (1 −0.6) × checkpoint4
4
EVALUATION ON NLP BENCHMARKS
We evaluate our model on the standard NLU and NLG benchmarks, which include native Hindi test
sets from IndicXTREME (Doddapaneni et al., 2022) and Indic NLG Suite (Kumar et al., 2022).
Further, to test the knowledge and reasoning capabilities of the model in Hindi, we translate the
English benchmarks such as MMLU (Hendrycks et al., 2021), Hellaswag (Zellers et al., 2019),
ARC (Clark et al., 2018), Winogrande (Sakaguchi et al., 2020) and BoolQ (Clark et al., 2019) and
use these to evaluate our final model. The IndicTrans2 (Gala et al., 2023) model was employed for
translating the benchmarks. Although this is not the perfect evaluation setup however, due to limited
resources, we rely on this method as a proxy indicator for assessing trends in the performance of
the model in terms of reasoning capabilities in Hindi. An important future direction would involve
creating equivalent benchmarks in the native language instead of solely relying on translations.
4.1
RESULTS
Tables 3 to 6 shows the comparison of Airavata with the base model (OpenHathi) and the translate-
test baseline using the Llama 2 7B Chat model. In the translate-test approach, the Hindi input is
translated into English using the IndicTrans2 model and is used as a prompt to the Llama 2 7B
Chat model. We observe that Airavata significantly outperforms the OpenHathi model on most
tasks, demonstrating that fine-tuning on the IndicInstruct dataset helps align the base model to a
variety of tasks. Moreover, the performance of the translate-test approach with the Llama 2 7B Chat
model has a lot of variance, while Airavata consistently performs well across tasks. OpenHathi
and Airavata exhibit comparable performance in the translation task. OpenHathi benefits from its
extensive training on parallel corpora, resulting in a highly proficient base model for the translation
task. We observe mixed results on generation tasks, indicating the scope for further improvement
of Airvata, especially in open-ended text generation capabilities. Table 4 shows the performance of
Airavata and other models on English test sets and the respective machine-translated Hindi test set.
We observe a 5-15 point performance gap between the English baseline and the respective Hindi
5

--- Page 6 ---

Technical Report
baseline across various tasks for both OpenHathi and Airavata models. This indicates limited cross-
lingual transfer of English knowledge to Hindi, highlighting the need for future research to improve
cross-lingual alignment to maximize knowledge transfer between English and Hindi.
0-Shot
5-Shot
OpenHathi Llama2 7B Chat Airavata OpenHathi Llama2 7B Chat Airavata
(translate-test)
(translate-test)
IndicSentiment
72.89
97.85
95.81
96.59
98.43
97.01
IndicCopa
68.69
76.53
63.75
42.77
78.34
72.97
IndicXNLI
16.67
23.67
73.26
42.25
47.96
74.70
IndicXParaphrase
71.72
09.54
76.53
66.67
48.56
69.87
Table 3: F1 scores on Indic NLU and Commonsense Reasoning tasks
Variant
0-Shot
5-Shot
OpenHathi Airavata OpenHathi Airavata
MMLU
English
36.16
41.39
40.12
43.28
Hindi (Translated)
32.27
34.96
35.13
36.00
BoolQ
English
52.63
73.00
64.46
62.02
Hindi (Translated)
58.56
64.50
65.69
51.47
ARC Easy
English
57.28
70.50
62.12
71.04
Hindi (Translated)
44.28
54.00
49.87
54.84
Arc Challenge English
39.85
45.90
46.25
48.29
Hindi (Translated)
32.68
35.92
36.60
36.26
Hella Swag
English
31.48
34.37
32.45
36.83
Hindi (Translated)
25.59
25.37
24.85
24.84
Winogrande
English
49.17
49.72
-
-
Table 4: Accuracy on English NLU and Commonsense Reasoning tasks and its translated variants
Metric
0-Shot
5-shot
OpenHathi Airavata OpenHathi Airavata
Flores
chrF++
55.41
54.82
54.98
54.24
BLEURT
0.7103
0.6970
0.7115
0.7084
IN22-Gen
chrF++
54.23
53.78
54.53
52.81
BLEURT
0.7156
0.7012
0.7181
0.7037
Table 5: chrF++ and BLEURT scores on English-Hindi translation task
5
HUMAN EVALUATION
We assess Airavata using authentic prompts provided by real users, evaluating its performance across
five distinct abilities outlined in Table 7.
We define a set of intents and domains of focus, which are then provided to users, along with clear
instructions on the type of prompts they should construct. More details about the benchmark will be
released soon.
Along with Airavata, we also evaluate ChatGPT (OpenAI, 2022), GPT-4 (Achiam et al., 2023) and
BactrianX-llama-7B (Li et al., 2023) models for the same abilities. BactrianX-llama-7B is an in-
structed fine-tuned model for Hindi directly fine-tuned with the Llama base model on a multilingual
instruction dataset. This multilingual instruction dataset consisted of machine-translated instructions
6

--- Page 7 ---

Technical Report
Metric
1-shot
OpenHathi Llama 2 7B Chat Airavata
(translate-test)
Indic QA (No Context)
F1
17
4.58
21.01
Indic QA (With Context)
F1
20.69
19.59
37.69
Indic Headline
Rouge L
11.26
23.06
12.32
BLEURT
0.4682
0.4590
0.3793
IndicWikiBio
Rouge L
20.45
41.01
10.66
BLEURT
0.5185
0.6415
0.4279
Table 6: F1, Rouge L and BLEURT scores on Indic NLG tasks
AbilityName
Ability
Long
Ability to generate long-form text like writing essays, speeches, reports, etc.
Fact-Ops
Ability to give factual opinions and explanations like seeking recommendations,
seeking advice, opinions, explanations, etc.
Content
Ability to make content accessible like summarizations, layman
explanations, etc
Lang-Creativity Ability to be creative in language like finding anagrams, rhyming words,
vocabulary enhancement, etc
Culture
Ability to answer questions related to Indian Culture.
Table 7: Description of abilities to test through human evaluation
from Alpaca (Taori et al., 2023) and Dolly (Conover et al., 2023) datasets, followed by response gen-
eration from ChatGPT (OpenAI, 2022). Annotators were presented with a prompt and a randomly
selected response from any of the models and were instructed to provide ratings based on the metrics
outlined in Table 8.
In addition to the above metrics, we also ask the human evaluators to give a final score on the likert
scale of 1 to 5, reflecting their overall satisfaction with the response.
We sample a set of 50 prompts8 covering various intents and domains (more details about the bench-
mark will be made available soon) and generate the responses from all three models. The prompt-
response pairs were shuffled randomly and anonymized, ensuring no indication of the generating
model, before being presented to the annotators for evaluation. Annotators were instructed to assess
responses strictly adhering to the aforementioned rubrics. We report the various results in Figures 3
to 5.
8https://huggingface.co/datasets/ai4bharat/human-eval
Metric
Details
Range
IFA: Instruction Fol-
lowing Ability
This assesses the model’s ability to accurately and effectively fol-
low the instructions provided in the prompt
0-2
CNS: Closeness to
Native Speaker
This assesses how naturally and fluently the model’s responses
align with the way a native Hindi speaker would express the same
ideas.
0-2
CQ: Content Qual-
ity
This evaluates the response in terms of its factual accuracy, logical
flow of ideas, and overall informational relevance.
0-2
Table 8: Rubrics for Human Evaluation
7

--- Page 8 ---

Technical Report
Figure 3: Average satisfaction scores for various models based on a Likert scale between 1 and 5
reported by Human annotators.
Figure 4: Human evaluation scores for assessing the instruction following and content generation
abilities of the models based on the rubrics described in Table 8.
Our observations suggest that while Airavata still trails significantly behind GPT-4 in terms of its
ability to follow instructions and the quality of its content, it performs relatively better when gen-
erating natural-sounding Hindi content compared to both GPT-4 and ChatGPT. Notably, Airavata
outperforms the BactrianX-llama-7B model by a significant margin. This difference in performance
can be attributed to a lack of vocabulary expansion in BactrainX-llama-7B to accommodate addi-
8

--- Page 9 ---

Technical Report
Figure 5: Fine-grained human evaluation of content generation abilities of the models described in
Table 7.
tional Hindi tokens and its lack of continual pre-training in Hindi. Furthermore, BactrainX-llama-7B
may be trained on a lower-quality dataset for instruction tuning that was completely generated using
ChatGPT. The OpenHathi model and Airavata, however, have addressed these shortcomings and
show substantial improvements over the BactrainX-llama-7B model. We discuss these performance
trends across various capabilities in more detail below.
The findings indicate that amongst all abilities, Airavata particularly excels in providing factual
opinions and explanations, as demonstrated by the earlier examples. However, the model struggles
with tasks demanding creative language usage, as our SFT data lacks components emphasizing cre-
ativity. When comparing GPT-4 and ChatGPT (GPT-3.5) performance, GPT-4 generally surpasses
the latter in knowledge-intensive or creativity-demanding tasks. Nevertheless, it’s noteworthy that
ChatGPT either outperforms or is comparable in tasks emphasizing language generation, such as
long-form content creation, offering factual opinions, and ensuring content accessibility.
We acknowledge that our current human evaluation is not robust and thorough due to the limited
number of prompts in our set and each prompt and response pair being evaluated by only one anno-
tator. However, our evaluation still offers valuable preliminary insights that will inform our efforts
to improve the model. Expanding the instruction dataset to include content covering a diverse range
of abilities can help improve the model’s capabilities. At the same time, it is important to ac-
knowledge that a significant portion of knowledge stems from English, which possesses the most
extensive knowledge repository. Therefore, achieving better cross-lingual alignment between Hindi
and English representations is essential for accurately answering factual questions and minimizing
erroneous responses.
6
TOXICITY AND MISINFORMATION
We evaluate Airavata, OpenHathi, and Llama2-7B models with publicly available benchmark
datasets, in both 0-shot and 5-shot settings. Our evaluation provides insights into key dimensions
for LM safety. Multilingual HateCheck (MHC) is a suite of functional tests for hate speech detec-
tion and we use its Hindi subset (Das et al., 2022) to evaluate and compare the performance of all
models. We translate the TruthfulQA, Implicit Hate, and a human-evaluated subset of the Toxigen
dataset, to Hindi. This subset of Toxigen has been denoised to retain instances that have annotation
9

--- Page 10 ---

Technical Report
0-Shot
5-Shot
Variant
OpenHathi
Llama2 7B Chat
(translate-test)
Airavata
OpenHathi
Llama2 7B Chat
(translate-test)
Airavata
Multilingual HateCheck
Hindi
70.15
70.24
70.24
70.15
70.24
70.25
Implicit Hate
English
50.65
57.92
62.33
51.41
65.02
62.44
Hindi (Translated)
52.45
53.21
61.15
49.99
52.98
58.84
Toxigen
English
44.91
83.35
78.63
42.71
66.34
72.24
(human evaluated)
Hindi (Translated)
47.75
83.97
78.56
42.83
73.20
74.80
TruthfulQA
English
30.72
37.25
33.60
30.72
37.25
33.64
(averaged MC1 & MC2)
Hindi (Translated)
34.31
35.66
35.32
34.31
35.66
35.32
Table 9: Accuracy on hate and toxicity identification, and answering factual questions.
agreement from all annotators (Hosseini et al., 2023). While the Implicit Hate dataset (Hosseini
et al., 2023) helps evaluate the model performance on detecting the subtle and implicit forms of
hate speech, human-evaluated Toxigen data contains instances that are directed towards various de-
mographics. We evaluate the model performance on detection of toxicity in these three datasets,
and their translated instances using the accuracy metric. Further, for evaluating the model’s capa-
bility towards answering factual questions, we use the TruthfulQA dataset (Lin et al., 2022) which
contains multiple choice questions which are factual and can mimic common human falsehoods.
Given the accuracy scores from our evaluation, in Table 9, Airavata is able to detect openly ex-
pressed hate in Hindi statements from MHC with an accuracy similar to the other two models, with
similar performance in both 0- and 5-shot settings. On the more challenging instances which contain
implicitly veiled hate speech, Airavata is able to identify hate with significantly better accuracy than
the other two models within the translated Hindi instances. On the original Implicit Hate dataset,
Llama2-7B seems to perform better, given a few examples. On the Translated Toxigen subset,
Llama2-7B is able to detect targeted toxic instances against certain demographics with the highest
accuracy among all three models. However, given a few examples, we observe a significant perfor-
mance dip for Llama2-7B and Airavata outperforms it marginally. We observe similar performance
on the original English dataset and note that Airavata is better at detecting targeted hate in Hindi, as
compared to implicitly veiled hate speech. Its performance at detecting targeted hate is surprisingly
better than detecting openly expressed hate speech from MHC. On the TruthfulQA dataset, in both
0- and 5-shot settings, Llama2-7B outperforms OpenHathi and Airavata. On the translated Truth-
fulQA data, a marginal dip in the performance can be observed which indicates that we need further
investigation into the model’s capability for generating misinformation.
Overall, these results may suggest that LLMs are able to identify toxicity and hateful speech, we
think that further investigation is needed to evaluate toxicity and the presence of social biases within
the content generated by LLMs. In the future, we plan to investigate additional existing benchmarks
and novel evaluation measures to test LLMs for content safety and reliability.
7
RESOURCES
You can find all the details about the project in this section. We release the following resources to
facilitate further research in instruction-tuning for Indian language LLMs.
• Airavata Github Repository (for fine-tuning and evaluation)
• Airavata SFT Dataset Collection: Huggingface
• Airavata Evaluation Dataset Collection: Huggingface
8
SUMMARY AND FUTURE OUTLOOK
We release Airavata, an open-source, instruction-tuned Hindi model demonstrating promising per-
formance across various tasks compared to existing open-source models. We provide both datasets
and models to facilitate further research in improving Hindi LLMs. This marks an initial stride to-
wards developing high-quality, open-source LLMs for Indian languages that require multi-faceted
10

--- Page 11 ---

Technical Report
efforts ranging from the creation of extensive pre-training datasets, diverse instruction tuning
datasets, and high-quality foundational models.
9
LIMITATIONS
Airavata, like other LLMs, faces common challenges such as potential hallucinations, resulting in
the generation of fabricated information, and may struggle with accuracy in complex or specialized
topics. There is also a risk of generating objectionable or biased content. Its understanding of
cultural nuances and effectiveness in mixed-language contexts may be constrained. Furthermore,
the model’s performance is closely tied to the quality and scope of its training data, influencing its
efficacy and reliability. It is crucial to note that this model is designed for research purposes and is
not recommended for any production use-cases.
11

--- Page 12 ---

Technical Report
REFERENCES
Josh Achiam, Steven Adler, Sandhini Agarwal, et al. Gpt-4 technical report. 2023. URL https:
//api.semanticscholar.org/CorpusID:257532815.
Kabir Ahuja, Harshita Diddee, Rishav Hada, Millicent Ochieng, Krithika Ramesh, Prachi Jain, Ak-
shay Nambi, Tanuja Ganu, Sameer Segal, Mohamed Ahmed, Kalika Bali, and Sunayana Sitaram.
MEGA: Multilingual evaluation of generative AI. In Houda Bouamor, Juan Pino, and Kalika Bali
(eds.), Proceedings of the 2023 Conference on Empirical Methods in Natural Language Process-
ing, pp. 4232–4267, Singapore, December 2023. Association for Computational Linguistics. doi:
10.18653/v1/2023.emnlp-main.258. URL https://aclanthology.org/2023.emnl
p-main.258.
Yuntao Bai, Andy Jones, Kamal Ndousse, et al. Training a helpful and harmless assistant with
reinforcement learning from human feedback. arXiv preprint arXiv: 2204.05862, 2022.
James Betker, Gabriel Goh, Li Jing, Tim Brooks, Jianfeng Wang, Linjie Li, Long Ouyang, Juntang
Zhuang, Joyce Lee, Yufei Guo, Wesam Manassra, Prafulla Dhariwal, Casey Chu, Yunxin Jiao,
and Aditya Ramesh.
Improving image generation with better captions, October 2023.
URL
https://cdn.openai.com/papers/dall-e-3.pdf.
Hyung Won Chung, Le Hou, Shayne Longpre, et al. Scaling instruction-finetuned language models.
arXiv preprint arXiv: 2210.11416, 2022.
Christopher Clark, Kenton Lee, Ming-Wei Chang, Tom Kwiatkowski, Michael Collins, and Kristina
Toutanova.
BoolQ: Exploring the surprising difficulty of natural yes/no questions.
In Jill
Burstein, Christy Doran, and Thamar Solorio (eds.), Proceedings of the 2019 Conference of
the North American Chapter of the Association for Computational Linguistics: Human Lan-
guage Technologies, Volume 1 (Long and Short Papers), pp. 2924–2936, Minneapolis, Minnesota,
June 2019. Association for Computational Linguistics. doi: 10.18653/v1/N19-1300. URL
https://aclanthology.org/N19-1300.
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick, and
Oyvind Tafjord. Think you have solved question answering? try arc, the ai2 reasoning challenge.
arXiv preprint arXiv: 1803.05457, 2018.
Together Computer. Redpajama: an open dataset for training large language models, October 2023.
URL https://github.com/togethercomputer/RedPajama-Data.
Mike Conover, Matt Hayes, Ankit Mathur, Jianwei Xie, Jun Wan, Sam Shah, Ali Ghodsi, Patrick
Wendell, Matei Zaharia, and Reynold Xin. Free dolly: Introducing the world’s first truly open
instruction-tuned llm, 2023. URL https://www.databricks.com/blog/2023/04/
12/dolly-first-open-commercially-viable-instruction-tuned-llm.
Marta R. Costa-jussà, James Cross, Onur Çelebi, Maha Elbayad, Kenneth Heafield, Kevin Heffer-
nan, Elahe Kalbassi, Janice Lam, Daniel Licht, Jean Maillard, Anna Sun, Skyler Wang, Guillaume
Wenzek, Al Youngblood, Bapi Akula, Loic Barrault, Gabriel Mejia Gonzalez, Prangthip Hansanti,
John Hoffman, Semarley Jarrett, Kaushik Ram Sadagopan, Dirk Rowe, Shannon Spruit, Chau
Tran, Pierre Andrews, Necip Fazil Ayan, Shruti Bhosale, Sergey Edunov, Angela Fan, Cynthia
Gao, Vedanuj Goswami, Francisco Guzmán, Philipp Koehn, Alexandre Mourachko, Christophe
Ropers, Safiyyah Saleem, Holger Schwenk, and Jeff Wang. No language left behind: Scaling
human-centered machine translation. arXiv preprint arXiv: 2207.04672, 2022.
Mithun Das, Punyajoy Saha, Binny Mathew, and Animesh Mukherjee. HateCheckHIn: Evaluating
Hindi hate speech detection models. In Nicoletta Calzolari, Frédéric Béchet, Philippe Blache,
Khalid Choukri, Christopher Cieri, Thierry Declerck, Sara Goggi, Hitoshi Isahara, Bente Mae-
gaard, Joseph Mariani, Hélène Mazo, Jan Odijk, and Stelios Piperidis (eds.), Proceedings of the
Thirteenth Language Resources and Evaluation Conference, pp. 5378–5387, Marseille, France,
June 2022. European Language Resources Association. URL https://aclanthology.o
rg/2022.lrec-1.575.
12

--- Page 13 ---

Technical Report
Ning Ding, Yulin Chen, Bokai Xu, Yujia Qin, Zhi Zheng, Shengding Hu, Zhiyuan Liu, Maosong
Sun, and Bowen Zhou. Enhancing chat language models by scaling high-quality instructional
conversations. arXiv preprint arXiv:2305.14233, 2023.
Sumanth Doddapaneni, Rahul Aralikatte, Gowtham Ramesh, Shreyansh Goyal, Mitesh M. Khapra,
Anoop Kunchukuttan, and Pratyush Kumar. Towards leaving no indic language behind: Build-
ing monolingual corpora, benchmark and models for indic languages. Annual Meeting of the
Association for Computational Linguistics, 2022. doi: 10.18653/v1/2023.acl-long.693.
Yann Dubois, Xuechen Li, Rohan Taori, Tianyi Zhang, Ishaan Gulrajani, Jimmy Ba, Carlos
Guestrin, Percy Liang, and Tatsunori B. Hashimoto. Alpacafarm: A simulation framework for
methods that learn from human feedback, 2023.
Jay Gala, Pranjal A Chitale, A K Raghavan, Varun Gumma, Sumanth Doddapaneni, Aswanth Kumar
M, Janki Atul Nawale, Anupama Sujatha, Ratish Puduppully, Vivek Raghavan, Pratyush Kumar,
Mitesh M Khapra, Raj Dabre, and Anoop Kunchukuttan. Indictrans2: Towards high-quality and
accessible machine translation models for all 22 scheduled indian languages. Transactions on
Machine Learning Research, 2023. ISSN 2835-8856. URL https://openreview.net/f
orum?id=vfT4YuzAYA.
Naman Goyal, Cynthia Gao, Vishrav Chaudhary, Peng-Jen Chen, Guillaume Wenzek, Da Ju, San-
jana Krishnan, Marc’Aurelio Ranzato, Francisco Guzmán, and Angela Fan. The flores-101 eval-
uation benchmark for low-resource and multilingual machine translation. 2021.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob
Steinhardt. Measuring massive multitask language understanding. In International Conference
on Learning Representations, 2021. URL https://openreview.net/forum?id=d7KB
jmI3GmQ.
Saghar Hosseini, Hamid Palangi, and Ahmed Hassan Awadallah.
An empirical study of
metrics to measure representational harms in pre-trained language models.
arXiv preprint
arXiv:2301.09211, 2023.
Edward J Hu, yelong shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang,
and Weizhu Chen. LoRA: Low-rank adaptation of large language models. In International Con-
ference on Learning Representations, 2022. URL https://openreview.net/forum?i
d=nZeVKeeFYf9.
Srinivasan Iyer, Xi Victoria Lin, Ramakanth Pasunuru, Todor Mihaylov, Daniel Simig, Ping Yu, Kurt
Shuster, Tianlu Wang, Qing Liu, Punit Singh Koura, Xian Li, Brian O’Horo, Gabriel Pereyra,
Jeff Wang, Christopher Dewan, Asli Celikyilmaz, Luke Zettlemoyer, and Ves Stoyanov. Opt-
iml: Scaling language model instruction meta learning through the lens of generalization. arXiv
preprint arXiv: 2212.12017, 2022.
Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, et al. Mistral 7b. arXiv preprint arXiv:
2310.06825, 2023.
Mario Michael Krell, Matej Kosec, Sergio P. Perez, and Andrew William Fitzgibbon. Efficient
sequence packing without cross-contamination: Accelerating large language models without im-
pacting performance, 2023. URL https://openreview.net/forum?id=ZAzSf9pz
Cm.
Aman Kumar, Himani Shrotriya, Prachi Sahu, Amogh Mishra, Raj Dabre, Ratish Puduppully,
Anoop Kunchukuttan, Mitesh M. Khapra, and Pratyush Kumar. IndicNLG benchmark: Multi-
lingual datasets for diverse NLG tasks in Indic languages. In Yoav Goldberg, Zornitsa Kozareva,
and Yue Zhang (eds.), Proceedings of the 2022 Conference on Empirical Methods in Natural
Language Processing, pp. 5363–5394, Abu Dhabi, United Arab Emirates, December 2022. As-
sociation for Computational Linguistics.
doi: 10.18653/v1/2022.emnlp-main.360.
URL
https://aclanthology.org/2022.emnlp-main.360.
Andreas Köpf, Yannic Kilcher, Dimitri von Rütte, Sotiris Anagnostidis, Zhi-Rui Tam, Keith Stevens,
Abdullah Barhoum, Nguyen Minh Duc, Oliver Stanley, Richárd Nagyfi, Shahul ES, Sameer Suri,
13

--- Page 14 ---

Technical Report
David Glushkov, Arnav Dantuluri, Andrew Maguire, Christoph Schuhmann, Huu Nguyen, and
Alexander Mattick. Openassistant conversations - democratizing large language model alignment.
arXiv preprint arXiv: 2304.07327, 2023.
Haonan Li, Fajri Koto, Minghao Wu, Alham Fikri Aji, and Timothy Baldwin. Bactrian-x: Multi-
lingual replicable instruction-following models with low-rank adaptation. arXiv preprint arXiv:
2305.15011, 2023.
Stephanie Lin, Jacob Hilton, and Owain Evans. TruthfulQA: Measuring how models mimic human
falsehoods. In Smaranda Muresan, Preslav Nakov, and Aline Villavicencio (eds.), Proceedings
of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long
Papers), pp. 3214–3252, Dublin, Ireland, May 2022. Association for Computational Linguistics.
doi: 10.18653/v1/2022.acl-long.229. URL https://aclanthology.org/2022.acl-l
ong.229.
S. Longpre, Le Hou, Tu Vu, Albert Webson, Hyung Won Chung, Yi Tay, Denny Zhou, Quoc V. Le,
Barret Zoph, Jason Wei, and Adam Roberts. The flan collection: Designing data and methods for
effective instruction tuning. International Conference on Machine Learning, 2023. doi: 10.485
50/arXiv.2301.13688.
OpenAI. Gpt3.5, November 2022. URL https://platform.openai.com/docs/model
s/gpt-3-5.
Maja Popovi´c. chrF++: words helping character n-grams. In Proceedings of the Second Conference
on Machine Translation, pp. 612–618, Copenhagen, Denmark, September 2017. Association for
Computational Linguistics. doi: 10.18653/v1/W17-4770. URL https://aclanthology.o
rg/W17-4770.
Keisuke Sakaguchi, Ronan Le Bras, Chandra Bhagavatula, and Yejin Choi. Winogrande: An ad-
versarial winograd schema challenge at scale. In The Thirty-Fourth AAAI Conference on Artifi-
cial Intelligence, AAAI 2020, The Thirty-Second Innovative Applications of Artificial Intelligence
Conference, IAAI 2020, The Tenth AAAI Symposium on Educational Advances in Artificial Intelli-
gence, EAAI 2020, New York, NY, USA, February 7-12, 2020, pp. 8732–8740. AAAI Press, 2020.
doi: 10.1609/AAAI.V34I05.6399. URL https://doi.org/10.1609/aaai.v34i05.
6399.
SarvamAI. Openhathi series: An approach to build bilingual llms frugally, December 2023. URL
https://www.sarvam.ai/blog/announcing-openhathi-series.
Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann Dubois, Xuechen Li, Carlos Guestrin, Percy
Liang, and Tatsunori B. Hashimoto. Stanford alpaca: An instruction-following llama model.
https://github.com/tatsu-lab/stanford_alpaca, 2023.
Hugo Touvron, Louis Martin, Kevin Stone, et al. Llama 2: Open foundation and fine-tuned chat
models. arXiv preprint arXiv: 2307.09288, 2023.
Lewis Tunstall, Edward Beeching, Nathan Lambert, Nazneen Rajani, Kashif Rasul, Younes Belkada,
Shengyi Huang, Leandro von Werra, Clémentine Fourrier, Nathan Habib, Nathan Sarrazin, Omar
Sanseviero, Alexander M. Rush, and Thomas Wolf. Zephyr: Direct distillation of lm alignment.
arXiv preprint arXiv: 2310.16944, 2023.
Xiangpeng Wei, Haoran Wei, Huan Lin, Tianhao Li, Pei Zhang, Xingzhang Ren, Mei Li, Yu Wan,
Zhiwei Cao, Binbin Xie, Tianxiang Hu, Shangjie Li, Binyuan Hui, Bowen Yu, Dayiheng Liu,
Baosong Yang, Fei Huang, and Jun Xie. Polylm: An open source polyglot large language model.
arXiv preprint arXiv: 2307.06018, 2023.
Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi, and Yejin Choi.
HellaSwag: Can a
machine really finish your sentence? In Anna Korhonen, David Traum, and Lluís Màrquez (eds.),
Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics, pp.
4791–4800, Florence, Italy, jul 2019. Association for Computational Linguistics. doi: 10.18653
/v1/P19-1472. URL https://aclanthology.org/P19-1472.
14

--- Page 15 ---

Technical Report
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Tianle Li, Siyuan Zhuang, Zhanghao Wu, Yonghao
Zhuang, Zhuohan Li, Zi Lin, Eric. P Xing, Joseph E. Gonzalez, Ion Stoica, and Hao Zhang.
Lmsys-chat-1m: A large-scale real-world llm conversation dataset, 2023a.
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang,
Zi Lin, Zhuohan Li, Dacheng Li, Eric P. Xing, Hao Zhang, Joseph E. Gonzalez, and Ion Stoica.
Judging llm-as-a-judge with mt-bench and chatbot arena. arXiv preprint arXiv: 2306.05685,
2023b.
15

--- Page 16 ---

Technical Report
A
EXAMPLES
In this section, we show example generations from Airavata. Note that the model’s outputs in
examples #A5 and #A6 did not contain newlines between bullet points. They have been added
here for readability.
A.1
EXAMPLES WHERE THE AIRAVATA MODEL GENERATES GOOD OUTPUT
Airavata excels in specific content generation tasks, such as soliciting mail drafts (#A1) and address-
ing general how-to inquiries (#A5, #A6). Furthermore, it demonstrates proficiency in adhering to
instructions related to output structure (#A3 and #A5).
Example #A1
Prompt
ɣजसग्राहककोअपनेऑडर्रमेंदेरीकाअनुभवहुआहो, उसकेɡलएएकमाफʏ ईमेलड्राफ्टकरेंऔरआȯस्तकरेंɟक
समस्याकासमाधानहोगयाहै।
Model Response
ɟप्रय[ग्राहककानाम], ।
मुझेआशाहैɟकयहईमेलआपकोअǵʍ तरहसेɠमलजाएगा।मैंआपकोयहसूɡचतकरनेकेɡलएɡलखरहाहूंɟक
हमारेɟपछलेऑडर्रमेंदेरीकेकारण, [ऑडर्रसंख्या] केɡलएआपकʏ ɟडलीवरीमेंथोड़ीदेरीहुईहै।मैंसमझताहूंɟकयह
असुɟवधाजनकहोसकताहैऔरमैंमाफʏ मांगताहूं।।
मैंयहसुɟनɢȮतकरनेकेɡलएहरसंभवप्रयासकररहाहूंɟकइसमुद्देकोजल्दसेजल्दहलɟकयाजाएऔरभɟवष्यमेंऐसी
ɟकसीभीघटनासेबचनेकेɡलएहमजोभीकदमउठासकतेहैं, वहउठारहेहैं।।
इसबीच, मैंआपकोसूɡचतकरनाचाहताहूंɟक[ऑडर्रसंख्या] केɡलएआपकʏ ɟडलीवरीअब[ɟतɡथ] परउपलȤ है।कृपया
मुझेबताएंɟकक्याआपकेपासकोईप्रȱ याɭचʌताएँहैं।।
आपकेधैयर्औरसमझकेɡलएधन्यवाद।मैंभɟवष्यमेंआपकेसाथकामकरनेकेɡलएतत्परहूं।।ईमानदारीसे, [आपका
नाम]
Example #A2
Prompt
भारतमेंबड़ोंकेपैरछूनाऔरउनसेबहसनकरनानैɟतकआचरणमानाजाताथा।इसकेपीछेक्यातकर्हैमुझेसमझाओ
Model Response
"हम्म, यहएकɞदलचȺ सवालहै! भारतमेंबड़ोंकोसम्माɟनतȭɜक्तमानाजाताहैऔरआमतौरपरबुजुगǏ कʏ ओररुख
ɟकयाजाताहैजबकोईकɞठनɟनणर्यलेनाहोताहैयाजानकारीलेनीहोतीहै।ऐसाइसɡलएहैक्योंɟकबड़ोंकाज्ञानऔर
अनुभवपीɞढ़योंसेपाɝरतɟकएगएहैंऔरइन्हेंबहुमूल्यसंपɢȉ मानाजाताहै।इसɡलए, बड़ोंकेसाथबातचीतकरतेसमय
सम्मानपूवर्कȭवहारकरनाऔरउनकेपैरोंकोछूनेजैसेɟवनम्रइशारोंकाउपयोगकरनामहत्वपूणर्मानाजाताहै।।
यहयादरखनाभीमहत्वपूणर्हैɟकबड़ोंकोअक्सरलोगोंकेɡलएमागर्दशर्कऔरसलाहकारकेरूपमेंदेखाजाताहै, और
उन्हेंआहतकरनेयाअपमाɟनतकरनेकेबजायउनकʏ सलाहलेनेकʏ कोɡशशकरनीचाɟहए।यɞदɟकसीबुजुगर्नेआपको
कुछअनुɡचतकहायाउसकेȭवहारमेंकोईगलतीकʏ, तोउɡचतप्रɟतɟक्रयादेनाऔरɜȸɟतकोठʎकसेसंभालनामहत्वपूणर्
है।"
16

--- Page 17 ---

Technical Report
Example #A3
Prompt
मैंअपनेसमयप्रबंधनकौशलकोकैसेसुधारसकताहूँ? मुझेपांचɫबʌदुबताएं।
Model Response
1. अपनेलÛयोंकोɡलखें।
2. अपनेलÛयोंकोछोटे, प्रबंधनीयकायǏ मेंɟवभाɣजतकरें।
3. एकअनुसूचीबनाएँऔरउसपरɞटकेरहें।
4. अपनेकायǏ कोप्राथɠमकतादें।
5. अपनेकायǏ कोपूराकरनेकेɡलएखुदकोपुरस्कृतकरें।
Example #A4
Prompt
मैंअपनेसमयप्रबंधनकौशलकोकैसेसुधारसकताहूँ? मुझेपांचɫबʌदुबताएंऔरउनकावणर्नकरें।
Model Response
1. अपनेकायǏ कोप्राथɠमकतादेंःउनकायǏ कोप्राथɠमकतादेंɣजन्हेंपूराकरनेकʏ सबसेअɠधकआवश्यकताहैऔरउन्हें
पहलेपूराकरें।
2. एकअनुसूचीबनाएँःएकअनुसूचीबनाएँऔरउसपरɞटकेरहें।यहआपकोअपनेसमयकाबेहतरप्रबंधनकरनेऔर
अपनेलÛयोंकोप्राप्तकरनेमेंमददकरेगा।
3. ध्यानभटकानेसेबचेंःअपनेफोनकोबंदकरदेंऔरअपनेकामपरध्यानकेंɞद्रतकरें।
4. ब्रेकलेंःɟनयɠमतब्रेकलेनेसेआपकोɝरचाजर्करनेऔरउत्पादकबनेरहनेमेंमददɠमलेगी।
5. अपनेआपकोपुरस्कृतकरेंःअपनेआपकोपुरस्कृतकरनेसेआपकोप्रेɝरतरहनेऔरअपनेलÛयोंकोप्राप्तकरनेके
ɡलएप्रेɝरतकरनेमेंमददɠमलेगी।
17

--- Page 18 ---

Technical Report
Example #A5
Prompt
मैनेबहोतजगहनौकरीकेɡलएएप्लाईɟकयापरकहीसेɝरप्लाईनहीआयाɣजस्सेमुझेɟडप्रेशनहोरहाहेमुझेइसकाकोई
उपायदो?
Model Response
यहसुनकरखेदहैɟकआपकोअवसादकासामनाकरनापड़रहाहै।यहयादरखनामहत्वपूणर्हैɟकअकेलेपन, ɭचʌताऔर
ɟनराशाजैसीभावनाओंकोदूरकरनेमेंमददकरनेकेकईतरीकेहैं।यहाँकुछसुझावɞदएगएहैंजोसहायकलगसकतेहैंः
1. ɟकसीɡचɟकत्सकयासलाहकारसेबातकरें-ɟकसीमानɡसकस्वाȹयपेशेवरसेबातकरनाआपकेअवसादकोप्रबंɠधत
करनेऔरइसेकमकरनेकʏ ɞदशामेंपहलाकदमहोसकताहै।वेआपकʏ भावनाओंकोसमझनेऔरउनपरकाबूपानेके
ɡलएएकयोजनाबनानेमेंआपकʏ मददकरसकतेहैं।
2. ɟनयɠमतȭायामःशारीɝरकगɟतɟवɠधएंडोɷफʌनछोड़तीहै, जोप्राकृɟतकमनोदशाबढ़ानेवालेहोतेहैं।यहांतकɟकछोटे
पैमानेकेȭायामजैसेचलना, तैरनायाकुछहल्काɰखʌचावभीअवसादग्रस्तताकʏ भावनाकोकमकरनेमेंमददकरसकता
है।
3. प्रकृɟतमेंसमयɟबताएँःप्रकृɟतमेंसमयɟबतानेसेतनावकोकमकरनेऔरकल्याणकʏ भावनाकोबढ़ावादेनेमेंमदद
ɠमलसकतीहै।आपटहलनेजासकतेहैं, पैदलयात्राकरसकतेहैंयाबागवानीकाकामकरकेप्रकृɟतमेंअपनीरुɡचɟवकɡसत
करसकतेहैं।
4. ɟप्रयजनोंकेसाथजुड़ेंःदोस्तों, पɝरवारयासहकɸमʌयोंकेसाथजुड़ेंजोसमथर्नऔरप्रोत्साहनप्रदानकरतेहैं।सामाɣजक
बातचीतकोप्रोत्साɟहतकरनेसेअलगावऔरअकेलेपनकʏ भावनाओंकोकमकरनेमेंमददɠमलसकतीहै।
5. रचनात्मकगɟतɟवɠधयोंमेंसंलग्नरहेंःकला, संगीतयालेखनजैसीरचनात्मकगɟतɟवɠधयोंमेंशाɠमलहोनेसेमनको
ɟवचɡलतकरनेऔरखुशीकʏ भावनालानेमेंमददɠमलसकतीहै।
6. माइंडफुलनेसतकनीकोंकोआजमाएँःध्यान, गहरीसांसलेनेकेअभ्यासयायोगसɟहतɟवɢभȡ माइंडफुलनेसतकनीकें
आरामकरनेऔरवतर्मानक्षणपरध्यानकेंɞद्रतकरनेमेंमददकरसकतीहैं।
7. आत्म-देखभालकाअभ्यासकरेंःपयार्प्तनींदलेना, संतुɡलतआहारखानाऔरस्वȸ जीवनशैलीबनाएरखनेजैसी
स्व-देखभालप्रथाओंमेंशाɠमलहोनाआवश्यकहै।इसमेंस्नानकरना, ɟकताबपढ़नायाटʍवीदेखतेहुएनाश्ताकरनाजैसी
चीजेंशाɠमलहोसकतीहैं।
8. सहायतासमूहोंमेंभागलेंःȸानीयसहायतासमूहयासामुदाɠयकसंगठनखोजनेकाप्रयासकरेंजोआपकेसमान
चुनौɟतयोंसेजूझरहेहों।दूसरोंसेजुड़कर, आपअपनेअवसादकोकमकरनेमेंमददकरनेकेतरीकोंकʏ पहचानकरसकते
हैं।
9. पेशेवरमददलेंःयɞदआपकेअवसादकाप्रबंधनकरनाबहुतकɞठनलगताहै, तोɡचɟकत्सायापरामशर्प्राप्तकरनेपर
ɟवचारकरें।एकप्रɡशɢक्षतमानɡसकस्वाȹयपेशेवरआपकोमुकाबलातंत्रसीखनेमेंमददकरसकताहैऔरआपकोअɠधक
सकारात्मकमानɡसकताɟवकɡसतकरनेमेंमददकरसकताहै।यादरखें, अवसादकोदूरकरनाआसाननहींहै, लेɟकनसही
समथर्नऔररणनीɟतयोंकेसाथ, आपप्रगɟतकरसकतेहैंऔरबेहतरमहसूसकरसकतेहैं।
18

--- Page 19 ---

Technical Report
Example #A6
Prompt
मैंउȉरभारतीयहूंऔरमूलɫहʌदʍ भाषीहूं।हालहीमें, मुझेअपनीनौकरीकेɡलएबैंगलोरɡशफ्टहोनापड़ा।मुझेयहांके
मूलɟनवाɡसयोंसेबातचीतकरनेमेंथोड़ीपरेशानीहोतीहैक्योंɟकवेकȡड़बोलतेहैंऔरɫहʌदʍ नहींजानतेहैं।मैंकȡड़
सीखनाचाहूंगीताɟकमुझेइससमस्याकासामनानकरनापड़े।मेरामागर्दशर्नकरेंɟकमैंखुदकोकȡड़भाषामेंकैसे
ɡशɢक्षतकरसकताहूं
Model Response
आपकेप्रȱ केɡलएधन्यवाद! बेंगलुरुजानेपरआपकोȸानीयलोगोंकʏ भाषासीखनेमेंकुछचुनौɟतयोंकासामनाकरना
पड़सकताहै, लेɟकनɭचʌतामतकरो-मददकेɡलएयहाँएकचरण-दर-चरणमागर्दɹशʌकादʍ गईहैः
कȡड़सीखनेकेɡलएयेकदमउठाएगएहैंः
कनार्टकसरकारद्वाराप्रदानɟकएजारहेमुफ्तकȡड़पाठ्यक्रम
2. कȡड़सीखनेवालेमंचजैसेɟक"कȡड़सीखें" या"अंगड़ी" जोकȡड़पाठोंऔरअभ्यासकायǏ तकपहुंचप्रदानकरते
हैं।
3. कȡड़वणर्माला, उǴारणऔरशब्दावलीसीखनाशुरूकरनेकेɡलएकȡड़केबुɟनयादʍ शब्दोंऔरवाक्यांशोंकोयाद
रखनेकाप्रयासकरें।आपअपनेदमपरऑनलाइनसंसाधनोंकाउपयोगकरकेयाअन्यकȡड़बोलनेवालोंकेसाथअभ्यास
करकेभीशुरुआतकरसकतेहैं।
4. कȡड़ȭाकरणऔरसंरचनाओंकेबारेमेंजाननेकेɡलएकȡड़ɟकताबेंयापɟत्रकाएंपढ़नाशुरूकरें।आपयूट्यूबचैनलों
परकȡड़सबकयावातार्लापसत्रोंकोदेखनेकाɟवकल्पभीचुनसकतेहैंɣजनमेंकȡड़भाषाशाɠमलहोसकतीहै।
5. कȡड़गीतों, ɟफल्मोंऔरटʍवीशोकाआनंदलेंɣजन्हेंआपसमझसकतेहैं।यहआपकोनएशब्दोंऔरअɢभȭɜक्तयों
कोसुननेऔरउनकाɟवȰेषणकरनेमेंमददकरेगा।
6. दैɟनकगɟतɟवɠधयोंऔरबातचीतमेंकȡड़काउपयोगकरनेकाअभ्यासकरें।उदाहरणकेɡलए, यɞदआपकेपासकॉफʏ
शॉपजानाहै, तोपहलेवहाँजातेसमयकȡड़मेंकुछछोटेवाक्यांशयाअɢभवादनआजमाएँ।
7. कȡड़मेंɟकसीदोस्तयापɝरवारकेसदस्यसेबातकरें।उन्हेंभाषाɡसखानेऔरउनसेसवालपूछनेसेआपनईचीजें
सीखनेऔरसुधारकरनेकेअवसरप्राप्तकरेंगे।
8. अन्यकȡड़भाषकोंकेसाथजुड़ेंɣजनकाआपअनुसरणकरसकतेहैंयाउनकʏ सामग्रीदेखसकतेहैं।चाहेवहकोई
फेसबुकसमूहहोयाएकभाषाɟवɟनमयकायर्क्रम, दूसरोंकेसंपकर्मेंरहनाआपकʏ प्रगɟतमेंसहायकहोगा।यादरखें, एक
अǵʍ नींवकेसाथ, आपɟनɢȮतरूपसेजल्दहीकȡड़धाराप्रवाहहोनेमेंसक्षमहोंगे।गुडलक!
19

--- Page 20 ---

Technical Report
A.2
EXAMPLES WHERE AIRAVATA OUTPUT HAS ERRORS
The model is prone to hallucinations and can present distorted facts as against the plot of the novel
in #B1 or may fail to follow the instructions provided (#B2).
Example #B1
Prompt
धरमवीरभारतीजीकाप्रɡसद्धउपन्यास"गुनाहोंकादेवता" केबारेमेंबताओऔरकहनीकेमुख्यɟकरदारसुधाऔरचंदर
केबारेमेंसंɢक्षप्तवणर्नकरें?
Model Response
गुनाहोंकादेवताएकलोकɟप्रयभारतीयक्लाɡसकहैजो18वींशताब्दʍ केअंतमेंɡलखागयाथा।यहकहानीसुधाऔरचंदर
नामकदोप्रेɠमयोंकʏ कहानीबतातीहै, ɣजन्हेंउनकेपɝरवारोंनेअलगकरɞदयाथा।सुधाअमीरपɝरवारसेआतीहैऔरउसे
एकअǵेपɟतकोखोजनेकेɡलएकईदावेदारोंपरɟवचारकरनापड़ताहै।चंदरएकगरीबɟकसानपɝरवारसेआताहैऔर
वहअपनीɡशक्षाऔरभɟवष्यमेंअपनेसपनोंकोपूराकरनेकेɡलएकड़ीमेहनतकरताहै।सुधाअंततःचंदरकोचुनतीहै
औरदोनोंशादʍ करलेतेहैं।हालाँɟक, उनकʏ खुशीअल्पकाɡलकहोतीहैक्योंɟकसुधाकाअɢभशापउसकेपूवर्जोंद्वाराडाला
जाताहैɟकवहकभीभीखुशनहींहोगी।सुधाऔरचंदरतबतकप्यारकरतेरहेजबतकɟकसुधामरजातीऔरचंदरɟफर
अपनाशेषजीवनअकेलेरहनेकेɡलएछोड़देता।उपन्यासकरुणाऔरप्रेमकेɟवषयोंकʏ पड़तालकरताहै, औरअक्सर
इसेरोमांɞटकसाɟहत्यकʏ उत्कृȲ कृɟतमानाजाताहै।
Example #B2
Prompt
मैंमधुबनीकलाकारीकेबारेमेंज़्यादाजानकारीकेɡलएउत्सुकहूँ| कृप्याइसकलाकारीकेबारेमेंमुझे१००शब्दोंमें
जानकारीदें|
Model Response
मुबɡलकलाएकप्रकारकʏ अमूतर्कलाहैजोमानवशरीरऔरअंगोंकाप्रɟतɟनɠधत्वकरतीहै।यहएकबहुमुखीकलारूपहै
ɣजसेपारंपɝरकऔरसमकालीनदोनोंतरीकोंसेɟकयाजासकताहै, औरइसकाउपयोगअक्सरɡचत्रकला, मूɷतʌकलाऔर
प्रदशर्नजैसेɟवɢभȡ माध्यमोंमेंɟकयाजाताहै।
20

```
