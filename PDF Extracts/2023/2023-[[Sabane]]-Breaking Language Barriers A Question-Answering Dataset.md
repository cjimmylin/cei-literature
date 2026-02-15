---\ntitle: "2023-[[Unknown]]-Breaking Language Barriers A Question-Answering Dataset - PDF Extract"\nsource_pdf: "2023/2023-[[Unknown]]-Breaking Language Barriers A Question-Answering Dataset.pdf"\npages: 8\nextracted_at: "2026-02-14T02:17:28.269829"\n---\n\n# PDF Extract: 2023-[[Unknown]]-Breaking Language Barriers A Question-Answering Dataset\n\n**Source PDF:** 2023/2023-[[Unknown]]-Breaking Language Barriers A Question-Answering Dataset.pdf\n**Total Pages:** 8\n\n---\n\n## Content\n\n```\n--- Page 1 ---\n\nBreaking Language Barriers: A Question-Answering Dataset for Hindi and
Marathi
Maithili Sabane*1, Onkar Litake*2,
Aman Chadha3,4†
1University of Southern California, 2University of California - San Diego,
3Stanford University, 4Amazon AI
Abstract
The recent advances in deep-learning have led to the devel-
opment of highly sophisticated systems with an unquench-
able appetite for data. On the other hand, building good
deep-learning models for low-resource languages remains a
challenging task. This paper focuses on developing a Ques-
tion Answering dataset for two such languages- Hindi and
Marathi. Despite Hindi being the 3rd most spoken language
worldwide, with 345 million speakers, and Marathi being the
11th most spoken language globally, with 83.2 million speak-
ers, both languages face limited resources for building effi-
cient Question Answering systems. To tackle the challenge
of data scarcity, we have developed a novel approach for
translating the SQuAD 2.0 dataset into Hindi and Marathi.
We release the largest Question-Answering dataset available
for these languages, with each dataset containing 28,000
samples. We evaluate the dataset on various architectures
and release the best-performing models for both Hindi and
Marathi, which will facilitate further research in these lan-
guages. Leveraging similarity tools, our method holds the
potential to create datasets in diverse languages, thereby en-
hancing the understanding of natural language across varied
linguistic contexts. Our fine-tuned models, code, and dataset
will be made publicly available.
Introduction
Question Answering is one of the predominant tasks of Nat-
ural Language Processing that is concerned with developing
systems that can automatically generate or retrieve an an-
swer for the given questions from the text document. Unlike
search systems that generate a series of related documents,
QA models generate an answer from the knowledge base.
These systems have a wide range of applications in infor-
mation extraction and have gained major importance in the
field of artificial intelligence due to the growth in the techni-
cal domain.
These systems differ in the way answers are generated,
such as: (i) extractive QA and (ii) generative QA. Extrac-
tive QA models generate answers directly from the provided
knowledge base, and they often utilize various Transformer-
based models such as BERT. In this approach, the answer is
selected or copied from the original text, serving as a word
*These authors contributed equally.
†Work does not relate to position at Amazon.
marker for the extracted answer. On the other hand, genera-
tive QA models produce free text answers based on contex-
tual information, leveraging text generation models. In this
case, the answer is generated from scratch and is not con-
strained to any specific portion of the original text. Instead,
it is an autonomously created response, distinguishing itself
from the extractive approach.
In addition to the differentiation between extractive and
generative QA models, Question Answering systems can
also be classified based on their domain of operation. This
classification involves distinguishing between open-domain
and closed-domain QA systems. Open-domain QA systems
retrieve the answer from the context of the given document
or a broader knowledge base. In other words, they are not
limited to specific predefined answers and can provide re-
sponses that are not explicitly present in the original text.
These systems are more flexible and capable of handling a
wide range of questions, even those they have not encoun-
tered during training. On the other hand, closed-domain QA
systems are designed to generate answers solely based on
the knowledge contained within their training data. They
are limited to providing responses within a predefined set
of possible answers. Consequently, closed-domain QA sys-
tems may be more suitable for specific use cases with well-
defined and structured questions and answers. In summary,
open-domain QA systems have a broader scope and can
generate responses beyond their training data, while closed-
domain QA systems are more restricted in their answers and
are tailored to specific domains with predefined sets of re-
sponses.
QA models are predominantly built and trained for the
English language and further optimized with a large English
corpus (e.g., SQuAD (Rajpurkar et al. 2016)). Such datasets
are not available for Indian languages, and hence these are
termed low-resource languages. The scarcity of sufficient
corpora hinders the progress of NLP models for these low-
resource languages.
India has a population of 1.4 billion and is home to 122
languages and 270 mother tongues. Indian languages fall in
the minority as far as Natural Language Processing models
are concerned. One of the Indian languages – Hindi – is spo-
ken by 577.8 million people worldwide. Likewise, Marathi,
which is another Indian language, is ranked 11th on the list
of most spoken languages. Despite the popularity of these
arXiv:2308.09862v3  [cs.CL]  17 Feb 2024

--- Page 2 ---\n\nlanguages, NLP systems in these languages remain unex-
plored.
While LLMs have made remarkable progress in natural
language understanding, we’d like to highlight that using
an extracted QA dataset in our research serves a specific
purpose. These datasets provide a structured framework for
benchmarking and evaluating various aspects of language
models, not just their raw performance. Additionally, they
remain relevant for research into data scarcity, model inter-
pretability, fairness, and domain-specific applications. Our
work aims to contribute insights into the limitations and
strengths of traditional QA datasets and LLMs, fostering a
comprehensive understanding of the field. We believe our
research remains valuable even in the context of advanced
LLMs.
Our works’s novelty is grounded in creating a substan-
tial QA dataset for Hindi and Marathi languages. These lan-
guages collectively have a vast user base of 714 million
speakers. This contribution addresses a critical gap in the
availability of resources for these languages. Even though
SQuAD dataset has been present for a long period of time,
still no work has been carried out for these low-resource lan-
guages. There are no Question-answering datasets and mod-
els for Marathi and Hindi. The SQuAD dataset set a prece-
dent for evaluating language models and has led to numer-
ous spin-off works that have expanded our understanding of
reasoning abilities. In a similar way, our work aims to repli-
cate the success of SQuAD by providing a foundational QA
dataset for Hindi and Marathi. The impact of our work ex-
tends beyond the dataset itself. It paves the way for advance-
ments in natural language understanding, reasoning, and ma-
chine learning applications for Hindi and Marathi-speaking
communities.
To the best of the authors’ knowledge, this dataset is the
largest for Hindi and Marathi QA. Our approach tries to re-
solve the difficulty in accurately determining the index of
the answer within the context. Our approach is explained in
the Dataset Creation section.
Our contributions can be summarized as follows:
• We present the largest Question-Answering dataset re-
leased for both Marathi and Hindi languages.
• We release the best-performing model for Question An-
swering based on our comprehensive evaluation and ex-
perimentation.
Related Work
Question-Answering models (Allam and Haggag 2012) are
artificial intelligence or deep learning algorithms designed
to respond to queries within specific contexts and, at times,
even without any context. These models must possess a
profound understanding of the language’s structure and se-
mantics, enabling them to locate the answer phrase within
the given context accurately. However, to achieve such pro-
ficiency, these models require extensive training on large
datasets. Manual creation of such datasets poses a significant
challenge due to the time-consuming annotation process in-
volved.
To address the scarcity of datasets for new languages,
methods have been explored to create datasets based on ex-
isting ones. Translating the context and answers within the
dataset is a relatively straightforward task. However, finding
the exact index of the translated answer within the context
becomes significantly more difficult. This challenge arises
from the black-box nature of Language Models (LMs),
where the translation of the answer, with or without sur-
rounding context, can differ, making it challenging to di-
rectly determine the index at which the answer lies within
the context.
The Dataset Creation section provides a more detailed ex-
planation of the complexities encountered during this pro-
cess. Consequently, constructing a model capable of deliv-
ering accurate answers becomes a formidable task due to the
scarcity of datasets and the associated challenges that need
to be addressed.
The availability of large-scale datasets, such as SQuAD
(Rajpurkar, Jia, and Liang 2018), Natural Questions (NQ)
(Kwiatkowski et al. 2019), CoQA (Reddy, Chen, and Man-
ning 2018), and others, play a pivotal role in enhancing the
model training process, especially for deep learning tech-
niques. Deep Learning models have an insatiable data ap-
petite; they require vast amounts of annotated data for effec-
tive training and performance improvement.
These large datasets offer a rich variety of real-world ex-
amples, covering diverse contexts and language patterns, al-
lowing deep-learning models to learn from a wide range
of scenarios. Consequently, the models can better grasp the
complexities and nuances of natural language and, in turn,
produce more accurate and robust results.
By leveraging large datasets, deep learning algorithms can
extract intricate patterns, correlations, and semantic relation-
ships, enabling them to provide more meaningful responses
and perform better in various natural language processing
tasks, including Question Answering. Therefore, the signifi-
cance of large datasets cannot be understated, as they are in-
strumental in feeding the data hunger of deep learning tech-
niques and substantially elevating their capabilities to com-
prehend and process natural language.
Most of these datasets are created for high-resource lan-
guages like English, German, etc., which in turn lead to the
development of better quality models in those specific lan-
guages. Due to the lack of availability of good quality data
in the low-resource languages, research and development is
hampered. The amount of work done on low-resource Indian
languages like Hindi and Marathi is inadequate in compari-
son to English and German.
(Gupta and Khade 2020) in their work experimented with
multilingual models on the task of Machine Comprehension,
which is a sub-task of Question-Answering (QA) for Hindi
and English. They experimented with mBERT on monolin-
gual, zero-shot, and cross-lingual fine-tuning setups. (Kumar
et al. 2022) fine-tuned an mBERT-based QA model using
augmented data by translating and transliterating QA sam-
ples of the target language into other languages, which in
turn helped to boost the performance of the models. (Lewis
et al. 2019b) in order to tackle the difficulty of availability of
datasets in languages other than English presented MLQA, a

--- Page 3 ---\n\nCreate subsets with 
window size. Move the 
window with 
sliding step = window size
Consider the subset with 
highest similarity
Merge the preceeding and 
succeeding subsets with subset 
with highest similarity
Create subsets with window 
size. Move the window with 
Sliding step=1
consider the subset with 
highest similarity
Final Answer
Context
Window Size:- No. of words in the translated answer 
Sliding step:- No. of steps the window moves horizontally between consecutive windows
Figure 1: Sliding window technique for answer extraction.
multi-way aligned extractive QA evaluation benchmark for
excelling research in this area. It consisted of 12,000 QA in-
stances in English and 5,0000 QA instances in 7 different
languages, which included Hindi. (Gupta et al. 2018a) cu-
rated a dataset containing 500 articles from 6 different do-
mains. 250 of these articles consisted of English and Hindi
documents, respectively. A total of 5,495 QA pairs were cre-
ated. Difficulties in answering questions in multiple domains
and languages were evaluated and necessary resources for
developing a baseline model and bench-marking were as-
sessed.
(Artetxe, Ruder, and Yogatama 2020) released the
XQuAD dataset, which consisted of 240 paragraphs and
1190 question-answer pairs from SQuAD v1.1, which was
translated by professional translators into ten different lan-
guages. The primary motivation behind this was to put forth
a more comprehensive cross-lingual benchmark. (Anuran-
jana, Rao, and Mamidi 2019a) released the first curated
dataset, which was divided according to the level of diffi-
culty of different grades for primary education. It consists
of a total of 24 passages and 127 questions. As a part of the
competition ‘Challenge in AI for India’, Google Research
released a dataset named ‘chaii-1’ (Howard et al. 2021),
which consists of QA pairs in Hindi and Tamil without the
use of translation.
Although the scarcity of datasets for Hindi is conspicu-
ous, some datasets do exist. MLQA (MultiLingual Question
Answering (Lewis et al. 2019a) is a benchmark dataset con-
sisting of 5K extractive QA instances in seven languages,
Hindi being one of them. The MMQA (Gupta et al. 2018b)
dataset has around 6000 English-Hindi Question Answering
pairs. HindiRC (Anuranjana, Rao, and Mamidi 2019b) is a
dataset for Reading Comprehension in Hindi containing 127
questions and 24 passages.
For the Marathi language, however, there exists no such
public datasets to date. (Govilkar 2018) proposed a QA
system for the Marathi language by making use of on-
tology. Domain-specific knowledge regarding semantic re-
lationships and limitations in the relevant domains is ex-
pressed using ontologies. (Shelke, Naik, and C 2024) is
working on curating datasets from textbooks for the pri-
mary grade classes. The dataset has a total of 901 questions.
(Phade and Haribhakta 2021) proposed a system QA sys-
tem for Marathi using transfer learning which utilizes the
word embedding from a trained multilingual BERT model
on a small custom dataset similar to SQuAD. (Kamble S.
2018) developed a system for English-Marathi QA by man-
ually scraping 1000 questions from Kaun Banega Crorepati
(KBC) and translating them into Marathi.
Experimental Setup
Data Collection
As the foundation of our research, we utilized the SQuAD
dataset (Rajpurkar, Jia, and Liang 2018) to develop our
Question-Answering system. It serves as a starting point for
our work, and we build upon it to create a dataset specif-
ically tailored for Marathi and Hindi languages. By lever-
aging the existing SQuAD dataset, we ensured a robust and
standardized framework for the comparison and evaluation
of our models’ performance. This dataset comprises a col-
lection of questions generated by crowd workers pertaining
to a set of Wikipedia articles, with the goal of testing read-
ing comprehension. Each question in the dataset requires an
answer in the form of a specific text segment or span derived
from the corresponding reading passage. Alternatively, some
questions may not have an answer and are labeled as unan-
swerable.
Dataset Creation
Following is the structure of a single example of the SQuAD
dataset:
We translate the given SQuAD dataset from English to
Marathi and Hindi. We used IndicTrans (Ramesh et al. 2022)
by AI4Bharat for Machine Translation. In order to develop
a Question-Answering model, it is necessary to provide the
character start index of the answer within the context. How-
ever, due to variations in sentence structures across different
languages, the original dataset’s indices cannot be directly
utilized. To address this, we devised a novel method to deter-
mine the optimal indices accurately. Ensuring that the text in
the answer aligns precisely with its appearance in the context
poses a challenge due to the black-box nature of machine
learning models, which can result in varied translations of
the text.

--- Page 4 ---\n\nDuring the compilation of the dataset, we address two pri-
mary challenges:
• Determining the appropriate answer start index within
the context.
• Replacing the translated answer with the exact corre-
sponding answer as it appears in the context, ensuring
precise alignment and maintaining the original meaning.
Figure 1 explains the process of extracting the final an-
swer from the context. To identify the indices of the answer
within the context, we employed a sliding window tech-
nique. This approach involved utilizing a window of length
equal to the size of the answer text. By iterating through
the context with this window size, we aimed to locate the
subset of the context that exhibited the highest similarity to
the answer text. This enabled us to pinpoint the precise in-
dices corresponding to the answer within the context. We
have used the MahaNLP (Joshi 2022c) library to calculate
the similarity. To address the possibility of the final answer
being spread across multiple subsets, we adopt a merging ap-
proach. After identifying the subset with the maximum simi-
larity, we merge it with the subsets preceding and succeeding
it. This consolidation allows us to consider the entire range
where the answer might reside. To determine the final subset
with maximum similarity, we traverse through the merged
subsets with a window size similar to the previous approach,
moving a distance of 1 at a time. Moreover, along with the
character indices, we also calculate the token start and token
end index of the answer, which can contribute to broader ap-
plications in model training and development. Additionally,
once we obtain the index of the answer in the context, we re-
place the answer text with the subset exhibiting the highest
similarity. This methodology ensures comprehensive cover-
age of the answer while maintaining accuracy through the
similarity-based selection process.
The reason to use these specific models for translation and
calculating similarity is that these are currently the only/best
performing open source models according to our knowledge.
The non-existent of multiple variant of these models again
highlights the scarcity of resources for these low-resource
languages.
Following is an example in English. The Translated An-
swer will originally be in target language(Hindi/Marathi),
here it is kept in English for reader’s convenience.
• Context: “The quick brown fox jumped over the lazy
dog. The dog persuaded the fox through the forest. Even-
tually, the fox escaped and the dog returned home.”
• Real Answer: persuaded the fox through
• Translated Answer: chased the fox through
• Window size: length(Translated Answer) = 4
Figure 2 provides an illustration of the sliding window
technique for locating the final answer in the context.
The decision to employ a stride of window size was made
with computational efficiency in mind. The need for such
a process arises because the answer is paraphrased during
translation and does not always lie in the context as it is.
While the average context length is 78 words, it’s worth not-
ing that translation, especially for multiple examples, which
Tag
Train
Test
Valid
Date
2113
464
413
Measure
4495
927
974
Organization
1412
321
271
Location
2069
459
466
Person
3415
606
697
Designation
136
18
29
Time
59
8
14
Table 1: Count of NER tags present in the answer text.
totals around 28,000, can impose a significant computational
load. Our approach aims to strike a balance between compu-
tational efficiency and adequate coverage of the data.
We believe this approach efficiently assists us in locating
the answer. We’d like to emphasize that even with a smaller
step size from the start, we expect to obtain the same answer
as with our mentioned approach.
Dataset Statistics
The dataset used for research was curated to encompass a
wide array of textual data across different domains. Due
to computational limitations, we translated 28,000 samples
from SQuAD 2.0 using a machine translation model for In-
dic Languages. We use 21000 samples for training and 4200
samples each for testing and validation, respectively. Each
sample is divided into title, context, question, answer, and
answer start. On average, the context segments contain 78
words, while the question and answers have average lengths
of 7 and 2 words, respectively. We observe similar trends in
terms of context, question and answer lengths for test and
validation sets.
Moreover, an analysis of NER tags reveals additional in-
sights into the dataset. Table 1 shows to count of each tag
present in the answers for each of the train test and valida-
tion datasets. We use the MahaNLP library, trained on the
L3Cube MahaNER (Litake et al. 2022) dataset, to predict
the NER tags.
Experimentation
Model Selection
Transformer-based (Vaswani et al. 2023) models have dom-
inated the field of natural language processing due to their
remarkable ability to capture complex linguistic relation-
ships. This architecture’s capacity for bidirectional context
understanding allows it to grasp contextual nuances and de-
pendencies within the text, making it highly effective for
tasks like language translation, sentiment analysis, and ques-
tion answering. Moreover, as they are pre-trained on large
corpora and subsequently fine-tuned on task-specific data,
transformers contribute to their widespread adoption and
consistent achievement of state-of-the-art results across var-
ious benchmarks.
To establish a baseline we have used several well-known
LMs, including monolingual and multilingual. Following
are the general LMs used for training on our dataset:

--- Page 5 ---\n\nWindow Size=4
Final Answer
Create subsets with 
window size=4
Move the window with 
sliding step = 1
Consider the subset with 
highest similarity 
(highlighted in red)
Merge the previous and 
next subsets
Create subsets with 
window size= 4
Move the window with 
sliding step = 4
persuaded the fox through
Figure 2: Illustration of the method using an English example.
Model
EM(%)
Rouge-2
Rouge-L
BLEU (Unigram)(%)
BLEU (Bigrams)(%)
mBERT
36.3
0.31
0.58
49.67
30.54
XLM-RoBERTa
43.16
0.33
0.63
55.98
33.87
Distil-BERT
31.14
0.27
0.52
41.41
25.26
Hindi BERT
47.84
0.36
0.66
61.47
38.51
Hindi RoBERTa
43.33
0.34
0.63
56.28
34.44
Table 2: Exact Match (EM), Rouge-N, Rouge-L, BLEU (Unigram), BLEU (Bigrams) for various models on Hindi dataset.
mBert: mBERT (Pires, Schlinger, and Garrette 2019)
stands for Multilingual BERT, is a variant of the BERT
model pre-trained on 104 languages that makes it adaptable
to various multilingual tasks, including Question Answer-
ing. Through its tokenization, segment embedding, and po-
sitional encoding techniques, mBERT can precisely capture
the intricate structures of questions and passages.
XLM-RoBERTa: XLM-RoBERTa (Conneau et al. 2020)
is an evolution of the original BERT model and makes sev-
eral modifications to the training procedure, leading to im-
proved performance. Some of the changes include larger
batch size, longer training time, and larger input. It is an
extension of Roberta (Liu et al. 2019) that is designed
to handle multilingual and cross-lingual tasks. It extends
the RoBERTa architecture to handle cross-lingual tasks by
learning shared representations of words in different lan-
guages.
DistilBERT: DistilBERT (Sanh et al. 2019) is a distilled
version of the BERT base multilingual model. DistilBERT
reduces the usage of computational resources by using a
distillation technique that transfers the knowledge from the
larger BERT model to a smaller one. It achieves faster infer-
ence times and requires less memory, making it well-suited
for deployment in resource-constrained environments.
The Marathi language-specific models utilized for train-
ing on our dataset were introduced by (Joshi 2022b) in
their recent research. These models consist of MahaBERT,
a Marathi BERT model, which is a fine-tuned version of
the multilingual BERT-base-cased model. MahaRoBERTa,
a Marathi RoBERTa model, which is based on the multi-
lingual RoBERTa (xlm-roberta-base) model. All of
these models are fine-tuned using L3Cube-MahaCorpus and
other publicly available Marathi monolingual datasets.
Similarly, the Hindi language-specific models utilized for
training on our dataset were introduced by (Joshi 2022a).
These models consist of HindBERT, a Hindi BERT model,
which is a fine-tuned version of the multilingual BERT-base-
cased model. HindRoBERTa, a Hindi RoBERTa model,
which is based on the multilingual RoBERTa (xlm-roberta-
base) model. All of these models are fine-tuned on publicly
available Hindi monolingual datasets.
The decision to focus on BERT-based models aligns with
the primary motivation of our paper, which was to create a
comprehensive dataset for Question and Answering (QnA)

--- Page 6 ---\n\nModel
EM(%)
Rouge-2
Rouge-L
BLEU (Unigram)(%)
BLEU (Bigrams)(%)
mBERT
28.78
0.32
0.54
43.34
30.34
XLM-RoBERTa
37.92
0.34
0.57
47.65
31.42
Distil-BERT
25.11
0.27
0.46
35.59
24.00
MahaBERT
42.97
0.38
0.62
57.42
39.70
MahaRoBERTa
38.52
0.35
58
52.03
35.64
Table 3: Exact Match (EM), Rouge-N, Rouge-L, BLEU (Unigram), BLEU (Bigrams) for various models on Marathi dataset.
tasks. We used BERT-based models for evaluation primarily
to ensure the correctness and effectiveness of our dataset.
These models have established themselves as a benchmark
for natural language understanding, and by using them, we
aimed to guarantee the reliability and generalizability of our
dataset.
To keep up with the ongoing trend on usage of LLMs, we
were not able to employ them as according to our knowledge
currently there are no open-source LLM for low-resource
languages such as Marathi and Hindi. Our extensive survey
of the existing multilingual LLMs has shown that their per-
formance is suboptimal for various tasks in these languages.
Experimental Settings
We fine-tuned the aforementioned models on our dataset us-
ing PyTorch (Paszke et al. 2019). The models were fine-
tuned using a single Tesla T4 GPU, and 12 GB RAM. A
batch size of 2 was employed, and optimization was per-
formed using the AdamW optimizer (Kingma and Ba 2017)
with a learning rate of 1e-5. The training process spanned
five epochs for all the models, with gradient accumulation
taking place over two batches. These hyperparameters col-
lectively shaped the training dynamics and contributed to the
outcomes of the experiments.
Results
In this study, we have experimented with various monolin-
gual and multi-lingual LMs on our dataset for Hindi and
Marathi. We have used the following evaluation metrics:
Exact Match: It measures the percentage of instances
where the predicted output exactly matches the reference
output.
Rouge-2: ROUGE (Lin 2004) (Recall-Oriented Under-
study for Gisting Evaluation) is used for evaluating the qual-
ity of machine-generated text. Rouge-N is one specific met-
ric within the Rouge family, where “N” refers to the size of
the n-grams being compared. Here we have calculated the
Rouge-2 score, which indicates that bi-grams are compared.
The reason for choosing a bi-gram is stated at the end of the
section.
Rouge-L: ROUGE-L measures the longest common sub-
sequence (LCS) between the predicted text and the refer-
ence text. The LCS represents the longest sequence of words
that appears in both the candidate and reference text. Rouge
score are represented between scale of 0 to 1.
BLEU: BLEU (Papineni et al. 2002) (Bilingual Eval-
uation Understudy) measures the similarity between the
machine-generated output and one or more human reference
outputs. BLEU calculates precision scores based on over-
lapping n-grams. Here we have selected n = 2 to calculate
overlapping unigram and bi-grams. The reason for choosing
n to be two is stated at the end of the section.
As mentioned in the ‘Dataset Statistics’ section, the aver-
age number of words for ‘answer’ (predicted text) is 2; hence
we decided to keep n = 2 for Rouge and BLEU scores.
The results have been reported in Table 2 and Table 3, re-
spectively. Hindi BERT outperforms the other models on the
Hindi dataset; similarly ‘MahaBERT’ model performs best
on the Marathi dataset.
The reason for Indic models outperforming general mod-
els is that these language-specific models focus solely on one
language, such as Marathi or Hindi, in contrast to general
models designed to work with many languages. This ded-
icated training approach helps them understand the unique
aspects of that language – things like how words are used,
sentence structures, and specific context details that are part
of the language’s nature. It makes the model knowledge-
able about specific topics, phrases, and everyday words used
for that specific languages. In short, the success of models
like MahaBERT and Hindi BERT comes from their focused
training on a particular language.
Conclusion
We introduce the biggest dataset for Question-Answering in
Marathi and Hindi languages consisting of 28,000 samples.
This is the first step taken to reduce the missing literature
in existing research work. With the availability of models
for Machine Translation, and Sentence Similarity, the same
method can be used to create datasets for different Indic
languages. Hindi BERT performs best for QA on the Hindi
dataset; similarly, ‘MahaBERT’ performs best for QA on the
Marathi dataset. We plan to release these models along with
our dataset. We want to encourage researchers to build better
models for QA tasks. We think that the development of con-
versational AI for the Marathi language will greatly benefit
from the use of our corpus.
Reproducibility
The pre-trained models, dataset, and code will be made pub-
licly available.
References
Allam, A. M. N.; and Haggag, M. H. 2012. The question
answering systems: A survey. International Journal of Re-
search and Reviews in Information Sciences (IJRRIS), 2(3).

--- Page 7 ---\n\nAnuranjana, K.; Rao, V. A.; and Mamidi, R. 2019a.
HindiRC: A Dataset for Reading Comprehension in Hindi.
In 20th International Conference on Computational Linguis-
tics and Intelligent Text.
Anuranjana, K.; Rao, V. A.; and Mamidi, R. 2019b.
HindiRC: A Dataset for Reading Comprehension in Hindi.
In 20th International Conference on Computational Linguis-
tics and Intelligent Text.
Artetxe, M.; Ruder, S.; and Yogatama, D. 2020.
On the
Cross-lingual Transferability of Monolingual Representa-
tions.
In Proceedings of the 58th Annual Meeting of the
Association for Computational Linguistics. Association for
Computational Linguistics.
Conneau, A.; Khandelwal, K.; Goyal, N.; Chaudhary, V.;
Wenzek, G.; Guzm´an, F.; Grave, E.; Ott, M.; Zettlemoyer,
L.; and Stoyanov, V. 2020. Unsupervised Cross-lingual Rep-
resentation Learning at Scale. In Proceedings of the 58th
Annual Meeting of the Association for Computational Lin-
guistics, 8440–8451. Online: Association for Computational
Linguistics.
Govilkar, J. W., Sharvari S.; Bakal. 2018. Question Answer-
ing System Using Ontology in Marathi Language.
Gupta, D.; Kumari, S.; Ekbal, A.; and Bhattacharyya, P.
2018a. MMQA: A Multi-domain Multi-lingual Question-
Answering Framework for English and Hindi. In Proceed-
ings of the Eleventh International Conference on Language
Resources and Evaluation (LREC 2018). Miyazaki, Japan:
European Language Resources Association (ELRA).
Gupta, D.; Kumari, S.; Ekbal, A.; and Bhattacharyya, P.
2018b. MMQA: A Multi-domain Multi-lingual Question-
Answering Framework for English and Hindi.
In chair),
N. C. C.; Choukri, K.; Cieri, C.; Declerck, T.; Goggi, S.;
Hasida, K.; Isahara, H.; Maegaard, B.; Mariani, J.; Mazo,
H.; Moreno, A.; Odijk, J.; Piperidis, S.; and Tokunaga,
T., eds., Proceedings of the Eleventh International Confer-
ence on Language Resources and Evaluation (LREC 2018).
Miyazaki, Japan: European Language Resources Associa-
tion (ELRA). ISBN 979-10-95546-00-9.
Gupta, S.; and Khade, N. 2020. BERT Based Multilingual
Machine Comprehension in English and Hindi.
Howard, A.; Nathani, D.; thakkar, D.; Elliott, J.; Talukdar,
P.; and Culliton, P. 2021. chaii - Hindi and Tamil Question
Answering.
Joshi, R. 2022a.
L3Cube-HindBERT and DevBERT:
Pre-Trained BERT Transformer models for Devanagari
based Hindi and Marathi Languages.
arXiv preprint
arXiv:2211.11418.
Joshi, R. 2022b.
L3Cube-MahaCorpus and MahaBERT:
Marathi Monolingual Corpus, Marathi BERT Language
Models, and Resources. In Proceedings of the WILDRE-6
Workshop within the 13th Language Resources and Evalua-
tion Conference, 97–101. Marseille, France: European Lan-
guage Resources Association.
Joshi, R. 2022c. L3Cube-MahaNLP: Marathi Natural Lan-
guage Processing Datasets, Models, and Library.
arXiv
preprint arXiv:2205.14728.
Kamble S., B. S. 2018. Learning to Classify Marathi Ques-
tions and Identify Answer Type Using Machine Learning
Technique.
Kingma, D. P.; and Ba, J. 2017.
Adam: A Method for
Stochastic Optimization. arXiv:1412.6980.
Kumar, G. K.; Gehlot, A. S.; Mullappilly, S. S.; and Nan-
dakumar, K. 2022. MuCoT: Multilingual Contrastive Train-
ing for Question-Answering in Low-resource Languages.
Kwiatkowski, T.; Palomaki, J.; Redfield, O.; Collins, M.;
Parikh, A.; Alberti, C.; Epstein, D.; Polosukhin, I.; Kelcey,
M.; Devlin, J.; Lee, K.; Toutanova, K. N.; Jones, L.; Chang,
M.-W.; Dai, A.; Uszkoreit, J.; Le, Q.; and Petrov, S. 2019.
Natural Questions: a Benchmark for Question Answering
Research. Transactions of the Association of Computational
Linguistics.
Lewis, P.; O˘guz, B.; Rinott, R.; Riedel, S.; and Schwenk, H.
2019a. MLQA: Evaluating Cross-lingual Extractive Ques-
tion Answering. arXiv preprint arXiv:1910.07475.
Lewis, P.; O˘guz, B.; Rinott, R.; Riedel, S.; and Schwenk, H.
2019b. MLQA: Evaluating Cross-lingual Extractive Ques-
tion Answering.
Lin, C.-Y. 2004. ROUGE: A Package for Automatic Evalu-
ation of summaries. 10.
Litake, O.; Sabane, M. R.; Patil, P. S.; Ranade, A. A.; and
Joshi, R. 2022. L3Cube-MahaNER: A Marathi Named En-
tity Recognition Dataset and BERT models.
In Proceed-
ings of the WILDRE-6 Workshop within the 13th Language
Resources and Evaluation Conference, 29–34. Marseille,
France: European Language Resources Association.
Liu, Y.; Ott, M.; Goyal, N.; Du, J.; Joshi, M.; Chen, D.;
Levy, O.; Lewis, M.; Zettlemoyer, L.; and Stoyanov, V.
2019. RoBERTa: A Robustly Optimized BERT Pretraining
Approach. arXiv:1907.11692.
Papineni, K.; Roukos, S.; Ward, T.; and Zhu, W.-J. 2002.
BLEU: A Method for Automatic Evaluation of Machine
Translation.
In Proceedings of the 40th Annual Meeting
on Association for Computational Linguistics, ACL ’02,
311–318. USA: Association for Computational Linguistics.
Paszke, A.; Gross, S.; Massa, F.; Lerer, A.; Bradbury, J.;
Chanan, G.; Killeen, T.; Lin, Z.; Gimelshein, N.; Antiga, L.;
Desmaison, A.; K¨opf, A.; Yang, E.; DeVito, Z.; Raison, M.;
Tejani, A.; Chilamkurthy, S.; Steiner, B.; Fang, L.; Bai, J.;
and Chintala, S. 2019. PyTorch: An Imperative Style, High-
Performance Deep Learning Library. arXiv:1912.01703.
Phade, A.; and Haribhakta, Y. 2021. Question Answering
System for low resource language using Transfer Learning.
In 2021 International Conference on Computational Intelli-
gence and Computing Applications (ICCICA), 1–6.
Pires, T.; Schlinger, E.; and Garrette, D. 2019. How multi-
lingual is Multilingual BERT? arXiv:1906.01502.
Rajpurkar, P.; Jia, R.; and Liang, P. 2018. Know What You
Don’t Know: Unanswerable Questions for SQuAD.
Rajpurkar, P.; Zhang, J.; Lopyrev, K.; and Liang, P. 2016.
SQuAD: 100,000+ Questions for Machine Comprehension
of Text. arXiv:1606.05250.

--- Page 8 ---\n\nRamesh, G.; Doddapaneni, S.; Bheemaraj, A.; Jobanputra,
M.; AK, R.; Sharma, A.; Sahoo, S.; Diddee, H.; J, M.; Kak-
wani, D.; Kumar, N.; Pradeep, A.; Nagaraj, S.; Deepak, K.;
Raghavan, V.; Kunchukuttan, A.; Kumar, P.; and Khapra,
M. S. 2022. Samanantar: The Largest Publicly Available
Parallel Corpora Collection for 11 Indic Languages. Trans-
actions of the Association for Computational Linguistics,
10: 145–162.
Reddy, S.; Chen, D.; and Manning, C. D. 2018. CoQA: A
Conversational Question Answering Challenge.
Sanh, V.; Debut, L.; Chaumond, J.; and Wolf, T. 2019. Dis-
tilBERT, a distilled version of BERT: smaller, faster, cheaper
and lighter. ArXiv, abs/1910.01108.
Shelke, B. A.; Naik, R. R.; and C, N. M. 2024. Database
Creation for Marathi QA System.
Vaswani, A.; Shazeer, N.; Parmar, N.; Uszkoreit, J.; Jones,
L.; Gomez, A. N.; Kaiser, L.; and Polosukhin, I. 2023. At-
tention Is All You Need. arXiv:1706.03762.
\n```\n