---
title: "2025-authors-Mapping the Italian Telegram Ecosystem Communities Toxicity and Hate - PDF Extract"
source_pdf: "2025-authors-Mapping the Italian Telegram Ecosystem Communities Toxicity and Hate.pdf"
pages: 29
extracted_at: "2026-02-13T13:14:08.316014"
---

# PDF Extract: 2025-authors-Mapping the Italian Telegram Ecosystem Communities Toxicity and Hate

**Source PDF:** 2025-authors-Mapping the Italian Telegram Ecosystem Communities Toxicity and Hate.pdf
**Total Pages:** 29

---

## Content

```
--- Page 1 ---

Mapping the Italian Telegram Ecosystem:
Communities, Toxicity, and Hate Speech
Lorenzo Alvisi1,2, Serena Tardelli2*, Maurizio Tesconi2
1IMT School for Advanced Studies, Lucca, Italy.
2Institute of Informatics and Telematics, National Research Council of Italy,
Pisa, Italy.
*Corresponding author(s). E-mail(s): serena.tardelli@iit.cnr.it;
Contributing authors: lorenzo.alvisi@iit.cnr.it, lorenzo.alvisi@imtlucca.it;
maurizio.tesconi@iit.cnr.it;
Abstract
Telegram has become a major space for political discourse and alternative media. However,
its lack of moderation allows misinformation, extremism, and toxicity to spread. While prior
research focused on these particular phenomena or topics, these have mostly been examined
separately, and a broader understanding of the Telegram ecosystem is still missing. In this
work, we fill this gap by conducting a large-scale analysis of the Italian Telegram sphere,
leveraging a dataset of 186 million messages from 13,151 chats collected in 2023. Using
network analysis, Large Language Models, and toxicity detection tools, we examine how
different thematic communities form, align ideologically, and engage in harmful discourse
within the Italian cultural context. Results show strong thematic and ideological homophily.
We also identify mixed ideological communities where far-left and far-right rhetoric coexist
on particular geopolitical issues. Beyond political analysis, we find that toxicity, rather
than being isolated in a few extreme chats, appears widely normalized within highly toxic
communities. Moreover, we find that Italian discourse primarily targets Black people,
Jews, and gay individuals independently of the topic. Finally, we uncover common trend
of intra-national hostility, where Italians often attack other Italians, reflecting regional and
intra-regional cultural conflicts that can be traced back to old historical divisions. This
study provides the first large-scale mapping of the Italian Telegram ecosystem, offering
insights into ideological interactions, toxicity, and identity-targets of hate and contributing
to research on online toxicity across different cultural and linguistic contexts on Telegram.
Keywords: Telegram, social network, communities, toxicity
1
arXiv:2504.19594v2  [cs.SI]  5 May 2025

--- Page 2 ---

1 Introduction
Telegram has shown a substantial growth in recent years, becoming a key platform for digital
communication. Its strong encryption, minimal content moderation and group-centric archi-
tecture have promoted a diverse ecosystem of discussions, from political debates to grassroots
organizations. However, these same features have also allowed the unmoderated spread of
disinformation, extremist content, and toxic discourse, raising concerns about ideological
polarization and online harm. [1].
Despite its growing relevance, Telegram remains largely unexplored with respect to other
social media platforms like Twitter. Existing research on Telegram mostly focused on spe-
cific cases of harmful content, such as conspiracy [2–4], far-right extremism [5, 6], and
disinformation campaigns [7–9]. Moreover, scholarly attention has mostly focused on right-
wing ideological spaces, with far-left clusters receiving comparatively little attention, as often
considered less problematic or more difficult to identify[5, 6, 10].In parallel, although toxic
discourse is widely recognized as a central challenge in digital ecosystems, our understanding
of its structural diffusion within Telegram communities remains limited. It is unclear whether
toxicity is confined to a few extreme environments or broadly normalized across ideologically
diverse discussions.
A key limitation in the study of Telegram is the scarcity of large-scale datasets. Most
existing datasets are either incomplete due to the complexity of data collection or are focused
on specific topics. In addition, a comprehensive mapping of a national or linguistic Telegram
ecosystem is still missing.
In this work, we address these gaps by conducting a large-scale analysis of the Italian
Telegram ecosystem. Building upon the methodology introduced in [4], and leveraging the
forwarding mechanism as a proxy for homophily we collected a dataset of over 186 million
Italian-language messages posted throughout 2023 across 15,378 public chats. This is, to the
best of our knowledge, the most extensive dataset of Telegram messages with a clear spatial-
linguistic focus that captures both large and small-scale conversations on a wide array of
topics. We build a directed weighted forwarding network and use several state-of-the-art Large
Language Models (LLMs) to characterize individual chats in terms of most discussed topics
and political orientation. Moreover, we assess message toxicity using the Perspective API and
explore how hate speech is distributed in communities by identifying its main targets.
We formulate the following three questions:
RQ1. How do political orientations vary across Italian Telegram communities?
RQ2. Is toxicity concentrated in a few extreme chats, or is it widely distributed across
communities?
RQ3. Who are the primary targets of hate speech, and how are they related to ideological
alignments?
Our findings show strong thematic and ideological homophily. Politically oriented com-
munities typically adhere to far-right or far-left narratives, but we also identified a hybrid
ideological group in which left- and right-wing rhetorics coexist, especially with regard to
geopolitical discourses. We find that toxicity is not limited to fringe groups but seems to be
widely normalized within highly toxic communities. Finally, hate speech frequently targets
LGBTQ+ and black people, but also reveals intra-regional antagonisms, in which Italians
attack other Italian groups along old historical divisions.
2

--- Page 3 ---

Our findings suggest the need of context-specific moderation strategies and pave the way
for future work on cross-linguistic comparisons and the social drivers of toxicity on Telegram.
2 Related work
Although Telegram’s user base and societal impact have expanded, studies on its wider
ecosystem are still limited. Most studies focused on specific phenomena such as political
extremism, misinformation, infodemic, and conspiracy, especially on other platforms [11–14],
leaving the overall thematic diversity and broader ecosystem of Telegram largely unexplored.
The majority of work on Telegram concentrated on specific phenomena such as extrem-
ism [6, 15] and political campaigns [16, 17]. For instance, the authors in [5] analyzed the
interconnections between extremist groups on Telegram, while authors in [18] analyzed
conspiracy-related communities. In addition, comparative studies have examined how conspir-
acy narratives differ across language communities, revealing culturally specific patterns [4].
Other research has targeted specific domains such as cryptocurrency-related fraud, uncover-
ing cross-platform scam networks using Telegram as a central hub [19]. Indeed, the limited
moderation of the platform and its privacy characteristics have been known to facilitate the
proliferation of harmful content, including supremacist speech [20], conspiracy theories [21],
and hate speech [22].
While several large-scale Telegram datasets have been released [23, 24], these typically
center on specific issues or domain (e.g., extremism or misinformation), and do not offer
focused analyses of national or linguistic Telegram spheres. To address these gaps, we present
a large-scale analysis of the Italian Telegram ecosystem, investigating community structures,
topic-driven clustering (homophily), network dynamics, ideological orientations, and toxicity
patterns across both political and apolitical domains.
Indeed, online toxicity has been extensively under scrutiny on platforms like Twitter,
especially in political contexts [25, 26], yet remains underexplored on Telegram and across
various thematic domains. Recent work showed that toxic behavior tends to persist, and
often intensify, within polarized online communities [27, 28], including Telegram. Moreover,
research on deplatforming events showed that Telegram frequently serves as a refuge for banned
extremist groups, subsequently increasing toxicity levels on the platform [29]. Despite these
efforts, comprehensive knowledge regarding how toxicity spreads or evolves across different
thematic settings is still limited. Existing research has largely focused on specific events or
domains [4, 30], therefore leaving mostly unexplored larger patterns and relationships, a gap
that we aim to address to understand how different thematic contexts influence the distribution
of toxic discourse.
To the best of our knowledge, this is the first in-depth look at the Italian Telegram sphere,
offering a broad overview of its landscape, main topics, political leanings, and levels of toxicity
within its socio-cultural context.
3

--- Page 4 ---

3 Data collection
3.1 Terminology
Telegram offers two main types of spaces for interaction: channels and groups. A channel
is a one-to-many communication space where subscribers may watch the content but can-
not participate personally, while only administrators may publish messages. They are used
for broadcasting information to a large audience, such as news updates or public announce-
ments, and also for sharing scams and other types of misleading content [19]. Conversely,
groups facilitate many-to-many communication in which every member may contribute to the
conversation. Recently, Telegram introduced linked chats, which allow a channel to be offi-
cially connected to an affiliated group, representing the same community. This connection is
significant within the dynamics of Telegram, as content posted in a channel is automatically
forwarded to the affiliated group, generating discussions in the community. Indeed, the for-
warding feature allows Telegram users to share messages between different chats, contributing
to the dissemination of information. This feature is also fundamental for the snowball sampling
technique used in this work, which is explained in the following sections.
In summary, we will use the term channel to refer to a channel, linked chat to indicate a
the pair channel-affiliated group, and group to denote a standalone group not associated with
any channel. Additionally, we will employ the generic term chat to broadly describe any of
these categories—channels, linked chats, or groups—when distinctions among them are not
relevant.
3.2 Initial Seed Collection of Public Telegram Chats
We first retrieve a list of public Telegram chats to use as starting seed for our data collection.
We retrieve them from two online sources: Telegram Italia1, a community-driven website
cataloging Italian Telegram chats, and TGStat2, a website providing an extensive catalog
of Telegram chats across various countries and languages. Both sources are widely used in
literature for data collection [5, 31, 32]. Given our focus on the Italian-speaking messages, we
retrieved chats classified under the Italian language from TGStat. Notably, unlike Telegram
Italia, which includes both channels and groups, TGStat only provided channels classified
in Italian. As a result, we collected 20,229 cataloged Italian chats from Telegram Italia and
1,241 from TGStat, for a total of 21,470 public Telegram chats, of which 14,767 consist of
channels and 6,703 consist of groups. Neither platform provides information on whether there
are linked chats among the channels and groups they list.
3.3 Retrieving data from chat seeds
We began by retrieving data posted in the 21,470 chat seeds between January 1 and December
31, 2023. To ensure the reliability of the catalogs, we first verified whether the chats were
indeed Italian, retaining only those that had at least 10 comments in Italian and where the
majority of messages were in Italian. Additionally, we discarded empty chats, chats whose
content consisted solely of pictures, non-public chats, and chats that were inaccessible at the
time of data collection. As a result, we were left with 4,360 valid seeds out of the original
1www.telegramitalia.it
2www.tgstat.com
4

--- Page 5 ---

21,470. Notably, TGStat yielded a higher percentage of valid seeds despite cataloging fewer
Italian chats, with 63% (776 out of 1,241) passing our checks. In contrast, only 18% (3,584
out of 20,229) of the seeds from Telegram Italia were considered valid. Notably, this finding
suggests the partial reliability and up-to-date accuracy of existing Telegram censuses.
3.4 Categorization of Chat Seeds
Both Telegram Italia and TGStat also provide a thematic classification for the chats in their
catalogs. Telegram Italia uses category labels in Italian, while TGStat in English. Although the
taxonomies differ in language, they are broadly comparable. For consistency, we aligned the
categories across the two platforms using English labels. The categories are shown in Figure 1,
which also illustrates the category distribution for the 4,360 valid seed chats from which we
successfully collected data. Interestingly, the distribution of chats across categories proved to
be balanced, ensuring a wide coverage of topics within the Italian Telegram ecosystem.
entertainment
religion
games
social
psychology
adults
cars
sport
shops
finance
travel
news
other
arts
anime
video and films
technology & science
politics
animals
medicine
kids & education
law
 
0
50
100
150
200
250
300
350
400
chats
Telegram Italia
TGStats
Fig. 1: Count of chats per category for the 4,360 valid seed chats as provided by their respective
sources. The balance distribution across categories ensures a wide coverage of topics within
the Italian Telegram ecosystem.
5

--- Page 6 ---

0
1
2
3
4
5
6
iteration
0
500
1000
1500
2000
chats
channel
linked chat
group
Fig. 2: Counts and types of Telegram chats retrieved at each iteration of our snowball crawling
strategy. Linked chats–consisting of a channel and its affiliated group–are the most prevalent,
while standalone groups are the least represented in the dataset. This is likely because groups,
by nature, tend to be more private, making them less accessible.
3.5 Data Collection via Snowball Sampling Strategy
Our goal is to conduct the largest-ever census of all Italian Telegram chats. Starting from the
seed chats, we initiated data collection using a snowball sampling strategy. This approach
focuses on the diffusion of forwarded messages–a Telegram feature that allows users to share
messages from one chat to another. It has been widely used in the literature for data collection,
and its diffusion patterns have already provided valuable insights into detecting homophily
and common interests in online communities [4]. Coupled with the balanced distribution of
thematic categories, this method ensures a broad and diverse dataset. Starting with our 4,360
seed chats, we retrieved their 2023 message history and followed the forwarded messages to
discover new channels and crawl their messages. The process was repeated iteratively in a
Dijkstra-style snowball fashion, where at each iteration, we retained only those chats containing
at least 10 messages and whose majority language was Italian. This process continued until
no additional chats could be identified for download. Seven iterations were needed to exhaust
the search. A the end of this process, we ended up with an unprecedented Italian Telegram
dataset, consisting of 15,378 chats and 186,757,857 messages posted throughout 2023. With
this comprehensive dataset, we are able to link channels with their affiliated groups, treating
them as a single entity, which we will refer to as linked chats moving forward. In Figure 2,
we present the count of chat downloads in each iteration, which follows a gamma distribution,
reflecting the diminishing returns of each subsequent iteration.
6

--- Page 7 ---

4 Methods
4.1 Building the network
The diffusion of forwarded messages plays a crucial role in shaping the structure of Telegram
communities, as it highlights shared themes and common interests among different chats. This
phenomenon reflects the principle of homophily — the tendency of individuals to connect
with others who are similar to themselves — which becomes visible through the forwarding
network [4].
To investigate the structure of the Italian Telegram sphere, we constructed a forwarding
network modeled as a directed, weighted graph G := (N,E). Each node represents a Telegram
chat, which can be a group, a channel, or a linked chat. For every pair of nodes 𝑛,𝑚∈N, we
draw a directed edge from 𝑛to 𝑚whenever a message is forwarded from 𝑛to 𝑚, assigning
to the edge a weight corresponding to the number of forwards. Linked chats — channels and
their associated groups — are normalized by using the channel’s identifier to represent the
entire linked entity. Additionally, we remove self-loops to maintain consistency.
This process initially produced a network composed of 15,378 nodes and 238,958 edges.
Although our aim was to comprehensively map the Italian public sphere on Telegram, the
method was inherently limited by the coverage of the initial dataset (i.e., the seed list).
Consequently, some segments of the Italian Telegram ecosystem may remain outside our scope.
Nonetheless, chats disconnected from the giant component — those that neither received nor
sent forwards — are likely to be less engaged or influential within the broader network.
To refine the network, we first excluded nodes without incoming or outgoing edges,
reducing the graph to 13,144 nodes. We then applied a fine-tuned version of the Louvain
algorithm [33], adapted for weighted and directed graphs, to detect communities. We retained
only the communities representing at least 1% of the total nodes (i.e., communities with at
least 132 chats), resulting in a final network composed of 11,305 nodes, 227,642 edges, and
organized into 15 distinct communities.
4.2 Topic labeling
To identify the predominant topics discussed within each community, we employ Mix-
tral:8x7B [34], an open-source sparse mixture-of-experts language model specifically designed
to efficiently handle complex classification and generation tasks.
We assign a topic label to each chat using a predefined set of categories derived from
the classifications provided by TGStat and Telegram Italia, as illustrated in Figure 1. The
labeling process is guided by the prompt detailed in Table A1. For each chat, we combine
three sources of information to maximize the reliability of the labeling process: (i) the chat
name, (ii) the chat description, (iii) and a random sample of messages posted in the chat.
Messages are randomly extracted until reaching a maximum of 4,000 characters - to balance
the trade-off between execution time, performance, and hallucination probability — ensuring
a representative snapshot of the chat’s content without exceeding the model’s constraints.
Using multiple sources (i.e., name, description, messages) allows the model to better infer the
dominant topic, especially for chats whose name or description alone might be ambiguous or
sparse. In this way, we assign a topic at the chat level based on the model’s classification.
7

--- Page 8 ---

At the community level, we determine the dominant topic by aggregating the labels
assigned to individual chats within each community and selecting the majority topic.
4.3 Political labeling
Shared political views are a significant factor driving homophily in online environments
[35, 36]. As such, we analyze the political leaning of chats using ChatGPT-4o [37].Several
studies have successfully employed this methodology [38, 39]. We present the prompt used for
this method in Table A2, In particular, we use seven political labels based on the methodology
adopted by MediaBiasFactCheck3, a website that fact-checks the credibility of news sources
widely used in the literature to classify political orientations [25, 40]. These labels include: far-
left, left, left-center, center, right-center, right, and far-right. We use categorical labels rather
than numerical ones, as LLMs are more adapt at interpreting the contextual meaning of labels,
as shown in the literature [41]. Political labels are initially assigned at the individual chat level
by providing chatGPT-4o: (i) the chat name, (ii) the chat description, (iii) and a random sample
of messages posted in the chat. Messages are randomly extracted until reaching a maximum of
5,000 characters. A chat may or may not exhibit a political leaning. Additionally, ChatGPT-4o
can generate error messages described with a reason such as self-harm, hate speech, sexual
content, or violence that further provides valuable insights for chat evaluation. Finally, at the
community level, we classify a community as political (i.e., with a political leaning) if at
least half of its chats exhibit a political orientation, with the community’s political leaning
determined by the most common leaning found in its labeled chats.
4.4 Toxicity detection
Toxicity has become an important area of research in recent years [27]. To assess the presence
of toxic language in our chat messages, we leverage the Perspective API,4 a tool for detecting
toxic language in online discussions developed by the Jigsaw unit within Google [42].
According to the documentation, the Perspective API “predicts the perceived impact a
comment may have on a conversation by evaluating that comment across a range of emotional
concepts (attributes)”. Perspective can score the following attributes: Toxicity, Severe toxicity,
Insult, Profanity, Identity attack, Threat, and Sexually explicit. The returned score represents
a probability, between 0 and 1, where higher scores indicate a greater likelihood that a reader
would perceive the comment as containing the given attribute. For this analysis, we leverage the
Toxicity attribute, which is also the most commonly studied in existing literature [26, 43, 44],
defined as “a rude, disrespectful, or unreasonable comment that is likely to make you leave a
discussion.”5.
We analyzed all textual messages using the API in September 2024, successfully obtaining
toxicity scores for 88% of messages. Notably, the API supports multiple languages, including
Italian. Finally, following the API guidelines, we label a message as toxic if its toxicity score
is greater than 0.7.6
3https://mediabiasfactcheck.com/methodology/
4https://www.perspectiveapi.com/.
5https://developers.perspectiveapi.com/s/about-the-api-attributes-and-languages
6https://developers.perspectiveapi.com/s/about-the-api-score
8

--- Page 9 ---

4.5 Hate detection
We leverage the Identity Attack attribute provided by the Perspective API to detect whether
a message contains hateful or discriminatory content. According to the Perspective API, the
Identity Attack attribute is defined as: “Negative or hateful comments targeting someone
because of their identity.” The API returns a probability score between 0 and 1, where
higher scores correspond to a greater likelihood that the message contains an identity attack.
Following the recommended guidelines, we classify a message as containing an identity attack
if its score exceeds a threshold of 0.7.
Since the Perspective API only provides a probability score without specifying the targeted
group, we adopt a semi-supervised approach to extract and identify the specific targets of
hate within each message. First, we compile a set of identity categories based on previous
literature [45, 46], which includes: nationality, ideology, ethnicity, religion, sexual orientation,
gender, age group, disability, profession, and social class.
Subsequently, we employ the llama-3.1-nemotron-70b-instruct model [47, 48], a
publicly available instruction-tuned model developed by NVIDIA,7 to classify each message
by assigning it to one of the predefined identity categories. Table A3 presents the prompt used
for this classification task.
Finally, since the prompt is unsupervised, we need to standardize the resulting outputs.
In fact, the model often generates various terms that refer to the same identity group, lead-
ing to inconsistencies. For instance, when identifying ethnicity-related targets, Nemotron may
use variations such as “African American” and “Afro-American” to describe the same group.
Although these expressions are conceptually equivalent, their lexical variability introduces
noise into the categorization process. To address this discrepancies, we implement a map-
ping strategy using ChatGPT-4o [37] and aggregate semantically similar terms into unified,
standardized identity categories. This approach improves the consistency and reliability of
the characterization of toxic communication within the interactions. To reduce the impact of
potential biases introduced by the model, especially in sensitive cases involving labels related
to ethnicity, sexual orientation, or gender, we adopted labels sourced directly from literature
in the respective domains.
5 Results
Applying our methodology, we obtained a forwarding network composed of 11,305 nodes
and 227,642 edges, organized into 15 distinct communities. We identified these communities
using a fine-tuned version of the Louvain algorithm [33], specifically optimized for weighted
and directed graphs, and focused our analysis on those communities comprising at least 1%
of the total nodes.
Figure 3 illustrates the overall structure of the resulting network. To gain deeper insights
into the nature of these communities, we first explore the main narratives discussed within
their chats. We then further characterize each community along several dimensions, including
political orientation, levels of toxicity, and primary targets of hate, addressing our research
questions throughout the analysis.
7https://build.nvidia.com/nvidia/llama-3 1-nemotron-70b-instruct
9

--- Page 10 ---

Fig. 3: Visualization of the chat network, colored by detected communities. Nodes represent
chats; edges indicate forwarded messages. Clear community separation suggests distinct top-
ical clusters and interaction patterns.
5.1 Narratives
Since our starting point is a set of seed chats, we rely on their associated thematic topics for
categorization. To this end, we use Mixtral (as described in Section 4) to assign topics to each
chat, based on the predefined set of categories from TGStat and Telegram Italia (as described
in Section 3.4). The topic of each community is then inferred based on the majority topic
among its chats.
The results are as follows: we identify two communities related to Entertainment, three on
News, two on Sports, two on Religion, two on Finance, one on Adult content, composed mainly
of adult-themed chat, one on Social movements, referring to politically or culturally engaged
communities, such as activist groups or grassroots organizations, rather than discussions about
social media platforms, one on Tech culture focused on tech-based shops, and one on Arts,
which appears to be associated with niche subcultures such as hikikomori, emo, introspectivity,
love, and poetry, where artistic expression plays a key role in identity and self-representation.
Interestingly, in the network representation, the Arts community, while still connected, appears
drifted away from the others, mirroring its introspective nature.
Figure 3 presents the communities renamed as follows. Given the limited scope of our
predefined set of categories, some communities were assigned the same topic despite having
10

--- Page 11 ---

subtle differences that our categories could not fully capture. Therefore, we compare the
communities with the same category using a state-of-the-art method called Wordshift [49]
and measure the differences in word usage across the chat descriptions of each community.
Results show that the two communities associated with the topic Entertainment, while
both falling under the same broad category, serve distinct purposes. One is centered around
general mainstream discussions, making it the largest community in our dataset in terms of
user base, chats, and comments. This community also appears to attract interactions from users
across various social media platforms. Many popular Italian meme pages from Facebook,
Instagram, and Twitter have a presence on Telegram within this community, as also observed
during manual inspection. As such, we label this community as General. In contrast, the
second community on Entertainment focuses on gaming and online role-play conversations.
For this reason, we name this community Gaming. A similar distinction emerges in the
three communities labeled with the topic News, which each emphasize different aspects of
information dissemination. One focuses on international news, with a strong emphasis on
warfare, particularly the conflicts in Ukraine and Israel. We thus label this community as
Warfare. The second community is about local news, either geographically based or centered
around specific topics such as local job searches or climate forecasts, henceforth referred to as
LocalNews. The third one is instead oriented toward personal freedom, counter-information,
and alternative news, which we refer to as AltNews.
The two communities under the topic Sports are primarily concerned with football, high-
lighting its central role in Italian culture and identity, with occasional mentions of other
sports. However, they differ in their mode of interaction. One community mostly converge
on discussion groups, while the other mostly comprises of channels where news, updates,
and information exchange take front stage. As such, we label them as SportForum and
SportInfo, respectively. Similarly, the two religious communities, though falling under the
same broad category, diverge, as one reflects Italian cultural ideas through a focus on Chris-
tianity, prayers, saints, and the holy church, while the other emphasizes mystical activities
and personal growth, spirituality and self-awakening. In light of these characteristics, we call
these communities Christianity and Spirituality, respectively. In addition, we observe
a similar pattern for the communities annotated with the topic Finance. In fact, one commu-
nity is centered around cryptocurrencies, which we refer to as Crypto, while the other takes a
broader approach, focusing on affiliate marketing and strategies for investments and generat-
ing passive income, which we refer to as Finance. Finally, we rename the community labeled
with the topic Social to Activism, to avoid confusion with social media-related content, as
the term refers instead to activism, social centers, and grassroots engagement.
Based on these distinctions, Table 1 summarizes the communities and their topics. The
coherence of our categorization is further supported by the strong thematic alignment observed
between each community’s topic distribution and that of its seed chats.
5.2 Political Orientations (RQ1)
To answer (RQ1), i.e., how political leaning and the topics discussed within Telegram com-
munities in the Italian public sphere are related, we first examine the distribution of political
orientation across different communities. As described in Section 4, a community is classified
as political if at least 50% of its chats exhibit a political orientation, with the dominant leaning
determined by the most common label.
11

--- Page 12 ---

Name
Topic
Chats
Messages
General
Entertainment
3,763
71,719,216
AltNews
News
2,306
13,866,439
Gaming
Entertainment
1,235
7,266,662
Warfare
News
907
9,271,835
SportForum
Sport
485
23,101,659
Adult
Adult
465
4,958,428
Spirituality
Religion
345
1,212,645
Activism
Social
334
856,596
Crypto
Finance
319
1,978,457
LocalNews
News
251
3,183,184
Christianity
Religion
240
497,578
Finance
Finance
184
1,620,185
SportInfo
Sport
151
6,371,009
Tech
Tech
151
4,820,753
Arts
Arts
139
378,093
Table 1: Communities statistics
As shown in Figure 4, most of the chats in our dataset do not show a clear political leaning.
In fact, politically oriented chats are prevalent in five communities: Activism, AltNews,
Warfare, General, and Christianity. Among these, only three (i.e., AltNews, Warfare,
and Activism) meet the threshold for our definition political classification. In particular, the
community AltNews is mainly composed of chats with a strong far-right political leaning,
the community Activism is composed on mainly far-left chats, and Warfare contains both
far-left and far-right political leaning chats.
The presence of both far-left and far-right narratives in Warfare reveals a complex ideo-
logical geopolitical landscape in which, for example, discussions on the Ukraine war involve
both right-leaning chats typically expressing nationalist and anti-immigration ideas, and left-
leaning chats matching with Russian rethoric and propaganda. This observation highlights the
complexity political views in online discourse, more than typically seen in studies of online
discourse. As right-wing and extreme communities are typically connected with disinforma-
tion, radicalization, and social media moderation difficulties [2], research on online political
debate really frequently focuses disproportionately on them. On the other hand, far-left inter-
net networks get far less attention in the research. Our results, however, shows the existence of
left-leaning groups on Telegram that occasionally participate in controversial debate, implying
that a more all-encompassing strategy of researching political extremism in digital settings is
required.
Although General and Christianity contain a substantial number of politically oriented
chats (442 and 50, respectively), these account for less than 50% of their total composition
and thus do not qualify the communities as explicitly political. All remaining communities
show low political content, with less than 20 politically labeled chats and less than 10% of
their composition associated with any ideological stance.
Findings and Remarks
Our analysis shows that political discourse is concentrated in a
few communities, with clear ideological distinctions: AltNews is predominantly far-right,
Activism is far-left, and Warfare is politically polarized, challenging the common focus on
right-wing extremism in online political research, revealing that far-left communities also play
a role in ideological discourse, sometimes engaging in contentious narratives.
12

--- Page 13 ---

Fig. 4: Visualization of the chat network, colored by political leaning of each chat. Communi-
ties such as Activism, AltNews, and Warfare show clear ideological polarization, separating
politically opposed groups.
These results suggest that while Telegram hosts a politically diverse ecosystem, the rela-
tionship between topic and political leaning is not straightforward, as users from various
ideological backgrounds engage in a wide range of discussions across different topics.
5.3 Toxicity distribution across communities (RQ2)
To answer RQ2, i.e., is community-level toxicity mainly driven by a few highly toxic chats,
or does it result from toxicity being widely and evenly distributed across many chats within
the community, we first analyze the distribution of toxicity across all chats. As mentioned,
perspectiveAPI managed to successfully label 164M messages, corresponding to the 88% of
our dataset. Following the official API guidelines, we classify a message as toxic if its toxicity
score is greater or equal to 0.7, resulting in a total of 2,3M toxic messages in our dataset. Next,
we define toxicity at chat level by computing, for each chat, the percentage of toxic messages
it contains. Finally, to assign a toxicity score to each community, we compute the average
toxicity percentage of the chats within that community.
Figure 5a shows the mean percentages of toxicity across the communities. The toxicity
of each community is represented by colored dots) Overall the toxicity of the communities
spans from 0% to almost 3%. In other words, on average, the chats within the communities
13

--- Page 14 ---

0
1
2
mean toxicity
AltNews**
General**
Warfare**
SportForum*
SportInfo**
Christianity**
Gaming**
Spiritual**
Activism**
Finance**
Adult**
LocalNews**
Crypto**
Tech**
Arts
global mean
(a) Mean toxicity percentages by community. Sta-
tistical significance levels indicate communities
with notably higher or lower toxicity than average:
∗∗: 𝜌< 0.01,∗: 𝜌< 0.1.
0.00
0.05
0.10
0.15
mean identity attack
AltNews**
General**
Warfare**
SportForum**
SportInfo**
Christianity**
Gaming**
Spiritual**
Activism**
Finance
Adult**
LocalNews**
Crypto**
Tech**
Arts**
global mean
(b) Mean identity attack percentages by commu-
nity. Statistical significance levels indicate com-
munities with notably higher or lower toxicity than
average: ∗∗: 𝜌< 0.01,∗: 𝜌< 0.1.
Fig. 5: Toxicity and identity attack percentages by community.
contain between the 0% and the 3% of toxicity. While these percentages may initially appear
low, it is important to consider that the dataset spans an entire year and includes conversations
potentially containing millions of messages. Consequently, even small percentages translate
into a significant number of toxic interactions.
We compared the average toxicity of each community against the overall average toxicity
across all chats in the network, represented by the red line at 0.73%. This baseline indicates
that the network, on average, exhibits relatively low toxicity. To determine whether each
community significantly differs from this overall toxicity, we used the Mann-Whitney U test
[50]. This test was chosen as the distribution of the toxicity scores violates the assumptions of
normality, and due to unequal sample sizes across communities. Specifically, we tested if the
distribution of chat toxicity percentages within each community significantly differs from the
toxicity percentages observed across all the chats in the network. This allowed us to identify
communities with toxicity levels that are notably higher or lower than average. The results
highlight statistical differences in toxicity levels across communities within the network.
As expected, the Adult community shows significantly higher toxicity levels compared
to the overall average, confirming expectations about the nature of its content. Interestingly,
the communities General, Gaming, and SportInfo also exhibit significantly higher toxicity
levels, suggesting unexpected problematic interactions within these groups. Notably, topics
of sports and entertainment have often been tied to antisocial behavior [51] that, in extreme
14

--- Page 15 ---

0.6
0.7
0.8
0.9
Gini index
0.0
0.5
1.0
1.5
2.0
2.5
toxicity (%)
Activism
Adult
AltNews
Arts
Christianity
Crypto
Finance
Gaming
General
LocalNews
Spiritual
SportForum
SportInfo
Tech
Warfare
Linear fit R2 = 0.7605 Pearson =
0.8721 
= 0.0000
Fig. 6: Relationship between community mean toxicity and Gini index. Communities with
higher toxicity generally have toxicity evenly distributed among chats, suggesting normaliza-
tion of toxic behavior.
cases, can bring up to the normalization of toxicity [52]. Conversely, communities such as
Tech, Crypto, AltNews, Warfare, and Activism display significantly lower toxicity, indi-
cating they might host more constructive or moderated discussions. These findings highlight
that toxicity is unevenly distributed across communities. This suggests that some communi-
ties might require targeted moderation or further investigation to identify factors or topics
contributing to their higher toxicity levels.
An important question arising from these observations is whether community toxicity
mainly results from a few highly toxic chats or if it emerges from many chats, each contributing
to the overall toxicity. Understanding this distinction can clarify how harmful behaviors
spread and become normalized within communities. Additionally, this insight can support the
design of more effective interventions aimed at promoting healthier interactions. To answer
this question, we used the Gini index, a measure commonly applied to study inequality
or concentration within a distribution. In our analysis, the Gini index[53] measures how
evenly toxicity is spread across the chats in each community. In particular, a high Gini index
indicates that toxicity is concentrated in only a few chats, while a low Gini index means
toxicity is more evenly shared among many chats. We compared the mean toxicity percentage
(indicating how toxic a community is on average) with the Gini index (indicating how toxicity
is distributed within the community). Confronting these two measures allows us to understand
if communities become toxic due to widespread normalization (i.e., low Gini) or because of
a small number of highly problematic chats (i.e., high Gini).
Figure 6 presents the relationship between the Gini index and mean toxicity percentage
across communities. Each community is represented by a circle, with its size corresponfing to
the number of chats it contains. The dashed red line shows a strong negative linear relationship
15

--- Page 16 ---

between the Gini index and mean toxicity, supported by significant statistical evidence (Pear-
son’s correlation = −0.8721, 𝑅2 = 0.7605, 𝜌< 0.0001). This result means that communities
with higher average toxicity tend to have lower Gini indices, suggesting that toxicity is usually
evenly spread across many chats. In other words, highly toxic communities typically become
toxic because toxic behaviors become normalized across most of their chats, rather than being
driven by only a few extremely toxic outliers. This linear dependency reinforces the idea that
toxicity increases as it becomes normalized within a community [52]. The Adult community
represents a special case: despite having an moderate Gini index, indicating that toxicity is
moderately evenly spread across its chats, it still shows significantly higher average toxicity
compared to other communities. This result likely reflects the explicit nature of adult discus-
sions, where inherently sensitive or explicit topics naturally lead to higher overall levels of
toxic interactions, independent of how concentrated toxicity is within specific chats. Finally,
community size does not appear related to either average toxicity or the Gini index. This means
that community size alone does not significantly affect how toxicity develops or spreads.
These insights can inform the design of effective moderation strategies. Communities with
evenly spread toxicity (i.e., low Gini, high mean toxicity) likely require broader cultural or
behavioral interventions, whereas communities with concentrated toxicity (i.e., high Gini, high
mean toxicity) might benefit more from targeted interventions focused on specific problematic
chats or users.
5.4 Targets of Hate (RQ3)
To answer RQ3, i.e., whether there are common targets of hate across Telegram communi-
ties and topics, we analyze the identity groups most frequently targeted by hateful messages.
Using the Identity Attack attribute from the Perspective API and further classification with
Llama-3.1-Nemotron-70B-Instruct, we examine attacks based on nationality, ethnicity, reli-
gion, sexual orientation, and gender. As mentioned in Section 4, we apply a mapping approach
using ChatGPT-4o to standardize identity labels for consistency in all categories.
Hate Based on Nationality
To analyze nationality-based attacks, we prompted the LLM
to identify nationalities. In general, the model returned appropriate responses; however, in
some instances, it produced broader regional or geographic labels (e.g., ”Arab,” ”African”)
rather than specific nationalities. This reflects a known limitation of LLMs, which can be
sensitive to linguistic context and occasionally inconsistent in how they represent complex
social categories such as identity, culture, or origin. Despite these nuances, we retain the term
nationalities for consistency. Figure 7 presents the targets on those communities that have at
least 100 recognized identity attacks. Interestingly, Italians are frequently targeted across all
communities. This trend highlights the cultural propensity in Italy for internal rivalries both
regional and intra-national (e.g., parochialism, north vs south, etc.) [54, 55]. Notably, these
rivalries are present not only in sports-related communities, where they might be expected,
but also in the other communities. Notably, hostility toward Israelis and Americans is most
prominent in the AltNews and Warfare communities. Ukrainians also appear frequently
in Warfare, reflecting broader political narratives in that context. Meanwhile, antagonism
toward Arab nationalities is particularly pronounced within sports communities. Overall,
while Italians appear as a cross-community target, most other nationalities tend to concentrate
16

--- Page 17 ---

AltNews
Gaming
General
SportForum
SportInfo
Warfare
 
0
20
40
60
80
100
top targeted nationalities (%)
20
49
28
32
33
8
27
4
23
13
5
19
9
9
4
5
7
6
6
9
3
16
12
5
19
4
4
3
3
4
3
19
18
27
31
29
19
Italian
Israeli
American
Chinese
African
Arab
Ukrainian
Russian
French
Indian
Other nationalities
Fig. 7: Top targeted nationalities across communities. Italians are the most frequently targeted
group, while Israeli, American, and Chinese users are also prominently targeted depending on
the context. The order of nationalities in the legend follows their global frequency as targets.
within specific thematic contexts, suggesting that nationality-based hostility is largely shaped
by the dominant cultural, political, or ideological focus of each community.
Hate Based on Ethnicity
To analyze ethnicity-based attacks, we derive the categories for
ethnicity from the classification proposed by the U.S. government agency [56]. Notably, the
Italian census adopts a different approach and classifies individuals based on their country of
origin rather than ethnicity, reflecting a different cultural approach toward ethnic categoriza-
tion [57]. As such, to avoid repetition with the nationality-based analysis, we use the categories
specified by the American government agency.
Our results, presented in Figure 8, reveal a clear trend: across all communities, Black and
African American individuals consistently represent the primary targets of ethnicity-based
hate. In most communities, between 85% and 93% of ethnicity-related attacks target Black
individuals, indicating a widespread pattern of racial hostility that aligns with findings from
existing literature [58, 59]. A more heterogeneous distribution is observed in Warfare, where
64% of attacks aimed at Black ethnicity is accompanied with 26% of White targets. Notably,
white group includes a wide spectrum of identities hl(e.g., Slavic, Anglo, Israeli, Roma, etc.).
Overall, the data highlights the centrality of anti-Black sentiment, while other targets appear
more context-specific and harder to interpret without cultural nuance
Hate Based on Religion
Results on religion-based hate (Figure 9) indicate that Judaism
is the most frequently targeted religion across all communities, accounting for 57% to 85%
of all religion-related hostility. Islam also receives 20% of religion-related attacks in most
communities. Other religious groups appear far less frequently, suggesting a concentration of
antisemitic and islamophobic narratives. The results seams pretty stable across all communi-
ties, except in Gaming where Christianity is more attacked than Islam. However, it is important
to note that our analysis is limited to data collected during 2023 and is thus influenced by the
sociopolitical climate and major events of that period. For example, international conflicts,
17

--- Page 18 ---

AltNews
Finance
Gaming
General
SportForum
SportInfo
Warfare
 
0
20
40
60
80
100
top targeted ethnicities (%)
84
91
92
88
85
93
64
3
3
3
6
5
7
11
4
4
4
6
3
25
Black or African American
Asian
White
Hispanic or Latino
American Indian or
Alaska Native
Native Hawaiian or
Other Pacific Islander
Fig. 8: Top targeted ethnic groups across communities. Black or African Americans are the
primary target in all communities, with notable increases in targeting of White and Asian
users within the Warfare community. The order of ethnicities in the legend follows their global
frequency as targets
AltNews
Gaming
General
SportForum
SportInfo
Warfare
 
0
20
40
60
80
100
top targeted religions (%)
72
60
61
56
68
84
16
16
22
25
24
9
7
22
11
15
6
3
Judaism
Islam
Christianity
Catholicism
Satanism
Hinduism
Atheism
Buddhism
Paganism
Other religions
Fig. 9: Top targeted religious groups across communities. Judaism is the most targeted religion
in all communities, with Islam and Christianity also facing notable targeting—particularly in
the sport and gaming communities. The order of religions in the legend follows their global
frequency as targets
domestic political debates, or media coverage spikes may have shaped the salience of certain
religious targets. As such, while the data reveals strong patterns, these should be interpreted
within the broader temporal and discursive context in which they emerged.
Hate Based on Sexual Orientation
To standardize sexual orientation labels, we derive the
labels from the LGBTQ+ acronym. As shown in Figure 10, gay individuals are overwhelmingly
the most targeted group, with over 85% of sexual orientation-based attacks directed at them
18

--- Page 19 ---

AltNews
Gaming
General
SportForum
SportInfo
Warfare
 
0
20
40
60
80
100
top targeted sexual
orientations (%)
85
93
90
97
94
83
6
3
3
9
5
5
Gay
Lesbian
Transexual
Straight
Bisexual
Queer
Fig. 10: Top targeted sexual orientations across communities. Gay individuals appear as the
primary target across all communities, although this may reflect a broader tendency to use the
term generically to target the entire queer community. The order of sexual orientations in the
legend follows their global frequency as targets
across all communities. Other identities within the LGBTQ+ spectrum, such as lesbian,
bisexual, or transgender individuals,appear far less frequently in explicit attacks. This sharp
imbalance may reflect both linguistic patterns in hate expression and broader social visibility
dynamics: the term “gay” is often used in hate speech to target queer people in general,
especially in online and meme-based discourse. Moreover, certain queer identities may be
targeted through coded language, implicit hostility, or gendered slurs not captured directly by
the sexual orientation categories used here. As such, these results should be interpreted as a
conservative estimate of queerphobic discourse online.
Hate Based on Gender
For gender-based hate, we rely on terminology from existing gender
discrimination studies [60, 61], which include both binary and non-binary gender identi-
ties. As shown in Figure 11, the majority of gender-related attacks are directed at cisgender
women, followed by cisgender men. This trend is consistent with previous research on online
misogyny, which highlights that women are more targeted in both political and non-political
contexts [62]. Moreover, while men also face a significant volume of online abuse, the nature
of the harassment is often gendered, as women are more frequently subjected to sexualized
and explicitly gendered attacks [63].
In contrast, transgender and non-binary identities appear far less frequently in our data.
This relative scarcity may reflect their lower visibility within Telegram communities, or the
use of indirect and coded language to target them, forms of hostility that are less likely to be
captured through surface-level keyword analysis. Additionally, the strong presence of cultural
and political narratives centered on traditional gender roles may shape which identities become
focal points for attack.
19

--- Page 20 ---

AltNews
Gaming
General
SportForum
SportInfo
Warfare
 
0
20
40
60
80
100
top targeted genders (%)
64
51
59
51
51
66
27
41
33
45
46
24
6
7
6
3
8
Cisgender Female
Cisgender Male
Transgender
Non binary
Fig. 11: Top targeted gender identities across communities. Cisgender females are the most
targeted group overall, followed by cisgender males. The order of genders in the legend follows
their global frequency as targets
Overall, while the distribution of gender-based hate is less fragmented than other identity
categories, it reveals persistent patterns of gendered hostility, particularly toward women, that
resonate with broader sociocultural dynamics across online platforms.
Findings and Remarks
Our results show that hate speech in Italian Telegram communities
follows clear patterns, with specific identity groups being targeted. Some forms of hate, like
anti-Ukrainian sentiment in Warfare or hostility toward Arabs in sports discussions, depend
on the context. However, hate against Italians, Black people, and gay people is widespread
across all communities and independent from the topic.
6 Discussions and Limitations
We analyzed the Italian Telegram landscape, showing that communities tend to form around
ideological homophily. While most communities do not exhibit political orientation, we find
strong political leanings in certain communities. In particular, some communities show both
far-left and far-right rhetoric around geopolitical issues like the war in Ukraine, reflecting the
broader trend in Italian politics where extremist views from opposite ends of the spectrum
sometimes converge on specific topics. Moreover, by analyzing toxicity levels across differ-
ent communities, we show that online toxicity is not confined to ideological spaces, but is
also present in entertainment, adult-themed, and sports communities. In particular, the highly
emotional nature of sport fandoms and adult discussions promotes a competitive and more
aggressive tone. Our analysis of hate speech patterns further reinforces these findings. In fact,
vulnerable minorities, such as LGBTQ+ individuals and Black people are the most frequently
targeted identities across the communities, independently from the topic of the community.
Instead, nationality-based hate varies by community ideology. In particular, both AltNews
and Warfare communities present antisemitic discourse, with Israeli citizens being the most
20

--- Page 21 ---

targeted nationality, aligning with the broader political narratives of these communities. More-
over, AltNews exhibits strong pro-Russian sentiment and strong hate directed at Ukrainians
and Americans. Most importantly, results highlight a unique aspect of Italian online discourse,
which is the widespread hostility directed at other Italians. This intra-national antagonism is
rooted in historical regional divisions and cultural rivalries and emerges in all communities.
While most evident in sports-related discussions, it is not confined to this domain. Political
discussions also reflect this tendency, with users from different regions expressing resentment
toward one another. This suggests that, beyond ideological or ethnic divides, internal cultural
fragmentation plays an important role in shaping toxic interactions within the Italian Telegram
ecosystem.
6.1 Limitations
While our study provides an unprecedented level of insight into the Italian Telegram ecosystem,
it has certain limitations. In particular, the dataset contains public groups only and does not
include private chats that might contain interesting insights into specific topics (e.g., invitation-
only chats on cryptocurrency scam or pump-and-dump schemes [19]). As such, while our
dataset is one of the most comprehensive Italian collections, it does not capture the entire
Italian Telegram landscape. Nevertheless, we argue that the scale and scope of our dataset
provide a highly representative sample of public discussions within the platform. Given the
structure of Telegram, if a chat is not included in this dataset, it is likely because it operates in
a closed or isolated manner, receiving little engagement from the broader network of public
discussions.
7 Conclusions
In this paper, we presented the most comprehensive analysis of the Italian Telegram ecosys-
tem to date. We collected a large dataset of 186M messages from 13,151 chats. By employing
a network-based approach, we mapped Italian Telegram communities. By using LLMs and
the Perspective API, we characterized the thematic and political orientation of these com-
munities and investigated the prevalence and distribution of toxic discourse and hate speech.
Our findings reveal that Telegram communities exhibit strong ideological homophily. In addi-
tion, most politically engaged communities aligning with either far-right or far-left narratives,
although communities on geopolitical issues like the war in Ukraine show an ideological mix,
blending far-left and far-right rhetoric. We also find that toxicity within highly toxic commu-
nities is widely spread among chats. Moreover Entertainment, adult and sports communities,
which have no clear political stance, show very high levels of toxic content, suggesting that
harmful discourse is not exclusive to ideological spaces. Additionally, our analysis of hate
speech reveals that gay individuals, black people, and Jewish people are among the most
frequently targeted groups. Moreover, we find that nationality-based hate varies depending
on community ideology. However, broader Telegram discussions show high levels of intra-
national (regional and local) hostility, with Italians frequently targeting other Italians. These
findings show that hate speech on Telegram is driven by political views, topic, and cultural
fragmentation, highlighting the need for context-specific moderation strategies. Finally, our
dataset is limited to the Italian Telegram sphere, therefore findings may not be directly appli-
cable to other linguistic or national contexts. Future works could explore how these patterns
21

--- Page 22 ---

compare in English-language communities and investigate the factors that drive users toward
toxic behavior.
Acknowledgements.
This work was partly supported by SoBigData.it which receives fund-
ing from European Union – NextGenerationEU – National Recovery and Resilience Plan
(Piano Nazionale di Ripresa e Resilienza, PNRR) – Project: “SoBigData.it – Strengthening the
Italian RI for Social Mining and Big Data Analytics” – Prot. IR0000013 – Avviso n. 3264 del
28/12/2021.; and by project SERICS (PE00000014) under the NRRP MUR program funded
by the EU – NGEU. During the preparation of this work the author(s) used OpenAI chat-
GPT in order to proof-check the grammar of some paragraphs and refine the language. After
using this tool/service, the author(s) reviewed and edited the content as needed and take(s)
full responsibility for the content of the publication.
Declarations
Ethics approval and consent to participate
Not applicable.
Consent for publication
Not applicable.
Availability of data and materials
To ensure reproducibility, we released an anonymized, privacy-preserving version of the
network analysed during the current study, with the link to be provided upon acceptance.
Competing interests
The authors declare that they have no competing interests.
Funding
Not applicable.
Authors’ contributions
LA, ST, and MT conceived the research, interpreted the results, shaped the discussion, and
reviewed the manuscript. LA, ST, and MT performed the research. LA collected and analyzed
the data. LA, ST, and MT wrote the manuscript. ST and MT coordinated the research. All
authors read and approved the final version of the manuscript.
Appendix A
Prompts Submitted to the LLMs
This appendix presents the prompts provided to the LLMs leveraged in this work. Tables
report the prompt text as follows.
22

--- Page 23 ---

Prompt
Task: Label Telegram channels
Context: You will be provided with a sample of messages from a Telegram channel. Your task is
to assign the most appropriate label to the entire channel based on these messages, choosing from
a fixed list of categories.
Input:
• Fixed list of categories: <CATEGORIES>
• Chat name: <chat name>
• Chat description: <chat description>
• Sample messages: <messages>
Instructions:
1. Familiarize yourself with the provided categories.
2. Read all the messages from the channel.
3. Analyze the overall content, tone, and purpose.
4. Select up to 3 relevant categories, in order of importance.
5. Provide the result in the specified JSON format.
Output Format:
• {"categories": ["category1", "category2", "category3"]}
Notes:
• Select 1 to 3 categories in order of relevance.
• Do not create or merge categories.
• No explanations or extra information.
• Categories must exactly match those from input1.
Example Output:
• {"categories": ["anime", "arts", "games"]}
• If only two categories apply: {"categories": ["news", "politics"]}
Table A1: Prompt for topic labeling of Telegram chats using Mixtral:8x7B
Prompt
Task: Label Telegram channels
Context: You will be provided with a sample of messages from a Telegram channel. Your task is
to evaluate its political leaning.
Input:
The chat name: <chat name>
The chat description: <chat description>
A sample of messages from the Telegram channel: <messages>
Fixed list of labels: Far-right, right, right-center, center, left-center, left, far-left
Instructions:
1. Read through all the provided messages from the channel.
2. Analyze the overall content, tone, and purpose of the channel.
3. Choose the political leaning of the channel and label it with one of the given labels.
4. Output the result in the specified Python-readable JSON format.
Output Format: Provide your response in the following JSON structure:
{"political leaning": str | null}
Notes:
The key must always be ”political leaning.”
The value must be one of the given labels.
If you cannot label the political leaning from the given context, assign null.
Do not create new categories or combine existing ones.
Do not include any explanation or additional information.
Table A2: Prompt for political labeling of Telegram chats using ChatGPT-4o
23

--- Page 24 ---

Prompt
Task: Label Telegram message
Context: You will be provided with a message from Telegram which contains an attack over one
or more identities. Your task is to assign the most appropriate label to targeted individuals.
Input:
The message: <message>
Instructions:
1. Read the message.
2. Identify the most appropriate attacked identity or identities. You need to specify the specific
ethnicity, nationality, religion, gender, sexual orientation, disability, or other relevant identity
characteristics of the victim(s) of the attack.
3. Output the result in the specified JSON format.
Output Format: Provide your response in the following JSON structure:
{"targeted nationalities": list[str] | null,
"targeted ideologies": list[str] | null,
"targeted ethnicities": list[str] | null,
"targeted religions": list[str] | null,
"targeted sexual orientations": list[str] | null,
"targeted genders": list[str] | null,
"targeted age groups": list[str] | null,
"targeted disabilities": list[str] | null,
"targeted professions": list[str] | null,
"targeted social classes": list[str] | null,
"others": list[str] | null}
Notes: Do not include any explanation or additional information.
Table A3: Prompt for extracting hate targets from Telegram chats using Llama-3.1-
Nemotron-70B-Instruct
References
[1] Scheffler, T., Solopova, V., Popa-Wyatt, M.: The telegram chronicles of online harm.
Journal of Open Humanities Data 7 (2021)
[2] Schulze, H., Hohner, J., Greipl, S., Girgnhuber, M., Desta, I., Rieger, D.: Far-right
conspiracy groups on fringe platforms: A longitudinal analysis of radicalization dynam-
ics on telegram. Convergence: The International Journal of Research into New Media
Technologies 28(4), 1103–1126 (2022)
[3] Hoseini, M., Melo, P., Benevenuto, F., Feldmann, A., Zannettou, S.: On the globalization
of the qanon conspiracy theory through telegram. In: Proceedings of the 15th ACM Web
Science Conference 2023, pp. 75–85 (2023)
[4] Alvisi, L., Tardelli, S., Tesconi, M.: Unraveling the italian and english telegram
conspiracy spheres through message forwarding. arXiv preprint arXiv:2404.18602
(2024)
[5] Urman, A., Katz, S.: What they do in the shadows: examining the far-right networks on
telegram. Information, communication & society 25(7), 904–923 (2022)
24

--- Page 25 ---

[6] Walther, S., McCoy, A.: Us extremism on telegram. Perspectives on Terrorism 15(2),
100–124 (2021)
[7] Ng, L.H.X., Loke, J.Y.: Analyzing public opinion and misinformation in a covid-19
telegram group chat. IEEE Internet Computing 25(2), 84–91 (2020)
[8] Willaert, T., Peeters, S., Seijbel, J., Van Raemdonck, N.: Disinformation networks: A
quali-quantitative investigation of antagonistic dutch-speaking telegram channels. First
Monday (2022)
[9] Ng, L.H.X., Kloo, I., Clark, S., Carley, K.M.: An exploratory analysis of covid bot
vs human disinformation dissemination stemming from the disinformation dozen on
telegram. Journal of Computational Social Science, 1–26 (2024)
[10] Zihiri, S., Lima, G., Han, J., Cha, M., Lee, W.: Qanon shifts into the mainstream, remains
a far-right ally. Heliyon 8(2) (2022)
[11] Calamusa, A., Tardelli, S., Avvenuti, M., Cresci, S., Federigi, I., Tesconi, M., Verani,
M., Carducci, A.: Twitter monitoring evidence of covid-19 infodemic in italy. European
Journal of Public Health 30(Supplement 5), 165–066 (2020)
[12] Corti, L., Zanetti, M., Tricella, G., Bonati, M.: Social media analysis of twitter tweets
related to asd in 2019–2020, with particular attention to covid-19: topic modelling and
sentiment analysis. Journal of big data 9(1), 113 (2022)
[13] Hashemi, M.: Geographical visualization of tweets, misinformation, and extremism
during the usa 2020 presidential election using lstm, nlp, and gis. Journal of Big Data
10(1), 125 (2023)
[14] Gambini, M., Tardelli, S., Tesconi, M.: The anatomy of conspiracy theorists: unveiling
traits using a comprehensive twitter dataset. Computer Communications 217, 25–40
(2024)
[15] Bloom, M., Tiflati, H., Horgan, J.: Navigating isis’s preferred platform: Telegram1.
Terrorism and Political Violence 31(6), 1242–1254 (2019)
[16] Vavryk, P.: Mapping growth of the russian domestic propaganda apparatus on telegram.
Challenges to national defence in contemporary geopolitical situation 2022(1), 227–231
(2022)
[17] Castagna, S., Porrino, G., Borgonovo, F.: The italian pro-russia digital ecosystem on
telegram. Cybersecurity and Law 10 (2023)
[18] Bovet, A., Grindrod, P.: Organization and evolution of the uk far-right network on
telegram. Applied Network Science 7(1), 76 (2022)
[19] Nizzoli, L., Tardelli, S., Avvenuti, M., Cresci, S., Tesconi, M., Ferrara, E.: Charting
the landscape of online cryptocurrency manipulation. IEEE access 8, 113230–113245
25

--- Page 26 ---

(2020)
[20] Guhl, J., Davey, J.: A safe space to hate: White supremacist mobilisation on telegram.
Institute for Strategic Dialogue 26 (2020)
[21] Pasquetto, I.V., Olivieri, A.F., Tacchetti, L., Riotta, G., Spada, A.: Disinformation as
infrastructure: Making and maintaining the qanon conspiracy on italian digital media.
Proceedings of the ACM on Human-Computer Interaction 6(CSCW1), 1–31 (2022)
[22] Vergani, M., Martinez Arranz, A., Scrivens, R., Orellana, L.: Hate speech in a telegram
conspiracy channel during the first year of the covid-19 pandemic. Social Media+ Society
8(4), 20563051221138758 (2022)
[23] Morgia, M.L., Mei, A., Mongardini, A.M.: TGDataset: a Collection of Over One Hundred
Thousand Telegram Channels (2023)
[24] Baumgartner, J., Zannettou, S., Squire, M., Blackburn, J.: The pushshift telegram dataset.
In: Proceedings of the International AAAI Conference on Web and Social Media, vol.
14, pp. 840–847 (2020)
[25] Tardelli, S., Nizzoli, L., Avvenuti, M., Cresci, S., Tesconi, M.: Multifaceted online
coordinated behavior in the 2020 us presidential election. EPJ Data Science 13(1), 33
(2024)
[26] Pierri, F.: Drivers of hate speech in political conversations on twitter: the case of the
2022 italian general election. EPJ Data Science 13(1), 63 (2024)
[27] Avalle, M., Di Marco, N., Etta, G., Sangiorgio, E., Alipour, S., Bonetti, A., Alvisi, L.,
Scala, A., Baronchelli, A., Cinelli, M., et al.: Persistent interaction patterns across social
media platforms and over time. Nature 628(8008), 582–589 (2024)
[28] Cavalini, A., Donadia, T., Comarela, G.: Characterizing the toxicity of the brazilian
extremist communities on telegram (2024)
[29] Wich, M., Gorniak, A., Eder, T., Bartmann, D., Cakici, B.E., Groh, G.: Introducing an
abusive language classification framework for telegram to investigate the german hater
community. In: Proceedings of the International AAAI Conference on Web and Social
Media, vol. 16, pp. 1133–1144 (2022)
[30] Blas, L., Luceri, L., Ferrara, E.: Unearthing a billion telegram posts about the 2024 us
presidential election: Development of a public dataset. arXiv preprint arXiv:2410.23638
(2024)
[31] La Morgia, M., Mei, A., Mongardini, A.M., Wu, J.: It’sa trap! detection and analysis
of fake channels on telegram. In: 2023 IEEE International Conference on Web Services
(ICWS), pp. 97–104 (2023). IEEE
[32] Tikhomirova, K., Makarov, I.: Community detection based on the nodes role in a network:
26

--- Page 27 ---

The telegram platform case. In: Analysis of Images, Social Networks and Texts: 9th
International Conference, AIST 2020, Skolkovo, Moscow, Russia, October 15–16, 2020,
Revised Selected Papers 9, pp. 294–302 (2021). Springer
[33] Dugu´e, N., Perez, A.: Directed louvain: maximizing modularity in directed networks.
PhD thesis, Universit´e d’Orl´eans (2015)
[34] Jiang, A.Q., Sablayrolles, A., Roux, A., Mensch, A., Savary, B., Bamford, C., Chaplot,
D.S., Casas, D.d.l., Hanna, E.B., Bressand, F., et al.: Mixtral of experts. arXiv preprint
arXiv:2401.04088 (2024)
[35] Ackland, R., Shorish, J.: Political homophily on the web. In: Analyzing Social Media
Data and Web Networks, pp. 25–46. Springer, ??? (2014)
[36] Halberstam, Y., Knight, B.: Homophily, group size, and the diffusion of political infor-
mation in social networks: Evidence from twitter. Journal of public economics 143,
73–88 (2016)
[37] OpenAI: ChatGPT-4o: OpenAI’s Multimodal Conversational AI. Accessed: 2024-02-10
(2024). https://openai.com
[38] Burnham, M.: Stance detection: a practical guide to classifying political beliefs in text.
Political Science Research and Methods, 1–18 (2024)
[39] Zhang, B., Fu, X., Ding, D., Huang, H., Dai, G., Yin, N., Li, Y., Jing, L.: Investigat-
ing chain-of-thought with chatgpt for stance detection on social media. arXiv preprint
arXiv:2304.03087 (2023)
[40] Tardelli, S., Nizzoli, L., Tesconi, M., Conti, M., Nakov, P., Da San Martino, G., Cresci, S.:
Temporal dynamics of coordinated online behavior: Stability, archetypes, and influence.
Proceedings of the National Academy of Sciences 121(20), 2307038121 (2024)
[41] Schick, T., Sch¨utze, H.: Exploiting cloze questions for few shot text classification and
natural language inference. arXiv preprint arXiv:2001.07676 (2020)
[42] Lees, A., Tran, V.Q., Tay, Y., Sorensen, J., Gupta, J., Metzler, D., Vasserman, L.: A
new generation of perspective api: Efficient multilingual character-level transformers.
In: Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and
Data Mining, pp. 3197–3207 (2022)
[43] Hua, Y., Ristenpart, T., Naaman, M.: Towards measuring adversarial twitter interactions
against candidates in the us midterm elections. In: Proceedings of the International AAAI
Conference on Web and Social Media, vol. 14, pp. 272–282 (2020)
[44] Saveski, M., Roy, B., Roy, D.: The structure of toxic conversations on twitter. In:
Proceedings of the Web Conference 2021, pp. 1086–1097 (2021)
[45] Nobata, C., Tetreault, J., Thomas, A., Mehdad, Y., Chang, Y.: Abusive language detection
27

--- Page 28 ---

in online user content. In: Proceedings of the 25th International Conference on World
Wide Web, pp. 145–153 (2016)
[46] Ashforth, B.E., Mael, F.: Social identity theory and the organization. Academy of
management review 14(1), 20–39 (1989)
[47] Wang, Z., Bukharin, A., Delalleau, O., Egert, D., Shen, G., Zeng, J., Kuchaiev, O.,
Dong, Y.: HelpSteer2-Preference: Complementing Ratings with Preferences (2024).
https://arxiv.org/abs/2410.01257
[48] Parmar, J., Prabhumoye, S., Jennings, J., Patwary, M., Subramanian, S., Su, D., Zhu,
C., Narayanan, D., Jhunjhunwala, A., Dattagupta, A., et al.: Nemotron-4 15b technical
report. arXiv preprint arXiv:2402.16819 (2024)
[49] Gallagher, R.J., Frank, M.R., Mitchell, L., Schwartz, A.J., Reagan, A.J., Danforth, C.M.,
Dodds, P.S.: Generalized word shift graphs: a method for visualizing and explaining
pairwise comparisons between texts. EPJ Data Science 10(1), 4 (2021)
[50] Mann, H.B., Whitney, D.R.: On a test of whether one of two random variables is
stochastically larger than the other. The annals of mathematical statistics, 50–60 (1947)
[51] Kearns, C., Sinclair, G., Black, J., Doidge, M., Fletcher, T., Kilvington, D., Liston,
K., Lynn, T., Rosati, P.: A scoping review of research on online hate and sport.
Communication & Sport 11(2), 402–430 (2023)
[52] Beres, N.A., Frommel, J., Reid, E., Mandryk, R.L., Klarkowski, M.: Don’t you know that
you’re toxic: Normalization of toxicity in online gaming. In: Proceedings of the 2021
CHI Conference on Human Factors in Computing Systems, pp. 1–15 (2021)
[53] Gini, C.: Variabilit`a e Mutabilit`a. Contributo Allo Studio delle Distribuzioni e delle
Relazioni Statistiche. Tipografia di P. Cuppini, Bologna (1912)
[54] Tak, H.: Changing campanilismo. Ethnologia Europaea 18(1), 149–160 (1988)
[55] Villano, P., Passini, S.: Competent in the north, passionate in the south. stereotypes and
prejudices between northern and southern italy. Psicologia sociale 13(2), 91–106 (2018)
[56] U.S. Office of Management and Budget: Revisions to the Standards for the Classifi-
cation of Federal Data on Race and Ethnicity. https://www.govinfo.gov/content/pkg/
FR-1997-10-30/pdf/97-28653.pdf. Federal Register, Vol. 62, No. 210, October 30, 1997
(1997)
[57] Istituto Nazionale di Statistica (ISTAT): Annuario statistico italiano 2023. https://www.
istat.it/storage/ASI/2023/ASI 2023.pdf. Edizione n. 145, Roma (2023)
[58] Silva, L., Mondal, M., Correa, D., Benevenuto, F., Weber, I.: Analyzing the targets of
hate in online social media. In: Proceedings of the International AAAI Conference on
Web and Social Media, vol. 10, pp. 687–690 (2016)
28

--- Page 29 ---

[59] Chaudhry, I., Gruzd, A.: Expressing and challenging racist discourse on facebook: How
social media weaken the “spiral of silence” theory. Policy & Internet 12(1), 88–108
(2020)
[60] Aparicio-Garc´ıa, M.E., D´ıaz-Ramiro, E.M., Rubio-Valdehita, S., L´opez-N´u˜nez, M.I.,
Garc´ıa-Nieto, I.: Health and well-being of cisgender, transgender and non-binary young
people. International Journal of Environmental Research and Public Health 15(10), 2133
(2018)
[61] Richards, C., Bouman, W.P., Seal, L., Barker, M.J., Nieder, T.O., T’Sjoen, G.: Non-binary
or genderqueer genders. International Review of Psychiatry 28(1), 95–102 (2016)
[62] Nadim, M., Fladmoe, A.: Silencing women? gender and online harassment. Social
Science Computer Review 39(2), 245–258 (2021)
[63] Erikson, J., H˚akansson, S., Josefsson, C.: Three dimensions of gendered online abuse:
Analyzing swedish mps’ experiences of social media. Perspectives on Politics 21(3),
896–912 (2023)
29

```
