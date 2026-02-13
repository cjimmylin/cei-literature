---
title: "2023-Nguyen-VinaLLaMA LLaMA-based Vietnamese Foundation Model - PDF Extract"
source_pdf: "2023-Nguyen-VinaLLaMA LLaMA-based Vietnamese Foundation Model.pdf"
pages: 13
extracted_at: "2026-02-13T09:50:30.608825"
---

# PDF Extract: 2023-Nguyen-VinaLLaMA LLaMA-based Vietnamese Foundation Model

**Source PDF:** 2023-Nguyen-VinaLLaMA LLaMA-based Vietnamese Foundation Model.pdf
**Total Pages:** 13

---

## Content

```
--- Page 1 ---

VinaLLaMA: LLaMA-based Vietnamese Foundation Model
Quan Nguyen∗, Huy Pham and†Dung Dao‡
December 19, 2023
Abstract
In this technical report, we present VinaLLaMA, an open-weight, state-of-the-art (SOTA)
Large Language Model for the Vietnamese language, built upon LLaMA-2 with an additional
800 billion trained tokens. VinaLLaMA not only demonstrates fluency in Vietnamese but also
exhibits a profound understanding of Vietnamese culture, making it a truly indigenous model.
VinaLLaMA-7B-chat, trained on 1 million high-quality synthetic samples, achieves SOTA results
on key benchmarks, including VLSP, VMLU, and Vicuna Benchmark Vietnamese, marking a
significant advancement in the Vietnamese AI landscape and offering a versatile resource for various
applications.
1
Introduction
The surge in Large Language Models (LLMs) such as ChatGPT and GPT-4 has significantly advanced
the field of artificial intelligence (AI), particularly in language processing.
In 2023, Vietnam’s AI
sector witnessed a notable development with the introduction of several Vietnamese-centric LLMs,
including BLOOMZ’s Vietcuna, URA-LLaMA, PhoGPT, and dama-2. Amidst this progression, we
introduce VinaLLaMA, a foundational LLM designed specifically for the Vietnamese language. VinaL-
LaMA, built on top of LLaMA-2, represents a vital stride towards linguistic inclusivity in AI, adeptly
addressing the syntactic and semantic intricacies of Vietnamese.
Embracing the spirit of collaboration and open innovation, we are pleased to announce VinaLLaMA,
an open-weight Foundation Language Model and its chat variant. These models are now accessible
on HuggingFace, ensuring compatibility with all ’transformers’ framework-supported libraries. This
endeavor not only contributes to the global AI research landscape but also provides a specialized tool
for exploring and enhancing Vietnamese language processing, encouraging a wider engagement and
application in AI-driven NLP research.
2
Related Work
2.1
Large Language Models
The development of large language models (LLMs) began with the Transformer [VSP+17], the foun-
dational architecture that enabled the pre-training of BERT [CMCC23] and GPT [RNSS] using large-
scale unsupervised data. This advancement led to the emergence of popular foundation models such
as RoBERTa [LOG+19], T5 [RSR+20], and BART [LLG+20].
Subsequently, GPT-3 [BMR+20] demonstrated capabilities in few-shot and zero-shot learning
through prompt engineering and in-context learning. This was followed by significant advancements
with ChatGPT (OpenAI, 2022) and GPT-4 (OpenAI, 2023), which have made substantial contribu-
tions not only in language modeling but also in the broader field of artificial intelligence. These models
exhibit a diverse range of skills and produce high-quality outputs, leading to the rise of newer LLMs
such as Llama [RSR+20], Llama-2 [TMS+23], Bloom [WSF+22], Falcon [AAA+23], Qwen [BBC+23],
and Mistral [JSM+23].
∗Virtual Interactive, qnguyen3@vilm.org
†Virtual Interactive, huypn@vilm.org
‡Virtual Interactive, dungdm@vilm.org
1
arXiv:2312.11011v1  [cs.CL]  18 Dec 2023

--- Page 2 ---

2.2
Vietnamese Large Language Models
The Vietnamese LLM landscape has seen significant advancements with models like Vietcuna [NPD23b],
which underwent further pre-training on BLOOMZ [WSF+22], followed by fine-tuning with the OpenOrca-
Viet [NPD23a] dataset. Another model, URA-Llama [NTN+23], was developed through fine-tuning on
a corpus of Vietnamese articles, building upon Llama-2’s architecture. DopikAI’s ViGPT™[NTNV23]
also made strides by continuing pre-training and supervised fine-tuning atop GPT-J-Vietnamese-News
[Vie21], pre-trained by VietAI. Additionally, PhoGPT [NNT+23] represents a significant development,
initially pre-trained on a 41GB text corpus, and later fine-tuned with a dataset of 150,000 samples,
enhancing its proficiency in Vietnamese text understanding and generation.
2.3
Alignment
Instruction tuning is a critical aspect of aligning large language models (LLMs) with human interaction
patterns, enhancing their ability in in-context learning, reasoning, and instruction learning.
Flan
[WBZ+21] introduced this approach with a comprehensive dataset featuring a wide array of tasks and
templates, closely mimicking human instructional styles. This approach involves refining the model’s
responses to align more closely with human instructional patterns, thereby making the model’s output
more intuitive and user-friendly.
InstructGPT [OWJ+22] extended this approach by incorporating human feedback, refining the
models to produce less toxic and higher quality text. This method of emulating human interaction in
instruction tuning has been pivotal in improving the performance and user-friendliness of LLMs.
Further advancements include the integration of chat data from open-assistant datasets in mod-
els like Vicuna and Guanaco, and the use of synthetic datasets generated by GPT-3.5 and GPT-4,
such as OpenOrca [WKM+22] and Platypus [LHR23]. These developments have further enhanced
the conversational capabilities of LLMs, making them more adept at handling real-world interaction
scenarios.
3
Training Procedure
3.1
Pretraining
LLaMA-2, a highly regarded pre-trained language model in English, shows a significant gap in handling
Vietnamese-related content due to limited relevant tokens in its training set. Additionally, its original
tokenizer falls short in multilingual applications. To address these issues, we compiled a new pretraining
dataset combining public and synthetic in-house data. We selected BKAI’s LLaMA-2-chat tokenizer
[Lab23] for the tokenizer, which has been specifically made for Vietnamese.
This tokenizer shows
enhanced performance in processing the Vietnamese language, making it a suitable choice for our
VinaLLaMA model.
3.1.1
Public Data
Books. The dataset encompassing Vietnamese literature in our study is comprehensive, comprising
250,000 volumes. This extensive collection spans various domains, including science, history, finance,
and philosophy, as well as fiction genres like novels and science fiction, in addition to traditional Viet-
namese literature. The distribution of these categories is methodically illustrated in Figure 1.
Public News. The dataset under examination is derived from two principal Vietnamese news sources,
VnExpress 1 and BaoMoi 2. This compilation encompasses an exhaustive collection of articles dis-
seminated by these entities from January 1, 2010, through September 30, 2023. To align with ethical
guidelines and content appropriateness standards, a filtration process was implemented, systematically
excluding articles that contained keywords indicative of harmful or violent content. The inclusion of
this public news data is crucial, as it helps the model better understand and represent important
aspects related to Vietnam and its people.
1VnExpress
2BaoMoi
2

--- Page 3 ---

25%
15%
7.5%
7.5%
30%
15%
Science (25%)
History (15%)
Finance (7.5%)
Philosophy (7.5%)
Novel & Sci-fi (30%)
Vietnamese Literature (15%)
Figure 1: Distribution of Book Topics Used in VinaLLaMA training.
Figure 2: The first stage of generating synthetic data for pretraining
Finally, we also include a subset of Vietnamese from CulturaX [NNL+23] and an additional 100B
tokens in English. The final public dataset has a total of roughly 330 billion tokens.
3.1.2
In-house Data
Influenced by the concept of synthetic textbooks for pretraining [GZA+23], our approach incorporates
a mechanism that selects random text segments from a publicly available dataset. These segments
are then integrated into over 80 bespoke prompt templates, each meticulously crafted to facilitate
the rewriting task. The prompts, when fed into GPT-4, result in roughly 100,000 samples. These
samples represent a high-quality synthetic dataset, specifically tailored for pretraining purposes. The
methodology and workflow of this process are illustrated in Figure 2.
Additionally, we employed Vietcuna-3B-v2, our successor smaller-scale language model, to train on
the synthetic samples generated in Step 1. This training process utilized the rewriting task-specific
prompts previously developed (as outlined in Step 2.1), which is detailed in Figure 3. Subsequently,
we replicated the procedure from Step 1 using this newly trained model. This iteration resulted in
the generation of over 500 billion synthetic tokens, a process detailed in Step 2.2. The final result of
this process is more than 500 billion of high-quality Vietnamese tokens ready to be used to continue
pretraining on the base LLaMA 2 with the expanded tokenizer.
3

--- Page 4 ---

Figure 3: Our second stage of generating synthetic data for pretraining. Vietcuna-3B-v2 was deployed
to save cost while maintaining the same performance with distillation from GPT-4
3.2
Supervised Instruction Fine-tuning
In collaboration with Nous Research 3, we employed proprietary methodologies to create 500,000 Viet-
namese synthetic samples. These samples encompassed both instructional and conversational formats.
To enhance the dataset, an additional 500,000 English samples were sourced from the OpenHermes-2.5
[tek23] and Capybara [DS23] datasets, also provided by Nous Research. This integration of datasets
culminated in a comprehensive collection of 1 million samples, paving the way for the development of
a bilingual language model. The comprehensive final dataset encompasses an array of tasks, including
reasoning, role-playing, poem writing, coding, function calling, and agent prompting. This diversity
ensures a broad scope of capabilities in the final model. We conducted a full fine-tuning of our pre-
trained model over four epochs, which led to the creation of a state-of-the-art foundation language
model specifically tailored for the Vietnamese language, more on the result in Section 4.
3.3
VinaLLaMA-2.7B
Adopting the structured pruning procedure outlined in [XGZC23], we successfully reduced our model
to a more compact variant with 2.7 billion parameters. This process involved strategically pruning
the network while retaining its core functional capabilities. Following the reduction in size, we applied
the same supervised fine-tuning methodology to this smaller variant as was used for the 7B model,
ensuring consistency in the training approach across different model scales.
3.4
Training Details
For our pretraining phase, we utilized a cluster consisting of eight nodes, each equipped with 8x Intel
Habana Gaudi2 Processors. This phase was completed over the course of one week. In contrast, the
fine-tuning phase was conducted more rapidly, utilizing a single node of Google Cloud TPU v5e, and
completed within a single day.
Additionally, our smaller 2.7 billion parameters variant, underwent an easier process. This variant
was both continued pre-trained and fully fine-tuned over a period of five days. This process was carried
out on a single node, which was provisioned with 8x NVIDIA A100 80GB GPUs. The use of such
high-performance hardware facilitated the efficient handling of the substantial computational demands
associated with training and fine-tuning a model of this scale.
3Nous Research
4

--- Page 5 ---

4
Evaluation
In our research, we utilized three distinct evaluation benchmarks: VLSP, VMLU, and the Vicuna
Benchmark, with the latter being translated into Vietnamese by VinAI Research. For each of these
benchmarks, we implemented a dual-evaluation approach. Specifically, we conducted separate exper-
iments for two categories of models: those in their pre-trained state and those that had undergone
instructional fine-tuning. This methodology allowed us to compare the baseline capabilities of the
pre-trained models against their performance post-instructional fine-tuning, providing insights into
the effectiveness of fine-tuning in enhancing model proficiency within the context of these Vietnamese
language benchmarks.
For the pre-training benchmarks, we selected VLSP’s hoa-7b, BKAI-LLaMA-2, ViGPT™, BLOOM-
7B, and PhoGPT-7B5 as the base models. In contrast, the instructional fine-tuned benchmarks com-
prised BLOOMZ-7B, ViGPT™-170K, Vietcuna-7B-v3, PhoGPT-7B5-Instruct, URA-LLaMA-13B and
SeaLLM-7B-chat. This diverse set of models provided a comprehensive perspective, enabling us to
assess both the inherent capabilities of these models in their original form and their enhanced perfor-
mance post-fine-tuning, specifically tailored to the Vietnamese language benchmarks.
4.1
VLSP
The first benchmark employed is the VLSP-LLM 2023 [CHC+23]. This benchmark parallels the Open-
LLM Leaderboard by HuggingFace, tailored specifically for the Vietnamese language. It encompasses
four distinct assessments: ARC Challenge, HellaSwag, MMLU, and TruthfulQA, each meticulously
adapted to Vietnamese. This comprehensive benchmark suite allows for a robust evaluation of lan-
guage models in understanding and generating Vietnamese text across various domains and complex-
ities. The results are reported in Table 1 and Table 2. In the pretrained segment of our study, the
VinaLLaMA-7B model demonstrated superior performance compared to other open-source Large Lan-
guage Models (LLMs) that support Vietnamese. This was evident in its outperformance on three of
the four benchmarks, leading to it achieving state-of-the-art results based on the average score across
these benchmarks. This signifies the robustness and effectiveness of the VinaLLaMA-7B model in
handling a variety of tasks in the Vietnamese language context.
In the supervised fine-tuning domain, our results continued to reflect a high level of excellence. No-
tably, VinaLLaMA-7B-chat, comparable in scale, astonishingly outperformed larger models, including
those with 13 billion parameters, in terms of average score. This impressive achievement highlights the
efficacy of the fine-tuning process and the model’s adeptness at leveraging its training to deliver out-
standing performance, even against much larger counterparts. Adding to this, the VinaLLaMA-2.7B,
a significantly smaller model, showcased remarkable performance. It not only competed closely with
larger 7B variants but also exceeded PhoGPT-7B5-Instruct in performance while achieving inferencing
speeds 60% faster. This showcases the model’s optimized balance between size, speed, and perfor-
mance. The success of VinaLLaMA-7B-chat, and the noteworthy performance of VinaLLaMA-2.7B,
underscore the considerable potential of well-implemented fine-tuning strategies with synthetic data
in elevating the capabilities of Large Language Models, especially in contexts requiring specialized
language processing.
5

--- Page 6 ---

Model
arc vi
hellaswag vi
mmlu vi
truthfulqa vi
Average
(25-shot)
(10-shot)
(0-shot)
(0-shot)
hoa-7b
0.2855
0.4329
0.2536
0.4542
0.3566
BKAI-LLaMA-2
0.2975
0.4402
0.3039
0.4542
0.3740
BLOOM-7B
0.3255
0.4830
0.2810
0.4701
0.3899
ViGPT™
0.2596
0.3877
0.2482
0.4612
0.3392
PhoGPT-7B5
0.2496
0.2577
0.2474
0.4677
0.3056
VinaLLaMA-2.7B
0.2906
0.4337
0.2490
0.4608
0.3585
VinaLLaMA-7B
0.3350
0.4956
0.3168
0.4552
0.4007
Table 1: VLSP Benchmark Scores of Pretrained Models
Model
arc vi
hellaswag vi
mmlu vi
truthfulqa vi
Average
(25-shot)
(10-shot)
(0-shot)
(0-shot)
URA-LLaMA-13B
0.3752
0.4830
0.3973
0.4574
0.4282
BLOOMZ-7B
0.3205
0.4930
0.3975
0.4523
0.4158
ViGPT™-170K
0.3651
0.4777
0.3412
0.4691
0.4133
PhoGPT-7B5-Instruct
0.2470
0.2578
0.2413
0.4759
0.3055
SeaLLM-7B-chat
0.3607
0.5112
0.3339
0.4948
0.4252
Vietcuna-7b-v3
0.3419
0.4939
0.3354
0.4807
0.4130
VinaLLaMA-2.7B-chat
0.3274
0.4814
0.3051
0.4972
0.4028
VinaLLaMA-7B-chat
0.4239
0.5407
0.3932
0.5251
0.4707
Table 2: VLSP Benchmark Scores of Supervised Fine-tuning Models
4.2
VMLU
VMLU [AoST23], a benchmark suite tailored for evaluating foundation models in the Vietnamese
language, comprises 10,880 multiple-choice questions across 58 subjects in domains like STEM, Hu-
manities, and Social Sciences. Its diverse range of difficulty levels tests models from basic knowledge to
advanced problem-solving. We selected VMLU for benchmarking due to its comprehensive coverage of
Vietnam-related questions, providing a relevant and challenging environment for assessing model ca-
pabilities in a context-specific manner. We conducted our experiments on the validation set of VMLU
since the answers to the test set are not publicly available, URA-LLaMA-13B is also not being tested
due to the lack of availability at testing time. We reported the results under two few-shot settings:
0-shot and 5-shot, which can be viewed in Table 3 and 4.
6

--- Page 7 ---

Model
(0-shot)
(5-shot)
ViGPT™
0.2379
0.2769
hoa-7b
0.2513
0.2903
BKAI-LLaMA-2
0.2678
0.2513
BLOOM-7B
0.2527
0.2312
PhoGPT-7B5
0.2352
0.2325
VinaLLaMA-2.7B
0.2245
0.2688
VinaLLaMA-7B
0.3199
0.3414
Table 3: VMLU Benchmark Scores of Pretrained Models
Model
(0-shot)
(5-shot)
ViGPT™-170K
0.2419
0.2567
BLOOMZ-7B
0.3945
0.3831
PhoGPT-7B5-Instruct
0.2298
0.2379
SeaLLM-7B-chat
0.2903
0.3508
Vietcuna-7b-v3
0.3441
0.3199
VinaLLaMA-2.7B-chat
0.2702
0.2567
VinaLLaMA-7B-chat
0.4046
0.4140
Table 4: VMLU Benchmark Scores of Supervised Fine-tuning Models
4.3
Vicuna Benchmark Vietnamese
The Vicuna Benchmark [ZCS+23], translated into Vietnamese by VinAI, serves as our final bench-
mark. This comprehensive benchmark is composed of 80 distinct instructions spanning 9 diverse areas,
providing a broad spectrum for assessing model capabilities. Uniquely, the evaluation of the results
from all participating models is conducted using GPT-4, which introduces an innovative approach to
performance assessment. This methodology employs an ELO ranking system, traditionally used in
chess and other competitive games, to rate the models. Such a system offers a dynamic and rela-
tive measure of model performance, allowing for a nuanced and comparative analysis of each model’s
proficiency in handling a variety of tasks and instructions within the benchmark. This ELO-based
evaluation provides a clear and quantifiable ranking of the models, reflecting their effectiveness and
adaptability in the context of the Vietnamese language and the specific challenges presented by the
Vicuna Benchmark.
In our Vicuna Benchmark evaluation, responses from models were assessed using a detailed five-
point scale: 0 (’very bad’), 1 (’bad’), 2 (’ok’), 3 (’good’), and 4 (’very good’). This granular scoring
system allows for an in-depth evaluation of the quality of each model’s response. The final ELO score
for each model is computed by aggregating these individual ratings, providing a holistic measure of a
7

--- Page 8 ---

model’s overall performance across the benchmark’s varied tasks.
To ensure language relevance, we implemented a strict rule: any response not in Vietnamese is
automatically assigned a score of 0. This criterion underscores the importance of language-specific
accuracy in our evaluation. The collective results, reflecting model performances across different tasks,
are visually represented in Figure 4.
In the interest of transparency and further research, we have made VinaLLaMA’s responses and
our evaluation code publicly available 4 5. This not only allows for independent verification of our
results but also facilitates further advancements in the field by providing valuable resources to other
researchers.
Figure 4: Score Distributions Assigned by GPT-4 Across Different Models: VinaLLaMA’s Exceptional
Performance Competing Closely with ChatGPT-3.5-Turbo in Multiple Benchmark Assessments
Model
Coding
Common-Sense
Counterfactual
Fermi
PhoGPT-7B5-Instruct
0.000
3.600
3.100
0.000
ViGPT™-170K
0.500
2.500
1.600
2.400
URA-LLaMA-13B
0.714
0.600
0.200
0.000
URA-LLaMA-7B
0.000
0.200
1.100
0.000
ChatGPT
4.000
4.000
4.000
3.700
VinaLLaMA-7B-chat
2.714
4.000
4.000
3.500
Table 5: Average Scores of Different Models Across Tasks in Vicuna Benchmark(Part 1)
The benchmark results revealed that VinaLLaMA showcased commendable performance in Viet-
4Viet-Eval-GPT-4
5vilm-ai/viet-llm-eval
8

--- Page 9 ---

namese, closely trailing behind ChatGPT-3.5-Turbo in some benchmarks. This indicates that VinaL-
LaMA is highly effective in Vietnamese language tasks, with only a slight margin separating it from
the more advanced ChatGPT-3.5-Turbo, as shown in Table 5 and Table 6.
PhoGPT also demonstrated better outcomes compared to other Vietnamese benchmarks, yet it
still fell significantly behind in some areas, highlighting potential avenues for improvement.
In contrast, URA-LLaMA-7B and 13B models performed less effectively, with some of their re-
sponses not aligning with Vietnamese language requirements. This points to a critical need for targeted
enhancements or language-specific training for these models to better cater to Vietnamese language
processing.
Model
Generic
Knowledge
Math
Roleplay
Writing
PhoGPT-7B5-Instruct
3.500
3.900
0.000
3.800
3.900
ViGPT™-170K
3.500
3.300
0.000
2.900
2.900
URA-LLaMA-13B
0.500
0.200
1.333
0.000
0.000
URA-LLaMA-7B
0.200
0.300
0.000
0.000
0.600
ChatGPT
4.000
4.000
4.000
4.000
4.000
VinaLLaMA-7B-chat
4.000
4.000
4.000
4.000
4.000
Table 6: Average Scores of Different Models Across Tasks in Vicuna Benchmark(Part 2)
4.4
HuggingFace OpenLLM Leaderboard (English)
Our approach in developing VinaLLaMA involved continued pretraining and fine-tuning with both
English and Vietnamese data, aiming to establish it as a bilingual large language model. This strategy
is key to enhancing its linguistic versatility and adaptability.
We have documented VinaLLaMA’s performance metrics on the HuggingFace OpenLLM Leader-
board, providing a comparative analysis with other open-source models. These results, detailed in
Table 7, offer insights into VinaLLaMA’s standing in the realm of bilingual language models. This
information is crucial for understanding its bilingual proficiency and for benchmarking its capabilities
against existing models in the field. The performance of both the VinaLLaMA-7B-chat and 2.7B-chat
models was particularly noteworthy, not only achieving the highest overall scores but also showing
remarkable strength in mathematical benchmarks, specifically the GSM8K. This highlights their ca-
pability in complex problem-solving and analytical reasoning, areas often challenging for language
models.
Remarkably, VinaLLaMA-7B-chat exhibited exceptional performance, surpassing even the rein-
forcement learning-enhanced variants of Meta’s LLaMA-2-chat. This achievement is significant, con-
sidering the advanced nature of reinforcement learning models and their typically strong performance
in such tasks. The success of VinaLLaMA-7B-chat in this regard underscores its advanced capabilities
and positions it as a leading model in the domain of mathematics and logic-based problem-solving.
9

--- Page 10 ---

Model
arc
hellaswag
mmlu
truthfulqa
winogrande
GSM8K
Average
(25-shot)
(10-shot)
(5-shot)
(0-shot)
(5-shot)
(5-shot)
LLaMA-2 7B-chat-hf
0.5290
0.7855
0.4832
0.4557
0.7174
0.0735
0.5074
BLOOMZ-7B
0.4078
0.6209
0.3613
0.4522
0.6535
0.0008
0.4161
MPT-7B-chat
0.4625
0.7587
0.3762
0.4056
0.6843
0.0409
0.4547
Nous-Capybara-7B
0.5520
0.7876
0.4880
0.4907
0.7340
0.0690
0.5202
VinaLLaMA-2.7B-chat
0.3891
0.6556
0.3323
0.4838
0.5904
0.1350
0.4310
VinaLLaMA-7B-chat
0.5000
0.7293
0.4753
0.4969
0.6346
0.3002
0.5227
Table 7: HuggingFace OpenLLM Leaderboard Benchmark Scores of Supervised Fine-tuning Models
10

--- Page 11 ---

5
Acknowledgement
We are also immensely grateful to the teams at Nous Research, LAION, and Symato Team. Their
assistance in the early stages of VinaLLaMA’s evaluation was crucial, providing insights that guided
further improvements and enhancements of the model. We also want to send our appreciation to Nam
Pham 6, Nhan Nguyen 7, @Teknium1 8 and @ldjconfirmed 9 for their contribution to our dataset
creation.
Lastly, our profound appreciation is extended to Google Cloud and StabilityAI. Their generous
computational support was a cornerstone in bringing VinaLLaMA to fruition, enabling the intensive
training and development processes required for such a sophisticated large language model. Their
contribution was vital in transforming our vision for VinaLLaMA into a reality.
6
Conclusion
In conclusion, the development of VinaLLaMA marks a significant milestone in the realm of language
models, particularly in the context of Vietnamese language processing.
Achieving state-of-the-art
(SOTA) scores across all Vietnamese benchmarks, VinaLLaMA has demonstrated exceptional profi-
ciency and adaptability. While its performance in English benchmarks was slightly less dominant, it
still showed considerable competence, underscoring its effectiveness as a bilingual model.
A key factor in VinaLLaMA’s success is the strategic use of carefully crafted synthetic data in
its training regimen. This approach has proven to be highly effective, yielding impressive results and
highlighting the importance of diverse and well-designed training datasets in the development of robust
language models.
VinaLLaMA’s achievements not only set a new standard for language models in Vietnamese but also
contribute valuable insights into the broader field of natural language processing. It exemplifies how
meticulous data preparation and comprehensive training can significantly enhance the capabilities of
language models, paving the way for future advancements in this dynamic and rapidly evolving domain.
6Nam Pham, HuggingFace
7Nhan Nguyen, HuggingFace
8@Teknium, X
9@ldjconfirmed, X
11

--- Page 12 ---

References
[AAA+23]
Ebtesam Almazrouei, Hamza Alobeidli, Abdulaziz Alshamsi, Alessandro Cappelli, Ruxan-
dra Cojocaru, Daniel Hesslow, Julien Launay, Quentin Malartic, Daniele Mazzotta,
Badreddine Noune, et al.
The falcon series of open language models.
arXiv preprint
arXiv:2311.16867, 2023.
[AoST23]
Zalo AI, Japan Advanced Institute of Science, and Technology.
Vmlu: A vietnamese
multitask language understanding benchmark suite for large language models. 2023.
[BBC+23]
Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin
Ge, Yu Han, Fei Huang, et al. Qwen technical report. arXiv preprint arXiv:2309.16609,
2023.
[BMR+20]
Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla
Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Lan-
guage models are few-shot learners. Advances in neural information processing systems,
33:1877–1901, 2020.
[CHC+23]
Le Anh Cuong, Nguyen Trong Hieu, Nguyen Viet Cuong, Nguyen Ngoc Quoc, Le-Minh
Nguyen, and Cam-Tu Nguyen. Vlsp 2023 challenge on vietnamese large language models.
2023.
[CMCC23]
Llinet Benavides Cesar, Miguel-´Angel Manso-Callejo, and Calimanut-Ionut Cira. Bert
(bidirectional encoder representations from transformers) for missing data imputation in
solar irradiance time series. Engineering Proceedings, 39(1):26, 2023.
[DS23]
Luigi Daniele and Suphavadeeprasit. Amplify-instruct: Synthetically generated diverse
multi-turn conversations for effecient llm training. arXiv preprint arXiv:(comming soon),
2023.
[GZA+23]
Suriya Gunasekar, Yi Zhang, Jyoti Aneja, Caio C´esar Teodoro Mendes, Allie Del Giorno,
Sivakanth Gopi, Mojan Javaheripi, Piero Kauffmann, Gustavo de Rosa, Olli Saarikivi,
Adil Salim, Shital Shah, Harkirat Singh Behl, Xin Wang, S´ebastien Bubeck, Ronen Eldan,
Adam Tauman Kalai, Yin Tat Lee, and Yuanzhi Li. Textbooks are all you need, 2023.
[JSM+23]
Albert Q Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh
Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile
Saulnier, et al. Mistral 7b. arXiv preprint arXiv:2310.06825, 2023.
[Lab23]
BKAI-HUST Foundation Models Lab. Llama-2-bk, 2023.
[LHR23]
Ariel N Lee, Cole J Hunter, and Nataniel Ruiz. Platypus: Quick, cheap, and powerful
refinement of llms. arXiv preprint arXiv:2308.07317, 2023.
[LLG+20]
Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed,
Omer Levy, Veselin Stoyanov, and Luke Zettlemoyer.
Bart:
Denoising sequence-to-
sequence pre-training for natural language generation, translation, and comprehension.
In Proceedings of the 58th Annual Meeting of the Association for Computational Linguis-
tics, pages 7871–7880, 2020.
[LOG+19]
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy,
Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. Roberta: A robustly optimized bert
pretraining approach. 2019.
[NNL+23]
Thuat Nguyen, Chien Van Nguyen, Viet Dac Lai, Hieu Man, Nghia Trung Ngo, Franck
Dernoncourt, Ryan A. Rossi, and Thien Huu Nguyen. Culturax: A cleaned, enormous,
and multilingual dataset for large language models in 167 languages, 2023.
12

--- Page 13 ---

[NNT+23]
Dat Quoc Nguyen, Linh The Nguyen, Chi Tran, Dung Ngoc Nguyen, Nhung Nguyen,
Thien Huu Nguyen, Dinh Phung, and Hung Bui. Phogpt: Generative pre-training for
vietnamese. arXiv preprint arXiv:2311.02945, 2023.
[NPD23a]
Quan Nguyen, Huy Pham, and Dung Dao. Openorca-viet. 2023.
[NPD23b]
Quan Nguyen, Huy Pham, and Dung Dao. Vietcuna. 2023.
[NTN+23]
Duc Q. Nguyen, Sang T. Truong, Toan D. V. Nguyen, Dong D. Le, Nhi N. Truong, and
Tho Quan. Ura-llama: Universal adapted large language model for vietnamese. 2023.
[NTNV23]
Minh Thuan Nguyen, Khanh Tung Tran, Nhu Van Nguyen, and Xuan-Son Vu. ViGPTQA
- state-of-the-art LLMs for Vietnamese question answering: System overview, core models
training, and evaluations. In Mingxuan Wang and Imed Zitouni, editors, Proceedings of the
2023 Conference on Empirical Methods in Natural Language Processing: Industry Track,
pages 754–764, Singapore, December 2023. Association for Computational Linguistics.
[OWJ+22]
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin,
Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob
Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder,
Paul F Christiano, Jan Leike, and Ryan Lowe. Training language models to follow instruc-
tions with human feedback. In S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho,
and A. Oh, editors, Advances in Neural Information Processing Systems, volume 35, pages
27730–27744. Curran Associates, Inc., 2022.
[RNSS]
Alec Radford, Karthik Narasimhan, Tim Salimans, and Ilya Sutskever. Improving lan-
guage understanding by generative pre-training.
[RSR+20]
Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael
Matena, Yanqi Zhou, Wei Li, and Peter J Liu. Exploring the limits of transfer learning with
a unified text-to-text transformer. The Journal of Machine Learning Research, 21(1):5485–
5551, 2020.
[tek23]
teknium. teknium/openhermes-2.5-mistral-7b. 2023.
[TMS+23]
Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine
Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al.
Llama 2: Open foundation and fine-tuned chat models. arXiv preprint arXiv:2307.09288,
2023.
[Vie21]
VietAI. Gpt-j 6b on vietnamese news, 2021.
[VSP+17]
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N
Gomez,  Lukasz Kaiser, and Illia Polosukhin. Attention is all you need. Advances in neural
information processing systems, 30, 2017.
[WBZ+21]
Jason Wei, Maarten Bosma, Vincent Zhao, Kelvin Guu, Adams Wei Yu, Brian Lester, Nan
Du, Andrew M Dai, and Quoc V Le. Finetuned language models are zero-shot learners.
In International Conference on Learning Representations, 2021.
[WKM+22] Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A Smith, Daniel
Khashabi, and Hannaneh Hajishirzi. Openorca. arXiv preprint arXiv:2212.10560, 2022.
[WSF+22]
BigScience Workshop, Teven Le Scao, Angela Fan, Christopher Akiki, Ellie Pavlick,
Suzana Ili´c, Daniel Hesslow, Roman Castagn´e, Alexandra Sasha Luccioni, Fran¸cois Yvon,
et al. Bloom: A 176b-parameter open-access multilingual language model. arXiv preprint
arXiv:2211.05100, 2022.
[XGZC23]
Mengzhou Xia, Tianyu Gao, Zhiyuan Zeng, and Danqi Chen. Sheared llama: Accelerating
language model pre-training via structured pruning, 2023.
[ZCS+23]
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao
Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric. P Xing, Hao Zhang, Joseph E. Gonzalez,
and Ion Stoica. Judging llm-as-a-judge with mt-bench and chatbot arena, 2023.
13

```
