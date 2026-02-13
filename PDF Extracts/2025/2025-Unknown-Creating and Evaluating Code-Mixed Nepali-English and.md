---
title: "2025-Unknown-Creating and Evaluating Code-Mixed Nepali-English and - PDF Extract"
source_pdf: "2025-Unknown-Creating and Evaluating Code-Mixed Nepali-English and.pdf"
pages: 34
extracted_at: "2026-02-13T09:15:42.424364"
---

# PDF Extract: 2025-Unknown-Creating and Evaluating Code-Mixed Nepali-English and

**Source PDF:** 2025-Unknown-Creating and Evaluating Code-Mixed Nepali-English and.pdf
**Total Pages:** 34

---

## Content

```
--- Page 1 ---

Creating and Evaluating Code-Mixed
Nepali-English and Telugu-English Datasets for
Abusive Language Detection Using Traditional
and Deep Learning Models
Manish Pandey1, Nageshwar Prasad Yadav1, Mokshada Adduru1,
Sawan Rai1*
1*Dept. of Computer Science and Engineering, SRM University AP,
Guntur, 522502, AP, India.
*Corresponding author(s). E-mail(s): sawan.r@srmap.edu.in;
Contributing authors: manish pandey@srmap.edu.in;
nageshwar prasadyadav@srmap.edu.in;
mokshada adduru@srmap.edu.in;
Abstract
With the growing presence of multilingual users on social media, detecting
abusive language in code-mixed text has become increasingly challenging. Code-
mixed communication, where users seamlessly switch between English and their
native languages, poses difficulties for traditional abuse detection models, as
offensive content may be context-dependent or obscured by linguistic blending.
While abusive language detection has been extensively explored for high-resource
languages like English and Hindi, low-resource languages such as Telugu and
Nepali remain underrepresented, leaving gaps in effective moderation. In this
study, we introduce a novel, manually annotated dataset of 2 thousand Telugu-
English and 5 Nepali-English code-mixed comments, categorized as abusive and
non-abusive, collected from various social media platforms. The dataset under-
goes rigorous preprocessing before being evaluated across multiple Machine
Learning (ML), Deep Learning (DL), and Large Language Models (LLMs).
We experimented with models including Logistic Regression, Random Forest,
Support Vector Machines (SVM), Neural Networks (NN), LSTM, CNN, and
LLMs, optimizing their performance through hyperparameter tuning, and eval-
uate it using 10-fold cross-validation and statistical significance testing (t-test).
1
arXiv:2504.21026v1  [cs.CL]  23 Apr 2025

--- Page 2 ---

Our findings provide key insights into the challenges of detecting abusive lan-
guage in code-mixed settings and offer a comparative analysis of computational
approaches. This study contributes to advancing NLP for low-resource languages
by establishing benchmarks for abusive language detection in Telugu-English
and Nepali-English code-mixed text. The dataset and insights can aid in the
development of more robust moderation strategies for multilingual social media
environments.
Keywords: Code-Mixed NLP, Abusive Language Detection, Telugu-English,
Nepali-English, Machine Learning, Deep Learning, Large Language Models
1 Introduction
Social media has become an important space where people share opinions, connect
with others, and express themselves freely. However, with its growing popularity,
there has been an increase in online abuse and hate speech, making these platforms
more toxic and unsafe for many users. One major challenge in detecting abusive con-
tent—especially in countries like India and Nepal—is the use of code-mixing, where
users switch between languages like Telugu or Nepali and English within the same sen-
tence or post. This form of multilingual communication feels natural to many speakers,
but it creates difficulties for automated abuse detection systems[1].
Most tools designed to detect hate speech or offensive language are trained on
English text, and they often struggle when confronted with code-mixed content [2].
This is because code-mixed text is messy—it includes inconsistent spelling, gram-
mar from more than one language, and Romanized native words, which aren’t always
spelled consistently. For instance, someone might write “nuvvu chesina thing chala
worst,” mixing Romanized Telugu with English. Similarly, in Nepali-English, a user
might say “timro attitude dherai irritating xa,” combining Nepali syntax and vocab-
ulary with English words. A system trained only in English would fail to understand
the full meaning or even recognize that this could be abusive. These challenges make
it difficult for traditional models to accurately classify such content.
Moreover, there is a lack of properly labeled datasets for code-mixed languages.
Telugu-English and Nepali-English, in particular, lack sufficient labeled data for train-
ing and testing abuse detection models [3], [4]. Most available datasets are small,
unbalanced, or not annotated for abusive content at all. Without enough high-quality
examples, building effective models becomes difficult. Additionally, because code-
mixed language reflects cultural and social context, detecting abuse becomes even
more complex—it’s not only about the words used but also about when and how they
are used.
Another unique challenge with code-mixed text is the subjectivity of meaning in
different cultural and regional contexts as discussed by Authors in [5]. A phrase that
may seem neutral to someone unfamiliar with the culture could carry deeply offensive
or sarcastic undertones in certain communities. Abusers often exploit these linguistic
grey areas to bypass content moderation systems. This underscores the importance of
2

--- Page 3 ---

training models not just on code-mixed data, but on data that reflects the nuanced
language patterns, tone, and slang commonly used in Telugu-English or Nepali-English
online interactions [6].
Furthermore, transliteration adds another layer of complexity. Since Telugu and
Nepali are written in their native scripts (Telugu and Devanagari, respectively), users
often type them in Roman script on social media platforms. However, there are no
strict rules for transliterating these words [7]. The same word can be spelled differ-
ently by different users—for example, “chepparu,” “cheparu,” or “cheppaaru” could
all mean the same thing in Telugu. Similarly, “kasto” in Nepali might appear as
“kasto,” “kasto,” or even “casto,” depending on the user. These inconsistencies con-
fuse models that haven’t been trained on a wide variety of such forms, making basic
text preprocessing more challenging.
Despite the growing number of multilingual users online, limited focus has been
given to building datasets and tools for low-resource code-mixed languages. Most
research has centered around more widely studied combinations like Hindi-English
or Spanish-English [8]. Languages like Telugu and Nepali, on the other hand, receive
relatively little attention in NLP research, despite being spoken by millions. This
creates a gap in resources and tools available to these communities, reflecting a kind
of digital inequality—where some language groups are better protected from online
abuse simply because they are better represented in research and development.
To address this issue, our research introduces a manually annotated dataset con-
taining 5,000 Nepali-English and 2,000 Telugu-English code-mixed abusive comments.
We focused on collecting realistic, social media-style examples and carefully labeled
them for accuracy. We then evaluated several machine learning and deep learning mod-
els—including Logistic Regression, SVM, Random Forest, Neural Networks, LSTM,
and CNN—to determine which performed best. The models were tested using 10-fold
cross-validation, and we also used statistical tests (such as T-tests) to fairly compare
their performance.
This paper not only fills a gap in available data but also provides insight into how
different models handle code-mixed abuse detection. Our findings demonstrate that,
with the right dataset and proper evaluation, it is possible to build better tools for
moderating content in multilingual online communities. This is particularly important
for making the internet safer and more inclusive for speakers of low-resource languages
like Telugu and Nepali, who are often overlooked in mainstream AI and NLP research.
Furthermore, the findings emphasize the importance of not only relying on auto-
mated systems but also ensuring that the data used for training reflects the language
spoken by the target community. A more culturally and linguistically diverse dataset,
along with improved preprocessing techniques to handle transliteration variations
and mixed-language syntax, could lead to more robust models for detecting abusive
content. By addressing these challenges, we can work toward creating a safer online
environment for users who communicate in code-mixed languages like Telugu and
Nepali.
The rest of this paper is organized as follows. Section 2 discusses the notion of
code-mixing within the context of Nepali and Telugu languages, giving linguistic and
3

--- Page 4 ---

sociocultural background. Section 3 describes the process of generating code-mixed
datasets for these languages, including the approaches adopted for data collection,
sources of data, preprocessing, annotation strategies, an overview of the datasets, the
difficulties faced during the process, and the ethical considerations upheld. Section 4
discusses the properties and characteristics of the curated datasets. Section 5 reports
experiments using these corpora, after which Section 6 describes results found.
Section 7 outlines an in-depth discussion of results, and Section 8 offers an overview of
previous work relevant to code-mixing as well as multilingual NLP. Section 9 concludes
the paper, including a summary of major contributions along with future prospects.
2 Code-Mixing in Telugu and Nepali
Code-mixing, the practice of alternating between two or more languages within a
sentence or discourse, is a common phenomenon in multilingual societies. In countries
like Nepal and India, where multiple languages coexist, code-mixing has become an
essential feature of communication, particularly among younger generations. In these
regions, the integration of English with native languages such as Nepali and Telugu
is especially prevalent. Several studies have observed this trend across various media
and conversational contexts, highlighting how English is increasingly embedded within
informal and semi-formal discourse in these societies [9–11]. This section explores the
use of English within Nepali and Telugu, examining its role in modern communication,
the contexts in which it occurs, and the patterns of language switching. The impact
of code-mixing on language structure, expression, and comprehension will also be
discussed.
2.1 Code-Mixing in Nepali
Code-mixing between Nepali and English is common in Nepal, especially in urban areas
and among younger generations. English is frequently used in education, media, and
business, which leads Nepali speakers to blend English words and phrases into their
speech. This is particularly evident when discussing modern, technological, or global
topics. Code-mixing reflects the influence of global culture and serves as a practical
way to switch between languages for ease and efficiency.
Example of Nepali-English Code-Mixing:
Nepali-English: ”Timi le test paper complete garne hoina ra? I think you should
finish it soon.”
Translation: ”Aren’t you going to complete the test paper? I think you should
finish it soon.”
In this example, the sentence is in Nepali structure, but English words like ”test
paper” and ”finish” are used for efficiency and because there may be no direct
translation for these terms in Nepali.
2.2 Code-Mixing in Telugu
Telugu speakers also commonly mix English into their sentences, especially in infor-
mal settings or digital communication. Telugu sentence structure and grammar are
4

--- Page 5 ---

maintained, but English words are often inserted, particularly when discussing mod-
ern, technical, or pop culture topics. This is particularly true in urban environments,
where English is widely used in schools, workplaces, and social media.
Example of Telugu-English Code-Mixing:
Telugu-English: ”Me intloo camping ke Yantha mandhi waiting?”
Translation: ”How many people are waiting for camping at your house?”
This sentence follows Telugu grammar but incorporates English words like ”camp-
ing” and ”waiting”, demonstrating how English is blended into everyday Telugu
conversation for terms that are commonly used in the global context.
2.3 Code-Mixing Patterns
Code-mixing in both Nepali and Telugu generally occurs in two main forms:
intrasentential mixing and intersentential mixing.
Intrasentential mixing involves switching languages within a single sentence. For
example, parts of the sentence may follow one language’s grammar and sentence struc-
ture, while other parts incorporate words from another language. This type of mixing is
often considered the most complex due to the syntactic constraints it imposes [12, 13].
Inter-sentential mixing occurs when the switch happens at sentence boundaries.
One sentence might be entirely in one language, followed by another sentence in a dif-
ferent language. This form is typically observed among speakers with lower proficiency
in their second language [12, 14].
Both forms of code-mixing allow speakers to seamlessly navigate between lan-
guages, helping them express themselves more effectively. However, this can make
language processing more complex, as the language switch may obscure the intended
meaning or emotion behind the sentence.
3 Creating the Telugu-Nepali Code-Mixed Dataset
To develop effective abusive language detection models for low-resource, code-mixed
languages, well-curated datasets are imperative. This part explains the formation of
Romanized Telugu-English and Nepali-English datasets, i.e., collection, preprocessing,
annotation, challenges, and ethics.
3.1 Data Collection
To tackle the lack of accessible datasets involving abusive content in code-mixed low-
resource languages, this study focused on collecting Romanized Telugu-English and
Nepali-English text data from social media. The aim was to build a diverse and real-
istic dataset to help identify abusive language in naturally occurring code-switched
conversations.
3.2 Data Sources
Comments were manually gathered from platforms like Twitter, YouTube, and Insta-
gram. These platforms were chosen for their large volumes of user-generated, informal,
and code-mixed content. The dataset includes both abusive and non-abusive comments
5

--- Page 6 ---

from various topics—politics, entertainment, and everyday life—ensuring a wide range
of linguistic tones and styles.
3.3 Preprocessing Steps
Prior to analysis, the data went through several systematic cleaning processes to cor-
rect quality and consistency. First, all texts were made lowercase to prevent duplication
due to case sensitivity. The punctuation marks were stripped off, and tokenization was
carried out to divide the sentences into separate words or symbols to facilitate easier
processing. Emojis were converted to their textual equivalents, and numerical values
were spelled out as words to ensure uniformity of format across the dataset. Spe-
cial characters and extraneous symbols were also removed, and the cleaned text was
then converted to numerical format (vectorized) to facilitate smooth input to machine
learning models.
3.4 Annotation Process
Comments were manually annotated by individuals fluent in English and either Telugu
or Nepali. They were classified into two categories: Abusive: Containing rude, disre-
spectful, or offensive language, even if not explicitly promoting hate. Non-abusive:
Free from any offensive, harmful, or inappropriate content. Annotators were guided
to consider tone, cultural context, sarcasm, and linguistic variation. In cases of dis-
agreement, annotations were discussed and finalized collectively to maintain labeling
consistency.
3.5 Dataset Overview
Telugu-English Dataset contains 2,000 comments in total — 1,200 labeled as abu-
sive and 800 as non-abusive, showing moderate class imbalance. while Nepali-English
Dataset includes 5,000 comments — 2,632 abusive and 2,368 non-abusive, offering a
more balanced distribution. These datasets offer valuable resources for building models
that address the unique challenges of code-mixed abusive content detection.
3.6 Challenges Faced
A key difficulty was the limited availability of Romanized content; most online data
exists in native scripts, especially for Telugu and Nepali. Since our focus was on
Romanized text, finding relevant content required extensive manual filtering.
Another issue was the inconsistency in Romanization — the same word could be
spelled in several ways due to differences in pronunciation or personal habits. This
made preprocessing more complex.
The nature of code-mixing added additional challenges. Comments often blended
English with native language words, even within a single term. This complicated both
the preprocessing and the annotation phases. Sarcasm, slang, and cultural nuances
made it harder to categorize comments as abusive or not, often requiring careful
judgment.
6

--- Page 7 ---

Lastly, the imbalance in class distribution—especially for Telugu—necessitated
focused collection efforts to ensure abusive content was adequately represented without
skewing the dataset.
3.7 Ethical Practices
All data used was publicly available and collected in line with platform policies, such
as Twitter’s Developer Agreement. No personal or sensitive information (like user-
names or timestamps) was retained, preserving user privacy. The dataset is solely for
academic and research purposes, aimed at contributing to the safe and ethical devel-
opment of abusive language detection systems. No text was fabricated, altered, or
misused during this study.
4 Analysis of Datasets
This section provides an in-depth breakdown of the code-mixed Nepali-English and
Telugu-English datasets. It includes data composition, the level of code-mixing using
the Code-Mixing Index (CMI), and token distribution language-wise to bring out the
linguistic patterns and diversity in the datasets.
Table 1 Data Composition Overview
Feature
Telugu-English
Nepali-English
Total Comments
2,000
5,000
Abusive Comments
1,200
2,632
Non-Abusive Comments
800
2,368
Total Tokens
18,551
44,902
Average Tokens per Sentence
9.28
8.98
Domain Diversity
High
High
Romanized Language Mix
Telugu + English
Nepali + English
Abusive/Non-Abusive Ratio
60:40
∼53:47
The Telugu-English dataset consists of 2,000 code-mixed comments. About 60%
are abusive, and the rest are non-abusive. The language used is mostly informal,
drawn from social media platforms, showcasing a diverse set of domains like politics,
entertainment, and daily life. The comments are written using Roman script and
contain tokens from both English and Telugu languages.
The Nepali-English dataset contains 5,000 code-mixed comments with a slightly
more balanced 53:47 abusive to non-abusive ratio. The data reflects natural online
usage, with Romanized Nepali intermingled with English, especially in technology,
current affairs, and youth conversations.
7

--- Page 8 ---

4.1 Code-Mixing Statistics
To measure the extent of code-mixing in the datasets, we calculated the Code-Mixing
Index (CMI), a commonly used metric in linguistic analysis. CMI quantifies the level
of mixing between multiple languages within a sentence or utterance. It is defined as:
CMI = 100 ×

1 −max(wi)
n −u

(1)
Where:
• n = Total number of tokens in the comment
• u = Number of language-independent tokens (e.g., punctuation, symbols)
• wi = Number of tokens in language i
• max(wi) = Number of tokens in the most dominant language
Higher CMI values indicate greater levels of code-mixing, while a value of 0 corre-
sponds to monolingual content. This metric was introduced by Gamb¨ack and Das [15]
and has been widely adopted in code-mixed language research [16].
The Nepali-English dataset demonstrates a moderate degree of code-mixing.
English tokens frequently occur within otherwise Nepali syntactic structures, espe-
cially in domains such as pop culture, online discourse, and education. These borrowed
words blend into everyday usage, reflecting a natural form of code-switching in digital
conversations.
Fig. 1 Distribution of Code-Mixing Index (CMI) for Nepali-English dataset.
Figure 2 shows the distribution of CMI scores in a Telugu-English dataset con-
taining Romanized comments. Most of the comments are concentrated at a CMI score
of 0, indicating that they are treated as monolingual. This is likely because Telugu
words written in the Roman script are not being identified as Telugu by the current
8

--- Page 9 ---

method, causing them to be classified as English. As a result, the true extent of code-
mixing in the dataset is likely underrepresented, suggesting a need for better handling
of Romanized Telugu in the analysis.
Fig. 2 Distribution of Code-Mixing Index (CMI) for Telugu-English dataset.
4.2 Language distribution
This section provides an overview of the distribution of tokens based on their lan-
guage labels. This analysis helps us understand the syntactic nature and code-mixing
dynamics of both the Telugu-English and Nepali-English datasets.
Table 2 Comment-wise Language Distribution in Telugu-English and
Nepali-English Datasets
Language Category
Telugu-English
Nepali-English
Count
%
Count
%
Mostly Native (Telugu/Nepali)
1,917
95.85
850
34.0
Code-mixed
80
4.00
820
32.8
Universal / Other
3
0.15
50
2.0
Total
2,000
100.0
2,500
100.0
9

--- Page 10 ---

5 Experiments on the Dataset
Fig. 3 Workflow of Experimental setup
Figure
3 describes the complete workflow used for abusive language classification
in code-mixed Nepali and Telugu corpora. The process starts with Data Collection,
wherein the user-created content is harvested from social media websites. It is then
followed by Annotation, where human annotators tag each sample as abusive or non-
abusive to form a supervised learning corpus. Then comes the Preprocessing phase
where the text is cleaned from noise like special characters, emojis, and duplicate sym-
bols and linguistic patterns are normalized. Following this, the data passes through
mBERT Tokenization and Embedding Generation, which employs multilingual BERT
to tokenize the input and produce contextual embeddings specifically for every sen-
tence. These embeddings are input into the Model Training step, wherein several
machine learning and deep learning models are trained on the preprocessed data. The
trained models are then evaluated using default classification metrics like Precision,
10

--- Page 11 ---

Recall, F1-Score, and Accuracy. Lastly, Result Analysis and Model Comparison is
done, involving statistical testing, to identify the best model for the task and to make
meaningful conclusions from the experimental results.
5.1 Preprocessing
Due to the inherent linguistic differences and unique difficulties that each lan-
guage posed, separate preprocessing pipelines were formulated to efficiently clean,
normalize, and ready the text for downstream analysis and model training. This sub-
section explains the preprocessing steps adopted for the gathered Telugu-English and
Nepali-English code-mixed data.
5.1.1 Telugu Text Preprocessing
The Telugu text preprocessing starts with Unicode normalization to deal with any
encoding inconsistency. The text is normalized in the NFKC form so that charac-
ters are represented consistently. The text is then cleaned after normalization such
that non-Telugu characters, special symbols, emojis, and unnecessary punctuation are
eliminated from the text using regular expressions. Only Telugu characters in the Uni-
code range (\u0C00--\u0C7F) are preserved, and additional spaces, tabs, and newline
characters are removed.
While Telugu is not case-sensitive, any Latin-script text (e.g., foreign words,
hashtags) is changed to lowercase for consistency. The text is then tokenized using
the mBERT tokenizer, which breaks the text into subword units and produces
768-dimensional embeddings for each token. This produces high-dimensional feature
vectors that are passed into downstream classification models.
Stopwords are also filtered out of the text so that frequently occurring words
with minimal semantic meaning are not able to influence the classification. The last
preprocessed text is then available for feature extraction and training of models.
5.1.2 Nepali Text Preprocessing
The preprocessing of Nepali text is similar to that of Telugu, beginning with Unicode
normalization using the NFKC form in order to ensure uniform character encoding.
Non-Nepali characters, unwanted punctuation, emoticons, and non-task-relevant num-
bers are removed from the text. Only Nepali characters within the Unicode range
(\u0900--\u097F) are retained, and additional spaces, tabs, and newline characters
are eliminated using regular expressions.
Since there is no casing involved in Nepali text, Latin-script words such as foreign
names or hashtags are converted to lowercase to maintain consistency. The prepro-
cessed Nepali text is then tokenized using the mBERT tokenizer, which segments the
text into subword pieces and generates 768-dimensional embeddings for each token.
These embeddings are subsequently used as input features by the classification models.
As part of preprocessing, stopword removal is also performed to eliminate fre-
quently occurring words such as “the,” “is,” or “in,” which do not carry significant
semantic content for the classification task. The preprocessed text is then ready for
analysis and model training.
11

--- Page 12 ---

5.2 Model Training
Here, we present the machine learning models selected for the task of classification,
giving an idea of the training methods and strategies employed to identify abusive
language successfully.
5.2.1 Logistic Regression
Logistic Regression is a straightforward but powerful binary classification model. It
is most useful when there is a linear relationship between features and the target
variable, and therefore can be a suitable option for text classification problems when
the relationships are not very complex. The model is trained using 768-dimensional
mBERT embeddings, which are numerical vectors that capture the semantic meaning
of the text. These embeddings are then fed into the model so that it can predict
whether the text is abusive or not based on the coefficients it learns during training
[17] [6].
5.2.2 SVM
SVM is employed for its capacity to deal with high-dimensional spaces well, and it is
suitable for text classification where the input data (embeddings) is of high dimension.
SVM operates by determining the best hyperplane that can divide the two classes. The
768-dimensional mBERT embeddings are input as features to the model, and SVM
utilizes these to calculate the best boundary that separates abusive from non-abusive
text [18].
5.2.3 Random Forest
Random Forest is an ensemble learning technique that functions by creating several
decision trees, enhancing classification accuracy and preventing overfitting [19]. It is
particularly effective when there are intricate, non-linear patterns in the data. The
model takes 768-dimensional mBERT embeddings as input, where the embedding of
each text is used as a feature for the decision trees. The trees’ ensemble votes as a
whole to determine whether the text is abusive or not.
5.2.4 Neural Network
The Neural Network (MLP) is employed because it can represent complex, non-linear
relationships within the data. This is particularly beneficial in text classification,
where word and context relationships are not necessarily linear. The 768-dimensional
mBERT embeddings are fed as input features to the network. The network feeds these
embeddings through several layers, learning complex patterns to classify the text as
abusive or non-abusive.
5.2.5 CNN
CNNs are good at pulling out local patterns from data and are, therefore, well-suited
for tasks where local dependencies (such as word sequences) are critical, e.g., text
12

--- Page 13 ---

classification. The mBERT 768-dimensional embeddings are input to the CNN model,
with the convolutional layers performing filtering to pick up on salient local patterns
(e.g., particular word combinations or n-grams) and then labeling the text as abusive
or not abusive based on these features.
5.2.6 LSTM
LSTM is used for sequential data, where the relationships between elements depend
on the sequence and context. It is particularly effective in capturing long-range
dependencies in text, making it ideal for understanding context in sentences. The 768-
dimensional mBERT embeddings are fed sequentially into the LSTM, which processes
the embeddings and captures temporal relationships between words to classify the
text as abusive or non-abusive.
5.2.7 LLM
The methodology entails a systematic investigation of hyperparameter setups to assess
the impact of learning rate and training time on the performance of transformer-based
classifiers. Several fine-tuning experiments were performed with different learning rates
(1e-5, 3e-5, and 5e-5) for different numbers of training epochs. Model performance was
measured in terms of classification accuracy in order to determine optimal setups and
to investigate training stability [20]. This perspective facilitates a better understand-
ing of how fine-tuning dynamics affect performance, particularly in low-resource and
cross-lingual scenarios, and points to the necessity of selecting hyperparameters with
caution—specifically learning rate adjustment—to achieve strong model performance.
6 Results
This section presents a comparative discussion of the model performance on both
Nepali and Telugu datasets, analyzing differences in results and how linguistic
variations affect classification accuracy.
6.1 Nepali Dataset
This sub-section provides the results of the evaluation of the machine learning models
used on the Nepali dataset, showing their performance in identifying abusive language
in Nepali-English code-mixed text.
13

--- Page 14 ---

6.1.1 Result on Logistic Regression
Fig. 4
F1-Score Trends for Logistic Regression
The Logistic Regression model with lbfgs solver produced the highest weighted
F1-score of 0.723 (accuracy: 72.3%) with the following parameters: C=0.01,
penalty=’l2’, class weight=’balanced’, and max iter=1000. Lower regularization
strength (C=0.01) performed consistently better than higher values (C=0.1, C=1), with
F1-scores falling to 0.702 and 0.685, respectively, showing weaker regularization better
handles bias-variance trade-offs for this dataset. The lbfgs solver beat saga by a little
(F1=0.723 vs. 0.722 at C=0.01), the probable reason for its efficiency at L2 penalty.
Class weighting (balanced) guaranteed unbiased performance, with the minority class
(1) F1-scores being no more than 2% lower than the majority class (0). Doubling
max iter to 5000 produced identical results to the 1000 iterations, vindicating the
efficiency of convergence. These results point out the importance of moderate regular-
ization (C=0.01) and solver choice (lbfgs) in the optimization of logistic regression
in well-balanced classification problems. .
14

--- Page 15 ---

6.1.2 Result on SVM Model
Fig. 5 F1-Score Trends for SVM
The SVM model with RBF kernel and C=1 had the best weighted F1-score of
0.724 (accuracy: 72.6%), showing the radial basis function’s ability to capture non-
linear decision boundaries when combined with moderate regularization. Lower C
values (e.g., 0.01) for all kernels resulted in extreme underfitting, especially for class
1, with F1-scores close to zero, indicating poor generalization. Increasing C enhanced
performance, but very high values (C=1 for sigmoid kernel) compromised results, indi-
cating kernel-dependent sensitivity to regularization. The poly kernel (C=1) was
second-best (F1=0.702), with higher precision for class 1 (78.5%), and the sigmoid
kernel reached a peak at C=0.1 (F1=0.692), reflecting limited applicability to the
dataset. Of particular interest, low C values showed class 0 recall bias (up to 99.6%),
well in excess of class 1, pointing to class imbalance issues, which were reduced by
increasing C values in RBF and poly setups. These findings strongly support the need
for the selection of kernels and regularization parameter tuning in SVMs, with the
RBF kernel (C=1, gamma=’scale’) being the best setup for balanced performance on
this task.
15

--- Page 16 ---

6.1.3 Result on Random Forest
Fig. 6 F1-Score Trends for Random Forest
The Random Forest model with 300 trees and disabled bootstrap sampling achieved
the highest weighted F1-score of 0.697 (accuracy: 70.1%), using the following param-
eters: n estimators=300, bootstrap=False, max depth=20,
max features=’sqrt’, min samples leaf=2, min samples split=5,
class weight=None. Disabling bootstrap sampling slightly improved performance
when compared to bootstrapped configurations (e.g., 300 trees with no bootstrap vs.
bootstrap: F1=0.697 vs. 0.693), likely due to reduced overfitting by utilizing the full
dataset for tree construction. Increasing the number of trees beyond 300 (e.g., 500 or
700) resulted in a degradation of performance (F1=0.689–0.697), suggesting dimin-
ishing returns with larger ensembles. Class balancing (class weight=’balanced’)
marginally improved the recall for the minority class (class 1), but at the cost of
reduced overall precision, indicating minimal impact from class imbalance. Fixed
hyperparameters such as max depth=20 and lower values for min samples leaf and
min samples split (2 and 5, respectively) provided sufficient model complexity
without overfitting, as performance remained stable across configurations. These
results highlight the importance of optimizing bootstrap sampling and the number of
trees, with smaller ensembles (300 trees) and full dataset utilization offering the best
trade-off between bias and variance for this task.
16

--- Page 17 ---

6.1.4 Result on Neural Network
Fig. 7 F1-Score Trends for Neural Network with Batch size: 64
Fig. 8 F1-Score Trends for Neural Network with Batch size: 128
The Neural Network tanh activation function and Adam optimizer achieved
the highest weighted F1-score of 0.736 (accuracy: 73.6%), having the following
parameters:
hidden layer sizes=(512, 256), max iter=500, batch size=64,
alpha=0.0001, learning rate init=0.001. Deeper architectures having 512-256
17

--- Page 18 ---

layers outperformed shallower networks with 128-64-32 layers, suggesting enhanced
hierarchical feature extraction. The tanh activation function consistently surpassed
ReLU in larger models (e.g., 73.6% vs. 71.9% accuracy), likely due to its zero-
centered output stabilizing gradients. Smaller batch sizes (i.e., batch size=64),
paired with moderate learning rates (0.001), improved convergence, while higher rates
(0.005) destabilized training, reducing F1-scores by 2–4%. Lower L2 regularization
(alpha=0.0001) outperformed stronger regularization (alpha=0.0005), indicating
minimal overfitting despite model complexity. Extending training iterations beyond
500 (max iter=700) yielded marginal gains, as early stopping effectively prevented
overfitting. These results underscore the synergy of architectural depth, activation
choice (tanh), and adaptive optimization (Adam) in balancing feature learning and
generalization for optimal performance.
6.1.5 Result on CNN
Fig. 9 F1-Score Trends for CNN
The highest-scoring model has a weighted F1-score of 0.7340 (accuracy: 73.5%)
using the following parameters: out channels=64, kernel size=5, dropout rate=0.3,
learning rate=0.001, and batch size=32. This setting implies that smaller networks
(64 channels) with an intermediate kernel size (5) and a more elevated learning rate
(0.001) work well to equilibrate feature extraction and generalization. Interestingly,
growing out channels to 128 or 256 tended to result in incremental or diminished
performance, suggesting diminishing returns for greater models. kernel size=3 or 7
models were inconsistent, but kernel size 5 consistently produced competitive results.
Reduced learning rates (0.0001) combined with lower batch sizes (16) sometimes
offered improved stability but at the expense of the F1 score, and increased learning
rates (0.001) combined with batch size 32 had improved performance combined with
18

--- Page 19 ---

optimal kernel sizes. Dropout (0.3) held steady, implying its usefulness in avoiding
overfitting without learning detriment. Across the board, the relationship among ker-
nel size, learning rate, and batch size had considerable effects on model performance,
the best combination prioritizing moderate complexity and adaptive learning.
6.1.6 Result on LSTM Model
Fig. 10 F1-Score Trends for LSTM
The LSTM model analysis indicates that architectural complexity and parame-
ter tuning have a strong impact on performance, with the best weighted aver-
age F1-score (0.7301) and accuracy (73.1%) being obtained by the model
with hidden dim=128, num layers=2, bidirectional=True, dropout=0.2, learn-
ing rate=0.0001, and batch size=32. Bidirectional LSTMs with two layers performed
better than more basic architectures throughout, demonstrating their capacity to
capture contextual dependencies in sequential data. Smaller dropout rates (0.2–0.3)
equilibrated regularization and model capacity, while higher rates (e.g., 0.5) compro-
mised performance by as much as 2.3% F1, presumably from too much regularization.
Lower learning rates (learning rate=0.0001) improved stability on deeper archi-
tectures, while higher rates (0.001) produced unstable convergence, especially in
bidirectional models. Higher hidden dimensions (hidden dim=128 compared to 32/64)
boosted F1 by 4–6%, highlighting their ability to capture complex patterns. Although
smaller batch sizes (batch size=16) slightly favored single-layer models, bidirec-
tional architectures alleviated this disparity, sustaining strong performance with
batch sizes of 32. The poorest performers (F1 less than 0.66), including models
with hidden dim=32 and high dropout (0.5), were plagued by low capacity and
over-regularization. These results highlight the need to balance architectural depth,
19

--- Page 20 ---

regularization, and learning dynamics to maximize LSTM performance in sequential
classification tasks.
6.1.7 Result on LLM
Analysis showed critical dependencies among learning rates, training length, and
model performance, with the best configuration (1e-5 learning rate, 4 epochs)
achieving 78.3% accuracy, highlighting the effectiveness of smaller learning rates for
stable fine-tuning. Models with higher rates showed extreme degradation: 3e-5 demon-
strated volatility (peak 71.2% at 3 epochs, decreasing to 65.2% by epoch 4), whereas
5e-5 catastrophically failed (53.9% for all epochs), showing optimization instability.
Interestingly, longer training benefited only the 1e-5 setting (73.6% →78.3% after 2–4
epochs), while higher rates plateaued or declined, indicating overfitting or unstable
gradient updates. These findings highlight the importance of careful hyperparame-
ter tuning, especially learning rate adjustment, for transformer-based classifiers, with
lower rates (1e-5) being most resilient to extended training. The dramatic 24.4% accu-
racy gap between optimal (78.3%) and worst (53.9%) settings sheds light on the biased
effect of parameter tuning versus architectural design in low-resource settings, calling
for principled validation of learning dynamics under cross-lingual transfer tasks.
6.2 Telegu Dataset
in this sub-section, we present the performance results of the machine learning models
over the Telugu dataset, with emphasis on their capacity to identify abusive language
in Telugu-English code-mixed text.
6.2.1 Logistic Regression
Fig. 11 F1-Score Trends for Logistic Regression
20

--- Page 21 ---

The models show that lower regularization strength (C=0.01) produces the best
performance, with a weighted F1-score of 0.8374 and 83.75% accuracy across
all solvers (lbfgs, saga) and iterations (max iter=1000 or 5000). This implies good
generalizability with balanced class weights, which will probably counteract over-
fitting even with the weaker penalty. On the other hand, increased regularization
(C=1) decreases performance (F1: 0.7948, accuracy: 79.5%), implying underfitting.
Of note, solver choice and max iter had minimal effect for C=0.01 since all
settings with these parameters converged to the same outcomes, suggesting opti-
mization stability. The optimal model is obtained with C=0.01, penalty=’l2’,
class weight=’balanced’, solver=’lbfgs’ (or saga), and max iter=1000, which
produces stable precision (0.8608) and recall (0.8644) for the majority class while pro-
viding balanced performance for the minority class (F1: 0.8012). This demonstrates
the efficacy of moderate regularization and class balancing for imbalanced datasets.
6.2.2 Result on SVM
Fig. 12 F1-Score Trends for SVM
Experiments compared SVM models with different kernels and strengths of regular-
ization (C) for binary classification. Best-performing SVM (RBF Kernel, C=1)
returned an 83.25% accuracy and a 82.86% weighted F1-score under parameters
such as kernel=’rbf’, C=1, and gamma=’scale’. Evidence showed that RBF kernel
tended to outperform polynomial (poly) and sigmoid kernels across instances, presum-
ably by capturing complex non-linear decision surfaces without overfitting. Stronger
regularization strength (C=1) enhanced performance in all kernels, striking the margin
flexibility vs. generalization balance, while lower strengths (C=0.01 or 0.1) resulted in
underfitting, as observed in models that predicted only the most frequent class (e.g.,
21

--- Page 22 ---

poly and sigmoid with C=0.01: F1 ≤43.79%). The sigmoid kernel performed reason-
ably well (C=1: F1=81.04%), but was challenged by class imbalance relative to RBF.
Of particular note, the polynomial kernel had low precision for the minority class
(poly, C=1: precision=90.38% for class 0 but recall=28.66%), which means overfit-
ting to certain features. The success of the best model highlights the value of kernel
choice and regularization: the RBF kernel’s flexibility with respect to data geometry,
along with C=1, best traded off margin violations against discriminative power. These
results emphasize that SVMs with RBF kernels and balanced regularization are stable
for imbalanced classification problems when tuned to avoid overfitting.
6.2.3 Result on Random Forest
Fig. 13 F1-Score Trends for Random Forest
The experiments compared Random Forest models with different ensemble sizes
(n estimators), bootstrapping approaches, and class-balancing methods for a binary
classification problem. The best-performing model, Random Forest (500 Trees,
No
Bootstrap), had an accuracy
of
77.50% and a weighted
F1-score
76.31% using parameter such as n estimators=500, bootstrap=False, max depth=20,
max features=’sqrt’, min samples leaf=2,
min samples split=5, and class weight=None. Analysis showed that bootstrapping
was disabled (bootstrap=False) consistently to always enhance performance in
all ensemble sizes, presumably from less bias caused by using the entire dataset
in each tree. Larger ensembles (n estimators=500) slightly performed better than
smaller ones (n estimators=300/700), indicating a balance between variance reduc-
tion and computational complexity. Class weighting (class weight=’balanced’)
compromised F1-scores (e.g., 500 Trees,
Bootstrap Balanced:
F1=72.85%
vs.
500 Trees, No Bootstrap:
F1=76.31%),
22

--- Page 23 ---

demonstrating the use of default class weighting adequately addressed imbal-
ance without penalizing the majority class too heavily. The max depth=20 and
max features=’sqrt’ settings offered suitable complexity and feature selection
diversity, but using deeper trees could result in underfitting. Pertinently, models
without bootstrapping had better recall for the minority class (e.g., 500 Trees, No
Bootstrap: recall=54.88% for class 0 vs. 500 Trees, Bootstrap: recall=52.44%),
highlighting their ability to effectively identify rare patterns. These results high-
light the significance of ensemble size, bootstrapping approach, and conservative class
weighting in optimizing Random Forests for imbalanced classification problems.
6.2.4 Result on Neural Network
Fig. 14 F1-Score Trends for Neural Network with Batch size: 64
The comparison of neural network models by weighted average F1-score provides
key insights into parameter optimization. Models with deeper architectures (e.g.,
(256, 128, 64) hidden layers) tended to perform better than shallower ones, with
greater stability and generalization. The ReLU activation function consistently
provided better performance (weighted F1: up to 0.8795) than tanh, presumably
because it avoids vanishing gradients. Smaller learning rates (0.001 vs. 0.005)
and adaptive learning rates enhanced convergence, whereas smaller batch sizes (64
vs. 128) sometimes minimized overfitting but at the expense of training stability.
The highest performing model had a weighted F1-score of 0.8795 and accu-
racy of 84.25% with the following parameters: hidden layer sizes=(256, 128,
64), max iter=500, batch size=128, alpha=0.0005, learning rate init=0.001,
activation=relu, solver=adam. Interestingly, raising max iter above 500 did not
23

--- Page 24 ---

Fig. 15 F1-Score Trends for Neural Network with Batch size: 128
result in meaningful improvements, indicating early convergence. These results empha-
size the interaction between regularization (through alpha=0.0005) and architectural
depth for maximizing discriminative ability in imbalanced classification problems.
6.2.5 Result on CNN
Fig. 16 F1-Score Trends for CNN
24

--- Page 25 ---

The experiments tested CNN models with different hyperparameters for a binary clas-
sification problem. The best model, yielded an accuracy of 84.00% and a weighted
F1-score of 84.05% using parameters such as 128 out channels, kernel size=7,
dropout rate=0.3, learning rate=0.0001, and batch size=32. Analysis indicated
that bigger kernel sizes (e.g., 7 vs. 3/5) enhanced feature extraction by detecting
larger contextual patterns, while moderate-sized out channels (128) balanced model
complexity and generalization better than smaller (64) or bigger (256) sizes. Lower
learning rates (0.0001) with dropout =0.3 increased stability and minimized overfit-
ting, especially in deeper architectures. Interestingly, batch size=32 performed better
than batch size=16 in top models, indicating better gradient generalization. Increas-
ing out channels to 256 sometimes enhanced performance (e.g., F1=82.53%), but
at the expense of potential overfitting, as evidenced by irregular performance across
kernel sizes. Models with kernel size=5 also competed (e.g., F1=83.27%), but ker-
nel size=7 consistently excelled, demonstrating the effectiveness of this setting for
contextual learning. These results reinforce the need to combine kernel size, chan-
nel depth, and learning dynamics, with the best setup operating on the cross-road of
receptive field breadth, regularization, and training stability.
6.2.6 Result on LSTM
Fig. 17 F1-Score Trends for LSTM
The tests compared LSTM models with different hyperparameters to select the best
one for a binary classification problem. The top model, had an accuracy of 84.25%
and a weighted F1-score of 84.09%, which far exceeded other configurations. Its
configuration is a hidden dimension of 128, a single-layer unidirectional architecture,
dropout of 0.3, learning rate of 0.001, and batch size of 16. Analysis showed that
25

--- Page 26 ---

increased hidden dimensions (128 compared to 32/64) enhanced model capacity, allow-
ing more detailed feature extraction without overfitting, especially in conjunction with
moderate dropout (0.3). Bidirectional architectures were below par compared to uni-
directional models. Bidirectional architectures reached 83.06% F1 compared to 84.09%
for the unidirectional version), indicating unidirectional context was adequate for the
task. Increased learning rates (0.001) with regularization (dropout=0.3) improved
convergence, whereas smaller batch sizes (16 vs. 32) probably helped to increase
gradient accuracy during training. Models with too much dropout (0.5) or reduced
learning rates (0.0001) showed lower F1-scores from underfitting or slow convergence.
Surprisingly, deeper architectures (2 layers) did not always beat single-layer models,
suggesting diminishing returns from increased complexity. These results underscore
the necessity to balance model capacity, regularization, and training dynamics, where
the best combination accomplishes robust generalization by virtue of a synergistic
interaction among hyperparameters.
6.2.7 Result on LLM
The comparative model analysis with different hyperparameters (learning rate and
epochs) for a binary classification problem (num labels=2) demonstrates different
performance patterns. Models trained with a learning rate of 1e-5 demonstrated incre-
mental increases in accuracy as epochs were increased: 76.25% (2 epochs), 76.75% (3
epochs), and 77.25% (4 epochs), indicating stable but incremental learning. Still, the
highest accuracy (80.50%) was obtained by the model learning with a learning rate
of 3e-5 and 3 epochs, suggesting the best balance between the speed of learning and
the training time. It should be noted that the increase in epochs beyond 3 for this
learning rate resulted in the decrease of accuracy (74.25% at 4 epochs), presumably
because of overfitting. On the other hand, higher learning rate models (5e-5) always
performed poorly (57.75% accuracy for all epochs), pointing towards the destabilizing
influence of high learning rates. The top-performing model with (learning rate=3e-5,
epochs=3), yielded an accuracy of 80.50%, showing that sensible learning rates cou-
pled with careful epoch choice are paramount in achieving optimal performance in
this task. The results outlined above highlight key differences among the evaluated
models, which are further examined and contextualized in the subsequent discussion.
7 Discussion
Through paired t-tests and performance measures, we compare the efficacy of conven-
tional, deep learning, and large language models (LLMs) before scrutinizing crucial
threats to validity that can affect the interpretation of findings. This part offers an
in-depth assessment of model performance on Nepali and Telugu code-mixed datasets
by integrating statistical analysis, comparative measures, and an understanding of the
relative strength and weaknesses of each methodology.
7.1 Discussion on Nepali Dataset
The statistical analysis of model performance provides several key findings. The LLM
showed undisputed dominance over all other models, displaying statistically
26

--- Page 27 ---

Table 3 Pairwise t-Test with p-values for Model Comparison on Nepali Dataset
LR
SVM
RF
NN
CNN
LSTM
LLM
LR
—
< (0.975)
> (0.001)
> (0.002)
> (0.078)
> (0.257)
< (0.001)
SVM
> (0.975)
—
> (0.003)
> (0.000)
> (0.045)
> (0.093)
< (0.001)
RF
< (0.001)
< (0.003)
—
> (0.369)
< (0.687)
< (0.009)
< (0.001)
NN
< (0.002)
< (0.000)
< (0.369)
—
< (0.373)
< (0.001)
< (0.001)
CNN
< (0.078)
< (0.045)
> (0.687)
> (0.373)
—
< (0.107)
< (0.001)
LSTM
< (0.257)
< (0.093)
> (0.009)
> (0.001)
> (0.107)
—
< (0.001)
LLM
> (0.001)
> (0.001)
> (0.001)
> (0.001)
> (0.001)
> (0.001)
—
significant differences (p < 0.0001) in paired comparisons with conventional machine
learning (e.g., Logistic Regression, SVM) and deep learning models (CNN, LSTM).
This emphasizes the revolutionary potential of large language models for sentiment
analysis tasks. Among classical models, Random Forest performed better than
Logistic Regression (p=0.001) and Neural Networks performed better than
Logistic Regression (p=0.002), although SVM had no significant benefit over Logis-
tic Regression (p=0.975), indicating minimal value of linear kernel-based methods for
this task. Interestingly, SVM performed better than Random Forest (p=0.003),
indicating subtle performance differences among ensemble methods. In deep learning
comparisons, LSTMs had an edge over Random Forests (p=0.009) and Neural
Networks (p=0.0007), but CNNs did not have a significant edge over LSTMs
(p=0.107), suggesting context-dependent effectiveness of recurrent over convolutional
architectures.
Surprisingly, CNNs had no significant advantage over Random Forests
(p=0.687), contradicting assumptions regarding automatic superiority of deep learn-
ing for embedded text representations. The consistent superiority of the LLM
(p < 0.0001 in all comparisons) is consistent with its ability to draw on contextual
patterns of semantics, surpassing both feature-engineered conventional models and
task-specialized neural designs. The findings highlight the need to match model type
to data complexity, with the LLM becoming a model for high-stakes sentiment analysis
tasks.
7.2 Discussion on Telugu Dataset
The statistical contrast of model performances through paired t-tests (α = 0.05)
following 10-fold cross-validation indicates clear hierarchical trends. The Large
Language Model (LLM) showed unambiguous superiority by being statistically
significantly better than all other models (p≈0.0000 for all contrasts). The LSTM
came in second, beating Logistic Regression (p=0.9097), Random Forest (p=0.0219),
Neural Network (p=0.0118), and CNN (p=0.6327), although its superiority over the
CNN was not statistically significant (p=0.6327). Standard models such as Logistic
Regression and Random Forest always lagged behind, with Random Forest being
significantly worse compared to SVM (p=0.0060) and LSTM (p=0.0219). Although
the SVM performed better than Logistic Regression (p=0.0220) and Random For-
est (p=0.0060), it could not outperform advanced architectures such as LSTM and
27

--- Page 28 ---

Table 4 Pairwise t-Test Results for Model Comparison on Telugu-English Dataset
LR
SVM
RF
NN
CNN
LSTM
LLM
LR
—
> (0.022)
> (0.006)
> (0.721)
> (0.142)
< (0.910)
< (0.001)
SVM
< (0.022)
—
> (0.462)
< (0.070)
< (0.588)
< (0.022)
< (0.001)
RF
< (0.006)
< (0.462)
—
< (0.031)
< (0.419)
< (0.012)
< (0.001)
NN
< (0.721)
> (0.070)
> (0.031)
—
> (0.381)
< (0.633)
< (0.001)
CNN
< (0.142)
> (0.588)
> (0.419)
< (0.381)
—
< (0.103)
< (0.001)
LSTM
> (0.910)
> (0.022)
> (0.012)
> (0.633)
> (0.103)
—
< (0.001)
LLM
> (0.001)
> (0.001)
> (0.001)
> (0.001)
> (0.001)
> (0.001)
—
LLM. Interestingly, the CNN and Neural Network had inconsistent performance,
where there were no statistically significant differences in a number of pairwise com-
parisons (e.g., CNN vs. Neural Network, p=0.4194). These observations highlight the
superior performance of sequence-based models (LLM, LSTM) over traditional meth-
ods in this task. The findings also point to the importance of epoch and learning rate
tuning, indicated by the fact that the highest accuracy (80.50%) was achieved using
the optimal parameter setting of the LLM (lr=3e-5, epochs=3).
Table 5 Performance Comparison of Models on Nepali-English and
Telugu-English Datasets
Model
Precision
Recall
F1 Score
Accuracy
Nepali-English Dataset
Logistic Regression
0.720
0.720
0.723
0.720
SVM
0.730
0.730
0.724
0.730
Random Forest
0.700
0.700
0.697
0.700
Neural Network
0.740
0.740
0.736
0.740
CNN
0.735
0.738
0.733
0.738
LSTM
0.738
0.733
0.729
0.733
LLM
0.790
0.788
0.786
0.788
Telugu-English Dataset
Logistic Regression
0.531
0.523
0.525
0.523
SVM
0.548
0.584
0.480
0.584
Random Forest
0.534
0.583
0.477
0.583
Neural Network
0.530
0.542
0.505
0.542
CNN
0.522
0.524
0.483
0.524
LSTM
0.535
0.548
0.537
0.548
LLM
0.910
0.907
0.907
0.907
Table 5 shows a comparative evaluation of different machine learning models on
Nepali and Telugu datasets with respect to four performance measures: Precision,
Recall, F1 Score, and Accuracy. In both datasets, the Large Language Model (LLM)
by far surpasses the conventional and deep learning models with the highest score in
all measures. To be precise, on the Nepali dataset, LLM achieves an F1 Score of 0.7858
and Accuracy of 0.7878, which is better than CNN and LSTM. The benefit is even
more marked on the Telugu dataset, where LLM achieves an F1 Score of 0.9069 and
28

--- Page 29 ---

Accuracy of 0.9070, reflecting a wide performance gap compared to traditional models
such as SVM and Random Forest. The results emphasize the better generalization and
language flexibility of LLMs for multilingual text classification tasks.
7.3 Threats to Validity
In conducting this study on abusive language detection within code-mixed Nepali and
Telugu social media posts, several potential threats to validity were identified and are
outlined below:
Internal Validity: The selection of comments from specific videos may introduce
selection bias, potentially affecting the representativeness of the dataset. Addition-
ally, relying on volunteer annotators could lead to annotation bias due to varying
interpretations of what constitutes abusive content.
External Validity: The findings may have limited generalization beyond the
specific linguistic and cultural contexts of Nepali and Telugu code-mixed social media.
The dynamic nature of language and evolving social norms also pose challenges to the
temporal validity of the developed models.
Construct Validity: Defining ”abusive” language is inherently subjective, which
may lead to inconsistencies in annotation. The complexity of code-mixed language
further complicates the accurate identification and labeling of abusive content.
Statistical Conclusion Validity: Potential issues such as overfitting, especially
when using complex models on limited data, could affect the reliability of the con-
clusions drawn. Ensuring appropriate statistical methods and validation techniques is
crucial to mitigate this threat.
Ethical Considerations: Exposure of annotators to potentially harmful content
raises concerns about their well-being. Additionally, collecting and using social media
comments necessitates careful attention to privacy and ethical standards.
Acknowledging these threats is essential for interpreting the study’s findings and
understanding the limitations inherent in the research design. To highlight the novelty
and relevance of our findings, we now review related work in this domain.
8 Related Work
The rise of code-mixed language as a dominant form of online communication, partic-
ularly on social media, has spurred increasing research interest in multilingual Natural
Language Processing (NLP). However, most of the existing work has centered on high-
resource language pairs such as Hindi-English, Spanish-English, and Arabic-English,
while low-resource combinations like Telugu-English and Nepali-English remain sig-
nificantly underexplored. This gap is particularly evident in the domain of abusive
language detection, where the informal, context-rich, and often culturally nuanced
nature of code-mixed language presents unique challenges.
Researchers have acknowledged the importance of building annotated datasets to
advance code-mixed NLP. A prominent contribution is the DravidianCodeMix dataset,
which includes Tamil-English, Malayalam-English, and Kannada-English comments
annotated for sentiment and offensive language detection tasks [21]. This dataset has
been used in shared tasks that aim to benchmark models on South Asian languages.
29

--- Page 30 ---

Similarly, Khanuja et al. introduced a Hindi-English dataset for natural language
inference using Bollywood dialogues, offering insights into reasoning and semantics in
code-switched settings [22]. However, such efforts rarely extend to low-resource pairs
like Telugu-English or Nepali-English.
Datasets like HASOC [4] and OffensEval [23] focus on hate speech and offensive
language but are mostly confined to Hindi-English or Urdu-English combinations.
These datasets form the foundation for supervised learning benchmarks, yet do not
account for the linguistic and cultural characteristics of other underrepresented South
Asian languages. While synthetic code-mixed data generation using large language
models has been explored [24], such methods often lack the realism and variation of
actual user-generated content, making human-annotated corpora indispensable.
In terms of methodology, early approaches to abusive language detection in code-
mixed text employed traditional machine learning models such as SVMs, Logistic
Regression, and Random Forests [25, 26]. These models relied on engineered features
like n-grams, character-level cues, and part-of-speech tags. Although these techniques
are interpretable and lightweight, they generally fall short in capturing deeper con-
textual or sequential information—especially in noisy or highly informal code-mixed
settings.
The advent of deep learning has led to the adoption of neural models such as
CNNs and LSTMs, which are more capable of handling the sequential and contextual
complexity of code-mixed language [27]. Transformer-based models like multilingual
BERT (mBERT) [17], XLM-R [28], and IndicBERT [29] have further advanced the
field by enabling cross-lingual understanding. However, the performance of these mod-
els is often constrained by the lack of representation for languages like Telugu and
Nepali in the pretraining data.
Linguistic challenges also remain significant. The absence of a standardized Roman-
ization system introduces orthographic inconsistencies that complicate tokenization
and preprocessing. Additionally, the fluidity of code-switching—occurring at phrase,
clause, or word level—makes it harder to design robust NLP pipelines. Annotation
itself is a complex task in this domain, as offensive language can be subtle, culturally
specific, or sarcastic. Studies have shown that inconsistencies in labeling, especially in
subjective tasks, can lead to notable drops in model accuracy [25].
Despite notable advances, Telugu-English and Nepali-English remain largely absent
from most mainstream resources, benchmarks, and shared tasks. Given that these
combinations are frequently used by millions of users in emotionally or politically
charged discussions, the need for focused research is clear. Moreover, existing datasets
tend to focus on sentiment or emotion detection rather than abuse-specific tasks in
organically occurring Romanized content.
To address this gap, the current study introduces two novel, manually annotated
datasets for classifying abusive and non-abusive content in Telugu-English and Nepali-
English tex 1. The data, collected from real-world social media platforms, covers a
variety of domains such as politics, entertainment, and daily conversation. By includ-
ing language tagging, part-of-speech labels, and code-mixing statistics, this dataset
1https://github.com/Ranveer098/Code-Mix-and-Code-Switch
30

--- Page 31 ---

serves as a valuable linguistic and computational resource for future multilingual NLP
research.
9 Conclusion
This research presents a significant step toward addressing the scarcity of resources
for abusive language detection in low-resource, code-mixed language contexts. By
curating and annotating a large dataset of Telugu-English and Nepali-English com-
ments, we contribute a valuable linguistic asset that mirrors the actual language
used in multilingual digital spaces. The dataset captures the complexity of informal
online discourse, including transliteration inconsistencies, cultural nuances, and diverse
syntactic patterns, all of which pose challenges for automated systems.
Through systematic experimentation, we assessed the performance of multiple
machine learning, deep learning, and large language models. The findings revealed
that while classical models like Logistic Regression, SVM, and Random Forest serve
as reasonable baselines, they struggle with the intricacies of code-mixed text. Deep
learning architectures such as LSTM and CNN performed better, particularly in han-
dling sequential and contextual dependencies. However, the most notable performance
gains came from transformer-based LLMs, which demonstrated robust generalization
and significantly outperformed other methods across both language pairs.
In addition to performance analysis, we applied rigorous statistical tests, including
paired t-tests, to validate the significance of model differences. These results affirm the
reliability of our evaluation and underscore the importance of hyperparameter tuning
and architecture selection in achieving optimal results for code-mixed abusive content
detection.
Despite the promising outcomes, the work also highlights persistent challenges,
such as inconsistent Romanization, limited domain coverage, and the subjective
nature of abuse annotation. These issues suggest avenues for future improvement,
including the integration of more refined preprocessing techniques, culturally sensi-
tive annotation guidelines, and the inclusion of additional South Asian code-mixed
languages.
Overall, this study lays a strong foundation for future research in code-mixed NLP
by offering a benchmark dataset, performance insights, and practical considerations
for model development. As multilingual communication continues to evolve online,
the need for effective moderation tools that account for linguistic diversity becomes
increasingly urgent. We hope this work will encourage further advancements in ethical
and inclusive AI systems tailored to underrepresented language communities.
Declarations
• Conflict of interest: The authors declare that they have no known competing finan-
cial interests or personal relationships that could have appeared to influence the
work reported in this paper.
31

--- Page 32 ---

References
[1] Srivastava, V. & Singh, M. Phinc: A parallel hinglish social media code-mixed
corpus for machine translation. arXiv preprint arXiv:2004.09447 (2020).
[2] Huzaifah, M., Zheng, W., Chanpaisit, N. & Wu, K. Evaluating code-switching
translation with large language models, 6381–6394 (2024).
[3] Singh, K., Sen, I. & Kumaraguru, P. A twitter corpus for hindi-english code mixed
pos tagging, 12–17 (2018).
[4] Mandl, T. et al. Overview of the hasoc track at fire 2019: Hate speech and offensive
content identification in indo-european languages, 14–17 (2019).
[5] Tiwari, P. & Rai, S. Mind your tweet: Abusive tweet detection, 704–715 (Springer,
2021).
[6] Ruder, S., Vuli´c, I. & Søgaard, A. A survey of cross-lingual word embedding
models. Journal of Artificial Intelligence Research 65, 569–631 (2019).
[7] Barman, U., Das, A., Wagner, J. & Foster, J.
Code mixing: A challenge for
language identification in the language of social media, 13–23 (2014).
[8] Solorio, T. et al. Overview for the first shared task on language identification in
code-switched data, 62–72 (2014).
[9] Adhikari,
K.
P.
English
in
nepal:
Code-switching
and
code-mixing
on
live
nepali
tv
show.
NELTA
ELT
Forum
(2018).
URL
https://neltaeltforum.wordpress.com/2018/02/06/
english-in-nepal-code-switching-and-code-mixing-on-live-nepali-tv-show/.
[10] Saud, M. S. Linguistic hybridity: The use of code mixing in nepali folk pop songs.
Journal of NELTA Gandaki 5, 43–54 (2022).
[11] Gurung, D.
Nepali-English code-switching in the conversations of Nepalese
people:
A
sociolinguistic
study.
Ph.D.
thesis,
University
of
Roehamp-
ton (2019).
URL https://pure.roehampton.ac.uk/portal/en/studentTheses/
nepali-english-code-switching-in-the-conversations-of-nepalese-pe.
[12] Poplack, S.
Sometimes i’ll start a sentence in spanish y termino en espa˜Nol:
Toward a typology of code-switching. Linguistics 18, 581–618 (1980).
[13] Muysken, P. Bilingual Speech: A Typology of Code-Mixing (Cambridge University
Press, Cambridge, UK, 2000).
[14] Ali, B. J. Inter and intrasentential code switching among late bilinguals. Zanco
Journal of Human Sciences 25, 13–25 (2019).
32

--- Page 33 ---

[15] Gamb¨ack, B. & Das, A. Comparing the level of code-switching in corpora, 11–19
(Association for Computational Linguistics, 2014).
[16] Gamb¨ack, B. & Das, A.
Comparing the level of code-switching in corpora.
Language Resources and Evaluation 50, 495–525 (2016).
[17] Devlin, J., Chang, M.-W., Lee, K. & Toutanova, K.
Bert: Pre-training of
deep bidirectional transformers for language understanding.
arXiv preprint
arXiv:1810.04805 (2019).
[18] Joachims, T. Text categorization with support vector machines: Learning with
many relevant features, 137–142 (Springer, 1998).
[19] Breiman, L. Random forests. Machine Learning 45, 5–32 (2001).
[20] Dodge, J. et al. Fine-tuning pretrained language models: Weight initializations,
data orders, and early stopping, 4346–4364 (2020).
[21] Chakravarthi, B. R. et al.
Dravidiancodemix: Sentiment analysis and offen-
sive language identification dataset for dravidian languages in code-mixed text.
Language Resources and Evaluation 56, 765–806 (2022).
[22] Khanuja, S., Dandapat, S., Sitaram, S. & Choudhury, M. A new dataset for natu-
ral language inference from code-mixed conversations, 9–16 (European Language
Resources Association, 2020).
[23] Zampieri, M. et al. Predicting the type and target of offensive posts in social
media, 1415–1420 (2019).
[24] Zeng, X. et al. Synthetic code-mixed data generation using pretrained language
models. arXiv preprint arXiv:2205.00000 (2022).
[25] Waseem, Z. & Hovy, D.
Hateful symbols or hateful people? predictive fea-
tures for hate speech detection on twitter, 88–93 (Association for Computational
Linguistics, 2016). URL https://aclanthology.org/N16-2013/.
[26] Founta, A. M. et al. Large scale crowdsourcing and characterization of twitter
abusive behavior (2018). URL https://ojs.aaai.org/index.php/ICWSM/article/
view/15051.
[27] Perez-Rosas, V., Balahur, A. & Caragea, C. Automatic detection of code-mixed
language in social media. Proceedings of the 27th International Conference on
Computational Linguistics 3033–3044 (2018).
[28] Conneau, A. et al. Unsupervised cross-lingual representation learning at scale
(2020).
33

--- Page 34 ---

[29] Kakwani, D., Sinha, R., Ramesh, V. et al. Indicnlpsuite: Monolingual corpora,
evaluation benchmarks and pretrained multilingual language models for indian
languages (2020).
34

```
