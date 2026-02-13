---
title: "2024-authors-Detecting Anti-Semitic Hate Speech Using Transformer-Based - PDF Extract"
source_pdf: "2024-authors-Detecting Anti-Semitic Hate Speech Using Transformer-Based.pdf"
pages: 8
extracted_at: "2026-02-13T09:15:45.672940"
---

# PDF Extract: 2024-authors-Detecting Anti-Semitic Hate Speech Using Transformer-Based

**Source PDF:** 2024-authors-Detecting Anti-Semitic Hate Speech Using Transformer-Based.pdf
**Total Pages:** 8

---

## Content

```
--- Page 1 ---

Detecting Anti-Semitic Hate Speech using Transformer-based Large Language
Models
Dengyi Liu, Minghao Wang, Andrew G Catlin
Katz School of Science and Health
Yeshiva University
dliu6@mail.yu.edu, mwang3@mail.yu.edu, andrew.catlin@yu.edu
Abstract
Academic researchers and social media entities grap-
pling with the identification of hate speech face significant
challenges, primarily due to the vast scale of data and the
dynamic nature of hate speech. Given the ethical and prac-
tical limitations of large predictive models like ChatGPT
in directly addressing such sensitive issues, our research
has explored alternative advanced transformer-based and
generative AI technologies since 2019. Specifically, we de-
veloped a new data labeling technique and established a
proof of concept targeting anti-Semitic hate speech, utiliz-
ing a variety of transformer models such as BERT [1], Dis-
tillBERT [2], RoBERTa [3], and LLaMA-2 [4], comple-
mented by the LoRA [5] fine-tuning approach. This pa-
per delineates and evaluates the comparative efficacy of
these cutting-edge methods in tackling the intricacies of
hate speech detection, highlighting the need for responsi-
ble and carefully managed AI applications within sensitive
contexts.
1. Introduction
In our research, we investigate the prevalent and per-
nicious issue of anti-Semitic hate speech proliferating
across digital platforms, particularly Twitter. This study is
twofold: firstly, it involves the collection of online discourse
related to anti-Semitic sentiment, upon which we apply
our specially designed data labeling algorithm for annota-
tion; secondly, we employ a variety of modeling techniques
to discern and categorize hate speech.
These method-
ologies include different embedding approaches coupled
with machine learning algorithms such as k-NN (k-nearest
neighbors), linear regression, random forest, and naive
Bayes, in addition to state-of-the-art transformer-based
large pre-trained models like BERT [1], DistilBERT [2],
and RoBERTa [3].
Moreover, we refine the capabilities
of RoBERTa [3] and LLaMA-2 [4] through fine-tuning via
Low-Rank Adaptation (LoRA) [5] technology, aiming to
significantly enhance their performance in detecting subtle
and overt forms of anti-Semitic content.
The surge of anti-Semitic expression on social media
platforms, unfortunately, parallels the rise in their user
base, presenting multifaceted challenges to effective detec-
tion and moderation. By leveraging models recognized for
their profound linguistic understanding, our work aims to
amplify the efficacy of detection mechanisms against anti-
Semitic expressions online. Through the application of so-
phisticated Natural Language Processing (NLP) techniques,
this research endeavors to bolster online safety and con-
front the spectrum of hate speech. It provides valuable in-
sights into how advanced NLP techniques can be intricately
applied to elevate content moderation standards on digital
platforms, thereby contributing to the critical conversation
on combating online hate speech and ensuring a safer com-
municative environment.
2. Related Work
The battle against online hate speech has leveraged var-
ious NLP technologies to sift through vast online content,
seeking patterns and markers indicative of harmful speech.
This section reviews the literature on hate speech detec-
tion, with a focus on the evolution from rule-based and
traditional machine learning approaches to the more recent
adoption of transformer-based models.
2.1. Embeddings in NLP
The utilization of embeddings in NLP represents a criti-
cal evolution in how machines understand and process hu-
man language. Embeddings transform discrete textual el-
ements—such as words, phrases, or sentences—into con-
tinuous vectors of real numbers, capturing semantic mean-
ings in a dense representation. This technique significantly
differed from earlier vectorization methods like one-hot
encoding, which failed to encapsulate contextual relation-
ships. Pioneering models such as Word2Vec and GloVe in-
arXiv:2405.03794v1  [cs.CL]  6 May 2024

--- Page 2 ---

troduced by Mikolov et al. (2013) and Pennington et al.
(2014) respectively, demonstrated how embeddings could
capture syntactic and semantic word relationships based
on their co-occurrence in large text corpora, fundamen-
tally enhancing the machine’s ability to interpret text [6][7].
The development of contextual embeddings by models like
ELMo and GPT further refined this approach by consider-
ing the context of words within sentences, leading to im-
provements in numerous NLP tasks[8] [9].
Traditional vectorization techniques play a vital role in
feature extraction from text. Techniques such as CountVec-
torizer, TfidfVectorizer, and HashingVectorizer are funda-
mental in transforming raw text into numerical vectors that
can be ingested by machine learning models. CountVector-
izer converts text documents into a matrix of token counts,
effectively capturing the frequency of each word within the
documents. On the other hand, TfidfVectorizer combines
the benefits of CountVectorizer with the TF-IDF (Term
Frequency-Inverse Document Frequency) weighting, which
diminishes the impact of tokens that occur very frequently
and are thus less informative. HashingVectorizer, mean-
while, offers a stateless operation where the text is con-
verted into a numeric hash value; this is particularly useful
for datasets too large to fit in memory, as it does not require
vocabulary fitting [10].
• CountVectorizer: Transforms text into a frequency
matrix of tokens which can effectively support mod-
els in learning from text data.
• TfidfVectorizer: Calculates TF-IDF scores for the to-
kens in text, balancing the frequency of tokens against
their rarity across all documents, enhancing the ability
to identify meaningful words.
• HashingVectorizer: Applies a hashing function to
term frequency counts, making it efficient for large-
scale text processing as it avoids the need to fit and
store a vocabulary in memory.
These vectorization techniques are instrumental in pre-
processing text for both traditional machine learning and
deep learning models, serving as a bridge between raw data
and the sophisticated algorithms designed to process them.
2.2. Traditional Methods to Hate Speech Detection
Initial efforts in hate speech detection predominantly uti-
lized rule-based algorithms and traditional machine learn-
ing models. These approaches, while foundational, often
struggled with the subtleties of language and context, lead-
ing to high false positive rates and limited scalability. Semi-
nal works such as Warner and Hirschberg (2012) and David-
son et al. (2017) explored the use of Support Vector Ma-
chines (SVM) and Naive Bayes classifiers, setting a prece-
dent for automated content moderation but highlighting the
need for more nuanced understanding and classification of
text [11] [12].
Further extending the repertoire of traditional machine
learning methods, Logistic Regression, k-Nearest Neigh-
bors (k-NN), and Random Forests have also been applied
to hate speech detection with varying degrees of success.
Logistic Regression, a linear model, is often favored for its
simplicity and interpretability, making it particularly useful
in scenarios where understanding the influence of individual
features (such as specific words or phrases) on the predic-
tion is crucial [13]. Meanwhile, k-NN has been employed
for its non-parametric nature, where the classification of a
document is based on the majority label among its nearest
neighbors in the feature space. This method is intuitive and
effective, especially when dealing with well-segmented data
clusters [14].
Random Forests, as an ensemble method comprising nu-
merous decision trees, provide a robust alternative to single
estimators like SVM. The strength of Random Forests lies
in their ability to reduce overfitting by averaging multiple
deep decision trees, trained on different parts of the same
training set. This method is exceptionally good at handling
the non-linear relationships and interactions within textual
data, thus providing better generalization in detecting hate
speech across diverse contexts [15].
These traditional models, though sometimes overshad-
owed by the more recent deep learning approaches, con-
tinue to be relevant, particularly in resource-constrained en-
vironments or as part of hybrid systems that incorporate
both traditional and modern techniques.
2.3. Deep Learning in NLP
The introduction of deep learning to NLP marked a sig-
nificant turning point, offering models capable of under-
standing complex language patterns through layered rep-
resentations [16]. Convolutional Neural Networks (CNNs)
and Recurrent Neural Networks (RNNs) began to outper-
form their predecessors in various tasks, including senti-
ment analysis and topic classification. However, these mod-
els still faced challenges in capturing long-term dependen-
cies and context in text, a crucial aspect of detecting hate
speech [17] [18].
2.4. Transformer Architecture
Since the invention of the transformer architecture [19],
the attention mechanism has been increasingly used in the
NLP field due to its good parallel computing capabilities.
Also, a transformer-based model can be used to do text
classification tasks. The advent of transformer architecture
revolutionized NLP by enabling models to process words
concerning all other words in a sentence, thus capturing the
context more effectively than ever before [19]. Building
upon this, BERT (Bidirectional Encoder Representations

--- Page 3 ---

from Transformers), developed by Devlin et al. (2019), rep-
resented a landmark in pre-trained models, allowing for an
even more nuanced understanding of language through bidi-
rectional training [1].
Following the success of BERT, DistilBERT was intro-
duced by Sanh et al. (2019) as a smaller, faster, and lighter
version of BERT. DistilBERT optimizes BERT’s architec-
ture to maintain 97% of its language understanding capabil-
ities while reducing the model size by 40% and speeding up
training significantly [2]. This makes it more accessible and
practical for real-time applications.
RoBERTa (Robustly Optimized BERT Approach), de-
veloped by Liu et al. (2019), extends BERT by modify-
ing key hyperparameters, training with much larger mini-
batches and learning rates, and training on more data.
RoBERTa removes BERT’s next-sentence pretraining ob-
jective and dynamically changes the masking pattern ap-
plied to the training data. This has led to improved perfor-
mance across a range of NLP tasks compared to BERT [3].
An interesting advancement in model adaptation is
LoRA (Low-Rank Adaptation), which can be applied
to models like RoBERTa.
LoRA allows for efficiently
adapting large pre-trained models with minimal addi-
tional parameters, preserving the original parameters while
achieving comparable performance to full fine-tuning ap-
proaches [5].
Recently, LLaMA-2 was introduced as an evolution of
transformer models designed for generative and multitask-
ing capabilities across multiple languages. LLaMA-2 ben-
efits from a large-scale training corpus and has shown sig-
nificant advancements in understanding and generating lan-
guage tasks [4]. When combined with LoRA, LLaMA-2
can be fine-tuned in a parameter-efficient manner, allowing
for custom adaptations without extensive retraining of the
model.
These developments reflect the ongoing innovation
within transformer-based architectures, making them more
efficient and adaptable for a wide range of NLP applica-
tions.
2.5. Application to Hate Speech Detection
Following these advancements, several studies have
specifically applied transformer-based models to the detec-
tion of hate speech. For instance, works by Mozafari et al.
(2019) and Yuan et al. (2019) demonstrated the superior
performance of BERT and its variants in classifying vari-
ous forms of online abuse and hate speech, including anti-
Semitic content. These studies underscore the effectiveness
of transformer-based models in grasping the complexities
and evolving nature of online discourse [20] [21].
2.6. Limitations and Future Directions
Despite their success, transformer-based models are not
without limitations. The high computational cost, need for
extensive training data, and challenges in interpretability
remain significant hurdles. Ongoing research is directed
towards making these models more accessible and under-
standable, with efforts like DistilBERT and TinyBERT of-
fering more efficient, albeit slightly less powerful, alterna-
tives [2] [22].
3. Methods
3.1. Data preparation and labeling method
In the development of this research, the formation of a
focused data analysis group was instrumental. This group
was tasked with establishing a comprehensive strategy for
data annotation, aimed at evaluating online discourse for
potential anti-Semitic content.
To this end, the Twitter
Application Programming Interface (API) was employed
to systematically retrieve a dataset consisting of approxi-
mately 10,000 posts, believed to have relevance to Jewish
topics based on preliminary keywords and contextual anal-
ysis.
The data annotation process, involved a detailed exam-
ination of the retrieved posts. This phase was critical in
identifying and labeling the manifestations of anti-Semitic
sentiments within the dataset. Through the collective efforts
of the data team, a subset of 3,000 posts was labeled.
Following the initial phase of data collection and prelim-
inary annotation, our research protocol detailed a structured
approach for the in-depth analysis and classification of the
data. The annotation process was carried out by a dedicated
team of two researchers, who independently reviewed each
post within the dataset. This methodological approach en-
sured that personal biases were minimized and that a com-
prehensive review of each post was conducted from multi-
ple perspectives.
Upon completion of the independent review process
by both team members, posts for which there was unan-
imous agreement—where both annotators identified a post
as exhibiting anti-Semitic sentiment—were immediately as-
signed a final label. This approach streamlined the initial
stage of data categorization, allowing for the rapid identi-
fication and classification of clear-cut cases of anti-Semitic
content.
For posts where the two initial annotators disagreed, a
distinctive procedure was implemented. These contentious
cases were escalated to a third, impartial reviewer. This
reviewer served as a mediator and provided an additional
level of scrutiny.
Following this, a joint discussion ses-
sion was organized involving all three team members. Dur-
ing this collaborative review, the disputed posts were re-
evaluated, and consensus was sought.
The outcome of

--- Page 4 ---

these discussions led to the final determination of the labels
for these disputed posts, ensuring a thorough and demo-
cratically reached conclusion to each case of uncertainty.
This meticulous approach to data annotation underscores
the commitment of our research to precision and reliabil-
ity in the identification of online hate speech.
Algorithm 1 Data Annotation with Threshold-Based Label-
ing and Dispute Resolution
1: Input: Dataset of posts (D)
2: Output: Annotated posts with labels (L)
3: Initialize annotated set L = ∅
4: Set scoring threshold θ = 6
5: for each post p ∈D do
6:
Annotator1 scores p with score1 from 0 to 10
7:
Annotator2 scores p with score2 from 0 to 10
8:
Determine label for p by Annotator1: label1 =
(score1 ≥θ)
9:
Determine label for p by Annotator2: label2 =
(score2 ≥θ)
10:
if label1 == label2 then
11:
Assign final label labelf = label1 to p
12:
Add (p, labelf) to L
13:
else
14:
Assign p to a third, impartial reviewer
15:
Third reviewer scores p with score3 from 0 to
10
16:
Determine
final
label
by
third
reviewer:
labelf = (score3 ≥θ)
17:
Add (p, labelf) to L
18:
end if
19: end for
20: return L
3.2. Train on machine learning and Fine-tuning
transformer-based models
In this segment of our research, we delineate the
methodologies applied in training traditional machine learn-
ing models with different embeddings and fine-tuning
transformer-based models to classify online discourse po-
tentially exhibiting anti-Semitic content. This classification
effort was premised on a well-defined data preparation and
annotation process, as delineated in preceding sections.
Initially, a dataset comprising approximately 10,000
posts suspected to carry relevance to Jewish topics was sys-
tematically compiled using the Twitter API. A focused data
analysis group undertook a meticulous annotation strat-
egy, identifying and labeling instances of anti-Semitic sen-
timents within a subset of 3,000 posts. This foundational
work laid the groundwork for the subsequent training and
evaluation of various classification models.
Machine Learning Models Training: Traditional ma-
chine learning models including Naive Bayes, SVM, Ran-
dom Forests, Logistic Regression, and K-Nearest Neigh-
bors (K-NN) were employed. These models were trained
using a standard approach, involving feature extraction
techniques such as TF-IDF for text representation, followed
by model-specific parameter tuning. The performance of
these models, as outlined in Table 2, indicates varied lev-
els of efficacy in classifying the annotated data, with SVM
showing a balanced performance and K-NN lagging in all
evaluated metrics.
Fine-tuning Transformer-based Models:
In contrast
to traditional machine learning approaches, transformer-
based models, specifically BERT [1], DistilBERT [2],
RoBERTa [3] and Llama-2 (7B) [4], were fine-tuned for
our classification task. These models leverage deep learn-
ing techniques that comprehend the complexities and nu-
ances of natural language, offering superior performance
over their machine learning counterparts. The fine-tuning
process involved adjusting pre-trained models to our spe-
cific dataset, optimizing them to understand the linguistic
subtleties of anti-Semitic discourse.
In traditional fine-tuning approaches for transformer-
based models, extensive parameter adjustments are typi-
cally required, which can be computationally expensive and
time-consuming, especially for models with a large num-
ber of parameters such as LLaMA-2 (7 billion parameters).
To address this challenge, we implemented the Low-rank
Adaptation (LoRA) method [5] to fine-tune RoBERTa and
LLaMA-2. LoRA strategically modifies only a small frac-
tion of the model’s parameters by introducing low-rank ma-
trices that adapt the pre-trained weights rather than alter-
ing them extensively. This approach significantly reduces
the computational overhead by limiting the scope of pa-
rameter updates during the training phase. Our experiments
demonstrated that, by using LoRA, we were able to achieve
comparable or even superior performance to traditional full-
model fine-tuning while drastically cutting down on train-
ing time.
This efficiency makes LoRA an exceptionally
viable option for enhancing large-scale language models
without the substantial resource investment typically asso-
ciated with conventional fine-tuning techniques.
The results, as demonstrated, underscore the superior-
ity of transformer-based models in handling the intricacies
of language and sentiment in online hate speech. BERT,
in particular, achieved remarkable results, affirming the ef-
fectiveness of fine-tuning approaches in enhancing model
performance.
The distinctions in performance between machine learn-
ing models and transformer-based models highlight the ad-
vancements in NLP technology and their applicability in
addressing complex societal issues like online hate speech.
This analysis not only informs our understanding of the
models’ capabilities but also guides future efforts in online

--- Page 5 ---

Figure 1. This figure shows the workflow of voting algorithm.
discourse classification.
In conclusion, the training on machine learning and
fine-tuning of transformer-based models were instrumen-
tal in advancing our research objectives. The preparation
and annotation of our dataset provided a robust foundation
for evaluating these models, ultimately contributing to our
overarching goal of identifying and mitigating anti-Semitic
content online.
4. Results
Table 1 presents a comprehensive evaluation of various
machine learning algorithms’ performance with different
text embeddings. The algorithms considered include Lo-
gistic Regression, k-NN, SVM, Random Forests, and Naive
Bayes, assessed across metrics such as Accuracy, Precision,
Recall, and F1-score. These metrics are pivotal for under-
standing the models’ effectiveness in classification tasks,
with each offering insights into different aspects of perfor-
mance.
Logistic Regression shows consistent accuracy across all
embeddings but exhibits varying degrees of precision, re-
call, and F1-scores, pointing its sensitivity to the choice of
embedding. The traditional CountVectorizer, TfidfVector-
izer, and HashingVectorizer perform comparably, whereas
Word2Vec and GloVe show reduced effectiveness, particu-
larly in recall and F1-score.
k-NN and SVM display a similar result, with TfidfVec-
torizer and HashingVectorizer providing optimal perfor-
mance. Significantly, SVM shows a complete lack of recall
and F1-score when utilizing Word2Vec, indicating a signif-
icant mismatch between this embedding and the SVM algo-
rithm for the data in question.
Random Forests demonstrates a high degree of consis-
tency across CountVectorizer, TfidfVectorizer, and Hash-
ingVectorizer, matching the highest precision observed but
with moderate recall and F1-scores.
This suggests Ran-
dom Forests’ robustness to different sparse representations
while highlighting potential limitations with dense embed-
dings like Word2Vec and GloVe.
Naive Bayes is noteworthy for achieving a precision of
1.00 with TfidfVectorizer, albeit at the cost of reduced re-
call and F1-score. This notes that while Naive Bayes can be
highly confident in its predictions, it may also miss a signifi-
cant number of relevant instances. In addition, Naive Bayes
used only two embeddings because other methods produce
negative values, whereas naive bayes requires all inputs to
have positive values.
All these results illustrate the importance of selecting ap-
propriate embeddings for different algorithms. While some
models like Random Forests and Naive Bayes exhibit ro-
bustness to the choice of embedding, others, such as SVM,
show pronounced variability. These findings underscore the
need for careful embedding selection in machine learning
applications to optimize performance across all evaluation
metrics.
Our analysis provides a comprehensive evaluation of var-
ious machine learning and deep learning models for the
classification of online anti-Semitic discourse. The perfor-
mance of each model, as summarized in Table 2, is assessed
based on Accuracy, Precision, Recall, and F1-score.
The results indicate that transformer-based models, par-

--- Page 6 ---

Figure 2.
Architecture of LoRA fine-tuning applied to Llama2 model weights, demonstrating how the injection of trainable low-rank
matrices A and B (initialized as A with a normal distribution and B set to zero) allows for efficient adaptation of the model’s weights to
new tasks, preserving the original parameters while introducing minimal updates.
ticularly BERT, demonstrate superior performance over tra-
ditional machine learning classifiers. BERT achieves the
highest Accuracy and F1-score, highlighting the effective-
ness of deep learning models that capture contextual nu-
ances in text. Meanwhile, fine-tuning with LoRA shows
promise, especially in improving Recall for RoBERTa and
F1-scores for LLaMA-2 (7B), suggesting that targeted op-
timizations can further enhance the performance of pre-
trained models.
Traditional algorithms like Naive Bayes, SVM, Random
Forests, and Logistic Regression, while effective to a de-
gree, fall short of the transformer-based models in various
metrics. Notably, K-NN exhibits the least effectiveness, in-
dicating that simpler classification methods may struggle
with the complexity of language inherent in hate speech de-
tection.
In summary, our results advocate for the adoption of
transformer-based models in the automated detection of
anti-Semitic hate speech, with fine-tuning techniques such
as LoRA offering additional improvements in model sensi-
tivity and specificity.
5. Discussion
This study has examined the capabilities of both tra-
ditional machine learning and modern transformer-based
models in identifying anti-Semitic content within online
discourse. The annotation process, underpinned by a demo-
cratic approach, established a robust dataset for training and
evaluating the performance of different models.
Our findings reveal that while traditional machine learn-
ing models, such as SVM and Logistic Regression, provide
a decent baseline in terms of accuracy and precision, they
fall short in capturing the nuanced context and complexities
inherent in natural language. This is evident in the rela-
tively low recall scores, indicating a significant number of
relevant cases went undetected. Conversely, K-NN’s under-
performance across all metrics highlights the challenges tra-
ditional algorithms face with high-dimensional and sparse
textual data.
The superior performance of transformer-based models,
notably BERT, DistilBERT, and RoBERTa, underscores the
transformative impact of deep learning in natural language
processing tasks. These models achieved notably higher
scores in all metrics, particularly in precision and recall,
illustrating their enhanced ability to discern nuanced lan-
guage patterns and contextual meanings. This is a critical
advancement, considering the sophisticated and evolving
nature of online hate speech.
However, the deployment of such models is not without
challenges. Transformer-based models require significant
computational resources and expertise, potentially limiting
their accessibility for smaller organizations or independent
researchers.
Additionally, the black-box nature of these
models can pose interpretability challenges, complicating
the process of understanding and explaining the basis of
their classifications.
6. Conclusion
The research undertaken provides valuable insights into
the application of machine learning and deep learning tech-

--- Page 7 ---

Table 1. Results of Different Models
Model
Accuracy
Precision
Recall
F1-score
Embedding
Logistic Regression
0.91
0.87
0.66
0.75
CountVectorizer
0.91
0.94
0.55
0.70
TfidfVectorizer
0.91
0.90
0.61
0.72
HashingVectorizer
0.81
0.50
0.18
0.26
Word2Vec
0.85
0.76
0.32
0.46
GloVe
k-NN
0.85
0.79
0.30
0.44
CountVectorizer
0.91
0.91
0.58
0.71
TfidfVectorizer
0.91
0.93
0.56
0.70
HashingVectorizer
0.83
0.57
0.40
0.47
Word2Vec
0.86
0.87
0.35
0.50
GloVe
SVM
0.90
0.79
0.69
0.73
CountVectorizer
0.92
0.91
0.67
0.77
TfidfVectorizer
0.92
0.90
0.67
0.77
HashingVectorizer
0.81
0.00
0.00
0.00
Word2Vec
0.85
0.80
0.31
0.44
GloVe
Random Forests
0.91
0.96
0.55
0.70
CountVectorizer
0.91
0.96
0.55
0.70
TfidfVectorizer
0.91
0.96
0.55
0.70
HashingVectorizer
0.86
0.72
0.47
0.57
Word2Vec
0.86
0.87
0.33
0.48
GloVe
Naive Bayes
0.91
0.94
0.56
0.70
CountVectorizer
0.89
1.00
0.46
0.63
TfidfVectorizer
BERT
0.94
0.96
0.73
0.81
BertTokenizer
DistillBert
0.92
0.91
0.71
0.80
DistillBertTokenizer
Roberta
0.93
0.88
0.75
0.81
RoBertaTokenizer
RoBerta + lora
0.91
0.86
0.73
0.79
RobertaTokenizer
Llama-2 (7B)
0.93
0.79
0.78
0.82
LlamaTokenizer
Llama-2 (7B) + lora
0.92
0.80
0.79
0.83
LlamaTokenizer
Table 2. Comparison of Fine-tuning time of different Transformer-based models
Method
Fine-tuning Epochs
Platform(GPU)
Fine-tuning time
BERT
30 epochs
Nvidia A4000(16GB)
176 mins
DistillBert
20 epochs
Nvidia A4000(16GB)
79 mins
RoBerta
10 epochs
Nvidia A4000(16GB)
54 mins
RoBerta + lora
10 epochs
Nvidia A4000(16GB)
21 mins
Llama-2 (7B)
3 epochs
Nvidia A100(80GB)
112 mins
Llama-2 (7B) + lora
3 epochs
Nvidia A100(80GB)
35 mins
niques for social good, specifically in combating anti-
Semitic hate speech online. Our comprehensive approach,
from data collection and annotation to model training and
evaluation, highlights the nuanced differences between var-
ious classification methods.
The
study
confirms
the
advanced
capability
of
transformer-based models in understanding and classifying
complex language patterns, outperforming traditional ma-
chine learning models. This finding aligns with the broader
trend in natural language processing and offers a promising
avenue for future research and practical applications in
online hate speech detection.
Nonetheless, the ethical implications, computational
costs, and interpretability issues associated with these ad-
vanced models warrant careful consideration. Future work
should focus on addressing these challenges, improving
model accessibility, and enhancing transparency without
sacrificing performance.
Ultimately, this research contributes to the ongoing ef-
fort to create safer online environments.
By leveraging
cutting-edge technology and rigorous methodologies, we
move closer to understanding and mitigating the spread of
hate speech on digital platforms.

--- Page 8 ---

References
[1] Jacob
Devlin,
Ming-Wei
Chang,
Kenton
Lee,
and
Kristina Toutanova.
Bert:
Pre-training of deep bidi-
rectional
transformers
for
language
understanding.
https://arxiv.org/abs/1810.04805, 2019. 1, 3, 4
[2] Victor Sanh,
Lysandre Debut,
Julien Chaumond,
and
Thomas Wolf. Distilbert, a distilled version of bert: smaller,
faster, cheaper and lighter. https://arxiv.org/abs/1910.01108,
2020. 1, 3, 4
[3] Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar
Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettle-
moyer, and Veselin Stoyanov. Roberta: A robustly optimized
bert pretraining approach. https://arxiv.org/abs/1907.11692,
2019. 1, 3, 4
[4] Hugo Touvron, Louis Martin, Kevin Stone, Peter Al-
bert, Amjad Almahairi, Yasmine Babaei, Nikolay Bash-
lykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhos-
ale, Dan Bikel, Lukas Blecher, Cristian Canton Ferrer,
Moya Chen, Guillem Cucurull, David Esiobu, Jude Fer-
nandes, Jeremy Fu, Wenyin Fu, Brian Fuller, Cynthia
Gao, Vedanuj Goswami, Naman Goyal, Anthony Hartshorn,
Saghar Hosseini, Rui Hou, Hakan Inan, Marcin Kardas, Vik-
tor Kerkez, Madian Khabsa, Isabel Kloumann, Artem Ko-
renev, Punit Singh Koura, Marie-Anne Lachaux, Thibaut
Lavril, Jenya Lee, Diana Liskovich, Yinghai Lu, Yuning
Mao, Xavier Martinet, Todor Mihaylov, Pushkar Mishra,
Igor Molybog, Yixin Nie, Andrew Poulton, Jeremy Reizen-
stein, Rashi Rungta, Kalyan Saladi, Alan Schelten, Ruan
Silva, Eric Michael Smith, Ranjan Subramanian, Xiao-
qing Ellen Tan, Binh Tang, Ross Taylor, Adina Williams,
Jian Xiang Kuan, Puxin Xu, Zheng Yan, Iliyan Zarov,
Yuchen Zhang, Angela Fan, Melanie Kambadur, Sharan
Narang, Aurelien Rodriguez, Robert Stojnic, Sergey Edunov,
and Thomas Scialom. Llama 2: Open foundation and fine-
tuned chat models. https://arxiv.org/abs/2307.09288, 2023.
1, 3, 4
[5] Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-
Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu
Chen. Lora: Low-rank adaptation of large language mod-
els. arXiv:2106.09685, 2021. 1, 3, 4
[6] Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg Corrado,
and Jeffrey Dean.
Distributed representations of words
and phrases and their compositionality.
arXiv preprint
arXiv:1310.4546. 2
[7] Jeffrey Pennington, Richard Socher, and Christopher Man-
ning. Glove: Global vectors for word representation. ACL
Anthology. 2
[8] Matthew E. Peters, Mark Neumann, Mohit Iyyer, Matt Gard-
ner, Christopher Clark, Kenton Lee, and Luke Zettlemoyer.
Deep contextualized word representations. arXiv Preprint
arXiv:1802.05365. 2
[9] Alec Radford, Karthik Narasimhan, Tim Salimans, and Ilya
Sutskever. Improving language understanding by generative
pre-training. Amazon.com. 2
[10] F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel,
B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss,
V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau,
M. Brucher, M. Perrot, and E. Duchesnay. Scikit-learn: Ma-
chine learning in python, 2011. 2
[11] William Warner and Julia Hirschberg. Detecting hate speech
on the world wide web. Association for Computational Lin-
guistics, Proceedings of the Second Workshop on Language
in Social Media, 2012. 2
[12] Thomas Davison, Dana Warmsley, Michael Macy, and Ing-
mar Weber. Automated hate speech detection and the prob-
lem of offensive language. International AAAI Conference
on Web and Social Media, 11, 2017. 2
[13] Hugo Haddad, Hala Mulki, Abdelmajid Oueslati, and
Mourad Gridach.
Benchmarking multi-class classification
algorithms for automatic hate speech detection.
Procedia
Computer Science, 159:685–694, 2019. 2
[14] Ziqi Zhang, Derek Robinson, and Jonathan Tepper.
De-
tecting hate speech on twitter using a convolution-gru based
deep neural network. In European Semantic Web Confer-
ence, pages 745–760. Springer, 2018. 2
[15] Pete Burnap and Matthew L Williams. Us and them: identi-
fying cyber hate on twitter across multiple protected charac-
teristics. EPJ Data Science, 5(1):11, 2016. 2
[16] Sepp Hochreiter and J¨urgen Schmidhuber. Long short-term
memory. Neural computation, 9(8):1735–1780, 1997. 2
[17] Yoon Kim. Convolutional neural networks for sentence clas-
sification. arXiv preprint arXiv:1408.5882, 2014. 2
[18] Kyunghyun Cho, Bart Van Merri¨enboer, Caglar Gulcehre,
Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, and
Yoshua Bengio. Learning phrase representations using rnn
encoder-decoder for statistical machine translation.
arXiv
preprint arXiv:1406.1078, 2014. 2
[19] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszko-
reit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia
Polosukhin. Attention is all you need. NeurIPS, 2017. 2
[20] Marzieh Mozafari, Reza Farahbakhsh, and Noel Crespi.
A bert-based transfer learning approach for hate speech
detection
in
online
social
media.
arXiv
preprint
arXiv:1910.12574, 2019. 3
[21] Lanqin Yuan, Tianyu Wang, Gabriela Ferraro, Hanna Suomi-
nen, and Marian-Andrei Rizoiu.
Transfer learning for
hate speech detection in social media.
arXiv preprint
arXiv:1906.03829, 2019. 3
[22] Xiaoqi Jiao, Yichun Yin, Lifeng Shang, Xin Jiang, Xiao
Chen, Linlin Li, Fang Wang, and Qun Liu. Tinybert: Distill-
ing bert for natural language understanding. arXiv preprint
arXiv:1909.10351, 2019. 3

```
