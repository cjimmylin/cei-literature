---\ntitle: "2024-Akhunzada-Multi-IsnadSet MIS for Sahih Muslim Hadith - PDF Extract"\nsource_pdf: "2024-Akhunzada-Multi-IsnadSet MIS for Sahih Muslim Hadith.pdf"\npages: 11\nextracted_at: "2026-02-14T06:21:39"\n---\n\n# PDF Extract: 2024-Akhunzada-Multi-IsnadSet MIS for Sahih Muslim Hadith\n\n**Source PDF:** 2024-Akhunzada-Multi-IsnadSet MIS for Sahih Muslim Hadith.pdf\n**Total Pages:** 11\n\n---\n\n## Content\n\n```\n--- Page 1 ---\n\nData in Brief 54 (2024) 110439 
Contents lists available at ScienceDirect 
Data in Brief 
journal homepage: www.elsevier.com/locate/dib 
Data Article 
Multi-IsnadSet MIS for Sahih Muslim Hadith 
with chain of narrators, based on multiple 
ISNAD 
Aziz Mehmood Farooqi a , b , ∗∗, Rauf Ahmed Shams Malick b , e , ∗∗, 
Muhammad Shahzad Shaikh c , Adnan Akhunzada d , ∗
a College of Computing and Information Sciences PAF Karachi Institute of Economics and Technology, Karachi, 
Pakistan 
b Department of Computer Science, FAST-National University of Computer and Emerging Sciences, Karachi 75300, 
Pakistan 
c Department of Sciences and Humanities, FAST-National University of Computer and Emerging Sciences, Karachi 
75300, Pakistan 
d College of Computing & IT, University of Doha for Science and Technology, P.O. Box 24 4 49, Doha, Qatar 
e Al-Ghazali University, Karachi, Sindh, Pakistan 
a r t i c l e 
i n f o 
Article history: 
Received 4 February 2024 
Revised 25 March 2024 
Accepted 12 April 2024 
Available online 23 April 2024 
Dataset link: Multi-IsnadSet MIDS for Sahih 
Muslim Hadith with chain of Narrators, 
based on multiple ISNAD (Original data) 
Keywords: 
Multi-Isnad of Hadith Narrators dataset 
Chain of narrators 
Machine learning 
Graph database 
Spatial–Temporal data 
Social-Network Analysis (SNA) 
Graph Neural Networks (GNN) 
a b s t r a c t 
In the Islamic domain, Hadiths hold signiﬁcant importance, 
standing as crucial texts following the Holy Quran. Each Ha- 
dith contains three main parts: the ISNAD (chain of narra- 
tors), TARAF (starting part, often from Prophet Muhammad), 
and MATN (Hadith content). ISNAD, a chain of narrators in- 
volved in transmitting that particular MATN. Hadith scholars 
determine the trustworthiness of the transmitted MATN by 
the quality of the ISNAD. The ISNAD’s data is available in its 
original Arabic language, with narrator names transliterated 
into English. 
This paper presents the Multi-IsnadSet (MIS), that has great 
potential to be employed by the social scientist and the- 
ologist. A multi-directed graph structure is used to repre- 
sents the complex interactions among the narrators of Ha- 
dith. The MIS dataset represent directed graph which con- 
∗Corresponding author. 
∗∗Corresponding authors at: College of Computing and Information Sciences PAF Karachi Institute of Economics and 
Technology, Karachi, Pakistan. 
E-mail addresses: aziz.farooqi@kiet.edu.pk , k214809@nu.edu.pk (A.M. Farooqi), rauf.malick@nu.edu.pk (R.A.S. Malick), 
shahzad.shaikh@nu.edu.pk (M.S. Shaikh), Adnan.adnan@udst.edu.qa (A. Akhunzada). 
https://doi.org/10.1016/j.dib.2024.110439 
2352-3409/© 2024 The Authors. Published by Elsevier Inc. This is an open access article under the CC BY license 
( http://creativecommons.org/licenses/by/4.0/ ) 

--- Page 2 ---\n\n2 
A.M. Farooqi, R.A.S. Malick and M.S. Shaikh et al. / Data in Brief 54 (2024) 110439 
sists of 2092 nodes, representing individual narrators, and 
77,797 edges represent the Sanad-Hadith connections. The 
MIS dataset represents multiple ISNAD of the Hadith based 
on the Sahih Muslim Hadith book. The dataset was care- 
fully extracted from online multiple Hadith sources using 
data scraping and web crawling techniques tools, provid- 
ing extensive Hadith details. Each dataset entry provides 
a complete view of a speciﬁc Hadith, including the orig- 
inal book, Hadith number, textual content (MATN), list of 
narrators, narrator count, sequence of narrators, and ISNAD 
count. In this paper, four different tools were designed and 
constructed for modeling and analyzing narrative network 
such as python library (NetworkX), powerful graph database 
Neo4j and two different network analysis tools named Gephi 
and CytoScape. The Neo4j graph database is used to rep- 
resent the multi-dimensional graph related data for the 
ease of extraction and establishing new relationships among 
nodes. Researchers can use MIS to explore Hadith credi- 
bility including classiﬁcation of Hadiths (Sahih = perfection 
in the Sanad/Dhaif = imperfection in the Sanad), and narra- 
tors (trustworthy/not). Traditionally, scholars have focused on 
identifying the longest and shortest Sanad between two Nar- 
rators, but in MIS, the emphasis shifts to determining the 
optimum/authentic Sanad, considering narrator qualities. The 
graph representation of the authentic and manually curated 
dataset will open ways for the development of computational 
models that could identify the signiﬁcance of a chain and a 
narrator. The dataset allows the researchers to provide Ha- 
dith narrators and Hadith ISNAD that could be used in a wide 
variety of future research studies related to Hadith authen- 
tication and rules extraction. Moreover, the dataset encour- 
ages cross-disciplinary research, bridging the gap between Is- 
lamic studies, artiﬁcial intelligence (AI), social network anal- 
ysis (SNA), and Graph Neural Network (GNN). 
© 2024 The Authors. Published by Elsevier Inc. 
This is an open access article under the CC BY license 
( http://creativecommons.org/licenses/by/4.0/ ) 
Speciﬁcations Table 
Subject 
Computer Science. 
Speciﬁc subject area 
Islamic Hadith corpus, Multi-Isnad of Hadith Narrators, Social Network 
Analysis (SNA), Graph Neural Network (GNN). Neo4j Graph Database 
Type of data 
Text ﬁle, Table, Graph etc. 
Filtered, Processed etc. 
How to data were acquired 
The dataset was collected from Hadith websites (these Hadiths originated from 
ancient Islamic Hadith book named Sahih Muslim). 
We used data scraping & web crawling with the help of Python Libraries such 
as Selenium automated agent-based library and Beautiful Soup to acquire the 
dataset with data cleaning and labelling. 
Data Format 
Raw: NetworkX Python Library dump 
Raw: Different Visualization & Exploration softwares (Gephi, Cytoscape, and 
Social Network Visualizer) dump 
Raw: Neo4J database dump 
Geography Markup Language format (.gml), XML-based graph format 
(.graphml) 
( continued on next page ) 

--- Page 3 ---\n\nA.M. Farooqi, R.A.S. Malick and M.S. Shaikh et al. / Data in Brief 54 (2024) 110439
3 
Description of Data collection 
The dataset used in this study was sourced from reputable repositories such as 
all data of Sahih Muslim with their multiple ISNAD and their narrators have 
been collected from Ihsan-Network website [ 1 ] and detail info of Narrator’s 
data has been scrapped from Muslim-Scholar website [ 2 ] so that the narrator’s 
could be assigned with the unique global identity. It was a big challenge for 
matching/mapping narrator’s name from both two sides, at last it has been 
achieved by some our logical code script and some fuzzywuzzy (python) 
library. Finally mapped manually for remaining narrator’s names which could 
not be mapped via automated logic. Detailed information about each dataset 
source is provided in Tables 1, 2 and 3. We conducted a thorough assessment 
to determine the potential impact of each source on the generated dataset, 
ensuring transparency and reliability in our data collection process. 
We collaborated with domain experts in Islamic studies to validate the 
authenticity and relevance of the dataset. 
The collection and processing of the dataset are based on two steps: 
1. The data including the Hadith number, Narrators numbers, Sanad 
numbers, ISNAD wise Narrators sequence, Source Narrators & Target 
Narrators for each Hadith Sanad ﬁelds are collected from Hadith websites. 
The raw text is further processed to separate Hadith components such as 
Chapter, MATN, and Narrators. The resulting Chapter, MATN and Sanad ﬁelds 
are stored in separate columns. 
Data source location 
Data was gathered till December 2023, with random web crawls carried out to 
ensure adequate global coverage. 
Scraped/crawled it from https://www.ihsanetwork.org/hadith.aspx and 
http://muslimscholars.info/ using the Python Selenium automated agent-based 
library and Beautiful Soup to acquire the dataset with data wrangling and 
labelling. 
Data accessibility 
Repository name: Mendeley Data 
Data identiﬁcation number: 10.17632/gzprcr93zn.2 
Direct URL to data: https://data.mendeley.com/datasets/gzprcr93zn/2 
Instructions for accessing these data: MIS contains three excel sheets (Table 1, 
Table 2 and Table 3) 
1. Value of the Data 
• Multi-IsnadSet is created for future research on the public repository for all the Research 
Institutes, Scientiﬁc and Islamic communities who want to work on Multi-ISNAD of Hadith 
including classiﬁcation of Hadiths (Sahih = perfection in the Sanad/Dhaif = imperfection in the 
Sanad) [ 3 ], and narrators (trustworthy/not) [ 4–9 ]. 
• The data can be used to build Hadith software tools for establishing social networks or graph 
neural network and it can become an imported source for information interaction and map- 
ping high level relationships [ 10–13 ] 
This dataset offers signiﬁcant value and contributions to multiple research areas with 
categorized way: 
(1) Islamic Hadith Studies: 
• Provides a comprehensive dataset for studying Hadith narrators, ISNAD chains, and Ha- 
dith propagation in a structured graph format. 
• This data is available in the public repository for all the Research Institutes, Scientiﬁc 
and Islamic communities who want to work on Hadith Narrators and Hadith ISNAD. 
(2) Hadith Authentication: 
• Researchers can explore the dataset to analyze the authenticity and credibility of Ha- 
dith narrators, ISNAD chains, and the propagation of Hadith in a structured graph for- 
mat 
• Provides Hadith narrators and Hadith ISNAD that could be used in a wide variety of 
future research studies related to Hadith authentication and rules extraction. 
(3) Graph Neural Networks (GNN):- The dataset is conducive to the application of Graph Neu- 
ral Networks (GNNs) and offers exciting possibilities: 

--- Page 4 ---\n\n4 
A.M. Farooqi, R.A.S. Malick and M.S. Shaikh et al. / Data in Brief 54 (2024) 110439 
• Node Embedding: GNNs can be employed to generate embeddings for each narrator, 
capturing their positions within the Hadith network. 
• Community Detection: GNNs can assist in the automatic detection of narrator commu- 
nities based on their interactions and shared characteristics. 
• Link Prediction: GNNs can predict missing Sanad-Hadith relationships, helping recon- 
struct and validate the Hadith network. 
• Graph Classiﬁcation: Researchers can use GNNs to classify narrators based on their 
attributes, authenticity, or credibility. 
(4) Social Network Analysis (SNA):- This dataset offers unique opportunities for Social Net- 
work Analysis (SNA) researchers according to ﬁnd Microscopic, Macroscopic, and Meso- 
scopic properties of Narrative Network.: 
• Network Structure: Researchers can examine the structural properties of the Hadith 
network, uncovering key characteristics such as network density, centrality measures, 
and clustering coeﬃcients. 
• Centrality Analysis: SNA metrics like degree centrality, betweenness centrality, and 
eigenvector centrality can be applied to identify inﬂuential narrators and nodes within 
the Hadith network. 
• Community Detection: Advanced community detection algorithms can be used to 
group narrators with similar attributes or roles, shedding light on the organization of 
the Hadith network. 
• Propagation Patterns: SNA techniques can reveal how Hadith propagate through narra- 
tors, providing insights into the ﬂow of information within the network. 
(5) Neo4j Graph Database: 
• Enables researchers to test and develop graph algorithms within a well-established 
database environment. 
• Integration with Neo4j, a powerful graph database platform, enhances the dataset’s 
utility: 
• Graph Algorithms: Neo4j ʼs extensive library of graph algorithms can be applied to per- 
form tasks such as ﬁnding the most inﬂuential narrators, identifying shortest paths, 
and detecting network anomalies. 
• Cypher Query Language: Researchers can leverage Cypher, Neo4j ʼs query language, for 
versatile and eﬃcient graph data retrieval, exploration, and analysis. 
• Scalability: Neo4j ʼs scalability ensures that the dataset can accommodate the demands 
of large-scale analyses, making it suitable for comprehensive Hadith research. 
(6) Cross-Disciplinary Research: 
• Encourages collaboration between scholars from Islamic studies, social network analy- 
sis, artiﬁcial intelligence and Machine Learning. 
• Facilitates interdisciplinary research, promoting transparency and reproducibility. 
2. Background 
The Hadiths, or Prophetic traditions, are narrations originating from the sayings and conduct 
of Prophet Muhammad (peace be upon him). Initially, the Hadiths were orally transmitted and 
a few decades later were committed into written form collected as small booklets. However, by 
the end of the second century Hijra (Islamic Calendar), scholars started compiling Hadiths into 
large collections classifying them subject wise. This work tackles the collection of Hadiths in 
Sahih of Muslim, named after Imam Muslim (d. CE 875). This collection along with that of Sahih 
of Bukhari (d. CE 870) are considered the most authentic collection since only the Hadiths with 
the most reliable transmitters were included in the collection. 
The Hadith takes the form: Narr-1 → Narr-2 → Narr-3 → … → Narr-k, followed by the text 
of the Hadith (or, the statement of the Hadith which is also known as MATN). The ISNAD, the 
chain of narrators, is a reverse chronological chain of narrators involved in transmitting this 
particular statement. So, Narr-k is the prime narrator who personally heard the Prophet says the 

--- Page 5 ---\n\nA.M. Farooqi, R.A.S. Malick and M.S. Shaikh et al. / Data in Brief 54 (2024) 110439
5 
Fig. 1. Narrator’s network of three multiple transmission chain (ISNAD) of single Hadith represented using multiple 
edges. 
statement. The importance of ISNAD is that it gives credibility to the transmitted statement. Has 
it been transmitted exactly as said (word for word), or by meaning. To accomplish this, scholars 
study the history of each narrator taking into consideration, his memory, his truthfulness, etc. 
This data article transformed the chains of narrations along with narrators into graphs and 
represented through knowledge graphs developed in Neo4j. The resultant knowledge graph will 
allow scientists across the disciplines to perform better analysis over structured information ac- 
cordingly. 
This dataset aims to provide a structured representation of MIS in Sahih Muslim Hadith, al- 
lowing for in-depth analysis of narrator chains and Hadith propagation. 
3. Data Description 
The earliest work reported regarding the computational studies of Hadith was by Mustafa 
AlAzami [ 14 ]. A Hadith is a narrative by the Holy Prophet Muhammad (Peace be upon him). A 
Hadith consists on two basic constituents including the narrative and the chain of narrators. The 
manual curation process that performs strict analysis over a chain of narrators is termed as IS- 
NAD ( Fig. 1 ). The ISNAD are being evaluated throughout the chain/transmission narrators till the 
actual source of the narrative. The evaluation process includes the authentication of a narrator 
and ranking among speciﬁc classes in terms of credibility along with the thorough inspection of 
the continuity of the narration. 
There are some qualities that are essential to determine the credibility and authenticity of 
Hadith in the narrators of the Hadith, which have been developed by Hadith experts around 

--- Page 6 ---\n\n6 
A.M. Farooqi, R.A.S. Malick and M.S. Shaikh et al. / Data in Brief 54 (2024) 110439 
Table 1 
Speciﬁcation for Dataset File (1_Hadith_SahihMuslim_HadithContent.xlsx). 
Seq. No Attribute 
Description 
Example Value 
1 
BookNo 
Global ID of the Hadith 
Book 
2 
2 
BookTitleEnAr 
Book Title with English and 
Arabic Text 
Sahih Muslim -  ملسملا حیحصلا
3 
HadithNo 
Unique Hadith No of the 
particular Book 
1 
4 
ChapterNo 
Unique Chapter No of the 
particular Book 
1 
5 
ChapterTitleAr 
Chapter Title with Arabic 
Text 
 ةمدقملا
6 
ChapterTitleEn 
Chapter Title with English 
Text 
Introduction -  ةمدقملا باتك
7 
UnitNo 
Unique Unit No of the 
particular Chapter 
1 
8 
UnitTitleAr 
Unit Title with Arabic Text  . نيباذكلا كرتو تاقثلا نع ةياورلا بوجو باب
9 
HadithText_Mushakkal 
Arabic Hadith Content with 
Diacritize text 
‏ "‏ َنيِبِذاَكْلا ُدَحَأ َوُهَف ٌبِذَك ُهَّنَأ ىَرُي ٍثيِدَحِب ،يِّنَع َثَّدَح ْنَم ‏ "‏
10 
HadithText_GhairMushakkal Arabic Hadith Content 
without Diacritize 
‏ "‏ نيبذاكلا دحأ وهف بذك هنأ ىري ثيدحب ،ينع ثدح نم ‏ "‏
11 
SanadCount 
Sanad Count of the 
particular Hadith 
3 
12 
SanadWithNarratorsCount 
e.g. 3 ISNAD & 6 Narrators 
for each Sanad 
1 = 6,2 = 6,3 = 6 
Table 2 
Speciﬁcation for Dataset File (2_Hadith_SahihMuslim_Narrators = Nodes for Graph.xlsx). 
Seq. No 
Attribute 
Description 
Example value 
1 
NarratorID_Mapped 
Global Narrator ID for Node Unique ID 
2 
2 
NarratorNameAr 
Narrator Complete Name in Arabic Text  قيدصلا ركب وبأ نامثع نب هللا دبع
3 
NarratorNameAr-Mapped 
Narrator Short Name in Arabic Text  قيدصلا ركب وبأ
4 
NarratorNameEn-Mapped 
Narrator Name for Node Label Property 
Abu Bakr As-Siddique (0) 
5 
Gender 
Narrator Gender for Node property 
Male 
6 
NarratorGeneration 
Narrator Generation for Node property 
Comp.(RA) 
1200 years ago. The study resulted into the advent of a new area of social studies named as 
Asma-ul-Rijal and Ilm-ul-Rijal (The study of authentication analysis of Hadith narrators). 
This includes the narrator of the Hadith should be of ﬁrm faith, be honest, be righteous and 
trustworthy, have an excellent memory as well, have sound knowledge of the QURAN, HADITH 
and FIQAH, should report the exact words without using any word from his own. Chain continu- 
ity, integrity of narrators’ character, report precision, non-deﬁciency and non-aberrance are also 
essential for authentic criteria of Hadith. 
The dataset in the article provides a valuable resource for machine learning tasks aimed at 
addressing the authenticity of Hadiths. For example, it can be utilized for sentiment analysis 
[15] , classiﬁcation, and clustering of Hadith [ 16 , 17 ]. By applying machine learning techniques to 
this dataset, researchers can gain deeper insights into the reliability and authenticity of various 
Hadiths, contributing to the broader discourse on Islamic scholarship [18] . 
This dataset contains three excel sheets ( Tables 1–3 ): Hadith document (7748 records) and 
Narrators of Multi-Isnad document (77,797 records). The data contains 7748 Hadith 2092 unique 
records of Narrators of all Sahih Muslim Hadith. Total records of ISAND are 14,155 is presented 
in Figs. 2 and 3 : 
The ﬁrst major generation records result is Follower_Tabi with 1013 Narrators (50.3 %) and 
Succ_TabaTabi, Comp_RA and Century_3rd_AH ranked second, third and fourth with 438 Narra- 

--- Page 7 ---\n\nA.M. Farooqi, R.A.S. Malick and M.S. Shaikh et al. / Data in Brief 54 (2024) 110439
7 
Table 3 
Speciﬁcation for Dataset File (3_Hadith_SahihMuslim_Isnad = Edges for Graph.xlsx). 
Seq. No 
Attribute 
Description 
Example value 
1 
BookNo 
Global ID of the Hadith Book 
2 
2 
HadithNo 
Unique Hadith No of the particular Book 
1 
3 
ChapterNo 
Unique Chapter No of the particular Book 
1 
4 
UnitNo 
Unique Unit No of the particular Chapter 
1 
5 
SanadNo 
Unique Sanad No of the particular Hadith 
1 
6 
sourceNarratorID 
Source Node ID for Directed Graph 
166 
7 
sourceNarratorNameEn 
Source Node property 
al-Mughira ibn Shu’ba (0) 
8 
targetNarratorID 
Target Node ID for Directed Graph 
10,834 
11 
targetNarratorNameEn 
Target Node property 
Maymun bin Abi Shbyb 
12 
intractionLabel 
Complete info of Single Hadith’s SANAD for 
Edge property 
B2-H0 0 01-C01-U01-S01-i1 
Fig. 2. Statistical analysis Hadith according to Multiple ISNAD. 
tors (21.8 %), 290 Narrators (14.4 %) and 271 Narrators (13.5 %) respectively. Fig. 3 shows the 
generation’s categories according Sahih Muslim Hadith book. 
A complete picture of the Global Hadith SANAD Narrator’s Network from the book Sahih 
Muslim with 2092 total number of Narrators (nodes) and 63,643 total number of their Trans- 
mission (edges) has been shown in Fig. 4 . 
4. Experimental Design, Materials and Methods 
Data Collection and Preprocessing: The dataset’s creation followed a systematic approach: 
• Data Extraction: Information was sourced from Islamic texts, Hadith databases, and au- 
thoritative references. Data extraction focused on collecting Hadith text, ISNAD chains, and 
narrator details. 
• Data Transformation: The collected data underwent transformation to represent narrators 
as nodes and ISNAD-Hadith relationships as edges in the graph structure. 
• Quality Control: Stringent quality control checks were implemented to ensure the 
dataset’s accuracy. This included standardizing naming conventions, resolving discrepan- 
cies, and addressing any missing or erroneous data points. 

--- Page 8 ---\n\n8 
A.M. Farooqi, R.A.S. Malick and M.S. Shaikh et al. / Data in Brief 54 (2024) 110439 
Fig. 3. Statistical analysis for four classiﬁcation of narrator’s generation. 
Fig. 4. Narrator’s network with multiple ISNAD represented by Python LIBRARY. 
Multi-IsnadSet Statistics: The dataset’s statistics include: 
• Nodes (Narrators): 2092 individual narrators. 
• Edges (Sanad-Hadith Relationships): 77,797 relationships representing the propagation of 
Hadith through narrators. 
The data is crawled from multiple web sources (that are manually curated), then data was 
pre-processed (cleaning, removing stop-Word, normalizing Arabic letter etc.) and merged. A few 
mismatched narrator’s names are found from different resources. The mismatch issue is resolved 
by different logical code script and fuzzywuzzy (python) library. The study attempted to match 
the complete name of narrators mentioned in Hadith while normally transmitter’s full name is 
not mentioned in given Hadith. The transmitters who have similar names in context of chain of 
narrators are further investigated. All unique chains of narrations that reports the same Hadith 
with little variation of words are identiﬁed and reported. Similarly, all different chains of single 

--- Page 9 ---\n\nA.M. Farooqi, R.A.S. Malick and M.S. Shaikh et al. / Data in Brief 54 (2024) 110439
9 
Table 4 
Narrator’s network with multiple ISNAD including single Hadith represented by three different network tools (Neo4j –
Gephi – CytoScape). 
Hadith are identiﬁed and mentioned separately having a variation in narrator’s chain. The social 
network of narrators and chain of narrators is represented through a graph G(V, E) where ver- 
tices represents the narrators and edges represented the narrations. Multiple tools are employed 
in representation, analysis and database for graphs including Python Library (NetworkX), Graph 
Database Neo4j and two different network analysis tools named Gephi and CytoScape [ Table 4 ]. 
Limitations 
Regarding the limitation section, the following points are included: 
• Data Limitations: Data has been collected exclusively from the Hadith book named Sahih 
Muslim only. 
• Domain or Context Limitations: The dataset primarily focuses on Hadith authentication 
and analysis, limiting its applicability to broader religious or cultural contexts outside of 
Islamic scholarship. 
• Incomplete Information of Narrator: The dataset may lack comprehensive details about 
narrators, including their stay locations, traveling locations and generation/level of narra- 
tors 

--- Page 10 ---\n\n10 
A.M. Farooqi, R.A.S. Malick and M.S. Shaikh et al. / Data in Brief 54 (2024) 110439 
Ethics Statement 
This data is available in the public domain, and no funding is received for the present effort. 
There is no conﬂict of interest. 
The authors state that this work involved: 
- No human subjects. 
- No animal experiments. 
- No data collection from social media platforms. 
Copyright: Data is from public domain; it is dated to decades and centuries. The data does 
not belong to users on the web resource (i.e., social media). The data is published on free and 
public Islamic websites and is available to anyone with internet access. 
Privacy: While the data is free and public, we anonymize the website and Hadith pages. 
Scrapping policies: The web resource does not have any special scrapping policy . 
CRediT Author Statement 
Aziz Mehmood Farooqi : Conceptualization, Methodology, Data curation, Formal analysis, 
Software, Validation, Investigation, Writing- Reviewing and Editing Rauf Ahmed Shams Malick : 
Supervision, Conceptualization, Writing-Original Draft, Writing- Reviewing and Editing Muham- 
mad Shahzad Shaikh : co-supervision, Domain Expect, Validation, Writing- Reviewing and Edit- 
ing Adnan Akhunzada : Writing- Reviewing and Editing. 
Data Availability 
Multi-IsnadSet MIDS for Sahih Muslim Hadith with chain of Narrators, based on multiple 
ISNAD (Original data) (Mendeley Data). 
Acknowledgments 
The open access funding is provided by Qatar National Library (QNL). 
Declaration of Competing Interest 
The authors declare that they have no known competing ﬁnancial interests or personal rela- 
tionships that could have appeared to inﬂuence the work reported in this paper. 
References 
[1] IHSAN Network. The Sunna project is aﬃliated with the prince Alaleed bin Talal Centre of Islamic studies, university 
of Cambridge. https://www.ihsanetwork.org/hadith.aspx . 
[2] Arees Institute. Muslim scholar database. http://muslimscholars.info/ . 
[3] A .M. Azmi , A .M. AlOfaidly , A novel method to automatically pass hukm on hadith, in: Proceedings of the 5th Inter- 
national Conference on Arabic Language Processing (CITALA’14), 2014, pp. 118–124 . 
[4] M.A. Saloot, N. Idris, R. Mahmud, S. Ja’afar, D. Thorleuchter, A. Gani, Hadith data mining and classiﬁcation: a com- 
parative analysis, Artif. Intell. Rev. 46 (1) (2016) 113–128, doi: 10.1007/s10462- 016- 9458- x . 
[5] M.M.A. Najeeb, A novel hadith processing approach based on genetic algorithms, IEEE Access 8 (2020) 20233–20244, 
doi: 10.1109/ACCESS.2020.2968417 . 
[6] M.M.A. Najeeb, Xml database for hadith and narrators, Am. J. Appl. Sci. 13 (1) (2016) 55–63, doi: 10.3844/AJASSP. 
2016.55.63 . 
[7] M.M.A. Najeeb, A hidden markov model-based tagging approach for arabic isnads of hadiths, Math. Probl. Eng. 2022 
(2022), doi: 10.1155/2022/7160509 . 

--- Page 11 ---\n\nA.M. Farooqi, R.A.S. Malick and M.S. Shaikh et al. / Data in Brief 54 (2024) 110439
11 
[8] A. Mahmood, H.U. Khan, F.K. Alarfaj, M. Ramzan, M. Ilyas, A multilingual datasets repository of the hadith content, 
Int. J. Adv. Comput. Sci. Appl. 9 (2) (2018) 165–172, doi: 10.14569/IJACSA.2018.090224 . 
[9] M.M. Najeeb, Towards innovative system for hadith isnad processing, Int. J. Comput. Trends Technol. 18 (6) (2014) 
257–259, doi: 10.14 4 45/22312803/IJCTT-V18P154 . 
[10] S. Saeed, S. Yousuf, F. Khan, Q. Rajput, Social network analysis of hadith narrators, J. King Saud Univ.-Comput. Inf. 
Sci. 33 (2021) 1–9, doi: 10.1016/j.jksuci.2021.01.019 . 
[11] T. Alam, J. Schneider, Social network analysis of hadith narrators from sahih bukhari, IEEE, 2020, pp. 1–5. doi: 
10.1109/BESC51023.2020.9348299 . 
[12] A. Azmi , N.B. Badia , iTree-Automating the construction of the narration tree of Hadiths (Prophetic Traditions), in: 
IEEE Proceedings of the 6th International Conference on Natural Language Processing and Knowledge Engineering 
(NLPKE-2010), 2010, pp. 1–7 . 
[13] A.M. Azmi , N.B. Badia , e-Narrator-An application for creating an ontology of Hadiths narration tree semantically and 
graphically, Arab. J. Sci. Eng. 35 (2 C) (2010) 51–68 . 
[14] M.M. Al-Azami, A note on work in progress on computerization of H. ad ¯ith, J. Islamic Stud. 2 (1) (1991) 86–91, 
doi: 10.1093/JIS/2.1.86 . 
[15] F. Haque , A.H. Orthy , S. Siddique , Hadith authenticity prediction using sentiment analysis and machine learning, 
in: 2020 IEEE 14th International Conference on Application of Information and Communication Technologies (AICT), 
IEEE, 2020, pp. 1–6 . 
[16] F. Binbeshr , A. Kamsin , M. Mohammed , A systematic review on hadith authentication and classiﬁcation methods, 
Trans. Asian Low-Resourc. Lang. Inf. Process. 20 (2) (2021) 1–17 . 
[17] H.M. Abdelaal , H.A. Youness , Hadith classiﬁcation using machine learning techniques according to its reliability, 
Rom. J. Inf. Sci. Technol. 22 (3–4) (2019) 259–271 . 
[18] E. Mohamed , R. Sarwar , Linguistic features evaluation for hadith authenticity through automatic machine learning, 
Digit. Scholarsh. Human. 37 (3) (2022) 830–843 . 
\n```\n