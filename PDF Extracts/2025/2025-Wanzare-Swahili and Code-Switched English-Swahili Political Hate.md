---
title: "2025-available-Swahili and Code-Switched English-Swahili Political Hate"
source_pdf: "[[Lit-WS-PDFs/2025/2025-Wanzare-Swahili and Code-Switched English-Swahili Political Hate.pdf]]"
extracted_date: "2026-02-14"
extraction_method: "PyMuPDF"
---

# PDF Extract: 2025-Wanzare-Swahili and Code-Switched English-Swahili Political Hate
```
## Page 1

Swahili and Code-Switched English-Swahili 
Political Hate Speech Detection 
Textual Dataset
Nelson Odhiambo Onyango†, Lilian Wanzare, James Obuhuma
School of Computing Informatics, Department of Computer Science, Maseno University, Maseno 40100, Kenya
Keywords:  High resourced; Offensive; Labels; Dataset size; Data preprocessing
Citation: Onyango N.O.,  Wanzare L.,  Obuhuma J.: Swahili and Code-Switched English-Swahili Political Hate Speech Detec­
tion Textual Dataset. Data Intelligence, Vol. 7, Art. No.: 2025d07, pp. 819–850, 2025. DOI: https://doi.org/10.3724/2096-7004.
di.2025.0053
Related data: Onyango N.O., Wanzare L., Obuhuma J.: UrduPSL-Kabaddi-Tweets. Data Intelligence, 2025. DOI: https://doi.
org/10.57760/sciencedb.27635
ABSTRACT
The growth of online platforms coupled with users’ ability to post and comment anonymously has 
resulted in an alarming spread of offensive and hateful content especially during election period. Efforts 
to monitor and detect hate speech, including computer based automated hate speech detection models 
remain unsatisfactory. This is primarily due to the fact that most annotated hate speech datasets focus 
on English, despite the growing use of low-resourced languages like Swahili and code-switched English-
Swahili on Kenyan social media platforms such as Twitter (now X). Currently, there is only one annotated 
publicly available hate speech dataset having Swahili and code-switched English-Swahili texts. However, 
the dataset lacks language annotation distinguishing Swahili from English-Swahili. This poses a challenge, 
as the dataset also contains pure English tweets, making it difficult for researchers who require tweets 
in a specific language. Moreover, the dataset lacks hate target annotations, such as politics, disability, 
religion, ethnicity, social-status, nationality, gender, and others. This is a challenge since hate target labels 
help in comprehensive analysis of the hate stereotypes. This study therefore fills this gap by curating 
Swahili and code-switched English-Swahili hate speech dataset and annotating with hate class, target 
and language. Data preparation involved combining the Politikweli, AfriSenti, and Hate_Speech_Kenya 
datasets, resulting in a collection of 101,014 tweets. Hate target labels include nationality, social status, 
politics, disability, ethnicity, gender, religion and other. Multilingual index of 0.72 was achieved for code 
†　Corresponding author: Nelson Odhiambo Onyango (E-mail: nodhianbo@gmail.com; ORCID: 0009-0004-2989-712X).
© 2025 Chinese Academy of Sciences. Published under a Creative Commons Attribution 4.0 International (CC BY 4.0) 
license.

## Page 2

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
820
switching. Randolph’s free marginal kappa score of 0.435 and 0.552 was achieved for the first and second 
pilot dataset respectively with a significant difference of 0.117. The overall inter annotator score using 
Randolph’s multirater kappa was 0.70 showing substantial agreement. As a result, this study provides hate 
speech textual dataset having a total of 19369 tweets labeled as hate, offensive and neither. To assess 
the dataset’s suitability, experiments were conducted using a non-linear SVM and a Bi-directional Long 
Short-Term Memory (Bi-LSTM) model. SwahBERT model, a variant of BERT pre-trained on Swahili texts 
was fine-tuned on the code-switched data and achieved an F1-score of 0.89. Bi-LSTM model with fastText 
embeddings achieved an f1-score, accuracy, recall and precision of 0.8 on the test set showing the ability 
of fastText embeddings in capturing the nuances in code-switched texts. The recall for the hate speech 
class improved from 0.57 to 0.76 when the Synthetic Minority Oversampling Technique (SMOTE) was 
applied, demonstrating the dataset’s practical applicability. Results for SVM trained on code-switched part 
of the dataset shows that traditional models performs better on a relatively smaller dataset. These results 
suggest that the dataset could be reused to develop machine learning models for moderation of bias and 
hate speech contents from social media especially in low-resource languages. This can help in promoting 
good mental health among social media users. The dataset can also serve as a benchmark for evaluating 
NLP techniques in low-resource settings.
1.  INTRODUCTION
Online platforms play a vital role, especially during elections, where millions of messages are posted 
daily [1]. However, the growth of these platforms has led to the spread of offensive, discriminatory 
and harmful content [2]. Users can anonymously post and comment, facilitating the spread of hate 
speech [3]. Negative impacts of hate speech include communal riots [4], violence and health issues for 
victims [1]. Efforts to regulate hate speech in Kenya include the National Cohesion and Integration Act of 
2008 [5] and hate speech detection models. Several studies have used datasets for hate speech detection, 
with some focusing on binary classification [1-2, 4, 6] and others on multi-class classification based 
on types like offensive or abusive language [3, 7]. However, most hate speech datasets focus on well-
resourced languages like English, and only a few address code-switched languages [4, 8-11].
Currently, there is only one annotated hate speech dataset having Swahili and code-switched English-
Swahili tweets publicly available. However, the dataset is not annotated with language labels as Swahili 
and English-Swahili. This is a challenge since the dataset also contains pure English tweets and hence 
difficult for the researchers who may require tweets in some specific language. In addition, hate tweets 
are not annotated with hate target labels, where target labels in this case are politics, disability, religion, 
ethnicity, nationality, social status, gender and others. This is a challenge since hate target labels help in 
comprehensive analysis and finding the stereotypes towards which hate speech is directed to [12]. There is 
therefore a need for a curated Swahili and code-switched English-Swahili hate speech textual dataset.
The main contribution of this paper is the curation of a high quality annotated dataset for political 
hate speech detection in Swahili and code-switched English-Swahili social media texts. This dataset fills 
a significant gap in low-resource language processing by incorporating linguistic and cultural nuances

## Page 3

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
821
specific to Swahili and code-switched tweets. It is manually annotated using clearly defined guidelines 
and validated through inter-annotator agreement and baseline models experiments. The rest of the paper is 
structured as follows – Section 2 reviews related work in hate speech detection, particularly in African and 
low-resource language settings. Section 3 describes the methodology of dataset curation, including data 
collection, preprocessing, annotation guidelines, and procedures. Section 4 presents the dataset analysis 
and findings, experimental validation of the dataset and comparison between the curated hate speech 
dataset and related existing datasets, section 5 outlines the limitation of the study, section 6 outlines 
recommendations for future work, section 7 outlines the significance of the study, section 8 outlines 
conclusions of the study and lastly, section 9 gives the data availability statement.
2.  RELATED WORKS
2.1  Existing Datasets Sizes, Labels and Language
Several datasets have been applied in the detection of hate speech based on previous studies. Some of 
them have presumed hate speech detection as a binary classification of hate and not hate [1-2, 4, 6, 13-15] 
while others have focused on multiclass classification of hate speech based on the stereotypes of hate 
speech and related terms such as offensive and abusive [3, 7] and the levels of hate speech. Commonly 
used datasets are [16] dataset and HEOT dataset which consist of English and Hindi code-switched 
tweets [8].
[13] applied binary classification on 4575 Hindi and English tweets with hate and not hate labels. The 
study focused on two tasks, sarcasm and hate speech detection. 88.254% were tweets with sarcasm and 
the rest without. For the second task, 86.437% of the tweets were labeled as hate and the rest not hate. 
The study came up with a code-switched dataset having Hindi and English texts. In addition, the study’s 
task of detecting sarcasm was a contribution since sarcasm has been one of the major challenges in hate 
speech classification when it comes to context.
[14] collected 8600 hate tweets and 9864 non-hate tweets from the 2016 Philippine electioneering 
period. The dataset focused on the Philippine language with hate and non-hate label.
[4] used Hindi and English code-switched tweets to classify tweets as hate and not hate. Out of the 
total, 6119 tweets and in Hindi and 6357 in English.
Two studies have focused on data from the recent Ukrainian-Russian war [2, 17]. [2] and [4] focused 
on hate target analysis together with binary hate speech classification. The study labeled tweets as hate 
and not hate and in terms of the target, the labels were directed and undirected which indicated whether 
the speech were targeted towards an individual or group or not directed at all. There were 6913 texts from 
Facebook, tweets from twitter (now X) and reddit related to the Ukrainian-Russian war. Similarly, [17] 
used hateMM dataset with 4700 data from Ukrainian and Russian war for binary classification of hate and 
none hateful content. HateMM is a multimodal dataset for hate video classification with 43 hours of the 
video from Bitchute. Out of the total data, 2665 were hate and 2058 were not hate. In terms of the target, 
237 were undirected while 2428 were not directed.

## Page 4

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
822
[6] used 400 labeled data from TOFORI forum for binary classification of hate and not hate. [15] 
and [18] focused on Spanish datasets. The former used 56869 Spanish tweets with 8715 hate tweets and 
the rest being not hate for the binary hate speech classification. The latter used 24000 Spanish tweets for 
the binary classification of hate and not hate content.
In terms of multiclass classification, [18] used 18614 clean, 1022 offensive and 709 hate comments and 
posts from Vietnam. From this study, the lowest percentage of hateful and related content was noted.
[16] dataset is the most commonly used hate speech dataset. In this dataset, 76% of the data is labeled 
as offensive, 16.6% non-offensive, 5% hate.
HASOC dataset is another commonly used dataset for the hate speech detection task. Kumari et al. 
(2022) used the HASOC 2021 dataset with 3000 posts for training and 844 posts for testing. Out of the 
total, 5.77% were hateful, 77.43% were offensive and 16.80% were labeled as neither.
[19] used 3395 tweets from the Nigerian 2023 electioneering period out of which 844 of them were code 
switched tweets in English, Yoruba and Naija language. The dataset was used for multiclass classification 
of normal versus abusive versus hateful versus contempt with a shift among the instances i.e, exclusion of 
instances not involved and binary classification of hate and not hate, offensive and not offensive.
[7] used 3000 tweets from campaign periods to do a multiclass classification of hate and offensive 
(HOF), hateful and non-hateful content. From this study, it is clear that offensive tweets can be hateful 
when tweets with insulting, deteriorating and abusive words are accompanied by the stereotype.
2.2  Low resourced language
According to [12], Natural language processing (NLP) has made significant progress for well-resourced 
languages such as English but has really lagged behind for low resource languages such as Swahili. Low 
resource language refers to those that have small amount of available resources such as written literature 
or other transcripts as well as internet presence [6]. It is therefore difficult to analyze and manipulate such 
language due to lack of requisite training qualities [20].
Swahili language is an African language of the Bantu family with a constantly changing vocabulary and 
is spoken by over 100 million people in East and Central Africa. However, it is still classified as a low-
resource language because of inadequate data for Natural Language Processing [21].
Low resource languages are those languages with scarcity of resources and are normally less privileged, 
less computerized, less frequently taught and less studied [22]. There is not enough data to make high 
performance statistical and NN based methods. For example, in Africa and India only 20% out of the 
7000 languages are under NLP research [6]. Most studies have concentrated on English whereas there 
are so many languages on social media platforms including regional and resource scarce languages [11]. 
Monolinguals are approximately forty percent of the whole population while multilingual and bilinguals 
and polyglots are approximately sixty percent [9].

## Page 5

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
823
2.3  Code Switching
Among bilingual and multilingual user groups in countries like Kenya, the use of English-Swahili 
code-switching and code mixing is a common practice in informal text-based communication such as 
messaging on social media platforms like twitter(now X) [21, 23]. [13] define Code-switching as the 
juxtaposition of speech belonging to two different grammatical systems or subsystems within the same 
speech.
Code-switching is typically considered informal and is most likely to be found in speeches and in casual 
texts as in social media. Users may be fluent in two or more languages but choose not to stay with one 
language [24]. The problem of code-switching has gained a lot of attention and has emerged as an active 
area of research. According to [10], the switching within the sentence is referred to as intra-sentential 
code-switching and the one happening at the sentence boundary is referred to as inter-sentential code 
switching. Intra-sentential code-switching is not a random mixing of one language with the other but the 
switching happens with the systematic interactions between the two languages.
From previous studies, most of the hate speech datasets are only focusing on English language and few 
code-switched languages with the common being Hindi-English. There is only one annotated publicly 
available hate speech detection dataset having Swahili texts and code switched English-Swahili code-
switched texts, which was used by [11]. However, the corpus was not annotated for language making 
it difficult for researchers who require specific language data for experimenting with or training of hate 
speech detection models. This signifies that there is a wider gap necessitating the need to curate a dataset 
having Swahili and code switched English-Swahili hate speech texts to enhance the detection of hate 
speech on social media.
Instances of code switching are given in Table 1.
3.  METHODOLOGY
This chapter outlines the processes in the curation of the hate speech dataset. Section 3.1 explains 
the data collection with sources of data. Section 3.2 covers preprocessing steps such as removal of 
punctuation marks, language identification, stopword removal and user de-identification. Sections 3.3 and 
Table 1.  Instances of code switching.
Language structure
Text
Type
Eng/Swa/Eng
Wheelbarrow style/iwachiwe tu wakisii ii hao ndio wanajua/ 
story for wheelbarrow
Intra-sentential
Eng/Swa
Kenya will never have peaceful election/sasawa
Emblematic
Swa/Eng/Swa
Ukweli Nairobi inaenda kuwa /headquarter/ya wakikuyu 
karibuni
Inter-sentential

## Page 6

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
824
3.4 describe the annotation guidelines and the detailed labeling procedure followed by human annotators. 
These steps were essential to ensure validation of the dataset.
3.1  Data collection
This study curated a combination of three publicly available datasets including Afrisenti [6], 
hate_Speech_Kenya [9] and politikweli [21] dataset shown in Table 2. The population of the dataset 
was 101,014 tweets obtained from merging the three datasets . In terms of ethical consideration, all 
the three datasets were originally from twitter (now X) and therefore the study followed twitter’s ethical 
considerations for the use and sharing of public data for research purposes to third party. The study 
ensured that care was taken to avoid exposure of sensitive contents and identities of individuals through 
anonymization and user de-identification.
Table 3 presents raw examples of hate speech tweets drawn from the merged hate speech dataset, 
illustrating the nature and tone of politically and ethnically charged language in online discourse. The 
samples reflect explicit references to ethnic groups such as the Luo and Kikuyu communities, showcasing 
Table 2.  Datasets description and access.
Dataset
Description
Access link and paper
Politikweli
50000 raw tweets in code switched English-Swahili and other 
African languages collected from 4th Oct 2021 to 5th Sep 2022. 
The dataset was sampled and used for misinformation 
classification with fact, fake and neutral labels. This study 
curated the raw Swahili and code-switched English-Swahili 
tweets from this dataset for hate speech with neither, hate and 
offensive labels.
Paper: [21]
Link: [25]
Afrisenti
3114 tweets labeled as neutral, positive and negative.
Collected in 2014 consist of Swahili tweets.
Only the tweets were extracted from this dataset and annotation 
with hate speech labels done.
Paper: [26]
Link : [27]
Hate_speech_
Kenya
48000 raw tweets in Swa-Eng, English, Swahili and other African 
languages 
-Developed by researchers at Nazarene University
-Tweets from 2012 and August 2017 General election 
Curated for hate speech detection using neither, hate and 
offensive labels for hate speech categories. Different from this 
work, the dataset had not been annotated for language labels as 
Swahili and English-Swahili. In addition, hate tweets were not 
annotated for hate target, where targets labels in this case are 
politics, disability, religion, social status, ethnicity, nationality, 
gender and others.
paper: [9]
Link: [28]

## Page 7

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
825
derogatory or divisive expressions often rooted in political alignment or stereotyping. Some tweets include 
code-switched English-Swahili phrases, slang, and informal syntax, emphasizing the linguistic complexity 
typical of social media content. These examples serve as qualitative evidence of the quality of the hate 
speech dataset.
3.2  Data Preprocessing
Natural Language Processing requires data to be pre-processed to guarantee effectiveness in models’ 
performance in different machine learning tasks [28]. Preprocessing also served as a way to ensure that 
ethical guidelines on responsible Artificial intelligence and Natural language processing are taken into 
consideration.
The following are the standard NLP preprocessing steps which were considered for this work:
i.  Removal of punctuationa marks
Another important NLP preprocessing technique was punctuation marks removal. Punctuation marks 
were used frequently in the tweets. This study removed punctuations with the aid of Regex library as a 
form of data normalization. Algorithm 1 shows the process of punctuation marks removal.
ii.  Stopwords removal
This is another most important NLP preprocessing technique [28]. Stopwords are those words which 
are frequently used but with no meaning. The removal of stopwords such as the determiners, articles and 
prepositions enabled the study to focus on important words carrying the most contextual meaning relevant 
for the task.
Swahili stopwords such as na/and, kwa/in, lakini/however, hata/also, kama/like, hadi/even, vya/
for, yao/their, hizo/those and other Swahili stopwords from [28] were removed. English stopwords were 
removed using gensim and natural language toolkit (NLTKb) libraries as shown by Algorithm 2.
a  https://www.regexlib.com/
b  https://pypi.org/project/demoji/pythonemojilibrary
Table 3.  raw sample hate speech texts from the merged hate speech dataset.
nani ni miguna miguma mwiteni baba kama raila maanake nyinyi wajaluo / “Who is Miguna, call him ‘Baba’ 
like Raila, because you Luo people
while theyre busy yapping kikuyus are chasing paper rt kikuyus hahahaha ur tlkn abt kikuyus hamna kazi ya 
kufanya / "While they’re busy yapping, Kikuyus are chasing paper. Right? Kikuyus, hahahaha, you’re talking 
about Kikuyus. You have no work to do."
which kenya luos are not the only kenyans bwanawaza zakouhurutotanotena

## Page 8

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
826
Algorithm 2.  Stopword Removal.
Libraries Used:
• nltk.corpus.stopwords – for English stopwords
• gensim.parsing.preprocessing.STOPWORDS – for Gensim’s predefined stopwords
• Custom-defined list – for Swahili stopwords
Input:
• A list of words from a tweet
• Combined stopword set (combined_stopwords) from NLTK, Gensim, and Swahili sources
Output:
• A list of words with stopwords removed
Steps:
1.  Import stopwords from the following libraries:
a. nltk.corpus.stopwords
b. gensim.parsing.preprocessing.STOPWORDS
2.  Define a set of Swahili stopwords manually or load from a resource.
3.  Combine stopwords from NLTK, Gensim, and the Swahili list into a single set:
combined_stopwords = nltk_stopwords ∪ gensim_stopwords ∪ swahili_stopwords
4.  For each word w in the input tweet:
a. Convert w to lowercase
b. If w ∉ combined_stopwords, keep it
5.  Return the cleaned list of words
Algorithm 1.  TextClean = RemovePunctuation(Text).
Input:
Text = A string containing raw text with punctuation and digits.
Output:
TextClean = The text with punctuation and unwanted characters removed
1: // Step 1: Remove punctuation characters
2: Text ← join all characters in Text where char ∉ string.punctuation
3: // Step 2: Remove all numeric digits
4: Text ← Text with all matches of pattern ‘[0-9]+’ replaced by “”
5: // Step 3: Remove non-alphanumeric symbols (except ?, !, ., ,)
6: Text ← Text with all matches of pattern ‘[^a-zA-Z0-9?!.,]+’ replaced by “ ”
7: Return Text as TextClean

## Page 9

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
827
iii.  Anonymization and textualizing of emojis
The dataset contained user mentions, Hashtags and URL, which could reveal the username of the 
hate speech perpetrators or the target. This study removed URLs from the dataset to ensure privacy. User 
mentions starting with @ were also removed to allow concentration on the texts. Both user mentions, 
hashtags and URLs were removed by the regex library. The emojis in the dataset were replaced with the 
actual text representation i.e, laughing emoji, crying emoji using the emojic library to give context during 
annotation. Algorithm 3 shows the procedures for anonymization and the text conversion of emojis.
Algorithm 3.  CleanTweet = Clean(Tweet).
Input:
Tweet = Raw tweet text string
Output:
CleanTweet = Cleaned tweet string
1: Raw ← Tweet
2: // Step 1: Remove hashtags and user mentions
3: for each pattern p ∈ {#\d+, USERNAME_\d+, @([^\s:]+)} do
4: Raw ← Raw with all matches of p replaced by “”
5: end for
6: // Step 2: Clean hyperlinks and markup symbols
7: for each replacement (pattern, replacement_string) ∈ {
 (<[a][^>]*>(.+?)</[a]>, ‘Link.’),
 (&gt;, ‘’),
 (&#x27;, “'”),
 (&quot;, ‘"’),
 (&#x2F;, ‘ ‘),
 (<p>, ‘ ‘),
 (<i>, ‘ ‘),
 (</i>, ‘’),
 (&#62;, ‘’),
 (\n, ‘’)
 } do
8: Raw ← Raw with all matches of pattern replaced by replacement_string
9: end for
10: Return Raw as CleanTweet
c  https://pypi.org/project/emoji/

## Page 10

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
828
iv.  Language identification
The study only focuses on tweets in Swahili and code-switched English-Swahili. Tweets in other 
languages such as pure English and other local languages were removed. The process of removing English 
tweets as revealed by Algorithm 4 was done using the language detectd library in python. However, due 
to the complex nature of social media tweets, manual removal of tweets which were in other languages 
such as Luo and Kikuyu was also considered.
vi.  Conversion of text to lowercase 
Lowercasing texts during preprocessing ensured normalization of the data thereby treating words 
in different capitalization as one. For example, the words Hate and hate were treated as hate after 
preprocessing. Lowercasing was done using the NLTK library. The steps followed are shown by 
Algorithm 5.
Algorithm 4.  data_filtered = LanguageFilter(data, detect_language).
Input:
data = Dataset containing a column of tweets
detect_language = Function to detect the language of a tweet
for each tweet t ∈ data do
    lang ← detect_language(t)
    Append lang to corresponding row in data as a new column language
end for
for each row r ∈ data do
    if r.language ≠ ‘en’ then
        Add r to data_filtered
    end if
end for
Remove column language from data_filtered (optional)
Export data_filtered to CSV as filtered_hate_speech_data.csv
Return data_filtered
d  https://pypi.org/project/langdetect/regexlibrary

## Page 11

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
829
vii.  Tokenization
Tokenization of the data was done using the Tokenizer class from TensorFlow’s Kerase preprocessing 
module to convert textual data into numerical sequences. All the texts input were first standardized 
to string format to ensure compatibility. The tokenizer was then fitted on the text corpus to generate a 
word index, which maps each unique word to an integer. Subsequently, the texts were transformed into 
sequences of these integers and padded to a uniform length of 100 as shown in Algorithm 6, using post 
padding to ensure consistent input shape for model training. This preprocessing step was essential for 
preparing the language data for machine learning models.
3.3 Annotation guidelines
Training of the annotators is vital in the achievement of better annotation results. The study did a 
purposive sampling of 30 tweets to be used as the pilot dataset and for provision of guidance on the 
annotation of the whole dataset. This study adopted an annotation guideline framework by [9, 11] in 
annotating the hate speech dataset in hate, offensive and neither categories [11, 16, 29-30]. In addition, 
we labeled hate speech dataset with language and the hate tweets for the target as ethnicity, gender, 
politics, disability, nationality, religion, social status and other. All the tweets were annotated for language 
with either Swa or Eng-Swa label.
3.3.1 Annotation guideline for language and hate speech categories:
i) Hate: tweets with derogatory, insulting, humiliating, abusive, or discriminatory language that 
targets specific individuals or groups based on their identifiable characteristics, including but not 
limited to gender, sexual orientation, political affiliation, disability, religious beliefs, health conditions, 
Algorithm 5.  DF = LowerCase(DF).
Input:
DF = A DataFrame with a column tweet containing text entries.
Output:
DF = The same DataFrame, with all words in the tweet column converted to lowercase.
1: for each row in DF do
2:     T ← DF[‘tweet’] at current row
3:   　  T_lower ← join all words w ∈ T.split() with w converted to lowercase
4:     DF[‘tweet’] at current row ← T_lower
5: end for
6: Return DF
e  Keras framework https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer

## Page 12

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
830
race, ethnicity, nationality, colour, behaviour, or socio-economic status with the aim of inciting and 
perpetuating hatred, discrimination, violence, and other harmful actions against the targeted individuals 
or groups.
ii) Offensive: tweets containing disrespectful, derogatory, insulting, abusive and discriminatory terms 
without necessarily targeting individuals or groups based on special protected attributes called stereotypes.
iii) Neither: tweets that does not contain offensive or hateful language and does not violate community 
guidelines or standards of respectful communication.
iv) Swa: For tweets having pure Swahili ikiwa unajua jinsi ya kuvuta pumzi kidogo ya kifaransa.
v) Eng-Swa: for tweets having code switched English and Swahili.
3.3.2  Target Annotation Guideline
Politics: if the hate speech targets political figures, parties, or ideologies. Look for words related to 
politics, such as the government, party, election, or specific political figures.
Algorithm 6.  X_padded = TokenizeAndPad(X_texts).
Input:
X_texts = A list of raw text entries (e.g., tweets or sentences).
Output:
X_padded = A list of tokenized and padded sequences, with padding applied at the end, and a maximum 
sequence length of 100.
1: // Step 1: Convert all entries in X_texts to strings
2: for each element text ∈ X_texts do
3: 　　text ← convert text to string
4: end for
5: // Step 2: Initialize Tokenizer
6: Initialize tokenizer as Tokenizer()
7: // Step 3: Fit tokenizer on X_texts
8: tokenizer.fit_on_texts(X_texts)
9: // Step 4: Convert X_texts to sequences of integers
10: X_sequences ← tokenizer.texts_to_sequences(X_texts)
11: // Step 5: Apply padding to sequences (post-padding, max length 100)
12: 　　X_padded ← pad_sequences(X_sequences, padding=‘post’, maxlen=100)
13: Return X_padded

## Page 13

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
831
Gender: if the hate speech refers to someone’s gender or promotes stereotypes based on gender. Check 
for the key terms including woman/mwanamke, man/mwanaume, girl/msichana “boy/mvulana, and any 
derogatory terms related to gender.
Disability: if the hate speech targets individuals based on their physical or mental disabilities by looking 
for terms such as disabled, handicapped, bubu/dumb, mwendawazimu or any derogatory terms used 
against disabled people.
Ethnicity: if the hate speech targets specific ethnic groups or cultures. By looking for Keywords 
including names of ethnic groups like Luo, Kikuyu and any derogatory terms associated with these groups.
Religion: if the hate speech uses slurs, insults, or negative stereotypes against individuals or groups 
based on their religious beliefs. look for mentions of specific religions, such as Christianity/kristo, Islam/
muislamu, Judaism, Hinduism or references to religious figures such as Jesus, Muhammad, Moses and 
sacred texts like the Bible and Quran.
Social status: Look for mentions of specific social classes, such as rich, poor, wealthy, middle class, or 
working class. Label as Social Status if the hate speech uses slurs, insults, or negative stereotypes based on 
someone’s economic situation. Analyze the context in which social status terms are used.
Nationality: Hate speech that targets or insults a person or group based on their nationality, national 
origin, or citizenship. This includes slurs, insults, or stereotypes used to demean or belittle a group of 
people based on their nationality.
Other Targets: If the hate speech does not fit into these categories, consider labeling it as Other. This 
can include hate based on age, sexual orientation, games teams.
The samples given to guide in the annotation is shown in Table 4.
3.4 Annotation Procedure
To ensure a well-rounded understanding of the socio-linguistic context, the dataset was annotated by 
five independent annotators from different geographical regions in Kenya, comprising three male and 
two female. All the annotators had a degree in computer science and had undergone a natural language 
processing training course. They were all fluent in English and Swahili and had prior experience of 
linguistic annotation tasks.
The dataset annotation began by a pilot dataset which was selected based on purposive sampling 
technique. Independent annotators were given a similar pilot dataset of 30 tweets. This pilot dataset 
ensured a balanced sample with diversity of hate contents and categories while also ensuring quick 
feedback and iterative training for improvements. The first pilot dataset followed the same labels of hate, 
offensive and neither during annotation. Randolph’s kappa was used to measure the rate of agreement 
among the annotators for the pilot dataset and the general samples annotated. Randolph’s kappa was

## Page 14

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
832
Table 4.  Annotation guideline samples per label.
CATEGORY
TWEET
LABEL
Hate speech 
detection
watu wa canaan ni kama walikuwa wanaenda hapa tu githurai wanachezea 
railapresser kenyadecided iebcresults/watu wa canaan ni kama walikuwa 
wanaenda hapa tu githurai wanachezea railapresser kenyadecided iebcresult
Hate
washenzi wa pwani kachagua mtu aliyepata dminus halafu wanakuja 
kutulilia shogah nyinyi kumamazenu endeni mkalie kwa choo jameni ujinga 
wenu sio mzigo wetu jipeni shughuli
hate
kutomba mkundu wangu mkali mpaka nitaporomoka
offensive
ikiwa unajua jinsi ya kuvuta pumzi kidogo ya kifaransa/“If you know how to 
take a little breath of French”
Neither
kuna vikundi vingi vya kikundi /There are lots of groups of a group
Neither
Language
ikiwa unajua jinsi ya kuvuta pumzi kidogo ya kifaransa/“If you know how to 
take a little breath of French”
swa
words that can kill a luhya karibu ndani hata ndio tumemaliza kula/“words 
that can kill a luhya welcome inside, we have just finished eating”
Eng-swa
Hate target
kila mtu akufe kifo chake ripjubilee/“May everyone die their own death. RIP 
Jubilee”
politics
wanawake hufanya kama hawajawahi kuona pizaa/Women behave as if they 
have never seen pizza
gender
vipuli vya bubu hufanya vitu na bubu wajinga/gadgets of the dumb do things 
with foolish dumb
disability
waluhya munatuaibisha tabia ya madame waluhya hawa exposing cleavage 
boobs zao coz matiti zao ni/luyhas you are disappointing us these luhya 
ladies behavior of exposing their boobs is
Ethnicity
wanaomba na wameshika mapanga hao wakristo unafiki kiasi chake hiki 
ripmsando/they are praying yet they have carried their pangas those hypocrite 
Christians ripmsando
Religion
je wewe kuchukua homie tajiri wote ni takataka wewe karibu bado usikilize 
lil b wow/“Are you taking homie every rich as trash? You’re almost there, still 
listening to Lil B. Wow.
Social-status
wakanyimwa majob ukabila wakenya wawe rada raundi this/They were 
denied jobs because of tribalism, Kenyans should be vigilant, this round.
Nationality
Nahitaji kuwafunza jinsi ya kukula dengu maumbwa nyinyi/I need to teach 
you how to consume beans you dogs
other

## Page 15

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
833
chosen considering the fact that the study had no predefined number of tweets to be assigned a given label 
and had more than two annotators annotating the same sets of tweets.
In terms of the inter agreement, overall agreement of 0.437 and free marginal kappa of 0.435 was 
achieved for the first pilot dataset. The low agreement score was as a result of inherent bias in annotation 
and the fact that the annotators were labelling based on presence of words without considering the context 
and defensive phrases which aims at defending the other groups such as “Don’t’ like the racist’,’ do not 
insult luo men/ usitusi wanaume wajaluo’.
Second meeting with the annotators was organized to address ambiguous cases and clarify any 
discrepancies in labelling after which a second pilot dataset of 30 tweets were given to the annotators. 
For the second agreement, 0.566 overall agreement was achieved showing that the annotators agreed 
56.6% of the time. Free marginal kappa 0.552 was achieved showing moderate agreement by chance. The 
difference of 0.117 in marginal kappa scores between the first and second pilot dataset shows a substantial 
improvement in terms of the bias reduction therefore annotation consistency.
Following the significant improvement in the inter annotator agreement, the annotators were therefore 
provided with a cleaned set of the hate speech dataset and instructed to assign one of the three predefined 
labels to each text sample based on the annotation scheme. The annotation was done on excel platform. 
To ensure consistency and reliability in the annotation process, annotators were trained on sets of 
annotation guidelines and provided with examples of text samples for each label. In addition, each tweet 
was annotated by three annotators and the final label assigned through majority votes.
The overall inter-annotator agreement score calculated by a random sample of 1000 tweets was found 
to be 0.7 and Randolph’s marginal kappa was achieved to be 0.68 between annotator 1 and 2 and 
0.65 between annotator 1 and 3 showing a high annotation consistency. The calculations of the overall 
inter annotator agreement using pandas library in python can be found in the project github repository. 
Multilingual index of 0.72 was achieved showing a good score for code switched English-Swahili tweets.
Table 5 shows pairwise agreements for the pilot dataset and the overall samples.
Table 5.  Pairwise inter-annotator agreement.
Dataset
Overall agreement score
Marginal kappa score
Pilot 1
0.437
0.435
Pilot 2
0.566
0.552
General samples annotated
0.700
0.680

## Page 16

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
834
4.  DATA ANALYSIS AND FINDINGS
We curated Swahili and code switched English-Swahili hate speech textual dataset with the final dataset 
having five columns including Tweet-ID, text, label, language and target. Tweet-ID shows the identifier for 
each final data, text column contains tweets, language column shows the language label allocated for the 
tweets, and the target shows the label allocated for the targets of hateful tweets.
This section analyzes the structure and content of the annotated hate speech dataset. Section 4.1 
presents word frequency statistics to highlight dominant terms in hate, offensive and neither classes. 
Section 4.2 summarizes the final distribution of samples by label and language. Section 4.3 details 
the target categories of hate speech, such as ethnicity and political affiliation. Section 4.4 discusses 
experimental validation, including comparative analysis of the baseline model performance. Section 
4.5 gives comparative analysis between the curated dataset and the existing datasets.
4.1  Hate speech dataset word distribution
Table 6, 7 and 8 gives the total number of common specific words per class label together with the 
corresponding percentages. From the list ranked from the top, the most frequent words appearing for the 
hate category are wajaluo/Luos, wakikuyu/kikuyus, muislamu/islamic, wazungu/Whites, wajinga/stupid 
people and wahindi/Indians. For the offensive category, pussy, matako/buttocks, jembe/prostitute, bitch, 
takataka/rubish, wakati/time. Mjinga/stupid, Nigga, shit seem to be the most common words. Lastly, 
sana/very much, kwenye/in, lakini/but, watu/people, sinema/film, iebc,mkuu/great person, filamu/film, 
moja/one, uchaguzi/election and Habari/news are the mostly frequently appearing words for the neither 
category.
Figure 1 shows word cloud for the hateful contents. Translations for the Swahili words in the word 
cloud not given in Table 6 due to their insignificant percentages are given as warudi/they go, mbaya/bad, 
wapi/where, uko/there, sisi/us, juu/up, sababu/reason, ndani/inside, wameru/people from Meru, Ndo/so 
that, kitu/something, nchi/country, bila/without, saa/time, luo/luo person, punda/monkey.
Figure 2 shows word cloud for the offensive contents. Translations for the Swahili words in the word 
cloud not given in Table 7 due to their insignificant percentages are given as Hivyo/that way, kijinga/in a 
stupid manner, lazima/a must, pia/also, najua/I know, Tayari/ready, kubwa/big, ambaye/that, kazi/work, 
mwenyewe/alone.
Figure 3 shows word cloud for the contents that are neither hate nor offensive. Translations for the 
Swahili words in the word cloud not given in Table 8 due to their insignificant percentages are given as 
gani/which one,sauti/sound, nina/I have, biashara/business, nadhani/I think, basi/therefore, huwa/always, 
namba/number, wengine /some people, kweli/true, labda/may be.

## Page 17

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
835
Table 6.  Hate Words Frequency & Percentages_i.
Word
English Version
Count
Percentage count
Wajaluo
Luos
519
1.21%
Wakikuyu
Kikuyus
500
1.16%
Muislamu
Islamic
353
0.82%
Wazungu
White people
324
0.75%
Wajinga
Stupid people
163
0.38%
Wahindi
Indians
137
0.32%
Wakale
Kalenjins
116
0.27%
Waarabu
Arabs
106
0.25%
Wao
Them
88
0.20%
Nyinyi
You
86
0.20%
Baba
Father
86
0.20%
Uhuru
Uhuru
83
0.19%
Wakamba
Kamba people
82
0.19%
Bubu
Dumb
79
0.18%
Waswahili
Swahili people
68
0.16%
Raila
Raila
54
0.13%
Ugali
Ugali
44
0.10%
Kill
Kill
37
0.09%
Ruto
Ruto
35
0.08%
Ndizi
Banana
33
0.08%
Malaya
Prostitute
22
0.05%
Railapresser
Raila presser
21
0.05%
Kisii
Kisii
17
0.04%
Wabaya
Bad people
5
0.01%
Wakristo
Christians
3
0.01%

## Page 18

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
836
Table 7.  Offensive Words Frequency & Percentages.
Word
English version
Count
Percentage count
Pussy
Pussy
3594
3.39%
Matako
Buttocks
1559
1.47%
Jembe
Prostitute
1138
1.07%
Bitch
Bitch
991
0.94%
Takataka
Rubbish
687
0.65%
Wakati
Time
684
0.65%
Mjinga
Stupid
655
0.62%
Nigga
Nigga
473
0.45%
Shit
Shit
351
0.33%
Huyu
This person
299
0.28%
Mbaya
Bad
293
0.28%
Mtombaji
Fucker
280
0.26%
dick
Dick
251
0.24%
Wako
Yours
213
0.20%
Huyo
That
195
0.18%
Fuck
Fuck
183
0.17%
Msichana
Girl
173
0.16%
Mboro
Penis
168
0.16%
Mlafi
Glutton
149
0.14%
Kitoto
Childish
132
0.12%
Wasichana
Girls
116
0.11%
Wanawake
Women
113
0.11%
Fuckin
Fucking
113
0.11%
Vidonda
Ulcers
96
0.09%
Wazimu
Mad
72
0.07%

## Page 19

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
837
Table 8.  Neither Words Frequency & Percentages.
Word
English version
Count
Percentage count
Sana
Very much
807
0.64%
Kwenye
In
764
0.61%
Lakini
But
412
0.33%
Watu
People
381
0.30%
Sinema
Film
322
0.26%
Iebc
Iebc
297
0.24%
Mkuu
Leader
275
0.22%
Filamu
Film
264
0.21%
Moja
One
251
0.20%
Uchaguzi
Election
245
0.19%
Habari
News
245
0.19%
Bora
Good
236
0.19%
Simu
Phone
206
0.16%
Bado
Not yet
183
0.15%
Kwamba
That
178
0.14%
Mzuri
Good
178
0.14%
Kabisa
Infact
173
0.14%
Vizuri
Good
158
0.13%
Maisha
Life
156
0.12%
Elect
Elect
143
0.11%
Election
Election
135
0.11%
Mungu
God
111
0.09%
Kuona
See
99
0.08%
Wanawake
Women
88
0.07%

## Page 20

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
838
4.2  Final Dataset Size Per Label and Language
Table 9 gives the distribution of the dataset in terms of the hate sentiments together with the 
corresponding language. The table shows a total of 19369 tweets. The result shows that 79.6 percent 
of the tweets curated for hate speech tasks are in Swahili language. The rest of the tweets are in code-
switched English-Swahili language. In terms of hate instances, the lowest number of hate tweets as 
compared to other labels shows the reality in normal conversations on social media. There are generally 
more clean tweets as compared to hateful and related contents under normal scenarios of conversations in 
social media platforms.
Figure 2.  Offensive contents word cloud.
Figure 1.  hateful contents word cloud.

## Page 21

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
839
Figure 3.  neither contents word cloud.
Figure 4 on the other hand shows the percentage distribution of tweets per label. The figure is derived 
using only code-switched part of the hate speech dataset. It is easy to see from the figure that there are 
more hate speech contents as compared to offensive contents. This is contradictory with the whole 
dataset where there is a much higher percentage of offensive contents as compared to hate. From the 
interpretation, it can be concluded that a greater percentage of the offensive content is in Swahili.
4.3  Percentage Distribution of Hate Targets
The distribution of the labels in the hate dataset in Table 10 reveals that the majority of the tweets are 
categorized under ethnicity, which makes 68.3% of the total. Although the dataset and the study’s title 
is primarily focused on political hate speech detection, the high percentage of tweets targeting ethnicity 
is justifiable due to the strong interplay between ethnic identity and political discourse, particularly in 
contexts of African continent [33].
Table 9.  distributions of hate speech labels with corresponding language.
Labels
Swa
Eng-Swa
Offensive
6526
1106
Hate
2065
1333
Neither
6824
1515

## Page 22

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
840
It is worth noting that the dataset only contains political linguistic patterns that are vital for the content 
moderation systems development and not political figures that can promote conflicts or violence. Political 
rhetoric and affiliations are often shaped by ethnic lines, and hate speech directed at political opponents 
frequently takes the form of ethnic slurs or attacks [33].
Other category follows with 9.2%, suggesting a diversity of topics outside the major categories 
including age, football teams and behavior. Religion accounts for 8.2%, highlighting the presence of 
religious discussions or mentions. Politics also forms a notable part, at 5.7% reflecting the study’s focus 
in political discourse. Minor representations of hate targets are in gender (2.9%), disability (2.7%), and 
nationality (2.1%), while social status has the least representation at 0.9%. This suggests that while 
Figure 4.  Percentage distribution of tweets per label for the code-switched dataset.
Table 10.  Percentage distribution of hate targets.
Target
Count
Percentage count
Ethnicity
2799
68.3
Other
379
9.2
Religion
336
8.2
Politics
233
5.7
Gender
117
2.9
Disability
112
2.7
Nationality
85
2.1
Social status
37
0.9

## Page 23

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
841
ethnicity and religion dominate the dataset, issues such as gender, disability, and social status are less 
frequently addressed in the tweets. The imbalance in distribution emphasizes the strong focus on ethnic 
and political issues, with other aspects being less prominent in the conversation. Pie chart in figure 5 was 
used to visualize these statistics.
4.4  Experimental Validation of The Dataset
To assess the suitability of the curated hate speech dataset, SwahBERT model, a variant of BERT pre-
trained on Swahili texts, was fine-tuned using this dataset on google colab pro with 100 computing units. 
The fine-tuning process was conducted over three epochs, with a training batch size of 16 and a test batch 
size of 64, warmup steps of 500 and a weight decay of 0.01.
The models performance was evaluated using accuracy, recall, precision and the F1-score, which 
was selected due to the imbalanced nature of the dataset. The F1-score provided a balanced measure by 
averaging precision and recall, ensuring that both false positives and false negatives are accounted for.
Despite the curated hate speech dataset’s imbalance, the fine-tuned SwahBERT model achieved 
an F1-score of 0.89, indicating ability to distinguish hate speech from non-hate speech content. The 
performance could be optimized through further fine tuning and data augmentation.
Bi-LSTM based deep learning model was trained on the code-switched English-Swahili hate speech 
dataset. Google colab pro, Keras Framework with tensorflow backend wre applied in training of the 
Bi-LSTM model. In terms of the hyper-parameters, Glove embeddings of 100 dimension, fastText 
Figure 5.  percentage distribution of hate target labels.

## Page 24

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
842
embeddings with 100 dimension achieved through principal component analysis, two Bi-LSTM layers, 
Adams optimizer, softMax activation function for prediction and ReLU activation function for dense layer, 
dropout of 0.2 after each layer and 10 epochs were used in training the Bi-LSTM model.
Synthetic minority oversampling technique which works by generating synthetic samples in the training 
set ensured a balanced training set. Test sets are representations of real world data and applying SMOTE 
on the test set could yield unrealistic performance as a result of data leakage. SMOTE, improved the 
Bi-LSTM models recall for the hate class by 0.19 from 0.57 to 0.76 showing its significance in creating a 
balance for the actual positive predictions made by the model.
The dataset contains a higher percentage of Swahili words as compared to English words in the texts. 
For this reason, it was noted that training Bi-LSTM features with fastText embeddings yielded better results 
with a recall=f1-score=precision=accuracy of 0.87 as compared to when gloVe embeddings with a recall 
of f1-score=precision=accuracy= 0.75. For the hate class, a recall of 0.75 and 0.57 was achieved with 
fastText and gloVe embeddings respectively. The results show the strength of fastText embeddings in 
capturing the grammatical and semantic complexities in text code-switched English-Swahili texts.
In terms of error analysis, Bi-LSTM model yielded a better performance with a slight difference in 
misclassifications between the validation and test set. We noted that 17.2% of hate instances were 
misclassified as either neither or offensive. However, the misclassification of hate instances was reduced 
by 2 for the test set showing a better generalization of the model as shown by figure 6.
Non-linear support vector machine was trained on both the Swahili and code-switched part of the 
dataset. The model achieved a score of 0.88 for f1-score, recall , precision and accuracy for code-
switched part of the dataset and 0.89 for the Swahili part of the dataset. This insignificant difference of 
0.01 shows that even the code-switched dataset is enough to train any machine learning model. Confusion 
Figure 6.  Bi-LSTM model confusion matrix on the code-switched texts.

## Page 25

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
843
matrix in figure 7 shows that for the Swahili part of the dataset, the model misclassified 20% and 6.5% of 
the hate instances as neither and offensive respectively. In addition, 13.1% of the offensive instances were 
misclassified as neither showing the inability of the traditional machine learning techniques to capture the 
semantic and syntactic complexities in Swahili hate speech texts.
On the other hand, the confusion matrix in figure 8 shows the predictions made by the SVM model on 
the code-switched part of the dataset. Results reveal that traditional machine learning models perform 
better on relatively smaller dataset with few misclassifications for the neither and offensive classes. 
However, there was misclassifications for the hate class where 10.1% and 7.6% of the hate instances were 
misclassified as neither and offensive respectively.
The results suggest that the dataset is well structured and suitable for training robust hate speech 
detection models especially with further fine-tuning. The scripts with detailed information about the 
models, the dataset and readme file have been made public for accountability and replicability in the 
project GitHub repositoryf.
4.5  Comparative Analysis Between The Curated Dataset And The Existing Related Datasets
Unlike previous hate speech detection datasets that focus majorly on English , such as [16] and HASOC 
dataset, this study provides a low resourced dataset tailored for hate speech detection in Swahili and 
code-switched English-Swahili texts. The inherent nature of bias in hate speech in real world platforms like 
Figure 7.  SVM confusion matrix on Swahili test set.
f  https://github.com/Odhiambo-nelson/Swahili-and-English-Swahili-hate-speech-models-and-datasets

## Page 26

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
844
X is confirmed by HEOT dataset [8] which has only 323 hateful contents out of 3679 texts and, hate and 
offensive dataset by [16] with only 5% out of the 24000 texts being hateful.
As opposed to Hate_speech_Kenya dataset, which lacks language and hate target labels, this dataset 
provides annotation for language and hate target labels. This enables deeper analysis of the hate speech 
target stereotypes. While politikweli and Afrisenti datasets contain Swahili texts, they have not been 
curated for hate speech detection tasks. For this reason , this is the first dedicated Swahili and code-
switched English-Swahili hate speech detection dataset with extensive labeling for the hate speech 
categories, language categories and hate speech target categories. The comparative analysis has been 
provided in Table 11.
5.  LIMITATIONS
The dataset focuses primarily on Swahili and code switched English-Swahili tweets which may not 
fully represent all linguistic diversities especially in multilingual environments. Given that more than 
half of the tweets were labeled as offensive and neither, there may be bias in testing for hateful contents 
due to the limited number of tweets having the hate label. Manual annotation is always subjective 
and the interpretations of what is considered hate or offensive could result in errors during annotation. 
While we annotated the dataset with the targets, the targets included may not fully represent all the hate 
target categories.
Figure 8.  SVM model confusion matrix on code-switched test set.

## Page 27

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
845
6.  RECOMMENDATIONS AND FUTURE WORK
To address the limitations in section 5, future work will expand the dataset to include other regional 
languages and dialects, ensuring broader linguistic representation. Other data augmentation techniques, 
such as synthetic data generation and oversampling, will be explored to improve model robustness against 
class imbalance.
Additionally, future research will include further transformer-based and the state of the art model’s 
fine-tuning for low-resource Swahili language. Future integration of the dataset with datasets from other 
Table 11.  Comparative analysis between the curated and existing datasets.
Dataset
Language
Total sample
Hate speech labels
Target labels
This study
Swahili and code-
switched English-
Swahili hate speech 
dataset
Swahili
Code-switched 
English-Swahili
19369
Hate
Offensive Neither
Ethnicity, politics, 
religion, disability, 
social-status, 
nationality, other
Politikweli
English, code-
switched 
English-Swahili
Swahili
50000 raw tweets
Curated for political 
misinformation 
detection task with 
fake, fact and neutral 
labels
Not applicable
Hate_speech_Kenya
English, Swahili, 
English Swahili,
Other African 
languages
48000
Annotated with 
Hate, offensive,
neither
No hate target 
labels,
No language labels
Afrisenti
Swahili
3114
Sentiment analysis 
based labels of 
neutral, negative, 
positive
No hate speech 
target labels
HateMM
Ukrainian , 
Russian
43 Hours of 
video from 
Bitchute
Hate, not hate
Directed, 
undirected targets
Hasoc (2021)
English, Hindi, 
German
10311
Hate, offensive, 
neither
No hate speech 
target labels
HEOT [8]
Hindi-English
1414-Non 
offensive
1942-Abusive
323-Hate speech
Hate
Non offensive
Abusive
No hate target 
labels
Hate speech offensive 
tweets by [16]
English
24000
Hate, offensive, 
neither
No hate target 
labels

## Page 28

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
846
platforms and other modes of hate speech datasets, such as HEOT [8] and hateMM, will be achieved by 
aligning standardizing language labels, and merging texts with similar categories of hate, neither/neutral 
and offensive, thus ensuring diverse dataset for multimodal hate speech detection.
Additionally, data augmentation will be applied to improve on the diversity of the dataset to aid in fine 
tuning of the state of the art models.
This approach will enhance the dataset’s utility for cross-lingual and cross-cultural hate speech 
detection while ensuring broader generalizability and robustness in real-world applications. Future studies 
will also include experimental analysis of the hate target using machine learning models.
7.  SIGINIFICANCE OF THE CURATED DATASET
The dataset, consisting of 19369 tweets, provides a valuable resource for training and evaluating 
machine learning models for multilingual hate speech detection. By annotating the tweets with hate 
classes, targets, and languages, this study not only contributes to the development of more accurate and 
inclusive hate speech detection systems but also supports further research on language biases, social 
media moderation, and content filtering. Beyond hate speech detection, the curated dataset has broader 
applications in AI models for science and smart medicine.
AI models can leverage this dataset to track psychological distress caused by hate speech, identify 
patterns in hate speech and offensive content incidents, and develop predictive systems for early 
intervention and recommendations for mental health support. In public health, the dataset can be used to 
assess the impact of hate speech on marginalized communities, guiding policy decisions and social media 
governance frameworks.
This dataset can serve as a benchmark for future studies on NLP techniques in African languages and 
promote the advancement of natural language processing applications in low-resource settings.
8.  CONCLUSION
In conclusion, this study addresses a significant gap in the field of hate speech detection by curating 
and validating a comprehensive Swahili and code-switched English-Swahili hate speech dataset having 
19369 texts. The research highlights the challenges of working with low-resource languages Swahili and 
code-switched English-Swahili, which have been underexplored in previous studies focused mainly on 
high-resourced languages like English. The dataset suitability was validated by fine tuning of the SwahBert 
model which achieved a remarkable f1-score of 0.89. In addition, training Bi-LSTM model and applying 
SMOTE on the training set improved recall for the hate class from 0.57 to 0.76 showing the significant role 
of oversampling techniques in machine learning tasks. The strength of fastText embeddings of capturing 
grammatical complexities in code-switched English-Swahili texts was also noted with a remarkable

## Page 29

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
847
f1-score of 0.87. The dataset validation results show its practicability in the development and fine-tuning 
of machine learning and transformer based models.
9.  DATA AVAILABILITY STATEMENT
The curated hate speech textual dataset [31, 32] can be accessed and downloaded via Zenodo and 
the science database’sg repository. Data identification numberh for the dataset in zenodo is 10.5281/
zenodo.14103420. The dataset also can be assessed through the Data Intelligence’s data repository at 
https://doi.org/10.57760/sciencedb.27635.
AUTHORS CONTRIBUTIONS
Nelson Odhiambo Onyango: Conceptualization; Methodology; Data Curation; Analysis and 
Visualization; Writing Original Draft.
Lilian Wanzare : Writing-review; Supervision & Project administration.
James Obuhuma : Supervision; Project administration & writing- review.
DECLARATION OF COMPETING INTEREST
The authors declare that they have no known competing financial interests or personal relationships that 
could have appeared to influence the work reported in this paper.
ACKNOWLEDGEMENT
This publication could not have been made possible without the support of the SG-NAPI award 
supported by the German ministry of education and research, BMBF through UNESCO-TWAS. The 
authors acknowledge the support of Maseno University for providing the resources and environment that 
facilitated this research. Special thanks to the annotators involved in the preparation of the dataset.
REFERENCES
[1]	
P. Agarwal, O. Hawkins, M. Amaxopoulou, N. Dempsey, N. Sastry, and E. Wood, “Hate speech in 
political discourse: A case study of UK MPs on Twitter,” in Proc. 32nd ACM Conf. Hypertext and Social 
Media, 2021, pp. 5–16.
[2]	
J. Armenta-Segura, C. J. Núñez-Prado, G. O. Sidorov, A. Gelbukh, and R. F. Román-Godínez, “Ometeotl@ 
multimodal hate speech event detection 2023: Hate speech and text-image correlation detection in 
real life memes using pre-trained BERT models over text,” in Proc. 6th Workshop on Challenges and 
g  Science database repository https://www.scidb.cn/en/c/j00104
h  DOI number https://doi.org/10.5281/zenodo.14103419

## Page 30

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
848
Applications of Automated Extraction of Socio-political Events from Text, 2023, pp. 53–59. Available: 
https://aclanthology.org/2023.case-1.7.pdf
[3]	
K. Kumari and A. Jamatia, “An approach of hate speech identification on Twitter corpus,” in Int. Conf. 
Frontiers Intell. Comput.: Theory Appl., Singapore: Springer Nature, 2022, pp. 115–125.
[4]	
A. Baruah, F. A. Barbhuiya, and K. Dey, “IIITG-ADBU at HASOC 2019: Automated hate speech and 
offensive content detection in English and code-mixed Hindi text,” in FIRE (Working Notes), 2019, pp. 
229–236.
[5]	
Kenya Law, National Cohesion and Integration Act, Nairobi, Kenya, 2008.
[6]	
T. Mahmud, M. Ptaszynski, J. Eronen, and F. Masui, “Cyberbullying detection for low-resource languages 
and dialects: Review of the state of the art,” Inf. Process. Manage., vol. 60, no. 5, 2023, Art. no. 103454.
[7]	
L. Grimminger and R. Klinger, “Hate towards the political opponent: A Twitter corpus study of the 2020 
US elections on the basis of offensive speech and stance detection,” arXiv preprint, arXiv:2103.01664, 
2021.
[8]	
R. Kapoor et al., “Mind your language: Abuse and offense detection for code-switched languages,” in Proc. 
AAAI Conf. Artif. Intell., vol. 33, no. 1, 2019, pp. 9951–9952.
[9]	
E. Ombui, L. Muchemi, and P. Wagacha, “Hate speech detection in code-switched text messages,” in 
2019 3rd Int. Symp. Multidiscip. Stud. Innov. Technol. (ISMSIT), 2019, pp. 1–6.
[10]	 P. A. Pratama, “Code switching and code mixing in English language learning during online learning in 
COVID-19 outbreak,” J. Pendidik. Bhs. Inggris Undiksha, vol. 10, no. 1, pp. 53–59, 2022.
[11]	 E. Ombui, L. Muchemi, and P. Wagacha, “Building and annotating a code-switched hate speech corpora,” 
Int. J. Inf. Technol. Comput. Sci., vol. 3, pp. 33–52, 2021.
[12]	 V. Marivate et al., “PuoBERTa: Training and evaluation of a curated language model for Setswana,” in 
Southern African Conf. Artif. Intell. Res., Springer, 2023, pp. 253–266.
[13]	 K. Pant and T. Dadu, “Towards code-switched classification exploiting constituent language resources,” 
in Proc. 1st Conf. Asia-Pacific Chapter Assoc. Comput. Linguistics & 10th Int. Joint Conf. Natural Lang. 
Process.: Student Res. Workshop, 2020, pp. 37–43.
[14]	 N. V. Cabasag et al., “Hate speech in Philippine election-related tweets: Automatic detection and 
classification using natural language processing,” Philipp. Comput. J., vol. XIV, no. 1, 2019.
[15]	 J. J. Amores, D. Blanco-Herrero, P. Sánchez-Holgado, and M. Frías-Vázquez, “Detecting ideological 
hatred on Twitter: Development and evaluation of a political ideology hate speech detector in tweets in 
Spanish,” Cuadernos. Info, no. 49, pp. 98–124, 2021.
[16]	 T. Davidson, D. Warmsley, M. Macy, and I. Weber, “Automated hate speech detection and the problem of 
offensive language,” in Proc. Int. AAAI Conf. Web Soc. Media, vol. 11, no. 1, 2017, pp. 512–515.
[17]	 K. Singh, V. Vajrobol, and N. Aggarwal, “IIC_Team@ multimodal hate speech event detection 2023: 
Detection of hate speech and targets using XLM-RoBERTa-base,” in Proc. 6th Workshop Challenges 
Applications Automated Extraction Socio-political Events Text, 2023, pp. 136–143.
[18]	 H. T.-T. Do et al., “Hate speech detection on Vietnamese social media text using the bidirectional-LSTM 
model,” arXiv preprint, arXiv:1911.03648, 2019.
[19]	 C. E. Ilevbare et al., “EkoHate: Offensive and hate speech detection for code-switched political discussions 
on Nigerian Twitter,” in 5th Workshop Afr. Natural Lang. Process., 2024.
[20]	 K. Nowakowski, M. Ptaszynski, F. Masui, and Y. Momouchi, “Improving basic natural language processing 
tools for the Ainu language,” Information, vol. 10, no. 11, p. 329, 2019.
[21]	 C. Amol, L. Wanzare, and J. Obuhuma, “PolitiKweli: A Swahili-English code-switched Twitter political 
misinformation classification dataset,” in Int. Conf. Speech Lang. Technol. Low-Resource Lang., Springer, 
2023, pp. 3–17.

## Page 31

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
849
[22]	 A. Magueresse, V. Carles, and E. Heetderks, “Low-resource languages: A review of past work and future 
challenges,” arXiv preprint, arXiv:2006.07264, 2020.
[23]	 H. C. Dewi, “Code switching used by Indonesian celebrities in social media,” Deiksis, vol. 13, no. 3, pp. 
222–230, 2021.
[24]	 S. Sitaram, K. R. Chandu, S. K. Rallabandi, and A. W. Black, “A survey of code-switched speech and 
language processing,” arXiv preprint, arXiv:1904.00784, 2019.
[25]	 PolitiKweli Misinformation Detection Dataset. [Online]. Available: https://doi.org/10.1007/978–3-031–
58495–4_1. Accessed: Aug. 25, 2024.
[26]	 S. H. Muhammad et al., “SemEval-2023 task 12: Sentiment analysis for African languages (AfriSenti-
SemEval),” arXiv preprint, arXiv:2304.06845, 2023.
[27]	 AfriSenti Dataset. [Online]. Available: https://github.com/afrisenti-semeval/afrisent-semeval-2023. Accessed: 
Aug. 20, 2024.
[28]	 Hate Speech Kenya Dataset. [Online]. Available: https://www.kaggle.com/datasets/edwardombui/hatespeech-
kenya. Accessed: Jul. 6, 2021.
[29]	 B. Masua, “Enhancing text pre-processing for Swahili language: Datasets for common Swahili stop-words, 
slangs and typos with equivalent proper words,” Data Brief, vol. 33, p. 106517, 2020.
[30]	 A. Toktarova et al., “Hate speech detection in social networks using machine learning and deep learning 
methods,” Int. J. Adv. Comput. Sci. Appl., vol. 14, no. 5, 2023.
[31]	 N. O. Onyango, J. Obuhuma, and L. Wanzare, “Zenodo dataset,” Zenodo, 2024. [Online]. Available: 
https://doi.org/10.5281/zenodo.14103420
[32]	 N. O. Onyango, J. Obuhuma, and L. Wanzare, “Science Data Bank dataset,” Sci. Data Bank, 2025. 
[Online]. Available: https://www.scidb.cn/en/c/j00104.
[33]	 B. Sule, I. K. Mika’il, and M. K. Tal, “Youth, proliferation of small arms and light weapons, and conflicts 
in 21st century Africa,” in The Palgrave Handbook of Violence in Africa, Cham: Springer Nature, 2024, pp. 
479–500.

## Page 32

Swahili and Code-Switched English-Swahili Political Hate Speech Detection Textual Dataset  
Data Intelligence
850
AUTHOR BIOGRAPHY
Nelson Odhiambo Onyango is a Master’s student in Computer Science 
at Maseno University, Kenya. He holds a First Class Honours Bachelor of 
Science degree in Computer Science from the same institution. His research 
interests lie in Natural Language Processing (NLP), particularly in low-
resource languages. He has actively contributed to dataset curation efforts 
for African languages, including Swahili and Dholuo.
Dr. Lilian Wanzare is the co-founder of KenCorpus and the Chairperson of 
the Department of Computer Science at Maseno University. She holds a 
Bachelor of Science in Computer Science (University of Nairobi), Master of 
Science in Computer Science (Free University of Bozen-Bolzano), Master of 
Science in Language Technology (Universität des Saarlandes) and Doctor 
of Philosophy in Computational Linguistics (Universität des Saarlandes). 
Dr. Lilian is one of the supervisors for Nelson Odhiambo Onyango and 
skilled in Natural Language Processing, Text mining, Knowledge Extraction, 
Knowledge acquisition, Programming (Python, Java, R) and Machine 
Learning. Her interests and passions lie in Natural Language Processing 
(NLP), Natural Language Understanding (NLU), Data Science, Machine 
Learning, building chatbots and personal assistants.
Dr. James Obuhuma is a Computer Science faculty, Department of 
Computer Science, Maseno University. He holds a PhD in Computer 
Science from Maseno University, an MSc in Computer Science from the 
University of Nairobi and a BSc in Computer Science and Technology 
from Maseno University. His MSc thesis focused on Road Traffic Analysis 
using GPS Technology which opened his interest in Intelligent Systems. 
This heavily influenced his PhD research topic which was in the area of 
Intelligent Transportation Systems (ITS) with a focus on Vehicle Driver 
Behaviour Modeling. His research interest is in the application of Machine 
Learning in different domains, including, ITS, Cybersecurity and IoT. Dr. 
Obuhuma is one of the MSc supervisors for Nelson Odhiambo, whose MSc 
research resulted in this publication. Dr. Obuhuma is also a passionate 
Design Thinking Coach who fosters for Social Innovations across the globe.

```
