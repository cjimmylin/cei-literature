---
title: "2024-Li-Language Ranker A Metric for Quantifying LLM Performance Across - PDF Extract"
source_pdf: "2024-Li-Language Ranker A Metric for Quantifying LLM Performance Across.pdf"
pages: 11
extracted_at: "2026-02-13T17:43:17.897840"
---

# PDF Extract: 2024-Li-Language Ranker A Metric for Quantifying LLM Performance Across

**Source PDF:** 2024-Li-Language Ranker A Metric for Quantifying LLM Performance Across.pdf
**Total Pages:** 11

---

## Content

```
--- Page 1 ---

Language Ranker: A Metric for Quantifying LLM Performance Across
High and Low-Resource Languages
Zihao Li1*, Yucheng Shi2, Zirui Liu3, Fan Yang4, Ali Payani5, Ninghao Liu2, Mengnan Du1
1New Jersey Institute of Technology, 2University of Georgia, 3University of Minnesota at Twin Cities
4Wake Forest University, 5Cisco Research
lizihao9885@gmail.com, yucheng.shi@uga.edu, zrliu@umn.edu, yangfan@wfu.edu,
apayani@cisco.com, ninghao.liu@uga.edu, mengan.du@njit.edu
Abstract
The development of Large Language Models (LLMs) re-
lies on extensive text corpora, which are often unevenly dis-
tributed across languages. This imbalance results in LLMs
performing significantly better on high-resource languages
like English, German, and French, while their capabilities in
low-resource languages remain inadequate. Currently, there
is a lack of quantitative methods to evaluate the perfor-
mance of LLMs in these low-resource languages. To ad-
dress this gap, we propose the Language Ranker, an intrinsic
metric designed to benchmark and rank languages based on
LLM performance using internal representations. By compar-
ing the LLM’s internal representation of various languages
against a baseline derived from English, we can assess the
model’s multilingual capabilities in a robust and language-
agnostic manner. Our analysis reveals that high-resource lan-
guages exhibit higher similarity scores with English, demon-
strating superior performance, while low-resource languages
show lower similarity scores, underscoring the effectiveness
of our metric in assessing language-specific capabilities. Be-
sides, the experiments show that there is a strong correla-
tion between the LLM’s performance in different languages
and the proportion of those languages in its pre-training cor-
pus. These insights underscore the efficacy of the Language
Ranker as a tool for evaluating LLM performance across dif-
ferent languages, particularly those with limited resources.
Introduction
Large Language Models (LLMs), such as GPT-4, Claude-3
and LlaMa-3, have demonstrated remarkable performance
in various NLP tasks (Achiam et al. 2023; Ouyang et al.
2022; Touvron et al. 2023; Team et al. 2024; Jiang et al.
2023; Bai et al. 2023). However, this progress masks a criti-
cal issue: the stark disparity in LLM performance across lan-
guages, particularly disadvantaging low-resource languages
common in developing countries. This disparity stems from
the overwhelming bias towards high-resource languages,
especially English, in training datasets (Xie et al. 2024).
For instance, approximately 92.65% of GPT-3’s training to-
kens are in English, leaving a mere 7.35% for all other
languages (OpenAI 2023). Similarly, English accounts for
89.70% of LlaMa2’s pre-training data (Touvron et al. 2023).
* Work done during Zihao Li’s remote internship at NJIT.
Copyright © 2025, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
This imbalance leads to significant performance gaps
between high-resource languages (e.g., English, German,
French) and low-resource languages, potentially exacer-
bating global digital divides. LLMs often struggle with
context-specific interpretations in low-resource languages,
such as understanding culturally specific expressions or id-
ioms (Zhang et al. 2023). Recent studies confirm that pre-
trained models perform poorly in languages with insufficient
training data (Lankford, Afli, and Way 2024), highlighting
the urgent need for robust methods to quantify and address
these disparities. It is urgent to develop a tool to quantify lin-
guistic biases in LLMs, so as to contribute to more equitable
AI technologies, potentially improving access and perfor-
mance for underserved language communities worldwide.
To tackle this challenge, we introduce Language Ranker,
a novel metric designed to systematically evaluate LLM
performance across diverse languages, with a particular fo-
cus on low-resource languages. Our method leverages in-
ternal representations of LLMs, establishing English corpus
representations as a baseline and measuring the similarity
between this baseline and representations from other lan-
guages. This similarity score serves as a quantitative mea-
sure of language-specific performance. We validate Lan-
guage Ranker by applying it to five state-of-the-art LLMs:
LlaMa2 (Touvron et al. 2023), LlaMa3 (Meta-AI 2024),
Qwen (Bai et al. 2023), Mistral-v0.1 (Jiang et al. 2023), and
Gemma (Team et al. 2024). Additionally, we analyze the re-
lationship between Language Ranker scores, the proportion
of languages in training datasets, and performance on estab-
lished benchmarks. Our comprehensive experiments yield
the following key findings:
• Experimental results indicate that high-resource lan-
guages consistently show higher similarity scores with En-
glish, while low-resource languages exhibit lower scores,
validating Language Ranker’s effectiveness in quantifying
language-specific performance disparities.
• We uncover a strong correlation between LLM perfor-
mance and the proportion of languages in pre-training cor-
pora, providing crucial insights into the impact of training
data distribution on multilingual capabilities.
• The analysis of embedding space distributions reveals
that high-resource languages are more evenly distributed,
while low-resource languages cluster narrowly, further
supporting the reliability of the proposed metric.
arXiv:2404.11553v3  [cs.CL]  11 Dec 2024

--- Page 2 ---

The Proposed Method
In this section, we will give an introduction to our analy-
sis method. First, we will introduce the dataset that we used.
Then, we will introduce how to obtain the similarity between
English and other languages, as well as how to compare dif-
ferent LLMs’ performances. 1
Probing Datasets
We use OPUS-100 (Zhang et al. 2020) as our evalua-
tion datasets. OPUS-100 is an English-centric multilin-
gual corpus that covers 100 languages. Each sample con-
sists of text in a non-English language as the original
data, with its English translation serving as the target data.
For example, {”German”: ”Ich wollte dir erst noch et-
was zeigen.”,”English”: ”I wanted to show you something
first.”}. After filtering, there are 94 subsets containing En-
glish, including high-resource languages such as German,
French, and Chinese, as well as low-resource languages such
as Oriya, Kannada, and Kazakh. Each subset contains 2000
samples.
Similarity Measurement
We employ cosine similarity to measure the LLMs’ perfor-
mance gap between the target language and English. Specif-
ically, given two sentences X = {xi}n
i=1 and Y = {yi}m
i=1
representing the text in English and the text in the tar-
get language. Since the current LLMs are all autoregres-
sive models, we use the representation obtained after LLM
mapping of the last token xn and ym as the representation
of the text and calculate the similarity between them. As
we know, LLM consists of several layers of Transformer
blocks (Vaswani et al. 2017). Therefore, after each layer of
mapping by the transformer block, we can get a representa-
tion vector xl
n and yl
m, l = 1...H, where H represents the
number of the layer of LLMs. According to (Li et al. 2024),
the intermediate representation can be briefly summarized
by the following equations:
xl+1 = MLP(xl + MHA(xl))
l = 1...H,
(1)
where MHA means multi-head attention or multi-group at-
tention, and MLP means standard multilayer perceptron
layer. Next, we take xl
n and yl
m to calculate the similarity.
To implement a more robust similarity measure, we use the
average similarity obtained by several intermediate layers as
the final similarity. This process can be described as follows:
Sim =
1
|lsub|
|lsub|
X
i=1
Simi, where Simi =
xi
nyi
m
||xin||||yim||, (2)
where lsub = {5, 10, 15, 20, 25} is the subset of the layers we
selected. Finally, we use Sim to evaluate the performance
gap between English and Non-English corpus.
Rank Correlation Measurement
When we get the similarity between each non-English rep-
resentation and the English representation, we sort them ac-
cording to the similarity to get a sorted ranking list of all
1Our code link: https://github.com/lizh9885/Language-Ranker/
languages. To measure the similarity of the sorted ranking
lists of two LLMs, we use the longest common partial or-
der sublist to measure. It can be defined as follows: For two
sorted lists A and B, find a sublist C that is a subset of A
and B such that for any number of index i1 ≤i2 ≤... ≤in,
Index(Ci1)≤Index(Ci2)≤...≤Index(Cin) is true for both A
and B, and the longest sublist C that makes it true is called
the longest common partial order sublist of A and B. We use
the ratio of the length of the longest common partial order
sublist of two LLMs to the total length of the ranking list as
a metric to measure the correlation.
Experiments
In our experiments, we utilize five prominent open-source
large models: LlaMa2 (Touvron et al. 2023), LlaMa3 (Meta-
AI 2024), Qwen (Bai et al. 2023), Mistral-v0.1 (Jiang et al.
2023), and Gemma (Team et al. 2024).
We conduct experiments to answer the following research
questions in the following four subsections respectively:
RQ1: Can the Language Ranker effectively quantify the per-
formance of LLMs across multiple languages? RQ2: How
consistent are the performance rankings of different LLMs
when evaluated across a diverse set of languages? RQ3: Is
the proposed cosine similarity metric correlated with the
proportion of a language in the LLMs’ pre-training corpus?
RQ4: Is the proposed cosine similarity metric correlated
with performance on other benchmark tasks for quantifying
the multilingual capabilities of LLMs?
Can Language Ranker Quantify LLM
Performance Across Languages? (RQ1)
To visualize the performance of different LLMs in these lan-
guages, we selected 10 representative languages to display
their inference results. They consist of five high-resource
languages, including German, Spanish, French, Indonesian,
and Chinese, and five low-resource languages, including
Igbo, Kazakh, Kannada, Oriya, and Turkmen. Figure 1
shows detailed results, where the X-axis represents differ-
ent layers of LLMs, while the Y-axis represents the similar-
ity between the target language and English for each layer.
From Figure 1, we can observe that high-resource languages
have representations more similar to English, whereas low-
resource languages show less similarity. Specifically, Ger-
man, Spanish, French, and Malay generally maintain cosine
similarity scores above 0.6, with Spanish and French often
showing the highest scores, indicating that these languages
are better represented in the models’ embeddings. In con-
trast, low-resource languages, such as Igbo, Kazakh, Kan-
nada, Oriya, and Turkmen, display significantly lower co-
sine similarity scores, often below 0.4. These results show
the disparities in performance across languages and high-
lights the utility of the Language Ranker in quantifying these
differences robustly.
Comparison Across Different LLMs (RQ2)
In this section, we analyze how various LLMs perform
across multiple languages using the Language Ranker. We

--- Page 3 ---

Figure 1: Performance of different LLMs for ten kinds of language. High-resource languages: German, Spanish, French, In-
donesian and Chinese; and low-resource languages: Igbo, Kazakh, Kannada, Oriya and Turkmen.
focus on understanding the consistency of language perfor-
mance among different LLMs, including models with vary-
ing architectures and training specifics. We have the follow-
ing findings:
(1) Different models display similar results across lan-
guages. Figure 1 presents the cosine similarity scores
across various layers for four different 7B parameter LLMs:
LlaMa2, Gemma, Mistral, and Qwen. Four LLMs display a
similar trend where high-resource languages (i.e., German,
Spanish, French, Malay, and Chinese) consistently exhibit
higher cosine similarity scores compared to low-resource
languages (i.e., Igbo, Kazakh, Kannada, Oriya, and Turk-
men). Figure 2 further corroborates these findings by com-
paring the rank correlation of the similarity scores across
the LLMs. Each LLM’s ranking is used as a baseline, and
the remaining three models exhibit ranking patterns that
are largely similar to this baseline. This similarity indi-
cates that despite differences in model architecture or train-
ing specifics, the relative performance of languages remains
consistent across these four models.
(2) Fine-tuning on specific languages will improve its per-
formance. According to the technical report of Qwen (Bai
et al. 2023), Qwen has additional fine-tuning on the Chi-
nese corpus, which leads to better performance in Chinese.
In Figure 1, we observe that for LlaMa2, Gemma, and Mis-
tral, the performance of Chinese is slightly lower than that of
other high-resource languages. However, for Qwen, the per-
formance of Chinese is roughly comparable to other high-
resource languages and even shows a gradual improvement
Language
Proportion
Similarity
Language
Proportion
Similarity
German
0.17%
0.723
Welsh
≤0.01%
0.396
French
0.16%
0.737
Persian
≤0.01%
0.300
Swedish
0.15%
0.662
Urdu
≤0.01%
0.275
Chinese
0.13%
0.552
Kannada
≤0.01%
0.236
Table 1: The proportion of different languages in the LlaMa2
pre-training corpus and the similarity metric we proposed.
The English language ratio is 89.7%.
in the last few layers. This improvement is more clear in
Qwen, mainly due to additional fine-tuning of the Qwen
model family on the Chinese corpus, as noted in the tech-
nical report of Qwen.
(3) Comparison of Larger LLM Sizes. We extended our
analysis to explore the performance of the similarity metric
in larger language models with 13 billion parameters. Fig-
ure 3 presents the results for LlaMa2 13B and Qwen 13B.
The findings reveal that the general trends observed in 7B
models persist in these larger models. Specifically, the rel-
ative performance of high-resource and low-resource lan-
guages remains largely unchanged, with a clear separation
between the two groups. LlaMa2 13B exhibits more pro-
nounced fluctuations in the initial layers compared to its 7B
counterpart, suggesting potentially richer early-stage lan-
guage representations. These observations highlight both the
consistency of language performance patterns across model
sizes and the potential for larger models to enhance repre-
sentations for specific languages.

--- Page 4 ---

Language
ARC
MMLU
LlaMa2 7B
Gemma 7B
Mistral 7B
Qwen 7B
LlaMa2 7B
Gemma 7B
Mistral 7B
Qwen 7B
Chinese
27%
71%
57%
66%
32%
54%
37%
44%
German
27%
68%
63%
32%
25%
57%
47%
27%
French
31%
76%
59%
42%
24%
58%
48%
28%
Spanish
31%
77%
60%
46%
29%
56%
52%
33%
Italian
29%
77%
67%
44%
23%
56%
44%
32%
Kannada
24%
48%
27%
21%
21%
40%
22%
19%
Hindi
28%
60%
42%
22%
25%
45%
32%
23%
Armenian
19%
40%
36%
20%
20%
36%
30%
25%
Marathi
28%
46%
26%
25%
27%
42%
30%
26%
Telugu
30%
42%
30%
30%
24%
33%
34%
23%
Table 2: Performance on two inference tasks
Llama2
Gemma
Mistral
Qwen
Llama2
Gemma
Mistral
Qwen
1
0.33
0.32
0.33
0.33
1
0.41
0.38
0.32
0.41
1
0.4
0.33
0.38
0.4
1
Correlation
0.0
0.2
0.4
0.6
0.8
1.0
1.2
Figure 2: Rank correlation between different LLMs. This is
calculated using metric introduced in Section 2.3. It shows
high correlations across LLMs.
Relationship to Ratio of Training Corpus? (RQ3)
In this section, we explore the relationship between the pro-
portion of each language in the LlaMa2 pre-training cor-
pus and their corresponding performance as measured by
the similarity metric. According to the technical report of
LlaMa2 (Touvron et al. 2023), we obtain the proportion of
the pre-training corpus of some languages. Table 1 illus-
trates this relationship by listing a selection of languages
with their proportion in the training data and their similar-
ity scores relative to English. The table is divided into two
parts: the left side lists high-resource languages with rela-
tively higher proportions in the LlaMa2 pre-training corpus,
and the right side lists low-resource languages with very low
proportions (≤0.01%). For example, German, with a pro-
portion of 0.17%, has a high similarity score of 0.723, in-
dicating strong performance in comparison to English. This
trend suggests that languages with a higher proportion in the
pre-training corpus tend to have higher similarity scores, re-
flecting better model performance. In contrast, low-resource
languages like Kannada and Urdu, each with proportions
of less than 0.01%, have much lower similarity scores (i.e.,
5
10
20
25
30
15
Layers
0.2
0.3
0..4
0.5
0.6
0.7
Cosine Similarity
LlaMa 13B
5
10
20
25
30
15
Layers
0.3
0..4
0.5
0.6
0.7
0.8
Cosine Similarity
Qwen 13B
Turkmen
German Spanish
French
Malay
Chinese
lgbo
Kazakh
Kannada
Oriya
Figure 3: Cosine similarity scores across model layers for
LlaMa2 13B and Qwen 13B. The graph shows results for the
same 10 languages as in Figure 1. The findings reveal that
the general trends observed in 7B models persist in these
larger models.
0.236 and 0.275).
Correlation with Other Inference Tasks? (RQ4)
To more comprehensively reflect the performance of LLMs
in various languages, we evaluate the multilingual reasoning
ability of these LLMs.
We use MLMM-evaluation2 as our benchmark dataset to
evaluate LLMs’ performances on reasoning tasks in vari-
ous languages. The benchmark dataset can be used to eval-
uate the LLM across 26 different languages. It consists of
three datasets: ARC (Clark et al. 2018), HellaSwag (Zellers
et al. 2019), and MMLU (Hendrycks et al. 2020). We chose
ARC and MMLU for evaluation, and both of them are
multiple-choice datasets. The ARC dataset consists of 7,787
multiple-choice science questions drawn from a variety of
sources. The MMLU dataset contains multiple-choice ques-
tions derived from diverse fields of knowledge. We selected
five high-resource languages (Chinese, German, French,
Spanish, Italian) and five low-resource languages (Kannada,
Hindi, Armenian, Marathi, Telugu) for evaluation, randomly
selected 100 samples from each language for 4-shot learning
prediction, and used accuracy as the metric. The LLMs eval-
uated are consistent with Figure 1: LlaMa2 7B, Gemma 7B,
Mistral 7B, and Qwen 7B.
2https://github.com/nlp-uoregon/mlmm-evaluation

--- Page 5 ---

Figure 4: Visualization of the embedding space of Gemma 7B for eight languages. Four figures at the top are high-resource
languages, Four figures at the bottom are low-resource languages.
High-High
Similarity Score
High-Low
Similarity Score
Low-Low
Similarity Score
English-German
0.72
German-Silesian
0.48
Azerbaijani-Turkmen
0.51
Italian-French
0.68
French-Erzya
0.35
Hungarian-Yiddish
0.24
German-French
0.67
Italian-Romany
0.32
Kab-SMT
0.36
French-Chinese
0.59
Italian-Uighur
0.27
Mari-Tatar
0.48
Table 3: Similarity score of different language pairs of Gemma 7B.
The predicted result is shown in Table 2. From the re-
sult, we find that for Gemma, Mistral, and Qwen, the per-
formance of high-resource languages is significantly better
than that of low-resource languages, and Gemma performs
best. For the LlaMa2, the performance in all languages is
generally not as good as the first three LLMs. This re-
sult shows that LLM reasoning ability in low-resource lan-
guages is worse than that in high-resource languages. This
result proves that there are differences in performance be-
tween high-resource and low-resource languages in reason-
ing tasks, illustrating the effectiveness of the proposed co-
sine similarity metric.
Further Analysis of Proposed Metric
In the last section, we introduced and evaluated the Lan-
guage Ranker, demonstrating its ability to quantify the mul-
tilingual capabilities of LLMs by comparing their internal
representations against an English baseline. This provided a
robust measure of how LLMs perform across different lan-
guages, especially highlighting the disparities between high-
resource and low-resource languages.
Building on these insights, in this section, we delve deeper
into the proposed metric to explore its credibility and reli-
ability further. Specifically, we aim to answer the follow-
ing questions in the following three subsections: RQ5: Is
choosing English as the benchmark a wise choice? RQ6:
What does the subspace of each language look like? RQ7:
Is choosing cosine similarity a wise choice?
Why Using English as Baseline? (RQ5)
In the above sections, we choose English as a baseline.
This is based on the a priori assumption that low-resource
languages generally perform worse than high-resource lan-
guages. But if we choose other high-resource languages
as baselines, will we get the same performance? In other
words, how can we ensure that our metric is not affected
by the English language itself? To answer this question,
we divided our probing datasets into three types: High
Resource-High Resource (H-H), High Resource-Low Re-
source (H-L), and Low Resource-Low Resource (L-L). To
fulfill our requirement, we utilize Tatoeba-Challenge (Tiede-
mann 2020) as our dataset instead of opus-100 because the
latter is an English-centric dataset which means there is
no Low Resource-Low Resource language pair. Tatoeba-
Challenge is a challenge set for machine translation that con-
tains 32G translation units in 2,539 bitexts. The whole data
set covers 487 languages linked to each other in 4,024 lan-
guage pairs. We select four language pairs for each group,

--- Page 6 ---

High-High
Similarity Score
High-Low
Similarity Score
Low-Low
Similarity Score
English-German
0.72
German-Silesian
0.44
Azerbaijani-Turkmen
0.51
Italian-French
0.69
French-Erzya
0.31
Hungarian-Yiddish
0.19
German-French
0.68
Italian-Romany
0.15
Kab-SMT
0.40
French-Chinese
0.56
Italian-Uighur
0.20
Mari-Tatar
0.42
Table 4: Similarity score of different language pairs of LlaMa2 7B.
0-0.1
0.1-0.2
0.2-0.3
0.3-0.4
0.4-0.5
0.5-0.6
Double Var
0.35
0.40
0.45
0.50
0.55
0.60
0.65
0.70
Similarity
Gemma 7B
0-0.1
0.1-0.2
0.2-0.3
0.3-0.4
0.4-0.5
0.5-0.6
Double Var
0.2
0.3
0.4
0.5
0.6
Similarity
Mistral 7B
Figure 5: Box plot of the relationship between the double variance and similarity of Gemma 7B and Mistral 7B.
English-German (en-de), English-French (en-fr), German-
French (de-fr), and Italian-German (it-de) represent H-H;
German - Silesian (de-szl), French-Erzya (fr-myv), Ital-
ian - Romany (it-ro) and Italian - Uighur (it-uig) represent
H-L; Azerbaijani-Turkmen (az-tr), Hungarian-Yiddish (hu-
yi), Kabyle-Standard Moroccan Tamazight (kab-SMT) and
Mari-Tatar (ma-ta) represent L-L. The results are shown in
Table 3 and Table 4.
From the results, we can observe that the score of High-
High is higher than the score of High-Low and Low-
Low universally. An obvious inference is that the distri-
bution of high-resource languages is relatively close to
each other, while the distribution of low-resource languages
varies greatly, neither being close to each other nor to
high-resource languages. Therefore, the distribution of high-
resource languages is relatively consistent, while the distri-
bution of low-resource languages varies greatly. Choosing
English as the baseline is a convenient choice. Thus, we can
also choose other high-resource languages such as German
and French as the baseline.
Deeper Analysis of the Embedding Space (RQ6)
We explained why we chose English as the baseline in
the above section. Choosing English is actually choosing
a high-resource language as our baseline. A question nat-
urally arises: How can we make sure that the performance
of high-resource languages is better than the performance
of low-resource languages? The result of Table 2 has con-
firmed the answer to the question by the reasoning task.
To answer this question more deeply, we need to analyze
the distribution of the embedding of different languages. As
is shown in Figure 4, the top four sub-figures are embed-
ding spaces of high-resource languages, while the bottom
four sub-figures are embedding spaces of low-resource lan-
guages. It is obvious that high-resource languages are more
evenly distributed throughout the space, while low-resource
languages are more narrowly distributed, and compressed
into a near straight line. Therefore, the performance of low-
resource languages is worse than that of high-resource lan-
guages, which means it is suitable to choose a high-resource
language like English as the baseline.
Why Using Cosine Similarity? (RQ7)
Recent research (Steck, Ekanadham, and Kallus 2024) has
shown that cosine similarity is not always a reliable metric.
Inspired by Section , the quality of the performance of vari-
ous languages can be clearly judged from the subspace dis-
tribution. Therefore, we decided to quantify the performance
of these languages from a distribution perspective.
Back to Figure 4, the projection distributions of high-
resource languages in different directions are relatively con-
sistent, while the distribution of low-resource languages is
compressed approximately into a straight line. The projec-
tion distributions outside the straight line, such as the pro-
jections perpendicular to the straight line, are crowded in a
smaller area. This suggests that we can use the projection
variance to approximately measure the quality of the distri-
bution.
According to PCA, we assume the embedding vectors are
{Xi}n
i=1(being centralized), the projection direction is ω,

--- Page 7 ---

Gemma 7B
Mistral 7B
High-resource
Low-resource
High-resource
Low-resource
Language
Double Var
Similarity
Language
Double Var
Similarity
Language
Double Var
Similarity
Language
Double Var
Similarity
Italian
0.04
0.66
Nepali
0.75
0.42
Italian
0.12
0.59
Nepali
0.60
0.28
French
0.09
0.69
Kazakh
0.85
0.38
French
0.17
0.65
Kazakh
0.32
0.32
Spanish
0.06
0.68
Burmese
0.36
0.30
Spanish
0.17
0.64
Burmese
0.40
0.20
German
0.10
0.72
Pashto
0.72
0.36
German
0.19
0.66
Pashto
0.73
0.29
Table 5: Similarity scores and double variance results for some languages on Gemma 7B and Mistral 7B.
the project variance V ar(X, ω) can be calculated as follows:
V ar(X, ω) = 1
n
n
X
i=1
(XT
i ω)2 = 1
n
n
X
i=1
ωT XiXT
i ω
= ωT Cov(X)ω
s.t.
ωT ω = 1
(3)
It is obvious that V ar(X, ω) is the eigenvalue of the
Cov(X). For high-resource languages, projection variance
in different directions should be close to each other so that
it can be evenly distributed in all directions. The opposite
is true for low-resource languages. Therefore, we can ex-
tract the first K eigenvalues {V ar(X, ωi)}k
i=1 and calculate
their variance. The variance of the eigenvalues can be used to
measure the differences in the distribution in each direction,
which is called double variance. This metric can be used
to specifically measure the quality of the distribution. The
higher the double variance, the more unbalanced the distri-
bution and the worse the performance, and the vice versa.
We employ the box plot to show the relationship between
the proposed cosine similarity metric and the double vari-
ance metric more clearly. From Table 5, we can observe that
for each LLM, the languages in the left part are some com-
mon high-resource languages, which have higher similarity
and lower double variance, while the right part is the oppo-
site for low-resource languages. The second observation is
that as the variance increases, the similarity score also tends
to decrease. The increase in variance means that the distri-
bution of the subspace becomes uneven and the similarity
score decreases accordingly. This shows that the proposed
cosine similarity metric can be utilized to roughly measure
the quality of distribution of the subspace, which can thus
measure the performance of LLM in different languages.
Related Work
Representation Engineering. Representation engineering
has emerged as an effective approach to enhance the in-
terpretability and transparency of LLMs. Researchers have
been leveraging internal representations to tackle various
challenges. Zou et al. (2023) summarizes the application of
representation engineering in bias, fairness, model editing,
and other areas. Gurnee and Tegmark (2023) found that the
internal representation of LLM has a certain correlation with
time and space, and the internal representation can be em-
ployed to represent time and space. Li et al. (2024) found
that the representation of the attention head inside the LLM
can be used to indicate the correct reasoning direction, probe
analysis is further used to correct the internal representa-
tion direction to improve the LLM’s performance. Marks
and Tegmark (2023) study the structure of LLM represen-
tations of true/false statements, proved that language mod-
els linearly represent the true/false of factual statements. Ju
et al. (2024) used probe technique to detect how LLM stores
knowledge layer by layer.
Multilingual Language Model. Recent research such as
(Qin et al. 2024) summarizes the recent progress and fu-
ture trends in multilingual large language models. Ahuja
et al. (2024) constructed a benchmark to evaluate LLM’s
multilingual ability comprising 22 datasets covering 83 lan-
guages. Huang et al. (2023); Qin et al. (2023) have proven
that LLM performance varies substantially across different
languages and they employ a prompt technique to improve
task performance across languages. Wendler et al. (2024) ex-
plores how LlaMa2 works in multilingual tasks and what
role English plays in these tasks. The imbalance distribution
of training corpus in different languages leads to the bias
of LLM towards some high-resource languages such as En-
glish (Blasi, Anastasopoulos, and Neubig 2021). Some ap-
proaches employ multilingual language modeling to allevi-
ate the phenomenon (Shen et al. 2024; Kalyan, Rajasekha-
ran, and Sangeetha 2021; Conneau et al. 2019). These stud-
ies show the importance of strengthening the cross-lingual
capabilities of the pre-trained model. Sch¨afer et al. (2024)
found that the presence of a primary language in the train-
ing process of LLMs can improve the performance of low-
resource languages and lead to a more consistent representa-
tion of LLMs in different languages. Liu et al. (2024) found
that for English-centric LLMs, although translation into En-
glish helps improve the performance of NLP tasks, it is not
the best choice for all situations.
Conclusions and Future Work
In this work, we propose the Language Ranker to evalu-
ate the performance of LLMs across diverse languages by
comparing their internal representations to English. The re-
sults show that high-resource languages show higher sim-
ilarity scores with English, while low-resource languages
have lower scores, validating the effectiveness of our met-
ric in assessing language performance. Besides, there is a
strong correlation between the performance of LLMs in dif-
ferent languages and the proportion of those languages in
the pre-training corpus. Further, results indicate that high-
resource languages are more evenly distributed in the em-
bedding space, whereas low-resource languages tend to be
narrowly clustered. In the future, we plan to design more
comprehensive benchmarks to measure LLM’s capabilities
in different languages. Besides, we plan to explore the ap-
plication of the Language Ranker to guide the development
of more balanced multilingual training datasets and improve
LLM performance on low-resource languages.

--- Page 8 ---

References
Achiam, J.; Adler, S.; Agarwal, S.; Ahmad, L.; Akkaya, I.;
Aleman, F. L.; Almeida, D.; Altenschmidt, J.; Altman, S.;
Anadkat, S.; et al. 2023.
Gpt-4 technical report.
arXiv
preprint arXiv:2303.08774.
Ahuja, S.; Aggarwal, D.; Gumma, V.; Watts, I.; Sathe, A.;
Ochieng, M.; Hada, R.; Jain, P.; Axmed, M.; Bali, K.; and
Sitaram, S. 2024.
MEGAVERSE: Benchmarking Large
Language Models Across Languages, Modalities, Models
and Tasks. arXiv:2311.07463.
Bai, J.; Bai, S.; Chu, Y.; Cui, Z.; Dang, K.; Deng, X.; Fan,
Y.; Ge, W.; Han, Y.; Huang, F.; et al. 2023. Qwen technical
report. arXiv preprint arXiv:2309.16609.
Blasi, D.; Anastasopoulos, A.; and Neubig, G. 2021.
Systematic Inequalities in Language Technology Perfor-
mance across the World’s Languages.
arXiv preprint
arXiv:2110.06733.
Clark, P.; Cowhey, I.; Etzioni, O.; Khot, T.; Sabharwal, A.;
Schoenick, C.; and Tafjord, O. 2018. Think you have solved
question answering? try arc, the ai2 reasoning challenge.
arXiv preprint arXiv:1803.05457.
Conneau, A.; Khandelwal, K.; Goyal, N.; Chaudhary, V.;
Wenzek, G.; Guzm´an, F.; Grave, E.; Ott, M.; Zettle-
moyer, L.; and Stoyanov, V. 2019.
Unsupervised cross-
lingual representation learning at scale.
arXiv preprint
arXiv:1911.02116.
Gurnee, W.; and Tegmark, M. 2023. Language models rep-
resent space and time. arXiv preprint arXiv:2310.02207.
Hendrycks, D.; Burns, C.; Basart, S.; Zou, A.; Mazeika,
M.; Song, D.; and Steinhardt, J. 2020.
Measuring mas-
sive multitask language understanding.
arXiv preprint
arXiv:2009.03300.
Huang, H.; Tang, T.; Zhang, D.; Zhao, W. X.; Song, T.; Xia,
Y.; and Wei, F. 2023. Not all languages are created equal
in llms: Improving multilingual capability by cross-lingual-
thought prompting. arXiv preprint arXiv:2305.07004.
Jiang, A. Q.; Sablayrolles, A.; Mensch, A.; Bamford, C.;
Chaplot, D. S.; Casas, D. d. l.; Bressand, F.; Lengyel, G.;
Lample, G.; Saulnier, L.; et al. 2023. Mistral 7B. arXiv
preprint arXiv:2310.06825.
Ju, T.; Sun, W.; Du, W.; Yuan, X.; Ren, Z.; and Liu,
G. 2024.
How Large Language Models Encode Context
Knowledge? A Layer-Wise Probing Study. arXiv preprint
arXiv:2402.16061.
Kalyan, K. S.; Rajasekharan, A.; and Sangeetha, S. 2021.
Ammus: A survey of transformer-based pretrained mod-
els in natural language processing.
arXiv preprint
arXiv:2108.05542.
Lankford, S.; Afli, H.; and Way, A. 2024. Transformers for
Low-Resource Languages: Is F\’eidir Linn! arXiv preprint
arXiv:2403.01985.
Li, K.; Patel, O.; Vi´egas, F.; Pfister, H.; and Wattenberg, M.
2024. Inference-time intervention: Eliciting truthful answers
from a language model. Advances in Neural Information
Processing Systems, 36.
Liu, C.; Zhang, W.; Zhao, Y.; Luu, A. T.; and Bing, L. 2024.
Is Translation All You Need? A Study on Solving Multi-
lingual Tasks with Large Language Models. arXiv preprint
arXiv:2403.10258.
Marks, S.; and Tegmark, M. 2023.
The geometry of
truth: Emergent linear structure in large language model
representations of true/false datasets.
arXiv preprint
arXiv:2310.06824.
Meta-AI. 2024.
LlaMa3.
https://github.com/meta-llama/
llama3. Accessed: 2024-06-14.
OpenAI. 2023. GPT-3 Dataset Statistics. https://github.com/
openai/gpt-3/tree/master/dataset statistics.
Ouyang, L.; Wu, J.; Jiang, X.; Almeida, D.; Wainwright, C.;
Mishkin, P.; Zhang, C.; Agarwal, S.; Slama, K.; Ray, A.;
et al. 2022. Training language models to follow instructions
with human feedback. Advances in neural information pro-
cessing systems, 35: 27730–27744.
Qin, L.; Chen, Q.; Wei, F.; Huang, S.; and Che, W.
2023. Cross-lingual prompting: Improving zero-shot chain-
of-thought reasoning across languages.
arXiv preprint
arXiv:2310.14799.
Qin, L.; Chen, Q.; Zhou, Y.; Chen, Z.; Li, Y.; Liao, L.; Li,
M.; Che, W.; and Yu, P. S. 2024. Multilingual large language
model: A survey of resources, taxonomy and frontiers. arXiv
preprint arXiv:2404.04925.
Sch¨afer, A.; Ravfogel, S.; Hofmann, T.; Pimentel, T.; and
Schlag, I. 2024.
Language Imbalance Can Boost Cross-
lingual Generalisation. arXiv preprint arXiv:2404.07982.
Shen, L.; Tan, W.; Chen, S.; Chen, Y.; Zhang, J.; Xu, H.;
Zheng, B.; Koehn, P.; and Khashabi, D. 2024. The language
barrier: Dissecting safety challenges of llms in multilingual
contexts. arXiv preprint arXiv:2401.13136.
Steck, H.; Ekanadham, C.; and Kallus, N. 2024. Is Cosine-
Similarity of Embeddings Really About Similarity? In Com-
panion Proceedings of the ACM on Web Conference 2024,
WWW ’24. ACM.
Team, G.; Mesnard, T.; Hardin, C.; Dadashi, R.; Bhupati-
raju, S.; Pathak, S.; Sifre, L.; Rivi`ere, M.; Kale, M. S.; Love,
J.; et al. 2024. Gemma: Open models based on gemini re-
search and technology. arXiv preprint arXiv:2403.08295.
Tiedemann, J. 2020. The Tatoeba Translation Challenge –
Realistic Data Sets for Low Resource and Multilingual MT.
In Proceedings of the Fifth Conference on Machine Trans-
lation, 1174–1182. Online: Association for Computational
Linguistics.
Touvron, H.; Martin, L.; Stone, K.; Albert, P.; Almahairi, A.;
Babaei, Y.; Bashlykov, N.; Batra, S.; Bhargava, P.; Bhosale,
S.; et al. 2023. Llama 2: Open foundation and fine-tuned
chat models. arXiv preprint arXiv:2307.09288.
Vaswani, A.; Shazeer, N.; Parmar, N.; Uszkoreit, J.; Jones,
L.; Gomez, A. N.; Kaiser, Ł.; and Polosukhin, I. 2017. At-
tention is all you need. Advances in neural information pro-
cessing systems, 30.
Wendler, C.; Veselovsky, V.; Monea, G.; and West, R. 2024.
Do Llamas Work in English? On the Latent Language of
Multilingual Transformers. arXiv:2402.10588.

--- Page 9 ---

Xie, Y.; Chen, X.; Zhan, H.; Shivakumara, P.; Yin, B.; Liu,
C.; and Lu, Y. 2024. Weakly supervised scene text genera-
tion for low-resource languages. Expert Systems with Appli-
cations, 237: 121622.
Zellers, R.; Holtzman, A.; Bisk, Y.; Farhadi, A.; and Choi,
Y. 2019. Hellaswag: Can a machine really finish your sen-
tence? arXiv preprint arXiv:1905.07830.
Zhang, B.; Williams, P.; Titov, I.; and Sennrich, R. 2020.
Improving Massively Multilingual Neural Machine Transla-
tion and Zero-Shot Translation. In Proceedings of the 58th
Annual Meeting of the Association for Computational Lin-
guistics, 1628–1639. Online: Association for Computational
Linguistics.
Zhang, X.; Li, S.; Hauer, B.; Shi, N.; and Kondrak, G. 2023.
Don’t trust ChatGPT when your question is not in English:
A study of multilingual abilities and types of LLMs. In Pro-
ceedings of the 2023 Conference on Empirical Methods in
Natural Language Processing, 7915–7927.
Zou, A.; Phan, L.; Chen, S.; Campbell, J.; Guo, P.; Ren, R.;
Pan, A.; Yin, X.; Mazeika, M.; Dombrowski, A.-K.; et al.
2023. Representation engineering: A top-down approach to
ai transparency. arXiv preprint arXiv:2310.01405.

--- Page 10 ---

Appendix
Ranking Result For LLMs
We give the similarity scores of the four LLMs used in
the experiment on 18 high-resource languages. Results are
shown in the following tables.
Language
Similarity Score
Language
Similarity Score
German
0.723
Western Frisian
0.378
French
0.737
Tamil
0.347
Spanish
0.768
Gujarati
0.313
Italian
0.706
Kurdish
0.308
Russian
0.734
Pashto
0.284
Dutch
0.709
Assamese
0.260
Polish
0.664
Central Khmer
0.240
Malay
0.651
Panjabi
0.218
Swedish
0.661
Amharic
0.202
Table 6: The similarity score of LlaMa2 7B.
Language
Similarity Score
Language
Similarity Score
German
0.719
Western Frisian
0.443
French
0.691
Tamil
0.420
Spanish
0.683
Gujarati
0.433
Italian
0.662
Kurdish
0.358
Russian
0.674
Pashto
0.362
Dutch
0.658
Assamese
0.396
Polish
0.618
Central Khmer
0.330
Malay
0.615
Panjabi
0.379
Swedish
0.629
Amharic
0.298
Table 7: The similarity score of Gemma 7B.
Language
Similarity Score
Language
Similarity Score
German
0.639
Western Frisian
0.346
French
0.623
Tamil
0.279
Spanish
0.616
Gujarati
0.270
Italian
0.571
Kurdish
0.262
Russian
0.611
Pashto
0.267
Dutch
0.566
Assamese
0.276
Polish
0.514
Central Khmer
0.252
Malay
0.497
Panjabi
0.213
Swedish
0.532
Amharic
0.191
Table 8: The similarity score of Mistral 7B.
Language
Similarity Score
Language
Similarity Score
German
0.805
Western Frisian
0.441
French
0.793
Tamil
0.510
Spanish
0.800
Gujarati
0.469
Italian
0.773
Kurdish
0.436
Russian
0.794
Pashto
0.448
Dutch
0.773
Assamese
0.507
Polish
0.752
Central Khmer
0.407
Malay
0.730
Panjabi
0.385
Swedish
0.759
Amharic
0.470
Table 9: The similarity score of Qwen 7B.
Details of experiment in Table 4 and Table 3
We selected data from the Tatoeba-Challenge repository3.
Since the number of samples for some low-resource lan-
guage pairs is small, we extracted 100 samples for each lan-
guage pair. If there are less than 100, we extracted all sam-
ples and extracted them according to the test-dev-train pri-
ority. We can observe that the scores of language pairs of
the same type may vary differently but the performance of
each LLM on different types of language pairs is roughly the
same.
High-High
Similarity Score
High-Low
Similarity Score
Low-Low
Similarity Score
English-German
0.64
German-Silesian
0.43
Azerbaijani-Turkmen
0.51
Italian-French
0.60
French-Erzya
0.30
Hungarian-Yiddish
0.18
German-French
0.62
Italian-Romany
0.25
Kab-SMT
0.39
French-Chinese
0.57
Italian-Uighur
0.24
Mari-Tatar
0.46
Table 10: Similarity score of different language pairs of mis-
tral 7B.
High-High
Similarity Score
High-Low
Similarity Score
Low-Low
Similarity Score
English-German
0.81
German-Silesian
0.58
Azerbaijani-Turkmen
0.67
Italian-French
0.75
French-Erzya
0.51
Hungarian-Yiddish
0.39
German-French
0.80
Italian-Romany
0.53
Kab-SMT
0.55
French-Chinese
0.71
Italian-Uighur
0.49
Mari-Tatar
0.55
Table 11: Similarity score of different language pairs of
qwen 7B.
Performance of LLMs with Other Sizes
Bloom 3B and Bloom 7B
Figure 6 shows the result of
Bloom 3B and Bloom 7B. Except for the last few layers
of the model, there are obvious differences between high-
resource languages and low-resource languages which are
similar to the above LLMs, while there are smaller differ-
ences within the same category of languages. The score is
higher than LlaMa2, Gemma, Mistral, and Qwen.
The Relation Between the Performance of
Reasoning and The Similarity Score
We also quantify the relationship between the performance
of the inference task (Table 2) and the language similarity to
English (Figure 1). It can be clearly observed from Figure 7
and Figure 8 that the performance of LLM in reasoning tasks
is highly correlated with the similarity score, it performs bet-
ter in high-resource languages(the first four languages) and
worse in low-resource languages(the last four languages).
3https://github.com/Helsinki-NLP/Tatoeba-
Challenge/tree/master/data

--- Page 11 ---

5
10
15
20
25
30
Layers
0.2
0.4
0.6
0.8
Cosine Similarity
Bloom 3B
5
10
15
20
25
30
Layers
0.0
0.2
0.4
0.6
0.8
1.0
Cosine Similarity
Bloom 7B
German
Spanish
French
Malay
Chinese
Igbo
Kazakh
Kannada
Oriya
Turkmen
Figure 6: Simlarity scores curves of Bloom 3B and Bloom 7B.
German French Spanish Italian Kannada
Hindi
Telugu Marathi
0.0
0.2
0.4
0.6
0.8
0.68
0.76
0.77
0.77
0.48
0.60
0.42
0.46
0.72
0.69
0.68
0.66
0.32
0.37
0.31
0.30
Gemma 7B
ARC Task Accuracy
Similarity Score
Figure 7: Accuracy of ARC reasoning tasks and similarity
scores in different languages on Gemma 7B.
German French Spanish Italian Kannada
Hindi
Telugu Marathi
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.63
0.59
0.60
0.67
0.27
0.42
0.30
0.26
0.64
0.62
0.62
0.57
0.25
0.30
0.31
0.27
Mistral 7B
ARC Task Accuracy
Similarity Score
Figure 8: Accuracy of ARC reasoning tasks and similarity
scores in different languages on Mistral 7B.

```
