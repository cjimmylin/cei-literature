---
title: "2025-Pudasaini-NepaliGPT A Generative Language Model for - PDF Extract"
source_pdf: "2025-Pudasaini-NepaliGPT A Generative Language Model for.pdf"
pages: 11
extracted_at: "2026-03-12T13:54:18.454298"
---

# PDF Extract: 2025-Pudasaini-NepaliGPT A Generative Language Model for

**Source PDF:** 2025-Pudasaini-NepaliGPT A Generative Language Model for.pdf
**Total Pages:** 11

---

## Content

```
--- Page 1 ---

arXiv:2506.16399v1  [cs.CL]  19 Jun 2025
NEPALIGPT: A GENERATIVE LANGUAGE MODEL FOR
NEPALI LANGUAGE
Shushanta Pudasaini
Technological University Dublin
Dublin, Ireland
shushanta574@gmail.com
Aman Shakya
Institute of Engineering
Lalitpur, Nepal
aman.shakya@ioe.edu.np
Siddhartha Shrestha
Kathmandu Engineering College
Kathmandu, Nepal
shrestha.siddhartha06@outlook.com
Sahil Bhatta
Fanshawe College
Ontario, Canada
sahilbhatta70@gmail.com
Sunil Thapa
Lambton College
Ontario, Canada
sunil43thapa@gmail.com
Sushmita Palikhe
Institute of Engineering
Lalitpur, Nepal
081msdsa024.sushmita@pcampus.edu.np
June 23, 2025
ABSTRACT
After the release of ChatGPT, Large Language Models (LLMs) have gained huge popularity in recent
days and thousands of variants of LLMs have been released. However, there isn’t any generative
language model for the Nepali language, due to which other downstream tasks, including fine-tuning,
have not been explored yet. To fill this research gap in the Nepali NLP space, this research proposes
NepaliGPT, a generative large language model tailored specifically for the Nepali language. This
research introduces an advanced corpus for the Nepali Language collected from several sources called
the Devanagari Corpus. Likewise, the research introduces the first NepaliGPT benchmark dataset
comprised of 4296 question-answer pairs in the Nepali language. The proposed LLM NepaliGPT
achieves the following metrics in text generation: Perplexity of 26.32245, ROUGE-1 score of 0.2604,
causal coherence of 81.25%, and causal consistency of 85.41%.
1
INTRODUCTION
Large Language Models (LLMs) have proliferated, revolutionising the science of Natural Language Processing (NLP)
by allowing machines to understand content produced by humans. However, such models are created for widely used
languages. There are few resources for the languages used by groups of people who prefer their native language over
English while using computers. One such language is Nepali.
Nepali, the official language of Nepal, is spoken by approximately 44.86% of the country’s population, according to the
2021 Nepal Population and Housing Census. Nepali is also used by communities of India, Myanmar, Bhutan and the
global Nepalese diaspora[1]. About 17.6 million people around the globe speak the Nepali language [2, 3]. Nepali is
based on Devanagiri script, which has 36 consonants, 13 vowels and 10 numerals [4] along with several half-alphabets.
There are no capital letters in the Nepali alphabet, and Nepali writing starts from left to right [4]. As the same word
can be written in different ways in the Nepali language, and there are multiple numbers of alphabets compared to the
English language. This increases the vocabulary size which makes the Nepali language complicated for NLP tasks.
Despite the challenges, the Nepali-specific NLP systems have been developed with a subsequent increase in accuracy.
This research paper intends to create generative large language model for the Nepali language, NepaliGPT. The model
can be used to get responses in the Nepali language and develop generative algorithm based applications such as
chatbots, articles, question answers and so on by finetuning the language model on custom data.

--- Page 2 ---

A PREPRINT - JUNE 23, 2025
Figure 1: System Architecture for NepaliGPT: Data Collection, Model Training, and Fine-Tuning Pipeline
2
LITERATURE REVIEW
In 2017, Google released a paper Transformer is all you need [5] which changed the landscape of NLP with the
introduction of the attention mechanism. Following the transformer architecture, many large pre-trained language
models came to rise, such as BERT, GPT, Roberta, Llama, and Mistral. With the advancement of such models, the
development of NLP in English rises to the top, but the development of NLP in low-resource languages such as Nepali
is still in the early phase. There hasn’t been any groundbreaking development in the Nepali language. There are few
language models that has been developed for the Nepali Corpus major, such as NepaliBERT [6], and NepBERTa [7].
Here, both models were trained on BERT architecture, the first one was trained for Masked Language Modelling (MLM)
along with next-word prediction, and the latter one adapting the RoBERTa’s strategy was only trained for MLM. So,
they are more of Natural Language Understanding (NLU) models i.e. cannot generate Nepali tokens to communicate.
3
Methodology
To build the NepaliGPT, a RAW Nepali corpus was collected by scraping from multiple available public Nepali sites
and translating existing English sources into Nepali. It was further filtered by checking if any alphanumeric character
existed using pre-processing steps, along with manual verification. Finally, Causal Language Model (CLM), i.e. GPT2
architecture, was trained from scratch on the collected Devanagiri Corpus. Then, to answer user’s queries, CLM on the
collected Nepali Question-Answer corpus was further finetuned, which was collected by scraping. The entire process
can be visualised in Figure 1.
3.1
BUILDING NEPALI CORPUS
3.1.1
Data Collection
Initially, we researched a publicly available corpus on the Nepali Language. Below are some of the major corpora we
found.
• Nepali National Corpus: It is a 14 million words corpus that is divided into three types of corpora i.e. written
Corpus, parallel Corpus, and spoken Corpus [8]
2

--- Page 3 ---

A PREPRINT - JUNE 23, 2025
• A Large-Scale Nepali Text Corpus: It is collected by scraping from the internet [9], and has a collection of
over 90 million words in Nepali. The corpus contains news articles, books, and websites. It can be downloaded
freely from the IEEE DataPort website.
• OSCAR Corpus: OSCAR project stands for Open Super-large Crawled Aggregated Corpus. It is a multilingual,
unannotated raw data corpus commonly used in the pretraining of large deep learning models. It is obtained by
filtering Common Crawl Croups. OSCAR Nepali Corpus is a collection of over 100 million words of Nepali
text [10].
Finally, we obtain our final text corpora by combining the following strategies:
• Scraping Nepali News Portal: Using Scrapy, a web crawling framework, and BeautifulSoup, a web scraping
framework, five of the most popular online Nepali news portal i.e. ekantipur.com, nepalinews.com, on-
linekhabar.com, setopati.com, and nagariknews.com were crawled, and finally, text from HTML code was
extracted.
• Downloading available raw Nepali textual data: All scraped content was combined into a single .txt file and
further processed for cleaning. Finally, it was split into multiple .txt files, each containing 10,000 lines, to
facilitate easier data management.
• Scripting on open-source NLP datasets: Publicly available NLP datasets for tasks like sentiment analysis,
fake news detections, etc, in both Nepali and English languages were listed. English Datasets were translated
into Nepali using Google Translate and further verified and filtered using processing steps like looking for
alphanumeric characters. Finally, once all Nepali datasets were prepared, each row was read and compiled
into a raw, unannotated .txt file for training.
3.1.2
CORPUS ANALYSIS
The Nepali corpus, which we named the Devanagari Corpus, was further preprocessed to remove noise and non-Nepali
tokens. To better understand the corpus and identify any potential bias, the corpus was tokenised, and the frequency of
each word was calculated. The wordcloud visualising the most common words in the corpus is represented in Fig. 2,
and the most frequent words and their frequency are represented in Fig. 3.
Figure 2: Wordcloud representation of the Devanagari Corpus
3

--- Page 4 ---

A PREPRINT - JUNE 23, 2025
Figure 3: Bar graph of the most frequent words in the Devanagari Corpus
We further calculated different statistics for our Nepali Corpus, like the total number of tokens, the total number of
sentences, unique words, corpus size, etc. A complete table about statistics can be found in the Table 1:
Nepali Corpus Statistics
Total number of tokens in the corpus
383303233
Total number of sentences across all files
23211003
Combined average sentence length (in words)
16.513859095
Combined average word length (in characters)
5.7533011546
Combined vocabulary size (unique words)
4494764
Size of the whole corpus
9.3 GB
Table 1: Basic text analysis statistics of Nepali Corpus
3.2
Building Nepali CLM
3.2.1
Training Byte Pair Encoding (BPE) based custom Nepali Tokeniser from scratch
We trained a custom BPE tokeniser utilising the collected Nepali Corpus from scratch using Sentencepiece Library [11].
The BPE algorithm [12] works by initialising the vocabulary with all the bytes or characters on the corpus. Then, the
frequency for each character was calculated and repeatedly merging the most common consecutive characters into the
vocabulary till we reach the desired number of tokens. For the Nepali BPE tokeniser, we followed the BPE algorithm
and collected the 10,000 most common consecutive characters or subwords assigned a unique ID for each subword.
A basic overview of training the custom Nepali BPE Tokenizer is shown in Figure 3.
3.2.2
Pretraining CLM for Nepali Language
Firstly, we pretrained the CLM models with our Nepali Corpus to make sure the model has a better understanding of
the Nepali language. For CLM, we used the GPT2 architecture with zero weight initialisation. Using the transformers
4

--- Page 5 ---

A PREPRINT - JUNE 23, 2025
Figure 4: Block Diagram representing methodology for training the custom Nepali BPE Tokeniser
API and our custom Nepali BPE Tokenizer we pre-trained the GPT2 architecture using our collected Nepali Corpus of
13 million Nepali text corpus and learned to predict the next token provided the previous token in the sequence.
3.3
Building Nepali Question Answer Dataset
To make sure our Causal Language Model (CLM) model is able to answer the query provided by the user we collected
the question-answer pair and listed it in the JavaScript Object Notation (JSON) format. The steps followed to build the
Nepali Question Answer dataset are explained in the sections below.
3.3.1
Scraping from Nepali Websites
We collected question-answer pairs by scraping from different public Nepali Websites that have question answers on
them, utilising the Scrapy and BeautifulSoup frameworks. We listed the question-answer pair in JSON. Below is the list
of the websites we used.
• 75 Nepali General Knowledge Quiz Questions Answers
• Nepali GK and Quiz Question Answer
• 150+ Nepali GK Questions and Answers | Nepali Samanya Gyan
3.3.2
Translating publicly available English Question-Answering Dataset
We collected 4000 question-answer pairs from Kaggle Datasets. Then, translated using the Google Translate API and
verified by applying post-processing steps like checking if any alphanumeric character exists. Further verified manually.
5

--- Page 6 ---

A PREPRINT - JUNE 23, 2025
Figure 5: Data format used for Question Answering Task
3.4
Finetuning Nepali CLM on question answering dataset
After we had the tokeniser, models, and supervised dataset from 3.2 and 3.3, we further finetuned the CLM model to
answer questions. We updated the entire weights during this fine-tuning step, making sure the model learns to answer
the user’s query.
Figure 6: Finetuning Nepali Causal Language Model
4
Experimental Setup
4.1
Hyperparameters used for Pretraining Nepali CLM
We ran multiple experiments for building Nepali CLM i.e. one with a smaller data corpus and the other with a bigger
data corpus. For hyperparameters on both use cases, i.e. CLM and finetuning for question answering, we researched
different available solutions in the English-recommended hyperparameter and set it to the optimal values.
6

--- Page 7 ---

A PREPRINT - JUNE 23, 2025
Hyperparameter
Values
Data Corpus size
3.2 GB
learning rate
5e-5
train_batch_size
12
eval_batch_size
5
seed
42
optimizer
Adam
train_batch_size
12
number of epochs
5
mixed precision training
Native AMP
model checkpoint
GPT-2
Table 2: Data size and training Hyperparameters Experiment I
Hyperparameter
Values
Data Corpus size
9.6 GB
learning rate
5e-5
train_batch_size
12
eval_batch_size
5
seed
42
optimizer
Adam
train_batch_size
12
number of epochs
5
mixed precision training
Native AMP
model checkpoint
GPT-2
Table 3: Data size and training hyperparameters for Experiment II
4.2
Hyperparameter for fine-tuning Nepali CLM and building Nepali GPT
Hyperparameter
Values
Base model
NepaliGPT
Max Length
150
Learning Rate
0.01
Weight Decay
0.01
fp16
True
warmup ratio
0.01
seed
42
train batch size
8
test batch size
8
Number of epoch
10
Table 4: Hyperparameter Values for Finetuning NepaliGPT model
4.3
Evaluation Metrics:
4.3.1
ROGUE (Recall Oriented Understanding for Gisting Evaluation) Score
ROGUE is used to calculate the degree of overlap between produced outputs and reference outputs. For CLM, we
removed the second half of 50 sentences and treated the removed part as a reference text, and the tokens predicted by
Nepali CLM as the produced text and calculated the Rogue Score to figure out the evaluation metrics of our CLM
model. Further for Nepali GPT, we have split the collected data into train, validation, and test datasets, among which the
test datasets were not provided during the finetuning step. These test datasets were used to calculate the ROGUE score
to evaluate the performance of Nepali GPT. A few of the samples from the evaluation set are represented in the Fig7.
7

--- Page 8 ---

A PREPRINT - JUNE 23, 2025
Figure 7: Data Samples Used for Evaluation
4.3.2
Casual Coherence and Casual Consistency
To measure these metrics, we used three different human evaluators, each with a different profile. The profile of the
evaluators is as mentioned in the Table 5.
Annotator
Gender
Education
Age
Nepali as Mother Tounge
Annotator 1
Male
Diploma
20-25
Yes
Annotator 2
Female
Bachelors
25-30
No
Annotator 3
Male
Masters
40-50
Yes
Table 5: Data Profile of the Annotators
Casual Coherence means evaluating the model’s output based on whether the model is generating output that makes
sense and is correct. For e.g. CLM produces “The glass fell from the table and broke”. This is a logically correct
sentence, as when glass falls it breaks. So, this can be considered a causally coherent sentence. Casual Consistency
refers to the consistency of that casual coherence in texts generated by CLM with one another. For e.g. we want the
model not to predict that the glass is broken if the glass is grabbed before hitting the ground.
4.3.3
Perplexity
During the training process, perplexity was used as a major evaluation metric. Perplexity refers to how confident the
model is while predicting the tokens based on the context or prior tokens. High perplexity means the model is less
confident in generating the next tokens.
5
RESULTS
5.1
Nepali CLM
Experiments were performed that involved varieties of corpus: small and large, and varieties of hyperparameters:
default, modified and fine-tuned. Among them, othe utput of the Two of the experiments are briefly explained.
For the first experiment, i.e. with a smaller data corpus of 3.2 GB following were the obtained training metrics:
8

--- Page 9 ---

A PREPRINT - JUNE 23, 2025
Epoch
Training Loss
Validation Loss
Perplexity
1.0
6.23568
5.235684
105.5983
2.0
6.22594
5.213568
104.2356
3.0
6.21456
5.211457
97.56823
4.0
6.21365
5.201234
92.56891
5.0
6.20156
5.182356
87.23567
Table 6: Training results from experiment I
Figure 8: Epoch Vs Perplexity from experiment I
For the second experiment, i.e. with a bigger data corpus of 9.6 GB following were the obtained training metrics:
Epoch
Training Loss
Validation Loss
Perplexity
1.0
3.7654
3.6291
37.6789
2.0
3.5857
3.4442
31.31812
3.0
3.5051
3.3439
29.2214
4.0
3.4688
3.3439
28.3294
5.0
3.3968
3.2705
26.32245
Table 7: Training results from experiment II
9

--- Page 10 ---

A PREPRINT - JUNE 23, 2025
Figure 9: Epoch Vs Perplexity from experiment II
5.2
NepaliGPT
We selected 50 unseen data points from our test dataset and calculated the Rogue-N score and causal coherence, and
consistency. The complete metrics are shown below.
ROUGE Type
Score
Validation Loss
Benchmark for English Dataset
ROGUE-1
0.2604
0.59
ROGUE-2
0.1466
0.25
ROGUE-1
0.1501
0.32
Table 8: ROUGE Scores obtained from evaluation data for NepaliGPT
Evaluation criteria
Value
Causal Coherence
81.25 %
Causal Consistency
85.41 %
Table 9: Causal Consistency and Coherence from NepaliGPT model
5.3
Training Time and Inference Time
The pretraining of the causal language model for the development of Nepali CLM took approximately 3 days, 7 hours
and 48 minutes. The model was trained on the NVIDIA Tesla T4 with 16 GB memory, 320+ GB/second bandwidth,
and 2560 Nvidia CUDA cores. The Question Answering model finetuning took approximately 6 hours and 54 minutes
on the same GPU device. The inference time of the NepaliGPT model is 0.7 seconds, i.e. it takes only 0.7 seconds
to generate new texts given some text in any context. This inference time is recorded from the HuggingFace API
endpoints.
10

--- Page 11 ---

A PREPRINT - JUNE 23, 2025
6
CONCLUSION AND FUTURE WORK
In conclusion, we were able to create a decent model by acquiring 26.32245 perplexity, which is comparable to the
perplexity of the GPT-2 model on the English Wikipedia dataset, i.e. 24.35. In addition, the model received a ROUGE-1
score of 0.1501, which is equivalent to the GPT-2 model’s ROUGE-1 score of 0.148 on the English Wikipedia dataset
[13]. Likewise, the model can produce text that is accurate, consistent, and causally coherent based on the human review.
The model’s correctness in terms of causal coherence was 81.25%, and causal consistency was 85.41%. The Nepali
Corpus and NepaliGPT datasets developed during this research can be used to improve the results of generative-based
language models. There is significant potential for further improvements. Usages of bigger and more diverse datasets,
including text from different sectors so that the model has more insights on different terminologies and can be finetuned
to use on different use cases. Further, evaluation of different datasets and approaches like translation+English models
might provide more insights into the model’s capability. Moreover, finetuning on instruction-based datasets might lead
to an instruction-following model.
References
[1] Rajesh Khatiwada. Nepali. Journal of the International Phonetic Association, 39(3):373–380, 2009.
[2] Rajendra Khanal. Linguistic geography of nepalese languages. The Third Pole: Journal of Geography Education,
pages 45–54, 2019.
[3] Annie Rajan and Ambuja Salgaonkar. Survey of nlp resources in low-resource languages nepali, sindhi and
konkani. In Amit Joshi, Mufti Mahmud, Roshan G. Ragel, and Nileshsingh V. Thakur, editors, Information and
Communication Technology for Competitive Strategies (ICTCS 2020), pages 121–132, Singapore, 2022. Springer
Singapore.
[4] Chiranjibi Sitaula, Anish Basnet, and Sunil Aryal. Vector representation based on a supervised codebook for
nepali documents classification. PeerJ Computer Science, 7:e412, 2021.
[5] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz Kaiser, and
Illia Polosukhin. Attention is all you need. Advances in neural information processing systems, 30, 2017.
[6] Shushanta Pudasaini, Subarna Shakya, Aakash Tamang, Sajjan Adhikari, Sunil Thapa, and Sagar Lamichhane.
Nepalibert: Pre-training of masked language model in nepali corpus. In 2023 7th International Conference on
I-SMAC (IoT in Social, Mobile, Analytics and Cloud)(I-SMAC), pages 325–330. IEEE, 2023.
[7] Sulav Timilsina, Milan Gautam, and Binod Bhattarai. Nepberta: Nepali language model trained in a large corpus.
In Proceedings of the 2nd Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics
and the 12th International Joint Conference on Natural Language Processing (Volume 2: Short Papers), pages
273–284, 2022.
[8] Yogendra P Yadava, Andrew Hardie, Ram Raj Lohani, Bhim N Regmi, Srishtee Gurung, Amar Gurung, Tony
McEnery, Jens Allwood, and Pat Hall. Construction and annotation of a corpus of contemporary nepali. Corpora,
3(2):213–225, 2008.
[9] Rabindra Lamsal. A large scale nepali text corpus. IEEE Dataport, 2020.
[10] Pedro Javier Ortiz Suárez, Laurent Romary, and Benoît Sagot. A monolingual approach to contextualized word
embeddings for mid-resource languages. arXiv preprint arXiv:2006.06202, 2020.
[11] Taku Kudo and John Richardson. Sentencepiece: A simple and language independent subword tokenizer and
detokenizer for neural text processing. arXiv preprint arXiv:1808.06226, 2018.
[12] Philip Gage. A new algorithm for data compression. The C Users Journal, 12(2):23–38, 1994.
[13] Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever, et al. Language models are
unsupervised multitask learners. OpenAI blog, 1(8):9, 2019.
11

```
