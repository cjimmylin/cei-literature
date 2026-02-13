---
title: "2024-Unknown-A New Benchmark Dataset and Mixture-of-Experts Language Models for - PDF Extract"
source_pdf: "2024-Unknown-A New Benchmark Dataset and Mixture-of-Experts Language Models for.pdf"
pages: 55
extracted_at: "2026-02-13T09:50:28.905327"
---

# PDF Extract: 2024-Unknown-A New Benchmark Dataset and Mixture-of-Experts Language Models for

**Source PDF:** 2024-Unknown-A New Benchmark Dataset and Mixture-of-Experts Language Models for.pdf
**Total Pages:** 55

---

## Content

```
--- Page 1 ---

A New Benchmark Dataset and Mixture-of-Experts
Language Models for Adversarial Natural Language
Inference in Vietnamese
Tin Van Huynha,b, Kiet Van Nguyena,b,∗, Ngan Luu-Thuy Nguyena,b
aFaculty of Information Science and Engineering, University of Information Technology,
Ho Chi Minh City, Vietnam
bVietnam National University, Ho Chi Minh City, Vietnam
Abstract
Existing Vietnamese Natural Language Inference (NLI) datasets lack adversarial com-
plexity, limiting their ability to evaluate model robustness against challenging linguistic
phenomena. In this article, we address the gap in robust Vietnamese NLI resources
by introducing ViANLI, the first adversarial NLI dataset for Vietnamese, and propose
NLIMoE, a Mixture-of-Experts model to tackle its complexity. We construct ViANLI
using an adversarial human-and-machine-in-the-loop approach with rigorous verifica-
tion. NLIMoE integrates expert subnetworks with a learned dynamic routing mecha-
nism on top of a shared transformer encoder. ViANLI comprises over 10,000 premise –
hypothesis pairs and challenges state-of-the-art models, with XLM-R Large achieving only
45.5% accuracy, while NLIMoE reaches 47.3%. Training with ViANLI improves perfor-
mance on other benchmark Vietnamese NLI datasets including ViNLI, VLSP2021-NLI,
and VnNewsNLI. ViANLI is released1 for enhancing research into model robustness and
enriching resources for future Vietnamese and multilingual NLI research.
Keywords: Adversarial dataset, natural language inference, mixture-of-experts,
pre-trained models
1. Introduction
Natural language inference is a core task in natural language processing (NLP) that
involves determining whether a hypothesis can be logically inferred from a given premise
[1]. As a cornerstone of natural language understanding, NLI underpins various down-
stream applications such as question answering [2, 3], machine translation [4], relation
extraction [5], and text summarization [6]. With the advancement of deep learning,
transformer-based models have achieved impressive results across many NLI bench-
marks. However, studies have shown that state-of-the-art (SOTA) models remain highly
1Our dataset is available at: https://huggingface.co/datasets/uitnlp/ViANLI
∗Corresponding author
Email addresses: tihv@uit.edu.vn (Tin Van Huynh), kietnv@uit.edu.vn (Kiet Van Nguyen),
ngannlt@uit.edu.vn (Ngan Luu-Thuy Nguyen)
arXiv:2406.17716v3  [cs.CL]  23 Oct 2025

--- Page 2 ---

vulnerable to adversarial examples—inputs carefully crafted to induce incorrect predic-
tions despite being semantically coherent [7, 8]. These adversarial failures raise critical
concerns about the robustness and generalizability of NLI models, particularly when
deployed in real-world or high-stakes domains [9, 10]. As a result, constructing adver-
sarial NLI datasets has emerged as an essential direction for evaluating and improving
the reliability of NLI systems. Unlike traditional datasets, which often consist of seman-
tically transparent sentence pairs, adversarial datasets intentionally contain challenging
linguistic phenomena designed to expose model weaknesses.
Despite progress in adversarial dataset construction for high-resource languages such
as English [8] and Chinese [11], the Vietnamese language remains underrepresented.
Existing Vietnamese NLI datasets achieving high performances such as ViNLI [12], Vn-
NewsNLI [13], and VLSP2021-NLI [14] were developed using conventional annotation
pipelines and lack the adversarial design necessary for assessing model robustness. Al-
though ViNLI has played an important role in evaluating Vietnamese NLI models, it
still suffers from several weaknesses, including annotator artifacts and limited coverage
of reasoning types. To address this gap, we present ViANLI, the first adversarial NLI
dataset for the Vietnamese language. Inspired by the human-and-machine-in-the-loop
methodology [15, 8, 16], our dataset construction process involves iterative collaboration
between annotators and machine learning models. This method is also used to create
other adversarial datasets such as ANLI [8], AdversarialQA [17], and Adversarial VQA
[18]. This design enables the generation of premise–hypothesis pairs that are difficult
for models to classify, thereby enhancing both dataset complexity and linguistic cov-
erage. ViANLI consists of over 10,000 high-quality, adversarially constructed sentence
pairs and serves as a new benchmark for Vietnamese NLI evaluation.
While constructing such a dataset offers a robust evaluation benchmark, it also ne-
cessitates novel modeling strategies capable of dealing with adversarial inputs. To this
end, in addition to releasing ViANLI, we propose NLIMoE, a Mixture-of-Experts lan-
guage model tailored for adversarial NLI. NLIMoE integrates expert subnetworks with
a learned dynamic routing mechanism built on top of a shared transformer encoder (e.g.,
XLM-RoBERTa [19]), enabling the model to dynamically assign inference examples to
specialized experts. Unlike a static threshold, our routing process employs a dynamic
threshold that flexibly adjusts expert selection based on input complexity. This design
enhances the ability of the model to handle syntactic variation, semantic ambiguity, and
linguistic noise as key characteristics of adversarial data.
In this article, we have four main contributions described as follows.
• Introduction of ViANLI Dataset: We introduce ViANLI, the first adversarial NLI
dataset for Vietnamese, containing over 10,000 premise-hypothesis pairs. Created
through a human-and-machine-in-the-loop approach with rigorous human-machine
verification, ViANLI is designed to challenge state-of-the-art models, thereby en-
hancing research into model robustness and enriching resources for future Viet-
namese and multilingual NLI research.
• Proposal of NLIMoE Model: We propose NLIMoE, a Mixture-of-Experts (MoE)
language model tailored for high-complexity NLI tasks in adversarial settings. In-
tegrating expert subnetworks and dynamic routing on a shared transformer en-
coder, NLIMoE achieves a 47.3% accuracy on ViANLI, surpassing the best baseline
model (XLM-R Large) at 45.5%, setting a new benchmark for NLI performance.
2

--- Page 3 ---

• Performance Improvement on Other Benchmark NLI Datasets: Our experimen-
tal results reveal that training models such as mBERT, PhoBERT, XLM-R, and NLIMoE
with ViANLI-augmented data improves their performance on other benchmark
Vietnamese NLI datasets. This validates the dual role of ViANLI as a benchmark-
ing tool and a valuable training resource.
• Enhanced Inference Capabilities of NLIMoE: Our proposed model, NLIMoE,
demonstrates stronger inference performance, particularly when handling long
sentences and resolving entailment ambiguities. It outperforms other models in
challenging scenarios such as numerical & quantitative reasoning, reference & nam-
ing, logical inference, lexical reasoning, and external knowledge reasoning.
The structure of this article is as follows: Section 1 provides an overview of the NLI
research context, the trends in constructing adversarial datasets, and the rationale for de-
veloping an adversarial NLI dataset for Vietnamese. Section 2 reviews related datasets
and models in the field of NLI. Section 3 outlines the process of constructing our ViANLI
dataset. Section 4 presents both basic and detailed statistical analyses of the dataset. Sec-
tion 5 describes the architecture of the Mixture-of-Experts NLI model (NLIMoE) that we
designed. Section 6 discusses the experimental setup and presents the results. Section 7
provides an analysis and discussion of the experimental findings. Finally, Section 8 sum-
marizes the key conclusions of our research and suggests directions for future work.
2. Related Works
In recent years, extensive research has been conducted to produce adversarial re-
sources for various languages to aid in natural language inference. In this section, we
discuss numerous available NLI datasets (non-adversarial and adversarial datasets) and
related models for natural language inference. Additionally, we provide details of re-
sources available for other languages. Lastly, we elaborate on the research conducted on
natural language inference using various machine learning and deep learning models.
2.1. Related Datasets
Based on the data collection strategy of the NLI datasets, we divide them into adver-
sarial and non-adversarial datasets. Some well-known datasets related to NLI in other
languages are summarized and compared by us to the Vietnamese NLI datasets in Table
1.
Non-adversarial datasets: Through ongoing research efforts, researchers have re-
leased many datasets related to the field of Natural Language Inference (NLI). In par-
ticular, these datasets are generated using a variety of methodologies and languages.
This has brought many positive effects on Natural Language Understanding. In the early
stages of the development of NLI research, The Recognizing Textual Entailment (RTE)
Challenge, introduced by [20], was one of the renewed efforts aimed at formalizing the
evaluation of Natural Language Inference (NLI) tasks. The challenge created a com-
mon platform and a standardized dataset that allowed researchers to assess the ability
of computational models to recognize textual entailment. This research area exploded
in 2015, when [1] published the SNLI dataset. This is a large-scale resource introduced
by researchers at Stanford that contains nearly 600,000 sentence pairs. SNLI employs
3

--- Page 4 ---

a unique data collection method that combines crowd-sourcing with careful curation.
Quality control measures were in place to ensure the reliability and consistency of the
annotations. This methodical approach to data collection enables the creation of a large-
scale, high-quality dataset that has been crucial for benchmarking. Therefore, SNLI is
quickly considered a cornerstone in the NLI field, providing a benchmark for evaluat-
ing various machine learning models’ generalization and reasoning capabilities. The
MultiNLI (Multi-Genre Natural Language Inference) [21] dataset was developed to ad-
dress some of the limitations of the Stanford Natural Language Inference (SNLI) dataset,
including the problem of the data being relatively simple and easy for advanced machine
learning models. The authors have revised the process of building MultiNLI in several
ways to solve these issues, including using diverse sources, complex reasoning, multi-
ple domains, and better annotation guidelines. MultiNLI aims to provide a more rigor-
ous and challenging benchmark for NLI models by making these improvements. This
data construction method was quickly applied to build a series of other datasets such as
OCNLI [22], IndoNLI [23], MedNLI [24], ViNLI [12],VnNewsNLI [13], and VLSP2021-
NLI [14]. Also, there are some other approaches to building NLI data sets, such as using
question and answer data to convert to NLI data sets such as SciTail [25], FarsTail [26],
using a translator to translate NLI data from one language to another such as XNLI [27],
Hinglish [28], KorNLI [29]. Using the NLI framework to label claims based on their
logical relationships with hypotheses, researchers can create a fact-checking dataset that
enables the development and evaluation of fact-checking models and systems. There are
famous fact-checking datasets created in such a way that have been published, such as
FEVER [30], VITAMINC [31], and FEVEROUS [32].
Adversarial datasets: The growing trend of building adversarial datasets in Natural
Language Processing (NLP) has been propelled by the increasing realization that ma-
chine learning models, though powerful, are often susceptible to nuanced forms of data
manipulation. Significant efforts are underway in the field of Natural Language Infer-
ence (NLI) to construct more challenging and representative datasets. One approach to
building adversarial datasets involves generating examples specifically designed to chal-
lenge or fool existing NLI models. Adversarial examples are meant to expose the lim-
itations and vulnerabilities of existing NLI models, thereby aiding in their subsequent
fortification. According to [17], there are different approaches to building adversarial
datasets: i) adversarial filtering, where the adversarial model is typically implemented
in an isolated phase, which comes after the data creation stage. Techniques include ma-
nipulating input text by flipping, inserting, deleting, or swapping words or characters.
Perturbation data is generated to be used during adversarial training. Many studies have
combined this type of data with machine learning models and have achieved positive
results in making the model more robust; works include AdvEntuRe [33], SCPNs [34],
First-Order Logic constraints [35], ASCC [36], FreeLB [37]. In addition, on the read-
ing comprehension task, there are also datasets built according to this method such as
SWAG [38], HotpotQA [39]; ii) adversarial model-in-the-loop annotation, where both
annotators and machine learning models work iteratively in a cycle to create and refine
adversarial examples. This approach usually starts with a model initially generating ad-
versarial samples, followed by annotators reviewing, modifying, or creating new ones
based on these initial examples. This method was successfully applied to build the fa-
mous ANLI [8] dataset, as it exploited the vulnerabilities of the model very well. In the
question-answering task, there are many datasets with adversarial properties, such as
4

--- Page 5 ---

Table 1: Summary of Well-known Datasets Related to Natural Language Inference. NLI and FC Stand for
Natural Language Inference and Fact-checking, Respectively.
Dataset
NLP task
Language
Text genre
Year
Quantity
Adversarial
strategy
FEVER [30]
NLI, FC
English
Wikipedia
2018
∼185K
No
FEVER2.0 [44]
NLI, FC
English
Wikipedia
2019
1,174
Yes
VITAMINC [31]
NLI, FC
English
Wikipedia
2021
∼488K
No
FEVEROUS [32]
NLI, FC
English
Wikipedia
2021
∼87K
No
SNLI [1]
NLI
English
Image captions
2015
∼570K
No
MultiNLI [21]
NLI
English
Multi-genre
2018
∼433K
No
OCNLI [22]
NLI
Chinese
Multi-genre
2020
∼56K
No
IndoNLI [23]
NLI
Indonesian
Multi-genre
2021
∼18K
No
MedNLI [24]
NLI
English
Medical
2019
∼14K
No
SciTail [25]
NLI
English
Education
2018
∼27K
No
FarsTail [26]
NLI
Persian
Education
2021
∼10K
No
XNLI [27]
NLI
Multi-language
Multi-genre
2018
∼129K
No
Hinglish [28]
NLI
Multi-language
Movie scripts
2020
2,240
No
KorNLI [29]
NLI
Korean
Multi-genre
2020
∼950K
No
ANLI [8]
NLI
English
Multi-genre
2020
∼169K
Yes
VLSP2021-NLI [14]
NLI
Multi-language
Newswire
2022
∼20K
No
VnNewsNLI [13]
NLI
Vietnamese
Newswire
2022
∼32K
No
ViNLI [12]
NLI
Vietnamese
Newswire
2022
∼30K
No
ViANLI (Ours)
NLI
Vietnamese
Newswire
2025
∼10K
Yes
DROP [40], CODAH [41], Quoref [42], AdversarialQA [17], Quizbowl [43]. The ad-
versarial human-and-machine-in-the-loop procedure is also quickly used to create fact-
checking datasets, as seen in FEVER 2.0 [44], which addresses weaknesses of the original
FEVER dataset.
Although recent efforts have introduced several Vietnamese NLI datasets such as
ViNLI [12], VnNewsNLI [13], and VLSP2021-NLI [14], these resources were constructed
without adversarial considerations and therefore provide limited challenge for modern
models. Prior studies already report strong baselines like XLM-R Large achieving high
performance (85.99% accuracy on ViNLI, 94.79% accuracy on VnNewsNLI, and 88.69%
F1 on VLSP2021-NLI), which indicates that these datasets lack adversarial complexity to
evaluate model robustness. Although ViNLI has played an important role in evaluating
Vietnamese natural language inference models, it still suffers from several weaknesses,
such as annotator artifacts and limited reasoning diversity. To address these issues, we
introduce ViANLI, a more challenging adversarial dataset designed to better evaluate
the reasoning ability of NLP models. This motivates the construction of ViANLI as
the first adversarial NLI dataset for Vietnamese. Our approach adopts an adversarial
human-and-machine-in-the-loop paradigm, where humans and models iteratively col-
laborate to generate and refine examples. This design not only increases dataset dif-
ficulty but also allows annotators to expose model vulnerabilities during the creation
process, yielding a more reliable benchmark for robust reasoning.
The research gaps identified in existing Vietnamese NLI datasets are as follows. First,
there is a significant absence of adversarial NLI datasets specifically for the Vietnamese
language, which hinders the evaluation of model robustness against challenging linguis-
tic phenomena in this low-resource context. Second, current Vietnamese NLI datasets,
such as ViNLI, VLSP2021-NLI, and VnNewsNLI, lack the iterative human-model collab-
5

--- Page 6 ---

oration needed to incorporate diverse adversarial elements like syntactic variations and
semantic ambiguities, resulting in over-optimistic performance metrics for state-of-the-
art models. Third, multilingual adversarial datasets overlook language-specific cultural
and contextual inferences relevant to Vietnamese, limiting their applicability and trans-
ferability. These gaps directly align with the objectives of this article, which include
introducing ViANLI as the first adversarial Vietnamese NLI dataset to challenge mod-
els and proposing NLIMoE as a specialized Mixture-of-Experts model to handle such
complexities, thereby improving robustness and performance on both adversarial and
benchmark NLI datasets.
2.2. Related NLI Models
Research topics in NLP, including NLI, have witnessed the daily development of ma-
chine learning models from simple models to more complex ones. The diverse evolution
of current machine learning models has enriched the choices of models for experimen-
tation, suitable for the characteristics of different tasks and data domains. Moreover, as
more adversarial NLI datasets emerge, the performance of these models also needs to
increase significantly.
In its early stages, probability-based models have historically laid the groundwork
for approaches to natural language inference and have established a foundation long
before the emergence of current deep learning techniques. These models operated on
the principle of computing the likelihoods of hypotheses given premises, often rooted
in Bayesian inference [20, 45]. Latent Semantic Analysis (LSA) [46] uses Singular Value
Decomposition (SVD) to compress space and discover semantic relationships between
words and documents. LSA can be used to measure the semantic similarity between a
premise and a hypothesis [47]. CBOW (Continuous Bag of Words) and Skip-gram are
two architectures introduced in the Word2Vec model [48] to learn vector word repre-
sentations. Both of these techniques aim to learn word representations that can capture
semantics based on the context in which the word appears, and these methods have
also yielded promising results on the NLI task [1, 21, 22, 23, 12]. Although these models
offered valuable information, they often struggled to capture intricate semantic relation-
ships and nuances in language.
The challenges and shortcomings of these probabilistic approaches paved the way for
neural models, especially with the advent of deep learning. Neural models, such as Re-
current Neural Networks (RNNs) [49], Long Short-Term Memory Networks (LSTMs)
[50], and ESIM [51], have achieved promising results on NLI tasks. Recently, trans-
former architectures such as BERT [52] and GPT [53] have demonstrated an unprece-
dented ability to capture complex semantic structures and relationships. Their capacity
to represent words in dense vector spaces, process sequences, and utilize attention mech-
anisms has made them exceptionally adept at tasks like NLI. In addition to these models,
a series of variant models have emerged using the BERT architecture, such as RoBERTa
[54], XLM-R [19], XLNet [55], ALBERT [56], DistilBERT [57], ELECTRA [58], and T5
[59], and have achieved high performance on datasets such as SNLI [1], MultiNLI [21],
FEVER [30], and ANLI [8].
Building upon the resounding success of previous transformer-based models on En-
glish data, considerable efforts have been made to extend their capabilities to other lan-
guages, including Vietnamese. The PhoBERT model [60], for example, represents a sig-
nificant advance by leveraging the foundation of BERT and fine-tuning it on Vietnamese
6

--- Page 7 ---

data, yielding impressive performance across various tasks. Additionally, earlier models
trained on multilingual data, including Vietnamese, such as mBERT [52], XLM-R [19],
mT5 [61], CafeBERT [62], and mBART [63], have also demonstrated excellent results on
Vietnamese Natural Language Inference (NLI) tasks [12].
Mixture-of-Experts (MoE) models have emerged as an effective approach for ad-
dressing complex NLP tasks, where single models often fail to capture the diverse as-
pects of data. MoE architectures consist of multiple sub-models (experts), each special-
izing in specific data types or tasks, along with a routing mechanism to allocate inputs
to the appropriate expert. This approach enables efficient handling of complex data
distributions and enhances overall performance. MoE has been successfully applied to
various NLP tasks, including machine translation [64], text summarization [65], and
text generation [66]. For instance, Switch Transformers [67], GShard [68], MoCE [69],
and M-BLS [70] demonstrate the effectiveness of MoE architectures in processing large
datasets and improving model robustness by leveraging conditional computation for ef-
ficient scaling, thus adeptly managing diverse linguistic phenomena. However, training
and deploying MoE models require substantial computational resources, and designing
effective routing mechanisms remains a primary research challenge.
Unlike large-scale MoE architectures such as Switch Transformers [67], GShard [68],
which primarily emphasize scalability for general-purpose language modeling, our work
introduces NLIMoE tailored for adversarial NLI in a low-resource language. While prior
studies have leveraged conditional computation mainly for efficiency, NLIMoE adopts a
dynamic routing mechanism specifically aimed at enhancing robustness against adver-
sarial linguistic phenomena. Specifically, NLIMoE integrates a shared transformer en-
coder (e.g., XLM-RoBERTa) with dynamically selected sub-networks, allowing different
experts to specialize in handling syntactic variations, semantic ambiguity, and linguistic
noise in Vietnamese. This design enables the model to achieve stronger performance
on the adversarial dataset and highlights the potential of MoE architectures for complex
inference tasks in low-resource languages.
3. Dataset
3.1. Task Definition
The task of Adversarial Natural Language Inference in the Vietnamese language aims
to rigorously evaluate and enhance the robustness of language models in discerning
logical semantic relationships based on complex and adversarial linguistic constructs.
This task is defined as follows.
• Input: A pair of Vietnamese sentences, comprising a premise, extracted from di-
verse news articles, and a corresponding hypothesis, meticulously crafted to probe
model reasoning capabilities.
• Output: A label of the logical relationship between the premise and hypothesis into
one of three classes: entailment, where the hypothesis is logically derivable from
the premise; contradiction, where the hypothesis negates the premise; or neutral,
where the hypothesis neither supports nor contradicts the premise.
7

--- Page 8 ---

Required
Label (rL)
Phase 3.1: Write hypothesis
(H) sentence to generate a
sample (P,H,rL)
Premise
(P)
Phase 3.2: Give (P, H) to a
pre-trained model to predict
label (pL)
Phase 3.3: Compare the
rL and pL labels, these
two labels must be
different
Phase 3.4: The annotator
adjusts H until the model
predicts incorrectly.
Phase 4.1: Verify 1st by human to
make sure H is written correctly for rL
Collect sample
data (P, H, rL)
into adversarial
dataset
Phase 3: Hypothesis generation
>= 2 correct 
verifications
< 2 correct 
verifications
Phase 4.2: Verify 2nd by LLM to
make sure H is written correctly
for rL in Dev and Test set
Train
Dev
Test
Large
Language
Model
Phase 4: Human-Machine Verification
GPT-4.0
Expert
If the LLM detects that H is
written incorrectly for rL, H will
be forwarded to an Expert for
review.
Modify H
Keep H
Correct
Incorrect
Phase 2: 
Annotator Recruitment 
and Training
Phase 1: 
Premise Data Collection
Figure 1: Overall Process for the Creation of the ViANLI Dataset.
3.2. Dataset Creation
We propose a new approach using the human-and-machine-in-the-loop integrated
with human-machine verification for constructing the ViANLI dataset. This approach
integrates both human annotators and machine learning models to generate and verify
data, addressing the challenges of current data collection methods related to the com-
plexity and quality of the dataset. The process is illustrated in Figure 1 and consists
of four key phases: Premise Data Collection (see Section 3.2.1), Annotator Recruitment
and Training (see Section 3.2.2), Hypothesis Generation (see Section 3.2.3), and Human-
Machine Verification (see Section 3.2.4).
3.2.1. Phase 1: Premise Data Collection
In the creation of the ViANLI dataset, the premise sentences were extracted from
news content sourced from VnExpress1, a popular Vietnamese online news platform that
covers a wide range of topics. The news content was selected to ensure diversity in the
premise sentences, with a focus on 13 domains such as business, tourism, technology,
news, science, entertainment, law, sports, health, life, education, world, and vehicles.
This diversity provides a solid foundation for generating hypothesis sentences that cover
different topics and complexity levels.
1https://vnexpress.net/
8

--- Page 9 ---

3.2.2. Phase 2: Annotator Recruitment and Training
Fifteen students participated in the ViANLI dataset generation process. The students
we hired were from famous universities in Vietnam. They are native speakers with good
language skills, enough knowledge, and awareness to read premise sentences and write
hypothesis sentences. Similar to the ViNLI dataset, we built an initial guideline to teach
students how to write hypothesis sentences to create hypothesis-premise adversarial
pairs of sentences. In addition, annotators were explicitly trained to use diverse inference
categories (Numerical and Quantitative Reasoning; Reference and Names; Standard
Logical Inferences; Lexical Reasoning; Tricky Linguistic Inferences; External Knowledge
Reasoning; and Cultural and Contextual Inferences) to ensure that the generated pairs
achieved a high level of adversarial difficulty. These types of inferences are clearly de-
fined in Section 4.5.
Annotators went through at least five rounds of hypothesis writing to be able to par-
ticipate in the development of ViANLI officially. In each round, they have to write 50
hypotheses corresponding to 50 premise sentences covered on three labels: entailment,
contradiction, and neutral. The data completed at each round of annotators is manually
checked by us to ask them to correct any errors, and it was also time for them to practice
writing their sentences. In the process of checking the data, we also constantly update
and edit the guidelines to ensure consistency between the annotators. Besides, we used
the XLM-RLarge baseline model, which achieved the highest performance on ViNLI to
evaluate the data annotators generated in each round. We always required annotators
to write hypotheses on a high difficulty level so that the prediction success rate on XLM-
RLarge is below 40%. We returned the prediction results of the model to the annotators
to help them study how the model encounters difficulties with the data characteristics
to improve writing for the next time. Once the annotators’ data generation capabilities
stabilized, they were selected to formally participate in our data-building process. At
the end of this process, we selected 15 students, as mentioned above. They were paid
$0.025 for writing a hypothesis.
3.2.3. Phase 3: Hypothesis Generation
• Phase 3.1 - Writing Hypothesis: Annotators are provided with a premise (P) and
tasked with writing a corresponding hypothesis (H) for the required label (rL),
which can be one of three labels: entailment, contradiction, or neutral. To write
complex hypothesis sentences that challenge machine learning models, they may
incorporate various types of inferences, such as numerical and quantitative rea-
soning, coreference and name-based inference, basic logical relations (e.g., nega-
tion, causality, comparison), lexical inference (e.g., synonyms, antonyms), tricky
inferences (e.g., wordplay, syntactic transformations), reasoning based on external
knowledge, and cultural or contextual inferences grounded in Vietnamese norms.
• Phase 3.2 - Model Prediction: The (P, H) pair is input into a pre-trained machine
learning model on a natural language inference task to predict an inference label
(pL).
• Phase 3.3 - Label Comparison: After model prediction, the predicted label (pL) is
compared with the required label (rL) to evaluate the ability of the model to infer
the semantic relationship between the premise and hypothesis. If the two labels
9

--- Page 10 ---

match, it means that the model has correctly identified the semantic relationship,
and the sample is considered not complex enough to challenge the model. In this
case, the H is moved to Phase 3.4 to adjust the hypothesis sentence and make it
more complex. On the other hand, if the labels differ, it indicates that the sample is
sufficiently complex to mislead the model. To ensure the accuracy of the generated
sample, it is moved to Phase 4, where the validation process begins.
• Phase 3.4 - Annotator Adjustment: In cases where the model predicts correctly,
annotators adjust the hypothesis (H) until the model produces the incorrect pre-
diction (Return to Phase 3.1). This phase focuses on refining the hypothesis to
expose the weaknesses of the model.
The hypothesis generation process is conducted over three rounds, with each round
utilizing a different pre-trained NLI model in Phase 3.2 to predict inference labels for
the premise–hypothesis pairs. We selected models with progressively stronger infer-
ence capabilities, as reported in the ViNLI benchmark [12], for each round. This grad-
ual increase in model strength is intended to encourage annotators to generate more
diverse and challenging sentence pairs that are difficult enough to mislead the model.
Furthermore, the data generated in each round is used to fine-tune a new model, which
is subsequently used to evaluate the hypotheses in the next round. The models and their
corresponding training datasets for each round are summarized in Table 2.
Table 2: Fine-tuning Models and the Corresponding Training Datasets Used in Each Round.
Round
Fine-tuning Model
Training Dataset
1
mBERT
ViNLI, XNLI
2
PhoBERTLarge
ViNLI, XNLI, VnNewsNLI, ViA1
3
XLM-RLarge
ViNLI, XNLI, VnNewsNLI, VLSP2021-NLI, ViA1, ViA2
• Round 1 - ViA1 Data: In the first round, We fine-tuned the mBERT model [52],
which was trained on the ViNLI dataset [12], along with 7,500 Vietnamese sam-
ples from the XNLI dataset [27], to predict labels for the premise-hypothesis pairs
generated by the annotators. The data generated in this round is referred to as
ViA1.
• Round 2 - ViA2 Data: In the second round, we utilized the PhoBERT model [60],
which outperformed mBERT on various tasks. The model was trained on a com-
bination of the ViNLI dataset, 7,500 Vietnamese samples from XNLI, and the data
generated in Round 1 (ViA1). To improve its understanding of Vietnamese NLI
tasks, we also included the VnNewsNLI dataset [13]. The data generated in this
round is referred to as ViA2.
• Round 3 - ViA3 Data: In the third round, the premise sentences remained the
same as in the previous rounds. In this round, we used the XLM-R model [19]
to predict the inference labels for the new premise-hypothesis pairs. To improve
the robustness of the model, we trained XLM-R on a larger dataset compared to
the previous rounds. The training data for XLM-R included the ViNLI dataset,
7,500 Vietnamese samples from XNLI, data generated in Rounds 1 (ViA1) and 2
(ViA2), the VnNewsNLI dataset, and over 10,000 pairs from the VLSP2021-NLI
dataset [14]. The data generated in this round is referred to as ViA3.
10

--- Page 11 ---

3.2.4. Phase 4: Human-Machine Verification
• Phase 4.1 - First verification by human: The first verification ensures that the hy-
pothesis (H) sentence is written correctly according to the required label (rL). In
this phase, each premise-hypothesis pair (P, H) is relabeled by three other anno-
tators. If two or more annotators agree with the original annotator, the sample is
considered correct and added to the dataset. Conversely, if fewer than two anno-
tators agree with the original annotator, the sample is removed.
• Phase 4.2 - Second verification by machine and expert: We perform an additional
round of annotation on test and development patterns to ensure accurate labelling.
The hypotheses (H) in the development and test sets are verified to ensure it is cor-
rectly written according to the required label (rL) for creating accurate premise-
hypothesis pairs. A Large Language Model (LLM), specifically GPT-4 [71], is em-
ployed to evaluate the correctness of H. If the LLM determines that H is written
incorrectly for rL, the sample is forwarded to an expert for review. The expert then
assesses H: if deemed correct, H is retained as is; if incorrect, the expert modifies
H to align with rL, ensuring the quality of the dataset.
4. Dataset Analysis
In this section, we analyze ViANLI from multiple perspectives to better understand
its characteristics. We provide statistical insights into dataset size and the distribution
of sentence lengths in both premises and hypotheses. We further examine word repeti-
tion and the introduction of new vocabulary in hypothesis generation. In particular, we
highlight the linguistic features captured through diverse inference types, which play a
crucial role in assessing vocabulary diversity and contribute significantly to the overall
difficulty of the dataset.
4.1. Initial Statistic
After completing the data construction process, we obtained three datasets (ViA1,
ViA2, ViA3) corresponding to the three rounds. Combining the data from these rounds,
we created the Vietnamese adversarial dataset (ViANLI), which consists of over 10,000
premise-hypothesis pairs sourced from more than 700 online news articles. Statistical
analysis reveals that the distribution of labels across the training, development, and test
sets is balanced, a result of our deliberate efforts during data construction to minimize
bias and enhance the learning capability of models. Additionally, we categorized the
samples by various text genres, with the business genre having the highest number of
instances at 947, while the vehicles genre had the lowest at 605. Nevertheless, the vari-
ation in sample counts across the 13 genres remains relatively minor overall. Detailed
statistics of the dataset are presented in Table 3. The data is distributed in a ratio of 8:1:1
for the training, development, and test sets, respectively.
11

--- Page 12 ---

Table 3: Dataset Statistics of the ViANLI Dataset.
Dataset Statistic
Train
Dev
Test
Total
#Sample
ViA1 (Round1)
2,609
330
330
3,269
ViA2 (Round2)
2,672
330
330
3,332
ViA3 (Round3)
2,731
340
340
3,411
ViANLI (Total)
8,012
1,000
1,000
10,012
#Label
Entailment
2,615
334
334
3,283
Contradiction
2,473
333
333
3,139
Neutral
2,924
333
333
3,590
#Topic
Business
783
74
90
947
Tourism
717
89
101
907
Technology
690
78
72
840
News
674
92
83
849
Science
673
84
87
844
Entertainment
603
90
71
764
Law
603
80
64
747
Sports
602
70
77
749
Health
550
72
73
695
Life
548
76
79
703
Education
544
69
72
685
World
536
62
79
677
Vehicles
489
64
52
605
Table 4: The Model Error Rate Represents the Percentage of the Incorrect Predictions of the Model on the Data
per Round in Phase 3. Verify 1 Success Rate Is the Percentage of Successful Confirmations on the Data Samples
That the Data Model Predicts Incorrectly in Phase 4.1.
Dataset
Model error rate (%)
Verify 1 success rate (%)
ViA1 (Round1)
51.65
77.59
ViA2 (Round2)
44.93
94.27
ViA3 (Round3)
41.98
94.71
ViANLI (Total)
46.18
88.86
Furthermore, as outlined in the data-building process for each round, we employed
progressively stronger models to evaluate the data generated in each round. The goal
was to identify more challenging adversarial patterns by focusing on the samples that
the model misclassifies. The model error rate decreases with each round, indicating that
the accuracy of the models in Phase 3.2 improves over time as shown in Table 4. This
means that the data pairs that mislead the model and are misclassified in later rounds
become increasingly difficult and complex.
Additionally, the success rate of Verification 1 increased significantly from 77.59%
in Round 1 to 94.71% in Round 3. This shows that the number of premise-hypothesis
pairs that successfully fool the model and are confirmed as correct by the annotators
has risen, reflecting an improvement in the annotators’ hypothesis generation quality
over successive rounds. Each data sample for each round is illustrated in Table A.17 (in
Appendix A).
12

--- Page 13 ---

Table 5: The Mean Length of Premise and Hypothesis Sentences on ViANLI and ViNLI.
Mean word length
Dataset
ViA1
ViA2
ViA3
ViANLI
ViNLI
Premise
24.4
25.3
25.0
24.9
24.5
Hypothesis
14.3
14.4
14.6
14.4
18.1
4.2. Length Distribution
We calculate the sentence lengths of both premise and hypothesis in our dataset using
the VnCoreNLP tool [72], which performs word segmentation for Vietnamese text. After
segmentation, we count the number of words in each sentence to determine its length,
following the same approach used in the ViNLI dataset. In addition, we compare the
sentence lengths in our dataset with those in the ViNLI dataset to analyze differences in
sentence complexity and structure.
As shown in Figures B.12a, B.12b, and B.12c in Appendix B (corresponding to the
data from Round 1, Round 2, and Round 3), the length of the hypothesis sentences is
distributed within a shorter range compared to the premise sentences. These three charts
also demonstrate that the annotators’ writing remains consistent in terms of difficulty,
with the hypothesis sentences tending to be shorter than the premise sentences.
When comparing ViANLI with ViNLI, Figures B.12d and B.12e in Appendix B show
a common trend: the length of hypothesis sentences is generally shorter than that of
premise sentences in both datasets. However, a closer look at these graphs and the data
presented in Table 5 reveals that the hypothesis sentences in ViANLI are significantly
shorter than those in ViNLI, while the premise sentence lengths are quite similar across
both datasets.
The authors of MultiNLI [21] and ViNLI [12] suggest that shorter hypothesis sen-
tence lengths, such as those found in the SNLI dataset, may lead to more predictable
data. While the hypothesis sentences in ViANLI are indeed shorter than those in ViNLI,
we have ensured the challenge and difficulty of the dataset through model error rate
evaluations in each round, as shown in Table 4. The impact of sentence length on model
accuracy is further analyzed in Section 7.3.
4.3. Word Overlap Rate
We calculate the word overlap rate (WOR) between the premise and hypothesis sen-
tences in the ViANLI adversarial dataset to investigate the extent to which annotators
reuse vocabulary from the premise sentence when constructing the hypothesis sentence.
This analysis is crucial for assessing the difficulty of the dataset, as previous studies
[12, 73] have indicated that word overlap can significantly impact the predictive ability
of models. To measure the word overlap, we use the Jaccard metric, which calculates
the unordered word overlap between the premise and hypothesis. Before calculating
the Jaccard value, we apply the VnCoreNLP toolkit for Vietnamese word segmentation.
The Jaccard measure between a pair of premise and hypothesis sentences is calculated
by the Equation (1).
Jaccard =
|P ∩H|
|P| + |H| −|P ∩H|
(1)
13

--- Page 14 ---

Where, premise and hypothesis sentences are represented in two lists of words, re-
spectively, as follows: P = [WP1, WP2, WP3, ..., WPn], H = [WH1, WH2, WH3, ..., WHm].
|P∩H| is the number of words that appear in both premise and hypothesis sentences. |P|
is the number of words in the sentence premise. |H| is the number of words in the sen-
tence hypothesis. |P∪H| is the number of words in the premise and hypothesis sentences
after the duplicates are removed. An example of word overlap between the premise and
hypothesis sentences for the entailment label is shown in Figure 2.
Premise: Việc khai_thác Bitcoin có_thể tiêu tốn hàng tỷ kilowatt điện, chủ_yếu từ
nhiên_liệu hóa_thạch - nguyên_liệu phát thải khí carbon lớn nhất. (Bitcoin mining can consume
billions of kilowatts of electricity, mainly from fossil fuels, which are the biggest carbon emitters.)
Sentence Pair of the Entailment Label
Hypothesis: Việc khai_thác Bitcoin gây ảnh_hưởng xấu đến với môi_trường rất nhiều
bởi_vì thải ra khí carbon. (Bitcoin mining is very harmful to the environment because it releases carbon
dioxide.)
Figure 2: Example of Word Overlap in the Premise-hypothesis Pair of the Entailment Label. Where the Green
Highlight Is the Same Words, the Red Highlight Is the New Words That Only Appear in the Hypothesis Sen-
tence.
Table 6 presents the average Jaccard value for each dataset after calculating the word
overlap for each premise-hypothesis pair. In general, when observing the word overlap
rate across each round of data and the entire ViANLI dataset, we found that the overlap
rate for the entailment label is the lowest, compared to the higher overlap rates for the
contradiction and neutral labels. This suggests that when writing entailment hypothe-
ses, annotators tend to use fewer words directly from the premise sentence. This dis-
tribution trend in Table 6 overcomes the weaknesses of previous studies, such as ViNLI
[73], which has shown that models tend to predict semantic relationships more accu-
rately when there is a high word overlap rate, particularly for the entailment label. There-
fore, to enhance the adversarial nature of ViANLI, annotators were deliberately inten-
tional to limit the reuse of premise words when crafting hypothesis sentences, making
it more challenging for models to rely solely on lexical overlap for accurate predictions.
To gain a more precise understanding of the impact of word overlap on model accuracy,
we provide further analysis in Section 7.4.
Table 6: The Word Overlap Rate in ViANLI Compares to That in ViNLI.
Label
Jaccard (%)
ViA1
ViA2
ViA3
ViANLI
ViNLI
Entailment
23.72
21.36
20.62
21.85
29.88
Contradiction
32.80
30.53
30.56
31.23
23.30
Neutral
30.82
31.97
30.92
31.22
20.19
14

--- Page 15 ---

Table 7: The New Word Rate in ViANLI Compares to That in ViNLI.
Label
New word rate (%)
ViA1
ViA2
ViA3
ViANLI
ViNLI
Entailment
50.95
53.44
54.31
52.95
46.59
Contradiction
36.82
39.78
40.61
39.17
53.96
Neutral
41.65
40.21
42.10
41.34
61.79
4.4. New Word Rate
In contrast to the word overlap rate, we analyze the new word rate in ViANLI. This
refers to the proportion of new words in the hypothesis sentence—words that do not
appear in the premise sentence. This statistic provides insight into the linguistic diver-
sity of annotators when generating hypothesis sentences. We calculate the ratio of new
words for each round and for the entire ViANLI dataset. The VnCoreNLP toolkit is also
applied to segment the Vietnamese text before calculating the new word rate. The results
are presented in Table 7, broken down by the three labels: entailment, contradiction, and
neutral.
The new word rate for the entailment hypothesis is the highest, while the lowest
rate is observed in the contradiction hypothesis, both for the per-round data and the
entire ViANLI dataset. When comparing ViANLI with ViNLI, notable differences are
observed. In the ViNLI dataset, the highest new word rate is associated with the neutral
label, and the lowest rate with the entailment label. Additionally, except for the fact that
the proportion of new words in the entailment label of ViANLI is higher than that of
ViNLI, the new word rate for the contradiction and neutral labels in ViANLI is signifi-
cantly lower than in ViNLI. The new word rate is also an important factor influencing the
performance of machine learning models, and its impact is further analyzed in Section
7.5.
Khi
lo_lắng
thái_quá và
không
làm
chủ
được
cảm_xúc , Kendall_Jenner thấy
chân_tay
tê_liệt .
Kendall_Jenner cảm_thấy
cơ_thể
tê
cứng
khi
bồn_chồn
trong
người .
POS-tag = 
Premise:
POS-tag = 
Hypothesis:
N
V
A
Cc
R
V
V
R
N
Np
V
N
V
Np
V
N
A
A
N
A
E
N
Legend POS-tags
N: Noun
V: Verb
A: Adjective
Cc: Coordinating conjunction
Np: Proper noun
E: Preposition
R: Adjunct
Figure 3: Example of POS-tag in the Premise-hypothesis Pair of the Entailment Label. The Red Words in the
Hypothesis Tree Are New Words, and the Arrows Represent Changes in the Position and Function of the Word.
15

--- Page 16 ---

To better understand the trend in word usage by annotators when writing hypothesis
sentences, we use PhoNLP [74] to identify the part of speech (POS) of new words in the
hypothesis sentences. We then calculate the percentage of each POS category for visual-
ization. PhoNLP recognizes several POS categories, but for clarity, we summarize them
into main word types, including Nouns, Verbs, Adjectives, Prepositions, Adjuncts, and
Others (combining the remaining types). Figure 4 illustrates the new word rate by Part-
of-Speech in ViANLI. Statistical results reveal that the usage of words is quite consistent
across all three labels, with Nouns and Verbs representing the largest proportions. Fur-
thermore, annotators tend to use more Nouns when writing entailment hypotheses. On
the other hand, adjectives are rarely used when writing hypothesis sentences. An illus-
trative example of the POS-tag analysis on new words in a hypothesis sentence is shown
in Figure 3.
Website Visits
Site Traffic Sources
Noun
31.8%
Verb
26.5%
Other
15.6%
Adjunct
9.4%
Preposition
8.4%
Adjective
8.2%
ENTALIMENT
Website Visits
Site Traffic Sources
Noun
28.9%
Verb
28%
Other
15%
Adjunct
10.8%
Preposition
9%
Adjective
8.3%
CONTRADICTION
Website Visits
Site Traffic Sources
Verb
27.8%
Noun
27.7%
Other
15.2%
Adjunct
11.1%
Preposition
9.4%
Adjective
8.8%
NEUTRAL
Figure 4: The New Word Rate by Part-of-Speech in ViANLI.
4.5. Inference Types
To investigate the linguistic characteristics of the ViANLI dataset, we conducted a
detailed analysis of the inference types present in the development sets of each round
(ViA1, ViA2, and ViA3) as well as the entire ViANLI development set. We categorized
the premise-hypothesis pairs into seven distinct inference types. Six of these types were
adapted from the inference ontology proposed in the ANLI study [8], with descriptions
tailored to account for the nuances of the Vietnamese language. Additionally, recogniz-
ing the unique cultural and contextual features of Vietnamese, we introduced a seventh
inference type, cultural and contextual inference, to capture reasoning based on cultural
knowledge, such as understanding social hierarchies, traditional practices, or context-
specific implicatures, which are prevalent in Vietnamese communication.
The seven inference types used in our analysis are defined as follows:
• Numerical and Quantitative Reasoning (NaQR): Inferences involving numerical
information, such as cardinal and ordinal numbers, dates, ages, or quantitative
comparisons, etc. (e.g., "60 minutes is 1 hour", "from February 1 to February 6
lasts 5 days").
• Reference and Names (RaN): Inferences requiring resolution of coreference (e.g.,
linking pronouns like "anh ấy - he" or "cô ấy - she" to specific individuals) or un-
derstanding attributes associated with proper names, such as gender, etc.
16

--- Page 17 ---

• Standard Logical Inferences (SLI): Reasoning based on logical structures, includ-
ing conjunctions (e.g., "và - and"), negations (e.g., "không - not"), cause-and-effect
relationships, comparatives, or superlatives, etc.
• Lexical Reasoning (LR): Inferences derived from lexical relationships, such as
synonyms (e.g., "vui vẻ- happy" and "hạnh phúc - delighted"), antonyms (e.g.,
"lớn - large" vs. "nhỏ- small"), etc.
• Tricky Linguistic Inferences (TLI): Inferences that involve sophisticated linguis-
tic strategies, such as wordplay, syntactic restructuring, or deducing the speaker’s
intent from subtle contextual cues, etc.
• External Knowledge Reasoning (EKR): Inferences that rely on external or world
knowledge not explicitly stated in the premise, such as geographical facts (e.g.,
"You cannot travel directly from Hanoi to the sea") or general knowledge about
Vietnamese society, etc.
• Cultural and Contextual Inference (CaCI): Inferences grounded in Vietnamese
cultural norms, traditions, or implicit meanings unique to the language (e.g., "miền
Tây" refers to the Mekong Delta, where people face challenges like salinity intru-
sion "hạn mặn - salinity drought"), etc.
The analysis of inference types utilized by annotators in the ViANLI dataset, as sum-
marized in Table 8, reveals distinct trends in the creation of adversarial premise-hypothesis
pairs across the ViA1, ViA2, and ViA3 rounds, with an overall average across the entire
ViANLI Dev Set. Standard Logical Inferences dominate with a consistent average of
72.51%, indicating a strategic emphasis on basic logical structures to challenge natural
language inference (NLI) models. External Knowledge Reasoning remains a stable com-
ponent, averaging 43.01% with minor increases (42.35%–43.63%), suggesting a reliance
on world knowledge to introduce complexity. Notably, Numerical & Quantitative Rea-
soning shows a gradual increase from 22.12% (ViA1) to 27.35% (ViA3), reflecting an
adaptive strategy to incorporate quantitative challenges as models evolve. Conversely,
Tricky Linguistic Inferences decline from 14.54% (ViA1) to 9.71% (ViA3), hinting at a
shift away from intricate linguistic strategies. Cultural & Contextual Inference, averag-
ing 10.09% with a peak of 11.21% (ViA1) and a small dip to 10.09% (ViA3), underscores
the annotators’ effort to leverage Vietnam-specific cultural nuances. This trend suggests
that annotators initially explore cultural elements but later prioritized logical and quan-
titative challenges, potentially reflecting model adaptation over the rounds.
Table 8: Inference Type Distribution (%) on the Dev Set for Each Round and Averages Across the Entire ViANLI
Dev Set.
Round
NaQR
RaN
SLI
LR
TLI
EKR
CaCI
ViA1
22.12
11.21
72.12
20.30
14.54
43.63
11.21
ViA2
24.54
6.06
74.84
24.24
9.69
43.03
8.18
ViA3
27.35
12.64
70.58
20.58
9.71
42.35
10.88
ViANLI
24.67
9.97
72.51
21.71
11.31
43.01
10.09
17

--- Page 18 ---

Annotators were allowed to use one or more inference types when writing hypothe-
ses in order to increase semantic richness and adversarial difficulty. Figure 5 shows the
distribution of the number of inference types combined in the ViANLI Dev Set. The re-
sults indicate that most hypotheses combine two inference types (72.6%), while a single
inference type accounts for 17.2%, and three inference types account for only 10.2%. This
analysis highlights that annotators often rely on multiple inference strategies rather than
a single one. The impact of combining inference types on model performance is further
analyzed in Section 7.7.
#Inference
Percentage (%)
0
20
40
60
80
1
2
3
Figure 5: Analysis of the combination ratio of Inference Types on the ViANLI Dev Set.
5. Our Proposed Model
In this section, we present the architecture of our proposed NLIMoE (Mixture-of-
Experts language model) for natural language inference, which is designed to effectively
handle the complexities and challenges posed by adversarial NLI datasets. This archi-
tecture allocates tasks to specialized experts based on the complexity of the input data,
enabling the model to focus on different linguistic aspects. By combining the power of
XLM-RoBERTa with a dynamic routing mechanism, the model adapts to various linguis-
tic challenges. The architecture of NLIMoE is shown in Figure 6.
18

--- Page 19 ---

x1
Ex1
Premise
Hypothesis
[CLS]
E[CLS]
x...
Ex...
xn
Exn
[SEP]
E[SEP]
y1
Ey1
y...
Ey...
ym
Eym
[SEP]
E[SEP]
Pooling Layer
Dynamic Router
FFN 3
FFN 4
FFN 5
FFN 2
FFN 1
Add & Normalize
Linear
Softmax
Class Probabilities 
(Entailment, Contradiction, Neutral)
Encoder Block
Input
Embedding
Input
Positional
Embedding
Multi-head Attention
Add & Norm
Feed Forward
Add & Norm
XLM-Roberta
Encoder
Positional
Encoding
Input
Embedding
Sentence Pair
Embedding
Linear
Dropout
ReLU
Feed-Forward
Network
Input
Mixture-of-Experts
Block
Classification 
Layer
Hx1
H[CLS]
Hx...
Hxn
H[SEP]
Hy1
Hy...
Hym
H[SEP]
Xx1
X[CLS]
Xx...
Xxn
X[SEP]
Xy1
Xy...
Xym
X[SEP]
S = 1024-dim embedding
Dynamic threshold
FFN 6
FFN 7
p = 0.23
p = 0.17
p = 0.17
p = 0.27
Input Sentence Pair
Input
Representation
Figure 6: Our Proposed Model NLIMoE - A Mixture of Experts Model for Natural Language Inference Lever-
aging XLM-RoBERTa Encoder with Dynamic Routing Method.
Figure 6 illustrates the overall architecture of NLIMoE. It consists of several sub-
modules: (i) Input Representation, where the premise and hypothesis are tokenized
and embedded, then combined with positional encodings; (ii) Encoder Block, imple-
mented by XLM-RoBERTa, which produces contextualized embeddings; (iii) Pooling
Layer, which aggregates token embeddings into a fixed-size sentence pair vector; (iv)
Mixture-of-Experts Block, which contains two main components: the Dynamic Router
(computing expert selection probabilities and applying a dynamic threshold), the Feed-
Forward Network Experts (specialized subnetworks that process the routed inputs);
and (v) Classification Layer, which predicts entailment, contradiction, or neutral.
Input Representation: The premise and hypothesis sentences are tokenized into sub-
word units using a pre-trained tokenizer. Let the premise and hypothesis sequences con-
sist of n and m tokens, respectively. The tokenized input, including special tokens [CLS],
[SEP] (separating premise and hypothesis), and [SEP] (terminating hypothesis), forms
a sequence of length n + m + 3. This sequence is embedded into a vector space using the
pre-trained XLM-RoBERTa tokenizer, producing a embedding E ∈R(n+m+3)×d, where d
is the embedding dimension. Positional encodings P ∈R(n+m+3)×d are added to capture
token order, resulting in the combined representation X = E + P, where X ∈R(n+m+3)×d
serves as the input to the encoder block.
19

--- Page 20 ---

Encoder Block: The encoder block processes the input representation X ∈R(n+m+3)×d
using the XLM-RoBERTa encoder, which consists of multiple transformer layers. Each
layer applies multi-head self-attention to capture semantic relationships between the
premise and hypothesis tokens, followed by feed-forward networks (FFNs) to trans-
form the attention output into a higher-level representation. The output of the encoder
block is a contextualized representation H ∈R(n+m+3)×d, where each row corresponds to
the contextualized embedding of a token in the input sequence.
Pooling Layer: The pooling layer aggregates the contextualized representation H ∈
R(n+m+3)×d from the encoder block into a fixed-size sentence pair embedding. We apply
mean pooling to compute the average representation across all tokens in the sequence,
including the special tokens [CLS] and [SEP]. Specifically, the sentence pair embedding
S ∈Rd is obtained by averaging all rows of H (see Equation (2)).
S =
1
n + m + 3
n+m+3
X
i=1
hi
(2)
where hi ∈Rd is the i-th row of H. This vector S represents a 1024-dimensional em-
bedding that captures the aggregated semantic representation of the premise–hypothesis
pair. By integrating information from all tokens, it serves as the input to the Mixture-of-
Experts block.
Mixture-of-Experts Block: This block is central to the NLIMoE model, designed to
tackle complex linguistic tasks by dynamically assigning inputs to specialized experts.
• Dynamic Router Mechanism: The router determines which expert(s) process a
given input. We use a softmax function to compute the probability distribution
across the available experts based on vector S, selecting the most appropriate ex-
pert based on linguistic features such as syntactic complexity, semantic ambigu-
ity, or adversarial noise. Unlike a static threshold—where the value is predefined
and remains fixed throughout the entire training process—we propose a dynamic
threshold mechanism consisting of two main steps: (1) computing the expert se-
lection probabilities, and (2) adjusting the Dynamic Threshold based on the com-
plexity of the input.
To generate gate values and directly normalize them into a probability distribution
over experts in a single step using the gate layer Wg ∈Rd×num_experts applied to S,
followed by the softmax function to obtain the probability distribution over the
experts, as calculated in Equation (3).
Pi =
exp  (WgS + bg)i

Pnum_experts
j=1
exp  (WgS + bg)j

(3)
where S ∈Rd is the pooled sentence-pair embedding via Equation ( 2), Wg ∈
Rd×num_experts and bg ∈Rnum_experts are the gating parameters, and Pi denotes the
probability of selecting expert i for a given input sample.
To estimate the complexity of the input for dynamic expert selection, we introduce
an additional complexity gate layer Wc ∈Rd×1 with bias bc ∈R. This layer takes
the pooled sentence-pair embedding S ∈Rd, which is obtained by averaging the
20

--- Page 21 ---

contextualized token representations from the encoder. The complexity score C is
then computed by applying a sigmoid activation, as in Equation (4).
C = σ(WcS + bc)
(4)
where σ denotes the sigmoid function, which bounds C between 0 and 1.
The dynamic threshold ρdynamic is then computed as a combination of a static thresh-
old ρstatic and the complexity score C (defined in Equation (4)), scaled by a coeffi-
cient γ, as in Equation (5).
ρdynamic = ρstatic + γ · C
(5)
where ρstatic is a fixed baseline threshold, γ is a scaling coefficient, and C is derived
from the pooled sentence-pair embedding S ∈Rd via Equation (4). For inputs
with higher complexity (larger C), the threshold ρdynamic increases, thus fewer ex-
perts will be activated. This encourages the model to focus on the most specialized
experts, thereby improving its ability to handle challenging samples.
To determine which experts are selected, we compare the gate probability Pi (from
Equation (3)) against ρdynamic. A binary mask Mi is then defined as Equation (6).
Mi =

1,
if Pi > ρdynamic,
0,
otherwise.
(6)
Here Mi indicates whether expert i is activated for a given input. The mask is ap-
plied across all experts for each sample in the batch, forming a binary selection
matrix. Experts with Mi = 1 are activated, while those with Mi = 0 remain inac-
tive.
• Feed-Forward Networks: Once the router determines the active experts, the pooled
sentence-pair embedding S ∈Rd (defined in Equation (2)) is passed to the cor-
responding Feed-Forward Networks (FFNs). Each FFN is specialized to capture
certain aspects of inference, such as complex linguistic relations. The i-th expert ap-
plies a Linear transformation, followed by Dropout for regularization, and a ReLU
activation to introduce non-linearity. The output of the i-th expert is computed as
Equation (7).
FFNi(S) = ReLU Dropout(WeiS + bei)
(7)
where S is the pooled representation from the encoder, Wei ∈Rd×d and bei ∈Rd
are the parameters of the i-th expert. The Dropout layer enhances generalization,
while the ReLU activation ensures non-linear transformations.
• Computation in MoE Block: After computing the outputs of the individual Feed-
Forward Networks (FFNs) for the active experts, the Mixture-of-Experts (MoE)
block aggregates them to produce a unified representation. The pooled embed-
ding S ∈Rd serves as the common input to all experts. The final MoE output O is a
21

--- Page 22 ---

weighted sum of the expert outputs FFNi(S), weighted by the corresponding gate
probabilities Pi and masked by Mi as in Equation (8).
O =
num_experts
X
i=1
Mi · Pi · FFNi(S)
(8)
where Mi is the binary mask from Equation (6), Pi is the gate probability from
Equation (3), and FFNi(S) is the output of the i-th expert defined in Equation (7).
To ensure numerical stability and proper normalization, the weighted sum is di-
vided by the sum of the active gate probabilities, as in Equation (9).
O =
Pnum_experts
i=1
Mi · Pi · FFNi(S)
Pnum_experts
i=1
Mi · Pi
(9)
This normalization ensures that the contribution of each active expert is appropri-
ately scaled, allowing the MoE block to effectively integrate the specialized knowl-
edge from the selected experts into a cohesive output for downstream processing.
Classification Layer: After obtaining the unified representation O from the MoE
block (Equation (9)), which is directly passed through a LayerNorm layer to stabilize
training and enhance the robustness of the representation. This normalized output is
then fed into the classification layer, which applies a linear transformation followed by a
softmax activation function to predict the class probabilities for each premise-hypothesis
pair. The classification layer computes the probabilities of the three labels: entailment,
contradiction, and neutral. The entire process is expressed in Equation (10).
P(class) = softmax

Wcls · LayerNorm(O) + bcls

(10)
where O ∈Rd is the MoE block output for a given input sample, Wcls ∈Rnum_labels×d
and bcls ∈Rnum_labels are the parameters of the classification layer, and LayerNorm(O)
denotes the layer-normalized representation.
Loss Computation: The loss function of the model is designed to optimize the classi-
fication performance while ensuring efficient and balanced expert selection in the Mixture-
of-Experts (MoE) framework.
• Cross-Entropy Loss (Lossce): This is the primary loss for the sequence classifica-
tion task, measuring the difference between the predicted logits and the ground
truth labels. It is calculated using the cross-entropy loss function to ensure the
model accurately predicts class probabilities for premise-hypothesis pairs, as shown
in Equation (11).
Lossce = CrossEntropyLoss(logits, labels)
(11)
Where logits represents the raw output scores from the classification layer before
applying softmax (Equation (10)), and labels denotes the ground truth labels for
for each input pair.
22

--- Page 23 ---

• Dynamic Loss (Lossd): To encourage the model to select only the minimal nec-
essary set of experts for each premise–hypothesis pair, an entropy-based dynamic
loss is applied. This loss minimizes the entropy of the gate probability distribu-
tion, promoting a more focused selection of experts similar to the previous study
[75], and is computed as in Equation (12).
Lossd = −
1
num_experts
num_experts
X
i=1
Pi · log(Pi)
(12)
where Pi is the gate probability of the i-th expert, and num_experts denotes the
total number of experts in the probability distribution for each input sample. In
practice, this entropy is computed for every sample and then averaged across the
batch. This penalty reduces routing uncertainty, encouraging the model to activate
fewer experts for simpler inputs while still allowing multiple experts for complex
cases.
• Load Balance Loss (Lossb): To ensure an even distribution of workload across
experts for each premise-hypothesis pair, a load balance loss is incorporated. This
loss penalizes imbalances between the fraction of samples assigned to each expert
and the average gate probabilities, which was applied in previous studies [75, 67,
68], calculated as in Equation (13).
Lossb = num_experts ·
num_experts
X
i=1
fi · Qi
(13)
where fi is the mean fraction of samples assigned to the i-th expert (computed as
the mean of the expert mask across the batch), and Qi is the mean gate probabil-
ity for the i-th expert across the batch. specifically, fi and Qi are calculated as in
Equations (14) and (15).
fi = 1
B
B
X
j=1
M ji
(14)
Qi = 1
B
B
X
j=1
P ji
(15)
where B is the batch size. Here, M ji corresponds to the binary expert mask intro-
duced in Equation (6), indicating whether expert i is activated for the j-th sample,
and Pji denotes the gating probability defined in Equation (3) for expert i given
the j-th input.
• Final Loss (Loss): The final loss is a weighted combination of the cross-entropy
loss, dynamic loss, and load balance loss (see Equation 16), allowing the model to
balance classification accuracy with expert selection efficiency.
Loss = Lossce + α · Lossd + β · Lossb
(16)
23

--- Page 24 ---

where α and β are hyperparameters (set to 1e −3 and 1e −2 respectively in the
code) that control the contribution of the dynamic and load balance losses. This
composite loss ensures the model learns to classify accurately while optimizing the
dynamic routing mechanism and maintaining load balance among experts.
6. Experiments and Results
In this section, we present the design of the main experiments to address the follow-
ing questions: whether our dataset is more complex than previous datasets, whether it
poses challenges to current models, and whether our proposed NLIMoE model outper-
forms other models. Detailed information regarding the datasets used, the selection and
configuration of baseline models, and the evaluation metrics for performance measure-
ment are also provided.
6.1. Benchmark Datasets
We combine the ViANLI dataset with other datasets to train machine learning mod-
els. These trained models are then used to evaluate our adversarial data, as well as sev-
eral other datasets. This allows us to assess both the challenge posed by the adversarial
data we have created and the effectiveness of using such data against attacks in the other
datasets. The datasets combined with the ViANLI data include ViNLI [12], XNLI [27],
VLSP2021-NLI [14], and VnNewsNLI [13]. Due to the varying nature and structure
of these datasets, we reorganized and subdivided them to fit our experimental design.
Specifically, XNLI and VLSP2021-NLI are multilingual inference datasets. Therefore, we
extracted only Vietnamese samples for inclusion in the training data. Additionally, the
authors of the VnNewsNLI and XNLI datasets developed only the development and test
sets. Consequently, we used 90% of the dev set for training and the remaining 10% for
model tuning. Furthermore, we allocated 10% of the training set from VLSP2021-NLI
for model tuning during the training process. Details of the sample sizes in each dataset
used for the experiment are presented in Table 9.
Table 9: Quantity Statistics of the Datasets in Our Main Experiment. ViANLI Dataset Is Aggregated Data from
ViA1, ViA2, and ViA3.
Dataset
Quantity
Train
Dev
Test
ViA1
2,609
330
330
ViA2
2,672
330
330
ViA3
2,731
340
340
ViANLI
8,012
1,000
1,000
ViNLI
24,376
3,009
2,991
XNLI
6,750
750
-
VLSP2021-NLI
7,816
869
2,118
VnNewsNLI
18,221
2,025
11,866
24

--- Page 25 ---

6.2. Baseline Models
In our experiments, we focus on using state-of-the-art transformer models, including
mBERT [52], XLM-R [19], CafeBERT [62], and PhoBERT [60]. The mBERT, XLM-R, and
CafeBERT models are powerful multilingual transformer models trained on large doc-
ument corpora, while PhoBERT is a monolingual transformer model developed specif-
ically for Vietnamese. Since Vietnamese uses both single words (one token) and com-
pound words (multiple tokens), we use the VnCoreNLP tool [72] to tokenize the Viet-
namese text, ensuring proper word segmentation for PhoBERT input.
Additionally, the hyperparameters selected for mBERT, XLM-R, CafeBERT, and PhoBERT
during model training are designed to optimize performance for most models after eval-
uation. The basic parameters are as follows: max_length=256, learning_rate=1e-05,
eval_frequency=400, batch_size=16, weight_decay=0.0, adam_epsilon=1e-08, dropout=0.4.
Furthermore, we set epochs=7 since this yielded the best accuracy for the models. Re-
ducing the number of epochs resulted in suboptimal performance, while increasing the
epochs led to either saturation or a decline in model accuracy.
For our proposed NLIMoE model, in addition to the above hyperparameters, we in-
troduce specific configurations for the Mixture-of-Experts (MoE) block. We set the num-
ber of experts to 7 and employ a dynamic routing mechanism to select an appropriate
number of experts for each input. The dynamic threshold (ρstatic) is defined by combin-
ing a static threshold ρstatic = 0.1 with an input complexity score scaled by γ = 0.1. The
coefficients of the additional loss terms are set to α = 1e-3 for the dynamic loss and β =
1e-2 for the load balance loss, which provided the best trade-off between accuracy and
expert utilization. This configuration enables NLIMoE to leverage conditional compu-
tation while maintaining robustness against adversarial inputs.
In addition, to compare NLIMoE with dynamic routing, we also implement a Top-K
routing variant, where the top K experts with the highest probabilities are selected. The
values of N (total experts) and K (selected experts) are dataset-dependent and tuned
separately for each case. Specifically, we set N = 5 and K = 4 for experiments on ViANLI,
while N = 13 and K = 9 were used for ViNLI.
6.3. Evaluation Metrics
We employ both accuracy and F1-score (macro average) as evaluation metrics to as-
sess the performance of the models, aligning with the approach used in the ViNLI evalu-
ation [12]. These metrics provide a comprehensive analysis of model effectiveness, with
accuracy measuring the proportion of correctly predicted samples and F1-score offer-
ing a balanced assessment of precision and recall across label categories. The accuracy
metric is formally defined in Equation (17), while the F1-score is detailed in Equation
(18).
Accuracy = C
N
(17)
where N is the total number of samples evaluated, and C is the number of samples
that the model correctly predicted.
F1macro = 1
L
L
X
i=1
F1l
(18)
25

--- Page 26 ---

where L is the total number of labels, and F1l is the F1-Score for each label l, calculated
as in Equation (19).
F1l = 2 · Precisionl · Recalll
Precisionl + Recalll
(19)
where Precisionl =
TPl
TPl+FPl is the precision for label l (with TPl as true positives and
FPl as false positives), and Recalll =
TPl
TPl+FNl is the recall for label l (with FNl as false
negatives).
6.4. Experimental Results
NLIMoEDynamic model performance is better than baseline models, and ViANLI
dataset is more challenging than previous dataset. Table 10 presents the results of
our main experiment. The objective is to compare and evaluate the performance of
our proposed NLIMoEDynamic model against baseline models such as mBERT, PhoBERT,
CafeBERT, and NLIMoETopK on the ViANLI dataset, which we developed, as well as
on the ViNLI dataset. This comparison highlights the challenges posed by our dataset
compared to previous datasets and demonstrates the versatility of our model across ad-
versarial and traditionally constructed datasets like ViNLI.
In this experiment, we evaluated two different input representations for the model:
word-based and syllable-based. For the word-based model, we used PhoBERT, while
the other models were based on syllable-based representations. To preprocess the Viet-
namese text for the PhoBERT model, we used the VnCoreNLP tool [72] for word seg-
mentation.
The results in Table 10 indicate that the ViANLI dataset presents more challenges to
the models compared to ViNLI, as the accuracy of all models on the ViANLI dataset is
significantly lower than on ViNLI. Notably, when comparing our model with the others,
on the development set of ViANLI, CafeBERT achieved 48.2%, NLIMoETopK achieved
48.3%, which is lower than the 49.2% of our model. On the test set, this discrepancy
becomes even more pronounced, with our model reaching 47.3%, nearly 2% higher than
the highest-performing baseline model, XLM-RLarge.
In addition, the NLIMoEDynamic model not only performs better on the ViANLI dataset
but also outperforms other models on ViNLI. On the development set, NLIMoEDynamic
achieved 83.59%, surpassing XLM-RLarge and CafeBERT by 0.57% and 1.42%, respec-
tively. On the test set, NLIMoEDynamic achieved 82.82%, outperforming XLM-RLarge by
1.46%. In general, when comparing the performance of the same model on both datasets,
the ViANLI dataset proves to be more challenging for the models to predict semantic re-
lationships accurately compared to ViNLI. Our model has shown greater effectiveness
in handling the more complex cases presented by our dataset.
26

--- Page 27 ---

Table 10: Model Performance on Two Benchmark Datasets including ViANLI and ViNLI. Results marked with
* are extracted from the study of [12]. DifAcc is the Abbreviation for the Accuracy Difference Between the
ViNLI and ViANLI Datasets.
Models
Dev
Test
ViNLI
ViANLI
DifAcc
ViNLI
ViANLI
DifAcc
Acc
F1-score
Acc
F1-score
Acc
F1-score
Acc
F1-score
Word
PhoBERTBase
75.07*
75.08*
45.20
43.12
29.87
72.87*
72.79*
44.30
41.92
28.57
PhoBERTLarge
77.33*
77.34*
46.80
44.27
30.63
75.93*
75.87*
44.90
41.51
31.03
Syllable
mBERT
67.41*
67.46*
44.00
41.99
23.41
64.84*
64.83*
42.50
39.41
22.34
XLM-RBase
72.02*
71.99*
46.90
42.54
25.12
71.59*
71.51*
44.80
39.88
26.79
XLM-RLarge
83.02*
82.98*
47.00
45.75
36.02
81.36*
81.31*
45.50
44.18
35.86
CafeBERT
82.17
82.15
48.20
47.93
33.97
82.51
82.49
45.10
44.98
37.41
NLIMoETopK
83.54
83.54
48.30
47.80
35.24
82.55
82.56
46.70
46.10
35.85
NLIMoEDynamic
83.59
83.60
49.20
47.24
34.39
82.82
82.83
47.30
44.92
35.52
Continuously augmenting training data with ViANLI improves model performance
on other datasets. Table C.18 (in Appendix C) presents the results of another experi-
ment we conducted to evaluate the ability of combining ViANLI with other datasets
to enhance reasoning capabilities and recognize semantic relationships across datasets
during the training process. The experimental results reveal many interesting findings
about the performance of the models and the characteristics of the adversarial data we
have created.
The models selected for evaluation are also the ones involved in the data generation
process, including mBERT, PhoBERT, XLM-R, and our proposed model NLIMoEDynamic.
As we gradually increased the training data by sequentially adding ViA1, ViA2, and
ViA3, the performance of the models improved incrementally with each addition. This
indicates that each additional round of adversarial data made the models more robust
and better equipped to handle data attacks, especially on the test sets of ViANLI and
VLSP2021-NLI.
Moreover, when combining the entire ViANLI dataset with all other datasets (ViNLI,
XNLI, VLSP2021-NLI, VnNewsNLI) to create a large training set, models including mBERT,
PhoBERT, XLM-R, and NLIMoEDynamic showed significant performance improvements
on datasets such as VLSP2021-NLI and VnNewsNLI. However, this combination inad-
vertently introduced noise, which reduced the effectiveness of the models when evalu-
ated on the ViANLI dataset. Overall, ViANLI still demonstrates that incorporating this
dataset into the training process helps the model learn more complex semantic relation-
ships, thereby improving its ability to handle and reason over other datasets. However,
a model that achieves high accuracy on these datasets may still fail when evaluated on
ViANLI.
Data in rounds become increasingly more challenging. We train NLIMoEDynamic on
an increasing amount of data from different rounds and evaluate the performance of
the model on the data from each round, as well as on the entire ViANLI dataset. This
experiment, presented in Figure 7, helps us specifically assess the impact of the amount
of training data on the predictive power of our model and the challenge of the data built
27

--- Page 28 ---

ViA1
ViA2
ViA3
Development set
40
42
44
46
48
50
52
54
Accuracy (%)
Training Data
ViA1
ViA1 + ViA2
ViA1 + ViA2 + ViA3
(a) Dev
ViA1
ViA2
ViA3
Test set
40
42
44
46
48
50
Accuracy (%)
Training Data
ViA1
ViA1 + ViA2
ViA1 + ViA2 + ViA3
(b) Test
Figure 7: Accuracy (%) of the Proposed NLIMoE Model on the dev and test sets of ViANLI in each round
(ViA1, ViA2, ViA3). NLIMoEDynamic Model is Trained with Incremental Training Data.
in each round.
The results of this experiment show that as the model is trained on an increasing
amount of adversarial data, the performance of the NLIMoEDynamic model strengthens,
with accuracy generally improving on the dev and test sets of ViA1, ViA2, ViA3, and
even ViANLI. This indicates that as the model is exposed to more adversarial data, it
improves its ability to handle attacks from such data.Besides, we observe that for all
three training cases of the NLIMoEDynamic model, the accuracy of the model gradually
decreases on both the Dev and Test sets through each round. This reinforces the fact
that the difficulty of the data is increasing. If this data-building process continues for fu-
ture rounds, it generates increasingly high-quality and challenging data. This is of great
significance in maintaining the challenge and attractiveness of the NLI task, thereby en-
couraging more future research rather than relying on a static data-building process.
7. Results Analysis and Discussion
In this section, we present a comprehensive analysis of the experimental results to
highlight the characteristics of the ViANLI dataset and evaluate the performance of the
proposed NLIMoEDynamic model in comparison with other NLI baselines. Our evaluation
addresses several key aspects of model design and data complexity. Specifically, we ex-
amine whether the proposed dynamic routing with a dynamic threshold outperforms
both static thresholding and traditional Top-K routing. We also investigate the sensi-
tivity of NLIMoEDynamic to ablation studies, and assess the impact of sentence length on
model stability relative to other NLI models. Furthermore, we analyze whether word
overlap between premise and hypothesis simplifies the NLI task or highlights the ad-
vantages of NLIMoEDynamic, and whether a high rate of new words presents challenges
that NLIMoE can better handle. We also consider the influence of potential annotator
artifacts in hypotheses on dataset difficulty. In particular, we evaluate the effectiveness
of NLIMoEDynamic across diverse linguistic features through inference types present in
ViANLI. Finally, we analyze model error patterns to identify areas for improvement,
providing insights into enhancing robustness and performance on complex Vietnamese
NLI tasks.
28

--- Page 29 ---

7.1. Ablation Studies
To evaluate the effectiveness of each component in our proposed NLIMoE model,
we conduct a comprehensive set of ablation studies on ViANLI and ViNLI. The pri-
mary objective of these experiments is to quantify the contribution of the auxiliary loss
terms—namely the dynamic loss (α) and the load-balance loss (β)—to the overall model
performance. We further investigate the impact of the routing regularization coefficient
(γ), which interacts with input complexity to determine the dynamic selection thresh-
old for experts. In addition, we examine the role of dropout regularization in controlling
overfitting within the expert networks, and assess the direct impact of the Mixture-of-
Experts (MoE) block itself compared to a standard transformer encoder.
We systematically vary the weighting coefficients of the auxiliary losses, including α
for the dynamic loss, β for the load-balance loss, and γ for the dynamic router mecha-
nism. We also adjust the dropout rate within the expert networks and compare model
variants trained with and without the MoE block. Accuracy on both datasets is showed
in Table 11.
For the dynamic loss coefficient α, the best performance is obtained at α = 1e−3
(49.20% on ViANLI and 83.59% on ViNLI). Both smaller and larger values reduce accu-
racy, indicating that a moderate level of entropy regularization is crucial for stable and
diverse expert routing. The load-balance loss coefficient β achieves the best results at
β = 1e−2, which balances the workload across experts while still allowing sufficient spe-
cialization. Increasing or decreasing β away from this value leads to load imbalance and
performance drops. For the routing regularization coefficient γ, moderate values with
1e−1 produce the most consistent improvements by dynamically adjusting the threshold
to activate an appropriate number of experts for each input. In contrast, higher values
of γ raise the threshold excessively, resulting in fewer selected experts and reduced flex-
ibility, which significantly degrades performance.
Dropout also plays a critical role, especially when a rate of 0.4 consistently yields
the strongest results across both datasets, effectively balancing overfitting and underfit-
ting within the expert networks. Furthermore, the comparison between variants with
and without the MoE block highlights the substantial contribution of the expert mecha-
nism itself. Incorporating MoE leads to clear performance gains, with improvements of
+1.4% on ViANLI and +1.1% on ViNLI. These results confirm that dynamic expert rout-
ing introduces complementary modeling capacity beyond the base transformer encoder,
enabling the model to specialize in diverse inference patterns and handle adversarially
challenging inputs more effectively.
29

--- Page 30 ---

Table 11: Ablation study results of the proposed NLIMoE model on ViANLI and ViNLI datasets across dif-
ferent hyperparameters (Alpha - α, Beta - β, Gamma - γ, Dropout) and model configurations (with/without
MoE).
Dataset
Ablation Studies
Alpha (α)
w/o
5e-4
1e-3
2e-3
5e-3
1e-2
ViANLI
46.80
46.90
49.20
47.30
46.40
47.00
ViNLI
82.61
83.32
83.59
82.66
82.44
82.31
Beta (β)
w/o
2e-3
5e-3
1e-2
2e-2
5e-2
ViANLI
44.40
46.90
45.60
49.20
46.10
40.60
ViNLI
82.00
82.83
83.14
83.59
82.88
82.17
Gamma (γ)
w/o
1e-2
5e-2
1e-1
1.5e-1
2e-1
ViANLI
47.10
47.70
47.10
49.20
46.70
44.5
ViNLI
82.26
82.48
83.23
83.59
81.59
80.33
Dropout
w/o
0.1
0.2
0.3
0.4
0.5
ViANLI
46.90
48.10
47.10
47.80
49.20
47.60
ViNLI
82.66
82.88
83.10
83.06
83.59
83.14
Mixture-of-Experts Block
w/o MoE
MoE
ViANLI
47.80
49.20 (↑1.40)
ViNLI
82.48
83.59 (↑1.11)
7.2. Comparing NLIMoE with Dynamic and Top-K Routing
We conducted comprehensive experiments to evaluate the effectiveness of our pro-
posed NLIMoE with dynamic routing compared to Top-K routing. The design of expert
quantity and Top-K selection are crucial factors in optimizing Mixture-of-Experts mod-
els, as they directly affect the ability of the model to specialize and capture complex
inference relations. To explore the best configuration, we varied both the number of ex-
perts (N) and the Top-K value on the ViANLI and ViNLI datasets, and systematically
compared the results with our dynamic routing approach. In addition, we explicitly
included Top-1 and Top-2 routing, which correspond to the strategies used in Switch
Transformer [67] and GShard [68], respectively, to contextualize our method against
prior advances in MoE architectures.
Table 12 presents the performance of the models on both the development and test
sets of ViANLI and ViNLI. On the ViANLI dataset, the optimal configuration was ob-
tained with 5 experts and Top-K = 4, achieving 48.30% on the development set and
46.70% on the test set. Reducing the number of experts to 3 or increasing it to 7, 9, 11, or
13 resulted in suboptimal accuracy. This suggests that ViANLI benefits from a moderate
30

--- Page 31 ---

number of experts combined with a carefully chosen Top-K value. In contrast, for the
ViNLI dataset, the best results with Top-K routing were achieved with 13 experts and
Top-K = 9, yielding 83.54% on the development set and 82.55% on the test set. Lower
expert counts, such as 11, 9, 7, 5, or 3, consistently led to reduced performance. This
indicates that ViNLI requires a larger number of experts and a higher Top-K value to
fully leverage the advantages of MoE routing.
Another important observation is that sparse Top-K routing generally outperformed
dense routing, where all experts are activated simultaneously. This finding demon-
strates the importance of careful and selective expert activation rather than relying on full
expert utilization, which can lead to computational inefficiency without corresponding
performance gains.
When compared with our NLIMoE using dynamic routing, the proposed model con-
sistently outperformed nearly all Top-K routing configurations on both ViANLI and
ViNLI. In particular, our approach achieved higher accuracy than Top-1 and Top-2 rout-
ing, which replicate the strategies of Switch Transformer and GShard. With 7 experts,
NLIMoE with dynamic routing demonstrated superior effectiveness, showing a stronger
ability to capture diverse linguistic inference patterns. These results confirm that our
proposed dynamic routing mechanism provides more robust and adaptive expert uti-
lization compared to recent MoE architectures, thereby establishing the innovation and
contribution of NLIMoE in advancing Mixture-of-Experts approaches for natural lan-
guage inference.
31

--- Page 32 ---

Table 12: Impact of Expert Quantity (#Expert) and Top-k Expert Selection of Top-K Routing on Model Accu-
racy and Computational Efficiency on ViANLI and ViNLI Datasets compared to Dynamic Routing. Top-1†
corresponds to the approach of Switch Transformer [67], while Top-2§ corresponds to the approach of GShard
[68].
NLIMoE
ViANLI
ViNLI
Routing Method
#Expert
#TopK
Dev
Test
Dev
Test
Top-K Routing
3
Sparse
1†
36.60
35.20
83.05
82.26
2§
48.20
45.40
83.28
82.38
Dense
3
47.40
44.70
83.19
82.46
5
Sparse
1†
48.20
46.70
82.79
81.71
2§
47.70
45.30
82.97
82.28
3
47.00
46.30
83.06
81.97
4
48.30
46.70
82.57
82.03
Dense
5
48.20
44.40
83.15
81.97
7
Sparse
1†
47.80
46.10
82.53
82.11
2§
47.30
47.40
83.23
82.06
3
47.20
46.20
82.97
82.38
5
48.30
45.10
82.84
81.80
Dense
7
47.80
45.10
82.79
82.46
9
Sparse
1†
48.00
46.40
83.02
82.41
2§
46.60
46.20
82.88
81.66
3
46.60
42.60
82.66
82.37
5
48.30
45.10
82.84
81.40
7
47.90
43.90
83.19
81.41
Dense
9
47.90
45.30
83.45
82.39
11
Sparse
1†
47.40
46.00
83.10
81.45
2§
47.60
46.60
82.83
82.32
3
47.10
44.70
83.15
81.71
5
48.10
46.20
82.48
82.14
7
46.10
45.70
83.19
82.33
9
48.00
45.70
82.93
82.37
Dense
11
48.20
44.10
83.31
82.24
13
Sparse
1†
48.30
45.80
83.37
82.46
2§
48.10
45.20
83.23
82.44
3
47.70
46.30
83.15
82.45
5
47.30
46.00
83.46
82.15
7
48.00
44.90
83.49
82.50
9
47.60
45.80
83.54
82.55
11
47.30
46.70
83.37
82.37
Dense
13
47.90
45.60
83.02
79.95
Dynamic Routing (Ours)
49.20
47.24
83.59
82.82
32

--- Page 33 ---

7.3. Do the Lengths of Premise and Hypothesis Affect the Model Performances?
Figure 8 clearly illustrates the effect of premise sentence length on the accuracy of
different models, including our NLIMoEDynamic model, in the ViANLI dataset. From the
chart, it is evident that shorter premise sentences (1-5 words) generally lead to higher
accuracy for most models, including mBERT, XLM-R, CafeBERT, and PhoBERT, with our
model (NLIMoEDynamic) also performing better at shorter lengths. However, the perfor-
mance of all models shows a sharp decline in accuracy as the premise length increases,
especially beyond 15 words, indicating a significant challenge with longer sentences.
This drop in accuracy highlights how the increasing complexity of longer premises in-
troduces more difficult inferences with potential adversarial samples. specific, models
such as mBERT, PhoBERT, and XLM-R experience a sharp decline in accuracy when the
premise length in range of 16-20 words. As the length continues to increase beyond 20
words, the accuracy of the models slightly increases. In general, it is clear that as the
premise sentence length increases, the data becomes more complex, making it harder
for the models to handle.
Surprisingly, when comparing NLIMoEDynamic with other models, our model demon-
strates superior stability compared to all other models with an accuracy of about 57%
when the length of the premise sentence is at its highest with over 35 words. This
demonstrates that NLIMoEDynamic is more robust to high sentence lengths, which may be
attributed to its Mixture-of-Experts (MoE) architecture, enabling it to handle sentence
complexity more effectively.
1-5
6-10
11-15
16-20
21-25
26-30
31-35
>35
Premise length (Words)
40
45
50
55
60
65
Accuracy (%)
0
5
10
15
20
Quantity ratio (%)
0.3
1.9
9.6
19.5
23.3
17.6
13.0
14.8
mBERT
XLM-R
CafeBERT
PhoBERT
NLIMoEDynamic
NLIMoETopK
Quantity ratio
Figure 8: Premise Sentence Length Affects the Accuracy of Models.
Figure 9 illustrates the relationship between hypothesis sentence length and model
accuracy. When the hypothesis is short (1–5 words), most models perform poorly. As
the hypothesis length increases from 6 up to more than 35 words, the accuracy of all base-
line models fluctuates considerably, with the exception of NLIMoEDynamic. Thanks to its
flexible expert selection mechanism, NLIMoEDynamic maintains stable performance as
sentence length grows. In particular, for longer hypotheses (26–35 words), our model
achieves the highest accuracy among all compared models. Notably, in the 31–35 word
range, mBERT, PhoBERT, XLM-R, CafeBERT, and NLIMoETopK all suffer a sharp drop in
accuracy, while NLIMoEDynamic continues to improve. These results demonstrate that hy-
pothesis length strongly influences task difficulty, as longer sentences introduce greater
structural and semantic complexity that many models struggle to process. However,
33

--- Page 34 ---

our Mixture-of-Experts architecture with dynamic routing effectively mitigates this chal-
lenge, highlighting its advantage in handling long, complex, and adversarial data in Viet-
namese NLI.
1-5
6-10
11-15
16-20
21-25
26-30
31-35
>35
Hypothesis length (Words)
20
25
30
35
40
45
50
55
Accuracy (%)
0
5
10
15
20
25
30
35
40
Quantity ratio (%)
1.0
20.0
40.2
23.8
9.5
3.6
1.1
0.8
mBERT
XLM-R
CafeBERT
PhoBERT
NLIMoEDynamic
NLIMoETopK
Quantity ratio
Figure 9: Hypothesis Sentence Length Affects the Accuracy of Models.
7.4. Does Word Overlap Affect the Model Performances?
In the process of constructing the NLI dataset, one important issue is that annotators
may reuse words from the premise sentence when writing the hypothesis. This reuse
of words can serve as a straightforward indicator, helping the model easily identify the
semantic relationship between the premise and hypothesis, as the shared words in both
sentences create a clear similarity. However, this also reduces the difficulty and complex-
ity of the data, as the model may rely on the word overlap to determine the relationship
without needing to perform deeper inference. Therefore, we conducted a performance
analysis of various models based on the word overlap ratio to comprehensively assess
the difficulty of the ViANLI dataset.
In Figure 10, when the word overlap ratio between the premise and hypothesis is low
(below 10%), the accuracy of all models remains relatively high. However, as the overlap
ratio increases from 11% to 40%, the performance of models such as mBERT, PhoBERT,
XLM-R, CafeBERT, NLIMoETopK, and even our model declines significantly. Although
most models show some recovery when the overlap ratio reaches 51–60%, their accu-
racy quickly drops again once the overlap increases to 61–70%. Notably, when the over-
lap becomes very high (71–80%), most of the models fail to effectively exploit the high
word overlap—especially NLIMoETopK, whose accuracy falls to around 25%. In contrast,
NLIMoEDynamic demonstrates improved performance in this range and achieves the high-
est accuracy among all models. Overall, NLIMoEDynamic exhibits greater stability at low
overlap levels and superior performance under high-overlap conditions, highlighting its
robustness compared to other approaches.
In comparison to the previous ViNLI study [12], where the word overlap ratio be-
tween the premise and hypothesis was considered a factor that helps identify the in-
ferential relationship between the two sentences, our ViANLI dataset offers a different
perspective. Although reusing words in the hypothesis can assist the model in easily
recognizing the relationship, our dataset maintains a high level of difficulty because we
design the hypothesis sentences in a way that requires more complex reasoning, not just
relying on word overlap. This result further highlights the distinction of our adversarial
NLI dataset, where even when there is word reuse from the premise, the model still faces
34

--- Page 35 ---

significant challenges in identifying and reasoning about the relationship between the
premise and hypothesis. Consequently, our NLIMoEDynamic model shows a distinct ad-
vantage, as it effectively leverages these lexical patterns while still capturing the deeper
semantic reasoning needed for accurate inference.
0-10
11-20
21-30
31-40
41-50
51-60
61-70
71-80
>80
Jaccard (%)
30
35
40
45
50
55
60
Accuracy (%)
0
5
10
15
20
25
Quantity ratio (%)
7.8
26.7
26.1
18.0
10.0
5.5
2.4
2.1
1.4
mBERT
XLM-R
CafeBERT
PhoBERT
NLIMoEDynamic
NLIMoETopK
Quantity ratio
Figure 10: Word Overlap Rate Affects the Accuracy of Models.
7.5. Does New Word Rate Challenge NLI Models?
In contrast to the word overlap rate, the new word rate measures the proportion of
words used by the annotator to write the hypothesis sentence that do not appear in the
premise sentence. This is also considered a factor that may affect the performance of
machine learning models, as the more new words in the hypothesis sentence, the more
challenging it may be for the models to infer. To evaluate this, we also measure the
accuracy of the models in terms of new word rates in the hypothesis sentence on the
development set (see Figure 11).
Figure 11 show that the performance of most models fluctuates and declines as the
new word rate increases from 0% to 30%, with the exception of XLM-R. When the rate
rises from 31% to 40%, models such as mBERT, PhoBERT, XLM-R, and CafeBERT experi-
ence a drop in accuracy, while NLIMoEDynamic and NLIMoETopK show improvements. As
the new word rate continues to increase from 41% to 80%, the performance of all mod-
els improves significantly. Although, our proposed NLIMoEDynamic does not achieve the
highest accuracy in any specific range, it demonstrates the greatest stability across dif-
ferent levels of new word occurrence, maintaining consistent performance without the
large fluctuations observed in other models.
Overall, once again, we found the opposite of the results on the ViNLI dataset. The
analysis results on ViNLI show that as the rate of new words increases, it causes the
performance of the model to gradually decrease. There is a clear dependence of accuracy
on the new word rate, whereas this dependence is less evident in our data. However, the
new word rate in ViANLI is not the only factor determining the complexity of the data.
This shows that the data generated from our process warrants a high level of difficulty
and challenges for modern machine learning models.
35

--- Page 36 ---

0-10
11-20
21-30
31-40
41-50
51-60
61-70
71-80
>80
New word rate (%)
35
40
45
50
55
60
65
Accuracy (%)
0
2
4
6
8
10
12
14
16
Quantity ratio (%)
9.2
9.7
11.9
15.1
16.8
12.8
13.3
8.4
2.8
mBERT
XLM-R
CafeBERT
PhoBERT
NLIMoEDynamic
NLIMoETopK
Quantity ratio
Figure 11: New Word Rate Affects the Accuracy of Models.
7.6. Do Annotator Artifacts in Hypotheses Make ViANLI Less Challenging Than Other Datasets?
In natural language inference, annotator artifacts refer to unintended patterns or bi-
ases introduced by human annotators during the data creation process, such as repetitive
word choices, sentence structures, or stylistic preferences in hypothesis sentences. These
artifacts can allow models to make predictions based on superficial cues rather than true
semantic understanding, thereby reducing the challenge of the dataset. To investigate
whether such artifacts exist in the hypothesis sentences of ViANLI, we evaluate the ac-
curacy of models when they are trained and tested solely on hypothesis sentences. This
analysis helps assess the presence of annotator artifacts and their impact on the predic-
tive ability of models during training, as well as the overall difficulty of the dataset. The
results of evaluating the models on data from each round and the full ViANLI dataset
are summarized in Table 13.
Table 13: Model Accuracy (%) That is Trained on Hypothesis-only Data.
Model
ViA1
ViA2
ViA3
ViANLI
Dev
Test
Dev
Test
Dev
Test
Dev
Test
mBERT
39.15
40.00
35.75
37.87
38.52
32.35
37.80
36.70
XLM-R
40.60
40.50
38.18
36.66
40.58
38.53
39.80
38.60
PhoBERT
40.30
40.90
40.90
40.00
39.11
38.52
40.10
39.80
CafeBERT
42.42
42.42
41.51
36.96
38.23
40.58
40.70
40.00
NLIMoETopK
38.78
41.51
41.21
41.51
41.76
41.17
40.70
41.40
NLIMoEDynamic
42.42
45.75
40.00
42.12
40.88
39.11
40.80
42.20
Overall, the performance of the models on the dev and test sets of ViANLI is quite
low when the models are trained on hypothesis sentences only, which suggests that the
artifacts in the hypothesis sentence do not seem clear enough to help the models make
accurate predictions. Our model, NLIMoEDynamic, achieves the highest accuracy on the
dev set at 40.8%. This accuracy is significantly lower compared to other datasets such as
OCNLI ( 66%) [22], IndoNLI ( 60%) [23], SNLI ( 69%) [76], MultiNLI ( 62%) [77], and
36

--- Page 37 ---

ViNLI ( 58%) [12]. This indicates that during the construction of these datasets, annota-
tors intentionally limited the inclusion of cues in the hypothesis sentences to hinder the
model in making accurate predictions. In contrast to our data, the rigorously designed
data construction process avoids hypothetical artifacts, which helps ensure the difficulty
and challenge of our dataset. To investigate the artifacts left by annotators when writing
hypothesis sentences, we calculated the PMI (Pointwise Mutual Information) score on
the hypothesis sentences of our dataset to observe which words in the hypothesis might
distinguish the labels from one another in a manner similar to the ViNLI, OCNLI, and
IndoNLI datasets.
The results of the PMI scores are presented in Table 14, show that datasets such as
IndoNLI and OCNLI, built using conventional methods, contain clear linguistic cues in
hypothesis sentences that enable models to easily identify semantic relationships with
premise sentences. Notably, for the contradiction label, negation words like “no” and
“not” rank among the top three words with the highest PMI scores, serving as strong
indicators for this label. In contrast, ViNLI exhibits a distinct pattern: negation words
appear more frequently in hypothesis sentences for the entailment label. The authors of
ViNLI explain that annotators were instructed to limit the use of negation words when
crafting contradiction hypotheses, inadvertently leading to their increased presence in
entailment hypotheses. Conversely, our dataset, ViANLI, shows no prominent lexical
cues in hypothesis sentences that would allow models to easily distinguish semantic la-
bels. The top five words with the highest PMI scores across all three labels (entailment,
contradiction, and neutral) are relatively similar, indicating a lack of distinctive lexical
patterns. This design makes ViANLI significantly more challenging than other datasets,
as models cannot rely solely on superficial lexical features to accurately predict semantic
labels. Instead, they must consider the deeper semantic intent targeted by the annota-
tors, enhancing the difficulty and robustness of the dataset.
Table 14: Comparison of PMI Scores to Identify Representative Words for Labels to Distinguish from Other
Labels. We select the Top 3 (word, label) pairs from ViANLI for comparison with IndoNLI and OCNLI, and
the Top 5 (word, label) pairs from ViANLI for comparison with ViNLI. The results marked with * are extracted
from the ViNLI dataset [73], those marked with † are from the IndoNLI dataset [23], and those marked with
§ are from the SINGLE subset of OCNLI dataset [22].
#Top
Word
Label
PMI
ViANLI
ViNLI*
IndoNLI†
OCNLI§
ViANLI
ViNLI*
IndoNLI†
OCNLI§
#1
được - tobe + verb (past participle)
và - and
salah - wrong
-
E
0.32
0.18
0.72
-
#2
các - some/several
các - some/several
sekitar - around
-
E
0.31
0.22
0.72
-
#3
của - of/object’s
của - of/object’s
suatu - something
-
E
0.31
0.28
0.58
-
#4
là - tobe
trong - in/inside
-
-
E
0.25
0.35
-
-
#5
và - and
không - no/not
-
-
E
0.24
0.35
-
-
#1
và - and
của - of/object’s
bukan - no
任何- any
C
0.33
0.19
1.28
0.89
#2
của - of/object’s
là - tobe
tidak - no
没有- no
C
0.26
0.21
1.24
0.83
#3
được - tobe + verb (past participle)
trong - in/inside
apapun - anything
无关- not related
C
0.22
0.22
1.20
0.72
#4
có- has/have
và - and
-
-
C
0.21
0.23
-
-
#5
đã - was/were/verb(past/ed)
các - some/several
-
-
C
0.21
0.30
-
-
#1
là - tobe
một - one/a/an
selain - aside from
-
N
0.25
0.27
1.08
-
#2
có - has/have
là - tobe
juga - also
-
N
0.25
0.31
1.05
-
#3
được - tobe + verb (past participle)
và - and
banyak - a lot
-
N
0.24
0.32
0.94
-
#4
của - of/object’s
có - has/have
-
-
N
0.24
0.33
-
-
#5
là - tobe
trong - in/inside
-
-
N
0.23
0.33
-
-
7.7. Comparison of NLIMoE Reasoning Ability with Other Models by Inference Types
In this section, we evaluate the reasoning capabilities of the NLIMoE model com-
pared to baseline models (CafeBERT, XLM-R, PhoBERT, and mBERT) on the ViANLI
37

--- Page 38 ---

Dev Set, with a focus on analyzing performance across different inference types. The
primary objective is to conduct a linguistic analysis that uncovers how these models
handle diverse reasoning challenges inherent in Vietnamese natural language inference.
Table 15 provides a detailed comparison of NLIMoEDynamic’s reasoning ability with
other models across seven distinct inference types: numerical & quantitative reasoning,
reference & names, standard logical inferences, lexical reasoning, tricky linguistic infer-
ence, external knowledge reasoning, and cultural & contextual inference. NLIMoEDynamic
demonstrates superior performance in most categories, achieving the highest scores in
numerical & quantitative reasoning (51.42%), reference & names (60.00%), standard
(49.79%), lexical (52.55%), and external knowledge (49.13%). NLIMoEDynamic effectively
captures complex linguistic phenomena such as numerical relationships, proper noun
references, lexical ambiguities, and supplementary information from external sources.
However, the performance of NLIMoETopK is highest in cultural & contextual inference
(48.51%), indicating that NLIMoEDynamic still faces challenges in reasoning over phe-
nomena tied to Vietnamese culture and context. Overall, NLIMoEDynamic demonstrates
strong and consistent reasoning capabilities across most inference types compared to
other models, particularly in handling numerical & quantitative reasoning, resolving
reference-based ambiguities, and addressing lexical variations, which are often difficult
for multilingual pre-trained models on low-resource languages like Vietnamese.
Table 15: Comparison of NLIMoEDynamic Reasoning Ability (Accuracy - %) with Other Models on the ViANLI
Dev Set by Different Inference Types.
Models
NaQR
RaN
SLI
LR
TLI
EKR
CaCI
Average
mBERT
43.32
40.00
44.00
45.62
38.05
48.83
42.57
43.19
XLM-R
47.77
52.00
47.03
51.61
46.91
44.41
47.52
48.17
PhoBERT
46.96
56.00
47.17
49.76
33.62
48.37
38.61
45.78
CafeBERT
50.62
52.00
49.11
50.23
44.24
47.44
39.61
47.61
NLIMoETopK
47.77
57.00
48.55
49.76
40.71
48.61
48.51
48.69
NLIMoEDynamic
51.42
60.00
49.79
52.55
43.36
49.13
43.56
49.97
Average
47.97
52.83
47.61
49.92
41.14
47.79
43.39
-
Table 16 compares the reasoning ability of NLIMoEDynamic with baseline models when
handling combinations of multiple inference types on the ViANLI Dev Set. Results
show that NLIMoEDynamic delivers competitive performance on premise–hypothesis pairs
involving single-type inference (50.00%), slightly behind CafeBERT (50.61%) but out-
performing most other baselines. In pairs requiring two-type inference, NLIMoEDynamic
maintains stable accuracy (47.52%), although CafeBERT achieves the highest score (52.00%).
Notably, in the most challenging cases involving three-type inference where models
must simultaneously reason over multiple intertwined linguistic phenomena, NLIMoEDynamic
achieves a significant performance advantage, reaching 59.80%, the highest among all
models and surpassing the second-best (XLM-R, 54.90%). This highlights NLIMoEDynamic’s
superior capability to integrate diverse reasoning skills and effectively tackle complex,
multi-faceted inference scenarios in Vietnamese NLI, benefiting from its adaptive Mixture-
of-Experts mechanism.
38

--- Page 39 ---

Table 16: Comparison of NLIMoEDynamic Reasoning Ability with Other Models on the ViANLI Dev Set by
combining multiple types of inference.
Models
#Inference Type
1 type
2 types
3 types
mBERT
42.44
43.53
50.00
XLM-R
48.25
45.59
54.90
PhoBERT
47.67
46.14
50.00
CafeBERT
50.61
52.00
49.1
NLIMoETopK
47.09
48.21
50.98
NLIMoEDynamic
50.00
47.52
59.80
7.8. Error Analysis
Confusion matrix analysis serves as a vital tool in evaluating the performance of ma-
chine learning models, enabling precise identification of error types encountered during
label classification. The purpose of this analysis is to gain deeper insights into the abil-
ity to differentiate between the labels including contradiction, entailment, and neutral,
thereby uncovering model weaknesses, especially in complex or adversarial data sce-
narios. This process not only aids in enhancing model accuracy but also highlights the
semantic factors models must learn to achieve more precise predictions. Results from the
confusion matrices of the proposed NLIMoEDynamic and other models, including mBERT,
PhoBERT, XLM-R, CafeBERT, and NLIMoETopK on the development set of the ViANLI
dataset are presented in Figure D.13 (in Appendix D).
The confusion matrices reveal distinct challenges posed by the Adversarial NLI dataset,
highlighting varying limitations among the compared models. mBERT shows a clear
bias toward Neutral predictions, often misclassifying both contradiction and entailment
as neutral, suggesting difficulty in capturing the adversarial nuances requiring fine-
grained semantic understanding. PhoBERT and XLM-R outperform mBERT in entail-
ment predictions, demonstrating a better grasp of entailment relationships, but they en-
counter consistency issues elsewhere, PhoBERT struggles to maintain accuracy on con-
tradiction, frequently misclassifying it, while XLM-R has difficulty sustaining perfor-
mance on neutral, often confusing it with other labels. CafeBERT appears more stable
across all labels compared to the other models, yet it still exhibits a notable weakness,
with a substantial number of contradiction samples being mispredicted as neutral, indi-
cating sensitivity to the dataset adversarial design. NLIMoETopK performs well on the
entailment label but misclassifies a substantial number of patterns belonging to the con-
tradiction and neutral labels. In contrast, NLIMoEDynamic demonstrates greater stability
than the other models, showing particularly strong performance on entailment and neu-
tral labels, though it still misclassifies a notable portion of contradiction samples, likely
due to the adversarial nature of the dataset. These findings suggest that the Mixture-of-
Experts architecture of NLIMoEDynamic offers a significant advantage in handling diverse
inference scenarios, representing a clear improvement over the more biased or inconsis-
tent tendencies observed in the other models.
Table E.19 (in Appendix E)provides examples of incorrect predictions by models, of-
fering valuable insight into challenges posed by the ViANLI dataset. The dataset tests
models with subtle semantic ambiguities, complex contextual dependencies, and ad-
versarial perturbations, as seen in premise-hypothesis pairs. Examples highlight diffi-
culties in detecting contradictions from implicit cues (e.g., gender specificity in testic-
39

--- Page 40 ---

ular torsion), recognizing temporal discrepancies (e.g., 18/5 to 20/5 spans 2 days, not
5), handling paraphrased entailments (e.g., the President of Palau meeting Taiwan’s
leader implies both leaders participated in an event), and managing numerical incon-
sistencies (e.g., currency conversion in LG pricing). These characteristics exploit weak-
nesses in semantic understanding, leading to frequent misclassifications, particularly for
contradiction, across mBERT, PhoBERT, XLM-R, and CafeBERT, underscoring the nu-
anced complexity of the dataset. While NLIMoEDynamic also errors in cases like the first
two examples alongside other models, it correctly predicts labels in scenarios involving
paraphrased entailments and numerical comparisons, as seen in the last two examples,
demonstrating enhanced capability in handling complex semantic relationships.
To further analyze this behavior, we investigate the distribution of experts activated
across different inference types in the ViANLI dev set as in Figure F.14 (Appendix F).
The analysis reveals that Expert 3 consistently emerges as the dominant contributor, be-
ing frequently activated across nearly all reasoning categories. Specifically, for numerical
and quantitative reasoning, Expert 3 plays a pivotal role, while Experts 1, 5, and 6 serve
as complementary contributors. For example, in Case 4 of Table E.19, NLIMoE success-
fully activated three out of these four experts, enabling accurate numerical inference.
Conversely, for standard logical inferences (e.g., Case 3), Experts 1 and 6 demonstrate
stronger specialization, and NLIMoE successfully activated these two experts and effec-
tively leveraged both to arrive at the correct prediction. These observations highlight that
the Mixture-of-Experts architecture in NLIMoEDynamic not only partitions inference tasks
among specialized experts but also dynamically selects the most relevant subset. This
adaptive routing provides a distinct advantage, allowing the model to better address the
diverse challenges of ViANLI and achieve superior accuracy through both specialization
and expert collaboration.
8. Conclusion and Future Work
In this article, we introduced ViANLI, the first adversarial dataset for Vietnamese
natural language inference, including over 10,000 premise-hypothesis pairs generated by
the human-and-machine-in-the-loop approach with human-machine verification. ViANLI
exhibits greater complexity compared to previous Vietnamese NLI datasets, significantly
challenging state-of-the-art models and setting a new benchmark for future Vietnamese
and multilingual NLI research. We also proposed NLIMoEDynamic with a dynamic rout-
ing mechanism capable of choosing the number of experts dynamically based on the
complexity of the input, this Mixture-of-Experts model tailored for adversarial NLI,
which compares to all baselines with an accuracy of 47.3% on the ViANLI test set, com-
pared to 45.5% for XLM-R. Notably, NLIMoEDynamic demonstrates superior inference ca-
pabilities, particularly in handling long sentences, high new word rates in hypotheses,
and effectively resolves entailment ambiguity cases such as numerical & quantitative,
reference & names, standard, lexical, and external knowledge reasoning, as shown in our
analyses. Furthermore, augmenting Vietnamese NLI datasets such as ViNLI, VLSP2021-
NLI, and VnNewsNLI with ViANLI data enhances the performance of NLI models like
mBERT, PhoBERT, XLM-R, and NLIMoE highlighting the value of ViANLI as a key re-
source for advancing NLI research in Vietnamese.
In future work, our dataset creation approach of ViANLI can be used with a wider
range of text genres, especially focusing on those reasoning types that machine models
40

--- Page 41 ---

commonly fail, to further enhance model knowledge. This approach provides a replica-
ble paradigm for NLI research in other low-resource languages, driving global AI tech-
nology toward more inclusive and balanced development. Indeed, while large language
models demonstrate exceptional potential across industries, previous research [78] has
also emphasized that the emergence of such models exacerbates global resource inequal-
ity. In addition, other state-of-the-art generative models such as MT5 [61], ViT5 [79],
mBART [63], and BARTpho [80] are explored on NLIMoEDynamic. Furthermore, we aim
to refine our NLIMoEDynamic model, making it more adept at handling high-complexity
data patterns when combined with large language models (LLMs). Furthermore, we
also combine ViANLI with other NLI datasets to enhance effectiveness in tasks such as
machine reading comprehension and text summarization.
Acknowledgement
This research is funded by Vietnam National University HoChiMinh City (VNU-
HCM) under grant number NCM2025-26-02.
Declarations of Interest
The authors declare that they have no conflict of interest.
Data Availability
Data will be made available on reasonable request.
Author Contribution
Tin Van Huynh: Conceptualization; Data curation; Formal analysis; Investigation;
Methodology; Validation; Visualization; Writing - original draft.
Kiet Van Nguyen: Conceptualization; Data curation; Formal analysis; Investigation;
Methodology; Validation; Visualization; Writing - review&editing.
Ngan Luu-Thuy Nguyen: Conceptualization; Formal analysis; Investigation; Method-
ology; Supervision; Validation; Writing - review&editing.
References
[1] S. Bowman, G. Angeli, C. Potts, C. D. Manning, A large annotated corpus for learn-
ing natural language inference, in: Proceedings of the 2015 Conference on Empiri-
cal Methods in Natural Language Processing, 2015, pp. 632–642.
[2] K. Nguyen, V. Nguyen, A. Nguyen, N. Nguyen, A vietnamese dataset for evalu-
ating machine reading comprehension, in: Proceedings of the 28th International
Conference on Computational Linguistics, 2020, pp. 2595–2605.
41

--- Page 42 ---

[3] K. Van Nguyen, T. Van Huynh, D.-V. Nguyen, A. G.-T. Nguyen, N. L.-T. Nguyen,
New vietnamese corpus for machine reading comprehension of health news arti-
cles, Transactions on Asian and Low-Resource Language Information Processing
21 (5) (2022) 1–28.
[4] K. Kann, A. Ebrahimi, M. Mager, A. Oncevay, J. E. Ortega, A. Rios, A. Fan,
X. Gutierrez-Vasques, L. Chiruzzo, G. A. Giménez-Lugo, et al., Americasnli: Ma-
chine translation and natural language inference systems for indigenous languages
of the americas, Frontiers in Artificial Intelligence 5 (2022) 266.
[5] X. Li, D. Zhao, J. Meng, H. Lin, Exploring biomedical relation extraction by com-
bining natural language inference and dual dependency trees, Expert Systems with
Applications 289 (2025) 128342.
[6] A. Mishra, D. Patel, A. Vijayakumar, X. L. Li, P. Kapanipathi, K. Talamadupula,
Looking beyond sentence-level natural language inference for question answer-
ing and text summarization, in: Proceedings of the 2021 Conference of the North
American Chapter of the Association for Computational Linguistics: Human Lan-
guage Technologies, 2021, pp. 1322–1336.
[7] R. Jia, P. Liang, Adversarial examples for evaluating reading comprehension sys-
tems, in: Proceedings of the 2017 Conference on Empirical Methods in Natural
Language Processing, 2017, pp. 2021–2031.
[8] Y. Nie, A. Williams, E. Dinan, M. Bansal, J. Weston, D. Kiela, Adversarial NLI: A
new benchmark for natural language understanding, in: Proceedings of the 58th
Annual Meeting of the Association for Computational Linguistics, Association for
Computational Linguistics, Online, 2020, pp. 4885–4901.
doi:10.18653/v1/
2020.acl-main.441.
URL https://aclanthology.org/2020.acl-main.441
[9] V. Agarwal, S. Joglekar, A. P. Young, N. Sastry, Graphnli: A graph-based natural
language inference model for polarity prediction in online debates, in: Proceedings
of the ACM Web Conference 2022, 2022, pp. 2729–2737.
[10] C. Tandon, P. Bongale, T. Arpita, R. Sanjana, H. Palivela, C. Nirmala, Use of natural
language inference in optimizing reviews and providing insights to end consumers,
in: 2021 7th International Conference on Advanced Computing and Communica-
tion Systems (ICACCS), Vol. 1, IEEE, 2021, pp. 60–65.
[11] S. Xu, K. Markert, The Chinese causative-passive homonymy disambiguation: an
adversarial dataset for NLI and a probing task, in: Proceedings of the Thirteenth
Language Resources and Evaluation Conference, European Language Resources
Association, Marseille, France, 2022, pp. 4316–4323.
URL https://aclanthology.org/2022.lrec-1.460
[12] T. V. Huynh, K. V. Nguyen, N. L.-T. Nguyen, ViNLI: A Vietnamese corpus for stud-
ies on open-domain natural language inference, in: Proceedings of the 29th In-
ternational Conference on Computational Linguistics, International Committee on
Computational Linguistics, Gyeongju, Republic of Korea, 2022, pp. 3858–3872.
URL https://aclanthology.org/2022.coling-1.339
42

--- Page 43 ---

[13] C. T. Nguyen, D. T. Nguyen, Building a vietnamese dataset for natural language
inference models, SN Computer Science 3 (5) (2022) 395.
[14] N. Quyen, H. Anh, N. Huyen, N. Lien, Vlsp 2021 - vnnli challenge: Vietnamese and
english-vietnamese textual entailment, VNU Journal of Science: Computer Science
and Communication Engineering 38 (2) (2022). doi:10.25073/2588-1086/
vnucsce.363.
URL //jcsce.vnu.edu.vn/index.php/jcsce/article/view/363
[15] A. Bonet-Jover, R. Sepúlveda-Torres, E. Saquete, P. Martínez-Barco, A. Piad-
Morffis,
S.
Estevez-Velarde,
Applying
human-in-the-loop
to
construct
a
dataset for determining content reliability to combat fake news, Engineer-
ing Applications of Artificial Intelligence 126 (2023) 107152.
doi:https:
//doi.org/10.1016/j.engappai.2023.107152.
URL
https://www.sciencedirect.com/science/article/pii/
S0952197623013362
[16] X. Cao, Y. Sun, J. Li, Q. Gesang, N. Qun, T. Nyima, Human-in-the-loop generation
of adversarial texts: A case study on tibetan script (2025). arXiv:2412.12478.
URL https://arxiv.org/abs/2412.12478
[17] M. Bartolo, A. Roberts, J. Welbl, S. Riedel, P. Stenetorp, Beat the ai: Investigating
adversarial human annotation for reading comprehension, Transactions of the As-
sociation for Computational Linguistics 8 (2020) 662–678.
[18] L. Li, J. Lei, Z. Gan, J. Liu, Adversarial vqa: A new benchmark for evaluating the ro-
bustness of vqa models, in: Proceedings of the IEEE/CVF International Conference
on Computer Vision (ICCV), 2021, pp. 2042–2051.
[19] A. Conneau, K. Khandelwal, N. Goyal, V. Chaudhary, G. Wenzek, F. Guzmán,
E. Grave, M. Ott, L. Zettlemoyer, V. Stoyanov, Unsupervised cross-lingual represen-
tation learning at scale, in: Proceedings of the 58th Annual Meeting of the Asso-
ciation for Computational Linguistics, Association for Computational Linguistics,
Online, 2020, pp. 8440–8451. doi:10.18653/v1/2020.acl-main.747.
URL https://aclanthology.org/2020.acl-main.747
[20] I. Dagan, O. Glickman, B. Magnini, The pascal recognising textual entailment chal-
lenge, in: Machine learning challenges workshop, Springer, 2005, pp. 177–190.
[21] A. Williams, N. Nangia, S. Bowman, A broad-coverage challenge corpus for sen-
tence understanding through inference, in: Proceedings of the 2018 Conference
of the North American Chapter of the Association for Computational Linguistics:
Human Language Technologies, Volume 1 (Long Papers), Association for Compu-
tational Linguistics, 2018, pp. 1112–1122.
URL http://aclweb.org/anthology/N18-1101
[22] H. Hu, K. Richardson, L. Xu, L. Li, S. K¨ubler, L. S. Moss, Ocnli: Original chinese
natural language inference, in: Findings of the Association for Computational Lin-
guistics: EMNLP 2020, 2020, pp. 3512–3526.
43

--- Page 44 ---

[23] R. Mahendra, A. F. Aji, S. Louvan, F. Rahman, C. Vania, IndoNLI: A natural lan-
guage inference dataset for Indonesian, in: Proceedings of the 2021 Conference
on Empirical Methods in Natural Language Processing, Association for Computa-
tional Linguistics, Online and Punta Cana, Dominican Republic, 2021, pp. 10511–
10527. doi:10.18653/v1/2021.emnlp-main.821.
URL https://aclanthology.org/2021.emnlp-main.821
[24] A. Romanov, C. Shivade, Lessons from natural language inference in the clinical
domain, in: E. Riloff, D. Chiang, J. Hockenmaier, J. Tsujii (Eds.), Proceedings of
the 2018 Conference on Empirical Methods in Natural Language Processing, As-
sociation for Computational Linguistics, Brussels, Belgium, 2018, pp. 1586–1596.
doi:10.18653/v1/D18-1187.
URL https://aclanthology.org/D18-1187/
[25] T. Khot, A. Sabharwal, P. Clark, Scitail: A textual entailment dataset from science
question answering, in: Proceedings of the AAAI Conference on Artificial Intelli-
gence, Vol. 32, 2018.
[26] H. Amirkhani, M. AzariJafari, S. Faridan-Jahromi, Z. Kouhkan, Z. Pourjafari,
A. Amirak, Farstail: A persian natural language inference dataset, Soft Comput-
ing (2023) 1–13.
[27] A. Conneau, R. Rinott, G. Lample, A. Williams, S. Bowman, H. Schwenk, V. Stoy-
anov, Xnli: Evaluating cross-lingual sentence representations, in: Proceedings of
the 2018 Conference on Empirical Methods in Natural Language Processing, 2018,
pp. 2475–2485.
[28] S. Khanuja, S. Dandapat, S. Sitaram, M. Choudhury, A new dataset for natural lan-
guage inference from code-mixed conversations, in: Proceedings of the The 4th
Workshop on Computational Approaches to Code Switching, 2020, pp. 9–16.
[29] J. Ham, Y. J. Choe, K. Park, I. Choi, H. Soh, Kornli and korsts: New benchmark
datasets for korean natural language understanding, in: Findings of the Associa-
tion for Computational Linguistics: EMNLP 2020, 2020, pp. 422–430.
[30] J. Thorne, A. Vlachos, C. Christodoulopoulos, A. Mittal, Fever: a large-scale dataset
for fact extraction and verification, in: Proceedings of the 2018 Conference of the
North American Chapter of the Association for Computational Linguistics: Human
Language Technologies, Volume 1 (Long Papers), 2018, pp. 809–819.
[31] T. Schuster, A. Fisch, R. Barzilay, Get your vitamin c! robust fact verification with
contrastive evidence, in: Proceedings of the 2021 Conference of the North Ameri-
can Chapter of the Association for Computational Linguistics: Human Language
Technologies, 2021, pp. 624–643.
[32] R. Aly, Z. Guo, M. Schlichtkrull, J. Thorne, A. Vlachos, C. Christodoulopoulos,
O. Cocarascu, A. Mittal, Feverous: Fact extraction and verification over unstruc-
tured and structured information, in: 35th Conference on Neural Information Pro-
cessing Systems, NeurIPS 2021, Neural Information Processing Systems founda-
tion, 2021.
44

--- Page 45 ---

[33] D. Kang, T. Khot, A. Sabharwal, E. Hovy, Adventure: Adversarial training for tex-
tual entailment with knowledge-guided examples, in: Proceedings of the 56th An-
nual Meeting of the Association for Computational Linguistics (Volume 1: Long
Papers), 2018, pp. 2418–2428.
[34] M. Iyyer, J. Wieting, K. Gimpel, L. Zettlemoyer, Adversarial example generation
with syntactically controlled paraphrase networks, in: Proceedings of NAACL-
HLT, 2018, pp. 1875–1885.
[35] P. Minervini, S. Riedel, Adversarially regularising neural nli models to integrate
logical background knowledge, in: Proceedings of the 22nd Conference on Com-
putational Natural Language Learning, 2018, pp. 65–74.
[36] X. Dong, A. T. Luu, R. Ji, H. Liu, Towards robustness against natural language word
substitutions, in: International Conference on Learning Representations, 2020.
[37] C. Zhu, Y. Cheng, Z. Gan, S. Sun, T. Goldstein, J. Liu, Freelb: Enhanced adversar-
ial training for natural language understanding, in: International Conference on
Learning Representations, 2019.
[38] R. Zellers, Y. Bisk, R. Schwartz, Y. Choi, Swag: A large-scale adversarial dataset
for grounded commonsense inference, in: Proceedings of the 2018 Conference on
Empirical Methods in Natural Language Processing, 2018, pp. 93–104.
[39] Z. Yang, P. Qi, S. Zhang, Y. Bengio, W. Cohen, R. Salakhutdinov, C. D. Manning,
Hotpotqa: A dataset for diverse, explainable multi-hop question answering, in:
Proceedings of the 2018 Conference on Empirical Methods in Natural Language
Processing, Association for Computational Linguistics, 2018.
[40] D. Dua, Y. Wang, P. Dasigi, G. Stanovsky, S. Singh, M. Gardner, Drop: A reading
comprehension benchmark requiring discrete reasoning over paragraphs, in: Pro-
ceedings of the 2019 Conference of the North American Chapter of the Association
for Computational Linguistics: Human Language Technologies, Volume 1 (Long
and Short Papers), 2019, pp. 2368–2378.
[41] M. Chen, M. D’Arcy, A. Liu, J. Fernandez, D. Downey, Codah: An adversarially-
authored question answering dataset for common sense, in: Proceedings of the 3rd
Workshop on Evaluating Vector Space Representations for NLP, 2019, pp. 63–69.
[42] P. Dasigi, N. F. Liu, A. Marasovi´c, N. A. Smith, M. Gardner, Quoref: A reading
comprehension dataset with questions requiring coreferential reasoning, in: Pro-
ceedings of the 2019 Conference on Empirical Methods in Natural Language Pro-
cessing and the 9th International Joint Conference on Natural Language Processing
(EMNLP-IJCNLP), 2019, pp. 5925–5932.
[43] E. Wallace, P. Rodriguez, S. Feng, I. Yamada, J. Boyd-Graber, Trick me if you can:
Human-in-the-loop generation of adversarial examples for question answering,
Transactions of the Association for Computational Linguistics 7 (2019) 387–401.
doi:10.1162/tacl_a_00279.
URL https://aclanthology.org/Q19-1029
45

--- Page 46 ---

[44] J. Thorne, A. Vlachos, O. Cocarascu, C. Christodoulopoulos, A. Mittal, The fever2.
0 shared task, in: Proceedings of the Second Workshop on Fact Extraction and VER-
ification (FEVER), 2019, pp. 1–6.
[45] J. R. Finkel, C. D. Manning, A. Y. Ng, Solving the problem of cascading errors: Ap-
proximate bayesian inference for linguistic annotation pipelines, in: Proceedings of
the 2006 Conference on Empirical Methods in Natural Language Processing, 2006,
pp. 618–626.
[46] T. K. Landauer, S. T. Dumais, A solution to plato’s problem: The latent semantic
analysis theory of acquisition, induction, and representation of knowledge., Psy-
chological review 104 (2) (1997) 211.
[47] Y. R. Oh, H.-B. Jeon, H. J. Song, Y.-K. Lee, J.-G. Park, Y.-K. Lee, A deep-learning
based native-language classification by using a latent semantic analysis for the NLI
shared task 2017, in: Proceedings of the 12th Workshop on Innovative Use of NLP
for Building Educational Applications, Association for Computational Linguistics,
Copenhagen, Denmark, 2017, pp. 413–422. doi:10.18653/v1/W17-5047.
URL https://aclanthology.org/W17-5047
[48] T. Mikolov, I. Sutskever, K. Chen, G. S. Corrado, J. Dean, Distributed representa-
tions of words and phrases and their compositionality, Advances in neural infor-
mation processing systems 26 (2013).
[49] J. L. Elman, Finding structure in time, Cognitive science 14 (2) (1990) 179–211.
[50] S. Hochreiter, J. Schmidhuber, Long short-term memory, Neural computation 9 (8)
(1997) 1735–1780.
[51] Q. Chen, X. Zhu, Z.-H. Ling, S. Wei, H. Jiang, D. Inkpen, Enhanced lstm for natural
language inference, in: Proceedings of the 55th Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Papers), 2017, pp. 1657–1668.
[52] J. Devlin, M.-W. Chang, K. Lee, K. Toutanova, BERT: Pre-training of deep bidirec-
tional transformers for language understanding, in: Proceedings of the 2019 Con-
ference of the North American Chapter of the Association for Computational Lin-
guistics: Human Language Technologies, Volume 1 (Long and Short Papers), As-
sociation for Computational Linguistics, Minneapolis, Minnesota, 2019, pp. 4171–
4186. doi:10.18653/v1/N19-1423.
URL https://aclanthology.org/N19-1423
[53] A. Radford, K. Narasimhan, T. Salimans, I. Sutskever, et al., Improving language
understanding by generative pre-training (2018).
[54] Y. Liu, M. Ott, N. Goyal, J. Du, M. Joshi, D. Chen, O. Levy, M. Lewis, L. Zettle-
moyer, V. Stoyanov, Roberta: A robustly optimized bert pretraining approach, arXiv
preprint arXiv:1907.11692 (2019).
[55] Z. Yang, Z. Dai, Y. Yang, J. Carbonell, R. R. Salakhutdinov, Q. V. Le, Xlnet: Gener-
alized autoregressive pretraining for language understanding, Advances in neural
information processing systems 32 (2019).
46

--- Page 47 ---

[56] Z. Lan, M. Chen, S. Goodman, K. Gimpel, P. Sharma, R. Soricut, Albert: A lite bert
for self-supervised learning of language representations, in: International Confer-
ence on Learning Representations, 2019.
[57] V. Sanh, L. Debut, J. Chaumond, T. Wolf, Distilbert, a distilled version of bert:
smaller, faster, cheaper and lighter, arXiv preprint arXiv:1910.01108 (2019).
[58] K. Clark, M.-T. Luong, Q. V. Le, C. D. Manning, Electra: Pre-training text encoders
as discriminators rather than generators, ELECTRA 85 (2016) 90.
[59] C. Raffel, N. Shazeer, A. Roberts, K. Lee, S. Narang, M. Matena, Y. Zhou, W. Li, P. J.
Liu, Exploring the limits of transfer learning with a unified text-to-text transformer,
The Journal of Machine Learning Research 21 (1) (2020) 5485–5551.
[60] D. Q. Nguyen, A. T. Nguyen, Phobert: Pre-trained language models for vietnamese,
in: Findings of the Association for Computational Linguistics: EMNLP 2020, 2020,
pp. 1037–1042.
[61] L. Xue, N. Constant, A. Roberts, M. Kale, R. Al-Rfou, A. Siddhant, A. Barua, C. Raf-
fel, mT5: A massively multilingual pre-trained text-to-text transformer, in: Pro-
ceedings of the 2021 Conference of the North American Chapter of the Associa-
tion for Computational Linguistics: Human Language Technologies, Association
for Computational Linguistics, Online, 2021, pp. 483–498. doi:10.18653/v1/
2021.naacl-main.41.
URL https://aclanthology.org/2021.naacl-main.41
[62] P. N.-T. Do, S. Q. Tran, P. G. Hoang, K. V. Nguyen, N. L.-T. Nguyen, VLUE: A
new benchmark and multi-task knowledge transfer learning for Vietnamese nat-
ural language understanding, in: K. Duh, H. Gomez, S. Bethard (Eds.), Find-
ings of the Association for Computational Linguistics: NAACL 2024, Association
for Computational Linguistics, Mexico City, Mexico, 2024, pp. 211–222.
doi:
10.18653/v1/2024.findings-naacl.15.
URL https://aclanthology.org/2024.findings-naacl.15/
[63] Y. Liu, J. Gu, N. Goyal, X. Li, S. Edunov, M. Ghazvininejad, M. Lewis, L. Zettle-
moyer, Multilingual denoising pre-training for neural machine translation, Trans-
actions of the Association for Computational Linguistics 8 (2020) 726–742. doi:
10.1162/tacl_a_00343.
URL https://aclanthology.org/2020.tacl-1.47
[64] T. Shen, M. Ott, M. Auli, M. Ranzato, Mixture models for diverse machine transla-
tion: Tricks of the trade, in: International conference on machine learning, PMLR,
2019, pp. 5719–5728.
[65] M. Ravaut, S. Joty, N. Chen, Summareranker: A multi-task mixture-of-experts re-
ranking framework for abstractive summarization, in: Proceedings of the 60th An-
nual Meeting of the Association for Computational Linguistics (Volume 1: Long
Papers), 2022, pp. 4504–4524.
47

--- Page 48 ---

[66] N. Du, Y. Huang, A. M. Dai, S. Tong, D. Lepikhin, Y. Xu, M. Krikun, Y. Zhou, A. W.
Yu, O. Firat, et al., Glam: Efficient scaling of language models with mixture-of-
experts, in: International conference on machine learning, PMLR, 2022, pp. 5547–
5569.
[67] W. Fedus, B. Zoph, N. Shazeer, Switch transformers: Scaling to trillion parameter
models with simple and efficient sparsity, Journal of Machine Learning Research
23 (120) (2022) 1–39.
[68] D. Lepikhin, H. Lee, Y. Xu, D. Chen, O. Firat, Y. Huang, M. Krikun, N. Shazeer,
Z. Chen, Gshard: Scaling giant models with conditional computation and auto-
matic sharding, arXiv preprint arXiv:2006.16668 (2020).
[69] Y. Gao, N. Xu, H. Tian, B. Zheng, J. Cao, A.-A. Liu, Mixture of causal ex-
perts:
A causal perspective to build dual-level mixture-of-experts mod-
els, Expert Systems with Applications 280 (2025) 127422.
doi:https:
//doi.org/10.1016/j.eswa.2025.127422.
URL
https://www.sciencedirect.com/science/article/pii/
S0957417425010449
[70] J. Wang, L. Nie, J. Duan, H. Zhao, C. P. Chen, Mixture-of-experts-based broad
learning system and its applications, Expert Systems with Applications 269 (2025)
126389.
[71] J. Achiam, S. Adler, S. Agarwal, L. Ahmad, I. Akkaya, F. L. Aleman, D. Almeida,
J. Altenschmidt, S. Altman, S. Anadkat, et al., Gpt-4 technical report, arXiv preprint
arXiv:2303.08774 (2023).
[72] T. Vu, D. Q. Nguyen, M. Dras, M. Johnson, et al., Vncorenlp: A vietnamese natural
language processing toolkit, in: Proceedings of the 2018 Conference of the North
American Chapter of the Association for Computational Linguistics: Demonstra-
tions, 2018, pp. 56–60.
[73] T. Van Huynh, H. Q. To, K. Van Nguyen, N. L.-T. Nguyen, Error investigation of
pre-trained bertology models on vietnamese natural language inference, in: Asian
Conference on Intelligent Information and Database Systems, Springer, 2022, pp.
176–188.
[74] D. Q. Nguyen, et al., Phonlp: A joint multi-task learning model for vietnamese
part-of-speech tagging, named entity recognition and dependency parsing, in: Pro-
ceedings of the 2021 Conference of the North American Chapter of the Association
for Computational Linguistics: Human Language Technologies: Demonstrations,
2021, pp. 1–7.
[75] Q. Huang, Z. An, N. Zhuang, M. Tao, C. Zhang, Y. Jin, K. Xu, K. Xu, L. Chen,
S. Huang, Y. Feng, Harder task needs more experts: Dynamic routing in MoE
models, in: L.-W. Ku, A. Martins, V. Srikumar (Eds.), Proceedings of the 62nd An-
nual Meeting of the Association for Computational Linguistics (Volume 1: Long
Papers), Association for Computational Linguistics, Bangkok, Thailand, 2024, pp.
12883–12895. doi:10.18653/v1/2024.acl-long.696.
URL https://aclanthology.org/2024.acl-long.696/
48

--- Page 49 ---

[76] A. Poliak, J. Naradowsky, A. Haldar, R. Rudinger, B. Van Durme, Hypothesis only
baselines in natural language inference, in: Proceedings of the Seventh Joint Con-
ference on Lexical and Computational Semantics, 2018, pp. 180–191.
[77] S. Bowman, J. Palomaki, L. B. Soares, E. Pitler, New protocols and negative results
for textual entailment data collection, in: Proceedings of the 2020 Conference on
Empirical Methods in Natural Language Processing (EMNLP), 2020, pp. 8203–
8214.
[78] S.-B. Guo, Y. Shen, Y. Meng, Z.-Z. Zhou, H.-L. Li, X.-Y. Cai, W.-J. Huang, X.-P. Tian,
Surge in large language models exacerbates global regional healthcare inequalities,
Journal of Translational Medicine 23 (1) (2025) 706.
[79] L. Phan, H. Tran, H. Nguyen, T. H. Trinh, ViT5: Pretrained text-to-text transformer
for Vietnamese language generation, in: Proceedings of the 2022 Conference of the
North American Chapter of the Association for Computational Linguistics: Hu-
man Language Technologies: Student Research Workshop, Association for Com-
putational Linguistics, Hybrid: Seattle, Washington + Online, 2022, pp. 136–142.
doi:10.18653/v1/2022.naacl-srw.18.
URL https://aclanthology.org/2022.naacl-srw.18
[80] N. L. Tran, D. M. Le, D. Q. Nguyen, BARTpho: Pre-trained Sequence-to-Sequence
Models for Vietnamese, in: Proceedings of the 23rd Annual Conference of the In-
ternational Speech Communication Association, 2022.
Appendix A. Examples from ViANLI Dataset
49

--- Page 50 ---

Table A.17: Examples from ViANLI Dataset. Where Pred. Is the Predictive Label of the Model, Vali.1 Is the
Three Confirmation Labels of the Three Verifiers in the Phase 4.1. C, E, and N Are the Abbreviations for
Contradiction, Entailment, and Neutral.
Premise
Hypothesis
Reason
Round
Gold label
Pred. label
Vali.1 labels
Các giảthuyết trước đây
cho rằng Hadrosaurid đã di
cư từBắc Mỹtới châu Á
nhưng khám phá mới lại cho
thấy điều ngược lại.
(Pre-
vious theories suggested that
the Hadrosaurid migrated from
North America to Asia, but the
new discovery suggests other-
wise.)
Các phát hiện
mới
đã
phủ
định
những
phỏng
đoán
trước
đây,
Hadrosaurid
không
hề
có
sự
thay
đổi
nơi sinh sống.
(The new find-
ings have denied
previous
conjec-
tures,
that
the
Hadrosaurid did
not
change
its
habitat.)
Dùng nhiều từngữkhác
với câu ban đầu nên mô
hình
có
thể
đoán
sai.
(Using
many
different
words
from
the
original
sentence,
the model may
guess wrong.)
ViA1
C
E
C C C
Hơn 30 phút sau, đám cháy
được khống chế, tàu hàng
2371 tiếp tục hành trình theo
hướng Bắc Nam. (More than
30 minutes later, the fire was un-
der control, cargo ship 2371 con-
tinued its journey in the north-
south direction.)
Đám cháy được
khống chếsau
hơn
nửa
giờ
đồng hồ.
(The
fire was brought
under
control
after more than
half an hour.)
Mô hình khó khăn trong
việc nhận biết nửa giờ
đồng hồvới 30 phút là
giống nhau, do đó có thể
dựđoán sai thành Con-
tradiction. (The difficulty
model recognizes that half an
hour and 30 minutes are the
same, so it can be wrong to
predict Contradiction.)
ViA2
E
C
E E E
Việt Trinh hái mít, xoài, dứa...
trĩu quảkhi vào mùa ởvườn
nhà rộng 3.000 m2.
(Viet
Trinh picks jackfruit, mango,
pineapple... laden with fruit in
season in a 3,000 m2 home gar-
den.)
Nhà Việt Trinh
rộng 3.000 m2.
(Viet
Trinh’s
house is 3,000 m2
wide.)
Tôi lược bỏchữ"vườn" để
tạo câu neutral và model
có thểnhầm thành entail-
ment.
I omitted the word
"garden" to create a neutral
sentence and model could be
mistaken for entailment.)
ViA3
N
C
N N E
Chính phủvừa đồng ý cho
các thương nhân nước ngoài
được nhập cảnh vào Việt
Nam thu mua vải thiều Bắc
Giang. (The Government has
just agreed to allow foreign
traders to enter Vietnam to buy
Bac Giang lychees.)
Vải
thều
Bắc
Giang chỉđược
trồng
ở
Bắc
Giang.
(Bac
Giang lychee is
only
grown
in
Bac Giang.)
Tôi dùng kiến thức thực tế
nhưng sai nên có thểmáy
sẽđoán thành neutral. (I
used practical knowledge but
it was wrong, so maybe the
machine will guess neutral.)
ViA2
N
C
C N N
Đại diện EVN cho biết, tập
đoàn không có hoạt động cho
vay tín chấp và không có
đơn vịtrực thuộc hay doanh
nghiệp liên kết có tên Ngân
hàng Điện lực Việt Nam. (A
representative of EVN said that
the group has no unsecured
lending activities and has no af-
filiated units or affiliated enter-
prises named Electricity of Viet-
nam Bank.)
EVN
không
có bất kì hoạt
động
cho
vay
tín
chấp
nào
trong thời gian
gần đây. (EVN
has
not
had
any
unsecured
lending activities
recently.)
Nêu thêm thời gian nên
mô
hình
sẽ
đoán
sai.
(Given more time, the model
will guess wrong.)
ViA3
E
C
E E C
50

--- Page 51 ---

Appendix B. Visual Length of Premise and Hypothesis of ViANLI
0
20
40
60
80
Sentence length (words)
0
50
100
150
200
250
Number of sentences
Premise
Hypothesis
(a) ViA1
0
20
40
60
80
Sentence length (words)
0
50
100
150
200
250
Number of sentences
Premise
Hypothesis
(b) ViA2
0
20
40
60
80
Sentence length (words)
0
50
100
150
200
250
300
Number of sentences
Premise
Hypothesis
(c) ViA3
0
20
40
60
80
Sentence length (words)
0
200
400
600
800
Number of sentences
Premise
Hypothesis
(d) ViANLI
0
20
40
60
80
100
Sentence length (words)
0
250
500
750
1000
1250
1500
1750
2000
Number of sentences
Premise
Hypothesis
(e) ViNLI
Figure B.12: Comparison of Length Distribution Between ViANLI and ViNLI.
Appendix C. Model Accuracy on Other Test Sets When Training Data is Combined
with Vietnamese Adversarial Data
51

--- Page 52 ---

Table C.18: Model Accuracy (%) on Other Test Sets When Training Data is Combined with Vietnamese Adver-
sarial Data. ViA1, ViA2, ViA3 Are the Data of Round 1, Round 2 and Round 3, Respectively. ViANLI Refers
to ViA1+ViA2+ViA3. VL Refers to the VLSP2021-NLI Dataset, and ViNe Refers to the VnNewsNLI Dataset.
Model
Training data
ViANLI
ViNLI
VLSP2021-NLI
VnNewsNLI
mBERT
ViNLI, XNLI (Vi)
27.50
66.21
70.16
72.87
+ ViA1
28.80
66.82
70.06
62.11
+ ViA1 + ViA2
31.90
65.85
70.20
58.60
+ ViA1 + ViA2 + ViA3
33.70
66.47
71.43
58.16
ViNLI, XNLI (Vi), ViA1, ViA2, ViA3, VL, ViNe
34.00
66.61
78.71
96.58
PhoBERTLarge
ViNLI, XNLI (Vi)
30.80
75.57
79.46
73.93
+ ViNe
31.80
75.66
79.32
97.18
+ ViNe + ViA1
34.70
75.57
80.35
97.58
+ ViNe + ViA1 + ViA2
36.80
75.39
80.55
97.81
+ ViNe + ViA1 + ViA2 + ViA3
39.20
75.13
80.73
97.78
ViNLI, XNLI (Vi), ViA1, ViA2, ViA3, VL, ViNe
41.00
75.22
87.72
97.51
XLM-RLarge
ViNLI, XNLI (Vi)
30.80
82.12
82.11
80.93
+ VL + ViNe
31.70
81.18
88.71
97.06
+ VL + ViNe + ViA1
34.00
82.59
89.14
96.68
+ VL + ViNe + ViA1 + ViA2
38.70
82.11
90.36
97.21
ViNLI, XNLI (Vi), ViA1, ViA2, ViA3, VL, ViNe
40.10
81.49
89.84
97.31
NLIMoEDynamic
ViNLI, XNLI (Vi)
30.90
82.33
83.56
80.21
+ VL + ViNe
30.30
82.37
89.14
97.19
+ VL + ViNe + ViA1
34.90
82.99
89.66
97.59
+ VL + ViNe + ViA1 + ViA2
38.30
82.55
89.75
97.53
ViNLI, XNLI (Vi), ViA1, ViA2, ViA3, VL, ViNe
40.60
82.59
90.58
97.72
52

--- Page 53 ---

Appendix D. Confusion Matrix of Pre-trained Language Models on the Development
Set
CONTRADICTION
ENTAILMENT
NEUTRAL
Predicted label
CONTRADICTION
ENTAILMENT
NEUTRAL
True label
61
69
203
13
162
159
63
53
217
25
50
75
100
125
150
175
200
(a) mBERT
CONTRADICTION
ENTAILMENT
NEUTRAL
Predicted label
CONTRADICTION
ENTAILMENT
NEUTRAL
True label
68
119
146
18
236
80
53
116
164
25
50
75
100
125
150
175
200
225
(b) PhoBERT
CONTRADICTION
ENTAILMENT
NEUTRAL
Predicted label
CONTRADICTION
ENTAILMENT
NEUTRAL
True label
152
99
82
61
223
50
130
108
95
60
80
100
120
140
160
180
200
220
(c) XLM-R
CONTRADICTION
ENTAILMENT
NEUTRAL
Predicted label
CONTRADICTION
ENTAILMENT
NEUTRAL
True label
128
78
127
60
192
82
72
99
162
60
80
100
120
140
160
180
(d) CafeBERT
CONTRADICTION
ENTAILMENT
NEUTRAL
Predicted label
CONTRADICTION
ENTAILMENT
NEUTRAL
True label
134
89
110
48
211
75
87
108
138
60
80
100
120
140
160
180
200
(e) NLIMoETopK
CONTRADICTION
ENTAILMENT
NEUTRAL
Predicted label
CONTRADICTION
ENTAILMENT
NEUTRAL
True label
77
82
174
28
204
102
35
87
211
50
75
100
125
150
175
200
(f) NLIMoEDynamic
Figure D.13: Confusion Matrix of Pre-trained Language Models on the Development Set.
53

--- Page 54 ---

Appendix E. Comparison of Predicted Labels by NLIMoEDynamic with Other Models
Table E.19: Comparison of Predicted Labels by NLIMoEDynamic with Other Models (E = Entailment, C = Con-
tradiction, N = Neutral).
Premise
Hypothesis
Gold
Label
Predicted Label
Activated
Expert
mBERT / PhoBERT / XLM-R / CafeBERT
NLIMoE
Xoắn tinh hoàn xảy ra khi
tinh hoàn di động quá
mức quanh thừng tinh,
dẫn đến tắc nghẽn hệ
thống mạch máu cấp tính.
(Torsion of the testicle oc-
curs when the testicle moves
excessively around the sper-
matic cord, leading to acute
vascular obstruction.)
Xoắn tinh hoàn chỉxảy
ra ởnam giới, không
xảy ra ởphụnữ.
(Testicular torsion only
occurs in males, not in fe-
males.)
E
N / C / C / N
N
[3]
Bệnh nhân được các giáo
sư đầu ngành Hội chẩn
Quốc gia ngày 18/5, tuy
nhiên
tình
trạng
bệnh
không
giảm,
tử
vong
ngày 20/5.
(The patient was consulted
by leading professors at the
National Consultation on
May 18, however, the condi-
tion did not improve, and the
patient passed away on May
20.)
Bệnh nhân tửvong sau
5 ngày hội chẩn.
(The patient died 5 days
after the consultation.)
C
N / E / E / E
E
[3, 5, 7]
Tổng thống Palau gặp
mặt lãnh đạo Đài Loan
Thái Anh Văn, cùng tham
gia sựkiện quảng bá du
lịch Palau cũng như tham
quan các công ty đóng tàu
và nuôi trồng thủy sản.
(The President of Palau met
with Taiwan’s leader, Tsai
Ing-wen, to attend an event
promoting Palau’s tourism
and to visit shipbuilding and
aquaculture companies.)
Lãnh đạo 2 nước Palau
và
Đài
Loan
cùng
nhau
tham
gia
sự
kiện quảng bá du lịch
Palau, đồng thời tham
quan các công ty đóng
tàu và nuôi trồng thuỷ
sản.
(The leaders of Palau
and Taiwan participated
in an event promoting
Palau’s
tourism
while
also visiting shipbuild-
ing
and
aquaculture
companies.)
E
N / N / C / N
E
[1, 3]
Ban đầu LG kỳvọng sẽ
tìm được khách hàng mua
lại nhà máy Hải Phòng với
giá 100 tỷwon (2.064 tỷ
đồng).
(Initially, LG expected to
find a buyer for the Hai
Phong factory at a price of
100 billion won (2.064 tril-
lion VND).)
LG định giá nhà máy
tại Hải Phòng với giá
dưới 2 nghìn tỷđồng.
(LG
priced
the
Hai
Phong factory at under 2
thousand billion VND.)
C
N / E / E / E
C
[3, 5, 6, 7]
54

--- Page 55 ---

Appendix F. Expert Activation Distribution across Inference Types
Figure F.14: Distribution of activation frequencies of experts in the proposed NLIMoEDynamic model across the
seven reasoning types on the ViANLI development set.
55

```
