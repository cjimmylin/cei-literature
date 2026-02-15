---
title: "2024-Clarke-GuyLingo The Republic of Guyana Creole Corpora - PDF Extract"
source_pdf: "2024-Clarke-GuyLingo The Republic of Guyana Creole Corpora.pdf"
pages: 7
extracted_at: "2026-02-15T17:51:55.991373"
---

# PDF Extract: 2024-Clarke-GuyLingo The Republic of Guyana Creole Corpora

**Source PDF:** 2024-Clarke-GuyLingo The Republic of Guyana Creole Corpora.pdf
**Total Pages:** 7

---

## Content

```
--- Page 1 ---

GuyLingo: The Republic of Guyana Creole Corpora
Christopher Clarke∗1,2
Roland Daynauth∗1,2
Charlene Wilkinson2
Hubert Devonish
Jason Mars1
1University of Michigan, Ann Arbor, MI
2University of Guyana, Georgetown, Guyana
{csclarke, daynauth, profmars}@umich.edu
{christopher.clarke, roland.daynauth, charlene.wilkinson}@uog.edu.gy
hubertsldevonish@gmail.com
Abstract
While major languages often enjoy substantial
attention and resources, the linguistic diversity
across the globe encompasses a multitude of
smaller, indigenous, and regional languages
that lack the same level of computational sup-
port. One such region is the Caribbean. While
commonly labeled as "English speaking", the
ex-British Caribbean region consists of a myr-
iad of Creole languages thriving alongside En-
glish. In this paper, we present GuyLingo:
a comprehensive corpus designed for advanc-
ing NLP research in the domain of Creolese
(Guyanese English-lexicon Creole), the most
widely spoken language in the culturally rich
nation of Guyana. We first outline our frame-
work for gathering and digitizing this diverse
corpus, inclusive of colloquial expressions, id-
ioms, and regional variations in a low-resource
language. We then demonstrate the challenges
of training and evaluating NLP models for ma-
chine translation in Creole. Lastly, we discuss
the unique opportunities presented by recent
NLP advancements for accelerating the formal
adoption of Creole languages as official lan-
guages in the Caribbean1.
1
Introduction
Major languages such as English and Chinese
frequently receive considerable attention and re-
sources due to their global prominence and eco-
nomic influence (Lent et al., 2021, 2022a). The
extensive focus on these major languages in natu-
ral language processing (NLP) has resulted in the
development of sophisticated models, extensive
datasets, and digital applications consumed by mil-
lions of users today. However, despite this global
prominence, the linguistic landscape of the globe
extends far beyond these dominant languages, en-
compassing a plethora of smaller, indigenous, and
1https://github.com/ChrisIsKing/
Caribbean-Creole-Languages-Translation
*Equal contribution.
Figure 1: Map of Guyana and its neighboring territories
regional languages that play crucial roles in the cul-
tural heritage and communication of their respec-
tive communities (Lent et al., 2022c; Hershcovich
et al., 2022). The countries of the Commonwealth
(ex-British) Caribbean Community represent an
example cluster of such countries.
Within the diverse linguistic tapestry of the
Caribbean Community, a rich array of languages
thrives, reflecting the historical, cultural, and ethnic
diversity of the region (Rickford, 1987; Holbrook
and Holbrook, 2001). While English is commonly
used as the official language in many Common-
wealth Caribbean states, the linguistic heritage goes
beyond just English, encompassing a variety of
Creole languages, indigenous languages, and in-
fluences from African, Indigenous, European, and
Asian languages (Devonish and Thompson, 2013).
Creole languages of the Caribbean emerged out
of the language contact between Europeans and
Africans arising from colonialism and plantation
slavery. These languages, such as Jamaican, oth-
erwise referred to as Jamaican Creole or Jamaican
Patois/Patwa (Armstrong et al., 2022), Trinidadian
arXiv:2405.03832v3  [cs.CL]  2 Jul 2024

--- Page 2 ---

Creole
English
“It luk laik nof ting cheenj op,” Seera se. “Somtaim mi doz get
fraikn.”
“So many things feel like they have changed,” said Sara. “I get
scared about it sometimes.”
When me lef’ han’ ’cratch me, money a-come
When my left hand itches, money is coming.
Di leedii prapa nais
The lady is very pretty
Table 1: Example Guyanese Creole from GuyLingo and its English Translation
Creole (Michaelis et al., 2013), and Haitian Creole
(Hewavitharana et al., 2011), have evolved as vi-
brant means of communication, showing language
features originating in West African languages as
well as the languages of the colonizing Europeans.
(Hagemeijer et al., 2014b).
Despite its prominence as the mother tongue of
the majority of the over 700,000 inhabitants of the
Republic of Guyana, Creolese (Guyanese English-
lexicon Creole) is a low-status vernacular language
that takes second place to the sole official language,
English. This is typical of local vernaculars in
post-colonial situations like Guyana (Hershcovich
et al., 2022). English has been traditionally the only
language in which Guyanese children are taught
to read and write in school. Written resources in
Creolese are limited, making it a low-resource lan-
guage within the field of Natural Language Pro-
cessing (NLP).
In this work, we introduce GuyLingo, a corpus
for Creolese curated for advancing NLP research
and development in Creole. Using this resource,
we explore the task of machine translation between
English and Creolese. To aid in this process we
design and implement the Guyanese Creole Trans-
lation tool2, a web-based GPT-powered machine
translation tool. Lastly, we briefly discuss the in-
sights gained from developing Guylingo alongside
considerations for accelerating the formal adoption
of Creole languages as official languages in the
Caribbean.
2
GuyLingo Corpus
This section describes the curation of GuyLingo, a
corpus of Creolese, the primary spoken language of
Guyana. The creation of this corpus aims to address
the scarcity of resources and attention devoted to
indigenous and regional languages within the NLP
community.
2.1
Data Collection
The compilation of GuyLingo requires the collect-
ing and digitizing of a series of linguistic resources.
2https://translation.csclarke.com
These sources should ideally encompass a spec-
trum of Creolese expressions, idiomatic phrases,
and regional variations. To ensure inclusivity and
authenticity, we employ a multi-pronged approach.
2.1.1
Expert Collaboration
In collaboration with the University of Guyana,
Guyanese Languages Unit, a collection of original
Guyanese Creole sources was curated, digitized,
and manually transcribed by a team of researchers.
Examples of this include Speirs (1902) a book of
Guyanese proverbs, containing over 1k culturally
rich proverbs from early British Guiana times still
used today, and Helen Patuck (2020) a COVID-
19 children’s book transcribed by Creolese experts
for primary education students. In addition, our
team of native Creole experts manually construct a
corpus of high-quality common Guyanese Creole
sayings and terms. Table 2 shows a full breakdown
of all information sources.
2.1.2
Online Resources
Whilst some of the aforementioned sources use the
consistent phonemic Cave-GLU standard writing
system (Cave, 1970) for creole, others do not. This
is particularly true for the many web-based sources
such as language forums, blogs, educational plat-
forms, etc., that contain small excerpts of colloqui-
alisms, everyday conversations, and idiomatic ex-
pressions prevalent in the Guyanese Creole. These
sources were scraped, cleaned, verified, and added
to GuyLingo as shown in 2.
2.2
Dataset Characteristics
GuyLingo encapsulates a diverse array of linguistic
data, including but not limited to:
• Conversational dialogues
• Idiomatic expressions and phrases
• Proverbs and folklore
• Regional variations and dialectical nuances
In total, GuyLingo consists of 2373 Guyanese
Creole sentences with a vocabulary size of 4177
unique Creole words.

--- Page 3 ---

Sources
Type
# Sentences
Vocab Size
Guyanese-Creole-English
Vocabulary-Basic
words.
(Polyglot Club, Accessed 2023)
Corpus
20
71
Guyanese Creole. (Wikipedia, Accessed 2023)
Article
6
28
Gender and Pronominal Variation in an Indo-Guyanese
Creole-Speaking (Sidnell, 1999)
Journal Article
21
82
Review of Guyanese Creole English (Guy, Accessed
2023)
Presentation
28
96
Guyanese Creole Survey Report. (Holbrook and Hol-
brook, 2001)
Language Survey
8
45
APiCS Online -Structure dataset. (Michaelis et al., 2013)
Report
344
351
Creolese. (Devonish and Thompson, 2013)
Journal Article
69
112
Habitual and Imperfective in Guyanese Creole. (Sidnell,
2002)
Journal Article
60
103
Tense and aspect in Guyanese Creole: A syntactic, se-
mantic and pragmatic analysis (Gibson, 1982)
PhD Thesis
231
374
Two areas of Guyanese Grammar (Guyanese Languages
Unit, 2016)
Article
14
26
Me Na Able: Creolese 101 (Letters from Guyana, 2017)
Blog
9
25
Travel Phrases - Guyanese Creole (Travel Phrases)
Blog
4
9
My Hero is you (Helen Patuck, 2020)
Educational
322
831
The Proverbs of British Guiana (Speirs, 1902)
Book
905
2054
Common Guyanese Creole Sayings (Manually created by
experts)
Corpus
332
712
Total
2373
4177
Table 2: Compilation of Guyanese Creole Language Resources: Sources, Type, Sentences, and Vocabulary Size
3
GuyLingo for Machine Translation
To investigate the utility of GuyLingo, we con-
duct experiments on the task of machine transla-
tion assessing the ability of NLP models to facili-
tate English←→Guyanese Creole translation. As
such to enable the training and evaluation of these
models GuyLingo was further expanded to include
English Creole translation pairs. Of the 2373 sen-
tences, the Common Guyanese Creole Sayings cor-
pus (expertly curated) was manually transcribed
into English. The remaining Creole sources were
extracted alongside their English translations. In
addition, 339 common Creole terms from (Speirs,
1902) alongside their English pairs were extracted
and verified. Using these initial translation pairs,
the Guyanese Creole Translation Tool was built to
allow the initial translation of remaining sentences
in GuyLingo. Of the remaining Creole sources,
the largest source of Creolese data from Speirs
(1902) contained no English translations for the
proverbs. As such, using the translation tool these
proverbs were machine translated. These machine
translations were reviewed and edited for lexical
correspondence but not semantic meaning given the
complexity of translating the contextual meaning
of cultural proverbs.
Figure 2: User Interface of Guyanese Creole Translation Tool.
This tool allows experts to rapidly and iteratively create trans-
lation pairs using GPT-4 (OpenAI, 2023) as a generator.
3.1
Guyanese Creole Translation Tool
The Guyanese Creole Translation tool, as shown
in figure 2, is a web-based application built using
Django+React to facilitate easy storing, editing,
and iterative testing of English Creole translations.
The UI allows Creolese experts to easily enter text
in English or Creole and get a sample translation.
We utilize GPT-4 (OpenAI, 2023) to automatically
perform these translations. The advanced prompt
includes a subset of example verified translations
from GuyLingo as in-context examples for gener-
ation. Once prompted, the user can modify the
generated output before saving it to the database.

--- Page 4 ---

Model
Bleu
Rouge1
Rouge2
RougeL
Meteor
CHRF
GPT-4 (Zero-shot)
1.35
17.22
2.4
17.0
12.55
21.68
GPT-4 (Few-shot)
1.64
20.6
3.42
20.2
14.56
22.32
T5-Large
09.74
37.44
13.74
36.63
28.19
30.09
Bart-Large
12.11
40.56
18.47
39.64
32.77
33.21
Bart-Base
10.17
37.49
16.08
36.59
29.54
29.47
Pegasus-Large
02.67
24.15
05.30
23.16
16.38
19.69
Table 3: Performance of MT Models on English-Creole
Translation
Users also have the option to modify the advanced
prompts as well as provide more seed examples for
greater control over the translation process. For
instance, users can provide a Guyanese proverb
and instruct GPT4 to consider the nuances of the
Guyanese culture while translating the text. As
mentioned previously, a subset of GuyLingo’s En-
glish pairs was generated using this tool.
Translation Dataset Statistics
In total, our trans-
lation dataset consists of 1969 total translation
pairs. For training and evaluation, we use the 302
manually curated translation pairs for testing and
the remaining GuyLingo translation pairs for model
training. The manually curated translation pairs are
all written in the Cave-GLU standard phonemic
system for Creoles (Cave, 1970).
3.2
Experiment Setup
Training and Models
We consider the models of
T5 (Raffel et al., 2023), BART (Lewis et al., 2020)
and Pegasus (Zhang et al., 2020) for their demon-
strated performance on several machine translation
tasks. All models were implemented with PyTorch
and Hugging Face Transformers. We train all mod-
els with AdamW (Loshchilov and Hutter, 2019)
and a weight decay of 0.01. We use a learning
rate of 2e-5, batch size of 4, and a linear learning
rate warmup over the first 10% steps with a cosine
schedule. We pre-process the data and train all
models with varying random seeds over multiple
runs for 10 epochs. Approximately 200 GPU hours
were required to train all hyperparameter variations
across all tasks. Additionally, we evaluate the per-
formance of GPT-4 using in-context learning on
GuyLingo.
Evaluation
For evaluation metrics, we adopted
common automatic evaluation methods used for
language generation based on n-gram overlap:
BLEU (Papineni et al., 2002), ROUGE (Lin, 2004),
METEOR (Banerjee and Lavie, 2005) and CHRF
(Popovi´c, 2015).
Model
Bleu
Rouge1
Rouge2
RougeL
Meteor
CHRF
GPT-4 (Zero-shot)
29.8
60.4
38.25
58.96
52.94
51.33
GPT-4 (Few-shot)
30.24
60.6
39.31
58.99
54.14
51.61
T5-Large
19.70
47.71
26.99
46.47
42.45
39.89
Bart-Large
17.70
45.74
24.41
39.75
32.77
37.23
Bart-Base
14.20
41.68
20.04
40.40
35.95
34.33
Pegasus-Large
6.10
28.96
09.88
27.91
22.53
23.72
Table 4: Performance of MT Models on Creole-English
Translation
4
Results
Table 3 and 4 summarize our evaluation results on
automated metrics. For en-creole translation, our
results show that the Bart-Large model achieves the
best performance amongst all models with a BLEU
score of 12.11, ROUGE-1 score of 40.56, ROUGE-
2 score of 18.47, ROUGE-L score of 39.64, ME-
TEOR score of 32.77 and a CHRF score of 33.21
outperforming other fine-tuned models such as T5
and large language models such as GPT-4 both in
zero and few-shot prompting settings. The perfor-
mance of en-creole translation is due to a couple of
factors: 1) Incoherent English to Creole mapping:
Many unique words/phrases found in Creole do not
contain English equivalents. 2) Writing System
of Testing set: The Creolese Cave-GLU writing
system (Cave, 1970) used by the manually curated
testing set is phonemic whereby a particular sound
is always represented by one letter/letter combina-
tion. GuyLingo’s training data, however, contains
samples where multiple letter/letter combinations
represent one sound. Thus, the chance of an error
is much higher for en-creole translations.
For creole-eng translation, GPT-4 (Few-shot) us-
ing a subset of GuyLingo training set as in-context
learning examples delivers the best performance
with a BLEU score of 30.24. a ROUGE-1 score
of 60.6, a ROUGE-2 score of 39.31, a ROUGE-L
score of 58.99, a METEOR score of 54.14, and a
CHRF score of 51.61. This result highlights the
power of GPT-4’s large and extensive training on
a diverse and extensive range of text data in addi-
tion to its ability to quickly adapt to new tasks or
language pairs with only a few examples.
5
Discussion
In this section, we briefly discuss the unique op-
portunity presented by recent NLP advancements
for accelerating the formal adoption of Creole lan-
guages in the Caribbean.

--- Page 5 ---

Figure 3: Conversational Agent in Whatsapp speaking in
Guyanese Creole.
5.1
AI-Driven Applications for Native
Languages
One of the major issues affecting the formal adop-
tion is Creolese despite its prominence as a spoken
language is its lack of use in formal communica-
tion outlets such as literature, news, and written
texts. AI-driven applications fueled by rich data
sources such as GuyLingo present a major oppor-
tunity for enabling the development of educational
content, legal documents, and official communi-
cations in Creolese. Figure 3 showcases a con-
versational AI Assistant named IRIS 3 deployed
to citizens of Guyana speaking in Creolese using
GuyLingo. Such applications present the ability to
make Creolese more accessible and applicable in
various formal contexts further allowing citizens
to feel empowered and foster a sense of national
pride.
6
Related Works
In the context of linguistic diversity, prior works
(Hershcovich et al., 2022; Lent et al., 2021, 2022a)
have highlighted the challenges faced by lesser-
known languages, emphasizing the importance of
recognition and preservation. Works such as Dabre
and Sukhoo (2022), Hagemeijer et al. (2014a), and
Liu et al. (2022) have contributed to advancing
NLP research in Creole languages by building a
corpus of text for various Creole languages, foster-
ing machine translation, and enhancing language
modeling techniques specific to these linguistic va-
rieties. Our work falls into this category. On the
other hand, works such as Lent et al. (2022b) and
Lent et al. (2022c) emphasize the importance of
linguistic diversity by documenting the challenges
and exploring the complexities of language mod-
eling for underrepresented languages. The juxta-
position of these studies with the dominance of
major languages in NLP underscores the need for
3https://fb.watch/rbtO5Wocny/
more inclusive research efforts that consider the lin-
guistic richness and cultural significance of smaller,
indigenous languages within global technological
advancements.
7
Conclusion
In this paper, we introduce GuyLingo, a corpus of
Guyanese Creolese designed to facilitate advance-
ments in NLP research. We discuss the process of
gathering and digitizing this diverse corpus while
highlighting the unique opportunities presented by
recent NLP advancements for accelerating the for-
mal adoption of Creole languages in the Caribbean.
By providing access to a rich collection of collo-
quial language expressions, idioms, and regional
variations, we hope to encourage further research
in this field and improve the representation and
understanding of Creole languages in NLP.
8
Limitations
While our work aims to contribute to the advance-
ment of NLP for Creole, several limitations arise:
Limited Representation:
Guyana is home
to many languages outside of Creolese such as
Wapichan, Makushi, Wai Wai, Akawaio, Arekuna,
Patamuna, Kalina (Carib), Warrau, and Lokono to
name a few. Given the cultural significance of these
languages, future research should prioritize their
inclusion to ensure a more inclusive and represen-
tative dataset. Additionally, The rich tapestry of
languages in the region extends beyond Guyanese
Creole, and efforts should be made to include ad-
ditional Creole languages and dialects for a more
comprehensive understanding.
Limited Generalizability: The findings and in-
sights gained from our work, particularly regarding
the formal adoption of Creole languages, may have
limited generalizability to other regions or linguis-
tic contexts.
Language Evolution: Creole languages, by
their nature, are dynamic and subject to continuous
evolution. The static nature of a curated corpus
and machine translation models may not fully cap-
ture the evolving linguistic landscape, necessitating
regular updates and adaptations to reflect current
linguistic usage.
Acknowledgements
We thank our anonymous reviewers for their feed-
back and suggestions. This work is supported in

--- Page 6 ---

part by the North American Chapter of the Asso-
ciation for Computational Linguistics (NAACL)
Regional Americas Fund. 4
References
Accessed 2023. Guyanese creole english. Accessed on
December 14, 2023.
Ruth-Ann Armstrong, John Hewitt, and Christopher
Manning. 2022. JamPatoisNLI: A jamaican patois
natural language inference dataset. In Findings of the
Association for Computational Linguistics: EMNLP
2022, pages 5307–5320, Abu Dhabi, United Arab
Emirates. Association for Computational Linguistics.
Satanjeev Banerjee and Alon Lavie. 2005. METEOR:
An automatic metric for MT evaluation with im-
proved correlation with human judgments. In Pro-
ceedings of the ACL Workshop on Intrinsic and Ex-
trinsic Evaluation Measures for Machine Transla-
tion and/or Summarization, pages 65–72, Ann Arbor,
Michigan. Association for Computational Linguis-
tics.
George N. Cave. 1970. Some sociolinguistic factors
in the production of standard language in guyana
and implications for the language teacher. Language
Learning, 20(2):249–263.
Raj Dabre and Aneerav Sukhoo. 2022.
Kreol-
morisienmt: A dataset for mauritian creole machine
translation. In Findings of the Association for Com-
putational Linguistics: AACL-IJCNLP 2022, pages
22–29.
Hubert Devonish and Dahlia Thompson. 2013. Cre-
olese. In Susanne Maria Michaelis, Philippe Mau-
rer, Martin Haspelmath, and Magnus Huber, editors,
The Survey of Pidgin and Creole Languages, Vol. I:
English-based and Dutch-based languages, pages
49–60. Oxford University Press, Oxford.
Kean Amelia Gibson. 1982.
Tense and aspect in
Guyanese Creole: A syntactic, semantic and prag-
matic analysis. Ph.D. thesis, University of York.
Guyanese
Languages
Unit.
2016.
Two
areas
of
guyanese
grammar.
https:
//guyaneselanguagesunit.com/2016/07/12/
two-areas-of-guyanese-grammar/. Accessed on
December 14, 2023.
Tjerk Hagemeijer, Michel Généreux, IHE Hendrickx,
Amália Mendes, Abigail Tiny, and Armando Zamora.
2014a. The gulf of guinea creole corpora.
Tjerk Hagemeijer, Michel Généreux, Iris Hendrickx,
Amália Mendes, Abigail Tiny, and Armando Zamora.
2014b.
The Gulf of Guinea creole corpora.
In
Proceedings of the Ninth International Conference
4https://www.aclweb.org/portal/content/
naacl-regional-americas-fund-cfp-2023
on Language Resources and Evaluation (LREC’14),
pages 523–529, Reykjavik, Iceland. European Lan-
guage Resources Association (ELRA).
Helen Patuck. 2020.
My Hero is You: How Kids
Can Fight COVID-19! https://www.unicef.org/
coronavirus/my-hero-you. Accessed on: Insert
Date Accessed.
Daniel Hershcovich, Stella Frank, Heather Lent,
Miryam de Lhoneux, Mostafa Abdou, Stephanie
Brandl, Emanuele Bugliarello, Laura Cabello Pi-
queras, Ilias Chalkidis, Ruixiang Cui, Constanza
Fierro, Katerina Margatina, Phillip Rust, and An-
ders Søgaard. 2022. Challenges and strategies in
cross-cultural nlp.
Sanjika Hewavitharana, Nguyen Bach, Qin Gao, Vamshi
Ambati, and Stephan Vogel. 2011. CMU Haitian
Creole-English translation system for WMT 2011.
In Proceedings of the Sixth Workshop on Statisti-
cal Machine Translation, pages 386–392, Edinburgh,
Scotland. Association for Computational Linguistics.
David
J
Holbrook
and
Holly
A
Holbrook.
2001.
Guyanese
creole
survey
report.
https://www.sil.org/resources/archives/9001.
Heather
Lent,
Emanuele
Bugliarello,
Miryam
de Lhoneux, Chen Qiu, and Anders Søgaard. 2021.
On language models for creoles. In Proceedings of
the 25th Conference on Computational Natural Lan-
guage Learning, pages 58–71, Online. Association
for Computational Linguistics.
Heather Lent, Emanuele Bugliarello, and Anders Sø-
gaard. 2022a. Ancestor-to-creole transfer is not a
walk in the park. In Proceedings of the Third Work-
shop on Insights from Negative Results in NLP, pages
68–74, Dublin, Ireland. Association for Computa-
tional Linguistics.
Heather Lent, Emanuele Bugliarello, and Anders Sø-
gaard. 2022b. Ancestor-to-creole transfer is not a
walk in the park. arXiv preprint arXiv:2206.04371.
Heather Lent, Kelechi Ogueji, Miryam de Lhoneux, Ore-
vaoghene Ahia, and Anders Søgaard. 2022c. What a
creole wants, what a creole needs. In Proceedings of
the Thirteenth Language Resources and Evaluation
Conference, pages 6439–6449, Marseille, France. Eu-
ropean Language Resources Association.
Letters from Guyana. 2017.
Me na able - creolese
101.
https://lettersfromguyana.wordpress.
com/2017/01/29/me-na-able-creolese-101/.
Accessed on December 14, 2023.
Mike Lewis, Yinhan Liu, Naman Goyal, Marjan
Ghazvininejad, Abdelrahman Mohamed, Omer Levy,
Veselin Stoyanov, and Luke Zettlemoyer. 2020.
BART: Denoising sequence-to-sequence pre-training
for natural language generation, translation, and com-
prehension. In Proceedings of the 58th Annual Meet-
ing of the Association for Computational Linguistics,
pages 7871–7880, Online. Association for Computa-
tional Linguistics.

--- Page 7 ---

Chin-Yew Lin. 2004. ROUGE: A package for auto-
matic evaluation of summaries. In Text Summariza-
tion Branches Out, pages 74–81, Barcelona, Spain.
Association for Computational Linguistics.
Zhengyuan Liu, Shikang Ni, Aiti Aw, and Nancy Chen.
2022. Singlish message paraphrasing: A joint task
of creole translation and text normalization. In Pro-
ceedings of the 29th International Conference on
Computational Linguistics, pages 3924–3936.
Ilya Loshchilov and Frank Hutter. 2019. Decoupled
weight decay regularization. In International Confer-
ence on Learning Representations.
Susanne Maria Michaelis, Philippe Maurer, Martin
Haspelmath, and Magnus Huber, editors. 2013.
APiCS Online. Max Planck Institute for Evolutionary
Anthropology, Leipzig.
OpenAI. 2023. Gpt-4 technical report.
Kishore Papineni, Salim Roukos, Todd Ward, and Wei
jing Zhu. 2002. Bleu: a method for automatic evalu-
ation of machine translation. pages 311–318.
Polyglot
Club.
Accessed
2023.
Guyanese
creole
english
vocabulary
-
basic
words.
https://polyglotclub.com/wiki/Language/
Guyanese-creole-english/Vocabulary/
Basic-words.
Accessed
on
December
14,
2023.
Maja Popovi´c. 2015. chrF: character n-gram F-score
for automatic MT evaluation. In Proceedings of the
Tenth Workshop on Statistical Machine Translation,
pages 392–395, Lisbon, Portugal. Association for
Computational Linguistics.
Colin Raffel, Noam Shazeer, Adam Roberts, Katherine
Lee, Sharan Narang, Michael Matena, Yanqi Zhou,
Wei Li, and Peter J. Liu. 2023. Exploring the limits
of transfer learning with a unified text-to-text trans-
former.
John R Rickford. 1987. Dimensions of a creole con-
tinuum: History, texts, and linguistic analysis of
Guyanese Creole. Stanford University Press.
Jack Sidnell. 1999. Gender and pronominal variation in
an indo-guyanese creole-speaking community. Lan-
guage in Society, 28(3):367–399.
Jack Sidnell. 2002.
Habitual and imperfective in
guyanese creole. Journal of pidgin and creole lan-
guages, 17(2):151–189.
James Speirs. 1902. The Proverbs of British Guiana.
With an Index of Principal Words, an Index of Sub-
jects, and a Glossary. The Argosy Company, Demer-
ara.
Travel Phrases.
Guyanese phrases and basics.
http://www.travelphrases.info/languages/
guyanese.htm. Accessed on December 14, 2023.
Wikipedia. Accessed 2023. Guyanese creole. https://
en.wikipedia.org/wiki/Guyanese_Creole. Ac-
cessed on December 14, 2023.
Jingqing Zhang, Yao Zhao, Mohammad Saleh, and Pe-
ter J. Liu. 2020. Pegasus: Pre-training with extracted
gap-sentences for abstractive summarization.
A
Guyanese Creole Translation Tool
In this section, we further showcase the Guyanese
Creole Translation tool detailing our prompts and
user interface.
Translate the following Guyanese Creole text
and provide the resulting English translation.
Please ensure that the translation is clear and
accurate. Guyanese Creole is spoken in Guyana
and may include unique vocabulary and grammar.
Try to capture the original meaning while
making it comprehensible in English.
Glossary:
English: Swallow
Creole: Swalla
English: Stagger
Creole: 'Taggah
English: Stop-off
Creole: "Taff-aff
...
Translations
Translation 1: The beef cooked until it was soft
Text 1: Di biif kuk kuk kuk til ii saaf
Translation 2: But my grandfather had a boat
Text 2: Bo mi granfaada bin ga wan boot
Figure 4: Example GPT-4 Prompt with translation examples
from Speirs (1902).

```
