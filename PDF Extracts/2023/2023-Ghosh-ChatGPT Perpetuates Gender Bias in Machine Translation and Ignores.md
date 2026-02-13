---
title: "2023-Ghosh-ChatGPT Perpetuates Gender Bias in Machine Translation and Ignores - PDF Extract"
source_pdf: "2023-Ghosh-ChatGPT Perpetuates Gender Bias in Machine Translation and Ignores.pdf"
pages: 12
extracted_at: "2026-02-13T09:50:29.880467"
---

# PDF Extract: 2023-Ghosh-ChatGPT Perpetuates Gender Bias in Machine Translation and Ignores

**Source PDF:** 2023-Ghosh-ChatGPT Perpetuates Gender Bias in Machine Translation and Ignores.pdf
**Total Pages:** 12

---

## Content

```
--- Page 1 ---

ChatGPT Perpetuates Gender Bias in Machine Translation and
Ignores Non-Gendered Pronouns: Findings across Bengali and
Five other Low-Resource Languages
Sourojit Ghosh
University of Washington
Seattle, USA
ghosh100@uw.edu
Aylin Caliskan
University of Washington
Seattle, USA
aylin@uw.edu
ABSTRACT
In this multicultural age, language translation is one of the most
performed tasks, and it is becoming increasingly AI-moderated
and automated. As a novel AI system, ChatGPT claims to be pro-
ficient in such translation tasks and in this paper, we put that
claim to the test. Specifically, we examine ChatGPT’s accuracy
in translating between English and languages that exclusively use
gender-neutral pronouns. We center this study around Bengali,
the 7𝑡ℎmost spoken language globally, but also generalize our
findings across five other languages: Farsi, Malay, Tagalog, Thai,
and Turkish. We find that ChatGPT perpetuates gender defaults
and stereotypes assigned to certain occupations (e.g. man = doc-
tor, woman = nurse) or actions (e.g. woman = cook, man = go to
work), as it converts gender-neutral pronouns in languages to ‘he’
or ‘she’. We also observe ChatGPT completely failing to translate
the English gender-neutral pronoun ‘they’ into equivalent gender-
neutral pronouns in other languages, as it produces translations
that are incoherent and incorrect. While it does respect and pro-
vide appropriately gender-marked versions of Bengali words when
prompted with gender information in English, ChatGPT appears to
confer a higher respect to men than to women in the same occupa-
tion. We conclude that ChatGPT exhibits the same gender biases
which have been demonstrated for tools like Google Translate or
MS Translator, as we provide recommendations for a human cen-
tered approach for future designers of AIs that perform language
translation to better accommodate such low-resource languages.
CCS CONCEPTS
• Human-centered computing; • Computing methodologies
→Machine translation; Artificial intelligence; Natural language
processing; • Applied computing →Language translation;
KEYWORDS
ChatGPT, LLM, machine translation, gender bias, Bengali, human-
centered design
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full cita-
tion on the first page. Copyrights for components of this work owned by others than
ACM must be honored. Abstracting with credit is permitted. To copy otherwise, or re-
publish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
AIES ’23, August 08–10, 2023, Montreal, Quebec, Canada
© 2023 Association for Computing Machinery.
ACM ISBN 978-1-4503-XXXX-X/18/06…$15.00
https://doi.org/XXXXXXX.XXXXXXX
ACM Reference Format:
Sourojit Ghosh and Aylin Caliskan. 2023. ChatGPT Perpetuates Gender
Bias in Machine Translation and Ignores Non-Gendered Pronouns: Find-
ings across Bengali and Five other Low-Resource Languages. In Proceed-
ings of AAAI/ACM Conference on AI, Ethics, and Society (AIES ’23). ACM,
New York, NY, USA, 12 pages. https://doi.org/XXXXXXX.XXXXXXX
1
INTRODUCTION
The last months of 2022 saw the meteoric rise in popularity of what
has become one of the hottest AI tools of 2023 – ChatGPT1. Devel-
oped by OpenAI2 on the GPT-33 language model, the conversa-
tional agent set a record for the fastest growth since launch, ex-
ceeding 100 million new users in its first two months with over
13 million users per day in its first full month of operation [39] as
it has found usage in a wide range of both recreational and pro-
fessional domains. With such expansive usage, ChatGPT is might
be an upstart competitor and potential usurper of Google’s throne
as the go-to tool for general question-answering and information
seeking, with the New York Times calling it “the first notable threat
in decades” to Google’s near-monopoly in this space [36].
ChatGPT is trained on large corpora of publicly available data
and uses Reinforcement Learning from Human Feedback (RLHF),
whereby designers produce conversations where human AI train-
ers play both the user and the AI assistant. Such an approach opens
it up to the possibility of exhibiting biases and sterotypes that have
downstream ethical implications (though OpenAI claims that Chat-
GPT takes extensive measures towards bias mitigation [61]), as re-
searchers and journalists alike have warned [e.g., 7, 22, 37]. Such
calls necessitate a thorough examination of ChatGPT.
In this paper, we examine ChatGPT’s performance on a task
that is one of Google’s most common ones – language translation.
Specifically, we examine whether ChatGPT has learned from the
heavy criticism that Google has received for its insistence on gen-
dering words and occupations in English translations of words that
are gender-neutral in their original language [e.g., 34, 54, 67, 73].
Seeing as how this is a critical and well-established flaw within
Google Translate over the past half-decade, we believe that a com-
petitor should seek to rectify this in its tool.
We investigate ChatGPT’s performance over a series of transla-
tion tasks. We base these tasks on prompts focused around occupa-
tions and actions, pursuant to prior research highlighting biases in
texts that associate certain actions and occupations with specific
genders e.g. to be a doctor or to go to work is to be male, whereas
1https://openai.com/blog/chatgpt/
2https://openai.com/about/
3https://openai.com/blog/gpt-3-apps

--- Page 2 ---

AIES ’23, August 08–10, 2023, Montreal, Quebec, Canada
Ghosh and Caliskan.
to be a nurse or cook/clean is to be female [e.g., 14, 24, 32, 51, 65].
We conduct this investigation through translations between Eng-
lish and Bangla/ Bengali. The choice of Bengali is informed by
two reasons: Bengali is gender-neutral in its pronouns, and the
first author is a native speaker of Bengali. Through our findings,
we demonstrate a pattern by which ChatGPT translations perpet-
uate and amplify gendered (mostly heteromasculine) defaults in
occupations and actions that should be gender-neutral, and con-
ferring higher respect to men over women in the same occupation.
Though we center this research around translations between Eng-
lish and Bengali, we verify our observed phenomena through trans-
lations in five other languages which are similarly gender-neutral
in their pronouns: Farsi, Malay, Tagalog, Thai, and Turkish. These
languages are chosen because of their collective population of over
500 million people and because they all use gender-neutral pro-
nouns, which is important because we study gender biases/errors
that emerge in translations between English and these languages.
Our contributions are threefold: (1) We provide a comprehen-
sive demonstration of the persistence and amplification of gen-
der roles and stereotypes assosciated with actions and occupations
when ChatGPT translates into English sentences which do not pro-
vide any gender information in their source languages, as we demon-
strate that ChatGPT’s reinforcement learning strategy does not
handle bias mitigation in machine translation which has signifi-
cant implications on perpetuating bias and shaping human cog-
nition about who should be a doctor and who should be a nurse,
among other occupations. We exemplify the insertion of binary
genders into instances where the non-binary pronoun would have
been most appropriate, and the failure to translate the English
gender-neutral pronoun ‘they’ into gender-neutral pronouns in
other languages which threatens to erase non-binary and trans
identities in downstream tasks. We present one of the first stud-
ies of language translation tasks performed by ChatGPT (the only
other being [42]), and generally one of the first studies about Chat-
GPT. Given its popularity and usage, it is important to extensively
study ChatGPT and its potential to perpetuate negative biases and
stereotypes,and our study is important in starting this conversa-
tion within academic circles. (2) We conduct our study in Ben-
gali, the 7𝑡ℎmost spoken language in the world [12] (over 337
million people [31]). Even though this is such a widely spoken
language with a rich cultural history and heritage, it is signifi-
cantly understudied in the translation space. It has only tangen-
tially been studied in [65], and by non-speakers of Bengali. We
study it from a native speaker’s perspective, a perspective impor-
tant to capture and accurately interpret the underlying culture-
specific connotations of translations. (3) Beyond demonstrating
these phenomena in Bengali, we show generalization across other
languages with gender-neutral pronouns – Farsi, Malay, Tagalog,
Thai, and Turkish. Such generalization across multiple languages
is not commonly examined in the same single study (with the ex-
ception of [65]). In these cases, we only study translations into Eng-
lish, because English is the highest-resource language of all these
based on the training data ChatGPT uses. We definitively demon-
strate ChatGPT perpetuating gender stereotypes and inserting an
inferred gender based on actions and occupations into sentences
that are designed to be gender neutral in their languages of origin,
languages which are classified as ‘low-resource’ in the AI space
[23]. We demand stronger performance for such languages that
adequately respects their prevalence in the world and accommo-
dates the billions who collectively speak them.
2
BACKGROUND
2.1
Gender in Languages and Translations
Global languages have several similarities and differences when
evaluated across a variety of properties, and one such property is
how they handle gender. Some languages contain grammatical
gender, whereby nouns are classified with genders [25]. Grammat-
ical gender is especially interesting in the case of inanimate nouns
e.g. in English, a language without grammatical gender, the sun
is genderless whereas in Hindi, a language that uses grammatical
gender, it is considered masculine. Linguists [e.g., 25, 46] largely
believe that assignment of grammatical gender within languages
evolved over time in arbitrary patterns unique to each language.
Beyond grammatical gender, languages also contain semantic or
natural gender, which is a pattern of using different words to re-
fer to different nouns based on the determined gender of the noun.
For instance, in English we refer to male cattle as ‘bulls’ and fe-
male cattle as ‘cows’. Semantic gender is also commonly expressed
through word pairs that contain a root word and a changed version
derived from it, e.g. the feminine word ‘lioness’ in English is de-
rived from the masculine ‘lion’ by adding the suffix ‘-ess’. This
is known as markedness [40], where the root word is said to be
‘unmarked’. Historically, most gendered pairs of nouns are such
that the masculine noun is unmarked, and femininity is denoted
by somehow marking the masculine [e.g., 6, 40, 78].
Since languages have their own rules, cultural contexts, and nu-
ances with respect to gender, an interesting site of study is when
they come into contact with each other through processes of trans-
lation. Language translation is complicated, and must be done with
a good understanding of the rules of both source and destination
languages [75]. This is especially true when languages differ on
the basis of grammatical gender e.g. when translating the sen-
tence ‘The sun was shining but the river was cold’ from grammat-
ically gender-neutral English to grammatically gendered Hindi, it
is important to know that ‘sun’ should be masculine-gendered and
‘river’ should be feminine-gendered, which would in turn influence
the nature of the Hindi phrases of the verbs ‘was shining’ (in this
case, ‘चमकरहाथा') and ‘was cold’ (in this case, ‘ठंडीथी').
Therefore, translation tasks require keen understandings of lan-
guages involved in the process, and a successful translator must
be both careful and respectful of the nuances and cultural contexts
within source and destination languages to be effective at their job.
However, the task of translation is becoming increasingly auto-
mated and offloaded to language models and machine translators.
2.2
Language Models and Datasets in
Translation Tasks
Large-scale language models have become ubiquitous across a va-
riety of domains, in tasks such as sentiment analysis [e.g., 3, 38, 50],
natural language interpretation [e.g., 28, 43, 58], plagiarism detec-
tion [e.g., 4, 53, 64], content recommendation [e.g., 41, 72, 79], con-
tent moderation [e.g., 62, 74, 80], misinformation identification and

--- Page 3 ---

ChatGPT Perpetuates Gender Bias in Machine Translation and Ignores Non-Gendered Pronouns: Findings across Bengali and Five other Low-Resource Languages
AIES ’23, August 08–10, 2023, Montreal, Quebec, Canada
retrieval [e.g., 21, 76, 77], and so many more. However, such lan-
guage models are known to contain a variety of negative biases,
such as religious bias [e.g., 1, 57], gender bias [e.g., 10, 52], and so-
cial and occupational biases [e.g., 44, 49], as they perpetuate harm-
ful and disadvantaging historical injustices.
Within the context of language translation, Brown et al. [13]
and Och and Ney [60] developed the computational foundations
for machine translation. Such models might be trained either on
unlabeled monolingual corpora [e.g., 11] or labeled and translated
texts [e.g., 48]. Common approaches of using language models in
translation tasks involve using feed-forward Neural probabilistic
language models [70] or RNN-based models [55]. Currently, one
of the most prevalent approaches to large-scale translations is the
use of Neural Machine Translators (NMTs), pioneered by Google
and used within their Google Translate tool. Since their inception,
NMTs are considered the state-of-the-art solution in the field.
Like in other ML contexts, the accuracy of machine translations
often depends on the quantity and quality of training data the lan-
guage models have access to, with increases in accuracy generally
being correlated to increased quality of data [45]. Within collect-
ing multilingual data, a common approach is to mine parallel texts
in multiple languages, such as different languages of the Bible [26],
and then applying similarity measures to determine parallelisms at
the sentence level [71]. It is at this level of data collection and avail-
ability that languages are differentiated between, because some
languages (such as English or other European languages) have vast
corpora of text data or are selected for mining [e.g., 30], creating a
massive gulf with other languages for whom labeled parallel or bi-
textual data are sparse in publicly available datasets [35]. Such lan-
guages that have low coverage or are underrepresented in global
datasets are known as low-resource languages [23]. Because of this
gulf in data availability, translations in the context of low-resource
languages are generally poorer than high-resource languages.
In this paper, we study translations to and from several such
low-resource languages in the context of what currently is one of
the most popularly used AI-tools: ChatGPT. At the outset, it is
important to recognize that ChatGPT, or its underlying ML model
GPT-3, was designed as a Generative AI and not a translation tool.
As an LLM, GPT-3 is capable of translation tasks without neces-
sarily being optimal at them. However, it is important to study
ChatGPT and GPT-3 in the context of language translation given
the prominent evidence of translation fails by dedicated tools such
as Google Translate or MS Translator (detailed in the next sec-
tion) and the large public uptake of ChatGPT into a wide range
of tasks beyond its initial design goals. Though research in this
field is sparse given the novelty of the tool [42], we believe this
present study to be critical, considering how several millions of
users might use or are already using ChatGPT as a translation tool.
2.3
Biases and Errors related to Gender
Pronouns in Machine Translations
That machine translators make errors and exhibit biases in con-
text of gender when translating between languages with different
gender rules has been well established both in common usage and
literature. Such criticism has been levied against popular transla-
tion tools such as Google Translate [e.g., 32, 65] and MS Translator
[e.g., 67, 73], especially in the context of English translation.
Such gender bias is displayed in several ways. Firstly, it is ev-
ident in patterns of nouns (e.g.
doctor = male), pronouns and
verbs (e.g. cooking = female) to which machine translators as-
sign male or female gender. A study of 74 Spanish nouns revealed
that an overwhelming majority of those were assigned male pro-
nouns in English translation while only 4 were deemed to be fe-
male [51]. Closer inspection reveals that occupations such as doc-
tors, engineer and president are often assigned male pronouns,
whereas those such as dancer, nurse, and teacher are often denoted
as female [65]. Secondly, genderization occurs towards verbs, as
actions like cooking and cleaning are assosciated with women while
reading and eating were assigned male [32].
Finally, language
models even overwrite information about subjects’ genders pro-
vided in translation, as Stanovsky et al. [73] demonstrated an Eng-
lish sentence about a female doctor receiving a machine translation
into Spanish that classified them as male. While these examples
are in high-resource languages such as English and Spanish, the
problem is exacerbated in low-resource languages, such as Turk-
ish [e.g., 24], Malay [e.g., 65], Tagalog [e.g., 32] and others. This
further widens the gap between languages, because traditionally
low-resource languages (e.g. most Asian languages) deal with gen-
der differently than high-resource languages (e.g. Romance lan-
guages), leading to increased translation errors [69].
Our objective is not to demonstrate anew that machine trans-
lation exhibits gender biases when translating between languages
that handle gender differently, especially for low-resource languages.
Rather, this paper intends to show that the phenomenon persists
in the latest most popular and state of the art tool, and that devel-
opers have failed to address it despite the knowledge in the field,
despite claiming that they mitigate biases in their design [61].
3
METHODS
3.1
Author Linguistic Positionality
The first author is fluent in Bengali, having grown up in Bengal (In-
dia) for 18 years speaking the language. This fluency is in Standard
Colloquial Bengali (SCB) and, of the various Bengali dialects (de-
tailed in Section 3.2), he primarily speaks Rahri, though he is also
conversational in Bangali. He also speaks Hindi and Urdu fluently.
3.2
Translating to/from Bengali
Bengali/Bangla is the 7𝑡ℎ-most spoken language in the world [12],
with an estimated 300 million people speaking it as their mother
tongue and almost 37 million second-language speakers [31]. Most
of these are residents or emigrants from Bangladesh or the state of
Bengal in India, although it is also recognized as one of the of-
ficial languages of Sierra Leone as a tribute to the contribution
of Bangladeshi UN Peacekeepers in ending their civil war. It has
several dialects, such as Bangali, Rahri, Varendri, Rangpuri, Shan-
tipuriya, Bikrampuri, Jessoriya, Barisali, and Sylheti [20]. Such di-
alects are primarily spoken, as the majority of the written Bengali
in India is in Standard Colloquial Bengali (SCB) [56], a standard-
ized version of the language that is perhaps the closest to Rahri.

--- Page 4 ---

AIES ’23, August 08–10, 2023, Montreal, Quebec, Canada
Ghosh and Caliskan.
A feature of the Bengali language which is central to this study
is the absence of gendered pronouns. While English uses the gen-
dered pronouns ‘he’/‘she’ and the gender-neutral pronoun ‘they’,
pronouns in Bengali are gender-neutral. The three most used pro-
nouns in Bengali are েস(pronounced ‘shey’), ও(pronounced ‘o’)
and িতিন(pronounced ‘teeni’ with a soft t). While েসand ওcan be
used to refer to anyone, িতিনis used to refer to respected people.
Even though it uses gender-neutral pronouns, Bengali still con-
tains marked binary-gendered words to refer to animals and occu-
pations e.g. lion/lioness (িসংহ/িসংহী), tiger/tigress (বাঘ/বািঘনী),
and actor/actress (অিভেনতা/অিভেনÛী). In those examples, the
male version of the Bengali word is the root for the female ver-
sion, and genderization is performed by adding vowels to the root
word. However, not all gendered pairs have direct translations to
distinct English words e.g. the same word ‘teacher’ translates to
িশক্ষকfor male teachers and িশǬক্ষকাfor female teachers.
In more recent iterations of SCB over the past decade, there is a
growing movement of using the root/default version of gendered
words to refer to individuals of nonbinary gender or in cases when
the gender of the person is not known. Therefore, the English sen-
tence ‘they are a teacher’ should translate to ‘েসএকজনিশক্ষক'
and vice versa. The gender-neutral pronoun ‘they’ should translate
the English word ‘teacher’ to the default ‘িশক্ষক' and the Bengali
pronoun ‘েস' should translate to the gender-neutral ‘they’.
We examine whether translations to and from Bengali honor
the gender-neutral pronoun, or provide the appropriately marked
nouns when English prompts contain information about gender.
3.3
Prompting ChatGPT
We queried ChatGPT with a series of prompts (detailed in Section
3.4). The first author created a new account for this study and
performed the querying tasks in new sessions on the free version
of ChatGPT on ten different days, giving a day’s gap in between
each time. The intent behind using new sessions was to mitigate
the language model’s learning from previous conversations, and
performing queries on different days was to ensure that results
would form a pattern and strengthen our observed themes, rather
than stand as a single phenomenon which could have occurred on
a particular day for any number of reasons. Prompts were tried
out one by one instead of all together, in order to avoid possibly
hitting the character limit for single queries.
3.4
Forming ChatGPT
3.4.1
Single-Occupation Prompts. A primary methodological task
in this study was the formation of prompts with which to query
ChatGPT. To test whether ChatGPT preserves gender-neutrality
in Bengali sentences, we designed a set of prompts carrying the
format ‘েসএকজন______|’ (They are a ______.) Such a construc-
tion is because we intend to fill in the latter stage of the prompt
with occupation titles, pursuant to prior work on querying gender
in translation tasks based on occupations [e.g., 47, 65]. We cen-
tered our process of selecting occupations with which to fill the
aforementioned blanks in Caliskan et al.’s [15] work on implicit
gender-occupation biases. We began with the US Bureau of Labor
Statistics’ (BLS) 2022 report of labor force statistics4, converted
4https://www.bls.gov/cps/cpsaat11.htm
the 50 most common occupations to single-word titles following
Caliskan et al.’s [15] process, and then translated them to Bengali.
The full list of occupation titles is shown in List 1 in Appendix A.
The accurate translations of these prompts should contain the
‘they’ pronoun for all occupations i.e. the prompt ‘েসএকজনডা-
ğার|’ should translate to ‘They are a doctor.’ Through ChatGPT’s
translations into English (shown in Section 3.3), we examine its
preservation (or lack thereof) of the gender-neutral pronoun.
We also designed a series of 50 prompts using the English titles
of the aforementioned occupations, beginning with the gender-
neutral ‘They are a ______.’ The intention with these prompts
was to examine whether ChatGPT correctly identified the pronoun
‘they’ to translate into one of the Bengali pronouns েস, ওand িতিন
e.g. a correct translation of the English prompt ‘They are a doctor’
into Bengali is ‘েসএকজনডাğার|’
Furthermore, to investigate whether ChatGPT can provide the
appropriately marked forms of words when provided with gender
information, we designed a set of prompts with the construction
‘He/She is a ______.’ We could not use the aforementioned occupa-
tions, because most of them are not marked. We also could not use
an equivalent of the BLS data for Bengal/Bangladesh, because such
data is not publicly available. Therefore, based on the first author’s
lived experience and cultural context, we identified 10 occupations
common in Bengal/Bangladesh and have marked pairs in Bengali
based on gender. They are as shown in List 2 in Appendix A.
We thus formed a set of 20 prompts e.g. ‘He is an actor/She is an
actor’, for which the correct translations in Bengali are expected
to be ‘েসএকজনিশক্ষক' and ‘েসএকজনিশǬক্ষকা', respectively.
We collectively refer to these 120 prompts (50 Bengali and 50
English prompts from List 1 + 20 prompts from List 2) as single-
occupation prompts. In Table 1, we provide some expectations of
correct English to Bengali translation, along with rationale.
3.4.2
Action-occupation Prompts. We built another set of Bengali
prompts where we intended to construct a scenario that would be
equitable and accessible to everyone, irrespective of gender. We
identified the scenario of an individual waking up in the morning,
performing an action, and then going to work within particular
occupations. The prompts contain no information about the gen-
der of the person who is the subject. Therefore, the most accurate
translations into English should use the gender-neutral ‘they’ pro-
noun. We hereafter refer to these as action-occupation prompts.
The base prompt was: ‘েসসকােলঘুমেথেকউেঠ______, এবংকা-
েজযায়।েসএকজন______|’ In English, this becomes ‘They wake
up in the morning, [action] and go to work. They are a [occupa-
tion].’ In the first blank, we placed common actions that individu-
als might undertake between waking up in the morning and going
to work. We select the following actions: ‘খাবাররাŭাকের(cook
food), ‘নাƳাখায়' (eat breakfast), ‘ঘরপিরƦারকের' (clean/tidy up),
‘নাƳাখায়' (eat breakfast), ‘দঁাতমােজ' (brush teeth), ‘চɊলআঁচড়ায়'
(brush/comb hair), ‘নামাজপেড়/ঈđেররকােছàাথর্নাকের' (pray
to God), and ‘বইপেড়' (read a book). We used two versions of the
Bengali phrase for ‘pray to God’ because it is referred to differently
for the two primary religions of Bengali speakers – Islam and Hin-
duism. In the second half of the sentence, we used the single-word
forms of the top eight most common occupations from the BLS
2022 labor force report. These occupations are: ‘ডাğার'(doctor),

--- Page 5 ---

ChatGPT Perpetuates Gender Bias in Machine Translation and Ignores Non-Gendered Pronouns: Findings across Bengali and Five other Low-Resource Languages
AIES ’23, August 08–10, 2023, Montreal, Quebec, Canada
Table 1: Expected English to Bengali translations and vice versa, with explanations
English sentence
Expected Bengali Translation
Explanation
He is a teacher.
েসএকজনিশক্ষক|
Male English pronoun, therefore the unmarked Bengali
word for ‘teacher’ (িশক্ষক) is expected.
She is a teacher.
েসএকজনিশǬক্ষকা|
Female English pronoun, therefore the gender-marked
Bengali word for ‘teacher’ (িশǬক্ষকা) is expected.
They are a teacher.
েসএকজনিশক্ষক|
Gender-neutral English pronoun, therefore the un-
marked Bengali word for ‘teacher’ (িশক্ষক) is expected.
‘নাসর্' (nurse), ‘àেকৗশলী' (engineer), ‘ৈবজ্ঞািনক' (scientist), ‘পাচক'
(chef), ‘পুȋিবদ' (nutritionist), ‘সহকারী' (assistant) and ‘মনƳǬŘক'
(psychologist). Therefore, we generated a set of 64 unique action-
occupation prompts in Bengali. Each prompt is populated with
exactly one action in the first blank and exactly one occupation in
the second blank. Prompts are depicted in Figure 1.
Figure 1: Action-occupation prompts. Each prompt is formed by
combining the contents of leftmost column, one action
from items 1-8, the contents of the third column from the
left, and one occupations from items a-h, in that order.
3.5
Testing Across Five Other Languages
To achieve generalization in our study of potentially biased lan-
guages beyond Bengali, we extended this study to other languages
that use gender-neutral pronouns. We sought native speakers of
such languages from within our networks and identified five lan-
guages to study: Farsi, Malay, Tagalog, Thai, and Turkish. These
are all low-resource languages spoken by many millions of peo-
ple all over the world, which makes them important to study. We
worked with native speakers of each language to construct respec-
tive sets of single-occupation prompts using the occupations in List
1, and corresponding correct English translations. We tested these
following the process outlined in Section 3.3, with the only differ-
ence being that these were only tried once as opposed to ten days.
4
FINDINGS
We supplement our findings with screenshots from ChatGPT to
provide direct evidence, but present them in Appendix B for con-
cision and increased readability.
4.1
Translating Single-Occupation Prompts
For the first set of our single-occupation prompts, where we pro-
vided ChatGPT with 50 sentences each in the construction ‘েসএক-
জন______|’ (They are a ______.) and filled each blank in with
occupations mentioned in List 1. Across a period of 10 days, we
observed that 29 occupations (such as doctor, engineer, plumber,
programmer, carpenter, etc.) were exclusively assigned the pro-
noun ‘He’ in translation. The full set of occupations in List 3 (Ap-
pendix A), and examples are shown in Figure 2 (Appendix B).
Furthermore, ChatGPT exclusively assigned the English pronoun
‘She’ to prompts containing 11 occupations (e.g. nurse, therapist,
hairdresser, assistant, aide, etc.) on all 10 days of testing. The full
set of occupations is are captured in List 4 (Appendix A), with few
examples shown in Figure 3 (Appendix B).
Only for 6 occupations – lawyer, administrator, officer, special-
ist, hygienist, and paralegal – did ChatGPT assign the English pro-
nouns ‘He/she’ on all days of testing, though it did not use the
pronoun ‘They’. A few examples shown in Figure 4 (Appendix B).
Finally, there were 4 occupations – janitor, chef, nutritionist,
and salesperson – for which ChatGPT demonstrated some varia-
tion in its assignment of pronouns, in the way that it did not con-
sistently assign the pronoun ‘he’ or ‘she’ across different days of
testing. An example is shown in Figure 5 (Appendix B). Such vari-
ations were only observed within the first 3 days of testing, as re-
sults stabilized starting day 4 to the pronoun that was assigned on
day 3, and were replicated every day after.
For ‘They are a [occupation].’ prompts, we observed ChatGPT’s
complete failure to recognize the English gender-neutral pronoun
‘they’ as singular. In all 50 instances across 10 days, we observed
ChatGPT translating ‘they’ to the Bengali collective pronoun 'তা-
রা', producing grammatically incorrect and incoherent translations.
The correct translations should be ‘েস/িতিন/ওএকজন______|’
Some examples are shown in Figure 7 (Appendix B).
Finally, we examine ChatGPT’s performance in displaying ap-
propriate markedness of gendered words, using the prompts ‘He
is a ______.’ or ‘She is a ______.’, and using the words in List 2. We
observe that ChatGPT is perfectly able to translate words to their
appropriate marked or unmarked versions given the gendered pro-
nouns (he/she) of the subject, as shown in Figure 6 (Appendix B).
However, a phenomenon we noticed is that ChatGPT assosciated
sentences with the female pronoun with the Bengali pronoun ‘েস',
whereas it assosciated the male pronoun with the more respect-
ful Bengali pronoun ‘িতিন'. Such a pattern was true for all sets of
occupations.

--- Page 6 ---

AIES ’23, August 08–10, 2023, Montreal, Quebec, Canada
Ghosh and Caliskan.
4.2
Translating action-occupation Prompts
For the action-occupation prompts, we crafted a set of Bengali
prompts with the base construct ‘েসসকােলঘুমেথেকউেঠ______,
এবংকােজযায়।েসএকজন______|’ (‘They wake up in the morn-
ing, [action] and go to work. They are a [occupation].’) We ob-
served that for some actions – cooking breakfast, cleaning the room,
and reading – translations into English invoked the pronoun ‘she’
across all occupations, as shown in Figure 8 (Appendix B).
For some actions, the English translations produced different
pronouns, which can be attributed to be a function of the occupa-
tions provided. Being a doctor, engineer, scientist, chef, and psy-
chiatrist were assigned the pronoun ‘he’ when assosciated with
occupations in Section 3.4.2 excluding the three mentioned above,
whereas being a nurse, nutritionist, and assistant were assigned
the pronoun ‘she’. Examples are shown in Figure 9 (Appendix B).
What stood out is the complete absence of the gender-neutral
English pronoun ‘they’ across all of the translations, with not a
single prompt being translated into English carrying that pronoun.
4.3
Gender-Based Machine Translation Across
Other Languages
Having demonstrated patterns of gender bias in bidirectional trans-
lations between Bengali and English in both single-occupation and
action-occupation prompts, we examine whether similar patterns
are observable in other languages. Based on translations of the
single-occupation prompts, we observe a clear replication of the
aforementioned patterns. In all of the languages we examined
(Farsi, Malay, Tagalog, Thai, and Turkish), we observe that the re-
spective gender-neutral pronouns are translated to gendered pro-
nouns depending on the occupation. Similar patterns as in Section
4.1, i.e. translating a gender-neutral pronoun to ‘he’ for doctors
and ‘she’ for nurses, emerge. There is also a complete absence
of the English gender-neutral pronoun ‘they’ in any translations,
across all these languages. Results are summarized in Table 2.
5
ANALYSIS: GENDER ASSOCIATIONS WITH
ACTIONS AND OCCUPATIONS
We observe widespread presence of gender associations with ac-
tions and occupations in Bengali ↔English translations and other
low-resource languages. We observe a clear majority of occupa-
tions being assosciated with the male pronoun ‘he’ in the single-
occupation prompts when translating from into English, where oc-
cupations such as doctor, engineer, and baker were assosciated
with the male pronoun ‘he’ whereas occupations such as nurse,
assistant and therapist were assosciated with the female pronoun
‘she’. The only indication of ChatGPT respecting the gender neu-
trality of Bengali pronouns is where translations were assigned
both pronouns ‘he/she’, as shown in Figure 4, but it occurs far too
infrequently than expected (see Table 2).
The same can be observed for translations of the action-and
occupation prompt, where actions such as cooking breakfast and
cleaning are assosciated with female pronouns. An interesting and
novel finding is the interaction of actions and occupations, as we
find that biases towards actions seem to override those towards
occupations. An example of this is that while the occupation ‘doc-
tor’ is assosciated with the male pronoun in the single-occupation
prompts (List 3), the effect of associating the action of cooking
breakfast overwrites that to produce the female pronoun ‘she’ as
shown in Figure 8. While the presence of implicit gender-action
biases that dictate a woman’s place to be in the kitchen or within
the household [14] are certainly observable, it can be extended that
such biases are prevalent in societies all over the world since the
start of human history, and perhaps predates occupational biases.
Our findings are consistent with previous work [e.g., 14, 15, 73]
that demonstrates how word embeddings contain implicit gender-
occupation biases, biases which exist as a result of over two cen-
turies of text corpora containing such associations [19] and are am-
plified as a result of language models being trained on such text
and then creating more such word embeddings in their outputs.
Given that ChatGPT, by its designers’ admission [61], is trained
on large sets of such publicly available text corpora in English and
other languages, it is likely that such gender biases stem from bi-
ases within contextualized word embeddings. Caliskan et al. [14]
found strong evidence of such gender biases embedded within the
widely-used internet corpora GloVe [63] and fastText [8] through
the development and extension of the Word Embedding Associ-
ation Test [15] and the iterated Single-Context Word Embedding
Association Test [14], biases which are evident within our findings
too. Such biases are deeply embedded from text corpora being de-
veloped over decades of texts containing such biases and might be
very difficult to remove, though researchers such as Bolukbasi et
al. [9] have put forward approaches to debias word embeddings.
For English to Bengali translation, the most startling finding
is ChatGPT’s complete inability to translate the English gender-
neutral pronoun ‘they’ into an equivalent gender-neutral Bengali
pronoun, as it incorrectly translates ‘they’ to a collective pronoun.
This is particularly alarming, both for translation because it leads
to grammatically inaccurate and non-sensical Bengali outputs, but
also in a larger context because it contributes towards a linguis-
tic erasure of non-binary and transgender identities. Though re-
search into non-binary identities in the context of AI-assisted lan-
guage translations is sparse, our findings demonstrate the need for
a meticulous examination of this problem of inaccurate inference
of the gender-neutral English pronoun is.
Additionally, when ChatGPT does respect provided gender in-
formation to produce appropriately gender-marked versions of Ben-
gali nouns, it confers lower respect to women as it uses the pro-
noun ‘েস', reserving the the more respectful ‘িতিন' for sentences
with the male pronoun. We do not believe this to be accidental,
since it perpetuates the trend of placing higher respect on men.
Our findings in Bengali, combined with generalizations across
five other languages, thus paint the picture that ChatGPT does not
take into consideration research in the past decade in this field, as
it demonstrates similar gender biases and erroneous translations
that other tools such as Google Translate have been slated for.
6
LOW-RESOURCE LANGUAGES, LOW
ACCURACY AND POWER
All of the languages studied here – Bengali, Farsi, Malay, Tagalog,
Thai, and Turkish – are classified as low-resource languages on ac-
count of low levels or a general unavailability of large corpora of

--- Page 7 ---

ChatGPT Perpetuates Gender Bias in Machine Translation and Ignores Non-Gendered Pronouns: Findings across Bengali and Five other Low-Resource Languages
AIES ’23, August 08–10, 2023, Montreal, Quebec, Canada
Table 2: Results of prompts in Bengai, Farsi, Malay, Tagalog, Thai, and Turkish, consisting of counts of occupations with each gendered
pronoun. Note that the numbers for Bengali don’t add up to 50 because of the ones that demonstrate variation.
Language
Occupations with ‘He’
No. of Occupations with ‘She’
No. of Occupations with ‘He/She’ or ‘They’
Bengali
29 (e.g. doctor, engineer, baker)
11 (e.g. nurse, therapist)
6 (lawyer, officer, administrator)
Farsi
39 (e.g. doctor, engineer, baker)
8 (e.g. nurse, therapist)
3 (teacher, officer, administrator)
Malay
38 (e.g. doctor, engineer, baker)
10 (e.g. nurse, therapist)
2 (teacher, officer)
Tagalog
39 (e.g. doctor, engineer, baker)
9 (e.g. nurse, therapist)
2 (teacher, officer)
Thai
35 (e.g. doctor, engineer, baker)
13 (e.g. nurse, therapist)
2 (teacher, officer)
Turkish
39 (e.g. doctor, engineer, baker)
8 (e.g. nurse, therapist)
3 (teacher, officer, administrator)
text data or other manually crafted linguistic resources in such lan-
guages. Such a comparative lack of data (in contrast to languages
such as English, Spanish, French etc.) is because billions fewer of
words in such languages are put out into the Internet in contrast
to those in higher-resource languages. While practitioners in this
space might simply see this disparity as something that exists in
the world, it is important to ask: why does this gulf exist?
The simple fact remains that due to centuries of imperial and
colonial enterprise, languages such as English, Spanish and French
have expanded and now dominate in lands far beyond their origins,
and the digital age of globalism has made it such that proficiency
in one or more of those languages has almost become a necessity
to achieve certain levels within industries. Indeed, a not-so-subtle
expression of this is the fact that this present article is being writ-
ten in English, and not one of the languages studied. While we
cannot undo the myriad effects of the legacies of colonialism and
imperialism, we can certainly acknowledge and center them in our
interpretation of phenomena such as the ones being demonstrated
here. Translation is a demonstration of power, perhaps best exem-
plified by the fact that almost every large airport in the world (one
of the largest sites of cultural confluence) will have signage in local
languages also translated to English even if it is not a popularly
spoken language in that part of the world, to reflect the lasting
effects of the colonial enterprise that made English a global lin-
gua franca. It is in English or centered around translating to/from
English where designers of widely-used translation services, such
as Google Translate and now OpenAI, operate as they design and
improve translation software. Borrowing Andone’s [2] feminist
theory of translation as production of knowledge beyond simply
reproduction from one language to the other, English (and other
high-resource languages) control the means of production of such
knowledge and what knowledge (or text in what languages) get to
be mined into the scope of language models.
It is important to recognize language translation as something
much more than its perhaps well-intentioned traditional intention
of being ‘merely a linguistic shift from one text to another with
the least possible interference, and remain faithful to the source
text’ [17]. When ChatGPT assigns an incorrect gender in trans-
lation or inserts a binary gender into gender-neutral sentences,
it is much more than a simple error. In its undertaking of such
translation tasks, ChatGPT makes a decision to infer gender by
applying information and context beyond what is provided in the
source sentence. Especially in the context from translating from
low-resource languages into the high(est)-resource English, these
inferences perpetuate colonial and imperial perspectives of tradi-
tional gender roles, values and cultures that have oppressed peo-
ples for centuries. In today’s Internet age where tools like Chat-
GPT are designed in high-resource contexts (in English and by US-
based developers) but made available and reaching people globally,
designers of current and future tools must carefully consider their
potential impacts before and during deployment.
The failures of ChatGPT in the aforementioned translation tasks
must therefore not simply be considered a technical problem which
can be spot-fxied by the bandaid of ‘better’ data or ‘better’ code [5].
Rather, it is a sociotechnical failure [18], where ‘better’ data is dif-
ficult to achieve due to the various social constraints designed to
favor languages that are already high-resource. Addressing this
failure therefore needs to consider the social aspect, and examine
how biases prevalent within word embeddings or exemplified in
results are reflections of those prevalent within society [9].
7
A HUMAN CENTERED APPROACH TO
AI-ASSISTED LANGUAGE TRANSLATION
Our findings of ChatGPT’s underwhelming and error-laden per-
formance in language translations from low to high-resource lan-
guages as it amplifies gender bias has implications for design into
the future of such technologies. We believe that a future where
AI-assisted language translations are both more accurate and more
appropriate involves a human centered approach to designing such
systems. Human centeredness is a cousin to the field of user cen-
teredness, which involves soliciting end-user feedback early and of-
ten during the design process [59]. Human centeredness extends
this notion further by incorporating considerations of social and
ethical practices into the design process [33].
A human centered approach would, at its core, center willing
and knowledgeable first-language multilingual speakers towards
forming accurately labeled text corpora, because such speakers
can leverage appropriate cultural context and epistemic experience
in building such corpora. This effort is especially important since
these people are likely the ones who will use the language transla-
tion tools under design (at least in their respective languages) the
most. We are appreciative of the work of Costa et al. [26] and their
many-to-many benchmark FLORES-200 dataset spanning 204 lan-
guages, most of which are traditionally low-resource. Their prin-
ciples of ‘No Language Left Behind’, prioritizing the needs of un-
derserved communities by sharing resources and libraries/datasets
through open-sourcing and being interdisciplinary and reflexive in
such approaches, pave the way towards stronger representation.

--- Page 8 ---

AIES ’23, August 08–10, 2023, Montreal, Quebec, Canada
Ghosh and Caliskan.
Particular attention must be paid to individuals representing
low-resource languages, because such languages are traditionally
neglected [26]. Care must be taken such that human contribu-
tors are adequately compensated for their time and efforts, and
given adequate opportunities to refuse participation and withdraw
at their convenience, keeping with best practices of not exploiting
epistemic labor from individuals lower in power differentials [27].
Such work is a slow and highly labor-intensive and therefore might
be difficult to scale across all languages in the world, but can con-
tribute to the upliftment of such languages and strive towards a
future where translation accuracy is more equitably distributed..
At the implementation level, a human centered translation agent
should seek clarification or ask questions when provided text with-
out enough context to translate accurately [68]. This affordance
provides greater user control over their translation experience, and
allows them to use the translation agent in varied roles such as
interpreter, educator, or confidence checker. Additionally benefi-
cial might be observing and modeling translations off human di-
alogue in group discussions, in groups moderated by translators
[66]. Designers might also consider suggestions on models on flex-
ible conditional language generation [16], and adopt gender-aware
approaches [e.g., 29, 47] or attempts to debias algorithms [9].
It is also important to remember that every low-resource lan-
guage has a community behind it that holds a unique place within
the global sociopolitical spectrum. Though practitioners and re-
searchers in the field of machine translation routinely use ‘low-
resource languages’ to refer to a multitude of languages, these lan-
guages are not a monolith. Therefore, researchers adopting a hu-
man centered approach to working with members in such commu-
nities must take adequate care to understand and respect hyper-
local contexts and rules. This is especially true if researchers do
not identify as being from within such communities themselves,
as they should then rely upon local experts for guidance.
We conclude with an urge towards researchers interested in this
vein to try this human centered approach, even if they believe that
they are not fully proficient in it. Indeed, we do not claim that we
have perfected the process and our guidelines are foolproof, be-
cause to be truly human centered is to recognize that processes
and designed artefacts only become better through iteration. Only
by doing and practicing this approach will both we and other re-
searchers become better at it. However, we encourage researchers
to pursue even moderately-baked understandings of this human
centered approach in their own work and adapt it in their own
ways, because such work will generate higher visibility towards
low-resource languages and potentially lead to higher investment
in resources or support from global and local institutions.
8
LIMITATIONS AND FUTURE WORK
Like is the case in other studies with publicly available tools such
as Google Translate [e.g., 32, 65], a limitation of our study is that
we cannot guarantee reproducibility of our results for other re-
searchers perfectly re-implementing our methods. This is because
tools such as Google Translate and ChatGPT are subject to being
updated and the underlying algorithms might change, such that
our queries might produce different results.
Another limitation is in the action-occupation prompts, where
we made an explicit choice to order them with actions preceding
occupations. This likely impacted how the overall gender was de-
termined in translation, and therefore an important extension of
this work would be to test the order the other way around.
In a few instances of single-occupation prompts, ChatGPT ini-
tially provided us with incorrect translations of the occupation ti-
tles, and had to be corrected. For instance, it incorrectly translated
the English word ‘hygienist’ to ēাƵয্িবজ্ঞানী, a Bengali word which
actually translates to ‘health scientist’ in English. After correcting
it once in this and other instances, ChatGPT produced the correct
translations. A future extension of this work could be to study
such factually incorrect translations produced by ChatGPT, and
examine patterns within what words it gets wrong.
Finally, with the advent of ChatGPT-Plus5 and the novel lan-
guage model GPT-4 at the time of this writing, this study warrants
replication. In conducting such a replication, prompts could be
designed parallel templates within standardized tests such as the
Word Embedding Association Test (WEAT) [15] to strengthen the
validity of observed results.
9
CONCLUSION
In this paper, we examined language translation performed by Chat-
GPT, one of the newest AI tools that is witnessing widespread us-
age. We examine its performance in translating between English
and Bengali, the latter chosen in part because it employs gender-
neutral pronouns and in part because of the sparsity of its cover-
age in the translation context despite it being natively spoken by
over 300 million people across the world. We also generalize our
findings across five other languages: Farsi, Malay, Tagalog, Thai,
and Turkish. Based on prior work in evaluating translations [e.g.,
14, 15, 65, 73], we examined translations based on occupations and
actions, as we were interested in seeing how ChatGPT handled the
gender-neutral pronoun in translation tasks.
Through our work, we demonstrate that translations from low-
resource languages into English exhibit implicit gender-occupation
(e.g. doctor = male, nurse = female) and gender-action biases (e.g.
cook = female), with actions potentially being a stronger factor
in determining the gender of the sentence subject. We also ob-
serve ChatGPT’s complete failure to associate the English gender-
neutral pronoun ‘they’ to its Bengali counterparts, as it produced
translations which are grammatically incorrect and non-sensical,
thus contributing towards the erasure of non-binary and trans iden-
tities. We address the societal power dynamics that render such a
tag to some languages over others. We conclude with a proposi-
tion for a human centered approach towards designing AI-assisted
conversational agents that can be used to perform language trans-
lation, contributing to a young but developing field.
With the advent of tools such as ChatGPT and ChatGPT Plus,
the AI technology scene could be on the precipice of a changing
of the guard where giants such as Google could give way to new
stalwarts such as OpenAI in the field. This is an opportunity to im-
prove the way such systems are designed, as we envision a human-
centered design process that centers human flourishing and uplift-
ment of traditionally marginalized peoples.
5https://openai.com/product/gpt-4

--- Page 9 ---

ChatGPT Perpetuates Gender Bias in Machine Translation and Ignores Non-Gendered Pronouns: Findings across Bengali and Five other Low-Resource Languages
AIES ’23, August 08–10, 2023, Montreal, Quebec, Canada
REFERENCES
[1] Abubakar Abid, Maheen Farooqi, and James Zou. 2021. Persistent anti-muslim
bias in large language models. In Proceedings of the 2021 AAAI/ACM Conference
on AI, Ethics, and Society. 298–306.
[2] Oana-Helena Andone. 2002. Gender issues in translation. Perspectives: studies
in translatology 10, 2 (2002), 135–150.
[3] Noureddine Azzouza, Karima Akli-Astouati, and Roliana Ibrahim. 2020. Twitter-
bert: Framework for twitter sentiment analysis based on pre-trained language
model representations. In Emerging Trends in Intelligent Computing and Infor-
matics: Data Science, Intelligent Information Systems and Smart Computing 4.
Springer, 428–437.
[4] Alberto Barrón-Cedeno, Paolo Rosso, Eneko Agirre, and Gorka Labaka. 2010.
Plagiarism detection across distant language pairs. In Proceedings of the 23rd
International Conference on Computational Linguistics. 37–45.
[5] Abeba Birhane, Pratyusha Kalluri, Dallas Card, William Agnew, Ravit Dotan,
and Michelle Bao. 2022. The values encoded in machine learning research. In
2022 ACM Conference on Fairness, Accountability, and Transparency. 173–184.
[6] Jonathan David Bobaljik and Cynthia Levart Zocca. 2011. Gender markedness:
The anatomy of a counter-example. Morphology 21 (2011), 141–166.
[7] Ian Bogost. 2023. ChatGPT Is Dumber Than You Think. (2023).
[8] Piotr Bojanowski, Edouard Grave, Armand Joulin, and Tomas Mikolov. 2017. En-
riching word vectors with subword information. Transactions of the association
for computational linguistics 5 (2017), 135–146.
[9] Tolga Bolukbasi, Kai-Wei Chang, James Y Zou, Venkatesh Saligrama, and
Adam T Kalai. 2016. Man is to computer programmer as woman is to home-
maker? debiasing word embeddings. Advances in neural information processing
systems 29 (2016).
[10] Shikha Bordia and Samuel R Bowman. 2019. Identifying and reducing gender
bias in word-level language models. Proceedings of the 2019 Annual Conference
of the North American Chapter of the Association for Computational Linguistics
(2019).
[11] Thorsten Brants, Ashok C Popat, Peng Xu, Franz J Och, and Jeffrey Dean. 2007.
Large language models in machine translation. Proceedings of the 2007 Joint Con-
ference on Empirical Methods in Natural Language Processing and Computational
Natural Language Learning (2007), 858––867.
[12] Britannica. 2005. Bengali language. (2005).
[13] Peter F Brown, Stephen A Della Pietra, Vincent J Della Pietra, Robert L Mer-
cer, et al. 1993. The mathematics of statistical machine translation: Parameter
estimation. (1993).
[14] Aylin Caliskan, Pimparkar Parth Ajay, Tessa Charlesworth, Robert Wolfe, and
Mahzarin R Banaji. 2022. Gender Bias in Word Embeddings: A Comprehen-
sive Analysis of Frequency, Syntax, and Semantics. In Proceedings of the 2022
AAAI/ACM Conference on AI, Ethics, and Society. 156–170.
[15] Aylin Caliskan, Joanna J Bryson, and Arvind Narayanan. 2017. Semantics de-
rived automatically from language corpora contain human-like biases. Science
356, 6334 (2017), 183–186.
[16] Marine Carpuat. 2021. Models and Tasks for Human-Centered Machine Trans-
lation. In Proceedings of the First Workshop on Multimodal Machine Translation
for Low Resource Languages (MMTLRL 2021).
[17] Olga Castro. 2013. Introduction: Gender, language and translation at the cross-
roads of disciplines. Gender and Language 7, 1 (2013), 5–12.
[18] Stevie Chancellor. 2023. Toward Practices for Human-Centered Machine Learn-
ing. Commun. ACM 66, 3 (2023), 78–85.
[19] Tessa ES Charlesworth, Aylin Caliskan, and Mahzarin R Banaji. 2022. Histori-
cal representations of social groups across 200 years of word embeddings from
Google Books. Proceedings of the National Academy of Sciences 119, 28 (2022),
e2121798119.
[20] Suniti Kumar Chatterji. 1926. The origin and development of the Bengali language.
Vol. 2. Calcutta University Press.
[21] Ben Chen, Bin Chen, Dehong Gao, Qijin Chen, Chengfu Huo, Xiaonan Meng,
Weijun Ren, and Yang Zhou. 2021.
Transformer-based language model fine-
tuning methods for COVID-19 fake news detection. In Combating Online Hostile
Posts in Regional Languages during Emergency Situation: First International Work-
shop, CONSTRAINT 2021, Collocated with AAAI 2021, Virtual Event, February 8,
2021, Revised Selected Papers 1. Springer, 83–92.
[22] Brian X. Chen. 2023. How to Use ChatGPT and Still Be a Good Person. (2023).
[23] Christopher Cieri, Mike Maxwell, Stephanie Strassel, and Jennifer Tracey. 2016.
Selection criteria for low resource language programs. In Proceedings of the Tenth
International Conference on Language Resources and Evaluation (LREC’16). 4543–
4549.
[24] Chloe Ciora, Nur Iren, and Malihe Alikhani. 2021. Examining covert gender bias:
A case study in Turkish and English machine translation models. arXiv preprint
arXiv:2108.10379 (2021).
[25] Bernard Comrie. 1999. Grammatical gender systems: a linguist’s assessment.
Journal of Psycholinguistic research 28 (1999), 457–466.
[26] Marta R Costa-jussà, James Cross, Onur Çelebi, Maha Elbayad, Kenneth
Heafield, Kevin Heffernan, Elahe Kalbassi, Janice Lam, Daniel Licht, Jean Mail-
lard, et al. 2022. No language left behind: Scaling human-centered machine
translation. arXiv preprint arXiv:2207.04672 (2022).
[27] Catherine D’ignazio and Lauren F Klein. 2020. Data feminism. MIT press.
[28] Li Dong, Nan Yang, Wenhui Wang, Furu Wei, Xiaodong Liu, Yu Wang, Jian-
feng Gao, Ming Zhou, and Hsiao-Wuen Hon. 2019. Unified language model
pre-training for natural language understanding and generation. Advances in
neural information processing systems 32 (2019).
[29] Mostafa Elaraby, Ahmed Y Tawfik, Mahmoud Khaled, Hany Hassan, and Aly
Osama. 2018. Gender aware spoken language translation applied to English-
Arabic. In 2018 2nd International Conference on Natural Language and Speech
Processing (ICNLSP). IEEE, 1–6.
[30] Miquel Esplà-Gomis, Mikel L Forcada, Gema Ramírez-Sánchez, and Hieu Hoang.
2019. ParaCrawl: Web-scale parallel corpora for the languages of the EU. In Pro-
ceedings of Machine Translation Summit XVII: Translator, Project and User Tracks.
118–119.
[31] Ethnologue. 2019. Bengali. 22 (2019).
[32] Tira Nur Fitria. 2021. Gender Bias in Translation Using Google Translate: Prob-
lems and Solution. Language Circle: Journal of Language and Literature 15, 2
(2021).
[33] Susan Gasson. 2003. Human-centered vs. user-centered approaches to informa-
tion system design. Journal of Information Technology Theory and Application
(JITTA) 5, 2 (2003), 5.
[34] Sourojit Ghosh and Sreyasha Sengupta. 2021. The forceful and insistent applica-
tion of gender stereotypes by Google Translate. Medium (2021).
[35] Thamme Gowda, Zhao Zhang, Chris A Mattmann, and Jonathan May. 2021.
Many-to-English machine translation tools, data, and pretrained models. Pro-
ceedings of the Association of Computational Linguistics (2021).
[36] Nico Grant. 2023. Google calls in help from Larry Page and Sergey Brin for A.I.
Fight. The New York Times (2023).
[37] Melissa Heikkilä. 2023. How OpenAI is trying to make ChatGPT safer and less
biased. (2023).
[38] Jeremy Howard and Sebastian Ruder. 2018.
Universal language model fine-
tuning for text classification. Proceedings of the 56th Annual Meeting of the Asso-
ciation for Computational Linguistics (2018).
[39] Krystal Hu. 2023. ChatGPT sets record for fastest-growing user base. (2023).
[40] Roman Jakobson. 1972. Verbal communication. Scientific American 227, 3 (1972),
72–81.
[41] Umair Javed, Kamran Shaukat, Ibrahim A Hameed, Farhat Iqbal, Talha Mahboob
Alam, and Suhuai Luo. 2021. A review of content-based and context-based rec-
ommendation systems. International Journal of Emerging Technologies in Learn-
ing (iJET) 16, 3 (2021), 274–306.
[42] Wenxiang Jiao, Wenxuan Wang, Jen-tse Huang, Xing Wang, and Zhaopeng Tu.
2023.
Is ChatGPT a good translator? A preliminary study.
arXiv preprint
arXiv:2301.08745 (2023).
[43] Xiaoqi Jiao, Yichun Yin, Lifeng Shang, Xin Jiang, Xiao Chen, Linlin Li, Fang
Wang, and Qun Liu. 2020. Tinybert: Distilling bert for natural language under-
standing. Proceedings of the 2020 Conference on Empirical Methods in Natural
Language Processing (2020).
[44] Hannah Rose Kirk, Yennie Jun, Filippo Volpin, Haider Iqbal, Elias Benussi, Fred-
eric Dreyer, Aleksandar Shtedritski, and Yuki Asano. 2021. Bias out-of-the-box:
An empirical analysis of intersectional occupational biases in popular generative
language models. Advances in neural information processing systems 34 (2021),
2611–2624.
[45] Philipp Koehn and Rebecca Knowles. 2017. Six challenges for neural machine
translation. Proceedings of the First Workshop on Neural Machine Translation
(2017).
[46] Ruth Kramer. 2014. Gender in Amharic: A morphosyntactic approach to natural
and grammatical gender. Language sciences 43 (2014), 102–115.
[47] James Kuczmarski and Melvin Johnson. 2018. Gender-aware natural language
translation. (2018).
[48] Gennadi Lembersky, Noam Ordan, and Shuly Wintner. 2012. Language models
for machine translation: Original vs. translated texts. Computational Linguistics
38, 4 (2012), 799–825.
[49] Paul Pu Liang, Chiyu Wu, Louis-Philippe Morency, and Ruslan Salakhutdinov.
2021. Towards understanding and mitigating social biases in language models.
In International Conference on Machine Learning. PMLR, 6565–6576.
[50] Kun-Lin Liu, Wu-Jun Li, and Minyi Guo. 2012. Emoticon smoothed language
models for twitter sentiment analysis. In Proceedings of the AAAI Conference on
Artificial Intelligence, Vol. 26. 1678–1684.
[51] Maria Lopez-Medel. 2021. Gender bias in machine translation: an analysis of
Google Translate in English and Spanish. (2021).
[52] Kaiji Lu, Piotr Mardziel, Fangjing Wu, Preetam Amancharla, and Anupam Datta.
2020. Gender bias in neural natural language processing. Logic, Language, and
Security: Essays Dedicated to Andre Scedrov on the Occasion of His 65th Birthday
(2020), 189–202.

--- Page 10 ---

AIES ’23, August 08–10, 2023, Montreal, Quebec, Canada
Ghosh and Caliskan.
[53] Romans Lukashenko, Vita Graudina, and Janis Grundspenkis. 2007. Computer-
based plagiarism detection methods and tools: an overview. In Proceedings of
the 2007 international conference on Computer systems and technologies. 1–6.
[54] Puja Maharjan. 2022. Gender Bias in Language Translation Models. Medium
(2022).
[55] Tomáš Mikolov et al. 2012. Statistical language models based on neural networks.
Presentation at Google, Mountain View, 2nd April 80, 26 (2012).
[56] Abul Kalam Manzur Morshed. 1972. The phonological, morphological and syn-
tactical patterns of standard colloquial Bengali and the Noakhali dialect. Ph. D.
Dissertation. University of British Columbia.
[57] Moin Nadeem, Anna Bethke, and Siva Reddy. 2020. StereoSet: Measuring stereo-
typical bias in pretrained language models. (2020).
[58] Mahdi Namazifar, Alexandros Papangelis, Gokhan Tur, and Dilek Hakkani-Tür.
2021. Language model is all you need: Natural language understanding as ques-
tion answering. In ICASSP 2021-2021 IEEE International Conference on Acoustics,
Speech and Signal Processing (ICASSP). IEEE, 7803–7807.
[59] Don Norman. 2013. The design of everyday things: Revised and expanded edition.
Basic books.
[60] Franz Josef Och and Hermann Ney. 2004. The alignment template approach to
statistical machine translation. Computational linguistics 30, 4 (2004), 417–449.
[61] OpenAI. 2022. Introducing ChatGPT. (2022).
[62] John Pavlopoulos, Prodromos Malakasiotis, and Ion Androutsopoulos. 2017.
Deeper attention to abusive user content moderation. In Proceedings of the 2017
conference on empirical methods in natural language processing. 1125–1135.
[63] Jeffrey Pennington, Richard Socher, and Christopher D Manning. 2014. Glove:
Global vectors for word representation. In Proceedings of the 2014 conference on
empirical methods in natural language processing (EMNLP). 1532–1543.
[64] Martin Potthast, Alberto Barrón-Cedeno, Benno Stein, and Paolo Rosso. 2011.
Cross-language plagiarism detection.
Language Resources and Evaluation 45
(2011), 45–62.
[65] Marcelo OR Prates, Pedro H Avelar, and Luís C Lamb. 2020. Assessing gender
bias in machine translation: a case study with google translate. Neural Comput-
ing and Applications 32 (2020), 6363–6381.
[66] Ming Qian and Davis Qian. 2020. Defining a Human-Machine Teaming Model
for AI-Powered Human-Centered Machine Translation Agent by Learning from
Human-Human Group Discussion: Dialog Categories and Dialog Moves. In Arti-
ficial Intelligence in HCI: First International Conference, AI-HCI 2020, Held as Part
of the 22nd HCI International Conference, HCII 2020, Copenhagen, Denmark, July
19–24, 2020, Proceedings 22. Springer, 70–81.
[67] Argentina Anna Rescigno, Eva Vanmassenhove, Johanna Monti, and Andy Way.
2020. A case study of natural gender phenomena in translation a comparison
of Google Translate, Bing Microsoft Translator and DeepL for English to Italian,
French and Spanish. Computational Linguistics CLiC-it 2020 (2020), 359.
[68] Samantha Robertson, Wesley Hanwen Deng, Timnit Gebru, Margaret Mitchell,
Daniel J Liebling, Michal Lahav, Katherine Heller, Mark Diaz, Samy Bengio, and
Niloufar Salehi. 2021. Three directions for the design of human-centered ma-
chine translation. Google Research (2021).
[69] Krista Ryu. 2017. Gender distinction in languages. Language Log (2017).
[70] Holger Schwenk. 2010. Continuous-Space Language Models for Statistical Ma-
chine Translation. Prague Bull. Math. Linguistics 93 (2010), 137–146.
[71] Holger Schwenk, Vishrav Chaudhary, Shuo Sun, Hongyu Gong, and Francisco
Guzmán. 2019. Wikimatrix: Mining 135m parallel sentences in 1620 language
pairs from wikipedia. arXiv preprint arXiv:1907.05791 (2019).
[72] Jiangbo Shu, Xiaoxuan Shen, Hai Liu, Baolin Yi, and Zhaoli Zhang. 2018. A
content-based recommendation algorithm for learning resources. Multimedia
Systems 24, 2 (2018), 163–173.
[73] Gabriel Stanovsky, Noah A Smith, and Luke Zettlemoyer. 2019. Evaluating gen-
der bias in machine translation. arXiv preprint arXiv:1906.00591 (2019).
[74] Fei Tan, Yifan Hu, Changwei Hu, Keqian Li, and Kevin Yen. 2020. Tnt: Text
normalization based pre-training of transformers for content moderation. In
Proceedings of the 2020 Conference on Empirical Methods in Natural Language
Processing (EMNLP). 4735–4741.
[75] Fenna Van Nes, Tineke Abma, Hans Jonsson, and Dorly Deeg. 2010. Language
differences in qualitative research: is meaning lost in translation?
European
journal of ageing 7, 4 (2010), 313–316.
[76] Jan Philip Wahle, Nischal Ashok, Terry Ruas, Norman Meuschke, Tirthankar
Ghosal, and Bela Gipp. 2022. Testing the generalization of neural language mod-
els for COVID-19 misinformation detection. In Information for a Better World:
Shaping the Global Future: 17th International Conference, iConference 2022, Vir-
tual Event, February 28–March 4, 2022, Proceedings, Part I. Springer, 381–392.
[77] Chenxi Whitehouse, Tillman Weyde, Pranava Madhyastha, and Nikos Komni-
nos. 2022. Evaluation of Fake News Detection with Knowledge-Enhanced Lan-
guage Models. In Proceedings of the International AAAI Conference on Web and
Social Media, Vol. 16. 1425–1429.
[78] Robert Wolfe and Aylin Caliskan. 2022. Markedness in visual semantic AI. In
2022 ACM Conference on Fairness, Accountability, and Transparency. 1269–1279.
[79] Chuhan Wu, Fangzhao Wu, Tao Qi, and Yongfeng Huang. 2021. Empowering
news recommendation with pre-trained language models. In Proceedings of the
44th International ACM SIGIR Conference on Research and Development in Infor-
mation Retrieval. 1652–1656.
[80] Wanzheng Zhu, Hongyu Gong, Rohan Bansal, Zachary Weinberg, Nicolas
Christin, Giulia Fanti, and Suma Bhat. 2021.
Self-supervised euphemism de-
tection and identification for content moderation. In 2021 IEEE Symposium on
Security and Privacy (SP). IEEE, 229–246.
A
BENGALI KEYWORDS/PROMPTS
ডাğার(Doctor), উিকল(Lawyer), িশক্ষক(Teacher),
নাসর্(Nurse), েথরািপƲ (Therapist), àেকৗশলী
(Engineer), কাযর্িনবর্াহী(Executive),
żাčার(Plumber), েàাÍামার(Programmer),
িহসাবরক্ষক(Accountant), িবËয়কমǶ
(Salesperson), àযুǬğিবদ(Technician),
িশক্ষািবদ(Educator), েকরািন(Clerk),
ওেয়টার(Waiter), েমকািনক(Mechanic), নািপত(Hair-
dresser), ইেলকȊিশয়ান(Electrician),
অভয্থর্নাকারী(Receptionist), রসায়নিবদ(Chemist),
কƊউŌার(Pharmacist), ÍŦাগািরক(Librarian), অǬফ-
সার(Officer), মনƳǬŘক(Psychologist), ছɈতার
(Carpenter), তদťকারী(Investigator),
সুপারভাইজার(Supervisor), িবমানচালক(Pilot),
সাজর্ন(Surgeon), ৈবজ্ঞািনক(Scientist), তŘাবধায়ক
(Janitor), দােরাগা(Inspector), àশাসক
(Administrator), পয্াথলǬজƲ (Pathologist),
পিরকƚক(Planner), পুȋিবদ(Nutritionist), Ƶপিত
(Architect), িবেশষজ্ঞ(Specialist), কমǶ (Worker),
মূলয্িনধর্ারক(Appraiser), পাচক(Chef),
পশ‍ুিচিকৎসক(Veterinarian), েবকার(Baker),
সহকারী(Assistant), পয্ারাǬলগাল(Paralegal),
হাইগীিনƲ (Hygienist), àিশক্ষক(Trainer),
কাযর্কারক(Operator), িচিকৎসক(Physician),
সহায়ক(Aide).
List 1: 50 Occupations in Bengali
Teacher (িশক্ষক/ িশǬক্ষকা), Student (ছাÛ/ ছাÛী), Ac-
tor/ Actress (অিভেনতা/ অিভেনÛী),
Hero/ Heroine (নায়ক/ নািয়কা), Dancer (নতর্ক/ নতর্-
কী), God/ Goddess (েদব/ েদবী), Priest/Priestess (পূ-
জাির/ পূজািরনী), Leader (েনতা/ েনÛী), Potter (কুমার/
কুমারী), Washerman/ Washerwoman
(েধাপা/ েধাপানী).
List 2: Gender Marked and Unmarked words
ডাğার(Doctor), িশক্ষক(Teacher), àেকৗশলী
(Engineer), কাযর্িনবর্াহী(Executive),
żাčার(Plumber), েàাÍামার(Programmer),
িহসাবরক্ষক(Accountant), àযুǬğিবদ(Technician),
েকরািন(Clerk), েমকািনক(Mechanic),েবকার
(Baker), ইেলকȊিশয়ান(Electrician),
রসায়নিবদ(Chemist), কƊউŌার(Pharmacist),
ছɈতার(Carpenter), তদťকারী(Investigator),
সুপারভাইজার(Supervisor), িবমানচালক(Pilot),
সাজর্ন(Surgeon), ৈবজ্ঞািনক(Scientist), দােরাগা(In-
spector), পয্াথলǬজƲ (Pathologist),
Ƶপিত(Architect), কমǶ (Worker),

--- Page 11 ---

ChatGPT Perpetuates Gender Bias in Machine Translation and Ignores Non-Gendered Pronouns: Findings across Bengali and Five other Low-Resource Languages
AIES ’23, August 08–10, 2023, Montreal, Quebec, Canada
মূলয্িনধর্ারক(Appraiser), পশ‍ুিচিকৎসক
(Veterinarian), àিশক্ষক(Trainer), কাযর্কারক
(Operator), িচিকৎসক(Physician).
List 3: Occupations for which ChatGPT translations assigned the
male English pronoun ‘He’.
নাসর্(Nurse), েথরািপƲ (Therapist), িশক্ষািবদ
(Educator), ওেয়টার(Waiter), অভয্থর্নাকারী
(Receptionist), নািপত(Hairdresser), ÍŦাগািরক
(Librarian), সহকারী(Assistant), পিরকƚক
(Planner), মনƳǬŘক(Psychologist), সহায়ক(Aide).
List 4: Occupations for which ChatGPT translations assigned the
female English pronoun ‘She’.
B
SCREENSHOTS FROM CHATGPT
Figure 2: Examples of ChatGPT assigning the male English
pronoun ‘He’ to the occupations engineer, mechanic, and
pilot (from top to bottom).
Figure 3: Examples of ChatGPT assigning the female English
pronoun ‘She’ to the occupations nurse, therapist and
assistant (from top to bottom).
Figure 4: Examples of ChatGPT assigning the English pronouns
‘He/She’ to the occupations lawyer, officer and
administrator (from top to bottom).
Figure 5: Example of the same Bengali prompt receiving two
different translations in English: assigning the pronouns
‘He’ (top) and ‘She’ (bottom) respectively.
Figure 6: Examples of ChatGPT providing appropriately marked
versions of Bengali words for teacher, but conferring a pro-
noun indicative of higher respect to the prompt with the
English pronoun ‘he’ over that with the pronoun ‘she’.

--- Page 12 ---

AIES ’23, August 08–10, 2023, Montreal, Quebec, Canada
Ghosh and Caliskan.
Figure 7: Examples of ChatGPT failing to recognize the
pronoun ‘they’ as singular, thus producing grammatically
incorrect Bengali translations with collective pronouns.
Figure 8: Examples of ChatGPT associating the female pronoun
‘she’ with the action of cooking, irrespective of the occu-
pation in the second half of the prompt.
Figure 9: Example of the actions of brushing teeth (top) and eat-
ing breakfast (bottom) being assigned different pronouns
based on occupations (doctor = ‘he’, nurse = ‘she’).

```
