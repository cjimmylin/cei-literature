---
title: "Optimized Quran Passage Retrieval Using an - PDF Extract"
source_pdf: "2024-Basem-Optimized Quran Passage Retrieval Using an.pdf"
pages: 12
extracted_at: "2026-01-24T17:05:26.993860"
---

# PDF Extract: Optimized Quran Passage Retrieval Using an

**Source PDF:** 2024-Basem-Optimized Quran Passage Retrieval Using an.pdf
**Total Pages:** 12

---

## Content

```
--- Page 1 ---

Optimized Quran Passage Retrieval Using an
Expanded QA Dataset and Fine-Tuned Language
Models
Mohamed Basem, Islam Oshallah, Baraa Hikal, Ali Hamdi, and Ammar
Mohamed
Faculty of Computer Science, MSA University, Egypt
{mohamed.basem1, islam.abdulhakeem, baraa.moaweya, ahamdi,
ammohammed}@msa.edu.eg
Abstract. Understanding the deep meanings of the Qur’an and the
bridge the language gap between modern standard Arabic and classi-
cal Arabic is essential to improve the question-and-answer system for
the Holy Qur’an. The Qur’an QA 2023 shared task dataset had limited
number of questions with weak model retrieval. To address this chal-
lenge, this work was done to update the original dataset and improve
the model accuracy. The original dataset which contains 251 questions
was reviewed and expanded to 629 questions with questions diversifi-
cation and reformulation, leading to a comprehensive set of 1895 cat-
egorized into single-answer, multi-answer, and zero-answer types. Ex-
tensive experiments fine-tuned transformer models, including AraBERT,
RoBERTa, CAMeLBERT, AraELECTRA, and BERT. The paper best
model, AraBERT-base, achieved a MAP@10 of 0.36 and MRR of
0.59, representing improvements of 63% and 59%, respectively, compared
to the baseline scores (MAP@10: 0.22, MRR: 0.37). Additionally, the
dataset expansion led to improvements in handling” no answer” cases,
with the proposed approach achieving a 75% success rate for such
instances, compared to the baseline’s 25%. These results demonstrate
the effect of dataset improvement and model architecture optimization in
increasing the performance of QA systems for Holy Qur’an, with higher
accuracy, recall, and precision.
Keywords: Quran Question Answering, Passage Retrieval, Modern Stan-
dard Arabic
1
Introduction
In context of expanding the number of Muslim populations worldwide (2.04 billion
in 2024), there Is a growing demand for understanding the holy Quran through a
reliable question-answering (QA) system capable of providing exact explanations
and answers from the Qur’an [9]. In recent years, the Qur’an QA 2023 shared
task dataset has highlighted the complexity of this task, as previous methods
have shown limited accuracy in retrieving relevant Qur’anic verses [19]. Many
arXiv:2412.11431v1  [cs.CL]  16 Dec 2024

--- Page 2 ---

2
Authors Suppressed Due to Excessive Length
traditional QA models face difficulties with the linguistic nuances of Classical
Arabic and the specificity required in Holy Qur’an [10]. the study of this work
builds upon this challenge by expanding the existing dataset and employing
advanced language models to improve retrieval accuracy [9]. The contributions
in this paper are as follows:
– Dataset Manipulation and Expansion: We expanded the original QA
dataset by generating new questions through rephrasing and categorization,
resulting in a significantly larger and more diverse set of 1895 questions.
– Accurate Language Model Fine-Tuning: We fine-tuned multiple trans-
former models on the expanded dataset, achieving notable improvements in
passage retrieval accuracy, particularly with the AraBERT-large model.
The layout of this article is outlined in the following manner: Section 1 explore into
the reasons and importance of improving Qur’anic question-answering systems.
Section 2 gives a summary of previous research, outlining major progress and
obstacles in the area. In Section 3, The research methodology is described,
including data collection, expanding the dataset, cleaning the data, and finetuning
the language model. The setup utilized to assess model performance is explained in
Section 4’s experimental design. Section 5 highlights and discusses the outcomes of
experiments are presented, showcasing the efficiency of the method. In conclusion,
Section 6 of the paper presents suggestions for upcoming studies.
2
Related Work
The field of question answering (QA) for Holy Qur’an, specifically Qur’anic
passage retrieval, has attracted a lot of attention from researchers because of the
distinct linguistic and contextual difficulties presented by the Qur’an [21]. The
task requires accurately retrieving relevant verses to answer both factoid and
non-factoid questions, often requiring systems to bridge the linguistic gap be-
tween Modern Standard Arabic (MSA) and Classical Arabic [20]. Additionally,
systems must be able of recognizing questions that have no answers within the
Qur’anic text, thereby requiring strong mechanisms for zero-answer scenarios [25].
The development of effective QA systems for Holy Qur’an remains a challenging
endeavor, as the richness of the Arabic language and the need for contextual
understanding demand advanced modeling techniques [14].
Transformer-based language models, such as AraBERT, CAMeLBERT, and Ara-
ELECTRA, have shown promise in handling Arabic language tasks [2]. However,
existing models often struggle with limitations stemming from insufficient and
imbalanced training datasets, which impact the models’ ability to generalize effec-
tively to unseen queries [18,12,13]. The Qur’an QA 2023 shared Task, for example,
highlighted the necessity of utilizing external resources and data augmentation
strategies to improve performance. Sarhan and Elkomy [9] addressed these chal-
lenges by leveraging ensemble learning techniques, combining dual-encoder and
cross-encoder architectures, and employing transfer learning on external datasets
such as TyDI-QA and tafseer. Their ensemble strategy improved prediction

--- Page 3 ---

Quran QA
3
stability and effectiveness, achieving a MAP score of 25.05% for passage retrieval.
Despite these advancements, their study underscored the persistent need for
dataset expansion and more robust fine-tuning approaches to tackle the linguistic
complexities of Qur’anic QA tasks [9].
The work of Alawwad et al [1] focused on enhancing Qur’anic passage retrieval
through the use of pre-trained models fine-tuned on specialized datasets like
Tafseer and TyDI-QA [6]. They merged thresholding mechanisms to manage
unanswerable questions and demonstrated the benefits of ensemble learning for
improving performance in low-resource settings. Although their approach showed
considerable success, achieving improved performance metrics, it also pointed to
the critical role of dataset quality and quantity in achieving consistent model
accuracy. The limitations of existing datasets and the models’ dependency on ex-
ternal resources highlight the need for further dataset expansion and optimization
strategies. Mahmoudi et al [19] proposed a multi-task transfer learning approach
that employs models like AraElectra and AraBERT, utilizing both unsupervised
and supervised fine-tuning to adapt to the Qur’anic context. They implemented
tech-niques like TSDAE and SimCSE to produce top-notch sentence embeddings,
greatly improving the models’ ability in reading comprehension and passage
retrieval. Their study showed that custom sentence embeddings and thorough
model fine-tuning can result in actual enhancements. Nonetheless, the study also
emphasized that further advancements require larger and more diverse datasets
to fully Understand the complexities of the language and context of the Quran.
This work builds on these prior efforts by addressing the pressing need for dataset
expansion and more effective model fine-tuning [27]. A significant increase was
achieved the size of the Qur’an QA dataset from 251 to 1895 questions, employing
strategic question rephrasing to improve data diversity and model robustness
[26]. The proposed approach involves extensive experimentation with multiple
transformer- based models, including AraBERT, CAMeLBERT, and AraElectra,
fine-tuning them on this enriched dataset. By doing so, the aim of this work is to
enhance the models’ ability to handle complex queries, manage zero-answer cases,
and improve overall passage retrieval accuracy, contributing to the advancement
of QA systems for Holy Qur’an [1].
3
Research Methodology
This section details the structured process followed to create and improve the
dataset utilized in Qur’anic Question Answering (QA) systems. The methodology
includes key phases: data collection, dataset expansion, data cleaning, and model
fine-tuning. Each phase is thoroughly designed to ensure the quality, reliability,
and efficacy of the dataset, establishing a strong foundation for robust QA
performance (see Figure 1).

--- Page 4 ---

4
Authors Suppressed Due to Excessive Length
Old Dataset
174 Q Train
52 Q Test
25 Q Development
Tafseer
TYDI QA
New Dataset
1895 Q Train
52 Q Test
25 Q Development
Tafseer
TYDI QA
LM
FineTuning
Question
Answer
Samples
DS Manipulation
Fig. 1. Architecture Diagram: The workflow for dataset expansion and model fine-
tuning. The old dataset is manipulated to create a larger set, which is then fed into
various Language Modelss for fine-tuning, resulting in improved question-answer pairs.
3.1
Data Collection
The dataset was collected from various trustworthy sources to provide a wide
range of questions and related Qur’anic verses. The aim was to gather reli-
able data of high quality to increase the dataset’s scope and improve the QA
model’s capability to handle diverse question-answer pairs. The initial dataset
was expanded significantly by integrating data from the following sources:
– Quran QA 2022 Dataset: This foundational dataset, available on GitHub
and curated by Mohammed Elkomy, was used for initial experiments [8]. It
features structured questions and annotated Qur’anic passages, focusing on
both factoid and non-factoid queries.
– Kaggle Dataset: The”Quran QA” dataset from Kaggle provided additional
questions and corresponding passages, enriching the dataset’s diversity [22].

--- Page 5 ---

Quran QA
5
– Tafseer Book PDF: the new dataset was increased by using 1000 Questions
and Answers in the Holy Quran, a Tafseer-based resource. Relevant question-
passage pairs were meticulously extracted and cleaned to ensure high-quality
integration [5].
– Hugging Face Datasets:: two key datasets were used from Hugging Face:
• Quran-TafseerBook Dataset by Mohamed Rashad, featuring classical
Tafseer texts [24].
• Quran-Classical-Arabic-English Parallel Texts by ImruQays, offering par-
allel translations for enriched linguistic context [15].
– List of Plants Citation in Quran and Hadith: This resource from
the Qur’anic Botanic Garden provided context-specific references to plants
mentioned in the Qur’an and Hadith, adding another dimension to the dataset
[11].
3.2
Dataset Expansion
To enhance the dataset, the original dataset was manipulated 251-question dataset
by rephrasing and generating additional questions, ultimately expanding it to
629 questions. All of these questions were rephrased twice, resulting in a robust
dataset of 1895 questions, which categorized into single-answer, multi-answer,
and zero-answer types. This process is illustrated in Figure 1, which shows
the transformation of the old dataset through” DS Manipulation” into a more
comprehensive version that feeds into language models (Language Models) for
fine- tuning. The expanded dataset enabled us to adjust multiple pre-trained
transformers models, with a focus on enhancing performance on Qur’anic passage
retrieval [23]. By varying the phrasing, the dataset’s ability was improved by
train models that are more flexible and effective in handling different question
formats and vocabulary, ultimately enhancing generalization and performance in
QA tasks.
Fig. 2. A sample from shared task A. We retrieve the most relevant Qur’anic segment

--- Page 6 ---

6
Authors Suppressed Due to Excessive Length
3.3
Data Cleaning
A rigorous data cleaning process was applied to ensure consistency and reliability:
– Duplicate Removal: All duplicate questions and passages were identified
and eliminated to maintain dataset integrity.
– Formatting Standardization: The text was normalized to make sure that
queries were in Modern Standard Arabic (MSA) and Qur’anic verses were in
Classical Arabic. This consistency makes model training more effective and
enhances semantic matching.
3.4
Language Model Fine-Tuning
Fine-tuning pre-trained language models is a essential element of this study, as it
greatly improves the model’s capability to correctly recognize and understand
Qur’anic verses when answering questions in Modern Standard Arabic (MSA).
Several advanced transformer models have been modified to address the complex
language structure and semantic complexity of the ‘Quran. the models were
enhanced using a larger dataset of 1,895 different questions. This dataset is
crafted to encompass diverse linguistic expressions while preserving the intended
meaning of each question. A diverse set of models was selected for fine-tuning,
each offering unique strengths that contribute to overall performance. These
models include AraBERT-base, AraBERT-large, CAMeLBERT, AraELECTRA,
Roberta-base, and BERT, all of which have demonstrated efficacy in processing
Arabic language tasks but required careful adaptation to the context of Qur’anic
QA. Here, fine-tuning process was described and the specific modifications for
each model:
1. AraBERT-base and AraBERT-large [3] are transformer-based models that
have been pre-trained in a large Arabic text corpus. The Ara-BERT base
model is characterized by 12 layers and 768 hidden units, while the Ara-BERT
large model has a more complex architecture of 24 layers and 1024 hidden
units. Both models were fine-tuned using the enhanced dataset, with an
emphasis on improving their capacity to manage intricate sentence structures
and to grasp the profound meanings embedded in Qur’anic verses. Notably,
AraBERT-large showed significant advancements in semantic matching and
in identifying instances where there is” no answer” largely due to the larger
dataset utilized in its training.
2. CAMeLBERT [16]: CAMeLBERT is another Arabic-specific language model
that has been trained on a balanced dataset covering diverse Arabic dialects
and MSA. CAMeLBERT was finetuned to leverage its robust language un-
derstanding capabilities, especially for questions requiring context sensitive
retrieval. The model was further optimized to address the stylistic and gram-
matical differences between MSA and Classical Arabic, which are prevalent
in the Qur’an.
3. AraELECTRA [4]: AraELECTRA employs a discriminative pre-training
method, focusing on distinguishing real tokens from replaced ones. This model

--- Page 7 ---

Quran QA
7
has shown particular strength in tasks requiring a fine-grained understanding
of token-level semantics. During fine-tuning, AraELECTRA was adopted
to new dataset, enhancing its ability to accurately detect the presence or
absence of relevant verses and improve performance on questions where subtle
word choices determine the answer.
4. Roberta-base [17]: Although Roberta-base is a general-purpose transformer
model, it has been adapted for Arabic NLP tasks through extensive pre-
training on large texts. Roberta-base was finetuned to improve its passage
retrieval capabilities, focusing on optimizing attention mechanisms to better
capture relationships between questions and Qur’anic text. The model’s
effectiveness was optimized in accurately ranking relevant verses by optimizing
hyperparameters and adjusting training procedures.
5. BERT [7]: The BERT model serves as a foundational architecture for many
NLP tasks. A finetuned version of BERT that had previously been trained
on the Squad dataset and then readapted it for Qur’anic question answering.
This step involved focusing on span prediction capabilities, which are critical
for extracting precise answers from passages. Fine-tuning BERT on enriched
dataset allowed to leverage its deep contextual understanding to handle
questions with complex or ambiguous phrasing.
Overall, the fine-tuning process involved extensive experimentation with different
hyperparameters, including learning rates, batch sizes, and training epochs, to
achieve optimal performance. In this work intensive evaluation procedures were
implemented to ensure that each model was capable of not only retrieving accurate
answers but also recognizing cases where no relevant answer existed in the Quran
(zero answer questions). Additionally, various techniques were integrated such
as dropout regularization and gradient clipping to improve model stability and
generalization. The outcome of this comprehensive fine-tuning approach is a set
of highly specialized models that are well-equipped to handle the linguistic and
contextual challenges inherent in Qur’anic QA.
4
Experimental Design
This paper experimental design involves fine-tuning several pre-trained Arabic
Language Models to tackle the tasks of Question Answering (QA) and Passage Re-
trieval (PR) in the context of Qur’anic texts. These models, including AraBERT,
CAMeLBERT, BERT, Roberta, and AraELECTRA, have been adapted to better
address the unique linguistic and semantic challenges presented by the Qur’an.
The fine-tuning process, utilizes expanded dataset of 1895 questions derived from
an initial set of 251 questions.
Transfer learning was employed to enhance model performance, leveraging the
pre-trained knowledge of each model and adapting it through a targeted fine-
tuning process. Moreover, implement ensemble learning techniques, combining
predictions from multiple fine-tuned models. This approach improves overall
answer accuracy and robustness by leveraging the strengths of each model while
mitigating individual weaknesses. Furthermore, a thresholding mechanism was

--- Page 8 ---

8
Authors Suppressed Due to Excessive Length
used to filter out low-confidence predictions, effectively managing zero-answer
cases by discarding uncertain or ambiguous results. The evaluation framework
uses the following metrics to measure model performance:
– Mean Average Precision (MAP): Measures the precision of each rank
position and compares it to the average in all queries, allowing a complete
ranking quality assessment.
– Mean Reciprocal Rank (MRR): Assesses the position of the first useful
responses in the result list and indicates how well the model finds the correct
answer.
– Recall:Measures such as recall@5 and recall@10 are used to evaluate the
effectiveness of the model in capturing relevant information in the highest
rankings.
5
Results and Discussion
The evaluation results indicate that fine-tuning various pre-trained models signif-
icantly enhanced the performance metrics for question answering and passage
retrieval tasks. This section discusses the results presented in Tables 1 ,2 and 3.
Table 1 compares the Mean Average Precision (MAP@10) and Mean Recip-
rocal Rank (MRR) measurements of each model before and after adjustment.
AraBERT-base the most notable improvement was MAP@10, which increased
from 0.22 to 0.36, and MRR, from 0.37 to 0.59. These findings indicate that the
retrieval accuracy and ranking accuracy have improved significantly, and show
that the model has improved its ability to effectively capture relevant passages.
The Roberta model, moderate improvements (MAP@10 was 0.05 to 0.12, MRR
was 0.01 to 0.17), but it benefited from fine tuning. AraBERT-large remained
relatively stable, with only slight increases in MAP@10 and MRR, suggesting
that the model was already well-tuned for these tasks or required additional mod-
ifications for further improvements. CAMeLBERT-base and AraELECTRA-
base demonstrated balanced enhancements, with moderate improvements in
both metrics. BERT-squad-accelerate, on the other hand, achieved significant
progress, with MAP@10 increasing from 0.07 to 0.25 and MRR from 0.12 to 0.40,
highlight the importance of dataset expansion and fine-tuning approach.
Table 2 illustrates the recall performance of various models at different cut-off
points. AraBERT-base demonstrated a notable improvement in recall metrics,
with Recall@5 increasing from 0.25 to 0.37 and recall@100 rising from 0.30 to 0.50.
This indicates a stronger capacity for the model to retrieve relevant passages in
the top ranks. In contrast, Roberta showed limited enhancements, with Recall@5
improving only from 0.10 to 0.18, suggesting potential challenges in grasping
the nuances of Qur’anic text. The AraBERT-large model exhibited moderate
improvements across recall metrics, with Recall@5 moving from 0.31 to 0.34 and
maintaining consistent performance in other recall metrics. CAMeLBERT-base
achieved strong results, improving Recall@5 from 0.32 to 0.36 and showing po-
tential in handling more complex queries, while AraELECTRA- base displayed

--- Page 9 ---

Quran QA
9
significant gains, especially in Recall@15, with an increase from 0.42 to 0.57.
BERT-squad-accelerate maintained stable recall values at lower cut-off points
but significantly performed better in handling unanswerable questions, as showed
by a No Answer Recall of 0.75, up from 0.25. This highlights its effectiveness
in addressing queries without clear answers. Table 3 presents precision metrics
across various cut-off points. AraBERT- base showed significant improvements,
with Precision@5 rising from 0.18 to 0.25 and Precision@100 increasing from
0.01 to 0.06. These enhancements underscore the model’s effectiveness in accu-
rately identifying relevant passages. Roberta showed only small improvement in
precision, with Precision@5 moving from 0.05 to 0.10, which corresponds with
its overall average performance. Both AraBERT- large and CAMeLBERT-base
demonstrated improved precision, particularly at higher cut-off points, indicating
their ability to deliver more relevant results, with CAMeLBERT-base achieving
Precision@5 of 0.27 compared to its base score of 0.23. The AraELECTRA-base
model displayed balanced precision gains, showing a notable increase from 0.21
to 0.30 at Precision@5.
Meanwhile, BERT-squad- accelerate excelled in handling no-answer scenarios,
attaining a No Answer Precision of 0.75, significantly higher than its base score
of 0.25, highlighting its strength in addressing unanswerable questions.
Overall, the results underscore the importance of model architecture and dataset
expansion in enhancing the performance of QA systems for Holy Qur’an. The use
of ensemble learning and thresholding mechanisms contributed to the robustness of
using these models, particularly in managing zero-answer cases. Future work could
explore optimizing specific model architectures further and integrating additional
data sources to enhance semantic understanding and retrieval performance.
Table 1. Comparison of multiple model versions based on MAP@10 and MRR evaluation
metrics.
Model
MAP@10
MRR
Baseline Ours Baseline Ours
AraBERT-base
0.22
0.36
0.37
0.59
Roberta
0.05
0.12
0.01
0.17
AraBERT-large
0.28
0.28
0.40
0.42
Camelbert-Base
0.32
0.34
0.45
0.47
Araelectra-Base
0.21
0.33
0.29
0.45
bert-squad-accelerate
0.07
0.25
0.12
0.40

--- Page 10 ---

10
Authors Suppressed Due to Excessive Length
Table 2. Comparison of multiple model versions based on Recall evaluation metrics.
Overall Recall
R@5
R@10
R@15
R@100
No Answer
Base Ours Base Ours Base Ours Base Ours Base Ours
AraBERT-base
0.25 0.37 0.30 0.50 0.30 0.50 0.30 0.50 0.00
0.25
Roberta
0.10 0.18 0.14 0.30 0.14 0.30 0.14 0.30 0.00
0.25
AraBERT-large
0.31 0.34 0.38 0.40 0.38 0.40 0.38 0.40 0.00
0.25
Camelbert-Base
0.32 0.36 0.46
0.40
0.46
0.40
0.46
0.40
0.25
0.50
Araelectra-Base
0.31 0.49 0.42 0.57 0.42 0.57 0.42 0.57 0.25
0.50
bert-squad-accelerate 0.07 0.32 0.09 0.35 0.09 0.35 0.09 0.35 0.25
0.75
Table 3. Comparison of multiple model versions based on Precision evaluation metrics.
Precision
P@5
P@10
P@15
P@100
No Answer
Base Ours Base Ours Base Ours Base Ours Base Ours
AraBERT-base
0.18 0.25 0.12 0.20 0.08 0.15 0.01 0.06 0.00
0.25
Roberta
0.05 0.10 0.04 0.10 0.02 0.08 0.01 0.05 0.00
0.25
AraBERT-large
0.18 0.20 0.13 0.15 0.09 0.12 0.01 0.05 0.00
0.25
Camelbert-Base
0.23 0.27 0.19 0.20 0.14 0.16
0.05 0.09 0.25
0.50
Araelectra-Base
0.21 0.30 0.18 0.24 0.13 0.18 0.05 0.10 0.25
0.50
bert-squad-accelerate 0.08 0.22 0.06 0.18 0.05 0.17 0.04 0.13 0.25
0.75
6
Conclusion
This study presents an effective approach to improving Qur’anic passage retrieval
in question-answering systems by fine-tuning pre-trained Arabic Language Models
(LMs) on an expanded dataset of 1,895 questions. Models like AraBERT, CAMeL-
BERT,Roberta , AraELECTRA, and BERT ,optimized using transfer learning,
showed improved ability to realize the difficulties of both the Qur’anic text and
user queries. Ensemble learning further boosted accuracy and developments, while
a thresholding mechanism ensured reliable answers and managed zero-answer
cases. The paper results highlight the significance of thorough datasets and
sophisticated model structures in creating strong QA systems for Holy Qur’an,
contributing both to Natural Language Processing research and providing a
valuable resource for Muslims. Future work is recommended to explore additional
data sources and further architectural refinements to address challenges like
semantic understanding and unanswerable queries (zero answers).

--- Page 11 ---

Quran QA
11
7
Acknowledgment
Heartfelt gratitude is extended to AiTech AU, AiTech for Artificial Intelligence
and Software Development (https://aitech.net.au), for funding this research,
providing technical support, and enabling its successful completion.
References
1. Alawwad, H., Alawwad, L., Alharbi, J., Alharbi, A.: Ahjl at qur’an qa 2023 shared
task: Enhancing passage retrieval using sentence transformer and translation. In:
Proceedings of ArabicNLP 2023, pp. 702–707 (2023)
2. Aljamel, A., Khalil, H., Aburawi, Y.: Comparative study of fine-tuned bert-based
models and rnn-based models. case study: Arabic fake news detection. The
International Journal of Engineering and Information Technology (IJEIT) 12(1),
56–64 (2024)
3. Antoun, W., Baly, F., Hajj, H.: Arabert: Transformer-based model for arabic
language understanding. arXiv preprint arXiv:2003.00104 (2020). URL
https://arxiv.org/abs/2003.00104
4. Antoun, W., Baly, F., Hajj, H.: Araelectra: Pre-training text discriminators for
arabic language understanding. In: Proceedings of the Sixth Arabic Natural
Language Processing Workshop, pp. 191–195. Association for Computational
Linguistics (2021). URL https://aclanthology.org/2021.wanlp-1.21/
5. Ashor, Q.: 1000 QAs from the Holy Qur’an. Noor Book (2023). URL
https://quranpedia.net/book/451/1/259
6. Clark, J., et al.: Tydi qa: A benchmark for information-seeking question answering
in typologically diverse languages. Transactions of the ACL (2020)
7. Devlin, J., Chang, M.W., Lee, K., Toutanova, K.: Bert: Pre-training of deep
bidirectional transformers for language understanding. In: Proceedings of the 2019
Conference of the North American Chapter of the Association for Computational
Linguistics: Human Language Technologies, pp. 4171–4186. Association for
Computational Linguistics (2019). URL https://aclanthology.org/N19-1423/
8. Elkomy, M.: Quran qa 2022 dataset (2022). GitHub Repository
9. Elkomy, M., Sarhan, A.: Tce at qur’an qa 2023 shared task: Low resource enhanced
transformer-based ensemble approach for qur’anic qa. In: Proceedings of
ArabicNLP 2023, pp. 728–742. Association for Computational Linguistics,
Singapore (Hybrid) (2023)
10. Essam, M., Deif, M., Elgohary, R.: Deciphering arabic question: A dedicated
survey on arabic question analysis methods, challenges, limitations and future
pathways. Artificial Intelligence Review 57(9), 1–37 (2024)
11. GARDEN, Q.B.: List of plants citation in quran and hadith v5.pdf (2024)
12. Hamdi, A., Shaban, K., Zainal, A.: A review on challenging issues in arabic
sentiment analysis. Journal of Computer Science (2016)
13. Hamdi, A., Shaban, K., Zainal, A.: Clasenti: a class-specific sentiment analysis
framework. ACM Transactions on Asian and Low-Resource Language Information
Processing (TALLIP) 17(4), 1–28 (2018)
14. Hillman, J., Baydoun, E.: Quality assurance and relevance in academia: a review.
Springer (2019)
15. ImruQays: Quran-classical-arabic-english parallel texts dataset on hugging face
(2024). URL https://huggingface.co/datasets/ImruQays/
Quran-Classical-Arabic-English-Parallel-texts

--- Page 12 ---

12
Authors Suppressed Due to Excessive Length
16. Inoue, G., Habash, N.: Camelbert: A language model for arabic. In: Proceedings of
the Sixth Arabic Natural Language Processing Workshop, pp. 270–278.
Association for Computational Linguistics (2021). URL
https://aclanthology.org/2021.wanlp-1.29/
17. Liu, Y., Ott, M., Goyal, N., Du, J., Joshi, M., Chen, D., Levy, O., Lewis, M.,
Zettlemoyer, L., Stoyanov, V.: Roberta: A robustly optimized bert pretraining
approach. arXiv preprint arXiv:1907.11692 (2019). URL
https://arxiv.org/abs/1907.11692
18. Liu, Z., Li, Y., Chen, N., Wang, Q., Hooi, B., He, B.: A survey of imbalanced
learning on graphs: Problems, techniques, and future directions. arXiv preprint
arXiv:2308.13821 (2023)
19. Mahmoudi, G., Eetemadi, S., Morshedzadeh, Y.: A multi-task transfer learning
approach for qur’an-related question answering. In: Proceedings of the First
Arabic Natural Language Processing Conference (ArabicNLP 2023). ACL
Anthology (2023)
20. Malhas, M., et al.: Qur’an qa 2023 shared task: Overview of passage retrieval and
reading comprehension tasks over the holy qur’an. In: ArabicNLP-WS 2023, pp.
1–13. Association for Computational Linguistics (2023)
21. Malhas, R.: Arabic question answering on the holy qur’an. Ph.D. thesis, Ph.D.
thesis (2023)
22. Mobassir: Quran qa dataset on kaggle (2024). URL
https://www.kaggle.com/datasets/mobassir/quranqa/code
23. Qamar, F., Latif, S., Latif, R.: A benchmark dataset with larger context for
non-factoid question-answering over islamic text. Preprint submitted to Elsevier
(2024)
24. Rashad, M.: Quran-tafseerbook dataset on hugging face (2024)
25. Sardar, Z.: Reading the Qur’an: The contemporary relevance of the sacred text of
Islam. Oxford University Press (2017)
26. Sun, L., Xia, C., Yin, W., Liang, T., Yu, P.S., He, L.: Mixup-transformer: Dynamic
data augmentation for nlp tasks. arXiv preprint arXiv:2010.02394 (2020)
27. Zheng, H., Shen, L., Tang, A., Luo, Y., Hu, H., Du, B., Tao, D.: Learn from model
beyond fine-tuning: A survey. arXiv preprint arXiv:2310.08184 (2023)

```
