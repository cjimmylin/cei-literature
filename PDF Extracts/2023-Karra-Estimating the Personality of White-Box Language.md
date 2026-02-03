---
title: "Estimating the Personality of White-Box Language - PDF Extract"
source_pdf: "2023-Karra-Estimating the Personality of White-Box Language.pdf"
pages: 30
extracted_at: "2026-01-24T17:05:15.845889"
---

# PDF Extract: Estimating the Personality of White-Box Language

**Source PDF:** 2023-Karra-Estimating the Personality of White-Box Language.pdf
**Total Pages:** 30

---

## Content

```
--- Page 1 ---

Estimating the Personality of White-Box Language Models
Saketh Reddy Karraa, Son The Nguyena, Theja Tulabandhulaa
aUniversity of Illinois Chicago, Chicago, United States
Abstract
Technology for open-ended language generation, a key application of artiﬁcial in-
telligence, has advanced to a great extent in recent years. Large-scale language
models, which are trained on large corpora of text, are being used in a wide range
of applications everywhere, from virtual assistants to conversational bots. While
these language models output ﬂuent text, existing research shows that these mod-
els can and do capture human biases. Many of these biases, especially those that
could potentially cause harm, are being well-investigated.
On the other hand,
studies that infer and change human personality traits inherited by these models
have been scarce or non-existent. Our work seeks to address this gap by exploring
the personality traits of several large-scale language models designed for open-
ended text generation and the datasets used for training them. We build on the
popular Big Five factors and develop robust methods that quantify the personality
traits of these models and their underlying datasets. In particular, we trigger the
models with a questionnaire designed for personality assessment and subsequently
classify the text responses into quantiﬁable traits using a Zero-shot classiﬁer. Our
estimation scheme sheds light on an important anthropomorphic element found in
such AI models and can help stakeholders decide how they should be applied as
well as how society could perceive them. Additionally, we examined approaches
to alter these personalities, adding to our understanding of how AI models can be
adapted to speciﬁc contexts.
Keywords:
Language models, Personality, Zero-shot learning
1. Introduction
With advancements in methodologies and increasing availability of computa-
tional resources for training deep neural networks in recent years, Natural Lan-
guage Processing (NLP) research has seen substantial progress on a variety of tasks
Email addresses: skarra7@uic.edu (Saketh Reddy Karra), snguye65@uic.edu (Son The
Nguyen), theja@uic.edu (Theja Tulabandhula)
arXiv:2204.12000v2  [cs.CL]  10 May 2023

--- Page 2 ---

such as language modeling (Liu & Lapata, 2018), question answering (Soares &
Parreiras, 2020), and machine translation (Zong & Hong, 2018) to name a few.
In particular, Natural Language Generation (NLG) models that enable the gen-
eration of human-readable language have become the central building blocks of
modern artiﬁcial intelligence (AI) applications, such as virtual assistants, chat-
bots, automatic translators, and text summarizers (Bai et al., 2022).
Incorporating personality into AI applications has gained increasing attention
in recent years, as seen from their use in ﬁnance (Spencer et al., 2018) and e-
commerce sectors (Ahmad et al., 2020). Personality is a complex construct that
encompasses a range of behaviors, emotional states, and thought patterns arising
from biological and environmental factors. In the context of AI, personality traits
can be thought of as the manifestation of human-like characteristics in language
models, which are typically trained on human-generated text from the Internet.
Consequently, these models indirectly incorporate human tendencies and biases
reﬂected in the written text unless data pre-processing steps are taken. Recent
studies (Bordia & Bowman, 2019; Sheng et al., 2019) have investigated the in-
corporation of such biases into language models, highlighting the need for careful
consideration of personality traits in the development of AI systems. In this direc-
tion, Our paper is among the ﬁrst to validate and quantify the personality traits of
language models empirically. We explore ways to modify these traits to meet spe-
ciﬁc requirements, thereby enhancing the eﬀectiveness and ethical considerations
of AI applications in various contexts.
Identifying personality traits in language models can have signiﬁcant implica-
tions for their design, implementation, and deployment. In terms of user expe-
rience, understanding the personality of a language model can lead to creating
more engaging and empathetic models, which can better interact with users and
improve user satisfaction, ultimately increasing user adoption of AI-based applica-
tions. Moreover, by identifying personality traits, researchers can uncover underly-
ing biases in language models, leading to bias reduction and improving the fairness
and accuracy of AI systems. Additionally, identifying personality traits can help
identify the most appropriate use cases for speciﬁc language models. For example,
a language model with a friendly personality may be better suited for customer
service applications. In contrast, a more formal personality may be more appropri-
ate for professional training applications. These potential implications highlight
the importance of considering the personality traits of language models in their
development and deployment. Moreover, we can aim to design learning systems
that enable language models to alter their personality traits over time in response
to changing environmental factors. This would result in dynamic AI systems that
are responsive and more engaging to users over a long time frame. Extending this
research could lead to further improvements in the development of chatbots, vir-
2

--- Page 3 ---

tual assistants, and other AI systems, enabling them to provide a more human-like
experience to users.
Our research focuses on quantifying the personality traits of white-box lan-
guage models and exploring how to change them. Investigating the personality
traits of language models is a challenging task, as the models’ outputs are stochas-
tic and require a suitable auxiliary veriﬁcation model to elicit traits from the text
responses (for example, manual human veriﬁcation may not be feasible). For mod-
ifying personalities, one direct approach is to train or ﬁne-tune language models
on personality-annotated text data, taking inspiration from human psychological
research. We show that this too is challenging, especially if we are interested in
achieving precise control over personality changes. In this paper, we aim to address
these challenges and investigate the personality traits of popular language models
in open-ended text generation, along with the datasets used to train them. Our key
hypothesis is that language models generate text responses reﬂecting the personal-
ity traits of the datasets on which they were trained when prompted. To quantify
their personalities, we process the datasets as well as the text responses generated
by the language models using state-of-the-art auxiliary prediction models. How-
ever, when it comes to altering the persona of language models, we limit ourselves
to evaluating white-box language models that allow users to access and modify
parameters, unlike black-box models like ChatGPT (Ray, 2023). Additionally, we
focus our attention solely on foundation models and do not consider instruction-
tuned models. Unlike foundation models, instruction-tuned models use supervised
instruction ﬁne-tuning to understand the tasks and do not require prompt engi-
neering. Furthermore, evaluating the intrinsic personalities of instruction-tuned
models can be challenging since they can be trained to embody any desired per-
sonality in their responses successfully.
To the best of our knowledge, we are one of the ﬁrst to explore personality traits
of large language models in general, complementing the literature that studies
biases. To recap, the primary contributions of this work are:
• We explore the ﬁve-factor method (Digman, 1990), a widely used personality
assessment questionnaire, to quantify the personality traits of datasets and
language models.
• We propose a novel estimation scheme for evaluating the personality traits
of both the datasets and the language models, using Zero-shot learning
(ZSL) (Yin et al., 2019). Our approach involves triggering language models
with the Big Five questionnaire and subsequently classifying the resulting
text responses into quantiﬁable personality traits.
• Finally, we discuss approaches to alter the personalities of these models by
ﬁnetuning as well as by using a pretrained auxiliary personality classiﬁcation
3

--- Page 4 ---

model.
• We perform extensive experiments on multiple white-box language models
and their underlying training corpora, explicitly contrasting how the person-
ality proﬁles diﬀer between the two. The results validate the eﬀectiveness
of our proposed methodology and give insights into what factors lead to
diﬀerences between models and data, as well as across models.
The rest of the paper is structured as follows. In Section 2, we discuss closely
related work. In Section 3, we introduce the Big Five factors, the Zero-shot clas-
siﬁer, and the pretrained language models. In Section 4, we propose the methods
to evaluate the personality traits of datasets and language models, followed by
a discussion on approaches to alter these traits.
In Section 5, we discuss the
experimental setup and extensively document the traits of datasets and the cor-
responding language models. In addition, we also provide preliminary results for
altering these personalities. We conclude with some comments on future work in
Section 6.
2. Related Work
Our work builds on the following streams of research: (a) measurement of
human personality traits, (b) design of personality detection methodologies, and
(c) studies on societal biases in open-ended text generation. We brieﬂy discuss
some of the works below.
2.1. Personality Measures
Researchers have used various schemes for human personality modeling such
as 16PF (Schuerger, 2000), EPQ-R (Miles & Hempel, 2004), Myers–Briggs Type
Indicator (MBTI) (Miles & Hempel, 2004), and the three trait personality mod-
els/PEN (Eysenck, 2012) among others. For instance, MBTI is a widely adopted
personality measure that is sometimes used to screen job candidates. It relies on
the theory that random variation in human behavior is quite orderly and consis-
tent due to certain basic diﬀerences in the way people prefer to use perception
and judgment. The MBTI personality measure categorizes people into two cat-
egories in each of the four dimensions: introversion versus extroversion; sensing
versus intuiting; thinking versus feeling; and judging versus perceiving. Another
popular measure used in the literature on automated personality detection is the
Big Five factors measure (Digman, 1990), which deﬁnes and quantiﬁes the follow-
ing attributes: Extraversion, Neuroticism, Agreeableness, Conscientiousness, and
Openness. In this work, we adapt and estimate the Big Five factors of white-
box language models and their underlying datasets using a novel methodology
described in Section 4.
4

--- Page 5 ---

2.2. Methods for Automatic Personality Detection
Automatic detection of personality traits from text produced by humans, in-
stead of them explicitly answering a questionnaire or undergoing a test, has been
explored in the literature. Pennebaker & King (1999) compiled a dataset of anony-
mous essays tagged with the authors’ personalities based on the Big Five factors
and used the so-called Linguistic Inquiry and Word Count (LIWC) features to
determine the correlation between essays and personality. Liu et al. (2016) used
deep learning-based models in combination with the atomic features of text, i.e.,
the characters, to predict personality traits of individuals using hierarchical and
vectorized word/sentence representations. Akrami et al. (2019) developed a model
that can extract Big Five factors from text using machine learning techniques like
support vector regression. Jeremy et al. (2019) performed experiments to auto-
matically predict a user’s personality based on Big Five factors on Twitter. Mehta
et al. (2020) provides an overview of state-of-the-art machine learning models for
automatic personality detection with a speciﬁc focus on multi-modal approaches.
Recently Derekmracek (2020) used Zero-shot learning (ZSL) to classify text re-
sponses from a self-report questionnaire in terms of the Big Five factors. Through
their experiments, the authors showed that a strong positive relationship (e.g.,
correlation) exists between the ZSL scores and the scores on the self-report ques-
tionnaire for each speciﬁc trait. While the approaches discussed earlier have shown
promising results in prediction tasks, they often rely on large amounts of data for
eﬀective performance.
To address this challenge, we quantify the traits of our
models by using the ZSL framework (see Section 4). Our novel approach explores
all the possible scenarios for deﬁning the personality trait labels and thus robustly
adapts the ZSL framework to language models.
2.3. Study of Biases in Language Modeling
Recent works have explored multiple societal biases that are learned by lan-
guage models, which may sometimes be at odds with the prevailing societal val-
ues. Bolukbasi et al. (2016) demonstrated quantitatively that word embeddings
contain biases in their geometry that reﬂect gender stereotypes present in the
broader society. Sheng et al. (2019) performed an experiment analyzing diﬀerent
textual contexts where biases can occur for diﬀerent demographics in text samples
generated using the state-of-the-art language models.
Bordia & Bowman (2019)
evaluated the magnitude of gender bias in word-level language models that are
trained on WikiText-2 and CNN/Daily Mail datasets. Nadeem et al. (2020) eval-
uated popular models such as BERT (Devlin et al., 2018), GPT-2 (Radford et al.,
2019) and XLNet (Yang et al., 2019) using StereoSet dataset and show that these
models exhibit strong stereotypical biases in the following four domains: gender,
profession, race, and religion. We note that our work is complementary to all
5

--- Page 6 ---

these studies in the following sense. While we aim to understand human tenden-
cies captured by language models similar to these prior studies, our narrow but
well-deﬁned focus on characterizing the learned personality traits and potentially
altering them is a diﬀerentiating factor, as well as a ﬁrst of its kind.
3. Preliminaries
In this section, we discuss the Big Five factors and introduce our hypothesis
for quantifying these traits in language models and their corresponding training
datasets. We also describe the Zero-shot classiﬁer (ZSC) and provide details about
the various language models we have analyzed in our study.
3.1. Big Five factors
Our study quantiﬁes personality traits using the Big Five factors, also known
as the ﬁve-factor model.
Under this model, personality can be reduced to the
following ﬁve core factors:
• Extraversion: sociable and energetic versus reserved and solitary.
• Neuroticism: sensitive and nervous versus secure and conﬁdent.
• Agreeableness: trustworthy, straightforward, generous, and modest versus
unreliable, complicated, meager, and boastful.
• Conscientiousness: eﬃcient and organized versus sloppy and careless.
• Openness: inventive and curious versus dogmatic and cautious.
The neuroticism factor has a negative connotation in contrast to the other four
factors. Therefore, we estimate Emotional Stability instead to be consistent with
other factors in the rest of the paper.
The questionnaire itself is a list of ﬁfty statements, each referring to diﬀer-
ent characteristics of an individual. Accordingly, each statement is designed to
elicit a speciﬁc Big Five factor behavior. In general, individuals respond to ev-
ery statement in the questionnaire by opting for one of the following choices: (a)
very inaccurate, (b) moderately inaccurate, (c) neither inaccurate nor accurate,
(d) moderately accurate, and (e) very accurate. The response to every statement
is scored against a predetermined Big Five factor on a scale of 1 to 5 as shown
in Table 1. There are ten statements evaluated for the extraversion factor, ten
questions for agreeableness, and so forth. Finally, the aggregated scores against
each of the Big Five factors are averaged to obtain the quantiﬁable trait scores.
6

--- Page 7 ---

Response
Score
Very Inaccurate
1
Moderately Inaccurate
2
Neither Inaccurate nor Accurate
3
Moderately Accurate
4
Very Accurate
5
Table 1: Scoring scheme to determine the traits based on text output.
3.2. Our Hypothesis for Personality Estimation
Assessing these personality traits for humans typically involves using two types
of data sources:
self-reports and peer reports (e.g., friends, colleagues, etc.).
Among the two, the more popular approach is via self-reports, in which people
describe how they see themselves while responding to a personality assessment
questionnaire. For example, a participant is expected to respond to statements
such as “I am someone who is outgoing and sociable” on a Likert-type scale (e.g.,
from 1 = strongly disagree to 5 = strongly agree). Self-reports capture people’s
explicit self-concepts about their personality traits, which are parts of their iden-
tities. On the other hand, peer reports help us understand how others perceive
an individual. Unlike self-reports, peer reports focus on the personality traits at-
tributed to an individual based on their interactions with others. To obtain peer
reports, peers complete a similar personality assessment questionnaire about the
individual, which then determines the perceived personality of that individual.
Our approach to measuring personality traits in language models will build on
the human self-reporting approach, avoiding the design choices needed to qualify
suitable peers. Our key hypothesis is that when prompted, language models gener-
ate text responses that reﬂect the personality traits of the datasets they were trained
on. Assuming that this hypothesis is true, we process the text responses gener-
ated by language models using auxiliary prediction models (which can be quite
sophisticated themselves) to quantify their personalities.
3.3. Zero-shot Classiﬁer
To the best of our knowledge, there is currently a dearth of textual datasets with
personality-annotated data. Moreover, traditional machine learning approaches
require vast amounts of data to achieve acceptable performance on prediction
tasks. However, recent studies have shown promise in addressing the issue. For
instance, the entailment-based ZSC method proposed by (Yin et al., 2019) has
demonstrated success in classifying tasks across multiple domains with satisfactory
performance without requiring prior training data (Ma et al., 2021). Therefore, we
consider ZSC as our method for classifying personality traits. ZSC employs a pre-
trained Natural Language Inference (NLI) model that utilizes both a premise and a
hypothesis input. The model predicts whether the hypothesis is true (entailment),
false (contradiction), or undetermined (neutral) with respect to the given premise.
7

--- Page 8 ---

ZSC uses the input text as the premise and generates a hypothesis for each
potential label. The accuracy of each label is subsequently evaluated by determin-
ing if the NLI model predicts whether the premise ”entails” the hypothesis. For
example, let’s consider the task of estimating the openness trait of a user based
on their social media posts. We set the content of each post as the premise and
construct a hypothesis for the openness trait as: ”This post reﬂects a high level
of openness.” We subsequently use the ZSC to evaluate the entailment and con-
tradiction probabilities between the premise and the hypothesis. The resulting
probabilities are then aggregated to obtain the likelihood of the user exhibiting
high or low levels of the openness trait.
3.4. Language Models in Open Ended Text Generation
We study multiple pretrained language models that diﬀer in their training
strategies and corpora. These models rely on the concept of auto-regressive lan-
guage generation, which assumes that the probability distribution of a word se-
quence can be decomposed into the product of conditional next-word distributions.
At the core of all these language models are neural network models known as
Transformers (Vaswani et al., 2017). Unlike traditional recurrent neural networks
(RNNs), transformer architecture is based on a self-attention mechanism that al-
lows the models to selectively focus on diﬀerent parts of the input sequence while
processing it. This framework is particularly beneﬁcial for language understanding
and text-generation tasks. Below, we brieﬂy discuss the language models studied
in the paper.
GPT-2 (Radford et al., 2019) is a transformer-based language model that is trained
with a causal language modeling objective: predicting the next word given a se-
quence of previous words. GPT-2 was pretrained on the WebText dataset that
was collected by scraping and ﬁltering web pages from sources such as Reddit (a
popular social networking website).
GPT-3 (Brown et al., 2020) is the 3rd version release and is an upgraded ver-
sion of GPT-2. It also uses a Transformer framework and Attention architecture
similar to GPT-2. It is trained with 175 billion parameters, which is over 10x the
size of its predecessor, GPT-2. With its superior performance, it can generate text
that human evaluators typically have a higher diﬃculty distinguishing from those
written by humans. It was pretrained on an open-source dataset called Common
Crawl (Wenzek et al., 2019) and other text corpora from sources such as Wikipedia
(a popular online encyclopedia).
GPT-3.5-Turbo (Ye et al., 2023) is a ﬁnetuned version of its predecessor, GPT-3.
In addition to the datasets used in the training of GPT-3, developers leveraged
8

--- Page 9 ---

human feedback to improve the language model’s performance through a novel op-
timization framework known as reinforcement learning via human feedback. This
unique approach to model training enables GPT-3.5-Turbo to provide more accu-
rate and policy-optimized responses, making it a highly robust language model.
LLaMA (Language Model for Multi-task Architectures)
(Touvron et al., 2023)
is a state-of-the-art collection of language models, with parameters ranging from
7B to 65B that are competitive with the best existing language models. These
models are built by making modiﬁcations to transformer architecture proposed
by Vaswani et al. (2017) and trained using large amounts of textual data from
various sources, including English CommonCrawl (67%), C4 (15%) (Raﬀel et al.,
2020), Github (4.5%) (Hoﬀa, 2016), Gutenberg and Books3 (4.5%) (Gao et al.,
2020), ArXiv (2.5%) (Lewkowycz et al., 2022), and Stack Exchange (2%) (Stack-
Exchange, 2017).
TransformerXL (Dai et al., 2019) is a state-of-the-art language model developed
by researchers at Carnegie Mellon University and Google AI Language. Its ar-
chitecture is designed using new recurrence mechanisms and positional encoding
schemes to overcome some of the limitations of the original Transformer archi-
tecture, such as the ﬁxed-length context window and the diﬃculty in handling
long-term dependencies. It was pretrained on the WikiText language modeling
dataset, which was extracted from the set of veriﬁed good and featured articles on
Wikipedia.
XLNet (Yang et al., 2019) is an extension of the TransformerXL model.
The
model learns bidirectional contexts by maximizing the expected likelihood over
all permutations of the input sequence rather than just the preceding context.
The auto-regressive objective provides a natural way to use the product rule for
factorizing the joint probability of the predicted tokens, eliminating a speciﬁc in-
dependence assumption that was made in BERT (Devlin et al., 2018). This model
was trained on BooksCorpus (Zhu et al., 2015) and English Wikipedia datasets
in a self-supervised fashion.
4. Methods for Estimating and Altering Personalities
In this section, we explore various approaches for evaluating the personality
traits of datasets. Building on this, we design a robust novel approach to evaluate
the traits of language models. Finally, we also present a few methods to alter the
personality traits of language models.
9

--- Page 10 ---

Labels
1
[agreeableness, antoganism]
2
[conscientiousness, disinhibition]
3
[extraversion, introversion]
4
[emotional stability, neuroticism]
5
[openness, closeness]
Table 2: Labels for creating the input hypotheses for ZSC in Approaches 2 and 3.
4.1. Evaluating Personalities of Datasets
Extracting quantiﬁable personality traits from datasets requires deﬁning suit-
able labels for ZSC, followed by a scoring scheme based on the ZSC outputs. As
discussed earlier in Section 3, ZSC takes a premise and a hypothesis as input and
predicts whether the hypothesis is true (entailment), false (contradiction), or un-
determined (neutral) given the premise. So the ﬁrst step in using ZSC is to cast
personality estimation as an entailment problem by converting the desired trait la-
bels into hypotheses. In this work, we use the following hypothesis template while
evaluating the ZSC: This response is characterized by {label}. Here the placeholder
{label} is replaced by trait-speciﬁc keywords as shown in Table 2.
We investigate diﬀerent approaches to ﬁnalize our model setup and extract
personality trait scores in terms of the Big Five factors.
Approach 1. The premise and the hypothesis can either be positively related or
negatively related in this approach. Accordingly, we set up a single ZSC to quantify
the ﬁve personality traits independently using ﬁve labels: agreeableness, openness,
extraversion, conscientiousness, and emotional stability. These labels will be used
to generate hypotheses sequentially, and each will be passed as an input to the
ZSC. We transform the resulting output probabilities (the entailment scores of the
NLI model after normalization with contradiction scores) obtained for each label
using one-dimensional linear interpolations to Big Five factor scores (ranging from
1 to 5).
Approach 2. The premise and the hypothesis can either be positively related or
unrelated under this approach. Under this assumption, we measure the personality
scores using labels for the two extreme ends of each trait independently using ﬁve
diﬀerent ZSCs. Then, the output probabilities for both extremes are transformed
via a softmax function to obtain the ﬁnal scores for each Big Five factor. The
labels for the extreme ends of each trait are provided in Table 2.
Approach 3. In this approach, we consider all three scenarios, i.e., the premise and
hypothesis can either be positively related, negatively related, or unrelated. Under
assumptions made in the previous two approaches, measuring the ﬁve personality
traits independently using ZSC might lead to incorrect results. The reason for this
10

--- Page 11 ---

is that ZSC could classify a non-synonymic or antithetical hypothesis with low
probability for a given premise.
Therefore, one cannot guarantee if the lower
score for a particular label is due to negative relation or no relation between
the hypothesis and premise. Hence in this third approach, we set up a ZSC for
each trait and measure the entailment for the two extreme ends in a dependent
manner. Under the hood, the ZSC will calculate a single probability score using
the underlying NLI’s entailment scores of the two extreme ends of a trait. We then
again match the probabilities to the big-5 scores. We use the same labels for the
extreme ends of each trait as discussed in Approach 2.
A Comparison Between the Three ZSC-based Approaches. Our ﬁrst approach works
well whenever the hypothesis and premise entail or contradict each other. How-
ever, when the ZSC is prompted with unrelated premises and hypotheses, output
label probabilities can be low, which leads to inaccurate measurements of person-
ality traits. The second approach also has limitations. The ZSC uses the NLI
model’s entailment and contradiction scores behind the screens to calculate the
probability of the output label. We cannot conclude that a low score implies that
the hypothesis and the premise are neutral to each other, since the ZSC does not
use the neutral score of the underlying NLI model. Our third approach overcomes
these pitfalls of the ﬁrst two approaches and is expected to provide a more precise
assessment of the personality traits of datasets.
4.2. Evaluating Personalities of Language Models
We adopt the assessment questionnaire for Big Five factors discussed in Sec-
tion 3.1 as follows. Firstly, acquiring the responses in the multi-choice question-
answer format is not directly feasible in open-ended text generation since the
language model output is a sequence of words.
Thus, we start by setting the
statements from the questionnaire as prompts to the language model and generate
text responses as shown in Figure 1. To account for the stochastic nature of the
responses, we trigger the language model N ∈Z+ times using the same prompt
to observe N diﬀerent text completions for every statement in the questionnaire.
Moreover, we prompt the language models with each statement independently.
This is to ensure that the order in which statements are fed as input to the model
does not aﬀect the personality assessment.
Each of the generated text responses is passed independently as an input
premise to the ZSC setup as discussed in Approach 3. The resulting outputs are
the independent probabilities for the responses to be characterized according to
the ﬁve factors. We obtain N such probabilities for each input prompt. We then
use a one-dimensional linear interpolation to match the probabilities to scores
ranging from 1 to 5. Finally, we compute the score distribution and summary
11

--- Page 12 ---

Figure 1:
Framework for evaluating the personality of training datasets and language
models.
statistics (such as the median) of the scores for all the statements to represent the
personality of the concerned language model.
4.3. Modifying Personalities of Language Models
Pretrained language models possess varied personality traits due to their train-
ing on diverse datasets and due to diﬀerences in their model deﬁnitions and train-
ing approaches. We propose the following two model-agnostic methods aimed at
altering the personality traits of language models.
Method 1:. Modifying the personalities of the language models in a desired fash-
ion can be viewed as updating the model’s parameters such that it generates
modiﬁed text responses that are closer to the desired personality traits. One way
to partially achieve this is by ﬁnetuning the language models using suitably cho-
sen personality-annotated text data. Although straightforward ﬁnetuning is an
open-ended approach without allowing for precise control on achieving reference
personality proﬁles, it allows the language model to partially adapt to the new data
corpus in a straightforward manner and change the traits of the generated text
without expending much computational overhead. Accordingly, when we trigger
the ﬁnetuned language model with a prompt from our questionnaire, we expect
that the generated response reﬂects the altered personality. In contrast, a precise
control would need a new objective as well as a personality classiﬁer in the loop,
increasing the complexity of the process.
For ﬁnetuning, we leverage a (relatively smaller) personality-annotated text
dataset made available as part of a machine learning competition (SIOP, 2019).
12

--- Page 13 ---

The dataset includes text responses to open-ended situational judgment items
(SJIs) designed to elicit trait-relevant behaviors and aggregates trait scores based
on the Big Five factors.
To modify the personality of a language model with
respect to a speciﬁc trait, we train the model on the ﬁltered textual responses cor-
responding to that factor. Note that under this approach, precise control towards
changing the personality traits to a speciﬁc desired set of values while maintaining
language generation quality is generally non-trivial.
Figure 2: Altering traits of language model using Method 1.
Figure 3: Altering traits of language model using Method 2.
Method 2:. In this closely related approach to the above, we start by ﬁnetuning
a pre-trained model on personality annotated text data but focus on a speciﬁc
auxiliary classiﬁcation task instead of the original text generation objective. In
particular, using the text annotated with a speciﬁc Big Five factor, we ﬁnetune
the model on a binary classiﬁcation task with opposite ends of a speciﬁc Big Five
factor as target labels. Once we ﬁnetune the model via the auxiliary task, we use
these updated model weights for text generation. Irrespective of the approach,
we can evaluate the resultant model using the assessment process discussed in
Section 4.2 and observe the altered traits.
5. Experiments
In this section, we present the experimental setup and the results obtained from
evaluating the personality traits of the language models and the corresponding
datasets they were trained on.
In particular, we compare the personalities of
language models and their underlying datasets to identify potential disparities.
Finally, we report on the eﬀectiveness of our approaches in altering the personality
traits of language models.
13

--- Page 14 ---

5.1. Traits of Datasets
Setup. We explore the personality traits of the following datasets used in train-
ing language models, namely: BookCorpus, English Wikipedia, WebText
Test Set and Wikitext103.
• BookCorpus (Zhu et al., 2015) is a large collection of free novel books
written by unpublished authors, and contains 11, 038 books of 16 diﬀerent
sub-genres and is used to train XLNet.
• English Wikipedia contains cleaned articles that are built from Wikipedia
content and used to train XLNet and GPT-3. However, the exact versions
of the dataset used to develop those models are publicly undisclosed. We
obtained a version of this data that was available on May 1st, 2020.
• WebText Test Set (Gokaslan & Cohen, 2019) is provided by the ﬁrm
OpenAI. The training dataset was used to train GPT-2 and has not been
publicly released. Hence, we use the test set for our experiments.
• Wikitext103 (Merity et al., 2016) contains more than 100 million word
tokens retrieved from the arrangement of (veriﬁed) good and featured articles
on Wikipedia and is used to train TransformerXL.
Evaluating all of the datasets discussed above to infer personality traits re-
quires extensive computational resources due to their large size. To overcome this
challenge, we limit ourselves to analyzing sub-samples of the datasets, as speciﬁed
in Table 3. These sub-sampled datasets can be evaluated at diﬀerent levels of gran-
ularity, from sentence level and paragraph level to document level. Our analysis
has revealed that when a document containing many paragraphs and sentences is
passed as a standalone input, the ZSC that estimates personality traits doesn’t
perform well, predicting a score close to 3 (which is neutral) for most samples.
This is because such paragraphs and sentences may exhibit multiple conﬂicting
traits or have multiple trait-less sentences (e.g., facts). To address this issue, we
preprocess the data so that all samples are at the sentence or small paragraph level
before evaluation. Once preprocessed, each sentence is passed as an input to ZSC
using Approach 3 as explained in Section 2. Finally, we aggregate the resulting
personality scores for each trait to obtain the personality trait distributions.
Results. Figure 4 presents the estimated distributions of personality traits across
the datasets referenced earlier. Overall, we observe trait distributions are positively
skewed, as reﬂected by scores greater than the neutral 3.0. Additionally, to aid
the comparison of these distributions, we report the median scores in the adjoining
box plots, in which the length of the boxes represent the variance of the traits.
14

--- Page 15 ---

Dataset
Size
Percent uses for
inference
Models
Bookcorpus
5.75 GB
10%
XLNet
English Wikipedia
34.88 GB
2%
GPT-3, XLNet
Webtext Test Set
1.28 GB
20%
GPT-2
Wikitext103
0.70 GB
100%
Transformer-XL
Table 3: Summary statistics of the datasets.
(a) BookCorpus
(b) English Wikipedia
(c) Webtext Test Set
(d)Wikitext103
Figure 4: Personality trait distributions of datasets.
15

--- Page 16 ---

We make a few key observations next.
In the BookCorpus dataset, Ex-
traversion and Agreeableness are the most prominent traits, followed by Openness,
Emotional Stability, and Conscientiousness. Further, Agreeableness scores have the
highest variance, followed by Openness. For the English Wikipedia dataset, the
most prominent trait is Agreeableness, followed by Extraversion, Emotional Stabil-
ity, Openness, and Conscientiousness. This dataset has smaller spreads compared
to others.
In the WebText Test Set dataset, Agreeableness and Extraver-
sion are again the prominent traits, followed by Emotional Stability, Openness,
and Conscientiousness.
The spreads of the distributions of Agreeableness and
Openness are wider than the other traits in this dataset.
Extraversion is the
most prominent trait in the Wikitext103 dataset, while Conscientiousness is
the least prominent. Agreeableness scores have the widest spread in this dataset,
followed by openness. The personality traits exhibited by the datasets discussed
above align with the expected characteristics from their content. For instance,
the Wikitext103 dataset contains a wealth of factual information, resulting in
predominantly neutral personality traits. By contrast, the skewed distribution of
traits observed in the BookCorpus dataset reﬂects its inclusion of diverse text
genres, such as ﬁction, non-ﬁction, and academic material. The trait proﬁles could
have been acquired through alternative techniques; however, we employ ZSCs to
maintain consistency with the estimation method used for the models.
5.2. Traits of Models
Setup. To quantify the personality traits of language models, we trigger them us-
ing the Big Five questionnaire 30 times. This is done to account for the stochastic
nature of the responses and to obtain a reliable and consistent estimate of per-
sonality traits. The generated text responses are then classiﬁed using the ZSC
framework discussed in Approach 3.
We have used the publicly available OpenAI programmatic API To evaluate
the performance of GPT-3 and GPT-3.5-Turbo. Among the LLaMA models, we
evaluated its publicly available 4bit-7b quantized version. All three models dis-
cussed above operate as black box models due to their undisclosed architecture.
Consequently, our evaluation focuses solely on comparing their personality traits
without the ability to modify them. We utilized the text generation pipeline from
Hugging Face’s transformer package (Wolf et al., 2019) to evaluate these white-
box language models, namely GPT-2, TransformerXL, and XLNet.
To ensure
the consistency of our experiments, we employed a standardized set of hyper-
parameters for text generation for evaluating each of the language models, i.e.,
we chose maxseqlength (maximum length of output sequence) as 256, temperature
(randomness parameter) as 1, and a top-p (smallest possible set of words whose
cumulative probability exceeds the probability p) as 1.
16

--- Page 17 ---

Prompt
Generated Response
I don’t talk a lot.
I’m more of an introvert so I’m less than happy to take time to talk.
I prefer to be able to take control over how I work and make sure I be able to talk a lot.
I’m relaxed most of the time.
In all my experiences, I did not notice a single problem about myself or others I dealt with,
because I was focused on my personal well-being and that was all . . .
I feel comfortable around people.
I get a lot done and it’s nice working out or just enjoying myself and being around people.
A lot of that comes with me . . .
I am full of ideas.
I am also a very creative person, so it is important to me to develop my own ideas.
I have a lot of inspiration and a lot of love for the world.
Table 4: Examples of (uncorrected) text responses generated using GPT-2.
Results. Table 4 shows a few examples of input prompts and the respective text
responses generated using GPT-2. Due to the auto-regressive nature of the text
generation process, we observe that the GPT-2 model generates contextually co-
herent text based on the input prompts.
We observe noticeable variations in trait distributions of text generated using
diﬀerent language models, as illustrated in Figures 5 and 6. These variations are
also evident from the median scores of personality traits, as shown in Table 5.
Based on these scores, we can make a few key observations. Firstly, the Agree-
ableness scores are higher for GPT-3.5-Turbo, suggesting that the generated text
for this language model reﬂects a more generous and empathetic personality. Sec-
ondly, the LLaMA model scores higher in Conscientiousness. On the other hand,
GPT-3.5-Turbo has a higher median Extraversion score, implying that the gener-
ated responses emulate extroverted rather than introverted personalities. Finally,
the LLaMA model scores the highest in Emotional Stability, reﬂecting a more
emotionally stable personality than the other language models under considera-
tion. All the language models have their unique set of inherent personality traits,
which can be leveraged in downstream applications based on speciﬁc use cases.
For instance, the LLaMA model, with its high emotional stability median score, is
suitable for designing a chatbot in a mental health care setting, facilitating more
empathetic conversations with users. Overall, Our work’s signiﬁcant contribution
is the principled approach to extracting and utilizing these personality traits to
enhance the eﬀectiveness of language models in practical applications.
Trait
GPT2
GPT3
GPT-3.5-Turbo
LLaMA
Transformer-XL
XLNet
Agreeableness
3.41 (0.73)
4.19 (1.14)
4.41 (0.93)
3.82 (0.85)
3.86 (0.66)
3.64 (0.87)
Conscientiousness
3.18 (0.39)
3.66 (0.77)
3.94 (0.69)
4.01 (0.90)
3.96 (0.78)
3.73 (0.64)
Extraversion
3.07 (0.60)
3.94 (1.10)
4.06 (1.24)
3.85 (0.94)
3.43 (0.69)
3.63 (0.91)
Emotional Stability
3.15 (0.46)
2.79 (1.11)
3.79 (0.73)
3.76 (0.82)
3.36 (0.74)
3.01 (0.70)
Openness
2.97 (0.47)
3.78 (1.06)
3.78 (0.79)
3.62 (1.00)
4.02 (0.83)
3.55 (0.71)
Table 5: Personality scores (along with their uncertainties) of Language Models.
17

--- Page 18 ---

(a) GPT-2
(b) GPT-3
(c) GPT-3.5-Turbo
(d) TransformerXL
(e) XLNet
(f) LLaMA
Figure 5: Personality trait distributions of language models.
(a) Agreeableness
(b) Conscientiousness
(c) Extraversion
(d) Emotional Stability
(e) Openness
Figure 6: Comparison of personality trait distributions across language models.
18

--- Page 19 ---

Trait
Wasserstein distance
Mode 2 vs Mode 1
Wasserstein distance
Mode 3 vs Mode 1
Agreeableness
0.248
0.248
Conscientiousness
0.563
0.361
Extraversion
0.489
0.425
Emotional Stability
0.559
0.249
Openness
0.591
0.610
Table 6: Comparing traits distributions across modes using Wasserstein distances ∈[0, 1] for
GPT-2.
Sensitivity of the estimated personality distributions to estimation parameters:
As discussed earlier, the datasets used for training these language models are
composed of text at diﬀerent levels of granularity. Similarly, the text responses
generated using these models can be multiple sentences long. This variation in text
length can aﬀect the personality trait distributions that we observe. To assess the
sensitivity of estimation to this, we generate personality trait scores using diﬀerent
output modes, as explained below.
• Mode 1: Trait score of the entire generated response.
• Mode 2: Trait score of the ﬁrst sentence in the generated response.
• Mode 3: Median of the trait scores of all sentences present in the generated
response.
Figure 7 shows the trait distributions for some of the language models obtained
using the modes listed above.
The distributions remain the same for GPT-3,
XLNet, and TransformerXL. This is due to the fact that the responses generated
using these models were single sentences. However, the trait distributions vary
for GPT-2 across diﬀerent modes of evaluation, implying that the structure of
the output inﬂuences the personality score estimation. This observation can be
made quantitative using Wasserstein distances (between trait distributions across
models) and is provided in Table 6. From the table, we observe that Agreeableness
varies the least, i.e., is least sensitive to how much of the response is used to assess
the trait. And while there is a lot of change across all these traits, Openness varies
the most.
5.3. Traits of Datasets vs Models
To validate our hypothesis of whether the language models inherit personality
traits of datasets used for their training, we compare the trait distributions of
the language models and their underlying corpora. Speciﬁcally, we evaluate the
traits of WebText Test dataset and text responses generated using GPT-2.
Our ﬁndings, as shown in Figure 8, indicate that the trait distributions of the
WebText Test dataset and randomly generated text using GPT-2, without
19

--- Page 20 ---

(a) GPT-2 (Mode 1)
(b) GPT-2 (Mode 2)
(c) GPT-2 (Mode 3)
(d) GPT-3 (Mode 1)
(e) GPT-3 (Mode 2)
(f) GPT-3 (Mode 3)
(g) TransformerXL (Mode 1)
(h) TransformerXL (Mode 2)
(i) TransformerXL (Mode 3)
(j) XLNet (Mode 1)
(k) XLNet (Mode 2)
(l) XLNet (Mode 3)
Figure 7: Personality trait distributions of language models obtained from diﬀerent modes of
evaluation.
20

--- Page 21 ---

(a) WebText Test Set
(b) GPT-2 evaluated considering in-
put prompts from Big Five Ques-
tionnaire.
(c) GPT-2 evaluated without con-
sidering input prompts.
Figure 8: Distributions of diﬀerent traits in: (a) WebText Test Set , and (b) GPT-2.
Traits
Wasserstein distance
dataset vs GPT-2 with prompt
Wasserstein distance
dataset vs GPT-2 no prompt
Agreeableness
0.205
0.102
Conscientiousness
0.427
0.077
Extraversion
0.630
0.048
Emotional Stability
0.154
0.032
Openness
0.139
0.025
Table 7: Wasserstein distance between trait distributions of WebText dataset and GPT-2 model
evaluated with and without input prompts from the Big Five Questionnaire.
taking into account any speciﬁc type of input prompts, are nearly identical. This
suggests that GPT-2 inherits the traits of its training dataset. However, when
we passed the test from the Big Five questionnaire as input prompts, we noticed
a signiﬁcant diﬀerence in the trait distribution of the WebText Test dataset
compared to GPT-2 as measured using the Wasserstein distance (see Table 7). It
is important to note that relying solely on random generation may not accurately
represent the personality traits of the GPT-2 model. This limitation arises due
to the training of GPT-2 on WebText data, which primarily consists of factual
information lacking speciﬁc personality characteristics. Consequently, randomly
generated text may not reﬂect the language model’s inherent traits. To address
this limitation, we prompted the language model using the Big Five questionnaire,
which allowed us to drive the generated text to reﬂect the traits indicative of the
language model. Using the questionnaire as a guide enables an accurate reﬂection
of the personality traits of the language model, providing a more nuanced and
reliable picture of its traits.
5.4. Altering the Traits of Models
Setup:. To investigate the methods for altering traits, we restrict ourselves to
working with GPT-2 due to limitations on the computational resources available.
To evaluate Method 1 discussed in Section 4.3, we ﬁlter the SIOP (2019) dataset
21

--- Page 22 ---

by retaining text responses labeled with Big Five factor scores greater than 4
for the individual traits. We ﬁnetune the GPT-2 model on the ﬁltered dataset
corresponding to each trait independently and subsequently evaluate the generated
text responses. For ﬁnetuning, we set the batch size to 16 and the number of epochs
to 20 with warmup proportion set to 0, learning rate set to 1e−5, and weight decay
set to 0.01.
Similar to Method 1, we analyze Method 2 using the same ﬁltered dataset
SIOP (2019) according to the following criteria. The personality trait scores in
our dataset are continuous values from 1 to 5; To set up the model for binary
classiﬁcation, we derive binary target labels for diﬀerent thresholds from the set
{2.5, 3, 3.5, 4, 4.5}. To illustrate, for a given threshold of 2.5, all the text responses
annotated with a score less than 2.5 are labeled as zero and vice-versa. We ﬁnetune
the original model using this classiﬁcation task. In particular, we use the standard
cross-entropy loss and the Adam optimizer (Kingma & Ba, 2014). We set the
learning rate to 5e−5 and the number of epochs to 10 while ﬁnetuning.
(a) Original
(b) Agreeableness
(c) Conscientiousness
(d) Extraversion
(e) Emotional Stability
(f) Openness
Figure 9: Personality trait distributions of ﬁnetuned GPT-2.
Results:. Table 8 presents the results of Method 1 for ﬁnetuning GPT-2, which
indicate a signiﬁcant change in the personality scores for Agreeableness, Consci-
entiousness, Emotional Stability, and Openness after ﬁnetuning with the ﬁltered
datasets. These changes are also reﬂected in the personality trait distributions
of the ﬁnetuned GPT-2, as shown in Figure 9. Our ﬁndings demonstrate that
22

--- Page 23 ---

ﬁnetuning can alter the personality traits of language models like GPT-2 in an
open-loop setting by allowing them to learn from a new data corpus. However, we
also note that ﬁnetuning can change the personality scores of other traits besides
the focal trait represented by the ﬁltered dataset, which may be undesirable if
precise control over a speciﬁc trait improvement is required. This issue remains
an avenue for future research.
Trait
Before ﬁnetuning
Agreeableness
Conscientiousness
Extraversion
Emotional Stability
Openness
Agreeableness
3.41 (0.73)
3.33 (0.43)
3.30 (0.21)
3.27 (0.36)
3.09 (0.27)
3.33 (0.37)
Conscientiousness
3.18 (0.39)
3.41 (0.39)
3.26 (0.25)
3.15 (0.22)
3.13 (0.34)
3.50 (0.38)
Extraversion
3.07 (0.60)
3.27 (0.26)
3.39 (0.30)
3.39 (0.32)
3.15 (0.24)
3.63 (0.44)
Emotional Stability
3.15 (0.50)
3.35 (0.38)
3.26 (0.29)
3.27 (0.28)
3.23 (0.37)
3.42 (0.36)
Openness
2.97 (0.47)
3.42 (0.36)
3.37 (0.29)
3.31 (0.31)
3.27 (0.38)
3.47 (0.39)
Table 8: Personality scores with their uncertainties of the ﬁnetuned GPT-2.
Table 9 compares median scores for personality traits of the GPT-2 model ﬁne-
tuned using Method 2 on Extraversion annotated labels at diﬀerent thresholds. We
observe improvement Extraversion scores of the ﬁnetuned GPT-2 models compared
to the original GPT-2 model. However, we also observe noticeable changes in the
scores of other personality traits, similar to Method 1, which is not desirable. We
noticed similar changes in personality trait scores when the model was ﬁnetuned
using other personality-annotated datasets, as shown in Appendix A.
Trait
Before ﬁnetuning
After ﬁnetuning
at threshold (2.5)
After ﬁnetuning
at threshold (3.0)
After ﬁnetuning
at threshold (3.5)
After ﬁnetuning
at threshold (4.0)
After ﬁnetuning
at threshold (4.5)
Agreeableness
3.41 (0.73)
3.02 (0.48)
3.19 (0.54)
3.33 (0.64)
3.14 (0.76)
3.24 (0.57)
Conscientiousness
3.18 (0.39)
3.19 (0.53)
3.11 (0.49)
3.17 (0.67)
3.04 (0.57)
3.19 (0.57)
Extraversion
3.07 (0.60)
2.89 (0.51)
3.19 (0.53)
3.24 (0.75)
2.90 (0.74)
3.25 (0.49)
Emotional Stability
3.15 (0.50)
3.12 (0.67)
2.99 (0.45)
3.19 (0.64)
3.00 (0.74)
3.11 (0.46)
Openness
2.97 (0.47)
2.96 (0.51)
3.09 (0.55)
3.13 (0.67)
2.88 (0.80)
3.15 (0.54)
Table 9: Personality scores before and after ﬁnetuning the GPT-2 using Extraversion labeled
data at diﬀerent thresholds using the Method 2.
Overall, our methods for altering personality traits show initial promise in
altering the personality traits of language models. But some of the challenges still
remain. Speciﬁcally, since the personality of a language model is closely tied to its
text generation capabilities, changing one of them may aﬀect the other. Further
work in this direction would be a valuable endeavor.
6. Conclusion
In this paper, we developed approaches to quantify the personality traits of
datasets and language models designed for open-ended text generation. We pre-
sented a principled approach for evaluating the personality traits of datasets using
a pre-trained zero-shot classiﬁer. We then extended this idea to estimate person-
ality proﬁles of language models using the prompts from the Big Five personality
23

--- Page 24 ---

test questionnaire. Our experiments revealed that language models possess varied
personality traits reﬂecting the datasets used in their training, thus inﬂuencing
their generated outputs. Furthermore, we proposed straightforward approaches
to alter the personality traits of white-box language models by ﬁnetuning them
on personality-annotated datasets. Overall, our work provides a critical starting
point for assessing and understanding the personality traits of language models.
In future research, we aim to design robust approaches that can precisely alter
the personality traits of language models. We also aim to integrate other commonly
used assessments like the Myer Briggs Type indicator in assessing, validating, and
modifying the personality traits of language models.
References
Ahmad, R., Siemon, D., Fernau, D., & Robra-Bissantz, S. (2020). Introducing
raﬃ: A personality adaptive conversational agent. In PACIS (p. 28).
Akrami, N., Fernquist, J., Isbister, T., Kaati, L., & Pelzer, B. (2019). Automatic
extraction of personality from text: Challenges and opportunities. In 2019 IEEE
International Conference on Big Data (Big Data) (pp. 3156–3164). IEEE.
Bai, Y., Jones, A., Ndousse, K., Askell, A., Chen, A., DasSarma, N., Drain,
D., Fort, S., Ganguli, D., Henighan, T. et al. (2022). Training a helpful and
harmless assistant with reinforcement learning from human feedback.
arXiv
preprint arXiv:2204.05862, .
Bolukbasi, T., Chang, K.-W., Zou, J. Y., Saligrama, V., & Kalai, A. T. (2016).
Man is to computer programmer as woman is to homemaker? debiasing word
embeddings. Advances in Neural Information Processing Systems, 29, 4349–
4357.
Bordia, S., & Bowman, S. R. (2019).
Identifying and reducing gender bias in
word-level language models. arXiv preprint arXiv:1904.03035, .
Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Nee-
lakantan, A., Shyam, P., Sastry, G., Askell, A. et al. (2020). Language models
are few-shot learners. arXiv preprint arXiv:2005.14165, .
Dai, Z., Yang, Z., Yang, Y., Carbonell, J., Le, Q. V., & Salakhutdinov, R.
(2019). Transformer-XL: Attentive language models beyond a ﬁxed-length con-
text. arXiv preprint arXiv:1901.02860, .
Derekmracek (2020). Zero-shot classify Big ﬁve personality traits. URL: https:
//dmracek.github.io/explorations_code_nbs/exploration_zs_big5/.
24

--- Page 25 ---

Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2018). BERT: Pre-training
of deep bidirectional transformers for language understanding. arXiv preprint
arXiv:1810.04805, .
Digman, J. M. (1990). Personality structure: Emergence of the ﬁve-factor model.
Annual Review of Psychology, 41, 417–440.
Eysenck, H. J. (2012).
A model for personality.
Springer Science & Business
Media.
Gao, L., Biderman, S., Black, S., Golding, L., Hoppe, T., Foster, C., Phang, J.,
He, H., Thite, A., Nabeshima, N. et al. (2020). The pile: An 800gb dataset of
diverse text for language modeling. arXiv preprint arXiv:2101.00027, .
Gokaslan, A., & Cohen, V. (2019).
Openwebtext corpus, .
URL: http:
//Skylion007.github.io/OpenWebTextCorpus.
Hoﬀa,
F.
(2016).
Github
on
bigquery:
Analyze
all
the
open
source
code.
URL: https://cloud.google.com/blog/topics/public-datasets/
github-on-bigquery-analyze-all-the-open-source-code.
Jeremy, N. H., Prasetyo, C., & Suhartono, D. (2019). Identifying personality traits
for Indonesian users from twitter dataset. International Journal of Fuzzy Logic
and Intelligent Systems, 19, 283–289.
Kingma, D. P., & Ba, J. (2014). Adam: A method for stochastic optimization.
arXiv preprint arXiv:1412.6980, .
Lewkowycz, A., Andreassen, A., Dohan, D., Dyer, E., Michalewski, H., Ra-
masesh, V., Slone, A., Anil, C., Schlag, I., Gutman-Solo, T. et al. (2022).
Solving quantitative reasoning problems with language models. arXiv preprint
arXiv:2206.14858, .
Liu, L., Preotiuc-Pietro, D., Samani, Z. R., Moghaddam, M. E., & Ungar, L.
(2016). Analyzing personality through social media proﬁle picture choice. In
10th International AAAI Conference on Web and Social Media.
Liu, Y., & Lapata, M. (2018). Learning structured text representations. Transac-
tions of the Association for Computational Linguistics, 6, 63–75.
Ma, T., Yao, J.-G., Lin, C.-Y., & Zhao, T. (2021). Issues with entailment-based
zero-shot text classiﬁcation. In Proceedings of the 59th Annual Meeting of the As-
sociation for Computational Linguistics and the 11th International Joint Confer-
ence on Natural Language Processing (Volume 2: Short Papers) (pp. 786–796).
25

--- Page 26 ---

Mehta, Y., Majumder, N., Gelbukh, A., & Cambria, E. (2020). Recent trends
in deep learning based personality detection. Artiﬁcial Intelligence Review, 53,
2313–2339.
Merity, S., Xiong, C., Bradbury, J., & Socher, R. (2016). Pointer sentinel mixture
models. arXiv preprint arXiv:1609.07843, .
Miles, J., & Hempel, S. (2004). The Eysenck personality scales: The Eysenck
personality questionnaire-revised (EPQ-R) and the Eysenck personality proﬁler
(EPP). Comprehensive Handbook of Psychological Assessment, 2, 99–107.
Nadeem, M., Bethke, A., & Reddy, S. (2020). Stereoset: Measuring stereotypical
bias in pretrained language models. arXiv preprint arXiv:2004.09456, .
Pennebaker, J. W., & King, L. A. (1999). Linguistic styles: language use as an
individual diﬀerence. Journal of Personality and Social Psychology, 77, 1296.
Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., Sutskever, I. et al. (2019).
Language models are unsupervised multitask learners.
Raﬀel, C., Shazeer, N., Roberts, A., Lee, K., Narang, S., Matena, M., Zhou, Y.,
Li, W., & Liu, P. J. (2020). Exploring the limits of transfer learning with a
uniﬁed text-to-text transformer. The Journal of Machine Learning Research,
21, 5485–5551.
Ray, P. P. (2023). Chatgpt: A comprehensive review on background, applications,
key challenges, bias, ethics, limitations and future scope. Internet of Things and
Cyber-Physical Systems, .
Schuerger, J. M. (2000).
The sixteen personality factor questionnaire (16PF).
Testing and Assessment in Counseling Practice, (pp. 73–110).
Sheng, E., Chang, K.-W., Natarajan, P., & Peng, N. (2019).
The woman
worked as a babysitter:
On biases in language generation.
arXiv preprint
arXiv:1909.01326, .
SIOP (2019). Evaluating state of the art in AI. URL: https://eval.ai/web/
challenges/challenge-page/160/overview online. Last Accessed September
6th 2021.
Soares, M. A. C., & Parreiras, F. S. (2020).
A literature review on question
answering techniques, paradigms and systems. Journal of King Saud University-
Computer and Information Sciences, 32, 635–646.
26

--- Page 27 ---

Spencer, J., Poggi, J., & Gheerawo, R. (2018). Designing out stereotypes in artiﬁ-
cial intelligence: Involving users in the personality design of a digital assistant.
In Proceedings of the 4th EAI international conference on smart objects and
technologies for social good (pp. 130–135).
StackExchange (2017). Stack exchange data dump. URL: https://archive.org/
details/stackexchange.
Touvron, H., Lavril, T., Izacard, G., Martinet, X., Lachaux, M.-A., Lacroix, T.,
Rozi`ere, B., Goyal, N., Hambro, E., Azhar, F. et al. (2023). Llama: Open and
eﬃcient foundation language models. arXiv preprint arXiv:2302.13971, .
Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N.,
Kaiser,  L., & Polosukhin, I. (2017). Attention is all you need. Advances in
Neural Information Processing Systems, 30.
Wenzek, G., Lachaux, M.-A., Conneau, A., Chaudhary, V., Guzm´an, F., Joulin,
A., & Grave, E. (2019). Ccnet: Extracting high quality monolingual datasets
from web crawl data. arXiv preprint arXiv:1911.00359, .
Wolf, T., Debut, L., Sanh, V., Chaumond, J., Delangue, C., Moi, A., Cistac, P.,
Rault, T., Louf, R., Funtowicz, M. et al. (2019). Huggingface’s transformers:
State-of-the-art natural language processing. arXiv preprint arXiv:1910.03771,
.
Yang, Z., Dai, Z., Yang, Y., Carbonell, J., Salakhutdinov, R. R., & Le, Q. V.
(2019). Xlnet: Generalized autoregressive pretraining for language understand-
ing. Advances in Neural Information Processing Systems, 32.
Ye, J., Chen, X., Xu, N., Zu, C., Shao, Z., Liu, S., Cui, Y., Zhou, Z., Gong, C.,
Shen, Y. et al. (2023). A comprehensive capability analysis of gpt-3 and gpt-3.5
series models. arXiv preprint arXiv:2303.10420, .
Yin, W., Hay, J., & Roth, D. (2019).
Benchmarking zero-shot text clas-
siﬁcation:
Datasets, evaluation and entailment approach.
arXiv preprint
arXiv:1909.00161, .
Zhu, Y., Kiros, R., Zemel, R., Salakhutdinov, R., Urtasun, R., Torralba, A., &
Fidler, S. (2015). Aligning books and movies: Towards story-like visual expla-
nations by watching movies and reading books.
In Proceedings of the IEEE
International Conference on Computer Vision (pp. 19–27).
Zong, Z., & Hong, C. (2018). On application of natural language processing in ma-
chine translation. In 2018 3rd International Conference on Mechanical, Control
and Computer Engineering (ICMCCE) (pp. 506–510). IEEE.
27

--- Page 28 ---

Appendix A. Additional Details
Wasserstein Distance (dp). It is a measure of the distance between two proba-
bility distributions. It quantiﬁes the amount of work required to transform one
distribution into the other.
The Wasserstein distance between two cumulative
distributions, P and Q, is given by:
dp(P, Q) := inf
U,V
||U −P||p
(A.1)
Where the inﬁmum is taken over all pairs of random variables (U, V ) with
respective cumulative distributions P and Q.
Adam. It is an optimization algorithm that extends the capabilities of stochastic
gradient descent (SGD) by incorporating adaptive learning rates for all the pa-
rameters. The adaptive learning rates allow the optimizer to converge faster and
more accurately, even in noisy or sparse gradients.
Learning Rate. It is a hyperparameter that controls the amount by which the
model weights need to be updated with respect to gradient loss during the training.
Epoch. It refers to one complete pass through the entire training dataset during
the training of a model
Weight Decay. It is a regularization hyperparameter used to prevent the overﬁtting
of models. It works by adding a penalty term to the loss function during training,
which enables the model to learn simpler and smoother weight conﬁgurations.
Warmup Proportion. It is a hyperparameter that determines the percentage of
training steps during which the learning rate is gradually increased from an initial
value to its maximum value
Tables A.10, A.11, A.12 and A.13 shows detailed results of ﬁnetuning GPT-2
model using Method 2 on personality annotated data.
Trait
Before ﬁnetuning
After ﬁnetuning
at threshold (2.5)
After ﬁnetuning
at threshold (3.0)
After ﬁnetuning
at threshold (3.5)
After ﬁnetuning
at threshold (4.0)
After ﬁnetuning
at threshold (4.5)
Agreeableness
3.41 (0.73)
3.51 (0.51)
3.19 (0.30)
3.19 (0.44)
3.10 (0.68)
3.04 (0.45)
Conscientiousness
3.18 (0.39)
3.29 (0.53)
3.17 (0.41)
3.13 (0.34)
3.26 (0.57)
3.36 (0.47)
Extraversion
3.07 (0.60)
3.24 (0.55)
3.13 (0.29)
3.20 (0.27)
3.00 (0.63)
3.04 (0.42)
Emotional Stability
3.15 (0.46)
3.42 (0.53)
3.15 (0.37)
3.11 (0.42)
3.09 (0.70)
2.94 (0.34)
Openness
2.97 (0.47)
3.33 (0.56)
3.23 (0.36)
3.26 (0.38)
3.03 (0.50)
3.11 (0.45)
Table A.10: Personality scores before and after ﬁnetuning the GPT-2 using Conscientiousness
labeled data at diﬀerent thresholds using the Method 2
28

--- Page 29 ---

Trait
Before ﬁnetuning
After ﬁnetuning
at threshold (2.5)
After ﬁnetuning
at threshold (3.0)
After ﬁnetuning
at threshold (3.5)
After ﬁnetuning
at threshold (4.0)
After ﬁnetuning
at threshold (4.5)
Agreeableness
3.41 (0.73)
3.05 (0.45)
3.22 (0.34)
2.83 (0.49)
2.99 (0.71)
3.06 (0.13)
Conscientiousness
3.18 (0.39)
3.08 (0.38)
3.28 (0.49)
2.93 (0.49)
3.12 (0.72)
3.09 (0.11)
Extraversion
3.07 (0.60)
3.03 (0.41)
3.30 (0.46)
2.90 (0.47)
3.11 (0.71)
3.08 (0.10)
Emotional Stability
3.15 (0.50)
3.09 (0.37)
3.17 (0.41)
2.93 (0.45)
3.09 (0.60)
3.08 (0.14)
Openness
2.97 (0.47)
3.08 (0.38)
3.22 (0.44)
3.07 (0.32)
3.04 (0.78)
3.09 (0.12)
Table A.11: Personality scores before and after ﬁnetuning the GPT-2 using Openness labeled
data at diﬀerent thresholds using the Method 2
Trait
Before ﬁnetuning
After ﬁnetuning
at threshold (2.5)
After ﬁnetuning
at threshold (3.0)
After ﬁnetuning
at threshold (3.5)
After ﬁnetuning
at threshold (4.0)
After ﬁnetuning
at threshold (4.5)
Agreeableness
3.41 (0.73)
3.83 (0.55)
3.05 (0.49)
2.89 (0.18)
2.93 (0.73)
3.04 (0.69)
Conscientiousness
3.18 (0.39)
3.31 (0.55)
2.98 (0.42)
2.90 (0.15)
3.02 (0.80)
3.05 (0.80)
Extraversion
3.07 (0.60)
3.38 (0.77)
3.06 (0.47)
2.90 (0.13)
2.99 (0.76)
3.20 (0.58)
Emotional Stability
3.15 (0.50)
3.16 (0.52)
3.01 (0.55)
3.17 (0.12)
3.14 (0.75)
3.22 (0.71)
Openness
2.97 (0.47)
3.15 (0.59)
3.19 (0.51)
2.91 (0.17)
3.19 (0.76)
3.07 (0.83)
Table A.12: Personality scores before and after ﬁnetuning the GPT-2 using Emotional stability
labeled data at diﬀerent thresholds using the Method 2
Trait
Before ﬁnetuning
After ﬁnetuning
at threshold (2.5)
After ﬁnetuning
at threshold (3.0)
After ﬁnetuning
at threshold (3.5)
After ﬁnetuning
at threshold (4.0)
After ﬁnetuning
at threshold (4.5)
Agreeableness
3.41 (0.73)
3.39 (0.73)
3.37 (0.63)
3.42 (0.51)
3.49 (0.23)
3.55 (0.36)
Conscientiousness
3.18 (0.39)
3.10 (0.80)
2.88 (0.57)
3.03 (0.70)
3.06 (0.31)
3.04 (0.24)
Extraversion
3.07 (0.60)
3.06 (0.66)
2.98 (0.61)
3.01 (0.40)
3.05 (0.24)
3.08 (0.38)
Emotional Stability
3.15 (0.50)
3.08 (0.66)
3.00 (0.65)
3.04 (0.40)
3.03 (0.19)
3.03 (0.25)
Openness
2.97 (0.47)
3.28 (0.66)
2.91 (0.62)
3.16 (0.32)
3.04 (0.13)
3.06 (0.22)
Table A.13: Personality scores before and after ﬁnetuning the GPT-2 using Agreeableness labeled
data at diﬀerent thresholds using the Method 2
29

--- Page 30 ---

I am the life of the party.
I have little to say.
I feel little concern for others.
I have a soft heart.
I am always prepared.
I often forget to put things back in their proper place.
I get stressed out easily.
I get upset easily.
I have a rich vocabulary.
I do not have a good imagination.
I don’t talk a lot.
I talk to a lot of diﬀerent people at parties.
I am interested in people.
I am not really interested in others.
I leave my belongings around.
I like order.
I am relaxed most of the time.
I change my mood a lot.
I have diﬃculty understanding abstract ideas.
I am quick to understand things.
I feel comfortable around people.
I don’t like to draw attention to myself.
I insult people.
I take time out for others.
I pay attention to details.
I shirk my duties.
I worry about things.
I have frequent mood swings.
I have a vivid imagination.
I use diﬃcult words.
I keep in the background.
I don’t mind being the center of attention.
I sympathize with others’ feelings.
I feel others’ emotions.
I make a mess of things.
I follow a schedule.
I seldom feel blue.
I get irritated easily.
I am not interested in abstract ideas.
I spend time reﬂecting on things.
I start conversations.
I am quiet around strangers.
I am not interested in other people’s problems.
I make people feel at ease.
I get chores done right away.
I am exacting in my work.
I am easily disturbed.
I often feel blue.
I have excellent ideas.
I am full of ideas.
Table A.14: Questions from the Big Five questionnaire
30

```
