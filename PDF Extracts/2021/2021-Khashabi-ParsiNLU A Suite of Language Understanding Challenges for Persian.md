---
title: "2021-Khashabi-ParsiNLU A Suite of Language Understanding Challenges for Persian - PDF Extract"
source_pdf: "2021-Khashabi-ParsiNLU A Suite of Language Understanding Challenges for Persian.pdf"
pages: 15
extracted_at: "2026-02-13T10:43:49.802047"
---

# PDF Extract: 2021-Khashabi-ParsiNLU A Suite of Language Understanding Challenges for Persian

**Source PDF:** 2021-Khashabi-ParsiNLU A Suite of Language Understanding Challenges for Persian.pdf
**Total Pages:** 15

---

## Content

```
--- Page 1 ---

TACL’21
PARSINLU:
A Suite of Language Understanding Challenges for Persian
Daniel Khashabi1 Arman Cohan1 Siamak Shakeri2 Pedram Hosseini3 Pouya Pezeshkpour4
Malihe Alikhani5
Moin Aminnaseri6
Marzieh Bitaab7
Faeze Brahman8
Sarik Ghazarian9
Mozhdeh Gheini9
Arman Kabiri10
Rabeeh Karimi Mahabadi11
Omid Memarrast12
Ahmadreza Mosallanezhad7
Erfan Noury13
Shahab Raji14
Mohammad Sadegh Rasooli15 Sepideh Sadeghi2 Erfan Sadeqi Azer2 Niloofar SaﬁSamghabadi16
Mahsa Shafaei17
Saber Sheybani18
Ali Tazarv4
Yadollah Yaghoobzadeh19
1Allen Institute for AI, 2Google, 3George Washington U., 4UC Irvine, 5U. of Pittsburgh, 6TaskRabbit, 7Arizona State U., 8UC Santa Cruz
9U. of Southern California, 10IMRSV Data Labs, 11EPFL, 12U. of Illinois - Chicago, 13U. of Maryland Baltimore County
14Rutgers U., 15U. of Pennsylvania, 16Expedia Inc., 17U. of Houston, 18Indiana U. - Bloomington, 19Microsoft
Abstract
Despite the progress made in recent years
in addressing natural language understand-
ing (NLU) challenges, the majority of this
progress remains to be concentrated on
resource-rich languages like English. This
work focuses on Persian language, one of
the widely spoken languages in the world,
and yet there are few NLU datasets avail-
able for this language. The availability of
high-quality evaluation datasets is a neces-
sity for reliable assessment of the progress
on different NLU tasks and domains. We
introduce PARSINLU, the ﬁrst benchmark
in Persian language that includes a range
of language understanding tasks — Reading
Comprehension, Textual Entailment, etc.
These datasets are collected in a multitude
of ways, often involving manual annota-
tions by native speakers.
This results in
over 14.5k new instances across 6 distinct
NLU tasks.
Besides, we present the ﬁrst
results on state-of-the-art monolingual and
multi-lingual pre-trained language models
on this benchmark and compare them with
human performance, which provides valu-
able insights into our ability to tackle natural
language understanding challenges in Per-
sian. We hope PARSINLU fosters further
research and advances in Persian language
understanding.1
1
Introduction
In recent years, considerable progress has been
made in building stronger NLU models, particu-
larly supported by high-quality benchmarks (Bow-
man et al., 2015; Rajpurkar et al., 2016; Wang
⋆The point of view of the authors are their own and not
attributable to the company they work for.
1https://git.io/JIuRO
et al., 2019) for resourceful languages like En-
glish. However, in many other languages, such
benchmarks remain scarce, unfortunately, stagnat-
ing the progress towards language understanding
in these languages.
In this work, we focus on developing NLU
benchmarks for Persian (also known as “Farsi”).
This language has many attributes that make it dis-
tinct from other well-studied languages. In terms
of script, Persian is similar to Semitic languages
(e.g., Arabic). Linguistically, however, Persian is
an Indo-European language (Masica, 1993) and
thus distantly related to most of the languages
of Europe as well as the northern part of the In-
dian subcontinent. Such attributes make Persian a
unique case to study in terms of language tech-
nologies.
Although Persian is a widely spoken
language (Simons and Fennig, 2017), our ability
to evaluate performance and measure the progress
of NLU models on this language remains lim-
ited. This is mainly due to the lack of major lan-
guage understanding benchmarks that can evaluate
progress on a diverse range of tasks.
In this work, we present PARSINLU, a collec-
tion of NLU challenges for Persian.2 PARSINLU
contains challenges for reading comprehension,
multiple-choice question-answering, textual en-
tailment, sentiment analysis, question paraphras-
ing, and machine translation (examples in Fig. 1).
PARSINLU offers data for tasks that have never
been explored before in the context of the Per-
sian language.
We are not aware of any pub-
licly available dataset for Persian question answer-
ing (§3.2.2), reading comprehension (§3.2.1), and
paraphrasing (§3.2.5). For the rest of the tasks,
we improve at least one aspect of the existing
2We focus on the standard Iranian Persian, spoken by over
80 million people. There are other dialects of Persian spoken
in other countries, e.g., Afghanistan and Tajikistan.
arXiv:2012.06154v2  [cs.CL]  13 Jul 2021

--- Page 2 ---

datasets (e.g., better data construction, more com-
prehensive evaluation, and evaluation of less in-
vestigated genres or domains). To ensure the qual-
ity of the presented challenge tasks, we rely on
the annotations from native Persian speakers or
novel data collection techniques, such as, search
engine auto-complete (§3.2.1), and past collegiate
exams (§3.2.2). To the best of our knowledge, this
is the ﬁrst comprehensive collection of its own,
composed of a variety of Persian NLU tasks.
We conduct a collection of empirical work
(§4) to establish the difﬁculty of PARSINLU.
We benchmark each PARSINLU task via col-
lecting state-of-the-art multi-lingual and mono-
lingual LMs, as well as estimating the human up-
per bound scores. The gap between human and
machine baselines indicate the need for further
research and stronger models for Persian.
We
hope that the release of PARSINLU will encour-
age more research on Persian NLP.
2
Related Work
Cross-lingual benchmarks.
There are several
recent cross-lingual benchmarks; however, almost
none includes Persian:
XNLI (Conneau et al.,
2018) for entailment, PWNS-X (Yang et al., 2019)
for paraphrasing, XCOPA (Ponti et al., 2020)
for choice of plausible alternatives, XQuAD,
MLQA, TyDI and MKQA (Artetxe et al., 2020b;
Lewis et al., 2020; Clark et al., 2020a; Longpre
et al., 2020) for reading comprehension. These
datasets have also been integrated as part of multi-
task multilingual evaluation suites such as the
XTREME (Hu et al., 2020) and XGLUE (Liang
et al., 2020). Unfortunately, the Persian portion
of the former benchmark covers only two tagging
tasks (POS and NER) and the latter does not cover
Persian.
NLU
benchmarks
for
other
languages.
Benchmarks like GLUE (Wang et al., 2019)
encourage development of better and stronger
models on a diverse set of challenges.
There
have been several efforts to create GLUE-like
benchmarks for other languages; for example,
CLUE for Chinese (Xu et al., 2020), GLUECoS
for Hindi (Khanuja et al., 2020), and Russian-
SuperGLUE (Shavrina et al., 2020).
We view
PARSINLU in the same family of benchmarks,
dedicated to the Persian language.
NLU Datasets for Persian.
Prior work on cre-
ating evaluation resources for the Persian lan-
guage has focused on low-level tasks in narrow do-
mains (e.g., datasets for POS (Bijankhan, 2004),
NER (Shahshahani et al., 2019), Parsing (Seraji
et al., 2013)). Complementary to these efforts, we
aim at providing an NLU evaluation benchmark
for Persian, consisting of a wide variety of tasks.
Below we mention several related works and how
we build upon them.
FarsTail (Amirkhani et al., 2020) is a concurrent
work on the entailment task, where the dataset is
constructed semi-automatically based on existing
multiple-choice exams. Different from this work,
our entailment datasets are built with the annota-
tions of native speakers of Persian and some use
of machine translation (§3.2.4).
Therefore, we
hypothesize our construction represents a slightly
different distribution than that of FarsTail.
There is a rich set of works on Persian sentiment
analysis. We build upon these works and differ
from them in the following manners: (a) The ex-
isting work mainly focuses on document-level sen-
timent identiﬁcation which does not capture the
nuanced judgements with respect to aspects and
entities of the context (HosseinzadehBendarkheili
et al., 2019; Sharami et al., 2020, inter alia). In ad-
dition to such document-level annotations, we pro-
vide aspect-level sentiment annotations (§3.2.3).
(b) The majority of existing resources, such as Mi-
rasOpinion (AshraﬁAsli et al., 2020) focus on bi-
nary or ternary sentiment classes. However, our
annotations contain a more granular sentiment in-
tensity with ﬁve labels (§3.2.3).
(c) Compared
to the aspect-level datasets Hosseini et al. (2018);
Ataei et al. (2019), we cover two relatively less in-
vestigated domains: food & beverages and movies,
each posing new challenges for Persian sentiment
analysis.
Machine translation of Persian ⇄English is
one of the few tasks that has enjoyed decent atten-
tion (Tiedemann and Nygaard, 2004; Mohaghegh
et al., 2010; Pilevar et al., 2011; Mohaghegh et al.,
2011; Rasooli et al., 2013; Karimi et al., 2018;
Kasheﬁ, 2018; Khojasteh et al., 2020). Unfortu-
nately, most published work for this task focus on
niche domains and datasets. Our contribution to
this task is compiling a set of high-quality evalua-
tion sets from a broad range of domains, based on
the existing datasets as well as datasets introduced
in this work. The hope is that this will help future

--- Page 3 ---

Multiple-Choice QA:
 
Sentiment Analysis:
Reading Comprehension:
اĨ؟ اĨÕqن ļuام ğ~ء uńńĉqو :Ĩtال
Question: Nahavand is part of which province? 
ŉăuان اĨÕqن Ĕ}ı ğĄtب در }ĉĩ ÀĐا .Ĩا اĐ}ان ı}ب در ĩĉ}ی (ńqون) qĐ uńńĉqو :Ĝqراľ}اف
... Ĩا Ððăğ }òń ۷۲٬۲۱۸ دارای uńńĉqو .Ĩا uńńĉqو ĩĉ}ĨÕqن ~ļ}Ń و ÅÕĲ}ľ ĸ}ار
Paragraph: Nahavand (Navan) is a city in western Iran. This city is
located in the southern part of Hamedan province and it is the
capital city of Nahavand. Nahavand has a population of 72,218, ... 
ŉăuان اĨÕqن ،ŉăuان :ĨqĜ
Answer: Hamedan; Hamedan province 
Machine Translation:
 
Who believe in the Unseen, are steadfast in prayer, and
spend out of what We have provided for them.
¾Đļ}د روزĐéqن ÅĦ }ŉ از و uńدار qĜ ÅĔ ńăqز و uńاŗر اĐăqن Ðı ğĉqن ÅĔ Åļ ńqèļ اŗن
 .uĄĄļ اńòqق ĲøÐ}ان ÅĔ
ăÐĸ }ĔĔ}ا دو Ġuودا ،Åńľ}و ĂÐġ ¾ŉ ~Ðþńا òþĩ در ÕĠ qŃا داره Ĕtġ ¾ðĮ :}ïń
.داره رو ľ}م ĩtľ
 òĄŃ :ĐqĄðŃ Ĕqر
(òĄŃ ĂÐġ :uĐ}ġ ارزش/ăÐĸ) (ÔÖŃ :¾ðĮ) :ľvاری Åńqéń
Review: it tastes good but it’s so expensive even with a special offer.
It’s almost double the price of fresh meat. 
Review sentiment score: negative (-1) 
Aspect annotation: (taste: positive), (price: very negative)
ŉèÕĄu؟ qńļ}و uÐòĨ Ððĭو در اĐ}ان ĩĉ}ŉqی ļuام :۱ Ĩtال
ŉèÕĄu؟ qńļ}و ~Ń}ĸ Ððĭو در Đqŉ}ĉĩ ÅĦ :۲ Ĩtال
Question Paraphrasing:
Q1:Which cities in Iran are in white zones for corona?  
Textual Entailment:
او از qĐ ~Ðń £ńĐqرا و uĩ ŃÕtاری ،Ĭuام ¨Ĩtĕ دĨÕþÐ}ی ¾ÐĔ از اŗن از ¢Ĝ :Ĳ}ض £ÐĜ
.uńuĩ òáŃ ġ}Ĕ و uĄÕèğ ĎĔ}ا
.éľ òáŃ و uĩ ŃÕtاری Ĭuام ،دĨÕþÐ}ی ¾ÐĔ از :ÅÐĭ}Ĳ
Hypothesis: For the fear of being captured, Saddam fled and
went into hiding. 
Answer: contradicts  
Premise: He then fled for fear of being captured by Saddam,
and his allies also left him and some went into hiding.
Q2: What cities are red zones of corona?
Answer: not a paraphrase pair  
ļĄ¾؟ Ġvف Ĕtک ¢ÐĲ Ĭòàqت ĕăqم از را ¾Đqŉ ·ĐǓǎ ¾ńĕtا Ń ÅńtþĦ :۱ Ĩtال
Q1:How can I unlike all Facebook pages? 
Q2: If I like someone's picture in Facebook and then unlike it
will there be any notification in Facebook disclosing me?
Answer: not a paraphrase pair  
،¾Ąļ ·ĐǚǕńŗا ÅĂĬqĲǚǕĔ و ¾Ąļ ·ĐǓǎ Ĕtک ¢ÐĲ در را ìáĩ ¢üİ ÀŃ }ľا :۲ Ĩtال
ļĄu؟ Ĳqش را ÀŃ Åļ uĄļ Ń ńqĨر اĮǕǚع اĐéqن ÅĔ Ĕtک ¢ÐĲ qĐŗا
...łqğ ĦĄuان Åń Đروا و ،ńéuه ÅÕġĜ}دا Ĩدر ĩáìÐÕĉqی و uĔ ŉqی Ĕqزی qĔ ¾ĂÐĲ ·Đ :}ïń
.¾ĄüÐăń ÅÐĬtĕ رو £ńuĐد ǚǕĬا
 òĄŃ ĂÐġ :ĐqĄðŃ Ĕqر
(òĄŃ :Đروا/داĨÕqن) (òĄŃ :Ĝ}دازی Ðìáĩ/Ĕqزی) :ľvاری Åńqéń
Review: a movie with poor acting and underdeveloped characters. Not
an interesting plot ... I don’t recommend seeing this movie at all. 
Review sentiment score: very negative (-2) 
Aspect annotation: (performance/acting: negative), (narrative: negative)
qÕńǚǕĕŗا ĸtøĠ ŉqی ·ăļ از qÕńǚǕĕŗا در ĩĉ}ĨÕqن دو از £ÐĔ در }ÐøĲ اĲ}اد :Ĳ}ض £ÐĜ
.uń}Ðľ Ń ·ăļ
ÅĔ را Õłدو ġuŃqت qÕńǚǕĕŗا ĩĉ}ی ļǕǚن łqĐا ĄĜ در qÕńǚǕĕŗا ĸtøĠ ŉqی ·ăļ :ÅÐĭ}Ĳ
.uŉد Ń ÅĎارا }ÐøĲ اĲ}اد
Hypothesis: Atlanta Legal Aid provides civil services to poor
people in five metro Atlanta counties. 
Answer: entails   
Premise: Poor people in more than two counties in Atlanta
receive help from the Atlanta Legal Aid.
shrouds herself in white and walks penitentially disguised as
brotherly love through factories and parliaments; offers
help, but desires power.
¢łqßŃ و qŉ Åńqġļqر در ÅńĔ}ادرا ³éİ ŃÔuل łÔqس qĔ ÅĔtĕ ńéqن ÅĔ uÐòĨ Đدا در ĜÐæÐuه
.Ĩا ĸuرت łqĮ qŃا ،uĄļ Ń ·ăļ ĜÐéĄĉqد رود؛ Ń راه ĸqńtńþvاری
و ńßqر }ľا Ĩqزد Ń łuĄĬ ·Đ روز ÅĨ در ĩqľ}دش و łuĄĬ ·Đ روزی ńßqری
Ĩqزńu؟ Ń روزه uĄĦ را łuĄĬ ۱۲ uĄĄļ ļqر ¾ŉqĔ ĩqľ}دش
۶ (۴         ۸ (۳          ۹  (۲ ✓        ۱۲ (۱
A carpenter makes a chair a day and his student makes a chair
in three days If a carpenter and his student work together, how
many days will they make 12 chairs?
1) 12     ✓ 2) 9        3) 8       4) 6
ÐĔ ļuام qĔ «Ń}Ĩqن }ĩ ،èÐń uÐŃا tĕ }Ðġ ÅĔ Ń}ا ** ļèqن }Ðġ ÅĔ Ńاŗد Ĕtد اŃÐuوار» :ÐĔ
دارد؟ ŃtĉòŃ ĨqĄĕ
uĄÔĔ qĐ Àļqŉر qĐ را qŃ Ńþvار ÀÐĄĦ ÀĐا ** uĄÔĔ qŃ ¾ġز ÅĔ ¾ŉ}Ń درت ġqک از ŉqľ  (۱   
 درود ،éļ Åļ }ŉ Åń و uÐĨر ،Ĳر Åļ }ŉ Åń ** Ĩا ġtش uÐŃا ŉăqن uĐqÔń وĬqل Ń}ا (۲   
 زن ¾ļ £Ðń ńèqزی Ń ¾ŉ}Ń tĦ ** زن ¾ļ £Đر دل }Ĕ ğtر ĨĄqن (۳ ✓
ĩدا uĐqĔ Ń ļ}دľqر ÅĔ uÐŃا ** uĐqéþń èļ ļqر èļ £ÐĜ از (۴   
اĨ؟ ļuام ğĉqن ی ĸqره ÀĐ}Õľ~Ĕ
 qøĐ}Ĳŗا (۴    qüĐ}Ńŗا  (۳   qĜارو (۲    qÐĨŗا (۱✓
What is the largest continent in the world? 
✓ 1) Asia      2) Europe      3) Americas      4) Africa 
natural
quora
product
movie
natural
mnli
mizan
quran
literature
math&logic
common
knowledge
The verse "A man hoped for the good of others. I do not hope for your
good, just don't act like an evil." is closer to the meaning of which one? 
1)  Sometimes put ointment on my wounds ** Don't stay passive; either leave or close
the wound
2) I might not reach to her, but sure I have have the hope ** Not everyone who leaves,
arrives and not everyone who plants, harvests 
✓ 3) Your spear of pain keeps wounding me  ** if you're not going to put any
ointment on this pain, don't make it worse
4) No one will solve your problems ** Better maintain trust in God 
Figure 1: Examples of the PARSINLU tasks. For each task (other than Machine Translation which already contains
English phrases) we show the English translations for ease of communication to non-Persian readers. The purple
tags indicate the example category, according to their construction (explained in the main text under Section 3.2).

--- Page 4 ---

work on Persian MT to evaluate their systems on a
variety of domains to get a more realistic measure
of machine translation.
To the best of our knowledge, this is the
ﬁrst work that publishes an evaluation benchmark
for Persian language, promoting future studies
on several NLU tasks such as question answer-
ing (§3.2.2), reading comprehension (§3.2.1), and
paraphrasing (§3.2.5), among others.
3
PARSINLU
3.1
Design Considerations
We now discuss possible design choices for con-
structing the dataset and the underlying reasons.
Naturally-occurring
instances.
A
common
way of collecting data for low-resource languages
has been using automated translation of the bench-
mark datasets of high-resource languages (Artetxe
et al., 2020b; Ponti et al., 2020).
This can be
a poor practice as recent investigations have
shown translation artifacts in data gathered via
translation of existing tasks (Artetxe et al., 2020a).
It is important for any NLP dataset to reﬂect the
natural distribution of the target language tokens
and their associated cultural contexts. Therefore,
one should avoid over-reliance on automatic
conversion
of
resources
from
high-resource
languages to minimize any unnatural instances or
artifacts (Khvalchik and Malkin, 2020).
Experts, over crowdworkers.
While crowd-
sourcing has been the common approach for build-
ing datasets, we choose to work with few native
Persian speakers to construct the dataset. Crowd-
workers are difﬁcult to train and often generate
more noisy annotations. However, expert anno-
tators that are closely familiar with the task at
hand often generate better quality annotations. Us-
ing crowdworkers is further complicated by the
fact that crowdsourcing platforms do not have
an active community of Persian-speaking workers
due to limited international ﬁnancial transactions
and crowdsourcing platforms. A study done by
Pavlick et al. (2014, Table 6) shows that there are
almost no crowd-workers for Persian on the Ama-
zon Mechanical Turk platform.
3.2
Constructing PARSINLU tasks
Examples are shown in Fig. 1. We now explain the
data construction of each task.
3.2.1
Reading Comprehension
We use the commonly used deﬁnition of reading-
comprehension task: extracting a substring from
a given context paragraph that answers a given
question.
SQuAD (Rajpurkar et al., 2016) is one of the
most popular reading comprehension datasets in
English.
Similar datasets to SQuAD are devel-
oped in other languages using varying degrees of
human or semi-automatic translation techniques:
KorQuAD for Korean (Lim et al., 2019), MMQA
for Hindi (Gupta et al., 2018), etc. For construct-
ing our reading comprehension tasks, we avoid
using SQuAD as a source and employ a process
resembling that of Kwiatkowski et al. (2019) that
would lead to more natural questions.
Collecting questions.
Our efforts to translate
questions from the English dataset indicated that
such questions are often about topics that are not
of much importance in Persian. For instance, there
are many questions in SQuAD (Rajpurkar et al.,
2016) about major US sports events (e.g., Super-
bowl, NFL) or western civilization history that
might not be common among Persian speakers. In-
stead, we follow a pipeline that is more similar to
the one introduced by Kwiatkowski et al. (2019),
setting our goal to annotate answers for an existing
naturalistic set of questions in Persian, as opposed
to writing questions for existing paragraphs.
Unlike Kwiatkowski et al. (2019), we do not
have direct access to query logs.
Thus we fol-
low the approach of Berant et al. (2013); Khashabi
et al. (2021) which relies on a query auto-
completion API for collecting questions.
Simi-
larly, we use Google’s auto-completion3 which en-
ables us to mine a rich, yet a natural set of ques-
tions in Persian as it is reﬂective of popular ques-
tions posed by users of Google.
We start with a seed set of question terms
(e.g., “úæ» ék” [che kasI] meaning “who”, and
“Am.»” [kojA] meaning “where”) We bootstrap based
on this set, by repeatedly querying parts of
previously-extracted questions, in order to dis-
cover a longer and richer set of questions. We hy-
pothesize that such questions extracted from the
auto-complete algorithm, are highly reﬂective of
popular questions posed by Persian-speaking users
of Google. We ﬁlter out any results shorter than
5 tokens as they are often incomplete questions.
3http://google.com/complete/search?client=chrome&q=...

--- Page 5 ---

This process yields over 50k questions.
Subsequently, we automatically ﬁlter out open-
ended questions with no concrete answers (e.g.,
“? 	áK@P AK. ø 	PAK. øéj. J
	K” [nætIdZe ye bAzI bA ZA-
pon?] meaning “What is the results of the game
with Japan?”). Our ﬁltering was guided by the
observation that typically more complete ques-
tions lead to Google results that include well-
established sources (such as Wikipedia). Hence,
we perform this ﬁltering by retrieving the Google
search results4 for each question and checking if
any of the top 10 search results overlap with a pre-
deﬁned list of credible websites.5 We keep only
the questions that match this criterion.
Annotating paragraphs and answers.
In this
step, native speakers of Persian select a paragraph
and an answer span within the paragraph that an-
swers each of the questions. At the ﬁrst step, the
annotators read the question and correct any gram-
matical errors and typos (e.g., “ 	àA@” [otsAn] is
corrected to “ 	àAJ@” [ostAn] “state”). Next, they
annotate all the minimal and coherent spans that
contains the answer to the question, from a para-
graph obtained from a relevant web page (from
the Google search results retrieved from an ear-
lier step).
Whenever possible, we annotate all
valid spans as the answer (for example, “ 	à@YÒë”
[hæmedAn] and “ 	à@YÒë 	àAJ@” [ostAn e hæmedAn],
as shown in Fig. 1). The paragraph that contains
this answer is also annotated as the context of the
question.
Overall, 6 native-speaker annotators annotated
a collection of 1.3k question-answer-paragraph
triplets (Table 2).
Annotation quality.
To ensure the quality of the
annotations,
the answers to each question were
labeled by two independent annotators. Any mis-
alignment of the answer spans or missing any valid
spans were indicated as disagreements. Such dis-
agreements were resolved in further adjudication.
3.2.2
Multiple-Choice QA
Multiple-choice questions are one of the common
formats for evaluation of fact-retrieval and reason-
ing (Richardson et al., 2013; Clark et al., 2020b).
Following prior works, we deﬁne the task as:
given a natural language question, pick the correct
answer among a list of multiple candidates. A key
4https://github.com/MarioVilas/googlesearch
5fa.wikipedia.org, bbcpersian.com, etc.
difference from reading comprehension (§3.2.1) is
that the instances are open-domain (i.e., no con-
text paragraph is provided). Hence, a model would
either need to retrieve external supporting docu-
ments or have stored the necessary knowledge in-
ternally to be able to answer the question.
Sources of questions.
We use existing sources
of multiple-choice questions, rather than annotat-
ing new ones. We collect the questions from a
variety of sources: (i) The literature questions of
the annual college entrance exams in Iran, for the
past 15 years. These questions often involve the
understanding of poetry and their implied mean-
ing, knowledge of Persian grammar, and the his-
tory of literature. (ii) Employment exams that are
expected to assess an individual’s depth in various
topics (accounting, teaching, mathematics, logic,
etc). (iii) Common knowledge questions, which
involve questions about topics such as basic sci-
ence, history, or geography.
Most of the above sources are scanned copies
of the original exams in image format. We use
an existing Persian OCR tool to convert the im-
age data to a textual format.6 Then 4 annotators
ﬁx any mistakes made by the OCR system and
convert the result into a structured format. Over-
all, this yields 2460 questions with an average of
4.0 candidate answers (Table 2).
Additionally,
the task comes with a label indicating the type
of knowledge it requires: ‘literature’ (understand-
ing of literary expressions), ‘common-knowledge’
(encyclopedic knowledge or everyday activities),
and ‘math & logic’ (logical or mathematical prob-
lems). Examples from each category of questions
are included in Fig. 1.
Annotation quality.
To further examine the
quality of the annotations, we randomly sampled
100 questions from the annotations and cross-
checked the OCR output with the original data.
We discovered that 94 of such questions exactly
matched the original data, and the rest required
minor modiﬁcations. We thus conclude that the
annotated data has a high quality.
3.2.3
Aspect-Based Sentiment Analysis
Sentiment Analysis (SA) is the study of opin-
ions (i.e., positive, negative, or neutral sentiment)
expressed in a given text (Liu, 2012).
Aspect-
based Sentiment Analysis (ABSA) is a more ﬁne-
6https://www.sobhe.ir/alefba/

--- Page 6 ---

grained SA that aims to extract aspects of entities
mentioned in the text and determine sentiment to-
ward these aspects (Pontiki et al., 2014). For in-
stance, “it tastes good but it’s so expensive ...”
(Fig. 1) conveys positive and negative sentiments
with respect to taste and price aspects of the men-
tioned product (entity), respectively.
Annotation scheme.
We follow the existing
ABSA scheme (Pontiki et al., 2014). For every
review, we do two types of annotations: (1) we
assign an overall sentiment to each review, se-
lecting from one of the following values: very-
negative, negative, neutral, positive, very positive,
and mixed. The mixed category indicates reviews
where none of the sentiments are dominant (mix of
positive and negative, or borderline cases), hence
it is hard to detect the primary sentiment of a re-
view. We also assign neutral label to reviews that
express no clear sentiment toward an entity or any
aspect of it. (2) we annotate pairs of (a, s) where,
a is an aspect that belongs to a predeﬁned set of
aspects for each domain and s expresses the senti-
ment toward the aspect a.
Collecting reviews.
At ﬁrst, we collect reviews
from two different domains: (1) food & beverages
and 2) movies. We chose these domains since they
are relatively less investigated in the existing lit-
erature (see §2 for the past work). For the food
& beverages category, we extracted7 reviews from
the online grocery section of Digikala,8 and for the
movie reviews category, we crawled reviews from
Tiwall.9 Both of these websites are well-known
and popular websites among Persian speakers.
Deﬁning aspects.
Following ABSA scheme, we
predeﬁned a set of aspects for each domain. For
food & beverages, we crawled Digikala and re-
trieved all listed aspects for product reviews in
the food & beverages category.
Subsequently,
we manually aggregated the extracted aspects and
merged those with signiﬁcant semantic overlap.
We also added taste/smell as a new aspect cate-
gory since users frequently commented on this as-
pect. For movie reviews, we created an initial list
of aspects based on the movie review aspects de-
ﬁned by Thet et al. (2010). In consultation with
a movie critic, we resolved the potential overlaps
among aspect categories and created a set of as-
7https://github.com/rajabzz/digikala-crawler
8https://www.digikala.com/
9https://www.tiwall.com/
Food & beverages aspects
Movie review aspects
purchase value/price - ߾छ࡝ࡹ ارزش ྈྦભવ و
packaging - ಹ೐ࡐࣃ ຠ௱ࡥی و ࠤᝣ࣊ࡥاری
delivery - ፚ፬ऄ و ࠤࢆऄ و ارॖߜل
product quality - ࣫࡝ࢇ࡝߾ و ࠧߜزᎋᏵ ౟࿇ैঁل
nutritional value - ᏵᎸارزش ᄈࡤا
taste/smell - ঁࠡ ८߹क، ఊఖه و
music - ਅৰ࡝ॖঁघ
sound - ृࡥا
directing - ಉಇቅኇرඏජداᎨᏵ و ઠવو
story/screenplay - ࣃघߜࡍ෽෸࡝ࡺ داॖࡐߜن و
acting/performance -ࠡߜزی و ൽ࿆ैᆠ߾ ফ৏دازی
cinematography -ཿཽࠡࡺ࡝෸෽೭ഏداری و دور
scene - ࿅࿇ࡍࣃ و ᄓ৔০ه ࣈߜی ࠡᅏၑی
Table 1: The predeﬁned sentiment aspects (§3.2.3).
pects that capture various perspectives of movie
reviews. Overall, this process resulted in 6 and
7 aspects for food & beverages and movie review
domains, respectively (Table 1).
After deﬁning the sentiment aspects, we trained
four native speaker annotators for the ﬁnal round
of annotations. This results in 2423 instances for
the sentiment task (Table 2).
Annotation quality.
To measure the quality
of the annotations, we randomly selected 100
samples from each domain and calculated the
Inter-Annotator Agreement (IAA) using Cohen’s
kappa (Cohen, 1960) on annotations elicited from
two independent annotators. Based on the com-
puted IAA values, there is a substantial agreement
on sub-task 1 (0.76), and moderate agreement on
sub-tasks 2 and 3 (0.49 and 0.47, resp.).
Distribution of the labels.
Here we report the
distribution of the labels for this task. Fig. 2 shows
the distribution of the document-level sentiment
labels. As expected, most reviews are associated
with extreme sentiments (very positive or very
negative) and a relatively small portion of them are
neutral. There is also a non-negligible portion of
the reviews that contains mixed sentiments (par-
tially positive and partially negative).
label distribution
0%
10%
20%
30%
very negative negative
neutral
positive
very positive
mixed
Food
Movie
Figure 2: The distribution of the overall sentiments la-
bels (document-level).
3.2.4
Textual Entailment
Textual Entailment (Dagan et al., 2013; Bowman
et al., 2015) is typically deﬁned as a 3-way classiﬁ-

--- Page 7 ---

Task
Attribute
Statistic
Reading
Comprehen-
sion
# of instances
1300
avg. question length (tokens)
6.3
avg. paragraph length (tokens)
94.6
avg. answer length (tokens)
7.6
Multiple-
Choice
QA
# of instances
2460
% of ‘literature’ questions
834
% of ‘common-knowledge’ questions
949
% of ‘math & logic’ questions
677
avg. # of candidates
4.0
Sentiment
Analysis
# of instances
2423
% of ‘food & beverages’ reviews
1917
% of ‘movie’ reviews
506
avg. length of reviews (words)
22.01
# of annotated pairs of (aspect, sentiment)
2539
Textual
Entailment
# of instances
2,700
% of ‘natural’ instances
1,370
% of ‘mnli’ instances
1,330
avg. length of premises (tokens)
23.4
avg. length of hypotheses (tokens)
11.8
Question
Paraphrasing
# of instances
4,644
% of ‘natural’ instances
2,521
% of ‘qqp’ instances
2,123
avg. length of Q1 (tokens)
10.7
avg. length of Q2 (tokens)
11.0
Machine
Translation
# of instances
47,745
% of ‘QP’ subset
489
% of ‘Quran’ subset
6,236
% of ‘Bible’ subset
31,020
% of ‘Mizan’ subset (eval. only)
10,000
Table 2: Statistics on various subsets of the dataset.
cation to determine whether a hypothesis sentence
entails, contradicts, or is neutral with respect to a
given premise sentence.
We construct two subsets: (i) based on available
natural sentences, and (ii) based on the available
English entailment dataset. The former approach
yields high-quality instances, however, it is a rela-
tively slower annotation task. The latter is slightly
easier, but yields less interesting instances.
Based on natural sentences.
We start with ran-
domly sampled raw sentences, selected from 3 dif-
ferent resources: Miras,10 Persian Wikipedia and
VOA corpus.11 In this random sampling process,
we speciﬁcally sample sentences that contain con-
junctive adverbs (e.g, “AÓ@” [amA] meaning “but”),
along with their preceding sentences. We chose
such examples as there is a higher chance that
these sentences naturally contain inference rela-
tionships.
We ask annotators to consider both
sentences and write a premise and correspond-
ing entailing, contradicting, and neutral sentences,
whichever they deem appropriate. To minimize
10https://github.com/miras-tech/MirasText
11https://jon.dehdari.org/corpora/
annotation artifacts and avoid creating an artiﬁ-
cially easy dataset, we speciﬁcally instruct anno-
tators to avoid using simple modiﬁcations, such as
simply negating a sentence or changing a word to
its synonym. For the rest of the work, we refer to
this set as the ‘natural’ set.
Based on existing datasets.
In this approach,
we use existing datasets in English. We start with
MNLI dataset (Williams et al., 2018) and translate
them with the publicly available Google Trans-
late API.12 Subsequently, expert annotators care-
fully review and ﬁx inaccurate translations. Fur-
thermore, each translated document is reviewed by
a native-speaker annotator to correct the transla-
tional mistakes. Our annotations show that about
66.4% of the translated documents have gone
through some form of correction by our annota-
tors. For the rest of the draft, we refer to this set as
‘mnli’.
Overall, our two-pronged construction with 6
annotators results in 2.7k entailment instances
(Table 2). Examples from each collected subset
are included in Fig. 1.
Annotation quality.
To verify the annotation
quality, we quantify the agreement of 3 indepen-
dent annotators, on 150 random examples. On this
subset, we observe a Fleiss Kappa (Fleiss, 1971)
of 0.77, indicating a substantial inter-annotator
agreement (Landis and Koch, 1977).
Distribution of the labels.
As the label distri-
bution (Fig. 3) shows, the distribution of the labels
across the three categories are not far from uni-
form distribution.
label distribution
0%
10%
20%
30%
40%
50%
entails
neutral 
contradicts 
natural
mnli
Figure 3: The distribution of the labels for the entail-
ment task.
3.2.5
Question Paraphrasing
This task is deﬁned as determining whether two
given questions are paraphrases or not. This task
12https://cloud.google.com/translate

--- Page 8 ---

has been previously used to improve down-stream
applications like document retrieval (Zukerman
and Raskutti, 2002; Callison-Burch et al., 2006;
Duboue and Chu-Carroll, 2006).
Similar to the construction of the entailment
task (§3.2.4), we take two different approaches: (i)
based on available natural sentences, (ii) based an
existing English question paraphrasing dataset.
Based on natural sentences.
We start with
questions mined using Google auto-complete
(§3.2.1) as well as an additional set of questions
mined from Persian discussion forums.13
We
create pairs of questions with high token over-
lap. Each pair is annotated as paraphrase or not-
paraphrase by native-speakers. We drop the pair if
any of the questions is incomplete. For the rest of
this document, we refer to this subset as ‘natural’.
Based on existing datasets.
We start with the
QQP dataset,14 which is a dataset of English
question-pairs, and translate it with Google Trans-
late API. Later, expert annotators carefully review
the translations and amend any inaccuracies. We
observe that about 65.6% of the translated docu-
ments have gone through some form of correction
by our annotators.
Overall, the annotations involved 4 annotators
and resulted in 4682 question paraphrasing in-
stances (Table 2). Examples from each collected
subset are included in Fig. 1.
Annotation quality.
After the annotation of the
earlier steps, the example were reviewed by an-
other annotators familiar with the task. The dis-
agreements were labeled and adjudicated among
the annotators, in order to ensure the quality of the
resulting labels.
Distribution of the labels.
As the label distri-
bution shows (Fig. 4), the label distributions of the
two splits (‘qqp’ vs ‘natural’) are not much differ-
ent.
3.2.6
Machine Translation
We consider the task of translating a given English
sentence into Persian, and vice versa.
This task is one of the few for which several
resources are available in the literature (Kasheﬁ,
2018; Prokopidis et al., 2016; Pilevar et al., 2011).
One major limitation is that there is no widely
13http://javabkoo.com/
14https://www.kaggle.com/c/quora-question-pairs
label distribution
0%
20%
40%
60%
80%
paraphrase 
not paraphrase 
natural
qqp 
Figure 4: Label distribution for the query paraphrasing
task.
Task
Train
Dev
Eval
Reading Comprehension
600
125
575
Multiple-Choice
1271
139
1050
Sentiment Analysis
1894
235
294
Textual Entailment
756
271
1,751
Question Paraphrasing
1,830
898
1,916
Machine Translation
1.6m
2k
47k
Table 3: Split sizes for different tasks.
adopted comprehensive assessment of this task:
most of the works are often limited to narrow
domains, and the generalization across different
styles of text is rarely studied. Our contribution
is to put together a collection of evaluation sets,
from various domains to encourage a more holis-
tic evaluation set.
Our proposed evaluation sets consist of the fol-
lowings: (i) Quran: Quran has been translated
into many languages, including English and Per-
sian (Tiedemann and Nygaard, 2004). We use sev-
eral different translations of Quran to create high-
quality evaluation sets (10 gold standard transla-
tions for each direction).
Having multiple gold
standards is particularly helpful for the automatic
evaluation of machine translation since such met-
rics work best when provided with several gold
standards (Gupta et al., 2019).
(ii) Bible: sim-
ilarly, we use Persian and English versions of
Bible15 as another evaluation set. (iii) QQP: us-
ing the data obtained in the construction of ques-
tion paraphrasing task (§3.2.5) to create an eval-
uation set for translating language questions. (iv)
Mizan: we use the evaluation subset of the Mizan
corpus (Kasheﬁ, 2018), which is acquired based
on a manual alignment of famous literary works
and their published Persian translations. Overall,
the combination of these four high-quality sub-
sets yields an evaluation set that contains 47k sen-
15https://github.com/christos-c/bible-corpus

--- Page 9 ---

Setup
Model ↓- Task →
Reading
Comprehension
Multiple-Choice Question Answering
Textual Entailment
Question Paraphrasing
Subtask →
all
literature
com-know
math & logic
natural
mnli
natural
qqp
trained on Persian
mBERT (base)
49.0
30.1.
28.7
33.8
48.7
51.6
80.4
75.3
WikiBERT (base)
39.2
36.9
30.2
34.1
52.8
52.6
80.0
75.5
ParsBERT (base)
40.7
33.4
28.6
32.5
51.8
53.9
79.4
72.0
mT5 (small)
30.9
33.7
23.7
39.1
51.9
51.0
75.2
72.0
mT5 (base)
42.6
34.0
24.0
36.9
57.8
59.9
79.1
75.1
mT5 (large)
49.2
32.6
27.1
38.9
69.1
71.6
84.6
76.6
mT5 (XL)
70.4
33.7
27.7
38.9
77.2
74.5
88.6
80.3
trained on
English
mT5 (small)
33.0
20.9
25.7
28.9
45.1
55.6
73.5
75.1
mT5 (base)
53.4
23.4
23.4
24.3
44.4
43.3
83.2
81.8
mT5 (large)
67.4
27.4
33.1
25.4
46.5
54.9
88.1
86.6
mT5 (XL)
68.2
28.3
38.6
22.0
66.2
77.8
89.2
87.0
trained on
Per + Eng
mT5 (small)
45.3
30.9
24.9
36.6
53.3
56.2
77.9
71.3
mT5 (base)
63.9
32.3
24.0
37.7
57.8
63.9
80.2
73.4
mT5 (large)
73.6
30.6
28.9
38.6
70.9
72.5
85.3
78.9
mT5 (XL)
74.7
38.0
33.7
38.0
75.5
78.7
88.2
80.3
Human
86.2
80.0
85.0
85.0
87.1
90.2
92.3
88.4
Setup
Model ↓- Task →
Sentiment
(sentence sent.)
Sentiment
(aspect ext.)
Sentiment
(aspect sent.)
Machine Translation (Eng →Per)
Machine Translation (Per →Eng)
Subtask →
food
movies
food
movies
food
movies
quran
bible
qqp
mizan
quran
bible
qqp
mizan
trained on our data
mBERT (base)
55.2
48.6
87.1
73.24
53.9
34.7
-
-
-
-
-
-
-
-
WikiBERT (base)
52.0
58.5
91.9
78.0
56.5
41.6
-
-
-
-
-
-
-
-
ParsBERT (base)
59.1
56.8
91.1
76.8
53.9
37.6
-
-
-
-
-
-
-
-
mT5 (small)
54.6
49.4
86.4
78.6
52.4
40.6
10.2
2.1
22.2
8.4
20.6
2.5
22.9
14.6
mT5 (base)
56.6
52.9
88.6
80.5
52.9
46.5
11.4
2.1
27.3
9.4
22.8
2.5
34.6
14.9
mT5 (large)
62.9
72.5
92.2
85.0
58.1
53.5
11.9
2.1
24.8
10.6
24.7
2.4
35.1
16.4
mT5 (XL)
63.1
70.6
92.0
85.8
58.9
54.5
13.5
2.2
20.0
11.0
30.0
2.6
33.7
19.3
trained on
English
mT5 (small)
-
-
-
-
-
-
-
-
-
-
6.6
1.9
7.7
3.7
mT5 (base)
-
-
-
-
-
-
-
-
-
-
11.5
2.1
14.0
5.7
mT5 (large)
-
-
-
-
-
-
-
-
-
-
20.2
2.3
21.0
7.4
mT5 (XL)
-
-
-
-
-
-
-
-
-
-
25.6
2.3
30.7
9.7
trained on
Per + Eng
mT5 (small)
-
-
-
-
-
-
-
-
-
-
19.2
2.5
25.6
12.1
mT5 (base)
-
-
-
-
-
-
-
-
-
-
24.1
2.4
36.0
14.8
mT5 (large)
-
-
-
-
-
-
-
-
-
-
29.9
2.6
36.5
18.1
mT5 (XL)
-
-
-
-
-
-
-
-
-
-
33.4
2.6
41.0
18.2
Human
88.4
90.3
93.1
91.6
71.0
61.6
-
-
-
-
-
-
-
-
Table 4: Evaluation of Persian-only models (top), English-only (middle) and Persian+English (bottom) models
on Persian tasks. Best baseline scores are indicated as bold.
tences, from 4 different domains (Table 2.)
While our main contribution here is providing a
more comprehensive evaluation of machine trans-
lation, we also provide training/dev sets to let the
future work create comparable experiments to that
of ours. We compile our training set at the union
of the following datasets: (i) questions obtained
from the question paraphrasing task (§3.2.5, by
translating the QQP instances), (ii) the training
set of Mizan dataset (Kasheﬁ, 2018), (iii) TEP
dataset (Pilevar et al., 2011) and Global Voices
dataset (Prokopidis et al., 2016). The latter two
are not included in our evaluation set due to their
noisy translations to prevent any inaccurate evalu-
ations. Note that the Quran and Bible documents
are intentionally not included in the training data,
in order to measure models’ generalization to un-
seen documents.
4
Experiments
We experiment with several recent LMs, to assess
the difﬁculty of the PARSINLU tasks (compared
to human expert performance) and also to estab-
lish baseline performance of the state-of-the-art
mono- and multi-lingual pre-trained models.
All the baseline models used in this work are
available online.16
Evaluation metrics.
For each task, we pick a
common set of existing metrics:
For reading-
comprehension, we use F1 between gold an-
swer and the response string (Rajpurkar et al.,
2016); for question paraphrasing, textual entail-
ment, multiple-choice question-answering, and
sentiment analysis, we use accuracy. For the ﬁrst
two sub-tasks of sentiment analysis (document-
level sentiment, aspect extraction), we use macro-
F1. For the third sub-task (aspect-speciﬁc senti-
16Included in the repository mentioned in footnote 1.

--- Page 10 ---

ment) we use accuracy as our target evaluation
metric (Angelidis and Lapata, 2018; Sun et al.,
2019).
For machine translation we use Sacre-
BLEU (Post, 2018).
Task splits.
For each task, we have provided
statistics on eval, train, and dev splits in Table 3. In
doing so, we have ensured that enough instances
are included in our evaluation sets.
Human performance.
To have an estimate of
the performance and the difﬁculty of the chal-
lenges, we report human performance on a ran-
dom subset (100-150) of instances from each task.
Similar to Wang et al. (2019), we collect annota-
tions from three human annotators, adjudicate the
inconsistencies and evaluate it against the gold la-
bels to estimate human performance for each task.
Models.
For evaluation of our baselines, we
use state-of-the-art LMs.
Multilingual BERT
(mBERT) (Devlin et al., 2019) is pre-trained on
the masked LM task over 104 languages.
Ad-
ditionally, we use two specialized variants of
BERT for Persian: wikiBERT17 (trained on Per-
sian Wiki) and ParsBERT (Farahani et al., 2020).18
We also use mT5 (Xue et al., 2021), which is a
multilingual variant of T5 (Raffel et al., 2020).
Model selection.
We train each model with var-
ious hyper-parameters and select the best one ac-
cording to their developement set performance.
For the BERT-based models, we ﬁne-tune them
according to the cross product of the following
hyper-parameters: (1) Batch sizes: {8, 16} for
small/base models and {1, 2} for large models;
(2) Training epochs: {3, 7}; (3) Learning-rates:
{3 × 10−5, 5 × 10−5}. For mT5 models, we ﬁne-
tune them for 20k steps, dumping checkpoints ev-
ery 1k step. For the translation task, we trained
the models for 200k steps since the task has much
larger training data. We use 10−3 learning-rate.
Input/output encoding.
We formulate ques-
tion paraphrasing (§3.2.5) and entailment (§3.2.4)
tasks as text classiﬁcation tasks.19 For sentiment-
analysis (§3.2.3), we follow formulation of Sun
et al. (2019) and encode the instances as questions
per aspect. The expected output is the sentiment
polarity of the input review with respect to the in-
put aspect-speciﬁc question. This formulation has
17https://github.com/TurkuNLP/wikibert
18https://github.com/hooshvare/parsbert
19https://git.io/JYTNr
the beneﬁt that it is not restricted to a particular
domain and its associated set of aspects, unlike al-
ternatives such as multi-class classiﬁcation.
Experimental setups.
First, we ﬁne-tune our
models on Persian (our dataset). The results of
this setup are listed in the top segment of Table 4.
Following the recent works on generalization
across languages (Artetxe et al., 2020b), we
evaluate English models on our Persian bench-
mark.
We use the commonly used English
datasets to supervise mT5 on each task and eval-
uate the resulting model on the evaluation sec-
tion of PARSINLU. The English datasets used
here are as follows: SQuAD 1.1 (Rajpurkar et al.,
2016) for reading comprehension (size:
88k),
the union of ARC (Clark et al., 2018), Open-
BookQA (Mihaylov et al., 2018) and Common-
senseQA (Talmor et al., 2019) for multiple-choice
question-answering (size: 18k), SNLI (Bowman
et al., 2015) for textual entailment (size: 550k),
QQP20 for question paraphrasing (size: 350k), and
Arabic-English subset of OPUS-100 (Zhang et al.,
2020) for machine translation (size: 1m).
We
don’t do such mixing for sentiment analysis since
existing English datasets are not quite compatible
with our sentiment schema. The results are re-
ported in the middle section of Table 4.
Finally, we train models on the union of Persian
and English datasets. Since English datasets tend
to be much bigger than Persian ones, we make
sure that the batches of training data, on average,
contain the same number of instances from each
language. Similar treatments of task mixing have
also been adopted by Khashabi et al. (2020); Raf-
fel et al. (2020). The results of this setup are at the
bottom segment of Table 4.
4.1
Results
Below are key insights from the empirical work:
Humans do well on PARSINLU.
As shown in
the last row of Table 4, the human upper-bound
scores are relatively high across the board. This is
an indication of a reasonable degree of consensus
between the ground-truth and judgments of native
speakers and hence, the quality of our dataset.
Models haven’t solved PARSINLU yet.
The
majority of the models signiﬁcantly lag behind
human performance. This is especially true for
the mid-sized (‘large’ or smaller) models that are
20See footnote 14.

--- Page 11 ---

commonly used. It is encouraging that our largest
model (mT5-XL) achieves close to human perfor-
mance, for certain tasks (e.g., question paraphras-
ing), however, this model is prohibitively large and
it requires a massive amount of compute. How-
ever, even these large models still struggle for
most of the remaining tasks, particularly multiple-
choice QA.
English models successfully transfer to Persian.
Consistent with the prior observations (Artetxe
et al., 2020b), multilingual models (mT5, in this
case) trained with English data show a surpris-
ing degree of generalization to other languages (to
Persian, in our case). Training on English data is
particularly helpful for challenges that were orig-
inally translated from English datasets (such as
‘qqp‘ and ‘mnli‘).
Joint training on English and Persian helps.
For most of the tasks, combining Persian and En-
glish yields better results than training solely on
Persian or English data.
While joint training generally helps, such com-
binations are not guaranteed to lead to positive
gains all the times. Whether the “Eng + Per” mod-
els will beat either of the Persian-only or English-
only models depends on whether their strengths
(large size of “Eng” and distributional alignment
of “Per”) align or go against each other. Because
of this issue, the combined models are not always
better than the individual models.
5
Discussion
We now discuss several limitations of the current
dataset and the experiments. We then outline sev-
eral directions for future work.
Beyond current models.
As shown in the ear-
lier experiments, for most of the tasks the cur-
rent mid-sized models perform signiﬁcantly worse
than humans. This is particularly pronounced for
the multiple-choice QA task where there is over
40% gap between the model and human perfor-
mance, and increasing the model size (number of
parameters) shows minimal beneﬁts.
We hypothesize that the difﬁculty of our
multiple-choice questions (and other tasks, to
some extent) for the models are partly due to the
reasoning and abstraction needed to answer them.
For example, the ‘literature’ questions often de-
mand creating connection several pieces of poetry,
based on abstract interpretations of their mean-
ings. Likewise, most of the ‘math & logic’ ques-
tions require several ‘hops’ of algebraic operations
to get to the ﬁnal answer. We hypothesizes these
challenges (multi-hop reasoning over high-level
abstractions of language) cannot be solely be ad-
dressed with more training data. and likely require
a dramatic rethinking of our architectures design.
For example, the poor performance on ‘math &
logic’ questions might be due to models’ inabil-
ity to comprehend Persian numbers and do logical
reasoning with them, a topic that is brieﬂy studied
in English (Geva et al., 2020).
There might also
be value in exploring multi-task setups across our
various tasks (Zaremoodi et al., 2018), which we
delegate to the future work. We hope this bench-
mark will encourage more of such studies, espe-
cially in the context of the Persian language.
Coverage of dialects.
There are other dialects
of Persian, including Dari and Tajiki dialects, that
are not covered by our dataset. We acknowledge
this limitation and hope the future work will create
broader and more inclusive collections.
6
Conclusion
This work introduced PARSINLU, a benchmark
for high-level language understanding tasks in
Persian. We present a careful set of steps we have
followed to construct each of the tasks with the
help of native speakers (§3.2). We have presented
human scores to establish estimated upper-bounds
for each task. This is followed by evaluating state-
of-the-art models on each task and quantifying the
human-machine gap (§4).
To the best of our knowledge, this is the ﬁrst
work that publishes a language understanding
benchmark for Persian language. We hope that
PARSINLU inspires more activity in the Persian
NLU tasks, as well as contributing to the latest ef-
forts in multilingual NLU.
Acknowledgement
The authors would like to thank Alireza Nourian
for providing the OCR system used in the work
and the anonymous reviewers for their construc-
tive feedback.
Thanks to Google’s TensorFlow
Research Cloud (TFRC) for making research
TPUs available.

--- Page 12 ---

References
Hossein
Amirkhani,
Mohammad
Azari
Ja-
fari,
Azadeh
Amirak,
Zohreh
Pourjafari,
Soroush Faridan Jahromi, and Zeinab Kouhkan.
2020.
Farstail:
A Persian natural lan-
guage inference dataset.
arXiv preprint
arXiv:2009.08820.
Stefanos Angelidis and Mirella Lapata. 2018.
Multiple instance learning networks for ﬁne-
grained sentiment analysis.
Transactions of
the Association for Computational Linguistics,
6:17–31.
Mikel Artetxe, Gorka Labaka, and Eneko Agirre.
2020a.
Translation artifacts in cross-lingual
transfer learning. In Proceedings of EMNLP,
pages 7674–7684.
Mikel Artetxe, Sebastian Ruder, and Dani Yo-
gatama. 2020b. On the cross-lingual transfer-
ability of monolingual representations. In Pro-
ceedings of ACL, pages 4623–4637.
Seyed Arad AshraﬁAsli, Behnam Sabeti, Zahra
Majdabadi, Preni Golazizian, Reza Fahmi, and
Omid Momenzadeh. 2020. Optimizing anno-
tation effort using active learning strategies: A
sentiment analysis case study in Persian.
In
Proceedings of LREC, pages 2855–2861.
Taha
Shangipour
Ataei,
Kamyar
Darvishi,
Soroush
Javdan,
Behrouz
Minaei-Bidgoli,
and Sauleh Eetemadi. 2019.
Pars-absa:
an
aspect-based sentiment analysis dataset for
Persian. arXiv preprint arXiv:1908.01815.
Jonathan Berant, Andrew Chou, Roy Frostig, and
Percy Liang. 2013. Semantic parsing on free-
base from question-answer pairs. In Proceed-
ings of EMNLP, pages 1533–1544.
Mahmood Bijankhan. 2004. The role of the cor-
pus in writing a grammar:
An introduction
to a software. Iranian Journal of Linguistics,
19(2):48–67.
Samuel R Bowman, Gabor Angeli, Christopher
Potts, and Christopher D Manning. 2015.
A
large annotated corpus for learning natural lan-
guage inference. In Proceedings of EMNLP.
Chris Callison-Burch, Philipp Koehn, and Miles
Osborne. 2006.
Improved statistical machine
translation using paraphrases. In Proceedings
of NAACL, pages 17–24.
Jonathan H Clark, Eunsol Choi, Michael Collins,
Dan Garrette, Tom Kwiatkowski, Vitaly Niko-
laev, and Jennimaria Palomaki. 2020a.
TyDi
QA: a benchmark for information-seeking ques-
tion answering in ty pologically di verse lan-
guages.
Transactions of the Association for
Computational Linguistics, 8:454–470.
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar
Khot, Ashish Sabharwal, Carissa Schoenick,
and Oyvind Tafjord. 2018.
Think you
have solved question answering?
try arc,
the ai2 reasoning challenge.
arXiv preprint
arXiv:1803.05457.
Peter Clark, Oren Etzioni, Tushar Khot, Daniel
Khashabi, Bhavana Mishra, Kyle Richardson,
Ashish Sabharwal, Carissa Schoenick, Oyvind
Tafjord, Niket Tandon, et al. 2020b. From ‘F’
to ‘A’ on the NY Regents Science Exams: An
Overview of the Aristo Project. AI Magazine,
41(4):39–53.
Jacob Cohen. 1960. A coefﬁcient of agreement for
nominal scales. Educational and psychological
measurement, 20(1):37–46.
Alexis Conneau, Ruty Rinott, Guillaume Lam-
ple, Adina Williams, Samuel Bowman, Holger
Schwenk, and Veselin Stoyanov. 2018.
Xnli:
Evaluating cross-lingual sentence representa-
tions. In Proceedings of EMNLP, pages 2475–
2485.
Ido Dagan, Dan Roth, Mark Sammons, and
Fabio Massimo Zanzotto. 2013.
Recognizing
Textual Entailment: Models and Applications.
Morgan & Claypool Publishers.
Jacob Devlin, Ming-Wei Chang, Kenton Lee,
and Kristina Toutanova. 2019.
BERT: Pre-
training of Deep Bidirectional Transformers for
Language Understanding.
In Proceedings of
NAACL, pages 4171–4186.
Pablo Duboue and Jennifer Chu-Carroll. 2006.
Answering the question you wish they had
asked: The impact of paraphrasing for question
answering.
In Proceedings of NAACL, pages
33–36.

--- Page 13 ---

Mehrdad Farahani, Mohammad Gharachorloo,
Marzieh Farahani, and Mohammad Manthouri.
2020. Parsbert: Transformer-based model for
Persian language understanding. arXiv preprint
arXiv:2005.12515.
Joseph L Fleiss. 1971. Measuring nominal scale
agreement among many raters. Psychological
bulletin, 76(5):378.
Mor Geva, Ankit Gupta, and Jonathan Berant.
2020. Injecting numerical reasoning skills into
language models. In Proceedings of ACL, pages
946–958.
Deepak Gupta, Surabhi Kumari, Asif Ekbal, and
Pushpak Bhattacharyya. 2018.
Mmqa:
A
multi-domain multi-lingual question-answering
framework for english and hindi. In Proceed-
ings of LREC.
Prakhar Gupta, Shikib Mehri, Tiancheng Zhao,
Amy Pavel, Maxine Eskenazi, and Jeffrey P
Bigham. 2019.
Investigating evaluation of
open-domain dialogue systems with human
generated multiple references. In Proceedings
of SIGDIAL, pages 379–391.
Pedram Hosseini, Ali Ahmadian Ramaki, Hassan
Maleki, Mansoureh Anvari, and Seyed Abol-
ghasem Mirroshandel. 2018.
Sentipers:
A
sentiment analysis corpus for Persian.
arXiv
preprint arXiv:1801.07737.
Fatemeh HosseinzadehBendarkheili, Rezvan Mo-
hammadiBaghmolaei, and Ali Ahmadi. 2019.
Product quality assessment using opinion min-
ing in persian online shopping. In Proceedings
of ICEE, pages 1917–1921. IEEE.
Junjie Hu, Sebastian Ruder, Aditya Siddhant, Gra-
ham Neubig, Orhan Firat, and Melvin John-
son. 2020.
Xtreme:
A massively multilin-
gual multi-task benchmark for evaluating cross-
lingual generalisation. In Proceedings of ICML,
pages 4411–4421. PMLR.
Akbar
Karimi,
Ebrahim
Ansari,
and
Bahram Sadeghi Bigham. 2018.
Extract-
ing an english-persian parallel corpus from
comparable corpora. In Proceedings of LREC.
Omid Kasheﬁ. 2018.
Mizan: a large Persian-
english
parallel
corpus.
arXiv
preprint
arXiv:1801.02107.
Simran Khanuja, Sandipan Dandapat, Anirudh
Srinivasan, Sunayana Sitaram, and Monojit
Choudhury. 2020.
GLUECoS: An evaluation
benchmark for code-switched NLP.
In Pro-
ceedings of ACL.
Daniel Khashabi,
Sewon Min,
Tushar Khot,
Ashish Sabharwal, Oyvind Tafjord, Peter Clark,
and Hannaneh Hajishirzi. 2020.
Uniﬁedqa:
Crossing format boundaries with a single qa
system. In Proceedings of EMNLP (Findings),
pages 1896–1907.
Daniel Khashabi, Amos Ng, Tushar Khot, Ashish
Sabharwal, Hannaneh Hajishirzi, and Chris
Callison-Burch. 2021. Gooaq: Open question
answering with diverse answer types.
arXiv
preprint arXiv:2104.08727.
Hadi Abdi Khojasteh, Ebrahim Ansari, and Mahdi
Bohlouli. 2020.
Lscp: Enhanced large scale
colloquial persian language understanding. In
Proceedings of LREC, pages 6323–6327.
Maria Khvalchik and Mikhail Malkin. 2020. De-
partamento de nosotros: How machine trans-
lated corpora affects language models in mrc
tasks. In Proceedings of the Workshop on Hy-
brid Intelligence for Natural Language Pro-
cessing Tasks (HI4NLP 2020) co-located with
24th European Conference on Artiﬁcial Intelli-
gence (ECAI 2020): Santiago de Compostela,
Spain, August 29, 2020, pages 29–33. CEUR
Workshop Proceedings.
Tom Kwiatkowski, Jennimaria Palomaki, Olivia
Redﬁeld, Michael Collins, Ankur Parikh, Chris
Alberti, Danielle Epstein, Illia Polosukhin, Ja-
cob Devlin, Kenton Lee, et al. 2019. Natural
questions: a benchmark for question answering
research.
Transactions of the Association for
Computational Linguistics, 7:453–466.
J Richard Landis and Gary G Koch. 1977. The
measurement of observer agreement for cate-
gorical data. biometrics, pages 159–174.
Patrick Lewis, Barlas Oguz, Ruty Rinott, Se-
bastian Riedel, and Holger Schwenk. 2020.
MLQA:
Evaluating
cross-lingual
extractive
question answering.
In Proceedings of ACL,
pages 7315–7330.
Yaobo Liang, Nan Duan, Yeyun Gong, Ning Wu,
Fenfei Guo, Weizhen Qi, Ming Gong, Linjun

--- Page 14 ---

Shou, Daxin Jiang, Guihong Cao, et al. 2020.
Xglue:
A new benchmark datasetfor cross-
lingual pre-training, understanding and gener-
ation. In Proceedings of EMNLP, pages 6008–
6018.
Seungyoung Lim, Myungji Kim, and Jooyoul Lee.
2019. Korquad1. 0: Korean qa dataset for ma-
chine reading comprehension.
arXiv preprint
arXiv:1909.07005.
Bing Liu. 2012. Sentiment analysis and opinion
mining. Synthesis lectures on human language
technologies, 5(1):1–167.
Shayne Longpre, Yi Lu, and Joachim Daiber.
2020. MKQA: A Linguistically Diverse Bench-
mark for Multilingual Open Domain Question
Answering. arXiv preprint arXiv:2007.15207.
Colin P Masica. 1993. The indo-aryan languages.
Cambridge University Press.
Todor Mihaylov, Peter Clark, Tushar Khot, and
Ashish Sabharwal. 2018. Can a suit of armor
conduct electricity?
a new dataset for open
book question answering.
In Proceedings of
EMNLP.
Mahsa Mohaghegh, Abdolhossein Sarrafzadeh,
and Tom Moir. 2010. Improved language mod-
eling for English-Persian statistical machine
translation. In Proceedings of the Workshop on
Syntax and Structure in Statistical Translation,
pages 75–82.
Mahsa
Mohaghegh,
Abdolhossein
Sar-
rafzadeh, and Tom Moir. 2011.
Improving
Persian-English
statistical
machine
transla-
tion:experiments in domain adaptation.
In
Proceedings of the Workshop on South South-
east
Asian
Natural
Language
Processing
(WSSANLP), pages 9–15.
Ellie Pavlick, Matt Post, Ann Irvine, Dmitry
Kachaev, and Chris Callison-Burch. 2014. The
language demographics of amazon mechanical
turk. Transactions of the Association for Com-
putational Linguistics, 2:79–92.
Mohammad Taher Pilevar, Heshaam Faili, and
Abdol Hamid Pilevar. 2011.
Tep:
Tehran
english-Persian parallel corpus.
In Interna-
tional Conference on Intelligent Text Process-
ing and Computational Linguistics, pages 68–
79. Springer.
Edoardo Maria Ponti, Goran Glavaš, Olga Majew-
ska, Qianchu Liu, Ivan Vuli´c, and Anna Korho-
nen. 2020. Xcopa: A multilingual dataset for
causal commonsense reasoning.
In Proceed-
ings of EMNLP, pages 2362–2376.
Maria Pontiki, Dimitris Galanis, John Pavlopou-
los, Harris Papageorgiou, Ion Androutsopou-
los, and Suresh Manandhar. 2014.
SemEval-
2014 task 4: Aspect based sentiment analysis.
In Proceedings of the International Workshop
on Semantic Evaluation (SemEval 2014), pages
27–35.
Matt Post. 2018.
A call for clarity in reporting
BLEU scores. In Proceedings of WMT, pages
186–191.
Prokopis Prokopidis, Vassilis Papavassiliou, and
Stelios Piperidis. 2016. Parallel global voices:
a collection of multilingual corpora with citizen
media stories. In Proceedings of LREC, pages
900–905.
Colin Raffel, Noam Shazeer, Adam Roberts,
Katherine
Lee,
Sharan
Narang,
Michael
Matena, Yanqi Zhou, Wei Li, and Peter J Liu.
2020. Exploring the limits of transfer learning
with a uniﬁed text-to-text transformer. Journal
of Machine Learning Research, 21(140):1–67.
Pranav Rajpurkar, Jian Zhang, Konstantin Lopy-
rev, and Percy Liang. 2016. Squad: 100,000+
questions for machine comprehension of text.
In Proceedings of EMNLP.
Mohammad Sadegh Rasooli, Ahmed El Kholy,
and Nizar Habash. 2013.
Orthographic
and morphological processing for Persian-to-
English statistical machine translation. In Pro-
ceedings of IJCNLP, pages 1047–1051.
Matthew Richardson, Christopher JC Burges, and
Erin Renshaw. 2013.
Mctest:
A challenge
dataset for the open-domain machine compre-
hension of text.
In Proceedings of EMNLP,
pages 193–203.
Mojgan Seraji, Carina Jahani, Beáta Megyesi, and
Joakim Nivre. 2013.
Uppsala Persian depen-
dency treebank annotation guidelines. Techni-
cal report, Uppsala University.
Mahsa
Sadat
Shahshahani,
Mahdi
Mohseni,
Azadeh Shakery, and Heshaam Faili. 2019.

--- Page 15 ---

Payma: A tagged corpus of Persian named en-
tities. Signal and Data Processing, 16(1):91–
110.
Javad PourMostafa Roshan Sharami, Parsa Ab-
basi Sarabestani, and Seyed Abolghasem Mir-
roshandel. 2020.
Deepsentipers: Novel deep
learning models trained over proposed aug-
mented persian sentiment corpus.
arXiv
preprint arXiv:2004.05328.
Tatiana Shavrina, Alena Fenogenova, Emelyanov
Anton, Denis Shevelev, Ekaterina Artemova,
Valentin Malykh, Vladislav Mikhailov, Maria
Tikhonova,
Andrey
Chertok,
and
Andrey
Evlampiev. 2020. Russiansuperglue: A russian
language understanding evaluation benchmark.
In Proceedings of EMNLP, pages 4717–4726.
Gary F Simons and Charles D Fennig. 2017. Eth-
nologue: languages of Asia. sil International
Dallas.
Chi Sun, Luyao Huang, and Xipeng Qiu. 2019.
Utilizing bert for aspect-based sentiment analy-
sis via constructing auxiliary sentence. In Pro-
ceedings of NAACL, pages 380–385.
Alon Talmor, Jonathan Herzig, Nicholas Lourie,
and Jonathan Berant. 2019. Commonsenseqa:
A question answering challenge targeting com-
monsense knowledge.
In Proceedings of
NAACL, pages 4149–4158.
Tun Thura Thet, Jin-Cheon Na, and Christo-
pher SG Khoo. 2010. Aspect-based sentiment
analysis of movie reviews on discussion boards.
Journal of information science, 36(6):823–848.
Jörg Tiedemann and Lars Nygaard. 2004.
The
OPUS corpus - parallel and free: http://
logos.uio.no/opus.
In Proceedings of
LREC.
Alex Wang, Yada Pruksachatkun, Nikita Nangia,
Amanpreet Singh, Julian Michael, Felix Hill,
Omer Levy, and Samuel Bowman. 2019. Super-
glue: A stickier benchmark for general-purpose
language understanding systems. In Proceed-
ings of NourIPS, pages 3266–3280.
Adina Williams, Nikita Nangia, and Samuel Bow-
man. 2018. A broad-coverage challenge corpus
for sentence understanding through inference.
In Proceedings of NAACL, pages 1112–1122.
Liang Xu, Hai Hu, Xuanwei Zhang, Lu Li, Chen-
jie Cao, Yudong Li, Yechen Xu, Kai Sun, Dian
Yu, Cong Yu, et al. 2020. Clue: A chinese lan-
guage understanding evaluation benchmark. In
Proceedings of COLING, pages 4762–4772.
Linting Xue, Noah Constant, Adam Roberts,
Mihir Kale, Rami Al-Rfou, Aditya Siddhant,
Aditya Barua, and Colin Raffel. 2021. mt5: A
massively multilingual pre-trained text-to-text
transformer. In Proceedings of the 2021 Con-
ference of the North American Chapter of the
Association for Computational Linguistics: Hu-
man Language Technologies, pages 483–498.
Yinfei Yang, Yuan Zhang, Chris Tar, and Ja-
son Baldridge. 2019. Paws-x: A cross-lingual
adversarial dataset for paraphrase identiﬁca-
tion. In Proceedings of EMNLP-IJCNLP, pages
3678–3683.
Poorya Zaremoodi, Wray Buntine, and Gholam-
reza Haffari. 2018. Adaptive knowledge shar-
ing in multi-task learning:
Improving low-
resource neural machine translation.
In Pro-
ceedings of the 56th Annual Meeting of the As-
sociation for Computational Linguistics (Vol-
ume 2: Short Papers), pages 656–661.
Biao Zhang, Philip Williams, Ivan Titov, and Rico
Sennrich. 2020.
Improving massively multi-
lingual neural machine translation and zero-
shot translation. In Proceedings of ACL, pages
1628–1639.
Ingrid Zukerman and Bhavani Raskutti. 2002.
Lexical query paraphrasing for document re-
trieval. In Proceedings of COLING.

```
