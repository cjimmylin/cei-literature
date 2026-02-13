---
title: "2025-Masood-Dialectal substitution as an adversarial approach for evaluating - PDF Extract"
source_pdf: "2025-Masood-Dialectal substitution as an adversarial approach for evaluating.pdf"
pages: 19
extracted_at: "2026-02-13T14:50:54.854866"
---

# PDF Extract: 2025-Masood-Dialectal substitution as an adversarial approach for evaluating

**Source PDF:** 2025-Masood-Dialectal substitution as an adversarial approach for evaluating.pdf
**Total Pages:** 19

---

## Content

```
--- Page 1 ---

ARTICLE IN PRESS
Article in Press
Dialectal substitution as an adversarial approach 
for evaluating Arabic NLP robustness
Scientific Reports
Received: 28 October 2025
Accepted: 12 January 2026
Cite this article as: Alshemali B. Dialectal 
substitution as an adversarial approach 
for evaluating Arabic NLP robustness. 
Sci Rep (2026). https://doi.org/10.1038/
s41598-026-36252-4
Basemah Alshemali
We are providing an unedited version of this manuscript to give early access to its 
findings. Before final publication, the manuscript will undergo further editing. Please 
note there may be errors present which affect the content, and all legal disclaimers 
apply.
If this paper is publishing under a Transparent Peer Review model then Peer 
Review reports will publish with the final article.
https://doi.org/10.1038/s41598-026-36252-4
© The Author(s) 2026. Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International 
License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit 
to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do 
not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this 
article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the 
article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain 
permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

--- Page 2 ---

Dialectal Substitution as an Adversarial Approach for
Evaluating Arabic NLP Robustness
Basemah Alshemali1,*
1Taibah University, College of Computer Science and Engineering, Yanbu, 46421, Saudi Arabia
*bshemali@taibahu.edu.sa
ABSTRACT
Recent advances in deep neural networks (DNNs) have led to significant enhancements in Arabic natural language processing
(NLP). However, their robustness remains insufficiently explored, particularly in adversarial settings. Most existing Arabic NLP
systems are predominantly trained on Modern Standard Arabic (MSA), whereas real-world Arabic text frequently incorporates
dialectal forms that diverge lexically and morphologically. To evaluate the impact of this distributional mismatch between training
data and deployment conditions, this paper introduces dialectal substitution as a black-box token-level adversarial method
against DNN-based MSA classification systems. Our approach identifies the most influential token in an input sequence via a
scoring function and replaces it with a dialectally equivalent form using a fine-tuned Arabic dialectizer. The proposed attack
demonstrates how dialectal substitutions can diminish the classification accuracy of the models, exposing vulnerabilities in
DNN-based models trained on MSA corpora. We reveal a significant gap in current Arabic NLP systems, which fail to resist the
diglossia nature of the Arabic language. We encourage researchers to pursue more robust and generalizable models that
consider all forms of Arabic dialects.
1 Introduction
Deep neural networks (DNNs) have dominated current natural language processing (NLP) and reach state-of-the-art results in
popular tasks such as sentiment analysis1, text classification, and machine translation2. They have proven to be capable of
capturing contextual semantics and syntactic dependencies across different languages. Despite their remarkable performance
on spoken and written tasks, DNNs have exhibited a level of vulnerability when some perturbational shifts are present in the
input data3. The susceptibility revealed when evaluating DNN-based systems in adversarial settings has raised concerns about
their effectiveness for use in real-world settings.
1.1 Adversarial Examples
One of the most recognizable vulnerabilities of DNN-based NLP systems is the existence of adversarial examples. An
adversarial example is an input that has been slightly modified so that it is still semantically equivalent to humans but causes
the model to produce an incorrect prediction. In the text domain, adversarial examples can be developed by tweaking tokens,
characters, and sentence structures in such a way that the semantic meaning remains correct, yet confuses the model. This
phenomenon shows how minor and insignificant changes can cause inaccurateness for models trained on very large corpora.
The difference between white-box and black-box adversarial attacks is one of the key categories in adversarial machine
learning4. White-box attacks assume full access to model parameters, architecture, and gradients, allowing for more advanced
optimizations to generate perturbations. White-box attacks allow for the usage of gradient information to reveal the smallest
perturbations that yield the largest errors in predictions5. However, Black-box attacks operate under absent knowledge of the
targeted model. They only have the ability to query the system and receive the output; therefore, they must leverage heuristics
or transferability from surrogate models to construct an impactful adversarial attack6. Black-box attacks tend to resemble the
real-world attack scenarios in which adversaries have limited access to proprietary systems.
Based on perturbation strategies and limitations, there are several types of adversarial attacks in NLP. Character-level
attacks7,8 involve the smallest perturbations of typos and character insertions and deletions, which still allow for some text
readability. Token-level attacks5 involve using synonyms, reordering within text, and paraphrasing, which, to some extent,
maintain a semantic meaning. Sentence-level attacks9,10 involve larger perturbations such as syntactic structuring and swapping
semantic roles. Each of the attacks presents unique challenges and requires specific defensive strategies.
Research on adversarial attacks in NLP initially developed in the English language, where character-level, token-level, and
sentence-level approaches have been shown to consistently deceive large-scale English NLP models1,9,11–18. These attacks
notably exposed the fragility of DNN-based systems, finding that even top-ranked models were susceptible to adversarial
manipulations. In contrast to English, there has been limited research on adversarial attacks in the Arabic language. There are
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 3 ---

only a small number of studies in this area, and they have applied variations of character substitution19, synonym substitution20,
and diacritical manipulations21. Overall, the Arabic adversarial NLP literature, compared to English, is sparse, disjointed, and
mostly experimental. There are still significant gaps in understanding how Arabic NLP models are vulnerable to adversarial
attacks across a variety of tasks and domains.
1.2 Arabic Language
Arabic is a Semitic language with unique morphological, phonological, and syntactic aspects that differentiate it from many
other languages in the world22. Arabic is also diglossic; the formalized, standardized version taught in schools and used in
official documents is known as Modern Standard Arabic (MSA) and exists alongside many dialects that serve as the primary
form of communication in daily life. Known dialects, such as Egyptian Arabic, Levantine Arabic, Maghrebi Arabic, and Gulf
Arabic, diverge significantly in phonology, vocabulary, and grammar, resulting in challenges for mutual intelligibility across
regions. Such aspects of MSA compared to its dialects indicate the relative complexity of Arabic language formations and the
need to recognize both in linguistic analysis and computational efforts.
Arabic possesses specific features that distinguish it from a number of other languages, providing a unique environment for
developing adversarial attacks. Arabic is morphologically rich, with a robust root-and-pattern system, where words can be
created by applying patterns to trilateral or quadrilateral roots22. In addition, Arabic has a right-to-left writing system and uses
diacritics that can change both meaning and pronunciation23. Due to the agglutinative nature of Arabic, individual words can
contain several morphemes, leading to a complex morphosyntactic organization that adversarial attacks may take into account.
In addition to this complexity, Arabic diglossia (dialects) represents one of the most distinctive features of the Arabic
linguistic landscape, creating a complex diglossia between MSA and Arabic dialects in various regions. MSA is different than
Arabic dialects at the lexical, morphological, and syntactic levels. Arabic dialects are typically dominant in spoken and informal
writing, while MSA is the high variety for formal writing, education, and news service24. The presence of MSA and regional
dialects creates systematic mismatches between the training corpora, which are often full of MSA, and the inputs selected in the
real world, which may contain words and structures of dialect. For instance, the MSA word for ‘now’ ( 	àB@) is often realized as
(ú
æ¯ñËX) in Egyptian Arabic and ( 	á
mÌ'@) in Gulf Arabic. Such lexical substitutions, while semantically transparent to native
speakers, can mislead models trained solely on MSA. Given this diglossic context, dialectal substitutions can be expected as
a natural and realistic form of adversarial attacks and may have a significant impact on downstream tasks, such as machine
translation, question answering, and sentiment analysis.
1.3 Arabic NLP and Diglossia
Sentiment analysis and news classification are two Arabic NLP tasks that heavily depend on lexical cues in determining the
sentiment polarity or topical classification of Arabic text25,26. The sentiment analysis task is expected to automatically detect
the subjective polarity conveyed by text content in Arabic language. This usually includes text classification as either positive,
negative, or neutral. In sentiment analysis tasks, the subjective sentiment is usually communicated through adjectives that have
quite different Arabic lexical forms in various Arabic dialects. For instance, the Arabic adjective word (MSA: YJ
k. ) with the
meaning ‘good’ may be dialectally changed in Egyptian Arabic as (
ñ») or even as ( 	áK
 	P) in the Gulf Arabic dialects. This
will preserve the semantic richness but remain incomprehensible to models trained exclusively on MSA Arabic texts.
News classification or topical classification is the task of automatically assigning a predefined topic label like politics,
sports, finance, or technological, to a news text based on text content. The trained models in news classification tasks establish
a strong link between topic labels and a minimal number of selective keywords27. Since most Arabic classification models
have massive training datasets supporting MSA Arabic language only, replacing MSA high-impact keywords with a dialectal
Arabic version can disrupt learned associations and lead to incorrect predictions. This lexical mismatch highlights how dialectal
variation poses a realistic and challenging robustness issue for Arabic NLP systems.
1.4 Proposed Approach
Despite the strong performance of existing Arabic NLP systems, most of these systems are trained almost exclusively on
Modern Standard Arabic26. In real-world usage, however, Arabic text frequently contains dialectal tokens that diverge lexically,
morphologically, and phonologically from MSA28. Existing models lack explicit mechanisms to normalize or generalize across
this dialectal variation, which leads to brittle decision boundaries. This paper investigates dialectal replacement and introduces
a black-box token-level adversarial attack to assess DNN-based models trained on non-dialectal Arabic text. We propose a
dialectal substitution attack to replace MSA tokens with their dialectal equivalents. We focus on the Egyptian and Gulf dialects
since both dialects are spoken widely and have clear lexically distinguished characteristics from MSA. Our methodology
extends to sentiment analysis and news categorization tasks, which are foundational tasks in Arabic NLP systems. We highlight
that replacing only one token with its dialectal equivalent could fool outstanding DNN-based classification models. Our goal
/
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 4 ---

is to show that a dialectal adversarial attack could reveal the vulnerability of DNN-based Arabic NLP models and to call for
developing more robust models that can handle dialectal variability with other special features of the Arabic language.
The remainder of this paper is structured as follows. Section 2 discusses the current adversarial approaches designed
to evaluate the robustness of DNN-based classifiers with Arabic text. Section 3 describes the proposed framework, and the
experimental setup is discussed in Section 4. Sections 5 and 6 describe and analyze the results of the experiments performed,
and Section 7 provides the conclusion and the suggested future work.
2 Related Work
Whereas adversarial attacks represent a popular method for evaluating deep neural architectures trained on English textual
datasets1,9,11–18, this is not the case for Arabic models; therefore, the gap in the current literature suggests more efforts to
exploit the efficiency of models working with Arabic. This section surveys eleven research studies that introduced different
methodologies for evaluating the performance of Arabic DNNs under adversarial conditions. These studies are presented
chronologically.
Alshemali and Kalita29 contributed to the security of Arabic NLP by presenting the first black-box token-level adversarial
attack involving perturbations created from Arabic text inputs. The authors derived their attack generation from the intentional
breach of grammatical features of the Arabic language: Noun-adjective agreement. Their findings show that they were able to
deceive two sentiment analysis DNN-based models: The Bi-LSTM model30 and the CNN model31, trained on the Hotel Arabic
Reviews dataset (HARD)32 and the Book Reviews in Arabic dataset (BRAD)33, respectively. According to their results, the
decrease in the classification accuracy of their models was greater than 50.00%.
Alshemali and Kalita19 also presented the first black-box character-level adversarial attacks against Arabic models. Their
method is predicated on flip operations spawned from common spelling mistakes made by non-native Arabic speakers. These
attacks are mere substitutions of one or two characters for visually similar characters. The authors validated their attacks’
effectiveness against DNN-based classifiers using the Bi-LSTM model30 and the CNN model31 trained on the BRAD dataset33.
They also analyzed the performance of the Bidirectional Encoder Representations from Transformers (BERT) model34 and
the XLNet model35 trained on the Single-labeled Arabic News Articles Dataset (SANAD)36. Their results indicate that the
Bi-LSTM and CNN architectures exhibited reductions in classification accuracy of 27.73% and 23.25%, respectively, while the
average classification accuracy dropped by 23.75% and 18.36% for the BERT and XLNet models, respectively.
Alshalan et al.20 assessed the robustness of Arabic transformer-based models via two token-level adversarial attacks. First,
they apply a black-box attack where tokens in the input sample are selected at random and substituted with tokens from
the Arabic WordNet37. Second, they assess their attack as a white-box fast gradient sign method (FGSM) attack38, where
a substitution token is selected from a dynamic set which maximizes the output label prediction probability change for the
input sample. The methods were assessed on two transformer-based models: The CAMeLBERT39 and the AraBERT26 models
trained on the HARD dataset32. Their findings suggest that, for the first attack, the average classification accuracy declined by
7.00% for CAMeLBERT and by 10.00% for AraBERT, whereas the second attack produced substantially larger reductions of
44.00% and 40.00%, respectively.
Abdelaty et al.40 utilized the Explainable AI (XAI) methodology41 to create black-box synonym-based token-level
adversarial instances. The XAI method was operated to evaluate the importance of each token in the input sample and
subsequently changing critical tokens. Then, these critical tokens were transformed into synonyms extracted from the
MARBERT transformer42. Their evaluation involves the AraBERT26 and QARiB43 models trained on the OSACT5 dataset44.
Their results demonstrated that their proposed attack achieved an average success rate of 29.60% against the AraBERT model
and 27.50% against the QARiB model.
Abdellaoui et al.45 tested the efficacy of the Dar-RoBERTa model46 to detect offensive mutations. They employed
various black-box character-level adversarial attacks including character modification, insertion, and deletion. For character
modification, they changed a character to a random character, changed punctuation to exclamation points, and changed numbers
to zeros. For character insertion, they added spaces or dots between letters, added random numbers, and duplicated vowels. For
character deletion, they deleted punctuation, numbers, and spaces between two tokens. According to their results, the model is
susceptible to adversarial attacks when an adversary adds a space or dot between two letters or changes one letter in a token,
with attack success rates ranging from 17.90% to 29.40%. Attacks that deleted spaces between tokens and duplicated vowels
had a 16.10% and 13.40% success rates, respectively. Attacks with the least success rates included attacking punctuation or
number changes, with success rates ranging from 0.42% to 6.10%.
Alajmi et al.47 assessed the stability of Arabic spam classification models under adversarial attacks. They proposed several
types of black-box adversarial attacks (character, token, and sentence). More specifically, the character-level attacks included
replacing some Arabic characters with visually similar ones and creating misspelled tokens. The token-level attacks involved
replacing tokens with synonyms. The sentence-level attacks included inserting paraphrase-based perturbations. They evaluated
the AraBERT model26 trained on the SMS Spam Collection48 and the Arabic Spam/Ham datasets49,50. Their findings indicated
/
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 5 ---

that the AraBERT model exhibited a significant vulnerability to their adversarial attacks. Specifically, a classification accuracy
reduction of approximately 67.40% with the character-level attacks, 22.95% with the token-level attacks, and a 77.40% with the
sentence-level attacks.
Alshahrani et al.51 introduced a black-box token-level adversarial attack to evaluate Arabic text classifiers with synonym
substitution. They attempted to generate adversarial examples by replacing tokens with synonymous counterparts derived from
a pretrained Arabic BERT language model. They tested their attack on three models: BERT34, WordCNN52, and WordLSTM53
models trained on the HARD dataset32 and the Sentiment Analysis for Social Media Posts in Arabic Dialect (MSDA) dataset54.
Their results demonstrated a degradation in all models’ performance, with classification accuracy dropping by around 20.94%,
2.94%, and 3.33%, for the BERT, WordCNN, and WordLSTM, respectively.
Nakhleh et al.55 evaluated the resilience of the AraBERT model26 to black-box character-level adversarial examples. Like
Alshemali and Kalita19, they created character-level perturbations based on spelling mistakes typically found in the writings of
non-native Arabic learners. They substituted the Arabic characters of the key tokens with visually similar ones, one character
per token. They assessed the performance of the AraBERT model trained on the BRAD dataset33. Their results indicated a
decline in performance, with the average classification accuracy decreasing by approximately 12.00%.
Radman et al.56 developed a white-box synonym-based adversarial attack. Cosine similarity was applied to locate the closest
lexical neighbors for each token, followed by leveraging models’ gradients to introduce their perturbations. Their experiments
tested seven different models: LSTM-based53, GRU-based57, CNN-based58, MHA-based59, LSTM-CNN, GRUCNN and
MHA-CNN. These models were trained on the Large-scale Arabic book Reviews (LABR) dataset60. Their proposed adversarial
attack diminished the classification accuracy of the evaluated models, resulting in an accuracy reduction of approximately
24.80% for LSTM, 21.30% for GRU, 19.00% for CNN, 11.50% for MHA, 26.30% for GRU-CNN, 34.40% for LSTM-CNN,
and 21.30% for MHA-CNN.
Alshemali61 is among the first to investigate the reliability of DNN-based classifiers trained on Arabic through black-box
adversarial attacks. Their technique generates sentence-level adversarial examples by paraphrasing the most important sentence
in the input sample. They evaluated the BERT model34 and the XLNet model35 trained on the BRAD dataset33. They also
assessed the performance of the Bi-LSTM model30 and the CNN model31 trained on the SANAD dataset36. Their results show
that even a single paraphrased sentence can deceive neural classifiers. The classification accuracy of the Bi-LSTM model and
the CNN model was reduced by around 27.20% and 26.00%, respectively. Furthermore, there was a 29.6% and a 26.0% drop in
the classification accuracy of the BERT and XLNet models, respectively.
Alshemali21 also proposed a black-box token-level adversarial attack exploiting Arabic diacritics (tashkeel) to deceive
Arabic DNN-based systems. The attack occurs by adding legitimate and even arbitrary diacritics to the most important token of
diacritic-free Arabic inputs. They experimented with several NLP systems, including the AraBERT model26 and CAMeLBERT
model39 trained on the HARD dataset32, in addition to the word-level CNN model31 and the word-level Bi-LSTM model30
trained on the SANAD dataset36. Their results support that DNN-based NLP systems are susceptible to adversarial attacks, and
the reduction in models’ classification accuracy was ranging from 23.675% to 32.24%.
This paper aims to fill the current gap in adversarial research in Arabic by systematically studying dialectal substitutions as
an adversarial generation approach to evaluate several NLP models. This will not only expand the current literature on Arabic
adversarial efforts but also promote the investigation of similar approaches to increase defenses against weaknesses in Arabic
NLP.
3 Adversarial Attack Design
In this work, dialectal substitution is investigated as an adversarial mechanism for testing the robustness of Arabic NLP
systems. We aim to demonstrate that Arabic dialects pose a major challenge for NLP systems that are trained on MSA. We
generate adversarial examples by substituting tokens from MSA into equivalent tokens from dialects, creating samples that
are semantically meaningful to human readers but may significantly decrease the performance of DNN-based models. The
approach introduced in this study situates adversarial evaluation within a black-box context, since white-box scenarios require
access to the underlying model parameters, which is not feasible for most secure applications in the real world.
The proposed token-level adversarial samples are produced in two distinct phases:
• Stage 1: The most important token is identified in the input sequence.
• Stage 2: The selected most important token is substituted by its dialectal equivalent.
/
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 6 ---

3.1 Ranking of Token Importance
The majority of prior black-box adversarial attacks reported in the literature first identify important tokens, followed by
manipulation of the input text. Perturbation-based importance is an effective approach for evaluating the importance of individual
input tokens to NLP model predictions, especially in black-box situations with no access to internal model parameters62–65.
Essentially, it evaluates whether perturbing/deleting certain tokens makes a difference in predicted output confidence. The
token’s importance is based on its resulting change to the output. Recent studies have leveraged the perturbation-based
importance approach to guide adversarial attack strategies to create efficient adversarial samples that expose the weaknesses of
NLP classifiers30,61,66,67. Ren et al.68 demonstrated that token selection via perturbation can efficiently support adversarial
attacking in black-box settings by finding minimal changes to inputs that produce strong impacts. Jin et al.69 used confidence
scores to guide perturbation attacks and found that high-importance tokens resulted in a significantly higher attack success rate
than random and frequency-guided attacks.
It can be noted that perturbation-based techniques are more appropriate for the black-box setting compared to the other
approaches that require access to the model’s internal parameters. Gradient-based attributions refer to techniques that calculate
the importance values of tokens based on the model’s response to the perturbation of its embedding or representation. Some of
the most popular techniques that belong to the former include saliency maps obtained from the input gradient70 and integrated
gradients71. Attention-based techniques that consider the attention weight values obtained from the model as a representation
of token importance have been widely adopted for the explanation of neural model predictions72. While these techniques can
provide fine-grained importance estimates, they require access to the internal model parameters and gradient values, which
makes them unsuitable for strict black-box adversarial settings. Li et al.1 systematically compared several evaluation approaches
and confirmed that perturbation-based scoring is more reliable than attention-based or gradient-based rules to reflect causal
contributions of tokens.
In this study, adversarial examples were generated by leveraging the class probability scores of the targeted models. A
scoring function (Score(.)) was used in this paper to investigate the influence of certain tokens on the predictions of the targeted
model F(.). The scoring function indicates the importance of each token in the input sequence x = x1x2...xn. The proposed
scoring function follows a leave-one-out perturbation strategy, in which the importance of a particular token xi is measured by
removing it and calculating the difference in the score of the model’s prediction against the original input. In formal terms:
Score(xi) = F(x1,x2,...,xi−1,xi,xi+1...,xn)−F(x1,x2,...,xi−1,xi+1,...,xn)
(1)
As an extension to the original concept of adversarial examples in computer vision, where small perturbations to an image
can change its predicted label3, we intentionally limit the attack to substituting a single token for each input to study the
minimal instances at which dialect differences can mislead a classifier. While multi-token substitution attacks can be considered
more effective, they may have compounding effects that diminish attribution clarity and lower the degree of imperceptibility.
Therefore, the aspect of our methodology shows priority in interpretability and conservative robustness assessment. Hence, the
proposed method focuses on the most significant token in the input sequence, which is the token with the largest Score(.) value.
Precisely, the token that holds:
argmax
1≤i≤n
Score(xi)
(2)
3.2 Strategy of Token Substitution
In the field of NLP, the generation of adversarial examples must satisfy a number of important prerequisites to ensure the
meaning and utility of adversarial examples. First, adversarial examples require semantic fidelity, meaning that a perturbed text
should retain the same meaning and also be comprehensible to human readers. Second, adversarial examples require fluency,
since any grammatical errors would easily expose the perturbation. Third, adversarial examples require imperceptibility, which
would need minimal changes to human inspection to ensure the naturalness of the text. Finally, adversarial examples need to be
effective in altering the output of the model, thereby exposing weaknesses in the system. All of these requirements provide a
framework for creating adversarial examples that are linguistically valid and also disruptive to NLP models. In order to meet
these needs, two simple but powerful transformers are presented:
3.2.1 MSA To Egyptian Token Substitution Attack (MSA-to-EGY Attack):
This attack replaces the most important token with its corresponding Egyptian dialectal equivalent. The substitution is performed
by retrieving the dialectal form from an Arabic dialectal transformation model. The remainder of the input sequence (the tokens
preceding and following the targeted token) is preserved unaltered.
3.2.2 MSA To Gulf Token Substitution Attack (MSA-to-GLF Attack):
Similar to MSA-to-EGY Attack, however, this attack replaces the most important token with its equivalent from the Gulf
dialect. As with the MSA-to-EGY Attack, the remainder of the input sequence is left unmodified.
/
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 7 ---

Algorithm 1: The overall procedure employed for generating the adversarial examples.
Input: Original input sequence x = [x1x2...xn], DNN-based model F(.), Arabic dialectizer Dialectize(.), Importance
scoring function Score(.) to identify the most important token.
Output: Adversarial text
1 for each token xi in x do
2
xremoved = remove(xi,x) // Delete xi from x
3
Score[i] = F(x)−F(xremoved) // calculate class probability drop
4 end
5 ImportantTokenIndex = argmax(Score)
6 DialectalToken ←−Dialectize(x[ImportantTokenIndex],x)
7 AdversarialInput = replace(x,ImportantTokenIndex,DialectalToken) // We replace the original token with its
dialectal equivalent.
8 return AdversarialInput
An outline of the proposed adversarial methodology is presented in Algorithm 1 and a procedural example showing the
internal stages of the methodology is presented in Figure 1.
We selected the Egyptian and Gulf dialects as varieties for our study since they are linguistically significant and relevant to
the field of Arabic NLP. Egyptian Arabic is the most widely understood dialect across all dialects, as Egypt is the home base for
media, cinema, and popular culture consumption. The Gulf Arabic, on the other hand, has distinguishable lexical, phonological,
and morpho-syntactic properties from MSA and other regional varieties. Therefore, by selecting these two Arabic dialects, we
obtain both a powerful variety that is widely understood and a localized variety with identifiable structural differences. These
two dialects are an important variety when assessing the robustness of NLP systems in real-world applications. We aim to
systematically assess how adversarial substitution attacks exploit lexical differences across Arabic dialects and to gain some
insights into vulnerabilities present in Arabic NLP systems.
Owing to its superior performance, the Arabic dialectation model proposed by Yang et al.73 was employed to transform
MSA tokens to dialectically equivalent tokens. Its high-performance architecture makes it a competitive choice for research that
requires both computational efficiency and robust reasoning. The Qwen3-7B dialectizer, when carefully fine-tuned, serves to
satisfy several prerequisites for developing valid and functional adversarial samples. These prerequisites are addressed through
particular capabilities and techniques of the model’s functioning.
First, semantic fidelity: The Qwen3-7B model leverages its deep contextual understanding acquired from extensive
pretraining and fine-tuning. The substitutions made by the model involve more than word-level replacement, picking forms that
are compatible with the semantic context as it is expected from native speakers. The attention mechanism is able to consider the
entire input, with the selection of word forms by the dialectizer being compatible with the surrounding context, syntax, and
semantics. Second, fluency: The fine-tuning of the Qwen3-7B model on diverse and naturally occurring dialectal text enables it
to produce grammatically coherent outputs that adhere to the morphological and syntactic conventions of the target dialect. The
architecture of the model’s decoder enables fluent creation of sequences that respect the grammatical structure of Arabic. This
makes it easier for the substitution to be inserted in the original sentence without introducing any grammatical errors.
Third, imperceptibility: This is achieved as a result of our one-token substitution approach. Only the most prominent
token is substituted, thereby resulting in a minimum textual footprint of alteration. Combined with the dialectizer’s ability to
produce naturalistic word forms, the adversarial example generated is unlikely to distinguish from natural dialectal text. Finally,
effectiveness: The dialectizer also cooperates with the perturbation scoring mechanism for the importance of the tokens. Since
it targets the token that significantly contributes to the model’s prediction, that maximizes the possibility of altering the output
classification. The dialectizer thus aims at the most effective single important lexical element so that the substitution carries a
high adversarial value with respect for the fidelity, fluency, and imperceptibility requirements.
This study presents a method that generates adversarial examples that are semantically accurate, meaning-preserving,
and syntactically coherent, ensuring that the altered inputs remain natural and comprehensible to human readers while still
posing challenges to automated systems. Comprehensive experimental assessments performed on two benchmark Arabic
corpora and across four different deep neural network models reveal that the suggested technique consistently undermines
model performance in realistic adversarial scenarios. The persistent performance declines noted across several datasets
and architectures suggest that the method is not customized for a particular model or task but rather reveals fundamental
vulnerabilities present in modern Arabic NLP systems.
/
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 8 ---

Figure 1. A high-level architectural diagram illustrating the main components and stages of the proposed adversarial
framework combined with an input sample.
/
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 9 ---

4 Experiments
This section outlines the classification models targeted in the experiments, along with the Arabic datasets and the Arabic
dialectizer we utilized.
4.1 Classification Models under Evaluation
In this study, we assess the robustness of the following models:
1. AraBERT26: A transformer-based language model that was pretrained on Arabic. AraBERT was created in response to
multilingual model limitations for the morphologically rich and complex nature of the Arabic language. AraBERT is
an adaptation of the BERT model and was retrained on a large corpus of Arabic text, such as news articles, Wikipedia
dumps, and other texts, enabling it to gain an extensive context-based understanding of the MSA language. When it
was finetuned to specific tasks, like sentiment analysis, named entity recognition, and question-answering, AraBERT
consistently performs state-of-the-art results, surpassing even multilingual models on most tasks.
2. CAMeLBERT39: A transformer-based language model, developed explicitly for high-level Arabic natural language
processing. CAMeLBERT was built on top of the BERT architecture, and it was extensively pretrained on a diverse
corpus that encompassed a rich text of MSA. CAMeLBERT introduced tokenization strategies that accommodate Arabic’s
complex morphological variations with training corpora that are specifically structured to include token diversity. This
linguistic diversity gave CAMeLBERT a more general capability and a more robust ability to understand the Arabic
language across different contexts. Overall, CAMeLBERT has been shown to have excellent performance on a variety of
tasks, including part-of-speech tagging, sentiment analysis, and named entity recognition.
3. Word-level CNN model31: A word-level Convolutional Neural Network (CNN) model that was an important advancement
made in the area of text classification. This approach processes sentences as sequences of word embeddings, applying
different sizes of one-dimensional convolutional filters to learn local n-gram features in the input text. Using multiple
filter sizes across the same input allows for the detection of all types of patterns, from bi-grams to long sequences.
Max-pooling occurs forward to obtain the most salient features from each filter output.
4. Word-level Bi-LSTM model30: A Bi-directional Long Short-Term Memory (Bi-LSTM) model developed for sequence
modeling in NLP. The main innovation of the model was its ability to recognize long-range dependencies within the
sentence by reading the word sequence in both forward and backward direction. This is done through the implementation
of two LSTM layers; one reads the sentence from beginning to end and one reads the same sentence from end to
beginning. The results from these two LSTMs are concatenated, providing a contextual representation for every word that
involve information from the entire surrounding context. This model demonstrates superior performance for extracting
features and modeling sequential information, especially in the Arabic Language.
The victim models, AraBERT, CAMeLBERT, CNN, and Bi-LSTM, have substantial differences in architecture, scale, and
training paradigm, which in turn may affect their robustness to dialectal substitution attacks. AraBERT and CAMeLBERT are
large-scale transformer-based models pre-trained on large corpora of MSA, approximately 6.5B and 8.7B tokens, respectively,
with 12 layers and approximately 135 million parameters each. On the other hand, CNN and Bi-LSTM are considerably smaller,
with roughly 3-5 million parameters and shallower architectures, trained from scratch on the Single-labeled Arabic News
Articles Dataset (SANAD) without any pre-exposure to large-scale MSA pre-training.
4.2 Arabic Textual Datasets
This section provides a description of the datasets employed for fine-tuning/training the models to perform two NLP tasks:
sentiment analysis and news categorization.
1. The Hotel Arabic Reviews Dataset (HARD)32: This corpus was used to fine-tune the AraBERT and CAMeLBERT
models. HARD is a balanced corpus designed to support researchers conducting sentiment analysis in Arabic. HARD
contains over 93,000 MSA hotel reviews collected from Booking.com and categorized as positive or negative. HARD
provides a large domain-specific resource, which facilitates comparative studies of machine learning and deep learning
approaches for sentiment analysis, contributing to advancing Arabic language processing research. The average length of
hotel reviews in the HARD dataset is 19.50 tokens, with a maximum of 503 tokens. Tokens in the HARD dataset have an
average length of four characters.
2. The Single-labeled Arabic News Articles Dataset (SANAD)36: This corpus was used to train the word-level CNN
model and the word-level Bi-LSTM model. SANAD is a large-scale corpus designed to support research on Arabic text
classification and related NLP tasks. The SANAD corpus contains 98,154 MSA news articles that were scraped from
/
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 10 ---

Table 1. The effectiveness of the proposed adversarial attacks: MSA-to-GLF and MSA-to-EGY attacks, which were assessed
against both the AraBERT and CAMeLBERT models. The values reported reflect the classification accuracy of the models
under the respective adversarial attacks.
AraBERT
CAMeLBERT
No-attack
94.00%
90.00%
Under MSA-to-GLF Attack
72.50%
63.40%
Under MSA-to-EGY Attack
65.30%
55.20%
various Arabic media resources such as Arabiya, AlKhaleej, and Akhbarona. Each article is categorized into one of
seven topical categories: Culture, politics, sports, finance, medical, religion, and technology. Each category contains
14,022 articles. The SANAD corpus is valuable due to its size, lexical variety, and representation of MSA across several
domains, providing a comprehensive resource for developing and validating machine learning and deep learning models.
4.3 Arabic Dialectation Model
Given its demonstrated superiority in recent benchmarks, we adopted the Qwen3-7B model73 as the primary model for
extracting the dialectal replacements. The Qwen3-7B model is an evolution of the Qwen family of large language models, and
it is representative of the latest enhanced generation of transformer-based architectures intended for improved performance
and efficiency. The Qwen3-7B has seven billion parameters and has been trained on a massive multilingual corpus that was
selected to comprise 119 different languages and dialects, including Arabic. The corpus includes website scrapes, books,
PDFs, and synthetic code developed by prior versions of prior Qwen models. This allows Qwen3-7B to exhibit competitive
performance on many benchmarks, including mathematics, code generation, and commonsense reasoning. According to their
empirical evaluations, Qwen3-7B had a superior performance on multilingual benchmarks, with other findings indicating strong
reasoning, knowledge recall, and instruction-following abilities74,75.
In the experiments of this study, we fine-tuned the Qwen3-7B model on the Nuanced Arabic Dialect Identification (NADI)
corpus76. NADI is an extensive resource developed to facilitate the study of Arabic dialectology and computational linguistics,
specifically in the area of dialect recognition. NADI corpus involves classification at multiple levels, such as country and
province, as well as individual dialect identification. NADI was collected from social media platforms such as the X.com
platform, and it comprises text for all 21 Arab countries and up to 100 provinces. By comprising a massive amount of social
media texts, NADI represents naturally occurring and varied dialectal texts. NADI has over one million tweets, which provide a
large benchmark for developing accurate classification systems. Qwen3-7B model was fine-tuned for 5 epochs, learning rate of
2e-5, batch size of 16, and cross-entropy loss function, to adapt to the dialectal data without overfitting. Equivalence of dialects
was validated by manually inspecting 1000 randomly substituted instances, which showed 95.00% consistency in semantics as
well as dialectal authenticity.
5 Results
In this section, we examine the effectiveness of the proposed method in the domains of sentiment analysis and news categoriza-
tion.
5.1 Sentiment Analysis Task
Consistent with the process observed in previous adversarial attacks research6,9–13,15,77–80, and because of the time-consuming
and resource-intensive nature of adversarial sample construction, a random sample of 1,280 examples from the HARD test set
was selected for testing the effectiveness of the proposed approach. We used stratified sampling by class label to preserve the
original distribution, avoid selection bias, and ensure that the evaluation subset is representative of the overall test distribution.
The sample size was chosen to balance computational feasibility, given the query-intensive nature of perturbation-based
black-box attacks, with the need for stable performance estimates. Adversarial attacks were applied to the sampled examples to
determine the models’ susceptibility, as illustrated in Table 1.
The results show that by manipulating the leading token in the input sequence, the proposed approach can create adversarial
examples that defeat both transformer-based classifiers. The proposed method can alter the label predictions of both classifiers
and decline the classification accuracy substantially. The classification accuracy of the AraBERT model dropped from 94.00%
to approximately 72.00% under the MSA-to-GLF adversarial attack, and further to 65.30% under the MSA-to-EGY attack.
Similarly, the classification accuracy of the CAMeLBERT was reduced from 90.00% to approximately 63.00% when it was
subjected to the MSA-to-GLF attack and further to 55.20% under the MSA-to-EGY adversarial attack. This suggests that both
transformer-based Arabic models, which were trained on dialect-neutral texts, are extremely sensitive to dialectal substitutions,
/
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 11 ---

Table 2. The effectiveness of the proposed adversarial attacks: MSA-to-GLF and MSA-to-EGY attacks, which were assessed
against both the CNN and the Bi-LSTM models. The values reported reflect the classification accuracy of the models under the
respective adversarial attacks.
CNN
Bi-LSTM
No-attack
83.50%
80.00%
Under MSA-to-GLF Attack
65.00%
59.30%
Under MSA-to-EGY Attack
61.70%
55.90%
with average accuracy reduction ranging from 25.10% to 30.70%. These models clearly exhibited a serious vulnerability, which
limits their ability to maintain performance based on minor differences. This highlights the urgent lack of robust Arabic NLP
models that can properly interpret and process inputs with various dialects while maintaining consistent performance and
resilience toward adversarial attacks.
In this study, we highlighted the effect of manipulating the most important token in each of the input samples. The
adversarial attacks presented were able to compromise the models’ performance by changing one token per instance, as noted
in Table 1. The findings in this paper provide evidence supporting the models’ sensitivity to small perturbations in significant
tokens. The results also suggest that the influence of adversarial attacks could be empowered by expanding the process to
include multiple tokens in a single input. This will provide more impactful adversarial examples that would cause a more
significant performance reduction across models.
5.2 News Classification Task
In addition to examining the proposed adversarial attacks on the sentiment analysis task, the efficacy of the said attacks was
similarly evaluated on the news categorization task. To accomplish this goal, we employed the word-level CNN model31 and the
word-level Bi-LSTM model30 trained on the SANAD dataset36. In accordance with the methodology outlined in Section 5.1, a
randomly selected sequence of 1,280 instances from the SANAD test set was chosen and converted into adversarial examples.
These perturbed examples were then used to test the models’ robustness to the dialectal substitution attacks. The results of this
evaluation are presented in Table 2, which demonstrates the influence of dialectal substitutions on the classification accuracy of
models trained on MSA-only corpus. The results may also reveal possible limitations of DNN-based architectures when it
comes to the task of Arabic news categorization.
The generated textual adversarial examples had a significant effect on all targeted models, resulting in notable performance
decline and illustrating the effectiveness of the proposed attacks against the intended models. These adversarial examples were
able to successfully compromise the performance of the CNN and the Bi-LSTM models, resulting in average degradations
in accuracy ranging from 20.15% to 22.40%. In particular, the word-level CNN model had a 18.50% drop in classification
accuracy under the MSA-to-GLF attack, while the MSA-to-EGY attack had a greater reduction of 21.80% in the classification
accuracy of the model. On the other hand, the performance of the Bi-LSTM model declined significantly, reducing its accuracy
from 80.00% to 59.30% under the MSA-to-GLF attack and to 55.90% under the MSA-to-EGY attack. These results show that
even models that have previously exhibited excellent performance in various Arabic NLP tasks81–84, can be affected by a few
targeted manipulations, demonstrating the real need to develop more robust Arabic NLP models that can sustain performance
with adversarial examples. Two sample outputs of the proposed attacks are presented in Tables 3 and 4.
5.3 Statistical Evaluation of Adversarial Impact
To verify that the observed performance drops were not the result of random sampling variation or incidental prediction
noise, we conducted a McNemar’s test85. This test is particularly suitable in our setting, as it assesses paired nominal
outcomes, specifically, the predictions generated by the same model on identical test instances prior to and after adversarial
perturbation. McNemar’s test evaluates whether the differences in classification results are symmetric or statistically significant
by concentrating on instances whose predicted labels differ between the clean MSA inputs and their corresponding adversarial
dialectal counterparts. We adjusted the significance threshold for each test to 0.05. For all evaluated models, AraBERT,
CAMeLBERT, CNN, and Bi-LSTM, the test yielded a p-value < 0.01, indicating that the change in the classification accuracy
is statistically significant.
6 Discussion
The findings in this research confirm that semantically faithful dialect substitutions can be used to severely undermine current
Arabic NLP models in a black-box setting. The performance degradation across different datasets and model architectures indi-
cates that current systems are vulnerable to realistic dialectal variation, even when perturbations are minimal and linguistically
natural.
/
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 12 ---

Table 3. An illustrative example of the MSA-to-EGY attack from HARD corpus, in which the targeted token is highlighted in
red. As a result of the applied attack, the model’s prediction shifted from positive in the original input to negative in the
adversarial version.
Original Arabic Text:
. 	YK
 	YËð ¨ñ	JJÓ 	àA¿ PA¢	¯B @ð HAÓY	mÌ'@ É¿ 	áÓ I. K
Q¯ ©¯ñÖÏ@ð éª@ðð é	®J
 	¢	
	¬Q	ªË@ . è	PAJÜØ I	KA¿ Y	J	®Ë@ ú
	¯ éÓA¯B @
English Translation: The stay at the hotel was excellent. The rooms were clean and spacious, the location was close to all
services, and the breakfast was varied and delicious.
Adversarial Arabic Text:
. 	YK
 	YËð ¨ñ	JJÓ 	àA¿ PA¢	¯B @ð HAÓY	mÌ'@ É¿ 	áÓ I. K
Q¯ ©¯ñÖÏ@ð éª@ðð é	®J
 	¢	
	¬Q	ªË@ . éÊK
Aë I	KA¿ Y	J	®Ë@ ú
	¯ éÓA¯B @
English Translation: The stay at the hotel was excellent. The rooms were clean and spacious, the location was close to all
services, and the breakfast was varied and delicious.
Table 4. An illustrative example of the MSA-to-GLF attack from HARD corpus, in which the targeted token is highlighted in
red. As a result of the applied attack, the model’s prediction shifted from negative in the original input to positive in the
adversarial version.
Original Arabic Text:
	à@ AÒ» èYJ
k. 	áºK ÕË
	­J
 	¢	JË@ éÓY 	gð éîE
QºË@ l'@ðQËAK. éJJ
ÊÓð éÖß
Y¯ I	KA¿ é	¯Q	ªËA	¯ AîDK.Qj. JK. IÔ¯ ú
æË@ XA	J	®Ë@ @ñ@ 	áÓ
. éJ
	¯@QgAK. @ñÊÓAªJK
 ÕË ÈAJ.®JB@ ù
	® 	£ñÓ
English Translation: One of the worst hotels I have ever stayed at, the room was old and filled with unpleasant odors, the
cleaning service was inadequate, and the reception staff were unprofessional.
Adversarial Arabic Text:
	à@ AÒ» èYJ
k. 	áºK ÕË
	­J
 	¢	JË@ éÓY 	gð éîE
QºË@ l'@ðQËAK. éJJ
ÊÓð éÖß
Y¯ I	KA¿ é	¯Q	ªËA	¯ AîDK.Qj. JK. IÔ¯ ú
æË@ XA	J	®Ë@ qJ
K.@ 	áÓ
. éJ
	¯@QgAK. @ñÊÓAªJK
 ÕË ÈAJ.®JB@ ù
	® 	£ñÓ
English Translation: One of the worst hotels I have ever stayed at, the room was old and filled with unpleasant odors, the
cleaning service was inadequate, and the reception staff were unprofessional.
6.1 Robustness Differences Between Transformer and Non-Transformer Models
By comparing the results of the experiments in Sections 5.1 and 5.2, it is evident that the BERT-based models examined in this
study exhibited greater sensitivity to adversarial attacks compared to the CNN and Bi-LSTM architectures. This observation is
consistent with previous literature on adversarial examples in Arabic NLP21,51,86–89, which also points out the sensitivity of
transformer-based models to targeted perturbations. Considering all models evaluated in this study, the CNN model exhibited
the greatest robustness to the MSA-to-GLF attack, experiencing a post-attack accuracy reduction of 18.50%. In contrast,
CAMeLBERT was the most vulnerable model, with a drop of 26.60% in accuracy under the same attack. The CAMeLBERT
model also had the lowest accuracy under the MSA-to-EGY attack (55.20%), while the CNN model had the highest post-attack
accuracy (61.70%). These findings highlight the increased sensitivity of transformer-based Arabic NLP models to minimal
token-level perturbations compared to other models, such as CNN and Bi-LSTM models.
The observed sensitivity of transformer models over non-transformer architectures can be explained by a number of closely
linked architectural and representational characteristics of transformer models. First, transformer models heavily depend on
subword tokenization strategies that break down words into more fine-grained units learned via pretraining datasets. Although
this is beneficial for improvements to vocabulary representational ability, this is also highly vulnerable to changes to the surface
form of words at a lexical level, which involve a number of unseen or low-probability subword sequences that can generally
result in large variations of subword partitions based on one token replacement90,91. Second, the transformer-based models
employ self-attention mechanisms that adapt the weightage of the tokens based on their relevance. This often results in the
predictions being driven by a subset of the most prominent tokens. Any changes in these tokens, especially the sentiment-
driven adjectives or crucial nouns, often result in higher variability in the model confidence92,93. It has been found that the
transformer-generated outputs are quite sensitive to changes happening in a constrained subset of crucial tokens68,69. This
makes them more susceptible to adversarial attacks.
Conversely, non–transformer-based models such as CNNs and Bi-LSTMs usually induce a more balanced representational
importance on the input sequence. CNNs process input representations over fixed n-gram windows, while Bi-LSTMs follow a
/
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 13 ---

Table 5. Distribution of Part-of-Speech (POS) tags for vulnerable tokens identified in the HARD hotel classification dataset
and the SANAD news classification dataset.
POS Tag
Sentiment Analysis
News Classification
Adjective
48.00%
14.00%
Verb
27.00%
22.00%
Noun/Named Entity
18.00%
58.00%
Others
7.00%
6.00%
sequential manner of capturing contextual representations, which distributes influence more evenly across tokens and reduce
reliance on exact lexical realizations30,31. As a result, although these models are less expressive, they may exhibit greater
robustness to targeted single-token perturbations.
6.2 Linguistic Analysis of Vulnerable Tokens
In order to better understand our results, we examined the linguistic categories of the tokens marked as "most important"
during Stage 1. We classify target tokens into four major class types: Adjective, Verb, Noun/Named Entity, and Other (Adverb,
Particle, etc.). For the sentiment analysis task, as shown in Table 5, adjectives proved to be the most susceptible word type with
48.00% in the HARD samples, followed by verbs, which made up 27.00% of attacks and mostly corresponded to experiential
verbs. Nouns and named entities accounted for 18.00%, while the remaining 7.00% covered the rest of the word classes. These
results clearly show that there is a heavy weighting of sentiment-bearing features in certain word forms in MSA that mainly lead
to overseen misclassifications due to the lack of ability of the employed DNN architectures to align them with dialect versions.
In the news classification task, a similar Part-of-Speech (POS) analysis was applied to the instances sourced from the
SANAD dataset. Noticeably, a considerable percentage of the instances were targeted using nouns and named entities at
58.00%, which contrasts with the mostly adjective-targeted instances in the sentiment analysis task. This implies that news
classification models are highly reliant on specific topical entities to classify articles under categories such as Politics and
Sports. The use of MSA terms that are replaced with dialectal forms compromises the models’ ability to map instances into
categories. Verbs comprised the second-leading target in the task at 22.00%, where specific action-oriented MSA terms were
replaced by dialectal equivalents.
6.3 Failure Modes of the Proposed Adversarial Attack
Although the proposed dialectal substitution attack is effective in many cases, a qualitative analysis of unsuccessful perturbations
shows several key reasons for their failure. There are several systematic conditions for which this kind of attack was not able to
change the prediction of the model.
• Adversarial failure can be defined as the spread of sentiment/categorical information across various word tokens. The
proposed method ensures perturbations are limited to a single word, ensuring the generated text still has the properties
of being imperceptible and semantically equivalent. However, for a statement where sentiment has been composed or
redundantly represented, simply perturbing a pivotal word may not be sufficient for a prediction change.
• The attack might fail in cases when the selected token does not have sentiment- or topic- bearing properties despite
having high perturbation scores. The importance calculation using perturbation scores focuses on sensitivity rather than
semantic meaning; hence, a given token can be important for reasons independent of class membership. The substitution
of tokens with their dialectical variants will, nevertheless, maintain the same semantic meaning, leading to equivalent
predictions. For instance, using a high-importance verb like ( 	àA¿) (was) will have no effect on predictions for sentiment
analysis, since the token does not carry meaning.
• Adversarial samples may be less effective if lexical substitutions do not produce sufficient lexical variation from MSA
words. There may be certain words in the dialect that have strong lexical and phonological similarities with MSA words;
for example, the word (©K
Qå) represents the token (fast). In these cases, it is possible that embeddings do not have
meaningful changes based on these substitutions and therefore may be less effective as an attack method. This becomes
particularly true for dialects that retain many MSA elements.
• Failures can arise from robustness issues at the level of the models. Certain models exhibit smoother decision boundaries
or rely on broader contextual tokens rather than isolated tokens. Non-transformer models could potentially pay equal
attention to the entire input sequence, thus being less susceptible to failures based on changes centered on a single
token30,31. There could be instances where fine-tuning the transformer models improves robustness by reducing
dependence on individual lexical items94,95.
/
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 14 ---

Table 6. The classification accuracy of the models under the proposed attack (MSA-to-EGY) and other state-of-the-art
black-box token-level attacks.
AraBERT
CAMeLBERT
No-attack
94.00%
90.00%
Under the attack of Alshahrani et al.51
71.60%
65.00%
Under the attack of Alshemali21
68.00%
59.20%
Under our MSA-to-EGY attack
65.30%
55.20%
These failure modes provide valuable insights into the aspects of the Arabic NLP systems which are resilient towards
dialectal differences and the ones which are prone to minimal perturbations. Understanding these limitations is essential in order
to have accurate interpretations of the attack’s results and for guiding the development of more robust models and evaluations.
6.4 Impact of Dialectal Variation on Model Robustness
The experimental findings in this paper suggest that dialectal substitutions of Gulf Arabic are less detrimental to DNN-based
models than similar substitutions in Egyptian Arabic. DNN-based models trained on mostly MSA data can better generalize to
Gulf forms of Arabic than the Egyptian. Adversarial examples with the Egyptian dialect tokens created a more significant drop
in classification accuracy and compromised model robustness to a higher degree than with the Gulf substitutions.
Egyptian and Gulf Arabic are different forms of Arabic that demonstrate obvious lexical, phonological, and syntactical
similarity, but still has many elements that distinguish them from each other and from MSA. The Egyptian dialect is heavily
influenced by the historical contact of Coptic–98, English, and French99, lending to many loanwords and colloquial constructs
that differ greatly from their MSA counterparts. The Gulf dialect, however, seems to remain closer to MSA in many respects,
especially vocabulary and phonological structures, as its use contains many classical Arabic elements and fewer colloquial
divergences100,101.
Empirical findings from earlier studies suggest that Gulf Arabic is more similar to MSA than Egyptian Arabic. A lexical
study conducted by Kwaik et al.102 statistically established that Gulf Arabic had a higher lexical overlap with MSA than
Egyptian Arabic. Quantitative comparisons based on lexical distance and shared vocabulary distributions, conducted by
Bouamor et al.103, placed Gulf Arabic closer to MSA than Egyptian Arabic, particularly for content words and formal registers.
Inoue et al.104 indicated that Gulf Arabic had better performance in the morphosyntactic tagging task, suggesting that MSA was
more aligned to the structures of Gulf Arabic than Egyptian Arabic. Other linguistic studies confirmed similar observations,
such as Broselow et al.105, who found that Levantine dialects, such as Palestinian Arabic, had a higher degree of similarity to
MSA than Egyptian Arabic, particularly in terms of lexical and phonological characteristics.
6.5 Comparison with State-of-the-Art Arabic Adversarial Attacks
This section compares the efficiency of the proposed adversarial attack method with state-of-the-art methods that experimented
with adversarial examples in the Arabic NLP domain, which has been surveyed in Section 2. For the purpose of a fair
and meaningful comparison, we restricted our comparison to black-box adversarial attacks on the token level that do not
require model parameter access. Additionally, we considered only those methods that explicitly preserve semantic fidelity and
grammatical correctness. These limitations correspond with the design objectives of the proposed methodology and represent
realistic adversarial situations.
Consequently, we evaluate our approach in relation to the synonym-based substitution attack proposed by Alshahrani et al.51
and the diacritical-based substitution attack proposed by Alshemali21. All these attacks provide linguistically valid adversarial
samples while functioning under black-box assumptions. To maintain experimental consistency, we reimplemented both attacks
and applied them to a subset of 1,280 clean instances randomly selected from the HARD test set, which was also utilized to
evaluate our technique in Section 5.1. The resultant adversarial instances were subsequently employed to assess the AraBERT
and CAMeLBERT models under uniform settings.
The results, summarized in Table 6, indicate that all assessed models exhibit susceptibility to the specified adversarial
attacks. The attack of Alshahrani et al. led to a decline in classification accuracy of roughly 22.40% for AraBERT and
25.00% for CAMeLBERT. Likewise, the attack proposed by Alshemali resulted in accuracy decline of 26.00% and 30.80% for
AraBERT and CAMeLBERT, respectively. While these findings validated the efficacy of current Arabic adversarial techniques,
Table 6 illustrates that the proposed dialectal substitution attack resulted in the most substantial performance decline in both
models, 28.70% for AraBERT and 34.80% for CAMeLBERT. Thereby highlighting its enhanced capability to reveal model
vulnerabilities. The superior effectiveness of the proposed attacks indicates that DNN-based models are susceptible to the
systematic language gap between MSA and dialects than to mere lexical or diacritic changes. These findings highlight an
/
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 15 ---

essential requirement for the development of diglossia-aware models capable of preserving semantic consistency across diverse
regional Arabic dialects.
7 Conclusion
This paper has established a novel framework for adversarial attacks on Arabic NLP systems through dialectal substitutions.
Using systematic token-level replacement across major dialects, including Egyptian and Gulf Arabic, we demonstrated how
a linguistic variation can be used as a subtle yet effective method for exposing weaknesses in Arabic DNN-based models.
Our framework combines a black-box scoring approach with dialect-specific lexical substitutions to generate an important
and practical addition to the field of adversarial research in Arabic. Our dialectal substitution attack was able to reduce
the classification accuracy by an average of 27.90% for the transformer-based models and an average of 21.30% for the
non-transformer-based models. The findings of this paper should point future research towards the study of other dialects and
finding defensive strategies in order to improve the robustness of Arabic NLP systems against adversarial manipulations.
References
1. Moraffah, R. & Liu, H. Exploiting class probabilities for black-box sentence-level attacks. In Findings of the Association
for Computational Linguistics: EACL 2024, 1557–1568 (Association for Computational Linguistics, 2024).
2. Liu, X., Dai, S., Fiumara, G. & De Meo, P. An adversarial training method for text classification. J. King Saud Univ. -
Comput. Inf. Sci. 35, 101697 (2023).
3. Szegedy, C. et al. Intriguing properties of neural networks. In International Conference on Learning Representations
(2014).
4. Alshemali, B. & Kalita, J. Improving the reliability of deep neural networks in nlp: A review. Knowledge-Based Syst.
191, 105210 (2020).
5. Wang, X., Yang, Y., Deng, Y. & He, K. Adversarial training with fast gradient projection method against synonym
substitution based text attacks. In Proceedings of the AAAI Conference on Artificial Intelligence, vol. 35, 13997–14005
(2021).
6. Li, D. et al. Contextualized perturbation for textual adversarial attack. In Proceedings of the 2021 Conference of the
North American Chapter of the Association for Computational Linguistics: Human Language Technologies, 5053–5069
(Association for Computational Linguistics, 2021).
7. He, X., Lyu, L., Sun, L. & Xu, Q. Model extraction and adversarial transferability, your BERT is vulnerable!
In
Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics:
Human Language Technologies, 2006–2012 (Association for Computational Linguistics, 2021).
8. Mondal, I. BBAEG: Towards BERT-based biomedical adversarial example generation for text classification. In
Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics:
Human Language Technologies, 5378–5384 (Association for Computational Linguistics, 2021).
9. Han, W., Zhang, L., Jiang, Y. & Tu, K. Adversarial attack and defense of structured prediction models. In Proceedings of
the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP), 2327–2338 (Association for
Computational Linguistics, Online, 2020).
10. Song, L., Yu, X., Peng, H.-T. & Narasimhan, K. Universal adversarial attacks with natural triggers for text classification.
In Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics:
Human Language Technologies, 3724–3733 (Association for Computational Linguistics, 2021).
11. Henderson, P. et al. Ethical challenges in data-driven dialogue systems. In Proceedings of the 2018 AAAI/ACM Conference
on AI, Ethics, and Society, 123–129 (2018).
12. Ribeiro, M. T., Singh, S. & Guestrin, C. Semantically equivalent adversarial rules for debugging NLP models. In
Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
856–865 (Association for Computational Linguistics, 2018).
13. Gan, W. C. & Ng, H. T. Improving the robustness of question answering systems to question paraphrasing. In Proceedings
of the 57th Annual Meeting of the Association for Computational Linguistics, 6065–6075 (Association for Computational
Linguistics, 2019).
14. Chen, Y., Su, J. & Wei, W.
Multi-granularity textual adversarial attack with behavior cloning.
arXiv preprint
arXiv:2109.04367 (2021).
/
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 16 ---

15. Fursov, I. et al. A differentiable language model adversarial attack on text classifiers. IEEE Access 10, 17966–17976
(2022).
16. Berezin, S., Farahbakhsh, R. & Crespi, N. No offence, bert - I insult only humans! multilingual sentence-level attack on
toxicity detection networks. In Findings of the Association for Computational Linguistics: EMNLP 2023, 2362–2369
(Association for Computational Linguistics, 2023).
17. Lel, T. E., Ahsan, M. & Latifi, M. Lexicon-based random substitute and word-variant voting models for detecting textual
adversarial attacks. Computers (2025).
18. Qiu, S. et al. Hard label adversarial attack with high query efficiency against nlp models. Sci. Reports 15 (2025).
19. Alshemali, B. & Kalita, J. Character-level adversarial examples in arabic. In 20th IEEE International Conference on
Machine Learning and Applications (ICMLA), 9–14 (IEEE, 2021).
20. Alshalan, H. & Rekabdar, B. Attacking a transformer-based models for arabic language as low resources language (lrl)
using word-substitution methods. In 2023 Fifth International Conference on Transdisciplinary AI (TransAI), 95–101
(IEEE, 2023).
21. Alshemali, B. Diacritical manipulations as adversarial attacks in arabic nlp systems. Arab. J. for Sci. Eng. (2025).
22. Yushmanov, N. V. THE STRUCTURE OF THE ARABIC LANGUAGE (ERIC, 1961).
23. Satterthwait, A. C. Computational research in arabic. Mech. Transl. Comput. Linguist. 7, 62–70 (1963).
24. Ferguson, C. A. Diglossia. WORD 15, 325–340 (1959).
25. Elnagar, A., Yagi, S. & Nassif, A. B. N. Arabic text classification using deep learning models. In International Conference
on Industrial, Engineering and Other Applications of Applied Intelligent Systems, 246–256 (Springer, 2018).
26. Antoun, W., Baly, F. & Hajj, H. AraBERT: Transformer-based model for Arabic language understanding. 9–15
(Association for Computational Linguistics, 2020).
27. Einea, O., Elnagar, A. & Al-Debsi, R. A comparative study of arabic text classification techniques. Inf. Process. &
Manag. 56, 102–124 (2019).
28. Abdul-Mageed, M., Elmadany, A. & Nagoudi, E. M. B. Mega-cov: A billion-scale dataset of 100+ languages for covid-19.
Proc. 16th Conf. Eur. Chapter Assoc. for Comput. Linguist. 3402–3420 (2021).
29. Alshemali, B. & Kalita, J. Adversarial examples in arabic. In International Conference on Computational Science and
Computational Intelligence, 371–376 (2019).
30. Gao, J., Lanchantin, J., Soffa, M. L. & Qi, Y. Black-box generation of adversarial text sequences to evade deep learning
classifiers. In IEEE Security and Privacy Workshops, 50–56 (2018).
31. Kim, Y. Convolutional neural networks for sentence classification. In Proceedings of the 2014 Conference on Empirical
Methods in Natural Language Processing (EMNLP), 1746–1751 (Association for Computational Linguistics, 2014).
32. Elnagar, A., Khalifa, Y. S. & Einea, A. Hotel arabic-reviews dataset construction for sentiment analysis applications. In
Intelligent Natural Language Processing: Trends and Applications, 35–52 (Springer, 2018).
33. Elnagar, A. & Einea, O. Brad 1.0: Book reviews in arabic dataset. In 2016 IEEE/ACS 13th International Conference of
Computer Systems and Applications (AICCSA), 1–8 (IEEE, 2016).
34. Devlin, J., Chang, M.-W., Lee, K. & Toutanova, K. BERT: Pre-training of deep bidirectional transformers for language
understanding. In The Conference of the North American Chapter of the Association for Computational Linguistics:
Human Language Technologies, 4171–4186 (2019).
35. Yang, Z. et al. Xlnet: Generalized autoregressive pretraining for language understanding. Adv. neural information
processing systems 32 (2019).
36. Einea, O., Elnagar, A. & Al Debsi, R. SANAD: single-label Arabic news articles dataset for automatic text categorization.
Data Brief 25 (2019).
37. Black, W. et al. The arabic wordnet project. In Proceedings of the Fifth International Conference on Language Resources
and Evaluation (LREC) (European Language Resources Association (ELRA), Genoa, Italy, 2006).
38. Goodfellow, I. J., Shlens, J. & Szegedy, C. Explaining and harnessing adversarial examples. In International Conference
on Learning Representations (2015).
39. Inoue, G., Alhafni, B., Baimukan, N., Bouamor, H. & Habash, N. The interplay of variant, size, and task type in Arabic
pre-trained language models. In Proceedings of the Sixth Arabic Natural Language Processing Workshop, 92–104 (2021).
/
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 17 ---

40. Abdelaty, M. & Lazem, S. Investigating the robustness of arabic offensive language transformer-based classifiers to
adversarial attacks. In 2024 Intelligent Methods, Systems, and Applications (IMSA), 109–114 (IEEE, 2024).
41. Gunning, D. et al. Xai—explainable artificial intelligence. Sci. robotics 4, eaay7120 (2019).
42. Abdul-Mageed, M., Elmadany, A. & Nagoudi, E. M. B. ARBERT & MARBERT: Deep bidirectional transformers
for Arabic. In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th
International Joint Conference on Natural Language Processing (Volume 1: Long Papers), 7088–7105 (2021).
43. Abdelali, A., Hassan, S., Mubarak, H., Darwish, K. & Samih, Y. Pre-training bert on arabic tweets: Practical considerations.
arXiv preprint arXiv:2102.10684 (2021).
44. Mubarak, H., Hassan, S. & Chowdhury, S. A. Emojis as anchors to detect arabic offensive language and hate speech. Nat.
Lang. Eng. 29, 1436–1457 (2023).
45. Abdellaoui, I. et al. Investigating offensive language detection in a low-resource setting with a robustness perspective.
Big Data Cogn. Comput. 8, 170 (2024).
46. Aghzal, M., El Bouni, M. A., Driouech, S. & Mourhir, A. Compact transformer-based language models for the moroccan
darija. In 2023 7th IEEE Congress on Information Science and Technology (CiSt), 299–304 (IEEE, 2023).
47. Alajmi, A., Ahmad, I. & Mohammed, A. Evaluating the adversarial robustness of arabic spam classifiers. Neural Comput.
Appl. 1–21 (2024).
48. Almeida, T. A., Hidalgo, J. M. G. & Yamakami, A. Contributions to the study of sms spam filtering: new collection and
results. In Proceedings of the 11th ACM symposium on Document engineering, 259–262 (2011).
49. Hassan, S. I., Elrefaei, L. & Andraws, M. S. Arabic tweets spam detection based on various supervised machine learning
and deep learning classifiers. MSA Eng. J. 2, 1099–1119 (2023).
50. Kaddoura, S. & Henno, S. Dataset of arabic spam and ham tweets. Data Brief 52, 109904 (2024).
51. Alshahrani, N., Alshahrani, S., Wali, E. & Matthews, J. Arabic synonym BERT-based adversarial examples for text
classification. 137–147 (Association for Computational Linguistics, 2024).
52. Kim, Y. Convolutional neural networks for sentence classification. In Proceedings of the Conference on Empirical
Methods in Natural Language Processing, 1746–1751 (2014).
53. Hochreiter, S. & Schmidhuber, J. Long short-term memory. Neural Comput. 9, 1735–1780 (1997).
54. Boujou, E. et al. An open access nlp dataset for arabic dialects: Data collection, labeling, and model construction. arXiv
preprint arXiv:2102.11000 (2021).
55. Nakhleh, S., Qasaimeh, M. & Qasaimeh, A. Character-level adversarial attacks evaluation for arabert’s. In 2024 15th
International Conference on Information and Communication Systems (ICICS), 1–6 (IEEE, 2024).
56. Radman, A. & Duwairi, R. Towards a robust deep learning framework for arabic sentiment analysis. Nat. Lang. Process.
1–35 (2024).
57. Chung, J., Gulcehre, C., Cho, K. & Bengio, Y. Empirical evaluation of gated recurrent neural networks on sequence
modeling. arXiv preprint arXiv:1412.3555 (2014).
58. LeCun, Y., Bottou, L., Bengio, Y. & Haffner, P. Gradient-based learning applied to document recognition. Proc. IEEE 86,
2278–2324 (1998).
59. Vaswani, A. Attention is all you need. Adv. Neural Inf. Process. Syst. (2017).
60. Aly, M. & Atiya, A. LABR: A large scale Arabic book reviews dataset. 494–498 (Association for Computational
Linguistics, Sofia, Bulgaria, 2013).
61. Alshemali, B. Sentence-level adversarial examples in arabic. In Computational Science and Computational Intelligence,
228–242 (Springer Nature Switzerland, Cham, 2025).
62. Li, L., Ren, K., Shao, Y., Wang, P. & Qiu, X. Perturbscore: Connecting discrete and continuous perturbations in nlp. In
Findings of the Association for Computational Linguistics: EMNLP 2023 (2023).
63. Lu, X. et al. Evaluating saliency explanations in nlp by crowdsourcing. In Proceedings of the 2024 Conference on
Language Resources and Evaluation (LREC) (2024).
64. Gao, X., Zhang, J., Mouatadid, L. & Das, K. Spuq: Perturbation-based uncertainty quantification for large language
models. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP) (2024).
/
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 18 ---

65. Gómez-Talal, I. A study on efficient perturbation-based explanations. Eng. Appl. Artif. Intell. 155, 110664 (2025).
66. Garg, S. & Ramakrishnan, G. BAE: BERT-based adversarial examples for text classification. In Proceedings of the 2020
Conference on Empirical Methods in Natural Language Processing (EMNLP), 6174–6181 (Association for Computational
Linguistics, 2020).
67. Maheshwary, R., Maheshwary, S. & Pudi, V. A context aware approach for generating natural language attacks. In
Proceedings of the AAAI conference on artificial intelligence, vol. 35, 15839–15840 (2021).
68. Ren, S., Deng, Y., He, K. & Che, W. Generating natural language adversarial examples through probability weighted
word saliency. In The Annual Meeting of the Association for Computational Linguistics, 1085 –1097 (2019).
69. Jin, D., Jin, Z., Zhou, J. T. & Szolovits, P. Is bert really robust? a strong baseline for natural language attack on text
classification and entailment. In Proceedings of the AAAI conference on artificial intelligence, vol. 34, 8018–8025 (2020).
70. Simonyan, K., Vedaldi, A. & Zisserman, A. Deep inside convolutional networks: Visualising image classification models
and saliency maps. arXiv preprint arXiv:1312.6034 (2014).
71. Sundararajan, M., Taly, A. & Yan, Q. Axiomatic attribution for deep networks. In Proceedings of the 34th International
Conference on Machine Learning, 3319–3328 (2017).
72. Vaswani, A., Shazeer, N., Parmar, N. et al. Attention is all you need. In Advances in Neural Information Processing
Systems, 5998–6008 (2017).
73. Yang, A. et al. Qwen3 technical report. arXiv preprint arXiv:2505.09388 (2025).
74. Altakrori, M. H., Habash, N., Freihat, A., Samih, Y. et al. Dialectalarabicmmlu: Benchmarking dialectal capabilities in
arabic and multilingual language models. arXiv preprint (2025). ArXiv:2510.27543.
75. Darwish, K., Ali, A. et al. Proceedings of the third arabic natural language processing conference. In ArabicNLP 2025
(Association for Computational Linguistics, 2025).
76. Abdul-Mageed, M. et al. NADI 2024: The fifth nuanced Arabic dialect identification shared task. In Proceedings of the
Second Arabic Natural Language Processing Conference, 709–728 (2024).
77. Niu, T. & Bansal, M. Adversarial over-sensitivity and over-stability strategies for dialogue models. In Proceedings of the
22nd Conference on Computational Natural Language Learning, 486–496 (Association for Computational Linguistics,
Brussels, Belgium, 2018).
78. Lin, J. C.-W., Shao, Y., Djenouri, Y. & Yun, U. Asrnn: A recurrent neural network with an attention model for sequence
labeling. Knowledge-Based Syst. 212, 106548 (2021).
79. Ye, M., Miao, C., Wang, T. & Ma, F. Texthoaxer: Budgeted hard-label adversarial attacks on text. In Proceedings of the
AAAI Conference on Artificial Intelligence, vol. 36, 3877–3884 (2022).
80. Li, Y., Li, Z., Gao, Y. & Liu, C. White-box multi-objective adversarial attack on dialogue generation. In Proceedings
of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 1778–1792
(Association for Computational Linguistics, Toronto, Canada, 2023).
81. Hussain, A. & Al-Harbi, S. A comparative study of deep learning approaches for arabic language processing. Jordanian
J. Electr. Eng. 9, 199–210 (2023).
82. Ahmad, S. & Syed, A. Cnn and lstm based hybrid deep learning model for sentiment analysis on arabic text reviews.
Mehran Univ. Res. J. Eng. Technol. 43, 23–30 (2024).
83. Zahidi, A., Al-Amrani, Y. & El Younoussi, Y. Deep learning cnn–lstm hybrid approach for arabic sentiment analysis
using word embedding models. Int. J. Mod. Educ. Comput. Sci. 17, 52–64 (2025).
84. Hassani, H., Ait Hammou, M. & El Alaoui, A. Boosting arabic text classification using hybrid deep learning approach.
SN Appl. Sci. 7, 425–439 (2025).
85. McNemar, Q. Note on the sampling error of the difference between correlated proportions or percentages. Psychometrika
12, 153–157 (1947).
86. Nassif, A. B., Darya, A. M. & Elnagar, A. Empirical evaluation of shallow and deep learning classifiers for arabic
sentiment analysis. Transactions on Asian Low-Resource Lang. Inf. Process. 21, 1–25 (2021).
87. Yuan, L., Zheng, X., Zhou, Y., Hsieh, C. & Chang, K.-W. On the transferability of adversarial attacks against neural
text classifier. In Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP),
1612–1625 (2021).
/
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

--- Page 19 ---

88. Miyajiwala, A., Ladkat, A., Jagadale, S. & Joshi, R. On sensitivity of deep learning based text classification algorithms to
practical input perturbations. arXiv preprint arXiv:2201.00318 (2022).
89. Alsaeed, S., Alqahtani, A. & Alharthi, F. A comparative study of effective approaches for arabic sentiment analysis. Inf.
Process. & Manag. 60, 103304 (2023).
90. Kudo, T. Subword regularization: Improving neural network translation models with multiple subword candidates. In
Proceedings of ACL (2018).
91. Bostrom, K. & Durrett, G. Byte pair encoding is suboptimal for language model pretraining. In Proceedings of EMNLP
(2020).
92. Wallace, E., Feng, S., Kandpal, N., Gardner, M. & Singh, S. Universal adversarial triggers for attacking and analyzing
nlp. In Proceedings of EMNLP-IJCNLP (2019).
93. Serrano, S. & Smith, N. A. Is attention interpretable? In Proceedings of ACL (2019).
94. Hendrycks, D., Liu, X., Wallace, E. et al. Pretrained transformers improve out-of-distribution robustness. In Proceedings
of the 58th Annual Meeting of the Association for Computational Linguistics (ACL) (2020).
95. Ribeiro, M. T., Wu, T., Guestrin, C. & Singh, S. Beyond accuracy: Behavioral testing of nlp models with checklist. In
Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL) (2020).
96. Behnstedt, P. & Woidich, M. Die ägyptisch-arabischen Dialekte, vol. 1-5 (L. Reichert, 1985).
97. Woidich, M. The coptic substratum of egyptian arabic. Romano-Arabica 6, 173–189 (2006).
98. Versteegh, K. The Arabic Language (Edinburgh University Press, 2014), 2nd edn.
99. Badawi, E., Carter, M. & Gully, A. Modern Written Arabic: A Comprehensive Grammar (Routledge, 2004).
100. Watson, J. C. E. The Phonology and Morphology of Arabic (Oxford University Press, 2002).
101. Al-Wer, E. The arabic dialect continuum revisited. Arab. Sociolinguistics 9–24 (2014).
102. Kwaik, K. A., Saad, M., Chatzikyriakidis, S. & Dobnik, S. A lexical distance study of arabic dialects. Procedia Comput.
Sci. 142, 157–164 (2018).
103. Bouamor, H., Habash, N., Salameh, M., Zaghouani, W. & Rambow, O. The madar arabic dialect corpus and lexicon. In
Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC) (2018).
104. Inoue, G., Khalifa, S. & Habash, N. Morphosyntactic tagging with pre-trained language models for arabic and its dialects.
arXiv preprint arXiv:2110.06852 (2021).
105. Broselow, E., Saiegh-Haddad, E. & Spolsky, B. Perspectives on Arabic Linguistics: Papers from the Annual Symposia on
Arabic Linguistics (John Benjamins Publishing Company, 2008).
8 Author contribution
The author B.A. solely conducted the study, designed the methodology, conceived the experiments, conducted the analysis,
interpreted the results, and wrote the manuscript.
9 Data availability
Two publicly available Arabic datasets are employed in the present study. The first dataset is HARD, introduced by Elnagar
et al. and released as a benchmark for Arabic sentiment analysis, which is accessible via the authors’ official repository
(https://github.com/elnagara/HARD-Arabic-Dataset). The second dataset is SANAD, proposed by Einea et
al., which consists of labeled Arabic news articles for text categorization and is available through the Mendeley Data repository
(https://data.mendeley.com/datasets/57zpx667y9/2).
10 Funding Declaration
The authors declare that no funding was received to support the research, authorship, or publication of this paper.
/
ACCEPTED MANUSCRIPT
ARTICLE IN PRESS
ARTICLE IN PRESS

```
