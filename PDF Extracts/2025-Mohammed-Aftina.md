---
title: "2025-Mohammed-Aftina - PDF Extract"
source_pdf: "2025-Mohammed-Aftina.pdf"
pages: 27
extracted_at: "2026-01-29T13:51:32.039107"
---

# PDF Extract: 2025-Mohammed-Aftina

**Source PDF:** 2025-Mohammed-Aftina.pdf
**Total Pages:** 27

---

## Content

```
--- Page 1 ---

Vol.:(0123456789)
Neural Computing and Applications 
 Neural Computing and Applications
https://doi.org/10.1007/s00521-025-11229-y
ORIGINAL ARTICLE
Aftina: enhancing stability and preventing hallucination 
in AI‑based Islamic fatwa generation using LLMs 
and RAG​
Marryam Yahya Mohammed1   · Sama Ayman Ali1 · Salma Khaled Ali1 · 
Ayad Abdul Majeed3 · Ensaf Hussein Mohamed1,2
Received: 10 December 2024 / Accepted: 26 March 2025 
© The Author(s) 2025, corrected publication 2025
Abstract
Question–answering (QA) systems face considerable challenges when involved in Islamic fatwas due to the com-
plexity and sensitivity of the data. Such problems involve providing accurate and reliable responses, managing 
hallucinations and inaccurate responses, and maintaining the stability of the generated responses. Prior studies 
have concentrated mainly on collecting and preprocessing Islamic datasets or developing retrieval-based QA 
systems, overlooking the precision and reliability required for fatwa issuance. To address this issue, we propose 
a QA approach utilizing advanced retrieval-augmented generation (RAG), which is enhanced by a re-ranker to 
increase response stability, eliminate hallucinations, and prioritize the most appropriate and exact answer. This 
enhancement significantly improves response stability and reduces hallucinations by improving the data used for 
answer generation. We conducted experiments across three setups: (1) base LLM, (2) LLM with RAG, and (3) 
LLM with RAG and re-ranker. The third method of LLM with RAG includes a re-ranker for knowledge retrieval, 
which improves the process and ensures relevant and trustworthy data. This differentiates it from the second 
method, which uses a retrieval model. The Flash re-ranker retrieves the most relevant data, which increases the 
response stability and trustworthiness. Evaluations using BERTScore, hallucination, completeness, and irrel-
evance metrics demonstrated that the third experiment LLM with RAG and re-ranker outperformed other setups, 
providing precise, stable, and dependable answers. This research contributes a robust methodology to improve 
AI-driven fatwa systems, guaranteeing higher precision and trustworthiness in Islamic QA systems.
Keywords  Question–answering · NLP · RAG​ · Re-ranker · LLM
1  Introduction
The application of QA systems to Islamic fatwas presents an essential challenge due to the sophistication and 
sensitivity of religious questions. Regardless of the progress in LLMs and RAG approaches, guaranteeing precise 
and compliant replies in Islamic jurisprudence is crucial. This paper aims to implement a fatwa QA system using 
Marryam Yahya Mohammed, Sama Ayman Ali, Salma Khaled Ali, and Ensaf Hussein Mohamed have contributed 
equally to this work.
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

--- Page 2 ---

	
Neural Computing and Applications
https://doi.org/10.1007/s00521-025-11229-y
RAG with LLMs to generate responses. It addresses the challenges in automating fatwa generation and proposes 
a solution for efficient and accurate automation.
Implementing the fatwa QA faces several challenges that slow its reliability. These challenges are categorized 
into two categories: linguistic and technical problems. These challenges occur from the needs of Islamic juris-
prudence, the sophistication or complexity of the Arabic language, and the limitations of current AI technologies.
1.1  Linguistic challenges
•	 General Language Complexities: Language complexity in QA systems is a notable issue that impacts all lan-
guages. Semantic ambiguity, syntactic variability, and multilingual limitations [1] pose significant challenges 
to Natural Language Understanding (NLU), particularly for languages with complex grammar. These com-
plications make it challenging for LLMs to appropriately understand and respond to Fatwa-related inquiries. 
For instance, the Arabic phrase:
 ﻿هل يجوز الصيام بدون نية؟
(Is fasting valid without intention?) is ambiguous because the ruling depends on the type of fasting (e.g., 
obligatory Ramadan fasting vs. voluntary fasting), requiring contextual clarification.
•	 Arabic Language Complexity: The primary language of Islamic texts is Classical Arabic, which presents mor-
phological and semantic challenges [2]. Arabic’s rich inflectional system complicates NLP models, making it 
difficult for QA systems to analyze fatwa-related questions accurately [3]. For example, the Arabic word:
 ﻿صالة
 may refer to obligatory prayer ( )صالة الفرضor voluntary prayer ( ,)صالة النافلةdepending on the context. 
Similarly,
 ﻿زكاة
( Zakat) can refer to mandatory almsgiving ( )زكاة المالor charity given at the end of Ramadan ( , )زكاة الفطرdem�
)
onstrating how one word can have multiple jurisprudential meanings.
•	 Difference in Dialects: Arabic has numerous dialects, adding another layer of complexity to fatwa-related QA 
systems. These dialectal variations affect how Islamic rulings are phrased and understood [3]. For example, 
consider the difference in asking about prayer shortening during travel:
 ﻿هل تجب الصالة في السفر؟
(Modern Standard)
versus
  هل الزم نصلي وإحنا مسافرين؟
(Egyptian Arabic)
While both sentences mean "Is prayer required during travel?", the dialectal variation can confuse NLP models. 
This emphasizes the need for dialect-aware processing in AI-driven fatwa systems to ensure accurate responses 
for diverse Arabic-speaking users.
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

--- Page 3 ---

Neural Computing and Applications	
https://doi.org/10.1007/s00521-025-11229-y
1.2  Technical challenges
•	 Limitation in the availability of the Dataset: There is a lack of complete datasets especially tailored for Islamic 
fatwa QA systems, as the existing datasets are either small or not publicly available, resulting in limitations 
when training and evaluating [4]. Additionally, most existing datasets focus on Quranic content, creating a 
resource gap for other types of Islamic texts, such as fatwas. This concentration limits the capacity to create 
systems competent in managing a more comprehensive range of Islamic questions [2]. Additionally, the avail-
able fatwa datasets do not cover different topics or questions related to fatwas, resulting in a narrow under-
standing of Islamic jurisprudence within automated systems. This scarcity of variety limits the relevance and 
effectiveness of fatwa QA systems in managing various user requirements [5].
•	 Automated Fatwas QA chatbots using AI: While progress in artificial intelligence (AI), machine learning 
(ML), and deep learning (DL) accomplish solutions [6], by combining these methods into a coordinated QA 
system that stays difficult due to the contextual knowledge since fatwas often require an in-depth contextual 
and cultural understanding [2]. Sequence-to-sequence (Seq2Seq) models struggle to grasp the subtle religious 
context needed to generate a precise response in the scope of Fatwas [7]. Adding to that, Seq2Seq does require 
a considerable amount of suitable data that must be of high quality and annotated precisely to fatwas that are 
insufficient, which are unfortunately hard to acquire [8].
•	 Integration of RAG with LLMs: The procedure of merging RAG with LLMs in the context of fatwa QA systems 
encounters several challenges that mainly arise from the inherent constraints of LLMs and the sophistication 
applied in knowledge retrieval and integration. LLMs tend to generate reasonable but false data, which is called 
a hallucination [9]. This is regarded as problematic in contexts like Fatwa, where the precision of the responses 
is necessary [10]. Existing RAG approaches seek to reduce the hallucinations by merging external knowledge; 
however, they struggle with trustworthiness due to the quality of the retrieved data. If the retrieved data is imprecise 
or deceitful, this can result in incorrect Fatwas [11].
Existing QA systems are unsuitable for the specialized task of fatwa answering owing to dataset availability con-
straints, the complexity of Arabic, and the inability to handle the complicated cultural and religious context. Exist-
ing techniques, like sequence-to-sequence (Seq2Seq), fail to preserve context, resulting in inaccurate or irrelevant 
responses [7]. Also, a lack of various high-quality datasets inhibits the development of effective fatwa QA systems.
Our approach seeks to avoid these limitations by using advanced RAG techniques and LLMs to provide 
accurate, contextually relevant fatwa responses. Using the Flash re-ranker during the retrieval stage improves 
the relevance of the retrieved information, reduces hallucinations, and ensures the generation of precise replies.
Apart from tackling these technological and linguistic problems, evaluating the ethical concerns of using AI 
in sensitive topics like fatwas is important. The ethical factors that must be taken into consideration when imple-
menting a fatwa QA system are:
•	 Confidentiality and Sensitivity: Ensuring that the Islamic data used in our implementation is handled with 
utmost respect and confidentiality. This will ensure that the system follows the norms of ethical data usage 
and protects sensitive religious information.
•	 Hallucination Mitigation: The possibility of producing inaccurate or misleading interpretations, known as 
hallucinations, is a serious problem. Our work aims to incorporate advanced RAG techniques, such as a re-
ranker, to reduce hallucinations and improve the trustworthiness and reliability of generated responses.
•	 Transparency: This system is a tool to help obtain reliable fatwas QA; however, it is not a replacement for 
consultation with trained Islamic scholars. This ensures the understanding of the system’s limits.
•	 Bias and Fairness: The system intends to evaluate balanced interpretations from many Islamic schools of 
thought to reduce bias. This guarantees that the produced replies are comprehensive and represent the full 
scope of Islamic jurisprudence.
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

--- Page 4 ---

	
Neural Computing and Applications
https://doi.org/10.1007/s00521-025-11229-y
By integrating these processes, the fatwa QA system can more effectively maintain ethical measures, ensuring 
that AI-generated religious fatwas are precise, reliable, and consistent with Islamic values.
We designed a structured approach to implementing a fatwa QA system using RAG and LLMs to guarantee 
precise and reliable outcomes. The contribution of our work is outlined as follows:
•	 Employing a reliable dataset acquired from Dar Alifta to guarantee quality for training and evaluation.
•	 Introducing Advanced RAG techniques, specifically, re-ranker, to reduce hallucinations and increase stability 
in the phase of generating responses.
•	 Used three different LLMs to generate responses and compared their performances.
•	 Utilizing metrics to evaluate the response’s completeness, hallucination, and irrelevance.
The rest of the paper is organized as follows: Section 2 covers the related work, Section 3 presents our proposed 
materials and methods, Section 4 presents our achieved results, Section 5 concludes the proposed work and dis-
cusses the recommendations for our future work, and finally, Section 6 covers the ethical considerations.
2  Related work
In recent years, the demand for Islamic fatwas has increased, resulting in an overwhelming volume of scholarly 
work that must be efficiently handled. This has exposed significant limitations in natural language process-
ing (NLP), particularly regarding the availability of Arabic datasets focused on Islamic content. While cur-
rent datasets, such as AyaTEC [12] and the Quranic Reading Comprehension Dataset (QRCD) [13], provide 
resources for Quranic QA and related tasks, they lack a detailed focus on the diverse and complicated domain 
of fatwas. Handling this gap, [4] introduced Fatwaset, a large-scale Arabic Islamic fatwa dataset comprising 
extensive metadata to enable NLP tasks and support research in Arabic and Islamic content. Yet, Fatwaset 
highlights metadata collection instead of delving into the capabilities of generative models for fatwa tasks.
Given the limitations of current automated Islamic fatwa QA systems, [6] performed a survey to investigate 
the state of the art (SoTA) in NLP and determine possible applications for resolving issues in question–answer-
ing and text classification within fatwa automation. Their work involved scraping 850,000 fatwas from various 
geographical provinces and accents, providing a significant dataset for baseline approaches in topic classifica-
tion, topic modeling, and retrieval-based QA. This work set a benchmark for prospective research but lacked 
a focus on generative models or domain-sensitive applications.
Similarly, [14] emphasized the need to get brief and verified direct responses from scholars. Their work 
involved developing a chatbot that uses fuzzy string matching to find replies to user inquiries based on Islamic 
law. The study test data were collected from multiple persons who used the chatbot directly by reviewing pairs 
of questions and responses to see whether they were good.
Building on this, prior studies stated that combining convolutional neural networks (CNNs) [15] with a 
transfer learning approach enhanced performance, specifically in learning and generating answers. Unlike 
retrieval strategies, these techniques improve the system’s capability to create reasonable replies rather than 
relying on responses that have been set. [16] implemented a chatbot for Islamic QA using CNN and transfer 
learning, which resulted in excellent accuracy. In their implementation, they used the PISS-KTB [17], an 
Indonesian Islamic QA dataset. Using CNN and the transfer learning approach, the results revealed that the 
use of transfer learning and Nadam [18] optimizer has increased the system’s performance in responding.
On the other hand, [19] outlined the features of question–answering systems (QAS), highlighting the chal-
lenges of the Arabic language’s complexity. Their survey presented current tools and datasets for Arabic QA, 
discussing evaluation metrics and suggesting recommendations for future research. However, the focus stayed 
on retrieval-based methods, with a limitation in exploring generative strategies.
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

--- Page 5 ---

Neural Computing and Applications	
https://doi.org/10.1007/s00521-025-11229-y
Building on this, [20] classified Islamic QAS into retrieval-based and pre-trained models or corpus-based sys-
tems but emphasized the limited availability of NLP tools and the limited range of existing techniques. These stud-
ies highlighted the possibility of AI-driven QA systems for Islamic fatwas; however, they did not include advanced 
techniques, such as combining retrieval methods with generative models for improved contextual understanding.
Recent advancements, such as the use of retrieval-augmented generation (RAG) models, have shown com-
mitment in handling some of these constraints. For example, [21] leveraged transformer models to develop 
a QA system for fatwa questions, balancing the exploitation of knowledge bases and generative capabilities.
Similarly, [22] proposed a RAG-based system for compassionate Islamic questions in Turkish, demon-
strating significant improvements over baseline models like ChatGPT. Both papers concentrated mainly on 
dataset evaluations and enhancing the accuracies but did not address reducing hallucination or increasing the 
stability for generating responses.
Other papers have examined cultural and linguistic diversity in QA datasets. For example, [23] introduced 
NativQA [24], a framework for culturally aligned datasets, yielding MultiNativQA with 64,000 QA pairs across 
seven languages. This approach enhanced performance in low-resource languages but did not target domain-
specific applications like fatwas. Additionally, [25] examined semantic search capabilities using LLM embed-
dings for Quranic texts, showing the efficiency of such methods over traditional keyword-based approaches.
These studies collectively underline the possibility of LLMs in religious and culturally sensitive domains 
but highlight the ongoing challenges, including hallucinations, lacking contextual understanding, and the lack 
of comprehensive fatwa evaluations.
To help clarify differences across RAG-based retrieval techniques, Table 1 illustrates a comparative review 
of the used existing retrieval models, highlighting their retrieval mechanism, description of each retrieval 
method, dataset coverage, and performance metrics.
Prior studies have employed a variety of retrieval techniques, each of which has its pros and cons. Trans-
former-based dense retrieval is computationally expensive, but it is effective in capturing contextual subtle-
ties. Knowledge-based exploitation is capable of achieving high levels of accuracy by employing structured 
data; however, it may encounter difficulties when performing unstructured queries. Semantic search with 
LLM embeddings yields relevant results depending on context, but it requires large computer resources. 
Scraping-based retrieval provides extensive data coverage, but it is prone to errors and requires significant 
preprocessing. Dense retrieval-based methods are effective for precise document matching, yet they may not 
be capable of competently handling complex queries. General retrieval methods are adaptable; however, they 
may not maintain the depth of more specialized techniques.
The related work focuses on existing datasets and techniques for Islamic QA systems, such as retrieval-based 
approaches and generative LLMs. Despite advances in dataset collection and retrieval approaches, previous 
studies highlighted problems such as poor handling of hallucinations, insufficient contextual understanding, 
and a lack of comprehensive evaluations of fatwa datasets.
3  Materials and methods
This section will comprehensively cover the dataset details, preprocessing, the proposed methodology, vec-
torization and retrieval, and the LLMs used to generate the response.
3.1  Dataset description
The dataset, obtained from Dar Alifta in Egypt, was used to implement the model. The dataset comprises three 
main categories, which are Fasting, Banks, and Zakka, which includes a total of 18,407 question–answering. 
Figure 1 shows the total number of occurrences for every category in the dataset.
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

--- Page 6 ---

	
Neural Computing and Applications
https://doi.org/10.1007/s00521-025-11229-y
3.2  Methodology
This paper will apply an experimental design approach to implement a QA approach that leverages an 
advanced retrieval-augmented generation (RAG) technique specifically designed to implement a Fatwa QA 
model based on large language models (LLMs).
The goal is to implement a system that minimizes the hallucinations and enhances the generated response. 
Our proposed model consists of four main steps, as shown in Fig. 2. The methodology will comprise various 
NLP techniques to guarantee that the model generates contextually relevant and reliable responses.
1.	 The first step involves transforming the datasets into an appropriate format, separating every question with 
its corresponding answer into chunks. These chunks are then prepared for the RAG implementation.
2.	 The chunks are embedded and stored in a vectorstore, allowing the RAG model to retrieve the most relevant 
fatwas based on semantic similarity [26] to the user query. This integration of document retrieval with LLMs 
reduces hallucinations and ensures that responses are both precise and contextually accurate. By combining 
the retrieved chunks with the user query in the LLM prompt, the model generates responses that reflect both 
the language understanding of the LLM and the factual accuracy of the retrieved documents.
Table 1   Comparison of QA approaches
Reference Methodology
Dataset
Accuracy and findings
Rule-Based QA
[6]
BoW-TF-IDF and classical retrieval-based 
methods for Fatwa classification
850,000 fatwas dataset
Accuracy: 53.5% using TF-IDF; lacks contex-
tual understanding
[12]
Retrieval-based QA using traditional similarity 
matching
AyaTEC dataset
Achieved a precision of 0.23 and Mean Recipro-
cal Rank of 0.34, revealing that traditional 
similarity matching struggles in retrieving for 
QA in Quran data
[14]
Fuzzy String-Matching Algorithm for answer-
ing Islamic Questions
Islamic Question Dataset
Achieved an accuracy of 70.37%, effective 
at matching users’ questions with relevant 
answers but performed poorly with complex 
and content-dependent questions
Transformer-Based QA
[21]
BERT-based QA model fine-tuned for Fatwa 
retrieval
Fatwa questions dataset
Evaluated using F1-BERTScore: 44%, improved 
contextual understanding
[13]
Dense retrieval using transformers for Quranic 
comprehension tasks
QRCD dataset
Achieved a score of 58.6% in partial Recipro-
cal Rank (pRR), revealing a good retrieval 
performance, but poor performance in exact 
answer matching
[16]
CNN-based model trained in Islamic QA
PISS-KTB dataset
Achieved an accuracy of 94.08%, revealing that 
despite its high result, the model struggles 
with responding to complex questions requir-
ing extensive contextual knowledge
Generative LLMs + RAG Models
[21]
Transformer-based dense retrieval with gen-
erative QA
Fatwa questions dataset
BERTScore: 48%; enhanced context under-
standing but hallucination occurs
[23]
Multilingual QA using transformer-based 
models
MultiNativQA (64,000 QA pairs) Achieved an F1-score of 87.5%, revealing 
that LLM with RAG has performed well in 
generating culturally and regionally aligned 
responses and enhanced the precision
[22]
RAG-based QA using structured knowledge 
bases
MufassirQAS
Evaluated using ChatGPT−3.5 Turbo, showing 
improved performance on sensitive questions. 
However, the dataset contains bias, affecting 
precision
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

--- Page 7 ---

Neural Computing and Applications	
https://doi.org/10.1007/s00521-025-11229-y
The RAG techniques, enhanced by a Flash re-ranker, enhance the relevance of retrieved chunks and the qual-
ity of generated responses, as shown in Fig. 2. This assures the procedure prioritizes the most relevant and 
precise answers, particularly enhancing response stability and minimizing mistakes in content generation.
3.2.1  Data preprocessing
The first step from our model pipeline, as shown in Fig. 2, involved acquiring data from reliable fatwa databases. 
We obtained our data from the Egyptian Dar Alifta. We received several files in CSV and HTML format. To 
prepare the data for analysis, we applied several preprocessing techniques to remove the HTML tags from the 
Fig. 1   Distribution of categories
Fig. 2   Proposed model pipeline
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

--- Page 8 ---

	
Neural Computing and Applications
https://doi.org/10.1007/s00521-025-11229-y
HTML files, such as <html>, <body>, <table>, <tr>, and <td>. Then, all the files were merged into two 
CSV files: testing and training, having three main columns: Subject, Question and Answer.
In Fig. 3, a sample of the data after being preprocessed and saved into a suitable format. After preprocessing 
the data and saving them into a suitable QA format, we applied the chunk mechanism by saving every question 
and its answer in a chunk. By breaking down the data into smaller question–answer pairs, the system can return 
more relevant information that matches the user query [27].
3.2.2  Vectorization and retrieval
Moving to the next phase in our model pipeline, as shown in Fig. 2, all the chunks were embedded using the 
Multilingual-E5 (mE5) [28] model, converting them into a vector. The mE5 model is a text embedding model 
that is fine-tuned on [28] multilingual datasets for retrieval tasks supporting over 100 different languages [29]. 
mE5 was chosen among the other embedding models because it outperforms in representing multilingual text, 
particularly in Arabic. It is ideal for handling fatwas written in various languages.
All the chunks are transformed and embedded to generate a vector representation. This ensures that the user 
query and the knowledge base are in the same vector space for a more accurate correspondence [30]. Having all 
the chunks vectorized from the knowledge base, they are stored in a vector database using Facebook AI Similar-
ity Search (FAISS) in our implementation. FAISS is a library dedicated to vector similarity search, a significant 
component of vector databases [31].
In our implementation, FAISS [31] was used to perform the similarity search by calculating the Euclidean 
distance between the query vector and the stored embeddings. These embeddings are indexed and arranged to 
allow for similarity calculations. Euclidean distance was decided over other options like cosine similarity due 
to its significance with dense embeddings in retrieval tasks. Once the user query gets vectorized, FAISS com-
putes the distances and returns the top-k chunks most similar to the user’s query. The value of K was adjusted 
Fig. 3   Dataset sample
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

--- Page 9 ---

Neural Computing and Applications	
https://doi.org/10.1007/s00521-025-11229-y
experimentally to guarantee a balance between precision and available computational power and memory. The 
top-k relevant chunks retrieved are passed to the last phase in the pipeline. The LLM generates an accurate and 
relevant response to the user’s query based on the context provided by the retrieved QA pairs.
Algorithm 1 illustrates the process of vectorization and retrieval. The procedure begins by converting the query 
into a dense vector using the mE5 [28] model. FAISS is then used to search for the top-k most similar embeddings in 
the stored index. Next, the corresponding questions and answers are retrieved using the indices of the nearest embed-
dings. Finally, the retrieved QA pairs are returned as chunks, providing the context for the last phase of the pipeline.
Algorithm 1   Vectorization and retrieval process
3.2.3  Answer generation
Upon retrieving the most relevant chunk, the user’s query and the context will be integrated and fed to the LLM prompt 
before passing to the LLM model. The retrieved chunks are concatenated with the user’s query to create a structured 
prompt that accurately guarantees the generated answer reflects the provided context and bypasses unwanted details.
This is where the final phase of our pipeline starts, which involves the generation of the responses. These LLMs 
aim to generate a reasonable, relatable, and semantically relevant reaction related to a certain query, known as a 
prompt [9]. The prompt instructed the model’s output by setting instructions.
In our experiment, we applied three different LLMs: Silma[32], AceGPT [33], and Gemini−1.5 [34] to gener-
ate the answer. These models were selected for their performance in processing and understanding Arabic text, 
capability to take context queries, and computational efficiency with quantized versions.
Silma LLM Silma AI [32] is a language model used in Text Generation, Chatbots and Conversational AI, and 
Text Summarization applications. Silma supports Arabic and English languages trained on 9 billion parameters, 
outperforming 72B models on most Arabic language tasks. It is built with the base models of Google Gemma [35], 
achieving good performance. Given that Silma is a large model in terms of computational power and memory, we 
applied the 4-bit quantization version. To generate a response, we initialized the prompt template to be specific 
and detailed to guide the model in generating responses related to Islamic fatwas.
AceGPT LLM The AceGPT [33] model shows significant advancements in language modeling. They are 
designed to understand and generate Arabic text. It comes in versions with 7 to 13 billion parameters, with 
the 7-billion-parameter AceGPT-7B standing out for its exceptional language generation and conversational 
capabilities. Its unique focus on Arabic allows it to comprehend and produce text effectively. AceGPT-7B’s 
impressive understanding of Arabic opens various possibilities for automation and creative applications. It is a 
key tool for AI-powered chatbots, meeting high-quality Arabic language processing. With a stable structure and 
extensive training data, it can generate logical and contextually relevant responses, making it suitable for casual 
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

--- Page 10 ---

	
Neural Computing and Applications
https://doi.org/10.1007/s00521-025-11229-y
and professional users. Given that AceGPT is a large model of computational power and memory, we used the 
AceGPT-7B Chat AWQ version that supports the 4-bit quantization version.
Gemini LLM Google’s Gemini 1.5 [34], a magnificent and giant language model, is ahead of all other 
models in humanlike natural language processing and generation. Gemini 1.5, on the one hand, has a better 
understanding of the context and a higher level of accuracy as it is trained on millions of tokens of context 
and is capable of handling up to at least 10 million tokens in long-context retrieval tasks, on the other, it is 
built on previous models by the addition of multimodal capabilities and the application of a more advanced 
architectural framework [36]. Therefore, the model can more naturally interpret and answer complex questions, 
leading to the successful application of informal AI and research assistance in many other areas. It is fully 
taught with a large volume of data that spans many fields; this way, the model’s knowledge will be greatly 
enhanced, and users will be able to get well-defined and detailed responses. Gemini 1.5 The token manage-
ment system and latency greatly decreased, which are the two key advantages of Gemini 1.5 in high-demand 
applications, making it one of the major contributions of AI to the world.
3.3  Flash re‑ranker
Re-ranking [37] is a procedure used to reorder the retrieved knowledge-based chunks. The hypothesis depends on the 
retrieved knowledge based on task-agnostic metrics, such as the Euclidean distance [38]. Based on the user query, 
the RAG will retrieve the top-k chunks, where these chunks are ranked based on their scores. These scores indicate 
how relevant the retrieved checks correspond to the user query. Unfortunately, these scores might not completely 
capture the context. So, the re-ranker re-evaluates the relevance of each chunk, intending to sort the most relevant 
and relatable information to generate a response. This involves applying and trying different machine learning algo-
rithms, such as the cross-encoder, to re-evaluate the first set of the retrieved outcomes. With this, re-rankers enhance 
the context input for the generative models, which will guide to a better relatable and relevant response [39].
The integration of RAG with LLMs occurs after the re-ranking process. Once the re-ranked chunks have been 
chosen, they are combined with the user query to provide a thorough input prompt for the LLM. The LLM then 
creates a response that includes the contextual information provided by the re-ranked chunks and the user query. 
The relation between RAG retrieval and the LLM guarantees that the generated response is relevant and accurate.
Algorithm 2   Generate response with re-rank
Algorithm 2 illustrates the re-ranking technique used to generate responses based on a given query in 
our work. The procedure starts by embedding the query and searching an FAISS index for the top-k results 
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

--- Page 11 ---

Neural Computing and Applications	
https://doi.org/10.1007/s00521-025-11229-y
corresponding to the query embedding. These results are then retrieved from the data to retrieve relevant 
QA pairs. The algorithm returns a message indicating this if no relevant chunks are located. Otherwise, the 
retrieved chunks will be re-ranked based on their relevancy to the query, and the re-ranked chunks will be 
returned as the final response. After re-ranking, the sorted chunks are combined with the user query and passed 
as input to the generative model, allowing it to create a response incorporating the most relevant retrieved 
knowledge. This strategy guarantees that the generated response is both appropriate and precise.
3.4  Validation and verification
To ensure the accuracy, reliability, and compliance of AI-generated Fatwas with Islamic jurisprudence, our pro-
posed Fatwa QA system incorporates a structured Validation and Verification Module as shown in Fig. 2. This 
module consists of the following key components: 
1.	 Automated Validation via Re-Ranking: The system employs a Flash re-ranker to refine retrieved knowl-
edge by scoring and ranking the most contextually relevant and jurisprudentially accurate sources. This step 
enhances retrieval quality and ensures that AI-generated responses align with verified Islamic rulings.
2.	 Human Verification and Expert Review: To maintain jurisprudential accuracy, the system incorporates 
human oversight. Responses flagged for low confidence or ambiguous content are reviewed by scholars before 
dissemination. This expert validation ensures alignment with Islamic principles and minimizes the risk of 
misinterpretation.
3.	 LLM-to-LLM Cross-Validation: An additional verification step is implemented using a higher-capability 
language model to assess clarity and contextual accuracy. This approach provides an additional layer of evalu-
ation, helping to refine AI-generated responses.
By integrating these validation and verification mechanisms, the system ensures that responses are accurate, 
contextually relevant, and ethically aligned with Islamic jurisprudence.
4  Results and discussion
This section will explain all the evaluation metrics used in detail and then present the results achieved using the 
three LLMs on the experiments performed.
4.1  Experimental setup
We conducted three experiments: (1) base model, (2) LLM with RAG, and (3) LLM with RAG and re-ranker. In 
the first experiment, we evaluated the models (AceGPT, Silma, and Gemini 1.5) without any retrieval mechanism, 
relying on the LLM pre-trained knowledge to generate answers. In the second experiment, we applied retrieval-
augmented generation (RAG), where relevant context is retrieved using an embedding model from an external 
knowledge base. The retrieved chunks (context) are then used to generate a response by passing them along with 
the LLM prompt. In the third experiment, we introduced a re-ranking step using the FlashRanker [37], where the 
retrieved chunks are reordered based on their relevance to the query. The re-ranking process applies a SIMILAR-
ITY_THRESHOLD of 0.97 to filter out irrelevant chunks.
For all experiments, the models (AceGPT, Silma, and Gemini 1.5) generate responses using the generate func-
tion, with hyperparameters like max_new_tokens=512 and max_length=256 for tokenization. Additionally, torch.
no_grad() is used to optimize memory consumption during generation. The experiments were performed on GPU T4.
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

--- Page 12 ---

	
Neural Computing and Applications
https://doi.org/10.1007/s00521-025-11229-y
4.2  Evaluation metrics
To assess the effectiveness of our proposed approach, we employed six widely recognized evaluation metrics, 
categorized into statistical and semantic measurements. Additionally, we conducted an LLM-to-LLM evaluation 
and engaged a domain expert to qualitatively assess a sample of the dataset.
These metrics provide quantitative and qualitative insights into the quality of generated text by comparing it 
against reference outputs. Below, we discuss each category in detail.
4.2.1  Statistical measurements
Statistical metrics primarily focus on surface-level text similarity, evaluating lexical overlap and n-gram cor-
respondence between generated and reference text.
4.2.2  Bilingual evaluation understudy (BLEU)
BLEU [40] is a precision-oriented metric that evaluates the match between n-grams of the generated and 
reference texts. It is often used for machine translation but is also effective in other text generation tasks:
where
•	 BP is the brevity penalty to penalize short translations.
•	 pn is the precision of n-grams.
•	 wn are weights (often equal) for different n-grams.
4.2.3  METEOR
METEOR [41] improves upon BLEU [40] by considering synonyms, stemming, and word order. It calculates 
the precision [42], recall [42], and harmonic mean [42], while also accounting for synonyms and paraphrasing, 
which enhances its accuracy in assessing semantic similarity: The METEOR score is calculated as follows:
where
•	 Precision: The fraction of words in the generated text that match the reference text.
•	 Recall: The fraction of words in the reference text that match the generated text.
•	 훼 : A parameter that controls the relative importance of precision and recall (default is usually 0.9).
•	 Penalty: A penalty term based on the fragmentation of matches (e.g., word order differences between the 
generated and reference text).
•	 훾 : A parameter that controls the impact of the penalty (default is usually 0.5).
(1)
BLEU = BP ⋅exp
( N
∑
n=1
wn log pn
)
(2)
METEOR = (1 −훾⋅Penalty) ×
Precision ⋅Recall
훼⋅Precision + (1 −훼) ⋅Recall
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

--- Page 13 ---

Neural Computing and Applications	
https://doi.org/10.1007/s00521-025-11229-y
4.2.4  Semantic measurements
Semantic metrics go beyond lexical similarity by evaluating meaning, contextual relevance, and factual con-
sistency in generated responses.
4.2.5  BERTScore
BERTScore [43] is a semantic similarity metric that leverages pre-trained BERT embeddings to evaluate 
the closeness of the generated text to the reference text. Given a pair of sequences X (generated text) and Y 
(reference text), BERTScore computes the cosine similarity between token embeddings and aggregates them 
to measure similarity:
where
•	 N is the number of tokens.
•	 embedding(⋅) represents the contextualized token embeddings from BERT.
•	 cos(⋅) denotes cosine similarity.
4.2.6  Hallucination
The hallucination [44] metric identifies inaccuracies in the generated answer by measuring the proportion of 
contradicting key points from the ground truth. It highlights areas where the response introduces unsupported or 
false information, which is critical for maintaining factual integrity. The formula is:
Here, A represents the generated response, K is the set of key points, and 1[⋅] determines whether A contradicts 
ki . This metric is essential to minimize domain errors where precision is paramount [44].
Algorithm 3 illustrates how we calculated the hallucination function in our experiment.
Algorithm 3   Calculate hallucination
(3)
BERTScore = 1
N
N
∑
i=1
cos(embedding(Xi), embedding(Yi))
Hallu(A, K) =
1
|K|
n
∑
i=1
1[A contradicts ki]
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

--- Page 14 ---

	
Neural Computing and Applications
https://doi.org/10.1007/s00521-025-11229-y
4.2.7  Irrelevance
The irrelevance [44] metric evaluates the proportion of key points that are neither covered nor contradicted by the 
generated response. This reflects the system’s ability to address relevant information while avoiding omissions. 
Irrelevance is derived as:
In this formula, completeness and hallucination scores are subtracted from 1 to quantify the key points the gen-
erated response fails to engage. This metric underscores areas where the system needs to improve its contextual 
alignment with the source material [44].
Algorithm 4 illustrates how we calculated the irrelevance function in our experiment.
Algorithm 4   Calculate irrelevance
4.2.8  Completeness
The completeness [44] metric assesses how well the generated response captures the critical information from 
the ground truth. This metric is defined as the proportion of key points semantically covered by the generated 
answer, ensuring factual alignment and comprehensiveness. According to the paper, completeness is calculated 
using the formula:
where A is the generated answer, K = {k1, k2, … , kn} is the set of key points, and 1[⋅] is an indicator function evalu-
ating whether A covers ki . This metric ensures the generated answer contains accurate and relevant information 
without omissions[44]. Algorithm 5 illustrates how we calculated the completeness function in our experiment.
Algorithm 5   Calculate completeness
Irr(A, K) = 1 −Comp(A, K) −Hallu(A, K)
Comp(A, K) =
1
|K|
n
∑
i=1
1[A covers ki]
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

--- Page 15 ---

Neural Computing and Applications	
https://doi.org/10.1007/s00521-025-11229-y
4.3  Experimental results
This section presents the results of our experiments. Initially, we evaluated the base LLMs on our dataset to assess 
their performance using only their pre-trained data. We then applied the RAG technique and re-evaluated the 
models. Finally, we assessed their performance after integrating the retrieval re-ranker mechanism.
4.3.1  LLMs base model
In this section, we present the experimental results of our Fatwa QA dataset without applying RAG techniques. 
Without RAG, the generative LLMs rely only on their pre-trained knowledge without retrieval. These results 
serve as the base for further improvement. Table 2 summarizes the performance of each generative LLM we 
evaluated.
The experimental findings of our fatwa QA dataset using the base model demonstrate the strengths and limi-
tations of the generative LLMs investigated. AceGPT outperforms Silma and Gemini 1.5 in F1-BERTScore 
and completeness, achieving a score of 64.92% and 98.46%, respectively, indicating its ability to provide 
relevant responses. However, its hallucination score (1.54%) is more significant than Silma’s (0.82%), which 
excels in reducing hallucinated context. Gemini 1.5 had the lowest completeness (95.55%) and the highest 
hallucination rate (4.45%), revealing complications in responding to fatwa questions. Despite these findings, 
the lack of RAG limits the models’ ability to access relevant, existing knowledge, resulting in partial or 
incorrect replies, particularly for complex and domain-specific fatwa questions. This underlines the need for 
incorporating RAG strategies to improve accuracy, decrease hallucination, and improve general performance 
in fatwa QA systems.
4.3.2  LLMs with RAG​
In this experiment, we applied the RAG model to the same generative LLMs to evaluate whether combining 
retrieval methods would enhance the generated responses. RAG introduces retrieval to improve response 
relevance in this setup, though it lacks re-ranking advancement. Table 3 illustrates the impact of retrieval 
on response quality, demonstrating improved relevance compared to using only the LLMs, even without the 
re-ranking step.
In this experiment, including the RAG model into the same generative LLMs increases response quality over 
the base model, which is completely based on pre-trained knowledge. AceGPT LLM F1-BERTScore increased 
to 68.29%, indicating improved response quality, but it is still behind Silma (68.93%), which continues to show 
in terms of completeness (99.48%). The hallucination rate also improves, with Silma dropping from 0.82% 
to 0.52%, revealing the beneficial effect of retrieval on decreasing inaccurate information. Gemini 1.5 also 
showed an enhancement from the retrieval approach, although its hallucination rate remains greater (7.50%), 
indicating weak retrieval. Notably, the completeness of AceGPT (96.72%) and Silma (99.48%) improves 
significantly compared to the base model, illustrating that retrieval offers more comprehensive responses by 
improving context and relevance. Despite these improvements, the lack of re-ranking advancement indicates 
that there is still a possibility for development in the relevance and accuracy of answers, highlighting the sig-
nificance of using additional strategies such as re-ranking to enhance retrieval and eliminate hallucinations.
4.3.3  LLMs with RAG and re‑ranker
In our final experiment, we aimed to enhance the relevance of the generated responses by integrating the RAG 
model with a re-ranking mechanism. This re-ranking step refined the retrieval process by selecting the most 
contextually relevant answers based on the user’s query. By applying RAG with re-ranking, we observed a 
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

--- Page 16 ---

	
Neural Computing and Applications
https://doi.org/10.1007/s00521-025-11229-y
considerable improvement in response accuracy, as the model effectively prioritized the most relevant answers. 
Table 4 shows the positive impact of re-ranking on both response accuracy and relevance.
In this last experiment, combining the RAG model with a re-ranking mechanism significantly enhances answer 
accuracy and relevance compared to the base model and the LLM with RAG. The F1-BERTScore of Silma with 
RAG re-ranker rises to 70.40%, outperforming both the base model (63.05%) and the LLM with RAG (68.93%), 
revealing a considerable improvement in the model’s capacity to create accurate and applicable responses. Silma’s 
hallucination rate also drops dramatically to 0.40%, revealing the efficiency of re-ranking in determining the most 
contextually appropriate responses. The completeness score for Silma also remains high at 99.60%, highlight-
ing that the re-ranking mechanism, when applied with RAG, improves the quality of the generated answers by 
prioritizing more appropriate and precise information.
4.3.4  Latency versus accuracy trade‑off
In this section, we analyzed the trade-off between the model accuracy and latency. to evaluate the feasibility of 
deploying our system in real-world scenarios, particularly given the sensitive nature of providing Islamic fatwas. 
Table 5 summarizes the average response generation time across the different experiments on the Silma model, 
as it was the best performing model.
As illustrated, adding RAG to the Silma base model leads to a notable improvement in accuracy, an increase of 
nearly 6 percentage points in F1-BERTScore, while introducing only a moderate increase in latency (from 4.02 
to 5.52 s). Furthermore, introducing the re-ranker enhances accuracy even more, achieving an F1-BERTScore of 
70.40%, which demonstrates the highest performance and stability in generating well-grounded fatwas. However, 
this comes at the cost of increased latency (26.95 s on average).
Despite this higher latency, the performance gain is critical in our application. Given the high-stakes nature of 
Islamic fatwa generation, where accuracy, coherence, and reliability are essential, we prioritize the quality and 
trustworthiness of responses over rapid response time. Incorrect or unstable answers could lead to misinforma-
tion and potentially serious real-world consequences. Therefore, although the Silma with RAG and re-ranker 
system require additional computational overhead, its superior performance justifies the latency in the context 
of our intended use case.
Table 2   Performance of 
LLMs base models
Base model
Model
F1-BERTScore 
(%)
Completeness 
(%)
Hallucination 
(%)
Irrelevance (%)
METEOR (%)
BLEU (%)
AceGPT
64.92
98.46
1.54
0.00
10.6
0.186
Gemini 1.5
62.30
95.55
4.45
0.00
10.6
0.1032
Silma
63.05
99.18
0.82
0.00
1.64
0.1032
Table 3   Performance of 
LLMs with RAG​
LLM with RAG​
Model
F1-BERT 
score (%)
Completeness 
(%)
Hallucination 
(%)
Irrelevance (%)
METEOR (%)
BLEU (%)
AceGPT
68.29
96.72
2.28
0.00
20.75
13.23
Gemini 1.5
67.94
92.50
7.50
0.00
13.25
2.01
Silma
68.93
99.48
0.52
0.00
17.02
10.18
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

--- Page 17 ---

Neural Computing and Applications	
https://doi.org/10.1007/s00521-025-11229-y
4.3.5  Human evaluation
To ensure the real-world applicability of our system, we conducted a qualitative expert evaluation on the third 
experiment LLM with RAG and re-ranker that achieved the highest accuracy and stability. The evaluation was 
done by a Professor of Arabic Studies at Mohamed Bin Zayed University for Humanities, who independently 
analyzed all 210 AI-generated fatwas, which consisted of 70 responses from each LLM Silma, AceGPT, and 
Gemini 1.5—without knowing their source. The professor independently and blindly evaluated the generated 
responses, in which the responses were graded 1 to 5 based on correctness and Islamic principles for fatwas. Each 
model’s evaluation score was derived by the average of the individual grades. Figure 4 presents the domain expert 
ratings, highlighting Silma’s distinguished performance in generating contextually relevant and accurate answers.
The results of the human evaluation showed that LLM Silma outperformed the other models with an average 
score of 3.86/5, followed by AceGPT at 3.56/5 and Gemini 1.5 at 2.95/5. The low performance of Gemini 1.5 can 
be interpreted as its inclination to hallucinate despite being merged with the knowledge base. Gemini 1.5 fails to 
generate contextually relevant replies as it depends on its training knowledge instead of the provided context and 
the instructions from the prompt. This conduct makes Gemini 1.5 unsuitable for sensitive topics like fatwa, where 
contextual precision is necessary. In contrast, Silma showed the best performance with the highest score and the 
lowest hallucination rate, revealing its capability to follow instructions and generate contextually precise answers. 
AceGPT showed intermediate performance with some room for improvement; nevertheless, it answered better 
with the given context compared to Gemini 1.5. This indicates that Silma is the most reliable LLM for sensitive 
topics, while Gemini 1.5 is less suitable due to its poor commitment to context.
4.3.6  LLM‑to‑LLM evaluation
To expand our evaluation, we applied an LLM-to-LLM evaluation using GPT-4o [45] LLM by giving it a 
specified detailed set of instructions (prompt). GPT-4o stands for its better capability, as assessed by the 
number of parameters and model design, allowing it to analyze and evaluate complicated inputs with more 
precision and consistency [45]. Its extensive training on varied datasets gives deeper contextual knowledge, 
making it an excellent choice for assessing the outputs of other models. The defined prompt 5 evaluated the 
quality and appropriateness of the generated responses related to Islamic fatwas by comparing them with the 
ground truth (original answer).
We evaluated the 210 total samples that were assessed by the expert domain. The evaluation criteria were 
based on 3 main criteria: 
Table 4   Performance 
of LLMs with RAG and 
re-ranking
LLM with RAG and re-ranker
Model
F1-BERT 
score (%)
Completeness 
(%)
Hallucination 
(%)
Irrelevance (%)
METEOR (%)
BLEU (%)
AceGPT
65.02
96.72
3.28
0.00
6.83
1.84
Gemini 1.5
67.59
91.47
8.53
0.00
13.03
1.98
Silma
70.40
99.60
0.40
0.00
20.75
13.23
Table 5   Latency vs. 
accuracy: a comparative 
analysis of models
Model
Average response time
(seconds)
F1-BERTScore 
(%)
Silma base model
4.02
63.05
Silma with RAG​
5.52
68.93
Silma with RAG and re-ranker
26.95
70.40
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

--- Page 18 ---

	
Neural Computing and Applications
https://doi.org/10.1007/s00521-025-11229-y
1.	 Clarity: This aims to evaluate whether the generated response by the LLM is easy to understand and delivers 
the intended response.
2.	 Information Completeness: This aims to determine if the generated response thoroughly addresses the ques-
tion and includes all the needed information.
3.	 Islamic Context: This aims to assess whether the generated response matches the Islamic principles, specifi-
cally in banking, Zakka, and Fasting.
Figure 6 presents the results of the LLM-to-LLM evaluation. Among the models, Silma with RAG and re-ranker 
achieved the highest clarity score of 7.67/10, followed by AceGPT and Gemini 1.5, both with a score of 7.46/10. 
For completeness, Gemini 1.5 outperformed the others with a score of 7.49/10, while Silma scored 7.26/10, 
and AceGPT scored the lowest at 6.99/10. In terms of Islamic Appropriateness, Silma again led with a score of 
8.11/10, followed by Gemini 1.5 with 7.53/10, and AceGPT with 7.04/10.
4.4  Performance comparison of existing and proposed models
Table 6 compares all the models applied to implement a Fatwa QA system to those we applied to our system.
Our experiments highlight the effectiveness of re-ranking in improving model performance across the various 
LLMs in our fatwa QA task. With re-ranking, the Silma AI model achieved the highest and lowest hallucination 
scores across all metrics while addressing the model’s instability by generating more relevant and consistent 
responses. In contrast, the Gemini 1.5 and AceGPT LLM, both with and without re-ranking, demonstrated sig-
nificantly lower performance, indicating limitations in their ability to produce high-quality outputs. However, 
they showed moderate improvements with the re-ranking approach but still lagged behind the Silma LLM model.
Fig. 4   Human evaluation scores
Fig. 5   LLM-to-LLM evalua-
tion prompt
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

--- Page 19 ---

Neural Computing and Applications	
https://doi.org/10.1007/s00521-025-11229-y
Figure 7 presents a sample-generated response across all the applied experiments.
Our findings demonstrate that integrating retrieval-augmented generation (RAG) and re-ranking significantly 
enhances the accuracy and reliability of fatwa QA systems. Without retrieval, base models struggled with fac-
tual consistency, with AceGPT achieving the highest F1-BERTScore (64.92%) but exhibiting higher hallucina-
tion (1.54%) than Silma (0.82%). Implementing RAG improved response quality, particularly for Silma, which 
achieved 68.93% F1-BERTScore and reduced hallucinations to 0.52%. Further integrating re-ranking optimized 
retrieval relevance, with Silma’s F1-BERTScore reaching 70.40% and hallucinations dropping to 0.40%. However, 
this came at the cost of increased latency (26.95s). Human evaluation rated Silma highest (3.86/5) for Islamic 
accuracy, and LLM-to-LLM evaluation (GPT-4o) confirmed its superior clarity (7.67/10) and relevance (8.11/10). 
These results confirm that re-ranking refines retrieval quality, reducing hallucinations and improving contextual 
accuracy, making Silma with RAG and re-ranking the most reliable choice for fatwa QA applications.
4.5  Ethical considerations and trustworthiness in AI‑generated fatwas
Given the sensitivity of fatwa issuance, ethical safeguards are crucial to maintaining the credibility, accuracy, 
and alignment of AI-driven Islamic QA systems with Islamic jurisprudence. Our proposed model incorporates 
several mechanisms to ensure trustworthiness and ethical compliance in AI-generated fatwas.
4.5.1  Verified and scholarly sources
To prevent misinformation, our RAG model exclusively retrieves data from verified Islamic databases. Addition-
ally, the Flash re-ranker prioritizes content that aligns with established jurisprudential principles, filtering out 
unreliable or misleading sources.
Fig. 6   LLM-to-LLM evalua-
tion results
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

--- Page 20 ---

	
Neural Computing and Applications
https://doi.org/10.1007/s00521-025-11229-y
4.5.2  Reducing hallucinations
Hallucination risks are mitigated using semantic similarity filtering, removing uncertain responses. Furthermore, 
the re-ranker acts as an additional verification layer, ensuring that retrieved content is both accurate and contex-
tually relevant to the user’s query.
4.5.3  Ethical oversight and human‑in‑the‑loop (HITL) Approach
We emphasize that AI should assist, not replace, scholars. The system flags ambiguous or sensitive fatwas for 
expert review, ensuring compliance with Islamic ethical guidelines. The HITL framework strengthens account-
ability by enabling scholars to validate AI responses before dissemination.
4.5.4  Transparency and explainability
To ensure trust and reliability, our model incorporates Explainable AI (XAI) techniques, allowing scholars to 
trace, interpret, and validate AI-generated fatwas. The following key approaches enhance the transparency and 
accuracy of our system: 
1.	 Source Attribution: Every ruling is linked to verified Islamic references. The AI retrieves the top three re-
ranked QA pairs from Dar al-Ifta, ensuring responses align with scholar-approved rulings. For instance, if a 
Table 6   Comparison of existing and proposed models
Category
Accuracy (%)
BERTScore F1
Hallucination
Completeness
Irrelevance
Related work
Baseline
BoW-Binary Features [6]
53.3
–
–
–
–
BoW-Count [6]
53.4
–
–
–
–
BoW-Frequency [6]
51
–
–
–
–
BoW-TF-IDF [6]
53.5
–
–
–
–
BoW Vectors [6]
47
–
–
–
–
One-layer LSTM [6]
52
–
–
–
–
One-layer GRU [6]
53
–
–
–
–
Two-layer LSTM [6]
50
–
–
–
–
Two-layer GRU [6]
56
–
–
–
–
AraBERT [6]
70
–
–
–
–
FastText with Cosine Similarity [6]
96.4
–
–
–
–
Neural Models
LSTM-based seq2seq [21]
–
36%
–
–
–
BERT2BERT [21]
–
44%
–
–
–
Knowledge-augmented BERT2BERT [21]
–
48%
–
–
–
Proposed Models
Proposed Models
With RAG re-ranker
SILMA
–
63.05
0.82
99.18
0.00
AceGPT
–
64.92
1.54
98.46
0.00
Gemini 1.5
–
62.3
4.45
95.55
0.00
SILMA with RAG​
–
68.93
0.52
99.48
0.00
AceGPT with RAG​
–
68.29
2.28
97.72
0.00
Gemini 1.5 with RAG​
–
67.94
7.50
92.50
0.00
SILMA with RAG re-ranker
–
70.40
0.40
99.60
0.00
AceGPT with RAG re-ranker
–
65.02
3.28
96.72
0.00
Gemini 1.5 with RAG re-ranker
–
67.59
8.53
91.47
0.00
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

--- Page 21 ---

Neural Computing and Applications	
https://doi.org/10.1007/s00521-025-11229-y
Fig. 7   Comparison of generated responses across all the experiments
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

--- Page 22 ---

	
Neural Computing and Applications
https://doi.org/10.1007/s00521-025-11229-y
Fig. 8   Heatmap visualization of the similarity between the user query and the top-k retrieved documents
Fig. 9   Heatmap visualization of the similarity between the top-k retrieved documents and the generated response
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

--- Page 23 ---

Neural Computing and Applications	
https://doi.org/10.1007/s00521-025-11229-y
user asks, “What is the ruling on not fasting in Ramadan?,” the AI retrieves relevant fatwas, grounding its 
response in authenticated Islamic sources.
2.	 Semantic Similarity Analysis: We employ BERTScore, achieving a 70.04% similarity, to filter inaccurate 
responses and minimize hallucinations, ensuring AI-generated fatwas remain contextually precise. Addi-
tionally, we conducted heatmap visualizations representing the user query vs. top-k retrieved documents as 
shown in Fig. 8, and this evaluates the precision of the retrieval process in determining contextually relevant 
documents, and top-k retrieved documents vs. generated response as shown in Fig. 9 to evaluate retrieval 
accuracy and response alignment.
3.	 Re-ranking for Accuracy: Retrieved documents are scored and ranked, refining knowledge selection before 
response generation. This step optimizes accuracy and prioritizes the most relevant rulings.
4.	 Interactive Scholar Feedback: Experts can review, correct, and refine responses, enabling continuous improve-
ment through human–AI collaboration.
These mechanisms make our system interpretable, auditable, and reliable, reinforcing its role as a scholarly-
assistive tool rather than an independent decision-maker.
Figure 10 illustrates the top three retrieved documents along with their re-ranked retrieval scores.
By integrating these safeguards, our model ensures trustworthy, contextually accurate, and ethically sound 
AI-generated fatwas, reinforcing its role as a scholarly-assistive tool rather than an independent decision-maker.
Fig. 10   Sample of the retrieved document and user query for answer generation
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

--- Page 24 ---

	
Neural Computing and Applications
https://doi.org/10.1007/s00521-025-11229-y
5  Conclusion and future work
This study presents a question–answering (QA) system that integrates the retrieval-augmented generation (RAG) 
approach with large language models (LLMs) to address the complexities of issuing Islamic fatwas. The model 
enhances response relevance and reliability by combining retrieval-based and generative approaches. The experi-
mental results revealed that each used LLM: Silma, AceGPT, and Gemini 1.5 showed an increase in the perfor-
mance when integrated with the RAG mechanism. The evaluations without RAG showed limited relevance, as 
shown in Table 2, with the percentage of hallucination scores being high compared to Silma 1.54%, 4.45%, and 
0.82% for AceGPT, Gemini 1.5, and Silma, respectively. After integrating RAG as shown in Table 3, the qual-
ity of the generated response has improved significantly and reduced the hallucination, with the hallucination 
score for Silma decreasing to 0.52% and applying a re-ranking mechanism in the final step enhanced accuracy, 
especially for Silma, which achieved the highest scores across all metrics in the re-ranking experiment Table 4.
Future enhancements could involve applying advanced RAG techniques to refine retrieval and ranking processes 
further and produce even more accurate and contextually relevant responses. Additionally, fine-tuning the LLMs 
on a fatwa-specific dataset could enhance their ability to handle diverse consultation topics, improving response 
precision and minimizing hallucinations.
Acknowledgements  The authors thank Dar Alifta for providing us with the dataset.
Author contribution  All authors listed have made a substantial, direct, and intellectual contribution to the work and approved 
it for publication. Dr. Ayad's position was as an Arabic domain expert, specifically reviewing the results.
Funding  Open access funding provided by The Science, Technology & Innovation Funding Authority (STDF) in coopera-
tion with The Egyptian Knowledge Bank (EKB).
Data availability  The dataset used and the implemented code in this study will be made publicly accessible upon the pub-
lication of this paper at the following repository: https://​github.​com/​Marry​am03/​Fatwa​QA. The data will be provided in 
a CSV format. No additional permissions are required to access the data, and it will be freely available for academic and 
research purposes.
Declarations 
Conflict of interest  The authors declare that they have no conflict of interest.
Consent for publication  Not applicable.
Ethics approval and consent to participate  Not applicable.
Open Access   This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, 
sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the 
original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The 
images or other third party material in this article are included in the article's Creative Commons licence, unless indicated 
otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your 
intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly 
from the copyright holder. To view a copy of this licence, visit http://​creat​iveco​mmons.​org/​licen​ses/​by/4.​0/.
References
	1.	 Qamar F, Latif S, Latif R (2024) A benchmark dataset with larger Context for non-factoid question answering over 
islamic text. arXiv:​2409.​09844
	2.	 Elhalwany I, Mohammed A, Wassif K, Hefny H (2015) Using textual case-based reasoning in intelligent fatawa qa 
system. Int Arab J Inf Technol 12:503–509
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

--- Page 25 ---

Neural Computing and Applications	
https://doi.org/10.1007/s00521-025-11229-y
	3.	 Alrayzah A, Alsolami F, Saleh M (2023) Challenges and opportunities for arabic question-answering systems: current 
techniques and future directions. PeerJ Comput Sci 9:1633. https://​doi.​org/​10.​7717/​peerj-​cs.​1633
	4.	 Alyemny O, Al-Khalifa H, Mirza A (2023) A data-driven exploration of a new islamic fatwas dataset for arabic nlp tasks. 
Data 8(10):155. https://​doi.​org/​10.​3390/​data8​100155
	5.	 Abdallah A, Kasem M, Abdalla M, Mahmoud M, Elkasaby M, Elbendary Y, Jatowt A (2024) ArabicaQA: A Compre-
hensive Dataset for Arabic Question Answering. arXiv:​2403.​17848
	6.	 Munshi AA, AlSabban WH, Farag AT, Rakha OE, Al Sallab AA, Alotaibi M (2021) Towards an automated islamic 
fatwa system: survey, dataset and benchmarks. Int J Comput Sci Mobile Comput 10(4):118–131
	7.	 Yigit G, Amasyali MF (2024) From text to multimodal: a survey of adversarial example generation in question answer-
ing systems. Knowl Inf Syst 66(12):7165–7204. https://​doi.​org/​10.​1007/​s10115-​024-​02199-z
	8.	 Wu L, Wu P, Zhang X (2020) A seq2seq-based approach to question answering over knowledge bases. In: Wang X, Lisi 
FA, Xiao G, Botoeva E (eds) Semantic Technology. Springer, Singapore, pp 170–181
	9.	 Mansurova A, Mansurova A, Nugumanova A (2024) Qa-rag: exploring llm reliance on external knowledge. Big Data 
Cognitive Comput 8(9):115. https://​doi.​org/​10.​3390/​bdcc8​090115
	10.	 Pham DK, Vo BQ (2024) Towards Reliable Medical Question Answering: Techniques and Challenges in Mitigating 
Hallucinations in Language Models. arXiv:​2408.​13808
	11.	 Zhou Y, Liu Y, Li X, Jin J, Qian H, Liu Z, Li C, Dou Z, Ho T-Y, Yu PS (2024) Trustworthiness in Retrieval-Augmented 
Generation Systems: A Survey. arXiv:​2409.​10102
	12.	 Malhas R, Elsayed T (2020) Ayatec: Building a reusable verse-based test collection for arabic question answering on 
the holy qur’an. ACM Trans Asian Low-Resour Lang Inf Process 19(6):1. https://​doi.​org/​10.​1145/​34003​96
	13.	 Malhas R, Mansour W, Elsayed T (2022) Qur’an QA 2022: Overview of the first shared task on question answering over 
the holy qur’an. In: Al-Khalifa, H., Elsayed, T., Mubarak, H., Al-Thubaity, A., Magdy, W., Darwish, K. (eds.) Proceed-
insg of the 5th Workshop on Open-Source Arabic Corpora and Processing Tools with Shared Tasks on Qur’an QA and 
Fine-Grained Hate Speech Detection, pp. 79–87. European Language Resources Association, Marseille, France. https://​
aclan​tholo​gy.​org/​2022.​osact-1.9
	14.	 Sihotang MT, Jaya I, Hizriadi A, Hardi SM (2020) Answering islamic questions with a chatbot using fuzzy string-
matching algorithm. J Phys: Conf Ser 1566(1):012007. https://​doi.​org/​10.​1088/​1742-​6596/​1566/1/​012007
	15.	 O’Shea K, Nash R (2015) An Introduction to Convolutional Neural Networks. arXiv:​1511.​08458
	16.	 Anggraini RNE, Tursina D, Sarno R (2024) Islamic qa with chatbot system using convolutional neural network. Iraqi J 
Sci. https://​doi.​org/​10.​24996/​ijs.​2024.​65.4.​38
	17.	 PISS KTB, TIM Dakwah Pesantren: Tanya Jawab Islam: Piss KTB. Daarul Hijrah Technology, Indonesia (2015). https://​
books.​google.​com/​books/​about/​Tanya_​Jawab_​Islam.​html?​id=​GMZQC​wAAQB​AJ
	18.	 Zhang Q, Zhang Y, Shao Y, Liu M, Li J, Yuan J, Wang R (2023) Boosting adversarial attacks with nadam optimizer. 
Electronics 12:1464
	19.	 Alwaneen T, Azmi A, Aboalsamh H, Cambria E, Hussain A (2021) Arabic question answering system: a survey. Artif 
Intell Rev 55:207. https://​doi.​org/​10.​1007/​s10462-​021-​10031-1
	20.	 Alnefaie S, Atwell E, Alsalka M (2023) Islamic question answering systems survey and evaluation criteria. Int J Islamic 
Appl Comput Sci Technol 11(1):9
	21.	 Alotaibi SS, Munshi AA, Farag AT, Rakha OE, Al Sallab AA, Alotaibi M (2022) KAB: knowledge augmented BERT-
2BERT automated questions answering system for Jurisprudential legal opinions. IJCSNS Int J Comput Sci Netw Secur 
22:346
	22.	 Alan AY, Karaarslan E (2024) Aydin: A RAG-based Question Answering System Proposal for Understanding Islam: 
MufassirQAS LLM. arXiv:​2401.​15378
	23.	 Hasan MA, Hasanain M, Ahmad F, Laskar SR, Upadhyay S, Sukhadia VN, Kutlu M, Chowdhury SA, Alam F (2024) 
NativQA: Multilingual Culturally-Aligned Natural Query for LLMs. arXiv:​2407.​09823
	24.	 Hasan MA, Hasanain M, Ahmad F, Laskar SR, Upadhyay S, Sukhadia VN, Kutlu M, Chowdhury SA, Alam F (2024) 
NativQA: Multilingual Culturally-Aligned Natural Query for LLMs. arXiv:​2407.​09823. arXiv:​2407.​09823
	25.	 Alqarni M (1970) Embedding search for quranic texts based on large language models. Int Arab J Inf Technol(IAJIT) 
21(02):243–256
	26.	 Gao Y, Xiong Y, Gao X, Jia K, Pan J, Bi Y, Dai Y, Sun J, Wang M, Wang H (2024) Retrieval-Augmented Generation 
for Large Language Models: A Survey. arXiv:​2312.​10997
	27.	 Zhong Z, Liu H, Cui X, Zhang X, Qin Z (2024) Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-
Augmented Generation. arXiv:​2406.​00456
	28.	 Wang L, Yang N, Huang X, Yang L, Majumder R, Wei F (2024) Multilingual e5 text embeddings: A technical report. 
arXiv preprint arXiv:​2402.​05672
	29.	 Acharya A, Murthy R, Kumar V, Sen J (2024) NLLB-E5: A Scalable Multilingual Retrieval Model. arXiv:​2409.​05401
	30.	 Siriwardhana S, Weerasekera R, Wen E, Kaluarachchi T, Rana R, Nanayakkara S (2023) Improving the domain adaptation 
of retrieval augmented generation (RAG) models for open domain question answering. Trans Assoc Comput Linguist 
11:1–17. https://​doi.​org/​10.​1162/​tacl_a_​00530
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

--- Page 26 ---

	
Neural Computing and Applications
https://doi.org/10.1007/s00521-025-11229-y
	31.	 Douze M, Guzhva A, Deng C, Johnson J, Szilvasy G, Mazaré P-E, Lomeli M, Hosseini L, Jégou H (2024) The Faiss 
library. arXiv:​2401.​08281
	32.	 Team S (2024) Silma. Silma. https://​www.​silma.​ai
	33.	 Huang H, Yu F, Zhu J, Sun X, Cheng H, Song D, Chen Z, Alharthi A, An B, Liu Z, et al (2023) Acegpt, localizing large 
language models in arabic. arXiv preprint arXiv:​2309.​12053
	34.	 Team G, Georgiev P al (2024) Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context. 
arXiv:​2403.​05160
	35.	 Team G (2024) Gemma: Open Models Based on Gemini Research and Technology. arXiv:​2403.​08295
	36.	 Saab K, Tu T, Weng W-H, Tanno R al, D.S (2024) Capabilities of Gemini Models in Medicine. arXiv:​2404.​18416
	37.	 Damodaran P (2024) FlashRank, Lightest and fastest 2nd stage Reranker for search pipelines. Zenodo. https://​doi.​org/​
10.​5281/​zenodo.​11093​524
	38.	 Wu S, Xiong Y, Cui Y, Wu H, Chen C, Yuan Y, Huang L, Liu X, Kuo T-W, Guan N, et al (2024) Retrieval-augmented 
generation for natural language processing: A survey. arXiv preprint arXiv:​2407.​13193
	39.	 Eibich M, Nagpal S, Fred-Ojala A (2024) ARAGOG: Advanced RAG Output Grading. arXiv:​2404.​01037
	40.	 Papineni K, Roukos S, Ward T, Zhu W-j (2002) Bleu: a method for automatic evaluation of machine translation, pp. 
311–318
	41.	 Banerjee S, Lavie A (2005) METEOR: An automatic metric for MT evaluation with improved correlation with human 
judgments. In: Goldstein, J., Lavie, A., Lin, C.-Y., Voss, C. (eds.) Proceedings of the ACL Workshop on Intrinsic and 
Extrinsic Evaluation Measures for Machine Translation And/or Summarization, pp. 65–72. Association for Computa-
tional Linguistics, Ann Arbor, Michigan. https://​aclan​tholo​gy.​org/​W05-​0909
	42.	 Powers DMW (2020) Evaluation: from precision, recall and F-measure to ROC, informedness, markedness and correla-
tion. arXiv:​2010.​16061
	43.	 Zhang T, Kishore V, Wu F, Weinberger KQ, Artzi Y (2020) BERTScore: Evaluating Text Generation with BERT. arXiv:​
1904.​09675
	44.	 Zhu K, Luo Y, Xu D, Wang R, Yu S, Wang S, Yan Y, Liu Z, Han X, Liu Z, Sun M (2024) RAGEval: Scenario Specific 
RAG Evaluation Dataset Generation Framework. arXiv:​2408.​01262
	45.	 OpenAI: GPT-4 Technical Report (2024). arXiv:​2303.​08774
Publisher's Note  Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional 
affiliations.
Authors and Affiliations
Marryam Yahya Mohammed1   · Sama Ayman Ali1 · Salma Khaled Ali1 · 
Ayad Abdul Majeed3 · Ensaf Hussein Mohamed1,2
 *	Marryam Yahya Mohammed 
	
M.Yahya2163@nu.edu.eg
	
Sama Ayman Ali 
	
S.Ayman2176@nu.edu.eg
	
Salma Khaled Ali 
	
Skhaled@nu.edu.eg
	
Ayad Abdul Majeed 
	
Ayad.Majeed@mbzuh.ac.ae
	
Ensaf Hussein Mohamed 
	
enmohamed@nu.edu.eg
1	
School of Information Technology and Computer Science ITCS, Nile University, Giza, Egypt
2	
Faculty of Computers and Artificial Intelligence, Helwan University, Cairo Governorate, Egypt
3	
Mohamed Bin Zayed University for Humanities, Ajman, United Arab Emirates
Content courtesy of Springer Nature, terms of use apply. Rights reserved.

--- Page 27 ---

1.
2.
3.
4.
5.
6.
Terms and Conditions
 
Springer Nature journal content, brought to you courtesy of Springer Nature Customer Service Center GmbH (“Springer Nature”).
 
Springer Nature supports a reasonable amount of sharing of  research papers by authors, subscribers and authorised users (“Users”), for small-
scale personal, non-commercial use provided that all copyright, trade and service marks and other proprietary notices are maintained. By
accessing, sharing, receiving or otherwise using the Springer Nature journal content you agree to these terms of use (“Terms”). For these
purposes, Springer Nature considers academic use (by researchers and students) to be non-commercial.
 
These Terms are supplementary and will apply in addition to any applicable website terms and conditions, a relevant site licence or a personal
subscription. These Terms will prevail over any conflict or ambiguity with regards to the relevant terms, a site licence or a personal subscription
(to the extent of the conflict or ambiguity only). For Creative Commons-licensed articles, the terms of the Creative Commons license used will
apply.
 
We collect and use personal data to provide access to the Springer Nature journal content. We may also use these personal data internally within
ResearchGate and Springer Nature and as agreed share it, in an anonymised way, for purposes of tracking, analysis and reporting. We will not
otherwise disclose your personal data outside the ResearchGate or the Springer Nature group of companies unless we have your permission as
detailed in the Privacy Policy.
 
While Users may use the Springer Nature journal content for small scale, personal non-commercial use, it is important to note that Users may
not:
  
use such content for the purpose of providing other users with access on a regular or large scale basis or as a means to circumvent access
control;
use such content where to do so would be considered a criminal or statutory offence in any jurisdiction, or gives rise to civil liability, or is
otherwise unlawful;
falsely or misleadingly imply or suggest endorsement, approval , sponsorship, or association unless explicitly agreed to by Springer Nature in
writing;
use bots or other automated methods to access the content or redirect messages
override any security feature or exclusionary protocol; or
share the content in order to create substitute for Springer Nature products or services or a systematic database of Springer Nature journal
content.
 
In line with the restriction against commercial use, Springer Nature does not permit the creation of a product or service that creates revenue,
royalties, rent or income from our content or its inclusion as part of a paid for service or for other commercial gain. Springer Nature journal
content cannot be used for inter-library loans and librarians may not upload Springer Nature journal content on a large scale into their, or any
other, institutional repository.
 
These terms of use are reviewed regularly and may be amended at any time. Springer Nature is not obligated to publish any information or
content on this website and may remove it or features or functionality at our sole discretion, at any time with or without notice. Springer Nature
may revoke this licence to you at any time and remove access to any copies of the Springer Nature journal content which have been saved.
 
To the fullest extent permitted by law, Springer Nature makes no warranties, representations or guarantees to Users, either express or implied
with respect to the Springer nature journal content and all parties disclaim and waive any implied warranties or warranties imposed by law,
including merchantability or fitness for any particular purpose.
 
Please note that these rights do not automatically extend to content, data or other material published by Springer Nature that may be licensed
from third parties.
 
If you would like to use or distribute our Springer Nature journal content to a wider audience or on a regular basis or in any other manner not
expressly permitted by these Terms, please contact Springer Nature at
  
onlineservice@springernature.com
 

```
