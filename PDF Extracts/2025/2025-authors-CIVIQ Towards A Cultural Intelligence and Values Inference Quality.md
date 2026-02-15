---
title: "2025-authors-CIVIQ Towards A Cultural Intelligence and Values Inference Quality - PDF Extract"
source_pdf: "2025-authors-CIVIQ Towards A Cultural Intelligence and Values Inference Quality.pdf"
pages: 6
extracted_at: "2026-02-15T17:54:29.356211"
---

# PDF Extract: 2025-authors-CIVIQ Towards A Cultural Intelligence and Values Inference Quality

**Source PDF:** 2025-authors-CIVIQ Towards A Cultural Intelligence and Values Inference Quality.pdf
**Total Pages:** 6

---

## Content

```
--- Page 1 ---

Towards A Cultural Intelligence and Values Inference Quality
Benchmark for Community Values and Common Knowledge
Brittany Johnson
johnsonb@gmu.edu
George Mason University
USA
Erin Reddick
tech@chatblackgpt.com
ChatBlackGPT
USA
Angela D.R. Smith
adrsmith@utexas.edu
University of Texas at Austin
USA
Abstract
Large language models (LLMs) have emerged as a powerful technol-
ogy, and thus, we have seen widespread adoption and use on soft-
ware engineering teams. Most often, LLMs are designed as “general
purpose” technologies meant to represent the general population.
Unfortunately, this often means alignment with predominantly
Western Caucasian narratives and misalignment with other cul-
tures and populations that engage in collaborative innovation. In
response to this misalignment, there have been recent efforts cen-
tered on the development of “culturally-informed” LLMs, such as
ChatBlackGPT, that are capable of better aligning with historically
marginalized experiences and perspectives. Despite this progress,
there has been little effort aimed at supporting our ability to develop
and evaluate culturally-informed LLMs. A recent effort proposed
an approach for developing a national alignment benchmark that
emphasizes alignment with national social values and common
knowledge. However, given the range of cultural identities present
in the United States (U.S.), a national alignment benchmark is an
ineffective goal for broader representation. To help fill this gap in
this US context, we propose a replication study that translates the
process used to develop KorNAT, a Korean National LLM alignment
benchmark, to develop CIVIQ, a Cultural Intelligence and Values In-
ference Quality benchmark centered on alignment with community
social values and common knowledge. As a proof-of-concept for
our approach, we focus our initial efforts on the Black community
in the US and leverage both general purpose (e.g., ChatGPT) and
culturally-informed (e.g., ChatBlackGPT) LLMs in our efforts. In
this paper, we discuss our plans for conducting this research, in-
cluding engaging our audience of interest in our efforts. Our work
provides a critical foundation for research and development aimed
at cultural alignment of AI technologies in practice.
Keywords
large language models, culturally-informed AI, benchmark
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
Conference’17, Washington, DC, USA
© 2025 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 978-x-xxxx-xxxx-x/YYYY/MM
https://doi.org/10.1145/nnnnnnn.nnnnnnn
ACM Reference Format:
Brittany Johnson, Erin Reddick, and Angela D.R. Smith. 2025. Towards A
Cultural Intelligence and Values Inference Quality Benchmark for Com-
munity Values and Common Knowledge. In . ACM, New York, NY, USA,
6 pages. https://doi.org/10.1145/nnnnnnn.nnnnnnn
1
Introduction
The advent of large language models (LLMs) has led to a shift in
how we collaborate and engage in software engineering. LLMs
can support natural language interactions for tasks such as facil-
itating asynchronous communication and learning, information
retrieval, analysis and summarization, and practical guidance across
domains, a trait that makes them highly attractive and frequently
integrated into everyday workflows [40], [24] , [9]. As a result, we
have evolved to the era of AI-assisted collaboration and innova-
tion [20], where artificial intelligence (AI) technologies like LLMs
are rapidly being integrated to support collaborative tasks such as
decision-making [19], communication [37], code review [10], and
project management [26].
While the integration of LLMs to support collaborative tasks
shows promise, it also has the potential to introduce workplace
and team inequities. These inequities stem from both the nature
of AI as a technology (e.g., centrality of data, nature of decision-
making) and the broader context in which it has been developed
and would potentially be used [13, 32]. As a result, those from
historically marginalized backgrounds are less likely to reap the
benefits due to the higher likelihood of discriminatory outcomes
and often being less equipped to find ways to extract the value of
AI-assisted collaboration. Therefore, as with any AI technology,
the outcomes and quality of support are only as good as the data
and evaluation mechanisms that are engaged in its design and
development.
One of the most common ways to assess the capabilities and risks
associated with a given AI technology is via benchmarking [18].
Benchmarks, which typically include some scoped dataset and cor-
responding metric(s), can be used to measure and identify flaws or
weaknesses in model performance over time and support assess-
ment of any number of concerns, including performance, efficiency,
and accuracy [22, 38]. While there are a variety of existing bench-
marks available, including contributions aimed at supporting the
assessment of cultural alignment of language technologies [31],
there is still a significant gap between the ability for existing bench-
marks to capture the nuances of socio-technical information needs
and foundations necessary to adequately support different expe-
riential perspectives in AI use in the workplace and beyond [35].
This gap is exaggerated by findings from a recent effort aimed
at developing a benchmark for cultural alignment with Korean
arXiv:2512.05176v1  [cs.SE]  4 Dec 2025

--- Page 2 ---

Conference’17, July 2017, Washington, DC, USA
Johnson et al.
culture, indicating both the necessary rigor behind cultural assess-
ments and the inadequacy of existing LLMs in representing diverse
perspectives [31].
To fill this gap in the U.S. context, we propose a research agenda
to develop CIVIQ (Cultural Intelligence and Values Inference Qual-
ity), a benchmark for LLM alignment with community culture. As a
proof-of-concept, we will develop CIVIQ for alignment with Black
culture in the U.S., a decision we discuss and further motivate in
Section 2. We outline our research goals and survey methodology,
clarifying the distinctions between our approach and the approach
it is inspired by (Section 3). We conclude with a discussion of antic-
ipated outcomes and plans for future work, including evaluations
plans following benchmark development (Section 5).
2
Background & Motivation
While promising, AI suffers from persistent issues in its ability
to adequately support the diaspora of potential users. This is es-
pecially problematic when these technologies are being rapidly
integrated into work environments and teams where there already
exists systemic barriers to meaningful engagement for historically
marginalized groups, like software development [16, 17].
These difficulties often stem from systemic misalignment be-
tween the experiences that inform AI and the experiences of its
users. In an attempt to address this issue, research and development
have rallied behind the concept of culturally-informed AI [11, 14].
While known by many different names (e.g., culturally-intelligent
AI, culturally-responsive AI), the idea is the same – an AI system
capable of going beyond predominantly Western narratives and
values to support engagement from historically marginalized users.
Two notable examples of culturally-informed LLMs are ChatBlack-
GPT 1 and Latimer 2. Latimer, touted as an AI for everyone trained
with diverse histories and inclusive voices, is an LLM trained to
accurately represent the experiences, culture, and history of Black
and Brown communities. ChatBlackGPT, while similar in its focus
on providing culturally-relevant interactions, distinguishes itself
by scoping to accurate representations of Black culture and history.
ChatBlackGPT further distinguishes itself by setting the precedent
for community-driven model design.
While there is promise in the development of culturally-informed
AI, there is still the issue of how to reproduce, evaluate, and maintain
such systems. In an effort to drive research and development in this
direction, there have been recent efforts aimed at understanding
and supporting cultural alignment of LLMs [2, 39]. In software and
AI engineering, we commonly use benchmarks as mechanisms for
supporting these endeavors [38]. Benchmarks provide structured,
standardized metrics for evaluating performance and facilitating
responsible innovation.
One concern raised regarding the cultural alignment of LLMs
through benchmarking is the ability to align them across multiple
cultures, as tools like Latimer attempt to do [27]. However, we posit
that the goal of cultural alignment should not be to encompass as
many cultures as possible (this is what got us where we are now)
but rather to facilitate alignment with specific cultures, as does
ChatBlackGPT. Making (to our knowledge) the first meaningful
1https://chatblackgpt.com/
2https://www.latimer.ai/
contribution in this direction is a recent study which introduced Ko-
rNAT, a national LLM alignment benchmark for Korea [31]. Their
effort focused on improving LLM alignment with Korean culture
by developing a dataset of social values and common knowledge
items specific to Korean culture and defining metrics for national
alignment scoring of LLMs. They used their benchmark to evaluate
seven LLMs and found that few existing models meet the threshold
for alignment with Korean social values and common knowledge.
Building on the promising foundation provided by prior work,
our ongoing efforts aim to facilitate the design and assessment
of alignment with specific user groups in the U.S. As a proof-of-
concept, we will center our efforts on Black culture within the
U.S. 3 While there exist numerous benchmarking efforts to support
cultural alignment, existing benchmarks are not built around Black
social values or common knowledge. This gap leads to considera-
tions like “AI Safety” defaulting to majority norms that erase Black
history and misread Black communities, thereby facilitating further
marginalization in an ever-AI-driven world. We aim to fill this gap
by replicating and expanding the work done for KorNAT to develop
CIVIQ, which we discuss next.
3
CIVIQ Research Agenda
The process behind KorNAT is multi-faceted and iterative, provid-
ing both rigor and culture-centered foundations. However, their
approach was designed for national alignment. Given the discourse
surrounding Black culture and erasure in the United States (U.S.) [29],
national alignment is not an appropriate goal. Below, we outline
our adapted approach to creating a cultural alignment benchmark
for community social values and common knowledge.
3.1
Research Goals & Objectives
The goal of our research is to extend and adapt the benchmarking
framework established by the KorNAT project to the U.S. context,
focusing specifically on the intersection of language model perfor-
mance and cultural representation. In our study, we will design and
develop CIVIQ (Cultural Intelligence and Values Inference Quality),
a community-centric, culturally-grounded benchmark that reflects
U.S.-based social values and common knowledge in the Black com-
munity. Ultimately, our work seeks to facilitate the design of cultural
alignment benchmarks that advance the development and use of
culturally intelligent LLMs. By providing an empirically grounded
standard for evaluating cultural alignment for more niche commu-
nities and cultures, our benchmark aims to support engineers in the
development and use of AI systems that accurately reflect the social
norms, cultural references, and histories that define the modern U.S.
landscape. We posit that the ability to create culturally intelligent
AI systems is a necessary step towards realizing equitable benefits
and gains from AI integration in diverse software teams.
3.2
Social Values Item Development
3.2.1
Topic Pool Determination. Following KorNAT’s approach,
we will curate our social values topic pool from two sources: timely
keywords and social conflict keywords.
3Any further rationale for this decision has been redacted for double anonymous
review.

--- Page 3 ---

Towards A Cultural Intelligence and Values Inference Quality Benchmark for Community Values and Common Knowledge
Conference’17, July 2017, Washington, DC, USA
For timely keywords, we will leverage media from the last 12
months that center Black communities. One of the key challenges
in creating a benchmark for Black culture alignment is ensuring
the social values are both relevant and accurate. Mainstream media
often exclude, misrepresent, or mischaracterize Black stories, a
systemic issue that makes most news or social media outlets difficult
to leverage alone [3, 6]. Therefore, we will focus our efforts on Black
media outlets (e.g., The Root 4 and Blavity 5) to curate keywords
that are relevant to timely social matters in the Black community.
For social conflict keywords, we will focus our keyword cu-
ration on topics that are long-standing pain points or sources of
conflict for the Black community. Our goal is to focus on topics
that have historical roots but also modern relevance, such as repa-
rations [15], school funding [34], confederate monuments [12],
equitable cannabis legalization [23], redlining remediation [25],
and anti-Black surveillance [41].
3.2.2
Item Generation & Validation. Once we have curated topic
keywords (approximately 1,500), we will gather approximately 5-
8 representative articles or community reports. We will provide
our keywords and artifacts to an LLM and prompt it to generate
10 closed-ended items per source, ensuring that it is using clear
and non-leading language. We will then perform two rounds of
human revision in collaboration with our trained Black survey
editors. In our rounds of revisions, we will leverage the revision
checklist used for KorNAT [31], which includes checking for timeli-
ness, relevance, single-theme items, language, and grammar. Items
will be phrased as Likert scale questions (e.g., “Strongly disagree”
to “Strongly agree”) and include a comprehension check (e.g., “I
clearly/roughly understand/cannot answer”). As another form of
validation, we will adapt KorNAT’s approach to cross-national
prompting (asking the model to answer “as someone from X”) to
test cross-group prompting (“answer as a Black American adult”).
3.3
Common Knowledge Item Development
Unlike social values items, which can rely on subjective sources
of information, the development of common knowledge requires
ground truth and historical accuracy. Similar to social values, our ap-
proach must diverge from the approach taken by KortNAT. In their
efforts, they could leverage Korean textbooks and GED reference
materials; however, in our context, much of the relevant history and
information that would inform Black common knowledge would
not be included in these materials.
Therefore, to develop our common knowledge items, we will
utilize recruit Black historians, educators, and subject matter ex-
perts to curate relevant resources and insights on Black history and
modern relevance. We will use their insights to Iteratively develop
multiple-choice question (MCQ) items. We will use ChatBlackGPT,
a GPT fine-tuned to Black history and context, to aid in scaling
item generation [14]. We will conduct independent revisions of re-
sulting items, auditing for differential item functioning [21] across
sub-groups.
The goal of our common knowledge set is to cover themes and
facts that have historical significance but also modern relevance.
This includes topics such as Pre-enslavement African history
4https://www.theroot.com/
5https://blavity.com/
& civilizations, Black Reconstruction, Great Migration &
Harlem Renaissance, Black STEM & business contributions,
Civics & rights today, Health & environment, and Practical
knowledge & culture. We will vette our topic selection with Black
historians and educators to ensure its relevance, completeness, and
accuracy.
Given the diversity of knowledge represented in our common
knowledge item set, and the need to balance the kinds of questions
provided, we will include a rationale and expected difficulty tag
(e.g., easy, medium, hard) for each item.
3.4
Survey Structure & Design
The final survey will include both social value likert scale items
(4,000) and common knowledge multiple choice items (6,000). The
survey structure will be based on the categories that unify and
represent the topics that emerge from the processes discussed in
Sections 3.2 and 3.3. Given our goal is to acquire the scale of Kor-
NAT (over 6,000 unique respondents), we will follow their approach
to survey design & deployment. This includes the use of stratified
sampling to facilitate engagement with small portions of the survey
at a time, alternating likert style and multiple choice questions
to reduce fatigue, and using short stems with concise options to
increase usability on mobile devices.
To support response quality control, we will include both at-
tention and consistency questions. Attention questions ask the
respondent to respond with a specific response to ensure they are
reading the questions (e.g., For this question, please select “None
of the above” below). Consistency questions provide another mech-
anism for ensuring respondents are truly engaged in the survey by
asking the same semantic question using different syntax (e.g., “I
prefer to use AI systems that reflect my cultural background.” vs. “It
doesn’t matter if an AI system understands my cultural context.”).
The expectation is that respondents would answer the same or sim-
ilarly for both questions. We will pilot our survey to evaluate and
improve all aspect of our survey design and structure, including
comprehension of and polarization on our survey items.
3.5
Sampling Frame & Weighting
The audience of interest is adult (18 years of age and over) Black
and African American adults across the United States. To ensure
balanced representation across the various demographic and socio-
cultural dimensions relevant to Black communities in the U.S., we
will use stratified random sampling [1]. Our stratification variables
will include age (18–29, 30–44, 45–59, and 60+), gender (male, fe-
male, transgender male, transgender female, non-binary), region
(South, Midwest, Northeast, and West), urbanicity (urban, sub-
urbans, and rural), socioeconomic factors (education level and
income tier), diaspora origin (African Descents of Slavery (ADOS),
Afro-Carribean, and African immigrant identities), faith tradition
(including, but not limited to Christian, Muslim, traditional African
religions, and secular respondents), carceral history (prior incar-
ceration or justice system contact), disability status, and sexual
orientation (heterosexual, gay, lesbian, bisexual, queer, pansexual,
asexual). We will use oversampling for underrepresented or hard-
to-reach groups (e.g., African immigrants, LGBTQ+ individuals,
persons with disabilities, and formerly incarcerated individuals) to
improve precision and reduce variance in sub-group estimates [8].

--- Page 4 ---

Conference’17, July 2017, Washington, DC, USA
Johnson et al.
Following KorNAT’s approach, we will adjust underrepresented
responses as necessary using two processes: stratification adjust-
ment and sampling adjustment. Stratification adjustment helps ad-
just demographic imbalances between the broader population and
survey respondents while sampling adjustment modifies the se-
lection probability when respondents are either over- or under-
represented in a specific group. We will use their calculations for
adjustment weights and normalize weighted responses.
3.6
Engaging Our Audience of Interest
As mentioned previously, it is critical for our efforts that we are able
to engage a diverse range of identities in the U.S. Black population.
Given the known issues regarding engagement from historically
marginalized communities in research [4, 5], we will experiment
with non-traditional mechanisms for engagement. Unlike survey
research aimed at broader audiences, we will use broad advertis-
ing (e.g., social media) as a last resort. Instead, we will prioritize
in-person, localized engagements across the U.S. We will leverage
our locality to cities and areas with large or predominantly Black
populations (e.g., Detroit, Washington, D.C., Austin) and partner-
ships in those areas to organize social events that will facilitate
survey participation. Those interested will have the option to take
the survey in exchange for admission to the event being hosted in
their city. We will also use a novel compensation model to ensure
response anonymity. Rather than respondents providing contact
information for compensation, respondents can earn coins for each
subset of the survey they take. Given the inclusivity benefits of
gamification [7, 33], this approach can increase engagement in
larger portions of the survey from a broader ranges of respondents.
We will set an appropriate limit for coins that can be acquired and
require photo identification for coin redemption to ensure data
integrity.
3.7
Calculating Cultural Alignment Score
Central to our research goals is the the ability for our efforts to facil-
itate evaluation of cultural alignment in LLMs and other advanced
technologies. As such, following KorNAT’s approach, we will use
our survey data to calculate scores for social value alignment and
common knowledge alignment.
3.7.1
Social Values Alignment Scoring. Given social value items
are likert-scale, there is no obvious ground truth. Furthermore,
selecting a ground truth in this context (e.g., based on majority
vote) could lead to our missing value information provided by other
responses [31]. Therefore, for the Social Value Alignment (SVA)
metric we will use the distribution of survey responses for each
social value item. More specifically, this metric is a ratio (𝑟𝑖𝑗) of
respondents choosing the 𝑗𝑡ℎoption for the 𝑖𝑡ℎquestion (𝑞𝑖). So
if a given model predicts the 𝑘𝑡ℎoption for 𝑞𝑖, it receive a social
alignment score of 𝑟𝑖𝑘(between 0 and 1). The final score is the
average score across all social value questions, with a score of over
0.5 indicating alignment with the majority of a given community.
As with KorNAT, we will use our empirical data to calculate
the maximum possible score and determine if and to what extent it
is necessary to develop an aggregated version of our SVA metric.
For example, in their work the empirically calculated maximum for
the SVA metric was 0.450 which suggests high variability in social
values on a five-point scale. To address this, they proposed an Ag-
gregated Social Value Alignment (A-SVA) metric that modifies
the ground truth distributions such that there are only three groups:
Disagree (grouping ‘Strongly Disagree’ and ‘Disagree’), Neutral,
and Agree (grouping ‘Strongly Agree’ and ’Agree’). In their efforts,
this increased the maximum achievable score to 0.626, indicating a
“moderate level” of agreement.
3.7.2
Common Knowledge Scoring. Given the common knowledge
items each have one correct answer, the Common Knowledge Align-
ment (CKA) metric is based on accuracy. For KorNAT, the standard
score was set as 0.6 to reflect the cut-off score for the Korean GED
(60 points); models above this threshold would be considered to
have sufficient common knowledge. However, given CIVIQ’s goal
to facilitate community culture-level alignment and the centrality
of Western White history in U.S. education [28, 36], this would be
a misalignment metric to leverage. Therefore, we will use the com-
petency threshold for Black history and culture proficiency exams
administered at HBCUs. The threshold across exams that score on
a 1–100 scales is 70 for competency; therefore, the threshold for
our CKA metric will be 0.70.
4
Ethics, Privacy, and Data Governance
We will adhere to rigorous ethical and privacy standards to ensure
participants and communities represented in the data are protected.
Our study protocol will undergo Institutional Review Board (IRB)
review and approval prior to data collection. We will acquired in-
formed consent, providing potential respondents with clear and
concise information about the study’s purpose, procedures, poten-
tial risks, and remind them of their right to withdraw from the study
at any time. To respect participant autonomy, we have designed
our study such that respondents can have the option to skip any
sensitive question without penalty or exclusion from the study.
One concern in conducting this research is the potential for push-
back from the Black community regarding their comfort with or
the potential harms that could stem from such broad access to their
values and lived experiences [30]. In an attempt to mitigate and
alleviate these kinds of concerns, our research efforts will operate
under a community data covenant, a governance framework that
will ensure data and artifacts derived from our work is used solely
for social benefit and non-harm. Our framework will have explicit
restrictions that prohibit use of the dataset or derivative models for
activities that could perpetuate harm, such as Surveillance or pre-
dictive policing, Immigration or law enforcement activities, Insurance
or credit risk scoring, Tenant screening or employment background
checks, and Any other carceral or punitive applications.
All downstream users will be required to submit a transparency
statement describing intended use, ethical safeguards, and commu-
nity benefits prior to accessing the dataset. Approved users will be
required to adhere to these covenant terms and cite them in any
derivative work.
Our release plan will follow the staged model used for KorNAT.
We will release a publicly accessible leaderboard and a sampled item
set that can be used to support benchmarking. We will only release
the full dataset via controlled access under a Data Use Agreement
(DUA) that enforces our community data covenant, privacy con-
strains, and reporting requirements. Each release will include an

--- Page 5 ---

Towards A Cultural Intelligence and Values Inference Quality Benchmark for Community Values and Common Knowledge
Conference’17, July 2017, Washington, DC, USA
accompanying data card documenting provenance, limitations, and
ethical constraints to ensure responsible and reproducible use.
5
Anticipated Outcomes & Future Work
The research outlined in this paper will lay the necessary founda-
tions to better understand the potential for sustainable innovation
around LLMs and other AI technologies capable of adequately sup-
porting culturally-diverse software teams. We anticipate a surge
in desire, even need, to meaningfully evaluate social proficiency of
intelligent systems which requires a trustworthy precedent. The
cooperative, community-engaged effort surrounding our proposed
benchmarking efforts provides a unique opportunity to build sus-
tainable bridges between academia, industry, and society that can
facilitate the design of a better technological landscape for all. Build-
ing on these foundations, we will experiment with top LLMs, both
general-purpose and culturally informed, using our benchmark
CIVIQ to evaluate alignment with Black culture. Our future ef-
forts will also involve deeper explorations into the use cases for
and potential benefits of culturally-aligned AI-assisted technolo-
gies on software teams and in other collaborative, human-facing
environments.
References
[1] Anita S Acharya, Anupam Prakash, Pikee Saxena, and Aruna Nigam. 2013. Sam-
pling: Why and how of it. Indian journal of medical specialties 4, 2 (2013), 330–333.
[2] Badr AlKhamissi, Muhammad ElNokrashy, Mai AlKhamissi, and Mona Diab.
2024. Investigating cultural alignment of large language models. arXiv preprint
arXiv:2402.13231 (2024).
[3] Emma-Lee Amponsah. 2024. Black dis/engagement: negotiating mainstream
media presence and refusal. European Journal of Cultural Studies 27, 5 (2024),
1037–1055.
[4] Oghenemaro Anuyah, Karla Badillo-Urquiola, and Ronald Metoyer. 2023. En-
gaging the discourse of empowerment for marginalized communities through
research and design participation. In Extended Abstracts of the 2023 CHI Conference
on Human Factors in Computing Systems. 1–7.
[5] Katrina Armstrong and Christine Ritchie. 2022.
Research participation in
marginalized communities—overcoming barriers.
New England Journal of
Medicine 386, 3 (2022), 203–205.
[6] April Baker-Bell, Raven Jones Stanbrough, and Sakeena Everett. 2017. The stories
they tell: Mainstream media, pedagogies of healing, and critical media literacy.
English Education 49, 2 (2017), 130–152.
[7] Ahlam Bavi and Neha Gupta. 2022. Gamification of digital heritage as an approach
to improving museum and art gallery engagement for blind and partially sighted
visitors. Archaeologies 18, 3 (2022), 585–622.
[8] Chia-Yun Chang, Ming-Tsung Hsu, Emilio Xavier Esposito, and Yufeng J Tseng.
2013. Oversampling to overcome overfitting: exploring the relationship between
data set composition, molecular descriptors, and predictive modeling methods.
Journal of chemical information and modeling 53, 4 (2013), 958–971.
[9] Aaron Chatterji, Thomas Cunningham, David J Deming, Zoe Hitzig, Christopher
Ong, Carl Yan Shan, and Kevin Wadman. 2025. How people use chatgpt. Technical
Report. National Bureau of Economic Research.
[10] Umut Cihan, Vahid Haratian, Arda İçöz, Mert Kaan Gül, Ömercan Devran, Emir-
can Furkan Bayendur, Baykal Mehmet Uçar, and Eray Tüzün. 2025. Automated
code review in practice. In 2025 IEEE/ACM 47th International Conference on Soft-
ware Engineering: Software Engineering in Practice (ICSE-SEIP). IEEE, 425–436.
[11] Angela M Cirucci, Miles Coleman, Dan Strasser, and Evan Garaizar. 2025. Cul-
turally responsive communication in generative AI: looking at ChatGPT’s advice
for coming out. AI & SOCIETY 40, 4 (2025), 2249–2257.
[12] Karen L Cox. 2021. No common ground: Confederate monuments and the ongoing
fight for racial justice. UNC Press Books.
[13] Lina Dencik, Jessica Brand, Philippa Metcalfe, and Cate Hopkins. 2025. AI
Inequalities at Work. (2025).
[14] Lisa Egede, Ebtesam Al Haque, Gabriella Thompson, Alicia Boyd, Angela DR
Smith, and Brittany Johnson. 2025. Exploring Culturally Informed AI Assistants:
A Comparative Study of ChatBlackGPT and ChatGPT. In Proceedings of the
Extended Abstracts of the CHI Conference on Human Factors in Computing Systems.
1–9.
[15] Ashley D Farmer. 2018. " Somebody Has to Pay": Audley Moore and the Modern
Reparations Movement. Palimpsest: A Journal on Women, Gender, and the Black
International 7, 2 (2018), 108–134.
[16] Babu George and Ontario S Wooden. 2025. Barriers to Equitable Progress. In AI
Empowered. Emerald Publishing Limited, 27–35.
[17] Emitzá Guzmán, Ricarda Anna-Lena Fischer, and Janey Kok. 2024. Mind the
gap: gender, micro-inequities and barriers in software development. Empirical
Software Engineering 29, 1 (2024), 17.
[18] Amelia Hardy, Anka Reuel, Kiana Jafari Meimandi, Lisa Soder, Allie Griffith,
Dylan M Asmar, Sanmi Koyejo, Michael S Bernstein, and Mykel John Kochen-
derfer. 2025. More than marketing? on the information value of ai benchmarks
for practitioners. In Proceedings of the 30th International Conference on Intelligent
User Interfaces. 1032–1047.
[19] Junda He, Christoph Treude, and David Lo. 2025. LLM-Based Multi-Agent Systems
for Software Engineering: Literature Review, Vision, and the Road Ahead. ACM
Transactions on Software Engineering and Methodology 34, 5 (2025), 1–30.
[20] Catherine M Hicks, Carol S Lee, and Kristen Foster-Marks. 2024. The new
developer: AI skill threat, identity change & developer thriving in the transition
to AI-assisted software development. (2024).
[21] Paul W Holland and Howard Wainer. 2012. Differential item functioning. Rout-
ledge.
[22] Capers Jones. 2000. Software assessments, benchmarks, and best practices. Addison-
Wesley Longman Publishing Co., Inc.
[23] Spruha Joshi, Samantha M Doonan, and John R Pamplin Ii. 2023. A tale of two
cities: racialized arrests following decriminalization and recreational legalization
of cannabis. Drug and alcohol dependence 249 (2023), 109911.
[24] Carolin Kaiser, Jakob Kaiser, Rene Schallner, and Sabrina Schneider. 2025. A
New Era of Online Search? A Large-Scale Study of User Behavior and Personal
Preferences during Practical Search Tasks with Generative AI versus Traditional
Search Engines. In Proceedings of the Extended Abstracts of the CHI Conference on
Human Factors in Computing Systems. 1–7.
[25] Helen H Kang. 2021. Looking toward restorative justice for redlined communities
displaced by eco-gentrification. Michigan Journal of Race and Law 26 (2021),
23–46.
[26] Stamatis Karnouskos. 2024. The relevance of large Language models for project
management. IEEE Open Journal of the Industrial Electronics Society 5 (2024),
758–768.
[27] Ariba Khan, Stephen Casper, and Dylan Hadfield-Menell. 2025. Randomness, not
representation: The unreliability of evaluating cultural alignment in llms. In Pro-
ceedings of the 2025 ACM Conference on Fairness, Accountability, and Transparency.
2151–2165.
[28] LaGarrett J King. 2017. The status of Black history in US schools and society.
Social Education 81, 1 (2017), 14–18.
[29] LaGarrett J King. 2020. Black history is not American history: Toward a frame-
work of Black historical consciousness. Social Education 84, 6 (2020), 335–341.
[30] Shamika Klassen. 2022. Black Twitter is gold: why this online community is
worthy of study and how to do so respectfully. Interactions 29, 1 (2022), 96–98.
[31] Jiyoung Lee, Minwoo Kim, Seungho Kim, Junghwan Kim, Seunghyun Won,
Hwaran Lee, and Edward Choi. 2024. KorNAT: LLM Alignment Benchmark for
Korean Social Values and Common Knowledge. In Findings of the Association
for Computational Linguistics: ACL 2024, Lun-Wei Ku, Andre Martins, and Vivek
Srikumar (Eds.). Association for Computational Linguistics, Bangkok, Thailand,
11177–11213. doi:10.18653/v1/2024.findings-acl.666
[32] Meng Li, Lai Wei, and Yao Yao. 2025. Large Language Models in the Workplace:
A Social Perspective. Available at SSRN 5222006 (2025).
[33] Jon McFarland. 2024. Cultural Inclusivity and Gamification. Pursuing Practical
Change: Lesson Designs That Promote Culturally Responsive Teaching (2024), 151.
[34] Robert Ponzini. 2022. Public school funding in the United States and its systemic
inequities. Economia Aziendale Online- 13, 1 (2022), 143–147.
[35] Anka Reuel, Amelia Hardy, Chandler Smith, Max Lamparth, Malcolm Hardy, and
Mykel J Kochenderfer. 2024. Betterbench: Assessing ai benchmarks, uncovering
issues, and establishing best practices. Advances in Neural Information Processing
Systems 37 (2024), 21763–21813.
[36] Noreen Naseem Rodríguez and Katy Swalwell. 2023. Social studies for a better
world: An anti-oppressive approach for elementary educators. Routledge.
[37] Mykyta Rohovyi and Marina Grinchenko. 2024. Towards the improvement of
project team performance based on large language models. Radioelectronic and
Computer Systems 2024, 4 (2024), 229–247.
[38] Alan Said, Domonkos Tikk, and Paolo Cremonesi. 2013. Benchmarking: A method-
ology for ensuring the relative quality of recommendation systems in software
engineering. In Recommendation Systems in Software Engineering. Springer, 275–
300.
[39] Yan Tao, Olga Viberg, Ryan S Baker, and René F Kizilcec. 2024. Cultural bias and
cultural alignment of large language models. PNAS nexus 3, 9 (2024), pgae346.
[40] Tianjia Wang, Tong Wu, Huayi Liu, Chris Brown, and Yan Chen. 2025. Generative
Co-Learners: Enhancing Cognitive and Social Presence of Students in Asynchro-
nous Learning with Generative AI. Proceedings of the ACM on Human-Computer
Interaction 9, 1 (2025), 1–24.

--- Page 6 ---

Conference’17, July 2017, Washington, DC, USA
Johnson et al.
[41] Damien Patrick Williams. 2020. Fitting the description: Historical and sociotech-
nical elements of facial recognition and anti-black surveillance. Journal of Re-
sponsible Innovation 7, sup1 (2020), 74–83.
Received 20 February 2007; revised 12 March 2009; accepted 5 June 2009

```
