---
title: "2023-Kohli-Building a Llama2-finetuned LLM for Odia Language Utilizing Domain - PDF Extract"
source_pdf: "2023-Kohli-Building a Llama2-finetuned LLM for Odia Language Utilizing Domain.pdf"
pages: 7
extracted_at: "2026-02-13T17:43:16.609283"
---

# PDF Extract: 2023-Kohli-Building a Llama2-finetuned LLM for Odia Language Utilizing Domain

**Source PDF:** 2023-Kohli-Building a Llama2-finetuned LLM for Odia Language Utilizing Domain.pdf
**Total Pages:** 7

---

## Content

```
--- Page 1 ---

Building a Llama2-finetuned LLM for Odia Language Utilizing Domain
Knowledge Instruction Set
GUNEET SINGH KOHLI, Thapar University, India
SHANTIPRIYA PARIDA, Silo AI, Finland
SAMBIT SHEKHAR, Odia Generative AI, India
SAMIRIT SAHA∗and NIPUN B NAIR∗, Amrita Vishwa Vidyapeetham, India
PARUL AGARWAL, Institute of Mathematics and Applications, India
SONAL KHOSLA, Odia Generative AI, India
KUSUMLATA PATIYAL, Sharda University, India
DEBASISH DHAL, NISER Bhubaneswar, India
Building LLMs for languages other than English is in great demand due to the
unavailability and performance of multilingual LLMs, such as understanding
the local context. The problem is critical for low-resource languages due to
the need for instruction sets. In a multilingual country like India, there is
a need for LLMs supporting Indic languages to provide generative AI and
LLM-based technologies and services to its citizens.
This paper presents our approach of i) generating a large Odia instruction
set, including domain knowledge data suitable for LLM fine-tuning, and ii)
building a Llama2-finetuned model tailored for enhanced performance in
the Odia domain.
The proposed work will help researchers build an instruction set and LLM,
particularly for Indic languages. We will release the model and instruction
set for the public for research and noncommercial purposes.
CCS Concepts: • Computing methodologies →Natural language gen-
eration.
Additional Key Words and Phrases: Llama2, Llama1, Fine Tuning, Natural
Language Processing, Odia, Generative AI, Large Language Models
ACM Reference Format:
Guneet Singh Kohli, Shantipriya Parida, Sambit Shekhar,
Samirit Saha, Nipun B Nair, Parul Agarwal, Sonal Khosla,
Kusumlata Patiyal, and Debasish Dhal. 2018. Building a Llama2-
finetuned LLM for Odia Language Utilizing Domain Knowledge Instruc-
tion Set. In Woodstock ’18: ACM Symposium on Neural Gaze Detection, June
03–05, 2018, Woodstock, NY. ACM, New York, NY, USA, 7 pages. https:
//doi.org/XXXXXXX.XXXXXXX
1
INTRODUCTION
In the ever-evolving landscape of Generative AI, language models
have played a pivotal role in revolutionizing how we interact with
and understand the world’s diverse linguistic tapestry. These models
have demonstrated remarkable capabilities, from the groundbreak-
ing BERT [5] to the omnipotent GPT, particularly in widely spoken
languages. However, the realm of Generative AI is not one-size-fits-
all, and the inadequacy of state-of-the-art models when applied to
∗Both authors contributed equally to this research.
Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
© 2018 Association for Computing Machinery.
This is the author’s version of the work. It is posted here for your personal use. Not
for redistribution. The definitive Version of Record was published in Woodstock ’18:
ACM Symposium on Neural Gaze Detection, June 03–05, 2018, Woodstock, NY, https:
//doi.org/XXXXXXX.XXXXXXX.
less-resourced languages, especially those belonging to the Indic
language family, remains an unsettling challenge.
The multilingual landscape of NLP has witnessed significant ad-
vancements in recent years, with several models tailored to support
a myriad of languages. However, a noticeable gap in the digital
representation persists when it comes to providing comprehensive
support for Indic languages, including Odia. This gap fuels our dedi-
cation to the cause – empowering the Odia language through robust
and dedicated language models.
Odia, an Indic language spoken predominantly in the Indian state
of Odisha, boasts a rich cultural heritage and a growing digital pres-
ence. However, it has long been underserved in the digital sphere,
and the need to empower it through enhanced language represen-
tation has never been more pressing [14]. Although only some
multilingual LLMs support the Odia language due to the amount
and quality of data, the performance of these LLMs could be better,
as shown in Fig. 1.
Fig. 1. The queries to ChatGPT3.5 about preparing the famous Odia sweet:
Rasgulla. The answer from ChatGPT3.5 is not relevant and noisy.
In this paper, we embark on a journey to introduce the Llama2-
finetuned language model meticulously tuned to cater to the specific
requirements of the Odia language. Llama2 [20] proudly stands
as a member of a burgeoning family of models, poised to bridge
the multilingual gap by providing precise, contextually relevant
results for Odia while championing linguistic diversity in the NLP
landscape.
1
arXiv:2312.12624v1  [cs.CL]  19 Dec 2023

--- Page 2 ---

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
Kohli, et al.
Our motivation transcends the boundaries of linguistic capabili-
ties; it is rooted in the broader mission of preserving and promoting
underrepresented languages. Llama2’s development and meticulous
fine-tuning of an extensive Odia domain knowledge dataset serve
not only to enhance its performance but also to contribute to safe-
guarding against potential plagiarism in Odia language research.
The authors aspire to foster innovation and knowledge creation
within the Odia-speaking community by offering researchers a de-
pendable and original language model.
2
DATASET
In the pursuit of empowering the Odia language in the digital sphere,
it is recognized by the team that data forms the bedrock of progress.
To this end, a comprehensive dataset of Llama2, the specialized
language model designed exclusively for Odia, has been meticu-
lously curated and prepared. The dataset encapsulates a wealth of
linguistic diversity, domain-specific knowledge, and an expansive
coverage of the Odia language landscape. The dataset is a versatile
repository that encompasses two distinct types of data.
Translated Instruction Set: This dataset segment is a testament
to the team’s commitment to linguistic diversity. A curated collec-
tion of translated instructions covering a wide range of topics and
contexts is encompassed by it. The data was obtained from vari-
ous internet sources, primarily blogs and Wikipedia. They were
translated using the Indic Trans library under the supervision of
colloquial speakers of the Odia language, who edited any discrep-
ancies manually. These instructions serve as valuable training data
for Llama2, enabling it to understand and generate Odia text that
remains faithful to the nuances and subtleties of the language.
Domain Knowledge: The necessary expertise to navigate Odia’s
unique linguistic intricacies has been equipped to Llama2 by in-
corporating domain knowledge into the dataset. This knowledge
is wide-ranging and deeply rooted in Odia’s culture, history, and
contemporary context. The power of sources such as Wikipedia and
ChatGPT has been harnessed to provide Llama2 with a rich under-
standing of Odia, enhancing its capacity to generate contextually
relevant and culturally sensitive content.
The instructions cover a wide array of subjects, ranging from the
culinary delights in RECIPES, the historical significance of HISTORI-
CAL PLACES, and TEMPLES OF ODISHA, to the intellectual pursuits
in ARITHMETIC, HEALTH, and GEOGRAPHY. It also explores the
artistic tapestry of Odisha through ART AND CULTURE, which cel-
ebrates renowned figures in FAMOUS ODIA POETS/WRITERS, and
FAMOUS ODIA POLITICAL LEADERS. Furthermore, it encapsulates
SPORTS and the GENERAL KNOWLEDGE OF ODISHA, providing an
all-encompassing representation of the state. These instructions re-
flect Odisha’s rich heritage and are a practical and engaging resource
for building a conversational AI that resonates with the region’s
people.
The dataset contains 181K Odia instruction sets [15]. The instruc-
tion sets include:
• Odia domain knowledge instruction set prepared using vari-
ous domain knowledge sources utilizing GPT models.
• Translating popular instruction sets (Alpaca [19], Dolly1, GPT
Teacher 2) from English to Odia using the IndicTrans3 ma-
chine translation library from AI4Bharat [16].
• Preparing translation instruction set using OdiEnCorp [13],
English-Odia parallel corpus.
• Hard-coded instruction set.
The statistics of the dataset are shown in Table 1.
Dataset
Size
Odia Domain_Context
10.5k
Alpaca
52k
Dolly
15k
GPT teacher role-play
3k
GPT teacher instruct
18k
Hard code Q&A
105
Table 1. Details of the data used in the instruction fine-tuning stage.
3
EXPERIMENTAL SETUP
3.1
Fine-Tuning
We used the Llama2-7b 4 which has 4k context length as our base
model for fine-tuning. A deliberate and balanced approach was
undertaken to optimize efficiency and performance in configuring
our model’s parameters. Employing a batch size of 128 strikes a
harmonious equilibrium, allowing the processing of 128 data sam-
ples concurrently while efficiently managing memory resources. A
learning rate of 2𝑒−4 was selected, signifying an informed choice
that facilitates model convergence without the risk of overshooting
[10]. The decision to train the model for seven epochs harnesses the
power of iterative learning, enabling it to refine its understanding
of the data progressively. To ensure streamlined processing, we
imposed a cutoff length of 256, which efficiently manages computa-
tional resources for handling input sequences. A weight decay factor
of 0.001 strikes a careful balance, enhancing generalization without
imposing undue constraints on the model’s flexibility [7]. A warmup
ratio of 0.03 in the learning rate schedule adds training stability by
gradually increasing the learning rate during early iterations.
Setting a maximum sequence length of 512 accommodates the
complexities of capturing context in NLP tasks. Adopting a linear
learning rate scheduler initially promotes faster convergence with
a higher learning rate [22]. Fine-tuning attention mechanisms with
LoRA (Learnable Reordering Attention) parameters [9], such as
LoRA r (64) and LoRA 𝛼(16), refines the model’s attention opera-
tions. A dropout rate of 0.1 introduces a measured dropout level,
mitigating overfitting risks. Leveraging 4-bit quantization optimizes
memory and computational efficiency without compromising per-
formance [23]. Setting the compute data type to “float16" further
balances precision and computational speed. While nested quanti-
zation, although not utilized in this instance, represents a potential
avenue for additional efficiency gains. Batch size 48 for training and
1https://huggingface.co/datasets/databricks/databricks-dolly-15k
2https://github.com/teknium1/GPTeacher
3https://github.com/AI4Bharat/indicTrans
4https://huggingface.co/meta-llama/Llama-2-7b
2

--- Page 3 ---

Building a Llama2-finetuned LLM for Odia Language Utilizing Domain Knowledge Instruction Set
Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
evaluation meticulously manages memory and training stability [3].
The accumulation of gradients over a single update step enhances
stability without necessitating additional memory.
A maximum gradient norm of 0.3 safeguards against unstable
training by preventing gradient explosions [1]. Employing the “Paged
AdamW 32-bit" optimizer signifies a specialized adaptation for 32-
bit computations, enhancing training efficiency [4]. The selection
of a constant learning rate schedule ensures steady learning rate
values conducive to convergence. Lastly, attention operations are
finely tuned by targeting specific projection modules (q_proj, k_proj,
v_proj, o_proj) with LoRA attention, potentially elevating perfor-
mance in those particular model areas. This holistic parameter con-
figuration approach harmonizes computational resource manage-
ment and model effectiveness in our research endeavor.
3.2
TRAINING
The training environment has been trained on NVIDIA A-100 PCI
Express, 40 GB single core because PCI Express boasts exceptional
computational power, enabling it to handle the complex mathemati-
cal operations required during the training of deep neural networks,
such as the Llama2 model [6]. Its advanced architecture allows for
rapid parallel processing, significantly accelerating model training.
The model completed its first training in approx 2.5 days. The train-
ing hyperparameters are shown in Table 2.
Hyper Parameter
Value
Batch Size
128
Learning Rate
2𝑒−4
Epochs
7
Cutoff Length
256
Weight_Decay
0.001
Warmup_Ratio
0.03
max_seq_length
512
LR_Scheduler
linear
Lora r
64
Lora 𝛼
16
Lora dropout
0.1
use_4bit
True
bnb_4bit_compute_dtype
“float16"
bnb_4bit_quant_type
“nf4"
use_nested_quant
False
per_device_train_batch_size
48
per_device_eval_batch_size
48
gradient_accumulation_steps
1
max_grad_norm
0.3
optim
“paged_adamw_32bit"
lr_scheduler_type
“constant"
Lora Target Modules
(q_proj, k_proj, v_proj, o_proj)
Table 2. Training Hyperparameters.
We visually represent our model’s learning process in the training
section through a loss function graph. The graph showcases the
progression of time steps along the x-axis and the corresponding
loss values on the y-axis. What becomes immediately apparent is
the model’s steady improvement over time, as indicated by the de-
creasing loss values [21]. This trend signifies the model’s ability to
learn and adapt as it refines its task understanding. The data points,
spanning key milestones at 5000, 10000, 15000, 20000, and 25000
time steps, offer concrete evidence of this learning trajectory. The
decreasing loss values at these checkpoints, starting at 0.4311 and
culminating at 0.3143, underscore the model’s continuous refine-
ment, validating its training effectiveness and the progress made
throughout the training process in Fig. 2.
Fig. 2. The Loss graph of the model
4
INFERENCE
The inference script is adapted from Alpaca-LoRA considering the
base model Llama2-7b with the built model weights.
4.1
Text Generation Setup
The decoding process of LLMs plays a critical role in determining
the quality and diversity of the generated text. In our experiments,
we use the following decoding hyperparameters:
• Size of the context: We establish the context size as 2048, deter-
mining the maximum number of tokens that the model can
take into account simultaneously during the text generation
process.
• Maximum sequence length: We impose a constraint on the
generated sequence length, limiting it to 512 tokens to ensure
that the outputs remain focused and closely related to the
input prompt.
• Temperature: We set the temperature to 0.2, regulating the
level of randomness in the sampling process. Lower values
make the model produce more focused and deterministic
outputs, while higher values introduce greater diversity at
the expense of coherence.
• Top-k sampling: For each step, we adopt Top-k sampling with
a value of k = 40, whereby the model selects the subsequent
token from the top 40 most probable options. This introduces
an element of randomness and diversity in the generated text.
• Top-p sampling: We also employ Top-p sampling with a value
of p = 0.9. This further enhances diversity by considering a
dynamic set of tokens that collectively account for 90% of the
probability mass.
• Repetition penalty: To discourage the model from generating
repetitive text, we apply a repetition penalty with a factor of
1.3, penalizing the selection of already chosen tokens.
3

--- Page 4 ---

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
Kohli, et al.
5
EVALUATION
Evaluation metrics like ROUGE and BLEU were used to assess the
quality and performance of the model. ROUGE is a set of metrics
commonly used for evaluating the quality of text summaries [24].
It measures the overlap between the words or n-grams (sequences
of words) in the generated text and the reference text. ROUGE is
widely used to evaluate machine-generated summaries, machine
translation, and text-generation tasks. BLEU is designed to assess the
adequacy of translations by comparing them to human-generated
reference translations. BLEU is a standard metric in machine trans-
lation evaluation [17]. We used 280 samples to calculate the BLEU
score and the ROUGE score. The BLEU score was 0.6158, and the
ROUGE score was 0.6583. The evaluation scores are shown in Table
3.
Evaluation metric
Score
ROUGE
0.6583
BLEU
0.6158
Table 3. Automatic Evaluation Scores.
5.1
HUMAN EVALUATION
The human evaluation process is a crucial and multifaceted element
in assessing the Odia generative model’s performance, adhering
to stringent ethical guidelines and user safety concerns. Trained
evaluators, possessing expertise in linguistics and a profound under-
standing of the Odia language, play pivotal roles in this assessment.
Apart from automatic evaluation, we performed a human assess-
ment of the model by the native Odia speakers by asking subjective
questions to verify model generative performance and toxicity. We
did our analysis on the basis of three metrics: readability, perplexity,
and correctness. A graphical analysis of the average is presented in
Fig. 3.
Three critical metrics often take center stage in text analysis and
natural language processing: Readability, Perplexity, and Correct-
ness. Readability, a measure of how easily a text can be compre-
hended by its intended audience, is pivotal in ensuring clarity and
accessibility in written communication [12]. On the other hand,
Perplexity is a crucial gauge for assessing the quality of language
models, quantifying their predictive accuracy and understanding of
language patterns. Lower perplexity values indicate more proficient
models. Lastly, Correctness evaluates the accuracy and fidelity of
information within the textual content, measuring alignment with
factual accuracy and adherence to linguistic rules [11]. These met-
rics, collectively, empower professionals in fields such as journalism,
linguistics, and artificial intelligence to enhance the quality, and
reliability of textual content, ultimately advancing the capabilities
of language models and text-based applications [2].
6
ANALYSIS AND DISCUSSION
Our model demonstrated strong performance in arithmetic-related
questions, showcasing its ability to provide accurate and concise
answers in this domain. The model performs quite well at toxicity,
in fact, it prefers using the formal honorific. The model has a good
Fig. 3. The score for human evaluation metrics
understanding of the grammar of the Odia language and it is able to
identify grammatical elements from a given piece of text. However,
in the context of classification tasks, we observed limitations. It
struggled to effectively distinguish between different classes and
often defaulted to providing explanations of the question rather
than assigning classifications.
Furthermore, one noteworthy limitation we encountered was re-
lated to the response length. When tasked with generating long an-
swers or explanations, the model faced challenges due to constraints
imposed by the maximum token size. This limitation impacted the
model’s ability to provide comprehensive and detailed responses in
scenarios where lengthy explanations were required.
These observations underscore the need for further research and
potential model enhancements to address these specific limitations,
particularly in the context of classification tasks and extended re-
sponses.
7
LIMITATION
Based on the evaluation, we observed the below issues and limita-
tions with the model.
• The model still suffers from hallucinations, particularly for
long answers. Item Still needs to be able to follow arithmetic
problems and critical reasoning.
• Still answers incorrectly sometimes for the questions related
to Odisha, although the model is explicitly trained, including
the domain knowledge instruction set.
• The model often produces additional unnecessary text, after
producing the correct answer. The model is not performing
well when it comes to generalization and summarizing.
• Under certain circumstances, the model produces insufficient
or no output at all. This is especially true when it comes to
arithmetic or when the response is supposed to be big.
8
CONCLUSION
This paper presented a Llama2-finetuned LLM for the low-resource
Odia language using a prepared instruction set containing domain
knowledge. Several parameters and techniques were employed to
optimize the model’s efficiency and performance. These included
batch size selection, learning rate, training epochs, sequence length,
weight decay, warmup ratio, attention mechanisms with LoRA
4

--- Page 5 ---

Building a Llama2-finetuned LLM for Odia Language Utilizing Domain Knowledge Instruction Set
Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
parameters, dropout rate, quantization, gradient norm, optimizer
choice, and specific projection module targeting. This comprehen-
sive parameter configuration balanced computational resource man-
agement and model effectiveness for the research endeavor. The
future work includes i) investigate model limitations ii) to perform
an in-depth comparison study of the proposed model with the avail-
able multilingual LLMs supporting Odia, iii) Exploring distilling
step-by-step approach [8] for build smaller model for comparative
analysis, iv) Release pre-train Odia LLM model following BLOOM
[18] specification.
ETHICS STATEMENT
We do not envisage any ethical concerns. The dataset does not contain any
personal or personally identifiable information, the source data is already
open source, and there are no risks or harm associated with its usage.
ACKNOWLEDGEMENTS
We are thankful to Silo AI, Helsinki, Finland, and Odia Generative AI,
Bhubaneswar, India for the necessary support.
REFERENCES
[1] Leila Arras, Franziska Horn, Grégoire Montavon, Klaus-Robert Müller, and Woj-
ciech Samek. 2016. Explaining predictions of non-linear classifiers in NLP. arXiv
preprint arXiv:1606.07298 (2016).
[2] Cheng-Han Chiang and Hung-yi Lee. 2023. Can Large Language Models Be an
Alternative to Human Evaluations? arXiv preprint arXiv:2305.01937 (2023).
[3] Hulin Dai, Xuan Peng, Xuanhua Shi, Ligang He, Qian Xiong, and Hai Jin. 2022.
Reveal training performance mystery between TensorFlow and PyTorch in the
single GPU environment. Science China Information Sciences 65 (2022), 1–17.
[4] Tim Dettmers, Mike Lewis, Sam Shleifer, and Luke Zettlemoyer. 2021. 8-bit
optimizers via block-wise quantization. arXiv preprint arXiv:2110.02861 (2021).
[5] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2018. Bert:
Pre-training of deep bidirectional transformers for language understanding. arXiv
preprint arXiv:1810.04805 (2018).
[6] Jiarui Fang, Zilin Zhu, Shenggui Li, Hui Su, Yang Yu, Jie Zhou, and Yang You.
2022. Parallel Training of Pre-Trained Models via Chunk-Based Dynamic Memory
Management. IEEE Transactions on Parallel and Distributed Systems 34, 1 (2022),
304–315.
[7] Boris Ginsburg, Patrice Castonguay, Oleksii Hrinchuk, Oleksii Kuchaiev, Vitaly
Lavrukhin, Ryan Leary, Jason Li, Huyen Nguyen, Yang Zhang, and Jonathan M
Cohen. 2019. Stochastic gradient methods with layer-wise adaptive moments for
training of deep networks. arXiv preprint arXiv:1905.11286 (2019).
[8] Cheng-Yu Hsieh, Chun-Liang Li, Chih-Kuan Yeh, Hootan Nakhost, Yasuhisa Fujii,
Alexander Ratner, Ranjay Krishna, Chen-Yu Lee, and Tomas Pfister. 2023. Distilling
step-by-step! outperforming larger language models with less training data and
smaller model sizes. arXiv preprint arXiv:2305.02301 (2023).
[9] Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean
Wang, Lu Wang, and Weizhu Chen. 2021. Lora: Low-rank adaptation of large
language models. arXiv preprint arXiv:2106.09685 (2021).
[10] Aitor Lewkowycz. 2021.
How to decay your learning rate.
arXiv preprint
arXiv:2103.12682 (2021).
[11] Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah
Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, et al. 2023.
Self-refine: Iterative refinement with self-feedback. arXiv preprint arXiv:2303.17651
(2023).
[12] John Mendonça, Patrícia Pereira, João Paulo Carvalho, Alon Lavie, and Isabel Tran-
coso. 2023. Simple LLM Prompting is State-of-the-Art for Robust and Multilingual
Dialogue Evaluation. arXiv preprint arXiv:2308.16797 (2023).
[13] Shantipriya Parida, Satya Ranjan Dash, Ondřej Bojar, Petr Motlicek, Priyanka
Pattnaik, and Debasish Kumar Mallick. 2020. OdiEnCorp 2.0: Odia-English Parallel
Corpus for Machine Translation. In Proceedings of the WILDRE5– 5th Workshop on
Indian Language Data: Resources and Evaluation. European Language Resources
Association (ELRA), Marseille, France, 14–19.
https://aclanthology.org/2020.
wildre-1.3
[14] Shantipriya Parida, Kalyanamalini Sahoo, Atul Kr Ojha, Saraswati Sahoo,
Satya Ranjan Dash, and Bijayalaxmi Dash. 2022. Universal Dependency Treebank
for Odia Language. arXiv preprint arXiv:2205.11976 (2022).
[15] Shantipriya Parida, Sambit Sekhar, Aisha Asif, Subham Pradhan, Guneet Singh
Kohli, and Swateek Jena. 2023. Large Odia Instruction Set for LlaMA2 Finetuning.
https://huggingface.co/OdiaGenAI.
[16] Gowtham Ramesh, Sumanth Doddapaneni, Aravinth Bheemaraj, Mayank Joban-
putra, Raghavan AK, Ajitesh Sharma, Sujit Sahoo, Harshita Diddee, Maha-
lakshmi J, Divyanshu Kakwani, Navneet Kumar, Aswin Pradeep, Srihari Na-
garaj, Kumar Deepak, Vivek Raghavan, Anoop Kunchukuttan, Pratyush Ku-
mar, and Mitesh Shantadevi Khapra. 2022.
Samanantar: The Largest Pub-
licly Available Parallel Corpora Collection for 11 Indic Languages.
Trans-
actions of the Association for Computational Linguistics 10 (02 2022), 145–
162. https://doi.org/10.1162/tacl_a_00452 arXiv:https://direct.mit.edu/tacl/article-
pdf/doi/10.1162/tacl_a_00452/1987010/tacl_a_00452.pdf
[17] Hadeel Saadany and Constantin Orasan. 2021. BLEU, METEOR, BERTScore: eval-
uation of metrics performance in assessing critical translation errors in sentiment-
oriented text. arXiv preprint arXiv:2109.14250 (2021).
[18] Teven Le Scao, Angela Fan, Christopher Akiki, Ellie Pavlick, Suzana Ilić, Daniel
Hesslow, Roman Castagné, Alexandra Sasha Luccioni, François Yvon, Matthias
Gallé, et al. 2022. Bloom: A 176b-parameter open-access multilingual language
model. arXiv preprint arXiv:2211.05100 (2022).
[19] Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann Dubois, Xuechen Li, Carlos
Guestrin, Percy Liang, and Tatsunori B Hashimoto. 2023. Alpaca: A strong,
replicable instruction-following model. Stanford Center for Research on Foundation
Models. https://crfm. stanford. edu/2023/03/13/alpaca. html 3, 6 (2023), 7.
[20] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine
Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale,
et al. 2023. Llama 2: Open foundation and fine-tuned chat models. arXiv preprint
arXiv:2307.09288 (2023).
[21] Tom Viering and Marco Loog. 2022. The shape of learning curves: a review. IEEE
Transactions on Pattern Analysis and Machine Intelligence (2022).
[22] Zenghui Wang and Jun Zhang. 2022. Incremental PID Controller-Based Learning
Rate Scheduler for Stochastic Gradient Descent. IEEE Transactions on Neural
Networks and Learning Systems (2022).
[23] Xiuying Wei, Yunchen Zhang, Xiangguo Zhang, Ruihao Gong, Shanghang Zhang,
Qi Zhang, Fengwei Yu, and Xianglong Liu. 2022. Outlier suppression: Pushing
the limit of low-bit transformer language models. Advances in Neural Information
Processing Systems 35 (2022), 17402–17414.
[24] S Yashaswini and SS Shylaja. 2021. Metrics for Automatic Evaluation of Text
from NLP Models for Text to Scene Generation. European Journal of Electrical
Engineering and Computer Science 5, 4 (2021), 20–25.
9
APPENDIX
9.1
Comparative Analysis
In our study, we conducted a comprehensive comparison between our model
and ChatGPT 3.5. The results of this comparative analysis are presented in
Figure 4, which encapsulates the key findings of our research. This compari-
son serves as a visual representation of the performance and capabilities of
our model in relation to ChatGPT 3.5.
5

--- Page 6 ---

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
Kohli, et al.
6

--- Page 7 ---

Building a Llama2-finetuned LLM for Odia Language Utilizing Domain Knowledge Instruction Set
Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
Fig. 4. The comparative analysis between our model and ChatGPT 3.5.
7

```
