---
title: "2024-Çakici-A cross-validation study of Turkish sentiment analysis datasets and - PDF Extract"
source_pdf: "2024-Çakici-A cross-validation study of Turkish sentiment analysis datasets and.pdf"
pages: 39
extracted_at: "2026-02-13T14:50:53.553011"
---

# PDF Extract: 2024-Çakici-A cross-validation study of Turkish sentiment analysis datasets and

**Source PDF:** 2024-Çakici-A cross-validation study of Turkish sentiment analysis datasets and.pdf
**Total Pages:** 39

---

## Content

```
--- Page 1 ---

ORIGINAL PAPER
Language Resources and Evaluation (2025) 59:4003–4041
https://doi.org/10.1007/s10579-025-09869-6
Abstract
In recent years, sentiment analysis has gained increasing significance, prompting re­
searchers to explore datasets in various languages, including Turkish. However, the 
limited availability and reuse of Turkish datasets across studies has yielded highly 
diverse outcomes. To address this, we conducted a systematic review of sentiment 
analysis studies on Turkish text. Our search identified 78 relevant studies, from 
which we extracted over 80 datasets. These studies were labeled using a compre­
hensive sentiment analysis taxonomy, and the dataset details were compiled into 
a structured repository. Furthermore, we evaluated the performance of four state-
of-the-art models-XLM-T, BERTurk (fine-tuned with the BounTi dataset), TSAM, 
and TurkishBERTweet-on four widely-used Turkish datasets. Among the models, 
XLM-T achieved the highest performance with an accuracy of 0.92 and F1 score 
of 0.95 on the Twt dataset, while TSAM reached 0.97 accuracy and F1 score on 
the Humir dataset. Our empirical results demonstrate that model performance varies 
significantly based on dataset characteristics such as domain, balance, and linguistic 
structure. Our review revealed key research gaps, including the limited application 
of emotion-based and concept-based sentiment analysis techniques and the lack of 
domain diversity in Turkish sentiment datasets. By highlighting such gaps and com­
piling a centralized repository, this study provides a comprehensive and publicly 
accessible resource to guide future research in Turkish sentiment analysis.
Keywords  Sentiment analysis · Turkish dataset · Cross-validation · Taxonomy · 
Deep learning models
Received: 12 December 2024 / Accepted: 17 July 2025 / Published online: 26 August 2025
© The Author(s) 2025
A cross-validation study of Turkish sentiment analysis 
datasets and tools
Şevval Çakıcı1 · Dilara Karaduman2 · Mehmet Akif Çırlan2 · Ali Hürriyetoğlu3
Extended author information available on the last page of the article
1 3

--- Page 2 ---

Ş. Çakıcı et al.
1  Introduction
The world is closely associated with people’s feelings and behaviors, ranging from 
research on societal trends to applications in product marketing. In recent years, the 
need for a systematization of understanding emotions and behaviors has become 
even more pronounced. Typically, scholars frame emotion as a mental experience, 
and the necessity to define and classify emotions has led to models such as Plutchik’s 
wheel of emotions (Plutchik, 1980). Ekman (1992) focused on six basic emotions, 
often referred to as Ekman categories in the text processing literature. According to 
Cabanac (2002), when there is no standard definition in the literature, researchers 
usually define emotion concerning a list: anger, disgust, fear, joy, sadness, and sur­
prise. These categorizations are foundational in many fields, especially in sentiment 
analysis and text processing.
With the development of technology, data has started to be recorded in the digi­
tal world more than ever in the history of humanity, with platforms like Facebook, 
Twitter, and Instagram serving as prime platforms of this digital data explosion. The 
vast amounts of user-generated online content provide an unprecedented opportunity 
to study human behavior on a large scale. Since the recorded data is accessible to 
everyone, it also plays a role in emerging new behaviors. For example, the expected 
behavior of the 21st-century consumer includes looking at the opinions of others 
online before making a decision (Yayli & Bayram, 2012). Likewise, companies ana­
lyze consumer behavior and opinions similarly before making decisions and launch­
ing a product. Such big data, which includes people’s thoughts, feelings, opinions, 
and practices, also serves as a source for scientific research.
Sentiment analysis, which arises as a result of the need to analyze behavior, evalu­
ate people’s attitudes, and orientations, and classify their emotions, is typically con­
cerned with determining the overall positive or negative stance expressed in text 
(Devika et al., 2016). For many practical applications, understanding this general 
sentiment is more critical than identifying specific emotions. Sentiment analysis, 
also known as opinion mining, is the computational study of people’s sentiments, 
feelings, views, and attitudes toward a particular topic, situation, event, or product 
(Zhang et al., 2018). This approach enables governments to notice mass referrals and 
helps companies analyze the behavior and views of their target audience. According 
to Zhang et al. (2018), these practices and industrial interests stimulated high motiva­
tions for sentiment analysis research.
Sentiment analysis studies are conducted in many languages, as Abbasi et al. 
(2008) indicated. Among these languages, Turkish ranked fourth in common lan­
guages for web content in January 2021, according to ‘The Most Used Languages 
on the Internet – Visual Capitalist Licensing’ (n.d.) (Visual Capitalist, 2022). As of 
July 2022, Internet World Stats, 2022) reports Turkey’s population as 85,839,173, 
with 72,500,000 internet users, underscoring the statistical significance of the Turk­
ish language on the internet (Internet World Stats, 2022). However, the limited avail­
ability of datasets in some commonly used languages in scientific environments leads 
to using the same or similar datasets in different studies. For instance, examining 
Turkish sentiment analysis studies published between 2012 and 2025 reveals that 
researchers created and used only 23 datasets in 31 studies. Most of these data sets 
1 3
4004

--- Page 3 ---

A cross-validation study of Turkish sentiment analysis datasets and…
contain less than ten thousand samples. These small-scale datasets are not obtained 
from a wide variety of sources. The most frequently recurring dataset is the one cre­
ated by Demirtas and Pechenizkiy (2013), utilized not only in their studies but also in 
works by Parlar and Özel (2016), Mulki et al. (2018) and Alqaraleh (2021).
In addition to general applications, Turkish sentiment analysis has also been 
applied in various domain-specific contexts. For example, Alawi and Bozkurt (2024c) 
introduced the Twitter Dataset, focusing on student opinions regarding higher educa­
tion institutions, which reflects sentiment trends in the education sector. In the health 
domain, Aygün et al. (2021) conducted an aspect-based sentiment analysis on pub­
lic discourse related to COVID-19 vaccines, revealing insights into public attitudes 
towards different vaccine types. Moreover, Yayli and Bayram (2012) explored the 
impact of online consumer reviews on purchasing behavior, emphasizing the rel­
evance of sentiment analysis for marketing and e-commerce research.
An aspect that needs more focus in Turkish sentiment analysis publications is the 
comparative presentation of these studies. To address this, we conducted an investi­
gation on research papers on ‘sentiment analysis’ and ‘Turkish dataset’ on Scopus to 
address this challenge. Subsequently, 78 studies and the datasets used within them 
were compiled and organized in a GitHub repository,1 including publicly available 
datasets (with access links) and non-public datasets (accompanied by the correspond­
ing authors’ contact information). In this study, we assign labels to these publications 
based on the sentiment analysis taxonomy classification (Rodrigues et al., 2018) to 
provide a comprehensive perspective. The goal is to offer a valuable resource for 
future sentiment analysis research in Turkish by classifying and comparing these 
studies.
Furthermore, the methodology employed aligns with the principles of a System­
atic Literature Review (SLR), aiming to identify relevant primary studies, extract 
the required information regarding the research questions (RQs), and synthesize the 
information to respond to these RQs. An SLR follows a well-defined methodology 
and assesses the literature in an unbiased and repeatable way (Kitchenham & Char­
ters, 2007).
We generate predictions using four transformer-based models: the multilingual 
XLM-T (Barbieri et al., 2021), trained on 198 million tweets and fine-tuned for senti­
ment analysis; BERTurk enhanced with the BounTi dataset (Köksal & Özgür, 2021); 
TSAM, a domain-specific model developed for Turkish sentiment tasks (Tasar et 
al., 2022); and TurkishBERTweet by ViralLab (Najafi & Varol, 2024). These models 
were evaluated on four widely reused datasets that appeared in multiple publica­
tions among the 78 studies included in our review. Another purpose of this study is 
to compare the best-reported model predictions from the studies and the predictions 
of the models. For this purpose, it is desired to shed light on the reasons for the low 
accuracy scores and to contribute to the cross-domain classification literature with 
the compiled information Hürriyetoglu et al. (2021).
Our study is designed to achieve two primary objectives. Firstly, it aims to pro­
vide a comprehensive and detailed overview of sentiment analysis in the Turkish 
language, offering a systematic classification and thorough comparison of existing 
1 https://github.com/sevvalckc/Turkish-SAD
1 3
4005

--- Page 4 ---

Ş. Çakıcı et al.
research. Secondly, the study focuses on comparing and discussing Turkish senti­
ment analysis tools in the context of dataset characteristics. By undertaking these 
objectives, we seek to contribute valuable insights to the field of Turkish sentiment 
analysis, facilitating a deeper understanding of the methodologies employed, dataset 
variations, and the overall landscape of sentiment analysis research in the Turkish 
language.
The upcoming parts of this article are organized as follows. In Sect. 2, we review 
relevant studies in sentiment analysis and cross-dataset classification. Then, sec­
tion 2.1 presents the methodology for study selection, details of the datasets, and 
introduces a heatmap to visualize the temporal distribution of taxonomy labels. Next, 
section 3 outlines the models used and the sentiment analysis process applied to 
selected Turkish datasets. Following that, section 4 reports model performance across 
datasets. Section 5 interprets the findings and highlights key observations. In Sect. 6, 
we elaborate on the theoretical, practical, and future research implications of our 
study. Afterward, section 7 summarizes the key takeaways. Finally, Sect. 8 proposes 
directions for future research including dataset expansion, model integration, and the 
use of large language models.
2  Related work
Our research focuses on sentiment analysis, a field predominantly concentrated 
on English language studies. However, we are specifically focusing on the Turk­
ish language. Acknowledging this methodology, our study aims to address this gap 
by systematically compiling and examining existing sentiment analysis research and 
datasets in Turkish. This effort is crucial for advancing the understanding and devel­
opment of sentiment analysis research, tools, and methodologies for the Turkish lan­
guage, thereby contributing to the improvement and enrichment of the Turkish NLP 
field.
A comprehensive study by Altinel Girgin et al. (2024) reviews the methods used 
in Turkish sentiment analysis, categorizing them into three main approaches: dic­
tionary-based, machine learning-based, and hybrid. Their analysis highlights the 
strengths and weaknesses of each method, particularly emphasizing that machine 
learning techniques are better suited to Turkish’s complex linguistic structure. Our 
study, by contrast, examines 78 studies through a taxonomic classification, analyz­
ing datasets in depth. We further compare the performance of four different deep 
learning models fine-tuned for sentiment analysis across these datasets, revealing the 
crucial impact of data diversity on model accuracy. This comparative approach adds 
a broader perspective, focusing on datasets and taxonomy, and highlights the signifi­
cant role of data preparation in sentiment analysis methods.
Similarly, Fehle et al. (2021)’s study systematically examines the methods of sen­
timent analysis for German texts and is a review. The study evaluates 19 existing 
sentiment dictionaries and 20 sentiment annotated corpora for German texts. This 
comprehensive review analyzes how the dictionaries and datasets perform in differ­
ent domains, while also detailing the impact of preprocessing steps (stemming, lem­
matization, etc.) used before sentiment analysis on performance. In this respect, the 
1 3
4006

--- Page 5 ---

A cross-validation study of Turkish sentiment analysis datasets and…
study provides a broad map of the methods used in sentiment analysis specific to the 
German language, similar to the literature reviews of sentiment analysis in Turkish.
Also, Oueslati et al. (2020) provide a detailed review of sentiment analysis research 
in Arabic. They examine different methods and datasets, focusing on machine learn­
ing and deep learning techniques. The study highlights challenges and limitations 
unique to Arabic sentiment analysis, such as its complex morphology. By pointing 
out gaps in the existing literature, the authors suggest directions for future research, 
including developing better datasets and models. Given the similarities in linguistic 
complexities, their review is a valuable resource for researchers working on Turkish 
sentiment analysis and dataset development.
The Turkish language has several linguistic features that pose unique challenges 
for sentiment analysis. As an agglutinative language, Turkish forms words by attach­
ing multiple suffixes to a single root, resulting in highly inflected and morphologi­
cally rich structures. For example, the word “sevmediğiniz” (meaning “that you don’t 
like”) combines a root (sev-) with negation (-me-), past tense (-di-), and second-
person plural (-ğiniz). These complex word forms contribute to a vastly expanded 
vocabulary and complicate model training based on word-level tokens (Oflazer, 
1994). Moreover, Turkish exhibits a relatively free word order with frequent use of 
scrambling-a syntactic phenomenon where constituents can appear in various posi­
tions without altering core meaning-which introduces further variability and sparsity 
in training data (Oflazer et al., 2003; Erguvanli-Taylan, 1984). These characteristics 
collectively reduce the effectiveness of traditional NLP models and demand more 
sophisticated morphological and syntactic handling.
Turkish also includes other structural challenges, such as vowel harmony, rich 
inflection, and derivational morphology, all of which can cause issues during prepro­
cessing and modeling. As highlighted by Aktas and Çebi (2020), these features can 
reduce the success of commonly used tools for tasks like tokenization and root detec­
tion. Even well-known NLP tools may struggle to handle the variation and ambiguity 
caused by Turkish morphology.
Rodrigues et al. (2018) contribute a detailed taxonomy of sentiment analysis stud­
ies. We utilized it to further enhance our study. This taxonomy, which is provided in 
Table 1, is a comprehensive framework that systematically classifies sentiment analy­
sis studies based on critical considerations. It addresses key aspects such as input 
structure, target class, opinion holder, analysis target, features analyzed in data, data 
source, application domain, and the approach of lexicon-based, concept-based, and 
machine learning-based methods. We used the taxonomy presented in Table 1 to clas­
sify Turkish sentiment analysis studies and datasets in a specific order and technique.
Each category captures essential dimensions of sentiment analysis, guiding 
researchers to examine studies comprehensively and fostering a standardized approach 
to classification. For instance, the “Turkish Multidomain Products Reviews"dataset, 
one of the datasets used in Demirtas and Pechenizkiy (2013) study, includes posi­
tive and negative comments received from Hepsiburada.com. This dataset is an ideal 
example for applying (Rodrigues et al., 2018)’s taxonomy. This dataset includes the 
detection of regular opinions expressed in texts such as “çok iyi sese sahip bir olan bir 
kulaklık. alalı neredeyse 1 yıl oldu hiç bir sorunum yok. verilen paraya değer."(EN: 
A headphone with a very good sound. I bought it almost a year ago and I have no 
1 3
4007

--- Page 6 ---

Ş. Çakıcı et al.
problems. It is worth the money.), and this sentence expresses a positive emotion. In 
applying the taxonomy specifically to the dataset used in Demirtas and Pechenizkiy 
(2013) study, the label “Regular"(O1) is assigned under Opinion Detection because 
the reviews reflect straightforward opinions about products, rather than comparisons. 
For Opinion Holder, “Text Author"(E1) is selected as the opinions are written directly 
by customers, and “Third Person"(E2) is included for instances where reviewers refer 
to others’ experiences (e.g., family or friends). Under Target Analysis, “Product"(E4) 
is used because the reviews are about specific products such as headphones, while 
“Organization"(E5) applies as the reviews often implicitly evaluate Hepsiburada, the 
platform providing the products. For Target Class, “Polarity"(T2) is assigned since 
the dataset classifies reviews into positive or negative sentiments, a clear binary clas­
sification. Under Data Specificity, “Language"(D1) is selected because the dataset is 
in Turkish, and “Application Domain"(D2) reflects the focus on e-commerce, spe­
cifically product reviews. Regarding Granularity, “Sentence"(G2) is chosen because 
the sentiment analysis is performed at the sentence level to capture the opinions 
expressed in each statement. Finally, ’Supervised Learning’ (A7) under Approach is 
selected because labeled data was used to train machine learning models for senti­
Table 1  A Taxonomy of Sentiment Analysis Classification from Rodrigues (2018)
Opinion 
Detection
Regular
O1
Comparative
O2
Entity
Identification
Opinion Holder
Text Author
E1
Third Person
E2
Problem
Target Analysis
Person
E3
Object
E4
Organization
E5
Target
Class
Subjectivity
T1
Polarity
T2
Emotion
T3
Data
Specificity
Language
D1
Application 
Domain
D2
Sentiment 
Analysis
Method
Granularity
Analysis
Phrase
G1
Sentence
G2
Aspect
G3
Paragraph
G4
Word
G5
Document
G6
Approach
Lexicon Based
Dictionary Based
A1
Corpus Based
Statistical
A2
Semantic
A3
Concept Based
Ontology
A4
Semantic Network
A5
Machine
Learning Based
Unsupervised
A6
Supervised
A7
Semi-Supervised
A8
1 3
4008

--- Page 7 ---

A cross-validation study of Turkish sentiment analysis datasets and…
ment classification. These labels, applied specifically to the Turkish Multidomain 
Products Reviews dataset in Demirtas and Pechenizkiy (2013) study, systematically 
define its characteristics and enable structured comparisons within the field of senti­
ment analysis. These steps were continued and a label was assigned for each study as 
presented in Table 2.
In Table 2, we label and present the distribution of these taxonomy categories 
for the 78 studies published between 2012 and 2025, aiming to enhance readability 
and facilitate efficient comparison. Each row in the Table 2 represents an individual 
study, and each column corresponds to the labels assigned in Table 1. This tabulation 
enables researchers to swiftly identify patterns and trends across studies, offering a 
condensed yet insightful overview of the sentiments explored in Turkish sentiment 
analysis. With the insights gained from Table 2, it becomes apparent that the concept-
based approach is infrequently used in these studies, with a prevalent focus on regular 
type opinion detection which is O1. The concept-based approach, involving a more 
nuanced understanding of sentiments, is overshadowed by the simplicity and effec­
tiveness of regular-type opinion detection.
2.1  Datasets
To comprehensively explore sentiment analysis studies in the Turkish language, a 
thorough investigation was conducted on research papers related to ‘sentiment analy­
sis’ and ‘Turkish dataset’ indexed on Scopus.2.
This initial search yielded 104 papers. Of these, 9 were inaccessible despite insti­
tutional subscriptions and individual requests to the authors. Additionally, 27 papers 
were excluded for being outside the scope of our review. These included studies that 
did not perform sentiment analysis (e.g., those focused solely on irony detection or 
topic classification), utilized languages other than Turkish (e.g., Kazakh), or lacked 
polarity/emotion labeling (e.g., aspect-only classification studies such as Deniz et al. 
(2022).
Furthermore, we included seven additional studies that were not retrieved through 
the original query but are commonly cited and considered central to the field. We 
also incorporated three more relevant papers published during the review process. 
As illustrated in the PRISMA flow diagram (Fig. 1), (Haddaway et al., 2022), a total 
of 78 studies were included in the final synthesis: 68 identified through systematic 
screening of Scopus records and 10 manually selected based on backward citation 
tracking and expert relevance.
To ensure consistency and relevance, we applied clear inclusion criteria. This 
study includes only Turkish-language sentiment analysis papers that either apply a 
classification model on labeled Turkish datasets and report performance metrics, or 
contribute novel Turkish sentiment-labeled datasets that are suitable for future mod­
eling tasks.
2 Search conducted in the Scopus database using the following query: (TITLE-ABS-KEY (sentiment 
AND analysis) AND TITLE-ABS-KEY (turkish AND dataset)) AND (LIMIT-TO (DOCTYPE,"cp") OR 
LIMIT-TO (DOCTYPE,"ar") OR LIMIT-TO (DOCTYPE,"ch")) The search included all available years 
and was limited to conference papers, articles, and book chapters.
1 3
4009

--- Page 8 ---

Ş. Çakıcı et al.
Dictionary construction papers were excluded unless the constructed resource was 
directly applied to a sentiment-labeled dataset, and the dataset was reused in subse­
quent applications (e.g., Ucan et al. (2016), which was later utilized by Acikalin et al. 
(2020). Studies focused solely on lexicon generation, without any applied classifica­
tion or evaluation, were not considered in the final taxonomy table. Although (Alti­
nok, 2023) does not involve model-based sentiment classification, it was included in 
the taxonomy table due to its contribution of large-scale Turkish sentiment-labeled 
datasets, which are openly available and suitable for future modeling efforts.
Subsequently, over 80 distinct datasets were identified across 78 Turkish senti­
ment analysis studies. Among these, 43 study have publicly available datasets, and 
23 study were reused datasets from prior publications, reflecting both the scarcity of 
Turkish-language resources and a growing culture of data sharing. These datasets 
were compiled and systematically organized within a GitHub repository.3 Table 3 
provides a detailed overview of the included studies, encompassing attributes such as 
study link, dataset name (with download link if available), datset source, availability 
and contact mail.
Overall, Table 3 functions as a central reference, offering a consolidated snapshot 
of methodological practices and dataset usage across the field. This compilation not 
only facilitates a nuanced understanding of the research landscape but also lays the 
groundwork for future comparative assessments and longitudinal analyses in Turkish 
sentiment analysis research.
Figure 2 presents a heatmap visualization that illustrates the yearly frequency of 
each taxonomy label. The X-axis corresponds to taxonomy labels (O1–A8), while 
the Y-axis represents publication years. Each cell shows the number of studies tagged 
with that specific label in the corresponding year.
This visualization reveals several important trends. First, the volume and diver­
sity of labeled studies increased significantly after 2018. Notably, labels such as O1 
(Opinion Mining), E1–E5 (Emotion categories), and A1–A7 (Analysis targets) appear 
more frequently in recent years. Additionally, the expansion of document types (D1–
D2) and granularities (G1–G6) reflects an increased methodological complexity and 
dataset richness in Turkish sentiment analysis. The peak years of taxonomy usage 
were 2019 and 2024, suggesting growing academic interest and diversification of 
research objectives.
While our investigation encompasses various datasets, our study particularly 
focuses on four datasets that were recurrently utilized in multiple publications in 
the Turkish language. Brief descriptions, contents, and classification types of five 
datasets are as follows: The Turkish Movie Reviews Dataset (TMRD), and The Turk­
ish Multidomain Products Reviews (TMPR), were prepared by Demirtas and Pech­
enizkiy (2013). Notably, these datasets have found application in three additional 
studies by Parlar and Özel (2016), Mulki et al. (2018), and Alqaraleh (2021). TMRD 
encompasses comments and reviews gathered from beyazperde.com, while TMPR 
consists of comments and reviews collected from hepsiburada.com. Both datasets 
are tailored for binary classification, with TMRD comprising 5331 positive and 5331 
negative instances, and TMPR presenting an equal distribution of 2800 positive and 
3 https://github.com/sevvalckc/Turkish-SAD
1 3
4010

--- Page 9 ---

A cross-validation study of Turkish sentiment analysis datasets and…
Studies
O1
O2
E1
E2
E3
E4
E5
T1
T2
T3
D1
D2
G1
G2
G3
G4
G5
G6
A1
A2
A3
A4
A5
A6
A7
A8
Demirtas and Pechenizkiy (2013)
X
X
X
X
X
X
X
X
Çetin and Amasyali (2013)
X
X
X
X
X
X
X
X
Isgüder Sahin et al. (2014)
X
X
X
X
X
X
X
X
X
Türkmenoglu and Tantug (2014)
X
X
X
X
X
X
X
X
X
Çoban et al. (2015)
X
X
X
X
X
X
X
X
X
Ekinci et al. (2016)
X
X
X
X
X
X
X
X
X
X
Ogul and Ercan (2016)
X
X
X
X
X
X
X
X
X
X
Parlar and Özel (2016)
X
X
X
X
X
X
X
X
X
Ucan et al. (2016)
X
X
X
X
X
X
X
X
X
Ayata et al. (2017)
X
X
X
X
X
X
X
X
X
Parlar et al. (2017)
X
X
X
X
X
X
X
X
X
Hayran and Sert (2017)
X
X
X
X
X
X
X
X
X
Omurca et al. (2017)
X
X
X
X
X
X
X
X
X
Mulki et al. (2018)
X
X
X
X
X
X
X
X
X
X
Yüksel and Tan (2018)
X
X
X
X
X
X
X
X
X
X
X
X
Ay Karakus et al. (2018)
X
X
X
X
X
X
X
X
X
X
Yurtalan et al. (2019)
X
X
X
X
X
X
X
X
X
X
X
X
Amasyali et al. (2018)
X
X
X
X
X
X
X
X
X
Ciftci and Apaydin (2018)
X
X
X
X
X
X
X
X
X
X
Çoban and Özyer (2018)
X
X
X
X
X
X
X
X
X
X
Ogul and Güran (2019)
X
X
X
X
X
X
X
X
X
X
Uslu et al. (2019)
X
X
X
X
X
X
X
X
X
X
X
Akin and Yildiz (2019)
X
X
X
X
X
X
X
X
X
X
Santur (2019)
X
X
X
X
X
X
X
X
X
X
Rumelli et al. (2019)
X
X
X
X
X
X
X
X
X
X
X
Shehu et al. (2019)
X
X
X
X
X
X
X
X
X
X
X
Ersahin et al. (2019)
X
X
X
X
X
X
X
X
X
X
X
Karamollaoglu et al. (2019)
X
X
X
X
X
X
X
X
X
Table 2  Studies labelled with sentiment analysis taxonomy classification
1 3
4011

--- Page 10 ---

Ş. Çakıcı et al.
Studies
O1
O2
E1
E2
E3
E4
E5
T1
T2
T3
D1
D2
G1
G2
G3
G4
G5
G6
A1
A2
A3
A4
A5
A6
A7
A8
Bayraktar et al. (2019)
X
X
X
X
X
X
X
X
X
X
X
Demirci et al. (2019)
X
X
X
X
X
X
X
X
X
X
Güven et al. (2020)
X
X
X
X
X
X
X
X
X
Shehu and Tokat (2019)
X
X
X
X
X
X
X
X
X
X
Kilimci (2020)
X
X
X
X
X
X
X
X
X
X
Kilimci et al. (2020)
X
X
X
X
X
X
X
X
X
X
Sigirci et al. (2020)
X
X
X
X
X
X
X
X
X
Acikalin et al. (2020)
X
X
X
X
X
X
X
X
X
X
X
Alqaraleh (2021)
X
X
X
X
X
X
X
X
X
X
Kiliç and Büyükeke (2021)
X
X
X
X
X
X
X
X
X
X
Eker et al. (2021)
X
X
X
X
X
X
X
X
Salur and Aydin (2021)
X
X
X
X
X
X
X
X
X
Aydin and Güngör (2021)
X
X
X
X
X
X
X
X
X
X
X
X
X
Zeybek et al. (2021)
X
X
X
X
X
X
X
X
X
X
Shehu et al. (2021)
X
X
X
X
X
X
X
X
X
X
Köksal and Özgür (2021)
X
X
X
X
X
X
X
X
Kemaloglu et al. (2021)
X
X
X
X
X
X
X
X
X
Aydin et al. (2021)
X
X
X
X
X
X
X
X
X
Aygün et al. (2021)
X
X
X
X
X
X
X
X
X
X
X
Aydogan and Kocaman (2023)
X
X
X
X
X
X
X
X
X
X
Balli et al. (2022)
X
X
X
X
X
X
X
X
X
X
Mutlu and Özgür (2022)
X
X
X
X
X
X
X
X
X
X
X
Kabakus (2022)
X
X
X
X
X
X
X
X
X
X
X
X
Guven (2022)
X
X
X
X
X
X
X
X
Erkan and Güngör (2023)
X
X
X
X
X
X
X
X
X
X
X
Alnahas et al. (2022)
X
X
X
X
X
X
X
X
X
X
Karayigit et al. (2022)
X
X
X
X
X
X
X
X
X
X
X
X
Table 2  (continued)
 
1 3
4012

--- Page 11 ---

A cross-validation study of Turkish sentiment analysis datasets and…
Studies
O1
O2
E1
E2
E3
E4
E5
T1
T2
T3
D1
D2
G1
G2
G3
G4
G5
G6
A1
A2
A3
A4
A5
A6
A7
A8
Demir and Bilgin (2023)
X
X
X
X
X
X
X
X
X
X
Abdellatif et al. (2023)
X
X
X
X
X
X
X
X
X
X
Altinok (2023)
X
X
X
X
X
Tohma et al. (2023)
X
X
X
X
X
X
X
X
X
Aydin et al. (2019)
X
X
X
X
X
X
X
X
X
X
X
X
Yilmaz and Altunay (2023)
X
X
X
X
X
X
X
X
X
Ezin et al. (2024)
X
X
X
X
X
X
X
X
X
X
X
Özdemir et al. (2024)
X
X
X
X
X
X
X
X
X
Kiziltepe et al. (2024)
X
X
X
X
X
X
X
X
X
X
Polat et al. (2024)
X
X
X
X
X
X
X
X
X
X
X
X
Alawi and Bozkurt (2024c)
X
X
X
X
X
X
X
Alawi and Bozkurt (2024b)
X
X
X
X
X
X
X
X
X
Nasution and Onan (2024)
X
X
X
X
X
X
X
X
X
X
Onan and Balbal (2024)
X
X
X
X
X
X
X
X
X
X
X
Bozuyla (2024)
X
X
X
X
X
X
X
X
X
X
Cam et al. (2024)
X
X
X
X
X
X
X
X
X
Alawi and Bozkurt (2024)
X
X
X
X
X
X
X
X
X
X
Najafi and Varol (2024)
X
X
X
X
X
X
X
X
X
X
Zümberoglu et al. (2025)
X
X
X
X
X
X
X
X
X
X
Özmen and Gündüz (2025)
X
X
X
X
X
X
X
X
X
X
X
Kaya et al. (2012)
X
X
X
X
X
X
X
X
X
X
X
X
Saglam et al. (2016)
X
X
X
X
X
X
X
X
X
X
X
X
Makinist et al. (2018)
X
X
X
X
X
X
X
X
X
Total count
77
1
78
7
5
64
32
1
76
4
78
75
2
73
4
2
18
12
29
53
3
1
2
12
59
2
Table 2  (continued)
 
1 3
4013

--- Page 12 ---

Ş. Çakıcı et al.
2800 negative instances. We predict instances of these two datasets using aforemen­
tioned four models. The datasets were combined into a single dataset, referred to as 
TMRD-TMPR in our paper.
In addition to the aforementioned datasets, our study also incorporates the Twitter 
Dataset prepared by Türkmenoglu and Tantug (2014). The Twitter Dataset is com­
posed of tweets collected from Twitter and adhere to a binary classification format 
and includes 1677 positive and 1301 negative instances. Türkmenoglu and Tantug 
Fig. 1  PRISMA 2020 flow diagram summarizing the inclusion process
 
1 3
4014

--- Page 13 ---

A cross-validation study of Turkish sentiment analysis datasets and…
References
Dataset name
Data source
Document 
type
CF
Items
Best reported model
Metric
Metric score
Demirtas and 
Pechenizkiy 
(2013)
Turkish Movie 
Reviews Dataset
Beyazperde.com
Comment
BC
Pos: 5331 
Neg: 5331
Turkish Multi­
domain Products 
Reviews
Hepsiburada.com
Comment
BC
Pos: 2800 
Neg: 2800
Çetin and 
Amasyali 
(2013)
Telecom Dataset A
Twitter
Tweet
TC
Pos: 3040 
Neg: 1847 
Neu: 1113
SMO + RF (char 
n-grams)
Accuracy
.655
Telecom Dataset B
Twitter
Tweet
TC
Pos: 2680 
Neg: 2316 
Neu: 1004
SMO + RF (char 
n-grams)
Accuracy
.653
Isgüder Sahin 
et al. (2014)
Ekşi Sözlük Tech­
nology Brand Com­
ments Dataset
Ekşi Sözlük
Comment
BC
Pos: 867 
Neg: 912
SVM
F-Measure
.696
Türkmenoglu 
and Tantug 
(2014)
Twitter Dataset
Twitter
Tweet
BC
Pos: 1677 
Neg: 1301
SVM
Accuracy
.85
Movie Dataset
Beyazperde.com
Comment
BC
Pos: 13,224 
Neg: 7020
SVM
Accuracy
.895
Çoban et al. 
(2015))
Twt
Twitter
Tweet
BC
Pos: 1000 
Neg: 1000
MNB
Accuracy
.66
Ekinci et al. 
(2016)
Turkcell Twitter 
Dataset
Twitter
Tweet
TC
Pos: 684 
Neg: 720 
Neu: 599
SVM-RF
Accuracy
max:.62
TTNet Twitter 
Dataset
Twitter
Tweet
TC
Pos: 640 
Neg: 716 
Neu: 656
SVM-RF
Accuracy
max:.55
Ogul and 
Ercan (2016)
Hotel Reviews 
Dataset
Booking.com, Tripadvi­
sor.com
Comment
BC
Pos: 128 
Neg: 203
Random Forest
AUC
.89
Table 3  Summary information of datasets, the best performing model, and accuracy score according to the cited paper are reported
1 3
4015

--- Page 14 ---

Ş. Çakıcı et al.
References
Dataset name
Data source
Document 
type
CF
Items
Best reported model
Metric
Metric score
Parlar and 
Özel (2016)
Turkish Multi­
domain Products 
Reviews
Hepsiburada.com
Comment
BC
Pos: 2800 
Neg: 2800
NBM
F-Score
.8042
Ucan et al. 
(2016)
Movie Review
Beyazperde.com
Comment
BC
Pos: 26,700 
Neg: 26,700
TSDp
Accuracy
.807
Hotel Review
Otelpuan.com
Comment
BC
Pos: 5800 
Neg: 5800
SWN
Accuracy
.846
Ayata et al. 
(2017)
Retail Tweets
Twitter
Tweet
BC
Pos: 865 
Neg: 842
SVM
Accuracy
.6368
Telecom Tweets 
(KemikA)
Twitter
Tweet
BC
Pos: 1287 
Neg: 756
SVM
Accuracy
.7386
Football Tweets
Twitter
Tweet
BC
Pos: 833 
Neg: 507
SVM
Accuracy
.8402
Banking Tweets
Twitter
Tweet
BC
Pos: 604 
Neg: 114
SVM
Accuracy
.8997
Parlar et al. 
(2017)
Turkish Twitter 
Dataset
Twitter (Telecom 
Company)
Tweet
TC
Pos: 1021 
Neg: 1022
MEM (with KKO)
F-Score
.7888
Hayran and 
Sert (2017)
Turkish Sentiment 
Dataset
Twitter
Tweet
BC
Pos: 16,000 
Neg: 16,000
Dvot
Accuracy
.8005
Omurca et al. 
(2017)
Turkish Hotel 
Review Dataset
Otelpuan.com
Comment
SA
1000 re­
views, 5364 
sentences
–
–
–
Mulki et al. 
(2018)
Turkish Movie 
Reviews Dataset
Beyazperde.com
Comment
BC
Pos: 5331 
Neg: 5331
NB
Accuracy
.928
Turkish Multi­
domain Products 
Reviews
Hepsiburada.com
Comment
BC
Pos: 2800 
Neg: 2800
NB
Accuracy
Kitchen:.85 
DvD:.814 
Electronic:.857 
Books:.886
Table 3  (continued)
 
1 3
4016

--- Page 15 ---

A cross-validation study of Turkish sentiment analysis datasets and…
References
Dataset name
Data source
Document 
type
CF
Items
Best reported model
Metric
Metric score
Yüksel and 
Tan (2018)
Foursquare Venue 
and Venue Com­
ments Data
Foursquare
Comment
BC
Total: 7086
RT-SKDA
Accuracy
.8197
Ay Karakus et 
al. (2018)
Turkish Movie 
Reviews
Beyazperde.com
Comment
BC
Total: 44,617
CNN-LSTM+PWE
Accuracy
.9807
Yurtalan et al. 
(2019)
Aziz Sancar Twitter 
Dataset
Twitter
Tweet
TC
Total: 300
Lexicon-based System
Accuracy
.882
Beşiktaş Twitter 
Dataset
Twitter
Tweet
TC
Total: 300
Lexicon-based System
Accuracy
.851
Arçelik Twitter 
Dataset
Twitter
Tweet
TC
Total: 500
Lexicon-based System
Accuracy
.823
Amasyali et 
al. (2018)
Twitter Dataset
Twitter
Tweet
TC
Pos: 4579 
Neg: 6886 
Neu: 5822
SDG
Success
.6925
Ciftci and 
Apaydin 
(2018)
Turkish Product 
Reviews
Hepsiburada.com
Comment
BC
Pos: 220,284 
Neg: 14,881
LSTM w/Word 
Embeddings
Accuracy
.829
Turkish Movie 
Reviews
Beyazperde.com
Comment
BC
Pos: 62,386 
Neg: 57,544
LSTM w/Word 
Embeddings
Accuracy
.829
Çoban and 
Özyer (2018)
VS1
Twitter
Tweet
TC
Pos: 756 
Neg: 1,287 
Neu: 957
BoW
Accuracy
.5384
VS2 (Turkish Senti­
ment Dataset)
Twitter
Tweet
BC
Pos: 16,000 
Neg: 16,000
BoW
Accuracy
.7221
Ogul and 
Güran (2019))
VS2
Twitter
Tweet
TC
Pos: 4579 
Neg: 6886 
Neu: 5822
SMOTE
Accuracy
.6859
Uslu et al. 
(2019)
Movie Comments 
(YTÜ/Kemik)
kemik.yildiz.edu.tr
Comment
BC
Total: 300
Logistic Regression
Accuracy
.661
Table 3  (continued)
 
1 3
4017

--- Page 16 ---

Ş. Çakıcı et al.
References
Dataset name
Data source
Document 
type
CF
Items
Best reported model
Metric
Metric score
Beyazperde Movie 
Comments – 5K
Beyazperde.com
Comment
BC
Total: 5,000
Logistic Regression
Accuracy
.735
Beyazperde Movie 
Comments – 10K
Beyazperde.com
Comment
BC
Total: 10,000
Logistic Regression
Accuracy
.7427
Beyazperde Movie 
Comments – 20K
Beyazperde.com
Comment
BC
Total: 20,000
Logistic Regression
Accuracy
.7735
Akin and 
Yildiz (2019)
Restaurant Dataset
Online
Comment
BC
Total: 756
with-TL
Accuracy
.901
Product Dataset
Online
Comment
BC
Pos: 220,284 
Neg: 14,881
with-TL
Accuracy
.834
Santur (2019)
Hepsiburada Re­
views Dataset
Kaggle 
(hepsi-burada-yorum)
Comment
BC
Pos: 229,821 
Neg: 13,676
GRU
Accuracy
.955
Rumelli et al. 
(2019)
Sentiment Analysis 
Twitter Dataset
Hepsiburada.com
Comment
BC
Pos: 221,071 
Neg: 13,012
kNN
Accuracy
.738
Shehu et al. 
(2019)
Dataset
Twitter
Tweet
TC
Total: 3,000 
and 10,500
RF
Accuracy
.885
Ersahin et al. 
(2019)
Movie Review
Beyazperde.com
Comment
BC
Pos: 26,700 
Neg: 26,700
Hybrid (SVM+eSTN)
Accuracy
.8631
Hotel Review
Otelpuan.com
Comment
BC
Pos: 5,800 
Neg: 5,800
Hybrid (SVM+eSTN)
Accuracy
.9196
Tweets Dataset
Twitter
Tweet
BC
Total: 1,756
Hybrid (NB+eSTN)
Accuracy
.8337
Karamol­
laoglu et al. 
(2019)
Turkish Tweets 
Dataset
Twitter
Tweet
BC
Train: 200 
Pos, 200 Neg 
Test: 100 Pos, 
100 Neg
Vector Space Model
Accuracy
.84
Table 3  (continued)
 
1 3
4018

--- Page 17 ---

A cross-validation study of Turkish sentiment analysis datasets and…
References
Dataset name
Data source
Document 
type
CF
Items
Best reported model
Metric
Metric score
Bayraktar et 
al. (2019)
Turkish Restaurant 
Dataset (SemEval 
2016)
SemEval ABSA 2016
Sentence
AC + PC
Train: 1232, 
Test: 144
Rule-Based System
F1 (Aspect Ex­
traction):.5628/
Accuracy 
(Sentiment 
Mapping):.5205
Demirci et al. 
(2019)
15 Temmuz Coup 
Tweets Dataset
Twitter (15Temmuz, 
2016–2017)
Tweet
BC
Total: 3,000 
(Train: 2,500/
Test: 500)
Deep Learning (NN with 
Dense+Dropout)
Accuracy
.8186
Güven et al. 
(2020)
Dataset
Twitter
Tweet
EC
Happy: 800 
Sad: 800 
Shocked: 800 
Fear: 800 
Angry: 800
GAA
Accuracy
.87
Shehu et al. 
(2019)
Turkish Tweets 
Dataset (Small)
Twitter
Tweet
TC
Total: 3000 
(Balanced)
Hybrid (SVM + RF)
Accuracy
.864
Turkish Tweets 
Dataset (Large)
Twitter
Tweet
TC
Total: 10,500 
(Balanced)
Hybrid (SVM + RF)
Accuracy
.828
Kilimci (2020) Turkish Financial 
Tweets
Twitter
Tweet
TC
Pos: 7844 
Neg: 20,172 
Neu: 2130
LSTM
Accuracy
.7842
Kilimci et al. 
(2020)
Hitman
Google Play Store
Comment
BC
Pos: 17,694 
Neg: 3082
FastText
Accuracy
.886
Soccer Manager
Google Play Store
Comment
BC
Pos: 3165 
Neg: 2546
FastText
Accuracy
.778
GTA San Andreas
Google Play Store
Comment
BC
Pos: 3343 
Neg: 1503
FastText
Accuracy
.830
City Driving 3D
Google Play Store
Comment
BC
Pos: 7331 
Neg: 3380
FastText
Accuracy
.767
Sigirci et al. 
(2020)
Turkish Google 
Play Reviews
Google Play Store
Comment
BC
 2 M
BERT
Accuracy
–
Table 3  (continued)
 
1 3
4019

--- Page 18 ---

Ş. Çakıcı et al.
References
Dataset name
Data source
Document 
type
CF
Items
Best reported model
Metric
Metric score
Acikalin et al. 
(2020)
Movie Review
Beyazperde.com
Comment
BC
Pos: 26,700 
Neg: 26,700
BERT
Accuracy
.9134
Hotel Review
Otelpuan.com
Comment
BC
Pos: 5800 
Neg: 5800
fastText-EN
Accuracy
.8080
Alqaraleh 
(2021)
Turkish Movie 
Reviews
Beyazperde web pages
Comment
BC
Total: 34,990
SA system
Accuracy
.8329
Kiliç and 
Büyükeke 
(2021)
TripAdvisor
TripAdvisor
Comment
TC
Total: 2000 
(approx.)
Text-GCN
Accuracy
.8786
BlogPosts
Turkish Blogs
Comment
TC
Total: 2000 
(approx.)
Text-GCN
Accuracy
.8613
IMDB Reviews
IMDB
Comment
TC
Total: 2000 
(approx.)
Text-GCN
Accuracy
.8774
Eker et al. 
(2021)
Dataset
Twitter
Tweet
EC
Happy: 800 
Sad: 800 
Shocked: 800 
Fear: 800 
Angry: 800
BiLSTM-RNN
Accuracy
.952
Salur and 
Aydin (2021)
Turkish Tourism 
ABSA Dataset
TripAdvisor
Comment
TC
Aydin and 
Güngör (2021)
Movie Dataset
Beyazperde.com
Comment
BC
Pos: 13,224 
Neg: 7020
SVM
Accuracy
.9098
Twitter Dataset
Twitter
Tweet
BC
Pos: 743 
Neg: 973
SVM
Accuracy
.7964
Zeybek et al. 
(2021)
Turkish Movie 
Reviews Dataset
Beyazperde.com
Comment
BC
Pos: 5,331 
Neg: 5,331
RNTN
Accuracy
.8984
Table 3  (continued)
 
1 3
4020

--- Page 19 ---

A cross-validation study of Turkish sentiment analysis datasets and…
References
Dataset name
Data source
Document 
type
CF
Items
Best reported model
Metric
Metric score
Turkish Multi­
domain Products 
Reviews
Hepsiburada.com
Comment
BC
Pos: 2800 
Neg: 2800
RNTN
Accuracy
Books:.8608 
DVD:.8295 
Electr.8295 
Electr.:.8666 
Kitchen:.8173
Shehu et al. 
(2021)
Dataset 1
Twitter
Tweet
TC
Pos: 1000 
Neg: 1000 
Neu: 1000
HAN
Accuracy
.8996
Dataset 2
Twitter
Tweet
TC
Pos: 3500 
Neg: 3500 
Neu: 3500
HAN
Accuracy
.8996
Köksal and 
Özgür (2021)
BounTi
Twitter
Tweet
TC
Total: 7964
BERTurk
Accuracy
.0745
Kemaloglu et 
al. (2021)
Twitter Dataset
Twitter
Tweet
TC
Pos: 5712 
Neg: 11,567 
Neu: 11,247
LSTM
Accuracy
.8446
Aydin et al. 
(2021)
Tweets on Open and 
Distance Education 
(ODE)
Twitter
Tweet
TC
Neg: 1075 
Neu: 3345 
Pos: 232
Logistic Regression 
(TF-IDF)
F-score
.7584
Aygün et al. 
(2021)
Turkish Data from 
Banda Dataset
Twitter
Tweet
BC
Total: 
928,402
BERTurk
Accuracy
.89
Aydogan and 
Kocaman 
(2023)
TRSAv1
Online shopping sites
Comment
TC
Total: 
150,000 
(50,000 
per neutral, 
positive, 
negative)
B-LSTM with GloVe
Accuracy
.8361
Balli et al. 
(2022)
SentimentSet 
Dataset
Twitter
Tweet
TC
Total: 2551
LSTM
Accuracy
.86
Public Dataset
Twitter
Tweet
BC
Total: 11,000
LSTM
Accuracy
.86
Table 3  (continued)
 
1 3
4021

--- Page 20 ---

Ş. Çakıcı et al.
References
Dataset name
Data source
Document 
type
CF
Items
Best reported model
Metric
Metric score
Mutlu and 
Özgür (2022)
Twitter Dataset
Twitter
Tweet
TC
3,952
T-BERTmarked-MP
F-1 Score
.669
Kabakus 
(2022)
COVID-19 Dataset
Twitter
Tweet
TC
Pos: 3,290 
Neg: 852 
Neu: 45,802
Proposed Model
Accuracy
.952
Guven (2022)
Hotel Review 
Dataset
Otelpuan.com
Comment
BC
Pos: 5,800 
Neg: 5,800
ELECTRA-Tr (w/TFM 
k=10)
Accuracy
.9838
Movie Review 
Dataset
Beyazperde.com
Comment
BC
Pos: 26,700 
Neg: 26,700
ELECTRA-Tr (w/TFM 
k=10)
Accuracy
.9221
Erkan and 
Güngör (2023)
Beyazperde Movie 
Reviews
Beyazperde.com
Comment
BC
Pos: 26,700 
Neg: 26,700
RoBERTa 
(XLM-RoBERTa)
Accuracy
.9439
Semeval Turkish 
Restaurant Reviews
Semeval 2016 Task 5
Comment
TC
Three-class 
distribution
RoBERTa 
(XLM-RoBERTa)
Accuracy
.8473
Alnahas et al. 
(2022)
Dataset
E-Commerce Websites
Comment
TC
Total: 
602,202
Suggested Ensemble 
Model
F-1 Score
.847
Karayigit et 
al. (2022)
Dataset1
Instagram
Comment
TC
Pos: 671 
Neg: 1473 
Neu: 743
BERT-based transfer 
learning model
Accuracy
.7864
Dataset2
Instagram
Comment
TC
Pos: 2,074 
Neg: 1564 
Neu: 3183
BERT-based transfer 
learning model
Accuracy
.7120
Demir and 
Bilgin (2023)
Turkish News Senti­
ment Dataset
Turkish News Websites
News
BC
Pos: 2,050 
Neg: 2950
RoBERTa
Accuracy
.80
TR-News Headlines 
Dataset
Turkish News Titles
News Title
BC
Total: 
100,000 
(auto-labeled)
RoBERTa
Accuracy
.84
Abdellatif et 
al. (2023)
Multilingual Senti­
ment Dataset (TR 
subset)
Twitter, Hepsiburada
Tweet, 
Review
BC
Total: 50,000 
(TR)
LSTM (BERT+LSTM 
pipeline)
Accuracy
.887 (via 
Yandex 
translation)
Table 3  (continued)
 
1 3
4022

--- Page 21 ---

A cross-validation study of Turkish sentiment analysis datasets and…
References
Dataset name
Data source
Document 
type
CF
Items
Best reported model
Metric
Metric score
Altinok (2023) Beyazperde Movie 
Reviews Dataset
Beyazperde.com
Comment
SC
 45,000
–
–
–
Beyazperde Top 300 
Movies Dataset
Beyazperde.com
Comment
SC
 54,000
–
–
–
Vitamins and Sup­
plements Dataset
Vitaminler.com
Comment
SC
 244,000
–
–
–
Tohma et al. 
(2023)
SCD (Q-A Dataset)
Human-Robot Interac­
tion (Created by 
Authors)
Q-A Pair
BC
Pos: 6750 
Neg: 6750
LinearSVM
Accuracy
.9105
DS1
Twitter
Tweet
BC
Total: 11,119
LinearSVM
Accuracy
.8725
SentimentSet
Twitter
Tweet
BC
Total: 2,600
LinearSVM
Accuracy
.8615
Aydin et al. 
(2019)
Movie Review 
Corpus
Beyazperde.com
Comment
BC
Pos: 7020 
Neg: 7020
Supervised 4-scores + 
3-feats
Accuracy
.9038
Telecom Tweets
Twitter
Tweet
BC
Pos: 743 
Neg: 973
Supervised 4-scores + 
3-feats
Accuracy
.7800
Yilmaz and 
Altunay 
(2023)
Mobile Phone 
Reviews Dataset
Trendyol, Hepsiburada, 
N11, GittiGidiyor, 
Amazon Türkiye
Comment
TC
Total: 6,081 
→ Cleaned: 
3,212
Lexicon-Based Approach
Sentiment Score –
Ezin et al. 
(2024)
TRSAv1 Dataset
Turkish e-commerce 
platforms
Comment
TC
Pos: 50,000 
Neg: 50,000 
Neu: 50,000
ChatGPT-4o (LLM 
relabelled)
Accuracy
.887
VSCR Dataset
Vitamins-Supplements 
Reviews
Comment
SC
Total: 
244,000 (1-5 
stars)
ChatGPT4-o (LLM 
relabeled)
Accuracy
.862
Özdemir et al. 
(2024)
Turkish Hotel Re­
views (Translated)
Booking Platforms
Comment
BC
Total: 5000
TURNA
Accuracy
.994
Kiziltepe et al. 
(2024)
VSCR
Online Supplement 
Reviews
Comment
TC
Total: 
244,866
SVM
Accuracy
.9631 (Bi­
nary),.9214 
(Multi-class)
Table 3  (continued)
 
1 3
4023

--- Page 22 ---

Ş. Çakıcı et al.
References
Dataset name
Data source
Document 
type
CF
Items
Best reported model
Metric
Metric score
TRSAv1
Turkish E-commerce 
Reviews
Comment
TC
Total: 
150,000
SVM
Accuracy
.9511 (Bi­
nary),.8011 
(Multi-class)
Polat et al. 
(2024)
Couple Dialogue
Collected via lab-based 
couple recordings
Dialogue 
(Utterance)
TC
Pos: 2083 
Neu: 6050 
Neg: 6161
DialogueRNN (FT 
BERT)
Weighted F1
+14.46% 
(contextual)
Alawi and 
Bozkurt 
(2024c)
Turkish University 
Tweets
Twitter (30 universities, 
April 2023)
Tweet
BC
Pos: 11,674 
Neg: 4,126
CNN-BiLSTM
Accuracy
.8725
Alawi and 
Bozkurt 
(2024b)
THED (Twitter/X)
Twitter (X)
Tweet
BC
Pos: 13,219 
Neg: 4,574
CNN-BiLSTM
F1 Score
.8392
HRD (Hotel 
Reviews)
Public Dataset (from 
Ucan et al. (2016) )
Comment
BC
Pos: 5,800 
Neg: 5,800
CNN-BiLSTM
F1 Score
.9543
Nasution and 
Onan (2024)
Turkish NLP 
Datasets
News articles, Twitter, 
Literary texts
Mixed 
(News, 
Tweet, 
Literary)
TC/BC/EC
60,000 
(DTC), 
50,000 
(DTSA), 
40,000 
(DEC)
ChatGPT-4
F1
Up to.92
Onan and Bal­
bal (2024)
TRSAv1
Online shopping sites
Comment
TC
Pos: 50,000 
Neg: 50,000 
Neu: 50,000
BERT-Large-ITPT
Accuracy
.9145
Bozuyla 
(2024)
Turkish Drug Re­
views Dataset
Eksisozluk.com + 
Drugs.com (translated)
Comment
TC
Pos: 8,120 
Neg: 3,385 
Neu: 1,013
BERTurk
W-F1
.951
Cam et al. 
(2024)
Financial Tweets 
Dataset
Twitter (#Borsaistan­
bul, #Bist, #Bist30, 
#Blist100)
Tweet
BC
Pos: 5,984 
Neg: 3,092
SVM
Accuracy
.89
Table 3  (continued)
 
1 3
4024

--- Page 23 ---

A cross-validation study of Turkish sentiment analysis datasets and…
References
Dataset name
Data source
Document 
type
CF
Items
Best reported model
Metric
Metric score
Alawi and 
Bozkurt 
(2024a)
Turkish Universities 
Satisfaction Dataset
Twitter
Tweet
BC
Pos: 13,219 
Neg: 4,574
BERT-BiLSTM-CNN
Accuracy
.9101
Najafi and 
Varol (2024)
VRLSentiment
Twitter
Tweet
TC
Pos: 5469 
Neu: 10,146 
Neg: 8,074
TurkishBERTweet + 
LoRA
Weighted-F1
.635
TSATweets
Twitter
Tweet
TC
Pos: 1,552 
Neu: 1,448 
Neg: 3,001
TurkishBERTweet + 
LoRA
Weighted-F1
.710
Kemik-17bin
Twitter
Tweet
TC
Pos: 4,579 
Neu: 5,822 
Neg: 6,888
TurkishBERTweet + 
LoRA
Weighted-F1
.757
Kemik-3000
Twitter
Tweet
TC
Pos: 756 
Neu: 957 
Neg: 1,287
TurkishBERTweet + 
LoRA
Weighted-F1
.661
BOUN
Twitter
Tweet
TC
Pos: 1,271 
Neu: 2,769 
Neg: 693
TurkishBERTweet + 
LoRA
Weighted-F1
.729
TSAD
Trendyol + Wikipedia
Comment
TC
Pos: 262,166 
Neu: 170,917 
Neg: 56,561
TurkishBERTweet + 
LoRA
Weighted-F1
.968
Zümberoglu et 
al. (2025)
FSMTSAD 
(Original)
Twitter, Product Re­
views, etc
Tweet + 
Comment
TC
Pos: 2333 
Neu: 2334 
Neg: 2333
Electra Base Turkish
Accuracy
.9064
FSMTSAD 
(Augmented)
Twitter, Product Re­
views, etc
Tweet + 
Comment
TC
Pos: 5284 
Neu: 5206 
Neg: 5363
Electra Base Turkish
Accuracy
.9064
Özmen and 
Gündüz 
(2025)
Trendyol Cosmetics 
Reviews
Trendyol.com
Comment
TC
Total: 
875,445
SVM
Accuracy
.93
Table 3  (continued)
 
1 3
4025

--- Page 24 ---

Ş. Çakıcı et al.
References
Dataset name
Data source
Document 
type
CF
Items
Best reported model
Metric
Metric score
Kaya et al. 
(2012)
Political Columns 
Dataset
Turkish News Sites
Column
BC
Pos: 200 
Neg: 200
N-gram LM
Accuracy
.7654
Saglam et al. 
(2016)
SWNetTR-PLUS 
Lexicon Evaluation 
Dataset (MLTC)
Turkish news from 
GDELT
News
BC
Pos: 265 
Neg: 235
Lexicon-Based
Accuracy
.722
Makinist et al. 
(2018)
Turkish Movie Re­
views (MCF-based)
Movie Review Site
Comment
BC
Total: 2,983
Not Reported
–
–
Note: CF Classification Format, BC Binary Classification, TC Tentary Classification, EC Emotion Classification, Pos Positive, Neg Negative, Neu Neutral
Table 3  (continued)
 
1 3
4026

--- Page 25 ---

A cross-validation study of Turkish sentiment analysis datasets and…
(2014) highlighted the effectiveness of Support Vector Machines (SVM) in the data­
set, achieving an accuracy of.85 for the Twitter Dataset. Notably, Aydin et al. (2021) 
utilized the same dataset in their study.
Furthermore, our study integrates the Twt dataset, prepared by Çoban et al. (2015). 
Comprising 2000 items, equally distributed with 1000 positive and 1000 negative 
instances, the Twt dataset is a unique addition to our analysis. This dataset was col­
lected by Çoban et al. (2015) using the Twitter API service. It is important to note 
that the Twt dataset, unlike others, lacks public access and has not been assigned a 
formal name. For our study, we will refer to it as the “Twt"dataset. The categorization 
of tweets as positive or negative in this dataset relies solely on emoticons, where “:)", 
“:D,"and similar expressions denote positivity, while “:(", “=(", “;("signify negativ­
ity. Following preprocessing steps, including the removal of hashtags, URLs, and 
usernames, the data were randomly collected without being constrained to a specific 
subject. Due to the temporal constraints of Twitter’s character limit at the time of 
data collection, posts were limited to 140 characters. Çoban et al. (2015) highlighted 
the effectiveness of Multinomial Naive Bayes (MNB) in Twt dataset, achieving an 
accuracy of.66 showcasing its unique characteristics and challenges. Furthermore, 
Kabakus (2022) utilized the same Twt dataset in their study.
Similarly, we will provide additional details about another dataset, referred to 
briefly as “Humir"as introduced by Ucan et al. (2016). The dataset acquisition pro­
cess involved the selection of two widely accessed platforms, namely “beyazperde.
com"for movie reviews and “otelpuan.com"for hotel reviews. A total of 53,400 
movie reviews were collected, with an average length of 33 words. These reviews 
were rated by the authors on a scale of 1 to 5 stars, ensuring a balanced representation 
of both positive and negative sentiments. Similarly, for hotel reviews, a set of 11,600 
positive and negative reviews were chosen from 18,478 reviews extracted from 550 
hotels. The average length of these hotel reviews was 74 words, more than double 
that of the movie reviews. This dataset’s versatility is further underscored by its uti­
Fig. 2  Heatmap of sentiment analysis taxonomy labels in Turkish studies by year (2012–2025). The 
intensity of each cell indicates the number of studies utilizing the corresponding taxonomy element
 
1 3
4027

--- Page 26 ---

Ş. Çakıcı et al.
lization in the study conducted by Acikalin et al. (2020) emphasizing its relevance 
across different analyses within the realm of sentiment analysis.
No additional preprocessing steps were applied to the datasets prior to model 
evaluation. Each dataset was used in its original form as released by its authors or 
retrieved through email correspondence. This decision was made to preserve the 
authenticity of each dataset and evaluate model robustness in realistic, unnormalized 
conditions. Future work may explore the effects of advanced preprocessing (e.g., 
lemmatization, normalization, or stopword removal) on model performance across 
diverse Turkish datasets.
3  Experimental setup
In our study, we have evaluated four state-of-the-art models to study sentiment in 
various texts, with a special focus on Turkish. These models are XLM-T, BERTurk 
(enhanced with the BounTi dataset), the TSAM available on Hugging Face, and 
TurkishBERTweet developed by ViralLab. These models predicts one of the labels 
positive, negative, and neutral for a given text.
	
●
XLM-T4: This model enables us to analyze sentiments across various languages, 
crucial for understanding multilingual sentiment on platforms like Twitter. It is 
a multilingual XLM-RoBERTa-based model trained on approximately 198  M 
tweets for sentiment analysis.BERTurk with the BounTi Dataset5: Specifically 
a fine-tuned version of the pre-trained BERTurk model, when combined with 
the BounTi dataset, offers us a valuable asset of sentiment prediction tool for 
Turkish texts. The BounTi dataset consists of Turkish tweets Köksal and Özgür 
(2021).TSAM on Hugging Face6: This model is optimized for Turkish sentiment 
analysis, utilizing a diverse set of Turkish texts for training. It is designed to 
accurately detect different expressions of sentiment.TurkishBERTweet by Vi­
ralLab7: This model excels in analyzing sentiments expressed in Turkish tweets. 
Its trained on 894 million Turkish tweets allows it to decode sentiments, casual 
expressions, emojis, and informal language found in social media texts. It is a 
large language model based on RoBERTa architecture.
Through the evaluation of four models, we provide a comprehensive evaluation of 
sentiment analysis models. This includes assessing each model's applicability to 
Turkish sentiment datasets. We also compile studies on sentiment analysis and cross-
dataset classification to provide detailed dataset information and compare their simi­
larities. This approach enables us to assess the strengths and potential limitations of 
each dataset and model comprehensively. Evaluation of various models and datasets 
4 ​h​t​t​p​s​:​/​/​h​u​g​g​i​n​g​f​a​c​e​.​c​o​/​c​a​r​d​i​f​f​n​l​p​/​t​w​i​t​t​e​r​-​x​l​m​-​r​o​b​e​r​t​a​-​b​a​s​e​-​s​e​n​t​i​m​e​n​t
5 ​h​t​t​p​s​:​/​/​g​i​t​h​u​b​.​c​o​m​/​b​o​u​n​-​t​a​b​i​/​B​o​u​n​T​i​-​T​u​r​k​i​s​h​-​S​e​n​t​i​m​e​n​t​-​A​n​a​l​y​s​i​s
6 ​h​t​t​p​s​:​/​/​h​u​g​g​i​n​g​f​a​c​e​.​c​o​/​e​m​r​e​/​t​u​r​k​i​s​h​-​s​e​n​t​i​m​e​n​t​-​a​n​a​l​y​s​i​s
7 ​h​t​t​p​s​:​/​/​h​u​g​g​i​n​g​f​a​c​e​.​c​o​/​V​R​L​L​a​b​/​T​u​r​k​i​s​h​B​E​R​T​w​e​e​t​#​-​t​u​r​k​i​s​h​b​e​r​t​w​e​e​t​-​f​a​s​t​-​a​n​d​-​r​e​l​i​a​b​l​e​-​l​a​r​g​e​-​l​a​n​g​u​a​g​e​-​
m​o​d​e​l​-​f​o​r​-​s​o​c​i​a​l​-​m​e​d​i​a​-​a​n​a​l​y​s​i​s
1 3
4028

--- Page 27 ---

A cross-validation study of Turkish sentiment analysis datasets and…
facilitates a detailed exploration of sentiment analysis, contributing valuable insights 
to the domain of Turkish NLP studies.
4  Results
The results we have obtained shed light the performance of the XLM-T, TSAM, 
TurkishBERTweet, and BERTurk models across various datasets. To enable more 
detailed analysis and facilitate the replication of our findings, we have made our 
code and models publicly available in our repository.8 This resource includes scripts 
for training the models, making predictions, and calculating key metrics such as 
Accuracy, Recall, Precision, and F1 scores. Our repository also offers a step-by-step 
guide, ensuring that both researchers and practitioners can easily leverage our work 
to benchmark or expand upon the sentiment analysis for Turkish texts.
In Table 4, we report detailed performance of these models using the aforemen­
tioned metrics. It is important to note that all models were designed to generate 
predictions based on a multi-classification format. However, the datasets vary, with 
some being tailored for multi-classification and others for binary classification. To 
address this variation and clarify the performance across different formats, Table 4 
includes scores calculated without modifying the classification formats of either the 
datasets or the models. Additionally, it presents scores recalculated for both datasets 
and models in a binary classification format, achieved by excluding “neutral"labels.
In binary classification tasks, where the objective was to differentiate between 
positive and negative sentiments, XLM-T and BERTurk showcased superior perfor­
mance across the board. Notably, XLM-T achieved a remarkable accuracy and F1 
score of.92 and.95, respectively, on the Twt dataset, highlighting its proficiency in 
binary sentiment analysis. Similarly, BERTurk exhibited strong performance with an 
accuracy of.86 and F1 score of.86 on the Twt dataset, further cementing its reliability 
in binary classification contexts.
TSAM, while showing moderate performance on the Twt dataset with accuracy 
and F1 scores of.59 and.54, respectively, demonstrated exceptional strength on the 
Humir dataset with near-perfect accuracy and F1 scores of.97. This indicates the 
TSAM’s potential effectiveness in specific binary classification scenarios, especially 
when tuned for particular types of data.
TurkishBERTweet, achieving an accuracy of.86 and an F1 score of.86 on the Twt 
dataset, also illustrated commendable binary classification capabilities, showcasing 
its potential utility in sentiment analysis tasks that require distinguishing between 
positive and negative sentiments.
Multi-class classification tasks, which included the challenge of identifying neu­
tral sentiments alongside positive and negative ones, revealed a different aspect of 
model performance. XLM-T showed consistent and promising results, particularly 
on the Turkmenoglu dataset, with an accuracy of.61 and an F1 score of.61. This 
underscores XLM-T’s versatility and strong adaptability across different classifica­
tion formats.
8 https://github.com/sevvalckc/Turkish-SAD
1 3
4029

--- Page 28 ---

Ş. Çakıcı et al.
Table 4  Model performance on different datasets
Da­
taset 
name
Model
Classification
Accuracy
Re­
call 
micro
Re­
call 
macro
Pre­
ci­
sion 
micro
Preci­
sion 
macro
F1 
micro
F1 
macro
Twt
XLM-T
Model: Multi, 
Dataset: Binary
.83
.83
.55
.83
.63
.83
.59
Both: Binary
.92
.95
.94
.95
.95
.95
.95
TSAM
Model: Multi, 
Dataset: Binary
.59
.59
.44
.59
.39
.59
.36
Both: Binary
.59
.59
.66
.59
.59
.59
.54
TurkishBER­
Tweet
Model: Multi, 
Dataset: Binary
.57
.57
.58
.57
.38
.57
.45
Both: Binary
.86
.86
.87
.86
.85
.86
.86
BERTurk
Model: Multi, 
Dataset: Binary
.56
.56
.52
.56
.37
.56
.40
Both: Binary
.75
.75
.78
.75
.71
.75
.72
Turk­
meno­
glu
XLM-T
Both: Multi
.61
.61
.61
.61
.62
.61
.61
Both: Binary
.82
.82
.82
.82
.81
.82
.81
TSAM
Both: Multi
.47
.47
.53
.47
.43
.47
.35
Both: Binary
.68
.68
.75
.68
.64
.68
.63
TurkishBER­
Tweet
Both: Multi
.56
.56
.62
.56
.58
.56
.56
Both: Binary
.82
.82
.83
.82
.82
.82
.82
BERTurk
Both: Multi
.61
.61
.62
.61
.62
.61
.61
Both: Binary
.81
.81
.81
.81
.81
.81
.81
TMRD 
TMPR
XLM-T
Model: Multi, 
Dataset: Binary
.56
.56
.48
.56
.37
.56
.42
Both: Binary
.72
.72
.72
.72
.72
.72
.72
TSAM
Model: Multi, 
Dataset: Binary
.73
.73
.52
.73
.49
.73
.48
Both: Binary
.74
.74
.78
.74
.74
.74
.73
TurkishBER­
Tweet
Model: Multi, 
Dataset: Binary
.46
.46
.49
.46
.31
.46
.37
Both: Binary
.73
.73
.73
.73
.73
.73
.73
BERTurk
Model: Multi, 
Dataset: Binary
.58
.58
.47
.58
.38
.58
.41
Both: Binary
.69
.69
.70
.69
.69
.69
.68
Humir
XLM-T
Model: Multi, 
Dataset: Binary
.81
.81
.56
.81
.54
.81
.55
Both: Binary
.85
.85
.85
.85
.85
.85
.85
TSAM
Model: Multi, 
Dataset: Binary
.97
.97
.65
.97
.65
.97
.65
Both: Binary
.97
.97
.97
.97
.97
.97
.97
TurkishBER­
Tweet
Model: Multi, 
Dataset: Binary
.64
.64
.54
.64
.42
.64
.47
Both: Binary
.80
.80
.81
.80
.78
.80
.79
BERTurk
Model: Multi, 
Dataset: Binary
.83
.83
.57
.83
.55
.83
.56
Both: Binary
.86
.86
.86
.86
.86
.86
.86
1 3
4030

--- Page 29 ---

A cross-validation study of Turkish sentiment analysis datasets and…
BERTurk and TurkishBERTweet displayed moderate success in multi-class sce­
narios, with BERTurk achieving an accuracy of.61 and an F1 score of.61 on the 
Turkmenoglu dataset. These outcomes suggest a balanced performance but also room 
for improvement in handling more nuanced classification tasks.
TSAM encountered challenges in multi-class classification, particularly evidenced 
by its lower accuracy (.47) and F1 score (.35) on the Turkmenoglu dataset. This 
performance difference highlights TSAM’s limitations in complex classification sce­
narios, despite its binary classification strengths. In scenarios where the dataset and 
model classification formats did not match, the performance of each model varied, 
revealing their flexibility and limitations. For instance, XLM-T managed a.83 accu­
racy in the Twt dataset when applying a multi-class model to a binary classified data­
set, showcasing its adaptability. However, the mismatch scenario generally resulted 
in lower performance metrics across models compared to when the classification for­
mats were aligned, indicating the importance of matching model and dataset formats 
for optimal performance.
5  Discussion
In this study, we conducted a comprehensive exploration of sentiment analysis stud­
ies in the Turkish language, spanning from data collection to model evaluation. We 
curated distinct Turkish datasets from publicly available sources and through email 
requests, organizing the compiled data within a GitHub repository. Furthermore, we 
systematically reviewed 78 relevant studies indexed on Scopus providing a detailed 
snapshot of each sentiment analysis study in our research.
The integration of four state-of-the-art models-XLM-T, BERTurk, TSAM, and 
TurkishBERTweet-allowed us to analyze sentiments in Turkish texts comprehen­
sively. These models were evaluated across various datasets, including the Turkish 
Movie Reviews Dataset (TMRD), Turkish Multidomain Products Reviews (TMPR), 
Twt dataset, and Humir dataset, among others. We also utilized a taxonomy to facili­
tate a nuanced understanding of the methodologies and datasets employed in Turkish 
sentiment analysis studies.
The evaluation of sentiment analysis models across various datasets provides 
valuable insights into their performance and suitability for different text corpora. 
Our study incorporated a diverse range of datasets, including movie reviews, product 
reviews, Twitter data, and COVID-19 related tweets, among others. Each dataset 
presents unique characteristics, such as data source, classification format, and size, 
which significantly impact model performance.
Across binary classification tasks, datasets like the Twt dataset and Turkish Movie 
Reviews Dataset (TMRD) demonstrated balanced distributions of positive and nega­
tive instances, contributing to relatively higher model accuracies. Multi-class clas­
sification tasks, which involve identifying neutral sentiments alongside positive 
and negative ones, revealed additional complexities. However, models like XLM-T 
exhibited promising adaptability and achieved competitive accuracy scores across 
multi-class scenarios.
1 3
4031

--- Page 30 ---

Ş. Çakıcı et al.
The performance of sentiment analysis models varied across datasets, reflecting 
the interplay between model architectures, training strategies, and dataset charac­
teristics. XLM-T emerged as a top performer, showcasing superior accuracy and F1 
scores in binary classification tasks across multiple datasets. This can be attributed to 
XLM-T’s cross-lingual learning capabilities, enabling it to effectively capture senti­
ment nuances in Turkish texts with diverse linguistic features. BERTurk, while dem­
onstrating strong performance overall, exhibited slightly lower accuracies compared 
to XLM-T in binary classification tasks. However, it showcased competitive results 
in multi-class scenarios, indicating its robustness in handling nuanced sentiment 
analysis tasks. The TSAM and TurkishBERTweet also displayed moderate to high 
accuracies across datasets, highlighting their effectiveness in capturing sentiment 
expressions in Turkish texts.
The relationship between model performance and dataset characteristics is com­
plex and multifaceted. Generally, models performed better on datasets with balanced 
class distributions, where positive and negative instances were evenly represented. 
This suggests that the measurement of the model accuracy is influenced by the avail­
ability of sufficient evaluation data for each class.
Moreover, the linguistic characteristics of the dataset, such as informal language, 
emoticons, and domain-specific jargon, significantly impact model performance. 
Models trained on datasets with diverse linguistic features, like social media texts, 
demonstrated higher adaptability and robustness in capturing sentiment nuances.
The discrepancy in model performance across datasets underscores the impor­
tance of dataset characteristics and preprocessing in sentiment analysis studies. 
Researchers must carefully curate datasets that align with the target application 
domain and ensure adequate representation of sentiment expressions to improve 
model generalization and performance.
The performance scores reported in original studies have been significantly 
updated in our study through the application of advanced deep learning models. 
Traditional machine learning methods, such as Multinomial Naive Bayes (MNB) 
and Support Vector Machines (SVM), achieved notable results in earlier research 
but were constrained by their limited ability to handle linguistic complexity. For 
instance, Çoban et al. (2015) reported an accuracy of 0.66 on the Twt dataset 
using MNB. In contrast, our deep learning models have considerably improved 
upon these results, with XLM-T achieving an accuracy of 0.92, TurkishBERT­
weet reaching 0.86, and BERTurk attaining 0.75. These advancements underscore 
the enhanced capabilities of modern models to capture linguistic nuances and 
domain-specific variations, demonstrating how the integration of deep learning 
can substantially elevate the benchmarks established by traditional approaches.
The quality and diversity of datasets also have a significant impact on model 
performance. In tasks like sentiment analysis, factors such as imbalanced class 
distributions, insufficient sample sizes, and noisy data can negatively affect the 
model’s ability to generalize. The experiments conducted on different datasets 
in this study reveal that the performance of the models varies according to the 
characteristics of the dataset. This situation highlights the critical importance of 
dataset preparation and preprocessing in sentiment analysis studies.
1 3
4032

--- Page 31 ---

A cross-validation study of Turkish sentiment analysis datasets and…
Lastly, the linguistic features of Turkish, such as its agglutinative structure and 
rich inflectional systems, present specific challenges for natural language pro­
cessing models. This study has shown that XLM-T is more effective than BER­
Turk in overcoming these types of challenges. These findings can guide future 
work and contribute to the development of more successful natural language pro­
cessing models for languages with complex structures.
6  Implications of the study
6.1  Theoretical and research implications
This study makes a methodological contribution to Turkish sentiment analy­
sis research by systematically compiling and categorizing 78 studies published 
between 2012 and 2025. By applying the taxonomy proposed by Rodrigues et al. 
(2018), we present a structured classification of studies and identify patterns in 
sentiment analysis approaches. This taxonomy-driven review provides a clearer 
understanding of research gaps in the Turkish NLP landscape-particularly the 
underrepresentation of emotion classification and the absence of concept-based 
sentiment analysis methods. Additionally, our use of a systematic literature 
review (SLR) methodology offers a replicable and comprehensive framework for 
future research synthesis in similar low-resource languages.
6.2  Practical implications
The comparative evaluation of four transformer-based models across multiple 
Turkish datasets yields practical insights for model and data selection. Our find­
ings show that dataset characteristics such as class balance, domain specificity, 
and text structure significantly affect model performance. For example, models 
trained on product reviews showed higher accuracy than those trained on social 
media texts, likely due to linguistic variability and noise. These results emphasize 
the importance of aligning dataset structure with model architecture to maximize 
effectiveness. Preprocessing decisions-such as handling emoticons, punctuation, 
and informal expressions-also critically shape model outcomes, particularly in 
high-variance datasets like Twitter.
6.3  Future potential and directions
Future studies can extend our findings by incorporating larger, more diverse 
datasets, particularly from underexplored domains like health, finance, and edu­
cation. Integrating large language models (LLMs) and domain-adapted transfer 
learning techniques may further improve model adaptability. A final and promis­
ing direction involves exploring concept-based sentiment analysis techniques in 
Turkish. These methods focus on identifying and modeling structured semantic 
relationships between concepts, enabling richer and more context-aware senti­
ment interpretation. For example, adapting multilingual affective resources such 
1 3
4033

--- Page 32 ---

Ş. Çakıcı et al.
as SenticNet (Cambria et al., 2020) or ConceptNet for Turkish can support the 
construction of sentiment graphs that link affective concepts across domains. 
Furthermore, developing a Turkish sentiment ontology-potentially grounded in 
Turkish WordNet and expanded through domain-specific thesauri-could facilitate 
automatic concept labeling and sentiment propagation within context-rich nar­
ratives. While these approaches are methodologically more complex, they hold 
high potential in domains like healthcare, education, and finance, where senti­
ment is often implied or metaphorically expressed.
7  Conclusion
This study provides a comprehensive landscape of Turkish sentiment analysis 
research by combining a systematic literature review with empirical model evalu­
ation. We compiled and categorized 78 studies using a structured taxonomy and 
analyzed datasets drawn from diverse sources, highlighting trends in polarity 
detection, dataset usage, and methodological design.
Through the evaluation of four transformer-based models-XLM-T, BER­
Turk, TSAM, and TurkishBERTweet-across diverse datasets, we demonstrated 
that model performance is strongly influenced by dataset characteristics such as 
domain, class balance, and language structure. Our results confirm that trans­
former-based models, particularly those trained in multilingual settings, offer 
substantial improvements over traditional machine learning approaches. These 
findings offer both theoretical and applied contributions to Turkish NLP and can 
guide future work in model selection and data preparation.
8  Future work
Future research can build on our findings by expanding the range and represen­
tativeness of Turkish sentiment datasets. Efforts to create benchmark datasets 
with standardized evaluation protocols would enable more consistent and com­
parable model development across studies. In addition, future work may incor­
porate methods such as few-shot learning, domain adaptation, and multilingual 
fine-tuning to enhance model generalizability in low-resource settings (Schick & 
Schützem, 2021; Ruder, 2019).
Another compelling direction lies in exploring concept-based sentiment analy­
sis, which remains largely absent in Turkish NLP research. These approaches-
focusing on semantic relationships and conceptual inference rather than 
surface-level polarity-could offer deeper insights, particularly in domains where 
sentiment is implicit. Developing a Turkish sentiment ontology and adapting 
semantic resources such as SenticNet or ConceptNet to the Turkish language 
could support this direction and enable richer, more context-aware sentiment 
interpretation in both academic and applied contexts (Cambria et al., 2020).
In addition, future work could expand the number of datasets used for compar­
ative evaluation. While our current study tested model performance on a subset 
1 3
4034

--- Page 33 ---

A cross-validation study of Turkish sentiment analysis datasets and…
of widely used datasets, applying the same models across all collected datasets 
and conducting statistical significance testing would allow for more robust and 
generalizable insights.
Finally, future extensions of this study will consider the integration of large-
scale language models (LLMs) such as OpenAI’s GPT series and Google’s 
Gemini. While this paper focused on publicly available models like BERTurk, 
XLM-T, TurkishBERTweet, and TSAM to ensure reproducibility and accessi­
bility, evaluating the performance of proprietary LLMs on Turkish sentiment 
datasets could offer valuable comparative benchmarks. Given the increasing 
multilingual capabilities of these models and their growing industrial relevance, 
future work may explore efficient fine-tuning or zero-shot evaluation across a 
representative sample of Turkish sentiment datasets.
Author Contributions  Ş.Ç. (Şevval Çakıcı) and D.K. (Dilara Karaduman) worked on curating the datasets 
by conducting a thorough search and contacting the authors of studies to request access to their data. D.K. 
also ran the models on the collected datasets and contributed to the analysis. A.H. (Ali Hürriyetoğlu) 
designed the overall framework and Ş.Ç. lead the study. M.A.Ç. (Mehmet Akif Çırlan) and Ş.Ç. col­
laborated on organizing and refining the tables, ensuring that all data and classifications were consistently 
represented. M.A.Ç. also led the process of labeling the studies based on the taxonomy table, ensuring 
the accuracy and consistency of the classifications. All authors, including Ş.Ç., D.K., M.A.Ç., and A.H., 
conducted the literature review and discussed the findings. A.H. provided expert insights into the method­
ology, critically revised the manuscript for intellectual content, and guided the structuring of the taxonomy 
and analytical approach. All authors contributed to the interpretation of results, reviewed the manuscript 
critically, and approved the final version for submission. They collectively agree to be accountable for all 
aspects of the work.
Data Availability  The datasets supporting the findings of this study include publicly available data and 
datasets accessible via email request. Publicly accessible datasets are detailed with their corresponding 
links in our GitHub repository ([https://github.com/sevvalckc/Turkish-SAD]). For datasets obtained via 
email request, we have included the contact information for the respective authors or institutions in the 
same repository. Detailed data sources and access methods are provided within the manuscript and the 
GitHub repository.
Declarations
Conflict of interest  The authors declare no Conflict of interest.
Open Access   This article is licensed under a Creative Commons Attribution 4.0 International License, 
which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long 
as you give appropriate credit to the original author(s) and the source, provide a link to the Creative 
Commons licence, and indicate if changes were made. The images or other third party material in this 
article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line 
to the material. If material is not included in the article’s Creative Commons licence and your intended use 
is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission 
directly from the copyright holder. To view a copy of this licence, visit ​h​t​t​p​:​/​/​c​r​e​a​t​i​v​e​c​o​m​m​o​n​s​.​o​r​g​/​l​i​c​e​n​
s​e​s​/​b​y​/​4​.​0​/​.​
1 3
4035

--- Page 34 ---

Ş. Çakıcı et al.
References
Abbasi, A., Chen, H., & Salem, A. (2008). Sentiment analysis in multiple languages: Feature selection for 
opinion classification in web forums. ACM Transactions on Information Systems,26(3), 1–34.
Abdellatif, A., Sahmoud, S., & Nizam, A. (2023). A unified framework for multi-language sentiment anal­
ysis. In 2023 3rd International Conference on Computing and Information Technology (ICCIT), (pp. 
280–284). IEEE.
Acikalin, UU., Bardak, B., & Kutlu, M. (2020). Turkish sentiment analysis using bert. In 2020 28th Signal 
Processing and Communications Applications Conference (SIU), (pp. 1–4). IEEE.
Akin, SE., & Yildiz, T. (2019). Sentiment analysis through transfer learning for turkish language. In 2019 
IEEE International Symposium on INnovations in Intelligent SysTems and Applications (INISTA), 
(pp. 1–6). IEEE.
Aktas, Zeynep, & Çebi, Ece. (2020). Challenges encountered in turkish natural language processing stud­
ies. Kastamonu Egitim Dergisi, 28, 847–860. https://doi.org/10.24106/kefdergi.753591
Alawi, A. B., & Bozkurt, F. (2024a). A hybrid machine learning model for sentiment analysis and satisfac­
tion assessment with Turkish universities using Twitter data. Decision Analytics Journal,11, 100473. 
https://doi.org/10.1016/j.dajour.2024.100473
Alawi, A. B., & Bozkurt, F. (2024b). Performance analysis of embedding methods for deep learning-based 
turkish sentiment analysis models. Arabian Journal for Science and Engineering. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​
.​1​0​0​7​/​s​1​3​3​6​9​-​0​2​4​-​0​8​3​4​1​-​z​
Alawi, AB., & Bozkurt, F. (2024c). Evaluating public sentiments about turkish universities through twitter 
using deep learning techniques. In 2024 32nd Signal Processing and Communications Applications 
Conference (SIU), (pp. 1–4). IEEE.
Alnahas, D., Asik, F., Kanturvardar, A., & Ülkgün, AM. (2022). Opinion mining using lstm networks 
ensemble for multi-class sentiment analysis in e-commerce. In 2022 3rd International Informatics 
and Software Engineering Conference (IISEC), pp. 1–6. IEEE.
Alqaraleh, S. (2021). Novel turkish sentiment analysis system using convnet
Altinel Girgin, A. B., Gümüsçekiççi, G., & Birdemir, N. C. (2024). Turkish sentiment analysis : A com­
prehensive review. Sigma: Journal of Engineering & Natural Sciences/Mühendislik ve Fen Bilimleri 
Dergisi, 42, 1292.
Altinok, D. (2023). A diverse set of freely available linguistic resources for turkish. In Proceedings of the 
61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 
13739–13750, Toronto, Canada, Association for Computational Linguistics. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​8​6​5​
3​/​v​1​/​2​0​2​3​.​a​c​l​-​l​o​n​g​.​7​6​5.
Amasyali, MF., Tasköprü, H., & Çaliskan, K. (2018). Words, meanings, characters in sentiment analysis. 
In 2018 Innovations in Intelligent Systems and Applications Conference (ASYU), pp. 1–6. IEEE.
Ay Karakus, B., Talo, M., Hallaç, I. R., & Aydin, G. (2018). Evaluating deep learning models for sentiment 
classification. Concurrency and Computation: Practice and Experience, 30(21), e4783. ​h​t​t​p​s​:​/​/​d​o​i​.​
o​r​g​/​1​0​.​1​0​0​2​/​c​p​e​.​4​7​8​3​
Ayata, D., Saraçlar, M., & Özgür, A. (2017). Turkish tweet sentiment analysis with word embedding and 
machine learning. In 2017 25th Signal Processing and Communications Applications Conference 
(SIU), pp. 1–4. IEEE.
Aydin, C. R., & Güngör, T. (2021). Sentiment analysis in Turkish: Supervised, semi-supervised, and unsu­
pervised techniques. Natural Language Engineering,27(4), 455–483.
Aydin, CR., Güngör, T., spsampsps Erkan, A. (2019). Generating word and document embeddings for 
sentiment analysis. In International Conference on Computational Linguistics and Intelligent Text 
Processing, volume 11455 of Lecture Notes in Computer Science, pp. 307–318, Cham, Springer 
Nature Switzerland. https://doi.org/10.1007/978-3-030-15719-7_24.
Aydin, Z. E., Ozturk, Z. K., & Cicek, Z. I. E. (2021). Turkish sentiment analysis for open and distance 
education systems. Turkish Online Journal of Distance Education, 22, 124–138.
Aydogan, M., & Kocaman, V. (2023). Trsav1: A new benchmark dataset for classifying user reviews on 
Turkish e-commerce websites. Journal of Information Science,49(6), 1711–1725.
Aygün, I., Kaya, B., & Kaya, M. (2021). Aspect based twitter sentiment analysis on vaccination and 
vaccine types in Covid-19 pandemic with deep learning. IEEE Journal of Biomedical and Health 
Informatics,26(5), 2360–2369.
1 3
4036

--- Page 35 ---

A cross-validation study of Turkish sentiment analysis datasets and…
Balli, C., Guzel, M. S., Bostanci, E., & Mishra, A. (2022). Sentimental analysis of twitter users from turk­
ish content with natural language processing. Computational Intelligence and Neuroscience, 2022, 
2455160.
Barbieri, Francesco, Anke, Luis E., & Camacho-Collados, Jose. (2021). Xlm-t: multilingual language 
models in twitter for sentiment analysis and beyond. Preprint retrieved from ​h​t​t​p​s​:​/​/​a​r​x​i​v​.​o​r​g​/​a​b​s​/​q​u​
a​n​t​-​p​h​/​2​1​0​4​.​1​2​2​5​0​
Bayraktar, K., Yavanoglu, U., & Özbilen, A. (2019). A rule-based holistic approach for turkish aspect-
based sentiment analysis. In 2019 IEEE International Conference on Big Data (Big Data), pp. 2154–
2158. IEEE.
Bozuyla, M. (2024). Sentiment analysis of Turkish drug reviews with bidirectional encoder represen­
tations from transformers. ACM Transactions on Asian and Low-Resource Language Information 
Processing (TALLIP), 23(1), 1–17. https://doi.org/10.1145/3641220
Cabanac, M. (2002). What is emotion? Behavioural Processes, 60(2), 69–83. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​S​0​
3​7​6​-​6​3​5​7​(​0​2​)​0​0​0​7​8​-​5
Cam, H., Cam, A. V., Demirel, U., & Ahmed, S. (2024). Sentiment analysis of financial twitter posts on 
twitter with the machine learning classifiers. Heliyon, 10(1), e23967. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​0​1​6​/​j​.​h​e​l​i​y​
o​n​.​2​0​2​4​.​e​2​3​9​6​7
Cambria, Erik, Li, Yang, Xing, Frank Z., Poria, Soujanya, & Kwok, Kenneth. (2020). Senticnet 6: Ensem­
ble application of symbolic and subsymbolic ai for sentiment analysis. In Proceedings of the 29th 
ACM International Conference on Information & Knowledge Management, pp. 105–114. ACM.
Çetin, M., & Amasyali, M. F. (2013). Supervised and traditional term weighting methods for sentiment 
analysis. In 2013 21st Signal Processing and Communications Applications Conference (SIU), pp. 
1–4. IEEE.
Ciftci, B., & Apaydin, MS. (2018). A deep learning approach to sentiment analysis in turkish. In 2018 
International Conference on Artificial Intelligence and Data Processing (IDAP), pp. 1–5. IEEE.
Çoban, Ö., & Özyer, G. T. (2018). Word2vec and clustering based twitter sentiment analysis. In 2018 Inter­
national Conference on Artificial Intelligence and Data Processing (IDAP), pp. 1–5. IEEE.
Çoban, Ö., Özyer, B., & Özyer, G. T. (2015). Sentiment analysis for turkish twitter feeds. In 2015 23nd 
Signal Processing and Communications Applications Conference (SIU), pp. 2388–2391. IEEE.
Demir, E., & Bilgin, M. (2023). Sentiment analysis from turkish news texts with bert-based language 
models and machine learning algorithms. In 2023 8th International Conference on Computer Science 
and Engineering (UBMK), pp. 01–04. IEEE.
Demirci, GM., Keskin, SR., & Dogan, G. (2019). Sentiment analysis in turkish with deep learning. In 2019 
IEEE International Conference on Big Data (Big Data), pp. 2215–2221. IEEE.
Demirtas, E., & Pechenizkiy, M. (2013). Cross-lingual polarity detection with machine translation. In 
Proceedings of the Second International Workshop on Issues of Sentiment Discovery and Opinion 
Mining, pp. 1–8. ACM.
Deniz, E., Erbay, H., & Cosar, M. (2022). Multi-label classification of e-commerce customer reviews via 
machine learning. Axioms,11(9), 436.
Devika, M. D., Sunitha, C., & Ganesh, A. (2016). Sentiment analysis: A comparative study on different 
approaches. Procedia Computer Science, 87, 44.
Eker, AG., Eker, K., & Duru, N. (2021). Multi-class sentiment analysis from turkish tweets with rnn. In 
2021 6th International Conference on Computer Science and Engineering (UBMK), pp. 560–564. 
IEEE.
Ekinci, M., Özcan, MS., & Amasyali, MF. (2016). Time effect in sentiment analysis. In 2016 24th Signal 
Processing and Communication Application Conference (SIU), pp. 209–212. IEEE.
Ekman, P. (1992). An argument for basic emotions. Cognition and Emotion,6(3–4), 169–200. ​h​t​t​p​s​:​/​/​d​o​i​.​
o​r​g​/​1​0​.​1​0​8​0​/​0​2​6​9​9​9​3​9​2​0​8​4​1​1​0​6​8​
Erguvanli-Taylan, E. E. (1984). The Function of Word Order in Turkish Grammar. University of California 
Press.
Erkan, A., & Güngör, T. (2023). Analysis of deep learning model combinations and tokenization 
approaches in sentiment classification. IEEE Access, 11, 134951–134968. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​0​9​/​
A​C​C​E​S​S​.​2​0​2​3​.​3​3​3​2​9​5​9​
Ersahin, B., Aktas, Ö., Kilinç, D., & Ersahin, M. (2019). A hybrid sentiment analysis method for turkish. 
Turkish Journal of Electrical Engineering and Computer Sciences, 27(3), 1780–1793.
Ezin, E., Kiziltepe, RS., & Karakus, M. (2024). Using llms for annotation and ml methods for comparative 
analysis of large-scale turkish sentiment datasets. In 2024 9th International Conference on Computer 
Science and Engineering (UBMK), pp. 204–209. IEEE.
1 3
4037

--- Page 36 ---

Ş. Çakıcı et al.
Fehle, J., Schmidt, T., & Wolff, C. (2021). Lexicon-based sentiment analysis in german: systematic evalu­
ation of resources and preprocessing techniques. Journal of Computational Linguistics.
Guven, Z. A. (2022). The comparison of language models with a novel text filtering approach for turkish 
sentiment analysis. ACM Transactions on Asian and Low-Resource Language Information Process­
ing (TALLIP), 22(2), 1–16. https://doi.org/10.1145/3543856
Güven, Z., Diri, B., & Çakaloglu, T. (2020). Comparison of n-stage latent dirichlet allocation versus other 
topic modeling methods for emotion analysis. Journal of the Faculty of Engineering and Architecture 
of Gazi University. https://doi.org/10.17341/gazimmfd.556104
Haddaway, N. R., Page, M. J., Pritchard, C. C., & McGuinness, L. A. (2022). Prisma 2020: An R package 
and shiny app for producing prisma 2020-compliant flow diagrams, with interactivity for optimised 
digital transparency and open synthesis. Campbell Systematic Reviews,18(2), Article e1230. ​h​t​t​p​s​:​/​/​
d​o​i​.​o​r​g​/​1​0​.​1​0​0​2​/​c​l​2​.​1​2​3​0​
Hayran, A., & Sert, M. (2017). Sentiment analysis on microblog data based on word embedding and fusion 
techniques. In 2017 25th Signal Processing and Communications Applications Conference (SIU), 
pp. 1–4. IEEE.
Hürriyetoglu, Ali, Yörük, Erdem, Mutlu, Osman, Durusan, Firat, Yoltar, Çagri., Yüret, Deniz, & Gürel, 
Burak. (2021). Cross-Context News Corpus for Protest Event-Related Knowledge Base Construc­
tion. Data Intelligence, 3, 308–335.
Internet World Stats. Usage and population statistics, (2022). URL ​h​t​t​p​s​:​/​/​w​w​w​.​i​n​t​e​r​n​e​t​w​o​r​l​d​s​t​a​t​s​.​c​o​m​/​s​
t​a​t​s​4​.​h​t​m.
Isgüder Sahin, G. G., Zafer, H. R., & Adah, E. (2014). Polarity detection of turkish comments on tech­
nology companies. In 2014 International Conference on Asian Language Processing (IALP), pp. 
136–139. IEEE
Kabakus, A. T. (2022). A novel COVID-19 sentiment analysis in Turkish based on the combination of 
convolutional neural network and bidirectional long-short term memory on Twitter. Concurrency and 
Computation: Practice & Experience,34(22), Article e6883.
Karamollaoglu, H., Dogru, IA., Arici, N., & Yildiz, O. (2019). Content based sentiment analysis for turkish 
twitter feeds through vector space model. In 2019 1st International Informatics and Software Engi­
neering Conference (UBMYK), pp. 1–6. IEEE.
Karayigit, H., Akdagli, A., & Aci, Ç. I. (2022). Bert-based transfer learning model for Covid-19 sentiment 
analysis on Turkish Instagram comments. Information Technology and Control,51(3), 409–428.
Kaya, M., Fidan, G., & Toroslu, IH. (2012). Sentiment analysis of turkish political news. In 2012 IEEE/
WIC/ACM International Conferences on Web Intelligence and Intelligent Agent Technology (WI-
IAT), vol 1, pp. 74–180. IEEE.
Kemaloglu, N., Küçüksille, E., & Özgünsür, M. (2021). Turkish sentiment analysis on social media. 
Sakarya University Journal of Science, 25, 629–638.
Kiliç, Y., & Büyükeke, A. (2021). An exploratory case study for turkish sentiment classification using 
graph convolutional neural networks. In 2021 6th International Conference on Computer Science and 
Engineering (UBMK), pp. 587–591. IEEE.
Kilimci, Z. H. (2020). Financial sentiment analysis with deep ensemble models (dems) for stock mar­
ket prediction. Journal of the Faculty of Engineering and Architecture of Gazi University, 35(2), 
635–650.
Kilimci, ZH., Yörük, H., & Akyokus, S. (2020). Sentiment analysis based churn prediction in mobile 
games using word embedding models and deep learning algorithms. In 2020 International Confer­
ence on Innovations in Intelligent Systems and Applications (INISTA), pp. 1–7. IEEE.
Kitchenham, B., & Charters, S. (2007). Guidelines for performing systematic literature reviews in soft­
ware engineering. Technical Report EBSE 2007-001, Keele University and Durham University Joint 
Report.
Kiziltepe, RS., Ezin, E., & Karakus, M. (2024). A comparative study of ml models on large-scale turkish 
sentiment datasets. In 2024 Innovations in Intelligent Systems and Applications Conference (ASYU), 
pp. 1–6. IEEE.
Köksal, A., & Özgür, A. (2021). Twitter dataset and evaluation of transformers for turkish sentiment analy­
sis. In 2021 29th Signal Processing and Communications Applications Conference (SIU), pp. 1–4. 
IEEE.
Makinist, S., Hallac, I. R., Karakus, B. A., & Aydin, G. (2018). Preparation of improved turkish dataset for 
sentiment analysis in social media. Preprint retrieved from https://arxiv.org/abs/quant-ph/1801.09975
1 3
4038

--- Page 37 ---

A cross-validation study of Turkish sentiment analysis datasets and…
Mulki, H., Haddad, H., Ali, C. B., & Babaoglu, I. (2018). Preprocessing impact on turkish sentiment 
analysis. In 2018 26th Signal Processing and Communications Applications Conference (SIU), pp. 
1–4. IEEE.
Mutlu, M. M., & Özgür, A. (2022). A dataset and bert-based models for targeted sentiment analysis on 
turkish texts. Preprint retrieved from https://arxiv.org/abs/quant-ph2205.04185
Najafi, A., & Varol, O. (2024). Turkishbertweet: Fast and reliable large language model for social media 
analysis. Expert Systems with Applications, 255, 124737. https://doi.org/10.1016/j.eswa.2023.124737
Nasution, A. H., & Onan, A. (2024). Chatgpt label: Comparing the quality of human-generated and llm-
generated annotations in low-resource language nlp tasks. IEEE Access. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​0​9​/​A​C​
C​E​S​S​.​2​0​2​4​.​3​3​5​0​3​2​5​
Oflazer, K. (1994). Two-level description of Turkish morphology. Literary and Linguistic Computing, 
9(2), 137–148.
Oflazer, K., Say, B., Hakkani-Tür, D., & Tür, G. (2003). Statistical morphological disambiguation for 
agglutinative languages. Computers and the Humanities,36(4), 381–410.
Ogul, B. B., & Ercan, G. (2016). Sentiment classification on turkish hotel reviews. In 2016 24th Signal 
Processing and Communication Application Conference (SIU), pp. 497–500. IEEE.
Ogul, H. A., & Güran, A. (2019). Imbalanced dataset problem in sentiment analysis. In 2019 4th Interna­
tional Conference on Computer Science and Engineering (UBMK), pp. 313–317. IEEE.
Omurca,S. I., Ekinci, E., & Türkmen, H. (2017). An annotated corpus for turkish sentiment analysis at 
sentence level. In 2017 International Artificial Intelligence and Data Processing Symposium (IDAP), 
pp. 1–5. IEEE.
Onan, A., & Balbal, K. F. (2024). Improving Turkish text sentiment classification through task-specific and 
universal transformations: An ensemble data augmentation approach. IEEE Access,12, 4413–4458. 
https://doi.org/10.1109/ACCESS.2024.3342511
Oueslati, O., Cambria, E., HajHmida, M. B., & Ounelli, H. (2020). A review of sentiment analysis research 
in Arabic language. Future Generation Computer Systems,112, 408–430.
Özdemir, A. O., Giritli, E. B., & Can, Y. S. (2024). Sentiment analysis for hotel reviews in turkish by 
using llms. In 2024 9th International Conference on Computer Science and Engineering (UBMK), 
pp. 210–214. IEEE.
Özmen, C. G., & Gündüz, S. (2025). Comparison of machine learning models for sentiment analysis of big 
Turkish web-based data. Applied Sciences,15(5), 2297. https://doi.org/10.3390/app15052297
Parlar, T. & Özel, S. A. (2016). A new feature selection method for sentiment analysis of turkish reviews. 
In 2016 International Symposium on INnovations in Intelligent SysTems and Applications (INISTA), 
pp. 1–6. IEEE.
Parlar,T., Saraç,E., & Özel, S. A. (2017). Comparison of feature selection methods for sentiment analysis 
on turkish twitter data. In 2017 25th Signal Processing and Communications Applications Confer­
ence (SIU), pp. 1–4. IEEE.
Plutchik, R. (1980). A general psychoevolutionary theory of emotion. Theories of emotion (pp. 3–33). 
Academic Press.
Polat, E. N., Yildiz, O. T., Demiroglu, C., & Kafescioglu, N. (2024). Decoding emotional dynamics: A 
comparative analysis of contextual and non-contextual models in sentiment analysis of turkish cou­
ple dialogues. IEEE Access. https://doi.org/10.1109/ACCESS.2024.3350190
Rodrigues, R., Camilo-Junior, C. G., & Rosa, T. (2018). A taxonomy for sentiment analysis field. Inter­
national Journal of Web Information Systems, 14(2), 193–211. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​1​0​.​1​1​0​8​/​i​j​w​i​s​-​0​7​-​2​0​1​
7​-​0​0​4​8​
Ruder, S. (2019). Neural transfer learning for natural language processing. retrieved from ​h​t​t​p​s​:​/​/​a​r​x​i​v​.​o​r​
g​/​a​b​s​/​q​u​a​n​t​-​p​h​/​1​9​0​3​.​1​1​2​6​0​
Rumelli, M., Akkus,D., Kart, Ö., & Isik, Z. (2019). Sentiment analysis in turkish text with machine learn­
ing algorithms. In 2019 Innovations in intelligent systems and applications conference (ASYU), pp. 
1–5. IEEE.
Saglam, F., Sever, H., & Genç, B. (2016). Developing turkish sentiment lexicon for sentiment analysis 
using online news media. In 2016 IEEE/ACS 13th International Conference of Computer Systems 
and Applications (AICCSA), pp. 1–5. IEEE.
Salur, M. U., & Aydin, I. (2021). An annotated turkish aspect based sentiment analysis corpus for smart 
tourism. In 2021 Innovations in Intelligent Systems and Applications Conference (ASYU), pp. 1–6. 
IEEE.
Santur, Y. (2019). Sentiment analysis based on gated recurrent unit. In 2019 International Artificial Intel­
ligence and Data Processing Symposium (IDAP), pages p. 1–5. IEEE.
1 3
4039

--- Page 38 ---

Ş. Çakıcı et al.
Schick, T., & Schützem, H. (2021). It’s not just size that matters: Small language models are also few-shot 
learners. In Proceedings of NAACL.
Shehu, H. A., & Tokat, S. (2019). A hybrid approach for the sentiment analysis of turkish twitter data. The 
International Conference on Artificial Intelligence and Applied Mathematics in Engineering (pp. 
182–190). Springer International Publishing.
Shehu, H. A., Sharif, M. H., Sharif, M. H. U., Datta, R., Tokat, S., Uyaver, S., & Ramadan, R. A. (2021). 
Deep sentiment analysis: A case study on stemmed turkish twitter data. IEEE Access, 9, 56836–
56854. https://doi.org/10.1109/ACCESS.2021.3072353
Shehu, H. A., Tokat, S., Sharif, M. H., & Uyaver, S. (2019). Sentiment analysis of turkish twitter data. In 
AIP Conference Proceedings, volume 2183, page 020001. AIP Publishing.
Sigirci, I. O., Özgür, H., Oluk, A., Uz, H., Çetiner, E., Oktay, H. U., & Erdemir, K. (2020). Sentiment 
analysis of turkish reviews on google play store. In 2020 5th International Conference on Computer 
Science and Engineering (UBMK), pp. 314–315. IEEE.
Tasar, D. E., Özcan, C., & Koruyan, K. (2022). Autotrain yaklasimi ile duygu analizi. In PRocEEDiNG 
BOOK, page 30.
Tohma, K., Okur, H. I., Kutlu, Y., & Sertbas, A. (2023). Sentiment analysis in turkish question answering 
systems: An application of human-robot interaction. IEEE Access, 11, 66522–66534. ​h​t​t​p​s​:​/​/​d​o​i​.​o​r​g​/​
1​0​.​1​1​0​9​/​A​C​C​E​S​S​.​2​0​2​3​.​3​2​8​4​2​8​9​
Türkmenoglu, C., & Tantug, A. C. (2014). Sentiment analysis in turkish media. In International Confer­
ence on Machine Learning (ICML).
Ucan, A., Naderalvojoud, B., Sezer, E. A., & Sever, H. (2016). Sentiwordnet for new language: automatic 
translation approach. In 2016 12th International Conference on Signal-Image Technology & Internet-
Based Systems (SITIS), pp. 08–315. IEEE.
Uslu, A., Tekin, S., & Aytekin, T. (2019). Sentiment analysis in turkish film comments. In 2019 27th Signal 
Processing and Communications Applications Conference (SIU), pp. 1–4. IEEE.
Visual Capitalist Licensing. The most used languages on the internet, (2022). URL ​h​t​t​p​s​:​/​/​l​i​c​e​n​s​i​n​g​.​v​i​s​u​a​
l​c​a​p​i​t​a​l​i​s​t​.​c​o​m​/​p​r​o​d​u​c​t​/​t​h​e​-​m​o​s​t​-​u​s​e​d​-​l​a​n​g​u​a​g​e​s​-​o​n​-​t​h​e​-​i​n​t​e​r​n​e​t​/.
Yayli, A., & Bayram, M. (2012). E-wom: The effects of online consumer reviews on purchasing decisions. 
International Journal of Internet Marketing and Advertising, 7(1), 51–64.
Yilmaz, M. K., & Altunay, H. T. (2023). Marketing insight from consumer reviews: Creating brand posi­
tion through opinion mining approach. Telematics and Informatics Reports, 11, Article 100094. 
https://doi.org/10.1016/j.teler.2023.100094
Yüksel, A. S., & Tan, F. G. (2018). A real-time social network-based knowledge discovery system for 
decision making. Automatika : časopis za automatiku, mjerenje, elektroniku, računarstvo i komuni­
kacije,59(3–4), 261–273.
Yurtalan, G., Koyuncu, M., & Turhan, Ç. (2019). A polarity calculation approach for lexicon-based Turk­
ish sentiment analysis. Turkish Journal of Electrical Engineering and Computer Sciences,27(2), 
1325–1339. https://doi.org/10.3906/elk-1807-65
Zeybek, S., Koç, E., & Seçer, A. (2021). MS-TR: A morphologically enriched sentiment treebank and 
recursive deep models for compositional semantics in turkish. Cogent Engineering,8(1), 1893621.
Zhang, L., Wang, S., & Liu, B. (2018). Deep learning for sentiment analysis: A survey. Wiley Interdisci­
plinary Reviews: Data Mining and Knowledge Discovery, 8(4), Article e1253.
Zümberoglu, K. B., Dik, S. Z., Karadeniz, B. S., & Sahmoud, S. (2025). Towards better sentiment analysis 
in the turkish language: Dataset improvements and model innovations. Applied Sciences, 15, 2062.
Publisher's Note  Springer Nature remains neutral with regard to jurisdictional claims in published maps 
and institutional affiliations.
Authors and Affiliations
Şevval Çakıcı1 · Dilara Karaduman2 · Mehmet Akif Çırlan2 · Ali Hürriyetoğlu3
	
 Şevval Çakıcı
sevval.cakici@ozu.edu.tr
1 3
4040

--- Page 39 ---

A cross-validation study of Turkish sentiment analysis datasets and…
	
 Ali Hürriyetoğlu
ali.hurriyetoglu@wur.nl
Dilara Karaduman
dkaraduman17@ku.edu.tr
Mehmet Akif Çırlan
mcirlan19@ku.edu.tr
1	
Ozyegin University, İstanbul, Turkey
2	
Koc University, Istanbul, Turkey
3	
Wageningen Food Safety Research, Wageningen, Netherlands
1 3
4041

```
