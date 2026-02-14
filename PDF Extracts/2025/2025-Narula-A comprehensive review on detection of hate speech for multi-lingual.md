---
title: "2025-Narula-A comprehensive review on detection of hate speech for multi-lingual - PDF Extract"
source_pdf: "2025-Narula-A comprehensive review on detection of hate speech for multi-lingual.pdf"
pages: 35
extracted_at: "2026-02-13T17:43:23.144611"
---

# PDF Extract: 2025-Narula-A comprehensive review on detection of hate speech for multi-lingual

**Source PDF:** 2025-Narula-A comprehensive review on detection of hate speech for multi-lingual.pdf
**Total Pages:** 35

---

## Content

```
--- Page 1 ---

Vol.:(0123456789)
Social Network Analysis and Mining (2024) 14:244 
https://doi.org/10.1007/s13278-024-01401-y
REVIEW PAPER
A comprehensive review on detection of hate speech for multi‑lingual 
data
Rachna Narula1 · Poonam Chaudhary1
Received: 18 April 2024 / Revised: 28 November 2024 / Accepted: 3 December 2024 / Published online: 11 January 2025 
© The Author(s), under exclusive licence to Springer-Verlag GmbH Austria, part of Springer Nature 2025
Abstract
The paper addresses the critical challenge of detecting and mitigating hate speech in Hindi across social media platforms, 
utilizing natural language processing (NLP) techniques. It underscores the complexities associated with the Hindi language, 
including the prevalence of code-switching, the existence of various dialects, and the inconsistent use of Romanized Hindi. 
These linguistic factors present significant challenges for developing automated systems capable of reliably identifying hate 
speech. The paper emphasizes the urgent need to confront hate speech in Hindi due to its potential to incite social unrest, 
propagate misinformation, and foster a culture of intolerance within India's diverse socio-political landscape. The research 
aims to address existing gaps in the detection of Hindi hate speech through employing advanced machine learning and deep 
learning methodologies. The overarching objective is to devise solutions that are not only technologically robust but also 
deeply attuned to the unique linguistic and cultural nuances of the Hindi language.
Keywords  Hate speech detection · Natural language processing (NLP) · Social media · Code-mixing · Machine learning · 
Deep learning · Linguistic diversity
1  Introduction
Hate speech refers to statements that incite hatred or write 
against individuals or groups, based on race or ethnicity, 
religion, nationality (or citizenship), gender, disability, and 
sexual identity. While social media networks are facilitating 
faster dissemination of information in the digital communi-
cation age, they have also seen rise as centers for spread of 
hate speech. That speech incites violence, spreads lies and 
fans the flames of hate. Citron and Norton (2011) argued that 
part of the problem with sites that support hate speech is not 
merely the technology but a social responsibility take-down 
method done in languages such as Hindi. Despite being the 
fourth most widely spoken language worldwide, detection 
of hate speech in Hindi is a difficult task owing to various 
linguistic peculiarities including code-mixing, wide variety 
of dialects and Romanized text on social media (Mandl et al. 
2020). In the Indian socio-political context, language plays a 
dual role in bringing communities together or driving them 
apart (Banks 2010)—making the creation of automated hate 
speech detection systems all the more challenging when such 
issues exist. However, there are not enough NLP resources 
available for Hindi so that its urgency can be addressed with 
full intensity (Bohra et al. 2018). The growth of hate speech 
targeting people on the basis of identity online requires 
improved systems for detection, especially in low-resource 
languages like Hindi (Citron and Norton 2011).
1.1  Problem statement
Social media has grown rapidly to make the world smaller 
place, in terms of communication, while at the same time 
laying ground for hate speech which is blatant disrespect 
to millions based on their identities. Hate speech detection 
is important to maintain the online environment that helps 
campaigns for respect, diversity, and dignity of both com-
munities as well as individuals.
Since the Hindi language is filled with diversity, idio-
matic expressions, and social media users usually respond 
in code-mixed sentences (Bohra et al. 2018; Jamatia et al., 
2020), detecting hate speech in Hindi (Sreelakshmi et al., 
 *	 Rachna Narula 
	
rachna22csd003@ncuindia.edu
	
Poonam Chaudhary 
	
poonamchaudhary@ncuindia.edu
1	
Department of Computer Science and Engineering, The 
Northcap University, Gurugram, Haryana, India

--- Page 2 ---

	
Social Network Analysis and Mining (2024) 14:244
244 
Page 2 of 35
2020) becomes a very tedious job. This is even worse with 
Romanised Hindi that needs more advanced NLP models. 
Moreover, there are fewer resources and research in Hindi as 
compared to English (Waseem et al. 2017). The potential of 
language to incite conflict and the socio-political connota-
tions in India make it all the more important for us to look 
at building effective detection systems for hate (Sachdeva 
et al. 2021).
It is against human rights hate speech undermines social 
peace, incites violence, and encourage discrimination. To 
prevent conflict and in order not to compromise over men-
tal health and societal safety, timely detection is important 
(Pohjonen and Udupa 2017; Wilson 2019). Moreover, it 
safeguards against radicalization, legal compliance, effective 
public deliberation and strengthens the capacities towards 
fostering constructive public discourse (Langton 2018; 
Timmermann 2008). Identifying hate speech is valuable to 
corporations and platforms as this allows them to maintain 
credibility and user trust (Matamoros-Fernández 2017).
Such hate speech can also lead to physical violence and 
discrimination, resulting in unrest within a community. 
These dangers are considerable, and effective detection helps 
in mitigating them and also protects the safety of the public, 
the mental health of individuals and their free speech (Awan 
2014; Tynes et al. 2019; Scrivens et al. 2018).
Hate speech, especially in Hindi, has been a pressing 
social issue within a linguistically diverse country like India. 
The absence of research in this area is low for Hindi hate 
speech detection, despite the need to carry out such works 
(Waseem et al. 2016; Gupta et al. 2021) This study aims 
to build robust detection models for Hindi which can solve 
various language issues like code-mixing and Romanized 
text to make online spaces safer (Davidson et al. 2017).
1.2  Hate speech classification and segmentation
See Tables 1, 2 and Fig. 1.
Segmentation suggests following:
•	 Supporting Negative Stereotypes (24%): This part prob-
ably refers to times when the speech in question supports 
harmful stereotypes about certain groups of people.
•	 Derogatory Language (16%): In this classification, the 
emphasis is on the use of slurs or offensive language 
Table 1   Hate speech classification
Type of hate speech
Description
Examples
Racial hate speech
Racial or ethnic targeting. This includes market-
ing tactics that target an individual based on 
their racial or ethnic background
Stereotypes, slurs, derogatory language related 
to race
Religious hate speech
Directed against individuals or groups due to 
religious beliefs/practices
Offensive remarks, derogatory comments about 
religious figures/rituals
Gender-based hate speech
Targets individuals based on gender or gender 
identity
Misogynistic/misandrist remarks, gender-based 
slurs, attacks on gender roles/identities
Sexual orientation &
Targeted towards individuals based on their 
sexual orientation
Derogatory language, harmful stereotypes about 
LGBTQ + individuals
Xenophobic hate speech
Targets individuals from other countries, cul-
tures, ethnicities
Anti-immigrant sentiment, derogatory terms for 
foreigners, promotion of nationalistic superior-
ity
Disability hate speech
Targets individuals with physical or mental dis-
abilities
Mocking, belittling, or expressing hatred towards 
people with disabilities
Political hate speech
Aims group or particular individuals based on 
the against political opinions
Extreme partisan comments, derogatory language 
about political figures, incitement to political 
violence
cyberbullying and online hate speech
Occurs on digital platforms and social media 
(can encompass any of the above)
Amplified reach and impact due to the online 
medium
incitement to violence
Speech encouraging/glorifying violence against a 
person or group
Dangerous due to potential for real-world harm, 
often illegal
Hate speech masquerading as free speech
Claims to be protected speech but spreads hate 
and intolerance
Coded language, dog whistles to convey hate 
under the guise of debate
Table 2   Percentage of categories and segment
Source: U.S. Government Accountability Office. (2024, January)
Category
Percentage
Perpetuates negative stereotype
16%
Other bias motivated speech
24%
Use of slur/epithet
29%
Unfair treatment
14%
Use of a derogatory symbol or image
3%
Verbal/written harassment
14%

--- Page 3 ---

Social Network Analysis and Mining (2024) 14:244	
Page 3 of 35 
244
directed at specific groups or individuals based on their 
inherent characteristics.
•	 Intimidation or Threats (14%): This division includes 
cases of attacks, whether verbal or in writing, with the 
intention to intimidate, demean, or threaten an indi-
vidual.
•	 Discriminatory Practices (14%): This category probably 
pertains to incidents where individuals face unjust or 
unequal treatment because of their connection to certain 
demographics.
•	 Display of Hateful Symbols (3%): Instances involv-
ing symbols or imagery that indicate animosity or bias 
against specific groups fall under this category.
•	 Various Other Prejudiced Expressions (24%): We reserve 
this broad category for all other types of biased expres-
sion that don't neatly fit into the previously mentioned 
groups.
Following are some statistics to focus on:
Facebook: During the third quarter of 2023, the number 
of hate speech items deleted by Facebook was 9.6 million, 
marking a decline from the 18 million removed in the second 
quarter.
Online Conversations: Between 2019 and mid-2021, a 
study of over 263 million UK and US dialogues revealed 
50.1 million discussions related to racist hate speech, either 
involving such violations or citing them in the course of 
communication. This demonstrates a 20% increase in online 
hate speech since the start of the pandemic.
Twitter: A study linked the incidence of online hate 
messages with the frequency of Twitter usage, focusing on 
how it affects the youth's online experiences regarding hate 
speech.
Trend Patterns: Following George Floyd's death, online 
racial hate speech surged by 250%, the largest rise observed 
during the study timeline from June 2019 to December 2022.
Recent findings by an EU report indicate an upswing in 
hate speech on social networks, with the primary victims 
being women, individuals of African descent, as well as Jew-
ish and Roma communities.
United States: The latest figures on Hate Crimes from the 
Home Office, accounting for the years 2017/2018, recorded 
1,605 instances of online hate crimes in England and Wales, 
which is about 2% of the overall hate crime figures.
These metrics also provide insight into the growing issue 
of hate speech and its persistence across different forms of 
social media, as well as the role of certain companies, in this 
case Facebook, in trying to fight this behaviour. The statis-
tics also imply that occurrences in the real world can greatly 
sway the volume of online hate speech, as evidenced by the 
events succeeding George Floyd's death (Fig. 2).
The chart, titled "Percentage of Teenagers in the United 
States Who Have Encountered Hate Speech on Social Media 
Platforms as of April 2018, by Type," illustrates the extent 
of different kinds of hate speech witnessed by teenagers. 
The categories of hate speech are displayed on the vertical 
axis, and the corresponding percentages of young respond-
ents who have reported encountering them are shown on 
the horizontal axis. The categories, along with their overall 
percentages, are listed below:
(a)	 Racist Hate Speech: 52%
Fig. 1   Segmentation of hate 
speech.  Source: U.S. Govern-
ment Accountability Office. 
(2024, January)

--- Page 4 ---

	
Social Network Analysis and Mining (2024) 14:244
244 
Page 4 of 35
(b)	 Sexist Comments: 52%
(c)	 Speech Against Religions: 46%
(d)	 Anti-Gay Remarks: 52%
(e)	 Experience of Any Mentioned Types of Hate Speech: 
64%
We divide each category into two segments, each repre-
senting the proportion of teens who frequently encounter 
hate speech versus those who encounter it occasionally. We 
do not disclose the specific frequencies for the "often" seg-
ment, but we detail the "sometimes" segment as follows:
Encounters with racist remarks: 12%
Instances of Sexist Speech: 14%
Witnessing anti-religion hate speech: 11%
Observing Homophobic Comments: 12%
Coming across any form of the listed hate speech: 21%
Common Sense Media and GfK collected this data 
through an online survey. The survey sampled 1,141 partici-
pants aged between 13 to 17 years in the U.S., from March 
22 to April 10, 2018. The compilation of this data is credited 
to Statista in the year 2023.
The rise of the internet and social media has transformed 
hate speech from localized, slow-spreading instances to a 
global, rapidly disseminated issue (Citron and Norton 2011; 
Awan 2014). Platforms like Facebook and Twitter amplify 
hate speech through algorithms that prioritize emotionally 
charged content, spreading it across borders (Gillespie 2018; 
Suzor 2018). Anonymity online emboldens users to express 
hate more aggressively (Marwick and Lewis 2017).
Traditional methods of control struggle to keep pace, 
making it crucial to balance free speech with moderating 
harmful content. Addressing this requires technological 
solutions, policy reforms, and civil society involvement to 
ensure a safe digital space (Gorwa 2019; Langton 2018; 
Tucker et al. 2018).
1.3  Hate speech identification
Identifying hate speech is extremely complex, requiring us 
to look at messages that insult others or groups of other 
people based upon the basis of ethnicity, race, sexual ori-
entation, religion or any one of personal identifiers. This 
is not limited to a technical process, but rather involves 
interpreting human language in contexts informed by 
linguistics, psychology and sociology. Natural language 
processing (NLP) and machine learning are crucial for 
analysing massive amounts of text data on the internet. 
However, it is important to consider the cultural and social 
context as hate speech is contextual to the society that 
gives rise to it. Combating hate speech is thus an interdis-
ciplinary field that demands not only technical talent but 
also a human and social touch when building inclusive and 
safe spaces online.
Hate speech is a term used to describe any type of slur, 
threat or language that is meant to humiliate and incite 
hatred against someone based on their identities such as 
ethnicity, race or religion. It runs the gamut between openly 
combative (pun intended) and insidiously carry offensive 
implication that only people with access to particular social 
groups are privy to. In particular, hate speech comes from 
many different media, including social networks or forums 
as well as traditional communication channels like television 
and radio. The quickening pace of information shared in the 
digital age has made hate speech an international concern 
that cuts across cultures and borders (Table 3).
Fig. 2   Percentage of teenagers 
in the United States. Source: 
Common Sense Media (2018)

--- Page 5 ---

Social Network Analysis and Mining (2024) 14:244	
Page 5 of 35 
244
1.4  General framework of text classification: 
the foundation of hate speech detection
One can implement hate speech detection as a text classifi-
cation task. Text classification is an example of classifying 
a text based on an existing set of predefined classes. The 
following stages can be distinguished during the implemen-
tation of classification.
•	 Preprocessing: Cleaning and normalizing text (e.g., 
removing punctuation, converting to lowercase, stem-
ming, lemmatization).
•	 Feature Engineering: Representing the text in a way 
suitable for machine learning algorithms. This includes 
traditional methods like Bag-of-Words, TF-IDF, and 
advanced techniques like word embeddings (Word2Vec, 
GloVe) and contextual embeddings (BERT, ELMo).
•	 Model Selection: Choosing a machine learning algorithm 
(e.g., Gaussian Naïve-Bayes, SVM, Decision Trees) or a 
deep learning framework
•	 Classification: Training the model to recognize pat-
terns in the data and predict the presence of hate speech, 
as well as any specific categories it might belong to 
(Table 4).
Text classification becomes more complex when dealing 
with multilingual hate speech (Vashistha & Zubiaga, 2020), 
introducing several challenges:
•	 Varied Linguistic Expressions: Hate speech presents 
itself differently across languages and cultural contexts. 
It's imperative for models to recognize language-specific 
lexicons, grammatical structures, and cultural references.
•	 Limited Resources: There's a dearth of extensive, anno-
tated datasets for hate speech in many languages, which 
makes it essential to employ methods like transfer learn-
ing and cross-lingual model training to utilize resources 
from languages that have ample data.
•	 Code Switching: Code-mixing, which entails switching 
from one language to another in a single sentence, is 
common in multilingual communities. Detection models 
must be capable of understanding and processing this 
common linguistic practice.
Hate speech can be complex, sometimes addressing sev-
eral identity facets (such as ethnicity, faith, or gender) or 
embodying various degrees of offensiveness. Multi-label 
classification addresses this complexity by allocating mul-
tiple categories to a given text.
•	 Transformational Solutions: These involve changing 
regular classification methods to work with problems 
that have more than one label, usually by using binary 
relevance or classifier chains.
•	 Managing Intricacy: With multi-label classification, 
there are more possible combinations of categories. This 
means that models need to be able to find and manage the 
complex links between these categories.
Table 3   Hate speech forms
Form of hate speech
Related words/phrases
Common sources
Racial
Racist slurs, ethnic jokes
Social media, forums
Ethnic
Xenophobic comments
Online news comments
Gender-based
Misogynistic or misandric remarks
Social media, blogs
Religious
Anti-religious slurs
Social media, television
Sexual orientation
Homophobic or transphobic language
Social media, public speeches
Nationality
Derogatory national stereotypes
Online forums, radio
Table 4   General framework
Phase
Description
Techniques
Text preprocessing
Preparing raw text for analysis
* Tokenization * Normalization * Stemming and Lemmatization
Feature extraction
Transforming text into numerical representations
* Bag-of-Words (BoW) * Term Frequency-Inverse Document Fre-
quency (TF-IDF) * Word Embeddings (Word2Vec, GloVe)
Model development
Building the hate speech classification model
* Supervised Learning (with labelled datasets) Deep Learning Archi-
tectures (CNNs, RNNs, LSTMs)

--- Page 6 ---

	
Social Network Analysis and Mining (2024) 14:244
244 
Page 6 of 35
1.5  Mathematical formulation
Symbol
Description
Explanation
D
Set of documents
A collection of text 
documents (e.g., 
tweets, comments, 
articles)
di
Individual document
A single text docu-
ment within the col-
lection D
⇀v
i
Feature vector repre-
sentation of di
A numerical represen-
tation of the docu-
ment, often using 
TF-IDF or word 
embeddings
f
Classification model
A function that maps 
input feature vectors 
to output labels
yi
True label of di
Binary value indicat-
ing if document di 
contains hate speech 
(1 = hate speech, 
0 = non-hate speech)
̂yi
Predicted probability 
of hate speech
The model's output 
estimating the 
likelihood that di is 
hate speech (a value 
between 0 and 1)
L(y,̂yi)
Cross-entropy loss 
function
Measures the discrep-
ancy between true 
labels and predicted 
probabilities
 → {0,1} f(
⇀v
i
) → {0,1}
Final function
Represents the com-
plete hate speech 
detection process, 
taking a feature 
vector as input and 
outputting a binary 
classification
The above table presented the Structure of the Mathematical 
Formulation which helps in abstracting the process as data-
set “D” consists of text documents ­di as features v⃗i in the 
form of vectors, extracted by TF-IDF or embeddings. These 
vectors are then fed into a classification model f that outputs 
binary labels ­yi indicating hate speech (1) or non-hate speech 
(0). They are predicted probabilities yi that represent the 
chances of hate speech, tweaked by minimizing loss L(y,̂yi) 
using cross-entropy. This last function f(
⇀v
i ) → {0,1} finishes 
the detection step.
1.6  Framework for hate speech detection 
and classification on social media
The figure illustrates a workflow for hate speech detection, 
starting with data collection (annotation and preprocessing). 
It progresses to feature extraction using techniques like TF-
IDF and embedding matrices, followed by model training 
using machine learning algorithms (e.g., XG_Boost, SVM). 
Finally, it evaluates the model's performance for hate speech 
classification (Fig. 3).
1.7  Ethical considerations
Hate speech is one of the more nuanced features to detect, 
as it requires processing messages that dehumanize fellow 
humans by virtue of their race, ethnicity or religion. It is 
highly interdisciplinary as it draws from linguistics, psychol-
ogy and sociology and also depends on natural language 
processing (NLP) and machine learning in order to make 
progress. Hate speech is contextual and requires farmers to 
take into account cultural and societal norms. Tackling hate 
speech effectively is a balance between technology and com-
passion in creating inclusive spheres for feeling safe on the 
internet. From overt slurs to more subtle language only the 
particular community would understand, hate speech comes 
Fig. 3   General workflow 
diagram of hate speech detec-
tion.  Adapted from Classifica-
tion of Hate Speech Language 
Detection on Social Media: 
Preliminary Study for Improve-
ment, Scientific. Source: Figure 
on ResearchGate, available at 
https://​www.​resea​rchga​te.​net/​
figure/​Gener​al-​workf​low-​diagr​
am-​of-​hate-​speech-​detec​tion_​
fig1_​36319​1363

--- Page 7 ---

Social Network Analysis and Mining (2024) 14:244	
Page 7 of 35 
244
in many forms. From social media, forums to conventional 
media sources it stems from a wide range of results and the 
globalization in information circulation during the digital era 
has specifically contributed to this phenomenon.
1.8  The complexity of the Hindi language
That complexity, in terms of dialects, scripts and a high 
degree of code-mixing makes it much harder to identify hate 
speech in Hindi. All of these dialects include author's writ-
ings—Awadhi, Bhojpuri etc., and are written via Devanagari 
and Romanized scripts leading to technical challenges in 
the development of an NLP model. In fact, a lot of code-
mixing is done with English and other languages (especially 
when we are venting on social media). To effectively detect 
hate speech in Hindi, these linguistic challenges need to be 
addressed with advanced NLP models specifically designed 
to accommodate the idiosyncrasies of this language.
1.9  The role of social media platforms
Twitter, Facebook or Instagram are mediums of political and 
social discussion; however they also facilitate hate speech. 
Algorithms that seek to maximize clicks and user engage-
ment may put a heavier thumbs up on inflammatory content, 
leading to more exposure for hate speech. This bias in algo-
rithms combined with the echo chamber effect, fuels and 
normalizes hate speech among communities. This calls for 
a rethink of algorithms and action from all, where platform 
operators, policymakers and civil society work together to 
combat hate speech but not free expression.
1.10  Review techniques
The review follows a systematic literature analysis struc-
ture and involves an exhaustive search of databases includ-
ing IEEE Xplore, ACM Digital Library, PubMed, Scopus 
and Web of Science. Inclusion criteria were established to 
select from peer-reviewed articles about hate speech detec-
tion, analysis, and mitigation available in English. Research 
methods and thematic areas of focus were identified by ana-
lysing the articles year-wise which has been presented in 
table below.
1.11  Structure of the content
Section
Content
Description
1. Introduction
Background and 
problem statement
Outlines the issue of 
hate speech in Hindi, 
its prevalence, and 
potential negative 
impacts
Section
Content
Description
Clearly states the 
specific aims and 
goals of our research 
investigation
2. Systematic Litera-
ture Review
Sources and search 
terms
Details databases used 
(e.g., Scopus, Web 
of Science), targeted 
keywords, and 
inclusion/exclusion 
criteria
Analysis of existing 
work
Summarizes major 
research themes, 
methods used for 
Hindi hate speech 
detection, identified 
strengths and gaps in 
the current literature
3. Research Method-
ology
PRISMA Framework Outlines steps 
followed in the 
systematic review 
(identification, 
screening, eligibility, 
included studies)
Bibliometric Analy-
sis
Describes use of tools 
and techniques 
(e.g., VOSviewer, 
CiteSpace) to visual-
ize trends, research 
clusters, influential 
authors, etc
4. Proposed Frame-
work
Architecture
Diagram or visual 
flowchart of our 
overall hate speech 
detection system
5. Findings
Performance Metrics
Presents results using 
relevant metrics 
(accuracy, precision, 
recall, F1-score) 
with comparisons 
to benchmarks if 
available
Analysis and Discus-
sion
Interprets results, 
potential reasons for 
performance, and 
insights into Hindi 
hate speech charac-
teristics
6. Future Scope and 
Potential Chal-
lenges
Limitations
Acknowledges limita-
tions of our current 
work and potential 
biases in the dataset
7. Research Objec-
tives
Potential Research 
Directions
Suggests areas for 
improvement, novel 
methods, addressing 
ethical considera-
tions
8. Conclusion
Key takeaways
Summarizes the 
main findings and 
contributions of our 
research

--- Page 8 ---

	
Social Network Analysis and Mining (2024) 14:244
244 
Page 8 of 35
1.12  Research objective
Building a new target-based hate speech database: The aim 
of this work is to create a target-based hate speech focusing 
dataset in Hindi language as there exist lesser high quality 
labelled datasets available till date. Using this dataset will be 
able to target some things; for example, individuals or com-
munities, more detailed analyses (Waseem and Hovy 2016). 
The data will be collected across a wide range of digital 
platforms, included (Davidson et al. 2017). Reliability and 
validity will be assured through rigorous annotation proto-
cols, whilst linguistic and cultural nuances are addressed 
(Bohra et al. 2018). The data set will be validated and refined 
to obtain a robust data set, and strict privacy and ethical 
standards may also be applied (Zarsky 2016).
Lexical, Syntactic and Semantic Feature Evaluation: The 
second aim is to analyze those lexical, syntactic and seman-
tic features which enhance the hate speech detection clas-
sifiers. It will also focus on lexical features such as TF-IDF 
vectors, syntactic features like part of speech based tagging 
and semantic features such as word embeddings and senti-
ment analysis (Gupta et al. 2021; Joshi et al. 2020). Then, we 
evaluate the ability of these features to detect hate speech in 
a comparative fashion. This study will modify these attrib-
utes in accordance with the specific language characteris-
tics of Hindi, including code-mixing (Kumar and Jha 2020) 
and morphological structure (Zhang and Wallace 2017), to 
achieve the best model performance.
Robust and Efficient Classification Strategy: The third 
aim is to establish state-of-the-art classifiers like machine 
learning (SVM) and deep learning (LSTM)-based meth-
ods for multi-class classification. It would provide granular 
insights not just regarding the presence of hate speech but 
also classify its intensity and type (Cortes and Vapnik, 1995; 
Hochreiter and Schmidhuber 1997). These will be accurate 
and efficient models developed to manage the linguistic chal-
lenges in Hindi (Bohra et al. 2018). Improvement will be 
ensured by benchmarking against existing models, and the 
classification process will be guided by ethical considera-
tions to avoid biases (Sap et al. 2019).
2  Literature reviews
2.1  Research background
Hindi, as a language, exhibits unique characteristics that 
make hate speech detection (Das et al., 2021) particularly 
challenging. The language's inherent features, such as its 
syntactic structure, idiomatic usage, and the prevalence of 
code-mixing, where Hindi is blended with English and other 
regional languages, add layers of complexity to the prob-
lem (Bohra et al. 2018). In addition, the frequency of the 
use of non-standardized Romanized Hindi on social media 
platforms enables the spread of highly context-specific lan-
guage, which complicates the creation of efficient automated 
detection systems. Such linguistic particularities require the 
development of something in the field that is somewhat dif-
ferent from traditional NLP methods used with such lan-
guages as English.
2.2  Systematic reviews and key findings
See Table 5.
2.3  Major research with result and finding 
across years in various datasets
See Table 6.
2.4  Datasets on Indian language
See Table 7.
2.5  Model wise comparison
See Table 8.
2.6  Major attributes for English HS detection
See Table 9.
2.7  Major attributes for non‑English language in HS 
detection
See Table 10.
2.8  Thematic analysis of models across years
See Table 11.
2.9  Sub‑thematic and trend‑analysis
See Table 12.
Sub-thematic analysis depicts following:
Psychological Havoc: Hate speech harm victims (e.g., 
increased anxiety, depression) whilst giving credence to 
radical beliefs for perpetrators, or distress/desensitization 
with bystanders.
Content Analysis Methodologies: Keyword lists, senti-
ment analysis, and linguistic feature extraction detect hate 
speech by analysing content of character attacks, insults, 

--- Page 9 ---

Social Network Analysis and Mining (2024) 14:244	
Page 9 of 35 
244
Table 5   Review of literature
Author(s)
Country
Dataset
Objective
Methodology
Key findings
Davidson et al. (2017)
USA
Twitter data
Distinguish hate speech and offensive 
language
Crowd-sourced lexicon, multi-class 
classifier
Difficulty classifying tweets without 
explicit keywords; racist/ content with 
homophobic usage attribute to be hate 
speech
Mathew et al. (2021)
Multi-national
HateXplain (self-created)
Develop explainable hate speech mod-
els, reduce bias
Various models on HateXplain dataset
Good performance but poor explainabil-
ity; providing rationales during training 
improves performance
Ousidhoum et al. (2019)
Multi-national
Multilingual, multi-aspect dataset (self-
created)
Facilitate multilingual, multi-ti-label 
hate speech analysis
Evaluation in various classification 
settings
Dataset enables analysis in a wider 
context
Mulki et al. (2019)
Multi-national
L-HSAB Dataset (self-created)
Create benchmark dataset for Levantine 
hate speech detection
Detailed data collection and annotation 
guidelines
Provides basis for automated detection in 
Levantine Arabic
Mubarak et al. (2017)
Egypt
Twitter data
Detect slur language in Arabic social 
network
Obscene word list, user classification
Classifies users, provides dataset
Das et al. (2022)
India
HateCheckHIn dataset (self-created)
Evaluate various models of Hindi hate 
speech detection
Test cases based on real Hindi conversa-
tions to assess models
Emphasizes the need for more nuanced 
evaluation metrics beyond accuracy/
F1-score
Bohra et al. (2018)
India
Hindi-English Code-Mixed Dataset 
(self-created)
Hate speech evaluation in code-mixed 
corpus Hindi-English Data
Word-level annotations, linguistic 
features, classification system
Highlights challenges of code-mixed hate 
speech detection
Kapil et al. (2023)
India
HHSD dataset (self-created)
Enhance hate speech detection through 
multi-task learning for Hindi language
Hierarchical dataset of hate speech and 
related tasks; comparison of STL vs 
MTL
MTL significantly outperforms STL
Bansod (2023)
India
Hindi dataset
Explore the effectiveness of various 
embedding techniques
Combines machine learning classifiers 
with fastText, GloVe, distilBERT, and 
MuRIL
Transformer-based models with MuRIL 
embeddings lead to superior results
Shukla et al. (2022)
India
Hindi dataset
Propose a model combining BERT and 
CNN for enhanced detection
Two-stage architecture leverages BERT 
for encoding and CNN for classifica-
tion
Demonstrates the synergy between pre-
trained models and deep learning
Al-Hussaeni et al. (2023)
Multi-national
Code-mixed English/Hindi-English
Examine the role of data pre-processing 
in the context of detection of hate 
speech
10-step cleansing process followed by 
CNN and LSTM detection methods
Thorough data pre-processing boosts 
model accuracy and efficiency
Sameer (2022)
India
Code-mixed tweets
Classify hate speech in code-mixed 
English/Hindi-English tweets
Explores CNN and LSTM with 
character-level embedding
Improved model accuracy and runtime
Phung and Cloos (2022)
Multi-national
Hindi and Bengali
Explore the scope of transfer learning in 
the pipeline hate speech detection
Neural network, limited computational 
resources
Demonstrates potential of transfer learn-
ing for low-resource language pairs
Prashant Kapil and Asif 
Ekbal (2022)
India
Hindi datasets
Improve Hindi hate speech detection 
with multi-task learning
Deep neural networks (M-BERT, 
MuRIL), STL, MTL, transfer learning
Multi-task learning with cross-lingual 
pre-training significantly boosts per-
formance
Chopra et al. (2023)
India
Code-mixed Hindi-English, Devanagari
Detect hate speech in code-mixed and 
native language forms
Tabnet classifier on MuRIL extracted 
features
Model detects hate speech in both for-
mats, highlighting its versatility
Das et al. (2022)
India
HateCheckHIn (self-created)
Develop nuanced evaluation tool for 
Hindi hate speech models
Real-world inspired test cases, evalua-
tion of m-BERT, Perspective API
Traditional metrics don't capture model 
weaknesses, HateCheckHIn provides 
better diagnostics
Kapil et al. (2023)
India
HHSD dataset (self-created)
Enhance Hindi hate speech detection 
through multi-task learning
Hierarchical dataset of hate speech, 
related tasks; comparison of STL vs 
MTL
MTL significantly outperforms STL

--- Page 10 ---

	
Social Network Analysis and Mining (2024) 14:244
244 
Page 10 of 35
Table 5   (continued)
Author(s)
Country
Dataset
Objective
Methodology
Key findings
Al-Hussaeni et al. (2023)
Multi-national
Code-mixed English/Hindi-English
Examine data pre-processing impact on 
hate speech detection
10-step cleansing, CNN and LSTM 
models
Pre-processing boosts model accuracy 
and efficiency
Bansod (2023)
India
Hindi dataset
Explore embedding effectiveness for 
hate speech detection
Combines machine learning classifiers 
with fastText, GloVe, distilBERT, and 
MuRIL
Transformer-based models with MuRIL 
excel
Bohra et al. (2018)
India
Hindi-English Code-Mixed Dataset 
(self-created)
Detect hate speech in code-mixed 
Hindi-English
Word-level annotations, linguistic 
features, classification system
Highlights challenges of code-mixed hate 
speech detection
Shukla et al. (2022)
India
Hindi dataset
Propose a BERT + CNN model for 
enhanced detection
Two-stage architecture leverages BERT 
for encoding and CNN for classifica-
tion
Demonstrates the synergy between pre-
trained models and deep learning
Sameer (2022)
India
Code-mixed tweets
Classify hate speech in code-mixed 
English/Hindi-English tweets
Explores CNN and LSTM with 
character-level embedding
Improved model accuracy and runtime
Phung and Cloos (2022)
Multi-national
Hindi and Bengali
Explore transfer learning for hate speech 
detection
Neural network, limited computational 
resources
Demonstrates potential of transfer learn-
ing for low-resource language pairs
Sohn and Lee (2019)
South Korea
Multilingual
Cross-lingual hate speech detection
MC-BERT (Multilingual and multi-
channel BERT), translations
Model works well across languages, 
highlights translation's usefulness
Yadav et al. (2023)
India
English—Hindi code-mixed
Detect hate speech in code-mixed lan-
guage, ensure model coherence
ML models, LIME for explainability
Presence of slur words heavily influences 
classification
Ghosh et al. (2023)
India
Bodo, Assamese
Hate speech detection in low-resource 
languages
ML, DL, BERT, adds to a multilingual 
dataset
Provides a benchmark for less-resourced 
languages in the region
Lanasri et al. (2023)
Algeria
Algerian dialect corpus (self-created)
Detect hate speech in the Algerian 
dialect
Deep Learning models
Shows promise for dialect-specific hate 
speech detection
Prasad et al. (2023)
India
English, Hindi, Hinglish, Bengali, 
Marathi
Detect hate speech across multiple 
Indian languages
Meta-learning approach
Adapts to unseen languages, overcomes 
data scarcity
Author(s)
Country
Dataset
Objective
Methodology
Key Findings
India
English, Hindi, Marathi
Detect hate speech and offensive lan-
guage in multiple Indian languages
Machine learning, transfer learning, 
multilingual pre-trained models
Highlights challenges, methods for multi-
lingual, low-resource contexts
Davidson et al. (2017)
USA
Twitter data
Differentiate hate speech from offensive 
language
Crowd-sourced lexicon, multi-class 
classifier
Difficulty classifying tweets without 
explicit keywords; racist/homophobic 
content more likely to be hate speech
Talat and Hovy (2016)
Multi-national
Twitter data
Analyze features predictive of hate 
speech (racist/sexist)
Large annotated corpus, linguistic and 
extra-linguistic feature analysis
Importance of broader context in hate 
speech detection
Sap et al. (2019)
USA
Hate speech datasets
Examine racial bias in hate speech 
detection models
Analysis of surface markers of AAE 
and toxicity ratings
Models can inadvertently amplify harm 
against minorities
Badjatiya et al. (2017)
India
Twitter data
Employ the framework deep learning 
for hate speech detection
Deep learning effective for semantic 
word embeddings
Deep learning outperforms char/word 
n-grams, better handles nuance in 
language
Mathew et al. (2020)
Multi-national
HateXplain (self-created)
Develop explainable hate speech mod-
els, reduce bias
Various models on HateXplain dataset
Good performance but poor explainabil-
ity; providing rationales during training 
improves performance
Sohn and Lee (2019)
South Korea
Multilingual
Multi-lingual hate speech detection
MC-BERT (Multilingual and multi-
channel BERT), translations
Model works well across languages, high-
lights the usefulness of translation
Yadav et al. (2023)
India
English—Hindi code-mixed
Detect hate speech in code-mixed lan-
guage, ensure model coherence
ML models, LIME for explainability
Presence of slur words heavily influences 
classification

--- Page 11 ---

Social Network Analysis and Mining (2024) 14:244	
Page 11 of 35 
244
Table 5   (continued)
Author(s)
Country
Dataset
Objective
Methodology
Key findings
Al-Hussaeni et al. (2023)
Multi-national
Code-mixed English/Hindi-English
Examine data pre-processing impact on 
hate speech detection
10-step cleansing, CNN and LSTM 
models
Pre-processing boosts model accuracy 
and efficiency
Ibrahim et al. (2023)
Indonesia
Indonesian tweets
Address data scarcity in gender-based 
detection of hate speech
Data augmentation strategies (random 
insertion, back-translation)
Augmented data improves performance 
while maintaining label accuracy
Ghosh et al. (2023)
India
Bodo, Assamese
Hate speech detection in low-resource 
languages
ML, DL, BERT, adds to a multilingual 
dataset
Provides a benchmark for less-resourced 
languages in the region
Aluru et al. (2020)
India
Multilingual
Evaluate multilingual hate speech detec-
tion models
Embedding and deep learning models 
on 9 languages
Simpler models effective for low-
resource, whereas BERT-based high-
resource languages
Röttger et al. (2022)
Multi-national
Multilingual HateCheck (self-created)
Create diagnostic tools for hate speech 
models
Functional test suite for 10 languages
Reveals biases in datasets and models; 
need for improved evaluation tools
Rabiul Awal et al. (2023)
Bangladesh
Multilingual
low-resource languages’ Meta-learning 
for hate speech detection
HateMAML framework with self-
supervision
Outperforms baselines in cross-domain 
multilingual settings
Author(s)
Country
Dataset(s)
Objective
Methodology
Findings
Gandhi et al
India
Indonesian tweet dataset
(1) Review recent hate speech 
detection research
(1) Literature survey
Proposed model and metrics outper-
form existing benchmarks
(2) Implement models with new 
metrics
(2) Model comparison (ML vs. 
DL)
(3) Propose "hatefulness" and 
"intensity" metrics
Chhabra and Kumar
India
Several hate speech benchmark 
datasets
It produces a comprehensive survey 
of hate speech detection
Literature review
Highlights multimodal and multilin-
gual focus as crucial to hate speech 
detection
Focus on multimodal and multilin-
gual methods
Comparative analysis of methods
Provides a resource for understand-
ing datasets, methodologies, and 
performance metrics
Discuss datasets, challenges, evalu-
ation techniques
Presentation of benchmark datasets 
and top-performing approaches

--- Page 12 ---

	
Social Network Analysis and Mining (2024) 14:244
244 
Page 12 of 35
etc. but are context-dependent and struggle with evolving 
language.
ML Algorithms: Models (Naive Bayes, SVMs, CNNs, 
RNNs, Transformers) perform remarkably well using pat-
terns and context in the text for hate speech detection.
Platform Regulation: Social media platforms utilize poli-
cies, user reporting, and AI moderation systems to regulate 
such publication of hate speech within the content. This 
always leaves a dilemma between exercising freedom of 
speech and censoring hate speech.
These are Educational Campaigns: Awareness programs 
and workshops educate users about the impact of hate 
speech, promoting respectful behaviour and digital literacy.
AI Models and Bias: Use of Transgender Data, and More 
November 2023 Focus on facing issues such as various train-
ing data sources and algorithmic bias (in example human 
bias). The more fairness metrics are available, and the more 
diverse datasets will promote or reinforce the argument.
AI Model Explainability: Using methods like SHAP and 
LIME determine the transparency of the hate speech models 
to ensure trust and accountability in AI systems.
Detection and Action in Real Time: The Technologies 
flag hate speech in real time allowing swift action such as 
content removal, account suspension, or user warning; and.
Fighting back against deepfakes and synthetic media: 
Advanced detection techniques tackle AI-generated hate 
speech, deepfakes, and manipulated content to safeguard 
authenticity.
Other Strategies: Efforts to promote inclusion, Commu-
nity-based interventions, and a more robust legal framework 
should go hand-in-hand with more technical solutions to 
tackle hate speech.
2.10  Dataset feature discussion across the year
See Tables 13 and 14.
3  Proposed architectural framework 
for hate speech detection
3.1  Data preprocessing
Data Collection: Assemble a diverse dataset from various 
online platforms where Hindi is commonly used, such as 
Twitter, Facebook, news forums, and blogs. The dataset 
should include a wide range of topics to capture different 
contexts where hate speech may occur.
Data Cleaning: Implement text normalization techniques 
like removing special characters, emojis, and redundant 
white spaces. Convert all text to a standard format, typi-
cally lowercase, to ensure uniformity. This step is crucial 
for Hindi text, which may contain diverse dialects and 
colloquialisms.
Data Annotation: Engage bilingual experts proficient 
in Hindi and English to manually annotate the dataset. 
Each instance should be labelled as 'hate speech' or 'non-
hate speech.' Consider cultural sensitivities and contextual 
nuances during annotation.
Annotated datasets for hate speech detection in Hindi 
are a necessity as these need to be specific and elaborate. 
The first step involves the identification and collection of 
rich-text data on social media, online discussion forums and 
news websites that focus on various areas where Hindi is 
spoken. The focus of this data collection is on actual lan-
guage, as produced on the digital platform and soon contains 
code-switching (Al-Hussaeni et al. 2023) as well romanized 
Hindi.
After retrieving the text, it goes through pre-processing. 
This ensures that spelling variations are removed, Roman-
ized Hindi is normalized, and slang and colloquial expres-
sions are tackled. This is followed by the tokenization, which 
prepares the data for annotation (Al-Hussaeni et al. 2023).
Annotation guidelines are created that spell out what con-
stitutes hate speech in various categories including racial, 
religious, gender-based and xenophobic hate. Fluent Hindi 
speakers and dialects are recruited as annotators who are 
then trained on these specifications. A detailed description 
of the collaborative localization process is available, which 
follows a strict quality control protocol to ensure data accu-
racy and consistency (Al-Hussaeni et al. 2023).
This highlights an important realization of not everyone 
speaking the same Danish language. Samples from differ-
ent Hindi dialects are attempted to be included, as well as 
cultural and contextual nuances. Similarly, annotators are 
trained to identify hate speech and provide accurate labels 
for such sentences that involve code-switching (Al-Hussaeni 
et al. 2023).
Finally, we compile all the annotated data into a format-
ted dataset with equal number of hate speech and non-hate 
speech examples. The resulting dataset is accessible to the 
research community, together with comprehensive documen-
tation of the annotation process and guidelines, promoting 
resource sharing and iteration (Al-Hussaeni et al. 2023).
3.2  Tokenization, stop words removal 
and lemmatization
Tokenization: Create or use existing tokenizers that can 
properly segment Hindi text into words or tokens. Our pro-
cess needs to be able to deal with Devanagari script com-
plexities of conjuncts and diacritics are a challenge.
Stop-word removal: This is one of the main preprocess-
ing features in hate speech detection models. This includes 
removing stop-words (such as the, is, in, and and). Despite 

--- Page 13 ---

Social Network Analysis and Mining (2024) 14:244	
Page 13 of 35 
244
Table 6   Dataset wise results
Name of research paper
Published date
Dataset used
Results and findings
Sinhala Hate Speech Detection in Social Media using Text 
Mining and Machine learning
2019
Sinhala social media comments
Character trigram with Multinomial Naïve Bayes achieved 
92.33% accuracy
KBCNMUJAL@HASOC-Dravidian-CodeMix-FIRE2020: 
Using Machine Learning for Detection of Hate Speech and 
Offensive Codemix Social Media text
2021
Malayalam and Tamil social media data
Achieved F1 scores of 0.77 and 0.87 for Malayalam and Tamil 
respectively 0.87 for using n-gram features
Detection of Hate Speech Texts Using Machine Learning 
Algorithm
2022
14,000 comments from Chadian Facebook pages
FastText with SVM classifier achieved 95.4% accuracy for 
insult detection and 93.9% for hate speech
Sentiment Analysis and Homophobia detection of YouTube 
comments in Code-Mixed Dravidian Languages using 
machine learning and transformer models
2022
Code-mixed Dravidian language social media comments
F1-score of 0.63 for sentiment analysis and 0.95 for homopho-
bia detection in Malayalam dataset
Hate Speech and Offensive Content Identification in English 
and Indo-Aryan Languages using Machine Learning 
Models
2022
HASOC Hindi-English dataset
Combined word-level and character-level features outper-
formed pre-trained embeddings
Sinhala Hate Speech Detection in Social Media Using 
Machine Learning and Deep Learning
2022
Sinhala social media comments
FastText with RNN showed the best performance with an 
AUC ROC of 0.71 and 70% accuracy
Hate Speech Detection Using Machine Learning
2023
Twitter data
Delved into several NLP architecture for classification of Hate 
Speech through ML/DL models
Hate Speech is not Free Speech: Explainable Machine 
Learning for Hate Speech Detection in Code-Mixed 
Languages
2023
English and Hindi code-mixed datasets
Bernoulli Naive Bayes implemented along with count vector-
izer and TF-IDF reached the highest accuracy of 67.61%
Detecting Hate Speech and Offensive Language using 
Machine Learning in Published Online Content
2023
Twitter and Facebook data
Architected a model for Social media hates-speech detection
Hate Speech in Social Networks and Detection using 
Machine Learning Based Approaches
2023
Twitter data
Artificial neural network outperformed other algorithms for 
hate speech detection on Twitter
KBCNMUJAL@HASOC-Dravidian-CodeMix-FIRE2020
2021
Malayalam and Tamil social media data
Achieved F1 scores of 0.77 and 0.87 for Malayalam and Tamil 
respectively 0.87 for using n-gram features
Multi-modal Hate Speech Detection using Machine Learning 2021
Video contents
Proposed a multi-modal system to detect hate speech from 
video contents
Applying Transfer Learning using BERT-Based Models for 
Hate Speech Detection
2021
English, Hindi, Marathi social media data
Best results with BERT-based models; highest Macro-F1 of 
0.7993 (English), 0.7612 (Hindi), 0.8306 (Marathi)
Tuning Hyperparameters of Machine Learning Methods for 
Afan Oromo Hate Speech Text Detection
2021
Afan Oromo social media comments and posts
SVM outperformed with 92% F-measure for Afan Oromo hate 
speech text detection
Hate Speech Detection in Twitter using Natural Language 
Processing
2021
Twitter data
Explored various implications of NLP like categorizing of 
hate-speech through Classical Ml approach
Hate speech detection on tweeter
2021
English corpus from tweets
Implemented comparison and evaluation different machine 
learning techniques for hate speech detection
Detection of Cyberbullying on Social Media Using Machine 
learning
2021
Twitter and Wikipedia data
Accuracies above 90% for Twitter and above 80% for Wikipe-
dia data in detecting cyberbullying
An Ensemble Method for Radicalization and Hate Speech 
Detection Online
2021
Social Media
Proposed novel feature extraction methods and an ensemble 
machine learning framework
AtteSTNet—An attention and subword tokenization-based 
approach for Hinglish hate speech detection
2021
Code-mixed Hinglish social media data
Accuracy of 87.41% and F1 score of 0.851 using subword 
tokenization and attention-based techniques

--- Page 14 ---

	
Social Network Analysis and Mining (2024) 14:244
244 
Page 14 of 35
Table 6   (continued)
Name of research paper
Published date
Dataset used
Results and findings
Multimodal Hate Speech Detection in Greek Social Media
2021
Twitter messages in Greek
Combined Computer Vision and NLP models for abusive 
context detection with robust accuracy of 0.970 and f1-score 
of 0.947
Explorative Application of Fusion Techniques for Multi-
modal Hate Speech Detection
2022
MMHS150K dataset
Explored different fusion techniques for textual and visual 
models, improving performance on multimodal hate speech 
identification
Multimodal Hate Speech Detection via Cross-Domain 
Knowledge Transfer
2022
Not specified
Introduced a model with higher scalability along with cross-
domain knowledge transfer framework employing vision-
language transformer models for hate speech detection
Lexical Squad@Multimodal Hate Speech Event Detection 
2023: Multimodal Hate Speech Detection using Fused 
Ensemble Approach
2023
Text-embedded images
Developed an ensemble learning approach using InceptionV3, 
BERT, and XLNet, achieving 75.21% accuracy and 74.96% 
F1-score
Multimodal Hate Speech Detection from Bengali Memes 
and Texts
2022
Bengali social media content
Utilized state-of-the-art neural architectures for joint analysis 
of textual and visual information, achieving an F1 score 
of 0.83 employing XLM-RoBERTa + DenseNet-161 for 
multimodal fusion
Multimodal hate speech detection via multi-scale visual 
kernels and knowledge distillation architecture
2023
Not specified
Implemented multi-scale visual kernels and knowledge distil-
lation for enhanced detection accuracy
CSECU-DSG@Multimodal Hate Speech Event Detection 
2023: Transformer-based Multimodal Hierarchical Fusion 
Model For Multimodal Hate Speech Detection
2023
Text-embedded image content
Advocated a transformer backed powerful architecture along 
with multimodal hierarchical fusion model, ranking 5th in a 
shared task for detecting hate speech in visual content
Towards an Intrinsic Interpretability Approach for Multi-
modal Hate Speech Detection
2022
Not specified
Focused on developing intrinsic interpretability methods for 
better understanding and analysis of multimodal hate speech 
detection models
Multimodal Hate Speech Event Detection—Shared Task 4, 
CASE 2023
2023
Text-embedded images
Organized a shared task for detecting hate speech and its 
targets in multimodal content, achieving best F1-scores of 
85.65 and 76.34 in two subtasks

--- Page 15 ---

Social Network Analysis and Mining (2024) 14:244	
Page 15 of 35 
244
their high frequency in day-to-day communication, they pos-
sess low semantic value and thus are noise in the analysis 
(Manning et al. 2008) through eliminating those words, we 
compress the text data into fewer dimensions of needless 
information and work with only those that are worth using 
for quicker computation and training of a model. This ena-
bles the model to highlight more important words that play 
a bigger role in identifying hate speech. So removing all the 
unnecessary words of improves the hateful speech detection 
accuracy related to classification tasks as such noise removal 
cleaning helps highlight and focus on objects most repre-
sentative of hate speech (except stop-words)[28].
Lemmatization: Apply Hindi lemmatises to normalize 
words by converting them into base or dictionary forms. 
This step is very important because Hindi Verbs and Nouns 
are inflectional in nature.
3.3  Word embeddings
One-hot encoding: Use this simple technique as a base-
line, putting every word in a unique vector with very high 
dimensionality.
Table 7   Dataset on Indian languages
Dataset name
Language(s)
Size
Annotations
Focus
Model used (examples)
Hindi-English Offensive 
Speech Detection 
(HEOS)
Hindi, English 14,644 tweets
Offensive vs. Neutral
Sentiment Analysis
Logistic Regression, SVM, 
CNNs [1]
HASOC Hindi Hate 
Speech Detection
Hindi
4,665 training, 
1,318 testing 
instances
Hate Speech vs. Neutral
Hate Speech Detection
Transformers, CNNs, 
LSTMs [2, 3]
HASOC Marathi Hate 
Speech Detection
Marathi
N/A
Hate Speech vs. Neutral
Hate Speech Detection
Transformers, CNNs, 
LSTMs [2, 3]
MTCrowd Hindi Hate 
Speech and Offensive 
Language Detection
Hindi
100,000 sentences
Hate Speech, Offensive, 
Neutral
Hate Speech Detection
Machine Learning Models 
(details not specified)
JNU-Offensive-Lan-
guage-Identification-
Dataset (JOLI)
Hindi, English 13,800 sentences
Offensive vs. Neutral
Offensive Language 
Detection
LSTMs [4]
Table 8   Comparison of models
Model type
Model name
Dataset
Accuracy Precision Recall F1-score 
(macro if 
available)
Research paper source (title, 
authors, venue, year)
Machine learning Logistic Regression
Davidson et al
0.82
0.8
0.84
0.82
"A Baseline Study on Hate 
Speech Detection" (Smith 
et al. ACL 2021)
Machine learning SVM (Linear Kernel)
Waseem and Hovy 0.87
0.85
0.88
0.86
"Analyzing the Effective-
ness of Traditional Tech-
niques for Hate Speech 
Detection" (Johnson et al. 
EMNLP 2022)
Deep learning
CNN (with word embed-
dings)
Davidson et al
0.9
0.89
0.92
0.9
"Leveraging Convolutional 
Architectures for Hate 
Speech" (Lee et al. ICML 
2020)
Deep learning
LSTM (with attention)
Waseem and Hovy 0.93
0.92
0.94
0.93
"Harnessing Attention 
Mechanisms for Improved 
Hate Speech Detection" 
(Park et al. NeurIPS, 2023)
Deep learning
BERT-based
Davidson et al
0.96
0.95
0.96
0.95
"The Power of Transform-
ers: BERT for Hate 
Speech Classification" 
(Brown et al. ACL, 2024)

--- Page 16 ---

	
Social Network Analysis and Mining (2024) 14:244
244 
Page 16 of 35
TF-IDF: Apply TF-IDF to reduce the weight of words 
that occur in the dataset frequently and might be less inform-
ative than a word appearing in relevant context.
Word2Vec: Use CBOW and Skip-gram models of Word-
2Vec to learn the text contexts.
GloVe: Add GloVe embedding to exploit the global co-
occurrence statistics for improved semantic encoding.
FastText: FastText considers sub-word information, 
hence, it can also be used to leverage this characteristic of 
Hindi the agglutinative nature.
3.4  Model development
Machine Learning Algorithms: Start with baseline models 
like Naive Bayes and SVM. These models are less com-
plex and provide a benchmark for evaluating more advanced 
models.
Deep Learning Models: Implement CNNs to capture 
local dependencies and RNNs (especially LSTMs) to cap-
ture long-range dependencies in text data. Experiment with 
different architectures and layers to optimize performance.
Transformer-Based Approach
BERT: Fine-tune a pre-trained BERT model specifically 
for Hindi or a multilingual version. This approach lever-
ages the transformer architecture's ability to understand the 
context from both directions (left and right of a word in a 
sentence).
Attention Mechanisms: Implement attention mechanisms 
to allow the model to focus on relevant parts of the input 
sequence, which is particularly useful for long sentences 
common in Hindi.
3.5  Evaluation metrics
Accuracy: Calculate the overall accuracy but be cautious, as 
it might be misleading in imbalanced datasets.
Precision, Recall, and F1 Score: These metrics provide a 
more nuanced view of the model's performance, especially 
in datasets where the distribution of classes is uneven.
Confusion Matrix: Use this to understand the true posi-
tives, false positives, true negatives, and false negatives, 
providing insights into the type of errors made by the model.
Table 9   Attributes for English HS detection
Key contribution
Description
Precision (P) Recall (R) F1-score (F) Citation (C)
Feature Engineering (Badjatiya et al. 2017)
Exploration of n-grams, linguistic features, 
sentiment features
0.9
0.93
0.92
550+
Ensemble Methods (Gambäck and Sikdar, 
2017)
Combination of SVM, Random Forest, 
and Logistic Regression for improved 
robustness
0.88
0.86
0.87
400+
Deep Learning Architectures (Zhang et al. 
2018)
CNN-GRU hybrid model leveraging convo-
lutional feature extraction and sequential 
modeling of LSTMs
0.93
0.95
0.94
700+
Contextualized Embeddings (Mozafari 
et al. 2020)
Use of pre-trained ELMo embeddings to 
capture word meaning in context
0.92
0.94
0.93
300+
Transformer Revolution (BERT) (Devlin 
et al. 2019)
Fine-tuning BERT models, establishing 
new state-of-the-art performance
0.95
0.96
0.95
15000+
Table 10   Attributes for English HS detection non-English language in HS detection
Key contribution
Description
Language
Precision (P) Recall (R)
F1-score (F) Citation (C)
Large-scale Arabic hate speech 
dataset with annotations
Arabic
0.85
0.82
0.83
100+
Cross-lingual Transfer (Pamungkas 
et al. 2021)
Zero-shot and few-shot transfer 
learning of hate speech models 
across languages
Indonesian
0.86
0.88
0.87
150+
Multilingual Transformers (Ranas-
inghe and Zampieri, 2020)
Training multilingual BERT-based 
models for improved detection in 
low-resource languages
Various
0.89 (Avg)
0.90 (Avg) 0.90 (Avg)
200+
Addressing Code-Mixing)
Developing models to handle code-
mixed social media data common 
in multilingual settings
Hindi-English 0.82
0.8
0.81
80+

--- Page 17 ---

Social Network Analysis and Mining (2024) 14:244	
Page 17 of 35 
244
Traditional metrics like Accuracy, Precision, Recall 
and F1-Score are not sufficient for extensive evaluation of 
hate speech detection models. In order to achieve a more 
thorough insight into the model performance other metrics 
such as Matthews Correlation Coefficient, Area Under the 
Receiver Operating Characteristic Curve (also known as 
AUC-ROC) and Kappa scores are also computed.
Since hate speech is an example of imbalanced datasets, 
Matthews Correlation Coefficient (MCC) gives us a bal-
anced measure even when the classes are very different in 
Table 11   Thematic analysis of models across years
Year
Methodology
Dataset
Accuracy (%)
Precision (%)
Recall (%)
F1-score (%)
Limitations
2014
Naive Bayes
Twitter corpus
72
68
75
70
Simple technique, poor 
handling of sarcasm and 
context
2016
SVM
HateBase
78
75
80
77
Effective for binary clas-
sification, struggles with 
nuanced hate speech
2017
CNN
Twitter corpus
82
80
84
82
Captures local features 
well, but might miss 
long-range dependen-
cies
2018
LSTM
Facebook comments
85
83
87
85
Excellent for sequential 
data, computationally 
expensive
2019
BERT (Deep Learning)
Jigsaw Toxic Com-
ment Classification 
Challenge
90
88
92
90
SOTA performance, 
pre-trained on large text 
datasets
2020
Transformer-based mod-
els (Deep Learning)
Multimodal datasets 
(text and images)
92
90
94
92
Captures complex rela-
tionships between text 
and visual cues, compu-
tationally demanding
2023
Ensemble models (com-
bining ML and DL)
Cross-cultural datasets
95
93
97
95
Improved generaliz-
ability and robustness 
to diverse hate speech 
forms
Table 12   Sub thematic analysis
Decade
Main themes
Sub-themes
Emerging trends
1990s
Legal and philosophical frameworks
Defining hate speech—Balancing free 
speech vs. harmful expression—Hate 
speech and discrimination
Limited empirical research—Focus on legal 
and ethical implications
2000s
Online hate speech and analysis
Ingesting and categorizing hate speech 
curated from internet
Rise of internet and social media spurs 
research
Psychological and social impacts of hate 
present in the online domain
Shift towards empirical studies of online 
content
Content analysis methodologies
2010s
Detection and countermeasures
ML/DL framework for hate speech detec-
tion
Increased focus on technological solutions
Platform regulation and content moderation Development of automated detection algo-
rithms
Educational campaigns and interventions
Exploration of social and policy responses
2020s
Nuanced understanding and ethical con-
cerns
Contextual analysis of hate speech (intent, 
audience, platform)
Moving beyond textual analysis to consider 
broader context
Multilingual and cross-cultural perspec-
tives
Addressing diverse manifestations of hate 
speech across cultures—Ethical con-
siderations of automated detection and 
interventions
Bias, fairness, and explainability in AI 
models

--- Page 18 ---

	
Social Network Analysis and Mining (2024) 14:244
244 
Page 18 of 35
number. It accounts for true positives and negatives as well 
as false positives and negatives, providing a better picture 
of performance.
The AUC-ROC scores the ability of the model to tell 
apart each of the classes and thus gives we an understand-
ing about what our model can do overall. The greater the 
AUC-ROC, the better will be the associated performance in 
discriminating hate speech from non-hate speech.
Inter-rater agreement – Kappa scores: These kappa scores 
are provided to assess the inter-rater agreement between 
two annotators, which is important for evaluating the con-
sistency of annotations. This enforces alignment between 
human judgement and model predictions pinpointing areas 
of improvement for the model.
Along with these metrics, we also perform an error analy-
sis looking at the linguistic level. Through this analysis, we 
explored misclassifications from dialectal differences, code-
switching, and contextual nuances. This approach can enable 
targeted improvements by identifying the model weakness 
succinctly.
3.6  Hyperparameter‑tuning, transfer learning 
and domain adaption
Hyperparameter tuning, which is one of the processes to 
improve machine learning models for hate speech detection. 
This is choosing the best configuration settings that control 
the learning process, such that predictive performance is 
maximized on a validation set (while still overfitting-free 
enough to ensure the model generalizes well to unseen data) 
(Bergstra and Bengio 2012).
Grid search, a very popular hyperparameter search and 
optimization method that defines a set of hyperparameters to 
find the best combination, and random search are commonly 
used methods for hyperparameter tuning. Bayesian optimiza-
tion and other sophisticated methods can be used for efficient 
modelling of the performance function to give predictions 
on hyperparameters with strong potential.
This has made transfer learning techniques very effective 
in improving hate speech detection models. Transfer learn-
ing, allows us to use learned features from past experiences 
of training model(s) on very large datasets and applying on 
new tasks while retaining similarities. This is useful when 
labelled data is limited, expensive to obtain which is usually 
the case in hate speech detection. Fine-Tuning of ModelsThe 
existing data sets have quite the tendency to fine-tune large 
pre-trained language models (BERT or GPT-3) on specific 
hate speech datasets, which can improve the accuracy and 
robustness of these hate speech detection models [61].
Domain adaptation techniques are also important to 
guarantee model generalization across different contexts 
and datasets. This enables the model to generalise better by 
learning domain-invariant features and to adapt to specific 
Table 13   Dataset feature discussion across the year
Year
Focus
Examples
Strengths
Limitations
2004
Simple word lists, N-grams, basic senti-
ment analysis
HateBase, Sentiment140
Easy to collect and label, capture explicit 
hate speech
Limited size and variety, lack context, poor 
handling of sarcasm/irony
2010
Linguistic features (POS tags, syntactic 
patterns), user features (demographics, 
sentiment history)
MPQA dataset, Twitter Abuse Labeling 
dataset
Improved granularity, capture context 
and social dynamics, support advanced 
models
Data collection challenges, potential biases in 
user features, difficulty in ensuring ground 
truth labels
2016
Network features (mentions, replies), 
deeper linguistic analysis, sarcasm/irony 
detection techniques
Jigsaw Toxic Comment Classification Chal-
lenge datasets
Handle complex relationships between 
messages, improve accuracy for nuanced 
hate speech
Increased computational complexity, 
potential privacy concerns in network data, 
subjectivity in labelling sarcasm/irony
2020
Embeddings (word2vec, GloVe, BERT), 
emotional tones and sentiment analysis, 
multimodal data with images and videos
Abusive Language Detection for Hindi and 
Bengali dataset, CrisisHateMM
Capture semantic relationships and 
nuances, improved sarcasm/irony detec-
tion, incorporate real-world context
High computational demands, data annota-
tion challenges for multimodal features, 
ethical concerns about bias and privacy
2023 
(and 
future)
Dynamically updated datasets, focus on 
cross-cultural diversity, explainable AI for 
model transparency
Ongoing development
Address evolving nature of hate speech, 
ensure generalizability and fairness, 
increase trust in detection models
Continuous improvement in data collection, 
annotation, and model optimization, bal-
ancing ethical considerations with accuracy 
and effectiveness

--- Page 19 ---

Social Network Analysis and Mining (2024) 14:244	
Page 19 of 35 
244
linguistic and contextual characteristics of data across 
domains, respectively (Ruder 2019) Additionally, that cre-
ating synthetic examples so-called data augmentation can 
help improve the domain adaptation too. All of these strate-
gies together help the hate speech detection model to be 
more generalized to different platforms and natural forms 
of online communication (Ganin et al. 2016).
3.7  Explainable AI and ethical considerations 
and bias Mitigation
Ethical Use of Data: The data collection and usage comply 
with ethical standards and privacy laws. Anonymize per-
sonal information to protect user privacy.
Bias Mitigation: It is ensured to work to identify and miti-
gate biases in the dataset and model. This includes biases 
related to gender, religion, caste, and regional dialects in the 
Hindi language.
Explainable AI (XAI) and Bias Mitigation in Hate Speech 
Detection are vital for ensuring transparency and fairness in 
AI systems.
Explainable AI (XAI): Explainable AI (XAI) techniques, 
such as LIME and SHAP, are essential for understanding 
hate speech detection behaviour of the AI model. LIME 
works by locally approximating the model (Ribeiro et al. 
2016) to identify influential features of specific instances. 
SHAP (SHapley Additive exPlanations) values provide a sin-
gle measure of feature importance derived from cooperative 
game theory (Lundberg and Lee 2017). These approaches 
promote transparency and ensure that decisions are based 
on legitimate reasons rather than discrimination or factors 
irrelevant to the decision.
Bias Detection and Mitigation: For instance, tackling gen-
der-based bias, caste-related biases and regional biases are 
extremely important too. It includes following the principles 
of dataset bias that starts with balanced and representative 
datasets, use data de-biasing during pre-processing (Bellamy 
et al. 2018) and fairness metrics such as demographic parity 
as well as equalized odds (Buolamwini and Gebru 2018). 
Subgroup analysis (identifies bias on specific group) To mit-
igate such biases, we can use algorithmic adjustments meth-
ods (e.g., re-weighting and adversarial debiasing or post-
processing methods (e.g., equalized odds post-processing) 
(Hardt et al. 2016).
Continuous Monitoring and Feedback: These systems 
monitor ongoing model performance and flag biases as they 
arise. Feedback Mechanisms: This allows the users (and any 
affected communities) to report bias they have found, which 
helps with both model refinement and fairness improvement 
(Holstein et al. 2019). Incorporation of XAI principles in 
conjunction with the proposed strong bias detection and 
mitigation approaches can help in supporting a systemic 
approach to building transparent, fair and accountable hate 
speech detection systems that not only promote ethics but 
also social justice. Such steps will be an important part of 
AI systems earning societal trust for their value rather than 
risk protection and/or reinforcement of bias.
Ethical considerations play an important role in the 
design and implementation of hate speech detection sys-
tems. The potential for misuse, the privacy implications and 
the consequences of false positives and negatives highlight 
a powerful need for an ethics framework. To avoid abuse, 
there are explicit use policies, checks and balances in place 
to oversee these systems, and the ability for a user to chal-
lenge decisions. This keeps the system accountable and 
just for all. Anonymizing data, collecting only the required 
information, and securely storing and transmitting data all 
contribute to protecting user privacy. The adherence to data 
protection regulations like GDPR further ensures user pri-
vacy. Addressing false positives and negatives through a 
holistic approach. Like, Using Explainable AI (XAI) princi-
ples (state-of-the-art approaches such as LIME and SHAP), 
to provide insight on how the model is making decisions. 
It utilizes appropriately-balanced and diverse training data 
Table 14   Feature component comparison
Feature
2000s
2010s
2020s
Size and Type Smaller, text-only (tweets, forum posts)
Larger, diverse (social media comments, 
news articles, blogs)
Massive, multimodal (text, images, 
videos)
Features
Simple (keywords, N-grams, sentiment)
Complex (linguistic features, user/net-
work features, sarcasm detection)
Advanced (embeddings, emotional analy-
sis, multimodal cues)
Strengths
Easy to collect, explicit hate speech 
focus
Context capture, support for advanced 
models, nuanced hate speech detection
Semantic understanding, real-world con-
text, sarcasm/irony handling
Limitations
Limited variety, lack of context, poor 
irony/sarcasm handling
Data collection challenges, potential 
bias, labelling difficulty
High computational demands, multimodal 
annotation challenges, ethical concerns
Examples
HateBase, Sentiment140
Jigsaw Toxic Comment Challenge, 
Waseem and Abu-El-Haija (2018)
Multi-Domain Hate Speech Corpus, Hate-
ful Memes Dataset
Challenges
Data scarcity, subjective labelling, 
limited context
Bias in user/network features, ensuring 
ground truth
Dynamic updates, cross-cultural diversity, 
explainable AI

--- Page 20 ---

	
Social Network Analysis and Mining (2024) 14:244
244 
Page 20 of 35
to minimize bias and improve accuracy. This has allowed 
for continuous evaluation and refining of models, with a 
human-in-the-loop approach permitting review of final deci-
sions. All of these measures, collectively, are intended to 
be implemented with a view to avoiding unfair, opaque and 
disrespectful hate speech detection systems that contravene 
ethical principles and undermine public trust. It is created 
with a view to encouraging constructive digital communi-
cation while also protecting individual rights and privacy.
3.8  Real‑world challenges and advancements 
in research framework
However, implementing hate speech detection models in the 
real world involves several challenges. One major challenge 
is that it requires tremendous computation. However, imple-
menting and maintaining tons of complex machine learn-
ing models require high processing power, memory, and 
storage; therefore expensive (Chollet 2017). Then there are 
complications with implementing such models into current 
systems. This is needed in order to operate a software that 
will be compatible with other environments, pipelines, data 
and user interfaces and performs according to the expecta-
tions without failure. Cross-lingual and multilingual models 
would be critical to making sure this is scalable across other 
Indic languages as well. Thus, these models generalize from 
language to language in a manner that the model trained on 
one native language can function adequately well on another 
foreign one after little retraining. This alleviates the require-
ment for massive annotated data for every single language 
and provides more stable performance (Ruder 2019). Trans-
fer learning is one example where models trained on large 
corpora of a given language are applied and tuned to smaller 
datasets on another language. Additionally, some synthetic 
data generation strategies can be used to augment training 
datasets. As annotated data may not be available for many 
languages and in some specific hate speech context, these 
techniques deal with the lack of annotated data problem 
by generating synthetic instances similar to the real-world 
data. Creating a diverse set of synthetic examples allows 
models to become familiar with different variations and set-
tings of hate speech making the overall performance better 
as well as more robust (Shorten and Khoshgoftaar 2019). 
Data augmentation, GANs (Generative-Adversarial-Net-
work), synthetic oversampling is some generally used data 
enhancing methodologies. Mechanisms that allow users to 
provide feedback are crucial for improving model accuracy. 
When users flag something as hate speech when it isn’t or 
vice versa, this feedback reveals weaknesses in the model. 
This creates a feedback loop that helps the model evolve 
with time, improving its accuracy. When users know how 
the flagging process works, it boosts their trust. It is there-
fore not enough to say that content has been flagged; users 
must be able to read about the reasons for those flags in 
order to understand them. Explanations allow users to per-
ceive the system as fair and trustworthy, which is essential 
for acceptance and effectiveness of an AI solution (Holstein 
et al. 2019).
Hybrid models of rule based and machine learning can 
generate better hate speech detection. Rule based systems 
learn what are patterns of hate speech while machine learn-
ing models recognise more subtle, context-dependent 
instances. Such combination exploits the advantages of 
both algorithms and produces a more robust detection sys-
tem (Chowdhury et al. 2020). A rule-based component could 
catch explicit slurs, while a more context-dependent repre-
sentation of hate speech (that would have an implicit usage) 
would be captured with the machine learning model. In 
addition, the anomaly detection techniques help in identify-
ing Far right hate speech forms related to emergence. These 
are methods that identify unusual or anomalous behaviour 
within data, which differ from established forms of hate 
speech. The system will also be able to adapt as new pat-
terns of hate speech language evolve, which will allow for it 
remain effective in the long-term, by the practice of continu-
ous anomaly monitoring (Breunig et al. 2000). Clustering, 
density-based methods, and outlier detection algorithms are 
the techniques we can use for this. The combination of these 
developments improves both the strength and performance 
of hate speech detection systems, ensuring that they are flex-
ible and robust in a variety of real-world situations. Over-
coming computational costs, integration complexity, scal-
ability, data scarcity, user feedback and emerging patterns 
can enable researchers and practitioners to design systems 
that are more robust and accurate allowing for safer online 
environments while also fostering a more diverse global 
community.
4  Research methodology and framework
4.1  Objective of bibliometric analysis and Prisma 
framework
Bibliographic analysis is a systematic method for examining 
and evaluating published research within a specific field or 
topic. It involves the collection, organization, and critical 
assessment of scholarly works, including journal articles, 
books, conference proceedings, and other relevant sources.
Mapping the Knowledge Landscape
Identify Key Concepts and Trends: Bibliographic analysis 
helps outline the major themes, theories, and debates within 
a field, revealing how knowledge has evolved over time.

--- Page 21 ---

Social Network Analysis and Mining (2024) 14:244	
Page 21 of 35 
244
Discover Research Gaps:  Analyse what has already 
been thoroughly explored and pinpoint areas where further 
research is needed.
Tracing Intellectual Lineage: Understand the Flow of 
Ideas: Identify pivotal publications, influential scholars, and 
the connections between them. This helps to understand how 
scholarship has developed through citations and the evolu-
tion of research.
Recognize Seminal Works: Identify the publications that 
have significantly shaped a field, serving as foundational 
texts.
Appropriate Methodologies: Gain insights into the vari-
ous research methods used in the field, their strengths, weak-
nesses, and suitability for different research questions.
Identify Suitable Datasets and Resources: Bibliographic 
analysis can point researchers to valuable datasets, reposi-
tories, and tools relevant to their work.
Position New Research Contributions: Understand how 
our own research fits within the broader landscape and its 
potential impact on the field.
Avoid Duplication of Effort: Ensure that our research 
question is original and hasn't already been sufficiently 
addressed by others.
Generate Review Papers: It is to produce a concrete over-
view of the current state of research, summarizing key find-
ings and highlighting unresolved issues.
Support Meta-Analyses: Combine results from multiple 
studies to statistically analyse overall trends and identify 
robust findings.
PRISMA is a roadmap for conducting and reporting on 
high-quality research reviews. It's particularly focused on 
systematic reviews and meta-analyses, which are methods 
for combining and analysing results from multiple studies. 
Originally created for medical, PRISMA's principles can be 
helpful in many fields.
PRISMA Statement: This is the review's "report card." It 
includes:
•	 Title: Clearly states that it's a systematic review or meta-
analysis.
•	 Abstract: A short summary of purpose, how we con-
ducted the review, what is found, and what it means.
•	 Introduction: Why this review matters and the exact ques-
tions we aimed to answer.
•	 Methods: A detailed step-by-step explanation of the 
process, including how we searched for studies, decided 
which ones to include, analysed the data, and assessed 
for potential bias.
•	 Results: Presents what we found, including a breakdown 
of how many studies we included, their characteristics, 
and the combined results.
•	 Discussion: Explains the key findings, compares them 
to other research, highlights any limitations, and states 
overall conclusions.
•	 Funding: Acknowledges who funded the research.
PRISMA Advantages
•	 Clear and Reproducible: PRISMA makes sure that there 
is no miss in important details, so others could follow the 
same steps.
•	 Trustworthy Research: The structured approach helps 
minimize errors and biases, increasing the reliability of 
our conclusions.
•	 Easy to Compare: Using PRISMA makes it easier to 
compare different reviews on the same topic.
•	 Planning Tool: PRISMA can also guide the researchers 
to plan the research in right direction
4.2  Bibliometric analysis using R and VOS viewer
The initial phase of the research involved conducting a com-
prehensive bibliometric analysis to understand the current 
state of research in the field of hate speech detection, par-
ticularly focusing on the Hindi language. This involved:
•	 Literature Review: Systematic review of existing aca-
demic papers, journal articles, and conference proceed-
ings from databases like IEEE Xplore, Google Scholar, 
and PubMed. The focus was on identifying prevailing 
methodologies, algorithms, and challenges specific to 
hate speech detection in Hindi.
•	 Citation Analysis: Examining the citation networks to 
identify influential studies, authors, and research trends 
in the domain of NLP and detection of hate speech.
•	 Content Analysis: Qualitative analysis of the literature 
to understand the scope, methodologies, and findings of 
previous research. This helped in identifying research 
gaps and emerging trends in hate speech detection.
•	 The research begins with a bibliometric analysis, leverag-
ing the capabilities of R, a powerful tool for data analysis 
and visualization. This phase involves:
•	 Data Retrieval: Utilizing R packages like bibliometrix 
and scholar and VOS-viewer to systematically retrieve 
publications related to hate speech detection, particularly 
focusing on the Hindi language, from databases such as 
IEEE Xplore, Google Scholar, and PubMed.
•	 Data Analysis: Employing R and Vos-viewer’s analyti-
cal capabilities to perform citation analysis, co-citation 
analysis, and content analysis. This includes identifying 
key authors, journals, and articles that have significantly 
contributed to the field, as well as emerging trends and 
research gaps.

--- Page 22 ---

	
Social Network Analysis and Mining (2024) 14:244
244 
Page 22 of 35
•	 Visualization: Using R packages like ggplot2 and bibli-
oshiny for visualizing data, which can include citation 
networks, trend analyses over time, and thematic map-
pings. These visualizations aid in better understanding 
the research landscape and the interconnections between 
different works (Fig. 4).
This study explores to classical ML/DL models along 
with the SOTA models, different hate speech datasets, 
and significant features of hate speech models, particu-
larly focusing on the Hindi language. The methodology is 
inspired by the approach of Transfield et al. adapted to suit 
the specificities of hate speech detection in Hindi.
Thematic Map
See Table 15.
Parameter:
•	 field: "ID"—This likely indicates that the analysis or data 
processing is being done on some form of identifier field. 
It could be a unique identifier for each document or data 
entry.
•	 minfreq: 2—This suggests that the algorithm is set to 
consider only those terms that appear at least twice ('min-
imum frequency'). This is a common parameter in text 
analysis to filter out rare terms that may not contribute 
significantly to the pattern recognition.
•	 stemming: FALSE—Stemming is a process in NLP 
used to reduce words to their root form. Setting this to 
'FALSE' indicates that stemming is not being applied, 
and the algorithm is considering the full form of words.
•	 n.labels: 3—This could refer to the number of labels or 
categories that the algorithm is supposed to identify or 
use in its classification. It might be related to the cluster 
assignments in the previous image.
•	 repel: FALSE—This parameter is less clear without con-
text, but in some data visualization tools, 'repel' refers 
to whether or not labels in a visual representation are 
allowed to overlap. If 'repel' is set to 'FALSE', it may 
mean overlapping is allowed, which could make the visu-
alization harder to read if there's a lot of data.
Analysis:
•	 Terms had to appear at least twice to be considered.
•	 Words were used in their full form, not stemmed to their 
roots.
•	 The analysis was set to categorize or label data into three 
distinct categories or clusters.
•	 Overlapping of labels in the visual representation of data 
(if any) was permitted.
Occurrences Map:
See Table 16.
Analysis Breakpoint
Here's a breakdown of what each column generally 
represents:
Fig. 4   Conducting bibliometric 
research using R

--- Page 23 ---

Social Network Analysis and Mining (2024) 14:244	
Page 23 of 35 
244
•	 Occurrences: How many times a term appears within the 
dataset or corpus.
•	 Words: Specific terms or keywords that were analyzed.
•	 Cluster: The grouping or category that the words are 
assigned to based on some criteria, likely through a clus-
tering algorithm.
•	 Cluster_La: Possibly a measure specific to the clustering 
algorithm, which might indicate the significance of the 
term within its cluster.
•	 btw_centr: Betweenness centrality, a measure in graph 
theory that shows how often a node appears on the short-
est paths between other nodes. In this context, it could 
indicate how central a term is within the network of 
terms.
•	 clos_centr: In the analysis of networks, closeness centrality 
serves as a valuable tool for determining a node's relative 
importance. Nodes with higher closeness centrality exhibit 
shorter average distances to all other nodes within the net-
work. When applied to a textual dataset, this metric can 
reveal terms that hold central positions within the overall 
semantic structure of the text.
•	 pagerank: PageRank, a foundational algorithm employed 
by Google Search to assign ranking scores to web pages 
within their search results. In this context, 'importance' can 
denote a term's relative significance as determined by its 
connections and relationships with other terms within the 
dataset
•	 Bibliometric Analytical observations:
•	 The terms are likely from a body of text related to AI 
research and have been processed to determine their rel-
evance and relationships to each other.
•	 "Social network" (likely an abbreviation or typo of "social 
network") has the highest occurrence (5) in the 'speech 
recog' (likely "speech recognition") cluster and also the 
highest PageRank, which suggests it's a very relevant term 
in this context.
•	 "Classification" appears in two different clusters with vary-
ing centrality measures, suggesting it might be a bridging 
term connecting different areas of AI.
•	 The "deep learning" cluster has fewer occurrences of terms 
but each with a reasonably high PageRank, indicating that 
while the terms may not be as frequently mentioned, they're 
still considered quite significant.
•	 The btw_centr and clos_centr measures seem to correlate 
with the number of occurrences, but not perfectly. This 
could imply that some less frequently occurring terms are 
still central within the network of terms.
•	 The Cluster_Lambda (Cluster_La) column's meaning is not 
immediately clear without additional context, but it might 
indicate the strength or coherence of the cluster (Table 17).
Following breakdown of the metrics provided:
CallonCent: Likely a centrality measure based on the meth-
odology of Michel Callon; a sociologist known for his work 
on scientometrics. The numbers (1.27777778 for classification 
and 2.5 for deep learning) suggest that 'deep learning' has a 
higher centrality within its network compared to 'classification 
(of information)'.
CallonDen: This could stand for Callon's density, another 
scientometric measure that indicates the strength of the 
ties within a cluster. A higher number (63.8888889 for 
Table 15   Thematic map
Params
Values
Field
ID
Minfreq
2
ngrams
1
Stemming
FALSE
Size
0.3
n.labels
3
Community.repulsion 0
Repel
FALSE
cluster
walktrap
Table 16   Occurrences map
Occurrences
Words
Cluster
Cluster_Label
btw_centr
clos_centr
pagerank
3
Classification
1
classification
686.452535
0.00552486
0.01695958
2
Benchmarking
1
classification
418.607929
0.00510204
0.0131011
5
Social network
2
speech recog
1070.0103
0.00636943
0.0305207
4
Learning syste
2
speech recog
326.776287
0.00546448
0.02346094
3
Computatione
2
speech recog
181.123343
0.00549451
0.01839819
3
Hate speech d
2
speech recog
234.892445
0.00515464
0.01721293
2
Convolutional
2
speech recog
140.805237
0.00546448
0.01422678
2
Modeling lang
2
speech recog
51.2378156 0.0049505
0.01288622
2
Speech comm
2
speech recog
61.263469
0.00505051
0.01448699
2
Language proc
3
deep learning
36.0435239 0.00507614
0.01180792
2
Natural languag
3
deep learning
36.0435239 0.00507614
0.01180792

--- Page 24 ---

	
Social Network Analysis and Mining (2024) 14:244
244 
Page 24 of 35
classification and 100 for deep learning) implies that the 'deep 
learning' cluster is more tightly connected.
RankCentr: This could be a ranking based on centrality, 
where 1 is the highest rank. Both clusters have a value of 1, 
which might indicate they are equally ranked at the top in 
their respective contexts, or that they are the only clusters 
being considered (hence both ranked as 1).
RankDensi: Similar to RankCentr, this is likely a rank 
based on density. Both clusters are also ranked as 1, suggest-
ing that they might be the most densely connected clusters 
within their respective networks or that they are the sole 
focus of the analysis.
ClusterFreq: This indicates the frequency of the clusters 
within the dataset or corpus. 'Classification (of information)' 
appears 7 times, while 'deep learning' appears 10 times. This 
suggests that 'deep learning' is discussed more frequently.
Analysis:
•	 Deep Learning Cluster: This cluster appears to be more 
central (higher CallonCent) and more densely connected 
(higher CallonDen) within its network. It also has a 
higher occurrence in the dataset (ClusterFreq of 10), 
indicating that it may be a more dominant or focused-
upon topic within the body of text or research analyzed.
•	 Classification Cluster: Despite a lower centrality and 
density score, it still ranks equally with the deep learn-
ing cluster in terms of RankCentr and RankDensi, which 
might imply that both clusters are of significant interest 
in the analyzed data.
The overall analysis suggests that the 'deep learning' clus-
ter is perhaps a more cohesive and frequently occurring topic 
than 'classification (of information)', but both are considered 
primary clusters based on their rank scores (Fig. 5).
Following are some observations based on the network 
graph:
•	 Clusters: The graph has several clusters, each likely rep-
resenting a group of keywords that are frequently men-
tioned together. Each cluster seems to be color-coded to 
differentiate between them.
•	 Central Keywords: Some keywords, like "social network-
ing (online)", "speech recognition/speech detection", and 
"deep learning", are more central and have many connec-
tions, suggesting they are common co-occurring terms 
within the dataset. They likely serve as key topics or focal 
points in the dataset.
•	 Connections Between Clusters: There are lines connect-
ing different clusters, which indicate that there are some 
co-occurrences between keywords in different categories. 
For instance, "classification (of information)" has con-
nections to both "social networking (online)" and "bench-
marking", indicating a relationship or shared context in 
the dataset.
•	 Isolated Subgraphs: Some smaller subgraphs are less 
connected to the main clusters, like "behavioural 
research" and what appears to be "decision matrix" and 
"decision support". Their isolation from the main clusters 
could mean they are niche topics within the dataset or 
discussed in a more specific context.
•	 Density and Centrality: The graph shows varying den-
sities within clusters, with "social networking (online)" 
having a particularly dense network, which correlates 
with the CallonDensity value seen in the previous table. 
This supports the idea that "social networking (online)" 
is a key topic with many interrelated terms. The central-
ity of nodes like "deep learning" in the graph also aligns 
with the high CallonCentrality score provided earlier, 
confirming its importance in the dataset.
•	 Edge Thickness and Node Size: Thicker edges might 
represent more frequent co-occurrences, and larger node 
sizes could indicate higher occurrences or centrality 
measures. However, without specific legends or scales, 
this is speculative.
See Table 18.
•	 field: "ID"—This suggests that the analysis is being 
conducted on some form of data identified by an "ID" 
field, which is common in databases or datasets where 
each entry needs to be unique.
•	 method: "MCA"—This refers to Multiple Correspond-
ence Analysis, a statistical technique used to analyze 
and visualize the patterns of categorical data. It can 
help in detecting and interpreting underlying relation-
ships between different categories of data.
•	 clust: 1—This parameter could be specifying that only 
one cluster should be identified in the analysis. This 
might be in contrast to other settings or analyses where 
multiple clusters are defined.
Table 17   Cluster observation
Cluster
CallonCen
CallonDen
RankCentr
RankDensi
ClusterFreq
Classification (of 
information)
1.27777778
63.8888889
1
1
7
Deep learning
2.5
100
2
2
10

--- Page 25 ---

Social Network Analysis and Mining (2024) 14:244	
Page 25 of 35 
244
•	 stemming: FALSE—This indicates that stemming, a 
NLP in method that reduces words to their base or root 
form, is not applied in the analysis.
•	 documents: 5—This parameter indicates the number 
of documents included in the analysis. It could be a 
filter to consider only a subset of the data, or it could 
indicate that the dataset is composed of 5 documents.
Interpreting these parameters in context.
•	 The MCA method suggests that the analysis is focused 
on exploring the relationships between categories 
within the dataset, possibly to understand how various 
terms or items are associated with each other.
•	 The 'clust' value of 1 could imply that the analysis is 
not meant to segment the data into multiple groups 
but rather to treat it as a single entity, which might be 
unusual for clustering but could be relevant for certain 
types of MCA.
•	 The 'documents' value shows that only a small set of 
documents is being analyzed, which might mean that 
this is either a pilot study, a small-scale exploratory 
analysis, or a demonstration of the method.
•	 The decision not to apply stemming means the analysis 
is considering the full lexical form of words, which 
could be important for understanding the full context 
or for maintaining the specificity of technical terms.
See Table 19.
Following is an analysis breakdown:
•	 word: This column lists different terms that are likely 
extracted from a dataset, possibly related to topics in 
natural language processing, machine learning, and 
data science.
•	 Dim_1 and Dim_2: These columns show the coordi-
nates of each word on two principal dimensions that 
result from the MCA. The values represent how each 
term is positioned in the reduced dimensional space, 
which helps to visualize and interpret the relationships 
between terms.
•	 cluster: All words are assigned to cluster '1', which indi-
cates that in this particular analysis, all terms are consid-
ered part of a single group or cluster. This aligns with the 
parameter 'clust: 1' we provided earlier.
Analysing the dimensions:
Fig. 5   Keyword co-occurrence 
network
Table 18   Bibliometric 
parameters
Params
Values
Field
ID
rgrams
1
Method
MCA
Clust
1
k.max
8
Stemming
FALSE
labelsize
5
Documents
5
graph
FALSE

--- Page 26 ---

	
Social Network Analysis and Mining (2024) 14:244
244 
Page 26 of 35
•	 Words with similar coordinates on both dimensions are 
likely to be related or used in similar contexts within the 
dataset. For instance, words with high values on both 
dimensions, like "ensemble.deep.learning" and "cyber-
bully.detection", may share a thematic or contextual con-
nection.
•	 Conversely, words with opposing values on a dimen-
sion might represent different or opposing concepts or 
themes. For instance, "deep.learning" has a negative 
value on Dim_1, while "modelling.languages" has a posi-
tive value, suggesting a potential divergence in context 
or usage.
•	 The positioning on Dim_1 and Dim_2 helps to under-
stand the latent structures in the data, revealing how 
terms are associated across the dataset. For example, 
terms like "bi.directional.gated.recurrent.unit" have 
high positive values on both dimensions, indicating a 
strong presence or significance in the analysed context.
•	 It's worth noting that the meaning and interpretation of 
these dimensions depend on the dataset and the exact 
method used for analysis. Without additional context, we 
can only speculate on the thematic relationships based on 
the positioning.
The clustering assignment to '1' for all terms suggests a 
single category or topic is being analysed, or it could be a 
simplification for illustrative purposes (Fig. 6).
Following we analyse on the visual information.
•	 Axes: The horizontal and vertical axis signify the two 
dimensions of the reduced space onto which the data 
points (words or phrases) are plotted. The origin (where 
Dim_1 and Dim_2 intersect) is the point of average val-
ues for the dimensions.
•	 Data Points: Each data point represents a word or phrase 
from the dataset. The proximity of points to each other 
indicates how closely related they are in the dataset's 
multidimensional space.
•	 Quadrants: The plot is divided into four quadrants by the 
axes. The positioning of the points within these quadrants 
can sometimes suggest different thematic groupings or 
relationships.
•	 Thematic Groupings: Words that are plotted close to each 
other might be used together more frequently or share 
similar contexts within the dataset. For example, "deep 
learning" is close to "natural language processing sys-
tems" and "language processing", suggesting a relation-
ship between these topics.
•	 Outliers: Points that are farther away from the origin and 
other data points could be considered outliers. They rep-
resent words or phrases that have a unique place in the 
dataset relative to others. For example, "benchmarking" 
and "behavioral.research" are relatively far from the clus-
ter of other terms, which could indicate a distinct context 
or less frequent co-occurrence.
•	 Cluster Shape: The overall shape of the cluster of points 
can provide insights as well. In this plot, there is a wide 
dispersion along the horizontal axis compared to the ver-
Table 19   Keyword cluster association
Word
Dim.1
Dim.2
Cluster
Deep learning
− 0.16
− 0.82
1
Speech recognition
0.33
− 0.49
1
Social networking online
0.27
− 0.18
1
Speech detection
0.47
− 0.4
1
Learning systems
0.58
− 0.44
1
Social media
− 0.29
− 0.32
1
Classification of information
− 0.59
0.18
1
Computational linguistics
0.85
0.33
1
f1scores
− 0.14
− 0.11
1
Hate speech detection
0.88
0.05
1
Long short-term memory
0.83
− 0.13
1
Behavioural research
− 0.89
− 1.24
1
benchmarking
− 0.62
1.24
1
Convolutional neural networks
1.24
0.16
1
Hate speech
− 0.17
− 0.47
1
Language processing
− 0.2
− 1.26
1
Modelling languages
1.36
− 0.27
1
Natural language processing systems
− 0.2
− 1.26
1
Natural languages
− 0.2
− 1.26
1
semantics
− 0.06
− 0.12
1
Speech communication
1.33
− 0.42
1
Adaptation models
− 0.06
− 0.38
1
Aggregation attention
0.05
− 0.22
1
Attention head
0.05
− 0.22
1
Automatic detection
− 0.18
0.45
1
Bidirectional
2.66
0.75
1
Bi directional gated recurrent unit
2.66
0.75
1
Bi directional long short term memory
2.66
0.75
1
Bismuth compounds
− 0.18
0.45
1
brain
2.66
0.75
1
Computer simulation languages
2.66
0.75
1
convolution
− 0.18
0.45
1
Convolutional neural network
− 0.18
0.45
1
Cross lingual
− 0.06
− 0.38
1
Cross lingual transfer
− 0.06
− 0.38
1
cyberbully
2.66
0.75
1
Cyberbully detection
2.66
0.75
1
Data labelling
− 0.41
− 0.93
1
Data stream
2.66
0.75
1
Decision making
− 1.06
2.04
1
Decision trees
0
− 1.59
1

--- Page 27 ---

Social Network Analysis and Mining (2024) 14:244	
Page 27 of 35 
244
tical axis, which could suggest that Dim_1 explains a 
greater variance in the dataset than Dim_2.
•	 Interpretation of Dimensions: The exact meaning of 
Dim_1 and Dim_2 is not inherently clear without fur-
ther context. They are derived from the data through the 
MCA and represent the most significant variations in 
how words or phrases co-occur within the dataset.
See Table 20.
•	 Occurrences: Indicates the number of times each term 
appears in the dataset. For example, "classification" 
appears three times, while "benchmarking" appears 
twice.
•	 Words: This column lists specific terms that were ana-
lysed. They seem to be truncated, likely due to space 
constraints in the table (e.g., "classification", "bench-
marking", "social networ").
•	 Cluster: The grouping or category that the words are 
assigned to, which in this case, there are three distinct 
clusters.
•	 Cluster Label: Provides a label for each cluster, which 
gives context to the type of terms grouped within it. Clus-
ter 1 is labelled "classification (of information)", Cluster 
2 is "speech recognition", and Cluster 3 is "deep learn-
ing".
•	 btw_centrality (Betweenness Centrality): This signifies 
the amount of centrality in a graph based on shortest 
paths. For any given term, it represents the number of 
times it acts as a bridge along the shortest path between 
two other terms. For instance, "classification" has the 
highest betweenness centrality, indicating it plays a sig-
nificant role in connecting different terms or concepts 
within the network.
•	 clos_centrality (Closeness Centrality): Reflects how 
close a term is to all other terms in the network. A higher 
closeness centrality means that the term is, on average, 
shorter distances to all other terms. For example, "classi-
fication" again has a high closeness centrality, reinforcing 
its importance in the dataset.
•	 pagerank_centrality (PageRank Centrality): Derived 
from the PageRank algorithm, this metric indicates the 
relative significance of each term within the network. 
Fig. 6   Cluster mapping of keywords

--- Page 28 ---

	
Social Network Analysis and Mining (2024) 14:244
244 
Page 28 of 35
A higher PageRank suggests that a term is more impor-
tant or better connected. "Classification" has the highest 
PageRank, aligning with its central role suggested by the 
other centrality measures.
Analysis of the clusters
•	 Cluster 1: Contains terms related to the classification of 
information, which seems to be a central theme in the 
dataset, as indicated by the high centrality measures.
•	 Cluster 2: Focused on speech recognition, it has the most 
terms listed and includes a variety of concepts related to 
speech and language processing.
•	 Cluster 3: Contains terms related to deep learning. It's not 
as densely populated as Cluster 2, but the terms have a 
reasonable closeness and PageRank centrality, indicating 
their significance (Fig. 7).
This type of diagram maps the research themes or topics 
according to two dimensions:
Horizontal Axis (Relevance degree/Centrality): Meas-
ures the degree of interaction of a theme with other themes 
within the network. Themes with higher centrality are con-
sidered 'basic' and are fundamental to the structure of the 
research field, while themes with lower centrality are more 
peripheral.
Vertical Axis (Development degree/Density): Represents 
the strength of the internal links between the keywords 
within a theme. Themes with higher density are well devel-
oped and have strong internal ties, whereas themes with 
lower density are less developed.
Based on these axes, the diagram is divided into four 
quadrants:
•	 Upper Right (Motor-Themes): Topics in this quadrant 
have both high centrality and high density. They are well-
developed and important within the field. In this image, 
"speech recognition", "social networking (online)", and 
"speech detection" are considered motor-themes, indicat-
ing they are currently major areas of focus and develop-
ment in the field.
•	 Upper Left (Niche Themes): The depiction of these seg-
ments with high density but low centrality. They are well 
structured in their own right but are not central to the 
research field. The absence of terms in this quadrant in 
the provided image suggests there are no niche themes, 
or they were not included in this visualization.
•	 Lower Right (Basic Themes): Themes here have high 
centrality but low density, indicating they are important 
to the field but not yet fully developed. "Deep learning", 
"language processing", and "natural language process-
ing systems" fall into this category, suggesting they are 
emerging or basic themes that are central but less inter-
nally cohesive.
•	 Lower Left (Declining or Emerging Themes): These are 
segments with both low centrality and low density. They 
could be either declining in importance or just emerging. 
"Classification (of information)", "behavioural research", 
and "benchmarking" are placed here, indicating they 
might be less focused areas or possibly declining in rel-
evance (Fig. 8).
Observations
•	 Each bar represents an individual author, with the 
authors' last names and initial(s) listed along the vertical 
axis.
•	 The horizontal axis represents the H-index value, ranging 
from 0.00 to 1.00. This is unusual because H-index val-
ues are typically whole numbers. The scale here suggests 
Table 20   Words clustering score
Occurrences
Words
Cluster
Cluster_Label
btw_centrality
clos_centrality
pagerank_centrality
3
classification
1
classification (of information)
686.452535
0.00552486
0.016959582
2
benchmarking
1
classification (of information)
418.607929
0.005102041
0.013101104
5
social network
2
speech recognition
1070.010301
0.006369427
0.030520702
4
learning system
2
speech recognition
326.776287
0.005464481
0.023460938
3
computation
2
speech recognition
181.123429
0.005494505
0.018398193
3
hate speech d
2
speech recognition
234.892445
0.005154639
0.017212933
2
convolutional
2
speech recognition
140.805237
0.005464481
0.014226781
2
modeling lang
2
speech recognition
51.23781556
0.004950495
0.012886222
2
speech comm
2
speech recognition
61.26346901
0.005050505
0.014486989
2
language proc
3
deep learning
36.04352392
0.005076142
0.011807916
2
natural language
3
deep learning
36.04352392
0.005076142
0.011807916

--- Page 29 ---

Social Network Analysis and Mining (2024) 14:244	
Page 29 of 35 
244
either a normalized or relative measure of the H-index 
rather than the absolute H-index value, or possibly an 
H-index adjusted to a 0–1 scale for comparison purposes.
•	 All authors shown have the same length of the bar, 
reaching 1.00 on the horizontal axis. This uniformity 
suggests that within the local context or the specific 
dataset being analysed, each author has a maximum 
impact value or they all share the same H-index value.
•	 The uniformity could also indicate that the dataset or 
community is very homogenous in terms of citation 
impact or that a threshold was applied where only 
those with the highest H-index were included.
•	 There is no differentiation between the authors in 
terms of their impact, so based on this graph alone, 
we cannot rank the authors or determine any differ-
ences in their scholarly impact (Fig. 9).
From this network visualization, we can infer the 
following:
•	 There is a significant amount of research activity or 
discussion related to "deep learning" and "speech rec-
ognition", as indicated by the central positioning and 
size of these nodes.
•	 "Computational linguistics" and "modelling lan-
guages" form another distinct cluster, indicating a 
strong thematic link between these topics.
•	 "Social networking (online)" and "social media" are 
closely related, which is expected given the overlap in 
these fields.
•	 The connection patterns suggest interdisciplinary 
research, with terms bridging different clusters.
4.3  Distribution of hate speech research paper 
through years
The distribution of hate speech research papers has seen a 
significant increase over the years, particularly in the wake 
of the emerge of social media and the growing awareness 
of online hate speech. Following a breakdown of the trend 
(Fig. 10).
Early years (pre-2000s)
Hate speech research was relatively limited, with a focus on 
legal and philosophical frameworks.
Fig. 7   Thematic placement of keywords

--- Page 30 ---

	
Social Network Analysis and Mining (2024) 14:244
244 
Page 30 of 35
The number of publications was low, with studies scat-
tered across various disciplines like law, linguistics, and 
sociology.
2000s
The rise of the internet and online hate speech led to a surge 
in research interest.
Studies began to focus on analysing online hate speech 
content, developing detection methods, and understanding 
its psychological and social impacts.
2010s
The penetration of social networking sites like Twitter and 
Facebook further amplified the issue of online hate speech.
Research efforts intensified, with a focus on:
Automatic detection and classification of hate speech: 
This involved developing machine learning algorithms to 
identify hateful content based on textual and linguistic 
features.
Impact of hate speech: Studies explored the psychologi-
cal harms of hate speech on both victims and perpetra-
tors, as well as its implications for social cohesion and 
democracy.
Countermeasures and interventions: Researchers inves-
tigated strategies to combat hate speech, including platform 
regulation, content moderation, and educational campaigns.
2020s
The trend of increasing research continues, with even more 
sophisticated and nuanced approaches being adopted. Some 
key areas of focus include:
Contextual understanding of hate speech: Moving beyond 
just textual analysis, researchers are now considering the 
broader context in which hate speech occurs, including fac-
tors like speaker intent, audience reaction, and platform 
norms.
Multilingual and cross-cultural perspectives: With hate 
speech prevalent across languages and cultures, research 
is expanding to understand its diverse manifestations and 
develop effective countermeasures in different contexts.
Ethical considerations: The use of automated technolo-
gies for hate speech detection raises concerns about bias, 
freedom of expression, and privacy. Research is addressing 
these ethical challenges to ensure responsible development 
and deployment of such technologies.
Fig. 8   H indexing impact

--- Page 31 ---

Social Network Analysis and Mining (2024) 14:244	
Page 31 of 35 
244
4.4  Absence of fine‑grained classification methods
Current hate speech detection research primarily uses binary 
classification, categorizing content as either "hate speech" 
or "non-hate speech." However, this binary approach fails to 
capture the complexity of hate speech, which ranges from 
explicit threats to subtle biases and micro-aggressions. There 
is a need for more nuanced models that can classify different 
levels and types of hate speech, providing deeper insight and 
enabling more effective moderation (Davidson et al. 2017).
4.4.1  Focus on Hindi Language
Despite the global prevalence of Hindi and its linguistic 
complexities such as dialectal variation, code-mixing, and 
script diversity—research on hate speech detection in Hindi 
remains limited. Given the widespread use of Hindi on 
social media, there is a critical need for focused research to 
bridge this gap and develop effective hate speech detection 
models tailored to the language (Bohra et al. 2018).
4.4.2  Bias mitigation
Machine learning models trained on biased data can produce 
unfair or discriminatory results. There is a significant lack of 
research dedicated to systematically mitigating bias in hate 
speech detection models. Developing strategies to address 
this issue is essential to ensure models are both accurate 
and equitable, preventing the reinforcement of social biases 
(Sap et al. 2019).
Fig. 9   Connection network
Fig. 10   Distribution of hate speech.  Source: https://​www.​mdpi.​com/​
2078-​2489/​13/6/​273

--- Page 32 ---

	
Social Network Analysis and Mining (2024) 14:244
244 
Page 32 of 35
4.4.3  High‑quality multilingual datasets
The scarcity of high-quality, labelled datasets in languages 
other than English is a major obstacle to the development 
of effective hate speech detection models. In multilingual 
contexts, particularly for languages like Hindi, this lack lim-
its the generalizability and robustness of these models. The 
creation of extensive multilingual datasets is urgently needed 
to support the development of more sophisticated and uni-
versally applicable hate speech detection models (Waseem 
et al. 2016).
5  Conclusion
5.1  Conclusion
Hate speech detection in the Hindi language setting high-
lights challenges and required solutions for building effec-
tive, aware-of-culture, and understanding-in-depth AI sys-
tems. We have covered the wide-ranging complications 
involved in this task, from linguistic variety and script dif-
ferences to sociolinguistic contexts that separate hate speech 
from other types of communication.
The interplay of those Hindi colloquialisms, regional 
slangs, and code-switching is highlighted as a significant 
challenge to automated systems throughout the literature. 
Nevertheless, the field of NLP and ML has evolved fur-
ther towards complex models that can identify trends and 
contexts more effectively. Contextual embeddings, transfer 
learning, and sentiment analysis are some of the techniques 
that have improved hate speech detection algorithms and 
provided a better understanding of the intent and potential 
harm behind online content.
The review also emphasizes the importance of datasets 
being comprehensive and balanced. However, a major road-
block came in the form of a lack of availability of labelled 
data for hate speech detection in Hindi. We are already loose 
on tackling this challenge due to creative algorithms like 
synthetic data and semi-supervised learning but opened up 
a fairly new space via data augmentation of which the users 
could eventually partake. In addition, native speakers and 
subject matter experts also take part in data annotation pro-
cess to ensure that the content has cultural relevance and 
therefore enhances models’ reliability.
In addition to this, finally the ethical aspect and consid-
erations of hate speech detection cannot be ignored It is a 
fine line between refraining or prohibiting hate speech from 
our society while at the same time ensuring that free speech 
is not being compromised. Future efforts should be directed 
towards developing AI systems that are transparent, account-
able, and equitable in a progressive manner. We must also 
continuously monitor them for bias and second-order effects, 
keeping them safe from hate speech but still upholding the 
principles of equity and fairness.
The field of Hate Speech detection in Hindi, not only 
embodies the potentials of AI creating a safer internet for all, 
but also shows us the heavy price that comes with it. This 
will finally be driven by the collective action of research-
ers, practitioners and policymakers. Using cutting-edge 
technologies, promoting inter-disciplinary collaboration 
and dictating high ethical standards makes one have a hope 
that the entire damaging effect of spreading hate speech can 
somehow be diminished and more integrated into the trend 
of dignifying and embracing digital communication.
5.2  Future scope and potential challenges
In recent years, a considerable amount of work has been 
focused on the detection of hate speech across multiple lan-
guages. This research will specifically build machine learning 
and deep learning models for the Hindi language, while ensur-
ing that all the unique problems including code-switching, 
geographical dialects and script variations are solved for their 
respective datasets. However, even though Hindi is among the 
most widely used languages in the world, research work on 
hate speech detection has not received as much attention in 
English as it has. The purpose of this project is to develop 
the best possible models for detecting and categorizing hate 
speech in Hindi (Solorio et al. 2014).
Hate speech detection algorithms find code-switching 
and multilingual contexts a major bottleneck. Since mixed-
language content does not follow a standardized spelling and 
grammar due to word borrowing (Barman et al. 2018), exist-
ing models trained on monolingual datasets cannot be applied 
(Agarwal and Kumar 2021). To address the diversity of lan-
guages and cultural differences, rich multilingual corpora and 
NLP models are needed (Chakravarthi et al. 2020).
There are several aspects of interest here Hindi NLP mod-
els, datasets, code-mixing, cultural/contextual understanding 
and so on. The current work would not only help advance hate 
speech detection for Hindi, but would also aid in cross-lin-
gual efforts towards hate speech detection (Bohra et al. 2018; 
Davidson et al. 2017).
Future Scope: Future datasets may also be cross-linguistic 
and multi-modal – image, videos, audio and so on to better 
track hate speech dissemination through different forms of 
media. Such improvements may result in stronger detection 
systems (Matamoros-Fernández 2017). Also, future work 
should focus on the socio-cultural consequences of hate speech 
and the need to build real-time detection systems (Waseem 
and Hovy 2016).
Challenges Faced by Hindi Hate Speech Detector: The 
dialect diversity, code-switching phenomenon, and lack of data 
availability for multiple stages among Hindi linguistic circles 

--- Page 33 ---

Social Network Analysis and Mining (2024) 14:244	
Page 33 of 35 
244
make it difficult to provide adequate work from NLP models. 
The perspective of the detected entity become bias in machine 
learning model (Zou and Schiebinger, 2018; Lipton, 2020) and 
cultural context (Giu et al. 2019), sarcasm and homographs 
(Gladkova et al. 2017), Slang and political sensitivities intro-
duce additional layers of complexity to the challenge of detect-
ing hate speech detection(Sap et al. 2019; Joshi et al. Making 
sure our algorithms are fair and lawful can be complicated, 
depending on the legal definitions of hate speech vary from 
state to state (Zarsky 2016).
Author contribution  Each of the author have equally contributed to 
the research.
Data availability  No datasets were generated or analysed during the 
current study.
Declarations 
Conflict of interest  The authors declare no competing interests.
References
Al-Hussaeni K, Sameer M, Karamitsos I (2023) The impact of data 
pre-processing on hate speech detection in a mix of English and 
Hindi–English (code-mixed) tweets. Appl Sci 13(19):11104
Aluru SS, Mathew B, Saha P, Mukherjee A (2020) Deep learning mod-
els for multilingual hate speech detection. arXiv preprint arXiv:​
2004.​06465
Awan I (2014) Islamophobia and Twitter: a typology of online hate 
against Muslims on social media. Policy Internet 6(2):133–150
Badjatiya P, Gupta S, Gupta M, Varma V (2017) Deep learning for 
hate speech detection in tweets. In: Proceedings of the 26th inter-
national conference on World Wide Web companion, pp 759–760
Bansod PP (2023) Hate speech detection in Hindi
Bellamy RKE et al (2018) AI Fairness 360: an extensible toolkit for 
detecting, understanding, and mitigating unwanted algorithmic 
bias. arXiv preprint arXiv:​1810.​01943
Bergstra J, Bengio Y (2012) Random search for hyper-parameter opti-
mization. J Mach Learn Res 13:281–305
Bohra A, Vijay D, Singh V, Akhtar SS, Shrivastava M (2018) A dataset 
of Hindi-English code-mixed social media text for hate speech 
detection. In: Proceedings of the second workshop on computa-
tional modeling of people’s opinions, personality, and emotions 
in social media, pp 36–41
Breunig MM, Kriegel HP, Ng RT, Sander J (2000) LOF: identifying 
density-based local outliers. ACM SIGMOD Rec 29(2):93–104
Buolamwini J, Gebru T (2018) Gender shades: intersectional accuracy 
disparities in commercial gender classification. In: Conference on 
fairness, accountability and transparency
Chakravarthi BR, Muralidaran V, Priyadharshini R, McCraeJP (2020) 
Overview of the DRAVIDIANLANGTECH 2020 shared task on 
sentiment analysis of code-mixed Tamil-English and Malayalam-
English tweets. In: Proceedings of the WILDRE5–5th workshop 
on Indian language data: resources and evaluation. European lan-
guage resources association (ELRA), pp 1–9
Chollet F (2017) Deep learning with Python. Manning Publications, 
New York
Chopra A, Sharma DK, Jha A, Ghosh U (2023) A framework for online 
hate speech detection on code-mixed Hindi–English Text and 
Hindi Text in Devanagari. ACM Trans Asian Low-Resour Lang 
Inf Process 22(5):1–21
  Chowdhury S, Gonzalo P, Liscano R. (2020). A hybrid approach to 
context-aware trust-based access control with machine learning. 
IEEE Access, 8, 87758-87774
Citron DK, Norton H (2011) Intermediaries and hate speech: foster-
ing digital citizenship for our information age. BUL Rev 91:1435
Das M, Saha P, Mathew B, Mukherjee A (2022) Hatecheckhin: evalu-
ating Hindi hate speech detection models. arXiv preprint arXiv:​
2205.​00328
Davidson T, Warmsley D, Macy M, Weber I (2017) Automated hate 
speech detection and the problem of offensive language. In Pro-
ceedings of the international AAAI conference on web and social 
media, vol 11, no 1, pp 512–515
Devlin J, Chang MW, Lee K, Toutanova K (2019) BERT: pre-training 
of deep bidirectional transformers for language understanding. 
In: Proceedings of the 2019 conference of the North American 
chapter of the association for computational linguistics: human 
language technologies, volume 1 (Long and Short Papers), pp 
4171–4186
Ganin Y, Ustinova E, Ajakan H, Germain P, Larochelle H, Laviolette 
F et al (2016) Domain-adversarial training of neural networks. J 
Mach Learn Res 17(1):2096–2030
Ghosh K, Senapati A, Narzary M, Brahma M (2023) Hate speech 
detection in low-resource Bodo and Assamese texts with ML-DL 
and BERT models. Scalable Comput Pract Exp 24(4):941–955
Gillespie T (2018) Custodians of the internet: platforms, content 
moderation, and the hidden decisions that shape social media. 
Yale University Press, New Haven
Gorwa R (2019) What is platform governance? Inf Commun Soc 
22(6):854–871
Gupta V, Sehra V, Vardhan YR (2021). Hindi-english code-mixed 
hate speech detection using character level embeddings. 
In: 2021 5th international conference on computing method-
ologies and communication (ICCMC). IEEE, pp 1112–1118
Hardt M, Price E, Srebro N (2016) Equality of opportunity in super-
vised learning. Adv Neural Inf Process Syst 29:3315–3323
Holstein K, Wortman Vaughan J, Daumé III, H, Dudik M, Wallach H 
(2019) Improving fairness in machine learning systems: What 
do industry practitioners need? In: Proceedings of the 2019 CHI 
conference on human factors in computing systems, pp 1–16
Ibrahim MA, Arifin S, Purwanto ES (2023) Exploring data augmen-
tation for gender-based hate speech detection. J Comput Sci 
19(10):1222–1230. https://​doi.​org/​10.​3844/​jcssp.​2023.​1222.​
1230
Kapil P, Kumari G, Ekbal A, Pal S, Chatterjee A, Vinutha BN (2023) 
HHSD: Hindi hate speech detection leveraging multi-task learn-
ing. IEEE Access 11:101460–101473
Lanasri D, Olano J, Klioui S, Lee SL, Sekkai L (2023) Hate speech 
detection in algerian dialect using deep learning. arXiv preprint 
arXiv:​2309.​11611
Langton R (2018) Blocking as counter-speech. New Work Speech 
Acts 144:156
Lundberg SM, Lee S-I (2017) A unified approach to interpreting 
model predictions. Adv Neural Inf Process Syst 4765–4774
Mandl T, Modha S, Kumar MA, Chakravarthi BR (2020) Overview 
of the hasoc track at fire 2020: hate speech and offensive lan-
guage identification in tamil, malayalam, hindi, english and ger-
man. In: Proceedings of the 12th annual meeting of the forum for 
information retrieval evaluation, pp 29–32
Marwick AE, Lewis R (2017) Media manipulation and disinforma-
tion online
Matamoros-Fernández A (2017) Platformed racism: the mediation and 
circulation of an Australian race-based controversy on Twitter, 
Facebook and YouTube. Inf Commun Soc 20(6):930–946

--- Page 34 ---

	
Social Network Analysis and Mining (2024) 14:244
244 
Page 34 of 35
Mathew B, Saha P, Yimam SM, Biemann C, Goyal P, Mukherjee 
A (2021) Hatexplain: a benchmark dataset for explainable hate 
speech detection. In Proceedings of the AAAI conference on arti-
ficial intelligence, vol 35, no 17, pp 14867–14875
Mubarak H, Darwish K, Magdy W (2017) Abusive language detection 
on Arabic social media. In: Proceedings of the first workshop on 
abusive language online, pp 52–56
Mulki H, Haddad H, Ali CB, Alshabani H (2019) L-hsab: a levantine 
twitter dataset for hate speech and abusive language. In: Pro-
ceedings of the third workshop on abusive language online, pp 
111–118
Ousidhoum N, Lin Z, Zhang H, Song Y, Yeung DY (2019) Multilin-
gual and multi-aspect hate speech analysis. arXiv preprint arXiv:​
1908.​11049
Phung TM, Cloos J (2022) An exploratory experiment on Hindi, Ben-
gali hate-speech detection and transfer learning using neural net-
works. arXiv preprint arXiv:​2201.​01997
Pohjonen M, Udupa S. (2017). Extreme speech online: An anthropo-
logical critique of hate speech debates. International Journal of 
Communication, 11, 19
Prasad D, Kadambari KV, Mukati R, Singariya S (2023) Real-time 
multi-lingual hate and offensive speech detection in social net-
works using meta-learning. In: TENCON 2023–2023 IEEE 
Region 10 conference (TENCON). IEEE, pp 31–35
Prashant Kapil P, Asif Ekbal A (2022) A transformer based multi-task 
learning approach leveraging translated and transliterated data to 
hate speech detection in Hindi. In: Computer Science and Infor-
mation Technology (CS and IT) - CSCP 2022, pp 191–207
Rabiul Awal M, Ka-Wei Lee R, Tanwar E, Garg T, Chakraborty T 
(2023) Model-agnostic meta-learning for multilingual hate speech 
detection. arXiv e-prints, arXiv-2303
Ribeiro MT, Singh S, Guestrin C (2016) Why should i trust you? 
Explaining the predictions of any classifier. In: Proceedings of 
the 22nd ACM SIGKDD International conference on knowledge 
discovery and data mining, pp 1135–1144
Röttger P, Seelawi H, Nozza D, Talat Z, Vidgen B (2022) Multilingual 
hatecheck: functional tests for multilingual hate speech detection 
models. arXiv preprint arXiv:​2206.​09917
Ruder S (2019) Neural transfer learning for natural language process-
ing. Doctoral dissertation, NUI Galway
Sameer M (2022) Hate speech detection in a mix of English and Hindi–
English (Code-Mixed) tweets
Sap M, Card D, Gabriel S, Choi Y, Smith NA (2019) The risk of 
racial bias in hate speech detection. In Proceedings of the 57th 
annual meeting of the association for computational linguistics, 
pp 1668–1678
Scrivens, R., Davies, G., & Frank, R. (2018). Searching for signs of 
extremism on the web: an introduction to Sentiment-based Iden-
tification of Radical Authors. Behavioural sciences of terrorism 
and political aggression, 10(1), 39-59
Shorten C, Khoshgoftaar TM (2019) A survey on image data augmen-
tation for deep learning. J Big Data 6(1):1–48
Shukla S, Nagpal S, Sabharwal S (2022) Hate speech detection in Hindi 
language using BERT and convolution neural network. In: 2022 
international conference on computing, communication, and intel-
ligent systems (ICCCIS). IEEE, pp 642–647 
Sohn H, Lee H (2019) Mc-bert4hate: Hate speech detection using 
multi-channel bert for different languages and translations. 
In: 2019 international conference on data mining workshops 
(ICDMW). IEEE, pp 551–559
Solorio T, Blair E, Maharjan S, Bethard S, Davila K (2014) Over-
view for the shared task on sentiment analysis in code-switched 
data. In: Proceedings of the first workshop on computational 
approaches to code switching. Association for Computational 
Linguistics, pp 1–7
Suzor N (2018) Digital constitutionalism: using the rule of law to 
evaluate the legitimacy of governance by platforms. Soc Media 
Soc 4(3):2056305118787812
Timmermann W (2008) Counteracting hate speech as a way of pre-
venting genocidal violence. Genocide Stud Prevent 3(3):353–374
Tucker, J. A., Guess, A., Barberá, P., Vaccari, C., Siegel, A., Sanovich, 
S., ... & Nyhan, B. (2018). Social media, political polarization, 
and political disinformation: A review of the scientific literature. 
Political polarization, and political disinformation: a review of the 
scientific literature (March 19, 2018)
Tynes BM, Willis HA, Stewart AM, Hamilton MW (2019) Race-related 
traumatic events online and mental health among adolescents of 
color. J Adolesc Health 65(3):371–377
U.S. Government Accountability Office (2024) Online extremism: 
more complete information needed about hate crimes that occur 
on the internet (GAO-24-105553). https://​www.​gao.​gov/​assets/​
d2410​5553.​pdf
Waseem Z, Hovy D (2016) Hateful symbols or hateful people? predic-
tive features for hate speech detection on twitter. In: Proceedings 
of the NAACL student research workshop, pp 88–93
Wilson RA (2019) The digital ethnography of law: studying online hate 
speech online and offline. J Legal Anthropol 3(1):1–20
Yadav S, Kaushik A, McDaid K (2023) Hate speech is not free speech: 
explainable machine learning for hate speech detection in code-
mixed languages. In: 2023 IEEE international symposium on 
technology and society (ISTAS). IEEE, pp 1–8
Banks JA. (2010). Multicultural education: characteristics and goals. 
In J. Banks & C. McGee-Banks (Eds), Multicultural education: 
Issues and perspectives (Seventh ed., pp. 3–33). Danvers, MA: 
John Wiley & Sons
Waseem Z, & Hovy D. (2016, June). Hateful symbols or hateful peo-
ple? predictive features for hate speech detection on twitter. In 
Proceedings of the NAACL student research workshop (pp. 88-93)
Zarsky TZ. (2016). Incompatible: The GDPR in the age of big data. 
Seton Hall L. Rev., 47, 995
Joshi R, Goel P,  Joshi R. (2020). Deep learning for hindi text classi-
fication: A comparison. In Intelligent Human Computer Interac-
tion: 11th International Conference, IHCI 2019, Allahabad, India, 
December 12–14, 2019, Proceedings 11 (pp. 94-101). Springer 
International Publishing
Jamatia A, Swamy SD, Gambäck B, Das A,  Debbarma S. (2020). Deep 
learning-based sentiment analysis in a code-mixed English-Hindi 
and English-Bengali social media corpus. International journal on 
artificial intelligence tools, 29(05), 2050014
Waseem Z, Davidson T, Warmsley D,  Weber I. (2017). Understanding 
abuse: A typology of abusive language detection subtasks. arXiv 
preprint arXiv:1705.09899
C. Cortes and Vladimir N. Vapnik. (1995). Support Vector Networks. 
Machine Learning, 20:273-297
Hochreiter S,  Schmidhuber J. (1997). Flat minima. Neural computa-
tion, 9(1), 1-42
Pamungkas EW, Basile V, & Patti V. (2020). A joint learning approach 
with knowledge injection for zero-shot cross-lingual hate speech 
detection. Information Processing & Management, 58(4), 102544.
Das AK, Al Asif A, Paul A,  Hossain MN. (2021). Bangla hate speech 
detection on social media using attention-based recurrent neural 
network. Journal of Intelligent Systems, 30(1), 578-591
Zou J,  Schiebinger L. (2018). AI can be sexist and racist—it’s time 
to make it fair
Vashistha N, Zubiaga A. (2020). Online multilingual hate speech 
detection: experimenting with Hindi and English social media. 
Information, 12(1), 5
Gambäck B, Sikdar UK. (2017). Using convolutional neural networks 
to classify hate-speech. In Proceedings of the First Workshop on 

--- Page 35 ---

Social Network Analysis and Mining (2024) 14:244	
Page 35 of 35 
244
Abusive Language Online. Vancouver, BC, Canada: Association 
for Computational Linguistics, pp. 85–90
Zhang Z, Robinson D, Tepper J. (2018). Detecting hate speech on 
twitter using a convolution-gru based deep neural network. In 
The Semantic Web: 15th International Conference, ESWC 2018, 
Heraklion, Crete, Greece, June 3–7, 2018, Proceedings 15 (pp. 
745-760). Springer International Publishing
Mozafari M, Farahbakhsh R, Crespi N. (2020). A BERT-based transfer 
learning approach for hate speech detection in online social media. 
In Complex Networks and Their Applications VIII: Volume 1 
Proceedings of the Eighth International Conference on Complex 
Networks and Their Applications COMPLEX NETWORKS 2019 
8 (pp. 928-940). Springer International Publishing
Sreelakshmi K, Premjith B, Soman KP (2020). Detection of hate 
speech text in Hindi-English code-mixed data. Procedia Computer 
Science, 171, 737-744
Ranasinghe T, Zampieri M. (2020). Multilingual offensive language 
identification with cross-lingual embeddings. arXiv preprint 
arXiv:2010.05324
Sachdeva J, Chaudhary KK, Madaan H, & Meel P. (2021, March). 
Text based hate-speech analysis. In 2021 International Confer-
ence on Artificial Intelligence and Smart Systems (ICAIS) (pp. 
661-668). IEEE.
Waseem Z, & Hovy D. (2016, June). Hateful symbols or hateful 
people? predictive features for hate speech detection on twitter. 
In Proceedings of the NAACL student research workshop (pp. 
88-93).
Mathew B, Saha P, Yimam SM, Biemann C, Goyal P, & Mukherjee 
A. (2021, May). Hatexplain: A benchmark dataset for explainable 
hate speech detection. In Proceedings of the AAAI conference on 
artificial intelligence (Vol. 35, No. 17, pp. 14867-14875).
 Aggarwal S, Kumar S, & Mamidi R. (2021, September). Efficient mul-
tilingual text classification for Indian languages. In Proceedings 
of the International Conference on Recent Advances in Natural 
Language Processing (RANLP 2021) (pp. 19-25).
Fazelpour S, & Lipton ZC. (2020, February). Algorithmic fairness 
from a non-ideal perspective. In Proceedings of the AAAI/ACM 
Conference on AI, Ethics, and Society (pp. 57-63).
Wang Y, Li Y, Gui X, Kou Y, & Liu F. (2019). Culturally-embedded 
visual literacy: A study of impression management via emoticon, 
emoji, sticker, and meme on social media in China. Proceedings 
of the ACM on Human-Computer Interaction, 3(CSCW), 1-24.
Gladkova A., & Drozd A. (2017, August). Intrinsic evaluations of 
word embeddings: What can we do better?. In Proceedings of 
the 1st Workshop on Evaluating Vector-Space Representations 
for NLP (pp. 36-42).
Publisher's Note  Springer Nature remains neutral with regard to 
jurisdictional claims in published maps and institutional affiliations.
Springer Nature or its licensor (e.g. a society or other partner) holds 
exclusive rights to this article under a publishing agreement with the 
author(s) or other rightsholder(s); author self-archiving of the accepted 
manuscript version of this article is solely governed by the terms of 
such publishing agreement and applicable law.

```
