---
title: "2019-Unknown-EmpatheticDialogues Towards Empathetic Open-domain Conversation Models - PDF Extract"
source_pdf: "2019-Unknown-EmpatheticDialogues Towards Empathetic Open-domain Conversation Models.pdf"
pages: 18
extracted_at: "2026-02-07T16:58:58.259387"
---

# PDF Extract: 2019-Unknown-EmpatheticDialogues Towards Empathetic Open-domain Conversation Models

**Source PDF:** 2019-Unknown-EmpatheticDialogues Towards Empathetic Open-domain Conversation Models.pdf
**Total Pages:** 18

---

## Content

```
--- Page 1 ---

Towards Empathetic Open-domain Conversation Models: a New
Benchmark and Dataset
Hannah Rashkin1⋆, Eric Michael Smith2, Margaret Li2, Y-Lan Boureau2
1 Paul G. Allen School of Computer Science & Engineering, University of Washington
2 Facebook AI Research
hrashkin@cs.washington.edu, {ems,margaretli,ylan}@fb.com
Abstract
One challenge for dialogue agents is recog-
nizing feelings in the conversation partner and
replying accordingly, a key communicative
skill. While it is straightforward for humans
to recognize and acknowledge others’ feelings
in a conversation, this is a signiﬁcant chal-
lenge for AI systems due to the paucity of
suitable publicly-available datasets for train-
ing and evaluation. This work proposes a new
benchmark for empathetic dialogue genera-
tion and EMPATHETICDIALOGUES, a novel
dataset of 25k conversations grounded in emo-
tional situations.
Our experiments indicate
that dialogue models that use our dataset
are perceived to be more empathetic by hu-
man evaluators, compared to models merely
trained on large-scale Internet conversation
data.
We also present empirical compar-
isons of dialogue model adaptations for em-
pathetic responding, leveraging existing mod-
els or datasets without requiring lengthy re-
training of the full model.
1
Introduction
A desirable trait in a human-facing dialogue
agent is to appropriately respond to a conversa-
tion partner that is describing personal experi-
ences, by understanding and acknowledging any
implied feelings — a skill we refer to as em-
pathetic responding.
For instance, while the
crossed-out response in Figure 1 is topically rel-
evant, “Congrats! That’s great!” may be more
satisfying because it acknowledges the underly-
ing feelings of accomplishment in an empathetic
way.
In this work, we investigate empathetic
response generation from current dialogue sys-
tems, and propose experiments using a new re-
source, EMPATHETICDIALOGUES, as a bench-
mark to evaluate this skill set.
⋆This work was done while ﬁrst author was intern at
Facebook AI Research (FAIR).
I ﬁnally got promoted today at work.
Why would anyone 
promote you?
Congrats! That’s great!
feels proud
😀
EMPATHETICDIALOGUES dataset example
Listener
Speaker
Figure 1: Example where acknowledging an inferred
feeling is appropriate
Empathetic responding is clearly relevant to
dialogue systems that are geared towards gen-
eral conversation or chit-chat.
Indeed, ordinary
communication is frequently prompted by peo-
ple sharing their feelings or circumstances. But
researchers analyzing goal-directed conversations
have also observed the frequent intrusion of or-
dinary conversation in those interactions as well,
either as a “warm-up” introduction or as a de-
tour (Levinson et al., 2000; Heritage, 2005). En-
gaging in social talk, reacting to emotional cues
and displaying a caring attitude have, in fact,
been associated with better task outcomes in many
domains (Wentzel, 1997; Levinson et al., 2000;
Bickmore and Cassell, 2001; Kim et al., 2004;
Fraser et al., 2018). While many of those stud-
ies deal with human-human interactions, humans
have been shown to often interact with machines
in a natural and social way (Reeves and Nass,
1996; Lee et al., 2010), so it is reasonable to ex-
pect that dialogue agents would also beneﬁt from
empathetic responding.
Most recent powerful language architectures are
trained on vast amounts of barely curated text
scrapes, social media conversations, or indepen-
dent books (Ritter et al., 2010; Zhang et al., 2018;
Mazare et al., 2018; Devlin et al., 2018; Liu et al.,
2019; Radford et al., 2019). It might be the case
arXiv:1811.00207v5  [cs.CL]  28 Aug 2019

--- Page 2 ---

Label: Afraid
Situation: Speaker felt this when...
“I’ve been hearing noises around the house at night”
Conversation:
Speaker: I’ve been hearing some strange noises around
the house at night.
Listener: oh no! That’s scary! What do you think it is?
Speaker: I don’t know, that’s what’s making me anx-
ious.
Listener: I’m sorry to hear that. I wish I could help you
ﬁgure it out
Label: Proud
Situation: Speaker felt this when...
“I ﬁnally got that promotion at work! I have tried so
hard for so long to get it!”
Conversation:
Speaker: I ﬁnally got promoted today at work!
Listener: Congrats! That’s great!
Speaker: Thank you! I’ve been trying to get it for a
while now!
Listener: That is quite an accomplishment and you
should be proud!
Figure 2: Two examples from EMPATHETICDIALOGUES training set. The ﬁrst worker (the speaker) is given an
emotion label and writes their own description of a situation when they’ve felt that way. Then, the speaker tells
their story in a conversation with a second worker (the listener).
that models trained on this type of data could ex-
hibit some of the aggressive and callous responses
that have been observed in spontaneous internet
conversations (Anderson, 2015).
Unfortunately,
while chitchat dialogue benchmarks have been
proposed (e.g., Dinan et al., 2019), to the best
of our knowledge there are currently no bench-
marks gauging whether dialogue agents can con-
verse with empathy.
This work aims to facilitate evaluating models’
ability to produce empathetic responses. We intro-
duce a new task for dialogue systems to respond
to people discussing situations that cover a wide
range of emotions, and EMPATHETICDIALOGUES
(ED), a novel dataset with about 25k personal di-
alogues. Each dialogue is grounded in a speciﬁc
situation where a speaker was feeling a given emo-
tion, with a listener responding (Figure 2). The
new resource consists of crowdsourced one-on-
one conversations, and covers a large set of emo-
tions in a balanced way. This dataset is larger and
contains a more extensive set of emotions than
many similar emotion prediction datasets from
other text domains such as Scherer and Wallbott
(1994), Strapparava and Mihalcea (2007), Mo-
hammad et al. (2018), and Gupta et al. (2017). The
dataset has been publicly released, with code to re-
produce the main experimental results of this pa-
per1.
Our experiments show that large-capacity con-
versation models trained on spontaneous internet
conversation data are not rated as very empathetic.
We propose two simple ways to leverage our
dataset to improve those models: use utterances
from our training data as candidate responses in a
retrieval model at inference time, and ﬁne-tune the
model on our task. Finally, we explore whether
1https://github.com/facebookresearch/EmpatheticDialogues
different ways of combining information from re-
lated tasks can lead to more empathetic responses.
The contributions of this work are thus: 1) we
release a novel empathetic dialogue dataset as a
new benchmark; 2) we show that training over this
dataset can improve the performance of an end-to-
end dialogue system on empathetic dialogue.
2
Related Work
Emotion data
Crafting our dataset requires de-
ciding what set of emotions the models should be
capable of reacting to.
Multiple schemas have
attempted to organize the spectrum of emotions,
from a handful of basic emotions derived from bi-
ological responses (Ekman, 1992; Plutchik, 1984)
to larger sets of subtle emotions inferred from
contextual situations (Skerry and Saxe, 2015).
We incorporate emotions from multiple annota-
tion schemas, noting that emotions merely in-
ferred from a situation are important in dialogue
scenarios. There is a wide breadth of research in
distributional representation approaches for many
emotion classiﬁcation tasks (Duppada et al., 2018;
Park et al., 2018; Xu et al., 2018; Mohammad
et al., 2018) that build on deep networks pretrained
on large-scale weakly-labelled data such as emo-
jis (Felbo et al., 2017) or hashtags (Mohammad,
2012), gathered from public social media content
published on Twitter. The SEMEVAL2019 Emo-
Context challenge also uses conversation data for
detection of three basic emotions (‘happy’, ‘sad’,
and ‘angry’) over two turns of context from Twit-
ter exchanges (Gupta et al., 2017).
We focus
on personal conversations rather than using social
media data to be closer to a context of a one-on-
one conversation. Public social media content oc-
curs in front of large “peripheral audiences” (Goff-
man, 1981) where uncertainty as to how wide

--- Page 3 ---

that audience is and the need for curated self-
presentation (Goffman, 1959) have been shown to
lead to different choices of subject matters com-
pared to private messaging, with people sharing
more intense and negative emotions through pri-
vate channels (Bazarova et al., 2015; Litt et al.,
2014). In this work, we generate a more balanced
coverage of emotions than would appear in public
social media content, using a domain that is closer
to our ultimate goal of training a model for con-
versation that can respond to any emotion.
Controllable
language
generation
Several
other works have focused on controlling the emo-
tional content of a text response either through
a manually speciﬁed target (Zhou and Wang,
2018; Zhou et al., 2018; Wang and Wan, 2018;
Hu et al., 2017; Huang et al., 2018) or through a
general term to encourage higher levels of affect
(Asghar et al., 2018), with evaluations focused
on matching a predetermined desired emotion
rather than empathetic responding.
Niu and
Bansal (2018) generate responses conditioned
on a speciﬁed politeness setting (polite, rude or
neutral). Huber et al. (2018) investigate how to
respond to emotions detected from an image. Our
work focuses on empathetic responses that are
appropriate to signals inferred purely from text
rather than conveying a pre-speciﬁed emotion.
Related chit-chat data
Several works have at-
tempted to make chit-chat dialogue models more
engaging by grounding them in personal contexts
(Li et al., 2016b; Zhang et al., 2018; Mazare et al.,
2018), focusing on personal facts (“I am from New
York”). Another interesting resource is the DAI-
LYDIALOG (DD) dataset (Li et al., 2017), which
comprises about 13k dialogues obtained by crawl-
ing educational websites intended for learners of
English and also has emotion label annotations.
Many of the dialogues are focused on topics for
ESL learners (ordering from a restaurant, asking
for directions, introductions, etc), but only ≈5%
of the utterances have a label other than “none” or
“happy”. Our task focuses explicitly on conversa-
tions about emotionally grounded personal situa-
tions, and considers a richer, evenly distributed set
of emotions. We also introduce an explicit single
listener in the conversation who is reacting to the
situation being described in an empathetic way, to
make the setting as close as possible to our desired
goal of a one-on-one empathetic conversation.
Emotion
Most-used 
speaker words
Most-used 
listener words
Surprised
got,shocked,really
that's,good,nice
Excited
going,wait,i'm
that's,fun,like
Angry
mad,someone,got
oh,would,that's
Proud
got,happy,really
that's,great,good
Sad
really,away,get
sorry,oh,hear
Annoyed
get,work,really
that's,oh,get
Grateful
really,thankful,i'm
that's,good,nice
Lonely
alone,friends,i'm
i'm,sorry,that's
Afraid
scared,i'm,night
oh,scary,that's
Terriﬁed
scared,night,i'm
oh,that's,would
Guilty
bad,feel,felt
oh,that's,feel
Impressed
really,good,got
that's,good,like
Disgusted
gross,really,saw
oh,that's,would
Hopeful
i'm,get,really
hope,good,that's
Conﬁdent
going,i'm,really
good,that's,great
Furious
mad,car,someone
oh,that's,get
Anxious
i'm,nervous,going
oh,good,hope
Anticipating
wait,i'm,going
sounds,good,hope
Joyful
happy,got,i'm
that's,good,great
Nostalgic
old,back,really
good,like,time
Disappointed
get,really,work
oh,that's,sorry
Prepared
ready,i'm,going
good,that's,like
Jealous
friend,got,get
get,that's,oh
Content
i'm,life,happy
good,that's,great
Devastated
got,really,sad
sorry,oh,hear
Embarrassed
day,work,got
oh,that's,i'm
Caring
care,really,taking
that's,good,nice
Sentimental
old,really,time
that's,oh,like
Trusting
friend,trust,know
good,that's,like
Ashamed
feel,bad,felt
oh,that's,i'm
Apprehensive
i'm,nervous,really
oh,good,well
Faithful
i'm,would,years
good,that's,like
1.9%
2.4%
2.5%
2.6%
2.7%
2.7%
2.9%
2.9%
2.9%
3%
3%
3.1%
3.1%
3.1%
3.1%
3.1%
3.1%
3.2%
3.2%
3.2%
3.2%
3.2%
3.2%
3.2%
3.3%
3.3%
3.4%
3.4%
3.5%
3.6%
3.8%
5.1%
Training set 
emotion distrib
Figure 3: Distribution of conversation labels within
EMPATHETICDIALOGUES training set and top 3 con-
tent words used by speaker/listener per category.
3
Talking about Personal Situations
We consider an open-domain one-on-one conver-
sational setting where two people are discussing a
situation that happened to one of them, related to
a given feeling. We collect around 25k conversa-
tions using the following format.
Emotional situation grounding
Each conversa-
tion is grounded in a situation, which one par-
ticipant writes about in association with a given
emotion label.
We consider 32 emotion labels,
listed in Figure 3, which we chose by aggregat-
ing labels from several emotion prediction datasets
(Scherer and Wallbott, 1994; Strapparava and Mi-
halcea, 2007; Skerry and Saxe, 2015; Li et al.,
2017; Mohammad, 2012). These emotion labels
cover a broad range of positive and negative emo-
tions. Our goal in providing a single emotion la-
bel is to have a situation strongly related to (at
least) one particular emotional experience, though
we note that some emotions may be very closely
related2 and additional related emotions may be
2Researchers could merge similar emotions, like ”afraid”
and ”terriﬁed”, to get coarser labels, if desired.

--- Page 4 ---

invoked in a given conversation.
Speaker and listener
The person who wrote the
situation description (Speaker) initiates a conver-
sation to talk about it. The other conversation par-
ticipant (Listener) becomes aware of the underly-
ing situation through what the Speaker says and
responds. Speaker and Listener then exchange up
to 6 more turns. We include two example con-
versations from the training data in Figure 2 and
ten more in Table 5 in the Appendix. The models
discussed below are tested in the role of Listener
responding to the Speaker. Neither the situation
description written by the Speaker nor the emotion
label is given to the models (just as they were not
given to the Listener during dialogue collection).
Our data could also be used to generate conversa-
tions for the Speaker conditioned on the situation
description though we leave this for future work.
Collection details
We collected crowdsourced
dialogues using the ParlAI platform (Miller et al.,
2017) to interact with Amazon Mechanical Turk
(MTurk), hiring 810 US workers. A pair of work-
ers are asked to (i) select an emotion word each
and describe a situation when they felt that way,
and to (ii) have a conversation about each of the
situations, as outlined below.
Each worker had
to contribute at least one situation description and
one pair of conversations: one as Speaker about
the situation they contributed, and one as Listener
about the situation contributed by another worker.
They were allowed to participate in as many hits as
they wanted for the ﬁrst ∼10k conversations, then
we limited the more “frequently active” workers
to a maximum of 100 conversations. The median
number of conversations per worker was 8, while
the average was 61 (some workers were more ac-
tive contributors than others). To ensure quality,
we manually checked random subsets of conver-
sations by our most-frequent workers.
Task set-up
In the ﬁrst stage of the task, work-
ers are asked to describe in a few sentences a situ-
ation based on a feeling label. We ask the workers
to try to keep these descriptions between 1-3 sen-
tences. The average response is 19.8 words. In the
second stage, two workers are paired and asked
to have two short chats with each other. In each
chat, one worker (speaker) starts a conversation
about the situation they previously described, and
the other worker (listener) responds. Neither can
see what the other worker was given as emotion
label or the situation description they submitted,
so they must respond to each others’ stories based
solely on cues within the conversation. Each con-
versation is allowed to be 4-8 utterances long (the
average is 4.31 utterances per conversation). The
average utterance length was 15.2 words long.
Ensuring balanced emotion coverage
After
the ﬁrst few initial rounds of data collection, we
forced workers to select an emotion that among
three emotion labels that had been the least cho-
sen overall so far if it was their ﬁrst time work-
ing on the task. If they had already performed the
task, the offered emotion labels were among those
that they had chosen the least often before. Given
that a conversation model trained for empathetic
responding needs to be able to handle emotions
even if they are less frequent, we opted for this
balancing procedure to make training for these cat-
egories easier, while still allowing for some mea-
sure of choice for workers. As shown in Figure 3,
the distribution of emotion label prompts is close
to evenly distributed, with a few that are selected
slightly more/less often.
EMPATHETICDIALOGUES
dataset
statistics
The resulting dataset comprises 24,850 conversa-
tions about a situation description, gathered from
810 different participants, which are publicly
available through the ParlAI framework3 and for
direct download with accompanying code4. We
split the conversations into approximately 80%
train, 10% validation, and 10% test partitions. To
prevent overlap of discussed situations between
partitions, we split the data so that all sets of
conversations with the same speaker providing
the initial situation description would be in the
same partition. The ﬁnal train/val/test split was
19533 / 2770 / 2547 conversations, respectively.
We include ten examples from our training set in
Appendix Section A.
4
Empathetic Response Generation
This section shows how ED can be used as a
benchmark to gauge the ability of a model to re-
spond in an empathetic way, and as a training re-
source to make generic chitchat models more em-
pathetic. We also examine different ways existing
models can be combined to produce more empa-
thetic responses. We use ED dialogues to train
3https://parl.ai/
4https://github.com/facebookresearch/EmpatheticDialogues

--- Page 5 ---

y* = argmax hx ⋅hy
x1 x2 . . .
x1 x2 . . .
y1 y2 . . .
</s> y1 y2 . . .
p(¯y|x)
hy
hx
Context 
Encoder
Context 
Encoder
Candidate 
 Encoder
Transformer 
Decoder
Generative Architecture
Retrieval Architecture
Figure 4: Dialogue generation architectures used in our
experiments. The context of concatenated previous ut-
terances is tokenized into x1, x2, · · · , and encoded into
vector hx by the context encoder. Left: In the retrieval
set-up, each candidate y is tokenized into y1, y2, · · ·
and encoded into vector hy by the candidate encoder.
The system outputs the candidate y∗that maximizes
dot product hx · hy. Right: In the generative set-up,
the encoded context hx is used as input to the decoder
to generate start symbol </s> and tokens y1, y2, · · · .
The model is trained to minimize the negative log-
likelihood of target sequence ¯y conditioned on context.
and evaluate models in the task of generating con-
versation responses in the Listener role. To emu-
late a normal conversation, the model has access
to previous utterances in the dialogue, but not to
the emotion word prompt (e.g., “proud”), nor to
the situation description generated by the Speaker.
Given a dialogue context x of n previous con-
versation utterances concatenated and tokenized
as x1, · · · , xm, followed by a target response ¯y,
our models are trained to maximize the likelihood
p(¯y|x) of producing the target response. We inves-
tigate both generative and retrieval-based settings
(Lowe et al., 2016) as described in Figure 4.
4.1
Base Architecture
We base our models on Transformer networks
(Vaswani et al., 2017), which have proven success-
ful in machine translation and dialogue generation
tasks (Zhang et al., 2018; Mazare et al., 2018).
Retrieval-based
In the retrieval-based set-up,
the model is given a large set Y of candidate re-
sponses and picks the “best” one, y∗.
We ﬁrst
experiment with the retrieval Transformer-based
architecture from Yang et al. (2018): two Trans-
former encoders separately embedding the con-
text, x, and candidates, y ∈Y , as hx and hy,
respectively. We also experiment with BERT (De-
vlin et al., 2018) as base architecture to encode
candidates and contexts, using the ﬁnal hidden
vector from BERT as the hx or hy encodings. The
model chooses a candidate utterance according to
a softmax on the dot product: hx·hy. We minimize
the negative log-likelihood of selecting the correct
candidate. At training time, we use all of the ut-
terances from the batch as candidates, with a large
batch size of 512 to give the model more negative
examples (except for BERT for which a batch size
of 256 was used). At inference time, we exper-
iment with three sets of candidate utterances for
the model to choose from: all of the response ut-
terances in the ED training set (Y ED), all the utter-
ances in the DailyDialog (Li et al., 2017) training
set (Y DD), and a million utterances from a dump
of 1.7 billion Reddit (R) conversations (Y R).
Generative
In the generative set-up, we use
the full Transformer architecture (Vaswani et al.,
2017), consisting of an encoder and a decoder.
The Transformer decoder uses the encoder output
to predict a sequence of words y, and is trained
to minimize the negative log-likelihood of the tar-
get sequence ¯y. At inference time, we use diverse
beam search from Vijayakumar et al. (2016).
Training details
Models are pretrained on pre-
dicting replies from a dump of 1.7 billion Reddit
conversations, starting either from scratch for the
Transformer architectures, or from the BERTbase
model released by Devlin et al. (2018) for the
BERT-based architectures.5
Pretrained models
without any ﬁne-tuning on ED will be referred
to as “Pretrained” hereafter. We limit the maxi-
mum number of word tokens in the context and
response to be 100 each. The Transformer net-
works used in most experiments have the same
base architecture (four layers and six transformer
heads) and are trained the same way as in Mazare
et al. (2018). We also experiment with a larger
architecture of ﬁve layers (denoted as ”Large”),
and BERT retrieval models, that are allowed to
train for much longer (see training times in Ta-
ble 3).6 For all models, we keep the version that
has the lowest loss on the validation set. For the
Transformer models, we use 300-d word embed-
5We used the Hugging Face PyTorch implementa-
tion of BERT at https://github.com/huggingface/pytorch-
transformers.
We experimented with directly ﬁne-tuning
BERT on ED without ﬁrst training on Reddit conversations,
but this did not perform as well.
6While the models had not fully converged when we
stopped training, we trained the Pretrained models for a few
iterations more than the corresponding Fine-Tuned models,
to ensure that any observed improvement was due to the data
used for ﬁne-tuning and not the extra training time.

--- Page 6 ---

Pre-trained 
Emotion Classiﬁer
embarrassed I slipped and…
I slipped and fell on my face
hw
Encoder
Figure 5: Incorporating additional supervised informa-
tion, here from an emotion classiﬁcation task. An input
sequence (either a dialogue context or a candidate) is
run through a pre-trained classiﬁer, and the top k out-
put labels are prepended to the sequence, which is then
run through the corresponding (context or candidate)
encoder to output a hidden representation hw (either
hx or hy) as in the base setting.
dings pretrained on common-crawl data using fast-
Text (Grave et al., 2018), and for the BERT mod-
els, we use 768-d word embeddings pretrained
on BooksCorpus and English Wikipedia (Devlin
et al., 2018). More training details are provided in
Appendix D.1.
4.2
Leveraging the Training Data from ED
A retrieval-based model relies on candidates. ED
data was explicitly collected with instructions to
be empathetic, in a one-on-one setting, which is
not the case of the Reddit conversation data used
for pretraining, and these domain candidates may
be better suited to empathetic responding than
generic conversation utterances. Thus, we exper-
iment with incorporating ED training candidates
into the pool used at inference time by pretrained
retrieval-based models, with no ﬁne-tuning on ED.
For retrieval-based and generative models, we also
experiment with ﬁne-tuning pretrained models to
predict the next utterance over ED with a con-
text window of four previous utterances, which
is the average length of a conversation in our
dataset. These models are referred to as “Fine-
Tuned” models. This ﬁne-tuning is conducted un-
til convergence for all architectures except those
referred to as “Pretrained”.
4.3
Adding Information from External
Predictors
Many existing models have been pretrained on su-
pervised tasks that may be relevant to empathetic
responding. Combining these models with the rep-
resentations from our base architecture may reap
beneﬁts from previous training time and external
training data without having to redo the work or
requiring access to that data, which may matter to
practitioners. Note that this may considerably aug-
ment the effective capacity of the resulting mod-
els, as well as the total amount of training data
used overall, but our goal here is to get an empiri-
cal sense of how robust performance improvement
is to variations in architecture set-up or supervi-
sion domain. We experiment with adding super-
vised information from two prediction tasks: emo-
tion detection, which is more closely relevant to
our task, and topic detection, which may also be
useful in crafting relevant replies.7
Prepending Top-k Predicted Labels
This set-
up (Fig. 5), PREPEND-1, is a very simple way
to add supervised information to data, requires no
architecture modiﬁcation, and can be used with
black-box classiﬁers.
The top predicted label8
from the supervised classiﬁer is merely prepended
to the beginning of the token sequence as encoder
input, as below:
Original:“I ﬁnally got promoted!”
Prepend-1:“proud I ﬁnally got promoted!”
Similar methods have been used for controlling
the style of generated text (e.g. Niu and Bansal,
2018). Here, we use a fastText model (Joulin et al.,
2017) as prediction architecture. Both the context
and the candidates are run through the classiﬁer
and receive prepended labels. Fine-tuning is con-
ducted similarly as before, but using these modi-
ﬁed inputs. We use two external sources of infor-
mation. To provide emotion signal, we train a clas-
siﬁer to predict the emotion label from the descrip-
tion of the situation written by the Speaker before
the dialogue for the training set dialogues of ED
(EMOPREPEND-1).9 To gauge whether supervi-
sion from a more distant task would still be help-
ful, we also experiment with a classiﬁer trained on
the 20-Newsgroup dataset (Joachims, 1996), for
topic classiﬁcation (TOPICPREPEND-1).
7We considered multitask or feature concatenation set-
ups, but they did not provide consistent improvements. These
experiments are included in Appendix D.2.
8We only discuss prepending the top predicted label here,
but also experimented with top-3 and top-5 models, with sim-
ilar result patterns, shown in Appendix D.3.
9We also experimented with training the classiﬁer on the
utterances themselves, with similar results.

--- Page 7 ---

Retrieval
Retrieval w/ BERT
Generative
Model
Candidate
Source
P@1,100
AVG
BLEU
P@1,100
AVG
BLEU
PPL
AVG
BLEU
Pretrained
R
-
4.10
-
4.26
27.96
5.01
ED
43.25
5.51
49.94
5.97
-
-
Fine-Tuned
ED
56.90
5.88
65.92
6.21
21.24
6.27
ED+DD
-
5.61
-
-
-
-
ED+DD+R
-
4.74
-
-
-
-
EmoPrepend-1
ED
56.31
5.93
66.04
6.20
24.30
4.36
TopicPrepend-1
ED
56.38
6.00
65.96
6.18
25.40
4.17
Table 1: Automatic evaluation metrics on the test set. Pretrained: model pretrained on a dump of 1.7 billion RED-
DIT conversations (4-layer Transformer architecture, except when speciﬁed BERT). Fine-Tuned: model ﬁne-tuned
over the EMPATHETICDIALOGUES training data (Sec. 4.2). EmoPrepend-1, Topic-Prepend1: model incorporating
supervised information from an external classiﬁers, as described in Sec. 4.3. Candidates come from REDDIT (R),
EMPATHETICDIALOGUES (ED), or DAILYDIALOG (DD). P@1,100: precision retrieving the correct test candi-
date out of 100 test candidates. AVG BLEU: average of BLEU-1,-2,-3,-4. PPL: perplexity. All automatic metrics
clearly improve with in-domain training on utterances (Fine-Tuned vs. Pretrained), other metrics are inconsistent.
Bold: best performance for that architecture.
5
Experimental Evaluation
We evaluate the models on their ability to repro-
duce the Listener’s portion of the conversation (i.e.
the ability to react to someone else’s story). We
use both automated metrics and human evaluation
to score each model’s retrievals/generations. Hu-
man evaluation is important, as automated metrics
don’t always correlate with human judgments of
dialogue quality (Liu et al., 2016), but we provide
automated metrics to give a sense of how well they
align with human judgment on this task.
Automated metrics (Table 1)
For both retrieval
and generative systems, we compute BLEU scores
(Papineni et al., 2002) for the model response,
comparing against the gold label (the actual re-
sponse), following the practice of earlier work in
dialogue generation (Wen et al., 2015; Li et al.,
2016a,b). For the generative systems, we addition-
ally report perplexity of the actual gold response.
For the retrieval-based systems, we further com-
pute p@1,100, the accuracy of the model at
choosing the correct response out of a hundred
randomly selected examples in the test set. When
we compute p@1,100, the actual response is in-
cluded in the candidates, unlike inference from the
retrieval systems for all other metrics, which only
uses training utterances as candidates.
Human ratings (Table 2)
We ran crowd-
sourcing tasks on MTurk (further details in
Appendix B). Participants were given a model’s
output for a randomly selected test set example
and asked to score different aspects of the model.
The rating task provides a means of comparing as-
pects of responses, and we ask raters speciﬁcally
about whether the response is acknowledging the
conversation partner’s feelings. We collected at
least 100 ratings per model and asked about three
aspects of performance, all rated on a Likert scale
(1: not at all, 3: somewhat, 5: very much):
Empathy/Sympathy: did the responses show
understanding of the feelings of the person talking
about their experience?
Relevance: did the responses seem appropriate
to the conversation? Were they on-topic?
Fluency: could you understand the responses?
Did the language seem accurate?
5.1
Results
Pretrained models baseline
Pretrained conver-
sation models are rated poorly by humans for em-
pathy when the candidates are retrieved from Red-
dit utterances or when a generative model is used
(Table 2). Higher ratings with models based on
BERT or larger Transformer models show that in-
creasing the capacity makes the models seem more
empathetic, but still remain far from human per-
formance, while being considerably more onerous

--- Page 8 ---

Model
Candidate
Empathy
Relevance
Fluency
Retrieval
Pre-trained
R
2.82 ± 0.12
3.03 ± 0.13
4.14 ± 0.10
R+ED
3.16 ± 0.14
3.35 ± 0.13
4.16 ± 0.11
ED
3.45 ± 0.12
3.55 ± 0.13
4.47 ± 0.08
Fine-tuned
ED
3.76 ± 0.11
3.76 ± 0.12
4.37 ± 0.09
EmoPrepend-1
ED
3.44 ± 0.11
3.70 ± 0.11
4.40 ± 0.08
TopicPrepend-1
ED
3.72 ± 0.12
3.91 ± 0.11
4.57 ± 0.07
Retrieval w/ BERT
Pre-trained
R
3.06 ± 0.13
3.29 ± 0.13
4.20 ± 0.10
R+ED
3.49 ± 0.12
3.62 ± 0.12
4.41 ± 0.09
ED
3.43 ± 0.13
3.49 ± 0.14
4.37 ± 0.10
Fine-tuned
ED
3.71 ± 0.12
3.76 ± 0.12
4.58 ± 0.06
EmoPrepend-1
ED
3.93 ± 0.12
3.96 ± 0.13
4.54 ± 0.09
TopicPrepend-1
ED
4.03 ± 0.10
3.98 ± 0.11
4.65 ± 0.07
Generative
Pre-trained
–
2.31 ± 0.12
2.21 ± 0.11
3.89 ± 0.12
Fine-Tuned
–
3.25 ± 0.12
3.33 ± 0.12
4.30 ± 0.09
EmoPrepend-1
–
3.16 ± 0.12
3.19 ± 0.13
4.36 ± 0.09
TopicPrepend-1
–
3.09 ± 0.13
3.12 ± 0.13
4.41 ± 0.08
Gold Response
–
–
4.19 ± 0.10
4.55 ± 0.07
4.68 ± 0.06
Table 2: Human ratings. Fine-tuning on ED and using ED candidates generally improves scores, especially on Em-
pathy, with minimal retraining. Additional external supervision (Prepend) improves the Empathy and Relevance
scores for BERT-based models. Bold: best score for that group. Italics: reference model for the group.
to train (Table 3).10
Using EMPATHETICDIALOGUES for candidate
selection
Table 1 shows that merely using the
pool of candidates from the training set of ED im-
proves the BLEU scores of retrieval models.
Using candidates from our dataset also substan-
tially improves the performance of pre-trained re-
trieval models on all human metrics, particularly
the Empathy subscore of most interest to us (Ta-
ble 2).
Using
EMPATHETICDIALOGUES
for
ﬁne-
tuning
Additionally,
ﬁne-tuning
to
predict
conversation responses on our data improves all
automated metrics (Table 1).
While ﬁne-tuning
on ED data improves performance on predict-
ing the next ED utterance, this may come at
the expense of performance when predicting
next utterance in other corpora.
To measure
this, we compared automated metrics on next
utterance prediction with pre-trained models and
models ﬁne-tuned using ED data (for our base
and larger retrieval-based Transformer models)
when predicting on DAILYDIALOG and REDDIT
(drawing both context and candidates from the
10Results on larger retrieval-based Transformer models in
Table 9 of the Appendix show the same pattern.
same corpus). Compared to the 12-14% P@1,100
increase measured with ED (see Tables 1 and 7),
ﬁne-tuning on ED leads to a 5-7% increase on
DD, and a 2-3% decrease on R.11 For all three
datasets, ﬁne-tuning increases AVG BLEU by 0.2
to 0.5. The slight decrease of performance on R
is not surprising because the pre-trained model
was trained directly on Reddit predictions. But,
the improvement on DD is an encouraging sign
that improvements from ﬁne-tuning on ED may
generalize to other conversation datasets.
Fine-tuning on the ED data also generally im-
proves human metrics on the ED task, in both re-
trieval and generative set-ups (Table 2).
Augmenting conversation models with exter-
nal pretrained classiﬁers
Automated and hu-
man evaluations suggest that prepending emo-
tion or topic predictions may boost perfomance of
high-capacity models based on BERT (but not the
smaller models), with Empathy ratings close to ap-
proaching human performance.
More extensive experiments with large models
would be required to conﬁrm that larger capacity
makes additional external supervision effective for
this task.
11Numbers for these datasets are included in Table 6 of the
appendix.

--- Page 9 ---

Model
Params, resources, train examples
Emp
Rel
Fluent
Retrieval
Pretrained-R
84.3M, 2.5 days, 8GPUs, 1.7B
2.8
3.0
4.1
Pretrained-ED
same , same, same
3.5
3.6
4.5
Fine-Tuned
same , + 0.5 hour, 1 GPU, +22.3k
3.8
3.8
4.4
Pretrained-Bert-R
217M, 13.5 days, 8GPUs , 1.7B
3.1
3.3
4.2
Pretrained-Bert-ED
same, same, same
3.4
3.5
4.4
Fine-Tuned-Bert
same, +1hour, 8GPUs, +22.3k
3.7
3.8
4.6
Generative
Pretrained
85.1M, 2 days, 32 GPUs, 1.7B
2.3
2.2
3.9
Fine-Tuned
same , +1 hour, 1 GPU, +22.3k
3.3
3.3
4.3
Pretrained-Large
86.2M, 2.5 days, 32 GPUs, 1.7B
2.8
3.0
4.0
Fine-Tuned-Large
same , +0.5 hour, 1 GPU, +22.3k
3.6
3.6
4.5
Table 3: Training resources for different models, with human ratings for empathy (Emp), relevance (Rel) and
ﬂuency (Fluent). Retrieval-based models use reply candidates from the ED training set (ED) or from Reddit (R).
Resource comparisons are relative to the ﬁrst row of each group. Fine-tuning on ED improves all scores (except
for Fluency in one case) while requiring minimal additional training resources. SEM is approximately 0.1
Context
Setup
Model
Cand
Generated Response
Someone came
to my door
with a gun the
other day.
Gen
Pretrained
-
I’m not sure if you’re joking or not.
Gen
Fine-Tuned
-
Oh no! What did you do?
Gen
EmoPrepend
-
Oh no! Did you have a weapon?
Gen
TopicPrepend
-
I’m glad to hear that.
My son failed
his exams! Can
you believe it!
I don’t know
what to do!
Ret-BERT
Pretrained
R
Hopefully his mistakes can help you
know what not to do on the tests.
Ret-BERT
Pretrained
ED
Oh no! I ’ m so sorry! I hope you could
pull your grade up!
Ret-BERT
Fine-Tuned
ED
Oh no! Did he not study?
Ret-BERT
EmoPrepend
ED
Im sorry about that! Did your son start
school already?
Ret-BERT
TopicPrepend
ED
Oh no! Does he have the option of tak-
ing it again?
Table 4: Examples of model responses. Shading is provided for better legibility.
Resources and capacity
Table 3 quantiﬁes re-
source and parameter usage for several models and
set-ups, including
a larger Transformer generative model (5 layers
instead of 4) and BERT-based architectures with
substantially more parameters that require longer
training. Using ED candidates in pretrained re-
trieval models, or ﬁne-tuning pretrained conversa-
tion models on ED data makes smaller models per-
form better than larger ones with minimal increase
in resource usage.
6
Conclusion
We introduce a new dataset of 25k dialogues
grounded in situations prompted by speciﬁc emo-
tion labels. Our experiments show that using this
dataset to provide retrieval candidates or ﬁne-tune
conversation models leads to responses that are
evaluated as more empathetic. how to integrate
empathetic responding into more general dialogue
when, for example, the needs for empathy have
to be balanced with staying on topic or provid-
ing information.
We hope that our results and
dataset will stimulate more research in the impor-
tant direction of making dialog systems more em-
pathetic.
Acknowledgments
We thank the anonymous reviewers for insightful
feedback and suggestions. This material is based,

--- Page 10 ---

in part, upon work supported by the National Sci-
ence Foundation Graduate Research Fellowship
Program under Grant No. DGE-1256082.
References
Katie Elson Anderson. 2015. Ask me anything: what
is reddit? Library Hi Tech News, 32(5):8–11.
Nabiha Asghar, Pascal Poupart, Jesse Hoey, Xin Jiang,
and Lili Mou. 2018. Affective neural response gen-
eration.
In European Conference on Information
Retrieval, pages 154–166. Springer.
Natalya N Bazarova, Yoon Hyung Choi, Victoria
Schwanda Sosik, Dan Cosley, and Janis Whitlock.
2015.
Social sharing of emotions on facebook:
Channel differences, satisfaction, and replies.
In
Proceedings of the 18th ACM conference on com-
puter supported cooperative work & social comput-
ing, pages 154–164. ACM.
Timothy Bickmore and Justine Cassell. 2001.
Rela-
tional agents: a model and implementation of build-
ing user trust. In Proceedings of the SIGCHI confer-
ence on Human factors in computing systems, pages
396–403. ACM.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2018.
BERT: pre-training of
deep bidirectional transformers for language under-
standing. CoRR, abs/1810.04805.
Emily Dinan,
Varvara Logacheva,
Valentin Ma-
lykh, Alexander Miller, Kurt Shuster, Jack Ur-
banek, Douwe Kiela, Arthur Szlam, Iulian Serban,
Ryan Lowe, Shrimai Prabhumoye, Alan W Black,
Alexander Rudnicky, Jason Williams, Joelle Pineau,
Mikhail Burtsev, and Jason Weston. 2019. The sec-
ond conversational intelligence challenge (convai2).
arXiv preprint arXiv:1902.00098.
Venkatesh Duppada, Royal Jain, and Sushant Hiray.
2018.
Seernet at semeval-2018 task 1: Domain
adaptation for affect in tweets. In Proceedings of
The 12th International Workshop on Semantic Eval-
uation, pages 18–23.
Paul Ekman. 1992. An argument for basic emotions.
Cognition & emotion, 6(3-4):169–200.
Bjarke Felbo, Alan Mislove, Anders Søgaard, Iyad
Rahwan, and Sune Lehmann. 2017. Using millions
of emoji occurrences to learn any-domain represen-
tations for detecting sentiment, emotion and sar-
casm.
In Proceedings of the 2017 Conference on
Empirical Methods in Natural Language Process-
ing, pages 1615–1625.
Jamie Fraser, Ioannis Papaioannou, and Oliver Lemon.
2018.
Spoken conversational ai in video games:
Emotional dialogue management increases user en-
gagement. In Proceedings of the 18th International
Conference on Intelligent Virtual Agents, pages
179–184. ACM.
Erving Goffman. 1959. The presentation of self in ev-
eryday life.
Erving Goffman. 1981. Forms of talk. University of
Pennsylvania Press.
Edouard Grave, Piotr Bojanowski, Prakhar Gupta, Ar-
mand Joulin, and Tomas Mikolov. 2018. Learning
word vectors for 157 languages. In Proceedings of
the Eleventh International Conference on Language
Resources and Evaluation (LREC-2018).
Umang Gupta, Ankush Chatterjee, Radhakrishnan
Srikanth, and Puneet Agrawal. 2017. A sentiment-
and-semantics-based approach for emotion detec-
tion in textual conversations.
arXiv preprint
arXiv:1707.06996.
John Heritage. 2005. Conversation analysis and insti-
tutional talk. Handbook of language and social in-
teraction, 103:47.
Zhiting Hu, Zichao Yang, Xiaodan Liang, Ruslan
Salakhutdinov, and Eric P Xing. 2017. Toward con-
trolled generation of text. In Proceedings of the 34th
International Conference on Machine Learning-
Volume 70, pages 1587–1596. JMLR. org.
Chenyang Huang, Osmar Zaiane, Amine Trabelsi, and
Nouha Dziri. 2018.
Automatic dialogue genera-
tion with expressed emotions. In Proceedings of the
2018 Conference of the North American Chapter of
the Association for Computational Linguistics: Hu-
man Language Technologies, Volume 2 (Short Pa-
pers), volume 2, pages 49–54.
Bernd Huber, Daniel McDuff, Chris Brockett, Michel
Galley, and Bill Dolan. 2018. Emotional dialogue
generation using image-grounded language models.
In Proceedings of the 2018 CHI Conference on
Human Factors in Computing Systems, page 277.
ACM.
Thorsten Joachims. 1996. A probabilistic analysis of
the rocchio algorithm with tﬁdf for text categoriza-
tion. Technical report, Carnegie-mellon univ pitts-
burgh pa dept of computer science.
Armand Joulin, Edouard Grave, Piotr Bojanowski, and
Tomas Mikolov. 2017.
Bag of tricks for efﬁcient
text classiﬁcation. In Proceedings of the 15th Con-
ference of the European Chapter of the Association
for Computational Linguistics: Volume 2, Short Pa-
pers, volume 2, pages 427–431.
Sung Soo Kim, Stan Kaplowitz, and Mark V John-
ston. 2004.
The effects of physician empathy on
patient satisfaction and compliance. Evaluation &
the health professions, 27(3):237–251.
Min Kyung Lee, Sara Kiesler, and Jodi Forlizzi. 2010.
Receptionist or information kiosk: how do people
talk with a robot?
In Proceedings of the 2010
ACM conference on Computer supported coopera-
tive work, pages 31–40. ACM.

--- Page 11 ---

Wendy Levinson, Rita Gorawara-Bhat, and Jennifer
Lamb. 2000.
A study of patient clues and physi-
cian responses in primary care and surgical settings.
Jama, 284(8):1021–1027.
Jiwei Li, Michel Galley, Chris Brockett, Jianfeng Gao,
and Bill Dolan. 2016a. A diversity-promoting ob-
jective function for neural conversation models. In
Proceedings of the 2016 Conference of the North
American Chapter of the Association for Computa-
tional Linguistics: Human Language Technologies,
pages 110–119.
Jiwei Li, Michel Galley, Chris Brockett, Georgios Sp-
ithourakis, Jianfeng Gao, and Bill Dolan. 2016b. A
persona-based neural conversation model. In Pro-
ceedings of the 54th Annual Meeting of the Associa-
tion for Computational Linguistics (Volume 1: Long
Papers), volume 1, pages 994–1003.
Yanran Li, Hui Su, Xiaoyu Shen, Wenjie Li, Ziqiang
Cao, and Shuzi Niu. 2017. Dailydialog: A manually
labelled multi-turn dialogue dataset. In Proceedings
of the Eighth International Joint Conference on Nat-
ural Language Processing (Volume 1: Long Papers),
volume 1, pages 986–995.
Eden Litt, Erin Spottswood, Jeremy Birnholtz, Jeff T
Hancock, Madeline E Smith, and Lindsay Reynolds.
2014. Awkward encounters of an other kind: collec-
tive self-presentation and face threat on facebook. In
Proceedings of the 17th ACM conference on Com-
puter supported cooperative work & social comput-
ing, pages 449–460. ACM.
Chia-Wei Liu, Ryan Lowe, Iulian Serban, Mike Nose-
worthy, Laurent Charlin, and Joelle Pineau. 2016.
How not to evaluate your dialogue system: An em-
pirical study of unsupervised evaluation metrics for
dialogue response generation. In Proceedings of the
2016 Conference on Empirical Methods in Natural
Language Processing, pages 2122–2132.
Xiaodong Liu, Pengcheng He, Weizhu Chen, and Jian-
feng Gao. 2019. Multi-task deep neural networks
for natural language understanding. arXiv preprint
arXiv:1901.11504.
Ryan Lowe, Iulian V Serban, Mike Noseworthy, Lau-
rent Charlin, and Joelle Pineau. 2016. On the eval-
uation of dialogue systems with next utterance clas-
siﬁcation. In 17th Annual Meeting of the Special In-
terest Group on Discourse and Dialogue, page 264.
Minh-Thang Luong, Quoc V Le, Ilya Sutskever, Oriol
Vinyals, and Lukasz Kaiser. 2016.
Multi-task se-
quence to sequence learning.
In Proceedings of
ICLR.
Pierre-Emmanuel Mazare, Samuel Humeau, Martin
Raison, and Antoine Bordes. 2018. Training mil-
lions of personalized dialogue agents. In Proceed-
ings of the 2018 Conference on Empirical Methods
in Natural Language Processing, pages 2775–2779.
Alexander Miller, Will Feng, Dhruv Batra, Antoine
Bordes, Adam Fisch, Jiasen Lu, Devi Parikh, and
Jason Weston. 2017. Parlai: A dialog research soft-
ware platform.
In Proceedings of the 2017 Con-
ference on Empirical Methods in Natural Language
Processing: System Demonstrations, pages 79–84.
Saif Mohammad, Felipe Bravo-Marquez, Mohammad
Salameh, and Svetlana Kiritchenko. 2018. Semeval-
2018 task 1: Affect in tweets. In SemEval@NAACL-
HLT.
Saif M. Mohammad. 2012. #emotional tweets. In Pro-
ceedings of the First Joint Conference on Lexical
and Computational Semantics - Volume 1: Proceed-
ings of the Main Conference and the Shared Task,
and Volume 2: Proceedings of the Sixth Interna-
tional Workshop on Semantic Evaluation, SemEval
’12, pages 246–255, Stroudsburg, PA, USA. Associ-
ation for Computational Linguistics.
Tong Niu and Mohit Bansal. 2018. Polite dialogue gen-
eration without parallel data. Transactions of the As-
sociation for Computational Linguistics, 6:373–389.
Kishore Papineni, Salim Roukos, Todd Ward, and Wei-
Jing Zhu. 2002. Bleu: a method for automatic eval-
uation of machine translation.
In Proceedings of
the 40th annual meeting on association for compu-
tational linguistics, pages 311–318. Association for
Computational Linguistics.
Ji Ho Park, Peng Xu, and Pascale Fung. 2018.
Plusemo2vec at semeval-2018 task 1: Exploiting
emotion knowledge from emoji and #hashtags. In
Proceedings of The 12th International Workshop on
Semantic Evaluation, pages 264–272.
Robert Plutchik. 1984.
Emotions: A general psy-
choevolutionary theory.
Approaches to emotion,
1984:197–219.
Alec Radford, Jeff Wu, Rewon Child, David Luan,
Dario Amodei, and Ilya Sutskever. 2019. Language
models are unsupervised multitask learners.
Byron Reeves and Clifford Ivar Nass. 1996. The media
equation: How people treat computers, television,
and new media like real people and places. Cam-
bridge university press.
Alan Ritter, Colin Cherry, and Bill Dolan. 2010. Un-
supervised modeling of twitter conversations.
In
Human Language Technologies: The 2010 Annual
Conference of the North American Chapter of the
Association for Computational Linguistics, pages
172–180. Association for Computational Linguis-
tics.
Klaus R. Scherer and Harald G. Wallbott. 1994. Evi-
dence for universality and cultural variation of dif-
ferential emotion response patterning.
Journal of
personality and social psychology, 66 2:310–28.
Amy Skerry and Rebecca Saxe. 2015. Neural repre-
sentations of emotion are organized around abstract
event features. Current Biology, 25:1945–1954.

--- Page 12 ---

Carlo Strapparava and Rada Mihalcea. 2007. Semeval-
2007 task 14: Affective text. In SemEval@ACL.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob
Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz
Kaiser, and Illia Polosukhin. 2017. Attention is all
you need. In Advances in Neural Information Pro-
cessing Systems, pages 5998–6008.
Ashwin K. Vijayakumar, Michael Cogswell, Ram-
prasaath R. Selvaraju,
Qing Sun,
Stefan Lee,
David J. Crandall, and Dhruv Batra. 2016. Diverse
beam search: Decoding diverse solutions from neu-
ral sequence models. CoRR, abs/1610.02424.
Ke Wang and Xiaojun Wan. 2018. Sentigan: gener-
ating sentimental texts via mixture adversarial net-
works.
In Proceedings of the 27th International
Joint Conference on Artiﬁcial Intelligence, pages
4446–4452. AAAI Press.
Tsung-Hsien Wen, Milica Gasic, Nikola Mrkˇsi´c, Pei-
Hao Su, David Vandyke, and Steve Young. 2015.
Semantically conditioned lstm-based natural lan-
guage generation for spoken dialogue systems. In
Proceedings of the 2015 Conference on Empirical
Methods in Natural Language Processing, pages
1711–1721.
Kathryn R Wentzel. 1997. Student motivation in mid-
dle school: The role of perceived pedagogical car-
ing. Journal of educational psychology, 89(3):411.
Peng Xu, Andrea Madotto, Chien-Sheng Wu, Ji Ho
Park, and Pascale Fung. 2018.
Emo2vec: Learn-
ing generalized emotion representation by multi-
task training. In Proceedings of the 9th Workshop
on Computational Approaches to Subjectivity, Senti-
ment and Social Media Analysis, pages 292–298.
Yinfei Yang, Steve Yuan, Daniel Cer, Sheng yi Kong,
Noah Constant, Petr Pilar, Heming Ge, Yun-Hsuan
Sung, Brian Strope, and Ray Kurzweil. 2018.
Learning semantic textual similarity from conversa-
tions. In Rep4NLP@ACL.
Saizheng Zhang, Emily Dinan, Jack Urbanek, Arthur
Szlam, Douwe Kiela, and Jason Weston. 2018. Per-
sonalizing dialogue agents: I have a dog, do you
have pets too?
In Proceedings of the 56th Annual
Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), volume 1, pages
2204–2213.
Hao Zhou, Minlie Huang, Tianyang Zhang, Xiaoyan
Zhu, and Bing Liu. 2018. Emotional chatting ma-
chine: Emotional conversation generation with in-
ternal and external memory. In Thirty-Second AAAI
Conference on Artiﬁcial Intelligence.
Xianda Zhou and William Yang Wang. 2018. Mojitalk:
Generating emotional responses at scale.
In Pro-
ceedings of the 56th Annual Meeting of the Associa-
tion for Computational Linguistics (Volume 1: Long
Papers), volume 1, pages 1128–1137.

--- Page 13 ---

A
Data Examples
We include ten randomly selected dialogues from
our training set in Table 5.
B
Human Evaluation Crowdsourcing
Task
Human evaluations were collected on MTurk. For
the rating task, each worker was shown a set of 10
randomly subsampled examples from the test set,
one after another, each from a different randomly
selected model. The worker had to rate the empa-
thy, relevance, and ﬂuency of each example before
moving onto the next one. At least 100 ratings
were collected per model. 221 US workers partic-
ipated in the rating task, and each had to perform
a minimum of one set of 10 ratings.
C
Next utterance prediction on other
datasets
We test how ﬁne-tuning on ED data affects
next utterance prediction on two external datasets
(REDDIT and DAILYDIALOG).
In this experi-
ment, we use both candidates and context from the
DD or R data. Results in Table 6 show that per-
formance on DAILYDIALOG improves after ﬁne-
tuning on our data.
D
Additional Experimental Details and
Results
D.1
Training Details
We used Adamax for training throughout, and
dropout was set to 0% everywhere except for a
20% dropout in the linear layer of the emotion-
label term of the MULTITASK objective function
(discussed below). A learning rate of 8e−4 was
used for all four-layer Transformer models, fol-
lowing Mazare et al. (2018). For the ﬁve-layer
retrieval-based Transformer model (Pretrained-
Large and Fine-Tuned-Large), the learning rate
was selected by picking the best performing over
the validation set, among values randomly sam-
pled between between 5e−5 and 8e−4.
When
training the retrieval-based BERT model on Red-
dit and ED data, the learning rate was selected by
picking the best performing over the validation set,
among values randomly sampled between 6e−6
and 2e−4. For training BERT models on Reddit
data, we also experimented with adding an addi-
tional Transformer layer after the output embed-
ding of the BERT model, but this slightly degraded
P@1,100 scores on the validation set. We used a
learning rate of 8e−5 for the ﬁve-layer generative
Transformer models.
D.2
Additional Experimental Set-Ups
We investigated a few additional approaches for
incorporating supervised emotion or topic predic-
tion in generating dialogue, but observed little per-
formance improvement.
Methods are described
below.
Multitask with Emotion labels
If the most ap-
propriate response depends on some information
for which supervision is available, e.g., the emo-
tions at play, nudging the model to encode this in-
formation could result in better performance. We
experimented with this by training the base ar-
chitecture in the one-to-many style of multi-task
learning that has been used for NLP seq2seq set-
tings (Luong et al., 2016). In this set-up, MULTI-
TASK, we altered the objective function to also op-
timize for predicting the emotion label of the con-
versation to which the utterances being encoded
belonged. We added to the context encoder a lin-
ear layer and softmax that predicted the emotion
label from the context sentences. The objective
function was altered to be the average of the nega-
tive log-likelihood of predicting the next utterance
¯y and the negative log-likelihood of the added lin-
ear layer being able to predict the correct emotion.
Prepend-3, Prepend-5
We investigated whether
Prepend models could be improved by adding the
top-3/5 predicted emotion or topic labels by the
classiﬁer (rather than top-1).
Ensemble of Encoders
We also investigated an-
other approach for incorporating external predic-
tors, which we report the results of in our ex-
tended results tables.
In this set-up (ENSEM),
we augmented the encoders to incorporate latent
representations from pretrained supervised archi-
tectures.
We replaced each of the encoders in
our Transformer networks with an Ensemble en-
coder , similar to a many-to-one style encoder-
decoder architecture (Luong et al., 2016). This en-
coder took the encoding hw from our basic Trans-
former encoder (either hx or hy), already trained
on our data, and concatenated it with the repre-
sentation hc extracted from the inner layer of a
classiﬁcation network. We used the penultimate
layer of a deep emotion classiﬁer. The concate-
nated encodings were projected linearly to the di-

--- Page 14 ---

Label: Content
Situation: Speaker felt this when...
“eating my favorite meal makes me happy.”
Conversation:
Speaker: i am at my best when i have my favorite
meal.
Listener: nice
Speaker: i love enchiladas
Listener: really?
Speaker: yes. enchiladas for the win!
Label: Proud
Situation: Speaker felt this when...
“I was proud when my brother ﬁnished college. He
worked so hard at it”
Conversation:
Speaker: I was proud of my brother when he ﬁnished
school. He worked so hard at it
Listener: Nice, tell him congrats. What did he major
in?
Speaker: It was English
Listener: He should become an English teacher1
Label: Joyful
Situation: Speaker felt this when...
“I have had a great week!”
Conversation:
Speaker: I have had a great start to my week!
Listener: That’s great. Do you think the rest of the
week will be as great?
Speaker: I hope so! It looks promising!!
Listener: Lucky you. Are you always a positive per-
son or it’s just been an amazing week really?
Speaker: haha. Kind of both. And also probably too
much coffee to start my shift tonight
Label: Terriﬁed
Situation: Speaker felt this when...
“I got home for lunch and found a bat outside on my
front porch.”
Conversation:
Speaker: I got home for lunch and found a bat out-
side on my front porch. It probably has rabies. Bats
shouldn’t be out during the day.
Listener: Doesn’t rabies cause sensativity to light?
Either way I would freak out...
Speaker: It can but, it also causes anmails to behave
erratically... like bats wadering around in the middle
of the day.
Listener: Oh yeah, gotcha. I really don’t like animals
that are small and move quickly
Speaker: Generally yes.
Label: Anticipating
Situation: Speaker felt this when...
“I cant wait to go on my end of summer trip”
Conversation:
Speaker: I cant wait to go on my end of summer trip
in texas.
Listener: Sounds like fun. What you got planned ?
Speaker: not really sure but im excited to just be
invited
Listener: Got any family out there? Cousins perhaps
Label: Terriﬁed
Situation: Speaker felt this when...
“My brother jump scared me while I was out playing. It was crazy
bad.”
Conversation:
Speaker: Just got scared to death.
Listener: Oh no. What happened?
Speaker: My brother jumped scared me.
Listener: lol is he younger or older?
Label: Proud
Situation: Speaker felt this when...
“My little dog learned to sit!”
Conversation:
Speaker: I ﬁnally tough my new little puppy his ﬁrst trick!
Listener: What trick did you teach him?
Speaker: I tought him to sit for a treat, its so cute.
Listener: That is good, do you plan to teach him more tricks?
Label: Apprehensive
Situation: Speaker felt this when...
“I have to call my landlord about being late on the rent. I really
don’t want to have this conversation.”
Conversation:
Speaker: I have to make a dreadful phone call tomorrow
Listener: Oh no, about what?
Speaker: I’m late on my rent and I need another week. I don’t
want to because my landlord isnt very nice
Listener: Oh no, I’ve been there done that too many times.
Speaker: I don’t want her to make a big deal
Label: Conﬁdent
Situation: Speaker felt this when...
“When my husband asked me about how to build a chicken coop
I was able to give him a reply that was backed up by blueprints
and research from the internet. ”
Conversation:
Speaker: We recently got 9 chicks and we’ve been having to work
on making them a coop! I had to do so much research but I think
we ﬁnally have a place that they’ll enjoy living when they aren’t
able to free range.
Listener: OHH! I Love chickens ! I have always wanted some. I
have a duck! lol- What kind of chickens are they?
Speaker: We currently have 2 Australorps, 3 Rhode Island Reds,
3 Barred Plymouth Rocks, and 1 Welsummer, but 4 of the 9 ended
up being roosters. Ugh!
Listener: Oh man! They ﬁght sometimes. I hope they aren’t too
bad about waking you up in the morning. Chickens can be very
sweet though!
Speaker: I love my little hens, especially one I’ve named Curly.
The roosters might get replaced by hens though because the crow-
ing is so frustrating!
Label: Surprised
Situation: Speaker felt this when...
“I got a lottery ticket while I was at work today. I won $100 on
the scratch off. I was shocked. I never win.”
Conversation:
Speaker: I won $100 on a scratch off today. I was shocked. I
never win.
Listener: Wow! How often do you play the lottery?
Speaker: I usually go on our Tuesday break to buy one with
coworkers.
Listener: Neat! Well that is a fantastic feat. Maybe you can win
again sometime?
Table 5: 10 random examples from EMPATHETICDIALOGUES training set.

--- Page 15 ---

P @1,100
BLEU
Model
DD
R
DD
R
Pretrained
39.04
58.95
6.65
1.43
Fine-Tuned
44.58
56.25
7.14
1.64
Pretrained-Large
42.28
61.60
6.94
1.42
Fine-Tuned-Large
48.96
58.71
7.42
1.73
Table 6: Performance of the retrieval-based pretrained
model and retrieval-based models ﬁne-tuned on ED
data for next utterance prediction in other datasets,
with both context and candidates from the same dataset
(R=Reddit, DD=DailyDialog).
mension required by the decoder, whose architec-
ture didn’t change. When training the dialogue
model, we froze both the base Transformer en-
coder and the pretrained classiﬁer and trained only
the linear layers (and the decoder for generative
systems).
We used emotion-related supervision
from Emojis from Twitter, through the use of
the trained Deepmoji system (Felbo et al., 2017)
released by the authors, either as-is (ENSEM-
DM) or ﬁne-tuned on the situation descriptions of
EMPATHETICDIALOGUES (ENSEM-DM+).
D.3
Additional Experiments Results
Automated and human evaluations for any addi-
tional experiments are in Tables 7 and 8, respec-
tively.
All of these model variations show im-
provements over the pre-trained models. In some
metrics, many of these models show slight im-
provements over the ﬁne-tuned models, as well,
though not as consistently, except for the larger
BERT retrieval-based models. While prepending
top-1 or top-3 labels do not improve generative
model scores, the results in Table 8 suggest that
multitask, prepend-5, and ensemble set-ups may
improve the human evaluations of the ﬁne-tuned
generative model for empathy, but are too incon-
sistent to be conclusive without more corroborat-
ing experiments.
D.4
Emotion Classiﬁcation Results
Our dataset can also be used to train or ﬁne-tune
an emotion classiﬁer, as we do in our PREPEND-
K and ENSEM-DM+ set-ups.
To give a sense
of where the difﬁculty falls compared to existing
emotion and sentiment classiﬁcation benchmarks,
we reproduce the table from Felbo et al. (2017)
and add results when ﬁne-tuning the Deepmoji
model on our dataset, or using a fastText classiﬁer
(Table 10).

--- Page 16 ---

Retrieval
Retrieval w/ BERT
Generative
Model
Candidate
Source
P@1,100
AVG
BLEU
P@1,100
AVG
BLEU
PPL
AVG
BLEU
Pretrained
R
-
4.10
-
4.26
27.96
5.01
R+ED
-
4.96
-
5.62
-
-
ED
43.25
5.51
49.94
5.97
-
-
Fine-Tuned
R
-
3.85
-
4.14
-
-
R+ED
-
4.76
-
5.39
-
-
ED
56.90
5.88
65.92
6.21
21.24
6.27
ED+DD
-
5.61
-
-
-
-
ED+DD+R
-
4.74
-
-
-
-
Pretrained-Large
R
-
4.16
-
-
-
-
ED
47.58
5.78
-
-
23.64
6.31
Fine-Tuned-Large
ED
60.44
6.01
-
-
16.55
8.06
Multitask
ED
55.73
6.18
65.90
6.17
24.07
5.42
EmoPrepend-1
ED
56.31
5.93
66.04
6.20
24.30
4.36
EmoPrepend-3
ED
55.75
6.23
65.85
6.14
23.96
2.69
EmoPrepend-5
ED
56.35
6.18
64.69
6.21
25.40
5.56
TopicPrepend-1
ED
56.38
6.00
65.96
6.18
25.40
4.17
TopicPrepend-3
ED
55.44
5.97
65.85
6.25
25.02
3.13
TopicPrepend-5
ED
55.75
6.17
65.65
6.19
25.10
6.20
Ensem-DM
ED
52.71
6.03
-
-
19.05
6.83
Ensem-DM+
ED
52.35
6.04
-
-
19.10
6.77
Table 7:
Automatic evaluation metrics on the test set for full set of experimental setups. Pretrained: basic
Transformer model pretrained on a dump of 1.7 billion REDDIT conversations. Fine-Tuned: model ﬁne-tuned
over the EMPATHETICDIALOGUES training data. Multitask: model trained with multitask loss function (pre-
dicting the emotion label). EmoPrepend-1/3/5, TopicPrepend-1/3/5: model using top-k labels outputted by an
external classiﬁer as prepended tokens. Ensem: model incorporating external classiﬁers by concatenating repre-
sentations from deepmoji with the ﬁne-tuned transformer representation. Candidates come from REDDIT (R) or
EMPATHETICDIALOGUES (ED). P@1,100: precision retrieving the correct test candidate out of 100 test candi-
dates. AVG BLEU: average of BLEU-1,-2,-3,-4. PPL: perplexity. Bold: best performance in that column.

--- Page 17 ---

Model
Candidate
Empathy
Relevance
Fluency
Retrieval
Pretrained
R
2.82 ± 0.12
3.03 ± 0.13
4.14 ± 0.10
R+ED
3.16 ± 0.14
3.35 ± 0.13
4.16 ± 0.11
ED
3.45 ± 0.12
3.55 ± 0.13
4.47 ± 0.08
Fine-Tuned
R
2.51 ± 0.12
2.90 ± 0.12
4.04 ± 0.11
R+ED
3.06 ± 0.14
3.34 ± 0.13
4.12 ± 0.11
ED
3.76 ± 0.11
3.76 ± 0.12
4.37 ± 0.09
Multitask
ED
3.63 ± 0.12
3.83 ± 0.12
4.49 ± 0.08
EmoPrepend-1
ED
3.44 ± 0.11
3.70 ± 0.11
4.40 ± 0.08
EmoPrepend-3
ED
3.54 ± 0.11
3.76 ± 0.11
4.54 ± 0.07
EmoPrepend-5
ED
3.42 ± 0.11
3.61 ± 0.11
4.53 ± 0.07
TopicPrepend-1
ED
3.72 ± 0.12
3.91 ± 0.11
4.57 ± 0.07
TopicPrepend-3
ED
3.64 ± 0.11
3.66 ± 0.12
4.51 ± 0.08
TopicPrepend-5
ED
3.34 ± 0.12
3.52 ± 0.12
4.24 ± 0.09
Ensem-DM
ED
3.61 ± 0.11
3.71 ± 0.12
4.45 ± 0.08
Pretrained-Large
R
2.94 ± 0.14
3.12 ± 0.14
4.23 ± 0.10
ED
3.47 ± 0.14
3.56 ± 0.13
4.41 ± 0.10
Fine-Tuned-Large
ED
3.81 ± 0.12
3.90 ± 0.12
4.56 ± 0.08
Retrieval w/ BERT
Pretrained
R
3.06 ± 0.13
3.29 ± 0.13
4.20 ± 0.10
R+ED
3.49 ± 0.12
3.62 ± 0.12
4.41 ± 0.09
ED
3.43 ± 0.13
3.49 ± 0.14
4.37 ± 0.10
Fine-Tuned
R
2.90 ± 0.13
3.39 ± 0.13
4.36 ± 0.09
R+ED
3.46 ± 0.13
3.90 ± 0.12
4.46 ± 0.08
ED
3.71 ± 0.12
3.76 ± 0.12
4.58 ± 0.06
Multitask
ED
3.80 ± 0.12
3.97 ± 0.11
4.63 ± 0.07
EmoPrepend-1
ED
3.93 ± 0.12
3.96 ± 0.13
4.54 ± 0.09
EmoPrepend-3
ED
3.73 ± 0.13
3.88 ± 0.14
4.60 ± 0.09
EmoPrepend-5
ED
4.08 ± 0.10
4.10 ± 0.11
4.67 ± 0.07
TopicPrepend-1
ED
4.03 ± 0.10
3.98 ± 0.11
4.65 ± 0.07
TopicPrepend-3
ED
3.73 ± 0.12
3.84 ± 0.13
4.52 ± 0.08
TopicPrepend-5
ED
3.72 ± 0.12
3.80 ± 0.12
4.46 ± 0.09
Generative
Pretrained
-
2.31 ± 0.12
2.21 ± 0.11
3.89 ± 0.12
Fine-Tuned
-
3.25 ± 0.12
3.33 ± 0.12
4.30 ± 0.09
Multitask
-
3.36 ± 0.13
3.34 ± 0.13
4.21 ± 0.10
EmoPrepend-1
-
3.16 ± 0.12
3.19 ± 0.13
4.36 ± 0.09
EmoPrepend-3
-
3.09 ± 0.13
3.02 ± 0.13
4.39 ± 0.09
EmoPrepend-5
-
3.32 ± 0.12
3.23 ± 0.12
4.35 ± 0.09
TopicPrepend-1
-
3.09 ± 0.13
3.12 ± 0.13
4.41 ± 0.08
TopicPrepend-3
-
3.09 ± 0.12
3.34 ± 0.13
4.53 ± 0.08
TopicPrepend-5
-
3.46 ± 0.13
3.68 ± 0.13
4.60 ± 0.08
Ensem-DM
-
3.42 ± 0.12
3.45 ± 0.12
4.67 ± 0.06
Pretrained-Large
-
2.84 ± 0.13
2.97 ± 0.12
4.01 ± 0.11
Fine-Tuned-Large
-
3.61 ± 0.13
3.62 ± 0.13
4.46 ± 0.10
Gold Response
–
–
4.19 ± 0.10
4.55 ± 0.07
4.68 ± 0.06
Table 8: Human evaluation metrics from rating task for additional experiments.

--- Page 18 ---

Model
Params, resources, train examples
Emp
Rel
Fluent
Retrieval
Pretrained-R
84.3M, 2.5 days, 8 GPUs, 1.7B
2.8
3.0
4.1
Pretrained-ED
same , same, +22.3k
3.5
3.6
4.5
Fine-Tuned
same , + 0.5 hour, 1 GPU, +22.3k
3.8
3.8
4.4
Multitask
+9.6k, + 0.5 hour, 1 GPU, +22.3k
3.6
3.6
4.5
Pretrained-Large-R
86.5M, 10.5 days, 8 GPUs , 1.7B
2.9
3.1
4.2
Pretrained-Large-ED
same, same, +22.3k
3.5
3.6
4.4
Fine-Tuned-Large
same, +1 hour, 1GPU, +22.3k
3.8
3.9
4.6
Pretrained-BERT-R
217M, 13.5 days, 8 GPUs , 1.7B
3.1
3.3
4.2
Pretrained-BERT-ED
same, same, +22.3k
3.4
3.5
4.4
Fine-Tuned-BERT
same, +1 hour, 8 GPUs, +22.3k
3.7
3.8
4.6
Multitask-BERT
+9.6k, +0.5 hour, 8 GPUs, +22.3k
3.8
4.0
4.6
Generative
Pretrained
85.1M, 2 days, 32 GPUs, 1.7B
2.3
2.2
3.9
Fine-Tuned
same , +1 hour, 1 GPU, +22.3k
3.3
3.3
4.3
Multitask
+9.6k, +1 hour, 1 GPU, +22.3k
3.2
3.2
4.3
Pretrained-Large
86.2M, 2.5 days, 32 GPUs, 1.7B
2.8
3.0
4.0
Fine-Tuned-Large
same , +0.5 hour, 1 GPU, +22.3k
3.6
3.6
4.5
Table 9: Training resources for different models, with human ratings for empathy (Emp), relevance (Rel) and
ﬂuency (Fluent) for full set of experiments. Retrieval-based models use reply candidates from the ED training set
(ED) or from Reddit (R). Resource comparisons are relative to the ﬁrst row of each group. Fine-tuning on ED
improves all scores (except for Fluency in one case) while requiring minimal additional training resources. SEM
is approximately 0.1
Dataset
Metric
SOTA
(in 2017)
fastText
DeepMoji
new
DeepMoji
full
DeepMoji
last
DeepMoji
chain-thaw
SE0714
F1
0.34
0.16
0.21
0.31
0.36
0.37
OLYMPIC
F1
0.50
0.38
0.43
0.50
0.61
0.61
PSYCHEXP
F1
0.45
0.44
0.32
0.42
0.56
0.57
SS-TWITTER
Acc
0.82
0.68
0.62
0.85
0.87
0.88
SS-YOUTUBE
Acc
0.86
0.75
0.75
0.88
0.92
0.93
SE0614
Acc
0.51
-
0.51
0.54
0.58
0.58
SCV1
F1
0.63
0.60
0.67
0.65
0.68
0.69
SCV2-GEN
F1
0.72
0.69
0.71
0.71
0.74
0.75
ED
Acc
-
0.43
0.40
0.46
0.46
0.48
ED-CUT
Acc
-
0.41
0.36
0.42
0.44
0.45
Table 10: Classiﬁcation performance on EMPATHETICDIALOGUES, with the benchmarks proposed in (Felbo et al.,
2017) for reference. ED: performance on predicting the emotion label from the situation description. ED-CUT:
same, but after having removed all the situation descriptions where the target label was present.

```
