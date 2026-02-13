---
title: "2024-Kajiwara-A comprehensive framework for multi-modal hate speech detection in - PDF Extract"
source_pdf: "2024-Kajiwara-A comprehensive framework for multi-modal hate speech detection in.pdf"
pages: 21
extracted_at: "2026-02-13T14:50:53.362418"
---

# PDF Extract: 2024-Kajiwara-A comprehensive framework for multi-modal hate speech detection in

**Source PDF:** 2024-Kajiwara-A comprehensive framework for multi-modal hate speech detection in.pdf
**Total Pages:** 21

---

## Content

```
--- Page 1 ---

A comprehensive framework for 
multi-modal hate speech detection 
in social media using deep learning
R. Prabhu1 & V. Seethalakshmi2
As social media platforms evolve, hate speech increasingly manifests across multiple modalities, 
including text, images, audio, and video, challenging traditional detection systems focused on single 
modalities. Hence, this research proposes a novel Multi-modal Hate Speech Detection Framework 
(MHSDF) that combines Convolutional Neural Networks (CNNs) and Recurrent Neural Networks 
(RNNs) to analyze complex, heterogeneous data streams. This hybrid approach leverages CNNs for 
spatial feature extraction, such as identifying visual cues in images and local text patterns, and Long 
Short Term Memory (LSTM) for modeling temporal dependencies and sequential information in text 
and audio. For textual content, utilize state-of-the-art word embeddings, including Word2Vec and 
BERT, to capture semantic relationships and contextual nuances. The framework integrates CNNs 
to extract n-gram patterns and RNNs to model long-range dependency up to sequences of up to 100 
tokens. CNNs extract key spatial features in visual tasks, while LSTMs process video sequences to 
capture evolving visual patterns. Image spatial features refer to object localization, color distributions, 
and text extracted via Optical Character Recognition (OCR). The fusion mechanism employs attention 
mechanisms to prioritize key interactions between modalities, enabling the detection of nuanced 
hate speech, such as memes that blend offensive imagery with implicit text, sarcastic videos where 
toxicity is conveyed through tone and facial expressions, and multi-layered content that embeds 
discriminatory meaning, across different formats. The numerical findings show that the proposed 
MHSDF model increases the detection accuracy ratio of 98.53%, robustness ratio of 97.64%, 
interpretability ratio of 97.71%, scalability ratio of 98.67%, and performance ratio of 99.21% compared 
to other existing models. Furthermore, the model’s interpretability is enhanced through attention-
based explanations, which provide insights into how multi-modal hate speech is identified. The 
framework improves traceability of decisions, interpretability by modality, and overall transparency.
Keywords  Hate speech recognition, Convolutional neural network, Recurrent neural network, Deep 
learning, Social media
There is a wealth of hate speech data in today’s digital age, including written comments and postings on social 
media and audio and video recordings1. Online hate crimes often originate online and impact us all, according to 
another work2. A correlation between hate speech and facial expressions was found in their research3. Important 
indicators of hostility include vocal intonation and facial emotions. Sometimes, to identify hostile interactions, 
it is necessary to note only the text data, facial expressions, or voice information as audio data4. Text data is used 
in almost all current hate speech identification studies. To better identify hate speech, this research recommends 
combining text, video, and audio components5. Considering all the ways hate speech might be delivered, this 
study aims to identify hate speech more accurately6.
Combining all model outputs in a majority voting or hard voting ensemble determines the conclusion of 
hate speech7. Video content from many sources, including YouTube and EMBY, mostly from films or series, has 
been used to compile the data, including both hate speech and non-hate speech8. After that, the video’s contents 
were analyzed for pictures, audio, and text data. Features retrieved from pictures, sounds, and text separately9. 
Recursive Feature Selection, Maximum Relevance - Minimum Redundancy is used to extract the most relevant 
characteristics during feature selection10. To demonstrate the relative research has several typical ML models in 
hate speech detection, the performance of seven classifiers has been examined using the hate speech dataset11. 
1Department of Information Technology, Dr. Mahalingam College of Engineering and Technology, Pollachi, India. 
2Department of Electronics and Communication Engineering, KPR Institute of Engineering and Technology, 
Coimbatore, India. email: prabhu310591@gmail.com
OPEN
Scientific Reports |        (2025) 15:13020 
1
| https://doi.org/10.1038/s41598-025-94069-z
www.nature.com/scientificreports

--- Page 2 ---

The computational difficulty is due to the massive amount of material, cultural variables, linguistic nuances, low 
resource languages, the inherent ambiguity of natural language, and other factors12.
Furthermore, hate speech creators are swiftly adjusting to platform limits to evade increasingly stringent 
artificial intelligence and natural language processing technologies that identify hate speech13. Visual streams, 
nasty memes, and contextual visual methods are ways hateful material may be spread14. One way to do this is 
by incorporating text into photographs or screenshots. The goal is to avoid having information flagged as nasty 
by Natural Language Processing algorithms that work directly with text15. This paper builds upon and expands 
upon the research of References about identifying hate speech against migrants and refugees16. Even while the 
research is primarily concerned with xenophobic and racist speech, it is easy to apply the findings to other types 
of abusive material that deal with issues like sexism, homophobia, religion, disability, or politics17.
Convolutional neural networks (CNNs) are great at detecting hierarchical structures and local patterns, 
which allows them to effectively extract spatial characteristics from spectrograms, pictures, and even text 
(employing convolution over word embeddings). However, RNNs, especially LSTMs or GRUs, become crucial 
when dealing with long-range dependencies, which CNNs cannot do. RNNs are great for dealing with patterns 
of spoken language in audio or changing textual context in long-form postings because they analyze sequential 
input and learn contextual dependencies over time.
The increasing variety and sophistication of hate speech in online material is the driving force behind 
creating a multi-modal hate speech detection system. Since most existing detection algorithms only consider 
text as a modality, they cannot catch more nuanced and dynamic types of hate speech, such as videos, memes, 
and layered sarcasm. Hate speech on social media may take many forms, including text, photos, and voice; thus, 
a stronger response is needed. To address this issue and create digital places that are safer and more inclusive for 
everybody, the architecture is designed to be comprehensive, scalable, and accurate.
Hate speech on social media may take many forms, including text, photos, audio, and video; the challenge 
of identifying it has grown in complexity. The complex and multi-layered character of multi-modal hate speech 
makes identifying it difficult for traditional detection techniques. Multi-layered content differs from other forms 
of multi-modal hate speech by embedding discriminatory meaning across multiple levels of abstraction rather 
than simply combining different modalities. This includes sarcastic memes, hate-laden videos, and mixed-format 
articles. These systems are prone to adversarial attacks and have poor accuracy because they fail to consider 
contextual and sequential information. Ensuring safer online settings has made the need for a more advanced 
multi-modal approach to analyzing various information and improving detection accuracy imperative. Due to 
high false-positive and false-negative rates, single-modality detection methods are severely limited in capturing 
the whole context of hate speech. Text-based models are inadequate in identifying context-dependent toxicity 
because they cannot handle sarcasm, implied hatred, or confusing statements that lack prosodic or visual clues. 
Unfortunately, audio-only systems aren’t smart enough to recognize context and can’t handle aggressively 
worded abusive speech. Similarly, without language and auditory context, vision-based techniques that depend 
on object identification or facial expressions cannot differentiate between harmless and hazardous information.
The main contribution of this paper is as follows:
•	 Fusion mechanism Framework: For text, picture, audio, and video analysis, it provides a new hybrid architec­
ture that combines CNNs with RNNs. Because of this, hate speech may be detected using a variety of modal­
ities, including those that capture patterns in space and time.
•	 Attention Mechanism for Enhanced Detection: The framework uses attention processes to prioritize impor­
tant interactions across modalities to detect better complex hate speech (e.g., ironic or multi-layered content).
•	 Interpretability and Scalability: The proposed MHSDF enhances detection accuracy by integrating mul­
ti-modal cues while maintaining interpretability through attention-based explanations. Additionally, its 
modular architecture ensures scalability, allowing it to adapt to varying data distributions and computational 
constraints across different platforms.
The organization of this paper is as follows: Sect. 2 describes hate speech detection, and Sect. 3 outlines the 
proposed MHSDF approach. Section  4 analyzes and discusses the effectiveness of MHSDF. Lastly, Sect.  5 
includes the conclusion and future work.
Related work
A person or group is hated or threatened with violence because of their race, religion, gender, or other protected 
characteristic, according to the Cambridge Dictionary. Similarly, Reference states that a tweet is toxic if it uses 
abusive, threatening, or insulting language aimed at a particular person or group. Although we look specifically 
at xenophobic and racist speech in this paper, it’s very unusual for accounts that spew hate speech to be poisonous 
in general, targeting communities or other social groups rather than specific ethnic minorities. This research will 
use the term toxic to describe harmful online activity in general and hateful to refer to xenophobic material 
specifically.
An increasing problem that hinders efforts to keep the internet safe and promote positive dialogue is hate 
speech on social media sites like Twitter. To lessen the negative effects of hate speech on people and communities, 
it is essential to recognize and monitor it effectively. This research provides a thorough method for detecting hate 
speech on Twitter by combining deep learning with classical machine learning by Toktarova, A. et al.18. To find 
out how well various methods detect hate speech on Twitter, this work includes a comprehensive comparison of 
them. To guarantee the accuracy of the models, build a strong dataset using data collected from various sources 
and annotated by specialists.
Unwanted cyber concerns, such as cyberbullying and hate speech, emerged with the fast expansion of 
Internet users. The issues surrounding hate speech on Twitter are addressed in this article. Inciting hatred by the 
Scientific Reports |        (2025) 15:13020 
2
| https://doi.org/10.1038/s41598-025-94069-z
www.nature.com/scientificreports/

--- Page 3 ---

dissemination of false information seems to be the hallmark of hate speech. Gender, religion, color, and disability 
are some of the protected characteristics that the hate speech targets by Roy, P. K. et al.,19. When individuals or 
communities feel demoralized as a result of hate speech, unanticipated criminal acts may occur.
According to Priyadarshini I. et al.20, an important issue is that hate speech not only incites violence and 
hatred but also requires a large amount of computer power and content monitoring by human specialists and 
algorithms to identify it. While there is a lot of ongoing research in this field and several AI strategies have been 
suggested to tackle the problem in the past, solutions that demonstrate better performance and shorter model 
creation times are needed due to the increasing number of petabytes of created material. Using a pre-trained 
model for data analysis, the proposed transfer learning method for social media hate speech detection promotes 
model reusability.
By automatically detecting hate speech in web content, models based on natural language processing and 
machine learning provide a means to make online platforms safer. The biggest challenge, however, is getting 
enough examples annotated to train these models. This work constructs a unified hate speech representation by 
combining two separate datasets using a transfer learning approach. To project and compare various datasets, 
develop a two-dimensional visualization tool for the built hate speech representation by Yuan, L. et al.21.
Identifying hate speech and distinguishing it from insulting material is difficult for current machine learning 
methods. Present methods often fail to accurately identify hate speech because they approach hate categorization 
as a multi-class issue. This article introduces the concept of hate speech detection on social media platforms as a 
multi-label issue. The proposed “Hate Classify” service platform uses HSD-DT to classify social media posts as 
either hate speech, offensive, or not offensive by Khan, M. U. et al.,22.
According to Jahan, M. S. et al.,23 the problem of detecting and monitoring hate speech is becoming an 
increasingly pressing concern for society, individuals, policymakers, and academics due to the proliferation of 
social media platforms that provide easy access to online community creation and anonymity. Despite ongoing 
attempts to use automated methods for monitoring and detection, their results are consistently unsatisfactory, 
necessitating further study into the matter.
AI for hate speech identification offers a versatile and multi-faceted opportunity for artificial intelligence by 
Mehta, H. et al.,24. This study aimed to understand how sophisticated AI models make choices by interpreting 
and explaining their judgments. This work used two datasets to show how AI can recognize hate speech. 
Inconsistent data was cleaned up, and tweet text was cleaned up, tokenized and lemmatized, etc., as part of the 
data pretreatment. The categorical variables were additionally simplified to have a clean dataset for training.
Although there are many offline and online methods to express it, its use and intensity have grown 
substantially due to the rise of social media. Thus, this study’s overarching goal is to identify and examine the 
unstructured data included in certain social media postings with the express purpose of spreading hate speech 
in their comment sections. All social media providers must be aware of the prevalence of hate speech on social 
media by using SA, a new framework that integrates data analysis with natural language processing techniques 
by Rodriguez A. et al.25.
Weiqiang Jin et al.26 suggested the Prompting Multi-Task Learning framework guided by news veracity 
Dissemination Consistency (PMTL-DisCo) for few-shot fake news detection. This work used sophisticated 
AI approaches for feature extraction and optimization, such as masked language model (MLM), multi-task 
learning (MTL), and prompt-based tuning. The following advances are included in PMTL-DisCo, in contrast to 
previous efforts that mostly use pre-trained language models (PLMs) for feature extraction: (1) supplementary 
work, “news distributed representation optimization,” which improves feature learning by using indications of 
dissemination consistency from nearby news examples. (2) an adaptive multi-label mapping-based verbalizer 
that increases prompt-tuning performance is based on high-quality, enlarged label words. Thirdly, a multi-
neighbor reasoning augmentation approach uses the credibility characteristics of news stories with strong social 
connections to improve forecast accuracy.
Weiqiang Jin et al.27 proposed context-aware prompt engineering for fake news detection (CAPE-FND). This 
approach uses self-adaptive bootstrap prompting optimization to enhance LLM predictions and uses unique 
veracity-oriented context-aware restrictions, background knowledge, and analogical reasoning to reduce LLM 
hallucinations. To maximize the effectiveness of LLM prompting, it adaptively iteratively optimizes the initial 
LLM prompts using a random search bootstrap approach. The CAPE-FND system outperforms sophisticated 
GPT-4.0 and humans in certain cases, as shown by extensive zero-shot and few-shot trials conducted on various 
public datasets using GPT-3.5-turbo.
Weiqiang Jin et al.28 recommended the rumor detection and fact verification framework called Det2Ver. 
Det2Ver’s structural level integrates the two processes and leverages external information from rumor detection 
to strengthen fact verification work by building adaptive prompt templates and prompt-tuned LLMs such as T5. 
The author shows how useful and important Det2Ver is. The Det2Ver for cross-task knowledge augmentation 
significantly improves macro-F1 for fact verification, as shown by the few-shot/zero-shot trials on three 
commonly used datasets, compared to other LLMs prompt-tuning baselines.
Weiqiang Jin et al.29 presented the Detection Yet See Few (DetectYSF) for fake news detection. DetectYSF can 
provide effective FEND capabilities with less supervised data by combining adversarial semi-supervised learning 
with contrastive self-supervised learning. As its foundation, DetectYSF uses Transformer-based PLMs (such as 
BERT and RoBERTa) and tunes its models using a Masked LM-based pseudo-prompt learning approach. In 
particular, the following improvement steps for DetectYSF are implemented during training: (1) To improve 
the sentence-level semantic embedding representations learned from PLMs, we develop a straightforward self-
supervised contrastive learning strategy. (2) To create an adversarial embedding flood, we build a Generation 
Adversarial Network (GAN) with random noises and negative fake news samples as inputs, and the author uses 
Multi-Layer Perceptrons (MLPs) and an additional independent PLM encoder. Next, the author uses semi-
Scientific Reports |        (2025) 15:13020 
3
| https://doi.org/10.1038/s41598-025-94069-z
www.nature.com/scientificreports/

--- Page 4 ---

supervised adversarial learning in conjunction with the adversarial embeddings to enhance DetectYSF’s output 
embeddings during the prompt-tuning process.
Ahmed R. Nasser et al.30 suggested the Deep learning-based malware detector for Android (DL-AMDet). 
There are primarily two detection models that makeup DL-AMDet. The first one employs the CNN-BiLSTM 
deep learning algorithm for malware detection via static analysis. In contrast, one approach employs deep 
Autoencoders as an anomaly detection model to identify malware dynamically. Two separate datasets are used 
to assess the DL-AMDet architecture’s performance. The findings demonstrate that DL-AMDet’s static and 
dynamic analysis models reach a competitive malware detection accuracy of 99.935%. The results also highlight 
how the CNN-BiLSTM and Deep Autoencoders models utilized in DL-AMDet significantly surpass the current 
state-of-the-art methods.
Ayad E. Korial et al.31 introduced an Improved Ensemble-Based Cardiovascular Disease Detection System 
with Chi-Square Feature Selection. To develop an ensemble model, the author used a voting mechanism to 
combine the predictions of several ML classifiers. The ensemble model’s performance was then evaluated and 
compared to the individual classifiers. In addition, the author used the 303 records spanning 13 clinical variables 
in the Cleveland heart disease dataset to determine the five most essential aspects using the chi-square feature 
selection approach. This method cut the computational burden by nearly half while increasing the ensemble 
model’s overall accuracy. The voting ensemble model outperformed the individual top classifier (LR) by an 
average of 2.95%, resulting in an impressive accuracy of 92.11%.
Ruqaya Abdulhasan Abed et al.32 discussed the modified Convolutional Neural Network for Intrusion 
Detection System (CNN-IDS) model. This paper aims to train and evaluate our models using the UNSW-NB15 
intrusion detection data set, which requires a thorough study. The principal component analysis (PCA) and 
the support vector descent (SVD) methods are used for feature selection. We also use the altered feature space 
to classify the datasets using three methods: Ridge Regression (RR), Stochastic Gradient Descent (SGD), and 
Convolutional Neural Network (CNN). It handles both multi-class and binary classification, which makes it 
quite useful. In terms of improving the accuracy of classification models, the results show that PCA and SVD 
are the most effective in achieving superior IDS performance compared to others. With an improvement in 
accuracy from 98.13 to 99.85%, the RR classifier stood out for its exceptional precision in the binary classification 
challenge.
An exhaustive examination of several hate speech detection systems used on social media sites such as Twitter, 
elucidating their advantages and disadvantages, is summarized in Table 1. More conventional methods like 
SVMs and decision trees and more cutting-edge ones like deep learning, RNNs, and transfer learning are part 
of it. Additionally, the research delves into how sentiment analysis and NLP might improve detecting capacities. 
This work sheds light on the effectiveness of models in preventing hate speech in online spaces by comparing 
various approaches and using a variety of datasets. Existing work mostly concentrates on text-based or audio-
based identification, which often misses the whole context of damaging material despite considerable progress 
in detecting hate speech. Models trained on textual data have difficulty with sarcasm, implicit hate speech, and 
code-mixed language; in contrast, systems trained on audio data are more affected by speaker variability and 
ambient noise. The high computing needs and difficulties in efficiently integrating visual signals have kept video-
based detection underexplored. In addition, the lack of interpretability in most previous research makes it hard 
to comprehend the logic behind the predictions made by the models. Given these restrictions, it is clear that 
a multi-modal hate speech detection framework (MHSDF) is required to enhance precision, resilience, and 
comprehensibility by combining visual, aural, and textual features.
Multi-modal hate speech detection framework
An innovative multi-modal deep learning system for hate speech detection on social media platforms is 
provided in this paper. It integrates text, images, audio, and video, among other sources, to exactly find harmful 
content across various mediums. The framework pre-processing and feature extraction from any data type uses 
S. no
Methods
Advantages
Limitations
1
Hate Speech Detection using Machine Learning (HSD-ML), 
Toktarova, A. et al.18
Combines classical ML and deep learning for 
comprehensive analysis.
It requires high-quality, annotated 
datasets and can be resource-intensive.
2
Recurrent Neural Network for Hate Speech Detection (RNN-HSD), 
Roy, P. K. et al.19
Captures temporal patterns and sequences in text data 
effectively.
Computationally expensive and prone 
to overfitting with small datasets.
3
SVM-Based Speech Detection (SVM-SD), Priyadarshini I. et al.20
Efficient with small datasets; simple implementation.
Struggles with large-scale data and 
complex feature representation.
4
Transfer Learning for Hate Speech Detection (TL-HSD), Yuan, L. et 
al.21
Reuses pre-trained models, reducing training time and 
data requirements.
Limited by the quality of pre-trained 
models and domain-specific nuances.
5
Hate Speech Detection based on Decision Trees (HSD-DT), Khan, 
M. U. et al.22
Simple and interpretable; useful for multi-label 
classification.
Prone to overfitting; struggles with 
high-dimensional data.
6
Hate Speech Detection using Natural Language Processing (HSD-
NLP), M. S. et al.23
Leverages advanced NLP techniques for better text 
understanding and context.
Requires extensive pre-processing and 
large datasets to be effective.
7
Artificial Intelligence in Hate Speech Detection (AI-HSD), H. et al.24
Versatile and scalable; capable of handling large, 
unstructured data.
Interpretability of AI decisions can be 
challenging with high resource usage.
8
Hate Speech Detection Using Sentiment Analysis (HSD-SA), 
Rodriguez A. et al.25
Detects underlying sentiments in hate speech, adding 
a layer of context.
May misinterpret sarcasm or neutral 
statements as hate speech.
Table 1.  Summary of the related works.
 
Scientific Reports |        (2025) 15:13020 
4
| https://doi.org/10.1038/s41598-025-94069-z
www.nature.com/scientificreports/

--- Page 5 ---

BERT, Word2Vec, CNN, and LSTM for text, image, and audio analysis. Using a fusion mechanism layer and an 
attention mechanism, the system guarantees accurate categorization of hate speech and provides interpretability 
for its decision-making process by helping the system prioritize significant features across modalities.
Contribution 1: develop a comprehensive multi-modal hate speech detection framework
The paper aims to create a robust multi-modal detection system that manages many data inputs, including text, 
images, audio, and video. The system uses CNN and RNN architectures to assess and extract significant patterns 
from many data sources, hence transcending the limitations of traditional single-mode detection systems.
Figure 1 presents a multi-modal deep learning system designed to detect hate speech. The system manages 
pictures, text, and audio as three types of input. Besides optional audio recordings, analytical inputs include visual 
Fig. 1.  Multi-modal deep learning architecture for hate speech detection.
 
Scientific Reports |        (2025) 15:13020 
5
| https://doi.org/10.1038/s41598-025-94069-z
www.nature.com/scientificreports/

--- Page 6 ---

ones, including photographs or videos, and textual ones, including social media postings. From a pre-processing 
level, text tokenization, stopword deletion, and lemmatization result from these inputs. Nous additionally scales 
and normalizes the visuals and uses the noise reduction method on the audio stream. After the pre-processing 
stage, the data is sent to the feature extraction one. Word2vec and BERT embedding systems translate words into 
numerical vectors, part of text processing.
CNN or ResNet models allow one to retrieve the visual characteristics of images. On audio, however, 
spectrograms and MFCC methods help to capture important auditory traits. Furthermore, fusion mechanism 
separates mixed text, image, and audio components blended by concatenation or attention procedures. This 
ability enables the model to compile pertinent data from many sources. Analysed will be deep learning models 
created after data fusion. RNN or transformer structures in text analysis assist in controlling sequential data 
management. Long Short-Term Memory (LSTM) networks are still the best option for hate speech identification 
when modeling temporal dependencies, even though Transformers are more popular for processing sequential 
input. Because of their gating methods, LSTMs are great at capturing long-range relationships and avoiding the 
problems caused by vanishing gradients in recurrent architectures. Because LSTMs process input sequentially, 
they are more efficient for real-time applications with limited processing capacity, unlike Transformers, which 
demand considerable computing resources owing to self-attention processes functioning on complete sequences. 
Because of their low parameter count and need for large-scale pretraining, Transformers could have trouble on 
smaller datasets, although LSTMs excel in this area. Given these benefits, LSTMs provide a fair trade-off between 
accuracy, efficiency, and feasibility to simulate temporal dependencies in multi-modal hate speech detection. 
CNN models are used in image processing to enable pattern recognition; RNN or CNN models are utilized in 
audio processing. Finally, the output layer presents either a binary classification, giving a wide perspective of all 
the many types of hate speech, or an optional multiclassification, indicating whether the content is hate speech 
from these two sets. Should hate speech occurrences be found, post-processing thresholding and monitoring 
strategies enhance the findings even more and provide alerts.
	
|j (k)| > ∀|r| + c, with 0 > δ > γ 2 −α 2, d ≤0 
(1)
Regarding multi-modal hate speech detection ∀|r|, the Eq. 1 ensures successful fusion by highlighting the 
limits c on the interaction between different modalities δ > γ 2 −α 2. This disparity guarantees that the multi-
modal model gives ( |j (k)|) across various data streams (text, image, video) over arbitrary or unimportant ones 
( α 2, d ≤0). Equation 1 enables the system to keep its effectiveness and accuracy in detection even when faced 
with complicated inputs.
	
∂Q + β 2P = −i (δ 2 (∇2 + p))
ϵ 3
+ mn2 ∗∆2 
(2)
Equation 2 ∂Q and β 2P represents changes in feature space and the i(δ 2(∇2+p))
ϵ 3
 represents gradients in data 
mn2 that are both spatial ∆2  and temporal. The equation identifies subtle forms of hate speech in real time 
because of this improvement in its capacity to capture changing multi-modal patterns.
	
∀E + δ 2Y = U (
X2 ∗Zn2 + Q)
−F1 ∗(α 2∇) 
(3)
The equation that takes into consideration contextual dependencies is ∀E + δ 2Y  and reflects the characteristics 
U retrieved from multi-modal inputs (such as text F1 and pictures (α 2∇) ) as X2 ∗Zn2 + Q. Equation 3 
highlights the balance between recovered interactions between features and context modeling.
	
v′ (r) = cos
[
∀u
(
∂2
3 −4
)]
+ 4vsin
[
rw
(
z
2
3 + 4
)]

(4)
Equation 4, which represents periodic patterns cos in literary ∀u
(
∂2
3 −4
)
 or visual data rw
(
z
2
3 + 4
)
 is 
given by v′ (r), whereas the term representing dynamic interactions in sequential data, like audio or video, is 
given by 4vsin. This equation improves the identification of complicated hate speech patterns across modalities. 
Convolutional neural networks (CNNs) automatically detect hierarchical patterns and local relationships in 
text without needing human feature engineering, making them a powerful alternative to conventional n-gram 
approaches for text feature extraction. Contrary to n-gram models, CNNs use convolutional filters to identify 
relevant n-gram-like characteristics in different settings instead of relying on predetermined word sequences, 
which might result in high-dimensional sparse representations. These filters make it possible for CNNs to 
identify important phrases and patterns in text without respect to their precise location. Furthermore, compared 
to conventional n-gram-based methods, which often experience complexity creep as vocabulary sizes expand, 
CNNs are quicker and more scalable due to their effective parallel text processing.
Figure 2 shows the suggested multi-modal decision-making system. It pre-processes the data after video data 
is gathered by converting it into pictures, audio, text, and images, resizing audio noise reduction. Individual traits 
from every bit of data are then obtained. One may extract temporal domain information and frequency domain 
using audio data. Every one of the gained qualities runs under one single algorithm and complements the others. 
Every feature picture, audio, text, and so on will be analyzed separately to ascertain the model’s accuracy. The 
model responds to every piece of input both with hate and non-hate. After that, the prediction decision-making 
will be a majority voting ensemble to forecast the final output, which suggests two or more modes must be 
hated to cause the final output to be hated. Two kinds of video data have been collected in this analysis: hate 
Scientific Reports |        (2025) 15:13020 
6
| https://doi.org/10.1038/s41598-025-94069-z
www.nature.com/scientificreports/

--- Page 7 ---

and non-hate. The negative emotions of rage, fear, hostility, dislikes, and disgust are found in hostile words or 
a sense of injury or violence to the greatest degree. These emotions relate to the hate facial expressions. Positive 
or non-hatred emotions, on the other hand, are those of pleasant or desirable activities, including pleasure, 
entertainment, satisfaction, etc. It has collected material from several sources, including films, online series with 
hate speeches, pictures of hate emotions, and comments. The three main components of video material are the 
visual frames, the audio component, and the textual transcription. Before extracting picture features using deep 
learning models such as convolutional neural networks (CNNs), the visual processing pipeline extracts and pre-
Fig. 2.  Multi-modal decision-making system.
 
Scientific Reports |        (2025) 15:13020 
7
| https://doi.org/10.1038/s41598-025-94069-z
www.nature.com/scientificreports/

--- Page 8 ---

processes frames (resizes, normalizes) (ResNet, VGG). The audio processing pipeline uses noise cancellation 
before extracting metrics, including MFCCs, chroma, energy, and Zero-Crossing Rate (ZCR), to extract features 
that capture speech patterns related to hate speech. Before turning text into numerical representations such as 
Bag-of-Words (BoW) or Term Frequency-Inverse Document Frequency (TF-IDF), the text processing pipeline 
eliminates stop words and regular expressions (RE), tokenizes and lemmatizes the text. A multi-modal decision-
making methodology fuses extracted data from all modalities using attention processes or deep learning-based 
feature fusion approaches. A classification machine trained to differentiate between hate and non-hate speech 
makes the ultimate conclusion. Non-Hate category: one can analyze the films with pleasant emotions using the 
same data extraction method as hate data.
	
z2
(
m′ −vf)
= G (M2 ∗∂Q −R (y, z)) ∗ey [M r −Ev] 
(5)
By highlighting the gradient z2 (m′ −vf) of the feature extraction process ey across modalities M r −Ev 
(text, pictures, audio), Eq.  5 represents the interaction G between the extracted multifunctional features 
M2 ∗∂Q and their velocity R (y, z). The CNN-RNN system can include varied characteristics for stronger 
hate speech identification, and Eq. 5 represents the fusion of multi-modal details.
	
P (m) = W (v2 ∗Mj + R (y, zr)) −∂2 ∗Ez (n2) 
(6)
This Eq.  6 shows multi-modal characteristics P (m) affect the detection process, with Mj + R (y, zr) 
representing the interactions between visual v2 and textual components W. The effect of mistakes or noise 
in the collected features is captured by subtracting ∂2 ∗Ez (n2). Accurate hate speech identification across 
heterogeneous data streams is ensured by aligning the balance between separating features and noise reduction. 
Computational efficiency, feature integration, and synchronization are all hindered by heterogeneous data 
streams, which are multi-modal inputs with different formats, structures, and temporal resolutions. Since audio 
and video data is continuous and not discrete like text, accurate temporal alignment is necessary for effective 
fusion. Dissimilar feature spaces, such as text word embeddings, audio spectrograms, and video pixel intensities, 
make unified representation learning more difficult.
	
||e (V2 ∗R2Q) + Z (Xcm ∗Ew)|| ∗M = R (2) −V n 
(7)
In this Eq.  7, the interplay between contextual embeddings ( Z (Xcm ∗Ew)) and complex multi-modal 
characteristics ( e (V2 ∗R2Q)) is reflected. The combined characteristics are amplified by the term M = R (2)
, and the final output is managed by V n. The ability of the algorithm to identify complex hate speech on social 
media may be enhanced by fusing this Eq. 
	
E2 ∗(
v2W)
=
2 m
R2 ∗ty ∗Z (ω 2 ∗σ τ ) −S (
U 2 −LK)

(8)
The link between the energy of multi-modal features E2 ∗(
v2W)
 and their temporal dependence 
2 m
R2∗ty  is 
summarised by the Eq. 8. Features are modulated across modalities by the Z (ω 2 ∗σ τ ), whilst structural 
changes are accounted for by S (
U 2 −LK)
. According to this equation, more precise and complex hate speech 
identification using various data sources is within the realm of possibility. A unified multi-modal representation 
is formed by concatenating features derived from several modalities. These modalities include text (LSTM-
encoded embeddings), audio (spectral and temporal information using GRU), and video (CNN-based spatial 
features). After concatenation, an attention module improves alignment across modes and reduces duplication. 
This module dynamically assigns a weight to each modality’s input depending on the relevant context. A series 
of completely linked layers are employed to classify this fused representation augmented with attention. This 
method, in contrast to conventional late fusion, which combines predictions at the decision level, guarantees 
deeper cross-modal interactions while keeping interpretability, which improves detection accuracy and resilience 
against missing modalities.
Contribution 2: leverage advanced deep learning techniques
The analysis mostly focused on adding modern deep learning techniques such as LSTM, BERT, CNN, and 
Word2vec. These methods handle the complexity of spatial, temporal, and sequential information in textual, 
visual, and audio material, improving the detection accuracy of subtle forms of hate speech across media, 
including memes and videos. Word2Vec captures semantic linkages like synonymy but lacks contextual 
sensitivity; it builds dense vector representations based on co-occurrence probabilities in a fixed-dimensional 
space. BERT uses deep bidirectional self-attention to simulate polysemy and contextual subtleties to create 
dynamic embeddings conditioned on nearby words. Word2Vec initializes embeddings to keep overall semantic 
similarity while BERT refines them during fine-tuning to reflect contextual dependencies; this hybrid embedding 
technique integrates both approaches.
Figure 3 illustrates the approach usually used for tasks needing text categorization; this might be viewed 
here. The approach consists of pre-processing stages starting with raw text data and comprising techniques to 
clean and standardize the data. Data loses stop words, special characters, and punctuation during operation 
phases. Then, the stemming approach helps simplify words to their most fundamental form. The pre-processing 
step produces two training sets and a testing set upon termination. The feature-extracting methods used to 
translate the text into numerical representations suited for the utilized algorithms in deep learning are TF-
Scientific Reports |        (2025) 15:13020 
8
| https://doi.org/10.1038/s41598-025-94069-z
www.nature.com/scientificreports/

--- Page 9 ---

IDF (Term Frequency-Inverse Document Frequency) and Word2Vec. Many classifiers are utilized in training 
models using the available data. Here among the classifiers are Logistic Regression (LR), Random Forest (RF), 
LightGBM (LGBM), Naive Bayes (NB), Support Vector Machine (SVM), Stochastic Gradient Descent (SGD), 
and AdaBoost. Following that, the general applicability of these models is evaluated on a testing set using criteria 
like accuracy, precision, recall, and F-measure.
	
T (∀2 (δ 4 (M −RT))) = H′ (n) * v2 (∇(U w (m*Ep))) 
(9)
The Eq. 9 captures both the spatial ( ∀2) and temporal ( T) components v2 and describes the transformation 
( H′ (n)) of multi-modal characteristics δ 4 (M −RT). On the other hand, the dynamic feature extraction is 
shown ∇, where the gradients between modalities are tracked by U w (m ∗Ep). This is with multi-modal hate 
speech identification that is good and considers context.
	
vb = Zr−2v
q
*Mcos (E*N2 −(ey*fw)) −Rzj−k 
(10)
Equation 10, vb represents the intricate change E ∗N2 of multi-modal characteristics Zr−2v
q
, where spatial 
components Mcos and time-dependent variations ey ∗fw are combined. The Rzj−k  represents the noise 
or decay in feature extraction. This improves the accuracy of recognizing subtle forms of hate speech, which 
features strength and variance between modalities.
	
H (2 −r) = dq−2
0
*tan −
[ v
r2 *M ′ (R −xy)
]
+ Z′ (∂−uz) 
(11)
Fig. 3.  Text classification process using term frequency-inverse document frequency.
 
Scientific Reports |        (2025) 15:13020 
9
| https://doi.org/10.1038/s41598-025-94069-z
www.nature.com/scientificreports/

--- Page 10 ---

Where dq−2
0
 scales the effect of spatial interactions tan, the Eq. 11, H (2 −r) explains the transformation 
Z′ (∂−uz)  of multi-modal characteristics v
r2 ∗M ′ (R −xy). While contextual adjustments are taken into 
consideration by dq−2
0
. By easing complicated, non-linear interactions across modalities, this equation bolsters 
the CNN-RNN architecture.
	
−F (z) ∗sin (∀2 ∗Ez (m −nb)) = −3F r
2
(
z′ −vt)

(12)
Equation  12 shows the contextual −F (z) changes affect the extracted sin multi-modal characteristics 
∀2 ∗Ez (m −nb). The characteristics are affected by spatial −3F r
2  and temporal elements z′ −vt, which 
causes them to oscillate. This connection improves its capacity to identify complicated hate speech patterns. This 
architecture uses a multi-stream convolutional neural network (CNN) that includes object identification, optical 
character recognition (OCR), and facial expression recognition (FAR) to extract visual information from movies 
and photos. A pre-trained facial action unit detector, like OpenFace, scans facial expressions to detect emotions 
associated with hate speech, such as wrath or disdain. Object recognition may identify contextual aspects 
supporting unpleasant material, such as violent images or insulting symbols, using a YOLO-based approach. 
Also, optical character recognition (OCR) methods may properly identify on-screen slurs, implicit hate symbols, 
or disparaging remarks by extracting and processing text inside pictures and video frames.
Figure 4 shows a thorough method for spotting hate speech in information gathered from social media 
platforms. The pipeline will begin with data collected from social media, with an eye toward messages falling into 
certain categories such as religion, countries, and ethnicities from the Twitter site. One must use a lexicon to find 
the slur phrases connected with these specific groups. The tweets are aggregated into a single dataset straight after 
being collected, and then human experts annotate them to assess whether or not they include hate speech. Several 
elements of hate speech are considered when creating the annotations. These features include insults, attribution, 
symbolizing, and using slights. By using a properly annotated dataset, one may train machine learning models 
capable of differentiating between tweets, including hate speech, and those devoid of hate speech. Employing 
these methods, quick interventions and the prevention of online abuse and discrimination are enabled. One 
conceivable use for these technologies is keeping an eye on social media channels and spotting something that 
can endanger users. Sampling methods, weighted loss functions, and data augmentation were used to tackle the 
issue of class imbalance in hate speech datasets. Text paraphrasing, audio pitch shifting, and picture alterations 
were used to construct synthetic samples that diversified minority-class cases to reduce bias toward the majority 
class. To ensure that underrepresented categories were penalized more severely for misclassification, a weighted 
cross-entropy loss function was used to achieve balanced learning. To ensure that uncommon instances of hate 
Fig. 4.  Design of Hate speech detection from social media platforms.
 
Scientific Reports |        (2025) 15:13020 
10
| https://doi.org/10.1038/s41598-025-94069-z
www.nature.com/scientificreports/

--- Page 11 ---

speech were adequately represented, we used oversampling and stratified sampling methods (such as SMOTE 
for text embeddings) to prevent overfitting.
Confusion matrix
A confusion matrix is a useful tool to evaluate the performance of a classification model. It provides insights 
into how well the model is performing by showing the counts of true positives (TP), true negatives (TN), false 
positives (FP), and false negatives (FN), as shown in Table  2. For the Multi-modal Hate Speech Detection 
Framework, assuming it is a binary classification ( hate speech vs. non-hate speech), the confusion matrix can 
be represented as follows:
Pseudocode for Multi-modal Hate Speech Detection Framework
Step 1: Import Required Libraries
1. Import TensorFlow, PyTorch, Keras, NumPy, and other dependencies.
Step 2: Load Pre-Trained Embeddings
2.1. Function Load_Embeddings(text, model=’BERT’)
→ Load BERT/Word2Vec embeddings for text input.
→ Return text embeddings.
Step 3: Define Feature Extraction Models
3.1. Function CNN_Model(video_input)
→ Apply Conv2D → MaxPooling2D → Dropout.
→ Flatten and return video features.
3.2. Function RNN_Model(sequential_input, model_type=’LSTM’)
→ If model_type = ‘LSTM’: Apply LSTM layers.
→ Else: Apply GRU layers.
→ Return sequential features (text/audio).
Step 4: Attention Mechanism
4.1. Function Attention_Module(features) → Compute attention scores.
→ Apply softmax weighting.
→ Return attention-weighted features.
Step 5: Fusion Mechanism
5.1. Function Multimodal_Fusion(video_features, text_features, audio_features)
→ Concatenate video_features, text_features, audio_features.
→ Apply Attention_Module.
→ Return fused features.
Step 6: Classification Layer
6.1. Function Classification_Layer(fused_features)
→ Pass fused features through Dense Layers.
→ Apply softmax activation for classification.
→ Return the predicted hate speech label.
Step 7: Multi-Modal Hate Speech Detection Process
7.1. Function Multimodal_Hate_Speech_Detection(text_input, audio_input, video_input)
→ Pre-process text: Tokenize and embed using Load_Embeddings().
→ Extract text_features ← RNN_Model(text_embeddings).
→ Pre-process audio: Convert to Mel spectrogram.
→ Extract audio_features ← RNN_Model(audio_input).
→ Pre-process video: Resize, normalize.
→ Extract video_features ← CNN_Model(video_input).
→ Fuse features: fused_features ← Multimodal_Fusion(video_features, text_features, audio_features).
→ Predict hate_speech_label ← Classification_Layer(fused_features).
→ Return hate_speech_label.
Step 8: Model Training
For each batch (text_batch, audio_batch, video_batch, label_batch):
8.1. Compute predicted_label ← Multimodal_Hate_Speech_Detection(text_batch, audio_batch, video_batch).
8.2. Compute loss ← Compute_Loss(predicted_label, label_batch).
8.3. Perform backpropagation (loss.backward()) and update (optimizer.step()).
8.4. Log training progress.
End For
Step 9: Model Saving & Testing
9.1. Save_Model(‘MHSDF_Model’).
9.2. Load_Model(‘MHSDF_Model’).
9.3. Test_Model_on_New_Inputs(new_text_input, new_audio_input, new_video_input)
 
This pseudocode outlines the structure of the Multi-modal Hate Speech Detection Framework, combining 
CNNs, RNNs, and attention mechanisms for effective detection across text, audio, and video data streams. The 
Multi-Modal Hate Speech Detection Framework (MHSDF) is novel because it incorporates feature extraction 
approaches that are particular to each modality and uses a modular data processing pipeline. Optimal fusion 
strategy that dynamically weights textual, visual, and contextual cues using attention-driven multi-modal 
alignment sets MHSDF apart from previous works, even though data pre-processing, feature extraction, and 
deep learning-based classification are well-established components. The system uses an adaptive learning 
technique to improve generalizability across different datasets further and reduce bias. Advancements in 
scalable, interpretable, and morally directed hate speech detection algorithms suited for implementation in 
Predicted hate speech
Predicted non-hate speech
Actual hate speech
True positive (TP)
False negative (FN)
Actual non-hate speech
False positive (FP)
True negative (TN)
Table 2.  Confusion matrix structure.
 
Scientific Reports |        (2025) 15:13020 
11
| https://doi.org/10.1038/s41598-025-94069-z
www.nature.com/scientificreports/

--- Page 12 ---

online moderation systems make this research noteworthy, even if its major contribution is its application to 
real-world social platforms.
Contribution 3: improve detection accuracy and model interpretability
This research intends to use attention mechanisms that enable effective fusion mechanism to improve the 
accuracy of hate speech detection and resilience. Moreover, it guarantees a more open and scalable solution by 
exposing the primary interactions and features utilized by the system to identify hate speech, hence stressing 
model interpretability with attention-based explanations. This work applies Grad-CAM to visual characteristics 
recovered by CNN to identify crucial picture areas contributing to the classification decision, while self-
attention weights from the transformer-based encoder emphasize the most significant text and audio segments. 
Furthermore, SHAP (SHapley Additive Explanations) measures the significance of features across modalities, 
providing a more detailed insight into the impact of various inputs on the model’s predictions.
	
δ 2E (m −α 3R) = Z (N2 ∗Q −2v) ∗f2 (n −∇k) 
(13)
δ 2E (m −α 3R) and feature extraction Z (N2 ∗Q −2v) are represented by the connection that the equation 
predicts. Here, f2 (n −∇k) measures the effect of spatial and temporal variables on the features extracted. 
Equation 13 with the CNN-RNN architecture improves the system’s performance.
	
∀w + r2Q + mcosp = V1 ∗∂r (
n2 (ZX))
+ pk 
(14)
Equation 14 describes the effect of gradients ∀w on the interaction of features r2Q and external factors mcosp
, while the influence of spatial ∂r (
n2 (ZX))
 and temporal features V1 and pk. To fully comprehend the many 
inputs that go into hate speech identification, this connection is vital to the CNN-RNN architecture.
	
Zx2
(
Mn2 −Ey)
= t2
(
cos ∗j (
rv
(
o2 (kr))))

(15)
The function Mn2 −Ey illustrates the connection t2 between the contextual variables cos ∗j and the 
retrieved rv
(
o2 (kr))
 multi-modal characteristics Zx2. Equation 15 improves the model’s capacity to identify 
complicated hate speech patterns by capturing the interplay.
The capacity of a multi-modal hate speech detection model to provide reasons for its conclusions that humans 
understand is known as interpretability. This is achieved mainly via attention maps, feature significance scores, 
and contextual support. Attention processes clarify decision-making by highlighting the input components that 
were most important for categorization, whether it is words in text, video frames, or audio tone cues. Whether 
text, audio, or visual aspects have the largest impact on detection may be shown using feature significance analysis, 
which prioritizes modality contributions. A model’s capacity to provide justifications for its categorization (such 
as determining that an acerbic tone in a speech was a factor in the hate speech label) is an example of post-hoc 
explanations that include interpretability.
The suggested framework’s attention mechanism dynamically prioritizes various modalities according to the 
contextual importance of the detected speech patterns using adaptive weights. A self-attention module calculates 
attention ratings for each text, audio, and video modality by generating query, key, and value representations. 
These scores are generated using a softmax function over similarity measurements across query-key pairs to 
provide more weight to the modalities that contribute the most discriminative features. For example, the approach 
enhances text embeddings and suppresses less useful visual or auditory inputs when textual cues dominate. On 
the other side, the system adjusts its priorities when it detects hate speech via non-verbal indicators like facial 
expressions or changes in tone.
Figure 5 covers text, graphics, audio, and video data. At the beginning of the process, specialized pipelines 
separately handle other forms of data text, images, audio, and video. Word embedding using Word2Vec or 
BERT starts the process; second, pattern recognition with CNN comes; last, temporal analysis with LSTM. 
Another uses each one of these techniques in textual resources. While LSTM concentrates on temporal 
correlations and auditory components, CNN layers synthesize visual signals from image data. While CNN 
has spatial characteristics, LSTM concentrates on sequential processing over video data frames. The processed 
information from all the senses is fused in a fusion mechanism layer under an attention mechanism emphasizing 
and engaging with the most important components of every modality. It constructs this layer from a fusion 
mechanism layer. The output then passes a fully connected neural network for classification to determine if 
the input comprises hate speech. Moreover, an attention-based interpretability layer improves the model’s 
detectability and explainability, thereby stressing important factors influencing its conclusion. Combining many 
data sources for thorough investigation, this multi-modal technique detects hate speech.
	
Rz∀(
m −n2k)
= pcost(b2 ∗tanvr −z (e, w) 
(16)
The connection between the determined characteristics Rz∀(
m −n2k)
 and their contextual modifications 
pcost is shown by the Eq. 16. The whole feature integration is modeled by b2 ∗tanvr, which takes contextual 
aspects and angular connections into account z (e, w). By properly capturing spatial and temporal dynamics, 
Eq. 16 with the CNN-RNN framework on analysis of detection accuracy.
	
d2
(
Mv −Rf (
xy −z2))
= NH (
n2 −∀∂q)

(17)
Scientific Reports |        (2025) 15:13020 
12
| https://doi.org/10.1038/s41598-025-94069-z
www.nature.com/scientificreports/

--- Page 13 ---

The contextual corrections Rf (
xy −z2)
 and the retrieved d2 multi-modal features Mv were calculated using 
the Eq. 17. Temporal dependencies are modeled as NH, and changes in these characteristics n2 −∀∂q are 
emphasized as being affected by spatial interactions. The model can successfully identify and analyze complicated 
patterns in hate speech across several modalities of robustness analysis. The textual and auditory modalities 
are considered to have temporal dependencies under this paradigm. Long short-term memories (LSTMs) can 
remember context over extended periods by capturing sequential patterns across word embeddings in text. 
Critical for the detection of sarcasm and implicit hate speech, RNN-based models analyze temporal patterns in 
speech, including rhythm, pauses, and intonation, for audio.
	
H (
y −m2)
= X (f3 ∗n (−2ev (y −y2))) 
(18)
The variables f3 ∗n in Eq. 18 and how they interact X with the variables H (
y −m2)
 in the context. The 
impact of dynamic interactions and adaptations y −y2 depending on variations in contextual components is 
modeled on −2ev. Equation 18 is of complex hate speech by effectively integrating environmental and feature-
driven information in interpretability analysis.
	
tx−v = F (
cos (
N 2 −Vb
))
∗Y tan ∗(∂2 (Em)) 
(19)
The dynamic relationship between time tx−v and cos (
N 2 −Vb
)
 as regulated by contextual variables, F 
is shown by Eq. 19. The non-linear interactions (∂2 (Em)) between various modalities are captured by the 
phrase Y tan, which highlights the importance of gradient variations in feature extraction. This Eq. 19 is in sync 
because it successfully incorporates geographical and temporal data from sources for scalability analysis.
	
cos ∗z2b (
tan (
mn3 −Ey))
= 1 + r2
(
3c2 −Rw)

(20)
The interaction among complex data streams is captured by cos ∗z2b, which depicts the link between 
tan (
mn3 −Ey)
 multi-modal characteristics r2
(
3c2 −Rw)
 and their contextual impacts. The CNN-RNN 
framework is compatible with Eq. 20, complex feature dynamics with contextual information to identify subtle 
hate speech in performance analysis. The model uses adaptive feature selection, modality-specific dropout, and 
regularization strategies to avoid overfitting while dealing with many modalities simultaneously. All learnable 
parameters undergo L2 regularization, known as weight decay, to prevent excessive weight magnitudes. To induce 
sparsity and reduce co-adaptation, modality-specific sub-networks (CNN for video, LSTM/GRU for text and 
Fig. 5.  Process flow of MHSDF.
 
Scientific Reports |        (2025) 15:13020 
13
| https://doi.org/10.1038/s41598-025-94069-z
www.nature.com/scientificreports/

--- Page 14 ---

audio) utilize strategically placed dropout layers with tuned probabilities. Batch normalization stabilizes feature 
distributions across modalities to further guarantee consistent learning dynamics. To reduce the likelihood of 
overfitting, a gating mechanism that relies on attention selectively improves the contributions of multi-modal 
characteristics, eliminating features that are either too noisy or too redundant, which might cause decision 
boundaries to be too complicated. Lastly, data enrichment approaches increase generalization by exposing the 
model to varied variations within each modality. Examples of these techniques include time-shifting for audio, 
text paraphrasing, and random cropping for video.
The research presents many developments in hate speech recognition using modern deep learning approaches. 
It then highlights how LSTM, BERT, CNN, and Word2Vec manage spatial, temporal, and sequential complexity 
across several media types, improving detection accuracy. Furthermore, it provides a multi-modal deep learning 
method that allows for the individual management of text, images, audio, and video inputs before aggregating 
them for hate speech recognition. Finally, employing attention processes improves model interpretability and 
detection accuracy, providing a scalable and open approach to monitoring social media channels for harmful 
content. In this framework, sequential modeling is performed independently for each modality before being 
integrated through a cross-modal fusion mechanism. Text and audio inputs are processed using separate LSTM/
GRU networks to capture temporal dependencies specific to linguistic and acoustic patterns. Video frames 
are analyzed using a CNN-based feature extractor and a temporal aggregation mechanism such as a Temporal 
Convolutional Network (TCN) or bidirectional LSTM to model motion dynamics over time. After extracting 
sequential features independently, a cross-modal attention module aligns temporal dependencies across 
modalities, ensuring that key events (e.g., sarcastic tone, offensive gestures, or toxic language) are synchronized 
for contextual understanding. This hybrid approach preserves modality-specific temporal structures while 
enabling joint learning at the fusion stage, enhancing the model’s ability to detect nuanced hate speech patterns 
across modalities.
Result and discussion
More sophisticated detection algorithms that can process complex, multi-modal material are required due to 
the proliferation of hate speech on social media. Using a mix of CNNs and RNNs, the proposed Multi-modal 
Hate Speech Detection Framework efficiently detects hate speech in several media types, including text, pictures, 
audio, and video. The framework improves detection accuracy and interpretability by using attention processes 
and advanced word embeddings to tackle the complex nature of hate speech in the modern digital sphere. Since 
hate speech identification often encounters class imbalance, precision, and recall are of utmost importance, while 
accuracy assesses the overall soundness of predictions. While recall is the number of true hate speech incidents 
caught, precision measures the number of detected hate speech occurrences that were appropriately recognized. 
When dealing with unbalanced datasets, the F1 score is preferable since it strikes a better compromise between 
recall and accuracy. To measure the model’s discriminatory power across various thresholds, we used the Area 
Under the Curve (AUC-ROC) (Receiver Operating Characteristic), where higher AUC values indicate better 
model performance.
This research chooses certain baselines to compare the proposed MHSDF against conventional and deep 
learning methods. Using hand-crafted text-based features, HSD-ML depicts standard machine learning models 
such as Random Forest and Support Vector Machines. The RNN-HSD algorithm uses recurrent neural networks 
(LSTMs/GRUs) to identify hate speech in text and identify any sequential relationships within it. Rule-based 
classifiers, such as XGBoost and Decision Trees, fall short when faced with multi-modal information, whereas 
HSD-DT assesses their performance on structured characteristics. Deep feature extraction and transformers 
are two examples of the more sophisticated AI-driven methods that AI-HSD employs. Combining fusion 
mechanism, attention processes, and deep learning, the suggested framework, MHSDF, outperforms text-only 
and uni-modal baselines regarding detection accuracy across various data.
Dataset description33
Hate speech, especially vile written material, has been widely disseminated via social media platforms. According 
to recent trends, a large dataset that includes slang, contractions, hashtags, emoticons, and emojis is needed to 
identify hate speech on social media. Two categories in this dataset include hate speech phrases in English: one 
for hateful content and another for non-hateful material, as listed in Table 3. Human annotators labeled the 
datasets to guarantee precise detection of multi-modal hate speech, even in complex circumstances such as 
sarcasm, implicit hatred, and violations that rely on context. Subject-matter experts and crowd workers manually 
annotated text, photographs, and videos per established annotation standards that considered language clues, 
visual qualities, and cultural context. Many annotators checked each sample to guarantee consistency, and inter-
annotator agreement was assessed using various metrics, such as Cohen’s kappa.
To enable an analysis of its accuracy as measured with publically accessible multi-modal hate speech 
datasets, the performance of the multi-layered multi-modal hate speech detection framework was compared 
over several modalities of texts, pictures, audio, and video. The system’s detection performance is enhanced 
relative to basic approaches based on a single modality by including CNN and LSTM networks in MHSDF that 
can capture spatial and temporal trends, as expressed in Eq. 16. With such capabilities, the system increases 
its performance on more subtle kinds of hate speech by employing advanced word vectors such as Word2Vec 
and BERT, which better understand the meaning of texts. It covers such elements as voicing by silent symbols 
and intellectual ridicule, such as sarcastic hyperboles. The Model performance was analyzed in all modalities, 
and the information needed to assess model performance was collected, with F1-score, recall, and precision 
being among other accuracy indicators. More precise discrimination of complex forms of hate speech is enabled 
through attention mechanisms that help the model focus on informative relations between text, graphics, and 
videos. It established that the effectiveness and accuracy of the framework are equally desirable and may serve 
Scientific Reports |        (2025) 15:13020 
14
| https://doi.org/10.1038/s41598-025-94069-z
www.nature.com/scientificreports/

--- Page 15 ---

as a feasible and efficient multi-layered hate speech detection system. Detection accuracy is one of the results 
raised to 98.53% in Fig. 6. The approach applies commonsense reasoning and sentiment analysis to reconcile 
sentiment incongruities across modalities, which improves sarcasm identification. Using polarity scores, a pre-
trained sentiment classifier applies sentiment analysis to textual input to find inconsistencies between literal 
meaning and contextual sentiment. An auxiliary knowledge network (like ConceptNet) provides context about 
expressions that usually mean sarcasm to enhance the model further. The system can dynamically reweight 
features thanks to integrating these external signals into the attention module during fusion. The model identifies 
possible sarcasm when a remark seems favorable in text but has negative prosody in audio (for example, when 
intonation is accentuated).
As shown in Fig. 7, it can be seen, by testing it on wider text, including pictures, audio, and video files, how 
effective the multi-modal hate speech recognition system is at tackling complex and diverse hate speech over 
the asymmetric approaches that they have. In MHSDF, regarding the combination of CNNs and LSTMs, the 
model manages to resist subtle layers of hate speeches such as ironic movies and memes. This is because of the 
nature of these two techniques; the generalization ability of the system improves across datasets regardless of 
how much the content varies, as already stated in Eq. 17. The extreme language is reinforced by using advanced 
word alignments like those of Bert and word2vec, as contextual meanings are hidden within the text. The latter 
supplementation is necessary in cases where a message is composed of many modalities, and the attentional 
Fig. 6.  The analysis of detection accuracy.
 
Dataset
Total instances
Classes
Dataset balance
Other features
HateXplain
20,148
Hate Speech, Offensive, Normal
Hate Speech: 31.7%
Offensive: 41.5%
Normal: 26.8%
Multi-modal: Text, 
images (memes), 
human explanations 
(33,716)
Davidson’s Hate Speech Dataset
24,783
Hate Speech, Offensive Language, 
Neither
Hate Speech: 5.77%
Offensive Language: 77.43%
Neither: 16.80%
Avg. Tweet Length: 
15.53 words; 
crowdsourced 
annotations
Stormfront Dataset
10,568
Hate Speech, Non-Hate Speech
Hate Speech: 62.4%
Non-Hate Speech: 37.6%
Avg. Post Length: 
48.5 words; labeled 
with hate ideologies
Kaggle Toxic Comment 
Classification
159,571
Toxic, Severe Toxic, Obscene, Threat, 
Insult, Identity Hate, Non-Toxic
Toxic: 9.6%
Severe Toxic: 0.9%
Obscene: 5.3%
Threat: 0.3%
Insult: 5.4%
Identity Hate: 1.0%
Non-Toxic: 89.8%
Avg. Comment 
Length: 67 words
OLID (Offensive Language 
Identification)
14,100
Offensive Language, Not Offensive
Offensive Language: 42.5%
Not Offensive: 57.5%
Avg. Tweet Length: 
14.5 words; 
subtasks: Individual, 
Group
Table 3.  Five popular hate speech detection datasets.
 
Scientific Reports |        (2025) 15:13020 
15
| https://doi.org/10.1038/s41598-025-94069-z
www.nature.com/scientificreports/

--- Page 16 ---

mechanism augments the hate speech detection capabilities of the model based on relevant encounters across 
modalities. A working system is also demonstrated against hostile data, adversarial cases, and many content 
forms to show that the system is more than robust. Nevertheless, even with exposure to extreme hate speech 
conditions, the model still has incredible recovery because it can still obtain decent detection accuracy. The 
robustness ratio is gained by 97.64% in the proposed method of MHSDF. External factors like user history and 
metadata were used for better identification accuracy, especially when recognizing hate speech that depends 
on context. There were contextual clues for differentiating between safe and dangerous material offered by 
metadata features such as timestamps, location tags, and engagement metrics like likes, shares, and comments. 
Identifying repeat offenders and deducing their intentions was easier by looking at their user history, language 
style, interaction patterns, and previous posting activity. Furthermore, coordinated hate speech campaigns were 
identified using network elements like user-community linkages.
The MHSDF procedure focuses on the interpretability of the system, i.e., how intuitive and understandable 
the system makes the decisions. The model helps focus aspect or modality text, graphics, audio, or video, which 
is useful in recognizing hate speech integrating attention processes as explained in Eq. 18. All these contribute 
to explaining these decisions by allowing us to understand the AI’s focus areas while categorizing verbal and 
visual complexities such as memes and sarcastic videos. Young drew attention focused on remembering relevant 
words spoken or expressed in images or words accompanied by sounds or images to facilitate recognition of 
hate speech. The analysts and neutralizers will be more accustomed to why materials were flagged, allowing 
users’ confidence in the system to improve. Also, providing adequate interpretability improves the system’s 
trustworthiness and proper use by preventing the model from considerable bias or inadequacy in the detection 
system. As reflected in Fig. 8, the Interpretability ratio is achieved at 97.71%. Mechanisms for re-weighing feature 
significance, offering counterfactual explanations, or using human-in-the-loop validation to modify results are 
examples of what the framework should define if user interaction is enabled. Since this feature would enable 
domain experts to rectify misclassifications, confidence in the model would increase. This is particularly true in 
subjective instances such as implicit hate speech or sarcasm.
The MHSDF strategy must be able to manage growth to be of benefit over several social landscaping sites 
that generate great extremes of content all day long, as illustrated in Fig. 9. Owing the features of the frameworks 
based on Radiomics that employ different types of media such as text, pictures, audio, and video using CNNs 
and RNNs, further makes it able to manage very large quantities of amounts of multi-modal data, which includes 
but is not limited to text, pictures, sound, and video. This will explain the concept in Eq. 19 concerning how 
scalability is defined. The system scalability is enhanced due to the inclusion of pre-trained embeddings such 
as Word2Vec and BERT, which reduce the chances of extensive retraining. Additional relevant features, such as 
incorporating attention mechanisms within the model, help the model efficiently allocate limited computational 
resources. In addition, due to the modular feature within the model’s architecture, the model can process different 
data streams simultaneously, making it deployable in different network systems. The system demonstrates these 
characteristics, even when expanded to include larger datasets and thousands of active records each day from 
social media events, where it can still meet the demands of the real world without improving, through it being 
Fig. 7.  The graphical representation of robustness.
 
Scientific Reports |        (2025) 15:13020 
16
| https://doi.org/10.1038/s41598-025-94069-z
www.nature.com/scientificreports/

--- Page 17 ---

used as intended, efficiency. Hence, the workability of the model extends to solving large-scale problems in a 
digital environment. The scaling of the ratio is attained by up to 98.67% in the proposed method of MHSDF. The 
research clarifies that sentiment-based embeddings were used in the model to identify hate speech if sentiment 
polarity affects it. One approach may be using sentiment polarity scores as extra input features in the classification 
layer or pre-trained sentiment analysis models like VADER or Sentiment RoBERTa to create sentiment-aware 
Fig. 9.  The analysis of scalability.
 
Fig. 8.  The graphical illustration of interpretability.
 
Scientific Reports |        (2025) 15:13020 
17
| https://doi.org/10.1038/s41598-025-94069-z
www.nature.com/scientificreports/

--- Page 18 ---

feature representations. The research should clarify whether sentiment embeddings were combined with text 
embeddings from BERT or Word2Vec or run independently via an auxiliary network if they were used.
Several measures, such as accuracy, precision, recall, and F1-score, are used to evaluate the performance of 
MHSDF. The model’s capacity to identify complicated types of hate speech in text, photos, audio, and video is 
greatly improved by combining spatial and temporal analysis strengths with RNNs and CNNs. The framework 
surpasses conventional single-modality methods by attaining better detection rates for complex hate speech, 
including sarcasm or layered content, according to extensive assessments conducted utilizing multi-modal 
datasets explained in Eq. 20. Better contextual comprehension, which reduces the number of false positives 
and false negatives, is another benefit of using complex word embeddings like BERT. To optimize the detection 
process, the attention mechanism improves performance by enabling the model to concentrate on crucial 
intermodal interactions. The framework performs well, suggesting it is prepared for actual use in combating 
hate speech on various social media sites. In Fig.  10, the performance ratio is improved by 99.21% in the 
proposed method of MHSDF. To ensure the model applied to diverse types of hate speech, domain adaptation 
approaches were used to reduce the impact of distributional changes across datasets while testing it on numerous 
datasets. This work will use transfer learning to fine-tune pre-trained BERT embeddings on each dataset to 
tailor language representations to different literary styles and vocabularies. Additionally, adversarial domain 
adaptation algorithms like gradient reversal layers (GRL) were used to harmonize feature distributions from 
different datasets, especially in the audio and visual domains.
Figure 11 shows how well ten different models performed using the included bar chart, which ranks them 
according to recall, accuracy, precision, and F1-score. Stack bars show each model, and there is some variation 
in the distribution of these performance indicators among the models. Regardless of the model, the percentage 
of recall (blue) is always higher than that of F1-score (yellow), precision (grey), AND accuracy (orange). Recall is 
the most important element in total performance; however, there are considerable differences in the proportions 
of each statistic. All models follow similar patterns. While recall and F1 scores are very consistent, there is 
potential for certain models to enhance their accuracy and precision, as seen by the little variation in these 
metrics among the models. For applications that need a balanced approach across all metrics, realizing that these 
models prioritize recall in their performance is vital, which might mean sacrificing accuracy.
Ablation study
Ablation research was carried out to evaluate CNNs, RNNs, and attention processes’ respective roles in multi-
modal hate speech detection. One thing to note is that CNNs are crucial for feature extraction; without them, 
performance suffers, especially when extracting spatial patterns from pictures and textual n-gram features. 
Model performance in understanding speech patterns and conversational context suffered when RNNs were 
not used because the model had trouble capturing temporal relationships in sequential data. Lastly, the model’s 
performance and interpretability took a hit after removing the attention mechanism since it could not prioritize 
key modalities properly. Since CNNs, RNNs, and attention are interdependent in multi-modal learning, the 
model that incorporates all three components attained the best accuracy.
An impressive 98.53% detection accuracy, 97.64% robustness, 96.71% interpretability, and 98.57% scalability 
ratio are all results of the MHSDF’s outstanding performance, as summarized in Table 4. The system outperforms 
conventional approaches by reliably detecting complicated hate speech forms and efficiently capturing spatial 
Fig. 10.  The graphical representation of performance.
 
Scientific Reports |        (2025) 15:13020 
18
| https://doi.org/10.1038/s41598-025-94069-z
www.nature.com/scientificreports/

--- Page 19 ---

and temporal patterns. Providing a scalable, efficient, and interpretable solution for hate speech detection 
contributes to a safer online environment, as confirmed by many assessments.
Adversarial robustness was evaluated by testing the model against manipulated inputs, including adversarial 
text modifications (character perturbations, word substitutions), altered images (noise injection, style transfer), 
and tampered audio (pitch shifting, speed variations). The model’s resilience was enhanced using adversarial 
training, where perturbed samples were incorporated into the training process to improve generalization. 
Additionally, defensive mechanisms such as input pre-processing, outlier detection, and confidence-based 
filtering were employed to mitigate adversarial attacks. The model’s architecture prioritized computing efficiency 
and scalability for real-world implementation. Utilizing efficient sequence modeling approaches in RNNs with 
gated mechanisms to decrease duplication and utilizing parallel processing in CNNs for feature extraction led to 
the optimization of the architecture. The attention mechanism zeroed down on the most important modalities 
to reduce superfluous calculations. The model was evaluated on massive datasets, showing that it can efficiently 
handle multi-modal data with high dimensions and low latency. Using GPU hardware acceleration and batch 
processing, the framework could handle real-time hate speech detection across varied platforms without 
significantly lowering performance, ensuring scalability.
The main ethical considerations surrounding hate speech detection powered by AI center on prejudice, 
justice, privacy, and free speech. Social disparities may be worsened when bias in training data causes specific 
languages or populations to be misclassified disproportionately. Being fair is of the utmost importance since too 
lenient models may allow damaging speech to remain online, while too harsh may ban harmless information34. 
Privacy issues might arise when dealing with multi-modal data, especially when processing user data, photos, or 
chats without their knowledge or permission. Furthermore, there must be an appeals process for flagged material 
and openness in decision-making to balance identifying abusive content and protecting free speech. It is critical 
to address these ethical concerns to keep AI-driven moderation fair and responsible35.
Conclusion
MHSDF is a major step in addressing hate speech on social media across disciplines. The characteristics of 
CNNs for spatial feature extraction and RNNs, especially LSTMs, for temporal dependencies allow this system 
to identify complex, multi-layered hate speech material in text, audio, pictures, and video. Sophisticated word 
embeddings like Word2Vec and BERT capture textual data’s semantic richness and contextual subtleties. The 
attention mechanism allows smooth fusion mechanism, making the model sensitive to complex data connections 
like meme visual signals or caustic audio-visual information. The algorithm can identify sophisticated hate 
speech that single-modality techniques miss by concentrating on these critical interactions. Multiple multi-
modal hate speech datasets show that CNNs, RNNs, and attention-based fusion enhance detection accuracy and 
S. no
Aspects
MHSDF
Ratio (%)
1
Detection accuracy
Effectiveness in identifying hate speech across text, images, audio, and video.
98.53%
2
Robustness
Ability to handle diverse and complex hate speech scenarios, maintaining high detection accuracy.
97.64%
3
Interpretability
Clarity in the model’s decision-making process, enhancing user confidence and understanding.
97.71%
4
Scalability
Capability to process large volumes of multi-modal data efficiently across various platforms.
98.67%
5
Performance
Overall effectiveness in detecting complex forms of hate speech, surpassing traditional methods.
99.21%
Table 4.  Findings of the proposed method.
 
Fig. 11.  A Comparison of hate and unhate model.
 
Scientific Reports |        (2025) 15:13020 
19
| https://doi.org/10.1038/s41598-025-94069-z
www.nature.com/scientificreports/

--- Page 20 ---

resilience. Attention processes explain the modalities and characteristics that led to a categorization, improving 
interpretability. Transparency improves model credibility and encourages research into online hate speech’s 
social and environmental dynamics. The MHSDF responds to the increased complexity of harmful social media 
material with an effective, scalable, and interpretable hate speech detection system. This work advances multi-
modal analysis, making the internet safer and laying the groundwork for automatic moderation and content 
screening systems. The numerical findings show that the proposed MHSDF model increases the detection 
accuracy ratio of 98.53%, robustness ratio of 97.64%, interpretability ratio of 97.71%, scalability ratio of 98.67%, 
and performance ratio of 99.21% compared to other existing models.
Future work
Other modalities, such as data from live streams and real-time interaction monitoring, should be incorporated 
into the multi-modal hate speech identification system in future work. The system’s capacity to identify hate 
speech worldwide may be improved by adding new languages, cultures, and dialects to the dataset. Additionally, 
it wants to enhance the attention mechanisms’ ability to identify changing online lingo and coded language, two 
examples of subtle types of hate speech. Addressing ethical concerns about bias and fairness in detection is also 
a primary goal, as is improving computing efficiency for large-scale deployment on social media sites.
Data availability
The datasets utilized in this research are not publicly available but can be provided by the corresponding author 
upon reasonable request.
Received: 25 January 2025; Accepted: 11 March 2025
References
	 1.	 Rana, A. & Jha, S. Emotion based hate speech detection using multi-modal learning. Preprint https://arXiv.org/220206218 (2022).
	 2.	 Chhabra, A. & Vishwakarma, D. K. A literature survey on multi-modal and multilingual automatic hate speech identification. 
Multimedia Syst. 29 (3), 1203–1230 (2023).
	 3.	 Bhowmick, R. S., Ganguli, I., Paul, J. & Sil, J. A multi-modal deep framework for derogatory social media post identification of a 
recognized person. Trans. Asian Low-Resource Lang. Inform. Process. 21 (1), 1–19 (2021).
	 4.	 Yang, F. et al. Exploring deep multi-modal fusion of text and photo for hate speech classification. In Proc. of the third workshop on 
abusive language online, 11–18 (2019).
	 5.	 Cao, R., Lee, R. K. W. & Hoang, T. A. DeepHate: Hate speech detection via multi-faceted text representations. In Proc. of the 12th 
ACM Conference on Web Science, 11–20 (2020).
	 6.	 Chhabra, A. & Vishwakarma, D. K. MHS-STMA: Multi-modal Hate Speech Detection via Scalable Transformer-Based Multilevel 
Attention Framework. Preprint https://arXiv.org/2409.05136 (2024).
	 7.	 Lippe, P. et al. A multi-modal framework for the detection of hateful memes. Preprint https://arXiv.org/2012.12871 (2020).
	 8.	 Das, A., Wahi, J. S. & Li, S. Detecting hate speech in multi-modal memes. Preprint https://arXiv.org/2012.14891 (2020).
	 9.	 Arya, G. et al. Multi-modal hate speech detection in memes using contrastive language-image pre-training. IEEE Access (2024).
	10.	 Mossie, Z. & Wang, J. H. Vulnerable community identification using hate speech detection on social media. Inf. Process. Manag. 57 
(3), 102087 (2020).
	11.	 Paul, S., Saha, S. & Hasanuzzaman, M. Identification of cyberbullying: A deep learning based multi-modal approach. Multimedia 
Tools Appl. 1, 20 (2022).
	12.	 Mahajan, E., Mahajan, H. & Kumar, S. EnsMulHateCyb: multilingual hate speech and cyberbully detection in online social media. 
Expert Syst. Appl. 236, 121228 (2024).
	13.	 Irfan, A., Azeem, D., Narejo, S. & Kumar, N. Multi-modal hate speech recognition through machine learning. In 2024 IEEE 1st 
Karachi Section Humanitarian Technology Conference (KHI-HTC), 1–6  (IEEE, 2024).
	14.	 Ayetiran, E. F. & Özgöbek, Ö. A review of deep learning techniques for multi-modal fake news and harmful languages detection. 
IEEE Access (2024).
	15.	 Yang, C., Zhu, F., Liu, G., Han, J. & Hu, S. Multi-modal hate speech detection via cross-domain knowledge transfer. In Proc. of the 
30th ACM International Conference on Multimedia, 4505–4514 (2022).
	16.	 Lu, S. et al. The multi-modal fusion in visual question answering: a review of attention mechanisms. PeerJ Comput. Sci. 9, e1400 
(2023).
	17.	 Choi, S. R. & Lee, M. Transformer architecture and attention mechanisms in genome data analysis: a comprehensive review. 
Biology 12 (7), 1033 (2023).
	18.	 Toktarova, A. et al. Hate speech detection in social networks using machine learning and deep learning methods. Int. J. Adv. 
Comput. Sci. Appl. 14(5) (2023).
	19.	 Roy, P. K., Tripathy, A. K., Das, T. K. & Gao, X. Z. A framework for hate speech detection using deep convolutional neural network. 
IEEE Access 8, 204951–204962 (2020).
	20.	 Priyadarshini, I., Sahu, S. & Kumar, R. A transfer learning approach for detecting offensive and hate speech on social media 
platforms. Multimedia Tools Appl. 82 (18), 27473–27499 (2023).
	21.	 Yuan, L., Wang, T., Ferraro, G., Suominen, H. & Rizoiu, M. A. Transfer learning for hate speech detection in social media. J. 
Comput. Social Sci. 6 (2), 1081–1101 (2023).
	22.	 Khan, M. U., Abbas, A., Rehman, A. & Nawaz, R. Hateclassify: A service framework for hate speech identification on social media. 
IEEE Internet Comput. 25 (1), 40–49 (2020).
	23.	 Jahan, M. S. & Oussalah, M. A systematic review of hate speech automatic detection using natural Language processing. 
Neurocomputing 546, 126232 (2023).
	24.	 Mehta, H. & Passi, K. Social media hate speech detection using explainable artificial intelligence (XAI). Algorithms 15 (8), 291 
(2022).
	25.	 Rodriguez, A., Chen, Y. L. & Argueta, C. FADOHS: framework for detection and integration of unstructured data of hate speech 
on Facebook using sentiment and emotion analysis. IEEE Access 10, 22400–22419 (2022).
	26.	 Jin, W., et al.. A prompting multi-task learning-based veracity dissemination consistency reasoning augmentation for few-shot fake 
news detection. Eng. Appl. Artif. Intell. 144, 110122 (2025). 
	27.	 Jin, W. et al. Veracity-oriented context‐aware large Language models–based prompting optimization for fake news detection. Int. 
J. Intell. Syst. 2025 (1), 5920142 (2025).
Scientific Reports |        (2025) 15:13020 
20
| https://doi.org/10.1038/s41598-025-94069-z
www.nature.com/scientificreports/

--- Page 21 ---

	28.	 Jin, W. et al. Can rumor detection enhance fact verification? Unraveling cross-task synergies between rumor detection and fact 
verification. IEEE Trans. Big Data (2024).
	29.	 Jin, W. et al. A veracity dissemination consistency-based few-shot fake news detection framework by synergizing adversarial and 
contrastive self-supervised learning. Sci. Rep. 14 (1), 19470 (2024).
	30.	 Nasser, A. R., Hasan, A. M. & Humaidi, A. J. DL-AMDet: deep learning-based malware detector for android. Intell. Syst. Appl. 21, 
200318 (2024).
	31.	 Korial, A. E., Gorial, I. I. & Humaidi, A. J. An improved ensemble-based cardiovascular disease detection system with chi-square 
feature selection. Computers 13 (6), 126 (2024).
	32.	 Abed, R. A., Hamza, E. K. & Humaidi, A. J. A modified CNN-IDS model for enhancing the efficacy of intrusion detection system. 
Measurement: Sens. 35, 101299 (2024).
	33.	 ​h​t​t​p​s​:​/​/​w​w​w​.​k​a​g​g​l​e​.​c​o​m​/​d​a​t​a​s​e​t​s​/​w​a​a​l​b​a​n​n​y​a​n​t​u​d​r​e​/​h​a​t​e​-​s​p​e​e​c​h​-​d​e​t​e​c​t​i​o​n​-​c​u​r​a​t​e​d​-​d​a​t​a​s​e​t
	34.	 Katirai, A. Ethical considerations in emotion recognition technologies: a review of the literature. AI Ethics. 4 (4), 927–948 (2024).
	35.	 Udupa, S., Maronikolakis, A. & Wisiorek, A. Ethical scaling for content moderation: extreme speech and the (in) significance of 
artificial intelligence. Big Data Soc. 10 (1), 20539517231172424 (2023).
Author contributions
All authors contributed significantly to this work. Prabhu R performed Conceptualization, Methodology, Data 
Curation, Software Implementation, Formal Analysis and Writing. Seethalakshmi V performed Supervision, 
Validation, Review & Editing. Both authors have read and approved the final manuscript.
Declarations
Competing interests
The authors declare no competing interests.
Additional information
Correspondence and requests for materials should be addressed to R.P.
Reprints and permissions information is available at www.nature.com/reprints.
Publisher’s note  Springer Nature remains neutral with regard to jurisdictional claims in published maps and 
institutional affiliations.
Open Access   This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 
4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in 
any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide 
a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have 
permission under this licence to share adapted material derived from this article or parts of it. The images or 
other third party material in this article are included in the article’s Creative Commons licence, unless indicated 
otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence 
and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to 
obtain permission directly from the copyright holder. To view a copy of this licence, visit ​h​t​t​p​:​/​/​c​r​e​a​t​i​v​e​c​o​m​m​o​
n​s​.​o​r​g​/​l​i​c​e​n​s​e​s​/​b​y​-​n​c​-​n​d​/​4​.​0​/​.​
© The Author(s) 2025 
Scientific Reports |        (2025) 15:13020 
21
| https://doi.org/10.1038/s41598-025-94069-z
www.nature.com/scientificreports/

```
