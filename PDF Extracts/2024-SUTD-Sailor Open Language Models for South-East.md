---
title: "2024-SUTD-Sailor Open Language Models for South-East - PDF Extract"
source_pdf: "2024-SUTD-Sailor Open Language Models for South-East.pdf"
pages: 30
extracted_at: "2026-02-13T09:15:43.954237"
---

# PDF Extract: 2024-SUTD-Sailor Open Language Models for South-East

**Source PDF:** 2024-SUTD-Sailor Open Language Models for South-East.pdf
**Total Pages:** 30

---

## Content

```
--- Page 1 ---

Technical Report
Sailor: Open Language Models for South-East Asia
Longxu Dou1∗Qian Liu1 ∗
Guangtao Zeng2
Jia Guo1
Jiahui Zhou1
Wei Lu2
Min Lin1
1Sea AI Lab, Singapore
2SUTD, Singapore
{doulx, liuqian}@sea.com
Homepage: https://sailorllm.github.io
Model: https://huggingface.co/sail
Abstract
We present Sailor, a family of open language models ranging from 0.5B
to 7B parameters, tailored for South-East Asian (SEA) languages. These
models are continually pre-trained from Qwen1.5, a great language model
for multilingual use cases. From Qwen1.5, Sailor models accept 200B to
400B tokens, primarily covering the languages of English, Chinese, Viet-
namese, Thai, Indonesian, Malay, and Lao. The training leverages several
techniques, including BPE dropout for improving the model robustness,
aggressive data cleaning and deduplication, and small proxy models to
optimize data mixture. Experimental results on four typical tasks indicate
that Sailor models demonstrate strong performance across different bench-
marks, including commonsense reasoning, question answering, reading
comprehension and examination. Embracing the open-source spirit, we
share our insights through this report to spark a wider interest in develop-
ing large language models for multilingual use cases.
Takeaway
(1) Language models struggle with multiple languages, and continual pre-training presents
an opportunity to improve specific language capabilities. (2) Code-switching techniques
can be beneficial in multilingual scenarios, improving the ability to handle language mix-
ing. (3) Language models are sensitive to subword segmentation, and techniques like BPE
dropout can improve model robustness. (4) Even available high-quality multilingual cor-
pora may require further data deduplication and cleaning. (5) Simulation experiments on
smaller models can provide insights into performance trends for large-scale experiments.
SlimPajama
SkyPile
Wikipedia
MADLAD-400
Translation
CC100
OpenSubtitles
Data Collection
Dataset for SEA Languages
Data Preprocessing
Continual Pre-training
Qwen
Mistral
BPE Dropout
Data Mixture
Simulation
Document-Level 
Code-Switching
Aggressive Data 
Cleaning
Aggressive Data 
Deduplication
Cleaned
Datasets
Proxy Model
Fix Escape Problem
Bidirectional Data
Llama
LLM
Sailor
⋯
Learning Rate
Tuning
Merging Adjacent 
Short Examples
Dataset for Replay
Figure 1: The pipeline of building Sailor, with insights marked by stars.
∗The first two authors contributed equally.
1
arXiv:2404.03608v1  [cs.CL]  4 Apr 2024

--- Page 2 ---

Technical Report
1
Introduction
Recent years have witnessed an astonishing surge in the performance of large language
models (LLMs), driven by the rapid growth of Internet data (Rana, 2010) and advances in
pre-training techniques. The advent of models such as GPT-3 (Brown et al., 2020), Gem-
ini (Anil et al., 2023), and Llama (Touvron et al., 2023a) has fueled ever-increasing expec-
tations for LLMs across diverse domains, ranging from creative writing (Wang et al., 2024),
coding (Lozhkov et al., 2024) and logical reasoning (Zhong et al., 2023). Developing high-
quality models crucially depends on access to a large-scale and high-quality dataset. The
ubiquity of digitized English content has established it as a preeminent source for training
LLMs. Consequently, mainstream LLMs (Touvron et al., 2023a; AI et al., 2024; Bai et al.,
2023) tend to heavily rely on English datasets. For example, 89.70% of the training data of
Llama-2 is English (Touvron et al., 2023b). However, these English-centric LLMs frequently
encounter difficulties in achieving comparable performance across other languages (e.g.,
Thai). This phenomenon, termed the curse of multilinguality (Chang et al., 2023), implies
that an over-reliance on English training leads to sub-optimal performance for non-English
languages, as the model lacks sufficient exposure to other languages during pre-training.
In this paper, we aim to develop LLMs that perform well across the South-East Asia (SEA)
region, encompassing a range of languages that include English, Chinese, Vietnamese,
Thai, Indonesian, Malay, and Lao. We share both successful experiences and failed at-
tempts in a completely open manner to accelerate the development of LLMs for the SEA
region. Specifically, we introduce and discuss the benefits of merging adjacent short exam-
ple, the document-level code-switching and the word-level code-switching, as illustrated
in Figure 1. Additionally, we share all of our data cleaning pipeline and deduplication pro-
cedure that turns out to be extremely important for the quality of LLMs, especially in the
scenario of continual pre-training. As for the tokenization, we explore the usage of BPE
Dropout (Provilkov et al., 2020) and highlight its importance for the robustness of LLMs.
Finally, we use small models as proxy to optimize the hyper-parameter for continual pre-
training, including the learning rate and data mixture ratio of different data sources.
2
Insights
During our development, we perform ablation studies on small LMs to understand the
impact of various strategies. We then apply the key insights gained from these studies to
improve LLMs. Most of the experimental results are obtained from three series of models:
our internal 120M model trained on 20B English tokens using SlimPajama (Soboleva et al.,
2023), the TinyLlama 1.1B model (Zhang et al., 2024), and the Qwen1.5-0.5B model (Bai
et al., 2023). All techniques we have considered are listed in Table 1.
2.1
Data
Merging Adjacent Short Examples
Several studies have emphasized the importance of
deduplication (Lee et al., 2022), with some popular corpora undergoing deduplication at
Technique
Stage
Used
Note
Merging Adjacent Short Examples
Data
Yes
Improve Performance
Document-Level Code-Switching
Data
Yes
Improve Performance
Word-Level Code-Switching
Data
No
Marginal Effect w. Document-Level
Aggressive Data Deduplication
Data
Yes
Improve Performance
Aggressive Data Cleaning
Data
Yes
Improve Performance
Vocabulary Expansion
Tokenization
No
Challenging to Apply
BPE Dropout
Tokenization
Yes
Improve Robustness
Learning Rate Tuning
Training
Yes
Accelerate the Training
Data Mixture Simulation
Training
Yes
Balance Different Languages
Table 1: The techniques we mainly consider during our development.
2

--- Page 3 ---

Technical Report
the paragraph level, resulting in a final corpus comprising unique paragraphs such as
CC100 (Wenzek et al., 2020a). The approach enhances data efficiency by maximizing the
number of unique tokens the model encounters, but it can adversely impact model perfor-
mance as the connections between different pieces within the context become less relevant.
To mitigate the issue, we have employed a simple method of randomly combining several
adjacent examples into one example before applying a global shuffle. The method can be
applied because the deduplicated paragraphs still retain the order in which they appear in
the original documents, allowing for the reconstruction of context when necessary. More-
over, the method is also applied to certain sources, such as subtitles, which are inherently
composed of short sentences.
Code-Switching
Code-switching refers to the phenomenon where different languages
are used within the same context. We categorize code-switching into two types: document-
level and word-level. For document-level code-switching, when preparing the dataset for
pre-training sequences, we pack documents from various languages instead of separately
packing them within each language. Regarding word-level code-switching, we randomly
select some words in each documents written in SEA languages (e.g., Indonesian) and
replace 10% of them with their corresponding English phrases, if available.
Our pre-
liminary experiments on TinyLlama show that the document-level code-switching alone
performs better than the word-level code-switching alone or a combination of both ap-
proaches. Therefore, we only apply the document-level code-switching method during
continual pre-training. Interestingly, despite the intuitive expectation that incorporating
translation data, such as CCAligned (El-Kishky et al., 2020), would enhance model perfor-
mance on document-level code-switching, the experimental results did not demonstrate a
significant improvement. In contrast, using translation data alone (i.e., without document-
level code-switching) can lead to improved model performance over the baseline on gen-
eral tasks (e.g., question answering), suggesting that translation data plays a role similar
to document-level code-switching to a certain degree. Nonetheless, to facilitate translation
capabilities, our dataset incorporates translation datasets, which will be discussed later.
Aggressive Data Cleaning and Deduplication
The data quality is crucial during con-
tinual pre-training. We employ aggressive cleaning parameters, extended filtering list for
each language, and multi-round deduplication. Consequently, even though we started
with well-curated open datasets, e.g., MADLAD-400 clean set (Kudugunta et al., 2023), we
still further removed 31.11% in data cleaning and 11.16% in data deduplication. By ex-
tensively filtering out noisy, harmful, and duplicated content, we are able to significantly
improve the efficiency of the pre-training process and the stability of the optimization pro-
cedure. Furthermore, LLMs are less prone to memorization issues when training data has
undergone thorough deduplication (Lee et al., 2022).
Question: ␣Siapakah pastur/ketua Ibadah pertama GBI KA?
Answer: ␣Dr. Petrus Octavianus.
Question: ␣Apakah nama film yang masuk nominasi FFI 2005 , 
diproduksi oleh PT Sinemart Pictures karya Hanung Bramantyo?
10000000
␣Tentang Dia
LLM
with 
trailing 
space (␣)
no 
trailing 
space
Answer: ␣
Answer:
(a) Minor variations in prompts such as a
trailing space visualized by
can drastically
change the prediction of LLMs.
Ablation
Prompt
Exact Match
Sailor-1.8B
no space
40.88
with space
38.41
w.o. BPE dropout
no space
38.94
with space
18.76
(b) Experimental results on the TydiQA dataset
indicate that applying BPE dropout significantly
enhances the robustness of the Sailor-1.8B model
when handling trailing spaces.
Figure 2: Initially Sailor models were trained on 200B tokens using a greedy tokenization
strategy. Subsequently, they were fine-tuned using BPE dropout for an additional 2B to-
kens, with the dropout rate as 0.1. As observed, BPE dropout improves the robustness.
3

--- Page 4 ---

Technical Report
2.6
2.8
3.0
3.2
3.4
3.6
3.8
Average Validation Loss on SEA Langauges
3.2
3.3
3.4
3.5
Validation Loss on English
0.25B
0.25B Trend
0.75B
0.75B Trend
2.25B
2.25B Trend
Figure 3: We initially pre-train a 120M model using a corpus of 20B tokens focusing on En-
glish. Subsequently, we continually pre-train the model using a mixed corpus comprising
both English and SEA languages. Each data point here corresponds to a different configu-
ration of data mixture and learning rate. As indicated, under a fixed total tokens, there is a
trade-off between the model’s performance on English and SEA languages.
2.2
Tokenization
BPE Dropout
We have observed that the model is unreasonably sensitive to small vari-
ations of the prompt, especially on spaces. As illustrated in Figure 2a, when prompting
the model with the string “Answer:” without any trailing space yields a substantially im-
proved performance compared to “Answer:
” 1. The same phenomenon are observed
in Qwen1.5, Mistral and Llama 2, and a similar issue has been discussed at lm-evaluation-
harness library2 (Gao et al., 2023). We attribute this kind of vulnerability to the tokenization
strategy used in data processing. Modern tokenization methods usually employ the Byte
Pair Encoding (BPE) (Sennrich et al., 2016) under the greedy segmentation setting 3, which
means that sentences are segmented into subwords using the optimal tokenization strat-
egy. However, the always-optimal strategy can lead to vulnerability in the model when
it encounters noisy subwords, such as an unexpected space in “Answer:
”. Typically, a
space is segmented into subwords alongside the subsequent chars (e.g., “ 1” constitutes
a single subword). Yet, if a space is left at the end of the prompt, it becomes an isolated
subword “ ”, deviating from the segmentation strategy in the demonstration examples. To
alleviate the problem, we employ the BPE-Dropout (Provilkov et al., 2020) during continual
pre-training, which stochastically corrupts the segmentation procedure of BPE to achieve
subword regularization. Experimental results indicate that although BPE Dropout slightly
increases the loss on greedy subword segmentation, it enhances both the performance and
the robustness of models, as shown in Figure 2b.
Vocabulary Expansion
We have tried our best to do vocabulary expansion on models
like Mistral (Jiang et al., 2023a) and Llama-2 (Touvron et al., 2023b). However, similar to
the observation in concurrent works (Zhao et al., 2024), it is challenging to expand the vo-
cabulary with maintaining the original performance. According to our investigation, with-
out sufficient continual pre-training, the performance of vocab expanded model could not
even recover to the baseline version. For example, after being trained on 20B tokens with
an expanded vocabulary of 15,000 subwords, Mistral’s question answering performance
over Thai remains 10% lower than that of the original model. We have also explored sev-
eral methods to eliminate the problem, including warmup the embedding layer first, or
modularized continual-training (Kim et al., 2024). Despite our efforts, the methods did
not perform as effectively as we expected. We acknowledge this interesting yet challeng-
ing problem as an opportunity for future research. Finally, we decided to develop Sailor
1We use “ ” to represent space.
2https://github.com/EleutherAI/lm-evaluation-harness/issues/614
3The default BPE class is initialized with no dropout in the HuggingFace tokenizers library.
4

--- Page 5 ---

Technical Report
2.75
3.00
3.25
3.50
3.75
4.00
4.25
4.50
log(English Proportion) −log(Learning Rate)
3.15
3.20
3.25
3.30
3.35
3.40
3.45
3.50
Validation Loss on English
y = 0.11x2 −1.04x + 5.54
R² = 0.9936
(a) The relationship between English loss and
log(English Proportion) −log(Learning Rate).
7.50
7.25
7.00
6.75
6.50
6.25
6.00
5.75
log(Malay Proportion) + log(Learning Rate)
3.2
3.3
3.4
3.5
3.6
3.7
3.8
3.9
4.0
Validation Loss on Malay
y = 0.13x2 + 1.24x + 6.28
R² = 0.9534
(b) The relationship between Malay loss and
log(Malay Proportion) + log(Learning Rate).
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
Learning Rate
×10
4
2.5
2.6
2.7
2.8
2.9
Avg. Validation Loss on SEA Langauges
(c) The average SEA loss with increasing the learning rate.
Figure 4: Under the same token budget, we observe that (a) the validation loss on English
can be modeled as a quadratic function of log(English Proportion) −log(Learning Rate);
(b) the validation loss on SEA languages, using Malay as an example, can be approximately
represented by a quadratic function with log(Malay Proportion) + log(Learning Rate); (c)
we can tune the learning rate by analyzing the learning curves on SEA languages.
models based on Qwen1.5 (Bai et al., 2023), which is inherently multilingual-friendly and
possesses a large vocabulary size, thereby guaranteeing a high compression rate for SEA
languages.
2.3
Training
When it comes to continual pre-training, two crucial hyper-parameters to consider are the
learning rate and the data mixture. In our practise, we begin by generating a number of
training configurations with varying learning rates 4 and language proportions to train
several proxy models 5. By analyzing the trade-off between English and SEA languages on
these proxy models, we can select a suitable learning rate. Once the learning rate is deter-
mined, we then conduct fine-grained data mixture simulation experiments to optimize the
joint loss across all languages, which is finally used in large-scale training.
The Curse of Multilinguality
Figure 3 provides a visual representation of the relation-
ship between the model’s performance on English and SEA languages when subjected
to the same token budget (e.g., 0.25B). It clearly illustrates that the trade-off that exists
among different languages. In other words, when performing continual pre-training on an
English-centric language model, increasing the proportion of SEA language corpus always
4We first divide the logarithmic range between 1e-5 and 4e-4 into 20 equal intervals. For each
configuration, we randomly select one interval and use the corresponding value as the learning rate.
5The proxy models are typically small, allowing for cheap experiments, yet they retain key char-
acteristics akin to those of the target base LLM.
5

--- Page 6 ---

Technical Report
Id
English
Chinese
Lao
Malay
Indonesian
Thai
Vietnamese
Joint Loss
1
0.2356
0.09388
0.0172
0.1487
0.2131
0.1603
0.1312
2.516
2
0.1076
0.1656
0.0722
0.1838
0.0892
0.1434
0.2372 
2.421
…
64
0.2004
0.1258
0.1236
0.1937
0.0714
0.1431
0.1419 
2.342
Linear Regression Model
A New Data Mixture:
English
…
Vietnamese
0.1359
…
0.0987
Joint Loss
2.115
Figure 5: We employ the experimental results from proxy models across a variety of data
mixtures (e.g., 64 distinct data mixture here) to fit a linear regression model. The model
is then utilized to predict the validation loss of simulate numerous random data mixtures,
enabling us to identify the most effective data mixture for optimizing joint loss. Subse-
quently, the best data mixture is applied to large-scale training.
results in a degradation of the model’s performance on English, even when a high-quality
English corpus is included for replay. These findings align with previous studies on the
curse of multilinguality (Conneau et al., 2020; Chang et al., 2023), which posit that mod-
eling multiple languages within a single model leads to competition among languages for
the fixed model capacity.
Learning Rate Tuning
Figure 3 also demonstrates an inverse relationship between the
number of tokens and the loss on English. As more tokens are consumed (e.g., 0.25B →
2.25B), the curve shifts towards the upper-left area, signifying an increase in the loss on
English. Interestingly, the loss trend on the source domain (i.e., English) is primarily in-
fluenced by two factors: the proportion of English data during continual pre-training and
the learning rate. Under the same token budget, the model’s loss on English can be accu-
rately modeled as a quadratic function of log(English Proportion) −log(Learning Rate), as
shown in Figure 4a. In other words, while keeping the proportion of English data constant,
increasing the learning rate may adversely affect the model’s performance on English.
Meanwhile, the loss trend on the target domain (i.e., SEA languages) is also mainly affected
by the proportion of the target domain and the learning rate. However, there is a different
modeling among the model loss on SEA languages, the proportion and the learning rate,
as demonstrated by Figure 4b. From the observation, it becomes evident that the learning
rate serves as a crucial hyper-parameter. A well-tuned learning rate plays a pivotal role in
striking a balance between the acquisition of SEA languages and the forgetting of English.
As shown in Figure 4c, considering that increasing the learning rate beyond 1e-4 does not
yield significant improvements in the loss on SEA languages, we set the peak learning rate
to 1e-4 in our experiments.
Data Mixture Simulation
We aim to develop an improved LLM tailored for the en-
tire SEA region, with a focus on ensuring balanced representation across all target lan-
guages. To achieve this, we have developed a new algorithm that determines the appro-
priate weights for various languages during continual pre-training. This method involves
conducting a series of randomized data mixture experiments, while adhering to a prede-
termined learning rate. Our goal is to determine the most effective data mixture. To this
end, we suggest employing simulations in conjunction with linear regression models. As
depicted in Figure 5, we begin by training a set of proxy models (e.g., 64 in total here)
on a variety of data mixtures for a limited number of training steps (e.g., 1000 steps). We
then fit a linear regression model, using the data mixture as the input feature and the joint
loss considering all languages 6 as the target. With this model, we can perform numerous
simulation experiments (e.g., 1,000,000) on randomly sampled data mixtures to explore the
vast array of possibilities within seconds. The linear model then guides us in selecting the
combination that yields the lowest predicted joint loss. Once this data mixture has been
optimized, it can be directly applied to large-scale training. More details and findings will
be discussed in our upcoming paper.
6We use the product of individual losses as the joint loss.
6

--- Page 7 ---

Technical Report
2.4
Best Practise for Continual Pre-training
Drawing from the above insights, we highlight the importance of selecting the learning rate
and the proportion of source domain data to mitigate issues such as catastrophic forgetting.
Therefore, we focus on the metric log(Source Domain Proportion) −log(Learning Rate),
which we refer to as the magic metric below. We suggest the following steps:
1. Fit a parametric quadratic function modeling the relationship between loss source
and the magic metric via experiments varying learning rates and proportions.
2. Estimate the boundary of the magic metric value beyond which the model’s
loss source starts to deviate significantly from the original one.
3. Balance the learning progress on the target domain with the retention rate on the
source domain by selecting a suitable magic metric larger than the boundary.
4. If the magic metric substantially exceeds the estimated boundary, it indicates that
the model retains more knowledge from the source domain; conversely, it facili-
tates a more rapid learning pace on the target domain.
The above guideline can potentially explain why Lemur (Xu et al., 2024) demonstrated
negligible performance deterioration on natural language benchmarks (e.g., MMLU) de-
spite undergoing continual pre-training from Llama-2 on an extremely imbalanced data
distribution (i.e., text:code as 1:10). The employment of a smaller learning rate (i.e., 4e-5)
during Lemur’s training likely preserved the magic metric within an good range, allowing
the model to maintain its proficiency in the source natural language domain.
3
Data Sources
Here we describe all the corpus used in our training. Note that we performed an additional
round of data deduplication and cleaning on these datasets before using them.
3.1
Dataset for Replay
To mitigate catastrophic forgetting of English and Chinese capabilities of our models, we
consider high-quality English and Chinese datasets as part of our data sources during con-
tinual pre-training.
SlimPajama
SlimPajama (Soboleva et al., 2023) is a high-quality dataset comprising 627B
tokens, curated by rigorously cleaning and deduplicating the RedPajama Corpus (Com-
puter, 2023). It primarily focuses on English, and removes 49.6% of low-quality and dupli-
cate data from RedPajama. We use the released version on HuggingFace 7.
SkyPile
SkyPile (Wei et al., 2023) is a massive, high-quality Chinese dataset for pre-
training. It comprises 233M web pages, totaling 150B tokens, carefully filtered and dedu-
plicated from public web sources. We download SkyPile by accessing its hosted dataset on
HuggingFace 8.
3.2
Dataset for SEA Languages
CC100
CC100 9 is a multilingual corpus comprising monolingual data from over 100 lan-
guages. The corpus was original constructed for training the XLM-R model (Conneau et al.,
2020), a powerful cross-lingual language model. The data was sourced from the Common
Crawl project (Rana, 2010). Specifically, the corpus was generated by processing Common
7https://huggingface.co/datasets/cerebras/SlimPajama-627B
8https://huggingface.co/datasets/Skywork/SkyPile-150B
9https://data.statmt.org/cc-100
7

--- Page 8 ---

Technical Report
Crawl snapshots from January to December 2018, using the open-source CC-Net reposi-
tory (Wenzek et al., 2020a). In our pre-training corpus, we take the Indonesian, Malay, Lao,
Thai and Vietnamese subsets.
MADLAD-400
The CC100 corpus is a great resource for multilingual languages due to
its high quality, but it has already split every document into separate paragraphs, making it
serve as a paragraph-level corpus. We believe using paragraphs as examples would greatly
hurt the document-level performance of the model, as evidenced by our preliminary study.
Therefore, we also consider MADLAD-400 (Kudugunta et al., 2023), a manually audited
and large-scale multilingual corpus spanning 419 languages. MADLAD-400 is also based
on CommonCrawl, which uses all available corpus till August 2022. In our pre-training
corpus, we take its clean version, downloaded from the dataset hosted by HuggingFace 10.
Wikipedia
We utilize the Wikipedia dump (encompassing Malay, Indonesian, Thai, and
Vietnamese) up to November 2023 from the Wikipedia dataset hosted on HuggingFace 11.
It should be noted that some of the Wikipedia corpus may be duplicated, as the SlimPajama
dataset has already included the multilingual Wikipedia corpora.
OpenSubtitles
We collect the Malay, Indonesian, Thai and Vietnamese subtitles from the
OPUS OpenSubtitles category 12. For all subtitles, we use a sliding window of 100 to con-
catenate adjacent subtitles to compose longer documents. An example of Indonesian sub-
title can be found below:
Duduk Manis dan Selamat Menikmati
Su-ho!
Asapnya terus mendekatiku.
Kembali ke kampung halaman, Kukira aku akan dapat Sashimi...
· · ·
Translation
While our preliminary studies indicate that translation data may have sim-
ilar effects to document-level code-switching, we still incorporated translation data since
translation is an important task. We curate a selection of English-SEA language translation
pairs available in the OPUS project 13 (e.g., TED2020 talks). Notably, we observe substan-
tial duplication within the translation data, thus necessitating a further deduplication step.
Concurrently, to account for both directions, we processed data for both English-to-SEA
and SEA-to-English translation directions for each example. An illustrative example is
provided below:
Indonesian to English: Pak Tanaka bukan murid. Mr. Tanaka is not a student.
English to Indonesian: Did the Israelites execute criminals by hanging them on
stakes? Apakah mereka menghukum mati penjahat dengan memakukannya pada
tiang?
4
Preprocessing Pipeline
The data quality is crucial during continual pre-training. We found that several publicly
available multilingual datasets could be further cleaned and deduplicated. To improve
the data cleaning process for SEA languages specifically, we expanded our list of filtering
words, trained new filtering models, and implemented a more aggressive deduplication
strategy. As a result of these optimizations, we extracted 61.19% of data for SEA languages
10https://huggingface.co/datasets/allenai/MADLAD-400
11https://huggingface.co/datasets/wikimedia/wikipedia
12https://opus.nlpl.eu/OpenSubtitles-v2018.php
13https://opus.nlpl.eu/
8

--- Page 9 ---

Technical Report
Extract
SEA Subsets
Data
Cleaning
Data
Deduplication
Figure 6: With aggressive data cleaning and deduplication, we obtain 61.19% high-quality
data from two well-curated open datasets, including CC100 (Wenzek et al., 2020a) and
MADLAD-400 (Kudugunta et al., 2023). This forms the SailCraft dataset, used to train the
Sailor models. The reported removal rate (grey) is with respect to each previous stage, and
the kept rate (colored) demonstrates the overall rate.
from public datasets, and constructed the final SailCraft dataset. The specific removal rates
are shown in Figure 6.
4.1
Data Normalization
We apply the following data normalization procedures before data cleaning:
1. Uniform whitespace. We first unify the whitespace within the sentence, trans-
forming all forms of whitespace to the classic space character. This approach guar-
antees consistency across various whitespace characters and facilitates the segmen-
tation, i.e., converting the documents into words.
2. Replace Unicode punctuation.
We replace Unicode punctuation in text with
ASCII equivalents. It ensures the compatibility by simplifying text processing, as
ASCII punctuation is more universally recognized and easier to work with.
3. Remove incorrect words. We exclude emojis using the EMOJI package 14, remove
HTML-related tags to eliminate links associated with source page code, and filter
out certain terms based on a pre-defined word list.
4. Remove lengthy words. We remove words exceeding a pre-defined length cutoff,
especially in web-scraped datasets where lengthy words often signify formatting
errors or URLs. This process helps to clean and standardize the data.
Note that for MADLAD-400, we have fixed the Unicode escaping issue (i.e., lots of “\\n”)
as introduced in HuggingFace forum 15, which would cause the trouble in few-shot in-
context learning and chatbot application where “\n” acts as an important delimiter be-
tween demonstrations and task input. Concretely, we replace all “\\n” with “\n\n” or
“\n” with some heuristic rules. Please refer to Appendix A for implementation details and
concrete cases.
9

--- Page 10 ---

Technical Report
4.2
Data Cleaning
The data cleaning mainly follows the BigScience data cleaning recipe 16. Note that for most
languages, we can make use of the publicly available resource. However, for several low-
resource languages, we have to train model from scratch. The entire data cleaning process
is as follows:
1. Filtering on the number of words. We first tokenize the documents with senten-
cepiece model for each language. Then we count the number of words and remove
the document that is less than min length or is greater than the max length. The
purpose of filtering short document is to remove the incorrect sentences or the
sentences without enough context. The purpose of filtering long document is to
remove redundant information or exceed the maximum input length.
2. Filtering on the character repetition ratio. We first compile the list of character-
level n-grams for the given document. Then, we calculate the frequency for each
n-gram. We define the character repetition ratio as the sum of frequencies of the
top m most frequent n-grams. A document is dropped if its character repetition
ratio score is above the pre-defined threshold. Note that m is determined as a
trade-off choice so that it can balance the distribution of short and long documents.
Practically, we choose m as the square root of the amount of n-grams.
3. Filtering on the word repetition ratio. The word repetition ratio is defined as the
sum of frequencies of all n-grams whose frequency is greater than 2. A document
is dropped if its word repetition ratio score is above the pre-defined threshold.
4. Filtering on the special characters ratio. A list is maintained to track special char-
acters. If a document’s ratio of special characters exceeds a pre-defined threshold,
it will be dropped. The purpose of this filter is to eliminate documents that consist
primarily of special characters.
5. Filtering on the stop words ratio. A list of stop words for each language is main-
tained, and a document will be removed if its stop words ratio is above the pre-
defined threshold. It is to remove machine-generated text that do not have much
semantically meaningful information. However, one significant challenge arises
with languages such as Chinese and Vietnamese that do not use spaces, as it be-
comes difficult to recognize stop words after tokenization. Following BigScience
practise, we address the issue by expanding the stop list to include both word-level
and byte-piece-level stop words, thereby enhancing the coverage and effectiveness
of the filtering. For stop words list, we collected those for Thai 17 and Malay 18 from
available resources. However, we did not find relevant resources for Lao, and thus
we translated the Thai stop words list into Lao.
6. Filtering on the flagged words ratio. We maintain a list of flagged words for each
language. A document is removed if its flagged words ratio is above the pre-
defined threshold. It will remove buzzwords about the porn, which is harmful
for model training. We create or expand the flagged word list for Thai, Malay, and
Lao by translating from English ones developed by BigScience.
7. Filtering on the language identification prediction score.
We adopt the fast-
Text (Joulin et al., 2016) model 19 to get the language identification result for each
document and the corresponding confidence score. A document will be dropped
if its confidence score is below the pre-defined threshold. The filter is to remove
unnatural content such as machine-generated text, advertisements, or frequently
changing spoken language. However, it also bring the drawback that it would
14https://github.com/carpedm20/emoji
15https://huggingface.co/datasets/allenai/MADLAD-400/discussions/2
16https://drive.google.com/file/d/1cCJ8sWE88TRLDAa3eHLmXO4JlkR2QzLY/view
17https://github.com/stopwords-iso/stopwords-th/blob/master/stopwords-th.txt
18https://github.com/stopwords-iso/stopwords-ms/blob/master/stopwords-ms.txt
19https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin
10

--- Page 11 ---

Technical Report
Language
Source
Raw
After Clean
After Dedup
Indonesian
CC100
149G
105G
88G
MADLAD-400
140G
130G
126G
Thai
CC100
72G
33G
11G
MADLAD-400
283G
103G
94G
Vietnamese
CC100
138G
95G
77G
MADLAD-400
281G
262G
251G
Malay
CC100
8.5G
7.2G
4.8G
MADLAD-400
12.0G
12.0G
12.0G
Lao
CC100
0.62G
0.15G
0.06G
MADLAD-400
1.80G
0.74G
0.69G
Table 2: The storage statistics on each subset, including raw data, after data cleaning and
after data deduplication. Even though we started with high-quality open datasets (i.e.,
the MADLAD-400 clean set and the CC100), we still removed 31.11% data during data
cleaning, and further removed 11.16% during data deduplication.
remove code-switching text that exists in SEA regions like Singlish (Singapore En-
glish) and Manglish (Malaysian English).
8. Filtering on the perplexity score. We adopt the KenLM (Heafield, 2011) model
to calculate the perplexity score of documents for each language. KenLM model
are trained from the high-quality corpus like Wikipedia. A document will be re-
moved if its perplexity score is above the pre-defined threshold. The filter will
remove the documents with unrelated words like tags, time, date and lots of rep-
etitions. One main drawback of the filter is that it would inevitably remove nec-
essary documents that have a different distribution from Wikipedia. For KenLM
model, we download most language models from BigScience repo 20. However,
there is no KenLM model available for Thai, Malay and Lao. Thus, we sample
a high-quality subset from the Wikipedia corpus and train KenLM models with
vocab size 65536 21.
4.3
Data Deduplication
The data deduplication procedure is the most important and challenging part in our data
preprocessing. Firstly, it distills the corpus for efficient pre-training. Moreover, it further
filters the noise information for effective training, like machine-generated advertisements
that could not be easily recognized by rule-based cleaning methods. Most importantly,
LLMs are less prone to exhibit memorization issues when training data has undergone
thorough deduplication (Lee et al., 2022).
Implementation Details
For implementation, we employ the Text-Dedup tool (Mou
et al., 2023) for data deduplication 22. It is well-packaged and offers easy command-line in-
teraction. The tool also demonstrates excellent performance in deduplication benchmark-
ing 23. It utilizes 5-gram MinHashLSH deduplication (Broder, 1997) with a threshold of 0.7.
The number of permutations (hashes) is set to 256 to conserve memory usage. The Jaccard
similarity threshold is set to 0.7. The TextDedup tool further computes the optimal Min-
HashLSH parameter that minimizes the weighted sum of probabilities of false positives
20https://github.com/bigscience-workshop/data-preparation/tree/main/preprocessing/
training/01b_oscar_cleaning_and_filtering#2-download-everything-you-need
21https://github.com/bigscience-workshop/data_tooling/tree/master/kenlm_training
22https://github.com/ChenghaoMou/text-dedup
23https://tinyurl.com/bdf6zerm
11

--- Page 12 ---

Technical Report
Language
Property
Most Frequent Deduplicate
CC100
Indonesian
Text
tekanan intra-abdomen (kembung berkepanjangan, ascitis,
adanya massa intra-abdomen, atau kehamilan
Translation
intra-abdominal pressure (prolonged bloating, ascitis,
presence of an intra-abdominal mass, or pregnancy
Count
40,371
CC100
Thai
Text
Translation
More information on details
Count
41,901
Text
Chơi Vui. Ngoài ra, bạn có thể lựa chọn thêm nhiều
chủ đề game hấp dẫn khác
CC100
Vietnamese
Translation
Fun. In addition, you can choose from many other
attractive game themes.
Count
9,219
MADLAD-400
Indonesian
Text
Segera obati dengan obat herbal kami yang sudah terbukti
ampuh dan aman dalam mengobati penya
Translation
Treat immediately with our herbal medicine which has been
proven to be effective and safe in treating the disease.
Count
37,009
MADLAD-400
Thai
Text
[Sensitive Data] เขตђฒนา กҚงเทพมหานคร'
Translation
[Sensitive Data], Watthana District, Bangkok
Count
121,364
MADLAD-400
Vietnamese
Text
bạn hãy chia sẻ với bạn bè của mình và luôn theo dõi,
ủng hộ chúng tôi để
Translation
Please share with your friends and always follow and
support us to
Count
13,813
้อҊลเٲมเѠมเ٨ยวѕบรายละเ҇ยด'
Figure 7: The most frequent textual duplicates identified across two datasets for three SEA
languages, along with their respective frequencies. Inappropriate content and personally
identifiable information are replaced with [Sensitive Data]. For brevity, we highlight only
the duplicate content. The lengthy content is truncated for better visualization.
and false negatives 24. Ultimately, the number of bands and the number of rows per band
(i.e., two crucial hyper-parameters) are optimized to 25 and 10, respectively.
For resource requirements, the data deduplication mainly consumes memory, CPU cores
and disk spaces. The memory requirement is primarily determined by the number of doc-
uments, rather than the disk size of the documents 25. To facilitate dealing with large files
within limited memory resource, we first split them into chunks (30GB) to make it tractable
on our CPU server. It takes about 200GB of memory to process a 30GB corpus with 256 per-
mutations. It takes approximately 30 minutes in total to deduplicate the 30GB corpus under
64 CPU cores. To improve the deduplication performance, we iteratively cycled through
the process of splitting into chunks, data deduplication, and recombining the chunks for 3 rounds
until the chunk size converged.
24Refer to the OPTIMAL PARAM function at https://github.com/ChenghaoMou/text-dedup/
blob/main/text_dedup/utils/analysis.py
25https://huggingface.co/blog/dedup
12

--- Page 13 ---

Technical Report
“Pendarahan” terbanyak terjadi ketika putra kami belajar mengemudi 
(pada sembilan bulan!). Jatuh dan banyak pendarahan internal. Begitu dia 
stabil, hal-hal menjadi lebih bermanfaat. Kami menanamkan anak kami 
dua kali seminggu penuh untuk mencegah “pendarahan”. Sekitar waktu 3, 
tak lama ia mulai mengendarai sepeda motor. Pada usia empat tahun, dia 
adalah sepatu roda. Pada usia enam tahun, dia bermain ski di Pegunungan 
Rocky (dengan infus setiap hari sebelumnya di luar sana di gunung). Dia 
bermain sepak bola dari usia lima hingga 10 tahun dan di kelas lima, dia 
berada di tim bola voli perguruan tinggi dan tim bola basket. Voli telah 
menjadi hasratnya dan ia berpartisipasi dalam kamp pelatihan bola voli 
setiap musim panas hanya selama dua minggu.
“Pendarahan” terbanyak terjadi ketika putra kami belajar berjalan-jalan 
(sembilan bulan!). Uang jatuh dan banyak brusing internal. Begitu dia stabil 
di kakinya, hal-hal menjadi lebih menguntungkan. Kami menanamkan 
anak kami dua kali seminggu untuk mencegah “pendarahan”. Tentang era 
3, tak lama ia mulai mengendarai sepeda. Pada usia empat tahun, dia adalah 
sepatu roda. Pada usia enam tahun, dia bermain ski di Pegunungan Rocky 
(dengan infus setiap pagi sebelum di luar sana di gunung). Dia bermain 
sepak bola dari usia lima hingga sepuluh tahun dan di kelas lima, dia berada 
di tim bola voli perguruan tinggi dan tim bola basket. Voli telah menjadi 
gairahnya dan dia berpartisipasi dalam kamp pelatihan bola voli setiap 
musim panas selama 2 minggu."
angka adalah salah satu yang pertama di Indonesia, banyak agen yang
digu-nakan di Indonesia yang menjual togel hongkong pool, data togel, 
live togel hongkong, togel sg karena kami adalah agen bola bonus deposit 
terbesar yang sudah sejak tahun 2004. Pemainnya juga sangat banyak 
karena kami menye-diakan informasi daftar situs judi qq online yang 
menyediakan nomor kegel dan sbobet Eropa dengan permainan menarik 
seperti baccarat online apk
togel sgp com adalah game yang sudah ada sejak dulu kala di Indonesia, 
banyak situs yang menjual di Indonesia yang menjual togel hongkong 30 
september, dunia togel, live draw hongkongpools, dan sgp com karena 
kami adalah agen kartu yang telah berdiri sejak tahun 2004. Pemainnya 
juga sangat banyak karena kami menyediakan informasi daftar situs judi 
qq online yang menyediakan prediksi togel sgp singapura dan potato777 
sbobet dengan permainan menarik seperti baccarat online asia
a. Segeralah bertaubat kpd Tuhan YME. Karena Tuhan sudah memberikan 
Anugerah dan Amanah, mahakarya ciptaan-NYA. yaitu seorg anak yg 
lahir dalam keadaan fitrah. Semua anak lahir ke dunia ini tanpa masalah, 
orang tualah yang membuat masalah kepada anak-anaknya
a. Segeralah bertaubat kpd Tuhan YME. karena Tuhan sudah memberikan 
Anugerah dan Amanah, mahakarya ciptaan-NYA. yaitu seorg anak yang 
lahir dalam keadaan fitrah. Semua anak lahir ke dunia ini tanpa masalah, 
orang tualah yang membuat masalah kepada anak-anaknya.
Figure 8: The above pairs of documents from the CC100-Indonesian dataset are identified
as duplicates by our deduplication algorithm. To enhance readability, the matching sub-
sequences within these document pairs are highlighted.
Definitely, more aggressive deduplication hyper-parameters (i.e., more permutations and
larger chunk sizes) would further improve the accuracy of data deduplication. We aim to
improve it from both algorithmic and engineering perspectives in the next version. For
more discussion, please refer to the future work section.
Case Study
Figure 7 showcases the most prevalent duplicate sentences across various
language subsets identified by our deduplication algorithm. These duplicates span a wide
range of domains, including medicine, customer service, and address information. The
presence of such noisy and redundant data can impede the pre-training process, as indi-
cated by Penedo et al. (2023). Additionally, sensitive information like emails and phone
numbers poses privacy risks.
Our deduplication approach effectively addresses the prevalent scenario where documents
are nearly identical, differing only in the interspersed template fields, as exemplified
in Figure 8. Despite cleaning efforts by CCNet (Wenzek et al., 2020b) and MADLAD-
400 (Kudugunta et al., 2023), the quality of open datasets remains sub-optimal, under-
scoring the challenges in multilingual data cleaning. For more deduplication cases, please
refer to Appendix B.
4.4
Data Composition
As detailed in Section 2.3, our algorithm involves utilizing proxy models to fit a linear re-
gression model, which then aids in determining the optimal data mixture for large-scale
training.
To elaborate, we extend the data mixture by extending it beyond language-
level considerations to also include the source of the data. This means we treat each lan-
guage from every source as a distinct dataset and try to optimize the data mixture of these
datasets. The Qwen1.5-0.5B model serves as our proxy model, and we apply the optimized
data mixture to the continual pre-training process across all model sizes. The effective to-
kens and equivalent epochs in SailCraft are documented in Table 3. From the table, we
observe that, in terms of quality or diversity, the CC100 dataset exhibits a relative advan-
tage over the MADLAD-400 dataset, particularly for Indonesian and Vietnamese.
13

--- Page 14 ---

Technical Report
Language
Source
Effective Tokens (B)
Epoch
English
SlimPajama
37.20
0.06
Chinese
SkyPile
22.64
0.15
Lao
CC100
0.03
0.97
MADLAD-400
0.31
0.97
Malay
CC100
2.02
1.34
MADLAD-400
5.54
1.54
OpenSubtitles
0.04
1.07
Wikipedia
0.17
1.32
Indonesian
CC100
23.72
0.90
MADLAD-400
25.62
0.66
OpenSubtitles
0.24
1.07
Wikipedia
0.45
1.32
Translation
0.50
1.16
Thai
CC100
3.00
1.28
MADLAD-400
32.07
1.35
OpenSubtitles
0.13
1.01
Wikipedia
0.28
1.32
Translation
0.34
1.14
Vietnamese
CC100
14.25
0.82
MADLAD-400
26.16
0.44
OpenSubtitles
0.05
1.08
Wikipedia
0.50
1.32
Translation
0.43
1.20
Table 3: The data composition of the final corpus SailCraft.
5
Model Training
We obtain the Sailor models through continual pre-training of Qwen1.5 (Bai et al., 2023) on
140B high-quality SEA tokens and 60B tokens for replay (see Section 4.4).
5.1
Training Infra
Codebase
To balance the training efficiency and debugging convenience, we leverage
two codebases for different size model. For relatively large models (i.e., 4B and 7B), we
utilize Megatron-LM (Shoeybi et al., 2019), which supports tensor parallel and pipeline
parallel to maximize the model flops utilization (MFU) of NVIDIA GPUs. But the origi-
nal Megatron codebase is a bit tricky to hands on due the absence of documents. Thus,
in practice, we employ the Megatron-LLM codebase 26. It is an optimized Megatron code-
base, paired with detailed documentation 27 and one-stop scripts (e.g., model sharding,
data preprocessing). For relatively small models (i.e., 0.5B and 1.8B), we employ TinyL-
lama (Zhang et al., 2024) codebase 28. The codebase follows a compact and well-organised
structure, which allows easy modifications for diverse purposes. Moreover, its optimisa-
tion enhancements significantly boost GPU utilisation. The combination of swift prototyp-
ing and efficient training make TinyLlama as a valuable tool in both early develop stage
and final continual training stage.
Hardware
For training devices, we use NVIDIA A100 SXM4 40GB GPUs. To acceler-
ate multi-node training, we further employ the InfiniBand for low latency and extreme
throughput. During the training, we employ 64 GPU cards for 7B / 4B models, and 32
GPU cards for 1.8B / 0.5B model.
26https://github.com/epfLLM/Megatron-LLM
27https://epfllm.github.io/Megatron-LLM/
28https://github.com/jzhang38/TinyLlama
14

--- Page 15 ---

Technical Report
5.2
Training Details
We adopt most of the pre-training settings and model architectures from Qwen1.5 (Bai
et al., 2023). It follows the standard transformer architecture (Vaswani et al., 2017), adopts
the pre-normalization with RMSNorm (Jiang et al., 2023b), SwiGLU activation (Shazeer,
2020) and rotary positional embeddings (Su et al., 2022). Notably, Qwen1.5 adds a bias
item in attention of the QKV layer to improve the extrapolation ability. Meanwhile, for
the 0.5B model, we set TIE WORD EMBEDDINGS to False, i.e., not tying the learning of the
input embedding (EMBEDDING module) and output projection (LM HEAD module). Thus,
the parameter of Sailor 0.5B is approximately 0.6B. However, we still name it 0.5B to be
consistent with Qwen1.5.
During training, we utilize a context window length of 4,096, and integrate Flash Attention
2 (Dao, 2023) to improve the training efficiency and reduce the memory usage 29. We utilize
AdamW (Kingma & Ba, 2014) for optimization, with the hyper-parameters β1 = 0.9, β2 =
0.95, eps = 1e−5. We use the weight decay of 0.1 and the gradient clipping of 1.0. We
train models with BFloat16 mixed precision to balance the training efficiency and stability.
Notably, we set ATTENTION SOFTMAX IN FP32 to True to execute attention masking and
Softmax operations in fp32, thereby preventing precision underflow 30.
The final pre-training corpus, SailCraft, is composed of approximately 200B tokens, inte-
grating both SEA tokens and replay tokens, as elaborated in Section 4.4. We use the batch
size of 4M tokens and the learning rate of 1e-4. Following a warmup period of 500 steps,
the learning rate remains constant. This scheduling strategy encourages more transfer-
able conclusions from simulations and allows for easier recovery from interrupted training
sessions. Generally Sailor models consume around 200B tokens, completing a full pass
through the SailCraft corpus once. However, the Sailor-0.5B model undergoes training
with 400B tokens, equivalent to 2 epochs.
6
Experiments
Sailor models are evaluated on several high-quality benchmarks, including question an-
swering, commonsense reasoning, reading comprehension and examination.
6.1
Benchmark
Question Answering
The XQuAD dataset (Artetxe et al., 2020) (Thai, Vietnamese) and
the TydiQA dataset (Clark et al., 2020) (Indonesian) were selected as the representative
benchmarks for question answering. The XQuAD dataset comprises 1,190 question-answer
pairs from professional translations of the development set of SQuAD v1.1 (Rajpurkar
et al., 2016). The TydiQA dataset covers 204,000 question-answer pairs directly sourced
from data in their original languages, with human-written questions.
An example from the TydiQA dataset (Indonesian).
[Context] Mencakupi sekitar 20% permukaan Bumi, Samudra Atlantik berada di
urutan kedua terbesar dalam segi ukurannya setelah Samudra Pasifik. Bersama
dengan lautan di sekitarnya ia mempunyai luas sebesar 106.450.000km²; jika lautan
di sekitarnya tidak dihitung, luasnya 82.362.000km². Jumlah wilayah yang mengalir
ke Samudra Atlantik lebih ...
[Qustion] seberapa luaskah samudera atlantik?
[Answer] 82.362.000km²
29In contrary to Flash Attention 1 (Dao et al., 2022), Flash Attention 2 makes it possible to train
model on an arbitrary dataset that also includes padding tokens.
30https://github.com/huggingface/transformers/pull/17437
15

--- Page 16 ---

Technical Report
Commonsense Reasoning
The XCOPA dataset (Ponti et al., 2020) (Indonesian, Thai, Viet-
namese) provides two choices for each premise, requiring the model to select one that bet-
ter addresses either the cause or effect of the event mentioned in the premise.
An example from the XCOPA dataset (Indonesian).
[Premise] Kunci tersebut hilang dari saku celana saya.
[Qustion] Penyebab
[Option 1] Saku celana saya sobek.
[Option 2] Celana saya baru.
[Answer] Saku celana saya sobek.
Reading Comprehension
The BELEBELE dataset (Bandarkar et al., 2023) is a large-scale
multiple-choice machine reading comprehension benchmark spanning 122 languages. The
Indonesian, Thai, and Vietnamese subsets were selected to evaluate model performance.
Each question is provided with a short paragraph of context and four possible options.
An example from the BELEBELE dataset (Indonesian).
[Context] Tumbuhan menghasilkan oksigen yang dihirup manusia, dan mereka
menghirup karbondioksida yang dikeluarkan manusia (yang artinya, bernapas).
Tumbuhan membuat makanan mereka dari matahari melalui fotosintesis. Mereka
juga memberikan tempat berteduh. Kita membuat rumah dari tanaman dan mem-
buat pakaian dari tanaman. Kebanyakan makanan yang kita makan ialah tum-
buhan. Tanpa tumbuhan, hewan tidak bisa bertahan hidup.
[Qustion] Apa yang membantu tanaman dalam proses fotosintesis?
[Option 1] Tempat berteduh
[Option 2] Hewan
[Option 3] Makanan
[Option 4] Matahari
[Answer] Matahari
Examination
The M3Exam dataset (Zhang et al., 2023) (Javanese, Thai, Vietnamese) is a
multilingual exam benchmark collected from official school tests used in nine countries.
Note that we chose its Javanese subset since the Indonesian version has yet to be released.
An example from the M3Exam dataset (Javanese).
[Qustion] Pak Untung iku sabendinane lunga menyang sanggar saperlu mimpin
lan ngatur lumakune crita drama
Miturut wacan ing inggil, pendamelan (penggawean) pak Untung dados
[Option 1] Aktor
[Option 2] Penulis
[Option 3] Pelawak
[Option 4] Sutradara
[Answer] Sutradara
6.2
Evaluation Protocol
As for evaluation, following established evaluation protocols, we employed the awesome
evaluation platform OpenCompass (Contributors, 2023) to build up our evaluation code 31.
The performance of all models is assessed based on the 3-shot Exact Match (EM) and F1
performance, with prompts provided in native languages (e.g., Indonesian task description
31The code can be found at https://github.com/sail-sg/sailor-llm.
16

--- Page 17 ---

Technical Report
3-shot (EM / F1)
XQuAD (th)
TydiQA (id)
XQuAD (vi)
Qwen1.5-0.5B
14.19 / 23.35
20.71 / 32.64
19.85 / 35.38
Sailor-0.5B
15.84 / 27.58
30.44 / 54.74
21.13 / 40.57
Qwen1.5-1.8B
27.24 / 43.56
29.73 / 53.76
29.17 / 48.15
Sailor-1.8B
32.72 / 48.66
40.88 / 65.37
34.22 / 53.35
Qwen1.5-4B
34.03 / 53.40
48.32 / 72.68
43.71 / 63.86
Sailor-4B
46.82 / 63.34
53.98 / 73.48
47.65 / 67.09
Llama-2-7B
30.64 / 43.80
56.64 / 72.14
46.96 / 66.16
Mistral-7B-v0.1
48.48 / 63.27
63.54 / 78.73
53.72 / 72.75
Typhoon-7B
51.70 / 68.92
–
–
VinaLLaMA-7B
–
–
44.82 / 64.81
Sea-Lion-7B
43.52 / 59.75
50.09 / 67.72
42.43 / 61.17
SeaLLM-7B-Hybrid
49.70 / 67.62
50.62 / 75.21
49.62 / 70.74
SeaLLM-7B-v2
34.55 / 55.13
52.21 / 77.00
46.19 / 72.11
Qwen1.5-7B
53.79 / 69.30
57.17 / 77.28
56.63 / 76.99
Sailor-7B
57.88 / 71.06
60.53 / 75.42
53.81 / 74.62
Table 4: Experimental results of different models on the question answering task. Note that
SeaLLM-7b-Hybrid and SeaLLM-7B-v2 are both models trained with instruction tuning
datasets, and the same for other tables.
for Indonesian tasks). Note that we keep the tokenizer consistent when computing the F1
scores of different models.
Following the evaluation approaches adopted in OpenCompass (Contributors, 2023) and
the Eleuther AI evaluation framework (Gao et al., 2023) on the popular HellaSwag bench-
mark Zellers et al. (2019), we reformulated the tasks with limited output spaces (i.e.,
XCOPA, BELEBELE) as continuation writing tasks. It is to say, each possible answer is
appended to the given input or question, and the one that achieves the lowest perplexity
score is considered as the model prediction. As for the M3Exam dataset, we adopt the
official evaluation method used in Zhang et al. (2023) to evaluate all models. The evalu-
ation approach involves directly prompting LLMs to produce the correct option ID when
presented with a question and its corresponding options.
6.3
Baseline Setup
We compare Sailor models with SeaLLM (Nguyen et al., 2023b), Sea-Lion (AI Singapore,
2023), Typhoon (Pipatanakul et al., 2023), and VinaLLaMA (Nguyen et al., 2023a). Our
reporting strictly adheres to the same evaluation methodology to ensure a fair comparison,
and we make much effort to closely match the reported results of all baselines.
6.4
Experimental Results
Experimental results shown in Table 4, 5, 6 indicate that our Sailor models typically out-
perform the baseline model, Qwen1.5, in terms of performance on SEA languages. Addi-
tionally, the performance of Sailor models is either superior or comparable to major SEA
LLMs such as SeaLLM, Sea-Lion, Typhoon, and VinaLLaMA on these benchmarks.
However, it is not the case for M3Exam. As shown in Table 7, our Sailor models exhibit
no evident advantage over Qwen1.5 at the 4B parameter scale or lower, and in certain in-
stances, it displays noticeable weaknesses. We have observed that the discrepancy is due to
a significant option bias, which leads the Sailor models to favor certain option IDs (e.g., al-
ways C) when making predictions. Interestingly, a similar phenomenon was also observed
among other baseline LLMs focusing on SEA languages. While instruction tuning could
mitigate the option bias, we have chosen not to tune the Sailor models to maintain fairness
and consistency in the evaluation process. We also provide additional results evaluated us-
17

--- Page 18 ---

Technical Report
3-shot (EM)
XCOPA (th)
XCOPA (id)
XCOPA (vi)
Qwen1.5-0.5B
51.00
52.20
53.80
Sailor-0.5B
51.00
58.20
58.00
Qwen1.5-1.8B
52.60
51.60
53.40
Sailor-1.8B
53.80
64.20
63.20
Qwen1.5-4B
53.40
55.00
57.80
Sailor-4B
53.40
69.20
68.20
Llama-2-7B
52.80
64.00
62.00
Mistral-7B-v0.1
57.20
62.40
61.60
Typhoon-7B
55.40
–
–
VinaLLaMA-7B
–
–
68.20
Sea-Lion-7B
60.80
60.60
67.80
SeaLLM-7B-Hybrid
58.20
71.60
67.60
SeaLLM-7B-v2
56.80
64.00
64.60
Qwen1.5-7B
54.20
62.20
66.20
Sailor-7B
59.00
72.20
72.20
Table 5: Experimental results of different models on the XCOPA dataset.
3-shot (EM)
Belebele (th)
Belebele (id)
Belebele (vi)
Qwen1.5-0.5B
29.89
26.89
30.22
Sailor-0.5B
32.22
30.89
32.33
Qwen1.5-1.8B
30.11
32.00
31.33
Sailor-1.8B
34.22
34.89
35.33
Qwen1.5-4B
32.78
36.22
35.22
Sailor-4B
36.11
41.33
38.89
Llama-2-7B
31.78
39.78
38.00
Mistral-7B-v0.1
34.33
41.33
41.33
Typhoon-7B
36.56
–
–
VinaLLaMA-7B
–
–
39.56
Sea-Lion-7B
36.33
35.56
37.00
SeaLLM-7B-Hybrid
37.78
43.11
43.00
SeaLLM-7B-v2
36.33
43.11
47.00
Qwen1.5-7B
38.33
42.00
42.89
Sailor-7B
41.56
44.33
45.33
Table 6: Experimental results of different models on the BELEBELE dataset.
ing the HellaSwag protocol in Appendix C, which is better aligned with other benchmark
results.
7
Conclusion and Future Work
In this paper, we present the Sailor family of open language models, tailored for South-East
Asian languages, which exhibit strong performance across various multilingual tasks and
benchmarks, fostering advancements in multilingual language models for the SEA region.
Here are some of the most important future works:
Document-Friendly Deduplication
We could improve data deduplication through
document-preserving deduplication to ensure the completeness of documentation.
It
should adhere to the following principles: (1) If we perform deduplication at the para-
graph level, it’s crucial to recombine these paragraphs into a coherent document. (2) If a
18

--- Page 19 ---

Technical Report
3-shot (EM)
M3Exam (th)
M3Exam (jv)
M3Exam (vi)
Qwen1.5-0.5B
22.38
22.10
29.12
Sailor-0.5B
21.87
28.84
23.53
Qwen1.5-1.8B
23.81
26.15
36.39
Sailor-1.8B
23.90
29.65
27.67
Qwen1.5-4B
26.26
30.19
40.02
Sailor-4B
27.23
29.11
31.58
Llama-2-7B
21.13
23.99
34.15
Mistral-7B-v0.1
29.59
31.00
43.54
Typhoon-7B
36.71
–
–
VinaLLaMA-7B
–
–
36.95
Sea-Lion-7B
23.90
21.56
26.89
SeaLLM-7B-Hybrid
25.98
24.53
38.79
SeaLLM-7B-v2
35.60
29.92
50.36
Qwen1.5-7B
35.88
33.15
51.09
Sailor-7B
38.33
35.85
51.98
Table 7: Experimental results of different models on the M3Exam dataset.
duplicated paragraph is found across multiple documents, it is advisable to retain only one
instance of the paragraph in a single document while removing the duplicate occurrences
from the other documents. For example, assuming document A, B, and C each contains
paragraphs a1, a2, b1, b2, c1 and c2 respectively. The paragraph a1 is a duplicate of b1,
while c1 is a duplicate of b2. Then the algorithm should filter out the duplicated para-
graphs b1 and b2 from the document B, thereby preserving the integrity and completeness
of both document A and C.
Cross-Lingual Instruction
In the diverse and multilingual context of South-East Asia re-
ligion, it is quite common for users to communicate in various languages. This creates a
particularly challenging scenario for chat models, which must be adept at understanding
and responding to queries in multiple languages. For example, if the user asks the chat
model a question in Indonesian, such as “Draf undangan pernikahan dalam bahasa Vietnam”
(English: Wedding invitation draft in Vietnamese), the user would expect the model to reply in
Vietnamese. Currently, in our internal evaluations, the Sailor models does not address the
challenge well. We plan to build cross-lingual instruction datasets to address the problem.
Code-Switching Language Generation
Although we introduce careful code-switching
techniques to improve the model performance on language mixing, there are still some
natural code-switching scenarios which are challenging for our models. It usually involves
the alternation between two or more languages within a single utterance. The natural
code-switching behavior is deeply rooted in the multilingual and multicultural societies
of South-East Asia, where individuals frequently navigate between multiple linguistic and
cultural backgrounds. However, for multilingual LLMs, it is still challenging to generate
code-switching texts (Yong et al., 2023).
More South-East Asian Languages
To broaden the impact of open language models for
SEA languages, we are dedicated to expanding our coverage to include more languages
from the region. We plan to achieve the goal by gathering high-quality training corpora
from all CommonCrawl snapshots and other open resources. Moreover, we aim to explore
language generalization techniques to transfer knowledge from high-resource languages
to low-resource languages, thereby enhancing the capabilities of Sailor models for the un-
derserved languages in the SEA region.
19

--- Page 20 ---

Technical Report
Acknowledgement
We extend our sincere gratitude to Zhikai Huang, Joseph Wong, and Xinyi Wan for their
regular maintenance of the cluster of Sea AI Lab, ensuring its stable operation and enabling
our jobs to run smoothly. We are deeply thankful to Xiaosen Zheng, Fan Zhou, Zhoujun
Cheng, Binyuan Hui, Junyang Lin and Terry Yin for the fruitful discussions. We appreciate
HuggingFace for providing a platform for open-source models and datasets, which have
been invaluable resources in building our pre-training corpus and advancing our research.
References
01. AI, :, Alex Young, Bei Chen, Chao Li, Chengen Huang, Ge Zhang, Guanwei Zhang,
Heng Li, Jiangcheng Zhu, Jianqun Chen, Jing Chang, Kaidong Yu, Peng Liu, Qiang Liu,
Shawn Yue, Senbin Yang, Shiming Yang, Tao Yu, Wen Xie, Wenhao Huang, Xiaohui Hu,
Xiaoyi Ren, Xinyao Niu, Pengcheng Nie, Yuchi Xu, Yudong Liu, Yue Wang, Yuxuan Cai,
Zhenyu Gu, Zhiyuan Liu, and Zonghong Dai. Yi: Open foundation models by 01.ai,
2024.
AI Singapore. Sea-lion (southeast asian languages in one network): A family of large lan-
guage models for southeast asia. https://github.com/aisingapore/sealion, 2023.
Rohan Anil, Sebastian Borgeaud, Yonghui Wu, Jean-Baptiste Alayrac, Jiahui Yu, Radu Sori-
cut, Johan Schalkwyk, Andrew M. Dai, Anja Hauth, Katie Millican, David Silver, Slav
Petrov, Melvin Johnson, Ioannis Antonoglou, Julian Schrittwieser, Amelia Glaese, Jilin
Chen, Emily Pitler, Timothy P. Lillicrap, Angeliki Lazaridou, Orhan Firat, James Molloy,
Michael Isard, Paul Ronald Barham, Tom Hennigan, Benjamin Lee, Fabio Viola, Malcolm
Reynolds, Yuanzhong Xu, Ryan Doherty, Eli Collins, Clemens Meyer, Eliza Rutherford,
Erica Moreira, Kareem Ayoub, Megha Goel, George Tucker, Enrique Piqueras, Maxim
Krikun, Iain Barr, Nikolay Savinov, Ivo Danihelka, Becca Roelofs, Ana¨ıs White, Anders
Andreassen, Tamara von Glehn, Lakshman Yagati, Mehran Kazemi, Lucas Gonzalez,
Misha Khalman, Jakub Sygnowski, and et al. Gemini: A family of highly capable mul-
timodal models. CoRR, abs/2312.11805, 2023. doi: 10.48550/ARXIV.2312.11805. URL
https://doi.org/10.48550/arXiv.2312.11805.
Mikel Artetxe, Sebastian Ruder, and Dani Yogatama. On the cross-lingual transferability of
monolingual representations. In Proceedings of the 58th Annual Meeting of the Association
for Computational Linguistics, ACL 2020, Online, July 5-10, 2020, pp. 4623–4637. Associa-
tion for Computational Linguistics, 2020. URL https://doi.org/10.18653/v1/2020.
acl-main.421.
Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin
Ge, Yu Han, Fei Huang, Binyuan Hui, Luo Ji, Mei Li, Junyang Lin, Runji Lin, Dayi-
heng Liu, Gao Liu, Chengqiang Lu, Keming Lu, Jianxin Ma, Rui Men, Xingzhang Ren,
Xuancheng Ren, Chuanqi Tan, Sinan Tan, Jianhong Tu, Peng Wang, Shijie Wang, Wei
Wang, Shengguang Wu, Benfeng Xu, Jin Xu, An Yang, Hao Yang, Jian Yang, Shusheng
Yang, Yang Yao, Bowen Yu, Hongyi Yuan, Zheng Yuan, Jianwei Zhang, Xingxuan Zhang,
Yichang Zhang, Zhenru Zhang, Chang Zhou, Jingren Zhou, Xiaohuan Zhou, and Tian-
hang Zhu. Qwen technical report. arXiv preprint arXiv:2309.16609, 2023.
Lucas Bandarkar, Davis Liang, Benjamin Muller, Mikel Artetxe, Satya Narayan Shukla,
Donald Husa, Naman Goyal, Abhinandan Krishnan, Luke Zettlemoyer, and Madian
Khabsa. The belebele benchmark: a parallel reading comprehension dataset in 122 lan-
guage variants. CoRR, abs/2308.16884, 2023. URL https://doi.org/10.48550/arXiv.
2308.16884.
Andrei Z. Broder. On the resemblance and containment of documents. Proceedings. Com-
pression and Complexity of SEQUENCES 1997 (Cat. No.97TB100171), pp. 21–29, 1997. URL
https://api.semanticscholar.org/CorpusID:11748509.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla
Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini
20

--- Page 21 ---

Technical Report
Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya
Ramesh, Daniel Ziegler, Jeffrey Wu, Clemens Winter, Chris Hesse, Mark Chen, Eric
Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner,
Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. Language mod-
els are few-shot learners. In H. Larochelle, M. Ranzato, R. Hadsell, M.F. Balcan, and
H. Lin (eds.), Advances in Neural Information Processing Systems, volume 33, pp. 1877–
1901. Curran Associates, Inc., 2020.
URL https://proceedings.neurips.cc/paper_
files/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf.
Tyler A. Chang, Catherine Arnett, Zhuowen Tu, and Benjamin K. Bergen. When is multi-
linguality a curse? language modeling for 250 high- and low-resource languages. CoRR,
abs/2311.09205, 2023.
doi: 10.48550/ARXIV.2311.09205.
URL https://doi.org/10.
48550/arXiv.2311.09205.
Jonathan H. Clark, Jennimaria Palomaki, Vitaly Nikolaev, Eunsol Choi, Dan Garrette,
Michael Collins, and Tom Kwiatkowski. Tydi QA: A benchmark for information-seeking
question answering in typologically diverse languages. Trans. Assoc. Comput. Linguistics,
8:454–470, 2020. URL https://doi.org/10.1162/tacl_a_00317.
Together Computer.
Redpajama: An open source recipe to reproduce llama training
dataset, 2023. URL https://github.com/togethercomputer/RedPajama-Data.
Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume
Wenzek, Francisco Guzm´an, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin
Stoyanov. Unsupervised cross-lingual representation learning at scale. In Dan Juraf-
sky, Joyce Chai, Natalie Schluter, and Joel Tetreault (eds.), Proceedings of the 58th Annual
Meeting of the Association for Computational Linguistics, pp. 8440–8451, Online, July 2020.
Association for Computational Linguistics. doi: 10.18653/v1/2020.acl-main.747. URL
https://aclanthology.org/2020.acl-main.747.
OpenCompass Contributors. Opencompass: A universal evaluation platform for founda-
tion models. https://github.com/open-compass/opencompass, 2023.
Tri Dao.
Flashattention-2: Faster attention with better parallelism and work partition-
ing. ArXiv, abs/2307.08691, 2023. URL https://api.semanticscholar.org/CorpusID:
259936734.
Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, and Christopher R’e. Flashattention:
Fast and memory-efficient exact attention with io-awareness. ArXiv, abs/2205.14135,
2022. URL https://api.semanticscholar.org/CorpusID:249151871.
Ahmed
El-Kishky,
Vishrav
Chaudhary,
Francisco
Guzm´an,
and
Philipp
Koehn.
CCAligned: A massive collection of cross-lingual web-document pairs. In Proceedings
of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP 2020),
pp. 5960–5969, Online, November 2020. Association for Computational Linguistics. doi:
10.18653/v1/2020.emnlp-main.480. URL https://www.aclweb.org/anthology/2020.
emnlp-main.480.
Leo Gao, Jonathan Tow, Baber Abbasi, Stella Biderman, Sid Black, Anthony DiPofi, Charles
Foster, Laurence Golding, Jeffrey Hsu, Alain Le Noac’h, Haonan Li, Kyle McDonell,
Niklas Muennighoff, Chris Ociepa, Jason Phang, Laria Reynolds, Hailey Schoelkopf,
Aviya Skowron, Lintang Sutawika, Eric Tang, Anish Thite, Ben Wang, Kevin Wang,
and Andy Zou. A framework for few-shot language model evaluation, 12 2023. URL
https://zenodo.org/records/10256836.
Kenneth Heafield. KenLM: Faster and smaller language model queries. In Chris Callison-
Burch, Philipp Koehn, Christof Monz, and Omar F. Zaidan (eds.), Proceedings of the
Sixth Workshop on Statistical Machine Translation, pp. 187–197, Edinburgh, Scotland, July
2011. Association for Computational Linguistics.
URL https://aclanthology.org/
W11-2123.
21

--- Page 22 ---

Technical Report
Albert Qiaochu Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Deven-
dra Singh Chaplot, Diego de Las Casas, Florian Bressand, Gianna Lengyel, Guillaume
Lample, Lucile Saulnier, L’elio Renard Lavaud, Marie-Anne Lachaux, Pierre Stock,
Teven Le Scao, Thibaut Lavril, Thomas Wang, Timoth´ee Lacroix, and William El Sayed.
Mistral 7b. ArXiv, abs/2310.06825, 2023a. URL https://api.semanticscholar.org/
CorpusID:263830494.
Zixuan Jiang, Jiaqi Gu, Hanqing Zhu, and David Z. Pan. Pre-rmsnorm and pre-crmsnorm
transformers: Equivalent and efficient pre-ln transformers.
ArXiv, abs/2305.14858,
2023b. URL https://api.semanticscholar.org/CorpusID:258865592.
Armand Joulin, Edouard Grave, Piotr Bojanowski, Matthijs Douze, H´erve J´egou, and
Tomas Mikolov.
Fasttext.zip: Compressing text classification models.
arXiv preprint
arXiv:1612.03651, 2016.
Seungduk Kim, Seungtaek Choi, and Myeongho Jeong. Efficient and effective vocabulary
expansion towards multilingual large language models. ArXiv, abs/2402.14714, 2024.
URL https://api.semanticscholar.org/CorpusID:267782714.
Diederik P. Kingma and Jimmy Ba. Adam: A method for stochastic optimization. CoRR,
abs/1412.6980, 2014. URL https://api.semanticscholar.org/CorpusID:6628106.
Sneha Kudugunta, Isaac Caswell, Biao Zhang, Xavier Garcia, Derrick Xin, Aditya
Kusupati, Romi Stella, Ankur Bapna, and Orhan Firat.
MADLAD-400:
A mul-
tilingual and document-level large audited dataset.
In Alice Oh, Tristan Nau-
mann, Amir Globerson, Kate Saenko, Moritz Hardt, and Sergey Levine (eds.), Ad-
vances in Neural Information Processing Systems 36:
Annual Conference on Neural In-
formation Processing Systems 2023, NeurIPS 2023, New Orleans, LA, USA, December
10 - 16, 2023, 2023.
URL http://papers.nips.cc/paper_files/paper/2023/hash/
d49042a5d49818711c401d34172f9900-Abstract-Datasets_and_Benchmarks.html.
Katherine Lee, Daphne Ippolito, Andrew Nystrom, Chiyuan Zhang, Douglas Eck, Chris
Callison-Burch, and Nicholas Carlini. Deduplicating training data makes language mod-
els better. In Smaranda Muresan, Preslav Nakov, and Aline Villavicencio (eds.), Pro-
ceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume
1: Long Papers), pp. 8424–8445, Dublin, Ireland, May 2022. Association for Computa-
tional Linguistics. doi: 10.18653/v1/2022.acl-long.577. URL https://aclanthology.
org/2022.acl-long.577.
Anton Lozhkov, Raymond Li, Loubna Ben Allal, Federico Cassano, Joel Lamy-Poirier,
Nouamane Tazi, Ao Tang, Dmytro Pykhtar, Jiawei Liu, Yuxiang Wei, Tianyang Liu, Max
Tian, Denis Kocetkov, Arthur Zucker, Younes Belkada, Zijian Wang, Qian Liu, Dmitry
Abulkhanov, Indraneil Paul, Zhuang Li, Wen-Ding Li, Megan Risdal, Jia Li, Jian Zhu,
Terry Yue Zhuo, Evgenii Zheltonozhskii, Nii Osae Osae Dade, Wenhao Yu, Lucas Krauß,
Naman Jain, Yixuan Su, Xuanli He, Manan Dey, Edoardo Abati, Yekun Chai, Niklas
Muennighoff, Xiangru Tang, Muhtasham Oblokulov, Christopher Akiki, Marc Marone,
Chenghao Mou, Mayank Mishra, Alex Gu, Binyuan Hui, Tri Dao, Armel Zebaze, Olivier
Dehaene, Nicolas Patry, Canwen Xu, Julian McAuley, Han Hu, Torsten Scholak, Se-
bastien Paquet, Jennifer Robinson, Carolyn Jane Anderson, Nicolas Chapados, Mostofa
Patwary, Nima Tajbakhsh, Yacine Jernite, Carlos Mu˜noz Ferrandis, Lingming Zhang,
Sean Hughes, Thomas Wolf, Arjun Guha, Leandro von Werra, and Harm de Vries. Star-
coder 2 and the stack v2: The next generation, 2024.
Chenghao Mou, Chris Ha, Kenneth Enevoldsen, and Peiyuan Liu. Chenghaomou/text-
dedup: Reference snapshot, September 2023. URL https://doi.org/10.5281/zenodo.
8364980.
Quan Nguyen, Huy Pham, and Dung Dao. Vinallama: Llama-based vietnamese foun-
dation model. CoRR, abs/2312.11011, 2023a. doi: 10.48550/ARXIV.2312.11011. URL
https://doi.org/10.48550/arXiv.2312.11011.
22

--- Page 23 ---

Technical Report
Xuan-Phi Nguyen, Wenxuan Zhang, Xin Li, Mahani Aljunied, Qingyu Tan, Liying Cheng,
Guanzheng Chen, Yue Deng, Sen Yang, Chaoqun Liu, Hang Zhang, and Lidong Bing.
Seallms - large language models for southeast asia. CoRR, abs/2312.00738, 2023b. doi:
10.48550/ARXIV.2312.00738. URL https://doi.org/10.48550/arXiv.2312.00738.
Guilherme Penedo, Quentin Malartic, Daniel Hesslow, Ruxandra Cojocaru, Alessandro
Cappelli, Hamza Alobeidli, Baptiste Pannier, Ebtesam Almazrouei, and Julien Launay.
The RefinedWeb dataset for Falcon LLM: outperforming curated corpora with web data,
and web data only. arXiv preprint arXiv:2306.01116, 2023. URL https://arxiv.org/abs/
2306.01116.
Kunat Pipatanakul, Phatrasek Jirabovonvisut, Potsawee Manakul, Sittipong Sripaisarn-
mongkol, Ruangsak Patomwong, Pathomporn Chokchainant, and Kasima Tharnpip-
itchai.
Typhoon: Thai large language models.
CoRR, abs/2312.13951, 2023.
doi:
10.48550/ARXIV.2312.13951. URL https://doi.org/10.48550/arXiv.2312.13951.
Edoardo Maria Ponti, Goran Glavas, Olga Majewska, Qianchu Liu, Ivan Vulic, and Anna
Korhonen. XCOPA: A multilingual dataset for causal commonsense reasoning. In Pro-
ceedings of the 2020 Conference on Empirical Methods in Natural Language Processing, EMNLP
2020, Online, November 16-20, 2020, pp. 2362–2376. Association for Computational Lin-
guistics, 2020. URL https://doi.org/10.18653/v1/2020.emnlp-main.185.
Ivan Provilkov, Dmitrii Emelianenko, and Elena Voita. BPE-dropout: Simple and effective
subword regularization. In Dan Jurafsky, Joyce Chai, Natalie Schluter, and Joel Tetreault
(eds.), Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics,
pp. 1882–1892, Online, July 2020. Association for Computational Linguistics. doi: 10.
18653/v1/2020.acl-main.170. URL https://aclanthology.org/2020.acl-main.170.
Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, and Percy Liang. Squad: 100, 000+
questions for machine comprehension of text. In Proceedings of the 2016 Conference on Em-
pirical Methods in Natural Language Processing, EMNLP 2016, Austin, Texas, USA, Novem-
ber 1-4, 2016, pp. 2383–2392. The Association for Computational Linguistics, 2016. URL
https://doi.org/10.18653/v1/d16-1264.
Ahad Rana. Common crawl – building an open web-scale crawl using hadoop, 2010. URL
https://www.slideshare.net/hadoopusergroup/common-crawlpresentation.
Rico Sennrich, Barry Haddow, and Alexandra Birch. Neural machine translation of rare
words with subword units. In Katrin Erk and Noah A. Smith (eds.), Proceedings of the 54th
Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp.
1715–1725, Berlin, Germany, August 2016. Association for Computational Linguistics.
doi: 10.18653/v1/P16-1162. URL https://aclanthology.org/P16-1162.
Noam Shazeer. Glu variants improve transformer, 2020.
Mohammad Shoeybi, Mostofa Patwary, Raul Puri, Patrick LeGresley, Jared Casper, and
Bryan Catanzaro.
Megatron-lm:
Training multi-billion parameter language mod-
els using model parallelism.
ArXiv, abs/1909.08053, 2019.
URL https://api.
semanticscholar.org/CorpusID:202660670.
Daria
Soboleva,
Faisal
Al-Khateeb,
Robert
Myers,
Jacob
R
Steeves,
Joel
Hestness,
and
Nolan
Dey.
SlimPajama:
A
627B
token
cleaned
and
deduplicated
version
of
RedPajama.
https://www.cerebras.net/blog/
slimpajama-a-627b-token-cleaned-and-deduplicated-version-of-redpajama,
2023. URL https://huggingface.co/datasets/cerebras/SlimPajama-627B.
Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen, and Yunfeng Liu. Roformer:
Enhanced transformer with rotary position embedding, 2022.
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux,
Timoth´ee Lacroix, Baptiste Rozi`ere, Naman Goyal, Eric Hambro, Faisal Azhar, Aur´elien
Rodriguez, Armand Joulin, Edouard Grave, and Guillaume Lample. Llama: Open and
efficient foundation language models.
CoRR, abs/2302.13971, 2023a.
doi: 10.48550/
ARXIV.2302.13971. URL https://doi.org/10.48550/arXiv.2302.13971.
23

--- Page 24 ---

Technical Report
Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine
Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, Dan Bikel,
Lukas Blecher, Cristian Canton-Ferrer, Moya Chen, Guillem Cucurull, David Esiobu,
Jude Fernandes, Jeremy Fu, Wenyin Fu, Brian Fuller, Cynthia Gao, Vedanuj Goswami,
Naman Goyal, Anthony Hartshorn, Saghar Hosseini, Rui Hou, Hakan Inan, Marcin
Kardas, Viktor Kerkez, Madian Khabsa, Isabel Kloumann, Artem Korenev, Punit Singh
Koura, Marie-Anne Lachaux, Thibaut Lavril, Jenya Lee, Diana Liskovich, Yinghai Lu,
Yuning Mao, Xavier Martinet, Todor Mihaylov, Pushkar Mishra, Igor Molybog, Yixin
Nie, Andrew Poulton, Jeremy Reizenstein, Rashi Rungta, Kalyan Saladi, Alan Schel-
ten, Ruan Silva, Eric Michael Smith, Ranjan Subramanian, Xiaoqing Ellen Tan, Binh
Tang, Ross Taylor, Adina Williams, Jian Xiang Kuan, Puxin Xu, Zheng Yan, Iliyan Zarov,
Yuchen Zhang, Angela Fan, Melanie Kambadur, Sharan Narang, Aur´elien Rodriguez,
Robert Stojnic, Sergey Edunov, and Thomas Scialom. Llama 2: Open foundation and
fine-tuned chat models. CoRR, abs/2307.09288, 2023b. doi: 10.48550/ARXIV.2307.09288.
URL https://doi.org/10.48550/arXiv.2307.09288.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N.
Gomez, Łukasz Kaiser, and Illia Polosukhin. Attention is all you need. In Proceedings
of the 31st International Conference on Neural Information Processing Systems, NIPS’17, pp.
6000–6010, Red Hook, NY, USA, 2017. Curran Associates Inc. ISBN 9781510860964.
Tiannan Wang, Jiamin Chen, Qingrui Jia, Shuai Wang, Ruoyu Fang, Huilin Wang, Zhaowei
Gao, Chunzhao Xie, Chuou Xu, Jihong Dai, Yibin Liu, Jialong Wu, Shengwei Ding, Long
Li, Zhiwei Huang, Xinle Deng, Teng Yu, Gangan Ma, Han Xiao, Zixin Chen, Danjun
Xiang, Yunxia Wang, Yuanyuan Zhu, Yi Xiao, Jing Wang, Yiru Wang, Siran Ding, Jiayang
Huang, Jiayi Xu, Yilihamu Tayier, Zhenyu Hu, Yuan Gao, Chengfeng Zheng, Yueshu Ye,
Yihang Li, Lei Wan, Xinyue Jiang, Yujie Wang, Siyu Cheng, Zhule Song, Xiangru Tang,
Xiaohua Xu, Ningyu Zhang, Huajun Chen, Yuchen Eleanor Jiang, and Wangchunshu
Zhou. Weaver: Foundation models for creative writing. CoRR, abs/2401.17268, 2024. doi:
10.48550/ARXIV.2401.17268. URL https://doi.org/10.48550/arXiv.2401.17268.
Tianwen Wei, Liang Zhao, Lichang Zhang, Bo Zhu, Lijie Wang, Haihua Yang, Biye Li,
Cheng Cheng, Weiwei L¨u, Rui Hu, Chenxia Li, Liu Yang, Xilin Luo, Xuejie Wu, Lu-
nan Liu, Wenjun Cheng, Peng Cheng, Jianhao Zhang, Xiaoyu Zhang, Lei Lin, Xiaokun
Wang, Yutuan Ma, Chuanhai Dong, Yanqi Sun, Yifu Chen, Yongyi Peng, Xiaojuan Liang,
Shuicheng Yan, Han Fang, and Yahui Zhou. Skywork: A more open bilingual foun-
dation model.
CoRR, abs/2310.19341, 2023.
doi: 10.48550/ARXIV.2310.19341.
URL
https://doi.org/10.48550/arXiv.2310.19341.
Guillaume Wenzek, Marie-Anne Lachaux, Alexis Conneau, Vishrav Chaudhary, Francisco
Guzm´an, Armand Joulin, and Edouard Grave. Ccnet: Extracting high quality mono-
lingual datasets from web crawl data. In Nicoletta Calzolari, Fr´ed´eric B´echet, Philippe
Blache, Khalid Choukri, Christopher Cieri, Thierry Declerck, Sara Goggi, Hitoshi Isa-
hara, Bente Maegaard, Joseph Mariani, H´el`ene Mazo, Asunci´on Moreno, Jan Odijk, and
Stelios Piperidis (eds.), Proceedings of The 12th Language Resources and Evaluation Confer-
ence, LREC 2020, Marseille, France, May 11-16, 2020, pp. 4003–4012. European Language
Resources Association, 2020a. URL https://aclanthology.org/2020.lrec-1.494/.
Guillaume Wenzek, Marie-Anne Lachaux, Alexis Conneau, Vishrav Chaudhary, Francisco
Guzm´an, Armand Joulin, and ´Edouard Grave. Ccnet: Extracting high quality mono-
lingual datasets from web crawl data. In Proceedings of The 12th Language Resources and
Evaluation Conference, pp. 4003–4012, 2020b.
Yiheng Xu, Hongjin SU, Chen Xing, Boyu Mi, Qian Liu, Weijia Shi, Binyuan Hui, Fan Zhou,
Yitao Liu, Tianbao Xie, Zhoujun Cheng, Siheng Zhao, Lingpeng Kong, Bailin Wang,
Caiming Xiong, and Tao Yu. Lemur: Harmonizing natural language and code for lan-
guage agents. In The Twelfth International Conference on Learning Representations, 2024.
URL https://openreview.net/forum?id=hNhwSmtXRh.
Zheng Xin Yong, Ruochen Zhang, Jessica Forde, Skyler Wang, Arjun Subramonian, Holy
Lovenia, Samuel Cahyawijaya, Genta Winata, Lintang Sutawika, Jan Christian Blaise
24

--- Page 25 ---

Technical Report
Cruz, Yin Lin Tan, Long Phan, Long Phan, Rowena Garcia, Thamar Solorio, and Alham
Aji. Prompting multilingual large language models to generate code-mixed texts: The
case of south East Asian languages. In Genta Winata, Sudipta Kar, Marina Zhukova,
Thamar Solorio, Mona Diab, Sunayana Sitaram, Monojit Choudhury, and Kalika Bali
(eds.), Proceedings of the 6th Workshop on Computational Approaches to Linguistic Code-
Switching, pp. 43–63, Singapore, December 2023. Association for Computational Linguis-
tics. doi: 10.18653/v1/2023.calcs-1.5. URL https://aclanthology.org/2023.calcs-1.
5.
Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi, and Yejin Choi. Hellaswag: Can a
machine really finish your sentence? In Proceedings of the 57th Conference of the Association
for Computational Linguistics, ACL 2019, Florence, Italy, July 28- August 2, 2019, Volume
1: Long Papers, pp. 4791–4800. Association for Computational Linguistics, 2019.
doi:
10.18653/V1/P19-1472. URL https://doi.org/10.18653/v1/p19-1472.
Peiyuan Zhang, Guangtao Zeng, Tianduo Wang, and Wei Lu. Tinyllama: An open-source
small language model. CoRR, abs/2401.02385, 2024. doi: 10.48550/ARXIV.2401.02385.
URL https://doi.org/10.48550/arXiv.2401.02385.
Wenxuan Zhang, Mahani Aljunied, Chang Gao, Yew Ken Chia, and Lidong Bing. M3exam:
A multilingual, multimodal, multilevel benchmark for examining large language mod-
els. In Advances in Neural Information Processing Systems 36: Annual Conference on Neu-
ral Information Processing Systems 2023, NeurIPS 2023, New Orleans, LA, USA, Decem-
ber 10 - 16, 2023, 2023. URL http://papers.nips.cc/paper_files/paper/2023/hash/
117c5c8622b0d539f74f6d1fb082a2e9-Abstract-Datasets_and_Benchmarks.html.
Jun Zhao, Zhihao Zhang, Luhui Gao, Qi Zhang, Tao Gui, and Xuanjing Huang.
Llama beyond english: An empirical study on language capability transfer.
CoRR,
abs/2401.01055, 2024.
doi: 10.48550/ARXIV.2401.01055.
URL https://doi.org/10.
48550/arXiv.2401.01055.
Wanjun Zhong, Ruixiang Cui, Yiduo Guo, Yaobo Liang, Shuai Lu, Yanlin Wang, Amin
Saied, Weizhu Chen, and Nan Duan. Agieval: A human-centric benchmark for evaluat-
ing foundation models. CoRR, abs/2304.06364, 2023. doi: 10.48550/ARXIV.2304.06364.
URL https://doi.org/10.48550/arXiv.2304.06364.
25

--- Page 26 ---

Technical Report
Algorithm 1 Fix Escape Issue for MADLAD-400
Require: text
Ensure: processed text
1: processed text ←””
2: sentences ←text.split(”\n”)
3: for i ←0 to length(sentences) −1 do
4:
has period space ←”.” ∈sentences[i]
5:
next has period space ←i < length(sentences) −1 and ”.” ∈sentences[i + 1]
6:
if has period space or next has period space then
7:
separator ←”\n\n”
8:
else
9:
separator ←”\n”
10:
end if
11:
processed text ←processed text + sentences[i] + separator
12: end for
13: processed text ←processed text.rstrip(”\n”)
14: return processed text
A
Fixing the Escape Issue in MADLAD-400 Dataset
The MADLAD-400 dataset presents an issue with unicode escaping, notably the excessive
occurrence of “\\n”, as discussed in the HuggingFace forum32. This issue could potentially
disrupt the in-context learning and chatbot applications, since “\n” is a common delimiter
between demonstrations and task inputs. Consequently, it is necessary to replace “\\n”
with either “\n\n” or “\n” to resolve this problem.
We fix the problem using a simple heuristic rule as shown in Algorithm 1. For example,
the original input is “A.\\nB.\\nC. D.\\nE. F.\\nG.”, where the utter-cased letter like A
and G, stands for individual sentence. The fixed output would be “A.\nB.\n\nC. D.\n\nE.
F.\n \nG.”. The challenge (the underlined parts) is to generate the “\n\n” between B. and
C. The rules for splitting text are defined as: (1) When a paraphrase contains more than
two periods, it is separated from its neighboring element with two spaces. (2) In all other
cases, a single space is used as the delimiter. For a clearer comparison, please refer to the
following specific examples.
32https://huggingface.co/datasets/allenai/MADLAD-400/discussions/2
26

--- Page 27 ---

Technical Report
Original Example with Escape Issue from the MADLAD-400 Indonesian Subset.
Masih Diributkan, Pakar Analisis Ucapan Puan: Maknanya Dalam\\nSenin, 07
September 2020 07:16 WIB\\nPakar komunikasi politik Universitas Pelita Hara-
pan Emrus Sihombing sangat menyayangkan terjadinya penggiringan wacana
negatif di ruang publik, terkait pernyataan Ketua DPP PDIP, Puan Maharani, baru-
baru ini.\\nEmrus mengatakan, orang yang tidak setuju lebih cenderung pen-
dapatnya bernuansa politis dan pragmatis daripada substansi makna mendalam
dari pernyataan Puan yang menyebut ’semoga Sumbar jadi pendukung negara
Pancasila’.\\n¨Jika kita simak dengan teori akal sehat saja, ungkapan Puan sedikit-
pun tidak menyebut apalagi menyinggung (perasaan) suku atau etnis tertentu yang
ada di Sumbar. Diksi yang ada pada kalimat tersebut yaitu ’Sumbar’ sebagai nama
provinsi yaitu Sumatera Barat. Bukan suku atau etnis tertentu,¨kata Emrus, Minggu
(6/9/2020).\\nBaca Juga: Mbak Puan, Jangan Jadi Pemecah Bangsa\\nEmrus men-
jelaskan, Indonesia sebagai negara kesatuan harus dimaknai bahwa setiap provinsi
milik kita bersama, bukan seolah milik satu etnis atau suku tertentu, sekalipun et-
nis tersebut lebih dulu datang dan tinggal di provinsi tersebut dan boleh jadi lebih
banyak jumlahnya.\\nWarga masyarakat Sumbar, dari segi etnis atau suku san-
gat heterogen. Emrus menilai semua suku dari seluruh Tanah Air sudah ada di
Sumbar, atau setidaknya pernah tinggal di sana. Sehingga, Sumbar bukan suku
atau etnis.\\nOleh karena itu, jika ada sekelompok orang mengatasnamakan suku
tertentu menolak pernyataan Puan atau berencana melaporkan ke proses hukum,
tampaknya kurang pas dan bisa jadi belum melakukan pengkajian mendalam
dan hilostik.\\n¨Seharusnya wacana publik tertuju pada bagaimana perwujudan
hak setiap individu sebagai WNI yang tinggal di Sumbar dan di semua provinsi
di Indonesia dapat dijamin dan diwujudkan dalam kehidupan sehari-hari,¨ucap
Emrus.\\n ¨Konstitusi kita, UUD 1945, menggunakan kata ’setiap’ warga negara,
bukan menggunakan diksi ’kelompok’ atas dasar kategori sosial tertentu, terma-
suk etnis. Artinya, setiap individu WNI memiliki hak dan kewajiban yang sama
sekalipun dari suku atau etnis yang berbeda,¨tambahnya.\\nTag: Puan Maharani,
Partai Demokrasi Indonesia Perjuangan (PDIP), Pancasila
27

--- Page 28 ---

Technical Report
The Corresponding Fixed Example from the MADLAD-400 Indonesian Subset.
Masih Diributkan, Pakar Analisis Ucapan Puan: Maknanya Dalam
Senin, 07 September 2020 07:16 WIB
Pakar komunikasi politik Universitas Pelita Harapan Emrus Sihombing sangat
menyayangkan terjadinya penggiringan wacana negatif di ruang publik, terkait
pernyataan Ketua DPP PDIP, Puan Maharani, baru-baru ini.
Emrus mengatakan, orang yang tidak setuju lebih cenderung pendapatnya bernu-
ansa politis dan pragmatis daripada substansi makna mendalam dari pernyataan
Puan yang menyebut ’semoga Sumbar jadi pendukung negara Pancasila’.
¨Jika kita simak dengan teori akal sehat saja, ungkapan Puan sedikitpun tidak
menyebut apalagi menyinggung (perasaan) suku atau etnis tertentu yang ada
di Sumbar. Diksi yang ada pada kalimat tersebut yaitu ’Sumbar’ sebagai nama
provinsi yaitu Sumatera Barat. Bukan suku atau etnis tertentu,¨kata Emrus, Minggu
(6/9/2020).
Baca Juga: Mbak Puan, Jangan Jadi Pemecah Bangsa
Emrus menjelaskan, Indonesia sebagai negara kesatuan harus dimaknai bahwa
setiap provinsi milik kita bersama, bukan seolah milik satu etnis atau suku tertentu,
sekalipun etnis tersebut lebih dulu datang dan tinggal di provinsi tersebut dan
boleh jadi lebih banyak jumlahnya.
Warga masyarakat Sumbar, dari segi etnis atau suku sangat heterogen.
Emrus
menilai semua suku dari seluruh Tanah Air sudah ada di Sumbar, atau setidaknya
pernah tinggal di sana. Sehingga, Sumbar bukan suku atau etnis.
Oleh karena itu, jika ada sekelompok orang mengatasnamakan suku tertentu
menolak pernyataan Puan atau berencana melaporkan ke proses hukum, tam-
paknya kurang pas dan bisa jadi belum melakukan pengkajian mendalam dan
hilostik.
¨Seharusnya wacana publik tertuju pada bagaimana perwujudan hak setiap indi-
vidu sebagai WNI yang tinggal di Sumbar dan di semua provinsi di Indonesia
dapat dijamin dan diwujudkan dalam kehidupan sehari-hari,¨ucap Emrus.
¨Konstitusi kita, UUD 1945, menggunakan kata ’setiap’ warga negara, bukan
menggunakan diksi ’kelompok’ atas dasar kategori sosial tertentu, termasuk etnis.
Artinya, setiap individu WNI memiliki hak dan kewajiban yang sama sekalipun
dari suku atau etnis yang berbeda,¨tambahnya.
Tag: Puan Maharani, Partai Demokrasi Indonesia Perjuangan (PDIP), Pancasila
B
Data Deduplication Case Study
We list the top-3 frequent textual duplicates for each language in Figure 9. To increase the
distinctiveness between examples, we group them in units of 100 frequencies. Ultimately,
the highest values from the first three groups are selected for demonstration.
C
Evaluation on M3Exam by HellaSwag Style
Table 8 shows the model performance on the M3Exam dataset following the evaluation
approach adopted in the HellaSwag benchmark in both the Eleuther AI LM Evaluation
Harness and the OpenCompass platform. We obtained the evaluation results by replacing
the answer part with each possible option and appending it to the pre-defined prompt of
the given question. Then, we rank the concatenated text strings by their perplexity scores
provided by models and choose the one with the lowest perplexity as the model predic-
tion. As observed, while models evaluated using this approach generally exhibit lower
performance compared to the evaluation method used in M3Exam, our inspection reveals
that the models exhibit significantly reduced option bias under the evaluation protocol.
28

--- Page 29 ---

Technical Report
Corpus
Property
#1 Deduplicate
#2 Deduplicate
#3 Deduplicate
CC100
Indonesian
Text
tekanan intra-abdomen
 (kembung berkepanjangan,
ascitis, adanya massa
 intra-abdomen,
atau kehamilan
ra-abdomen (kembung
berkepanjangan, ascitis,
 adanya massa intra-
abdomen, atau kehamilan),
genetik
a-abdomen (kembung
berkepanjangan, ascitis,
adanya massa intra-abdomen,
 atau kehamilan), genetik
Translation
intra-abdominal pressure
(prolonged bloating, ascitis,
presence of an intra-
abdominal mass,
or pregnancy
ra-abdominal (prolonged
bloating, ascitis, presence of
an intra-abdominal mass,
or pregnancy), genetics
a-abdomen (prolonged
bloating, ascitis, presence of
an intra-abdominal mass, or
pregnancy), genetics
Count
40,371
30,312
20,155
CC100
Thai
Text
้อҊลเٲมเѠมเ٨ยวѕบราย
ละเ҇ยด'
านѯนหาโรงแรมьเหมาะҍ
หٕบท҂ปђ'
ҍหٕบٚอҊลเٲมเѠมเ٨ยวѕ
บราย'
Translation
More information on details
Search for hotels suitable
for day trips
For more information about
this
Count
41,901
37,636
35,748
CC100
Vietnamese
Text
Chơi Vui. Ngoài ra, bạn có
thể lựa chọn thêm nhiều chủ
đề game hấp dẫn khác'
điện tử Người Đưa Tin.
Mọi thông tin góp ý, chia sẻ
xin vui lòng gửi về hò
Translation
Fun. In addition, you can
choose from many other
attractive game themes.
electronic Messenger. If
you have any information,
suggestions or shares,
please send them to 'ho'.
News. Please send any
comments or suggestions to
the mailbox [Sensitive Data]
Count
9,219
7,892
7,164
MADLAD-400
Indonesian
Text
innya. Segera obati dengan
obat herbal kami yang sudah
terbukti ampuh dan aman
dalam mengobati penya
bal kami yang sudah terbukti
ampuh dan aman dalam
mengobati penyakit anda,
karena obat kami sudah be
bukti ampuh dan aman dalam
mengobati penyakit anda,
karena obat kami sudah
berlisensi dengan No. UKO
Translation
innya. Treat immediately with
our herbal medicine which
has been proven to be
effective and safe in
treating the disease.
Our bales have been proven
to be effective and safe in
treating your illness, because
our medicine has been
proof that it is effective and
safe in treating your disease,
because our medicine is
licensed with No. UKO
Count
37,009
32,622
29,286
MADLAD-400
Thai
Text
[Sensitive Data] เขตђฒนา
กҚงเทพมหานคร
Translation
[Sensitive Data],
Watthana District, Bangkok
Sukhumvit [Sensitive Data]
Road, Khlong Toei Nuea
Subdistrict
One Thirty-One Company
Limited (Office
Count
121,364
121,255
121,119
MADLAD-400
Vietnamese
Text
bạn hãy chia sẻ với bạn bè
của mình và luôn theo dõi,
ủng hộ chúng tôi để
và luôn theo dõi, ủng hộ
chúng tôi để cập nhật những
thông tin mới nhất. Chú
ng nội dung bài viết sẽ đáp
ứng được nhu cầu của bạn,
chúng tôi sẽ thườn
Translation
Please share with your
friends and always follow
and support us to
If the content of the article
will meet your needs,
we will often
Count
13,813
12,516
11,438
Đưa Tin. Mọi thông tin góp ý,
chia sẻ xin vui lòng gửi về
hòm thư [Sensitive Data]
And always follow and
support us to update the latest
information. Uncle
ถนนєԟมҏท
[Sensitive Data]
แขวงคลองเตยเหڮ
บ҂Ғท ђน สามҲบเڟด ҃ѕด
(ҍѢกงา
Figure 9: The top-3 frequent textual duplicates identified across CC100 and MADLAD-400
for three SEA languages, along with their respective frequencies. Inappropriate content
and personally identifiable information are replaced with [Sensitive Data]. The lengthy
content is truncated for clear visualization.
29

--- Page 30 ---

Technical Report
3-shot (EM)
M3Exam (th)
M3Exam (jv)
M3Exam (vi)
Qwen1.5-0.5B
22.93
25.07
26.66
Sailor-0.5B
24.41
26.15
30.91
Qwen1.5-1.8B
24.04
24.26
28.68
Sailor-1.8B
25.38
28.30
34.71
Qwen1.5-4B
24.50
24.26
30.02
Sailor-4B
27.88
31.27
40.69
Llama-2-7B
23.67
25.07
33.15
Mistral-7B-v0.1
26.03
26.68
36.11
Typhoon-7B
28.53
–
–
VinaLLaMA-7B
–
–
36.22
Sea-Lion-7B
25.29
22.91
38.74
SeaLLM-7B-Hybrid
27.18
26.95
36.50
SeaLLM-7B-v2
28.48
29.92
39.18
Qwen1.5-7B
25.75
26.15
36.28
Sailor-7B
30.00
32.88
44.10
Table 8: Experimental results of different models on M3Exam using the HellaSwag style
evaluation protocol.
30

```
