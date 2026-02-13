---
title: "2025-Chakravarthi-Detecting Caste and Migration Hate Speech - PDF Extract"
source_pdf: "2025-Chakravarthi-Detecting Caste and Migration Hate Speech.pdf"
pages: 36
extracted_at: "2026-02-13T10:43:53.240398"
---

# PDF Extract: 2025-Chakravarthi-Detecting Caste and Migration Hate Speech

**Source PDF:** 2025-Chakravarthi-Detecting Caste and Migration Hate Speech.pdf
**Total Pages:** 36

---

## Content

```
--- Page 1 ---

Vol.:(0123456789)
Language Resources and Evaluation (2025) 59:3051–3086
https://doi.org/10.1007/s10579-025-09848-x
ORIGINAL PAPER
Detecting caste and migration hate speech in low‑resource 
Tamil language
Bharathi Raja Chakravarthi1,3 · Saranya Rajiakodi2 · Rahul Ponnusamy3 · 
Bhuvaneswari Sivagnanam2 · Sara Yogesh Thakare4 · Sathiyaraj Thangasamy5
Accepted: 16 May 2025 / Published online: 12 June 2025 
© The Author(s) 2025
Abstract
The Indian constitution categorizes its population into groups such as Scheduled 
Castes, Scheduled Tribes, Other Backward Classes, and Forward Castes, reflecting 
historical inequalities that influence social dynamics and discrimination. Migrants 
who are relocating within the country for better opportunities are often viewed 
as outsiders, leading to concerns about job security and crime, fostering hate and 
discrimination against them. Social media has exacerbated these issues, becom-
ing hotspots for caste and migration-related hate speech, especially in low-resource 
languages. This study introduces a novel dataset specifically curated to detect hate 
speech related to caste and migration in the low-resourced Tamil language. Using 
this dataset, we benchmarked the dataset with baseline experiments with the high-
est macro-F1 score of 0.73. We also created custom-modified models integrating 
custom loss functions, adapter-based fine-tuning, and parameter-efficient fine-tuning 
techniques. To support further research, we released the dataset, conducted a shared 
task, and ranked participant systems. By publicly releasing this dataset, we aimed to 
facilitate further study and improve the detection and mitigation of hateful content 
related to caste and migration on social media.
Keywords  Caste and migration hate speech · Low-resourced dataset creation · Large 
language models · Model optimization · Adapters · Parameter-efficient fine-tuning · 
Tamil
1  Introduction
The Indian constitution divides the people into four main social groups: Sched-
uled Castes (SC), Scheduled Tribes (ST), Other Backward Classes (OBC), and the 
General/Forward castes (FC). Title 341(1) says that “Scheduled Castes” are cer-
tain castes, races, tribes, or subgroups within castes or races (Kijima, 2006). The 
Constitution of India says that Scheduled Tribes are tribes or tribal communities, 
Extended author information available on the last page of the article

--- Page 2 ---

3052
	
B. R. Chakravarthi et al.
or certain parts or groups within the tribes or tribal communities, that are publicly 
recognized as those under Article 342 of the Constitution. According to the Man-
dal Commission (1978), people who are not in the Scheduled Castes or Scheduled 
Tribes groups are in the Other Backward Classes group. Other Backward Classes 
group have been pushed to the edges of society in the past, and they still face social, 
economic, and educational inequality. In addition, “forward castes” (FC) are social 
groups that don’t fit into any of the three groups listed above (Mal & Saikia, 2024; 
Rawal & Swaminathan, 2011; Shukla et  al., 2024). The caste system, which has 
been prevalent in India for many years, is a societal framework deeply rooted in 
religious and cultural norms. This system divides the population into a hierarchical 
structure of distinct classes (Binny, 2022). Caste is a very important factor in how 
people’s social and economic lives turn out in modern India. Unfairness is caused 
by a structured system, not just cultural identity, that decides who has benefits and 
disadvantages (Mosse, 2018).
Policymakers, governments, civil society groups, and experts working on local 
and European projects to track, stop, and fight the spread of casteism and xenopho-
bia in our Indian society all have different ideas about how to solve these problems 
(Abubakar et al., 2022). At the moment, experts from a number of different fields 
are focusing on mass media and different aspects of the language used in these set-
tings to find contrasting hate speech (Cuzzocrea et al., 2025). Data network analysis, 
social psychology, and discourse analysis are all fields that study and keep an eye 
on them (Arce-García et al., 2024). However, the problems they create make it dif-
ficult for artificial intelligence and computational linguistics to handle. It has been 
one of the hottest topics in Natural Language Processing (NLP), text classification, 
and opinion mining over the last few years to find hateful material on social media 
(Basile et al., 2019; Bosco et al., 2018).
Social media has become an integral part of our daily lives, which transforms 
the way we communicate, connect, and disseminate information (Chakravarthi 
et al., 2023a). Such a cyberworld enables users to share their viewpoints and artic-
ulate their opinions globally. It substantially impacts society, allowing us to influ-
ence everything around us. Nowadays, hate speech concerning sensitive topics are 
proliferating in social media platforms such as X (Twitter), YouTube and Facebook 
(Shanmugavelan, 2022). Globally, the detection of hate speech text across various 
realms on social media has become a pivotal field due to the growing prevalence 
of online hate speech and its likelihood to trigger real-world violence and discrimi-
nation (Rodríguez-Peral et al., 2025). Researchers across the world have developed 
various methodologies, including Machine Learning (ML), Deep Learning (DL) and 
NLP techniques, to identify and mitigate hate speech. However, the challenge lies 
in the nuances of language and cultural aspects of diverse regions across the world 
(Abubakar et al., 2022). In the context of Indian scenarios, the issue of caste and 
migration-related hate speech is particularly increasing on social media platforms 
because of India’s cultural heritage and historical caste-based discrimination (Banaji 
& Bhat, 2022).
Social media platforms have become hotbeds for people to comment on their 
opinions related to caste-based prejudices and anti-migrants, which typically 
leads to social unrest (Fouskas et al., 2022; Udupa, 2020). As India has diverse 

--- Page 3 ---

3053
Detecting caste and migration hate speech in low‑resource…
linguistics, Indian researchers have been developing algorithms to detect and flag 
content posted in native languages depending on the contextual understanding of 
caste and migrated-related derogatory comments (Pohjonen & Udupa, 2017). In 
states such as Tamil Nadu, located in the southern part of India, the caste systems 
are integrated in social and cultural contexts, particularly in rural areas (Rajiakodi 
et  al., 2024). Even in this contemporary society in Tamil Nadu, the caste sys-
tem periodically determines the different spheres of people’s lives, such as mari-
tal bonds, political manipulation, social interactions, and social status (Vaghela 
et al., 2022). People are using social media to spread hate speech against a par-
ticular caste, which intensifies the tension and even worsens the social divides. 
Offenders are exploiting anonymity to post hateful or inflammatory content by 
demeaning a particular caste without facing repercussions. In addition, such hate 
speech typically goes viral on social media and it easily reaches a vast audience, 
especially youth, so the digital spread of hate speech can lead to discrimination 
and further marginalization of vulnerable groups. Such hate speech not only 
affects the targeted caste but also facilitates an environment of anxiety and hostil-
ity (Kirasur & Jhaver, 2024).
In addition, another growing issue in Tamil Nadu in social media is hate speech 
targeting migrants, particularly with respect to interstate migrates from northern 
and eastern states of India like Bihar, Uttar Pradesh, West Bengal, Assam, and 
also from neighboring states who have moved to Tamil Nadu for employment 
and a better-quality life (Rawat et  al., 2024). Hate speech comments regarding 
migrants often involve blaming them for crime, accusing them of taking jobs 
away from local people, and even shaming their physical appearance. To address 
these challenges, a significant demand for NLP models is required that can effec-
tively handle the complexities of Tamil and code-mixed texts related to caste/
migration hate speech on social media.
Our research aims to bridge this gap by enhancing the development and imple-
mentation of advanced NLP techniques which are specially used to detect and 
classify caste/migration hate speech in Tamil and code-mixed (Tamil-English) 
texts on social media, as well as distinguishing it from not-caste/migration-related 
content, thereby it mitigates the spread of harmful content and promotes a more 
harmonious digital society.
Research Question: How can NLP models be effectively optimized and uti-
lized to detect and classify caste/migration-related hate speech in Tamil and 
code-mixed texts on social media platforms, considering its linguistic and cul-
tural features?
In this paper, we have discussed the key contributions of our work. They are as 
follows: 
1.	 We have curated the first ever novel dataset for detecting the hate speech related to 
caste/migration in the Tamil language and made it publically available for future 
research.
2.	 We provided the evaluation framework for this dataset and performed baseline 
experiments using various DL architectures.

--- Page 4 ---

3054
	
B. R. Chakravarthi et al.
3.	 We conducted experiments with the custom model by incorporating custom loss 
functions, Adapters, P-tuning and Low-Rank Adaptation (LoRA) techniques to 
improve its performance.
4.	 We performed an error analysis on the optimal model to identify its limitations 
and highlight potential areas for future enhancements.
5.	 We organized a shared task for researcher to measure various method’s perfor-
mance to the dataset.
2  Related work
The identification of hate speech has emerged as a significant issue in the age of 
social media and digital communication platforms. The use of offensive language 
is connected to a range of linguistic and social problems, including the use of abu-
sive and violent language, cyberbullying, racism, extremism, radicalization, toxicity, 
profanity, and hate speech. The surge in hate speeches has resulted in a growth in 
the quantity of corpora that annotate abusive languages. Zampieri et al. introduced 
a novel dataset in a study. This dataset provides a systematic structure for classify-
ing offensive language according to its type and intended recipient. Jeong et al. have 
recently presented a Korean abusive language dataset in their concurrent work. The 
dataset contains annotations for the target group, offensive span, target span, and 
level of offensiveness. They focus on justifying the decision for offensiveness by 
using additional activities, such as identifying the target of the insult and assessing 
the severity of the offense. The objective of this study is to enhance the accuracy 
of offensive content classification by integrating additional tasks such as Automatic 
Lexical Detection (ALD) and Sentiment Analysis (SA).
Researchers have been investigating many methods, such as machine learning, 
deep learning, and transformer-based models, to effectively address the increase 
in hate speech events (Fortuna & Nunes, 2018). The majority of study focuses on 
commonly spoken languages, such as English (Davidson et al., 2017; Waseem & 
Hovy, 2016). Nevertheless, the lack of a substantial corpus for Indian languages 
has impeded the advancement of NLP models, resulting in their limited explora-
tion (Chakravarthi et al., 2020; Ponnusamy et al., 2024). Transformer models for 
several Indian languages, including Hindi, Marathi, and Bengali, have been recently 
made available (Chhaya et al., 2024). The findings also indicate that models trained 
on monolingual datasets exhibit superior performance. Several significant contests, 
like SemEval 2018, SemEval 2019, HASOC 2020, and GermEval 2018, have been 
held to explore enhanced outcomes for NLP jobs. Researchers have collected data-
sets from many sources for languages other than English. This has facilitated the 
investigation of different methods and feature sets for detecting hate speech, such 
as machine learning techniques (Kumaresan et al., 2023; Sreelakshmi et al., 2024; 
Subramanian et al., 2022).
Recent advancements in deep learning methodologies have underscored the 
necessity of massive amounts of labeled data to achieve high performance (Brown 
et al., 2020; Liu et al., 2019). However, the majority of research in this area has pre-
dominantly focused on English and a few other major languages, leaving many other 

--- Page 5 ---

3055
Detecting caste and migration hate speech in low‑resource…
languages underrepresented and lacking in sufficient labeled datasets for training 
robust models (Bender et al., 2021; Hedderich et al., 2021). This disparity presents 
a significant challenge, particularly for low-resource languages, which often lack the 
volume of undesirable data needed for effective model training (Joshi et al., 2020; 
Nekoto et al., 2020).
Many low-resource languages have attempted to bridge this gap by developing 
their own language models. These models are typically created by collecting open-
source data available online and pretraining it to suit the specific linguistic features 
and usage of the language (Kakwani et al., 2020; Joshi et al., 2020). Subsequently, 
these pretrained models are fine-tuned for various specific tasks such as offensive 
language detection, hate speech identification, emotion detection, and translation 
(Hedderich et al., 2021; Ruder et al., 2019). Notably, Tamil is one such language 
where efforts have been made to develop tailored models to address its unique lin-
guistic needs (Chakravarthi et  al., 2021, 2024; Ponnusamy et  al., 2024; Premjith 
et al., 2024; Ravikiran et al., 2024). The advent of transformer-based models has sig-
nificantly transformed the field of NLP. These models have demonstrated superior 
performance across a range of tasks but come with the drawback of being resource-
intensive, particularly during the fine-tuning process (Devlin et al., 2019; Vaswani 
et al., 2017). Fine-tuning transformers for specific tasks can be prohibitively costly 
in terms of computational resources and time, which is a critical issue for many 
researchers and practitioners working with low-resource languages (Kaplan et al., 
2020; Raffel et al., 2020). Prior studies (Chakravarthi et al., 2021, 2023b; Kumare-
san et al., 2024; Subramanian et al., 2022; Waseem et al., 2017) have categorized 
offensive occurrences into two distinct groups: explicit and implicit. However, 
none of the aforementioned studies specifically tackle the problem of hate speech 
on caste and migration in the Indian context Tamil. This study is one of the few 
that addresses the problem of Tamil language caste hate by incorporating additional 
tasks that are important.
To mitigate these challenges, various methods have been introduced to optimize 
the fine-tuning process, making it more resource-efficient. One prominent approach 
is Adapter-based fine-tuning, which involves adding lightweight adapter modules 
to the pretrained models. These adapters can be fine-tuned for specific tasks while 
keeping the majority of the model’s parameters fixed, thus significantly reducing the 
computational cost (Houlsby et al., 2019). Additionally, Parameter-Efficient Fine-
Tuning (PEFT) techniques, such as LoRA, P-tuning, and Prompt tuning, have been 
developed. These techniques allow for effective fine-tuning by optimizing a smaller 
subset of parameters, thereby making the process more efficient and accessible (Hu 
et al., 2022; Lester et al., 2021; Liu et al., 2022).
These advancements are particularly relevant for detecting hate speech and other 
forms of offensive content in low-resource languages like Tamil. By leveraging opti-
mized fine-tuning techniques, researchers can develop models that are both effective 
and resource-efficient, enabling broader application and deployment in real-world 
settings. This is crucial for addressing the nuanced and culturally specific forms of 
hate speech that are prevalent on social media platforms, especially in linguistically 
diverse regions such as India (Chakravarthi et al., 2021; Subramanian et al., 2022). 
In our work, we have created a standard dataset for the automatic detection of hate 

--- Page 6 ---

3056
	
B. R. Chakravarthi et al.
speech on caste or migrants in Tamil language. We experimented with various tech-
nique, starting from traditional fine-tuning to recent PEFT methods with the adapt-
ers. The detailed explanation of the dataset creation and the performance of all the 
experiments conducted are clearly discussed in the upcoming sections.
3  Dataset
The caste/migration hate speech detection dataset is one of its kind which focuses on 
identifying the hateful/abusive/derogatory comments directed against certain castes 
or migrated people in Tamil Nadu. It is collected as a part of ongoing research on 
developing a model for automatically detecting harmful content towards a certain 
community of people. Because of the increasing number of abusive comments on 
social media platforms, a need for this dataset in NLP for low-resource languages is 
crucial, especially for Tamil. So this dataset plays a crucial role in detecting abusive 
and derogatory comments. It also focuses on various forms of hate speech and pro-
vides unique insights into regional and cultural-specific discrimination. The work-
flow of the dataset design is, we start with the data collection process, then proceed 
with data preprocessing, annotation of the dataset and splitting the dataset into train-
ing, testing, and validation of the dataset for our task.
3.1  Collection
For creating a caste/migration hate speech detection dataset, we need to collect the 
good quality data. For this step, the dataset has been carefully curated from the You-
Tube platform by gathering comments from videos discussing caste and migration-
related issues. The reason why the YouTube platform has been chosen is for its 
diverse social interactions so that we can get various kinds of public opinion and 
social debates. It is the first ever dataset that has been solely focusing on caste and 
migration hate speech in Tamil language.
To collect the comments from the YouTube videos, we have used one of the 
Python libraries named “youtube-comment-scraper”.1 This tool has scraped the 
YouTube comments of the given videos including the replies of these comments 
and these replies have been considered as separate comments. The videos have been 
chosen based on hashtags and by manual key searches. The below illustrated word 
cloud representation that highlights various hashtags, including ‘vadakan’ (North 
Indian), ‘devar’ (caste) and more shown in Fig.  1 and manual keywords such as 
‘Agamudiyar’ (caste), ‘Melpathi temple issue’ (a particular caste named devar) and 
others shown in Fig. 2 which are in both Tamil and code-mixed (Tamil-English). 
The words illustrated in the word clouds are the most frequently used keywords to 
choose the YouTube videos. Figure 1 listed the hashtags used for the search, whereas 
1  https://​github.​com/​belli​ngcat/​youtu​be-​comme​nt-​scrap​er.

--- Page 7 ---

3057
Detecting caste and migration hate speech in low‑resource…
Fig. 2 describes the keywords related to certain events associated with the debate of 
the issues pertaining to caste/migration.
3.2  Data preparation
The second step in the dataset design is data pre-processing or data preparation. In 
this step, we proceeded to remove unrelated content from the collected YouTube 
comments like removing usernames, removing URLs and removing sentences that 
contained less than three words. Figure 3 describes the most frequently used words 
in the dataset. After collecting a total of 10,173 comments, we retained 7875 for 
annotation following the preprocessing step.
3.3  Annotation
The crucial task of constructing a dataset is annotation. The annotation process for 
this task involves three annotators who will be manually annotating a total of 7875 
comments. These human experts will annotate the comments into two different cate-
gories, such as Hate speech on caste/migration which has been labeled as 1 and Not-
hate speech on caste/migration has been labeled as 0. Before sending the data to the 
annotators, we removed all kinds of personal information and privacy related data 
from the comments, which is done in the data pre-processing step. It is to ensure the 
confidentiality and privacy of the commentator.
Each comment is annotated by three annotators. If there is any disagreement in 
determining the label for a comment, the final decision will be based on the major-
ity vote. Specifically, if two out of the three annotators assign the same label to the 
comment, that label will be adopted. For this annotation task, the annotators are all 
well-versed in the Tamil language. The group of heterogeneous annotators compris-
ing individuals from various castes including historically marginalized and domi-
nant groups, different age groups from young-adults (between 20 and 29 years old) 
to middle-aged (between 30 and 45 years old), gender and professional experience. 
Figure 4 illustrates the example of sample dataset after the meticulous annotation, 
and Table 2 shows the information about the annotators.
3.3.1  Annotation guidelines
To do annotation in this task, we have a set of guidelines given to the annotators. 
First, it is mentioned in our guidelines that there are two categories: Hate speech on 
caste/migration and Not-hate speech on caste/migration. Below are the definition for 
each category:
•	 Hate speech on caste/migration: Comments that include abusive, disrespect-
ful, discriminatory language, as well as ridiculing and mockery, and content that 
aims to delegitimize certain caste or migrated individuals.

--- Page 8 ---

3058
	
B. R. Chakravarthi et al.
•	 Not-Hate speech on caste/migration: Comments that do not include any dis-
criminatory or derogatory remarks towards individuals based on their caste/
migration status.
In the second step, the annotators have to read through the entire comment and 
make sure that the entire context is understandable. After that, they have to mark 
the labels. For example, specific criteria are used to determine whether the con-
text is hate speech related to caste (Fig. 5) or migration (Fig. 6). These criteria 
include terms such as vadakan, marvadi, parayan, vaduka pallan, vaellalar, and 
mukkulathor.
3.3.2  Annotation difficulties
In this section, we will be discussing the difficulties faced by the annotators doing 
annotation process. The annotator finds it challenging to determine the intended 
context of comments that contain words related to multiple genres, such as work, 
play, and others. Another problem encountered during annotation is the mix of 
Fig. 1   This illustrated word cloud represented the hashtags used for the YouTube video search

--- Page 9 ---

3059
Detecting caste and migration hate speech in low‑resource…
languages, such as Hindi within Tamil comments, which makes it difficult to 
understand the meaning of the comments. Example for annotation difficulties: 
Fig. 7.
3.4  Inter annotator agreement (IAA)
To determine the quality of annotated data, Statistical measures such as Cohen’s 
kappa, Fleiss kappa, Scott’s pi, or Krippendorff’s alpha will be used (Lombard et al., 
2010). For this task, we have chosen Krippendorff’s alpha measure.
The reason for choosing Krippendorff’s alpha is that it can handle various data types 
and missing values in case one of the annotators does not label all the items in the 
dataset. It can be used when there are more than two annotators, and if it achieves 
Krippendorff’s alpha score more than 0.80, then there is a strong agreement and 
considered reliable. For our task, the Krippendorff’s score is 0.83441.
(1)
훼= 1 −Do ÷ De
Fig. 2   This illustrated word cloud displays the words used for the manual search of certain issues related 
to caste/migration from the YouTube videos

--- Page 10 ---

3060
	
B. R. Chakravarthi et al.
4  Experimental setup
In our experimental setup, we leveraged a powerful computational environment to 
facilitate efficient processing and thorough analysis. The core hardware component 
was the Nvidia Tesla V100 GPU, chosen for its exceptional performance in handling 
intensive computational tasks. The system was equipped with 156 GiB of RAM, 
which ensured ample memory capacity for managing large-scale datasets and large 
language learning models. The GPU featured 16 GiB of dedicated memory, ena-
bling efficient processing of graphics-intensive operations. Our operating system of 
choice was Ubuntu, selected for its stability and compatibility with a wide range of 
Fig. 3   This word cloud represents the visual summary of the whole dataset, highlighting the frequent 
terms. The word ‘Tamil’ appears the most in the dataset

--- Page 11 ---

3061
Detecting caste and migration hate speech in low‑resource…
machine learning frameworks. Python was utilized as the primary programming lan-
guage, owing to its extensive library support and strong community. For coding and 
development, we employed the VS Code editor, which provided a robust and flexible 
environment for writing and managing code. This setup was critical in ensuring a 
stable and effective platform for conducting our experimental procedures. Table 3 
provides an overview of the hardware and software configurations employed.
The dataset was divided into three parts, such as training, development, and test-
ing sets, with ratios of 65, 15, and 20% to ensure comprehensive analysis and sup-
port effective model training. The accompanying Table 1 gives the breakdown of the 
comments distributed across these subsets. The multilingual models (obtained from 
Hugging Face2) used in these experiments are: 
1.	 bigscience/bloom-560 m3
2.	 google/muril-base-cased4
3.	 ai4bharat/indic-bert5
4.	 l3cube-pune/tamil-bert6
5.	 l3cube-pune/tamil-sentence-bert-nli7
6.	 FacebookAI/xlm-roberta-base8
7.	 facebook/xmod-base9
All of these models are multilingual and are suitable for working in the Tamil lan-
guage. They have been used for the downstream task of sequence classification. We 
performed experiments with 5 different learning rates to find each model’s best pos-
sible learning rate, keeping all other parameters constant. The configurations used 
were as follows: weight_decay: float = 0.01. We employed the AdamW optimizer10 
with the following parameters: Beta1: 0.9, Beta2: 0.999, adam_epsilon: float = 
1e-08. The training was conducted for 5 epochs, as this is the standard for train-
ing transformer models, with a batch size of 8, which optimizes memory usage and 
allows efficient training on GPUs. All models were implemented in the PyTorch11 
framework.
2  https://​huggi​ngface.​co/​models.
3  https://​huggi​ngface.​co/​bigsc​ience/​bloom-​560m.
4  https://​huggi​ngface.​co/​google/​muril-​base-​cased.
5  https://​huggi​ngface.​co/​ai4bh​arat/​indic-​bert.
6  https://​huggi​ngface.​co/​l3cube-​pune/​tamil-​bert.
7  https://​huggi​ngface.​co/​l3cube-​pune/​tamil-​sente​nce-​bert-​nli.
8  https://​huggi​ngface.​co/​Faceb​ookAI/​xlm-​rober​ta-​base.
9  https://​huggi​ngface.​co/​faceb​ook/​xmod-​base.
10  https://​pytor​ch.​org/​docs/​stable/​gener​ated/​torch.​optim.​Adam.​html.
11  https://​pytor​ch.​org/.

--- Page 12 ---

3062
	
B. R. Chakravarthi et al.
4.1  Fine‑tuning
The pretrained models utilized to address this problem were selected based on 
their effectiveness in processing the Tamil language and knowledge from the Tamil 
culture which are listed below. BLOOM: BLOOM (BigScience Large Open-sci-
ence Open-access Multilingual Language Model) (Scao et  al., 2022) is based on 
a Decoder-only architecture derived from Megatron-LM’s GPT2. For our task we 
used BLOOM-560 m, it has 559,214,592 total parameters, with 256,901,120 param-
eters dedicated to embeddings. It operates with 24 layers, each utilizing 16 attention 
heads. The hidden layers within BLOOM are 1024-dimensional, and it processes 
sequences up to 2048 tokens in length. The model is trained using the Cross Entropy 
objective function with mean reduction. To train BLOOM, the ROOTS corpus (Lau-
rençon et al., 2022) was utilized, which comprises diverse sources in 46 natural lan-
guages and 13 programming languages, totaling 59 languages in total.
IndicBERT: IndicBERT (Kakwani et al., 2020) is a multilingual ALBERT model 
that has been trained on extensive corpora encompassing 12 major Indian languages, 
totaling 9 billion tokens and occupying a storage size of 120 GB. ALBERT was 
selected as the foundational model due to its reduced parameter count, facilitating 
easier distribution and deployment in various downstream applications.
MuRIL: MuRIL (Khanuja et  al., 2021) is a multilingual model based on the 
BERT architecture. It was pre-trained from scratch using a combination of datasets 
including Wikipedia, Common Crawl, PMINDIA, and Dakshina corpora, which 
cover 17 Indian languages. MuRIL is trained on both parallel and monolingual seg-
ments of these datasets. The model utilizes a self-supervised masked language mod-
eling task during training to learn language representations effectively.
TamilBERT: Existing multilingual models like MuRIL, XLM-RoBERTa, and 
IndicBERT have been fine-tuned on monolingual corpora. This process has resulted 
in models specifically tailored for Hindi, termed as HindBERT, HindRoBERTa, 
and HindAlBERT, as well as corresponding Devanagari-specific models named 
DevBERT,12 DevRoBERT,13 and DevAlBERT.14 These models have demonstrated 
excellent performance on various tasks such as classification and Named Entity 
Recognition (NER). Building on the success of HindBERT and DevBERT, mono-
lingual models have been released for other Indian languages including Kannada, 
Telugu, Malayalam, Tamil, Gujarati, Assamese, Odia, Bengali, and Punjabi. These 
models are respectively referred to as Kannada-BERT,15 Telugu-BERT,16 Malay-
alam-BERT,17 Tamil-BERT,18 Gujarati-BERT,19 Assamese-BERT,20 Odia-BERT,21 
12  https://​huggi​ngface.​co/​l3cube-​pune/​hindi-​marat​hi-​dev-​bert.
13  https://​huggi​ngface.​co/​l3cube-​pune/​hindi-​marat​hi-​dev-​rober​ta.
14  https://​huggi​ngface.​co/​l3cube-​pune/​hindi-​marat​hi-​dev-​albert.
15  https://​huggi​ngface.​co/​l3cube-​pune/​kanna​da-​bert.
16  https://​huggi​ngface.​co/​l3cube-​pune/​telugu-​bert.
17  https://​huggi​ngface.​co/​l3cube-​pune/​malay​alam-​bert.
18  https://​huggi​ngface.​co/​l3cube-​pune/​tamil-​bert.
19  https://​huggi​ngface.​co/​l3cube-​pune/​gujar​ati-​bert.
20  https://​huggi​ngface.​co/​l3cube-​pune/​assam​ese-​bert.
21  https://​huggi​ngface.​co/​l3cube-​pune/​odia-​bert.

--- Page 13 ---

3063
Detecting caste and migration hate speech in low‑resource…
Bengali-BERT,22 and Punjabi-BERT.23 For our task, we used Tamil-BERT (Joshi, 
2022) for our task.
TamilSBert: Sentence-BERT (SBERT) adapts the BERT architecture and fine-
tunes pre-trained BERT models specifically for generating sentence embeddings. 
SBERT incorporates additional training techniques aimed at enhancing the effec-
tiveness of training sentence embeddings. The model is trained using supervised 
datasets such as Natural Language Inference (NLI) and Semantic Textual Similar-
ity (STS), which aid in capturing sentence semantics. TamilSBERT (Deode et al., 
2023), also known as TamilBERT, is a variant trained specifically for Tamil. It 
leverages the NLI dataset, which has been translated into Tamil through machine 
translation from the original English version. This adaptation ensures that the model 
learns to encode meaningful representations of Tamil sentences based on the seman-
tics inferred from the NLI tasks.
XLM-RoBERTa: XLM-RoBERTa is a multilingual version of RoBERTa that has 
been pre-trained on a substantial dataset from CommonCrawl, amounting to 2.5TB 
of filtered data covering 100 languages (Conneau et  al., 2020). This model, like 
RoBERTa, employs a transformer-based architecture and is pre-trained in a self-
supervised manner. Specifically, XLM-RoBERTa (XLM-R) (Conneau et al., 2020) 
is pre-trained using the Masked Language Modeling (MLM) objective. In MLM, 
15% of the words in a sentence are randomly masked, and the model is tasked with 
predicting these masked words based on the context provided by the entire sentence. 
This differs from traditional recurrent neural networks (RNNs) that process words 
sequentially or autoregressive models like GPT that internally mask future tokens. 
Table 1   This table shows the 
distribution of sentence in the 
dataset after annotation
Sets
Hate speech on 
caste/migration
Not-Hate speech on 
caste/migration
Total
Train
2052
3303
5355
Development
351
594
945
Test
602
973
1575
Total
3005
4870
7875
Table 2   Annotator’s 
demographics
In Age group column Young-adults denoted the annotators age is 
between 18 and 25.Middle-aged denoted between 26 and 45
Gender
Qualification
Age group
Male
PhD
Middle-aged
Female
PG
Young-adults
Female
PG
Young-adults
22  https://​huggi​ngface.​co/​l3cube-​pune/​benga​li-​bert.
23  https://​huggi​ngface.​co/​l3cube-​pune/​punja​bi-​bert.

--- Page 14 ---

3064
	
B. R. Chakravarthi et al.
The bidirectional nature of sentences is effectively captured through this approach, 
allowing the model to learn contextual representations that account for both preced-
ing and following words in the input sequence.
XMOD: X-MOD (Pfeiffer et  al., 2022) is a multilingual masked language 
model that has been trained on filtered CommonCrawl data, which includes con-
tent from 81 different languages. Unlike previous multilingual models such as 
XLM-R (Conneau et al., 2020), X-MOD introduces a novel approach by incor-
porating language-specific modular components known as language adapters 
during its pre-training phase. In X-MOD, these language adapters are frozen 
in each transformer layer during fine-tuning, enabling efficient adaptation to 
Fig. 4   The sample annotated comments from dataset with the translation. The label “Hate” means the 
hate speech related to caste/migration, and “Not-Hate” means not hate speech related to caste/migration

--- Page 15 ---

3065
Detecting caste and migration hate speech in low‑resource…
specific languages without modifying the underlying model architecture. Moreo-
ver, X-MOD utilizes the same tokenizer as XLM-R, ensuring compatibility and 
leveraging existing infrastructure for tokenization across languages. This design 
Fig. 5   The sample comment related to caste hate speech from the dataset. The text inside the purple box 
is the comment and the blue box is the translation
Fig. 6   The sample comment related to migration hate speech from the dataset. The text inside the purple 
box is the comment and the blue box is the translation
Fig. 7   The sample comment from the dataset, which we found difficult to annotate is outlined in purple 
box. The yellow box contains explanation of the difficulties encountered during an annotation process

--- Page 16 ---

3066
	
B. R. Chakravarthi et al.
choice facilitates seamless integration into existing frameworks and workflows 
that are based on XLM-R or similar models.
4.1.1  Default loss
All models were trained using 5 different learning rates over 5 epochs, alongside 
other specified hyperparameters. The objective was to determine the optimal learn-
ing rate that maximizes performance for each model. The selected learning rates for 
the experiment were: 1.00E−05, 2.00E−05, 3.00E−05, 4.00E−05, and 5.00E−05. 
The learning rate yielding the highest macro F1-score was chosen as the best for 
each model.
Following the evaluation of baseline models, further experiments were conducted 
to enhance their performance. These experiments involved the implementation of 
custom loss functions, adapter modules, and parameter-efficient fine-tuning strate-
gies. The objective was to optimize model refinement and improve their effective-
ness in specific tasks or domains.
4.1.2  Custom loss
The three following loss functions were chosen for the experiments. 
1.	 KL divergence Loss: The Kullback–Leibler (KL) divergence, denoted as 
KL(P||Q) , is a statistical measure that quantifies how one probability distribu-
tion P diverges from another reference distribution Q . In the context of evaluating 
model outputs against true labels, P typically represents the predicted distribution 
while Q represents the actual distribution of the labels.
	
  A higher KL divergence score indicates greater dissimilarity between the two 
distributions P and Q . Conversely, a KL divergence score of zero signifies that 
the distributions P and Q are identical. 
 where yc = True labels, ̂yc = Predictions.
(2)
KL(yc||̂yc) =
M
∑
c=1
̂yc log ̂yc
yc
Table 3   Specifications of the 
experimental platform used for 
model training and evaluation
Item name
Specifications
GPU
Nvidia Tesla V100
RAM
156 GiB
GPU RAM
16 GiB
OS
Ubuntu
Language
Python
IDE
VS Code editor

--- Page 17 ---

3067
Detecting caste and migration hate speech in low‑resource…
2.	 Hinge Loss: The hinge loss is another popular loss function used for training 
classifiers. The hinge loss of the prediction y is defined as: 
 Where, t = ±1 and y is the “raw” output of the classifier’s decision function
3.	 Binary Cross Entropy Loss: Binary Cross Entropy is the negative average of the 
log of corrected predicted probabilities. 
 where y = True labels, p(̂y) = Probability of predicted label.
4.2  Adapter based fine‑tuning
In each layer of a Transformer model, Bottleneck adapters (Hu et al., 2023) intro-
duce bottleneck feed-forward layers characterized by a W_down matrix for down-
projection, reducing the dimensionality d_bottleneck of layer hidden states, an acti-
vation function f , W_up for up-projection restoring the original dimension, and a 
residual connection r.
These layers can be incorporated at various positions within a Transformer block 
based on the adapter configuration. Further customization is possible for layer 
norms, activation functions, residual connections, and bottleneck sizes. The bottle-
neck dimension d_bottleneck stands out as a crucial configuration hyperparameter. 
It is indirectly defined through the reduction_factor attribute in the configuration, 
representing the ratio between a model’s layer hidden dimension and the bottleneck 
dimension, i.e.:
Figure 8 provides a visual representation of additional configuration options pertain-
ing to the adapter structure. This adapter is implemented with the help of “BnCon-
fig” from AdapterHub24 and LLM-Adapters package (Hu et al., 2023).
4.3  Parameter‑efficient fine‑tuning
Parameter-efficient fine-tuning (PEFT)25 is a technique employed in NLP to enhance 
the performance of pre-trained language models when applied to specific down-
stream tasks. Unlike traditional fine-tuning where all layers and parameters of the 
pre-trained model are adjusted, PEFT selectively freezes certain layers and focuses 
(3)
HL(y) = max(0, 1 −t ⋅y)
(4)
BCE = −[y ∗log(p(̂y)) + (1 −y) ∗log(1 −p(̂y))])
(5)
h ←Wup ⋅f(Wdown ⋅h) + r
(6)
reduction_factor =
dhidden
dbottleneck
24  https://​docs.​adapt​erhub.​ml/​metho​ds.​html.
25  https://​huggi​ngface.​co/​docs/​peft/​index.

--- Page 18 ---

3068
	
B. R. Chakravarthi et al.
solely on fine-tuning the last few layers relevant to the new task. This strategy con-
serves computational resources and time compared to full fine-tuning from scratch. 
Moreover, PEFT enables effective adaptation of the model to new tasks even when 
limited labeled data is available. By targeting only the essential parameters for the 
task at hand, PEFT optimizes efficiency without compromising performance, mak-
ing it a practical choice for scaling up models in resource-constrained environments.
4.3.1  P‑tuning
In P-tuning,26 the traditional discrete prompt is augmented with trainable continu-
ous prompt embeddings, which serve as additional learnable parameters. Unlike 
manually designed text prompts, these continuous embeddings are optimized via 
backpropagation, enhancing both stability and effectiveness in steering a pre-trained 
language model (LM). Figure  9 illustrates the workflow of the P-Tuning mecha-
nism. Specifically, let M denote a pre-trained language model with a hidden size h 
and a vocabulary size V . Consider a labeled dataset (xi, yi) for an NLU task, where 
x0∶n = {x0, x1, … , xn} forms a sequence of discrete tokens constituting the input, 
and y ∈Y represents a label. The objective is to estimate the conditional probability 
fM(x) = ̂p(y|x) , with M ’s parameters either fine-tuned or frozen. Recognizing that 
discrete prompts often exhibit high instability and suboptimal behavior under back-
propagation, P-Tuning introduces continuous prompt embeddings to enhance stabil-
ity and effectiveness in prompting.
The 
prompt 
template 
used 
in 
P-Tuning 
is 
structured 
as 
follows: 
T = {[P0∶i
], x, [P(i+1)∶j
], y, [P(j+1)∶k
]}
 , where each 
[Pi
]
 represents the (ith) con-
tinuous prompt embedding. P-Tuning incorporates an additional embed-
ding 
function 
f ∶[Pi
] →hi , 
which 
maps 
the 
template 
to 
h0, … , hi, 
e(x), hi+1, … , hj, e(y), hj+1, … , hk . These embeddings are then updated, [Pi
]k
i=1 , to 
optimize a task-specific loss function. Importantly, P-Tuning is applicable to both 
frozen and fine-tuned language models, demonstrating versatility across different 
model configurations.
4.3.2  LoRA
LoRA,27 or Low-Rank Adaptation of large language models (Hu et  al., 2022), is a 
technique in PEFT aimed at reducing the number of trainable parameters. It achieves 
this by integrating trainable rank decomposition matrices into each layer of the Trans-
former architecture, thereby decreasing the number of trainable parameters for sub-
sequent tasks. It’s crucial to emphasize that the parameters of the original pre-trained 
transformer remain static. Aghajanyan et al. demonstrate that over-parametrized mod-
els learned on a low intrinsic dimension support the hypothesis that weight changes 
during model adaptation also possess a low “intrinsic rank”, forming the foundational 
26  https://​huggi​ngface.​co/​docs/​peft/​packa​ge_​refer​ence/p_​tuning.
27  https://​huggi​ngface.​co/​docs/​peft/​packa​ge_​refer​ence/​lora.

--- Page 19 ---

3069
Detecting caste and migration hate speech in low‑resource…
Fig. 8   Adapter architecture

--- Page 20 ---

3070
	
B. R. Chakravarthi et al.
principle of LoRA. The study additionally asserts that LoRA enables the indirect train-
ing of select dense layers within a neural network by optimizing rank decomposition 
matrices of these layers’ adaptations, all while maintaining the frozen state of pre-
trained weights.
Figure 10 shows the work flow of LoRA. “d” represents the number of input fea-
tures and “h” represents the number of output features, and they are connected through 
the weight matrix that transforms the ‘d’-dimensional input into an ‘h’-dimensional 
output. A pre-trained weight matrix ‘ W0 ’ is expressed using a low-rank decomposition 
to constrain its updates:
(7)
W0 + ΔW = W0 + BA
Fig. 9   Working diagram of P-Tuning
Fig. 10   Working diagram of LoRA technique. In this figure, ‘x’ represents the number of input features, 
where ‘d’ denotes the dimensionality of x. Similarly, ‘h’ represents the number of output features, where 
‘h’ corresponds to the dimension of the transformed input

--- Page 21 ---

3071
Detecting caste and migration hate speech in low‑resource…
During training, W0 remains frozen and does not receive gradient updates, while A 
and B consist of trainable parameters. For h = W0x , the modified forward pass is 
given by:
Initially, A is randomly initialized using a Gaussian distribution, and B is initial-
ized to zero, ensuring that ΔW = BA is zero at the start of training. In the Trans-
former architecture, there are four weight matrices in the self-attention module 
( Wq, Wk, Wv, Wo ) and two in the MLP module. LoRA adapts only the attention 
weights for downstream tasks while freezing the MLP modules. In summary, the 
LoRA technique decomposes the weight matrix into low-rank matrices that are 
trained and updated, keeping all the pre-trained model parameters frozen. After 
training, the low-rank matrices are incorporated back into the original weights. This 
approach simplifies training and storage of LoRA models due to the significantly 
reduced number of parameters.
5  Results
The performance of our models was based on the macro-F1 metric, calculated using 
the scikit-learn28 library. This metric is used because it provides insights into both 
the overall effectiveness of the models and their ability to manage class imbalances, 
which is particularly challenging in the context of caste and migration-related hate 
speech detection. In this study, the efficacy of the language models was assessed 
using a dedicated test set. Tables 4 and 5 shows the results of the baseline and the 
custom methods.
A classification layer was appended to the pre-trained models to fine-tune the 
models using the training set for the baseline results. The performance of these 
fine-tuned models on the test set varied significantly based on the learning rates 
and pre-trained weights used. Among the tested models, TamilSBERT demon-
strated the highest performance with a macro-F1 score of 0.70 at a learning rate 
of 2.00E−05, highlighting its effectiveness in handling the task. Other competitive 
models included Bloom-560 m, Muril-base-cased, and xmod-base, each achieving 
a score of 0.69 with optimal learning rates of 4.00E−05, 2.00E−05, and 3.00E−05, 
respectively. Tamil-BERT followed closely with 0.67 at 1.00E−05, while Indic-
BERT achieved 0.63 at the same learning rate. In contrast, XLM-RoBERTa base 
underperformed, scoring only 0.50 at its best learning rate of 1.00E−05, suggesting 
its limitations in this specific task. These results indicate TamilSBERT’s superior 
contextual understanding, while XLM-RoBERTa and IndicBERT may require fur-
ther optimization for better performance.
Next, we explored custom models by modifying loss functions and integrating 
adapter and PEFT techniques, using the optimal learning rates identified in the 
(8)
h = W0x + ΔWx = W0x + BAx
28  https://​scikit-​learn.​org/​stable/.

--- Page 22 ---

3072
	
B. R. Chakravarthi et al.
baseline experiments to enhance model performance. The results varied significantly 
based on the techniques applied. Among the loss functions tested, KL loss proved 
the most effective, enabling Bloom-560 m to achieve the highest macro-F1 score of 
0.73, marking a substantial improvement over its baseline. BCE loss also contrib-
uted to incremental gains, improving TamilBERT by 2% (0.69), TamilSBERT by 
1% (0.69), and significantly boosting XLM-RoBERTa by 18% (0.68). In contrast, 
Hinge loss consistently yielded poor performance (0.22−0.47) across all models, 
indicating its unsuitability for this task. For adapter-based techniques, the bottle-
neck adapter with XMOD reached 0.59, though it remained below the fine-tuning 
results. The LoRA (PEFT) technique improved XMOD to 0.62, but still fell short of 
KL loss, which performed 7% better. Similarly, P-tuning (PEFT) with Bloom-560 m 
achieved a macro-F1 score of 0.51, showing limited improvements.
Overall, Bloom-560 m fine-tuned with KL loss at a learning rate of 4.00E−05 
outperformed all other models and methods, achieving the best macro-F1 score of 
0.73. This superior performance can be attributed to the KL loss function’s effec-
tiveness in handling the nuances of caste and migration-related hate speech detec-
tion. The KL loss function likely helped the model better differentiate between sub-
tle variations in the text, which is crucial for accurately identifying hate speech. This 
result underscores the importance of selecting an appropriate loss function to opti-
mize model performance in complex NLP tasks. These findings indicate that choos-
ing the right loss function has a greater impact on model performance than using 
adapter-based or PEFT techniques, as even the best adapter-based methods fell short 
of fine-tuning with KL loss. Furthermore, while BCE loss helped certain models, its 
improvements were marginal compared to KL loss, emphasizing that loss function 
choice plays a pivotal role in improving classification accuracy for nuanced text-
based tasks.
6  Error analysis
Error analysis is crucial in understanding the limitations of our classification model 
and identifying patterns in misclassification. Despite achieving high performance, 
the BLOOM with KL loss model occasionally misclassifies comments due to vari-
ous linguistic complexities, including metaphorical expressions, context sensitiv-
ity, and reliance on specific keywords. In this section, we analyze five misclassi-
fied examples to highlight possible reasons for incorrect predictions and suggest 
improvements. Figure 11 presents the five misclassified examples along with their 
transliteration and translation, aiding in a deeper understanding of the errors. The 
misclassifications fall into several categories, including keyword-based misclassifi-
cation, failure to recognize indirect hate speech, challenges with Romanized Tamil, 
difficulties with informal and dialectal variations, and over-sensitivity to identity-
based discussions.
One such case is Comment ID 50, where the model misclassified a non-
hate speech comment as hate speech. The phrase “Karuppu” (black) was mis-
interpreted as a racial or casteist term, though in this context, it metaphorically 
referred to “black sheep” within the Tamil community. The error stemmed from 

--- Page 23 ---

3073
Detecting caste and migration hate speech in low‑resource…
keyword-based misclassification, where the system over-relied on specific words 
rather than understanding their contextual meaning. Similarly, Comment ID 82 
expressed concerns about financial exploitation, suggesting that an unnamed 
group benefits at the expense of Tamilians. Though the comment implicitly rein-
forces an “Us vs. Them” narrative-often present in migration-related hate speech-
the model misclassified it as non-hate speech. This error highlights the model’s 
failure to detect implicit bias and exclusionary rhetoric, likely due to its depend-
ence on explicit identity markers. In Comment ID 96, the model misclassified a 
comment targeting the Marwari (Marvadi—people originating from the Marwar 
region of Rajasthan, India) community as non-hate speech. A key reason for this 
misclassification was Romanized Tamil confusion-since the comment was written 
in English letters instead of Tamil script, the model struggled to correctly inter-
pret its meaning. Additionally, informal Tamil and slang usage further compli-
cated detection, as the phrase “thimir pidichavanugha” (arrogant people) is a col-
loquial expression that may not have been well-represented in the training data.
Further, Comment ID 136 blended formal and informal Tamil, making it 
harder for the model to classify it correctly. The statement promoted exclusion-
ary political rhetoric, arguing that jobs should be reserved exclusively for Tamil 
Table 4   Baseline results with selective learning rates with various LLMs assessed with macro-F1 score
Highest values are highlighed in bold
Learning rates
BLOOM
MuRIL
TamilBERT
TamilSBert
XLM-RoBERTa
XMOD
IndicBERT
1.00E−05
0.63
0.65
0.67
0.68
0.50
0.67
0.62
2.00E−05
0.54
0.69
0.66
0.70
0.38
0.67
0.62
3.00E−05
0.65
0.38
0.64
0.69
0.38
0.69
0.63
4.00E−05
0.69
0.38
0.64
0.38
0.38
0.38
0.38
5.00E−05
0.54
0.38
0.38
0.57
0.38
0.38
0.38
Table 5   Results of the custom models with the modification of custom loss, Adapter and PEFT tech-
niques assessed with macro-F1 score
Highest values are highlighed in bold
Methods
BLOOM
MuRIL
TamilBERT
TamilSBert
XLM-RoB-
ERTa
XMOD
IndicBERT
4.00E−05
2.00E−05
1.00E−05
2.00E−05
1.00E−05
3.00E−05
3.00E−05
Default loss
0.69
0.69
0.67
0.68
0.50
0.69
0.63
BCE loss
0.42
0.38
0.69
0.69
0.68
0.38
0.38
KL loss
0.73
0.38
0.38
0.38
0.38
0.38
0.38
Hinge loss
0.22
0.28
0.28
0.28
0.28
0.28
0.28
Bottleneck 
adapter
0.47
0.38
0.38
0.39
0.39
0.59
0.40
LoRA 
(PEFT)
0.58
0.38
0.38
0.38
0.44
0.62
0.38
P-tuning 
(PEFT)
0.51
0.38
0.38
0.38
0.38
0.38
0.38

--- Page 24 ---

3074
	
B. R. Chakravarthi et al.
speakers. The model misclassified this as non-hate speech due to difficulties in 
analyzing mixed-style language and informal dialects, as well as challenges in 
recognizing coded exclusionary speech. Similarly, Comment ID 121 was wrongly 
classified as hate speech due to over-sensitivity to identity-based statements. The 
comment discussed government job allocations, arguing that non-Tamil officials 
prioritize hiring individuals from their own states. While this could contribute 
to regional bias, the comment itself lacks explicit slurs or aggressive language, 
making it more of a policy concern than hate speech. The model’s inability to 
differentiate between political/economic complaints and actual hate speech likely 
led to this false positive.
To address these misclassifications in future, the model must be enhanced with 
deeper contextual understanding, allowing it to analyze full sentence meanings 
rather than relying on specific keywords. Metaphor recognition should be improved 
to distinguish between figurative language and explicit hate speech, preventing 
errors such as the one in Comment ID 50. Additionally, self-criticism differentia-
tion should be refined to prevent misclassifying intra-community criticism as hate 
speech. Recognition of indirect hate speech must be strengthened to detect implicit 
biases and exclusionary rhetoric, even when explicit identity markers are absent, 
which would help resolve errors like those in Comment ID 82. Furthermore, the 
model must recognize “Us vs. Them” narratives and be trained on Romanized 
Tamil, slang, and informal speech to better classify hate speech written in mixed-
language contexts. Coded exclusionary speech detection should be enhanced to 
capture political rhetoric that indirectly promotes discrimination while ensuring the 
model can distinguish policy discussions from actual hate speech. Finally, the model 
should reduce over-sensitivity to identity-related discussions, ensuring that factual 
demographic statements are not unnecessarily flagged. Implementing these refine-
ments will significantly enhance the system’s ability to detect nuanced hate speech 
while reducing both false positives and false negatives.
7  Shared task overview
7.1  Task description
A shared task named “Caste and Migration Hate Speech Detection” (Rajiakodi et al., 
2024) was conducted as part of LT-EDI@EACL 2024 with the dataset created. The 
main objective of the task is to create an automatic classification system that can 
precisely detect the occurrence of hate speech related to caste/migration in textual 
content. This shared task is conducted via the Codalab competition.29 A total of 51 
teams participated, out of which 15 teams submitted their entries. The participants 
were provided with training, development, and test datasets. As far as we know, this 
is the first collaborative effort focused on identifying hate speech related to caste and 
29  https://​codal​ab.​lisn.​upsac​lay.​fr/​compe​titio​ns/​16089.

--- Page 25 ---

3075
Detecting caste and migration hate speech in low‑resource…
migration in social media comments. The annotation has been categorized into two 
groups: Hate speech on caste/migration or Not-Hate speech on caste/migration.
7.2  Participants methodology and results
The methodologies used by the participants are described below, and the rank list is 
shown in the Table 6.
•	 BITS_GraphAI: This team employed two pre-trained transformers, namely 
TamilSBERT-STS and Indic-SBERT, as described in the works of Deode et al. 
(2023) and Mirashi et al. (2023) respectively. They then fine-tuned these trans-
formers using the provided data, utilizing triplet and cosine similarity loss func-
tions, respectively. Triplet loss involves using triples in the format of (anchor, 
positive, negative), where the anchor and positive sentences belong to the same 
class, while the negatives are taken from other classes. Triplet loss enhances the 
model’s ability to distinguish subtle correlations. In order to improve the clas-
sification process, they employed the TextGCN architecture (Yao et al., 2019) by 
utilizing the fine-tuned sBERT embeddings as feature input and the text graph 
as an adjacency matrix. All three models exhibited strong performance, with 
sBERT-enhanced TextGCN graph-based learning demonstrating slightly supe-
rior outcomes. The team attained a ranking of 4, accompanied by a macro F1 
score of 0.77.
•	 SSN-Nova (Reddy et al., 2024): This team explores various boosting techniques, 
including Adaboost and XGBoost (Demir & Sahin, 2023). They also conduct a 
comparative analysis using a voting classifier that combines multiple traditional 
models. This approach thoroughly investigates ensemble methods, utilizing the 
advantages of both boosting algorithms and conventional models to improve the 
system’s predictive performance. They achieved a macro F1 score of 0.59, secur-
ing the 12th rank in the process.
•	 Kubapok (Pokrywka & Jassem, 2024): The team adopted a systematic approach, 
relying exclusively on the data provided by the organizers. Their methodology 
focused on using a variety of models, including ‘l3cube/pune-kannada’ (Deode 
et  al., 2023; Mirashi et  al., 2023), ‘microsoft-mdeberta-v3’ (He et  al., 2021) 
(used twice), and ‘XLM-RoBERTa’. These models were trained using standard 
Hugging Face scripts for text classification, incorporating adjustments like a 
warm-up ratio of 0.1 and running for 30 epochs. Importantly, they combined the 
training and development data, creating new random splits for each model. The 
optimal epoch checkpoint was selected based on the development F1 score. A 
critical part of their strategy was averaging the probabilities generated by all four 
models and applying a threshold of 0.5 for class selection. This approach led the 
team to achieve rank 2 with a macro F1 score of 0.81.
•	 KEC_AI_DSNLP (Shanmugavadivel et al., 2024): This team developed machine 
learning models including K-Nearest Neighbors, Decision Trees, and Naive 
Bayes to classify hate speech text. Their approach yielded a macro F1 score of 
0.65, securing them the 9th rank.

--- Page 26 ---

3076
	
B. R. Chakravarthi et al.
Table 6   Participants rank list of the shared task based on average macro F1 Score
Participant’s team names
Macro F1
Rank
Transformers_run3 (Singhal & Bedi, 2024)
0.82
1
kubapok_run1 (Pokrywka & Jassem, 2024)
0.81
2
CUET_NLP_Manning_run3 (Alam et al., 2024)
0.80
3
BITS_Graph4NLP_run1
0.77
4
Algorithmalliance_run1 (Sangeetham et al., 2024)
0.76
5
lidoma_run2 (Tash et al., 2024)
0.76
6
CUET_NLP_GoodFellows_run2
0.75
7
quartet_run1 (Shaun et al., 2024)
0.73
8
KEC_AI_DSNLP_run2 (Shanmugavadivel et al., 2024)
0.65
9
selam_run1
0.62
10
byteSizedllm_run1
0.61
11
SSN-nova_run3 (Reddy et al., 2024)
0.59
12
WordWizards_tamil_run1
0.54
13
KEC_DL_KSK_run2
0.49
14
Habesha_run1
0.38
15
Fig. 11   Displayed the five misclassified comments analyzed in the error analysis section, showing the 
original and predicted labels

--- Page 27 ---

3077
Detecting caste and migration hate speech in low‑resource…
•	 CUET_NLP_GoodFellows: This team utilized two BERT models, specifically 
mBERT and XLM-R, both of which were fine-tuned for their task. In addition to 
these, they also employed a fine-tuned random classifier.
•	 selam: This team employed a Support Vector Machine (SVM) approach within 
the realm of Natural Language Processing (NLP). The primary goal was to 
develop a robust text classification system capable of predicting whether a given 
text contains caste/migration hate speech and scored macro F1 of 0.62 and 
secured rank 10.
•	 KEC_DL_KSK: This team utilized sampling techniques such as SMOTE and 
Random Oversampling to balance the datasets. They implemented machine 
learning algorithms, including Random Forest, Support Vector Machine, Naive 
Bayes, Logistic Regression, and Decision Tree. Additionally, they employed 
word embedding methods such as TF-IDF, Word2Vec, Doc2Vec, and FastText. 
Their approach resulted in a macro F1 score of 0.49.
•	 bytesizedllm: This team utilized embeddings derived from a subset of AI4B-
harat’s data, consisting of 100,000 randomly selected lines. These embeddings 
were generated using their custom-built subword tokenizers for Telugu (7.6 MB) 
and Tamil (1.3 MB). They employed a Bidirectional Long Short-Term Memory 
(BiLSTM) classifier for classification tasks. The model was trained on labeled 
datasets and achieved a macro F1 score of 0.61.
•	 Word Wizards: This team utilized LaBSE (Pei et al., 2022), a pre-trained lan-
guage representation model designed for multilingual text understanding. LaBSE 
employs a Siamese encoder architecture, which generates high-quality sentence 
embeddings by encoding text into fixed-size vector representations. After obtain-
ing these embeddings, a K-Nearest Neighbors (KNN) model was implemented, 
likely for tasks such as similarity searches or classification based on the encoded 
representations. KNN, a simple yet effective algorithm, is widely used for clas-
sification and regression, especially in high-dimensional spaces. This combina-
tion of LaBSE embeddings and KNN likely facilitated tasks involving semantic 
similarity, clustering, or text classification. The team secured 13th place with a 
macro F1 score of 0.54.
•	 Lidoma Tash et al. (2024): This team utilized both deep learning and machine 
learning models, including Convolutional Neural Networks (CNN) and Support 
Vector Machines (SVM), to classify hate speech related to caste and migration in 
the Tamil language. Their approach achieved a macro F1 score of 0.76, securing 
them the 6th rank in the competition.
•	 Transformers Singhal and Bedi (2024): This team employed an ensemble model 
consisting of XLM-RoBERTa, a multilingual BERT-based model, and the 
MuRIL cased model (Subramanian et  al., 2022). These models achieved the 
highest accuracy compared to all other tested models. The ensemble approach 
further enhanced overall accuracy by leveraging the strengths of both models. 
Notably, all models were trained on raw text without preprocessing, as data 
cleaning negatively impacted their performance.
•	 CUET_NLP_Manning (Alam et  al., 2024): This team implemented six machine 
learning models (Logistic Regression, Support Vector Machine, Stochastic Gradi-
ent Descent, XGBoost, Ensemble, and Random Forest), three deep learning mod-

--- Page 28 ---

3078
	
B. R. Chakravarthi et al.
els (BiLSTM, Attention, and BiLSTM-CNN), and three transformer-based models 
(M-BERT, XLM-R, and Tamil-BERT) using TF-IDF and FastText embeddings. 
Among these, the transformer-based models demonstrated the best performance, 
achieving the highest evaluation scores. The team secured 3rd place with a macro 
F1 score of 0.80.
•	 Habesha: This team developed a model based on BERT transformers for generating 
embeddings. Additionally, they incorporated Long Short-Term Memory (LSTM) 
deep learning techniques to enhance classification tasks. This hybrid architecture 
effectively utilizes transformer-based embeddings for rich text representation while 
leveraging LSTM’s sequential learning capabilities for improved classification. 
Their approach resulted in a macro F1 score of 0.38.
•	 ALGORITHM ALLIANCE (Sangeetham et  al., 2024): This team implemented 
various supervised machine learning algorithms, including Logistic Regression, 
(SVM), Multi-Layer Perceptron (MLP), Random Forest Classifier (RFC), Decision 
Tree, and K-Nearest Neighbors (KNN) for classification tasks. Among these mod-
els, SVM achieved the highest performance with a macro F1 score of 0.76, securing 
the 5th rank in the competition.
•	 Quartet (Shaun et al., 2024): This team employed machine learning models, includ-
ing Logistic Regression, SVM, Random Forest Classifier, Decision Tree Classifier, 
and Naive Bayes, for classification tasks. They used TF-IDF for feature representa-
tion. Among these models, SVM demonstrated the best performance, achieving a 
macro F1 score of 0.73 and securing the 8th rank in the competition.
8  Conclusion
In this study, we addressed the significant challenge of detecting caste and migration-
related hate speech in Tamil language by developing a specialized dataset and leverag-
ing advanced multilingual models. Our experiments revealed that the choice of model 
and fine-tuning strategies greatly influence performance, with tamil-sentence-bert-nli 
achieving the highest baseline score of 0.69. We further enhanced model performance 
by experimenting with various loss functions and adapter techniques. Notably, Bloom-
560 m combined with the KL loss function reached an impressive macro-F1 score of 
0.73, highlighting the importance of loss function selection in capturing nuanced hate 
speech patterns. These findings underscore the potential of leveraging state-of-the-
art NLP techniques and thoughtful experimental design to tackle hate speech in low-
resource languages, paving the way for more effective and culturally aware automated 
moderation systems. Future work will focus on refining these models and exploring 
additional methods to further enhance detection accuracy and robustness.
9  Ethical considerations
In conducting our study, which involves analyzing YouTube comments, we have 
prioritized ethical considerations throughout the data collection process. We took 
significant measures to safeguard the privacy of commentators, ensuring that their 

--- Page 29 ---

3079
Detecting caste and migration hate speech in low‑resource…
identities were protected and that the comments were used responsibly and in a 
manner that would not cause harm. Moreover, we strictly limited the distribution of 
data to academic and non-commercial research purposes only, thereby adhering to 
ethical standards that prioritize privacy and prevent misuse.
By conducting our research ethically and responsibly, we aimed to minimize 
potential harm, uphold privacy protections, and contribute meaningfully to our field 
of study. These efforts underscore our commitment to conducting research that is 
both rigorous and respectful of ethical principles. In conducting this study, which 
involves the utilization of YouTube comments, we have taken into account many 
ethical implications while collecting the YouTube comments we made sure that the 
privacy of commentators was well protected and that the comments were not used 
in a way that could have caused any harm. In addition, we ensured that data distri-
bution is prohibited for anything but academic and non-commercial research uses. 
Thus we have done our research ethically and responsibly to reduce harm, protect 
privacy, and make meaningful contributions to the field of study.
Acknowledgements  This work was conducted with the financial support of the Science Foundation Ire-
land (SFI) under Grant Number SFI/12/RC/2289_P2 (Insight_2) supported in part by a research grant 
from Science Foundation Ireland Centre for Research Training in Artificial Intelligence under Grant No. 
18/CRT/6223.
Author Contributions  Bharathi Raja Chakravarthi - Conceptualization, Investigation, Writing (Original 
Draft Preparation), Writing (review & Editing), Resources, Supervision; Saranya Rajiakodi - Investiga-
tion, Writing (Original Draft Preparation), Writing (Review & Editing), Resources, Supervision; Rahul 
Ponnusamy - Formal Analysis, Investigation, Methodology, Project Administration, Software, Validation, 
Writing (Original Draft Preparation), Writing (Review & Editing); Bhuvaneswari Sivagnanam - Writ-
ing (Original Draft Preparation), Visualization; Sara Yogesh Thakare - Software, Visualization, Writing 
(Original Draft Preparation); Sathiyaraj Thangasamy - Data Curation, Investigation, Writing (Review & 
Editing).
Funding  Open Access funding provided by the IReL Consortium.
Data availability  Data is provided in shared task https://​codal​ab.​lisn.​upsac​lay.​fr/​compe​titio​ns/​16089.
Declarations 
Conflict of interest  The authors declare no conflict of interest.
Open Access  This article is licensed under a Creative Commons Attribution 4.0 International License, 
which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long 
as you give appropriate credit to the original author(s) and the source, provide a link to the Creative 
Commons licence, and indicate if changes were made. The images or other third party material in this 
article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line 
to the material. If material is not included in the article’s Creative Commons licence and your intended 
use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permis-
sion directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/
licenses/by/4.0/.

--- Page 30 ---

3080
	
B. R. Chakravarthi et al.
References
Abubakar, I., Gram, L., Lasoye, S., Achiume, E. T., Becares, L., Bola, G. K., Dhairyawan, R., Lasco, G., 
McKee, M., Paradies, Y., Sabharwal, N. S., Selvarajah, S., Shannon, G., & Devakumar, D. (2022). 
Confronting the consequences of racism, xenophobia, and discrimination on health and health-care 
systems. The Lancet, 400(10368), 2137–2146. https://​doi.​org/​10.​1016/​S0140-​6736(22)​01989-4
Aghajanyan, A., Gupta, S. & Zettlemoyer, L. (2021). Intrinsic dimensionality explains the effectiveness 
of language model fine-tuning. In C. Zong, F. Xia, W. Li, & R. Navigli (Eds.), Proceedings of the 
59th Annual Meeting of the Association for computational Linguistics and the 11th International 
Joint Conference on Natural Language Processing (Volume 1: Long Papers) (pp. 7319–7328) 
Online, August. Association for Computational Linguistics. https://​doi.​org/​10.​18653/​v1/​2021.​acl-​
long.​568. https://​aclan​tholo​gy.​org/​2021.​acl-​long.​568/.
Alam, M. d., Ali Taher, H. M., Hossain, J., Ahsan, S. & Hoque, M. M. (2024). CUET_NLP_Manning@
LT-EDI 2024: Transformer-based approach on caste and migration hate speech detection. In B. Raja 
Chakravarthi, B. Bharathi, P. Buitelaar, T. Durairaj, G. Kovács, & M. García Cumbreras (Eds.), 
Proceedings of the Fourth Workshop on Language Technology for Equality, Diversity, Inclusion (pp. 
238–243), St. Julian’s, Malta, March. Association for Computational Linguistics. https://​aclan​tholo​
gy.​org/​2024.​ltedi-1.​30.
Alam, M. d. A., Taher, H. M. A., Hossain, J., Ahsan, S. & Hoque, M. M. (2024). CUET_NLP_Man-
ning@LT-EDI 2024: Transformer-based Approach on Caste and Migration Hate Speech Detection. 
In Proceedings of the Fourth Workshop on Language Technology for Equality, Diversity and Inclu-
sion, Malta, March . European Chapter of the Association for Computational Linguistics.
Arce-García, S., Said-Hung, E., & Montero-Díaz, J. (2024). Unmasking coordinated hate: Analysing hate 
speech on Spanish digital news media. New Media & Society Article. https://​doi.​org/​10.​1177/​14614​
44824​12597​15
Banaji, V., & Bhat, R. (2022). Social media and hate. Taylor & Francis.
Basile, V., Bosco, C., Fersini, E., Nozza, D., Patti, V., Rangel Pardo, F. M., Rosso, P. & Sanguinetti, M. 
(2019). SemEval-2019 task 5: Multilingual detection of hate speech against immigrants and women 
in Twitter. In J. May, E. Shutova, A. Herbelot, X. Zhu, M. Apidianaki, & S. M. Mohammad (Eds.), 
Proceedings of the 13th International Workshop on Semantic Evaluation (pp. 54–63), Minneapolis, 
Minnesota, USA, June. Association for Computational Linguistics. https://​doi.​org/​10.​18653/​v1/​S19-​
2007. https://​aclan​tholo​gy.​org/​S19-​2007.
Bender, E. M., Gebru, T., McMillan-Major, A. & Shmitchell, S. (2021). On the dangers of stochastic 
parrots: Can language models be too big? In Proceedings of the 2021 ACM conference on fairness, 
accountability, and transparency (pp. 610–623).
Binny, M. (2022). Tracing the contours of hate speech in India in the pandemic year: The curious case of 
online hate speech against Muslims and during the pandemic. Contemporary Voice of Dalit. https://​
doi.​org/​10.​1177/​24553​28X22​10943​64
Bosco, C., Dell’Orletta, F., Poletto, F., Sanguinetti, M., Tesconi, M. et al. (2018). Overview of the evalita 
2018 hate speech detection task. In Ceur workshop proceedings (vol. 2263, pp. 1–9). CEUR.
Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Neelakantan, A., Shyam, P., 
Sastry, G., Askell, A., Agarwal, S., Herbert-Voss, A., Krueger, G., Henighan, T., Child, R., Ramesh, 
A., Ziegler, D. M., Wu, J., Winter, C., Hesse, C., Chen, M., Sigler, E., Litwin, M., Gray, S., Chess, 
B., Clark, J., Berner, C., McCandlish, S., Radford, A., Sutskever, I. & Amodei, D. (2020). Language 
models are few-shot learners. In Proceedings of the 34th International Conference on Neural Infor-
mation Processing Systems, NIPS ’20, Red Hook, NY, USA. Curran Associates Inc.
Chakravarthi, B. R., Chinnappa, D., Priyadharshini, R., Madasamy, A. K., Sivanesan, S., Nava-
neethakrishnan, S. C., Thavareesan, S., Vadivel, D., Ponnusamy, R. & Kumaresan, P. K. (2021). 
Developing successful shared tasks on offensive language identification for Dravidian languages. 
arXiv:​2111.​03375.
Chakravarthi, B. R., Kumaresan, P., Priyadharshini, R., Buitelaar, P., Hegde, A., Shashirekha, H., Rajia-
kodi, S., García, M., Jiménez-Zafra, S. M., García-Díaz, J., Valencia-García, R., Ponnusamy, K., 
Shetty, P. & García-Baena, D. (2024). Overview of third shared task on homophobia and transpho-
bia detection in social media comments. In B. Raja Chakravarthi, B. Bharathi, P. Buitelaar, T. Durai-
raj, G. Kovács, & M. Á. G. Cumbreras (Eds.), Proceedings of the Fourth Workshop on Language 
Technology for Equality, Diversity, Inclusion (pp. 124–132), St. Julian’s, Malta, March. Association 
for Computational Linguistics. https://​aclan​tholo​gy.​org/​2024.​ltedi-1.​11.

--- Page 31 ---

3081
Detecting caste and migration hate speech in low‑resource…
Chakravarthi, B. R., Mariappan, A. K., McCrae, J. P., Premjith, B., Soman, K. P. & Mandl, T. (2020). 
Overview of the track on hasoc-offensive language identification-dravidiancodemix. In FIRE (Work-
ing notes) (pp. 112–120).
Chakravarthi, B. R., Priyadharshini, R., Jose, N., Kumar M, A., Mandl, T., Kumaresan, P. K., Ponnusamy, 
R., R L, H., McCrae, J. P. & Sherly, E. (2021). Findings of the shared task on offensive language 
identification in Tamil, Malayalam, and Kannada. In B. Raja Chakravarthi, R. Priyadharshini, M. 
Anand Kumar, P. Krishnamurthy, & E. Sherly (Eds.), Proceedings of the First Workshop on Speech 
and Language Technologies for Dravidian Languages (pp. 133–145), Kyiv, April. Association for 
Computational Linguistics. https://​aclan​tholo​gy.​org/​2021.​dravi​dianl​angte​ch-1.​17.
Chakravarthi, B. R., Jagadeeshan, M. B., Palanikumar, V., & Priyadharshini, R. (2023). Offensive lan-
guage identification in Dravidian languages using MPNET and CNN. International Journal of 
Information Management Data Insights, 3(1), Article 100151.
Chakravarthi, B. R., Priyadharshini, R., Banerjee, S., Jagadeeshan, M. B., Kumaresan, P. K., Ponnusamy, 
R., Benhur, S., & McCrae, J. P. (2023). Detecting abusive comments at a fine-grained level in a 
low-resource language. Natural Language Processing Journal, 3, Article 100006. https://​doi.​org/​10.​
1016/j.​nlp.​2023.​100006
Chhaya, Bhargav, Kumaresan, P. K., Ponnusamy, R. & Chakravarthi, B. R. (2024). Sampar: A Marathi 
hate speech dataset for homophobia, transphobia. In B. Raja Chakravarthi, B. Bharathi, M. Ángel 
García  Cumbreras, S.  María Jiménez  Zafra, M. Subramanian, K. Shanmugavadivel, & P. Nakov 
(Eds.), Speech and Language Technologies for Low-Resource Languages (pp. 34–51). Springer.
Conneau, A., Khandelwal, K., Goyal, N., Chaudhary, V., Wenzek, G., Guzmán, F., Grave, E., Ott, M., 
Zettlemoyer, L. & Stoyanov, V. (2020) Unsupervised cross-lingual representation learning at scale. 
In D. Jurafsky, J. Chai, N. Schluter, & J. Tetreault (Eds.), Proceedings of the 58th Annual Meeting 
of the Association for Computational Linguistics (pp. 8440–8451), July. Association for Compu-
tational Linguistics. https://​doi.​org/​10.​18653/​v1/​2020.​acl-​main.​747. https://​aclan​tholo​gy.​org/​2020.​
acl-​main.​747.
Cuzzocrea, A., Akter, M. S., Shahriar, H., & García Bringas, P. (2025). Cyberbullying detection, preven-
tion, and analysis on social media via trustable LSTM-autoencoder networks over synthetic data: 
The TLA-net approach. Future Internet, 17(2), 84. https://​doi.​org/​10.​3390/​fi170​20084
Davidson, T., Warmsley, D., Macy, M., & Weber, I. (2017). Automated hate speech detection and the 
problem of offensive language. Proceedings of the International AAAI Conference on Web and 
Social Media (vol. 11(1), pp. 512–515). https://​doi.​org/​10.​1609/​icwsm.​v11i1.​14955https://​ojs.​aaai.​
org/​index.​php/​ICWSM/​artic​le/​view/​14955.
Demir, S., & Sahin, E. K. (2023). An investigation of feature selection methods for soil liquefaction pre-
diction based on tree-based ensemble algorithms using adaboost, gradient boosting, and xgboost. 
Neural Computing and Applications, 35(4), 3173–3190.
Deode, S., Gadre, J., Kajale, A., Joshi, A. & Joshi, R. (2023). L3Cube-IndicSBERT: A simple approach 
for learning cross-lingual sentence representations using multilingual BERT. In C.-R. Huang, Y. 
Harada, J.-B. Kim, S. Chen, Y.-Y. Hsu, E. Chersoni, A. Pranav, W. Huiheng Zeng, B. Peng, Y. Li, & 
J. Li (eds.), Proceedings of the 37th Pacific Asia Conference on Language, Information and Com-
putation (pp. 154–163), Hong Kong, China, December. Association for Computational Linguistics. 
https://​aclan​tholo​gy.​org/​2023.​paclic-​1.​16/.
Devlin, J., Chang, M., Lee, K. & Toutanova, K. (2019). BERT: Pre-training of deep bidirectional trans-
formers for language understanding. In J. Burstein, C. Doran, & T.Solorio (eds), Proceedings of the 
2019 Conference of the North American Chapter of the Association for Computational Linguistics: 
Human Language Technologies, Volume 1 (Long and Short Papers) (pp. 4171–4186), Minneapolis, 
Minnesota, June. Association for Computational Linguistics. https://​doi.​org/​10.​18653/​v1/​N19-​1423. 
https://​aclan​tholo​gy.​org/​N19-​1423/.
Fortuna, P., & Nunes, S. (2018). A survey on automatic detection of hate speech in text. ACM Computing 
Surveys, 51(4), 85. https://​doi.​org/​10.​1145/​32326​76
Fouskas, Th., Koulierakis, G., Mine, F., Theofilopoulos, A., Konstantopoulou, S., Ortega-de Mora, F., 
Georgiadis, D., & Pantazi, G. (2022). Racial and ethnic inequalities, health disparities and racism in 
times of covid-19 pandemic populism in the eu: Unveiling anti-migrant attitudes, precarious living 
conditions and barriers to integration in Greece. Societies, 12(6), 189. https://​doi.​org/​10.​3390/​soc12​
060189
He, Pengcheng, Liu, Xiaodong, Gao, Jianfeng, & Chen, Wei. (2021). Deberta: Decoding-enhanced bert 
with disentangled attention. In 2021 International Conference on Learning Representations, May. 

--- Page 32 ---

3082
	
B. R. Chakravarthi et al.
https://​www.​micro​soft.​com/​en-​us/​resea​rch/​publi​cation/​deber​ta-​decod​ing-​enhan​ced-​bert-​with-​disen​
tangl​ed-​atten​tion-2/.
Hedderich, Michael  A., Lange, L., Adel, H., Strötgen, J. & Klakow, D. (2021). A survey on recent 
approaches for natural language processing in low-resource scenarios. In K. Toutanova, A. Rum-
shisky, L. Zettlemoyer, D. Hakkani-Tur, I.  Beltagy, S. Bethard, R. Cotterell, T. Chakraborty, & 
Y. Zhou (eds.), Proceedings of the 2021 Conference of the North American Chapter of the Asso-
ciation for Computational Linguistics: Human Language Technologies (pp. 2545–2568), Online, 
June. Association for Computational Linguistics. https://​doi.​org/​10.​18653/​v1/​2021.​naacl-​main.​201. 
https://​aclan​tholo​gy.​org/​2021.​naacl-​main.​201.
Houlsby, N., Giurgiu, A., Jastrzebski, S., Morrone, B., De Laroussilhe, Q., Gesmundo, A., Attariyan, M. 
& Gelly, S. (2019). Parameter-efficient transfer learning for NLP. In Proceedings of the 36th Inter-
national Conference on Machine Learning.
Hu, Edward J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Wang, L. & Chen, W. (2022). LoRA: 
Low-rank adaptation of large language models. In International Conference on Learning Represen-
tations. https://​openr​eview.​net/​forum?​id=​nZeVK​eeFYf9.
Hu, Z., Wang, L., Lan, Y., Xu, W., Lim, E., Bing, L., Xu, X., Poria, S. & Lee, R. (2023). LLM-adapters: 
An adapter family for parameter-efficient fine-tuning of large language models. In H. Bouamor, J. 
Pino, & K. Bali (Eds.), Proceedings of the 2023 Conference on Empirical Methods in Natural Lan-
guage Processing (pp. 5254–5276), Singapore, December. Association for Computational Linguis-
tics. https://​doi.​org/​10.​18653/​v1/​2023.​emnlp-​main.​319. https://​aclan​tholo​gy.​org/​2023.​emnlp-​main.​
319.
Jeong, Y., Oh, J., Lee, J., Ahn, J., Moon, J., Park, S. & Oh, A. (2022). KOLD: Korean offensive language 
dataset. In Y. Goldberg, Z. Kozareva, & Y. Zhang (Eds.), Proceedings of the 2022 Conference on 
Empirical Methods in Natural Language Processing (pp. 10818–10833), Abu Dhabi, United Arab 
Emirates, December. Association for Computational Linguistics. https://​doi.​org/​10.​18653/​v1/​2022.​
emnlp-​main.​744. https://​aclan​tholo​gy.​org/​2022.​emnlp-​main.​744.
Joshi, R. (2022). L3cube-Hindbert and Devbert: Pre-trained bert transformer models for Dbased Hindi 
and Marathi languages. arXiv:​2211.​11418.
Joshi, P., Santy, S., Budhiraja, A., Bali, K. & Choudhury, M. (2002). The state and fate of linguistic 
diversity and inclusion in the NLP world. In D. Jurafsky, J. Chai, N. Schluter, & J. Tetreault (Eds.), 
Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (pp. 
6282–6293) Online, July. Association for Computational Linguistics. https://​doi.​org/​10.​18653/​v1/​
2020.​acl-​main.​560. https://​aclan​tholo​gy.​org/​2020.​acl-​main.​560.
Kakwani, D., Kunchukuttan, A., Golla, S., Gokul N. C., Bhattacharyya, A., Khapra, Mitesh M. & Kumar, 
P. (2020). IndicNLPSuite: Monolingual corpora, evaluation benchmarks and pre-trained multilin-
gual language models for Indian languages. In T. Cohn, Y. He, & Y. Liu (Eds.), Findings of the 
Association for Computational Linguistics: EMNLP 2020 (pp. 4948–4961), Online, November. 
Association for Computational Linguistics. https://​doi.​org/​10.​18653/​v1/​2020.​findi​ngs-​emnlp.​445. 
https://​aclan​tholo​gy.​org/​2020.​findi​ngs-​emnlp.​445.
Kakwani, D., Kunchukuttan, A., Golla, S., Gokul, N. C., Bhattacharyya, A., Khapra, Mitesh M., & 
Kumar, P. (2020). Indicnlpsuite: Monolingual corpora, evaluation benchmarks and pre-trained mul-
tilingual language models for Indian languages. In Findings of the Association for Computational 
Linguistics: EMNLP, 2020 (pp. 4948–4961).
Kaplan, J., McCandlish, S., Henighan, T., Brown, Tom B., Chess, B., Child, R., Gray, S., Radford, A., 
Wu, J. & Amodei, D. (2020). Scaling laws for neural language models. ArXiv:​2001.​08361. https://​
api.​seman​ticsc​holar.​org/​Corpu​sID:​21086​1095.
Khanuja, S., Bansal, D., Mehtani, S., Khosla, S., Dey, A., Gopalan, B. Margam, D. K., Aggarwal, P., 
Nagipogu, R. T., Dave, S., Gupta, S., Gali, S. C. B., Subramanian, V., & Talukdar, B. (2021). Muril: 
Multilingual representations for Indian languages. arXiv:​2103.​10730
Kijima, Y. (2006). Caste and tribe inequality: evidence from India, 1983–1999. Economic Development 
and Cultural Change, 54(2), 369–404.
Kirasur, N. & Jhaver, S. (2024). Understanding the resilience of caste: A critical discourse analysis of 
community profiles on x. arXiv:​2407.​02810.
Kumaresan, P. K., Ponnusamy, R., Sharma, D., Buitelaar, P. & Chakravarthi, B. R. (2024). Dataset 
for identification of homophobia and transphobia for Telugu, Kannada, and Gujarati. In N. Cal-
zolari, M.-Y. Kan, V. Hoste, A. Lenci, S. Sakti, & N. Xue (Eds.), Proceedings of the 2024 Joint 
International Conference on Computational Linguistics, Language Resources and Evaluation 

--- Page 33 ---

3083
Detecting caste and migration hate speech in low‑resource…
(LREC-COLING 2024) (pp. 4404–4411), Torino, Italia, May. ELRA and ICCL. https://​aclan​tholo​
gy.​org/​2024.​lrec-​main.​393.
Kumaresan, P. K., Ponnusamy, R., Priyadharshini, R., Buitelaar, P., & Chakravarthi, B. R. (2023). Homo-
phobia and transphobia detection for low-resourced languages in social media comments. Natural 
Language Processing Journal, 5, Article 100041. https://​doi.​org/​10.​1016/j.​nlp.​2023.​100041
Laurençon, H., Saulnier, L., Wang, T., Akiki, C., Moral, Albert Villanova, del, Le Scao, T., Von Werra, 
L., Mou, C., González Ponferrada, E., Nguyen, H., Frohberg, J., Šaško, M., Lhoest, Q., McMillan-
Major, A., Dupont, G., Biderman, S., Rogers, A., Allal, L. B., ... Jernite, Y. (2022). The bigscience 
roots corpus: A 1.6 tb composite multilingual dataset. In Advances in Neural Information Process-
ing Systems, 35 (pp. 31809–31826).
Lester, B., Al-Rfou, R. & Constant, N. (2021). The power of scale for parameter-efficient prompt tuning. 
In M.-F. Moens, X. Huang, L. Specia, & S. Wen-tau Yih (Eds.), Proceedings of the 2021 Confer-
ence on Empirical Methods in Natural Language Processing, (pp. 3045–3059), Online and Punta 
Cana, Dominican Republic, November. Association for Computational Linguistics. https://​doi.​org/​
10.​18653/​v1/​2021.​emnlp-​main.​243. https://​aclan​tholo​gy.​org/​2021.​emnlp-​main.​243.
Liu, X., Ji, K., Fu, Y., Tam, W., Du, Z., Yang, Z. & Tang, J. (2022). P-tuning: Prompt tuning can be com-
parable to fine-tuning across scales and tasks. In S. Muresan, P. Nakov, & A. Villavicencio (Eds.), 
Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 
2: Short Papers) (pp. 61–68), Dublin, Ireland, May. Association for Computational Linguistics. 
https://​doi.​org/​10.​18653/​v1/​2022.​acl-​short.8. https://​aclan​tholo​gy.​org/​2022.​acl-​short.8.
Liu, Y., Ott, M., Goyal, N., Du, J., Joshi, M., Chen, D., Levy, O., Lewis, M., Zettlemoyer, L. & Stoy-
anov, V. (2019). Roberta: A robustly optimized BERT pretraining approach. CoRR, abs/1907.11692. 
http://​arxiv.​org/​abs/​1907.​11692.
Lombard, M., Snyder-Duch, J. & Bracken, C. C. (2010). Intercoder reliability.
Mal, P., & Saikia, N. (2024). Disparity by caste and tribe: Understanding women’s empowerment and 
health outcomes in India. Social Science & Medicine. https://​doi.​org/​10.​1016/j.​socsc​imed.​2024.​
117074
Marcos, Z., Shervin, M., Nakov, P., Rosenthal, S., Farra, N. & Kumar, R. (2019). Predicting the type and 
target of offensive posts in social media. In J. Burstein, C. Doran, & T. Solorio (Eds.), Proceed-
ings of the 2019 Conference of the North American Chapter of the Association for Computational 
Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers) (pp. 1415–1420), 
Minneapolis, Minnesota, June. Association for Computational Linguistics. https://​doi.​org/​10.​18653/​
v1/​N19-​1144. https://​aclan​tholo​gy.​org/​N19-​1144.
Mirashi, A., Sonavane, S., Lingayat, P., Padhiyar, T. & Joshi, R. (2023). L3Cube-IndicNews: News-based 
short text and long document classification datasets in Indic languages. In J. D. Pawar, & S. L. Devi 
(Eds.), Proceedings of the 20th International Conference on Natural Language Processing (ICON) 
(pp. 442–449), Goa University, Goa, India, December. NLP Association of India (NLPAI). https://​
aclan​tholo​gy.​org/​2023.​icon-1.​37/.
Mosse, D. (2018). Caste and development: Contemporary perspectives on a structure of discrimination 
and advantage. World Development, 110, 422–436.
Nekoto, W., Marivate, V., Matsila, T., Fasubaa, T., Fagbohungbe, T., Akinola, S. O., Muhammad, S., 
Kabongo Kabenamualu, S., Osei, S., Sackey, F., Niyongabo, R. A., Macharm, R., Ogayo, P., Ahia, 
O., Berhe, M. M., Adeyemi, M., Mokgesi-Selinga, M., Okegbemi, L., Martinus, L., ... & Bashir, A. 
(2020). Participatory research for low-resourced machine translation: A case study in African lan-
guages. In T. Cohn, Y. He, & Y. Liu (Eds.), Findings of the Association for Computational Linguis-
tics: EMNLP 2020 (pp. 2144–2160), Online, November. Association for Computational Linguistics. 
https://​doi.​org/​10.​18653/​v1/​2020.​findi​ngs-​emnlp.​195. https://​aclan​tholo​gy.​org/​2020.​findi​ngs-​emnlp.​
195.
Pei, Y., Chen, S., Ke, Z., Silamu, W., & Guo, Q. (2022). AB-LABSE: Uyghur sentiment analysis via the 
pre-training model with BILSTM. Applied Sciences, 12(3), 1182.
Pfeiffer, J., Goyal, N., Lin, X., Li, X., Cross, J., Riedel, S. & Artetxe, M. (2022). Lifting the curse of 
multilinguality by pre-training modular transformers. In Proceedings of the 2022 Conference of the 
North American Chapter of the Association for Computational Linguistics: Human Language Tech-
nologies (pp. 3479–3495), Seattle, United States, July. Association for Computational Linguistics. 
https://​doi.​org/​10.​18653/​v1/​2022.​naacl-​main.​255. https://​aclan​tholo​gy.​org/​2022.​naacl-​main.​255.
Pohjonen, M., & Udupa, S. (2017). Extreme speech online: An anthropological critique of hate speech 
debates. International Journal of Communication, 11, 19.

--- Page 34 ---

3084
	
B. R. Chakravarthi et al.
Pokrywka, J. & Jassem, K. (2024). kubapok@LT-EDI 2024: Evaluating transformer models for hate 
speech detection in Tamil. In B.  Raja Chakravarthi, B. Bharathi, P. Buitelaar, T. Durairaj, G. 
Kovács, & M. Ángel García Cumbreras (Eds.), Proceedings of the Fourth Workshop on Language 
Technology for Equality, Diversity, Inclusion (pp. 196–199), St. Julian’s, Malta, March. Association 
for Computational Linguistics. https://​aclan​tholo​gy.​org/​2024.​ltedi-1.​22.
Ponnusamy, R., Pannerselvam, K., R, Saranya, Kumaresan, P. K., Thavareesan, S., S, Bhuvaneswari, 
K.a, Anshid, Kumar, S. S., Buitelaar, P., & Chakravarthi, B. R. (2024). From laughter to inequality: 
Annotated dataset for misogyny detection in Tamil and Malayalam memes. In N. Calzolari, M.-Y. 
Kan, V. Hoste, A. Lenci, S. Sakti, & N. Xue (Eds), Proceedings of the 2024 Joint International 
Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 
2024) (pp. 7480–7488), Torino, Italia, May. ELRA and ICCL. https://​aclan​tholo​gy.​org/​2024.​lrec-​
main.​660.
Premjith, B., Chakravarthi, B. R., Kumaresan, P. K., Rajiakodi, S., Karnati, S., Mangamuru, S. & Jana-
kiram, C. (2024). Findings of the shared task on hate and offensive language detection in Telugu 
codemixed text (HOLD-Telugu)@DravidianLangTech 2024. In B.  Raja Chakravarthi, R. Priyad-
harshini, A. Kumar Madasamy, S. Thavareesan, E. Sherly, R. Nadarajan, & M. Ravikiran, (eds.), 
Proceedings of the Fourth Workshop on Speech, Vision, and Language Technologies for Dravid-
ian Languages (pp. 49–55), St. Julian’s, Malta, March. Association for Computational Linguistics. 
https://​aclan​tholo​gy.​org/​2024.​dravi​dianl​angte​ch-1.8.
Raffel, C., Shazeer, N., Roberts, A., Lee, K., Narang, S., Matena, M., Zhou, Y., Li, W., & Liu, P. J. 
(2020). Exploring the limits of transfer learning with a unified text-to-text transformer. Journal of 
Machine Learning Research, 21(140), 1–67.
Rajiakodi, S., Chakravarthi, B. R., Ponnusamy, R., Kumaresan, P., Thangasamy, S., Sivagnanam, B., & 
Rajkumar, C. (2024). Overview of shared task on caste and migration hate speech detection. In Pro-
ceedings of the Fourth Workshop on Language Technology for Equality, Diversity, Inclusion (pp. 
145–151).
Rajiakodi, S., Chakravarthi, B. R, Ponnusamy, R., Kumaresan, P., Thangasamy, S., Sivagnanam, B. & 
Rajkumar, C. (2024). Overview of shared task on caste and migration hate speech detection. In 
B. Raja Chakravarthi, B. Bharathi, P. Buitelaar, T. Durairaj, G.Kovács, & M. Ángel García Cum-
breras (Eds.), Proceedings of the Fourth Workshop on Language Technology for Equality, Diver-
sity, Inclusion (pp. 145–151), St. Julian’s, Malta, March. Association for Computational Linguistics. 
https://​aclan​tholo​gy.​org/​2024.​ltedi-1.​14.
Ravikiran, M., Rajalakshmi, R., Chakravarthi, B. R, Madasamy, A. K. & Thavareesan, S. (2024). Find-
ings of the first shared task on offensive span identification from code-mixed Kannada-English com-
ments. In B. R. Chakravarthi, R. Priyadharshini, A. Kumar Madasamy, S. Thavareesan, E. Sherly, 
R. Nadarajan, & M. Ravikiran (Eds.), Proceedings of the Fourth Workshop on Speech, Vision, and 
Language Technologies for Dravidian Languages (pp. 43–48), St. Julian’s, Malta, March. Associa-
tion for Computational Linguistics. https://​aclan​tholo​gy.​org/​2024.​dravi​dianl​angte​ch-1.7.
Rawal, V., & Swaminathan, M. (2011). Income inequality and caste in village India. Review of Agrarian 
Studies, 1(2), 1–27.
Rawat, A., Kumar, S., & Samant, S. S. (2024). Hate speech detection in social media: Techniques, recent 
trends, and future challenges. Wiley Interdisciplinary Reviews: Computational Statistics, 16(2), 
Article e1648.
Reddy, A., Thomas, A., Moorthi, P. & Bharathi, B. (2024). SSN-nova@LT-EDI 2024: POS tagging, 
boosting techniques and voting classifiers for caste and migration hate speech detection. In B. R. 
Chakravarthi, B. Bharathi, P. Buitelaar, T. Durairaj, G. Kovács, & M. A. García Cumbreras (Eds.), 
Proceedings of the Fourth Workshop on Language Technology for Equality, Diversity, Inclusion (pp. 
233–237), St. Julian’s, Malta, March. Association for Computational Linguistics. https://​aclan​tholo​
gy.​org/​2024.​ltedi-1.​29.
Rodríguez-Peral, E., Gómez Franco, T., & Rodríguez-Peral Bustos, D. (2025). Propagation of hate speech 
on social network x: Trends and approaches. Social Inclusion, 13, 9317. https://​doi.​org/​10.​17645/​si.​
9317
Ruder, S., Peters, M. E., Swayamdipta, S., & Wolf, T. (2019). Transfer learning in natural language pro-
cessing. In A. Sarkar & M. Strube (Eds.), Proceedings of the 2019 Conference of the North Ameri-
can Chapter of the Association for Computational Linguistics: Tutorials (pp. 15–18), Minneapolis, 
Minnesota, June. Association for Computational Linguistics. https://​doi.​org/​10.​18653/​v1/​N19-​5004. 
https://​aclan​tholo​gy.​org/​N19-​5004.

--- Page 35 ---

3085
Detecting caste and migration hate speech in low‑resource…
Sangeetham, S., Vinay, S., Rajan G, K., Abishna, A. & Bharathi, B. (2024). Algorithm alliance@LT-
EDI-2024: Caste and migration hate speech detection. In B. R. Chakravarthi, B. Bharathi, P. Buite-
laar, T. Durairaj, G. Kovács, & M. A. García Cumbreras (Eds.), Proceedings of the Fourth Work-
shop on Language Technology for Equality, Diversity, Inclusion (pp. 254–258), St. Julian’s, Malta, 
March. Association for Computational Linguistics. https://​aclan​tholo​gy.​org/​2024.​ltedi-1.​33.
Scao, T,, Fan, A., Akiki, C., Pavlick, E., Ili’c, S., Hesslow, D., Castagn’e, R., Luccioni, A., Yvon, F., 
Gallé, M., Tow, J., Rush, A., Biderman, S., Webson, A., Ammanamanchi, P., Wang, T., Sagot, B., 
Muennighoff, N., Moral, A., Ruwase, O., Bawden, R., Bekman, S., McMillan-Major, A., Beltagy, 
Iz., Nguyen, H., Saulnier, L., ... Wolf, T. (2022) Bloom: A 176b-parameter open-access multilingual 
language model. ArXiv:​2211.​05100. https://​api.​seman​ticsc​holar.​org/​Corpu​sID:​25342​0279.
Shanmugavadivel, K., Subramanian, M., Aiswarya, M., Aruna, T. & Jeevaananth, S. (2024). KEC 
AI DSNLP@LT-EDI-2024:caste and migration hate speech detection using machine learn-
ing techniques. In B. R. Chakravarthi, B. Bharathi, P. Buitelaar, T. Durairaj, G. Kovács, & M. A. 
García Cumbreras (Eds.), Proceedings of the Fourth Workshop on Language Technology for Equal-
ity, Diversity, Inclusion (pp. 206–210), St. Julian’s, Malta, March. Association for Computational 
Linguistics. https://​aclan​tholo​gy.​org/​2024.​ltedi-1.​24.
Shanmugavelan, M. (2022). Caste-hate speech and digital media politics. Journal of Digital Media & 
Policy, 13(1), 41–55.
Shaun, H., Sivakumar, S., R, Rohan, Jayaguptha, N. & Thenmozhi, D. (2024). Quartet@lt-edi 2024: A 
support vector machine approach for caste and migration hate speech detection. In Proceedings of 
the Fourth Workshop on Language Technology for Equality, Diversity, Inclusion (pp. 211–215). 
Association for Computational Linguistics. https://​aclan​tholo​gy.​org/​2024.​ltedi-1.​25.
Shukla, P. K., Bheemeshwar Reddy, A., & Kumar, D. (2024). Class in caste: Inequalities in human capital 
investments in children in India. International Journal of Educational Development, 106, Article 
103004. https://​doi.​org/​10.​1016/j.​ijedu​dev.​2024.​103004
Singhal, K. & Bedi, J. (2024). Transformers@LT-EDI-EACL2024: Caste and migration hate speech 
detection in Tamil using ensembling on transformers. In B. R. Chakravarthi, B. Bharathi, P. Buite-
laar, T. Durairaj, G. Kovács, & M. A. García Cumbreras (Eds.), Proceedings of the Fourth Work-
shop on Language Technology for Equality, Diversity, Inclusion (pp. 249–253), St. Julian’s, Malta, 
March 2024. Association for Computational Linguistics. https://​aclan​tholo​gy.​org/​2024.​ltedi-1.​32.
Sreelakshmi, K., Premjith, B., Chakravarthi, B. R., & Soman, K. P. (2024). Detection of hate speech 
and offensive language codemix text in Dravidian languages using cost-sensitive learning approach. 
IEEE Access, 12, 20064–20090. https://​doi.​org/​10.​1109/​ACCESS.​2024.​33588​11
Subramanian, M., Ponnusamy, R., Benhur, S., Shanmugavadivel, K., Ganesan, A., Ravi, D., Shanmu-
gasundaram, G. K., Priyadharshini, R., & Chakravarthi, B. R. (2022). Offensive language detection 
in Tamil Youtube comments by adapters and cross-domain knowledge transfer. Computer Speech & 
Language, 76, Article 101404. https://​doi.​org/​10.​1016/j.​csl.​2022.​101404
Tash, M., Ahani, Z., Zamir, M., Kolesnikova, O. & Sidorov, G. (2024). Lidoma@LT-EDI 2024: Tamil 
hate speech detection in migration discourse. In In B. R. Chakravarthi, B. Bharathi, P. Buitelaar, 
T. Durairaj, G. Kovács, & M. A. García Cumbreras (Eds.),Proceedings of the Fourth Workshop on 
Language Technology for Equality, Diversity, Inclusion (pp. 184–189), St. Julian’s, Malta, March. 
Association for Computational Linguistics. https://​aclan​tholo​gy.​org/​2024.​ltedi-1.​20.
Udupa, S. (2020). Digital technology and extreme speech: Approaches to counter online hate. Technical 
report, Centre for Media and Communication Research, University of Leeds. https://​sahan​audupa.​
net/​wp-​conte​nt/​uploa​ds/​2020/​09/​Digit​al_​techn​ology_​and_​extre​me_​speech_​Udupa.​pdf.
Vaghela, P., Mothilal, R. K., Romero, D., & Pal, J. (2022). Caste capital on twitter: A formal network 
analysis of caste relations among Indian politicians. Proceedings of the ACM on Human-Computer 
Interaction, 6(CSCW1), 1–29.
Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł. & Polosukhin, I. 
(2017). Attention is all you need. In Advances in neural information processing systems, 30.
Waseem, Z. & Hovy, D. (2016). Hateful symbols or hateful people? predictive features for hate speech 
detection on Twitter. In J. Andreas, E. Choi, & A. Lazaridou (Eds.), Proceedings of the NAACL Stu-
dent Research Workshop (pp. 88–93), San Diego, California, June. Association for Computational 
Linguistics. https://​doi.​org/​10.​18653/​v1/​N16-​2013. https://​aclan​tholo​gy.​org/​N16-​2013.
Waseem, Z., Davidson, T., Warmsley, D. & Weber, I. (2017). Understanding abuse: A typology of abu-
sive language detection subtasks. In Z. Waseem, W. H. K. Chung, D. Hovy, & J. Tetreault (Eds.), 
Proceedings of the First Workshop on Abusive Language Online (pp. 78–84), Vancouver, BC, 

--- Page 36 ---

3086
	
B. R. Chakravarthi et al.
Authors and Affiliations
Bharathi Raja Chakravarthi1,3 · Saranya Rajiakodi2 · Rahul Ponnusamy3 · 
Bhuvaneswari Sivagnanam2 · Sara Yogesh Thakare4 · Sathiyaraj Thangasamy5
 *	 Bharathi Raja Chakravarthi 
	
bharathi.raja@universityofgalway.ie
	
Saranya Rajiakodi 
	
saranya@cutn.ac.in
	
Rahul Ponnusamy 
	
r.ponnusamy1@universityofgalway.ie
	
Bhuvaneswari Sivagnanam 
	
bhuvisiva24@gmail.com
	
Sara Yogesh Thakare 
	
sara.thakare.22033@iitgoa.ac.in
	
Sathiyaraj Thangasamy 
	
sathiyarajkkt@gmail.com
1	
School of Computer Science, University of Galway, Galway, Ireland
2	
Department of Computer Science, Central University of Tamil Nadu, Thiruvarur, Tamil Nadu, 
India
3	
Data Science Institute, University of Galway, Galway, Ireland
4	
Indian Institute of Technology Goa, Bandiwada, India
5	
Department of Tamil, Sri Krishna Adithya College of Arts and Science, Kovaipudur, 
Tamil Nadu, India
Canada, August. Association for Computational Linguistics. https://​doi.​org/​10.​18653/​v1/​W17-​3012. 
https://​aclan​tholo​gy.​org/​W17-​3012.
Yao, L., Mao, C., & Luo, Y. (2019). Graph convolutional networks for text classification. In Proceedings 
of the AAAI conference on artificial intelligence, 33 (pp. 7370–7377).
Publisher’s Note  Springer Nature remains neutral with regard to jurisdictional claims in published maps 
and institutional affiliations.

```
