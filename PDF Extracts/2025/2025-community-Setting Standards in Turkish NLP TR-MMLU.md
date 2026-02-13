---
title: "2025-community-Setting Standards in Turkish NLP TR-MMLU - PDF Extract"
source_pdf: "2025-community-Setting Standards in Turkish NLP TR-MMLU.pdf"
pages: 6
extracted_at: "2026-02-13T09:15:44.825211"
---

# PDF Extract: 2025-community-Setting Standards in Turkish NLP TR-MMLU

**Source PDF:** 2025-community-Setting Standards in Turkish NLP TR-MMLU.pdf
**Total Pages:** 6

---

## Content

```
--- Page 1 ---

arXiv:2501.00593v2  [cs.CL]  4 Jan 2025
Setting Standards in Turkish NLP: TR-MMLU for
Large Language Model Evaluation
M. Ali Bayram1, Ali Arda Fincan2, Ahmet Semih Gümü¸s2,
Banu Diri1, Sava¸s Yıldırım3, Öner Ayta¸s4
1Yıldız Technical University, 2Yeditepe University,
3˙Istanbul Bilgi University, 4I¸sık University
malibayram20@gmail.com
Abstract
Language models have made remarkable advancements in understanding and gen-
erating human language, achieving notable success across a wide array of applica-
tions. However, evaluating these models remains a signiﬁcant challenge, particu-
larly for resource-limited languages such as Turkish. To address this gap, we intro-
duce the Turkish MMLU (TR-MMLU) benchmark, a comprehensive evaluation
framework designed to assess the linguistic and conceptual capabilities of large
language models (LLMs) in Turkish. TR-MMLU is constructed from a carefully
curated dataset comprising 6,200 multiple-choice questions across 62 sections, se-
lected from a pool of 280,000 questions spanning 67 disciplines and over 800
topics within the Turkish education system. This benchmark provides a transpar-
ent, reproducible, and culturally relevant tool for evaluating model performance.
It serves as a standard framework for Turkish NLP research, enabling detailed
analyses of LLMs’ capabilities in processing Turkish text and fostering the devel-
opment of more robust and accurate language models. In this study, we evaluate
state-of-the-art LLMs on TR-MMLU, providing insights into their strengths and
limitations for Turkish-speciﬁc tasks. Our ﬁndings reveal critical challenges, such
as the impact of tokenization and ﬁne-tuning strategies, and highlight areas for
improvement in model design. By setting a new standard for evaluating Turkish
language models, TR-MMLU aims to inspire future innovations and support the
advancement of Turkish NLP research.
Keywords: Large Language Models (LLM), Natural Language Processing (NLP),
Artiﬁcial Intelligence, Turkish NLP
1
Introduction
Advancements in artiﬁcial intelligence (AI) and natural language processing (NLP) have revolution-
ized the ﬁeld of computational linguistics, particularly with the advent of large language models
(LLMs) such as GPT-4, BERT, and Llama. These models, trained on massive datasets, have demon-
strated remarkable capabilities in a diverse range of applications, including machine translation,
question answering, content generation, and even code synthesis. Their integration into real-world
systems has transformed industries, driving innovation and efﬁciency. However, evaluating the true
capabilities of these models remains a persistent challenge, particularly for resource-limited lan-
guages like Turkish, where performance often falls short of human-level comprehension [1].
Existing benchmarks for assessing LLMs predominantly focus on widely spoken languages like En-
glish. While these benchmarks, such as MMLU and SuperGLUE, have provided comprehensive
evaluation frameworks for high-resource languages, they often overlook the unique linguistic com-
plexities of morphologically rich and agglutinative languages like Turkish. Turkish, with its intricate

--- Page 2 ---

morphology and syntactic structure, poses distinct challenges for NLP. For instance, a single Turkish
verb root can generate numerous word forms through sufﬁxation, encoding tense, person, and mood
in a compact yet complex manner. This variability complicates tokenization and semantic parsing,
requiring models to grasp both surface patterns and deep linguistic structures.
To effectively evaluate Turkish NLP models, it is essential to account for these unique features.
Questions derived from Turkey’s education system offer an ideal basis for such assessments. The
education system’s curriculum, with its wide-ranging topics and rich linguistic content, provides a
robust framework for evaluating the depth of knowledge and linguistic capabilities of LLMs. These
questions test not only factual recall but also conceptual understanding, logical reasoning, and cul-
tural context, making them invaluable for benchmarking Turkish language models.
Two core dimensions underpin the evaluation of LLMs: instruction following and knowledge assess-
ment. Instruction following assesses a model’s ability to execute speciﬁc commands, focusing on
adherence to predeﬁned instructions and task completion. In contrast, knowledge assessment exam-
ines a model’s comprehension and understanding, evaluating the breadth and depth of its knowledge
base. While instruction-following tasks are important for practical applications, knowledge assess-
ment provides a more comprehensive evaluation of a model’s linguistic and conceptual capabilities.
For Turkish, where linguistic complexity often obscures semantic nuances, knowledge assessment
is particularly critical for evaluating model performance.
This study emphasizes knowledge assessment as the primary metric for evaluating Turkish LLMs.
By leveraging questions from standardized Turkish exams such as the University Entrance Exami-
nation and the Open Education Faculty (AUZEF) exams, we aim to comprehensively analyze model
performance across a diverse set of topics. These exams, designed to test student proﬁciency across
disciplines, provide a rigorous and culturally relevant benchmark for assessing Turkish NLP models.
The objectives of this study are threefold: 1. To introduce the Turkish MMLU (TR-MMLU) bench-
mark, a comprehensive evaluation framework tailored for Turkish. 2. To analyze the performance of
state-of-the-art LLMs on TR-MMLU, highlighting their strengths and limitations in Turkish-speciﬁc
tasks. 3. To identify critical challenges and opportunities for improving Turkish NLP through tai-
lored approaches such as advanced tokenization and ﬁne-tuning strategies.
In summary, this study seeks to advance Turkish NLP by addressing critical gaps in model evalua-
tion. By leveraging questions grounded in Turkey’s education system, TR-MMLU provides a robust
framework for assessing the linguistic and conceptual capabilities of Turkish LLMs. This bench-
mark not only sets a new standard for evaluating Turkish language models but also paves the way
for future innovations in resource-limited language processing.
2
Related Work
The rapid development of large language models (LLMs) has been accompanied by signiﬁcant ef-
forts to evaluate their performance across various linguistic tasks. Benchmarks and datasets such as
MMLU, SuperGLUE, and SQuAD have been instrumental in assessing comprehension, knowledge
depth, and generative capabilities, primarily in widely spoken languages like English. However,
resource-limited languages, including Turkish, pose unique challenges due to their morphological
richness and syntactic complexity. In response, several benchmarks have been developed speciﬁcally
for Turkish, aiming to address these limitations and provide meaningful evaluations of LLMs.
One of the most comprehensive efforts in Turkish NLP evaluation is TurkishMMLU. This bench-
mark was developed to meet the need for a structured evaluation framework tailored to Turkish
LLMs. The dataset includes questions derived from Turkey’s national curriculum, covering a di-
verse range of subjects designed to assess linguistic, cultural, and conceptual comprehension. Each
question is assigned a difﬁculty rating based on real-world educational performance, enabling nu-
anced assessments of model capabilities. TurkishMMLU has been applied to over 20 models, in-
cluding open-source multilingual LLMs like Llama and MT5, as well as Turkish-adapted models.
The benchmark supports various evaluation paradigms, such as zero-shot, few-shot, and chain-of-
thought reasoning, making it a foundational resource for Turkish NLP research [2].
Additional Turkish-speciﬁc benchmarks include the OpenLLMTurkishLeaderboard and its up-
dated version, OpenLLMTurkishLeaderboard_v0.2.
These benchmarks rely on translated
datasets from widely used English benchmarks such as MMLU, AI2_ARC, and GSM8K. While
2

--- Page 3 ---

these resources provide insights into model performance across a range of tasks, translation-based
benchmarks often fail to capture the linguistic and cultural nuances unique to Turkish. Consequently,
models evaluated on these datasets may exhibit performance inconsistencies when applied to native
Turkish tasks. Nevertheless, studies leveraging these benchmarks have demonstrated the effective-
ness of ﬁne-tuning multilingual models with Turkish-speciﬁc data, highlighting the importance of
language-speciﬁc training to improve performance [3, 4].
The THQuAD dataset, focusing on historical Turkish texts, evaluates reading comprehension tasks
using models such as BERT and ELECTRA. This dataset underscores the challenges inherent to
Turkish NLP, including context-based understanding and the interpretation of nuanced, historically
rooted language. Although THQuAD provides valuable insights into speciﬁc domains, its narrow
focus on historical texts limits its applicability to broader Turkish NLP tasks [5].
In addition to these structured benchmarks, other studies have explored Turkish NLP tasks such
as sentiment analysis, question answering, and language-speciﬁc embeddings. Sentiment analysis
research, in particular, has highlighted the challenges of processing Turkish social media content,
which is often informal and laden with linguistic variations. These efforts underscore the critical
need for culturally aligned, Turkish-speciﬁc datasets to bridge the performance gap between Turkish
LLMs and their English counterparts.
Compared to these existing benchmarks, the Turkish MMLU (TR-MMLU) benchmark offers several
key advancements: - TR-MMLU is natively designed for Turkish, avoiding the translation-related
errors and cultural mismatches often present in multilingual benchmarks. - The dataset encompasses
a wide range of topics, including healthcare, law, history, and the natural sciences, providing a
holistic evaluation framework that reﬂects the linguistic and conceptual diversity of Turkish. - TR-
MMLU evaluates both instruction-following capabilities and knowledge comprehension, enabling a
comprehensive assessment of LLM performance in Turkish.
In summary, while existing benchmarks such as TurkishMMLU, OpenLLMTurkishLeaderboard,
and THQuAD have laid the groundwork for Turkish NLP, they leave critical gaps in terms of lin-
guistic depth and evaluation scope. TR-MMLU addresses these gaps by providing a robust, trans-
parent, and culturally relevant framework tailored to Turkish. By fostering advancements in model
evaluation and development, TR-MMLU sets a new standard for future research and innovation in
Turkish NLP.
3
Task Deﬁnition and Methodology
The primary objective of this study is to establish a robust and comprehensive benchmark for eval-
uating the performance of Large Language Models (LLMs) in the Turkish language. The Turkish
MMLU benchmark (TR-MMLU) was developed using a high-quality dataset of 6,200 multiple-
choice questions spanning 62 categories. These categories encompass diverse ﬁelds such as law,
healthcare, history, and the arts, with questions carefully derived from the Turkish education sys-
tem and other specialized domains. The benchmark aims to provide a standardized and transparent
framework to evaluate the linguistic and conceptual understanding of LLMs, addressing critical gaps
in Turkish NLP research.
TR-MMLU serves three core purposes. First, it evaluates Turkish language performance by objec-
tively measuring LLMs’ comprehension across diverse topics, offering insights into their strengths
and weaknesses. Second, it ensures transparency and reproducibility by making all questions, an-
swers, and evaluation scripts publicly available, allowing independent veriﬁcation of ﬁndings. Third,
it contributes to the Turkish AI ecosystem by identifying gaps in model performance and guiding
the development of accurate and robust Turkish language models.
The importance of TR-MMLU lies in its ability to address speciﬁc challenges faced by Turkish NLP.
Unlike existing multilingual benchmarks, which often rely on translations, TR-MMLU is natively
crafted by curriculum experts in Turkish, ensuring cultural and linguistic relevance while eliminating
errors introduced by translation. Moreover, the dataset is curated to avoid overlap with pre-training
data, enabling unbiased evaluations of model performance. This makes TR-MMLU particularly
effective for assessing models’ ability to process Turkish text independently of prior exposure.
The methodology for TR-MMLU evaluation is designed to ensure consistency and accuracy. A
total of 39 LLMs were evaluated, encompassing open-source models (e.g., Llama, Gemma) and
3

--- Page 4 ---

closed-source models (e.g., GPT-4, Claude). The evaluation process includes controlled hardware
environments to ensure comparable results, with metrics such as accuracy, success rate, and process-
ing time used to assess performance. To address response format variations, paraphrase detection
models are employed to standardize responses and ensure semantic consistency.
Prompt engineering plays a critical role in maximizing the accuracy of model responses. Various
prompt structures were tested, each designed to align with the linguistic characteristics of Turkish
and the capabilities of the evaluated models. Results were analyzed based on the number of cor-
rect answers provided under different prompt conditions, offering insights into the effectiveness of
prompting strategies.
A publicly accessible leaderboard has been created on the Hugging Face platform, ranking models
based on their accuracy and performance metrics. The leaderboard includes detailed information
about each model, such as architecture, parameter size, and quantization level, providing a transpar-
ent view of model capabilities. This ensures that the research community has a reliable reference for
comparing model performance and identifying best practices for Turkish NLP.
TR-MMLU represents a signiﬁcant advancement in Turkish NLP by providing a reliable benchmark
tailored to the unique characteristics of the Turkish language. This benchmark sets a high standard
for evaluating LLMs, offering both researchers and developers a valuable tool to advance the ﬁeld.
By fostering transparency, reproducibility, and collaboration, TR-MMLU lays the groundwork for
future innovations in NLP, particularly for resource-limited languages like Turkish.
4
Experiments and Results
Experiments were conducted on the Ollama platform using a Python script that automated the eval-
uation of 39 large language models (LLMs) on the 6,200 questions in the TR-MMLU dataset. To
ensure reproducibility, all tests were conducted with a ﬁxed seed value of 42. Various prompt struc-
tures tailored to Turkish were employed to maximize response accuracy. Below are some example
prompts used during the evaluation:
Prompt Examples:
• Prompt 1: Sana soru ve seçenekleri veriyorum. Sadece hangi seçene˘gin sorunun do˘gru
cevabı oldu˘gunu yaz. (Translation: I will give you a question and its options. Write only
the correct answer.) Results: gemma2:9b = 63 correct, llama3.1 = 47 correct
• Prompt 2:
Sana çoktan seçmeli soru ve seçeneklerini veriyorum.
Sorunun do˘gru
seçene˘gini bul ve sadece do˘gru seçene˘gin hangi ¸sıkka ait oldu˘gunu söyle. (Translation:
I will give you a multiple-choice question. Indicate which option corresponds to the cor-
rect answer.) Results: gemma2:9b = 60 correct, llama3.1 = 33 correct
• Prompt 3: Sana soru ve seçenekleri veriyorum, sorunun cevabının hangi seçenek oldu˘gunu
bul ve sadece do˘gru seçene˘gin hangi ¸sıkka ait oldu˘gunu söyle.
(Translation: I will
give you a question. Find and indicate the correct option.) Results: gemma2:9b = 58
correct, llama3.1 = 37 correct
• Prompt 4: Sana verece˘gim çoktan seçmeli sorunun sadece do˘gru ¸sıkkının harﬁni söyle.
(Translation: For the question, write only the letter of the correct answer.)
Results:
gemma2:9b = 55 correct, llama3.1 = 36 correct
• Prompt 5: Sana soru ve seçenekleri veriyorum. Sadece hangi seçene˘gin do˘gru oldu˘gunu
yaz. Örne˘gin ’A’ veya ’B’. Lütfen açıklama yapma. (Translation: I will give you a question
and options. Write only the correct option, e.g., ’A’ or ’B,’ without explanation.) Results:
gemma2:9b = 58 correct, llama3.1 = 42 correct
The evaluation results were published on the Hugging Face platform as three distinct datasets:
1. AI Turkish MMLU Leaderboard: This dataset ranks models based on overall perfor-
mance, including metrics such as accuracy, parameter size, quantization level, and process-
ing time. Table 1 summarizes the performance of selected models.
2. AI Turkish MMLU Section Results: This dataset provides detailed performance analyses
across 62 categories, highlighting strengths and weaknesses. Table 2 illustrates the perfor-
4

--- Page 5 ---

mance of select models in key ﬁelds such as the Medical Specialization Examination (TUS)
and Public Personnel Selection Exam (KPSS).
3. AI Turkish MMLU Model Responses: This dataset includes detailed answers from all
models, allowing error analysis and deeper insights into model behavior.
Table 1: AI Turkish MMLU Leaderboard
Model
Family
Param Size
Quantization
Correct Answers
Accuracy (%)
Time (s)
gpt-4o
GPT
Unknown
None
5260
84.84
5021
claude-3.5
Sonnet
Unknown
None
5233
84.40
7379
llama3.3:latest
llama
70.6B
Q4_K_M
4924
79.42
13355
gemini-1.5-pro
Gemini
Unknown
None
4758
76.74
4985
gemma2:27b
gemma2
27.2B
Q4_0
4470
72.10
5506
Table 2: AI Turkish MMLU Section Results (Selected Categories)
Model
General Avg (%)
TUS (%)
KPSS (%)
Driver’s License (%)
AÖF Avg (%)
gpt-4o
84.84
91
74.5
97
84.55
claude-3.5
84.40
88
71.5
96
84.65
llama3.3:latest
79.42
85
66.5
92
79.58
gemma2:27b
72.10
77
60
90
72.57
aya-expanse:32b
70.66
69
55.5
84
70.96
To address variations in response format, a semantic similarity model, “paraphrase-multilingual-
mpnet-base-v2,” was employed. This model computes similarity scores between the generated re-
sponses and correct answers. The highest-scoring option was selected as correct if it semantically
aligned with the ground truth.
The results revealed that models with robust tokenization strategies tailored to Turkish morphol-
ogy consistently outperformed others. Fine-tuned models achieved substantial performance gains,
though challenges such as catastrophic forgetting were observed, where previously acquired knowl-
edge deteriorates during ﬁne-tuning. These ﬁndings underscore the importance of localized datasets
and optimized training strategies.
Expanding TR-MMLU beyond multiple-choice questions to include open-ended tasks, sentiment
analysis, and named entity recognition would further enhance its utility. Additionally, the devel-
opment of diverse, high-quality Turkish datasets remains a critical priority for advancing Turkish
NLP.
5
Conclusion
The evaluation of Turkish large language models (LLMs) using the TR-MMLU benchmark has
revealed several challenges and opportunities for advancing Turkish natural language processing
(NLP). One of the most signiﬁcant challenges is tokenization, particularly given Turkish’s agglu-
tinative structure and complex morphology. Many existing models struggle to effectively process
Turkish tokens, leading to suboptimal accuracy. Future work should focus on developing advanced
tokenization techniques tailored to Turkish, addressing linguistic complexities and enabling more
accurate model representations.
Fine-tuning strategies for Turkish-speciﬁc tasks present another area for improvement. While ﬁne-
tuning on Turkish datasets has proven to enhance performance, it is often accompanied by challenges
such as catastrophic forgetting, where previously learned knowledge degrades during the ﬁne-tuning
process. To mitigate this, future research should explore more robust ﬁne-tuning methodologies that
preserve foundational knowledge while optimizing models for Turkish-speciﬁc tasks.
The limited availability of high-quality Turkish datasets is another barrier to comprehensive model
evaluation and training. Expanding the pool of diverse and ethically sourced Turkish datasets will
not only support ﬁne-tuning but also improve generalizability across various NLP applications. Ad-
ditionally, broadening the TR-MMLU benchmark to include open-ended tasks, sentiment analysis,
named entity recognition, and contextual word embeddings would enable a more holistic evaluation
of Turkish language models and their capabilities.
5

--- Page 6 ---

Model performance discrepancies observed across different categories also highlight the need for
deeper investigations into the underlying causes of these variations. Understanding these discrep-
ancies will clarify the strengths and limitations of Turkish LLMs and provide guidance for targeted
improvements. Such research will enable models to better adapt to the linguistic nuances of Turkish,
enhancing their versatility across different applications.
TR-MMLU represents a pivotal step forward for Turkish NLP, providing a robust and transparent
evaluation framework designed speciﬁcally for the Turkish language. By offering 6,200 multiple-
choice questions derived from the Turkish education system and specialized ﬁelds, this benchmark
serves as an invaluable resource for researchers and developers to objectively measure model perfor-
mance.
The ﬁndings from this study underscore the critical importance of tokenization and language-speciﬁc
ﬁne-tuning. Models equipped with advanced tokenization techniques tailored to Turkish morphol-
ogy consistently achieved higher accuracy. Additionally, ﬁne-tuning with Turkish-speciﬁc data
yielded signiﬁcant performance gains, though with some limitations in maintaining foundational
knowledge. These results highlight the need for tailored approaches in model design and training to
address the unique challenges of Turkish NLP.
As a reliable benchmark emphasizing transparency and reproducibility, TR-MMLU fosters collab-
oration and innovation within the research community. Moving forward, the benchmark aims to
expand its scope beyond multiple-choice questions, incorporating more diverse evaluation tasks to
provide a comprehensive assessment of Turkish LLMs. This will not only enhance the utility of TR-
MMLU but also set new standards for evaluating language models in resource-limited languages.
In conclusion, TR-MMLU is a foundational advancement for Turkish NLP, offering a standard-
ized framework for evaluating language models and guiding future research. By addressing key
challenges such as tokenization, ﬁne-tuning, and dataset availability, and by expanding evaluation
metrics, researchers and developers are encouraged to enhance Turkish language processing tech-
nologies further. These advancements will undoubtedly contribute to setting new benchmarks in the
ﬁeld and drive the development of more robust and versatile Turkish LLMs.
References
[1] D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika, D. Song, and J. Steinhardt. Measuring
massive multitask language understanding. arXiv, abs/2009.03300, 2021.
[2] A. Yüksel, A. Köksal, L. K. ¸Senel, A. Korhonen, and H. Schütze. Turkishmmlu: Measuring
massive multitask language understanding in turkish. 2024. arXiv preprint arXiv:2407.12402.
[3] Mohamad Alhajar. Openllm turkish leaderboard v0.2—a hugging face space by malhajar. (n.d.).
Retrieved October 15, 2024.
[4] E. Dogan, M. E. Uzun, A. Uz, H. E. Seyrek, A. Zeer, E. Sevi, H. T. Kesgin, M. K. Yuce, and
M. F. Amasyali. Türkçe dil modellerinin performans kar¸sıla¸stırması performance comparison
of turkish language models. 2024. arXiv preprint arXiv:2404.17010.
[5] F. Soygazi, O. Ciftci, U. Kok, and S. Cengiz. Thquad: Turkish historic question answering
dataset for reading comprehension. In 2021 6th International Conference on Computer Science
and Engineering (UBMK), pages 215–220, 2021.
6

```
