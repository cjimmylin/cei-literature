---
title: "2025-Fillies-A novel German TikTok hate speech dataset far-right comments against - PDF Extract"
source_pdf: "2025-Fillies-A novel German TikTok hate speech dataset far-right comments against.pdf"
pages: 21
extracted_at: "2026-02-13T14:50:58.458831"
---

# PDF Extract: 2025-Fillies-A novel German TikTok hate speech dataset far-right comments against

**Source PDF:** 2025-Fillies-A novel German TikTok hate speech dataset far-right comments against.pdf
**Total Pages:** 21

---

## Content

```
--- Page 1 ---

Vol.:(0123456789)
 Discover Data             (2025) 3:4  
| https://doi.org/10.1007/s44248-025-00020-y
Discover Data
Research
A novel German TikTok hate speech dataset: far‑right comments 
against politicians, women, and others
Jan Fillies1,2 · Esther Theisen4 · Michael Hoffmann2 · Robert Jung4 · Elena Jung4 · Nele Fischer4 · Adrian Paschke1,2,3
Received: 11 September 2024 / Accepted: 5 February 2025
© The Author(s) 2025 
 
OPEN
Abstract
With the rise of new social media platforms designed for teenagers and adolescents, the importance of content modera-
tion supported by algorithms is more necessary than ever. State-of-the-art hate speech detection algorithms are increas-
ingly challenged by the rapid and creative evolution of modern language. To better understand the online discourse and 
phenomena of German far-right extremism on contemporary platforms, this research presents the first German TikTok 
dataset, consisting of 10,586 comments collected from comment sections and annotated for far-right extremism and hate 
speech. An extensive and novel annotation scheme comprising of 32 labels was developed in collaboration with domain 
experts in online extremism, specifically tailored to the TikTok platform. Three trained annotators meticulously annotated 
the dataset, with 13.76% of the collected data annotated to be hateful. A quantitative analysis was conducted, examin-
ing the primary keywords emerging within hate speech classes, identifying label combinations and distributions, and a 
sentiment analysis was performed. The dataset reveals extensive hate directed toward German politicians, particularly 
members of the Green Party, as well as women and immigrants. This research contributes to the field by introducing a 
new annotation schema, providing a fully annotated dataset, and analyzing the annotations and language used.
Keywords  Hate speech · Dataset · German · Politics · TikTok
1  Introduction
Social media’s unprecedented reach—encompassing 4.8 billion users and nearly 60% of humanity as of April 2023 [1] — 
has made online platforms crucial battlegrounds for combating hate speech. The magnitude of this challenge is evident 
in Facebook’s content moderation efforts alone, which resulted in the removal of 38.3 million hate speech statements in 
just the first three quarters of 2023 [2]. These figures underscore an urgent need for effective detection and prevention 
strategies, particularly in multilingual contexts.
While substantial research on automatic hate speech detection has focused on X (ex-Twitter) and Facebook, TikTok has 
received comparatively less attention. In the context of German hate speech detection, the lack of research is particularly 
severe, as till date there are no data sets on German TikTok datasets, hindering the development of effective detection 
tools. This limitation is particularly concerning in light of recent European Union legislation, including the Digital Services 
Act and AI Act, which emphasizes the need for unbiased data collection and enhanced online protections for minors. 
 *  Jan Fillies, jan.fillies@fu-berlin.de | 1Institut für Angewandte Informatik, Leipzig, Germany. 2Freie Universität Berlin, Berlin, 
Germany. 3Fraunhofer FOKUS, Berlin, Germany. 4Modus-Zad, Berlin, Germany.

--- Page 2 ---

Vol:.(1234567890)
Research	
 
Discover Data             (2025) 3:4  
| https://doi.org/10.1007/s44248-025-00020-y
Given TikTok’s demographic composition—with 47.4% of users under 30 and 25% between ages 10 and 19 [3] —the 
platform represents a critical focus for investigating German-language hate speech.
To address this research gap, the authors present and analyze the first German hate speech dataset from TikTok. It 
consists of 10,586 posts collected from comment sections under TikTok Videos on individual accounts associated with 
the German far-right scene. To select the accounts, the authors worked together in collaboration with experts in deradi-
calization and extremism prevention. Moreover, the authors developed together with these experts a novel, fine-grained 
multidimensional annotation schema encompassing 32 different aspects of hate, including various targets, types, and 
intensity levels. This detailed approach enables the capture of subtle but significant variations in hate speech expression, 
promoting more consistent and nuanced annotations.
Thus the main contributions of this research are: 
1.	 a novel fine-grained annotation schema for hate speech, containing 32 classes.
2.	 the first German annotated dataset for hate speech on TikTok, and
3.	 a comprehensive quantitative analysis and qualitative exploration of the dataset.
The research is organized as follows: Sect. 2 provides the background, including the definition of hate speech and far-
right ideologies, as well as an overview of related works in the field. Section 3 focuses on the dataset, describing its 
collection process, privacy protection measures, principles for data collection, and the accompanying data statement. 
Section 4 details the core aspects of the methodology, including the taxonomy employed and the annotation procedure. 
Section 5 presents an analysis of the dataset and annotations, covering topics such as label distribution, inter-annotator 
agreement, sentiment scores, and keyword analysis. Section 6 highlights the qualitative findings. Section 7 discusses 
the results, and the research concludes with a future outlook in Sect. 8.
2  Background
2.1  Definition of far‑right
Far-right politics encompasses diverse political movements and parties that scholars have variously termed ‘radical 
right’ [4], ‘extreme right’ [5], and ‘populist radical right’ [6, 7]. While definitions and categorizations remain debated in 
contemporary scholarship [8], the authors of this study use the notion of ‘far right’ as an umbrella term encompassing 
both radical and extreme right actors. This terminology acknowledges that far-right ideology manifests not only through 
traditional political parties but also through movements like Patriotische Europäer gegen die Islamisierung des Abend-
landes (PEGIDA) and the Identitarian Movement in Germany [9].
Far-right actors position themselves as defenders of a native population, advocating either substantial political reform 
to ’protect democracy’ (in the case of radical right) or complete replacement of democratic systems with authoritarian 
leadership (in the case of extreme right) Ignazi [10]. As Castelli Gattinara et al. [9] note, these groups are ideologically 
united by nativism, a radical and exclusionary form of nationalism that “rejects ‘alien’ persons and ideas from their con-
ception of the nation state”.
2.2  Definition of hate speech
The challenge of defining hate speech has been extensively studied by various scholars [11–14], with no universal consen-
sus emerging despite numerous attempts by academics, social media platforms, and regulatory bodies. The understand-
ing of hate speech varies significantly even within the same research community, and becomes even more multifaceted 
across different disciplines [15]. Among the various definitions proposed, [13] stands out for its comprehensive approach, 
describing hate speech as "language that attacks or diminishes, that incites violence or hate against groups, based on 
specific characteristics such as physical appearance, religion, descent, national or ethnic origin, sexual orientation, gen-
der identity or other, and it can occur with different linguistic styles, even in subtle forms or when humour is used" [13].
The complexity in reaching a unified definition stems from several interrelated factors. First, there is the difficulty in 
distinguishing hate speech from related concepts like cyberbullying Slonje et al. [16] and toxic speech Fortuna et al. [13]. 
Second, hate speech has a dynamic nature, demonstrated by how seemingly neutral terms can be co-opted for hateful 

--- Page 3 ---

Vol.:(0123456789)
Discover Data             (2025) 3:4  
| https://doi.org/10.1007/s44248-025-00020-y 
	
Research
purposes. A prime example of this can be seen in how right-wing circles modified the meaning of the German word 
‘goldstück’ (piece of gold) during the 2015 refugee crisis, transforming it into a sarcastic derogatory term for immigrants 
[17]. Third, hate speech serves as a discursive strategy to establish and maintain social hierarchies and power dynamics 
[18], making the socioeconomic context particularly significant. For instance, hate speech from economically privileged 
groups may have different implications than offensive comments from marginalized populations that might be classified 
not as hate speech but as ‘weapons of the weak’ [19].
While the debate continues in this interdisciplinary field spanning social and computer sciences, there are several 
common elements that emerge across definitions. Hate speech encompasses both linguistic and image-based actions, 
as well as non-factual statements, that aim to degrade, hurt, intimidate, or threaten individuals or groups based on their 
association with particular social groups or political commitments. It often relies on stereotyping (racist, Islamophobic, 
xenophobic) and can be either deliberate or unintentional [20]. In digital spaces particularly, it manifests as a form of 
violence or violent language that represents a specific form of incivility [21] or norm-breaking communication. Based 
on these insights and expanding on them, the authors of this study then developed a very precise taxonomy of what 
constitutes hate speech, a process described in detail in the Sect. 4.1.2 of this study.
2.3  Hate speech datasets
In the field of annotated hate speech, datasets are increasing in number in recent years. While a vast majority are still 
with in English (e.g. [22–25]). More complex datasets are being collected with a wider range of languages covered [26]. 
In the monolingual section, there are some key contribution datasets that are established resources within the research 
community. In 2017 Davidson et al. [27] collected 24,802 English tweets labeled as hate speech, offensive language, or 
neither. It is one of the earliest and most widely used hate speech datasets. In 2018 Founta et al. [28] collected 80,000 
English tweets annotated for abusive behavior, including hate speech, offensive language, and cyberbullying. A very 
popular benchmark for the community is the HateExplain dataset by Mathew et al. [29] containing 20,148 English posts 
from Twitter and Gab, annotated for hate speech, offensive content, and target communities. It also provides word-level 
annotations resulting in explanations for the classifications. More recently, among others, Fillies et al. [30] is notable as 
they collected over 88,000 English discord messaged and annotated eight different classes of hate speech.
For the scope of this study, annotated datasets in German are particularly highlighted. An early and still significant 
German hate speech dataset is the one by Bretschneider and Peters [31], which contains 469 German posts from Twitter 
annotated with binary hate labels. Further extending this work, the GermEval 2018 dataset by Wiegand et al. [32] contains 
2,871 German tweets classified as offensive language. In 2019, Mandl et al. [26] published an annotated multilingual 
dataset containing 4,669 German tweets and Facebook comments annotated for hate speech, offensive, and profane 
speech. The work so far primarily focused on tweets based on keywords, achieving a high proportion of up to 40% hateful 
tweets in their datasets. Assenmacher et al. [33] published the first large-scale dataset based on comments from news 
outlet websites. The dataset contains 85,000 annotated comments, with 8.4% of them being abusive. They labeled a 
variety of seven categories: sexism, racism, threats, insults, profane language, meta, and advertisement. Similar in depth 
of annotation schema was the work by Demus et al. [34], who annotated sentiment, hate speech, type of discrimination, 
criminal relevance, expression, toxicity, extremism, target, and threat. Their dataset consists of 10,278 German Twitter 
comment threads, with a rate of 10.85% hateful content. More recently, Goldzycher et al. [35] published a dataset consist-
ing of 10,996 texts made up of synthetic data and news sentences, with binary annotation and 42.4% hateful content.
In contrast to the vast repositories of annotated datasets of single-tongue corpora, the number of multilingual datasets 
with appropriate annotations remains rather meager [36].
As seen above, hate speech datasets feature various annotation schemes [36], ranging from binary to multi-class 
hierarchies [37]. Additionally, more universal annotation schemes are available [38], commonly applied in tasks such as 
hate speech annotation and in related areas like cyberbullying [39], demonstrating their versatility in addressing diverse 
challenges.
Despite the availability of numerous publicly accessible German hate speech datasets, it is observable how they are 
mainly focused on Twitter, with small research outlines for News outlets and Facebook comments. Other platforms are 
understudied. This research adds to the research field by providing research institutions with the first German TikTok hate 
speech dataset. It is essential to collect and analyze datasets from different platforms and a recent timeframe to account 
for shifts in topics and language and though reduce the bias within the available training data.

--- Page 4 ---

Vol:.(1234567890)
Research	
 
Discover Data             (2025) 3:4  
| https://doi.org/10.1007/s44248-025-00020-y
3  Dataset
3.1  Sources and collection
A multistep process led to the identification and selection of the annotated comments, as illustrated in Fig. 1. The first 
two steps, account identification and data collection, were done as part of the European Research Project RECO_DAR.1 
The RECO_DAR research project identified 323 accounts relevant to the German-speaking far-right ecosystem, using a 
combination of expert interviews, key figures, keywords, and hashtags specific to the far-right scene. RECO_DAR utilized 
snowball sampling, which involved examining follower lists, comments, and engagement networks of known far-right 
users, to identify further accounts. Out of the 323 accounts initially identified, only 142 were ultimately included in the 
analysis due to bans, deactivations, or privacy restrictions on some accounts. The dataset was collected from 1st of 
November 2023 to 30th of November 2023, amounting to approximately 815,000 comments in total.
Due to performance, time, and resource constraints, this research selected a random subset of comments grouped 
by the videos they were posted under, totaling approximately 150,000 comments. An ensemble of six established hate 
speech classifiers (five open models and one commercial model from Google Jigsaw2) was used to annotate the selected 
statements for binary hate speech classification. The English-based models received translated inputs, the authors chose 
to translate content into English and use English-based classifiers based on Fillies et al. [40] findings, which demonstrated 
that using DistillBERT and translate-to-English approach achieved comparable performance to both native monolingual 
classifiers and multilingual classifiers, the general approach for BERT based models is further supported by Saheth et al. 
[41]. The scripts and algorithms for this task are available on GitHub.3
Hate speech predictions were averaged across all comments under each video. Videos with the highest average hate 
level, including all comments, not just hateful ones, were selected for human annotation. Videos were selected until the 
total number of comments reached 10,000; however, for the last video, no comments were omitted, resulting in a total 
of 10,586 comments. This selection approach was intended to overcome the challenge of focusing only on comments 
containing classic or easily detectable forms of hate, thereby influencing the percentage of hate in the dataset but pro-
viding a broader view of the language used in comment sections under polarizing political TikTok videos. Only the final 
selected and anonymized comments, annotated for hate speech, are being published with this research.
3.2  Principles for data collection
Vidgen and Derczynski [42] outline key considerations when creating an abusive content dataset. Firstly, they mention 
the “Purpose” of the dataset, which in this case is to establish a base for validating and improving hate speech detection 
within online communication. TikTok, with its young audience and rapid development, is suspected to have a unique form 
of communication that this dataset aims to capture. Secondly, the recommendation to “Explore new sources” is addressed 
as no German hate speech TikTok dataset has been discovered so far. The next requirement, a “Clear taxonomy” was 
developed with experts in extremism research,4 detailed in Sect. 4.1.2. The raised need to “Develop guidelines iteratively 
with your annotators” was followed and is described in the Annotations Procedure, 4.1.1. Lastly, a “Data Statement” was 
created using the methodology outlined by [43], ensuring comprehensive documentation of the dataset’s characteristics 
and collection process, see Sect. 3.4.
Fig. 1   Overview of the collection process
1  https://​www.​scenor.​at/​recod​ar
2  https://​jigsaw.​google.​com/
3  https://​github.​com/​filli​es/​diffr​entHa​teAlg​os
4  https://​modus-​zad.​de/

--- Page 5 ---

Vol.:(0123456789)
Discover Data             (2025) 3:4  
| https://doi.org/10.1007/s44248-025-00020-y 
	
Research
3.3  Privacy protection
The dataset does not contain any personal data as defined in Art. 4 No. 1 of the GDPR. This was achieved using a two-step 
approach. Firstly, specifically developed algorithms were employed to pseudonymize usernames and identify personal 
information using standard pattern matching approaches and advanced machine learning techniques such as Named 
Entity Recognition. Problematic statements were excluded (e.g. a problematic statement is of the nature: “I live on the Karl 
Marx Allee 27, 10245 in Berlin, Germany”). Only statements that did not contain personal information were selected for 
further evaluation. In the second step, during the annotation phase, annotators were tasked with identifying problematic 
statements that were not correctly detected in the first phase. Any statements identified during this human evaluation 
phase were also excluded from the dataset, ensuring no personal data was included.
3.4  Data statement
The statement is presented in the form of Table 1. It was created following Gebru et al. [43]. The classes “RECORDING 
QUALITY”, “OTHER”, and “PROVENANCE APPENDIX” were not available or applicable for the dataset.
4  Methodology
4.1  Annotation
Three annotators annotated the dataset independently. The team of annotators consisted of researcher in the field of 
online extremism, computer science and social anthropology. The average age of the members was 33.33 years. The 
ages varied from 26 to 45 years. The team consisted of one female and two male annotators. The ethnic background and 
mother tongue was German.
4.1.1  Annotation procedure
As suggested by Vidgen and Derczynski [42], an annotation guideline was jointly developed with the three annotators 
and continuously improved during the annotation process. This iterative process included the introduction of new labels 
and discussions about specific examples and edge cases. Beyond the shared development of the guideline and the initial 
establishment of a common understanding, regular meetings were held to discuss challenges, conduct mental check-ins, 
and facilitate knowledge exchange.
Table 1   Data statement for the dataset
This research bases its definition on Bahlo et al. [44] and views youth language as a variation of language that can be found within the pre-
sent language of adolescents, while acknowledging that there are group characteristic variations in any setting
Characteristic
Description
CURATION RATIONALE
The data set consists of the comments under far-right political TikTok videos. The accounts were selected by 
experts in online extremism and the specific videos chosen by the highest amount of hate determined by 
an ensemble of classifiers.
LANGUAGE VARIETY
The messages are online, written in German, and provided by a multinational setting, predominantly Ger-
many and Austria. It is partly youth language1.
SPEAKER DEMOGRAPHIC
There are 9723 unique author IDs. With 47.4% of TikTok users being under 30 [3] and 25% being 10–19 years 
old [3] there is a strong focus on adolescents.
ANNOTATOR DEMOGRAPHIC
Three annotators were used. They are full-time students with an age range between 26 and 45, average age 
33.33. The group consisted of two males, one female. They are native German speakers. One is holding a 
PhD in social Anthropology.
SPEECH SITUATION
The data set was collected between 01.09. 2023 to 30.11. 2023. It consists of written, unscripted TikTok com-
ments. The intended audience were other participants of the application.
TEXT CHARACTERISTICS
They are comments under videos of German and Austrian far-right politician. TikTok does provide content 
moderation.

--- Page 6 ---

Vol:.(1234567890)
Research	
 
Discover Data             (2025) 3:4  
| https://doi.org/10.1007/s44248-025-00020-y
Each annotator was tasked with annotating each statement independently, and each statement could have multiple 
labels. If a statement was considered hateful, the annotator was also tasked to give an intensity level. Once confident 
in their choices, they were required to validate their annotations. The task was to consider each statement as an inde-
pendent instance, with the knowledge that it was posted under a German far-right video on TikTok. Annotators could 
flag comments for further discussion or exclusion from the final dataset if needed. Only statements that were annotated 
by all three annotators were included in the final dataset. Annotators were also responsible for conducting additional 
research if they encountered unknown concepts or references to public figures. In such cases, they could leave separate 
comments for their peers, providing further information or requesting assistance to decode certain aspects of the com-
ment. Lastly, the annotators were asked to flag any potential comments that share personal information. For efficient 
and reliable annotation, the open-source tool Doccano5 was used. Doccano allows for multi-label annotations with a 
standardized annotation schema, input validation, and comment functions, making it well-suited for the collaborative 
and iterative nature of this annotation process.
4.1.2  Annotation scheme
The annotation schema is structured into a taxonomy. Developed in collaboration with online extremism experts,6 this 
taxonomy covers an extensive spectrum of hate-related definitions, while acknowledging the inherent limitations of 
capturing all possible manifestations. It is possible and necessary to introduce more specific labels and categories that 
cover other aspect in future work. While insults, disinformation, and conspiracy theories do not necessarily always meet 
the technical definition of hate speech, this study included these categories because they frequently lead to or are closely 
associated with hateful and toxic content.
While undoubtedly categorizing hate speech intensity is inherently subjective and influenced by personal experi-
ences and preconceptions about what constitutes extreme, moderate, or mild hate speech, this study included such a 
classification to get a better understanding on the intensity of hate. The annotators were provided with the following 
examples to guide the annotation process: 
1.	 Low: “Du Arsch bist der letzte Dreck” (You ass, are the last dirt)
2.	 Medium: “Lieber ein Arschlo..... als Grüner kriminellen Dreck” (Rather an a...than a green criminel dirt)
3.	 High: “Diese schlampe baerbock holt sie alle rein toetet sie" (The slut baerbock get her and kill her)
The labels indicate the urgency of interaction needed with these comments, ranging from minimal to immediate.
The taxonomy consists of three top-level categories: hate speech, non-hate speech, and unreadable content. The hate 
speech category is further subdivided into three aspects: the origin of hate, the target of hate, and types of hate. Below, 
the authors introduce each category with examples. Figure 2 shows the complete structure of the hate speech schema 
proposed by the experts, though not all depicted classes appeared in the dataset. Note also that annotators could assign 
multiple classifications to each statement.
Annotation Scheme Class: Types of Hate The class is further divided into eight general concepts regarding what 
kind of hate could be identified in the statement. Table 2 displays an overview of the classes, their definitions and gives 
a possible example.
Class: Origin of Hate The class refers to the underlying concepts of the hateful concepts. It is broken down further 
into two classes: ideology and narrative. Ideology refers to a system of beliefs, values, and ideas that can shape and justify 
hatred toward certain groups or individuals. The narrative class contains stories or discourses that shape and perpetuate 
hatred toward certain groups or individuals.
The class ideology holds the concepts of Third Reich nostalgia and white supremacy. In the class of narratives the 
concepts of anti-LGBTQIA+, anti-wokeness, delegitimization of liberal democracy, misogyny anti-feminism, the roman-
ticization of the homeland, conspiracy theory, and disinformation can be found. Table 3 displays an overview of the 
classes, their definitions and gives a possible example.
Class: Target of Hate The class refers to the targets of the hateful statements. They are broken down further into eight 
classes: gender, immigration status, national origin, physical attributes, race/ethnicity, religious beliefs, sexual orientation, 
occupation. The class of gender is broken down further to women, men, and transgender. The class of religious beliefs is 
5  https://​github.​com/​docca​no/​docca​no
6  https://​modus-​zad.​de/

--- Page 7 ---

Vol.:(0123456789)
Discover Data             (2025) 3:4  
| https://doi.org/10.1007/s44248-025-00020-y 
	
Research
broken down further to Jews and Muslims, occupational group is broken down further to journalists and politicians. All 
classes could be defined further, but to limit the scope, the research included only the most prevalent target of hate found 
by the radicalization experts. Table 4 displays an overview of the classes, their definitions and gives a possible example.
Fig. 2   Overview of taxonomy 
for the hate class

--- Page 8 ---

Vol:.(1234567890)
Research	
 
Discover Data             (2025) 3:4  
| https://doi.org/10.1007/s44248-025-00020-y
Table 2   Class: Types of Hate
Label
Definition
Example
Dehumanization
Depicts individuals or groups as less than human, often comparing them to 
animals, objects, or as subhuman.
“bloß net diese Affen wählen” (don’t vote for this monkey)
Devaluation
Diminishes the worth, value, or dignity of individuals or groups, suggesting 
they are inferior or less deserving of respect, rights, or opportunities.
“Ihr Profilbild sagt schon alles” (Her profile picture says everything)
Stereotyping
Oversimplifies and generalizes beliefs about a group, leading to prejudiced 
attitudes and discrimination.
“Er sollte lieber eine Dönerbude aufmachen” (He should rather open a Kebab 
shop)
Criminalization
Unjustly labels individuals or groups as inherently criminal or dangerous.
“Lieber ein Arschlo..... als Grüner kriminellen Dreck” (Rather an a... than green 
criminal dirt)
Support for Hateful Entities
Expresses support for groups or individuals known for promoting hate, 
discrimination, or violence.
“SS beste, endlich mal was getan!” (SS is the best; they finally did something)
Threatening Language
Threatens harm, violence, or intimidation toward individuals or groups, 
creating fear of imminent harm.
“Geh lieber nicht mehr allein raus” (Rather do not go out alone anymore)
Violence and Killing
Advocates for, glorifies, or incites physical violence, assault, or murder.
“Diese schlampe baerbock holt sie alle rein toetet sie” (The slut baerbock, get 
her and kill her)
Insult
Offensive remark or action intended to demean or disrespect someone.
“Du Arsch bist der letzte Dreck” (You ass, are the last dirt)

--- Page 9 ---

Vol.:(0123456789)
Discover Data             (2025) 3:4  
| https://doi.org/10.1007/s44248-025-00020-y 
	
Research
Table 3   Annotation Scheme Class: Origin of Hate
Label
Definition
Example
Third Reich Nostalgia
Invokes historical references to the Nazis, using propaganda methods 
from that era. This includes narratives that both deny and affirm atroci-
ties committed during the Third Reich.
“88” (Code for: Heil Hitler)
White Supremacy
Refers to the belief that white people are superior to all other races.
“England musste einfach all diese Barbaren zivilisiert.” (England just had 
to civilize all these barbarians)
Anti-LGBTQIA+
Hostile or discriminatory attitudes, actions, or policies against LGBTQIA+ 
individuals. Includes opposition to LGBTQIA+ rights, negative stereo-
typing, and exclusionary practices.
“Frankenstein” (When referring to transgender people)
Anti-Wokeness
Uses narratives suggesting that progressive voices are part of a “woke" 
or leftist conspiracy, often targeting political opponents, specifically 
the Green Party, accusing them of overly broad prohibitions and open 
borders.
“linksgrünversifft” (leftgreenfilth)
Delegitimization of Liberal Democracy Uses extremist narratives to sow skepticism and mistrust toward the 
state, media, and democratic institutions, often scapegoating groups 
like foreigners, Asians, or Jews.
“Lügenpresse” (Lying press)
Misogyny / Anti-feminism
Expresses contempt or prejudice against women, opposing women’s 
rights and equality.
“Ab in die Küche” (Go to the kitchen)
Romanticization of the Homeland
Idealizes and nostalgically glorifies one’s country, emphasizing positive 
aspects, cultural heritage, and perceived superiority, while downplay-
ing negative aspects and complexities.
“In der DDR war alles gut” (Everything was good in the DDR)
Antisemitism
Displays prejudice, hatred, or discrimination against Jewish people 
based on their ethnicity, religion, or cultural heritage, including stereo-
types, derogatory remarks, or violence.
“Geltgeile Juden” (Greedy Jews)
Anti-immigrant
Expresses negative attitudes or discriminatory actions toward immi-
grants, often based on fears of cultural change, economic concerns, or 
perceptions of immigrants as a threat to social stability.
“Goldstück” (Term implying immigrants come only for money)
Conspiracy Theory
Belief that events result from secret plots by groups or organizations, 
often lacking credible evidence and contradicting mainstream expla-
nations, relying on speculation and mistrust of authorities.
“Die Mondlandung ist nicht passiert” (The moon landing didn’t happen)
Disinformation
Spread of false or misleading information to deceive, manipulate public 
opinion, or obscure the truth, often creating confusion and mistrust.
“Impfen verursacht Autismus” (Vaccination causes autism)

--- Page 10 ---

Vol:.(1234567890)
Research	
 
Discover Data             (2025) 3:4  
| https://doi.org/10.1007/s44248-025-00020-y
Table 4   Annotation Scheme Class: Target of Hate
Label
Definition
Example
Men
Targets men with discrimination, prejudice, or hostility based on gender, mani-
festing in stereotypes, unfair treatment, or systemic biases.
“Du Beta looser” (You beta looser)
Women
Targets women with discrimination, prejudice, or hostility based on gender, 
manifesting in stereotypes, unfair treatment, or systemic biases.
“Früher hat man Hexen Verbrannt oder Ertränkt” (In the old days, witches were 
burnt or drowned)
Transgender People
Targets transgender individuals with discrimination, prejudice, or hostility, mani-
festing in stereotypes, unfair treatment, or systemic biases.
“Relativ einfach zu lösen, tritt ins gemächt und er weiß zu welchem Bereich er 
gehört” (Pretty simple to solve, a kick in the groin and you know where he 
belongs)
Immigration Status
Targets individuals based on immigration status, with negative attitudes, preju-
dices, or discriminatory actions, often focused on cultural, economic, or social 
concerns.
“Alle diese Imigranten stehlen unsere Jobs” (All these immigrants are stealing our 
jobs)
National Origin
Uses prejudice, discrimination, or hostility based on an individual’s country of 
origin.
“Dann soll die alte dahin zurückkriechen wo sie her gekommen ist, wenn es ihr 
hier nicht gefällt” (She should crawl back to where she came from if she doesn’t 
like it here)
Physical Attributes
Targets individuals based on bodily characteristics like skin color, body size, or 
visible traits, using prejudice, discrimination, or hostility.
“Du Krüppel” (You cripple), “Jepp, aus Kuhmist und Lehm. Sind ja alle hochqualifi-
ziert” (Yeah, out of cow dung and clay. All highly qualified.)
Race/Ethnicity
Uses prejudice, discrimination, or hostility based on perceived racial or ethnic 
background.
“Vielleicht können die im Bus auch einfach wieder hinten sitzen” (Maybe they can 
just sit in the back of the bus again)
Muslims
Targets individuals who practice Islam or identify as Muslim, using prejudice, 
discrimination, or hostility.
“Muslime und Deutschand sind unvereinbar” (Muslims and Germany can not be 
combined)
Jews
Targets individuals who practice Judaism or identify as Jewish, using prejudice, 
discrimination, or hostility.
“Die geldgieriegen Juden” (The greedy Jews)
Sexual Orientation
Targets individuals based on sexual orientation, using prejudice, discrimination, 
or hostility against those who identify as non-heterosexual.
“Schwuchtel” (faggot)
Politicians
Uses prejudice, discrimination, or hostility toward individuals in political roles, 
often targeting them based on their party affiliation or policies.
“Grüner Mist! Verbotspartei!” (Green dung! Party of prohibition)
Journalists
Uses prejudice, discrimination, or hostility toward individuals in journalism due 
to their role in gathering, reporting, and disseminating news.
“Und wieder diese fascho Lügen presse” (Again this fascist lying press)

--- Page 11 ---

Vol.:(0123456789)
Discover Data             (2025) 3:4  
| https://doi.org/10.1007/s44248-025-00020-y 
	
Research
5  Data analysis
The dataset consists of 10,586 annotated comments from 9723 unique users under 146 different TikTok videos. When 
considering a binary flag where at least two annotators choose other flags than “no hate” 26.04% of the comments in the 
dataset are considered problematic. If it is broken further down and to a class level where at least two annotators selected 
the same label of hate 13.76% of the comments included some form of toxicity. The dataset has 11 columns, which are 
outlined in Table 5. This includes the individual annotations from the three annotators and the combined annotation. 
Combined annotations are labels assigned by at least two of the three annotators. In addition to the classical labels, 
each annotator was also asked to annotate the level of intensity if hate speech was present. The highest selected level 
for each comment was identified in the column highest_intensity_level.
The research’s analysis of the newly created dataset examined annotated labels, calculated inter-annotator agree-
ment, identified frequently occurring keywords and emoticons, and applied BERT-based sentiment analysis to uncover 
emotional patterns, with the results presented alongside brief contextual explanations and a more detailed discussion 
provided in Sect. 7.
5.1  Annotation analysis label distribution
Tables 6, 7, 8 display the distribution of the labels for each of the three main classes of the taxonomy. For each label, it is 
noted how often it was annotated by at least two annotators without any other label assigned. The table also indicates 
how frequently each label was annotated by at least two annotators in combination with other labels, and it lists the 
top three labels with which each label was most often co-annotated. Finally, the table shows the total number of times 
each label was annotated. The distribution of the labels ‘Level of Intensity’ can be seen in table 9.
The trend of very unbalanced hate speech datasets observed in related literature is also evident in this research. The 
‘no hate’ class constitutes the majority of the dataset, and even within the annotated hate speech classes, 9 out of the 32 
Table 5   Columns of the 
dataset
Column name
Definition
id
Unique identifier for each entry (integer)
text
Text of the comment (string)
user
User identifier (string)
video_id
Identifier for the video associated with the comment (string)
label_annotator_1
Labels assigned by an annotator 3 (string, list of labels)
label_annotator_2
Labels assigned by annotator 2 (string, list of labels)
label_annotator_3
Labels assigned by annotator 3 (string, list of labels)
common_labels
Common labels among two of three annotators (string, list of labels)
binary_hate
True if at least two annotators selected other field than non-hateful
highest_intensity_level
The highest level of hate detected in the comment (string)
comments
Additional comments (string)
Table 6   Label Occurrences and Top Co-Occurrences, with majority annotator agreement, for the Class: Types of Hate (demo. = democracy, 
home. = homeland, lan. = language, stereo. = stereotyping, deval. = devlauation, crimi = criminalisation)
Label
Alone
With others
Top combinations
Insult
179
323
politicians: 211, women: 67, deval.: 63, Threatening_lan.: 22
Threatening_lan.
98
126
politicians: 69, violence_and_killing: 22, insult: 22, women: 16
Devaluation
44
155
politicians: 85, insult: 63, women: 29, journalists: 13
Stereotyping
22
65
politicians: 23, immigration_status: 17, anti-immigrant: 17, crimi.: 14
Criminalisation
8
56
politicians: 35, stereo.: 14, threatening_language: 11, immigration_status: 9
Violence_and_killing
9
31
threatening_language: 22, politicians: 12, women: 7, third_reich_nostalgia: 3
Dehumanization
3
17
insult: 10, politicians: 8, threatening_language: 3, deval.: 3

--- Page 12 ---

Vol:.(1234567890)
Research	
 
Discover Data             (2025) 3:4  
| https://doi.org/10.1007/s44248-025-00020-y
labels have fewer than 20 examples. The most common target of hate is politicians, reflecting the dataset’s focus, followed 
by women and immigrants. The most common type of hate is ‘insult’, followed by ‘threatening_language’ and ‘devaluation’. 
The most frequently used narratives are ‘anti-wokeness’, ‘delegitimization_of_liberal_democracy’, and ‘anti-immigrant’.
As designed in the annotation framework, an optimal statement should have at least one label in each of the main 
groups: a target_of_hate, type_of_hate, and narrative. In practice, obtaining multiple annotations proved challenging, 
as evidenced by the high number of statements that received only one label. However, for statements with multiple 
annotations, clear groupings can be identified, such as [target: ‘politician’, type: ‘insult’, narrative: ‘delegitimization_of_lib-
eral_democracy’], or [target: ‘women’, type: ‘insult’, narrative: ‘misogyny_anti-feminism’]. Additionally, combinations like 
Table 7   Label Occurrences and Top Co-Occurrences, with majority annotator agreement, for the Class: Origin of Hate (demo. = democracy, 
home. = homeland, lan. = language, stereo. = stereotyping, deval. = devlauation, crimi = criminalisation)
Label
Alone
With others
Top combinations
Anti-wokeness
49
42
Insult: 12, deval.: 8, anti-LGBTQIA+: 8, stereo.: 6
Delegi_lib._demo.
27
45
Politicians: 37, deval.: 7, insult: 6, Threatening_lan.: 4
Anti-immigrant
0
62
Immigration_status: 62, stereo.: 17, crimi.: 9, deval.: 6
Conspiracy theory
19
23
Journalists: 7, politicians: 6, deval.: 3, desinformation: 2
Anti-LGBTQIA+
20
22
Trans: 10, anti-wokeness: 8, deval.: 3, politicians: 2
Desinformation
24
14
Politicians: 5, Immigration_status: 4, anti-immigrant: 4, Con-
spiracy theory: 2
Mysogyny_anti-feminism
2
30
Women: 27, insult: 13, politicians: 9, deval.: 7
Romanti_of_home.
20
9
Insult: 3, politicians: 3, national_origin: 2, immigration_status: 1
Third_reich_nosta.
7
4
Threatening_language: 4, violence_and_killing: 3, women: 1
Antisemitism
0
8
Jews: 8, Conspiracy theory: 2, stereo.: 1
White_supremacy
2
2
Race_ethnicity: 2
Table 8   Label Occurrences and Top Co-Occurrences, with majority annotator agreement, for the Class: Target of Hate (demo. = democracy, 
home. = homeland, lan. = language, stereo. = stereotyping, deval. = devlauation, crimi = criminalisation)
Label
Alone
With others
Top combinations
Politicians
97
395
Insult: 211, deval.: 85, Threatening_lan.: 69, delegi_liberal_democ.: 37
Women
32
113
Insult: 67, deval. 29, mysogyny/anti-feminism: 27, politicians: 21
Immigration_status
0
62
Anti-immigrant: 62, stereo.: 17, crimi.: 9, deval.: 6
Journalists
18
35
Deval.: 13, insult: 8, Conspiracy theory: 7, Threatening_lan.: 4
Race_Ethnicity
14
15
National_origin: 5, stereo.: 4, deval.: 4, anti-wokeness: 3
Trans
8
13
Anti-LGBTQIA+: 10, deval.: 2, anti-wokeness: 2, insult: 1
National_origin
5
14
Race_ethnicity: 5, stereo.: 5, deval.: 4, romanticisation_homeland: 2
Muslims
8
9
Stereo.: 6, women: 2, national_origin: 1, Immigration_status: 1
Men
2
10
Insult: 7, dehumanization: 2, anti-wokeness: 1, deval.: 1
Physical_attributes
2
7
Women: 6, politicians: 6, insult: 5, mysogyny_anti-feminism: 5
Jews
0
8
Antisemitism: 8, conspiracy theory: 2, stereo.: 1
Table 9   Label distribution of 
the three labels in the class 
Level of Intensity
Label
Total appearances
Percent-
age of 
hate
level_low
715
0.494
level_medium
479
0.331
level_high
253
0.175

--- Page 13 ---

Vol.:(0123456789)
Discover Data             (2025) 3:4  
| https://doi.org/10.1007/s44248-025-00020-y 
	
Research
‘journalists’ with ‘conspiracy theories’ and ‘anti-immigrant’ with ‘criminalization’ clearly indicate the nature of the hate 
speech. It is important to note the very low occurrence of antisemitism, hate based on physical attributes, and religion.
5.2  Inter‑annotator agreement
For calculating inter-annotator agreement, Fleiss’ Kappa [45] was used. Fleiss’ Kappa is an unweighted measure that 
calculates the level of agreement among any fixed number of raters. It can be applied to multiple annotators when 
there is no connection between the raters’ annotations. To apply Kappa in the present multi-label setting, each annota-
tion was converted into a binary vector representing all possible classes, with flags indicating the annotated instances. 
Equation 1 represents Fleiss’ Kappa [45], where N represents the number of annotators, n is the number of ratings per 
subject, and k is the number of labels. The index i, where i = 1,..., N, represents the subjects, and the subscript j, where j 
= 1,..., k, represents the categories. nij is the number of raters who assigned the i’th subject to the j’th category, and pj is 
the proportion of assignments that were to the j’th category.
Fleiss’ Kappa is on a scale from -1 to 1. Positive values indicate systematic agreement, a score of 0 suggests agreement by 
chance, and negative values reflect systematic disagreement [46]. Table 10 displays the pairwise and aggregated rounded 
agreement levels. An average score of 0.40 corresponds to a fair agreement, bordering on a moderate level of agreement 
Banerjee et al. [47]. This level of agreement indicates that while the annotators exhibit some level of consistency, there 
is still a significant amount of discrepancy in their annotations. Given the extensive taxonomy and the large number of 
categories involved in the annotation task, this level of agreement is considered acceptable.
5.3  Keyword analysis
The keyword analysis was conducted in two steps. First, stop words from the NLTK library7 were used to remove small 
words of minor importance (e.g., genau (exactly)). The provided list was expanded with additional words identified 
during the process. Secondly, the most frequently appearing words in all the statements, as well as for each individual 
label, were identified. The top ten keywords for all statements, irrespective of any associated class are: afd, deutschland, 
grünen, wählen, regierung, einfach, menschen, macht, land, politiker (Translation: Afd (a relatively new far-right German 
political party), Germany, Green (from the political centre-left, with a strong focus on environmental protection), voting, 
government, simply, humans, power, land, politicians) Table 11 and Table 12 display the top ten keywords for each label 
(keywords are sorted by frequency) and their translations. Table 13a displays the 10 most used emoticons.
Based on the general keywords, it can be observed that the main content of the dataset is regarding the German 
political landscape. Two political parties seem to be the primary focus of the statements: the AfD and the Grünen. Nota-
bly, the keyword “AfD” appears most frequently within the ‘no hate’ class, while variations in the spelling of the Grünen 
party occupy the top three spots in the ‘insult’ class, indicating a clear trend. The AfD is mostly discussed in a non-hateful 
context, while the Grünen party is a frequent target of hate speech. The positive context surrounding the AfD is further 
supported by the fact that the second most used emoticon (see Table 13a) is the blue heart, symbolizing love for the 
AfD (which uses blue as its party color).
Evidence supporting the assumption that the Grünen party is a primary target of hate can be found in the fact 
that, in all types_of_hate classes (‘insult,’ ‘stereotyping,’ ‘threatening_language,’ ‘violence_and_killing,’ ‘dehumanization,’ 
(1)
pj = 1
Nn
N
∑
i=1
nij
Table 10   Inter-Annotator 
Agreement Fleiss’ Kappa
Annotators
Agreement
Annotator 1 / Annotator 2
0.42
Annotator 1 / Annotator 3
0.43
Annotator 2 / Annotator 3
0.35
Average
0.40
7  https://​www.​nltk.​org/​search.​html?q=​stopw​ords

--- Page 14 ---

Vol:.(1234567890)
Research	
 
Discover Data             (2025) 3:4  
| https://doi.org/10.1007/s44248-025-00020-y
‘devaluation,’ and ‘criminalization’) the Grünen party is mentioned within the top ten keywords, sometimes even as the 
most mentioned word. Among all keywords, three individuals are personally mentioned: Olaf Scholz (a Chancellor of 
Germany) in the context of ‘politician,’ Louis Klamroth (a German TV moderator) in the context of ‘journalists,’ and Ricarda 
Lang (a representative of the Grünen party in the German parliament). The top ten keywords in the ‘physical_attributes’ 
class (e.g., women, Greens, Lang, huge, fat, problem, right, Ricarda, politics, second) reveal how Ricarda Lang is extensively 
targeted with hate based on her physical attributes.
5.4  Sentiment analysis
A sentiment analysis was conducted using a pre-trained German BERT-based classifier, which was trained for dialog 
systems by Guhr et al. [48]. The classifier provides three classes: positive, negative, and neutral. Table 13b displays the 
results of the sentiment analysis on the collected dataset. It can be observed that the dataset is strongly dominated by 
negatively annotated comments.
Table 11   First part of top ten keywords per label
Label
Keywords
Translation
Stereotyping
Politiker, grünen, deutschland, afd, linke,
Politician, Greens, Germany, AfD, Left,
Türken, wählen, einfach, täter, migrationshintergrund
Turks, vote, simply, perpetrator, migration background
no_hate
Afd, deutschland, wählen, grünen, menschen,
AfD, Germany, vote, Greens, people,
Einfach, macht, land, regierung, recht
Simply, power, country, government, right
Women
Frau, alte, gut, frauen, einfach,
Woman, old, good, women, simply,
Gehört, dame, grünen, wohl, kopf
Belongs, lady, Greens, probably, head
insult
Grünen, grüne, grün, einfach, dreck,
Greens, Green, Green, simply, dirt,
Dumm, lügen, pack, deutschland, regierung
Stupid, lies, pack, Germany, government
delegi.liberal_democ.
Regierung, demokratie, afd, politiker, partei,
Government, democracy, AfD, politician, party, Greens,
Grünen, volk, ampel, ddr, politik
People, traffic light, DDR, politics
politicians
Grünen, regierung, politiker, grüne, politik,
Greens, government, politician, Green, politics,
Grün, scholz, einfach, afd, deutschland
Green, Scholz, simply, AfD, Germany
anti-wokeness
Weiße, rassismus, gendern, einfach, kinder,
White, racism, gendering, simply, children,
Macht, mutter, wäre, sinn, woke
Power, mother, would be, sense, woke
Verschwörungsideologie
Deutschland, virus, lügen, kinder, deutschen,
Germany, virus, lies, children, Germans,
Wahlen, politik, neue, wacht, grünen
Elections, politics, new, wakes, Greens
third_reich_nostalgia
Afd, ging, österreich, früher, gesogs,
AfD, went, Austria, earlier, mob,
Geschichte, gehört, gebrauchen, geben, gaspreise
History, belongs, use, give, gas prices
Threatening_language
Grünen, regierung, müssen, endlich, land,
Greens, government, must, finally, country,
Gehört, sofort, volk, deutschland, hoffe
Belongs, immediately, people, Germany, hope
Violence_killing
Todesstrafe, krieg, holt, dreckpack, gut,
Death penalty, war, fetch, scum, good,
Gaskammer, wäre, ausgerottet, müssen, grüne
Gas chamber, would be, exterminated, must, Green
Dehumanization
Macht, unten, mensch, krank, milch,
Power, down, person, sick, milk,
Politik, grüne, schweine, kuh, zeit
Politics, Green, pigs, cow, time
Devaluation
Grünen, politiker, einfach, regierung, frau,
Greens, politician, simply, government, woman,
Politik, macht, lügen, deutschland, grün
Politics, power, lies, Germany, Green
Desinformation
Nazis, deutschland, ukraine, korrupt, leider,
Nazis, Germany, Ukraine, corrupt, unfortunately,
Grünen, medien, regierung, afd, kämpfen
Greens, media, government, AfD, fight
Race_Ethnicity
Weiße, deutsche, kinder, warum, schwarze,
White, German, children, why, black,
Deutschland, land, deutschen, bekämpfen, mädchen
Germany, country, Germans, fight, girl
Romanti_homeland
Deutschland, stolz, land, deutschen, deutscher,
Germany, proud, country, Germans, German,
Verteidigt, kultur, leben, grünen, religion
Defends, culture, life, Greens, religion

--- Page 15 ---

Vol.:(0123456789)
Discover Data             (2025) 3:4  
| https://doi.org/10.1007/s44248-025-00020-y 
	
Research
6  Qualitative observations
During the annotation process, the annotators met at regular intervals to discuss difficult statements, refine their under-
standing of definitions, and share their experiences. Several qualitative key factors were noted during these discussions.
6.1  Overall content observations
There was a widely observed and noted overwhelming hate directed toward the Green Party and anyone associated 
with the “woke” movement. Women affiliated with the Green Party were particularly targeted. This is further supported 
by the quantitative analysis presented in Table 8, which shows that the two most frequent targets of hate are politicians 
and women. In regard to the Green Party the dataset contains some of the most extreme statements found in the data-
set. Some examples for these are “KOGLER muss hängen vorm Parlament am besten” (Kogler need to hang, best infront 
of the parlament), “Das grüne Dreckpack muss ausgerottet werden!!!!” (The green pack needs to be made extinct), “Die 
Grünen gehören in die Gaskammer           ”(The greens belong in the gas chamber). This shows that far-right groups use 
extreme rhetoric to frame the green party as an enemy. For the green party, this may not be surprising. As a report by the 
Table 12   Second part of top ten keywords per label
Label
Keywords
Translation
Journalists
Medien, lügen, klamroth, lügenpresse, journalisten,
Media, lies, Klamroth, lying press, journalists,
Warum, tv, fernsehen, staatsfernsehen, regierung
Why, TV, television, state television, govern-
ment
Immigration_status
Migranten, land, deutschland, deutsche, menschen,
Migrants, country, Germany, German, people,
Gehen, kommt, leute, asyl, zurück
Go, comes, people, asylum, back
Anti-immigrant
Migranten, land, deutschland, deutsche, menschen,
Migrants, country, Germany, German, people,
Gehen, kommt, leute, asyl, zurück
Go, comes, people, asylum, back
Jews
Wehren, juden, eigene, schön, israel,
Defend, Jews, own, beautiful, Israel,
Goliath, gegenteil, gelenk, gemeinde, gerald
Goliath, opposite, joint, community, Gerald
Antisemitism
Wehren, juden, eigene, schön, israel,
Defend, Jews, own, beautiful, Israel,
Goliath, gegenteil, gelenk, gemeinde, gerald
Goliath, opposite, joint, community, Gerald
anti-LGBTQIA+
Frau, mutter, queer, sagen, wegen,
Woman, mother, queer, say, because,
Weibliche, sowas, kinder, person, männer
Female, such, children, person, men
Muslims
Islam, moschee, muslimischen, wann, muslime,
Islam, mosque, Muslim, when, Muslims,
Deutschland, deutschen, ändern, ganz, gegenüber
Germany, Germans, change, entirely, towards
Criminalisation
Verbrecher, grünen, gehört, gehören, müssen,
Criminals, Greens, belong, should belong, must,
Land, politiker, knast, regierung, sollten
Country, politicians, jail, government, should
Mysogyny_anti-feminism
Frauen, grünen, lang, riesen, fette,
Women, Greens, long, huge, fat,
Problem, richtig, ricarda, politik, zweite
Problem, right, Ricarda, politics, second
National_origin
Deutschland, türken, ausländer, deutschen, land,
Germany, Turks, foreigners, Germans, country,
Deutscher, problem, gut, erdogan, wählen
German, problem, good, Erdogan, vote
Not_readable
Klar, hunde, tut, land, schwul,
Clear, dogs, does, country, gay,
Ehe, city, bitte, betrug, sagt
Marriage, city, please, fraud, says
Men
Eier, männer, affen, endlich, frauen,
Eggs, men, apes, finally, women,
Gefragt, gehen, gerne, gesagt, zurück
Asked, go, like, said, back
White_supremacy
Weiße, kinder, übernommen, kleopatra, anbieten,
White, children, taken over, Cleopatra, offer,
Ausgehen, bauen, besten, camp, christus
Go out, build, best, camp, Christ
Physical_attributes
Lang, problem, grünen, ricarda, sterben,
Long, problem, Greens, Ricarda, die,
Riesen, fette, frau, fettes, fetten
Huge, fat, woman, fat, fat
Trans
Frau, transfeindlich, identifizieren, leben, person,
Woman, transphobic, identify, live, person,
Sowas, deutschland, männer, trans, chromosome
Such, Germany, men, trans, chromosome
Suppor_hateful_entities
Wähle, wurde, witz, trauermarsch, sofort,
Vote, became, joke, funeral march, immediately,
Rechte, npd, leute, heißt, eigentlich
Right-wing, NPD, people, actually called

--- Page 16 ---

Vol:.(1234567890)
Research	
 
Discover Data             (2025) 3:4  
| https://doi.org/10.1007/s44248-025-00020-y
German news-outlet Welt revealed, their co-chief and economic minister Robert Habeck has put forward 700 criminal 
reports because of mostly online hate crime alone in the time period in between April 2023 till July 2024.8 The findings 
in this research confirm such newspaper reports and underline it with quantitative data from three TikTok datasets.
6.2  Language‑specific observations
The language-specific observations were made retrospectively by the annotators, who reflected on common language 
characteristics and supported their findings with selected examples.
Two interesting aspects regarding the used language were observed. Firstly, online youth language in general, and 
Algospeak (the purposeful distortion of spelling [49]) in particular, was found to a small extent but were present in 
several examples. Some selected examples of Algospeak in the dataset include: “Ngr,” “                ,” “slam..pe fik dik,” “w3cht 
3uf,” “          ,” “Nªzis,” and “d*nnsch!$$.” The fact that there is little Algospeak may have to do with the age of the users or 
with the fact that Algospeak in the German social media world may be a relatively new phenomena. Future investiga-
tions may use this dataset as a historic reference point.
Secondly, the presence of local German dialects was noteworthy. Predominantly Bavarian or Austrian dialects were 
used to express problematic statements. Examples include: “ihr grieagts eichre rechnung...olle” (you will get the bill... 
all of you), “gusch pifke bua. Sonst gibt’s auf nosn” (leave, German braggart boy. Else you will be hit on the nose), and 
“Den deutschen hätt i dermaßen ane eini gehaut, dass er nimma aufsteht” (I would have hit the German so hard that he 
wouldn’t get up again). The general observation is that these dialects are often used to express very hateful thoughts. It 
may be that formulating hateful sentences in the dialect is a tactic applied by users to avoid moderation, or it may be that 
the hateful comments in dialect are written by genuine Bavarian/Austrian native speakers. This has yet to be explored.
6.3  Mental health
The three annotators consistently raised concerns in regular meetings regarding the adverse effects of the dataset’s 
negativity on their mental health. One annotator specifically noted that engaging extensively in annotation “gives you 
a dark worldview if you annotate too much in one day.” This experience aligns with observations documented in the lit-
erature [50]. Consequently, all three annotators chose to limit their annotation sessions to a few hours per day to sustain 
their well-being and productivity.
6.4  Further observations
Some of the comments in the dataset may also be interpreted as expressions of a form of “German angst.” For instance, 
statements like “Knapp nochmal Deutschland vor dem Tot gerettet” (“Barely saved Germany from its own death”) suggest 
Table 13   (a) Top 10 most used emoticons; (b) Results sentiment analysis
8  https://​www.​welt.​de/​polit​ik/​deuts​chland/​artic​le252​750350/​Habeck-​Wir-​werden-​dich-​haeng​en-​Wirts​chaft​smini​ster-​stellt-​700-​Straf​anzei​
gen-​wegen-​Hassk​rimin​alita​et.​html

--- Page 17 ---

Vol.:(0123456789)
Discover Data             (2025) 3:4  
| https://doi.org/10.1007/s44248-025-00020-y 
	
Research
somewhat of a doomsday scenario and may reflect a specific type of anxiety-German angst-similar to what historian 
Frank Biess explores in his book Republik der Angst (Republic of Fear) [51]. This modern German angst encapsulates fears 
related to immigration, national identity, and cultural change, echoing historical national anxieties while being shaped 
by the unique historical trajectories of today’s globalized world. Interestingly, these comments are not necessarily hate 
speech, but instead contribute to a climate of fear. Future work may explore if other German datasets contain also such 
particular fears in non-hateful comments, and explore if and to what extent there may be a relationship between the 
occurrence of fearful and hateful comments.
7  Discussion
This section is organized into several key areas: first, it addresses the dataset selection and collection process, followed 
by a discussion of the annotation schema and the annotation procedure. Next, the quantitative results are analyzed, 
followed by a detailed outline of the encountered limitations. Finally, the ethical considerations are discussed.
7.1  Dataset selection and collection
Focusing on a single platform as a content source introduces a clear bias into the dataset, as topics of conversation, lan-
guage, and demographic groups vary widely across social media platforms. However, because building these datasets is a 
time- and labor-intensive task, therefore this research should be seen as part of a larger, global effort to study hate speech 
across various social media platforms. Future work could now analyze the similarities and differences between platforms.
The process of identifying a specific set of accounts whose comment sections are analyzed also introduces bias into 
the dataset. However, as the primary goal of this research is to create a dataset focused on a specific subgroup of political 
activity on TikTok, this pre-selection is a necessary first step to ensure a reliable representation of German-speaking far-
right accounts. To achieve this, we collaborated with qualitative experts in online radicalization, who carefully selected 
these accounts to provide a general overview of German Austrian far-right online spaces.
The process of first selecting individual videos based on existing hate speech classifiers and then annotating all of 
their comments as either flagged for hate speech or not demonstrates its value, as it results in a reasonable amount of 
hate content without relying on word lists that would otherwise limit linguistic variety.
7.2  Schema and annotation procedure
The unbalanced nature of the dataset is comparative to prior research. The fact that 26.04% of the comments have 
received at least one hateful label by two of the annotators shows the high amounts of hate present in the dataset. 
In terms of annotation consistency, the inter-annotator agreement was calculated using the Fleiss’ Kappa, yielding 
an average score of 0.40. This indicates a fair level of agreement, bordering on moderate, which is acceptable given 
the complexity and subjectivity involved in annotating hate speech. The large discrepancy in annotations under-
scores the challenges in annotating hate speech, where context and individual perspectives are significant factors 
in the interpretation of each statement. With a smaller taxonomy and more annotators, the scores could maybe be 
improved upon. But with the large taxonomy creating a deep insight into the data this is a choice that was made, 
and can be referenced for further approaches.
In the annotation procedure, it would have been highly advantageous to have a larger annotation team to improve 
reliability. Additionally, providing more context for each annotated statement could have been beneficial. In this 
research, only the information that the statement was posted under a far-right TikTok video was provided. Supplying 
at least the topic of the video could have offered a useful reference point for annotators. However, identifying video 
topics on an individual basis is challenging and was beyond the scope of this project.
7.3  Quantitative results
The analysis showed that certain groups, particularly politicians, women, and immigrants, were frequent targets of 
hate speech. The most common types of hate identified were ‘insult,’ ‘threatening language,’ and ‘devaluation,’ show-
ing the aggressive and derogatory nature of the dataset.

--- Page 18 ---

Vol:.(1234567890)
Research	
 
Discover Data             (2025) 3:4  
| https://doi.org/10.1007/s44248-025-00020-y
The distribution of labels across the dataset further highlights the specific narratives of hate speech present. For 
instance, labels like ‘anti-wokeness,’ ‘delegitimization of liberal democracy,’ and ‘anti-immigrant’ narratives show the 
underlying ideologies supporting the hate speech. Because the dataset consists of comments from German and 
Austrian far-right influencers, the comment sections reflect how their political discourse can become a breeding 
ground for hate speech.
The keyword analysis shows the specific content of the hate speech, with political figures and entities like Olaf 
Scholz, Ricarda Lang, the AfD, and the Grünen party being frequently mentioned. The nature of these mentions, 
particularly against the Grünen party and the women affiliated with it, suggests a structured effort to attack and 
undermine certain political groups through hate speech. The use of online youth language and Algospeak, as well 
as the presence of local dialects like Bavarian and Austrian, also points to the diverse strategies employed by users 
to express themselves and their hate while evading moderation.
Finally, the sentiment analysis using a BERT-based classifier revealed a strong presence of negative sentiments, 
with 59.3% of the comments classified as negative. This finding is consistent with the high level of hate speech and 
further underlines the negative tone that dominates the comments in the dataset. The qualitative observations by 
the annotators, particularly regarding the high levels of hate directed toward the Grünen party and the use of coded 
language, shows the ongoing challenges in moderating and understanding hate speech in online environments.
7.4  Limitations
The dataset created in this study has certain limitations, some of which are discussed in detail in Sects. 7.1, 7.2, and 
7.3. A key limitation concerns the inter-annotator agreement. The observed moderate (bordering on fair) agreement 
presents a challenge for the research, as it underscores discrepancies among the trained annotators. This is further 
emphasized by the higher agreement scores observed among some annotators in certain classes. These discrepancies 
could hinder the future reuse of the dataset, particularly for tasks such as training specific classifiers. The moderate 
(bordering on fair) agreement is likely attributable to the large number of annotation classes.
Furthermore, several other biases and limitations must be acknowledged and addressed in future work. The dataset 
was collected exclusively during the fall of 2023, which restricts its temporal scope and may not capture long-term 
trends in hate speech. Additionally, the data was collected solely from a single platform, limiting the generalizability 
of the findings to other platforms. The annotators were exclusively German-speaking adults, which could pose chal-
lenges when interpreting and evaluating online youth language.
The initial data selection process relied on pre-trained hate speech classifiers using English translations as inputs, 
potentially introducing biases related to model performance and linguistic nuances. Finally, the dataset is restricted 
to textual content and does not include supplementary elements such as images, the topics of connected posts, or 
user behavior patterns (e.g., comment posting frequency), all of which could offer valuable insights into the propa-
gation of hate speech online.
7.5  Ethical considerations
This research focuses on societal interests, particularly the public good. Making these datasets available for research 
is essential to understanding fundamental societal developments. However, identifying and defining hate speech 
remains a complex challenge, as it directly relating to an individual’s personal freedom of speech. In line with this, 
the research does not claim to provide a singular definition of hate, but a general schema from which researchers 
can draw when defining hate speech in their own contexts.
It is important to ensure that this research and its datasets are shared only with validated scientific personnel 
to prevent misuse, therefore the dataset is only available after verification. Furthermore, algorithmic hate speech 
detection should not operate in isolation, it is essential to avoid reliance solely on automated methods. This research 
advocates for a hybrid human-in-the-loop approach to online moderation, fostering a safer environment for all. 
Continued collection and annotation of new datasets with humans-in-the-loop remains therefore essential for the 
understanding of evolving language and patterns in online hate speech.

--- Page 19 ---

Vol.:(0123456789)
Discover Data             (2025) 3:4  
| https://doi.org/10.1007/s44248-025-00020-y 
	
Research
8  Conclusion and future work
This research presents the first German TikTok dataset, comprising of 10,586 comments collected from different 
comment sections and annotated for hate speech. Domain experts identified far-right accounts, and an ensemble 
of established classifiers are used to select videos with high levels of hateful comments. A novel and extensive anno-
tation scheme with 32 labels was developed, and three trained annotators labeled the dataset, with 13.76% of the 
collected data identified as hateful.
A quantitative analysis was conducted, examining the primary keywords within hate speech classes, identifying 
label combinations and distributions, and performing a sentiment analysis. The most common types of hate iden-
tified were ‘insult,’ ‘threatening language,’ and ‘devaluation.’ The dataset reveals widespread hate directed toward 
German politicians, particularly members of the Green Party, as well as women and immigrants. This dataset offers a 
comprehensive view of the dynamics of hate speech on TikTok, highlighting both the challenges in annotation and 
the underlying narratives driving toxic discourse. These insights are crucial for developing more effective moderation 
strategies and understanding the social and political contexts that fuel online hate speech.
Future work will explore how this annotated dataset and the new taxonomy can be utilized in algorithmic hate 
speech classification. It would be interesting to explore how the comment sections differ between far-right content 
on TikTok and similar content on other platforms. The impact of the large taxonomy on the performance of the trained 
classifier needs careful examination. Additionally, the linguistic phenomena noted and their influence on the classifier 
require further study. Based on the identified trends and topics, specific moderation strategies could be developed 
to address the issues in the discourse.
Acknowledgements  Content Warning: This research contains examples of hate speech.
Author contributions  Conceptualization: J.F., E.T., M.H. R.J. E.J. and A.P. Methodology, J.F. E.T., E.J and A.P Figures: J.F. Validation: J.F., E.T., M.H. 
R.J. E.J. and A.P. Formal analysis: J.F. M.H. Resources: J.F., E.T., M.H. R.J. E.J. N.F. and A.P. Writing-original draft preparation: J.F., E.T., M.H., and R.J. 
Writing-review and editing: J.F., E.T., M.H. R.J. E.J. N.F. and A.P. Visualization: J.F. Supervision: E.J. and A.P. Project administration: J.F. All authors 
reviewed the manuscript.
Funding  No funding was received for this research.
Data availability  The data is available on Zenodo: https://​zenodo.​org/​recor​ds/​14677​171. It is accessible by request only and exclusively to 
researchers at verified research institutions with an active project in the field, demonstrating their contribution to the social good.
Code availability  The code is available for the ensemble of existing classifiers at Github: https://​github.​com/​filli​es/​diffr​entHa​teAlg​os.
Declarations 
Ethics approval and consent to participate  Not required since the dataset is collected within the public interest and specially just for research 
purposes. It will only be made available for research institutions and is anonymized, therefore can’t be traced back to the authors.
Consent for publication  Not required since the dataset is anonymized, therefore can’t be traced back to the authors.
Competing interests  The authors declare no competing interests.
Open Access   This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which 
permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to 
the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You 
do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party 
material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If 
material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds 
the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://​creat​iveco​
mmons.​org/​licen​ses/​by-​nc-​nd/4.​0/.
References
	 1.	 Kemp S. Digital 2023 April global statshot report—datareportal—global digital insights. DataReportal—Global Digital Insights 2023. 
https://​datar​eport​al.​com/​repor​ts/​digit​al-​2023-​april-​global-​stats​hot.

--- Page 20 ---

Vol:.(1234567890)
Research	
 
Discover Data             (2025) 3:4  
| https://doi.org/10.1007/s44248-025-00020-y
	 2.	 Dixon SJ. Facebook hate speech removal per quarter 2023 (2023). https://​www.​stati​sta.​com/​stati​stics/​10138​04/​faceb​ook-​hate-​speech-​
conte​nt-​delet​ion-​quart​er/.
	 3.	 Howarth J. Tiktok user age, gender, & demographics (2024). Exploding Topics (2024). https://​explo​dingt​opics.​com/​blog/​tiktok-​demog​
raphi​cs#​tiktok-​demog​raphic-​data.
	 4.	 Rydgren J. The oxford handbook of the radical right. New York: Oxford University Press; 2018. https://​doi.​org/​10.​1093/​oxfor​dhb/​97801​
90274​559.​001.​0001.
	 5.	 Bruter M, Harrison S. Mapping extreme right ideology: an empirical geography of the European extreme right. Basingstoke: Palgrave 
Macmillan; 2011.
	 6.	 Mudde C. Populist radical right parties in Europe. (No Title) 2007.
	 7.	 Akkerman T, Lange SL, Rooduijn M (eds.) Radical Right-Wing Populist Parties in Western Europe: Into the Mainstream?, 1st edn. Routledge 
Studies in Extremism and Democracy, p. 316. Routledge, London 2016. https://​doi.​org/​10.​4324/​97813​15687​988.
	 8.	 Lewys Brace SJB, Ging D. Where do ‘mixed, unclear, and unstable’ ideologies come from? A data-driven answer centred on the incelosphere. 
J Policing Intell Counter Terrorism. 2024;19(2):103–24. https://​doi.​org/​10.​1080/​18335​330.​2023.​22266​67.
	 9.	 Castelli Gattinara P, Pirro AL. The far right as social movement. Eur Soc. 2019;21(4):447–62.
	10.	 Ignazi P. Extreme Right Parties in Western Europe. Comparative Politics. Oxford University Press, Oxford; New York 2003.
	11.	 Waldron J. The harm in hate speech. Harvard university press 2012.
	12.	 Sellars A. Defining hate speech. Berkman Klein Center Research Publication. 2016;2016–20:16–48.
	13.	 Fortuna P, Soler J, Wanner L. Toxic, hateful, offensive or abusive? What are we really classifying? An empirical analysis of hate speech 
datasets. In: Proceedings of the Twelfth Language Resources and Evaluation Conference, 2020;6786–6794.
	14.	 Tontodimamma A, Nissi E, Sarra A, Fontanella L. Thirty years of research into hate speech: topics of interest and their evolution. Sciento-
metrics. 2021;126:157–79.
	15.	 Unesco., Gagliardone I, Gal D, Alves T, Martinez GMS. Countering Online Hate Speech / Iginio Gagliardone, Danit Gal, Thiago Alves, Gabriela 
Martinez. Unesco series on internet freedom. United Nations Educational, Scientific and Cultural Organization, Paris 2015.
	16.	 Slonje R, Smith PK, Frisén A. The nature of cyberbullying, and strategies for prevention. Comput Hum Behav. 2013;29(1):26–32.
	17.	 Udupa S, Maronikolakis A, Wisiorek A. Ethical scaling for content moderation: Extreme speech and the (in) significance of artificial intel-
ligence. Big Data Society. 2023;10(1):20539517231172424.
	18.	 Van Dijk TA. Critical discourse analysis. The handbook of discourse analysis, 2015;466–485.
	19.	 Scott JC. Weapons of the weak: Everyday forms of peasant resistance. Yale University P 1985.
	20.	 Haas J. Hate speech and stereotypic talk. In: Giles H, editor. The Handbook of Intergroup Communication. New York and London: Rout-
ledge; 2012. p. 128–40.
	21.	 Hameleers M, Meer T, Vliegenthart R. Civilized truths, hateful lies? Incivility and hate speech in false information-evidence from fact-
checked statements in the us. Inf Commun Society. 2022;25(11):1596–613.
	22.	 Hosseinmardi H, Mattson SA, Ibn Rafiq R, Han R, Lv Q, Mishra S. Analyzing labeled cyberbullying incidents on the instagram social network. 
In: Liu T-Y, Scollon CN, Zhu W, editors. Social Inf. Cham: Springer; 2015. p. 49–66.
	23.	 Gibert O, Perez N, García-Pablos A, Cuadros M. Hate speech dataset from a white supremacy forum. In: Proceedings of the 2nd Workshop 
on Abusive Language Online (ALW2), pp. 11–20. Association for Computational Linguistics, Brussels, Belgium 2018. https://​doi.​org/​10.​
18653/​v1/​W18-​5102. https://​aclan​tholo​gy.​org/​W18-​5102.
	24.	 ElSherief M, Kulkarni V, Nguyen D, Wang WY, Belding E. Hate lingo: a target-based linguistic analysis of hate speech in social media 2018.
	25.	 Wen X, Wang Y, Wang K, Sui R. A Russian hate speech corpus for cybersecurity applications. In: 2022 IEEE 8th Intl Conference on Big Data 
Security on Cloud (BigDataSecurity), IEEE Intl Conference on High Performance and Smart Computing, (HPSC) and IEEE Intl Conference 
on Intelligent Data and Security (IDS), 2022;41–47. https://​doi.​org/​10.​1109/​BigDa​taSec​urity​HPSCI​DS549​78.​2022.​00018.
	26.	 Mandl T, Modha S, Majumder P, Patel D, Dave M, Mandlia C, Patel A. Overview of the hasoc track at fire 2019: Hate speech and offensive 
content identification in Indo-European languages. In: Proceedings of the 11th Annual Meeting of the Forum for Information Retrieval 
Evaluation. FIRE ’19, pp. 14–17. Association for Computing Machinery, New York, NY, USA 2019. https://​doi.​org/​10.​1145/​33685​67.​33685​
84.
	27.	 Davidson T, Warmsley D, Macy M, Weber I. Automated Hate Speech Detection and the Problem of Offensive Language 2017. arxiv:​1703.​
04009.
	28.	 Founta A-M, Djouvas C, Chatzakou D, Leontiadis I, Blackburn J, Stringhini G, Vakali A, Sirivianos M, Kourtellis N. Large Scale Crowdsourcing 
and Characterization of Twitter Abusive Behavior 2018. arxiv:​1802.​00393.
	29.	 Mathew B, Saha P, Yimam SM, Biemann C, Goyal P, Mukherjee A. Hatexplain: a benchmark dataset for explainable hate speech detection. 
Proc AAAI Conf Artif Intell. 2021;35(17):14867–75. https://​doi.​org/​10.​1609/​aaai.​v35i17.​17745.
	30.	 Fillies J, Peikert S, Paschke A. Hateful messages: a conversational data set of hate speech produced by adolescents on discord 2023.
	31.	 Bretschneider U, Peters R. Detecting offensive statements towards foreigners in social media. In: Hawaii International Conference on 
System Sciences 2017.
	32.	 Wiegand M, Siegel M, Ruppenhofer J. Overview of the germeval 2018 shared task on the identification of offensive language. Proceedings 
of GermEval 2018, 14th Conference on Natural Language Processing (KONVENS 2018), Vienna, Austria—September 21, 2018, pp. 1–10. 
Austrian Academy of Sciences, Vienna, Austria 2019. https://​nbn-​resol​ving.​org/​urn:​nbn:​de:​bsz:​mh39-​84935.
	33.	 Assenmacher D, Niemann M, Müller K, Seiler MV, Riehle DM, Trautmann H. RP-Mod & RP-Crowd: Moderator-and Crowd-Annotated Ger-
man News Comment Datasets Supplementary Material.
	34.	 Demus C, Pitz J, Schütz M, Probol N, Siegel M, Labudde D. Detox: A comprehensive dataset for German offensive language and conversa-
tion analysis. In: Narang, K., Mostafazadeh Davani, A., Mathias, L., Vidgen, B., Talat, Z. (eds.) Proceedings of the Sixth Workshop on Online 
Abuse and Harms (WOAH), pp. 143–153. Association for Computational Linguistics, Seattle, Washington (Hybrid) 2022. https://​doi.​org/​
10.​18653/​v1/​2022.​woah-1.​14. https://​aclan​tholo​gy.​org/​2022.​woah-1.​14.
	35.	 Goldzycher J, Röttger P, Schneider G. Improving Adversarial Data Collection by Supporting Annotators: Lessons from GAHD, a German 
Hate Speech Dataset 2024. arxiv:​2403.​19559

--- Page 21 ---

Vol.:(0123456789)
Discover Data             (2025) 3:4  
| https://doi.org/10.1007/s44248-025-00020-y 
	
Research
	36.	 Chung Y-L, Kuzmenko E, Tekiroglu SS, Guerini M. CONAN—COunter NArratives through nichesourcing: a multilingual dataset of responses 
to fight online hate speech. In: Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics, pp. 2819–2829. 
Association for Computational Linguistics, Florence, Italy 2019. https://​doi.​org/​10.​18653/​v1/​P19-​1271. https://​aclan​tholo​gy.​org/​P19-​1271.
	37.	 Ranasinghe T, Zampieri M. Multilingual offensive language identification with cross-lingual embeddings 2020.
	38.	 Bartalesi V, Sprugnoli R, Lenzi VB, Moretti G. CAT: the CELCT Annotation Tool CREEP (Cyberbullying Effects Prevention) View Project It-
TimeBank View Project CAT: the CELCT Annotation Tool. http://​knowt​ator.​sourc​eforge.​net/​index.​shtml.
	39.	 Sprugnoli R, Menini S, Tonelli S, Oncini F, Piras E. Creating a WhatsApp dataset to study pre-teen cyberbullying. In: Proceedings of the 2nd 
Workshop on Abusive Language Online (ALW2), pp. 51–59. Association for Computational Linguistics, Brussels, Belgium 2018. https://​
doi.​org/​10.​18653/​v1/​W18-​5107. https://​aclan​tholo​gy.​org/​W18-​5107.
	40.	 Fillies J, Hoffmann MP, Paschke A. Multilingual hate speech detection: Comparison of transfer learning methods to classify German, Ital-
ian, and Spanish posts. In: 2023 IEEE International Conference on Big Data (BigData), 2023;5503–5511. IEEE.
	41.	 Aluru SS, Mathew B, Saha P, Mukherjee A. A deep dive into multilingual hate speech classification. In: Dong Y, Ifrim G, Mladenić D, Saunders 
C, Van Hoecke S, editors. Machine learning and knowledge discovery in databases. Applied data science and demo track. Cham: Springer; 
2021. p. 423–39.
	42.	 Vidgen B, Derczynski L. Directions in abusive language training data, a systematic review: garbage in, garbage out. PLoS ONE. 
2021;15(12):1–32. https://​doi.​org/​10.​1371/​journ​al.​pone.​02433​00.
	43.	 Gebru T, Morgenstern J, Vecchione B, Vaughan JW, Wallach H, Crawford K. Datasheets for datasets. Commun ACM. 2021;64(12):86–92. 
https://​doi.​org/​10.​1145/​34587​23.
	44.	 Bahlo N, Becker T, Kalkavan-Aydin Z, Lotze N, Marx K, Schwarz C, ims̨ek Y. Jugendsprache: Eine Einführung. J.B. Metzler, Stuttgart, Germany 
2019. https://​doi.​org/​10.​1007/​978-3-​476-​04767-0.
	45.	 Fleiss JL. Measuring nominal scale agreement among many raters. Psychol Bull. 1971;76(5):378.
	46.	 Landis JR, Koch GG. An application of hierarchical kappa-type statistics in the assessment of majority agreement among multiple observ-
ers. Biometrics, 1977;363–374.
	47.	 Banerjee M, Capozzoli M, McSweeney L, Sinha D. Beyond kappa: a review of interrater agreement measures. Can J Stat. 1999;27(1):3–23.
	48.	 Guhr O, Schumann A-K, Bahrmann F, Böhme HJ. Training a broad-coverage german sentiment classification model for dialog systems. 
In: Proceedings of the Twelfth Language Resources and Evaluation Conference, 2020;1627–1632.
	49.	 Fillies J, Paschke A. Simple llm based approach to counter algospeak. In: Proceedings of the 8th Workshop on Online Abuse and Harms 
(WOAH 2024), 2024;136–145.
	50.	 AlEmadi MM, Zaghouani W. Emotional toll and coping strategies: Navigating the effects of annotating hate speech data. In: Proceedings 
of the Workshop on Legal and Ethical Issues in Human Language Technologies@ LREC-COLING 2024, 2024;66–72.
	51.	 Biess F. German Angst: Fear and Democracy in the Federal Republic of Germany. New York and Oxford: Emotions in History. Oxford Uni-
versity Press; 2020.
Publisher’s Note  Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

```
