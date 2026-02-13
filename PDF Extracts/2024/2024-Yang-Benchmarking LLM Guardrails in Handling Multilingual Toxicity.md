---
title: "2024-Yang-Benchmarking LLM Guardrails in Handling Multilingual Toxicity - PDF Extract"
source_pdf: "2024-Yang-Benchmarking LLM Guardrails in Handling Multilingual Toxicity.pdf"
pages: 8
extracted_at: "2026-02-13T09:50:30.667060"
---

# PDF Extract: 2024-Yang-Benchmarking LLM Guardrails in Handling Multilingual Toxicity

**Source PDF:** 2024-Yang-Benchmarking LLM Guardrails in Handling Multilingual Toxicity.pdf
**Total Pages:** 8

---

## Content

```
--- Page 1 ---

Benchmarking LLM Guardrails in Handling Multilingual Toxicity
Yahan Yang
University of Pennsylvania
yangy96@seas.upenn.edu
Soham Dan *
Microsoft
sohamdan@microsoft.com
Dan Roth
University of Pennsylvania
danr@seas.upenn.edu
Insup Lee
University of Pennsylvania
lee@seas.upenn.edu
Abstract
With the ubiquity of Large Language Models
(LLMs), guardrails have become crucial to de-
tect and defend against toxic content. However,
with the increasing pervasiveness of LLMs in
multilingual scenarios, their effectiveness in
handling multilingual toxic inputs remains un-
clear. In this work, we introduce a compre-
hensive multilingual test suite, spanning seven
datasets and over ten languages, to benchmark
the performance of state-of-the-art guardrails.
We also investigates the resilience of guardrails
against recent jailbreaking techniques, and as-
sess the impact of in-context safety policies and
language resource availability on guardrails’
performance. Our findings show that existing
guardrails are still ineffective at handling mul-
tilingual toxicity and lack robustness against
jailbreaking prompts. This work aims to iden-
tify the limitations of guardrails and to build a
more reliable and trustworthy LLMs in multilin-
gual scenarios. Warning: This paper contains
potentially harmful examples.
1
Introduction
Large language models (LLMs) (Touvron et al.,
2023; Brown et al., 2020) have shown significant
potential across a variety of applications. However,
deploying LLMs for safety-critical application in-
troduces substantial concerns. Recent studies (An-
driushchenko et al., 2024; Chao et al., 2023; Liu
et al., 2024) demonstrate that LLMs can be easily
manipulated by malicious inputs to produce unde-
sirable responses and spread the harmful informa-
tion. Addressing the challenge of protecting both
LLMs and users from such inputs without compro-
mising the models’ performance is an emerging
research area. Developing standalone guardrails
(Inan et al., 2023; Ghosh et al., 2024; Ji et al., 2023)
for LLMs offers an effective defense against harm-
ful content and provides the adaptability needed
for different scenarios (Dong et al., 2024).
*Work done prior to joining Microsoft
Figure 1: The guardrails are providing inconsistent pre-
dictions for English and Thai inputs with the same se-
mantic meaning. In this case, we are using LLaMa-
Guard-3 as the guardrail model which supports Thai.
Harmful/toxic content detection has been a focus
of study for many years (Röttger et al., 2022; Stap-
pen et al., 2020; Kurita et al., 2019). Traditional
encoder-only classifiers like BERT (Devlin et al.,
2019) are often confined to the training distribution,
which limits their generalization and adaptability
to definitions of harmful content in practical ap-
plications (Markov et al., 2022; Lin et al., 2023).
Recent guardrail research (Li et al., 2024; Inan
et al., 2023; Rebedea et al., 2023; Kang and Li,
2024) has leveraged pre-trained LLMs, such as
LlaMa (Touvron et al., 2023) and Mistral (Jiang
et al., 2023), to identify safe versus unsafe content,
which have demonstrated promising results in de-
tecting harmful content in English across various
datasets. Yuan et al. (2024) further improves the
base guardrail model with energy-based data gen-
eration and combined the guardrails’ predictions
with kNNs’ predictions. However, previous works
only concentrate on detecting English harmful in-
puts. Since the large-scale training dataset enables
LLMs to handle multiple languages, guardrails and
jailbreaking protections should also be designed to
account for multiple languages.
Recent efforts have focused on understanding how
LLMs manage harmful content in multilingual con-
texts.
Wang et al. (2023) takes existing safety
benchmarks and translates them to different lan-
arXiv:2410.22153v1  [cs.CL]  29 Oct 2024

--- Page 2 ---

guages. However, their focus is limited to the
performance of commercial detection tools within
their datasets. Ye et al. (2023) collects a multi-
lingual moderation dataset from Reddit, covering
high-resource language only. The study shows
that encoder-only classifiers for toxic content can-
not adequately handle rule-specific content mod-
eration. de Wynter et al. (2024) and Jain et al.
(2024) investigate the ability of LLMs can respond
multilingual toxic prompts and assess whether
guardrails effectively filter out toxic inputs and
responses. Jailbreaking prompts aim to bypass the
safeness instructions of LLMs and force LLMs to
distribute sensitive or inappropriate information to
users. Deng et al. (2023) shows that both inten-
tional (append adversarial suffix) or unintentional
multilingual jailbreaking prompts can elicit unsafe
responses from LLMs. Follow-up work (Yoo et al.,
2024) uses GPT-4 to combine parallel jailbreak-
ing queries in Deng et al. (2023) from different
languages into a single code-switching prompt,
demonstrating that such prompts further increase
the attack success rate compared to monolingual
attacks. Nevertheless, previous evaluation neglects
the potential of guardrails to filter out those harmful
inputs. Our work is the first to systematically in-
vestigate the multilingual capabilities of guardrails
across diverse datasets and languages, as well as
their resilience against multilingual jailbreaking
prompts. Our contribution can be listed as follows:
• We create a comprehensive multilingual test
suite for evaluating guardrails and benchmark
open-source SOTA guardrails on our multilin-
gual toxicity evaluation suite.
• We evaluate the effectiveness of guardrails on
detecting intentional jailbreaking prompts in
multilingual scenarios.
• We additionally analyze the factors such as in-
context policy that impact guardrails’ perfor-
mance on filtering multilingual toxic contents.
Multilingual?
ToxicChat(Lin et al., 2023)
No
AegisSafety (Ghosh et al., 2024)
No
RTP-LX (de Wynter et al., 2024)
Yes
PTP(Jain et al., 2024)
Yes
Moderation (Markov et al., 2022)
No
MultiJail (Deng et al., 2023)
Yes
XSafety (Wang et al., 2023)
Yes
Table 1: Summary of the dataset in our test suite for
evaluating the guardrail models on multilingual inputs.
2
Multilingual Guardrail Test Suite
We first collect a set of content safety/toxicity
dataset as listed in Table 1 for evaluating the perfor-
mance of SOTA guardrails on multilingual safety
moderation across various dataset1. For English
safety dataset such as ToxicChat (Lin et al., 2023),
OpenAI Moderation(Markov et al., 2022), AEGIS
(Ghosh et al., 2024), we translate the test set into
other languages: Chinese, German, Russian, Ara-
bic, Korean, Indonesian, Bengali, and Swahili via
Google Translate API.Following previous paper
Deng et al. (2023), we separate the language into
three groups: high-resource group (ZH, DE, and
RU); medium-resource group (AR, KO, and ID);
and low-resource group ( BN and SW), according
to the data distribution in CommonCrawl Corpus2.
3
Benchmarking Guardrail Models on
Multilingual Prompts
In this section, we want to answer the following
questions: 1. How can guardrails be generalized
to moderate toxic content from different sources? 2.
How effective are the guardrails when dealing with
various multilingual prompts? E.g., Can guardrail
defend multilingual jailbreaking prompts?
We aim to benchmark the latest off-the-shelf
guardrails using light decoder-only pre-trained lan-
guage models on our multilingual toxicity test suite
to answer those questions. Here are the guardrails
we evaluated in our experiments:
• LlaMa-Guard-3, a safety classifier fine-tuned
on LlaMa-3.1-8B, supporting multilingual
data.
• LlaMa-Guard-2, a safety classifier fine-tuned
on LlaMa-3-7B.
• Aegis-Defensive (Ghosh et al., 2024), which
is fine-tuned LlaMa-Guard on Aegis dataset.
• MD-Judge (Li et al., 2024), a safety classifier
fine-tuned on Mistral 7B (Jiang et al., 2023).
In our experiments, we report the F1 score of
this binary classification problem (safe/unsafe),
and Table 2 shows the result of different models
on various multilingual toxicity dataset. Figure 2
shows the performance across different languages
on Aegis dataset. We observe a consistent perfor-
mance drop for all guardrails on non-English data,
indicating that these guardrails are less effective in
1See details of the test suite in Appendix A.2
2https://commoncrawl.github.io/
cc-crawl-statistics/plots/languages.html

--- Page 3 ---

F1 Score
Moderation
Aegis
Toxicchat
RTP_LX
XSafety
En
Mul
En
Mul
En
Mul
En
Mul
En
Mul
Aegis-Defensive
66.75
56.40
84.95
78.95
63.83
43.93
86.89
86.59
67.61
73.12
MD-Judge
76.8
67.03
84.62
35.30
81.05
47.40
92.13
43.14
58.62
28.54
LlaMa-Guard-2
75.88
73.54
59.81
55.91
42.14
33.56
40.33
35.80
35.80
32.93
LlaMa-Guard-3
78.21
74.23
68.82
63.66
46.29
42.17
49.4
45.30
42.65
39.38
Table 2: Benchmarking the performance of guardrails on our test suite. Here we report the F1 score for classifying
user prompt safety. En and Mul denotes the performance of English and the non-English, respectively. Number in
bold and underline highlights the best and the second-best performance across different models, respectively.
handling multilingual harmful inputs. Additionally,
although MD-Judge has a better performance on
English across different datasets, its performance
on multilingual inputs is low. Also, for the XSafety
dataset, we observe that the Aegis-Defensive model
performs better on non-English data compared to
English data. As illustrated in Figure 3, the model
exhibits a high False Positive Rate (FPR) on low-
resource languages, suggesting a tendency to overly
misclassify non-English prompts as unsafe inputs.
Since the XSafety dataset exclusively contains in-
puts with safety issues, this may explain the ob-
served inconsistency in performance.
Figure 2: F1 score of different models on Aegis dataset
across different languages.
To answer question 2, we investigate the poten-
tial of using guardrails to detect the multilingual
jailbreaking prompts. We used the the existing mul-
tilingual jailbreaking dataset, MultiJail (Deng et al.,
2023), and additionally evaluate extension of Mul-
tijail based on code-switching (CSRT) as proposed
in (Yoo et al., 2024). As shown in Table 3 and Fig-
ure 4, we observe that the code-switching prompts
causes significant drop on guardrails’ performance.
MultiJail (Deng et al., 2023) discusses the inten-
tional jailbreaking attacks which prepend a mali-
cious English instruction to the multilingual harm-
ful prompts in MultiJail and shows that this inten-
tional attacks further increase the attack success
Figure 3: False Positive Rate of different models on
Aegis dataset across different languages.
F1 Score
En
Mul
CSRT
Aegis-Defensive
94.47
83.76
86.28
MD-Judge
92.31
37.05
49.64
LlaMa-Guard-2
75.25
62.66
62.75
LlaMa-Guard-3
80.23
76.70
75.25
Table 3: The performance of guardrails on multilingual
jailbreaking prompts including their code-switching
variants. En denotes the English jailbreaking prompts,
Mul denotes the non-English prompts, CSRT denotes
the code-switching jailbreaking prompts.
Figure 4: F1 Score of different models on Multijail
dataset across different languages.
rate. As shown in Table 4, the results indicate
that two guardrails nearly perfect categorize the

--- Page 4 ---

concatenation of multilingual prompts and English
malicious instructions as harmful inputs. To further
evaluate their robustness with multilingual instruc-
tions, we extended the recent English jailbreaking
attack, AutoDAN (Liu et al., 2024), to a multi-
lingual version, generating multilingual malicious
instructions for the multilingual harmful prompts
in the MultiJail dataset. The performance of the
guardrails, as shown in Table 4, drops when han-
dling these multilingual instructions, highlighting
their vulnerabilities3.
F1 Score
En
Mul
AutoDAN
Aegis-Defensive
99.20
100.0
72.65
MD-Judge
100.0
99.57
13.17
LlaMa-Guard-2
64.22
51.14
40.0
LlaMa-Guard-3
82.90
71.38
67.96
Table 4: The performance of guardrails on intentional
multilingual jailbreaking prompts. En denotes the En-
glish intentional jailbreaking prompts, Mul denotes the
non-English intentional prompts (English malicious in-
structions + multilingual jailbreaking prompts), Auto-
DAN denotes the multilingual intentional prompts from
AutoDAN (multilingual malicious instructions + multi-
lingual jailbreaking prompts).
4
Discussions
Here we present additional analysis on the effec-
tiveness of guardrails on multilingual data from the
perspective of in-context safety policy, and the re-
lationship between toxicity detection performance
and the language resource availability.
4.1
The impact of safe guidelines
Our goal is to investigate whether including the de-
tailed guidelines of unsafe categories can enhance
the performance of guardrails in zero-shot setting
(Inan et al., 2023). In our experiments, we aim
to investigate the impact of the policies defined
in the prompt to guardrails. We consider the pol-
icy which the guardrail is fine-tuned as the default
policy (Def), and the dataset specific policy as the
customized policy (Cus). Given the results in Table
5, we observe that the dataset-specific in-context
policy improves the toxicity detection performance,
indicating that the customized policy is necessary
for multilingual unsafe content detection.
4.2
The impact of resource availability
In this section, we analyze the relationship between
resource availability for different languages and de-
3The example of different types of multilingual jailbreak-
ing prompts are in Appendix A.3.
Moderation
En
Mul
Def
Cus
Def
Cus
Aegis-Defensive
66.75
69.33
56.4
60.66
MD-Judge
76.8
80.59
67.03
63.56
LlaMa-Guard-2
75.88
81.31
73.54
77.99
LlaMa-Guard-3
78.21
80.89
74.23
76.55
RTP_LX
En
Mul
Def
Cus
Def
Cus
Aegis-Defensive
86.89
85.63
86.59
88.28
MD-Judge
92.13
92.91
43.14
50.19
LlaMa-Guard-2
40.33
53.26
35.8
51.75
LlaMa-Guard-3
49.4
60.17
45.30
50.19
Table 5: Comparison of impact of different in-context
policy on multilingual toxicity detection. "Def Policy"
refers to the results under the default policy, while "Cus
Policy" refers to the customized policy.
En
High
Medium
Low
Aegis
84.95
82.63
77.92
66.69
Moderation
69.33
63.90
61.01
52.18
Toxicchat
63.83
53.70
45
23.08
Table 6: Comparison of safeness detection performance
(F1 score) across high-, medium-, and low-resource
languages on various datasets. The evaluated guardrail
is the Aegis-Defensive model.
tection performance across various datasets. From
Table 6, we notice the performance of guardrails
decreases as the language resource availability de-
creases. This suggests that resource availability sig-
nificantly influences the ability for the guardrails
to defend against multilingual toxic inputs.
5
Conclusion
In this study, we introduce a comprehensive test
suite designed to evaluate the effectiveness of
decoder-only based guardrail for detecting harm-
ful inputs/contents in multilingual scenarios and to
benchmark the performance of the latest decoder-
based guardrails. Our evaluation shows that the cur-
rent guardrails still lack of abilities to detect multi-
lingual toxic inputs. We additionally demonstrate
that the guardrails are susceptible to the jailbreak-
ing prompts. Our analysis investigates different
factors that influence the guardrails’ effectiveness
and show that 1) customized policy is helpful when
adapting guardrails to the specific safety taxon-
omy 2) language resource availability influences
guardrails’ performance. We believe that this work
is a critical fundamental step towards the practical
deployment of LLMs in multilingual environments.

--- Page 5 ---

Limitations
Our experiments only focus on open-source
guardrails because of their flexibility and cost. The
language coverage in our test suite remains limited,
and the translation rely solely on Google Translate
API. This may lead to inaccuracies and misalign-
ment with human perception.
Ethical Statement
Our work aims to investigate the potential of off-
the-shelf guardrails for filtering unsafe prompts in
multilingual scenarios. We hope our work can ac-
celerate building a more safe unified LLM system
for multilingual users.
References
Maksym Andriushchenko, Francesco Croce, and Nico-
las Flammarion. 2024. Jailbreaking leading safety-
aligned llms with simple adaptive attacks. arXiv
preprint arXiv:2404.02151.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, et al. 2020. Language models are few-shot
learners. Advances in neural information processing
systems, 33:1877–1901.
Patrick Chao, Alexander Robey, Edgar Dobriban,
Hamed Hassani, George J Pappas, and Eric Wong.
2023. Jailbreaking black box large language models
in twenty queries. arXiv preprint arXiv:2310.08419.
Adrian de Wynter, Ishaan Watts, Nektar Ege Altınto-
prak, Tua Wongsangaroonsri, Minghui Zhang, Noura
Farra, Lena Baur, Samantha Claudet, Pavel Gajdusek,
Can Gören, et al. 2024. Rtp-lx: Can llms evaluate
toxicity in multilingual scenarios? arXiv preprint
arXiv:2404.14397.
Yue Deng, Wenxuan Zhang, Sinno Jialin Pan, and Li-
dong Bing. 2023. Multilingual jailbreak challenges
in large language models. In The Twelfth Interna-
tional Conference on Learning Representations.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. BERT: Pre-training of
deep bidirectional transformers for language under-
standing. In Proceedings of the 2019 Conference of
the North American Chapter of the Association for
Computational Linguistics: Human Language Tech-
nologies, Volume 1 (Long and Short Papers), pages
4171–4186, Minneapolis, Minnesota. Association for
Computational Linguistics.
Yi Dong, Ronghui Mu, Gaojie Jin, Yi Qi, Jinwei Hu,
Xingyu Zhao, Jie Meng, Wenjie Ruan, and Xiaowei
Huang. 2024. Building guardrails for large language
models. arXiv preprint arXiv:2402.01822.
Shaona Ghosh, Prasoon Varshney, Erick Galinkin, and
Christopher Parisien. 2024. Aegis: Online adaptive
ai content safety moderation with ensemble of llm
experts. arXiv preprint arXiv:2404.05993.
Hakan Inan, Kartikeya Upasani, Jianfeng Chi, Rashi
Rungta,
Krithika Iyer,
Yuning Mao,
Michael
Tontchev, Qing Hu, Brian Fuller, Davide Testuggine,
et al. 2023. Llama guard: Llm-based input-output
safeguard for human-ai conversations. arXiv preprint
arXiv:2312.06674.
Devansh Jain, Priyanshu Kumar, Samuel Gehman,
Xuhui Zhou, Thomas Hartvigsen, and Maarten Sap.
2024. Polyglotoxicityprompts: Multilingual evalua-
tion of neural toxic degeneration in large language
models. Preprint, arXiv:2405.09373.
Jiaming Ji, Mickel Liu, Josef Dai, Xuehai Pan, Chi
Zhang, Ce Bian, Boyuan Chen, Ruiyang Sun, Yizhou
Wang, and Yaodong Yang. 2023. Beavertails: To-
wards improved safety alignment of llm via a human-
preference dataset. In Advances in Neural Informa-
tion Processing Systems, volume 36, pages 24678–
24704. Curran Associates, Inc.
Albert Q Jiang, Alexandre Sablayrolles, Arthur Men-
sch, Chris Bamford, Devendra Singh Chaplot, Diego
de las Casas, Florian Bressand, Gianna Lengyel, Guil-
laume Lample, Lucile Saulnier, et al. 2023. Mistral
7b. arXiv preprint arXiv:2310.06825.
Mintong Kang and Bo Li. 2024.
r2-guard:
Ro-
bust reasoning enabled llm guardrail via knowledge-
enhanced logical reasoning.
arXiv preprint
arXiv:2407.05557.
Keita Kurita, Anna Belova, and Antonios Anastasopou-
los. 2019. Towards robust toxic content classification.
arXiv preprint arXiv:1912.06872.
Lijun Li, Bowen Dong, Ruohui Wang, Xuhao Hu, Wang-
meng Zuo, Dahua Lin, Yu Qiao, and Jing Shao.
2024. Salad-bench: A hierarchical and comprehen-
sive safety benchmark for large language models.
arXiv preprint arXiv:2402.05044.
Zi Lin, Zihan Wang, Yongqi Tong, Yangkun Wang,
Yuxin Guo, Yujia Wang, and Jingbo Shang. 2023.
Toxicchat: Unveiling hidden challenges of toxicity
detection in real-world user-ai conversation. In Find-
ings of the Association for Computational Linguistics:
EMNLP 2023, pages 4694–4702.
Xiaogeng Liu, Nan Xu, Muhao Chen, and Chaowei
Xiao. 2024. Autodan: Generating stealthy jailbreak
prompts on aligned large language models. In The
Twelfth International Conference on Learning Repre-
sentations.
Todor Markov, Chong Zhang, Sandhini Agarwal, Tyna
Eloundou, Teddy Lee, Steven Adler, Angela Jiang,
and Lilian Weng. 2022.
A holistic approach
to undesired content detection.
arXiv preprint
arXiv:2208.03274.

--- Page 6 ---

Shana Poplack. 2001. Code-switching (linguistic). In
Neil J. Smelser and Paul B. Baltes, editors, Inter-
national Encyclopedia of the Social and Behavioral
Sciences, pages 2062–2065. Elsevier.
Traian Rebedea, Razvan Dinu, Makesh Narsimhan
Sreedhar, Christopher Parisien, and Jonathan Cohen.
2023. NeMo guardrails: A toolkit for controllable
and safe LLM applications with programmable rails.
In Proceedings of the 2023 Conference on Empirical
Methods in Natural Language Processing: System
Demonstrations, pages 431–445, Singapore. Associa-
tion for Computational Linguistics.
Paul Röttger, Haitham Seelawi, Debora Nozza, Zeerak
Talat, and Bertie Vidgen. 2022. Multilingual Hate-
Check: Functional tests for multilingual hate speech
detection models. In Proceedings of the Sixth Work-
shop on Online Abuse and Harms (WOAH), pages
154–169, Seattle, Washington (Hybrid). Association
for Computational Linguistics.
Lukas Stappen, Fabian Brunn, and Björn Schuller. 2020.
Cross-lingual zero-and few-shot hate speech detec-
tion utilising frozen transformer language models and
axel. arXiv preprint arXiv:2004.13850.
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier
Martinet, Marie-Anne Lachaux, Timothée Lacroix,
Baptiste Rozière, Naman Goyal, Eric Hambro,
Faisal Azhar, et al. 2023. Llama: Open and effi-
cient foundation language models. arXiv preprint
arXiv:2302.13971.
Wenxuan Wang, Zhaopeng Tu, Chang Chen, Youliang
Yuan, Jen-tse Huang, Wenxiang Jiao, and Michael R
Lyu. 2023. All languages matter: On the multilin-
gual safety of large language models. arXiv preprint
arXiv:2310.00905.
Thomas Wolf, Lysandre Debut, Victor Sanh, Julien
Chaumond, Clement Delangue, Anthony Moi, Pier-
ric Cistac, Tim Rault, Rémi Louf, Morgan Funtowicz,
Joe Davison, Sam Shleifer, Patrick von Platen, Clara
Ma, Yacine Jernite, Julien Plu, Canwen Xu, Teven Le
Scao, Sylvain Gugger, Mariama Drame, Quentin
Lhoest, and Alexander M. Rush. 2020. Transform-
ers: State-of-the-art natural language processing. In
Proceedings of the 2020 Conference on Empirical
Methods in Natural Language Processing: System
Demonstrations, pages 38–45, Online. Association
for Computational Linguistics.
Meng Ye, Karan Sikka, Katherine Atwell, Sabit Hassan,
Ajay Divakaran, and Malihe Alikhani. 2023. Multi-
lingual content moderation: A case study on reddit.
arXiv preprint arXiv:2302.09618.
Haneul Yoo, Yongjin Yang, and Hwaran Lee. 2024.
Csrt: Evaluation and analysis of llms using code-
switching red-teaming dataset.
arXiv preprint
arXiv:2406.15481.
Zhuowen Yuan, Zidi Xiong, Yi Zeng, Ning Yu, Ruoxi
Jia, Dawn Song, and Bo Li. 2024. Rigorllm: Re-
silient guardrails for large language models against
undesired content. arXiv preprint arXiv:2403.13031.
A
Appendix
A.1
Experimental Setup
We used the Huggingface framework (Wolf et al.,
2020) to load dataset and evaluate the guardrails
and applied the default greedy decoding for
decoder-based guardrails. For generating jailbreak-
ing prompts using AutoDAN(Liu et al., 2024), we
use Google Translate API to translate the English
prototype prompts in other languages and utilize
the proposed genetic algorithm in their official im-
plementation. The victim model is LlaMa-3.1-8B-
Instruct. We use 2 NVIDIA RTX-A6000 to run all
our experiments. Additionally, all the datasets and
artifacts we used are consistent with their intended
usages. We use ChatGPT for correcting grammars
and short-form paraphrasing.
A.2
Details of the Test Suite
The test suite contains seven different datasets:
Aegis, Toxicchat, Moderation, RTP_LX, PTP, Mul-
tiJail, XSafety. For Toxicchat, we only translate
subset of it. For PTP, we only use the small split
of a subset of languages. For different datasets, we
give the list of languages and the stats in Table 7.
A.3
Example Multilingual Jailbreaking
Prompts
We present examples of the prompt variations de-
rived from MultiJail, as discussed in Section 3.
A.4
Additional Results
Here we present results of additional dataset across
different languages in Figure 6 , 7, and 8.
A.5
Code-switching Jailbreaking Prompts
Code-switching is a phenomenon in which a multi-
lingual speaker alternates between two or more
languages within an utterance (Poplack, 2001).
It is generally recognized as an advanced abil-
ity, as it demonstrates a person can master mul-
tiple languages simultaneously. Here, we generate
the code-switching prompt for English data with
other languages using LLMs. Different from (Yoo
et al., 2024), we only mixed one language with
English. Specifically, we crafted in-context learn-
ing code-switching examples by human and use
gpt-3.5-turbo. The prompts is listed in Figure 9.
The results presented in Figure 10 and 11
demonstrate that code-switching inputs confuse
the guardrails, resulting in a decrement of detec-
tion performance. Additionally, we observe that

--- Page 7 ---

Multilingual?
Lang
Size
ToxicChat
No
AR,BN,DE,RU,ID,KO,SW,ZH
1000
AegisSafety
No
AR,BN,DE,RU,ID,KO,SW,ZH
1199
Moderation
No
AR,BN,DE,RU,ID,KO,SW,ZH
1680
RTP-LX
Yes
AR,DE,ES,FI,FR,HI,ID,IT,JA,KO,RU,SW,TH,TR,ZH-Hans
999
PTP-LX
Yes
DE, FR, IT, JA, KO, RU, ZH
5000
MultiJail
Yes
AR, IT, JV, KO, SW, TH, VI, ZH, BN
315
XSafety
Yes
AR, BN, DE, EN, FR, HI, JA, RU, SP, ZH
2800
Table 7: Details of the dataset included in our test suite for evaluating the guardrail models on multilingual content.
If is not multilingual dataset, then we translate the English dataset into different languages. The size is the size of
the English data.
Figure 5: Examples of different multilingual jailbreaking prompts we evaluted in our experiments. (Top rorw is for
IT, and bottom row is for KO.)
Figure 6: Performance of different models on RTP_LX
dataset.
the performance drop more for low-resource lan-
guages such as BN, JV, and SW compared to other
languages. For both dataset, the Aegis-Defensive
model is the most robust against code-switching
Figure 7: Performance of different models on Toxicchat
dataset.
inputs.

--- Page 8 ---

Figure 8: Performance of different models on PTP
dataset. Note that PTP dataset is not a parallel dataset.
Figure 9: Use LLMs to generate code-switching jail-
breaking prompts.
Figure 10: Performance of different models on Code-
switched MultiJail dataset.
Figure 11: Performance of different models on Code-
switched Aegis dataset.

```
