---
title: "2025-Barrett-African Data Ethics A Discursive Framework for Black Decolonial AI - PDF Extract"
source_pdf: "2025-Barrett-African Data Ethics A Discursive Framework for Black Decolonial AI.pdf"
pages: 16
extracted_at: "2026-02-15T17:54:28.640124"
---

# PDF Extract: 2025-Barrett-African Data Ethics A Discursive Framework for Black Decolonial AI

**Source PDF:** 2025-Barrett-African Data Ethics A Discursive Framework for Black Decolonial AI.pdf
**Total Pages:** 16

---

## Content

```
--- Page 1 ---

arXiv:2502.16043v3  [cs.CY]  17 Jun 2025
African Data Ethics: A Discursive Framework for Black
Decolonial Data Science
Teanna Barrett
Paul G. Allen School of Computer
Science & Engineering
University of Washington
Seattle, Washington, USA
tb23@cs.washington.edu
Chinasa T. Okolo
The Brookings Institution
Washington, D.C., USA
cokolo@brookings.edu
B. Biira
Information School
University of Washington
Seattle, Washington, USA
bbiira@uw.edu
Eman Sherif
Paul G. Allen School of Computer
Science & Engineering
University of Washington
Seattle, Washington, USA
emans@uw.edu
Amy X. Zhang
Paul G. Allen School of Computer
Science & Engineering
University of Washington
Seattle, Washington, USA
axz@cs.uw.edu
Leilani Battle
Paul G. Allen School of Computer
Science & Engineering
University of Washington
Seattle, Washington, USA
leibatt@cs.washington.edu
Abstract
The shift towards pluralism in global data ethics acknowledges the
importance of including perspectives from the Global Majority to
develop responsible data science practices that mitigate systemic
harms in the current data science ecosystem. Sub-Saharan African
(SSA) practitioners, in particular, are disseminating progressive
data ethics principles and best practices for identifying and navi-
gating anti-blackness and data colonialism. To center SSA voices
in the global data ethics discourse, we present a framework for
African data ethics informed by the thematic analysis of an inter-
disciplinary corpus of 50 documents. Our framework features six
major principles: 1) Challenge Power Asymmetries, 2) Assert Data
Self-Determination, 3) Invest in Local Data Institutions & Infrastruc-
tures, 4) Utilize Communalist Practices, 5) Center Communities on
the Margins, and 6) Uphold Common Good. We compare our frame-
work to seven particularist data ethics frameworks to find similar
conceptual coverage but diverging interpretations of shared values.
Finally, we discuss how African data ethics demonstrates the oper-
ational value of data ethics frameworks. Our framework highlights
Sub-Saharan Africa as a pivotal site of responsible data science by
promoting the practice of communalism, self-determination, and
cultural preservation.
CCS Concepts
• Computing methodologies →Philosophical/theoretical founda-
tions of artificial intelligence; • Human-centered computing →
Human computer interaction (HCI).
Keywords
data ethics, AI ethics, data science, responsible AI, African philoso-
phy
This work is licensed under a Creative Commons Attribution-NonCommercial 4.0
International License.
Preprint,
© 2025 Copyright held by the owner/author(s).
ACM ISBN 978-x-xxxx-xxxx-x/YYYY/MM
https://doi.org/10.1145/nnnnnnn.nnnnnnn
ACM Reference Format:
Teanna Barrett, Chinasa T. Okolo, B. Biira, Eman Sherif, Amy X. Zhang,
and Leilani Battle. 2025. African Data Ethics: A Discursive Framework for
Black Decolonial Data Science. In Proceedings of Summer, 2025 (Preprint).
ACM, New York, NY, USA, 16 pages. https://doi.org/10.1145/nnnnnnn.nnnnnnn
1
Introduction
Artificial intelligence (AI), machine learning (ML), and data science
research and development are primarily conducted in economically
powerful countries such as the United States, China, the United
Kingdom, France, and Germany [11]. Consequently, data-driven
technology (DDT) leveraging these methodologies often reflect
the logics of large corporations and the hegemonic values of the
countries they are based in [15]. When ethical dilemmas arise within
data science development, mitigation strategies are often limited
by the perspectives of these actors who rarely experience the direct
consequences of data harm [27, 53, 78].
To balance these dominant perspectives, pluralistic data ethics
calls for perspectives from the Global Majority to better mitigate
systemic concerns [22, 108]. Embracing pluralism in global data
ethics acknowledges the limits of any single ethical perspective in
guiding comprehensive responsible data science (RDS) practices.
Unfortunately, Sub-Saharan African (SSA) 1 voices have routinely
been left out of data science ethics discussions [42]. This is a glaring
omission—African data collaborators have an intimate experience
with how anti-blackness and data colonialism operate in data sci-
ence work [2, 16, 42]. African people are often exploited as data
workers, their resources are extracted for computing infrastructure,
and even when deploying systems in their own communities, many
processes are managed and owned by external actors [14].
To address the underrepresentation of African perspectives in
global data ethics, African data scientists have returned to African
philosophies such as Ubuntu to articulate the current ethical dilem-
mas in data science work on the continent [53]. However, African
data ethics texts are spread across a variety of publication venues
and are rarely synthesized into a cohesive review or framework
1Throughout the rest of the document, Africa or SSA will be usedACM FAcct 2025
Proceedings to refer to Sub-Saharan Africa.

--- Page 2 ---

Preprint,
,
Barrett et al.
[38]. For this reason, it can be difficult to grasp common topics,
differing fields of thought, and how proposed principles translate
to current practices of RDS in Africa. In this work, we synthesize
the current African data ethics discourse and contextualize data
ethics theories through the application of African philosophies. We
conduct a thematic analysis of 50 documents from African philoso-
phy, information ethics, AI ethics, and human-computer interaction
(HCI) research to answer the following research question: What
are the African values and ethical theories that can inform
responsible data science (RDS) practices in Africa? As a re-
sult of our inquiry, we derived an ethical framework consisting of
six major principles rooted in the realities of data science work in
Africa (Table 1).
Our framework surfaces novel understandings, theories, and
practices for RDS in Africa that contend with the legacy of colonial-
ism and the current administration of neocolonialism to articulate
the inefficacy of current data science relations in African contexts.
Several principles also engage with a range of African commu-
nitarian theories to recontextualize common paradigms of social
good, participatory design, and comprehensive data ethics educa-
tion. The framework also exhibits the practical solutions African
data scientists offer to local governments, multinational technology
companies, grassroots collectives, and individual data scientists
engaged in the African data science ecosystem.
We place our framework in conversation with other particular-
ist data ethics frameworks to gauge its unique contributions to
global efforts. While every framework is concerned with imple-
menting technology for social good, we find African data ethics
problematizes vague universalist language and calls for material re-
dress for data harms. Overall, our work aims to bridge rich African
philosophical traditions with contemporary data science practices,
developing a framework that can guide responsible technology
development within African contexts while contributing to global
discussions on data ethics and justice.
2
Background
2.1
Pluralistic Efforts in Global Data Ethics
Data ethics encompasses the normative frameworks and moral
principles governing the collection, processing, storage, and de-
ployment of data [46]. An ethical principle, in a data ethics context,
represents a fundamental normative guide for action—such as
respect for persons, beneficence, or justice—that transcends mere
technical guidelines or professional best practices. What distin-
guishes genuine ethical principles from operational procedures
are their foundation in moral philosophy and their universal ap-
plicability across contexts. Literature within this field has pro-
posed new data ethics paradigms [20, 69, 120], critiqued current
approaches to responsible data science [47, 72, 117], and experi-
mented with algorithmic and other technical approaches to mitigate
bias [57, 116, 122]. While scholarly communities such as the ACM
Conference oACM FAcct 2025 Proceedingsn Fairness, Accountabil-
ity, and Transparency (FAccT) and the AAAI Artificial Intelligence,
Ethics, and Society (AIES) serve as platforms for engaging discourse
on AI and data ethics, a significant portion of the scholarship pro-
duced in these venues is primarily rooted in Western philosophy.
While Western philosophical traditions have dominated data
ethics discourse through frameworks such as utilitarianism and
deontological ethics [56, 81], emerging scholarship increasingly
recognizes the necessity of incorporating diverse ethical paradigms
and epistemological frameworks from Global Majority perspectives.
For example, Indigenous knowledge systems provide alternative
conceptualizations of data sovereignty and stewardship that chal-
lenge Western individualistic notions of privacy and ownership
[23, 59, 73, 102, 121]. East Asian philosophical traditions, including
Confucian ethics, contribute valuable insights regarding social har-
mony and collective responsibility in technological development,
offering nuanced frameworks for balancing individual rights with
communal interests in data-driven systems [33, 43, 127]. Traditional
African philosophy offers Ubuntu-based approaches that emphasize
collective well-being and communal responsibility in data ethics
[94, 107]. HCI and data ethics scholars have also applied knowledge
from Black studies such as Black feminism [106], critical race theory
[31], Afropessimism [32], prison abolitionism [12], and historical
and contemporary social analysis [17, 48, 80, 87] to articulate how
data technology perpetuates anti-black racism in the United States.
2.2
African Philosophy: Foundation of African
Data Ethics
African Philosophy is a sub-domain of philosophy meant to
reclaim and generate philosophical theories from Africans
[104]. Around the time of widespread decolonization, African
philosophers pivoted away from classic Western philosophy to
uncover the rich intellectual theories and practices of pre-colonial
Africans [125]. Beyond examining the past, African philosophers
have also worked to cultivate an intellectual home for Africans to
generate new philosophies that speak to the realities of African life
in modernity [67, 104].
Several African philosophical frameworks offer valuable insights
for data ethics and responsible technology development. The Yoruba
concept of “iwa” (character/moral behavior) emphasizes the ethical
implications of one’s actions on the collective community, sug-
gesting approaches to data governance that prioritize communal
benefit over individual gain [99]. Similarly, the Akan concept of
“onipa” (personhood) [98, 124] and the Zulu notion of Ubuntu, of-
ten translated as “umuntu ngumuntu ngabantu” (a person is a
person through other persons) [53, 107], provide frameworks for
understanding human dignity and agency in technological contexts,
particularly relevant for issues of consent and data sovereignty. The
Ethiopian philosophy of “Medemer” (synergy/coming together) of-
fers a model for collaborative data sharing and governance that
balances individual autonomy with collective benefit [7]. Addition-
ally, the Igbo concept of “omenala” (customs/traditions) [88, 90]
and the Swahili principle of “ujamaa” (familyhood) [91] suggest
that data governance should align with existing social structures
and cultural practices rather than imposing external frameworks.
Overall, these philosophies collectively lay the foundation for ethi-
cal frameworks that challenge Western individualistic approaches
to data privacy, data sharing, and ownership while promoting in-
terdependence and cultural alignment.

--- Page 3 ---

African Data Ethics: A Discursive Framework for Black Decolonial Data Science
Preprint,
,
2.3
Current AI Ethics Discourse in Africa
A growing number of technology researchers are leveraging African
philosophy to assess technological development and AI [8, 21, 44,
53, 110]. This work, along with foundational African philosophy,
can inform practical approaches to data collection protocols that
respect communal ownership and decision-making [18], inspire
algorithmic fairness metrics that incorporate African conceptions
of justice and equity [6], and help shape privacy policies that bal-
ance individual rights with community interests [61]. Additionally,
African philosophy can be valuable in informing ethics review pro-
cesses that consider local cultural contexts and values, and help
build data governance structures that reflect African leadership
models and decision-making practices [26]. Our work aims to help
bridge these issues and expand discourse on how African philoso-
phies can contribute to advancing responsible data science practices
within the continent.
2.3.1
Practitioner-led. Sábëlo Mhlambi’s pioneering work on African
data ethics, grounded in the principles of Ubuntu [77], draws from
the epistemic, ontological, and ethical theories of African philoso-
phers like Mogobe Ramose [103] to critique prevailing AI paradigms
[78]. Since Mhlambi’s Ubuntu data ethics contribution, a signifi-
cant amount of African scholarship on data ethics has highlighted
Ubuntu as an African philosophy that should be engaged with more
in global data ethics work [49, 53, 64, 70, 113]. This body of work
makes a general appeal to African communitarian ethics to cri-
tique current ethical paradigms [76], report on data science work
in Africa [34], and survey perceptions and concerns among African
data science practitioners [39]. There is also a plethora of African
data ethics gray literature published through African data organi-
zations (often in partnership or funded by institutions in Europe
or the United States) by way of blog posts [114], reports [115], and
formalized briefs [52]. It must also be noted that many contribu-
tions made by non-African data ethicists disproportionately fail to
engage with other African philosophies beyond Ubuntu.
2.3.2
Continental & Local Policy. The development of local and
continental policies for AI and data regulation can help African
countries improve adherence to data ethics frameworks while steer-
ing responsible AI development. Currently, 38/55 African Union
(AU) member states have enacted formal data protection regula-
tions, with Malawi and Ethiopia recently enacting data protection
laws in mid-2024 [92]. The African Union has also released conti-
nental frameworks, such as the African Union Convention on Cyber
Security and Personal Data Protection (Malabo Convention), which
mandates national cybersecurity policies and strategies while ad-
dressing personal data protection and cybercrime [118]. In parallel,
efforts to regulate AI are gaining momentum, with 14 countries
adopting national AI strategies [37], complemented by the AU’s
AU-AI Continental Strategy published in August 2024 [5]. However,
systematic gaps in data regulation persist [38, 63, 92, 97], and if left
unaddressed, these shortcomings may undermine AI regulatory
efforts. To advance data ethics and safeguard African communities,
governments must prioritize enforcement of existing data privacy
laws while ensuring regulations provide adequate protections.
3
Methods
Inspired by ongoing work, we have two aims in developing an
ethical framework for African data ethics: 1) honoring the existing
scholarship of African data ethicists by preserving distinct per-
spectives in the discourse, and 2) re-engaging with classic African
philosophies to productively expand on African data ethics princi-
ples. To achieve the balance between a respectfully discursive and
productively expansive framework, we combined methods from
qualitative document analysis and literature reviews to develop our
qualitative analysis protocol [10, 15, 82].
3.1
Data Collection
The first author seeded the search by reading The African Philoso-
phy Reader [28] due to prior exposure. This text informed subse-
quent keyword searches in established academic databases: Google
Scholar, Web of Science, Scispace,2 and the publication reposito-
ries of ACM and IEEE. The first author also searched their insti-
tutional library and online African philosophy libraries accessible
through their institution. They used key phrases such as “African
AI ethics”, “African philosophy” and “African data ethics”
to identify relevant literature. Documents from database searches
were excluded if African values and data science practices were
not the primary topic. In addition, documents were excluded if
they were not a full document. Full documents were understood as
non-archival and archival papers (no extended abstracts), reports,
or book chapters. No range was set on the publishing year to permit
the inclusion of foundational texts from African philosophy.
In parallel to keyword searches, we requested literature rec-
ommendations from other scholars in the field. In addition, we
used reference and citation tracking to identify relevant documents
missed in searches. By the end of our iterative data collection, 50
documents were collected. The details of document inclusions and
exclusions can be found in Appendix A.
3.2
Thematic Analysis
The first author reflexively coded the documents through a prac-
tice iteration followed by two rounds of coding to surface themes
of African data ethics. First, the first author began a grounded re-
flection process by selecting six documents as a representative set
of corpus topics [5, 30, 34, 77, 85, 113]. From this selection, she
highlighted and recorded meaningful excerpts from each document.
Then she noted how the excerpt answers the research question.
These reflections enabled the first author to focus on coding im-
plicit or explicit African ethical principles. In subsequent coding
iterations, we consider an African ethical principle to be a moral
value, understanding, or standard prioritized by or derived
from SSA communities. The first author then repeated the above
process for each document in the full corpus, in which she coded
excerpts that discussed African ethical principles relevant to RDS.
Then, she organized the resulting codes into themes through affin-
ity diagramming [112] using Miro.3 After the first full round of
coding and principle clustering, she identified several minor princi-
ples with conceptual gaps that required the analysis of additional
documents.
2Scispace is a language model search engine for literature reviews: https://typeset.io
3https://miro.com/

--- Page 4 ---

Preprint,
,
Barrett et al.
3.3
Positionality Statement
Our research team’s converging individual interests have led us
to develop and propose our framework for African data ethics.
The second author has extensive experience in developing AI pol-
icy in Africa and research expertise in developing explainable AI
paradigms for marginalized communities. Other authors identify
with a variety of African diasporic communities and are dedicated
to expanding the representation of Black data science communities
in their work on climate change, computer science education and
responsible data science. For the author who does not belong to the
African Diaspora, their work in pluralistic alignment of AI necessi-
tates learning about the values of all user communities especially
those on the margins. Since our research team is affiliated with aca-
demic and independent institutions based in the United States and
the majority are not directly involved in technology collectives or
disciplines represented in our corpus, the lens of epistemic humility
guided our framework construction.
The first author is a Black, Jamaican-American woman. She ac-
knowledges that her recent ethnicity is not Sub-Saharan African,
but is committed to engaging and contributing to African data ethics.
Her positionality as United States-educated, English monolinguist
and observer of African data ethics discourse limits generative
efforts. Her analytical perspective may also perpetuate misconcep-
tions of the myriad of African perspectives highlighted in the work.
As such, she aimed to reflexively guide the study by seeking guid-
ance from technologists, policymakers and thought leaders within
African data science communities.
4
African Data Science Ethical Framework
In this section, we summarize the key components of our framework
for African data ethics. For an overview of the six major princi-
ples, 19 associated minor principles and recommended practices or
policies derived from our analysis, view Table 1.
4.1
Challenge Power Asymmetries
Challenging power structures in technological development is not
only necessary to mitigate the perpetuation of colonial power lega-
cies, but also misuse and exploitation by any authority.
Challenge Colonial Power. RDS practices from the West do not
seamlessly transfer to the African context because these practices
are developed within colonial contexts disconnected from the reali-
ties of African practitioners and users [4, 22, 39–41, 49, 52, 93, 114].
African practitioners identify three dimensions in which the so-
ciotechnical disconnect harms responsible data science in Africa:
epistemic injustice, dehumanizing extraction, and dependent part-
nerships. Firstly, African scholars identify how philosophical epis-
temic injustice permeates global data ethics paradigms [39, 76, 95].
As many African philosophers agree, Enlightenment ideals (a pre-
mier part of the Western philosophical canon) were predicated
on colonialism and anti-black racism [52]. European colonizers
weaponized the Enlightenment emphasis on human rationality
to deem Africans sub-human by assessing them as primitive and
incapable of reason [71]. Colonization was not only justified but
encouraged by the philosophies of rationality. Colonizers deter-
mined they had a moral obligation to develop Africans capacity
for reason through European education. The legacy of colonialism
is why African data scientists encourage casting aside Western
perspectives to develop distinctly African RDS perspectives [77].
Additionally, an over reliance on “rational” performance metrics
encourages the same epistemic injustice that justifies and encour-
ages the marginalization of Africans in technology such as facial
recognition [19, 27, 53, 77].
Secondly, many documents recognize most African contribu-
tions to data science as disproportionately benefiting corporations
such as OpenAI, Google, Meta, and Microsoft [2, 25, 64, 85, 89]. The
computing demand of large-data systems such as AI proliferates
neocolonialism to new heights in Africa [40]. The work of Africans
within the data science ecosystem should benefit Africans first [67].
The fact that it currently does not is connected to the legacy of
colonialism and chattel slavery in which Africans were forced to ex-
tract their raw materials so colonialists could fuel industrialization
and capitalism in their home countries [14, 34, 77, 85, 114].
Finally, the last vestige of colonial power to be challenged in
African RDS are dependent partnerships. Africa currently lacks
the technical infrastructure for large-scale data-driven technology,
which pushes data scientists towards unfair agreements with power-
ful organizations to access vital resources [58, 96, 114]. Even worse,
companies such as Amazon, Google, Meta, and Uber use savior
language such as “liberating the bottom million” to describe their
digital services in Africa [2].
Challenge Internal Power Asymmetry. Critical African philoso-
phers conceptualize authoritarianism as governing to accumulate
wealth and power rather than serving the needs of citizens and
Africa as a whole [91]. Even after liberation from colonial rule,
many African philosophers accuse their governments of replac-
ing the colonial ruling class instead of dismantling it [29, 67]. To
maintain their position, government officials focus on maintain-
ing dependent relationships with the West and enforcing cultural
nationalism to suppress dissent [52].
African governments have already harnessed their control of
national technology through internet shutdowns [93]. Therefore,
to many authoritarian actors, powerful data technology is just
another tool for suppression. Of particular concern to many African
practitioners is China as a neocolonial collaborator with African
authoritarian leaders and governments. Chinese companies have
been found to provide the data technology Ethiopia, Uganda, and
Zimbabwe have used to surveil their citizens [93].
While authoritarian uses of data technology are resolutely un-
ethical, more widely accepted uses of government data-driven tech-
nologies are scrutinized as well. The ubiquitous deployment of digi-
tal identification systems force citizens to choose between accessing
important services or preserving their privacy from a system they
have no control over [52]. As governments consider adopting data
technology, they need to be held accountable to their citizens [3, 96].
To combat the misuse of government power, authors in our corpus
suggest data science initiatives should focus on improving govern-
ment efficiency, transparency, and enforcement of citizens’ freedom
[40, 52, 74].
4.2
Assert Data Self-Determination
Responsible African data science should be an avenue for bolstering
the self-determination of Indigenous African communities.

--- Page 5 ---

African Data Ethics: A Discursive Framework for Black Decolonial Data Science
Preprint,
,
Major Principle
Minor Principle
Practices & Policies
Challenge
Power
Asymmetries
Challenge Colonial Power
Adopt data science practices that are localized, decentralized, bottom-up and
in less deference to Big Tech paradigms
Challenge Internal Power Asymmetry
Establish agencies to triage citizen concerns and doubts about new technology
Assert
Data
Self-
Determination
"For Africans, By Africans"
Africans speak for themselves in global data ethics discourses, negotiations
for technical partnerships and design for local needs
Treasure Indigenous Knowledge
Conduct natural language processing projects to document and represent
indigenous languages
Protect Data Agency
Integrate communal conceptions of privacy for data protection such as data
trusts, data collaboration tools, and community data management
Invest in Local Data
Institutions & Infras-
tructures
Invest in Physical & Organizational Infras-
tructures
Construct secure and locally-run peer to peer networks
Cultivate Governance Infrastructure
Develop protocol for conducting algorithmic impact assessments
Support Formal & Informal Data Science
Collectives
Provide technical training and education for data scientists outside of the
university and working in the informal sector
Utilize Communalist
Practices
Ground Design in Community-Engaged
Consensus
Consult intended users on a routine basis to build trust and incorporate their
cultural perspectives in design
Instantiate Reciprocal Relationships
Collaborate with African organizations already conducting research or build-
ing technologies of interest
Mend Data-Driven Harms
Implement reconciliation processes that place disenfranchised communities
in positions of power and hold the perpetrating parties accountable
Center Communities
on the Margins
Design in Solidarity
Embrace diverse data ethics standards and avoid imposing standards on other
communities
Center Remote & Rural Communities
Develop AI solutions that address the needs of remote communities such as
agriculture, climate change, and healthcare accessibility
Center Women
Incentivize women-led data science entrepreneurship
Protect & Empower Youth
Organize continental meetings for young Africans to discuss the state of data
science in their communities
Uphold
Common
Good
Adopt Technology with a Measured Mind-
set
Appraise imported state-of-art technologies before use
Preserve the Dignity of Data Contributors
Treat every collaborator as morally responsible agents deserving of materially
and psychologically safe working conditions
Strive for Common Good with Systemic
Change
Build open data ecosystems that safeguard against harmful use and compen-
sate data subjects from economic gains
Maintain Harmony with Stakeholders
Update country-level data ethics to align with continental frameworks and
vice versa
Table 1: Overview of the major and minor principles of our proposed African data ethics framework as well as highlighted
practices and policies associated with each minor principle.
“For Africans, By Africans”. This principle is inspired by the
concerted efforts of African data scientists to reclaim leadership in
African data science work [25]. To combat deficit-based narratives
about Africa, scholars in our corpus call on African data scientists
to reclaim and celebrate their strength, rich cultures, and scientific
achievements in conducting RDS [2, 4, 22, 30, 52, 58, 71]. Given the
thousands of cultures that comprise Africa, African data scientists
believe that grounding African data technology development in
local talent, knowledge and data ethics can address local problems
effectively and at scale [5, 28, 29, 34, 36, 39, 49, 53, 67, 95, 110, 113,
114].
To achieve the ideal of African-led data science, the authors in
our corpus highlight several changes to how African data scientists
approach their work. African data should not be primarily collected
for technology powers or published for immediate and uncontrolled
use [14, 58]. Additionally, African data practitioners do not need
tech superpowers to speak for Africans on the global stage, only
provide off-the-shelf models, or oversee the standards of African
data science institutions; Africans are more than capable of leading
without interference [2, 3, 13, 49, 78, 85, 93]. This does not mean
Africans should not collaborate with external data practitioners
and vice versa [41, 58]. Rather, local African data practitioners must
lead data science work so its development is properly situated in
the communities in which the technology will be deployed [40, 64,
71, 89].
Treasure Indigenous Knowledge. With the legacy of colo-
nial epistemic injustice, African modernization and Indigenous
knowledge preservation are often viewed as at odds with each
other [5, 41, 67]. On the contrary, many documents hold Indige-
nous knowledge as a pivotal component of responsible data sci-
ence in Africa. As elders, griots, and other stewards of Indigenous
knowledge pass, younger generations are obligated to preserve
their community’s culture [68, 104].

--- Page 6 ---

Preprint,
,
Barrett et al.
Data-driven technology can be used to store Indigenous lan-
guages, customs, and history in close consultation with Indigenous
communities. There are over 1500 languages indigenous to Africa,
but very few are represented in data technology, such as natural lan-
guage processing (NLP), which leaves out large portions of Africans
from using ubiquitous technology [114]. Local communities can
never fully be represented if there is not an understanding of their
roots or history [104]. Building datasets that represent Indigenous
languages for inclusive models opens a whole set of new users
who can digitally store and analyze Indigenous knowledge that is
typically shared orally for future generations [79, 114]. However,
some scholars caution that releasing Indigenous information into
the globalized data ecosystem could lead to a loss of cultural control
and appropriation [2, 3, 5, 40]. The boundaries of what Indigenous
knowledge should be a part of data-driven technology must be
understood by consulting with the community before proceeding
on any project [68, 79].
African philosophers also emphasize Indigenous knowledge isn’t
limited to the past [58]. Pre-colonial Indigenous knowledge needs
to be reclaimed to develop African data values that reflect local
communities [1, 25]. Investing in African responsible data science
is an investment in creating new Indigenous knowledge [71, 119].
Local talent do not have to reinvent the wheel to explore open
questions in the more recent field of data science [71, 74, 79]. The
richness of African knowledge can develop new responsible data
science practices and understandings [1, 13, 29, 77].
Protect Data Agency. Given the legacies of extractive colonial-
ism, ownership is viewed as the key to data self-determination in
Africa [52, 64, 114]. African ownership in the data science process
can be achieved by codifying intellectual property rights [5], enforc-
ing data ownership [114], and exploring Indigenous conceptions of
collective privacy [49, 70, 74, 79, 89].
Africans are often regarded as “simply” data subjects [114]. How-
ever, the role of a data subject is materially essential to data science
work (without data, nothing can be done). Performance progress
narratives that require unbounded data consumption devalue data
subjects as dehumanized sources of raw material [14, 52, 77, 85, 95].
This devaluing encourages data collectors to share and use data
without the knowledge, consent, or compensation of data subjects
[91, 115]. Many African data ethicists call for a correction of this
narrative to recognize data subjects as the proper owners by shift-
ing power and access control to data subjects [1, 34, 110]. Achieving
this shift in ownership should be done by demanding data-sharing
terms and not working with data collaborators who do not honor
these terms [13, 93]. African ownership of data, resources for data
science, and technical contributions are a non-negotiable for re-
sponsible data science in Africa.
4.3
Invest in Local Data Institutions &
Infrastructures
Prioritizing infrastructure, investing in local talent, and establishing
sound policy and governance frameworks are essential for sustained
and independent RDS in Africa.
Invest in Physical & Organizational Infrastructures. To im-
plement data technology in Africa, practitioners call for investment
in physical data science infrastructure, assessment of the current ca-
pacities of technical infrastructure, and development of responsible
data management practices [79, 110]. Achieving this principle in
Africa is a big feat when electricity and broadband access is not only
sparse but one of the most expensive to access in the world [3, 93].
Nigeria, Mozambique, and Rwanda have recognized the need to
invest in technical infrastructure and have partnered with external
tech companies and international financial institutions to build their
respective capacities to host data-driven systems [93]. There are
also innovative ways to work with current technical infrastructure
to lessen reliance on external investment [77]. Technical infrastruc-
ture development should also coincide with the development of
responsible data management protocols so African data and data
science work are not vulnerable to dispossession [2, 52].
Cultivate Governance Infrastructure. The authors in our cor-
pus call for sustainable and measured governance infrastructure to
guide the development of data science in Africa [5, 25]. Policy mea-
sures and regulations are major priorities for African data science
communities. African Union member states are slowly developing
data protection regulations, but many documents stress the urgency
for African data policy [64, 101]. Without clear policies and legal
standards for RDS, African data scientists lack guidance in their
practices, leaving African communities vulnerable to data exploita-
tion from external and internal actors alike [2, 27, 75]. Governance
infrastructures include incremental regulations [52], monitoring
bodies [49], continental commitments [5], and algorithmic impact
assessments [115].
Support Formal & Informal Data Science Collectives. The
African population has low attainment of digital skills [3, 93]. As
large foreign technology companies set root in Africa, policymak-
ers stress the need for monumental efforts to train local talent
[5, 27, 77, 114]. Providing technical skills early in education will
help prepare a strong cohort of future data scientists [89, 115]. An
indispensable part of a comprehensive data science education is
data ethics [49, 64, 104]. A United Nations Educational, Scientific
and Cultural Organization (UNESCO) survey found that very few
African countries feel equipped to contend with the ethical impli-
cations of AI [64]. Teaching data ethics in Africa should involve
centering the lived experiences and cultures of the students [49, 64].
Students should be educated about the common harms of data sci-
ence and also develop their ethical discernment to prepare them
for the sociotechnical complexities of data science.
However, only focusing on supporting formal data science ed-
ucation (in which wider recognition and acceptance is a common
issue related to epistemic injustice [25, 39]) neglects a large portion
of potential data collaborators [58]. 81% of jobs in Africa are based
in informal economies [114]. There should also be investments in
integrating AI curricula in informal organizations like the Data
Values Project to reduce educational barriers [114]. There should
be efforts to connect Africans interested in using data science for
entrepreneurship [13, 114] and accessible data science job training
[2]. Capacity-building in Africa necessitates the support of formal
and informal data science collectives [2, 93].
Crucially, scholars in our corpus recommend dismantling the
boundary between formal and informal data organizations to ex-
change technical knowledge, coordinate work, and pool resources
[35, 66]. Both forms of collectives have vital affordances and need

--- Page 7 ---

African Data Ethics: A Discursive Framework for Black Decolonial Data Science
Preprint,
,
to rely on each other to flourish. One form of collective is not meant
to replace the other [96]. If both of these collectives are not sup-
ported, African data scientists will have to seek support outside
of their communities, which furthers the “brain drain” of highly
skilled Africans to global superpowers [93]. Investing in collectives
also builds a workforce for in-house development which reduces
foreign dependence [22, 64, 101].
4.4
Utilize Communalist Practices
The development and deployment of data-driven technology should
mitigate harms, involve communities in decision-making, and en-
sure reciprocal benefits for African stakeholders.
Ground Design in Community-Engaged Consensus. Consensus-
building is a well-practiced strategy from African communities that
can inform responsible practices and encourage effective collabora-
tion [126]. Rather than majority-rule common in European societies,
African elders discuss issues until they all agree on a final decision
[22, 125]. Achieving consensus requires the final decision to be
1) the dominant view of the group, 2) in line with the common
good, and 3) aligned with the morals of the individual parties [30].
Consensus should be broached in an environment of trust, practical
reason, humility, openness, and respect for the viewpoints of all
involved parties [30, 52, 53, 77, 89, 93].
Community engagement provides spaces for consensus in the
data science lifecycle to include more perspectives [34, 74]. Akan
philosophies regard the community as an invaluable resource that
guides how every individual lives [30, 53, 76, 78, 125]. Therefore,
community input is crucial for constructing a full picture of techni-
cal requirements, especially in high-stakes domains [40, 77, 115].
The concept of community can be misappropriated to deem any
collection of stakeholders as sufficient community representatives.
African communitarian ethics define a community as individuals
with a shared identity who are emotionally invested in each other
[54, 89, 110, 115]. With this more narrow definition of community,
involving affected communities in all stages of the lifecycle requires
building trust and respecting boundaries by gaining an understand-
ing of cultural norms [2, 3]. Additionally, community members
should be sufficiently trained or educated on the nature of the
technology so they can provide well-informed input [4, 101, 114].
Consensus processes should also include procedures for docu-
mentation to keep track of disagreements, dissenting opinions, and
the progression of project values [66]. It is not easy to achieve these
conditions, so conflict management, negotiation, and reasonable
bargaining are helpful mechanisms to fully consider and resolve
contradicting positions [35, 52, 96]. Consensus should be a dynamic
feedback loop to ensure every contributor is on the same page about
the team’s approach to RDS [2, 36, 52, 67, 89, 113, 119]. Community-
centered consensus-building is a co-creation process in which all
stakeholders depend on each other [2, 4, 64, 67, 70, 71, 89].
Instantiate Reciprocal Relationships. In many African philoso-
phies, reciprocity is the foundation of a healthy society. In Akan so-
ciety, practicing reciprocity ensures that community needs are met,
while building deep social bonds [126]. African perfectionist propo-
nents go as far as to assert that assisting others in achieving their
goals makes someone more of a person [123, 126]. Without reci-
procity, society becomes imbalanced and co-dependent [30, 78, 91].
There are numerous examples of African data subjects not reap-
ing any benefits from the data collaborations they participate in
[2, 52]. This often leads to technically mediated harms while the
controllers of data amass profits [52]. Therefore, sustainable RDS
should practice reciprocity on several dimensions [126]. If some-
one contributes to DDT they should meaningfully benefit from the
system or project [54, 77, 115]. Inspired by philosophies such as
Ubuntu or Ujamaa, DDT should operate in a manner that benefits
the society in which they are created and deployed [4, 36, 40].
Given the current gap between Africa’s AI readiness and grow-
ing interest in AI adoption, many concede external partnership as
a necessity [5, 41]. However, exploitative external relationships set
a precedent that curtails African self-determination in data science
work [85, 115]. When building relationships, there are established
obligations that each collaborator owes to the other [30, 76]. Data
collaborations must be predicated on trust, fair attribution of work,
and a commitment to prioritizing the agency of African collabora-
tors [2, 4, 52, 89, 123, 126].
Mend Data-Driven Harms. When disagreements, conflict, or
harm occur at any stage of the data science lifecycle, African data
ethicists assert the need for mechanisms of accountability and
reconciliation to correct wrongs and empower those impacted. In
African societies, harm is not just actively making someone’s life
worse but also neglecting obligations to the community [54, 125]. A
person who causes harm is viewed as a moral failure who must be
corrected by their community through sanctions and even mental
rehabilitation to address deeper issues connected to their poor
actions [30, 126]. Even the most powerful members of society, such
as chiefs, are subject to correction and even dismissal by their
community for misconduct [125].
The adoption of AI and other DDT have already caused harm to
African populations by way of data bias, socio-economic risk, and
privacy violations [3]. There are African data ethicists who stress
the need to develop procedures for communities and individuals
harmed by DDT to seek restitution [52, 78]. These solutions are
dependent on African governments and external multinational
organizations committing to transparency, equality, and restorative
practices [5, 36, 52, 64, 93]. African governments can mitigate data
harm by being transparent about their potential data collaborations,
outlining their plans for data protection before, during, and after the
deployment of DDT, and enforcing mechanisms of accountability
and dissent from their citizens [114, 115]. Similar to the dismissal of
chiefs, powerful stakeholders acting outside of their agreed duties,
must experience restorative consequences, not just a slap on the
wrist [13, 29, 52, 70, 75, 77, 78, 85, 114].
4.5
Center Communities on the Margins
Community involvement ensures African DDT considers the needs
and potential impacts of rural communities, women, youth and
populations beyond the end-users.
Design in Solidarity. Solidarity is understood as looking out
for other diverse communities based on mutual respect and the
goal of social cohesion [52, 77]. In Ubuntu understanding, solidarity
is a deep care for others, including people of the past, present, fu-
ture, and the environment [36, 52, 53, 78, 93]. With this perspective,

--- Page 8 ---

Preprint,
,
Barrett et al.
African data scientists in our corpus call for DDT to not be devel-
oped with only the end user in mind but all other communities that
could be impacted by the technology [53, 54, 95].
While Africa needs to be included in global data science efforts,
Africa itself is home to vastly diverse communities that should also
be appropriately represented in these efforts [4, 49, 52]. African
communities’ underrepresentation in datasets across all data sci-
ence tasks is due to, as Gwagwa described, being “uncounted, un-
accounted, and discounted” [52]. Leaving communities out of data
also excludes them from the benefits DDT provide [53]. Given the
need to build explicitly African DDT, the lack of African datasets is
a threat to efficacy [3, 93, 95]. Including marginalized communities
requires mutual respect for diverse perspectives and creating pro-
cedures such as impact assessments to provide opportunities for
inclusive input [2, 5, 49, 77]. In addition, it’s important to challenge
the social, political, and economic dynamics that push communities
to the margins in the first place [2, 34, 64, 95, 113, 119].
Solidarity violations between African countries is of particular
concern. The success of one African community should not be
predicated on the suffering of another [13, 85]. Upholding solidarity
means that all actions made in the data science lifecycle should
explicitly protect or improve the lives of vulnerable or marginalized
communities. Exploiting the vulnerability of another is not only
unethical but unsustainable due to our interconnected nature. The
suffering of one community will eventually lead to the destruction
of all communities [89]. Banding together, “watching one another’s
back,” and developing DDT as a united front is key to mitigating
harm [91, 95].
Center Remote & Rural Communities. Development, espe-
cially technical development, is usually focused in urban centers
and excludes remote and rural communities [3, 96, 115]. Given the
lack of infrastructure in remote and rural communities, DDT should
be used to develop and optimize infrastructures and public services
for these regions [5, 22]. However, it’s important to keep in mind
that RDS done on behalf of rural and remote communities that do
not consider their culture, livelihoods, and direct input can lead to
harm [5, 22, 85].
Center Women. Due to the prevalence of patriarchy in many
African societies, authors in our corpus encourage the agency
of women in data science efforts. A few documents suggest that
women-led technology businesses and the education of women and
girls should be incentivized [5]. However, open questions remain
about how to maintain African women’s participation in a field
known to be male-dominated and antagonistic to women [5, 52].
Afro-feminists have a response to the techno-chauvinism that
dominates data science [115]. Rather than centering women in
general, there must be a recognition of the intersectional status
of African women [115]. As articulated by Rosebell Kagumire,
African women experience domination through systems of pa-
triarchy, race, sexuality, and global imperialism [30, 35]. There-
fore, data-driven technology should be developed with the com-
plex needs of African women in mind, because their compounded
experiences of marginalization provide insight into the needs of
various oppressed populations [115]. There are numerous examples
of African women harnessing the internet to fill in the gaps of
an oppressive society and DDT holds similar potential [35]. For
example, Chil AI Lab Group is a women-led data science collective
successfully using data technology to address the often neglected
health needs of women in Africa [40].
Protect & Empower Youth. Africa is a young continent with
a large population of educated and digitally native youth [49, 89].
Prioritizing the youth of Africa is a two-pronged principle: 1) protect
young people from harm and 2) empower youth to lead data science
agendas. The youngest generation has a tech-savviness transferable
to data science skills [2, 5, 14]. If youth are expected to be the first
adopters of African data technology then these systems should be
designed to protect youth so they cannot be taken advantage of.
Their comfort with technology may lead them to uncritically adopt
a “move fast and break things” approach [2, 110]. To address these
concerns, data science work should be intergenerational. African
data technology should enrich the development of African youth
and empower them to innovate, imagine, and contribute to bettering
the communities they are a part of.
4.6
Uphold Common Good
Ethical development and deployment of DDT requires a commit-
ment to upholding fundamental human dignity and ensuring these
technologies benefit all.
Adopt Technology with a Measured Mindset. Various schol-
ars in our corpus want the development of African data science
ecosystems to be balanced, measured, inclusive, and community-
minded [3, 40, 67]. Without this approach, the adoption of AI and
other data technologies can lead to more unrest and inequality
across Africa. To many, the potential of DDT is profound and would
change the trajectory of African development [5, 74]. Data are
viewed as the driving resource for the Fourth Industrial Revolution
[22, 52]. There are African data scientists and governments who
insist joining the AI boom will provide Africa the quality of life
benefits afforded to the major players of past industrial revolutions
[29, 67, 93].
However, there is skepticism towards wholeheartedly diving
into large-scale data science adoption [95, 119]. There is a need
to quell the AI hype as the solution for all African problems and
consider who will actually be served: Africans or the external pow-
ers propelling the AI boom [14, 115, 123]. Through the paradigm
of measured development, technical development should move at
the pace of social development [64, 91]. Paulin Hountondji’s cri-
tique of science in Africa applies well to data science development.
Development should not be driven by “scientific extroversion” or
catching up with global superpowers [49, 58]. Rather, the develop-
ment of data science should be an investment in the progress of
African people based on African intellect, priorities, and visions of
the future [13, 114].
Preserve the Dignity of Data Contributors. Every human and
community deserves humane treatment, and African scholars in our
corpus do not want data technology to ever violate human dignity
[77, 95]. The African Charter on Human and Peoples’ Rights and
the Universal Declaration on Human Rights set the precedent for
the just treatment of humans [5]. Regardless of these laws, African
philosophies necessitate respect for human dignity because humans
should be inherently valued for their existence and connection to
others [36, 76, 113]. Every human must be treated with respect,
care, and concern for their well-being [30, 35, 54, 125, 126]. In

--- Page 9 ---

African Data Ethics: A Discursive Framework for Black Decolonial Data Science
Preprint,
,
applying the principle of universal dignity to RDS practices, every
person involved in the data science lifecycle should be respected.
Individuals should not be used as a means to execute data work
[76, 104]. Rather, all efforts should be taken to ensure their well-
being and dignity are preserved when asked to contribute to DDT
[2, 52]. This same respect also extends to communities. Collective
agreements need to be honored, and collective work or resources
should not be used in a manner that threatens the well-being of the
community [79]. While this principle is self-evident, there are many
cases in which the rights of Africans were violated for large-scale
DDT [5, 67, 79, 113].
Strive for Common Good with Systemic Change. African
scholars view responsible data science as contributing to the safety,
health, and goodness of all [95]. In various African philosophies, a
person is defined by their commitment to acting for the benefit of
those around them [1, 5, 30, 54, 78, 89, 110, 126]. DDT have to be
made with the explicit goal of improving society and dismantling
systemic harms [40, 93, 115]. In Africa, improving the efficacy of
agriculture practices, healthcare access, responsiveness of public
services, and the security of financial services are over-arching
priorities [22, 67]. Achieving common good involves incorporating
collective values early in the process [36, 70], guiding development
with regulatory toolkits [95], not focusing on individualistic profit
maximization [35, 52, 74, 77, 91, 113], and encouraging the open
sharing of data [2, 34, 52]. The ultimate goal of RDS in Africa is
upholding common good [22, 74, 76, 95].
Maintain Harmony with Stakeholders. Scholars in our cor-
pus urge for DDT to further the mutual well-being of all stake-
holders. In addition, data standards and frameworks will be most
effective when they harmonize with each other [52, 64, 74, 123]. In
many African philosophies, harmony is not a state but a dynamic
and reciprocal process of calibrating one’s actions in response to
changes in the environment. In Ubuntu ethics, dogmatism is re-
jected because it impedes individuals from acting in harmony with
the changing world [103]. In Akan philosophy, morality is defined
as acting in line with collective human interests [126]. Upholding
harmony in data science can be understood through two dimen-
sions: impact and practice.
Data should be harnessed to bring people closer to their environ-
ment so they can act in the best interests of not only themselves but
also those around them. In terms of practice, data ethics frameworks
are most effective when all the elements of data science work are ac-
counted for [52, 64]. Also, acknowledging the unique ethical needs
at each stage of the data science lifecycle can inform an adaptable
practice of RDS. As Gwagwa, et al. assert, the harmonious practice
of RDS in Africa requires country-level data ethics frameworks to
be in alignment with frameworks developed at the continental level
[53].
5
Orienting African Data Ethics
Now, we orient the African data ethics framework we proposed
in the previous section by placing it in conversation with larger
data ethics and African philosophy discourses. First, we summarize
moral imperatives raised in our framework by connecting politi-
cal analyses of African “development”. Next, we code data ethics
framework papers from different data science communities to ex-
plore how our framework relates to the larger data ethics discourse.
Finally, we highlight how our framework raises a new perspective
on what it means to operationalize data ethics.
5.1
The Role of “Development” in African Data
Ethics
Rethinking power relations is the root of all of the values presented
in our framework. Each principle offers two-fold analyses of how
power relations in African data science hamper responsible prac-
tices. On one hand, neocolonial forces bring harm to Africans in
the data science lifecycle and assert control that robs Africans of
agency over their DDT. On the other hand, there are internal power
asymmetries in existing sociopolitical dynamics that push fellow
Africans to the periphery and can lead to further marginalization. By
confronting these two dimensions of power asymmetries, African
data ethics shows how RDS is not only an approach to technical
work but an avenue for progressive power redistribution.
The focus on self-organizing power seamlessly connects to clas-
sic African scholarship about development in Africa. Scholars such
as Walter Rodney in How Europe Underdeveloped Africa presents the
European extraction of African resources, exploitation of African
people and suppression of African state-building as a means to keep
Africa in a state of limited development [86, 109]. However, other
scholars acknowledge the impact of colonialism and imperialism
but place the responsibility for Africa’s lack of development on
African leaders [51]. The elitism, corruption, and power-hungry
tendencies of African leaders harm everyday citizens and the sus-
tainable progress of their nations [60]. Rather than choosing a
side in this debate, our framework discourse demonstrates both
problems must be overcome concurrently for progress to be made.
Many scholars go a step further to even problematize the concept
of “development” because the metrics for being “developing” or “de-
veloped” are set by global superpowers [84]. Therefore, to imagine
responsible African data science beyond AI readiness metrics, it’s
important for African scholars to define what success looks like to
them. Our analysis of the African data ethics corpus surfaces a set
of clear goals for future African data science grounded in moral clar-
ity and ideological traditions. These value-laden objectives guide
and continue to guide the critiques, initiatives, and policies Africa
develops for RDS. For examples of African data science initiatives
aligned with the principles of our framework, see Appendix B.
5.2
Comparing Across Particularist Data Ethics
Frameworks
We compare our framework to seven particularist frameworks to
gauge the breadth of our work alongside: intersectional feminists
[65], Western technology powers [45], Indigenous communities
of Turtle Island [24], policymakers from global superpowers [62],
Central Asian data scientists [128], Muslim data scientists [105] and
Black American data scientists [80]. We call these works particular-
ist frameworks because the authors of each paper aim to present
the data science values of distinct global communities and apply
the ethical theories of distinct philosophical traditions. The first
author reviewed each framework and used the minor principles in

--- Page 10 ---

Preprint,
,
Barrett et al.
our African data ethics framework as a codebook (see Appendix C
for comparative coding results).
Each framework covered, at most, 68% of our proposed 19 princi-
ples. Delving into the diverging and converging principles provides
insight into how African data ethics deepens global data ethics
discourse through particularism.
None of the frameworks discussed Centering Remote and
Rural communities. Our framework highlights RDS for rural
communities because they represent a significant portion of Africa
and have unique needs not fully met by the status quo [9]. Com-
munities have distinct shared experiences that inform their values
and normative understandings of the world. Engaging with data
ethics from different cultural standpoints exposes data scientists to
approaches or potential harms they would have never considered
[111].
Strive for Common Good with Systemic Change and Ground
Design in Community-Engaged Consensus were the only prin-
ciples discussed by all the frameworks. This finding also falls in
line with a popular understanding of philosophy: universalism. The
whole RDS community is broadly guided by a universalist commit-
ment to social good [45]. However, upon closer review, references to
the common good in non-African frameworks often remain abstract,
lacking the depth and specificity seen in the work of African data
ethicists. African appeals to universalism are grounded in the tradi-
tion of speaking truth to power. Drawing from critiques of interna-
tional human rights law, African scholars highlight the importance
of pairing narrative restoration—the recognition and reclamation of
African humanity and agency—with material restoration, including
tangible reparative actions [13, 50, 100]. Our framework corpus
notes numerous examples of data science practices in Africa violat-
ing the knowledge, ownership, and safety of African communities.
Social good is often taken for granted as an obvious universal goal
for RDS. However, African data ethics urges the RDS community
to confront the harm they have caused before it can truly achieve
social good.
5.3
Reframing the Operationalization of Data
Ethics
The primary critique of data ethics frameworks is the difficulty of
operationalizing ideals into effectual protocols or technical prac-
tices [83]. We offer a new perspective on the utility of data ethics
frameworks: constructing frameworks is an essential operation in
itself for RDS.
Articulating values and moral convictions are the first steps to
contextualizing responsible data science in the epistemic traditions
implicitly embedded in current practices, the socio-political status
quo, and the future worlds to build for. Surfacing these contexts is
important because they afford data scientists the ability to make
technical decisions, develop projects, and outline long-term goals
with a clear vision. The African scholars in our corpus recognize
that if they don’t set the moral vision for data science in their
communities, African data science will implement the divergent and
often times destructive vision of global superpowers. For example,
Western longtermism imagines a world in which DDT dominates
humanity [48], while Afrofuturism imagines a future in which DDT
joins with humanity to build a more just world [1]. Articulating
optimistic, collectivist, and resolutely African moral visions such as
Afrofuturism is crucial for Africa as an emerging site of data science.
Thus, as responsible data scientists, we must take responsibility
for envisioning and implementing futures for ourselves and our
communities. Otherwise, we remain at risk of perpetuating the
injustices we seek to mitigate with RDS.
6
Limitations
Our reflexive thematic analysis should not be conflated with a sys-
tematic literature review. While we cast a wide net to build our
corpus (including gray literature), there are impactful African data
ethics documents not included in our framework. Therefore, the re-
sulting framework should not be considered comprehensive but an
introduction to notable ideas. Future work will aim to incorporate
more African data ethics documents and engage African practition-
ers to evaluate the merits, gaps, and usability of our framework.
7
Conclusion
Through a thematic analysis of 50 documents, we derived an African
data ethics framework that encompasses six major principles: 1)
Challenge Power Asymmetries, 2) Assert Data Self-Determination,
3) Invest in Local Data Institutions & Infrastructures, 4) Utilize
Communalist Practices, 5) Center Communities on the Margins,
and 6) Uphold Common Good. Our framework scratches the sur-
face of African data ethics discourse, and the surface is rich with
historically grounded, communitarian, and pragmatic insights for
RDS.
A comparative analysis of our framework with seven other data
ethics frameworks highlights African perspectives as progressive
and needed voices in global data ethics discourse. For truly plural-
istic and responsible data science, we urge the RDS community to
readily seek the moral perspectives of Africans, other practitioners
of the Global Majority, and the particular data science communities
to which they belong. Such reflexivity will not only enrich the theo-
retical foundation of data ethics but can inform more equitable and
culturally responsive approaches to data governance, algorithmic
fairness, and technological development.
Acknowledgments
Thank you to Joseph Asike, George Obaido, Innocent Obi Jr., and
Andrew Shaw for additional advice and support. The work pre-
sented was funded in part by the NSF (award # 2141506), the Sloan
Foundation, and Google.
References
[1] Ojochogwu S. Abdul. 2023. Transhumanism, Singularity and the Meaning of Life:
An Afrofuturist Perspective. Springer International Publishing, Cham, 97–119.
doi:10.1007/978-3-031-36163-0_8
[2] Rediet Abebe, Kehinde Aruleba, Abeba Birhane, Sara Kingsley, George Obaido,
Sekou L. Remy, and Swathi Sadagopan. 2021. Narratives and Counternarra-
tives on Data Sharing in Africa. In Proceedings of the 2021 ACM Conference
on Fairness, Accountability, and Transparency (Virtual Event, Canada) (FAccT
’21). Association for Computing Machinery, New York, NY, USA, 329–341.
doi:10.1145/3442188.3445897
[3] Abejide Ade-Ibijola and Chinedu Okonkwo. 2023. Artificial Intelligence in
Africa: Emerging Challenges. Springer International Publishing, Cham, 101–117.
doi:10.1007/978-3-031-08215-3_5
[4] David Ifeoluwa Adelani, Graham Neubig, Sebastian Ruder, Shruti Rijhwani,
Michael Beukman, Chester Palen-Michel, Constantine Lignos, Jesujoba O. Alabi,

--- Page 11 ---

African Data Ethics: A Discursive Framework for Black Decolonial Data Science
Preprint,
,
Shamsuddeen H. Muhammad, Peter Nabende, Cheikh M. Bamba Dione, An-
diswa Bukula, Rooweither Mabuya, Bonaventure F. P. Dossou, Blessing Sibanda,
Happy Buzaaba, Jonathan Mukiibi, Godson Kalipe, Derguene Mbaye, Amelia
Taylor, Fatoumata Kabore, Chris Chinenye Emezue, Anuoluwapo Aremu, Perez
Ogayo, Catherine Gitau, Edwin Munkoh-Buabeng, Victoire M. Koagne, Allah-
sera Auguste Tapo, Tebogo Macucwa, Vukosi Marivate, Elvis Mboning, Tajud-
deen Gwadabe, Tosin Adewumi, Orevaoghene Ahia, Joyce Nakatumba-Nabende,
Neo L. Mokono, Ignatius Ezeani, Chiamaka Chukwuneke, Mofetoluwa Adeyemi,
Gilles Q. Hacheme, Idris Abdulmumin, Odunayo Ogundepo, Oreen Yousuf, Ta-
tiana Moteu Ngoli, and Dietrich Klakow. 2022. MasakhaNER 2.0: Africa-centric
Transfer Learning for Named Entity Recognition. doi:10.48550/ARXIV.2210.
12391 Version Number: 2.
[5] African
Union.
2024.
Continental
Artificial
Intelligence
Strat-
egy.
https://au.int/sites/default/files/documents/44004-doc-EN-
_Continental_AI_Strategy_July_2024.pdf
[6] Mercy Nyamewaa Asiedu, Awa Dieng, Iskandar Haykel, Negar Rostamzadeh,
Stephen Pfohl, Chirag Nagpal, Maria Nagawa, Abigail Oppong, Sanmi Koyejo,
and Katherine Heller. 2024. The case for globalizing fairness: a mixed methods
study on colonialism, AI, and health in Africa. In Proceedings of the 4th ACM
Conference on Equity and Access in Algorithms, Mechanisms, and Optimization.
1–24.
[7] Tefera Assefa et al. 2024. A Critical Review of Medemer from Ideological
Perspectives. African Journal of Political Science 12, 1 (2024), 119–135.
[8] Aribiah David Attoe, Segun Samuel Temitope, Victor Nweke, John Umezurike,
and Jonathan Okeke Chimakonam. 2023. Conversations on African Philosophy
of Mind, Consciousness and Artificial Intelligence. Springer Nature.
[9] Christopher
B.
Barrett,
Luc
Christiaensen,
Megan
Sheahan,
and
Abebe Shimeles. 2017.
On the Structural Transformation of Rural
Africa.
Journal of African Economies 26, suppl_1 (06 2017), i11–
i35.
doi:10.1093/jae/ejx009
arXiv:https://academic.oup.com/jae/article-
pdf/26/suppl_1/i11/19407068/ejx009.pdf
[10] Leilani Battle and Alvitta Ottley. 2024. What Do We Mean When We Say “In-
sight”? A Formal Synthesis of Existing Theory. IEEE Transactions on Visualization
and Computer Graphics 30, 9 (2024), 6075–6088. doi:10.1109/TVCG.2023.3326698
[11] Yoshua Bengio, Sören Mindermann, Daniel Privitera, Tamay Besiroglu, Rishi
Bommasani, Stephen Casper, Yejin Choi, Danielle Goldfarb, Hoda Heidari, Leila
Khalatbari, Shayne Longpre, Vasilios Mavroudis, Mantas Mazeika, Kwan Yee
Ng, Chinasa T. Okolo, Deborah Raji, Theodora Skeadas, Florian Tramèr, Bayo
Adekanmbi, Paul Christiano, David Dalrymple, Thomas G. Dietterich, Edward
Felten, Pascale Fung, Pierre-Olivier Gourinchas, Nick Jennings, Andreas Krause,
Percy Liang, Teresa Ludermir, Vidushi Marda, Helen Margetts, John A. McDer-
mid, Arvind Narayanan, Alondra Nelson, Alice Oh, Gopal Ramchurn, Stuart
Russell, Marietje Schaake, Dawn Song, Alvaro Soto, Lee Tiedrich, Gaël Varo-
quaux, Andrew Yao, and Ya-Qin Zhang. 2024. International Scientific Report
on the Safety of Advanced AI (Interim Report). arXiv preprint arXiv:2412.05282
(2024).
[12] Ruha Benjamin. 2019. Race After Technology: Abolitionist Tools for the New Jim
Code. Polity, USA.
[13] Steve B. Biko. 2004. Black Consciousness and the quest for a true humanity. In
The African Philosophy Reader. Routledge, 93–101.
[14] Abeba Birhane. 2020. Algorithmic Colonization of Africa. SCRIPT-ed 17, 2 (Aug.
2020), 389–409. doi:10.2966/scrip.170220.389
[15] Abeba Birhane, Elayne Ruane, Thomas Laurent, Matthew S. Brown, Johnathan
Flowers, Anthony Ventresque, and Christopher L. Dancy. 2022.
The For-
gotten Margins of AI Ethics. In Proceedings of the 2022 ACM Conference on
Fairness, Accountability, and Transparency (Seoul, Republic of Korea) (FAccT
’22). Association for Computing Machinery, New York, NY, USA, 948–958.
doi:10.1145/3531146.3533157
[16] Benedetta Brevini, Irene Fubara-Manuel, Clément Le Ludec, Jakob Linaa Jensen,
Andrea Jimenez, and Jo Bates. 2024. Critiques of Data Colonialism (1 ed.). Bristol
University Press, 120–137. http://www.jstor.org/stable/jj.15617032.11
[17] SIMONE BROWNE. 2015. Dark Matters: On the Surveillance of Blackness. Duke
University Press. http://www.jstor.org/stable/j.ctv11cw89p
[18] Michael Max Bühler, Igor Calzada, Isabel Cane, Thorsten Jelinek, Astha Kapoor,
Morshed Mannan, Sameer Mehta, Vijay Mookerje, Konrad Nübel, Alex Pentland,
et al. 2023. Unlocking the power of digital commons: Data cooperatives as
a pathway for data sovereign, innovative and equitable digital communities.
Digital 3, 3 (2023), 146–171.
[19] Joy Buolamwini and Timnit Gebru. 2018. Gender shades: Intersectional accu-
racy disparities in commercial gender classification. In Conference on fairness,
accountability and transparency. PMLR, 77–91.
[20] Christopher Burr and David Leslie. 2023. Ethical assurance: a practical ap-
proach to the responsible design, development, and deployment of data-driven
technologies. AI and Ethics 3, 1 (2023), 73–98.
[21] Rafael Capurro. 2008. Information ethics for and from Africa. Journal of the
American Society for Information Science and Technology 59, 7 (May 2008), 1162–
1170. doi:10.1002/asi.20850
[22] Mary Carman and Benjamin Rosman. 2023. Applying a Principle of Explicability
to AI Research in Africa: Should We Do It? Springer International Publishing,
Cham, 183–201. doi:10.1007/978-3-031-36163-0_13
[23] Stephanie Russo Carroll, Ibrahim Garba, Oscar L Figueroa-Rodríguez, Jarita
Holbrook, Raymond Lovett, Simeon Materechera, Mark Parsons, Kay Raseroka,
Desi Rodriguez-Lonebear, Robyn Rowe, et al. 2023. The CARE principles for
indigenous data governance. Open Scholarship Press Curated Volumes: Policy
(2023).
[24] Stephanie Russo Carroll, Edit Herczog, Maui Hudson, Keith Russell, and Shelley
Stall. 2021. Operationalizing the CARE and FAIR Principles for Indigenous data
futures. Scientific Data 8, 1 (April 2021), 108. doi:10.1038/s41597-021-00892-0
[25] Alan Chan, Chinasa T. Okolo, Zachary Terner, and Angelina Wang. 2021. The
limits of global inclusion in AI development. arXiv preprint arXiv:2102.01265
(2021).
[26] Gregory Emeka Chinweuba. 2019. Philosophy and Governance in Contemporary
Africa. LASU Journal of Philosophy 2, 1 (2019), 95–108.
[27] Moustapha Cisse. 2018. Look to Africa to advance artificial intelligence. Nature
562, 7728 (Oct. 2018), 461–461. doi:10.1038/d41586-018-07104-7
[28] P.H. Coetzee and A.P.J. Roux (Eds.). 2004. The African Philosophy Reader (0 ed.).
Routledge. https://www.taylorfrancis.com/books/9781135884192
[29] Pieter H. Coetzee. 2004. Later Marxist morality: Its relevance for Africa’s post-
colonial situation. In The African Philosophy Reader. Routledge, 641–653.
[30] Pieter H. Coetzee. 2004. Particularity in morality and its relation to community.
In The African Philosophy Reader. Routledge, 321–337.
[31] Grisha Coleman and Stephanie L Batiste. 2024. Blk as Tek | echo::system and
Black Performance Technologies. In Proceedings of the 9th International Con-
ference on Movement and Computing (Utrecht, Netherlands) (MOCO ’24). As-
sociation for Computing Machinery, New York, NY, USA, Article 1, 9 pages.
doi:10.1145/3658852.3658854
[32] Jay Cunningham, Gabrielle Benabdallah, Daniela Rosner, and Alex Taylor. 2023.
On the Grounds of Solutionism: Ontologies of Blackness and HCI. ACM Trans.
Comput.-Hum. Interact. 30, 2, Article 20 (April 2023), 17 pages. doi:10.1145/
3557890
[33] Paul D’Ambrosio. 2023. AI Ethics Beyond the Anglo-Analytic Approach: Hu-
manistic Contributions from Chinese Philosophy. Asian Studies 11, 3 (2023),
17–46.
[34] Suzanne Day and Stuart Rennie. 2023. Data science research in sub-Saharan
Africa: Ethical considerations in crowdsourcing for community engagement.
South African Journal of Science 119, 5/6 (May 2023). doi:10.17159/sajs.2023/
14911
[35] Rama Salla Dieng. 2023. Speaking out, talking back? African feminist politics
and decolonial poetics of knowing, organising and loving. Review of African
Political Economy ahead-of-print, ahead-of-print (2023). doi:10.1080/03056244.
2023.2284524
[36] Virginia Dignum. 2023. Responsible Artificial Intelligence: Recommendations and
Lessons Learned. Springer International Publishing, Cham, 195–214. doi:10.
1007/978-3-031-08215-3_9
[37] ECDPM. 2023. Interactive tool: Data policies in African countries. Retrieved
December 28, 2023 from https://ecdpm.org/work/interactive-tool-data-policies-
african-countries
[38] D Eke, P Ochang, A Adimula, F Borokini, S Akintoye, R Oloyede, L Sorborikor,
M Adeyeye, B Wale-Oshinowo, and T Ogundele. 2022. Responsible Data Gover-
nance in Africa: Institutional gaps and capacity needs. Centre for the Study of
African Economies (CSEA) Published: September (2022), 4.
[39] Damian Eke and George Ogoh. 2022. Forgotten African AI Narratives and the
future of AI in Africa. The International Review of Information Ethics 31, 1 (Aug.
2022). doi:10.29173/irie482
[40] Damian Okaibedi Eke, Schmidt Shilukobo Chintu, and Kutoma Wakunuma. 2023.
Towards Shaping the Future of Responsible AI in Africa. Springer International
Publishing, Cham, 169–193. doi:10.1007/978-3-031-08215-3_8
[41] Damian Okaibedi Eke, Kutoma Wakunuma, and Simisola Akintoye. 2023. Intro-
ducing Responsible AI in Africa. Springer International Publishing, Cham, 1–11.
doi:10.1007/978-3-031-08215-3_1
[42] Damian Okaibedi Eke, Kutoma Wakunuma, and Simisola Akintoye. 2023. Re-
sponsible AI in Africa: challenges and opportunities. Palgrave Macmillan (2023).
[43] Charles Ess. 2006. Ethical pluralism and global information ethics. Ethics and
Information Technology 8 (2006), 215–226.
[44] Cornelius Ewuoso. 2021. An African relational approach to healthcare and big
data challenges. Science and Engineering Ethics 27, 3 (2021), 34.
[45] Luciano Floridi, Josh Cowls, Monica Beltrametti, Raja Chatila, Patrice Chazerand,
Virginia Dignum, Christoph Luetge, Robert Madelin, Ugo Pagallo, Francesca
Rossi, et al. 2018. AI4People—an ethical framework for a good AI society:
opportunities, risks, principles, and recommendations. Minds and machines 28
(2018), 689–707.
[46] Luciano Floridi and Mariarosaria Taddeo. 2016.
What is data ethics?
20160360 pages.
[47] Ben Gansky and Sean McDonald. 2022. CounterFAccTual: How FAccT under-
mines its organizing principles. In Proceedings of the 2022 ACM Conference on

--- Page 12 ---

Preprint,
,
Barrett et al.
Fairness, Accountability, and Transparency. 1982–1992.
[48] Timnit Gebru and Émile P. Torres. 2024. The TESCREAL bundle: Eugenics and
the promise of utopia through artificial general intelligence. First Monday 29, 4
(Apr. 2024). doi:10.5210/fm.v29i4.13636
[49] Emmanuel R. Goffi. 2023. Teaching Ethics Applied to AI from a Cultural Standpoint:
What African “AI Ethics” for Africa? Springer International Publishing, Cham,
13–26. doi:10.1007/978-3-031-23035-6_2
[50] Geoff Gordon. 2022. Universalism. TMC Asser Institute for International &
European Law, Asser Research Paper 4 (Feb. 2022).
[51] Vusi Gumede. 2015. Exploring Thought Leadership, Thought Liberation and
Critical Consciousness for Africa’s Development. Africa Development / Afrique
et Développement 40, 4 (2015), 91–111. http://www.jstor.org/stable/90000045
[52] Arthur Gwagwa. 2019. Recommendations on the inclusion sub-Saharan Africa
in Global AI Ethics. RANITP Policy Brief 2 (2019). https://www.researchictafrica.
net/wp/wp-content/uploads/2020/11/RANITP2019-2-AI-Ethics.pdf
[53] Arthur Gwagwa, Emre Kazim, and Airlie Hilliard. 2022. The role of the African
value of Ubuntu in global AI inclusion discourse: A normative ethics perspective.
Patterns 3, 4 (2022).
[54] Kwame Gyekye. 2004. Person and community in African thought. In The African
Philosophy Reader. Routledge, 348–366.
[55] Dominique Habimana, Juvenal Ntambara, Francois Kambogo, Apolline Mukany-
onga, Jeanne d’Arc Mukarugomwa, Beatrice Uwayezu, Tharcisse Nzasingiz-
imana, and Jean Claude Nyirimanzi. 2018. Guidelines for Quality Assessment
of Administrative Data. (June 2018).
[56] Ciara Heavin and Yvonne O’Connor. 2024. Digital Ethics: Resolving “Wicked”
Problems and Dilemmas. (2024).
[57] Max Hort, Zhenpeng Chen, Jie M Zhang, Mark Harman, and Federica Sarro.
2024. Bias mitigation for machine learning classifiers: A comprehensive survey.
ACM Journal on Responsible Computing 1, 2 (2024), 1–52.
[58] Paulin J. Hountondji. 2004. Producing knowledge in Africa Today. In The
African Philosophy Reader. Routledge, 589–596.
[59] Maui Hudson, Stephanie Russo Carroll, Jane Anderson, Darrah Blackwater,
Felina M Cordova-Marks, Jewel Cummins, Dominique David-Chavez, Adam
Fernandez, Ibrahim Garba, Danielle Hiraldo, et al. 2023. Indigenous peoples’
rights in data: a contribution toward indigenous research sovereignty. Frontiers
in Research Metrics and Analytics 8 (2023), 1173805.
[60] AHMED ALI ILMI. 2014. CHAPTER EIGHT: Rethinking Development: An
Indigenous African Communal Approach. Counterpoints 443 (2014), 142–156.
http://www.jstor.org/stable/42982053
[61] Mujib Jimoh. 2023. The quest for information privacy in Africa: A critique of the
Makulilo-Yilma debate. African Journal on Privacy & Data Protection 1 (2023),
17.
[62] Anna Jobin, Marcello Ienca, and Effy Vayena. 2019. The global landscape of
AI ethics guidelines. Nature Machine Intelligence 1, 9 (Sept. 2019), 389–399.
doi:10.1038/s42256-019-0088-2
[63] Sokfa Francis John. 2021. Technology governance: Minding and closing the
gaps in Africa. African Journal of Governance and Development 10, 2 (2021),
375–389.
[64] Sountongnoma Martial Anicet Kiemde and Ahmed Dooguy Kora. 2022. Towards
an ethics of AI in Africa: rule of education. AI and Ethics 2, 1 (2022), 35–40.
[65] Lauren Klein and Catherine D’Ignazio. 2024. Data Feminism for AI. In The 2024
ACM Conference on Fairness, Accountability, and Transparency. ACM, Rio de
Janeiro Brazil, 100–112. doi:10.1145/3630106.3658543
[66] Sharon Kling, Shenuka Singh, Theresa L Burgess, and Gonasagrie Nair. 2023.
The role of an ethics advisory committee in data science research in sub-Saharan
Africa. South African Journal of Science 119, 5-6 (2023), 1–3.
[67] Dirk Kohnert. 2022. Machine ethics and African identities: Perspectives of
artificial intelligence in Africa. SSRN Electronic Journal (2022). doi:10.2139/ssrn.
4163096
[68] Lindah Kotut, Neelma Bhatti, Taha Hassan, Derek Haqq, and Morva Saaty.
2024. Griot-Style Methodology: Longitudinal Study of Navigating Design With
Unwritten Stories. In Proceedings of the 2024 CHI Conference on Human Factors
in Computing Systems (Honolulu, HI, USA) (CHI ’24). Association for Computing
Machinery, New York, NY, USA, Article 615, 14 pages. doi:10.1145/3613904.
3642682
[69] Joris Krijger, Tamara Thuis, Maarten de Ruiter, Emma Ligthart, and Indy Broek-
man. 2023. The AI ethics maturity model: a holistic approach to advancing
ethical data science in organizations. AI and Ethics 3, 2 (2023), 355–367.
[70] Simon K. Langat, Pascal M. Mwakio, and David Ayuku. 2020. How Africa
Should Engage Ubuntu Ethics and Artificial Intelligence. Journal of Public Health
International 2, 4 (Dec. 2020), 20–25. doi:10.14302/issn.2641-4538.jphi-20-3427
[71] Helen Lauer. 2017. African Philosophy and the Challenge of Science and Technol-
ogy. Palgrave Macmillan US, New York, 605–620. doi:10.1057/978-1-137-59291-
0_39
[72] Sabina Leonelli. 2016. Locating ethics in data science: responsibility and account-
ability in global and distributed knowledge production systems. Philosophical
Transactions of the Royal Society A: Mathematical, Physical and Engineering
Sciences 374, 2083 (2016), 20160122.
[73] Raymond Lovett, Vanessa Lee, Tahu Kukutai, Donna Cormack, Stephanie Carroll
Rainie, and Jennifer Walker. 2019. Good data practices for Indigenous data
sovereignty and governance. Good data (2019), 26–36.
[74] Jacob Emmanuel Mabe. 2007. Security Thought in Africa in the Context of
Global Ethics. The International Review of Information Ethics 7 (Sept. 2007),
209–215. doi:10.29173/irie23
[75] Ibbo Mandaza. 2004. Reconciliation and social justice in southern Africa: The
Zimbabwe experience. In The African Philosophy Reader. Routledge, 596–606.
[76] Thaddeus Metz. 2021. African Reasons Why AI Should Not Maximize Utility.
Springer International Publishing, Cham, 55–72. doi:10.1007/978-3-030-70550-
3_4
[77] Sábëlo Mhlambi. 2020. From Rationality to Relationality: Ubuntu as an Ethical
and Human Rights Framework for Artificial Intelligence Governance. Carr
Center for Human Rights Policy (2020).
[78] Sábëlo Mhlambi and Simona Tiribelli. 2023. Decolonizing AI Ethics: Relational
Autonomy as a Means to Counter AI Harms. Topoi 42, 3 (July 2023), 867–880.
doi:10.1007/s11245-022-09874-2
[79] Kgomotso H Moahi. 2007. Globalization, Knowledge Economy and the implica-
tion for Indigenous Knowledge. The International Review of Information Ethics 7
(Sept. 2007), 55–62. doi:10.29173/irie13
[80] Thema Monroe-White. 2021. Emancipatory Data Science: A Liberatory Frame-
work for Mitigating Data Harms and Fostering Social Transformation. In Pro-
ceedings of the 2021 Computers and People Research Conference (Virtual Event,
Germany) (SIGMIS-CPR ’21). Association for Computing Machinery, New York,
NY, USA, 23–30. doi:10.1145/3458026.3462161
[81] Ariel Antonio Morán-Reyes. 2022. Towards an ethical framework about Big
Data era: metaethical, normative ethical and hermeneutical approaches. Heliyon
8, 2 (2022).
[82] Hani Morgan. 2022. Conducting a qualitative document analysis. The Qualitative
Report 27, 1 (2022), 64–77.
[83] Luke Munn. 2023. The uselessness of AI ethics. AI and Ethics 3, 3 (2023),
869–877.
[84] Amber Murrey and Patricia Daley. 2023. Beyond Tokenism: Pluriversals and
Decolonizing Solidarity for Thriving and Dignified Futures (1 ed.). Pluto Press,
203–227. http://www.jstor.org/stable/jj.5938918.12
[85] Clarisse Y Ndjungu. 2020. Blood Minerals and the Curse: The Invisible Hand,
State Failure, War and Mining in the Democratic Republic of the Congo. Ph. D.
Dissertation. Howard University.
[86] Sabelo J. Ndlovu-Gatsheni. 2015. Genealogies of Coloniality and Implications
for Africa’s Development. Africa Development / Afrique et Développement 40, 3
(2015), 13–40. http://www.jstor.org/stable/afrdevafrdev.40.3.13
[87] Safiya Noble. 2018. Algorithms of Oppression: How Search Engines Reinforce
Racism. NYU Press, USA.
[88] T Uzodinma Nwala. 1985. Igbo philosophy. (1985).
[89] Ezinne Nwankwo and Belona Sonna. 2019. Africa’s social contract with AI.
XRDS: Crossroads, The ACM Magazine for Students 26, 2 (2019), 44–48.
[90] Chinwe MA Nwoye. 2011. Igbo cultural and religious worldview: An insider’s
perspective. International Journal of Sociology and anthropology 3, 9 (2011),
304–317.
[91] Julius K Nyerere. 1962. " Ujamaa": The Basis of African Socialism. Tanganyika
Standard Limited Dar-es-Salaam.
[92] Chinasa T. Okolo. 2024. Operationalizing Comprehensive Data Governance in
Africa. African Journal of Sustainable Development (2024), 200–214.
[93] Chinasa T. Okolo, Kehinde Aruleba, and George Obaido. 2023. Responsible AI in
Africa—Challenges and Opportunities. Springer International Publishing, Cham,
35–64. doi:10.1007/978-3-031-08215-3_3
[94] Beatrice Okyere-Manu. 2023. The place of the African relational and moral
theory of Ubuntu in the global artificial intelligence and big data discussion:
critical reflections. In Elgar Companion to Regulating AI and Big Data in Emerging
Economies. Edward Elgar Publishing, 99–114.
[95] Helen Titilola Olojede. 2023. Towards African Artificial Intelligence Ethical
Principles. In 2023 First International Conference on the Advancements of Artificial
Intelligence in African Context (AAIAC). IEEE, 1–6.
[96] Eghosa E. Osaghae. 2004. Rescuing the post-colonial state of Africa: A recon-
ceptualization of the role of the civil society. In The African Philosophy Reader.
Routledge, 606–619.
[97] Sone Osakwe and Adedeji Peter Adeniran. 2021. Strengthening data governance
in Africa. (2021).
[98] Clifford Owusu-Gyamfi. 2019. Onipa:: The Human Being and the Being of
Human Among the Akan people of West Africa. Towards an African Theological
Anthropology. Trinity Postgraduate Review Journal 18, 1 (2019), 74–94.
[99] Olatunji A Oyeshile. 2021. Yoruba philosophy of existence, iwa (character)
and contemporary socio-political order. Philosophia: International Journal of
Philosophy 22, 1 (2021), 1–18.
[100] Oritsegbubemi Anthony Oyowe. 2014. An African Conception of Human Rights?
Comments on the Challenges of Relativism. Human Rights Review 15, 3 (Sept.
2014), 329–347. doi:10.1007/s12142-013-0302-2

--- Page 13 ---

African Data Ethics: A Discursive Framework for Black Decolonial Data Science
Preprint,
,
[101] Paul Plantinga, Kristophina Shilongo, Oarabile Mudongo, Angelique Umubyeyi,
Michael Gastrow, and Gabriella Razzano. 2024. Responsible artificial intelligence
in africa: Towards policy learning. Data & Policy 6 (2024), e72.
[102] Stephanie Carroll Rainie, Tahu Kukutai, Maggie Walter, Oscar Luis Figueroa-
Rodríguez, Jennifer Walker, and Per Axelsson. 2019. Indigenous data sovereignty.
(2019).
[103] Mogobe B. Ramose. 2004. The ethics of ubuntu. In The African Philosophy
Reader. Routledge, 379–387.
[104] Mogobe B. Ramose. 2004. The struggle for reason in Africa. In The African
Philosophy Reader. Routledge, 1–9.
[105] Amana Raquib, Bilal Channa, Talat Zubair, and Junaid Qadir. 2022. Islamic
virtue-based ethics for artificial intelligence. Discover Artificial Intelligence 2, 1
(2022), 11.
[106] Shaniah Reece, Covenant Adenuga, Tierra Ablorh, and Yolanda A. Rankin. 2025.
A Powerful Sisterhood: Black Women Scholars in Feminist HCI. Interactions 32,
1 (Jan. 2025), 44–47. doi:10.1145/3705739
[107] Urbano Reviglio and Rogers Alunge. 2020. “I am datafied because we are
datafied”: An Ubuntu perspective on (relational) privacy. Philosophy & Technol-
ogy 33, 4 (2020), 595–612.
[108] Mohammad Rashidujjaman Rifat, Ayesha Bhimdiwala, Ananya Bhattacharjee,
Amna Batool, Dipto Das, Nusrat Jahan Mim, Abdullah Hasan Safir, Sharifa
Sultana, Taslima Akter, C Estelle Smith, et al. 2023. Many Worlds of Ethics:
Ethical Pluralism in CSCW. In Companion Publication of the 2023 Conference on
Computer Supported Cooperative Work and Social Computing. 490–496.
[109] Walter Rodney. 1982. How Europe Underdeveloped Africa. Howard University
Press.
[110] Emma Ruttkamp-Bloem. 2023. Epistemic Just and Dynamic AI Ethics in Africa.
Springer International Publishing, Cham, 13–34. doi:10.1007/978-3-031-08215-
3_2
[111] Muhammad Sadi Adamu. 2021. Rethinking Technology Design and Deployment
in Africa: Lessons from an African Standpoint. In Proceedings of the 3rd African
Human-Computer Interaction Conference: Inclusiveness and Empowerment (Ma-
puto, Mozambique) (AfriCHI ’21). Association for Computing Machinery, New
York, NY, USA, 75–83. doi:10.1145/3448696.3448704
[112] Raymond Scupin. 2008.
The KJ Method: A Technique for Analyz-
ing Data Derived from Japanese Ethnology.
Human Organization
56,
2
(01
2008),
233–237.
doi:10.17730/humo.56.2.x335923511444655
arXiv:https://meridian.allenpress.com/human-organization/article-
pdf/56/2/233/1726606/humo_56_2_x335923511444655.pdf
[113] Samuel T. Segun. 2021. Critically engaging the ethics of AI for a global audience.
Ethics and Information Technology 23, 2 (June 2021), 99–105. doi:10.1007/s10676-
020-09570-y
[114] Shilongo, Kristophina and Peter, Kaulyaalalwa. 2023. Creativity, innovation, and
open data: Fostering inclusive growth in Africa. Grappa Marketing Editorial 15,
4 (Dec. 2023). https://cetic.br/media/docs/publicacoes/6/20240201125420/year-
xv-n-4-data-collaboratives-and-data-sharing.pdf
[115] Amber Sinha and Bobina Zulfa. 2023. Principles of Afro-Feminist AI Data: Visions
of Afro-feminist Emancipatory, Liberatory AI. Pollicy.
[116] Philip Smith and Karl Ricanek. 2020. Mitigating algorithmic bias: Evolving an
augmentation policy that is non-biasing. In Proceedings of the IEEE/CVF Winter
Conference on Applications of Computer Vision Workshops. 90–97.
[117] Linnet Taylor and Nadezhda Purtova. 2019. What is responsible and sustainable
data science? Big Data & Society 6, 2 (2019), 2053951719858114.
[118] African Union. 2020. African Union Convention on Cyber Security and Personal
Data Protection. https://au.int/sites/default/files/documents/44004-doc-EN-
_Continental_AI_Strategy_July_2024.pdf
[119] Michael Maduawuchi Uzomah, Philip Osarobu Isanbor, and Chinyere Scholas-
tica Uzomah. 2023. African tech development: The ideal and summit of con-
temporary African philosophy and literary studies. African Social Science and
Humanities Journal 4, 1 (Feb. 2023), 23–36. doi:10.57040/asshj.v4i1.351
[120] Stefaan G Verhulst. 2021. Reimagining data responsibility: 10 new approaches
toward a culture of trust in re-using data to address critical public needs. Data
& Policy 3 (2021), e6.
[121] Maggie Walter, Raymond Lovett, Bobby Maher, Bhiamie Williamson, Jacob
Prehn, Gawaian Bodkin-Andrews, and Vanessa Lee. 2021. Indigenous data
sovereignty in the era of big data and open data. Australian Journal of Social
Issues 56, 2 (2021), 143–156.
[122] Guanchu Wang, Mengnan Du, Ninghao Liu, Na Zou, and Xia Hu. 2023. Mitigat-
ing algorithmic bias with limited annotations. In Joint European Conference on
Machine Learning and Knowledge Discovery in Databases. Springer, 241–258.
[123] C. S. Wareham. 2021.
Artificial intelligence and African conceptions of
personhood. Ethics and Information Technology 23, 2 (June 2021), 127–136.
doi:10.1007/s10676-020-09541-3
[124] Ajume Wingo. 2006. Akan philosophy of the person. Stanford Encyclopedia of
Philosophy (2006).
[125] Kwasi Wiredu. 2004. An Akan perspective on human rights. In The African
Philosophy Reader. Routledge, 366–379.
[126] Kwasi Wiredu. 2004. The moral foundations of an African culture. In The
African Philosophy Reader. Routledge, 337–348.
[127] Quey-Jen Yeh and Xiaojun Xu. 2010. The effect of Confucian work ethics on
learning about science and technology knowledge and morality. Journal of
business ethics 95 (2010), 111–128.
[128] Ammar Younas and Yi Zeng. 2024. Proposing Central Asian AI ethics principles:
a multilevel approach for responsible AI. AI and Ethics (June 2024). doi:10.1007/
s43681-024-00505-7
A
PRISMA Diagram of Document Collection
To supplement the description of the data collection process in
Methods section, the following PRISMA diagram illustrates the
corpus-building process including the identification, screening and
inclusion stages.
Figure 1: PRISMA diagram of document collection process
for African data ethics corpus.
B
African Data Ethics Framework Case Studies
The following section presents six case studies from the African
data ethics corpus to further contextualize our framework with real
world examples from data science work in the African context.
B.1
Challenge Power Asymmetries Case Study:
DRC Mineral Extraction
The violent exploitation of miners in the Democratic Republic of
Congo (DRC) is a harrowing example of how unchecked power
from the West and within Africa corrupts the data science ecosys-
tem. The DRC is home to an abundance of minerals necessary
for data science. Specifically, cobalt and silicon are foundational
components of all technology, especially the vast number of com-
puters that store and process data in global data centers [85]. To
keep up with computing demand, multinational companies collect
a copious amount of minerals from the DRC with feigned igno-
rance of the unsafe working conditions, the prevalence of child
labor, and the inhumane actions of the rebel groups who often
control mining operations. Silicon and cobalt are often referred to
as “blood minerals” because Western companies are able to make
billions of dollars from the technology industry while the DRC
continues to experience violent internal displacement, ineffective
interventions, and a minuscule fraction of the value of their min-
ing labor [85]. The extractive relationship between the Congolese

--- Page 14 ---

Preprint,
,
Barrett et al.
and large Western companies has direct parallels to DRC’s colo-
nial relationship with Belgium [85]. The monarch of Belgium, King
Leopold, violently claimed DRC to extract and sell raw materials
so Belgium could be a major player in meeting the material de-
mands of an industrializing Europe without any concern for the
humanity of the Congolese people. This colonial relationship is fur-
thered by African leaders who have assumed the role of middlemen
in the mineral trade. Dodd-Frank Section 1502 is a United States
law passed to address dehumanizing mining labor practices [85].
This law required companies to execute due diligence measures to
ensure they were not selling DRC minerals mined from conflict.
Rather than adhering to this law, multinational companies pulled
out of direct agreements with the DRC and joined new partnerships
with neighboring countries such as Rwanda. These countries then
acted as middlemen, buying conflict minerals from the DRC and
selling them to multinational companies, allowing the companies
to legally distance themselves from the exploitative sourcing[85].
Understanding the colonial and modern-day political background
of DRC blood minerals is key to contextualizing calls for reduc-
ing the scale of datasets and demand for new technology 4. Every
leader within the data science ecosystem has the responsibility to
challenge and not perpetuate colonial and asymmetric power.
B.2
Assert Data Self-Determination Case Study:
The Promise of African-led Data Science
Masakhane is an African natural language processing (NLP) collec-
tive that builds language datasets and models in Indigenous African
languages. By all reports across documents, Masakhane practices all
the principles proposed in this framework and especially upholds
the major principle of Data Self-Determination [25, 42, 114].They
uphold these principles with a commitment to centering African
values as their founding principles, working with existing public
datasets to not infringe on data privacy, and building language
datasets to preserve indigenous African languages for the future to
come [4]. Masakhane also has a very welcoming and communal or-
ganizational structure that includes any interested party in weekly
meetings and communications. Once a member wants to contribute
to a Masakhane project, they must undergo in-house training to
maintain quality of the their dataset and model. They also explicitly
prohibit “parachute research from the Global North” to ensure the
time and resources of their collective provide direct benefit to their
communities.5 Finally, every project plan includes a discussion of
data privacy considerations to guide their work. While there are
many other parts to Masakhane’s work, the practices described in
their public documents demonstrate an African data science com-
munity that is closely aligned with the perspectives represented
in our framework. Masakhane is part of the growing grassroots
efforts to imagine and practice what African-led responsible data
science can achieve.
4https://newint.org/violence/2024/its-time-hold-big-tech-accountable-violence-drc
5https://www.masakhane.io/
B.3
Invest in Local Data Institutions &
Infrastructures Case Study: Building the
Capacity of National Statistical Offices
As a formal data collective, the National Institute of Statistics of
Rwanda (NISR) developed a report to guide their management
procedures for administrative data [55]. Their report recognizes
the data sharing network they are a part of, raises concerns with
data quality specific to Rwanda, and proposes new administrative
standards for assessing data quality. While the authors recognize
that their data management infrastructures need to progress, they
view collaborations between local data practitioners as the key to
development. Development collaborations include technical work-
shops, conferences, dissemination of data quality frameworks, and
supporting staff in their respective data work [55]. African data
scientists are eager to develop their communities’ capacity to man-
age data science projects. Organizations such as NISR recognize
that this development requires a comprehensive assessment of the
status quo, supportive collaboration, and incremental development
of data standards.
B.4
Utilize Communalist Practices Case Study:
Challenging Utilitarian Data Ethics with a
Communitarian Analysis
Another aspect of practicing communalism in data science is ap-
plying communitarian theories as a lens for evaluating data ethics.
The Western concept of utilitarianism is a predominant paradigm
in data ethics. Utilitarian data science aims to construct AI and
other DDT that maximize the amount of social good and minimize
the amount of social harm at scale (see effective altruists). African
communitarian theories provide novel and strong critiques of utili-
tarian data ethics as well. One African data ethicist, in particular,
applies African values to outline why utilitarianism: 1) trivializes
human dignity through rationality, 2) justifies the suppression of
non-dominant people and values, 3) ignores the role relationality
plays in human-AI interaction, and 4) misinterprets the nature of
self-sacrifice [76]. Respectful debate with diverging perspectives is
essential to the progress of responsible data science.
B.5
Center Communities on the Margins Case
Study: Limits of Inclusive Representation in
African Facial Recognition Technology
African people, and Black people in general, are severely under-
represented in facial recognition datasets, and this has led to a
performance bias against Black users. African technology compa-
nies committed to addressing this bias so their primarily African
users could rely on their products. For example, a women-led facial
recognition start-up called BACE curated a diverse dataset from the
local community so their system could better detect Black subjects
[42]. Users upload photos of their IDs and short videos from their
phones to confirm their identity 6. The technology was created to
aid financial fraud investigation efforts in Ghana that are hampered
by many citizens not having formal identification documents 7.
6https://www.bacegroup.com/
7https://www.thehabarinetwork.com/meet-charlette-nguessan-she-and-her-team-
have-innovated-facial-recognition-technology-designed-to-identify-black-africans

--- Page 15 ---

African Data Ethics: A Discursive Framework for Black Decolonial Data Science
Preprint,
,
While at face value BACE is practicing community-engaged work,
the principles described above call for more meaningful community
involvement. Data representation is only one stage of the data sci-
ence lifecycle that communities should be involved in. BACE was
meeting the needs of financial institutions but did the team gauge
if the local community was comfortable with this identification
product [14]? To center all communities in responsible data science,
local communities should be involved in the ideation, creation, de-
ployment, and maintenance of data-driven technology to build trust
and buy-in for new technology [93]. The work of N’Guessan is very
aligned with the principles of data self-determination & infrastruc-
tures because it was in indigenous effort to build a DDT for their
local Black community. While this case study is seemingly doing
everything “right” facial recognition is still used for surveillance
and has performance issues for marginalized communities [14].
B.6
Uphold Common Good: International
Partnership to Increase Access to COVID-19
Information
At the beginning of the COVID-19 pandemic, the Rwandan gov-
ernment partnered with the German technology company GIZ
to develop a chatbot for remote communities to access tailored
COVID-19 information and guidance [67]. To meet the needs of
Rwandan users, the chatbot can communicate in the local language
of Kinyarwanda; the medical advice is based on the Rwandan medi-
cal databases, and the project is open source 8. Beyond the features
of the product, both organizations worked together to develop
Rwanda’s technical infrastructure to not only host the chatbot soft-
ware but also maintain local technologies in the future 9. The RBC
chatbot is the product of an equitable partnership of African and
Western data organizations that were committed to promoting the
well-being of their community in the face of a catastrophic pan-
demic that impacted the world. The collaboration was successful
because their decisions were attuned to each stakeholder’s capabil-
ities and limitations [67]. By all accounts, this is an example of a
harmonious, dignified, and socially good data science practice.
C
Comparative Analysis Table
As a supplement to the discussion’s comparative analysis, the fol-
lowing table shows the coding of minor African data ethics princi-
ples to each of the seven particularist frameworks.
8https://github.com/Digital-Umuganda/Mbaza-chatbot
9https://www.giz.de/en/workingwithgiz/KI-Ruanda-Digitalisierung.html

--- Page 16 ---

Preprint,
,
Barrett et al.
Figure 2: A table of minor African data ethics principles on the y-axis and seven comparison papers on the x-axis ([24, 45, 62,
65, 80, 105, 128]. Between these axes a check mark indicates a principle is covered by the compared framework.

```
