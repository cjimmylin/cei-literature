---
title: "2025-Mohammed-Cross-Language Approach for Quranic QA - PDF Extract"
source_pdf: "2025-Mohammed-Cross-Language Approach for Quranic QA.pdf"
pages: 10
extracted_at: "2026-02-13T09:15:45.121386"
---

# PDF Extract: 2025-Mohammed-Cross-Language Approach for Quranic QA

**Source PDF:** 2025-Mohammed-Cross-Language Approach for Quranic QA.pdf
**Total Pages:** 10

---

## Content

```
--- Page 1 ---

Cross-Language Approach for Quranic QA
Islam Oshallah, Mohamed Basem, Ali Hamdi, and Ammar Mohammed
Faculty of Computer Science, MSA University, Egypt
{ islam.abdulhakeem, mohamed.basem1, ahamdi, ammohammed}@msa.edu.eg
Abstract. Question answering systems face critical limitations in languages with limited
resources and scarce data, making the development of robust models especially challenging.
The Quranic QA system holds significant importance as it facilitates a deeper understanding
of the Quran, a Holy text for over a billion people worldwide. However, these systems face
unique challenges, including the linguistic disparity between questions written in Modern
Standard Arabic and answers found in Quranic verses written in Classical Arabic, and the
small size of existing datasets, which further restricts model performance. To address these
challenges, we adopt a cross-language approach by (1) Dataset Augmentation: expanding
and enriching the dataset through machine translation to convert Arabic questions into
English, paraphrasing questions to create linguistic diversity, and retrieving answers from
an English translation of the Quran to align with multilingual training requirements; and
(2) Language Model Fine-Tuning: utilizing pre-trained models such as BERT-Medium,
RoBERTa-Base, DeBERTa-v3-Base, ELECTRA-Large, Flan-T5, Bloom, and Falcon to
address the specific requirements of Quranic QA. Experimental results demonstrate that this
cross-language approach significantly improves model performance, with RoBERTa-Base
achieving the highest MAP@10 (0.34) and MRR (0.52), while DeBERTa-v3-Base excels
in Recall@10 (0.50) and Precision@10 (0.24). These findings underscore the effectiveness
of cross-language strategies in overcoming linguistic barriers and advancing Quranic QA
systems.
Keywords: Quran Question Answering, Passage Retrieval, Modern Standard Arabic, Classical
Arabic, Dataset Expansion, Fine-Tuning.
1
Introduction
The Holy Quran is revered by Muslims worldwide as a Holy source of guidance and knowledge
[1]. However, its accessibility is often limited by linguistic barriers, particularly for non-Arabic
speakers and even for native Arabic speakers unfamiliar with its Classical Arabic form [2].
Readers and commentators have historically faced challenges in understanding the Quran due
to its linguistic style and complex composition [3]. These complexities are compounded by the
linguistic gap between modern standard Arabic (MSA), often used in questions, and classic Arabic
(CA), the language of the Quran [4]. To bridge this gap, a cross-language approach is essential,
taking advantage of advanced translations and language models.
Existing Quranic QA systems, such as those explored in the Quran QA 2023 shared task, have
made significant strides to address these challenges [5]. These tasks focus on two primary subtasks:
Passage Retrieval, which aims to identify the most relevant Quranic passages in response to a
query, and Machine Reading Comprehension, which aims to retrieve accurate and contextually
relevant passages. However, the development of Quranic QA systems faces critical challenges due
arXiv:2501.17449v1  [cs.CL]  29 Jan 2025

--- Page 2 ---

2
Islam Oshallah et al.
to the small size of existing datasets and the linguistic disparity between MSA, used in questions,
and Classical Arabic (CA), found in Quranic verses. These limitations cause a severe hinder to the
model performance, emphasizing the need for innovative approaches to dataset expansion and
fine-tuning LLMs and LMs to meet the unique requirements of Quranic QA.
This research adopts a cross-language approach to enhance Quranic QA systems. By translating
both questions and answers, the linguistic barriers posed by MSA and CA are overcome. The
dataset was significantly expanded through machine translation, paraphrasing, and the integration
of additional questions from existing literature. Fine-tuned LLMs, such as BERT-Medium,
RoBERTa-Base, DeBERTa-v3-Base, ELECTRA-Large, Flan-T5, Bloom, and Falcon, were trained
to address these challenges effectively. This approach not only enhances the dataset but also aligns
advanced language models with the unique linguistic and contextual complexities of Quranic
texts. By upgrading and highlighting these advancements, the system provides more accurate and
context-sensitive responses, allowing deeper engagement with the Quran[6].
Figure 1 illustrates the workflow adopted in this study, showcasing the process from dataset
augmentation to fine-tuning and evaluation. This diagram highlights the cross-language approach
and the transformations of the data set essential for improving the Quranic QA system.
Old Dataset
174 Q Train
52 Q Test
25 Q Dev
Augment with Literature & Paraphrase
Expanded Dataset: 1895 Q (Arabic)
Translate to English
Final Dataset: 1895 Q (English)
Fine-Tune LMS & LLMs
Evaluation Metrics (MAP ,MRR ,Recall , Precision)
Fig. 1. Workflow for Cross-Language Dataset Expansion and Fine-Tuning.
2
Related Work
The Quranic text is rich and contains many events, making it essential to efficiently retrieve
passages and answer questions [7]. Its unique features, like complex syntax, multiple definitions,
and deep linguistic elements, present challenges for question-answering systems [8]. One major
challenge is bridging the gap between Modern Standard Arabic and Classical Arabic, as well as
handling unanswerable queries using techniques like thresholding [9].
Models like AraBERT, CAMeLBERT, and AraELECTRA have shown great potential in
handling Arabic text, effectively capturing its meaning and context [10]. However, limited or
unbalanced datasets often hinder their performance, making it harder to handle new or unseen
queries [11]. Sarhan and Elkomy [9] addressed these issues by using hybrid models that combine

--- Page 3 ---

Quran QA
3
dual-encoder and cross-encoder approaches. They leveraged transfer learning with external datasets
like TyDI QA and Tafseer, improving performance with a MAP score of 0.25. Despite this, there
is still a need for more dataset expansion.
Mahmoudi et al. [12] introduced a multitask transfer learning method, combining both
unsupervised and supervised fine-tuning using models like AraELECTRA and AraBERT. They
used advanced embedding techniques like TSDAE and SimCSE to improve passage retrieval by
producing high-quality sentences. However, they also stressed the need for more dataset expansion.
In another approach, Alawwad et al. [13] focused on Quranic passage retrieval by translating
Arabic queries into English. This allowed them to use advanced English-based models, such
as OpenAI embeddings and sentence transformers. Their system also included a paraphrasing
module to create multiple query variations, significantly improving retrieval accuracy. This method
demonstrated the power of translation-based techniques in overcoming linguistic barriers. The
queries were applied to an English-translated version of the Quran, utilizing LLMs and other
models that support English [14].
This work approach focuses on two main aspects: (1) Dataset Augmentation, which expands
and enriches datasets by translating Arabic questions into English and paraphrasing to create more
diverse queries. Answers are then retrieved from an English translation of the Quran; and (2)
Language Model Fine-Tuning, where models like BERT-Medium, RoBERTa-Base, DeBERTa-v3-
Base, ELECTRA-Large, Flan-T5, Bloom, and Falcon are fine-tuned to handle Quranic QA tasks.
This approach effectively bridges the gap between Modern Standard Arabic and Classical Arabic,
improving performance.
3
Methodology
The methodology of this study comprises three key phases:
1. Dataset Preparation: Expanding and diversifying the original dataset through the addition
of new questions and paraphrasing to increase the linguistic variation.
2. Cross-Language : Translating questions into English to leverage the capabilities of widely
available pre-trained language models that perform better in English.
3. Model Fine-Tuning: Fine-tuning state-of-the-art models, including BERT-Medium, RoBERTa-Base,
DeBERTa-v3-Base, ELECTRA-Large, Flan-T5, Bloom, and Falcon, to optimize performance for the
Quranic QA task.
3.1
Dataset Preparation
Database Collection The dataset was collected and picked from multiple authentic and trustworthy
sources to ensure its diversity, accuracy, and relevance. This comprehensive dataset enhances the
ability of the model to handle various QA scenarios and context-dependent or ambiguous queries
from the Quranic text, thereby improving the overall performance of Quranic QA systems. The
primary sources included:
– Quran QA 2023 Shared Task Dataset: This foundational dataset, curated for the Quran QA
shared task [5], comprises 251 structured questions paired with annotated Quranic passages.
It served as the basis for our experiments.

--- Page 4 ---

4
Islam Oshallah et al.
– SQuAD v2 Dataset: The SQuAD v2 dataset [15] was incorporated to increase diversity and
address unanswerable questions. With over 100,000 questions, it enriched the adaptability of
the model across various QA scenarios.
– 1000 Questions and Answers in the Holy Quran PDF: Extracted data from this resource
[16] underwent rigorous cleaning to ensure relevance and integration into the dataset.
– List of Plants Citation in Quran and Hadith: Context-specific references from the Quranic
Botanic Garden [17] added unique dimensions to the dataset.
– Translated Quran Texts: Translations of the Quran [18] bridged linguistic and contextual
gaps between Modern Standard Arabic and Classical Arabic.
Dataset Expansion The dataset was expanded from the original 251 questions in the Quran QA
2023 Shared Task to 629 questions using resources such as the 1000 Questions and Answers in
the Holy Quran [16] and the List of Plants Citation in Quran and Hadith [17]. Each question
was rephrased twice, resulting in a rich dataset of 1,895 questions categorized into single-answer,
multi-answer, and zero-answer types.
This process, illustrated in Figure 1, demonstrates how dataset manipulation enhances linguistic
diversity and adaptability. The expanded dataset allowed for fine-tuning multiple pre-trained
transformer models, improving their ability to handle varied question formats and enhancing
overall retrieval performance in Quranic QA tasks.
Dataset Cleaning To ensure the quality of the dataset and reliability, the following cleaning steps
were performed:
– Removal of Irrelevant or Low-Quality Pairs: Unclear or irrelevant question-passage pairs
were removed to maintain dataset integrity.
– Standardization of Question Formats: Questions were standardized to ensure consistency
across the dataset, facilitating effective model training and comprehension.
3.2
Cross-Language Approach
A key aspect of this study is the cross-language approach, which involved translating the dataset
into English to enhance the performance of language models in the Quranic Question Answering
task. This approach addresses the linguistic challenges posed by the use of Modern Standard Arabic
(MSA) in the questions and Classical Arabic (CA) in the Quranic passages. Since many pre-trained
large language models (LLMs) and language models (LMs), such as BERT-Medium, RoBERTa-
Base, DeBERTa-v3-Base, ELECTRA-Large, Flan-T5, Bloom, and Falcon, are primarily optimized
for English, this translation step was essential to bridge the linguistic gap and significantly improve
model performance in handling context-dependent or ambiguous queries from the Quranic text.
To make the dataset compatible with these models, the questions were translated using the
Google Translate API To English, with a focus on preserving the structure and nuances of the
original text. This process helped align the dataset with the strengths of pre-trained LMS and
LLMs, which tend to perform more effectively on English data [19]. Additionally, the use of the
translated Quran by Marmaduke Pickthall [18], a renowned Islamic scholar, helped overcome the
linguistic complexities associated with Classical Arabic. This translation, known for its authenticity
and clarity, provided a standardized and contextually accurate version of the Quranic passages.

--- Page 5 ---

Quran QA
5
This translation process proved instrumental in improving the ability of the model to interpret
user queries and retrieve relevant Quranic passages. By converting questions into English, the
models could better understand and process the input while providing answers rooted in accurate
and clear translation of Pickthall. This ensured that the answers preserved the original meanings
while seamlessly adapting to the English language structure, making them both accessible and
contextually accurate.
Furthermore, this cross-language approach helped address several challenges unique to Arabic,
such as its complex syntax and linguistics, which can sometimes hinder the effectiveness of
Arabic-language models. Translating both the questions and the Quranic verses into English
facilitated the training of models that could generalize across different question formats and
languages, improving overall performance.
In summary, the cross-language approach, which involved translating the dataset using the
Google Translate API and utilizing the translated Quran of Marmaduke Pickthall, significantly
enhanced the ability of the model to perform in Quranic QA tasks. It ensured the compatibility of
state-of-the-art models with the dataset while preserving the integrity of the Quranic text, leading
to improved retrieval accuracy and more context-aware answers.
Fig. 2. Cross-Language Example of Quranic QA: A question posed in Arabic is translated into English by
using Google Translate API,then used to retrieve relevant passages from the English-translated Quran, and
then translated back into Arabic.

--- Page 6 ---

6
Islam Oshallah et al.
3.3
Model Fine-Tuning
In this study, transformer-based language models were fine-tuned for the Quran QA task, including
BERT-Medium, RoBERTa-Base, DeBERTa-v3-Base, ELECTRA-Large, Flan-T5, Bloom, and
Falcon. These models were pre-trained and fine-tuned on the SQuAD v2 dataset [15] to improve
their ability to handle complex and zero-answer questions. Each model brings unique strengths,
collectively offering a robust solution for question answering. Additionally, a cross-encoder
model was implemented in the study to enhance the way questions and texts interact. The
algorithm was able to increase accuracy and better convey context by evaluating them as a single
input, particularly when it came to recognizing the most significant portions. This methodology
significantly contributed to delivering accurate responses that were also contextually appropriate.
Table 1. Summary of Models Fine-Tuned on SQuAD v2 Dataset (all models fine-tuned on SQuAD v2)
Model
Number of Parameters Overview
BERT-Medium
86 million
Compact transformer designed for perfor-
mance and efficiency [20]
RoBERTa-Base
125 million
Optimized for natural language understand-
ing tasks [21]
DeBERTa-v3-Base
220 million
Enhances BERT and RoBERTa with disen-
tangled attention [22]
ELECTRA-Large
335 million
Efficient training method using a generator-
discriminator architecture [23]
Bloom
7 billion
Large transformer model supporting a wide
range of languages [24]
Falcon
7 billion
Designed for complex, context-dependent
query handling [25]
Flan-T5
11 billion
Instruction-tuned for a variety of NLP tasks,
including translation and question answering
[26]
3.4
Explanation of the Workflow Diagram
Figure 3 illustrates the complete workflow for fine-tuning and retrieval tasks in our Quran QA
system. The diagram shows how the input question (Q-Text) is processed along with positive
(relevant) and negative (non-relevant) passages to generate the final answer during the fine-tuning
phase.
1. Question-Text (Q-Text): In the training phase, the input question is provided as part of the
dataset. This is a question from the dataset that the model is being trained to answer from the
Quranic passages.
2. Positive and Negative Passages: The system uses passages from the Quran that are either
relevant (positive passages) or irrelevant (negative passages) to the given question. These passages
are labeled with "1" indicating relevance and "0" indicating irrelevance during training. This helps
the model learn how to find relevant passages and handle context-dependent or ambiguous queries
from the Quranic text.

--- Page 7 ---

Quran QA
7
Q-Text
Positive passages
Text
Relevance
Passage1
1
Passage3
1
...
1
Negative passages
Text
Relevance
Passage6
0
Passage14
0
...
0
Randomizer
Combined Data for each question
Text
Relevance
Passage3
1
Passage6
0
...
...
LLM & LM using Cross-Encoder
LLM & LM Output
Retrieval
Test Cases
Answers
Passage2
Passage5
Passage9
...
Fig. 3. Workflow for LLM & LM training
3. Randomizer and Combined Data: The system combines both positive and negative
passages using a randomizer . After mixing positive and negative passages with a randomizer,
contrastive learning could further help the model by creating training pairs. Each pair would
be evaluated to ensure that the model distinguishes between relevant and irrelevant passages
effectively. This would enhance the ability of the model to prioritize relevant passages over
irrelevant ones, improving retrieval performance.
4. Cross-Encoder Fine-Tuning: The combined data, along with relevant labels, is passed
into a language model and large language model using a cross-encoder architecture to understand
the context-dependent or ambiguous queries from the Quranic text. Models like RoBERTa-Base,
DeBERTa-v3-Base, ELECTRA-Large, Flan-T5, Bloom, Falcon, and BERT-Medium have been
fine-tuned using the Quran QA dataset. While these models are fine-tuned on other datasets like
squad, then undergo specific fine-tuning for this task to better retrieve the most relevant passages
when answering questions.
5. LLM & LM Output and Retrieval: The fine-tuned model generates output in the form of
relevance scores for each passage based on its understanding of the relationship between the input
question and the passages.These scores are then used to rank the passages, with the highest ranked
ones selected to provide the best and most relevant answers which led to an increase in the ability
to deal with context-dependent or ambiguous queries from the Quranic text.
4
Results
The evaluation results show the impact of dataset expansion, cross language, and model fine-tuning
on enhancing the performance of QA systems for the Holy Quran. Multiple models evaluated on
metrics such as MAP10 (Mean Average Precision at 10), MRR (Mean Reciprocal Rank), Recall
at top 5 and 10 passages (Rec5, Rec10), and Precision for the same ranks (Pre5, Pre10). The

--- Page 8 ---

8
Islam Oshallah et al.
Model
MAP10
MRR
Rec5
Rec10
Pre5
Pre10
Base Ours Base Ours Base Ours Base Ours Base Ours Base Ours
Electra-Large
0.04 0.31 0.11 0.43 0.05 0.34 0.08 0.46 0.05 0.21 0.04 0.19
Bloom
0.04 0.14 0.14 0.24 0.07 0.25 0.15 0.29 0.07 0.14 0.07 0.10
Flan-T5
0.01 0.26 0.07 0.35 0.01 0.33 0.08 0.38 0.02 0.20 0.03 0.14
Falcon
0.03 0.26 0.10 0.40 0.05 0.32 0.08 0.40 0.04 0.20 0.04 0.12
Roberta-Base
0.10 0.34 0.22 0.52 0.19 0.36 0.25 0.43 0.13 0.22 0.12 0.20
Bert-Medium
0.07 0.27 0.17 0.39 0.09 0.35 0.23 0.40 0.10 0.20 0.08 0.18
Deberta-v3-Base 0.08 0.32 0.12 0.47 0.10 0.46 0.15 0.50 0.09 0.25 0.08 0.24
Table 2. Comparison of multiple model versions based on MAP10, MRR, Recall, and Precision evaluation
metrics. The table highlights the improvements achieved by the fine-tuned models (Ours) compared to their
baseline (Base) across the evaluation metrics.
table highlights the highest improvements achieved by fine-tuning . Noticed observations are:
– Electra-Large achieved the highest improvements, with MAP10 improving from 0.04 to 0.31
and MRR from 0.11 to 0.43, Reflecting better ranking of relevant passages.
– Roberta-Base showed strong baseline performance and achieved further improvements after
fine-tuning, with MAP@10 increasing from 0.10 to 0.34 and MRR enhancing from 0.22 to
0.52.
All models showed consistent improvements in Recall (Rec5, Rec10) and Precision (Pre5,
Pre10), with DeBERTa-v3-Base achieving the best results, scoring 0.46 and 0.50 in Recall
(Rec5, Rec10) and 0.25 and 0.24 in Precision (Pre5, Pre10), respectively.
This detailed comparison highlights the effectiveness of expanding the dataset,cross language
and fine-tuning the models, showing how these improvements help QA systems better retrieve and
rank Quranic passages.
5
Conclusion
This study addresses the unique challenges of Quranic QA systems by adopting a cross-language
approach to reduce the linguistic difference between Modern Standard Arabic questions and
Classical Arabic Quranic texts. By enhancing the dataset with techniques like machine translation,
paraphrasing, and adding more varied question sets, and by fine-tuning both language models and
large language models, this work achieved improvements in performance. Notably, RoBERTa-Base
demonstrated the best MAP@10 (0.34) and MRR (0.52), while DeBERTa-v3-Base excelled
in Recall@10 (0.50) and Precision@10 (0.24). These results underscore the effectiveness of
cross-language strategies in overcoming linguistic barriers and enhancing Quranic QA systems.
Future research will focus on further expanding dataset diversity, exploring alternative fine-tuning
strategies, Fine-tuning multilingual models to improve accuracy and generalizability. This work
lays a foundation for more accessible and robust Quranic QA systems, allowing users worldwide
to engage more deeply with the Holy Quran.
References
1. Ali, A.Y.: The Holy Qur’an. Wordsworth Editions (2000)

--- Page 9 ---

Quran QA
9
2. Almelhes, S.: Enhancing Arabic language acquisition: Effective strategies for addressing non-native
learners’ challenges. Education Sciences 14(10), 1116 (2024). MDPI AG
3. Saeed, A.: Interpreting the Qur’an: Towards a Contemporary Approach. Taylor & Francis (2006)
4. Kadhim, B.J., Merzah, Z., Ali, M.M., et al.: Translatability of the Islamic terms with reference to
selected Quranic Verses. International Journal of Linguistics, Literature and Translation 6(5), 19–30
(2023)
5. Malhas, R., Mansour, W., Elsayed, T.: Qur’an QA 2023 Shared Task: Overview of Passage Retrieval and
Reading Comprehension Tasks over the Holy Qur’an. In: Proceedings of ArabicNLP 2023, pp.
690–701, Singapore (Hybrid). Association for Computational Linguistics (2023)
6. Essam, M., Deif, M., Elgohary, R.: Deciphering arabic question: A dedicated survey on arabic question
analysis methods, challenges, limitations and future pathways. Artificial Intelligence Review 57(9),
1–37 (2024)
7. Qamar, F., Latif, S., Latif, R.: A benchmark dataset with larger context for non-factoid
question-answering over islamic text. Preprint submitted to Elsevier (2024)
8. Essam, M., Deif, M.A., Attar, H., Alrosan, A., Kanan, M.A., Elgohary, R.: Decoding Queries: An
In-Depth Survey of Quality Techniques for Question Analysis in Arabic Question Answering Systems.
IEEE Access (2024). IEEE
9. Elkomy, M., Sarhan, A.: Tce at qur’an qa 2023 shared task: Low resource enhanced transformer-based
ensemble approach for qur’anic qa. In: Proceedings of ArabicNLP 2023, pp. 728–742. Association for
Computational Linguistics, Singapore (Hybrid) (2023)
10. Aljamel, A., Khalil, H., Aburawi, Y.: Comparative study of fine-tuned bert-based models and rnn-based
models. case study: Arabic fake news detection. The International Journal of Engineering and
Information Technology (ĲEIT) 12(1), 56–64 (2024)
11. Liu, Z., Li, Y., Chen, N., Wang, Q., Hooi, B., He, B.: A survey of imbalanced learning on graphs:
Problems, techniques, and future directions. arXiv preprint arXiv:2308.13821 (2023)
12. Mahmoudi, G., Eetemadi, S., Morshedzadeh, Y.: A multi-task transfer learning approach for
qur’an-related question answering. In: Proceedings of the First Arabic Natural Language Processing
Conference (ArabicNLP 2023). ACL Anthology (2023)
13. Alawwad, H., Alawwad, L., Alharbi, J., Alharbi, A.: Ahjl at qur’an qa 2023 shared task: Enhancing
passage retrieval using sentence transformer and translation. In: Proceedings of ArabicNLP 2023, pp.
702–707 (2023)
14. Pavlova, V.: Leveraging Domain Adaptation and Data Augmentation to Improve Qur’anic IR in English
and Arabic. In: Proceedings of ArabicNLP 2023, pp. 76–88 (2023)
15. Rajpurkar, P., Jia, R., Liang, P.: Know What You Don’t Know: Unanswerable Questions for SQuAD.
Huggingface (2018). URL https://huggingface.co/datasets/rajpurkar/squad_v2
16. Ashor, Q.: 1000 QAs from the Holy Qur’an. Noor Book (2023). URL
https://quranpedia.net/book/451/1/259
17. GARDEN, Q.B.: List of plants citation in quran and hadith v5.pdf (2024)
18. M-AI-C.: Quran English Translations. Huggingface Repository. URL https://huggingface.co/
datasets/M-AI-C/quran_en_translations/viewer/default/train?p=62. Accessed: [date]
19. Ali, A.R., Siddiqui, M.A., Algunaibet, R., Ali, H.R.: A large and diverse Arabic corpus for language
modeling. Procedia Computer Science 225, 12–21 (2023). Elsevier
20. Devlin, J., Chang, M.W., Lee, K., Toutanova, K.: Bert: Pre-training of deep bidirectional transformers
for language understanding. In: Proceedings of the 2019 Conference of the North American Chapter of
the Association for Computational Linguistics: Human Language Technologies, pp. 4171–4186.
Association for Computational Linguistics (2019). URL https://aclanthology.org/N19-1423/
21. Liu, Y.: Roberta: A robustly optimized bert pretraining approach. arXiv preprint arXiv:1907.11692 364
(2019).
22. He, P., Liu, X., Gao, J., Chen, W.: Deberta: Decoding-enhanced bert with disentangled attention. arXiv
preprint arXiv:2006.03654 (2020).

--- Page 10 ---

10
Islam Oshallah et al.
23. Clark, K.: Electra: Pre-training text encoders as discriminators rather than generators. arXiv preprint
arXiv:2003.10555 (2020). URL https://arxiv.org/abs/2003.10555
24. Workshop, BigScience and Scao, T.L., Fan, A., Akiki, C., Pavlick, E., Ilić, S., Hesslow, D., Castagné, R.,
Luccioni, A.S., Yvon, F., et al.: Bloom: A 176b-parameter open-access multilingual language model.
arXiv preprint arXiv:2211.05100 (2022).
25. Almazrouei, E., Alobeidli, H., Alshamsi, A., Cappelli, A., Cojocaru, R., Debbah, M., Goffinet, É.,
Hesslow, D., Launay, J., Malartic, Q., et al.: The Falcon series of open language models. arXiv preprint
arXiv:2311.16867 (2023). URL https://arxiv.org/abs/2311.16867
26. Raffel, C., Shazeer, N., Roberts, A., Lee, K., Narang, S., Matena, M., Zhou, Y., Li, W., Liu, P.J.:
Exploring the limits of transfer learning with a unified text-to-text transformer. Journal of machine
learning research 21(140), 1–67 (2020).

```
