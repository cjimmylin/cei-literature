---
title: "2024-Grezes-“It’s how you do things that matters” Attending to Process to Better - PDF Extract"
source_pdf: "2024-Grezes-“It’s how you do things that matters” Attending to Process to Better.pdf"
pages: 8
extracted_at: "2026-02-13T13:57:11.388764"
---

# PDF Extract: 2024-Grezes-“It’s how you do things that matters” Attending to Process to Better

**Source PDF:** 2024-Grezes-“It’s how you do things that matters” Attending to Process to Better.pdf
**Total Pages:** 8

---

## Content

```
--- Page 1 ---

“It’s how you do things that matters”: Attending to Process to Better Serve
Indigenous Communities with Language Technologies
Ned Cooper∗
Australian National University
edward.cooper@anu.edu.au
Courtney Heldreth
Google Research, USA
cheldreth@google.com
Ben Hutchinson
Google Research, Australia
benhutch@google.com
Abstract
Indigenous languages are historically under-
served by Natural Language Processing (NLP)
technologies, but this is changing for some lan-
guages with the recent scaling of large mul-
tilingual models and an increased focus by
the NLP community on endangered languages.
This position paper explores ethical consider-
ations in building NLP technologies for In-
digenous languages, based on the premise that
such projects should primarily serve Indige-
nous communities. We report on interviews
with 17 researchers working in or with Aborig-
inal and/or Torres Strait Islander communities
on language technology projects in Australia.
Drawing on insights from the interviews, we
recommend practices for NLP researchers to in-
crease attention to the process of engagements
with Indigenous communities, rather than fo-
cusing only on decontextualised artefacts.
1
Introduction
In this position paper, we discuss how to ethically
build Natural Language Processing (NLP) tech-
nologies for Indigenous languages, which have
historically been poorly served by NLP. This is
a timely question, as we are in the UNESCO Inter-
national Decade of Indigenous Languages (2022–
2032), and there has been a recent trend towards
more NLP technologies processing Indigenous lan-
guages. One thread of recent projects has been mo-
tivated by scaling large multilingual models to in-
clude Indigenous languages, including M¯aori, Zulu,
Igbo, Southern Quechua, Hawaiian, Querétaro
Otomi, Navajo, and more (e.g., Pratap et al., 2023;
Imani et al., 2023; Kudugunta et al., 2023). An-
other thread of recent projects is driven by threats
of language extinction, for example, the six Work-
shops on the Use of Computational Methods in
the Study of Endangered Languages (‘ComputEL’)
held since 2014, and the ACL 2022 Theme Track:
∗Work done while at Google Research.
“Language Diversity: From Low-Resource to En-
dangered Languages”. Both threads of research
are typically based on assumptions that language
technologies should be accessible to everyone in
their first language(s), and that the availability of
those language technologies will promote language
use and preservation (Bird, 2020).
We start with the premise that NLP for Indige-
nous languages should primarily serve Indigenous
communities. If this is indeed the goal of the NLP
community, then we need NLP to be accountable
to and benefit Indigenous communities (Schwartz,
2022), and to prioritise communities’ values and ex-
periences with respect to NLP projects. Prioritising
these values and experiences specifically includes
considering the context of Indigenous communities
within colonised societies (Schwartz, 2022; Bird,
2020) and the expressed opinions of those com-
munities around data governance (e.g., Liu et al.,
2022; Mager et al., 2023). The overarching ques-
tion for this paper, then, is: how can NLP better
serve Indigenous communities?
To consider this question, we first review the
developing discourse around decolonisation of lan-
guage technology, along with principles for Indige-
nous data governance. We then report on interviews
with researchers working in or with Aboriginal
and/or Torres Strait Islander communities on lan-
guage technology projects in Australia, the coun-
try in which two of the authors live. Drawing on
insights from the interviews, we recommend prac-
tices for NLP researchers working with Indigenous
languages. Overall, we encourage NLP researchers
to increase attention to the process of engagements
with Indigenous communities, rather than focusing
only on decontextualised artefacts.
2
Background
Languages can be marginalised in different ways.
The NLP research community describes a language
as ‘low-resource’ when there is insufficient data
arXiv:2402.02639v2  [cs.CL]  6 Feb 2024

--- Page 2 ---

in that language to train and evaluate statistical
and machine learning models (Liu et al., 2022).
The poverty-conscious framing of the term ‘low-
resource’ has been criticised by Bird (2022), how-
ever, for being colonial and Eurocentric. We prefer
the term under-served in this paper (echoing, for
example, Bender and Friedman, 2018; Kaffee et al.,
2018; Armstrong et al., 2022; Forbes et al., 2022),
as we recognise that a language may be fully consti-
tuted in its own ways, while it may not be serviced
by dominant NLP tools or techniques. Guided by
scholars of marginalisation processes (e.g., Bagga-
Gupta, 2017), we seek to pivot the discussion from
‘low-resource’ languages to how technology com-
munities are under-serving language communities.
Languages spoken by few people may addition-
ally be defined as endangered—at risk of disap-
pearing due to a lack of speakers (Bromham et al.,
2022). However, having few living speakers does
not necessarily mean a language is ‘low-resource’
(e.g., Latin has enough data to support Google
Translate).
The
majority
of
Indigenous
languages—
languages spoken in a particular region by
Indigenous peoples—are forecast to disappear
by the end of this century (Bromham et al.,
2022). In practice, most Indigenous languages
are endangered due not to any inherent linguistic
inferiority, but rather due to the global economic,
ideological, military, and nationalistic practices
that are constitutive of colonialism.
2.1
Decolonisation and Language Technology
Decolonial approaches to addressing marginalisa-
tion in technology are primarily motivated by so-
cial justice and self-determination (Smith, 1999),
not only data efficiency (Bird, 2022). These ap-
proaches encourage researchers to embrace per-
spectives from and at the margins in order to
surface and critique the persistence of colonial
relationships in present-day society (Maldonado-
Torres, 2007; Quijano, 2007; Escobar, 2018). Ac-
cording to the literature on decolonisation, there are
three broad strategies to enact decolonial agendas
in language technology work.
Firstly, decolonial agendas require that we con-
sider whose interests are served by NLP. Language
technologies are laden with cultural perspectives
and assumptions (Awori et al., 2016), and NLP has
a “habit of ... technological colonisation” along
with making assumptions about goals and meth-
ods (Bird, 2020). Research on languages of In-
digenous communities must be conducted on their
terms (Dourish et al., 2020) and research outputs
must be primarily relevant to those communities,
not only to research communities (Alvarado Garcia
et al., 2021).
Secondly, decolonial agendas encourage us to
question the universality of values (Mignolo, 2011;
Grosfoguel, 2007), in particular, the primacy of
Western values over others. This includes question-
ing methods and utility functions of NLP projects.
Assuming all communities want the same lan-
guage technologies disempowers local communi-
ties (Bird, 2020). Instead, we must critique the uni-
versalising logic of our methods, along with tech-
nologies (Dourish et al., 2020; Irani et al., 2010).
In addition, imagining alternative futures for NLP
and under-served languages means defending other
perspectives and worldviews (Escobar, 2018).
Thirdly, decolonial agendas direct us to interro-
gate power dynamics embedded in NLP projects.
Approaches from the Global North are often dis-
connected from the life experiences of those in the
Global South (Alvarado Garcia et al., 2021). In
addition, power asymmetries exist between users
and platforms (Couldry and Mejias, 2018), and be-
tween different regions of the world (Kwet, 2019).
2.2
Principles for Indigenous Data
Governance
We believe it is critical to consider Indigenous per-
spectives on language data management. Examples
of such perspectives are reflected in the CARE prin-
ciples of the Global Indigenous Data Alliance (Car-
roll et al., 2020), the Maiam nayri Wingara (2018)
Indigenous Data Sovereignty Principles, and the
Te Mana Raraunga (2016) principles of M¯aori data
sovereignty. These principles grapple with an on-
going tension for Indigenous communities when
engaging with language technologists—between
maintaining sovereignty over their language data
and engaging with technological developments that
could benefit language revitalisation efforts. Al-
though each set of principles is distinct, a thematic
analysis by the authors revealed some common
areas of concern.
• Respect: Acknowledge and support the rights
of people and communities to hold and ex-
press different values, norms and aspirations
regarding data and technology. This requires
listening, and understanding culture.

--- Page 3 ---

• Relationships: Act cooperatively. Build posi-
tive, long-term relationships.
• Shared control: Support data governance and
control. Support the exercise of data guardian-
ship using traditional protocols.
• Benefits: Understand disparate benefits and en-
sure equitable distribution of benefits. Provide
evidence of individual and collective benefits.
3
Insights from Interviews
Building on the previous section, our focus here
narrows to Australia as a case study. Australian
Aboriginal and Torres Strait Islander languages are
marginalised in multiple ways. There is a scarcity
of language technologies, which reflects a much
broader technological under-serving of these com-
munities. Indeed, many communities struggle to
get reliable and affordable access to the internet
(Featherstone et al., 2023). Prior to colonisation,
there were more than 250 local languages spoken in
Australia, though today just over 120 languages are
in use or being revitalised and more than 90% of
those are considered endangered (Australian Gov-
ernment et al., 2020). However, it is not for a lack
of internet, data, or NLP technologies that many
local languages are endangered or extinct. We can-
not ignore the impacts of colonialism—in many
cases, language loss is the byproduct of oppression.
Local languages were often the target of colonial
oppression as those languages sustained identities
and connection to Indigenous lands and cultures
(Bird, 2020). For example, up until the mid-20th
century, the Commonwealth Government of Aus-
tralia forced Aboriginal and Torres Strait Islander
people to learn English and forbade them from
speaking their own languages in government and
mission schools (Rademaker, 2018).
To delve deeper into this context, we formulated
two research questions guiding a series of inter-
views with researchers who work in or with Abo-
riginal and/or Torres Strait Islander communities on
speech and language technology projects. Firstly,
how should language technologists work with lo-
cal communities to develop speech and language
technologies? Secondly, what is the role of speech
and language technologies in sustaining language
use by local communities?
We conducted semi-structured, 60-minute in-
terviews with 17 researchers from academia and
community-based organisations between October
2022 and June 2023 (see Appendix). Our approach
to recruitment combined purposeful and snowball
sampling (Palinkas et al., 2015). First, we con-
tacted researchers known to the authors who had
published on language technology development
projects conducted in or with Aboriginal and/or
Torres Strait Islander communities in Australia. We
asked our initial interviewees to recommend oth-
ers for us to contact in a second round, including
members of Aboriginal and Torres Strait Islander
communities researching their own languages. We
contacted all potential interviewees via email, and
those who accepted our request completed a con-
sent form. The vast majority of the interviews
were conducted via video conference, though a few
were conducted in person. All interviews were tran-
scribed and shared with interviewees following the
interview for review.
Each interview followed the same general for-
mat, though we tailored interview guides to each
interviewee and their published work. After asking
background questions about the project(s) relevant
to the study and the interviewee, we asked each
interviewee a series of descriptive questions about
how they approach working with communities in
language technology development projects. Finally,
we asked a series of more open-ended questions
prompting interviewees to reflect on the present
and future of NLP for Indigenous languages in
Australia—for example, exploring projects and ac-
tivities to focus on and practices to avoid.
Insights from the interviews were derived using
thematic analysis, initially by hand and in a second
round using coding software. The descriptions and
reflections of our interviewees, detailed in the fol-
lowing two sections, shed light on strategies and
challenges to enact decolonial agendas and Indige-
nous data governance principles at the project level.
We include anonymised quotes from our intervie-
wees throughout the sections.
3.1
How to work with Aboriginal and Torres
Strait Islander communities
We first asked interviewees how they decide what
to work on and who to work with. All intervie-
wees strongly emphasised that speech and language
technology projects “must start with a community
need”, and that recognising such needs requires
long-term relationships. The need for translation,
for example, often arises where communities or
researchers observe something happening across

--- Page 4 ---

cultures over time. Many interviewees also argued
that projects shouldn’t start with technology, or
solutions. Instead, interviewees encouraged other
technologists to demo existing technology and fa-
cilitate experimentation with the tools by commu-
nities for their languages.
We also asked researchers how they manage re-
lationships with the people they work with. All
interviewees emphasised that researchers must clar-
ify to partner communities the mutual benefits of a
project at the outset, with some interviewees explic-
itly mentioning the negotiation of data access rights.
Several interviewees noted that community-based
work requires researchers to question universal as-
sumptions about the social or cultural factors rele-
vant to technology, and that personal relationships
are key to managing those complexities.
Finally, we asked about finishing projects. Most
interviewees noted that, though it is important for
projects to have an end date, personal relationships
between researchers and communities persist. Sev-
eral interviewees encouraged translating documen-
tation into an accessible form that communities can
continue to access (rather than locking up data in
bespoke, single purpose tools). Those same inter-
viewees argued that repositories and archives sup-
port the sustainability of project outcomes: “Apps
and websites are disposable ... store the data in
an archival format that is going to persist.”
3.2
What to work on with Aboriginal and
Torres Strait Islander communities
Most interviewees stated that the primary motiva-
tion of the communities they work with for build-
ing speech and technologies is the transmission of
culture via language: “Tap into the intrinsic mo-
tivation of transmitting life and knowledge down
the generations.” Several interviewees encouraged
a “design for one, then scale” approach, where
researchers collaborate with one community, then
scale a “digital shell”—a technological template
tailored for one community, yet adaptable enough
to be customised by others—streamlining early de-
velopment stages for each new engagement. Others
urged technologists to consider the benefits of the
production process to communities, to facilitate
capacity building in technology development, not
only focusing on project outputs like datasets or
publications.
In terms of application domains, several inter-
viewees advocated for improving accessibility to
archival materials using front-end tools for meta-
data tagging and information retrieval, especially
for audio. Others emphasised the importance of
vehicular languages like Aboriginal English, Aus-
tralian Kriol, and Torres Strait Creole. Intervie-
wees noted that many communities use vehicular
languages to participate in the national economy
and access education and health systems. Finally,
some interviewees encouraged multi-modal work
to support signed Aboriginal languages, alongside
text and audio.
4
Recommendations and Conclusion
To conclude, we propose a set of practices build-
ing on the insights from our interviews, along with
the decolonial agendas and Indigenous data gov-
ernance principles outlined earlier. We recognise
that Indigenous communities and their languages
vary considerably across the world, and the needs
of communities in one region might not necessarily
reflect those of other regions. However, many In-
digenous communities have common experiences
with respect to colonialism and its links to research
practices (Smith, 1999). Therefore, while our in-
terview study was specific to Australia, we put
forward these practices for NLP researchers to test
and build upon in other regions.
The practices grapple with a tension for NLP
researchers working with Indigenous languages—
between producing work that is relevant to local
partner communities and the demands of research
communities for projects that scale across many
languages. We intend to contribute to the discourse
about decolonisation of language technology, not
by resolving this tension, but by recommending a
cyclical process of engagement to assist researchers
to navigate it (Figure 1). As Escobar (2018) sug-
gests for design, we argue that the NLP community
can engage with marginalisation and dispossession
through a greater focus on the process of engage-
ments rather than on artefacts alone.
An ethical process starts by seeking out commu-
nity needs. This means asking communities we
wish to partner with about their goals for their lan-
guages, and ensuring our efforts are aligned with
those goals (Liu et al., 2022). This approach may
lead us to focus more on supporting the transmis-
sion of cultural knowledge across generations, not
only expanding access to products and services.
Focusing solely on data collection by communi-
ties to develop products and services risks disen-

--- Page 5 ---

franchising communities. Instead, one approach
might be to demo existing technology at commu-
nity events (e.g., the PULiiMA Indigenous Lan-
guages and Technology Conference) and asking
how communities can appropriate it for their needs.
Engaging with community representative bodies
can help researchers establish long-term relation-
ships with community members. While personal
relationships between researchers and community
members are crucial, engaging through representa-
tive bodies offers a distinct advantage in balancing
power dynamics. Additionally, these bodies al-
ready have established relationships within their
communities, allowing researchers to build trust
and credibility more rapidly.
Relatedly, we must consider how to negotiate
control over project resources and ongoing rela-
tionships. At the start of community-engaged lan-
guage technology projects, this involves several
steps. Firstly, researchers should schedule time
to interrogate power dynamics (Blodgett et al.,
2020), which involves recognising the often distinct
decision-making processes and communication ap-
proaches of researchers and Indigenous community
participants, and developing mutually agreed pro-
tocols for the project (Cooper et al., 2022). Sec-
ondly, it’s important to consider how to share power
with community partners by recognising Indige-
nous (co-)ownership of outcomes of data collec-
tion efforts (e.g., community ownership of datasets
or other intellectual property, and joint publications
(Janke, 2021)).
Where data collection is a component of a
project with an Indigenous community, we must
consider how the process of engagement might be
an opportunity for community benefit. In practice,
this may involve designing experiences for commu-
nity members to learn about language technology
as part of the process of generating or collecting
data, and creating outputs from data collection that
are accessible by community members, not only
usable by language technologists.
In addition, it is critical to store and maintain
data produced from the project in a format that
community partners can access beyond the project
(e.g., archives or repositories). Where researchers
also intend to scale projects across languages, we
recommend starting small—focusing on one to two
communities, then scaling digital shells to other
contexts (see, for example, Richards et al., 2019;
Foley et al., 2018).
Figure 1: Recommended process for engagement.
Finally, we also urge the NLP research envi-
ronment to pay more attention to the process of
engaging with Indigenous communities, rather
than focusing on de-contextualised model accuracy
benchmarks as proxies for utility to communities
(Hutchinson et al., 2022). This means including
the process of engagement as a core reviewing cri-
terion when processing Indigenous languages, and
fostering forums where Indigenous voices can ar-
ticulate their needs to the NLP community. While
NLP research processes can, like NLP artefacts, be
a source of harm to communities (Ashurst et al.,
2022), such processes can be generative for com-
munities when guided by their methodologies and
interests (see e.g., ‘yarning’ as a research method:
Rodríguez Louro and Collard, 2021). Let the pro-
cess of engagement with Indigenous communities
and their voices be the pillars of our research.
5
Limitations
Our paper has several limitations. Firstly, our sam-
pling approach may introduce selection bias, as the
initial set of researchers we recruited influenced the
final group of interviewees. Our approach favoured
researchers in our existing networks, which could
overlook the perspectives of researchers and com-
munity members outside those networks. Secondly,
we conducted interviews with researchers working
in or with Aboriginal and/or Torres Strait Islander
communities; however, the majority of our inter-
viewees were non-Indigenous, and we did not re-
cruit any interviewees from Torres Strait Islander
communities. While engaging with researchers
aligns with our goal of understanding strategies
and challenges for NLP researchers to enact de-
colonial agendas and Indigenous data governance
principles, we have limited insight into the per-
spectives of Aboriginal and Torres Strait Islander
communities. Thirdly, our positions of privilege as

--- Page 6 ---

researchers affect our interpretation and presenta-
tion of themes from the interviews. While we strive
for understanding and sensitivity, our perspectives
could overlook lived experiences that we might
not recognise. This emphasises the importance of
considered engagement with Indigenous voices to
ensure appropriate representation in NLP research
about Indigenous languages.
6
Acknowledgements
We would like to thank our interviewees, whose
insights and experiences informed this paper, and
extend that thanks to the communities collaborating
with our interviewees. Additionally, our thanks go
to the organisers and participants of the 2023 PULi-
iMA Indigenous Languages and Technology Con-
ference, for enriching discussions that improved
the paper, and to the anonymous reviewers for their
suggestions and feedback.
References
Adriana Alvarado Garcia, Juan F Maestre, Manuhuia
Barcham,
Marilyn
Iriarte,
Marisol
Wong-
Villacres, Oscar A Lemus, Palak Dudani, Pedro
Reynolds-Cuéllar,
Ruotong Wang,
and Teresa
Cerratto Pargman. 2021. Decolonial pathways: Our
manifesto for a decolonizing agenda in HCI research
and design.
In Extended Abstracts of the 2021
CHI Conference on Human Factors in Computing
Systems, CHI EA ’21, pages 1–9, New York, NY,
USA. Association for Computing Machinery.
Ruth-Ann Armstrong, John Hewitt, and Christopher
Manning. 2022. JamPatoisNLI: A jamaican patois
natural language inference dataset. In Findings of the
Association for Computational Linguistics: EMNLP
2022, pages 5307–5320, Abu Dhabi, United Arab
Emirates. Association for Computational Linguistics.
Carolyn Ashurst, Solon Barocas, Rosie Campbell, and
Deborah Raji. 2022. Disentangling the components
of ethical research in machine learning. In Proceed-
ings of the 2022 ACM Conference on Fairness, Ac-
countability, and Transparency, FAccT ’22, page
2057–2068, New York, NY, USA. Association for
Computing Machinery.
Australian Government, Australian Institute of Aborigi-
nal and Torres Strait Islander Studies, and Australian
National University. 2020. National Indigenous Lan-
guages Report. Technical report, Commonwealth of
Australia.
Kagonya Awori, Nicola J Bidwell, Tigist Sherwaga Hus-
san, Satinder Gill, and Silvia Lindtner. 2016. De-
colonising technology design. In Proceedings of the
First African Conference on Human Computer Inter-
action, AfriCHI’16, pages 226–228, New York, NY,
USA. Association for Computing Machinery.
Sangeeta Bagga-Gupta. 2017.
Marginalization Pro-
cesses Across Different Settings: Going Beyond the
Mainstream. Cambridge Scholars Publishing.
Emily M Bender and Batya Friedman. 2018.
Data
statements for natural language processing: Toward
mitigating system bias and enabling better science.
Transactions of the Association for Computational
Linguistics, 6:587–604.
Steven Bird. 2020. Decolonising speech and language
technology. In Proceedings of the 28th International
Conference on Computational Linguistics, pages
3504–3519, Barcelona, Spain (Online). International
Committee on Computational Linguistics.
Steven Bird. 2022. Local Languages, Third Spaces,
and other High-Resource Scenarios. In Proceedings
of the 60th Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers),
pages 7817–7829, Dublin, Ireland. Association for
Computational Linguistics.
Su Lin Blodgett, Solon Barocas, Hal Daumé, III, and
Hanna Wallach. 2020.
Language (technology) is
power: A critical survey of “bias” in NLP. In Pro-
ceedings of the 58th Annual Meeting of the Asso-
ciation for Computational Linguistics, pages 5454–
5476, Online. Association for Computational Lin-
guistics.
Lindell Bromham, Russell Dinnage, Hedvig Skirgård,
Andrew Ritchie, Marcel Cardillo, Felicity Meakins,
Simon Greenhill, and Xia Hua. 2022. Global pre-
dictors of language endangerment and the future of
linguistic diversity. Nature Ecology & Evolution,
6(2):163–173.
Stephanie Carroll, Ibrahim Garba, Oscar Figueroa-
Rodríguez,
Jarita Holbrook,
Raymond Lovett,
Simeon Materechera, Mark Parsons, Kay Raseroka,
Desi Rodriguez-Lonebear, Robyn Rowe, Rodrigo
Sara, Jennifer Walker, Jane Anderson, and Maui Hud-
son. 2020. The CARE principles for indigenous data
governance. Data Science Journal, 19:1–12.
Ned Cooper, Tiffanie Horne, Gillian R Hayes, Courtney
Heldreth, Michal Lahav, Jess Holbrook, and Lauren
Wilcox. 2022. A Systematic Review and Thematic
Analysis of Community-Collaborative Approaches
to Computing Research. In CHI Conference on Hu-
man Factors in Computing Systems, pages 1–18, New
Orleans, LA, USA. ACM.
Nick Couldry and Ulises A Mejias. 2018. Data colo-
nialism: Rethinking big data’s relation to the contem-
porary subject. Television & New Media, 20(4).
Paul Dourish, Christopher Lawrence, Tuck Wah Leong,
and Greg Wadley. 2020. On being iterated: The affec-
tive demands of design participation. In Proceedings
of the 2020 CHI Conference on Human Factors in
Computing Systems, CHI ’20, pages 1–11, New York,
NY, USA. Association for Computing Machinery.

--- Page 7 ---

Arturo Escobar. 2018. Designs for the Pluriverse: Rad-
ical Interdependence, Autonomy, and the Making of
Worlds. New Ecologies for the Twenty-First Century.
Duke University Press, Durham.
Daniel Featherstone, Lyndon Ormond-Parker, Lauren
Ganley, Julian Thomas, Sharon Parkinson, Kieran
Hegarty, Jenny Kennedy, and Indigo Holcombe-
James. 2023. Mapping the digital gap: 2023 out-
comes report. Technical report, ARC Centre of Ex-
cellence for Automated Decision-Making and Soci-
ety.
Ben Foley, Joshua T Arnold, Rolando Coto-Solano,
Gautier Durantin, T Mark Ellison, Daan van Esch,
Scott Heath, Frantisek Kratochvil, Zara Maxwell-
Smith, David Nash, et al. 2018. Building speech
recognition systems for language documentation:
The CoEDL endangered language pipeline and in-
ference system (ELPIS). In 6th Workshop on Spoken
Language Technologies for Under-Resourced Lan-
guages, pages 205–209, Gurugram, India. ISCA.
Clarissa Forbes, Farhan Samir, Bruce Oliver, Chang-
bing Yang, Edith Coates, Garrett Nicolai, and Miikka
Silfverberg. 2022. Dim wihl gat tun: The case for
linguistic expertise in NLP for Under-Documented
languages. In Findings of the Association for Com-
putational Linguistics: ACL 2022, pages 2116–2130,
Dublin, Ireland. Association for Computational Lin-
guistics.
Ramón Grosfoguel. 2007. The epistemic decolonial
turn: Beyond political-economy paradigms. Cultural
Studies, 21(2-3):211–223.
Ben Hutchinson, Negar Rostamzadeh, Christina Greer,
Katherine Heller, and Vinodkumar Prabhakaran.
2022. Evaluation Gaps in Machine Learning Practice.
In 2022 ACM Conference on Fairness, Accountability,
and Transparency, pages 1859–1876, Seoul Republic
of Korea. Association for Computing Machinery.
Ayyoob Imani, Peiqin Lin, Amir Hossein Kargaran,
Silvia Severini, Masoud Jalili Sabet, Nora Kass-
ner, Chunlan Ma, Helmut Schmid, André Martins,
François Yvon, and Hinrich Schütze. 2023. Glot500:
Scaling multilingual corpora and language models to
500 languages. In Proceedings of the 61st Annual
Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 1082–1117,
Toronto, Canada. Association for Computational Lin-
guistics.
Lilly Irani, Janet Vertesi, Paul Dourish, Kavita Philip,
and Rebecca E Grinter. 2010. Postcolonial comput-
ing: a lens on design and development. In Proceed-
ings of the SIGCHI Conference on Human Factors
in Computing Systems, CHI ’10, pages 1311–1320,
New York, NY, USA. Association for Computing
Machinery.
Terri Janke. 2021. True Tracks: Indigenous cultural
and intellectual property principles for putting self-
determination into practice. University of New South
Wales Press.
Lucie-Aimée Kaffee, Hady Elsahar, Pavlos Vougiouklis,
Christophe Gravier, Frédérique Laforest, Jonathon
Hare, and Elena Simperl. 2018. Learning to gener-
ate Wikipedia summaries for underserved languages
from Wikidata. In Proceedings of the 2018 Confer-
ence of the North American Chapter of the Associ-
ation for Computational Linguistics: Human Lan-
guage Technologies, Volume 2 (Short Papers), pages
640–645, New Orleans, Louisiana. Association for
Computational Linguistics.
Sneha Kudugunta, Isaac Caswell, Biao Zhang, Xavier
Garcia, Christopher A Choquette-Choo, Katherine
Lee, Derrick Xin, Aditya Kusupati, Romi Stella,
Ankur Bapna, and Orhan Firat. 2023. MADLAD-
400: A multilingual and Document-Level large au-
dited dataset. arXiv preprint arXiv:2309.04662.
Michael Kwet. 2019. Digital colonialism: US empire
and the new imperialism in the global south. Race &
Class, 60(4):3–26.
Zoey Liu, Crystal Richardson, Richard Hatcher, and
Emily Prud’hommeaux. 2022. Not always about
you: Prioritizing community needs when developing
endangered language technology. In Proceedings
of the 60th Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers),
pages 3933–3944, Dublin, Ireland. Association for
Computational Linguistics.
Manuel Mager, Elisabeth Mager, Katharina Kann, and
Ngoc Thang Vu. 2023. Ethical considerations for
machine translation of indigenous languages: Giv-
ing a voice to the speakers. In Proceedings of the
61st Annual Meeting of the Association for Compu-
tational Linguistics (Volume 1: Long Papers), pages
4871–4897, Toronto, Canada. Association for Com-
putational Linguistics.
Maiam
nayri
Wingara.
2018.
Indigenous
data
sovereignty
communique.
https:
//www.maiamnayriwingara.org/
mnw-principles. Accessed: 2023-6-16.
Nelson Maldonado-Torres. 2007. On the Coloniality of
Being. Cultural Studies, 21(2-3):240–270.
Walter D Mignolo. 2011. Global Futures, Decolonial
Options. Duke University Press.
Lawrence A Palinkas, Sarah M Horwitz, Carla A Green,
Jennifer P Wisdom, Naihua Duan, and Kimberly
Hoagwood. 2015. Purposeful sampling for quali-
tative data collection and analysis in mixed method
implementation research. Adm. Policy Ment. Health,
42(5):533–544.
Vineel Pratap, Andros Tjandra, Bowen Shi, Paden
Tomasello, Arun Babu, Sayani Kundu, Ali Elkahky,
Zhaoheng Ni, Apoorv Vyas, Maryam Fazel-Zarandi,
Alexei Baevski, Yossi Adi, Xiaohui Zhang, Wei-Ning
Hsu, Alexis Conneau, and Michael Auli. 2023. Scal-
ing speech technology to 1,000+ languages. arXiv
preprint arXiv:2305.13516.

--- Page 8 ---

Aníbal Quijano. 2007.
Coloniality and Moder-
nity/Rationality. Cultural Studies, 21(2-3):168–178.
Laura Rademaker. 2018. Found in Translation: Many
Meanings on a North Australian Mission. University
of Hawaii Press, Honolulu, HI, USA.
Mark Richards, Caroline Jones, Francesca Merlan, and
Jennifer MacRitchie. 2019. Revitalisation of Man-
garrayi: Supporting community use of archival audio
exemplars for creation of language learning resources.
Language Documentation & Conservation, 13:253–
280.
Celeste Rodríguez Louro and Glenys Collard. 2021.
Working together: Sociolinguistic research in urban
Aboriginal Australia. Journal of Sociolinguistics,
25(5):785–807.
Lane Schwartz. 2022. Primum Non Nocere: Before
working with Indigenous data, the ACL must con-
front ongoing colonialism. In Proceedings of the
60th Annual Meeting of the Association for Compu-
tational Linguistics (Volume 2: Short Papers), pages
724–731, Dublin, Ireland. Association for Computa-
tional Linguistics.
Linda Tuhiwai Smith. 1999. Decolonizing Methodolo-
gies: Research and Indigenous Peoples, 2nd edition.
Zed Books, London, UK.
Te
Mana
Raraunga.
2016.
Our
charter.
https://www.temanararaunga.maori.
nz/tutohinga. Accessed: 2023-6-16.
A
Summary of interviewees
Indigenous status
Count
Non-Indigenous
12
Aboriginal
5
Table 1: Indigenous status of interviewees.
Field of Expertise
Count
Linguistics
7
Computing
7
Community-based research
3
Table 2: Primary field of expertise of interviewees.
Australian State or Territory
Count
Queensland
4
New South Wales
4
Victoria
4
Northern Territory
3
Western Australia
2
Table 3: Location of interviewees.

```
