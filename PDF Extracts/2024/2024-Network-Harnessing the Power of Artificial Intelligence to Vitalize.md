---
title: "2024-Network-Harnessing the Power of Artificial Intelligence to Vitalize - PDF Extract"
source_pdf: "2024-Network-Harnessing the Power of Artificial Intelligence to Vitalize.pdf"
pages: 31
extracted_at: "2026-02-13T13:57:11.807970"
---

# PDF Extract: 2024-Network-Harnessing the Power of Artificial Intelligence to Vitalize

**Source PDF:** 2024-Network-Harnessing the Power of Artificial Intelligence to Vitalize.pdf
**Total Pages:** 31

---

## Content

```
--- Page 1 ---

Harnessing the Power of Artificial Intelligence to Vitalize
Endangered Indigenous Languages: Technologies and Experiences
Claudio Pinhanez1,2, Paulo Cavalin1, Luciana Storto2, Thomas Finbow2,
Alexander Cobbinah2, Julio Nogima1, Marisa Vasconcelos1,
Pedro Domingues1, Priscila de Souza Mizukami1, Nicole Grell2,
Majoí Gongora2, and Isabel Gonçalves1
1IBM Research Brazil
2University of São Paulo
Abstract
Since 2022 we have been exploring application
areas and technologies in which Artificial Intel-
ligence (AI) and modern Natural Language Pro-
cessing (NLP), such as Large Language Models
(LLMs), can be employed to foster the usage
and facilitate the documentation of Indigenous
languages which are in danger of disappearing.
We start by discussing the decreasing diversity
of languages in the world and how working
with Indigenous languages poses unique ethi-
cal challenges for AI and NLP. To address those
challenges, we propose an alternative develop-
ment AI cycle based on community engage-
ment and usage. Then, we report encouraging
results in the development of high-quality ma-
chine learning translators for Indigenous lan-
guages by fine-tuning state-of-the-art (SOTA)
translators with tiny amounts of data and dis-
cuss how to avoid some common pitfalls in the
process. We also present prototypes we have
built in projects done in 2023 and 2024 with In-
digenous communities in Brazil, aimed at facil-
itating writing, and discuss the development of
Indigenous Language Models (ILMs) as a repli-
cable and scalable way to create spell-checkers,
next-word predictors, and similar tools. Finally,
we discuss how we envision a future for lan-
guage documentation where dying languages
are preserved as interactive language models.
1
Introduction
Most of the recent extraordinary developments in
Artificial Intelligence (AI) and Natural Language
Processing (NLP), such as Large Language Mod-
els (LLMs), have predominantly used English lan-
guage texts and data gathered in developed coun-
tries. These advancements have primarily targeted
the needs and problems of those populations. Even
within these countries, racial, ethnic, and linguistic
minorities have been largely underrepresented in
the construction of such models and technologies.
This paper describes research and work with In-
digenous communities performed in the context of
a joint project by IBM Research and the University
of São Paulo, covering a period from early 2022
to mid-2024, under the auspices of the Center for
Artificial Intelligence (C4AI)1.
The work described in this paper is premised on
the need to increase the diversity of representation
and knowledge in the technologies and language
models being built. This involves encompassing
a broad and diverse range of languages, peoples,
places, and genders, as part of a social justice and
decolonial agenda (Buccella, 2023).
In particular, we have been working for the past
two years to create AI technologies for Indigenous
peoples in Brazil, targeting small communities in
where Indigenous languages are still in use but
under threat. About 200 languages are spoken cur-
rently in Brazil by between one to two million
people2, but the vast majority of these languages
are in danger of disappear until the end of the cen-
tury (Moseley, 2010). Many of these languages
are spoken by fewer than 100 people, often elderly,
and are at immediate risk. Even the most spoken
Indigenous language in Brazil, Tikuna, probably
has at most 50,000 speakers.
The projects and ideas described here explore
the development of technologies to support Indige-
nous communities in documenting, preserving, and
vitalizing their languages. Developing language
technologies, both for speech and text, for these
languages has been difficult in the past because of
a lack of resources and linguistic knowledge and
of appropriate computational technologies capable
of working with small amounts of data.
However, as discussed in a recent UNESCO pub-
lication (Llanes-Ortiz, 2023), “... artificial intelli-
gence, natural language processing and automated
speech recognition and voice processing could pro-
1https://c4ai.inova.usp.br/research_2/
#ProIndL_B_eng.
2According to the 2010 and 2022 Brazilian Census, respec-
tively.
arXiv:2407.12620v2  [cs.CL]  29 Jul 2024

--- Page 2 ---

vide a crucial boost to language revitalization ef-
forts, but these technologies need to be developed
in accordance with the rights and provisions set
by, among others, the Universal Declaration on
the Rights of Indigenous Peoples and the princi-
ples of Indigenous Data Sovereignty [...]. Yet, the
need to develop voice recognition, machine trans-
lation, speech processing, and text analysis tech-
nologies for Indigenous languages cannot be over-
stated.” (Llanes-Ortiz, 2023, p. 168).
The emergence of LLMs in recent years has pos-
itively changed the landscape of opportunities, in
our view, for those efforts. Paradoxically, while
LLMs need to be trained with gruesome amounts
of data, at extremely high costs, they also have
the ability to address new needs and requirements
by methods such as prompt engineering, Retrieval-
Augmented Generation (RAG), and by fine-tuning
them with small amounts of data. Although the
first two techniques do not help much in the con-
text of endangered Indigenous languages, since it
is unlikely that standard LLM models have ever
seen samples of them, the fine-tuning approach has
led to some cases of success (see a detailed review
of related works in section 7).
Fine-tuning LLMs with tiny amounts of data is
the main method explored in this work to create
useful language tools such as automatic transla-
tors, spell-checkers, and editing tools. Some of
the techniques described here may also applicable
to domains outside Indigenous languages. More-
over, from a scientific standpoint, working with
endangered Indigenous languages spoken by small
groups of people has the additional benefit of guar-
antying that all fine-tuning effects come from this
process and not from contamination errors, as dis-
cussed in (Pinhanez et al., 2023).
The recent success of LLMs is, from the tech-
nical side, a strong incentive to work on text-
based tools.
However, orality is a major com-
ponent of most Indigenous languages and, even
more troublesome, most of those languages use
writing systems which were adapted from west-
ern languages (Franchetto, 2020). In spite of that,
creating tools to foster reading and writing is very
important to strengthen endangered Indigenous lan-
guages. While young children are often the focus
of vitalization efforts, it is common for Indigenous
people to lose interest in their own language during
the teenage to early adulthood period, by means of
language attrition (Schmid, 2011).
The loss of interest in the native language is
likely compounded by the interest in using and
exploring the digital world at those ages. The chal-
lenge is furthered by the fact that it is generally
easier to forget a language that one does not know
how to read and write in (Jayasuriya et al., 1992;
Burn et al., 2014). We thus decided to focus our
activities on creating writing tools and translators
for endangered Indigenous languages, particularly
for young people and written content creators of
those languages.
The works and ideas described in this paper
are structured around three basic research themes.
First, we have been exploring how to adapt current
(and possibly create new) AI and NLP algorithms
given the constraints imposed by ultra low-resource
and endangered languages. Second, we have been
investigating whether these AI- and NLP-based
technologies can actually support Indigenous com-
munities’ language vitalization and documentation
efforts, especially in the case of endangered lan-
guages. And third, we have been looking into how
to promote the development and use of language
technologies for Indigenous communities in a sus-
tainable and ethical way.
2
Language Diversity is Decreasing
Languages are the most comprehensive record of
human linguistic and cognitive evolution (Hale
et al., 1992) and documenting and analyzing them
is as important as Archaeology and Anthropology
for understanding humanity’s past. Moreover, lan-
guages have distinct ways of organizing thinking
and comprehending reality and society (Harrison,
2008). The disappearance of a language, when its
last speaker dies, is equivalent to the destruction of
an archaeological site or the extinction of a specie.
There are about 7,000 different languages spo-
ken in the world today3, with 4,000 of them spoken
solely by approximately 370 million Indigenous
people4. Of these, 2,680 are likely to disappear by
the end of the century (Moseley, 2010). This threat
to Indigenous languages has led the United Nations
to establish 2022-2032 as the Decade of Indige-
nous Languages, in an effort led by UNESCO (UN-
ESCO, 2020b). Language endangerment is a con-
tinuum, highly dependent on the number of speak-
ers and, particularly, whether young children and
teenagers speak the language.
3https://en.wal.unesco.org/
world-atlas-languages.
4https://www.un.org/esa/socdev/unpfii/
documents/5session_factsheet1.pdf.

--- Page 3 ---

Figure 1: Histograms of 444 Indigenous languages used in the Americas today and of 221 Indigenous languages
in Brazil (based on 2010 numbers) with the number of languages for different logarithmic intervals of number of
speakers.
There are multiple ways to prevent the disappear-
ance of languages. These include ensuring they are
taught and used in schools from an early age, fos-
tering their use by teenagers and young adults, pro-
moting literacy for languages with a written form,
and making them official languages in regions with
significant numbers of speakers. Additionally, it
is important to provide social and government ser-
vices in those languages and to encourage their use
in digital contexts and social media. However, the
appropriateness of different policies and tools de-
pends on many factors including the number and
age profile of the language’s speakers.
As an example of the diversity of endangerment
conditions among Indigenous language, consider
that there are about 1,000 languages used today in
the Americas5. We could found data on the number
of speakers for 444 of these languages6. Figure 1
shows the histograms of the number of languages
considering different logarithmic intervals in the
number of speakers for those 444 American lan-
guages and for 221 languages spoken in Brazil.
In the Americas, there are 6 languages spoken
by more than 1 million people, notably Guarani,
with 6.5 million speakers, and Southern Quechua,
with 5 million speakers (as a reference, a num-
ber comparable to the speakers of Bulgarian in
the world). This group, together with the 27 lan-
guages with more than 100K speakers, such as
5https://en.wikipedia.org/wiki/Indigenous_
languages_of_the_Americas.
6Combining
data
from
https://en.wikipedia.
org/wiki/Indigenous_languages_of_the_Americas;
https://www150.statcan.gc.ca/t1/tbl1/en/
tv.action?pid=9810027101;
https://www.ibge.
gov.br/en/statistics/social/population/
18391-2010-population-census.html?edicao=19316&
t=resultados, table 1.13;
https://www2.census.gov/
library/publications/2011/acs/acsbr10-10.pdf.
Yucatec Mayan (890K), Mapuche (260K), and
Navajo (170K), are thriving languages, with reason-
able support from digital tools such as automatic
translators and word editors. There is no Indige-
nous language in Brazil with a similar number of
speakers.
The next interval consists of 54 languages with
between 10K and 100K speakers, including lan-
guages such as Cree (96K), Tikuna (47K), and
Nheengatu (20K), which already exhibit signs of
endangerment, such as a limited number of young
speakers, and have almost no support from dig-
ital tools. This group includes 5 languages spo-
ken in Brazil. The subsequent interval comprises
114 languages with between 1K and 10K speakers,
such as Choctaw (9.6K), Guarani Mbya (6K), and
Mohawk (3.9K), of which about 35 are Brazilian
languages.
We consider these two groups of 169 languages
(marked in orange in figure 1) as the major tar-
get for the research described here. For these lan-
guages, there is enough written data, as shown later,
to allow the development of digital text tools such
as translators, and enough digital and social media
literacy to enable their vitalization through digital
means. Notable examples are the two languages
we have been working with, Nheengatu (20K) and
Guarani Mbya (6K).
The interval between 100 and 1,000 speakers,
with 111 languages in the Americas, marked in
red in figure 1, includes languages such as Cho-
cho (810), Nambikwara (573), and Koyukon (300).
These languages are in severe danger of disappear-
ing and are more likely to benefit from the use of
digital technology as a support for documentation
and analysis. They are also good candidates for
the creation of interactive language preservation

--- Page 4 ---

not mentioned
in the census
0
[1-10]
[10-100)
[100-1K)
[1K,10K) [10K-40K)
Number of speakers given by Brazilian census
0
10
20
30
40
50
60
70
80
90
Number of languages covered by Wikipedia
38.5%
53.8%
55.6%
76.8%
84.4%
96.8%
100%
63.5%
84.6%
60%
60.7%
76.6%
96.8%
100%
pt
en
Unclassified
Extinct
Critically
Endgd
Severely
Endgd
Definitely
Endgd
Vulnerable
0
10
20
30
40
50
60
70
80
90
Number of Languages covered by Wikipedia
39.7%
53.8%
75.0%
73.9%
66.7%
83.6%
51.7%
84.6%
75.0%
69.6%
83.3%
76.4%
pt
en
Figure 2: Histograms of the number of Brazilian Indigenous languages with a descriptive page in Wikipedia per
number of speakers (left) and according to different levels of endangerment (right).
models described at the end of this paper. Of these
languages, 69 are spoken in Brazil.
Finally, languages with up to 100 speakers,
marked in grey and black in figure 1, are in se-
vere danger of disappearing within 20 years or less,
as most of their speakers are elderly. Traditional
efforts of documentation and preservation, possibly
aided by digital means, seem to be the most appli-
cable methodology here. There are about 132 lan-
guages in these conditions in the Americas, with
112 being languages spoken in Brazil. However,
the numbers of both languages and speakers for
this range are notoriously imprecise.
The digital situation of languages with fewer
than 1,000 speakers is often bleaker. In a study per-
formed in the context of our project (Vasconcelos
et al., 2024), we found that many Indigenous lan-
guages spoken in Brazil are likely to disappear with-
out even leaving essential digital traces. Figure 2
(left) shows that about half of the languages with
10 speakers or fewer have no entries in Wikipedia
about their existence, either in English or in Por-
tuguese. Similar observations were made for about
20% of the languages in the 10 to 1K range. Be-
yond 1,000 speakers, virtually all languages have
a descriptive entry. However, as discussed by Vas-
concelos et al. (2024), many of these pages have
limited quality and content, or have a reduced num-
ber of active editors, so information is likely to be
limited and outdated. Moreover, the lack of entries
correlates with the level of endangerment of the
languages, as shown in figure 2 (right).
3
Working with Indigenous Communities
Our work has been guided by the principle that
technologies and solutions for Indigenous peoples
must be developed with them, as stated in the Dec-
laration of Los Pinos: “Nothing for us without
us.” (UNESCO, 2020a).
Since the start of this project in 2022, we have
been engaging with many communities in Brazil,
including the Guarani Mbya, Guarani Kaiowá,
Guarani Nhandewa, Tupi, Terena, Baré, Wassu,
Tukano, Pankararu, Zoé, and Mehinako peoples.
We have also engaged organizations which work
with Indigenous communities in Brazil, such as the
Ministry of Indigenous Peoples, the Interamerican
Development Bank (BID), the Federation of the In-
digenous Organizations of the Rio Negro (FOIRN),
the National Foundation of Indigenous Peoples
(FUNAI), the Plurinational Union of Indigenous
Students (UPEI), the Socio-Environmental Institute
(ISA), and many other NGOs.
These engagements have resulted in two projects
with communities of speakers of two languages,
Guarani Mbya and Nheengatu, which we describe
in this section. However, before discussing the
projects, it is important to discuss the ethical prin-
ciples and guidelines we have used to frame our
engagement with those communities.
3.1
AI Research with Indigenous Peoples
Doing research with Indigenous peoples is sub-
jected to specific guidelines and legal constraints.
Mihesuah (1993) is a good example of a com-
prehensive set of guidelines for research with US
American Indigenous communities. Straits et al.
(2012) also proposed a set of guidelines on how to
engage in research with Native US American com-
munities based on 11 principles, including native-
centrism, co-learning and ownership, continual di-
alogue, transparency and accountability, integrity,
and community relevance.

--- Page 5 ---

Most importantly, there is a lot of distrust from
many Indigenous communities towards researchers
and academic work, resulting from a history of ex-
ploitation, disregard, and knowledge extractivism:
“... [the word research] is probably one of the
dirtiest words in the Indigenous world’s vocabu-
lary.” (Smith, 1999, p. 1). To address these issues,
Smith (1999) proposes, as part of a decolonization
perspective, that relational accountability (Wilson,
2008) should guide these engagements since it is
inherent to Indigenous ways of doing. The key
ideas behind relational accountability is that rela-
tionships with the communities are important in
research and that all the parties are responsible for
maintaining them.
Besides ethical considerations, there are legal
and regulatory procedures that must be followed
in different countries when working with specific
Indigenous communities. Particularly relevant to
our cases, of developing AI-based tools, are is-
sues related to data sovereignty, consent, and intel-
lectual property (IP) rights (Harding et al., 2012)
which should be considered in tribal research in
the USA. Research, in such cases, should include
special procedures for informed consent processes
and the involvement of community members in
defining exposure and risk to the community. Simi-
larly, Sahota (2007) discusses the need for research
regulation in American Indian and Alaska Native
communities and the challenges to establish this
regulation.
Llanes-Ortiz (2023) has proposed a research
framework based on 7 key approaches for digi-
tal initiatives with Indigenous languages, based
on: facilitating digital communication in Indige-
nous languages; multiplying Indigenous language
content online; normalizing the use of Indigenous
languages online; educating in and teaching Indige-
nous languages online; reclaiming and revitaliz-
ing Indigenous languages and knowledge digitally;
imagining and creating new digital media in Indige-
nous languages; defending spaces for Indigenous
languages and linguistic rights; and protecting In-
digenous linguistic heritage and communities.
The research described in this paper aims to ex-
plore and develop technologies which are related to
many of those issues and, in particular, to the need
to normalize the usage of Indigenous languages in
the online space. Similar issues are also discussed
by Oliveira et al. (2024), with a focus on practi-
cal aspects such as fonts, keyboards, and Unicode
representations.
When it comes to AI- and NLP-related research,
gathering, controlling, and using linguistic data be-
come essential parts of the research process and,
therefore, of ethical concerns. The sovereignty of
Indigenous data is an area that has attracted con-
siderable discussion in recent years, particularly
in the case of population and genetic data (Kuku-
tai and Taylor, 2016; Walter et al., 2021; Kukutai,
2023). Its importance for digital and AI research
has attracted some recent attention (Llanes-Ortiz,
2023). There are also some efforts to create new
agreements and practices, such as the Kaitiakitanga
data license7 proposed by members of the Maori
language community (see also the various links
provided by TeHiku8).
A more specific guide for AI-related work, in-
cluding tool and technology design methodologies,
was proposed by the The Indigenous Protocol and
Artificial Intelligence (A.I.) Working Group (Lewis
et al., 2020) as a result of two workshops with In-
digenous leaderships, linguistic professionals, and
computer researchers. Nevertheless, although large
AI conferences have hosted workshops dedicated
to Indigenous contexts, the discussion of ethical
guidelines when working with Indigenous peoples
is still limited within the AI community.
The engagement principles and ethical guide-
lines used in our research have been discussed in
more detail in (Pinhanez et al., 2023). In par-
ticular, the paper describes a practice, which we
have adopted in our work as described in the next
sections, of putting in place damage containment
procedures when dealing with Indigenous data.
Such damage containment procedures are based
in four different damage mitigation actions (Pin-
hanez et al., 2023). First, we ensure that everyone
involved in handling language data is fully aware
of the ethical issues and the dangers of releasing
data without the proper authorizations. Second, as
part of the containment process, we do not release
the data or the created models publicly, not even
among other AI researchers, which is a common
practice in the field. Third, we make sure that pro-
totypes of tools, especially in actual systems, are
only deployed or tested with express authorization
from the community, as they may generate inappro-
priate or offensive language. Fourth, the existence
7https://github.com/TeHikuMedia/
Kaitiakitanga-License
8https://tehiku.nz/te-hiku-tech/
te-hiku-dev-korero/25141/
data-sovereignty-and-the-kaitiakitanga-license.

--- Page 6 ---

of the data and its associated models, including
their shortcomings, is transparently disclosed to
the Indigenous communities and other stakehold-
ers, and protocols to control and use the data are
established.
3.2
Working in a Guarani Mbya School
In the case of the works described in this paper,
we started in 2022 to contact various Indigenous
groups and organizations in Brazil. Following a se-
ries of meetings with the Tenondé Porã community
on the outskirts of São Paulo city, in 2023 we were
invited by the community to explore the use of writ-
ing assistants by Indigenous high school students
and to conduct activities fostering community-lead
linguistic documentation and analysis. This school
is part of an Indigenous land, home to approxi-
mately 1,500 people, where the main language is
Guarani Mbya.
The Guarani Mbya language is spoken by ap-
proximately 6,000 people in Brazil (Morello and
Seiffert, 2011), mostly in the South-Southeast re-
gion.
Although it is still actively spoken and
well-studied, there are few sources of translated
texts and digitized data. Guarani Mbya belongs to
the Tupi linguistic family and it is related to the
Guarani language spoken by millions of people in
Paraguay and Bolivia. However, it is as different
from Guarani as Portuguese is from Spanish.
The invitation from the Tenondé-Porã commu-
nity led to weekly 2-hour workshops where various
technologies and prototypes were introduced to and
used by the high school students of the Gwyra Pepo
Indigenous Guarani School. The students explored
these technologies and discussed how to modify
and improve them. As a result of this work, we
developed an initial prototype of a writing assistant
for the Guarani Mbya language, which included
rudimentary electronic dictionaries, and word pre-
diction, and basic translation.
The technical aspects of those tools are discussed
in sections 4 and 5 but some of them could only be
built because we applied state-of-the-art AI technol-
ogy. For instance, the translator was developed by
fine-tuning a German-English high-quality transla-
tor using data obtained from traditional dictionar-
ies, schoolbooks, and folk tales, mostly from the
collection of Prof. Robert Dooley (Dooley, 1985,
1988a,b, 2016), an expert in Guarani Mbya.
We faced a major challenge when we began de-
signing the workshops with the high school stu-
dents. As discussed in more detail in (Pinhanez,
2023), the last 15 years have produced many schol-
arly works with cases of engagement with Indige-
nous communities for the design of digital arti-
facts (Awori et al., 2015; Muntean et al., 2017;
Taylor et al., 2017; Muashekele et al., 2019; Re-
itsma et al., 2019; Tzou et al., 2019; Moradi et al.,
2020; Shedlock and Hudson, 2022). Most of these
works focus describing key principles that design-
ers should follow when engaging with Indigenous
communities.
However, while this literature offer extensive de-
scriptions of what should be done in the design
process, it often provides very limited on how the
actual design process should happen. For instance,
when considering the use of Respectful Design, pro-
posed by Sheehan (2011), we could not find any
literature on how it should be implemented in ac-
tual design processes. There are a few exceptions
were details about how design workshops were
conducted were actually provided (Taylor et al.,
2017; Muashekele et al., 2019; Tzou et al., 2019).
However, even in those cases a systematic descrip-
tion of the methods and means was never provided
nor good ideas and practices on how to actually
conduct the design workshops.
Interestingly, some works discussing community
research related to Indigenous education, schools,
and connectivity (Franchetto, 2008a; Hermes et al.,
2012; Arola, 2017; Leal and Teles, 2022) and
Indigenous writing (Johnson, 1997; Franchetto,
2008a) were more helpful. In particular, the discus-
sion in (Arola, 2017) about being an Indigenous
person vs. doing the Indigenous way was enlight-
ening and helped us to outline some initial ideas
for the workshop.
Based on this concept, we structured our work-
shops around three principles. First, we adopted the
conversational structure observed in the three meet-
ings we had with the leadership of the Tenondé-
Porã community. In those meetings, everyone was
welcomed to voice their opinions, whenever they
felt comfortable, and the discussion progressed at
its own pace toward a consensus. In our work at
the high school, students could enter and leave the
classroom, stop to smoke their pipes, small children
were welcomed to observe, and humor and laugh-
ing were valued and welcomed, similar to what we
had observed in the meetings with the community.
Second, we began the process by exploring the
students’ current activities on the Internet, particu-
larly on WhatsApp and in the game Free Fire. This
served as a starting point to examined their use of

--- Page 7 ---

Figure 3: Photographs taken during the workshops at the Gwyra Pepo Indigenous High School in 2023.
written language and how a language aid could play
a role in their current usage. For instance, students
reported to us that sometimes they used their native
language as code to talk among themselves with
privacy in public forums of Free Fire.
Third, we tried to downplay our own eminence
as scholars, linguists, designers, and computer wiz-
ards. On the second workshop, we presented a
version of a Guarani Mbya to Portuguese transla-
tor which we knew had a poor performance. The
goal was to showcase our incompetence in their
language and also to present ourselves as people
who can fail, sometimes miserably.
In total, 14 workshops were conducted over
three months, during which different versions of
the writing assistant prototype and its components
were used and discussed within the context of vari-
ous writing activities. One of the best workshops
happened when we used, as a writing theme, im-
ages from a recent protest by the Guarani commu-
nity in São Paulo for land rights and the subsequent
confrontation with the local riot police. Possibly,
since many of them knew people involved in the
conflict, they felt more interested and engaged to
write to document their struggles.
This first engagement had limited outcomes in
terms of creating high-quality technology or de-
ploying actual writing tools. Instead, its main result
was to provide a context for us, for the students,
and for the community to understand the opportu-
nities and challenges involved in bringing AI to the
realm of Indigenous languages.
For the researchers involved in the workshops,
this engagement demonstrated the need for good
writing tools and methods to support a generation
of students who, despite being fluent in their na-
tive language, were still learning how to write in
it. While these youngsters were actively involved
in writing messages among themselves, reading
social media, and sharing content, the presence of
Guarani Mbya text in their virtual lives seemed to
be almost nonexistent.
We concluded that there is a pressing need to
develop tools to support writing among youngsters,
who encounter difficulties translating concepts and
ideas they can easily express verbally into text.
Also, it became evident how diverse their writing
abilities were and the challenge of creating support-
ing tools that could be used by students of different
levels of literacy.
Conversations with the students during and af-
ter the workshops led us to believe that the work-
shops had some positive impacts on the participat-
ing students. The presence of a team of individ-
uals, clearly unable to understand their language
but interested in developing tools to enable them
to write in it, was recognized by some as an in-
dication of the value placed on their culture. We
also observed some students expressing interesting
on learning how to use computers to improve their
writing skills, on how to employ them to gain a
better understanding of their own language, and
even on how to program them.
Finally, for the community where the school is
located, our project seemed to have contributed
to a larger discussion about how the community
wants to interact with the digital world and the
Internet. This is a community where high-speed
Internet had arrived just one year before our en-
gagement, through an optical cable provider, since
before there was very poor cell phone coverage in
the area. When we engaged with them, there were
ongoing debates about which websites and apps
the community would allow access to, and when.
We believe our project served as an opportunity
for the community to explore potentially positive
uses of these resources, in a controlled experiment.
In fact, after the four months of the project, the

--- Page 8 ---

(a) Traditional AI development cycle.
(b) AI development cycle for Indigenous communities.
Figure 4: Traditional AI development cycle (a) and the proposed AI development cycle for Indigenous communities
with emphasis on community usage, engagement, and sovereignty (b).
Tenondé-Porã expressed concerns about exposing
their language and culture to the Internet. They
requested that our activities be suspended while
the community deliberated on the proper continu-
ation of the project. We assured them that no lan-
guage data had been collected during the process,
thanked them for the opportunity to collaborate
with their students, and suspended further work on
the Guarani Mbya writing assistant, accordingly.
3.3
An AI Development Cycle Suitable for
Indigenous Communities
Consider all the different ethical issues discussed
in sections 3.1 and the lessons learned working
with the Guarani Mbya students explored in 3.2,
we started to question whether the traditional ways
AI has been often developed would work for In-
digenous communities.
Figure 4.a shows the traditional AI development
cycle to text-based systems which starts with an
initial cycle of data gathering, often from the Inter-
net, identified as data crawling, followed by model
training, and a repeating cycle of model usage,
data collection from the users’ interaction with the
model, and retraining of the model.
Is Internet crawling a feasible strategy for en-
dangered Indigenous languages? Putting aside for
a moment the issue of how to get approval and
permission from Indigenous peoples to use data
obtained from the Internet, an important techni-
cal challenge is to find public websites containing
text in endangered Indigenous languages. As dis-
cussed before, data from disappearing languages is
scarce (Vasconcelos et al., 2024), even for the lan-
guages considered here, with the number of speak-
ers ranging from 1,000 to 100,000.
To find this data, which is dispersed among vast
amounts of content in more used languages, it is
fundamental to employ automatic mechanisms for
language identification. In (Cavalin et al., 2023)
we explored the development of language identi-
fiers for 7 Brazilian Indigenous languages, using an
SVM classifier with bag-of-words features trained
on data from the Bibles dataset described in sec-
tion 4. When tested with non-Bible data, recogni-
tion accuracy varied from 37.3% to 91.7% in test
datasets with only Indigenous languages samples.
Accuracy was higher when similar languages from
the same linguistic family were considered. How-
ever, in a realistic evaluation where the data from
more commonly used non-Indigenous languages
were also present in high proportions, the perfor-
mance was much worse (Cavalin et al., 2023).
The first impulse of AI developers and scien-
tists in such conditions would be to engage the
community to create a data gathering mechanism
based on the promise of future use of the system.
In our experience, this is very difficult because of
both the difficulties in communicating how AI is
built and the common distrust of those communi-
ties towards research projects as discussed before.
Instead, our experience with the Guarani Mbya
people suggested that a different framework for AI
development is needed, centralized on the use of
the tools by the community.
Figure 4.b shows a diagram of the proposed AI
development cycle. First, it is anchored on commu-
nity engagement and community sovereignity, as
central pillars to ethically and sustainably realize
the focus of the development which is community
usage. To enable the initial use by the community,
there is an initialization step, with approval of the
community, where a starter model is built based on
linguistic data such as publicly available dictionar-

--- Page 9 ---

ies, theses, grammars, books, and similar materials.
The starter model is the seed for community usage,
even if it has shortcomings such as the translator
we used with the Tenondé Porã students.
In the AI development cycle we are proposing,
there are two sub-cycles associated the commu-
nity usage, short- and long-term. The short-term
sub-cycle follows the path of traditional AI devel-
opment with data collection and model training
activities, but in this case with direct participation
of the community in key decisions and under its
strict supervision. Also, all data collected is con-
sidered private, belongs to the community, and is
used only when authorized. The long-term sub-
cycle refers to the establishment of structures and
processes of data governance and to the training
of people and the creation of mechanisms to allow
model appropriation.
The centrality of community usage is key be-
cause it guarantees both that the tools being devel-
oped are useful and used and that the research and
development efforts provide a clear and immediate
return to the community. However, we still have
to demonstrate that development of AI tools and
systems based on this framework is feasible, use-
ful, and efficient. Some initial works exploring the
framework are presented in the next sections but
first we describe our engagement efforts to find a
community to explore those ideas with.
3.4
Working with Nheengatu Speakers
Following our engagement with the Guaranis, we
decided to focus on another Indigenous language,
Nheengatu, which is spoken by approximately
20,000 people across three different areas of the
Amazon area and in the Northeast of Brazil. This
language is used by various peoples and ethnicities,
including cases where the language was adopted
by groups after the loss of their original language,
such as the Baré people (Epps and Stenzel, 2013).
The choice of Nheengatu was motivated the
availability of public data and knowledge, its multi-
ethnic characteristic, the participation of linguistic
experts at the University of São Paulo, and ongoing
Indigenous-led initiatives focused on translation in
Nheengatu. Also, there have been some recent ef-
forts to bring Nheengatu to the digital world, such
as the self-learning tool Nheengatu app9.
In our on-going engagement with the community,
we have been working on two basic workstreams.
9Developed by Suellen Tobler, https://heengatu-app.
web.app.
First, we have recently started a partnership with a
group of Indigenous students, mostly from the Baré
ethnicity, from the State University of Campinas.
This collaboration will involve a structured writing
workshop using a new and improved version of
the Nheengatu writing assistant, ultimately lead-
ing to the development of educational and cultural
materials.
The second workstream aligns with the need
for more comprehensive translation services and
materials. The availability of translation services,
especially from dominant to Indigenous languages,
is important to increase the accessibility to legal,
health, schooling, and other government services.
At the same time, it is important that Indigenous
individuals are able to communicate in their own
language to denounce crimes, request services, and
participate in the political and social debates, mak-
ing the translation from their languages to a domi-
nant language also essential to citizenship.
In both scenarios, the goal is not to replace the In-
digenous translators but rather to make their work
more productive and reliable, allowing an often
small number of translators to support a larger
volume of demands and tasks. We are currently
establishing a collaboration with a team of pro-
fessional translators and writers in the Nheengatu
language, who recently undertook the translation of
the Brazilian Constitution into Nheengatu10. The
goal is to collaborate with them in developing a
version of the writing assistant tailored for trans-
lation tasks and, possibly, focusing on legal and
healthcare texts, incorporating as much as possi-
ble high-quality automatic translators as a way to
enhance both productivity and quality.
Our plan is to work with those communities to
build AI-based tools for Nheengatu as a proof point
that it is possible to develop such tools for endan-
gered Indigenous languages, in their typical con-
texts of ultra-low data resources. In the next two
sections, we present the methods and technologies
we have been exploring to create prototype tools
together with Indigenous communities, following
the proposed community-based AI development
cycle depicted in figure 4.b.
10https://www.cnj.jus.br/wp-content/uploads/
2023/07/constituicao-nheengatu-web.pdf.

--- Page 10 ---

4
Building Translators with Ultra-Low
Amounts of Linguistic Data
In this section we look into the technical challenges
and the solutions we have found to create bilin-
gual machine translators (MTs) for Indigenous lan-
guages based solely on publicly available linguistic
data, following the initialization process of the de-
velopment cycle of figure 4.b. Given the extremely
limited amounts of data available for most Indige-
nous languages, especially for endangered ones,
the development of translators for such languages
is only feasible today due to recent developments
in AI technology, such as the use of Transformer
technologies (Vaswani et al., 2017) and the avail-
ability of open pre-trained Large Language Models
(LLMs) (Joo et al., 2023).
The most common way to create MTs for low-
resource languages such as endangered Indigenous
Languages involves taking generic LLMs, pre-
trained on large corpus using self-supervised tech-
niques with high levels of data, and fine-tune them
with a much smaller parallel downstream corpus in
the target language (Lee et al., 2022; Mager et al.,
2023). This usually results in better translation
accuracy than training from scratch with limited
data (Adelani et al., 2022). Additionally, some
results suggest that translation quality can be im-
proved by using data from multiple languages or
multilingual models (Saleh et al., 2021).
However, our experience in building translators
for Indigenous languages has led us into a dif-
ferent direction. First, we saw that multilingual
translators often achieve falsely improved accu-
racy results by adopting a “cheating” strategy of
memorization (Cavalin et al., 2024). Furthermore,
we investigated the impact of adding more fine-
tuning data, particularly in the situation where the
additional data raised ethical concerns (Domingues
et al., 2024). Unfortunately, we observed traces
of contamination in the outputs, though in lim-
ited numbers and scope. We also found that the
most significant improvement in accuracy was ob-
tained by manually enhancing the quality of the
fine-tuning training data.
These results and associated challenges, dis-
cussed in technical detail next, suggest that it is
feasible to fine-tune LLMs into valuable bilingual
translators using data commonly available for In-
digenous languages that have been reasonably doc-
umented and studied by linguists, if some key
methodological conditions, such as data cleanli-
ness, are met. We start by describing the data
sources we used in those works and ethical issues
related to them.
4.1
The Data Used in our Research
To develop both writing assistants and translators,
we have been exploring machine learning methods
based on small amounts of data. The data used
in our work can be divided into two basic types:
data extracted from linguistic sources, such as dic-
tionaries, lexicons, theses, and publicly available
books; and data extracted from multiple versions
of the Bible available on the Internet.
We have been working exclusively with Brazil-
ian Indigenous languages (BILs). Brazil was home
to about 270 Indigenous languages according to the
2010 Census (IBGE, 2010), although some linguis-
tic experts believe the actual number is more likely
to be close to 200 (Franchetto, 2020; Storto, 2019).
Those languages were spoken by approximately
800,000 people (IBGE, 2010), with half living in In-
digenous lands, although the 2022 Census revised
this number to about 1.7 million11. Storto (2019)
provides a good overview of the history, structure,
and characteristics of a few BILs. Almost all of
these languages are considered endangered (Mose-
ley, 2010), remnants of the 1,000 languages esti-
mated to be in use in Brazil before the arrival of
Westerners 500 years ago (Rodrigues, 2019).
The first type of data comprises data extracted
from publicly available dictionaries, lexicons, the-
ses, and books. For the languages in the range of
1,000 to 100,000 speakers we are targeting, such
sources are common, mostly created through lin-
guistic research and educational efforts. We have
mostly collected resources for two languages we
have been working with, Guarani Mbya and Nheen-
gatu. The data, often in the form of PDF files,
are processed by scripts and manually, resulting in
datasets with pairs of sentences, for the training
of translators, or well-structured sentences, for the
training of encoders of Indigenous languages mod-
els and to be used in development of the writing-
support tools. Following the previous discussion,
we do not release publicly or share this data with-
out the permission of the associated Indigenous
communities.
The second type of data was collected in the
early stages of the project by researchers from IBM
Research and comprises 39 Indigenous languages
11https://biblioteca.ibge.gov.br/index.php/
biblioteca-catalogo?view=detalhes&id=2102018.

--- Page 11 ---

Name
Acron
Branch
Family
Speakers
Train
Test
Total
Bororó
bor
Macro-Jê
Bororó
1035
1861
202
2063
Apinayé
apn
Macro-Jê
Jê
1386
877
75
952
Kaingáng
kgp
Macro-Jê
Jê
19905
5695
917
6612
Kayapó
txu
Macro-Jê
Jê
5520
2669
510
3179
Xavánte
xav
Macro-Jê
Jê
11733
1275
342
1617
Karajá
kpj
Macro-Jê
Karajá
3119
2828
333
3161
Maxakali
mbl
Macro-Jê
Maxakali
1024
5566
905
6471
Rikbaktsa
rkb
Macro-Jê
Rikbaktsa
10
3560
710
4270
Mawé
maw
Tupi
Mawé
8103
6381
970
7351
Mundurukú
myu
Tupi
Mundurukú
3563
3110
190
3300
Guajajára
gub
Tupi
Tupi-Guarani
8269
4956
934
5890
Guaraní (West Bolivia)
gnw
Tupi
Tupi-Guarani
NA
5263
970
6233
Guaraní (East Bolivia)
gui
Tupi
Tupi-Guarani
NA
5263
924
6187
Guaraní Kaiowá
kgk
Tupi
Tupi-Guarani
24368
3034
479
3513
Guaraní Mbyá
gun
Tupi
Tupi-Guarani
3248
6340
970
7310
Guaraní (Paraguay)
gug
Tupi
Tupi-Guarani
NA
5196
970
6166
Ka'apor
urb
Tupi
Tupi-Guarani
1241
3380
436
3816
Kaiabi
kyz
Tupi
Tupi-Guarani
673
2187
280
2467
Nheengatu (LGA)
yrl
Tupi
Tupi-Guarani
3771
5035
691
5726
Tenharim
pah
Tupi
Tupi-Guarani
32
3215
844
4059
Jamamadí-Kanamanti
jaa
no branch
Arawá
217
4759
715
5474
Kulina Madijá
cul
no branch
Arawá
3043
4319
697
5016
Paumarí
pad
no branch
Arawá
166
3653
372
4025
Apurinã
apu
no branch
Aruak
824
6329
970
7299
Palíkur
plu
no branch
Aruak
925
6137
904
7041
Paresí
pab
no branch
Aruak
122
6381
970
7351
Teréna
ter
no branch
Aruak
6314
6381
970
7351
Wapixána
wap
no branch
Aruak
3154
5081
853
5934
Kadiwéu
kbc
no branch
Guaikurú
649
4523
793
5316
Apalaí
apy
no branch
Karib
252
5548
970
6518
Bakairí
bkq
no branch
Karib
173
4000
317
4317
Hixkaryána
hix
no branch
Karib
52
4270
472
4742
Makuxi
mbc
no branch
Karib
4675
4900
940
5840
Nadëb
mbj
no branch
Makú
326
5213
811
6024
Nambikwára
nab
no branch
Nambikwára
951
2774
844
3618
Kashinawá (Peru)
cbs
no branch Pano-Tacanan
3588
2136
130
2266
Tukano
tuo
no branch
Tukano
4412
3750
846
4596
Yanomámi
guu
no branch
Yanomámi
12301
1283
196
1479
Tikúna
tca
no branch
no family
30057
3097
386
3483
TOTAL
39
3
16
169201
162225
25808
188033
Indigenous Languages
# Aligned Sentences
Table 1:
Indigenous languages and corresponding
dataset sizes used in the study. Language name, branch,
family, and number of speakers (considering only those
who speak the language at home in an Indigenous land
in Brazil) according to the table 1.13 of the Indigenous
data of the Brazilian census of 2010 (IBGE, 2010).
spoken in Brazil, for which we found translations of
the New Testament of the Bible, a book with about
7,000 verses in its English versions. The Bible
is often available in many of these languages due
to translations by Christian churches (Franchetto,
2008b). Table 1 lists these languages, including
36 spoken primarily in Brazil and 3 Guarani-related
languages used mostly in Paraguay and Bolivia, but
also spoken in some areas in Brazil. We adopted
the Indigenous language classification, nomencla-
ture, and data from the 2010 Brazilian Census by
IBGE (IBGE, 2010) and language acronyms ac-
cording to ISO 639-3.
This dataset, referred as Bibles, was mainly ob-
tained from the ebible website12. A few other lan-
guages were sourced from the YouVersion online
platform13. The Bibles dataset consists of 188,033
parallel verses from the New Testament in English
and the 39 Indigenous languages listed in table 1.
The parallelism among translations of the same
verse, performed by some of the authors, is of rea-
sonable quality, although we are aware that the
12https://ebible.org/download.php.
13https://www.bible.com/en-GB/.
sources of the translations come from different ver-
sions, languages, and narrative styles of the Bible.
To avoid cross-contamination in the decoder and
to study memorization issues without data leakage
between the training and test sets, we used the
Matthew chapter from the New Testament as the
source for the test set, and the remainder of the
text as the training set. We are aware that some
similarity among verses could happen between the
book of Matthew and the other synoptic gospels,
such as Mark and Luke. However, we consider the
existence of some similarity to be positive, as in
most practical multi-language training datasets the
presence of similar sentences is common.
We understand that using the Bible as a source of
data for Indigenous languages raises important ethi-
cal, historical, and cultural concerns. Many unfortu-
nate aspects of past and present colonial history of
Indigenous peoples, especially in the Americas, are
connected to different forms of Christianity. At the
same time, the Bible is one of the most commonly
found documents translated to several of those lan-
guages, by Jesuits in the early days of colonization
and often by Evangelical churches and initiatives
over the last 100 years (Franchetto, 2008b). As
such, the translations of the Bible are often asso-
ciated with different forms of cultural abuse and
violence and the establishment of orthographies of
domination (Franchetto, 2008b).
However, such texts are one of the few available
sources of parallel multilingual datasets for most
Indigenous languages. We thus view the use of the
Bible in this work as an “exceptional” first step,
where it is treated as potentially “toxic” data that
should not be used, in principle, for any actually
deployed system unless with explicit agreement
of the Indigenous community. Nevertheless, we
believe Bible data can be used carefully for in-
laboratory technical experiments in well-contained
contexts, such as the studies we have performed.
To mitigate some of these risks, we implemented
the protocols suggested in (Pinhanez et al., 2023),
including the adoption of containment procedures.
4.2
The Perils of Multilingual Translators
To evaluate whether using multilingual MTs was
a effective strategy for endangered Indigenous lan-
guages, as often suggested by the literature (Lee
et al., 2022; Chen and Abdul-Mageed, 2022),
we used the Bibles dataset, and fine-tuned two
commonly-used LLMs using one bilingual and two
multilingual fine-tuning strategies.

--- Page 12 ---

The first pre-trained model is mBART50 (Tang
et al., 2020), an extended version of mBART (Liu
et al., 2020), with 680M parameters, and pre-
trained with masked language modeling on 203M
sentences. The second LLM is WMT19 (Ng et al.,
2019), a 315M-parameter German-to-English ma-
chine translator pre-trained on about 28M pairs of
translated sentences and over 500M back-translated
sentences. For more details about the experimental
methodology, refer to (Cavalin et al., 2024).
Our evaluation considered three different fine-
tuning strategies using data from the Bibles dataset,
resulting in three different types of models, evalu-
ated on two sets of test data from the same dataset.
Firstly, we assessed bilingual (BL) models created
by fine-tuning each LLMs exclusively on source-
to-target pairs from the BILs listed in table 1, yield-
ing 39 unique bilingual models. Secondly, we
considered the extreme multilingual scenario by
fine-tuning both LLMs with all languages (AL) at
once. Lastly, we created in-between multilingual
solutions, the Tupi-family (TF) models, where the
training set comprised by 10 languages belonging
to the Tupi-Guarani family.
With the goal of measuring the impact of the
previously-mentioned models, we defined two dis-
tinct sets of experiments. The first one, BL39 vs.
AL39, considered all 39 BILs in a single test set,
so that we could compare the performance of each
bilingual model on its own language test set against
a multilingual one trained with all the languages for
each language data set. The second set is BL10 vs
TF10 vs AL10, where we compared the BL models
not only against AL but also against TF, which is
more targeted at Tupi-family languages. For this,
the test dataset contained only the 10 languages
used to train the TF models.
We used three metrics to evaluate the results.
The first is the traditional BLEU score (Papineni
et al., 2002), using the average of sentence-level
BLEU scores. This allowed us to compare all
metrics with the same methodology, used by two
neural-based metrics, BLEURT (Sellam et al.,
2020) and BERTScore (Zhang et al., 2020).
A summary of the results is provided in figure 5.
As it can be seen, mBART50 performed slightly
better than WMT19 but with higher standard devi-
ation, and the three metrics afforded similar results.
The three models yielded similar results, but the
bilingual ones presented smaller standard deviation
in comparison to the AL models. The TF10 model
performed slightly better than the bilingual models
Figure 5: Average and standard deviation scores in
different test sets of languages for the fine-tuning of
mBART50 and WMT19 to different models for each of
the three metrics. The best models of each group are
indicated with the bold typeface.
but with a higher standard deviation, although the
differences were not statistically significant.
In this work, multilingual MTs did not seem to
perform better than bilingual translators. Therefore,
our conclusion was that in cases where there is
just the need for a translator for one language or
data is available for only one language, working
with a bilingual translator seems to be the natural

--- Page 13 ---

(a) mBART-BL39
(b) mBART-AL39
(c) WMT19-BL39
(d) WMT19-AL39
Figure 6: Distribution of BLEU scores of samples from
the training set for mBART50 (top) and WMT19 (bot-
tom). The peaks on the right of the AL39 histograms,
corresponding to perfect scores, are evidence of rogue
memorization strategies
choice. However, it could be argued that, in cases
where data from multiple languages is available,
the converse, that is, working with multilingual
translators, would be recommended. As described
in (Cavalin et al., 2024), this is not the case, where
we showed that high scores of the multilingual
translators were achieved not by improving the
quality of the translation, but by learning a “wrong”
strategy of memorization and retrieval, signaled by
the higher standard deviations.
In fact, we found that high standard deviations
were a symptom that the translation model had
started to perform rogue memorization, that is, it
had become a retriever of the contents of the train-
ing set instead of a translator (Cavalin et al., 2024).
This can be seen by looking at the distribution of
BLEU scores computed with samples from the
training set, shown in figure 6. From these dis-
tributions, we can clearly observe that the BL39
models (both for mBART50 and WMT19) usually
result in right-skewed normal distributions, while
for AL39 the shapes of the distributions resemble
more binomial distributions.
The high number of training samples with per-
fect translations of those models on the right side of
the histograms were obtained by the models adopt-
ing a erroneous strategy of storing internally some
of the verses, as further demonstrated in (Cavalin
et al., 2024). The paper also shows that the cause
of this pernicious learning behavior was connected
to the many-to-one mapping of the multilingual
training datasets which can be alleviated by the use
of rephrasing.
4.3
The Impact of Data Quantity
While working with the Tenondé-Porã community
and their commitment to enabling their high-school
students to write in Guarani Mbya, we consid-
ered that having translators to and from Portuguese
would be helpful. Following our experiences with
fine-tuning MTs in the context of the Bibles dataset,
we started developing a Guarani Mbya to English
MT to be used in conjunction with a commercial
English-Portuguese translator.
To train the MT, we created a dataset, referred to
as the Dictionary dataset, with pairs of sentences
from three different sources. The first source was a
set of Guarani Mbya short stories with 1,022 sen-
tences, available in Portuguese and English (Doo-
ley, 1988a,b). The second source comprised 245
texts extracted from PDF files with a pedagogical
character (Dooley, 1985). The third source was
Robert A. Dooley’s Lexical Guarani Mbya dictio-
nary (Dooley, 2016), a reference work for the lan-
guage, from which we extracted 2,230 sentence
pairs. In total, the Dictionary dataset had 3,155
training and 300 test sentence pairs.
We then considered using the Guarani Mbya
subset of the Bibles’ dataset to increase the amount
of training data. Keenly aware of the ethical issues
of using texts from the Bible in a translator for
Indigenous languages in Brazil, we conducted a
series of experiments, detailed in (Domingues et al.,
2024), to determine whether the additional “toxic”
data from the Bible was useful and, if so, how much
its use would contaminate the outputs.
As a baseline for this study, we defined
the zeroshot model, consisting of the original
German-English WMT19 model (Ng et al., 2019)
without any fine-tuning. Using only the Bibles
training set, we generated three different models
based on directly fine-tuning WMT19: mbya, the
WMT19 model fine-tuned with only the Guarani
Mbya data from the Bibles training set; TGf, the
WMT19 model fine-tuned with Bibles data from
10 languages of the Tupi-Guarani linguistic fam-
ily; and all, the WMT19 model fine-tuned with data
from all the 39 Indigenous languages of the Bibles
training set.
Using the data from the Dictionary training set,
we generated four additional models: dict, the
WMT19 model fine-tuned only with Dictionary data;
mbya>dict, the mbya model fine-tuned a second

--- Page 14 ---

Figure 7: Performance according to the metrics SacreBLEU (top) and chrF (bottom) in the Dictionary test set of the
original WMT19 model and its fine-tuning into 8 Guarani Mbya translators using different training data sets and
regimes; significant differences are also shown.
time with Dictionary data; TGf>dict: the TGf
model fine-tuned a second time with Dictionary
data; and all>dict: the all model fine-tuned
a second time with Dictionary data. Finally, we
trained mbya+dict, consisting of the WMT19 model
fine-tuned with Guarani Mbya data from the Bibles
training set and Dictionary data simultaneously.
We used two metrics to evaluate the results:
the BLEU metric, computed with the SacreBLEU
Python package (Post, 2018); and the chrF met-
ric (Popovi´c, 2015), in both cases using segment-
level scores. For the two metrics, we computed the
average and standard deviation over the score of
each sentence in the two test sets created from the
Dictionary and Bibles datasets.
Figure 7 shows the results of the 9 models, evalu-
ated with the Dictionary test data. For the two met-
rics, the zeroshot model had an extremely low
performance, as expected since it is basically a
German-to-English translator. The performance
of the three models fine-tuned with Bibles data
was poor, as expected. This becomes clearer when
comparing the dict model to them: the average ac-
curacy was considerably improved. Although dict
had a larger standard deviation, it was significantly
better than the other models (p < 0.001) for the
2 metrics, using standard one-tailed Student t-tests.
The three two-step models (marked with
->dict), had gains of about 16% to 36% in ac-
curacy over dict. The t-tests confirm that each
of these models was significantly better than dict.
The best nominal performance was achieved with
the both-at-once model, mbya+dict, across all met-
rics and test sets, although there was some statisti-
cally significant difference (p < 0.05) compared to
some of two-step models.
The results with the Dictionary test set indicated,
with high confidence and across all metrics, that
the best results were achieved by the fine-tuning of
the WMT19 model with the two types of data, from
linguistic resources and the Bible, at the same time.
In other words, the quantity of data available for
fine-tuning seems to matter, as expected, and the
best training methodology involved using all the
data together in a single fine-tuning process. A
more detailed discussion and related results are
available in (Domingues et al., 2024).
4.4
Quantifying Contamination
Having established that adding the Bible data could
improve the accuracy of the Guarani Mbya to En-
glish translator, even when tested only with non-
Bible sentences, the work then focused on quan-
tifying the extent of contamination in the output.
Specifically, we aimed to determine how many of
the translators’ outputs contained, either explicitly
or implicitly, typical words or language from the
Bible.
Table 2, from (Domingues et al., 2024), contains
a random selection of outputs for 15 sentences in
Guarani Mbya, together with the expected output.
Segments manually identified as associated with
biblical texts and expressions are marked in red, for
three of the models. All the 15 outputs of the mbya
translator have contamination, as expected since it
was trained only with Bible data, while the dict
translator, which was not exposed to Bible data in
the fine-tuning process, had none.

--- Page 15 ---

models
EXPECTED OUTPUT FROM TEST SET
mbya OUTPUT
BLEU
chrF
dict OUTPUT
BLEU
chrF
mbya+dict OUTPUT
BLEU
chrF
long ago there lived a giant.
there were two men in the crowd.
13
30
long ago there lived a giant.
100
100 long ago there lived a giant.
100
100
one day he went to the woods again.
then one of them went to the other side of 
the lake.
13
32
one day he went again to the woods.
46
76
and so one day he went again to the woods.
36
73
when he arrived at his house, he said to his 
wife, "can there be anyone who can hunt 
like me?"
when he came to the tomb, he said to his 
mother, how can i not know where i am.
17
30
when he got home, he said to his wife, "could 
it be that i'm from here?"
37
38
when he got home, he said to his wife, 
"couldn 't i find the ring?"
32
39
when he fell, he hit his back on the ground 
and died then and there.
so then, how much more will the earth 
bear down on him than the earth will bear 
down on him.
3
21
as he fell, he hit his forehead on the rock.
32
38
and as soon as he touched the ground, he 
died too.
7
30
years ago when i was a child, i didn't know 
the language of non-indians.
i have not been able to speak the word of 
the one who sent me into heaven.
3
13
years ago when i was a lot younger, i didn 't 
know what to do with the books.
29
48
years ago when i was a child, i did not 
understand the meaning of portuguese.
52
54
when my brother went, saw a snake.
when he came to my house, he saw me.
6
18
my brother went out to see the snake.
22
56 my brother went and saw the snake.
24
61
one day, one of them said to his younger 
brother, now then, i'm going to the woods.
then one of them said to him, look, i am 
going to die.
22
40
one day he said to his brother-in-law, "now i 'll 
go to the woods."
19
26
then one day he said to his brother, "now i 
'll go to the woods."
21
45
there comes an inhabitant of the hare 
village.
you are one of the twelve living creatures.
10
20
there comes the hare from the hare.
15
38
there comes the tapixi village.
15
43
each time the giant went to the woods, he 
would kill two or three peccaries.
but the one who comes after him will eat 
the bread, and the bread will come out of 
his mouth.
2
20
he went very early to the woods to kill two 
coatis, one of whom was a shotgun.
11
32
this giant will go every day to the woods 
and kill two or three people.
22
48
is your father at home?
but what do you want me to do for you
0
15
have you come yet?
8
16 your father is?
23
52
he grabbed him by his arm
so he went up to heaven with his brother.
5
12
he took his brother -in -law there.
7
12 then he took hold of the indian in the sky.
4
9
when evening came, the birds were singing 
and singing, but the indian was still stuck.
but the spirit of the spirit is in the spirit, 
and the spirit is in the spirit.
5
17
and then it was the turn to eat the birds, both 
of which were indians.
6
35
and the one who drinks the spirit remains 
in it, though the spirit remains.
3
17
you changed arbitratriously what you were if i am a believer, i will be a believer in you
3
9
if you guys believe me, i will believe you.
5
11 you will defraud me even more.
6
12
even though his face got completely 
bloodied, he smiled.
now the world was divided into three 
parts.
4
12
that type of wound has already healed lit., it 
has already healed lit., it already has peel.
2
14
he had bruising on his face.
9
17
who come with lower and higher people;
and all who are in the world and all who are 
in the world
4
17
has a lot of faith in him.
0
10
low-cost and high-cost carriers also must 
go;
7
25
dict
mbya+dict
mbya
Table 2: Examples of outputs of the mbya, dict, and mbya+dict models with SacreBLEU (marked as BLEU)
and chrF scores and the expected output from the test set; segments which are associated with biblical texts and
expressions are marked in red.
input in Guarani Mbya
expected output
generated by mbya+dict
BLEU
chrF
ha'e vy je ojuka jevy mboapy tapi'i.
he killed three tapirs
he killed three of the jesus,
24
61
yvy ku'i rataxĩ
dust.
a bagel of dust.
21
64
jaye'o 'rã kova'e poryko
let's take out the stomach of this pig.
i will pronounce this pig.
18
24
ha'e gui ma je ita ova oĩ va'e gui je peteĩ ava ramigua okẽ 
oipe'a jekuaa .
then he saw something like a man open a door in the rock 
cliff.
then just as the stone was coming out of the tomb, 
something like a man opened the door.
14
49
ha'e va'e ava poapẽ va'e ma je ogueraa nhande'i va'e omerã .
the "claw-man" took the indian home to be her husband.
this man took the indian and brought him to life.
13
36
ha'e rã je ipy jevy oja .
but his foot stuck too.
once again he washed his feet.
8
13
enhoẽ eme yaku tyrã pa remoakỹmbaxe vi tupa?
don't spill the tea or do you want to wet the bed 
completely?
do you not untie the strap of your sandals or sandals?
7
17
nhaxi' ũ oixu'u oke va'e
the pernilongs bit the one who was sleeping.
the dove dove.
5
6
xapy'a-py'a py rive nda'u mba'emo vai oiko nhandere?
will it be by chance that bad things happen to us?
have we not turned a blind eye to evil?
4
13
ha'e ndaxyi va'e rire ndoui va'erãgue
if he wasn't sick, it wouldn't have come.
if i hadn 't been born, i would have never been born.
4
23
xepoano va'e rire
if you had treated me I would have been cured.
if i die, i die;
4
4
ha'e gui ka'aru ma guyra'i onhe'ẽ-nhe'ẽ ma teĩ nhande'i va'e 
oĩ tema ha'e py .
when evening came, the birds were singing and singing, but 
the indian was still stuck.
and the one who drinks the spirit remains in it, though the 
spirit remains.
3
17
ha'e vy tu porami rei xeayvu: "você que ta veio já que risada 
guaraní," ha'e rive.
i said something like, "you what came already what laugh at 
guaraní."
he was very pleased with the way he talked about it: "we 
could have bought a hat that would belong to jesus."
3
17
yvyra kyxĩa 'y
sawing cable.
small tree with adjective subordinate prayer;
0
11
Table 3: Outputs of the mbya+dict model which were identified as possible cases of contamination; segments which
are possibly associated with biblical texts and expressions are marked in red.
The mbya+dict outputs depicted in table 2 show
only one possible case of contamination. This out-
put, “and the one who drinks the spirit remains in
it, though the spirit remains.” resembles the John
6:56 verse, “The one who eats my flesh and drinks
my blood resides in me, and I in him.”.
The qualitative evaluation of all the 300 outputs
of the mbya+dict for the Dictionary test set found
that 14 (4.7%) of the 300 outputs had some level
of contamination, including 2 obvious cases where
the word “Jesus” appeared. These 14 outputs are
shown in table 3, from (Domingues et al., 2024).
They include, as contaminated outputs, examples
where words such as “prayer”, “dove”, “bagel”
were produced; and expressions such as “washed
his feet”, “blind eye to evil”, and “if I die, I die”,
whose degree of connection to the Bible is ques-
tionable.
Based on those findings, as discussed in
(Domingues et al., 2024), we advise against the
release of the mbya+dict translator in broader con-
texts and recommend its use only in tightly con-
trolled situations where negative effects can be mit-
igated. Of course, the final decision shall be made
by the relevant Indigenous communities (Mihesuah,
1993; Sahota, 2007; Straits et al., 2012).

--- Page 16 ---

4.5
The Impact of Data Quality
In our collaboration with the high school students
of the Tenondé-Porã community, we incorporated
the dict Guarani Mbya to English translator with
a commercial, API-based English to Portuguese
translator into a writing assistant, which will be
discussed in detail in section 5. As expected, due
to the low SacreBLEU and chrF average scores (see
figure 7), the quality of the translations it generated
were of limited usefulness to the students.
Improving the quality of this translator was im-
portant, so we began by seeking a better understand-
ing of the errors it was producing and assessing the
usefulness of different parts of the output. Drawing
conclusions about human usefulness of a translator
based only on values from automatic metrics such
as SacreBLEU is challenging, since they rely on
straightforward computations such as word com-
parison and n-grams, often overlooking semantic
issues. Therefore, to determine the usefulness of
the translators, we conducted a human evaluation
on the texts generated from the test set inputs.
This evaluation, described in detail in (Pinhanez
et al., 2024) involved the ranking of each of the
generated outputs in a seven-point scale according
to how useful it would be for someone proficient in
the language using the translator as a writing sup-
port: near-perfect, correct, mostly correct, usable,
mostly incorrect, incorrect, and very wrong.
Figure 8 (left) shows the histogram of the dis-
tribution of the 300 outputs of the Guarani Mbya
translator (dict), according to the usefulness scale.
About 40% of all outputs were in the very wrong
category, with 26% categorized as incorrect and
mostly incorrect categories. Of the remaining 34%,
about 28% were sentences requiring a significant
level of human intervention to be used (usable and
mostly correct categories), with only 7% suitable
for an automatic translation scenario. As a refer-
ence, the distribution of the SacreBLEU scores of
these 300 outputs is shown in figure 8 (right).
As we moved to work with the Nheengatu
community, as discussed earlier, we decided to
apply the same techniques to develop a Nheen-
gatu to English translator. The Nheengatu dataset
comprised sentences from five different sources
with Portuguese translations.
The first source
was the Nheengatu lexicon (Ávila, 2021) with
6,846 sentences extracted from the lexicon ex-
amples. We processed the original file provided
by the author. The second source was Corpus
Lições (Ávila, 2021), containing 1,665 samples
available in a spreadsheet format.
The other
sources, extracted from PDFs, included: Texto
Anônimo (Navarro, 2011), with 427 samples; Bril-
hos na Floresta (Ishikawa, 2019), with 590 sam-
ples; and Curso LGA (Navarro, 2016), with a partial
extract of 590 samples.
In total, the Nheengatu dataset contained 7,281
samples, with a random split of 6,804 samples
for training and 233 samples (10% of the data
from all sources except Nheengatu lexicon) for
testing. We translated the Portuguese sentences to
English, when necessary, using a Portuguese-to-
English commercial translation service14.
The top row of figure 9 shows the equivalent
results of the Guarani Mbya for the Nheengatu
translator. The numbers of the Nheengatu translator
were slightly better, with 42% of the 233 outputs
in the very wrong category but only 16% in the
incorrect and mostly incorrect categories. Of the
remaining 42%, 24% would need human correction
to be usable, and 18% would be suitable for an
automatic translation scenario. The distribution of
the SacreBLEU scores of the outputs, shown on the
right side, was also better than that of the Guarani
Mbya translator, though not significantly better.
The improved results of the Nheengatu translator
can be attributed simply to the larger amount of
training data.
A side effect of the manual evaluation of use-
fulness of the outputs was that it became clear to
the team that there were many errors in the test
set, included expected outcomes which were empty
sentences and some residual lexical information in
some entries. This was mainly caused by the semi-
automatic conversion of the input materials, espe-
cially from the lexicon dictionary. This prompted
a manual, exhaustive revision of the whole train-
ing set, removing incorrect pairs and fixing oth-
ers, which resulted in the Nheengatu Clean dataset,
with 6,848 pairs, about 6% smaller than the origi-
nal Nheengatu dataset. This dataset was split into
6,621 pairs for training and 227 for testing.
The translator created using the Nheengatu
Clean dataset was remarkably better than the one
created with the original Nheengatu dataset, as
shown in the bottom row of figure 9. About 48% of
the 227 outputs were in the near perfect category,
suitable to automatic translation; 17% were correct
or mostly correct; 8% were usable; and only 27%
14IBM Watson Language Translation v9.0.0.

--- Page 17 ---

Figure 8: Histograms of the performance of the Guarani Mbya translator according to the human evaluation of
usefulness of the outputs (left) and, as a reference, the SacreBLEU metrics (right).
Figure 9: Histograms of the performance of the Nheengatu translators trained with the original data (top) and the
cleaned data (bottom) according to the SacreBLEU metrics (left) and the human evaluation of usefulness of the
outputs (right).
were unusable, summing up the very wrong, incor-
rect, and mostly incorrect categories. The average
BLEU score jumped from 18.9±16.8 with the orig-
inal dataset to 38.6 ± 47.1, flipping the histograms
of the SacreBLEU scores, as shown by the right
graphs of figure 9.
Notice that all the above gains were obtained by
removing only 6% of the entries and fixing basic er-
rors in about 10% of them. Moreover, the manual
inspection of the outputs of the original Nheen-
gatu translator seems to indicate that the translator
learned to output errors, that is, to generate empty
outputs and to include incorrect elements. What
we observed was that a fine-tuning process with
very little data seems to see errors as valid outputs
and learns to generate them. Fine-tuning LLMs
with very small amounts of data seem to require
that what is presented to the model to be heavily
curated, because the LLMs learn to generate errors
if they see even few examples of them.
These and the previous results seem to indi-
cate three important guidelines when building MTs
by fine-tuning large translators with very limited
amounts of data.
First, unlike what is recom-
mended by most of the previous literature, there is
almost no gain from using multilingual translators.

--- Page 18 ---

Second, problematic data sources should not be
used since contamination is likely to appear in the
outputs. And third, the small datasets used for fine-
tuning should be thoroughly inspected and cleaned
from errors.
5
Using AI to Create Writing Assistants
In the second workstream of our project we are
developing technologies for the creation of digital
writing assistants which can simplify and foster
the use of Indigenous languages among their com-
munities, especially teenagers and young adults.
This need was identified in our work with both the
Guarani Mbya and Nheengatu communities.
Stimulating the use of writing is also, as dis-
cussed before, one of the effective methods to di-
minish the process of forgetting a language learned
by individuals as a child. This is true both for
languages which were learned orally from family
members, friends, and community and also in cases
where the formal education process had actually
thought them how to read and write. Moreover, in
the context of increasing use of digital tools and
Internet access, providing easy ways for writing in
Indigenous languages in those media is likely to be
key to reach teenagers and young adults, often the
heaviest users of such tools.
We have been developing such writing assis-
tants within the communities using a process of
co-design where different component tools are pro-
totyped, put together, and tested with Indigenous
speakers in the context of different tasks. How
those tools are assembled, integrated, and accessed
is an essential part of the process, as well as the
development of the tools themselves. The main
tools we have been building are:
Word dictionary: a tool to provide access to
words, their meanings, and translations based
on approximate search;
Word completion: a tool which suggests words
that can complete a partially-typed word;
Next-word completion: a tool which suggests
words which can follow a partially-typed sen-
tence;
Spell checker: a tool which suggests corrections
in the words of a partially- or a fully-typed
sentence;
Translator: a tool which translates words and sen-
tences to and from the Indigenous language
and another language, or between different
orthographies of the same language.
In many ways, those are the typical writing-
support tools which languages with a large number
of speakers have easily available in word editors,
social media apps, and similar. They are often built
by dedicated, large professional teams, using tradi-
tional programming and machine learning methods,
with the support of deployment and maintenance
people. We do not believe that such resources are
likely to be made available to endangered Indige-
nous languages, what has prompted us to develop
an strategy to build those tools in the context of
limited resources and data.
Figure 10 depicts an overview of the technical
strategy we have devised based on developing In-
digenous Language Models (ILMs) by fine-tuning
existing LLMs of more resourced languages. The
fine-tuning process uses linguistic and educational
data as well as data from the Internet, extracted
and formatted by a set of training data genera-
tors, so the ILM is trained to perform the tasks
of the component tools described before, such as
word completion and spell checking. As the tools
are incorporated into applications and used by the
community, the new generated data can be used to
improve the ILMs and the tools.
There are two structuring premises behind the
proposal of this strategy. The first premise is the
admission that there are very limited data resources
for a given endangered Indigenous language and
therefore they should be used efficiently and judi-
ciously. The lack of data clearly pushes towards a
fine-tuning strategy instead of a full training model
for which there would not be enough data. At the
same time, as discussed before, fine-tuning data
must be as correct and clean as possible, suggest-
ing as much as possible the use of linguistic data
such as dictionaries, lexicons, theses, education
materials, and carefully collected web data.
The second key premise, and possibly the most
controversial, is the use of an ILM as the basis
for all tools. This ILM can be tailored to produce
the outcomes of the different component tools by
the use appropriate prompting. Using different
prompts, the same model can produce translations,
provide word and sentence completions, generate
answers to questions, or simply retrieve the mean-
ings of words.
The main reason to adopt this technical strategy
is replicability: the ILM allows all tools to share a
single knowledge and data framework which can
be built in a replicable manner from linguistic data.
At the heart of our strategy is the idea that all the

--- Page 19 ---

Figure 10: Technical strategy to develop writing assistants for low-resource Indigenous languages.
code for the development and training of the ILMs
can be openly available, built and maintained by a
community of developers following open-source
practices.
However, the data needed for the training, the
fine-tuned language model, and its use as the basis
for the writing tools should be controlled by the In-
digenous community using the governance model it
finds appropriate. If we were developing the tools
the traditional way, as a mix of programs, rules,
and machine learning, the linguistic data would be
intertwined with the code, making its separation as
open-source code and governed data much more
difficult.
As we discuss later, we are in the initial stages of
creating writing assistants using this strategy and
whether it will work is still a research question. In
the prototypes of the writing assistants we are de-
veloping, we are using a mixed approach where we
have used task-specific machine learning compo-
nents, such as in the case of translators, completion
systems, and spell checkers, and traditional proce-
dural programming, for the dictionaries. We are
doing this to accelerate the development of pro-
totypes so they can be immediately explored and
co-designed with the Indigenous communities. As
we progress and the needs and requisites become
clearer, we plan to replace the specifically created
tools with the generic ILM model.
5.1
Prototyping Writing Assistants
The development of prototypes of writing assis-
tants started about one month after we begun to
have weekly workshops at the Tenondé-Porã high
school. We employed technology probes (Hutchin-
son et al., 2003), a variation of the idea of cultural
probes (Gaver and Dunne, 1999), a.k.a. design
probes. The main idea was to insert some sort
of technological artifact into the classroom which
could elicit responses from the students in the con-
text of actual writing tasks.
The first technology probe was a rudimentary
version of the Guarani Mbya to Portuguese transla-
tor, accessible through a bare-bones Internet inter-
face. It showed it had almost no use for the students,
aggravated by the poor quality of the translations.
But it triggered good conversations with the stu-
dents about what kind of writing support would
be useful for them. Based on this feedback, we
started focusing on another component tools which

--- Page 20 ---

Figure 11: Prototype of the writing assistant developed for Guarani Mbya, May of 2023.
seemed to be more useful, such as the tools to do
word and sentence completion, and access to a dic-
tionary.
For the next iteration we created a new version
of the writing assistant, incorporating early ver-
sions of those tools. The basic layout is shown
in figure 11, comprising an area for writing in
Guarani Mbya, a button to generate translations
to Portuguese, and an area where the translation
was shown. It included a word completion tool,
shown in action in figure 11, suggesting possible
completions for the partial word “Avax” as a list in
the bottom of the interface, followed by their mean-
ings in Portuguese. The sentence completion tool
worked in identical ways except that was triggered
by the typing of spaces and punctuation marks.
We worked with the students in a couple of work-
shops with this prototype. Our anecdotal observa-
tions did not see much actual acceptance of the
suggestions provided by the tools nor much use of
the translator. However, the whole environment
seemed to be conducive to explorations and to mo-
tivate the students to write, and by the third work-
shop we started to see longer and more complex
sentences being produced as expected. This in spite
of the tools still having a very limited performance
and many students struggling with typing using the
laptops we provided (they were used to type in cell
phones). The main conclusions were that the idea
of a writing assistant as a tool to foster writing was
valid but that better component tools were needed
and, eventually, a smartphone version.
As we moved to work with the Nheengatu lan-
guage, we ported the writing assistant to Nheengatu.
The main screen of this application (in its English
version) is shown in figure 12, following basically
the same design but with some improvements in the
drop down mechanisms of the word and next-word
completion. More importantly, for the Nheengatu
language we developed a Portuguese to Nheengatu
translator which we also made available in the in-
terface (see figure 13).
We are in the process of introducing this version
of the writing assistant to two groups of Nheen-
gatu speakers. The first is composed of students of
the State University of Campinas, mostly from the
Baré ethnic group, who have very diverse knowl-
edge and fluency levels in Nheengatu. A prelimi-
nary workshop indicated that the usage is quite dif-
ferent for individuals who know and do not know
how to read and write. We could also see that the
use of the translators was more common, possi-
bly because of the better quality of our Nheengatu
translators (see figure 13 for an example) compared

--- Page 21 ---

(a) main screen
(b) word completion
(c) next word prediction
Figure 12: Main screen (top) and details of the word completion (bottom left) and of the word prediction tools
(bottom right) in the Nheengatu writing assistant prototyped in April of 2024.
to the Guarani Mbya one. We are currently organiz-
ing a writing workshop in the second half of 2024
to continue the co-design of this application.
The second group of Nheengatu speakers are In-
digenous teachers and translators who have both
a high command and a high need of writing in
Nheengatu. This collaboration is still in its initial
stages but one of our goals is to develop versions
of the writing assistant which are more appropri-
ate for writing and translation work, such as the

--- Page 22 ---

Figure 13: Translation of a sentence from Nheengatu to English in the Nheengatu writing assistant prototyped in
April of 2024.
ability to handle long texts, and investigating its in-
corporation into professional or open-source word
editors.
From the interaction we are having with teachers
and leaders of the Indigenous communities, it is
fundamental that we make the writing assistants
available in smartphones. First, the majority of
teenagers and young adults do not have access
to traditional screen-and-keyboard computers but
only to cell phones. Second, as we saw in the
work with the Guarani students, most of people in
this group do not have experience nor proficiency
with traditional keyboards, preferring the use of
thumb-based typing common in mobile phones.
And finally, in the hot and humid environment of
many Indigenous groups in Brazil, smartphones
have been much more successful in fending off
damage caused by mold and humidity.
Considering those issues, we have been explor-
ing, in parallel with the efforts described before, the
deployment of writing assistants in more readily
available platforms, such as smartphones and social
media apps. Figure 14 shows an early prototype
of the writing assistant as a chatbot in WhatsApp,
where dictionary and translation services are made
available through interactions with the chatbot15.
Currently we are starting to work on porting the
writing assistant to an Android app, together with
a system to re-configure the keyboard we have al-
ready developed16.
15This work was developed in collaboration with undergrad-
uate computer engineering students from Insper.
16Also, in a collaboration with students from Insper.
5.2
Developing the Component Tools
In the development of the actual tools used in the
prototypes of the writing assistants described in the
previous paragraphs, we did not use a single ILM
as the source of the component tools as advocated
in the description of our technical strategy shown
in figure 10. The main reason was that the process
of co-design and development of the prototypes
required to have versions of those tools working,
to some extent, in the early steps of the initializa-
tion process, as part of the new development cycle
proposed before (depicted in figure 4.b).
We now briefly describe the development pro-
cess of the tools which were actually used and
discuss how we will move to a single-source ILM
framework. Notice that the existence of those tools
will eventually simplify the training of the generic
ILM because they can be easily employed to gen-
erate prompt-like synthetic training data for the
generic ILM.
The word dictionary used in the Guarani Mbya
and Nheengatu prototypes was implemented by
looking up a database of words extracted from
actual dictionaries available for the language.
This database contained associated descriptions in
Brazilian-Portuguese and English of each word.
One shortcoming of that version was not listing
valid variations of base words, such as the use
of prefixes and suffixes to indicate gender, num-
ber and verbal tenses. Most dictionaries for major
languages used in editing tools often incorporate
the handling of variations by direct programming
rules for valid modifications, a time- and effort-
consuming process. We believe this can also be

--- Page 23 ---

Figure 14: Writing assistant for the WhatsApp platform: a request for the meaning of a word (left) and for a
translation (right); prototype of May of 2023.
achieved by training the ILM with appropriate syn-
thetic data, an idea yet to be verified in practice.
The word completion tool used in the Guarani
Mbya and Nheengatu prototypes used a variation of
the techniques used by the word dictionary, based
on partial searches in the database of words. Par-
tially entered words were matched against the list
of valid words and the most likely words were
listed in alphabetical order.
The next-word completion tool used in the
Guarani Mbya and Nheengatu prototypes have
been implement as a bag-of-words machine learn-
ing model (Weiss et al., 2010), trained with sen-
tences extracted from the bilingual datasets created
for the training of the translators, detailed before.
Next-word completion is a task extremely depen-
dent on the context and good performance is often
achieved through personalization, that is, on learn-
ing the most commonly used words by an individ-
ual. In this initial version, however, we focused on
a general-purpose training set, where we decom-
posed the original sentences in sub-sentences with
up to five tokens, and used the subsequent token as
the label to train an SVM-based classifier. Conse-
quently, when the user was typing in the writing
assistant, the system sent the typed words to the
classifier and the predicted class corresponded to
the suggested next word.
We have not yet deployed a spell checker tool
in the Guarani Mbya and Nheengatu prototypes,
but one is being developed for Nheengatu using
an LLM-based framework. The basic idea is to
first generate a dataset with pairs of correct and
incorrect sentences, where the incorrect versions
are created synthetically by changing, removing,
or adding letters, following common human pat-
terns of producing typos. We first implemented
this methodology with a dataset in Portuguese lan-
guage, where we obtained an accuracy of about
60.8%. We are currently in the process of applying
the same methodology to Nheengatu, using sen-
tences extracted from the bilingual datasets created
for the training of the translators, as we did with
the next-word prediction tool. Besides, we are also
investigating more effective ways to evaluate the
results, such as applying a BLEU-like metric to
compute the quality of the generate results.
The translator tools used in the Guarani Mbya
and Nheengatu prototypes were different versions
of the bilingual translators described previously in
detail in section 4. The translators were deployed
as API-based services and had an average response
time of 1-2 seconds, which was found adequate for
the task.
Notice that the translators we have used were
based on fine-tuning large, high-resource, high-
quality translators to Indigenous languages, gen-
erating translation-only ILMs and not generic,
prompt-based LLMs. Given that the accuracy of
translation-specific models is today often better
than of generic LLMs, it is a good question whether
having a translation-specific ILM in our technical
strategy would not be a better option. We will ex-
plore this issue as we start developing the generic-
task ILMs proposed in the strategy. An additional
issue is that translators also include a second lan-
guage to translate to and from, which may intro-
duce noise into the generic ILM.
It is also important to highlight that the strat-
egy of fine-tuning a single ILM to be a source
of the component tools requires the development
of methods and code which generate the appro-
priate synthetic training data, in the right format.
This data can be complemented, eventually, by data
logged from the writing assistants, obviously with
the permission of the users and from the commu-

--- Page 24 ---

Figure 15: Diagram of an Endangered Language Model
(ELM).
nity, and with provisions to preserve privacy and
remove personal information. We believe some
of the synthetic data generators may also require
language-specific knowledge which we will have
to be encoded and tested by developers.
Those data generators are part of the set of tools
depicted between the data sources and the fine-
tuning process in figure 10, for which we are de-
veloping generic versions which will be eventually
open-sourced, without language data. This layer
is an important area of language-specific collabo-
ration between Indigenous speakers, linguists, and
developers of each language, and how to foster
such collaborative environment and at the same
preserve governance of the Indigenous language
data is an open question.
6
Can Languages Be Documented by
Endangered Language Models?
When the last native speaker of a language dies, a
language is lost together with the large amount of
the knowledge accumulated through generations
by peoples and communities. Humanity as a whole
loses not only tacit knowledge about the world and
the culture of communities but also different ways
of thinking and structure knowledge and cognition.
When a language ceases to be spoken and used,
what is left, in the best cases, are documents and
media registering its use by previous speakers:
texts, books, recordings, videos. In many cases,
there are also linguistic material such as grammars,
dictionaries, articles and books, and other linguistic
materials with systematic, analytical descriptions
of the language. In some rare cases, such media
has been used to revitalize the language, that is,
to enable a new generation of speakers to use the
language or a good approximation of it. The most
famous case of revitalization is the case of Hebrew,
which was a lost language in the beginning of the
20th century and currently is spoken and used by
millions of people (Thomason, 2015).
The tools most commonly used today by lin-
guists for the documentation of Indigenous lan-
guages are FLEX17 and ELAN18, which create and
manage databases of annotated lexical and textual
information. FLEX allows for a text to be auto-
matically labelled or glossed with items from the
dictionary and ELAN allows for a media archive
to be transcribed and translated. Both have the
possibility of synchronizing work done in paral-
lel by more than one user. It would be ideal if
these tools could be adapted computationally to
interact with AI systems, if possible, and adapted
to smartphones, to facilitate documentation by lin-
guists and speakers. This improvements would be
of great help on making documentation less time
consuming and more accessible.
Linguistic documentation is vital for the preser-
vation and vitalization of Indigenous languages,
and native and community speakers must be able to
work actively as researchers on these databases to-
gether with non-Indigenous researchers. Moreover,
efficient tools which record the time spent by users
on the database could inaugurate a new economic
activity for Indigenous researchers, allowing doc-
umentation projects switch from grants to hourly
payments to remunerate participants.
The emergence of LLMs and interactive chatbots
based on them has created a possible new frame-
work to document an endangered language, based
on the development of Endangered Language Mod-
els (ELMs) following methodologies similar to our
technical strategy described in figure 10. Figure 15
shows the main components of the process of cre-
ating and using ELMs, including the direct inter-
action of the model with native speakers as a key
source of training data.
We are not aware of any on-going initiative to
preserve a language using this approach of creat-
ing an ELM for it but we think this is possibly a
novel way to avoid the negative aspects of losing a
language. ELMs may be able to provide future gen-
erations with more interactive ways to do research
17https://lingtransoft.info/apps/
flex-fieldworks-language-explorer.
18https://archive.mpi.nl/tla/elan.

--- Page 25 ---

on a lost language, access some of the knowledge
associated to it, and even revitalize it. We discuss
next some of the benefits of this approach and the
challenges associated with building ELMs to pre-
serve endangered languages.
The main differences between using an ELM
and the current documentation methods using me-
dias such as books and recordings is that an ELM
is more generative but less correct than traditional
documentation media. Therefore, we envision here
the use of ELMs not as a replacement for traditional
media but as a new tool in the documentation tool-
box, one that allows interactive conversation and
the easy exploration of multiple cases and situa-
tions. However, it must be used with care since
it may exhibit known problems of LLMs such as
hallucinations, biases, and fine-tuning defects such
as memorization as discussed before.
But how could such ELMs be actually built?
Should the ELM be developed carefully by ML
technicians guided by linguists, as a a way of clean-
ing the data, that is, using relevant structures which
often do not appear easily in texts and recordings,
such as paradigms and complex sentences? Or
should the ELM be trained “in the wild”, using the
help of, for instance, reinforcement learning (RL)
methods? Not only these questions seem to drive
complex technical choices but they also rely on
ethical and cultural decisions and processes which
are hard to foresee.
Linguistic documentation have dealt before with
issues of incorporating new technologies such as
the photograph, the film, the audio and video
recordings, and, more recently, the Internet and the
mobile phone, and have developed new research
protocols and methodologies. We envision a simi-
lar process would be necessary to establish ELMs
as a new form of documentation.
Finally, it is important to consider which kinds of
endangered languages are more likely to be feasibly
preserved as an ELM. Going back to our analysis
in section 2, we do not think there is going to be
enough data to train and speakers to test an ELM
in the case of languages with less than 10 speakers,
and even possibly in the case of 10 to 100 speakers,
which we depicted as black and grey bars in the
histograms of figure 1. The best candidates are
likely to be in the 100 to 1,000 range, about a third
of the Indigenous languages in the Americas and in
Brazil. For languages with more than 1,000 speak-
ers, on-the-ground initiatives of teaching young
children to speak the language seem to be a more
effective way to make sure that the language does
not disappear.
7
Previous and Related Work
The work described in this paper certainly did not
happen in a vacuum. There have been consider-
able work, especially in the last 5 years, looking
into how to apply AI technologies in support of en-
dangered languages and, in particular, Indigenous
languages. A detailed survey is beyond the scope
of this paper.
A good survey of early work was done by Mager
et al. (2018) which described work, data resources,
and challenges of language technologies for Amer-
ican Indigenous languages. Kuhn et al. (2020) de-
scribed many different language technology ini-
tiatives of the Indigenous Languages Technology
(ILT) project at the National Research Council of
Canada, including the construction of corpora for
several languages, annotation tools, speech recogni-
tion systems, and read-along audiobooks. Neubig
et al. (2020) summarized a workshop on the state
of use of technology for language documentation
in 2019. And Mager et al. (2023) presented a de-
tailed discussion on the challenges and common
approaches to develop machine translation systems
for Indigenous languages of America.
In particular, NLP technologies have been used
in varied contexts and scenarios of endangered lan-
guages. Alavi et al. (2015) discussed whether an
automatic conversational system could be used to
document languages; Anastasopoulos (2019) ex-
plored diverse language tools for language docu-
mentation; Anastasopoulos et al. (2020) discussed
modern NLP issues with endangered languages;
Bird (2018) looked into the specific issue of us-
ing mobile technologies; Cruz and Waring (2019)
listed linguistic issues of using technology for en-
dangered languages; Everson and Waring (2019)
described a platform for community-based descrip-
tion of Indigenous languages; Foley et al. (2018)
described the process of building speech recogni-
tion systems for language documentation; Katin-
skaia (2017) presented a language learning sys-
tem to support endangered languages; Maldon-
ado et al. (2016) described a system for automatic
recognition of Guarani speech; Martín-Mor (2017)
explored the use of technologies for Sardinian
languages; Maxwell and Bills (2017) discussed
how digitizing print dictionaries could help to cre-
ate data for endangered languages; Mirza (2017)

--- Page 26 ---

explored social persuasive ubiquitous knowledge
systems in the context of the Maori language;
Simha (2019) explored automatic speech recog-
nition systems; Ubahlet (2021) presented a system
to manage corpora of endangered languages; Van
Esch et al. (2019) explored future directions to
in automatic support for language documentation;
Yangarber (2018) explored support for endangered
and low-resource languages via e-Learning, trans-
lation, and crowd-sourcing; and Zuckermann et
al. (2021) studied a web platform for revival and
documentation based on community engagement.
Finally, the workshops on The Use of Computa-
tional Methods in the Study of Endangered Lan-
guages (ComputEL) are a good source of real,
field applications of technology to endangered lan-
guages19, as well as the workshops of the Spe-
cial Interest Group on Under-resourced Languages
(SIGUL) set up by the ELRA Language Resources
Association (ELRA) and the International Speech
Communication Association (ISCA)20; and the se-
ries of workshops on NLP for Indigenous Lan-
guages of the Americas (AmericasNLP)21.
8
AI is not Enough
This paper summarizes and discusses many differ-
ent works (Cavalin et al., 2023; Pinhanez et al.,
2023; Pinhanez, 2023; Pinhanez et al., 2024; Cav-
alin et al., 2024; Domingues et al., 2024; Vascon-
celos et al., 2024) developed since 2022 under the
joint project of IBM Research and the University of
São Paulo to develop AI technologies to strengthen
Brazilian Indigenous languages22. This work was
fundamentally the result of the discussions and col-
laboration we had with many Indigenous individu-
als and communities, particularly with the Tenondé-
Porã community and the Indigenous speakers and
linguists of Nheengatu.
It would be naive of us to pretend that AI tech-
nology can save endangered Indigenous languages
from decline and disappearance. First, for many
Indigenous communities, the loss of their language
is, regretably, the by-product of the disappearance
of their own community or ethnicity. Many Indige-
nous communities are under threat of expulsion
from their lands, of violence, and of economic
exploitation. Moreover, history is adamant that
19https://computel-workshop.org/
20https://www.sigul.eu/
21https://turing.iimas.unam.mx/americasnlp/
22https://c4ai.inova.usp.br/research_2/
#ProIndL_B_eng.
languages are vitalized by their own communities,
under their own practices and motives, in complex
socio-political processes undertaken by their native
speakers (Thomason, 2015; Carroll et al., 2020).
In particular, we should be careful with the por-
trayal of AI tools as “white savior” technologies,
and see the role of our work, described in this pa-
per, as the exploration of technologies which some
communities may adopt, use, and, eventually, ap-
propriate, at their own discretion and decision.
Moreover, as discussed in the first part of the
paper, the development of AI-based tools has to
be done with and for the Indigenous communities,
under ethical principles and relational accountabil-
ity (Wilson, 2008). In the case of AI, and ML tools
in particular, issues of data sovereignty, consent,
and intellectual property are particularly impor-
tant (Harding et al., 2012; Walter et al., 2021; Kuku-
tai and Taylor, 2016; Kukutai, 2023), although hard
to communicate and to reach agreement on. Efforts
to create new agreements and practices, such as the
Kaitiakitanga data license23 seem to be going in
the right direction.
From a technical standpoint, we believe our work
has been contributing in many ways to the under-
standing of the possibilities of AI technology in
the context of vitalization of endangered Indige-
nous languages. We believe our proposal of an
AI development cycle focused on community us-
age, engagement, and sovereignty, described in
section 3.3 is a good way to address some of the
key ethical issues discussed in section 3.1. In sec-
tion 4, we have shown that fine-tuning machine
translators with ultra-low amounts of data has to be
done with extreme care, due both to memorization
effects and the dangers of contamination. We also
provided evidence that data quantity matters and,
more importantly, that data quality is essential.
Our work with writing assistants described in
section 5, although in its early stages, is develop-
ing methodologies and practices for co-designing
writing-support tools for Indigenous communities
and exploring the feasibility of a technical strat-
egy we proposed based on Indigenous Language
Models (ILMs). Finally, we are proposing here a
new form of language documentation based on En-
dangered Language Models (ELMs) where some
of the technologies developed for translators and
writing assistants may be applicable.
23https://github.com/TeHikuMedia/
Kaitiakitanga-License

--- Page 27 ---

Overall, we have been developing a set of tech-
nologies and methods which explore how to har-
ness the recent advances in AI to support the vital-
ization of endangered Indigenous languages. The
use of the term “harness” here and in the title of
this paper is intentional, because the two meanings
of the term represent well our main goals. “To har-
ness” can be understood as “to control”, which is
a good way to view our efforts to use fine-tuning
mechanisms to harness high-resource MTs to pro-
duce translations of Indigenous languages, or the
methodology we are using to develop spell check-
ers. But “to harness” can also mean “to utilize” the
power of AI, and particularly of modern NLP tech-
nologies such as LLMs, to create tools that would
otherwise be impossible or very difficult to build.
The research described here should be regarded
as the initial results of our project. We are still in
the beginning of our engagement with the Nheen-
gatu writers and translators and we expect many
new design and development ideas to be created
as we work together and see those and new tools
being developed. Equally, the development and
use of writing assistants are in the infancy, and we
hope that the coming workshops with Nheengatu-
speaking students will take the design and deploy-
ment of those tools in new directions. We are also
exploring, with other Indigenous communities and
related organizations, how such tools could be used
in other contexts, such as law, health, and educa-
tion, and in the support of economic activities.
From a technical view, we are continuing the
exploration of techniques to build better transla-
tors, exploring different methods of fine-tuning,
and looking into how to produce synthetic data.
We also want to work with other research groups
to allow them to use our translator-development
tools to create translators for other languages, to
ensure that the technology is replicable. In the
case of writing assistants, our main goal is to finish
the development of a first, complete, usable proto-
type which can be used and tested by a large and
diverse community of users, delivered from multi-
ple platforms. The next step is to move towards a
single-source ILM able to provide the functionality
of all the component tools (except, possibly, trans-
lation, as discussed before). The following step
would be the creation of a set of basic training data
generators, closing the ILM production cycle, and
then work with multiple communities to use and
enhance the technological framework.
During the first day of our first workshop at
the Tenondé-Porã high school, one of the students
asked us when we would start teaching them com-
puter science. We are aware that this project will
not be successful in producing real impact if the
technologies developed are not transferred and ap-
propriated by the Indigenous communities, as part
of the “community sovereingty” long-term process
of the proposed AI development cycle (see fig-
ure 4.b). A parallel effort is needed to cultivate
Indigenous linguists, computer scientists, program-
mers, and UX designers to ensure the continuity of
successful tools and technologies.
Many Indigenous leaders we have talked to are
cognizant of the importance of empowering their
communities with digital tool-making technologies.
The adoption, adaptation, and appropriation of new
technologies by non-Indigenous people have been
the history and the reality for most of these com-
munities for the last 500 years. In many ways, our
project will be really successful when our involve-
ment is no longer necessary, and Indigenous com-
munities are fully empowered to independently de-
velop, utilize, manage, and govern these language
and AI technologies.
Acknowledgements
Most and foremost, we acknowledge the vast
amounts of knowledge and wisdom we have gen-
erously received from the people we worked with
in the Indigenous communities, from their leader-
ships, and from people of NGOs who work with
them: the teachers and students of the Gwyra
Pepo Guarani School, in the Tenondé Porã com-
munity, in particular Jordi Karai Mirim and Joana
Cabral de Oliveira, and from Talita Lazarin Dal
Bo and Ana Luísa Brites Blaser from the “Pro-
grama de Educação do Comitê Interaldeias”; from
the Nheengatu community, Arlindo Baré, Clau-
dia Baré, Elizângela Baré, Cauã Borari, Édson
Baré Warixi, Melvino Baré, and Marivelton Bar-
roso Baré; and from the Terena community, Dario
Terena. We also acknowledge the work of under-
graduates who were involved at different stages
of this work: Caio Medeiros, Marina Geiger, and
Sofia Cabral from the University of São Paulo, and
Carolina Souza from MIT.
We also want to thank the people who have been
worked with us in this project but whose work is
not directly reflected in the works described here:
professors Sarajane Peres, Antônio Cândido, and
Marcelo Finger from the University of São Paulo,

--- Page 28 ---

and Karin Vivanco from the State University of
Campinas; and the student Gustavo Evangelista.
We also thank many people who have allowed us
to access results, data, and publications related to
Indigenous languages: prof. Robert Dooley, prof.
Marcel D’Avila, and prof. Eduardo Navarro.
Finally we acknowledge the leadership of the
institutions who have supported this work: Bruno
Flach and Stacy Hobson from IBM Research, pro-
fessor Fábio Cozman of the Center for Artificial
Intelligence (C4AI) of the University of São Paulo,
and Rosabelli Coelho-Keyssar of the MIT Brazil
Program.
This work has been partially funded by the Cen-
ter for Artificial Intelligence (C4AI-USP), with sup-
port by the FAPESP (São Paulo Research Founda-
tion, grant #201907665-4) and by the IBM Corpo-
ration.
References
David Adelani, Jesujoba Alabi, Angela Fan, Julia
Kreutzer, Xiaoyu Shen, Machel Reid, Dana Ruiter,
Dietrich Klakow, Peter Nabende, Ernie Chang, Tajud-
deen Gwadabe, Freshia Sackey, Bonaventure F. P.
Dossou, Chris Emezue, Colin Leong, Michael Beuk-
man, Shamsuddeen Muhammad, Guyo Jarso, Oreen
Yousuf, Andre Niyongabo Rubungo, Gilles Hacheme,
Eric Peter Wairagala, Muhammad Umair Nasir, Ben-
jamin Ajibade, Tunde Ajayi, Yvonne Gitau, Jade
Abbott, Mohamed Ahmed, Millicent Ochieng, An-
uoluwapo Aremu, Perez Ogayo, Jonathan Mukiibi,
Fatoumata Ouoba Kabore, Godson Kalipe, Derguene
Mbaye, Allahsera Auguste Tapo, Victoire Memd-
jokam Koagne, Edwin Munkoh-Buabeng, Valen-
cia Wagner, Idris Abdulmumin, Ayodele Awokoya,
Happy Buzaaba, Blessing Sibanda, Andiswa Bukula,
and Sam Manthalu. 2022. A few thousand transla-
tions go a long way! leveraging pre-trained mod-
els for African news translation. In Proceedings of
the 2022 Conference of the North American Chap-
ter of the Association for Computational Linguistics:
Human Language Technologies (NAACL’24), pages
3053–3070, Seattle, United States. Association for
Computational Linguistics.
S. Alavi, J. Brixey, and D. Traum. 2015. Can we use
a spoken dialogue system to document endangered
languages? In Dialog for Good Conference.
A. Anastasopoulos. 2019. Computational tools for en-
dangered language documentation.
Ph.D. thesis,
University of Notre Dame.
A. Anastasopoulos, C. Cox, G. Neubig, and H. Cruz.
2020. Endangered languages meet modern NLP. In
Proc. of COLING’20.
K. Arola. 2017. Indigenous interfaces. In D. Walss and
S. Vie, editors, Social writing/social media: Publics,
presentations, and pedagogies. Elsevier.
M. T. Ávila. 2021. Proposta de dicionário nheengatu-
português.
Tese de doutorado, Faculdade de
Filosofia, Letras e Ciências Humanas, Universidade
de São Paulo, São Paulo. Recuperado em 2023-12-
27, de www.teses.usp.br.
K. Awori, F. Vetere, and W. Smith. 2015. Transnational-
ism, indigenous knowledge and technology: Insights
from the kenyan diaspora. In CHI’15.
S. Bird. 2018. Designing mobile applications for endan-
gered languages. In Oxford Handbook of Endangered
Languages, pages 842–861. Oxford University Press.
Alessandra Buccella. 2023. “AI for all” is a matter of
social justice. AI and Ethics, 3(4):1143–1152.
Jo Anna Burn, Ineke Crezee, Kim Hastwell, Elizabeth
Brugh, and Rosemary Harison. 2014. ‘I study long,
long time in my language, so I never forget it’: read-
ing and first language maintenance. Intercultural
Education, 25(5):377–390.
S. Carroll, I. Garba, O. Figueroa-Rodríguez, J. Hol-
brook, et al. 2020.
The CARE principles for In-
digenous data governance. Data Science Journal,
19(1):43. Number: 1.
Paulo Cavalin, Pedro Domingues, Julio Nogima, and
Claudio Pinhanez. 2023. Understanding native lan-
guage identification for brazilian indigenous lan-
guages. In Proceedings of the Workshop on Natural
Language Processing for Indigenous Languages of
the Americas (AmericasNLP’23), pages 12–18.
Paulo Cavalin, Pedro H. Domingues, Claudio Pinhanez,
and Julio Nogima. 2024. Fixing rogue memorization
in many-to-one multilingual translators of extremely-
low-resource languages by rephrasing training sam-
ples. In Proceedings of the 2024 Annual Conference
of the North American Chapter of the Association for
Computational Linguistics (NAACL’24).
Wei-Rui Chen and Muhammad Abdul-Mageed. 2022.
Improving neural machine translation of indigenous
languages with multilingual transfer learning. arXiv
preprint: 2205.06993.
H. Cruz and J. Waring. 2019. Deploying technology to
save endangered languages. ArXiv, abs/1908.08971.
Pedro Domingues, Claudio Pinhanez, Paulo Cavalin,
, and Julio Nogima. 2024. Quantifying the ethical
dilemma of using culturally toxic training data in ai
tools for indigenous languages. In Proceedings of
3rd Annual Meeting of the Special Interest Group on
Under-resourced Languages (SIGUL’24)).
Robert Dooley. 1985. Nhanhembo’e aguã nhandeayvu
py [1-5].
Robert A. Dooley. 1988a. Arquivo de textos indígenas
– guaraní (dialeto mbyá) [1].

--- Page 29 ---

Robert A. Dooley. 1988b. Arquivo de textos indígenas
– guaraní (dialeto mbyá) [2].
Robert A. Dooley. 2016. Léxico guarani, dialeto mbyá:
Guarani-português.
Patience Epps and Kristine Stenzel. 2013. Upper rio
negro: cultural and linguistic interaction in north-
western amazonia. Rio de Janeiro: Museu Nacional.
R. Everson, W. Honoré, and S. Grimm. 2019. An online
platform for community-based language description
and documentation. In Proc. of ComputEL’19.
B. Foley, J. Arnold, R. Coto-Solano, G. Durantin, et al.
2018. Building speech recognition systems for lan-
guage documentation: the CoEDL endangered lan-
guage pipeline and inference system (ELPIS). In
Proc of SLTU’18.
B. Franchetto. 2008a. A guerra dos alfabetos: os povos
indígenas na fronteira entre o oral e o escrito. Mana,
14.
Bruna Franchetto. 2008b. The war of the alphabets:
indigenous peoples between the oral and the written.
Mana, 4:31–59.
Bruna Franchetto. 2020. Língua (s): cosmopolíticas,
micropolíticas, macropolíticas. Campos-Revista de
Antropologia, 21(1):21–36.
William Gaver and Anthony Dunne. 1999. Projected
realities: conceptual design for cultural effect. In
Proceedings of the SIGCHI conference on Human
Factors in Computing Systems, pages 600–607.
K. Hale, M. Krauss, L. Watahomigie, A. Yamamoto,
C. Craig, M. Jeanne, and N. England. 1992. Endan-
gered languages. Language, 68(1):1–42.
Anna Harding, Barbara Harper, Dave Stone, Catherine
O’Neill, Patricia Berger, Stuart Harris, and Jamie
Donatuto. 2012. Conducting research with tribal
communities: Sovereignty, ethics, and data-sharing
issues. Environmental health perspectives, 120(1):6–
10.
K. Harrison. 2008. When languages die: The extinction
of the world’s languages and the erosion of human
knowledge. Oxford University Press.
M. Hermes, M. Bang, and A. Marin. 2012. Designing
indigenous language revitalization. Harvard Educa-
tional Review, 82(3).
Hilary Hutchinson, Wendy Mackay, Bo Westerlund,
Benjamin B Bederson, Allison Druin, Catherine
Plaisant, Michel Beaudouin-Lafon, Stéphane Con-
versy, Helen Evans, Heiko Hansen, et al. 2003. Tech-
nology probes: inspiring design for and with families.
In Proceedings of the SIGCHI conference on Human
factors in computing systems, pages 17–24.
IBGE. 2010. Censo demográfico 2010. Accessed on
2022-12-30.
Noemia Kazue Ishikawa. 2019. Brilhos na Floresta.
Editora Valer; Editora Inpa, Manaus.
Laksiri Jayasuriya, David Sang, and Angela Fielding.
1992. Ethnicity, immigration and mental illness: A
critical review of Australian research. Bureau of
immigration research.
C. Johnson. 1997. Levi-strauss: The writing lesson
revisited. The Modern Language Review.
Ha-Young Joo, Hyeontaek Oh, and Jinhong Yang. 2023.
A survey on open source based large language mod-
els.
The Journal of Korea Institute of Informa-
tion, Electronics, and Communication Technology,
16(4):193–202.
A. Katinskaia, J. Nouri, and R. Yangarber. 2017. Re-
vita: a system for language learning and supporting
endangered languages. In Proc. of the workshop on
NLP for CALL and for Language Acquisition.
P. Kruthika. 2019. Improving automatic speech recog-
nition on endangered languages.
Master’s thesis,
Rochester Institute of Technology.
R. Kuhn, F. Davis, A. Désilets, E. Joanis, et al. 2020.
The Indigenous languages technology project at NRC
Canada: An empowerment-oriented approach to de-
veloping language software. In Proc. of COLING’20,
pages 5866–5878.
Tahu Kukutai. 2023. Indigenous data sovereignty—a
new take on an old theme.
Tahu Kukutai and John Taylor. 2016. Indigenous data
sovereignty: Toward an agenda. ANU press.
D.C. Leal and E.C. Teles. 2022. Tangible and intangi-
ble spaces of community connectivity. Interactions,
29(3):62–65.
En-Shiun Lee, Sarubi Thillainathan, Shravan Nayak,
Surangika Ranathunga, David Adelani, Ruisi Su,
and Arya McCarthy. 2022.
Pre-trained multilin-
gual sequence-to-sequence models: A hope for low-
resource language translation? In Proceedings of the
60th Annual Meeting of the Association for Computa-
tional Linguistics - Findings (ACL’22), pages 58–67,
Dublin, Ireland. Association for Computational Lin-
guistics.
J. Lewis, A. Abdilla, N. Arista, K. Baker, et al. 2020.
Indigenous protocol and artificial intelligence posi-
tion paper. Indigenous Protocol and Artificial Intelli-
gence Working Group.
Yinhan Liu, Jiatao Gu, Naman Goyal, Xian Li, Sergey
Edunov, Marjan Ghazvininejad, Mike Lewis, and
Luke Zettlemoyer. 2020. Multilingual denoising pre-
training for neural machine translation.
Transac-
tions of the Association for Computational Linguis-
tics, 8:726–742.
Genner Llanes-Ortiz. 2023. Digital initiatives for in-
digenous languages. UNESCO Publishing.

--- Page 30 ---

M. Mager, X. Gutierrez-Vasques, G. Sierra, and I. Meza.
2018. Challenges of language technologies for the
Indigenous languages of the Americas. In Proc. of
COLING, page 55—69.
Manuel Mager, Rajat Bhatnagar, Graham Neubig,
Ngoc Thang Vu, and Katharina Kann. 2023. Neural
machine translation for the indigenous languages of
the Americas: An introduction. In Proceedings of
the Workshop on Natural Language Processing for
Indigenous Languages of the Americas (Americas-
NLP), pages 109–133, Toronto, Canada. Association
for Computational Linguistics.
D. Maldonado, R. Villalba Barrientos, and D. Pinto-Roa.
2016. Eñe’e: Sistema de reconocimiento automático
del habla en Guaraní. In Simposio Argentino de In-
teligencia Artificial (ASAI 2016).
A. Martín-Mor. 2017. Technologies for endangered
languages: The languages of Sardinia as a case in
point. MTm, 9:365–86.
M. Maxwell and A. Bills. 2017. Endangered data for
endangered languages: Digitizing print dictionaries.
In Proc. of ComputEL’17.
Devon A Mihesuah. 1993. Suggested guidelines for
institutions with scholars who conduct research on
american indians. American Indian Culture and Re-
search Journal, 17(3):131–139.
A. Mirza. 2017. Design and implementation of social
persuasive ubiquitous knowledge systems to revitalise
endangered languages. Ph.D. thesis, Auckland.
F. Moradi, L. Öhlund, H. Nordin, and M. Wiberg. 2020.
Designing a digital archive for indigenous people:
understanding the double sensitivity of design. In
NordCHI’10.
Rosângela Morello and Ana Paula Seiffert, editors. 2011.
Inventário da Língua Guarani Mbya - Inventário Na-
cional da Diversidade Linguística. Editora Gara-
puvu, Florianópolis, Brazil.
Christopher Moseley. 2010. Atlas of the World’s Lan-
guages in Danger. Unesco.
C. Muashekele, H. Winschiers-Theophilus, and G. Ka-
puire. 2019. Co-design as a means of fostering appro-
priation of conservation monitoring technology by
indigenous communities. In Proc. of the 9th Interna-
tional Conference on Communities & Technologies-
Transforming Communities.
A. Muntean, R.and Antle, B. Matkin, K. Hennessy,
S. Rowley, and J. Wilson. 2017. Designing cultural
values into interaction. In CHI’17.
Eduardo de Almeida Navarro. 2011. Um texto anônimo,
em língua geral amazônica, do século xviii. Revista
USP, 90:181–192.
Eduardo de Almeida Navarro. 2016. Curso de língua
geral (nheengatu ou tupi moderno): a língua das
origens da civilização amazônica, 2 edition. Edição
do Autor, São Paulo.
G. Neubig, S. Rijhwani, A. Palmer, J. MacKenzie, et al.
2020. A summary of the first workshop on language
technology for language documentation and revital-
ization. arXiv preprint arXiv:2004.13203.
Nathan Ng, Kyra Yee, Alexei Baevski, Myle Ott,
Michael Auli, and Sergey Edunov. 2019. Facebook
FAIR’s WMT19 news translation task submission.
In Proceedings of the Fourth Conference on Machine
Translation (Volume 2: Shared Task Papers, Day
1), pages 314–319, Florence, Italy. Association for
Computational Linguistics.
Janine Oliveira, Marison Ranieri Rodrigues de Freitas,
and Delaney Gomez-Jackson. 2024. Hello Indige-
nous: a blueprint on the preservation of endangered
Indigenous languages through digital inclusion. UN-
ESCO Publishing.
Kishore Papineni, Salim Roukos, Todd Ward, and Wei-
Jing Zhu. 2002. Bleu: a method for automatic evalu-
ation of machine translation. In Proceedings of the
40th Annual Meeting of the Association for Computa-
tional Linguistics (ACL’02), pages 311–318, Philadel-
phia, Pennsylvania, USA. Association for Computa-
tional Linguistics.
C. Pinhanez, P. Cavalin, M. Vasconcelos, and J. Nogima.
2023. Balancing social impact, opportunities, and
ethical constraints of using ai in the documentation
and vitalization of indigenous languages. In Proc. of
the 2023 International Joint Conference on Artificial
Ingelligence (IJCAI’23), Macao, China.
Claudio Pinhanez, Paulo Cavalin, and Julio Nogima.
2024. Human evaluation of the usefulness of fine-
tuned english translators for the guarani mbya and
nheengatu indigenous languages. In Proceedings of
First Workshop on NLP for Indigenous Languages of
Lusophone Countries (ILLC-NLP’24).
Claudio Santos Pinhanez. 2023. How to structure the
design workshop of a conversational language aid
for/with an indigenous community?
In Proc. of
the Conversational User Interfaces workshop of the
CHI’23 (CUIatCHI’23).
Maja Popovi´c. 2015. chrF: character n-gram F-score
for automatic MT evaluation. In Proceedings of the
Tenth Workshop on Statistical Machine Translation,
pages 392–395, Lisbon, Portugal. Association for
Computational Linguistics.
Matt Post. 2018. A call for clarity in reporting BLEU
scores. In Proceedings of the Third Conference on
Machine Translation: Research Papers, pages 186–
191, Brussels, Belgium. Association for Computa-
tional Linguistics.
L. Reitsma, A. Light, T. Zaman, and P. Rodgers. 2019.
A respectful design framework. incorporating indige-
nous knowledge in the design process. The Design
Journal, 22.

--- Page 31 ---

Aryon Dall’Igna Rodrigues. 2019. Línguas indígenas:
500 anos de descobertas e perdas. DELTA: Documen-
tação e Estudos em Linguística Teórica e Aplicada,
9(1).
P. Sahota. 2007. Research regulation in American In-
dian/Alaska native communities: Policy and practice
considerations. In NCAI.
Fahimeh Saleh, Wray Buntine, Gholamreza Haffari, and
Lan Du. 2021. Multilingual neural machine transla-
tion: Can linguistic hierarchies help? In Proceedings
of the 2021 Conference on Empirical Methods in
Natural Language Processing (EMNLP 2021), pages
1313–1330, Punta Cana, Dominican Republic. Asso-
ciation for Computational Linguistics.
Monika S Schmid. 2011. Contact x time: External
factors and variability in l1 attrition. Modeling bilin-
gualism: From structure to chaos, pages 155–176.
Thibault Sellam, Dipanjan Das, and Ankur P Parikh.
2020. Bleurt: Learning robust metrics for text gen-
eration. In Proceedings of the 48th Annual Confer-
ence of the Association of Computational Linguistics
(ACL’20). Association for Computational Linguis-
tics.
K. Shedlock and P. Hudson. 2022. Kaupapa m¯aori con-
cept modelling for the creation of m¯aori it artefacts.
Journal of the Royal Society of New Zealand, 52.
N. Sheehan. 2011. Indigenous knowledge and respect-
ful design: An evidence-based approach. Design
Issues, 27(4).
L. Smith. 1999. Decolonizing methodologies: research
and Indigenous peoples. Zed Books ; University of
Otago Press.
Luciana Raccanello Storto. 2019. Línguas indígenas:
tradição, universais e diversidade. Mercado de Le-
tras.
K. Straits, D Bird, E. Tsinajinnie, J. Espinoza, et al.
2012. Guiding principles for engaging in research
with Native American communities. UNM Center
for Rural and Community Behavioral Health.
Yuqing Tang, Chau Tran, Xian Li, Peng-Jen Chen, Na-
man Goyal, Vishrav Chaudhary, Jiatao Gu, and An-
gela Fan. 2020. Multilingual translation with exten-
sible multilingual pretraining and finetuning. arXiv
preprint: 2008.00401.
J. Taylor, A. Soro, P. Roe, A. Lee Hong, and M. Br-
ereton. 2017. Situational when: Designing for time
across cultures. In CHI’17.
S. Thomason. 2015. Endangered languages. Cam-
bridge University Press.
C. Tzou, Meixi, E. Suárez, P. Bell, D. LaBonte,
E. Starks, and M. Bang. 2019. Storywork in stem-
art: Making, materiality and robotics within everyday
acts of indigenous presence and resurgence. Cogni-
tion and Instruction, 37(3).
I. Ubaleht. 2021. Lexeme: the concept of system and
the creation of speech corpora for two endangered
languages. In Proc. of ComputEL’21.
UNESCO. 2020a. Los pinos declaration [chapoltepek] –
making a decade of action for indigenous languages.
https://en.unesco.org/sites/default/
files/los_pinos_declaration_170720_en.pdf.
Accessed: 2022-02-02.
UNESCO. 2020b.
Upcoming decade of indige-
nous languages (2022 – 2032) to focus on
indigenous
language
users’
human
rights.
https://www.un.org/development/desa/
indigenouspeoples/about-us/73pga.html.
Accessed: 2022-02-02.
D. van Esch, B. Foley, and N. San. 2019. Future direc-
tions in technological support for language documen-
tation. In Proc. of ComputEL, volume 1.
Marisa Vasconcelos, Priscila de Souza Mizukami, and
Claudio Santos Pinhanez. 2024. Disappearing with-
out a trace: Coverage, community, quality, and tem-
poral dynamics of wikipedia articles on endangered
brazilian indigenous languages. In Proc. of the 18th
International AAAI Conference on Web and Social
Media (ICSWM’24).
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob
Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz
Kaiser, and Illia Polosukhin. 2017. Attention is all
you need. In Proc. of Advances in Neural Informa-
tion Processing Systems (Neurips’17).
Maggie Walter, Tahu Kukutai, Stephanie Russo Carroll,
and Desi Rodriguez-Lonebear. 2021.
Indigenous
data sovereignty and policy. Taylor & Francis.
Sholom M. Weiss, Nitin Indurkhya, and Tong Zhang.
2010. Fundamentals of Predictive Text Mining, 1st
edition. Springer Publishing Company, Incorporated.
S. Wilson. 2008. Research is ceremony: Indigenous
research methods. Fernwood Publishing.
R. Yangarber. 2018. Support for endangered and low-
resource languages via e-learning, translation and
crowd-sourcing. In Proc. of FEL, pages 90–97.
Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q.
Weinberger, and Yoav Artzi. 2020. Bertscore: Evalu-
ating text generation with bert. In Proc. of the 2020
International Conference on Learning Representa-
tions (ICLR’20).
G. Zuckerman, S. Vigfússon, M. Rayner, N. Chiaráin,
et al. 2021. LARA in the service of revivalistics and
documentary linguistics: Community engagement
and endangered languages. In Proc. of ComputEl’21,
pages 13–23.

```
