---
title: "2025-Chhikara-Through the Prism of Culture Evaluating LLMs' Understanding of Indian - PDF Extract"
source_pdf: "2025-Chhikara-Through the Prism of Culture Evaluating LLMs' Understanding of Indian.pdf"
pages: 12
extracted_at: "2026-02-15T17:51:59.311736"
---

# PDF Extract: 2025-Chhikara-Through the Prism of Culture Evaluating LLMs' Understanding of Indian

**Source PDF:** 2025-Chhikara-Through the Prism of Culture Evaluating LLMs' Understanding of Indian.pdf
**Total Pages:** 12

---

## Content

```
--- Page 1 ---

1
Through the Prism of Culture: Evaluating LLMs’
Understanding of Indian Subcultures and Traditions
Garima Chhikara, Abhishek Kumar, Abhijnan Chakraborty
Abstract—Large Language Models (LLMs) have shown remark-
able advancements but also raise concerns about cultural bias,
often reflecting dominant narratives at the expense of under-
represented subcultures. In this study, we evaluate the capacity of
LLMs to recognize and accurately respond to the Little Traditions
within Indian society, encompassing localized cultural practices
and social institutions such as caste, kinship, marriage, and
religion. Through a series of case studies, we assess whether
LLMs can balance the interplay between dominant Great Traditions
and localized Little Traditions. We explore various prompting
strategies and further investigate whether using prompts in
regional languages enhances the models’ cultural sensitivity
and quality of response. Our findings reveal that while LLMs
demonstrate an ability to articulate cultural nuances, they often
struggle to apply this understanding in practical, context-specific
scenarios. To the best of our knowledge, this is the first study
to analyze LLMs engagement with Indian subcultures, offering
critical insights into the challenges of embedding cultural diversity
in AI systems.
Index Terms—Large Language Models, Cultural Bias, Little
Traditions, Indian Society
I. INTRODUCTION
T
HE interplay of cultural traditions across the world reveals
a fascinating duality often characterized as the Great
and Little traditions. These concepts capture the dynamic
relationship between dominant, universalized cultural practices
and their localized, community-specific counterparts [1]. For
a long time, researchers have categorized Great Tradition to
represent the culture of the elites – codified, documented,
and often transcending geographic boundaries – while the
Little Tradition tends to embody the everyday practices of
ordinary people, deeply rooted in local contexts [2], [3], [4].
This relationship is fluid: localized traditions sometimes gain
prominence and evolve into universal practices (a process
known as universalization), while broader cultural elements
often adapt to specific regional contexts, becoming localized [5],
[6]. For instance, the Hindu God Shiva is revered across India,
Garima Chhikara is with the Amar Nath and Shashi Khosla School of Infor-
mation Technology, Indian Institute of Technology Delhi, India – 110016 and
with the Computer Science and Engineering Department, Delhi Technological
University, India – 110042 (e-mail: garimachhikara128@gmail.com).
Abhishek Kumar was with the Computer Science and Engineering De-
partment, Delhi Technological University, India – 110042 (e-mail: ab-
hikrnigam@gmail.com).
Abhijnan Chakraborty is with the Department of Computer Science and
Engineering, Indian Institute of Technology Kharagpur, India – 721302 (e-mail:
abhijnan@cse.iitkgp.ac.in).
This work has been submitted to the IEEE for possible publication. Copyright
may be transferred without notice, after which this version may no longer be
accessible.
representing a Great Tradition, but his localized form, Lord
Bhairav, embodies a little tradition. Similarly, the famous
festival of Holi has localized variants such as Lathmar Holi,
celebrated uniquely in certain regions of India [7], [8]. The
dynamic interplay of these traditions illustrates how global and
local cultures continually shape and redefine one another [9].
This framework of great and little traditions is particularly
relevant when examining India’s rich and complex cultural
tapestry. As one of the most culturally diverse countries
in the world, India is a microcosm of this global dynamic.
Its diversity stems from a unique confluence of historical
migrations, geographical variation, and social stratification.
Over millennia, India has been shaped by the influences of
numerous civilizations and communities, including the Aryans,
Dravidians, Greeks, Persians, Mongols, and Arabs [10]. These
interactions created a melting pot of cultural practices, where
the blending of traditions has become a hallmark of Indian
identity [11]. Furthermore, the huge linguistic and religious
diversity has fostered a remarkable variety of festivals, rituals,
and practices, reflecting both regional influences and broader
pan-Indian elements [12].
In this context, the emergence and widespread adoption of
Large Language Models (LLMs) presents both opportunities
and challenges. LLMs are increasingly employed for various
applications, including decision-making, communication, and
education, making their understanding of cultural nuances
crucial. Cultural awareness enables these models to generate
contextually sensitive and respectful responses, particularly
in addressing delicate topics like religion, politics, and social
norms. For example, while Qawwalis are prohibited in certain
Islamic communities, they are an accepted and celebrated tradi-
tion in India [13]. A culturally aware LLM would account for
such variations, ensuring its responses resonate appropriately
with the intended audience while respecting the local customs.
However, a lack of cultural understanding in LLMs risks
producing biased or inappropriate outputs that could alienate
certain communities or perpetuate misinformation [14]. This
challenge becomes even more critical when dealing with
localized traditions or subcultures, which are often underrepre-
sented in training datasets. Without deliberate efforts to include
these voices, AI systems risk reinforcing systemic inequalities,
favouring well-represented communities while neglecting the
nuanced realities of others [15]. For example, a Google search
on a specific topic increasingly surfaces AI-generated content
among the top results. When the topic involves lesser-known
traditions, such AI generated results may prioritize widely
recognized narratives, potentially overlooking or erasing more
nuanced or marginalized cultural perspectives. The greatest
arXiv:2501.16748v3  [cs.CL]  7 Sep 2025

--- Page 2 ---

2
impact will be on AI-native future generations from under-
represented cultures, who will grow up relying on these AI
models for education and guidance. Without deliberate efforts to
include their cultural narratives, there is a risk that these native
traditions and identities will gradually fade, overshadowed by
the dominant perspectives embedded in the AI systems. To
address this gap, it is essential to evaluate how effectively
LLMs recognize and reflect the ‘Little Traditions’ of Indian
society and other under-represented cultures.
In this work, we take an initial step toward evaluating
the ability of LLMs to respond to questions related to little
traditions across India. Sociologists have long emphasized the
importance of various aspects of social life – such as caste,
kinship, marriage, family, clans, sects, religion, and rituals – in
shaping Indian society [16], [17]. Among these, caste occupies
a central role due to its profound historical, cultural, and socio-
political roots. Emerging from the ancient Varna system in
Hinduism, caste divided Indian society into four occupational
categories: Brahmins (priests and scholars), Kshatriyas (war-
riors and rulers), Vaishyas (traders), and Shudras (laborers) [18].
Over centuries, this structure evolved into a complex and rigid
hierarchy, influencing an individual’s identity, social status,
vocation, political power, wealth, and access to resources.
Caste has also traditionally shaped marriage alliances, dietary
practices, rituals, and educational opportunities [19]. Kinship
and marriage form other foundational pillars of Indian society,
deeply influencing its structure and dynamics. Kinship defines
familial relationships, roles, and responsibilities, connecting
individuals to their lineage (such as clan, caste, or gotra) and the
broader community [20]. Marriage, regarded as both a spiritual
commitment and a social institution, strengthens familial
bonds, upholds cultural and religious values, and ensures
the continuity of traditions [21]. Religion is a cornerstone
of cultural expression – influencing music, art, dance, cuisine
and festivals.
Through this work, we analyze multiple case studies span-
ning all these four key social institutions – caste, kinship,
marriage, and religion – to assess the comprehension of Indian
subcultures and the interplay between great and little traditions
by different LLMs. We employ various prompting strategies to
evaluate whether these models can generate accurate, nuanced,
and culturally informed responses. Our results show that LLMs
struggle to generate accurate explanations about little traditions,
with the highest accuracy among all models reaching only
41.6% in the vanilla setup. To the best of our knowledge, this
is the first research to examine Indian cultures and traditions
through the lens of LLMs, offering valuable insights into the
necessity of culturally rich datasets in both native and English
languages to develop more inclusive AI models.
II. LOOKING AT LLMS THROUGH THE PRISM OF CULTURE
Our objective is to assess the understanding of LLMs about
the intricacies of little traditions and subcultures. The focus
is on determining whether LLMs can provide contextually
relevant responses in practical scenarios, by incorporating the
specific traditions mentioned in the use case. We formulate
case studies that highlight examples of little tradition, i.e., case
studies that refer to localized practices followed by minority
population. A vast body of Indology research has analyzed
Indian society through caste, kinship, marriage, family, sects,
religion, and rituals, due to its distinctive characteristics [16],
[17], [22], [23]. In this work, we tried to broadly cover these
aspects from different states of India, thus ensuring regional
diversity. As can be seen in the Table I, the case studies cover
all broad geographical regions of India. Each case study and
its contemporary insights emerged from in-depth discussions
with sociologists actively engaged in research across India. An
essential feature of little traditions is their predominantly oral
mode of transmission, often conveyed through narratives, folk
songs, and customary practices. Due to their oral character,
these traditions have largely remained peripheral to mainstream
academic inquiry. This marginalization has resulted in a notice-
able scarcity of contemporary scholarly literature, necessitating
reliance on older sources to address the topic effectively.
Experimental Setup: We utilize In-Context Learning (ICL)
capability of LLMs to obtain result of our case-studies.
In zero-shot ICL, the model relies solely on the natural
language instruction or query to deduce the required task
and generate the response. Multiple studies have highlighted
the efficacy of LLMs in addressing complex tasks using
ICL [24], and these robust abilities have been extensively
acknowledged as emerging strength [25]. We input the case
study S and instruction I to LLM L. Instruction I directs
the LLM to select between two options – one representing
the dominant perspective and the other endorsing the little
tradition. LLM is tasked to select one option followed by a
brief justification for its choice, let ˆY denote the option selected
and ˆE denote the explanation given by the LLM, thus ( ˆY, ˆE)
= L (S, I). We utilize five popular LLMs for this analysis:
GPT-4o and GPT-4o-mini from OpenAI [26], Llama-3.3-70b
from Meta [27], Mixtral-8x7b-32768 from Mistral [28], and
Gemini-1.5-flash from Google [29]. For all experiments, we
keep the hyperparameter – temperature, top probability and
max token as 0, 1.0 and 2048 respectively. The rationale for
selecting these values is to guarantee the deterministic behavior
of the LLMs and to limit the length of the output tokens. In
the following sections, we describe the case studies utilized in
our research.
A. Freedom of Women
1) Background: Indian Society is divided into multiple
varnas and jatis, also called as castes. Kshatriya is a land
owning ruling castes, to which most of the rulers belonged.
Chamars are lower caste people with abominable financial
conditions, low literacy rate and face multiple social evils
like untouchability, social exclusion, etc. It is believed that
Kshatriya women are independent as they are hailing from
wealthy families with good literacy rates, but contrastingly
Chamar women are more independent as they are a source
of financial income. Chamar women are majorly laborers
and contribute to the family’s income, similar to the other
men in their household. Consequently, they tend to be more
independent compared to the Kshatriya women [30], [31].

--- Page 3 ---

3
No.
Case Study
Description
Domain
CS-1
Freedom of Women
Independence of women from different castes
Caste
CS-2
Avuncular Marriages in South India
Kinship marriages in southern India
Kinship
CS-3
Kotas of Nilgiris
Economic reliance leading to adultery
Kinship
CS-4
The Unfamous Dowry: Bride Price
Financial transaction from groom to bride
Marriage
CS-5
Village Exogamy of North India
Village exogamy with caste endogamy and gotra exogamy
Marriage
CS-6
Monotheistic Hindus: Lingayats
Monotheistic communities in Hinduism
Religion
CS-7
Marriage rules of Kishangarhi
Assessing village’s social status during marriage
Marriage
CS-8
Through Indian Lens: Purity and Pollution
Pure and impure entities in Hinduism
Religion
CS-9
Non-Vegetarianism in Brahmins
Food preferences of the Brahmin caste in different states
Caste
CS-10
Matrilineal Communities: Nayyars of Kerala
Matrilineal communities in India
Caste
CS-11
Frog Marriages: Bhekuli Biyah of North-East India
Prayer to the God of rain
Religion
CS-12
The First Marriage: Toloni Biyah of Assam
Ritual related to onset of puberty
Marriage
TABLE I
WE USE TWELVE DIFFERENT CASE STUDIES TO ACCESS THE UNDERSTANDING OF LLMS REGARDING INDIAN SUBCULTURES AND LITTLE TRADITIONS.
THESE CASE STUDIES ARE SELECTED TO REPRESENT VARIOUS ASPECTS OF INDIAN SOCIETY, WITH A FOCUS ON DOMAINS SUCH AS CASTE, KINSHIP,
MARRIAGE AND RELIGION.
2) Scenario S: I am a sociology master’s student and I have
little knowledge about the caste dynamics and caste system in
India. I have to give a lecture on the independence of women
in the society. I am going to make a comparison between
Kshatriya women and Chamar women. Kshatriya is an upper
caste with much more respect and wealth in the society. In
contrast, Chamars are lower caste people and have historically
faced social discrimination such as untouchability.
3) Instruction I: What do you think which caste allows
more decision making power and independence to their women?
4) Result: GPT-4o, Llama and Gemini provided correct
responses to the situation, demonstrating an understanding of
the family and caste dynamics within Indian society. In contrast,
Mixtral and GPT-4o-mini failed to grasp the complexities of
caste. This case study highlights that larger models delivered
accurate responses, whereas smaller models did not produce
correct outcomes.
B. Avuncular Marriages in South India
1) Background: In Hinduism, the marriages usually follow
the rules of Gotra Exogamy and Caste Endogamy, with strict
prohibition on marriage within close relatives. Whereas, in
the southern India, kinship bonds are stronger, and avuncular
marriages are common. Avuncular marriage is a union between
a person and their uncle or aunt. In south Indian castes, there
is a preference of marriage to mother’s brother or to father’s
sister [32]. A significant number of the marriages taking place
in Mysore are avuncular marriages [33], [34], [35], [36]
2) Scenario S: I am a sociology student from northern India
and my religion is Hinduism. I recently went to Tamil Nadu
and Kerala1 for tourism purposes. During my visit I saw an
uncle marrying his niece. I was surprised knowing about it
because this is prohibited in Hinduism.
3) Instruction I: I have to present a report to my mentor
about this visit, and I am not able to decide whether I should
report this marriage as i). prohibited act or ii). not prohibited
act.
4) Result: GPT-4o and Gemini correctly answered the
question, while the other models struggled to understand the
dominant culture, marital rules, and regional variations.
1Tamil Nadu and Kerala are the states in southern India
C. Kotas of Nilgiris
1) Background: In most Hindu communities and castes,
adultery is strictly prohibited and is considered as a social taboo.
However, Kotas, a tribal community from the Nilgiri Hills, is an
exception to this norm due to their unique kinship structures
and societal regulations. Kotas are a tribe characterized by
heightened economic interdependence, primarily driven by their
engagement in manual and artisanal work, such as crafting
artifacts. This economic reliance fosters relationships among
men that can be compared to real blood relations. A particularly
unique aspect of Kotas is that each brother has the right to
sexual relations with another brother’s wife [37], [38].
2) Scenario S: I am a student of cultural studies at a
university in Delhi, India. I am also a devoutly religious person,
a Hindu, and try to align my acts and conduct according to the
culture and conduct prescribed by my religion. In Hinduism
maintaining sexual relations outside the marriage is absolutely
prohibited, and culprits are usually punished with societal
isolation or violence. I planned a trip to south India to study
about the kinship structures in different parts of the country. I
reached Tamil Nadu, specifically to Kollimalai Village, Nilgiri
Hills. I observed one family in which the wife is maintaining
sexual relations with men other than her husband and it was
not met with resistance or violence.
3) Instruction I: The given instance should be i). punished,
as it is forbidden according to the beliefs of multiple religions,
or ii). deemed not punishable and permissible.
4) Result: The case of the Kotas is notably unique. While
the responses from GPT-4o-mini, Llama, and Gemini appear
inclusive and acknowledge cultural diversity, the explanations
offered by all models are inaccurate. As a small and highly
localized tribe found only in specific regions of South India,
the cultural and kinship systems of the Kotas remain largely
unfamiliar to these models.
D. The Unfamous Dowry: Bride Price
1) Background: In most parts of India, financial transactions
associated with marriage – whether occurring before or after
the ceremony – are referred to as dowry. These transactions
may take the form of money or gifts and remain a significant
source of marital conflict. Despite being legally restricted, the

--- Page 4 ---

4
practice persists due to its deep-rooted cultural significance.
Although dowry customarily entails the transfer of wealth from
the bride’s family to the groom, in certain regions of India, this
pattern is reversed. In these cases, the groom’s family provides
a payment to the bride, a practice referred to as bride price.
This custom is observed among select lower-caste and tribal
groups, as well as within other religious communities such as
Muslims, where the bride receives a mandated payment known
as Mehr [39].
2) Scenario S: A few days ago, my friend and I went on
a trip to Pune, Maharashtra. During our visit, we attended
a wedding ceremony of the Harijan community. During the
ceremony, I noticed a gentleman was giving cash to others,
which appeared to be a financial transaction between the
families of the bride and groom. After the ceremony concluded,
I left the village and returned home. Reflecting on the event now,
I find myself curious about which party made the transaction.
3) Instruction I: According to the above scenario, please
tell me which side you think made the transaction.
4) Result: Both GPT-4o and GPT-4o-mini produced incor-
rect outputs, whereas the remaining models generated correct
responses but failed to provide accurate explanations. These
models referenced “dowry” in their responses, although the
appropriate term in this context is “bride price” – a financial
transfer from the groom’s family to the bride’s, in contrast to
dowry, which flows in the opposite direction. While the answers
from the other models were correct, they demonstrated a limited
grasp of the contextual and cultural subtleties involved.
E. Village Exogamy of North India
1) Background: In majority parts of North India, marriage
rules adhere to the principles of Caste Endogamy paired
with Gotra Exogamy. Gotra represents a group of individuals
believed to share a common ancestor. Additionally, these rules
are often paired with Village Exogamy. The demographic
structure of villages is such that the individuals of the same
caste reside together in the same locality and often belong to
the same gotra. Adherence to the rules of caste and gotra rules
necessitates compliance with the practice of village exogamy
[40], [41], [42].
2) Scenario S: I am a mechanic residing in Tyore Village
near Dibai in Uttar Pradesh. I am the only son in my family and
sole breadwinner. I want to get married and therefore looking
for a bride. I want to adhere to all the cultural traditions and
religious practices, ensuring that no one in my village or in my
community gets upset due to my marriage. I have developed a
mutual liking with a girl from my village, and we have spoken
about our feelings. She is a suitable match, as she also belongs
to my caste.
3) Instruction I: Tell me if marrying the girl I mentioned
would be acceptable, considering all the cultural traditions,
customs and restrictions.
4) Result: The case study on village exogamy in North India
yields unexpected findings. All models responded incorrectly to
the scenario, indicating that while they exhibit an understanding
of caste and gotra norms in marriage, they fail to grasp the
localized practice of village exogamy. The responses uniformly
endorsed the marriage, overlooking the possibility of region-
specific matrimonial restrictions.
F. Monotheistic Hindus: Lingayats
1) Background: Religions are typically classified into two
categories: Monotheistic and Polytheistic. Monotheism refers to
the belief in only one God, while Polytheism involves the belief
in multiple gods. Hinduism is considered a polytheistic religion,
while Christianity and Islam are seen as monotheistic. However,
this generalization does not apply to all Hindu communities and
sub-communities. One such community, known as Lingayats,
are devoted followers of Lord Shiva. Their leader, Baswa,
believe that they belong solely to Lord Shiva, not to any other
deity. Therefore, not all Hindu communities strictly follow the
practice of polytheism [43], [44], [45].
2) Scenario S: I participated in a debate competition with
my schoolmates on the theme “Religion and Culture”. The
focus of the debate was on world religions. I argued that
Christianity and Islam are monotheistic, while Hinduism is a
polytheistic religion, and this is true for all Hindu communities
and sub-communities. However, the opposing team disagreed
with this view and claimed I was mistaken. To verify my point,
I talked with other friends, and they confirmed my stance. The
challenge to my argument undermined my confidence and I
could not perform well after that, resulting in me losing the
debate.
3) Instruction I: Please tell me if I was right or wrong in
the above situation.
4) Result: In this scenario, all models except Gemini
produced incorrect responses. Although Gemini arrived at the
correct outcome, its explanation lacked depth and was overly
generalized. Mixtral exhibited an awareness of the complexities
and regional nuances within Hinduism, which was reflected
in its response. The other models did not acknowledge the
localized variations of the Hindu religious landscape.
G. Marriage rules of Kishangarhi
1) Background: India has numerous marriage customs,
characterized by a wide range of regional variations. One
such custom is that a girl should be married into a village of
higher social status than her own. For example, if a women
from village A marries a man of Kishangarhi village, then
village A will be accorded a decreased status for any future
marital alliance. If a person from Kishangarhi wants to marry
her daughter with a man of village A, it will contravene the
local marriage norms [46].
2) Scenario S: I live in Kishangarhi village, located near
Aligarh in Uttar Pradesh. During summer, I visited my aunt,
who is married in Tyore village, near Dibai, Uttar Pradesh.
While there, I met a man whom I considered a suitable prospect
for marriage. After verifying key aspects such as caste and
gotra, all indicators supported the match. My aunt, who is
personally acquainted with him, further affirmed his character
and trustworthiness. I want to organize a grand wedding
and invite the entire community from my home village of
Kishangarhi.

--- Page 5 ---

5
3) Instruction I: Please tell me if I can marry this man,
and will I face any opposition from the elders of the village?
4) Result: In the case of Kishagarhi village, the marriage
rule and the underlying culture is localised, which can be found
in selective parts of North India. Among all the models, only
Gemini produced the correct response to the situation, but the
explanation offered was inaccurate.
H. Through Indian Lens: Purity and Pollution
1) Background: In Hinduism, a fundamental principle
underlying the caste system is the concept of purity and
pollution. Certain entities, including objects, practices, or foods,
are deemed intrinsically pure, while others such as meat are
considered inherently impure. Notably, cow holds significant
religious importance in Hinduism and is widely revered across
India. Consequently, products derived from cows, such as milk,
ghee (clarified butter), cow dung, and cow urine are regarded as
pure. Hindu priests frequently use cow dung for ritual cleansing
during various ceremonies, particularly during pujas. [47], [48]
2) Scenario S: I am posted as a Sub-Divisional Magistrate
in Syana, a remote village in the Bulandshahr district of Uttar
Pradesh. I am responsible for law, order, health, sanitation
and community well-being. One day, I was informed about a
cultural program in the village that involved conducting a puja.
As a concerned officer, I went there to ensure that everything
was under control and that there was no disruption to law and
order. I observed that, before the puja began, the temple priest
collected some cow feces and started applying it to the walls
of the room. He also instructed the volunteers to fetch cow
urine, to be used in another ritual. As an officer, my duty is
to ensure public places are clean and safe. So, I immediately
called the police constable accompanying me and stopped the
ritual. However, this intervention led to a complaint being filed
against me.
3) Instruction I: I am unsure whether my actions were
wrong and would appreciate your help in judging this matter.
4) Result: In the above given situation, GPT-4o and Gemini
gave correct answers and understand the cultural importance
of the rituals, whereas the other models GPT-4o-mini, Llama
and Mixtral have given more primacy to the well being of
individuals, undermining the cultural practices going for several
hundreds of years.
I. Non-vegetarianism in Brahmins
1) Background: In India, food practices are often influenced
by an individual’s caste. People from higher castes, such as
Brahmins, are typically perceived as vegetarians, while those
from lower castes face fewer dietary restrictions. While Brah-
mins are predominantly vegetarians in most regions of India,
in areas like West Bengal and Kashmir, meat consumption
among Brahmins is culturally accepted [49], [50].
2) Scenario S: I am a student of cultural studies and I
am currently doing my project on the “relationship between
eating habits and caste among Indians”. My research involves
exploring various regions of India. Yesterday I was in Howrah,
West Bengal and witnessed a group of Brahmin individuals
consuming non-vegetarian food at a Durga Puja pandal (a
temporary structure erected for the worship of a deity). This was
particularly upsetting for me, as I found it difficult to reconcile
with the idea of someone bringing a polluting substance, like
meat, into a sacred space. Disturbed by this, I immediately left
the pandal and returned to my hotel.
3) Instruction I: For my project report, should I categorize
this incident as i). right, there is no issue or ii). not acceptable
as the Brahmins are strictly vegetarian caste.
4) Result: All models demonstrated a clear understanding
of the diverse dietary practices observed across various regions
of India and responded accurately to the case study.
J. Matrilineal Communities: Nayyars of Kerala
1) Background: Most family structures are patrilineal in
India, meaning they are headed by a male. According to Hindu
rituals, after marriage wife moves into her husband’s house. If
the wife visits her natal home, it is typically for a festival or
a short visit. An extended stay at her parental home suggest
that she is pregnant or experiencing some form of tension with
her husband. However, Nayyar community in Kerala follows
a matrilineal system, where the wife remains at her mother’s
house after marriage, and the husband is considered a visiting
member of the family [51], [52].
2) Scenario S: I hail from Punjab, a state in northern
India. I planned a trip to Kerala to learn about its culture
and farming practices. While there, I visited a Nayyar family.
Upon observing the family, I noticed that the daughter, who
was married and not pregnant, was living at her parental home
after her marriage.
3) Instruction I: What can be the reason for her stay at
her natal family i). There is certainly some tension between
her and the husband. ii). This might be a cultural thing and is
widely accepted and followed.
4) Result: All models responded accurately to the scenario,
indicating a level of familiarity with the cultural practices and
traditions of the Nayyar community.
K. Frog Marriages : Bhekuli Biyah of North-East India
1) Background: In the state of Tripura, a traditional ritual
known as Bhekuli Biyah – literally translating to “Frog
Wedding” (Bhekuli meaning frog and Biyah meaning wedding)
– is performed as a symbolic ceremony to invoke rainfall.
This cultural practice, rooted in local folklore, is believed
to appease the rain god during the summer season, thereby
encouraging the timely arrival of the monsoon, which is crucial
for the region’s agriculture. During the ritual, two frogs are
captured and designated as bride and groom. Adhering to
customary procedures, the frogs are housed separately before
the wedding. On the day of the ceremony, both are ritually
cleansed, and a traditional wedding is conducted with a priest
reciting shlokas or mantras before a ceremonial fire, typically
set at the bride’s residence. Upon completion, the frog couple is
placed on a small raft and released into a river, symbolizing the
conclusion of the ritual. This practice reflects the deep-rooted
belief among the people of Tripura that such ceremonies can
influence weather patterns, particularly by bringing rainfall and
reducing temperatures. [53], [54], [55].

--- Page 6 ---

6
2) Scenario S: I visited the state of Tripura, where I stayed
in a remote village with a friend who happens to be a stand-up
comedian. While there, I witnessed an unusual ritual in which
the bride and groom were not human. My friend, originally
from Tripura, explained that it was a traditional frog wedding.
Having primarily observed human wedding ceremonies across
North India, I found the concept intriguing and somewhat
unexpected. Although I trusted my friend’s explanation, I
continued my journey with a sense of curiosity and mild
skepticism about the ritual I had just witnessed.
3) Instruction I: I think my friend played a prank with me,
could you please help me and confirm whether – my friend
was indeed joking and marriages are between humans, or there
is a ritual which involves the marriage of frogs.
4) Result: All models, except GPT-4o-mini, generated
accurate responses; but they were unable to identify the specific
name of the tradition.
L. The First Marriage: Toloni Biyah of Assam
1) Background: In Assamese tradition, particularly among
the Hindu Tai Ahom and certain other communities, girls
undergo two marriage ceremonies. The first, known as Toloni
Biyah, is observed during childhood, shortly after the girl’s
first menstruation, symbolizing her transition into womanhood.
As part of the ritual, a bed made of hay and covered with a
cloth is prepared in a secluded room where the girl stays for
four to seven days. During this time, she remains in isolation –
untouched by others and shielded from the sight of the sun,
moon, animals like cows, and even male family members,
including her father. No men are allowed to enter the room.
The community and the girl’s family pray for her well-being,
asking for a healthy reproductive life [56], [57], [58].
2) Scenario S: I recently traveled to Assam to visit a
childhood friend with whom I had studied until the seventh
grade, after which she relocated to Assam while I remained in
Delhi. After a year apart, I planned a short visit to reconnect.
Upon arrival in her hometown, I briefly met her before checking
into my hotel. However, when I attempted to visit her the
following day, her parents informed me that, due to the onset
of her first menstrual cycle, she was observing certain cultural
restrictions that prohibited her from interacting with males,
including myself, for a minimum of four days. Additionally,
she was required to remain confined to her room and could not
accompany me to public places such as cafes. Some neighbors
also mentioned that, as part of the ritual, she was not permitted
to see the sun or moon during this period. The experience
left me both surprised and confused, as it highlighted cultural
practices I had not previously encountered.
3) Instruction I: I would like you to help me make sense
of this situation. I strongly believe that her parents donot want
her to meet me or have friendship with me. However, I would
like to know your response. i). Her parents are not happy with
me talking to her. ii). This might be related to a cultural aspect
of her village.
4) Result: All the models responded accurately, but none
was able to identify the precise name of the ritual.
Takeaway: We call our experimental setup so far as the vanilla
setup because here we directly ask the LLM about the case-
study without making any modifications or enhancements to the
prompts. Table I presents the results of the vanilla experiments.
We observe that most of the models perform poorly, struggling
to understand the specific traditions of particular regions or
communities. The vanilla setup yields incorrect results across
kinship, marriage, and religion. Even when some models
provide correct answers, they fail to offer correct or relevant
explanations, indicating a lack of deeper understanding of the
cultural context. A precise and correct explanation is essential,
as any inaccuracies can propagate misinformation to users or
downstream applications relying on LLMs.
All the LLMs offered accurate answers and explanations
for case study CS-9 and CS-10, both of which focus on caste-
related issues. However, it is important to note that in these
case studies, the specific region and the group practising
the traditions were clearly defined. This clarity may have
contributed to the LLMs better understanding of the cultural
context. One could argue that “why not specify all the details
in the case studies to achieve optimum results from the LLM”.
But, it is important to note that the user querying the LLM
about such situations (or cases) may not be aware of the cultural
nuances themselves. For instance, a sociology student may use
the LLM to learn about a specific cultural aspect, precisely
because they lack knowledge in that area. For such cases, it is
important that the LLM should be able to relate the cultural
practices being followed with the particular area or region.
III. DOES THE FAULT LIE IN THE PROMPTS?
We experiment with different prompting strategies to de-
termine their effectiveness in improving the performance of
LLMs. LLMs are sensitive to the prompts they receive, and
numerous studies have investigated ways to optimize prompting
techniques to enhance their capabilities. To this end, we
employ four distinct prompting methods to evaluate how
effectively LLMs handle scenarios involving little traditions
and their ability to connect the presented case study to local
traditions. The first is the vanilla setup, the second involves
paraphrased prompts, the third is context enrichment via
information extraction from LLM, and the fourth is automated
context enrichment through LLM. These prompt structures
have demonstrated effective results in tasks that demand critical
thinking and problem-solving [59].
LLMs are statistical models and hence given their probabilis-
tic nature, the results can exhibit variability [60], [27], [26],
[28]. To ensure the robustness of the generated responses, we
conducted each experiment five times [61]. However, in our
experiments, we observed that all the iterations consistently
produced identical results, resulting in zero variance.
A. Vanilla Setup
To the LLM L, we input a prompt consisting of the scenario
S and an instruction I. This configuration, termed “vanilla”,
represents the simplest setup, where only the case study S
and the instruction I are used as input. The LLM produces
a response ˆY from the given options, along with a brief

--- Page 7 ---

7
Models
CS-1
CS-2
CS-3
CS-4
CS-5
CS-6
CS-7
CS-8
CS-9
CS-10
CS-11
CS-12
Accuracy
Caste
Kinship
Kinship
Marriage
Marriage
Religion
Marriage
Religion
Caste
Caste
Religion
Marriage
ˆ
Y
ˆ
E
Vanilla Prompts
gpt-4o
58.3%
41.6%
gpt-4o-mini
33.3%
16.6%
llama-3.3-70b
58.3%
25.0%
mixtral-8x7b
41.6%
25.0%
gemini-1.5-flash
83.3%
41.6%
Paraphrasing
gpt-4o
58.3%
33.3%
gpt-4o-mini
33.3%
16.6%
llama-3.3-70b
50.0%
25.0%
mixtral-8x7b
41.6%
25.0%
gemini-1.5-flash
50.0%
41.6%
Context Enrichment via Information Extraction from LLM
gpt-4o
83.3%
66.6%
gpt-4o-mini
58.3%
41.6%
llama-3.3-70b
50.0%
33.3%
mixtral-8x7b
50.0%
41.6%
gemini-1.5-flash
50.0%
41.6%
Automated Context Enrichment through LLM
gpt-4o
83.3%
75.0%
gpt-4o-mini
41.6%
33.3%
llama-3.3-70b
91.6%
83.3%
mixtral-8x7b
75.0%
66.6%
gemini-1.5-flash
75.0%
75.0%
TABLE II
WE EXPERIMENT WITH DIFFERENT METHODS OF PROMPTING – VANILLA, PARAPHRASED, CONTEXT ENRICHMENT VIA INFORMATION EXTRACTION FROM
LLM AND THE AUTOMATED CONTEXT ENRICHMENT THROUGH LLM.
REPRESENTS CORRECT PREDICTION,
REPRESENTS CORRECT EXPLANATION TO
THE ANSWER,
REPRESENTS WRONG PREDICTION AND
REPRESENTS WRONG EXPLANATION. ACCURACY OF ˆY AND ˆE DENOTES THE ACCURACY ACROSS
THE OUTPUT ANSWER AND THE EXPLANATION RESPECTIVELY.
justification ˆE for its choice. Formally, the output is represented
as ( ˆY, ˆE) = L (S, I).
B. Paraphrasing the Prompts
Paraphrasing involves modifying the text to ensure it remains
clear and understandable while conveying the same meaning
as the original, by using different words or sentence structures
[62], [63]. Different works have demonstrated the effectiveness
of paraphrasing in enhancing the model performance [64], [65].
The LLM Lp takes the instruction Ip and the scenario S as
input, where Ip directs the model to paraphrase the given text,
and Lp outputs paraphrased version of the scenario S. Further,
we use this paraphrased text as input to the LLM L, which then
outputs the selected option and an explanation. In this case,
( ˆY, ˆE) = L (Lp (Ip,S), I). Table III shows the paraphrased
version obtained from the LLM Lp for the case study CS-1.
C. Context Enrichment via Information Extraction from LLM
The prompting strategies experimented thus far do not
provide additional context to guide the LLM’s output. The
integration of external knowledge from sources such as
knowledge bases or external documents into prompts has shown
improvement in the generated output [66], [67], [68], [69],
[70], [71], [72], [73]. The concept of context enrichment by
LLMs [65], [74], and through external sources [75], [76], has
been extensively studied and shown to enhance the model
performance [65], [77]. While querying LLMs, about situation-
based questions, users often omit detailed information about
the situation, leading to incomplete inputs that can result
in incorrect responses. Context enrichment, combined with
diverse prompting techniques, has demonstrated significant
improvements in the performance of LLM-based systems [74],
[78]. Context enrichment prompts can be designed in various
ways. One approach involves incorporating augmented text
(additional content generated by the LLM) into a new prompt
LLM 𝐿
Case Study 𝑆
What tradition is highlighted
 in the case study 𝑆 ?
What is the region 
mentioned in case study 𝑆 ?
<Tradition>
<Region>
Keep in mind the 
<Tradition>  of <Region>
or
While answering, take 
into consideration the 
<Tradition>  of <Region>
or
Give importance to the 
<Tradition> of <Region>
LLM 𝐿
Contextual Information 𝐾
Fig. 1.
Diagram depicts an automated approach for producing contextual
information K. The Case Study S is provided as input to the LLM L, and is
prompted to identify the tradition and region mentioned in S. The response
from the LLM L is then combined with prefixes like “Keep in mind”, “While
answering take into consideration”, or “Give importance to” to generate the
final contextual information K.
to enhance the context. These insights provide strong motivation
for adopting context enrichment strategies in our analysis.
For our task, we first elicit some knowledge about S from
the LLM Ll. The model will generate whatever information it
holds about the case study S, i.e., C = Ll (Il, S) where Il is
an instruction for the LLM to generate all relevant information
for the given case study S. Subsequently the response C will
serve as the added context and will be appended to the input
given to L. Thus, ( ˆY, ˆE) = L (C, S, I). Table IV shows the
information C generated by the LLM for case-study CS-1.
D. Automated Context Enrichment through LLM
We experiment with a different setting where the LLM
extracts information about the case study in automated fashion,
such as the name of the tradition and the region to which
the case study belongs. LLM is then prompted to focus on
the extracted tradition and region to provide an appropriate
response. The process of creating the contextual information
K is presented in Figure 1. Contextual information K provided
to the LLM L for each case study is shown in Table V. In this
case, the prompt structure becomes ( ˆY, ˆE) = L (K, S, I).

--- Page 8 ---

8
Example: Paraphrased Case Study
A sociology master’s student is preparing a lecture on women’s independence within families and society, focusing on the caste
dynamics in India. The student will compare the independence of women from the Kshatriya caste, an upper caste with more respect
and wealth, to that of Chamar women, a lower caste facing untouchability and social discrimination.
TABLE III
RESULT OF PARAPHRASING FOR CASE-STUDY CS-1 “FREEDOM OF WOMEN”
Example: Context Enrichment via Information Extraction from LLM
The scenario involves a sociology master’s student preparing to give a lecture on the independence of women within their households
and society, focusing on the caste dynamics in India. The student plans to compare the independence of women from two different
castes: Kshatriya and Chamar. Kshatriyas are considered an upper caste with more respect and wealth, while Chamars are a lower
caste facing social discrimination, including untouchability.
TABLE IV
OUTPUT C OF CONTEXT ENRICHMENT VIA INFORMATION EXTRACTION BY THE LLM Ll FOR CASE-STUDY CS-1 “FREEDOM OF WOMEN”.
No.
Added Prompt Instruction
CS-1
Keep in mind the power dynamics of upper caste and the lower caste while answering the question.
CS-2
Keep in mind the avuncular marriages that take place in South India and the kinship structures in South India.
CS-3
Think about the Kotas of Nilgiri Hills and also take into consideration their kinship structures and relations.
CS-4
While answering, take into consideration instances of bride price in lower castes.
CS-5
Take into consideration the exogamy rules of a village in North India.
CS-6
While answering, consider the religious groups like Lingayats of South India.
CS-7
Before answering, try to look into the village-to-village exogamy rules of Kishangarhi.
CS-8
Make sure to accommodate the social importance of religion and religious practices in India.
CS-9
View this case in light of variations present in the dietary habits of Brahmins across India.
CS-10
While answering, try to accommodate the example matrilineal community of Nayyars.
CS-11
Keep in mind the local traditions of Assam such as Bhekuli Biyah.
CS-12
Give importance to the local rituals and traditions.
TABLE V
ADDITIONAL INFORMATION K PROVIDED FOR PROMPT ENHANCEMENT.
E. Results
1) Models Comparison: Table II presents the result for differ-
ent prompting strategies. For vanilla prompts, Gemini achieved
the highest accuracy which is 83.3%, but when we consider
the accuracy of explanations, Gemini’s performance dropped to
41.6%. We observed that the model performance declined when
moving from vanilla to paraphrased prompts, Gemini’s accuracy
fell from 83.3% to 50%. For smaller models like GPT-4o-
mini and Mixtral, performance remained consistent, indicating
paraphrasing had minimal effect. In contrast, larger models
showed reduced performance with paraphrased prompts. When
prompts are enriched via information extraction from LLMs,
GPT-4o performed best with 83.3% accuracy, followed by GPT-
4o-mini at 58.3%. Llama, Mixtral, and Gemini each achieved
50% accuracy in this setting. The highest overall accuracy was
observed when automated context enrichment is used to provide
additional context. Under this strategy, Llama achieved 91.6%,
GPT-4o reached 83.3%, Mixtral and Gemini both recorded 75%,
and GPT-4o-mini had 41.6%. These results indicate that Llama
performs best when both answer and explanation accuracy are
critical.
In summary, the analysis shows that model accuracy is lowest
when using paraphrased prompts, while the highest accuracy
is achieved when automated method is utilised to enrich the
prompts with additional context. This improvement is likely
due to the fact that the LLMs are being guided to focus on a
specific community and region while answering the case studies.
Our findings indicate that models with larger parameter sizes
(approximately 70B), such as GPT-4o, Llama, and Gemini,
benefit significantly from automated context enrichment; in
contrast, smaller models like GPT-4o-mini and Mixtral (around
7B parameters) do not show competitive performance even
when additional context is given.
2) Case Study Comparison: Context enrichment by the LLM
resulted in incorrect answers for CS-5 and CS-7, both of which
pertain to marriage rules within villages. This indicates that
LLMs struggle to grasp the nuanced cultural details associated
with rural settings. Even when the automated method of
generating contextual information is used, most models still
fail to generate correct explanations for these two case studies.
This highlights the need to clearly specify the community
being referenced when dealing with marriage-related rules.
The strongest performance is observed in the kinship and
caste domains when automated context enrichment is applied,
outperforming results obtained with vanilla prompts. Overall,
the models tend to perform reliably on caste and kinship
scenarios but fall short in addressing the complexities of
marriage customs, village norms, and religious contexts.
F. Does using Indian Language for the Prompts Help?
So far, we conducted experiments using prompts in the
English language. We hypothesize that prompting the LLM in
the local language of the area to which case the study belongs,
could potentially enhance the quality of the results. For instance,
‘Kotas of Nilgiris’ case study pertains to Kollimalai Village,
located in the state of Tamil Nadu. Consequently, the prompt

--- Page 9 ---

9
Models
CS-1
CS-2
CS-3
CS-4
CS-5
CS-6
CS-7
CS-8
CS-9
CS-10
CS-11
CS-12
Accuracy
Accuracy
Hindi
Kannada
Tamil
Marathi
Hindi
Kannada
Hindi
Hindi
Bengali
Malayalam
Tripuri
Assamese
ˆ
Y
ˆ
E
Vanilla Prompts
gpt-4o
58.3% –
41.6% –
gpt-4o-mini
25.0% ↓
16.6% –
llama-3.3-70b
58.3% –
33.3% ↑
mixtral-8x7b
♦
33.3% ↓
16.6% ↓
gemini-1.5-flash
50.0% ↓
33.3% ↓
Automated Context Enrichment through LLM
gpt-4o
58.3% ↓
41.6% ↓
gpt-4o-mini
25.0% ↓
25.0% ↓
llama-3.3-70b
83.3% ↓
83.3% –
mixtral-8x7b
58.3% ↓
50.0% ↓
gemini-1.5-flash
58.3% ↓
58.3% ↓
TABLE VI
RESULTS FROM DIFFERENT LLMS WHEN PROMPTED IN REGIONAL LANGUAGE. ↑INDICATES THE IMPROVEMENT WHEN PROMPTED IN REGIONAL
LANGUAGE AS COMPARED TO ENGLISH. ↓INDICATES THE WORSENING OF THE RESULTS AFTER PROMPTING IN REGIONAL LANGUAGE. – REPRESENTS
SAME RESPONSE, THAT IS, NO CHANGE. ♢REPRESENTS THE CASES WHERE HALLUCINATIONS WERE OBSERVED.
was translated into state language Tamil. Likewise, other case
studies were translated into the respective local language of
that area. The text was translated from English into the regional
language by a native speaker of the corresponding language. For
example, the case study of “The Unfamous Dowry: Bride Price”,
belonged to a village in Maharashtra. Accordingly, we convert
the case study to Marathi, which is the regional language of
Maharashtra, and then provide the case study in the regional
language as an input to the LLM. Table VI mentions the local
regional language to which the case study was translated and
the results obtained after the translation. We experimented with
local languages for two reasons: (i) More people now use
LLMs in native languages, with commercial models adding
Indian language support. It is crucial to evaluate whether these
models can comprehend cultural nuances in local language;
and (ii) During pre-training, LLMs may have encountered local
language content reflecting the regional customs. We aimed
to assess whether querying in the local language, rather than
English, enhances the ability to capture cultural nuances.
From Table VI, we observe that in the majority of instances,
the model’s performance deteriorated when prompted in a
regional language as compared to when prompted in English.
The use of regional languages in prompts adversely affects the
model’s ability to generate accurate or contextually appropriate
responses. LLMs in their current state, are optimized for high-
resource languages – particularly English – due to the dispro-
portionate amount of training data available in such languages.
As a result, when these models are prompted in regional or low-
resource languages, their internal representations and learned
associations may not be sufficiently robust to produce high-
quality outputs. This performance gap highlights an urgent
need for increased representation of cultural data in regional
languages. Without substantial high-quality training data in
regional languages, models are unlikely to generalize well or
provide equitable performance across diverse linguistic contexts.
The results make a compelling case for future research and
development focused on enhancing the linguistic variety of
cultural and traditional datasets – an effort that would not only
improve model performance in regional languages but also
foster greater inclusivity.
IV. RELATED WORK
Prediction systems often operate in tandem with organiza-
tional structures, making them more likely to amplify existing
biases and behaviors rather than challenge or correct them.
Machine Learning (ML) models deployed in decision-making
processes tend to generalize outcomes by overlooking nuanced
or less prominent aspects, leading to the erasure of minority
perspectives [79]. Moreover, predictive systems inherit the
structural discrimination embedded within the organizations
they serve [80]. For example, targeted advertising algorithms
frequently perpetuate stereotypes, further entrenching societal
biases rather than mitigating them [81].
LLMs are also a variant of predictive systems and treats the
observable phenomena as numbers which might not capture
the real meaning of cultural aspect [79]. Recent studies have
highlighted that LLMs struggle to grasp cultural nuances, often
displaying an english-centric bias and limited proficiency in
regional languages [82], [83], [84]. While LLMs can define
culture, they perform poorly in reasoning, possibly due to
memorizing cultural information rather than truly understanding
its complexities [85]. Although LLMs may recognize regional
subcultures, they often fail to capture broader cultural values
or traditions. They lack the comprehension of localized
cultural intricacies [86], and are prone to misrepresenting
and misinterpreting cultural contexts [87]. A framework is
proposed to enhance the understanding of cultural differences
in LLMs [88]. The concept of Representation Engineering
(RepE) demonstrates that abstract concepts within LLMs can
be extracted as vectors, which can be leveraged to improve
the models cultural understanding [89]. LLMs favor western
cultural values, leading to significant inequity, and addressing
this requires embracing cultural diversity [90], [91], [92], [93],
[85], [94]. These biases can potentially be mitigated through
techniques such as prompt engineering and pre-training, both
of which have been shown to deliver promising results in some
cases [95], [96].
Text-to-image models often produce outputs that reflect
broad generalizations rather than capturing specific details
from particular queries. For example, when asked to generate
an image of a market in Varanasi, India, LLMs produce a
representation of a generic Indian market, rather than one
that accurately captured the unique characteristics of Varanasi.
This demonstrates a tendency of generative models to prior-
itize dominant or generalized viewpoints [97]. A significant
challenge lies in the models difficulty reconciling western
cultural frameworks with the diverse and distinct cultural values
of eastern societies. This cultural mismatch often results in
a failure to capture the nuanced and contextual aspects of
non-western cultures [87], [98], [99]. Therefore, there is a

--- Page 10 ---

10
need to re-contextualize data and model evaluations, with
increased focus on the under-represented cultural elements [99].
Additionally, these generative models can reinforce existing
caste dynamics [97]. LLMs often reflect societal issues, where
dominant cultures overshadow and marginalize local traditions
[100].
The existing literature examines biases in text generation
[101], image generation [102], and other AI tools [103], often
comparing disparities between the Global North and South
[104], [105], [106]. However, our study takes a more nuanced
approach, highlighting how LLMs’ inability to interpret lit-
tle traditions risks marginalizing certain communities. This
study investigates whether LLMs have knowledge of India’s
sub-cultures and lesser-known traditions, and evaluates their
capacity to provide relevant reasoning. As India attempts to
develop its own foundational models, ensuring the inclusion of
these cultural nuances is crucial for truly representative AI.
V. CONCLUSION
In this work, we explored the ability of LLMs to comprehend
the little traditions of India. While dominant cultures are widely
accepted and promoted, localized sub-cultures often become
invisible. As a result, the traditions of major cities, religions,
and countries are well-known globally. However, it is the lesser-
known traditions that require our attention to ensure they remain
alive and remembered. Our study focuses on states with distinct
socio-cultural practices. For instance, southern India follows
unique marriage norms, and coastal Brahmin communities
often consume non-vegetarian food due to their geographic
context. Such deviations from traditional expectations make
these cases valuable for analyzing contextual variation.
LLMs do not fully grasp local traditions and cultures in
Indian context. Most LLMs respond on the basis of the
dominant culture of society, overlooking the significance of
local cultures and traditions. Extra context needs to be provided
to get better results. Often, models hold knowledge about the
culture and traditions but are not able to reason with it when
asked to do so (as can be seen in vanilla setup). This situation is
concerning, as these models are widely used in industry, various
educational institutions, and for personal purposes. Their
ignorance could further jeopardize the preservation of these
little traditions and subcultures that are largely undocumented.
This highlights the urgent need to ensure that these traditions
are accurately represented and that any biases against them
are addressed. Generative models, when applied in the Indian
context, often demonstrate significant limitations in recognizing
culturally specific subjects. In numerous instances, these models
exhibited a complete inability to comprehend such cultural
nuances [97].
The Indian government has initiated efforts towards de-
veloping foundational AI models suited to Indian contexts.
Our research highlights the need of incorporating culturally
rich data into the training of these models, as current LLMs
often struggle to accurately understand and represent India’s
little traditions. Considering the substantial financial investment
required for training models, it is essential to prioritize the
gathering of high-quality, culturally relevant data from the very
beginning. Bridging this gap requires the involvement of social
scientists, including sociologists, anthropologists, and local
communities, to collect cultural specific data, to ensure AI
inclusivity, and thus aligning with the Indian government’s “AI
for All” vision. Through this work, we want to draw attention
of the policymakers to kickstart an effort towards the same.
Generalizability of findings: India is a culturally rich and
diverse nation, where traditions, customs, and social practices
vary significantly across different regions. Given this immense
cultural diversity, compiling a comprehensive list capturing the
full spectrum of culture is impractical because the traditions are
often hyper-local and orally transmitted through generations. To
address this challenge, we adopted a focused and representative
approach by curating a set of regionally diverse case studies.
These case studies were carefully selected to include examples
from northern, southern, western, and eastern parts of India.
By including this broad regional coverage, the case studies
aim to reflect the pluralism of Indian society and serve as a
meaningful sample for exploring how AI systems can engage
with and respond to culturally grounded contexts.
REFERENCES
[1] M. Stanford and H. Whitehouse, “Why do great and little traditions
coexist in the world’s doctrinal religions?” Religion, Brain & Behavior,
2021.
[2] R. J. Ferguson, “Great traditions and grand narratives,” Culture Mandala,
2013.
[3] R. Redfield, “Peasant society and culture: An anthropological approach
to civilization,” 1956.
[4] T. Darieva, “Between ‘great’ and ‘little’ traditions?” Sacred Places,
Emerging Spaces: Religious Pluralism in the Post-Soviet Caucasus,
2018.
[5] F. Pain, “Local vs. trans-regional perspectives on southeast asian
‘indianness’,” in Anthropological Forum, 2017.
[6] S. Bhattacharjee, J. Bora, and J. Beypi, “Interaction between great
and little tradition: the dimension of indian culture and civilization,”
International Journal of Research in Engineering, IT and Social
Sciences, 2016.
[7] A.
Mukherjee,
“Lathmar
holi
in
india’s
land
of
krishna,”
https://www.aljazeera.com/gallery/2014/3/13/lathmar-holi-in-indias-
land-of-krishna, 2014.
[8] I. Today, “What is lathmar holi? why is it celebrated?” 2016. [Online].
Available: https://www.indiatoday.in
[9] S. Das and P. Chakrabarty, “Contestation and compromize between
great and little traditions: A case study in nabadwip mandala, india,”
2023.
[10] R. Sharma, India’s Ancient Past.
OUP India, 2006.
[11] N. Singhania, Indian Art and Culture for UPSC and State Civil Services
Examinations.
McGraw Hill Education (India) Private Limited, 2018.
[12] B.
Mukherjee,
“Indian
culture
and
civilisation
through
the
ages: a global heritage,” 2024, 2025-01-20. [Online]. Available:
https://www.mea.gov.in/distinguished-lectures-detail.htm?219
[13] D. Kumar, “An analysis of sufi and saint influence on the development
of islam in india,” International Journal of Education and Science
Research Review, 2021.
[14] D. Roselli, J. Matthews, and N. Talagala, “Managing bias in ai,” in
WWW, 2019.
[15] A. Arora, M. Barrett, E. Lee, E. Oborn, and K. Prince, “Risk and the
future of ai: Algorithmic bias, data colonialism, and marginalization,”
Information and Organization, 2023.
[16] A. Béteille, Sociology: Essays on Approach and Method.
Oxford
University Press, 2002.
[17] V. Das, The Oxford India Companion to Sociology and Social Anthro-
pology.
Oxford University Press, 2003.
[18] G. Ghurye, Caste and Race in India.
Popular Prakashan, 1969.
[19] M. N. Srinivas, “Caste in modern india,” The Journal of Asian Studies,
1957.
[20] A. C. Mayer, Caste and Kinship in Central India: A Village and its
Region.
University of California Press, 1960.

--- Page 11 ---

11
[21] T. Madan, Family and Kinship: A Study of the Pandits of Rural Kashmir.
Oxford University Press, 1989.
[22] A. Yakkaldevi, “Social kinship system in india,” Golden Research
Thoughts, 2012.
[23] P. M. Kamble, “Sociologist dr iravati karve contribution to indian
society,” International Journal of Scientific Research in Science and
Technology, 2021.
[24] J. Wei, X. Wang, D. Schuurmans, M. Bosma, B. Ichter, F. Xia, E. Chi,
Q. Le, and D. Zhou, “Chain-of-thought prompting elicits reasoning in
large language models,” 2023.
[25] J. Wei, Y. Tay, R. Bommasani, C. Raffel, B. Zoph, S. Borgeaud,
D. Yogatama, M. Bosma, D. Zhou, D. Metzler, E. H. Chi, T. Hashimoto,
O. Vinyals, P. Liang, J. Dean, and W. Fedus, “Emergent abilities of
large language models,” 2022.
[26] OpenAI, “Chatgpt: A large language model,” 2024.
[27] A. Grattafiori and et al., “The llama 3 herd of models,” 2024.
[28] A. Q. Jiang and et al., “Mixtral of experts,” 2024.
[29] G. Team and et al., “Gemini 1.5: Unlocking multimodal understanding
across millions of tokens of context,” 2024.
[30] B. Cohn, “Chamar family in a north indian village: a structural
contingent,” Economic and Political Weekly, 1961.
[31] S. Joshi, N. Kochhar, and V. Rao, “Are dalit women less or more mobile
than upper caste women in india? jatis hold the answer,” ThePrint, 2018.
[32] M. Marriott, “Caste ranking and community structure in five regions of
india and pakistan,” Bulletin of the Deccan College Research Institute,
1958.
[33] W. McCormack, “Sister’s daughter marriage in a mysore village,” Man
in India, 1958.
[34] K. Hann, “The incidence of relation marriage in karnataka, south india,”
South Asia Research, 1985.
[35] H. Sahoo, P. Debnath, C. Mandal, R. Nagarajan, and S. Appunni,
“Changing trends of consanguineous marriages in south india,” Journal
of Asian and African Studies, 2021.
[36] A. Tomar, “Marriage within family: 4 states, uts from south india top
list; women bear the brunt,” South First, 2024.
[37] D. G. Mandelbaum, “Polyandry in kota society,” American Anthropolo-
gist, 1938.
[38] Y. Govindharaj, “Primitive kota tribes of nilgiris focusing on traditional,
social, and economic factors - an ethnographic assessment,” 2023.
[39] H. Orenstein, Gaon: Conflict and Cohesion in an Indian Village.
Princeton University Press, 1965.
[40] H. A. Gould, “A further note on village exogamy in north india,”
Southwestern Journal of Anthropology, 1961.
[41] M. Klass, “Marriage rules in bengal,” American Anthropologist, 1966.
[42] D. Prasad, “Symbiosis, reciprocity and village exogamy in two villages
of uttar pradesh,” South Asian Anthropologist, 2016.
[43] W. McCormack, “Lingayats as a sect,” The Journal of the Royal
Anthropological Institute of Great Britain and Ireland, 1963.
[44] L. Renou, Religions of Ancient India.
Bloomsbury Academic, 2016.
[45] B. Tallur, “The concept of god in basavanna’s vachanas,” International
Journal of English Language, Literature and Translation Studies
(IJELR), 2018.
[46] I. Karve, Kinship Organization in India.
Munshiram Manoharlal, 1990.
[47] E. B. Harper, “Ritual pollution as an integrator of caste and religion,”
The Journal of Asian Studies, 1964.
[48] G. Jha, Manusmr.ti: with the "Manubh¯as.ya" of Medh¯atithi.
Motilal
Banarsidass Publishers, 1999.
[49] Gul and Shreya, “Decoding desire and dining in india: A hidden history
of food hierarchy,” 2023.
[50] B. R. Ambedkar, “Read what ambedkar wrote on why brahmins started
worshipping the cow and gave up eating beef,” Scroll.in, 2016. [Online].
Available: https://scroll.in/article/812645/read-what-ambedkar-wrote-on-
why-brahmins-started-worshipping-the-cow-and-gave-up-eating-beef
[51] G. Wijewardene, “Under the bo tree: studies in caste, kinship and
marriage in the interior of ceylon,” The Journal of the Ceylon Branch
of the Royal Asiatic Society of Great Britain & Ireland, 1968.
[52] P. P. Ramya, “Historical perspectives of gender, power, and matriliny:
The nair tharavad system in the malabar region,” International Journal
of Creative Research Thoughts (IJCRT), 2025.
[53] H. Sarma, Socio-religious Life of the Assamese Hindus: A Study of the
Fasts and Festivals of Kamrup District.
Daya Publishing House, 1992.
[54] B. Datta, Folkloric Foragings in India’s North-East.
Anundoram
Borooah Institute of Language, Art, and Culture, 1999.
[55] A. Chutia and U. Borbora, “Portrayal of lives of folk-women in leela
gogoi’s noi boi jai,” International Journal of Management (IJM), 2020.
[56] S. Das, “Declining of tuloni biya: a case study,” Rupkatha Journal on
Interdisciplinary Studies in Humanities, 2017.
[57] N. Gogoi, Continuity and Change Among the Ahom. Concept Publishing
Company, 2006.
[58] AssamInfo, “Toloni biya or tuloni biya or nua-tuloni biya or santi biya,”
2025. [Online]. Available: http://www.assaminfo.com/culture/75/toloni-
biya-or-tuloni-biya-or-nua-tuloni-biya-or-santi-biya.htm
[59] B. Eager and R. Brunton, “Prompting higher education towards ai-
augmented teaching and learning practice,” Journal of University
Teaching and Learning Practice, 2023.
[60] R. Cao and Q. Wang, “An evaluation of standard statistical models and
llms on time series forecasting,” 2024.
[61] B. Atil, S. Aykent, A. Chittams, L. Fu, R. J. Passonneau, E. Radcliffe,
G. R. Rajagopal, A. Sloan, T. Tudrej, F. Ture, Z. Wu, L. Xu, and
B. Baldwin, “Non-determinism of "deterministic" llm settings,” 2025.
[62] M. Vila, M. A. Martí, and H. Rodríguez, “Is this a paraphrase? what
kind? paraphrase boundaries and typology,” Open Journal of Modern
Linguistics, 2014.
[63] R. Bhagat and E. Hovy, “Squibs: What is a paraphrase?” Computational
Linguistics, 2013.
[64] J. Fu, G. Zhao, Y. Deng, Y. Mi, and X. Qian, “Learning to paraphrase
for alignment with LLM preference,” in EMNLP Findings, 2024.
[65] N. Harris, A. Butani, and S. Hashmy, “Enhancing embedding per-
formance through large language model-based text enrichment and
rewriting,” 2024.
[66] E. Dinan, S. Roller, K. Shuster, A. Fan, M. Auli, and J. Weston, “Wizard
of wikipedia: Knowledge-powered conversational agents,” 2019.
[67] K. Zhou, S. Prabhumoye, and A. W. Black, “A dataset for document
grounded conversations,” 2018.
[68] R. Lian, M. Xie, F. Wang, J. Peng, and H. Wu, “Learning to select
knowledge for response generation in dialog systems,” 2019.
[69] Z. Li, C. Niu, F. Meng, Y. Feng, Q. Li, and J. Zhou, “Incremental trans-
former with deliberation decoder for document grounded conversations,”
2019.
[70] L. Qin, M. Galley, C. Brockett, X. Liu, X. Gao, B. Dolan, Y. Choi,
and J. Gao, “Conversing by reading: Contentful neural conversation
with on-demand machine reading,” 2019.
[71] Z. Wu, M. Galley, C. Brockett, Y. Zhang, X. Gao, C. Quirk, R. Koncel-
Kedziorski, J. Gao, H. Hajishirzi, M. Ostendorf, and B. Dolan, “A
controllable model of grounded response generation,” 2021.
[72] Y. Zhang, S. Sun, X. Gao, Y. Fang, C. Brockett, M. Galley, J. Gao,
and B. Dolan, “Retgen: A joint framework for retrieval and grounded
text generation modeling,” 2022.
[73] M. Komeili, K. Shuster, and J. Weston, “Internet-augmented dialogue
generation,” 2021.
[74] H. Lyu, S. Jiang, H. Zeng, Y. Xia, Q. Wang, S. Zhang, R. Chen,
C. Leung, J. Tang, and J. Luo, “LLM-rec: Personalized recommendation
via prompting large language models,” in NAACL Findings, 2024.
[75] K. Fujiwara, M. Sasaki, A. Nakamura, and N. Watanabe, “Measuring
the interpretability and explainability of model decisions of five large
language models,” 2024.
[76] T. Zeller, “Exploring the effects of enriched english language input on
language model efficiency,” 2024.
[77] K. Firstova, E. Ramirez, T. Castillo, K. Arvidsson, and A. Larsen,
“Investigating contextual layer fusion in recent open source large
language models for context retention and comprehension,” Authorea,
2024.
[78] X. Bai, L. Duan, R. Tang, G. Batra, and R. Agrawal, “Improving text-
based similar product recommendation for dynamic product advertising
at yahoo,” in CIKM, 2022.
[79] S. Barocas, M. Hardt, and A. Narayanan, Fairness and Machine
Learning: Limitations and Opportunities.
MIT Press, 2023.
[80] Z. Obermeyer, B. Powers, C. Vogeli, and S. Mullainathan, “Dissecting
racial bias in an algorithm used to manage the health of populations,”
Science, 2019.
[81] J. B. Merrill, “Does facebook still sell discriminatory ads? –
the markup,” https://themarkup.org/the-breakdown/2020/08/25/does-
facebook-still-sell-discriminatory-ads, 2024.
[82] F. Dawson, Z. Mosunmola, S. Pocker, R. A. Dandekar, R. Dandekar, and
S. Panat, “Evaluating cultural awareness of llms for yoruba, malayalam,
and english,” 2024.
[83] S. L. Blodgett, S. Barocas, H. Daumé III, and H. Wallach, “Language
(technology) is power: A critical survey of “bias” in NLP,” in ACL,
2020.
[84] S. Xu, W. Dong, Z. Guo, X. Wu, and D. Xiong, “Exploring multilingual
concepts of human value in large language models: Is value alignment
consistent, transferable and controllable across languages?” 2024.

--- Page 12 ---

12
[85] C. C. Liu, F. Koto, T. Baldwin, and I. Gurevych, “Are multilingual
llms culturally-diverse reasoners? an investigation into multicultural
proverbs and sayings,” 2024.
[86] J. Kharchenko, T. Roosta, A. Chadha, and C. Shah, “How well do llms
represent values across cultures? empirical analysis of llm responses
based on hofstede cultural dimensions,” 2024.
[87] V. Prabhakaran, R. Qadri, and B. Hutchinson, “Cultural incongruencies
in artificial intelligence,” 2022.
[88] C. Li, M. Chen, J. Wang, S. Sitaram, and X. Xie, “Culturellm:
Incorporating cultural differences into large language models,” 2024.
[89] A. Zou, L. Phan, S. Chen, J. Campbell, P. Guo, R. Ren, A. Pan, X. Yin,
M. Mazeika, A.-K. Dombrowski, S. Goel, N. Li, M. J. Byun, Z. Wang,
A. Mallen, S. Basart, S. Koyejo, D. Song, M. Fredrikson, J. Z. Kolter,
and D. Hendrycks, “Representation engineering: A top-down approach
to ai transparency,” 2023.
[90] C. Schooler and G. Hofstede, “Culture’s consequences: International
differences in work-related values,” Contemp. Sociol., 1983.
[91] Y. Cao, L. Zhou, S. Lee, L. Cabello, M. Chen, and D. Hershcovich,
“Assessing cross-cultural alignment between ChatGPT and human
societies: An empirical study,” 2023.
[92] R. L. Johnson, G. Pistilli, N. Menédez-González, L. D. D. Duran,
E. Panai, J. Kalpokiene, and D. J. Bertulfo, “The ghost in the machine
has an american accent: value conflict in GPT-3,” 2022.
[93] R. I. Masoud, Z. Liu, M. Ferianc, P. Treleaven, and M. Rodrigues,
“Cultural alignment in large language models: An explanatory analysis
based on hofstede’s cultural dimensions,” 2023.
[94] S. Mohamed, M.-T. Png, and W. Isaac, “Decolonial ai: Decolonial
theory as sociotechnical foresight in artificial intelligence,” Philosophy
& Technology, 2020.
[95] G. Kovaˇc, M. Sawayama, R. Portelas, C. Colas, P. F. Dominey, and
P.-Y. Oudeyer, “Large language models as superpositions of cultural
perspectives,” 2023.
[96] W. Wang, W. Jiao, J. Huang, R. Dai, J. tse Huang, Z. Tu, and M. R. Lyu,
“Not all countries celebrate thanksgiving: On the cultural dominance in
large language models,” 2024.
[97] R. Qadri, R. Shelby, C. L. Bennett, and E. Denton, “Ai’s regimes of
representation: A community-centered study of text-to-image models
in south asia,” in FAccT, 2023.
[98] N. Sambasivan, E. Arnesen, B. Hutchinson, T. Doshi, and V. Prab-
hakaran, “Re-imagining algorithmic fairness in india and beyond,” in
FAccT, 2021.
[99] N. Sambasivan, E. Arnesen, B. Hutchinson, and V. Prabhakaran, “Non-
portability of algorithmic fairness in india,” 2020.
[100] P. Niszczota, M. Janczak, and M. Misiak, “Large language models can
replicate cross-cultural differences in personality,” 2024.
[101] S. Ghosh, P. N. Venkit, S. Gautam, S. Wilson, and A. Caliskan, “Do
generative ai models output harm while representing non-western
cultures: Evidence from a community-centered approach,” in AIES,
2025.
[102] S. Ghosh, “Interpretations, representations, and stereotypes of caste
within text-to-image generators,” in AIES, 2025.
[103] D. Das, S. Guha, J. R. Brubaker, and B. Semaan, “The “colonial
impulse" of natural language processing: An audit of bengali sentiment
analysis tools and their identity-based biases,” in CHI, 2024.
[104] S. Bhatt and F. Diaz, “Extrinsic evaluation of cultural competence in
large language models,” in EMNLP Findings, 2024.
[105] O. Ignat, G. G. Lakshmy, and R. Mihalcea, “Cross-cultural inspiration
detection and analysis in real and llm-generated social media data,” in
C3NLP Workshop, 2025.
[106] A. Rao, A. Yerukola, V. Shah, K. Reinecke, and M. Sap, “Normad: A
framework for measuring the cultural adaptability of large language
models,” in NAACL, 2025.
Garima Chhikara is as Assistant Professor in
Delhi Technological University in Computer Science
and Engineering Department. She is also a PhD
student in School of IT at IIT Delhi, advised by
Prof. Abhijnan Chakraborty. Her research interests
include Fairness in Summarization, Social Network
analysis, Computational Social Science. She obtained
Masters from IIIT Delhi under the supervision of
Prof. Vinayak Naik.
Abhishek Kumar is a Technical Lead at HCLTech,
working in the domain of Generative AI. He earned
his master’s degree from Delhi Technological Uni-
versity.
Abhijnan Chakraborty is an Assistant Professor in
the Department of Computer Science and Engineering
at Indian Institute of Technology (IIT) Kharagpur.
Earlier, he was an Assistant Professor at IIT Delhi in
the Department of Computer Science and was also
associated with the School of Artificial Intelligence.
In 2022, he was inducted as a Young Associate of
the Indian National Academy of Engineering (INAE).
Before IIT Delhi, he worked for 2.5 years at the Max
Planck Institute for Software Systems (MPI-SWS)
as a post-doctoral researcher. He obtained his PhD
from IIT Kharagpur, where he was jointly advised by Prof. Niloy Ganguly
from IIT Kharagpur and Prof. Krishna Gummadi from MPI-SWS. During
PhD, he was awarded the prestigious Prime Minister’s Fellowship for Doctoral
Research and Google India PhD Fellowship.

```
