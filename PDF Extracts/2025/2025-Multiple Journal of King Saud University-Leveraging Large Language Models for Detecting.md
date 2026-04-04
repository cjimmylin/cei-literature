---
title: "2025-Multiple Journal of King Saud University-Leveraging Large Language Models for Detecting - PDF Extract"
source_pdf: "2025-Multiple Journal of King Saud University-Leveraging Large Language Models for Detecting.pdf"
pages: 23
extracted_at: "2026-04-04T10:22:22.612022"
---

# PDF Extract: 2025-Multiple Journal of King Saud University-Leveraging Large Language Models for Detecting

**Source PDF:** 2025-Multiple Journal of King Saud University-Leveraging Large Language Models for Detecting.pdf
**Total Pages:** 23

---

## Content

```
--- Page 1 ---

Journal of King Saud University Computer and Information Sciences (2025) 37:271
https://doi.org/10.1007/s44443-025-00269-y
ORIGINAL PAPER
Leveraging large language models for detecting and preserving
emotions in quran translations
Arwa Almarzoqi1 · Mohammed Alsuhaibani1
Received: 11 April 2025 / Accepted: 4 September 2025 / Published online: 22 October 2025
© The Author(s) 2025
Abstract
Over the years, translations of the Quran have served as a vital tool for conveying its message to non-Arabic speaking audiences.
This research proposes a computational quantitative approach to investigate emotion preservation in English translations of
the Quran using Large Language Models (LLMs). The proposed approach implements emotion analysis using the state-of-
the-art models and evaluates the agreement levels through a human validation process, using a parallel corpus of the Quran
with seven English translations. This research yields the Emotionally-Labeled Quran Verses (ELQV) dataset, a collection of
2100 Quran verses annotated by specialists, designed to advance Arabic Natural Language Processing (NLP), particularly
NLP-based Quranic research. The analysis demonstrates that the investigated translations preserved the emotional semantics
at a fair level. Compared to the Quran, neither of the translations reached substantial agreement with Arabic readers, with
Cohen’s Kappa (κ) scores ranging from 0.29 to 0.35. Despite the challenges associated with Classical Arabic scripts, the
LLMs adopted in this research proved their ability to capture the emotional semantics of the Quran, indicating their aptitude
to comprehend complex scripts with cultural and theological signiﬁcance.
Keywords Emotion preservation · Emotion analysis · Sentiment analysis · Large language models (LLMs) · Text classiﬁcation
1 Introduction
The pragmatic indication of sentiment (i.e., positive, neg-
ative, or neutral) or emotion (i.e., anger, fear, happiness,
sadness, etc.) is not purely conveyed in translations (Almar-
zoqi and Alsuhaibani 2025). This important element may be
omitted in the translation process of a source texts (Moham-
mad et al. 2016; Barhoumi et al. 2018; Kumari et al. 2021). As
such, preserving the overall traits of the source text during the
translation process is essential, as the translations must accu-
rately convey the syntactic, semantic, and pragmatic aspects
of the source texts. This is particularly crucial with the sacred
scriptures, as even a slight emotional shift can signiﬁcantly
affect their major implications.
Islam is the ﬁnal religion for all humanity, with over two
billion adherents globally1. It has two fundamental sources
B Arwa Almarzoqi
a.almarzoqi@qu.edu.sa
Mohammed Alsuhaibani
m.suhibani@qu.edu.sa
1
Department of Computer Science, College of Computer,
Qassim University, 51452 Buraydah, Saudi Arabia
1 https://worldpopulationreview.com/country-rankings/muslim-
population-by-country
of principles, the Holy Quran and the Hadith. The Quran
has been revealed to the Prophet Mohammed, Peace Be
Upon Him (PBUH), in clear Arabic language. It is consid-
ered the word of Allah and serves as the principal source for
all Islamic tenets. Given the global expansion of Islam into
non-Arabic countries, comprehending the meanings of the
Islamic scriptures is therefore crucial for non-Arabic Mus-
lims. Translations have emerged as the principal means for
non-Arabic Muslims to read, comprehend, and contemplate
the Quran. Therefore, conveying the emotional semantics
in the Quran translations is especially important due to the
sacred signiﬁcance of the Quran.
The examination of emotion preservation involves the
analysis of textual data, which is implicitly associated with
Natural Language Processing (NLP). This includes the appli-
cation of emotion analysis to assess the preservation level
of emotion of the target text after the translation pro-
cess. Recently, the domain of NLP has had a breakthrough
advancement with the development of the Transformer archi-
tecture (Vaswani et al. 2017) that, in turn, contributed to the
creation of Large Language Models (LLMs), like Bidirec-
tional Encoder Representations from Transformers (BERT)
(Devlin et al. 2019), Robustly Optimized BERT Approach
(RoBERTa) (Liu et al. 2019), and Decoding-enhanced BERT
123

--- Page 2 ---

271
Page 2 of 23
Journal of King Saud University Computer and Information Sciences (2025) 37 :271
with Disentangled Attention (DeBERTa) (He et al. 2021),
to name a few. The LLMs are trained on extensive textual
data to acquire contextual word representations, meaning
each word possesses different representations according to
its contextual usage, thereby capturing the different uses of
words across various contexts (Jurafsky and Martin 2025).
This attribute resulted in remarkable performance gains com-
pared to traditional approaches, as these models exhibited
substantial performance capability for nearly all NLP tasks
(Raiaan et al. 2024).
Research into sentiment preservation in translations has
broadened in various directions (Zhang et al. 2017; Lohar
et al. 2017, 2018; Si et al. 2019; Saadany and Orasan
2020; Troiano et al. 2020; Kumari et al. 2021; Saadany
et al. 2022; Banik 2023; Miao et al. 2024). These direc-
tions included traditional models, such as mixed linear
regression (Zhang et al. 2017), both manual and automatic
sentiment classiﬁcation (Lohar et al. 2017), and Bidirectional
Long Short-Term Memory (BiLSTM) (Troiano et al. 2020),
which progressively evolved into state-of-the-art models,
Transformer-based models (Si et al. 2019; Saadany et al.
2022; Miao et al. 2024). Another avenue explored emotion
preservation in translations through annotation projection,
focusing on English and Finnish, French, and Italian lan-
guage pairs (Kajava et al. 2020). In spite of these extensive
scholarly investigations, there is a notable research gap in
the analysis of emotions, particularly within the Arabic
and English language pairs (Saadany and Orasan 2020). To
further clarify this gap, a body of existing research has pre-
dominantly concentrated on English and other languages,
such as German (Zhang et al. 2017; Lohar et al. 2017, 2018;
Troiano et al. 2020), Hindi (Kumari et al. 2021; Banik 2023),
and Chinese (Si et al. 2019). Nevertheless, these studies and
their proposed models may insufﬁciently capture the emo-
tional semantics of Arabic sacred scriptures, particularly the
Quran. This research, therefore, aims to investigate emotion
preservation in Arabic-to-English translations of the Quran,
leveraging emotion analysis and LLMs, extending the ﬁnd-
ings of a previous study focused on sentiment (Gaanoun and
Alsuhaibani 2025). This research introduced several contri-
butions to the domain of Arabic NLP, which can be outlined
as follows:
• Investigating the abilities of LLMs to comprehend the
Arabic sacred scripture, the Quran, and its inherent emo-
tional semantics.
• Offering an analysis of the preserved emotional seman-
tics in seven English translations of the Quran.
• Providing evidence of how the LLMs can capture the
different emotional semantics in certain languages, Ara-
bic and English, particularly with anger, fear, joy, and
sadness classes.
• Establishing a framework for assessing the quality of
emotional translation in the Quran and its English trans-
lations.
• Development of the Emotionally-Labeled Quran Verses
(ELQV), a dataset annotated by experts in the Arabic lin-
guistics and Islamic law, with the objective of enhancing
Arabic NLP and NLP-based Quran studies.
The structure of this research is embodied in nine sec-
tions, including this introductory one. It is organized in the
following manner: Section 2 deﬁnes the research questions
and objectives, and Section 3 reviews the existing research on
sentiment preservation. Section 4 explains the methodologi-
cal design of this research, whereas Section 5 describes the
experimental design. Section 6 then outlines the results, suc-
ceeded by a discussion in Section 7 and a qualitative analysis
in Section 8. Section 9 lastly concludes the research.
2 Research questions and objectives
The central question that this research seeks to answer is:
“Do the non-Arabic Muslims who read English translations
of the Quran perceive the same emotions as the original Ara-
bic readers?” In addition, this research seeks to address the
following questions:
1. To what degree do English translations of the Quran
convey the emotions experienced by the original Arabic
reader?
2. TowhatextentcanLLMsaccuratelycapturetheemotions
conveyed in sacred scriptures, speciﬁcally the Quran?
3. What is the variation in emotion preservation levels
among English translations of the Quran?
Based on the given research questions, this research aims to
achieve the following objectives:
1. To examine the emotion preservation in English transla-
tions of the Quran using LLMs.
2. To investigate the potential of LLMs in capturing the
emotions conveyed in the Quran and its English transla-
tions.
3. To develop a framework for assessing the quality of
emotional translation in the Quran and its English trans-
lations, adjusted for LLMs.
123

--- Page 3 ---

Journal of King Saud University Computer and Information Sciences (2025) 37 :271
Page 3 of 23
271
3 Literature review
Studies on the utilization of the translation process in NLP
applications have demonstrated its impact on sentiment
polarity (Aﬂi et al. 2017). This impact on sentiment polar-
ity led to an alteration of the original sentiment class of the
source text (Gangula and Mamidi 2018; Poncelas et al. 2020;
Qian et al. 2023). The extent of alteration was assessed by the
drop in the accuracy of sentiment analysis models (Moham-
mad et al. 2016; Barhoumi et al. 2018; Poncelas et al. 2020;
Sazzed 2020). Despite signiﬁcant ﬂaws in maintaining sen-
timent polarity during translation, some sentiment analysis
models can, however, derive sentiment information from the
translations (Mohammad et al. 2016; Barhoumi et al. 2018;
Poncelas et al. 2020; Saadany et al. 2023). Nevertheless, the
translation processes must ensure that the knowledge con-
tained in the source text, including the emotional traits, is
accurately conveyed to the target text. As many translations
often fail to maintain sentiment information from the source
text (Kumari and Ekbal 2024), several studies addressed this
concern, proposing different methodologies (Zhang et al.
2017; Lohar et al. 2017, 2018; Si et al. 2019; Saadany
and Orasan 2020; Troiano et al. 2020; Kumari et al. 2021;
Saadany et al. 2022; Banik 2023; Gaanoun and Alsuhaibani
2025).
Zhang et al. (2017) investigated whether translation, either
manual or automatic, preserves the sentiment of the original
text. Research results indicated that there was no statistically
signiﬁcant difference in sentiment between an English gold
standard corpus and human translations. Therefore, human
translation can preserve the sentiment class of the original
texts, while machine translation systems tend to lose or mis-
represent sentiment.
To address the premise that machine translation systems
fail to preserve the sentiment of the original text, Lohar et al.
(2017) developed three sentiment-speciﬁc models to trans-
late textual data associated with a speciﬁc sentiment class,
including positive, neutral, or negative. The models inte-
grated sentiment classiﬁcation with the machine translation
system to produce the translations. The ﬁndings showed that
this integration effectively preserved sentiment information.
Lohar et al. (2018) built upon their prior research by
introducing an approach termed nearest sentiment class to
enhance the sentiment-speciﬁc machine translation mod-
els. The proposed approach entailed including training data
from the nearest sentiment class during the training process.
The nearest sentiment class approach, using the sentiment-
speciﬁc models, attained the highest sentiment preservation
score of 60.33% while ensuring a balance between the quality
of translation and the preservation of sentiment.
By the same token, Si et al. (2019) enhanced the ability of
neural machine translation systems to maintain the sentiment
in the produced translations. They introduced a sentiment-
aware neural machine translation system that incorporates
a neural machine translation model with a sentiment anal-
ysis model to produce sentiment-aware translations. The
researchers reported that including contextual information
in neural machine translation systems enhanced the transla-
tion of subtle contextual traits. They concluded that neural
machine translation systems can maintain the sentiment con-
veyed in the source texts.
SaadanyandOrasan(2020)developedsentiment-sensitive
neural machine translation systems that handle sentiment
polarity.Theresearchersincludedsentimentinformationdur-
ing the encoding phase and then ﬁne-tuned neural machine
translation models based on sentiment polarity. The results
showed that sentiment-sensitive neural machine translation
models can rectify sentiment errors in online translation of
Arabic User-generated Content (UGC).
Similarly,Troianoetal.(2020)examinedemotionpreservation
in neural machine translation systems. The study presented
an emotion-driven translation candidate re-ranking proce-
dure as a post-processing phase for the translations produced
by neural machine translation systems. The re-ranking pro-
cedure utilizes an emotion classiﬁcation model that lever-
ages probabilistic outputs to select a candidate translation
that aligns closely with the emotional traits of the source
emotion. The results showed that the proposed procedure
enhanced emotion preservation without compromising trans-
lation accuracy.
In an in-depth investigation, Kumari et al. (2021) intro-
duced a reinforcement learning-based framework to examine
sentiment preservation in review translations. The proposed
approach used an actor-critic approach with a novel harmonic
reward module to ﬁne-tune a neural machine translation
model to generate sentimentally and semantically preserved
translations. The research revealed that the proposed method,
with the novel harmonic reward, preserved the overall traits
of the original text during the translation process.
Saadany et al. (2022) presented a semi-supervised neu-
ral machine translation model to improve the translation of
sentiment in dialectical Arabic UGC. The proposed model
was developed by training a Transformer model to translate
dialectical Arabic into English. The evaluation of sentiment
preservation showed that the semi-supervised machine trans-
lation system preserved the sentiment effectively.
Banik (2023) proposed a statistical machine translation
model that generates sentiment-based translations. The pro-
posedmodelcombinesasentimentmodelintoaphrase-based
statistical machine translation model by incorporating sen-
timent scores in the phrase table. Thus, the proposed model
prioritizes phrases exhibiting a slight difference in sentiment
score between the source phrase and the target phrase. The
researcher demonstrated that the sentiment-phrase-based
model preserved the sentiment successfully.
123

--- Page 4 ---

271
Page 4 of 23
Journal of King Saud University Computer and Information Sciences (2025) 37 :271
In a seminal work to preserve the sentiment of the
Quran, which is the closest study for this research, is the
study conducted by Gaanoun and Alsuhaibani (2025). The
study, particularly, investigated sentiment preservation in
the English translations of the Quran using Transformer
Language Models (TLMs) alongside a human validation
approach. The researchers used the TLMs to predict the
sentiment class for each verse of the Quran and its asso-
ciated translations. These predictions were then validated by
humans, as this approach enabled the researchers to assess
the agreement levels between the Quran and the translations
about sentiment.
Considering the above-mentioned literature, most studies
have focused on sentiment preservation in translations rather
than on emotion. This gap is particularly noteworthy because
sentiment addresses the overall polarity, whereas emotion
explores the subtleties conveyed in the scripts, providing a
detailed analysis. Additionally, a signiﬁcant number of stud-
ies were centered on investigating the preservation level of
the translations produced by machine translation systems,
speciﬁcally in the context of UGC. These gaps are partic-
ularly signiﬁcant considering the contextual nature of the
Islamic scripts, where little shifts in tone or meaning can
lead to substantial differences in interpretation.
Furthermore, although the scholarly investigation into senti-
ment preservation expanded in various directions, merely a
single study, the closest work to our proposed approach, has
investigated sentiment preservation in English translations
of the Quran (Gaanoun and Alsuhaibani 2025). One of the
pronounced gaps in this study is the dominance of the neutral
sentiment class in their Quranic dataset. Statistically, the neu-
tral class constituted between 58% and 74%, which served
as the primary impetus for this research. Further, despite the
commendable human veriﬁcation approach, its focus on a
non-expert population of Arabic readers could potentially
lead to incomplete understanding of the sentiment embed-
ded in the Quran verses, resulting in the above-mentioned
issue, the dominance of the neutral class. Additional gap is
that the study focused primarily on the CAMeLBERT models
(Inoue et al. 2021), which did not utilize pre-segmentation,
lightweight, or disentangled attention techniques during the
training process. CAMeLBERT models, while promising,
are tailored for sentiment analysis, raising questions about
their applicability in capturing subtleties in Arabic emotion
analysis. Last gap is that the study lacks an assessment of
the concordance between the predictions of the TLMs and
those of the annotators, which this research seeks to address.
Therefore, this research aims to bridge the above-mentioned
gaps by investigating emotion preservation in English trans-
lations of the Quran using LLMs. In particular, the research
seeks to enhance the human veriﬁcation approach and expand
the array of the models to examine the efﬁcacy of different
models trained using multiple methodologies and architec-
tures.
4 Methodology
To successfully achieve the primary objectives of this
research, we utilize diverse methodological strategies. The
proposed methodology includes two fundamental modules:
emotion analysis and emotion agreement evaluation, as illus-
trated in Fig. 1.
The primary objective of the methodology is to identify
the emotional class for each verse of the Quran and its cor-
Fig. 1 High-level overview of the proposed methodology
123

--- Page 5 ---

Journal of King Saud University Computer and Information Sciences (2025) 37 :271
Page 5 of 23
271
responding English translations. Following that, it seeks to
evaluate the extent to which the English translations of the
Quran preserve the original emotional essence by statistical
metrics. As mentioned earlier, this objective will be achieved
through two primary modules, namely the emotion analysis
module and the emotion agreement evaluation module.
The emotion analysis module involves a two-step process
that integrates the functionalities of advanced approaches,
speciﬁcally LLMs, with human proﬁciency. It involves two
major stages, namely the emotion prediction and emotion
veriﬁcation. The emotion prediction stage involves using a
collection of LLMs to identify the emotional class for each
verse of the Quran and its corresponding English translations.
The emotional classes employed in this research consist of
four class labels: anger, fear, joy, and sadness. To predict the
emotional class, the LLMs underwent ﬁne-tuning, the speci-
ﬁcations of the ﬁne-tuning settings provided in Appendix A,
which includes adding a fully connected linear layer on
top of a pre-trained model. Consequently, the LLMs were
employed exclusively for the task of emotion analysis using
the above-mentioned emotional classes. As for the emotion
veriﬁcation stage, it entails sampling the automatic emotion
annotations generated by the LLMs and annotating and val-
idating them by specialist human annotators. This two-step
process enables a comprehensive understanding of emotional
consistency between the Quran and the English translations.
The emotion agreement evaluation module seeks to eval-
uate the compatibility of emotional classiﬁcations between
the verses of the Quran and their associated English transla-
tions. To achieve that, this module utilizes certain statistical
techniques, namely the inter-rater reliability measures, to
quantify the level of agreement between the emotion class
assigned to each verse and its respective English translations.
Thismoduleprimarilydemonstratestheextenttowhichemo-
tional semantics is preserved in English translations of the
Quran following the translation process.
5 Experiment
This section describes the experimental settings employed
for training and analysis. It is structured as follows: Sec-
tion 5.1 commences with a description of the experimental
setup. Section 5.2 then provides a thorough explanation of the
parallel corpus utilized for the analysis. Section 5.3 clariﬁes
the emotion analysis process.
5.1 Experimental setup
For the experimental setup, we utilized Google Colab2, a
hosted Jupyter Notebook service that demands no setup and
offers complimentary access to computational resources.
2 https://colab.google/
All experiments were conducted using the Colab Pro+
version with GPUs and using the Hugging Face Transform-
ers library3. The experimental conﬁguration comprised an
NVIDIA A100-SXM4-40GB GPU utilizing CUDA version
12.2 and a 10-core Apple M2 GPU with 8GB of RAM to
guarantee efﬁcient and reliable execution.
5.2 Data
This research primarily investigates whether English trans-
lations preserve the emotional essence of the Quran. To
this end, we used a high-quality parallel corpus, compiled
via web scraping, that integrates all 6236 Quran verses
together with seven different English translations (Gaanoun
and Alsuhaibani 2025). A detailed description of the included
English translations is highlighted below, accompanied by a
sample from the dataset in Table 1.
• The Koran Interpreted. It is an English translation of
the Holy Quran, published in 1955 by Arberry (1996).
The author is a non-Muslim British academic interested
in Arabic literature, Persian studies, and Islamic studies.
Despite being non-Muslim, he agreed with the Islamic
perspective that the Quran cannot be translated but can
only be interpreted. This translation is among the most
notable produced by a non-Muslim expert.
• The Holy Quran, The Arabic Text and English Trans-
lation. This translation was published in 1981 by scholar
Muhammad (Sarwar 1981). He is a Muslim who con-
tributed to the translation of the meanings of the Quran
from Arabic to English, resulting in this Shi’a translation.
• Interpretation of the Meanings of the Noble Quran.
This translation has been written by Al-Hilali and Khan
(1998), where both are Islamic scholars who interpreted
the meaning of the Quran according to their under-
standing. This translation has received approval from the
University of Medina and the Saudi Dar al-Ifta. It was
published in 1998 and printed at the King Fahd Complex
for the Printing of the Holy Quran in Madinah, Saudi
Arabia. This translation is the most extensively circulated
translation in most of the English-speaking globe.
• The Meaning of the Glorious Koran. It is an English
translation of the Quran, along with a brief introduction
to the chapters (surahs), released in 1930 by Muham-
mad Marmaduke Pickthall (1953). He is a British Muslim
who embraced Islam in 1917 and was an English Islamic
scholarinterestedinreligiousaffairs.Thistranslationwas
the ﬁrst translation by a Muslim whose native language
is English and continues to be among the most popular
translations.
3 https://huggingface.co/
123

--- Page 6 ---

271
Page 6 of 23
Journal of King Saud University Computer and Information Sciences (2025) 37 :271
Table 1 Sample of the data
Sourah_number
1
26
31
Verse_number
6
195
3
VerseDiac
Verse
Sourah_Ar
Sourah_En
l-fatihah
l-shu’ara
luq’man
Sahih_int
Guide us to the straight
path
In a clear Arabic lan-
guage
As guidance and mercy
for the doers of good
Pickthall
Show
us
the
straight
path
In plain Arabic speech
A guidance and a mercy
for the good
YA
Show
us
the
straight
way
In the perspicuous Ara-
bic tongue
A Guide and a Mercy to
the Doers of Good
Shakir
Keep us on the right
path
In
plain
Arabic
lan-
guage
A guidance and a mercy
for the doers of good-
ness
MS
(Lord), guide us to the
right path
It has been revealed in
plain Arabic
A guidance and mercy
for the righteous
MK
Guide us to the Straight
Way
In the plain Arabic lan-
guage
A guide and a mercy for
the Muhsinun (gooddo-
ers)
Arberry
Guide us in the straight
path
In
a
clear,
Arabic
tongue
For a guidance and a
mercy to the good-doers
• The Holy Quran (Saheeh International). Three Ameri-
canMuslimwomentranslatedtheQuranincontemporary
language translation (International 1997). They metic-
ulously used English terminology that is contextually
appropriate for the Quran; for instance, they utilize Allah
rather than God.
• The Quran. The provenance of this translation remains
uncertain. The translation, initially published by Shakir
(1999) in 1968, is predominantly attributed to him, while
the initial author is purported to be Mohammed Ali Habib
Shakir, the son of Habib Esmail. This translation is one
of the most widely recognized Quran translations among
Shi’a Muslims.
• TheHolyQuran,Text,Translation,andCommentary.
This translation was initially published in 1934 by Abdul-
lah Yusuf Ali (2001), who is a British Indian Muslim
scholar. This translation is notable for its clear explana-
tions through the extensive use of footnotes. It received
ﬁnancial support from Saudi Arabian benefactors in the
late twentieth century. These attributes have made it one
ofthemostwell-knownEnglishtranslationsoftheQuran.
This parallel corpus constitutes the foundational material
to fulﬁll the primary objective of this research. It facilitates
a systematic investigation of the heterogeneity in emotional
preservation in the English translations of the Quran.
5.3 Emotion analysis
This section provides a detailed explanation of emotion anal-
ysis. It begins with Section 5.3.1, which outlines the adopted
models. Section 5.3.2 then describes the emotion veriﬁcation
process, followed by an explanation of the evaluation metrics
in Section 5.3.3.
5.3.1 Models
This research employs multiple pre-trained Transformer-
based models for the emotion analysis. Given the nature
of the Quran, we have prioritized Arabic LLMs trained in
Classical Arabic, followed by those trained in Modern Stan-
dardArabic(MSA),totalingfourteenmodels.Thedecisionto
select fourteen models was based on practical considerations.
The resource limitations required the selection of models
that optimize performance and practicality. Additionally, the
selected models were publicly available, allowing us to take
advantage of their pre-training for utilization in the proposed
framework. These considerations collectively informed the
selection of fourteen models, ensuring a thorough yet prac-
tical evaluation within our resource limitations.
Considering that English is a high-resource language, the
English LLMs employed in this research are fewer than the
Arabic models. Table 2 presents the models utilized in this
123

--- Page 7 ---

Journal of King Saud University Computer and Information Sciences (2025) 37 :271
Page 7 of 23
271
research. It details the language of models, their names, and
their architectural characteristics, including the number of
hidden layers, hidden size, and the parameters.
The Arabic models used in this research share several
commonalities. The majority of them built upon the same
model type, BERT. This is based on a study that demon-
strated that BERT-based models achieved good outcomes in
Arabic emotion analysis (Al-Twairesh 2021). Most of these
models are of the base version, featuring 12 hidden layers
and a hidden size of 768, while two of them are of the BERT
large type, comprising 24 hidden layers and a hidden size of
1024. Here is a detailed explanation of the Arabic models:
• CAMeLBERT models. A collection of BERT base mod-
els pre-trained on Arabic texts was proposed by Inoue
et al. (2021). CAMeLBERT models vary in training
sizes and the form of Arabic. CAMeLBERT-CA was
trained on Classical Arabic texts obtained from various
sources, totaling 6GB in size. CAMeLBERT-MIX was
trained on Classical Arabic, MSA, and dialectal Arabic
texts using multiple corpora, comprising 167GB in size.
CAMeLBERT-MSAwastrainedonacorpusofMSAtex-
tual data with a size of 107GB. All formerly described
models of CAMeLBERT possess the same parameter
count of 110M.
• MARBERT and ARBERT models. A set of Arabic
BERT base models was introduced by Abdul-Mageed
et al. (2021). MARBERT and ARBERT vary in the
type and size of training data. MARBERT concentrated
on both MSA and dialectal Arabic and was trained on
128GB of textual data. On the other hand, ARBERT
focused exclusively on MSA and had been trained on
61GB of textual data. The models were then enhanced
withfurthertextualmaterial,resultinginthedevelopment
of a second version, MARBERTv2 and ARBERTv2. We
experimented with all the versions of MARBERT and
ARBERT, each with 163M parameters.
• QARiB model. An Arabic model built upon the base
version of BERT, introduced by Abdelali et al. (2021).
The model was trained on 600M of textual data, gath-
ered from news articles and tweets. The QARiB model
contains 135M parameters.
• ArabicBERT models. A set of BERT-based versions
presented by Safaya et al. (2020) for Arabic. We only
experimented with two versions, the base and large ver-
sions, that weretrainedon95GBof texts sourcedfromthe
Arabic version of the Open Super-large Crawled Aggre-
gated coRpus (OSCAR) and Wikipedia. The base version
consists of 110M parameters, whereas the large version
contains 336M parameters.
• AraBERT models. A collection of BERT-based Ara-
bic models introduced by Antoun et al. (2020), with
several versions. We only experimented with a single ver-
sion, AraBERTv2, which was trained on 77GB of texts.
AraBERTv2 is differentiated from the other versions by
Table 2 Adopted LLMs
Language
Model
HL
HS
Parameters
Arabic
CAMeLBERT-CA Inoue et al. (2021)
12
768
110M
CAMeLBERT-MIX Inoue et al. (2021)
CAMeLBERT-MSA Inoue et al. (2021)
MARBERT Abdul-Mageed et al. (2021)
163M
MARBERTv2 Elmadany et al. (2023)
MARBERT-Sentimenta
ARBERT Abdul-Mageed et al. (2021)
ARBERTv2 Elmadany et al. (2023)
QARiB Abdelali et al. (2021)
135M
ArabicBERT base Safaya et al. (2020)
110M
AraBERTv2 base Antoun et al. (2020)
135M
Arabic ALBERT Safaya (2020)
11M
ArabicBERT large Safaya et al. (2020)
24
1024
336M
AraBERTv2 large Antoun et al. (2020)
371M
English
XLM-RoBERTa Conneau et al. (2020)
12
768
278M
BERT Devlin et al. (2019)
110M
ALBERT Lan et al. (2019)
11M
DistilBERT Sanh et al. (2019)
6
66M
DeBERTa He et al. (2021)
24
1024
405M
HL:
Hidden
Layers;
HS:
Hidden
Size
ahttps://huggingface.co/Ammar-alhaj-ali/arabic-MARBERT-sentiment
123

--- Page 8 ---

271
Page 8 of 23
Journal of King Saud University Computer and Information Sciences (2025) 37 :271
using a pre-segmentation approach on the textual data.
The base version contains 135M parameters, whereas the
large version comprises 371M parameters.
• Arabic ALBERT. A collection of ALBERT-based mod-
els introduced by Safaya (2020) for Arabic. It includes
several versions: base, large, and x-large, which differ
based on the number of parameters. We conducted exper-
iments only with one version, the base, which had been
trained on 4.4B words collected from the Arabic version
of the OSCAR and Wikipedia. The Arabic ALBERT base
version contains 11M parameters.
As for the English models, the majority of them were
constructedusingthebaseversion, but onewas built usingthe
largeversion. Themodels differ inthequantityof parameters,
spanning from 11M to 405M. Below is a detailed explanation
of each model:
• XLM-RoBERTa model. It is a multilingual version of
the RoBERTa base model introduced by Conneau et al.
(2020). We exclusively used the base version, which was
pre-trained on 2.5TB of textual material obtained from
the Common Crawl dataset that covers 100 languages.
The XLM-RoBERTa model consists of 278M parame-
ters.
• BERT model. A collection of BERT-based models intro-
duced by Devlin et al. (2019) for the English language. It
includes several versions that differ based on the number
of parameters. We use only the base version, which was
trained using the BooksCorpus datasets and the English
Wikipedia. The BERT base model consists of 110M
parameters.
• ALBERT model. A compilation of ALBERT-based
models introduced by Lan et al. (2019) for the English
language. It comprises two main versions, version one
and version two; each version contains multiple models
that vary based on the number of parameters. We use only
one version, the second version, using the base model that
had been pre-trained on a corpus of unpublished books
and English Wikipedia. The ALBERT base version con-
tains 11M parameters.
• DistilBERT model. A distilled version of the BERT
model tailored for the English language was introduced
by Sanh et al. (2019). The model was pre-trained in a
manner analogous to the BERT model. Yet, it features
a reduced number of hidden layers, decreasing from 12
in BERT base to 6, which yields a lightweight model
comprising approximately 66M parameters.
• DeBERTa model. A set of DeBERTa-based models
presented by He et al. (2021) for the English lan-
guage. It improves the BERT and RoBERTa models
with the implementation of disentangled attention and
an enhanced mask decoder. The DeBERTa comprises
multiple versions that vary in terms of the number of
parameters. We use the large version, which was pre-
trained on 80GB of textual data and consists of 405M
parameters.
The aforementioned LLMs were used to classify each
verse of the Quran and its associated English translations
into either anger, fear, joy, or sadness. Thus, all the verses
were assigned a predicted emotion class coupled with a pre-
diction score. These predictions undergo further evaluation
in a subsequent step, known as the emotion veriﬁcation pro-
cess, that will be detailed in the following section.
5.3.2 Emotion veriﬁcation process
This section details the process for emotion veriﬁcation of the
predictions assigned to each verse of the Quran and its corre-
sponding English translations through ensemble approaches,
organized into two subsequent sections.
Arabic validation process Human annotation and veriﬁca-
tion techniques, guided by a Quran expert, validate the
emotion predictions of the Arabic LLMs. This procedure
entails distributing a sample of Quranic verses to annotators
for annotation and veriﬁcation, as illustrated in Algorithm 1.
The subsequent sections comprehensively describe the anno-
tation and veriﬁcation process, including the scheme, dataset,
and procedure.
Annotation and veriﬁcation scheme Emotions have been
classiﬁed into several models that analyze human emotions
from different perspectives. The emotion models are struc-
tured frameworks that classify different human emotions
based on speciﬁc classiﬁcations or dimensions (Sailunaz and
Alhajj 2019). They are divided into two major classiﬁcations:
dimensional models and categorical models (Saffar et al.
2023), both of which are utilized in NLP research (Nand-
wani and Verma 2021). The annotation scheme established
four categorical emotions, derived from a recognized psy-
chological paradigm. Here is the list of emotions, including
the original Arabic terms in parentheses alongside their cor-
responding English translations:
• Anger
.
• Fear
.
• Joy
.
• Sadness
.
The rationale behind selecting these emotion classes is
quite justiﬁable for three reasons. First, we considered the
holiness of Quranic scripture during the selection of emotion
categories. Second, the chosen emotion classes are derived
123

--- Page 9 ---

Journal of King Saud University Computer and Information Sciences (2025) 37 :271
Page 9 of 23
271
from the Ekman emotional model (Ekman 1992), which
is commonly used in NLP research to identify emotions
in textual data (Saffar et al. 2023; Tafreshi et al. 2024).
Third, this model is frequently employed in most annotation
schemes (Plaza-del-Arco et al. 2024). Given these grounds,
the deﬁnitive annotation scheme for emotions comprises the
previously mentioned four categories.
Annotation and veriﬁcation dataset The construction of a
dataset is a fundamental step for the annotation and veri-
ﬁcation. To compile a comprehensive dataset suitable for
emotion annotation, a meticulous verse selection process was
conducted to ensure diversity and class relevance. The initial
step to construct the dataset is the compilation of instances
through the verse selection process. This was carried out by a
Quranic expert who oversaw the overall annotation and ver-
iﬁcation procedure. The verse selection process is grounded
in multiple scientiﬁc principles. Initially, it started with a
review of the classiﬁcations of the Quran verses and their
main concepts, using several trustworthy scientiﬁc sources
that address the objective interpretation of the Holy Quran.
Accordingly, several Quran verses were selected based on
their overall exegesis (tafseer) from tafseer as-Sa’di4. The
selected verses are then evaluated according to an established
scientiﬁc classiﬁcation, accomplished by referring to the
Encyclopedia of Thematic Interpretation of Quranic Stud-
ies5, the ﬁrst peer-reviewed scientiﬁc encyclopedia to study
the topics of the Holy Quran. The verses are also assessed
based on the following inclusion and exclusion criteria:
Inclusion criteria
• The verse is imbued with emotion, according to the
expert analysis.
• The verse is categorized in accordance with the sci-
entiﬁc classiﬁcations presented in the Encyclopedia.
• The verse can be categorized within one of the clas-
siﬁcations of our scheme (i.e., anger, fear, joy, or
sadness).
Exclusion criteria:
• The verse lacks emotional depth, according to the
expert opinion.
• The verse is not categorized within the scientiﬁc clas-
siﬁcations of the Encyclopedia.
• Theverseiscategorizedasmixed,ambiguous,orneu-
tral.
The inclusion and exclusion criteria guided the verse
selection process, assessed by a Quran expert, culminating in
4 https://shamela.ws/book/42
5 https://modoee.com/
theselectionof2100versesincludingdiversethemesrelevant
to human existence for human veriﬁcation and annotation.
Annotation and veriﬁcation process The human annotation
and veriﬁcation phase constitutes a key component of the
proposed methodology. The selected Quran verses, the con-
structed dataset, have been annotated by specialists, all of
whom possess PhDs in either Arabic linguistics or Islamic
law (i.e., Hadith, the Holy Quran, and its associated sci-
ences). The selected verses constitute approximately 34% of
the verses of the Quran and have been distributed to the anno-
tators via Google Forms. Each form consists of 300 verses
organized into several sets of forms for validation. The verses
are written without referencing the chapter (surah) name to
reduce potential bias in the annotator. The annotators were
familiarized with the annotation guidelines by a Quran expert
over multiple training sessions. The guidelines provided to
the annotators include several essential elements to guarantee
clarity and consistency during the annotation and veriﬁca-
tion process. The Quran expert explained the objectives of
the annotation process to guide the annotators regarding
the intended results. Additionally, the deﬁnition for each
class label was comprehensively deﬁned to the annotators
to eliminate any doubt. Throughout the annotation process,
the annotators possessed the annotation guidelines document
that included the annotation objectives, scheme description,
the deﬁnitions of the emotion classes, and a set of represen-
tative examples. Table 3 presents a selection of exemplary
instances that guided the annotation process; the ﬁrst line
contains the Arabic Quran verses, whereas the second line
provides their English translation. The verses are annotated
with the respective emotion class in the ﬁrst column.
In addition, the annotators were instructed to assign emo-
tions, as deﬁned in our scheme (i.e., anger, fear, joy, or
sadness), for each verse of the Quran to determine their
impression or the emotion acquired when reading a particular
verse, informed by the following deﬁnitions of the emotional
classes:
• Anger. These are the verses that detail the actions and
behaviors that displease Allah and lead to His wrath and
punishment. This category includes verses that mention
theactionsortypesofdisbelieverswhoincurredthewrath
of Allah as they rejected the truth and arrogantly turned
away from it.
• Fear. These are the verses that encompass the themes
of fear and awe of Allah’s majesty. They contain warn-
ings and descriptions of the punishment for those who
arrogantly reject the truth in this worldly life, as well as
verses that describe the torment of Jahannam (Hell) for
those who are wretched. These verses also serve to instill
fear and reverence for Allah.
123

--- Page 10 ---

271
Page 10 of 23
Journal of King Saud University Computer and Information Sciences (2025) 37 :271
Table 3 Exemplary instances for the annotation process
Emotion Class
Verses
Anger
Say, (O Muhammad SAW to the polytheists, etc.):
“Do you order me to worship other than Allah, O you
fools?”
Can We ignore sending you the Quran just because you
are a transgressing people?
Who set up another ilah (god) with Allah, then (both
of you) cast him in the severe torment.
Fear
So, when the sight shall be dazed.
Do they not then think deeply in the Quran, or are
their hearts locked up (from understanding it)?
And whosoever strives, he strives only for himself.
Verily, Allah is free of all wants from the ’Alamin
(mankind, jinns, and all that exists).
Joy
Then what do you think about the Lord of the ’Alamin
(mankind, jinns, and all that exists)?
And in the heaven is your provision, and that which
you are promised.
Verily! The Muttaqun (pious—see V.2:2) will be in
place of Security (Paradise).
Sadness
Indeed, We know that your breast is straitened at what
they say.
And my breast straitens, and my tongue expresses not
well. So send for Harun (Aaron) (to come along with
me).
And the Messenger (Muhammad SAW) will say, “O
my Lord! Verily, my people deserted this Quran (nei-
ther listened to it, nor acted on its laws and orders)”.
123

--- Page 11 ---

Journal of King Saud University Computer and Information Sciences (2025) 37 :271
Page 11 of 23
271
2100
Verses for validation
115
Verses for validation
Disagreement verses subdivision for annotators
Verses subdivision for annotators
Fig. 2 Human annotation and validation process
• Joy. These are the verses that encompass the themes of
joy, bliss, and happiness. This includes verses of mercy,
descriptions of Jannah (Paradise), and the joys that await
its dwellers (i.e., those who have done righteous good
deeds). These verses bring comfort, hope, and reas-
surance to believers, ﬁlling their hearts and souls with
happiness and tranquility.
• Sadness. These are verses that encompass sorrow, includ-
ing verses about trials, hardships, and tribulations faced
by the prophets and the believers from previous nations, as
well as all verses that evoke sadness and grief in the heart.
The annotation and veriﬁcation process adopts a two-
phasehumanvalidationtechniquetoguaranteeahigh-quality
annotation and veriﬁcation procedure, as illustrated in Fig. 2.
This methodology comprises two principal phases, which
will be explained in the parts that follow.
First Phase.
• The 2100 verses were divided into seven sets, each
containing 300 verses.
• Each set was assigned to three annotators for a total
of 21.
• At the stage of class label assignments, when the
annotatorsexhibitedcompleteagreementontheverse
classiﬁcation, the corresponding emotion class was
assigned. In instances of partial agreement among
annotators, the emotion class was established through
majority voting among the three annotators.
The ﬁrst phase was completed with 1050 verses demon-
strating complete agreement in the emotional class labels
and 935 verses exhibiting partial agreements, totaling 1985
verses, which constitutes 94.52% of the dataset. The remain-
ing 115 verses exhibited discrepancies in the emotional class
labels among the three annotators; hence, these verses pro-
ceeded to the second phase.
Second Phase.
In this phase, 115 verses, approximately 5.48% were
assigned to three additional annotators.
• The verses were divided into three sets, each contain-
ing 38 verses, and one set consisted of 39 verses.
• The emotional class labels were determined through
majority voting by all annotators in the ﬁrst and sec-
ond phases.
This meticulous, expert-driven annotation and veriﬁcation
approach yielded a contribution derived from this research.
We introduced a publicly accessible dataset, the ELQV6,
featuring 2100 instances of systematically curated Quran
verses annotated by experts holding PhDs in Arabic linguis-
tics or Islamic law. The ELQV dataset seeks to contribute
to the ﬁeld of Arabic NLP, particularly in emotion analysis,
which presently faces a scarcity of annotated data in Clas-
6 https://github.com/Arwaalmrzoqi/ELQV
123

--- Page 12 ---

271
Page 12 of 23
Journal of King Saud University Computer and Information Sciences (2025) 37 :271
sical Arabic, by supporting various research directions in
emotion-based Quranic studies.
English validation process The emotion predictions of the
English models for the Quran translations are validated by
ensemble methodologies, as illustrated in Algorithm 2. In the
initial instance, wevalidatedthetranslations throughamajor-
ity vote of the LLMs. In the absence of a label in majority
voting, we assign the label with the highest average predic-
tion score.
5.3.3 Evaluation measures
The evaluation metrics are essential indicators used to assess
the results of the analysis. This research utilizes various
inter-rater reliability metrics to quantitatively assess the con-
cordance of several raters.
1. Cohen’s Kappa (κ). Cohen’s Kappa (κ) (Landis and
Koch 1977) is a statistical metric employed to assess
inter-rater reliability between two raters or annotators
about nominal data (Litvinenko 2021). Cohen’s Kappa
is the most well-known chance-corrected metric (Moons
and Vandervieren 2023). This indicates that this metric
considers the probability of agreement among anno-
tators occurring by random chance. The κ coefﬁcient
accounts for the difﬁculty of the classiﬁcation problem
by integrating the element of random chance (Moons and
Vandervieren 2023). The κ coefﬁcient is computed using
the following formula:
κ = Po −Pe
1 −Pe
(1)
where:
Po denotes the observed agreement among annotators,
Pe denotes the expected agreement by chance.
In particular, the Po signiﬁes the ratio of instances
where both raters agree. It is calculated by dividing the
frequency of agreement among raters by the total num-
ber of rated instances. Whereas Pe represents the ratio
of instances where agreement is expected to occur by
chance. It is calculated based on the marginal probabili-
ties associated with each category selected by the raters.
The κ coefﬁcient scores range between -1 and 1, with κ
= 1 signifying full agreement, whereas κ = 0 indicates
an agreement comparable to that expected by random
chance. Landis and Koch (1977) introduced an interpre-
tive scale for κ score, shown in Table 4.
2. Fleiss Kappa (κ). Fleiss Kappa (κ) (Fleiss 1971) was
established to broaden the concept of agreement mea-
Table 4 Interpretive scale of κ scores (Landis and Koch 1977)
Kappa κ
Level of Agreement
<0
Poor
0.00-0.20
Slight
0.21-0.40
Fair
0.41-0.60
Moderate
0.61-0.80
Substantial
0.81-1.00
Almost Perfect
surement to include more than two raters or annotators
for nominal variables. It assesses dependability by con-
sidering both the consistency of the evaluators and the
degree to which their concordance exceeds what would
be expected by chance. According to Eq. (1), Fleiss
Kappa κ describes Po and Pe in distinct manners detailed
below.
Assume I denotes the total number of instances, R
denotes the ﬁxed total number of raters, and C denotes
the total number of classes. The quantity of raters who
classiﬁed the ith instance into the cth class is represented
by xir. Since the classes are mutually exclusive, it fol-
lows that each instance i will have received exactly R
classiﬁcations, therefore 
c xi c = R. The observed
agreement Po, representing the degree of agreement
among R raters, for instance, i, can be computed as the
ratio of concordant rater pairs
xic
2

to the total potential
rater pairs
R
2

. The proportion Pi for a given instance i
can therefore be calculated as:
Pi =

c
xic
2

R
2

(2)
The overall observed fraction of agreement Po can be
quantiﬁed by the average of all Pi values as follows:
Po = 1
I

i
Pi
(3)
The Pe is the expected agreement by chance. All raters
R select exactly one class for each instance; therefore,
in total we will have I R classiﬁcations. Thus, the ratio
of all assignments to the cth class can be expressed as

i x2
ic
I R , which is the probability of assigning an instance i
to a class c by chance. Additionally, the probability that
any pair of raters classiﬁes an instance i into a class is c
given by (

i x2
ic
I R )2. Consequently, if the raters conducted
their classiﬁcations entirely at random, the probability
123

--- Page 13 ---

Journal of King Saud University Computer and Information Sciences (2025) 37 :271
Page 13 of 23
271
Table 5 Interpretive scale of α scores (Hughes 2021)
Alpha α
Level of Agreement
α ≤0.2
Slight
0.2 < α ≤0.4
Fair
0.4 < α ≤0.6
Moderate
0.6 < α ≤0.8
Substantial
α > 0.8
Near-Perfect
that two raters agree on all categories by chance is given
by Eq. (4):
Pe =

c
(

i xic
I R
)2
(4)
Substituting the equations into the κ coefﬁcient in (1)
returns Fleiss’ Kappa κ.
3. Krippendorff’s Alpha (α). Krippendorff’s Alpha (α)
(Krippendorff 2004) it is a statistical metric used to
evaluate inter-rater reliability between multiple raters or
annotators for a versatile type of data, including nomi-
nal, ordinal, interval, and ratio scales. The α coefﬁcient
is computed given Eq. (5).
α = 1 −Do
De
(5)
where:
Do denotes the observed disagreement among annota-
tors,
De denotes the expected disagreement by chance.
The Do quantiﬁes the actual agreement observed among
the raters. It is computed using a coincidence matrix that
cross-references the data with compatible values. De denotes
the ratio of instances in which agreement is expected to occur
Table 6 Agreement scores among the annotators
Set
κ Value
α Value
1st
0.58
0.51
2nd
0.56
0.39
3rd
0.17
0.15
4th
0.36
0.28
5th
0.56
0.55
6th
0.69
0.67
7th
0.68
0.64
by chance. It modiﬁes the agreement score by considering the
probability of a chance agreement. The α coefﬁcient values
span from 0 to 1, with α = 1 indicating perfect reliability,
while α = 0 denotes an absence of reliability. Table 5 presents
an interpretation for the α score.
6 Results
Thissectionpresentstheresultsofourinvestigationintoemo-
tion preservation in English translations of the Quran using
LLMs. Beginning with the human annotation and veriﬁcation
outcomes, Fig. 3 shows the distribution of emotional classes
of the ELQV dataset, which represents approximately 34% of
the Quran verses. Table 6 shows the agreement levels among
the seven sets of annotators, indicated by the Fleiss Kappa κ
and Krippendorff’s Alpha α values.
The distributions of emotion in the Quran and its English
translations are analyzed with Fig. 4 and Table 7, respec-
tively. Figure 4 illustrates the comparative bar graph showing
the distributions of emotion across the Quran and the
seven English translations. Table 7 presents comprehensive
statistics on the discovered emotion of the Quran and the
translations.
Fig. 3 Distribution of emotional classes of the ELQV
123

--- Page 14 ---

271
Page 14 of 23
Journal of King Saud University Computer and Information Sciences (2025) 37 :271
Fig. 4 Distribution of emotion in the Quran and the translations
Table 7 Statistics of emotions in the Quran and the translations
Scripts
Anger
Fear
Joy
Sadness
The Quran
973
2483
2237
543
Arberry (Arberry, 1996)
624
3189
2155
268
Muhammad Sarwar (Sarwar, 1981)
957
2598
2307
374
Mohsin Khan and AlHilali (Al-Hilali and Khan, 1998)
733
2870
2343
290
Pickthall (Pickthall, 1953)
603
3065
2304
264
Sahih International (International, 1997)
785
2936
2211
304
Shakir (Shakir, 1999)
737
2997
2166
336
Yusuf Ali (Ali, 2001)
694
3024
2272
246
Fig. 5 κ agreement scores between the annotators and Arabic LLMs
123

--- Page 15 ---

Journal of King Saud University Computer and Information Sciences (2025) 37 :271
Page 15 of 23
271
Table 8 Detailed κ agreement scores between the annotators and Ara-
bic LLMs
Model
κ Value
CAMeLBERT-CA (Inoue et al., 2021)
0.36
CAMeLBERT-MIX (Inoue et al., 2021)
0.35
CAMeLBERT-MSA (Inoue et al., 2021)
0.32
MARBERT (Abdul-Mageed et al., 2021)
0.89
MARBERTv2 (Elmadany et al., 2023)
0.37
MARBERT-Sentiment
0.36
ARBERT (Abdul-Mageed et al., 2021)
0.37
ARBERTv2 (Elmadany et al., 2023)
0.37
QARiB (Abdelali et al., 2021)
0.36
ArabicBERT base (Safaya et al., 2020)
0.32
AraBERTv2 base (Antoun et al., 2020)
0.31
Arabic ALBERT (Safaya, 2020)
0.27
ArabicBERT large (Safaya et al., 2020)
0.36
AraBERTv2 large (Antoun et al., 2020)
0.23
The degree of emotional agreement between annotators
and the Arabic LLMs is quantiﬁed using Cohen’s Kappa κ,
considering there are just two raters: the emotions assigned
by annotators and those assigned by Arabic LLMs. Fig-
ure 5 visualizes the agreement level between annotators and
LLMs, while Table 8 presents the detailed κ score values.
As for the level of emotional concordance between the
Quran and its English translations, the central goal of this
research, it was assessed using Cohen’s Kappa κ. Figure 6
illustrates the extent of emotional alignment between the
Quran and the English translations, whereas Table 9 presents
a breakdown of these degrees.
Table 9 Detailed κ agreement scores between the Quran and the trans-
lations
Translation
κ Value
Arberry (Arberry, 1996)
0.290
Muhammad Sarwar (Sarwar, 1981)
0.355
Mohsin Khan and AlHilali (Al-Hilali and
Khan, 1998)
0.351
Pickthall (Pickthall, 1953)
0.322
Sahih International (International, 1997)
0.344
Shakir (Shakir, 1999)
0.350
Yusuf Ali (Ali, 2001)
0.317
In terms of testing the hypothesis that claims there is a sig-
niﬁcant difference in the agreement scores of the translations
with the Quran, a bootstrapping technique is used. It illus-
trates the sampling distribution of the Cohen Kappa κ scores
of a sample derived from the original dataset by repeatedly
sampling with replacement. The experiment then includes
calculating the difference between κ values for translation
pairs, the conﬁdence interval, and p-values related to that
sample to assess the statistical signiﬁcance of the variation
in κ-values among the translations presented in Table 9.
Accordingly, the analytical experiments indicated that the
translation of Arberry demonstrated a statistically signiﬁ-
cant outcome to all translations, excluding the translations
of Pickthall and Yusuf Ali, indicating that the conﬁdence
interval consistently does not intersect 0 and the p-value was
less than 0.001.
Although the primary goal of this research is to measure
the emotion preservation in the Quran translations, it also
Fig. 6 κ agreement scores between the Quran and the translations
123

--- Page 16 ---

271
Page 16 of 23
Journal of King Saud University Computer and Information Sciences (2025) 37 :271
contributes to measuring the consistency of emotional levels
among English translations of the Quran. Figure 7 depicts
the agreement Cohen Kappa κ score among the translation
pairs.
7 Discussion
According to Fig. 3, the results obtained from from the
ELQV, which was annotated by PhD holders in Arabic lin-
guistics or Islamic law, demonstrate that 675 of the verses are
classiﬁed as fear verses, accounting for around 32.14% of the
total human veriﬁcation sample. Additionally, approximately
28.05% of the Quran verses are classiﬁed as joy verses. Con-
versely, the verses classiﬁed as anger or sadness are less
than other emotions, representing approximately 23.57% and
16.24%, respectively. Given the fact that the annotators are
divided among several sets and each set contains different
verses, the agreement levels among annotators vary accord-
ingly, based on Table 6. The agreement scores of the third
set are slight depending on both κ and α interpretations.
This indicates difﬁculties in reaching consensus among the
annotators, potentially due to several factors, including the
complexity of the annotation process or the ambiguous deci-
sion boundary. The complexity of the annotation process may
arise from annotators encountering difﬁculties with a verse
being analyzed, leading to discrepancies in their annotations.
The ambiguous decision boundary may further justify the
low κ score; possibly the annotator encountered challenges
in classifying the verses due to the similarities among the
classes. A potential technique to resolve these challenges
entails conducting a pilot test on a limited sample to pinpoint
sources of discrepancy and thereafter modifying deﬁnitions
or samples as required.
Figure 4 illustrates the emotion of the Quran and the
translations. Precisely, the Quran verses classiﬁed as the fear
versesconstituteapproximately39.82%,whiletheversesthat
are classiﬁed as the joy verses are about 35.87%. As for the
percentage of the Quran verses classiﬁed as anger verses,
it amounts to 15.6%, while the verses that are classiﬁed as
sadness verses are around 8.71%. By the same token, the
distribution of emotions in all English translations resembles
the emotions in the Quran. This suggests that the emotions
conveyed by the English translations under examination gen-
erally align with emotions expressed in the Quran. Table 7
demonstrates that the verses in the Quran and its transla-
tions conveying fear and joy exceed those verses with other
emotions. In comparison, the quantity of verses classiﬁed as
conveying anger or sadness is relatively lower than the other
emotions. This is aligned with the results acquired from the
human annotation and validation process that were illustrated
Fig. 7 κ agreement score among English translations
123

--- Page 17 ---

Journal of King Saud University Computer and Information Sciences (2025) 37 :271
Page 17 of 23
271
in Fig. 3. This can be attributed to the fact that the verses of
the Quran and the Quranic principles are purely rooted in
the emotion of fear. This was apparent from the annotation
process conducted by professionals with a PhD in Islamic
law, who likely considered traits that would elude the typical
Quran reader.
Figure 5 shows that all the models exhibited similar levels
of agreement with human annotations, with the exception of
the MARBERT model. The predictions of the majority of
Arabic LLMs align with human annotators at a fair level of
agreement, with κ scores between 0.23 and 0.37. This indi-
cates that while there is some agreement, a considerable level
of disagreement remains. Thus, these models may necessitate
improvement to enhance prediction accuracy and improve
consistency with human annotations. Conversely, the pre-
dictions of the MARBERT model exhibited almost perfect
agreement with human annotations, with a κ value of 0.89.
This level of agreement demonstrates that the MARBERT
proﬁciently captures the emotional subtleties of the Quran,
highlighting its value as an Arabic LLM.
Remarkably, all the translations under investigation pre-
served the emotion of the Quran at a fair level. Speciﬁcally,
theemotionagreementlevelbetweentheQuranandthetrans-
lations, as determined by human annotations, ranges from a
κ score of 0.29 to 0.35. As demonstrated in Table 9, the trans-
lations by Muhammad Sarwar, Mohsin Khan and AlHilali,
and Shakir preserved the emotional essence of the Quran
with a κ score of 0.35. The translation of Sahih Interna-
tional maintained the emotional semantics at a level of κ =
0.34. Comparatively, the translations of Pickthall and Yusuf
Ali preserved the emotions conveyed in the Quran with a
κ scores of 0.32 and 0.31, respectively. The translation of
Arberry showed a marginally lower level of emotion preser-
vation, reﬂected by a κ score of 0.29. The relatively fair κ
scores suggest a signiﬁcant amount of emotion in the Quran is
not fully conveyed in the English translations. This may arise
from the inherent challenges of translating the Quran, which
frequently relies on cultural and contextual aspects that may
lack their counterparts in English. On top of that, each trans-
lation reﬂects the translator’s interpretation of the Quran,
shaped by their subjective reading and sectarian orientation
(Elewa 2016); therefore, the theological interpretation and
the translator’s sectarian background can profoundly impact
emotion preservation by altering the emotional semantics of
the source scripts, leading to these low κ scores. However, the
varied levels indicate that the analyzed English translations
adequately capture the emotional semantics of the Quran at
a fair level. Yet, this level remains relatively low, indicating
that non-Arabic readers perceive between 29% and 35% of
the emotions conveyed in the Quran.
For the agreement levels among the translations, Fig. 7
indicates that the emotions in the pairs of English transla-
tions are generally consistent. All English translations exhibit
a substantial degree of agreement. Notably, the translation by
Mohsin Khan and AlHilali, along with Sahih International,
achieved the highest agreement κ score of 0.74. Conversely,
the translations by Muhammad Sarwar and Arberry exhib-
ited the lowest agreement κ score of 0.61. The remaining
translation pairs exhibited agreement κ scores ranging from
0.63 to 0.73, as detailed in Fig. 7.
8 Qualitative analysis
This section offers a qualitative analysis of the differences in
emotional classiﬁcation between the verses of the Quran and
their English translations. It provides multiple examples with
distinct emotional categories and analyzes the causes behind
thevariationsusingtwoEnglishdictionaries:theCambridge7
and Merriam-Webster8.
Example 1
ِ
ِ
ِﻭﺡِ
[Fear]
• Mohsin Khan and AlHilali: And they ask you (O
Muhammad SAW) concerning the Ruh (the Spirit); Say:
“The Ruh (the Spirit): it is one of the things, the knowl-
edge of which is only with my Lord. And of knowledge,
you (mankind) have been given only a little.” [Sadness]
• Pickthall: They are asking thee concerning the Spirit.
Say: The Spirit is by command of my Lord, and of knowl-
edge ye have been vouchsafed but little. [Joy]
• Sahih International: And they ask you, [O Muhammad],
about the soul. Say, “The soul is of the affair of my Lord.
And mankind have not been given of knowledge except a
little.” [Anger]
The verse was disclosed to the Prophet Mohammed,
PBUH, in response to the disbelievers who inquired about
the spirit using confrontational language. The answer to the
inquiry was that the spirit is a creation of Allah Almighty, the
knowledge of which He has retained for Himself. The verse
also asserts the reality of humanity’s constrained knowledge.
The wordﻭﺡُwas translated as “the spirit” in most trans-
lations of the Quran and has a broader meaning in the Quran
and Arabic language. In the Quran, the termﻭﺡُencom-
passes several aspects, one of which pertains to the spirit
asked about by the disbelievers in the verse under analy-
sis9. To determine the intended meaning of the word under
investigation, we shall use Arabic dictionaries to uncover its
7 https://dictionary.cambridge.org/dictionary/english/
8 https://www.merriam-webster.com/
9 https://shamela.ws/book/6462
123

--- Page 18 ---

271
Page 18 of 23
Journal of King Saud University Computer and Information Sciences (2025) 37 :271
original interpretation. The meanings of the word were exam-
ined in two Arabic dictionaries: Al-Qamus Al-Muhit10 and
Lisan Al-Arab11.
• Al-Qamus Al-Muhit:
ِ
What constitutes the existence of souls.
• Lisan Al-Arab:
ﻭﺡِﺃ
The interpretation of the soul is that it represents what
gives life to the soul.
In light of these senses derived from the Quran and the
Arabic dictionaries, it can be concluded that the wordﻭﺡُ
signiﬁes anything that embodies life, including meaning or
signiﬁcance, such as the Holy Quran, which is termed a spirit
for its ability to revive spirits via knowledge and faith. There-
fore, the meaning of
in this verse refers to the spirit that
animates human bodies.
The translation by Mohsin Khan and AlHilali used the
word “the Ruh,” a transcription of
, to preserve its
original meaning and document the word in English, accom-
panied by its equivalent English translation, “the spirit,”
and Pickthall’s translation used the same word. Conversely,
the translation of Sahih International rendered
as “the
soul,” which may signify distinct meanings based on theo-
logical perspectives in archaic English. The translations of
Mohsin Khan and Al-Hilali and Pickthall utilized the word
“concerning” to capture the nature of the inquiry. It is clear
from the meaning of the verse that the question of the disbe-
lievers was framed as a challenge to the Prophet Mohammed,
PBUH, driven not by a desire for knowledge or comprehen-
sion but rather by an intent to confront him. While Mohsin
Khan and AlHilali’s translation offered a straight response
that included the knowledge Allah has reserved for Him-
self, the translations of Pickthall and Sahih International
addressed the same meaning using the words “command”
and “affair.” The translation of Pickthall differed from the
other two by using the word “vouchsafe” instead of “given”
for the word
. Both convey the meaning of the verse;
yet, linguistic discrepancies may directly contribute to the
variation in the classiﬁcation.
Example 2
[Anger]
10 https://shamela.ws/book/7283
11 https://shamela.ws/book/1687
• Muhammad Sarwar: He continued, “Remember, this
one whom you have honored more than me I shall bring
him and most of his offspring under my sway if you will
give me respite until the Day of Judgment.” [Fear]
• Arberry: He said, “What thinkest Thou? This whom
Thou hast honoured above me—if Thou deferrest me to
the Day of Resurrection I shall assuredly master his seed,
save a few.” [Joy]
The whole context of the two translations suggests that
theydidnotadequatelyconveythetoneofdisbeliefexpressed
by Satan in dialogue with Allah Almighty. Both translations
insteadconveyedhisthreatsandpledgestomisleadhumanity.
The term
was rendered as “sway” in the translation
of Muhammad Sarwar. According to the Cambridge English
dictionary, “sway” is the act of causing an object to move
slowly from side to side. This could partly fail to fully convey
the primary objective of Satan, which is persistent misleading
of humanity, resulting in ambiguity on the extent or nature
of sway, which contributed to the classiﬁcation of the fear
emotional class. Conversely, the translation of Arberry used
the term “master,” which introduced a positive sense to the
overall context of the translation, so inadequately conveying
the intended meaning associated with the word
,
resulting in its classiﬁcation under the joy class.
Example 3
[Sadness]
• Pickthall: And every small and great thing is recorded.
[Joy]
• Yusuf Ali: Every matter, small and great, is on record.
[Fear]
The Arabic term
was rendered as “record” in
the English translations by Pickthall and Yusuf Ali. The
translations differ in their interpretation of
, in which
the translation of Pickthall used “every...thing,” and Yusuf
Ali translated it as “every matter.” Both terms convey the
intended meaning of the verse; however, they differ in
their linguistic characteristics. The term “thing” has broader
implications that denote unspeciﬁed entities, whereas “mat-
ter” speciﬁcally refers to the content of a physical entity,
leaving an unanswered concern of what will be recorded,
where the actual meaning of the verse includes all human
deeds.
Example 4
[Sadness]
123

--- Page 19 ---

Journal of King Saud University Computer and Information Sciences (2025) 37 :271
Page 19 of 23
271
• Pickthall: Whatever of misfortune striketh you, it is what
your right hands have earned. And He forgiveth much.
[Joy]
• Shakir: And whatever afﬂiction befalls you, it is on
account of what your hands have wrought, and (yet) He
pardons most (of your faults). [Fear]
The term
was rendered as “misfortune” in the
translation of Pickthall, whereas Shakir preferred the term
“afﬂiction.” Both terms denote challenging or distressing
events; however, they differ fundamentally. The Cambridge
English Dictionary deﬁnes “misfortune” as an adverse event
or circumstance, whereas “afﬂiction” denotes a more endur-
ing condition of suffering, typically associated with pain or
distress. The two translations translated the term
with
two different words. Pickthall translated it as “earned,” while
Shakir used “wrought,” with each term possessing unique
implications. “Earned” generally denotes acquiring some-
thing via labor or merit, whereas “wrought,” on the other
hand, is an adjective used to characterize something created
or completed with meticulousness or artistry. The Arabic
term
was translated as “forgiveth” and “pardons.”
The Merriam-Webster English dictionary indicates that the
two terms exhibit distinctions. “Forgive” denotes the end of
wrath towards an offender, while “pardon” signiﬁes the deci-
sion not to hold an individual accountable for wrongdoing.
The variance in usage of terms might not faithfully convey
the intended meaning of the Quran, leading to different levels
of emotional preservation.
Example 5
[Sadness]
• Muhammad Sarwar: All that is in the heavens and the
earth will return to the Beneﬁcent God as His submissive
servants. [Joy]
• MohsinKhanandAlHilali:Thereisnoneintheheavens
and the earth but comes unto the Most Beneﬁcent (Allah)
as a slave. [Fear]
The word
was translated into “come” in most English
translations of the Quran except the translation of Muham-
mad Sarwar, which used the word “return.” Both “come”
and “return” signify movement toward a particular desti-
nation. The word “come” implies the action of moving to
a location, outcome, or conclusion. Conversely, the word
“return” describes a return to something, revealing the
intended meaning of the text, wherein all of humanity would
revert to the Creator, Allah Almighty. The word
was
translated into English as “slave” and “servant.” Based on
the English dictionaries, the two words denote the condi-
tion of human slavery, although the intended meaning of the
verse refers to the slaves of Allah Almighty, who worship
Him exclusively. The signiﬁcant differences between the two
meanings may impact the classiﬁcation of emotions in the
present translations.
Example 6
[Fear]
• Pickthall: Lo! there are above you guardians. [Joy]
• Shakir:Andmostsurelytherearekeepersoveryou.[Sad-
ness]
The verse clariﬁed the accounting of Allah for His wor-
shipers, where He assigned over them vigilant angels who
document all their deeds, whether good or evil, for which
they would be held accountable in the afterlife. The word
was rendered as “guardians” in Pickthall’s transla-
tion and as “keepers” in Shakir’s translation. Although these
two words failed to fully explain the angelic nature of the
guards and do not highlight their signiﬁcance, they could
lead the reader to infer that they are human beings. However,
the word
refers to the watching angels, as this discrep-
ancy signiﬁcantly inﬂuenced the differences in the classes of
emotions for the translations.
Example 7
[Sadness]
• Sahih International: And preferred the life of the world.
[Joy]
• Yusuf Ali: And had preferred the life of this world. [Fear]
The term
has been translated as “preferred” in the
majority of Quran translations. This interpretation conveys
that the individual favored and chose earthly life rather than
the Hereafter. The Sahih International translation was classi-
ﬁed as conveying emotions of joy, a label that may partially
lack the intended meaning within the context of the verse.
Conversely, Yusuf Ali’s translation was categorized as fear,
reﬂecting the concern about the repercussions of prioritizing
worldly matters above the Hereafter, as this temporal world
is ﬂeeting and mortal, while the afterlife is permanent.
Example 8
[Sadness]
• Muhammad Sarwar: Father, do not worship satan; he
has disobeyed the Beneﬁcent God. [Anger]
123

--- Page 20 ---

271
Page 20 of 23
Journal of King Saud University Computer and Information Sciences (2025) 37 :271
• Mohsin Khan and AlHilali: O my father! Worship not
Shaitan (Satan). Verily! Shaitan (Satan) has been a rebel
against the Most Beneﬁcent (Allah). [Fear]
• Yusuf Ali: “O my father! serve not Satan: for Satan is a
rebel against (Allah) Most Gracious. [Joy]
ThisverseoutlinedthedifﬁcultsituationofIbrahim(Abra-
ham) with his father, Azar, highlighting his prayer for his
father to refrain from worshipping Satan, which, in this con-
text, refers to the disobedience of Satan in the worship of
idols. In the Quran, the ones who worship entities other than
Allah are deemed as disbelievers, akin to Satan. The verse
was characterized by a tone of sadness that was attributed
to the situation of Ibrahim, whereas the translations were
differently classiﬁed as anger, fear, and joy. The term
signiﬁes a tone of kindness and gentleness that Ibrahim used
when speaking to his father. Both the translations of Mohsin
Khan and AlHilali, as well as Yusuf Ali, expressed this
tone by rendering
as “o my father.” The translation
by Muhammad Sarwar employed a formal tone, which may
imperfectly convey the deep sympathy in the verse, partic-
ularly in the usage of the term “father.” The term
was
rendered as “worship” in the translations by Muhammad
Sarwar, Mohsin Khan, and AlHilali, whereas Yusuf Ali trans-
lated it as “serve.” The term “worship” accurately reﬂects
the intended meaning of the verse; however, the term “serve”
denotes loyalty and service to Satan, failing to highlight
the meaning of servitude, which may introduce an unin-
tended sense of the verse. Mohsin Khan and AlHilali, along
with Yusuf Ali, translated the term
as “rebel,” while
Muhammad Sarwar interpreted it as “disobeyed.” The term
“rebel” denotes a scenario in which an individual exhibits
opposition or deﬁance, whereas “disobey” indicates the con-
dition in which an individual neglects to comply. Notably, the
translations, except for Muhammad Sarwar, used the term
“Allah” instead of “God,” highlighting cultural-linguistic
distinctions that may inﬂuence emotion preservation in the
translations.
9 Conclusion
This research introduces a computational quantitative app-
roach to investigate emotion preservation in English trans-
lations of the Quran using LLMs. The research enriches the
Arabic NLP ﬁeld within the context of emotion analysis by
theintroductionoftheELQVdatasetandrevealsthepotential
of leveraging LLMs in the Islamic context. This research had
two limitations, including the scarcity of emotionally labeled
Classical Arabic textual materials and insufﬁcient computa-
tional resources, which signiﬁcantly constrained the scope of
the research. Future research may entail exploring additional
LLMs and assessing their efﬁcacy for detecting emotional
semantics within religious contexts. Additionally, forthcom-
ing research will likely include an expansion of the ELQV
dataset to cover nearly all of the Quran verses.
A Fine-tuning settings
The models in this work underwent ﬁne-tuning across mul-
tiple epochs (e) utilizing various learning rates (η), with a
Table 10 Hyperparameter setting
Model
Hyperparameters
CAMeLBERT-CA
e = 3
CAMeLBERT-MIX
b = 16
CAMeLBERT-MSA
η = 3e −5
MARBERT
MARBERTv2
e = 3
MARBERT-Sentiment
b = 16
ARBERT
η = 5e −5
ARBERTv2
QARiB
e = 5
b = 16
η = 5e −5
ArabicBERT base
e = 3
b = 16
η = 5e −5
AraBERTv2 base
e = 3
b = 8
η = 5e −5
Arabic ALBERT
e = 3
ArabicBERT large
b = 16
η = 5e −5
AraBERTv2 large
e = 3
b = 16
η = 1e −5
XLM-RoBERTa
e = 5
b = 16
η = 5e −5
BERT
e = 3
DistillBERT
b = 16
η = 5e −5
ALBERT
e = 3
DeBERTa
b = 16
η = 1e −5
123

--- Page 21 ---

Journal of King Saud University Computer and Information Sciences (2025) 37 :271
Page 21 of 23
271
weight decay of 0.01 used for regularization. A batch size
(b) of 16 or 8 sequences per device was employed for both
training and evaluation. This appendix outlines the hyper-
parameter conﬁgurations for the ﬁne-tuning of the models
outlined in Table 2.
B. Validation algorithms
This appendix describes the validation algorithms employed
to validate the emotion predictions of the Quran verses and
the English translations. Algorithm 1 describes the process
for validating Arabic emotion predictions within the Quran
verses. All Quran verses V are used as input, each accom-
panied by predictions from various LLMs M, along with a
subset of verses HV S that undergo a human annotation and
veriﬁcation process. For each verse, the algorithm receives
both hard and soft predictions from all models, as enumer-
ated in lines 9 to 11. For lines 12 to 15, if a majority vote
exists among the models, the prediction is assigned accord-
ingly; if not, the prediction with the greatest average score
across labels is selected. Additionally, verses in the human
veriﬁcation sample HV S undergo a human validation step
to verify the label assigned by the LLMs. The output is the
aggregate set of predictions P for all the Quran verses. Algo-
rithm 2 differs from Algorithm 1 in that, in the absence of a
majority vote, the label with the highest average prediction
score is selected.
Algorithm 1 Validation of Arabic Emotion Prediction.
1: Input: V = {v1, v2, . . . , v6236} Sum of the Quran verses
2: Output: P = {Pv1, Pv2, . . . , Pv6236} Sum of LLMs predictions
3: HumanV eri f icationSample:
HV S
=
{hvs1, hvs2, . . . , hvs2100}
4: M = {m1, m2, . . . , m14} Sum of Arabic LLMs
5: Pv,m: Hard prediction of model m for verse v
6: Sv,m: Soft prediction score of model m for verse v
7: ModelsMajorityV ote: Label predicted by the majority of Arabic
LLMs
8: Highest AverageScore(): Highest average score among the aver-
age scores of each label
9: for vi ∈V do
10:
for mi ∈M do
11:
Get soft and hard predictions {Pv,m, Sv,m}
12:
if ∃ModelsMajorityV ote then
13:
Pvi ←ModelsMajorityV ote
14:
else
15:
Pvi ←Argmax(Highest AverageScore())
16:
end if
17:
end for
18:
if vi ∈HumanV eri f icationSample then
19:
HumanVeriﬁcation()
20:
else
21:
Pvi ←ModelsMajorityV ote
22:
end if
23: end for
Algorithm 2 Validation of English Emotion Prediction.
1: Input: V = {v1, v2, . . . , v6236} Sum of the verses in the translations
2: Output: P = {Pv1, Pv2, . . . , Pv6236} Sum of LLMs predictions
3: M = {m1, m2, . . . , m5} Sum of English LLMs
4: Pv,m: Hard prediction of model m for verse v
5: Sv,m: Soft prediction score of model m for verse v
6: ModelsMajorityV ote: Label predicted by the majority of English
LLMs
7: LabelHighest AverageScore(): Returns the label with the highest
average score
8: for vi ∈V do
9:
for mi ∈M do
10:
Get soft and hard predictions {Pv,m, Sv,m}
11:
if ∃ModelsMajorityV ote then
12:
Pvi ←ModelsMajorityV ote
13:
else
14:
Pvi ←LabelHighest AverageScore()
15:
end if
16:
end for
17: end for
Acknowledgements The authors gratefully acknowledge Qassim Uni-
versity, represented by the Deanship of Graduate Studies and Scientiﬁc
Research, on the ﬁnancial support for this research under the number
(QU-J-PG-2-2025-53285) during the academic year 1446 AH / 2024
AD.
Funding This work was supported by the Deanship of Graduate Studies
and Scientiﬁc Research at Qassim University under Grant QU-J-PG-2-
2025-53285.
Data Availability Data is accessible here: https://github.com/Arwaalmr
zoqi/ELQV (accessed on 20 February 2025).
Declarations
Competing Interests The authors report there are no competing inter-
ests to declare regarding this research.
Open Access This article is licensed under a Creative Commons
Attribution-NonCommercial-NoDerivatives 4.0 International License,
which permits any non-commercial use, sharing, distribution and repro-
duction in any medium or format, as long as you give appropriate credit
to the original author(s) and the source, provide a link to the Creative
Commons licence, and indicate if you modiﬁed the licensed mate-
rial. You do not have permission under this licence to share adapted
material derived from this article or parts of it. The images or other
third party material in this article are included in the article’s Creative
Commons licence, unless indicated otherwise in a credit line to the
material. If material is not included in the article’s Creative Commons
licence and your intended use is not permitted by statutory regula-
tion or exceeds the permitted use, you will need to obtain permission
directly from the copyright holder. To view a copy of this licence, visit
http://creativecommons.org/licenses/by-nc-nd/4.0/.
References
Abdelali A, Hassan S, Mubarak H, Darwish K, Samih Y (2021)
Pre-training bert on arabic tweets: Practical considerations.
https://arxiv.org/abs/2102.10684
123

--- Page 22 ---

271
Page 22 of 23
Journal of King Saud University Computer and Information Sciences (2025) 37 :271
Abdul-Mageed M, Elmadany A, Nagoudi EMB (2021) ARBERT &
MARBERT: Deep bidirectional transformers for Arabic. Pro-
ceedings of the 59th annual meeting of the association for
computational linguistics and the 11th international joint confer-
ence on natural language processing (volume 1: Long papers), pp
7088–7105. https://doi.org/10.18653/v1/2021.acl-long.551
Aﬂi H, Maguire S, Way A (2017) Sentiment translation for low
resourced languages: Experiments on irish general election tweets.
Int J Comput Linguist Appl
Al-Hilali MTD, Khan MM (1998) The noble qur’an: The english trans-
lation of the meanings and commentary. King Fahd Complex,
Madinah
Ali Y (2001) The holy quran: Translation and commentary. Islamic
Vision, Birmingham UK
Almarzoqi A, Alsuhaibani M (2025) Sentiment analysis-based review
of sentiment polarity in translations. Proceedings of the 2024 8th
international conference on computer science and artiﬁcial intel-
ligence, pp 382–391. https://doi.org/10.1145/3709026.3709092
Al-Twairesh N (2021) The evolution of language models applied to
emotion analysis of arabic tweets. Inf 12(2):84. https://doi.org/10.
3390/info12020084
Antoun W, Baly F, Hajj H (2020) AraBERT: Transformer-based model
for Arabic language understanding. In Al-Khalifa HW, Magdy K,
Elsayed DT, Mubarak H (eds) Proceedings of the 4th workshop on
open-source arabic corpora and processing tools with a shared task
on offensive language detection, European Language Resource
Association, pp 9–15. https://aclanthology.org/2020.osact-1.2/
ArberryAJ(1996)Thekoraninterpreted:Atranslation.Schuster,Simon
Banik D (2023) Sentiment induced phrase-based machine translation:
Robustness analysis of pbsmt with senti-module. Eng Appl Artif
Intell 126:106977
Barhoumi A, Aloulou C, Camelin N, Esteve Y, Belguith L (2018) Arabic
sentiment analysis: An empirical study of machine translation’s
impact. Lang Process Knowl Manag Int Conf (LPKM2018)
Conneau A, Khandelwal K, Goyal N, Chaudhary V, Wenzek G, Guzmán
F, Grave E, Ott M, Zettlemoyer L, Stoyanov V (2020) Unsuper-
vised crosslingual representation learning at scale. In Jurafsky D,
Chai J, Schluter N, Tetreault J (eds) Proceedings of the 58th annual
meeting of the association for computational linguistics, Associ-
ation for Computational Linguistics, pp 8440–8451. https://doi.
org/10.18653/v1/2020.acl-main.747
Devlin J, Chang MW, Lee K, Toutanova K (2019) BERT: Pre-training
of deep bidirectional transformers for language understanding.
https://doi.org/10.48550/arXiv.1810.04805
Ekman P (1992) An argument for basic emotions. Cognit Emot 6(3–
4):169–200. https://doi.org/10.1080/02699939208411068
Elewa A (2016) Translating the sacred text: A polysystem approach. J
Transl 12(1):13–27. https://doi.org/10.54395/jot-v5pkk
Elmadany A, Nagoudi EB, Abdul-Mageed M (2023) ORCA: A chal-
lenging benchmark for Arabic language understanding. In Rogers
A, Boyd-Graber J, Okazaki N (eds) Findings of the association
for computational linguistics: Acl 2023, Association for Compu-
tational Linguistics, pp 9559–9586. https://doi.org/10.18653/v1/
2023.ﬁndings-acl.609
Fleiss JL (1971) Measuring nominal scale agreement among many
raters. Psychol Bull 76(5):378
Gaanoun K, Alsuhaibani M (2025) Sentiment preservation in Quran
translation with artiﬁcial intelligence approach: Study in rep-
utable English translation of the Quran. Humanit Soc Sci Commun
12(1):222. https://doi.org/10.1057/s41599-024-04181-0
Gangula RRR, Mamidi R (2018) Impact of translation on sentiment
analysis: A case-study on telugu reviews. 19th international con-
ference on computational linguistics and intelligent text processing
He P, Liu X, Gao J, Chen W (2021) Deberta: Decoding-enhanced bert
with disentangled attention. https://arxiv.org/abs/2006.03654
Hughes J (2021) Krippendorffsalpha: An r package for measuring
agreement using krippendorff’s alpha coefﬁcient. arXiv preprint
arXiv:2103.12170
Inoue G, Alhafni B, Baimukan N, Bouamor H, Habash N (2021) The
interplay of variant size and task type in Arabic pre-trained lan-
guage models. In Habash N, Bouamor H, Hajj H, Magdy W,
Zaghouani W, Bougares F, Tomeh N, Abu Farha I, Touileb S
(eds) Proceedings of the 6th arabic natural language processing
workshop, Association for Computational Linguistics, pp 92–104.
https://aclanthology.org/2021.wanlp-1.10/
International S (1997) The qur’an: Arabic text with corresponding
english meanings
Jurafsky D, Martin JH (2025) Speech and language processing: An
introduction to natural language processing computational linguis-
tics and speech recognition with language models (3rd) [Online
manuscript released January 12 2025]. https://web.stanford.edu/
~jurafsky/slp3/
Kajava K, Öhman E, Hui P, Tiedemann J (2020) Emotion preservation
in translation: Evaluating datasets for annotation projection. Digit
Human Nordic Countries 38–50
Krippendorff K (2004) Measuring the reliability of qualitative text anal-
ysis data. Qual Quant 38:787–800
Kumari D, Ekbal A (2024) Enhancing sentiment and emotion transla-
tion of review text through mlm knowledge integration in nmt. J
Intell Inf Syst 62(5):1213–1237. https://doi.org/10.1007/s10844-
024-00843-2
Kumari D, Ekbal A, Haque R, Bhattacharyya P, Way A (2021)
Reinforced NMT for sentiment and content preservation in low-
resource scenario. ACM Trans Asian Low-Resour Lang Inf
Process 20(4) .https://doi.org/10.1145/3450970
Lan Z, Chen M, Goodman S, Gimpel K, Sharma P, Sori-
cut R (2019) ALBERT: A lite BERT for self-supervised
learning of language representations. CoRR abs/1909.11942.
http://arxiv.org/abs/1909.11942
Landis JR, Koch GG (1977) The measurement of observer agreement
for categorical data. Biometrics 159–174
Litvinenko A (2021) Youtube as alternative television in russia: Political
videos during the presidential election campaign 2018. Soc Media
Soc 7(1). https://doi.org/10.1177/2056305120984455
Liu Y, Ott M, Goyal N, Du J, Joshi M, Chen D, Levy O, Lewis M,
Zettlemoyer L, Stoyanov V (2019) Roberta: A robustly optimized
bert pretraining approach. arXiv:1907.11692
Lohar P, Aﬂi H, Way A (2017) Maintaining sentiment polarity in
translation of user-generated content. Prague Bull Math Linguist
108:73–84
Lohar P, Aﬂi H, Way A (2018) Balancing translation quality and sen-
timent preservation (non-archival extended abstract) In Cherry C,
Neubig G (eds) Proceedings of the 13th conference of the associa-
tion for machine translation in the Americas (volume 1: Research
track), Association for Machine Translation in the Americas, pp
81–88. https://aclanthology.org/W18-1808
Miao J, Zhang Y, Jiang N, Wen J, Pei K, Wan Y, Wan T, Chen H (2024)
Towards unifying pre-trained language models for semantic text
exchange. Wirel Netw 30(7):6385–6398. https://doi.org/10.1007/
s11276-023-03439-w
Mohammad SM, Salameh M, Kiritchenko S (2016) How translation
alters sentiment. J Artif Intell Res 55:95–130. https://doi.org/10.
1613/jair.4787
Moons F, Vandervieren E (2023) Measuring agreement among several
raters classifying subjects into one-or-more (hierarchical) nomi-
nal categories. A generalisation of ﬂeiss’ kappa. arXiv preprint
arXiv:2303.12502
Nandwani P, Verma R (2021) A review on sentiment analysis and emo-
tion detection from text. Soc Netw Anal Min 11(1):81. https://doi.
org/10.1007/s13278-021-00776-6
123

--- Page 23 ---

Journal of King Saud University Computer and Information Sciences (2025) 37 :271
Page 23 of 23
271
Pickthall MW (1953) The meaning of the glorious koran: An explana-
tory translation by mohammed marmaduke pickthall. New Amer-
ican Library
Plaza-del-Arco FM, Cercas Curry AA, Cercas Curry A, Hovy D (2024)
Emotion analysis in NLP: Trends gaps and roadmap for future
directions. In Calzolari N, Kan MY, Hoste V, Lenci A, Sakti S, Xue
N (eds) Proceedings of the 2024 joint international conference on
computational linguistics language resources and evaluation (lrec-
coling 2024), ELRA; ICCL, pp 5696–5710. https://aclanthology.
org/2024.lrec-main.506/
Poncelas A, Lohar P, Hadley J, Way A (2020) The impact of indirect
machine translation on sentiment classiﬁcation. In Denkowski M,
Federmann C (eds) Proceedings of the 14th conference of the asso-
ciationformachinetranslationintheamericas(volume1:Research
track), Association for Machine Translation in the Americas, pp
78–88. https://aclanthology.org/2020.amta-research.7/
Qian S, Orasan C, Carmo FD, Li Q, Kanojia D (2023) Evalua-
tion of Chinese-English machine translation of emotion-loaded
microblog texts: A human annotated dataset for the quality assess-
ment of emotion translation. In Nurminen M, Brenner J, Koponen
M, Latomaa S, Mikhailov M, Schierl F, Ranasinghe T, Vanmassen-
hove E, Vidal SA, Aranberri N, Nunziatini M, Escartín CP, Forcada
M, Popovic M, Scarton C, Moniz H (eds) Proceedings of the 24th
annual conference of the european association for machine transla-
tion, European Association for Machine Translation, pp 125–135.
https://aclanthology.org/2023.eamt1.13/
Raiaan MAK, Mukta MSH, Fatema K, Fahad NM, Sakib S, Mim
MMJ, Ahmad J, Ali ME, Azam S (2024) A review on large lan-
guage models: Architectures applications taxonomies open issues
and challenges. IEEE Access 12:26839–26874. https://doi.org/10.
1109/ACCESS.2024.3365742
Saadany H, Orasan C (2020) Is it great or terrible? preserving senti-
ment in neural machine translation of Arabic reviews. In Zitouni I,
Abdul-Mageed M, Bouamor H, Bougares F, El-Haj M, Tomeh N,
Zaghouani W (eds) Proceedings of the ﬁfth arabic natural language
processing workshop, Association for Computational Linguistics,
pp 24–37. https://aclanthology.org/2020.wanlp-1.3/
Saadany H, Orasan C, Quintana RC, Carmo FD, Zilio L (2023)
Analysing mistranslation of emotions in multilingual tweets by
online MT tools. In Nurminen M, Brenner J, Koponen M, Latomaa
S, Mikhailov M, Schierl F, Ranasinghe T, Vanmassenhove E,
Vidal SA, Aranberri N, Nunziatini M, Escartín CP, Forcada M,
Popovic M, Scarton C, Moniz H (eds) Proceedings of the 24th
annual conference of the european association for machine transla-
tion, European Association for Machine Translation, pp 275–284.
https://aclanthology.org/2023.eamt-1.27/
Saadany H, Or˘asan C, Mohamed E, Tantawy A (2022) A semisuper-
vised approach for a better translation of sentiment in dialectical
Arabic UGT. In Bouamor H, Al-Khalifa H, Darwish K, Rambow
O, Bougares F, Abdelali A, Tomeh N, Khalifa S, Zaghouani W
(eds) Proceedings of the 7th arabic natural language processing
workshop (wanlp,) Association for Computational Linguistics, pp
214–224. https://doi.org/10.18653/v1/2022.wanlp-1.20
Safaya
A
(2020).
Arabic-albert.
https://doi.org/10.5281/zenodo.
4718724
Safaya A, Abdullatif M, Yuret D (2020) KUISAIL at SemEval-2020
task 12: BERT-CNN for offensive speech identiﬁcation in social
media. In Herbelot A, Zhu X, Palmer A, Schneider N, May J,
Shutova E (eds) Proceedings of the 14th workshop on semantic
evaluation, International Committee for Computational Linguis-
tics, pp 2054–2059. https://doi.org/10.18653/v1/2020. semeval-
1.271
Saffar AH, Mann TK, Ofoghi B (2023) Textual emotion detection
in health: Advances and applications. J Biomed Inf 137:104258.
https://doi.org/10.1016/j.jbi.2022.104258
Sailunaz K, Alhajj R (2019) Emotion and sentiment analysis from twit-
ter text. J Comput Sci 36:101003
Sanh V, Debut L, Chaumond J, Wolf T (2019) Distilbert a dis-
tilled version of bert: Smaller faster cheaper and lighter. ArXiv
abs/1910.01108
Sarwar M (1981) The holy quran: Arabic text and english translation.
Tahrike Tarsile Quran, Elmhurst NY, USA
Sazzed S (2020) Cross-lingual sentiment classiﬁcation in low-resource
Bengali language. In Xu W, Ritter A, Baldwin T, Rahimi A (eds)
Proceedings of the 6th workshop on noisy user-generated text (w-
nut 2020), Association for Computational Linguistics, pp 50–60.
https://doi.org/10.18653/v1/2020.wnut-1.8
Shakir MH (1999) The holy quran translated. Tahrike Tarsile Quran,
Elmhurst NY USA
Si C, Wu K, Aw AT, Kan MY (2019) Sentiment aware neural machine
translation.InNakazawaT,DingC,DabreR,KunchukuttanA,Doi
N, Oda Y, Bojar O, Parida S, Goto I, Mino H (eds) Proceedings of
the 6th workshop on asian translation, Association for Computa-
tional Linguistics, pp 200–206. https://doi.org/10.18653/v1/D19-
5227
Tafreshi S, Vatsal S, Diab M (2024) Emotion classiﬁcation in low and
moderate resource languages. https://arxiv.org/abs/2402.18424
Troiano E, Klinger R, Padó S (2020) Lost in back-translation: Emo-
tion preservation in neural machine translation. In Scott D, Bel
N, Zong C (eds) Proceedings of the 28th international conference
on computational linguistics, International Committee on Compu-
tational Linguistics, pp 4340–4354. https://doi.org/10.18653/v1/
2020.coling-main.384
Vaswani A, Shazeer N, Parmar N, Uszkoreit J, Jones L, Gomez AN,
Kaiser, Ł, Polosukhin I (2017) Attention is all you need. Proceed-
ings of the 31st international conference on neural information
processing systems 6000–6010
Zhang C, Capelletti M, Poulis A, Stemann T, Nemcova J (2017) A case
study of machine translation in ﬁnancial sentiment analysis. In
Yamada M, Seligman M (eds) Proceedings of machine translation
summit xvi: Commercial mt users and translators track, pp 49–58.
https://aclanthology.org/2017.mtsummitcommercial.7/
Publisher’s Note Springer Nature remains neutral with regard to juris-
dictional claims in published maps and institutional afﬁliations.
123

```