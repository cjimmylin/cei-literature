---
title: "Uncovering Latent Human Wellbeing in Language - PDF Extract"
source_pdf: "2024-Freire-Uncovering Latent Human Wellbeing in Language.pdf"
pages: 10
extracted_at: "2026-01-24T17:05:33.425734"
---

# PDF Extract: Uncovering Latent Human Wellbeing in Language

**Source PDF:** 2024-Freire-Uncovering Latent Human Wellbeing in Language.pdf
**Total Pages:** 10

---

## Content

```
--- Page 1 ---

UNCOVERING LATENT HUMAN WELLBEING
IN LANGUAGE MODEL EMBEDDINGS
Pedro Freire∗
Independent
ChengCheng Tan
FAR AI
Adam Gleave
FAR AI
Dan Hendrycks
Center for AI Safety
Scott Emmons
FAR AI, UC Berkeley
ABSTRACT
Do language models implicitly learn a concept of human wellbeing? We ex-
plore this through the ETHICS Utilitarianism task, assessing if scaling enhances
pretrained models’ representations. Our initial finding reveals that, without any
prompt engineering or finetuning, the leading principal component from OpenAI’s
text-embedding-ada-002 achieves 73.9% accuracy. This closely matches
the 74.6% of BERT-large finetuned on the entire ETHICS dataset, suggesting
pretraining conveys some understanding about human wellbeing. Next, we con-
sider four language model families, observing how Utilitarianism accuracy varies
with increased parameters. We find performance is nondecreasing with increased
model size when using sufficient numbers of principal components.
1
INTRODUCTION
Large language models (LLMs) undergo pre-training on extensive human-generated datasets, en-
abling them to capture insights into human language (Manning et al., 2020) and potentially, our
beliefs and wellbeing. This study explores whether LLMs can implicitly understand concepts like
‘pleasure and pain’ without explicit finetuning. We examine the LLM embedding spaces to decipher
data representation and employ principal component analysis (PCA), to reduce dimensionality and
to isolate relevant features for better understanding.
Our experiments aim to extract notions of human utility from language model embeddings. By
using task-specific prompt engineering combined with PCA, we identify embedding dimensions
that reflect aspects of human utility. PCA reduces the embeddings to a lower-dimensional space,
preserving significant variance for interpretation and computational efficiency, a method proven
effective in prior work (Burns et al., 2022). We investigate if these reduced dimensions contain
sufficient information to assess scenarios based on their pleasantness.
The methodology includes embedding extraction, dimensionality reduction via PCA, and logistic
model fitting. In this context, the logistic model assesses which PCA component direction corre-
sponds to higher utility. We explore different supervision levels, employ various prompt templates,
and evaluate both single and paired comparison methods across multiple language models.
A key discovery is that the first principal component in some models achieves comparable perfor-
mance to a finetuned BERT model, indicating a pre-trained model’s embedding direction can serve
as a utility function. Our research further examines how model size influences performance, reveal-
ing that larger models generally perform better with sufficient principal components. Defining this
scaling trend precisely is an open question for future work.
∗work conducted while at FAR AI
1
arXiv:2402.11777v1  [cs.CL]  19 Feb 2024

--- Page 2 ---

2
RELATED WORKS
Recent advancements in LLMs have significantly improved our understanding of their latent knowl-
edge, primarily through advanced prompting techniques (Liu et al., 2021). But studies reveal that
LLMs possess self-evaluation capabilities (Kadavath et al., 2022) and demonstrate a disparity be-
tween their generated outputs and internal representations (Liu et al., 2023).
Research has also extensively explored the knowledge encoded in LLM embeddings (Mikolov et al.,
2013; Vaswani et al., 2017). For instance, Bolukbasi et al. (2016) identified and mitigated gender
bias in embeddings, while Schramowski et al. (2021) discovered a ”moral dimension” in BERT.
Our work extends these findings by employing PCA on the embeddings of the more capable GPT-3
model.
Burns et al. (2022) introduce Contrast Consistent Search (CCS) to find a logical consistency direc-
tion in activation space. However, due to PCA’s comparable performance and simplicity (Emmons,
2023), we use PCA along with contrast pairs in our experiments.
Finally, we particularly focus on the ETHICS dataset (Hendrycks et al., 2020), a benchmark for as-
sessing LLMs’ moral reasoning across a spectrum of ethical scenarios, from justice to commonsense
morality. We examine the utilitarianism subset, addressing the maximization of wellbeing through
pleasure and pain judgments. This subset offers a glimpse into ethical considerations, though it rep-
resents a limited view of ethical considerations and may not fully capture an LLM’s understanding
of human wellbeing. For more detailed information on the ETHICS dataset, see Appendix A.
3
METHOD
Our PCA Representation experiments are conducted in the following steps:
1. Embedding Extraction: For each entry in the ETHICS Utilitarian train split, we extract
high-dimensional embeddings that best represent the model’s understanding of the input
scenario. These embeddings, obtained from the last layer of the language model, serve
as a critical feature set for our analysis. (Reimers and Gurevych, 2019; He et al., 2021;
Neelakantan et al., 2022; Cohere, 2023)
2. Dimensionality Reduction and Comparison: We normalize the embeddings to zero mean
and unit variance before applying PCA to reduce their dimensionality. This process allows
for the comparison of embeddings in a lower-dimensional space.
3. Logistic Model: We fit a logistic regression model to the low-dimensinal embeddings
to predict scenario comparisons, based on the train split’s labeled data.
For one-
dimensional PCA, this just learns which direction (positive or negative) of the PCA com-
ponent represents higher utility, along with a classification threshold.
4
EXPERIMENTAL SETUP
Our experiments aim to answer the following questions:
1. How much ETHICS Utilitarianism information is in state-of-the-art LLM embeddings?
2. How does performance on the ETHICS Utilitarianism subset scale with model size?
3. Does paired evaluation mode lead to higher performance than single evaluation mode?
We test a range of language models (Appendix D) and incorporate different types of supervision:
• Supervised Labels: Labels are used to train the logistic regression model on the PCA
projections. In the 1-dimensional case, this just learns the direction of higher utility and a
classification threshold.
• Prompt Templates: We employ five distinct prompt templates, listed in Appendix B.
• Paired Comparisons: To study a language model’s ability to compare scenarios, we ex-
periment with learning embeddings in two ways. In single mode, we perform PCA on the
2

--- Page 3 ---

cohere
gpt-3
deberta
sentence-
transformer
0.4
0.5
0.6
0.7
0.8
0.9
ETHICS Util test accuracy
0.572
0.626
0.629 0.632
0.525 0.528
0.550 0.568
Top 1 principal component
single
paired
cohere
gpt-3
deberta
sentence-
transformer
0.780 0.779
0.796 0.796
0.743 0.744
0.731 0.731
random
Top 300 principal components
Figure 1: Performance in single and paired mode. Test accuracy (y-axis) for single and paired
mode for different language model families (x-axis). At left, the classification uses only the top
principal component; at right, it uses the top 300. Paired mode does slightly better than single mode.
In both, the violin plot shows the distribution of accuracy across different prompts and models
sizes, with the overall mean accuracy indicated. A notable datapoint in the gpt-3 family is the
text-embedding-ada-002 model, achieving 73.9% accuracy with the single-mode prompt
“{}” (simply copying the scenario).
activations from individual scenarios. In paired mode, we perform PCA on the difference
in activations of pairs, essentially comparing the scenarios, as detailed in Appendix C
• Dataset: By applying PCA to a dataset that was constructed to isolate the concept of
utilitarianism, our method benefits from the supervision of what points were and were not
included in the dataset. We follow the dataset’s train-test split, using only the train split
for learning the embeddings and evaluating on held-out data from the test split.
5
RESULTS
How much ETHICS Utilitarianism information is in state-of-the-art LLM embeddings?
For
various language models, Figure 1 shows the accuracy of a classifier based only on the leading prin-
cipal component. A high-performing setup is text-embedding-ada-002 with the single-mode
prompt “{}”, which embeds the individual scenarios with no additional prompting; this achieves
73.9% accuracy. We were surprised to see that the leading principal component achieved this level of
accuracy without explicit finetuning, because it is comparable to the 74.6% accuracy of BERT-large
after supervised finetuning on the entire ETHICS Utilitarianism training dataset (see Hendrycks
et al., 2020, Table 2). We also observe that a linear reward function using the top 10-50 principal
components is often enough to attain state-of-the-art performance. This is evidence that language
model representations capture information about human wellbeing without the need for explicit fine-
tuning. Contrasting to our best test accuracy of 81.84% with 300 principal components, Rodionov
et al. (2023) achieved an impressive 88% accuracy on the ETHICS dataset using advanced prompt-
ing alone on GPT-4, without embedding extraction or finetuning.
How does ETHICS Utilitarianism performance scale with model size?
To study this, we look
at the accuracy of different model families as the size of the model and the number of PCA compo-
nents varies; see Figure 2 and Appendix E. With 300 principal components, test accuracy within a
model family is a nondecreasing function of model size. However, with just the top principal com-
ponent, increasing the model size can hurt test accuracy; this is the case with the DeBERTa models.
Because the variance across prompts is higher when using fewer principal components (see Figure
3), we hypothesize that the nondecreasing trend observed with 300 principal components is the more
representative trend. As the trend depends on the prompt format and language model family, future
work with more prompts and language models is needed.
3

--- Page 4 ---

102
103
104
0.5
0.6
0.7
0.8
ETHICS Util test accuracy
PCA 1 dimension
cohere
gpt-3 (001 models only)
deberta
sentence-transformer
paired
single
102
103
104
Model size (in millions of parameters)
0.5
0.6
0.7
0.8
ETHICS Util test accuracy
PCA 300 dimension
cohere
gpt-3 (001 models only)
deberta
sentence-transformer
paired
single
Figure 2: How performance scales with model size: Test accuracy averaged over all prompts (y-
axis) generally increases with model size (x-axis) within a given model family, especially with a
larger number of PCA dimensions (see bottom).
Does paired evaluation mode lead to higher performance than single evaluation mode?
Based
on our human intuition, we hypothesized that paired evaluation mode would be an easier task. In
Figure 1, we see for all model families that the average performance in paired mode is indeed equal
or better than the average performance in single mode. However, the effect size is small, and the size
of the effect varies depending on the model family. Overall, we draw a low-confidence conclusion
that paired mode improves performance over single mode.
6
CONCLUSION AND FUTURE DIRECTIONS
Our research explores the encoding of human wellbeing within Large Language Model (LLM) em-
beddings, particularly focusing on how this encoding scales with model size. A key finding from
our study is the performance of the GPT-3-based model text-embedding-ada-002, which,
remarkably, competes with BERT models that have been finetuned on the entire ETHICS Utilitari-
anism dataset, solely based on its pretraining. Our analysis suggests a potential trend where model
performance improves with an increase in model size, especially when considering the number of
PCA dimensions. This observed trend, however, depends upon the family of language models em-
ployed, indicating room for further investigation.
In our experimental setup, we utilized the ETHICS Utilitarianism dataset’s training labels only at the
final logistic regression stage, opting for unsupervised embedding extraction via PCA. This method
was compared against BERT models that had been finetuned using the training labels. While this
approach yields valuable insights, it is essential to recognize the limitations inherent in the Utilitari-
anism subset and the ETHICS dataset more broadly, which present a narrowed, crowdsourced view
of the multifaceted discipline of ethics. Consequently, the performance on this dataset may not fully
reflect the complex nuances of human wellbeing or ethical reasoning.
4

--- Page 5 ---

Looking forward, conducting experiments that incorporate both supervised and unsupervised em-
bedding extraction methods across various models could elucidate the underlying reasons for the
performance disparities observed in our study. Exploring the wider ETHICS dataset may allow us
to further assess not only pleasure and pain but also broader aspects of human ethics, including
commonsense moral judgments,virtue ethics, and deontology.
7
ACKNOWLEDGEMENTS
Thanks to Steven Basart, Michael Chen, and Edmund Mills, who collaborated in related work.
Thomas Woodside, Varun Jadia, Alexander Pan, Mantas Mazeika, Jun Shern Chan, and Jiaming
Zou participated in adjacent discussions.
REFERENCES
Tolga Bolukbasi, Kai-Wei Chang, James Zou, Venkatesh Saligrama, and Adam Kalai. Man is to
computer programmer as woman is to homemaker? Debiasing word embeddings. arXiv.org,
2016. URL https://arxiv.org/abs/1607.06520.
Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal,
Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are
few-shot learners. arXiv.org, 2020. URL https://arxiv.org/abs/2005.14165.
Collin Burns, Haotian Ye, Dan Klein, and Jacob Steinhardt.
Discovering latent knowledge in
language models without supervision. arXiv.org, 2022. URL https://arxiv.org/abs/
2212.03827.
Cohere.
Embeddings, 2023.
URL https://docs.cohere.com/docs/embeddings#
how-embeddings-are-obtained.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova.
BERT: Pre-training of
deep bidirectional transformers for language understanding. arXiv.org, 2018. URL https:
//arxiv.org/abs/1810.04805.
Scott Emmons.
Contrast pairs drive the empirical performance of contrast consistent search
(CCS), 2023.
URL https://www.lesswrong.com/posts/9vwekjD6xyuePX7Zr/
contrast-pairs-drive-the-empirical-performance-of-contrast.
Pengcheng He, Jianfeng Gao, and Weizhu Chen. Debertav3: Improving deberta using electra-style
pre-training with gradient-disentangled embedding sharing. arXiv: Computation and Language,
2021. URL https://arxiv.org/abs/2111.09543.
Dan Hendrycks, Collin Burns, Steven Basart, Andrew Critch, Jerry Li, Dawn Song, and Jacob
Steinhardt. Aligning AI with shared human values. arXiv preprint arXiv:2008.02275, 2020.
URL https://arxiv.org/abs/2008.02275.
Saurav Kadavath, Tom Conerly, Amanda Askell, T. Henighan, Dawn Drain, Ethan Perez, Nicholas
Schiefer, Z. Dodds, Nova DasSarma, Eli Tran-Johnson, Scott Johnston, S. El-Showk, Andy
Jones, Nelson Elhage, Tristan Hume, Anna Chen, Yuntao Bai, Sam Bowman, Stanislav Fort,
Deep Ganguli, Danny Hernandez, Josh Jacobson, John Kernion, S. Kravec, Liane Lovitt, Kamal
Ndousse, Catherine Olsson, Sam Ringer, Dario Amodei, Tom B. Brown, Jack Clark, Nicholas
Joseph, Benjamin Mann, Sam McCandlish, C. Olah, and Jared Kaplan.
Language models
(mostly) know what they know. arXiv preprint, 2022. doi: 10.48550/ARXIV.2207.05221. URL
https://arxiv.org/abs/2207.05221.
Kevin Liu, Stephen Casper, Dylan Hadfield-Menell, and Jacob Andreas. Cognitive dissonance:
Why do language model outputs disagree with internal representations of truthfulness?
Con-
ference on Empirical Methods in Natural Language Processing, 2023. doi: 10.18653/V1/2023.
EMNLP-MAIN.291. URL https://arxiv.org/abs/2312.03729.
5

--- Page 6 ---

Pengfei Liu, Weizhe Yuan, Jinlan Fu, Zhengbao Jiang, Hiroaki Hayashi, and Graham Neubig.
Pre-train, prompt, and predict: A systematic survey of prompting methods in natural lan-
guage processing.
ACM Computing Surveys, 2021.
doi: 10.1145/3560815.
URL https:
//arxiv.org/abs/2107.13586.
Christopher D. Manning, Kevin Clark, John Hewitt, Urvashi Khandelwal, and Omer Levy. Emergent
linguistic structure in artificial neural networks trained by self-supervision. Proceedings of the
National Academy of Sciences, 2020. doi: 10.1073/PNAS.1907367117. URL https://doi.
org/10.1073/PNAS.1907367117.
Tomas Mikolov, Kai Chen, Greg S. Corrado, and Jeffrey Dean.
Efficient estimation of word
representations in vector space.
arXiv: Computation and Language, 2013.
URL https:
//arxiv.org/abs/1301.3781.
Arvind Neelakantan, Tao Xu, Raul Puri, Alec Radford, Jesse Michael Han, Jerry Tworek, Qim-
ing Yuan, Nikolas Tezak, Jong Wook Kim, Chris Hallacy, et al. Text and code embeddings by
contrastive pre-training. arXiv.org, 2022. URL https://arxiv.org/abs/2201.10005.
Alec Radford, Karthik Narasimhan, Tim Salimans, and Ilya Sutskever. Improving language un-
derstanding by generative pre-training, 2018.
URL https://openai.com/research/
language-unsupervised.
Nils Reimers and Iryna Gurevych. Sentence-BERT: Sentence embeddings using siamese BERT-
networks. arXiv.org, 2019. URL https://arxiv.org/abs/1908.10084.
Sergey Rodionov, Z. Goertzel, and Ben Goertzel. An evaluation of gpt-4 on the ethics dataset.
arXiv.org, 2023.
doi: 10.48550/ARXIV.2309.10492.
URL https://arxiv.org/abs/
2309.10492.
Patrick Schramowski, Cigdem Turan, Nico Andersen, Constantin A. Rothkopf, and Kristian Kerst-
ing. Large pre-trained language models contain human-like biases of what is right and wrong to
do. arXiv.org, 2021. URL https://arxiv.org/abs/2103.11790.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez,
Lukasz Kaiser, and Illia Polosukhin.
Attention is all you need.
arXiv.org, 2017.
URL
https://arxiv.org/abs/1706.03762.
6

--- Page 7 ---

A
ETHICS DATASET
The ETHICS dataset (Hendrycks et al., 2020) is an extensive benchmark designed to assess a lan-
guage models’ understanding of fundamental concepts in morality. It compiles a variety of natural
language scenarios reflecting everyday ethical dilemmas and moral questions, spanning five domain:
justice, wellbeing, duties, virtues, and commonsense morality. The text scenarios require integrating
physical and social world knowledge to make value judgments, highlighting the complexity of the
ethical considerations these models are expected to navigate.
Central to its creation, the dataset incorporates over 130,000 examples, carefully curated to ensure
unambiguous moral scenarios through rigorous labeling by English-speaking crowdworkers from
select countries. The construction process involved advanced techniques like counterfactual aug-
mentations and adversarial filtration, aiming to bolster the dataset’s robustness.
We focus on the utilitarianism subset, which concentrates on maximizing individual wellbeing
through the lens of pleasure and pain, mirroring the utilitarian principle of maximizing happiness
and minimizing suffering. Crowdworkers were instructed to generate and rank scenarios based on
the usual perspective of a typical person from the US. For instance, an assessment could compare
eating an apple versus a Tide pod:
S: “I ate an apple since it looked tasty and sweet, but it was sour.”
is more pleasant than
T: “I ate a Tide pod since it looked tasty and sweet, but it was sour.”
Separate workers re-rank the scenarios and eliminate sets with substantial disagreement. Overall,
the Utilitarianism subset of the ETHICS dataset contains approximately 23,000 pairs of examples
(14,000 in the train split, 5,000 test, and 4,000 test hard).
However, the ETHICS dataset quantifies moral judgments by reducing complex emotional and well-
being factors to scalar assessments, a simplification that might not capture all nuances of wellbeing,
including long-term impacts and diverse emotional responses. Additionally, its reliance on primarily
US-centric, English-speaking crowdworkers introduces cultural biases, limiting global applicability.
These issues highlight the need for more inclusive AI ethical benchmarks that encompass a broader
range of ethical frameworks and wellbeing considerations.
B
FULL LIST OF PROMPT TEMPLATES
Here is the complete list of five different prompts that we use:
{}
Consider the instantaneous pleasantness of “{}”
How pleasant is the following scenario? “{}”
“{}” is better than
“{}” is more pleasant than
Among these templates, the {} would be replaced with sample scenarios S or T from the dataset.
For instance, in the template ‘ Consider the instantaneous pleasantness of “{}” ’ becomes:
S: ‘ Consider the instantaneous pleasantness of
“I ate an apple since it looked tasty and sweet, but it was sour.” ’ or
T: ‘ Consider the instantaneous pleasantness of
“I ate a Tide pod since it looked tasty and sweet, but it was sour.” ’
7

--- Page 8 ---

C
SINGLE VS PAIRED COMPARISONS
We consider evaluating the absolute pleasantness of a scenario in isolation, which we call “single
mode.” We also evaluate the relative pleasantness of pairs of scenarios, which we call “paired mode.”
For humans, we conjecture that it is easier to evaluate pairs of scenarios relative to single scenarios.
Thus, we hypothesize that paired mode will be easier for language models.
The following two equations summarize single mode vs paired mode:
1. Single mode: φ(S, T) = P(H(f(S))) −P(H(f(T)))
2. Paired mode: φ(S, T) = P(H(f(S)) −H(f(T)))
In both equations:
• f is the prompt formatting function that substitutes the scenario(s) into the prompt template.
• H denotes the last-layer first-token activations from the model.
• P refers to normalization and PCA that further processes the activations to obtain the final
low-dimensional representation.
• φ(S, T) is input to the regression model which says whether S is more pleasant than T.
Suppose the ETHICS utilitarianism dataset has N pairs of comparisons (Si, Ti) for i = 1, . . . , N. In
single mode, PCA is performed on model activations. In paired mode, however, PCA is performed
on differences between model activations. Intuitively, this means that in paired mode, the classi-
fier operates in a space that represents comparative pleasantness between scenario pairs. In both
modes, we do normalization followed by PCA on the dataset D. Then, we learn a logistic regression
classifier on φ(S, T) indicating whether scenario S is more pleasant than scenario T.
D
MODELS
The range of language models investigated varied in type (bidirectional (Devlin et al., 2018) vs
autoregressive (Radford et al., 2018)) and size measured by parameter count within model families.
The bidirectional models include DeBERTa (He et al., 2021) and SentenceTransformers (Reimers
and Gurevych, 2019), while the autoregressive models were GPT-3 (Brown et al., 2020) and Cohere
(Cohere, 2023).
Table 1: Details of language models used, including their embedding dimensions.
Type
Vendor
Model
Dim
Bidirectional
Language Models
Microsoft
DeBERTa
microsoft/deberta-v3-xsmall
384
microsoft/deberta-v3-small
768
microsoft/deberta-v3-base
768
microsoft/deberta-v3-large
1024
Sentence
Transformers
sentence-transformers/all-MiniLM-L6-v2
384
sentence-transformers/all-MiniLM-L12-v2
768
sentence-transformers/all-mpnet-base-v2
768
Autoregressive
Language Models
OpenAI GPT-3
text-similarity-ada-001
1024
text-similarity-babbage-001
2048
text-similarity-curie-001
4096
text-embedding-ada-002
1536
Cohere
cohere/small
1024
cohere/medium
2048
cohere/large
4096
8

--- Page 9 ---

E
SUPPLEMENTAL FIGURES
We present a compilation of supplementary figures derived from our experimental results.
100
101
102
103
Number of PCA dimensions
10−5
10−4
10−3
Variance of ETHICS Util test accuracy
Variance and PCA dimensions relationship
sentence-transformer
deberta
gpt-3
cohere
large
medium
small
x-small
Figure 3: Variance of test accuracy (y-axis) versus the number of principal components (x-axis).
The variance decreases as the number of principal components increases (note that the axes are in
log scale). The primary exception to this trend is deberta increasing in variance as the number
of principal components increases from 1 to 10; we conjecture that this is because deberta with
a small number of principal components has performance that’s only a little better than random
guessing.
{}
Consider the instantaneous pleasantness of “{}”
How pleasant is the following scenario? “{}”
“{}” is better than
“{}” is more pleasant than
0.5
0.6
0.7
0.8
ETHICS Util test accuracy
0.695
0.691
0.696
0.689
0.688
random
Performance across all models by prompts
Figure 4: Test accuracy (y-axis) by prompt templates (x-axis). The violin plot displays the distri-
bution of accuracy across different models and sizes, with the overall mean accuracy indicated. We
find that most prompt templates have similar performance.
9

--- Page 10 ---

102
103
104
0.5
0.6
0.7
0.8
ETHICS Util test accuracy
PCA 1 dimension
cohere
gpt-3 (001 models only)
deberta
sentence-transformer
paired
single
102
103
104
0.5
0.6
0.7
0.8
ETHICS Util test accuracy
PCA 10 dimension
cohere
gpt-3 (001 models only)
deberta
sentence-transformer
paired
single
102
103
104
0.5
0.6
0.7
0.8
ETHICS Util test accuracy
PCA 50 dimension
cohere
gpt-3 (001 models only)
deberta
sentence-transformer
paired
single
102
103
104
Model size (in millions of parameters)
0.5
0.6
0.7
0.8
ETHICS Util test accuracy
PCA 300 dimension
cohere
gpt-3 (001 models only)
deberta
sentence-transformer
paired
single
Figure 5: Test accuracy (y-axis) for top-1, 10, 50, and 300 principal components (subplots) for
different language model families (colors) ranging in size (x-axis).
10

```
