---
title: "2023-Unknown-RMDM A Multilabel Fakenews Dataset for Vietnamese Evidence - PDF Extract"
source_pdf: "2023-Unknown-RMDM A Multilabel Fakenews Dataset for Vietnamese Evidence.pdf"
pages: 6
extracted_at: "2026-02-13T09:50:28.236402"
---

# PDF Extract: 2023-Unknown-RMDM A Multilabel Fakenews Dataset for Vietnamese Evidence

**Source PDF:** 2023-Unknown-RMDM A Multilabel Fakenews Dataset for Vietnamese Evidence.pdf
**Total Pages:** 6

---

## Content

```
--- Page 1 ---

RMDM: A Multilabel Fakenews Dataset for
Vietnamese Evidence Verification
Hai-Long Nguyen1, Thi-Kieu-Trang Pham1, Thai-Son Le1, Tan-Minh Nguyen1,
Thi-Hai-Yen Vuong1, Ha-Thanh Nguyen2
1VNU University of Engineering and Technology, Hanoi, Vietnam
2National Institute of Informatics, Tokyo, Japan
{1long.nh, 20020485, 20020069, 20020081, yenvth}@vnu.edu.vn
2nguyenhathanh@nii.ac.jp
Abstract—In this study, we present a novel and challenging
multilabel Vietnamese dataset (RMDM) designed to assess the
performance of large language models (LLMs), in verifying elec-
tronic information related to legal contexts, focusing on fake news
as potential input for electronic evidence. The RMDM dataset
comprises four labels: real, mis, dis, and mal, representing real in-
formation, misinformation, disinformation, and mal-information,
respectively. By including these diverse labels, RMDM captures
the complexities of differing fake news categories and offers
insights into the abilities of different language models to handle
various types of information that could be part of electronic
evidence. The dataset consists of a total of 1,556 samples, with
389 samples for each label. Preliminary tests on the dataset
using GPT-based and BERT-based models reveal variations in
the models’ performance across different labels, indicating that
the dataset effectively challenges the ability of various language
models to verify the authenticity of such information. Our
findings suggest that verifying electronic information related to
legal contexts, including fake news, remains a difficult problem
for language models, warranting further attention from the
research community to advance toward more reliable AI models
for potential legal applications.
Index Terms—Electronic evidence verification, AI and Law,
Vietnamese multilabel dataset, Large Language Models
I. INTRODUCTION
The Civil Procedure Code of 2015 (CPC) plays a significant
role in addressing civil and commercial cases in practice. One
of the progressive regulations in the CPC is the introduction of
“electronic data” as a source of evidence, commonly referred
to as “electronic evidence”, following the 2006 Electronic
Transactions Law (ETL). According to the ETL, “data” refers
to information in the form of symbols, writings, numbers, im-
ages, sound, or similar formats, revealing that “electronic data”
is regarded as a source of evidence in electronic transactions.
Large Language Models (LLMs) [19], such as GPTs [12,
2, 11], have contributed significantly to advances in natu-
ral language processing tasks, including text classification,
sentiment analysis, and content generation, among others.
However, the potential of LLMs in the context of verifying
the authenticity of electronic evidence in legal proceedings
remains underexplored [17, 9, 8, 20]. Therefore, we propose
a novel dataset tailored to evaluating LLMs’ performance in
verifying electronic evidence.
Our dataset, RMDM, is designed to assess the capabilities
of LLMs in verifying electronic evidence in Vietnamese legal
proceedings. The dataset includes four labels: real, mis, dis,
and mal, which represent real information, misinformation,
disinformation, and mal-information as electronic evidence,
respectively.
By introducing a diverse set of labels for electronic evi-
dence, our RMDM dataset enables a more granular analysis of
various types of fake news. This multilabel approach captures
the complexities of differing fake news categories, which can
inform the development and evaluation of LLMs that are better
equipped to handle the varied nature of electronic evidence in
legal proceedings.
The main contributions of this paper are as follows:
• Development of a new dataset with four labels suitable
for evaluating various language models, such as GPTs and
BERT, in the context of verifying electronic evidence in
legal proceedings, capturing the complexities of differing
fake news categories and offering insights into their
abilities to handle various types of electronic evidence.
• Assessment of the electronic evidence verification ca-
pabilities of state-of-the-art generative models, including
ChatGPT (GPT-3.5) and GPT-4, providing an empirical
evaluation of their strengths and weaknesses in detecting
different fake news types.
• Identification of key challenges associated with language
models’ performance in verifying electronic evidence,
highlighting the need for further research and develop-
ment in AI models for legal applications and paving the
way for potential integration of external knowledge bases
and logical verifiers to enhance their understanding of
information and context.
II. BACKGROUND
The digital era has brought increasing importance to elec-
tronic evidence in legal proceedings. Electronic evidence can
encompass various forms of electronic data, including both
real and fake information. Fake news presents a significant
challenge in legal contexts, as it can be intentionally deceptive
and difficult to differentiate from legitimate electronic evi-
dence. Given the prevalence of fake news on social media and
arXiv:2309.09071v1  [cs.CL]  16 Sep 2023

--- Page 2 ---

other online platforms, the need for reliable methods to verify
electronic evidence, particularly in distinguishing between real
information and fake news, is critical for ensuring accurate and
fair decision-making in legal proceedings.
A. Definition of Fake News
Although there are many studies related to fake news, there
is no common and official definition for fake news. One of the
first definitions, widely used in many studies, was provided
by Shu et al. (2017) [14], which defined fake news as “fake
news is a news article that is intentionally and verifiably
false.” This definition limits the types of information in
fake news, intending to deceive users and disregarding some
misleading information. According to Siva Vaidhyanathan -
Professor of Communication at the University of Virginia,
author of “Antisocial Media: How Facebook Disconnects Us
and Undermines Democracy,” fake news is a piece of news
or information shared with the intent to confuse, deceive,
or undermine the trust of some people in the public. It can
be distorted information, inaccurate information, or entirely
fabricated stories and is often spread quickly on the network
by users’ sharing [18]. However, according to Claire Wardle,
co-founder and leader of First Draft 1, the term fake news
is not enough to describe the complexity of different types
of information phenomena. Instead, she divided it into three
types of information: Misinformation, Disinformation, and
Mal-information 2.
B. Classification of Fake News
Fake news exists in various forms, so classifying fake news
is not an easy task. There are many studies on the classification
of fake news. The authors introduce the classification of fake
news according to Claire Wardle [22]. Accordingly, fake news
is divided into the following three categories:
1) Misinformation [23, 15, 7]: Misinformation is created
but not intended to harm, including the following two
types:
• False connection: When the headline, image, or
caption does not match the content. For example,
information that is not entirely false can be distorted
using misleading or sensational headlines.
• Misleading content: Using incorrect information and
causing misunderstanding for the reader. For ex-
ample, the statement “Scientists claim that eating
chocolate every day can help you lose weight” can
be misleading to readers. Some studies have sug-
gested that chocolate may have health benefits, such
as improving cardiovascular health and reducing
stress, but there is no scientific evidence to support
the claim that eating chocolate every day can help
you lose weight.
1https://firstdraftnews.org/
2https://money.cnn.com/2017/11/03/media/claire-wardle-fake-news-
reliable-sources-podcast/index.html
2) Disinformation [4, 5]: Inaccurate information, created
and shared by those who intend to harm, includes the
following types:
• False context: Verified information is shared with
false information about the context (adjusted in
dangerous ways). For example, a video circulated
on social media showing the screams of a female
student in school, with the introduction that the
screams were due to harassment. However, it was
just the screams of a female student who could not
control her emotions in an argument.
• Imposter content: False information is created and
circulated to impersonate someone or an organiza-
tion by using their famous features. This form is
often used to deceive, steal information, and affect
the reputation and credibility of the person being
impersonated. A common example is impersonating
bank employees or police officers to call the victims
and get their personal information to seize assets in
bank accounts or savings.
• Manipulated content: When some aspects of the
original content are changed. This usually involves
images or videos. For example, when intention-
ally spreading false information about a celebrity
scandal, a commonly used trick is photo editing
or modifying the original image to illustrate the
content.
• Fabricated content: 100% false content designed to
fabricate and cause harm. This type of fabricated
content is often created and spread with the goal of
attracting attention or generating clicks, rather than
providing accurate and truthful information. For
example, “Tran Thanh and many other Vietnamese
stars have embezzled charity money for the Central
region” is fabricated content and has no basis in
reality, as there is no evidence or foundation to
verify the accuracy of this information.
3) Mal-information [21, 1]: True information that has been
reconfigured or manipulated in a way that is misleading
or harmful. It includes:
• Leaks: Leaking information is an event that occurs
when secret information is disclosed to unauthorized
persons or parties. For example, in US presidential
elections or before Party congresses in Vietnam,
there are often many pieces of information be-
lieved to be leaked from confidential documents
and almost impossible to verify. This information
often causes confusion and creates many conflicting
public opinions.
• Harassment: Any behavior, whether through speech,
images, text, or otherwise, intended to offend or
humiliate an individual or organization. With social
media, harassment is becoming more prevalent and
sophisticated. For example, fan pages of celebrities
often spread information to discredit competitors

--- Page 3 ---

and raise their idol’s image.
• Hate speech: Content expressed through speech,
text, or other expressions that show hatred or
ridicule towards a person or other people. Hate
speech often targets a social group defined by at-
tributes such as race, ethnicity, gender, or sexual
orientation.
C. Overview of Some Vietnamese Fake News Datasets
In this section, we briefly discuss a few existing Vietnamese
fake news datasets as a foundation and reference for develop-
ing our dataset:
• VFND [16]: Vietnamese Fake News Dataset. This dataset
includes 2,070 news articles collected between 2017 and
2019, comprising 1,035 fake news articles and 1,035
real ones. The news articles were classified as real or
fake based on various sources, cross-referencing the cited
sources, or community-based classification.
• VNTC [6]: A Large-scale Vietnamese News Text Clas-
sification Corpus. This dataset encompasses 2,010 news
articles with 1,005 fake news articles and 1,005 real ones,
gathered from various sources, including social media
and online forums, covering an array of topics such as
politics, health, and entertainment.
• VLSP Fake News: Part of a shared task organized by
the Vietnamese Language and Speech Processing group
over several years, this dataset contains both fake and real
news articles in Vietnamese. It focuses on political news
gathered from various sources, including social media,
and has been manually labeled. The dataset consists of
8,170 news articles, including 2,040 fake news articles
and 6,130 real ones.
A key limitation of existing Vietnamese fake news datasets,
such as VFND, VNTC, and VLSP Fake News, is that they
predominantly focus on binary classification, which may over-
simplify the complexity of fake news types. To address this,
our RMDM dataset introduces four distinct labels - real, misin-
formation, disinformation, and mal-information - representing
a diverse range of information and intent. This more com-
prehensive classification enables a deeper understanding of
various fake news categories and promotes the development of
robust models suitable for broader applications, particularly in
legal contexts where verifying electronic information accuracy
and credibility is crucial. For instance, having four distinct
labels allows for better identification of electronic evidence
that may have been manipulated with malicious intent, as well
as evidence that may simply contain unintentional errors, thus
providing a more accurate basis for decision-making in legal
proceedings.
III. DATASET
A. Dataset Overview
The dataset, referred to as RMDM, consists of 1556 sam-
ples, with each sample containing two fields: text and label.
The details of these fields are as follows:
Fig. 1. Distribution of word count in the text field across the entire dataset.
The horizontal axis represents the number of words, while the vertical axis
represents the number of documents.
Fig. 2.
Distribution of word count in the text field for the real label.
The horizontal axis represents the number of words, while the vertical axis
represents the number of documents.
• text: a short snippet containing news information.
• label: the label of the sample, which belongs to one of
the following four categories: real, mis, dis, and mal.
The label field comprises: 1) real: representing true or legit-
imate news sources; 2) mis: denoting misleading information
that causes confusion for readers; 3) dis: indicating fabricated
and deliberately harmful news; and 4) mal: referring to leaked
information that deliberately causes harm. The dataset includes
389 samples for each label.
B. Text Field Description
The average word count in the text field is 31, with the
longest sentence having 78 words and the shortest having 9.
The distribution of word count in the text field for the entire
dataset with varying lengths is illustrated in Figure 1.
1) Real Label: The average word count in the text field
for the real label is 30, with the longest sentence having 67
words and the shortest having 10. The distribution of word
count in the text field for the real label with varying lengths
is illustrated in Figure 2.

--- Page 4 ---

Fig. 3.
Distribution of word count in the text field for the mis label.
The horizontal axis represents the number of words, while the vertical axis
represents the number of documents.
Fig. 4.
Distribution of word count in the text field for the dis label.
The horizontal axis represents the number of words, while the vertical axis
represents the number of documents.
2) Mis Label: The average word count in the text field for
the mis label is 30, with the longest sentence having 67 words
and the shortest having 9. The distribution of word count in the
text field for the mis label with varying lengths is illustrated
in Figure 3.
3) Dis Label: The average word count in the text field for
the dis label is 28, with the longest sentence having 67 words
and the shortest having 9. The distribution of word count in
the text field for the dis label with varying lengths is illustrated
in Figure 4.
4) Mal Label: The average word count in the text field for
the mal label is 40, with the longest sentence having 78 words
and the shortest having 9. The distribution of word count in the
text field for the mal label with varying lengths is illustrated
in Figure 5.
The four-label structure of the RMDM dataset allows for
a more comprehensive understanding of the characteristics,
nuances, and interrelations of different types of electronic
evidence. By incorporating this diverse set of labels, we aim to
simulate the complexity and variety that LLMs may encounter
in real-world legal scenarios, which could contribute to a more
Fig. 5.
Distribution of word count in the text field for the mal label.
The horizontal axis represents the number of words, while the vertical axis
represents the number of documents.
accurate and robust verification of electronic evidence.
C. Label Field Description
We assigned 388 samples for each label. The false news
types with labels mis, dis, and mal were created by altering
the true news - news with the real label. The team built the
dataset using the following steps:
First, true news snippets, labeled as real, were extracted
from reputable sources, specifically from Vietnamnet and VTV
websites. The news information was selected from various
domains, including domestic and international news, business
news, sports news, healthcare news, and technology news. The
time frame of the snippets mainly falls within the years 2019
and 2020.
Next, for each of the three types of false news, we created
false news from true news. For samples with the mis label, the
text field was populated by slightly altering some information
(but not the entire content) in the samples with the real label.
The team changed information that was deemed to have little
impact on the content, such as dates, locations, etc. This
resulted in samples that contain both types of misleading
information - causing confusion and incorrect connections.
For samples with the dis label, the text field was created
by changing almost all the information or turning it into a
negation of the samples with the real label. These samples
with the dis label mainly fall into the categories of fabricated
and counterfeit information. For samples with the mal label,
we added some judgmental or sarcastic sentences to the
samples with the real label, thus primarily creating divisive
information.
IV. EXPERIMENT
A. Experiment Setup
To construct the baseline model for the dataset, state-of-
the-art models such as chatGPT (GPT 3.5) and GPT-4, or
the model with classic BERT architecture [3] and pre-trained
parameters Multilingual-BERT 3 have been employed. The
3https://huggingface.co/bert-base-multilingual-cased

--- Page 5 ---

Fig. 6. Confusion matrix of ChatGPT (GPT-3.5) in percentage format.
Fig. 7. Confusion matrix of GPT-4 in percentage format.
objective of these experiments is to assess the effectiveness of
the most prevalent language models on the task of determining
how well these state-of-the-art models can verify electronic
evidence in the context of Vietnamese legal proceedings.
Evaluating the performance of advanced language models
on the RMDM dataset, which consists of four distinct labels,
sheds light on their success and shortcomings in dealing
with different types of electronic evidence. This multilabel
evaluation indicates the adaptability and reliability of LLMs
in verifying electronic evidence and understanding the com-
plexities of fake news categories, demonstrating the value of
four-label datasets in advancing AI applications in the legal
domain.
B. Results and Analysis
Figures 6, 7, and 8 illustrate the confusion matrices for
ChatGPT, GPT-4 models and BERT-based model with pre-
trained Multilingual BERT respectively, presented in percent-
age format.
The revised results and analysis based on the actual confu-
sion matrices demonstrate that all models indeed struggle to
accurately predict fake news labels, with a strong bias towards
classifying most information as real news.
For ChatGPT:
Fig. 8. Confusion matrix of Multilingual-BERT based in percentage format.
• 25% of samples were correctly labelled as real news.
• 23% of samples were misclassified from misinformation
(mis) to real news.
• 20% of samples were misclassified from disinformation
(dis) to real news.
• 18% of samples were misclassified from mal-information
(mal) to real news.
For GPT-4:
• 25% of samples were correctly labelled as real news.
• 23% of samples were misclassified from misinformation
(mis) to real news.
• 16% of samples were misclassified from disinformation
(dis) to real news.
• 11% of samples were misclassified from mal-information
(mal) to real news.
For BERT-based model with Multilingual-BERT parame-
ters:
• 5% of samples were correctly labelled as real news.
• 3% of samples were misclassified from misinformation
(mis) to real news.
• 6% of samples were misclassified from disinformation
(dis) to real news.
• 1% of samples were misclassified from mal-information
(mal) to real news.
The models performed poorly in differentiating between
mis, dis, and mal news types. This consistent bias towards
real news reveals the models’ lack of a proper understanding of
fake news and highlights the difficulty in effectively detecting
various fake news types.
The observed limitations of these advanced language models
in verifying electronic evidence raise critical challenges for
their application in the field of AI and Law. To overcome these
challenges, one potential solution is to incorporate external
knowledge bases and logical verifiers into the LLMs [13, 10].
Such integration could provide models with additional context
and factual information, enhancing their ability to verify the
authenticity of the input data.
As LLMs, such as ChatGPT and GPT-4, become increas-
ingly popular in various fields, addressing these challenges

--- Page 6 ---

with comprehensive datasets and improved solutions becomes
essential. Further investigation into methods and techniques to
improve electronic evidence verification capabilities is crucial
to responsibly harness AI and law applications.
V. CONCLUSIONS
In conclusion, the RMDM dataset evaluates the performance
of language models, such as GPTs and BERT, in verifying
electronic evidence in Vietnamese legal proceedings. This
multilabel dataset captures the complexities of fake news
categories and highlights the limitations of state-of-the-art
models in this context. The findings emphasize the need for
further research and improvements in AI models for legal
applications, and the potential integration of external knowl-
edge bases and logical verifiers to enhance language models’
understanding of information and context.
ACKNOWLEDGEMENT
Hai-Long Nguyen was funded by the Master, PhD Scholar-
ship Programme of Vingroup Innovation Foundation (VINIF),
code VINIF.2022.ThS.050.
REFERENCES
[1] D. Baines, R. J. Elliott, et al. Defining misinformation,
disinformation and malinformation: An urgent need for
clarity during the covid-19 infodemic. Discussion papers,
20(06):20–06, 2020.
[2] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Ka-
plan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry,
A. Askell, et al. Language models are few-shot learners.
Advances in neural information processing systems, 33:
1877–1901, 2020.
[3] J. Devlin, M. Chang, K. Lee, and K. Toutanova. BERT:
pre-training of deep bidirectional transformers for lan-
guage understanding. CoRR, abs/1810.04805, 2018. URL
http://arxiv.org/abs/1810.04805.
[4] D. Fallis. The varieties of disinformation. The philosophy
of information quality, pages 135–161, 2014.
[5] D. Fallis. What is disinformation? Library trends, 63(3):
401–426, 2015.
[6] V. C. D. Hoang, D. Dinh, N. Le Nguyen, and H. Q. Ngo.
A comparative study on vietnamese text classification
methods.
In 2007 IEEE international conference on
research, innovation and vision for the future, pages 267–
273. IEEE, 2007.
[7] J. Jerit and Y. Zhao. Political misinformation. Annual
Review of Political Science, 23:77–94, 2020.
[8] H.-T. Nguyen, M.-P. Nguyen, T.-H.-Y. Vuong, M.-Q. Bui,
M.-C. Nguyen, T.-B. Dang, V. Tran, L.-M. Nguyen, and
K. Satoh. Transformer-based approaches for legal text
processing. The Review of Socionetwork Strategies, 16
(1):135–155, 2022.
[9] H.-T. Nguyen, M.-K. Phi, X.-B. Ngo, V. Tran, L.-M.
Nguyen, and M.-P. Tu. Attentive deep neural networks
for legal document retrieval. Artificial Intelligence and
Law, pages 1–30, 2022.
[10] H.-T. Nguyen, F. Wachara, F. Nishino, and K. Satoh. A
multi-step approach in translating natural language into
logical formula. In Legal Knowledge and Information
Systems, pages 103–112. IOS Press, 2022.
[11] OpenAI. Gpt-4 technical report, 2023.
[12] A. Radford, J. Wu, R. Child, D. Luan, D. Amodei,
I. Sutskever, et al. Language models are unsupervised
multitask learners. OpenAI blog, 1(8):9, 2019.
[13] K. Satoh, K. Asai, T. Kogawa, M. Kubota, M. Nakamura,
Y. Nishigai, K. Shirakawa, and C. Takano. Proleg: an
implementation of the presupposed ultimate fact the-
ory of japanese civil code by prolog technology.
In
New Frontiers in Artificial Intelligence: JSAI-isAI 2010
Workshops, LENLS, JURISIN, AMBN, ISS, Tokyo, Japan,
November 18-19, 2010, Revised Selected Papers 2, pages
153–164. Springer, 2011.
[14] K. Shu, A. Sliva, S. Wang, J. Tang, and H. Liu. Fake
news detection on social media: A data mining perspec-
tive. ACM SIGKDD explorations newsletter, 19(1):22–
36, 2017.
[15] B. Swire-Thompson, D. Lazer, et al. Public health and
online misinformation: challenges and recommendations.
Annu Rev Public Health, 41(1):433–451, 2020.
[16] H. Q. Thanh and Ninh-Pm-Se.
thanhhocse96/vfnd-
vietnamese-fake-news-datasets.
a
collection
of
viet-
namese articles and facebook posts classified into two
labels real - fake (228 articles), 2019.
URL https:
//zenodo.org/record/2578917.
[17] N. H. Thanh, B. M. Quan, C. Nguyen, T. Le, N. M.
Phuong, D. T. Binh, V. T. H. Yen, T. Racharak,
N. Le Minh, T. D. Vu, et al. A summary of the alqac
2021 competition. In 2021 13th international conference
on knowledge and systems engineering (kse), pages 1–5.
IEEE, 2021.
[18] S. Vaidhyanathan.
Antisocial media: How Facebook
disconnects us and undermines democracy.
Oxford
University Press, 2018.
[19] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit,
L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin.
Attention is all you need. Advances in neural information
processing systems, 30, 2017.
[20] Y. T.-H. Vuong, Q. M. Bui, H.-T. Nguyen, T.-T.-T.
Nguyen, V. Tran, X.-H. Phan, K. Satoh, and L.-M.
Nguyen. Sm-bert-cr: a deep learning approach for case
law retrieval with supporting model.
Artificial Intelli-
gence and Law, pages 1–28, 2022.
[21] C. Wardle, H. Derakhshan, et al. Thinking about ‘in-
formation disorder’: formats of misinformation, disinfor-
mation, and mal-information. Journalism,‘fake news’&
disinformation, pages 43–54, 2018.
[22] C. Wardle et al. Information disorder: Toward an inter-
disciplinary framework for research and policy making
(2017). 2017.
[23] J. D. West and C. T. Bergstrom. Misinformation in and
about science. Proceedings of the National Academy of
Sciences, 118(15):e1912444117, 2021.

```
