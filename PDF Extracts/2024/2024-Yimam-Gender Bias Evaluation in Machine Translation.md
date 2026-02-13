---
title: "2024-Yimam-Gender Bias Evaluation in Machine Translation - PDF Extract"
source_pdf: "2024-Yimam-Gender Bias Evaluation in Machine Translation.pdf"
pages: 11
extracted_at: "2026-02-13T09:15:45.468010"
---

# PDF Extract: 2024-Yimam-Gender Bias Evaluation in Machine Translation

**Source PDF:** 2024-Yimam-Gender Bias Evaluation in Machine Translation.pdf
**Total Pages:** 11

---

## Content

```
--- Page 1 ---

Proceedings of the 2nd International Workshop on Gender-Inclusive Translation Technologies, pages 1–11
June 27, 2024 ©2024 European Association for Machine Translation
Gender Bias Evaluation in Machine Translation for Amharic, Tigrinya,
and Afaan Oromoo
Walelign Tewabe Sewunetie1,2, Atnafu Lambebo Tonja3,4,5, Tadesse Destaw Belay4,
Hellina Hailu Nigatu6, Gashaw Kidanu7, Zewdie Mossie1, Hussien Seid7,
Seid Muhie Yimam8
∀Ethio NLP, 1Debre Markos University, Ethiopia, 2University of Miskolc, Hungary, 3Lelapa AI,
4Instituto Politécnico Nacional, Mexico, 5Mohamed bin Zayed University of Artificial Intelligence, UAE,
6University of California, Berkeley, USA, 7Addis Ababa Science and Technology University, Ethiopia
8Universität Hamburg, Germany
Abstract
While Machine Translation (MT) research has
progressed over the years, translation systems
still suffer from biases, including gender bias.
While an active line of research studies the ex-
istence and mitigation strategies of gender bias
in machine translation systems, there is limited
research exploring this phenomenon for low-
resource languages.
The limited availability
of linguistic and computational resources con-
founded with the lack of benchmark datasets
makes studying bias for low-resourced lan-
guages that much more diﬀicult. In this paper,
we construct benchmark datasets to evaluate
gender bias in machine translation for three
low-resource languages: Afaan Oromoo (Orm),
Amharic (Amh), and Tigrinya (Tir).
Build-
ing on prior work, we collected 2400 gender-
balanced sentences parallelly translated into
the three languages. From human evaluations
of the dataset we collected, we found that
about 93% of Afaan Oromoo, 80% of Tigrinya,
and 72% of Amharic sentences exhibited gen-
der bias. In addition to providing benchmarks
for improving gender bias mitigation research
in the three languages, we hope the careful
documentation of our work will help other low-
resourced language researchers extend our ap-
proach to their languages.1
© 2024 The authors. This article is licensed under a
Creative Commons 4.0 licence, no derivative works, at-
tribution, CC-BY-ND.
1Our dataset is available at https://huggingface.co/
datasets/EthioNLP/Gender-Bias-Evaluation-Dataset
1
Introduction
Machine Translation (MT) systems play a piv-
otal role in breaking down language barri-
ers and facilitating cross-cultural communica-
tion. Gender bias poses a significant challenge,
particularly in languages with limited linguis-
tic resources. The imbalance within datasets
used for MT training often results in gender-
related disparities. In low-resource languages
like Amharic, Tigrinya, and Afaan Oromoo,
and in morphologically rich languages like Ara-
bic (Habash et al., 2019; Alhafni et al., 2022)
professional names such as doctor, pilot, pro-
fessor, etc., are mostly translated using the
masculine gender.
Machine Translation services often default
to masculine forms for professions like “doc-
tor” and “nurse,” for feminine forms poten-
tially reflecting and reinforcing gender stereo-
types. Figure 1 and Figure 2 demonstrate this
for the Amharic language2. These types of bias
can lead to misunderstandings and reinforce
gender roles, influencing how people perceive
different professions based on gender. Under-
standing and addressing gender bias in MT
systems is vital for ensuring equitable and ac-
curate communication across diverse linguistic
communities.
Addressing the issue of gender bias in MT
systems requires adequate datasets for eval-
uation; a challenging task in the context of
low-resource languages. This work contributes
to building equitable MT systems for low-
resource languages by constructing a gold-
test dataset for three languages:
Amharic,
2In the screenshots provided, Google Translate translit-
erated the word “doctor” instead of translating it to the
Amharic word for ‘doctor’ ሐኪም
1

--- Page 2 ---

Figure 1:
Translating the sentence “The doctor
is coming” Google Translate translates the word
“doctor” into masculine gender for the Amharic
language.
The word “doctor,”
translated in
Amharic as “ዶክተር” (dokter), is gender-neutral.
However, when translating “The doctor is coming,”
Google Translate translates the sentence to “ዶክተሩ
እየመጣነው።” (dokteru eyemet’a new).
Here the
phrase “The doctor” becomes “ዶክተሩ” (dokteru);
the prefix “u” indicates masculine gender in the
Amharic language.
In addition, the word “com-
ing” translates into “እየመጣ” (eyemet’a); which also
indicates masculine gender.
Figure 2: In the sentence “The nurse is coming”,
the word “nurse,” translated in Amharic as “ነርስ”
(ners), is gender-neutral. However, when translat-
ing “The nurse is coming,” Google Translate trans-
lates the sentence to “ነርሷእየመጣችነው።” (nerswa
eyemet’ach new). Here the phrase “The nurse” be-
comes ”ነርሷ” (ners-wa); the prefix “wa” indicates
feminine gender in the Amharic language. In addi-
tion, the word “coming” translates into “እየመጣች”
(eyemet’ach); which also indicates feminine gender.
Tigrinya, and Afaan Oromoo.
The method-
ologies developed in this research can subse-
quently be applied and scaled up to assess
gender bias in other low-resource languages.
We collected 2400 gender-balanced sentences,
which can be used as a benchmark for gender
bias evaluation in low-resource language trans-
lation.
In addition, this study investigates users’
perceptions of gender bias in commercial MT
systems and evaluates Google Translate as a
use case in the three languages of study. Our
analysis shows interesting differences in re-
spondents’ perceptions of gender bias across
these language communities.
These findings
underscore the detailed relationship between
language, culture, and gender bias percep-
tion in MT systems, highlighting the need
for adapted approaches to mitigate bias and
enhance translation accuracy within specific
linguistic contexts.
Furthermore, this study
investigates the performance of one open-
source MT model and one commercial model,
namely, NLLB
(Team et al., 2022), and
Google MT using automatic evaluation met-
rics, such as SacreBleu
(Post, 2018), and
Chrf++
(Popović, 2017).
The outcomes of
this evaluation across various language pairs
shed light on the eﬀicacy and accuracy of MT
systems in translating between English and
the target languages.
The evaluation shows
diverse performance metrics across language
pairs, with distinct variations in translation
quality and effectiveness.
These results un-
derscore the importance of robust evaluation
methodologies and metrics in assessing MT
system performance and informing strategies
for enhancing translation accuracy and eﬀi-
ciency across diverse linguistic contexts.
2
Related work
Investigating bias in MT systems is an ac-
tive body of work in the NLP community.
We use the taxonomy from (Blodgett et al.,
2020a) and focus on representational harms
due to stereotyping:
sustaining stereotypi-
cal gender connotations for occupations dur-
ing translation, thereby limiting the variety
2

--- Page 3 ---

of occupations a specific gender may or may
not engage in3. Previous works in this space
have relied on (1) curating benchmark datasets
(e.g.(Wairagala et al., 2022; Cho et al., 2019)),
(2) human evaluation schemes (e.g. (Stanovsky
et al., 2019)), and (3) automatic evaluation
schemes(e.g. (Savoldi et al., 2021)).
In cu-
rating benchmark datasets,
(Prates et al.,
2020) prepared a gender-balanced dataset for
evaluating gender bias in translation systems
pertaining to occupation.
Since different
languages represent gender in various ways
(Savoldi et al., 2021), evaluation and mitiga-
tion strategies might also have to account for
such variation.
For instance,
(Cho et al.,
2019) prepared test sets with gender natural
pronouns used in the Korean language for in-
vestigating bias in Korean-English translation
pairs.
In evaluating gender bias in MT, several
works rely on automatic metrics.
(Prates
et al., 2020) found that Google Translate de-
faults to the masculine pronoun when translat-
ing job descriptions, particularly in relation to
science, technology, engineering, and mathe-
matics (STEM) professions. (Cho et al., 2019)
introduces a new evaluation index, the Trans-
lation Gender Bias Index (TGBI), for measur-
ing gender neutrality and evaluating Korean-
English translation pairs.
(Stanovsky et al.,
2019) introduce an evaluation protocol that
relies on co-reference resolution datasets and
morphological analysis to automatically eval-
uate gender bias across eight target languages
that use grammatical gender.
(Wairagala et
al., 2022) used the Word Embeddings Fairness
Evaluation Framework (WEFE) to measure
gender bias in MT systems built for Luganda-
English translation.
While automated mea-
sures allow us to capture a broader under-
standing of the phenomenon, they may limit
the detail and depth of our analysis. The study
by (Stanovsky et al., 2019) uses automatic and
human evaluations in tandem, exploiting both
the versatility of automated evaluation and the
nuance and detail captured by human evalua-
tion.
As the work by (Blodgett et al., 2020b) ar-
gues, it is important first to articulate how bias
3We note in this work, we are considering a binary gen-
der system of men and women
in such systems can be harmful. Relying on the
taxonomy of harms from prior work (Crawford,
2017; Barocas et al., 2017), we posit that un-
derstanding gender bias exhibited by MT sys-
tems would allow us to (1) uncover the repre-
sentational harms the systems exhibit thereby
understanding what power structures they up-
hold and (2) mitigate allocational harms that
might result from deploying such systems in
downstream applications (e.g.
employment
and job search).
One challenge in studying bias in machine-
translated text is the diverse socio-cultural as-
pects that shape how gender is articulated
among different groups and how stereotypes
propagate in this diverse context.
Talat et
al. (2022) have shed light on the diﬀiculty
of studying and mitigating bias across multi-
cultural, multilingual groups.
Such contexts
require community-rooted efforts that thor-
oughly investigate how the culture and lan-
guage are structured. In this work, we curate
benchmark datasets for three low-resource lan-
guages through collaborations among native
speakers. Based on previous works, (Renduch-
intala et al., 2021; Stanovsky et al., 2019), we
conduct an automatic evaluation of the trans-
lation quality overall and human evaluations
of gender bias in popular machine translation
systems to understand the current landscape
of translation systems for these languages.
3
Background: Linguistic Gender
Representation
Amharic, a Semitic language, uses grammati-
cal gender. Most nouns and pronouns have dis-
tinct masculine and feminine forms. Gender-
specific pronouns are used (e.g., እሱ(ǝssu) for
“he” and እሷ(ǝsswa) for “she”), and job titles
can also have gendered forms.
Like Amharic, Tigrinya, another Semitic
language, has grammatical gender.
Gender
distinctions are marked in nouns and pro-
nouns. There are specific pronouns for differ-
ent genders (e.g., ንሱ(nǝssu) for “he” and ንሳ
(nǝssa) for “she”), and job titles may vary de-
pending on gender.
Afaan Oromoo, a Cushitic language, does
not have grammatical gender in the same way
as the other two languages.
Gender-neutral
pronouns are often used, but context can some-
3

--- Page 4 ---

times specify gender. Gender is less likely to
be marked in job titles compared to the other
two languages of study.
To illustrate more about the issues in trans-
lating a sentence and a professional word, we
can see the following example of Gender Bias
in English to Amharic Translation.
The English to Amharic Google Translate
(accessed January 20, 2024) output of the
sentence “The nurse helped the doctor” is
“ነርሷ
ሐኪሙን
ረድታለች።” (nerswa hakimun
redtalech). Here, “ነርሷ” (nerswa) ‘the nurse’
is female, and “ሐኪሙን” (hakimun) “the doc-
tor” is male. The word “helped”, while it has
a translation issue4, is translated to “ረድታለች”
(redtalech), which is indicative of a feminine
subject.
In Amharic, the source sentence “The nurse
helped the doctor” can be translated in eight
different ways as follows:
1. “ነርሷ
ሐኪሙን
ረድታዋለች።”
(nerswa
hakimun
redtawalech).
Here
“ነርሷ”
(neriswa) ‘the nurse’ is female, “ሐኪሙን”
(hakimun)
‘the
doctor’
is
male,
and
“ረድታዋለች” (reditawalechi) ‘she helped
him’.
2. “ነርሷ
ሐኪሟን
ረድታታለች።”
(neriswa
ḥākīmwan reditatalechi).
Here “ነርሷ”
(neriswa) ‘the nurse’ is female, “ሐኪሟን”
(ḥākīmwan) ‘the doctor’ is female, and
“ረድታታለች” (reditatalechi) ‘she helped
her’.
3. “ነርሷ
ሐኪሙን
ረድታቸዋለች።”
(neriswa
ḥākīmun reditachewalechi) (for respect
or plural).
Here “ነርሷ” (neriswa) ‘the
nurse’ is female, “ሐኪሙን” (hakimun) ‘the
doctor’ is male, and “ረድታቸዋለች” (redi-
tachewalechi) ‘she helped him.’
4. “ነርሷ
ሐኪሟን
ረድታቸዋለች።”
(neriswa
ḥākīmwan reditachewalechi). Here “ነርሷ”
(neriswa) ‘the nurse’ is female, “ሐኪሟን”
(ḥākīmwan) ‘the doctor’ is female, and
“ረድታቸዋለች”
(reditachewalechi)
‘she
helped her’ (for respect or plural).
4It should be translated in this context as “ረድታዋለች”
(redtawalech) or “ረድታቸዋለች” (redtachewalech) for re-
spect (she helped him) instead of ”ረድታለች” (red-
talech).
5. “ነርሱ
ሐኪሙን
ረድቶታል።” (nersu ḥākī-
mun reditotale). Here “ነርሱ” (nersu) ‘the
nurse’ is male, “ሐኪሙን” (hakimun) ‘the
doctor’ is male, and “ረድቶታል” (redito-
tale) ‘he helped him’.
6. “ነርሱ
ሐኪሟን
ረድቷታል።”
(nersu
ḥākīmwan
reditwatale).
Here
“ነርሱ”
(nersu) ‘the nurse’ is male,
“ሐኪሟን”
(hakimun) ‘the doctor’ is female, and
“ረድቷታል” (reditwatale) ‘he helped her’.
7. “ነርሱ
ሐኪሟን
ረድቷቸዋል።”
(nersu
ḥākīmwan reditwachewal).
Here “ነርሱ”
(nersu) ‘the nurse’ is male,
“ሐኪሟን”
(ḥākīmwan) ‘the doctor’ is female, and
“ረድቷቸዋል” (reditwachewal) ‘he helped
her’ (for respect or plural).
8. “ነርሱሐኪሙንረድቷቸዋል።” (nersu ḥākī-
mun reditwachewal). Here “ነርሱ” (nersu)
‘the nurse’ is male, “ሐኪሙን” (ḥākīmun)
‘the doctor’ is female, and “ረድቷቸዋል”
(reditwachewal) ‘he helped him’ (for re-
spect or plural).
This range of translations reflects the po-
tential for gender bias in translation when as-
sumptions are made about the gender of indi-
viduals based on their professional names.
4
Gold Gender Bias Test Dataset
Preparation
4.1
Dataset Collection and Composition
The gold gender bias test dataset was crafted
by combining sentences from public reposito-
ries
(Sharma et al., 2022), with a thorough
examination of gender biases across these se-
lected target languages. We first collected an
English-centric dataset from a variety of pub-
licly available sources such as SimpleGEN, 5
and winomt,6 focusing on relevance and diver-
sity.
To maintain balance, for every gender-
specific sentence, we ensured there was an
equivalent counterpart. For example, if a sen-
tence says, “He is a doctor,” a corresponding
sentence like “She is a doctor” is included for
gender parity.
5SimpleGEN:https://github.com/arendu-zz/
SimpleGEN
6winomt:
https://github.com/manandey/bias_
machine_translation/tree/main/data/base/winomt
4

--- Page 5 ---

Figure 3: An example from our test dataset used out of 108 professional names.
However, these open-source datasets do not
contain all professional names relevant to our
communities of interest, even though they con-
tain enough test datasets.
For this reason,
we used a crowdsourcing approach to collect
additional data that reflects various profes-
sions.
For this approach, we first incorpo-
rated the major professional names from (1)
the Ethiopian Civil Service Commission list of
job titles and (2) querying GPT 3.5 for recent
technological professional words.
Through
this process, we collected 108 unique profes-
sional names. Figure 3 demonstrates a sample
gender-balanced dataset of each professional
name.
Then, we used paid freelancers for crowd-
sourcing and prepared a Google form contain-
ing clear and short instructions about the task.
The goal of the crowdsourcing task was to
create gender-balanced translation pairs from
English-centric data from various sources. One
of the key considerations was to include both
pronouns and occupations in the dataset. This
ensured that each profession is associated with
different pronouns, such as “he,” “his,” and
“him” for the masculine, and “she” and “her”
for the feminine gender. For this task, ten free-
lancers were involved and signed an incentive
agreement first. Then, we collected the English
dataset from SimpleGEN (n=130), winomt
(n=192), and crowd-sourced (n=2078), a to-
tal of 2400 sentences.
4.2
Dataset Translation
The
next
task
is
to
translate
this
col-
lected dataset into three Ethiopian languages:
Amharic, Afaan Oromoo, and Tigrinya. Like-
wise, we have used paid linguistic experts who
were proficient in one of our target languages,
then undertook the translation process to pre-
serve linguistic accuracy and capture cultural
differences specific to each target language.
To prevent boredom and errors, we engaged
six language experts and fluent speakers per
language pair, totaling eighteen individuals
from various universities.
We assigned 600
sentence pairs per individual to keep the task
manageable.
After the translation, we re-
cruited two paid professional linguists and edi-
tors for each language pair for quality checking.
The dataset used in this research, referred
to as the Gold Gender Bias Test Dataset (GG-
BTD), comprises 2400 sentence pairs for each
language pair, specifically English-Amharic,
English-Afaan Oromoo, and English-Tigrinya,
resulting in a total of 7200 sentence pairs.
5

--- Page 6 ---

Within each language pair, the dataset main-
tains a comprehensive gender balance. Specif-
ically, for each language pair, 1200 sentences
represent masculine gender expressions, while
the remaining 1200 sentences capture feminine
gender expressions.
5
Evaluation Techniques
5.1
Automatic Evaluation
Different evaluation metrics are usually em-
ployed to automatically evaluate MT systems.
These metrics are often based on word over-
lap and/or context similarity between refer-
ences and model outputs.
In our work, we
employ both types of metrics to evaluate the
quality of NLLB and Google MT that we con-
sider in our study. Namely, we used SacreBleu
(Post, 2018) and Chrf++ (Popović, 2017) ma-
chine translation evaluation metrics. We chose
these MT evaluation metrics for several rea-
sons. Firstly, these metrics are widely recog-
nized and utilized in the field of MT research,
ensuring compatibility and comparability with
existing literature (Kadaoui et al., 2023).
Additionally, SacreBleu and Chrf++ are
known for their robustness and effectiveness
(Puduppully et al., 2023) in assessing trans-
lation quality across different languages and
translation systems. Their ability to capture
detailed aspects of translation quality, such as
fluency, adequacy, and fidelity to the source
text, makes them suitable choices for our eval-
uation framework. Furthermore, both metrics
are supported by well-established methodolo-
gies and have demonstrated consistent perfor-
mance in benchmarking studies, giving us con-
fidence in their reliability. However, these met-
rics evaluate only the overall translation accu-
racy.
5.2
Human Evaluation
In this work, we relied solely on human-level
evaluation techniques for evaluating gender
bias.
We assessed the gender bias in two
MT systems:
(1) open source NLLB model
and (2) commercially available Google Trans-
late. We chose these models since they support
all three languages (Amharic, Tigrinya, Afaan
Oromoo).
Given the high cost of human-level evalu-
ation, we only evaluated the gender bias of
Google Translate. For the human-level evalua-
tion, first, we developed the evaluation guide-
lines shown in the appendix 10.1, and used the
Potato annotation tool (Pei et al., 2022). Fig-
ure 4 shows the Potato annotation tool GUI
for human-label evaluation, which supports all
modern browsers and can be accessed both
from computers and mobile phones for man-
ual annotation.
Criteria included gender bi-
ases, translation quality, and the accuracy of
professional name translations. For evaluation,
eighteen paid linguistic experts per language
were selected.
To avoid subjectivity, we di-
vided evaluators into three groups and made
the evaluation into three phases; this implies
each sentence is evaluated three times. This
is good for taking the majority vote for result
analysis.
After each sentence in each of the three lan-
guages is evaluated by three evaluators, the an-
notation tool decides whether the sentence is
biased or not by taking the majority vote of
the three evaluators.
6
Result and Analysis
Figure 5 provides a clear comparison of re-
sponses across three language categories, al-
lowing for insights into the distribution of re-
sponses within each language. It presents the
gender bias across various language groups,
delineating respondents’ perceptions regarding
the presence or absence of gender bias within
each language category.
The data in Table 1 underscores the dis-
parate perceptions of gender bias among re-
spondents
across
different
linguistic
back-
grounds.
Particularly notable is the signif-
icantly higher percentage (92.96%) of Afaan
Oromoo respondents who indicated observ-
ing gender bias compared to other language
groups, with only 7.04% indicating otherwise.
Similarly, in the Amharic group, approxi-
mately 72.50% of respondents indicated ob-
serving gender bias, contrasting with 27.50%
who did not.
Likewise,
in the Tigrinya
group, the majority (80.96%) indicated observ-
ing gender bias, while 19.04% expressed no
bias. These findings reveal distinct patterns re-
garding whether speakers observe gender bias
across language groups, suggesting potential
implications for addressing and understanding
6

--- Page 7 ---

Figure 4: The Potato annotation GUI for the evaluation annotation.
Table 1: Translation Issues by Language
Amharic
Tigrinya
Afaan Oromoo
There is an issue in translating the sentence
1429
936
918
There is an issue in translating the profession
258
475
612
No issue
510
619
421
Both issues
203
370
449
Total
2400
2400
2400
gender bias in MT within these communities.
Table 1 outlines translation issues across lan-
guages, categorized into “Translating the sen-
tence issue” and “Professional word translation
issue.” Amharic records the highest instances
of sentence translation issues at 1429, followed
by Tigrinya with 936, and Afaan Oromoo
with 918. Regarding professional word transla-
tion, Afaan Oromoo leads with 612 instances,
trailed by Tigrinya at 475, and Amharic at 258.
Tigrinya exhibits the fewest reported issues
overall, with 619 sentences indicating no trans-
lation issues, compared to 510 for Amharic and
421 for Afaan Oromoo. Conversely, Amharic
shows the highest incidence of respondents fac-
ing both types of issues at 203, followed by
Afaan Oromoo at 449, and Tigrinya at 370.
This data underscores the diverse challenges
faced in translation across languages and pro-
vides valuable insights for enhancing transla-
tion quality and addressing language-specific
obstacles.
Table 2 presents the evaluation results for
NLLB and Google Translate models in the se-
lected language pairs.
The table is divided
into rows representing different language pairs
and columns representing the specific evalua-
tion metrics. Each language pair is evaluated
in both translation directions (e.g., Eng-Amh
and Amh-Eng), providing insights into ma-
chine translation systems’ translation quality
and performance across various linguistic con-
texts.
The result shows that the Google MT sys-
tem outperformed the NLLB model when us-
ing English as the source language in both
evaluation metrics. This shows that translat-
ing English sentences into the target Ethiopian
language is challenging for the model. On the
other hand, the Google MT system showed
better results compared to the NLLB model
when translating English sentences into target
Ethiopian languages. We observed better per-
formance results when using English as the tar-
get language than when using it as the source
language in the NLLB model. From this, we
can see that for low-resource languages, pub-
licly available MT models like NLLB are strug-
7

--- Page 8 ---

Figure 5: Illustration of the Google Translation Gender Bias test dataset human evaluation result. “Yes” and
“No” are the answers to the question, “Is there bias in the translation?”. “Yes” means the sentence contains
gender bias when translated to a specified language. “No” is no gender bias observed in the translated sentence;
the sentence is correctly translated.
Table 2: Automatic Evaluation Results
Language
NLLB
Google MT
SacreBleu ↑
Chrf++ ↑
SacreBleu ↑
Chrf++ ↑
Eng- Amh
3.48
23.73
16.13
47.97
Amh- Eng
21.87
50.76
-
Eng- Orm
4.85
34.85
22.96
56.71
Orm- Eng
17.80
41.63
-
Eng- Tir
3.89
18.52
16.00
38.00
Tir- Eng
20.01
43.91
-
gling to predict the correct translation when
using English as the source language.
7
Conclusion and Future Work
In this paper, we curated a benchmark dataset
for evaluating gender bias in machine transla-
tion systems in three low-resource languages.
With this test dataset, we conducted a human-
level gender bias evaluation of Google Trans-
late and NLLB MT models for the given lan-
guage pairs. The evaluation result shows that
92.96% of Eng-Orm, 80.96% of Eng-Tir, and
72.50% of Eng-Amh language pairs transla-
tions have a gender bias. In addition, we used
the automatic evaluation to measure the trans-
lation quality of the currently available trans-
lation tools that support Amharic, Tigrinya,
and Afaan Oromoo languages.
Our findings highlight the need for further
research and development efforts to mitigate
gender bias and promote gender-inclusive lan-
guage translation. We observed that this work
can be scaled up and used as a benchmark for
other low-resource languages. In future work,
we will use automatic gender bias evaluation
metrics in addition to human evaluation. In
addition, we will prepare a gender-balanced
dataset for the given language, and we will
fine-tune the currently available MT tools.
8
Limitations
The cost and time constraints limit our work
to only three language pairs. The sources of
gender biases in NLP are different such as the
8

--- Page 9 ---

nature of the language gender, unbalanced pro-
fessional names in the dataset, and gender un-
balanced pronouns in the dataset. This work
only focuses on unbalanced professional names.
9
Acknowledgments
We thank GRAIN for funding this work. We
also thank the linguistic experts who par-
ticipated in the annotation and translation
of the gender bias test dataset.
We thank
Hailay Teklehaymanot for his feedback on our
manuscript.
Finally, we thank the reviewers
for their extremely helpful remarks and feed-
back.
References
Alhafni,
Bashar,
Nizar
Habash,
and
Houda
Bouamor.
2022.
The arabic parallel gender
corpus 2.0: Extensions and analyses.
In Pro-
ceedings of the International Conference on Lan-
guage Resources and Evaluation (LREC 2022),
Marseille, France.
Barocas, Solon, Kate Crawford, Aaron Shapiro,
and Hanna Wallach. 2017. The problem with
bias: Allocative versus representational harms
in machine learning. In 9th Annual conference
of the special interest group for computing, in-
formation and society.
Blodgett, Su Lin, Solon Barocas, Hal Daumé III,
and Hanna Wallach. 2020a. Language (technol-
ogy) is power: A critical survey of” bias” in nlp.
arXiv preprint arXiv:2005.14050.
Blodgett, Su Lin, Solon Barocas, Hal Daumé Iii,
and Hanna Wallach. 2020b. Language (Tech-
nology) is Power: A Critical Survey of “Bias” in
NLP. ACL Anthology, pages 5454–5476, July.
Cho, Won Ik, Ji Won Kim, Seok Min Kim, and
Nam Soo Kim. 2019. On measuring gender bias
in translation of gender-neutral pronouns. arXiv
preprint arXiv:1905.11684.
Crawford, Kate. 2017. The trouble with bias.
Habash, Nizar, Houda Bouamor, and Christine
Chung. 2019. Automatic gender identification
and reinflection in arabic. In Proceedings of the
First Workshop on Gender Bias in Natural Lan-
guage Processing, pages 155–165.
Kadaoui,
Karima,
Samar
M
Magdy,
Abdul
Waheed,
Md
Tawkat
Islam
Khondaker,
Ahmed Oumar El-Shangiti,
El Moatez Bil-
lah Nagoudi, and Muhammad Abdul-Mageed.
2023. Tarjamat: Evaluation of bard and chatgpt
on machine translation of ten arabic varieties.
arXiv preprint arXiv:2308.03051.
Pei,
Jiaxin,
Aparna
Ananthasubramaniam,
Xingyao Wang, Naitian Zhou, Apostolos Dede-
loudis, Jackson Sargent, and David Jurgens.
2022. POTATO: The portable text annotation
tool. In Che, Wanxiang and Ekaterina Shutova,
editors, Proceedings of the 2022 Conference
on Empirical Methods in Natural Language
Processing: System Demonstrations, pages 327–
337, Abu Dhabi, UAE, December. Association
for Computational Linguistics.
Popović, Maja. 2017. chrf++: words helping char-
acter n-grams. In Proceedings of the second con-
ference on machine translation, pages 612–618.
Post, Matt. 2018. A call for clarity in reporting
bleu scores. arXiv preprint arXiv:1804.08771.
Prates, Marcelo OR, Pedro H Avelar, and Luís C
Lamb. 2020. Assessing gender bias in machine
translation: a case study with google translate.
Neural Computing and Applications, 32:6363–
6381.
Puduppully, Ratish, Raj Dabre, Ai Ti Aw, and
Nancy F Chen.
2023.
Decomposed prompt-
ing for machine translation between related lan-
guages using large language models.
arXiv
preprint arXiv:2305.13085.
Renduchintala, Adithya, Denise Díaz, Kenneth
Heafield, Xian Li, and Mona Diab. 2021. Gen-
der bias amplification during Speed-Quality op-
timization in Neural Machine Translation. ACL
Anthology, pages 99–109, August.
Savoldi, Beatrice, Marco Gaido, Luisa Bentivogli,
Matteo Negri, and Marco Turchi. 2021. Gen-
der bias in machine translation. Transactions of
the Association for Computational Linguistics,
9:845–874.
Sharma, Shanya, Manan Dey, and Koustuv Sinha.
2022. How sensitive are translation systems to
extra contexts? mitigating gender bias in neu-
ral machine translation models through relevant
contexts.
In Findings of the Association for
Computational Linguistics: EMNLP 2022, pages
1968–1984, Abu Dhabi, United Arab Emirates,
Dec. Association for Computational Linguistics.
Stanovsky, Gabriel, Noah A Smith, and Luke
Zettlemoyer.
2019.
Evaluating
gender
bias in machine translation.
arXiv preprint
arXiv:1906.00591.
Talat, Zeerak, Aurelie Neveol, Stella Biderman,
Miruna Clinciu,
Manan Dey,
Shayne Long-
pre, Sasha Luccioni, Maraim Masoud, Margaret
Mitchell, Dragomir Radev, Shanya Sharma, Ar-
jun Subramonian, Jaesung Tae, Samson Tan,
Deepak Tunuguntla, and Oskar Van Der Wal.
2022.
You reap what you sow: On the Chal-
lenges of Bias Evaluation Under Multilingual
Settings. ACL Anthology, pages 26–41, May.
9

--- Page 10 ---

Team, NLLB, Marta R. Costa-Jussà, James Cross,
Onur Çelebi, Maha Elbayad, Kenneth Heafield,
Kevin Heffernan, Elahe Kalbassi, Janice Lam,
Daniel Licht, Jean Maillard, Anna Sun, Skyler
Wang, Guillaume Wenzek, Al Youngblood, Bapi
Akula, Loïc Barrault, Gabriel Mejía González,
Prangthip Hansanti,
John Hoffman,
Semar-
ley Jarrett,
Kaushik Ram Sadagopan,
Dirk
Rowe,
Shannon Spruit,
Chau Tran,
Pierre
Andrews, Necip Fazil Ayan, Shruti Bhosale,
Sergey Edunov,
Angela Fan,
Cynthia Gao,
Vedanuj Goswami, Francisco Guzmán, Philipp
Koehn, Alexandre Mourachko, Christophe Rop-
ers, Safiyyah Saleem, Holger Schwenk, and Jeff
Wang.
2022.
No language left behind: Scal-
ing human-centered machine translation. arXiv
preprint arXiv:2207.04672.
Wairagala,
Eric
Peter,
Jonathan
Mukiibi,
Jeremy
Francis
Tusubira,
Claire
Babirye,
Joyce Nakatumba-Nabende, Andrew Katumba,
and Ivan Ssenkungu. 2022. Gender bias evalua-
tion in luganda-english machine translation. In
Proceedings of the 15th biennial conference of
the Association for Machine Translation in the
Americas (Volume 1:
Research Track), pages
274–286.
10
Appendix
10.1
Appendix: Human-level Evaluation
Guideline
Hello everyone,
We are excited to invite you to participate
in an important evaluation task aimed at as-
sessing gender bias in Google Translation from
English into Amharic, Afaan Oromoo, and
Tigrinya.
As well as, to evaluate the qual-
ity of the overall translation, you are asked to
evaluate the translation issue of the whole sen-
tence and whether there is an issue with profes-
sional name translation only. As an evaluator,
your valuable insights will help us ensure that
translations accurately reflect gender inclusiv-
ity and professionalism. By carefully reviewing
each sentence pair and considering both gender
specification and professional terminology, you
will play a pivotal role in enhancing translation
quality. Your diligent efforts in evaluating 400
sentences will contribute to creating more in-
clusive and accurate translations. Thank you
for your time and cooperation in this endeavor.
Let’s work together to promote fairness and ac-
curacy in translation.
Evaluation Task:
Gender Bias in Google
Translation from English into Amharic, Afaan
Oromoo, and Tigrinya
1. Login Credentials: Use the provided user-
name and password to access the evalua-
tion platform.
2. Accessing the Task: Open the designated
link on your preferred device, whether mo-
bile or computer.
3. Evaluation Procedure:
• Reviewing Sentences:
Carefully ex-
amine
each
provided
sentence
in
English
alongside
its
translation
into Amharic,
Afaan Oromoo,
or
Tigrinya.
• Identifying Gender Bias: Determine
the presence of gender bias by con-
sidering two factors:
– Gender Section: Assess whether
the translated gender (feminine or
masculine) aligns with the gender
specified in the original sentence.
– Professional
Words:
Check
if
professional terms are translated
with the same gender as provided
in the original sentence.
• Selecting Response:
Choose ”Yes,
there is gender bias” if bias is de-
tected, or ”No, gender bias in trans-
lation” if not.
• Evaluate the quality of translation:
Select the first check box “There is
an issue in translating the sentence”
if there is an issue in overall trans-
lation or/and select the second check
box “There is an issue in translating
the profession word”.
• Moving to Next Sentence: Click the
”Next” button after making your as-
sessment to proceed to the next set of
sentences.
4. Total Sentences: The evaluation task con-
sists of 400 sentences to be assessed.
5. Completion and Compensation:
Upon
completing the evaluation of all 400 sen-
tences, compensation will be provided ac-
cording to the prearranged agreement.
We appreciate your dedication and cooperation
in contributing to this evaluation task. Your
feedback is crucial for improving translation
quality and mitigating gender bias.
10

--- Page 11 ---

10.2
Appendix: List of Pronouns in English,
Amharic, Tigrinya, Afaan Oromoo
Table 3: Pronouns in English, Amharic, Tigrinya, and
Afaan Oromoo.
Key:
M=Masculine,
F=Feminine,
sg=singular,
pl=plural, R=Respect
English
Amharic
Tigrinya
Afaan Oromoo
I
እኔ(ǝne)
ኣነ(anä)
ana, na
We
እኛ(ǝñña)
ንሕና(nǝḥǝna)
nu
You (M. sg.)
አንተ(antä)
ንስኻ(nǝssǝxa)
You (F. sg.)
አንቺ(anči)
ንስኺ(nǝssǝxi)
You (sg.)
si
You (R)
እርስዎ(ərswo)
You (F, R)
ንሰን/ንስኽን(nsen/nskhn)
You (M, R)
ንሶም/ንስኹም(nsom/nskhum)
You (pl.)
እናንተ(ǝnnantä)
isin
You (M. pl.)
ንስኻትኩም(nǝssǝxatkum)
You (F. pl.)
ንስኻትክን(nǝssǝxatkǝn)
He
እሱ(ǝssu)
ንሱ(nǝssu)
isa
She
እሷ(ǝsswa)
ንሳ(nǝssa)
isii, ishii, isee, ishee
S/he (R)
እሳቸው(ǝssaččäw)
She (R)
ንሰን(nsen)
He (R)
ንሶም(nsom)
They
እነሱ(ǝnnässu)
isaan
They (M.)
ንሳቶም(nǝssatom)
They (F.)
ንሳተን(nǝssatän)
11

```
