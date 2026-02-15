---
title: "2024-Qian-CamelEval Advancing Culturally Aligned Arabic Language Models and - PDF Extract"
source_pdf: "2024-Qian-CamelEval Advancing Culturally Aligned Arabic Language Models and.pdf"
pages: 12
extracted_at: "2026-02-15T17:51:57.413281"
---

# PDF Extract: 2024-Qian-CamelEval Advancing Culturally Aligned Arabic Language Models and

**Source PDF:** 2024-Qian-CamelEval Advancing Culturally Aligned Arabic Language Models and.pdf
**Total Pages:** 12

---

## Content

```
--- Page 1 ---

arXiv:2409.12623v2  [cs.CL]  24 Sep 2024
CamelEval: Advancing Culturally Aligned Arabic
Language Models and Benchmarks
Zhaozhi Qian
Elm Company
zqian@elm.sa
Faroq Altam
Elm Company
faltam@elm.sa
Muhammad Alqurishi
Elm Company
mualqurishi@elm.sa
Riad Souissi
Elm Company
rsouissi@elm.sa
Abstract
Large Language Models (LLMs) are the cornerstones of modern artiﬁcial intelli-
gence systems. This paper introduces Juhaina, a Arabic-English bilingual LLM
speciﬁcally designed to align with the values and preferences of Arabic speak-
ers. Juhaina inherently supports advanced functionalities such as instruction fol-
lowing, open-ended question answering, information provisioning, and text pro-
cessing. Our model contains 9.24 billion parameters and is trained on a context
window of up to 8,192 tokens. This paper details the creation process of Juhaina
and provides an extensive empirical evaluation. Furthermore, we identify the lim-
itations of widely-adopted Open Arabic LLM Leaderboard (OALL) and propose
a new evaluation benchmark, CamelEval. Our ﬁndings demonstrate that Juhaina
surpasses existing LLMs of comparable sizes, such as the Llama and Gemma
families, in generating helpful responses in Arabic, providing factually accurate
information about the region, and understanding nuanced cultural aspects. We
aspire for Juhaina to democratize cutting-edge AI technologies, serving over 400
million Arabic speakers by offering LLMs that not only communicate in their
language but also comprehend their culture. We publicly release all models on
Huggingface1.
1
Introduction
Large Language Models (LLMs) have emerged as transformative tools in artiﬁcial intelligence.
LLMs are believed to signiﬁcantly enhance productivity by automating complex tasks such as con-
tent creation and customer service [4]. Moreover, they enable more intuitive and accessible interac-
tions with technology, from personalized virtual assistants to advanced language translation services.
Currently, approximately 400 million people worldwide speak Arabic [8]. However, Arabic con-
tent constitutes only a small fraction of the web corpus used for pre-training large language models
(LLMs). For example, Common Crawl contains merely 0.6% of documents in Arabic [5]. This
scarcity is compounded by the unique linguistic patterns and the rich cultural and historical con-
notations inherent in the Arabic language. Consequently, many existing Arabic-centric [19, 12] or
multilingual LLMs [3, 17, 15] struggle to generate responses that are both useful and culturally
aligned in Arabic [16, 13].
To better serve the Arabic-speaking community, we set the goals as follows:
1The Juhaina LLMs can be downloaded from https://huggingface.co/elmrc

--- Page 2 ---

1. Proﬁciency in the Arabic Language. The LLM should understand user inputs in Arabic, gener-
ating coherent and grammatically correct outputs. It should avoid translationese, producing natural,
human-like responses. Additionally, the LLM should effectively articulate technical topics using
domain-speciﬁc terminology, such as in science.
2. Awareness of Local Facts. The LLM should be knowledgeable about facts commonly known
in Arabic-speaking regions, including history and geology. It should provide accurate information
without hallucination and incorporate this knowledge into general conversations.
3. Alignment with Arabic Culture. The LLM should generate responses that are appropriate and
respectful to the Arabic audience, adhering to the cultural and social norms of the region.
In this paper, we introduce Juhaina, a novel Arabic-English bilingual LLM, alongside CamelEval,
a new benchmarking tool, marking strides toward achieving these objectives. Juhaina is a decoder-
only dense transformer model, trained on context windows extending up to 8192 tokens, and has
9.24 billion parameters. This design allows for inference and further adaptation without the need
for high-end GPUs, enhancing its accessibility to the broader community. Juhaina is post-trained on
Gemma 2, a series of open-weight LLMs made available by Google [22].
CamelEval is a new benchmark for Arabic LLMs, speciﬁcally designed to assess their conversational
abilities and instruction-following proﬁciency within Arabic contexts. This benchmark embraces
the llm-as-a-judge framework, an approach pioneered by AlpacaEval[14]. To evaluate the LLMs’
capability to produce coherent responses that accurately reﬂect cultural nuances and regional facts,
we have carefully trans-curated two sets of challenging prompts. We aspire that CamelEval would
play a crucial role in gauging progress towards achieving the three key goals.
In this report, we outline the development and assessment of Juhaina, aiming to contribute our
insights to the broader community. We delve into our process of data curation, which involves
systematically searching for, collecting, annotating, and reﬁning datasets. This rigorous approach
yields a high-quality dataset that integrates translated open-source data, synthetic data, and human
annotations. Furthermore, we discuss our post-training strategies, which encompass supervised ﬁne-
tuning (SFT) and adjustments based on human feedback.
We conducted a thorough evaluation of Juhaina, employing a wide array of benchmarks to gain a
comprehensive understanding of its performance. Our evaluation incorporated benchmarks from
the Open Arabic LLM Leaderboard (OALL) [7] and CamelEval. The results of our assessment
show that Juhaina surpasses other LLMs of similar size in delivering useful responses within Arabic
contexts. This success represents a crucial advancement towards our goals of developing a model
that not only demonstrates a deep understanding of the Arabic language but also effectively captures
and aligns with the cultural and contextual nuances speciﬁc to Arabic-speaking regions.
We publicly release all Juhaina LLMs under MIT license. We aim for this release to serve the
Arabic-speaking communities and help narrow the disparity in accessing advanced AI technology.
2
Creating Juhaina LLMs
Juhaina is created by performing rigorous post-training on the Gemma 2 family of models, which
were pre-trained on up to 13 trillion tokens of primarily-English data [22]. Our post-training pro-
cess comprises two stages: the supervised ﬁne-tuning (SFT) stage and the alignment with human
preference stage.
In the SFT stage, the Juhaina LLM is trained to reproduce responses crafted by human annotators.
This involves exposing the model to a diverse set of high-quality, human-generated text examples,
ensuring it learns to generate coherent and contextually appropriate responses. The goal here is to
reﬁne the model’s understanding of language and improve its ability to generate text that closely
mirrors human communication.
In the alignment with human preference stage, the LLM is further reﬁned to adapt its style and
tone to align with human preferences. This stage involves using techniques such as reinforcement
learning from human feedback (RLHF), where the model’s outputs are evaluated and ranked by
human reviewers. The model is then adjusted based on this feedback to better match the desired
style, tone, and appropriateness of responses. This ensures that the LLM not only produces accurate
2

--- Page 3 ---

and contextually relevant information but also communicates in a manner that is consistent with
human expectations and cultural norms.
2.1
Data Collection
Collecting Arabic datasets was one of the main bottlenecks for developing Juhaina. Most of the
open Arabic datasets are translated from other languages and are subject to translation biases or fail
to reﬂect cultural context appropriately [23, 21, 24, 16]. Moreover, regional datasets are extremely
scarce and with limited quality [20, 2].
2.1.1
Data Sources
To systematically collect data, we ﬁrst identiﬁed a comprehensive list of subject categories, such
as “Science” and “Humanities.” For each subject, we further delineated sub-categories, such as
“Physics” and “History.” For each identiﬁed category, we conducted a thorough search to locate and
collect relevant datasets. Our search methodology encompassed the following data sources:
1. Internal Datasets: We identiﬁed existing datasets within our database. These datasets were
evaluated for relevance and quality to ensure they met our requirements.
2. Open Web Search: We performed extensive searches on the open web to ﬁnd websites containing
useful data that could be scraped. This involved using advanced search techniques and tools to
identify and extract data from various online sources. The data obtained from these sources was
then cleaned, validated, and integrated into our dataset.
3. Translatable Datasets: We located datasets available in different languages. These datasets were
ﬂagged for translation to ensure their effective utilization within our project. The translation process
involved both automated tools and manual veriﬁcation to maintain accuracy.
During the search, we considered a variety of criteria, such as relevance, accuracy, and timeliness.
The full list of criteria is available in the Appendix. We used a tagging system to annotate various
aspects of the data and ﬂagged data with high uncertainty for human review. We prioritized Mod-
ern Standard Arabic (MSA) data, ensured sources were reputable, and preferred cleaned data. We
collected the resulting dataset into a corpus with the associated category tags for further processing.
2.1.2
Data Cleaning
To ensure the quality and relevance of our dataset, we implemented a multi-step data cleaning pro-
cess. Initially, we applied basic ﬁlters to eliminate empty and invalid rows, which helped in removing
obvious errors and gaps in the data. Following this, we employed advanced ﬁltering techniques, in-
cluding semi-regular expressions (semi-regex) and fuzzy matching. These methods allowed us to
perform more nuanced cleaning, such as removing unwanted characters like emojis and ﬁltering out
non-Arabic data records, which could otherwise introduce noise and inaccuracies. We have also take
care to avoid data contamination by removing data that duplicate or paraphrase the benchmarks.
2.1.3
Prompt Generation
We deﬁned a list of LLM capabilities that we would like Juhaina to achieve, such as factuality and
reasoning (the full list of capabilities is provided in the Appendix). For each document in the data
corpus, the annotators generated prompts that invoke different LLM capabilities. Each prompt may
contain a context, which is an extract or summary of the original document, followed by the task
instruction or question. In some cases, the annotator also provided a “system prompt” that speciﬁes
the role of the LLM and the expected style of the response.
After curating the initial set of prompts, we used an automated tool to tag the quality and difﬁculty
of each prompt. Prompts with low quality are often ambiguous and lack clear instructions. We
removed these low-quality prompts from the ﬁnal set.
2.1.4
Answer Generation
We split the set of prompts into two parts: one for supervised ﬁne-tuning (SFT) and the other for
alignment through human feedback. For the SFT data, the annotators provided the ground truth
3

--- Page 4 ---

Data Quality Checklist
Duplicate or near-duplicate data
Missing data and other artifacts due to web scraping
Artifacts introduced by translation
Data in out-of-scope languages
Ill-formatted code blocks or structured text
Irrelevant system prompts
Unbalanced mix of tasks, categories, or difﬁculty
Table 1: Common data quality issues with multi-lingual datasets.
responses to the prompts. For the alignment data, the annotators provided preference feedback on
pairs of answers generated by the LLM.
2.1.5
Postprocessing
The dataset then undergoes three postprocessing pipelines: ﬁltering, transformation, and balancing.
The ﬁltering pipeline cleans the data by removing duplicates, unnecessary white spaces, foreign
language content, and other irrelevant elements. It also veriﬁes the overlap between each sample
and the evaluation data to ensure there is no contamination with the test set. The transformation
pipeline converts the cleaned data into the desired alignment format. During each stage, native
speakers conduct manual investigations to address any non-trivial cases.
Once the data is processed, a further level of re-sampling is performed to improve data distribu-
tion. We sub-sample an equal number of rows for each subject category, resulting in a ﬁnal dataset
comprising approximately 600,000 rows for SFT and 40,000 rows for alignment.
2.1.6
Learnings on Data Collection
We have learned several key lessons from our data curation process.
Focus on Data Quality. There is a well-known trade-off between quality and quantity in data collec-
tion. We found that quality matters much more than quantity in post-training. In fact, our experience
shows that including low-quality data signiﬁcantly hurts benchmark performance. However, in prac-
tice, we tend to overemphasize data quantity simply because it is easier to measure (i.e., just count
the tokens or rows), whereas understanding data quality is quite non-trivial. Based on the problems
we have encountered and resolved during the curation process, we created a checklist of common
data quality issues with multi-lingual datasets:
Tag the Data. We found that extensively tagging the data greatly facilitates the curation process.
It not only exposes data quality issues but also informs data selection and sampling. We adopted a
variety of automated tagging systems and human annotations to understand various aspects of the
data, including subject category and sub-category, task type, task difﬁculty, and more.
Effective Communication with Annotators. We extensively used human annotation and feedback
in the curation process. We found that effective communication with the annotators is vital for
success. Care needs to be taken to ensure that the annotators understand and adhere to the desired
annotation practices. Providing practical examples and a walk-through of the process helps align
expectations and behaviors. Failure or delay in communication could lead to systematic errors or
biases in the data, rendering the effort worthless.
2.2
Post-training Procedure
2.2.1
Supervised Finetuning (SFT)
We used the Llama Pro algorithm [25] for supervised ﬁne-tuning (SFT). Llama Pro performs block
expansion on the base model to introduce additional free parameters. During the training stage,
only these newly added parameters are trained. Our experiments indicate that, compared to standard
SFT, Llama Pro enables the LLM to acquire additional capabilities in the Arabic language without
compromising its existing capabilities in English. The training settings are detailed in Table 2.
4

--- Page 5 ---

Parameter
SFT
Align.
Optimizer
AdamW
AdamW
Method
Llama pro [25]
Freeze
Initial lr
5e-5
1e-5
Scheduler
Cosine
Cosine
Epochs
3
1
GPU (per node)
8
8
Nodes
8
8
Batch size
64
32
Table 2: The parameters being adopted for training.
2.2.2
Alignment with Human Feedback
At the conclusion of the Supervised Fine-Tuning (SFT) stage, the Juhaina model has demonstrated
proﬁciency in following instructions and adapting to domain-speciﬁc knowledge. However, addi-
tional post-processing is necessary to ensure safety and adherence to desired behaviors, such as
compliance with speciﬁc cultural norms.
This requirement is particularly important given the ﬂexibility of the Arabic language and the di-
versity of its dialects and cultural contexts. To address these challenges, we have implemented a
bespoke data curation approach aimed at achieving high data quality. In particular, the alignment
data is meticulously collected and validated by native Arabic speakers to ensure accuracy and cul-
tural relevance.
We used the Monolithic Odds Ratio Preference Optimization (ORPO) algorithm [10] to align
Juhaina with human preference data. ORPO is inspired by the Direct Preference Optimization (DPO)
algorithm [18]. Based on empirical evidence from our pilot studies, we selected ORPO for two pri-
mary reasons. Firstly, unlike DPO, ORPO does not require a reference model, which signiﬁcantly
reduces GPU memory usage during training. Secondly, ORPO naturally incorporates a supervised
ﬁne-tuning (SFT) loss, which is known to stabilize the training process [6].
Similar to the SFT stage, we adopted freeze tuning, adapting only a subset of the model parameters.
Our pilot studies indicated that freeze tuning achieves better performance compared to full parameter
tuning or other parameter-efﬁcient methods, such as LoRa [11]. The training parameters are detailed
in Table 2. The computing setup is the same as the SFT stage.
2.2.3
Infrastructure and Computing
The SFT was conducted on our computing cluster, which consists of 8 nodes, each equipped with
8 GPUs featuring 80GB of VRAM. We utilized PyTorch’s Fully Sharded Data Parallel (FSDP) to
efﬁciently manage the parallel training process. The training was completed in 3 days.
3
Evaluation of Arabic LLMs
3.1
Open Arabic LLM Leaderboard (OALL)
The Open Arabic LLM Leaderboard (OALL) is one of the few close-ended Arabic benchmarks
[7]. It encompasses three primary benchmarks: AlGhafa [1], ACVA [9], and Arabic MMLU [13],
which are all curated speciﬁcally for Arabic LLMs. OALL also include translated versions of stan-
dard LLM benchmarks such as EXAMS, ARC, BOOLQ, COPA, HELLASWAG, OPENBOOK-QA,
PIQA, RACE, SCIQ, and TOXIGEN. They assess the model’s capability in selecting the correct an-
swer from yes-no or multiple-choice options in the zero-shot setting. The normalized log-likelihood
of the target is used to measure the model’s ability to generate the correct choice. The OALL has a
centralized and managed process to evaluate all submitted LLMs. This ensures reproducibility and
standardization of the results.
5

--- Page 6 ---

Model
Size (B)
Average
ACVA
AlGhafa
AR-MMLU
TOXIGEN
Silma-9B-v1
9.24
70.62
78.89
71.85
52.55
67.59
Gemma-2-SimPO
9.24
58.55
43.45
54.2
53.65
82.46
SauerkrautLM
12.25
57.35
39.54
56.09
43.99
79.04
Gemma-2-SPPO
9.24
57.16
46.97
52.55
52.91
81.28
Juhaina
9.24
60.18
61.82
60.47
51.06
80.21
Table
3:
Top
performing
LLMs
on
the
OALL
with
model
sizes
between
7B
to
13B
at
the
time
of
writing.
The
other
models
being
compared
are
“Silma-9B-
v1”(silma-ai/Silma-9B-Instruct-v1.0 ), “Gemma-2-SimPO”(princeton-nlp/gemma-2-9b-it-SimPO
), “SauerkrautLM”(VAGOsolutions/SauerkrautLM-Nemo-12b-Instruct ), and “Gemma-2-SPPO”
(UCLA-AGI/Gemma-2-9B-It-SPPO-Iter3 ).
The latest leaderboard is available online 2. In Table 3, we reproduce the results of the top-ﬁve LLMs
among those with less than 13B parameters. We note that Juhaina is currently at the second place,
achieving strong performance in the overall average score and the three main Arabic benchmarks.
Remarkably, Silma-9B-v1 stands out for its incredible performance, leading the overall leaderboard
and surpassing models even with more than 70B parameters.
OALL is instrumental in evaluating text completion capabilities, logical correctness, and factual
knowledge across different domains. However, it has several key limitations:
1. Narrow coverage of LLM Capabilities. The benchmark’s reliance on multiple-choice questions
means it fails to evaluate the broader spectrum of LLM capabilities, such as engaging in conver-
sations or following instructions. It does not measure the helpfullness or the utility of the LLM’s
replies, which are essential aspects of its performance. In fact, the ability to participate in general
conversations is a deﬁning feature of LLMs. Consequently, while this benchmark is effective for as-
sessing the foundational knowledge and reasoning skills of pre-trained LLMs, it does not adequately
measure the performance of LLMs that have been instruction-ﬁnetuned for generating meaningful
interactions with users.
2. Oversimpliﬁed evaluation metric. The evaluation metric used by OALL, the normalized log-
likelihood (NLL), is overly simplistic. NLL calculates the log-probability of producing the "gold
response," adjusted for the length of this ideal response. However, the assumption that there’s a sin-
gular "gold response" is ﬂawed, even in contexts like multiple-choice questions. This inconsistency
is apparent in OALL itself, where some correct answers are labeled as A, B, C, or D, and others
are identiﬁed by the text of the correct option3. The variability in deﬁning what constitutes a "gold
response" renders NLL an unreliable and imprecise metric for LLMs, which can generate texts in
diverse formats and styles.
3. Public test set. Publishing the benchmark test set enhances transparency, but it simultaneously
opens the door for gaming the leaderboard. Speciﬁcally, individuals could ﬁne-tune the LLM using
a compromised dataset, leading to inﬂated scores. We have taken considerable efforts in our data cu-
ration process to minimize the chance of test set contamination (Section 2.1). However, considering
the widespread recognition and credibility of OALL, it’s plausible that some might be motivated to
undertake deceptive practices.
3.2
CamelEval
To address the limitations in OALL, we developed a new evaluation benchmark, CamelEval.
CamelEval is based on AlpacaEval [14], an LLM-as-a-judge automatic evaluation framework for
instruction-following LLMs. Essentially, two competing LLMs provide responses to a set of test
prompts, and they are subsequently evaluated by a “judge” LLM to decide the win rate.
CamelEval enables a better coverage of LLM capabilities, especially the ability to generate helpful
conversations and following user instruction. Using a LLM as a judge, CamelEval avoids much
2https://huggingface.co/spaces/OALL/Open-Arabic-LLM-Leaderboard
3Adding few-shot examples may help alleviate the arbitrariness of "gold response”, but OALL employees
zero-shot evaluation in all cases [7].
6

--- Page 7 ---

Curated
Translated
Model
Size (B)
Win Rate %
Std
Win Rate %
Std
GPT-4o-2024-05-13
-
99.73
0.11
97.11
0.50
Qwen2-72B-Instruct
72.7
95.80
0.57
91.95
0.83
MBZUAI-ORYX-new
43.7
93.55
0.72
85.70
1.09
Gemma2-9B-IT
9.24
50.00
0.00
50.00
0.00
Jais-Inception-70b
72.7
43.67
1.68
43.08
1.66
Silma-9B-v1
9.24
30.56
1.49
45.26
1.61
Juhaina-9B
9.24
98.47
0.36
91.37
0.88
Table 4: Performance of Juhaina and other notable Arabic-centric or multilingual LLMs of equal or
larger sizes on CamelEval. We report the winrate against the Gemma2-9B-IT model on the curated
and translated prompt sets. Juhaina is able to generate more helpful responses for challenging Arabic
queries compared to LLMs of 4-7 times the size.
of the limitations of simple metrics, such as NLL. Furthermore, we included new prompts that
have not appear in OALL before, reducing the chance of contamination. Therefore, we believe
that CamelEval offers additional insights into LLM capabilities, which are more aligned with the
practical use cases of instruction-following AI assistants.
CamelEval comprises two distinct test sets. The ﬁrst, known as the Translated Set, consists of trans-
lations of the 805 prompts found in the original AlpacaEval. The English version of these prompts
has gained widespread use for evaluating LLMs and has demonstrated a high level of concordance
with assessments made by human evaluators. To assemble the Translated Set, we enlisted native-
speaking annotators to reﬁne the initial translations provided by Freedom Intelligence (link). These
annotators have successfully identiﬁed and corrected various anomalies that likely originated from
the process of machine translation.
To better reﬂect Arabic cultural linguistic nuances, we developed the second test set, named the Cu-
rated Set. This premium test set contains 805 prompts, synthetically created using GPT-4, based on a
corpus of human-curated, textbook-quality content spanning various ﬁelds such as culture, religion,
history, sociology, and other scientiﬁc disciplines. To ensure the prompts encapsulate complex in-
structions and pose challenging questions, we directed GPT-4 to formulate questions that go beyond
the information provided in the text, necessitating supplementary knowledge for accurate responses.
We then assessed the difﬁculty level of these questions, selecting only the most challenging for in-
clusion. To guarantee the accuracy and relevance of these prompts, annotators manually reviewed
each one. The speciﬁc subject categories covered in the Curated Set are detailed in Appendix A.4.
In Table 4, we present a comparison of Juhaina’s performance against a selection of LLMs that are
either focused on Arabic or are multilingual, and that have a parameter count equal to or larger than
that of Juhaina. For this comparison, Gemma2-9b-IT serves as the baseline against which the win
rate is calculated.
We observe that in the Translated Set, Juhaina’s performance is on par with that of the much larger
70B Qwen2-Instruct LLM, showcasing its efﬁciency in handling translated prompts. In the more
demanding Curated Set, Juhaina closely follows the performance of GPT-4o, indicating its strong
capability in addressing complex, culturally nuanced questions. Additionally, we note a signiﬁcant
and consistent underperformance by Silma-9B-v1 compared to the model it was ﬁne-tuned from,
Gemma2-9b-IT, with a win rate of less than 50% across both test sets. This highlights a potential is-
sue in the ﬁne-tuning process or the adaptability of Silma-9B-v1 to the speciﬁc challenges presented
by the CamelEval benchmark.
We note that the typical constraints associated with using LLMs as evaluators also apply to Camel-
Eval. For example, there’s a possibility that the judge LLM might show a preference for answers it
generates itself. Additionally, other factors, like the length of the response, could introduce biases
into the evaluation process. We aim to tackle these and other unresolved challenges in future updates
of CamelEval.
7

--- Page 8 ---

4
Discussion
In this study, we have detailed the development of Juhaina, a leading open-weight Arabic LLM,
and introduced CamelEval, a new benchmark for Arabic LLMs that serves as a complement to the
existing OALL benchmarks. We aspire that the release of Juhaina’s LLM weights, along with the
CamelEval benchmark and the insights shared in this work, will assist the community in advancing
the creation of improved and more culturally attuned LLMs for the Arabic-speaking world.
References
[1] ALMAZROUEI, E., COJOCARU, R., BALDO, M., MALARTIC, Q., ALOBEIDLI, H., MAZ-
ZOTTA, D., PENEDO, G., CAMPESAN, G., FAROOQ, M., ALHAMMADI, M., LAUNAY, J.,
AND NOUNE, B. AlGhafa evaluation benchmark for Arabic language models. In Proceedings
of ArabicNLP 2023 (Singapore (Hybrid), Dec. 2023), H. Sawaf, S. El-Beltagy, W. Zaghouani,
W. Magdy, A. Abdelali, N. Tomeh, I. Abu Farha, N. Habash, S. Khalifa, A. Keleg, H. Had-
dad, I. Zitouni, K. Mrini, and R. Almatham, Eds., Association for Computational Linguistics,
pp. 244–275.
[2] ALYAFEAI, Z., ALMUBARAK, K., ASHRAF, A., ALNUHAIT, D., ALSHAHRANI, S., AB-
DULRAHMAN, G. A., AHMED, G., GAWAH, Q., SALEH, Z., GHALEB, M., ET AL. Cidar:
Culturally relevant instruction dataset for arabic. arXiv preprint arXiv:2402.03177 (2024).
[3] ARYABUMI, V., DANG, J., TALUPURU, D., DASH, S., CAIRUZ, D., LIN, H., VENKITESH,
B., SMITH, M., MARCHISIO, K., RUDER, S., ET AL. Aya 23: Open weight releases to further
multilingual progress. arXiv preprint arXiv:2405.15032 (2024).
[4] BROWN, T. B. Language models are few-shot learners. arXiv preprint arXiv:2005.14165
(2020).
[5] CRAWL,
C.
Statistics
of
common
crawl
monthly
archives.
https://commoncrawl.github.io/cc-crawl-statistics/plots/languages.html.
Accessed: 2024-09-11.
[6] DUBEY, A., JAUHRI, A., PANDEY, A., KADIAN, A., AL-DAHLE, A., LETMAN, A.,
MATHUR, A., SCHELTEN, A., YANG, A., FAN, A., ET AL. The llama 3 herd of models.
arXiv preprint arXiv:2407.21783 (2024).
[7] ELFILALI,
A.,
ALOBEIDLI,
H.,
FOURRIER,
C.,
BOUSSAHA,
B.
E.
A.,
CO-
JOCARU,
R.,
HABIB,
N.,
AND
HACID,
H.
Open
arabic
llm
leaderboard.
https://huggingface.co/spaces/OALL/Open-Arabic-LLM-Leaderboard, 2024.
[8] ETHNOLOGUE. Ethnologuearabic statistics. https://www.ethnologue.com/language/ara/.
Accessed: 2024-09-11.
[9] FREEDOMINTELLIGENCE.
Acva
arabic
cultural
value
alignment.
https://huggingface.co/datasets/FreedomIntelligence/ACVA-Arabic-Cultural-Value-Alignment,
2024.
[10] HONG, J., LEE, N., AND THORNE, J. Orpo: Monolithic preference optimization without
reference model. arXiv preprint arXiv:2403.07691 2, 4 (2024), 5.
[11] HU, E. J., SHEN, Y., WALLIS, P., ALLEN-ZHU, Z., LI, Y., WANG, S., WANG, L.,
AND CHEN, W.
Lora: Low-rank adaptation of large language models.
arXiv preprint
arXiv:2106.09685 (2021).
[12] HUANG, H., YU, F., ZHU, J., SUN, X., CHENG, H., SONG, D., CHEN, Z., ALHARTHI, A.,
AN, B., LIU, Z., ZHANG, Z., CHEN, J., LI, J., WANG, B., ZHANG, L., SUN, R., WAN, X.,
LI, H., AND XU, J. Acegpt, localizing large language models in arabic, 2023.
[13] KOTO, F., LI, H., SHATNAWI, S., DOUGHMAN, J., SADALLAH, A. B., ALRAEESI, A.,
ALMUBARAK, K., ALYAFEAI, Z., SENGUPTA, N., SHEHATA, S., ET AL. Arabicmmlu: As-
sessing massive multitask language understanding in arabic. arXiv preprint arXiv:2402.12840
(2024).
[14] LI, X., ZHANG, T., DUBOIS, Y., TAORI, R., GULRAJANI, I., GUESTRIN, C., LIANG, P.,
AND HASHIMOTO, T. B. Alpacaeval: An automatic evaluator of instruction-following models.
https://github.com/tatsu-lab/alpaca_eval, 5 2023.
8

--- Page 9 ---

[15] MUENNIGHOFF, N., WANG, T., SUTAWIKA, L., ROBERTS, A., BIDERMAN, S., SCAO,
T. L., BARI, M. S., SHEN, S., YONG, Z.-X., SCHOELKOPF, H., ET AL. Crosslingual gener-
alization through multitask ﬁnetuning. arXiv preprint arXiv:2211.01786 (2022).
[16] NAOUS, T., RYAN, M. J., RITTER, A., AND XU, W. Having beer after prayer? measuring
cultural bias in large language models. arXiv preprint arXiv:2305.14456 (2023).
[17] PENEDO, G., MALARTIC, Q., HESSLOW, D., COJOCARU, R., CAPPELLI, A., ALOBEI-
DLI, H., PANNIER, B., ALMAZROUEI, E., AND LAUNAY, J. The reﬁnedweb dataset for
falcon llm: outperforming curated corpora with web data, and web data only. arXiv preprint
arXiv:2306.01116 (2023).
[18] RAFAILOV, R., SHARMA, A., MITCHELL, E., MANNING, C. D., ERMON, S., AND FINN,
C. Direct preference optimization: Your language model is secretly a reward model. Advances
in Neural Information Processing Systems 36 (2024).
[19] SENGUPTA, N., SAHU, S. K., JIA, B., KATIPOMU, S., LI, H., KOTO, F., MARSHALL, W.,
GOSAL, G., LIU, C., CHEN, Z., ET AL. Jais and jais-chat: Arabic-centric foundation and
instruction-tuned open generative large language models. arXiv preprint arXiv:2308.16149
(2023).
[20] SINGH, S., VARGUS, F., DSOUZA, D., KARLSSON, B. F., MAHENDIRAN, A., KO, W.-Y.,
SHANDILYA, H., PATEL, J., MATACIUNAS, D., OMAHONY, L., ET AL. Aya dataset: An
open-access collection for multilingual instruction tuning. arXiv preprint arXiv:2402.06619
(2024).
[21] STANOVSKY, G., SMITH, N. A., AND ZETTLEMOYER, L. Evaluating gender bias in machine
translation. arXiv preprint arXiv:1906.00591 (2019).
[22] TEAM, G., RIVIERE, M., PATHAK, S., SESSA, P. G., HARDIN, C., BHUPATIRAJU, S.,
HUSSENOT, L., MESNARD, T., SHAHRIARI, B., RAMÉ, A., ET AL. Gemma 2: Improving
open language models at a practical size. arXiv preprint arXiv:2408.00118 (2024).
[23] VANMASSENHOVE, E., SHTERIONOV, D., AND GWILLIAM, M.
Machine translationese:
Effects of algorithmic bias on linguistic complexity in machine translation. arXiv preprint
arXiv:2102.00287 (2021).
[24] WANG, J., RUBINSTEIN, B., AND COHN, T. Measuring and mitigating name biases in neu-
ral machine translation. In Proceedings of the 60th Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers) (2022), pp. 2576–2590.
[25] WU, C., GAN, Y., GE, Y., LU, Z., WANG, J., FENG, Y., LUO, P., AND SHAN, Y. Llama
pro: Progressive llama with block expansion. arXiv preprint arXiv:2401.02415 (2024).
9

--- Page 10 ---

A
Appendix
A.1
Criteria for Data Search
1. Relevance to Topic Criteria: The data must be directly related to our subject categories.
2. Timeliness Criteria: The data should be up to date.
3. Completeness Criteria: The dataset should be comprehensive enough to support robust
analysis.
4. Granularity Criteria: The data should have the appropriate level of detail.
5. Availability and Accessibility Criteria: The data should be accessible and has an open
license.
6. Bias and Objectivity Criteria: The data should be free from bias or, if biased, the bias
should be understood and accounted for.
7. Cost: The estimated cost for accessing and curating the data.
A.2
List of LLM Capabilities
1. Information Provision: Delivering speciﬁc information or facts on various topics.
2. Reasoning: Engaging in logical thinking, problem-solving, or managing complex tasks.
3. Planning: Assisting in the creation of plans or strategies for activities and projects.
4. Editing: Editing, rephrasing, proofreading, or performing other tasks related to the com-
position of written content.
5. Coding & Debugging: Assisting with writing, reviewing, or ﬁxing code in programming.
6. Math: Providing help with mathematical concepts, problems, and calculations.
7. Role Playing: Interacting with users by adopting a character or persona.
8. Data Analysis: Interpreting data, analyzing statistics, or performing analytical tasks.
9. Creative Writing: Crafting stories, poems, or other creative texts.
10. Advice Seeking: Offering recommendations or guidance on various personal or profes-
sional issues.
11. Brainstorming: Generating ideas, engaging in creative thinking, or exploring possibilities.
12. Other: Addressing queries that do not ﬁt into the above categories.
A.3
Examples of Translation Issues in OALL
Example One:
: 	àB ,. éªÒ Ë@ úÎ« èXñk. ñÖÏ@ éÊª Ë@ HA	®¢	@
.ÉJ
J	®Ë@ úÎ« HQm.	¯ Y®Ë (0
.ÉJ
J	®Ë@ úÎ« H. A®K Xñ« Iª 	ð Y®Ë (1
ÉJ
J	®Ë@ úÎ« HQm.	¯ Y®Ë: éK.Ag. B @
Example Two:
: ½Ë 	YË ,. éÊ	®mÌ'@ ú
	¯ èQºK. Ég. QË@ H. Qå
.ú
ÍAJË@ ÐñJ
Ë@ ú
	¯ ¨@YË@ 	áÓ ú
	GAªK
 	àA¿ (0
.ú
ÍAJË@ ÐñJ
Ë@ ú
	¯
	­	KB@ ú
	¯ 	àCJ
. I. 
@ (1
.ú
ÍAJË@ ÐñJ
Ë@ ú
	¯ ¨@YË@ 	áÓ ú
	GAªK
 	àA¿: éK.Ag. B @
10

--- Page 11 ---

Example Three:
: ½Ë 	YË ,. éÒÊ¾Ë@ éK.AJ» ú
	¯ I. ËA¢Ë@ A¢ 	k@
.AêjJ
jK. ÕÎªÖÏ@ ÐA¯ (0
. éÒÊªÖÏ@ AîEXQ£ (1
: éK.Ag. B @
Example Four:
: HAg@Q¯B@ Ég. P .I. JºÓ
	­Ê 	g HYjJK Z@QÔg éËYJ.K. è@QÓ@
.P@Ym.Ì'@ úÎ« ÉÓAg 	áÓ H@Q» 	Y 	gAK
 (0
. éJ
KAK.QêºË@ é	ºÖÏAK. Xñ@ ú
æQ»
	­J
 	¢	JK. Ðñ®K
 (1
.Q
	ª
	J
K.@
	ñk ú
	¯ ZAÖÏ@
QK
 (2
.èQê 	£
	­Ê 	g éÓY¯ ÉÒm'
ð
	­®K
 (3
èQê 	£
	­Ê 	g éÓY¯ ÉÒm'
ð
	­®K
: éK.Ag. B @
A.4
Subject Categories in CamelEval Curated Set
11

--- Page 12 ---

Category
Occurrence
Physics
66
Biographic
65
Economy
62
Philosophy
61
Geology
61
Psychology
60
Nutrition
59
Chemistry
58
Education
56
Arts
54
Medicine
53
Arabic
50
Math
39
Engineering
24
Tech
16
Anthropology
14
Infographic
3
Environment
2
History
2
Table 5: Subject categories in CamelEval Curated Set. The prompts in the Curated Set covers a wide
range of topics that are science and culture related.
12

```
