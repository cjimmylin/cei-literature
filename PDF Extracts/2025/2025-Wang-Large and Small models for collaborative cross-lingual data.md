---
title: "2025-Wang-Large and Small models for collaborative cross-lingual data - PDF Extract"
source_pdf: "2025-Wang-Large and Small models for collaborative cross-lingual data.pdf"
pages: 22
extracted_at: "2026-02-13T17:43:25.694749"
---

# PDF Extract: 2025-Wang-Large and Small models for collaborative cross-lingual data

**Source PDF:** 2025-Wang-Large and Small models for collaborative cross-lingual data.pdf
**Total Pages:** 22

---

## Content

```
--- Page 1 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:56
https://doi.org/10.1007/s44443-025-00055-w
ORIGINAL PAPER
Large and Small models for collaborative cross-lingual data
augmentation in entity relationship extraction for low-resource
languages
Yurong Wang1,2,3 · Min Lin1,4,6 · Qitu Hu1,2,3 · Longjie Bao5 · Shuangcheng Bai4 · Yanling Li4
Received: 9 February 2025 / Accepted: 4 May 2025 / Published online: 5 June 2025
© The Author(s) 2025
Abstract
Entity relationship extraction tasks conducted in low-resource language domains (such as the medical and military domains)
have long faced signiﬁcant challenges, and data augmentation (DA) is considered an effective solution for addressing this
issue. Compared with monolingual DA methods, cross-lingual augmentation methods more effectively enhance the diversity
of data in low-resource language settings by leveraging and extending data resources derived from other languages. Unlike
traditional DA methods, large language model (LLM)-based DA reduces the reliance on manual evaluations and generates
more ﬂuent and diverse data. The superior performance of LLMs is attributed to their large-scale corpora and computational
resources, but these advantages also limit their applicability in cases involving low-resource languages. To address these
issues, this paper proposes LS-CLDARE, an entity relationship extraction framework based on collaborative cross-lingual
DA that employs both large and small models. Speciﬁcally, the small language model (SLM) is responsible for extracting
entity information, while the LLM generates cross-lingual samples by combining this entity information and its high-resource
language description via chain-of-thought (CoT) prompts, which guide the model through step-by-step reasoning to better
handle complex tasks. To achieve enhanced cross-lingual transfer performance, the generated cross-lingual samples are
combined with cross-lingual soft prompts and input into an SLM pretrained on a high-resource language domain dataset.
Through transfer learning and data expansion, the entity recognition and relation extraction capabilities for the low-resource
languages of the SLM are continuously improved. Extensive experiments conducted on ultralow-resource languages in the
Mongolian medical domain and classical Chinese texts validate the effectiveness of LS-CLDARE. Compared with those of
other DA methods, the F1 score was improved by 3.52% to 9.42%, and compared with those of other prompt-based relation
extraction methods, the F1 score was improved by 1.8% to 16.93%.
Keywords Collaboration of large and small models · Cross-lingual data augmentation · Chain-of-thought ·
Low-resource languages · Domain relation extraction
1 Introduction
Relation extraction (RE) is one of the core subtasks of infor-
mation extraction, and it aims to identify and extract the
semantic relationships between entities from text. Speciﬁ-
cally, RE can be divided into two forms: determining the
relationship between a known head entity and tail entity
(Zeng et al. 2014; Zhang et al. 2017; Sahu et al. 2019;
Xu et al. 2021) and predicting the corresponding tail entity
given a known head entity and relationship (Li et al. 2019;
Wang et al. 2023a). This task is crucial in natural language
Extended author information available on the last page of the article
processing (NLP) scenarios, as it not only provides key sup-
port for applications such as information retrieval (Kadry
and Dietz 2017) and question-answering systems (Sun et al.
2024; Chen et al. 2019) but also serves as an important
information resource for implementing complex knowledge
reasoning in large language models(LLMs) (Liu et al. 2024;
Wang et al. 2024). In recent years, signiﬁcant progress has
been made in terms of RE approaches that are based on deep
learning. However, these methods are typically designed for
high-resource scenarios and rely strongly on large datasets,
posing challenges for speciﬁc domains (e.g., the medical
and military domains) that involve low-resource languages.
General-domain data concerning low-resource languages are
already scarce, whereas domain-speciﬁc data are even harder
123

--- Page 2 ---

56
Page 2 of 22
Journal of King Saud University Computer and Information Sciences (2025) 37 :56
to obtain because of the need for expert knowledge and the
high cost of annotation.
To address the data scarcity issue, researchers have pro-
posed two main strategies. The ﬁrst strategy focuses on
improving the learning capabilities of models to more efﬁ-
ciently utilize existing data. For example, prompt learning
employs prompt templates to embed useful information into
model inputs, thereby alleviating the problem of insufﬁcient
data (Chen et al. 2024; Tang et al. 2024). Cross-lingual
RE transfers rich annotated data and knowledge from high-
resource languages to low-resource languages, enhancing the
performance of models that use in the latter (Ma et al. 2024;
Hsu et al. 2023; Li et al. 2024). Additionally, multitask learn-
ing improves the adaptability of models by training multiple
informationextractiontaskssimultaneously,enablingknowl-
edge sharing and complementarity (Sun et al. 2021). The
second strategy involves the use of data augmentation (DA)
to increase the amount of available data. From the perspec-
tive of data sources, DA techniques are typically divided
into two types: monolingual and cross-lingual approaches.
Monolingual methods rely on data within the target language
for augmentation purposes, whereas cross-lingual methods
leverage data resources involving other languages to achieve
diversity and enrichment through transfer and expansion.
In low-resource language scenarios, cross-lingual augmen-
tation effectively enhances the generalization and transfer
learning performance of the utilized model.
The traditional DA methods are typically rule-based
approaches (Cubuk et al. 2019; Krell and Kim 2017; Liu
et al. 2020; Takahashi et al. 2019; Zhang et al. 2024) that
generate new samples through operations such as inser-
tion, substitution, and deletion. These methods usually rely
on synonym dictionaries or manually set transformation
rules, lack an understanding of contextual semantics and
syntactic structure, and are prone to generating forged sam-
ples with grammatical errors or semantic inconsistencies. If
such low-quality samples are used for model training, the
model may learn expressions that do not conform to the
laws of the real language. This, in turn, weakens its abil-
ity to model entity boundaries, semantic relationships, and
language alignment patterns. Figure 1(a) illustrates how rule-
based augmentation operates in the low-resource Mongolian
medical domain given a labelled sentence. For example,
replacing
(chest tightness) with
(had
chest tightness) introduces an inappropriate change in tense,
whereas substituting
(myocardial infarction)
with
results in a missing possessive sufﬁx
,
leading to syntactic incompleteness. Such tense and struc-
tural deviations are particularly sensitive in medical contexts,
as the temporal and semantic boundaries of events are often
directly related to the recognition and judgement of ill-
nesses. Once ambiguous or mis-ordered representations exist
in the generated samples, they may interfere with the model’s
understanding of the causal relationship between symptoms
and diseases, signiﬁcantly reducing its accuracy and utility
value in downstream diagnostic assistance tasks. In addition
to using bilingual dictionaries for substitution, cross-lingual
DAmethodscanleveragemachinetranslationorparalleldoc-
uments from the same domain. For example, Xie et al. (2020)
and Hayashi et al. (2018) used back-translation to generate
new samples, whereas (Yamada and Ri 2024) utilized paral-
lel encyclopaedic data to translate entities into high-resource
languages, producing mixed cross-lingual augmented data.
However, such resources are often difﬁcult to obtain in spe-
ciﬁc domains, particularly for tasks involving low-resource
languages.
Fig. 1 Comparison of the four DA methods. Rule-based monolingual
DA relies on synonym dictionaries or handcrafted rules, often leading
to grammatical or semantic errors. Generation-based monolingual DA
may produce incorrect outputs in low-resource languages. Rule-based
cross-lingual DA depends on parallel corpora or dictionaries, which are
often unavailable in domain-speciﬁc settings. In contrast, our proposed
generation-based cross-lingual method produces ﬂuent and coherent
text without relying on external cross-lingual resources
123

--- Page 3 ---

Journal of King Saud University Computer and Information Sciences (2025) 37 :56
Page 3 of 22
56
To overcome these challenges, researchers are increas-
ingly adopting LLMs for DA purposes (Dai et al. 2023;
Samuel et al. 2023; Zhang et al. 2023b). By learning the
features and distributions of the original data, LLMs can
generate augmented samples that are structurally similar
but distinct in terms of content (Dai et al. 2023; Huang
et al. 2023), ensuring certain degrees of ﬂuency and coher-
ence in the generated text. For example, Kang et al. (2024)
generated sentences with various structures using entities
of the same type, whereas (Tian et al. 2024) employed a
collaboration between large and small models to ﬁlter LLM-
generated samples. The powerful capabilities of LLMs stem
from their extensive training on large-scale corpora and the
support of signiﬁcant computational resources. However,
in low-resource languages, LLM often generates inaccu-
rate or unrealistic information, a phenomenon known as
‘hallucination’. To systematically investigate this issue, we
constructed three sets of augmented samples (each con-
taining 1,000 samples) within the Mongolian medical text
domain, on the basis of three data augmentation methods:
LLM-based generation, rule-based replacement, and back-
translation. The results showed that approximately 14% of
the samples generated by the rule-based method contained
grammatical or semantic errors (as this method relies on dic-
tionary support), while the error rate for back-translation
was approximately 15% (with relatively monotonous con-
tent). In contrast, the hallucination rate of samples generated
by LLMs was signiﬁcantly higher. To identify the speciﬁc
manifestations of such hallucinations, we further analysed
the samples generated by LLMs. We found that approx-
imately 30% of these samples exhibited word creation
errors. For example,
was incor-
rectly changed to
; the word in green
font does not exist in Mongolian. About 50% of these sam-
ples also contained sequential or grammatical errors. For
example,
was incorrectly changed to
,inwhichthewordorderisclearly
abnormal. The green text in Figure 1(b) labels typical hallu-
cination content, covering grammatical errors, misspellings,
and irregular word formation. Such hallucinatory samples, if
used directly for model training, can easily lead the model
to learn structures or false semantics that do not conform
to the laws of language, which in turn interferes with its
performance in multiple downstream tasks. For example, in
named entity recognition, the model may misclassify illu-
sory words as entities, affecting boundary judgement, and in
bitext retrieval or cross-language alignment tasks, semantic
biasmaybeintroduced,reducingtheaccuracyandrobustness
of retrieval and matching.
Therefore, we believe that using LLMs to generate cross-
lingual samples for low-resource languages is a challenging
and complex task. Recently, prompt strategies such as chain-
of-thought (CoT) prompting (Wei et al. 2024) have gained
attention because they breakdown complex reasoning pro-
cesses into simpler steps and outperform standard methods in
many cases (Wang et al. 2025). For example, Liu et al. (2024)
ﬁrst identiﬁed entities in the given text and then performed
relation classiﬁcation and generated CoT prompts, allow-
ing the utilized LLM to answer questions in a step-by-step
manner.Inspiredbythesepreviousworks,weattempttocom-
bine the entity recognition capability of LLMs with the more
complex chain-of-through prompts in low-resource scenar-
ios to guide the model to generate structured data. To this end,
we conducted zero-sample entity recognition experiments by
using GPT-4o on the Mongolian Medical Entity Relationship
dataset (MDRE). With an accuracy rate of 33.5%, a recall
rate of 62.4%, and an F1 score of 43.59%, the experimental
results show that the proposed strategy has a limited effect on
practical application and that the LLM has difﬁculty accu-
rately identifying entities and their types. The speciﬁc types
of errors can be classiﬁed into three main categories. First,
LLMstendtowards‘broadrecall’,whichhasahighrecallrate
but a low accuracy rate and often misclassiﬁes many observa-
tional descriptions as entities. For example,
(muscle strength health) was incorrectly identiﬁed as a check
class entity. Second, there is a signiﬁcant bias in entity bound-
ary identiﬁcation, which is often redundant or truncated. For
example,
(bilateral lower limb swelling
on compression) should read
(swelling of
both lower limbs), and
(a strong heart-
beat) is then incorrectly truncated to
. Third,
there is confusion in the entity type judgement. In the case
of
(normal skin colour), for example, the
phrase was misclassiﬁed as an entity in the examination cat-
egory when it should actually be classiﬁed as a symptom
and sign. Tables 1 and 2 illustrate a typical case of the above
problem. On the other hand, previous studies have shown that
small language models (SLMs) based on prompt learning
can effectively learn entity spans and segment information
by combining prompt information with contextual semantics
(Cui et al. 2021; Liu et al. 2022). Inspired by these ﬁnd-
ings, we propose a collaborative approach involving large
and small language models to generate cross-lingual aug-
mented data. This approach decomposes the complex task of
low-resource data generation into multiple CoT-based step-
by-stepprompts,leveragingthestrengthsofbothmodeltypes
to achieve improved performance.
Nearly 7,000 languages exist worldwide, many of which
are low-resource languages that make it difﬁcult to effec-
tively leverage LLMs for data generation purposes. This
challenge is particularly evident in agglutinative languages
such as Mongolian, Kazakh, Uyghur, and Hungarian. These
123

--- Page 4 ---

56
Page 4 of 22
Journal of King Saud University Computer and Information Sciences (2025) 37 :56
Table 1 An Example of Entity Recognition by GPT-4o on a Dataset in the Field of Mongolian Medicine
languages typically use sufﬁxes or preﬁxes to convey gram-
matical functions, such as tense, case, and voice, resulting in
highly complex morphological variations.
In summary, entity RE for low-resource languages urgently
needs more effective solutions. Speciﬁcally, it requires a
method that ensures text ﬂuency, eliminates reliance on
additional parallel corpora, and enhances transfer learning
through data augmentation. To address these challenges,
we propose a collaborative cross-lingual DA framework
for entity RE named LS-CLDARE, which is illustrated in
Figure 2. First, an SLM is used to identify domain-speciﬁc
entities in low-resource language texts while describing their
types in high-resource languages, providing richer contex-
tual information for the LLM. Next, clear step-by-step data
generation rules are constructed on the basis of source lan-
guage prompts and, together with the original text, are input
into the LLM to generate cross-lingual samples that com-
binehigh- andlow-resourcelanguages. Finally, thegenerated
cross-lingual hybrid samples and the soft prompts, initial-
ized with entity-type or relation-type word vectors from the
high-resource language, are jointly fed into the SLM pre-
trainedonahigh-resourcedomaindataset.Throughmultitask
learning for entity recognition and relation extraction, the
model is guided to effectively transfer semantic knowledge
from the high-resource language to the low-resource lan-
guage. This approach ultimately enhances both the transfer
capability and the generalization performance. Speciﬁcally,
this study employs two cross-lingual data augmentation
strategies. First, it involves pretraining the RE model using
high-resource-domain datasets. Second, it generates mixed
high- and low-resource language datasets through the col-
laborative efforts of large and small models. Combined with
cross-lingual prompts, this strategy enhances the adaptability
of the model and its understanding of low-resource language
semantics. Extensive experiments conducted on a Mongo-
lian medical dataset and a Chinese classical text dataset
demonstrate the effectiveness of LS-CLDARE. Compared
with other DA methods, LS-CLDARE achieves F1 score
improvements of 3.52% to 9.42%, and compared with other
prompt-based RE models, it achieves F1 score improvements
of 1.8% to 16.93%.
Our contributions are as follows:
We propose LS-CLDARE, a collaborative cross-lingual
DA method involving large and small models that addresses
entity relation extraction tasks involving low-resource lan-
guages.
Table 2 An Example of Named Entity Recognition by DeepSeek-R1-Lite-Preview on a Classical Chinese Corpus
123

--- Page 5 ---

Journal of King Saud University Computer and Information Sciences (2025) 37 :56
Page 5 of 22
56
Fig. 2 LS-CLDARE architecture diagram
LS-CLDARE employs a CoT cross-lingual data genera-
tion approach that breaks the complex cross-lingual DA task
involving low-resource languages into multistep processes to
ensure the ﬂuency and semantic consistency of the generated
data.
Furthermore, LS-CLDARE integrates cross-lingual trans-
ferlearning,cross-lingualsoftpromptlearning,andmultitask
learning on the generated cross-lingual augmented dataset.
This strategy effectively facilitates the transfer of knowledge
from high-resource languages to low-resource languages and
signiﬁcantly enhances the RE performance for low-resource
languages.
The effectiveness of LS-CLDARE is validated on datasets
derivedfromtwolow-resourcelanguages,offeringapractical
and generalizable solution for conducting RE tasks involving
other low-resource languages.
2 Related work
2.1 Relation extraction
Currently, the available deep learning-based triple extraction
methods can be categorized into four main types: annotation-
based methods, table-ﬁlling methods, machine reading com-
prehension (MRC)-based methods, and generation-based
methods.
Annotation-based methods typically use binary classiﬁ-
cation to annotate sequences and determine the starting and
ending positions of entities and relations. Zheng et al. (2017)
proposed the use of the BIEOS schema to represent the begin-
ningsandendingsofentities,withthenumbers1and2usedto
label the head and tail entities, respectively. Yu et al. (2020)
and Wei et al. (2020) ﬁrst extracted head entities and then
jointly extracted the relations and their corresponding tail
entities based on the head entities.
Table-ﬁlling methods create a table for each relation.
Each table entry indicates whether the corresponding pair
of words holds the given relation. The relations are then
extracted based on these tables. Wang et al. (2020) proposed
TPLinker, which is a one-step joint extraction model that
addresses exposure bias and error propagation issues in mul-
tistep extraction scenarios. Shang et al. (2022) introduced the
OneRel model, which is similar to TPLinker but reduces the
number of label matrices from 2N+1 to N.
MRC-based methods treat entity RE as a multiturn
question-answering task, transforming entity and relation
extraction into a task that involves ﬁnding answer spans from
the input text (Li et al. 2019). This approach enables the
integrationofpromptlearningintoentityREmodels,enhanc-
123

--- Page 6 ---

56
Page 6 of 22
Journal of King Saud University Computer and Information Sciences (2025) 37 :56
ing their learning capabilities. Zhao et al. (2021) proposed
a mechanism for detecting entity spans through a diverse
question-answering scheme and then predicted the potential
subsets of relations and ﬁltered out irrelevant subsets. Chai
et al. (2023) developed a framework for extracting entities
and relations from ﬁnancial documents, utilizing multiturn
machine reading comprehension and the Longformer model
to handle long text dependencies.
With the emergence of generative pretrained models such
asBART,T5,andgenerativepretrainedtransformers,genera-
tive information extraction models have become increasingly
viable. Huguet Cabot and Navigli (2021) pretrained and ﬁne-
tuned BART on a large-scale, distantly supervised dataset. In
2022, researchers proposed the QA4RE framework (Zhang
et al. 2023a) to address the lack of instruction-based datasets
for RE tasks. Wan et al. (2023) improves entity-relation
correlations through logical reasoning, whereas (Li et al.
2023b) utilized natural language inference to generate rela-
tions. However, compared with that of entity recognition, the
RE performance gap exhibited by generative models is much
larger, especially for low-resource languages.
The above methods focus primarily on improving the
learning capabilities of models but do not fundamentally
expand data volumes. Therefore, leveraging the DA to further
increase the size of the utilized dataset becomes particularly
essential for achieving enhanced performance.
2.2 Data augmentation
Traditional DA techniques (Cubuk et al. 2019; Krell and
Kim 2017; Liu et al. 2020; Takahashi et al. 2019; Zhang
et al. 2024), such as image rotation, cropping, ﬂipping, and
rule-based natural language generation, have been widely
used to address data limitations. Wei and Zou (2019) gen-
erated new sentences by replacing, deleting, and inserting
relevant words, whereas (Mueller and Thyagarajan 2016)
used WordNet for synonym substitution to create additional
training data. Although these methods improve the diversity
of data and alleviate data scarcity issues to some extent, they
struggle to fully capture the complexity of data (Feng et al.
2021), cannot generate data at scale (Yang et al. 2022), fail
to ensure textual ﬂuency, and often exhibit different gram-
matical structures than those of the original data (Bayer et al.
2022). In addition to monolingual DA, another approach is
cross-lingual DA. Jiang et al. (2022) and Ri et al. (2022)
aligned words or phrases via bilingual dictionaries to gener-
ate cross-lingual data. Xie et al. (2020) and Hayashi et al.
(2018) created new samples through back-translation for
each given sentence, but this method relies on machine trans-
lation models trained on large-scale data. Yamada and Ri
(2024) expanded the target language corpora by incorporat-
ing English entity names, thereby generating mixed high-
and low-resource data. In summary, these cross-lingual DA
methods rely on domain-speciﬁc parallel documents or high-
quality bilingual dictionaries, which are often difﬁcult to
obtain in specialized domains.
To overcome these challenges, researchers have increas-
ingly turned to LLM-based data synthesis and augmentation
techniques (Dai et al. 2023; Samuel et al. 2023; Zhang et al.
2023b). These approaches reduce the reliance on manually
curated datasets and are capable of generating high-quality,
diverse data. For example, Kang et al. (2024) generated sen-
tences with various structures by using entities of the same
type, whereas (Tian et al. 2024) employed collaborative ﬁl-
tering between large and small models to ensure the ﬂuency
of LLM-generated text and mitigate label hallucination prob-
lems. However, for low-resource languages, the limited scale
of training data often results in LLM-generated samples that
lack ﬂuency and contain numerous semantic and grammati-
cal errors. To address these issues, we propose leveraging an
SLM to assist the employed LLM in generating cross-lingual
data,therebyreducingthenumberofhallucinationsproduced
when LLMs generate data for low-resource languages.
2.3 Collaborative large and small language models
The current approaches involving the collaboration of LLMs
and SLMs can be broadly categorized into two types. The ﬁrst
type integrates the outputs of an SLM as a component of the
overall framework to assist the corresponding LLM in bet-
ter completing downstream tasks (Xu et al. 2023; Leviathan
etal.2023).Forexample,Leviathanetal.(2023)combinedan
LLMandanSLMtoefﬁcientlyperformsupervisedtasks,and
Ding et al. (2024) proposed a large-small model collabora-
tion method to address the omission issues encountered when
extracting complex sentence triples via an LLM, signiﬁcantly
improving its triple extraction performance. Similarly, Tian
et al. (2024) employed collaborative ﬁltering between large
and small models to reﬁne LLM-generated samples. The sec-
ond type focuses on jointly training large and small models
to effectively utilize unlabelled data and reduce model biases
(Lang et al. 2022). Unlike these approaches, we propose a
novel method that uses collaboration between large and small
models to generate cross-lingual samples. To our knowledge,
no prior research has applied this approach to cross-lingual
DA in low-resource languages.
2.4 Chain of thought
To enable LLMs to address more complex logical reasoning
tasks, Wei et al. (2024) introduced the CoT concept, which
employs step-by-step reasoning processes to help models
gradually comprehend complex tasks, thereby enhancing
their contextual learning capabilities. Kojima et al. (2024)
discovered that simply adding the phrase “Let’s think step by
step” to a prompt enables LLMs to perform error-free log-
123

--- Page 7 ---

Journal of King Saud University Computer and Information Sciences (2025) 37 :56
Page 7 of 22
56
ical reasoning without additional human-designed prompts
(Chu et al. 2023). Auto-CoT (Zhang et al. 2022) eliminates
the instability of manually crafted prompts by automatically
constructing CoTs, and RE2 (Xu et al. 2024) uses question
rephrasing strategies to improve the model’s understanding
of zero-shot questions. Wang et al. (2023b) guided LLMs to
answer questions by decomposing them into planning and
solving steps via CoT prompts. ERA-CoT (Liu et al. 2024)
adopts a process in which entities in the given text are ﬁrst
identiﬁed; this process is followed by relationship classiﬁca-
tion, and then, CoT prompts are generated for the LLM to
answer. Inspired by these works, we decompose the complex
task of low-resource-language data generation into multistep
rules and constraints.
3 Methodology
To facilitate the explanation of the data generation and RE
components contained within the LS-CLDARE framework,
we deﬁne a cross-lingual data generation module named LS-
CLDA based on the collaboration of large and small models.
The SLM, which is responsible for entity and relation extrac-
tion, is referred to as the soft prompt knowledge extraction
(SPKE) model. Notably, SPKE also serves as the SLM within
the LS-CLDA module.
3.1 Definition of the cross-lingual DA task
In the cross-lingual DA task of RE, the problem to be solved
can be formalized as follows. Given a dataset T = {(Xi, Yi) |
i ∈[1, 2, . . . , m]}, where Xi = {xi,1, xi,2, . . . , xi,k rep-
resents the original input text and where Yi denotes its
corresponding labels, the label space Yr is deﬁned to include
all possible relational triples. The objective of DA is to gen-
erate new samples X′
i = {x′
i,1, x′
i,2, . . . , x′
i,k} along with
their corresponding labels Y ′
i , creating an augmented dataset
T ′ = {(X′
i, Y ′
i ) | i ∈[1, 2, . . . , n]} .
In the generated augmented samples X′
i, the nonentity
portion, denoted as x′
i, j , with its content expressed in the
source language (e.g., Chinese). The entity portion, which is
denoted by as x′
i,k, is expressed in the target language (e.g.,
Mongolian or classical Chinese).
3.2 Collaborative large and small language models
for cross-lingual DA
LLMs are capable of adapting to speciﬁc downstream tasks
by analysing input-output examples, which is a capability
known as in-context learning (ICL). ICL enables LLMs to
perform complex reasoning tasks within context and without
the need for explicit parameter adjustments. Xie et al. (2022)
introduced a latent concept, formalizing ICL as an implicit
Bayesian inference process within LLMs as follows:
p(X | prompt) =

p(X | θ∗, prompt)p(θ∗| prompt)dθ∗
(1)
here, θ∗represents the task-speciﬁc parameters or latent
states that are implicitly learned by the model on the basis of
the provided prompts. When generating outputs, the model
integrates the implicitly inferred parameters θ∗with the input
data X to derive the target results while also accounting
for the inﬂuence of θ∗on the ﬁnal output. This mechanism
revealstheunderlyingprinciplesofLLMsinin-contextlearn-
ing, further emphasizing the critical role of prompt design in
tasks, as well as the sensitivity and reasoning capabilities of
LLMs with respect to task contexts (Møller et al. 2024). To
capture this generation process, we introduce data generation
constraints and guidelines based on the CoT approach. By
employing step-by-step reasoning, we generate cross-lingual
data for low-resource languages, as detailed below.
Input The input consists of a text X and its corresponding
label, which form a set of relations R = {(s, p, o)}. Each re
lational triple is defined as (s, p, o) = (subject, predicate,
object).
Entity Recognition and Annotation via an SLM The trained
NER model SPKE is used to extract all entities Ei
=
{ei, j}k
j=1 and their corresponding types Ti = {ti, j}k
j=1 from
the input text X:
Ei, Ti = SPK E(X)
(2)
The entity set Ei is represented in the low-resource
language (target language), whereas the type set Ti is rep-
resented in the high-resource language (source language).
The reason for using the source language to represent entity
types is that it provides the LLM with richer and more com-
prehensible contextual information.
Prompt Construction for the LLM The complex task of
generating data for low-resource languages is decomposed
into multiple parts to construct CoT prompts, including text
generation rules, relation generation rules, and data output
formats.
Text Generation Rules: The input text X consists of an
entity part E and a nonentity part X −E, i.e., X = {xi |
xi ∈E} ∪{xi | xi /∈E}. The nonentity part xi /∈E is
translated into a logically clear high-resource language (e.g.,
Chinese); the entity part xi ∈E remains unchanged without
any translations, modiﬁcations, or omissions.
The reasons for including as many target language entities
as possible in the sample are as follows. First, the inclu-
sion of more target language entities enriches the source
123

--- Page 8 ---

56
Page 8 of 22
Journal of King Saud University Computer and Information Sciences (2025) 37 :56
language type annotation vocabulary related to the entities,
which not only increases the proportion of source language
text but also provides more complete contextual informa-
tion. This approach results in smoother and more logically
coherent cross-lingual text. Second, integrating all target
language entities into the sample effectively increases the
amount of data noise, preventing the model from relying
solely on language-speciﬁc features to directly recognize the
target language text during training, thereby enhancing its
generalizability.
RelationGenerationRules:Eachtriple(s, p, o)remaining
in the input relation set R is used as the output, i.e., R′ = R.
Data Output Format: The output data must include two
ﬁelds: text and spo_list. The text ﬁeld contains the newly
generated text, whereas the spo_list ﬁeld is a list of triples
that must remain consistent with the relations contained in
the input. Formally, the process generates three new texts
X′
1, X′
2, X′
3 and constructs their corresponding outputs O =
{(X′
1, R), (X′
2, R), (X′
3, R)}.
Data Filtering To ensure the quality of the generated data,
we ﬁrst pretrain the SPKE on the original annotated dataset
to equip it with basic entity recognition capabilities. A two-
stage ﬁltering process is then applied. In the ﬁrst stage, we
automatically check whether the entities in the generated
triples are explicitly present in the corresponding generated
text. If not, the sample is discarded; otherwise, it proceeds
to the next stage. In the second stage, we use the pretrained
SPKE model to identify entities and their types from the
generated sample and compare the recognized results with
the labels in the generated triple. If they match, the sample
is retained; if not, it is submitted for manual veriﬁcation.
Annotators assess whether the labels can be corrected based
on context; corrected samples are added to the ﬁnal dataset,
whereas uncorrectable samples are discarded. Although the
prompt template explicitly instructs the LLM to preserve
original entities and their labels during generation, halluci-
nations in low-resource languages may still introduce errors.
Therefore, this ﬁltering mechanism is essential for correct-
ing and reﬁning the generated data. The full process is shown
in Algorithm 1, and a detailed case analysis is provided in
Section 5.4.
3.3 Feedback loop: generating data to enhance
model training
In the LS-CLDARE framework, SPKE is responsible for
handling NER and RE tasks while assisting the LLM in gen-
erating cross-lingual augmented data. During each iteration,
SPKE and the LLM collaboratively generate cross-lingual
augmented data from the original training dataset Dtrain as
Algorithm 1 Data Filtering.
1: Input: Original annotated dataset Da, Generated dataset Dz
2: Output: Filtered dataset Db
3: Pretrain SPKE model on Da
4: Initialize Db ←Da
5: for each (xz, yz) ∈Dz do
6:
Check whether the triple yz exists in input xz
7:
if yz /∈xz then
8:
continue
▷Skip if entity not in text
9:
else
10:
Predict yd from xz using SPKE
11:
if yz = yd then
12:
Db ←Db ∪{(xz, yz)}
▷Add if prediction matches
13:
else
14:
Manually verify (xz, yz)
15:
if human conﬁrms or corrects yz then
16:
Db ←Db ∪{(xz, yz)}
▷Add corrected or conﬁrmed sample
17:
end if
18:
end if
19:
end if
20: end for
21: return Db
follows:
D(t)
train_DA = LLM(SPK E(t)(Dtrain))
(3)
The generated data is ﬁltered to remove invalid or irrele-
vant data, resulting in a veriﬁed augmented dataset:
D(t)
train_DA_veriﬁed = Filter(D(t)
train_DA, criteria=“valid triples”)
(4)
The veriﬁed augmented data is then merged with the exist-
ing training dataset:
D(t+1)
train = D(t)
train ∪D(t)
train_DA_veriﬁed
(5)
Subsequently, the expanded dataset is used to train and
update SPKE:
SPK E(t+1) = Train(SPK E(t), D(t+1)
train )
(6)
3.4 SPKE model
The SPKE model is composed of a “multilingual pretrained
model + pointer network,” where the multilingual pretrained
model is used for encoding and the pointer network is used
for decoding. Previous studies (Li et al. 2019; Wang et al.
2023a) have demonstrated that prompt learning can effec-
tively enhance the learning ability of a model. Therefore, we
unify NER and RE as span extraction tasks on the basis of
reading comprehension, thereby incorporating prompt learn-
ing into the framework.
3.4.1 Task deﬁnition
Given an input sequence X = {x1, x2, . . . , xL} with a length
of L, a task-speciﬁc question Qt is deﬁned for each task t ,
123

--- Page 9 ---

Journal of King Saud University Computer and Information Sciences (2025) 37 :56
Page 9 of 22
56
where t represents either the entity recognition task or the tail
entity recognition task for a triple. The text X is concatenated
with the question Qt then input into the pretrained model to
generate a matrix Ht as follows:
Ht = PLM(Qt, X) ∈R(L Q+L)×d
(7)
Here, L Q is the length of the question Qt , and d is the hidden
layer dimensionality. The concatenated sequence length is
L + L Q. The objective of the task is to predict the starting
and ending positions of the segments contained in the input
sequence that satisfy the task requirements.
3.4.2 Cross-lingual soft prompt construction
Prompt learning can be categorized into hard prompt learn-
ing and soft prompt learning. Hard prompt learning relies
on manually designed discrete templates, which require
task-speciﬁc customization. In contrast, soft prompt learn-
ing converts templates into optimizable continuous vectors,
which can be adaptively adjusted through training. Since soft
prompts are composed of a set of parameters, their perfor-
mance is highly sensitive to the initial parameters, especially
in low-resource language scenarios. To address this issue, we
propose initializing prompt templates using word embed-
dings derived from high-resource languages, leveraging
their rich semantic information and the prior knowledge
of pretrained models. These initialized templates transfer
knowledge to low-resource language tasks, and the prompt
templates include high-resource language-based prompts
and mixed high- and low-resource language prompts, which
are collectively referred to as cross-lingual prompt templates.
By employing these cross-lingual prompts, the generated
data can be utilized more effectively, further enhancing the
cross-lingual transfer learning capabilities of the constructed
model. Below, we provide a detailed introduction to soft
prompt templates and their initialization methods for use in
NER and RE tasks.
Initializing the soft prompts for the NER task by using
the word embeddings of the entity types derived from the
sourcelanguageisasimpleyetefﬁcientapproach.Incontrast,
initializing soft prompts for the RE task is more complex.
The question template for the RE task is formulated as
T (h,r) =“
” , where h repre-
sents the head entity (expressed in the target language) and
r represents the relation (expressed in the high-resource lan-
guage). For example,
“
”.
More speciﬁcally, the process begins by predicting the
head entity h , which is then combined with the relation r
and ﬁlled into the template. For each relation type ri, a corre-
sponding tail entity prediction prompt P(h,ri) is generated,
and then, the word embeddings P(h,ri) are used to initial-
ize the soft prompt Psoft(h,r). Through model training, the
prompt vector Psoft is dynamically learned to optimize the
performance of the tail entity prediction method.
3.4.3 SPKE input
Let PE = {e1, e2, . . . , ek} represent the word embedding
vector corresponding to the hard prompt for the NER or RE
task. The soft prompt initialization step is deﬁned as Psoft =
PE, where K denotes the length of the prompt vector. Let
X E = {x1, x2, . . . , xt} denote the word embeddings of the
input text X = {x1, x2, . . . , xt}. The soft prompt Psoft is then
concatenated with the input text embeddings X E, with the
addition of a start token [CLS] and an ending token [SEP],
to form the ﬁnal input sequence Einput as follows:
Einput = {[CLS], Psoft, X E, [SEP]}
(8)
3.4.4 Decoding in SPKE
Let the new matrix obtained from the input text processed
by the pretrained language model be denoted by H ∈Rn×d.
The matrix H is then input into two fully connected networks
to produce the following:
hα
start = Wα
startH + bα
start
(9)
hα
end = Wα
endH + bα
end
(10)
Here, hα
start and hα
end are matrices of size n × d. Wα
start and
Wα
end are the weight matrices of the fully connected layers
corresponding to entity types α, and bα
start and bα
end are their
biases:
Sα(i, j) = hα
start(i)⊤hα
end( j)
(11)
The score Sα(i, j) represents the span score for a segment
from position i to position j. Row coordinate i indicates the
start position of the span for entity or relation type α, while
column coordinate j represents the end position. The loss
function is deﬁned as:
log
⎛
⎝1 +

(i, j)∈Pα
e−sα(i, j)
⎞
⎠+ log
⎛
⎝1 +

(i, j)∈Qα
esα(i, j)
⎞
⎠
(12)
Here, Pα represents the set of all starting and ending position
pairs for entities of type α in the sample, whereas Qα denotes
the set of all starting and ending position pairs for nonentities
123

--- Page 10 ---

56
Page 10 of 22
Journal of King Saud University Computer and Information Sciences (2025) 37 :56
or entities that are not of type α in the sample. To simplify
this process, we consider only the combinations for which
i ≤j :
 = {(i, j) | 1 ≤i ≤j ≤n}
Pα = {(i, j) | t[i: j] is an entity of type α}
(13)
Qα =  −Pα
Although cross-lingual augmented datasets and cross-
lingual prompts have been introduced, fully improving the
performance of the model still requires the structural and
semantic knowledge accumulated from the relation extrac-
tion tasks in high-resource languages. To this end, we ﬁrst
pretrain the model on the high-resource relation extraction
dataset CMeIE-V2, enabling it to acquire the general knowl-
edge, such as structural patterns, semantic composition, and
label distributions, required for relation recognition. The
model is then further trained on cross-lingual augmented
data composed of both high- and low-resource languages,
along with the original data in the low-resource target lan-
guage. In this phase, the hybrid-language samples serve as a
semantic “bridge” that helps the model retain abstract seman-
tic representations from the source language while gradually
adapting to the lexical and syntactic characteristics of the tar-
get language, thus facilitating both structural and knowledge
transfer across languages. In addition, although both the aug-
mented and original data are predominantly expressed in the
target language, the prompt templates consistently use soft
prompts initialized from the entity types in the high-resource
language. This approach ensures that the model continuously
receives semantic guidance from the high-resource language
during both training and inference. This consistency in the
prompts not only enhances the model’s understanding of task
semantics but also strengthens contextual coherence in cross-
lingual semantic alignment.
4 Experiments
4.1 Datasets and implementation details
In the experiments, we used three datasets: the Chinese Med-
ical Entity-Relation (CMeIE-V2) dataset, the Mongolian
Medical Entity-Relation (MDRE) dataset, and the Chinese
Historical Text Entity-Relation (CHisIEC) dataset. Among
these datasets, the CMeIE-V2, MDRE and CHisIEC NER
datasets were used to pretrain the SPKE model. The MDRE
and CHisIEC relation datasets were employed to evaluate
the effectiveness of our proposed method. Detailed informa-
tion about the datasets is provided in Table 3. Notably, the
MDRE dataset exhibits a long-tailed distribution, as shown
in Table 4. Due to the uniqueness of Chinese historical texts
coupled with the scarcity of their corpora, they are classiﬁed
as low-resource languages. Although LLMs perform better
on Chinese historical texts than on Mongolian texts, their
performance still lags signiﬁcantly behind that achieved on
English and modern Chinese tests.
In the experimental setup and inspired by previous work
(Li et al. 2023a; Wei et al. 2023), we divided the data into
typical K-shot settings to simulate low-resource scenarios.
Speciﬁcally, the MDRE dataset was set to K = 10, 20, and
50, whereas the CHisIEC dataset was set to K = 5, 10,
and 15. Since Mongolian medical data constitute a double
low-resource scenario (in terms of both the language and the
domain), the K values were set relatively high to ensure the
effectiveness of the model. Detailed information regarding
the dataset splits and statistics is provided in Table 3. In the K-
shot scenario, when the number of triples was insufﬁcient, all
available data were used, and to facilitate an efﬁcient knowl-
edge transfer process via multilingual models, the Mongolian
text was Latin-transliterated. For a more realistic experimen-
tal representation, all subsequent ﬁgures and tables adopt the
Latin-transliterated Mongolian format.
The experiments were conducted on a single NVIDIA
A100 GPU with 80 GB of memory. For AugGPT and LS-
CLDA, we used the samples generated via GPT-4o, with the
temperature parameter set to 0.7. The prompt template used
for CoT-based data generation is shown in Table 5. Attempts
to use other versions of GPT yielded unsatisfactory results,
as they struggled to effectively complete the translation from
Mongolian to Chinese. During the SPKE training process,
we adopted MC-BERT (Wang 2023) as the backbone; MC-
BERT is a multilingual BERT model ﬁne-tuned on 150, 000
Mongolian monolingual sentences and 67, 200 Mongolian-
Chinese parallel sentence pairs. It consists of 12 transformer
layers, each with 768 hidden units and 12 attention heads.
The maximum input sentence length was set to 512, and the
Table 3 Detailed Information About the Splits and Statistics of the RE
Datasets
Datasets
Statistic
Dev Test Train
Full
10-shot 20-shot 50-shot
MDRE
Sentences 45
47
367
41
72
111
Triples
268
252
2587
80
151
312
Full
5-shot
10-shot 15-shot
CHisIEC Sentences 194
194
1560
31
63
90
Triples
824
810
6975
60
120
180
123

--- Page 11 ---

Journal of King Saud University Computer and Information Sciences (2025) 37 :56
Page 11 of 22
56
Table 4 Number of Relation Triples Contained in the MDRE Dataset
Relation
Clinical
Imaging
Laboratory
Auxiliary
Surgical
Drug
Traditional
Affected
Types
Manifestation
Examination
Examination
Examination
Treatment
Treatment
Therapy
Area
Count
670
43
35
13
49
155
1087
535
batch size was set to 8. Decoding in SPKE is performed by
using a Global Pointer Network, which effectively models
span-level entity and relation boundaries. The learning rate
was set to 2 × 10−5, the number of training epochs was 40,
and the threshold was set to 0.4.
4.2 Compared models
To validate the effectiveness of our proposed DA method,
we conducted comparative experiments with rule-based and
generation-based DA methods.
Base This method used the original dataset without any DA.
WSS (Mueller and Thyagarajan 2016): This method involves
synonym replacement that generates augmented datasets. In
the original paper, the public WordNet model was used for
replacement. However, due to the lack of publicly available
WordNet data in Mongolian, we adopted a dictionary-based
replacement method, taking a monolingual DA approach. For
the CHisIEC historical text dataset, which contains many real
historical ﬁgures and their relationships, the inherent charac-
teristics of the data make replacement operations infeasible.
AugGPT (Dai et al. 2023): This approach implements DA
through ChatGPT by generating new samples via speciﬁc
prompt templates. However, directly using AugGPT to gen-
erate Mongolian data results in severe hallucination issues.
For example, the generated triples were sometimes com-
pletely unrelated to the text content or failed to properly
replace the original text. To address this problem, we trans-
lated the nonannotated parts of the text into Chinese. This
method involves cross-lingual DA.
To validate the performance of LS-CLDARE within the
uniﬁed loop, which consists of data generation and entity RE,
and to fairly compare the effects of different DA methods,
we conducted experiments across various entity RE models.
TPLinker (Wang et al. 2020): This approach identiﬁes entity
pairs and their relationships in text by employing a “head-
tail” pairing mechanism.
OneRel (Shang et al. 2022): This method combines entity
recognition and relation classiﬁcation into a single step to
directly complete the RE task.
HugIE (Wang et al. 2023a): This approach improves the uti-
lization of data by using manually designed input prompt
templates, making it suitable for few-shot and low-resource
tasks.
In the experiments, all of the DA methods generated new
samples at a 1:3 ratio relative to the original dataset. The aug-
mented dataset was then combined with the original dataset
and used to train the RE models.
Table 5 Chain-of-Thought prompt template used by GPT-4o for generating task examples
123

--- Page 12 ---

56
Page 12 of 22
Journal of King Saud University Computer and Information Sciences (2025) 37 :56
Table 6 Experimental Results Produced by Different Models Various DA Methods on the MDRE Dataset
Model
Method
10-shot
20-shot
50-shot
full
P
R
F1
P
R
F1
P
R
F1
P
R
F1
TPLinker
Base
0
0
0
100
0.52
1.04
22.22
3.14
5.50
56.12
22.63
32.26
WSS
100
0.52
1.04
25.00
1.57
2.96
75.00
3.14
6.03
91.46
39.26
54.94
AugGPT
100
0.52
1.04
75.00
1.75
3.08
87.5
10.99
19.53
87.50
40.31
55.19
LS-CLDA
23.08
1.57
2.94
27.78
2.60
4.78
90.24
19.37
31.9
94.19
42.41
58.48
OneRel
Base
0
0
0
0
0
0
86.67
26.81
32.62
51.30
41.60
45.9
WSS
0
0
0
78.43
20.94
33.06
77.53
36.13
39.29
77.78
41.36
54.23
AugGPT
0
0
0
79.07
17.80
29.06
74.50
24.70
38.40
87.64
40.84
55.71
LS-CLDA
0
0
0
83.33
23.56
36.73
73.08
29.84
42.38
84.21
41.88
55.94
HugIE
Base
17.15
17.53
16.22
28.56
32.52
28.88
40.20
45.74
40.78
45.67
55.82
50.24
WSS
11.02
9.99
9.51
32.88
29.98
29.19
40.02
54.21
42.01
58.19
67.53
59.90
AugGPT
20.53
19.20
18.41
27.88
29.42
27.38
35.23
40.58
34.53
59.17
64.56
59.77
LS-CLDA
11.15
9.34
11.18
35.33
32.79
31.91
43.31
51.53
44.31
64.07
66.19
63.56
SPKE
Base
24.75
28.11
23.81
22.90
28.03
22.55
40.82
46.94
41.85
55.76
58.29
55.07
WSS
25.05
25.52
23.58
30.24
41.00
32.37
41.76
49.48
43.19
62.18
67.57
62.98
AugGPT
29.55
27.11
26.38
24.45
37.62
27.08
35.71
45.96
38.09
65.92
65.85
64.13
LS-CLDA
26.17
30.69
28.11
34.65
40.30
33.78
48.48
50.46
47.23
64.56
74.37
65.61
4.3 Main results
We evaluated the proposed LS-CLDARE framework on low-
resource language entity RE datasets, and the experimental
results are presented in Tables 6 and 7.
Comparison Among the DA Methods Most DA methods
outperform the baseline model (Base) without augmenta-
tion, demonstrating the effectiveness of DA techniques. Both
WSS and AugGPT improved the performance of the model
in low-resource scenarios to some extent but still lagged sig-
niﬁcantly behind LS-CLDA. On the MDRE dataset and using
SPKE, LS-CLDA achieved average F1 score improvements
of 3.52%, 6.44%, 6.18%, and 4.88% in the 10-shot, 20-
shot, 50-shot, and full settings, respectively. On the CHisIEC
dataset and using SPKE, LS-CLDA achieved average F1
score improvements of 4.49%, 9.42%, and 8.96% in the 5-
shot,10-shot,and15-shotsettings,respectively.Theseresults
indicate that LS-CLDA can generate more ﬂuent and diverse
samples than the other methods, signiﬁcantly enhancing the
model performance in low-resource scenarios.
Table 7 Experimental Results Produced by Different Models with Various DA Methods on the CHisIEC Dataset
Model
Method
5-shot
10-shot
15-shot
P
R
F1
P
R
F1
P
R
F1
TPLinker
Base
100
0.12
0.25
20.69
0.74
1.43
22.48
0.86
1.66
AugGPT
18.18
0.25
0.49
14.63
0.74
1.41
21.05
0.99
1.88
LS-CLDA
100
0.23
0.31
18.18
0.49
0.96
12.5
1.35
2.44
OneRel
Base
5.0
0.12
0.25
20.0
0.37
0.73
20.0
1.11
2.21
AugGPT
11.76
0.52
0.48
7.94
0.62
1.14
19.05
1.48
2.74
LS-CLDA
5.88
0.25
0.47
6.32
0.74
1.32
11.02
1.6
2.8
HugIE
Base
30.93
31.62
29.90
31.81
48.90
34.02
33.37
56.39
36.35
AugGPT
30.15
36.48
30.75
32.19
50.67
37.57
37.74
58.73
43.75
LS-CLDA
38.31
53.88
42.17
42.24
57.40
46.27
44.61
57.10
46.74
SPKE
Base
30.04
33.56
32.57
31.74
39.63
34.17
34.07
46.40
36.82
AugGPT
36.15
39.51
38.73
38.55
50.66
40.51
44.37
47.64
42.34
LS-CLDA
36.96
47.81
40.14
42.64
57.28
46.76
44.38
58.19
48.54
LS-CLDA(-CMeIE-V2)
26.42
39.92
30.10
35.55
49.02
39.62
40.18
58.52
46.00
123

--- Page 13 ---

Journal of King Saud University Computer and Information Sciences (2025) 37 :56
Page 13 of 22
56
Model Performance Comparison Overall, SPKE and HugIE,
two models based on prompt learning, consistently outper-
form TPLinker and OneRel, which rely on large amounts of
annotated data in low-resource scenarios. This performance
advantage is attributed not only to the prompting mechanism
itself but also to the model’s pretraining stage on the high-
resource language relation extraction dataset (CMeIE-V2).
During pretraining, the model ﬁrst learns the general knowl-
edge required for relation recognition from the high-resource
language, including structural patterns, semantic composi-
tion,andlabeldistributions.Subsequently,itisfurthertrained
on cross-lingual hybrid data and the original data from the
target low-resource language, thereby enabling structural and
semantic transfer from the high-resource source language to
the low-resource target language. To further validate the con-
tribution of pretraining to transfer performance, we introduce
an additional setup,“LS-CLDA (-CMeIE-V2)”, in Table 7, in
which the model was trained without any pretraining on the
CMeIE-V2 dataset and compared against the full training
strategy. The results show signiﬁcant performance degrada-
tion without pretraining: in the 5-shot, 10-shot, and 15-shot
settings, the F1 scores of the SPKE model decreased by
10.04%, 7.14%, and 2.54%, respectively, clearly demonstrat-
ing the critical role of high-resource language pretraining in
terms of enhancing cross-lingual transfer learning. In addi-
tion, we conducted more comprehensive ablation studies on
the MDRE task to further analyse the effectiveness of pre-
training in low-resource scenarios, as detailed in Section 4.5
and Table 9.
Moreover, SPKE, which uses cross-lingual soft prompts,
outperforms HugIE, which uses hard prompts in the target
language. This advantage is largely attributed to the learnable
nature of soft prompts, which allows the model to adap-
tively reﬁne their representations according to contextual
semantics during training. Compared with manually crafted
hard prompts, soft prompts offer greater ﬂexibility and
contextual sensitivity, especially in unstable low-resource
environments. Speciﬁcally, on the MDRE dataset using the
LS-CLDA augmentation method, SPKE outperforms HugIE
in the 10-shot, 20-shot, 50-shot, and full settings, with
average F1 gains of 16.93%, 1.87%, 2.92%, and 2.05%,
respectively. On the CHisIEC dataset, the performance gap
was narrower: SPKE achieves average F1 changes of -2.03%,
+0.49%, and +1.8% in the 5-shot, 10-shot, and 20-shot set-
tings, respectively. These results further demonstrate the
robustness and adaptability of soft prompts in cross-lingual
transfer learning. However, we also observe that SPKE
underperforms when compared to HugIE in the 5-shot set-
ting on CHisIEC. This phenomenon likely occurs because
soft prompts are parameterized and require sufﬁcient training
data to be effectively optimized. In extremely low-resource
scenarios, the limited number of samples makes it difﬁcult
for the soft prompt parameters to converge, thus diminish-
ing their advantage. In contrast, HugIE’s manually designed
hard prompts, while less ﬂexible, provide more stable guid-
ance in such settings. The ﬁxed inductive bias offered by
hard prompts may become beneﬁcial when training data are
scarce.
4.4 Analysis of different relation types
As shown in Table 4, the MDRE dataset exhibits an imbal-
anced distribution across different relation types, with a clear
long-tailed distribution. Therefore, it is crucial to conduct
experiments that individually analyse each relationship type.
We report the precision (P), recall (R), and F1 scores for
each relation to assess the model’s ﬁne-grained performance
across different categories. While the F1 score can reﬂect the
model’s ability to identify medium- and high-resource rela-
tion types to some extent, it is less reliable for low-resource
categories. In such cases, the score is easily inﬂuenced by
individual predictions and may exhibit a “false high” effect,
making accurate assessment of the model’s generalization
ability difﬁcult. To more objectively evaluate the model’s
overall performance under imbalanced data conditions, we
introduce the Macro-F1 metric, which is calculated as the
arithmetic mean of the F1 scores across all relation types.
Macro-F1 is not affected by class sample size when evaluat-
ing the overall model performance, making it an important
complement for assessing the model’s overall balance and
preventing misleading results due to high scores on low-
frequency categories.
We evaluated the SPKE model on the base dataset and the
datasets produced with the three DA methods. Table 8 shows
that all three DA methods improve the performance across
most relation types. However, the performance of WSS was
weaker than that of AugGPT and LS-CLDA, indicating
that rule-based DA methods are less effective than large
model-based generation methods. In addition, LS-CLDA
outperformed AugGPT, suggesting that the text generated by
LS-CLDA not only possesses stronger cross-lingual trans-
fer capabilities but is also more ﬂuent and natural. For
example, in terms of types such as “Clinical Manifesta-
tion,” “Affected Area,” and “Surgical Treatment,” LS-CLDA
performed signiﬁcantly better than did WSS and AugGPT.
Theserelationshiptypessharecommoncharacteristicsacross
Western medicine, traditional Chinese medicine, and Mon-
golian medicine. The LS-CLDA cross-lingual augmented
dataset, combined with the SPKE model, more effectively
transferred knowledge from high-resource languages to low-
resource languages, resulting in enhanced performance. We
can observe from Table 8 that certain relation types (such as
Laboratory Examination and Imaging Examination) achieve
relatively high F1 scores due to factors such as extremely
limited samples, lack of diversity, and well-deﬁned semantic
123

--- Page 14 ---

56
Page 14 of 22
Journal of King Saud University Computer and Information Sciences (2025) 37 :56
Table 8 Experimental Results Produced by Different DA Methods on the MDRE Dataset Across Various Relation Types
Method
Metric Clinical
Imaging
Laboratory
Auxiliary
Surgical
Drug
Traditional Affected Macro-F1 All Data
Manifestation Examination Examination Examination Treatment Treatment Therapy
Area
Base
P
64.21
37.50
33.33
50.00
20.00
42.85
42.47
22.97
55.76
R
75.65
50.00
100
50.00
20.00
23.07
50.09
22.07
58.29
F1
69.46
42.86
50.00
50.00
20.00
29.99
45.97
22.51
41.35
55.07
WSS
P
70.30
83.33
100
33.33
66.66
15.71
45.78
64.77
62.18
R
74.12
83.33
100
33.33
80.00
28.57
52.42
69.27
67.57
F1
71.14
83.33
100
33.33
70.00
20.23
44.95
66.21
61.15
62.98
AugGPT
P
75.74
83.33
100
33.33
80.00
28.57
50.80
65.76
65.92
R
77.63
83.33
100
33.33
100
19.04
53.19
68.01
65.85
F1
74.67
83.33
100
33.33
86.66
21.42
53.57
65.76
64.84
64.13
LS-CLDA P
78.90
83.33
100
66.66
80.00
23.80
49.75
66.75
64.56
R
80.70
83.33
100
66.66
80.00
23.80
73.85
75.22
74.37
F1
75.92
83.33
100
66.66
80.00
23.80
54.34
69.00
69.13
65.61
boundaries. However, such high scores do not necessar-
ily indicate strong generalizability. In these cases, greater
emphasis should be placed on the Macro-F1 metric, which
better reﬂects the model’s overall balanced performance
across all relation types. In low-resource language settings,
Macro-F1 provides a more reliable and interpretable indica-
torofthemodel’sabilitytohandleallrelationtypesuniformly
and is particularly suitable for real-world applications such
as medical diagnosis or fraud detection, where full coverage
of all categories is critical.
4.5 Ablation study
To verify the effectiveness of the different modules contained
in the LS-CLDARE framework, we conducted ablation
experiments across various relation types. The primary con-
tributions of LS-CLDARE involve two aspects: the ﬁrst is
the collaborative cross-lingual data generation scheme using
large and small models, which was used to conduct abla-
tion experiments to analyse the contribution of the SLM;
the second is the SPKE extraction model, which was pre-
trained on the CMeIE-V2 high-resource Chinese medical
dataset and was designed to efﬁciently utilize the generated
cross-lingual data. These experiments evaluate the impact
of the CMeIE-V2 dataset on the performance of the model
and provide insights into how each module contributes to the
overall effectiveness of the LS-CLDARE framework.
During the data generation procedure, the SLM respon-
sible for entity recognition was ablated (-SLM). In this
scenario, the large model identiﬁed entities in the text based
Table 9 Results of Ablation Experiments Conducted on the MDRE Dataset
Relation Type Metric Clinical
Imaging
Laboratory
Auxiliary
Surgical
Drug
Traditional
Affected Area All data
Manifestation Examination Examination Examination Treatment Treatment Therapy
-SLM
P
69.21
83.33
100
33.33
70.00
19.04
46.59
65.54
59.76
R
75.21
83.33
100
33.33
100
23.80
64.99
81.08
72.3
F1
70.09
83.33
100
33.33
79.90
18.57
50.36
69.57
62.54
-CMeIE-V2
P
68.85
83.33
100
16.66
45.00
11.90
47.12
64.95
60.93
R
80.04
83.33
100
33.33
80.00
23.80
78.80
76.12
63.43
F1
70.12
83.33
100
22.22
54.66
15.30
53.15
67.34
60.20
All
P
78.90
83.33
100
66.66
80.00
11.90
49.75
66.75
64.56
R
80.70
83.33
100
66.66
80.00
19.04
73.85
75.22
74.37
F1
75.92
83.33
100
66.66
80.00
12.85
54.34
69.00
65.61
123

--- Page 15 ---

Journal of King Saud University Computer and Information Sciences (2025) 37 :56
Page 15 of 22
56
on the CoT prompts and annotated these entities in Chinese.
New text was subsequently generated on the basis of the
identiﬁed entities and their types to create cross-lingual data.
While the generated text may have lacked ﬂuency in this case,
it could at least ensure the accuracy of the Mongolian con-
tent. As shown in Table 9, when the small model was ablated
(-SLM), the performance attained across most relation types
decreased, with an average decrease of 4.61%. This ﬁnding
indicates that the use of an SLM for entity recognition results
in more ﬂuent and diverse text generation, which enhances
the performance of low-resource, few-shot RE models.
After ablating the pretraining task implemented on the
Chinese medical dataset (-CMeIE-V2), the overall model
performance decreased signiﬁcantly, particularly for relation
types such as “Clinical Manifestation,” “Auxiliary Examina-
tion,” and “Surgical Treatment,” where the corresponding
F1 scores decreased by 5.8%, 44.44%, and 25.34%, respec-
tively. The Chinese medical dataset contains a wealth of
domain-speciﬁc knowledge, including professional termi-
nology, entity relationships, and contextual information,
which helps the model better understand and extract rela-
tionships between entities. During transfer learning, Chinese
medical data serve as a critical semantic bridge, laying a solid
foundation for the subsequent cross-lingual augmentation
and model training tasks, thereby effectively improving the
performance of the model in low-resource language domains.
5 Discussion
5.1 Text fluency analysis
The use of perplexity (PPL) to evaluate text ﬂuency is a com-
mon and effective approach. Perplexity serves as an indicator
of the reliability of a language model in terms of generating
or predicting text. The lower the PPL value is, the closer
the associated text aligns with the probability distribution of
the utilized language model, which in turn indicates greater
ﬂuency.
P PL = exp

−
	M
d=1 log p(wd)
	M
d=1 Nd

(14)
Figure 3 shows that AugGPT has the highest perplexity,
clearly indicating that directly using large-scale language
models to generate text in low-resource scenarios often
results in disﬂuency and even logical incoherence. Among
all of the DA methods, LS-CLDA achieves the lowest per-
plexity, demonstrating that this method generates the most
ﬂuent and coherent text.
5.2 Sample diversity analysis
Increasing the diversity of training data helps enhance the
adaptability of the employed model to different linguistic
features and expressions, thereby improving its generaliza-
tion performance. To quantify this effect, we introduce topic
diversity and topic consistency as evaluation metrics (Mimno
et al. 2011). Topic diversity measures the breadth and uni-
formity of the topic distribution within the dataset, assessing
its coverage of various linguistic patterns. As shown in (14),
it is calculated as the percentage of unique words appearing
among the top NNN words across all KKK topics. A diver-
sity score close to 0 indicates topic redundancy, whereas a
score close to 1 indicates diverse topics.
T D =
unique(ω(1)
topN, ω(2)
topN, . . . , ω(k)
topN)
K × N
(15)
Topic consistency, on the other hand, evaluates the coher-
ence and logical consistency of the given data to ensure that
while the diversity level is increased, the semantic relevance
and task alignment of the data are maintained. It measures the
quality of topics via the average pointwise mutual informa-
tion (APMI) between any two words within the same topic,
as expressed in (16). A higher APMI value indicates stronger
word associations within the topic and, consequently, higher
topic quality.
f (wi, w j) =
log
p(wi,w j)
p(wi)p(w j)
−log p(wi, w j)
(16)
The experimental results, shown in Figure 4, indicate
that the augmented datasets outperform the original datasets
in terms of both diversity and consistency. Compared with
monolingual data, the cross-lingual data generated by the
LLM exhibited better performance because of the introduc-
tion of richer and more diverse textual content. Among the
evaluated methods, LS-CLDA achieves the highest com-
bined score for topic diversity and topic consistency, further
Fig. 3 Results of the perplexity analyses
123

--- Page 16 ---

56
Page 16 of 22
Journal of King Saud University Computer and Information Sciences (2025) 37 :56
validating the effectiveness and advantages of our approach
in terms of DA.
5.3 Case study of different DA methods
To further evaluate the effectiveness of our proposed method,
we compared the examples generated by different DA meth-
ods, as shown in Table 10.
Rule-Based Methods
These methods do not alter the text
structure but may result in less ﬂuent text generation results.
For example, implementing synonym replacement via WSS
leads to semantic inconsistencies, such as the generation of
“CEGEJI DUGRUGSEN AMISGVL BACIMDAN” (short-
ness of breath due to chest tightness), which lacks semantic
coherence.
LLM-Generated
Cross-Lingual
Text Directly generating
Mongolian-Chinese cross-lingual text via LLMs often results
in signiﬁcant hallucinations and disﬂuent text. For exam-
ple, when employing the AugGPT method, a sentence such
as “
JIRUHE HADHVLG_A-YIN EBEDCINIYER
CEGEJI DUGURCU
AMISHVL CIHVL-
DAHV” (translated to English as “The patient’s symptoms of
myocardial infarction include chest tightness and shortness
of breath”) clearly demonstrates disﬂuency, overly simplistic
contexts, and insufﬁciently rich narratives.
LS-CLDA This method achieves the highest generation qual-
ity, maintaining ﬂuency while ensuring rich and diverse text
content. It effectively addresses the issues of coherence and
richness, demonstrating its superior performance in terms of
generating high-quality augmented data.
5.4 LS-CLDA case study
Table 11 provides a case generated by LS-CLDA, includ-
ing the prompt, input, and output. Overall, the model
generated relatively ﬂuent and logical Mongolian-Chinese
cross-lingual mixed samples upon receiving the instructions.
However, some limitations remain.
Hallucination While constructing the Mongolian dataset,
hallucinations occasionally occurred. For example, some-
Fig. 4 Results of the consistency and diversity analyses
times, the model retained the original input text instead of
translating it. In contrast, such hallucinations were less fre-
quent in tasks involving the generation of historical texts.
Label Errors The generated results may have included incor-
rect labels. For example, in the third generated sample shown
in Table 11, a triple (indicated by the underlined part) was
produced but was not present in the generated text.
Untranslated Nonentity Text Although the model was
instructed to translate nonentity text into Chinese, errors still
occurred. For example, “EGUDEN EMNELGE” in the ﬁrst
sample shown in Table 11 and “MAN-U H0RIYAN-U EGU-
DEN EMNELGE” in the second sample were not translated
into Chinese, even though they were not designated to be
medical entities. This oversight indicates a weakness in the
adherence of the model to translation rules.
Uneven Entity Distribution When instructed to generate
three sentences, each containing all of the given entities,
the model exhibited inconsistent performance. Sometimes,
entities were distributed across different sentences, failing to
satisfy the requirement that each sentence should include all
entities.
In conclusion, while our method reduces hallucination to
some extent when working with low-resource languages, the
issue is not entirely eliminated. This issue highlights the need
for continued research and exploration in this ﬁeld.
5.5 Ethical considerations
Using LLMs to automatically generate medical texts may
result in issues such as hallucinations, factual inaccuracies,
or semantic ambiguities. If not rigorously screened, such
content could misdirect downstream tasks and even pose
potential safety risks. To mitigate these risks, we designed
a robust data ﬁltering pipeline that integrates both automatic
validation and manual veriﬁcation mechanisms, ensuring the
accuracy and reliability of the generated data. All generated
data in this study were used strictly for research purposes
and did not involve any real patient information or clini-
cal decision-making. In future work, we plan to incorporate
a more comprehensive ethical AI framework and enhance
human-in-the-loopmechanismstofurtherimprovethesafety,
controllability, and traceability of LLMs in high-sensitivity
domains such as healthcare.
In addition, all original data used in this study were
thoroughly deidentiﬁed in accordance with the Health Insur-
ance Portability and Accountability Act (HIPAA) standards,
including the removal of all sensitive personal information
123

--- Page 17 ---

Journal of King Saud University Computer and Information Sciences (2025) 37 :56
Page 17 of 22
56
Table 10 provides a case comparison analysis of different da methods
The text is annotated as follows: red indicates Mongolian medical entities, blue represents newly generated or replaced text, and black denotes
nonentity parts of the original text. And provides the corresponding full Chinese translation
such as names, addresses, and dates of birth, thereby ensuring
data privacy and security.
5.6 Practical application potential
The proposed LS-CLDARE framework has demonstrated
strong performance when executing cross-lingual entity and
relation extraction tasks under low-resource settings, indi-
cating a promising potential for real-world applications.
Its advantages are particularly notable in sensitive domains
such as healthcare and the military, where accurate language
understanding is critical.
In the healthcare domain, the extreme scarcity of medi-
cal data in low-resource languages poses serious challenges
for medical entities and relation extraction, thereby hindering
the effective development of applications such as intelligent
diagnosis and intelligent therapy. LS-CLDARE proposes a
cross-lingual data augmentation strategy that leverages high-
resource languages (such as Chinese and English) to generate
medical-related cross-lingual data, signiﬁcantly improving
the accuracy of information extraction from medical texts in
low-resource languages. For example, in the case of lim-
ited clinical data in Mongolian, LS-CLDARE can utilize
high-resource languages to construct high-quality training
samples, enhancing the model’s ability to process Mongo-
lian medical texts. However, considering the sensitive nature
of medical data, further research is needed to investigate the
authenticity and ethical risks of the generated data to prevent
hallucinations or biases introduced by LLMs, which may
compromise the reliability of downstream clinical decisions.
In the military domain, cross-lingual intelligence anal-
ysis often involves multiple low-resource languages, par-
ticularly in multilingual regions such as the Middle East
and Central Asia. LS-CLDARE has the potential to enhance
multilingualinformationextractioncapabilitiesinthesecom-
plex language settings, thereby improving the automation
and overall efﬁciency of intelligence processing. However,
given the high security and conﬁdentiality requirements
of military data, further reﬁnement of the data genera-
tion and ﬁltering mechanisms is necessary to ensure the
reliability, controllability, and compliance of the generated
content. Future research may incorporate secure strategies
and human-in-the-loop mechanisms to increase the applica-
bility of LS-CLDARE in sensitive real-world scenarios.
6 Conclusions
We propose a framework for the collaboration of large and
small language models that is designed to perform cross-
lingual DA in low-resource language RE tasks. LLMs exhibit
strong contextual understanding in high-resource languages
but perform less effectively in low-resource languages, par-
ticularly minority languages in China. In contrast, small
language models excel at completing fundamental tasks such
as entity recognition. To address the limitations of individ-
ual models, we propose a collaborative method that combines
123

--- Page 18 ---

56
Page 18 of 22
Journal of King Saud University Computer and Information Sciences (2025) 37 :56
Table 11 Provides an analysis of the cross–lingual samples generated by LS-CLDA
The “text” ﬁeld is annotated as follows: red indicates Mongolian medical entities, blue represents newly generated or replaced text, and black
denotes nonentity parts of the original text, which should be translated into Chinese in the generated text to be considered correct.
large and small language models, applying it for the ﬁrst time
to cross-lingual DA tasks involving low-resource languages.
Speciﬁcally, the framework ﬁrst uses an SLM to iden-
tify domain-speciﬁc entities in low-resource languages while
describing the entity types contained in high-resource lan-
guages to retain their critical information and provide LLMs
with richer contextual information. Then, it generates cross-
lingual samples that mix high- and low-resource languages
via CoT prompts. On this augmented dataset, the framework
combines cross-lingual transfer learning, cross-lingual soft
prompt learning, and multitask learning to successfully trans-
fer knowledge from high-resource languages to low-resource
languages, signiﬁcantly improving the RE performance for
low-resource languages. The effectiveness of LS-CLDARE
was validated on two low-resource language datasets, pro-
viding a reference solution for conducting RE tasks in other
low-resource languages. However, the proposed framework
still has room for improvement.
First, due to signiﬁcant differences among various types
of low-resource languages in terms of syntactic structure,
morphological complexity, and data availability, the general-
izability of LS-CLDARE still requires further investigation.
Future research may explore the applicability of our method
to a wider range of low-resource languages (such as Hmong,
Tibetan, and Uyghur), particularly in scenarios involving
greater structural divergence or different writing systems.
In addition, future work could explore multilingual joint
training strategies to leverage the shared characteristics of
123

--- Page 19 ---

Journal of King Saud University Computer and Information Sciences (2025) 37 :56
Page 19 of 22
56
multiple low-resource languages, thereby further enhancing
the effectiveness of cross-lingual data augmentation.
Second,similartootherLLM-baseddatagenerationmeth-
ods, the proposed method may produce incorrectly labelled
data. Future work could explore an intelligent ﬁltering
scheme for LLM-generated data. For example, multiagent
adversarial learning (MAAL) can be introduced, in which
one agent generates data while another ﬁlters and veriﬁes
their quality. The ﬁltering agent, which acts as a discrimina-
tor, can evaluate the accuracy of the generated data, further
improving their reliability.
Finally, due to the limited training data available for LLMs
in low-resource languages, future work could ﬁrst ﬁne-tune
LLMs via machine translation data derived from general
domains. This approach will enhance the understanding of
the model and its generation capabilities in terms of target-
ing low-resource languages, providing a stronger foundation
for generating more reliable domain-speciﬁc cross-lingual
samples.
Acknowledgements This work was supported in part by the National
Natural Science Foundation of China (NSFC) under grant (62266033),
in part by the Key Laboratory of Inﬁnite-dimensional Hamiltonian Sys-
temandItsAlgorithmApplication(InnerMongoliaNormalUniversity),
Ministry of Education (2023KFZD03), and in part by the Graduate Stu-
dents’ Research Innovation Fund of Inner Mongolia Normal University
(CXJJB23011).
AuthorContributions YurongWang:Writing–OriginalDraft,Method-
ology, Software. Min Lin: Writing–Original draft preparation, Writing-
Reviewing and Editing. Longjie Bao: Resources, Data curation. Huqitu:
Data curation, Investigation. Shuangcheng Bai: Supervision. Yanling
Li: Supervision.
Funding This work was supported in part by the National Natural Sci-
ence Foundation of China (NSFC) under grant (62266033), and in part
by the Graduate Students’ Research & Innovation Fund of Inner Mon-
golia Normal University (CXJJB23011).
Data Availability Data will be made available on reasonable request.
Declarations
Conﬂicts of Interest The authors declare that they have no conﬂict of
interest.
Open Access This article is licensed under a Creative Commons
Attribution-NonCommercial-NoDerivatives 4.0 International License,
which permits any non-commercial use, sharing, distribution and repro-
duction in any medium or format, as long as you give appropriate credit
to the original author(s) and the source, provide a link to the Creative
Commons licence, and indicate if you modiﬁed the licensed mate-
rial. You do not have permission under this licence to share adapted
material derived from this article or parts of it. The images or other
third party material in this article are included in the article’s Creative
Commons licence, unless indicated otherwise in a credit line to the
material. If material is not included in the article’s Creative Commons
licence and your intended use is not permitted by statutory regula-
tion or exceeds the permitted use, you will need to obtain permission
directly from the copyright holder. To view a copy of this licence, visit
http://creativecommons.org/licenses/by-nc-nd/4.0/.
References
Bayer M, Kaufhold MA, Reuter C (2022) A survey on data augmenta-
tion for text classiﬁcation. ACM Comput Surv 55(7):1–39
Chai Y, Chen M, Wu H et al (2023) Fin-emrc: an efﬁcient machine
reading comprehension framework for ﬁnancial entity-relation
extraction. IEEE Access 11:82685–82695. https://doi.org/10.
1109/ACCESS.2023.3299880
Chen ZY, Chang CH, Chen YP, et al (2019) UHop: an unrestricted-
hop relation extraction framework for knowledge-based question
answering. In: Burstein J, Doran C, Solorio T (eds) Proceed-
ings of the 2019 Conference of the North American Chapter of
the Association for Computational Linguistics: Human Language
Technologies, Volume 1 (Long and Short Papers). Association
for Computational Linguistics, Minneapolis, Minnesota, pp 345–
356. https://doi.org/10.18653/v1/N19-1031 https://aclanthology.
org/N19-1031/
Chen Y, Shi B, Xu K (2024) Ptcas: prompt tuning with continuous
answer search for relation extraction. Inf Sci 659:120060
Chu Z, Chen J, Chen Q et al (2023) A survey of chain of thought
reasoning: advances, frontiers and future. arXiv:2309.15402
Cubuk ED, Zoph B, Mane D et al (2019) Autoaugment: learning aug-
mentation strategies from data. In: Proceedings of the IEEE/CVF
conference on computer vision and pattern recognition, pp 113–
123
Cui L, Wu Y, Liu J, et al (2021) Template-based named entity recogni-
tion using BART. In: Zong C, Xia F, Li W, et al (eds) Findings of the
Association for Computational Linguistics: ACL-IJCNLP 2021.
Association for Computational Linguistics, Online, pp 1835–
1845. https://doi.org/10.18653/v1/2021.ﬁndings-acl.161 https://
aclanthology.org/2021.ﬁndings-acl.161/
Dai H, Liu Z, Liao W et al (2023) Auggpt: leveraging chatgpt for text
data augmentation. arXiv:2302.13007
Ding Z, Huang W, Liang J et al (2024) Improving recall of large lan-
guage models: a model collaboration approach for relational triple
extraction. arXiv:2404.09593
Feng SY, Gangal V, Wei J et al (2021) A survey of data augmen-
tation approaches for NLP. In: Zong C, Xia F, Li W, et al
(eds) Findings of the Association for Computational Linguistics:
ACL-IJCNLP 2021. Association for Computational Linguistics,
Online, pp 968–988. https://doi.org/10.18653/v1/2021.ﬁndings-
acl.84 https://aclanthology.org/2021.ﬁndings-acl.84/
HayashiT,WatanabeS,ZhangYetal(2018)Back-translation-styledata
augmentation for end-to-end asr. In: 2018 IEEE spoken language
technology workshop (SLT), IEEE, pp 426–433
Hsu C, Zan C, Ding L et al (2023) Prompt-learning for cross-lingual
relation extraction. In: 2023 International joint conference on neu-
ral networks (IJCNN), IEEE, pp 1–9
Huang H, Wei X, Shi G et al (2023) Boosting event extraction with
denoised structure-to-text augmentation. arXiv:2305.09598
Huguet Cabot PL, Navigli R (2021) REBEL: relation extraction by end-
to-end language generation. In: Moens MF, Huang X, Specia L,
et al (eds) Findings of the association for computational linguis-
tics: EMNLP 2021. Association for Computational Linguistics,
Punta Cana, Dominican Republic, pp 2370–2381. https://doi.org/
10.18653/v1/2021.ﬁndings-emnlp.204
https://aclanthology.org/
2021.ﬁndings-emnlp.204/
Jiang X, Liang Y, Chen W et al (2022) Xlm-k: improving cross-lingual
language model pre-training with multilingual knowledge. In: Pro-
ceedings of the AAAI conference on artiﬁcial intelligence, pp
10840–10848
123

--- Page 20 ---

56
Page 20 of 22
Journal of King Saud University Computer and Information Sciences (2025) 37 :56
Kadry A, Dietz L (2017) Open relation extraction for support passage
retrieval: merit and open issues. In: Proceedings of the 40th inter-
national ACM SIGIR conference on research and development
in information retrieval. Association for Computing Machinery,
New York, NY, USA, SIGIR ’17, pp 1149-1152. https://doi.org/
10.1145/3077136.3080744
Kang H, Seo H, Jung J, et al (2024) Guidance-based prompt data aug-
mentation in specialized domains for named entity recognition.
In: Ku LW, Martins A, Srikumar V (eds) Proceedings of the 62nd
annual meeting of the association for computational linguistics
(Volume 2: Short Papers). Association for Computational Linguis-
tics, Bangkok, Thailand, pp 665–672. https://doi.org/10.18653/
v1/2024.acl-short.61 https://aclanthology.org/2024.acl-short.61/
Kojima T, Gu SS, Reid M et al (2024) Large language models are zero-
shotreasoners.In:Proceedingsofthe36thinternationalconference
on neural information processing systems. Curran Associates Inc.,
Red Hook, NY, USA, NIPS ’22
Krell MM, Kim SK (2017) Rotational data augmentation for elec-
troencephalographic data. In: 2017 39th Annual international
conference of the IEEE engineering in medicine and biology soci-
ety (EMBC), IEEE, pp 471–474
Lang H, Agrawal M, Kim Y et al (2022) Co-training improves
prompt-based learning for large language models. In: International
conference on machine learning. https://api.semanticscholar.org/
CorpusID:246472998
Leviathan Y, Kalman M, Matias Y (2023) Fast inference from trans-
formers via speculative decoding. In: International conference on
machine learning, PMLR, pp 19274–19286
Li T, Wang Z, Chai L et al (2024) mt4crossoie: multi-stage tuning
for cross-lingual open information extraction. Expert Syst Appl
255:124760
Li J, Jia Z, Zheng Z (2023b) Semi-automatic data enhancement for
document-level relation extraction with distant supervision from
large language models. In: Bouamor H, Pino J, Bali K (eds) Pro-
ceedings of the 2023 conference on empirical methods in natural
language processing. Association for Computational Linguis-
tics, Singapore, pp 5495–5505.https://doi.org/10.18653/v1/2023.
emnlp-main.334 https://aclanthology.org/2023.emnlp-main.334/
Liu AT, Xiao W, Zhu H et al (2022) Qaner: Prompting question
answering models for few-shot named entity recognition.
ArXiv:2203.01543
https://api.semanticscholar.org/CorpusID:
247222693
Liu Y, Peng X, Du T et al (2024) ERA-CoT: improving chain-of-
thought through entity relationship analysis. In: Ku LW, Martins
A, Srikumar V (eds) Proceedings of the 62nd Annual Meeting of
the Association for Computational Linguistics (Volume 1: Long
Papers). Association for Computational Linguistics, Bangkok,
Thailand, pp 8780–8794. https://doi.org/10.18653/v1/2024.acl-
long.476 https://aclanthology.org/2024.acl-long.476/
Liu P, Wang X, Xiang C, et al (2020) A survey of text data augmentation.
In: 2020 International Conference on Computer Communication
and Network Security (CCNS), IEEE, pp 191–195
Li G, Wang P, Ke W (2023a) Revisiting large language models as
zero-shot relation extractors. In: Bouamor H, Pino J, Bali K (eds)
Findings of the association for computational linguistics: EMNLP
2023. Association for Computational Linguistics, Singapore, pp
6877–6892. https://aclanthology.org/2023.ﬁndings-emnlp.459/
Li X, Yin F, Sun Z et al (2019) Entity-relation extraction as multi-turn
question answering. In: Korhonen A, Traum D, Màrquez L (eds)
Proceedings of the 57th annual meeting of the association for com-
putational linguistics. Association for Computational Linguistics,
Florence, Italy, pp 1340–1350. https://doi.org/10.18653/v1/P19-
1129 https://aclanthology.org/P19-1129/
Ma Y, Wang A, Okazaki N (2024) Building a japanese document-
level relation extraction dataset assisted by cross-lingual transfer.
arXiv:2404.16506
Mimno D, Wallach HM, Talley E et al (2011) Optimizing semantic
coherence in topic models. In: Proceedings of the conference on
empirical methods in natural language processing. Association for
Computational Linguistics, USA, EMNLP ’11, pp 262-272
Møller AG, Pera A, Dalsgaard J et al (2024) The parrot dilemma:
Human-labeled vs. LLM-augmented data in classiﬁcation tasks.
In: Graham Y, Purver M (eds) Proceedings of the 18th conference
of the european chapter of the association for computational lin-
guistics (Volume 2: Short Papers). Association for Computational
Linguistics, St. Julian’s, Malta, pp 179–192. https://aclanthology.
org/2024.eacl-short.17/
Mueller J, Thyagarajan A (2016) Siamese recurrent architectures for
learning sentence similarity. In: Proceedings of the AAAI confer-
ence on artiﬁcial intelligence
Ri R, Yamada I, Tsuruoka Y (2022) mLUKE: the power of entity
representations in multilingual pretrained language models. In:
Muresan S, Nakov P, Villavicencio A (eds) Proceedings of the 60th
annual meeting of the association for computational linguistics
(Volume 1: Long Papers). Association for Computational Linguis-
tics, Dublin, Ireland, pp 7316–7330. https://doi.org/10.18653/v1/
2022.acl-long.505 https://aclanthology.org/2022.acl-long.505/
Sahu SK, Christopoulou F, Miwa M, et al (2019) Inter-sentence rela-
tion extraction with document-level graph convolutional neural
network. In: Korhonen A, Traum D, Màrquez L (eds) Proceed-
ings of the 57th annual meeting of the association for compu-
tational linguistics. Association for Computational Linguistics,
Florence, Italy, pp 4309–4316,https://doi.org/10.18653/v1/P19-
1423 https://aclanthology.org/P19-1423/
Samuel V, Aynaou H, Chowdhury AG, et al (2023) Can llms augment
low-resource reading comprehension datasets? opportunities and
challenges. arXiv:2309.12426
Shang YM, Huang H, Mao X (2022) Onerel: joint entity and relation
extraction with one module in one step. In: Proceedings of the
AAAI conference on artiﬁcial intelligence, pp 11285–11293
Sun K, Zhang R, Mensah S et al (2021) Progressive multi-task learn-
ing with controlled information ﬂow for joint entity and relation
extraction. In: Proceedings of the AAAI conference on artiﬁcial
intelligence, pp 13851–13859
Sun Y, Zhu Z, Zuo Z et al (2024) Dsamr: dual-stream attention
multi-hop reasoning for knowledge-based visual question answer-
ing. Expert Syst Appl 245:12309. https://doi.org/10.1016/j.eswa.
2023.123092 https://www.sciencedirect.com/science/article/pii/
S0957417423035947
Takahashi R, Matsubara T, Uehara K (2019) Data augmentation using
random image cropping and patching for deep CNNs. IEEE Trans
Circ Syst Vid Technol 30(9):2917–2931
Tang X, Wang J, Su Q (2024) Small language model is a good guide
for large language model in chinese entity relation extraction.
arXiv:2402.14373
Tian X, Guo Y, Ge B et al (2024) Agent-da: enhancing low-resource
event extraction with collaborative multi-agent data augmentation.
Knowl-Based Syst 305:11262. https://doi.org/10.1016/j.knosys.
2024.112625 https://www.sciencedirect.com/science/article/pii/
S0950705124012590
Wan Z, Cheng F, Mao Z et al (2023) GPT-RE: in-context learning
for relation extraction using large language models. In: Bouamor
H, Pino J, Bali K (eds) Proceedings of the 2023 conference on
empirical methods in natural language processing. Association for
Computational Linguistics, Singapore, pp 3534–3547. https://doi.
org/10.18653/v1/2023.emnlp-main.214 https://aclanthology.org/
2023.emnlp-main.214/
Wang Y (2023) Research on cross-lingual word vector learning in mon-
golian and chinese based on bert. Ph.d. thesis, Inner Mongolia
Normal University. https://doi.org/10.27230/d.cnki.gnmsu.2022.
000773
123

--- Page 21 ---

Journal of King Saud University Computer and Information Sciences (2025) 37 :56
Page 21 of 22
56
Wang J, Chen N, Sun Q et al (2023a) Hugnlp: a uniﬁed and compre-
hensive library for natural language processing. In: Proceedings
of the 32nd ACM International Conference on Information and
Knowledge Management. Association for Computing Machinery,
New York, NY, USA, CIKM ’23, pp 5111-5116. https://doi.org/
10.1145/3583780.3614742
Wang L, Hu Y, He J et al (2025) T-sciq: teaching multimodal
chain-of-thought reasoning via large language model signals for
science question answering. In: Proceedings of the Thirty-Eighth
AAAI conference on artiﬁcial intelligence and thirty-sixth con-
ference on innovative applications of artiﬁcial intelligence and
fourteenth symposium on educational advances in artiﬁcial intelli-
gence. AAAI Press, AAAI’24/IAAI’24/EAAI’24. https://doi.org/
10.1609/aaai.v38i17.29884
Wang J, Sun Q, Li X et al (2024) Boosting language models reason-
ing with chain-of-knowledge prompting. In: Ku LW, Martins A,
Srikumar V (eds) Proceedings of the 62nd annual meeting of
the association for computational linguistics (Volume 1: Long
Papers). Association for Computational Linguistics, Bangkok,
Thailand, pp 4958–4981. https://doi.org/10.18653/v1/2024.acl-
long.271 https://aclanthology.org/2024.acl-long.271/
Wang L, Xu W, Lan Y et al (2023b) Plan-and-solve prompting:
improving zero-shot chain-of-thought reasoning by large lan-
guage models. In: Annual Meeting of the Association for Com-
putational Linguistics. https://api.semanticscholar.org/CorpusID:
258558102
Wang Y, Yu B, Zhang Y et al (2020) TPLinker: single-stage joint extrac-
tion of entities and relations through token pair linking. In: Scott
D, Bel N, Zong C (eds) Proceedings of the 28th international con-
ference on computational linguistics. International Committee on
Computational Linguistics, Barcelona, Spain (Online), pp 1572–
1582. https://doi.org/10.18653/v1/2020.coling-main.138 https://
aclanthology.org/2020.coling-main.138/
Wei X, Cui X, Cheng N et al (2023) Zero-shot information extraction
via chatting with chatgpt. arXiv:2302.10205
Wei Z, Su J, Wang Y, et al (2020) A novel cascade binary tagging frame-
workforrelationaltripleextraction.In:JurafskyD,ChaiJ,Schluter
N, et al (eds) Proceedings of the 58th annual meeting of the associa-
tion for computational linguistics. Association for Computational
Linguistics, Online, pp 1476–1488. https://doi.org/10.18653/v1/
2020.acl-main.136 https://aclanthology.org/2020.acl-main.136/
Wei J, Wang X, Schuurmans D et al (2024) Chain-of-thought prompting
elicits reasoning in large language models. In: Proceedings of the
36th international conference on neural information processing
systems. Curran Associates Inc., Red Hook, NY, USA, NIPS ’22
Wei J, Zou K (2019) EDA: Easy data augmentation techniques for
boosting performance on text classiﬁcation tasks. In: Inui K,
Jiang J, Ng V, et al (eds) Proceedings of the 2019 conference
on empirical methods in natural language processing and the
9th international joint conference on natural language processing
(EMNLP-IJCNLP). Association for Computational Linguistics,
Hong Kong, China, pp 6382–6388. https://doi.org/10.18653/v1/
D19-1670 https://aclanthology.org/D19-1670/
Xie Q, Dai Z, Hovy E et al (2020) Unsupervised data augmentation for
consistency training. Adv Neural Inf Process Syst 33:6256–6268
Xie S, Raghunathan A, Liang P et al (2022) An explanation of in-context
learning as implicit bayesian inference. In: International confer-
ence on learning representations. https://openreview.net/forum?
id=RdJVFCHjUMI
Xu X, Tao C, Shen T et al (2024) Re-reading improves reasoning in
large language models. In: Al-Onaizan Y, Bansal M, Chen YN
(eds) Proceedings of the 2024 conference on empirical methods
in natural language processing. Association for Computational
Linguistics, Miami, Florida, USA, pp 15549–15575. https://doi.
org/10.18653/v1/2024.emnlp-main.871 https://aclanthology.org/
2024.emnlp-main.871/
Xu B, Wang Q, Lyu Y, et al (2021) Entity structure within and through-
out: modeling mention dependencies for document-level relation
extraction. In: AAAI conference on artiﬁcial intelligence. https://
api.semanticscholar.org/CorpusID:231985811
Xu C, Xu Y, Wang S et al (2023) Small models are valuable plug-ins
for large language models. arXiv:2305.08848
YamadaI,RiR(2024)LEIA:facilitatingcross-lingualknowledgetrans-
fer in language models with entity-based data augmentation. In: Ku
LW, Martins A, Srikumar V (eds) Findings of the association for
computational linguistics: ACL 2024. Association for Computa-
tional Linguistics, Bangkok, Thailand, pp 7029–7039. https://doi.
org/10.18653/v1/2024.ﬁndings-acl.419 https://aclanthology.org/
2024.ﬁndings-acl.419/
Yang S, Xiao W, Zhang M et al (2022) Image data augmentation for
deep learning: A survey. arXiv:2204.08610
Yu B, Zhang Z, Shu X et al (2020) Joint extraction of entities and
relations based on a novel decomposition strategy. In: ECAI 2020.
IOS Press, pp 2282–2289
Zeng D, Liu K, Lai S et al (2014) Relation classiﬁcation via convolu-
tional deep neural network. In: Tsujii J, Hajic J (eds) Proceedings
of COLING 2014, the 25th international conference on computa-
tional linguistics: technical papers. Dublin City University and
Association for Computational Linguistics, Dublin, Ireland, pp
2335–2344. https://aclanthology.org/C14-1220/
Zhang S, Chen Z, Shen Y et al (2023b) Planning with large language
models for code generation. arXiv:2303.05510
Zhang K, Jimenez Gutierrez B, Su Y (2023a) Aligning instruc-
tion tasks unlocks large language models as zero-shot rela-
tion extractors. In: Rogers A, Boyd-Graber J, Okazaki N
(eds) Findings of the association for computational linguistics:
ACL 2023. Association for Computational Linguistics, Toronto,
Canada, pp 794–812. https://doi.org/10.18653/v1/2023.ﬁndings-
acl.50 https://aclanthology.org/2023.ﬁndings-acl.50/
Zhang Z, Zhang A, Li M et al (2022) Automatic chain of thought
prompting in large language models. arXiv:2210.03493
Zhang J, Zhao Y, Zhang S et al (2024) Enhancing cross-lingual emotion
detection with data augmentation and token-label mapping. In:
Proceedings of the 14th workshop on computational approaches
to subjectivity, sentiment, & social media analysis, pp 528–533
Zhang Y, Zhong V, Chen D et al (2017) Position-aware attention and
supervised data improve slot ﬁlling. In: Palmer M, Hwa R, Riedel
S (eds) Proceedings of the 2017 conference on empirical meth-
ods in natural language processing. Association for Computational
Linguistics, Copenhagen, Denmark, pp 35–45. https://doi.org/10.
18653/v1/D17-1004 https://aclanthology.org/D17-1004/
Zhao T, Yan Z, Cao Y et al (2021) Asking effective and diverse ques-
tions: a machine reading comprehension based framework for
joint entity-relation extraction. In: Proceedings of the twenty-ninth
international conference on international joint conferences on arti-
ﬁcial intelligence, pp 3948–3954
Zheng S, Wang F, Bao H et al (2017) Joint extraction of entities and
relations based on a novel tagging scheme. In: Barzilay R, Kan MY
(eds) Proceedings of the 55th annual meeting of the association for
computational linguistics (Volume 1: Long Papers). Association
for Computational Linguistics, Vancouver, Canada, pp 1227–
1236. https://doi.org/10.18653/v1/P17-1113 https://aclanthology.
org/P17-1113/
Publisher’s Note Springer Nature remains neutral with regard to juris-
dictional claims in published maps and institutional afﬁliations.
123

--- Page 22 ---

56
Page 22 of 22
Journal of King Saud University Computer and Information Sciences (2025) 37 :56
Authors and Aﬃliations
Yurong Wang1,2,3 · Min Lin1,4,6 · Qitu Hu1,2,3 · Longjie Bao5 · Shuangcheng Bai4 · Yanling Li4
B Min Lin
linmin@imnu.edu.cn
Yurong Wang
15049138357@163.com
Qitu Hu
huqitu@gmail.com
Longjie Bao
1016486749@qq.com
Shuangcheng Bai
bsc@onon.cn
Yanling Li
liyanling7871397@163.com
1
College of Mathematics Science, Inner Mongolia Normal
University, Hohhot 010022, Inner Mongolia, China
2
Center for Applied Mathematics Inner Mongolia, Zhao Wu
Da Road, 010022 Hohhot, Inner Mongolia, China
3
Key Laboratory of Inﬁnite-dimensional Hamiltonian System
and Its Algorithm Application, Ministry of Education, Zhao
Wu Da Road, 010022 Hohhot, Inner Mongolia, China
4
College of Computer Science and Technology, Inner
Mongolia Normal University, Hohhot 010022, Inner
Mongolia, China
5
International Mongolian Hospital of Inner Mongolia, Hohhot
010020, Inner Mongolia, China
6
Inner Mongolia Electronic Information Vocational Technical
College, Hohhot 010070, Inner Mongolia, China
123

```
