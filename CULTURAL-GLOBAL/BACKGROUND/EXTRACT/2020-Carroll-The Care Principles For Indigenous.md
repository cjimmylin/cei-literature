# 2020-Carroll-The Care Principles For Indigenous

**Source:** 2020-Carroll-The Care Principles For Indigenous.pdf
**Pages:** 13
**Extracted:** 2026-04-03

---

## Page 1

Edinburgh Research Explorer 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
The CARE principles for Indigenous data governance
Citation for published version:
Carroll, S, Garba, I, Figueroa-Rodriguez, O, Holbrook, J, Lovett, R, Materechera, S, Parsons, M, Raseroka,
K, Rodriguez-Lonebear, D, Rowe, R, Sara, R, Walker, J, Anderson, J & Hudson, M 2020, 'The CARE
principles for Indigenous data governance', Data Science Journal, vol. 19. https://doi.org/10.5334/dsj-2020-
043
Digital Object Identifier (DOI):
10.5334/dsj-2020-043
Link:
Link to publication record in Edinburgh Research Explorer
Document Version:
Publisher's PDF, also known as Version of record
Published In:
Data Science Journal
General rights
Copyright for the publications made accessible via the Edinburgh Research Explorer is retained by the author(s)
and / or other copyright owners and it is a condition of accessing these publications that users recognise and
abide by the legal requirements associated with these rights.
Take down policy
The University of Edinburgh has made every reasonable effort to ensure that Edinburgh Research Explorer
content complies with UK legislation. If you believe that the public display of this file breaches copyright please
contact openaccess@ed.ac.uk providing details, and we will remove access to the work immediately and
investigate your claim.
Download date: 23. Jul. 2021

## Page 2

Carroll, SR, et al. 2020. The CARE Principles for Indigenous 
Data Governance. Data Science Journal, 19: 43, pp. 1–12. 
DOI: https://doi.org/10.5334/dsj-2020-043
PRACTICE PAPER
The CARE Principles for Indigenous Data 
Governance
Stephanie Russo Carroll1, Ibrahim Garba1, Oscar L. Figueroa-Rodríguez2, 
Jarita Holbrook3, Raymond Lovett4, Simeon Materechera5, Mark Parsons6, 
Kay Raseroka7, Desi Rodriguez-Lonebear8, Robyn Rowe9, Rodrigo Sara10, 
Jennifer D. Walker9, Jane Anderson11 and Maui Hudson12
1	University of Arizona, US
2	COLPOS, Campus Montecillo, MX
3	University of Western Cape, ZA
4	Australian National University, AU
5	North West University, ZA
6	Rensselaer Polytechnic Institute, US
7	Joint Minds Consult, BW
8	University of California, Los Angeles, US
9	Laurentian University, CA
10	One Planet Solutions, FR
11	New York University, US
12	University of Waikato, NZ
Corresponding author: Stephanie Russo Carroll (stephaniecarroll@email.arizona.edu)
Concerns about secondary use of data and limited opportunities for benefit-sharing have focused 
attention on the tension that Indigenous communities feel between (1) protecting Indigenous 
rights and interests in Indigenous data (including traditional knowledges) and (2) ­supporting 
open data, machine learning, broad data sharing, and big data initiatives. The International 
Indigenous Data Sovereignty Interest Group (within the Research Data Alliance) is a network 
of nation-state based Indigenous data sovereignty networks and individuals that developed the 
‘CARE Principles for Indigenous Data Governance’ (Collective Benefit, Authority to Control, 
Responsibility, and Ethics) in consultation with Indigenous Peoples, scholars, non-profit organi­
zations, and governments. The CARE Principles are people– and purpose-oriented, reflecting the 
crucial role of data in advancing innovation, governance, and self-determination among Indig­
enous Peoples. The Principles complement the existing data-centric approach represented in 
the ‘FAIR Guiding Principles for scientific data management and stewardship’ (Findable, Acces­
sible, Interoperable, Reusable). The CARE Principles build upon earlier work by the Te Mana 
Raraunga Maori Data Sovereignty Network, US Indigenous Data Sovereignty Network, Maiam 
nayri Wingara Aboriginal and Torres Strait Islander Data Sovereignty Collective, and numerous 
Indigenous Peoples, nations, and communities. The goal is that stewards and other users of 
Indigenous data will ‘Be FAIR and CARE.’ In this first formal publication of the CARE Principles, 
we articulate their rationale, describe their relation to the FAIR Principles, and present exam­
ples of their application.
Keywords: Indigenous; data sovereignty; data governance; data principles; FAIR principles
Introduction
As the world engages with open data, big data, data reuse, and open science, data have increasingly become 
a global resource used for wielding power, making decisions, spurring innovation and discovery, and com­
mercialization (Independent Expert Advisory Group 2014, The Economist 2017). The effects of this shift are

## Page 3

Carroll et al: The CARE Principles for Indigenous Data Governance
Art. 43, page 2 of 12  
amplified by the adoption of artificial intelligence technologies and the increasing convergence of biological 
and digital worlds facilitated through data sharing platforms. Historically plagued by data inequities and 
data exploitation, Indigenous Peoples have raised concerns about the need to integrate Indigenous knowl­
edges and approaches into data practices and policies as both the volume and opportunities for secondary 
use of data increase (Jackson et al. 2019; Kukutai & Cormack 2019; Carroll et al. 2019; Garrison et al. 2019; 
Rainie et al. 2019; Kukutai & Taylor 2016b). The articulation of Indigenous Peoples’ rights and interests in 
data about their peoples, communities, cultures, and territories is part of reclaiming control of data, data 
ecosystems, data science, and data narratives in the context of open data and open science. Control, coupled 
with a focus on collective benefit and equity, repositions Indigenous Peoples, nations, and communities 
from being subjects of data that perpetuate unequal power distributions to self-determining users of data 
for development and wellbeing. Harnessing data for governance and acting in the governance of data, shifts 
Indigenous Peoples from invisibility within data ecosystems to vibrant contributors to data policies, prac­
tices, ethics, and innovation.
Leveraging Indigenous Rights for Indigenous Data Futures
Background
Global Indigenous presence spans over 90 countries and includes over 370 million Indigenous persons living 
out more than 5,000 distinct cultures (UN 2009). Indigenous Peoples have continuity with their pre-colonial 
societies and seek to use their own social, political, and economic systems to preserve, develop, and trans­
mit to future generations their cultures, knowledges, and relationships with their territories and resources 
(Martinez Cobo 1982). While often limited by settler-colonial oppression and definition, Indigenous Peoples 
retain their rights to self-determine their forms of collective governance and rules of membership.
In the contemporary world, Indigenous Peoples and nations, people, and communities have become 
actors across global societies. Indigenous Peoples and their nations are the rightsholders as affirmed by the 
United Nations and nation-state legal recognition of Indigenous sovereignty (Echo-Hawk 2013; UN 2007; 
Anaya 2004). Indigenous Peoples as sovereign political collectives often participate in supra- and inter-
tribal organizations such as the Oceti Sakowin Oyate and the Iwi Chairs’ Forum, and have local or regional 
sub-systems such as Tohono O’Odham districts in the US and the Federation of Victorian Traditional Owner 
Corporations in Australia. Indigenous people often live as citizens of nations (Indigenous) within nations 
(the nation state, e.g., the United States). Indigenous people also participate in other Indigenous stakeholder 
groups that do not hold inherent sovereignty, including daily life within Indigenous communities (groups of 
individuals) within their nations or mainstream society and interaction with Indigenous organizations such 
as health care entities, non-profits, and businesses. 
Ongoing processes of colonization of Indigenous Peoples and globalization of Western ideas, values, 
and lifestyles have resulted in epistemicide, the suppression and co-optation of Indigenous knowledges 
and data systems (Carroll, Rodriguez-Lonebear & Martinez 2019; Kukutai & Taylor 2016a; Kukutai & Walter 
2015; Smith 2012). These processes have limited the ability of Indigenous Peoples to recover, develop, and 
sustain their knowledges, an ability that is central to Indigenous Peoples’ capacity to realize their human 
rights and fulfil their responsibilities (Wilson, 2004; Ratima 2001). 
Alongside Indigenous aspirations for self-determination, social justice movements have promoted the 
importance of equity within society and become more deliberate about addressing the negative effects of 
unconscious bias and structural racism. The pervasiveness of bias across data ecosystems (digital infrastruc­
tures, analytics, and applications), within sub-systems (regions/platforms), as well as institutions and com­
munities indicate the importance of addressing inequities at multiple levels. Indigenous people recognize 
and already incorporate this multi-scale complexity in their knowledge systems and activities; however, this 
may not be the case for other communities of practice, or knowledge systems. 
The Emergence of Indigenous Data Sovereignty
Since the 1970s, there has been a resurgence in discourse around Indigenous knowledges, identities, and 
rights, culminating in the 2007 United Nations Declaration on the Rights of Indigenous Peoples [UNDRIP] 
(UN 2007). UNDRIP reaffirms Indigenous Peoples’ rights to self-determination as political entities and hon­
ors the principle of Indigenous control over Indigenous data (Tsosie 2019; Davis 2016). The rights articulated 
in UNDRIP (especially Article 31) also reflect discourse around Indigenous Cultural and Intellectual Property 
Rights (ICIP) and Indigenous research ethics (Mātaatua Declaration 1993; Julayinbul Statement 1993; Janke 
1998, 2004; Drugge 2016; Tsosie 1997, 2019; Anderson 2009, 2015). UNDRIP reflects a broad approach to

## Page 4

Carroll et al: The CARE Principles for Indigenous Data Governance
Art. 43, page 3 of 12
Indigenous data that is not restricted by mainstream conceptions of knowledge and intellectual property 
(Posey & Dutfield, 1996).
Indigenous Peoples’ data include data generated by Indigenous Peoples, as well as by governments and other 
institutions, on and about Indigenous Peoples and territories. As well as information about Indigenous com­
munities and the individuals, Indigenous and non-Indigenous, that live within (Carroll, ­Rodriguez-Lonebear 
& Martinez 2019; Rainie et al. 2019; MnW 2018; Nickerson 2017; TMR 2016). Indigenous Peoples’ data 
­comprise (1) information and knowledge about the environment, lands, skies, resources, and non-humans 
with which they have relations; (2) information about Indigenous persons such as administrative, census, 
health, social, commercial, and corporate and, (3) information and knowledge about Indigenous Peoples 
as collectives, including traditional and cultural information, oral histories, ancestral and clan knowledge, 
cultural sites, and stories, belongings.
The advancement of Indigenous self-determination and the reclamation of Indigenous identity and 
knowledges over the past 50 years has led to the emergence of Indigenous Data Sovereignty, an assertion 
of the rights and interests of Indigenous Peoples in relation to data about them, their territories, and their 
ways of life (Carroll, Rodriguez-Lonebear & Martinez 2019; Rainie et al. 2017; Kukutai & Taylor 2016a; 
Snipp 2016). Indigenous Data Sovereignty has become an increasingly relevant topic as big data, open 
data, open science, and data reuse become an integral part of research and institutional practices (Carroll, 
Rodriguez-Lonebear & Martinez 2019; Lovett et al. 2019; Rainie et al. 2019; Kukutai & Taylor 2016a; Taylor 
& Kukutai 2015). Given that most Indigenous data are held by non-Indigenous governments, institutions, 
and agencies, increasing Indigenous Peoples’ participation in data governance activities is central to realiz­
ing Indigenous Data Sovereignty (Carroll, Rodriguez-Lonebear & Martinez 2019; Rainie et al. 2019; Kukutai 
& Taylor 2016b; Rodriguez-Lonebear 2016; Smith 2016; Snipp 2016). Indigenous data governance includes 
both the stewardship and the processes necessary to implement Indigenous control over Indigenous 
data (collection, storage, analysis, use, reuse) (Carroll, Rodriguez-Lonebear & Martinez 2019; Rainie et al. 
2019; Walter 2018; Rodriguez-Lonebear 2016; Smith 2016). The development of conceptual frameworks 
to inform processes for stewardship and control of Indigenous data has been ongoing in areas such as 
­science, research methods, and research governance (Cajete, 2000; Wilson, 2008; Kovach, 2009; McGregor, 
Restoule & Johnston, 2018). There is a need to apply insights generated from these frameworks within data 
ecosystems to help address the challenge of producing data that reflect Indigenous Peoples’ interests and 
governance needs. 
The Care Principles
Rationale 
Mainstream values related to research and data are often inconsistent with Indigenous cultures and collec­
tive rights. For instance, data historically belonged to the researcher in mainstream settings, a notion that 
has shifted under open data and open science movements where publicly funded research requires data 
sharing. Meanwhile, Indigenous worldviews have typically centered ‘people’ and ‘purpose’ through govern­
ance processes that emphasize collective ownership and control of data (Carroll, Rodriguez-Lonebear & 
Martinez 2019; Kukutai & Taylor 2016b; Smith 2016; Snipp 2016). Indigenous Peoples have been working 
on ways to authenticate Indigenous forms of knowledge and to fortify their rights to govern research and 
resulting data (Garrison et al. 2019; Hudson et al. 2016; Smith 2012).
Drawing on the First Nations principles of OCAP® that created data standards for Ownership, Control, 
Access, and Possession in Canada in the 1990s (FNIGC 2019), Indigenous Data Sovereignty networks in 
Aotearoa New Zealand, Australia, and the United States, as well as Indigenous scholars, leaders, and allies, 
determined that there was an urgent need to develop global principles for the governance of Indigenous 
data. Underlying this need were the primary goals of (1) fostering Indigenous self-determination by enhanc­
ing Indigenous use of data for Indigenous pursuits and (2) honoring the ‘FAIR Guiding Principles for ­scientific 
data management and stewardship’ (Findable, Accessible, Interoperable, Reusable) (Wilkinson et al. 2016), 
while ensuring data sharing on Indigenous terms. 
The ‘CARE Principles for Indigenous Data Governance’ (Collective Benefit, Authority to Control, 
Responsibility, and Ethics) (RDA IG 2019) empower Indigenous Peoples by shifting the focus from regulated 
consultation to value-based relationships that position data approaches within Indigenous cultures and 
knowledge systems to the benefit of Indigenous Peoples (Castellano 2004; Anderson et al. 2003). This shift 
ultimately promotes equitable participation in processes of data reuse, which will result in more equitable 
outcomes.

## Page 5

Carroll et al: The CARE Principles for Indigenous Data Governance
Art. 43, page 4 of 12  
Development
Academics and practitioners in the International Indigenous Data Sovereignty Interest Group within the 
Research Data Alliance (RDA 2017) acknowledged the tension between protecting Indigenous rights and 
interests in data and supporting open data. With this challenge in mind, a workshop was held in Gaborone, 
Botswana, on Indigenous Data Sovereignty as part of International Data Week in 2018. This Indigenous-led 
workshop convened Indigenous and allied academics and practitioners to draft principles for Indigenous 
data governance. Workshop organizers prepared an analysis of principles from frameworks issued by Indig­
enous Data Sovereignty and governance networks, as well as by mainstream sources, to inform dialogue 
(Table 1). 
Participants concluded that existing frameworks were oriented toward data, people, and purpose (see 
Figure 1). While both Indigenous and mainstream principles identified data-centric principles (such as 
those named in the FAIR Principles), the Indigenous frameworks emphasized people- and purpose-oriented 
principles. 
Table 1: Key Documents Contributing to the Development of the CARE Principles.
Principles of Māori Data Sovereignty
(TMR 2018)
Indigenous Data Sovereignty Communique 
(MnW 2018)
United States Indigenous Data Sovereignty Network Indigenous Data Governance Principles
(USIDSN 2020) 
OCAP®: Ownership, Control, Access, and Possession
(FNIGC 2018)
Principles of Ethical Métis Research 
(MC 2011)
National Inuit Strategy on Research
(ITK 2018)
Open Data Charter Principles
(ODC 2015)
FAIR Guiding Principles for scientific data management and stewardship 
(Wilkinson et al. 2016)
STREAM properties for industrial and commoditized data
(Demchenko et al. 2018)
Figure 1: Indigenous and Mainstream Data Principles, and Orientation toward Data, People, and Purpose.

## Page 6

Carroll et al: The CARE Principles for Indigenous Data Governance
Art. 43, page 5 of 12
Workshop participants felt that the mainstream frameworks adequately covered data-centric principles 
and focused their attention on the ‘people’ and ‘purpose’ foci of the Indigenous principles to create the CARE 
Principles. Once the four primary CARE Principles of Collective benefit, Authority to control, Responsibility, 
and Ethics were identified, participants broke into small groups to outline and draft the language for both 
primary and sub-principles. The resulting draft was shared among nation-state based network members, 
Indigenous leaders, Indigenous scholars, and allies for input (edits, revisions, comments, feedback) via elec­
tronic media, presentations, and engagements. 
The CARE Principles are designed to complement the FAIR Principles and guide the inclusion of Indigenous 
Peoples in data processes that strengthen Indigenous control for improved discovery, access, use, reuse, and 
attribution in contemporary data landscapes. 
Exposition 
The CARE Principles address important considerations for modern data ecosystems and across data lifecycles 
that support both innovation and Indigenous self-determination (Figure 2). The Principles describe high-
level actions applicable within research, government, and institutional data settings. The goal is for data 
stewards and other users of Indigenous data to implement CARE and FAIR Principles in tandem.
While each is conceptually distinct, the CARE Principles are related to each other. The Principles define 
rights, interests, and concepts to be employed in facilitating Indigenous control in data governance and 
reuse. An enacted mechanism can address a single Principle or multiple simultaneously. However, data 
­governance must address the full set of Principles to demonstrate a CARE Full process. 
Figure 2: The CARE Principles for Indigenous Data Governance.

## Page 7

Carroll et al: The CARE Principles for Indigenous Data Governance
Art. 43, page 6 of 12  
The CARE Principles and Their Supporting Concepts
Indigenous data must facilitate collective benefit for Indigenous Peoples to achieve inclusive development 
and innovation, improve governance and citizen engagement, and realize equitable outcomes. Benefits 
accrue when data ecosystems are designed and function to support (1) Indigenous nation and community 
use and reuse of data; (2) use of data for policy decisions and evaluation of services; and (3) creation and use 
of data that reflect community values.
UNDRIP affirms Indigenous Peoples’ rights and interests in their data. Recognition of these rights bolsters 
Indigenous Peoples’ authority to control and govern such data, further affirming the need for ‘data for 
governance.’ Indigenous Peoples must have access to data that support Indigenous governance and self-
determination. Indigenous Peoples must be the ones to determine data governance protocols, while being 
actively involved in stewardship decisions for Indigenous data that are held by other entities.
When working with Indigenous data, there is a responsibility to nurture respectful relationships with 
Indigenous Peoples from whom the data originate. Aspects of the relationship include investing in capacity 
development, increasing community data capabilities, and embedding data within Indigenous languages 
and cultures. Pursuing these goals fulfills the ultimate responsibility of supporting Indigenous data that 
advances Indigenous Peoples’ self-determination and collective benefit. 
Indigenous Peoples’ rights and wellbeing should be the focus across data ecosystems and throughout 
data lifecycles in order to minimize harm, maximize benefits, promote justice, and allow for future use. 
Paramount to ethics in data practices is representation and participation of Indigenous Peoples, who must 
be the ones to assess benefits, harms, and potential future uses based on community values and ethics.
The CARE Principles in Action
The usefulness of high-level Indigenous data governance principles relies on both Indigenous communities 
and research/data communities to understand operative concepts and to apply them preemptively across 
data ecosystems and lifecycles. Creating opportunities for non-Indigenous understanding and for Indig­
enous leadership in data processes will contribute to the development of data and data systems that can lead 
to Indigenous innovation and development.
Early Adopters of the CARE Principles 
Defining principles is an important step toward exercising Indigenous Data Sovereignty and addressing long­
standing concerns about data governance. Some organizations are adopting the CARE Principles through 
relationships, policies, and mechanisms. Examples include the Research Data Alliance, the Smithsonian 
Institution, and the Open Data Charter. 
Research Data Alliance (www.rd-alliance.org), in research environments
In 2016, the Research Data Alliance (RDA) hosted a workshop on Indigenous Data Sovereignty. Recogniz­
ing the importance of enhancing Indigenous rights and interests in data and potential implications for 
mainstream data policy, the RDA supported the creation of the International Indigenous Data Sovereignty 
Interest Group (IG). The IG convenes existing Indigenous Data Sovereignty networks with other Indigenous 
and allied researchers, which has resulted in broader global connections, a deeper focus on research data, 
and the CARE Principles (Lovett et al. 2019; Rainie et al. 2019; RDA IG 2019; RDA 2017). In further support of 
the IG and the CARE Principles, the RDA formally affiliated with the Global Indigenous Data Alliance (GIDA), 
which hosts the Principles. The affiliation affirms the importance of both CARE and GIDA, and represents an 
effort to promote implementation of the Principles throughout the RDA community (RDA 2019). 
The Smithsonian Institution (www.si.edu), in collections environments
In 2012, the American Museum of Natural History at the Smithsonian Institution in Washington, DC 
released an Access and Benefit Sharing Policy on Genetic Resources in response to the Nagoya Protocol 
(2010) addressing Indigenous expectations around benefit sharing, prior informed consent, and mutually 
agreed terms for collections that it stewards (UN 2011; SI 2012). Subsequently, the US government released 
the new Open Access to Research Policy in 2013 as an important step in providing unprecedented access to 
research and data (Stebbins 2013). However, this policy (and others like it) treats all data in the same way: 
without attention to the nature, the content, or the conditions under which the data was created in the first 
place (Creative Commons 2019, Wikimedia 2019). 
In December 2019, Smithsonian Directive 609 was released (SI 2019). With specific focus on digital asset 
access and use, it sets forth Smithsonian policy for access and use of Smithsonian digital assets ahead of the

## Page 8

Carroll et al: The CARE Principles for Indigenous Data Governance
Art. 43, page 7 of 12
expected release of the institutional Open Access Statement, in February 2020. The SD 609 is important, 
because it helps identify specific categories of material that might need more attention and care in their 
management. One of these includes sensitive content, which is: 
defined in different ways by members of individual communities, nations, tribes, ethnic groups, 
and religious denominations, but may include materials that relate to traditional knowledge and 
practices. Such materials may: a) be considered the private domain of specific individuals, clans, 
cults or societies; b) require an appropriate level of knowledge to view and understand; c) threaten 
the privacy and well-being of a community when exposed or disclosed to outsiders; and/or d) give 
offense if inappropriately used or displayed, or when appropriated or exploited for commercial 
purposes. SD 609 Restriction Code: B1. (SI 2019)
This identification offers an important opportunity to further explore the incorporation of the CARE Prin­
ciples into the Smithsonian’s imminent Open Access policy. Recognizing complexity within Smithsonian 
digital assets and accompanying metadata, the CARE Principles would add an important layer of relational 
and temporal governance for Indigenous collections within an open access logic. Additionally, there are 
further opportunities for the CARE Principles to be directly extended into collection management practices. 
For example, work is about to begin to develop a unique set of ‘Collection CARE Notices’ for Indigenous 
collections at the Smithsonian and then into other US institutional contexts. Extending the current Cul­
tural Institution Notices developed by Local Contexts (LC 2018), these new Notices will reflect inherent 
relationships of care, responsibility and governance in collection stewardship within the institution. As 
they are developed, these Notices will integrate the CARE Principles directly, embedding these into the 
Smithsonian’s cataloguing and digital infrastructure for Indigenous collections. By providing item- and 
collection-specific information, the Collection CARE Notices will function as a direct mechanism to assist in 
management and decision-making consistent with CARE Principles. 
Open Data Charter (opendatacharter.net), in government environments
After release of the CARE Principles, the Open Data Charter (ODC) Implementation Working Group hosted 
a conversation on the Principles (Stone and Calderon 2019). Discussion focused on implementation mecha­
nisms as well as resonance among ODC, FAIR, and CARE Principles (Figure 3). While ODC Principles reflect 
all four FAIR Principles, they directly address only the CARE Principle of ‘Collective benefit.’ The ODC Prin­
ciple of ‘Open by default’ does not directly map to the FAIR or CARE Principles. During a review of ODC 
Principles in 2018, open data community members hotly debated ‘Open by default,’ showing a broad range 
of interpretations ranging from construing ‘Open by default’ as a key tenet of open data to considering the 
principle as tough to define and operationalize (Stone and Calderon 2019). The CARE Principles can help 
refine and specify what ‘Open by default’ means by (1) ensuring roles for Indigenous Peoples and other 
Figure 3: The Overlap Between the CARE and FAIR Principles and the Open Data Charter.

## Page 9

Carroll et al: The CARE Principles for Indigenous Data Governance
Art. 43, page 8 of 12  
­marginalized communities in open data decision-making and (2) using mechanisms to protect access to data 
as indicated by these communities to minimize harms and maximize benefits. 
While implementation has commenced in these examples and elsewhere, further research is needed (1) to 
identify mechanisms that support implementation of the CARE Principles; (2) to create tools, policies, and 
practices that enact the Principles; (3) to explore the application of the Principles in different contexts, such 
as research repositories, knowledge co-production, institutional policies and practices, and, retrospectively, 
in already existing databases and systems; and (4) to operationalize the Principles in tandem with the FAIR 
Principles.
Conclusion
Being CARE Full is a prerequisite for equitable data and data practices. The CARE Principles draw from, inte­
grate, and build on the work of mainstream stakeholders focused on data for reuse (e.g., FAIR Principles) and 
the efforts of Indigenous-led networks and coalitions focused on Indigenous data governance and research 
control. While centering data in the FAIR Principles complements other efforts to inform responsibilities 
for data producers and repositories, the CARE Principles extend that work to actions that align with the 
‘people’ and ‘purpose’ for which data exist and are used. As the mainstream community of data stakeholders 
advances standards and practices to facilitate data reuse and research reproducibility, the CARE Principles 
enhance that work by reversing historical power imbalances. The CARE Principles address historical inequi­
ties by creating value from Indigenous data in ways that are grounded in Indigenous worldviews and by 
realizing opportunities for Indigenous Peoples within the knowledge economy. 
In addition, increasingly robust management and stewardship frameworks for Indigenous digital resources 
to the benefit of Indigenous Peoples have broader implications for other marginalized populations, high­
lighting the importance of local and group control for the quality and reproducibility of research and data 
(Rainie et al. 2019). Furthermore, the CARE Principles address issues of relevance for many populations (e.g., 
privacy, future use, reuse, stewardship), to the extent that the Principles provide a normative foundation for 
setting standards, crafting policy, and developing research agendas in relation to data acquired about popu­
lations as collectives. Those populations might be minority groups, distinctive communities, or other collec­
tives wanting to maintain high levels of trust and accountability in the use of data about their communities. 
The implementation of the CARE Principles in tandem with the FAIR Principles will result in data that 
reflect the realities of Indigenous Peoples, be useful for Indigenous purposes, and remain under Indigenous 
control, while promoting knowledge discovery and innovation. The CARE Principles are a guide for data pro­
ducers, stewards, and publishers to affirm Indigenous rights to self-determination through CARE Full data 
practices that will ultimately address complex issues related to privacy, future use, and collective interests, 
and increase the value of data for reuse. Just as the FAIR Principles are a precursor to good data management 
and stewardship practices, the CARE Principles encourage data users to be FAIR and CARE. 
Acknowledgements
The original workshop “Indigenous Data Sovereignty Principles for the Governance of Indigenous Data,” 
was organized by Stephanie Russo Carroll and Maui Hudson, in collaboration with the Research Data Alli­
ance (RDA) International Indigenous Data Sovereignty Interest Group at the International Data Week held 
Thursday, 8 November 2018, in Gaborone, Botswana. The Principles described in this manuscript represent 
voluntary contributions and participation of the authors at, and/or subsequent to, this workshop and from 
the wider US Indigenous Data Sovereignty Network, Te Mana Raraunga Māori Data Sovereignty Network, 
and Maiam nayri Wingara Aboriginal and Torres Strait Islander Data Sovereignty Collective communities. 
We acknowledge the Indigenous Peoples of Botswana, on whose land the Principles emerged, as well as 
Indigenous Peoples worldwide. We are grateful to the RDA for the workshop location and to the RDA US for 
travel support for some attendees. This paper was supported by the RDA Europe 4.0 project that has received 
funding from the European Union’s Horizon 2020 research and innovation programme under grant agree­
ment No 777388. Thank you to the following individuals for their comments, edits, and suggestions: Randy 
Akee, Leah Ballantyne, Donna Cormack, Dominique David-Chavez, Bhiamie Eckford-Williamson, Nanibaa’ 
Garrison, Sharon Hausam, Lydia Jennings, Tahu Kukutai, Kelsey Leonard, Christina Ore, Qunmigu (Kacey 
Hopson), Andrew Sporle, Michele Suina, Maggie Walter, the Alaska Native Policy Center at the First ­Alaskans 
Institute, and the attendees at the “The International Law, United Nations Declaration of the Rights of 
­Indigenous Peoples and Indigenous Data Sovereignty” Workshop at the Oñati International Institute of the 
Sociology of Law. We also acknowledge Andrew Martinez’s contributions to designing the tables and figures.

## Page 10

Carroll et al: The CARE Principles for Indigenous Data Governance
Art. 43, page 9 of 12
Competing Interests
M.P. is Editor-in-Chief of the Data Science Journal, but played no role in the review and editing of this paper. 
The authors have no other competing interests to declare.
Author Contributions
S.R.C. was the primary author of the manuscript, and coordinated and participated extensively in the draft­
ing and editing of the CARE Principles. S.R.C., I.G., and D.R.L received partial support from the Morris K. 
Udall and Stewart L. Udall Foundation. As senior author, M.H. was significantly involved in the drafting of 
the CARE Principles and this manuscript text. I.G. was significantly involved in the drafting of the manu­
script. J.A. contributed a case that illustrates the emerging implementation of the CARE Principles. All other 
authors are listed alphabetically, and contributed to the manuscript by their participation in the initial 
workshop and/or by editing or commenting on the manuscript text.
References
Anaya, J. 2004. Indigenous Peoples and International Law. Oxford: Oxford University Press. 
Anderson, I, Griew, R, et al. 2003. Ethics Guidelines, Health Research and Indigenous Australians. New 
Zealand Bioethics Journal, 20–29. 
Anderson, J. 2009. Law, Knowledge, Culture: The Production of Indigenous Knowledge in Intellectual Property 
Law. Cheltenham, UK: Edward Elgar Press.
Anderson, J. 2015. Intellectual Property and Indigenous Knowledge. 2nd ed. International Encyclope­
dia for Social and Behavioral Sciences, 769–778 DOI: https://doi.org/10.1016/B978-0-08-097086-
8.64078-3
Cajete, G. 2000. Native science: Native laws of interdependence. Santa Fe: Clear Light.
Carroll, SR, Rodriguez-Lonebear, D and Martinez, A. 2019. Indigenous Data Governance: Strategies from 
United States Native Nations. Data Science Journal, 18(31): 1–15. DOI: https://doi.org/10.5334/dsj-
2019-031
Castellano, MB. 2004. Ethics of Aboriginal research. Journal of Aboriginal Health, January, 98–114.
Creative Commons. 2019. When We Share, Everyone Wins. 2019. Available at https://creativecommons.
org/ [Last accessed 17 January 2020].
Davis, M. 2016. Data and the United Nations Declarations on the Rights of Indigenous Peoples. In: Kukutai, 
T and Taylor, J (eds.), Indigenous data sovereignty: Toward an agenda, 25–38. Canberra, Australia: Austral­
ian National University Press. DOI: https://doi.org/10.22459/CAEPR38.11.2016.01
Demchenko, Y, Los, W and de Laat, C. 2018. Data as Economic Goods: Definitions, Properties, Challenges, 
Enabling Technologies for Future Data Markets. ITU Journal: ICT Discoveries 2(23). University of Amster­
dam Available at https://www.itu.int/en/journal/002/Documents/ITU2018-12.pdf [Last accessed 17 
January 2020].
Drugge, A-L. 2016. Ethics in Indigenous Research: Past Experiences - Future Challenges. Umea, Sweden: 
Vaartoe Centre for Sami Research, Umea University.
Echo-Hawk, W. 2013. In the Light of Justice: The Rise of Human Rights in Native America and the Declaration 
on the Rights of Indigenous Peoples. London: Fulcrum Press.
First Nation’s Information Governance Centre. 2018. The First Nations Principles of OCAP®. Available 
at https://fnigc.ca/ocap [Last date accessed 2 December 2019].
Garrison, N, Hudson, M, Ballantine, L, Garba, I, Martinez, A, Taualii, M, Arbour, L, Caron, NR and 
Rainie, SC. 2019. Genomic Research through an Indigenous Lens: Understanding the Expectations. 
Annual Review of Genomics and Human Genetics Volume 20. DOI: https://doi.org/10.1146/annurev-
genom-083118-015434
Hudson, M, Milne, M, Russell, K, Smith, B, Reynolds, P and Atatoa-Carr, P. 2016. The Development 
of Guidelines for Indigenous Research Ethics in Aotearoa/New Zealand. In A.-L. Drugge (ed.), Ethics in 
Indigenous Research, Past Experiences – Future Challenges, 157–174. Umea, Sweden: Vaartoe Centre for 
Sami Research, Umea University.
Independent Expert Advisory Group. 2014. Mobilising the data revolution for sustainable develop­
ment. Available at http://www.undatarevolution.org/wp-content/uploads/2014/11/execsum.pdf [Last 
accessed 17 January 2020].
Inuit Tapiriit Kanatami. 2018. National Inuit Strategy on Research. 2018. Available at https://www.itk.ca/
wp-content/uploads/2018/03/National-Inuit-Strategy-on-Research.pdf [Last accessed 17 January 2020].

## Page 11

Carroll et al: The CARE Principles for Indigenous Data Governance
Art. 43, page 10 of 12  
Jackson, L, Kuhlman, C, Jackson, F and Keolu Fox, P. 2019. Including Vulnerable Populations in the 
Assessment of Data From Vulnerable Populations. Frontiers in Big Data Volume 2. DOI: https://doi.
org/10.3389/fdata.2019.00019
Janke, T. 1998. Our Culture: Our Future. Report on Australian Indigenous Cultural and Intellectual Property 
Rights. Australian Institute of Aboriginal and Torres Strait Islander Studies: Canberra. 
Janke, T. 2004. Minding Culture: Case Studies in Intellectual Property and Traditional Cultural Expressions. 
Geneva: World Intellectual Property Organization. Available at https://www.wipo.int/publications/en/
details.jsp?id=286 [Last accessed 22 January 2020].
Julayinbul Statement in Indigenous Intellectual Property Rights. 1993. The Julayinbul Conference on 
Intellectual and Cultural Property. Australia: Jingarrba. 
Kovach, M. 2009. Indigenous methodologies: Characteristics, conversations, and contexts. Toronto: University 
of Toronto Press.
Kukutai, T and Cormack, D. 2019. Mana motuhake ā-raraunga: datafication and social science research in 
Aotearoa, Kōtuitui. New Zealand Journal of Social Sciences Online, 14(2): 201–208, DOI: https://doi.org
/10.1080/1177083X.2019.1648304
Kukutai, T and Taylor, J. 2016a. Indigenous data sovereignty: Toward an agenda. Canberra, Australia: Aus­
tralian National University Press. DOI: https://doi.org/10.22459/CAEPR38.11.2016
Kukutai, T and Taylor, J. 2016b. Data Sovereignty for Indigenous Peoples: Current Practice and Future 
Needs. In: Kukutai, T and Taylor, J (eds.), Indigenous data sovereignty: Toward an agenda, 1–22. Canberra, 
Australia: Australian National University Press. DOI: https://doi.org/10.22459/CAEPR38.11.2016.01
Kukutai, T and Walter, M. 2015. Recognition and indigenizing official statistics: Reflections from Aotearoa 
New Zealand and Australia. Statistical Journal of the IAOS, 31(2) 317–326. DOI: https://doi.org/10.3233/
sji-150896
Local Contexts. 2018. Cultural Institution Notices. 2018. Available at https://localcontexts.org/ci-notices 
[Last accessed January 2020].
Lovett, R, Lee, V, Kukutai, T, Cormack, D, Rainie, SC and Walker, J. 2019. Good data practices for 
Indigenous Data Sovereignty and Governance. In: Daly, A, Devitt, K and Monique, M (eds.), Good Data. 
­Amsterdam: Institute of Network Cultures Inc. ISBN 978-94-92302-27-4.
Maiam nayri Wingara. 2018. Indigenous Data Sovereignty Communique. Indigenous Data Sovereignty 
Summit. 20th June 2018, Canberra: Australian Capital Territory. Available at https://static1.squares­
pace.com/static/5b3043afb40b9d20411f3512/t/5b6c0f9a0e2e725e9cabf4a6/1533808545167/
Communique%2B-%2BIndigenous%2BData%2BSovereignty%2BSummit.pdf.
Martinez Cobo, J. 1982. Study of the Problem of Discrimination Against Indigenous Populations Final 
Report. Available at https://www.un.org/development/desa/indigenouspeoples/publications/mar­
tinez-cobo-study.html [Last accessed 17 January 2020].
Mātaatua Declaration on Cultural and Intellectual Property Rights of Indigenous Peoples. 1993. 
First International Conference on the Cultural and Intellectual Property Rights of Indigenous Peoples. 
12-18 June 1993. Aotearoa, New Zealand. Available at https://www.wipo.int/export/sites/www/tk/en/
databases/creative_heritage/docs/mataatua.pdf.
McGregor, D, Restoule, JP and Johnston, R. (eds.) 2018. Indigenous research: Theories, practices, and rela­
tionships. Canadian Scholars’ Press.
Metis Centre. 2011. Principles of Ethical Métis Research. 2011. National Aboriginal Health Organization. 
Available at https://ruor.uottawa.ca/bitstream/10393/30555/1/2011_04_ethics.pdf [Last accessed 17 
January 2020].
Nickerson, M. 2017. First Nations’ data governance: Measuring the nation-to-nation relationship discussion 
paper. British Columbia First Nations’ Data Governance Initiative. 
Open Data Charter. 2015. Open Data Charter Principles. 2015. Available at https://opendatacharter.net/
principles/ [Last accessed 17 January 2020].
Rainie, SC, Schultz, JL, Briggs, E, Riggs, P and Palmanteer-Holder, NL. 2017. Data as strategic resource: 
Self-determination and the data challenge for United States Indigenous nations. International Indigenous 
Policy Journal, 8(2). DOI: https://doi.org/10.18584/iipj.2017.8.2.1
Rainie, SC, Kukutai, T, Walter, M, Figueroa-Rodriguez, OL, Walker, J and Axelsson, P. 2019. Issues in 
Open Data: Indigenous Data Sovereignty. In: Davies, T, Walker, S, Rubinstein, M and Perini, F (eds.), The 
State of Open Data: Histories and Horizons. Cape Town and Ottawa: African Minds and International 
Development Research Centre. pp. 300–319.

## Page 12

Carroll et al: The CARE Principles for Indigenous Data Governance
Art. 43, page 11 of 12
Ratima, M. 2001. Kia uruuru mai a hauora being healthy, being Maori: Conceptualising Maori 
health promotion. Published thesis (PhD) Department of Public Health. Dunedin, University of 
Otago. 
Research Data Alliance. 2017. International Indigenous Data Sovereignty Intertest Group. Available at 
https://www.rd-alliance.org/groups/international-indigenous-data-sovereignty-ig [Last accessed 17 
January 2020].
Research Data Alliance. 2019. RDA Announces Memorandum of Understanding with the Global Indige­
nous Data Alliance. Available at https://www.rd-alliance.org/rda-announces-memorandum-understand­
ing-global-indigenous-data-alliance [Last accessed 17 January 2020].
Research Data Alliance International Indigenous Data Sovereignty Interest Group. September 2019. 
CARE Principles for Indigenous Data Governance. The Global Indigenous Data Alliance. GIDA-global.org. 
Available at gida-global.org/care [Last accessed 17 January 2020].
Rodriguez-Lonebear, D. 2016. Building a data revolution in Indian country. In: Kukutai, T and Taylor, J 
(eds.), Indigenous data sovereignty: Toward an agenda. Canberra, Australia: Australian National University 
Press. pp. 253–272. DOI: https://doi.org/10.22459/CAEPR38.11.2016.14
Smith, D. 2016. Governing data and data for governance: the everyday practice of Indigenous sover­
eignty. In: Kukutai, T and Taylor, J (eds.), Indigenous data sovereignty: Toward an agenda. Canberra, 
Australia: Australian National University Press. pp. 117–135. DOI: https://doi.org/10.22459/
CAEPR38.11.2016.07
Smith, LT. 2012. Decolonizing Methodologies: Research and Indigenous Peoples. Zed Books. London: Univer­
sity of Otago Press. 
Smithsonian Institution. 2012. Access and Benefit Sharing Policy on Genetics Resources. Washington, DC: 
National Museum of American History. Available at https://naturalhistory.si.edu/sites/default/files/
media/file/nmnhabspolicys508issues.pdf [Last accessed 17 January 2020].
Smithsonian Institution. 2019. Smithsonian Directive 609 – Digital Asset Access and Use. Available at 
https://www.si.edu/content/pdf/about/sd/SD609.pdf [Last accessed 31 January 2020].
Snipp, CM. 2016. What does data sovereignty imply: what does it look like? In: Kukutai and Taylor, J (eds.), 
Indigenous data sovereignty: Toward an agenda. Canberra, Australia: Australian National University Press. 
pp. 39–55. DOI: https://doi.org/10.22459/CAEPR38.11.2016.01
Stebbins, M. 2013. Expanding Public Access to the Results of Federally Funded Research. Available at 
https://obamawhitehouse.archives.gov/blog/2013/02/22/expanding-public-access-results-federally-
funded-research [Last accessed 17 January 2020].
Stone, P and Calderon A. 2019. [Spotlight] CARE Principles Unpacking Indigenous Data Governance. 
Available at https://medium.com/@opendatacharter/spotlight-care-principles-f475ec2bf6ec [Last 
accessed 17 January 2020].
Taylor, J and Kukutai, T. 2015. Report to the Academy of the Social Sciences in Australia on the Workshop 
Data Sovereignty for Indigenous Peoples: Current Practice and Future Needs. 9–10 July 2015. University 
House, Australian National University. Available at https://socialsciences.org.au/publications/data-
sovereignty-for-indigenous-peoples-current-practice-and-future-needs/ [Last accessed 17 January 2020]. 
DOI: https://doi.org/10.22459/CAEPR38.11.2016.01
Te Mana Raraunga. 2016. Māori Data Sovereignty Network Charter. Available at https://static1.squares­
pace.com/static/58e9b10f9de4bb8d1fb5ebbc/t/5913020d15cf7dde1df34482/1494417935052/Te+
Mana+Raraunga+Charter+%28Final+%26+Approved%29.pdf [Last accessed 17 January 2020].
Te Mana Raraunga. 2018. Principles of Māori Data Sovereignty Brief #1. October 2018. Available at 
https://static1.squarespace.com/static/5d3799de845604000199cd24/t/5d6f940cc5442b00013
e4dab/1567593484780/TMR%2BMa%CC%84ori%2BData%2BSovereignty%2BPrinciples%2BOct
%2B2018.pdf [Last accessed 17 January 2020].
The Economist. 2017. The world’s most valuable resource is no longer oil, but data, 6 May 2017. Available 
at https://www.economist.com/news/leaders/21721656-data-economy-demands-new-approach-anti­
trust-rules-worlds-most-valuable-resource [Last date accessed 17 January 2020].
Tsosie, R. 1997. Indigenous Peoples Claims to Cultural Property: A Legal Perspective. Museum Anthropology, 
21(3): 5–11. DOI: https://doi.org/10.1525/mua.1997.21.3.5
Tsosie, R. 2019. Tribal Data Governance and Informational Privacy: Constructing ‘Indigenous Data Sover­
eignty.’ Montana Law Review, 80(2). Available at https://scholarship.law.umt.edu/mlr/vol80/iss2/4/ 
[Last accessed 9 February 2020].

## Page 13

Carroll et al: The CARE Principles for Indigenous Data Governance
Art. 43, page 12 of 12  
United Nations. 2007. United Nations Declaration on the Rights of Indigenous Peoples: Resolution/
Adopted by the General Assembly, 2 October 2007, A/RES/61/295. Available at: https://www.refworld.
org/docid/471355a82.html [Last date accessed 17 January 2020].
United Nations. 2011. Nagoya Protocol on Access to Genetic Resources and the Fair and Equitable Sharing 
of Benefits Arising from their Utilization to the Convention on Biological Diversity. Available at https://
www.cbd.int/abs/ [Last accessed 17 January 2020].
United Nations. 2009. State of the World’s Indigenous Peoples. Unknown. Available at https://www. 
un.org/esa/socdev/unpfii/documents/SOWIP/en/SOWIP_web.pdf [Last accessed 28 August 2018].
United State Indigenous Data Sovereignty Network. 2020. The US Indigenous Data Sovereignty Net­
work Indigenous Data Governance Principles. 
Walter, M. 2018. The Voice of Indigenous Data: Beyond the markers of disadvantage First Things First. Grif­
fith Review, 60: 256–263. Available at https://griffithreview.com/articles/voice-indigenous-databeyond-
disadvantage/.
Wikimedia. 2019. Available at wikimedia.org [Last accessed 17 January 2020].
Wilkinson, M, Dumontier, M, Aalbersberg, I, et al. 2016. The FAIR Guiding Principles for scientific data 
management and stewardship. Sci. Data, 15 March 2016, DOI: https://doi.org/10.1038/sdata.2016.18
Wilson, S. 2008. Research is ceremony: Indigenous research methods. Winnipeg: Fernwood.
Wilson, WA. 2004. Introduction: Indigenous knowledge recovery is indigenous empowerment. American 
Indian Quarterly, 359–372. DOI: https://doi.org/10.1353/aiq.2004.0111
How to cite this article: Carroll, SR, Garba, I, Figueroa-Rodríguez, OL, Holbrook, J, Lovett, R, Materechera, S, Parsons, 
M, Raseroka, K, Rodriguez-Lonebear, D, Rowe, R, Sara, R, Walker, JD, Anderson, J and Hudson, M. 2020. The CARE 
Principles for Indigenous Data Governance. Data Science Journal, 19: 43, pp. 1–12. DOI: https://doi.org/10.5334/dsj-
2020-043
Submitted: 10 February 2020       Accepted: 21 October 2020        Published: 04 November 2020
Copyright: © 2020 The Author(s). This is an open-access article distributed under the terms of the Creative 
Commons Attribution 4.0 International License (CC-BY 4.0), which permits unrestricted use, distribution, and 
reproduction in any medium, provided the original author and source are credited. See http://creativecommons.org/
licenses/by/4.0/.
Data Science Journal is a peer-reviewed open access journal published by Ubiquity 
Press.
OPEN ACCESS
